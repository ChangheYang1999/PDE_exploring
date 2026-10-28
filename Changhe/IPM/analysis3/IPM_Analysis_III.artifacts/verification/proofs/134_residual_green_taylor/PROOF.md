# Residual interval integration by the Green differential equations

## Statement and scope

This is a rigorous alternative local expansion for the full residual certificate of proof 127. It uses the same exact normalized modal trial, the same target Y, and every angular mode of the residual. It changes neither the data nor the norm. A completed full-norm result still requires exact interval coverage, both tails, outward arithmetic and an independent final audit. No numerical result is asserted by this proof alone.

On each analytic radial piece let H_j(t) be the sine coefficients of rho/r^3. For n=1,...,261 define the scaled Green moments

 I_n^*(t)=exp(2t)I_n(t), J_n^*(t)=exp(2t)J_n(t).

They satisfy the exact equations

 (I_n^*)'=-(2n+2)I_n^*+exp(2t)H_(n-1),
 (J_n^*)'=(2n-2)J_n^*-exp(2t)H_n.                       (1)

The velocity coefficients are

 P_n=n(J_n^*-I_n^*),
 Q_n=n(J_n^*+I_n^*)-exp(2t)(H_n+H_(n-1))/2.             (2)

These equations follow by differentiating the canonical full-plane Green integrals. They do not divide by the difference between an endpoint decay exponent and a Green exponent. This matters because the input inner matching exponent is close, but not equal, to50, one of the Green exponents. A partial-fraction representation remains exact there but can give a very large unnecessary interval Taylor bound.

## Taylor recurrence and its remainder

Let t=m+h z, |z|<=1, h>0. Suppose K'=lambda K+S(t), and let s_0,...,s_N be the exact Taylor coefficients of S(m+h z), with a uniform remainder e_S. Let k_0=K(m), and recursively set

 k_(j+1)=h(lambda k_j+s_j)/(j+1), j=0,...,N.             (3)

For K_N(z)=sum_(j=0)^N k_j z^j, the exact ODE residual is

 h(lambda K_N+S)-partial_z K_N
  =(N+1)k_(N+1)z^N+h R_S(z).

Variation of constants from z=0 to z, including negative z, therefore gives

 |K(m+h z)-K_N(z)|
 <=exp(|lambda|h)(|k_(N+1)|+h e_S).                    (4)

Indeed the integral of (N+1)|s|^N between0 and z is at most1, and the remaining path length is at most1. Formula(4) is valid for real or complex lambda. In the present application lambda is an exact integer.

Interval arithmetic encloses the true center value and every coefficient in(3). The recurrence is an identity for the true coefficients; the interval values need not satisfy the identity for every independent choice inside their balls. Formula(4) is applied to that true polynomial, whose coefficient norms are then bounded by the saved balls. This distinction prevents an artificial interval dependency from being interpreted as a new exact identity.

The source functions exp(2t)H_j are finite exponential polynomials. Their coefficients and remainders are obtained directly from the exponential Taylor formula of proof 127. For spline pieces H_j has exact degree7. For either endpoint branch its finite exponential-polynomial representation is used, without evaluating a nearly singular Green denominator in the remainder calculation.

## Certified center data and velocity error

At the center, the independently checked point formulas of proof 105 enclose H,H',P,Q and P'. Formula(2) gives

 J_n^*(m)=[Q_n(m)+exp(2m)(H_n(m)+H_(n-1)(m))/2+P_n(m)]/(2n),
 I_n^*(m)=[Q_n(m)+exp(2m)(H_n(m)+H_(n-1)(m))/2-P_n(m)]/(2n).

No division by zero occurs, since n>=1. Apply(3)-(4) separately to the two equations(1). If their error bounds are e_I,e_J and the two source errors are e_n,e_(n-1), then valid velocity errors are

 e_P=n(e_I+e_J),
 e_Q=n(e_I+e_J)+(e_n+e_(n-1))/2.

The coefficient of z in P also agrees with h P'(m), independently provided by the original point formula. This comparison is checked before accepting a window. The entire residual center is compared with the complete original point residual as well.

## Full angular norm and radial coverage

Form the nonlinear residual polynomial from the density, density derivative and the P,Q polynomials before interval evaluation. Every angular sine index through522 is retained, including its zero padding. Apply the exact two angular divisions, the exact axis row, and the beta-weight Gram form of topics98 and105 to each radial Taylor coefficient. The omitted residual has the product-error bound of proof 127, using the summed velocity errors above.

If its angular coefficient l1 remainder is e, put E=sqrt(1+M) C_N e, with M=2 Beta(1/4,3/2) and C_N=4(522)^4(1045). If the polynomial coefficients are f_j in the angular target norm N, then throughout the window

 max(0,N(f_0)-sum_(j>=1)N(f_j)-E)
 <=N(F/r^3)<=N(f_0)+sum_(j>=1)N(f_j)+E.

The exact positive integral of g(t), with g=exp(-t/2) on the left and exp(27t/4) on the right, multiplies the squared bounds. Every window lies in one analytic branch or one closed spline span and does not cross0. Adaptive subdivision affects efficiency only. A complete certificate is the rational sum over a gap-free, overlap-free partition, plus the proof 127 inner tail and proof 122 outer tail.

Previously accepted windows from proof 127 may be reused because their enclosures concern the identical exact trial and norm. Such reuse must retain their original records and dates and record the old code, old proof and journal hashes. No prior row is relabeled as having been recomputed by the new recurrence.

## Limitations

This proof establishes validity of the local algorithm. It does not certify a full norm before the computation and final audit finish, does not control a finite-section complement, and supplies no inverse or nonlinear closure constant. The close inner exponent is a representation issue in the old remainder estimate, not an instability or a change in the exact profile.
