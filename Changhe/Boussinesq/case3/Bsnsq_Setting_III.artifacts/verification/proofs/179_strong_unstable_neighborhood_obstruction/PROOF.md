# No constant-temperature or irrotational neighborhood along the endpoint strong orbits

Status: CONFIRMED by independent full derivation and exact controls, with actual Opus5.5 written reviews314/316 and explicitly recorded follow-up availability limits. This is a conditional beta-two boundary theorem, not a full B2 exclusion.

## Exact statement and hypotheses

Let W,Theta,Omega be smooth on the physical plane with coordinates(x,y), and assume

    div W=4, Omega=-curl W,
    W.grad Theta=0, (W.grad+1)Omega=Theta_x,
    W(X)=2X+o(|X|), W=2X+U-U(0).                    (1)

In the last formula U is the B2 divergence-free velocity; the local assertions about analyticity use only that W-U is affine. Let gamma be its compact smooth central zero arc with normally repelling interior, and let p be a nonaccumulating endpoint. Assume the local conditions already proved for the B2 arc: in physical tangent-normal coordinates DW(p)=4n tensor n, with tangent tau perpendicular to n, and Theta-Theta(p) and Omega flat to every order at p. The exact local center/strong-unstable construction is the one in173,174,177. Its finite C4 simultaneous coordinates have p=(0,0), gamma on v=0,u<=0, strong unstable curve C on u=0, and

    u'=g(u)+uv B(u,v), v'=v D(u,v),
    D>2, |B|<=M, g=0 for u<=0.                     (2)

On small positive u suppose either g>0 (outgoing endpoint), or g<0 (incoming endpoint). In the incoming case require every other zero outside gamma isolated, so177 applies. No such extra global zero hypothesis is imposed in the outgoing case. All coordinates in(2) are spatial changes with unchanged physical time. C itself is smooth by the strong unstable theorem; this is separate from the finite-C4 simultaneous chart.

Let L=Theta(p) and let Cstar consist of p and the two complete orbits extending the branches of C. Then:

(A) No neighborhood of any X in Cstar has Theta identically L.
(B) No neighborhood of any X in Cstar has Omega identically0. Equivalently there is no neighborhood of X on which U is real analytic. Both equivalence directions here use the coupled equations and the open irrotational side proved below, not only the identity Omega=-curl U.
(C) Every ambient derivative of Theta-L and Omega vanishes at every point of Cstar. Near each such point there is an open side of its orbit on which Theta=L and Omega=0, but every full neighborhood contains points with Theta!=L and points with Omega!=0.

For the following additional assertion impose the B2 x-reflection, assume Z={W=0}=gamma, and assume the established arc meets the axis only at its central point. Its endpoints p+ and p- are exchanged by reflection, so their temperature values agree. Write Cstar+ and Cstar- for their strong orbits. Define

    O+={X not in Cstar+: phi_(-t)X tends to p+},
    O-=the x-reflection of O+.

(D) Both endpoints are outgoing. O+ and O- are nonempty open connected invariant sets with Theta=L and Omega=0. Their boundaries are contained in Cstar+ union Cstar-. Each is a connected component of int{Omega=0} and of int{Theta=L}.

Every claim is conditional on these arc and endpoint hypotheses. Accumulating endpoints, incoming endpoints without the isolated-exterior-zero premise, and basin boundaries outside these strong orbits when Z differs from gamma remain outside the theorem. No existence or general nonexistence statement is made.

## Local exterior region and arc-side projection

The sublinear correction to2X makes the flow complete in both time directions, by the linear-growth inequality. For an incoming endpoint,177 gives a small open exterior side with Theta=L and Omega=0. For an outgoing endpoint this follows directly from(2). In backward time T, |v(T)|<=|v0|exp(-2T), and for k>M/2 the function |u|exp(k|v|) is nonincreasing for u>0. A sufficiently small such half-neighborhood is backward invariant. With

    I(T)=integral_0^T v B dt, |I(infinity)|<=M|v0|/2,
    h(T)=u(T)exp(I(T)), h'=-g(u(T))exp(I(T))<0,

u(T) has a nonnegative limit. A positive limit would make h' bounded above by a negative constant, impossible. Thus u,v tend to0. Thermal transport gives Theta=L on this open backward basin. The vorticity source Theta_x vanishes there and boundedness of the backward orbit gives

    Omega(Y)=exp(-T)Omega(phi_(-T)Y) ->0.             (3)

Choose a connected open set E equal in the chart to {u>0} intersected with a sufficiently small rectangle, so E contains a full one-sided neighborhood beyond C, with p and both small branches of C in its boundary. All its points have Theta=L,Omega=0, in either endpoint case. In the outgoing case E can be chosen backward invariant or inside a larger backward-invariant half-neighborhood. In the incoming case only the local equalities, not backward invariance of E, are asserted.

For u0<0 in(2), backward time stays on the arc side and

    u(T)=u0 exp(-I(T)),
    |v(T)|<=|v0|exp(-2T),
    |I(infinity)-I(T)|<=M|v0|exp(-2T)/2.             (4)

