# Nonflat equilibrium companions and a planar singleton criterion

Status: A572-A574 CONFIRMED after complete source, primary-input and independent proof postreads. The planar hypothesis is additional and is not deduced from Euler. A separate area lemma has an explicit rate-sign correction.

## 1. Exact global setting

Let 0<c<1/2 and omega be any finite real number. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    U=o(|y|) uniformly, U.curl U=0 everywhere,
    A=cI-omega J, J(y1,y2,y3)=(-y2,y1,0).

Write B=Ay+U, W=curl U, a=1-2c, kappa=1+c, H=P+|U|^2/2+(Ay).U and g=U.B. Let p be a vortical carrier equilibrium and let rho be its real covector eigenvalue, DB(p)^T U(p)=rho U(p). Assume rho<=-2a. Let L+ be either half of the complete W-orbit through p, parametrized in the forward B direction, and assume L+ is bounded. Put K=omega_B(L+) and E=K intersect{B=0}.

The exact A540-A542 results give that K is nonempty compact connected and fully invariant, contained in the vortical closure, and

    W=0, H=H(p), g=0, grad H=-aU, grad g=rho U on K,
    min_K |U|>0, Phi_t^*Uflat=exp(rho t)Uflat.          (1)

The identities H=H(p), g=0, grad H=-aU and grad g=rho U also hold on L+, whose points have W!=0. K has no nonconstant periodic orbit. Every invariant probability on K is supported on E. If q in E and F=DB(q), its invariant plane U(q)^perp has eigenvalues

    lambda_-<=0<lambda_+, lambda_-+lambda_+=3c-rho.    (2)

Finally A542 proves: if K consists of finitely many hyperbolic equilibria and finitely many equilibrium-to-equilibrium connecting orbits with singleton ends, then K is a singleton. This last statement is a conditional geometric theorem, not an inference from the invariant probabilities. Section5 recalls its actual passage estimate.

Momentum makes grad P C1, hence P and H are C2. All carrier and vorticity flows used here are complete by the confirmed uniform-sublinearity results. No far-field derivative or pressure-decay estimate is needed.

## 2. Nonflat equilibrium finiteness and the exceptional rate

For q in E with DW(q)!=0, the two A469 spectral families are

    I:  {rho,rho+kappa,-a-2rho},
    II: {rho,(-a-rho)/2,(1+4c-rho)/2}.               (3)

In family II, rho<=-2a implies that both plane eigenvalues are strictly positive. This contradicts(2). Thus only I occurs. Its last eigenvalue is positive and rho is negative. It has a zero eigenvalue exactly when rho=-kappa. If rho!=-kappa, (2) forces rho+kappa<0. Consequently every such nonflat equilibrium is hyperbolic and

    spec F={rho,rho+kappa,-a-2rho}, rho<-kappa.      (4)

An invertible F makes q an isolated zero of B by the inverse-function theorem. More generally, any nonisolated zero q has a zero eigenvalue: choose distinct zeros q_n->q, divide B(q_n)-B(q)=F(q_n-q)+o(|q_n-q|) by |q_n-q|, and pass to a unit-vector subsequence. Its limit lies in ker F.

Therefore, when rho!=-kappa, E is the disjoint union of its relatively open discrete nonflat part and its closed flat part E_flat={q in E:DW(q)=0}. Accumulation points of the nonflat part can only be flat. If E_flat is empty, compactness makes E finite. A nonconstant continuous curve of equilibria cannot contain one of these isolated points. At rho=-kappa a nonflat equilibrium instead has spectrum

    {-kappa,0,1+4c};                                (5)

neither a curve of zeros nor a more complicated zero set is excluded at that exceptional rate. These are necessary algebraic restrictions, not realizations of local or global Euler profiles.

## 3. The planar hypothesis and the projected field

Add precisely:

    ND_E: DW(q)!=0 for every q in E, and rho!=-kappa;
    PL: K has a planar open neighborhood D0 in the regular level H=H(p).

Here planar means homeomorphic to an open subset of R2. Holes are permitted. The regular level is the C2 surface near K, whose existence follows from(1). A disk is not required. ND_E does not assert that DW is nonzero at every point of K.

On a regular open neighborhood of K define

    X=B-[(B.grad H)/|grad H|^2]grad H.                (6)

It is C1 and tangent to the level. It equals B on K and on the tail of L+ because g=0 there. Thus all K-orbits and that tail are actual X-orbits. At q in E and v tangent to the level,

    D(B.grad H)(q)v=grad H(q).Fv=0,
    DX(q)v=Fv.                                      (7)

