# External limits near an expanding surface flow

Status: CONFIRMED at A614, A615, A616. Exact hypotheses, proof and limitations are stated below. Informal independent verification; no formal build or numerical proof is claimed.

## 1. Statement and dependencies

Let S be a C2 surface without boundary near the sets considered. It need not be orientable, compact or complete. Let X be a C1 vector field and Phi its local flow. A compact set Lambda is invariant if the flow through every point of Lambda exists for all real times and stays in Lambda. Assume its equilibria form a finite set E, each a hyperbolic saddle for the TWO-DIMENSIONAL field X. Assume a positive C1 area density nu on an open neighborhood V of Lambda satisfies

    Lie_X nu=d nu, d>=gamma>0 on V.

Let y outside Lambda have a forward orbit defined for every time t>=0, with compact closure in S and omega(y) contained in Lambda. Then omega(y) is a single member of E. In particular there is no such external orbit if E is empty.

The expansion assumption can instead be: a positive C1 density nu0 is defined near Lambda and every invariant Borel probability mu on Lambda has integral div_nu0(X) dmu>0. In particular it suffices that every such probability is supported on E and tr DX(q)>0 for each q in E.

The proof uses elementary C1 flow-box theory, the local C1 stable and unstable manifolds of a hyperbolic saddle, compactness of probabilities on a compact metric space, and the change-of-variables formula. No generalized Poincare-Bendixson or classification of surface minimal sets is imported. The conclusion concerns an orbit starting outside Lambda; it does not say that Lambda itself contains no regular recurrent point or periodic orbit.

## 2. Flux expansion and zero transverse measure

In an oriented patch set beta=i_X nu and choose an orientation of a transverse arc so that beta is positive. Its coordinate is the integral of beta. If a regular passage P(x)=Phi_(tau(x))(x) joins transverse arcs with trajectory in V, differentiation adds a time term proportional to X, annihilated by beta. The flow identity for nu and D Phi_t X=X(Phi_t x) therefore give

    P*beta=exp(integral_0^tau(x) d(Phi_t x)dt) beta.

With a density on a nonorientable surface the formula holds for absolute flux and absolute derivative. Passage orientation may reverse; every distance estimate below uses absolute values. Any passage of duration at least h has absolute derivative at least exp(gamma h).

For t>0, invariance and change of variables give

    nu(Lambda)=integral_Lambda exp(integral_0^t d(Phi_s x)ds)dnu(x)
              >=exp(gamma t)nu(Lambda).

Compactness makes this finite, hence nu(Lambda)=0. This implies zero flux length on any compact transverse arc T0. Indeed a flow box F(s,t)=Phi_t(xi(s)) has positive continuous area density relative to ds dt. The saturation of (Lambda cap T0) times a fixed small time interval is contained in Lambda by invariance. Positive transverse measure would give positive area, a contradiction. Thus Lambda cap T0 is closed and nowhere dense on every such arc. Merely having no interval would be a weaker statement; the measure argument proves what is used.

## 3. Local saddle blocks with C1 regularity

Take small disjoint blocks around the finitely many saddles, with closures in V. Here is the local description required in the subsequent construction. In a smooth coordinate chart centered at a saddle, write the two C1 invariant manifolds as x=f(y) and y=g(x), after aligning the eigendirections. Their slopes at0 vanish. The coordinates

    u=x-f(y), v=y-g(x)

are a C1 diffeomorphism near0. Subtracting the invariant-manifold tangency identities and applying the fundamental theorem of calculus to the original C1 field shows, along trajectories,

    u'=u A(u,v), v'=v B(u,v),

with continuous A tending to lambda>0 and B tending to -b<0. This does not assert that a C1 coordinate change produces a C1 transformed vector field. Choose the block |u|<=r, |v|<=s so that A>=lambda/2 and B<=-b/2. Its two v-boundaries are incoming; its two u-boundaries are outgoing. Each retained boundary segment is transverse. An entering orbit exits in finite forward time unless u=0, in which case it converges to the saddle. A complete orbit in the block must have both u=v=0.

As an incoming point tends to a stable crossing, u tends to0 and its passage time tends to infinity: boundedness of A gives the necessary lower bound for the time to reach |u|=r. During that time |v| decays exponentially, so its exit tends to the corresponding unstable crossing. The sign of u chooses the outgoing side. These facts hold on both incoming arcs and both sides of their stable crossings.

