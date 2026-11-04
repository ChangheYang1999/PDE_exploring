# Coupled continuation: exact primary-source scope

## 1. Statements and reading coverage

Write partial=(partial_x-i partial_y)/2 and dbar=(partial_x+i partial_y)/2. All norms of matrices below are Euclidean or the induced operator norm as indicated. A domain is connected and open. Infinite L2 order at z means integral_B_r(z)|u|²=o(r^m) for every m>=0.

The following source statements are checked at their stated scope:

1. Pan and Zhang, arXiv:2203.04346v1, Theorem1.1: u in H1_loc(Omega;C^N), Omega in C, |dbar u|<=A|u| a.e., A in L2_loc, and infinite L2 order at one point imply u=0. In higher complex dimension their Theorem1.3 asserts continuation from an open zero set. Their Theorem4.1 concerns a smooth scalar complex function with the special potential C/|z|.
2. Coffman and Pan, arXiv:1102.2462v1, Example3.2 and Theorem4.1: a smooth map u from a disk in C to C² has an isolated infinitely flat zero and satisfies dbar u=Q partial u with continuous Q, smooth off zero, and |Q(z)|<=C|z|^(-2)exp(-1/|z|). Q is not Lipschitz in any neighborhood of zero. The header is dated2011; the retained manuscript's internal date is2021.
3. Coffman, Pan and Zhang, arXiv:2402.15503v2, Theorem1.3: a locally Lipschitz u:Omega in R^n -> R^M satisfying |grad u|<=A|u| with A in L^n_loc, n>=1, vanishes identically if it has one zero. For H1_loc regularity Theorem1.1 requires n>=2 and infinite L2 order.

The complete12-page Pan-Zhang and21-page Coffman-Pan manuscripts have been read. For the gradient paper the introduction, complete proof of Theorem1.1, all of Section3 through Corollary3.11, and Section4 through the discussion after Theorem4.2 have been read. Theorem2.6, Theorem2.7 and the remaining complex applications have not been independently audited. Three decisive primary pages were also inspected as images. All four submitted scope sections were read. Retained copies and hashes are in verification. This pass is an offline primary-source audit, not a claim of fresh online retrieval.

## 2. Why the critical dbar proof closes

For positive A in L2(C), the weighted Riesz estimate is

    ||I1 f||_L2(A) <= C ||A||_2 ||f||_L2(1/A).

Here I_alpha has kernel |z|^(alpha-2), with immaterial positive normalization constants. A proof is obtained by splitting I_(1/2)g at radius delta. The inner part is bounded by C delta^(1/2) Mg and the outer part by C delta^(-1/2)||g||_2. Set delta=1/A(z), square, multiply by A and integrate. The L2 maximal inequality gives a bound C(1+||A||_2)||g||_2. Rescaling A by a positive constant and optimizing gives ||I_(1/2)g||_L2(A)<=C||A||_2^(1/2)||g||_2. Duality followed by composition of the two fractional integrals gives the displayed estimate.

For a compact H1 function w supported away from zero, the Cauchy formula and its zero moments imply

    |w(z)|/|z|^m <= pi^(-1) I1(|dbar w|/|z|^m)(z)

for every positive integer m. Indeed 1/(z-zeta)+sum_(l=0)^(m-1) z^l/zeta^(l+1)=z^m/[zeta^m(z-zeta)], and the added integrals vanish because w is zero near0. The formula extends from smooth functions by H1 approximation and local boundedness of the Cauchy operator.

Choose a small radius r, an outer cutoff eta equal to1 on D_r and zero outside D_(2r), and an inner cutoff psi_epsilon vanishing on D_epsilon and equal to1 outside D_(2epsilon). Replace A by A 1_(D_r)+epsilon0/(1+|z|²), with epsilon0>0 small. The replacement has arbitrarily small L2 norm and a positive lower bound on D_(2r). The original differential inequality is needed only on D_r. Applying the weighted estimate to w=psi_epsilon eta u and choosing the norm small enough absorbs the inner A|u| term. For fixed m, the inner-cutoff error is at most C_m epsilon^(-2m-2) integral_D_(2epsilon)|u|², which tends to0 by infinite order. Fatou then gives

    integral_D_r |u|² A/|z|^(2m)
       <= C integral_(D_(2r) minus D_r) |dbar(eta u)|²/[A |z|^(2m)].

Multiplication by r^(2m), restriction on the left to D_(r/2), and m->infinity force u=0 there. The right side is finite by H1 regularity and the lower bound on A. Small-ball absolute continuity on compact subsets lets the same argument propagate the open zero set across its boundary; connectedness gives global zero.

A printed sentence on page6 says that the truncated coefficient still gives the original differential inequality on D_(2r). It only guarantees it on D_r. The proof just given uses exactly D_r, so no theorem is lost. Universal constants must also be reselected after squaring an operator bound and expanding a sum. No sharp constant is claimed.

