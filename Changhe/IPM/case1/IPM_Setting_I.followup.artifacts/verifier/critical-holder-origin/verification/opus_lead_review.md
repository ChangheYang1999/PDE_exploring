# Lead review: critical ordinary Hoelder regularity (verifier PROOF.md, sha256 b4ee1b06...)

Reviewed by hand, 2026-10-20 (from 21:22Z). Verdict: CONFIRMED (no gap).

1. Lemma. 0 < x < y, h = y - x. If h >= x/2: |F(y) - F(x)| <= e (x^beta + y^beta) <= e (2^beta + 3^beta) h^beta. If
   h < x/2: |F(y) - F(x)| <= e h x^(beta - 1) = e h^beta (h/x)^(1 - beta) <= e h^beta. x = 0 by the amplitude bound.
   For u with |u^(j)| <= e x^(k + beta - j), j <= k + 1: sup norms of u^(j), j <= k, are <= e max(1, L)^(k + 1);
   F = u^(k) satisfies the hypotheses. Uniform in the size of the zero neighbourhood.
2. p_(N,a): d/dx = -x^(-1) d/dt, so p^(j) = (a/N) x^(7 + beta - j) P_j(psi_N, psi_N', ..., psi_N^(j)) with fixed
   polynomial coefficients; cutoff derivatives bounded uniformly in N. With k = 7: ||p||_(C^(7,beta)) <= C_M/N; t_N f
   has C^(7,beta) norm O(1/N).
3. Density on (0, r_0]: sigma = p/w_0 with w_0 = x s(x), s smooth nonzero, so |sigma^(j)| <= C N^(-1) x^(6 + beta - j).
   Faa di Bruno: q factors give N^(-q) x^(q(6 + beta) - j) <= N^(-1) x^(6 + beta - j) as x < 1. Reciprocal difference
   -p/(w_0^2 (1 + sigma)) has derivatives <= C N^(-1) x^(5 + beta - j); its primitive from 0 is <= C N^(-1) x^(6 + beta).
   So (3) for eta and for e^eta - 1. g_0 = x^2 phi, phi analytic positive: Leibniz terms g_0^(i) (e^eta - 1)^(j - i) are
   <= C x^(2 - i) x^(6 + beta - j + i) for i <= 2 and <= C x^(6 + beta - j + i) <= C x^(8 + beta - j) for i >= 3. (4).
4. On [r_0, L]: (lambda - 1) g_0 on [r_0, b_0], fixed-interval correction on [b_0, c_0], zero after c_0; C^9 differences
   O(1/N); x >= r_0 fixed, so (4) holds on (0, L] with a larger constant; k = 8 gives (5).
5. IVT exactly as in the fibers proof, with N chosen once for (1), (2), (5) on |a| <= M; continuity at fixed N as
   before. Consequence: B takes every real value on compatible traces in every C^(7,beta) x C^(8,beta) neighbourhood
   of (w_0, g_0), with germs at 0 and on [delta, L] fixed. Sharpens the C^m (m < 7 + beta) discontinuity of the
   origin bump family in the report (C^(7,beta) norm >= C^7 norm).
