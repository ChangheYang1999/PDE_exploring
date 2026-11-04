# T2_REV_v01: independent reviews of AT-060 to AT-064, and closure function v2

Version 1. Owner: the second theory agent (theory agent; Opus reviewer for the theory auditor, as requested in the theory auditor's team notes 20:24Z).
Written 2026-11-02T20:37Z. Plain-text mathematics as in T2_WGK_v01.

Reviewed files (read-only; SHA256 at the time of review):
- AT-064: theory_audit/research/angular_sobolev_constants/PROOF.md, f808070a0c357b7a32ccd72f90ced939132e8214d0e0edf1d2aaa9ea7c826571
- AT-063: theory_audit/research/principal_constant_lower/PROOF.md, 661bc0aa9c7b24cc5486d8486361c727592a1a326a35b458804e28aa9e28a5ed
- AT-061: theory_audit/research/sobolev_necessary_test_audit/PROOF.md, dfa82a9e04ba5dd8ef08927bb767e77303d93c8d161e6a80e16f39f097547884
- AT-060: theory_audit/research/recentering_audit/PROOF.md, aacb0a79e85191720d02481d42efdeb8c4d3b778157ad17f87455c30727c48c5
- AT-062: theory_audit/research/pareto_objective_audit/PROOF.md, cce25b4b2dd8791d021baac768c2faf6b95ffbecd2e158bf4f609756585e4f4c

Evidence scripts (FLOAT): theory_agent_2/scratch/at064/check_at064.py, closure_fn_v2.py, g0max.py, with .out files.

## Summary

| item | verdict of this review | remarks |
|---|---|---|
| AT-064 sharp interpolation constants | AGREE, all six bounds | B_1/4 equals C*_sym of T2_WGK_v01 Lemma SYM exactly; Sym DU uses B_1/4 |
| AT-063 lower bound c_1 >= q | AGREE | the normalized class (ell = 0) follows by a translated construction (section 2) |
| AT-061 additions (2), (3), pointwise test | AGREE | (3) may use Sym Da; the WG-K route has its own test (T2_WGK_v01 section 5) |
| AT-060 center class, product statement | AGREE | the correction of the word "needs" is accepted |
| AT-062 three-term weights | AGREE | Q = (G/beta0)^p N is also the leading proxy of the WG-K closure |

## 1. AT-064

Checked step by step.
- (3): Fourier inversion with fhat = int exp(-iX.xi) f, Cauchy-Schwarz with the weight a + beta |xi|^(2q), and
  ||fhat||_2 = 2 pi ||f||_2. This gives the factor (2 pi)^(-1) and the factor [a L^2 + beta H^2]^(1/2).
- (4): the substitution v = beta r^(2q)/a gives (1/(2q)) a^(s-1) beta^(-s) int v^(s-1)/(1+v) dv, with s = (p+1)/q. The
  identity int v^(s-1)/(1+v) dv = pi/sin(pi s) needs 0 < s < 1. Here s = 1/q for p = 0 and s = 2/q for p = 1, both in
  (0, 1) for 2 < q < 3.
- The choice a = t/L^2, beta = s/H^2 is the minimizer over the ratio beta/a: the bound is homogeneous of degree 0 in
  (a, beta), and d/dx [x^(-s)(L^2 + x H^2)] = 0 at x = s L^2/(t H^2). The constant
  sqrt(I/(2 pi)) B_p = (I/(8 pi q sin(pi s)))^(1/2) t^(-t/2) s^(-s/2) agrees with (3) and (4).
- Since Cauchy-Schwarz is attained at |fhat| proportional to r^p |b|/(a + beta r^(2q)), these are the sharp constants of
  the Fourier-L^1 route. They coincide with the KKT constants of T2_WGK_v01 Lemma SYM. Numerically
  (check_at064.out), B_1/4 and C*_sym agree to 2e-16 relative at q = 2.1, 2.25, 2.4, 2.5, 2.6 and 2.8. The two
  derivations are independent: Beta-function moments in T2_WGK_v01, a sine formula in AT-064.
- Angular integrals. Each was checked by hand and by quadrature: pi for v.grad; 2 pi for the value;
  int m m^T = diag(pi/4, 3 pi/4) for U; M(z) = (pi/8)(1 + 4t) for the operator norm of DU, with the Cauchy-Schwarz step
  I(z, w) <= (M(z) M(w))^(1/2) and v.m = c_phi (z.omega) for z = (-v_2, v_1). The Gram matrix (pi/8)[[2,0,0],[0,1,-1],[0,-1,5]]
  has eigenvalues 2 and 3 -+ sqrt(5). The ell symbol is -i r c_phi^2 s_phi, with I = pi/8. The moments are those
  listed. A random search over 400 pairs (v, w) gives at most 0.6187 pi, below the claimed maximum 5 pi/8 = 0.625 pi.
- Comparison with AT-033: C(q, p, 2 pi)^2 = (4 pi q)^(-1) s^(-(1+s)) t^(-(1+t)) and B_p^2/C^2 = pi s t/sin(pi s) agree
  with the second theory agent's C_split to all printed digits. The proof of sin(pi s) > pi s (1 - s) is correct: g' > 0 on (0, 1/2)
  because the cosine is concave and lies above its chord, and g is symmetric about 1/2.
- Transfer to the weighted ball: ||f||_(Hdot^q) <= ||<D>^q f|| <= c_W N(f). Correct.

Remarks.
- (a) Sym DU. For the absorption in the WG-K route (T2_WGK_v01 Proposition TAU) only Sym DU[k] enters. For a unit e
  the symbol of e^T DU e has angular factor c_phi sin(2 phi - 2 alpha)/2, with squared integral pi/8 for every alpha.
  So ||Sym DU[f]||_(inf,op) <= (B_1/4) ||f||^theta ||f||_(Hdot^q)^(1-theta), smaller by sqrt(5) than C_DU = sqrt(5) B_1/4.
  The latter is still needed where the full DU enters: the non-tame KP-W coefficient, and the bound |U(X)| <= eps(k) r
  in TAU.
- (b) The tame quantity A(z) = ||grad z||_inf + ||z||_inf of KP-W uses C_grad = B_1/sqrt(2) and C_value = B_0. That is the
  binding term of the closure (T2_WGK_v01 section 6), so the gain from AT-064 enters the closure directly (section 6
  below).

## 2. AT-063

Checked step by step.
- The construction: P = -x^2 y/2 is S1; U[-Delta psi] = (-d_xy psi, d_xx psi) from the symbol; a = (x, -y) and
  Da = diag(1, -1) where chi_R = 1.
- The bounds (3) and (4).
- The scaling (5): a_e = e a_R(X/e), Da_e = Da_R(X/e), ||k_e||_2 = e^2 ||k_R||_2.
- The pure-strain region contains |X| < e/2 for R >= 2.
- The Fourier identity (6): F[(AX).grad u] = -(A^T xi).grad_xi uhat when tr A = 0. Integrating by parts gives the real
  part (1/2) int grad_xi <xi>^(2q) . A^T xi |uhat|^2 = q int (xi^T A xi) <xi>^(2q-2) |uhat|^2.
- The packet limits (7): at xi near (+-n, 0), xi^T A xi <xi>^(2q-2) / <xi>^(2q) -> 1.
- The p bound (8): |p| <= sigma |X|^2/r0^2 <= sigma e^2/(4 r0^2).
- The tame term divided by ||u_n||_(H^q)^2 is O(n^(1-q)).
- The order of the limits: n first, then e, then R.
The theorem is correct as stated.

Addition: the normalized class. AT-063 does not claim the bound for k restricted to ell(k) = 0. It holds there too.
Take X_0 = (d, d) with d > 2 R^2. Let psi be the sum of the four S1 reflections of (P chi_R)((X - X_0)/e) e^3, with the
signs that make psi S1. Because U[-Delta psi] = (-d_xy psi, d_xx psi) is local in psi, near X_0 we have
a(X) = A(X - X_0), and psi vanishes near the origin. Hence ell(k) = d_y d_xx psi(0) = 0. Test with
u_n = phi(X - X_0) cos(n x), plus its three S1 images. At each image the strain is again A = diag(1, -1); this was
checked for both reflections. The cross terms between images have disjoint supports at positive distance, so they are
O(n), while ||u_n||_(H^q)^2 is of order n^(2q). The Fourier computation (6) is
translation invariant. On the support, |p| <= |A(X - X_0)| |grad log W| <= sigma e/(4 r0) -> 0. So c_1 >= q also when (1)
is assumed only for normalized S1 k. The same construction is the KP-W-level analogue of T2_WGK_v01 Proposition OBS,
which places a sharp strain profile at lambda Y_A.

Consequence for the routes.
- In the scalar kappa route (AT-058, AT-059, AT-061), c_1 >= q justifies q in the necessary screens, as AT-063 says.
- In the WG-K route (T2_WGK_v01), c_1 does not enter the absorption at all. The principal term is the exact
  q Sym DU[k], and its size is q (B_1/4) R^theta (c_W M)^(1-theta). Proposition OBS shows this is attained up to
  c_W^(1-theta). The WG-K necessary test N(h_0) R^((q-2)/2) < [beta/(q B_1/4)]^(q/2) is weaker than the scalar test with
  c_1 = q by the factor (C_U/(B_1/4))^(q/2): 4.0 at q = 5/2 with C_U = C_GN^U, and 5^(q/4) = 2.7 with the AT-064 value
  C_DU = sqrt(5) B_1/4. Both are necessary only for their own sufficient criterion.

## 3. AT-061 additions

- (2): from M >= a >= N(F)/beta and c_1 C_U R^theta (c_W M)^(2/q) < beta, raising to the power q/2 gives
  N(F) R^p < beta [beta/(c_1 C_U)]^(q/2), with p = theta q/2 = (q-2)/2. Correct.
- (3): ||Da(X)||_op <= H r^alpha with H = [Da]_(C^alpha, op) and Da(0) = 0. Integrating along the segment gives
  |a(X)| <= H r^(1+alpha)/(1+alpha) and the bound on |a.grad log W|. Correct.
  - Remark: q Sym Da enters the frozen matrix, so H may be the Hoelder seminorm of Sym Da.
  - Remark: H <= C ||k||_(Hdot^q) holds with an explicit C. For alpha = q - 2, the integral
    int |xi|^(2-2q) min(1, r^2 |xi|^2) d xi converges at both ends exactly when 2 < q < 3 (the external referee t2-wgk1 (20), checked
    in T2_WGK_v01 section 3).
- The pointwise implication lambda_max(P + Q) <= lambda_max P + lambda_max Q is correct.
- The K(grad k) caveat is correct. It concerns the derivative of the nonlinear map, not A_k. So it is irrelevant for
  the invariance (S-inv-K) and relevant for any contraction or derivative statement.

## 4. AT-060 additions

- Identity (1): L_* d = L d + U[h_*].grad d + U[d].grad h_*. Expanding gives F_* + L_* d + U[d].grad d. Correct.
- The inverse (2):
  - L_* + U[e].grad = A_(h_*+e) + K_*, and ||K_* d||_2 <= g_* ||d||_2 because |m| <= 1.
  - The imported coercivity constant beta_0 is uniform over the coefficient class, since U[k].grad is skew.
  - Then A + K_* = (I + K_* A^(-1)) A with ||K_* A^(-1)|| <= g_*/beta_0 < 1. The inverse has norm at most
    (1/beta_0)/(1 - g_*/beta_0) = 1/(beta_0 - g_*). Correct, and this repairs the a priori statement of v02 section 9
    into an actual inverse.
- The L^2 center qualification is correct and necessary as a hypothesis. A difference of two candidate profiles with
  different far fields need not be in L^2.
- (3) and F_* = U[h_0].grad h_0 at h_* = h_0: correct.
- The product statement:
  - W U[h_0].grad h_0 = a.(grad g - (grad log W) g), with g = W h_0 in H^q.
  - a = U[W^(-1) g] is in H^q (c_W and the boundedness of U on H^q), and H^(q-1) is an algebra for q - 1 > 1.
  - So W F_* is in H^(q-1). Correct.
  - The correction of the wording in v02 section 9 is accepted: one extra derivative of h_0 is a sufficient input for
    N(F_*) < infinity, not a proved necessity.
  - Note: for a computed smooth center h_* (h_N), the question does not arise, because N(F_*) is then computed.

## 5. AT-062

- With beta_0 and w fixed, dH = 2G dG + 2 w N dN and d log Q = p dG/G + dN/N. Taking the factor 2G^2/p gives
  w = G^2/(p N^2).
- With N = N_2^(3-q) N_3^(q-2), dN/N = (3-q) dN_2/N_2 + (q-2) dN_3/N_3. This gives w_2 = (3-q) G^2/(p N_2^2) and
  w_3 = (q-2) G^2/(p N_3^2) = 2 G^2/N_3^2. Correct.
- Remark: Q = (G/beta_0)^p N is also the leading proxy of the WG-K closure (T2_WGK_v01 section 7), not only of the
  scalar criterion.
  - With M about N/b, both the absorption term and the tame term are of order R^theta M^(1-theta). The condition
    R^theta (N/b)^(1-theta) <~ const is R^p N <~ const, since theta/(1-theta) = p.
  - The second tame term R^theta_0 M^(1-theta_0) gives R^(q-1) N <~ const, which is weaker for small R.
  - So the coordinator's objective targets the right combination for this route as well.
  - The re-centered route uses (||F_*||_2/beta_0_*)^p N(F_*).

## 6. Closure function v2 (FLOAT; the constants C_eps_bar, c_4', c_W and eps remain HEURISTIC)

theory_agent_2/scratch/at064/closure_fn_v2.py is closure_fn.py of T2_WGK_v01 with a switch which = "v1" or "v2".
- "v1" reproduces T2_WGK_v01 section 7 exactly.
- "v2" uses AT-064:
  - tame: C_grad = B_1/sqrt(2), C_value = B_0;
  - gap: Sym DU uses B_1/4; the bound |U| <= eps(k) r uses sqrt(5) B_1/4; U.e uses sqrt(3/8) B_0.

Constants at q = 5/2:

| constant | v1 | v2 |
|---|---|---|
| C_grad | 0.5728 | 0.3746 |
| C_value | 0.5099 | 0.4540 |
| C_DU | 0.4051 | 0.2961 |
| C_U | 0.3605 | 0.2780 |
| C_sym | 0.1324 | 0.1324 |

Largest N(F) that closes, v2, with C_eps_bar = 0, c_4' = 1, c_W = 1 and eps = 0:

| tuple | G0 = 0.377 | 0.0521 | 0.0376 | 0.01 | 1e-3 | 1e-4 | 1e-6 |
|---|---|---|---|---|---|---|---|
| P-Q2 | 0.0069 | 0.0158 | 0.0185 | 0.0308 | 0.0587 | 0.0988 | 0.254 |
| P-BG2 | 0.0068 | 0.0214 | 0.0251 | 0.0433 | 0.0904 | 0.169 | 0.547 |
| P-Q1 | 0.0044 | 0.0121 | 0.0151 | 0.0317 | 0.0823 | 0.179 | 0.737 |
| P-BG1 | 0.0006 | 0.0020 | 0.0023 | 0.0049 | 0.0141 | 0.0318 | 0.133 |

The gain over v1 is a factor of 1.34 to 1.41. The qualitative reading of T2_WGK_v01 section 7 is unchanged.

Sharper threshold (g0max.out). Since N(F) >= G0, closure needs max N(F) >= G0. The largest G0 for which this holds:

| constants | P-Q2 | P-BG2 | P-Q1 | P-BG1 |
|---|---|---|---|---|
| v1, C_eps_bar = 0, c_4' = 1 | 0.0181 | 0.0226 | 0.0168 | 0.0049 |
| v2, C_eps_bar = 0, c_4' = 1 | 0.0228 | 0.0285 | 0.0213 | 0.0063 |
| v2, C_eps_bar = 1, c_4' = 10 | 0.0035 | 0.0042 | 0.0036 | 0.0011 |

So the un-centered WG-K ball cannot close for ||F||_2 above about 0.03, even with the optimistic constants. T2_WGK_v01
said "about 0.05"; that statement is true but not sharp. For the re-centered residual the same numbers apply to
||F_*||_2, with beta_* and beta0_* in place of beta and beta0.

## 7. Requests

- The theory auditor: record these reviews as the independent Opus review of AT-060 to AT-064. Check the normalized-class addition
  to AT-063 (section 2).
- The first theory agent: in theory_v01, use B_1/4 for Sym DU in the WG-K absorption, B_1/sqrt(2) and B_0 in the tame term, and
  sqrt(5) B_1/4 wherever the full DU enters.
- numerics: closure_fn_v2.py (which = "v2") replaces closure_fn.py for screening. Targets for a re-centered residual
  (HEURISTIC constants; P-BG1 needs about 6 times less):
  - c_4' = 1, C_eps_bar = 0: ||F_*||_2 = 0.01 with N(F_*) <= 0.03 to 0.04, or ||F_*||_2 = 1e-3 with N(F_*) <= 0.06 to 0.09;
  - c_4' = 10, C_eps_bar = 1: ||F_*||_2 = 1e-3 with N(F_*) <= 0.006 to 0.009.
