# Independent audit of V261 (proof 236): joint cofactor Holder space Z3

Target: verification/proofs/236_joint_cofactor_holder_space/PROOF.md
SHA256 at start: 58369aa93dbfd1dd90cf8b305f3a1ab3f143dbb38bb2359fbf2b57e59049688e (matches expected)
SHA256 at end:   58369aa93dbfd1dd90cf8b305f3a1ab3f143dbb38bb2359fbf2b57e59049688e (unchanged)
Run date (date -u): Wed Oct 28 16:20:15 UTC 2026 (start); file written 2026-10-28 ~16:30Z
Directory contents: PROOF.md, evidence/derivation.json, evidence/derivation_initial.json.
No AUDIT_CLARIFICATIONS.md exists for proof 236.

Dependencies read (read only), hashes checked against evidence/derivation.json, all match:
- 234_divided_velocity_full_holder/PROOF.md   1fb068b4...cbcb65 (V257; own audit pending)
- 228_scaled_quadratic_axis_space/PROOF.md    dc9ffef5...cd31d3e
- 228_scaled_quadratic_axis_space/AUDIT_CLARIFICATIONS.md 420f095e...7cd34
- 217_full_moving_tail_holder/PROOF.md        a4a9e82a...575477
- 217_full_moving_tail_holder/AUDIT_CLARIFICATIONS.md ebabca8b...adee9f
Also read: 222 (PROOF + both clarification files), 223 AUDIT_CLARIFICATIONS, 227 AUDIT_CLARIFICATIONS,
213 (PROOF residual section + clarification), 232 (PROOF + AUDIT_CLARIFICATIONS, the V256 packets).
No computation was run. No scratch files were created.

## VERDICT: PASS WITH REMARKS

Every claimed statement (Banach space and Z3->Z2 embedding; bounded C0, Cren with the tail bound (2);
F0, H0, M0 in Z3; closed maximal domains for T, Lren, A0; nonclosable J; exterior bijection for T_R and
A_R^(3) with R-uniform inverse; exact discrepancy (5); unboundedness of the V256 packets in Z3) was
re-derived and holds, conditional on V257 (proof 234 eqs (1),(2)). V261 uses only what V257 states; it
needs nothing beyond V257. One citation-level gap (finding 1, horizontal derivative of M0/x^2) must be
closed by a clarification, but the needed bound follows from cited finite-mode structure. No scope
overstatement was found.

## Findings

1. Lines 91 and 23-27 (M0 column cofactor). Class: NEEDS CLARIFICATION.
   Joint C^alpha of M0/x^2 needs bounds on BOTH Cartesian derivatives, locally and at infinity.
   Proof 217 eqs (4) and (6) give only |m0/x^2|, |partial_y(m0/x^2)| and the UNDIVIDED partial_x m0.
   They do not give partial_x(M0/x^2). For the thin vertical cone, the bound
   |grad(M0/x^2)| <= C r^(2k-4)(1+log r) is in proof 232 AUDIT_CLARIFICATIONS item 1. V261 needs it at
   every angle and on B4. Line 91 cites only "the exact differentiated finite-mode formula in proof 217".
   The claim is true. Fix by adding three sentences:
   (i) At infinity, divide proof 217 eq (5) (finite smooth angular factors, fixed cylinder derivatives)
       by cos^2(theta) at all angles, as in 232 clarification 1. This gives
       |grad(M0/x^2)| <= C r^(p-3)(1+log r), hence M_R(M0/x^2) <= C R^(p-2)(1+log R).
   (ii) Near 0, proof 217 eq (3) with U[zeta]=c[zeta](-x,y)+R_zeta gives
        n'_0 m0/x^2 = c[zeta](-(2/3)a1+(4/3)y a2) + a1 R_zeta1/x + a2 R_zeta2.
        This is Lipschitz, because a1 and a2 are Lipschitz and R_zeta is smooth near 0 (zeta vanishes
        there), with R_zeta1 odd in x.
   (iii) On the compact punctured region, use the C6 joins and smooth axis division.
   The same remark applies to the H0 cofactor chi0(a1+y a2)/3. That one is immediate from Lipschitz
   a1, a2.

2. Statement section, lines 3-48, versus lines 68-75 and 172. Class: REMARK (conditionality).
   The mapping theorem depends on V257:
   - proof 234 eq (2), the joint annular C^alpha of U1/x, at lines 68-71;
   - proof 234 eq (1), the compact quotient lemma, at line 75.
   Without them, the horizontal cofactor seminorm of a1 U1/x costs the factor q^(alpha-1) of
   proof 232 (3)-(4). Z3 boundedness of the coupling would then fail to follow. This conditionality
   appears only at line 172; it is not in the theorem statement. V261 applies (1) to x^2 chi' g with
   chi' g jointly C^alpha, which is more than the vertical C^alpha that (1) requires. It applies (2)
   via Z3 -> Z2. So V261 needs NO hypothesis beyond V257's statement.
   Fix: add to the statement "conditional on the pending audit of proof 234 eqs (1),(2)".

