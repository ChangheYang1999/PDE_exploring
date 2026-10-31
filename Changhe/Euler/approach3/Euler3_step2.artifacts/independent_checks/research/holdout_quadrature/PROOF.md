# Positive-volume holdout quadrature and residual comparison

Status: exact changes of variables and finite-sample identities proved below.
They do not bound quadrature error and do not establish an Euler solution.

## Statement, hypotheses and notation

Let 0 <= a < b < infinity, let S(a,b) = {y in R^3: a < |y| < b},
and let f be an integrable scalar function on S(a,b). Write dS for area measure
on the unit sphere. Normalized volume integration is

    mean_S f = 1/(4 pi) int_(S^2) int_0^1
               f((a^3 + (b^3-a^3)t)^(1/3) n) dt dS(n).

The same formula with f(y0 + r n) gives the normalized integral on a ball
centered at y0 when a=0. Let t_i in (0,1), w_i>0 have sum w_i=1, and let unit
vectors n_j and weights v_j>0 have sum v_j=1. The finite quadrature defines

    <f,g>_Q = sum_(i,j) w_i v_j f(y_ij) dot g(y_ij),
    ||f||_Q = sqrt(<f,f>_Q).

It is a norm on arrays of sampled values. If R=L+N, then

    ||R||_Q^2 = ||L||_Q^2 + ||N||_Q^2 + 2 <L,N>_Q.

For approximate residuals R0 and R1 on the identical points and weights,

    abs(||R1||_Q - ||R0||_Q) <= ||R1-R0||_Q.

If they differ only in the pressure gradient, R1-R0 = gradP1-gradP0. In
particular, the pressure refinement difference bounds the difference between
the two computed residual norms. It does not bound either norm's error against
the exact pressure without a separate pressure error estimate.

## Proof

Spherical coordinates give dy = r^2 dr dS. With
r(t) = (a^3+(b^3-a^3)t)^(1/3), one has
r^2 dr = (b^3-a^3) dt/3. The volume is 4 pi(b^3-a^3)/3, which proves the
normalized formula. A translation has Jacobian one, so the centered-ball
formula follows. Strictly positive weights identify the sampled arrays with a
Euclidean space after multiplying each array component by sqrt(w_i v_j).
The inner product, norm, expansion of a squared norm, and triangle inequality
are therefore the corresponding Euclidean statements. Applying the triangle
inequality to R1=(R1-R0)+R0 and then reversing their roles proves the last
inequality. If all nonpressure terms agree, subtraction leaves precisely the
pressure-gradient difference.

## Numerical conventions and scope

The implementation uses Gauss-Legendre nodes in the normalized volume
coordinate t and a Gauss-Legendre / equally spaced azimuthal sphere rule. The
azimuthal phase and all node counts are recorded. The radial rule is generally
not a polynomial-exact rule in r; no such claim is made. Separate refinements
of the holdout rule and the pressure source rule are needed.

The physical momentum terms are T1=(1-c)U, T2=c DU y,
T3=omega(JU-DU Jy), T4=DU U, and T5=gradP. Their individual norms determine
the registered denominators. The numerator is evaluated as L+T4+T5, with
L=T1+T2+T3 obtained from the exact stable potential identity in
`../stable_linear_operator/PROOF.md`. This avoids subtracting the leading
far-field terms in floating point. It does not change their exact sum.

The single-term ratio is ||R||_Q/||(1-c)U||_Q. No epsilon is added to a
denominator. Zero and undersized denominators are flagged as unresolved.
The standard and half-offset shell families are reported separately. A
positive-volume core ball has geometric-reference radius zero in the
registered rescaled denominator flags. A near-zero residual, a refinement
difference, and a finite-sample identity are numerical evidence only.

## Dependencies

Spherical-coordinate change of variables, finite-dimensional inner-product
algebra, and the stable linear operator identity. Pressure existence and its
full-space Green representation require the hypotheses of
`../pressure_consistency/PROOF.md`. No formal proof source or build is supplied.