Shrink the initial rectangle so these bounds prevent leaving the chart. The limit

    P(u0,v0)=u0 exp(-I(infinity))<0                 (5)

is the arc coordinate of its backward limit. It is continuous in the initial point: finite-time dependence is continuous, and the last bound in(4) gives uniform convergence of I(T) on a fixed smaller rectangle. Also

    exp(-M|v0|/2)|u0|<=|P(u0,v0)|
                         <=exp(M|v0|/2)|u0|.         (6)

For fixed small nonzero v1, P(u,v1) tends to0 as u tends to0 from below. Its image for -epsilon<u<0 therefore contains a whole terminal interval(-eta,0), by continuity and the intermediate value theorem. No differentiability, monotonicity or uniform upper exit-time estimate of this projection is needed.

## Endpoint nonconstancy and failure of a harmonic neighborhood

First Omega cannot be zero on a full neighborhood of p. If it were, constant divergence and zero curl would make both components of W harmonic and real analytic there. Its normal component has nonzero normal derivative4 at p, so its zero set is an analytic graph near p. Gamma lies on that graph. The tangential component restricted to the graph is analytic and vanishes on the terminal negative interval of gamma, hence also on a positive interval. This extends the same zero component beyond its endpoint, contradicting the prescribed local zero set.

Nor can Theta be L on a nondegenerate terminal subarc of gamma. The projection(5)-(6) puts sufficiently small arc-side backward limits in that subarc, so Theta=L on the arc side. E supplies the same equality on the exterior side; continuity fills C. This gives a full constant-temperature neighborhood of p. On its smaller arc side the backward trajectories stay in a slightly larger constant-temperature neighborhood, as(4) shows. Equation(3) then gives Omega=0 on that side. E gives it on the exterior side and continuity fills C, yielding the forbidden harmonic neighborhood. This also proves that Theta-L cannot vanish on a full neighborhood of p.

These arguments establish(A)-(B) at p without presupposing an analytic trace or an analytic strong curve.

## Thermal obstruction at every other point of Cstar

Each X in Cstar minus{p} can be written X=phi_T X1 for some T>=0 and some X1 on a small branch of C, with coordinate X1=(0,v1), v1!=0. This follows from backward convergence along the strong unstable branch. If Theta=L on a neighborhood N of X, transport pulls that equality to the neighborhood phi_(-T)N of X1. It contains all (u,v1) with u<0 sufficiently close to0. Their backward limits are (P(u,v1),0). Equation(5) and continuity of Theta imply Theta=L at those points of gamma. Their image contains a terminal interval by(6), contradicting the endpoint nonconstancy just proved. This proves(A).

## Irrotational obstruction, including the exceptional physical component

Suppose Omega=0 on a connected disk N around X in Cstar minus{p}. Then W and U are harmonic, hence real analytic on N. The vorticity equation gives Theta_x=0 there, and thermal transport gives

    W2 Theta_y=0 on N.                              (7)

If W2 is not identically zero, its zero set has empty interior by the identity theorem for real analytic functions on connected domains. Hence Theta_y=0 on a dense open subset and, by smoothness, throughout N. Thus Theta is constant on N and its value is Theta(X)=L. This contradicts(A).

The exceptional case W2 identically0 cannot be omitted: the local field W=(4x,0),Omega=0,Theta=f(y) satisfies all the local equations(1) for any smooth f. We now rule it out using the actual endpoint geometry.

Choose X=phi_T X1 as above with X1 in the boundary of E. Set

    G=N union {phi_r Y: Y in E, 0<=r<=T}.             (8)

Every phi_r(E) is open; its points have Theta=L by transport. At every point on their orbit segment Theta_x=0, so(3) in finite forward time gives Omega(phi_r Y)=exp(-r)Omega(Y)=0. The swept union is connected: any of its points is joined to its initial point in connected E by the orbit segment included in(8). N intersects phi_T(E), since X1 is a boundary point of E and X lies in N. Thus G is a connected open set. W is harmonic there. Its analytic component W2 vanishes on N and therefore on G. Div W=4 and curl W=0 now give

    partial_x W1=4, partial_y W1=partial_x W2=0,
    W=(4x+c,0) on G                                (9)

with one constant c. Since E approaches p and W(p)=0, c=-4p_x. Continuity of DW at p and DW(p)=4n tensor n show n=+/-e1 and the tangent to gamma is +/-e2. Since the strong curve is transverse to that tangent, the fixed vertical ray from p in the exterior tangential direction belongs to E for sufficiently small positive displacement: in tangent-normal coordinates C is a graph s=sigma(z) with sigma(0)=0, and at z=0 that ray has s>0. Equation(9) makes W zero on this ray, contradicting the absence of exterior zeros near a nonaccumulating endpoint. This simpler zero-ray argument avoids assigning a coordinate component of the center drift in a different chart. It proves(B)'s vorticity assertion.

