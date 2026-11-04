# External expanding surface limits with nonisolated zeros

Status: CONFIRMED A657-A659 for the corrected surface and endpoint theorems; REFUTED A656 and A660 for the two specified source assertions. The complete independent reconstruction and both referee proofs have been postread. No global Euler profile is excluded by this result alone.

## 1. Exact surface statement and dependencies

Let M be a C2 surface without boundary near the sets below, X a C1 vector field, and Phi its local flow. Let y0 have a forward-complete orbit with compact closure in M, let K=omega(y0), and assume y0 is not in K. Suppose a positive C1 area density nu on a neighborhood V of K satisfies

    div_nu X >= gamma > 0 on V.                            (1)

At every equilibrium q in K assume the two eigenvalues of DX(q) are real and obey

    lambda(q)<=0<eta(q).                                   (2)

Then K consists of one equilibrium. In particular its equilibrium subset E is finite. No isolation among the surface zeros, finite-order center zero, periodic-orbit exclusion, invariant-probability classification, or total-disconnectedness assumption is needed. No assertion about an orbit starting in K is made.

The dependencies are C1 flow-box theory, uniqueness and differentiable dependence for the original C1 field, the local C1 center-manifold theorem with its small complete-orbit property, and the hyperbolic and isolated semihyperbolic blocks independently checked in A614/A629. An equilibrium has a complete local orbit, so all sufficiently nearby zeros lie on the chosen center curve. The new uniform unstable-graph construction and nonisolated half-block argument are proved below. The finite-section proof is also included.

All compact invariance here means existence for all real times within the compact set. Precompactness of the forward orbit gives this property for K. The density can be nonorientable; all transverse calculations use absolute flux coordinates.

## 2. The proposed vertical-strip estimate is false

Set f(s)=s2(1-s)2/100 and, near [-2,2] times [-1,1],

    s'=f(s)+r, r'=r[2-f'(s)].                              (3)

The field is smooth, has divergence2, and has zeros(0,0),(1,0), each with eigenvalues0,2. Since |f'|<=3/5 on |s|<=2, its transverse coefficient lies between1 and3. Start at (delta/10,delta), 0<delta<1. In backward time tau, r decreases and r(tau)>=delta exp(-3tau), while ds/dtau=-f(s)-r<=-r. Unless s=-1 is reached earlier, at tau1/3 one has

    s<=delta/10-(delta/3)(1-exp(-1))<-delta/10.

Thereafter f has a positive minimum on [-1,-delta/10], so s reaches -1 in finite further backward time. No horizontal exit occurs because r decreases. Thus arbitrarily small transverse perturbations above the bounded gap(0,1) escape distance1 from its closure. An enlargement tending to0 uniformly over the raw center gap is impossible. This refutes Claim A, not the surface theorem.

## 3. Uniform invariant curves through every nearby zero

At a semihyperbolic q use a C1 center curve, with graph coordinates(s,r) retaining an original linear coordinate s along it. The original C1 field, invariance of the graph and the fundamental theorem of calculus give

    s'=F(s)+r A(s,r), r'=r C(s,r),
    |F'|<=ell<b<=C<=B, |A|<=M0.                            (4)

F is C1, A,C are continuous, and F'(q)=0. Shrinking makes the displayed bounds hold. All original zeros near q lie on r0, where they are exactly the zeros of F. We never infer C1 regularity of the transformed field from a C1 coordinate change.

Choose L>M0/(b-ell), a smaller closed center interval J, and a common sufficiently small height delta. For every zero z in J construct an invariant graph s=h_z(r), |r|<=delta, with

    h_z(0)=z, |h_z(r)-z|<=L|r|.                            (5)

For each sign sigma start the original flow at(z,sigma epsilon). Put rho=|r|. Because rho'=rho C>0, rho is a parameter. On the boundaries of |s-z|<=Lrho the forward vector field points inward: the upper derivative is at most (ell L+M0-Lb)rho<0 and the lower one is at least its positive opposite. The common height ensures these cones remain in the larger chart. The orbit reaches rho=delta, and its graph has derivative magnitude at most (ell L+M0)/b<L.

Extend it constantly as z below rho=epsilon. Arzela-Ascoli gives a uniformly convergent subsequence as epsilon decreases to0. Pass the graph's integral equation on every compact rho interval away from0. Its limit is C1 there and is an original orbit when parameterized by rho'=rho C. Negative time is infinite as rho tends to0, and (5) gives convergence to(z,0), with rho(-t)<=rho(0)exp(-bt).

The positive and negative graphs fit C1 at0. Put alpha=1-F'(z)/C(z,0)>0, beta=A(z,0)/C(z,0), and u(r)=(h_z(r)-z)/r. The bounded function u satisfies

    r u'=-alpha u+beta+o(1).

For v(rho)=u(sigma rho), boundedness kills the integration constant, so

    v(rho)=rho^(-alpha) integral_0^rho t^(alpha-1)[beta+o(1)]dt
            ->beta/alpha.

The graph equation gives the same limit for h_z', namely A(z,0)/[C(z,0)-F'(z)]. Hence (5) is a C1 invariant graph through z. Distinct graphs cannot intersect: uniqueness of the original flow would identify their negative orbits and their equilibrium limits. Their order therefore agrees with that of their center zeros.

