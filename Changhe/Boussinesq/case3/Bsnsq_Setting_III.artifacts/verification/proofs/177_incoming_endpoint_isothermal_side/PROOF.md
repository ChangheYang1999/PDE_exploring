# An isothermal side at incoming endpoints with isolated exterior zeros

Status: CONFIRMED after independent derivation, primary-source audit, exact controls and actual Opus5.5 review with resolved follow-ups. This is a conditional beta-two theorem, not a full B2 exclusion. Written before the new controls.

## Statement and hypotheses

Use fixed orthonormal physical coordinates (x,y), curl W=partial_x W2-partial_y W1. Let W,Theta,Omega be C-infinity on the plane and satisfy

    div W=4, Omega=-curl W,
    W.grad Theta=0, (W.grad+1)Omega=Theta_x,
    W(X)=2X+o(|X|) at infinity.                       (1)

Suppose one connected component gamma of the zero set of W is a compact smoothly embedded arc, including its endpoints. Assume that DW has eigenvalues0,4 on gamma, the regular interior has the smooth fiber coordinates of packet173, and neither endpoint is accumulating: no other zeros approach either endpoint. Equivalently in the local center reduction, the scalar drift on a center manifold just outside each endpoint has a fixed nonzero sign. Every zero outside gamma is assumed isolated. In particular there are no other zero curves. At an incoming endpoint p, the exterior center drift points toward p. Suppose DW(p)=4n tensor n, and all derivatives of Theta-L and Omega vanish at p, where L=Theta(p). These extra local conditions hold at the beta-two B2 endpoints previously studied. No extra reflection symmetry is used in the theorem.

Let C be the local strong unstable curve through p. It separates a small neighborhood into two sides. The arc gamma is on one side of C. The conclusions are:

(A) There is a neighborhood N of p such that, on the other side of C,

    Theta=L, Omega=0.                                (2)

The statement is equality on an open region, not merely flatness on C. It holds even for arbitrarily flat nonzero incoming center drift and isolated degenerate exterior zeros.

(B) Consequently the analytic-strong-unstable-curve exclusion for outgoing endpoints also applies to this incoming endpoint: C cannot be a real analytic curve germ. This part uses the harmonic reflection and normal-nullcline argument given below.

(C) In fixed tangent-normal coordinates (s,z) at p with s pointing beyond gamma, it is impossible that W(0,z) is real analytic for |z|<delta and that Omega(s,z) is real analytic in z on this common connected interval for every0<s<delta. The trace condition can equivalently be imposed on U in B2, because W-U is affine. No condition that C itself crosses s>0 is required in this incoming case.

The hypotheses concerning isolated exterior zeros are essential to the argument supplied here. Accumulating endpoints, other nonisolated zero components, the general smooth beta-two endpoint problem, and beta>2 are not decided.

## Completeness, compactness, and exclusion of invariant loops

The asymptotic condition gives |W(X)|<=K(1+|X|), so the flow phi_t exists for all real t. On every sufficiently large circle W points strictly outwards, and in its exterior X.W(X)>=|X|^2. Thus each backward orbit remains in a bounded set. All zeros lie in a fixed compact disk.

The arc gamma is isolated as a zero component. At an interior point, the regular normal component has a unique nullcline, and the whole local zero set is the arc. At either endpoint a finite C4 center manifold contains the nearby equilibria, and its fixed nonzero exterior drift rules out other nearby zeros. A finite cover of gamma gives a zero-free separating neighborhood. The remaining zeros form a compact discrete set, hence are finitely many.

There is no invariant Jordan curve J. If D is its bounded complementary component, then the complete flow maps J onto itself and D onto itself: a plane homeomorphism maps complementary components to complementary components, and the image of the compact closure of D is compact. The variational equation gives det Dphi_t=e^(4t). Hence

    |D|=|phi_t D|=e^(4t)|D|,

which is impossible for t>0 because0<|D|<infinity. This argument requires no differentiability or rectifiability of J. It excludes periodic orbits, homoclinic loops, and any finite directed cycle of distinct connecting orbits whose endpoints can be joined along gamma.

