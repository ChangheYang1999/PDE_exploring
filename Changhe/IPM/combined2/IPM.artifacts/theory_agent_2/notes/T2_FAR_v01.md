# T2_FAR_v01: the far part of atil charged to the free gain; scope of AT-423; smallest split radius for 009 (FLOAT)

Agent the second theory agent. This is the shift-3 scope check announced in team notes 05:53Z item 2 (scratch/h4/nelo3_plan.md section 7):
is the far-oscillation cost of AT-423 (the numerical auditor OBS-H4-OSC-001) carried by every construction, or only by the TII-0
construction? It also answers, in FLOAT, three requests of the coordinator for the complete 009 coefficient:
- 06:36Z item 3(c): the smallest split radius rho at which the TII-1 and C_aw coefficients fit under G = q (c - s_*)
  for the FLOAT s_*, the near price at that rho against D, and the inputs that need certificates;
- 07:16Z item 3: the combined far charge priced against Gbar = q (c - 3/2) first, with the excess if it does not fit;
- 07:37Z item 3(c): the smallest such rho as a function of the certified gain G, with the near price at each.
The analytic sections 1 to 3 were audited as a draft by the theory auditor (AT-512 to AT-518, 06:58:17Z; Lemma SC-LB in AT-544 to
AT-548 and AT-553); this version adopts the smaller C_aw weight of AT-514, the repair of AT-516 and the corrected
Lemma SC-LB. The FLOAT screen of the 07:41Z interim entry was replayed by the theory auditor (AT-574 to AT-576); section 5 adopts its
qualifications. Builds on notes/T2_H4_v01.md (setting of section 2, Proposition DR, Lemma KER, Theorem H4-R; AT-332,
AT-361 to AT-366) and notes/T2_NELO_v01.md (Lemma OSC, Proposition TII-0; AT-402 to AT-408). Labels as there:
CONFIRMED (cited audit), CLAIMED (proved here, audit requested), FLOAT, HEURISTIC, OPEN. P-S1 = (21/10, 1, 1/2),
W^2 = 1 + 4|X|^2, c = 4076476460239181/2251799813685248, cap = c + 1 - q. All times are real UTC times.

## 0. Summary

Statuses of the analytic results are as in sections 1 to 3. Every number in items 3 to 7 is a FLOAT value of a far
constant or a HEURISTIC value of the HF-1 model near price, set against the first theory agent's Arb budgets at stipulated inputs
(||F||_2 = 2.76e-6; N = 0.022, or 0.0141 in brackets). None of them is a bound.

1. Scope of AT-423 (Corollary SC; CONFIRMED conditionally, AT-513). Under Proposition FG the far part a_f of atil is
   charged to the free gain G = q (c - s_*) through (FG1). The slack condition of Theorem H4-R then contains no
   osc(a_f) term, so the oscillation term that AT-423 uses is specific to the TII-0 construction. Every construction
   of this kind needs SC(a_f) <= G (Lemma SC-LB; CONFIRMED, AT-545 and AT-553), and with Lemma TII-1 also
   osc(a_f) < G. For 009, G <= q because s(0) = c - 1 exactly. The AT-423 oscillation bounds for 009 and 008
   (0.909, 0.623 and 0.451) are below q.
2. Far constant. Lemma TII-1 (CONFIRMED conditionally, AT-473 and AT-513) and Lemma CAW-F with the AT-514 weight
   (CONFIRMED, AT-514) give the admissible (FG1) constant A_a = min_nu A_nu(a_f) + (q^2/2) M2[w_new](a_f).
3. The coordinator 07:37Z item 3(c). The smallest split radius rho_G with A_a <= G for the complete 009 coefficient
   (Table F4; FLOAT; interpolated between scanned radii), and the near price there (Table F9; HEURISTIC; min over the
   sampled rates b0 of P_A/U, and P_A/D at b0 = 0.60):

   | G | rho_G, log 16 | rho_G, log 8 | P_A/U at rho_G (log 16) | P_A/D at rho_G (log 16) |
   |---|---:|---:|---:|---:|
   | Gbar = q (c - 3/2) = 0.6517 | 4.0 | 6.1 | 7.89 [6.87] | 16.6 [14.8] |
   | 1.0 | 2.92 | 4.41 | 4.82 [4.19] | 10.1 [9.02] |
   | 1.5 | 2.25 | 3.38 | 3.23 [2.81] | 6.81 [6.05] |
   | 2.0 | 1.9 | 2.86 | 2.49 [2.17] | 5.25 [4.66] |
   | q = 2.1 | 1.85 | 2.78 | 2.39 [2.08] | 5.03 [4.47] |

   Log 16 is the best of the scanned cut families (log 4 to 64, lin 1.5 to 4). The minimum over the sampled rates
   (b0 = 0.30 to 0.70, section 5) is at b0 = 0.55 in every row. If (FG1) is certified through derivative energies of the complete source with a smooth
   cutoff (AT-475; AT-482 with J4 = 0), rho_G grows by 19 to 60 percent (log 16: 5.2 at Gbar, 2.84 at q).
4. The coordinator 06:36Z item 3(c). At the FLOAT s_* = s(0) = c - 1 (G = q), the TII-1 and C_aw coefficients fit from
   rho = 1.85 on (log 16). The near price there is P_A = 5.0 D at b0 = 0.60, and 2.4 U at the best rate. The
   inputs that need certificates are listed in 6.1, (C1) to (C7).
5. The coordinator 07:16Z item 3 (Gbar first). A_a fits under Gbar from rho = 4.0 on (log 16). The near price there is
   7.9 U [6.9 U]. The best scanned split with A_a <= Gbar (log 32 at rho 3) gives 8.93 U [7.78 U] (AT-575). If
   instead the split is put where the near price meets U (rho_U = 1.07 [1.17] for log 16), A_a is 6.31 [5.25]: the
   excess over Gbar is 5.65 [4.59], and over all families a factor of 8 to 16 (Table F8). Within D the excess factor
   is about 29 or more.
6. Reading (HEURISTIC). In the HF-1 model with the TII-1 + CAW-F far charge, no certified gain G <= q closes the route
   for 009: the price exceeds U at every sampled rate (AT-552 wording: C_constr >= P > U excludes this construction
   only; the all-rate exclusion is not certified, AT-576). The near price at the threshold scales roughly like 1/G,
   so the route would need G of about 2.1 q to 2.4 q. The shape of the cut is not the lever. A certified s_* close to
   c - 1 (the numerical auditor strain refinement) lowers the excess from about 7.9 U to about 2.4 U, but does not remove it.
7. The lever is the far estimate (O2, OPEN). At rho_U, A_a is 16 to 20 times the floor SC(a_f), and it exceeds the
   larger of SC(a_f) and the FLOAT band-limited value by factors 12 to 34 at the rows of Table F7. To fit under the
   gain at rho_U a far constant must be within a factor 1.0 to 2.1 of SC(a_f) at G = Gbar, or 3.3 to 6.8 at G = q
   (Table F10). Since osc(a_f) at rho_U is
   0.55 to 0.73 (0.85 to 1.12 Gbar), a constant with the TII-1 low block osc(a_f)(1 + nu^2) would have to lose almost
   nothing else to fit under Gbar there. Under q it can fit, if the M2 and C_aw overheads shrink by a factor of 3 to 5.
8. Section 7 corrects the 07:41Z interim figures. Section 8 lists the requests to the coordinator, the theory auditor, the numerical auditor, the second numerics agent and
   the first theory agent. The far side at rho in [1, 2] asked for in the coordinator 08:10Z item 3(a) (band-limited values at kmax 4 pi and
   8 pi, a far upper for the complete 009 form, P_A and P_B with the M4 sensitivity at rho 1 and 2, prices at
   N 0.0161) is not in this version; it follows in a later note.

## 1. Setting and the general-coefficient kernels

Setting and notation as in T2_H4_v01 section 2. Tests g are real S1 Schwartz functions, J = <D>, R_j = d_j |D|^(-1)
with symbol i omega_j(xi), omega(xi) = xi/|xi|, f^(xi) = int e^(-i X.xi) f(X) dX,
S[k](g) = (2 pi)^(-4) int int k(xi, eta) g^(eta) conj(g^(xi)) d eta d xi and zeta = xi - eta. For a real function a
with a^ in L^1(R^2) (so a is bounded and continuous) put
    Q_a(g) := sum_j <a R_j g, R_j g> - <a g, g>,      C_aw[a](g) := <a g, g> - Re<a J^(-q) g, J^q g>,
    osc(a) := sup a - inf a,   Wi(a) := (2 pi)^(-2) int |a^|,   M2(a) := (2 pi)^(-2) int |zeta|^2 |a^(zeta)| d zeta,
    M_(2,m)(a) := (2 pi)^(-2) int |zeta|^2 (1 + |zeta|)^m |a^(zeta)| d zeta,   M2[w](a) := (2 pi)^(-2) int |zeta|^2 w(zeta) |a^(zeta)| d zeta,
    H_q(t) := [sinh(q t/2)/(q sinh(t/2))]^2 for t > 0, H_q(0) := 1,   w_new(zeta) := H_q(asinh(|zeta|/2))   (AT-514).
s_* := sup over the plane of s(X) = lambda_max Sym D ubar(X) (the audit name; earlier agent notes call it s_inf).
For smooth a of moderate growth, C_aw[a](g) = -Re<[J^q, a] J^(-q) g, g>, the form of Lemma 2.0 of T2_H4_v01. Both
forms are linear in a and vanish for constant a. Hence T_II = Q_atil (T2_NELO_v01 section 1, AT-361) and
C_aw = C_aw[a_W] = C_aw[atil], since a_W - atil = sigma c is constant.

Lemma KER' (CONFIRMED conditionally, AT-512; Lemma KER of T2_H4_v01 for a general coefficient). If a is real with a^ in L^1, then
for every test, with r = <xi>/<eta> and absolutely convergent integrals,
    Q_a(g) = S[-(1/2) a^(zeta) |omega(xi) - omega(eta)|^2](g),   C_aw[a](g) = S[-(1/2) a^(zeta) (r^(q/2) - r^(-q/2))^2](g).
Proof.
- (a f)^ = (2 pi)^(-2) a^ * f^ for f in L^2, and <f, k> = (2 pi)^(-2) int f^ conj(k^). Hence for f, k in L^2
  with f^, k^ suitably weighted, <a f, k> = (2 pi)^(-4) int int a^(xi - eta) f^(eta) conj(k^(xi)).
- With f = k = R_j g, (R_j g)^ = i omega_j g^, and the sum over j gives the kernel a^(zeta) omega(xi).omega(eta).
  Subtracting <a g, g> gives a^(zeta)(omega(xi).omega(eta) - 1) = -(1/2) a^(zeta) |omega(xi) - omega(eta)|^2.
- With f = J^(-q) g and k = J^q g the kernel is a^(zeta) r^q. Since a is real, conj(a^(zeta)) = a^(-zeta), and
  exchanging xi and eta shows Re S[a^ r^q](g) = S[a^ (r^q + r^(-q))/2](g). Then
  1 - (r^q + r^(-q))/2 = -(1/2)(r^(q/2) - r^(-q/2))^2.
- Absolute convergence: int int |a^(xi - eta)| F_1(xi) F_2(eta) <= ||a^||_1 ||F_1||_2 ||F_2||_2 (Young), with
  F_1, F_2 among |g^|, <.>^(+-q) |g^|, all in L^2 for a test. QED.

