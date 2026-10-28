# Independent audit: proof 244 sharp renormalized coupling tail (V278, V281)

Target: verifier/proofs/244_sharp_renormalized_tail/

SHA256 checked (sha256sum, 2026-10-28):
- PROOF.md                 c1816d9ce3e8bfccb7aeae16978d775783a9c67d0d91f2bc434cd02092211d50 (matches expected)
- AUDIT_CLARIFICATIONS.md  108a6eb6e022f7c73c091a90b16d2b442ed65797471e07125505db8310ff385b
- evidence/derivation.json 613b0748a9e105d1afb7137371184bb0bcecddf84cbe9e8817f08e7ce7b5e97d
- All ten dependency hashes listed in derivation.json (topics 213, 214, 217, 222, 226,
  PROOF.md and AUDIT_CLARIFICATIONS.md each) were recomputed and match.
- Also read: 243 PROOF.md b718ea65ec31af8b67c779fab843e9fee74bd86d02cb1514f7ccbb6a92b5d8c5,
  01_operator_conventions and 201 (sign conventions), 204 (definition of J).

VERDICT: PASS WITH REMARKS

The claim holds as stated, with the binding sign sidecar. For B = E2 and every
Y_gamma, gamma > 4k: b_B R^(k-1) log R <= ||beta_R Cren||_(B0->B) <= ||beta_R Cren||_(B->B)
<= C_B R^(k-1) log R. Since C0 = Cren on ker c, beta_R C0 restricted to B0 has the same rate.
I found no binding defect. All remarks below are cosmetic or about citations.

Scratch check (single-threaded, nice 19, under 1 s): agent_244/check.py. It symbolically
confirms (8), the strain kernel and the sidecar identity, and checks (11) by quadrature.

## Findings

1. [Sidecar, binding part of the statement; verified consistent] Statement, line 17.
   PROOF.md writes c[h] = partial_x U1[h](0). From U = (-v_xy, v_xx), v = (-Delta)^(-1)h
   (the proof 01 convention U = (-psi_y, psi_x), psi = v_x), I derive
   -partial_x U1(0) = partial_y U2(0) = v_xxy(0) = psi_xy(0) = integral Kc h with
   Kc = y(3x^2-y^2)/(pi r^6) = sin(3theta)/(pi r^3). That matches proof 213 and proof 01
   (DU(0) = diag(-c,c)), and also the kernel in PROOF line 137. So the sidecar's corrected
   sign is correct. The magnitude bound (13), the condition c = 0 and the c[phi] = 1
   normalization (divide by the nonzero integral) do not depend on the sign. No step uses
   the wrong sign.

2. [Check (1): input norms; correct] Section "Uniformly bounded packets", lines 99-121.
   The packet stays away from the axis; it does not rely on quadratic vanishing at x = 0.
   - Supports: 1 <= |X - X_R| <= S = R^delta around X_R = 3R(cos th*, sin th*), with
     0 < th* < pi/2, plus three reflections. The distance to both axes is about R, since S = o(R).
   - Size: sup <= 1. The gradient is bounded uniformly, since the angular factor costs 2/s
     with s >= 1 and the outer cutoff costs 1/S. So the global C^alpha bound is uniform.
   - Vertical seminorm: on a vertical line meeting the support |x| >= cR, so
     [q_R]_(y,2) <= C R^(-2). Lines missing the support contribute 0.
   - Parity and q(0,y) = 0 are checked directly from the four-term extension.
   - Weighted L2: ||q_R||^2 <= C S^2 R^(-gamma) = C R^(2 delta - gamma). This is bounded
     because 2 delta < gamma when delta = min(1/2, gamma/4).

3. [Check (2): log R at a point where beta_R = 1; correct] Lines 90-95 and 123-133.
   - Kernels (8) and the local term -h/2 are confirmed symbolically.
   - At the center the input vanishes (s >= 1), so the integral converges absolutely and
     there is no local term.
   - n.U[a_R](X_R) = (1/2pi) int f(phi)^2 dphi int chi/s ds = (1/2) int chi/s ds >= (1/2)log S - log 2.
     Quadrature with S = 50 gives 1.609438 on both sides.
   - Evenness of the kernels under Z -> -Z is correct.
   - The three reflected packets contribute O(S^2/R^2) = O(1/R).
   - |X_R| = 3R > 2R gives beta_R(X_R) = 1. H0 = chi0 X.grad rho0/3 (proof 214) has compact
     support, and c = 0 anyway.
   - |grad rho0(X_R)| >= b R^(k-1) follows from (6). Theta is a nonzero trigonometric
     polynomial (a_521 nonzero, as in proof 222 lines 148-151), so it has finitely many zeros
     and some th* in (0, pi/2) has Theta(th*) nonzero, hence k Theta e_r nonzero.
   - Nothing cancels: the output at X_R is exactly |grad rho0(X_R)| n_R.U[h_R](X_R), and the
     sup norm is part of both output norms.

