# Newton pressure decay after the first two moment cancellations

## Statement and notation

Let q be a real number with 4<q<5, and let C>=0. Let f:R^3->R be measurable with

    |f(y)| <= C (1+|y|)^(-q)

for almost every y. Suppose its absolutely convergent zeroth and first moments vanish:

    integral f(y) dy = 0,    integral y_i f(y) dy = 0  (i=1,2,3).

Define the full-space Newton potential

    P(x) = (1/(4pi)) integral f(y)/|x-y| dy.

This integral is absolutely convergent at every x. For every |x|=r>=2,

    |P(x)| <= C B_q r^(2-q),

where the explicit constant is

    B_q = 2^(q-2)/(5-q) + 2^(q-3)
          + 3*2^(q-3)/(q-3) + 2^(q-4)/(q-4).

The estimate uses no second source moment. Such a moment need not be absolutely convergent when q<5. It does not permit one to set nonzero discrete moments to zero without quantifying the numerical change.

## Proof

The bound on f implies local boundedness almost everywhere, so the integrable singularity |x-y|^(-1) causes no problem. For |y|>2|x|+1 the kernel is at most 2/|y| and the tail is integrable. Thus P is defined by an absolutely convergent integral. The first two moments are absolutely convergent since q>4.

Fix x with r=|x|>=2. By their vanishing,

    4pi P(x) = integral f(y) [1/|x-y| - 1/r - (x dot y)/r^3] dy.

Split the integral into A={|y|<r/2} and B={|y|>=r/2}. On A, apply Taylor's formula in y at zero to K(y)=1/|x-y|. Its Hessian has operator norm 2/|x-y|^3. The segment from zero to y stays at distance at least r/2 from x. The Taylor remainder therefore has absolute value at most 8|y|^2/r^3. Since (1+s)^(-q)<=s^(-q), the contribution of A, including the factor 1/(4pi), is bounded by

    (8C/r^3) integral_0^(r/2) s^(4-q) ds
      = C 2^(q-2) r^(2-q)/(5-q).

The integral at zero converges because q<5. This estimate does not assert that f is singular at zero; it merely uses a larger integrable majorant for the weighted integral.

For the Newton-kernel term on B, first take B_near={|y|>=r/2, |x-y|<r/2}. There |f(y)|<=C 2^q r^(-q), and

    integral_(|z|<r/2) |z|^(-1) dz = pi r^2/2.

Its contribution after division by 4pi is at most C 2^(q-3) r^(2-q). On B_far={|y|>=r/2, |x-y|>=r/2}, the kernel is at most 2/r. Combining this bound with the subtracted constant term, whose absolute value is 1/r on all of B, gives at most

    (3C/r) integral_(r/2)^infinity s^(2-q) ds
      = C 3*2^(q-3) r^(2-q)/(q-3).

Finally, |x dot y|/r^3<=|y|/r^2, so the subtracted linear term on B contributes at most

    (C/r^2) integral_(r/2)^infinity s^(3-q) ds
      = C 2^(q-4) r^(2-q)/(q-4).

Adding the four bounds proves the stated estimate.

## Application to the exact finite rotating representation

Take the exact finite potentials, positive radii, integer damping order and real coefficients of ../finite_tail_integrability/PROOF.md, with c in (2/5,1/2). Set alpha=(1-c)/c and q=2alpha+2. Then 1<alpha<3/2 and 4<q<5. The fixed-parameter estimates in ../represented_tail_decay/PROOF.md give

    |U(y)| <= C_0 (1+|y|)^(-alpha),
    |DU(y)| <= C_1 (1+|y|)^(-alpha-1).

Use the Frobenius norm in the bound for DU. For any real 3 by 3 matrix A, Cauchy-Schwarz gives |tr(A^2)| = |sum_ij A_ij A_ji| <= sum_ij |A_ij|^2 = |A|_F^2. The source f=tr((DU)^2) consequently satisfies the theorem with C=C_1^2. If the displayed derivative bound instead uses the operator norm, |A|_F^2 <= 3 |A|_op^2 gives C=3 C_1^2. It is smooth. The solenoidal moment identities in ../pressure_moments/PROOF.md supply the two vanishing moments. Therefore its full-space Newton pressure obeys P=O(r^(-2alpha)) uniformly in direction. No homogeneous pressure correction or finite-radius boundary condition has been introduced.

The same fixed-parameter estimates give Omega=O(r^(-alpha-1)). The finite-tail theorem supplies the stronger remainder with delta=1>3-2alpha. All tail hypotheses of the energy and helicity identities in ../energy_helicity/PROOF.md are therefore satisfied by the exact finite representation and its Newton pressure. In particular, if its Euler momentum residual is identically zero, then

    E_ren^A = 0,    integral_R3 U dot Omega = 0,

where A is the exact leading sphere integral of |F|^2. This is a necessary condition, not an existence theorem. A nonzero floating-point estimate does not rigorously exclude a zero exact integral without a proved error bound.

## Dependencies and scope

The decay lemma uses the Newton kernel, its explicit Hessian, Taylor's formula, moment cancellation and elementary radial integrals. The application additionally uses the separately stated exact finite-basis decay, moment and energy/helicity results. The Newton pressure convention and Poisson identity are stated in ../pressure_consistency/PROOF.md. The estimate is quantitative in C, but no numerical upper bound for C_1 of any checkpoint is supplied here. No quadrature error, exact normalization or Euler solution is certified. This proof has not been formalized.