Remark DEC (hypotheses for an actual far part; CONFIRMED conditionally, AT-512, which also covers 1 <= q < 3). Let a be C^6 on R^2 with
|d^alpha a(X)| <= C_a <X>^(-gamma - |alpha|) for |alpha| <= 6 and some gamma in (0, 2). Then a^ is in L^1 and
Wi(a), M2(a) and M_(2,q)(a) are finite. Sketch: take a smooth dyadic partition 1 = sum_k phi_k with phi_k supported in
2^(k-1) <= |X| <= 2^(k+1) for k >= 1. Then a phi_k = b_k(X/2^k) with ||b_k||_(H^6) <= C 2^(-k gamma), and
int |zeta|^m |(b(./lambda))^| d zeta = lambda^(-m) int |zeta|^m |b^| for lambda > 0. In two dimensions
int (1 + |zeta|)^m |b^| <= C_s ||b||_(H^(m + s)) for s > 1, and 2 + q + 1 < 6, so the pieces are summable. The
weights only need (1 + 2^k |zeta|)^q >= (1 + |zeta|)^q, and w_new <= (1 + |zeta|)^(q-1). For atil, gamma = 1 - 1/c; the
qualitative decay of the accepted 009 source follows from AT-476, and explicit constants are OPEN (N2). For a = (1 - chi) atil with chi smooth and compactly supported, the same holds.

## 2. Two far lemmas

Lemma TII-1 (CONFIRMED conditionally, AT-473 and AT-513). Let a be real with a^ in L^1 and M2(a) finite. For every nu > 0 and every test,
    Q_a(g) <= A_nu(a) ||J^(-1) g||^2,   A_nu(a) := lambda_max [[osc(a)(1 + nu^2), beta], [beta, beta/4]],
    beta := 2 (1 + nu^(-2)) M2(a).
Proof.
- Split g = g_l + g_h with g_l^ = 1_(|xi| < nu) g^. Both are real (the cutoff is radial and even) and
  x^2 + y^2 = ||J^(-1) g||^2 with x = ||J^(-1) g_l||, y = ||J^(-1) g_h||. Q_a is a real quadratic form, so
  Q_a(g) = Q_a(g_l) + 2 B_a(g_l, g_h) + Q_a(g_h), with B_a its symmetric bilinear form and the kernel of Lemma KER'.
- Low-low. Lemma OSC (T2_NELO_v01, AT-402) gives Q_a(g_l) <= osc(a) ||g_l||^2, and <xi>^2 <= 1 + nu^2 on the support
  of g_l^, so Q_a(g_l) <= osc(a)(1 + nu^2) x^2.
- Two elementary inequalities. (i) |omega(xi) - omega(eta)| <= 2 |zeta|/max(|xi|, |eta|): if |xi| >= |eta|,
  |xi/|xi| - eta/|eta|| <= |zeta|/|xi| + |eta| (1/|eta| - 1/|xi|) <= 2 |zeta|/|xi|. (ii) |omega(xi) - omega(eta)|^2
  <= |zeta|^2/(|xi| |eta|), since |zeta|^2 = |xi|^2 + |eta|^2 - 2 |xi| |eta| cos theta >= 2 |xi| |eta| (1 - cos theta)
  and |omega(xi) - omega(eta)|^2 = 2 (1 - cos theta).
- Cross term. Here max(|xi|, |eta|) =: m >= nu, and <xi> <eta> <= 1 + m^2 <= (1 + nu^(-2)) m^2. By (i) the kernel is
  bounded by 2 (1 + nu^(-2)) |zeta|^2 |a^(zeta)| <xi>^(-1) <eta>^(-1). With G_l = <.>^(-1) |g_l^| and
  G_h = <.>^(-1) |g_h^|, Young gives |B_a(g_l, g_h)| <= (2 pi)^(-4) 2 (1 + nu^(-2)) ||  |.|^2 a^ ||_1 ||G_l||_2 ||G_h||_2
  = 2 (1 + nu^(-2)) M2(a) x y = beta x y, since ||G_l||_2^2 = (2 pi)^2 x^2.
- High-high. Here |xi|, |eta| >= nu, so <xi> <= (1 + nu^(-2))^(1/2) |xi| and likewise for eta. By (ii) the kernel is
  bounded by (1/2)(1 + nu^(-2)) |zeta|^2 |a^(zeta)| <xi>^(-1) <eta>^(-1), and |Q_a(g_h)| <= (beta/4) y^2.
- Sum: Q_a(g) <= osc(a)(1 + nu^2) x^2 + 2 beta x y + (beta/4) y^2 <= A_nu(a)(x^2 + y^2). QED.
Remarks.
- A_nu(a) >= osc(a)(1 + nu^2), which is > osc(a) for every nu if a is not 0 (a = 0 gives equality; AT-516). At low frequency ||J^(-1) g|| and ||g|| are comparable, and by
  AT-451 the constant 1 of Lemma OSC is sharp among coefficients with given oscillation. So a TII-1-type bound cannot
  have a constant below osc(a) times the best low-frequency Lemma OSC constant for the actual coefficient.
- The lemma uses only the size of a^ times |zeta|^2, and at the radii where it fits under the gain its low block
  osc(a)(1 + nu^2) dominates. For the far part of the complete 009 coefficient it exceeds the larger of the FLOAT band value
  and the floor SC(a_f) of Lemma SC-LB by factors 12 to 34 (Table F7), and with Lemma CAW-F it fits under G = q only from
  rho of about 1.85 on and under Gbar from rho of about 4 on (log cut lam 16, Table F4).

