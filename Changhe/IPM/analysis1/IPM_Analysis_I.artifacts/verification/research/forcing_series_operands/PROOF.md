# Finite series operands on the localized forcing blocks

Written2026-10-21before the replay and its checking programs. This result
concerns a contemporary replay of the geometric part of the frozen v2.2
forcing source. Historical composed model arrays were not saved. This
result cannot attest those arrays or the physical residual enclosure.

## Statement

For delta=33/2000 and every p in the exact source bracket, use the13
radial parents4096..4108 and16 angular parents of topic119. A parent has
local coordinates sigma in[0,h], phi in[-w,w]. Divide into2 radial and2
angular blocks. Let H=32hk, W=2wk, with hk>=h/64 and wk>=2w/8. Block
(bs,bp) is shifted by a_s=bs H, a_p=-w+4bp wk+2wk. Its local coordinates
are sigma' in[0,H], phi' in[-W,W]. Physical assertions are restricted to
the intersection with the original parent and theta>=0. These832 blocks
cover the upper support by the exact coverage argument of topic119.

Let q=(x-p)^2+y^2. Suppose a saved geometric model of q-c0 has coefficient
midpoints m_ij, nonnegative radii r_ij, scalar remainder e>=0, and c0>0.
Define the exact rational number
 B=sum_(i,j)(|m_ij|+r_ij) H^i W^j+e.
If the saved Umax>=B and the saved x>=Umax/c0, then |q-c0|<=c0 x on the
restricted block whenever that geometric model is sound. The triangle
inequality proves this statement. It includes the scalar remainder and
the uncertain p. We also check |q-c0|<=c0 x directly using interval
geometry, independently of the model's physical soundness.

For every accepted block with0<=x<1 and integer K=16, define
 T(c0,x)=c0^(-1/2)x^17/(1-x),
 b_k=(-1)^k binom(2k,k)c0^(-k-1/2)/4^k, 0<=k<=16.
The real series remainder after degree16 in(q-c0) has absolute value at
most T(c0,x). This follows from |binom(-1/2,k)|<=1 and the geometric
series, as proved in topic119. Thus a saved nonnegative tail R is a
sufficient scalar allowance if R>=T. This can be checked without a
floating transcendental operation: for c0>0 and0<=x<1,
 R>=T if and only if R^2 c0(1-x)^2>=x^34.                 (1)
All quantities in(1) are exact rationals when the saved inputs are binary64.
For x=0 the claim holds with any R>=0. Independently, Arb and mpmath.iv
can evaluate the positive square root expression with directed enclosures.
Every saved midpoint-radius binomial coefficient must enclose the exact
b_k. Its signed formula is checked independently, with no assumption
about a libm pow rounding guarantee.

## Direct geometry proof

For r=exp(t), theta in[a,b] with0<=a<=b<pi/2,
 q=r^2-2rp cos(theta)+p^2
 increases with theta and is convex in r. Let r in[r1,r2]. At theta=a,
 q=(r-p cos(a))^2+(p sin(a))^2.
A lower bound is the squared distance from the interval enclosing p cos(a)
to[r1,r2], plus a lower bound on(p sin(a))^2. At theta=b the maximum
occurs at r1 or r2. Bound those two values using the same stable squared
formula. Interval evaluation over p gives a simultaneous enclosure for
every p in the source bracket. Enclosing the exact knot in its saved
canonical ball bounds the radial interval; exact rational block shifts
are then added. Intersect the angular domain with its parent and the
upper half-plane. A radial box larger than the restricted physical radial
interval remains safe. These operations produce q_lower<=q<=q_upper.
The two rational inequalities c0(1-x)<=q_lower and q_upper<=c0(1+x)
then certify the ratio directly, without relying on a composed Taylor
remainder. The Arb engine uses square roots of distance bounds; the
second interval engine uses squared distances directly.

## Replay and verification scope

The replay retains every geometric q and q-c0 coefficient, scalar
remainder, c0, Umax, x, tail and17 binomial coefficient intervals. It
uses only the canonical knot boxes and the one-frequency trigonometric
geometry. It does not evaluate the physical residual or compose its
forcing models. The source expressions generating these operands must
be identified and bound to the saved source hashes. The replay's values
are checked by exact rational summation and inequality(1), independently
by ball arithmetic, and by the direct interval geometry above.

A complete finite PASS certifies these contemporary scalar operands and
the direct q-range assertions only. It does not validate historical
execution, full Taylor-model algebra, the radial physical residual,
Bernstein output, or the published physical forcing norm. Generic
all-input floating tail correctness also does not follow from a finite
PASS. Any failed inequality must be retained and reported. No PDE
endpoint follows from this result.
