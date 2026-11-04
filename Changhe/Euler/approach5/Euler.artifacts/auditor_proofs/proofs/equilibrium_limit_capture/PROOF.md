# All-equilibrium backward limits of vortical trajectories

Status: CONFIRMED in A122. The local ODE argument and Euler spectral step were independently cross-checked by the coordinator; the final source-based discrete proof is supplied below.

## Exact Euler statement

Let U in C2(R3;R3), P in C1(R3), 0<c<1/2, and finite real omega satisfy the rotating profile equation and div U=0. Assume U(y)=o(|y|) uniformly. Put B=(cI-omega J)y+U and Omega=curl U. Every point x with Omega(x)!=0 whose backward limit set is contained entirely in {B=0} has a single-point backward limit. The set of all such vortical x has Lebesgue measure zero.

The limiting equilibria need not be vortical. No pressure normalization, derivative decay, integrability, symmetry or rotation bound is required. Limit sets containing nonstationary orbits are outside this theorem.

## 1. Local ODE theorem

Let Y be a C2 vector field on a three-dimensional manifold, and let z(t), t>=0, be a precompact forward orbit. Suppose its omega-limit K consists entirely of equilibria of Y. If K is not a point, then K cannot contain an equilibrium p such that

    spectrum DY(p) = {lambda_s, 0, lambda_u},
    lambda_s < 0 < lambda_u,
    rank DY(p) = 2.

Equivalently, if it contains such a point, the orbit converges to a single equilibrium.

This assertion needs no Lyapunov function, volume condition, gradient structure or vorticity. It uses that the whole omega-limit consists of equilibria. A heteroclinic cycle is not within its scope.

## 2. Extracting an interior arc from a nonpoint limit

Suppose instead that p in K has the spectrum in Section 1, without an a priori equilibrium arc. Rank two and the implicit function theorem put the whole equilibrium set in a sufficiently small neighborhood of p inside one embedded C2 curve gamma. The full zero set may be a closed proper subset of this curve. The nonzero normal eigenvalues remain real, simple and of opposite signs at nearby zero points; the third eigenvalue is zero at non-isolated zeros.

A nonempty compact connected set K of equilibria containing p, if it is not one point, contains a nontrivial interval of gamma arbitrarily near p. Here is the elementary local-topology argument. Parameterize gamma so that p has coordinate zero. If one side of every sufficiently short interval from zero is entirely in K, there is already the required interval. Otherwise choose nearby curve coordinates alpha<0<beta with gamma(alpha),gamma(beta) not in K. Take a narrow closed tube around gamma([alpha,beta]), compactly in the implicit-function neighborhood, with end faces meeting the curve only at these two points. Its whole boundary is disjoint from K, since every local equilibrium lies on gamma. Its intersection with K is nonempty and both relatively open and closed in K. Connectedness therefore puts all of K in this tube. K is then a compact connected subset of gamma, hence a closed interval; because it is not a point, it contains an interior subinterval.

Choose q in the interior of one such interval, still in the neighborhood where the two nonzero eigenvalues have opposite signs. The local equilibrium set near q is exactly an open part of gamma, since it contains that interval and is contained in gamma. The discrete capture proof in Section 3 below applies and forces convergence, contradicting that K is not a point.

## 3. Source-anchored discrete proof of capture

This section removes the need to assume a flow version of the local center-stable theorem. It uses the actual Main Theorem and Corollary 1.5 in Bonatti and Crovisier, "Center manifolds for partially hyperbolic sets without strong unstable connections", arXiv:1401.2452v1. The manuscript is archived at `in the team records`, relative to this agent root. Both statements and the regularity proof in Section 5.3.1 have been read. The result gives a locally invariant submanifold for a diffeomorphism, which is all the argument below needs.

Let J be a small closed subarc of equilibria around the interior point q found in Section 2. Extend Y smoothly outside a compact neighborhood if necessary to obtain a complete C2 flow without altering the orbit near J. Fix T>0 and let f be its time-T map. On J, the derivative has the continuous invariant splitting E^s+E^c+E^u, with E^c tangent to J, identity on E^c, uniform contraction on E^s and uniform expansion on E^u. The eigenvalues are distinct. An adapted norm makes the stable and unstable bounds uniform; a larger T absorbs the bounded change of eigenbases.

Apply the Main Theorem with its center bundle equal to E^s+E^c, and its strong unstable bundle E^u. Distinct points of J are fixed, so no two belong to the same strong unstable leaf. The center derivative is uniformly bounded under positive iterates, while the unstable derivative expands exponentially. Thus this splitting is r-normally hyperbolic in the source's sense for r=2. Corollary 1.5 gives a C2 locally f-invariant surface S^cs through J. Apply the same argument to f^{-1}, with its center bundle E^c+E^u, to get a C2 locally invariant surface S^cu. Their tangent spaces intersect precisely in E^c along J. The surfaces are transverse, and their local intersection is exactly J near q.

A simultaneous C2 coordinate chart (w,s,u) therefore has J={s=u=0}, S^cs={u=0} and S^cu={s=0}. Local invariance is an equality of germs near the fixed arc: the source statement f(S) intersect S contains a neighborhood of J in S, together with continuity of f^{-1} near fixed points, gives both directions after shrinking. In these coordinates,

    w_{n+1} = w_n + F(w_n,s_n,u_n),
    s_{n+1} = A(w_n,s_n,u_n) s_n,
    u_{n+1} = D(w_n,s_n,u_n) u_n.

