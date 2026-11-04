# T2_NELO_v01: first form of NE-lo for T_II at P-S1 (near-field radius rho), its price, budgets at 007 + b14s size

Agent the second theory agent. theory_v06 T6.4 item 3, second bullet (first form of NE-lo with its near-field radius rho), and the coordinator
04:32Z item 5 (H4 for new centers only). Builds on notes/T2_H4_v01.md (setting of section 2, Lemmas HI, QW-Q, QW-S,
Theorem H4-R; AT-361 to AT-366 CONFIRM them conditionally) and notes/T2_H4A_v01.md (Corollary BUD-NEC, AT-369). All
times are real UTC times. Labels: CONFIRMED (cited audit), CLAIMED (proved here, audit requested), FLOAT, HEURISTIC,
OPEN. P-S1 = (21/10, 1, 1/2), W^2 = 1 + 4|X|^2, c = 4076476460239181/2251799813685248, cap = c + 1 - q.

## 0. Summary

- Lemma OSC (CLAIMED). For every real bounded coefficient a, the T_II-type form Q_a(g) = sum_j <a R_j g, R_j g>
  - <a g, g> satisfies |Q_a(g)| <= (sup a - inf a) ||g||^2. This prices the far part of T_II by sup norms only.
- Lemma M2-LB (CLAIMED). At P-S1, Delta atil(0) = 16 c for every background with ubar of class C^2 and div ubar = 0.
  Hence M2(a) >= 16 c for every coefficient a that equals atil near 0 (Fourier moment of AT-333). The explicit weight
  part atil_c of Remark WM (M2 = 16 c, AT-363) is the smallest possible value.
- Proposition TII-0 (CLAIMED). A complete NE bound for T_II with explicit radius rho, frequency cut mu, Riesz cut nu
  and split t. Its slack is osc of the far part + 2 phi M2(chi_rho atil) mu^(-2) + an L^1 term; its price is
  2 sup((chi_rho atil)_- W^2) kappa_q(mu)^2 + a Riesz term that vanishes when atil <= 0 on |X| <= 2 rho. At P-S1,
  atil W^2 = 4 ubar.X - c exactly, so the rho dependence of the price is through ubar.X on |X| <= 2 rho only.
- Corollary PR-0 (CLAIMED given the FLOAT monotonicity of kappa_q; values FLOAT). Used inside Theorem H4-R, Proposition
  TII-0 gives a bound on C^opt(b0) of at least 2 c kappa_q(mu_0)^2, mu_0 = (32 phi c/(cap - b0))^(1/2). At
  stipulated C5 + b14s-size inputs (certified ||F||_2 >= 1.4e-5, N(F) >= 0.091, beta0 <= c + 1) this exceeds the
  necessary budget U of Corollary BUD-NEC at every b0 <= cap (scan 0.60 to 0.70 with smallest ratio 1.71 at
  b0 = 0.64, and monotone bracketing between scan points, section 3), so this first form cannot certify the CE P-S1
  test there. At stipulated 007 + b14s-size inputs (||F||_2 2.8e-6,
  N 0.02 to 0.08) it uses 0.5 to 4 percent of U at b0 = 0.60 to 0.65 (FLOAT kappa).
- Budgets at 007 + b14s size (Arb; stipulated inputs; section 4). At ||F||_2 = 2.8e-6 and N = 0.02 to 0.08 the
  necessary budget U (beta0 <= c + 1) is 5.67e9 to 5.25e10 and the witness budget D (beta0 = 209/100) is 2.17e9 to
  2.5e10, against about 1e8 to 6e8 at the C5 + b14s size (Tables A4 and A5 of T2_H4A_v01). HEURISTIC: the
  single-piece model of T2_H4_v01 section 6 with C2 = 770 (price 4.64e9 at b0 0.60, 8.97e9 at 0.65) is below the
  witness D for N <= 0.06 at b0 = 0.60 and 0.65 at ||F||_2 = 2.8e-6; with C2 = 7700 it is not. Table N4 reproduces
  the first theory agent's notes 25 item 4(b) and 28 (AT-395) at their inputs.
- H4 at P-S1 remains OPEN. NE-lo for C_aw, C_tr, T_IS, NE-vs, N2 (moments and sup norms of the actual coefficients)
  and N3 (certified kappa) remain OPEN. Section 5 lists the N2 inputs that Proposition TII-0 needs.