For a smooth real vector v, set u=partial v. Then |u|=|grad v|/2 and dbar u=Delta v/4. Thus the real-vector Laplacian consequence follows when |Delta v|<=A|grad v|, A in L2, and v is smooth and flat. Flatness passes to all derivatives in this smooth category. This argument is not a proof of the full H2 version's derivative-flatness step, which is separately attributed to the cited theorem. For complex v the identity |partial v|=|grad v|/2 fails. No such unmodified complex reduction is used here.

## 3. The continuous principal-matrix counterexample

Here are enough details to verify both existence and the decisive regularity distinction. Let r_n=1/log(n+1), p_n=n², Delta_n=r_n-r_(n+1), and F_1=1,

    F_n=log(n+2)^(2n-2) F_(n-1).

Take a smooth nondecreasing cutoff s on[0,1], equal to0 near0 and1 near1, with s(1/2)=1/2, s'(1/2)=2, s''(1/2)=0. Put chi_n(z)=s((|z|-r_(n+1))/Delta_n). Work on the disk |z|<r_2, using n>=2. On r_(n+1)<=|z|<=r_n for even n define

    u1=F_n z^(n²),
    u2=chi_n F_(n-1)z^((n-1)²)+(1-chi_n)F_(n+1)z^((n+1)²),

and interchange the components for odd n. The formulas agree on overlapping boundary collars, so the field is smooth off0. Set u(0)=0. One component on each annulus is an exactly nonzero holomorphic monomial, so u and partial u do not vanish off0.

For every fixed derivative order k, differentiation of chi gives a bound C_k |z|^(-2k) Delta_n^(-k). The product rule consequently bounds all order-k derivatives by constants times the three neighboring monomial quantities. They tend to0 because

    F_(n+1)(n+1)^(2k) r_n^((n+1)²-4k)/(Delta_n/r_n)^k ->0.

To verify this limit, Delta_n/r_n is comparable to1/[n log(n+2)]. The upper bound obtained by substituting this estimate has successive quotient at most a constant times

    [log(n+4)/log(n+2)]^(2n+2+k)
      ((n+2)/(n+1))^(3k) / log(n+2),

which tends to0. The ratio of Delta_n/r_n to Delta_(n+2)/r_(n+2) is bounded, so the two neighboring terms obey the same estimate. Extension by zero has every derivative equal to0 at0. This proves smooth flatness, not merely flat function values.

The holomorphic component bounds |partial u| from below. Direct differentiation and the recurrence for F yield

    |dbar u|/|partial u| <= C log(n+2)²/n
                         <= C |z|^(-2)exp(-1/|z|).

Define the rank-one matrix

    Q=(dbar u)(partial u)^*/|partial u|² off0, Q(0)=0.

Then Q partial u=dbar u and ||Q||=|dbar u|/|partial u|. Q is continuous, smooth off0 and flat in value. For sufficiently small radius ||Q||<1. At every nonzero real covector the two Cauchy-Riemann symbols have equal modulus, so a Neumann-series estimate makes dbar-Q partial elliptic. No derivative bound on Q follows.

One can also verify its failure of Lipschitz regularity without inferring it from flatness. At the annular midpoints x_n=(r_n+r_(n+1))/2 for even n, put ell=log(n+2) and D=partial u1(x_n)>0. The monomial ratios are

    F_(n-1)x_n^((n-1)²)/D ~ 1/n²,
    F_(n+1)x_n^((n+1)²)/D ~ 1/(n² ell²),

since ell x_n=1+1/(2n ell)+o(1/(n ell)). Also chi_z=chi_dbar~n ell² and chi_zdbar~n ell³/2 at these points. Hence, with all displayed quantities real there,

    dbar u2/D ~ ell²/n,
    partial u2/D ~ ell/2,
    partial dbar u2/D ~ n ell³,
    dbar²u2/D=O(ell³/n),
    [partial²u2-(n²-1)partial u2/x_n]/D=O(n ell³).

These follow by the product rule; in the last line the leading n^4 monomial contributions cancel. Differentiating Q22 leaves three terms: one with dbar²u2, one with the bracketed difference, and

    -(dbar u2)(conjugate(partial u2))²(partial dbar u2)/|partial u|^4.

The first is O(ell³/n), the second O(ell), and the last is asymptotic to -4 ell³. Therefore dbar Q22(x_n)/ell³ -> -4. Its derivatives are unbounded in every neighborhood of0, which excludes Lipschitz regularity there. This independent asymptotic agrees with the source's lower bound by a positive multiple of x_n^(-3).

This is a system with two complex, hence four real, unknowns. It satisfies no asserted Euler pressure, homogeneity, helicity or rank equation. Its continuous, small principal coupling cannot be silently replaced by a smooth or Lipschitz coefficient example.

## 4. A complete proof of the locally Lipschitz gradient criterion

First let phi be Lipschitz on[0,1], phi(0)=0, and

    |phi'(t)|<=lambda(t)|phi(t)|t^((1-p)/p),
    lambda in L^p(0,1), p>=1.

Replace lambda by lambda+1. Let delta be the largest endpoint of an initial interval on which phi=0. For x>delta, the fundamental theorem and Holder give

    |phi(x)|^p <= x^(p-1) integral_delta^x |phi'|^p.

