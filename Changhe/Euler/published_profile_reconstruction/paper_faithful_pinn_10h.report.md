# Result

**The requested measured optimization campaign is complete, but the published high-accuracy Euler profile was not reproduced.** The campaign performed **36,611.873680 seconds (10.169965 accumulated hours)** of profile optimization, followed by completed independent **100-million-point full-domain audits of two preselected checkpoints**. All reported large-audit counts are actual evaluations; queueing, initialization, validation and reporting are excluded from optimizer time.

The three-equation aggregate candidate has full computational-domain RMS residuals **RU=3.9501e-4, ROmega=1.6873e-4 and RPsi=5.4855e-4**. Its differentiated-U RMS values are **d_rRU=3.0356e-5 and d_zRU=2.9195e-4**. The five-equation-balanced selection improves d_zRU to **1.7918e-4**, with slightly larger base-equation errors. The axial differentiated residual is approximately **100.7 / 61.8 times** the paper's Table S1 reference for the two candidates; neither reaches paper-level accuracy. The fields also differ substantially in amplitude and two-dimensional shape from the published profile. No convergence, exact full-plane solution, stability result or certification is claimed.

This was a direct three-field, FP64 PINN campaign with fixed lambda=1/2, free C, exact radial evenness, residual-gradient regularization, adaptive collocation/balancing, genuine SS-eSOAP and SS-Broyden, and frozen-stage boosting. The leading checkpoints descend from the independent signed PINN initialization. The strongest demonstrated obstruction is uneven spatial accuracy under finite collocation, accompanied by conditioning and unresolved profile/normalization choices.

All experimental artifacts are under **ROOT = `/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114`**. Previous research remains unchanged under `/resnick/groups/Hou-group/Changhe/agd_euler_reproduction_20261112T2213Z/reconstruction_20261113`. This report is the permanent Markdown result beside the prompt; source, environments, data, checkpoints and figures remain outside the prompt/report repository.

## A. Paper-method reproduction