If U is analytic on a disk around X, so is Omega. That disk meets phi_T(E), where Omega vanishes, and the analytic identity theorem makes Omega vanish on the whole disk, already excluded. At p use E itself for the nonempty intersection. Conversely Omega=0 locally would make U harmonic and analytic locally. This proves the stated equivalence. Analyticity of U alone does not generally imply zero curl without this open zero subset.

## Flat jets and the one-sided equalities

The strong unstable convergence to p is exponential in backward time, even though p also has a zero eigenvalue. For a fixed X on either branch,

    |phi_(-T)X-p|<=C exp(-aT), a>0.

Along the compact backward orbit closure all finite derivatives of W are bounded, and the variational equations give exponential bounds for every finite derivative of phi_(-T) at X. Differentiate Theta=Theta composed with phi_(-T). Flatness at p of arbitrarily high order dominates every finite product of flow derivatives, exactly as in178(E); for derivative order m use a bound C exp((m K_m-aN)T). Thus every thermal jet at X is flat. In the finite-time vorticity formula all differentiated source terms vanish because the thermal jets vanish along the whole orbit. The remaining factor is exp(-T) times a composition with a function flat at p, which tends to0 with every derivative. This proves all vorticity jets flat on Cstar. At p this was a hypothesis.

For a sufficiently small neighborhood of a regular X=phi_T X1, the local diffeomorphism phi_T maps the exterior side E near X1 to an open side of the orbit near X. Transport and(3) give Theta=L,Omega=0 there. At p the side is E. Combining this with(A)-(B) proves(C).

## Global exterior basins when Z equals gamma

We detail the global prerequisites used in(D). The completeness, finite-limit-set and collapse argument in177 covers nonaccumulating endpoints of either sign; the incoming sign is used only for its later isothermal-side theorem. When Z=gamma there are no exterior singular points. It gives convergence of every bounded semiorbit to one point of gamma, in particular every backward orbit. An incoming endpoint would have a connecting orbit from some point of gamma back to that endpoint; if that point differs from the endpoint, the connection and the gamma subarc form an invariant Jordan loop; if it is the same endpoint, the closure of the homoclinic orbit is an invariant Jordan loop, which is excluded by the exact area multiplier exp(4t). Hence both endpoints are outgoing. This step does not assume that individual point basins are open.

Let F be the set of points with backward limit in the open arc gamma interior. The local smooth fiber rectangles from173 show it is open near that arc, and finite-time flow images show F is globally open. It includes the interior arc itself. Recall that Cstar, by definition, includes the endpoint itself as well as both complete strong orbits. The basin of each endpoint is the disjoint union of that Cstar and its exterior open basin O. Indeed every orbit tending backward to the endpoint eventually stays in(2). On the negative-u side(5) gives a limit strictly inside gamma; u=0 puts it on Cstar; positive u puts it in the open exterior side. Conversely positive-u points of the chosen small E converge backward to the endpoint and cannot lie on Cstar, by uniqueness and preservation of the sign of u. Consequently

    O+=union_(T>=0) phi_T(E+),
    O-=union_(T>=0) phi_T(E-).                      (10)

Each is open, invariant in both time directions by its original basin definition, and connected: every point in the union is joined by an orbit segment in that union to connected E+ or E-. They are disjoint, since backward limits are unique. Thermal transport gives Theta=L on every open phi_T(E). Thus Theta_x=0 throughout the swept sets, and the vorticity equation along each swept orbit segment gives Omega(phi_T Y)=exp(-T)Omega(Y)=0. This does not assert general flow invariance of Omega. Reflection gives the common value of L. The partition is

    R2 = F disjoint-union O+ disjoint-union O-
                      disjoint-union (Cstar+ union Cstar-). (11)

The sets Cstar+ and Cstar- in(11) include both endpoints, exactly as defined in the statement. Every point of F or O- has an open neighborhood avoiding O+, and every point of O+ is interior. Hence its boundary is contained in Cstar+ union Cstar-. The analogous assertion holds for O-.

Finally O+ is contained in some connected component H of int{Omega=0}. If H were larger, its path-connectedness as a connected open subset of the plane would give a path from O+ to a point of H outside O+. Its first exit meets the boundary of O+, and that point lies in H with an irrotational neighborhood. This contradicts(B) at the appropriate endpoint's strong orbit. Therefore H=O+. The identical argument for int{Theta=L} uses(A) and the equality of the endpoint values. This proves(D).

## Dependencies and scope

Dependencies: independently audited173 local fibers,174 strong-unstable endpoint jets,177 local form and finite-limit-set result plus incoming-side theorem,178 flat-jet propagation estimates; elementary ODE completeness and variational equations; the real analytic identity theorem for harmonic functions; analytic implicit functions; connectedness and paths in open planar sets. The proof of the exceptional W2 case was independently replaced by the explicit zero-ray contradiction. No numerical approximation is a premise, no boundary or gauge correction is added, and no theorem-prover proof is claimed.

Written UTC 2026-10-21T15:28:53.357226+00:00, before new verification controls.

Audit completed UTC 2026-10-21T15:39:29.014275+00:00.
