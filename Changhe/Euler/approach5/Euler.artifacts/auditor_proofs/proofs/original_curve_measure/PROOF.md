# An invariant incoming-curve measure retaining the original target

## Exact statement

Let f:R^m->R^m be a C-infinity diffeomorphism with bounded derivatives of every positive order and bounded derivative of f^(-1). Let K be compact with f(K) subset K. Let D0 be a straight compact embedded arc in K, and G0 a measurable positive-length subset such that limsup_N N^(-1)log J_(f^N)(x)>=lambda_0>0 for every x in G0, where J is the tangent arclength Jacobian along D0.

There exist a restricted arc D, G=G0 intersect D of positive length, a compact positive-length E subset G, an integer p>=1 and g=f^p, with a nonzero finite g-invariant measure mu supported in K. There is a finite joint measure theta on pairs (gamma,x), with x on gamma, whose x marginal is mu. Its curve marginal is q, and

    theta << q(dgamma)lambda_gamma(dx),

where lambda_gamma is normalized arclength. The curves are embedded, nonconstant and C^(r-1,1) for one fixed integer r>=3. This regularity denotes a Lipschitz derivative of order r-1, not convergence in its Lipschitz norm.

There are increasing finite joint measures theta^M tending to theta, with marginals mu^M tending to mu. For every fixed integer M>=0, q^M-almost every gamma is a C1 limit of original image curves g^(ell_j)(P_j), ell_j->infinity, parametrized by the affine tree. Each P_j contains a point of E; the image lengths lie between v_M>0 and 2epsilon; restricted-iterate arclength distortion is less than two; and length(P_j intersect G)/length(P_j)->1. For all k>=0,

    diameter(g^(-k)gamma)<=2epsilon 100^(-k),
    ||(g^(-k)gamma)'||_infinity<=epsilon 100^(-k).

Every positive-mu-measure Borel alternative is seen by some finite M. A full-mu-measure generic and Oseledets-regular set is full for that partial measure as well. Generic points on the same incoming curve have the same g-ergodic component. At every two-sided regular point, the nonzero curve tangent has backward contraction rate at least log100.

This theorem constructs an incoming-curve measure. It does not assert full unstable dimension, SRB physicality, vortical localization or coverage.

## 1. Parameters, original density and finite selected sets

Apply A306, choosing r>=3 and fixing p, epsilon, a restricted straight D and its A305 interval tree. These parameters can be fixed before a later positive-length restriction of G. The normalized arclength lambda on D is a constant multiple of parameter length. Its nested partition atoms have lengths tending uniformly to zero.

For almost every x in G, the fraction of G in the atom P^ell(x) tends to one. Indeed the ordinary density theorem applies to any interval containing x whose length tends to zero: its complement fraction is at most twice that in the centered interval of twice its length. Remove partition boundaries, a countable null set. Egorov and inner regularity give a compact positive-length E subset G on which these fractions tend to one uniformly.

The final selection step of A306 now applies to this E with the same tree. For infinitely many n it supplies E_n subset E with m_n=lambda(E_n)>=1/(2n^2), and every point of E_n visits at least beta n large hyperbolic atoms by time n. Set eta_n=lambda|E_n/m_n. Call an atom good when it is large and contains a hyperbolic witness. This is an atom property; the witness need not be every point in the atom.

## 2. Original parents and joint measures

For window M and time 0<=ell<n, select an entire depth-ell parent P if it contains y in E_n whose good descendant occurs at depth ell+i for some 0<=i<=M with ell+i<=n. Discard zero eta_n-weight parents. Let gamma_(ell,P) be its normalized image parameterization. Let rho_(n,ell,P) be the pullback to [-1,1] of the conditional image probability (g^ell)_*(eta_n|P/eta_n(P)). Define

    p_n^M=(1/n)sum_(ell,P selected) eta_n(P) delta_(gamma,rho).

Push this measure forward by (gamma,rho)->delta_gamma times gamma_*rho to obtain theta_n^M; let mu_n^M be its x marginal. All masses are at most one. At window zero their mass is at least beta-1/n, since at most the good time n is omitted from the average. Enlarging the window adds terms with unchanged weights, curves and conditional probabilities. Thus these finite measures increase with M.

All curves lie in K and have the common C^r bounds from A305. Their C^(r-1) closure is compact and is also a compact C1 class. For each M, take a weak limit of p_n^M, and choose a common diagonal subsequence for all integers M. Continuity of evaluation gives the limits theta^M and mu^M; positivity shows their monotonicity in M.

## 3. Every fixed window has a deterministic length lower bound

Put L_M=max(1,||Dg||_infinity^M) and v_M=epsilon/(2L_M). A selected parent P has a good descendant Q at depth ell+i, i<=M. The latter image has length at least epsilon/2. Lipschitz continuity gives

    epsilon/2<=length(g^(ell+i)Q)
       <=L_M length(g^ell Q)<=L_M length(g^ell P).

Hence every selected image curve has length at least v_M, individually. C1 continuity of length passes this lower bound to q^M-almost every limiting curve.

The bounded-curve derivative inequality also passes to the limit. Its maximum speed is at least v_M/2, while its minimum speed is at least (1-2eta)v_M/2. Projection onto a maximal-speed tangent direction is strictly increasing, since the tangent vector varies by at most 2eta times the maximum speed. Thus every such limit is regular and embedded. Its arclength has no atoms.

