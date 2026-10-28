## 2026-10-28 12:20Z (theory author, a session, team message 39: V179 to V182 integrated; one small verification request; numerics as in team message 38)

Verifier: V179 to V182 are integrated in the final report (brief items 1 and 3, 6.2 item 6, 6.3, 6.4 table), S2_CLOSURE,
S2_NUMERICAL_CERTIFICATES, S2_L2_THEORY, S2_RESTART and S2_BASIS_CERTIFICATION. V182 is quoted only as a deliberately
loose upper bound in the explicitly fixed equivalent norm, with your statement that it does not test (S).
One small request, if a slot is free (low cost; it would let the report call it a THEOREM instead of DERIVED):
 Claim NT (necessary test of (S)). In the setting of proof 174, assume (I) and (S) and let h_j be the iterates (7).
 Then for every j >= 1, F_ell(h_j)(rho_ell(h_j) + h_j) = (A_(h_j) - A_(h_(j-1))) h_j in Y, and
     ||F_ell(h_j)(rho_ell(h_j) + h_j)||_Y <= q_0^j ||f_0||_Y,  q_0 = K_L C K_H eta_H.
 Proof sketch: (14) gives F(h_j) = f_0 + A_(h_j) h_j and (7) gives A_(h_(j-1)) h_j = -f_0. Then (6), ||h_j||_H <=
 K_H eta_H, the contraction ||h_j - h_(j-1)||_X <= q_0^(j-1) ||h_1||_X and ||h_1||_X <= K_L ||A_0 h_1||_Y = K_L ||f_0||_Y.
 Consequence: every admissible (r_*, K_H, K_L, C) satisfying (S) has q_0 >= ||F(h_1)||_Y / ||f_0||_Y, so if the
 first step does not reduce the low residual norm, (S) fails for every admissible choice of constants.
 Text: S2_THEORY_18H_REPORT.md section 6.5 item 8 (theory author, DERIVED).
Numerics: team message 38 stands (repaired assembler or parts-only for S1M3, which is at about 380/392 cells per worker;
s1_robust; FAM_36_03_E/F; then S1J1). Please post the S1M3 values with their resolution flags as soon as they exist.
