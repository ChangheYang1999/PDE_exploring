# An escaping collinear orbit without Dini decay

Audit A215. Written: 2026-11-02T22:02:05Z. Status: CONFIRMED.

## Exact statement

Let B,W be C^1 vector fields on R3 with B complete and [B,W]=-kappa W for a constant kappa. Suppose there are R0,b>0 such that

    y.B(y)>=b|y|^2 for |y|>=R0.

Then there is a complete B orbit gamma that escapes to infinity in forward time and satisfies B cross W=0 at every point. Its backward limit is a nonempty compact invariant subset of {B cross W=0}. It lies in the compact set of points with bounded full B orbits. In particular, this applies to every C^2 uniformly sublinear Euler profile with c>0 and arbitrary finite omega, without a Dini derivative assumption.

If div B is a positive constant, the set of forward-bounded points is null. The existence of the special orbit therefore gives no positive-volume obstruction and does not prove nonexistence.

## Proof

Fix R>R0. On the radius-R sphere, the denominator B(y).y is strictly positive. The field

    V_R(y)=W(y)-[W(y).y/(B(y).y)]B(y)

is a continuous tangent vector field on that sphere. By the hairy-ball theorem it has a zero y0. At this point W(y0) is a scalar multiple of B(y0), including the possibility W(y0)=0.

Exact bracket transport gives

    D Phi_t(y)B(y)=B(Phi_t y),
    D Phi_t(y)W(y)=exp(kappa t)W(Phi_t y).

Since D Phi_t is invertible, linear dependence of B and W is invariant for every real t. Thus the whole orbit through y0 lies in the closed set {B cross W=0}.

For forward time, d|Phi_t y0|/dt>=b|Phi_t y0| as long as the orbit is outside the radius-R0 sphere. It starts outside and cannot cross back inward, so it escapes at least exponentially. Backward orbits enter, and then remain in, a fixed ball: outside that ball their radius decreases at least exponentially in backward time, and the inward boundary condition prevents exit. The alpha limit of y0 is consequently nonempty and compact. Completeness and continuity give its full invariance. It lies in the closed collinear set and every orbit in it is bounded, proving the claim.

For the final null-set assertion, choose a large ball D that traps the backward flow. Every forward-bounded point stays in D; otherwise the radial estimate would force escape. If K denotes this set, then K is measurable and Phi_t(K)=K. Positive constant divergence d gives |K|=|Phi_t(K)|=exp(dt)|K|. Since K has finite volume, |K|=0.

## Dependencies and scope

Only hairy-ball, elementary radial flow estimates and exact bracket transport are used. For Euler, B=(cI-omega J)y+U, W=curl U, kappa=1+c, div B=3c; uniform sublinearity supplies the radial bound. The argument is independent of the scattering map and therefore removes the extra Dini hypothesis from the existence conclusion of Theory Agent A Corollary T.6(c), but not from its precise asymptotic representation or projected divergence formula. The orbit may be entirely irrotational. No claim of a nonzero-vorticity orbit, more than one orbit, or a positive-volume family is made.
