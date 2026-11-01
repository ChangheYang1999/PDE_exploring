# Independent bivariate audit of the nonlinear recurrence

Status: PROVED algebraic identity, independently reviewed in V312. Numerical checks remain finite consistency tests, not an all-order convergence theorem.

## Statement and notation

For the canonical sequence at delta=2/3, c=3, let t=log r and write
F_n(t,theta)=sum_(m odd>0) a_(n,m)(t) sin(m theta) and
G_n(t,theta)=sum_(m even>0) b_(n,m)(t) sin(m theta).
Set p_n=1-2n/3, P_n=2-2n/3 and lambda_n=2(n-1).
The recurrence to be checked is

\[
 (\lambda_n-3\partial_t)F_n
 =\sum_{i+j=n}\left[(P_iG_i+\partial_tG_i)\partial_\theta F_j
 -\partial_\theta G_i(p_jF_j+\partial_tF_j)\right].
 \tag{1}
\]

This follows by expanding the radial and angular derivatives in
(cX+u).grad rho-rho, using u=(-psi_y,psi_x). The linear coefficient is
cp_n-1=-(n-1)(c-1)=-lambda_n, and the nonlinear Jacobian is
r^(-1)(psi_r rho_theta-psi_theta rho_r). Matching i+j=n gives(1).

## Laurent representation and signs

Use a formal variable z=e^(i theta) and define real Laurent polynomials

\[
 \mathcal F_n=\frac12\sum_{m>0}a_{n,m}(t)(z^m-z^{-m}),\qquad
 \mathcal G_n=\frac12\sum_{m>0}b_{n,m}(t)(z^m-z^{-m}).
\]

Thus mathcal F_n=iF_n and mathcal G_n=iG_n after evaluating z on the unit circle.
Let E=z partial_z, so partial_theta=iE. Multiplying(1) by i cancels every
imaginary factor and gives the real Laurent identity

\[
 (\lambda_n-3\partial_t)\mathcal F_n
 =\sum_{i+j=n}\left[(P_i\mathcal G_i+\partial_t\mathcal G_i)E\mathcal F_j
 -E\mathcal G_i(p_j\mathcal F_j+\partial_t\mathcal F_j)\right].
 \tag{2}
\]

For example, the product of an ordinary sine and a differentiated sine has
one remaining sine factor. The transform above retains this sign and the two
factors1/2; the positive-frequency coefficient of mathcal F is half the
ordinary sine coefficient. No trigonometric product routine from the main
implementation is used.

## Kronecker substitution without aliasing

The generated support obeys |m|<=2i for both fields at order i. Fix output
order n and put M_i=2i and K=4n+1. Encode a monomial t^q z^m of an order i
input by x^(Kq+m+M_i). Every exponent is nonnegative. In a product of orders
i and j with i+j=n, the exponent is K(q+v)+m+l+2n, with angular index
0<=m+l+2n<=4n<K. Therefore there is no carry between the angular index and
the logarithmic degree. Ordinary univariate polynomial multiplication
exactly implements the bivariate Laurent multiplication in(2). All products
use the same output shift2n and can be summed coefficientwise.

The angular operator E multiplies each input coefficient by its signed
frequency m. The radial operator P+partial_t replaces the log coefficient
h_q by P h_q+(q+1)h_(q+1). These transformations are applied before packing.
The expected left side uses lambda_n h_q-3(q+1)h_(q+1).

## Verification scope

The script decodes a frozen checkpoint into outward-rounded Arb intervals,
constructs the four packed inputs for every pair i+j=n, and evaluates the
right side by univariate Arb polynomial multiplication. Every coefficient
of its difference from the independently packed left side must contain zero,
including coefficients predicted to vanish by parity or support. It records
an upper bound for the residual coefficient norm, scaled by the forcing norm,
as well as the maximum input and output sizes and actual elapsed time.

This verifies the high-order arithmetic and the implementation's agreement
with the independently derived signs, indices and factors. Interval overlap
at finitely many orders does not establish the infinite recurrence by itself,
nor does it establish convergence. The independent exact low-order derivation
and the source implementation remain separate parts of the overall audit.

## Independent Poisson audit of a complete finite prefix

At stream frequency m=2j, the angular Poisson equation gives

\[
 [m^2-(P_n+D)^2]b_{n,j}
 =\tfrac12[(P_n-m+D)a_{n,j-1}+(P_n+m+D)a_{n,j}].
 \tag{3}
\]

This is obtained directly by expanding p cos(theta)F-sin(theta)partial_theta F,
with p replaced by p+D for logarithmic coefficients. Therefore the coefficient
of t^q on the left is
(m^2-P_n^2)b_q-2P_n(q+1)b_(q+1)-(q+1)(q+2)b_(q+2), and the right coefficient
uses the displayed two adjacent density modes at degrees q and q+1.
Missing coefficients are zero. The separate prefix checker evaluates these
expressions directly, without using either the stored Poisson inverse or a
formal inversion at resonance. It also checks b_(n,j)(0)=0 whenever P_n=-m.
The latter check verifies the chosen canonical harmonic constant, which the
Poisson differential equation alone would not determine.

## Bounded chunks at order290

The order290 nonlinear sum has289 ordered products. To keep each command within the run's time limit, the independent chunk implementation assigns disjoint intervals of the index i to separate bounded jobs. Each partial sum is serialized with the exact dyadic midpoint and radius of every Arb coefficient. The merge decodes those same balls, checks the checkpoint digest, arithmetic precision and order, and verifies that the sorted index intervals cover exactly1 through289 without gaps or repetitions. It then adds the partial sums and performs the same full coefficient residual test against the left side of(2). Splitting the sum changes only the outward-rounded grouping of additions. It introduces neither a missing product nor a numerical approximation to a saved ball. Each chunk and the merge retain their source hashes, input hashes and actual elapsed times.
