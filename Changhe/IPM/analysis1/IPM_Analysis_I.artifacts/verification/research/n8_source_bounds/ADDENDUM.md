# Review clarification

The first actual Opus5.5 review accepted the limited scope at 2026-10-21T01:05:38Z. Its request ID is 9f035db6-e095-4c03-862f-e5d85c4f9e3a. This addendum narrows two comments before closure.

1. The exact missing-point computation compares the reported cover endpoint, which is a floating np.exp result. Thus the directly proved statement is a metadata coverage obstruction. A separate directed exponential check should establish the actual radial endpoint before extending this to the exact runtime domain. The review's phrase negligible rounding is not itself a rigorous bound. No derivative supremum certificate is accepted.

2. Extending a polynomial range beyond h_up does not by itself require extending the Taylor remainder theorem. If the actual target points remain inside [0,h_up], bounding the polynomial on a larger interval and using the remainder only on target points is valid. The real obligation is that each target point be covered by the polynomial range paired with its coordinate-factor range, including the existing coefficient radii. The mismatch is an unresolved proof obligation, not a verified counterexample to the computed enclosures. The review's assertion that a remainder extension is necessarily required is too strong.

3. The exact scalar comparisons in checks.json are comparisons of reported numbers only. They verify the conditional constants, not the coefficient hypotheses. The imported source estimate is conditional and topic80 must accompany topic77.
