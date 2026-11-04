# First nonzero vorticity jets and their spectral resonances

Status: CONFIRMED in A441 after independent reconstruction and focused configured-model review. This audits LIT92, including its profile-dependent analytic compactness refinement. It is a necessary spectral theorem, not a nonexistence result.

## 1. Statement with exact regularity

Fix an integer k>=1, 0<c<1/2 and any real omega. On an open subset of R3 let U be C^(k+1), P be C1, div U=0, and suppose

    (1-c)U+B.grad U+omega JU+grad P=0,
    B=(cI-omega J)y+U, W=curl U.

Let K be compact, invariant under the whole B flow, with every orbit in K defined for all real time. Write Psi_t for the backward carrier flow. Let mu be an invariant probability on K, ergodic for the whole flow. Suppose that mu-almost everywhere

    B!=0, D^j W=0 for 0<=j<k, D^k W!=0.                       (1)

All derivatives are ambient Cartesian derivatives. Set

    a=1-2c, kappa=1+c, d=3c.

The three ambient backward Lyapunov exponents are simple and have the form

    (lambda,0,-d-lambda), lambda>0.                            (2)

Moreover lambda belongs to the union of these two finite lists, with m an integer:

    F_(k,m)=[kappa+(k-m)d]/(2m-k),
        0<=m<=k, 2m>k;
    T_(k,m)=[kappa+(k-m-1)d]/(2m-k+1),
        0<=m<=k, 2m>k-1.                                    (3)

These are necessary values; no realization of every value is asserted. In particular,

    a/(k+1)<=lambda<=kappa+floor((k-1)/2)d.                    (4)

The first three sets are

    k=1: {a/2,kappa},
    k=2: {a/3,kappa/2,kappa},
    k=3: {a/4,kappa/3,kappa/2,kappa+d}.

The entropy of the time-one map is zero. Ergodicity of that map is not required. This conclusion concerns full derivative-cocycle exponents, not eigenvalues of -DB at individual nonstationary points.

If U is smooth, a whole-flow-ergodic probability with B!=0 and W=0 almost everywhere either satisfies (1) for some finite k, or gives full measure to points at which every finite derivative of W vanishes. If W is real analytic and not identically zero on the connected open domain containing K, the flat alternative is impossible. In that analytic case, compactness gives a finite upper bound for k depending on this particular profile and K. There is no bound uniform over profiles and no conclusion for measures supported on B=0.

## 2. Differentiated Cauchy law, including the lower-order terms

The momentum equation gives grad P in C^k, so the assumed C1 pressure is in fact C^(k+1). Curling is therefore legitimate. The curl equation is [B,W]=-kappa W. Let A_t=D Psi_t. The exact Cauchy law is

    W(Psi_t x)=exp(kappa t)A_t(x)W(x).                        (5)

Let Sigma_j be the common zero set of D^ell W for 0<=ell<=j. The invariance of Sigma_0 follows from invertibility of A_t. Inductively, differentiate (5) j times at a point in Sigma_(j-1). On the left, every chain-rule term other than the j-th derivative of W evaluated on j copies of A_t contains a derivative of W of order below j. On the right, every term differentiating A_t at least once contains a derivative of W of order below j. All these terms vanish. Thus, for T=D^k W at a point in Sigma_(k-1),

    T_(Psi_t x)[A_t v1,...,A_t vk]
        =exp(kappa t)A_t T_x[v1,...,vk].                    (6)

The same identity at every lower order proves invariance of Sigma_j. C^(k+1) regularity of the carrier supplies derivatives through order k+1 of its finite-time flow, exactly those needed to differentiate A_t k times; W is C^k. For any fixed finite time, compactness of K gives a neighborhood on which these derivatives exist. No complete surrounding-domain flow is assumed.

Since D^(k-1)W is identically zero along the whole orbit of x in (1), differentiating this zero tensor along that orbit yields

    T_x[B(x),v2,...,vk]=0.                                   (7)

Symmetry gives the same conclusion in every argument slot. Using Cartesian components avoids any derivative of a chosen frame. Ergodicity turns invariance of the Sigma_j into the zero-or-one alternatives used in Section1.

## 3. Two-sided boundedness and the tensor resonance

