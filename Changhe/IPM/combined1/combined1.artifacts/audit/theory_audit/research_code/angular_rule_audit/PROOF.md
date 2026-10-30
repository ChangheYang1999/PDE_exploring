# Independent audit of angular bandwidth and midpoint integration

## Exact statement

Let chi(r,theta) be a finite real potential with angular modes cos(2m theta), 0<=m<=M, and smooth radial coefficients for r>0. Define rho=-partial_y Delta chi, psi=partial_x partial_y chi, U=(-psi_y,psi_x), and F=(cr partial_r-1)rho+U.grad rho. For every fixed r>0, F belongs to the span of sin((2k+1)theta), 0<=k<=2M+1. The quotient R=F/(r sin theta), extended continuously on the quadrant endpoints, belongs to the span of cos(2k theta), 0<=k<=2M+1.

For N>=2M+2, the N equally spaced quadrant midpoint nodes theta_i=(i+1/2)pi/(2N), with weights pi/(2N), integrate F² and R² exactly. This is an exact-arithmetic statement at a fixed radius. It asserts neither radial integration accuracy nor finite-precision accuracy.

For any real positive quadrature rule the Gram-matrix eigenvalues in the respective orthonormal bases give lower and upper bounds for the ratio of its squared norm to the true angular squared norm. A floating eigenvalue is a diagnostic. A rigorously enclosed positive sum evaluated on a specified rational coefficient vector and specified rational nodes and weights is a certified witness for that particular rule.

## Proof of the bandwidth

The polar Laplacian acts separately on each angular mode. A single Cartesian derivative changes a mode number by at most one, because partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r. Thus rho has odd sine modes at most2M+1 and psi has even sine modes at most2M+2. These parities also follow from chi being even in both Cartesian variables.

The polar Jacobian identity is U.grad rho=(psi_r rho_theta-psi_theta rho_r)/r. Each product has frequencies at most(2M+2)+(2M+1)=4M+3. S1 parity removes all except odd sine modes. The linear radial term has the same parity and lower maximum frequency. Therefore F has the asserted expansion.

For every k>=0, sin((2k+1)theta)/sin(theta)=1+2 sum_(j=1)^k cos(2j theta). This follows by summing exp(2ijtheta) for -k<=j<=k and multiplying by sin(theta), with continuity at its zeros. Dividing the expansion of F by r sin(theta) proves the quotient statement.

## Exact discrete orthogonality

The quadrant integrals of cos(2l theta) vanish for every positive integer l. At the midpoint nodes,

sum_(i=0)^(N-1) cos(l pi(i+1/2)/N)=0

unless l is a multiple of2N. To verify it when exp(i l pi/N)!=1, sum the geometric progression; its real part is sin(l pi)/(2 sin(l pi/(2N)))=0. At multiples of2N the sum is N(-1)^(l/(2N)). The l=0 sum is N.

Products of the sine basis functions are half the difference of cos((n-m)theta) and cos((n+m)theta). Their largest cosine index in the notation cos(2ltheta) is l=4M+3. Products of quotient basis functions have maximum l=4M+2. Since2N>=4M+4, neither product has a positive index divisible by2N. Every nonconstant product term therefore has both exact integral and quadrature equal to zero. Constant terms have quadrature equal to interval length. This proves exactness for all products and hence for both squares.

The orthonormal density basis is sqrt(4/pi)sin((2k+1)theta). The quotient basis has constant sqrt(2/pi) and positive modes sqrt(4/pi)cos(2k theta). Thus both spaces have dimension2M+2. Fewer than2M+2 arbitrary nodes cannot define a positive definite squared norm on either complete space: evaluation from a larger-dimensional vector space into R^N has a nonzero kernel. This dimension observation concerns the whole allowed harmonic space, not the smaller set of residuals realized by a particular nonlinear ansatz.

## Arbitrary rules and certified counterexamples

For an orthonormal basis b and a coefficient vector v, exact integration gives ||v||². The quadrature gives v^T Gv, where G=sum_i w_i b(theta_i)b(theta_i)^T. The spectral theorem gives the eigenvalue comparison. Positivity of w_i makes G positive semidefinite. Polynomial exactness of a Gauss-Legendre rule in theta gives no trigonometric exactness theorem because the sine and cosine functions here are not algebraic polynomials in theta.

If a vector of sine coefficients v has exact rational entries, its true squared integral is (pi/4)sum v_k². Freeze the nodes and weights as exact rational inputs as well. A ball enclosure of sum_i w_i (sum_k v_k sin((2k+1)theta_i))², divided by the exact-integral enclosure, can rigorously prove a failure for this specified rule. It need not prove anything about the exact mathematical Gauss nodes, every implementation of a named quadrature routine, or realizability by an IPM residual. Those are separate claims.

Extra angular weights require a fresh product-bandwidth count. The result does not automatically cover a loss multiplied by a nonconstant angular weight.

## Audit conclusion and dependencies

This independently confirms the analytic claims in source/N4_PROOF.md and the angular-resolution subsection of source/N4_radial_PROOF.md. The latter's composite trapezoid criterion N>2M+1 for the quotient follows from the analogous endpoint-weighted cosine sum; its maximum index is4M+2<2N. No numerical Gram eigenvalue or candidate loss is certified by this proof alone. The dependencies are only the displayed polar derivative, trigonometric product and finite geometric-sum identities.
