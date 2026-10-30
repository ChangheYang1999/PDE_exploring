# Uniform size of all admissible graded boxes

## Statement

Use the component norms of T4-013: P=||omega D^2 J^s h||2, a=||D J^s h||2, b=||J^s h||2, with omega>=1 and ordered derivative tensors. A component box has radii r2,r1,r0>=0 and

    n=(r2^2+2r1^2+r0^2)^(1/2), nu=n/sqrt(s), s>0.

Suppose its top margin satisfies

    0<m2=1/2-4708s-(217/50+(1049/5)s)nu.                    (1)

Then every h in the box obeys

    ||h||2 <= ||h||H^(2+s) <= n
       < 50/(651 sqrt(28248)) < 25/54684 < 1/2000.          (2)

This applies to the graded and gradedL2 frameworks because they use the same top margin. It uses no other closure condition.

## Complete argument

The Fourier polynomial identity (1+|xi|^2)^2=1+2|xi|^2+sum_ij xi_i^2 xi_j^2 gives ||h||H^(2+s)^2<=b^2+2a^2+P^2<=n^2. The multiplier of J^s is at least one, proving the first inequality in(2).

Equation(1) requires s<1/9416 and yields

    n < (50/217) sqrt(s)(1/2-4708s).

Writing u=sqrt(s), differentiate u/2-4708u^3. Its unique positive critical point satisfies u^2=1/28248; the derivative changes from positive to negative there. The maximum is1/(3 sqrt(28248)). Since168^2=28224<28248, (2) follows exactly. This independently confirms T2 Proposition G.

For d2 and Mpen2, T4-064 independently confirmed that every exact fixed-c L2 distributional correction has norm at least0.29552675 and0.55006675, respectively. Both decimals are rounded downward. They exceed25/54684, so neither reference has an exact fixed-c solution in any of these boxes. The older d2 decimal0.0029920 in the T2 source is slightly above its corresponding root0.002991969448; it must be marked approximate, or replaced by0.00299196 if a rigorous lower decimal is desired. The present stronger bound avoids that rounding issue entirely.

## Independent evidence and scope

The code verifies the cubic maximum algebra and all rational comparisons, and encloses the sharper irrational constant by512-bit Arb. It also reconstructs the earlier uniform axis point bound, confirming the Mpen2 and b6 exclusions of T1 R1-004 reviewed by T2. With nu<25/217 and s<1/9416, those point coefficients are

    C1sym n <25/(868 sqrt(pi)),
    C0 n <25/(434 sqrt(9416 pi)).

They bound the axis inequality from T4-017. Inputs are the independently confirmed T4-015 Cartesian values. The resulting d2 point gap remains negative and is inconclusive. No assertion concerns a changed scaling parameter or an arbitrary large correction.
