# High angular modes change a low resonant coefficient

Verifier result 156, written 2026-10-21 before the supporting calculation. The finite coefficient assertions below are to be marked CONFIRMED only after the independently implemented exact computation passes. This result audits the additional claim in external audit22. It does not execute or import that audit's code.

## 1. Statement and hypotheses

For ell=3 put (K,M)=(5,2); for ell=5/2 put (K,M)=(9,4). Let p=1/ell, delta=1-p and s_k=p-k delta. For an odd sine polynomial Theta define P_0=Theta and, for 0<=k<K, define H_k by the particular Poisson inverse of r^(s_k)P_k. Define P_k for 1<=k<=K by the transport recurrence (1) below. Let g[Theta] be the coefficient of sin(M theta) in d_x[r^(s_K)P_K]/r^(s_K-1).

These are finite algebraic definitions for every odd sine polynomial, independent of the existence of any IPM profile. If an exact exterior Setting III profile with symbol bounds S^p has trace Theta, the finite expansion and sector isolation proofs in results142 and150 identify this functional with its first resonant source coefficient. Isolation depends on radial deficits, not on the leading trace having a single angular mode. No profile with a specified Theta is constructed here.

Claim: for every finite angular cutoff L there are an odd N>L and a real epsilon, arbitrarily small and nonzero, such that

    g[sin(theta)+epsilon sin(N theta)] != g[sin(theta)].

Thus g on the space of sine polynomials is not determined by any fixed finite set of leading Fourier coefficients. At N=101, its linear coefficient in epsilon is zero, and its quadratic coefficient is a nonzero rational. Their full exact values are stored in verification/EXACT_CHECKS.json. The residues modulo 1000003 are 668607 at ell=3 and159236 at ell=5/2. These residues are secondary checks; the proof uses the exact nonzero rational values and a rational-function argument.

This assertion concerns the coefficient functional. It does not prove that changing a tail can set g to zero, or that two actual profiles realize the compared traces. It also does not contradict continuity in a sufficiently strong norm of the whole angular trace.

## 2. Exact recurrence and polynomial dependence

For a positive odd sine frequency n,

    d_x[r^s sin(n theta)]/r^(s-1)
      =(s-n)/2 sin((n+1)theta)+(s+n)/2 sin((n-1)theta).

Drop sin(0), and use sin(-n)=-sin(n). If G is this source, the stream coefficient is H_m=G_m/[m^2-(s+1)^2]. For i<K, no positive even integer m satisfies m^2=(s_i+1)^2 in either case, so every division is valid. The zero mode is absent by odd parity, including when s_i+1=0.

The polar advection bilinear form of a stream coefficient H_i and a density coefficient P_j is obtained by summing

    h_m a_n/2 * [( (s_i+1)n-ms_j ) sin((n+m)theta)
               -( (s_i+1)n+ms_j ) sin((n-m)theta)].

With B denoting this expression,

    P_k = [ell k delta]^(-1) sum_(i+j=k-1) B(H_i,P_j).     (1)

The derivative and inverse are linear, and B is bilinear. Induction shows P_k is a homogeneous polynomial of degree k+1 in the input amplitudes. Thus g[sin(theta)+epsilon sin(N theta)] is a polynomial in epsilon of degree at most K+1. To obtain its coefficients up to epsilon^2 it is exact to compute in the quotient ring Q[epsilon]/(epsilon^3). No higher epsilon power can contribute to a lower one.

This recurrence and its relation to the actual asymptotic coefficient were proved in result150. The no-harmonic-overlap argument uses the deficit set {k delta+2l:l=0 or l>=2}; it remains true for any finite angular trace. It identifies g only if an actual profile satisfying the symbol hypotheses exists.

## 3. Frequency bookkeeping and a rational function of N

Expand every sine into signed exponentials for this argument. At epsilon degree e in P_k, there are exactly e high-frequency leaves and k+1-e unit-frequency leaves. A binary interaction contributes a frequency shift of plus or minus1, because the stream source shifts by1 and the polar product adds the two frequencies. It has k interactions. Consequently every density frequency can be written

    aN+b, |a|<=e, |b|<=2k+1-e.

