# Phase 1 reconstruction of the case6 travelling profile

The selected spectral checkpoint fits the supplied epoch-250000 case6 spline export at fixed $\lambda=0.4989408258587428$ and fitted $C=9.371073665480694$. On 40,960 independent physical points the relative RMS field errors are $1.58\times10^{-14}$ for U, $1.86\times10^{-4}$ for Ω and $1.41\times10^{-6}$ for Ψ. The strongest remaining field discrepancy occurs in vorticity around $(R,Z)=(523,-238)$. There the independently supplied Ω and Ψ disagree with the Poisson equation by essentially the entire spectral reconstruction error. [Checkpoint](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/checkpoints/best.npz) · [Reproduction and loading instructions](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/README.md) · [Field and error plots](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/geometry.png)

| Field | Absolute RMS | Relative RMS | Maximum absolute error | Physical (R, Z) at maximum |
|---|---:|---:|---:|---|
| U | 3.639e-13 | 1.581e-14 | 5.715e-12 | (0, 6236) |
| Ω | 6.385e-05 | 0.0001863 | 0.0005166 | (523.2, -238.2) |
| Ψ | 0.0002736 | 1.406e-06 | 0.002693 | (149, 197.7) |

### Input and phase convention

The epoch, neural checkpoint hash and interpolation errors come from the export metadata. The available reference consists of three independent float64, degree-nine tensor splines. Their control grids are $1601\times1601$ for U, $1601\times3201$ for Ω and $601\times1601$ for Ψ. The raw neural checkpoint named by the metadata was unavailable at its recorded path. Ω is the exported fit to the saved vorticity model. The computational coordinates are $(\operatorname{asinh}R,\operatorname{asinh}Z)\in[0,30]\times[-30,30]$. The shared neural shift $-0.2826438049496659$ is already built into the splines, and the physical phase shift is zero. All fits and comparisons used identical physical coordinates for model and target.

The supplied checker uses $V_R=R(\lambda-\Psi_Z)$ and $V_Z=C+\lambda Z+2\Psi+R\Psi_R$. Its elliptic diagnostic is $\Omega+\Psi_{RR}+3\Psi_R/R+\Psi_{ZZ}$, with $3\Psi_{RR}$ replacing the radial quotient at $R\le10^{-8}$. At 14 sites, including the axis, the moving origin and the domain edge, the production reference reader agreed with the supplied PyTorch evaluator to $5.69\times10^{-14}$ across field values and $4.19\times10^{-12}$ across tested derivatives. At $(1.01\times10^{-8},0.19)$ the original radial quotient was $-0.46298995$, compared with $-0.46298656$ using centered spline differentiation. The export metadata reports spline-to-neural RMS errors of $1.16\times10^{-14}$, $1.94\times10^{-16}$ and $4.97\times10^{-10}$ for U, Ω and Ψ on its 63,001-point comparison. These errors limit comparisons to the neural profile. [Reference checks](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/crosscheck.json) · [Input hashes](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/input_sha256.txt)

### Representation and exact constraints

The spherical part uses $\widehat R=R/256$, $\widehat z=(Z+C/\lambda)/256$, unit lift scale in these coordinates, and physical amplitudes $(U,\Psi,\Omega)=(\widehat U,256\widehat\Psi,\widehat\Omega/256)$. Both transport equations retain their given coefficients under this dilation. The two independently fitted leading Gegenbauer series include degrees 0–4. Three free multipoles have degrees 0–2. Every potential lift contributes its analytic negative Laplacian to Ω via the two sparse $B_{p+2,\ell}$ and $B_{p+4,\ell}$ coefficients in the specification. The pure-tail lifts use $K=2$ and the divided differences include both corrected legs.

The protection order is $S=6.01$. With $a=2.0042456904160297$, the protected weights in order are $a,4,2a,5,6,a+4$. The choice includes the first mixed monopole–dynamic interaction and ends below $3a=6.012737071248089$. At $2a$ the compiler generates all angular degrees through 9, and at $a+4$ through 5. It eliminates the transport coefficients recursively and inverts the angular Poisson multiplier. The near-resonant $(2a,0)$ and $(a+4,2)$ potential sectors use divided differences. The homogeneous monopole leg of the first divided difference enters the mixed forcing at its true weight 4. The resonant forcing at weights 4, 5 and 6 is zero. The polynomial-in-log solver therefore leaves just the independent homogeneous multipole at each resonance. Synthetic tests exercise nonzero resonant log forcing, omitted mixed terms and insufficient tail correction order. [Compiler](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/tail.py) · [Coefficient tests](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/tail_test.py)

