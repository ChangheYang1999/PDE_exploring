# Audit of the repaired finite-cell range enclosure

## Claim and assumptions

The inspected snapshot of encl.py is identified by SHA-256
b2b88870afe8ab420075305be0bfd6ff68a6b377a9ecb7cf520d355a4c1d408f.
It replaces the unsound interval union of proof 55 and adds finite-cell
resonance merging. Assume a finite exponential polynomial

    f(s)=sum_e exp(e s) p_e(s), 0<=s<=h,

with exact rational exponents, h>0 exact rational, and finite Arb balls
enclosing every coefficient. Assume arithmetic produces finite balls and
the directed conversion fup returns a floating upper bound of its input's
exact upper endpoint. Then the snapshot's range_finite encloses the range
of f. The proof concerns this finite-cell method, not an entire margin or
hypothesis-A certificate.

## Resonance merging

For any choice of base exponent e0 and integer J>=0,

    exp(e s)p_e(s)
      =exp(e0 s) sum_{j=0}^J ((e-e0)s)^j/j! p_e(s)+R_e(s).

Taylor's theorem for the exponential gives, uniformly on the cell,

    |R_e| <= max(1,exp(e0 h))
             (sum_a |c_(e,a)| h^a)
             (|e-e0|h)^(J+1)/(J+1)! exp(|e-e0|h).            (1)

Every quantity on the right is enclosed in Arb before its final directed
upper conversion. Polynomial multiplication and summation create the
merged coefficients with outward error. The sum of (1) is a uniform
additive radius for the merged exponential polynomial.

The code's float choices of clusters and base exponents affect efficiency
and tightness only: (1) holds for every exponent difference. In particular
no proof step assumes that the heuristic test |e-e0|h<=1 was exact. Each
term belongs to one cluster and is included exactly once. The array length
len(p_e)+J accommodates its largest degree deg(p_e)+J. A singleton cluster
is copied unchanged.

Increasing the arithmetic precision for merging is safe but cannot undo
radii already introduced when constructing the input coefficients. Useful
near-resonance cancellation therefore requires sufficiently precise input
coefficients as well. It is not enough to increase precision only after a
low-precision primitive expansion was formed.

## Taylor enclosure and union

For the merged function g, let m=h/2 and r=h/2. Taylor's theorem gives

    g([0,h]) subset g(m)+[-R,R],
    R=sum_{j=1}^K |g^(j)(m)| r^j/j!
                +sup_[0,h]|g^(K+1)| r^(K+1)/(K+1)!.

The coefficient-sum estimate used for the last derivative is valid term
by term: |s|^a<=h^a and exp(e s)<=max(1,exp(e h)). The code computes the
bound with Arb and converts its upper endpoint by fup, so the symmetric
radius cannot round below the bound. Derivative evaluations at the
midpoint are themselves enclosed.

The exact rational subintervals are [i h/N,(i+1)h/N]. ExpPoly.shift is a
binomial shift with outward exponential and polynomial arithmetic; their
union covers the entire cell regardless of how the integer N was chosen.
For each subinterval the new code retains its exact dyadic lower and upper
endpoints. It takes their minimum lo and maximum hi, then constructs

    (lo+hi)/2 + [-fup((hi-lo)/2), fup((hi-lo)/2)].

The midpoint is computed in Arb, so any midpoint rounding is included in
its own radius. This ball contains [lo,hi]. It therefore contains every
subinterval enclosure. The uniform resonance remainder is added at the
end, proving the claim. This is precisely the step that was invalid when
lo and hi were independently rounded to nearest floats before the union.

## Independent checks

The former counterexample is

    f(s)=1+2^-80+2^-200 exp(10s), 0<=s<=1.

The old snapshot excluded f(0); the present one contains it. This is a
regression check of the actual implementation, in addition to the proof.

A second test uses the exact original-data exponent difference
lambda=75/70368744177664 and

    q(s)=exp(-52s) integral_0^s exp(-lambda u)u^6 du.

It has two large primitive terms at exponents -52 and -52-lambda.
The primitive coefficients are constructed at512 bits. The unmerged
single-cell Taylor radius is greater than1.37e94. Resonance merging and
subdivision give a radius less than3.523e-7. Sixty-five independently
evaluated points, using the stable phi series of proof 56, are contained.
The sampled containment is not the continuum proof; the preceding Taylor
and remainder argument supplies that proof.

The generic bound is intentionally loose here. Proof 56's special
positive-kernel half-line estimate is much tighter for this test.

## Scope and remaining obligations

This confirms the repaired finite-cell algorithm and withdraws the
current applicability of V058 to this new snapshot. V058 remains a valid
verdict for its archived old snapshot. No change to an old verdict's
historical evidence is made.

The full certificate still needs every original coefficient and Green
endpoint enclosure, all radial and angular cells, the half-line bounds,
normalization identities for any discarded constants, and every reported
minimum/maximum. Half-line cells in this snapshot still use separate
coefficient-sum bounds; finite-cell resonance merging does not repair or
quantify those automatically. No global positive margin, axis rate or
inverse is asserted.
