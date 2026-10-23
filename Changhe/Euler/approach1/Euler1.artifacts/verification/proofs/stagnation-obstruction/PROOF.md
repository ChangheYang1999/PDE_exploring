# Countable stagnation sets below the half exponent

Date: 2026-10-23. Status: independent informal proof of the lead's claim L1. This is a theorem under a countability hypothesis. It is not an obstruction covering the full prompt class. No formal verification is claimed.

## Exact statement

Let 0 < c < 1/2. Suppose U and P are C² on R³, U(y) tends uniformly to zero as |y| tends to infinity, and

    (1-c)U + (cy+U)·∇U + ∇P = 0,    div U = 0.

Write V(y)=cy+U(y) and Z={y:V(y)=0}. If Z is countable, then U=0. No rotational symmetry is needed. The same conclusion holds with a constant axial drift C after the translation Y=y+(C/c)e_z. Countability and decay are preserved by that translation.

Notation: G_ij=∂_j U_i, S=(G+Gᵀ)/2, W=(G-Gᵀ)/2, Ω=curl U. Then W a=Ω×a/2 and WΩ=0. A set of Lebesgue measure zero is called null. All flow maps below are finite-dimensional classical ODE flows.

Dependencies: the profile and vorticity identities proved in ../profile-identities/PROOF.md; existence, uniqueness and differentiable dependence for C¹ ODEs; elementary matrix spectral decomposition and its exponential estimates; the Banach contraction theorem; Fubini's theorem; the mean-value estimate for harmonic functions. The only invariant-manifold fact needed is proved explicitly below, rather than assumed.

## 1. Every backward trajectory converges to one zero of V

U is bounded by continuity and decay. Thus |V(y)|≤c|y|+B, so both forward and backward trajectories exist for every finite time. For example, the integral inequality for |Y(s)| on a finite time interval and Gronwall's estimate bound |Y|, and local existence can then be continued on a compact ball.

Choose R with |U(y)|≤c|y|/2 when |y|≥R. Then V(y)·y≥c|y|²/2 there. In backward time t=-s the derivative of |Y(-t)|² is -2Y·V≤-c|Y|² outside B_R. Hence the entire backward orbit from a is contained in B_max(R,|a|). In particular it is precompact.

Set H=|V|²/2+P+c(c-1)|y|²/2. Direct substitution using Ω×V=(G-Gᵀ)V gives

    (1-2c)V + Ω×V + ∇H = 0,
    dH(Y(s))/ds = -(1-2c)|V(Y(s))|².

H is bounded on the compact backward orbit. It therefore has a finite limit h_- as s tends to -infinity. The alpha-limit set A is nonempty and compact. It is connected: it is the nested intersection of the compact connected closures of {Y(s):s≤-n}.

If q∈A, choose s_j→-infinity with Y(s_j)→q. For every fixed real t, continuous dependence gives Y(s_j+t)→Φ_t(q). Both H(Y(s_j)) and H(Y(s_j+t)) tend to h_-. Thus H(Φ_t(q))=h_-. Differentiating at t=0 and using c<1/2 gives V(q)=0. Therefore A⊆Z. A connected countable subset of R³ contains at most one point: two distinct points would have a coordinate projection containing a nontrivial interval. Hence A={q} for some q∈Z. Compactness then implies Y(s)→q as s→-infinity.

## 2. A basin with strain strictly below one carries zero vorticity

Along a trajectory the vorticity equation gives

    dΩ(Y(s))/ds = (G(Y(s))-I) Ω(Y(s)).

Suppose λ_max(S(q))<1 and Y(s)→q backward. Choose η>0 and s₀ such that λ_max(S(Y(s)))≤1-η for all s≤s₀. Dotting the preceding ODE with Ω yields

    d|Ω(Y(s))|²/ds ≤ -2η |Ω(Y(s))|².

For s<s₀, integration gives

    |Ω(Y(s₀))|² ≤ exp[-2η(s₀-s)] |Ω(Y(s))|².

Ω is bounded on the compact backward orbit. Taking s→-infinity proves Ω(Y(s₀))=0. Uniqueness for the linear vorticity ODE then gives Ω(a)=0. This proof does not require estimating an inverse flow derivative.

## 3. Every remaining equilibrium has a strictly contracting forward direction

At q∈Z the exact vorticity equation says G(q)Ω(q)=Ω(q).

If Ω(q)≠0, G has eigenvalue 1. Since tr G=0, the other two eigenvalues have sum -1, counted algebraically. The corresponding eigenvalues of DV=cI+G have sum 2c-1<0, so at least one has negative real part. This holds for a complex conjugate pair too. Also WΩ=0 gives SΩ=Ω, so this case cannot have λ_max(S)<1.

If Ω(q)=0, then W(q)=0 and G(q)=S(q) is real symmetric. In the remaining case λ_max(S(q))≥1, its smallest eigenvalue is at most -1/2 because its trace is zero. Thus DV has an eigenvalue at most c-1/2<0.

Consequently every equilibrium not handled by section 2 has at least one eigenvalue of DV with negative real part.

## 4. Local backward-bounded points near such an equilibrium lie on a null graph

This elementary graph lemma also allows zero eigenvalues and Jordan blocks. Translate the equilibrium to zero and write the C¹ vector field as x'=Ax+g(x), where g(0)=0 and Dg(0)=0. Split R³=E_s⊕E_cu into the real generalized eigenspaces with respectively negative and nonnegative real parts. By hypothesis dim E_s≥1, hence dim E_cu≤2. The spectral projections P_s and P_cu commute with A.