The interior consists of $12\times22$ overlapping Chebyshev patches in $t=\log(1+R^2)/2$ and $v=\operatorname{asinh} Z$. Each field has degree 44 in each local coordinate. Smooth compact windows form a partition of unity across the supplied rectangle. A collar of width 0.10 in each mapped outer coordinate tapers the interior contribution to zero outside the data. This compact support preserves every protected spherical coefficient. The model uses **1,069,214 free scalar coordinates** including 534,600 interior coefficients per independent field, 13 free tail coordinates and C. The 45 assembled spherical coordinates include 32 dependent ones. All vorticity values and derivatives follow from the potential.

For a patch potential $G(\xi,Z)$, $\xi=R^2$, the evaluator differentiates both polynomial and window and uses $-\Delta_5G=-(4\xi G_{\xi\xi}+8G_\xi+G_{ZZ})$. This identity and the analytic spherical coefficient map hold for arbitrary free coefficients in exact arithmetic. Evenness in R is built in, and both axial parities are present. The potential is smooth and decays globally. Its source has a convergent five-dimensional Newton potential since its leading outer decay is $O(r^{-a-1})$. The difference between the represented potential and its decaying Newton inverse is entire harmonic and decays, hence vanishes.

| Independent structural test on the fitted coefficients | Measured discrepancy |
|---|---:|
| Re-expanded protected transport coefficients, largest absolute in scaled coordinates | $9.44\times10^{-15}$ |
| Same test, divided by max(1, sum of participating coefficient norms) | $1.78\times10^{-15}$ |
| 108-decimal scalar differentiation, Ω at $R=0,10^{-8}$ and $Z=0.19$ | $3.29\times10^{-16}$ or smaller |
| 108-decimal scalar differentiation, Ω at $(0.63,-0.77)$ | $2.69\times10^{-13}$ |
| Full Newton potential, largest discrepancy at three axis sites, quadrature orders 16, 32, 48, 72 | 1.63, $8.95\times10^{-4}$, $9.70\times10^{-7}$, $6.49\times10^{-12}$ |

The coefficient check expands the actual fitted J and Q coordinates in an independent Legendre-polynomial calculation, applies the angular Laplacian and assembles the original cylindrical fluxes. It also finds zero artificial lift coefficients at each protected correction power. The Newton calculation integrates the compact vorticity with the cylindrical free-space kernel and the spherical vorticity by radial moments to infinity. At $Z=0$ the compact and spherical contributions are about $-535.76$ and $+531.07$, so quadrature convergence matters. [Coefficient extraction](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/crosscheck.json) · [High-precision derivatives](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/poisson_hp.json) · [Newton convergence](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/newton.json)

### Reconstruction and the role of C

The fit used only measured field discrepancies. The shell initializer fitted all three fields on ten physical radii from 512 to 32,768 with 41 directions each. It enriched the leading angular degree from 2 to 4, solving for free tail coordinates and C by damped Gauss–Newton. The compact projection used patchwise Lobatto interpolation of U and Ψ after tail subtraction, followed by joint potential/source least squares with analytically differentiated columns. Successive degrees 8, 14, 22, 32 and 44 prolonged earlier patch solutions. A further correction used denser training samples in the intermediate region. The final swirl coefficients were reprojected after the center update.

The regional least-squares weight for a field was the inverse of its reference RMS in that region, floored in the denominator at $10^{-3}$ of the largest regional RMS for the field and $10^{-12}$ absolutely. Final comparisons added absolute fidelity weights in quadrature, with denominator scales $(0.2,0.005,1)$ for $(U,\Omega,\Psi)$. These weights were chosen after lower-resolution field comparisons showed that changes to Ψ could buy small improvements on low-amplitude source samples. The final linear potential correction, tail updates, step-length comparisons and center selection used only reconstruction data. Training, development and final validation used distinct seed streams. The table shows development field RMS after the Lobatto projection and before the degree-specific joint correction. [Fitting history and trial C values](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/fit.json)

