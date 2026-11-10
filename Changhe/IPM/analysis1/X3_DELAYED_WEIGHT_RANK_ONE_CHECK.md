# X3 delayed-weight and rank-one check

Date: 2026-11-07, America/Los_Angeles.

**Result:** all requested weights have positive sampled transport energy and repair the previous vertical-axis example. The tested fixed-speed matrices also have positive symmetric energy. However, every candidate retains a substantially negative **off-axis principal-symbol margin**, so these finite matrices do not support a continuum direct-coercivity claim. The finite Schur scalars stay away from zero, but their response approximations have large spatial residuals. Continuum invertibility and Schur nondegeneracy remain unestablished.

## Comparison

Energy means minus the real weighted pairing divided by the squared norm. The tested minima below are generalized symmetric-energy eigenvalues on the same 18-function span as the [previous quick estimate](X3_WEIGHTED_L2_QUICK_ESTIMATE.md).

| Quantity | \(s=1/2,R=1\) | \(s=3/4,R=10\) | \(s=3/4,R=30\) | \(s=3/4,R=100\) |
|---|---:|---:|---:|---:|
| Minimum sampled transport coefficient | **0.893368** | **1.867314** | **2.963266** | **3.369758** |
| Minimum sampled principal-symbol margin | **−7.109899** | **−7.037668** | **−5.176114** | **−4.623067** |
| Minimum tested transport energy | 0.906478 | 3.120810 | 3.419779 | 3.434239 |
| Minimum tested Darcy energy | −0.454828 | −0.472817 | −0.466129 | −0.464174 |
| Minimum tested \(\mathcal L_0\) energy | **0.860917** | **3.428185** | **3.429457** | **3.443804** |
| Minimum tested rank-one energy | −280.14 | −174.66 | −252.27 | −392.76 |
| Minimum tested complete energy | −273.99 | −168.73 | −246.31 | −386.79 |
| Projected Schur scalar, 18 functions; **finite only** | 0.852687 | 0.890932 | 0.895552 | 0.899480 |
| Continuum Schur interpretation legitimate yet? | No inverse established | No inverse established | No inverse established | No inverse established |
| Residual / complete column weighted membership | Both yes | Both yes | Both yes | Both yes |

Component eigenvalue minima generally occur in different directions and cannot be added as equalities. A large negative rank-one energy has not been interpreted as noninvertibility.

The optional \(s=1,R=30\) comparison gave transport minimum 2.092567, symbol-margin minimum −5.428816, tested base energy 2.714756, rank-one energy −141.60, complete energy −136.01, and projected 18-function Schur scalar 0.896298.

## Reference and scope

The reference and canonical Green conventions are unchanged from the [profile audit](../case1/X3_CURRENT_PROFILE_AUDIT.md) and previous quick estimate: the exactly joined, strain-repaired 260-mode modal object defined from `IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz`, SHA-256

```text
a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874
```

Here \(k=1615536043799051/2^{53}\), \(\bar c_l=1/k\). The raw X3 profile was not used. The complete moving-tail column is exactly the previous calculation's fixed-\(\Theta\), \(\log r\) family with the last-ten-splines cutoff, not an unconverted \(\log(r/r_+)\) column. Numerically \(3-\sigma[\zeta]\simeq3.018048609275\), and

\[
M=\frac{X\cdot\nabla\bar\rho+\mathcal L_0\zeta}
        {3-\sigma[\zeta]}.
\]

Its leading far-field cancellation was retained. The final operator remains \(\mathcal L=\mathcal L_0+M\sigma\); speed variation was not dropped from the final problem.

Existing fine background fields were reused. The preceding run had saved energy summaries but not the individual perturbation-image arrays, so the same 18 images were reconstructed once, then cached and reweighted for all candidates. Temporary scripts, image cache and JSON results are in `/tmp/x3_delayed_weight/`; only this report was added to the repository. There was no profile modification, profile optimization, high-order analysis or interval campaign.

