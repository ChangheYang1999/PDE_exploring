# Completed A/B handoff

Updated 2026-11-05 00:42 UTC. The campaign deadline remains **2026-11-05 21:34:55 UTC**. This handoff completes this agent's assigned coercivity/residual calculations. It does **not** establish stationary existence or end the root agent's continuing campaign.

## A. Completed direct Candidate013 L² estimate

The authoritative result is [L2_signed_far_v05/result.json](L2_signed_far_v05/result.json), SHA256

`0e9e24ab8fbb02e300a9f375305c95f7ba571ef2f145352362bcbf553043b2e7`.

It proves, directly for Candidate013,

\[
\theta_*\le1/80,\qquad \kappa_*<0.710328127935052,
\]

\[
c+1-\theta_*-\kappa_*>2.087491082264946.
\]

Thus the conservative signed rate **2.08** is available. For compact smooth real tests, and a sufficiently regular divergence-free perturbation transport,

\[
\operatorname{Re}\langle A_kh,h\rangle\le-2.08\|h\|_2^2.
\]

The maximal operator/inverse realization is a separate root/operator-theory obligation. [A_summary.cert.json](A_summary.cert.json) verifies the completed result's code/cache/chunk bindings and gives the a priori ratio

\[
\frac{7.961207\times10^{-7}}{2.087491082264946\ldots}
<3.813768148587\times10^{-7}.
\]

This ratio bounds a solution supplied by the separate inverse theorem; it does not assert that a solution already exists.

The whole-plane proof uses all1856 exact-source core panels from r=10⁻⁵ to r=1149.668827752…, the complete origin expansion, and the complete exterior expansion. Every theta flag passes; the failed-index list is empty. Signed far theta is at most0.007753485521. The three whole-plane Hessian squared uppers are

| Quantity | Certified upper, rounded upward |
|---|---:|
| ||rho_xx||² | 4.673784704104 |
| ||rho_xy||² | 16.942987218688 |
| ||rho_yy||² | 249.756738186891 |

The exact HS identity is

\[
\kappa_*^2=\frac{(\log2-1/2)(\|\rho_{xx}\|_2^2+\|\rho_{xy}\|_2^2)
 +(3\log2-2)(\|\rho_{xy}\|_2^2+\|\rho_{yy}\|_2^2)}{16\pi}.
\]

Its gradient-structured identity and cutoff extension are inherited established analytic results; their numerical inputs here are newly evaluated for013. The actual sublinear profile has gradient tending uniformly to zero and Hessian in L², so its cutoff extension applies. The signed decomposition and origin/far Taylor/Cauchy arguments are detailed in [DIRECT_L2_CERTIFICATE_METHOD.md](DIRECT_L2_CERTIFICATE_METHOD.md).

The improved far integration retains all finite homogeneous cross terms exactly. Powers are grouped modulo2; writing p=p_c−2j and c_j=a_p R^p, native Arb polynomial multiplication evaluates

\[
R^2\sum_j\frac{(P_cP_d)_j}{-p_c-p_d+2j-2}.
\]

Angular orthogonality is exact, and the omitted differentiated analytic tail is added in L². Each exterior analytic remainder is below7.200e−36. The root independently reviewed the signed far proof; the finite-rank agent independently reviewed both the direct cross-power formula and the native polynomial/cache implementation. [A_native_crosscheck_v01.json](A_native_crosscheck_v01.json) records agreement of the direct and native implementations for xx and xy within1e−100.

[A_final_finiteness_audit_v01.json](A_final_finiteness_audit_v01.json) checks71792 containing Arb scalars and4420 machine numbers, including the exact expansion cache, with no NaN/Inf. The invalid initial series-cap prototypes remain explicitly marked INVALID and contribute no adopted value.

## B. Completed genuine full-matrix Riesz residual upper

This calculation concerns **H=J^(21/10)(WF)**, W=sqrt(1+4r²). It is different from the root's Q-source WJ^(21/10)F. No transfer between those sources is asserted.

Write D=(cX+u)·grad(log W). The actual matrix used in every cell is

\[
M=(c+1+D)I-\tfrac{21}{10}(cI+\operatorname{Sym}Du)
 +\begin{pmatrix}\rho_y&-\rho_x/2\\-\rho_x/2&0\end{pmatrix}.
\]