## 4. Absolute continuity of the incoming measure

Apply A257 separately for each fixed M. Its original partitions are the nested A305 partitions; its selected collections contain whole parents. The entropy cost satisfies log(1/m_n)<=log2+2log n. Choosing N_n=floor(sqrt(n)) gives N_n/n->0 and N_n log(1/m_n)/n->0. The image of normalized original arclength on a selected parent is bounded above by twice normalized image arclength, by the uniform iterate distortion. Every depth-(ell+N) descendant has time-ell image diameter at most 2epsilon 100^(-N). The selected curves belong to the compact C1 class and have lengths bounded below by v_M. These are exactly A257's hypotheses, so

    theta^M << q^M(dgamma)lambda_gamma(dx).

This step uses a proved finite relative-entropy lemma, not a reparametrization or existence theorem from the measured-disk preprint.

Take the bounded increasing limits p, theta, mu and q as M tends to infinity. Their common mass is between beta and one. Each q^M is supported on nonconstant curves, so q is too. Since q^M<=q, each theta^M is absolutely continuous with respect to q(dgamma)lambda_gamma(dx). The increasing limit theta retains that property.

## 5. Invariance from the exact existential witness rule

If a time-ell parent with ell>=1 is selected for window M, its time-(ell-1) ancestor is selected for window M+1. The same original witness works, and its future good descendant is now at most M+1 steps ahead. This implication concerns every sampled point in the current selected parent, whether or not it is the witness.

For every nonnegative continuous phi,

    integral phi d(g_*mu_n^(M+1))
       >= integral phi dmu_n^M-||phi||_infinity/n.

The missing term is only time zero. Pass first to the common n subsequence and then to increasing M. The result is g_*mu>=mu. Both sides have the same finite total mass, hence are equal. The support is contained in K and therefore in its maximal invariant part. No unsupported domination by phase images of the window-zero measure is used.

## 6. Original approximants and backward contraction

For each fixed L, the total finite measure contributed by times ell<L is at most L/n. Thus it disappears in the limit. For a curve in the support of q^M, take shrinking C1 neighborhoods. Each has positive limiting measure; the portmanteau lower bound shows that a sufficiently late finite measure has mass there contributed by arbitrarily large ell. Choose a positive-weight original parent from each such neighborhood. This yields original image curves converging in C1 with ell_j->infinity.

Every chosen parent meets E_n subset E. Because the atom containing every point of E has uniformly asymptotic G density, the required original fraction tends to one. This uses the retained original E, not weak convergence of the image measures.

Fix k. For ell_j>=k, g^(-k)gamma_j is a restriction of the depth-(ell_j-k) bounded small curve with additional affine slope at most 100^(-k). A305 gives its derivative and diameter bounds. Composition with g^(-k) preserves C1 convergence on the compact region for this fixed k. Passing to the limit proves the bounds in the statement. The countably many k can be retained simultaneously. The limit curves and all their negative iterates lie in K, since the corresponding finite-time images do.

The positive minimum-speed estimate implies

    ||Dg^(-k)(gamma(t)) gamma'(t)/|gamma'(t)||
      <=[2epsilon/((1-2eta)v_M)]100^(-k).

At a two-sided Oseledets-regular point the tangent therefore belongs to the sum of spaces with forward exponents at least log100. This does not claim a lower bound on all positive exponents of g.

## 7. Alternatives and ergodic components

If mu(Z)>0, monotone convergence gives mu^M(Z)>0 for some finite M. Since mu^M<=mu, every full-mu-measure set is full for mu^M. Disintegration and incoming absolute continuity give a curve carrying positive arclength of the chosen alternative intersected with the simultaneous generic and regular set. A positive-length portion can be confined to a regular compact subarc and a uniform Pesin block by countable restriction.

For any x,y on the same incoming curve, backward distances tend to zero exponentially. Uniform continuity of a continuous test on K makes its backward orbit values asymptotic, so their backward Cesaro limits agree whenever they exist. A countable dense set of continuous tests identifies the ergodic-component probability at simultaneous two-sided generic points. Hence all such points on one curve have the same component label. Disintegrating by that measurable label preserves the incoming arclength absolute continuity. No ergodic component needs to be an atom in the global ergodic decomposition.

## Application and limits

For the cutoff backward carrier flow in LIT41, f is a compactly supported smooth time-one map, so all bounded-jet hypotheses hold. In a positive-volume vortical target the bracket and determinant estimate give a positive upper operator exponent. Since ||Df^N||<=sqrt(m) max_i |Df^N e_i|, finitely many fixed coordinate directions suffice to select one direction with positive upper exponent on a positive-volume subset. Fubini inside a box contained in the vortical open set and the trapping ball gives a straight original arc and positive-length target of the stated kind. Null exceptions can be removed before applying the theorem.

This confirms the entire elementary original-curve output at C-infinity regularity. Turning it into full unstable conditionals for a three-dimensional flow, excluding irrotational components, capturing the original target in a physical basin and deducing almost-everywhere coverage are separate arguments. The present theorem makes no C2 assertion and gives no helicity sign or Euler nonexistence conclusion.

## Verification evidence

Dependencies: A305, A306, A257, ordinary weak compactness and disintegration, Birkhoff and Oseledets theory. No theorem of the 2026 measured-disk source is used. The source submission and SHA256 hash are retained in the team records. All finite-time premises were checked against their exact stated forms; no computation or formalization was needed.