On K, A_t and A_t^(-1) are bounded uniformly for |t|<=1. The two-sided multiplicative ergodic theorem therefore applies to the derivative cocycle and every finite tensor construction used below, with its logarithmic integrability premises satisfied. The source and exact relevant statements are pinned and checked in the team records: Filip, Notes on the Multiplicative Ergodic Theorem, arXiv1710.10694v1, Theorem2.2.6, invertible Variant2.2.10 and Section3.1.1. We use the theorem componentwise for a possibly nonergodic time-one map.

Equation (6) says that T is a bounded section transported by the tensor cocycle

    C_t T=exp(kappa t) A_t T (A_t^(-1),...,A_t^(-1)).

A block with input exponents lambda_1,...,lambda_k and output exponent eta has exponent

    rho=kappa+eta-sum_j lambda_j.                             (8)

The minus sign for each input is the inverse dual tensor factor. T(Psi_t x) remains bounded for positive and negative t because T is continuous on compact K. At a two-sided regular point the Oseledets projections are tempered. If T had a component with exponent rho>0, its positive-time exponential growth would exceed the subexponential projection of a bounded total tensor. A component with rho<0 is excluded at negative times. Grouping blocks with the same exponent handles multiplicities. Consequently every nonzero block has rho=0, giving

    sum_j lambda_j-eta=kappa.                                (9)

Neither an integrability assumption on log|T| nor an inverse of T is used. Vanishing or small tensor norms at other points cause no problem.

The carrier vector satisfies A_t B(x)=B(Psi_t x) and is bounded both ways. If nonzero it lies in the zero-exponent space by the same argument. Also div(-B)=-d gives det A_t=exp(-dt), so the sum of all three exponents is -d. The exponents and regular splitting can be taken invariant under the whole flow: fixed-time conjugacies have bounded derivatives and inverses on K, and bounded unit-time pieces bridge continuous and integer time. Whole-flow ergodicity therefore makes the spectrum constant almost everywhere, even if the time-one decomposition is nontrivial.

## 4. Exhausting all possible tensor blocks in dimension three

There is at least one zero exponent. If zero had multiplicity two, the remaining exponent would be -d. Every input sum in (9) would be nonpositive; subtracting the output could add at most d. But kappa>d, a contradiction. Three zero exponents contradict the determinant. Thus zero is simple and its line is R B.

If both remaining exponents were negative, each would be strictly between -d and zero. Again every input sum is nonpositive and subtracting an output adds less than d, contradicting (9). Thus there is one positive lambda and one negative eta=-d-lambda, proving (2). Equation (7) removes every block with an input from the zero line.

Let exactly m inputs be from the positive line and k-m from the negative line. Their sum is

    m lambda+(k-m)eta=(2m-k)lambda-(k-m)d.                  (10)

There are three possible outputs.

For output zero, (9)-(10) give

    (2m-k)lambda=kappa+(k-m)d.

The numerator is positive, so the denominator must be positive. This is exactly F_(k,m).

For output eta, they give

    (2m-k+1)lambda=kappa+(k-m-1)d.

The numerator is at least kappa-d=a>0, including m=k. Again positivity specifies exactly the index range in T_(k,m).

For output lambda, they give

    (2m-k-1)lambda=kappa+(k-m)d.

The denominator must be positive. Algebraically this number equals T_(k,m-1). The index m-1 lies between 0 and k and satisfies 2(m-1)>k-1. Thus the third list adds no numbers to (3). The folding is an equality of rates. The divergence identity in fact ties every positive-output block to a negative-output block of the same rate. To see this, take an adapted basis (e_plus,e_flow,e_minus) and its dual, and contract one input with the output in D^(k-1)(div W)=0. For a fixed remaining multi-index with m-1 positive and k-m negative inputs, the flow-input term vanishes by (7), leaving T^plus with m positive inputs plus T^minus with m-1 positive inputs equal to zero. Thus either both coefficients vanish or both are nonzero, and their rate is T_(k,m-1). The all-positive-input negative-output block and flow-output blocks are not constrained by this trace. This relation changes no number in the necessary list and makes no claim of Euler realizability.

## 5. Bounds and the first three orders

Treating m momentarily as real where the denominators are positive, differentiation of F gives the negative numerator -2kappa-kd. Differentiation of T gives -2kappa-(k-1)d. Thus each list decreases as its integer index increases.

Their smallest values are F_(k,k)=kappa/k and T_(k,k)=a/(k+1). The latter is smaller because a<kappa and k+1>k.