The strongest completed test uses m=115, a=1471/10000 and

\[
\psi=\sqrt{\frac2{\pi\,115!}}a^{-116}r^{115}\sin(115\theta)e^{-r^2/(2a^2)},
\qquad \Phi=RJ^{-1/10}\psi.
\]

Its genuine source coordinate is local:

\[
c_\Phi=\langle RH,\Phi\rangle=\langle WF,(1-\Delta)\psi\rangle,
\quad c_\Phi=0.0004959551591671882\ldots\ \pm6.548\times10^{-14}.
\]

The displayed stored interval is deliberately outward-rounded more coarsely. [source_projection_m115_v01/result.json](source_projection_m115_v01/result.json) includes all73 Taylor/Cauchy panels and both exact polynomial–Gamma tail bounds. The inherited ||F||₂ upper is charged to these tails.

The exact Fourier Gram is B=||Phi||²=0.42391113883761547645…. The heat quadrature has a uniform radial coefficient error below1.379e−23, proved using a complex heat ellipse and the inverse Fourier L¹ bound. Native Arb nodes/weights and special functions enclose point values; real derivative bounds certify eleven-node radial interpolation. The finite-rank agent independently reviewed the angular-Gaussian normalization, Hankel coefficients, signs, complex-heat majorant, Gram, source-coordinate formula and test-tail normalization.

[matrix_dual_m115_v01/result.json](matrix_dual_m115_v01/result.json) includes all73 actual inverse-matrix core panels and1024 angular arcs per panel. Its complete omitted test L² mass is at most1.892758421e−8, obtained from the exact total Gram minus a certified polynomial core lower. The entire test tail is therefore charged; no plane FFT or Riesz-input pointwise substitution is used.

**Remaining explicit premise:** actual M>=0.7I. This is the root's fresh actual-source matrix-cover task. The matrix-dual result is labeled `COMPLETED_ANGULAR_MATRIX_DUAL_GIVEN_GLOBAL_LOWER`; the arithmetic assembly records `global_matrix_evidence_bound:false`. It must not be adopted unconditionally before that premise is discharged. The older0.704955805507 matrix theorem is not needed for this m115 record.

For beta_o=0.69995, it gives

\[
\Gamma=\int\Phi^T(M-\beta_oI)^{-1}\Phi<0.453730729070.
\]

Using the inherited whole-plane source upper n=0.0055545729030073655758, weighted Cauchy–Schwarz and rank-one Woodbury give

\[
d^2:=\int(RH)^TM^{-1}(RH)
\le n^2/\beta_o-\frac{|c_\Phi|^2}{\beta_o^2(\Gamma+B/\beta_o)}
<4.360534121203\times10^{-5},
\]

\[
d<0.006603434046920,\qquad \sqrt{\beta_o}d<0.005524631986057.
\]

[full_matrix_residual_m115_v01.cert.json](full_matrix_residual_m115_v01.cert.json) records every baseline. Its squared upper is0.98931908423 times the corresponding scalar n²/0.7 comparison, an improvement of about1.068% in that upper bound. This is a rigorous upper enclosure with the displayed premises, not a sharp evaluation of d. [m115_B_finiteness_audit_v01.json](m115_B_finiteness_audit_v01.json) confirms all1300 recorded scalars finite.

For a high-order remainder loss epsilon, reuse the same Gamma with beta=beta_o−epsilon, because (M−epsilon I)−beta I=M−beta_o I. `assemble_full_matrix_residual_bound_v02.py --energy-loss <epsilon>` implements this consistent comparison. The inherited source-norm theorem and its accepted source identities/arithmetic/remainders remain explicit premises.

The earlier cubic test is also fully assembled in [full_matrix_residual_cubic_v01.cert.json](full_matrix_residual_cubic_v01.cert.json), with its own explicitly inherited matrix premise. It offers only a0.0168% squared-upper improvement and is superseded quantitatively by m115 for the0.7 comparison. A safe transfer of its recorded Gamma to a fresh M>=0.7 proof with auxiliary beta<=0.695044194493 is documented in [MATRIX_RESIDUAL_CERTIFICATE_METHOD.md](MATRIX_RESIDUAL_CERTIFICATE_METHOD.md).

