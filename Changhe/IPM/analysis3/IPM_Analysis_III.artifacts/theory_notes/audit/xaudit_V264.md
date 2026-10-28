# Independent audit of V264 (proof 237): nonlinear derivative loss in the joint cofactor graph Z3

Target: verification/proofs/237_joint_cofactor_nonlinearity/PROOF.md
SHA256 at start: f53d764231c7b4c10244e2337d0715d06f652433e43e52a5349a7f9896965618 (matches expected)
SHA256 at end:   f53d764231c7b4c10244e2337d0715d06f652433e43e52a5349a7f9896965618 (unchanged)
Run date (date -u): Wed Oct 28 16:30:41 UTC 2026; file written ~16:35Z
Directory contents: PROOF.md, evidence/derivation.json. No AUDIT_CLARIFICATIONS.md exists.

Dependencies (read only), hashes checked against evidence/derivation.json, all match:
- 207_quadratic_holder_nonlinearity/PROOF.md 1088e2e8...d798 (V211; its independent audit
  evidence/opus_xaudit_V211.md, PASS WITH REMARKS, was also read)
- 236_joint_cofactor_holder_space/PROOF.md 58369aa9...688e (V261; audited in xaudit_V261.md,
  PASS WITH REMARKS)
- 234_divided_velocity_full_holder/PROOF.md 1fb068b4...cbcb65 (V257; audit pending)
No computation was run. No scratch files were created.

## VERDICT: PASS WITH REMARKS

The claim holds as stated:
- smooth compact h_n with c = J = 0, uniformly bounded in the T, A0 and Lren graph norms on Z3;
- ||N(h_n)||Z3 >= b n;
- every maximal-domain solution of Lv = N(h_n) has ||v||Z3 >= b_L n;
- rescaling gives discontinuity at 0.
The T statements are unconditional. The A0 and Lren statements depend on bounded C0 and Cren on Z3
(V261, which in turn depends on V257). The mechanism is exactly that of proof 207. The only new
ingredients are the norm comparisons (3) and (4) and the use of the actual full-plane T, and both
are correct. No gap was found.

## Findings

1. Lines 16, 25, 30 and 88. Class: REMARK (conditionality).
   The bounds for A0 h_n and Lren h_n in (1), and the control of Cv in the proof of (2) (line 108),
   use Z3 boundedness of C0 and Cren. That boundedness is V261 statement 1, which rests on V257
   (proof 234 eqs (1),(2)), whose audit is pending.
   The T-only parts need only the Z3 definition and (3)-(4):
   - (1) without the A0 and Lren terms;
   - (2) with C = 0.
   Fix: state "the A0 and Lren parts are conditional on proof 236/proof 234".

2. Lines 34 and 117 (selections). Class: REMARK.
   "Any selection of preimages ... fails continuity at zero" is correct, but one step is implicit. A
   selection S may have S(0) = v0, a nonzero element of ker L in D3. The text does not say why
   S N(a_n) cannot converge to v0. The reason is linearity: S N(a_n) - v0 is itself a maximal-domain
   preimage of N(a_n), so (2), rescaled, gives ||S N(a_n) - v0||Z3 >= b_L for every v0 in ker L.
   Note that the two-point difference argument alone would not exclude convergence to a fixed v0,
   because a generic C^alpha function has differences of exact order n^(-alpha) at distance 1/n.
   Fix: add this one sentence.

3. Lines 52-56 and 82. Class: REMARK (implicit hypotheses, as in the V211 audit remarks 1 and 3).
   - Reflection equivariance. Extending k_n^0 to the reflected boxes with V.grad z = 0 there uses
     equivariance of the actual V under both reflections: V1 odd in x and even in y, V2 even in x and
     odd in y. This holds for V = ell X + U[rho0] but is not stated.
   - Regularity. The flow box needs only C^3 regularity of V near Q, which the actual trial provides.
     The text asserts smoothness "by the actual finite inner formulas". That also needs
     pseudo-locality of U, because rho0 is smooth near Q.
   - Trajectories stay in the tube. The lower bound uses only the first box, and trajectories with
     z = 0 and z = 1/n stay in the inner tube (eta = 1, grad d = 0, zeta = 0) for s in [0, tau] by
     construction.
   Fix: state these three points.