## Incoming branches at isolated zeros

We record local facts before using a planar limit-set theorem. If DW(q) is invertible, differentiated thermal transport gives DW(q)^T grad Theta(q)=0. Thus grad Theta(q)=0, and the vorticity equation at q gives Omega(q)=0. Consequently DW(q) is symmetric, with trace4. It is either positive definite or has one positive and one negative eigenvalue. In the first case q has an open backward basin and is a source; in the second it has exactly two local incoming stable branches. In particular there are no sinks or foci at these invertible zeros.

If DW(q) is singular, its eigenvalues are0,4. A finite C4 local center manifold and the transverse smooth strong unstable curve can be simultaneously straightened. In the resulting C4 coordinates, invariance and two applications of Hadamard division give a C3 field of the form

    u'=g(u)+u v B(u,v), v'=v D(u,v),
    D>2, |B|<=M, g(0)=g'(0)=0.                      (3)

Indeed v=0 is the center manifold, u=0 is the strong unstable curve, and subtracting g(u) from u' gives a function vanishing both on v=0 and on u=0. The center manifold contains all nearby equilibria by its complete-orbit property. Isolation of q therefore makes g nonzero on each punctured half-interval. Any nonstationary orbit converging forward to q must eventually remain in the coordinate neighborhood. Since |v| grows at least as e^(2t) while it remains there, it must have v=0. On each sign of u, forward convergence then occurs exactly when g(u)/u<0. There are at most two incoming branches. If neither side is incoming, g(u)/u>0 on both sides and q is a source by the local estimate below.

The same local form applies at the endpoints. There g=0 on the arc side and has fixed sign on the other. No nonstationary orbit can converge forward to an interior arc point: a sufficiently small fiber rectangle from packet173 has dynamics a'=0,r'=4r and is backward invariant. An orbit that leaves this rectangle in forward time can never return. Within it a nonzero r must leave in finite time. At a nonaccumulating endpoint there is one incoming branch if it is incoming, and none if outgoing. Thus gamma as a whole has at most two incoming branches.

For later use, suppose g(u)/u>0 on one punctured side. In backward time T, |v(T)|<=|v(0)|e^(-2T), the sign of u is preserved, and, for k>M/2,

    d/dT [log|u|+k|v|]
       =-g(u)/u-vB-kD|v| <=(M-2k)|v|<=0.           (4)

Consequently the half-neighborhood |v|<epsilon, |u|e^(k|v|)<delta is backward invariant. Set h=|u|exp(int_0^T vB dt). Its derivative is

    h'=-exp(int_0^T vB dt) g(u)sgn(u)<0.

Since int_0^infinity |vB|dT<=M|v(0)|/2, the exponential has a positive finite limit, so |u| has a limit. A positive limit would bound |g(u)| away from0 and force h to decrease at a fixed positive rate forever. Hence u,v tend to0. This proves the one-sided open backward basin, without assuming a finite order of g or exponential center contraction. If both sides have the outward sign, their union and u=0 give a full source neighborhood.

## Every bounded limit set is one zero point

We justify the global step with a theorem for continuous surface flows, because collapsing gamma need not produce a differentiable field. Collapse gamma to one point. A smoothly embedded compact arc is a nonseparating continuum contained in an open disk. Corollary6.4 of Yokoyama, arXiv:2109.12478v5, makes the quotient homeomorphic to the plane. The quotient map pi is proper: a compact set in the quotient has compact inverse image, since the only nonsingleton fiber is the compact arc and outside a compact neighborhood the quotient is unchanged. For completeness this can also be checked by covering a quotient compact set by finitely many images of bounded neighborhoods; pi is a closed map, as the saturation of a closed set is either itself or its union with gamma.

The original flow fixes gamma pointwise. It descends to a continuous complete quotient flow. To check joint continuity, for t in a compact time interval the maps phi_t are uniformly continuous on a compact neighborhood of gamma and fix gamma; points approaching its collapsed fiber therefore stay close to that fiber. Away from the fiber continuity is ordinary flow continuity. The quotient has finitely many equilibria and no other singular points.