3. Lines 68-71. Class: COSMETIC.
   The first line of (6), ||U||_inf + R^alpha[U]_C^alpha <= C N R^beta, is proof 222 eq (4) and
   proof 228 eq (6). It is not from proof 234. Fix: attribute it to proof 222/228.

4. Lines 113, 119, 168. Class: COSMETIC.
   - The packets at line 168 are introduced in proof 232 (V256), eqs (8) and (10). Proof 234 only
     restates them, at its line 171. Cite proof 232 as the source.
   - The symbol q is used three ways: the strain-normalizing bump (line 113), 1/a (line 119), and the
     packet scale (line 168). Rename two of them, e.g. q_c and s.

5. Line 40. Class: COSMETIC.
   D_R^(3) is named but never written out. Fix: state
   D_R^(3) = {h in F_R^(3): V.grad h in F_R^(3) distributionally on Omega_R}, as in proof 228 (b).

6. evidence/derivation.json and lines 93, 158, 172. Class: REMARK (provenance).
   The manifest hashes only 234, 228 (+ clarifications) and 217 (+ clarifications). The proof also
   uses the following, without naming the topics at lines 93 and 158:
   - proof 213: F0 = x^2 y B; B = O(r^2) near 0 and O(r^(2k-4)) at infinity with cylinder
     derivatives; C5 joins; weighted threshold gamma > 4k.
   - proof 222: canonical velocity, eq (4), and the far F0 expansion.
   - proof 223 AUDIT_CLARIFICATIONS item 4: C1 flow boxes, at line 158.
   - proof 228 AUDIT_CLARIFICATIONS item 5: time-change equivalence.
   - proof 232: the packets, and clarification 1 if adopted for finding 1.
   Fix: add these citations and their hashes.

7. Line 158. Class: REMARK.
   "Obeys the same orbit relation off the vertical axis, and continuity extends it through that axis"
   is correct but unnecessary. On r >= R0/2, V is C1 and nonvanishing, with V2 > 0 on the axis. The
   flow-box argument therefore applies on the axis directly. No change is needed.

8. Line 168 and line 48. Class: REMARK (supports the scope statement).
   Rescaling the packets does not rescue the V256/V257 open-mapping argument in Z3. The rescaled
   packets eps^alpha F_(q,eps) are bounded in Z3. With them, inequality (20) of proof 234 becomes
   b eps^alpha q^2 lambda^(-1/2) <= C N q^2 lambda^(-alpha), i.e. b q^(alpha-1/2) eps^(1/2) <= C N.
   For alpha >= 1/2 the left side is at most q0^(alpha-1/2) eps^(1/2), which tends to 0. For
   alpha < 1/2 it equals lambda^(-1/2) q^alpha, which also tends to 0.
   So there is no contradiction for any alpha in (0,1). This agrees with V261's statement that the
   unboundedness concerns that specific proof and is not evidence of surjectivity.

9. Line 75. Class: COSMETIC.
   The radii of the local split are not specified. For example, take chi' = 1 on B8 and supported in
   B16, with output disk B4. The remote input is then separated from the output by at least 4, which
   the smooth subtracted-kernel bounds use. Fix: state the radii.

## Checks confirmed

(a) Norm and space
- g is uniquely determined: by h off x=0 and by continuity on x=0.
- The parities are consistent: h even in x iff g even in x (x^2 is even), and h odd in y iff g odd
  in y.
- The norm is definite (continuity plus the L2 term).
- Completeness (line 62) holds: local uniform convergence, lower semicontinuity of the Holder
  quotients, and identification of the L2 limit.
- The scaling is consistent: |g| <= N R^(beta-2) and [g] <= N R^(beta-2-alpha) give |h| <= C N R^beta,
  which is exactly Z2 homogeneity.
- Z3 -> Z2 (lines 54-60) was verified:
  - |x^2 - x'^2| <= 8R|x - x'| <= C R^(2-alpha)|x - x'|^alpha on A_R;
  - the divided vertical quotient of h equals the vertical quotient of g;
  - ||chi h||E2 <= C||chi g||C^alpha, including pairs leaving supp chi.
- Dyadic overlap, grid equivalence and the cutoff and multiplier bounds (lines 52, 64) hold with no
  segment condition.

(b) Coupling
- Identity (7) is exact: U.grad rho0 = U1 x a1 + U2 x^2 a2.
- The far orders hold: M_R(a1) <= C R^(k-2) and M_R(a2) <= C R^(k-3), from Lipschitz bounds with
  R^alpha R^(1-alpha) = R.
- Product rule M_R(fg) <= C M_R(f) M_R(g) gives (8):
  R^(k-2) R^(beta-1) + R^(k-3) R^beta = R^(beta+k-3) = R^(beta-2) R^(k-1).
  Then R^(2-beta) times this is R^(k-1).
- Weighted tail: integral_R^inf r^(2beta+2k-1-gamma) dr gives R^(beta+k-gamma/2), finite since
  gamma > 4k > 2beta+2k.
