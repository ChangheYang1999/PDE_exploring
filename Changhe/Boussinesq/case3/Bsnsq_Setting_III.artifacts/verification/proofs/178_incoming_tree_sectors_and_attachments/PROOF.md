# The compact tree, incoming sectors and flat attachments at beta two

Status: CONFIRMED after independent full derivation, exact controls, actual Opus5.5 review and focused follow-up. This extends packet177 under its explicitly retained finiteness premises. It is not a full B2 exclusion.

## Exact hypotheses and conclusions

Let smooth fields W,Theta,Omega on R2 satisfy, in fixed physical coordinates,

    div W=4, Omega=-curl W,
    W.grad Theta=0, (W.grad+1)Omega=Theta_x,
    W(X)=2X+o(|X|) as |X| tends to infinity.             (1)

Assume the connected zero component gamma is a compact smooth embedded arc with the regular normal dynamics specified in packet177. Its two endpoints are nonaccumulating and incoming. All other zeros of W are isolated. At each endpoint p, DW(p)=4n tensor n, and Theta-Theta(p) and Omega are flat to all orders. These are the hypotheses of177 specialized to incoming endpoints. A source here means a zero q for which an entire neighborhood is contained in its backward basin, including degenerate sources with both center sides outgoing. Let phi_t be the complete flow, Z its zero set, B(q)={X:phi_(-t)X tends to q}, and

    K={X: {phi_t X:t>=0} is bounded}.                  (2)

For a fixed endpoint p put L=Theta(p). Let C be its strong unstable curve and eta its incoming exterior center orbit. The exterior side of C means the side opposite gamma. All references to neighborhoods and sectors below concern sufficiently small neighborhoods of p.

(A) Z minus gamma is finite. Every backward orbit converges to a single zero. K is a compact connected finite embedded tree after subdividing gamma at its finitely many attachment points. It consists exactly of gamma, the exterior zeros and finitely many connecting orbits whose limits in both time directions are zeros. It contains no Jordan curve. Each connected tree of exterior vertices and exterior-to-exterior edges has exactly one connecting edge to gamma. Furthermore

    Theta(R2)=Theta(gamma).                            (3)

(B) The two open sectors between eta and the two branches of C each lie, near p, in the interior of B(q), for an exterior zero q that is a source or a zero of index0 with eigenvalues0,4. The two q values can be different, and neither need equal the backward limit of eta. Consequently Theta=L and Omega=0 on the exterior side and on C near p. The stronger basin statement, not just equality of field values, is asserted here.

(C) Theta-L does not vanish identically on any neighborhood of p. Equivalently, Theta cannot be constant on any nondegenerate terminal subarc of gamma ending at p.

(D) In fixed orthonormal tangent-normal coordinates (s,z) at p, with positive s pointing beyond gamma, there is no delta>0 such that W(0,z) is analytic for |z|<delta and Omega(s,z) is analytic in z on that same interval for every0<s<delta. One of the two sectors in(B) already gives the zero intervals used in this argument. Also C is not a regular analytic curve germ through p; at least one of its two branches fails to admit a regular analytic continuation through p. Replacing the W trace by U is equivalent when W-U is affine.

(E) Suppose in addition that every exterior zero is nondegenerate. At every attachment a in gamma all derivatives of Theta of positive order vanish. The proof below also gives flatness of Omega there. For the B2 component through0, assume its already established reflection invariance, its sole axis intersection0, DW(0)=diag(0,4), Theta_xx(0)=2a0!=0 and invariance of the x=0 axis. Then W has no other axis zero. Each open half-axis is a single orbit, with backward limit0 and forward escape to infinity.

Nondegeneracy in(E), isolated exterior zeros, and nonaccumulating incoming endpoints are additional restrictions. The result does not decide smooth accumulating endpoints, other nonisolated zero components, or the beta>2 problem.

## The finite compact tree