Apply Corollary5.9 of that paper to this plane flow, also with reversed time. For a nonclosed orbit its limit set is empty, a singular point, a limit cycle, a limit nonperiodic virtual circuit, or a Q-set. Corollary4.2 excludes Q-sets on a surface contained in the sphere. A bounded original semiorbit has a nonempty compact limit set, so the empty case and any end at infinity are absent. Its quotient has compact closure too. Thus a virtual circuit here is an ordinary compact circuit. A cycle would lift to a periodic orbit outside gamma and is already excluded.

A point-limit at the collapsed fiber lifts to a single point of gamma. To see this for an alpha-limit, if the original alpha-limit contains an interior arc point, a negative-time iterate enters a backward invariant fiber rectangle and thereafter follows a fixed fiber to one arc point. If it contains no interior point, it is a connected subset of the two endpoints, hence a singleton. The connectedness of an alpha-limit of a bounded semiorbit follows from its description as the intersection of decreasing compact connected orbit-tail closures. For an omega-limit contained in gamma, the backward-invariant rectangle argument above excludes an interior point for a nonstationary orbit; again connectedness gives one endpoint. Thus every connecting orbit incident at the collapsed vertex has well-defined individual endpoints on gamma in the original plane.

Yokoyama's Definition4 permits a circuit with infinitely many edges, even when the singular set is finite. That possibility must not be discarded without proof. In the present quotient every connecting edge has its forward limit at one of finitely many singular points. At an ordinary zero it must be one of the at most two incoming local branches proved above. At the collapsed gamma it must be one of at most two endpoint branches. Distinct complete orbits cannot share one local incoming branch, by uniqueness. Therefore a circuit has only finitely many edges here. As a nontrivial directed circuit it contains a directed cycle with no repeated vertices except the start and end. This is a finite-graph fact: follow edges and remove an initial segment and any repeated subloops until a shortest directed closed walk remains.

If the cycle avoids the collapsed vertex it lifts to a Jordan curve of trajectories and point equilibria. If it includes that vertex, its incoming and outgoing edges lift to limits b,a in gamma. Join b to a by the unique subarc of gamma; if a=b use that point. The other vertices are distinct, trajectories are disjoint, and no nonstationary trajectory intersects gamma. Each closed connecting trajectory is an embedded compact arc because it is injective at finite times and has its indicated distinct endpoint limits; a same-endpoint connection is already a Jordan loop. Thus the lifted cycle, with the possible gamma subarc, is an invariant Jordan curve. This is impossible by the area argument. No circuit can occur.

It follows that each bounded forward or backward semiorbit converges to an individual zero in the original plane. In particular every incoming branch of any isolated zero has a single alpha-limit, either an isolated zero or a point of gamma. We use this conclusion only for such branches and the endpoint incoming branch.

## Propagating a constant-temperature neighborhood through isolated zeros

For a fixed real L define P_L as the open set of points having a neighborhood on which Theta=L and Omega=0. It is invariant under every finite flow time. Thermal transport carries the constant value to the image of an open neighborhood, so Theta_x=0 there. The homogeneous vorticity equation then carries Omega=0 to its image in either time direction.

At a source q the open backward basin has Theta=Theta(q) by transport and continuity. Each backward orbit remains in a compact local set. The variation-of-constants identity

    Omega(X)=e^(-T)Omega(phi_(-T)X)
       +int_0^T e^(-t)Theta_x(phi_(-t)X)dt            (5)

gives Omega=0, because the thermal value is constant on the open basin and Omega is bounded there. Thus a source whose value is L has a neighborhood contained in P_L.

