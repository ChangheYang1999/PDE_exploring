# Polynomial corrections to the highest-mode edge growth

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement and notation

Fix delta in (0,1), put d=delta/(1-delta), and let B=L+1>=2, where L is the largest odd frequency of a nonzero finite real leading sine polynomial. Set eta=B-delta. Normalize its nonzero top amplitude as in topics112 and113, so that the full highest coefficients h_n and their K-edge counterparts h_(n,K) are positive and start at one. The K-edge recurrence keeps exactly min(i,j)<=K. Define R_K by

    sum_(i=1)^K h_i R_K^i/(eta i+2)=2d/B.

Topic113 proves that R_K is the exact radius and decreases strictly to

    R_H=4d[a Beta(a,b)]^(1/a),  a=2/eta, b=2(B-1)/eta.

Define a probability vector and its mean by

    p_(i,K)=B h_i R_K^i/[2d(eta i+2)],   1<=i<=K,
    mu_K=sum_(i=1)^K i p_(i,K).

Then the polynomial decay exponent is

    s_K=2-delta/B-(B-2)/(B mu_K).

For every epsilon>0 there are constants c_epsilon,C_epsilon>0 such that

    c_epsilon R_K^(-n) n^(-s_K-epsilon)
       <= h_(n,K)
       <= C_epsilon R_K^(-n) n^(-s_K+epsilon),   n>=1.     (1)

Equivalently,

    lim_n log(h_(n,K) R_K^n)/log n = -s_K.                (2)

Here the limit is over n>=2. These statements do not assert convergence of h_(n,K) R_K^n n^(s_K) to a nonzero constant.

The means and exponents satisfy

    1=mu_1<mu_2<...<b,   mu_K tends to b,
    s_1=1+(2-delta)/B,
    s_K tends to 1+1/b.

For B=2 every s_K equals 2-delta/2. For B>2 the sequence s_K is strictly increasing. In particular, at delta=2/3 with leading top frequency one, every fixed K has exponent s_K=5/3, even though R_K depends on K.

There is also an ordinary full highest-mode root limit:

    lim_n h_n^(1/n)=1/R_H.                               (3)

This strengthens the limsup radius statement of topic38. It makes no assertion about the root limit of the complete density or stream norms.

## The first correction in the finite-memory recurrence

For n>2K, topic113 derives

    h_(n,K)=sum_(i=1)^K q_(n,i)h_(n-i,K),

    q_(n,i)=h_i/[2d(n-1)] *
       {B[(n-i)/(eta i+2)+i/(eta(n-i)+2)]-1}.

Let

    c_i=B h_i/[2d(eta i+2)],
    D_i=i-1+(eta i+2)/B.

All c_i and q_(n,i) are strictly positive. The exact identity

    q_(n,i)/c_i
      =1-D_i/(n-1)
         +i(eta i+2)/[(n-1)(eta(n-i)+2)]

gives, for each fixed K, uniformly over 1<=i<=K,

    q_(n,i)/c_i=1-D_i/n+O(n^(-2)).                      (4)

The constants in this estimate may depend on K, delta and B. This is a finite rational expansion in 1/n, with denominators bounded away from zero for n>2K. No infinite-series convergence assumption is used.

Set lambda=1/R_K, so p_(i,K)=c_i lambda^(-i) and sum_i p_(i,K)=1. For a real number s define the positive comparison sequence v_n=lambda^n n^(-s). Since K is fixed,

    sum_i q_(n,i) v_(n-i)/v_n
      =sum_i p_(i,K) [1-D_i/n+O(n^(-2))](1-i/n)^(-s)
      =1+[s mu_K-sum_i p_(i,K)D_i]/n+O(n^(-2)).         (5)

Now

    D_i=(2-delta/B)i+(2/B-1),

and hence sum_i p_(i,K)D_i=mu_K s_K. Therefore the right side of(5) is

    1+(s-s_K)mu_K/n+O(n^(-2)).                          (6)

## Two positive comparison arguments