4. Lines 72 and 5-8. Class: COSMETIC.
   The letter k denotes both the exponent k = 1615536043799051/2^53 and the strips k_n. The letter
   tau denotes both the strip time and, in proof 236, the cutoff tau_R. Fix: rename the strips
   (e.g. s_n).

5. Line 92. Class: REMARK.
   Z3 membership of N(h_n) for each fixed n is correct: it is smooth, physical parity, supported in K,
   and (3) applies. The parity check (U1 odd-even times h_x odd-odd, U2 even-odd times h_y even-even)
   is the same as in the V211 audit but is not written here. Fix: optionally add it.

## Checks confirmed

1. Norm comparison (3)
   - Choose phi smooth, even-even, compactly supported off the vertical axis, with phi = 1/x^2 near
     K. Then f/x^2 = phi f, so ||chi phi f||C^alpha <= C||f||C^alpha.
   - Only finitely many annuli meet K, and their weights are bounded.
   - L2 <= sup times area.
   - Separation from the axis also keeps K away from the origin.

2. Converse (4)
   - g is C^alpha on every compact set with norm at most C||f||Z3 (local term plus finitely many
     overlapping annuli).
   - Multiplying by the smooth function x^2 gives ||f||C^alpha(K') <= C||f||Z3.

3. Flow box and transverse velocity
   - (5) follows from the group property of the actual V flow.
   - (6) was rechecked from the multiplier: d^ = |xi|^2 P^, xi eta P^ = -(P_xy)^ and
     -xi^2 P^ = (P_xx)^.
   - On the tube: P_xx = w2, P_xy = -w1 and P_yy = 0. Hence U[d] = w, d = -w2 and grad d = 0.
   - U[d] has the velocity parities.
   - c[d] = 0, since U[d] vanishes near 0, and J(d) = 0.

4. Strips and graph bounds
   - Strips: sup is O(n^(-alpha)) and Lip is O(n^(1-alpha)). Splitting at distance 1/n gives a
     uniform C^alpha bound.
   - V.grad k_n^0 = n^(-alpha) Psi(nz) eta'(s) has no transverse factor n.
   - Strain: |c[k_n^0]| <= C n^(-alpha) n^(-1) from the smooth kernel on K. The compensator
     (parity-projected off-axis bump) is fixed.
   - h_n and T h_n are supported in K, so (3) gives (8).
   - h_n lies in D3 with no density argument.
   - With V261, C0 h_n and Cren h_n are bounded in Z3.

5. Nonlinear image
   - ||U[k_n]||inf <= C n^(-alpha)(1+log n) from the near (Holder cancellation), intermediate and
     far split.
   - On the tube: N(h_n) = n^(1-alpha) Psi'(nz)(w+U[k_n]).grad z. This is 0 on z = 0 and at least
     b_* n^(1-alpha) on z = 1/n.
   - The two points are O(1/n) apart, so the Holder quotient is at least c n. With (4) this gives
     ||N(h_n)||Z3 >= b n, for every alpha in (0,1).

6. Preimage bound (2)
   - Orbit identity (11): d/ds[e^(-s) v(Phi_s X)] = e^(-s)(N - Cv)(Phi_s X), justified for continuous
     distributional solutions by flow-box integration along almost every orbit, then by continuity.
   - The nonlinear difference is at least b_*(1-e^(-tau)) n^(1-alpha).
   - Endpoint and Cv differences are at most C||v||Z3 n^(-alpha), by (4) and bounded C.
   - Hence ||v|| >= b_L n. No existence, injectivity or inverse bound is assumed.

7. Rescaling
   - N is exactly quadratic: U and c are linear, and c[h_n] = 0 makes the X/3 term vanish.
   - a_n = n^(-1/2) h_n tends to 0 in each graph norm, while ||N(a_n)|| >= b and every preimage has
     norm at least b_L. So N is discontinuous at 0 on the smooth c = J = 0 core.

8. Scope (lines 34, 117, 123)
   - No nonexistence result, no failure for stronger or derivative-bearing norms, and no global
     inverse is claimed. The claim matches the coordinator's summary.
