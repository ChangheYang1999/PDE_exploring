# Concentration at a stationary point in the isotropic Holder realization

Date: 2026-10-20. Independent audit of the compact-support theorem in the lead's fred17 and FINAL_REPORT6.4(v). This proof concerns the specified linear operator between specified Banach spaces. It constructs approximate null sequences, not solutions of the nonlinear equation.

## Statement, spaces and hypotheses

Fix0<sigma<1. Let Omega be a bounded open subset of R2, and K a compact subset of Omega containing a closed ball about P. Let rho,W belong to C^(2,sigma) on an open neighborhood of the closure of Omega, with finite norms on a slightly larger bounded neighborhood, and assume W(P)=0. Let U be the canonical compact-input IPM velocity, the order-zero multiplier

    m(xi)=(xi_1 xi_2/|xi|^2, -xi_1^2/|xi|^2).

The compact-input convention agrees with the prescribed full-plane velocity on admissible parity inputs. Define

    X_K={v in C^(2,sigma)(R2): supp v subset K},
    Y=C^(1,sigma)(closure Omega),
    T v=W dot grad v-v+U[v] dot grad rho.

The norms are the sum of uniform norms of all derivatives up to the integer order and the sigma-Holder seminorms of the top derivatives, with Euclidean distance in the seminorm. X_K is a closed Banach subspace. The conclusion is:

1. T is bounded but not upper semi-Fredholm: it cannot simultaneously have a finite-dimensional kernel and closed range.
2. The same is true after restricting X_K by any fixed finite collection of bounded linear scalar constraints.
3. Adding finitely many bounded scalar output rows and finitely many parameter columns does not restore upper semi-Fredholmness in these same norms.
4. For parity-restricted inputs the construction is valid when K also contains neighborhoods of the reflected stationary points needed by the parity, and the background and operator preserve that parity.

There is no assertion for other graph, anisotropic, weighted or global norms. Bounded Omega is an explicit sufficient realization; an unbounded Omega requires separate uniform mapping assumptions, which are not inferred here from local regularity.

## The compact-input multiplier bound

For every fixed bounded support K and bounded observation set Omega,

    ||U[v]||_(C^(1,sigma)(closure Omega))
       <= C_(K,Omega,sigma) ||v||_(C^(1,sigma)(R2)).       (1)

Here U includes the local term-rho e2/2 in its second component. One must not add that local term a second time to the multiplier. The kernel and multiplier identification are established in the independent propagation-audit proof, Localization section, using the differentiated logarithmic fundamental solution. For completeness, the bound needed here follows directly from that kernel representation. Decompose its zero-mean homogeneous degree-minus-two kernel into smooth annular pieces at scales s. For a compact C^sigma input f, cancellation bounds a scale-s piece, s<=1, by C s^sigma[f]_sigma and its first derivative by C s^(sigma-1)[f]_sigma. In comparing two points distance h<=1, sum the sup bounds over s<=h and the derivative bounds times h over h<s<=1. Both geometric sums are O(h^sigma). At scales s>=1, the compact support gives the L1 bound, and the kernel and its derivatives decay as s^-2 and s^-3. Their sums are bounded by C||f||L1. Apply the same calculation to the first derivatives of v, which commute with U distributionally and remain compactly supported. Since the support is fixed, ||D^j v||L1<=|K| ||D^j v||infinity for j<=1. This proves(1). The local multiplier term is bounded directly. All constants are independent of a shrinking support inside K.

The ordinary product estimate [fg]_sigma<=||f||infinity[g]_sigma+[f]_sigma||g||infinity and the Leibniz rule show T is bounded X_K to Y. Only values of W near K are used in its transport term.

## The approximate null sequence

Choose a nonzero real phi in C_c^infinity(R2), supported in the annulus1<|Z|<4/3. Put

    v_epsilon(X)=epsilon^(2+sigma) phi((X-P)/epsilon).

For sufficiently small epsilon its support lies in K. For j=0,1,2, exact scaling gives

    ||D^j v_epsilon||infinity
       =epsilon^(2+sigma-j)||D^j phi||infinity,
    [D^j v_epsilon]_sigma
       =epsilon^(2-j)[D^j phi]_sigma.                  (2)

At least one second derivative of phi has nonzero Holder seminorm: otherwise its Hessian is constant, and compact support forces phi=0. Thus

    c<=||v_epsilon||X_K<=C,
    ||v_epsilon||C2 ->0,
    ||v_epsilon||C1sigma<=C epsilon.                   (3)

To estimate transport without losing the small value of W at P, use Z=(X-P)/epsilon. On a fixed ball containing the support, set

    A_epsilon(Z)=W(P+epsilon Z)/epsilon.

The identity W(P)=0 and the integral formula

    A_epsilon(Z)=integral_0^1 DW(P+t epsilon Z)Z dt