If k=2n+1, the first allowed index in both lists is m=n+1. Their maximum values are respectively kappa+n d and [kappa+(n-1)d]/2. The former is larger, also at n=0, where the latter is a/2. If k=2n, the first F index is n+1 and the first T index is n. Their maxima are [kappa+(n-1)d]/2 and kappa+(n-1)d. This proves the upper bound (4). Substituting k=1,2,3 and deleting repeated entries gives the displayed low-order sets. These are exact formulas for arbitrary c in the stated interval; no sampling or numerical extrapolation is used.

## 6. Entropy and the analytic refinement

The confirmed A089 theorem applies to C^r carrier fields with r>=2 and C^(r-1) W satisfying the bracket law on a compact full invariant set. Any ergodic backward time-one measure of positive entropy supported on W=0 must have every derivative D^j W zero almost everywhere for j<=r-1. Here r=k+1, so its conclusion conflicts with D^k W!=0.

For clarity, A089 first selects the least nonzero tensor order. Its Cauchy law forces some nonzero tensor input along the one-dimensional backward unstable direction. A scalar component of D^(k-1)W then has nonzero derivative along that direction, so its common zero set is locally discrete on each unstable leaf. Conditional probabilities on those leaves are atomic. Their n-step information is bounded by the negative logarithm of the point mass, independent of n; the unstable entropy identity and Birkhoff imply zero entropy. Its complete proof and actual Ledrappier-Young source check have been reread. It allows the zero flow exponent and uses C2 dynamics, with no physical-basin assumption.

Decompose the present mu into time-one ergodic components. The full-measure conditions (1) remain true for almost every component. A089 excludes positive entropy for each of those components. Nonnegativity and affinity of entropy give h_mu(Psi_1)=0. A cutoff and compactification outside a neighborhood of K provide the compact-manifold setting without changing the flow or derivatives on K. The divergence identity is needed only there.

At finite regularity U in C^r, r>=2, only k<=r-1 is available: either (1) holds for such a k or every accessible D^jW, j<=r-1, vanishes almost everywhere, with no spectral conclusion in that remaining case.

In the smooth case the invariant sets Sigma_j are decreasing. If their intersection has full measure, every finite jet vanishes almost everywhere. Otherwise some Sigma_j has measure less than one, hence zero by ergodicity. Taking the least such j gives (1), since Sigma_0 has full measure under the zero-vorticity assumption.

For real analytic W on a connected domain, vanishing of all derivatives at one point makes W vanish on a neighborhood and then throughout that domain. If W is not identically zero, for every x in K at least one finite derivative is nonzero at x. Its continuity preserves nonvanishing on a neighborhood. Compactness extracts finitely many such neighborhoods, and the maximum derivative order used supplies a finite k_K. Thus, for this fixed analytic profile and K, only finitely many orders and rates in (3) can occur. This observation supplies no estimate of k_K in terms of c or omega, no uniform bound for varying profiles, and no information about equilibrium measures.

## 7. The exact realized family and remaining global scope

The independent hand proof in the team records establishes the explicit LIT92 family (1) there for every integer k>=1 and every real omega. For omega!=0 its nonstationary compact orbit has first nonzero vorticity derivative of order k and spectrum (kappa/k,0,-d-kappa/k). Thus at least this member F_(k,k) of (3) is genuinely realized by local Euler, with full momentum and the actual curl relation checked.

The same proof records the axis singularity, polynomial growth, incomplete off-circle trajectories and whole-germ obstruction from A014. A separately proposed global helicity-free rank filter is proposed to exclude these particular finite jets under the stated closure-of-vorticity premise, pending focused review. These local realizations do not show that any listed rate occurs in an entire decaying profile. They also do not cover arbitrary rates, every tensor order uniformly, the infinitely flat case or equilibria.

For the C2 baseline, only k=1 is available and its kappa alternative still exceeds 2a when 2/5<c<1/2. The value kappa also occurs in the k=2 list, so C3 regularity alone does not remove that possible rate even when DW=0 almost everywhere. At higher regularity the list is useful structure, but the upper bound in (4) increases with k. No removal of the extra componentwise growth hypothesis follows. All results hold for arbitrary finite omega through the exact bracket identity; no rotation limit or symmetry restriction is used in the necessary spectral theorem.

No new computation was required. The general identities and integer lists were derived by hand, independently of the submitted proof, then compared against it. Source copies, dependencies and hashes are in the team records.