## Provenance and reproducibility

Fixed c=4076476460239181/2251799813685248. Exact Candidate007 was recovered read-only in combined1, SHA256 `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`. Raw correction013 in combined2 has SHA256 `a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a`. Equality of recovered007 with the accepted quotient base is inherited from combined2's accepted exact bridge. No inherited file was edited.

`fields013.py` SHA256 remains `2ac292c416860432c0b64cb97d66e7e68b17aa12fef126b0979a5b1f0917f23c`; `asymptotics013.py` remains `1d7c89105fd5c4ce2a9d558e278b63fe0e2d39e9079c419221c2694a4b042f21`. Other agents' live certificates still bind these files; preserve them. New variants need new filenames/configurations.

[runtime_environment.json](runtime_environment.json) records Python3.12.3, python-flint0.9.0, numpy2.5.4, scipy1.18.1, mpmath1.4.1 and gmpy2 2.3.2. The venv is external at `/tmp/ipm-combined3-venv` and was recreated after three host restarts. Every inherited import used Python-B; all numerical workers limit BLAS threads to1.

From the repository root, use **fresh output directories** for replay: assemblers update result timestamps and hashes. Cold A replay can run

```sh
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/ipm-combined3-venv/bin/python -B \
 Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/certify_L2_013.py \
 --out Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/A_replay_core \
 --workers 8 --max-panels 1856

env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
 /tmp/ipm-combined3-venv/bin/python -B \
 Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/assemble_L2_signed_far_v05.py \
 --source-out Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/A_replay_core \
 --out Changhe/IPM/combined3/IPM.artifacts/coercivity_residual/A_replay \
 --panels 1856 --expansion-degree 24
```

For B, rerun `certify_angular_source_projection.py`, `certify_angular_matrix_dual.py` and `assemble_full_matrix_residual_bound_v02.py` into fresh directories, then run `audit_certificate_finiteness.py` on those directories. Each producer verifies source/configuration/code bindings and reuses only matching complete chunks. The original A core directory remains intentionally incomplete relative to its larger2994-panel backup target; the completed1856-panel plus infinite-exterior proof is the authoritative A result.

## Jobs and stopping state

Completed sessions: native A **72449**, m115 source **1075**, resumed m115 matrix dual **89129**, B arithmetic and both final scalar audits. A summary/binding verification session17500 also completed.

After validated A>2.08, the parent authorized stopping redundant A backups at their next valid checkpoint. Watcher **68823** completed successfully; [A_backup_stop_receipt.json](A_backup_stop_receipt.json) has status `SUPERSEDED_A_BACKUPS_STOPPED`. It stopped the old direct pair implementation session17657/PID1746 at00:38:01 after preserving its xy norm checkpoint. It stopped the original full-core backup session32692/PID1723 and newly spawned workers2353/2354 at00:39:06 after valid `chunk_02176_02207.json` was saved. All2208 completed backup panels remain preserved. The watcher verified parseable complete records before signaling and touched no root/operator/source/matrix jobs. Authoritative ps at00:41:30 confirmed **no live coercivity_residual jobs**; watcher PID2305 also exited.

If that redundant full-core run is ever intentionally resumed, use its original restart command with `--out .../L2_cert_v04 --workers 2 --chunk 32`; do not change its frozen producer or configuration. It is unnecessary for the completed A theorem. If the native A assembler is interrupted on replay, its exact expansion and individual Hessian-norm caches allow restart using the identical command. The authoritative result and caches are already complete.

## Remaining mathematical status

No stationary IPM existence theorem is asserted here. The root, operator-theory and finite-rank agents continue the campaign's actual local/joint high-order form, operator and nonlinear closure work. The root's fresh M>=0.7 proof is still an explicit B adoption premise at this handoff.

Unused research is clearly separated by status: all FFT residual values remain FLOAT with uncontrolled interpolation/localization/periodic-image/frequency/spatial-tail errors; no clipped far tail is treated as negligible. The S1 reflection identity is saved, and the Mellin multiplier file is a FLOAT m1 investigation, not an actual-source S1 HS bound. The Q-vector perturbation certificate supplies only a test-distance identity, not a Q-source residual bound. None of these investigations is used to claim closure.
