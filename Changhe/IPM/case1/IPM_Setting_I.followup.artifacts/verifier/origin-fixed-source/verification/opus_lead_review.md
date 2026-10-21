# Lead review: origin discontinuity with the source germ fixed (verifier PROOF.md, sha256 407cb7cf...)

Reviewed by hand, 2026-10-20. Verdict: CONFIRMED (no gap).

1. Formula (4). (log g)' = w'/w - A/w; with u = 0 near 0 and both g normalized by g/x^2 -> 1, the constant is 0. Valid
   up to L because u = 0 near L. Checked.
2. Origin layer p_N = (a/N) x^(7+beta) chi(t) chi(N+2-t): (5) from d/dx = -x^(-1) d/dt with bounded cutoff derivatives;
   (6) as in the critical-norm proof with eps = a/N. Leading term: g_0^3 = x^6(1+O(x^2)), W_0 = A^(beta-2) x^(-beta)
   (1+O(x^2)), so (Q_hat - Q_0) W_0 = -(A^(beta-2)/2) p'' x^(-6-beta) + O(eps x). Error ledger (7): lower part of
   delta Q (delta g' = O(eps x^(7+beta)), / x^6, times x^(-beta): O(eps x)); relative change of g^(-3) times the O(x)
   numerator: same; (Q_0 - Q_0(L)) delta W = O(x^(-5)) O(eps x^6) = O(eps x); delta Q(L) W = O(eps x^(-beta));
   products smaller. Integrable, O(eps). On [r_0, L] the exact formulas Q_hat = lambda^(-2) G + lambda^(-3) V,
   W_hat = lambda^(1-beta) W_0 give O(eps (L-x)^(beta-1)). Below supp p_N only Q(L) changes (integrable x^(-beta)).
   Prefactor: (beta-1)A^(1-beta)/3 * (-(A^(beta-2)/2)) = (1-beta)/(6A). Two integrations by parts (flat compact
   support): (6+beta)(7+beta) int p x^(-8-beta). Plateau: (a/N)(N + 2 int_0^1 chi) = a + (2a/N) int_0^1 chi. Checked.
3. Interior correction. I_N = O(1/N) (integrand -p/(w_0(w_0+p)) = O(eps x^(5+beta))). J smooth near 0, J'(0) =
   -int f/w_0^2 < 0, so t_N = O(1/N) unique small. Disjoint supports give int [1/w_N - 1/w_0] = 0 over [0, L]; by (4)
   g_N = g_0 on [c, L] (u_N = 0 there and the accumulated integral is 0). Critical norm of t_N f is O(1/N) (support at
   positive distance from 0); with r = r_0 the C^(2,theta)[r_0, x*] tail norm of t_N f is also O(1/N), and the Taylor
   coefficients at 0 are unchanged, so convergence holds in the full norm of 6.3.1 (i) with sigma = beta. Checked.
4. Comparison (12). On [0, b): (w_N, g_N) = (w_hat_N, g_hat_N) by causality of (4); only Q(L) differs, by O(1/N), with
   weight bounded by C x^(-beta) near 0 and bounded on [r_0, b]. On [b, c]: w_0, g_0 bounded away from 0; changes of w,
   w', w'' are O(1/N) (t_N f), of g, g' O(1/N) (from (4) and the first equation), hence of Q, W O(1/N). On [c, L]:
   (w_0, g_0) against (w_0, lambda_N g_0): O(N^(-1)(L-x)^(beta-1)). Both traces agree near 0, so the finite parts
   differ by the ordinary integral. |B[w_N] - B[w_hat_N]| <= C_a/N. Checked.
5. Scope: no hypothesis on g_* (so it includes 2A - 2); consistent with the source-supported fixed-value estimate,
   since u_N has an origin component. The support of f can be any fixed compact subinterval of (r_0, L): the proof
   uses only disjointness from supp p_N and distance from L (the choice (2r_0, L - r_0) is not needed).

# Lead review: exact values in fixed finite-observation fibers (verifier PROOF.md, sha256 d8634e16...)

Reviewed by hand, 2026-10-20. Verdict: CONFIRMED (no gap).

1. Uniformity on |a| <= M: every estimate of the origin-fixed-source proof carries the factor |a|/N (p linear in a),
   denominators w_0 + p comparable to w_0 once C M/N is small; constants C_M and the threshold for N are uniform.
2. t_N(a) = J^(-1)(-I_N(a)) is smooth in a: I_N is smooth in a (differentiation under the integral, integrand
   O(x^(5+beta)) uniformly), J is a local diffeomorphism at 0 with a fixed inverse neighbourhood. Disjoint supports
   give (3); (4) gives (w, g) = base on [c_0, L] and below r_0 exp(-(N+2)). (5): f has fixed support at positive
   distance from 0.
3. (6): the origin-fixed-source estimates with C_M; the plateau gives a kappa_A (1 + (2/N) int chi), error O(M/N).
   The support (b_0, c_0) of f lies in (2 r_0, delta), possibly not in (2 r_0, L - r_0); as noted in the first review
   only disjointness from supp p and distance from L are used, so this is fine.
4. Continuity in a at fixed N: all traces equal the base below r_0 exp(-(N+2)) and on [c_0, L], with the same Q(L);
   B[w_(N,a)] - B[w_0] is an ordinary integral over a fixed compact subinterval of (0, L) of an integrand continuous
   in (x, a) (w < 0, g > 0 there, g and g' continuous in a). IVT with a_-, a_+ as stated, N fixed after b and eps.
5. Consequence: delta below the smallest positive point of a finite S; all jets of w and g at S are those of the base;
   B takes every real value on the set within any positive critical-norm radius. Also in the norm of 6.3.1 (i) with
   sigma = beta and r = r_0: Taylor coefficients unchanged, tail norm of t_N f O(1/N).
