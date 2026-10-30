# Complete Laplacian tail and dyadic forcing lower bound

## Statement and exact source

Let c=4076476460239181/2251799813685248, delta=1-1/c and b=1-2delta. Let rho and U be the exact state131 density and canonical velocity from the finite rational potential recorded in ../baseline/data/state131_independent.json. Set F=(cX+U).D rho-rho. The source identity and smoothness are established in the baseline and radial_fourier topics. Write t=r²/(1+r²), v=1-t. The complete residual, with no angular truncation, is

    F=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),

where n is positive odd and each polynomial is rational. Every derivative and product here is the exact finite operation of ../radial_fourier/PROOF.md and ../whole_plane_norms/PROOF.md.

The checker shall compute the full Cartesian Laplacian and form its exact finite expansion

    r^(2-b) Delta F=t^delta sum_e v^e C_e(theta).             (1)

All equal exponents and angular modes are combined before any norm is taken. Assume the resulting exponents are nonnegative and C_0 is nonzero. Put E_e=sum_n C_(e,n)² and D=sqrt(pi E_0). For J>=1 define v_J=1/(1+2^(2J)), t_J=1-v_J and

    R_J=1-t_J^delta+sum_(e>0) v_J^e sqrt(E_e/E_0).          (2)

If an outward interval calculation gives R_J<=epsilon<1, then, for every r>=2^J,

    ||Delta F(r,.)||_(L²(S¹)) >= (1-epsilon)D r^(b-2).      (3)

This statement uses the full finite expansion. It does not infer a finite-radius estimate from leading asymptotics alone.

## Independent Cartesian construction

For a term r^p v^d P(t) exp(i n theta), logarithmic radial differentiation replaces P by (p-2dt)P+2t(1-t)P'. Cartesian differentiation uses partial_x=cos(theta)partial_r-sin(theta)partial_theta/r and partial_y=sin(theta)partial_r+cos(theta)partial_theta/r. Exact product-to-sum rules therefore construct partial_xx F and partial_yy F separately. In the normalized representation of whole_plane_norms their sum is

    Delta F=r sum_(ell,n) v^(1+ell delta/2) L_(ell,n)(t) sin(n theta).

Multiplying by r^(2-b) and using r²=t/v yields (1): expand the rational polynomial t L_(ell,n)(t) at t=1-v, and assign its coefficient of v^k to exponent e=ell delta/2-delta+k. This construction does not use the peer's polar Laplacian arrays. As an algebraic cross-check, the resulting tL equals

    [T_(d,1)²-n²] P,  T_(d,1)P=(1-2dt)P+2t(1-t)P'.

The mixed Cartesian derivatives are checked to commute. This gives two symbolic routes to the same complete Laplacian.

## Tail estimate

For r>=2^J one has 0<v<=v_J and t_J<=t<1. Subtract C_0 from (1). The leading error has norm (1-t^delta)D, at most (1-t_J^delta)D. Every other term has norm at most v_J^e sqrt(pi E_e), since e>0 and t^delta<=1. The triangle inequality and the full-circle sine orthogonality identity give an error no greater than R_J D. The reverse triangle inequality proves (3). Every square E_e is computed with exact rational coefficients, including cancellation before squaring.

## Lower bound in the specified dyadic space

Assume Y is the dyadic norm defined in the frozen T4_Y_PROOF.md and that its audited cutoff plateaus give

    Y(F)² >= sum_(j>=J) 2^(2(2-a)j)
                   ||Delta F||²_(L²(2^j<r<2^(j+1))).

This assumption specifies the norm and normalization; it is not a general statement about arbitrary weighted spaces. If a>1+b and b<1, set eta=a-1-b and K=(1-2^(2b-2))/(2-2b)>0. Integrating (3) in polar measure r dr dtheta gives the jth shell lower bound (1-epsilon)²D² K 2^((2b-2)j). The displayed dyadic factor changes this to (1-epsilon)²D² K 2^(-2eta j). Summing the convergent geometric series proves

    Y(F) >= (1-epsilon)D sqrt(K)
                  2^(-eta J)/sqrt(1-2^(-2eta)).             (4)

The low-weight regularization radius does not occur in this bound.

## Complete scalar interval cover

Suppose a proposed closure would require

    Y(F)<sqrt(8pi)(1+c-ca)²/(1+a)                          (5)

throughout the possible window 2/c<a<1+1/c. This is a conditional implication until the inverse and radius-ceiling hypotheses establishing (5) have received the required analytic reviews. This audit does not replace those reviews.

Set a=2/c+delta x with 0<x<1. Then eta=delta x and 1+c-ca=(c-1)(1-x). Taking epsilon=1/2, squaring positive quantities in (4),(5), and cancelling pi proves that the forcing lower bound exceeds (5) exactly when

    (E_0 K/4)(1+2/c+delta x)²
      > 8(c-1)^4(1-x)^4(1-2^(-2delta x))2^(2J delta x).    (6)

On a rational cell [l,h] within [0,1], the left member is bounded below by its value at l. The right member is bounded above by evaluating the decreasing factor (1-x)^4 at l and each increasing factor at h. Each factor is nonnegative. A strictly positive outward lower bound for the difference of these two endpoint expressions proves (6) on the entire cell. A consecutive exact rational partition covers the closed interval, and hence the open membership window. This argument is an interval cover, not a point scan.

## Verification and scope

The implementation reconstructs rho,U,F from this lane's independently checked potential. It compares all exact E_e with the peer result, recomputes all eleven radius tests, and independently checks every cell in the scalar cover. It records source, code and proof hashes. The finite numerical claims are OPEN until this execution passes. The conditional scheme exclusion additionally depends on the independently reviewed dyadic plateau estimate, the radius ceiling, the genuine high-inverse lower bound and its finite-angular decay hypotheses. It does not rule out the intended profile or any different existence scheme.
