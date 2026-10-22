# Conditional validation of midpoint-radius sums and products

Written 2026-10-20, before the checking program. Status: OPEN pending independent review and exact verification. This is a source-level theorem, not acceptance of a BLAS implementation or of the flow certificate.

## 1. Statement and arithmetic hypotheses

Let u=2^-53 and eta=2^-1074. Inputs are finite binary64 numbers; interval radii are nonnegative. All intermediate values are finite. Scalar arithmetic is round-to-nearest with gradual underflow. `succ` returns the next binary64 number toward positive infinity. Hence succ(RN(x))>=x for a nonnegative exact scalar result x. The sum/product routines below are the frozen file `../flow_certificate/evidence/source/midrad.py`, SHA256 5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e.

The extra dot-product hypothesis is explicit: a K-term dot product is evaluated by K multiplications and an addition tree with K-1 additions, with any subset of multiplication/addition pairs fused into FMA; no data-dependent scaling or extra arithmetic is used. Each path has at most K rounded operations. Ordinary addition of binary64 operands has no absolute underflow error: a subnormal exact sum is representable. There are at most K multiplication or fused nodes which can incur an absolute underflow error. This hypothesis must be separately established for the BLAS output used by a certificate. Merely naming BLAS does not establish it.

Under these hypotheses, for 2<=K<=1024, `mr_matmul` returns an interval containing every dot product of values in the input intervals. For 1<=K<=1024, `MR.sum` is enclosing if its reduction is an addition tree. For the same K range, the nonnegative weighted-sum formula in `TMArr.sup` is enclosing under the dot hypothesis. These statements assume that supplied weights are themselves upper bounds. They do not validate library powers, modal maps, transcendental conversions, ODE remainders, angular coverage, historical output provenance, or the full flow certificate.

## 2. Error bound for a dot-product tree

For each elementary multiplication or FMA, write fl(z)=z(1+delta)+xi with |delta|<=u and |xi|<=eta/2. For ordinary addition use xi=0. Expanding a tree expresses each exact product with a factor equal to a product of at most K factors 1+delta, and each additive xi with at most K subsequent such factors. The elementary product estimate

  |product_(j=1)^l(1+delta_j)-1| <= gamma_l=l u/(1-l u)

follows by (1+u)^l<=1/(1-l u) and (1-u)^l>=1-l u, for l u<1. Therefore, with g=K u/(1-K u) and c=K/[2(1-K u)],

  |dot_hat-dot_exact| <= g sum |a_i b_i| + c eta.                 (1)

The at most K additive errors are amplified by at most1/(1-Ku). This also proves for a nonnegative dot product D the lower bound

  dot_hat >= (1-g)D-c eta.                                     (2)

The zero or subnormal terms are included. No O(u²) terms are discarded.

## 3. The matrix radius

For one output entry, set

  D=sum |a_i b_i|,
  P1=sum |a_i| rb_i, P2=sum ra_i |b_i|, P3=sum ra_i rb_i,
  P=P1+P2+P3.

For any actual input values in the boxes, the exact output differs from sum a_i b_i by at most P. Let dhat be the source's `absAB` output and phat its three auxiliary products followed by two additions. Because the operands of those two additions are nonnegative, rounding underflow is exact and

  dhat >= (1-g)D-c eta,
  phat >= (1-u)^2 ((1-g)P-3c eta).                             (3)

Even when the displayed right side is negative, these inequalities remain valid.

Set G=2Ku/(1-2Ku). The source's floating `gam` is >=G: for the stated K the numerator and denominator are exact binary64 quantities and the division is followed by succ. Its scalar radius operations followed by succ give

  radius >= G dhat+(1+G)phat+4(K+1)eta.                        (4)

Replacing the computed gam by G is justified directly by dhat,phat>=0, before invoking (3). Now

  G(1-g)=2g,
  (1+G)(1-u)^2(1-g)=(1-u)^2/(1-Ku)>=1                        (5)

for K>=2. Thus (3)-(4) give

  radius >= 2gD+P - c[G+3(1+G)(1-u)^2]eta+4(K+1)eta.

It suffices that

  c[1+G+3(1+G)(1-u)^2] <= 4(K+1).                            (6)

There is a simple exact bound. Since Ku<=1/8, c<=4K/7, G<=1/3, and the square bracket is <=4(1+G)<=16/3. The left side is <=64K/21<4K<4(K+1). Hence radius>=gD+P+c eta, proving the assertion by (1). The spare gD has not been used to hide a deficit.

The source allowance4(K+1)eta is exactly representable for K<=1024, as are the integers involved. The final successor additions preserve the lower bound (4). This argument addresses the composed radius, including the computed auxiliary products, instead of claiming that multiplying an arbitrary gamma_2K relative-error bound by1+gamma_2K reverses it. That latter generic claim would be false.

## 4. A sum of midpoint-radius intervals

Let K<=1024, D=sum |m_i| and R=sum r_i. An addition tree of K terms has midpoint error <=gamma_(K-1)D, without an additive underflow term. For a nonnegative reduction,

  sum_hat >= (1-(K-1)u) sum_exact.

The source factor I=succ(RN(1+Ku)) is >=1+Ku. Since

  (1+Ku)(1-(K-1)u)=1+u-K(K-1)u²>=1,

it inflates either nonnegative reduction above its exact sum. The source's computed gamma_(K-1) is an upper bound, and all subsequent nonnegative scalar operations are followed by succ. The extra K eta is harmless. For K=1 the gamma term vanishes and the reduction is exact.

## 5. Nonnegative weighted polynomial sums

Suppose d_i,w_i>=0 are binary64 numbers and w_i bounds the corresponding true nonnegative weight. Let P=sum d_i w_i and K be the number of terms. A product-and-sum tree gives the sharper positive lower bound

  Phat >= (1-u)^K P-c eta,                                   (7)

by expanding its positive leaves; this uses at most K underflow-producing nodes as above. Let I=succ(RN(1+(K+1)u)), the factor used in the source. For K<=1024, I<3/2 and

  I(1-u)^K >= (1+(K+1)u)(1-Ku)
            =1+u-K(K+1)u²>=1.

Also I c < (3/2)(4K/7)=6K/7<K+1. Therefore

  succ(succ(Phat I)+(K+1)eta) >= P.                          (8)

Adding a nonnegative remainder with succ preserves the enclosure. This validates the formula in `TMArr.sup` (K=Q+1), and the analogous `polysup` formula in `TMArr.mul_poly` (K=d+1), provided the magnitude inputs and h powers enclose their intended quantities. It does not validate the other parts of those methods.

## 6. Evidence plan and scope

An exact Fraction checker will verify (5)-(6) and the two inflation inequalities for every integer K in the stated range, and check the actual source factors against exact rational values. A separate rational Gaussian elimination or unrelated interval calculation is not relevant to this arithmetic theorem; the independent numerical cross-check will instead evaluate all scalar margins using Arb512 and mpmath.iv180, then audit saved enclosures at higher precision. Synthetic dot products may test actual finite cases but cannot prove the dot-tree hypothesis for a library. Actual Opus5.5 will review the proof and a follow-up will resolve objections. Any future verdict must retain this distinction.

Dependencies: elementary binary64 model explicitly stated above; no external theorem is needed beyond the proved tree estimate. The flow source still needs a finite audit or a documented evaluation model for its actual BLAS products, as well as all the separate analytic and coverage checks.
