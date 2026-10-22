# Review resolutions and final scope

The actual Claude Opus 5.5 review ended at 2026-10-21T14:30:42Z. Its finite scalar conclusion agrees with the independent calculations. The following qualifications are mandatory parts of the result.

1. Derivative-order labels. Of the 7,809 middle rows, 7,432 have `nder = 2` and 377 have `nder = 5`. All 2,632 inner and 8,948 outer rows have `nder = 2`. Every row has all six fields with i + j <= 2, and every saved second-order field is strictly positive. The frozen source loops over i in range(nder + 1) and j in range(nder + 1 - i), so `nder = 2` explicitly includes (2,0), (1,1), and (0,2). The supplementary checker verifies the source statements and all row fields. This excludes missing or zero placeholder fields in these saved files. It does not establish that the values are genuine derivative majorants. That remains an explicit hypothesis of the physical implication, and remains OPEN.

2. Locations. Cell 4124 maximizes the saved gradient and R5 expressions, and cell 4123 maximizes the saved second-partial expression. No claim is made that a physical supremum is attained in those cells or at their left endpoints. The radius displayed by the producer is not independently certified here.

3. Completion. The last paragraph of ADDENDUM.md was written before the second calculation completed. It is retained unchanged to preserve its recorded digest. The completed evidence is compute.json at 14:27:33Z, independent.json at 14:29:15Z, and coverage.json at 14:29:59Z. The latter two establish all 19,389 ordered rows, 232,668 exact comparisons, 465,336 interval enclosures and the complete footer. This document supersedes only that pending-status sentence.

4. Terminology. The review calls the ceilings for K and E K “inward-safe”; the appropriate term is outward upper ceilings. This audit's exact rational outputs, not that wording, determine the direction. For R5 an outward replacement is 0.427444, since the exact saved ratio is strictly smaller. The larger suggestions 0.42745 and 0.428 also dominate it.

The finite arithmetic verdict is CONFIRMED. The claim that 0.427 is an outward ceiling for the saved middle R5 majorants is REFUTED. Physical derivative Taylor models, canonical inputs, weight bounds, geometric coverage, tails, inverse bounds and every IPM endpoint remain OPEN. No saved upper majorant is interpreted as a lower bound on the physical residual.
