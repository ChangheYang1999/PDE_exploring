# A vortical stagnation point need not have vorticity as its strongest stable direction

## Refuted claim

B07 and Section 4.3 of in the team records assert under H0 that a vortical stagnation point with forward eigenvalues {1+c,lambda_2,lambda_3}, lambda_2>0>lambda_3, has vorticity as the strong stable direction for backward time. Section 4.4 further identifies every compact invariant subset of {Omega!=0} as singular-hyperbolic by using that line and quotient area expansion. These statements are false as written. A spectral gap and a dominated splitting are missing.

## Exact family

Fix any 0<c<1/2 and omega!=0. For a real parameter d, let

    U(x,y,z)=(d x-omega y, omega x-(1+d)y, z),
    M=DU,
    P=-1/2 [(d+d^2-omega^2)(x^2+y^2)
            +2 omega(1+2d)xy+2z^2].

Then div U=d-(1+d)+1=0 and Omega=(0,0,2omega). The similarity field is diagonal:

    B=((c+d)x,(c-1-d)y,(c+1)z).

For any affine U=My the momentum residual before pressure is

    [M+M^2+omega(JM-MJ)]y.

In this family that symmetric matrix has diagonal entries
(d+d^2-omega^2,d+d^2-omega^2,2), with xy entry omega(1+2d), and all other off-diagonal entries zero. It is exactly -D^2 P. Thus this is an entire C^infinity solution of the full profile equation for every c and omega under consideration, with no numerical approximation.

At the vortical stagnation point zero, the forward spectrum is

    {c+d, c-1-d, c+1}.

For d>1, the backward direction x contracts at rate c+d>c+1, while vorticity lies along z and contracts at rate c+1. Thus the asserted designation of vorticity as the strongest stable direction is false.

For d=1, the backward spectrum is

    {-(1+c), 2-c, -(1+c)}.

The compact invariant set K={0} lies in {Omega!=0}. It has a two-dimensional eigenspace with exactly equal negative exponents -(1+c). No one-dimensional contracting subspace can be dominated by a complementary two-dimensional subspace: the latter necessarily contains a vector with the same contraction exponent. Accordingly K is not a three-dimensional singular-hyperbolic set with a one-dimensional strong stable bundle and a two-dimensional dominated sectional-expanding complement. This disproves the asserted implication from exact vorticity contraction and quotient area expansion to singular hyperbolicity.

## What remains true

If one separately assumes 0<lambda_2<1+c, then vorticity is the strong stable eigenvector, -lambda_2 is weak stable, and -lambda_3=lambda_2+1-2c>lambda_2. These are the stated Lorenz-like eigenvalue inequalities. The quotient area expands at rate 1-2c whenever Omega stays uniformly nonzero; that is an exact consequence of the two-form transport law. Quotient area expansion alone does not choose an invariant complement or prove domination.

All examples here grow linearly. They violate H1 and H1-prime and are not counterexamples to the target nonexistence conjecture. They refute the explicitly H0 local and compact-set claims, not every possible global argument using decay. No geometric Lorenz construction satisfying the complete global kinematic requirements has been certified.

Other local corrections: exact exponential contraction of a vortex segment follows from Cauchy's formula, but does not identify it with the entire strong stable leaf in the absence of a proved dominated splitting. Frozen-vorticity completeness is valid by A048; it cannot be justified by the false inference that U tends to zero implies globally bounded Omega.

Audit recorded: 2026-11-02T18:53:25Z


## Further audit: a zero transverse eigenvalue is possible

The revised B07 case list still omits a nonhyperbolic possibility. In the exact affine family above set d=-c and choose omega nonzero. Then

    U=(-c*x-omega*y, omega*x-(1-c)*y, z),
    B=(0,(2*c-1)*y,(1+c)*z), Omega=2*omega*e3,
    P=-1/2 [ (c*c-c-omega*omega)*(x*x+y*y)
                      +2*omega*(1-2*c)*x*y+2*z*z ].

Direct substitution is covered by the affine matrix identity already proved. At every point of the x-axis, B=0 and the spectrum is {0,2*c-1,1+c}. Thus a vortical zero need not be hyperbolic, and the strict cases of two negative transverse eigenvalues or one negative and one positive are not exhaustive. The vorticity line remains the one-dimensional exponentially contracting direction of the backward flow at this example; a neutral direction is also present. For the repeated case d=1, the two backward stable rates coincide, so neither is a uniquely stronger or weaker direction.

These exact profiles satisfy the claimed local H0 scope and violate decay. They refute the proposed exhaustive classification, not the campaign conjecture. A repaired list must include a zero eigenvalue and distinguish strict rate inequalities from equality.
