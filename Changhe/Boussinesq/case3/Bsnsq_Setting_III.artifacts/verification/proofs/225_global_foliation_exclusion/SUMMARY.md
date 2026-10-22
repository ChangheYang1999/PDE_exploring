# P225: global separated temperature excluded at beta2

Published 2026-10-21T23:39:48.085212+00:00. Verdict CONFIRMED within the following scope: a positive C3 scale a on the whole real line, nonconstant C1 H, and C2 W cannot satisfy Theta=H(x/a(y)), div W=4, W(X)=2X+o(|X|), the beta2 temperature and vorticity equations, and Omega=-curl W. Neither parity nor an inverse assumption is required. General smooth B2 temperatures remain OPEN.

PROOF.md was completed before symbolic verification. The regular set of H is bounded by the horizontal limit. On a nonzero critical endpoint curve, continuity extends the regular-strip identities. The vorticity source vanishes, compact backward flow forces vorticity on this curve to vanish, and a becomes monotone or constant. This forces a bounded end, contradicting the vertical limit.

Independent controls: 39 PASS, 2026-10-21T23:26:45.935546+00:00 to 2026-10-21T23:26:46.361785+00:00, 0.426261 seconds. An initial 38/39 run had an unresolved symbolic derivative representation; canonicalizing the physical derivative before the critical substitution repaired the checker. Initial code/results and recovery explanation are retained. Numerical or symbolic finite controls do not replace the global proof.

Actual Opus5.5 request444 independently confirmed the proof (81.430082 seconds); requests440-442 supplied no audit and remain recorded as such. See verification/review_adjudication.md and the root verification/opus444_beta2_critical_followup directory. No formal build was attempted.