## 4. Backward strips and finiteness

For zeros a0<a1 in J define

    D={|r|<=delta, h_(a0)(r)<=s<=h_(a1)(r)}.                (6)

It is compact and backward invariant. The side curves are invariant and cannot be crossed; the horizontal boundaries point outward forward. Compact containment provides continuation for every negative time. Moreover its negative orbits satisfy

    |r(-t)|<=|r(0)|exp(-bt),
    a0-L|r(0)|exp(-bt)<=s(-t)<=a1+L|r(0)|exp(-bt).

Choose the entire chart disjoint from y0, possible because q lies in K and y0 does not. If the forward orbit ever met D, its unique negative orbit would put y0 in D, a contradiction. Thus the orbit misses D and K misses its interior.

Any equilibrium e in K whose center coordinate lies strictly between two zeros of F would be in that interior. Consequently the equilibria of K in J are among the minimum and maximum of its compact zero set. There are at most two. Each semihyperbolic point is therefore isolated relative to E. Hyperbolic points are isolated surface zeros by the inverse function theorem. E is closed in compact K, so it is finite: an infinite E would have an accumulation point in E. If E is empty, the later finite-section proof applies with no blocks and yields a contradiction.

This finiteness uses only (2), the original flow, and the external orbit. It does not use (1). Raw vertical-coordinate claims are not substituted for (6): the boundaries can differ from s=a_i by order |r|. At a nonextreme zero, however, a full neighborhood lies inside a strip, so even visits with s equal exactly to that zero are excluded.

## 5. The active side of a nonisolated surface zero

Let q in E be nonisolated among ALL surface zeros. It is semihyperbolic. Section4 excludes zeros on both sides of q. Reverse s if necessary so the other zeros lie on the left, q0, and F has no zero on(0,h]. Choose one left zero a0 and use its strip with q. Straighten h_0 by x=s-h_0(r). The invariant lines are now x0 and r0. The center equation remains x'=F(x), and r'=r Ctilde with b<=Ctilde<=B.

Near q the region x<0 lies strictly inside the strip. Therefore K lies in x>=0 locally, while the external orbit lies strictly in x>0 on every visit. The boundary x0 itself is also forbidden to the external orbit, since its full negative orbit stays in the strip.

The sign of F on(0,h] is negative. If positive, choose eta small so x=h is outward in forward time. Together with the outward r=+-eta edges and invariant x0, this makes the half-rectangle0<=x<=h,|r|<=eta backward invariant and disjoint from y0. Accumulation at q from x>0 would force an orbit visit, a contradiction. Thus F<0 on the active side. It is zero-free and center-attracting. A repelling side at an isolated semihyperbolic point is excluded by the same argument; the remaining ordinary blocks are those of A629.

## 6. Passages through a half-block

Take Bplus={0<=x<=h,|r|<=eta} with x=h incoming and r=+-eta outgoing. An entering point(h,r0),0<|r0|<eta, cannot cross x0, leave through the incoming side or change the sign of r. It exits through |r|=eta in time T with

    B^(-1)log(eta/|r0|)<=T<=b^(-1)log(eta/|r0|).           (7)

The only incoming point with infinite passage is c0=(h,0), whose center orbit decreases to q. Nonvanishing F prevents a positive limiting center coordinate, and uniqueness prevents reaching q at finite time.

On each punctured half incoming interval the original flow gives a C1 passage map with nonzero derivative. The exit x-coordinate lies in(0,h); it is strictly monotone and has one endpoint limit as r0 tends to0. As |r0| increases to eta, (7) makes T tend to0, so the exit tends to the corner x=h. Strict monotonicity makes the other endpoint limit strictly less than h. The inverse passage extends continuously there by mapping it to c0.

