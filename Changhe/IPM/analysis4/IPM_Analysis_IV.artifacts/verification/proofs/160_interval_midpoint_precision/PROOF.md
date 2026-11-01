# Interval arithmetic does not promise full-precision midpoints

Status: exact logical observation; a reproducible finite implementation test follows.

## Statement

An interval enclosure computed with a 512-bit arithmetic context does not,
by itself, certify that its midpoint is a 512-bit approximation to the
target value. The midpoint error is bounded by the interval radius when
the target is enclosed, not by the context's nominal unit roundoff.

This applies to the canonical logarithmic continuation after its
coefficient radii become large. It does not invalidate a valid enclosure
or an independently narrow norm bound.

## Proof

Let the exact target be x and let an arithmetic procedure return
I=[m-r,m+r], with x in I. The enclosure proves only |x-m|<=r.
The procedure may choose a midpoint m with fewer significant bits
whenever the radius still encloses x. For example, the interval
[1-2^-10,1+2^-10] encloses x=1+2^-11, although its midpoint error is
2^-11. Both endpoints can be represented exactly with 512-bit arithmetic.
No property of this example depends on rounding the endpoints poorly.
Thus a context size alone cannot replace the radius in an error bound.

## Controlled polynomial test

Choose two length-16 polynomials with exact dyadic coefficients
A_i=u_i/2^30 and B_i=v_i/2^30. The integer lists are retained in the
verification JSON. Their exact product is computed by independent
integer convolution:

    C_k = 2^-60 sum_(i+j=k) u_i v_j.

For each q in {8,20,80}, give every input coefficient the same midpoint
as above and radius 2^-q. Multiply these interval polynomials in the
installed Arb implementation at a 512-bit context. Compare each returned
interval and midpoint with C_k in exact Fraction arithmetic.

The test checks two separate propositions: every interval contains the
exact product coefficient, and at least one midpoint differs from the
exact coefficient when q is8 or20. A zero-radius control checks that
the exact product is representable and is recovered exactly in this
case. These are finite implementation observations, not a theorem about
every polynomial degree or every Arb algorithm.

## Consequence and scope

After discarding input radii, new narrow output balls certify recurrence
from the selected midpoints only; see53 and V305. If those midpoints
were computed from wide balls, they need not have the accuracy of a
separate point-arithmetic run at the nominal context precision. A fresh
continuation, independent arithmetic comparison or an error-propagation
argument is required to assess their accuracy.

The controlled example does not quantify the errors of any particular
high-order IPM coefficient. Such coefficients must be assessed from
their own enclosures or independent checks.

## Completed check

At 2026-10-31T11:55:36+00:00, the zero-radius product was exact. The radius2^-8 and2^-20 tests each had29 nonzero midpoint errors, with respective maxima2442083/72057594037927936 and867/72057594037927936. All93 output enclosures contained their exact targets. The radius2^-80 test happened to recover every midpoint exactly. Independent exact replay at2026-10-31T11:59:10+00:00 passed. This confirms the stated limitation without weakening any valid interval enclosure.

At 2026-10-31T13:34:51+00:00, the latest reset329 report was rechecked against the current reset code. Its new narrow radii enclose continuation from the selected midpoint arrays; they do not propagate the previously certified329 intervals. No claim about exact original coefficients at341,344 or345 follows solely from that reset computation. The original unreset bounds used inV271 remain valid. Evidence:verification/reset329_scope_1324.json.

## Propagation correction at 2026-10-31T13:59:06+00:00

The 13:58 numerical note says the absolute uncertainty of orders330..350 equals the uncertainty of the329midpoints, about2.5e-6 relative. Section5.11b also says it grows by at most the same propagation factors, without providing such a bound. The reset code deletes every old radius. Its new narrow intervals therefore enclose only the continuation from the midpoint arrays. A simple exact quadratic counterexample is F(x)=1+10^6(x^2-1), x in [1-e,1+e], e=1/400000. The reset input1 produces F(1)=1 with zero arithmetic radius, whereas the allowed input1+e produces error5.00000625. Thus narrow reset output balls do not quantify propagation of the discarded uncertainty. This example refutes the inference, not the particular IPM values. The actual inherited error at350 remains OPEN. Comparing two reset runs is a diagnostic, not that missing proof. Original unreset V271 inequalities remain valid.