Choose the corner parameters r,s so that all four corners avoid Lambda. This is possible because the set has area0 and the local coordinate Jacobian is bounded above and below. Omit small corner intervals disjoint from Lambda, while retaining all stable and unstable crossings. These gaps lose no Lambda point crossing the block boundary. The remaining incoming and outgoing arcs are compact, disjoint transversals with endpoints off Lambda. Collars of them cover Lambda near the boundaries. There are no other chosen sections in block interiors.

## 4. Construction of finitely many disjoint sections

The regular part of Lambda outside the interiors of the blocks is compact. The boundary collars and finitely many additional flow boxes cover it. Take central transverse arcs of these additional boxes outside the blocks, with small excess in both arc length and flow time, so the cover has margins before any perturbation. Choose their endpoints off Lambda using Section2.

The arcs can be made disjoint without losing the cover of Lambda by their flow saturations. Perturb the finite family into general position, relative to the already chosen boundary collars: pairwise intersections are transverse and finite, with no triple intersection or endpoint intersection. In a flow box at an intersection, one arc is t=0 and the other is t=h(s), with h' nonzero there. If their intersection belongs to Lambda, choose a nearby point of the first arc outside Lambda, possible by nowhere density, and make a small supported C1 perturbation of h which moves the intersection to that point. Finiteness permits disjoint supports and perturbations small enough to preserve transversality and the coverage margins. The same local operation applies to intersections with a fixed boundary arc; only the central arc is moved.

Every remaining intersection is outside the closed set Lambda. Remove small intervals around it on the intersecting arcs, disjoint from Lambda, and subdivide. No Lambda point is lost from their flow saturations: if a removed point flowed to a point of Lambda, invariance would put the removed point in Lambda. Choose all newly created endpoints off Lambda. The finite family T of compact transverse arcs is now pairwise disjoint. Let A=Lambda cap T, a compact set of zero flux length.

There is H<infinity such that an orbit of Lambda which stays outside the saddle blocks for time2H crosses one of the central or collar sections. To see this, use the finite cover at the midpoint of the time interval; the flow time from a covered point to its section has absolute value at most H. Entering a block crosses its incoming section, and leaving crosses its outgoing section. Consequently every a in A has a finite next return to T except possibly an incoming stable crossing. Conversely an incoming stable crossing has no next return, because its orbit stays inside that block forever. Let C be the subset of such crossings belonging to A. This set is finite, with at most two per saddle.

Every regular point of Lambda reaches the interior of T in finite positive OR negative time. Outside blocks this follows from the cover. In a block a nonstationary point either has a finite backward entrance or a finite forward exit, by the saddle description. This signed-time version includes points on the stable and unstable manifolds.

Because T is a finite disjoint union of compact transverse arcs, there is h>0 such that consecutive intersections of any flow trajectory with T are separated by at least h. If no such h existed, a sequence of pairs and times tending to0 would have a common limit on one of the arcs by compactness and disjointness. A flow box there, including an endpoint if necessary, forbids a second intersection with that arc in a sufficiently small time. This proves the uniform lower bound independently of return-time upper bounds.

## 5. Finitely many first-return branches and their endpoints

For a in A minus C, the first return is a finite-time transverse intersection in the interior of a target arc. Its intermediate compact orbit segment has no other intersection with T. Flow-box transversality near the initial and terminal points and compact separation on the remaining segment therefore give a C1 first-return branch on a neighborhood of a. Shrink this neighborhood so every passage stays in V and its closure remains in a regular branch domain. The possible problem of an earlier hit at an endpoint is absent because the orbit of a lies in Lambda and all endpoints of T avoid Lambda.

For c in C, each punctured side of a sufficiently small incoming interval has its first return on the corresponding outgoing arc by the saddle passage in Section3. Its return time tends to infinity and its image tends to the unstable crossing u_plus or u_minus. These outgoing crossings need NOT belong to Lambda. Retaining them in the outgoing arcs is enough.