Packet177 proves completeness, boundedness of all backward orbits, finiteness of exterior zeros, convergence of every bounded semiorbit to one zero, at most two incoming branches at any exterior zero, at most one incoming branch at each incoming endpoint, and no nonstationary orbit with forward limit in the interior of gamma. It does so by a checked continuous-plane-flow theorem after collapsing gamma, an independent finite-incoming-edge count, exact local normal-form estimates, and an area argument excluding every invariant Jordan loop. These precise conclusions, rather than a general claim for arbitrarily many zero components, are used here.

Choose a closed disk D_R so large that X.W(X)>=|X|^2 on and outside its boundary. It is backward invariant. An orbit that crosses outward never returns and its radius thereafter grows at least exponentially; an orbit that starts outside also escapes forward. Therefore a forward orbit is bounded exactly when it remains in D_R for all positive times, and

    K=intersection over t>=0 of phi_(-t)(D_R).          (4)

The sets on the right are nonempty nested compact topological disks: each contains all zeros, and phi_(-t) is a plane homeomorphism. Thus K is compact and connected. Each regular point of K has a forward limit q in Z and lies on one of q's incoming branches. There are only finitely many such branches by177. Each of their backward limits exists, and each orbit together with its endpoint limits is a simple compact arc, since a repeated point would be periodic and equal forward and backward limits of one orbit would make a homoclinic loop. Two distinct connecting orbits with the same two endpoint limits would form a Jordan bigon and are excluded as well. Edges cannot cross away from zeros by uniqueness. Adding the compact arc gamma and subdividing it at the finitely many incidences gives a finite embedded graph with underlying set K.

A Jordan curve in this graph consists of edges and zero subarcs and is invariant. Its bounded complementary region would have invariant positive finite area, contradicting det Dphi_t=exp(4t), as in177. Hence the connected graph is a tree. In particular it has no undirected cycle, a stronger graph fact than merely having no directed cycle.

Remove gamma and the edges incident with it, retaining the exterior vertices and the closed edges joining exterior vertices. Each remaining connected component T is a finite compact tree. At least one edge joins it to gamma by connectedness of K. If two distinct joining edges existed, the unique path between their exterior endpoints in T, the joining edges, and the subarc between their endpoints in gamma would give a Jordan curve. This includes the case of equal endpoints in gamma. Thus exactly one edge attaches T to gamma. In particular the exterior tree containing the backward limit of eta has eta as its unique attachment, admits no other edge from gamma, and is distinct from the exterior tree attached to the other endpoint.

Thermal transport and continuity make Theta constant along every edge, including its endpoints. Every exterior vertex therefore has the Theta value of its component's unique attachment to gamma. For any X, convergence of its backward orbit and transport give Theta(X)=Theta(alpha(X)). The alpha-limit is one zero, so its value belongs to Theta(gamma). The reverse inclusion is immediate. This proves(A).

## A quantitative local passage to a half-section

We give the local step needed for individual sectors. At an isolated singular zero, simultaneously straighten a finite C4 center manifold and the strong unstable curve as in177. The field has

    u'=g(u)+uvB(u,v), v'=vD(u,v),
    D>2, |B|<=M, g(0)=g'(0)=0,                       (5)

with g nonzero on each punctured center side. At an endpoint g=0 on the arc side and g<0 on the positive exterior side. The local proofs below use only bounded continuous coefficients and finite C1 estimates, so finite C4 coordinates suffice.

On a center side with u g(u)<0, backward time T gives decreasing |v| and the integrating factor

    h(T)=|u(T)| exp(int_0^T vB dt),
    h'=-sign(u)g(u) exp(int_0^T vB dt)>0.             (6)

The integral has absolute value at most M|v(0)|/2. As proved in177, each point on this side reaches a fixed section |u|=delta in finite backward time; otherwise h and |u| would have positive finite limits, contradicting the strict positive lower bound for h' at the limiting u. It cannot exit across u=0 or |v|=epsilon. Shrink epsilon at the section so that the incoming center drift still crosses it strictly. Sign(v) is preserved.

