# P231: beta2 requires variation in a finite axis ratio

Published 2026-10-22T00:18:08.987142+00:00. CONFIRMED by complete proof and32 own exact controls; external review unavailable.

For smooth full-plane B2 at beta2, if Theta_xx(0,y) never vanishes, then Theta_xxxx/Theta_xx² and partial_x^6Theta/Theta_xx³ cannot both be constant along the entire axis. No exact separated representation or symbol estimate is assumed. The finite Taylor remainder protects the same two vorticity identities used in P227; their finite elimination and singular uniqueness are included in the standalone proof.

Controls took57.176765s. Actual Opus5.5 request454 returned no written review. Separate lead audit pending. This necessary variation condition leaves general B2 OPEN.

# Independent adjudication of the lead review of P231

Read in full and adjudicated on 2026-10-22T00:33:37.873267+00:00. Verdict: CONFIRMED within the original theorem's hypotheses.

The lead review audit_p231 returns VALID with 37 separate exact controls. The verifier has compared its derivation with the already completed independent proof and exact controls, rather than adopting its verdict alone. The frozen answer SHA256 is 417ff2f682c448b511fe565d2a32e757d8dba7d6fad5ebe669465f25b977f818.

The scale normalization gives B0=A0^2 I2/6 and D0=A0^3 I3/120. Smooth remainders, including mixed derivatives, yield deltaW2=O(k^6), deltaW1=O(k^7), deltaOmega=O(k^5), and comparison residual O(k^5). Exactly the first and third coefficients vanish; a fifth coefficient equation is not available. The elimination polynomial, nonzero resultant, Bezout certificate and flat regular-singular uniqueness agree with the verifier's prior calculations. The derivative count six describes the constrained temperature jets, while full smoothness remains a hypothesis.

Additional referee example checked by direct reasoning before computation: take W1=0, W2=4y+c2*x^2+c4*x^4+d6*x^6, Theta=-c2*x^2-c4*x^4-d6*x^6, Omega=-2c2*x-4c4*x^3-6d6*x^5, c2<0. Then divW=4, Omega=-curlW, both transport equations hold because every scalar is independent of y, and the required parity and nonzero center jet hold. It fails the required asymptotic W2/y->2. Dropping d6*x^6 from the comparison velocity while retaining the true temperature produces residual 6d6*x^5, so a fifth coefficient cannot be used. This is a local algebra stress test, not an admissible profile.

The review attempted Opus 5.5 collaboration but credential retrieval failed before inference. No model was invoked or substituted in that attempt. The verifier's actual Opus request 454 returned no written mathematical audit, so no Opus endorsement is claimed. General B2 remains OPEN.
