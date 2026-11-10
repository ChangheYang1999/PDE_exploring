# X3 weighted L² quick estimate

Date: 2026-11-07, America/Los_Angeles.

**Verdict: numerical no-go for direct coercivity with either proposed weight.** A simple smooth perturbation near the vertical axis has negative complete energy for both weights, including the variable-speed/moving-tail contribution. In an 18-function span, the moving-tail rank-one term produces substantially larger negative mixed energies. These are numerical counterexamples, not interval-certified inequalities or conclusions about invertibility by other methods.

## Comparison

Here “energy” always means minus the real weighted pairing, divided by the squared weighted norm. The finite-span minima allow arbitrary real combinations of the stated tests.

| Quantity | \(s=3/4\) | \(s=1\) |
|---|---:|---:|
| Minimum sampled transport coefficient | **−1.447629** | **−3.788626** |
| Minimum sampled transport-minus-principal-symbol margin | **−8.486574** | **−9.926909** |
| Most unfavorable tested complete nontransport energy, 18-function span | −123.89 | −55.49 |
| Minimum tested combined energy, 18-function span | **−120.18** | **−52.41** |
| Minimum combined energy among the individual basis functions | −1.421669 | −3.756385 |
| Variable-\(c_l\) term included? | Yes, full moving-tail column | Yes, full moving-tail column |
| Residual weighted \(L^2\) membership | Yes | Yes |
| Analytic far transport limit | 3.484601632 | 2.787681305 |

The \(s=3/4\) weight has better local transport margins. The \(s=1\) weight gives less unfavorable **complete finite-span** energies because it suppresses the distant tail-transition coupling more strongly. Neither passes the requested direct-coercivity test.

## Reference, chart, and evaluation

The background is the exactly joined, strain-repaired 260-mode reference defined from

`IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz`,

with SHA-256 `a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874`, \(k=1615536043799051/2^{53}\), and \(\bar c_l=1/k\). The raw X3 profile was not used. The earlier [profile audit](../case1/X3_CURRENT_PROFILE_AUDIT.md) supplies the factorization and positivity information.

This calculation reused its temporary exactified floating evaluator and fine canonical Green data. New scripts and numerical outputs stayed in `/tmp/x3_weighted_l2_quick/`. No original profile or certificate was modified. No optimization, interval campaign, or nonlinear work was performed.

The moving-tail family is the historical S2 construction

\[
\rho_c=\bar\rho+\chi(r)(r^{1/c}-r^k)\Theta(\theta),
\qquad \zeta=\left.\partial_c\rho_c\right|_{\bar c_l}
=-k^2\chi(r)r^k\log r\,\Theta(\theta),
\]

where \(r^k\Theta\) is the exact leading modal tail. For a concrete cutoff, this audit used the historical numerical choice from Analysis III `numerics/artifacts/code/basis.py`: the sum of the last ten degree-seven modal splines, extended by zero/one. It is zero below approximately \(3151.8417\), and one above \(3332.4356\). Its \(C^6\) regularity suffices for these \(L^2\) computations. The theoretical family and full column are those of Analysis III verification proofs `167_moving_tail_uniform` and `217_full_moving_tail_holder`.

**Chart dependence:** the rank-one numerical values below refer to this cutoff and the displayed fixed-\(\Theta\) family. The numerical basis column called `KP` elsewhere uses \(\log(r/r_+)\); it must be converted before identifying it with this family's \(\log r\) derivative. No unconverted `KP` image was substituted here.

## Transport identity and pointwise diagnostics

Write \(m_s=(1+r^2)^{-s/2}\), \(h=\bar\rho g\), and \(T h=\bar{\mathbf v}\cdot\nabla h-h\). Since

\[
T(\bar\rho g)=\bar\rho\,\bar{\mathbf v}\cdot\nabla g+F_{\bar\rho}g,
\qquad \operatorname{div}\bar{\mathbf v}=2\bar c_l,
\]

integration by parts for the compact tests gives

\[
-\operatorname{Re}\langle Th,h\rangle_{w_s}
=\int m_s|g|^2\left[
\bar c_l-\frac{F_{\bar\rho}}{\bar\rho}
-\frac{s}{2}\frac{\bar{\mathbf v}\cdot X}{1+r^2}
\right]dX.
\]

This independently verifies the requested sign and coefficient. All axis values used spectral limits. In particular, no tiny density values were divided near an axis.

The scan used 24,577 log-uniform radii on \([10^{-6}L,10^8L]\), approximately \([7.65\times10^{-6},7.65\times10^8]\), and 1,025 angles on the closed first quadrant. It retained all 261 nonzero background stream modes. Reflection gives the remaining quadrants. Values below are experimental sampled extrema.