| Patch degree | U | Ω | Ψ |
|---:|---:|---:|---:|
| 8 | 0.003063 | 0.005151 | 1.373 |
| 14 | 6.581e-05 | 8.26e-05 | 0.0272 |
| 22 | 2.136e-07 | 6.304e-05 | 0.001525 |
| 32 | 3.592e-10 | 6.303e-05 | 0.0001445 |
| 44 | 3.999e-13 | 6.303e-05 | 1.031e-05 |

C started at 9.37120536910309. Fitting the bare spherical terms alone first moved C to $-27.46$ at leading degree 2 and then to $-8.01$ at degree 4. Two full-resolution fits explored this branch and a branch initialized at the reference speed. Both allowed C to move. The development score selected **9.371073665480694**, a change of $-1.3170\times10^{-4}$. The full-rectangle fit weights the interior and the angular data very differently from the shell initializer.

| Equal-resolution fit | C | Held-out weighted MSE | Held-out Ω RMS | Held-out Ψ RMS |
|---|---:|---:|---:|---:|
| Selected free C | 9.37107366548 | 0.00234974180 | $6.38471\times10^{-5}$ | $2.73641\times10^{-4}$ |
| Fixed-C control | 9.37120536910 | 0.00234979247 | $6.38445\times10^{-5}$ | $1.88617\times10^{-5}$ |
| Other free-C branch | −8.00983420046 | 0.00234974894 | $6.38486\times10^{-5}$ | $2.76480\times10^{-4}$ |

Allowing C to vary improved the held-out weighted score by **0.00216%** relative to fixing it. The fixed-C control actually has the smaller unweighted Ψ RMS. The two free-speed results, separated by 17.38 in C, give nearly equal reconstruction scores. Translating the physical profile by $Z\mapsto Z+d$ would change C by $\lambda d$. The fit kept the physical samples and phase fixed. Its flexible interior can compensate for a shifted spherical representation, leaving the speed weakly identifiable from these fields. [Fixed-C checkpoint](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/checkpoints/fixedC.npz) · [Alternative free-C checkpoint](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/checkpoints/alternateC.npz) · [Paired comparison](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/C_comparison.json)

### Regional accuracy and geometry

Each row uses 4,096 independent points. The first three boxes are uniform in physical coordinates. Intermediate, global and extrema-scale boxes sample uniformly in computational coordinates out to $(x_R,|x_Z|)=(9,10),(30,30),(6,10)$ respectively. Exact-axis samples span the full axial interval. The near-axis set uses log-uniform R from $10^{-12}$ to $0.1$ and $|x_Z|\le10$. The far corners use $10\le x_R,|x_Z|\le30$. Outer rays have reference-centered radii log-uniform from 512 to 131,072 and uniform $\mu$. Relative RMS denotes $\|f_{sp}-f_{ref}\|_2/\|f_{ref}\|_2$. The aggregate gives each stratum equal point count, without physical volume weights. Sample maxima are empirical.

| Stratum | U absolute / relative RMS | Ω absolute / relative RMS | Ψ absolute / relative RMS |
|---|---:|---:|---:|
| 0.1 box | 1.271e-14 / 3.098e-16 | 1.706e-06 / 2.774e-06 | 1.651e-05 / 3.521e-06 |
| 1 box | 1.321e-14 / 3.577e-16 | 6.52e-06 / 1.381e-05 | 1.645e-05 / 3.481e-06 |
| 10 box | 7.316e-15 / 4.663e-16 | 1.61e-05 / 0.0001044 | 1.412e-05 / 2.482e-06 |
| Axis | 6.666e-13 / 3.316e-14 | 2.422e-06 / 6.922e-06 | 0.0001944 / 8.182e-07 |
| Near-axis | 8.739e-13 / 2.492e-14 | 2.276e-06 / 3.775e-06 | 0.0003474 / 1.526e-06 |
| Intermediate | 1.416e-13 / 1.175e-14 | 9.995e-05 / 0.0006363 | 0.0004925 / 2.155e-06 |
| Full coordinate box | 8.999e-14 / 2.474e-14 | 3.458e-05 / 0.0008203 | 0.000169 / 1.035e-06 |
| Far corners | 3.639e-16 / 4.266e-11 | 3.628e-06 / 0.9998 | 3.249e-05 / 2.491e-07 |
| Outer rays | 1.583e-14 / 1.503e-12 | 0.0001614 / 3.356 | 0.0003373 / 9.788e-07 |
| Extrema-scale box | 2.957e-13 / 2.038e-14 | 5.662e-05 / 0.0002954 | 0.0004513 / 1.906e-06 |

