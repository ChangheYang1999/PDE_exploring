# A joint weight closes products but not the polynomial Poisson inverse

Status: CONFIRMED after independent theory-part review and verifier recheck at 2026-10-31T05:42:01Z. This identifies the obstruction left after repairing the deficit-only product norm of topic70. It does not settle the actual rational IPM series.

## 1. A reciprocal-binomial norm

For an integer k>=1 and a polynomial A(t)=sum_(q=0)^(k-1) a_q t^q, with coefficients in a normed algebra satisfying ||ab||<=||a||||b||, define

    N_k(A)=sum_(q=0)^(k-1) ||a_q||/binom(k-1,q).             (1)

The plain coefficient norm P(A)=sum_q ||a_q|| satisfies

    N_k(A)<=P(A)<=2^(k-1)N_k(A).                             (2)

Indeed1<=binom(k-1,q)<=2^(k-1). Thus a geometric bound on N_k is equivalent, up to a change in geometric constant, to a geometric bound on the plain coefficient norm.

With deficit d=k-1-q, the weight in(1) can also be written

    ||a_q||/binom(k-1,q) = [d!/(k-1)!] q!||a_q||.             (3)

It is a joint weight in block index and deficit, so the obstruction of topic70 does not apply.

For i,j>=1, set k=i+j. The product has degree at most k-2. For every pair u,v of input degrees, Vandermonde's identity gives

    binom(i-1,u)binom(j-1,v)
        <=binom(k-2,u+v)<=binom(k-1,u+v).

Apply this to each coefficient product and sum. It proves

    N_(i+j)(AB)<=N_i(A)N_j(B).                               (4)

The same bound holds with output index i+j+1, since increasing the upper binomial index only decreases each weight. These are precisely the two possible output block indices in the high-high IPM product. This is a product estimate, not yet an estimate for the complete Jacobian.

## 2. Differentiation and the stationary inverse

For1<=q<=k-1,

    q/binom(k-1,q-1) = (k-q)/binom(k-1,q).

Consequently

    N_k(partial_t A)<=(k-1)N_k(A).                           (5)

Fix Q>=3, delta=2/Q and c=Q/(Q-2). In density block n=Qk+r,1<=r<=Q, k>=1, the stationary equation is

    (lambda_n-c partial_t)F_n=S_n,
    lambda_n=(n-1)(c-1)>=2ck.

On polynomials of degree at most k-1, differentiation is nilpotent. Its finite Neumann inverse and(5) give

    N_k(F_n)<=N_k(S_n)/[lambda_n-c(k-1)]
             <=2 N_k(S_n)/lambda_n.                         (6)

Thus the product and stationary-inverse steps themselves do not force a factorial loss in this joint norm.

## 3. A factorial witness for the Poisson inverse

At the same rational parameter, take k>=2 and choose the nonresonant order n=Qk+1. Set

    q=k-1,   m=2k-3,
    F_n(t,theta)=t^q sin(m theta).                           (7)

This respects S1 symmetry and the universal degree and bandwidth restrictions. It is an arbitrary input to the linear Poisson map, not asserted to be a coefficient of the nonlinear recursion.

For a density a(t)sin(m theta), the upward stream harmonic m+1 has coefficient

    B_+(t)=-(1/2)(partial_t+P_n+m+1)^(-1)a(t),
    P_n=2-n delta.                                          (8)

To derive(8), the upward forcing is (1/2)(partial_t+p_n-m)a. The Poisson operator at harmonic m+1 factors as

    (m+1)^2-(P_n+partial_t)^2
      =(m+1-P_n-partial_t)(m+1+P_n+partial_t).

The first factor is minus the forcing numerator, so it cancels on polynomials. At(7), P_n+m+1=-2/Q. Both factors are invertible because n is not a stream-resonant order. Therefore, writing s=2/Q,

    B_+(t)=-(1/2)(partial_t-s)^(-1)t^q
          =(1/(2s)) sum_(h=0)^q s^(-h) partial_t^h t^q.

Every displayed coefficient is positive. In particular

    B_+(0)=q!/(2s^(q+1))=(k-1)!/[2(2/Q)^k].                 (9)

With the physical sine-coefficient l1 angular norm, N_k(F_n)=1. The output stream coefficient at t^0 has weight1 in(1), so

    N_k(G_n)/N_k(F_n)>=(k-1)! (Q/2)^k/2.                    (10)

This exceeds C^k for every fixed C as k tends to infinity. For example, the last floor((k-1)/2) factors in(k-1)! are each at least(k-1)/2, proving supergeometric growth without asymptotic formulas.

No bound of the form N_k(G_n)<=C_0 C_1^k N_k(F_n) can therefore hold for all inputs satisfying only the generic degree and bandwidth bounds. Fixed losses in angular strip width or in radial radius change the norm ratio by at most an exponential in k and cannot remove(10).

More generally, the same conclusion applies to any family of norms exponentially equivalent to the plain coefficient norm, uniformly on these input and output spaces: the input has plain norm1 and the output has at least the constant coefficient(9), so exponential equivalence cannot absorb the factorial lower bound.

## 4. What this does and does not exclude

The joint weight in(3) repairs the product obstruction of topic70 and retains enough information for ordinary convergence. But the Poisson inverse remains unbounded with any geometric loss on the full polynomial input space. A proof using this norm must exploit extra relations in the actual density coefficients, or estimate density and stream together on a smaller space preserved by the nonlinear recurrence.

The witness(7) is not an IPM-generated sequence. It proves failure of an unrestricted operator estimate, not divergence of the IPM expansion. The fixed-deficit theorems do not contradict this example: its top-degree density input has no accompanying compatible high-block history, and the large constant stream coefficient lies at deficit k-1 rather than at any fixed deficit.

## 5. Verification

An independent exact Cartesian Poisson implementation checks(9) and the full differential equation at several Q and k values. Separate exact integer checks verify the Vandermonde coefficient inequality and the derivative identity. The all-order argument is the factorization and the explicit polynomial inverse above.

## Review closure

2026-10-31T05:42:01Z: The joint norm, inverse estimate and factorial Poisson obstruction are confirmed. The independent review checked the exact inequalities and recurrence shifts. It is retained in sources/lead_review_20261031T0538Z.md. The finite checks supplement the argument; the proof does not rely on finite enumeration.
