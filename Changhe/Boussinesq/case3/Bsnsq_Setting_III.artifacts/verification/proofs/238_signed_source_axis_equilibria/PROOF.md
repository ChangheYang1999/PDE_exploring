# Two additional axis equilibria in a signed Gaussian transport field

## Statement and exact setting

This is a theorem about an explicitly prescribed external-source field, not an unforced B2 profile. Let beta=3 and

    Omega_e(x,y)=A x [exp(-(x^2+(y-4)^2)/2)
                    -(3/10)exp(-2(x^2+y^2)/9)],
    A=80/(1-9exp(-8)).

Let Psi_e be the decaying whole-plane canonical stream function with -Delta Psi_e=Omega_e, U_e=(-Psi_ey,Psi_ex), and W=3(x,y)+U_e(x,y)-U_e(0). Then W has an axis equilibrium in each of the disjoint rational intervals

    x=0, -6681/1000 < y < -6680/1000,
    x=0, -1884/1000 < y < -1883/1000.

The first is a hyperbolic forward source and the second a saddle. The center is also a forward source, with eigenvalues 1/2 and 11/2. Thus entering a small center ball cannot be inferred solely from backward completeness or the positive center eigenvalues. The source is the literal Gaussian configuration of NUM scan_signed_16, normalized by its exact canonical strain. No assertion identifies it with NUM's fitted source.

The numerical values in the statement are rational test brackets. This argument was written before its arithmetic checks. The exact rational certificate passed all 13 comparisons at 2026-10-22T01:00:36.765849+00:00, closing that finite arithmetic step. Its SHA256 is 52b6a8a62c4b1ff506a26e9cef0cac7ebf12b07c0fa5f65bd766cff84835c9b3. The pre-check proof is preserved in verification/PROOF_before_status_closure.md, and its hash is recorded in the certificate. The theorem is CONFIRMED for this exact external-source field.

## Canonical inverse and axis formula

For a>0 define B_a(S)=(1-exp(-aS))/S and B_a(0)=a. The identity

    Delta[x B_a(x^2+(y-h)^2)]=-4a^2 x exp(-a(x^2+(y-h)^2))

follows by differentiation. Therefore

    Psi_e=A x [B_(1/2)(x^2+(y-4)^2)
                -(243/160)B_(2/9)(x^2+y^2)]

is smooth, solves the required Poisson equation and has velocity O(r^-2). It is the canonical decaying inverse: the difference from any other decaying smooth inverse velocity is a bounded harmonic vector field, hence is constant and then zero by its decay. The upper-lobe strain is A(1-9exp(-8))/32=5/2. The centered lobe contributes zero strain. Consequently DW(0)=diag(3-5/2,3+5/2), and the moving-center subtraction is exactly U_e(0), not a fitted drift.

Write phi(y)=W2(0,y). Since U1 is odd in x, W1(0,y)=0 for all y, and

    phi(y)=3y+A[B_(1/2)((y-4)^2)
                 -(243/160)B_(2/9)(y^2)
                 -(1-exp(-8))/16+27/80].             (1)

At points away from 0 and4 the derivative is

    phi'(y)=3+A[2(y-4) B'_(1/2)((y-4)^2)
                  -(243/80)y B'_(2/9)(y^2)],         (2)
    B'_a(S)=((1+aS)exp(-aS)-1)/S^2.

The rational certificate checks phi(left)<0<phi(right) on the first interval, and phi(left)>0>phi(right) on the second. Continuity and the intermediate value theorem give the equilibria.

At an axis point parity makes DW diagonal. Its entries are 6-phi'(y) and phi'(y), since div W=6. The certificate bounds 2<phi'<3 throughout the first interval, so both eigenvalues are positive. It bounds -4<phi'<-2 on the second interval, so the eigenvalues have opposite signs. The derivative bounds also give uniqueness within each of these two small brackets. They do not assert that there are no other equilibria.

## Exact rational enclosure

For rational z>=0 let E_n(z)=sum_(k=0)^n (-z)^k/k!. Taylor's integral remainder, whose integrand has a fixed sign because exp(-t)>0, gives

    E_(2m+1)(z) <= exp(-z) <= E_(2m)(z).

Take m=160. All operations and sums are rational. For an interval z in [l,u], monotonicity gives the enclosure [E_321(u),E_320(l)]. Interval addition, subtraction, multiplication and division use the exact extrema of rational endpoint operations; division is used only for intervals separated from zero. Substitution in (1) at the four rational endpoints proves the four signs. Substitution in (2) with y in each whole bracket proves the derivative intervals. Every bound is stored as exact numerator/denominator strings in JSON. No binary floating-point value is used to decide a sign.

This algorithm proves the finite inequalities if its rational outputs satisfy the stated comparisons. The included verifier checks those comparisons directly and records hashes of the proof and executable. It does not constitute a Lean formalization or an interval enclosure for NUM's fitted map.

## Domain consequence and scope

A sufficiently small neighborhood of the additional hyperbolic forward source has backward trajectories tending to that source. One can see this directly here because the real diagonal Jacobian has positive entries: for reverse time and displacement Z, d|Z|^2/dt=-2 Z.DW_* Z+O(|Z|^3)<0 in a sufficiently small ball; the same inequality bounds the norm by an exponentially decreasing function. Such trajectories never reach a sufficiently small ball around the origin. The external-source center construction therefore cannot define its values everywhere simply by waiting longer for every backward orbit to enter the origin's ball.

This says nothing decisive about general B2 existence. A different basin could require other compatible data. The source's canonical velocity, parity, drift and center strain are correct, but its prescribed vorticity is not asserted to be the transported vorticity. The theorem explains a possible obstruction in this particular external-source experiment only.