Only q has a complete orbit in Bplus: nonzero r exits forward, and positive x with r0 exits backward through x=h. Points on x0 with r nonzero also exit forward. A point of K may lie on this invariant edge. Extend each outgoing horizontal transversal slightly across x0 into x<0, where r' is still nonzero and the new part misses K. Thus such a crossing is in the interior of a section, not an artificial endpoint.

One may thicken the half-block slightly into x<0 to get an ambient neighborhood of q. This added part can contain zeros outside K. It contains neither K nor any visiting external orbit. The incoming singular branches above stay wholly on the active side. These are precisely the required local block properties; a stronger assertion that the thickened block has no other complete orbit is neither true nor used.

## 7. Finitely many sections and return branches

Take disjoint blocks about the finite E, inside V: ordinary saddle/isolated semihyperbolic blocks and the half-blocks just proved. By invariance and (1),

    nu(K)>=exp(gamma t)nu(K), t>0,

so nu(K)=0. In a flow box, positive flux measure of K on a transversal would give positive area by a short flow saturation within K. Hence all its transverse intersections have zero flux measure and are nowhere dense. Choose block corners and section endpoints outside K. The choices of width/height giving a corner in K form area-null subsets of the parameter rectangles; finitely many can be avoided. The added-side half-block corners already miss K.

Cover the compact regular remainder of K outside the block interiors by finitely many flow boxes with margins. Add their central transversals and block-boundary collars. Perturb the finite arcs to transverse finite intersections. At an intersection in K, in flow coordinates one arc is t0 and another t=g(s) with g' nonzero. Move its single crossing a short distance to a point outside K, using the dense transverse complement, while keeping the coverage margins. Delete small intervals around the resulting intersections, all disjoint from K. This loses no K point from flow saturations, because any point flowing into K belongs to K. Subdivide to obtain a finite pairwise disjoint union T of compact transversals with endpoints outside K.

Let A0=K intersect T. Every regular point of K has a finite positive OR negative crossing of the interior of T. Inside blocks use entry or exit, and outside use the finite flow-box cover. The time coordinates of this cover are bounded by some H; a K orbit segment of length2H outside blocks must cross a central section by considering its midpoint. Each point of A0 has a next finite section crossing except the finite set Cstar of incoming stable/center crossings converging to equilibria. Each new half-block contributes at most one.

For a in A0 minus Cstar, compactness of its intervening orbit segment, endpoint avoidance and transversality give an ordinary C1 first-return branch on a neighborhood. Shrink it to keep the trajectory in V. At c in Cstar, the two punctured incoming sides have the block passages above, with unique limiting images and inverse extensions sending those limits to c. The incoming interval stays on the zero-free side even when the surface zero is nonisolated.

Choose these finitely many singular neighborhoods first. The remaining compact part of A0 has a finite regular-branch cover. Endpoints can be chosen outside A0. We obtain finitely many first-return branches P_j:I_j to J_j whose domains together with Cstar cover a relative neighborhood of A0, with continuous inverse extensions g_j on closure(J_j) and

    g_j(A0 intersect closure(J_j)) subset A0.               (8)

At ordinary endpoints this is finite-time invariance. At a singular endpoint its image under the inverse is c in Cstar subset A0, even if that outgoing endpoint itself is outside A0. Overlapping branch domains cause no issue: their first returns coincide there.

## 8. Flux expansion excludes regular limit points

Consecutive crossings of T have a common positive minimum time hstar. Otherwise compactness and disjointness give two crossings tending to the same point of one arc in times tending to0, contradicting its local flow box, including at an endpoint.

For beta=i_X nu, a variable-time passage satisfies

    P_j^*|beta|=exp(integral_0^T div_nu X(Phi_t x)dt)|beta|.

The variable time contributes a multiple of X, annihilated by beta. In flux coordinates |P_j'|>=exp(gamma hstar), so its inverse, including its continuous endpoints, has Lipschitz constant theta=exp(-gamma hstar)<1.

Embed the finite section components as real intervals with positive gaps. Choose epsilon below these gaps and below every positive distance from a selected image endpoint to A0. If z in J_j has distance to A0 below epsilon, a nearest A0 point can be taken in closure(J_j). Otherwise an intervening endpoint either belongs to A0 and is closer, or has positive distance to A0 below epsilon, contradicting the choice. By (8),

    dist(g_j(z),A0)<=theta dist(z,A0).                      (9)

