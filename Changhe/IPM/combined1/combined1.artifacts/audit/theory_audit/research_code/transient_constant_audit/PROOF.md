# Sharp use of the three-component stationary inverse bound

## Assumptions and quantities

Use the background hypotheses and the high/low domain consistency proved in the audited transient theorem (T4-051 with its T4-057 addendum), or in the audited positive-real-resolvent theorem (T4-059). Fix s>0, R>0 and K_L>0. Every normalized input k in the radius-R X_s ball must satisfy the low bound ||A_k^-1||_(L2->L2)<=K_L. The high inverse must already exist by one of those theorems. This scalar calculation does not establish those operator hypotheses.

Set nu=R/sqrt(s) and

    A_s=127/50+(653/5)s, B_s=(9/5)(1+44s),
    alpha=9/10-4290s-(13/10)nu-s(6+1360s),
    q=6+1360s,
    m2=1/2-4708s-(A_s+B_s)nu,
    v1=10+34816s,
    k1=347/5+5440s+B_s nu+s v1.

Require alpha>0 and m2>0. The established stationary estimates for h=A_k^-1 f are

    b<=K_L f0,
    a<=(f1+q K_L f0)/alpha=:G1,
    b_s<=K_L f0+s G1,
    P<=f2/m2+(k1/m2+sqrt(40/m2))G1+v1 K_L f0/m2,

where P=||omega D^2 J^s h||2, a=||D J^s h||2, b_s=||J^s h||2, f2=||omega D^2 J^s f||2, f1=||D J^s f||2 and f0=||f||2.

## Matrix bound and closure

Put D=k1/m2+sqrt(40/m2). Multiplication by the output norm weights gives

    (P,128a,512b_s) <= N (f2,128f1,512f0)

componentwise, with the nonnegative matrix

    N=[[1/m2, D/(128alpha), K_L(v1/m2+Dq/alpha)/512],
       [0, 1/alpha, K_L q/(4alpha)],
       [0, 4s/alpha, K_L(1+s q/alpha)]].                    (1)

Since ||(f2,128f1,512f0)||2<=X_s(f), taking Euclidean norms yields

    ||A_k^-1 f||X_s <= ||N||2 X_s(f).                      (2)

This improves replacing every component of the input vector separately by X_s(f). There is no assertion that N gives a lower bound for the actual operator norm.

Let K be a rational number satisfying K^2 I-N^T N positive definite. Then ||N||2<K, by the Rayleigh quotient. The nonlinear self-map closes whenever X_s(F)<=R/K. Its low contraction has constant at most K_L c_s R, where c_s=(4 pi s(1+s))^(-1/2). Thus one also requires K_L c_s R<1 and c_sR<a0 for a positive corrected slope. The latter follows from c_sR<7/10 and the independently assumed origin lower bound. All normalization, domain and uniqueness steps are inherited unchanged from the audited theorems.

## Exact certification method

The script takes only the rational parameters appearing in T1's table. At s=2^-17 the square root is enclosed by Arb; at s=1/n^2 it is rational. It forms N independently from(1). It certifies positivity of K^2 I-N^TN with its three leading principal minors, by Sylvester's criterion. A rational bisection followed by upward rational rounding gives an explicit certified K. A downward rational rounding of R/K gives a sufficient eta. The script also tests each printed T1 eta directly by taking K=R/eta, retaining positive or negative matrix evidence rather than trusting decimal rounding.

Every step uses512-bit outward Arb arithmetic. Failure of the matrix test for a rounded eta means the stated upper-bound argument does not certify that exact decimal; it does not disprove closure by a sharper inverse estimate. Conversely a positive certificate with eta as printed is a sufficient quantitative result under the stated operator hypotheses. No optimization is needed or run.

## Scope

The baseline point and the six K_L variants are conditional scalar packages. No candidate is asserted to satisfy their low or high operator hypotheses or residual requirement. The distinction between an approximate displayed threshold and a rational sufficient tolerance is part of this audit.