Source and stream frequencies have |b|<=2k+2-e. These are containing bounds; cancellations can reduce support. They follow inductively by adding the bounds for i and j in (1) and accounting for one source shift, with i+j=k-1.

At every step needed for g, k<=K. For N>4K+4, two different pairs (a,b) with |b|<=2K+2 cannot describe the same frequency unless they are the same pair: if a!=a', the equality needs N<=|b-b'|<=4K+4. For a!=0 the sign of aN+b is then the sign of a. Modes with a=0 have their fixed integer frequencies. Thus collection, reflection of negative sine modes, and dropping the zero sine mode have a pattern independent of N throughout this range.

With this fixed finite pattern, the coefficients of the recurrence are rational functions of N: each derivative multiplies by an affine function, each inverse divides by (aN+b)^2-(s_i+1)^2, and sums and products preserve rationality. The excluded zero mode is identically absent, and every inverse at an actual positive even frequency is nonresonant for i<K. None of the denominators used for a nonzero symbolic mode is identically zero. Therefore the quadratic coefficient is one rational function R_ell(N) for all odd N>4K+4.

The independently recomputed value R_ell(101) is nonzero in both cases; 101>4K+4. Hence the numerator polynomial of this rational function is nonzero. It has only finitely many real zeros, as does each nonzero denominator polynomial. There are infinitely many odd integers beyond any prescribed L, so one can choose such an N with R_ell(N)!=0.

At epsilon degree1, |a|=1, because there is exactly one high-frequency leaf. Its resulting source frequency has magnitude at least N-(2K+1)>M in this range. Thus the linear coefficient of the target low mode is zero. This structural statement also holds for every sufficiently large odd N, not merely for101.

## 4. Completing the finite-cutoff claim

Choose an odd N>L with R_ell(N)!=0 as above. The polynomial g[sin(theta)+epsilon sin(N theta)]-g[sin(theta)] has zero constant and linear coefficients and nonzero quadratic coefficient. It is therefore nonzero for all sufficiently small nonzero epsilon: divide by epsilon^2 and use continuity at epsilon=0. The two inputs agree in every frequency up to L. This proves the claim.

The same argument with a nonzero first-mode amplitude A gives a quadratic coefficient A^(K-1)R_ell(N), since the recurrence has amplitude degree K+1. It stays nonzero for every nonzero real A. No smallness norm uniform in N is asserted. In particular, the C^j size of epsilon sin(N theta) includes the factor N^j.

## 5. Independent supporting calculation

The verifier code implements two coefficient algebras independently. The first stores real positive sine modes indexed also by epsilon degree, using the polar formulas in Section2. The second stores signed Laurent coefficients with epsilon degree and obtains advection from Cartesian derivatives. A real sine polynomial is i sum_n D_n exp(in theta), with D_n=-a_n/2 and D_-n=a_n/2. On real coefficient dictionaries,

    X_q: n -> n+1 with (q-n)/2, n -> n-1 with (q+n)/2,
    Y_q: n -> n+1 with (n-q)/2, n -> n-1 with (n+q)/2.

Here partial_x is X_q, while partial_y contributes an extra i and uses Y_q. For stream iS and density iD the advection coefficient after removing i is

    Y_(s_i+1)S * X_(s_j)D - X_(s_i+1)S * Y_(s_j)D.

Ordinary Laurent convolution includes epsilon exponents and drops powers above2. The second code does not evaluate a trigonometric product formula. All intermediate P_k, sources and H_k are compared, and the Cartesian negative Laplacian is checked. Its constant coefficient is compared with the already independently checked result150; its quadratic coefficient is compared with the frozen external rational. Agreement verifies finite algebra, not the existence of an exterior or full-plane solution.

## 6. Dependencies and verdict

Dependencies: result150's recurrence and radial isolation; result142's conditional finite-depth expansion only when interpreting g for an actual profile; elementary finite Fourier algebra and the fact that a nonzero polynomial has finitely many roots. The functional statement itself needs no asymptotic existence assumption.

CONFIRMED only after the exact gate passes: no fixed finite Fourier cutoff determines this functional. OPEN: whether another trace cancels its resonant source, whether such a trace is realized by an exact profile, and the principal Setting III endpoint.