The first equality uses B(q)=0 and the fact that F preserves U(q)^perp, already supplied by its covector eigenvalue. This is stronger justification than B(q)=0 alone. By Section2, E is finite and the planar eigenvalues at each q are rho+kappa<0 and -a-2rho>0. Every q is a hyperbolic saddle for X.

The late tail has compact closure inside D0. Indeed choose a smaller neighborhood of K whose compact closure lies in D0. If the bounded orbit visited its complement at arbitrarily late times, a subsequence would converge to a point of K outside that neighborhood. This is impossible. X and B agree on all of K, so the equilibria and periodic orbits of X in K are exactly those of B. In particular K has no periodic orbit of X.

No invariance of the entire original H-level under B has been assumed. Projection supplies the surface field needed by the planar argument.

## 4. The precise planar input, with its finite-equilibrium consequence

The only imported geometric fact is the ordered-crossing lemma for a planar flow: along any sufficiently short transverse simple arc with a fixed crossing direction, the successive intersections of a nonperiodic orbit are strictly ordered in the arc parameter. The proof joins two consecutive crossings by the orbit segment and the intervening arc to obtain a Jordan curve. Uniqueness prevents crossing the orbit segment, and transversality fixes the crossing direction through the arc. A later crossing must therefore lie farther along in the same arc direction. This argument needs the Jordan separation in the plane, not that the filling region lie inside the vector-field domain. Holes do not invalidate it.

The complete primary author note by Harald Hanche-Olsen, The Poincare-Bendixson theorem, version2007-01-16, was obtained and read. Its Lemma3, pages3-4, states and proves this ordered-crossing input. Its introductory warning correctly distinguishes connecting graphics from equilibrium or periodic omega limits. The following consequence is proved here rather than attributing an unchecked theorem number to Perko.

Let a C1 surface flow have a positive orbit with compact closure in a planar domain. Let K be its omega-limit set, suppose K contains no periodic orbit and only finitely many equilibria E. Then every regular orbit in K has a singleton equilibrium as each of its alpha- and omega-limit sets.

To prove this, the original positive orbit is nonperiodic. Every sufficiently short transverse arc meets K in at most one interior point. Indeed the original orbit's crossings are strictly monotone. They have at most one accumulation point in the arc. Every interior K-point on that arc is such an accumulation point: nearby late visits can be moved to the central transversal by the flow-box coordinate, with time shifts tending to zero. This yields arbitrarily late actual crossings. Thus two distinct interior K-points are impossible.

Now let y be regular in K. Its full orbit lies in compact K. If a regular z belonged to omega(y), a short transverse arc through z would be crossed by the orbit of y infinitely often. All crossing points lie in K and in the interior of the arc, so they must equal the same point. Repetition makes the orbit periodic by uniqueness, contrary to the hypothesis. Thus omega(y) is contained in E. It is nonempty compact connected, as the intersection of decreasing compact closures of connected forward tails, so it is one equilibrium. Applying the same crossing argument to negative-time visits proves the identical conclusion for alpha(y). No claim about invariant probabilities was used.

If every equilibrium in E is a hyperbolic planar saddle, there are at most2|E| such regular connecting orbits: each belongs to one of the two unstable branches of its alpha equilibrium, and each branch is a single orbit. Hence K is a finite saddle network or a singleton.

The same argument works with PL as stated, without assuming a differentiable global planar coordinate. Push the flow and its local flow boxes through the given homeomorphism. The transverse arcs, their orders, uniqueness and Jordan separation are topological properties preserved by that map. The differentiability needed for the local saddle theorem is supplied in the original C2 surface charts, not demanded of the homeomorphism. This avoids an unmentioned smooth-classification theorem.

## 5. Collapse and the endpoint window

Apply Section4 to the projected field(6). Its K is therefore a finite hyperbolic network unless already a singleton. All its K-orbits are B-orbits. The exact A542 collapse applies, giving

    K={q}, L+(t)->q.                                (8)

