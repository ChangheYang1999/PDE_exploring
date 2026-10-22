# Three-region geometry when the beta-two zero set is the central arc

Status: CONFIRMED by complete independent proof and controls, with actual Opus5.5 written review326 and the limitations of follow-ups327/328 recorded in verification/review_adjudication.md. This is a necessary configuration in the subclass Z=gamma, not a B2 exclusion or existence assertion.

## Statement and precise prerequisites

Let the smooth full-plane B2 fields satisfy

    W=2X+U-U(0), div W=4, Omega=-curl U,
    W.grad Theta=0, W.grad Omega+Omega=Theta_x,
    U(X)=o(|X|), Theta(-x,y)=Theta(x,y),
    W(SX)=S W(X), S(x,y)=(-x,y).

The nonzero center temperature coefficient and all other B2 hypotheses remain in force. Suppose the entire zero set of W is the compact central smooth arc gamma, with endpoints p+ in x>0 and p-=S p+. The arc meets the axis only at the center, its interior is normally repelling, and its endpoints are outgoing. Write L=Theta(p+)=Theta(p-).

The following previously audited consequences of these hypotheses are stated explicitly, so the proof's dependence can be checked.

1. The complete flow phi_t has bounded backward orbits, and each tends to one point of gamma. Every point outside gamma escapes in forward time. In particular there are no other forward trapped orbits. These are the beta-two arc and limit-set results of45,53,177 and179. Outside a fixed disk, d|phi_t X|²/dt>=2|phi_t X|².
2. At each endpoint p there is a smooth strong unstable curve C through p with two branches. Both branches tend to p in backward time. A finite C4 chart (u,v) near p puts C on u=0, the terminal arc on v=0,u<=0, and the flow in the form

       u'=g(u)+uv B(u,v), v'=v D(u,v), D>=2,
       g=0 for u<=0, g>0 for u>0.

   A smaller whole positive-u half-rectangle E belongs to the backward basin of p. It is disjoint from Cstar: every strong orbit eventually lies exactly on u=0, whereas a backward orbit from u>0 stays strictly positive at every finite backward time. Merely having limit u=0 would not distinguish these two kinds of orbit. Its points have Theta=L,Omega=0. On the negative-u side, the backward orbit remains in the larger chart and tends to an interior point of gamma with negative arc coordinate. These are173,174,179; in particular C is the only local part of the strong-orbit set.
3. Let Cstar_p consist of p and the two complete strong orbits, and define O_p as the backward basin of p with Cstar_p removed. Then O_p is nonempty, open, connected and invariant. The set F of points with backward limit in the interior of gamma, including those equilibrium points, is open. Theta=L and Omega=0 on O_p and all their ambient derivatives vanish on Cstar_p. No full neighborhood of a point of Cstar_p has Theta identically L or Omega identically zero. These are179.
4. On E_escape=R² minus gamma there is a C1 scattering diffeomorphism

       Phi:E_escape -> R² minus {0},
       Phi(phi_t X)=exp(2t)Phi(X).

   Its normalized value is the forward asymptotic direction. Thus distinct complete escaping orbits have distinct directions. Denote the direction sets whose backward limits are p+ and p- by I+ and I-. Denote the directions of the remaining orbits by Gamma+ union Gamma-, in the notation for the two sides of the interior arc. The scattering map is given by53,54,61 and the beta-two specialization of lead4.12. The closed-arc property of I+ and I-, previously obtained in53, will also be derived below rather than assumed. Item4 is only needed for the directional conclusion, not for the planar separation argument.

Write C+=Cstar_p+, C-=S C+, O+=O_p+, O-=S O+.

Then:

(A) C+ and C- are disjoint smooth properly embedded copies of R. Both branches of each line escape forward and tend backward to its own endpoint. C+ lies in x>0, and C- in x<0.

(B) F,O+,O- are exactly the three connected components of R² minus (C+ union C-). They are simply connected. Their boundaries are respectively C+ union C-, C+, and C-. The whole axis lies in F, F=S F, O+ lies in x>0, and O- in x<0.

(C) Theta=L and Omega=0 on the closed complement of F, which is closure(O+) union closure(O-). U is harmonic on its interior O+ union O-. Every point of the boundary of F is approached from F by points with Theta!=L, and by points with Omega!=0. These two sequences need not be the same. All ambient jets of Theta-L and Omega vanish on that boundary. The actual U has no harmonic or analytic full neighborhood there, as in179; this does not exclude an extension of its one-sided restriction by a different field.