- Origin disk (line 75):
  - the compact part uses V257 (1) and the compact Riesz C^alpha bound;
  - the remote part's first two kernel derivatives, O(|Y|^-3) and O(|Y|^-4), are integrable against
    |Y|^beta for beta < 1;
  - odd-x parity gives U1/x;
  - a1 = 2y+O(r^3) and a2 = 1+O(r^2) are Lipschitz.
- Column: M_R(M0/x^2) <= C R^(p-2)(1+log R) and the L2 tail is R^(2k-gamma/2)(1+log R) (subject to
  finding 1). The c bound comes via Z2 (proof 222 (5)).
- All four exponents in (2) are negative: k-1; beta+k-gamma/2 < 2k-gamma/2; p-beta; 2k-gamma/2.
- Crossing pairs are handled by the multiplier lemma, and the local term vanishes for R >= 4.

(c) Residual
- F0/x^2 = yB.
- Far: |yB| = O(r^(p-2)) with gradient O(r^(p-3)) from cylinder derivatives, so
  R^(2-beta) M_R = O(R^(p-beta)), bounded for beta > p.
- Origin: yB = O(r^3) with gradient O(r^2). The joins are C5. L2 is finite iff gamma > 4k
  (proof 213).
- H0 cofactor chi0(a1+y a2)/3 is Lipschitz.

(d) Domains
- Z3 convergence implies local uniform convergence, hence distributional convergence of V.grad h.
  So D3 is closed.
- Bounded C0 and Cren give equal maximal domains for T, Lren and A0, and closedness.
- No density assumption is used.

(e) Exterior inverse
- W1 = V1/a = x exactly, so (Psi_t X)_1 = e^t x and f(Psi_t X)/x^2 = e^(2t) g_f(Psi_t X) exactly.
- (9) was verified:
  - sup: e^(2t) N (r e^t)^(beta-2) = N r^(beta-2) e^(beta t);
  - seminorm: e^(2t) N (r e^t)^(beta-2-alpha) (C e^t)^alpha = C N r^(beta-2-alpha) e^(beta t);
  - images of A_r lie in Omega_R at radii comparable to r e^t;
  - chord segments of close pairs stay in r >= r/2 >= R0/2.
- Multipliers: m_t (R|D m_t| <= C e^(-kt) R^(k-1)) and 1/a (Da = O(r^(k-2))) are even-even, and
  Psi_t commutes with both reflections. Integrating e^((beta-k)t) gives (10).
- Weighted L2:
  - the Jacobian e^(-2t) and weight factor e^(gamma t) give e^((gamma/2-1)t), with denominator
    k+1-gamma/2 when gamma < 2+2k;
  - otherwise the pointwise r^beta bound gives (11), whose exponent beta+1-gamma/2 <= beta-k < 0;
  - both cases have R-uniform constants.
- Cocycle: Q_R f(Psi_s X) = -(1/m_s) integral_s^inf m_tau (f/a)(Psi_tau) dtau gives
  W.grad Q = q Q + f/a, hence V.grad Q_R f = Q_R f + f.
- The terminal term m_t h(Psi_t X) = O(e^((beta-k)t) r^beta) tends to 0 (lower radial comparison
  when beta < 0). So Q_R T_R h = h and T_R Q_R f = f, and the graph norm of the inverse is at most
  2K+1.
- B_R = P_R tau_(R/2) C0 E_R is small by (2), and the Neumann formula Q_R(I+B_R Q_R)^(-1) was
  verified two-sided.
- (5) was verified from T(eta h) = eta T h + h V.grad eta.
- V.grad eta_R is even-even, O(1), with scale-R derivatives.

(f) J nonclosable
- g_eps = y zeta(X/eps) = eps G(X/eps) has sup <= C eps and Lip <= C, so C^alpha <= C eps^(1-alpha).
  Annular terms vanish for eps < 1, and L2 is O(eps^4).
- (T h)/x^2 = V.grad g + (2V1/x-1)g is exact.
- Vlin = (-(2ell-1)x, (4ell-1)y) agrees with the normalization c = 3ell-1, and div = 2ell.
- Linear terms are eps (Z.grad-type G)(X/eps), of C^alpha size eps^(1-alpha). W terms have sup
  eps^3 and Lip eps^2, so size eps^(3-alpha). W = O(r^3) by parity (no quadratic terms).
- c[h_eps] = eps^2 c[H] from the order -3 kernel.
- The parity-projected off-axis bump has c = 1 and J = 0 and is fixed in the graph.

(g) Packet cofactor phi(x/q)cos(x/eps)g(y)
- Take points pi*eps apart inside phi = 1 (|x| <= 2Bq, possible since lambda = q/eps -> inf). The
  quotient there is 2|g(y)|/(pi eps)^alpha.
- The fixed correction c[F]q_c is bounded. So the Z3 norm is at least c eps^(-alpha) - C, which
  diverges. The claim is correct.

(h) Scope
- No global inverse, Fredholm property, closed normalization, Sobolev condition (I), existence,
  range of F0 or cokernel claim is made (lines 48, 164, 172). The INDEX entry matches.
- Line 48 correctly says proof 234 does not decide surjectivity on Z3.
