# Flat-zero stable plaques and transverse capture

Status: CONFIRMED, A200. This is a geometric lemma; it does not assert that a required limiting unstable curve exists.

## Exact statement

Let B,W be smooth vector fields on R3, with B complete and [B,W]=-kappa W for a fixed real kappa. Write Psi_t for the backward B-flow and O={W!=0}. Let K be a compact invariant set on which all derivatives of W vanish.

Suppose x is in K, B(x)!=0, and there is a C1 curve L through x such that each y in L has a bounded forward Psi orbit and, for some C_y,ell_y>0,

    |Psi_t y-Psi_t x| <= C_y exp(-ell_y t), t>=0.

Then L is contained in {W=0}. In particular this applies to a sufficiently small Pesin strong stable curve through a regular point of K, provided a common compact forward trap is available.

Suppose a C1 immersed arc gamma through x is transverse to B(x), and

    T_x L + span(B(x),T_x gamma) = R3.

Then gamma cannot be a local C1 limit of immersed arcs gamma_n entirely in O. No absolute continuity of the stable lamination is needed for this conclusion.

## Proof that L is irrotational

Fix y in L. Its forward orbit and the orbit of x lie in a common compact ball. Enlarge that ball to contain the connecting segments at all sufficiently large times, and let L0 bound ||DB|| on a compact neighborhood of both orbits. Flatness of W on K and Taylor's formula give, for every integer N>=1,

    |W(Psi_t y)| <= C_N |Psi_t y-Psi_t x|^N
                   <= C_N C_y^N exp(-N ell_y t).

The exact bracket transport reads

    D Psi_t(y) W(y)=exp(-kappa t) W(Psi_t y).

The inverse derivative along this orbit is bounded by exp(L0 t). Thus

    |W(y)| <= C_N C_y^N exp((L0-kappa-N ell_y)t).

Choose N with N ell_y>L0-kappa and let t tend to infinity. This proves W(y)=0. The short flow saturation of L also lies in {W=0}, since that zero set is invariant by the transport formula.

## Proof of transverse capture

Restrict gamma and the flow time to small intervals. The map

    (s,t) -> Psi_t(gamma(s))

has rank two at x and, after shrinking, is a C1 embedded surface Sigma. Its tangent at x is span(B(x),T_x gamma). The analogous maps for gamma_n converge in C1 and define embedded surfaces Sigma_n locally. Because O is flow invariant, each Sigma_n is contained in O.

The fixed curve L crosses Sigma transversely at x. This intersection persists for all sufficiently large n. Explicitly, flatten Sigma in a C1 coordinate chart and express Sigma_n as small C1 graphs over it. A local parameterization l(r) of L has a nonzero derivative in the normal coordinate at r=0. Choose two small parameter values of opposite sign at which this normal coordinate has strictly opposite signs. Subtracting the small graph height of Sigma_n preserves those signs. The intermediate value theorem gives a zero, hence an intersection point of L and Sigma_n.

Such a point has both W=0, because it lies in L, and W!=0, because it lies in Sigma_n. This contradiction proves the second assertion.

## Application and scope

For the proposed generalized u-Gibbs localization, x is a regular point of a flat-zero compact support, L is its one-dimensional Pesin stable plaque, and gamma is a limiting unstable arc. The three directions stable, unstable and flow are independent because the spectrum is (+,0,-). The remaining existence input is that the original measured-curve construction supplies gamma as a C1 limit of image arcs inside O and supplies a regular flat point on a locally immersed part. This lemma does not supply or assume the truth of the external construction.

Only local flow times are used for Sigma_n. The curves need not be uniformly hyperbolic, and the limiting invariant set may contain singularities away from x. No pressure or actual-curl relation is used.