| Stratum | U max at (R, Z) | Ω max at (R, Z) | Ψ max at (R, Z) |
|---|---|---|---|
| 0.1 box | 4.263e-14 (0.001562, 0.03324) | 2.766e-06 (0.0009718, -0.09953) | 1.667e-05 (0.04045, 0.09988) |
| 1 box | 4.974e-14 (0.4032, -0.2361) | 1.848e-05 (0.9952, -0.6914) | 1.796e-05 (0.03065, 0.9997) |
| 10 box | 4.974e-14 (0.5654, 2.831) | 5.592e-05 (1.737, -9.809) | 2.128e-05 (0.0455, 5.929) |
| Axis | 5.715e-12 (0, 6236) | 6.842e-06 (0, 214.4) | 0.001247 (0, 677.4) |
| Near-axis | 5.697e-12 (5.36e-08, 6263) | 9.634e-06 (0.08655, 2273) | 0.001247 (2.793e-11, 678.1) |
| Intermediate | 3.089e-12 (0.7215, 3455) | 0.0005159 (547, -235) | 0.00262 (174.5, 262.3) |
| Full coordinate box | 4.375e-12 (0.1129, 1.242e+04) | 0.0005166 (523.2, -238.2) | 0.002669 (166.2, 240.9) |
| Far corners | 1.039e-14 (1.173e+04, 1.737e+04) | 1.444e-05 (1.123e+04, -4.737e+04) | 0.0004944 (1.436e+10, 2.564e+07) |
| Outer rays | 3.915e-13 (169.6, -633) | 0.0005164 (533.3, -244.6) | 0.002025 (268.5, 420.3) |
| Extrema-scale box | 4.907e-12 (0.1276, 5397) | 0.0003623 (182.8, 306.1) | 0.002693 (149, 197.7) |

| Physical derivative | Absolute RMS | Relative RMS | Max at (R, Z) |
|---|---:|---:|---|
| U_R | 3.99e-13 | 8.683e-14 | 1.552e-11 (0.3782, 5251) |
| U_Z | 7.289e-14 | 1.062e-11 | 6.497e-13 (0.05595, -0.04302) |
| Ω_R | 2.323e-05 | 0.0001624 | 0.0003994 (0.6699, -2601) |
| Ω_Z | 7.771e-06 | 0.00489 | 0.0001261 (3.137e+06, 0.2038) |
| Ψ_R | 1.907e-06 | 6.483e-05 | 3.452e-05 (54.82, 194.9) |
| Ψ_Z | 2.714e-06 | 7.392e-06 | 2.476e-05 (141, 92.95) |

| Extremum | Spline value at (R, Z) | Spectral value at (R, Z) |
|---|---|---|
| U max | 4.11408138e-05 (92.9, 1.679e+09) | 4.11408138e-05 (92.9, 1.679e+09) |
| U min | -41.617904 (0, 100.5) | -41.617904 (0, 100.5) |
| Ω max | 1.10000468 (0, -365.9) | 1.10000461 (0, -365.9) |
| Ω min | -0.556545914 (0, 1023) | -0.556547637 (0, 1023) |
| Ψ max | 571.600836 (75.45, 8237) | 571.600687 (75.46, 8237) |
| Ψ min | -357.838746 (87.06, -4015) | -357.838771 (87.06, -4015) |

