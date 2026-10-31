# Exact modal pressure Laplacians and centered radial differences

Status: proved identities for manufactured functions. No campaign state or pressure error bound is certified here. This argument was written before the accompanying numerical code test.

## Statement and notation

Let l be a nonnegative integer, let a>0, and let Y be a real smooth spherical harmonic on S² satisfying Delta_S² Y=-l(l+1)Y. Put r=|y|, s=r/a and t=s². Let h be twice continuously differentiable on (0,infinity). For y≠0 define P(y)=s^l h(t)Y(y/r). Then

Delta P(y)=a^-2 s^l [(4l+6)h'(t)+4t h''(t)]Y(y/r).

In particular the following smooth functions extend across the origin because r^l Y is a homogeneous harmonic polynomial and the other factors are smooth functions of r²:

1. For P_G(y)=r^l exp(-r²/a²)Y(y/r),
   Delta P_G=[4r²/a^4-(4l+6)/a²]r^l exp(-r²/a²)Y.
2. For q>0 and P_R(y)=s^l(1+t)^(-q)Y(y/r),
   Delta P_R=2q a^-2 s^l (1+t)^(-q-2)[(2q-2l-1)t-(2l+3)]Y.
   Its radial coefficient derivative is
   a^-1 s^(l-1)(1+t)^(-q-1)[l+(l-2q)t].
   The formula is used for r>0, including l=0, with its smooth limit at zero.
   Taking q=(l+4)/2 gives P_R=O(r^-4) at infinity for fixed a,l,Y.

For a scalar radial coefficient p∈C⁴([r-d,r+d]), where r>d>0, define

L_l p=p''(r)+2p'(r)/r-l(l+1)p(r)/r²,

L_l,d p=[p'(r+d)-p'(r-d)]/(2d)+2p'(r)/r-l(l+1)p(r)/r².

In exact arithmetic,

|L_l,d p-L_l p| ≤ d²/6 sup_{u∈[r-d,r+d]} |p''''(u)|.

If Y_1,...,Y_M are real orthonormal spherical harmonics for surface area measure dS, then for real coefficients v_j,

(1/(4pi)) integral_S² |sum_j v_j Y_j|² dS=(1/(4pi)) sum_j v_j².

Consequently, for radial quadrature weights w_i>0, the shell RMS of any finite modal field on an angular rule exact for all products Y_jY_k can be evaluated from its modal coefficients as

RMS² = sum_i w_i sum_j v_ij² / (4pi sum_i w_i).

This applies to the numerical error coefficients and the exact Laplacian coefficients separately. It does not require division by a pointwise exact Laplacian, which may vanish.

## Proof

In spherical coordinates Delta(p(r)Y)=[p''+2p'/r-l(l+1)p/r²]Y. Differentiate p(r)=s^l h(s²) twice. The term multiplying h is [l(l-1)+2l-l(l+1)]s^(l-2)/a²=0. The terms multiplying h' are (4l+2+4)s^l/a², and the h'' term is 4s^(l+2)/a². This proves the general identity.

For the Gaussian use h(t)=exp(-t), h'=-h and h''=h, and multiply the result by a^l to obtain the r^l convention. For the rational function, h'=-q(1+t)^(-q-1) and h''=q(q+1)(1+t)^(-q-2). Factoring 2q(1+t)^(-q-2) gives the stated expression. Direct first differentiation gives the radial derivative. Since s^l(1+s²)^(-q)=O(s^(l-2q)), the stated q gives exponent -4. Smoothness at the origin follows from the harmonic polynomial representation and the smoothness of exp(-r²/a²) and (1+r²/a²)^(-q).

For the difference bound, apply the order-two Taylor formula with integral remainder to f=p' at r+d and r-d. The even f'' terms cancel upon subtraction. The two remainder magnitudes total at most 2(d³/6) sup|f'''|. Division by 2d yields d² sup|p''''|/6. The two algebraic radial-operator terms are identical in L_l,d and L_l, hence contribute no error in exact arithmetic.

Finally expand the square of the modal sum and apply integral Y_jY_k dS=delta_jk. If an angular quadrature integrates these products exactly, the same expansion proves its discrete equality. Weight and sum the radial values and divide by the total radial weight to obtain the shell formula.

## Dependencies and scope

The proof uses the spherical-coordinate Laplacian, the harmonic polynomial representation, Taylor's theorem and orthonormality. The related quadrature conventions are in ../holdout_quadrature/PROOF.md and finite angular-product degree bounds in ../angular_residual_norms/PROOF.md. Realized floating-point table accuracy is a separate empirical check.

A large relative error in a manufactured outer shell can arise even when its absolute field is tiny. Omitting an underflowed shell leaves that shell untested. Agreement between two radial step sizes does not provide the derivative supremum in the displayed bound and does not bound pressure-solver truncation, interpolation or roundoff. A code test on these manufactured functions tests a formula; it does not make its observed error a uniform error bound for unrelated campaign pressures.

## Rescaling a manufactured mode and computing its discrete norm

Fix one shell with positive quadrature weights and at least one node, a positive scale a and a degree l. Let p(r)=r^l exp(-r²/a²), and let p_tilde(r)=(r/a)^l exp(-r²/a²). Both radial Laplacian operators defined above are linear, and p=a^l p_tilde. Consequently the discrete relative error ||L_l,d p-L_l p||/||L_l p|| equals the corresponding error for p_tilde whenever the denominator is nonzero. The constant a^l cancels exactly. This is an exact-arithmetic statement, not an assertion that the two floating-point programs agree.

For any nonzero finite real vector x and positive weights w_i, set M=max_i |x_i|. Its weighted RMS is M sqrt(sum_i w_i (x_i/M)² / sum_i w_i). This identity follows by factoring M² from the sum of squares. It avoids squaring the largest unscaled values. It cannot rescue a vector whose entries already overflowed or underflowed when formed.

A shell [0,b] with b>0 has geometric endpoint center sqrt(0*b)=0, which is not an admissible a in the Gaussian definition. A positive convention must be stated for that shell. The production HoldoutGrid uses sqrt(max(0,b/64)*b)=b/8; this is a convention, not the geometric mean of the two actual endpoints. For positive dyadic shells [b,2b], the ordinary geometric center is sqrt(2)*b. The code test at different shells may use different positive constants a, but any resulting observation must identify that choice.