## Transport repair and the remaining symbol problem

With \(m_{s,R}=(1+r^2/R^2)^{-s/2}\), the previous integration-by-parts identity changes only through

\[
\tfrac12\bar{\mathbf v}\cdot\nabla\log m_{s,R}
=-\frac{s}{2}\frac{\bar{\mathbf v}\cdot X}{R^2+r^2}.
\]

Consequently the requested \(\kappa_{s,R}\) formula is correct. Spectral axis limits were used throughout.

The scan covered 24,577 logarithmic radii on approximately \([7.65\times10^{-6},7.65\times10^8]\) and 1,025 closed-quadrant angles, with reflection to the plane. It found **no negative transport samples** for any tested candidate.

| \((s,R)\) | Location of global sampled minimum | Minimum on \(1\le r\le100\) | Far limit |
|---|---|---:|---:|
| \((1/2,1)\) | \((0,3.95255)\) | 0.893368 | 4.181521958 |
| \((3/4,10)\) | \((0,20.50228)\) | 1.867314 | 3.484601632 |
| \((3/4,30)\) | \((0,82.88800)\) | 2.963266 | 3.484601632 |
| \((3/4,100)\) | \((0,528.26718)\) | 4.158152 | 3.484601632 |
| \((1,30)\), optional | \((0,82.88800)\) | 2.092567 | 2.787681305 |

Each listed middle-region minimum is also the sampled vertical-axis minimum in that region. Analytically \(\kappa_{s,R}\to\bar c_l\) at zero and \(\bar c_l(1-s/2)\) at infinity. Positive sampled minima and positive endpoint limits are not a continuous-domain certificate. No extra scan of \(R\) was necessary to find positive sampled transport.

The Darcy symbol loss survives this repair:

| \((s,R)\) | Minimum of \(\kappa_{s,R}-(|\nabla\bar\rho|-\bar\rho_y)/2\) | Location \((x,y)\) |
|---|---:|---|
| \((1/2,1)\) | −7.109899 | \((3.49875,11.53385)\) |
| \((3/4,10)\) | −7.037668 | \((3.73228,14.61442)\) |
| \((3/4,30)\) | −5.176114 | \((4.08166,13.99466)\) |
| \((3/4,100)\) | −4.623067 | \((4.09217,11.95464)\) |
| \((1,30)\), optional | −5.428816 | \((4.09636,15.44565)\) |

These points are away from both axes. The previous scan's largest symbol penalty was about 10.141886 near \((4.09310,11.78015)\), exceeding even the undamped coefficient \(\bar c_l\simeq5.57536\). Delaying radial decay cannot make that principal-symbol test positive there when the radial drift is outward.

This distinction is consequential: the small smooth basis does not resolve localized high-frequency directions. Off the axes, the weight and conjugation are smooth, and such packets sample the displayed symmetric principal symbol. Thus the negative margins indicate an obstruction to **direct continuum coercivity**, despite positive base energy in the tested span. Their signs were not interval-certified here, and no wave-packet refinement was pursued after this clear numerical obstruction. Neither a negative energy nor a failed coercivity criterion proves noninvertibility.

## Rechecking the earlier examples

For the same compact vertical-axis test

\[
h=x^2y\,\Phi\!\left(\frac{\log(r/4)}{0.3}\right)e^{-1024x^2/r^2},
\]

the separate signed ratios are:

| \((s,R)\) | Transport | Darcy | Rank one | Complete |
|---|---:|---:|---:|---:|
| \((1/2,1)\) | 0.906531 | 0.006279 | 0.000132 | **0.912942** |
| \((3/4,10)\) | 4.493125 | 0.006308 | 0.000132 | **4.499566** |
| \((3/4,30)\) | 5.436301 | 0.006310 | 0.000133 | **5.442743** |
| \((3/4,100)\) | 5.562619 | 0.006310 | 0.000133 | **5.569061** |
| \((1,30)\), optional | 5.389962 | 0.006310 | 0.000133 | **5.396405** |