The large negative swirl minimum has radial half-amplitude radius 1.84297 in both profiles. Its axial half-amplitude crossings are approximately −963.38 and 1750.24. The positive Ω peak has radial half-amplitude radius 0.957250 in the spline and 0.957278 in the reconstruction. For the negative peak the radii are 1.016134 and 1.016189. At the reference positive Ω extremum the radial curvatures are −2.22310 and −2.22534. On a separate near-axis line at $R=10^{-8}$, the Ω RMS error is $2.34\times10^{-6}$, with maximum $7.00\times10^{-6}$. The broad Ψ geometry extends thousands of physical units along Z. The full-domain figure and machine-readable diagnostics include the outer field, half-height crossings, local curvatures and detailed axis profiles. [Geometry plot](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/geometry.png) · [Full-domain plot](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/domain.png) · [Numerical diagnostics](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/validation.json)

### Transport diagnostics and limitations

| Equation | Reference RMS | Spectral RMS | Largest absolute spectral residual | Physical (R, Z) |
|---|---:|---:|---:|---|
| U transport | $1.0750\times10^{-5}$ | $1.3493\times10^{-4}$ | $1.0277\times10^{-3}$ | $(8.09\times10^{-11},154.06)$ |
| Ω transport | $2.9876\times10^{-5}$ | $1.5125\times10^{-4}$ | $3.5722\times10^{-3}$ | $(24951.33,-0.244)$ |
| Poisson | $6.3846\times10^{-5}$ | zero algebraically | independent differentiation above | |

At the U-residual maximum, the change in the stretching term $-2U\Psi_Z$ is $+1.02750\times10^{-3}$. At the Ω-residual maximum, the change in axial advection $V_Z\Omega_Z$ is $-3.55213\times10^{-3}$, compared with $-1.35\times10^{-5}$ from radial advection. These termwise differences use the two fields at the identical physical sites. Both transport RMS values increased. The table uses unnormalized equation residuals on the same 40,960 points, with each model's own C. These diagnostics were computed after selection. The earlier six-million-point audit used a different mixture of six strata. Its quoted RMS values $1.12\times10^{-5},1.95\times10^{-5},3.59\times10^{-5}$ are contextual. The supplied checker implements the stated equations, although its current file hash differs from the checker hash recorded in the export metadata.

Three limitations matter for reuse.

1. **The reference violates Poisson locally.** At the largest Ω error the signed spectral discrepancy is $-5.16567\times10^{-4}$ and the signed reference Poisson diagnostic is $+5.16576\times10^{-4}$. The RMS values agree to about $1.5\times10^{-9}$ across the sample. On outer rays the Ω RMS error is 3.36 times the reference Ω RMS. The measured Ψ geometry and direct vorticity target pull the constrained fit in different directions. These observations quantify this reconstruction's tradeoff and do not establish a lower bound over all possible weighted fits.
2. **The imposed asymptote is an extrapolation.** The compact correction carries substantial signal well into the finite outer domain. On a radius-$10^8$ shell, the spline Ψ RMS is about 161.90 and the bare fitted spherical tail gives $7.02\times10^{-5}$. At $10^{12}$ they give 1.1664 and $6.75\times10^{-9}$. The full patched profile reproduces the finite-domain potential. Data outside the rectangle would be needed to validate its continuation, including the outer collar. The far-corner Ω has nearly unit relative RMS discrepancy even though its absolute RMS error is only $3.63\times10^{-6}$. [Bare-tail shell measurements](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/results/tail_shells.json)
3. **Phase 2 has a large starting parameter space.** The source discrepancy is already insensitive to raising the interior degree from 22 to 44. Higher degrees mainly improve U and Ψ. The additional multipole and nonlinear sectors beyond $S$ have not been constrained. The fitted speed, compact extrapolation and high-order coefficients should be carried with the checkpoint when interpreting subsequent optimization.

The pickle-free archive contains the independent potential and swirl tensors, regularized tail variables, derived spherical coefficients, physical normalization, patch and lift parameters, fixed λ and fitted C. The Python loader was checked at the same 14 sites against the independent production implementation. The largest field difference was $1.03\times10^{-12}$ and the largest tested derivative difference was $1.50\times10^{-11}$. A fresh V8 replay from the spline coefficients reproduced the selected C, both full coefficient tensors byte for byte, and the held-out Ω RMS. Phase 1 ended with this checkpoint and its diagnostics. [Loader](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/spectral_profile.py) · [Fit entry point](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/reproduce.js) · [Best checkpoint](/resnick/groups/Hou-group/Changhe/euler_case6_phase1/checkpoints/best.npz)