(D) The directions of the O+ orbits form the interior of I+, and the two C+ orbits other than p+ have its two endpoint directions. The corresponding assertions hold with minus signs. The F orbits off gamma have directions Gamma+ union Gamma-. In a reference to directions of closure(O+), the equilibrium p+ must be omitted because it has no escaping direction.

## Properness and separation of the strong lines

Each small strong branch is part of one complete orbit, because the vector field does not vanish away from p on that branch. The two orbits are distinct: their backward tails stay in different local branches. They cannot meet by uniqueness, and neither is periodic because its backward limit is p. By prerequisite1 both escape forward, and the exterior radial estimate makes their radius tend to infinity, not just unbounded along a subsequence.

A parametrization is most easily constructed by gluing the local smooth arc C through p to its two forward orbit tails. Choose a small closed arc of C containing p. Each endpoint of that arc lies on its corresponding orbit and has W nonzero. Parametrize its local branch outward using a smooth coordinate of the arc, then extend outward along forward time. The two resulting half-lines are joined using the original smooth parametrization of C near p. Their images are disjoint except at p. This gives a continuous injection c:R->R² with c(0)=p. A smooth match of its chosen parameter at the two junctions is not needed for properness. It can be chosen so |c(t)| tends to infinity as t tends to either plus or minus infinity. For the negative parameter end one traverses the first orbit toward its forward infinity as t decreases; one does not make its physical backward limit infinity.

This last radial property makes c proper: inverse images of compact sets are bounded and closed in R. A proper continuous injection from R into the Hausdorff plane is a homeomorphism onto its closed image. To see this without a compact-domain assumption, any convergent sequence c(t_n) lies in a compact plane set; properness supplies a convergent subsequence of t_n, and injectivity identifies its only possible limit. At every regular point the image is locally the smooth orbit arc in a flow box. At p the prescribed local smooth arc is the full strong-orbit set in a small chart by prerequisite2. The homeomorphism and properness prevent a distant parameter segment from accumulating into one of these local arcs. Thus the image is a smooth one-dimensional embedded submanifold. Its arclength parameter is defined on all of R, since each unbounded end has infinite length, and gives a smooth proper embedding.

If C+ met C-, uniqueness of the backward limit would force p+=p-, which is false. ODE uniqueness and W(SX)=S W(X) give phi_t(SX)=S phi_t(X). Reflection therefore maps C+ to C-. If a point of C+ lay on x=0 it would be fixed by S and hence also belong to C-. This is impossible. Connectedness of C+ and the positive x coordinate of p+ now put the whole line in x>0. The assertions for C- follow by reflection.

## The three open components and their exact boundaries

Every point has one backward limit in gamma. The basin definitions and prerequisite3 therefore give the disjoint partition

    R² = F disjoint-union O+ disjoint-union O-
                disjoint-union C+ disjoint-union C-.                 (1)

All three first sets are open and nonempty. Connectedness of O+ and O- is known from their descriptions as forward sweeps of connected exterior half-neighborhoods. F is path connected: for X in F the curve phi_(log s)X, 0<s<=1, joins X continuously to its backward limit as s decreases to0, and stays in F. Join two such limits along the interior of gamma. This also treats X already on gamma. Thus the three open sets in(1) are precisely the connected components of the complement of the two lines.

For a proper embedded line C+, add the point infinity to the plane and to the line. Properness shows that the extended map is a continuous injection of the one-point compactification of R, a circle, into the sphere. The Jordan separation theorem gives two components of the complement, with common boundary C+ in the plane. The connected set C- lies entirely in one of them. Denote the other by A. It is open and connected, avoids both lines, and its closure is A union C+. Thus it is also closed relative to the complement of the two lines, and is exactly one of F,O+,O-.

Both closure(F) and closure(O-) contain p-. For F this follows from the interior arc; for O- it follows from the reflected exterior half-rectangle, whose positive-u side is disjoint from Cstar by prerequisite2 and hence belongs to O-. But p- cannot belong to closure(A), because that closure is A union C+ and C- lies on the other side of C+. Hence A=O+, and

    boundary(O+)=C+.

The reflected argument gives boundary(O-)=C-. Their closures are disjoint, since O+ avoids C-, O- avoids C+, and the two closed lines are disjoint. Let Y belong to C+. Every neighborhood of Y contains points on the side opposite O+. Closure(O-) is a closed set not containing Y, so a sufficiently small such neighborhood avoids it. Opposite-side points there must lie in F by(1). Therefore C+ is contained in boundary(F). Similarly C- is. Conversely the openness of the other sets and(1) imply boundary(F) is contained in C+ union C-. This proves the claimed equality.