For some 0<kappa<1 and C<infinity on a sufficiently small closed chart box,

    |A| <= kappa,   |D| >= kappa^{-1},
    |F| <= C(|s|+|u|).

The factors are continuous by Hadamard factorization. Their values on the arc are the stable and unstable normal eigenvalues of Df. Only C1 regularity of the coordinate map and bounded first derivatives of F are needed here, and the source provides C2.

For a finite passage z_0,...,z_n inside this box, iteration gives

    |s_j| <= kappa^j |s_0|,
    |u_j| <= kappa^{n-j} |u_n|,
    |w_n-w_0| <= C(1-kappa)^{-1} (|s_0|+|u_n|).       (3.1)

Take an inner box Q={|w|<=r, |s|,|u|<=d} and a larger box Qplus compactly in the chart. Choose Q with its center interval compactly inside the center interval of Qplus. Since f fixes the whole center arc, all points of Q with sufficiently small |s|+|u| have their image in Qplus. This follows uniformly from continuity and compactness.

The original precompact continuous orbit has distance to its equilibrium limit K tending to zero. In Qplus the equilibrium set is exactly the center arc. Hence, at sufficiently late times, all visits to Qplus have |s|,|u|<epsilon. The point q is also a limit of the time-T samples: if z(t_j) tends to q, write t_j=n_j T+tau_j with 0<=tau_j<T and use z(n_j T)=Phi_{-tau_j}(z(t_j)) and uniform continuity on this compact time interval; q is fixed. Thus there are arbitrarily late sample entries with |w_0|<r/4 and |s_0|,|u_0|<epsilon.

Choose epsilon so small that f sends the normally epsilon-close part of Q into Qplus, epsilon<d, and 2C epsilon/(1-kappa)<r/2. Suppose n is the first later sample outside Q. All earlier samples are in Q, while z_n is in Qplus by the preceding image property. Every sample from 0 through n is late and in Qplus, so its normal coordinates are less than epsilon. Formula (3.1), applied using the estimates on Qplus, gives |w_n-w_0|<r/2. Consequently |w_n|<3r/4 and |s_n|,|u_n|<d, contradicting the definition of n.

All subsequent samples remain in Q. Uniform expansion of the u coordinate forces u_0=0. The stable coordinate decays geometrically, and the center increments are absolutely summable. Thus the samples converge to a fixed point of the arc. Uniform continuity of Phi_tau for 0<=tau<=T gives convergence of the whole continuous orbit to the same equilibrium. This proves the capture assertion with a fully specified primary-source dependency.

The proof does not assume that an arbitrary compact equilibrium set is a manifold. The arc is first extracted from connectedness and a rank-two point. It does not apply to a limit set containing even one nonstationary orbit.
## 4. Euler theorem: every vortical all-equilibrium limit is a point

Assume U in C2(R3;R3), P in C1(R3), div U=0, the rotating profile equation, U=o(|y|) uniformly, 0<c<1/2, and any finite omega. Set B=(cI-omega J)y+U and Omega=curl U. Let x be vortical, Omega(x)!=0, and suppose

    alpha_Phi(x) is contained in N={B=0}.

Then alpha_Phi(x) is a single point. In particular, all such x form a Lebesgue-null set, by the already confirmed point-limit theorem.

To derive it, let K=alpha_Phi(x). The backward orbit is precompact, K is nonempty compact connected, and the exponent-transfer result A098 gives an ergodic invariant probability on K with top FORWARD derivative exponent at least b=1+c. Since every point of K is fixed, each ergodic probability is a point mass. Thus there is p in K for which

    max Re spectrum DB(p) >= 1+c.

If K is not a point, none of its points is isolated in N. Consequently det DB(p)=0. The other two eigenvalues sum to 3c. They cannot be a complex conjugate pair, whose common real part would be 3c/2<1+c. Thus they are real; writing the larger as lambda,

    lambda >= 1+c,
    the remaining eigenvalue = 3c-lambda <= 2c-1 < 0.

All three eigenvalues are distinct, so rank DB(p)=2. For Y=-B, they give one strictly negative, one zero and one strictly positive eigenvalue. The local ODE statement applies and forces K to be a point, the required contradiction.

This step makes no assumption on Omega(p). It therefore covers mixed zero sets containing irrotational equilibria, which A111 alone did not address. The negative eigenvalue at the limiting point, used in the null point-basin theorem, follows from the same exponent transfer even when that point is irrotational.


## 5. Dependencies, verification and consequence

The exact dependencies are A006 (complete flow and compact backward limits under sublinearity), A098 (a vortical limit carries an ergodic measure with top forward derivative exponent at least 1+c), A058 (the countable local-graph nullity theorem for vortical point-convergent basins), and the stated Bonatti-Crovisier Main Theorem and Corollary 1.5. The latter source was read directly, including Section 5.3.1. No numerical calculation is used.

The coordinator independently checked the spectral reduction, clopen-tube argument, local invariant surfaces and finite-passage estimate in its Note 5c dated 2026-11-02T20:01Z. The discrete argument above supplies an explicit source version and avoids confusing map invariance with flow invariance.

Consequently the conditional point-or-periodic-orbit Liouville criterion may replace its point alternative by the broader assumption that the entire backward limit consists of equilibria. If almost every vortical point has an all-equilibrium limit or a single periodic-orbit limit, then Omega=0 and U is constant; uniform decay makes U=0. This remains a dynamical hypothesis, not an unconditional nonexistence proof.
