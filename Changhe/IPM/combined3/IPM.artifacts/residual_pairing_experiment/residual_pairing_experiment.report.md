# Sharper residual-pairing experiment for exact Candidate013

This is an isolated, fixed-source experiment. It does not alter Candidate013 or the main stationary-IPM campaign. Numerical values below are screening evidence unless explicitly identified as exact algebraic facts.

## Principal finding

For the exact residual \(F_*\), the proposed whole-plane quantity

\[
D(F_*)=\|J^{2.1}(W^2J^{2.1}F_*)\|_{L^2(\mathbb R^2)}
\]

is **infinite**, even though its well-resolved, localized finite-box analogue is approximately 214. Here \(W=(1+4r^2)^{1/2}\), \(J^{2.1}=(1-\Delta)^{1.05}\). The obstruction is an actual algebraic tail, not insufficient numerical resolution.

The whole-plane numerical result is **\(Q(F_*)\simeq0.0050494\)**, with estimated absolute screening uncertainty about \(10^{-7}\). A Gaussian high-pass split has finite D and gives a promising numerical pairing bound approximately **\(9.79\times10^{-5}\)** at the specified radii, about 5.0% of the direct \(Q(F_*)M\) estimate. Neither fractional norm estimate is a rigorous certificate.

The exact far-field expansion starts with

\[
 F_*(r,\theta)=r^p a(\theta)+o(r^p),\qquad
 p=-\frac{11375183046454913}{4076476460239181}
 =-2.7904449240429297\ldots,
\]

where \(a\) is a nonzero, finite sine polynomial. In particular its sine-111 coefficient is the nonzero rational

\[
 a_{111}=\frac{75721217446012923983908031612974761599527058671478788160285}
 {2696369547882770748177000442961031902060190232476045113355665408}
 =2.8082655623176856\times10^{-5}.
\]

The angular coefficient norm is numerically \(\|a\|_{L^2(S^1)}=1.63843936711436\times10^{-4}\). A separate nonzero \(r^{-3}\sin(3\theta)\) term, with coefficient \(8.210322454454767\times10^{-6}\), would by itself give logarithmic divergence if the leading term were absent.

The independent endpoint calculation is especially simple: the sine-111 potential coefficient at exponent \(\beta=p+2\) is \(-217127111/576460752303423488\). Multiplying this by \((cp-1)(111^2-\beta^2)\) gives the rational above. Exact cancellation of all larger residual powers is checked before conversion to floating point. The finite expansion through radial correction degree two captures every possible residual power at least \(-4\); omitted terms cannot conceal a slower tail.

## Why this proves the finiteness distinction

Every potential atom is a polynomial harmonic \(r^n\sin(n\theta)\) or \(r^n\cos(n\theta)\), multiplied by real-analytic factors of \(r^2\) with positive denominators. Thus the exact fields and their residual are smooth at the origin and on every bounded set. At infinity their differentiated asymptotic expansions obey symbol estimates: each Cartesian derivative lowers the power by one.

For such a smooth algebraic tail, the Bessel multiplier has leading symbol one at physical frequency zero. Equivalently, its exponentially localized nonlocal kernel and the identity \(J^{2.1}=(1-\Delta)J^{0.1}\) give

\[
 J^{2.1}F_*=F_*+O(r^{p-2}).
\]

One way to justify the leading-term assertion is the heat-semigroup representation, with \(\alpha=.05\),

\[
 (1-\Delta)^\alpha g=g+\frac{\alpha}{\Gamma(1-\alpha)}
 \int_0^\infty e^{-t}(g-e^{t\Delta}g)t^{-1-\alpha}\,dt.
\]

Taylor expansion inside the Gaussian convolution, cancellation of its first moment, and the derivative decay give \(g-e^{t\Delta}g=O(t r^{p-2})\) for bounded t; the remaining integral is exponentially localized. Applying \(1-\Delta\) preserves the leading coefficient. This uses the actual smoothness and decay of the exact source, independently of any FFT truncation.

Consequently \(WJ^{2.1}F_*\sim2r^{p+1}a\), which is square integrable because \(p<-2\). However \(W^2J^{2.1}F_*\sim4r^{p+2}a\), whose squared radial integral behaves as \(16\|a\|_{S^1}^2\int r^{2p+5}dr\), and \(2p+5=-0.5808898480858594>-1\). This function is not in \(L^2\). If applying \(J^{2.1}\) made it an \(L^2\) function, applying the bounded inverse \(J^{-2.1}:L^2\to L^2\) would imply that the original function was in \(L^2\), a contradiction. Thus \(D(F_*)=\infty\).

For the unmodified output restricted to a ball of radius \(T\), the leading divergence is

\[
 D_T\sim \frac{4\|a\|_{S^1}}{\sqrt{2p+6}}T^{p+3}
 \simeq0.0010123\,T^{0.2095550759570703}.
\]