Lemma CAW-F (CONFIRMED, AT-514; the theory auditor's sharper form of the draft lemma, with the exact bracket ratio). Let q >= 1 and
let a be real with a^ in L^1 and M2[w_new](a) finite. For every test,
    |C_aw[a](g)| <= (q^2/2) M2[w_new](a) ||J^(-1) g||^2.
Proof.
- Put L = <xi>, l = <eta>, t = |log(L/l)|. Then (r^(q/2) - r^(-q/2))^2 = 4 sinh(q t/2)^2 and (L - l)^2 = 4 L l sinh(t/2)^2,
  so (r^(q/2) - r^(-q/2))^2 = q^2 (L - l)^2 H_q(t)/(L l), with equality also at t = 0.
- H_q is nondecreasing on [0, infinity) for q >= 1: with x = t/2, (d/dx) log(sinh(q x)/sinh x) = q coth(q x) - coth x >= 0,
  because y coth y is nondecreasing (its derivative has the sign of sinh y cosh y - y, which vanishes at 0 and has
  derivative 2 sinh(y)^2 >= 0).
- <.> is 1-Lipschitz, so |L - l| <= |zeta|. Over |xi - eta| = d the ratio <xi>/<eta> is at most
  R_*(d) = (d + (d^2 + 4)^(1/2))/2 = exp(asinh(d/2)) (AT-514; the maximum of (1 + (s + d)^2)/(1 + s^2) over real s is
  R_*(d)^2, and the collinear configuration is the worst one). So t <= asinh(|zeta|/2) and H_q(t) <= w_new(zeta).
- The kernel of Lemma KER' is therefore bounded by (q^2/2) |zeta|^2 w_new(zeta) |a^(zeta)| <xi>^(-1) <eta>^(-1), and
  Young as in Lemma TII-1 gives the claim. QED.
Remarks.
- w_new(zeta) <= min((1 + |zeta|)^(q-1), cosh(q |zeta|/4)^2), and w_new(zeta) ~ |zeta|^(q-1)/q^2 as |zeta| -> infinity
  (AT-514). So Lemma CAW-F implies the AT-474 bound (q^2/2) M_(2,q-1)(a), and the moment is finite under the
  M_(2,11/10) condition of AT-482. At q = 2.1 and |zeta| = 1, 2, 4, 8 the weight is 1.067, 1.238, 1.723, 2.882, against
  1.302, 2.572, 17.18, 100.9 for the first draft weight min((1 + |zeta|)^q, cosh(q |zeta|/4)^2) (AT-514). For the actual
  far part M_(2,q-1)(a_f)/M2[w_new](a_f) is 3.7 / 2.7 / 1.8 / 1.4 at rho 1 / 3 / 8 / 16 (log cut lam 8, Table F1).
- An intermediate form with t <= min(log(1 + |zeta|), |zeta|/2) in place of asinh(|zeta|/2) was in the agent draft at
  07:00Z; it is superseded (its values, M2w in the run files, are 0.2 to 8.7 percent above M2[w_new] for the actual far part).

Lemma SC-LB (high-frequency floor for (FG1); CONFIRMED in this corrected form by the theory auditor AT-545 and, under the weaker
moment hypothesis stated here, AT-553, after AT-544 and AT-546 refuted the first version). Let a be real with a^ in
L^1 and M2(a) finite, so that a is C^2 with bounded continuous Hessian H = Hess a, and let a be even in both
coordinates (atil is, and so is every product of atil with a radial cut). If a constant A satisfies
Q_a(g) + C_aw[a](g) <= A ||J^(-1) g||^2 for every test, then
    A >= SC(a) := (1/2) sup_X max_(|theta| = 1) [q^2 H(X)(theta, theta) + H(X)(theta_perp, theta_perp)]
               = (1/2) sup_X [(q^2 - 1) lambda_max H(X) + tr H(X)].
The same argument for Q_a alone gives A >= (1/2) sup_X lambda_max H(X) =: SC_II(a). Without the evenness, a must be
replaced by its average abar over the coordinate reflections: for S1 tests g^2, |R_j g|^2 and (J^(-q) g)(J^q g) are even
in both coordinates, so Q_a = Q_abar and C_aw[a] = C_aw[abar] on tests. (A first version without this hypothesis was
false: a = x exp(-|X|^2) has abar = 0 and SC(a) > 0.)
Proof.
- Packets. Fix X0 off the coordinate axes and a unit vector theta. Let phi be a nonzero real radial Schwartz function
  with phi^ supported in |xi| <= C, h_lambda(X) = phi(lambda^(1/2)(X - X0)) cos(lambda theta.X), and
  g_lambda(X) = sum over the four reflections S = diag(+-1, +-1) of S_22 h_lambda(S X), a test. Every Fourier
  component of g_lambda lies in a ball of radius C lambda^(1/2) about one of the points +- lambda S theta, so
  ||J^(-1) g_lambda||^2 = lambda^(-2) ||g_lambda||^2 (1 + O(lambda^(-1/2))).
- Large transfers and distinct clusters. For lambda/2 <= |xi|, |eta| <= 2 lambda both kernel factors of Lemma KER' are
  at most C_q lambda^(-2) |zeta|^2 (|log r| <= C lambda^(-1) |zeta| and r is bounded). So by Young the part of either
  form with |zeta| > R is at most C_q lambda^(-2) m2(R) ||g_lambda||^2, m2(R) := (2 pi)^(-2) int_(|zeta| > R) |zeta|^2 |a^|,
  which tends to 0 as R -> infinity. Distinct clusters are at distance comparable to lambda, so their interaction
  (including + lambda theta against - lambda theta) is o(lambda^(-2)) ||g_lambda||^2.
- One cluster. For xi, eta in B(lambda nu, C lambda^(1/2)), integrating D omega(p) = |p|^(-1)(I - omega omega^T) and
  grad log <p> = p/<p>^2 along the segment from eta to xi gives, with additive errors,
      |omega(xi) - omega(eta)|^2 = lambda^(-2) (zeta.nu_perp)^2 + O(lambda^(-5/2) |zeta|^2),
      (r^(q/2) - r^(-q/2))^2 = q^2 lambda^(-2) (zeta.nu)^2 + O_q(lambda^(-5/2) |zeta|^2).
  (Multiplicative errors are not uniform: zeta.nu = 0 does not force r = 1.) The kernel -(1/2) a^(zeta) (zeta.e)^2 is
  the form (1/2) int (d_e^2 a) |v|^2, since (d_e^2 a)^ = -(zeta.e)^2 a^. Hence, for v with Fourier support in that ball,
  (Q_a + C_aw[a])(v) = (1/(2 lambda^2)) int b_nu(X) |v|^2 dX + O_q(lambda^(-5/2) M2(a) ||v||^2),
  b_nu := q^2 H(nu, nu) + H(nu_perp, nu_perp).
- Limit. Within one cluster the leading term is multiplication by the bounded continuous function b_nu, and products
  of packets with distinct spatial centres have L^1 norm o(lambda^(-1)). The reflected packet S h_lambda(S .) has
  direction S theta and centre S X0, and b_(S theta)(S X0) = b_theta(X0) because a is even in both coordinates. So
  (Q_a + C_aw[a])(g_lambda)/||J^(-1) g_lambda||^2 -> (1/2) b_theta(X0). H is continuous, so the supremum over X0 off
  the axes is the supremum over the plane; b_theta = (q^2 - 1) H(theta, theta) + tr H, and maximizing over theta gives
  the second form since q^2 > 1. QED.
Remarks.
- The repairs (evenness, additive cluster errors, compact Fourier support of the packets, the integrable moment tail)
  were found independently by the theory auditor (AT-544 to AT-546; full proof in the theory auditor research/high_frequency_floor_audit/PROOF.md)
  and by an external model consulted by this agent (the external referee, 07:20Z to 07:26Z). Sign check: for
  a = -exp(-|X|^2), H(0) = 2 I and the lemma forces A >= q^2 + 1 = 5.41. For atil itself the joint floor at the
  origin is 4 (q^2 (2c - 1) + 1), about 50.228 (AT-547); the HF-1 sufficient formula uses the larger 56.711, and the
  two differ by exactly 8 (c - 1). Neither applies to a far part that vanishes near 0.
- The C_aw limit (q^2/2) H(theta, theta) agrees with the symbol of J^q a J^(-q) + J^(-q) a J^q. A finite-band FLOAT
  test (band |xi_i| <= k) underestimates the best constant in (FG1): for the log cut lam 4 at rho 1 (007 background)
  the band-limited best constants are 0.75 at k = 2 pi and 1.25 at k = 4 pi, against SC = 2.72
  (research/h4/far009/runs/scan2.log and near_diag2.out). These are periodic collocation eigenvalues (FLOAT). They
  become continuum lowers only with controlled periodization, interpolation and aliasing errors (AT-554).
- So every construction that charges a far part a_f to the free gain (Proposition FG) needs SC(a_f) <= G, whatever
  the far estimate. SC(a_f) is an explicit pointwise quantity of the Hessian of a_f.

## 3. The free gain and the far part

Proposition FG (CONFIRMED conditionally, AT-513). Assume the setting of T2_H4_v01 section 2 at P-S1 and s_* < c. Let
atil = a_n + a_f with a_f real, a_f^ in L^1, and let A_far >= 0 be such that for every test
    Q_(a_f)(g) + C_aw[a_f](g) <= A_far ||J^(-1) g||^2.                                                   (FG1)
Put G := q (c - s_*) and
    D_rem^n := T_IS + Q_(a_n) + C_tr + C_aw[a_n] + C_vs.
Then for every test
    D_rem(g) <= -(G - A_far) ||J^(-1) g||^2 + D_rem^n(g).
In particular, if A_far <= G and D_rem^n satisfies the NE inequality of Theorem H4-R with some eps_R, C_N and pairs
(a_i, Phi_i), then D_rem satisfies NE with the same eps_R, C_N and pairs. With Lemmas TII-1 and CAW-F,
A_far = min over nu of A_nu(a_f) + (q^2/2) M2[w_new](a_f) is admissible in (FG1). If only an upper s_* <= sbar < c is
certified, the proposition holds with G(sbar) := q (c - sbar) in place of G.
Proof. Proposition DR gives D_rem = T_I + T_II + C_tr + C_aw + C_vs with
T_I <= -q (c - s_*) ||J^(-1) g||^2 + T_IS. By linearity, T_II = Q_(a_n) + Q_(a_f) and C_aw = C_aw[a_n] + C_aw[a_f].
Insert (FG1). If A_far <= G the first term is <= 0. QED.
Remark (AT-513). G is used once. If T_IS, C_tr or C_vs are also charged to the free gain, they share G - A_far.

Corollary NT (near part of T_II; CONFIRMED conditionally, AT-513). Let a_n be real, bounded, supported in a bounded set, with
M2(a_n) finite and sup(|a_n| W^2) finite. The proof of Proposition TII-0 without its far step gives, for every
mu, nu > 0, t in (0, 1) and test g,
    Q_(a_n)(g) <= e_n ||g||^2 + P_II ||h||^2,   e_n = 2 phi M2(a_n) mu^(-2) + t^(-1) pi^(-1) ||(a_n)_+||_(L^1) nu^2,
with P_II exactly as in Proposition TII-0. There is no osc(a_f) term.
Proof. Proposition TII-0 bounds Q_(a_f) by Lemma OSC and Q_(a_n) by the high part (Lemma HI with
A_l = 2 M2(a_n)), the order-0 low part and the Riesz band. Only the last three steps are used, and they need only
the stated properties of a_n (the compact support of chi_rho is not used beyond them). QED.

Corollary SC (scope of AT-423; CONFIRMED conditionally, AT-513). Insert Proposition FG with A_far <= G, and Corollary NT for
Q_(a_n), into Theorem H4-R, with any bounds for the other pieces of D_rem^n. Then the slack condition of H4-R contains
e_n and the slack contributions of the other pieces, and no osc(a_f) term. The far part enters only through (FG1)
and the condition A_far <= G. Since s_* >= s(0), G <= q (c - s(0)), which is q for backgrounds with s(0) = c - 1 (009: exact by the
normalization, the second numerics agent 07:05Z, AT-479). Any (FG1) constant is >= SC(a_f) (Lemma SC-LB), so every such construction needs
SC(a_f) <= G. If A_far is taken from Lemmas TII-1 and CAW-F and a_f is not 0, then A_far > osc(a_f), so this route
needs in addition osc(a_f) < G <= q.
Proof. Read off from Proposition FG, Corollary NT and Theorem H4-R. QED.
Consequences.
- AT-423 is stated for the TII-0/H4-R construction, and Corollary SC shows that the oscillation term it uses is
  specific to that construction: under Proposition FG the far part costs no rate. The AT-423 oscillation lower
  bounds for 009 and 008 (0.909, 0.623 and 0.451 on circles of radius 4, 10 and 20) are below q = 2.1. So they do
  not exclude a Proposition FG construction.
- This does not give a far bound for 009 or 008. It moves the question to (FG1): a certified A_far <= G for the
  actual a_f, with G - A_far left for T_IS, C_tr and C_vs if those pieces are also charged to the free gain.
  Section 5 shows in FLOAT that Lemmas TII-1 and CAW-F fit under the gain only at split radii where the HF-1 model
  near price exceeds the budget (Tables F4, F8 and F9), and that they exceed the larger of the FLOAT band value and
  SC(a_f) by factors 12 to 34 (Table F7).
- The free gain needs s_* < c (OPEN, AT-212). For 009, s(0) = c - 1 exactly (the second numerics agent 07:05Z, AT-479), and the FLOAT
  value of s_* is s(0), so G <= q.

Remark HP (HF-1 principal floor with ubar; CLAIMED, elementary). At P-S1, if ubar is C^2 near 0 with ubar(0) = 0,
    Hess atil(0) = 8 c I + 8 S(0),   lambda_max Hess atil(0) = 8 (c + s(0)).
Proof. atil = (4 ubar.X - c) e with e = (1 + 4|X|^2)^(-1). Hess(-c e)(0) = 8 c I. Since ubar.X and grad e vanish at
0, Hess((ubar.X) e)(0) = Hess(ubar.X)(0) = D ubar(0) + D ubar(0)^T = 2 S(0). QED.
So the principal constant (1/2)(1 + q^2) sup lambda_max(Hess a)_+ of the HF-1 inequality (AT-428) is at least
4 (1 + q^2)(c + s(0)) for every coefficient equal to atil near 0. At s(0) = c - 1 this is 4 (1 + q^2)(2c - 1) = 56.71,
against 4 (1 + q^2) c = 39.18 for the weight-only model of the 05:35Z to 05:43Z entries (ubar = 0). The trace,
16 c, is unchanged (Lemma M2-LB). The HF-1 model prices of those entries are therefore low: at fixed slack, mu^2
scales by the factor (2c - 1)/c = 1.448 in the principal term (HEURISTIC; section 6).

## 4. (not used in this version)

## 5. FLOAT evaluation for the complete 009 coefficient

Nothing in this section is a bound. The far constants are FLOAT values of the provable forms of Lemmas TII-1 and
CAW-F, computed from FFT moments of a sampled and windowed far part. The near prices are values of the HF-1 model
(HEURISTIC), set against the first theory agent's Arb budgets at stipulated inputs. Together they answer the coordinator 06:36Z item 3(c),
07:16Z item 3 and 07:37Z item 3(c) in FLOAT. Section 6 lists what would turn them into statements with certificates.

Sampled rates and scanned radii. Every statement "at every rate" or "for every rho" in this note refers to finite
sampled sets, and nothing is claimed between their points.
- Rates: the sampled rates b0 of the first theory agent's budget tables. P/D and P/U at fixed rate use b0 = 0.60, 0.65 and 0.70
  (budget_009n, budnec_009n). The minima over rates in Tables F8 to F10 and in 5.4 use the sampled rates
  b0 = 0.30, 0.35, ..., 0.70 of budnec_tii0 at which U is finite. The rate scan of 5.4 shows b0 = 0.25 to 0.70.
- Radii: the scanned radii rho of the far scan. They are log 4: 2 to 20 (10 radii); log 8: 1 to 16 (13); log 16:
  0.5 to 8 (9); log 32 and log 64: 0.5 to 3 (8 each); lin 1.5: 5.33 to 21.3 (6); lin 2: 4 to 24 (8); lin 3: 2.67 to
  10.7 (6); lin 4: 2 to 12 (8). Table F1 shows a selection; the full lists are in the run files. The thresholds
  rho_G, rho_U and rho_D are log-log interpolations between scanned radii, not computed values (Table F4 also gives
  the first scanned radius with A_a <= G).

### 5.1 Method

- Coefficient. atil of the complete C2-N1-009 coefficient is the unchanged Candidate 007 background plus the b14s
  correction.
  - Background: the cosine modes cos(2 k theta), k < 8, of the agent's polar grid tables of the 007 source (r < 0.5 and
    0.5 <= r <= 2000), interpolated by cubic splines in log r.
  - Correction: datil = 4 v.X/(1 + 4|X|^2) with v = (-phi_xy, phi_xx) (the snapshot definition), evaluated in closed form
    in binary64 from a copy of the snapshot file phi_007_b14s_phi_exact.json of C2-N1-009 (SHA256 prefix a04eb34f).
  - Check: on a finer polar grid (0.02 <= r <= 1e4, 4000 radii, 512 angles on the quarter plane) sup |Delta phi| is
    5.8826e-3 at r = 3.86, against the snapshot mesh value 5.8478e-3.
  - The correction changes every far quantity by less than 0.1 percent (Table F3), and SC(a_f) by 0.05 percent. So
    the band-limited runs of 5.6, which use the 007 background, describe 009 to that accuracy.
- Cut. chi = Sinf(log(r/rho)/log lam) (log cut) or chi = Sinf((r/rho - 1)/(lam - 1)) (lin cut), where
  Sinf(t) = e^(-1/t)/(e^(-1/t) + e^(-1/(1 - t))) for 0 < t < 1, Sinf = 0 for t <= 0 and Sinf = 1 for t >= 1. Then
  a_f = chi atil vanishes on r <= rho and equals atil on r >= R_out := lam rho, and a_n = (1 - chi) atil. Both are
  products of atil with a radial function, so both are even in each coordinate, and Lemma SC-LB applies to a_f.