Multiply by lambda(x)^p x^(1-p), integrate from delta to s, and use the differential inequality. With

    J(s)=integral_delta^s lambda(x)^p |phi(x)|^p x^(1-p) dx,

one obtains J(s)<=J(s) integral_delta^s lambda^p. J(s) is finite: Lipschitz regularity gives |phi(x)|<=Cx at zero. If delta<1, continuity gives arbitrarily close s>delta with J(s)>0. Absolute continuity of the Lp integral contradicts the last inequality. Thus phi=0.

Now take a locally Lipschitz real vector u on a ball B centered at one of its zeros. Almost every radial line avoids the null set of nondifferentiability and satisfies integral_0^r A(t theta)^n t^(n-1)dt<infinity by polar Fubini. Its vector restriction is Lipschitz, and the scalar restriction |u| is Lipschitz with derivative bounded by |grad u| wherever needed, almost everywhere. Set lambda(t)=A(t theta)t^((n-1)/n) and p=n, with harmless radius scaling. The preceding one-dimensional result makes u zero along almost every radial line. Continuity makes it zero on B. This proves that its zero set is both open and closed, and thus proves the theorem on a connected domain. For n=1 use the same lemma with p=1 directly.

For the H1 infinite-order version, the source's separate Hardy proof is consistent: for lambda>n/2,

    integral |w|²/|x|^(2lambda)
       <= 4/(2lambda-n)² integral |grad w|²/|x|^(2lambda-2).

It follows by integrating div(x|x|^(-2lambda)|w|²) and Cauchy-Schwarz, then density. Consequently the gradient of w/|x|^(lambda-1) is bounded in L2 by a uniform constant times the weighted gradient for all sufficiently large lambda. Sobolev and small ||A||_Ln on a ball absorb the potential term. An inner cutoff error is bounded by C epsilon^(-2lambda) integral_B_(2epsilon)|u|² and vanishes. The outer annulus then bounds the weighted interior gradient independently of lambda, forcing grad u=0 on the half ball as lambda grows; flatness forces that constant to be0. In dimension2 the dbar theorem of Section2 supplies the result. No Lipschitz point-zero conclusion is inferred at mere H1 regularity.

## 5. The logarithmic-gradient obstruction and a printed domain error

Let f be real locally Lipschitz, and let z be a relative boundary point of its zero set in a domain in R^n, n>=2. For every neighborhood U of z,

    integral_(U intersect {f!=0}) |grad f/f|^n = infinity.

If the integral were finite on a small ball, set g=f² and define A=2|grad f/f| off the zero set and0 on it. The function g is locally Lipschitz, differentiable with zero gradient at every zero, and satisfies |grad g|<=A|g| almost everywhere. Section4 would make g vanish on that ball, contradicting the boundary-point assumption. This is exactly Theorem3.7 with Remark3.8, and its proof needs no Euler equation or flatness.

A distinct statement in the same manuscript, Theorem4.2 as printed on page16, is false with its literal punctured-domain local Sobolev notation. For example take Omega=B_1 in R^n, u(x)=x1 and a=0. Then log|u(x)-u(a)|=log|x1| is smooth, hence W1,n_loc, on Omega minus {x1=0}. Nevertheless u has zeros. Indeed log|f| is automatically locally Lipschitz off the zero set of any locally Lipschitz f, by a positive lower bound on every compact subset there. The intended obstruction is integrability across a neighborhood of a boundary zero, precisely the displayed divergent integral, not local integrability after deleting all zeros. The actual PDF was inspected to rule out a text-extraction error. The correct Theorem3.7 and the submitted scope note are unaffected.

## 6. Consequences and open hypotheses for the Euler reduction

For a smooth nontrivial pair (V,S) on a two-dimensional orbit disk, f=(|V|²+S²)^(1/2) is locally Lipschitz. At any boundary point of {f=0}, its logarithmic gradient therefore cannot belong to L2 across that point. A quotient such as R=|V|²/|S| need not vanish and is a different function. Even a constant positive quotient may coexist with a flat common amplitude. Thus regularity of the original fields gives no logarithmic-energy estimate for the coefficients obtained after division.

The positive dbar theorem requires a constant principal part and a checked L2 zeroth-order coefficient. The negative example allows a non-Lipschitz principal matrix and four real unknowns. Neither decides strong continuation for the actual two-scalar degenerate Euler system, whose Poisson, rank, homogeneity and support relations remain to be used. The source's higher-dimensional weak result and scalar C/|z| theorem must also retain their exact dimensions and target spaces. The scalar theorem's cited1992 one-dimensional base theorem was not obtained in this pass; its scope is checked from the actual statement, not recertified independently here. All omega remains in the campaign's open problem; no dependence on omega is suppressed to make one of these theorems apply.

The missing estimate is a consequence of the Euler equations, not another appeal to smoothness before division. No profile nonexistence, smooth-coefficient counterexample, or local coupled Euler counterexample is established here.