4. [Check (3): strain correction; correct] Lines 137-147.
   - |c[q_R]| <= C S^2 R^(-3) follows from homogeneity -3.
   - phi is a fixed bump at angle pi/6 with four reflections; Kc phi >= 0 on all four disks
     (same construction as topics 222 and 243). It gives c[h_R] = 0 exactly.
   - J(h_R) = 0, where J(h) = partial_x^2 partial_y h(0)/2 (proof 204/214), because h_R
     vanishes near the origin.
   - The norm change is O(S^2 R^(-3)).
   - The change in velocity at X_R is O(S^2 R^(-6)). Even the crude kernel bound O(R^-2)
     for U[phi] would be enough.

5. [Check (4): maximal domain; correct] Line 149.
   h_R is smooth with compact support away from x = 0. V = ell0 X + U[rho0] is C1, by
   proof 214 line 147 (rho0 is C^(4,1) and the joins are at least C5). So T h_R is C1 with the
   same axis-separated compact support, and lies in E2 and Y_gamma. Proof 226 then gives the
   full domains. The proof correctly says the graph norms are not uniform (|V| ~ R at X_R),
   and the operator-norm claim does not need them.

6. [Check (5): upper bound; correct, and it really does beat proof 226] Lines 34-71.
   - E2 part: this is proof 226 (5), from the body of proof 214 lines 135; it does not depend
     on gamma.
   - 4k < gamma < 2: the dyadic proof of (2) is correct. On blocks with |i-j| > 2 the
     distance is at least (3/4)2^max and the Hilbert-Schmidt bound is C 2^(-|i-j|). The
     weighted coefficients a_d = 2^(-|d| - gamma d/2) are summable exactly when
     -2 < gamma < 2, and Young's inequality on l2 then applies. The identification with the
     canonical velocity is correct (the r^-4/w_gamma integral is finite for gamma < 2; proof 226
     clarification 1).
   - The gain over proof 226 is real. The bound sup_(r>=R)|grad rho0| * ||U h||_(L2(w)) <=
     C R^(k-1) ||h||_(L2(w_gamma)) uses the weighted input norm, which is part of the
     Y_gamma norm. Proof 226's (3) used only the E2 norm through the pointwise log growth, which
     is why it got the larger R^(k-gamma/2) log R.
   - The sharp lower bound does not contradict this. The packet's velocity behaves like
     log(S/t) on its disk, so its weighted L2 norm is about S R^(-gamma/2), which is
     comparable to ||h_R||_(L2(w)).
   - gamma >= 2: the polar integral of r^(2k-1-gamma) log^2 r gives R^(k-gamma/2) log R,
     which is at most R^(k-1) log R. beta_R H0 = 0 for large R.
   - So the output tail is at most C R^(k-1) log R ||h||_B for every gamma > 4k.

7. [Cosmetic, citation] Lines 34-49 and 71. The weighted bound for gamma < 2 and the
   resulting R^(k-1) weighted tail are already proved in proof 214 (lines 93-107 and
   137-141, eq. (1) there). Proof 244 rederives them instead of citing them. "Upgrading
   proof 226" really means going back to proof 214's sharper bound, which proof 226's simpler
   E2-only envelope did not use. Recommend citing proof 214 (1) explicitly.

8. [Cosmetic] Lines 75-86. The derivative remainder O(r^(2k-2)) in (6) is not given a
   source. It follows from the exact finite outer modal sum (proof 214 (10), proof 222 line
   160) and should be cited. Line 84's "Since k>0 ..." would read better with the
   finite-zeros argument from finding 3 spelled out.

9. [Cosmetic, notation] Line 141 uses phi for the fixed c = 1 function, but phi is also the
   polar angle in (9) and (11). Line 145 says "order-zero velocity kernel", meaning an
   order-zero operator whose kernel has homogeneity -2. J is used without a definition or a
   citation (proof 204/214).

10. [Cosmetic, scope] Lines 30 and 160 and proof 243 agree with each other. Proof 243 gives the
    slower R^(max(2k-1, 2k-gamma/2)) log R rate for the full C0 on unrestricted inputs. Proof 244
    claims the R^(k-1) log R rate only on ker c, and never uses proof 243. There are no
    inverse, Fredholm or existence claims.
