# Independent audit of the first omitted radial descendant

## Statement and scope

The candidate is exact C1-N1-007, at
c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The canonical potential coefficients are the already independently
verified JSON in ../taylor_projection/source/canonical007.json.
For this finite generator family, the first sine harmonic of the exact
residual has a nonzero term r^(gamma-8). Its rational coefficient is
recorded in verification/result.json and compared exactly with the
independent N4-195 computation. This statement certifies an omitted
term; it does not bound the complete truncation error or establish a
finite-radius norm estimate.

## Polar reconstruction and an independent coefficient formula

Write t=r^2/(1+r^2), v=1-t and a=delta/2. The previously audited
polar differentiation identities in ../weak_probe_audit/PROOF.md give
branch-zero density in the form

    rho_0(r,theta)=r v^a sum_n R_n(t) sin(n theta),

where each R_n is an exact rational polynomial. These identities are
also stated in ../scaled_polar_weak/PROOF.md. They follow by applying
Euler radial differentiation twice for the Laplacian and once for
minus the y derivative. All two-fold divisions by t are exact, as is
verified before accepting the polynomials. Only potential harmonics
0 and 2 can contribute to density harmonic 1, since a Cartesian first
derivative changes an angular harmonic by one. Accordingly the
checker first selects precisely those two harmonics in branch zero.

Set z=r^-2 for r>1. Since t=(1+z)^-1 and v=z/(1+z), the first harmonic
is exactly

    r^gamma (1+z)^(-a) R_1((1+z)^-1).

If R_1(t)=sum_k b_k t^k, its coefficient at r^(gamma-2q) is

    d_q=sum_k b_k binom(-a-k,q).                         (1)

This is different from N4's direct homogeneous-potential derivative
formula: differentiation and summation have already produced a single
exact density polynomial before its expansion at infinity. For every
real rational beta, the coefficient of z^q in (1+z)^beta is determined
by the differential equation (1+z)f'=beta f and f(0)=1. The recurrence
is B_0=1, B_(q+1)=B_q(beta-q)/(q+1). The analytic expansion converges
for |z|<1; finitely many polynomials are being summed. Thus (1) gives
the actual asymptotic coefficient rather than a formal approximation.

The linear stationary operator c r partial_r-1 multiplies the q-th
term by c(gamma-2q)-1=-2cq. Hence its residual coefficient is

    f_q=-2cq d_q.                                       (2)

The checker compares all seven coefficients q=0,...,6 with N4's exact
rational outputs and requires f_4 to be nonzero.

## No cancellation from another branch or a nonlinear product

Every residual exponent in this finite family is

    1-ell delta-2q',

where 1<=ell<=8 for linear terms and 2<=ell<=16 for quadratic terms,
and q' is a nonnegative integer. Equality with gamma-8 would require

    (ell-1)delta/2=4-q'.

For ell=2,...,16 the left side is not an integer, as verified with
exact rational arithmetic. For ell=1 equality forces q'=4. Therefore
no other branch or quadratic product cancels f_4. Distinct fractional
powers cannot cancel an asymptotic coefficient: along each fixed
angle, divide by the largest surviving power and let r tend to
infinity; repeat over the finite branches and their analytic series.
In particular this proves that a table stopping before q=4 cannot
be the complete exact residual expansion.

## Meaning for the finite Beta pairing model

For a finite homogeneous model F_tr=sum_e s_e r^e sin(theta), the
whole-plane integral against phi_k=r t^k(1+r^2)^-2 sin(theta) is

    int F_tr phi_k = (pi/2) sum_e s_e
          B(k+(e+3)/2,(1-e)/2),                         (3)

provided k+(e+3)/2>0 and (1-e)/2>0 for every term. Polar coordinates,
sine orthogonality, and s=r^2 give (3) directly. It is an identity for
that finite model. The actual smooth residual differs outside r=1 by
an infinite analytic descendant sum and may differ arbitrarily inside
that disk. Bounding the true pairing by (3) requires a quantitative
bound for both differences. The single nonzero omitted coefficient
proved here gives neither a signed pairing error nor its magnitude.
A last retained term alone does not certify the infinite remainder.

## Dependencies and evidence

Dependencies: the canonical007 source audit, the polar derivative
identities and exact rational arithmetic. No unproved existence or
resolvent claim enters. The checker writes hashes of its proof, code,
canonical input, shared polar primitive, and frozen peer evidence.
The result is CONFIRMED only after exact agreement and nonresonance
checks pass. No new full residual cache or optimizer is used.
