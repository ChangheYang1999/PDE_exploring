# Summed triangle bounds for factorial-weighted products

Status: the identity below is exact. The stated finite interval computations are independently cross-checked against the direct column-pair sums in topic78. No bound for the infinite generated sequence is asserted.

## Statement and notation

Use the canonical polynomial-log recursion with delta=2/3, c=3, leading density sin(theta), and zero resonant stream constants. Write t=log r, p_j=1-2j/3, P_i=2-2i/3, and

\[
 J_{i,j}(G,F)=(P_iG+\partial_tG)\partial_\theta F
             -(\partial_\theta G)(p_jF+\partial_tF).
\]

For each log column define the nonnegative numbers

\[
 a_{i,u}=\|[t^u]G_i\|_{\ell^1},\quad
 a'_{i,u}=\|\partial_\theta[t^u]G_i\|_{\ell^1},\qquad
 b_{j,v}=\|[t^v]F_j\|_{\ell^1},\quad
 b'_{j,v}=\|\partial_\theta[t^v]F_j\|_{\ell^1}.
\]

Primes here denote angular derivative norms, not derivatives of the nonnegative generating polynomials. Define

\[
 A_i(x)=\sum_u a_{i,u}x^u,\quad A_i^\theta(x)=\sum_u a'_{i,u}x^u,
 \qquad B_j(x)=\sum_v b_{j,v}x^v,\quad B_j^\theta(x)=\sum_v b'_{j,v}x^v,
\]

and the linear functional W(H)=sum_q q![x^q]H. Then the sum of the individual column-pair triangle bounds is exactly

\[
 U_n=W\left(\sum_{i+j=n}\left[
 |P_i|A_iB_j^\theta+|p_j|A_i^\theta B_j
 +(\partial_x A_i)B_j^\theta+A_i^\theta(\partial_xB_j)
 \right]\right).
 \tag{1}
\]

In particular,

\[
 \left\|\sum_{i+j=n}J_{i,j}(G_i,F_j)\right\|_!\le U_n.
 \tag{2}
\]

Setting all four constant coefficients to zero before applying (1) gives the positive-degree bound U_n^{++}. It bounds the norm of the signed sum in which both log degrees are positive. It is not an additive contribution to the norm of the full forcing.

## Proof

For one pair G=t^u g and F=t^v f, direct differentiation gives

\[
 J_{i,j}(G,F)=t^{u+v}(P_i gf'-p_jg'f)
                  +t^{u+v-1}(u gf'-v g'f).
\]

The last term is zero when u=v=0. The sine coefficient norm of a sine-cosine product is at most the product of the two coefficient norms: each pair of basis elements produces two sine terms of magnitude at most one half. Therefore, with q=u+v, this pair's factorial norm is bounded by

\[
 q!(|P_i|a_{i,u}b'_{j,v}+|p_j|a'_{i,u}b_{j,v})
 +\mathbf1_{q>0}(q-1)!(u a_{i,u}b'_{j,v}+v a'_{i,u}b_{j,v}).
 \tag{3}
\]

The first two polynomial products in (1) collect the degree q terms in (3). Differentiating A_i or B_j lowers the degree by one and supplies the factors u or v. Applying W consequently gives exactly the sum of (3), with no omitted multiplicity. Summing the triangle inequality over all i,j,u,v proves (2). Removing the constant coefficients selects precisely u,v>=1 and proves the positive-degree statement.

## Finite audit and scope

The implementation reads the exact dyadic balls of the frozen order280 checkpoint retained in topic78. At640-bit precision it reconstructs every column norm and angular derivative norm, then computes (1) for every n from2 through280. One hundred independent random nonnegative integer examples compare the polynomial formula with a direct integer double sum. The four all/positive sums at270 and280 overlap the separately computed direct column-pair sums of topic78.

Normalize U_n by the same full denominator as topic78:

\[
 D_n=\sum_{i+j=n}\{2j(|P_i|+1)+2i(|p_j|+1)\}
                      \|G_i\|_!\|F_j\|_!.
\]

The first order with U_n/D_n>1 is235, where the ratio is1.0212804534790934489262380025838083 with outward radius1.54e-35. Every earlier ratio is strictly below1. The strictly unique finite maximum occurs at265 and is1.4738031095283007569570213665757052 with radius3.28e-35. At280 the ratio is1.4691267190278617672749854912652 with radius1.90e-32.

For the positive-degree denominator D_n^{++}, the first ratio above1 is at90, with value1.0021071635070066063477857651522202 and radius1.28e-35. Its strictly unique finite maximum is144.74733414847224445586891289605870 with radius1.23e-33 at280. At that order U_n^{++}/U_n is .81734311137077141096792471785464 with radius3.27e-33.

These estimates are bounds obtained before angular and inter-pair cancellation. The full signed ratio itself remains below .361 through280, as checked in topic78. Neither the bounded finite maximum nor the difference between these statistics proves an all-order bound. Actual computation time was52.6905666179955 seconds. The exact outward intervals, input digest, retained source and comparison checks are in verification/checks.json and verification/summary.json.

## Dependencies

Only the independently derived recurrence, finite sine product identities, factorial norm and exact finite polynomial arithmetic are used. The input sequence remains conditional on its audited high-order implementation; the present computation independently recomputes its norm bounds, not all of its high-order signed coefficients.