First select these finitely many one-sided saddle intervals, with their outer endpoints off A. Removing smaller neighborhoods of C leaves a compact subset of A, which has a finite cover by regular branch intervals with closures inside regular domains and endpoints off A. Together their domains and C contain a relative neighborhood of A in T. Overlaps can be merged when they describe the same first return, or left as a finite cover; no uniqueness of branch labels is needed. Write the branches as P_j:I_j to J_j. Each has a continuous extension to endpoints. At an ordinary endpoint this is a finite-time map; at c in C it is the saddle-passage limit.

By Section2 and the return-time lower bound, |P_j'|>=lambda:=exp(gamma h)>1. Each inverse g_j extends to the closed image interval and is lambda^-1 Lipschitz in flux coordinates. Furthermore

    g_j(A cap closure(J_j)) is contained in A.                 (1)

For an interior point or a finite-time endpoint, full backward invariance of Lambda gives (1). At an endpoint arising from infinite passage time the extended inverse is precisely c in C, already in A. The formula does not require the limiting outgoing separatrix to lie in Lambda. This endpoint distinction is necessary.

## 6. Contraction relative to A and the external-orbit contradiction

Place the finitely many flux-coordinate intervals comprising T on a real line separated by positive gaps. Let epsilon>0 be smaller than those gaps and than the positive distance to A of every endpoint of every J_j which lies outside A. There are finitely many such endpoints. If z belongs to J_j and dist(z,A)<epsilon, a nearest point of A can be chosen in closure(J_j). Indeed if a nearest point were beyond an endpoint e of J_j, then either e belongs to A and is closer, or

    dist(e,A)<=|e-a|<=|z-a|<epsilon,

contrary to the choice of epsilon. Using this nearest point and (1) gives

    dist(g_j(z),A)<=lambda^-1 dist(z,A).                      (2)

Suppose omega(y) contains a regular point x. By Section4, Phi_s(x) lies in the interior of T for some finite signed time s. A sequence of forward orbit points tending to x then crosses T near Phi_s(x), at times tending to infinity, by the local flow box. Negative s is harmless since these times eventually exceed |s|. Thus the orbit has infinitely many late intersections; list consecutive ones z_n.

Precompactness and omega(y) contained in Lambda imply dist(z_n,A) tends to0. The orbit can never enter Lambda at a finite time, because backward uniqueness from a point of Lambda would place y in Lambda. Hence all these distances are strictly positive and z_n never belongs to C. For sufficiently large n, z_n lies in one of the selected domains I_j, and its next hit is exactly z_(n+1)=P_j(z_n). Formula(2) gives

    0<dist(z_n,A)<=lambda^-1 dist(z_(n+1),A).

Iteration forces the positive distances to grow by at least lambda at every step, contradicting their convergence to0. Thus omega(y) has no regular point. The omega-limit set is nonempty, compact and connected: it is the intersection of the nested compact connected closures of forward orbit tails. Being contained in the finite set E, it is a single saddle. This proves the surface theorem without any genus restriction.

## 7. The invariant-measure replacement

Let D=div_nu0 X, continuous near Lambda. Invariant probabilities on the compact invariant set form a nonempty compact space. Their D-integrals attain a positive minimum b>0 by hypothesis. There is T0>0 such that every x in Lambda satisfies

    (1/T0) integral_0^T0 D(Phi_t x)dt>=b/2.

Otherwise choose counterexamples at arbitrarily large times; weak limits of their empirical probabilities are invariant, by the bounded endpoint error for continuous tests, and have D-integral at most b/2, a contradiction. Choose a C1 function F within b/8 of D near Lambda. On a neighborhood where the flow exists up to T0 set

    u(x)=(1/T0) integral_0^T0 (T0-t)F(Phi_t x)dt.

This is C1. Integration by parts gives Xu=-F+average_0^T0(F o Phi_t). Therefore the positive C1 density exp(u)nu0 has divergence

    D+Xu>=b/2-b/4=b/4 on Lambda,

and by continuity at least b/8 on a smaller neighborhood. Section1 now applies. Approximating D by F is essential because D itself is only continuous. At a zero of X, div_nu0 X=tr DX regardless of density. If all invariant probabilities are supported on the finitely many equilibria, the stated positive-trace special case follows.

## 8. Application to a bounded Euler vortex half-line

Let U in C2(R3;R3) and P in C1(R3) solve the rotating profile equation

    ((1-c)I+omega J)U+DU((cI-omega J)x+U)+grad P=0, div U=0,

