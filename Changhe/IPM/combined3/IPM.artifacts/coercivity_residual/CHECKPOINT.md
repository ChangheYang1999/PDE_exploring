# Candidate 013 coercivity and residual checkpoint

Campaign deadline: 2026-11-05 21:34:55 UTC. This is an intermediate checkpoint, not an existence report.

## Current mathematical status

- No unconditional IPM existence theorem is claimed.
- Direct whole-plane L² certificate is **COMPLETE** in `L2_signed_far_v05/result.json`: theta≤1/80, kappa<0.710328127935052, betaL2>2.087491082264946. All1856 core panels plus the complete origin and infinite exterior pass. Code/source/cache/chunk bindings and the final finiteness audit pass. The larger original v04 backup was intentionally stopped after2208 saved panels once this sufficient complete theorem was validated; that partial backup has no final result and is not the authoritative certificate.
- Independent finite checks passed: 1848 exact Cartesian-polynomial differentiation identities and 2774 Taylor/asymptotic enclosure crosschecks (`verify_fields013.json`). These checks support the numerical machinery; they do not replace the complete cover.
- `source_projection_cubic_v01` completed at 2026-11-04 22:56:29 UTC: the true Riesz-residual coordinate lies in `[-0.000402408 +/- 1.79e-10]`. All 585 core panels and both radial tails were assembled. `matrix_residual_dual_v02` completed at 23:34:16 UTC with all 631 panels and the complete Riesz-vector L² complement. `full_matrix_residual_cubic_v01.cert.json` combines them: at beta=0.70495, the full-plane dual squared is at most 4.375892036716e−5, a 0.0168% improvement over the inherited scalar upper. The inherited global matrix/source premises remain explicit; this is no existence result.
- Exact degree24 far expansion proves theta<=0.007753486 for r>=1149.668827752. Native polynomial integration of all finite far power cross terms in v05 sharply improves the preliminary v02 Minkowski estimate; analytic remainder norms remain explicitly charged. The exact expansion and each Hessian norm have restartable caches.
- The normalized m=115 angular Gaussian residual direction is **COMPLETE**: source c=0.0004959551591671882±6.548e−14; B=0.42391113883761547645; Gamma(beta=.69995)<=0.453730729070 conditional on the root's fresh actual-source M>=0.7I proof. Combined d²<=4.360534121203e−5 and effective source<=0.005524631986057. `full_matrix_residual_m115_v01.cert.json` retains this global-matrix premise explicitly; its evidence-bound flag is false until the root binds its completed matrix proof. The256-bit prototype is marked incomplete; v02 uses higher/adaptive precision and finite assertions. All final m115 scalars pass the audit.
- `scan013_401.json`, `residual_modal_v01.float.json`, Gaussian projection files, and FFT matrix evaluations are FLOAT investigations. None certifies the invariant ball.

## Exact source recovery

Candidate007, omitted from combined2's publication, was recovered in the tracked combined1 snapshot:

`../../../combined1/combined1.artifacts/candidates/C1-N1-007-d2w-j7-e2bal/d2w_j7_n4_E2bal_mid180_exact.json`

SHA256: `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`.

The Candidate013 raw potential correction is read directly, without modification, from combined2. Its SHA256 is `a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a`. Its quotient-base equality with Candidate007 is inherited from the accepted exact identity in combined2's reference-b18s2 audit. Neither old source is copied over or edited.

## Direct L² estimate

The exact signed decomposition gives

\[
\sup_{\|g\|_2=1}\langle g,U[g]\cdot\nabla\rho_*\rangle
\le\theta_*+\kappa_*,\qquad
\theta_* =\sup_X\frac{|\nabla\rho_*|-\partial_y\rho_*}{2},
\]

\[
\kappa_*^2=
\frac{(\log2-1/2)\|D\partial_x\rho_*\|_2^2
 +(3\log2-2)\|D\partial_y\rho_*\|_2^2}{16\pi}.
\]

The completed exact whole-plane upper is kappa<0.710328127935052; the corresponding betaL2 exceeds2.087491082264946. The inherited plain source upper divided by this rate is below3.813768148587e−7. See `A_B_HANDOFF.md` for all final values, premises, replay commands and process receipts.

Theta's interval test avoids cancellation in square roots. For \(T>0\),

\[
\theta(X)\le T\quad\Longleftrightarrow\quad
\rho_x^2\le4T(\rho_y+T),\qquad \rho_y+2T\ge0.
\]

The core cover uses outward Arb trigonometric enclosures and explicitly outward IEEE interval sums/products. Origin and exterior bounds come from exact homogeneous expansions with analytic Cauchy remainders.

## Taylor and endpoint certificates

`fields013.py` groups each exact potential as

\[
G(r)\operatorname{trig}(n\theta),\qquad
G(r)=r^n(1+r^2)^b(t+r^2)^{-v}P\!\left(\frac{r^2}{t+r^2}\right).
\]

All coefficients are combined as exact rationals before Arb evaluation. Cartesian differentiation uses an independently checked polar derivative algebra. For a real center \(r>0\), the outer complex disk \(|z-r|\le r/4\) obeys

\[
\Re(t+z^2)\ge t+r^2/2>0.
\]