This asymptotic contribution remains hidden under the approximately 214 core norm on all ordinary Cartesian FFT boxes. A convergence table of such boxes cannot establish finiteness.
Smoothly cutting off the source changes the asymptotic prefactor but retains the power \(T^{p+3}\).

## Exact source and method

The source is frozen Candidate013 with \(c=4076476460239181/2251799813685248\). The original source hashes are:

- Candidate007 base: `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`.
- Candidate013 correction: `a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a`.

The authoritative `coercivity_residual/fields013.py`, `asymptotics013.py`, and `residual_modal_screen.py` are imported read-only. Residual coefficients are formed and cancelled in Arb before conversion to binary64. Large separately interpolated fields are never subtracted to form a residual. The inherited cache `residual_modal_v02.float.json` has SHA256 `68156301d9e52e71bdbf35c5ac88dc9b937ac666d8a21c375c2ee88cc59c8811` and 1,680 radial rows. New far-field point values and all experiment outputs are stored only in this directory.

`exact_far.py` performs exact rational homogeneous differentiation and trigonometric polynomial convolution. `verify_leading_mode.py` independently obtains the sine-111 coefficient directly from the correction potential's endpoint polynomial values. `far_validate.py` evaluates the actual residual in Arb at very large radii to check the asymptotic coefficient without using its truncated expansion. `exact_origin.py` obtains its exact Taylor polynomial through degree nine; in particular the residual begins at degree three, with sine-one coefficient .223975765292043 and sine-three coefficient .0240596468749523.

`fft_pairing.py` reconstructs the residual from cancellation-resolved sine modes using a degree-seven spline in log radius, applies a smooth source cutoff \(\exp[-(r/C)^{16}]\), and uses a Cartesian FFT on \([-L,L)^2\). **The physical multiplier is**

\[
 k_i=2\pi\operatorname{fftfreq}(N,\Delta x),\qquad
 j(k)=(1+k_x^2+k_y^2)^{1.05}.
\]

With SciPy's backward FFT normalization, physical squared norms use \(\Delta x^2\sum|u|^2\), or \(\Delta x^2N^{-2}\sum|\widehat u|^2\). The weight is applied after the first Bessel multiplier. These are the requested norms, distinct from \(\|J^{2.1}(WF_*)\|_2\).

## Cartesian resolution evidence

For \(L=8,C=6\), the following values are for the localized source and therefore are not the whole-plane \(D\).

| N | dx | Q of localized source | D of localized source | D energy above 70% axial Nyquist |
|---:|---:|---:|---:|---:|
| 512 | .03125 | .003850643774893 | 71.0811993452 | .60017 |
| 1024 | .015625 | .004681241592145 | 187.1132360917 | .84132 |
| 2048 | .0078125 | .004789058934268 | 213.9626468403 | 3.54e-5 |
| 4096 | .00390625 | .004789058934252 | 213.9626469396 | 8.59e-10 |

The last refinement changes Q by \(1.65\times10^{-14}\) and localized D by \(9.93\times10^{-8}\). These differences measure resolution error for the chosen interpolant and cutoff; they do not enclose interpolation, localization, or far-field error. At 4096, the maximum first-multiplier field on the four-row boundary band is \(1.56\times10^{-12}\), while the weighted field there is \(4.48\times10^{-10}\).

Different Cartesian domains give:

| L | C | N | Localized Q | Localized D |
|---:|---:|---:|---:|---:|
| 4 | 3 | 2048 | .00449438094004 | 213.258284289 |
| 8 | 6 | 4096 | .00478905893425 | 213.962646940 |
| 16 | 12 | 4096 | .00485306525437 | 213.996691162 |

The source localization error is therefore much larger than the final mesh-refinement differences.

### Interpolation regularity and density

The value-only splines have degree seven and are C6 across knots, which accommodates the 4.2 derivatives in the twice-applied Bessel operator. A C2 cubic spline or C2 piecewise quintic Hermite interpolation would not, in general, be in H4.2; apparent stability of a fixed cutoff could conceal knot artifacts. These lower-regularity interpolants are not used for D.

The following checks all use the same resolved \(N=2048,L=8,C=6\) Cartesian calculation:

| Cache / spline | Localized Q | Localized D |
|---|---:|---:|
| 1,680 rows, degree 5 (C4) | .00478905422479 | 213.962691843 |
| 1,680 rows, degree 7 (C6) | .00478905893427 | 213.962646840 |
| 1,680 rows, degree 9 (C8) | .00478905899787 | 213.962647370 |
| 848 rows, degree 7 (C6) | .00478902012001 | 213.962402424 |