This campaign reconstructs the PINN discovery procedure in [Ganeshram, Duruisseaux and Anandkumar, Sections 2.1–2.3 and Appendix B](https://arxiv.org/html/2609.10867v2), while identifying independent implementation choices. It does not equate undisclosed author settings with the settings below. The PINN represents U, Ω and Ψ directly; the paper's later two-head spline fit, which derives Ω elliptically, is a separate certification representation. No image-fitting term enters production training. Historical C_02 cycle0022 and C01 broad-tube cycle0009 provide field-only initialization; a separate signed initialization avoids dependence on them.

### Disclosure and implementation choices

| Element | Explicit paper disclosure | Confirmed released code/data | Reproduction choice |
|---|---|---|---|
| Representation | MLP in computational coordinates | No Euler training model found | Three-output tanh MLP; 32-wide, three hidden layers |
| Coordinates | Sinh map; box [0,30]×[−30,30] | Linked Lean identities | Input division by six; unrestricted trainable weights |
| Symmetry/parameters | Radial evenness, no z parity; FP64; free C | Lean equations | Symmetrized forward evaluation; λ fixed at 1/2 |
| PDE | Three profile equations | Lean transformed identities | Distinct loss components of the full coupled system |
| Far field | All fields decay at infinity | No profile download found | Separate far-volume field penalties |
| Nontriviality | Anti-collapse term | Expression unavailable | One-sided sampled U-energy floor |
| Smoothness | Gradient of PDE residual | Training details unavailable | Both physical derivatives of all three residuals |
| Adaptive weights | Balancing schedules | Schedule unavailable | Bounded gradient-norm balancing and EMA |
| Collocation | Refresh; core/axis; residual adaptation | Samples unavailable | Mixed random/grid/mined points and dynamic axis roots |
| SS-eSOAP | Initial curvature-aware optimizer | Public variant differs | Independent printed Algorithm 2 implementation |
| SS-Broyden | High-accuracy refinement | Urbán reference available | Dense SSBroyden1 with guarded line search |
| Boosting/validation | Frozen additive corrections; independent estimates | Euler numerical checkpoints unavailable | Plateau rule, wider correction sensitivity, separate physical evaluator |

The authors' linked [Lean repository](https://github.com/lean-dojo/Euler) verifies selected derivations; it does not supply the PINN architecture, trained weights or numerical profile in the inspected tree.

### Equations and verification

Set ξ=asinh(r), η=asinh(z), a=sechξ, b=sechη, t=tanhξ and q=tanhη. Independent differentiation gives

\[
f_r=af_\xi,\quad f_z=bf_\eta,\quad
f_{rr}=a^2(f_{\xi\xi}-tf_\xi),\quad
f_{zz}=b^2(f_{\eta\eta}-qf_\eta).
\]

For λ=1/2, define $A=t(\lambda-b\Psi_\eta)$ and $B=Cb+\lambda q+b(2\Psi+t\Psi_\xi)$. Appendix-B residuals become

\[
R_U=U-2Ub\Psi_\eta+A U_\xi+B U_\eta,
\]
\[
R_\Omega=(1+\lambda)\Omega-2UbU_\eta
+A\Omega_\xi+B\Omega_\eta,
\]
\[
R_\Psi=\Omega+a^2(\Psi_{\xi\xi}-t\Psi_\xi)
+\frac{3\Psi_\xi}{\sinh\xi\cosh\xi}
+b^2(\Psi_{\eta\eta}-q\Psi_\eta).
\]

Smooth radial evenness gives Ψξ=Ψξξ(0,η)ξ+O(ξ³), hence the axis formula

\[
R_\Psi(0,\eta)=\Omega+4\Psi_{\xi\xi}
+b^2(\Psi_{\eta\eta}-q\Psi_\eta).
\]

Safe denominators avoid invalid inactive autodiff branches. Symmetrization evaluates each network at ±ξ and averages, with no z reflection. C remains trainable through every correction stage. Coordinate input normalization does not fix a physical radial width.

The independent evaluator composes the model with asinh(r,z) and differentiates with respect to physical inputs, rather than importing training residuals. Compute-node checks reported maximum discrepancy 6.59×10⁻¹⁵ across residuals and their physical gradients. Manufactured tests cover the axis. A full-loss directional parameter finite-difference test includes residual-gradient smoothness and a frozen nonzero parent (relative tolerance 3×10⁻⁶, absolute 10⁻⁹). Parameter-only backward was also checked against ordinary backward with bitwise-identical active parameter gradients. These check implementation consistency; they do not establish convergence or a blowup theorem.

### Objective, sampling and boosting

S42 is implemented as separate equation means, residual-gradient means, far-field means, nontriviality, and additional axis equation means. For equation j, smoothness is the sample mean of [(∂rRj)²+(∂zRj)²]/2; it therefore requires third spatial derivatives of Ψ. Far-field fields are divided by fixed output scales. Distilled scales use teacher absolute-field 99th percentiles with lower floors (1,.01,1); independent initialization uses (2,1,4).

Nontriviality is

\[
L_{NT}=\left[\max\left(0,A_{min}-\sqrt{\langle U^2\rangle+10^{-20}}\right)\right]^2,
\]

sampled uniformly over ξ∈[0,5],η∈[−6,6]. Floors are 1 for C_02, .5 for C01 broad, and 2 for the independent branch. They neither prescribe −39 nor impose positivity. This fixed-box floor is scale-dependent and does not establish localization: the exact nondecaying family U=F(r), Ω=0, Ψ=z/2 satisfies the PDEs. Tail, width and transport diagnostics remain necessary.

The 13 component coefficients use base factors 1 for PDE/axis/FF/NT and .1 for smoothness. With component parameter-gradient norms gi and g* the geometric mean of the three PDE norms, desired coefficients are bi·clip(g*/gi,.1,10), with numerical norm floors. Updates use .9 previous+.1 desired. Raw losses, norms and coefficient histories are retained; PDE coefficients never vanish.

The initial code retained coefficients at monitoring/checkpoint times rather than every intervening refresh. The logging revision records every subsequent coefficient update in JSONL and saved checkpoint histories. That early logging gap is retained as a reproducibility limitation; no missing coefficient trajectory is reconstructed or claimed. SS-Broyden probe coefficients remain fixed throughout each objective block.

| Sampling configuration | PDE | Smoothness | Axis | FF | NT | Mining pool |
|---|---:|---:|---:|---:|---:|---:|
| Initial | 1024 | 128 | 128 | 128 | 256 | 8192 |
| Enlarged | 4096 | 512 | 256 | 256 | 512 | 65536 |
| High-batch SS-Broyden | 16384 | 2048 | 1024 | 1024 | 1024 | 131072 |
| Second GPU remine | 32768 | 4096 | 2048 | 2048 | 2048 | 262144 |

Broad-box, core and near-axis proposals are mixed. Mining adds normalized per-equation residual hotspots, a global grid and thin axial-plane proposals. Dynamic axis sampling retains at least half global coverage and adds current-model roots/hotspots with signed log-uniform physical offsets .001–10. Separate smoothness samples cover axis neighborhoods and residual peaks, with computational peak jitter .2. Far-field volume samples place ξ or signed η in [20,30], retaining the other coordinate throughout its box; these are finite proxies for decay, not finite-radius boundary equalities.

Main-run refresh intervals are 200 SS-eSOAP or 1000 SS-Broyden updates; secant/curvature history resets after objective changes. Dedicated SS-Broyden probes hold their newly mined batches and coefficients fixed throughout. No validation coordinates enter these samples.

Boosting freezes every earlier network, adds a zero-output correction, and evaluates the full nonlinear residual of the sum. The implementation uses six-report plateau comparisons, minimum stage duration 1200 optimizer seconds, and a correction scale derived from PDE MSE/output scales and clipped to [.01,.5]. Comparing changing weighted objectives makes this plateau heuristic imperfect. Wider 64×3 corrections are a capacity sensitivity choice; only C and the current correction train, giving 8708 active parameters including C (8707 in the correction network). Mixed capacities and legacy checkpoint loading have explicit regression tests.

### Optimizers and accuracy interpretation

[SS-eSOAP Algorithm 2](https://arxiv.org/html/2608.29448v1) uses gradient-covariance Kronecker factors, adaptive eigenbases, rotated momentum, variance downscaling and the raw-gradient secant factor τ, multiplying the eigenspace Adam update by τ⁻¹/². The implementation evaluates the inverse-Kronecker secant energy using current factors. Published defaults are β=(.9,.95), ε=10⁻⁸, check interval 1 and trigger .2. Independent choices are τmin=10⁻³, eigenvalue floor 10⁻¹², zero warmup/weight decay, and vector/scalar Adam fallback. Enlarged base learning rates are 5×10⁻⁴ for C01/independent and 5×10⁻⁵ for C02; restored states can carry smaller rates. A transactional growth guard (1.1 ceiling, eight attempts, halving) preserves raw gradients and rolls back rejected optimizer states.

The inspected [public SS-SOAP variant](https://github.com/al2wang/ss_esoap_nips) differs in τ application, denominator and gradient history; it was audited rather than silently substituted. Dense [SSBroyden1](https://github.com/jorgeurban/self_scaled_algorithms_pinns) uses strong-Wolfe bracketing/bisection, c1=10⁻⁴,c2=.9, 20 trials in campaign configurations, an explicit Armijo fallback, curvature rejection, identity restart and rollback. Main-run switching targets mean PDE MSE below 10⁻⁶ plus nontriviality; separate probes can start above that automatic threshold and are labeled sensitivity experiments, with their own trained-parent starting regime.

Validation keeps computational dξdη RMS, physical-area ball RMS and historical weighted measures separate. Two completed final audits each used 100 million fresh full-box points, with regional/axis/ball cohorts, saved coordinates/hashes and separate coordinate-only peak searches. Model parameters freeze while spatial derivatives remain active. Sampled RMS/maxima and refined local maxima remain empirical, never certificates or automatic evidence of equivalence to Table S1. Optimizer clocks exclude initialization, mining, validation, I/O and reporting; fresh-probe clocks do not recredit parent time.

## B. Optimization history and accounting

The completed campaign accumulated **36,611.873680 measured profile-optimizer seconds (10.169965 hours)**. This sums elapsed objective/gradient/step sections across concurrent branches, synchronized with CUDA where used. It excludes queueing, environment installation, field initialization, mining, coefficient refreshes, checkpoint I/O, validation, plotting and reporting. It is not elapsed campaign wall time or a normalized device-hour measure.

| Branch | Optimizer | Measured seconds | Research update counter | Final networks | Hardware |
|---|---|---:|---:|---:|---|
| C02 distilled | SS-eSOAP | 6868.350674 | 12048 | 6 | V100 16 GB |
| C01 broad distilled | SS-eSOAP | 11124.506446 | 23130 | 8 | V100 16 GB |
| Independent signed | SS-eSOAP | 11412.661768 | 20147 | 8 | V100 16 GB |
| Independent CPU curvature, including continuation | SS-Broyden | 1201.115791 | 686 | 2 | One CPU thread |
| C01 CPU curvature | SS-Broyden | 301.521691 | 185 | 2 | One CPU thread |
| Independently remined CPU curvature | SS-Broyden | 602.589723 | 216 | 2 | One CPU thread |
| First high-batch GPU curvature | SS-Broyden | 3300.366725 | 6217 | 2 | V100S 32 GB |
| Second GPU remine | SS-Broyden | 1800.760861 | 1914 | 2 | P100 16 GB |
| **Total** | | **36611.873680** | | | |

C02's 206.651434-second finite divergence is included once in its cumulative clock; recovery restored a stable early model and retained all discarded-path artifacts. Its final accepted-lineage counter is 10901 rather than the research counter 12048. The CPU continuation's 1201.115791 seconds already include the first 300.394099 seconds and are not added to them again. Fresh-objective probes start their own clocks at zero and retain parent time only as metadata. Even excluding the initial divergent C02 phase, recorded optimizer execution exceeds 36,000 seconds.

The user requirement was a global minimum, not 12,000 seconds on every initialization. C02 stopped after a full wider-correction block remained uncompetitive. Once the published cumulative total exceeded 36,000 seconds, the two primary processes received SIGTERM after their exact source paths and process identities were checked; both saved full state and exited normally. Their immutable configurations still show the original 12,000-second targets, which were **not** met individually. The final P100 curvature block then completed its 1800-second target. Stopped primary trainers skip their automatic final audit; the separate completed common screens and selected-profile audits provide the independent comparison.

True frozen boosting executed on all primary branches. The strongest curvature candidates descend from an early independent two-network stage and train only C plus the current 2307-parameter correction, giving 2308 active parameters and a saved dense inverse Hessian. C02's best retained profile comes from the completed first 64-wide correction block; its just-added later correction is preserved separately. More frozen stages and a wider correction did not uniformly improve independent residuals.

The original CPU SS-Broyden continuation showed overfitting of a fixed spatial objective, motivating fresh mined data and curvature restarts. The first 16384-point GPU block improved full-domain RU/Omega/Psi RMS on identical before/after coordinates from (.00204734,.000823096,.00162504) to (.000389472,.000166818,.000562864). Its old-center radius-.1 ball also improved, but its transport root moved from -.78951 to +.23092; those paired balls do not measure the new root neighborhood. The second 32768-point block improved Omega, Psi, axial RU gradients and peak control while worsening RU and radial RU gradients. These tradeoffs motivate separate final selections.

Full clocks, configurations, coefficient histories, line-search traces, checkpoints, Stage A/B records and Euler-only scheduler accounting are retained outside this repository. Detailed provenance is in ROOT/research/optimizer_results_draft.md, final_accounting_review.md and euler_sacct_provisional.txt. The first unguarded C02 failure, one pre-readiness audit exit and an early plotting-only orchestration failure were preserved and corrected; queue time and audits receive no profile-optimizer credit.

## C. Retained candidates and selection

The completed final common screening evaluated **211 checkpoint paths representing 116 unique profiles**; 95 paths were duplicates, and every evaluated profile had finite metrics. Deduplication used actual model tensors, buffers, stage architecture and additive coefficients, excluding optimizer/history metadata. Every original label, selection reason and native checkpoint alias remains retained. The [checkpoint index](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/best_checkpoint_index.json) groups 10 distinct criterion winners and records their expected hashes, measures, counts, root centers and source provenance.

Two distinct criteria were declared before sampling grand seed 742631887: the three-equation aggregate
`RMS(RU)^2+RMS(ROmega)^2+RMS(RPsi)^2`, and a five-equation minimax
`max_i(RMS_i/T_i)`, where the five quantities are RU, d_rRU, d_zRU, ROmega and RPsi and the fixed normalization values T_i are the recorded Table S1 references. These are reproduction/selection choices, not author-prescribed rankings or error certificates. They selected two older high-batch GPU SS-Broyden states, original steps 6217 and 4638, respectively. Additional P100 optimization improved individual/regional criteria but did not displace those two aggregate selections.

The table reports **screening**, not grand-audit, scores: 65,536 common points uniform in computational `(xi,eta)` on `[0,30]×[-30,30]`, seed 613842917; each listed regional set has 8,192 points. Ball entries show computational/physical-area scores separately. Source steps belong to their respective branches.

| Criterion | Model ID | Source step | Screening score | Source NT floor / fresh U RMS |
|---|---|---:|---:|---:|
| Three-equation aggregate | model_019_6c45bab89cc7 | 6217 | 4.34423e-7 | 2 / 1.99716 |
| Normalized five minimax | model_060_3ed07bd69c9b | 4638 | 57.9401 | 2 / 1.99321 |
| RU RMS | model_071_7ff7a2e41a88 | 5905 | 3.84705e-4 | 2 / 1.99475 |
| ROmega RMS | model_074_5af9479e77fe | 1914 | 1.04841e-4 | 2 / 1.99929 |
| RPsi RMS | model_095_e8e61c0886c1 | 1364 | 4.77625e-4 | 2 / 1.99856 |
| d_rRU RMS | model_004_846003d17c15 | 9919 | 1.47851e-5 | .5 / .504011 |
| d_zRU RMS | model_060_3ed07bd69c9b | 4638 | 1.68026e-4 | 2 / 1.99321 |
| Three-equation sampled maximum, full/all regions | model_083_68908f2a5eae | 585 | .00761672 | 2 / 1.99700 |
| Own-root radius .1 aggregate | model_065_4cecc7be7252 | 5212 | 6.31198e-11 / 6.18614e-11 | 2 / 1.99394 |
| Own-root radius 1 aggregate | model_075_0f5e25ef6bb7 | 63 | 6.94938e-9 / 7.52632e-9 | 2 / 1.99795 |
| Own-root radius 10 aggregate | model_019_6c45bab89cc7 | 6217 | 6.53869e-8 / 1.44104e-7 | 2 / 1.99716 |

Ball centers differ between models: the radius 0.1, 1 and 10 winners are centered at physical z ≈ 0.434675, 0.230801 and 0.230921. They are **not identical physical-region comparisons**. Axis, far-field and core auxiliary winners and both maximum definitions are separately indexed. The maximum-winner estimates use the completed 65,536-point full screen and 8,192-point regional cohorts; this candidate did not receive a 100M audit.

Energy admission required fresh U RMS ≥ **0.8 times each recorded source floor**, using the same computational energy measure as that source's nontriviality mechanism. This is a diagnostic admission rule, not a new training-loss target. The low d_rRU C01 winner has U(0,0) ≈ −0.526, compared with ≈ −2.67 for the primary selections; its lower floor is a material comparison confound. Neither energy admission nor these residual rankings establishes correct amplitude, localization or solution-branch identity. The C02 distilled initial MLP remains a qualitative historical shape reference only; **no verified shape-fidelity winner was found**.

Supplemental CPU audits with one million full-domain points for the Omega and Psi winners completed with **1,981,841 streamed points across 15 regions each**, all finite, and zero optimizer-time credit. Their full-domain `(RU,ROmega,RPsi)` RMS values were respectively `(.000488812,.000103625,.000479330)` and `(.000562909,.000123150,.000477583)`. Their full-coordinate SHA256 is identical, beginning `f49eba22ec30`, and matches the preceding four-candidate 1M audit. Exact counts, hashes and measures remain in the [Omega audit](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/supplement_finalcriteria/Omega/validation.json) and [Psi audit](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/supplement_finalcriteria/Psi/validation.json).

Immutable grand evaluation copies are [overall_three.pt](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/checkpoints/final_inputs/independent_ssb_gpu/overall_three.pt) and [normalized_five.pt](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/checkpoints/final_inputs/independent_ssb_gpu/normalized_five.pt). These lightweight model archives support evaluation; exact native optimizer restarts use their separately retained `*_full_state.pt` copies. The [frozen-input manifest](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/research/grand_inputs_20261114T1318Z.json) and index give full paths and verified expected hashes for both kinds, preserving all original native aliases without conflating model-only and restart payloads.

## D. Independent final accuracy

Two profiles were selected by the preregistered criteria before consuming the fresh grand-validation seed: **A**, minimum three-equation full-box sum of squared RMS; **B**, minimum worst normalized RMS across the five Table S1 residuals. Both are frozen stage-1 high-batch SS-Broyden profiles: A at step 6,217 (3,300.366725 optimizer seconds), B at step 4,638 (2,471.087054 seconds). These clocks describe source profiles, not additional training or validation credit.

Each completed FP64 audit evaluated **100,000,000 full-box points**, seed **742631887**, batch **16,384**, and **100,981,841 streamed residual points** including regional/historical cohorts. Both use the same full, axis, far-field and narrow-core coordinates; the full-coordinate SHA256 is `0205e70fdc3ddba2796748890fe0be48281ae6582fbe2f82df06feb7fdf65731`. Thus these are two model evaluations of a common 100M draw, not 200M unique full-box coordinates. Every profile parameter remained frozen and before/after parameter hashes matched.

Write ξ=asinh(r), η=asinh(z). Full sampling is uniform dξdη on [0,30]×[−30,30], axis uniform dη at ξ=0, far field uniform on [10,30]×([−30,−10]∪[10,30]), and core conditioned on 0≤r≤10, |z|≤6000. Each fresh axis/far-field/core/ball cohort has 100,000 points. Balls have physical radii 0.1, 1 and 10 about each profile’s own axis transport root: A (0,0.2309207670), B (0,0.5761396088). “Comp” conditions uniform dξdη on the physical half-ball; “area” is uniform physical dr dz, not cylindrical volume. Different root centers mean the two ball cohorts differ despite matching generation seeds.

All following accuracy cells are **RMS / sampled maximum absolute residual**, rounded to three significant digits. Radial derivatives vanish on the smooth-even axis by construction.

**Profile A**

| Region | R_U | ∂r R_U | ∂z R_U | R_Ω | R_Ψ |
| --- | --- | --- | --- | --- | --- |
| Full | 0.000395 / 0.0077 | 3.04e-05 / 0.000881 | 0.000292 / 0.014 | 0.000169 / 0.00257 | 0.000549 / 0.0218 |
| Axis | 3.89e-05 / 0.000308 | 0 / 0 | 2.07e-05 / 0.000153 | 2.41e-05 / 0.000143 | 4.89e-05 / 0.000267 |
| Far field | 0.000167 / 0.00226 | 6.9e-09 / 1.93e-07 | 2.56e-08 / 1.12e-06 | 6.04e-05 / 0.00116 | 3.52e-05 / 0.000586 |
| Core | 0.000211 / 0.00119 | 0.000131 / 0.000881 | 0.00011 / 0.000872 | 9.53e-05 / 0.000433 | 0.000299 / 0.00196 |
| Ball 0.1 comp | 7.57e-06 / 1.54e-05 | 1.86e-06 / 5.28e-06 | 0.00014 / 0.000155 | 2.23e-06 / 3.61e-06 | 5.27e-06 / 1.25e-05 |
| Ball 1 comp | 2.56e-05 / 5.64e-05 | 3.19e-05 / 8.37e-05 | 0.000103 / 0.000191 | 2.52e-05 / 6.93e-05 | 9.24e-05 / 0.000198 |
| Ball 10 comp | 0.000117 / 0.000438 | 8.74e-05 / 0.00025 | 0.000192 / 0.000871 | 6.45e-05 / 0.000284 | 0.000214 / 0.00118 |
| Ball 0.1 area | 7.58e-06 / 1.54e-05 | 1.85e-06 / 5.27e-06 | 0.00014 / 0.000155 | 2.24e-06 / 3.61e-06 | 5.29e-06 / 1.25e-05 |
| Ball 1 area | 2.61e-05 / 5.64e-05 | 3.2e-05 / 8.36e-05 | 0.000105 / 0.000191 | 2.55e-05 / 6.93e-05 | 9.66e-05 / 0.000198 |
| Ball 10 area | 0.000152 / 0.000438 | 9.66e-05 / 0.00025 | 0.000194 / 0.000872 | 7.51e-05 / 0.000285 | 0.000338 / 0.00118 |

**Profile B**

| Region | R_U | ∂r R_U | ∂z R_U | R_Ω | R_Ψ |
| --- | --- | --- | --- | --- | --- |
| Full | 0.000403 / 0.0083 | 3.65e-05 / 0.000861 | 0.000179 / 0.00707 | 0.000187 / 0.00229 | 0.000559 / 0.0165 |
| Axis | 4.2e-05 / 0.000233 | 0 / 0 | 2.31e-05 / 0.000137 | 2.97e-05 / 0.000191 | 3.76e-05 / 0.000291 |
| Far field | 0.000199 / 0.00387 | 7.48e-09 / 1.54e-07 | 2.18e-08 / 4.15e-07 | 6.38e-05 / 0.000993 | 3.85e-05 / 0.00043 |
| Core | 0.000214 / 0.00158 | 0.000144 / 0.000822 | 0.000104 / 0.00058 | 0.000113 / 0.000568 | 0.000369 / 0.00273 |
| Ball 0.1 comp | 2.75e-05 / 3.58e-05 | 1.22e-05 / 2.43e-05 | 9.98e-05 / 0.000128 | 3.44e-06 / 5.33e-06 | 1.62e-05 / 2.41e-05 |
| Ball 1 comp | 4.09e-05 / 0.000119 | 8.11e-05 / 0.000224 | 0.000124 / 0.000325 | 3.47e-05 / 9.02e-05 | 0.000133 / 0.000282 |
| Ball 10 comp | 0.000123 / 0.000412 | 0.000103 / 0.000281 | 0.000181 / 0.00058 | 8.02e-05 / 0.000364 | 0.000264 / 0.00134 |
| Ball 0.1 area | 2.76e-05 / 3.58e-05 | 1.21e-05 / 2.43e-05 | 9.95e-05 / 0.000128 | 3.44e-06 / 5.33e-06 | 1.61e-05 / 2.41e-05 |
| Ball 1 area | 4.06e-05 / 0.000119 | 7.74e-05 / 0.000224 | 0.000124 / 0.000325 | 3.54e-05 / 9.02e-05 | 0.000145 / 0.000282 |
| Ball 10 area | 0.000145 / 0.000412 | 9.77e-05 / 0.000281 | 0.000166 / 0.00058 | 0.000103 / 0.000369 | 0.000405 / 0.00134 |

The full-box three-equation squared-RMS sums are A **4.8540e−7**, B **5.0984e−7**. B improves the axial residual derivative substantially while slightly worsening all three undifferentiated full-box RMS values. Neither profile reproduces all [paper Table S1](https://arxiv.org/html/2609.10867v2) targets:

| Residual | Paper RMS / max | A/paper RMS / max | B/paper RMS / max |
| --- | --- | --- | --- |
| R_U | 4.2e-05 / 0.0036 | 9.4 / 2.14 | 9.59 / 2.31 |
| ∂r R_U | 0.00012 / 0.0083 | 0.253 / 0.106 | 0.304 / 0.104 |
| ∂z R_U | 2.9e-06 / 0.00013 | 101 / 108 | 61.8 / 54.4 |
| R_Ω | 1.7e-05 / 0.00095 | 9.93 / 2.7 | 11 / 2.42 |
| R_Ψ | 3.8e-05 / 0.0014 | 14.4 / 15.6 | 14.7 / 11.8 |

The dominant relative gap is ∂z R_U: about **101×** the paper RMS for A and **61.8×** for B. Conversely ∂r R_U is below the paper reference. These compare finite-sample statistics and do not establish equal author implementation, approximation error, or certified suprema.

Root diagnostics also remain nonzero. A has C=3.64658918, U(0,0)=−2.67352429; B has C=1.67892290, U(0,0)=−2.66419992. At their respective roots, the signed defects [Ψ_z−1/2, 1.5Ω−2UU_z, 1.5U_z−2UΨ_zz] are A [5.79e−7, −1.80e−6, −1.43e−4], B [−5.24e−6, 2.79e−6, −9.83e−5]. Sign-change scans can miss tangent roots.

Separate coordinate-only local searches used **545 targeted points for A** and **457 for B**. Their observed three-equation peaks and physical locations are below; searches range over the full computational box and are not restricted to starting balls. Targeted points enter neither RMS nor the streamed counts; profile optimizer credit is zero. These observed peaks are not global certificates.

| Profile / equation | Refined absolute residual | Physical (r,z) |
| --- | --- | --- |
| A / R_U | 0.0077 | (250,53.7) |
| A / R_Ω | 0.00257 | (1.21e+03,-0.892) |
| A / R_Ψ | 0.0218 | (2.4e+03,-0.141) |
| B / R_U | 0.0083 | (409,-90.6) |
| B / R_Ω | 0.00229 | (750,-57.9) |
| B / R_Ψ | 0.0165 | (2.25e+03,-0.117) |

**Exact historical-coordinate comparison.** The following RMS values use the same stored 32,768 common-asinh points as the old 35-profile audit: uniform asinh(r), asinh(z) on physical [0,20000]×[−20000,20000], historical generation seed 7349911; archive SHA256 `1704bba81462973f5a8ab4faccde90e89a05dd809cacce1b180728693da25954`. Eight representative old rows preserve original starts, earlier retained/control milestones and componentwise bests; the linked artifact contains all 35 plus every historical region. These are reused comparison coordinates, distinct from the fresh full-box measure.

| Profile | R_U RMS | R_Ω RMS | R_Ψ RMS | rR_Ω RMS |
| --- | --- | --- | --- | --- |
| Original C01 | 0.698 | 0.00801 | 5.68e-16 | 5.58 |
| Original C02 | 0.479 | 0.00569 | 6.11e-16 | 4.73 |
| Strict C02 persistent cycle0022 | 0.0248 | 0.000604 | 5.20e-14 | 0.267 |
| Historical 0734 | 0.00237 | 0.0104 | 3.18e-19 | 0.234 |
| Old latest (best rRΩ) | 0.013 | 0.0136 | 7e-18 | 0.0773 |
| Old retained (best RU) | 0.00137 | 0.00416 | 3.49e-19 | 0.44 |
| Prior dense escape (best RΩ) | 0.00276 | 0.000336 | 2.2e-15 | 0.317 |
| Broad C01 tube cycle0009 | 0.0129 | 0.000458 | 4.03e-15 | 0.278 |
| A grand | 0.000838 | 0.000359 | 0.00145 | 1.63 |
| B grand | 0.000845 | 0.0004 | 0.00145 | 1.85 |

A/B improve historical R_U below every old profile. Their unweighted R_Ω is lower than the original starts and old weighted-norm winner, but remains above **prior dense escape**. Old ansätze structurally closed the Poisson equation, giving near-roundoff R_Ψ; the independent three-head MLP does not. Weighted vorticity RMS is A **1.629**, B **1.849**, versus the old minimum **0.07734**. Fresh full-box rR_Ω RMS is A **8.227e7**, B **8.744e7**; its different units and radial emphasis make it a separate diagnostic, not the Table S1 vorticity norm.

Eight-digit values, all sampled-maximum locations, additional historical cohorts, frozen-state hashes and timing are retained in [A tables](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/research/grand_overall_three_tables.md), [B tables](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/research/grand_normalized_five_tables.md), their linked completed validation JSON files, and the [35-profile historical comparison](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/research/final_historical_comparison_20261114T1332Z/comparison.json). Optional ∂rR_Ψ and separate high-precision C02 checks do not certify all five derivative errors.

## E. Two-dimensional profiles, transport and localization

Both selected profiles have a negative U core, sign-changing Omega/Psi, and similar observed-scale geometry. Their sampled |U| peaks are **2.676 and 2.668**, far below the published amplitude near 39. Ordinary isotropic spatial scaling and axial translation preserve U amplitude, so adjusting those gauges cannot repair this discrepancy. The displayed Omega/Psi sign patterns and raw amplitudes also differ from the published panels. Those panels are original perspective rasters with different windows and colorbars; no numerical author profile was available for a quantitative two-dimensional comparison. These observations do not establish reproduction from axis cross-sections or visual resemblance.

The following artifacts retain raw fields and explicit coordinate/color scales:

| Selection | Observed physical core | Broad physical window | Full computational box | Published comparison |
|---|---|---|---|---|
| Three-equation | [Observed](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_overall_three/euler-pinn-grand-three-e743cacc8859-6897020/plots/observed_physical.png) | [Broad](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_overall_three/euler-pinn-grand-three-e743cacc8859-6897020/plots/broad_physical.png) | [Computational](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_overall_three/euler-pinn-grand-three-e743cacc8859-6897020/plots/full_computational.png) | [Qualitative only](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_overall_three/euler-pinn-grand-three-e743cacc8859-6897020/plots/qualitative_published_comparison.png) |
| Normalized-five | [Observed](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_normalized_five/euler-pinn-grand-five-cee5b2646649-6897030/plots/observed_physical.png) | [Broad](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_normalized_five/euler-pinn-grand-five-cee5b2646649-6897030/plots/broad_physical.png) | [Computational](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_normalized_five/euler-pinn-grand-five-cee5b2646649-6897030/plots/full_computational.png) | [Qualitative only](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/validation/grand_normalized_five/euler-pinn-grand-five-cee5b2646649-6897030/plots/qualitative_published_comparison.png) |

Small positive U lobes appear outside the observed core: sampled maxima **0.00365 / 0.00357**, around r=6680,z=−259, approximately 0.14% of the core amplitude. A black zero contour through an almost white region can therefore mark a tiny sign change, not a large positive lobe. The broad/full views are necessary to see these features.

Independent axis searches found the following roots and compatibility defects. Columns retain the two selections separately; their own-root balls have different centers.

| Axis quantity | Three-equation | Normalized-five |
|---|---:|---:|
| z* | 0.2309207670 | 0.5761396088 |
| 1.5Omega−2U Uz | −1.79839e-6 | 2.79458e-6 |
| 1.5Uz−2U Psi_zz | −1.43084e-4 | −9.83479e-5 |
| RPsi | 3.01913e-6 | −1.31586e-5 |

Psi_z−.5 at these roots is +5.79e-7 / −5.24e-6: the expected nearly degenerate radial transport is approximately present, but the differentiated compatibility defect remains nonzero.

Finite global/core searches retained **9 / 5 off-axis numerical candidates**: **5 / 2** have two positive computed transport eigenvalues and **4 / 3** are saddles. Other attempts were nonconverged, duplicated, above tolerance or ill-conditioned. Representative outgoing candidates are (r,z)=(248.7100,−1.61028), eigenvalues (0.0972792,1.402721), and (235.1655,−0.554675), eigenvalues (0.0696757,1.430324). Their (ROmega,RPsi,d_zRU) defects are respectively **(1.88688e-4,−3.94296e-4,−2.34530e-4)** and **(1.63680e-4,5.36930e-4,−5.22226e-4)**. Near-zero transport/RU does not eliminate these defects. Several other candidates have weak radial eigenvalues and worse conditioning. These are roots of the approximate networks found by a bounded search, not certified complete root counts, isolation, outgoing geometry or stability of an exact Euler solution.

Radial resolution checks at physical z=0 used 257 and 513 log-radial points. U's first half-axis-amplitude crossings were **27.929065→27.927345** and **28.880051→28.847248**, changes of about 0.0062% and 0.114%. These finite checks support limited radial sampling stability; they are not certified convergence. Localization's separate sampled radial widths were 28.00 / 28.94 and axial full widths **265.92 / 243.06**, with uncensored crossings. The latter use one interpolation mesh; no multi-resolution axial study or peak-z radial scan is recorded.

On the active observed core, RMS(Psi_z−.5) is **0.2515 / 0.2530**, and RMS(U_z) is **0.00508 / 0.00555**. Together with nonzero Omega, these do not support identifying either profile with the exact axially constant family U=F(r), Omega=0, Psi=z/2. Energy admission alone does not determine target identity.

Sampled axial-ray fields are small near the trained boundary, but maximum |U| over the fixed-r rays rises from **1.17e-4 / 3.71e-4 at |eta|30** to **0.0175 / 0.0229 at |eta|40**. The latter is extrapolation beyond training. It leaves decay at infinity unresolved without proving eventual divergence. Viewing meshes, root searches and these targeted rays receive **zero residual-RMS and optimizer-time credit**; none supplies certification.

## F. Failure analysis and limitations

The strongest demonstrated barrier is uneven spatial accuracy under finite collocation. An exact continuation of the original independent CPU SS-Broyden objective reduced training RU MSE from 1.204706e-6 to 3.583795e-7, while RU RMS on identical independent full-domain coordinates rose from .00318885 to .00583461 and its sampled maximum rose from .0689443 to .160983. Its narrow-core residuals and fixed local ball improved at the same time. This is a controlled spatial generalization tradeoff, not a line-search failure: all 686 recorded CPU updates satisfied strong Wolfe conditions. The later freshly mined/larger CPU objective improved full RU by 35.2% and Omega by 31.7%, but again traded off some narrow-core errors. Sampling, balancing, curvature restart and optimization duration changed together in that intervention, so its effect cannot be assigned exclusively to batch size.

Conditioning and incomplete loss balance also have direct evidence. Unguarded C02 proposals grew to enormous finite residuals without triggering a nonfinite check; an objective-growth guard and lower learning rates were needed. At later refreshes, raw RU/Omega gradient norm ratios exceeded 1600 for C02 and 2600 for C01, beyond what the bounded coefficient range could equalize. The independent branch had much closer equation-gradient norms and still plateaued, so a single suppressed equation does not explain every branch. SS-Broyden produced substantial gains in an existing two-network representation while the primary branches added many corrections; parameter count alone is therefore not established as the dominant cause. C02 improved modestly during the wider-correction block, which also changed sampling and continued optimization; width's causal contribution remains unresolved. Architecture, basin selection, correction scaling and the undisclosed author nontriviality term remain unresolved interacting choices.

Energy admission does not identify the published profile. C01 settled near its .5 energy floor, and independent profiles stayed near their floor of 2. C02 retained much larger amplitude while remaining inaccurate. The exact nondecaying PDE family U=F(r), Omega=0, Psi=z/2 shows why nonzero energy and small PDE loss alone are insufficient. The recorded finite-width, tail and derivative data do not classify the computed profiles as that family. Isotropic spatial scaling and axial translation preserve U amplitude, so they cannot by themselves reconcile a small observed swirl amplitude with the published large-amplitude profile. No numerical two-dimensional author profile was available to establish quantitative shape agreement.

The very-near-axis optional elliptic radial gradient needs a separate numerical qualification. At the saved C02 point r=1.014323e-7, z=-202.925022, a 60-digit evaluation of the same binary64 weights and physical coordinates gives RPsi=.001309198857 and d_rRPsi=-1.028802e-6. CPU FP64 gives d_rRPsi about -10.95, and the original GPU audit reported an absolute value of 13.22. Two large radial quotient derivative terms cancel; the apparent huge gradient is numerical. Exact-axis RPsi agrees to about 2e-13. Original FP64 cohort results are preserved, and these three targeted points do not replace any RMS or provide a certificate. This qualification does not remove C02's true Poisson error or its much larger global PDE errors.

The campaign remains a finite numerical reproduction with documented choices. Soft far-field samples do not establish decay at infinity, empirical maxima do not bound a supremum, bounded root searches do not prove absence of other roots, and a 100-million-point count alone does not certify a full-half-plane solution. The convection-varied Appendix-A family was reviewed but no epsilon-family experiment was run; primary production retained epsilon=1 and lambda=1/2 throughout.

## G. Reproduction, artifacts and continuation

All numerical work is retained under **ROOT = `/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114`**. The original rational experiments remain unchanged in the previous experimental directory. Source is in `ROOT/src/`, configurations in `ROOT/configs/`, checkpoints in `ROOT/checkpoints/`, optimizer histories in `ROOT/results/`, and coordinates, metrics, local searches and plots in `ROOT/validation/`. Full-state checkpoints retain model architecture, field scales, correction coefficients, C, optimizer state, training batches, training RNG state and available coefficient/history records. Fixed monitoring coordinates are saved alongside runs and embedded in the SS-Broyden probe states. The primary trainers did not serialize their advancing nontriviality-monitor RNG; full bitwise replay of those monitoring draws is not claimed. The early coefficient-logging limitation described above also remains.

The two selected profiles have separate immutable evaluation and full-state restart copies:

| Selection | Full-state restart file under ROOT | Saved phase clock / step | Full-state SHA256 |
|---|---|---|---|
| Three-equation aggregate | `checkpoints/final_inputs/independent_ssb_gpu/overall_three_full_state.pt` | 3300.366725 s / 6217 | `9b01968fc7243b6519a4076437276ab1aa06bf8ca8da004ebb3c77fd098e05fd` |
| Five-equation minimax | `checkpoints/final_inputs/independent_ssb_gpu/normalized_five_full_state.pt` | 2471.087054 s / 4638 | `55c0de79ac24af125efa6d773b64a6b16e0904a0329d177dc514d3523ddd018f` |

The corresponding `overall_three.pt` and `normalized_five.pt` files are lightweight evaluation copies. Exact optimization resumes use the **full-state** files. Original native aliases for the other criterion winners remain indexed in [best_checkpoint_index.json](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/best_checkpoint_index.json); its hashes and source metadata distinguish them from evaluation-only archives.

The numerical continuation command inside a validated compute allocation is:

```bash
TASK_ROOT=/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114
TASK_PY=/resnick/groups/Hou-group/Changhe/Euler/environments/euler-torch28-cu126/bin/python
TASK_FULL="$TASK_ROOT/checkpoints/final_inputs/independent_ssb_gpu/overall_three_full_state.pt"
source "$TASK_ROOT/environment.sh"
"$TASK_PY" -B "$TASK_ROOT/src/ssb_probe.py" \
  --resume "$TASK_FULL" --config "$TASK_ROOT/configs/probes/ssb_gpu.json" \
  --seconds 6000 --device cuda
```

`--seconds 6000` is a cumulative **phase-clock target**, requesting about 2699.633 additional seconds from the aggregate state, or 3528.913 from the normalized-five state if `TASK_FULL` is changed accordingly. Exact resume restores the saved objective, batches, coefficients and inverse Hessian; changing the supplied configuration does not silently change that saved objective. A fresh collocation/weight objective requires the explicitly supported restart protocol and fresh curvature, with its own accounting.

Submit through the central `slurmctl.py prepare → submit → mark-ready` workflow, which freezes source and runs Stage B on the production allocation. Complete literal resource-plan commands, both restart choices and revalidation commands are in [CONTINUATION_REPRODUCE.md](/resnick/groups/Hou-group/Changhe/euler_paper_pinn_20261114/CONTINUATION_REPRODUCE.md). No numerical workload should run on a login node.

The original environment is `Euler/environments/euler-torch28-cu128`; P100 validation/refinement used the separate `euler-torch28-cu126` environment because the installed CUDA 12.8 wheel lacked Pascal kernels. Both use Python 3.9.21, PyTorch 2.8.0, NumPy 2.0.2 and FP64. SciPy is 1.13.1 in the P100 environment. Actual dependency probes, interpreter fingerprints and GPU models are saved in central Stage B records; the new environment lock is `ROOT/research/p100_requirements.lock.txt`. Hardware/build changes need not reproduce every floating-point bit.

The completed grand jobs are **6897020** and **6897030**. Both used frozen source SHA256 `755a0d5b803bb4099a10c572d0c20f57ce209c2f6709dee59ca806bd4b31f955`, one P100, two CPUs and 16 GB host RAM. Actual allocation elapsed times were 473 and 380 seconds; these audit times are excluded from the optimizer budget. Central plans and frozen snapshots are under `/resnick/groups/Hou-group/Changhe/hpc/slurm/records/`, with plan names `euler-pinn-grand-three-e743cacc8859` and `euler-pinn-grand-five-cee5b2646649`.

Final selection and input identities are preserved in `ROOT/research/final_audit_selection_20261114T1317Z.json` and `grand_inputs_20261114T1318Z.json`. Both large audits used seed **742631887** after all profile optimization and selection had finished. Reusing it is an exact cohort repeat, not a fresh independent test; a future continuation needs a newly reserved holdout seed. Coordinate NPY files, coordinate/checkpoint hashes and actual counts accompany each validation JSON.

The most informative follow-up is a controlled test of training-only residual-gradient coverage in the thin axial-plane error regions, keeping initialization and other choices fixed. Recovering the authors' undisclosed architecture, nontriviality expression, scales and schedules would reduce reproduction uncertainty. Derivative-aware distillation could also test whether field-only teacher initialization lost useful elliptic structure. These are proposed experiments, not demonstrated fixes or additional computation claimed in this campaign.
