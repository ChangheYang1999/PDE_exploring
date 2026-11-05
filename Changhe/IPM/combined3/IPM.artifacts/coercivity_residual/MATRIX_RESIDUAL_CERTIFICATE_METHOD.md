# Full-matrix residual certificate: method and obligations

This note specifies an implemented enclosure, not a completed existence theorem. Adopt numerical bounds only after both source-coordinate and inverse-Gram runs have assembled successful `result.json` files and have been independently reviewed.

Set \(q=21/10\), \(H=J^q(WF_*)\), \(v=RH\), and let \(M=\mathcal M_*\) be the actual pointwise matrix. The inherited matrix certificate gives \(M\ge\beta_*I\), \(\beta_*=704955805507/10^{12}\).

## The test vector and its exact source coordinate

For \(a=3/200\), use

\[
\psi_a(X)=\frac{y}{\sqrt\pi a^2}\left(2-\frac{r^2}{a^2}\right)e^{-r^2/(2a^2)}.
\]

Its L² norm is one: substitution \(s=r^2/a^2\) reduces the squared norm to \(\frac12\int_0^\infty s(2-s)^2e^{-s}\,ds=1\). It is a real S1 function. The harmonic-oscillator identity gives

\[
(1-\Delta)\psi_a=\left(1+\frac8{a^2}-\frac{r^2}{a^4}\right)\psi_a.
\]

Define the genuine smooth vector test \(\Phi=RJ^{-1/10}\psi_a\). Riesz isometry and self-adjointness of J imply

\[
c=\langle RH,\Phi\rangle
=\langle WF_*,(1-\Delta)\psi_a\rangle.
\]

Thus the exact-source certificate integrates only the sine-one radial coefficient of \(F_*\). It does not replace \(RH\) pointwise by \(H\).

`certify_source_projection.py` integrates the actual source through cancellation-resolved Arb Taylor coefficients and Cauchy remainder bounds. Both omitted radial tails are bounded using the inherited \(\|F_*\|_2\) and exact polynomial–incomplete-Gamma integrals of \(\|W(1-\Delta)\psi_a\|_2\). The latter test-tail norms were independently evaluated as about 0.0001580291353 at the origin and 0.00000118718094 at infinity, giving a total source-coordinate tail error below \(1.268\times10^{-10}\).

## Exact total Gram

The unitary Fourier transform of the normalized polar Laguerre cubic has magnitude

\[
|\widehat\psi_a(\xi)|
=\frac{a^2}{\sqrt\pi}\kappa\left|2-a^2\kappa^2\right|e^{-a^2\kappa^2/2}|\sin\vartheta|.
\]

Consequently

\[
B=\|\Phi\|_2^2
=\frac{a^4}2\left[
4U(2,29/10,a^2)-8a^2U(3,39/10,a^2)
+6a^4U(4,49/10,a^2)\right].
\]

Both an independent reduction and the finite-rank agent's general Laguerre Gram implementation enclose \(B\) at 0.3965327004091046030380315629004226339938484…. The formula uses the standard Tricomi U integral with its Gamma normalization; all evaluation is Arb ball arithmetic.

