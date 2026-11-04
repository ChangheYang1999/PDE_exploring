# Repeated audit of all-equilibrium backward limits

## 1. Statement and exact scope

Let U in C2(R3;R3), P in C1(R3), 0<c<1/2 and omega in R satisfy

    (1-c)U + (B.grad)U + omega J U + grad P = 0,
    div U=0, B=(cI-omega J)y+U, J(x,y,z)=(-y,x,0).

Assume U(y)=o(|y|) uniformly at infinity. Write Omega=curl U, phi_t for the B-flow and psi_t=phi_-t. For every a with Omega(a)!=0, if its entire backward limit K=alpha_phi(a) lies in N={B=0}, then K is a singleton. The set of all these vortical initial points is Lebesgue-null.

The limiting equilibria may be irrotational and may belong to a non-discrete zero set. There is no pressure normalization, rate of decay, integrability, symmetry or bound on omega. The conclusion does not cover a limit set containing a nonstationary orbit. It is a conditional dynamical theorem, not unconditional profile nonexistence.

The report excerpt and source hashes are in the team records. This repeats the A058, A098 and A122 arguments, with direct reading of the source passages specified there. D3(c)'s separate Alves-Pinheiro argument is not freshly audited here.

## 2. Completeness and a full-flow growth measure

The C1 vector field B has at most linear growth, so its flow is complete in both directions. Outside a sufficiently large ball, B(y).y>=c|y|^2/2. The backward flow enters that ball and remains there. Consequently every negative orbit is precompact, K is nonempty compact connected and invariant, and the distance of psi_t(a) to K tends to zero.

The curl equation gives [B,Omega]=-(1+c)Omega. Uniqueness for the linear variational equation yields

    Dphi_t(x)Omega(x)=exp((1+c)t)Omega(phi_t(x)).

In particular, vorticity never vanishes along the orbit of a vortical point.

Here is a direct proof of the measure needed in D3.1. On a compact neighborhood of the negative orbit, use the normalized derivative flow

    F_t(x,v)=(phi_t(x),Dphi_t(x)v/|Dphi_t(x)v|), |v|=1.

One may cut off B outside a larger compact set and extend the resulting zero field near infinity to the one-point compactification S3, without changing any segment used below. The unit tangent sphere bundle of this compact base is compact. The instantaneous logarithmic growth is the continuous function g(x,v)=v.DB(x)v. Put x_n=psi_n(a) and v_n=Omega(x_n)/|Omega(x_n)|. The length-n lifted segment starting at (x_n,v_n) satisfies

    integral_0^n g(F_t(x_n,v_n))dt
      =(1+c)n+log|Omega(a)|-log|Omega(x_n)|.

Vorticity is bounded above on the negative orbit, so these averages have lower limit at least 1+c. Take a weak limit eta of their empirical probabilities. Translating any segment by a fixed flow time changes its normalized integral against a bounded continuous function by at most two endpoint intervals divided by n. Thus eta is invariant under every F_t. All but a bounded initial portion of a negative orbit is arbitrarily close to K, so eta is supported over K. Its integral of g is at least 1+c.

The ergodic decomposition of eta contains a component eta_0 with integral g at least 1+c. Its projection mu is ergodic for the full B-flow: the inverse image of a base invariant set is an invariant set for F. Birkhoff on the lifted flow and Oseledets on the base imply that the typical directional growth of eta_0, equal to its integral of g, is bounded above by the largest exponent of mu. Compactness gives the required integrability of the derivative and its inverse. Hence mu has largest forward exponent at least 1+c.

This is a full-flow statement. No ergodicity of a particular time map is assumed.

## 3. What the cited subadditive papers establish

Schreiber's Theorem1, printed page336, gives a supremum over flow-ergodic probabilities; it does not state attainment. Morris's TheoremA3 and PropositionA5, printed pages24-25 of the archived manuscript, give attainment for a discrete compact system. The passage from a time map to the full flow requires an argument. Section2 supplies the precise Euler conclusion directly.

The general maximum formula used in the report also follows by the same normalized derivative construction. On K times the unit sphere, choose times t_n tending to infinity and initial directions attaining sup_K|Dphi_tn|. Their empirical measures have invariant limit eta with integral g equal to the uniform growth rate chi_*. Every invariant lifted measure has integral g<=chi_* by integration of the finite-time bound. A maximizing ergodic lifted component therefore projects to a flow-ergodic measure whose largest exponent is at least chi_*. The uniform derivative bound gives the reverse inequality. Subadditivity and bounded growth on bounded time intervals give existence of chi_*. Thus the maximum assertion is valid for the derivative cocycle used here, including attainment.

The sentence in Schreiber's proof of Lemma3 on printed page342 that passes directly from flow ergodicity to time-one ergodicity is false. A circle flow of period one has ergodic normalized length measure, whereas its time-one map is the identity. This source defect was already recorded in the team records and the original A098 proof; it is not a newly discovered gap. The desired support relation can be repaired by time-one ergodic decomposition in one direction and full-flow averaging followed by ergodic decomposition in the other. Neither this sentence nor an unproved attainment assertion is needed above.