There exist a>0 and K≥1 such that ||exp(A_s t)||≤K exp(-at) for t≥0. Choose 0<b<β<a. Increasing K if needed gives ||exp(A_cu t)||≤K exp(-bt) for t≤0. These estimates follow by putting A in Jordan form: the polynomial factors can be bounded by an arbitrarily small additional exponential. All vector norms may be taken in the equivalent direct-sum norm |x_s|+|x_cu| after choosing Euclidean norms on the two subspaces. Its projections have norm at most one. Equivalently, constants can absorb the bounded oblique projections in the original Euclidean norm.

Cut g off outside a small ball. Because Dg(0)=0, the cutoff extension g_tilde can be made globally Lipschitz with arbitrarily small constant L, while agreeing with g in a smaller ball. To see this, on a radius-r ball use |Dg|≤ε and |g(x)|≤ε|x|; a smooth cutoff with |Dχ|≤C/r adds at most Cε to the derivative. Extend by zero beyond that ball.

On the Banach space of continuous functions x:(-infinity,0]→R³ with norm sup_{t≤0} exp(βt)|x(t)|, fix ξ∈E_cu and define a map by

    (Tx)_cu(t) = exp(A_cu t) ξ
                 + integral_0^t exp(A_cu(t-s)) P_cu g_tilde(x(s)) ds,
    (Tx)_s(t)  = integral_{-infinity}^t exp(A_s(t-s)) P_s g_tilde(x(s)) ds.

The first nonlinear integral, with its oriented integration sign, has norm bound KL/(β-b) times ||x||. The second has bound KL/(a-β) times ||x||. The input term has norm at most K|ξ|. Choose L so the sum of the two Lipschitz bounds is strictly below one. The contraction theorem supplies a unique fixed point x_ξ. The same estimates for differences show that x_ξ depends Lipschitz-continuously on ξ. Thus h(ξ)=P_s x_ξ(0) is Lipschitz.

Every actual trajectory that remains in the smaller ball for all negative time is bounded and belongs to this weighted space. Variation of constants gives its cu equation with ξ=P_cu x(0). In the stable equation start at t₀<t and send t₀→-infinity. The term exp(A_s(t-t₀))P_s x(t₀) tends to zero because the trajectory is bounded. Therefore it satisfies the displayed integral equations and equals x_ξ by uniqueness. Its endpoint belongs to the graph {ξ+h(ξ):ξ∈E_cu}.

That graph is null in R³. In the linear coordinates E_cu×E_s each fiber over ξ consists of a single point in a positive-dimensional space E_s, which has measure zero. The graph is measurable because h is continuous. Fubini proves the assertion, and an invertible linear coordinate change preserves null sets.

## 5. The global exceptional set is null

Fix one of the equilibria from section 3 and its small ball from section 4. Any trajectory converging backward to that equilibrium eventually remains in this ball for all earlier time. There is an integer n≥0 such that Φ_{-n}(a) belongs to the local null graph. Thus the whole backward basin is contained in the countable union over n of Φ_n(graph).

Each Φ_n is a C¹ diffeomorphism. It is locally Lipschitz, so it maps null sets to null sets, by covering its domain with countably many compact balls and using the elementary Lipschitz image estimate. The basin is null. There are only countably many equilibria, hence the union of these exceptional basins is null.

Section 1 puts every initial point in a backward basin. Section 2 shows Ω=0 in every other basin. Thus Ω=0 almost everywhere. Its continuity implies Ω=0 everywhere.

## 6. Finish and scope

The identities div U=0 and curl U=0 imply ΔU=0 componentwise. Each component is a bounded entire harmonic function and hence constant. For completeness the interior gradient estimate from the mean-value formula is |∇U_i(a)|≤C sup|U_i|/R for every ball B_R(a); send R→infinity to obtain ∇U_i(a)=0. Decay makes each constant zero.

This proves the stated theorem. It does not prove that Z must be countable for a smooth Euler profile. Analyticity alone does not ensure isolated zeros of an analytic vector field. A numerical root finder cannot enumerate an arbitrary continuum or certify the absence of further zeros on R³. Finding finitely many approximate roots therefore does not apply this theorem rigorously to a trained checkpoint.

Nor does this theorem give a universal residual floor for arbitrary approximations. A quantitative floor would require a compactness argument with controlled global tails, derivatives and nontriviality, followed by persistence or certified control of the stagnation structure. No such quantitative estimate is asserted here. The theorem does not justify stopping the full numerical campaign.


## Addendum: sublinear velocity and arbitrary alpha-limit sets

The lead's stronger stated hypothesis U(y)=o(|y|) is also sufficient for the conclusion that U is constant. Uniform sublinear growth supplies |V(y)|<=K(1+|y|), the same outward radial inequality outside a ball, global flow, and compact backward orbits. All vorticity and graph arguments above then apply unchanged: they only require boundedness on each compact backward orbit, not a global bound on U or Ω. At the last step, for each component and every fixed a,

    |grad U_i(a)| <= C R^(-1) sup_{B_R(a)} |U_i| -> 0.

Indeed, for each epsilon>0, |U_i(y)|<=epsilon |y| outside a sufficiently large ball, and the fixed compact remainder contributes O(1)/R. First send R to infinity, then epsilon to zero. Thus U is constant; decay additionally makes it zero.

The lead's Corollary L1' is valid too. With no countability assumption, the compact alpha-limit set lies in Z by section 1. If it avoids E={q in Z:lambda_max(S(q))>=1}, compactness and continuity give one eta>0 and a neighborhood of the entire alpha-limit set with lambda_max(S)<=1-eta. The backward trajectory is eventually in that neighborhood. The direct vorticity energy estimate from section 2 then yields Ω(a)=0. Section 3 gives a negative-real-part eigenvalue of DV at every point of E. The remaining difficulty is controlling basins whose alpha-limit sets meet E; the countable proof does not settle that case in general.