| Diagnostic | \(s=3/4\) | \(s=1\) |
|---|---:|---:|
| Minimum \(\kappa_s\) | −1.447628718 | −3.788625785 |
| Location | \((x,y)=(0,3.952547)\) | Same |
| Maximum \(\kappa_s\) | 8.412449181 | 9.358145106 |
| Location | \((2.451999,0)\) | Same |
| Minimum on \(r<0.1\) | 5.496440 | 5.470133 |
| Minimum within distance 0.5 of \((8.600063805,0)\) | 5.372094 | 5.304337 |
| Minimum on \(1\le r\le100\) | −1.447629 | −3.788626 |
| Minimum on \(r\ge10^3\), within the scan | 3.369494 | 2.634205 |
| Minimum on \(r\ge10^6\), within the scan | 3.484202 | 2.787149 |

At the origin, \(\kappa_s\to\bar c_l\). At the nonzero similarity zeros, its axis limit is \(\bar c_l+2.2528\times10^{-8}\), independent of \(s\). At infinity, \(\kappa_s\to\bar c_l(1-s/2)\).

The negative transport samples lie near the vertical axis. Their polar-coordinate envelopes are:

* \(s=3/4\): \(1.5493\lesssim r\lesssim12.1640\), \(1.21338\lesssim\theta\le\pi/2\).
* \(s=1\): \(1.0549\lesssim r\lesssim26.1330\), \(1.04617\lesssim\theta\le\pi/2\).

These envelopes contain the negative samples; they do not assert that every enclosed point is negative. The negative regions have nonzero width off the axis. Near the minimum, \(\bar{\mathbf v}\cdot X/(1+r^2)\simeq18.728\): the radial weight correction overwhelms the approximately \(5.57536\) unmodified coefficient.

For the Darcy principal symbol, the symmetric frequency-direction matrix is

\[
\begin{pmatrix}-\bar\rho_y&\bar\rho_x/2\\\bar\rho_x/2&0\end{pmatrix}.
\]

Its largest eigenvalue is exactly \((|\nabla\bar\rho|-\bar\rho_y)/2\), verifying the requested expression. The sampled minima after subtraction are:

| Weight | Minimum | Location \((x,y)\) |
|---|---:|---:|
| \(s=3/4\) | −8.486573854 | \((3.21006,11.19768)\) |
| \(s=1\) | −9.926908527 | \((2.97915,10.76527)\) |

Negative-symbol-margin samples extend over polar envelopes approximately \(1.4915\le r\le181.614\), \(\theta\ge0.66115\) for \(s=3/4\), and \(1.0480\le r\le261.869\), \(\theta\ge0.65194\) for \(s=1\). The largest sampled symbol penalty is 10.141886 near \((4.09310,11.78015)\). These are principal-symbol diagnostics, not full Darcy bounds; axis behavior is handled separately by the actual test energies.

## Complete moving-tail contribution

Let \(c[h]=\psi[h]_{xy}(0)\). The physical density increment is \(h+\delta c_l\zeta\). Differentiating \(3c_l-1-c[\rho_c+h]=0\) gives

\[
\boxed{\delta c_l=\frac{c[h]}{3-c[\zeta]}}.
\]

Differentiating the residual family gives

\[
B=X\cdot\nabla\bar\rho+T\zeta+U[\zeta]\cdot\nabla\bar\rho,
\qquad M=B/(3-c[\zeta]),
\]
\[
A h=T h+U[h]\cdot\nabla\bar\rho+c[h]M.
\]

This agrees with the historical full S2 moving-tail linearization. The calculation found

\[
c[\zeta]\simeq-0.018048609275,
\qquad 3-c[\zeta]\simeq3.018048609275.
\]

The canonical Green integral of \(\zeta\) included the exact logarithmic exterior moment; it was not closed by a pure-power fit. The leading dilation terms in \(B\) were combined before evaluation: \(X\cdot\nabla(r^k\Theta)=kr^k\Theta\) cancels \((\bar c_l r\partial_r-1)(-k^2r^k\log r\Theta)\). No norm of the uncancelled speed column was taken. The rank-one energies below are those of the complete \(c[h]M\).

## Test functions and signed energies

Every test was the smooth compact perturbation

\[
h=x^2y\,\bar a(R,0)\,
\Phi\!\left(\frac{\log(r/R)}d\right)Q(\theta),
\quad
\Phi(z)=\begin{cases}\exp(1-(1-z^2)^{-1}),&|z|<1,\\0,&|z|\ge1.\end{cases}
\]