give uniform C^(1,sigma) bounds on this fixed ball. Indeed, D_Z A_epsilon=DW(P+epsilon Z), whose Holder seminorm is at most epsilon^sigma[DW]_sigma. Multiplying A_epsilon by a fixed smooth cutoff equal to one on the support of phi gives a globally supported function with the same uniform bounds. Consequently

    W dot grad v_epsilon
       =epsilon^(2+sigma)(A_epsilon dot grad phi)(Z),
    ||W dot grad v_epsilon||C1sigma<=C epsilon.        (4)

The fixed cutoff changes no product, because phi and all its derivatives vanish outside their common compact support. Formula(1), the C^(1,sigma) product estimate and rho in C^(2,sigma) give

    ||U[v_epsilon] dot grad rho||Y<=C epsilon.

Together with(3),(4), this proves ||Tv_epsilon||Y<=C epsilon. This estimate does not require rho to solve the nonlinear equation; W(P)=0 is the relevant local degeneracy.

## Why this contradicts upper semi-Fredholmness

Suppose T has finite-dimensional kernel N and closed range. The quotient X_K/N is Banach, and the induced bounded bijection to ran T has bounded inverse by the open mapping theorem. Therefore

    dist_X_K(v,N)<=C||Tv||Y.                           (5)

For epsilon_n decreasing to zero, choose n_n in N within twice this distance (or within an additional epsilon_n if it is zero). The sequence n_n is bounded, so a subsequence converges strongly in X_K because N is finite-dimensional. The same then holds for v_epsilon_n by(5). But strong convergence in X_K implies convergence in C2, whose limit is zero by(3). This contradicts the positive lower X_K norm in(3). Thus T is not upper semi-Fredholm. No exact nonzero kernel vector has been constructed by this argument.

## Arbitrary finite constraints and finite borders

Let ell_1,...,ell_m be bounded linear functionals on X_K. Choose epsilon_n=4^-n, so the annular supports of successive v_epsilon_n are disjoint. In each block of m+1 consecutive indices, the m homogeneous equations

    sum_j a_j ell_i(v_epsilon_j)=0, i=1,...,m

have a nonzero solution. Normalize it by max_j|a_j|=1. Let z_n be that linear combination. Its X_K norm is at most(m+1)C, its C2 norm tends to zero, and ||Tz_n||Y tends to zero, by(3),(4). Its X_K norm is bounded below uniformly: in a bump whose coefficient has modulus1, choose two fixed rescaled points witnessing a positive second-derivative Holder quotient. No other bump is supported at either point, so the quotient is unchanged. The chosen pair can be inside the annulus and its slightly larger annular neighborhood, disjoint from the other supports; compactness and nontriviality of phi ensure such a pair exists. Thus the preceding contradiction applies on the closed constraint subspace.

For finitely many additional bounded output rows, impose their scalar functionals among the ell_i as well. For an enlarged domain X_K times R^p, set the parameter coordinates to zero. The resulting bounded approximate null sequence still has no strongly convergent subsequence. A finite-dimensional kernel and closed range for the bordered operator would again imply(5), now in the enlarged Banach space, yielding the same contradiction. The parameter columns need only be bounded into the chosen target. This is a statement about finite modifications of this specific realization; it does not rule out a different function space or a different operator domain.

## Parity and admissibility of the local directions

For P=(a,0),a>0, choose phi even in its first variable and odd in its second. Form the equal reflected pair about P and(-a,0). This density is even in x and odd in y. For small epsilon the two supports are disjoint, and the same estimates hold with fixed factors. The required support condition is that K contain neighborhoods of both points; merely containing P does not suffice for this symmetric version. The canonical velocity preserves the corresponding velocity parities, so W(-a,0)=0 follows from W(a,0)=0 for a symmetric background. At P=0 one centered bump with the stated parity suffices.

Each bump is smooth, compactly supported and zero near the original center when a>0, so it preserves all center jets. Any further finite continuous linear normalization can be imposed by the preceding block argument. Positivity constraints on nonlinear profiles are not linear subspaces and are not addressed by this operator theorem. Nor does it produce a nonlinear perturbation solving transport.

## Audit verdict and dependencies

The compact-support isotropic theorem in fred17 and the lead report is CONFIRMED in the bounded local realization above. Its proof does not justify a global weighted mapping assertion, an exact kernel, a kernel dimension, a nonlinear family or either task endpoint. For clarity the report may state bounded Omega explicitly and condition the parity sentence on including the reflected support. If C^(2,sigma) near an unbounded closure is read only locally, it is insufficient to define a bounded global target map. That broader interpretation remains outside this confirmation.

Dependencies: the elementary compact-input kernel identity from propagation-audit, the Holder product inequality proved above, basic finite-dimensional linear algebra, completeness of Holder spaces and their closed subspaces, and the Banach open mapping theorem. No interval computation or numerical residual is used in this analytic conclusion. A second-model review and any finite algebra checks are recorded in verification/ and must not be described as a PDE existence proof.