- Far box.
  - a_f is multiplied by the window 1 - Sinf((r - Rw)/Ww) with Rw = min(max(50, 6 lam rho), 1500) and Ww = Rw/5. It is
    sampled on the square of side 2.2 (Rw + Ww) with 2048^2 points. The window ends at 1.2 Rw <= 1800, inside the
    tabulated range r <= 2000.
  - Wi, M2, M_(2,q-1), M2[w_new] and the L^2 norms D0 = ||Delta a_f||, D1 = ||grad Delta a_f||, E = ||Delta^2 a_f||
    and B = ||grad Delta^2 a_f|| are computed by FFT and Parseval.
  - osc(a_f) is max - min over the samples. SC(a_f) and SC_II(a_f) are maxima of the spectral Hessian on r <= Rw.
  - The window and the truncation at Rw are not controlled.
  - Resolution. The far spacing is h = 2.2 (Rw + Ww)/2048. Table F3b compares N 2048 with N 4096. The change in A_a
    is 0.2 percent at h/rho = 0.06 (log 8, rho 3), 0.3 to 0.7 percent at h/rho = 0.12 (log 16, rho 2 and 4), 1.3 to
    8.9 percent at h/rho = 0.25 (log 32, rho 3 down to 0.5) and 2.5 to 18 percent at h/rho = 0.5 (log 64, rho 3 down
    to 0.5). The values increase under refinement. SC(a_f) changes by at most 5 percent except at log 64, rho 0.5
    (13 percent). The under-resolved rows are those of the wide log cuts lam 32 and 64, whose window radius 6 lam rho
    is large. Their far rows are therefore taken from N 4096 runs (h/rho = 0.12 for lam 32 and 0.25 for lam 64) in
    all tables below, as marked in Table F1. At the same rho the change for lam 64 at h/rho = 0.5 is about twice
    that for lam 32 at h/rho = 0.25, which suggests an error of first order in h (the two families differ in lam, so
    this is only an indication). If so, the N 4096 values of A_a are still low by about the N 2048 to N 4096 change
    at that row: 1.3 to 4.7 percent for lam 32 and 2.5 to 8.5 percent for lam 64 at rho 1 to 3. The lam 32 and 64
    entries are therefore optimistic. The best family, log 16, is resolved to 0.7 percent.
- Far constants per row.
  - A_TII1 := min over nu of A_nu(a_f) (Lemma TII-1 with the FFT value of M2).
  - A_a := A_TII1 + (q^2/2) M2[w_new](a_f) (Lemmas TII-1 and CAW-F). This is the far charge of Proposition FG used
    throughout.
  - A_474 := A_TII1 + (q^2/2) M_(2,q-1)(a_f) (the weight of AT-474). It is weaker, since w_new <= (1 + |zeta|)^(q-1).
  - A_deriv: in TII-1, M2 is replaced by the AT-475 bound ((2 D0 E + 2 D1^2)/(4 pi))^(1/2), and the C_aw moment by
    the AT-482 bound for M_(2,11/10). That bound is inequality (15) of AT-482 with jump term J4 = 0 (the cut is
    smooth), with inputs the AT-475 value of M2, E and B, and with its free parameters optimized. This is the route
    that needs only derivative energies of the complete source with a smooth cutoff (AT-478, AT-481, AT-482).
- Near box.
  - a_n is sampled on the square of side 2.5 lam rho with spacing 0.03 (at most 4096 points per side).
  - Computed: sup((a_n)_- W^2), sup((a_n)_+ W^2), ||(a_n)_+||_1, M2(a_n), M4(a_n) and
    Lambda_+(a_n) = sup lambda_max Hess a_n.
  - The sampled Lambda_+(a_n) is 20.86 to 20.95 for every split. This is the grid value of the origin Hessian. Remark
    HP gives lambda_max Hess atil(0) = 8 (2c - 1) = 20.97, a lower for Lambda_+(a_n) that every sampled value misses
    (AT-576). The model therefore uses max(sampled value, 8 (2c - 1)).
  - M4(a_n) depends on the spacing. It is 5005 to 5478 at spacing 0.03, and 1855 to 2954 at spacings 0.039 to 0.117
    (boxes with 2.5 lam rho > 122.9). It also grows under refinement below 0.03, because the near field is a spline
    in log r of sampled modes.
  - So rows with spacing > 0.0305 use M4REF = 5011.6, the median over the rows at spacing 0.03 (the theory auditor found the
    same median, AT-575). 5.4 gives the sensitivity to M4.
- Near price. code/hf1_near2.py applies the HF-1 model of research/h4/hf1_model2.py with a_n in place of atil_c.
  - mu solves K/mu^2 + A4/mu^4 + tail(mu) = cap - b0, with K = (1/2)(1 + q^2) max(Lambda_+(a_n), 8 (2c - 1)),
    A4 = (pi^2 (1 + c_aw/2) + C_D/2) M4(a_n) and the three-zone tail of atil_c. Then
        P_A = 2 sup((a_n)_- W^2) kappa_q^2 + 2 sup(|a_n| W^2) kappa_0 kappa_(2q),   P_B = P_A + 4 sup((a_n)_+ W^2) kappa_q^2,
    with kappa^Psi log-log interpolated from the agent's FLOAT table (research/h4/kappa_ims_tab.out).
  - mu depends on the split only through Lambda_+(a_n) and M4(a_n), which hardly vary between splits. mu is 40.7 to
    41.4 at b0 = 0.55, 44.8 to 45.5 at 0.60, 53.0 to 54.0 at 0.65 and 94.4 to 95.6 at 0.70. So, to that accuracy, the
    price of a split is fixed by its two sups.
  - P_A is the smaller variant. It is the one compared below.
- Budgets. These are copies of the first theory agent's Arb outputs (note 35), at stipulated inputs ||F||_2 = 2.76e-6 and N = 0.022 or
  0.0141. They are CLAIMED by the first theory agent, with audit requested.
  - D is the Theorem CE-G lower at beta0 = 209/100. At b0 = 0.60, 0.65 and 0.70 it is 1.44e10, 1.94e10 and 2.52e10 at
    N 0.022, and 1.62e10, 2.13e10 and 2.74e10 at N 0.0141.
  - U(b0) is the necessary upper at beta0 = c + 1 (budnec_tii0), for b0 = 0.25 to 0.70 in steps of 0.05; at N 0.022,
    b0 = 0.25 has no passing C0.
  - A construction price above U(b0) at every b0 of the range means that construction cannot close at any rate of the
    range (C_constr >= P > U; AT-552 wording). A price at or below D is on the sufficient side.

### 5.2 Far constants of the complete 009 coefficient

Table F1 (FLOAT; far box N 2048, or N 4096 where marked; a selection, all rows in the run files)

| cut | rho | osc(a_f) | M2 | M2[w_new] | M_(2,1.1) | A_TII1 (nu) | A_a | A_474 | M_(2,1.1) by AT-482 | A_deriv | SC(a_f) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| log 8 | 1 | 0.805 | 2.03 | 5.25 | 19.5 | 7.78 (1.75) | 19.4 | 50.7 | 61 | 144 | 0.968 |
| log 8 | 1.5 | 0.680 | 0.806 | 1.56 | 5.26 | 3.85 (1.40) | 7.28 | 15.4 | 15.6 | 39 | 0.448 |
| log 8 | 2 | 0.599 | 0.418 | 0.68 | 2.11 | 2.43 (1.20) | 3.93 | 7.08 | 6 | 16 | 0.243 |
| log 8 | 2.5 | 0.540 | 0.249 | 0.363 | 1.04 | 1.74 (1.06) | 2.54 | 4.04 | 2.85 | 8.26 | 0.148 |
| log 8 | 3 (N 4096) | 0.496 | 0.163 | 0.22 | 0.592 | 1.35 (0.95) | 1.83 | 2.65 | 1.56 | 4.94 | 0.099 |
| log 8 | 3.5 | 0.461 | 0.113 | 0.144 | 0.364 | 1.1 (0.87) | 1.41 | 1.9 | 0.932 | 3.27 | 0.0686 |
| log 8 | 4 | 0.432 | 0.0824 | 0.101 | 0.241 | 0.927 (0.80) | 1.15 | 1.46 | 0.599 | 2.34 | 0.0502 |
| log 8 | 5 | 0.388 | 0.0484 | 0.056 | 0.121 | 0.714 (0.70) | 0.837 | 0.981 | 0.288 | 1.41 | 0.0298 |
| log 8 | 6 | 0.355 | 0.0313 | 0.0349 | 0.07 | 0.587 (0.63) | 0.664 | 0.741 | 0.159 | 0.978 | 0.0193 |
| log 8 | 8 | 0.308 | 0.0157 | 0.0168 | 0.0299 | 0.444 (0.52) | 0.481 | 0.51 | 0.0631 | 0.607 | 0.00971 |
| log 8 | 16 | 0.219 | 0.00294 | 0.003 | 0.0042 | 0.257 (0.34) | 0.264 | 0.266 | 0.00753 | 0.28 | 0.0018 |
| log 16 | 1 | 0.646 | 0.797 | 1.59 | 5.45 | 3.75 (1.42) | 7.27 | 15.8 | 16.7 | 41.3 | 0.419 |
| log 16 | 2 (N 4096) | 0.470 | 0.166 | 0.231 | 0.636 | 1.32 (0.97) | 1.83 | 2.72 | 1.69 | 5.21 | 0.1 |
| log 16 | 3 | 0.387 | 0.0645 | 0.0772 | 0.179 | 0.788 (0.77) | 0.958 | 1.18 | 0.445 | 1.84 | 0.0399 |
| log 16 | 4 (N 4096) | 0.336 | 0.033 | 0.0373 | 0.0772 | 0.573 (0.65) | 0.655 | 0.743 | 0.176 | 1 | 0.0204 |
| log 16 | 6 | 0.275 | 0.0126 | 0.0133 | 0.0231 | 0.388 (0.51) | 0.417 | 0.439 | 0.0483 | 0.514 | 0.00775 |
| log 32 | 1 (N 4096) | 0.516 | 0.375 | 0.641 | 2.04 | 2.14 (1.21) | 3.55 | 6.64 | 5.89 | 15.5 | 0.21 |
| log 32 | 1.5 (N 4096) | 0.426 | 0.15 | 0.209 | 0.577 | 1.2 (0.97) | 1.66 | 2.47 | 1.55 | 4.77 | 0.0879 |
| log 32 | 2 (N 4096) | 0.370 | 0.0779 | 0.0977 | 0.24 | 0.826 (0.83) | 1.04 | 1.36 | 0.608 | 2.25 | 0.0465 |
| log 32 | 3 (N 4096) | 0.303 | 0.0306 | 0.0346 | 0.0717 | 0.521 (0.65) | 0.598 | 0.679 | 0.164 | 0.923 | 0.0184 |
| log 64 | 0.5 (N 4096) | 0.569 | 0.953 | 2.25 | 8.12 | 4.08 (1.55) | 9.03 | 22 | 25.5 | 61.2 | 0.436 |
| log 64 | 1 (N 4096) | 0.412 | 0.193 | 0.284 | 0.822 | 1.34 (1.06) | 1.96 | 3.15 | 2.35 | 6.73 | 0.111 |
| log 64 | 1.5 (N 4096) | 0.338 | 0.0776 | 0.0971 | 0.24 | 0.782 (0.85) | 0.996 | 1.31 | 0.629 | 2.26 | 0.0462 |
| log 64 | 2 (N 4096) | 0.294 | 0.0403 | 0.0467 | 0.102 | 0.558 (0.72) | 0.661 | 0.783 | 0.25 | 1.16 | 0.024 |
| log 64 | 3 (N 4096) | 0.240 | 0.0159 | 0.0171 | 0.0316 | 0.368 (0.57) | 0.406 | 0.438 | 0.0694 | 0.544 | 0.00929 |
| log 4 | 2 | 0.758 | 1.43 | 3.1 | 11 | 5.9 (1.61) | 12.7 | 30.1 | 33.1 | 80 | 0.756 |
| log 4 | 4 | 0.558 | 0.28 | 0.406 | 1.17 | 1.88 (1.09) | 2.77 | 4.46 | 3.2 | 9.18 | 0.164 |
| log 4 | 6 (N 4096) | 0.461 | 0.105 | 0.131 | 0.322 | 1.06 (0.85) | 1.35 | 1.77 | 0.816 | 2.97 | 0.0636 |
| log 4 | 12 | 0.328 | 0.0193 | 0.0208 | 0.0382 | 0.49 (0.55) | 0.535 | 0.574 | 0.083 | 0.702 | 0.0121 |
| lin 4 | 2 | 0.724 | 0.595 | 0.842 | 2.39 | 3.24 (1.26) | 5.09 | 8.51 | 7.04 | 19.4 | 0.303 |
| lin 4 | 4 | 0.530 | 0.114 | 0.129 | 0.276 | 1.19 (0.83) | 1.48 | 1.8 | 0.696 | 2.87 | 0.0614 |
| lin 4 | 8 | 0.380 | 0.0211 | 0.022 | 0.0355 | 0.559 (0.54) | 0.607 | 0.637 | 0.0746 | 0.758 | 0.0117 |
| lin 2 | 4 | 0.709 | 1.42 | 2.58 | 8.57 | 5.79 (1.64) | 11.5 | 24.7 | 27.9 | 68.7 | 0.631 |
| lin 2 | 10 | 0.466 | 0.149 | 0.18 | 0.429 | 1.25 (0.94) | 1.65 | 2.2 | 1.2 | 4.09 | 0.0732 |
| lin 2 | 20 | 0.332 | 0.0265 | 0.0282 | 0.0504 | 0.534 (0.61) | 0.596 | 0.645 | 0.119 | 0.846 | 0.0136 |
| lin 3 | 4 | 0.601 | 0.283 | 0.362 | 0.93 | 1.95 (1.06) | 2.75 | 4.01 | 2.63 | 8.07 | 0.148 |
| lin 3 | 8 | 0.433 | 0.0519 | 0.0566 | 0.108 | 0.786 (0.69) | 0.911 | 1.03 | 0.261 | 1.44 | 0.0285 |