## 1. Two lemmas

Setting and notation as in T2_H4_v01 section 2: tests g are real S1 Schwartz functions, u = J^(-q) g, h = W^(-1) u,
R_j = d_j |D|^(-1) with symbol i omega_j, atil = sigma (ubar.X - c r0^2)/(r0^2 + |X|^2), and
T_II = (1/2) sum_j <[[atil, R_j], R_j] g, g> (Proposition DR, AT-332, AT-361). For a real bounded measurable a put
    Q_a(g) := sum_j <a R_j g, R_j g> - <a g, g> = int a (|Rg|^2 - g^2),   Rg = (R_1 g, R_2 g).
Then T_II = Q_atil (the identity sum_j R_j* a R_j - a = (1/2) sum_j [[a, R_j], R_j] of the DR proof), Q is linear
in a, and Q_a has the kernel -(1/2) a^(zeta) |omega(xi) - omega(eta)|^2 of Lemma KER.

Lemma OSC (CLAIMED, elementary). For real bounded measurable a and real g in L^2,
    |Q_a(g)| <= (sup a - inf a) ||g||^2.
If a <= 0, then Q_a(g) <= sup(-a) ||g||^2.
Proof. ||Rg||^2 = ||g||^2 (Plancherel; sum_j omega_j^2 = 1 off 0), so Q_k(g) = 0 for a constant k and
Q_a = Q_(a - k). With k = (sup a + inf a)/2, |a - k| <= (sup a - inf a)/2, and
|Q_(a - k)(g)| <= ((sup a - inf a)/2)(||Rg||^2 + ||g||^2). If a <= 0, int a |Rg|^2 <= 0 and -int a g^2 <=
sup(-a) ||g||^2. QED.
This is the exact form of the far-part bound named in T2_H4_v01 section 5 (there with 2 sup|a_f|). The subtraction of
the constant is the one that removes sigma c from a_W.

Lemma M2-LB (CLAIMED, elementary). Let ubar be of class C^2 near 0 with div ubar = 0. Then
    Delta atil(0) = 4 sigma c/r0^2   (= 16 c at P-S1).
