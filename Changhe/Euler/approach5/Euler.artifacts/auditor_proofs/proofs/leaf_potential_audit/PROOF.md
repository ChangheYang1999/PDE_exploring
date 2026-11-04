# Exact leaf potentials and their limits as an obstruction

## Hypotheses and identities

Let U,P be C^2 rotating Euler profiles, div U=0, c!=1/2, and omega finite. No far-field condition is needed for the local statements. Put a=1-2c, X=cy+U, B=X-omega Jy, Omega=curl U, q=|U|^2/2, M=Jy dot U, and

    H=P+q+c y dot U+c(2c-1)|y|^2/2-omega M,
    G=(P+q+c y dot U-omega M)/(2c-1).

Then H=-a(G+c|y|^2/2). The exact Bernoulli identity gives

    a(U-grad G)=B cross Omega,                    (1)
    B dot grad G=U dot B.                         (2)

Equation (2) also follows by differentiating H and |y|^2 along B. These identities already hold for C^1 U,P. Every B-orbit segment has U-action G(end)-G(start), so every periodic B orbit has zero circulation. An explicit global transfer function is supplied; no Livsic theorem is needed for this implication.

## Integrable plane field

On Z1={B cross Omega!=0}, the C^1 plane field E=span(B,Omega) is integrable because [B,Omega]=-(1+c)Omega. Its leaves are the orbits obtained by composing B and Omega flow segments, or equivalently the maximal flow-saturations of vortex curves. Cauchy's formula makes the field invariant under B.

With sigma=i_Omega volume=d(U dot dy), let alpha=(B cross Omega)^flat. Then

    alpha=dH+a X^flat=-i_B sigma,
    d alpha=a sigma,
    alpha wedge d alpha=0.

The sign follows from i_B sigma(v)=volume(Omega,B,v)=(Omega cross B) dot v. Alpha annihilates E. Thus on each immersed leaf S,

    X^flat|S=-(1/a)d(H|S),
    U^flat|S=d(G|S)=-(1/a)d(H|S)-c d(|y|^2/2)|S.   (3)

Both forms are exact, but they have different potentials. In particular U's potential is G, not just -H/a. Every closed curve in a leaf has zero U-circulation.

The scalar triple-product identities in B08 are also exact:

    X dot (Omega cross B)=-omega Omega dot (Jy cross X),
    X dot grad H=-a|X|^2+omega Omega dot (Jy cross X),
    partial_theta H=-a M+Omega dot (Jy cross X).

On {Omega=0}, grad H=-aX pointwise. Saying this on an invariant closed set does not extend it to an open neighborhood unless vorticity vanishes there.

## Vortex-filament pairing

Let gamma be a C^2 embedded closed curve, oriented, and A_gamma its Biot-Savart field with curl A_gamma equal to the associated line current. It is O(|y|^-3) at infinity because the total tangent current integral is zero. Near the curve it obeys |A_gamma(y)|<=C/dist(y,gamma). The latter bound follows by parametrizing near a closest point and bounding the kernel by C/(d^2+s^2), then integrating in arclength s. Smooth tubular coordinates exist for sufficiently small radius.

For any continuous Omega, bounded on a fixed tube,

    absolute value of integral_(tube_delta) Omega dot A_gamma
       <= C sup_tube|Omega| delta -> 0.             (4)

This elementary bound proves C6(c) under the regularity relevant to a periodic orbit. It does not require the printed curvature expansion with O(1) remainder, which needs stronger control than bare C^2 to justify uniformly. It also does not assert that a small nonzero tube integral has either sign.

For bounded C^1 divergence-free U with curl U=Omega, integration by parts gives

    integral_gamma U dot dl
       =lim_(R->infinity) integral_(B_R) Omega dot A_gamma.

The boundary term is bounded by C R^-1 sup|U| and vanishes. This is a ball-truncated, possibly conditionally convergent pairing. Absolute convergence at infinity is not being assumed. The singularity on gamma is locally integrable, so the distributional curl identity is legitimate.

## Exact conclusion and unproved extrapolation

B08's core leaf theorem, its displayed triple-product identities, and C6(a,c,d) are confirmed, with the potential and tube-proof corrections above. For 0<c<1/2, C6(d)'s invariant-measure identities give

    integral |X|^2 dmu=omega integral M dmu,
    omega integral partial_theta P dmu=-(1-2c) integral |X|^2 dmu.

A periodic circulation identity being a consequence of Bernoulli does not prove that it cannot be combined with another geometric hypothesis to yield a contradiction. The broad assertion in C6(b) and the final paragraph that no cone condition can help has not been established. Nor does (4) prove that all local flux signs are impossible. Such impossibility claims need a defined class of cone conditions and a countermodel or theorem for that class. A complete smooth abstract model satisfying the relevant transport and divergence constraints has not been supplied.

Audit recorded: 2026-11-02T18:56:51Z
