# Result: rapid Boussinesq-to-IPM numerical campaign

The campaign found **useful full-plane IPM improvements, but no converged similarity profile**. Compared with the prior A20 control, the RBF40 candidate reduces the normalized core maximum by 7.1% and the remote two-power residual estimate by 8.4 times, with a 3.6% normalized core RMS penalty. RBF56 lowers normalized RMS by 5.9% and raw RMS by 10.1%, while increasing the normalized maximum by 35.2%. A later quartic-loss candidate lowers that maximum by 25.9%, but increases normalized RMS by 18.3% and raw RMS by 56.0%. These are complementary physical tradeoffs; no candidate improves every important measure.

The new Boussinesq training lowered an independent six-equation RMS by 3.07 times in 113 seconds, but failed the independent global velocity check. It is **not a successful physical reproduction**. The useful IPM ingredients were constraint-compatible corrections, cached canonical responses, damped least squares, and explicit asymptotic error control. No similarity parameter was imported from the Boussinesq paper.

This report answers the attached “22-Hour Rapid Numerical Campaign” request. The archived specification and all executable artifacts are in [the campaign directory](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/README.md). Work began conservatively at **2026-11-12 08:47 UTC**; final numerical work ended at **2026-11-12 12:52:31 UTC**, about **4 hours 5 minutes** after the start. The 22-hour limit was a maximum, with an absolute deadline of November 13 at 06:47 UTC. The complete accounting contains 50 job records, including startup refusals, diagnostics and independent validators: **3.327 allocated CPU-hours**, **0.178 allocated GPU-hours** and **2.391 reported consumed CPU-hours**. No campaign jobs remain active. The recorded production spans sum to 10,823 seconds across jobs; this is not the campaign wall time. Exact accounting and coverage are in [resource_summary.md](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/resource_summary.md).

## Physical problem retained

The IPM target is the existing whole-plane, travelling-centered equation

\[
R=(c_lX+u[\rho](X))\cdot\nabla\rho-\rho,
\quad u[\rho](X)=U[\rho](X)-U[\rho](0),
\quad -\Delta\psi=\partial_x\rho,
\quad U=(-\psi_y,\psi_x).
\]

The source representation remains even in \(x\), permits both \(y\) parities, and has the **local** jet \(\rho=x^2+O(r^3)\). There is no global \(x^2\) factor or imposed whole-axis zero. Five dependent density coefficients enforce the four required jet conditions and the actual canonical strain

\[
S=\psi_{xy}(0)=c_l-\tfrac12.
\]

Indeed, the quadratic transport term is \([2(c_l-S)-1]x^2\). The strain comes from the density, with no independent harmonic component. The moving-center subtraction is retained exactly. The normalization \(a_0=1\) fixes a legitimate scale: \(\rho_b(X)=b\rho(X/b)\), \(U_b(X)=bU(X/b)\) preserves the equation and \(c_l\), while taking \(a_0\) to \(a_0/b\).

The exponent \(c_l\) is optimized jointly with the density throughout. The inherited sublinear source family requires \(c_l>1\); this is a restriction of the searched family, not a conclusion about all solutions. Fixed-parameter Candidate 013 and boundary-IPM assumptions were not used. The separate Boussinesq case4 project, including its \(\beta=3\) convention, was untouched.

## Boussinesq: local improvement rejected by global reconstruction