Table F3 (FLOAT; 009 against the 007 background, far box N 2048)

| check | cut | rho | osc | M2 | M2[w_new] | A_a | A_474 | A_deriv | SC | sup((a_n)_- W^2) | sup((a_n)_+ W^2) |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 007 background | log 8 | 1 | 0.8051 | 2.029 | 5.254 | 19.36 | 50.7 | 144 | 0.9677 | 8.7 | 8.52 |
| 009 | log 8 | 1 | 0.8051 | 2.03 | 5.254 | 19.36 | 50.71 | 144 | 0.9682 | 8.7 | 8.53 |
| 007 background | log 8 | 3 | 0.4962 | 0.1627 | 0.2193 | 1.828 | 2.642 | 4.935 | 0.09794 | 40.4 | 58.8 |
| 009 | log 8 | 3 | 0.4962 | 0.1627 | 0.2193 | 1.828 | 2.642 | 4.936 | 0.09795 | 40.4 | 58.8 |

Table F3b (FLOAT resolution checks of the far box, N 2048 -> N 4096; the near box does not depend on N)

| cut | rho | M2 | M2[w_new] | A_a | A_474 | A_deriv | SC(a_f) | far spacing h at N 2048 |
|---|---:|---|---|---|---|---|---|---:|
| log 16 | 2.0 | 0.1651 -> 0.1659 | 0.2262 -> 0.2307 | 1.816 -> 1.829 | 2.678 -> 2.722 | 5.19 -> 5.215 | 0.09999 -> 0.1 | 0.248 |
| log 16 | 4.0 | 0.03285 -> 0.033 | 0.03687 -> 0.03732 | 0.6536 -> 0.6554 | 0.7385 -> 0.7432 | 1.001 -> 1.003 | 0.02035 -> 0.02035 | 0.495 |
| log 32 | 0.5 | 1.854 -> 1.908 | 5.041 -> 5.704 | 18.14 -> 19.76 | 48.74 -> 55.17 | 146.4 -> 156.5 | 0.7589 -> 0.7662 | 0.124 |
| log 32 | 0.75 | 0.7022 -> 0.7213 | 1.35 -> 1.498 | 6.318 -> 6.704 | 13.41 -> 14.84 | 36.01 -> 38.39 | 0.3594 -> 0.3667 | 0.186 |
| log 32 | 1.0 | 0.365 -> 0.3748 | 0.5844 -> 0.6406 | 3.397 -> 3.555 | 6.086 -> 6.635 | 14.58 -> 15.49 | 0.1999 -> 0.2098 | 0.248 |
| log 32 | 1.25 | 0.2208 -> 0.2267 | 0.3159 -> 0.3431 | 2.215 -> 2.296 | 3.505 -> 3.772 | 7.544 -> 7.981 | 0.1287 -> 0.1311 | 0.309 |
| log 32 | 1.5 | 0.1463 -> 0.1501 | 0.194 -> 0.2091 | 1.608 -> 1.656 | 2.318 -> 2.467 | 4.529 -> 4.77 | 0.0878 -> 0.08789 | 0.371 |
| log 32 | 2.0 | 0.07596 -> 0.07795 | 0.09173 -> 0.09771 | 1.019 -> 1.041 | 1.295 -> 1.355 | 2.157 -> 2.251 | 0.04672 -> 0.04648 | 0.495 |
| log 32 | 2.5 | 0.04547 -> 0.04664 | 0.052 -> 0.05494 | 0.7446 -> 0.7566 | 0.8766 -> 0.9067 | 1.296 -> 1.342 | 0.02816 -> 0.02801 | 0.619 |
| log 32 | 3.0 | 0.02981 -> 0.03057 | 0.03294 -> 0.03459 | 0.5902 -> 0.5977 | 0.6621 -> 0.6794 | 0.8975 -> 0.9229 | 0.01847 -> 0.01838 | 0.743 |
| log 4 | 6.0 | 0.1053 -> 0.1053 | 0.131 -> 0.1311 | 1.352 -> 1.352 | 1.772 -> 1.773 | 2.974 -> 2.974 | 0.06356 -> 0.06356 | 0.186 |
| log 64 | 0.5 | 0.871 -> 0.9527 | 1.728 -> 2.247 | 7.638 -> 9.031 | 16.93 -> 21.97 | 50.32 -> 61.17 | 0.387 -> 0.4358 | 0.248 |
| log 64 | 0.75 | 0.3417 -> 0.3697 | 0.5189 -> 0.6379 | 3.101 -> 3.458 | 5.395 -> 6.558 | 13.52 -> 15.93 | 0.1966 -> 0.1968 | 0.371 |
| log 64 | 1.0 | 0.1791 -> 0.1933 | 0.2379 -> 0.284 | 1.809 -> 1.963 | 2.696 -> 3.15 | 5.81 -> 6.726 | 0.1119 -> 0.1113 | 0.495 |
| log 64 | 1.25 | 0.1086 -> 0.1171 | 0.1335 -> 0.1562 | 1.247 -> 1.331 | 1.676 -> 1.901 | 3.171 -> 3.616 | 0.06982 -> 0.06916 | 0.619 |
| log 64 | 1.5 | 0.07203 -> 0.07759 | 0.08428 -> 0.09709 | 0.9438 -> 0.9957 | 1.181 -> 1.31 | 2.007 -> 2.255 | 0.04676 -> 0.04622 | 0.743 |
| log 64 | 2.0 | 0.03748 -> 0.04033 | 0.04137 -> 0.0467 | 0.6353 -> 0.6607 | 0.7281 -> 0.7829 | 1.058 -> 1.157 | 0.02435 -> 0.02401 | 0.99 |
| log 64 | 2.5 | 0.02249 -> 0.02418 | 0.02405 -> 0.02679 | 0.4839 -> 0.4989 | 0.5285 -> 0.5574 | 0.6933 -> 0.7427 | 0.0145 -> 0.01428 | 1.24 |
| log 64 | 3.0 | 0.01479 -> 0.01588 | 0.01552 -> 0.01713 | 0.3958 -> 0.4057 | 0.4203 -> 0.4376 | 0.5155 -> 0.5436 | 0.009441 -> 0.009287 | 1.49 |
| log 8 | 3.0 | 0.1627 -> 0.1628 | 0.2193 -> 0.2202 | 1.828 -> 1.831 | 2.642 -> 2.651 | 4.936 -> 4.937 | 0.09795 -> 0.09899 | 0.186 |

Readings (FLOAT).
- Along each family osc(a_f) falls like rho^(-gamma) and M2(a_f) like rho^(-gamma-2), as the asymptotic homogeneity of
  atil of degree -gamma predicts (gamma = 1 - 1/c = 0.448). For log 8 between rho 8 and 16 the fitted exponents are
  0.49 and 2.42.
- At the thresholds of 5.3 the low block osc(a_f)(1 + nu^2) of Lemma TII-1 dominates A_a. For log 8 at rho 3,
  A_TII1 = 1.35 (nu 0.95, N 4096 row of Table F1) of A_a = 1.83, and osc(a_f)(1 + nu^2) = 0.94 of that.
- M_(2,1.1)/M2[w_new] is 3.7 at rho 1 and 1.4 at rho 16 (log 8). The AT-482 bound exceeds the FFT value of M_(2,1.1)
  by a factor 3.1 at rho 1, 2.6 at rho 3 and 1.8 at rho 16. So the derivative route multiplies the far charge by 1.3
  to 3.4 at the thresholds of Table F4: 1.5 to 3 for log 4 to 16 (log 16: 2.85 at rho 2, 1.5 at rho 4), up to 3.4 for
  log 32 and 64 near rho 1 (log 64, rho 1: 6.73 against 1.96), and about 1.3 for lin 4 near rho 7.5.
- At fixed rho a wider cut (larger lam) gives a smaller osc(a_f), M2 and A_a, because a_f is then small where atil is
  large. But it has a larger R_out, and so larger near sups (5.4).

### 5.3 Smallest split radius at which the far charge fits

Table F4 (FLOAT). rho_G is the smallest rho with A_a <= G, log-log interpolated between scanned rows; the first
scanned rho with A_a <= G is in brackets, and "> 21.3" means that no scanned row fits. The log 32 and 64 rows use
the N 4096 far rows (optimistic by a few percent, 5.1). For a certified gain G the strain target is sbar = c - G/q:
sbar = 3/2, 1.334, 1.096, 1, 0.858 and c - 1 for the six columns. G = q is the ceiling (sbar = s(0) = c - 1, the
FLOAT value of s_*).

| cut | G = Gbar = 0.6517 | G = 1.0 | G = 1.5 | G = q (c - 1) = 1.7017 | G = 2.0 | G = q = 2.1 |
|---|---:|---:|---:|---:|---:|---:|
| log 4 | 10.1 [12] | 7.35 [8] | 5.64 [6] | 5.23 [6] | 4.77 [5] | 4.65 [5] |
| log 8 | 6.1 [8] | 4.41 [5] | 3.38 [3.5] | 3.13 [3.5] | 2.86 [3] | 2.78 [3] |
| log 16 | 4.02 [6] | 2.92 [3] | 2.25 [2.5] | 2.09 [2.5] | 1.9 [2] | 1.85 [2] |
| log 32 | 2.81 [3] | 2.06 [2.5] | 1.6 [2] | 1.48 [1.5] | 1.35 [1.5] | 1.31 [1.5] |
| log 64 | 2.02 [2.5] | 1.5 [1.5] | 1.17 [1.25] | 1.09 [1.25] | 0.991 [1] | 0.966 [1] |
| lin 1.5 | > 21.3 | > 21.3 | 19.8 [21.3] | 18.5 [21.3] | 17 [21.3] | 16.6 [21.3] |
| lin 2 | 18.7 [20] | 13.7 [16] | 10.6 [12] | 9.82 [10] | 9 [10] | 8.76 [10] |
| lin 3 | 10.5 [10.7] | 7.48 [8] | 5.7 [6.67] | 5.26 [5.33] | 4.8 [5.33] | 4.67 [5.33] |
| lin 4 | 7.52 [8] | 5.26 [6] | 3.96 [4] | 3.67 [4] | 3.32 [4] | 3.23 [4] |

The weaker forms, interpolated rho_G at G = Gbar / 1.0 / 1.5 / 2.0 / q ("> 3" = no scanned row fits):