Thus all noninteger powers have an analytic branch there. Exact coefficient absolute sums bound every potential on that disk. Cauchy derivative estimates bound every field's radial Fourier coefficient on the inner disk of radius \(r/8\). Actual Taylor coefficients are summed before interval evaluation; the coefficient tail beyond degree \(N\) is bounded by

\[
M\frac{(h/(r/8))^{N+1}}{1-h/(r/8)}.
\]

The true Taylor degree is asserted in code. The default process-global `flint.ctx.cap` silently truncates higher-order power-series products unless raised: this was detected in prototypes before adopting any bound. Prototype directories v01/v02 are explicitly INVALID. v03 lost its process during a host restart and has no panel output. v04 sets the cap correctly and includes explicit analyticity/series-degree assertions.

For Hessian norms, each enclosed Taylor polynomial is squared and integrated exactly in the radial measure \(r\,dr\), with analytic remainder errors added by Cauchy–Schwarz. Angular mode integration is exact. This yields the actual whole-plane quantities in the HS identity once all panels and endpoint bounds are present.

`asymptotics013.py` constructs exact origin powers and far powers in \(r^2\) or \(r^{-2}\). Its finite coefficients use rational binomial sums. The remaining homogeneous differentiated series is bounded through Cauchy's coefficient bound and a geometric ratio no larger than twice the endpoint series ratio. The finite source makes the origin/far analyticity premises explicit rather than assumed.

## Full-matrix residual mechanism

Let \(H=J^{21/10}(WF_*)\), \(v=RH\). The target quantity is

\[
d^2=\int v^T\mathcal M_*^{-1}v.
\]

For smooth scalar tests \(\psi_i\), choose genuine vector tests

\[
\Phi_i=R J^{-1/10}\psi_i.
\]

Then the source coordinates are local, despite the nonlocal vectors:

\[
c_i=\langle RH,\Phi_i\rangle
=\langle WF_*,(1-\Delta)\psi_i\rangle.
\]

If \(\mathcal M_*-\beta I>0\), define

\[
\Gamma_{ij}=\int\Phi_i^T(\mathcal M_*-\beta I)^{-1}\Phi_j,
\qquad B_{ij}=\langle\Phi_i,\Phi_j\rangle.
\]

Weighted Cauchy–Schwarz and Woodbury's identity give

\[
d^2\le\frac{\|H\|_2^2}{\beta}
-\frac1{\beta^2}c^T(\Gamma+\beta^{-1}B)^{-1}c.
\]

This is a rigorous full-matrix enclosure when all three finite objects and the positive matrix condition are certified. It does not identify the Riesz transform pointwise with its input. The cubic source coordinate, Fourier Gram, and actual inverse-matrix Gram are now complete; their combination retains the inherited matrix/source hypotheses and makes only a small quantitative improvement.

The current test is the normalized cubic

\[
\psi=\frac{y}{\sqrt\pi a^2}(2-r^2/a^2)e^{-r^2/(2a^2)},\qquad a=3/200,
\]

for which \((1-\Delta)\psi=[1+8/a^2-r^2/a^4]\psi\). The FLOAT coordinate is about \(-4.02408\times10^{-4}\). Gaussian degree-one tests at widths 0.1,0.2,0.4 give much smaller coordinates and are not being polished.

## FLOAT findings worth following

- Exact-source modal H² residual screen: norm about 0.00316103. Angular energies are largest at m=3,115,5,1. A refined radial quadrature run is in progress.
- The m=1 energy is concentrated near r=0.03, while m=115 is concentrated near r=1.6. A single coarse uniform grid can miss meaningful source energy.
- Initial1024-grid, box-radius16 full-matrix FFT evaluation gave Hq norm about0.0039293, matrix dual norm about0.0025376, and effective source about0.0021306. That grid was underresolved. A4096-grid, box-radius8 screen with cutoff radius6 gave Hq about0.00478849, matrix dual about0.00335969, and effective source about0.00282085 (ratio0.589). Every interpolation, localization, periodic-image, Fourier, and spatial-tail error remains uncontrolled; these are not certified numbers.
- The R≤64 modal screens omit a significant far weighted-L² tail. Inherited||WF||² is about1.8313e−6, concentrated at far radii. Neither the clipped FFT nor the modal H² screen is a whole-plane residual norm. This tail must remain explicitly charged.
- Leading far gradient coefficients were extracted exactly in `leading_far_gradient_exact.json`. Only even harmonics n=0..20 occur at the leading power \(-(1-1/c)\); the Candidate013 correction decays faster and does not alter them.

## Restart

Use `/tmp/ipm-combined3-venv/bin/python -B` with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. Never import the inherited trees without `-B`.

The L², cubic-projection, and inverse-Gram scripts reuse complete matching chunk files. Before restarting after an interruption, verify no prior process is live. Do not change `fields013.py`, `asymptotics013.py`, `source_projections013.py`, or the finite-rank agent's `cubic_heat_certificate.py` while current certificate configurations bind them. Any edit requires a new output configuration/version or a reviewed explicit rebinding; do not silently reuse old chunks.

After a full run, inspect `result.json`, all failed-index lists, source/code hash bindings, and the endpoint proofs before adopting any constant. A run directory without its final assembled result supplies no completed certificate.
