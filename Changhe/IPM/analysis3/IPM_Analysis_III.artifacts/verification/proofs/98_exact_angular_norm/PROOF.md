# Exact angular integration for the strong jet target

## Statement

Let p=x^2 y, t=log r, and let the real parity-compatible function f have the finite angular cofactor

 f(X)=p(X) B(t,theta), B(t,theta)=sum_(m=0)^N b_m(t) cos(2m theta),

with measurable real coefficients. Set

 gamma(t)=B(t,pi/2)=sum_m (-1)^m b_m(t),
 Q(t,theta)=[B(t,theta)-gamma(t)]/cos(theta)^2.

The quotient extends across the vertical axis and is a cosine polynomial of degree at most N-1. Write Q=sum_j q_j cos(2j theta). For N=0 put Q=0. With

 w=|x|^(-17/2) max(1,r)^(29/4),
 omega(t)=e^(-t/2) for t<0, e^(27t/4) for t>=0,
 Y=E G direct-sum L2_P(w dX), E gamma=p gamma(t),
 ||gamma||_G^2=integral omega gamma^2 dt,

the exact norm identity is

 ||f||_Y^2=integral_R omega(t)
       [gamma(t)^2+2 Beta(1/4,3/2) H(q(t))] dt,           (1)

where

 H(q)=sum_(j,l) q_j q_l [m_(j+l)+m_|j-l|]/2,             (2)

and every normalized angular moment m_n is rational. They are specified by

 m_0=1, m_1=-5/7,
 (4n+7)m_(n+1)=-10m_n+(4n-7)m_(n-1), n>=1.              (3)

Both sides of (1) may be infinite; f lies in Y if and only if the right side is finite. Thus (1) is also an exact membership criterion for this finite angular class. No angular quadrature, sampled axis limit, or finite-band truncation error is present. Radial integration and its error bounds remain to be supplied for an actual residual certificate.

The quotient coefficients are explicitly

 q_0=2 sum_(m=1)^N (-1)^(m-1) m b_m,
 q_j=4 sum_(m=j+1)^N (-1)^(m-1-j)(m-j)b_m, j>=1.          (4)

They can be evaluated by two reverse cumulative sums in O(N) operations. Formula (2) is a positive definite Gram form on every finite polynomial space, even though its individual moments and cross terms have signs.

## Proof of the target splitting and radial factors

On each circle, B-gamma vanishes at theta=pi/2 and3pi/2. As a polynomial in z=cos(2theta), it vanishes at z=-1 and is divisible by 1+z=2cos(theta)^2. Hence Q is a polynomial of degree at most N-1. The exact splitting is f=E gamma+f_R with

 f_R=x^2 y cos(theta)^2 Q.

The two summands have trivial intersection in the target decomposition: a nonzero angularly constant cofactor gives the nonintegrable factor |cos(theta)|^(-9/2) sin(theta)^2 in its squared remainder norm. For f_R the extra cos(theta)^4 changes that factor to |cos(theta)|^(-1/2)sin(theta)^2, which is integrable at both axes. All circle integrals below are therefore legitimate.

In polar logarithmic coordinates, p^2 dX=r^8 cos(theta)^4 sin(theta)^2 dt dtheta. Multiplying by w gives radial factor r^(-1/2) for r<1 and r^(27/4) for r>=1. Consequently

 ||f_R||_R^2=integral omega(t) integral_0^(2pi)
                     |cos(theta)|^(-1/2)sin(theta)^2 Q(t,theta)^2 dtheta dt.

By reflection symmetry, the angular integral is four times its first-quadrant part. With u=cos(theta)^2 that part is

 (1/2) integral_0^1 u^(-3/4)(1-u)^(1/2) Q(2u-1)^2 du.

The full angular mass is therefore 2 Beta(1/4,3/2). Normalizing this beta weight to a probability measure, and using cos(2j theta)cos(2l theta)=[cos(2(j+l)theta)+cos(2(j-l)theta)]/2, proves (1)-(2). Tonelli's theorem applied before expanding the finite polynomial allows infinite radial integrals and proves the stated membership equivalence.

## Exact rational moments

In z=2u-1 coordinates the normalized weight is proportional to

 w_J(z)=(1-z)^(1/2)(1+z)^(-3/4), -1<z<1.

Let m_n be the expectation of the Chebyshev polynomial T_n(z). The mean of u under Beta(1/4,3/2) is1/7, so m_1=2/7-1=-5/7. For n>=1 integrate the derivative of (1-z^2)w_J(z)T_n(z). Its endpoint values vanish, since (1-z^2)w_J is of orders3/2 and1/4 at the two endpoints. The identities

 [(1-z^2)w_J]'=(-5/4-(7/4)z)w_J,
 z T_n=(T_(n+1)+T_(n-1))/2,
 (1-z^2)T_n'=n(T_(n-1)-T_(n+1))/2

give precisely (3). Starting with rational initial values, every moment is rational. This proves the recurrence by an independent integral identity rather than by numerical fitting.

## Stable quotient and convolution evaluations

Polynomial division gives the identity, for m>=1,

 2[T_m(z)-(-1)^m]/(1+z)
 =2(-1)^(m-1)m+4 sum_(j=1)^(m-1)(-1)^(m-1-j)(m-j)T_j(z).

It follows either from T_(m+1)=2zT_m-T_(m-1), or by multiplying the right side by1+z and cancelling adjacent terms. This proves (4). For an O(N) evaluation define the alternating tail A_(j+1)=sum_(m>=j+1)(-1)^(m-j-1)b_m and S_j=A_(j+1)-S_(j+1), with zero terminal values. Then q_0=2S_0 and q_j=4S_j for j>=1.

To compute H without an O(N^2) matrix product, form the Laurent polynomial

 L(z)=q_0+sum_(j>=1) q_j(z^j+z^(-j))/2.

If L(z)^2=c_0+sum_(j>=1)c_j(z^j+z^(-j)), then

 H(q)=c_0+2 sum_(j>=1)c_j m_j.                            (5)

An ordinary polynomial product after multiplication of L by a sufficient power of z computes these coefficients. Directed Arb polynomial multiplication and exact rational moments therefore give a rigorous enclosure from coefficient balls. Cancellation can require increased precision; a float result or a negative ball lower endpoint is not a proof of negativity. The integral shows that the exact value is nonnegative.

For a finite sine expansion f/r^3=sum_(j=0)^M h_j sin((2j+1)theta), the preliminary identity

 sin((2j+1)theta)/sin(theta)=1+2 sum_(m=1)^j cos(2m theta)

converts it to a polynomial D. If the exact f has the x^2 factor, D(-1)=0 and B=2D/(1+z). The same quotient operation, applied to D-D(-1), recovers B exactly under that proved divisibility condition. Merely discarding a nonzero interval midpoint at the axis without the exact divisibility proof would be invalid.

## Evidence and limits

The code provides exact recurrence and directed quotient/angular-norm functions. The JSON file contains moments through1044 as exact numerator/denominator pairs, their beta parameters and the recurrence. A separate check compares the first25 moments with exact monomial integration using E[u^k]=(1/4)_k/(7/4)_k, checks the quotient identity for nontrivial rational polynomials, and compares the directed convolution norm with exact rational polynomial integration. Input and code hashes are recorded.

This is an exact angular reduction. It does not enclose the actual radial coefficients, integrate over t, bound the radial tails, or produce the residual eta. Those remain independent obligations. Its purpose is to remove an avoidable angular quadrature and near-axis cancellation issue from that computation.
