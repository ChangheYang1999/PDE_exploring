# The bivariate polynomial product radius

This is a source-level conditional lemma for the frozen `BiTM.__mul__`.
It corrects the first Opus review's operation-path count. It does not
validate the whole product of Taylor models or the actual BLAS routines.
Written before the checker for this lemma; see the WORKLOG timestamp.

Assume finite binary64 round-to-nearest scalar additions and products,
gradual underflow, no overflow, and the exact scalar loop in the snapshot.
Let u=2^-53, eta=2^-1074, and 2<=K<=1024. One output coefficient has N<=K
contributions. Starting from zero, the code forms the midpoint sum mhat,
the nonnegative sum dhat of absolute midpoint products, and phat by
accumulating

 RN(RN(RN(|a| rb) + RN(ra |b|)) + RN(ra rb)).

Each leaf of this last expression passes through one multiplication, at
most two inner additions, and at most N-1 nontrivial accumulator additions.
The first addition to zero is exact. The longest path therefore has at
most N+2<=K+2 rounded operations, not4K. The total count of operations is
irrelevant to the multiplicative error on an individual leaf.

Write D=sum |a b| and P=sum(|a|rb+ra|b|+ra rb). Let

 g=Ku/(1-Ku), G=2Ku/(1-2Ku),
 cD=K/[2(1-Ku)], cP=3K/[2(1-(K+2)u)].

Expanding the addition trees with |delta|<=u and multiplication error
|xi|<=eta/2 yields

 |mhat-sum ab| <= gD+cD eta,
 dhat >= (1-g)D-cD eta,
 phat >= (1-u)^(K+2)P-cP eta.                         (1)

There are at most K underflow-producing multiplication nodes in each
midpoint or absolute sum, and at most3K in phat. Binary64 addition has no
absolute underflow error because a subnormal exact sum of binary64 inputs
is representable. Subsequent relative-error factors amplify each xi by
at most1/(1-(K+2)u), giving the stated safe cP. The same reasoning with K
gives cD. Skipped zero contributions only reduce these counts.

The returned coefficient radius obeys

 r >= G dhat+(1+G)phat+4(K+1)eta.                       (2)

The source computes gam by a successor of a division with exactly
representable numerator2Ku and denominator1-2Ku. The scalar operations
in the final radius are outward successors of nonnegative operations;
4(K+1)eta is exactly representable in this range. These facts justify(2).

Now G(1-g)=2g and, by Bernoulli,

 (1+G)(1-u)^(K+2)
 >= [1-(K+2)u]/[1-2Ku] >=1,                           (3)

where the last inequality uses K>=2. Also Ku<=1/8 and
(K+2)u<=2Ku<=1/4, so cD<=4K/7, cP<=2K, and1+G<=4/3. Consequently

 (1+G)(cD+cP) <=24K/7 <4(K+1).                         (4)

Insert(1) in(2), use(3), and then(4). This gives

 r >=2gD+P-[GcD+(1+G)cP]eta+4(K+1)eta
   >=gD+P+cD eta
   >=P+|mhat-sum ab|.

Thus the full, untruncated polynomial coefficient interval encloses all
products of inputs in their midpoint-radius boxes. This proof resolves
the specific claimed deficit in the accumulation of input radii. It does
not address power weights, polynomial truncation, remainder products,
Bernstein domain alignment, an actual BLAS evaluation tree, or the full
forcing bound. In the current source K=(12+1)(8+1)=117.
