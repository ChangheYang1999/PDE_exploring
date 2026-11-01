# A positive asymptotic constant for every fixed edge width

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement

Fix delta in (0,1), an even integer B>=2, and an integer K>=1. Put d=delta/(1-delta), eta=B-delta. Let h_n be the amplitude-normalized positive highest coefficients of the full canonical IPM recurrence, and let h_(n,K) be those of the modified recurrence retaining exactly the ordered pairs with min(i,j)<=K. Both sequences start at one. Topics112 and113 derive these sequences directly from the angular recurrence and prove h_(i,K)=h_i for i<=K.

Define R_K>0, the probabilities p_i, their mean mu_K, and s_K by

    sum_(i=1)^K B h_i R_K^i/[2d(eta i+2)]=1,
    p_i=B h_i R_K^i/[2d(eta i+2)],
    mu_K=sum_(i=1)^K i p_i,
    s_K=2-delta/B-(B-2)/(B mu_K).

There is a constant kappa_K>0 such that

    h_(n,K)=kappa_K R_K^(-n) n^(-s_K)[1+O(1/n)].       (1)

The constant and the implicit error bound may depend on delta, B and K. In particular, the consecutive coefficient ratio tends to 1/R_K. Multiplying by the original signed leading amplitude gives the corresponding physical highest coefficient; its absolute geometric factor is |alpha|/R_K.

For B=2 and K=1, put

    a=2/(2-delta), s=2-delta/2, R_1=d(4-delta).

Then h_(1,1)=1, and for n>=2 the remaining coefficients and the limiting constant are explicit:

    h_(n,1)=(1/2) R_1^(-(n-1))
       Gamma(n+a-s) Gamma(1+a)
       /[Gamma(1+a-s) Gamma(n+a)],                    (2)

    kappa_1=(R_1/2) Gamma(1+a)/Gamma(1+a-s).              (3)

All gamma arguments in (2) are positive. Formula (1) does not depend on the proposed full highest-mode asymptotic in topic115.

## Normalize the finite-memory recurrence

For n>2K, topic113 gives

    h_(n,K)=sum_(i=1)^K q_(n,i) h_(n-i,K),

    q_(n,i)=h_i/[2d(n-1)]
       {B[(n-i)/(eta i+2)+i/(eta(n-i)+2)]-1}>0.

With c_i=B h_i/[2d(eta i+2)] and D_i=i-1+(eta i+2)/B, its exact rational expansion is

    q_(n,i)/c_i=1-D_i/n+O(n^(-2)).                    (4)

The error is uniform in i because K is fixed. Set w_n=h_(n,K) R_K^n n^(s_K). Its recurrence is

    w_n=sum_(i=1)^K a_(n,i) w_(n-i),
    a_(n,i)=q_(n,i) R_K^i (1-i/n)^(-s_K)>0.

Thus

    a_(n,i)=p_i[1+(s_K i-D_i)/n+O(n^(-2))].           (5)

The definition of s_K gives sum_i p_i(s_K i-D_i)=0. Consequently

    r_n=sum_i a_(n,i)=1+O(n^(-2)).                    (6)

This cancellation makes the remaining multiplicative error summable.

## Uniform positive bounds for the normalized coefficients

Choose n_0>2K so that |r_n-1|<=C/n^2<1/2 for n>=n_0. Define the maximum and minimum in the length-K state vector by

    M_n=max(w_n,...,w_(n-K+1)),
    m_n=min(w_n,...,w_(n-K+1)).

All initial entries are strictly positive. The recurrence implies

    M_n<=max(1,r_n) M_(n-1),
    m_n>=min(1,r_n) m_(n-1).

The products of these factors converge to finite positive limits. Indeed, for |r_n-1|<1/2 the absolute logarithm of either factor is bounded by 2|r_n-1|, whose sum is finite. Multiplying the inequalities from n_0 onward therefore proves constants m,M with

    0<m<=w_n<=M<infinity.                             (7)