Let C0 bound |g(u)/u|+epsilon M in the rectangle. Since g is C1 and g(0)=0, C0 is finite, even when g is flat. Before reaching the section,

    |d log|u|/dT|<=C0,
    T_exit >= log(delta/|u(0)|)/C0,
    |v_exit|<=|v(0)| exp(-2 T_exit).                 (7)

Thus, for points on a fixed outgoing transverse section |v|=epsilon approaching its strong-unstable basepoint u=0 from the given side, the backward passage to |u|=delta extends continuously to the incoming-branch basepoint v=0. This is only continuity and a lower exit-time bound. No uniform upper exit time or analytic transition map is claimed.

On a center side with u g(u)>0,177's backward-invariant weighted neighborhood

    |v|<epsilon, |u|exp(k|v|)<delta, k>M/2

has backward limit q throughout its open half. Hence this half lies in int B(q). If both sides have this sign, q is a source. If only one does, q has one incoming side and one outgoing side and index0: along v=0 the signs of g on the two sides agree, while v has positive derivative; the usual local degree, or the checked index formula in174, gives0. If both sides are incoming, q is the degenerate saddle case and neither half is an open basin of q.

At a hyperbolic saddle, straightening its stable and unstable axes gives u'=uA, v'=vD with A<-a<0 and D>d>0. The same passage statement follows from backward growth of |u| and decay of |v|, with2 replaced by d in(7). At a nondegenerate source a whole neighborhood lies in B(q). Coupling in(1) makes the derivative at every nondegenerate zero symmetric, as177 proves, so no other nondegenerate type occurs. Ordinary finite-time passage along a compact regular orbit segment is a diffeomorphism between short transverse sections, taking each chosen half to a chosen half and extending continuously to the basepoint.

## Backward passage of the two endpoint sectors

The backward limit q0 of eta is an exterior zero, since an orbit from gamma to p joined to the gamma subarc would form an invariant Jordan loop. Fix a short transverse section J through eta. Choose one half of J. Follow eta backward into a local neighborhood of q0.

If q0 is a source, the entire sufficiently short half-section lies in its open basin. If eta approaches q0 backward within an outgoing center half of a singular zero, that orbit is already in the open one-sided basin, so a whole short transverse neighborhood is in that basin. If eta is a strong unstable branch and the chosen adjacent side is an outgoing center half, the chosen half-section lies in that same open basin. This final case can have index0. These are terminal cases.

In every remaining case, the chosen side passes backward near q0 to one of its incoming branches by(6)-(7) or the hyperbolic analogue. The sign of u selects the incoming center side in(5), and the corresponding sign selects the stable branch at a hyperbolic saddle. Finite-time flow boxes preserve each selected half-section. The half-section passage is continuous to the incoming-branch basepoint. Follow that incoming branch backward to its zero q1 and repeat the same classification. Every step adds an incoming edge to a directed chain ending at eta and p. No qj can lie on gamma, because the chain and the gamma subarc would give a loop. No exterior vertex can repeat, because K is a tree. The finite set of exterior zeros therefore makes this procedure terminate at a source or an outgoing center side of an index0 zero. The terminal open basin contains a short half-section. The finite composition of continuous half-section maps pulls it back to a short half of J, still contained in the interior of that same basin. We do not assert the same terminal zero for the other half of J.

At p use(5) with gamma on u<=0,v=0, C on u=0, eta on u>0,v=0 and g<0 for u>0. Choose J at u=delta. After shortening J so that each of its halves has the preceding basin property, every point with0<u<delta and small positive v reaches its corresponding half of J in backward time; |v_exit|<=|v(0)| suffices to keep it in the chosen half. The same holds for negative v. A small physical disk has its two sectors in these coordinate rectangles. This proves the individual basin statement in(B).

