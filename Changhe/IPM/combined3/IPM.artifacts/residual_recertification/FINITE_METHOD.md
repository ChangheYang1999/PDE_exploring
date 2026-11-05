# Finite annulus residual certificate

The producer uses the immutable Candidate007 and Candidate013 exact rational files loaded and SHA256 checked by `fields013.Evaluator`. It computes the potential derivatives defining the actual unchanged residual, then convolves the exact angular expansions with Arb-enclosed radial Taylor coefficients. It does not read a historical residual norm, a historical quadrature table, a historical endpoint certificate or a historical complex majorant.

## Exact reconstruction and arithmetic

`fields013.load_groups` groups the exact rational source into terms

\[
G(r)=r^n(1+r^2)^b(t+r^2)^{-v}P\!\left(\frac{r^2}{t+r^2}\right),\quad t>0,
\]

multiplying either a cosine or sine harmonic. Its rational Cartesian differentiation formulas give the density, its two first derivatives, and both velocity components. The Candidate007 terms supply chi and the Candidate013 terms supply phi; rho=-Delta chi_y-Delta phi, psi=chi_xy+phi_x, u=(-psi_y,psi_x).

The fields have the angular parity rho: sine odd; rho_x: sine even; rho_y: cosine even; u1: cosine odd; u2: sine odd. A sine is represented formally as (z^n-z^-n)/2 and a cosine as (z^n+z^-n)/2. Every product in u·grad rho contains exactly one sine, so suppressing the factor 1/i in all sine coefficients preserves every product. The density subtraction has the same parity. The resulting positive Laurent coefficient times2 is the actual sine coefficient of F.

The radial Taylor variable is scaled before polynomial multiplication. If the truncation degree is K, encode the angular Laurent index j and radial index k as j(2K+1)+k. Input radial degrees are at most K, so the product radial degree is at most2K and cannot spill into a neighboring angular index. The Kronecker polynomial product therefore contains every radial coefficient through K of the exact angular convolution. The Laurent shift is chosen from the actual maximal field harmonic. Arb polynomial arithmetic encloses all coefficient roundoff. The independent cross-check uses the existing Acb angular-convolution implementation at five radii for all modal coefficients through radial order2.

## Source-derived complex majorant

For an exact positive radial center c let D=c/4 and R=c/8. On the complex disk |z-c|≤D,

\[
\Re z^2\ge(c-D)^2=9c^2/16.
\]

Indeed the minimum of c²+2ca+a²-b² subject to a²+b²≤D² is attained at a=-D,b=0 because D≤c/2. Consequently every t+z² lies in the right half-plane, all real powers have a single analytic branch, and

\[
|t+z^2|\ge t+9c^2/16,\quad |z^2-c^2|\le2cD+D^2.
\]

Set Z_t=z²/(t+z²), z0=c²/(t+c²). Then

\[
|Z_t-z0|\le\delta_t=
\frac{t(2cD+D^2)}{(t+c^2)(t+9c^2/16)}.
\]

The producer computes the finite polynomial P(z0+w) in Arb power series (its complete degree is at most25). If its coefficients are p_j, it bounds P by sum_j |p_j| delta_t^j. This retains cancellation in the exact grouped source.

Write n=2k+eps with eps in{0,1}. The identity

\[
z^n(1+z^2)^b(t+z^2)^{-v}
=z^{\mathrm{eps}}Z_1^k(1+z^2)^{b+k-v}A_t^v,
\quad A_t=(1+z^2)/(t+z^2)
\]

avoids separately bounding large cancelling radial factors. Z1 is bounded by c²/(1+c²)+delta1. At is bounded by

\[
\frac{1+c^2}{t+c^2}+
\frac{|1-t|(2cD+D^2)}{(t+c^2)(t+9c^2/16)}.
\]

When v<0, its reciprocal is bounded by the corresponding expression with t and1 exchanged. The remaining real power of1+z² uses its lower modulus1+9c²/16 for negative exponent and its upper modulus1+(c+D)² for nonnegative exponent. Summing these potential bounds by angular harmonic gives M_n.