Thus source/interpolant variation, rather than the last Cartesian refinement, sets the useful numerical precision. In FFTLog the exact degree-nine origin polynomial is joined with a C-infinity transition over radii approximately 2e-5–4e-5. The far asymptotic continuation is also joined smoothly over 1e9–1e10. These transitions avoid artificial derivative jumps at the ends of the radial cache.

## Whole-plane Q and far-field accounting

The own Arb-resolved cache contains 337 additional log-spaced radial rows from 64 to 1e10. Above that scale the exact homogeneous expansion through power -4 supplies the continuation. Its actual pointwise angular-L2 discrepancy is 0.0193% near 1e9 and 0.000360% at 1e10, where the source is already extremely small. This is a numerical continuation check, not a remainder certificate.

The asymptotic regime is genuinely late. Actual Arb evaluation gives:

| r | r^-p times angular L2 norm of F | r^-p times sine-111 coefficient |
|---:|---:|---:|
| 1e4 | .405295941054 | -4.36975232782e-6 |
| 1e6 | .002414317872 | 2.79973558313e-5 |
| 1e8 | .000163722656 | 2.80815067799e-5 |
| 1e10 | .000163851645 | 2.80825327115e-5 |
| 1e14 | .000163844289 | 2.80826540078e-5 |
| exact leading limit | .000163843937 | 2.80826556232e-5 |

To compute the weighted norms without a Cartesian box reaching these radii, `hankel_pairing.py` applies FFTLog separately to each angular harmonic. For

\[
 H_n(k)=\int_0^\infty f_n(r)J_n(kr)r\,dr,\qquad
 h_n(k)=(1+k^2)^{1.05}H_n(k),\quad t=\log k,
\]

Parseval and the Fourier identity \(r^2\leftrightarrow-\Delta_k\) give

\[
 Q^2=\pi\sum_n\int\left[k^2h_n^2+4(\partial_t h_n)^2+4n^2h_n^2\right]dt,
\]

\[
 D^2=\pi\sum_n\int(1+k^2)^{2.1}
 \left[h_n-4k^{-2}(\partial_t^2h_n-n^2h_n)\right]^2 k^2\,dt.
\]

The second identity is applied to the finite high-pass source. The Bessel argument is physical kr, so k already denotes angular frequency. A localized-source cross-check against the Cartesian FFT gives Q=.00478905264 and D=213.96263156 at 16,384 log nodes, agreeing with the Cartesian values to 6.3e-9 and 1.6e-5 respectively. This independently checks the transform normalization and both weight placements.

On the log radial domain 1e-8–1e22, bias -1, and physical frequency integration 1e-15–1000, the full-source results are:

| Log nodes | Q | D of high-pass, lambda=1e-7 |
|---:|---:|---:|
| 16,384 | .005049322349 | 214.950238349 |
| 32,768 | .005049377021 | 214.950377310 |
| 65,536 | .005049380452 | 214.950386018 |
| 131,072 | .005049380666 | 214.950386564 |

Additional log domains extending to 1e14 and 1e18, with biases 0 and -.5, give Q=.005049379801 and .005049380570. Changing the frequency upper limit from 500 to 2000 changes Q by less than 3e-15 and high-pass D by about 2e-7. Degree-5 versus degree-9 splines change the high-pass D by 6.4e-4. Halving the new far-cache density changes Q by 4.9e-8 and high-pass D by 3.3e-7. These diagnostics support conservative screening uncertainty estimates **1e-7 for Q and .01 for high-pass D**; they do not prove interval bounds.

The full-source L2 value is approximately 7.96045e-7, consistent with the independent main-campaign certified upper bound 7.961207e-7.

The far-field effect is also visible by varying the smooth source cutoff C within the radial calculation:

| C in exp[-(r/C)^16] | Q of localized source |
|---:|---:|
| 6 | .004789055117 |
| 12 | .004853061453 |
| 48 | .004864305861 |
| 192 | .004864739690 |
| 1e3 | .004868587621 |
| 1e4 | .005035008797 |
| 1e6 | .005049377020 |
| full source | .005049380666 |

These extent rows use 32,768 log nodes, so the final differences include their approximately 4e-9 log-discretization error. The apparent plateau from C=48 through 1e3 misses the broad distant contribution. The sine-115 harmonic contributes approximately 2.14e-6 to full Q squared, about 8.4% of the total; retaining high angular modes matters.

Unmodified-source `D_with_kmin` values in the saved FFTLog JSON are infrared-conditioned diagnostics of a divergent target. Some vary greatly with bias, lower frequency cutoff, and roundoff. They are deliberately **not** interpreted as whole-plane D or used to infer the divergence power. The exact tail calculation supplies that conclusion.

## Comparison at the user-specified radii

The radii used throughout this experiment are exactly \(R=4.549261\times10^{-7}\), \(M=.387\), independently of any main-campaign changes.