| cut | A_474 | A_deriv (AT-475 and AT-482) |
|---|---|---|
| log 4 | 10.9 / 8.19 / 6.56 / 5.67 / 5.54 | 12.7 / 9.79 / 8.0 / 7.09 / 6.95 |
| log 8 | 6.62 / 4.95 / 3.94 / 3.42 / 3.34 | 7.66 / 5.93 / 4.86 / 4.28 / 4.19 |
| log 16 | 4.43 / 3.33 / 2.65 / 2.3 / 2.25 | 5.2 / 4.01 / 3.31 / 2.9 / 2.84 |
| log 32 | > 3 / 2.37 / 1.9 / 1.66 / 1.62 | > 3 / 2.89 / 2.38 / 2.1 / 2.06 |
| log 64 | 2.26 / 1.74 / 1.4 / 1.22 / 1.2 | 2.7 / 2.15 / 1.79 / 1.58 / 1.55 |
| lin 4 | 7.86 / 5.7 / 4.44 / 3.8 / 3.71 | 8.97 / 6.76 / 5.39 / 4.7 / 4.59 |

The floor itself: SC(a_f) <= Gbar from rho = 2.14 (log 4), 1.23 (log 8), 0.78 (log 16) and 0.55 (log 32) on, and at
every scanned row of log 64 (rho >= 0.5). SC(a_f) <= 1.0 from rho = 0.61 on for log 16, and at every scanned row of the
other log families. If these FLOAT values of SC(a_f) are accurate, no (FG1) constant fits under G at a smaller
scanned rho (Lemma SC-LB). They are windowed FFT values on partly under-resolved grids (5.1), not certified values.

So, for the coordinator's question in its own terms:
- The combined far charge fits under Gbar from rho = 6.1 (log 8) or 4.0 (log 16) on, and under G = q from rho = 2.8
  (log 8) or 1.85 (log 16) on.
- The derivative route moves rho_G up by a factor 1.2 to 1.6.
- In every family rho_G grows by a factor of 2.1 to 2.3 between G = q and G = Gbar.

### 5.4 Near price at the threshold, and the excess over Gbar

Table F9 (HEURISTIC near price at FLOAT inputs, N 0.022). At the rho where A_a = G (log-log interpolation between
scanned rows), the near input S := sup((a_n)_- W^2) + max(sup((a_n)_- W^2), sup((a_n)_+ W^2)) is shown with the
ratios min over b0 in [0.30, 0.70] of P_A/U(b0), and P_A/D at b0 = 0.60. The minimum over b0 is at b0 = 0.55 in every
row.

| cut | G = Gbar: rho, S, P_A/U, P_A/D | G = 1.0 | G = 1.5 | G = 2.0 | G = q |
|---|---|---|---|---|---|
| lin 1.5 | - | - | 19.8, 800, 24.3, 51.3 | 17, 636, 19.3, 40.7 | 16.6, 612, 18.6, 39.1 |
| lin 2 | 18.7, 851, 25.9, 54.5 | 13.7, 532, 16.1, 34 | 10.6, 359, 10.9, 23 | 9, 280, 8.5, 17.9 | 8.76, 269, 8.15, 17.2 |
| lin 3 | 10.5, 484, 14.7, 31 | 7.48, 288, 8.72, 18.4 | 5.7, 189, 5.72, 12.1 | 4.8, 145, 4.38, 9.22 | 4.67, 139, 4.19, 8.83 |
| lin 4 | 7.52, 383, 11.6, 24.5 | 5.26, 222, 6.73, 14.2 | 3.96, 143, 4.32, 9.11 | 3.32, 109, 3.28, 6.91 | 3.23, 104, 3.13, 6.6 |
| log 4 | 10.1, 423, 12.8, 27 | 7.35, 259, 7.86, 16.6 | 5.64, 172, 5.22, 11 | 4.77, 133, 4.03, 8.48 | 4.65, 128, 3.86, 8.14 |
| log 8 | 6.1, 295, 8.96, 18.9 | 4.41, 180, 5.45, 11.5 | 3.38, 119, 3.61, 7.6 | 2.86, 91.8, 2.77, 5.84 | 2.78, 87.9, 2.65, 5.59 |
| log 16 | 4.02, 260, 7.89, 16.6 | 2.92, 159, 4.82, 10.1 | 2.25, 107, 3.23, 6.81 | 1.9, 82.3, 2.49, 5.25 | 1.85, 79, 2.39, 5.03 |
| log 32 | 2.81, 265, 8.07, 17 | 2.06, 166, 5.02, 10.6 | 1.6, 112, 3.4, 7.15 | 1.35, 86.8, 2.63, 5.53 | 1.31, 83.2, 2.52, 5.3 |
| log 64 | 2.02, 298, 9.06, 19.1 | 1.5, 189, 5.73, 12.1 | 1.17, 129, 3.92, 8.27 | 0.991, 101, 3.05, 6.43 | 0.966, 96.9, 2.94, 6.19 |

At N 0.0141 the P_A/U ratios are 0.87 times these and the P_A/D ratios 0.89 times, and the best family is the same. Log 16 gives min_b0 P_A/U = 6.87, 4.19,
2.81, 2.17 and 2.08, and P_A/D = 14.8, 9.02, 6.05, 4.66 and 4.47 for the five columns (runs/tables4_N0.0141.out).

The interpolated thresholds of Table F9 fall between scanned rows. Over the scanned rows themselves (no interpolation;
code/best_split.py), the best split with A_a <= G and its ratios min_b0 P_A/U (at b0 = 0.55 in every case) and P_A/D
at b0 = 0.60 are, at N 0.022 [N 0.0141]:

| G | best scanned split | A_a | min_b0 P_A/U | P_A/D at b0 0.60 |
|---|---|---:|---:|---:|
| Gbar | log 32, rho 3 | 0.598 | 8.93 [7.78] | 18.8 [16.7] |
| 1.0 | log 16, rho 3 | 0.958 | 5.03 [4.38] | 10.6 [9.43] |
| 1.5 | log 16, rho 2.5 | 1.26 | 3.80 [3.31] | 8.01 [7.12] |
| q (c - 1) | log 32, rho 1.5 | 1.66 | 3.09 [2.69] | 6.51 [5.79] |
| 2.0 and q | log 16, rho 2 | 1.83 | 2.69 [2.34] | 5.67 [5.04] |

The Gbar entry agrees with AT-575 (8.928 and 7.775, computed without the floor on Lambda_+(a_n)).

Readings (HEURISTIC).
- The best family is log 16, with log 32 within 6 percent. At a given far charge, S varies by less than 25 percent
  over log 8 to log 64. The lin cuts and log 4 are worse by factors 1.3 to 3.4, and lin 1.5 by up to 7.8. The shape
  of the cut is not the lever.
- G = Gbar (the target of the coordinator 07:16Z item 3). The far charge fits at rho = 4.0 (log 16), and the near price
  there is 7.89 times U at the best rate (N 0.022; 6.87 at N 0.0141). The best scanned split, log 32 at rho 3, gives
  8.93 times U (7.78 at N 0.0141) and P_A/D = 18.8 at b0 = 0.60.
- G = q (the ceiling, FLOAT s_*). The near price at the threshold is 2.39 times U at the best rate (N 0.022; 2.08 at
  N 0.0141), and P_A/D = 5.03 at b0 = 0.60.
- Rate dependence at the best scanned split for G = q (log 16, rho 2, N 0.022): P_A/U is 80.9, 12.6, 6.19, 4.01,
  3.06, 2.69, 2.81, 4.18 and 34.3 at b0 = 0.30, 0.35, ..., 0.70. At N 0.0141 the range starts at b0 = 0.25 (67.3).
  The minimum is at b0 = 0.55 for every G and both N.
- Sensitivity to M4(a_n) at log 8, rho 8 (the first scanned row with A_a <= Gbar, b0 = 0.60). P_A/D is 16.2, 18.5,
  20.2, 28.6 and 50.9 for M4 = 1854 (= 1024 c, the weight-only value), 2506, 2954 (the sampled value at that row),
  5012 (M4REF) and 1.0e4. The smallest M4 lowers the ratios by a factor 0.57. With that factor the G = q value 2.39
  becomes about 1.35 (this scaling is approximate), still above U.
- The floor on Lambda_+(a_n) changes every ratio of this section by less than 0.5 percent.
- So, in the HF-1 model with the TII-1 + CAW-F far charge, no certified gain G <= q closes. The excess factor over U
  at the best split is at least about 7 at G = Gbar and at least about 2 at G = q.

Table F8 (the excess of the far charge over Gbar when the split is chosen by the near side; N 0.022, N 0.0141 in
brackets). rho_U is the largest rho at which min_b0 P_A/U <= 1 (log-log interpolation), and rho_D the largest rho at
which P_A <= D at some b0 in {0.60, 0.65, 0.70}. A_a is given at those radii.

| cut | rho_U | A_a at rho_U | A_a - Gbar | A_a/Gbar | A_a/q | rho_D | A_a at rho_D |
|---|---:|---:|---:|---:|---:|---:|---:|
| log 4 | < 2 [2.17] | - [10.5] | - [9.87] | - [16.1] | - [5.01] | < 2 | - |
| log 8 | 1.51 [1.64] | 7.23 [6.01] | 6.57 [5.36] | 11.1 [9.22] | 3.44 [2.86] | < 1 [1.01] | - [18.7] |
| log 16 | 1.07 [1.17] | 6.31 [5.25] | 5.65 [4.59] | 9.68 [8.05] | 3.0 [2.5] | 0.64 [0.695] | 24.6 [19.7] |
| log 32 | 0.73 [0.796] | 7.22 [5.87] | 6.57 [5.22] | 11.1 [9.01] | 3.44 [2.8] | < 0.5 | - |
| log 64 | < 0.5 [0.528] | - [7.93] | - [7.28] | - [12.2] | - [3.78] | < 0.5 | - |
| lin 1.5 to 4 | below the scanned range | | | | | | |

So if the split is chosen where the near price is within U, the combined far charge exceeds Gbar by at least 5.65
(N 0.022) or 4.59 (N 0.0141), a factor of 8 to 16, and exceeds q by a factor of 2.5 to 5. If it is chosen within D,
it exceeds Gbar by a factor of about 29 or more. The log 32 and 64 entries at rho < 1 are the least resolved
(5.1; at log 64, rho 0.5 the N 2048 to N 4096 change is 18 percent), and their true A_a is larger.

Table F10 (the floor SC(a_f) of Lemma SC-LB at rho_U and rho_D; N 0.022, N 0.0141 in brackets). Every (FG1) constant
is at least SC(a_f), so G/SC(a_f) is the largest loss factor, relative to the floor, that a far estimate may have at
that split if the far charge is to fit under G there.

| cut | rho_U | SC at rho_U | osc(a_f) at rho_U | A_a/SC | Gbar/SC | q/SC | rho_D | SC at rho_D | Gbar/SC | q/SC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| log 4 | < 2 [2.17] | - [0.632] | - [0.731] | - [16.7] | - [1.03] | - [3.32] | < 2 | - | - | - |
| log 8 | 1.51 [1.64] | 0.445 [0.371] | 0.679 [0.654] | 16.2 [16.2] | 1.46 [1.76] | 4.72 [5.66] | < 1 [1.01] | - [0.944] | - [0.691] | - [2.23] |
| log 16 | 1.07 [1.17] | 0.367 [0.308] | 0.627 [0.603] | 17.2 [17.0] | 1.78 [2.12] | 5.73 [6.82] | 0.64 [0.695] | 0.924 [0.799] | 0.705 [0.816] | 2.27 [2.63] |
| log 32 | 0.73 [0.796] | 0.386 [0.326] | 0.595 [0.572] | 18.7 [18.0] | 1.69 [2.0] | 5.45 [6.43] | < 0.5 | - | - | - |
| log 64 | < 0.5 [0.528] | - [0.391] | - [0.555] | - [20.3] | - [1.67] | - [5.37] | < 0.5 | - | - | - |

Readings (FLOAT, with the HEURISTIC rho_U and rho_D).
- At rho_U, Lemmas TII-1 and CAW-F give 16 to 20 times the floor SC(a_f). A far estimate within a factor of 1.0 to 2.1
  of SC(a_f) (1.46 to 2.12 for log 8 to 64) would fit under Gbar there, and one within a factor of 3.3 to 6.8 under
  q.