The finitely many earlier indices are absorbed into m and M.

## Contraction of differences across a finite window

Let X_n=(w_n,w_(n-1),...,w_(n-K+1))^T. Let P_n be the row-stochastic companion matrix with first row a_(n,i)/r_n and subsequent rows shifting the coordinates. The recurrence becomes

    X_n=P_n X_(n-1)+E_n,

where only the first component of E_n can be nonzero. By (6) and (7),

    ||E_n||_infinity=O(n^(-2)).                       (8)

Since p_i>0 and a_(n,i)/r_n tends to p_i, choose alpha>0 so that every first-row entry is at least alpha for n sufficiently large, with alpha<1/(2K). Every entry of a product of K consecutive matrices P is then at least alpha^K. For an explicit induction, the first row after one step has every entry at least alpha. At each subsequent step the contribution through the first coordinate alone multiplies the preceding first row by a factor at least alpha. Thus the first row after r steps has every entry at least alpha^r. The jth row after K steps equals the first row after K-j+1 steps, because the lower rows shift coordinates. Its entries are therefore at least alpha^(K-j+1)>=alpha^K.

For a vector X let osc(X)=max_j X_j-min_j X_j. If a row-stochastic matrix Q has every entry at least beta, subtract beta from each entry of every row. The remaining rows have total mass 1-K beta. Hence

    osc(QX)<=(1-K beta) osc(X).

Apply this with beta=alpha^K. Products of row-stochastic matrices have infinity norm one, so (8), iterated over K steps, yields

    osc(X_(n+K))<=rho osc(X_n)+C_1/n^2,
    rho=1-K alpha^K in (0,1).                        (9)

This implies osc(X_n)=O(n^(-2)). For detail, iterate (9) separately on each residue class modulo K. The resulting geometric convolution is bounded by a constant times n^(-2): split its indices at half the elapsed number of blocks. In the recent half, denominators are at least a fixed multiple of n^2 and the geometric sum is bounded. The older half has exponentially small weights and a bounded sum of reciprocal squares. The exponentially decaying initial term has the same bound.

The first component equation now gives

    |w_n-w_(n-1)|
       <=osc(X_(n-1))+||E_n||_infinity
       =O(n^(-2)).                                  (10)

This argument includes K=1, where the oscillation is identically zero. Summing (10) proves that w_n has a finite limit kappa_K and |w_n-kappa_K|=O(1/n). The lower bound in (7) gives kappa_K>=m>0. This proves (1). Taking the quotient of the asymptotic formulas at n+1 and n proves the ratio limit.

## The closed formula for B=2, K=1

When B=2, eta=2-delta and a=2/eta. Direct simplification of the exact coefficient in the scalar tail recurrence gives, for n>=3,

    q_(n,1)=R_1^(-1) (n-1+a-s)/(n-1+a),
    s=1+eta/2=2-delta/2.

At n=2 there is only one central ordered pair, not two orientations. Consequently h_(2,1) is exactly half the value obtained by extending this tail formula to n=2. Iterating from this correct h_(2,1) and applying Gamma(x+1)=x Gamma(x) gives (2), including its factor1/2. The smallest displayed gamma argument is

    1+a-s=a-eta/2=(4-eta^2)/(2eta)>0,

because 1<eta<2. Stirling's formula at the two positive large arguments gives Gamma(n+a-s)/Gamma(n+a)=n^(-s)[1+O(1/n)], proving (3).

## Dependencies and verification scope

The proof uses the exact positive recurrence in topic113 and the first-order cancellation computed in topic114. The stochastic-matrix contraction estimate, summable-error argument and limiting-constant proof are supplied here. No theorem about an unrestricted recurrence is inferred from fixed K.

Finite checks will compare the exact gamma-product formula with independently generated K1 coefficients, and evaluate the normalized fixed-K sequences at increasing n. Such tests can diagnose a constant or sign error; they cannot prove (1). Independent review of the all-order argument remains required.