where 0<c<1/2, omega is any finite real number, Jx=(-x2,x1,0), and U is uniformly sublinear. Assume U.curl U=0 everywhere. Put a=1-2c, kappa=1+c, B=(cI-omega J)x+U, W=curl U, H=P+|U|^2/2+((cI-omega J)x).U and g=U.B. Let p be a vortical carrier equilibrium with covector rate rho, DB(p)^T U(p)=rho U(p), and suppose rho<=-2a. Consider a forward-bounded half of the W-line through p, parameterized as an external forward B-orbit L_plus, and let K be its omega-limit set.

The hypotheses and prior conclusions used here are A540-A543 and A572. They give on K

    W0, H=H(p), g0, grad H=-aU!=0,
    grad g=-(rho/a)grad H, DB(q)^T U(q)=rho U(q) at equilibria q.

Every invariant probability on K is supported on its carrier equilibria. Assume additionally DW(q)!=0 at EVERY equilibrium q in K and rho!=-kappa. A572 gives a finite equilibrium set, all first-family hyperbolic points, with rho<-kappa. The two eigenvalues in U(q)^perp are rho+kappa<0 and -a-2rho>0; their sum is3c-rho.

Choose bounded ambient neighborhoods N1,N0 with K in N1, closure(N1) contained in N0 and closure(N0) contained in {grad H!=0}. The profile equation makes grad P C1, hence P and H are C2. Then S=N0 cap {H=H(p)} is a C2 surface. The late half-line lies in N1; its closure lies in the compact set closure(N1) cap {H=H(p)}, which is a subset of S. Thus the relevant forward orbit is precompact in the SURFACE, not merely in ambient space.

On a neighborhood of S set N=grad H/|grad H|^2, f=BH=-ag and X=B-fN. This is C1 and XH=0 identically. On K and L_plus it equals B, so K is invariant for X and the half-line is its external orbit, since W is nonzero on that orbit and zero on K. At an equilibrium q and a tangent vector v perpendicular to U(q),

    DX(q)v=DB(q)v-(grad H(q).DB(q)v)N(q)=DB(q)v,

because DB(q)^T U(q)=rho U(q). Thus the surface equilibria are precisely the finite hyperbolic saddles just listed.

The surface area form is nu0=(i_N vol)|S=dA/|grad H|. In coordinates with first coordinate H, ambient volume is dH wedge nu0 and X has identically zero H-component. Hence surface divergence relative to nu0 equals ambient divergence of X. On K,

    div_nu0 X=3c-Nf-f div N=3c-rho>0,

using f0 and df=-a dg=rho dH. Continuity gives uniform positive expansion on a neighborhood of K in S. This calculation requires only the identities on K, not an ambient rank identity in a full neighborhood. Alternatively Section7 applies using A542 and the positive saddle traces.

The surface theorem proves K={q} and L_plus tends to q. The independent endpoint result A543 then gives

    -2(1+c)<=rho<-(1+c).

This removes the earlier planar-neighborhood assumption from A573. It does not remove DW(q)!=0 at equilibria, the exceptional rho=-(1+c), or the possible heteroclinic connection itself. If flat equilibria are nonetheless known to form a finite hyperbolic surface-saddle set, the surface collapse still applies, but the nonflat endpoint interval does not follow without its separate hypotheses. No full-profile nonexistence claim is made.

## 9. A limited observation about a torus source and saddle

For completeness the source's comparison can be made precise without a classification of Cherry flows. Suppose a C1 torus flow has exactly a hyperbolic source p and a hyperbolic saddle q, both of positive trace. Let U_source be the unstable basin of p and Q its invariant compact complement. Every invariant probability gives U_source minus {p} measure0. Indeed a small source neighborhood has a backward trapping property; a fundamental region between it and a fixed positive-time image has pairwise disjoint time translates, each of equal measure. Countably many translates cover the basin minus the source, so that measure is0.

If Q carried only the saddle atom, every invariant probability on the entire torus would be a convex combination of the source and saddle atoms. Section7 would construct an everywhere positive-divergence density on the compact torus. Integrating its divergence, or applying the global change-of-variables formula, is impossible. Thus Q carries a nonatomic invariant probability after removing its possible saddle atom. This observation is confined to this definition of Q and these assumptions. It is not used in the surface theorem or Euler application and is not a statement about every object called a Cherry flow.