Thus the former local negative test is repaired in all cases.

The inner/tail-transition pair uses the previous radial functions \(h_3,h_{3250}\), with the same amplitudes and logarithmic widths. Minimizing again over this **two-dimensional span** gives:

| \((s,R)\) | Minimum base energy | Minimum rank-one energy | Minimum complete energy |
|---|---:|---:|---:|
| \((1/2,1)\) | **4.281501** | −217.28 | −212.67 |
| \((3/4,10)\) | **3.586188** | −141.44 | −136.69 |
| \((3/4,30)\) | **3.586343** | −209.42 | −204.58 |
| \((3/4,100)\) | **3.588104** | −327.70 | −322.86 |
| \((1,30)\), optional | **2.891070** | −117.27 | −112.79 |

The mixed rank-one negative direction persists, while removing rank one leaves positive energy on this pair. For example, for \((3/4,30)\), \(h_3-0.01539594h_{3250}\) has complete energy about −204.58. This does not determine the Schur scalar.

## Schur calculation and its legitimacy

### What the historical results allow

Analysis III verification proofs `21_radial_fredholm` and `76_actual_modal_fredholm` concern different radial-density or stronger axis-adapted realizations. They do **not** establish a bounded inverse of \(\mathcal L_0\) on the present spaces

\[
H_{s,R}=\{h=\bar\rho g:g\in L^2(m_{s,R}dX)\}.
\]

The earlier membership checks still apply: \(s>2k\) puts the residual and complete column in the target, and \(s<4-2k\) makes \(\sigma\) bounded. These facts do not establish the Darcy mapping bound, the fixed-speed domain, Fredholmness, or injectivity. No specific index/range obstruction was established for this new \(L^2\) realization either. An obstruction from a different historical target must not be transferred to it without justification.

Therefore the continuum inverse formula is **conditional**, not presently available. The appropriate system to retain without assuming an inverse is

\[
\begin{pmatrix}\mathcal L_0&M\\-\sigma&1\end{pmatrix}
\binom{h}{b}=\binom{f}{0}.
\]

Its scalar variable satisfies \(b=\sigma[h]\). If \(\mathcal L_0^{-1}\) exists, eliminating \(h\) gives the requested scalar \(1+\sigma[\mathcal L_0^{-1}M]\). Without that inverse, the bordered system, rather than a scalar inverse formula, is the object requiring analysis.

### Finite calculations

The response solve used the **nonsymmetric Galerkin matrix of the actual operator**, not the symmetric energy matrix. Basis/test functions were orthonormalized with the weighted Gram matrix. For nested spans of sizes 6, 12 and 18, the computed values were:

| \((s,R)\) | \(S_6\) | \(S_{12}\) | \(S_{18}\) | Base-matrix condition number, size 18 |
|---|---:|---:|---:|---:|
| \((1/2,1)\) | 0.959998 | 0.881489 | 0.852687 | 7.55 |
| \((3/4,10)\) | 0.910064 | 0.923792 | 0.890932 | 6.74 |
| \((3/4,30)\) | 0.901030 | 0.925655 | 0.895552 | 6.75 |
| \((3/4,100)\) | 0.899921 | 0.925728 | 0.899480 | 6.73 |
| \((1,30)\), optional | 0.904089 | 0.928363 | 0.896298 | 8.53 |

The six-function span contains origin, source, inner radial, narrow vertical-axis, tail-transition and far radial tests. The twelve-function span adds origin axis tests, horizontal/vertical \(r=4\) tests and the two oblique tests; the final span adds the remaining radial/far-axis functions. All are from the previous 18-function basis.

