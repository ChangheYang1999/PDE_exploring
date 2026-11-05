# Rigorous fractional Riesz vector for the narrow cubic source test

For physical width a=3/200 let
\[
\psi_a(X)=\frac{y}{\sqrt\pi a²}\left(2-\frac{r²}{a²}\right)e^{-r²/(2a²)}.
\]
It has L2 norm1 and equals −phi21/2−sqrt3 phi03/2 in the normalized Cartesian Hermite basis of physical widtha. The target vector is Phi=R J^-1/10 psi_a. This note certifies the vector fields on0<=r<=.31; it does not itself certify any full-M integral.

## Exact heat representation

For s=1/20,
\[
J^{-1/10}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t}e^{t\Delta}\,dt.
\]
Put t=z²⁰. Then
\[
\Phi=\Gamma(21/20)^{-1}\int_0^\infty e^{-z^{20}}R(e^{z^{20}\Delta}\psi_a)\,dz.
\]
Writing D=a²+2t and w=r²/(2D), Fourier-Laguerre/Hankel evaluation gives
\[
R(e^{t\Delta}\psi_a)
=(C_2(r,t)\sin2\theta,\ C_0(r,t)-C_2(r,t)\cos2\theta),
\]
\[
C_0=-\frac{a²}{\sqrt2}D^{-3/2}M(3/2;1;-w)
+\frac{3a^4}{2\sqrt2}D^{-5/2}M(5/2;1;-w),
\]
\[
C_2=\frac{3a²r²}{8\sqrt2}D^{-5/2}M(5/2;3;-w)
-\frac{15a^4r²}{16\sqrt2}D^{-7/2}M(7/2;3;-w),
\]
where M denotes Kummer1F1. These formulas agree independently with the Cartesian Hermite combination and with the Laguerre Fourier phase. The sign C2 for R1 and −C2 for the cosine2 component of R2 is essential.

The angular L2 integral is exactly
\[
\int_0^{2\pi}|\Phi|²d\theta=2\pi(\overline C_0²+\overline C_2²),
\]
where the bars here denote the real heat-integrated radial coefficients, not complex conjugation.

## Uniform analytic ellipse

For z in the Bernstein ellipse of[0,2] with semiminor b=1/25, its rho parameter is b+sqrt(1+b²). Set
\[
m=(.6²+.04²)^{10},\qquad d_*=a²-2m>0.0001485611.
\]
If Re z<=.6, the ellipse lies in |z|²<=.6²+.04², including its tiny negative real endpoint; hence Re z²⁰>=−m. If Re z>=.6, then |arg z|<=atan(1/15) and20 atan(1/15)<pi/2, so Re z²⁰>=0. Thus Re D>=d*>0 on the entire ellipse. All D powers use a single analytic branch, and Re w>=0 for real r.

Euler's integral for positive parameters A<B proves |M(A;B;−w)|<=1 when Re w>=0. Contiguous identities give the additional bounds
\[
|M(3/2;1;-w)|\le1+\tfrac34|w|,
\]
\[
|M(5/2;1;-w)|\le1+\tfrac53|w|+\tfrac{35}{96}|w|²,
\]
\[
|M(7/2;3;-w)|\le1+\tfrac7{24}|w|.
\]
For example the middle identity is
\(M(5/2;1;z)=M(5/2;3;z)+(5/3)zM(7/2;4;z)+(35/96)z²M(9/2;5;z)\).
All Euler functions on the right have positive A<B.

For r<=rmax=.31 use |w|<=rmax²/(2d*), |D|^-p<=d*^-p and |exp(−z²⁰)|<=exp(m) in the explicit C0,C2 formulas. The companion code encloses the resulting uniform integrand bound M*. No sampled maximum is used.

For n-node Gauss-Legendre quadrature on[0,2], Chebyshev approximation on this ellipse and positivity/exactness of Gauss weights give
\[
|I-Q_n|\le\frac{8M_*\rho^{-2n}}{1-\rho^{-1}}.
\]
At n768, the code certifies this below3.423e-18 for each radial coefficient. All quadrature nodes and weights are rigorous Arb Legendre-root enclosures. Direct real-radial interval evaluation therefore gives a rigorous enclosure simultaneously for every radius in the input interval.

## Heat tail

The discarded z>2 interval corresponds to t>2²⁰. Positive majorants of the exact real formulas, obtained with the preceding Kummer bounds, are decreasing in t and below1 at t=2²⁰ for r<=.31. Since Gamma(1/20)>1 and t^(1/20−1)<=1 there, each omitted mode is bounded by
\[
\Gamma(1/20)^{-1}\int_{2^{20}}^\infty t^{-19/20}e^{-t}dt
\le e^{-2^{20}}.
\]
This is far smaller than the Gauss error. The total field error is added as an absolute Arb radius.

## Reproduction and limits

`cubic_heat_certificate.py` produces the uniform bound and sample values in `cubic_heat_certificate.json`. Construct `CubicHeat()` and call `.modes(r_interval)` for subsequent whole-core integration. It returns R1sin2, R2cos0 and R2cos2 coefficients. The interval dependence of Kummer expressions may require radial subdivision for a useful L2 lower bound. Such overestimation does not invalidate the enclosure.

The exact full L2 norm of Phi is independently certified by Tricomi-U moments as0.3965327004091046030380315629 in `fractional_riesz_cubic_gram.json`. A rigorous core lower Q and the admitted global M*−.7I>=.004955805507I imply a tail bound (B−Q)/.004955805507 for the relevant inverse-matrix test norm. The full profile-dependent Gamma certificate remains a separate obligation.
