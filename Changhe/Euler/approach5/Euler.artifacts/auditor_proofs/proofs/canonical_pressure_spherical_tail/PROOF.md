# Canonical pressure means and the reconstructed model pressure

## Statement

Let 1<beta<2 and let u be a real C2 divergence-free vector field on R3. Suppose, uniformly at infinity,

    u(y)=u_h(y)+O(|y|^-2),

where u_h is a nonzero C2 divergence-free field off the origin satisfying the rotating homogeneity law

    u_h(R Q_R theta)=R^-beta Q_R u_h(theta), theta in S2,

with Q_R rotations. No derivative bound on the remainder is assumed. Let P_can=sum R_i R_j(u_i u_j), where the Riesz multiplier is -i xi_i/|xi|. Then P_can belongs to L2. Define unit-sphere integrals

    P_r=integral_S2 |u_h(theta).theta|^2,
    P_t=integral_S2 (|u_h(theta)|^2-|u_h(theta).theta|^2),
    C_beta=(2-beta)P_r+(beta-1)P_t>0.

The exact conclusions of LIT73 are

    integral_S2 P_can(R theta)
      =((2-2beta)P_r-P_t) R^-2beta/(2beta)+O(R^(-beta-2)),
    integral_S2 (P_can+|u|^2/2)(R theta)
      =C_beta R^-2beta/(2beta)+O(R^(-beta-2)).

The first is negative and the second positive at every sufficiently large R. These are spherical means, not pointwise or basin signs. The pressure normalization is part of the theorem.

For the specific A331 reconstruction, with its normalized independent Lamb potential H and P_*=H-|v|^2/2-(Ay).v, the exact exterior mean of P_* is minus the mean kinetic energy. Thus the spherical mean of P_can-P_* has the positive asymptotic just displayed. This diagnoses one pressure correction and supplies no new universal nonexistence theorem.

## 1. Regularity and the exact spherical identity

The assumptions make u bounded and O(r^-beta), so u_i u_j is in L2. Fourier L2 boundedness of the Riesz transforms supplies the stated canonical pressure. Distributionally,

    -Delta P_can=div div(u tensor u)=sum_{i,j} partial_i u_j partial_j u_i.

The right side is locally C1. Local elliptic regularity gives the classical C2 pressure representative needed below. Let

    F_r(R)=integral_S2 |u(R theta).theta|^2,
    F_t(R)=integral_S2 (|u(R theta)|^2-|u(R theta).theta|^2),
    M(R)=integral_S2 P_can(R theta).

For T=u tensor u and n=y/|y|,

    integral_{|y|=R} (div T).n
      =d/dR(R^2 F_r(R))-R F_t(R).

Indeed div(T n)=(div T).n+T:Dn and Dn=(I-n tensor n)/R. Integrate over an annulus and differentiate its outer radius to obtain the formula. Integrating the Poisson equation over the full ball then gives

    R^2 M'(R)=-d/dR(R^2 F_r(R))+R F_t(R).

All fields are regular at the origin, so no inner-source integration constant is present. Consequently

    M(R)=-F_r(R)+integral_R^infinity (2F_r(s)-F_t(s)) ds/s+C.

The integral converges absolutely because u=O(r^-beta). Both velocity terms tend to zero. If C were nonzero, M would tend to C, and Cauchy-Schwarz on spheres would force the radial L2 integral of P_can to diverge. Hence C=0. This is the exact formula, valid before a homogeneous expansion:

    M(R)=-F_r(R)+integral_R^infinity (2F_r(s)-F_t(s)) ds/s.

No integrability or asymptotic estimate for F_r' is required.

## 2. Evaluate the tail

Rotations preserve sphere measure and radial components. The uniform remainder estimate gives

    F_r(R)=P_r R^-2beta+O(R^(-beta-2)),
    F_t(R)=P_t R^-2beta+O(R^(-beta-2)).

The squared remainder O(R^-4) is absorbed since beta<2. Insert the expansions into the exact formula and integrate the powers. This gives the stated coefficient ((2-2beta)P_r-P_t)/(2beta) for pressure. Adding (P_r+P_t)/2 gives C_beta/(2beta). Each coefficient of C_beta is positive, while each nonzero contribution to the pressure coefficient is negative. The errors are smaller by the positive power 2-beta.

This calculation is valid without an Euler transport equation. It requires neither a derivative asymptotic for u-u_h nor absolute integrability of the pressure source over all space.

## 3. The exact exterior mean of the independent model pressure

Use the A331 fields with 2/5<c<1/2, beta=1/c-1, A=cI-omega J and a=1-2c:

    B=Ay+U1, curl v=W, div v=0,
    a v+grad H=B cross W,
    P_*=H-|v|^2/2-(Ay).v.

U1 is compactly supported; v=v_h+O(r^-2); H is normalized to zero at infinity and H=O(r^{1-beta}). On the exterior of supp U1, the identity

    Ay cross curl v=grad((Ay).v)-A^T v-(Ay).grad v

and A^T=cI+omega J give

    (1-c)v+(Ay).grad v+omega Jv+grad[H-(Ay).v]=0.

Set G(R)=integral_S2 v(R theta).theta. Global divergence freedom and regularity at the origin imply R^2 G(R)=0, hence G=G'=0. The integral of the radial component of the first three terms above is

    (1-c)G(R)+cR G'(R)=0.

The rotation cancellation is exact. Integrating the angular derivative of v(R theta).theta along the divergence-free rotation generator J theta shows

    integral_S2 ((Jy).grad v).theta
      =-integral_S2 v.J theta
      =integral_S2 (Jv).theta.

Thus the spherical mean of H-(Ay).v is constant in exterior radius. Both terms tend uniformly to zero since beta>1, so the constant is zero. It follows that

    integral_S2 P_*(R theta)=-integral_S2 |v(R theta)|^2/2

for every exterior sphere, not just asymptotically. Part2 now gives

    integral_S2(P_can-P_*)(R theta)
      =C_beta R^-2beta/(2beta)+O(R^(-beta-2))>0.

Replacing P_* by P_can repairs its scalar Poisson equation but changes the independent Lamb potential. The already confirmed A338 excludes any Euler pressure for this specific reconstructed velocity; the mean calculation is not that any-pressure proof. Neither result excludes arbitrary Euler attractors or supplies a sign for a basin boundary flux.

## Verification record

The complete LIT73 proof was read. The two tensor flux signs, unit-sphere normalization, zero integration constant and exterior rotation cancellation were independently checked. No computation was needed. Fourier L2 boundedness and local elliptic regularity are the standard external analytic inputs; A331's marked model and its tail estimates are explicit additional dependencies only in Part3. Source hashes and a retained copy are in verification.