On an open backward basin Theta equals its zero's value by transport and continuity. Hence Theta_x=0 there. Along each backward orbit Omega is bounded and

    Omega(X)=exp(-T)Omega(phi_(-T)X)

forces Omega=0. Each sector accumulates at p, so its thermal constant is L. Continuity supplies the same equalities on eta and C. Since div W=4 and curl W=0, W and the B2 velocity U are harmonic componentwise on this open exterior side. This proves all of(B).

## Terminal temperature values and analyticity

Suppose Theta is L on a terminal subarc of gamma. For u<0 in the endpoint chart, g=0 and backward time gives v(T) tending to0 and

    u(T)=u(0)exp(-int_0^T vB dt).

The integral is absolutely bounded by M|v(0)|/2. Thus the limit u_infinity exists, has the same negative sign and remains in the prescribed terminal interval if the initial neighborhood is small enough. Every such point has its backward limit on that subarc. Thermal transport makes Theta=L on the whole local arc side. Part(B) gives the same on the exterior side and smoothness across C gives it in a full neighborhood of p. Conversely a constant neighborhood restricts to a constant terminal subarc.

In that situation, backward orbits on the arc side stay within a slightly larger constant neighborhood if the starting disk is small enough, by the estimates just given. Variation of constants in the vorticity equation yields Omega=0 on that side. Part(B) gives Omega=0 on the other side, so Omega=0 near p. Both components of W are harmonic, hence real analytic near p. Its analytic normal nullcline has a reduced tangential component with a flat jet, inherited from gamma. That component vanishes identically and extends the zero arc beyond p, contrary to gamma being the entire connected component. This proves(C).

For(D), eta is a graph z=h(s) with h(s) tending to0. A small fixed positive-s line intersects either chosen sector in a nonempty open interval adjacent to h(s). On it Omega=0. Real analyticity in z on the stipulated common connected interval (-delta,delta) forces Omega=0 along the whole interval. Thus Omega vanishes on a positive half-rectangle. An analytic value trace for W extends each harmonic component across s=0 by subtracting an analytic harmonic extension of that trace and oddly reflecting the zero-trace difference. The full smooth jet and the implicit normal-nullcline jet match those of the extension; the flat tangential reduction again extends the zero component. All reflection details, including the corresponding Neumann argument for analytic C, are proved explicitly in177. They apply with only this one sector for the transverse-analyticity assertion.

The strong unstable curve C itself is C-infinity, by the smooth strong unstable theorem (also the endpoint fiber construction in173); this property is not being inferred from the finite C4 chart. If both branches of C admit regular analytic continuations through p, use the normal coordinate z as parameter, since C is transverse to the endpoint tangent. Their analytic graph functions have the same jets, the jets of the actual smooth C. Analytic uniqueness makes their germs equal, so they form one regular analytic curve containing C. This contradicts177(B). Conversely an analytic whole germ extends each branch. This proves the stated equivalence and(D); it does not say that both separate branches fail to extend.

## Flatness through a hyperbolic tree

Assume now that all exterior zeros are nondegenerate. Each is a source or a saddle. Every saddle has its two stable branches in K, since each converges forward to that saddle and has a bounded full negative semiorbit. The backward boundedness follows from the explicit outward inequality X.W(X)>=|X|^2 used above; no stronger interpretation of the asymptotic is being assumed. Hence its degree in the finite graph K is at least2. For a given exterior tree T with its unique attaching edge to gamma, add the attachment point as one additional leaf. This finite tree has another leaf, whose vertex is exterior and has degree1 in K. It must be a source. This also covers a component T consisting of just one vertex.

At such a source q, a sufficiently small neighborhood stays near q under backward time. Transport and continuity give Theta=Theta(q) there. Thus Theta_x=0, and Omega(X)=exp(-T)Omega(phi_(-T)X) with a bounded backward value gives Omega=0 there. Thus all derivatives of Theta-Theta(q) and Omega vanish at q. We justify propagation of flat jets in both time directions, which is needed for an undirected path in T, not only an upstream chain.

