# Exact angular input quotients and a finite division error bound

## Statement and notation

Let m be a positive integer, p(theta)=cos(theta)^2 sin(theta), and define the angular remainder input

 G_m(theta)=p(theta)(cos(2m theta)-(-1)^m).

Then its quotient by cos(theta)^4 extends to the entire circle as the odd sine polynomial

 Q_m(theta)=2 sum_{j=0}^{m-1} (-1)^(m-1-j)(2m-2j-1) sin((2j+1)theta).                 (1)

Every coefficient is an integer. Formula(1) is independent of zero padding, has coefficient l1 norm2m^2 and squared coefficient l2 norm4m(4m^2-1)/3. Thus these input templates can be represented exactly in binary floating arithmetic whenever their integer coefficients are representable. This does not make the operator images, angular Gram entries or radial quadrature exact.

For an arbitrary sine polynomial G with n coefficients, n>=3, which is divisible by cos(theta)^4 with a quotient Q having n-2 coefficients, exact coefficient recovery is

 Q_j=16 sum_{k=0}^{n-3-j} (-1)^k binom(k+3,3) G_{j+2+k},   0<=j<=n-3.             (2)

In particular, if Qhat has n-2 coefficients and R=G-cos(theta)^4 Qhat, then

 ||Q-Qhat||_(coefficient infinity) <=16 binom(n+1,4)||R||_(coefficient infinity),
 ||Q-Qhat||_(coefficient l1) <=16 binom(n+2,5)||R||_(coefficient infinity).          (3)

These are bounds for exact coefficient data. A floating residual needs its own rounding enclosure before(3) gives a certificate.

## Proof of the input formula

Multiplication of sin((2j+1)theta) by cos(theta)^2 equals one half of that sine plus one quarter of its two neighboring odd sines. At j=0, the lower neighbor is sin(-theta)=-sin(theta). Insert the coefficients in(1). The alternating affine coefficient sequence has zero interior second difference after this multiplication. The top two surviving terms are

 (1/2)sin((2m+1)theta)-(1/2)sin((2m-1)theta),

and the first coefficient has the additional term -(-1)^m sin(theta). For m=1 the coincident first and top indices give the same identity directly. Consequently

 cos(theta)^2 Q_m(theta)=sin(theta)(cos(2m theta)-(-1)^m).

Multiplying by cos(theta)^2 proves G_m=cos(theta)^4 Q_m. The l1 norm is twice the sum of the first m odd positive integers, namely2m^2. The sum of their squares is m(4m^2-1)/3, proving the l2 formula. Equality as trigonometric polynomials includes the axes by continuity; there is no singular numerical division.

The first three templates are

 Q_1=2sin(theta),
 Q_2=-6sin(theta)+2sin(3theta)=-8sin(theta)^3,
 Q_3=10sin(theta)-6sin(3theta)+2sin(5theta)
    =2sin(theta)-16sin(theta)^3+32sin(theta)^5.

## Proof of the coefficient inverse

Use cos(theta)^4=(3+4cos(2theta)+cos(4theta))/8. Read the coefficient of sin((2j+5)theta), starting at the highest frequency and extending the quotient coefficients by zero above n-3. Since this frequency index is at least2, no reflected negative frequency appears. The resulting triangular system is

 16G_{j+2}=Q_j+4Q_{j+1}+6Q_{j+2}+4Q_{j+3}+Q_{j+4}.

The inverse formal power series of (1+z)^4 has coefficients (-1)^k binom(k+3,3). The finite triangular system therefore gives(2). The hypothesis that G is in the multiplication range ensures that its remaining lowest two coefficients are also matched. Conversely they must be checked when divisibility has not been established.

Apply(2) to R=cos(theta)^4(Q-Qhat). The hockey-stick identities give

 sum_{k=0}^{n-3-j} binom(k+3,3)=binom(n+1-j,4),
 sum_{j=0}^{n-3} binom(n+1-j,4)=binom(n+2,5),

which prove(3). These powers of n explain why a small multiplication residual alone gives a much weaker forward error estimate at high padding.

## Weighted angular norms

For the remainder weight used in S1, the quotient norm uses |cos(theta)|^(-1/2)dtheta. Put

 I_p=integral_0^(2pi) sin(theta)^(2p)|cos(theta)|^(-1/2)dtheta
    =2 Beta(p+1/2,1/4).

The substitution u=sin(theta)^2 in each quadrant proves the identity. It also gives I_(p+1)/I_p=(p+1/2)/(p+3/4). Therefore every Gram entry between Q_1,Q_2,Q_3 is an exact rational multiple of I_0. For example, the two-mode Gram has entries4I_1,-16I_2,64I_3. General sine-polynomial inner products can be obtained from the same moments after writing the odd sines as sin(theta) times a polynomial in sin(theta)^2. Only the common Beta factor then needs interval evaluation.

For any coefficient error e, its weighted angular norm is at most sqrt(I_0)||e||_(coefficient l1), by the triangle inequality and |sin|<=1. Combining this with(3) gives a valid, possibly large forward error bound. It is not a replacement for the smaller rigorous error bounds needed for a practical section certificate.

## Scope and verification

The algebra above applies to arbitrary finite sine polynomials and does not depend on the IPM trial. Proof 183 supplies the concrete padding-dependent input errors that motivate its use. The accompanying rational script checks(1), both coefficient norm identities, the triangular inverse, the first three exact Gram ratios and the error constants for the current padding. It uses no pseudoinverse and no numerical quadrature. No finite or infinite-dimensional inverse for the IPM linearization follows.
