# Acceptance of the complete independent candidate 017 background cover

Status: conditional on the source and arithmetic checks below. This argument
was written and checked before the acceptance checker. The verification record
will supply the actual verdict and real execution time.

## Statement and exact object

Let rho be the exact canonical S1 density of C1-N1-017-legqs50-quot013,
raw SHA256 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114,
and let c=4076476460239181/2251799813685248. The claim is

    sup_(x,y) (|grad rho(x,y)| - rho_y(x,y))/2 <= 2/25,
    c+1-sup_(x,y) (|grad rho(x,y)| - rho_y(x,y))/2-kappa
        > 200123867/100000000 = 2.00123867.                 (1)

Here kappa is the structured commutator coefficient accepted in N4-303,
with strict upper bound 729080538628955349/1000000000000000000.
The supremum is over the entire real plane. This is a statement about this
background alone. No inverse, stationary solution, or small-distance correction
is asserted.

## Exact representation and finite partition

N4-311 accepted the independent T4-378 reconstruction of all 40082 nonzero
rational coefficients in

    t=r^2/(1+r^2), z=cos(2theta), w=(1-t)^(delta/2), delta=1-1/c,
    D(t)=(1+2499(1-t))^19,
    rho_y = sum_(j=1)^8 w^j P_yj(t,z)/D(t),
    rho_x = sin(2theta) sum_(j=1)^8 w^j P_xj(t,z)/D(t).

Each P has degrees at most 103 in t and 80 in z. The reconstruction verifies
origin continuity, the canonical density, and the raw source. D is positive
on [0,1]. These accepted exact identities are dependencies, not inferred
from agreement at point samples.

Starting from [0,1] times [-1,1], each letter t or T selects the left or right
radial half and each letter z or Z the lower or upper angular half. The
247 recorded leaf paths form a full binary tree: every internal prefix has
exactly t,T or exactly z,Z as children, and no leaf is an internal prefix.
Induction on this finite tree proves that the closed leaf rectangles cover
the initial rectangle. Exact area two and pairwise disjoint interiors are
additional independent checks. The origin and the limiting edge t=1 are
included. Both signs of sin(2theta) are covered by the absolute value below.

## Independent range calculation reviewed here

T4-400 uses its own global Bernstein transform followed by de Casteljau
subdivision. A monomial t^k has degree-n Bernstein coefficient
binom(i,k)/binom(n,k). For z^k on [-1,1] the coefficient is

    sum_(l=0)^min(i,k) binom(k,l)(-1)^(k-l)2^l binom(i,l)/binom(n,l).

These follow by substituting z=2s-1 and using the monomial identity on
[0,1]. Halving replaces coefficients b_j by

    left_i=sum_(j=0)^i binom(i,j)2^(-i)b_j,
    right_i=sum_(j=i)^n binom(n-i,j-i)2^(-(n-i))b_j.

Substitution in the Bernstein basis proves both formulas. The exact small
fixtures check both transformations and half maps, separately from the
production reconstruction.

On a radial cell [a,b], set L=1+2499(1-a), R=1+2499(1-b). At degree n>=19
the positive denominator coefficients are

    d_i=sum_k binom(19,k)binom(n-19,i-k)/binom(n,i) L^(19-k)R^k.

They lie between R^19 and L^19. With all d_i positive, a quotient P/D is a
convex combination of its Bernstein coefficient ratios. This is the
rational Bernstein theorem accepted by N4-310 through T4-377.

The independent-w enclosure converts sum_j w^j P_j/D into degree-eight
Bernstein coefficients on [(1-b)^(delta/2),(1-a)^(delta/2)]. It enlarges
the actual correlated set, so remains an enclosure. When b<1, the second
enclosure uses the degree-six Taylor polynomial of (1-t)^(j delta/2)
at mu=(a+b)/2. For alpha=j delta/2 its remainder is bounded by

    |alpha(alpha-1)...(alpha-6)| ((b-a)/2)^7/7!
           * max((1-a)^(alpha-7),(1-b)^(alpha-7)).

Taylor's theorem proves this bound because 1-t is positive and the seventh
derivative is a constant times (1-t)^(alpha-7). Multiply each Taylor
polynomial by P_j using

    B_i^n B_k^6=binom(n,i)binom(6,k)/binom(n+6,i+k) B_(i+k)^(n+6).

Normalize at degree n+6 and add the sum of each Taylor error times the
independent bound for |P_j/D|. This proves the second range enclosure.
The edge b=1 uses only the first enclosure, avoiding a Taylor expansion
at a singular endpoint. T4-400 performs every matrix operation with
outward Arb arithmetic at 2048 bits; its complete proof and source were
read before this acceptance.

## Leaf reduction and strict margin

Let [y0,y1] enclose rho_y and [x0,x1] enclose the reduced rho_x without
sin(2theta) on a cell with angular interval [u,v]. Put X=max(|x0|,|x1|)
and s=sqrt(1-z0^2), where z0=0 if 0 belongs to [u,v], otherwise z0 is the
endpoint nearest zero in absolute value. Then |rho_x|<=sX. Since

    f(y,x)=(sqrt(y^2+x^2)-y)/2

is nonincreasing in y and nondecreasing in |x|, the cell signed defect
is bounded above by f(y0,sX). Derivatives verify monotonicity away from
the origin and continuity gives it there. The smaller of the two valid
enclosure bounds is valid. Every saved leaf must yield an upper bound
at most 2/25, with positive denominator bounds and exact matching paths.
The partition then proves the first part of (1). Substituting the accepted
strict kappa bound and exact c proves the strict second part by rational
arithmetic.

Saved 100-digit endpoint balls are wider than the unrounded Arb endpoints.
Re-evaluation encloses their exact values; its overlap with the saved
110-digit theta ball is a consistency check. For certification the checker
also requires the re-evaluated outward upper bound itself to be below 2/25.
Thus the shorter endpoint serialization cannot accidentally strengthen a
leaf's bound. The proof of the polynomial range enclosures depends on the
reviewed independent calculation and its complete hash-bound leaf records,
not on this short consistency calculation alone.

## Dependencies and verification scope

Bind the T4-400 proof, checker, parameters, manifest, result, all seven frozen
source records, and all 247 leaf bytes. Reuse the existing exact polynomial
file by its hash instead of copying it. Recheck the local source graphs of
N4-309 (original complete cover), N4-310 (rational Bernstein theorem),
N4-311 (independent full reconstruction) and N4-303 (commutator bound).
Compare the exact raw candidate and all leaf paths with the original cover.
The independent complete production ran in T4; this acceptance executes
only its own finite consistency checker. No foreign code is executed here.

Successful verification closes the independent leaf-replay step left open
in N4-309. All separately registered scalar-family and original graded-ball
exclusions for this candidate retain their stated scopes. No localized or
dyadic conclusion, no unverified norm component and no inverse claim follows.