Let a be real, bounded and measurable, equal to atil on a neighborhood of 0, with a^ locally integrable, and
M2(a) = (2 pi)^(-2) int |zeta|^2 |a^(zeta)| d zeta (the normalization of AT-333 and Lemma HI'). Then
M2(a) >= 4 sigma c/r0^2.
Proof.
- atil = atil_c + atil_u (Remark WM). atil_c = -sigma c (1 + |X|^2/r0^2)^(-1) = -sigma c (1 - |X|^2/r0^2) + O(|X|^4),
  and Delta |X|^2 = 4 in R^2, so Delta atil_c(0) = 4 sigma c/r0^2.
- atil_u = sigma (ubar.X) e(X) with e = (r0^2 + |X|^2)^(-1) radial. ubar.X vanishes at 0 and grad e(0) = 0, so
  Delta atil_u(0) = sigma e(0) Delta(ubar.X)(0). Delta(ubar.X) = sum_i (X_i Delta ubar_i + 2 d_i ubar_i), which is
  2 div ubar(0) = 0 at X = 0.
- If M2(a) is infinite there is nothing to prove. Otherwise |zeta|^2 a^ is integrable, so Delta a is continuous with
  Delta a(X) = -(2 pi)^(-2) int |zeta|^2 a^(zeta) e^(i X.zeta) d zeta and |Delta a(0)| <= M2(a). Near 0, a = atil
  is C^2, and the classical Laplacian equals the distributional one. QED.
- Consequences. M2(chi_rho atil) >= 16 c and M2(atil) >= 16 c at P-S1 whenever these moments are used. AT-363 gives
  M2(atil_c) = 16 c exactly, so the explicit weight part already has the smallest value that any localization of
  atil can have.

## 2. Proposition TII-0 (first form of NE-lo for T_II)

Let chi_rho(X) = chi(X/rho) with chi smooth radial, 0 <= chi <= 1, chi = 1 on |X| <= 1 and chi = 0 on |X| >= 2.
Put a_n = chi_rho atil (near part), a_f = (1 - chi_rho) atil (far part) and, for mu > 0, g_lo = psi_mu(D) g with psi
as in T2_H4_v01 section 3. For 0 < nu and j = 1, 2 let
    kappa_j(nu, mu) = || w_sigma F^(-1)[omega_j (1 - psi_nu) psi_mu <.>^q] ||_(L^1)
(finite: the symbol is smooth with compact support; N3, not computed here).

Proposition TII-0 (CLAIMED, elementary). Assume M2(a_n) < infinity. For every rho > 0, mu > 0, nu > 0, t in (0, 1)
and every test g,
    T_II(g) <= e_II ||g||^2 + P_II ||h||^2,
    e_II = osc(a_f) + 2 phi M2(a_n) mu^(-2) + t^(-1) pi^(-1) ||(a_n)_+||_(L^1) nu^2,
    P_II = 2^sigma [ sup((a_n)_- W^2) kappa_q(mu)^2 + (1 - t)^(-1) sup((a_n)_+ W^2) sum_j kappa_j(nu, mu)^2 ],
with osc(a_f) = sup a_f - inf a_f <= sup_(|X| >= rho) (atil)_+ + sup_(|X| >= rho) (atil)_-, phi = (1 + sqrt5)/2,
kappa_q(mu) = kappa_(2.1)(mu) of Table H4-2 (FLOAT values), and x_+ = max(x, 0), x_- = max(-x, 0).
Proof.
- T_II = Q_(a_f) + Q_(a_n) by linearity. Lemma OSC bounds Q_(a_f)(g) by osc(a_f) ||g||^2. Since a_f = 0 on
  |X| < rho and 0 <= 1 - chi_rho <= 1, sup a_f <= sup_(|X| >= rho) (atil)_+ and -inf a_f <= sup_(|X| >= rho) (atil)_-.
- High part. |omega(xi) - omega(eta)| <= 2|zeta|/max(|xi|, |eta|), so the kernel of Q_(a_n) is bounded by
  2 |zeta|^2 |a_n^(zeta)| mu^(-2) where max(|xi|, |eta|) >= mu. Lemma HI (with l = 2|zeta|^2, A_l = 2 M2(a_n);
  AT-362) gives |Q_(a_n)(g) - Q_(a_n)(g_lo)| <= 2 phi M2(a_n) mu^(-2) ||g||^2.
- Low part. g_lo is real (psi radial). Q_(a_n)(g_lo) = int a_n (|R g_lo|^2 - g_lo^2) <= sum_j ||b_+ R_j g_lo||^2
  + ||b_- g_lo||^2, with b_(+-) = ((a_n)_(+-))^(1/2).
- ||b_- g_lo||^2. g = J^q W h gives g_lo = k * (W h) with k = F^(-1)[psi_mu <.>^q]. Peetre and Young as in Lemma QW-Q
  give ||b_- g_lo||^2 <= 2^sigma ||b_- W||_inf^2 ||w_sigma k||_1^2 ||h||^2, and ||b_- W||_inf^2 = sup((a_n)_- W^2),
  ||w_sigma k||_1 = kappa_q(mu). There is no high-frequency remainder, since the multiplier psi_mu has compact
  support.
- ||b_+ R_j g_lo||^2. Write omega_j psi_mu = omega_j psi_mu psi_nu + omega_j psi_mu (1 - psi_nu). The first part
  gives the operator b_+(X) phi_j(D), phi_j = i omega_j psi_mu psi_nu, which is Hilbert-Schmidt with norm
  ||b_+||_2 ||phi_j||_2/(2 pi). Since sum_j |phi_j|^2 <= psi_nu^2 and ||psi_nu||_2^2 <= 4 pi nu^2, the sum over j of the
  squared norms is at most ||(a_n)_+||_1 nu^2/pi. The second part is priced as in Lemma QW-Q with the kernel constant
  kappa_j(nu, mu). Then ||x + y||^2 <= t^(-1) ||x||^2 + (1 - t)^(-1) ||y||^2 for each j. QED.

Remarks.
- At P-S1, atil W^2 = 4 ubar.X - c exactly (sigma = 1, r0^2 = 1/4). Hence
  sup((a_n)_- W^2) <= sup_(|X| <= 2 rho) (c - 4 ubar.X)_+ and sup((a_n)_+ W^2) <= sup_(|X| <= 2 rho) (4 ubar.X - c)_+.
  The price grows with rho only through ubar.X on |X| <= 2 rho, at most like c + 8 rho sup_(|X| <= 2 rho) |ubar|.
  For the weight part alone (ubar = 0) the price is 2 c kappa_q(mu)^2 for every rho, and osc(a_f) <= c/(1 + 4 rho^2).
- If atil <= 0 on |X| <= 2 rho (that is, ubar.X <= c/4 there), then (a_n)_+ = 0. The Riesz pieces, nu, t and N3
  then drop out: e_II = osc(a_f) + 2 phi M2(a_n) mu^(-2) and P_II = 2 sup((a_n)_- W^2) kappa_q(mu)^2. Whether
  ubar.X <= c/4 holds near the origin for a registered background is part of N2 (OPEN).
- In Theorem H4-R, Proposition TII-0 supplies the T_II part of NE with eps_R contribution e_II and C_N contribution
  P_II. The pieces C_aw, C_tr, T_IS and C_vs need their own bounds (OPEN).
- The low part is of order 0 here: the cancellation of |omega(xi) - omega(eta)|^2 at small |zeta| is used only above
  mu. Section 3 shows what that costs.

## 3. Corollary PR-0 (price of the first form) and its evaluation

Corollary PR-0 (CLAIMED, elementary, given that kappa_q(mu) is nondecreasing in mu, a FLOAT observation from Table H4-2
and research/h4/nelo2_orient.out). Let the background satisfy N0 with beta_* <= cap (AT-211 for normalized
backgrounds), with ubar of class C^2 near 0 and div ubar = 0, and let T_II be bounded by Proposition TII-0 inside
Theorem H4-R at rate b0 < beta_*. Then the bound on C^opt(b0) obtained is at least
    P_0(b0) := 2^sigma c kappa_q(mu_0)^2,   mu_0 = (32 phi c/(cap - b0))^(1/2)   (sigma = 1, r0 = 1/2).
Proof. The slack condition of H4-R needs e_II <= beta_* - b0 <= cap - b0, so 2 phi M2(a_n) mu^(-2) <= cap - b0, and
Lemma M2-LB gives mu >= mu_0. chi_rho(0) = 1 and atil(0) = -sigma c, so sup((a_n)_- W^2) >= c. All other
contributions to the H4-R bound are nonnegative. Monotonicity of kappa_q gives P_II >= P_0(b0). QED.
If the bound of H4-R exceeds the necessary budget U(b0, R, n) of Corollary BUD-NEC (T2_H4A_v01, AT-369), it cannot
certify a CE P-S1 pass at those inputs, because every witness budget D at those inputs is at most U.

Table N1 (research/h4/nelo2_orient.out; kappa FLOAT, U upper decimals from Arb: bud_nec.out part 2 at ||F||_2 1.4e-5
and bud_nec2.out at 2.8e-6, beta0 <= c + 1; "excl" means B0-THR excludes every C0 at that cell).

| b0 | cap - b0 | mu_0 | kappa_q(mu_0) | P_0 | P_0/U, 1.4e-5, N 0.091 | N 0.10 | P_0/U, 2.8e-6, N 0.02 | N 0.06 | N 0.08 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.55 | 0.160319 | 24.18 | 4520.2 | 7.398e7 | excl | excl | - | - | - |
| 0.58 | 0.130319 | 26.82 | 5511.3 | 1.1e8 | excl | excl | - | - | - |
| 0.60 | 0.110319 | 29.15 | 6476.3 | 1.519e8 | 5.2 | excl | 0.00524 | 0.0117 | 0.0268 |
| 0.62 | 0.090319 | 32.21 | 7876.6 | 2.246e8 | 1.92 | excl | - | - | - |
| 0.64 | 0.070319 | 36.51 | 10091 | 3.687e8 | 1.71 | 4.25 | - | - | - |
| 0.65 | 0.060319 | 39.42 | 11761 | 5.008e8 | 1.87 | 3.66 | 0.013 | 0.0238 | 0.0391 |
| 0.66 | 0.050319 | 43.16 | 14111 | 7.209e8 | 2.23 | 3.81 | - | - | - |
| 0.68 | 0.030319 | 55.60 | 23607 | 2.018e9 | 4.53 | 6.66 | - | - | - |
| 0.70 | 0.010319 | 95.31 | 71820 | 1.868e10 | 32.4 | 43.6 | 0.374 | 0.608 | 0.865 |

- The kernel mass printed in nelo2_orient.out is 1 to within 3e-6 in every row (the quadrature check of Table H4-2).
- Between scan points, P_0 and U both increase with b0, so P_0(b0)/U(b0) >= P_0(b_left)/U(b_right). With the scan
  values this gives a ratio above 1.04 on [0.60, 0.70] at (1.4e-5, N 0.091) (the worst bracket is [0.62, 0.64]:
  2.246e8/2.15e8), and above 3.7 on (0.5928366, 0.60] (P_0(0.58)/U(0.60)). On [0.70, cap] the ratio is above
  1.868e10/6.49e8 = 28.7 (U at the cap, Table A5). At and below 0.5928366 the test is excluded (Table A3). So, with
  FLOAT kappa, the first form cannot certify the CE P-S1 test at any b0 <= cap at those stipulated inputs.
- The single-piece model price of T2_H4_v01 section 6 (C2 = 770: 4.64e9 at b0 0.60, 8.97e9 at 0.65) is larger than
  P_0 at these rates. The model piece has coefficient C2 = 770 and weight W2 = 3.2, against c and W(0)^2 = 1 for
  P_0, and this outweighs its gain from kappa_(q-1) in place of kappa_q. P_0 is a lower estimate for one piece and the
  model is a model for another, so no exact comparison is claimed.

## 4. Budgets at 007 + b14s size (Arb; stipulated inputs)

Inputs: ||F||_2 in {2.8e-6, 5.7e-6} and N in {0.02, ..., 0.12} are stipulated numbers chosen near the second numerics agent's FLOAT
007 + b14s report (||F_*||_2 2.844e-6 on 0.02 <= r <= 1e4, polar N_2 0.01408 at P-S1 on that range; the coordinator 04:52Z
item 2(e)). They are not certified, and the FLOAT N_2 is not a whole-plane value (AT-356 applies). For U a certified
lower of ||F||_2 is needed; for a witness D a certified upper (D decreases in R; Corollary SRC). The first theory agent's note 25 item
4(b) (witnesses D) and note 28 (U; AT-395 CONFIRMS, AT-396 corrects the reading) evaluate the same routines at
||F||_2 = 2.76e-6 and N = 0.0105 to 0.05. Tables N2 and N3 add ||F||_2 = 5.7e-6 and N up to 0.12; Table N4 is a
cross-check at their inputs and at the numerics_v04 FLOAT values (||F_*||_2 2.858e-6, mesh N_2 0.0145).

Table N2 (upper decimals of U, Corollary BUD-NEC, beta0 <= c + 1; research/h4/bud_nec2.out).

| ||F||_2 | b0 | N 0.02 | 0.04 | 0.06 | 0.08 | 0.10 | 0.12 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.8e-6 | 0.60 | 2.9e10 | 2.08e10 | 1.3e10 | 5.67e9 | excluded | excluded |
| 2.8e-6 | 0.65 | 3.86e10 | 2.96e10 | 2.1e10 | 1.28e10 | 4.97e9 | excluded |
| 2.8e-6 | 0.70 | 4.99e10 | 4.02e10 | 3.07e10 | 2.16e10 | 1.29e10 | 4.67e9 |
| 2.8e-6 | cap | 5.25e10 | 4.26e10 | 3.3e10 | 2.37e10 | 1.48e10 | 6.35e9 |
| 5.7e-6 | 0.60 | 6.78e9 | 4.83e9 | 2.98e9 | 1.24e9 | excluded | excluded |
| 5.7e-6 | 0.65 | 9.03e9 | 6.89e9 | 4.84e9 | 2.88e9 | 1.04e9 | excluded |
| 5.7e-6 | 0.70 | 1.17e10 | 9.36e9 | 7.11e9 | 4.96e9 | 2.89e9 | 9.36e8 |
| 5.7e-6 | cap | 1.23e10 | 9.92e9 | 7.64e9 | 5.44e9 | 3.33e9 | 1.33e9 |

Table N3 (lower decimals of the witness budget D = M (P(M) - N)/R^2 at one searched M, beta0 = 209/100, method of
Table A4; research/h4/budget_h4e.out). Any C0 >= max(0, C^opt(b0)) with C0 <= D passes the direct CE test at that
cell (AT-370 conditions).

| ||F||_2 | b0 | N 0.02 | 0.04 | 0.06 | 0.08 |
|---:|---:|---:|---:|---:|---:|
| 2.8e-6 | 0.60 | 1.44e10 | 1.01e10 | 6.01e9 | 2.17e9 |
| 2.8e-6 | 0.65 | 1.93e10 | 1.45e10 | 1e10 | 5.67e9 |
| 2.8e-6 | 0.70 | 2.5e10 | 1.98e10 | 1.49e10 | 1.01e10 |
| 5.7e-6 | 0.60 | 3.31e9 | 2.28e9 | 1.32e9 | 4.2e8 |
| 5.7e-6 | 0.65 | 4.43e9 | 3.31e9 | 2.23e9 | 1.22e9 |
| 5.7e-6 | 0.70 | 5.77e9 | 4.54e9 | 3.36e9 | 2.23e9 |

Table N4 (cross-check; research/h4/bud_nec3.out (U, beta0 <= c + 1, upper decimals) and budget_h4f.out (D,
beta0 = 209/100, lower decimals); stipulated inputs).

| ||F||_2 | N | U b0 0.60 | 0.65 | 0.70 | cap | D b0 0.60 | 0.65 | 0.70 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2.76e-6 | 0.0105 | 3.4e10 | 4.43e10 | 5.63e10 | 5.9e10 | 1.7e10 | 2.22e10 | 2.84e10 |
| 2.76e-6 | 0.0145 | 3.23e10 | 4.24e10 | 5.42e10 | 5.69e10 | 1.61e10 | 2.12e10 | 2.73e10 |
| 2.76e-6 | 0.0152 | 3.2e10 | 4.2e10 | 5.39e10 | 5.66e10 | 1.59e10 | 2.11e10 | 2.71e10 |
| 2.858e-6 | 0.0105 | 3.17e10 | 4.12e10 | 5.24e10 | 5.5e10 | 1.59e10 | 2.07e10 | 2.64e10 |
| 2.858e-6 | 0.0145 | 3.01e10 | 3.95e10 | 5.05e10 | 5.3e10 | 1.5e10 | 1.98e10 | 2.54e10 |
| 2.858e-6 | 0.0152 | 2.98e10 | 3.91e10 | 5.02e10 | 5.27e10 | 1.48e10 | 1.96e10 | 2.52e10 |

- At (2.76e-6, N 0.0152) the U row equals the first theory agent's note 28 (3.2e10, 4.2e10, 5.39e10, 5.66e10) and the D row equals
  note 25 item 4(b) (1.59e10, 2.11e10, 2.71e10) in every printed digit.
- Each D is below the U of the same cell, as it must be (beta0 209/100 against beta0 <= c + 1). As AT-396 notes, D
  and U bound the tolerated constant C0; they are not lower bounds on C^opt(b0).
- Reading (HEURISTIC). At ||F||_2 = 2.8e-6 the budgets are of order 1e10, against 1e8 at the C5 + b14s size
  (Tables A4, A5). At (2.76e-6, N 0.0152), P_0 is 0.47, 1.2 and 35 percent of U and 0.96, 2.4 and 69 percent of D at
  b0 = 0.60, 0.65 and 0.70. At ||F||_2 = 2.8e-6, P_0 is 1 to 9 percent of D at b0 = 0.60 and 0.65, and 75 to 185 percent
  at 0.70. At 5.7e-6 it is 4.6 to 36 percent (0.60), 11 to 41 percent (0.65) and 324 to 838 percent (0.70). The
  single-piece model price with C2 = 770 (4.64e9 at b0 0.60, 8.97e9 at 0.65; T2_H4_v01 section 6) is below D for
  N <= 0.06 at both rates at 2.8e-6, and above every D at 5.7e-6. With
  C2 = 7700 (5.77e11, 1.12e12) it is above every D. The P-S1 content N(F) and ||F||_2 of 007 + b14s are not
  certified, and the actual H4 constant is not known, so none of this is a pass.

## 5. N2 inputs for Proposition TII-0 (with the numerical auditor; AT-357 method)

For a registered background (C5 or unchanged 007 with the b14s correction, once its frozen ID and background
certificates exist) Proposition TII-0 needs, for one chosen rho:
1. sup_(|X| <= 2 rho) (c - 4 ubar.X)_+ and sup_(|X| <= 2 rho) (4 ubar.X - c)_+ (the second may be 0);
2. sup_(|X| >= rho) (atil)_+ and sup_(|X| >= rho) (atil)_-, with atil = (4 ubar.X - c)/(1 + 4|X|^2);
3. M2(chi_rho atil) through Lemma MOM: M2 <= (4 pi)^(-1/2) ||Delta (1 - Delta)(chi_rho atil)||_2, an L^2 norm of
   derivatives of order 2 to 4 of chi_rho atil. By Leibniz this needs derivatives of ubar up to order 4 on
   |X| <= 2 rho, plus explicit derivatives of chi_rho and of (r0^2 + |X|^2)^(-1). AT-357 CONFIRMS, conditionally and
   for the compactified source, a method for integer derivative energies through order 3 (the same order-K
   coefficients serve every derivative prefix through K). Applied to ubar, item 3 needs it through order 4;
4. if (a_n)_+ is not 0: ||(a_n)_+||_1 and kappa_j(nu, mu) (N3).
The background enters only through ubar (atil is explicit in ubar at P-S1). Items 1 and 2 are sup norms of an
explicit function of ubar; item 3 is the only energy input.

## 6. Requests

- The theory auditor: audit Lemma OSC, Lemma M2-LB, Proposition TII-0 and Corollary PR-0 (CLAIMED), and Tables N2 and N3 (same
  routines as AT-369 and AT-370). Table N1 is FLOAT in kappa.
- The first theory agent: cite Proposition TII-0 as the first form of NE-lo for T_II, with the open status of the other pieces, and
  Corollary PR-0 as the reason the order-0 low part fails at the C5 + b14s size.
- The numerical auditor (with the first numerics agent for the frozen IDs): the N2 items of section 5 for the 007 + b14s background (and C5 + b14s),
  starting with items 1 and 2 at rho in {2, 5, 10}, and whether ubar.X <= c/4 holds on |X| <= 2 rho.
- The second numerics agent: whole-plane ||F||_2 (certified upper and lower) and N(F) at P-S1 for 007 + b14s; Tables N2 and N3 then give
  the budgets.
- The coordinator (ledger input): at stipulated 007 + b14s-size inputs the CE P-S1 budgets are about 1e10 (Tables N2 to N4;
  Table N4 reproduces the first theory agent's notes 25 and 28 at their inputs), against about 1e8 at the C5 + b14s size. The first
  form of NE-lo for T_II fails at C5 + b14s size (Corollary PR-0, FLOAT kappa) and is not excluded at 007 + b14s
  size. H4 at P-S1 remains OPEN.

## 7. Files and real run times (paths relative to the agent directory; core 40, nice 19, one thread)

| file | run (UTC, 2026-11-03) | exit | label |
|---|---|---|---|
| research/h4/bud_nec2.py, bud_nec2.out, run_bn2.log | 05:03:55Z to 05:04:14Z | 0 | Arb |
| research/h4/nelo2_orient.py, nelo2_orient.out, run_no2.log | 05:06:25Z to 05:07:42Z | 0 | FLOAT |
| research/h4/budget_h4e.py, budget_h4e.out, run_e.log | 05:07:59Z to 05:08:14Z | 0 | Arb |
| research/h4/bud_nec3.py, bud_nec3.out, run_x3.log | 05:14:45Z to 05:15:03Z | 0 | Arb |
| research/h4/budget_h4f.py, budget_h4f.out, run_x3.log | 05:15:03Z to 05:15:22Z | 0 | Arb |
| research/h4/nelo1_orient.py, nelo1_orient.out | 04:59:04Z, under 1 s | 0 | HEURISTIC, superseded |

- bud_nec2.py imports bud_nec.py unchanged and changes only the input lists. budget_h4e.py is budget_h4d.py with the
  b0, ||F||_2 and N lists and the first comment line changed. bud_nec3.py and budget_h4f.py are bud_nec2.py and
  budget_h4e.py with the ||F||_2 and N lists, the print precision of ||F||_2 and the first comment line changed.
  nelo2_orient.py copies the kappa function of kappa_h4.py unchanged.
- nelo1_orient.py (a first orientation) used half of the slack and the combined coefficient 2 + c_aw of Lemma HI'
  for the T_II piece, and the FLOAT power fit kappa_q = 5.0 mu^2.1. That choice of parameters is not the cheapest one
  for the T_II piece, so its ratios (309 and more) are not used; Corollary PR-0 replaces it.