- At rho_U, osc(a_f) is 0.55 to 0.73, which is close to Gbar = 0.65 and well below q = 2.1. Every estimate of the
  form of Lemma TII-1 is at least osc(a_f) (the low block). So an estimate of that form would need to lose almost
  nothing over osc(a_f) at G = Gbar, while at G = q it may lose a factor of about 3. Most of A_a at rho_U is the M2
  and C_aw overhead: A_a/osc(a_f) is 9 to 14 there.
- At rho_D, SC(a_f) exceeds Gbar (Gbar/SC = 0.69 to 0.82). So, if these FLOAT values are accurate, no (FG1) constant
  fits under Gbar at a split whose HEURISTIC model near price is within D. Under G = q a factor of 2.2 to 2.6 is left.

### 5.5 Fixed outer radius

Table F6 (lin cuts at fixed R_out = lam rho; HF-1 model price at b0 = 0.60, N 0.022)

| R_out | lam | rho | osc(a_f) | A_a | SC | sup((a_n)_- W^2) | sup((a_n)_+ W^2) | P_A/D |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 2 | 4 | 0.709 | 11.5 | 0.631 | 34.3 | 44.8 | 5.03 |
| 8 | 4 | 2 | 0.724 | 5.09 | 0.303 | 21.9 | 26.8 | 3.09 |
| 12 | 1.5 | 8 | 0.585 | 11 | 0.522 | 79.9 | 121 | 12.8 |
| 12 | 2 | 6 | 0.592 | 4.48 | 0.246 | 60.9 | 88.7 | 9.52 |
| 12 | 3 | 4 | 0.601 | 2.75 | 0.148 | 45.3 | 63.7 | 6.93 |
| 12 | 4 | 3 | 0.605 | 2.37 | 0.12 | 38.8 | 53.8 | 5.88 |
| 16 | 2 | 8 | 0.518 | 2.48 | 0.125 | 91.7 | 142 | 14.9 |
| 16 | 4 | 4 | 0.530 | 1.48 | 0.0614 | 58.4 | 86.8 | 9.25 |
| 20 | 2 | 10 | 0.466 | 1.65 | 0.0732 | 126 | 204 | 21.1 |
| 20 | 4 | 5 | 0.477 | 1.07 | 0.0362 | 80.2 | 125 | 13.1 |
| 24 | 1.5 | 16 | 0.421 | 2.24 | 0.099 | 214 | 367 | 37.1 |
| 24 | 2 | 12 | 0.427 | 1.21 | 0.0472 | 163 | 272 | 27.8 |
| 24 | 3 | 8 | 0.433 | 0.911 | 0.0285 | 121 | 198 | 20.4 |
| 24 | 4 | 6 | 0.437 | 0.843 | 0.0234 | 104 | 167 | 17.3 |
| 32 | 2 | 16 | 0.371 | 0.793 | 0.0235 | 245 | 429 | 43.2 |
| 32 | 4 | 8 | 0.380 | 0.607 | 0.0117 | 156 | 265 | 27 |

At fixed R_out, osc(a_f) is nearly constant, and a wider cut (larger lam, smaller rho) lowers both A_a, through M2,
and the near sups. The near sups are not a function of R_out alone: they are set where (1 - chi) |atil| W^2 is
largest, and for a wide cut that is well inside R_out. This is why the wide log cuts of Table F9 do best.

### 5.6 How lossy the far lemmas are

Table F7 (FLOAT values of lowers of the optimal (FG1) constant A_f* := sup over tests of (Q + C_aw)[a_f](g)/||J^(-1) g||^2,
against A_a). SC(a_f) is the floor of Lemma SC-LB. A_II+aw(kmax) is the best constant over S1 tests with Fourier
support in |xi_i| <= kmax (Lanczos, code/far_box.py, box side 128, 007 background). It is a periodic collocation
eigenvalue, which becomes a lower bound for A_f* only with controlled periodization, interpolation and aliasing
errors (AT-554). A_II is the same for Q alone. SC(a_f) is a lower bound by Lemma SC-LB, evaluated in FLOAT.

| cut | rho | SC(a_f) | A_II+aw, kmax 2 pi | 4 pi | 8 pi | A_II, 2 pi | osc(a_f) | A_a | A_a/max(lowers) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| log 16 | 0.25 | - | 1.85 | - | - | 0.644 | 1.090 | - | - |
| log 16 | 0.35 | - | 1.03 | - | - | 0.427 | 0.978 | - | - |
| log 16 | 0.5 | 1.43 | 0.524 | - | - | 0.311 | 0.860 | 48.5 | 33.8 |
| log 16 | 0.75 | - | 0.255 | - | - | 0.239 | 0.731 | - | - |
| log 16 | 1 | 0.419 | 0.203 | - | - | 0.201 | 0.646 | 7.27 | 17.3 |
| log 8 | 0.5 | - | 1.17 | - | - | 0.454 | 1.030 | - | - |
| log 8 | 0.75 | - | 0.501 | - | - | 0.314 | 0.898 | - | - |
| log 8 | 1 | 0.968 | 0.31 | 0.532 | - | 0.258 | 0.805 | 19.4 | 20 |
| log 8 | 1.5 | 0.448 | 0.204 | - | - | 0.202 | 0.680 | 7.28 | 16.2 |
| log 8 | 2 | 0.243 | 0.171 | 0.173 | - | 0.17 | 0.599 | 3.93 | 16.1 |
| log 8 | 3 | 0.0979 | 0.133 | - | - | 0.133 | 0.496 | 1.83 | 13.8 |
| log 4 | 0.5 | - | 3.49 | - | - | 0.943 | 1.215 | - | - |
| log 4 | 0.75 | - | 1.47 | - | - | 0.506 | 1.072 | - | - |
| log 4 | 1 | - | 0.751 | 1.25 | - | 0.366 | 0.982 | - | - |
| log 4 | 1.5 | - | 0.428 | - | - | 0.265 | 0.850 | - | - |
| log 4 | 2 | 0.756 | 0.309 | 0.485 | - | 0.22 | 0.758 | 12.7 | 16.8 |
| log 4 | 3 | 0.315 | 0.172 | - | - | 0.172 | 0.636 | 5.01 | 15.9 |
| log 4 | 4 | 0.164 | 0.144 | - | - | 0.144 | 0.558 | 2.77 | 16.9 |
| log 4 | 6 | 0.0636 | 0.11 | - | - | 0.11 | 0.461 | 1.35 | 12.3 |

Readings (FLOAT).
- A_a exceeds the larger of the two FLOAT values by a factor 12 to 34 at every computed row. To the extent that the
  FLOAT values are lowers, A_f* lies in [max(lowers), A_a]. Where it lies is not known. The band-limited value grows
  with kmax (log 4 at rho 1: 0.75 at 2 pi, 1.25 at 4 pi; log 8 at rho 1: 0.31 and 0.53), and SC(a_f) is its
  high-frequency limit.
- At low band the Q part dominates at the larger radii: at 2 pi, A_II+aw agrees with A_II to within 1 percent for
  rho >= 1 (log 16), rho >= 1.5 (log 8) and rho >= 3 (log 4). There A_II is 0.24 to 0.31 times osc(a_f), against
  the factor 1 + nu^2 >= 1 of the TII-1 low block.
- The 8 pi column is empty. The N 2048 run for log 8 at rho 1 was stopped by hand at 08:18Z because its memory
  reached 2.78 GB, close to the agent limit of 3 GB (runs/scan11.log).
- Table F10 makes the same comparison at the near-side radii. At rho_U, A_a is 16 to 20 times SC(a_f). To fit under
  Gbar there, a far constant must be within a factor of 1.0 to 2.1 of SC(a_f); to fit under q, within 3.3 to 6.8.
  Whether such a constant exists depends on where A_f* lies in [max(lowers), A_a], which is not known. It would come
  from a far estimate of a different kind from Lemma TII-1, whose low block alone is osc(a_f), about Gbar, at rho_U.

## 6. What a certified far bound needs, and the tradeoff

### 6.1 Inputs that need certificates

These are the inputs of the route priced in section 5: Lemmas TII-1 and CAW-F for (FG1), the HF-1 inequality (or
Corollary NT) for a_n, a smooth cut with parameters (cut, lam, rho), and the complete 009 coefficient. Each item is an
upper bound unless stated. The FLOAT targets are in Tables F1 and F4.
- (C1) s_* <= sbar < c, globally (the coordinator 06:36Z item 3(a)). G(sbar) = q (c - sbar), so every 0.1 lost in sbar costs
  0.21 in G. Since s(0) = c - 1 exactly, G <= q. In every cut family rho_G grows by a factor of 2.1 to 2.3 from G = q
  to G = Gbar (sbar = 3/2), and the near price at rho_G by a factor of 3.1 to 3.7 (3.3 for log 16; Tables F4 and F9).
- (C2) osc(a_f): two-sided sup bounds of atil on r >= rho, including the far region beyond the certified annuli.
- (C3) M2(a_f) and M2[w_new](a_f). Either directly by a Fourier-side enclosure (not available), or through the L^2
  derivative energies D0 = ||Delta a_f||, D1 = ||grad Delta a_f||, E = ||Delta^2 a_f|| and B = ||grad Delta^2 a_f||
  by AT-475 and AT-482 with J4 = 0. The derivative route multiplies the far charge by 1.3 to 3.4 at the radii of
  Table F4 (1.5 to 3 for log 4 to 16) and moves rho_G up by 19 to 60 percent (A_deriv in Table F4).
- (C4) The cut: bounds for the derivatives of Sinf up to order 5 on [0, 1], which enter (C3). This is routine.
- (C5) The near inputs at the chosen split:
  - sup((a_n)_- W^2) and sup((a_n)_+ W^2) (equivalently, signed sup bounds of atil W^2 on r <= lam rho), and ||(a_n)_+||_1;
  - Lambda_+(a_n) = sup lambda_max Hess a_n. This is at least 8 (2c - 1) = 20.97 by Remark HP, and every sampled value
    lies below that, so a certified upper must come from elsewhere (AT-576);
  - M4(a_n). The sampled value depends on the spacing (5.1); a certified value needs the exact Taylor jets of the source;
  - the tail T_q and kappa^Psi at the chosen mu (N3) for HF-1, or M2(a_n) and the Riesz-band inputs for Corollary NT.
- (C6) The other pieces of D_rem^n (T_IS, C_tr, C_vs) are not priced here. If any of them is charged to the free gain,
  it must fit under G - A_far (AT-513).
- (C7) The budget comparison needs the strong-norm inputs at the right sides: uppers of ||F||_2 and N_q for the
  sufficient D, lowers for the necessary U (the theory auditor 07:33Z). The ratios of section 5 use stipulated values.

### 6.2 The tradeoff

All statements in this subsection are FLOAT or HEURISTIC readings of section 5.
- Far side. Along each family osc(a_f) falls like rho^(-gamma) and M2(a_f) like rho^(-gamma-2). As M2 tends to 0, the
  optimal nu of Lemma TII-1 tends to 0 and A_TII1 tends to osc(a_f). So at large rho the TII-1 + CAW-F charge falls
  only like rho^(-0.45). Near the thresholds of Table F4 it falls like rho^(-1.5) (log 16: A_a = 1.83 at rho 2 and
  0.655 at rho 4).
- Near side. For a fixed cut shape the near input S grows like R_out^(2 - gamma) = R_out^1.55, because |atil| decays
  like r^(-gamma) and W^2 grows like 4 r^2. The model price is linear in S at fixed mu, and mu is fixed by the rate
  slack, since Lambda_+(a_n) and M4(a_n) hardly vary between splits (5.1). In Table F9 (log 16), S grows by a factor 3.3
  from G = q (rho 1.85) to G = Gbar (rho 4.02), against (4.02/1.85)^1.55 = 3.3.
