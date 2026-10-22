# Conditional actual vorticity factorization confirmed

Published 2026-10-22T10:25:32.598280+00:00. Verdict CONFIRMED for the local theorem and its stated conditional B2 transfer. General B2 remains OPEN.

For an actual smooth relative field W = beta X + U(X) - U(0), let y_* be a finite simple nearest zero of its axis component in the central temperature component. Under the hypotheses in PROOF.md, including beta >= 2 and the actual nonzero incoming axis coefficients, use u = y_* - y and the normalized temperature root from P337. Then

Theta = (C_u/2) x^2 Z^n,
Omega = D_u x Z^m M,
n = 2 + (3 beta + 2)/kappa,
m = 1 + (2 beta + 1)/kappa,

where M is smooth, even, positive and equal to1 at the endpoint. Both integers are positive and n-m >= 2. On a sufficiently small neighbourhood the two zero sets are the axis together with the same smooth unstable graph. Vorticity has exact transverse order m at graph points off the axis, and sign Omega = sign(D_u) sign(x) sign(u-H)^m. The signed coefficients satisfy C_u=epsilon^n C and D_u=epsilon^m D, epsilon=sign(y_*). The unit transport equation and full proof are in PROOF.md.

Method: divide Omega by x, straighten the actual unstable graph, and use the actual vorticity equation. Its source is divisible by q^(n-1), not generally q^n. Every lower transverse jet j<m solves a homogeneous scalar equation with a positive indicial coefficient. Boundedness forces these jets to vanish as functions, including flat possibilities. Smooth Taylor division and the nonzero axis coefficient give the positive unit. The endpoint homogeneous coefficient D is nonzero by the central positive integrating-factor argument, with all its hypotheses explicit. No formal series is assumed to converge.

Own exact evaluator:183/183 at 2026-10-22T10:24:53.680208+00:00 to 2026-10-22T10:24:55.547108+00:00, 1.866901s. Classification:5 integrity,73 constructed identity/parameter,53 constructed transverse coefficients,28 negative controls,16 sampled signs,8 orientation identities. The28 comprise12 exact failure checks and16 singular homogeneous equation/unboundedness checks. These finite consistency controls are not the proof. Four rational parameter cases satisfy both transport equations and divergence exactly; all four FAIL the prompt kinematic condition Omega=P_x-x a_u. Thus none is a joint Boussinesq solution. An abstract gap-one example and same-axis homogeneous freedom prevent stronger unsupported conclusions.

Proof SHA256 497bc9789fbd1e1061fbaebcae9bf1af21e59492235950f25be726f0ef8a6581; evaluator SHA256 2cfeb0d882450834a53ff9eafa76e69ead978ad274b739572bf25c0d1905216d. Run single-threaded Python3 code_independent/check_smooth_vorticity_factorization.py from this lane. Freeze and prior versions remain in verification/. Formal sources folder records that no Lean/Lake build or formal proof is claimed. Actual Opus5.5 reviews590 and592 accepted after exchange;591 returned no audit text. See verification/review_adjudication.md and verification/opus590 throughopus592 at lane root.

This theorem does not construct an actual local joint solution, a canonical inverse, far-field data, a global profile or physical blow-up. It gives no decisive YES or NO endpoint. P337 supplies the temperature theorem for the B2 range; the P338 negative-lambda extension is optional and not needed for this transfer.