Let q be any isolated zero with Theta(q)=L, and suppose each of its incoming branches is contained in P_L. We prove that a full neighborhood of q is contained in P_L. For a hyperbolic saddle, straighten the stable and unstable manifolds as coordinate axes. The equations have u'=u A, v'=v D with A<-a<0, D>d>0. In backward time any point with u!=0 in a sufficiently small rectangle exits through u=+delta or u=-delta, with |v| decreasing. Choose short exit sections inside P_L about the two stable-branch points (±delta,0). Every point off u=0 then has a backward iterate in P_L; finite-time invariance puts it in P_L. Continuity gives Theta=L,Omega=0 also on u=0. These equalities hold on an entire open rectangle, proving the claim there.

At a singular zero use(3). On an outward center side g(u)/u>0, equation(4) gives a one-sided open backward basin, and the source argument gives Theta=L,Omega=0 on it. On an incoming side g(u)/u<0, run backward time until reaching |u|=delta or exiting the coordinate domain. The sign of u is fixed and |v| decreases. The integrating factor h=|u|exp(int_0^T vBdt) is now strictly increasing, while its exponential factor has a positive finite limit. If the orbit never reached the prescribed u section, h would have a positive finite limit and therefore |u| would too. The incoming g would then be bounded away from0, forcing h to increase at a fixed positive rate forever, a contradiction. Thus the exit occurs in finite backward time. The orbit cannot leave through |v|=epsilon, since |v| decreases, or through u=0, since that axis is invariant. This exit time is not claimed uniform as u(0) tends to0; flat center drift can make it arbitrarily large. Taking |v(0)| sufficiently small puts its exit point in a short section in P_L about that incoming branch. A smaller common rectangle on both sides works. Finite-time invariance gives(2) off u=0, and continuity gives it on u=0. This proves the full-neighborhood assertion, including saddle and semisaddle degeneracies.

Now take the incoming endpoint branch eta with omega-limit p. Its alpha-limit is a zero q. It cannot lie in gamma: eta, together with the gamma subarc between its two limits, would form an invariant Jordan loop. Hence q is an isolated exterior zero, with Theta(q)=L by transport along eta and continuity.

Build the ancestral graph by adjoining every incoming branch of q, then every incoming branch of their isolated alpha-limits, and so on. There are finitely many isolated zeros and at most two incoming branches at each. A directed cycle would give an invariant Jordan loop by the same lifting argument, so the graph is acyclic. None of its ancestors can be in gamma: the path from that ancestor along the graph and eta back to p in gamma, with the appropriate gamma subarc, would contain such a loop. Every vertex is therefore isolated, and the finite ancestral graph has roots with no incoming branches. The local classification above makes these roots sources. Continuity of Theta along every edge makes all their values equal L.

Order the finite graph from roots to q. The sources have neighborhoods in P_L. Invariance propagates P_L along their outgoing edges. Once all incoming branches of a vertex lie in P_L, the preceding local argument gives its full neighborhood in P_L. Induction reaches q and then all of eta. This does not assume that source basins exhaust the plane or that finite differences imply continuity of a branch. It is a finite directed graph argument about the actual flow.

## The side beyond the strong unstable curve

At p choose the simultaneous center and strong-unstable coordinates in(3), with gamma at u<=0,v=0. The exterior center branch is u>0,v=0, and g(u)<0 there. Fix delta>0 on this incoming branch. Since eta lies in P_L, a short section u=delta, |v|<epsilon lies in P_L. Every point0<u<delta, |v|<epsilon sufficiently close to p reaches that section in finite backward time by the incoming integrating-factor argument just proved. It therefore lies in P_L. The coordinate u=0 is C, and u>0 is the side opposite gamma. After shrinking the physical neighborhood, this proves(A).

## Analytic consequences