For clarity, A542 does not need a planar filling region. Near each surface saddle, whose eigenvalues are -beta<0<lambda with lambda-beta=3c-rho>0, straighten its two invariant curves by a C1 change of coordinates. Componentwise factorization gives xi'=xi(lambda+o(1)) and eta'=eta(-beta+o(1)). Choose epsilon>0 with theta=(beta+epsilon)/(lambda-epsilon)<1. If a nearby nonseparatrix enters a saddle box at incoming distance r, its outgoing distance is at least C r^theta. Along the finitely many connecting tubes, C1 transverse maps have derivative bounded away from zero. If the original orbit accumulated on the entire network, its successive incoming distances would tend to zero but obey r_next>=C r^theta for a uniform theta<1. For small r the right side exceeds2r, a contradiction. If the orbit reaches a stable branch exactly, it converges to that equilibrium. Finitely many passages likewise give convergence. This is the complete mechanism behind the imported confirmed collapse.

By(4), q is a nonflat first-family equilibrium with rho<-kappa. A543's exact local stream-function theorem says that, at such an equilibrium in the vortical closure, a converging vortical orbit on the zero-g level is impossible when rho<-2kappa, because its stable curve is then irrotational. The actual L+ is vortical and converges by(8), so

    -2kappa<=rho<-kappa.                            (9)

The original rho<=-2a remains an assumption; outside the target c range one retains its intersection with(9). The lower endpoint is not excluded. No existence follows from the surviving interval.

## 6. Separate area lemma and the return-map sign

Let Sigma0 be a connected regular H-level on which g=0. Suppose dH wedge dg=0 holds on an ambient open neighborhood of Sigma0. In each regular H-coordinate box it gives g=G(H). Overlapping boxes show that G'(H0) is locally constant along Sigma0 and hence constant by connectedness. Set rho_Sigma=-aG'(H0). Differentiating BH=-ag gives on Sigma0

    Lie_B dH=rho_Sigma dH.

For N=grad H/|grad H|^2 define the positive oriented area form nu=i_N vol restricted to Sigma0. Since dH wedge i_N vol=vol and div B=3c, pullback by the tangent B-flow, or the same identity differentiated at time0, gives

    Lie_B nu=(3c-rho_Sigma)nu.                       (10)

The neighborhood assumption is essential: g=0 on a surface alone does not make its transverse derivative constant.

If delta=3c-rho_Sigma is nonzero, no compact region of positive nu-area contained in this domain can have piecewise C1 boundary consisting only of B-orbit arcs and equilibria. Stokes gives delta integral_R nu=integral_boundaryR i_B nu=0, since each orbit tangent annihilates i_B nu. The filling region must stay in the domain of(10). There is no exclusion of nonbounding cycles based on this argument alone.

Put beta=i_B nu. Then Lie_B beta=delta beta. For a regular return branch P(x)=Phi_{T(x)}x with T>0 and entire trajectories inside the domain,

    P^*beta=exp(delta T)beta.                         (11)

The derivative of the return time contributes a multiple of B, annihilated by beta. In compatible transverse flux coordinates P'=exp(delta T). It is greater than1 only if delta>0, equals1 if delta0, and is less than1 if delta<0. In the present lower-window companion setting delta=3c-rho>=3c+2a=2-c>0, so expansion is valid there. The source's general 'delta!=0' hypothesis does not justify an unqualified greater-than1 sign on an unrelated regular level.

For a direct surface countertest of that general inference, on the annulus S1 times(-epsilon,epsilon) let X=partial_theta-r partial_r and nu=dtheta wedge dr. Then Lie_X nu=-nu and the return map after2pi is r->exp(-2pi)r. This is an elementary surface example, not an Euler profile counterexample. It also illustrates why area divergence does not exclude a nonbounding periodic orbit.

## 7. Scope, source corrections and verification

The source's revised Proposition9 repairs its earlier unsupported shrinking of a whole disk inside the area-identity neighborhood. ND_E suffices, holes are allowed, and the new proof uses no filling region. The old claim that infinitely many ordinary saddle connections may remain when E is finite hyperbolic is false: at most2|E| unstable branches exist. The unresolved issue without planarity is whether every regular K-orbit has singleton equilibrium ends. Flat equilibria and rho=-kappa also remain outside the criterion.

All of W1_FARFIELD Sections4f-4g, the complete actual w1far5 referee and the full A540-A542 independent proofs were read. The primary four-page crossing proof was read in full; the failed Perko download is recorded, and no exact Perko theorem number or unreceived review is claimed. No computation is used. The Theory Agent B source is from the existing theory agent; configured-model premises and coordinator file exchange continue.

This proves a conditional planar collapse and exact nonflat equilibrium restrictions. It does not prove planarity of an Euler Bernoulli level, classify general higher-genus singular limit sets, or establish the unrestricted nonexistence conjecture.
