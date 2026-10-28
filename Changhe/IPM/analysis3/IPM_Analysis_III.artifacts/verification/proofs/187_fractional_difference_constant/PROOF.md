# An exact fractional difference constant for the high residual

## Statement and notation

The Fourier transform on R is unitary. Let sigma=25/4 and

 ||f||H^sigma^2 = integral_R (1+xi^2)^sigma |fhat(xi)|^2 dxi.

Every f in this space has a unique C5 representative. For any two real numbers t,u,

 |f^(5)(t)-f^(5)(u)|^2
 <= [8/(3sqrt(2pi))] |t-u|^(3/2) ||f||H^sigma^2.       (1)

More generally, let t_1,...,t_N be real and let a_1,...,a_N be real numbers with sum a_i=0. Then

 |sum_i a_i f^(5)(t_i)|^2 <= E(a,t) ||f||H^sigma^2,      (2)

 E(a,t) = -[4/(3sqrt(2pi))] sum_(i,j) a_i a_j |t_i-t_j|^(3/2).

The expression E is nonnegative. If the points are distinct and the coefficients are not all zero, it is positive. These inequalities use the explicitly fixed H^sigma norm, with no unspecified embedding constant. The constant in (1) is the exact Fourier integral after replacing the inhomogeneous Bessel weight by its homogeneous upper bound; we do not assert that it is the optimal constant for a fixed nonzero separation in the inhomogeneous norm.

For the exact residual and the fixed high target norm eta_* of topics177,179,182, the scalar summand gives eta_*>=||g_axis||H^sigma. Consequently a directed lower bound for |g_axis^(5)(t)-g_axis^(5)(u)| divided by sqrt(8/(3sqrt(2pi))) |t-u|^(3/4) is a lower bound for eta_*. Numerical acceptance requires the stored certified derivative enclosures and an independent scalar calculation.

## Proof

First consider a Schwartz function. Fourier inversion and Cauchy-Schwarz give the square of the left side of (2) at most ||f||H^sigma^2 times

 (1/(2pi)) integral_R |xi|^10 (1+xi^2)^(-25/4)
                         |sum_i a_i exp(i t_i xi)|^2 dxi.

Since (1+xi^2)^(-25/4)<=|xi|^(-25/2) for xi!=0, this is at most the same norm squared times

 J=(1/(2pi)) integral_R |xi|^(-5/2) |sum_i a_i exp(i t_i xi)|^2 dxi.       (3)

The zero-sum condition makes the numerator O(xi^2) at zero; at infinity it is bounded. Thus (3) converges. Expanding the finite sum and using the zero-sum condition yields

 |sum_i a_i exp(i t_i xi)|^2
 = -sum_(i,j) a_i a_j [1-cos((t_i-t_j)xi)].

All terms on the right are integrable against |xi|^(-5/2). Hence it remains to evaluate

 I=integral_0^infinity (1-cos x) x^(-5/2) dx.

For x>0 use x^(-5/2)=Gamma(5/2)^(-1) integral_0^infinity s^(3/2) exp(-s x) ds. The integrand after multiplication by 1-cos x is nonnegative, so Tonelli's theorem applies without any conditional interchange. The elementary Laplace integral gives

 I=Gamma(5/2)^(-1) integral_0^infinity s^(3/2) [1/s-s/(s^2+1)] ds
  =Gamma(5/2)^(-1) integral_0^infinity s^(1/2)/(1+s^2) ds
  =Gamma(5/2)^(-1) pi/sqrt2
  =(4/3)sqrt(pi/2).

For the third equality, substitute v=s^2 to obtain (1/2)B(3/4,1/4)=pi/sqrt2. Substitution x=|t_i-t_j|xi in (3) now gives

 J=-(I/pi) sum_(i,j) a_i a_j |t_i-t_j|^(3/2)=E(a,t).

Its integral representation proves nonnegativity. If J=0, the continuous finite exponential sum vanishes everywhere away from zero, hence everywhere. Its derivatives at zero of orders0,...,N-1 give the Vandermonde system sum_i a_i t_i^k=0. Distinct points make that matrix invertible, so all a_i=0. Taking N=2 and (a_1,a_2)=(1,-1) proves (1).

Schwartz functions are dense in H^sigma. For j<=5, the Fourier Cauchy-Schwarz estimate has integrable factor |xi|^(2j)(1+xi^2)^(-sigma), since sigma>j+1/2. Thus their derivatives through order5 converge uniformly to the C5 representative. Passing to the limit proves (1) and (2) for every f in H^sigma.

## Scope

Proof 177 proves membership of the actual weighted scalar residual despite its finitely many C5 spline joins. Thus no assumption of C6 regularity is made when points lie on opposite sides of a join. The constant in (1) improves the elementary min(x^2,4) majorant of proof 182 by the exact ratio sqrt(2/sqrt(pi)) in the resulting norm lower bound. Neither this improvement nor a multi-point lower bound supplies an inverse estimate or refutes the nonlinear closure condition(S) by itself.

Dependencies: proof 177 for the precise high norm and actual membership; topics179 and182 for independently reconstructed original-data fifth derivative enclosures. Numerical status is PENDING until the scalar audit is recorded.

## Certified result

Using the independently reconstructed1024-bit derivative enclosures at t=8 and t=1001/125, with their exact rational endpoints, the lower expression from(1) is

 38666592266.2833308090823201281897463999596462323923604778925...

Directed1024-bit evaluation of8/(3sqrt(2pi)) and a separate768-bit Beta/Gamma evaluation of the integral I both prove

 eta_* > 38666592266.

The original NPZ hash and the preceding point-certificate hashes are checked. No rounded decimal midpoint is treated as an exact derivative. The bound remains independent of the angular cutoff and dyadic partition because it uses only the fixed scalar summand. Combined with proof 177, the accepted two-sided statement is38666592266<eta_*<6.321e129. This certifies the size of the residual in that specified high norm and leaves base injectivity and condition(S) open.