Let q be any hyperbolic zero and eta0 a connecting orbit with q as either endpoint. If X is on eta0, then for one sign sigma in {+1,-1},

    |phi_(sigma T)X-q|<=C exp(-aT), T>=0.             (8)

For every positive derivative order m, the derivatives of phi_(sigma T) at X up to order m grow at most C_m exp(K_m T). Products of at most m such derivatives therefore have a bound C exp(m K_m T); the undifferentiated case uses no such factor. This follows inductively from the variational equations along the compact orbit closure, on which all derivatives of the smooth field W are bounded. Constants and rates may depend on m and X; no uniform estimate over an entire basin is asserted.

If Theta-Theta(q) is flat at q, Taylor's theorem bounds each derivative of any prescribed order by C_N |Y-q|^N near q for every N. Differentiating Theta=Theta composed with phi_(sigma T), using the chain rule and(8), bounds every fixed derivative of Theta-Theta(q) at X by C exp((m K_m-aN)T) for m>=1, and by C exp(-aNT) for m=0. Choosing N sufficiently large and then sending T to infinity makes it zero. Thus the full ambient jet is flat at every point of eta0. Continuity transfers flatness to its other endpoint. This argument works for stable and unstable edges equally.

For completeness Omega is also flat on eta0 when flat at q. The just established thermal flatness makes all derivatives of Theta_x vanish at every point along eta0. Differentiate the finite-time variation-of-constants formula at X. Every derivative of its source integral vanishes because every such jet at phi_t X vanishes. If sigma=-1 the remaining term is exp(-T) times derivatives of Omega composed with phi_(-T); if sigma=+1 it is exp(T) times derivatives of Omega composed with phi_T. For derivative order m>=1 the absolute bound is C exp((1+m K_m-aN)T), and for m=0 it is C exp((1-aN)T). Arbitrarily high order flatness at q and(8) dominate these factors. Hence all Omega derivatives vanish at X and then at its other endpoint. This step uses hyperbolic exponential convergence; it is not exported to a flat degenerate exterior zero.

Starting from the source leaf, propagate along the unique undirected path in T to the attaching edge and then to its endpoint a in gamma. At each intermediate exterior vertex hyperbolicity permits the next step. Continuity at a supplies flatness there without requiring a to be hyperbolic. Values of Theta are constant along the whole tree, so the flat scalar is Theta-Theta(a). This proves(E)'s attachment assertion.

Finally impose the stated B2 axis hypotheses. If another axis zero existed, gamma's sole axis intersection0 makes it exterior. There are only finitely many exterior zeros. On one of the two half-axes take the first zero q encountered from0. The scalar axial field b(y)=W2(0,y) satisfies b(y)=4y+O(y^2), so has the sign of y between0 and q. The intervening axis interval is an orbit from0 to q, is forward bounded and belongs to K. Thus0 is an attachment point, forcing Theta_xx(0)=0, a contradiction. Hence b(y) is nonzero for y!=0 and has sign(y) everywhere. Each half-axis is one complete orbit; its backward limit is0, and its forward orbit escapes, since b(y)=2y+o(|y|) for large |y|. This proves the rest of(E).

## Dependencies and limits

This proof uses the fully stated and source-audited177 global convergence lemma and local normal form,174's index convention, elementary finite embedded graph topology, completeness and variational equations, exact scalar transport, ordinary hyperbolic stable/unstable convergence, and177's explicit harmonic reflections. The B2 axis conclusion uses the previously proved geometry of the center component, rather than deriving it from arbitrary fields satisfying(1). No Poisson wall, harmonic gauge freedom or artificial far-field boundary is introduced. The conditional conclusions provide neither a numerical candidate nor a full nonexistence endpoint.

Written UTC 2026-10-21T15:16:05.140297+00:00, before new verification controls.

Audit completed UTC 2026-10-21T15:24:02.157619+00:00.