The normalization of this integral is the one in [DLMF13.4.4](https://dlmf.nist.gov/13.4.E4). The positive Euler integral used below corresponds to [DLMF13.4.1](https://dlmf.nist.gov/13.4.E1), with the conventional Kummer M obtained by multiplying the displayed regularized function by Gamma(b).

## Certified smooth Riesz vector

The heat formula is

\[
\Phi=\Gamma(1/20)^{-1}\int_0^\infty t^{-19/20}e^{-t}R(e^{t\Delta}\psi_a)\,dt.
\]

The substitution \(t=z^{20}\) gives weight \(e^{-z^{20}}/\Gamma(21/20)\). The scalar radial heat modes are explicit confluent hypergeometric functions, implemented in the independently audited `finite_rank/cubic_heat_certificate.py`. Its certified Gauss rule uses native containing Arb Legendre roots and weights. A Bernstein ellipse of semiminor 1/25 proves a uniform quadrature error below \(3.423\times10^{-18}\) on real radii \(0\le r\le0.31\); the heat tail is charged completely.

The native node/weight enclosure is documented by [FLINT's Gauss–Legendre implementation](https://flintlib.org/doc/algorithms/special-functions/legendre.html).

For completeness, the ellipse bound uses \(D=a^2+2z^{20}\). When \(\Re z\ge0.6\), the ellipse obeys \(20|\arg z|<\pi/2\), so \(\Re z^{20}\ge0\). On the rest of the ellipse, \(|z|^{20}\le(0.6^2+0.04^2)^{10}\), giving \(\Re D\ge0.0001485611378\). Positive Euler-integral hypergeometric representations, after the required parameter recurrences, bound the complex quadrature integrands. These statements concern the heat variable; no complex-r assumption is used in the radial interpolation below.

## Sharp radial interval enclosure without special-function dependency loss

Write

\[
\Phi_1=C_2(r)\sin2\theta,
\qquad \Phi_2=C_0(r)-C_2(r)\cos2\theta.
\]

For any integer \(j\ge0\), the unitary inverse Fourier integral gives the uniform real-radial derivative bound

\[
|C_0^{(j)}(r)|,|C_2^{(j)}(r)|\le D_j,
\quad D_j=\frac{2a^2}{\sqrt\pi}\left[2I_{j+2}+a^2I_{j+4}\right],
\]

\[
I_p=\frac12\left(\frac2{a^2}\right)^{(p+1)/2}\Gamma((p+1)/2).
\]

Indeed, the multipliers R and \(J^{-1/10}\) have norm at most one, a directional derivative costs at most \(\kappa^j\), and extracting a radial sine/cosine coefficient costs at most \(4/\pi<2\). The displayed bound follows by integrating \(\kappa^{j+2}(2+a^2\kappa^2)e^{-a^2\kappa^2/2}\).

On a radial panel centered at r with halfwidth h, evaluate the certified heat vector at the eleven ideal Chebyshev roots. The degree-ten real interpolant has uniform error

\[
\varepsilon_{\rm int}\le D_{11}h^{11}/(2^{10}11!),
\]

because the monic node polynomial is \(2^{-10}T_{11}\). Ideal irrational nodes and DCT coefficients are enclosed by Arb. The polynomial range is bounded by its constant Chebyshev coefficient plus/minus the sum of absolute nonconstant coefficients, with the interpolation remainder added. This derivative/interpolation argument was independently reviewed by the finite-rank agent.

The improved v02 implementation also integrates the squared interpolating polynomials exactly in \(r\,dr\), rather than using pointwise minima for their L² norms. The uniform interpolation error is charged by Cauchy–Schwarz. Angular integration is exact:

\[
\int_0^{2\pi}|\Phi|^2\,d\theta=2\pi(C_0^2+C_2^2).
\]

## Actual inverse-matrix integration and complete tails

Choose any free scalar \(0<\beta<\beta_*\) and set \(N=M-\beta I\). On the core annulus \(10^{-6}\le r\le0.3\), the actual Candidate013 matrix and the certified vector ranges are interval-integrated over radial panels and 256 angular arcs. The determinant/inverse is charged explicitly. If an interval determinant fails positivity, the inherited bound \(N\ge(\beta_*-\beta)I\) provides a conservative fallback on that entire cell.

Let \(\Gamma_{\rm core}\) be the resulting upper and \(Q_{\rm core}\le\int_{\rm core}|\Phi|^2\) the exact polynomial-based lower. The full-plane Gram satisfies

\[
\Gamma=\int\Phi^TN^{-1}\Phi
\le\Gamma_{\rm core}+\frac{B-Q_{\rm core}}{\beta_*-\beta}.
\]

This accounts for both omitted radial tails using the exact total Gram. No pointwise far-field expansion of \(\Phi\) is needed. All angular floating interval operations are rounded outward; final positive sums and radial masses are accumulated in Arb.

## Full-plane dual-norm enclosure

Weighted Cauchy–Schwarz implies \(N\ge|\Phi\rangle\langle\Phi|/\Gamma\). Positive-operator inversion and the rank-one Woodbury identity give

\[
\int (RH)^TM^{-1}(RH)
\le\frac{\|H\|_2^2}{\beta}
-\frac{|c|^2}{\beta^2(\Gamma+B/\beta)}.
\]

Upper endpoints for \(\|H\|_2,B,\Gamma\) and a lower endpoint for \(|c|\) yield a numerical certificate of the entire full-matrix residual functional. Changing the auxiliary baseline \(\beta\) changes the corresponding scalar coercivity comparison; closure must use the same baseline consistently. v02 records several free baseline choices in one source evaluation, including 0.7 and 0.70495. This does not optimize or replace the pointwise matrix minimum.

The coordinate is only one direction. Its improvement can be small even when direct FLOAT evaluations suggest a much larger full-matrix benefit. Such small improvement is reported quantitatively rather than extrapolated to a complete residual norm computation or an existence theorem.

## Reusing the cubic record with a fresh M >= 0.7 certificate

Suppose an independent actual-source cover proves only \(M\ge mI\), with m=0.7. The old cubic core computation used the minimum of a direct interval inverse of \(M-0.7I\), whenever its determinant passed, and the fallback \(|\Phi|^2/\delta_o\), where \(\delta_o=0.004955805507\). Its full-plane tail uses the same denominator \(\delta_o\).

For any new auxiliary \(\beta_n\le m-\delta_o=0.695044194493\), every recorded cell upper is still valid for \(\Phi^T(M-\beta_n I)^{-1}\Phi\). On a cell whose old direct determinant passed, the fresh bound \(M-0.7I\ge0\) makes that matrix positive definite, and adding \((0.7-\beta_n)I\) decreases its inverse. Independently, the fresh global bound gives \((M-\beta_n I)^{-1}\le(m-\beta_n)^{-1}I\le\delta_o^{-1}I\), so the old fallback is also valid. Thus their recorded minimum remains valid without invoking the old global matrix theorem. The exact Gram-complement tail is conservative for the same reason.

Consequently, the saved cubic upper22.9252679512 may be reused as an upper for \(\Gamma(\beta_n=0.69)\) once the fresh M>=0.7 certificate is complete. The new Woodbury comparison must use beta_n=0.69 consistently. This transfer does not reuse the old0.704955805507 matrix premise; it uses the directly computed old local inverse cells, their explicitly larger fallback, and the fresh0.7 global theorem.

## A genuine test for the alternative Q source

For the distinct source \(H_Q=WJ^{21/10}F_*\), one must change the vector test. Set

\[
\Phi_Q=R[W^{-1}J^{-1/10}\psi_a].
\]

Then exactly

\[
\langle RH_Q,\Phi_Q\rangle=\langle F_*,(1-\Delta)\psi_a\rangle.
\]

This follows from \(R^*R=I\), pointwise cancellation of W, and self-adjointness of J; no commutation of W with J is asserted. The local integral on the right remains a separate numerical obligation.

There is also a rigorous perturbation estimate from the legacy vector:

\[
\|\Phi_Q-\Phi\|_2\le2\|r^2J^{-1/10}\psi_a\|_2
<0.001501870983783.
\]

The pointwise inequality \(0\le1-(1+4r^2)^{-1/2}\le2r^2\) and Riesz isometry prove the first step. `q_vector_weight_perturbation.py` evaluates the remaining norm exactly as a finite Gamma–U combination. In Fourier variables s=|xi|², write \(\widehat{J^{-1/10}\psi_a}=ia^2\kappa\sin\vartheta f(s)/\sqrt\pi\), where \(f(s)=(2-a^2s)e^{-a^2s/2}(1+s)^{-1/20}\). The exact identity

\[
\Delta_\xi[\kappa\sin\vartheta f(\kappa^2)]
=\kappa\sin\vartheta[8f'(s)+4sf''(s)]
\]

reduces the squared norm to \(a^4\int_0^\infty s[8f'+4sf'']^2ds/2\). Its certified value is \(5.639041129817378\times10^{-7}\); a separate real quadrature agrees. Consequently, a certified legacy Gamma transfers to the Q-vector upper \((\sqrt\Gamma+e/\sqrt{\beta_*-\beta})^2\), with \(e=0.001501870983783\). No completed Q residual enclosure is claimed from this distance estimate alone.