The axis is connected and misses both lines. It contains the center in the interior of gamma, so it lies in F. O+ is connected and avoids the axis. It contains points of E sufficiently near p+, all with x>0, so it lies in x>0. Reflection and uniqueness of limits give O-=S O+ and F=S F.

## Simple connectedness, with the planar criterion justified

For each D in {F,O+,O-}, its complement in the sphere is connected. For F the complement consists of the two closed exterior basins and infinity; each closure(O+) union {infinity} and closure(O-) union {infinity} is connected, since it is the closure in the sphere of its connected unbounded open basin. They meet at infinity. For O+, its complement contains the connected set C+ union C- union {infinity}, and closure(F), closure(O-); each attached closure is connected and meets the line set along its nonempty boundary. This union is exactly the complement. The argument for O- is reflected.

We recall why connectedness of that complement is sufficient here. A Jordan polygon in D separates the sphere into a bounded polygonal interior and the other component containing infinity. The connected complement of D is disjoint from the polygon and contains infinity, so it lies entirely in the outer component. Hence the whole polygonal interior lies in D. A general loop in the open planar set D can be approximated and homotoped inside D to a polygonal loop: take a finite subdivision subordinate to open disks contained in D and replace each short piece by its chord within the corresponding disk. A sufficiently small perturbation of its finitely many vertices, still in those disks, gives only finitely many transverse crossings and no coincident edges. Subdivide at crossings and successively split off simple polygonal loops; the number of edges decreases at each split. Each such polygon bounds its finite triangulated interior in D and contracts there. The splits may introduce paths to and from each simple loop; they appear as basepoint conjugations, which preserve null-homotopy. Rejoining these finite contractions contracts the original loop. Thus D is simply connected. No smooth or analytic extension across either bounding line is used in this topological step.

## Temperature, vorticity and the necessity of interior nonconstancy

Prerequisite3 gives Theta=L and Omega=0 in O+ and O-, and continuity gives both equalities on their closures. The boundary identities show that these closures have union R² minus F. The interiors are exactly O+ union O-: each point of C+ or C- is also approached by F, so none is an interior point of the complement. On the open basins div U=0 and curl U=-Omega=0, which imply componentwise Delta U=0 by differentiating the divergence and curl identities. Thus U is harmonic there.

Fix Y in boundary(F). By prerequisite3 no ball centered at Y has Theta identically L or Omega identically zero. The closed complement of F has exactly those equalities. Hence, in each ball of radius1/n, choose a point in F with Theta!=L and, independently, a point in F with Omega!=0. Both sequences tend to Y. Flatness of every jet also follows directly here: derivatives of a smooth function that vanishes on an open basin vanish on that basin and, by continuity, on its boundary. Thus this part does not need a separate propagation theorem once(B) has been established. Neither this flatness nor harmonicity on the exterior implies analyticity of the actual fields across the lines.

## Direction arcs and the role of the escaping-orbit bijection

An orbit in E_escape is mapped by Phi onto an entire positive ray, because t runs through R and Phi(phi_t X)=exp(2t)Phi(X). Conversely each ray has exactly one complete orbit as its preimage. This proves both the surjectivity and the injectivity needed in identifying direction sets.

Since O+ is open, connected and invariant, Phi(O+) is an open connected set invariant under positive dilations. Its radial projection J+ is a nonempty open connected subset of the circle. It is a proper subset because there are escaping orbits through the normally repelling interior of gamma in F, and their rays are disjoint from Phi(O+). At this stage J+ may include the case of the circle with one point removed; the boundary argument below excludes that case.

The full endpoint basin consists exactly of O+ and C+, so its escaping directions are

    I+ = J+ union {d1,d2},                                         (2)

where d1,d2 are the directions of the two distinct strong orbits. They are distinct by the orbit-ray bijection, and neither lies in J+. The homeomorphism Phi determines the endpoints without assuming that I+ is closed. In the relative space E_escape, the boundary of O+ is C+ minus{p+}, by(B). Homeomorphisms preserve relative boundaries, so

    boundary_(R² minus0) Phi(O+)
                    = Phi(C+ minus{p+}).                            (3)

