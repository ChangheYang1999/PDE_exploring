# Lead review of research/angular_residual_norms/PROOF.md (verifier side, file of 02:48Z)

Reviewed 2026-10-29T03:1xZ. Verdict: CORRECT. No gap found. Two optional wording additions.

Checked step by step:
1. curl(f(q) H y) = f (grad H x y): the 2 f' y H part of grad(fH) is killed by x y. Degree l at fixed r.
2. curl curl(g(q) H y) = ((l+1) g + 2 q g') grad H - 2 l g' y H. Recomputed from grad div - Laplacian:
   div(gHy) = ((3+l) g + 2 q g') H; Laplacian(gH) = H (4 q g'' + (6+4l) g'); grad H coefficient
   (3+l) g + 2 q g' - 2 g; y H coefficient 2(5+l) g' + 4 q g'' - 4 q g'' - (6+4l) g' - 4 g' = -2 l g'. Matches.
3. One Cartesian derivative raises the degree by at most one (2 f' y_j P or f d_j P): d = max(L_T+1, L_S+2).
4. Vorticity: curl P_g = -curl(Laplacian(gH) y) gives the toroidal coefficient b = -4 q g'' - (4l+6) g' (matches
   the stated identity); curl T_f = P_f. Hence v = max(L_S, L_T+1), e = max(L_S+1, L_T+2). Regularity f in C^2, g in
   C^3 is exactly what A, Omega and DOmega need.
5. Pressure: a(r) r^-l H(y) = b(q) H(y) with b in C^1; grad P = b grad H + 2 b' y H, degree <= L_P + 1.
6. L, N, L_Omega, N_Omega degree rules and the values m = max(u, d+1, d+u, L_P+1), h = max(v, e+1, e+u, d+v).
7. Quadrature: equally spaced N_phi points annihilate every frequency 0 < |k| < N_phi, independent of the offset.
   Monomials with a + b odd have only odd azimuthal frequencies, and with a, b both odd the zero frequency
   vanishes by symmetry, so the discrete azimuthal sum equals 2 pi times the exact mean at every node mu_i (the
   half-integer powers of 1 - mu^2 never reach the Gauss-Legendre sum). The remaining (1 - mu^2)^j mu^k has degree
   <= D and is integrated exactly when 2 N_mu - 1 >= D.
8. Substitution L_T = 15, L_S = 14, L_P = 36: u 15, d 16, v 16, e 17, m 37, h 32; 2m = 74 <= 83 and < 84 (42 x 84);
   48 x 96 also; vorticity 64.

Optional additions:
(a) State why the twisted channels are of the assumed form: a rotation about the z axis by psi(r) maps H_lm to a
    combination of H_l,m and H_l,-m with coefficients cos(m psi(r)) and sin(m psi(r)), so the twist only changes the
    radial coefficients; the smooth twist keeps f in C^2 and g in C^3 on (0, infinity). The scope paragraph says this
    in one line ("a radial twist that changes only radial coefficients"); one sentence with the rotation formula
    would make the dependence explicit.
(b) Since u >= 1, m = max(d+u, L_P+1) and h = max(e+u, d+v) for the campaign values; with L_P = 36 the momentum bound
    is set by the pressure truncation (L_P + 1 = 37), not by A U (32). A synthesis truncated at L_P = 32 would give
    m = 33. Harmless; it explains where 74 comes from.