The report's theorem remains valid. A useful citation clarification would append the direct normalized-derivative proof or explicitly distinguish the continuous-time supremum and the attainment step. No source theorem is declared false merely because its printed proof has this repairable sentence.

## 4. A rank-two saddle point and an actual arc

If K lies in N, every flow-ergodic probability on K is a point mass. Section2 therefore supplies p in K with max Re spec DB(p)>=1+c. If K is non-singleton, connectedness implies that none of its points is isolated in N. The inverse function theorem gives det DB(p)=0. Since tr DB(p)=3c, the other two eigenvalues cannot be a complex pair: their common real part would be 3c/2<1+c. Hence

    spec DB(p)={lambda,0,3c-lambda},
    lambda>=1+c, 3c-lambda<=2c-1<0.

All eigenvalues are real and distinct; DB(p) has rank two. For Y=-B this is a saddle with one center direction.

Two components of B have independent differentials at p. Their common zero set in a small neighborhood is an embedded C2 curve gamma. The full equilibrium set is only a closed subset of that curve at this stage. Parameterize gamma with gamma(0)=p. If an interval on either side of zero lies in K, an arc is already available. Otherwise select alpha<0<beta with both endpoint images outside K. A thin closed tube around gamma([alpha,beta]), compactly within the local chart, has boundary disjoint from K: its side boundary misses gamma and its end faces meet gamma only at the chosen endpoints. Its intersection with K is nonempty and both relatively open and closed. Connectedness forces all of K into the tube, and then K is a non-singleton compact connected subset of a curve, hence contains an interval.

Choose q inside such an interval sufficiently near p. Near q the entire equilibrium set is exactly an open arc. Shrink to a compact subarc J about q on which the two nonzero normal eigenvalues remain real, simple and of opposite sign. No manifold structure of the original global zero set was assumed.

## 5. Local invariant surfaces and their source hypotheses

Cut off Y outside a compact neighborhood to obtain a complete C2 flow agreeing with the original field there, and let f be a sufficiently long positive time map. The compact arc J consists of fixed points. Along J, Df has a continuous splitting Es+Ec+Eu, where Ec is the tangent to J, Df is the identity on Ec, Es contracts uniformly and Eu expands uniformly. The distinct simple eigenvalues make the eigenline bundles continuous; a sufficiently large time absorbs uniform coordinate constants.

Apply Bonatti-Crovisier's Main Theorem with center bundle Es+Ec and strong unstable bundle Eu. Two different fixed points cannot approach each other under backward iteration, so the required absence of strong unstable connections holds. The center derivative is uniformly bounded under positive iterates, while the unstable derivative expands exponentially; their definition of r-normal hyperbolicity therefore holds for r=2. Their Corollary1.5 gives a C2 locally invariant center-stable surface. Apply the same statement to f inverse to obtain a C2 center-unstable surface.

The Main Theorem, Corollary1.5 and the proof of the latter in Section5.3.1 were read directly in the archived manuscript. This audit checks their stated hypotheses at this application; it does not claim a new proof or complete rereading of that paper. Only C1 surface regularity is actually used in the remaining argument.

The two surfaces meet transversely along J and can be straightened simultaneously near q into u=0 and s=0, with J={s=u=0}. The source's local invariance, expressed through f(S) intersect S containing a neighborhood of J in S, gives equality of germs: restrict to a small neighborhood of the fixed arc and use continuity of both f and its inverse. Thus this step does not replace map invariance by an unproved flow-invariance assertion.

## 6. Finite-passage control and capture

In the straightened coordinates the map has the form

    w'=w+F(w,s,u), s'=A(w,s,u)s, u'=D(w,s,u)u,
    |A|<=theta<1, |D|>=theta^-1,
    |F|<=C(|s|+|u|).

The factorizations follow from invariance of the coordinate surfaces. On the center arc the diagonal normal multipliers are the stable and unstable eigenvalues, so the strict bounds persist on a small closed box. The drift bound follows from F vanishing on the arc and its bounded first derivatives.

For any finite passage z_0,...,z_n inside that box,

    |s_j|<=theta^j|s_0|,
    |u_j|<=theta^(n-j)|u_n|,
    |w_n-w_0|<=C(1-theta)^-1(|s_0|+|u_n|).

The last estimate is a sum of two geometric series. It is independent of the passage duration, which is essential.

Take a closed inner box Q with |w|<=r and |s|,|u|<=d, and a larger closed box Qplus compactly inside the chart. The center interval of Q has positive margin inside that of Qplus. Continuity and the fixed center arc imply that all points in Q with sufficiently small normal coordinates have their image in Qplus.

Since the entire limit set consists of equilibria, every sufficiently late visit of the orbit to Qplus has arbitrarily small normal coordinates. Otherwise a subsequence of such visits would converge to a point of K inside Qplus off the equilibrium arc. Also q is a limit of time-map samples: for t_j=n_j T+tau_j with tau_j in[0,T), apply the inverse flow for tau_j to an orbit point tending to q. Uniform continuity over bounded times and the fact that q is fixed give convergence of the samples to q.