Every finite scalar is positive, with distance from zero equal to its displayed value. The projected fixed-speed matrices were nonsingular and not poorly conditioned. The finite bordered matrices had full ranks 7, 13 and 19. However, the complete projected operator had condition numbers approximately \(3.5\times10^3\)–\(1.6\times10^4\) for the four required size-18 cases. A nonzero scalar alone does not control the inverse norm of a large rank-one update.

Most importantly, these were inaccurate response approximations. The Galerkin residual was below \(4\times10^{-16}\) relative to the projected right-hand side, but evaluating the actual image on the spatial grid gave:

| \((s,R)\) | \(\|\mathcal L_0h_{M,18}-M\|_{D}/\|M\|_{D}\) |
|---|---:|
| \((1/2,1)\) | **7.298** |
| \((3/4,10)\) | **8.669** |
| \((3/4,30)\) | **8.669** |
| \((3/4,100)\) | **8.664** |
| \((1,30)\), optional | **10.705** |

Here \(D\) is only the represented radial interval, with both axes included by cofactor limits and all quadrants included by symmetry. These are **finite-domain relative residuals**, not bounds on the full-plane relative residual; the omitted tails were not certified. They changed very little with basis size. The large values demonstrate that a small projected residual is misleading here. The complete-operator consistency residual \(\mathcal Lh_{M,N}-S_NM\) is the same base response residual algebraically and was evaluated with the full column included.

There is an additional consistency requirement: for fixed \(s\), changing finite \(R\) gives equivalent norms on the **same set of functions**. For the same maximal operator realization, a true \(\mathcal L_0^{-1}M\), if unique, and its Schur scalar cannot depend on \(R\). The observed weight dependence is a projection effect, not a different continuum scalar. The present values do not certify nondegeneracy. Given both the large response residual and negative principal margins, no further basis-enrichment campaign was pursued.

## Decision and minimum remaining certificate

1. **Transport:** yes, delaying the weight restores a positive margin throughout the sampled domain; \(s=1/2,R=1\) also succeeds by reducing the decay exponent. Continuous-domain positivity remains to be certified if needed.
2. **Fixed-speed energy:** yes on the tested span, including the old two-function pair. **No continuum coercivity conclusion:** all candidates retain an off-axis principal-symbol obstruction to the direct quadratic-form route.
3. **Rank one:** the finite systems show nonzero Schur scalars and no near-singularity of the projected base matrices. The response residuals prevent a continuum nondegeneracy conclusion. Large negative rank-one energy has not been used to infer singularity.
4. **Best candidate:** \(s=3/4,R=100\) has the strongest sampled transport and tested-base margins among the four required choices. It is the best of these norms for continuing a base-operator diagnostic, not an established best inverse. For fixed \(s\), changing \(R\) changes norm constants rather than the underlying invertibility question. None passes the direct continuum coercivity criterion.
5. **Smallest useful next certificate:** a legitimate base inverse estimate, obtained by a method allowing the observed indefinite energy, together with an actually accurate response residual. If \(\|\mathcal L_0^{-1}\|\le K\), \(\|\sigma\|\le C_\sigma\), and \(e=\mathcal L_0\widetilde h_M-M\) is bounded in the full target norm, then
   \[
   |1+\sigma[\mathcal L_0^{-1}M]-(1+\sigma[\widetilde h_M])|
   \le C_\sigma K\|e\|.
   \]
   A strict inequality \(|1+\sigma[\widetilde h_M]|>C_\sigma K\|e\|\) would certify the scalar step. The current projected responses are not close to meeting this test. If a base inverse is obstructed in the eventual realization, the bordered system must be analyzed directly instead.

All new numerical values are binary64 observations, using the prior NumPy/SciPy evaluator. Energy quadrature used 6,145 radii and 513 angles, with all cross terms. The moving-tail velocity retained its finer grid and analytic logarithmic exterior moment. The prior approximately 0.0035 worst transport integration discrepancy applies to this unchanged basis; the large-span eigenvalues are therefore exploratory. No interval certificate or full Fredholm proof was attempted, and no full-plane inverse is claimed.