For the whole source, the direct numerical estimate is \(Q(F_*)M\simeq.00195411032\), while \(D(F_*)R=\infty\). A finite D would need to be below approximately 4295.45 to beat this numerical Q value. Certifying a finite bound such as \(D\lesssim6500\) for the unmodified source is impossible.

For the localized core above, \(D_C R=9.73371925\times10^{-5}\), whereas \(Q_C M=.00185336580756\). This tempting 5.25% ratio is **not a valid whole-plane comparison**.

## Finite high-pass alternative

A Gaussian frequency split is tested with

\[
 P_\lambda=e^{\Delta/(2\lambda^2)},\qquad
 F_{\rm hi}=(I-P_\lambda)F_*.
\]

The high-pass acts on **F before** either Bessel multiplier or weight. For each fixed positive \(\lambda\), its leading far power is \(p-2\), since \((I-P_\lambda)F_*=-\Delta F_*/(2\lambda^2)+O(r^{p-4})\). Thus \(D(F_{\rm hi})\) is finite. The resulting legitimate candidate inequality is

\[
 |\langle WJ^{2.1}F_*,WJ^{2.1}f\rangle|
 \le R\,D(F_{\rm hi})+M\,Q(P_\lambda F_*).
\]

Whole-plane screens, including that broad intermediate far field, give:

| lambda | Q of low-pass | D of high-pass | R D_high + M Q_low |
|---:|---:|---:|---:|
| 1 | .001353349627 | 213.998220 | .00062109968 |
| .01 | .001283882420 | 214.015094 | .00059422355 |
| 1e-4 | .000216379012 | 214.522232 | .00018133044 |
| 1e-6 | 3.479166108e-6 | 214.945200 | .00009913062 |
| 1e-7 | 3.492257023e-7 | 214.950387 | .00009792169 |
| 1e-9 | 3.492292567e-9 | 214.950603 | .00009778799 |

The stable choice lambda=1e-7 gives a candidate bound 9.79216914e-5, or **5.011%** of the direct numerical Q M value. The finest two log grids change this objective by about 2.5e-13; the conservative interpolation-based D uncertainty .01 would instead correspond to about 4.55e-9 uncertainty in the objective. This remains screening evidence, not a certified upper bound.

The objective is nearly flat for very small lambda. Smaller tested lambda=1e-9 gains only 0.14% over lambda=1e-7; no exact optimizer is claimed. The high-pass norm is far below both 6500 and the numerical competitive threshold 4295.45.

Small Cartesian boxes would give false reassurance for the low piece: at lambda=1, cutoff C=6 gives Q_low about 3.97e-7, whereas the full source gives .00135335. At lambda=.25 even the localized-source Cartesian and radial low-piece values differ by about 20%, due to periodic Gaussian images on the small box. The reported whole-plane split uses the radial calculation instead.

## Limitations and certification status

The exact nonzero leading coefficient and the smoothness/decay argument rule out finite whole-plane D. Cartesian FFT values, spline interpolation, FFTLog calculations, quadratures, and their differences remain numerical evidence. They are not Arb enclosures of either fractional norm.

**Worth certifying:** the Gaussian high-pass split, whose numerical pairing improves the direct Q M estimate by about a factor of twenty. Even lambda=1 offers about a factor of three, potentially with simpler bounds. Any certificate must enclose the actual low-piece Q and high-piece D, including the intermediate far field and fractional multiplier errors. The tiny box-only low-piece values are unusable for that purpose. Exact Arb Taylor fields are preferable to interpolants for a rigorous certificate.

**Not worth attempting:** a finite certificate for the original D; its exact tail forbids one. No main-campaign argument, candidate, cache, environment, checkpoint, or job was changed by this experiment.

## Reproduction and saved artifacts

All numerical children ran one at a time with SCHED_IDLE, BLAS/OpenMP threads set to one, and FFT workers one. From this directory, for example:

```bash
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B exact_far.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B verify_leading_mode.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B exact_origin.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B extend_radial.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B domain_batch.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B hankel_batch.py
chrt --idle 0 env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/ipm-combined3-venv/bin/python -B summarize.py
```

The cache extension checkpoints each new radius; batch scripts preserve existing output files. Initial Cartesian resolution cases can be repeated with `fft_pairing.py --grid N --radius 8 --cutoff 6 --out output.json`.

The consolidated actual values and convergence tables are in [summary.json](summary.json). Exact far coefficients are in [exact_far_result.json](exact_far_result.json), the independent endpoint identity in [leading_mode_independent.json](leading_mode_independent.json), actual large-radius values in [far_validation.json](far_validation.json), and the finest full-source result in [hankel_full_n131072_bm1_r22.json](hankel_full_n131072_bm1_r22.json). Individual Cartesian and FFTLog JSON files preserve all settings and diagnostics. All files written by this experiment remain in this isolated directory.