- Combined. Near the thresholds rho_G is proportional to G^(-1/1.5), so S at rho_G is roughly proportional to
  G^(-1.03). The model price at the threshold is therefore roughly inversely proportional to G. With the log 16 values
  of Table F9 (P_A/U = 2.39 at G = q, N 0.022; 2.08 at N 0.0141), the route would need G of about 2.1 q to 2.4 q,
  which exceeds the ceiling q.
  The same conclusion in far-side terms: at the radius rho_U where the near price meets U, the far charge must fall
  from A_a(rho_U) >= 5.25 (Table F8) to G. This needs a far estimate that is sharper than Lemmas TII-1 and CAW-F
  by a factor of at least 2.5 at G = q and at least 8 at G = Gbar.
- How far a sharper estimate could go. Table F10 gives the floor SC(a_f) of Lemma SC-LB at rho_U and rho_D. Every
  (FG1) constant is at least SC(a_f), so G/SC(a_f) at rho_U is the largest loss factor that a far estimate can have at
  that split if the construction is to close in the model. That factor is 1.0 to 2.1 at G = Gbar and 3.3 to 6.8 at
  G = q, while Lemmas TII-1 and CAW-F are 16 to 20 times SC(a_f) there. At rho_D, the FLOAT SC(a_f) exceeds Gbar, so (if
  those values are accurate) no far estimate at all fits under Gbar at a split whose model near price is within D.
  Since osc(a_f) at rho_U is 0.55 to 0.73 (0.85 to 1.12 Gbar), an estimate whose low block costs osc(a_f)(1 + nu^2),
  as in Lemma TII-1, would have to lose almost nothing else to fit under Gbar at rho_U. At G = q it can fit, if the M2 and C_aw overheads (A_a - osc(a_f) = 4.6 to 9.8 at rho_U) are reduced by a factor of 3
  to 5 (log 8 to 64; 7 for log 4).
- Cut shape. At a fixed far charge, S varies by less than 25 percent over the log cuts lam 8 to 64. Lin cuts and the
  narrow log cut lam 4 are worse. At fixed R_out (Table F6), a wider cut lowers both A_a and the near sups. The shape
  of the cut is not the lever.
- So, with the far lemmas of section 2, neither the cut nor the gain (up to its ceiling q) closes the HF-1 route for
  009 in the model. A certified s_* closer to c - 1 reduces the excess at the threshold from about 7.9 U (Gbar) to
  about 2.4 U (G = q) but does not remove it. The open lever is (FG1) itself: a far estimate of a different kind from
  Lemma TII-1, whose constant approaches SC(a_f) at moderate rho (O2, OPEN).

## 7. Errata and corrections

- T2_NELO-E1 (announced 05:53Z; AT-405, AT-406). Corollary PR-0 of T2_NELO_v01 holds under the added hypothesis that
  kappa_q is nondecreasing on [mu_0, infinity). That hypothesis is OPEN; global monotonicity is false (AT-406). The
  monotonicity-free bound P >= 2 c (1 + 32 phi c/(cap - b0))^q of AT-408 can be used in place of PR-0.
- T2_NELO-E2 (announced 05:53Z; AT-406). In the second remark after Proposition TII-0, when a_n <= 0 only the
  Riesz-band inputs (nu, t and kappa_j) drop out. kappa_q remains an N3 input that needs certification.
- Correction to team notes 05:53Z item 2 and the theory_v08 summary of it. The statement "HF-1 is no route for 009
  or 008" assumed that the far part is charged by Lemma OSC. Under Proposition FG it is not, and HF-1 (or TII-0) is
  needed only for the near part a_n. HF-1 is therefore a candidate route for 009 and 008, conditional on a certified
  (FG1), s_* < c, and the near-part inputs. AT-449 (the obstruction persists while the far part is charged by Lemma
  OSC) is unchanged. Section 5 prices this route for 009 in FLOAT: with Lemmas TII-1 and CAW-F for (FG1) and the HF-1
  model for a_n it does not close for any certified gain G <= q (Table F9; HEURISTIC). It stays open for a sharper
  far estimate (section 6.2).
- Correction to the 05:35Z entry: the principal constant 39.2 is the weight-only value; with ubar it is at least
  4 (1 + q^2)(c + s(0)) (Remark HP).
- Corrections to the 07:41Z interim entry (team notes). All are FLOAT or HEURISTIC figures; section 5 supersedes them.
  - Item 1. With the derivative-energy bounds the threshold radii grow by 19 to 60 percent, not 20 to 30 percent. At
    G = Gbar the growth is 19 to 34 percent, close to the interim figure; at G = q it is 42 to 60 percent
    (Table F4).
  - Item 2. With the log cuts lam 32 and 64, which were scanned after the interim entry, the best scanned split for
    G = Gbar is log 32 at rho 3 (A_a = 0.598 with the N 4096 far box; P_A = 18.8 D at b0 = 0.60, N 0.022), not lin 4
    at rho 8 (26.9 D in the interim entry; 27 D with the Lambda_+ floor, Table F6). The minimum of P_A/U over the
    sampled rates is 8.93 (N 0.022) and 7.78 (N 0.0141), at b0 = 0.55 (section 5.4), not 12.8 and 11.1. The theory auditor found the same from the 07:47Z run files (AT-575: 8.928 and 7.775).
    The log 64 split at rho 2 fits under Gbar with the N 2048 far box (A_a = 0.635) but not with N 4096 (0.661).
    The reading of item 2 (no closure at any sampled rate, even at G = q) is unchanged.
  - Item 3. The statement that the split comes near the budget only at about rho = 1, where the far charge must be
    within a factor 2 to 2.2 of the SC floor, was for the log cut lam 8 only. Table F10 replaces it.
  - The near prices of section 5 floor Lambda_+(a_n) at 8 (2c - 1) (AT-576). The interim entry used the sampled values
    20.86 to 20.95, which lie below that lower. The change in the ratios is below 0.5 percent.

## 8. Requests

- The coordinator. For the ledger and the 09:30Z report, the reading of Tables F4, F8 and F9 is as follows (FLOAT far
  constants, HEURISTIC near price, stipulated budgets):
  - The TII-1 + CAW-F far charge of the complete 009 coefficient fits under G from rho_G = 4.0 (Gbar), 2.9 (1.0),
    2.25 (1.5), 1.9 (2.0) and 1.85 (q) on (log 16).
  - The HF-1 model near price at rho_G exceeds U at every sampled rate, for every G <= q.
  - Within the model the gain is therefore not the binding input of this route. The far lemma is.
  - The numerical auditor strain refinement (07:37Z) improves the excess factor at the threshold from about 7.9 to about 2.4, but
    alone it does not close the route. Table F10 shows what the far lemma would have to achieve: within a factor of
    3.3 to 6.8 of SC(a_f) at rho_U for G = q, against 16 to 20 for Lemmas TII-1 and CAW-F. I recommend keeping it, since every route needs (C1), and pairing it with the
    far-lemma work (O2) rather than with further near-side pricing.
- The theory auditor.
  - (1) Section 5 as conditional statements. If certified uppers of s_* and of the far inputs (C2) and (C3) satisfy
    the FLOAT values of Table F1 at a split with A_a <= G, then (FG1) holds there with A_far <= G (Proposition FG
    with Lemmas TII-1 and CAW-F). Separately, the HF-1 model reading that C_constr >= P_A > U at every sampled rate
    (AT-552 wording). Please check that neither is stated more strongly than that.
  - (2) A replay of Tables F4, F8, F9 and F10 and of the best scanned splits of 5.4 (code/best_split.py) from the run
    files, as in AT-574 to AT-576. This version floors Lambda_+ at 8 (2c - 1), uses the N 4096 far rows where they
    were computed (all scanned rows of log 32 and 64), and adds the SC(a_f) entries. The resolution reading of 5.1
    (an error of first order in h, so that the lam 32 and 64 values are still low by a few percent) is a further
    point to check.
  - (3) The scaling reading of 6.2 (near price at the threshold roughly proportional to 1/G).
- The numerical auditor. The certificate list of 6.1, in this order, for the log cut lam 16 at rho between 1.85 and 4 (the Table F4
  range for G between q and Gbar):
  - (C1) s_* <= sbar, with sbar as close to c - 1 as possible;
  - (C2) two-sided sup bounds of atil on r >= rho;
  - (C3) the derivative energies D0, D1, E and B of a_f, if a Fourier-side enclosure of M2 and M2[w_new] is out of reach.
  The FLOAT targets are in Table F1.
- The second numerics agent.
  - An independent FLOAT check of osc(a_f), M2(a_f) and M2[w_new](a_f) for the log cut lam 16 at rho = 2 and 4 by the
    per-mode Hankel route (no box, no window).
  - M4(a_n) near the origin with the exact Taylor jets of the base. The sampled near field gives a spacing-dependent
    M4 (5.1), and the near price moves by a factor 0.57 to 1.8 over the plausible range (5.4).
- The first theory agent. For theory_v09: Proposition FG with G(sbar), Lemma CAW-F (AT-514), Lemma SC-LB (AT-545, AT-553), Corollary SC,
  and Tables F4 and F9 with their labels (FLOAT far constants, HEURISTIC near price, stipulated budgets, AT-552
  wording). Please also carry the corrections of section 7 to the 07:41Z interim figures.

## 9. Files and runs

All paths are relative to the agent directory the second theory agent. Nothing listed here is a certificate.
- Code (research/h4/far009/code/):
  - far_scan.py: far box and near box per split; the FLOAT far constants and near inputs; env CORR=b14s.
  - b14s_corr.py: the b14s correction on the polar grids.
  - check_h.py: the check of sup |Delta phi|.
  - far_box.py: band-limited Lanczos values (007 background).
  - hf1_near2.py: thresholds and HF-1 model prices.
  - make_tables3.py (F6, F7), make_tables4.py (F4, F8, F9, F10; env FARN=4096), make_f1.py (F1 and Table F3b) and
    best_split.py (the best scanned split per G in 5.4).
  - The HF-1 model and the kappa table are research/h4/hf1_model2.py and research/h4/kappa_ims_tab.out.
- Runs (research/h4/far009/runs/):
  - far_scan_<cut>_lam<lam>_b14s_N2048_K8.json for log 4, 8, 16, 32, 64 and lin 1.5, 2, 3, 4;
    far_scan_log_lam<lam>_b14s_N4096_K8.json (resolution checks, and the log 32 and 64 rescans);
  - far_scan_<cut>_lam<lam>_N2048_K8.json (007 background, Table F3);
  - far_box_log_lam<lam>_L128_N<N>_k<kmax>_S1_inf_K8.json (Table F7);
  - hf1_near2_N0.022.out and hf1_near2_N0.0141.out; tables4_N0.022.out and tables4_N0.0141.out (FARN=4096), with
    the N 2048 versions tables4_N*_far2048.out; best_split_N0.022.out and best_split_N0.0141.out; tables_f1.out;
    tables3.out (rerun at 08:18Z with the Lambda_+ floor; the previous version is tables3_0818prev.out);
  - logs scan7b.log to scan11.log (with the scripts scan*.sh), tables11b.log and best11.log. Each log records its
    real start and end times and the runs that were stopped by hand. The table step of scan11.sh failed on an
    ordering error in hf1_near2.py (fixed at 08:11Z) and was rerun by tables11b.sh; its outputs replace the failed
    ones.
- Inputs:
  - research/h4/far009/data/phi_007_b14s_phi_exact.json: a copy of the C2-N1-009 snapshot file, SHA256 prefix
    a04eb34fb51df707. Its reference_sha256 for Candidate 007 begins ed4962328d88fa14.
  - runs/near.json and runs/main.json: the agent's polar grid tables of the 007 source.
  - Copies of the first theory agent's Arb budget outputs (note 35), with SHA256 prefixes:
    - runs/budget_009n_c2t1.out: 53e18d35a291fca1;
    - runs/budnec_009n_c2t1.out: e78f0737e4af4a2a;
    - runs/budnec_tii0_c2t1.out: 8dfdb54915cb4019.