On the inner radial disk |z-c|≤R, Cauchy's inequality bounds the a-th radial derivative of a potential harmonic by a! M_n/(D-R)^a. The exact Cartesian polar differentiation formulas also contain z^-b; bound them by(c-R)^-b and sum their absolute rational coefficients. This produces Fourier l1 bounds for rho, rho_x, rho_y,u1,u2 on the entire inner complex disk. Finally,

\[
H=(|c_l|(c+R)+U_1)B_x+(|c_l|(c+R)+U_2)B_y+B_0
\]

bounds the sum of the absolute angular coefficients of the actual F, uniformly on that disk. Every factor is evaluated with Arb and rounded upward. A containing Arb center for the intended exact rational c is sufficient: all displayed formulas are enclosed at that exact c. The stored R is the lower endpoint of c/8, so using it for later Cauchy estimates is conservative.

## Radial Taylor quadrature

For the exact geometric panel[c-h,c+h], write F=sum_n f_n(r) sin(n theta), with positive odd n≤323. Let P_n be its Taylor polynomial of degree K about c. Cauchy's formula, triangle inequality and summation over finitely many harmonics give

\[
\sum_n\sup_{|r-c|\le h}|f_n(r)-P_n(r)|
\le\delta=H\frac{(h/R)^{K+1}}{1-h/R}.
\]

The l1 form follows by applying Cauchy's integral formula coefficientwise and then summing inside the contour integral; the same H bounds the sum at every point of the contour. It does not multiply the scalar H by the number of harmonics.

Let B=sum_n sum_{k=0}^K |f_n^{(k)}(c)/k!|h^k. Then the difference between the exact modal square sum and its polynomial approximation is bounded by2B delta+delta². Angular orthogonality gives

\[
\int_{c-h\le|X|\le c+h}|F|^2dX
=\pi\int_{c-h}^{c+h}r\sum_n f_n(r)^2dr.
\]

The producer forms the complete degree2K+1 polynomial(c+hx)sum_n P_n(c+hx)² and integrates every even coefficient exactly with factor2h pi/(k+1), enclosed by Arb. The remaining error is at most

\[
e=2h\pi(c+h)(2B\delta+\delta^2).
\]

The final panel lower/upper is the containing polynomial integral minus/plus e, with lower clipped at0. All polynomial coefficient intervals, its integral, B,delta,e,H,R, precision, degree and exact geometry are saved. An independent rational reducer can reconstruct the integral from those raw coefficients and reconstruct the error from the saved scalar bounds; pi can be bounded by an independent rational interval.

## Coverage and high-order data

The finite endpoints are exact rationals. Consecutive panels have right/left ratio17/16, with the last clipped at the exact exterior radius. All panels retain their exact left,right,center,halfwidth; the reducer must verify adjacency and both endpoint identities.

The shared `high_order.panel_energy` uses the same source-enclosed residual Taylor coefficients. It encloses each modal radial derivative through order3 on the whole panel, with Cauchy derivative tail H (K+1)_d R^-d(h/R)^(K+1-d)/(1-2h/R). It saves all containing derivative intervals, their analytic error bounds and all nonnegative modal energy upper bounds. These data supply the independent integer-norm and fractional conversion argument in the final report.

## Equivalent parity-compressed convolution

Later panels use `finite_fast.residual_taylor_fast`. Both velocity fields have only odd angular harmonics (maximal161); both density gradients have only even angular harmonics (maximal162). Therefore the Laurent exponent parity of each factor is known. Encode an odd exponent m as (161+m)/2, an even exponent m as (162+m)/2, and an output odd exponent n as (323+n)/2. This halves the angular polynomial length while preserving ordinary polynomial multiplication exactly. The same radial stride2K+1 prevents radial wraparound. Radial powers used for scaling are precomputed by repeated Arb multiplication. All 2430 coefficients in the five-radius independent Acb comparison pass for both layouts. Every new raw panel records `convolution_layout: parity_compressed`; the initial legacy panels omit that field. The exact original producer is retained as `run_finite_legacy.py`; both algorithms enclose the identical Taylor coefficients of the immutable residual. Restarting the final producer can reuse either layout, or removing the output directory regenerates the entire certificate with the faster layout.