If K contains a regular point, external accumulation there and persistence of its finite signed-time section crossing give infinitely many late successive intersections z_n with T. Compactness gives dist(z_n,A0)->0. Those distances are positive because any actual intersection with K would put y0 in K by uniqueness and backward invariance. Eventually every z_n lies in a selected branch domain; it cannot equal a point of Cstar subset K. Its next return is z_(n+1), so (9) gives

    0<dist(z_n,A0)<=theta dist(z_(n+1),A0).

Iteration contradicts convergence to0. Thus K has no regular point. The compact closures of forward orbit tails are nested, nonempty and connected; their intersection K is connected. As K is now contained in finite E, it is a singleton. Precompactness then gives actual convergence of the external orbit to that equilibrium.

## 9. Bounded Euler vortex lines and exact scope

Use the bounded W1 data from A540-A542 and Section1 of in the team records. Explicitly, U in C2 and P in C1 solve the rotating Euler profile equation, are globally helicity-free with U uniformly sublinear, 2/5<c<1/2 and arbitrary finite omega. Put a=1-2c,kappa=1+c,B=(cI-omega J)x+U,Omega=curl U,H=P+|U|2/2+((cI-omega J)x).U,g=U.B. A vortical carrier equilibrium p has normal covector rate rho<=-a. A forward-bounded half of its vortex line is a nonstationary forward B orbit y(t), with

    Omega(y(t))=alpha0 exp(-kappa t)B(y(t)), alpha0!=0.

Its compact limit K satisfies Omega0,g0,dg=-(rho/a)dH and grad H=-aU!=0. At equilibria, DB(q)^T U(q)=rho U(q), and the two level eigenvalues satisfy lambda<=0<eta,lambda+eta=3c-rho. These are the already proved structural inputs, not conclusions for every arbitrary profile orbit.

Choose nested bounded neighborhoods of K whose closures lie in grad H!=0. The late orbit is precompact in the resulting C2 regular surface H=H(p), not only in ambient space. Set N=grad H/|grad H|2,f=BH=-ag,X=B-fN. Then X is C1, tangent to the surface, and equals B on K and the late orbit. The density nu=(i_N volume) restricted to the surface is positive C1. In coordinates with H first,

    div_nu X=3c-Nf-f div N=3c-rho=:d>0 on K.

Continuity supplies div_nu X>=d/2 on a smaller neighborhood. It does NOT supply equality d there. At an equilibrium, df=rho dH and DB^T U=rho U, so DX restricted to the tangent plane equals DB there. Its eigenvalues obey (2). The orbit is external because Omega is nonzero on it and zero on K. Sections1-8 apply with gamma=d/2. Thus K={q}, q is an irrotational carrier equilibrium with U(q)!=0 and the same rho, and the bounded half-line converges to q.

This removes the finite-equilibrium and surface-isolation premises from the bounded W1 collapse. No far-field derivative, tail density, A2, nonflatness, or symmetry is added. For the selected lower-window witness rho<=-2a, A630 gives lambda>=-kappa at any hyperbolic endpoint and |Omega| comparable to distance^(1-kappa/lambda). A631 makes an endpoint at rho=-kappa first-order flat. A nonflat endpoint is of the first A469 family and has -2kappa<=rho<-kappa. Smooth integer order remains the order along its stable curve. The connection itself is not excluded.

The source's endpoint clause is stated even at rho=-a, whereas A630 was recorded with rho<-a. Section10 below treats that boundary separately rather than silently enlarging the cited theorem.

## 10. Boundary extension of the hyperbolic endpoint estimate

At rho=-a, retain an actual convergent endpoint with level eigenvalues lambda<0<eta. Then d=kappa and mu=d-kappa=0. The construction in A630 of a C2 local level graph, its C2 tangential-component field Y, a C2 stream function psi with psi(q)=0 and dpsi=i_Omega nu, and the connected vortical component D containing the stable branch is unchanged. On D, Y=B, div_nu Y=d, and

    Ypsi=mu psi=0.

The constant is zero because psi is zero along the stable orbit, where Omega is parallel to B, and that orbit tends to q. Nearby off-stable trajectories remain in D until exiting a small saddle rectangle. Their exit limits lie on the unstable branch, and each fixed backward portion of that branch lies in closure D and is a B orbit.

The unstable eigenvalue eta is the largest ambient eigenvalue because rho<0 and lambda<0. The Cauchy law and Lipschitz Omega, exactly as at A630, give Omega=0 at every point of this unstable branch: the bound is C exp((-kappa+2epsilon)T) as the negative time T increases. Therefore dpsi=0 along the WHOLE branch. Continuity to q gives psi=0 there. This replaces the earlier use of mu>0; dividing by mu would be invalid.

