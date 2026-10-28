# The leading far residual of the actual modal trial

## Exact expansion and quantity to be checked

Let rho be the normalized, exactly C6-joined modal trial reconstructed from the original file identified in proof 50. Write k=1615536043799051/9007199254740992, ell=1/k, t=log r, tau=t-t_+, R_+=exp(t_+), alpha_0=k-3 and alpha_1=2k-4. Use the sine coefficients A_{j,l} of the density cofactor:

 rho/r^3=sum_{j=0}^{261} H_j(tau) sin((2j+1)theta),
 H_j=A_{j,0}exp(alpha_0 tau)+A_{j,1}exp(alpha_1 tau)
                         +O(exp((3k-5)tau)).              (1)

The coefficients in (1) are the exact defining data after angular conversion and normalization, not fitted asymptotic values. The remaining original exponents and the exact matching correction have strictly faster decay than alpha_1. Derivatives of every fixed cylinder order satisfy the same expansion.

Let A_j=A_{j,0}, B_j=A_{j,1}. Set missing indices to zero and, for 1<=n<=261, define

 p_n=n R_+^2[A_n/(2n-4-alpha_0)-A_{n-1}/(alpha_0+2n+4)],
 q_n=R_+^2{n[A_n/(2n-4-alpha_0)+A_{n-1}/(alpha_0+2n+4)]
                                      -(A_n+A_{n-1})/2}.  (2)

All denominators are nonzero because 0<k<1. Put

 A(theta)=sum_j A_j sin((2j+1)theta),
 B(theta)=sum_j B_j sin((2j+1)theta),
 P(theta)=sum_n p_n cos(2n theta),
 Q(theta)=sum_n q_n sin(2n theta),
 S(theta)=(1-ell)B(theta)-k P(theta)A(theta)+Q(theta)A'(theta). (3)

Then the exact stationary residual F=(ell X+U[rho]).grad rho-rho satisfies

 F/r^3=exp(alpha_1 tau) S(theta)+O(exp((3k-5)tau)).          (4)

In particular the leading physical degree is 2k-1 if S is nonzero. The all-mode directed calculation below is the remaining numerical nonvanishing check; an observed fitted slope alone would not establish it.

## Proof of the expansion

The full-plane modal Green formula has velocity coefficients

 U_r/r=-sum_n P_n(tau)cos(2n theta),
 U_theta/r=sum_n Q_n(tau)sin(2n theta).

In the notation of proof 68, its two scalar integrals for mode n have leading coefficients A_{n-1}/(alpha_0+2n+4) and A_n/(2n-4-alpha_0). Their exact combination gives (2). The exterior homogeneous part of the canonical Green solution decays at least as exp(-4tau) in U/r. The next density term supplies a velocity term with exponent 2k-2, and all other terms are faster. Thus

 P_n=p_n exp((k-1)tau)+O(exp((2k-2)tau)),
 Q_n=q_n exp((k-1)tau)+O(exp((2k-2)tau)).

No growing exterior harmonic term is allowed in the canonical inverse.

The pure dilation residual on a cofactor exp(alpha tau) is [ell(3+alpha)-1] times that cofactor. It vanishes exactly at alpha_0, and its value at alpha_1 is 1-ell. The leading radial derivative of rho is k r^3 exp(alpha_0 tau)A(theta); the leading angular derivative is r^3 exp(alpha_0 tau)A'(theta). Combining these with the leading velocity gives (3)-(4). The next possible exponent is alpha_0+(2k-2)=3k-5, or equivalently alpha_1+(k-1). Every finite polynomial in tau from the matching correction is absorbed by its strict faster exponential decay. The finite angular expansion permits termwise differentiation at every fixed order.

## Exact strong-target rate

The factorization of the actual density and the velocity parities give

 S(theta)=cos(theta)^2 sin(theta) B_S(theta).

Here B_S is an even finite cosine polynomial. Define

 gamma_S=B_S(pi/2),
 Q_S(theta)=[B_S(theta)-gamma_S]/cos(theta)^2.

The quotient is again an exact finite cosine polynomial. The angular remainder norm of proof 98 is

 E_S=M H(Q_S),
 M=2 Beta(1/4,3/2),
 H(Q_S)=M^(-1)int_0^(2pi)|cos(theta)|^(-1/2)sin(theta)^2 Q_S(theta)^2 dtheta.

For the fixed strong target, the axis and remainder energy densities therefore obey

 e_axis(t)=exp(-2alpha_1 t_+) gamma_S^2 exp((4k-5/4)t)
                                      +O(exp((5k-9/4)t)),
 e_rem(t)=exp(-2alpha_1 t_+) E_S exp((4k-5/4)t)
                                      +O(exp((5k-9/4)t)). (5)

The displayed error exponents follow from the cross term between alpha_1 and 3k-5. If E_S>0, the logarithmic decay rate of the remainder density tends to the exact rational number 4k-5/4. Since this number is negative, the asymptotic tail is integrable. Equation (5) is an asymptotic statement, not by itself a finite-radius certified tail upper bound.

## Numerical verification protocol

The script reads the original NPZ through the independently checked exact-join construction. At 512 bits it computes (2)-(3) using every density and velocity mode, divides by the angular factors exactly in coefficient arithmetic, and computes E_S with the rational moment recurrence of proof 98. It also checks the coefficients in (2) against the original-data Green exponential-polynomial representation, and recomputes the complete residual at t=33/4. All output intervals, input hashes and comparison results are retained in evidence. The completed result is recorded in VERIFICATION_RECORD.md.
