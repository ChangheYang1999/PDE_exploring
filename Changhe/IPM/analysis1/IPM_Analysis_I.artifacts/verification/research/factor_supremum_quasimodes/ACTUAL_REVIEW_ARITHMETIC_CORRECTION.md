# Arithmetic correction to the actual packet review

Written 2026-10-22T09:33:35.395362+00:00 after reading the full actual Claude Opus5.5 response request972bcc5e-3cc2-4a68-bbe4-0a938959ee88, end09:31:05.102261Z.

The response's first mode-2 table bullet is wrong. The exact formula has coefficient1/8 and primitive bounds |J1|<=delta^2/2 and r^-4|I5|<=delta^2/6. The triangle bound is (1/8)(1/2+1/6)=1/16+1/48=1/12, not1/8+1/24=1/6. No sign cancellation is used; it holds for arbitrary signed chi with |chi|<=1. The proof and both finite scripts use the correct coefficients. The review's attempted nonnegative-sign justification is rejected. This needs an explicit actual follow-up before final acceptance.

The rest of that derivative bullet is correct: Dpsi2 gives1/8+1/24+1/4=5/12; D2psi2 gives1/4+1/12+1+B1/4=4/3+B1/4. Own fmpq exact checks below accompany the follow-up request.

The earlier follow-up heading says it follows request6c14ad95, which is correctly the first request being answered. Its own request ID is10e0ffd7 as the metadata states. Calling this a labeling slip is unnecessary, but the metadata binding is unambiguous.

The frozen original gate checks the main actual packet review and later adjudication. The new external_final_check.py additionally authenticates this arithmetic follow-up and rehashes the supplemental file map contained in the final adjudication JSON. Final acceptance will require both checks.