In straightened C2 saddle coordinates, passage to z=delta has |s(T)|<=C exp((lambda+epsilon)T) and z0>=delta exp(-(eta+epsilon)T). At the limiting unstable exit, psi=dpsi=0, so the transported Taylor estimate is

    |psi(s0,z0)|/z0 <=C exp((-mu+2lambda+eta+3epsilon)T)
                     =C exp((lambda+kappa+3epsilon)T).

If lambda<-kappa this tends to0, contradicting nonzero Omega on the stable orbit. Hence lambda>=-kappa also at rho=-a. The scalar equation on the C2 stable curve gives distance comparable to exp(lambda t); with Omega=alpha0 exp(-kappa t)B, it gives the same power law. This is a separate boundary extension of the hyperbolic part of A630. The selected campaign witnesses already lie in rho<-a.

There is also a nonflat semihyperbolic possibility to check at rho=-a; the second existing referee identified it explicitly. Suppose D Omega(q)!=0. The first A469 family has both level eigenvalues positive and is excluded by the level index. The second family then gives spec F={-a,0,kappa}, where F=DB(q). Put J0=D Omega(q). Expanding the Cauchy bracket at their common zero gives

    F J0-J0 F=kappa J0.

No second derivative of Omega is used: expand B,Omega,DB,D Omega to their existing first orders. Since 0<a<kappa, the only difference of two distinct eigenvalues equal to kappa is target kappa minus source0. The three eigenvalues are distinct, so J0 vanishes on the -a and kappa eigenlines and can only map the center line into the kappa line.

The convergent orbit eventually lies on the local center curve of the surface field: its transverse equation r'=r C with C>=b>0 would prevent any nonzero r from staying in the chart for all future time. Its secant direction at q therefore tends, up to sign, to the center eigenline. On the orbit, Omega=alpha0 exp(-kappa t)B and local Lipschitz continuity of B gives

    |Omega(y(t))|/|y(t)-q|<=C exp(-kappa t)->0.

Differentiability of Omega forces J0 to kill the center eigenline too, hence J0=0, a contradiction. Thus every endpoint at rho=-a is first-order flat. Together with the preceding hyperbolic boundary estimate, this supplies both missing boundary deductions for B40(c). Neither alone replaces the other.

## 11. Source-scope corrections

B40 Remark(xxv) incorrectly assigns the nonstationary spectrum {0,rho,3c-rho} to the limiting equilibrium atom. At an equilibrium the derivative cocycle is exp(t DB(q)), so the Lyapunov exponents are the real parts of its matrix eigenvalues. They are {rho,lambda,eta}, with lambda+eta=3c-rho. A flow-direction zero exponent does not exist automatically at a zero of B. The displayed nonstationary spectrum applies to the atom only if lambda=0. Polynomial factors from Jordan blocks do not change these exponential rates. This is a refuted source inference, separate from the correct collapse theorem.

Positive area expansion is essential in the collapse proof, though not in the strip finiteness argument. Removing it gives immediate counterexamples such as an attracting periodic orbit on an annulus; the equilibrium spectral premise is then vacuous. The Euler bounded theorem needs only uniform sublinearity and its stated global helicity-free structure. In contrast, the escaping-end conclusion still requires the natural far-field bounds or the exact derivative premises supplying them. Its common zero is that of velocity and PROJECTED tail vorticity; the radial tail vorticity is nonzero with the parameter sign by A602. No full tail-vorticity zero is implied. Both bounded halves may end at different equilibria.

## 12. Verification record and limitations

The complete w1cantor proof, exact question and verification statement, B40's source proposition, A614/A629 finite-section proofs and A630's endpoint proof were read. The original counterexample and each new cone, strip, half-block, flux and compactness argument were independently reconstructed above. The source's assertion of constant divergence on a neighborhood must be read as the positive lower bound actually used in its Step5; equality holds only on K in the Euler construction.

No computation or formal build is used. The inner attempted model consultation reported credential failure before any response and is not counted. Existing configured-model coordinator/theory file collaboration continues, with model the primary model configured and no independent provider-runtime attestation. The complete second existing referee proof w1cantor2 was then read and compared. It independently confirms the strip/half-block theorem, identifies the same divergence correction, and adds the nonflat rho=-a repair above. Its proof of that repair is verified here; the separate hyperbolic flat endpoint at rho=-a also needs the preceding A630 extension. The new focused model comparison remains pending.