Choose epsilon<d small enough for the image property above and 2C epsilon/(1-theta)<r/2. Take a sufficiently late sample with |w_0|<r/4 and both normal coordinates less than epsilon. If n is its first later exit from Q, all earlier samples lie in Q and the exiting one lies in Qplus. All their normal coordinates are less than epsilon. The finite-passage bound gives |w_n|<3r/4, while the normal coordinates remain less than d. This contradicts exit.

Every later sample stays in Q. The uniform unstable expansion forces u_0=0; stable coordinates decay geometrically and center increments are absolutely summable. The samples converge to one point of J. Bounded-time continuity then gives convergence of the whole continuous orbit to that same equilibrium. This contradicts non-singleton K and proves the claimed point-limit conclusion.

## 7. Nullity of all vortical point-limit basins

For a vortical orbit converging backward to p, the largest real part of spec DB(p) is at least 1+c, by Section2 with K={p}. Since the trace is 3c, another eigenvalue has real part at most (2c-1)/2. All such p belong to the compact set

    N1={p in N: min Re spec DB(p)<=(2c-1)/4}.

At each p in N1, DY(p)=-DB(p) has a positive-real-part eigenvalue. To see the required local nullity without counting equilibria, split into generalized eigenspaces Ecs+Eu for real parts at most zero and greater than zero. Choose beta below the smallest positive real part, epsilon0=beta/4 and eta=beta/2. Semigroup bounds have the form

    |exp(-tLu)|<=M exp(-beta t),
    |exp(tLcs)|<=M exp(epsilon0 t).

Write Y(p+z)=Lz+r(z), with r of Lipschitz constant ell on a sufficiently small bounded convex neighborhood. For two orbits staying there for all positive time, let w be their difference and D*=sup_t exp(-eta t)|w(t)|. Variation of constants in Ecs and the terminal integral in Eu give

    D*<=M|w_cs(0)|+M ell[(eta-epsilon0)^-1+(beta-eta)^-1]D*.

The terminal boundary term vanishes because the orbits are bounded and beta>eta. Shrink the neighborhood until the last coefficient is at most1/2. Then D*<=2M|w_cs(0)|. Projection of the trapped set to Ecs is injective, with a Lipschitz graph as inverse. Its dimension is at most two, so this local trapped set is Lebesgue-null.

Choose smaller neighborhoods covering the compact set N1, and extract a finite subcover. An orbit converging to a point of N1 eventually stays in one corresponding larger neighborhood, after some integer time. Its initial point belongs to the image of one local null set under an integer-time C1 diffeomorphism. A countable union over the finite cover and integer times is null. This proves the stated measure-zero conclusion, including uncountable sets of limiting equilibria.

## 8. Existing comparisons and residual scope

The original A098 proof, the complete A122 standalone proof and SOURCE_ERRATA were reread. The previously recorded coordinator comparison of the capture argument, and Theory Agent A 's later checks of the D1-D3 source attributions and local-topology wording, are the existing model collaboration for this repeat. The source warning is already accounted for by A098; it does not revoke D3.1 or D3(b).

This audit finds no additional mathematical premise needed for D3(a)-(b). In particular, no pressure gauge, boundary integral or numerical calculation enters. The source-to-time-map regularity and the whole-limit-set hypothesis are retained explicitly. The main nonexistence problem remains OPEN because arbitrary vortical backward limits have not been shown to consist only of equilibria or other already excluded classes.


## 9. Follow-up with the Theory Agent A  citation correction

NoteA84 correctly retracts the attribution of full-flow attainment directly to Schreiber and Morris. The former gives the continuous-time supremum; the latter gives discrete attainment. Sections2-3 and the earlier A098 proof supply the missing passage for the actual derivative cocycle. No theorem is withdrawn.

The optional averaging proof in A84 is also valid. Let mu1 be a time-one ergodic maximizing measure on the compact invariant set K, and define nu as the integral of (phi_s)_*mu1 over 0<=s<=1. Time-one invariance makes this average invariant under every real flow time: translating the unit interval changes its integral by two intervals that agree after an integer shift. For s in[0,1], the cocycle identity is

    Dphi_t(phi_s x)=Dphi_s(phi_t x) Dphi_t(x) [Dphi_s(x)]^(-1).

Compactness bounds Dphi_s and its inverse uniformly. Hence the logarithms of the two norms Dphi_t(phi_s x) and Dphi_t(x) differ by at most a fixed constant independent of t and s. Whenever the top exponent exists at x it has the same value at phi_s x. The integer-time exponent equals the continuous-time exponent by the same bounded-remainder-time argument. Thus nu has top exponent chi_star almost everywhere. Ergodic decomposition of nu gives that value for almost every full-flow ergodic component, and in particular supplies an attaining component.

This argument verifies A84's proposed passage rather than assuming that a flow-ergodic measure is time-one ergodic. The independent normalized-derivative proof remains a direct alternative requiring no maximizing time-one measure as input.