For(B), assume that C is a regular real analytic curve germ with p in its interior. Its tangent is the strong unstable direction n, transverse to the endpoint tangent. The equalities in(A) extend to the boundary C by smoothness. On its exterior side, curl W=0 and div W=4, so W=grad H with Lap H=4 locally. C is a trajectory and W is tangent to it, giving the homogeneous Neumann condition partial_n H=0 on C. Here is an explicit analytic reflection construction. Write the physical complex coordinate as F(zeta), where F is holomorphic, F'(0)!=0, and F maps the real zeta axis onto C; such an F comes by holomorphically extending a real analytic regular parametrization. The pulled-back potential has Laplacian4|F'|^2 and zero normal derivative on the real axis. The real analytic particular solution P(zeta)=|F(zeta)|^2 has that Laplacian. Put g(a)=partial_b P(a,0), let g^hol be its local holomorphic extension, and choose a holomorphic primitive K with K'=-i g^hol. Then h=Re K is harmonic and partial_b h(a,0)=g(a). Therefore P0=P-h has the required Poisson source and zero normal derivative. Subtract P0 from the actual pulled-back potential and reflect the harmonic difference evenly. The difference is smooth up to the line and has zero normal derivative; even reflection is C2 and harmonic, hence real analytic. Adding P0 and returning by F^(-1) gives an analytic extension of H and its physical gradient W across C. This argument uses the actual one-sided potential and elementary holomorphic primitives. It does not infer convergence from a formal series or invoke an unspecified analytic Cauchy problem.

The one-sided jet of W agrees with its full smooth jet at p and with the jet of its analytic extension. Both the actual smooth normal nullcline and the extended analytic normal nullcline exist because the normal derivative is4. Their jets, and the jets of their reduced tangential components, are determined by that common field jet through implicit differentiation. The actual reduced component vanishes on the terminal half-arc of zeros, so all of its derivatives vanish at p. The analytic reduced component has the same flat jet and therefore vanishes identically. The extended analytic field therefore has a zero curve through p tangent to the endpoint tangent direction. Its positive-tangent segment lies on the exterior side of C because C is transverse to that direction at p. There it is the actual W, extending gamma as a connected zero arc beyond p. This contradicts the hypothesis that gamma was the whole connected component. Thus C cannot be analytic.

For(C), the incoming center branch eta has tangent s direction and hence a graph z=h(s) for0<s<delta' with h(s)->0. Every point of eta lies in the open set P_L. For each sufficiently small fixed s>0, Omega(s,.) vanishes on a nonempty open interval about h(s). Real analyticity on the stipulated common connected interval makes it zero on that entire interval. Hence W is curl-free and its two components are harmonic on a positive half-rectangle. The analytic value trace W(0,z) suffices to extend each harmonic component across s=0: subtract the harmonic analytic extension of the trace and apply odd reflection to the remaining zero-trace harmonic function. Smoothness up to the line makes the reflection C2 and harmonic; it is consequently analytic. As in(B), the analytic normal-nullcline reduction is flat and therefore zero, extending the same zero component beyond p. This contradiction proves(C). Unlike the crossing argument in174, the zero intervals on the positive-s lines now come from the open neighborhood of eta.

## Dependencies, scope and verification plan

Dependencies: packet173's exact local fiber chart; packet174's endpoint geometry and finite C4 center/strong-unstable normalization (with its primary Podvigina theorem citation); elementary flow uniqueness and variational equations; the Jordan curve theorem and change of variables for area; elementary finite graph induction; Yokoyama2109.12478v5 Corollaries4.2,5.9,6.4 and Definition4, used for continuous plane flows with the stated compactness and finiteness checks; local analytic harmonic reflection and holomorphic primitives as explicitly constructed above. The separate Spadaro1504.04258v1 example documents why finite singular points alone would not justify a finite-edge claim. It is not used as a source for a stronger theorem.

The open PDE system, the canonical full-plane inverse and the B2 center jet enter only through the listed hypotheses. This conditional result does not assert a B2 candidate, a global isothermal field, a full beta-two exclusion, or an unrestricted NO. The local sign estimates, coupled examples and failures when positive divergence or incoming-branch information is removed passed113 exact controls and3 negative controls. The explicit reflection construction passed12 supplemental exact checks after its final clarification. Actual Opus5.5 reviewed topology, degenerate passage and analytic reflection; all substantive disagreements are resolved in verification/review_adjudication.md. These algebra checks are not a formal proof of the global topological argument.

Written UTC 2026-10-21T14:55:09.948614+00:00.

Audit completed UTC 2026-10-21T15:12:58.502401+00:00.
