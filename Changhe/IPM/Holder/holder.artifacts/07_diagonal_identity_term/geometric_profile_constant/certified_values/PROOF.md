# Certified projection-profile factors

For the planar profile g and full geometric quantity K*_alpha defined in
../PROOF.md, the following inequalities hold:

    [g]_(3/10) <= K*_(3/10) <= 1.007,
    [g]_(1/2) <= K*_(1/2) <= 1.021.

Consequently these rational numbers can replace the sufficient denominator
K_alpha in the corresponding finite projection witness theorem. All other
hypotheses of that theorem, including its restrictions on a and rho, remain.
These are upper bounds for a profile seminorm, not sharp operator norms.

## Proof

Use epsilon=1/1000000 and the exact covering algorithm in ../PROOF.md.
The code works at160-bit Arb precision and uses exact rational subdivision
coordinates. Every split replaces one closed box by two closed boxes whose
union is that box. Every box is either accepted with an upper enclosure
at most the rational target or split. Thus termination with an empty stack
certifies the whole compact region. The endpoint intervals are checked
separately. No sample determines acceptance.

At alpha=3/10, the run checked1926349 boxes and accepted963175 terminal
boxes, with maximum depth33. Its largest accepted upper bound is less than
1.006999999776; the two endpoint bounds are less than1.000000301 and
1.000009465. At alpha=1/2, the run checked1331983 boxes and accepted665992
terminal boxes, with maximum depth42. Its largest accepted upper bound is
less than1.0209999990; the endpoint bounds are less than1.000000501 and
1.000250001. In each case the accepted count is exactly one more than the
number of split boxes, as expected for the binary tree.

The geometric reduction in ../PROOF.md and the nonexceptional-pair
estimates in ../../finite_projection_extended/PROOF.md prove the seminorm
inequality from the covering. Independent real-coordinate diagnostics
checked719130 sampled points in rational boxes and500000 arbitrary pairs.
Their agreement supports the audit; the complete interval covering and
analytic reduction provide the proof.

All proof, code and exact JSON input dependencies are hashed in the adjacent
verification manifest. The underlying certificate source list omitted the
extended-range proof because it used a stale optional path; the manifest
here explicitly includes that required dependency.
