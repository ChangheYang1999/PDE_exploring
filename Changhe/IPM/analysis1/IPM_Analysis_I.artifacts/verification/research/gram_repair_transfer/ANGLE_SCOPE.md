# The angular derivative is included uniformly in the repair bound

This note states the argument before the supplemental angular arithmetic.
The last review requested a direct link to topic132's angular bound.
That topic's PROOF.md already includes the angular derivative. The
radial-only interpretation is not used.

For t=log r and Phi_m(theta)=cos^2(theta)sin(theta)cos(2m theta), set
A0=integral_0^{2pi} Phi_m^2>0 and
A1=integral_0^{2pi} (Phi_m')^2>=0. The full broken energy is

    L^6 integral W(t)[(A0+A1)B^2+A0(3B+B')^2]dt.

This includes all angular differentiation of x^2y and cos(2m theta).
For the affine repair difference d, topic132 bounds the numerator by
L^6(A0+A1)U, using A0<=A0+A1, and the original denominator from below
by L^6(A0+A1)V. The entire factor A0+A1 cancels. Thus sqrt(U/V) bounds
the relative error for every individual mode m, even though the actual
relative error may depend on m. The bound is neither radial-only nor an
angular orthogonality assumption. All modes0 through23 are covered by
the same argument, and the same is true for every integer m>=0.

A separate exact audit will check these angular integrals in two ways.
First,

    Phi_m=(sin((1+2m)theta)+sin((1-2m)theta)
          +sin((3+2m)theta)+sin((3-2m)theta))/8.

After combining signed frequencies, sine orthogonality gives A0/pi as
the sum of squared coefficients and A1/pi as the frequency-squared sum.
For the independent check, construct T_{2m}(q) by the Chebyshev recurrence,
set B(q)=q^2 T_{2m}(q), and differentiate sin(theta)B(cos(theta)):

    Phi_m'=q B(q)-(1-q^2)B'(q).

Expand both squares and use

    integral_0^{2pi} cos^{2p}(theta)sin^{2q}(theta)dtheta / pi
      =2(2p)!(2q)!/[4^(p+q)p!q!(p+q)!].

The moment formula follows by the beta integral or repeated integration
by parts. It is used with q=1 for A0 and q=0 for A1. Exact rational
agreement, positivity of A0 and A1, and A0<=A0+A1 will be checked for
all24 actual mode indices. This supports the explicit application binding;
the uniform inequality itself follows from the preceding polar argument.
The frozen topic132 proof and current final pins must be checked directly.