The right side consists of the two distinct rays in directions d1,d2. On the other hand Phi(O+) is the open cone over J+, and its relative boundary is the cone over the boundary of J+ in the circle. A nonempty connected proper open subset of a circle is an open arc or a circle with one point removed. The latter case has a single boundary direction and is excluded by(3). Thus J+ has exactly two endpoints d1,d2 and I+=closure(J+) is a nondegenerate closed proper arc. The closed arcs I+ and I- are disjoint because closure(O+) minus{p+} and closure(O-) minus{p-} are disjoint invariant subsets, and distinct complete orbits have distinct directions. Reflection proves the minus case. The escaping F-orbit directions are Gamma+ union Gamma- by definition.

This independently strengthens the input accounting: the closed-arc premise used in the lead's proof is already a consequence of the scattering homeomorphism and(B). If one instead uses the earlier closed-arc theorem, the lead's interval argument is valid: deleting an interior point and one other distinct point from a closed interval leaves nonempty separated pieces, while J+ is connected. Without scattering injectivity, different strong orbits can have the same direction. The manufacture below demonstrates this failure when the sublinear-velocity condition is removed.

## Scope, dependencies and report audit

The proof establishes the lead's frozen4.7(xvi)(a)-(d), subject to the previously audited B2 prerequisites listed at the start. It adds no parity in y, wall condition, absolute center-velocity constraint or harmonic correction. It excludes no B2 profile: the full coupled problem remains open within F and under the matching conditions on its two characteristic boundaries. Profiles with additional zeros outside gamma are not covered by this decomposition. The four-source/two-saddle example of180 is consequently outside these hypotheses and is not a counterexample.

The only general topological input is Jordan separation for an embedded circle; the simple-connectedness consequence is proved here for these open planar sets. ODE uniqueness, finite-time smooth dependence and elementary harmonic identities are used as stated. No numerical state or experimental convergence assertion is a premise. Exact controls and review evidence are recorded alongside this proof, with no claim of proof-assistant verification.

Written UTC 2026-10-21T16:04:42.515006+00:00, before new controls.

## Manufactured geometry and a counterexample without the scattering premise

The following separate field supplies exact controls and illustrates a premise that cannot be dropped. It is not in the B2 admissible class. Define a smooth odd function h by h=0 on[-1,1] and

    h(x)=2(x-1) exp[-1/(x-1)²] for x>1.

Use odd reflection for x<-1, and set

    W=(h(x),[4-h'(x)]y),
    U=W-2X, Psi=[2x-h(x)]y, Omega=h''(x)y.                           (3)

All right derivatives at x=1 of the displayed h are zero, because each is an exponential times a finite Laurent polynomial in x-1. This proves smooth gluing at both endpoints. With t=1/(x-1)²,

    h'(x)=2exp(-t)(1+2t)<=4exp(-1/2)<4.

The derivative with respect to t is2exp(-t)(1-2t), so its maximum occurs at t=1/2. Hence4-h' is uniformly positive. The derivative h' is bounded and |h(x)|<=2|x|, which give linear growth and completeness of W. Direct differentiation gives div W=4, U=(-Psi_y,Psi_x), Omega=-Delta Psi and the required x reflection. The zero set is exactly[-1,1] times{0}.

For |x|<1 the orbits have constant x and y(t)=exp(4t)y(0). At x=+/-1 the same formula gives the two strong lines. For x>1, the backward scalar x equation decreases to1: a different finite limit would have h nonzero, and monotonicity prevents divergence. Also y decays exponentially in backward time, since4-h' has a fixed positive lower bound. Thus this whole half-plane has backward limit(1,0); forward x tends to infinity by the same scalar argument. Reflect for x<-1. Consequently F={|x|<1}, O+={x>1}, O-={x<-1}, and C+/-={x=+/-1}. All three components are convex and have exactly the asserted boundaries.

Nevertheless the upper strong orbits at x=1 and x=-1 both have asymptotic direction e2, as do all the upper interior-fiber orbits. The lower ones likewise share -e2. Hence proper strong lines and the three-region partition alone do not give the direction-orbit bijection. The missing full-plane hypothesis is explicit: along(0,y), U=(0,2y), so |U|/|X|=2, rather than tending to0. The model does not contradict prerequisite4 or the B2 theorem.

One may choose a smooth even f with f(x)=a0x² near0 and f constant near and outside both endpoints, and put Theta=f(x). Then W.grad Theta=0 everywhere, by the disjoint supports of h and f'. But near the origin Omega=0, so the vorticity equation has residual -2a0x. This refutes the model as a coupled B2 profile with a0 nonzero. It also separates a valid geometric manufacture from a manufactured PDE solution.

Independent audit completed UTC 2026-10-21T16:17:21.164380+00:00.