Take s=s_K-epsilon. By(6), there is an integer n_0>2K such that

    sum_i q_(n,i)v_(n-i)<=v_n,   n>=n_0.

The finite positive constant C=max_(1<=n<n_0)h_(n,K)/v_n bounds the initial prefix. Positivity of q_(n,i) and induction then give h_(n,K)<=Cv_n for every n. This is the upper bound in(1).

Take instead s=s_K+epsilon. For a sufficiently large n_1>2K, (6) gives the reverse inequality. The finite positive constant c=min_(1<=n<n_1)h_(n,K)/v_n bounds the initial prefix below. The same induction proves h_(n,K)>=cv_n for every n. This is the lower bound.

Taking logarithms in(1), dividing by log n and letting n tend to infinity gives upper and lower limits within epsilon of -s_K. Letting epsilon decrease to zero proves(2).

## Monotonicity and the limit of the means

Write p_i=p_(i,K) and p_i'=p_(i,K+1) for i<=K. Since R_(K+1)<R_K,

    0<p_i'<p_i.

Both probability vectors have total mass one, so p_(K+1,K+1)=sum_(i<=K)(p_i-p_i'). Consequently

    mu_(K+1)-mu_K
       =sum_(i<=K)(K+1-i)(p_i-p_i')>0.                 (7)

To identify the limit, define

    p_(i,infinity)=B h_i R_H^i/[2d(eta i+2)].

Topic38 and the boundary calculation repeated in topic113 give

    H(R_H)=sum_i h_i R_H^i=4d,
    J(R_H)=sum_i h_i R_H^i/(eta i+2)=2d/B.

Thus the limiting p_i have total mass one, and their mean is finite:

    sum_i i p_(i,infinity)
      =B/[2d eta] [H(R_H)-2J(R_H)]
      =2(B-1)/eta=b.                                  (8)

For an elementary domination argument, the explicit bound in topic113 implies

    K log(R_K/R_H)
       <= K(R_K-R_H)/R_H
       <=4d(eta+2)/(eta R_H)=C_*.

For i<=K,

    i p_(i,K)
       =i p_(i,infinity)(R_K/R_H)^i
       <=exp(C_*) i p_(i,infinity).

Extend p_(i,K) by zero for i>K. For each fixed i it tends to p_(i,infinity), and the displayed summable majorant justifies passage to the limit in the means. Thus mu_K tends to b. One can verify this passage without a measure-theoretic theorem: choose a finite cutoff whose majorant tail is small, pass to the limit in that finite prefix, then bound the remaining tails uniformly. Strict monotonicity gives mu_K<b for every finite K.

The claimed behavior of s_K follows from its formula. For the endpoint,

    2-delta/B-(B-2)/(Bb)=1+1/b,

using b=2(B-1)/(B-delta). When B=2 the term involving mu_K vanishes. When B>2 it increases strictly with mu_K.

## An ordinary root limit for the full highest mode

Topic112 gives h_n>=h_(n,K)>0 for every n and fixed K. The root limit from topic113 therefore yields

    liminf_n h_n^(1/n)>=1/R_K.

Let K tend to infinity. Since R_K decreases to R_H, the lower bound tends to 1/R_H. The exact radius of topic38 gives limsup_n h_n^(1/n)=1/R_H by Cauchy-Hadamard. The two bounds coincide, proving(3).

## Dependencies, checks and scope

Topics38,112 and113 supply the exact highest-mode recurrence, positivity, finite-memory radius, full beta-integral radius and boundary sums. All new arguments are finite rational expansions, positive comparisons, and convergence under an explicitly summable majorant.

Finite checks will verify the rational identity(4), the probability-root brackets, the first-correction exponent, the mean ordering and the special value5/3. They support algebra and indexing only. They do not replace either limiting proof. The physical coefficients are obtained by multiplying h_(n,K) by (-1)^(n-1)alpha^n, so their geometric rate includes |alpha|; their polynomial exponent is unchanged.