The requested [Discovery of Unstable Singularities](https://arxiv.org/abs/2509.14185) and both third-party repositories were inspected before reuse. At the audited revisions, [LucasAschenbach/fluid-singularities](https://github.com/LucasAschenbach/fluid-singularities) has inconsistent similarity drift signs, stream-function parity, and coordinate use in its Boussinesq path. The advertised example in [flamehaven01/Unstable-Singularity-Detector](https://github.com/flamehaven01/Unstable-Singularity-Detector) solves a toy equation rather than the physical Boussinesq system. Neither was run unchanged or credited with physical convergence. Exact commits, source locations and audit notes are in [audit.md](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/audit/audit.md).

A working physical representation and genuine checkpoints were obtained from the primary-author repository for the **different** [unbounded-domain PINN paper, arXiv:2506.19243](https://arxiv.org/abs/2506.19243): [RoyWangyx/High-precision-PINNs-unbounded-domains-](https://github.com/RoyWangyx/High-precision-PINNs-unbounded-domains-/tree/466370c4f826503f6b9147dcc60e39222398acea). This is not official code for the DeepMind paper. The experiment uses \(y=x/(T-t)^{1+\lambda}\), the exact gauge \(\Omega_x(0)=-1\), and five fields \(U_1,U_2,\Omega,\Phi=\Theta_x,\Psi=\Theta_y\). With \(A=(1+\lambda)y+U\), the six tested equations are

\[
\begin{aligned}
\Omega+A\cdot\nabla\Omega-\Phi&=0,\\
(2+U_{1x})\Phi+A\cdot\nabla\Phi+U_{2x}\Psi&=0,\\
(2+U_{2y})\Psi+A\cdot\nabla\Psi+U_{1y}\Phi&=0,\\
U_{1x}+U_{2y}&=0,\\
U_{2x}-U_{1y}-\Omega&=0,\\
\Phi_y-\Psi_x&=0.
\end{aligned}
\]

Independent frozen Sobol points mix three compactified ranges and reach physical coordinates of about 202. The wall condition is measured, and velocity is separately reconstructed with an anchored half-plane image-kernel Biot–Savart integral, varying the cutoff and doubling quadrature. An analytic Gaussian fixture checks the integral signs and anchoring.

| Experiment | Initial audit RMS | Final audit RMS | Reduction | Training seconds |
|---|---:|---:|---:|---:|
| Same 184-parameter last-affine model, LM | .0194544 | .0140827 | 1.38× | 49.2 |
| Same model, Adam | .0194544 | .0189351 | 1.03× | 75.4 |
| Same model, L-BFGS | .0194544 | .0179031 | 1.09× | 59.4 |
| Full 28,627-parameter model, L-BFGS | .0194544 | .00633954 | 3.07× | 113.2 |

The full-network run used 185 steps and 375 closure calls. Its freely optimized \(\lambda\) moved from 1.3007396 to 1.6744286, the exact slope survived, and vorticity-field amplitude RMS increased by a factor of 1.24 rather than collapsing. **However**, the maximum independent velocity mismatch at cutoff \(2^{39}\) increased from **2.0531 to 12.4601**. Doubling quadrature changes the latter by only .00254; its cutoff sequence grows from .256 at \(2^{31}\) through 4.691 at \(2^{35}\), so a fortuitous smaller-cutoff crossing is not evidence of convergence. Some individual equations and the local origin identity also worsen. The overall sampled maximum falls from .400247 to .146207. The individual physical equations show why the aggregate RMS is insufficient:

| Equation | Initial RMS | Final RMS | Initial maximum | Final maximum |
|---|---:|---:|---:|---:|
| Vorticity transport | .011069 | .006829 | .096051 | .037830 |
| Temperature-x-gradient transport | .013758 | .007672 | .045566 | .046625 |
| Temperature-y-gradient transport | .001659 | .003199 | .005556 | .012881 |
| Incompressibility | .031561 | .007645 | .400247 | .146207 |
| Curl minus vorticity | .030861 | .007557 | .380831 | .061517 |
| Temperature-gradient compatibility | .002791 | .003138 | .008670 | .014844 |

Wall penetration maximum improves from .05315 to .004649, while the local lambda-identity defect worsens from .01816 to .02006.

For context, the already-trained published stable checkpoint has \(\lambda=1.920675468\), six-equation RMS about \(2.85\times10^{-6}\), and finite-cutoff velocity mismatch .002108 at \(2^{39}\). It is an inherited approximate control, not a new reproduction or campaign training achievement; its prior training cost is unknown here. The new local reduction does not establish the original scalar-temperature equation either. The full rejection and reconstruction data are in [Boussinesq_DISPOSITION.md](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/Boussinesq_DISPOSITION.md). The filename `transfer_ready.json` refers only to the local screening threshold and must not be interpreted as global approval.

## IPM implementation and measured efficiency

The campaign reused the canonical source evaluator from the existing X2 travelling search and preserved the old A20 tail control. It combined its spectral coefficients with small Gaussian density corrections,

\[
\tfrac12\left[e^{-((x-a)^2+(y-b)^2)/s^2}
+e^{-((x+a)^2+(y-b)^2)/s^2}\right],
\]

with signed \(b\) free to differ between features. New amplitudes start at zero, preserving the initial physical fields. Centers and widths are chosen from residual locations and then fixed within a run; amplitudes and \(c_l\) remain free. RBF40 has 24 standard pairs plus 16 added pairs; RBF56 adds another 16, with minimum width .02. The standard loader already introduces 24 zero-amplitude pairs, which are trainable. Thus the early “optimizer control” is not a pure unchanged 206-variable spectral optimization: it has 230 unknowns; RBF40 and RBF56 have 246 and 262 respectively.

Canonical density/gradient/velocity response matrices are cached at Chebyshev nodes of the free exponent. Coefficient Jacobians are analytic; off-node responses are checked, trial acceptance uses the uncached canonical evaluator, and independent validation uses actual saved coefficients. No local Poisson surrogate or free velocity network was introduced.

A matched kernel benchmark on the same state and machine found **12.66× faster residual/Jacobian evaluation and 20.02× faster trial residual evaluation** after replacing array Clenshaw evaluation with one Chebyshev-basis contraction. Relative response-matrix differences were about \(2\times10^{-16}\), and full Jacobian differences about \(6.5\times10^{-11}\). This is a kernel speedup; it is not the optimizer's end-to-end speedup. A 641.5 MB steady derivative copy was removed; coefficient storage remains about 681.6 MB. Exact acceptance and validation still cost appreciably.

An independently derived exponent derivative agreed with the original chart finite difference to \(1.36\times10^{-10}\) relative, ruling out that proposed derivative error at the tested state. No physical gain is attributed to that change. Changing the five constraint pivots to Gaussian columns was physically equivalent to roundoff but did not improve the bottleneck: a matched comparison gave common-grid RMS/maximum .0338729/.344678 for the original chart and .0338773/.345172 for the new chart, both worse in maximum than the .277506 starting state. Each used about 500 seconds.

Divided-difference coordinates for matching free radial pairs improved several weak column-scaled Jacobian directions (five more numerical directions at relative threshold 1e-10), while leaving the weakest singular value unimproved. Their explicit exponent derivative agreed with a converged finite-difference check to 2.2e-7. A subsequent pilot was stopped after more than 90 accepted steps because its RMS/maximum plateaued near .033781/.343244, with no substantive physical gain. Its checkpoint is retained as a conditioning control. Reduced validation frequency also improved throughput, so the wall-time change cannot be attributed solely to coordinates.

## Why the far-field correction mattered

Finite-only far sampling gave misleading improvements. Write the candidate's density and canonical stream function as

\[
\rho=r^p\Theta_0+r^{2p-1}\Theta_1+\cdots,
\qquad \psi=r^{p+1}\Phi_0+r^{2p}\Phi_1+\cdots,
\qquad p=1/c_l.
\]

The first nonlinear transport coefficient required by the equation is

\[
D_0=-p\Phi_0'\Theta_0+(p+1)\Phi_0\Theta_0'
-(c_l-1)\Theta_1.
\]

All angular functions are obtained from the current density and canonical inverse. No angular boundary data are prescribed. At \(c_l\simeq1.0033\), \(r^{p-1}\) is still about .88 at \(10^{16}\). The old control has \(\|D_0\|_{\rm RMS}=.000707531\), whereas finite-only RBF and uniform refinements reach **1.36472, 1.21712, and 1.17921** despite improved residuals at four finite far radii. They were rejected as global improvements.

The corrected fit adds the exact \(D_0\) rows, with block weight 2500 to balance the initial core/tail scales, and an uncached error guard. The first guard is 1.05 times the old error; later refinements use \(10^{-4}\). This penalizes PDE error without fixing angular values or \(c_l\). The corrected RBF40 run took about 510 seconds with 98 accepted steps; capacity used 84 steps in 511 seconds and mild zoom 66 in 524 seconds. These correspond to about 5.2, 6.1 and 7.9 seconds per accepted step, including cache/validation overhead. Coarse adaptive sampling did not clearly beat uniform sampling on their common score. An aggressive 1,024-point narrow-ridge refinement worsened held-out RMS and maximum substantially and was stopped.

The remote audit also retains the interaction of both slow powers. If \(q_0=p,q_1=2p-1\) and

\[
N_{ij}=-q_j\Phi_i'\Theta_j+(q_i+1)\Phi_i\Theta_j',
\]

then

\[
R/r^{2p-1}=W(z,\theta)+\text{higher terms},\quad
W=D_0+z(N_{01}+N_{10})+z^2N_{11},\quad z=r^{p-1}.
\]

The mean-square of \(W\) is a quartic polynomial in \(z\); its extrema are evaluated continuously over the candidate-specific interval for the same physical region \(r\ge10^8\). This exposes residual peaks at formal radii far beyond directly sampled grids. It is an asymptotic diagnostic, not a uniform bound on the full equation.

A third-slow-power leverage diagnostic also exposed a collocation failure. On only 384 core points, an old-family response step appeared to lower the remote maximum from .03107 to .001390 with nearly unchanged core error. Fresh dense validation instead gave normalized RMS .5437 and maximum 16.948, with a new peak near the positive y axis at radius 2.09. The separate sampled inverse agreed with the analytic source on its own points (RMS about .6901), so this was physical overfitting between diagnostic points. The candidate was rejected. Adding the third power in that diagnostic also violated the first-tail guard and did not beat the old-family response. This does not establish that a higher-power representation cannot help; it establishes that the small leverage grid was inadequate. A follow-up one-step response used 96×128 global points plus 80 signed-axis points and jointly varied cl. All three bounded trials also failed: the smallest raised held-out normalized RMS from .03697 to .3501 and maximum from .23965 to 2.047, while both tail guards worsened. Here training and held-out errors rose together, exposing nonlinear step curvature in addition to the earlier sampling failure. None was saved as a lead. A single dense smooth-quartic run then tested the peak objective with the physical equations unchanged. Its fixed core merit was q(R)=R*sqrt(R²+tau²)/s0, with tau=.25 of the initial training RMS and s0 matching the initial transformed block norm. The run used 48 accepted steps in 521 seconds including setup/final diagnostics. It lowered normalized peaks but increased RMS/raw error; it did not produce a balanced winner.

| Checkpoint | Dense normalized RMS | Dense normalized maximum | Dense raw RMS | Remote W maximum RMS |
|---|---:|---:|---:|---:|
| RBF40 restart | .03710027 | .24002371 | .01289957 | .02255934 |
| Quartic step 3 | .04236258 | .19145514 | .01956273 | .02108253 |
| Quartic terminal | .04338911 | .19352461 | .02161334 | .01348358 |

The fixed predeclared audit set was steps 1, 3, 6, 12 and terminal; all used the same dense/Sobol points as the original comparison. Step 3 lowers the original A20 normalized maximum by 25.9%, but its normalized RMS is 18.3% higher and raw RMS 56.0% higher. The separate canonical inverse agrees, with velocity/r RMS differences 3.05e-7 and 1.73e-7 for step 3 and terminal. Their exact D0 RMS values are 2.55e-5 and 2.08e-5. These are preserved peak/tail alternatives, not replacements for the lower-RMS states. The fixed-step directional derivative diagnostic warned at the quartic seed; a low cached/uncached merit discrepancy and actual uncached acceptance support the reported physical metrics, not a claim of certified Jacobian accuracy. The final experiment directly added the mean-square remote polynomial W to the damped least-squares objective. Three Gauss–Legendre nodes integrate W² exactly in the slow coordinate; their physical z positions are recomputed at each cl. A fixed initial norm match gave weight 4.84449. The unchanged D0 and remote-maximum checks were supplemented by guards keeping all four original training-core measures (raw and normalized RMS/maximum) within 2% of the same-grid original restart.

This run was stopped intentionally after about 6.6 minutes, with four accepted steps and 45 core-guard rejections. Every rejection violated the raw maximum; 18 also violated raw RMS. Accepted fractions shrank from 1/64 to 1/512. The preselected third accepted state was independently audited:

| Matched dense-grid measure | RBF40 restart | Guarded remote-loss control |
|---|---:|---:|
| Normalized RMS | .03710027 | .03709511 |
| Normalized maximum | .24002371 | .24005392 |
| Raw RMS | .01289957 | .01292136 |
| Raw maximum | .09758890 | .09938937 |
| Remote W maximum RMS | .02255934 | .02238200 |

The remote gain is only .79%, accompanied by a 1.85% raw-maximum increase. Sobol confirms the core comparison. The separate inverse has velocity/r discrepancy 7.84e-8, and exact D0 RMS is 2.53e-5. This is a stopped optimization control, not a substantive new lead. Its third accepted checkpoint is distinct from the run's final fourth state. The full-merit Jacobian directional check was 1.19e-6 relative and cached/uncached merit difference 7.03e-7, so this final barrier was observed with usable scientific controls.

## Independent validation of the initial IPM tradeoff set

All following core rows use the **same** frozen 256-radius × 256-angle shifted full-circle log-polar grid on \(.005\le r\le40\), plus a separate set of 20,000 scrambled Sobol points. The fixed envelope is \(E_{\rm abs}=r^2/(1+r^2)\). RMS gives equal weight to sampled points, not physical-area weight. Both the unmodified transport residual \(R\) and \(R/E_{\rm abs}\) are reported. Saved point-array SHA256 is `9580264698b914f3e342a29b4af960a63c43badab8ff5fb06c7ba30105dfc5ae`.

| Candidate | \(c_l\) | Dense raw RMS | Dense raw maximum | Dense \(R/E_{\rm abs}\) RMS | Dense normalized maximum |
|---|---:|---:|---:|---:|---:|
| Prior A20 control | 1.003334123 | .01253913 | .10025715 | .03579640 | .25842076 |
| RBF40 peak representative | 1.003504415 | .01289957 | .09758890 | .03710027 | .24002371 |
| RBF56 core RMS representative | 1.002251599 | .01127612 | .12250674 | .03369229 | .34927127 |
| RBF56 mild zoom | 1.002251497 | .01208183 | .10494972 | .03389945 | .29119207 |

Sobol normalized RMS/max are respectively .03583206/.25780881, .03710480/.24010317, .03364523/.34885118, and .03387276/.29018522. The independent sampling distribution therefore confirms the tradeoff. Mild zoom lowers the capacity parent's maximum by 16.6%, but its maximum remains 12.7% above the historical control. A narrow ridge near \(r=.116\)–.139 remains unresolved. Saved-data half-height widths span eight to nine above-threshold dense radial samples and thirteen angular samples, and the zoom training grid also covers the feature; the failed targeted sampling is not explained by an infinitesimal unseen spike alone. These sampled maxima are not continuous upper bounds, and the printed \(c_l\) digits identify saved states rather than certified parameter accuracy.

| Candidate | Near \(r<.05\) RMS | Inner \(.05\le r<.5\) RMS | Middle \(.5\le r<5\) RMS | Outer \(r\ge5\) RMS | Four-axis RMS |
|---|---:|---:|---:|---:|---:|
| Prior A20 | .017938 | .061097 | .027235 | .016305 | .062700 |
| RBF40 peak | .023163 | .061753 | .026982 | .019043 | .061499 |
| RBF56 core RMS | .029720 | .052898 | .022624 | .016908 | .061306 |
| RBF56 mild zoom | .030043 | .050811 | .027599 | .016978 | .059024 |

These regional entries use the same fixed-envelope residual. In particular, the near-origin band worsens even though the exact leading jet survives; the total core RMS reduction must not conceal this defect. Across the three new states, \(|\rho(0)|<4.6\times10^{-12}\), the \(x^2\) coefficient differs from one by less than \(2.7\times10^{-10}\), and canonical strain compatibility is within \(1.4\times10^{-11}\). The normalized jet defect at \(r=.001\) is about \(1.35\times10^{-4}\) to \(3.08\times10^{-4}\); nonzero local/core density is retained. Reflection discrepancies are at floating-point cancellation scale, up to \(2.8\times10^{-9}\) on the tested grid.

### Separate canonical Darcy reconstruction

A separate sampled-density Fourier-moment inverse uses 600 core rings, 300 exterior rings extending to \(10^{24}\), and 256 angles. It fits the candidate's own two exterior powers. It is independent of the analytic source inverse, while density gradients still come from the analytic representation. A signed Gaussian fixture reproduces the known strain \(1/8\) within \(6.6\times10^{-10}\).

| Candidate | RMS \((u_{\rm sampled}-u_{\rm source})/r\) | Strain difference | Sampled-inverse normalized transport RMS |
|---|---:|---:|---:|
| Prior A20 | 1.440e-7 | −1.057e-7 | .03535310 |
| RBF40 peak | 8.468e-8 | −6.262e-8 | .03678074 |
| RBF56 core RMS | 1.705e-7 | 2.776e-8 | .03351079 |
| RBF56 mild zoom | 2.381e-7 | −1.942e-7 | .03363988 |

Transport here uses a different 2,048-point common probe grid. Analytic and sampled-inverse normalized RMS agree within \(2.8\times10^{-8}\) **on those matched points**. Its RMS values should not be compared directly with dense-grid RMS as a convergence-in-resolution test. No elliptic/Poisson training residual was used: canonical coupling was imposed directly.

### Remote behavior

| Candidate | Exact \(D_0\) RMS | Maximum remote \(W\) RMS | Sampled-angle maximum \(|W|\) | Formal \(\log_{10}r\) at RMS peak |
|---|---:|---:|---:|---:|
| Prior A20 | 7.07531e-4 | .19049696 | .31262115 | 92.26 |
| RBF40 peak | 2.53956e-5 | .02255934 | .03932587 | 89.32 |
| RBF56 core RMS | 1.97456e-5 | .02409822 | .03867063 | 137.42 |
| RBF56 mild zoom | 2.76825e-5 | .03107100 | .05063389 | 137.02 |

The 128/256-angle checks agree closely. At actual radii \(10^8\) and \(10^{16}\), the full-source versus two-power normalized RMS discrepancy is at most \(4.4\times10^{-10}\) for these states. This supports the remote comparison at those samples; it does not bound all omitted terms uniformly. The natural exponent-dependent normalization changes with the candidate, so fixed-envelope and raw comparisons remain necessary.

Actual **raw** far RMS is still large: at \(10^4\), the old control gives 124.384 versus 10.164, 9.020 and 9.844 for the new states; at \(10^{16}\), it gives \(5.55\times10^{14}\) versus \(6.21\times10^{13}\), \(4.86\times10^{13}\) and \(6.42\times10^{13}\). Thus no candidate has a small uniform absolute full-plane residual. The reduction of the leading tail amplitude also contributes to the improvement. On the common finite-core validation measure, density RMS decreases from .07745 to .06106, .05454 and .06002; this is nonzero but a 21–30% amplitude change. The unit local jet alone does not prove relative convergence everywhere.

## Preserved states and reproduction

All paths in this section are beneath `/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112`.

| Role | Checkpoint in `preserved_candidates/` | SHA256 |
|---|---|---|
| Historical control | `prior_source_best_A20_tail_cl100333.npz` | `a5a3e96b8d1caac2625c617557084ea65afc4e68d0bba421aa0db98ea5529b57` |
| Peak/tail representative | `A20_RBF40_peak_pareto.npz` | `d9006123166d16002a401bede5ee4f23e53b151f54928442077f6f8a78c3ec63` |
| Core RMS representative | `A20_RBF56_tail_corrected_capacity.npz` | `ef231d73f8253c703d32c716e93fb12de82267700b72a5410d7449d6898c9437` |
| Mild-zoom compromise | `A20_zoom_peak_first_6784630.npz` | `7b4fa96c8dfaf44ba8ee2af38d0c194a7edd8f8f396d13738e9d33c4e24e9fef` |

The original baselines were copied, not overwritten. Exact source snapshots, commands, hardware and gate records are in the central SLURM records, with a collected [run ledger](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/run_ledger.json). The initial tradeoff metrics and hashes are in [FINAL_METRICS.json](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/FINAL_METRICS.json) and [the selection manifest](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/ipm_audit/final_pareto_manifest.json). Later objective experiments are in [QUARTIC_METRICS.json](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/QUARTIC_METRICS.json) and the combined [CAMPAIGN_METRICS.json](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/CAMPAIGN_METRICS.json).

The [reproducible archive](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112_reproducible.tar.gz) is 43.5 MB and contains source, seed weights, preserved candidates, configurations, selected validation arrays and frozen controller records. SHA256: `13da538f86bc8531ff752f34dea7f9c3e4d616278a6d42c6bb541df420725270`. Its manifest and all 2,754 payload files were checked against the archive bytes. The complete original results remain in the campaign directory.

The [remote-tail comparison figure](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/figures/ipm_final_pareto_tail.pdf) visualizes the initial tradeoff set and the finite-radius sampling limitation.

The existing Python 3.9.21 environment with NumPy 2.0.2, SciPy 1.13.1 and PyTorch 2.8/CUDA 12.8 was reused. Actual V100 float64 execution was checked. Substantial science ran in central-controller allocations, with one CPU/BLAS thread for the source experiments. Future reproduction uses the existing [replay.py](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/replay.py), which prepares/submits/freezes a fresh central plan. From the campaign directory:

```bash
python3 replay.py ipm_refine --output-base /resnick/scratch/cyang6/ipm-replay/refine \
  --submit --authorized-by 'User requests reproduction of the preserved IPM run'
python3 replay.py ipm_capacity --output-base /resnick/scratch/cyang6/ipm-replay/capacity \
  --submit --authorized-by 'User requests reproduction of the preserved IPM run'
python3 replay.py ipm_validate_dense --output-base /resnick/scratch/cyang6/ipm-replay/dense \
  --submit --authorized-by 'User requests validation of the preserved IPM candidate'
python3 replay.py ipm_validate --output-base /resnick/scratch/cyang6/ipm-replay/canonical \
  --submit --authorized-by 'User requests independent canonical validation'
python3 replay.py ipm_slow_tail --output-base /resnick/scratch/cyang6/ipm-replay/tail \
  --submit --authorized-by 'User requests the remote-tail comparison'
```

Validation defaults to the preserved RBF40 peak representative; `--restart` selects another state. The README gives additional sampling, coordinate-control and negative-control commands. `ipm_quartic` reproduces the peak-objective run, and `ipm_remote_merit` reproduces the final guarded global-loss test; both request 32 GB for their denser response caches. `environment_reproduce.sh` deliberately removes the campaign's expired deadline for future authorized runs. A time-limited reproduction can stop at a different iteration; the reported candidates and their configurations are preserved exactly.

Several execution failures are recorded rather than hidden: two initial environment-fingerprint refusals, one readiness race, a quartic startup logger collision, and end-of-run logger errors after numerical summaries had been written. The fingerprint/logging bugs were corrected; the quartic startup refusal produced no training result and was retried with a fresh frozen source. Numerical claims above use saved validated arrays, not scheduler success status alone. Final verification passed 57 small algebra tests, parsed 52 Python sources, checked shell syntax, verified selected checkpoint/source identities and the complete archive inventory, and confirmed that no campaign job remained active. The report also received an independent mathematical and numerical consistency review. These checks support reproducibility, not a mathematical error enclosure.

## Single next direction and limits

**The most promising next numerical direction is an active-set constrained Gauss–Newton step in the existing canonical density basis.** Include active signed raw/normalized peak linearizations and RMS budgets inside the step subproblem, with a numerical trust region, then retain uncached canonical acceptance and independent validation. The final run repeatedly shrank a direction that crossed the same raw-maximum boundary; all 45 rejected trials identify that boundary directly. Incorporating it into the step could find a feasible decrease along the boundary. This is a specific untested hypothesis, not evidence that the current basis is sufficient or that a profile exists. The mathematical formulation is preserved in [FUTURE_CONSTRAINED_STEP.md](/resnick/groups/Hou-group/Changhe/rapid_pinn_campaign_20261112/ipm_audit/FUTURE_CONSTRAINED_STEP.md).

The finite source dictionary, nearly coalescent radial powers near \(c_l=1\), coefficient norms around \(3\times10^5\), sampled quadrature and unresolved narrow core ridge remain material limitations. The campaign did not reproduce an unstable branch, determine stability, certify a value of \(c_l\), prove existence, or obtain a uniformly small physical residual. Its positive result is narrower: measured canonical-consistent IPM improvements and a demonstrated way to prevent false finite-far gains from concealing a severe asymptotic error.
