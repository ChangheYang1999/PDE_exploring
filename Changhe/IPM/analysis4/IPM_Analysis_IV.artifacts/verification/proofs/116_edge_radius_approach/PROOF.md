# How fast the highest-mode edge radii approach their limit

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement and notation

Fix delta in (0,1), d=delta/(1-delta), and an even integer B>=2 arising as one plus the largest odd frequency of a nonzero finite leading sine polynomial. Set

    eta=B-delta, a=2/eta, b=2(B-1)/eta, nu=1/b,
    Beta=integral_0^1 t^(a-1)(1-t)^(b-1) dt,
    R=4d(a Beta)^(1/a),
    kappa=4d(ab Beta)^nu nu/Gamma(1-nu).

Let h_n>0 be the amplitude-normalized highest coefficients of the complete canonical recurrence. Topic115 proposes

    h_n R^n ~ kappa n^(-1-nu).                         (1)

For K>=1 define R_K and mu_K by

    sum_(i=1)^K h_i R_K^i/(eta i+2)=2d/B,
    mu_K=B/(2d) sum_(i=1)^K i h_i R_K^i/(eta i+2).

These are the highest-mode radius and the finite-memory mean in topics113 and114. Assuming (1),

    R_K-R ~ C_R K^(-1-nu),
    b-mu_K ~ C_mu K^(-nu),                            (2)

where the exact positive constants are

    C_R=B R kappa/[4d(B-1)(1+nu)],
    C_mu=B kappa/[2d eta nu].                         (3)

For B>2 the fixed-edge polynomial exponents

    s_K=2-delta/B-(B-2)/(B mu_K)

satisfy

    (1+nu)-s_K ~ [(B-2)kappa/(4d(B-1))] K^(-nu).       (4)

For B=2 this difference is identically zero. No constant here is a convergence radius for the full angular norm. The limiting process is K->infinity with delta and B fixed.

## The omitted generating-function tail

Put V_K(z)=sum_(i<=K)h_i z^i/(eta i+2) and J(z)=sum_(i>=1)h_i z^i/(eta i+2). The positive endpoint identities proved in topic38 are

    H(R)=4d, J(R)=2d/B, J'(R)=2d b/(B R).             (5)

For the derivative identity, the nonnegative series gives

    R J'(R)=sum_i i h_i R^i/(eta i+2)
           =[H(R)-2J(R)]/eta=2d b/B.

The derivative sum is finite, so all these expressions are justified at the boundary.

Define the positive omitted tail tau_K=J(R)-V_K(R). By (1),

    h_i R^i/(eta i+2) ~ (kappa/eta) i^(-2-nu).

The elementary tail estimate sum_(i>K)i^(-p)~K^(1-p)/(p-1) for p>1 follows by bounding the decreasing summands between their adjacent integrals. Applying upper and lower comparisons after a sufficiently large finite index gives

    tau_K ~ kappa/[eta(1+nu)] K^(-1-nu).              (6)

## Controlling the derivative between the two radii

Topic113 proves R_K decreases to R and

    0<R_K-R<=4d(eta+2)/[eta(K+1)+2].                  (7)

Consequently there is a finite constant C_* independent of K such that

    K log(R_K/R)<=C_*.

For every z in [R,R_K] and i<=K, the ith term of V_K'(z) is at most

    exp(C_*) i h_i R^(i-1)/(eta i+2).

The latter sequence is summable by (5). For every fixed i, its original derivative term tends to the corresponding term of J'(R), uniformly over z in [R,R_K]. Splitting the sum into a finite prefix and a uniformly bounded tail therefore proves

    sup_(R<=z<=R_K)|V_K'(z)-J'(R)| ->0.              (8)

This step controls the growing degree K; pointwise convergence at the endpoint alone would not justify evaluation at a moving point beyond R.

Since V_K(R_K)-V_K(R)=tau_K, integration and (8) give

    tau_K=(R_K-R)[J'(R)+o(1)].                       (9)

Use (5) and (6). The resulting constant is

    [kappa/(eta(1+nu))]/[2d b/(B R)]
      =B R kappa/[4d(B-1)(1+nu)],

which is C_R. This proves the first assertion in (2). In particular, the stronger estimate R_K/R-1=O(K^(-1-nu)) is now available.

## The mean approaches b by an omitted-tail effect

Define the full probability weights

    p_i=B h_i R^i/[2d(eta i+2)].

They sum to one and have finite mean b by (5). Their tail asymptotic is

    p_i ~ A i^(-2-nu), A=B kappa/(2d eta).            (10)

Let epsilon_K=R_K/R-1. Then

    b-mu_K
      =sum_(i>K) i p_i
         -sum_(i<=K) i p_i[(1+epsilon_K)^i-1].        (11)

The first sum is asymptotic to (A/nu)K^(-nu) by the same integral comparison. The second sum is smaller. The inequality (1+epsilon)^i-1<=i epsilon exp(i epsilon), for epsilon>=0, and the first result of (2) give

    0<=sum_(i<=K) i p_i[(1+epsilon_K)^i-1]
       <=epsilon_K exp(K epsilon_K) sum_(i<=K)i^2 p_i
       =O(K^(-1-nu)) O(K^(1-nu))
       =O(K^(-2nu)).                                 (12)

Here K epsilon_K=O(K^(-nu)) is bounded, and (10) gives sum_(i<=K)i^2p_i=O(K^(1-nu)) because 0<nu<1. Since K^(-2nu)=o(K^(-nu)), (11) proves

    b-mu_K ~ A K^(-nu)/nu.

This is the second assertion in (2) with C_mu as stated.

## The polynomial-exponent gap

Topic114 proves mu_K->b and s_K=2-delta/B-(B-2)/(B mu_K), with limiting exponent 1+nu. For B>2,

    (1+nu)-s_K
      =(B-2)/B * (b-mu_K)/(b mu_K)
      ~ (B-2) C_mu/(B b^2) K^(-nu).

Since b nu=1 and eta b=2(B-1), the prefactor simplifies to (B-2)kappa/[4d(B-1)]. For B=2 the formula for s_K is independent of mu_K. This proves (4) and the asserted exceptional case.

## Dependencies and finite checks

The proof uses the highest-mode recurrence and endpoint sums in topic38, the exact finite-edge radii and their O(1/K) bound in topic113, the mean and exponent formula in topic114, and the proposed sharp coefficient asymptotic in topic115. Without independent confirmation of topic115, the present assertions are conditional results, not PROVED statements.

Finite tests can bracket the polynomial roots at increasing K and evaluate the scaled gaps K^(1+nu)(R_K-R) and K^nu(b-mu_K). They can test the constants but cannot establish either asymptotic. No whole-sequence convergence conclusion is drawn from such comparisons.