The positive amplitude is only a basis scaling. For horizontal/vertical localization, \(Q=e^{-\beta\sin^2\theta}\) / \(e^{-\beta\cos^2\theta}\); oblique localization uses \(Q=e^{-\beta(\cos2\theta-\cos2\theta_0)^2}\). These functions have the required reflections and vanish near the origin, so their polar definitions extend smoothly to the whole plane. Norms and pairings used the nonsingular variable \(g=(h/(x^2y))/\bar a\).

Basis parameters: origin \((R,d)=(0.08,0.8)\); origin axis tests \((0.3,0.7),\beta=16\); source \((8.600063805,0.1),\beta=1024\), horizontal; middle \((3,0.55)\); horizontal/vertical tests \((4,0.3)\) with \(\beta=64\), plus a narrow vertical test with \(\beta=1024\); symbol-minimum neighborhood \((11.5,0.18),\beta=256,\theta_0=1.29\); diagonal \((8,0.3),\beta=64,\theta_0=\pi/4\); radial tests at \(R=30,100,1000,10000,100000\), each \(d=0.5\); tail transition \((3250,0.12)\); far axis tests \((1000,0.5),\beta=64\). Unspecified angular factors are one.

Here \(T\) is transport energy, \(N\) includes Darcy **and** the full moving-tail column, and \(E=T+N\). All entries are normalized signed ratios.

| Test | \(T_{3/4}\) | \(N_{3/4}\) | \(E_{3/4}\) | \(T_1\) | \(N_1\) | \(E_1\) |
|---|---:|---:|---:|---:|---:|---:|
| origin | 5.556 | −0.002 | 5.554 | 5.549 | −0.002 | 5.547 |
| origin horizontal | 5.963 | 0.017 | 5.980 | 6.091 | 0.017 | 6.108 |
| origin vertical | 4.738 | 0.004 | 4.742 | 4.462 | 0.004 | 4.466 |
| source | 5.556 | 2.560 | 8.116 | 5.550 | 2.556 | 8.106 |
| middle | 3.691 | −1.000 | 2.691 | 3.066 | −0.958 | 2.108 |
| horizontal, R=4 | 7.923 | 1.904 | 9.827 | 8.711 | 1.884 | 10.595 |
| vertical, R=4 | −1.382 | 0.107 | **−1.275** | −3.701 | 0.112 | **−3.589** |
| narrow vertical, R=4 | −1.428 | 0.006 | **−1.422** | −3.763 | 0.006 | **−3.756** |
| symbol-minimum neighborhood | 1.345 | 1.423 | 2.768 | −0.068 | 1.450 | 1.381 |
| diagonal, R=8 | 4.408 | 5.480 | 9.888 | 4.016 | 5.539 | 9.555 |
| R=30 | 3.771 | 2.087 | 5.859 | 3.172 | 2.098 | 5.270 |
| R=100 | 3.567 | 0.867 | 4.434 | 2.898 | 0.870 | 3.769 |
| R=1000 | 3.495 | 0.135 | 3.630 | 2.802 | 0.135 | 2.937 |
| tail transition | 3.489 | 0.142 | 3.631 | 2.794 | 0.142 | 2.935 |
| R=10000 | 3.486 | 0.021 | 3.508 | 2.790 | 0.021 | 2.811 |
| R=100000 | 3.485 | 0.003 | 3.488 | 2.788 | 0.003 | 2.791 |
| far vertical | 3.418 | 0.014 | 3.432 | 2.699 | 0.017 | 2.716 |
| far horizontal | 3.486 | 0.053 | 3.539 | 2.790 | 0.051 | 2.841 |

The symmetric energy and weighted Gram matrices were formed including all cross terms. After diagonal norm scaling, the Gram matrix's smallest eigenvalue was about 0.307. The complete generalized energy minima were −120.18 and −52.41. The separately minimized **tested-span** Darcy energies were only −0.464 and −0.488, whereas the complete moving-tail rank-one minima were −125.92 and −57.69. These component minima occur in different directions and must not be added as equalities. They identify the speed/tail coupling as the largest observed unfavorable contribution, without giving continuum operator bounds.

### Concrete negative tests and refinement

A particularly simple counterexample is

\[
\boxed{h=x^2y\,\Phi\!\left(\frac{\log(r/4)}{0.3}\right)
                  e^{-1024x^2/r^2}.}
\]

It is zero outside \(2.96327<r<5.39944\), and concentrates near the vertical axis. Its amplitude differs from the basis function by a harmless positive constant. Refining to 12,289 radii and 1,025 angles gave:

| Signed ratio | \(s=3/4\) | \(s=1\) |
|---|---:|---:|
| Transport | −1.428059842 | −3.762753239 |
| Darcy | +0.006258769 | +0.006236344 |
| Complete speed/tail column | +0.000132365 | +0.000132367 |
| Total | **−1.421668708** | **−3.756384528** |

Direct differentiation of \(Th\) and the integration-by-parts coefficient formula agreed within \(2.1\times10^{-9}\) in normalized energy. Doubling the radial and angular resolutions changed these displayed total ratios by less than \(10^{-9}\). This is strong numerical evidence of a genuine negative test, not an interval certificate.

There is also a simple mixed negative direction showing the rank-one effect. Let \(h_3\) and \(h_{3250}\) be the radial basis functions defined above, including their stated amplitudes. The refined two-function calculation gave

* \(s=3/4\): \(h=-0.189941199h_3+0.006593521h_{3250}\), total ratio about **−88.73183**.
* \(s=1\): \(h=-0.221474253h_3+0.018092571h_{3250}\), total ratio about **−36.44541**.

For these two-dimensional spans the complete rank-one minima were approximately −92.695 and −39.773. A positive diagonal energy for each separate radial bump therefore misses a large unfavorable cross term.

## Quick analytic membership checks

These use the existing modal asymptotics and positivity, without new interval computation.

* **Residual:** \(F/\bar\rho=O(r^{k-1})\) at infinity. Its weighted square has radial integrand \(O(r^{2k-1-s})\), integrable exactly when \(s>2k\) for the known nonzero leading tail. Both weights satisfy this. Origin and axis limits are regular, so there is no local divergence.
* **Strain:** in the cofactor Hilbert space its dual kernel is \(\bar\rho\sin(3\theta)/(\pi r^3)\). The squared dual integral is finite near zero and has far radial order \(r^{2k-5+s}\), integrable for \(s<4-2k\). Both weights satisfy this. Sampled dual norms were approximately **1.43734** and **1.84384**, respectively; these numerical constants are not certified.
* **Complete moving-tail column:** \(M/\bar\rho=O(r^{k-1}(1+\log r))\), so its weighted square is integrable for \(s>2k\), again true for both. Its finite origin/axis limits give local membership. In contrast, \(\zeta/\bar\rho\sim-k^2\log r\) is not in these spaces; the chart derivative must remain an external tail coordinate. The leading cancellation in \(B\) is essential.
* **Nonlocal images of the tests:** they have regular divided axis limits. Compact physical-parity tests give \(U[h]=O(r^{-3})\), hence \((U[h]\cdot\nabla\bar\rho)/\bar\rho=O(r^{-4})\) away from, and by the factorization also across, the axes. Adding \(c[h]M/\bar\rho\) preserves weighted membership. No integrability obstruction was found for these tests. A bound for the full Darcy map on arbitrary weighted \(L^2\) inputs was not proved.

## Numerical reliability and decision

All new computations were binary64, using NumPy 1.26.4 and SciPy 1.14.1. The first 18-function calculation used 6,145 radii and 513 angles, composite Simpson integration in \((\log r,\theta)\), and the existing six-point canonical Green recurrence. Perturbations were compactly supported, with zero exterior source continuation. The moving-tail velocity used the finer 24,577-radius grid and analytic logarithmic exterior integration. The two-function refinement used 12,289 radii and 513 angles; the single negative test used 12,289 radii and 1,025 angles.

The initial basis's largest transport integration-by-parts discrepancy was about 0.0035, at the narrow tail-transition bump. Refinement reduced the two-function discrepancy below \(6.2\times10^{-6}\); the simple negative test achieved the much smaller error quoted above. Thus the displayed large-span eigenvalues should be read as exploratory values, while the simple negative test has the strongest numerical cross-check. No continuum estimate is inferred from any positive finite eigenvalue, and no numerical value here is claimed interval-certified.

**Answers to the five decision questions:**

1. Neither weight appears promising for direct complete weighted \(L^2\) coercivity on a domain containing these smooth compact tests.
2. The full speed/moving-tail rank-one term produces the largest unfavorable mixed energy. Independently, the radial factor already creates negative local transport energy near the vertical axis.
3. \(s=1\) is less unfavorable for the complete historical-chart finite matrix; \(s=3/4\) is better locally. Neither choice resolves both problems.
4. The boxed annular vertical-axis test is an explicit, converged numerical negative direction for both weights. The two radial-bump combinations supply stronger mixed examples.
5. There is no remaining positive-constant estimate that can make this same quadratic form coercive if the negative tests are confirmed. The smallest useful next validation is a focused enclosure of the simple negative test's quadratic form. A conditional **positive coercivity** theorem would require a change to the proposed energy or admissible class, beyond this quick audit.
