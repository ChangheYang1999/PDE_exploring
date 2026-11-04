# X9 theory audit addendum: endpoint correction

Written 2026-11-04T04:16:14.445509+00:00.

Correction to AT2038-2039, exchange v623 and the endpoint sentence in the frozen X9 report: Proposition FG permits s^+ <=4963249980622857/4503599627370496. Equality is admissible for far absorption; it gives zero far slack. A strictly positive margin requires the strict inequality. My earlier endpoint audit incorrectly promoted that stronger sufficient condition into a necessary condition for the accepted route. Its rational arithmetic is unchanged, but AT2038 is withdrawn in that reading. T2_PART7_v04 section2.3 and the coordinator phrase up to the threshold are correct for absorption. AN570 should retain strictness only when describing positive slack. The137/125 target retains its exact positive margin. Whole-plane strain, near, inverse and O3 remain OPEN. Read reports/X9_THEORY_AUDIT_ADDENDUM_v01.md together with the immutable X9 report.

The original report SHA256 is4eae44be20e73fbab4f0b5d71f832714f09b4889a92daab7da292088b92d9b93 and remains unchanged. This addendum supersedes only its assertion that strictness is required for far absorption. The exact coverage, numerical constants and all other verdicts are unchanged.

Proof: research/far_endpoint_scope_correction/PROOF.md. Check: research/far_endpoint_scope_correction/verification/check_v01.json, SHA256 17536a4600caa39e1d900417928c5ff47dfab669f1e6d9402636535aa0cc4070.
