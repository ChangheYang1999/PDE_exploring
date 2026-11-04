# T2_FAR_v02: Lemma HSB for the complete 009 far piece, its certification inputs, the best model split (erflog 8, rho 0.9 to 1), the OMF split at G = 2, Proposition TS at log 16, rho 1.5, and C2-N1-013 against C2-N1-009 (FLOAT and HEURISTIC)

Agent the second theory agent. This version answers the coordinator's 10:05Z note item 4(c): the best model split with Lemma HSB, the list of
certified inputs in a form the numerical auditor can certify, the erflog 16, rho 1 split with the OMF charge at G = 2 and its
resolution and window checks, the inputs needed to certify Proposition TS at log 16, rho 1.5, Lemma HSB with its
FLOAT evaluation, the OMF baseline row, and the corrections of the second theory agent 09:37Z note item 9. It also completes the
answer to the coordinator's 10:37Z item 3(c) and 10:26Z item 5(a) (C2-N1-013 against C2-N1-009 on the far side; section 6),
and it collects the analytic content of the second theory agent's notes of 09:37Z to 10:57Z. It builds on notes/T2_FAR_v01.md
(setting, Lemma KER', Lemma TII-1, Lemma CAW-F, Lemma SC-LB, the OMF baseline), which stays unchanged.
Labels: CONFIRMED (cited the theory auditor verdict, with its qualifier), CLAIMED (proved here or in a cited note, audit
requested), FLOAT (a floating-point value of a far constant or of an input; never a bound), HEURISTIC (a value of the
HF-1 model near price), OPEN. P-S1 = (21/10, 1, 1/2), q = 21/10, c = 4076476460239181/2251799813685248, and
Gbar = q (c - 3/2) = 0.65167 (FLOAT conversion). Paths code/ and runs/ are research/h4/far009/code/ and
research/h4/far009/runs/ of this agent. All times are real UTC times.

## 0. Summary

1. Analytic far uppers (section 2). Proposition TS (two-scale reduction; CONFIRMED by the theory auditor, AT-681, under the stated
   Fourier moment and domain assumptions), Lemma HB (high band; CONFIRMED, AT-682, under the stated Fourier moment
   and high-band assumptions) and the theory auditor's Lemma HB' (exact C_aw remainder; CONFIRMED, AT-688, under Fourier L1 and
   finite M4) give TS3 = max(A_low(K'), A_hi(K)) + E(K, K'). Lemma HSB (CONFIRMED conditionally, AT-695) gives the far
   constant max(SC(a), A_low(K')) + S_h^B with a weighted Schur cost S_h^B of the ramp remainder; Corollary HSB-R
   (CONFIRMED conditionally, AT-706) is its row-wise form, and the band-restricted rows of AT-707 (CONFIRMED) give a
   continuum band upper of the size osc(a_f) or more. Remark 3 of Lemma HSB is restated with a disk of fixed
   positive radius (AT-799 REFUTED the disk of radius K for K = 0; AT-797 and AT-798 CONFIRMED the repaired necessary
   conditions and the window 3/5 < s <= 7/5 under the envelope C <zeta>^(-9/2)). None of these results gives a
   certified number by itself: each needs the certified inputs of section 3.
2. Certification inputs (section 3). Lemma HSB at a split needs C0 to C7: the unwindowed far piece handled inside HSB
   (charging the window tail separately by an absolute bound costs osc of the tail, 0.27 to 0.29 at Rw 50 (the second numerics agent),
   against the HSB-R margins to Gbar of 0.047 and 0.175 at the rows of item 4); SC^+ (an interval Hessian of the 009
   coefficient times the cut); a continuum band upper A_low^+(K') of the full plane; a majorant of |a^|; the Schur
   rows with their regularity
   between nodes and their tail; the regularity of the 009 coefficient across its panel boundaries; the strain
   target s_* <= c - A/q; the near price (the first theory agent HF1-NEAR). The operative band condition is A_low^+ <= G - S^+, not
   A_low^+ <= SC^+: HSB <= G holds exactly when both SC^+ and A_low^+ are at most G - S^+. Proposition TS needs T1 to
   T4 (band upper, IMS error, Lambda_+^+ with the remainders of Lemma HB or HB', and C0, C5, C6, C7).
3. FLOAT evaluation (section 4, Tables B, U, P, K, T, O, W, D, N, L). At every computed HSB row the lead is SC(a_f)
   and the band value is a high-frequency packet located where SC is attained. The second numerics agent finds this packet stable under
   changes of box and window below 2e-4 relative. A second, low-frequency branch grows with the box: by 1 percent at
   erflog 8 and by 6 to 11 percent at log 16, rho >= 1.5 (Table L). It lies below the 8 pi packet value except at
   log 16, rho >= 1.5, and below SC except at log 16, rho 1.75 and 2.
4. Best model split with Lemma HSB (section 5.1): erflog 8 at rho 0.9 and rho 1 (K' = 8 pi, K = 2 pi). These rows are
   admissible at Gbar in FLOAT and have the smallest model near prices among such rows.
   - rho 0.9: SC 0.5778, band 0.4735, S_h^B 0.0369, HSB 0.6148, HSB-R 0.6046, margin to Gbar 0.047, level c - far/q
     1.522. Model prices P_A/budget and P_B/budget: 0.334 and 0.621 at D161, 0.469 and 0.873 at U22.
   - rho 1: SC 0.4598, band 0.3848, S_h^B 0.0227, HSB 0.4825, HSB-R 0.4766, margin 0.175, level 1.583. Model prices:
     0.384 and 0.737 at D161, 0.541 and 1.04 at U22.
   - At rho 0.85, HSB-R is 0.6880 > Gbar.
   - The N 3072 resolution check at rho 1 gives SC 0.4608, HSB 0.4835 and HSB-R 0.4776, 0.2 percent above the
     N 2048 values.
   All far values are FLOAT and all prices are HEURISTIC.
5. erflog 16, rho 1 with the OMF charge at G = 2 (section 5.2, Table W). OMF = 1.939 (N 2048, Rw 96); N 1024 and 4096
   give 1.9314 and 1.9396; Rw 150 gives 1.9350; Rw 50 gives 2.0032, above 2. The value fits G = 2 in FLOAT (it needs
   s_* <= 0.887; G = 2 itself needs s_* <= 0.85793). The model price P_B/D161 is 1.35, so this split gives no near
   price below the budget (HEURISTIC).
6. Proposition TS at log 16, rho 1.5 (section 5.3, Table T). TS3 = 0.4535 at K' = 8 pi, K = 14.37 (lead A_hi 0.2514,
   E 0.2020); the band budget Gbar - E = 0.4496 is 2.6 times the full-plane band value 0.1699 (the second numerics agent). The far side fits
   with a large margin in FLOAT, but the model prices 1.27 (P_A/D161) and 2.64 (P_B/D161) exceed every budget. The
   inputs to certify are T1 to T4 with the FLOAT targets of 5.3. At erflog 8, rho 1 (section 5.4), TS3 at 16 pi would
   be 0.6030 < Gbar if the 16 pi band value is at most 0.5819; that band value is in the queue.
7. C2-N1-013 against C2-N1-009 (section 6, Table N). At the four HSB rows (log 8, rho 1 and 1.5; log 16, rho 1; erflog
   8, rho 1) the largest change of a far value is 1.4e-5 (HSB-R at erflog 8, rho 1). The linear transfer bound
   A(013) <= A(009) + OMF(d_f), with OMF(d_f) between 3.1e-4 and 8.509e-4 at six splits (Table D), moves the level by
   at most 4.06e-4. On the far side the two centers are indistinguishable in FLOAT. This corrects the wording of the
   10:57Z notes entry (AT-810; section 1 item Q11).
8. Corrections (section 1). Items Q1 to Q9 correct or qualify v01 and the 09:37Z note: band values are not bounds
   (AT-554, AT-612, AT-621); there is no 007-to-009 transfer (AT-610); "SC(a_f) is the high-frequency limit" is
   withdrawn (AT-622, AT-623); the AT-624 certification rule; the scaling readings (AT-625, AT-626); the high-high
   block (AT-649, AT-650); the cut shape; the window of the 09:37Z TS values (AT-697); and the band space is not
   finite-dimensional (AT-697). Items Q10 (Remark 3, AT-799) and Q11 (the 10:57Z wording, AT-810) are new.
9. OPEN:
   - a certified continuum band upper A_low^+(K') (AT-697; section 2.5 route (b));
   - a global Fourier envelope for the actual 009 or 013 far coefficient (AT-800);
   - A_* for the 009 far part (AT-623);
   - SC^+, the certified Schur rows, and a certified near price at any split.
   No split of this note is certified.

## 1. Corrections and qualifications to T2_FAR_v01 and to the second theory agent's notes since

T2_FAR_v01 (frozen 08:29:12Z, SHA256 8c37f0d7...) stays unchanged. The following statements of it are corrected or
qualified here (audit items of the theory auditor as cited in theory_v09 and in the theory audit exchange).
- (Q1) Band values (v01 Table F7 and 5.6). The band constant A_K (sup of F[a_f](g)/||J^(-1) g||^2 over S1 tests with
  g^ supported in a band of radius K) is nondecreasing in K and tends to the best (FG1) constant A_* as K tends to
  infinity (AT-621). The periodic collocation values of the code are FLOAT approximations of A_K; they are not
  certified lower or upper bounds of A_K (AT-554), and agreement of two resolutions does not certify their error
  (AT-612).
- (Q2) Source. The v01 band values were computed for the 007 background. They are not lower bounds for the complete
  009 coefficient without a transfer bound (AT-610). Section 4 gives the band values of the complete 009 coefficient
  (env CORR=b14s) and lists the 007 values separately.
- (Q3) The sentence of v01 5.6 "SC(a_f) is its high-frequency limit" is withdrawn. Lemma SC-LB gives A_* >= SC(a_f),
  but the high-frequency limit of A_K need not equal SC(a_f): the theory auditor gives a counterexample with large dilations of a
  radial bump (AT-622). A_* for the 009 far part is OPEN (AT-623). In the FLOAT data of section 4 the band values at
  rho 1.75 and 2 (log 16) agree at kmax 4 pi and 8 pi and exceed SC(a_f), so there the maximizer is a low-frequency
  mode, consistent with AT-622.
- (Q4) Certification rule (AT-624). A FLOAT far constant and an interpolated threshold radius are not certificates.
  (FG1) holds at a split once certified uppers O >= osc(a_f), m >= M2(a_f), w >= M2[w_new](a_f) and a certified
  global sbar >= s_* satisfy, at some explicit nu > 0 and with outward rounding,
  lambda_max [[O (1 + nu^2), 2 (1 + nu^(-2)) m], [2 (1 + nu^(-2)) m, (1 + nu^(-2)) m/2]] + q^2 w/2 <= q (c - sbar).
  At rho = 4 exactly, the log 16 charge of v01 is 0.65537, above Gbar = 0.65167; the threshold 4.0 printed in v01 is
  the rounded interpolation 4.0204 (AT-624).
- (Q5) Scaling readings (AT-625, AT-626). The local near-price law "roughly proportional to 1/G" (v01 6.2) is a fit to
  the finite log 16 data (gain exponent 1.0215 between Gbar and q). Under the scaled-family hypotheses of AT-625 the
  large-radius gain exponent would be (2 - gamma)/gamma = 3.468, so the local fit must not be extrapolated. The
  model price depends on the two signed sups S_- and S_+ separately, not on S = S_- + S_+ alone.
- (Q6) The high-high block. The theory auditor AT-649 gives a sign-free high-band bound B_nu (one of the high-band options of
  the TS3 evaluation in section 4) and refutes the general 1.23 improvement ceiling (AT-650). The proposed reading that a factor 2.5 needs
  sign information is therefore not established; the TS3 evaluation takes the smaller of the signed bound
  (Lemma HB with Lemma HB') and B_nu at each K.
- (Q7) Cut shape (v01 6.2, "the cut shape is not the lever"). Revised: at the same split radius the erflog cut of
  section 4 has the same near sups as the log cut and far moments 2 to 4 times smaller (FLOAT), and the OMF charge of
  the complete 009 far piece fits under q at rho 1.37 (erflog 8) against 2.18 (log 8). The cut shape is a lever for
  absolute-kernel far charges and also for Lemma HSB, whose lead is SC(a_f): at rho 1, SC(a_f) is 0.460 for erflog 8
  against 0.968 for log 8, with near prices within 1 percent of each other (Tables U and P; FLOAT and HEURISTIC).
- (Q8) Window. The Proposition TS values of the 09:37Z the second theory agent's note used the far_scan window max(50, 6 lam rho), while
  the band values use Rw 50: a mismatched-window diagnostic, not a common-coefficient value (AT-697). Section 4
  recomputes TS in the band window (TS3 column of Table U, with min(rC, rE)).
- (Q9) The 09:37Z note item 10 called the band problem finite-dimensional. L^2 of a frequency disk is
  infinite-dimensional even with S1 parity (AT-697); a certified band constant needs a quantitative projection error
  inside the disk (section 2.3, Remark 4).
- (Q10) Remark 3 of Lemma HSB (10:33Z note). Its second necessary condition used the disk of radius K around xi. For
  K = 0 that disk has zero area and the condition is vacuous, so the two displayed conditions do not characterize the
  window 0.6 < s <= 1.4 (AT-799, REFUTED as stated; the theory auditor: K = 0, envelope <zeta>^(-9/2), s = 2). The repair is a disk of
  any fixed positive radius R0 (AT-797, CONFIRMED for every K >= 0); section 2.3, Remark 3, is restated with it. No
  HSB statement and no row value changes.
- (Q11) The notes entry of 10:57Z said that all columns of the log 8 comparison of C2-N1-013 with C2-N1-009 agree
  within 1.3e-7 and that the largest OMF of the difference is at most 8.5e-4 (AT-810, REFUTED as worded). The HSB-R
  difference at log 8, rho 1 is 2.4e-7 and the band difference 3.1e-7; the largest printed OMF of the difference is
  8.509e-4 (erflog 8). Section 6 gives the corrected statements.

## 2. Analytic far uppers

### 2.1 A two-scale reduction: Proposition TS

Setting and notation as in T2_FAR_v01 section 1: F[a](g) := Q_a(g) + C_aw[a](g), S[k], zeta = xi - eta, s = |zeta|,
omega(p) = p/|p|, <p> = (1 + |p|^2)^(1/2), w_new and M2[w_new] as there. By Lemma KER', F[a] = S[k_a] with
    k_a(xi, eta) = -(1/2) a^(zeta) [ |omega(xi) - omega(eta)|^2 + 4 sinh(q t/2)^2 ],   t := log<xi> - log<eta>.
Extended class. X is the set of real S1 functions g with <xi>^q g^ in L^2. For g in X the kernel integral S[k_a](g)
converges absolutely (Young, as in the proof of Lemma KER'), and we take it as the definition of F[a](g); for tests
it is the form of Lemma KER'. For a radial real bounded function chi on R^2, chi(D) maps X into X (it keeps
reality and the S1 symmetry, since chi^ commutes with the coordinate reflections). With G(xi) := <xi>^(-1) |g^(xi)|,
||G||_2^2 = (2 pi)^2 ||J^(-1) g||^2, and Young gives, for every kernel with |k(xi, eta)| <xi> <eta> <= |a^(zeta)| e(|zeta|),
    |S[k](g)| <= (2 pi)^(-2) int |a^(zeta)| e(|zeta|) d zeta ||J^(-1) g||^2.                                    (Y)

Band constants. For 0 < K < K' put
    A_low(K') := sup { F[a](g)/||J^(-1) g||^2 : 0 != g in X, g^ = 0 a.e. on |xi| > K' },
    A_hi(K)   := sup { F[a](g)/||J^(-1) g||^2 : 0 != g in X, g^ = 0 a.e. on |xi| < K },
and let A_* := sup over tests of F[a](g)/||J^(-1) g||^2 (the best (FG1) constant). Tests are dense in X for the norm
||<xi>^q g^||_2 and F[a] is continuous for it (Young), so A_low(K') <= A_* and A_hi(K) <= A_*.

Proposition TS (two-scale reduction; CLAIMED here; CONFIRMED by the theory auditor, AT-681, under the stated Fourier moment and
domain assumptions). Let a be real with a^ in L^1 and M2[w_new](a) finite, and 0 < K < K'.
Then for every g in X
    F[a](g) <= [ max(A_low(K'), A_hi(K)) + E(K, K') ] ||J^(-1) g||^2,   E(K, K') := (2 pi)^(-2) int |a^(zeta)| eI(|zeta|) d zeta,
with
    eI(s) := (1/4) s^2 (o_K(s) + q^2 w_new(s)) (2 - 2 cos((pi/2) min(1, s/(K' - K)))),
    o_K(s) := min( 4 (1 + K^(-2)), ((1 + K^(-2))(1 + (K - s)^(-2)))^(1/2) ) for s < K,   o_K(s) := 4 (1 + K^(-2)) for s >= K.
Hence A_low(K') <= A_* <= max(A_low(K'), A_hi(K)) + E(K, K').
Proof.
- Partition. Let theta(p) := (pi/2) min(1, max(0, (|p| - K)/(K' - K))), chi_0 := cos theta, chi_1 := sin theta. These
  are radial, real and Lipschitz, chi_0^2 + chi_1^2 = 1, chi_0 = 0 on |p| >= K' and chi_1 = 0 on |p| <= K. Put
  g_i := chi_i(D) g, in X. Then ||J^(-1) g||^2 = ||J^(-1) g_0||^2 + ||J^(-1) g_1||^2, and g_0 (g_1) is admissible in
  A_low(K') (A_hi(K)).
- IMS identity. chi_0(xi) chi_0(eta) + chi_1(xi) chi_1(eta) = cos(theta(xi) - theta(eta))
  = 1 - (1/2) Dchi(xi, eta), Dchi := sum_i (chi_i(xi) - chi_i(eta))^2 = 2 - 2 cos(theta(xi) - theta(eta)). Since
  g_i^(eta) conj(g_i^(xi)) = chi_i(eta) chi_i(xi) g^(eta) conj(g^(xi)),
      F[a](g) = F[a](g_0) + F[a](g_1) + (1/2) S[k_a Dchi](g).
- Error kernel. |theta(xi) - theta(eta)| <= (pi/2) min(1, ||xi| - |eta||/(K' - K)) <= (pi/2) min(1, s/(K' - K)), so
  Dchi <= 2 - 2 cos((pi/2) min(1, s/(K' - K))). Dchi = 0 unless m := max(|xi|, |eta|) > K, and then
  min(|xi|, |eta|) >= m - s > K - s. By Lemma TII-1 (i), |omega(xi) - omega(eta)|^2 <xi> <eta> <= 4 s^2 (1 + m^2)/m^2
  <= 4 s^2 (1 + K^(-2)), using <xi> <eta> <= 1 + m^2. For s < K, by (ii), |omega(xi) - omega(eta)|^2 <xi> <eta>
  <= s^2 (<xi>/|xi|)(<eta>/|eta|) <= s^2 ((1 + K^(-2))(1 + (K - s)^(-2)))^(1/2). By the proof of Lemma CAW-F,
  4 sinh(q t/2)^2 <xi> <eta> <= q^2 s^2 w_new(s). Hence (1/2) |k_a Dchi| <xi> <eta> <= |a^(zeta)| eI(s), and (Y) bounds
  the last term by E(K, K') ||J^(-1) g||^2.
- Sum. F[a](g) <= A_low(K') ||J^(-1) g_0||^2 + A_hi(K) ||J^(-1) g_1||^2 + E(K, K') ||J^(-1) g||^2. QED.
Remarks.
- Any radial Lipschitz pair with chi_0^2 + chi_1^2 = 1 can be used, with eI changed accordingly. E(K, K') is finite
  under M2[w_new](a) < infinity, and E -> 0 as K' - K -> infinity at fixed K/K' only if the moment of order 4 is finite
  (eI(s) ~ s^4 for s << K' - K).
- The proposition reduces (FG1) to a band-limited problem (A_low, a finite-band quadratic form) and a high band A_hi,
  with the explicit cost E. A certified A_low needs a certified band computation (OPEN; the periodic collocation values
  of section 4 are FLOAT, AT-554). The square band |xi_1|, |xi_2| <= K' contains the disk |xi| <= K', so its best
  constant is >= A_low(K').

### 2.2 The high band: Lemma HB and Lemma HB'

Lemma HB (high band; CLAIMED here; CONFIRMED by the theory auditor, AT-682, under the stated Fourier moment and high-band
assumptions). Let a be real with a^ in L^1 and M2[w_new](a) finite. Then a is C^2 with bounded
continuous Hessian H; put Lambda_+(a) := sup_X max(lambda_max H(X), 0). For K > 0 and every g in X with g^ = 0 a.e. on
|xi| < K,
    F[a](g) <= [ (1/2)(1 + K^(-2) + q^2) Lambda_+(a) + R_Q(K) + R_C(K) ] ||J^(-1) g||^2,
    R_Q(K) := (2 pi)^(-2) int |a^(zeta)| rQ_K(|zeta|) d zeta,   R_C(K) := (2 pi)^(-2) int |a^(zeta)| rC_K(|zeta|) d zeta,
with
    rQ_K(s) := (1/2)(1 + K^(-2)) min(s^4/(4 K^2), s^2),
    rC_K(s) := (1/2) min( q^2 s^2 (w_new(s) + 1), p_K(s) + q^2 e_K(s) ) for s < 2K,   rC_K(s) := (1/2) q^2 s^2 (w_new(s) + 1) for s >= 2K,
    p_K(s) := min( (q^4/12) cosh(q tm) s^4/<K>^2, q^2 s^2 w_new(s) ),   tm := min(asinh(s/2), s/<K>),
    e_K(s) := (s^4/<d>^2) P(s/<d>),   P(x) := 9/4 + (7/4) x + (19/16) x^2 + (13/16) x^3 + (5/16) x^4,   <d>^2 := 1 + K^2 - s^2/4.
So A_hi(K) <= (1/2)(1 + K^(-2) + q^2) Lambda_+(a) + R_Q(K) + R_C(K).
Proof. Let xi, eta lie in |p| >= K, with angle phi between them.
- (H1) An exact identity. With n(p) := p_perp/|p|^2, p_perp = (-p_2, p_1): zeta.n(xi) = -|eta| sin(phi)/|xi| and
  zeta.n(eta) = -|xi| sin(phi)/|eta| (signed angle phi from xi to eta), so
      |omega(xi) - omega(eta)|^2 = 2 - 2 cos phi = (zeta.n(xi))(zeta.n(eta)) + (1 - cos phi)^2.
  Similarly, with u(p) := p/<p>^2 = grad log<p>,
      4 sinh(q t/2)^2 = q^2 (zeta.u(xi))(zeta.u(eta)) + [4 sinh(q t/2)^2 - q^2 (zeta.u(xi))(zeta.u(eta))].
- (H2) Principal parts are Hessian forms. Put W := grad_perp (-Delta)^(-1) g and U := grad J^(-2) g, so
  W^ = i n(xi) g^ and U^ = i u(xi) g^; both are real L^2 fields (g^ vanishes on |xi| < K). For b with b^ in L^1 and
  f, k in L^2, <b f, k> = (2 pi)^(-4) int int b^(xi - eta) f^(eta) conj(k^(xi)). With b = d_j d_k a, b^ = -zeta_j zeta_k a^
  (in L^1 because M2(a) is finite):
      S[-(1/2) a^(zeta) (zeta.n(xi))(zeta.n(eta))](g) = (1/2) int H(W, W) dX <= (1/2) Lambda_+ ||W||^2 <= (1/2)(1 + K^(-2)) Lambda_+ ||J^(-1) g||^2,
      S[-(q^2/2) a^(zeta) (zeta.u(xi))(zeta.u(eta))](g) = (q^2/2) int H(U, U) dX <= (q^2/2) Lambda_+ ||U||^2 <= (q^2/2) Lambda_+ ||J^(-1) g||^2,
  since |xi|^(-2) <= (1 + K^(-2)) <xi>^(-2) on |xi| >= K and |xi|^2 <xi>^(-4) <= <xi>^(-2).
- (H3) The Q remainder. 1 - cos phi = |omega(xi) - omega(eta)|^2/2 <= s^2/(2 |xi| |eta|) by Lemma TII-1 (ii), and
  <xi> <eta> <= (1 + K^(-2)) |xi| |eta|. So (1 - cos phi)^2 <xi> <eta> <= (1 + K^(-2)) s^4/(4 |xi| |eta|) <= (1 + K^(-2)) s^4/(4 K^2),
  and also (1 - cos phi)^2 <= 2 (1 - cos phi) <= s^2/(|xi| |eta|) gives (1 - cos phi)^2 <xi> <eta> <= (1 + K^(-2)) s^2.
  So the remainder kernel of Q_a is bounded by |a^| rQ_K/(<xi> <eta>), and (Y) applies.
- (H4) The C_aw remainder, crude form. 4 sinh(q t/2)^2 <xi> <eta> <= q^2 s^2 w_new(s) (proof of Lemma CAW-F), and
  |zeta.u(xi)| |zeta.u(eta)| <xi> <eta> <= s^2 |xi| |eta|/(<xi> <eta>) <= s^2. So the bracket of (H1) times <xi> <eta> is at most
  q^2 s^2 (w_new(s) + 1) in absolute value.
- (H5) The C_aw remainder, Taylor form (s < 2K). Write L = <xi>, l = <eta>, A = zeta.u(xi), B = zeta.u(eta). Then
  |4 sinh(q t/2)^2 - q^2 A B| <= |4 sinh(q t/2)^2 - q^2 t^2| + q^2 |t^2 - A B|.
  - First term. 4 sinh(x/2)^2 - x^2 = sum_(n >= 2) 2 x^(2n)/(2n)!, which lies in [0, (x^4/12) cosh x] (termwise,
    2/(2n)! <= 1/(12 (2n - 4)!) for n >= 2). Since (L - l)^2 = 4 L l sinh(t/2)^2 >= L l t^2 and |L - l| <= s,
    t^2 <= s^2/(L l), and |t| <= log(1 + s/min(L, l)) <= s/<K>; also |t| <= asinh(s/2) (Lemma CAW-F). So
    |4 sinh(q t/2)^2 - q^2 t^2| L l <= (q^4/12) cosh(q tm) t^4 L l <= (q^4/12) cosh(q tm) s^4/<K>^2. It is also
    <= 4 sinh(q t/2)^2 L l <= q^2 s^2 w_new(s). This gives p_K.
  - Second term. Let mid := (xi + eta)/2, phi(p) := log<p> and f(tau) := phi(mid + tau zeta) for |tau| <= 1/2, so
    t = f(1/2) - f(-1/2), A = f'(1/2), B = f'(-1/2). Put A0 := f'(0), B0 := f''(0)/2, m3 := sup |f'''| on [-1/2, 1/2].
    Taylor: f'(tau) = A0 + 2 B0 tau + R(tau), |R(tau)| <= m3 tau^2/2, so t = A0 + r_t with |r_t| <= m3/24, A = A0 + B0 + R(1/2),
    B = A0 - B0 + R(-1/2), |R(+-1/2)| <= m3/8, and
        t^2 - A B = B0^2 + A0 (2 r_t - R(1/2) - R(-1/2)) + B0 (R(1/2) - R(-1/2)) + r_t^2 - R(1/2) R(-1/2),
        |t^2 - A B| <= B0^2 + |A0| m3/3 + |B0| m3/4 + (10/576) m3^2.
    Derivatives of phi: grad phi = p/<p>^2, D^2 phi = <p>^(-2) I - 2 <p>^(-4) p p^T (eigenvalues <p>^(-2) and
    (1 - |p|^2) <p>^(-4), both of modulus <= <p>^(-2)), and for |e| = 1, x = p.e,
    D^3 phi(e, e, e) = (x/<p>^4)(-6 + 8 x^2/<p>^2), of modulus <= 6 |x|/<p>^4 <= 6/<p>^3. Every point of the segment
    [eta, xi] has |p| >= d := (K^2 - s^2/4)^(1/2) (the foot of the perpendicular splits the segment into parts x_1, x_2
    with x_1 + x_2 = s and K^2 <= d_0^2 + min(x_1, x_2)^2 <= d_0^2 + s^2/4 for the distance d_0; if the foot lies
    outside, the minimum is at an endpoint). Let <p_0> be the minimum of <p> on the segment, so <p_0> >= <d>,
    <mid> >= <p_0> and <mid> <= <p_0> + s/2. Then |A0| <= s/<mid>, |B0| <= s^2/(2 <mid>^2), m3 <= 6 s^3/<p_0>^3, and
    L^2 l^2 = (<mid>^2 + s^2/4)^2 - (mid.zeta)^2, so L l <= <mid>^2 + s^2/4. Hence
        B0^2 L l <= s^4/(4 <d>^2) + s^6/(16 <d>^4),
        |A0| (m3/3) L l <= 2 s^4 (<mid> + s^2/(4 <mid>))/<p_0>^3 <= 2 s^4/<d>^2 + s^5/<d>^3 + s^6/(2 <d>^4),
        |B0| (m3/4) L l <= (3/4) s^5 (1 + s^2/(4 <mid>^2))/<p_0>^3 <= (3/4) s^5/<d>^3 + (3/16) s^7/<d>^5,
        (10/576) m3^2 L l <= (5/8) s^6 (<p_0>^2 + s <p_0> + s^2/2)/<p_0>^6 <= (5/8) s^6/<d>^4 + (5/8) s^7/<d>^5 + (5/16) s^8/<d>^6.
    The sum is e_K(s). So |4 sinh(q t/2)^2 - q^2 A B| L l <= p_K(s) + q^2 e_K(s).
  With (H4), the C_aw remainder kernel is bounded by |a^| rC_K/(<xi> <eta>), and (Y) applies.
- Sum of (H2) to (H5). QED.
Remarks.
- Lemma HB uses the sign of the Hessian (Lambda_+ in place of M2) in the principal part, which is what the first theory agent's note 36
  item 6 asks of a high-high estimate. Its principal constant (1/2)(1 + K^(-2) + q^2) Lambda_+ is at least SC(a)
  (Lemma SC-LB) up to the factor (1 + q^2) Lambda_+/sup((q^2 - 1) lambda_max + tr H). The remainders are of fourth
  order for s << K: R_Q + R_C ~ C (2 pi)^(-2) int |zeta|^4 |a^| /K^2. So the lemma is effective once K^2 is large
  compared with M4(a)/Lambda_+(a), M4(a) := (2 pi)^(-2) int |zeta|^4 |a^|.
- The closed forms rQ_K, rC_K and eI were also checked against the exact kernels by sampling (code/check_upper_kernels.py;
  FLOAT, not part of the proof).

Lemma HB' (the theory auditor AT-688 to AT-690, research/high_band_exact_remainder/PROOF.md in agent the theory auditor, proved there with an
independent checker; reviewed here, no error found). Under the hypotheses of Lemma HB with M4(a) := (2 pi)^(-2) int |zeta|^4 |a^|
finite, the C_aw remainder rC_K of Lemma HB may be replaced, for every s >= 0, by
    rE_K(s) := (1/2) min( [Gq (1 + x) + q^2/4] s^4/k^2, q^2 s^2 (W_K(s) + 1) ),   Gq := q^2 (q^2 - 4)/12 = 6027/40000,
    k := <K>, x := s/k, W_K(s) := H_q(min(asinh(s/2), log(1 + s/k))),
and pointwise by min(rC_K, rE_K). Moreover rE_K(s) <= s^4/(1 + K^2), so
    A_hi(K) <= (1/2)(1 + K^(-2) + q^2) Lambda_+(a) + [(1 + K^(-2))/(8 K^2) + 1/(1 + K^2)] M4(a).
Review. With A = zeta.xi/L^2 and B = zeta.eta/l^2 (L = <xi>, l = <eta>, t = log(L/l)): sinh t = zeta.(xi + eta)/(2 L l),
so sinh(t)^2 - A B = (zeta.xi - zeta.eta)^2/(4 L^2 l^2) = s^4/(4 L^2 l^2) and
    D := 4 sinh(q t/2)^2 - q^2 A B = g_q(t) + q^2 s^4/(4 L^2 l^2),   g_q(t) := 4 sinh(q t/2)^2 - q^2 sinh(t)^2.
The Taylor coefficients of g_q are 2 q^2 (q^(2n - 2) - 4^(n - 1))/(2n)! >= 0 (q >= 2), so g_q >= 0; the bound
g_q(t) <= Gq (e^|t| - 1)^4 is taken from AT-428 (sampled ratio at most 0.9998 on |t| <= 12, code/check_rE.py). For L >= l:
e := L - l <= s, l >= k, L/l <= 1 + x, so g_q(t) L l <= Gq e^4 L/l^3 <= Gq (1 + x) s^4/k^2 and q^2 s^4/(4 L l) <= q^2 s^4/(4 k^2).
The second branch: 4 sinh(q t/2)^2 L l = q^2 (L - l)^2 H_q(|t|) <= q^2 s^2 W_K(s) (AT-649) and |A B| L l <= s^2. The
coefficient one: H_q(t) <= e^((q - 1) t) since 1 - z^q <= q (1 - z) on [0, 1]; for x <= 4 the first branch gives at most
(5 Gq + q^2/4)/2 = 14847/16000; for x >= 4 the second gives at most q^2 ((1 + x)^(11/10) + 1)/(2 x^2), decreasing in x,
so at most 441 (5^(11/10) + 1)/3200 < 1. Sampled kernel check (FLOAT): |D| L l/2 <= rE_K(s) with worst ratio 0.986 on
1.4e6 random pairs, K from 0.5 to 50 (code/check_rE.py).
In section 4, TS3 denotes Proposition TS evaluated with Lemma HB' (min(rC_K, rE_K)).

### 2.3 Lemma HSB: the signed principal part of Lemma HS with a band constant at low frequency

Lemma HS of the first theory agent (agent the first theory agent, research/far_hh/HS_DERIVATION.md, CLAIMED; reviewed in the 09:37Z the second theory agent's note, no error
found) bounds the far form by max(SC(a), osc(a)) + S_h. Its lead term contains osc(a), which exceeds Gbar at the radii
of interest (HS Remark 3), and its remainder rows at low frequency are large (the C_aw part of the kernel is not
cancelled there). Lemma HSB keeps the signed principal part of HS at high frequency and replaces the zeroth-order
piece by the band constant of Proposition TS.

Notation (as in HS): v = J^-1 g, w = xi/|xi|, w' = eta/|eta|, zeta = xi - eta, <xi> = (1 + |xi|^2)^(1/2),
  Ktil(xi, eta) = <xi><eta> |w - w'|^2 + (<xi>^q - <eta>^q)^2 (<xi><eta>)^(1 - q),
  P(xi, eta)    = |zeta|^2 (w.w') + (q^2 - 1)(zeta.w)(zeta.w'),
so that B_a(g) := (Q_a + C_aw[a])(g) = S[-(1/2) a^ Ktil](v) (Lemma KER') and, for any multiplier phi(|xi|) with
values in [0, 1], M_phi(v) := S[-(1/2) a^ phi phi' P](v) <= SC(a) ||Phi v||^2 (HS Step 2), where
SC(a) = sup_x max(0, (1/2)[(q^2 - 1) lambda_max Hess a(x) + Delta a(x)]).

Band constant. For K' > 0 let A_low(K') be the supremum of S[-(1/2) a^ K](f)/||J^-1 f||^2, K = Ktil/(<xi><eta>) the
kernel of Lemma KER', over real nonzero f in L^2 with the parity of the test class and Fourier support in the closed
disk |xi| <= K'. For such f the double integral converges absolutely (K is bounded on the band and a^ is integrable),
so A_low(K') is finite; on band-limited Schwartz tests the kernel form equals B_a(f) (Lemma KER'), so
A_low(K') <= A_* (the optimal constant of the full form), and A_low increases with K' (AT-621).

Lemma HSB (CLAIMED here; CONFIRMED conditionally by the theory auditor, AT-695; see Remark 5). Let a be real and bounded with a^
a function such that int |a^(zeta)| (1 + |zeta|^2) d zeta is finite (the hypotheses of HS). Let 0 <= K < K', alpha(t) = (pi/2) clip((t - K)/(K' - K), 0, 1), theta(t) = cos alpha(t), phi(t) = sin alpha(t),
and let h : R^2 -> (0, infinity) be measurable. Put
  r_B(xi, eta) = (1 - theta(|xi|) theta(|eta|)) Ktil(xi, eta) - phi(|xi|) phi(|eta|) P(xi, eta),
  S_h^B = sup_xi (2 pi)^-2 int (1/2) |a^(xi - eta)| |r_B(xi, eta)| h(eta)/h(xi) d eta.
Then for every g in the test class
  B_a(g) <= SC(a) ||Phi v||^2 + A_low(K') ||Theta v||^2 + S_h^B ||v||^2 <= [max(SC(a), A_low(K')) + S_h^B] ||J^-1 g||^2.

Proof. Ktil = phi phi' P + theta theta' Ktil + r_B pointwise, so
  B_a(g) = M_phi(v) + S[-(1/2) a^ theta theta' Ktil](v) + S[-(1/2) a^ r_B](v),
each term converging absolutely (v^ is rapidly decreasing, the kernels grow at most polynomially and a^ is
integrable). The first term is at most SC(a) ||Phi v||^2 by HS Step 2.
For the second, f := J Theta v has f^ = <xi> theta(|xi|) v^, which vanishes for |xi| >= K'; f is real with the parity
of g since theta is radial and real; and S[-(1/2) a^ theta theta' Ktil](v) = S[-(1/2) a^ K](f) by
substitution. Hence it is at most A_low(K') ||J^-1 f||^2 = A_low(K') ||Theta v||^2. The kernel -(1/2) a^ r_B has
|k(xi, eta)| = |k(eta, xi)| (a is real; Ktil, P and the products are symmetric), so the weighted Schur test of HS Step 4
bounds the third term by S_h^B ||v||^2. Finally phi^2 + theta^2 = 1 and SC(a) >= 0 give the second inequality. QED.

Remarks.
1. r_B = 0 when |xi|, |eta| <= K. On |xi|, |eta| >= K', r_B = Ktil - P, the high-frequency remainder of HS. In general
   r_B = (1 - cos(alpha - beta)) Ktil + phi phi' (Ktil - P) with alpha = alpha(|xi|), beta = alpha(|eta|), and
   1 - cos(alpha - beta) <= (pi^2/8) (|xi| - |eta|)^2/(K' - K)^2 <= (pi^2/8) |zeta|^2/(K' - K)^2: the IMS error of
   Proposition TS appears inside the Schur rows instead of as a separate sum.
2. Lemma HSB uses osc(a) nowhere. Its lead is max(SC(a), A_low(K')), which lies between SC(a) and A_* (Lemma SC-LB).
   A three-part version with a third multiplier chi carrying Lemma OSC (phi^2 + theta^2 + chi^2 <= 1) has lead
   max(SC, A_low, osc) and is not useful when osc(a) exceeds the other two.
3. (Corrected 10:33Z; the 10:08Z note had "S_h^B is finite only if int |a^| (1 + |zeta|)^(q + 1) is finite", which
   holds for h = 1 only.) Finiteness of S_h^B needs decay of a^ beyond the HS hypotheses. For |xi| <= K and
   |eta| >= K', theta(|xi|) = 1, phi(|xi|) = 0, theta(|eta|) = 0, so r_B = Ktil there, and for fixed xi
   Ktil(xi, eta) >= (<eta>^q - <xi>^q)^2 (<xi><eta>)^(1 - q) is of order <eta>^(q + 1); the same holds with xi and eta
   exchanged. For h = <xi>^-s, s >= 0, the row at a fixed xi is therefore finite only if
   int_(|zeta| > R) |a^(zeta)| <zeta>^(q + 1 - s) d zeta is finite (for every fixed xi, since r_B = Ktil - phi(|xi|) P
   once theta(|eta|) = 0 and |P| = O(|xi - eta|^2) is of lower order), and for every fixed R0 > 0 the rows at large
   |xi| contain (2 pi)^-2 int_(|eta| <= R0) (1/2) |a^(xi - eta)| |r_B| (<xi>/<eta>)^s d eta with |r_B| bounded below by a
   constant times <xi>^(q + 1) on that disk, so they stay bounded only if int_(|eta| <= R0) |a^(xi - eta)| d eta is
   O(<xi>^-(q + 1 + s)). (Corrected 11:15Z after AT-799: the 10:33Z text used the disk of radius K, which has zero area
   when K = 0, so that its condition is vacuous there; the two conditions with a fixed positive radius R0 are the
   necessary conditions proved by the theory auditor in AT-797, for every K >= 0.) For a weight that is constant at large |xi|
   (the Perron weight as extended in code/hsb_far.py) the first condition reads int |a^(zeta)| <zeta>^(q + 1) d zeta < infinity. If |a^| decays like
   |zeta|^(-9/2) (the order expected, HEURISTIC, for radial profiles that are C^2 with jumps of the third derivative
   on circles, such as the cubic splines in log r used by the FLOAT code), the two conditions hold exactly for
   0.6 < s <= 1.4, and a weight constant at infinity gives S_h^B = infinity. The theory auditor (AT-798, CONFIRMED) proves the
   sufficiency direction: a global upper envelope |a^(zeta)| <= C <zeta>^(-9/2) gives a finite Schur supremum for
   3/5 < s <= 7/5, and a matching lower envelope makes the window necessary. No such envelope is established for the
   actual 009 coefficient (AT-800, OPEN). In the FLOAT field this decay is not visible: at erflog 8, rho 1 (N 4096, runs/ahat_decay_erflog8_rho1_N4096.out) the shell means of |a^| fall with
   local log-log slopes between -6 and -12 for 6 < |zeta| < 40, then stay at a flat floor near 1e-11 (rounding and
   aliasing) up to the grid frequency 97.5, and (2 pi)^-2 int_(|zeta| <= Z) |a^| <zeta>^(q + 1) d zeta is 3.746,
   3.799, 3.806 at Z = 10, 20, 97.5. The regularity of the actual 009 coefficient across its radial panel
   boundaries is nevertheless an input of any certificate (section 3, item C5).
4. Certification needs, beyond those of HS: a certified upper for A_low(K'). The band operator is a bounded
   operator on the band space with an explicit kernel, but the band space is infinite-dimensional (AT-697: the
   tests with Fourier transform i xi_2 f_j(|xi|), f_j smooth radial on disjoint annuli K'/(j + 2) < |xi| < K'/(j + 1),
   are mutually orthogonal real S1 tests). A certificate therefore needs a finite matrix enclosure together with a
   quantitative projection or discretization error bound inside the disk; the exterior remainder of HSB does not
   supply it. The FLOAT square-band periodic values of section 4 are not such an upper (AT-554, AT-612).
5. Lemma HSB is CONFIRMED by the theory auditor (AT-695 to AT-698) under these hypotheses with a finite certified S_h^B and the
   continuum band constant. In the FLOAT runs, SC is a spatial maximum over r <= Rw of the windowed field and does
   not include the outer window transition (AT-697), and the Perron weights and row matrices are saved from the
   09:57Z version of code/hsb_far.py on.

### 2.4 Row-wise form (HSB-R)

Corollary HSB-R (the first theory agent's note 37, Corollary HS-R and its HSB analogue; CONFIRMED conditionally by the theory auditor AT-706,
research/hs_rows_audit/PROOF.md in agent the theory auditor). Under the hypotheses of Lemma HSB, with
  rho_h^B(xi) = (2 pi)^-2 int (1/2) |a^(xi - eta)| |r_B(xi, eta)| h(eta)/h(xi) d eta,
every g in the test class satisfies
  B_a(g) <= int [ SC(a) phi(|xi|)^2 + A_low(K') theta(|xi|)^2 + rho_h^B(xi) ] |v^(xi)|^2 dmu(xi)
         <= ess sup_xi [ SC(a) phi^2 + A_low(K') theta^2 + rho_h^B ] ||J^-1 g||^2,     dmu = (2 pi)^-2 d xi.
Proof. In the proof of Lemma HSB, apply the weighted Schur inequality
|f(xi) f(eta)| <= (1/2)[|f(xi)|^2 h(eta)/h(xi) + |f(eta)|^2 h(xi)/h(eta)] to f = v^ before taking the supremum in xi
(AT-706); the two other terms are already diagonal in xi. The right side is at most the HSB constant
max(SC, A_low) + S_h^B, since phi^2 + theta^2 = 1 and rho_h^B <= S_h^B. QED.
FLOAT evaluation (code/hsbr_rows.py on the saved rows of code/hsb_far.py): the maximum over the 32 sampled radii of
SC phi^2 + band theta^2 + (row of weight h at that radius, maximum over the 5 sampled angles), minimized over the five
weights; band = the square-band periodic value (FLOAT, not an upper). It reproduces the theory auditor AT-715 (log 8: 1.3678 at
rho 1, 0.5306 at rho 1.5). The gain over the separate maxima is between 0.2 and 2.3 percent in the computed rows (Table U,
HSB and HSB-R columns; largest at erflog 8, rho 0.75), because at the ramps used the largest rows sit at frequencies
where phi is close to 1 and the lead there is already SC.

### 2.5 What is available for a continuum band upper, and what is not

Lemma HSB needs a certified upper of the continuum band constant A_low(K') (Remark 4). Two routes.

(a) Band-restricted rows (the theory auditor AT-707, CONFIRMED). For E = {|xi| <= K'}, multipliers phi_E, theta_E with
phi_E^2 + theta_E^2 <= 1, a positive weight h, and the HS remainder r = Ktil - phi_E phi_E' P - theta_E theta_E' |w - w'|^2,
  A_low(K') <= ess sup_(xi in E) [ SC(a) phi_E^2 + osc_* theta_E^2 + rho_h^E(xi) ],
where rho_h^E integrates only over eta in E and osc_* = min(osc(a), osc(a_(2K'))), a_(2K') the low-pass part of a at
radius 2K' (AT-707: Q_a(f) = Q_(a_(2K'))(f) for f^ supported in E). This bound is a continuum statement with no
discretization of the band space. FLOAT findings (code/osc_lowpass.py, runs/osc_lowpass_1020.out; code/hsb_band_rows.py,
runs/hsb_band_rows_erflog_lam8_b14s_N512_RW50.json):
- At the nine candidate splits of Table O, osc(a_(2K')) differs from osc(a_f) by at most 0.1 percent for K' >= 2, is
  up to 1.5 percent larger at K' = 1 and up to 6 percent larger at K' = 0.5 (ringing of the sharp low-pass): the
  low-pass does not lower the oscillation coefficient here.
- At frequency 0 the restricted row with theta_E = 1 is of order 1: the C_aw part 4 sinh(q t/2)^2 of Ktil is not
  small at |eta| of order 1. At erflog 8, rho 1 (N 512, a resolution-limited trial run) the bound is 1.14 for the
  part_tau1_p2 multipliers (maximum at the origin row, osc 0.771 plus row 0.37 in the weight <xi>^-1.5), against
  SC 0.450 and the square-band value 0.385.
So route (a) gives a certifiable A_low upper only of the size osc(a_f) + rho^E(0), above SC(a_f) and, at the splits
of interest, above Gbar. It cannot make the HSB lead equal to SC(a_f).

(b) A finite enclosure with a projection error (AT-697). The square-band periodic values (Table B) are below SC(a_f)
at every split of the complete 009 far piece with an HSB row (Table U); they exceed it at log 16, rho 1.75 and 2
(Table L). A certificate of A_low(K') <= G - S^+ (the band budget of section 3, C2) needs (i) a finite
matrix enclosure of the band form on a finite-dimensional space V_n of band-limited tests, and (ii) a bound for the
form on the orthogonal complement of V_n in the band space and for the cross terms. One natural choice for (i) and
(ii): for a square band [-K', K']^2 (which contains the disk), Shannon sampling identifies the band space with
l^2(Z^2) through the samples f(pi n/K'); the band form becomes an infinite matrix with entries given by the kernel of
Lemma KER' on sinc functions; a compactly supported (windowed) coefficient makes the entries decay away from the
support (for the unwindowed a_f of C0 the far asymptotics of the coefficient take the place of the compact
support), and a Schur tail bound for the entries with n outside a finite box gives (ii). This is not done here; the
periodic collocation of code/far_box4.py is a different discretization (periodized coefficient, frequencies on the
2 pi/L lattice) and has no such error bound (AT-554, AT-612). The disk band constant is at most the square-band
constant of the same K' (the disk space is a subspace), so an upper for the square band suffices.

## 3. Certification inputs, in a form that can be certified one by one

Each item is a single inequality with its direction, the quantity it bounds, the FLOAT value that the certified
number has to stay close to for the split to keep its margin, and the method suggested. Nothing in this section is
certified. "Split" means (cut, lam, rho) and the far coefficient a_f = cut(r/rho) atil of the complete 009
coefficient (C2-N1-009, CORR b14s); the near coefficient is a_n = (1 - cut) atil.

### 3.1 Far charge by Lemma HSB / Corollary HSB-R at a split, with ramp (K, K') and weight h

The certified far constant is A = max(SC^+, A_low^+) + S^+ (Lemma HSB) or the row-wise maximum of Corollary HSB-R with
the same certified pieces; the split is admissible for the gain G = q (c - s_*) when A <= G, i.e. s_* <= c - A/q
(G = Gbar = q(c - 3/2) needs A <= 0.65167; G = 1.5 needs s_* <= 1.0960; G = 2 needs s_* <= 0.85793; these are
FLOAT conversions of the fixed q = 21/10, c = 4076476460239181/2251799813685248).

C0 (window and angular truncation). The FLOAT runs use a_f^W = a_f (1 - Sinf((r - Rw)/Ww)), Rw 50, Ww 10, and the
background truncated to the cosine modes cos(2 k theta), k < 8 (KUSE 8). Lemma HSB applies to the unwindowed far piece
a_f itself once a_f satisfies its hypotheses (C5): a_f is real and bounded, and with the decay |a_f| of order
r^(-0.448) at large r reported by the second numerics agent (FLOAT) its Fourier transform is locally integrable at the origin. The window
is then a computational device, and a certificate should bound the three HSB inputs of the unwindowed a_f directly.
Charging the tail a_t = a_f Sinf((r - Rw)/Ww) separately by an absolute bound does not work at these margins: the second numerics agent
(10:57Z note item 3; results/N2_BAND_ALOW_v01.md in agent the second numerics agent) finds that every available absolute bound of the tail
(Lemma OSC, Lemma TII-1 with CAW-F, and so OMF) costs at least osc(a_t), 0.27 to 0.29 at Rw 50 and still 0.05 at
Rw 2000, against HSB-R margins to Gbar of 0.047 and 0.175 at the rows of section 5.1. Inside HSB the tail enters
only (i) SC (the tail Hessian is small; in
runs/omf_check_*.out the maximum over the whole box equals the maximum over r <= Rw to four digits), (ii) A_low (the
band constant of the full plane; the second numerics agent: at the HSB rows of Table U the top band vector is a high-frequency packet
where SC is attained, insensitive to box and window below 2e-4 relative, while a low-frequency branch moves by 4 to
11 percent with the box and lies below SC at log 16, rho <= 1.5 and above it at rho 1.75 and 2), and (iii) the Schur
rows, through |a^| at |zeta| of order 1/Rw, where r_B vanishes to second order in zeta (small; not quantified here).
The angular modes k >= 8 enter SC, A_low and the rows in the same way; the second numerics agent finds a mode-truncation effect of 2e-6 on
the band value at log 16, rho 1.5 (all 88 modes). Needed: certified bounds of the unwindowed quantities in C1, C2,
C3, from the far asymptotics of the 009 coefficient and a certified angular mode tail.

C1 (semiclassical constant). SC^+ >= sup over x in R^2 of max(0, (1/2)[(q^2 - 1) lambda_max D^2 a(x) + Delta a(x)])
for a = a_f (all of R^2, C0). Method: interval evaluation of the second derivatives of cut * atil on a polar
covering of a bounded region, from certified C^2 bounds of the radial mode functions of the 009 coefficient and of
the C-infinity cut, plus a certified bound of D^2 a_f outside it from the far asymptotics. FLOAT values: Table U
(SC column, maximum over r <= Rw of the windowed field).

C2 (band constant). A_low^+ >= A_low(K'), the continuum band constant of section 2.3 on the disk |xi| <= K' (or on
the square [-K', K']^2, which is larger). For the lead of HSB to be SC^+ one needs A_low^+ <= SC^+, but the
operative requirement for the gain G is weaker: HSB <= G holds exactly when SC^+ <= G - S^+ and A_low^+ <= G - S^+,
so A_low^+ may exceed SC^+ as long as it stays below the band budget G - S^+ (Table K; at Gbar the budget is 1.3 to
1.6 times the FLOAT band value at erflog 8, rho 0.9 and 1, and at log 16, rho 1). The band value must be the
full-plane one: the second numerics agent finds a low-frequency branch that grows with the box and the window (section 4, Table L).
Route (b) of section 2.5 (finite enclosure plus a projection error) is the only route seen that can give such an
upper; route (a) gives values of the size osc(a_f) + rho^E(0). FLOAT targets: Tables B and L (periodic values, not
uppers).

C3 (majorant of |a^|). A measurable m(zeta) >= |a^(zeta)| for all zeta in R^2, for the coefficient of C1. Suggested:
FFT values on a zero-padded grid plus (i) the aliasing sum bounded through |a^(zeta)| <= ||Delta^k a||_1 |zeta|^(-2k)
(Poisson summation is exact for the grid sums of a compactly supported a), (ii) the variation between grid nodes
through |grad a^(zeta)| <= || |x| a ||_1 (or exact sinc interpolation, a being supported in the box), and (iii) the
same decay bound beyond the grid frequency. m must satisfy the decay conditions of Remark 3 of section 2.3 for the
weight used, and the rows of C4 computed with m in place of |a^| must stay below the target.

C4 (Schur rows). S^+ >= sup over xi in R^2 of rho_h^B(xi) (Lemma HSB) or, for Corollary HSB-R, a bound of
SC^+ phi^2 + A_low^+ theta^2 + rho_h^B at every xi. Inputs: (i) a_f is even in x_1 and in x_2 (cosine modes in
2 theta), so |a^| and the rows are invariant under the reflections of xi and xi may be restricted to the closed
first quadrant; (ii) a modulus of continuity of xi -> rho_h^B(xi) between the sampled nodes (32 radii, 5 angles),
from bounds of the xi-derivatives of r_B and of log h (the ramp angle alpha is Lipschitz with constant
(pi/2)/(K' - K)); (iii) a bound of rho_h^B for |xi| > 60 (FLOAT rows with h = 1 decay to 0.03 at |xi| = 60 at
log 8, rho 1; with the Perron weight they stay between 0.35 and 0.42); (iv) the weight h exactly as used: the
Perron weight is defined on the nodes u_j = log<r_j> (saved as perron_weight in runs/hsb_*.json since 09:57Z),
extended linearly in u = log<|xi|> between nodes and constantly outside; with that extension Remark 3 requires
int |a^| <zeta>^(q + 1) < infinity, so a certificate may need a weight that decays at infinity; (v) the eta
integral as an integral, not an FFT sum (cell-wise variation of m |r_B| h).

C5 (hypotheses of HS/HSB). a real and bounded, a^ a function with int |a^| (1 + |zeta|^2) finite (HS), plus the decay
needed for a finite S^+ with the chosen h (Remark 3 of section 2.3). These are regularity statements about the
actual 009 coefficient across its radial panel boundaries and about the cut and window (C-infinity), to be read off
the candidate representation.

C6 (strain target). The admissibility A <= G requires the certified global sbar >= s_* with s_* <= c - A/q. FLOAT
reference: for every HSB row the level c - far/q is given in Table P.

C7 (near side). The near price at the split is not certified here: the HF-1 model prices P_A, P_B of Table P are
HEURISTIC; the first theory agent Proposition HF1-NEAR (CLAIMED) is to replace them. Its inputs at the split (Lambda_+(a_n), M4(a_n),
the signed sups S_-, S_+ of a_n W^2, ||(a_n)_+||_1) are FLOAT values of runs/far_scan*_b14s_N2048_K8.json at the
near spacing near_h of the table.

### 3.2 Proposition TS at log 16, rho 1.5 (or any split), with (K, K')

TS: A = max(A_low^+(K'), A_hi^+(K)) + E^+(K, K'), with
T1. A_low^+(K') >= A_low(K') (continuum band; as C2, the same open discretization problem).
T2. E^+(K, K') >= (2 pi)^-2 int |a^(zeta)| eI(|zeta|) d zeta (the IMS error of Proposition TS; with rE of AT-688 the
pointwise minimum of the two remainders, AT-733), computed for the same coefficient and the same spatial window as T1
and T3 (AT-686, AT-697): a certified majorant m of C3 suffices, since the integrand is |a^| times an explicit radial
function.
T3. A_hi^+(K) >= A_hi(K), the high-band constant on |xi| >= K, for the same coefficient. With Lemma HB (section 2.2):
a certified global upper of Lambda_+(a) = sup_x lambda_max D^2 a(x) (all of R^2, including the window transition), and
certified values of the two remainder integrals RQ and RC of Lemma HB (or of the rE remainder of Lemma HB'), each an
integral of |a^| times an explicit kernel, so again C3 suffices.
T4. Inputs C0, C5, C6 and C7 as for HSB.
The FLOAT TS values in the band window (Table U, TS3 column) use the square-band periodic band values for T1.
For Lemma HSB at the same split, SC^+ of C1 is needed in addition (it does not enter TS).

## 4. FLOAT tables

Tables B, U, P and N are printed by code/make_v02_tables2.py and Tables K, T, O, W and D by code/make_v02_tables3.py
from the saved run files (outputs runs/v02_tables2_1118.md and runs/v02_tables3_1118.md of this version). Table L is
assembled from the second numerics agent's results and from runs/lowbr_1106.log. Every far value is FLOAT and every price is HEURISTIC; no entry is a bound. The coefficient
is the complete 009 coefficient (env CORR=b14s) unless a column says 007 (background only) or 013 (CORR=b18s2,
C2-N1-013). The field pipeline, cuts (log lam, erflog lam), window and angular truncation are those of
T2_FAR_v01 section 5 and of the table headings.

### Table B. Band values A_II_aw (FLOAT; square band |xi_1|, |xi_2| <= kmax; L 128, Rw 50, Ww 10)

| log 8 | 009 4 pi | 007 4 pi | 009 8 pi | 007 8 pi | 013 8 pi |
|---|---|---|---|---|---|
| rho 1 | 0.5322 | 0.5320 | 0.7284 | 0.7282 | 0.7284 |
| rho 1.25 | 0.3881 | 0.3880 | 0.5067 | 0.5065 | - |
| rho 1.5 | 0.2861 | 0.2861 | 0.3674 | 0.3673 | 0.3674 |
| rho 1.75 | 0.2224 | 0.2223 | 0.2747 | 0.2746 | - |
| rho 2 | 0.1730 | 0.1730 | 0.2109 | 0.2109 | - |

| log 16 | 009 2 pi | 007 2 pi | 009 4 pi | 007 4 pi | 009 8 pi | 007 8 pi | 013 8 pi | 009 16 pi |
|---|---|---|---|---|---|---|---|---|
| rho 1 | 0.2032 | 0.2032 | 0.2557 | 0.2557 | 0.3395 | 0.3393 | 0.3395 | 0.3863 |
| rho 1.25 | - | - | 0.1818 | 0.1818 | 0.2275 | 0.2274 | - | - |
| rho 1.5 | - | - | 0.1588 | 0.1588 | 0.1603 | 0.1603 | - | - |
| rho 1.75 | - | - | 0.1446 | 0.1446 | 0.1446 | 0.1446 | - | - |
| rho 2 | - | - | 0.1330 | 0.1330 | 0.1330 | 0.1330 | - | - |

| erflog 8 | 009 2 pi | 009 8 pi | 013 8 pi |
|---|---|---|---|
| rho 0.75 | - | 0.6716 | - |
| rho 0.85 | - | 0.5291 | - |
| rho 0.9 | 0.2961 | 0.4735 | - |
| rho 1 | 0.2635 | 0.3848 | 0.3848 |

### Table U. FLOAT far values of the complete 009 far piece (b14s, N 2048, K 8 modes)

Window Rw 50, Ww 10 except OMF (far_scan window max(50, 6 lam rho) for log, 2.2 x 1.1 rho lam^(1/2) e^(...) for erflog).
HSB: smallest over the computed (K', K/K') configurations; lead = max(SC, band); HSB-R: row-wise, weight in brackets.

| log 8, rho | SC | osc | band (conf) | S_h^B | HSB | HSB-R (h) | HS | TS3 | OMF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.9682 | 0.805 | 0.7284 (8pi_K0.25) | 0.416 | 1.3844 | 1.3678 (perron) | 2.47 | 6.87 | 14.4 |
| 1.25 | 0.6450 | 0.735 | - | - | - | - | - | 3.15 | 7.84 |
| 1.5 | 0.4471 | 0.68 | 0.3674 (8pi_K0.25) | 0.0863 | 0.5334 | 0.5306 (perron) | 1.2 | 1.66 | 4.92 |
| 1.75 | 0.3256 | 0.635 | - | - | - | - | - | 0.971 | 3.4 |
| 2 | 0.2437 | 0.599 | 0.2109 (8pi_K0.25) | 0.0275 | 0.2711 | 0.2691 (s0) | 0.853 | 0.615 | 2.51 |

| log 16, rho | SC | osc | band (conf) | S_h^B | HSB | HSB-R (h) | HS | TS3 | OMF |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 0.4275 | 0.646 | 0.3863 (16pi_K0.25) | 0.0345 | 0.4621 | 0.4592 (s0) | 1.18 | 0.864 | 4.96 |
| 1.25 | 0.2743 | 0.585 | 0.2275 (8pi_K0.25) | 0.0414 | 0.3157 | 0.3143 (perron) | 0.885 | 0.836 | 2.9 |
| 1.5 | 0.1874 | 0.538 | - | - | - | - | - | 0.453 | 1.95 |
| 1.75 | 0.1344 | - | - | - | - | - | - | 0.277 | - |
| 2 | 0.1001 | 0.47 | - | - | - | - | - | 0.185 | 1.13 |

| erflog 8, rho | SC | osc | band (conf) | S_h^B | HSB | HSB-R (h) | HS | TS3 | OMF |
|---|---|---|---|---|---|---|---|---|---|
| 0.75 | 0.8536 | 0.863 | 0.6716 (8pi_K0.25) | 0.0817 | 0.9353 | 0.9140 (s0) | 1.86 | 1.75 | 7.31 |
| 0.85 | 0.6535 | 0.822 | 0.5291 (8pi_K0.25) | 0.0479 | 0.7014 | 0.6880 (s0) | 1.54 | 1.17 | 5.44 |
| 0.9 | 0.5778 | 0.804 | 0.4735 (8pi_K0.25) | 0.0369 | 0.6148 | 0.6046 (s0) | 1.43 | 0.986 | 4.78 |
| 1 | 0.4598 | 0.771 | 0.3848 (8pi_K0.25) | 0.0227 | 0.4825 | 0.4766 (s0) | 1.25 | 0.727 | 3.81 |

### Table P. Strain level and HF-1 model prices (HEURISTIC) at every HSB row (009, b14s)

far = min(HSB, HSB-R); level = c - far/q (the far test asks s_* <= level; Gbar <=> level >= 3/2). Entries P_A/budget, P_B/budget
at the scanned near row of the same rho (near spacing h_n; M4 median stand-in where h_n > 0.0305).

| split, rho | far | level | h_n | D161 | U161 | U22 | D22 | U141 | D141 |
|---|---|---|---|---|---|---|---|---|---|
| log 8, 1 | 1.3678 | 1.159 | 0.0299 | 0.388 / 0.743 | 0.356 / 0.68 | 0.547 / 1.05 | 1.1 / 2.11 | 0.488 / 0.933 | 0.979 / 1.87 |
| log 8, 1.5 | 0.5306 | 1.558 | 0.0300 | 0.74 / 1.48 | 0.677 / 1.36 | 1.04 / 2.08 | 2.1 / 4.2 | 0.929 / 1.86 | 1.86 / 3.73 |
| log 8, 2 | 0.2691 | 1.682 | 0.0300 | 1.17 / 2.4 | 1.08 / 2.2 | 1.65 / 3.38 | 3.33 / 6.8 | 1.47 / 3.01 | 2.96 / 6.05 |
| log 16, 1 | 0.4592 | 1.592 | 0.0300 | 0.669 / 1.35 | 0.612 / 1.24 | 0.941 / 1.9 | 1.89 / 3.83 | 0.84 / 1.7 | 1.68 / 3.4 |
| log 16, 1.25 | 0.3143 | 1.661 | 0.0300 | 0.956 / 1.96 | 0.875 / 1.79 | 1.34 / 2.75 | 2.71 / 5.55 | 1.2 / 2.46 | 2.41 / 4.93 |
| erflog 8, 0.75 | 0.9140 | 1.375 | 0.0300 | 0.263 / 0.462 | 0.241 / 0.423 | 0.37 / 0.65 | 0.746 / 1.31 | 0.33 / 0.58 | 0.663 / 1.16 |
| erflog 8, 0.85 | 0.6880 | 1.483 | 0.0300 | 0.309 / 0.565 | 0.283 / 0.517 | 0.435 / 0.795 | 0.875 / 1.6 | 0.388 / 0.709 | 0.778 / 1.42 |
| erflog 8, 0.9 | 0.6046 | 1.522 | 0.0300 | 0.334 / 0.621 | 0.305 / 0.568 | 0.469 / 0.873 | 0.945 / 1.76 | 0.419 / 0.779 | 0.84 / 1.56 |
| erflog 8, 1 | 0.4766 | 1.583 | 0.0300 | 0.384 / 0.737 | 0.352 / 0.674 | 0.541 / 1.04 | 1.09 / 2.09 | 0.483 / 0.925 | 0.968 / 1.86 |

Budgets (stipulated inputs, code/price3.py): U22 = N 0.022 U(l 2.76e-6, c+1); D22 = N 0.022 D(f 2.76e-6, 209/100); U141 = N 0.0141 U(l 2.76e-6, c+1); D141 = N 0.0141 D(f 2.76e-6, 209/100); U161 = N 0.0161 U(l 1.5e-06, 7/4); D161 = N 0.0161 D(f 1.5e-06, 7/4).

### Table N. C2-N1-013 (CORR b18s2) against 009 (CORR b14s), same field, window and ramp configurations (FLOAT)

| split, rho | center | SC | osc | M2 | band (conf) | S_h^B | HSB | HSB-R (h) | level | D161 | U161 | U22 | D22 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| log 8, 1 | 009 | 0.9682 | 0.8051 | 2.0295 | 0.7284 (8pi_K0.25) | 0.416 | 1.3844 | 1.3678 (perron) | 1.159 | 0.388 / 0.743 | 0.356 / 0.68 | 0.547 / 1.05 | 1.1 / 2.11 |
| log 8, 1 | 013 | 0.9682 | 0.8051 | 2.0295 | 0.7284 (8pi_K0.25) | 0.416 | 1.3844 | 1.3678 (perron) | 1.159 | 0.388 / 0.742 | 0.355 / 0.68 | 0.547 / 1.04 | 1.1 / 2.1 |
| log 8, 1.5 | 009 | 0.4471 | 0.6800 | 0.8188 | 0.3674 (8pi_K0.25) | 0.0863 | 0.5334 | 0.5306 (perron) | 1.558 | 0.74 / 1.48 | 0.677 / 1.36 | 1.04 / 2.08 | 2.1 / 4.2 |
| log 8, 1.5 | 013 | 0.4471 | 0.6800 | 0.8188 | 0.3674 (8pi_K0.25) | 0.0863 | 0.5334 | 0.5306 (perron) | 1.558 | 0.739 / 1.48 | 0.677 / 1.36 | 1.04 / 2.08 | 2.09 / 4.19 |
| log 16, 1 | 009 | 0.4275 | 0.6464 | 0.8156 | 0.3395 (8pi_K0.25) | 0.1 | 0.5277 | 0.5245 (perron) | 1.561 | 0.669 / 1.35 | 0.612 / 1.24 | 0.941 / 1.9 | 1.89 / 3.83 |
| log 16, 1 | 013 | 0.4275 | 0.6464 | 0.8156 | 0.3395 (8pi_K0.25) | 0.1 | 0.5277 | 0.5245 (perron) | 1.561 | 0.669 / 1.35 | 0.612 / 1.24 | 0.941 / 1.9 | 1.89 / 3.82 |
| erflog 8, 1 | 009 | 0.4598 | 0.7711 | 0.7700 | 0.3848 (8pi_K0.25) | 0.0227 | 0.4825 | 0.4766 (s0) | 1.583 | 0.384 / 0.737 | 0.352 / 0.674 | 0.541 / 1.04 | 1.09 / 2.09 |
| erflog 8, 1 | 013 | 0.4598 | 0.7711 | 0.7700 | 0.3848 (8pi_K0.25) | 0.0227 | 0.4825 | 0.4766 (s0) | 1.583 | 0.384 / 0.737 | 0.352 / 0.674 | 0.541 / 1.04 | 1.09 / 2.09 |

### Table K. Band budgets of Lemma HSB (FLOAT): the largest band upper A_low^+ that keeps max(SC, A_low^+) + S_h^B <= G

Gbar = q(c - 3/2) = 0.65167. Configuration of the smallest HSB value; band = square-band periodic value (L 128, Rw 50).

| split, rho | conf | SC | S_h^B | band | Gbar - S_h^B | ratio to band | SC <= Gbar - S_h^B | 1.5 - S_h^B |
|---|---|---|---|---|---|---|---|---|
| log 8, 1.0 | 8pi_K0.25 | 0.9682 | 0.4162 | 0.7284 | 0.2355 | 0.32 | no | 1.0838 |
| log 8, 1.5 | 8pi_K0.25 | 0.4471 | 0.0863 | 0.3674 | 0.5654 | 1.54 | yes | 1.4137 |
| log 8, 2.0 | 8pi_K0.25 | 0.2437 | 0.0275 | 0.2109 | 0.6242 | 2.96 | yes | 1.4725 |
| log 16, 1.0 | 16pi_K0.25 | 0.4275 | 0.0345 | 0.3863 | 0.6171 | 1.60 | yes | 1.4655 |
| log 16, 1.25 | 8pi_K0.25 | 0.2743 | 0.0414 | 0.2275 | 0.6103 | 2.68 | yes | 1.4586 |
| erflog 8, 0.75 | 8pi_K0.25 | 0.8536 | 0.0817 | 0.6716 | 0.5700 | 0.85 | no | 1.4183 |
| erflog 8, 0.85 | 8pi_K0.25 | 0.6535 | 0.0479 | 0.5291 | 0.6038 | 1.14 | no | 1.4521 |
| erflog 8, 0.9 | 8pi_K0.25 | 0.5778 | 0.0369 | 0.4735 | 0.6147 | 1.30 | yes | 1.4631 |
| erflog 8, 1.0 | 8pi_K0.25 | 0.4598 | 0.0227 | 0.3848 | 0.6290 | 1.63 | yes | 1.4773 |

### Table T. Proposition TS with Lemma HB' (TS3; FLOAT, window Rw 50, N 2048, best K on a grid of 120 values)

A_hi = principal (1/2)(1 + K^-2 + q^2) Lambda_+ plus the remainders R_Q + min-kernel R_C; band budget = Gbar - E (TS3 <= Gbar
exactly when A_low^+ and A_hi are both <= Gbar - E). Where no band value was computed at K', only A_hi + E is listed.

| split, rho | Lambda_+ | K'/pi | K | band | principal | remainders | A_hi | E | TS3 or A_hi + E | Gbar - E |
|---|---|---|---|---|---|---|---|---|---|---|
| log 8, 1.0 | 0.4329 | 8 | 19.68 | 0.7284 | 1.1715 | 0.3617 | 1.5333 | 5.3333 | 6.8666 | -4.6817 |
| log 8, 1.0 | 0.4329 | 16 | 32.92 | - | 1.1712 | 0.1252 | 1.2963 | 1.7135 | 3.0098 (no band) | -1.0618 |
| log 8, 1.25 | 0.2878 | 8 | 17.56 | 0.5067 | 0.7789 | 0.1774 | 0.9563 | 2.1946 | 3.1509 | -1.5429 |
| log 8, 1.25 | 0.2878 | 16 | 30.22 | - | 0.7786 | 0.0581 | 0.8366 | 0.6047 | 1.4413 (no band) | 0.0470 |
| log 8, 1.5 | 0.1996 | 8 | 16.58 | 0.3674 | 0.5404 | 0.0914 | 0.6318 | 1.0268 | 1.6586 | -0.3752 |
| log 8, 1.5 | 0.1996 | 16 | 28.54 | - | 0.5401 | 0.0300 | 0.5701 | 0.2491 | 0.8193 (no band) | 0.4025 |
| log 8, 1.75 | 0.1452 | 8 | 15.22 | 0.2747 | 0.3932 | 0.0561 | 0.4493 | 0.5215 | 0.9707 | 0.1302 |
| log 8, 1.75 | 0.1452 | 16 | 26.95 | - | 0.3930 | 0.0174 | 0.4104 | 0.1144 | 0.5247 (no band) | 0.5373 |
| log 8, 2.0 | 0.1088 | 8 | 14.79 | 0.2109 | 0.2945 | 0.0334 | 0.3279 | 0.2870 | 0.6149 | 0.3647 |
| log 8, 2.0 | 0.1088 | 16 | 25.45 | - | 0.2943 | 0.0110 | 0.3053 | 0.0574 | 0.3628 (no band) | 0.5942 |
| log 16, 1.0 | 0.1909 | 8 | 16.58 | 0.3395 | 0.5166 | 0.1080 | 0.6247 | 1.1974 | 1.8221 | -0.5457 |
| log 16, 1.0 | 0.1909 | 16 | 29.37 | 0.3863 | 0.5164 | 0.0334 | 0.5498 | 0.3142 | 0.8640 | 0.3375 |
| log 16, 1.25 | 0.1223 | 8 | 15.66 | 0.2275 | 0.3312 | 0.0462 | 0.3774 | 0.4584 | 0.8358 | 0.1933 |
| log 16, 1.25 | 0.1223 | 16 | 27.73 | - | 0.3310 | 0.0143 | 0.3453 | 0.1032 | 0.4485 (no band) | 0.5485 |
| log 16, 1.5 | 0.0836 | 8 | 14.37 | 0.1603 | 0.2263 | 0.0252 | 0.2514 | 0.2020 | 0.4535 | 0.4496 |
| log 16, 1.5 | 0.0836 | 16 | 25.45 | - | 0.2261 | 0.0078 | 0.2339 | 0.0405 | 0.2744 (no band) | 0.6112 |
| log 16, 1.75 | 0.0599 | 8 | 13.57 | 0.1446 | 0.1623 | 0.0148 | 0.1771 | 0.0996 | 0.2767 | 0.5520 |
| log 16, 1.75 | 0.0599 | 16 | 23.36 | - | 0.1622 | 0.0049 | 0.1670 | 0.0180 | 0.1850 (no band) | 0.6337 |
| log 16, 2.0 | 0.0446 | 8 | 11.43 | 0.1330 | 0.1209 | 0.0122 | 0.1331 | 0.0516 | 0.1847 | 0.6001 |
| log 16, 2.0 | 0.0446 | 16 | 22.70 | - | 0.1208 | 0.0030 | 0.1238 | 0.0092 | 0.1330 (no band) | 0.6424 |
| erflog 8, 0.75 | 0.3947 | 8 | 12.46 | 0.6716 | 1.0690 | 0.1138 | 1.1828 | 0.5675 | 1.7503 | 0.0842 |
| erflog 8, 0.75 | 0.3947 | 16 | 21.44 | - | 1.0682 | 0.0377 | 1.1059 | 0.0901 | 1.1959 (no band) | 0.5616 |
| erflog 8, 0.85 | 0.3010 | 8 | 11.77 | 0.5291 | 0.8153 | 0.0718 | 0.8871 | 0.2850 | 1.1721 | 0.3667 |
| erflog 8, 0.85 | 0.3010 | 16 | 20.84 | - | 0.8146 | 0.0225 | 0.8370 | 0.0464 | 0.8835 (no band) | 0.6052 |
| erflog 8, 0.9 | 0.2658 | 8 | 11.43 | 0.4735 | 0.7199 | 0.0587 | 0.7787 | 0.2070 | 0.9857 | 0.4447 |
| erflog 8, 0.9 | 0.2658 | 16 | 20.84 | - | 0.7192 | 0.0174 | 0.7366 | 0.0350 | 0.7716 (no band) | 0.6167 |
| erflog 8, 1.0 | 0.2110 | 8 | 11.11 | 0.3848 | 0.5717 | 0.0389 | 0.6105 | 0.1169 | 0.7274 | 0.5348 |
| erflog 8, 1.0 | 0.2110 | 16 | 20.84 | - | 0.5710 | 0.0109 | 0.5819 | 0.0211 | 0.6030 (no band) | 0.6306 |

### Table O. osc(a_f) against osc(a_(2K')), the low-pass part at radius 2K' (AT-707; FLOAT, N 1024)

| split, rho | SC | osc(a_f) | K' 0.5 | K' 1 | K' 2 | K' 4 | K' 4 pi | K' 8 pi |
|---|---|---|---|---|---|---|---|---|
| log 8, 1 | 0.9607 | 0.8051 | 0.8209 | 0.8084 | 0.8049 | 0.8051 | 0.8051 | 0.8051 |
| log 8, 1.5 | 0.4471 | 0.6800 | 0.6869 | 0.6819 | 0.6799 | 0.6800 | 0.6800 | 0.6800 |
| log 16, 1 | 0.4276 | 0.6464 | 0.6514 | 0.6493 | 0.6462 | 0.6464 | 0.6464 | 0.6464 |
| log 16, 1.25 | 0.2743 | 0.5851 | 0.5866 | 0.5842 | 0.5851 | 0.5851 | 0.5851 | 0.5851 |
| erflog 8, 0.75 | 0.8536 | 0.8624 | 0.8949 | 0.8750 | 0.8632 | 0.8624 | 0.8624 | 0.8624 |
| erflog 8, 1 | 0.4591 | 0.7711 | 0.7999 | 0.7750 | 0.7710 | 0.7711 | 0.7711 | 0.7711 |
| erflog 16, 0.5 | 0.8837 | 0.8266 | 0.8740 | 0.8345 | 0.8268 | 0.8267 | 0.8266 | 0.8266 |
| erflog 16, 0.75 | 0.3640 | 0.7023 | 0.7363 | 0.7022 | 0.7023 | 0.7023 | 0.7023 | 0.7023 |
| erflog 16, 1 | 0.1912 | 0.6209 | 0.6291 | 0.6225 | 0.6209 | 0.6209 | 0.6209 | 0.6209 |

### Table W. OMF baseline osc + M2 + (q^2/2) M2[w_new] of the windowed far piece: window and resolution (FLOAT)

| split, rho | N | Rw | h | osc | M2 | M2[w_new] | OMF | SC (r <= Rw) | SC (box) |
|---|---|---|---|---|---|---|---|---|---|
| erflog 16, 1 | 2048 | 96 | 0.1238 | 0.62091 | 0.34444 | 0.44163 | 1.93913 | 0.1906 | 0.1906 |
| erflog 16, 1 | 1024 | 96 | 0.2475 | 0.62091 | 0.34390 | 0.43838 | 1.93144 | 0.1891 | 0.1891 |
| erflog 16, 1 | 1066 | 50 | 0.1238 | 0.62091 | 0.36191 | 0.46276 | 2.00321 | 0.1906 | 0.1906 |
| erflog 16, 1 | 3200 | 150 | 0.1238 | 0.62091 | 0.34320 | 0.44032 | 1.93501 | 0.1906 | 0.1906 |
| erflog 16, 1 | 4096 | 96 | 0.0619 | 0.62091 | 0.34445 | 0.44183 | 1.93961 | 0.1912 | 0.1912 |
| erflog 8, 1.4 | 2048 | 72 | 0.0928 | 0.67022 | 0.36485 | 0.43587 | 1.99616 | 0.2190 | 0.2190 |
| erflog 8, 1.4 | 1024 | 72 | 0.1856 | 0.67020 | 0.36484 | 0.43584 | 1.99606 | 0.2164 | 0.2164 |
| erflog 8, 1.4 | 4096 | 72 | 0.0464 | 0.67022 | 0.36486 | 0.43611 | 1.99671 | 0.2190 | 0.2190 |
| erflog 8, 1.4 | 1422 | 50 | 0.0928 | 0.67022 | 0.37970 | 0.45524 | 2.05373 | 0.2190 | 0.2190 |
| erflog 8, 1.4 | 3200 | 108 | 0.0891 | 0.67022 | 0.36390 | 0.43479 | 1.99282 | 0.2190 | 0.2190 |
| erflog 8, 1.5 | 2048 | 72 | 0.0928 | 0.65053 | 0.31386 | 0.36834 | 1.77658 | 0.1871 | 0.1871 |
| erflog 8, 1.5 | 1024 | 72 | 0.1856 | 0.65051 | 0.31385 | 0.36832 | 1.77651 | 0.1871 | 0.1871 |
| erflog 8, 1.5 | 4096 | 72 | 0.0464 | 0.65054 | 0.31386 | 0.36855 | 1.77705 | 0.1874 | 0.1874 |
| erflog 8, 1.5 | 1422 | 50 | 0.0928 | 0.65053 | 0.33393 | 0.39518 | 1.85582 | 0.1871 | 0.1871 |
| erflog 8, 1.5 | 3200 | 108 | 0.0891 | 0.65053 | 0.31242 | 0.36672 | 1.77157 | 0.1872 | 0.1872 |

### Table D. OMF envelope of the far-form difference d_f = cut (atil(013) - atil(009)) window (FLOAT, N 2048, Rw 50)

| split, rho | sup abs d_f | osc | M2 | M2[w_new] | OMF(d_f) | share of M2[w_new] from abs zeta > 20 | OMF, abs zeta <= 20 | SC(d_f) | SC(-d_f) |
|---|---|---|---|---|---|---|---|---|---|
| log 8, 1 | 8.725e-10 | 1.521e-09 | 1.914e-05 | 3.060e-04 | 6.939e-04 | 0.993 | 5.296e-06 | 2.053e-06 | 1.874e-06 |
| log 8, 1.5 | 2.804e-10 | 5.012e-10 | 8.768e-06 | 1.377e-04 | 3.124e-04 | 0.991 | 2.880e-06 | 9.767e-07 | 7.834e-07 |
| log 16, 1 | 4.558e-10 | 7.999e-10 | 1.093e-05 | 1.733e-04 | 3.931e-04 | 0.992 | 3.315e-06 | 1.180e-06 | 9.899e-07 |
| erflog 8, 0.9 | 1.196e-09 | 2.059e-09 | 2.342e-05 | 3.753e-04 | 8.509e-04 | 0.993 | 6.302e-06 | 2.719e-06 | 2.453e-06 |
| erflog 8, 1 | 8.998e-10 | 1.549e-09 | 1.952e-05 | 3.122e-04 | 7.080e-04 | 0.993 | 5.384e-06 | 2.101e-06 | 1.906e-06 |
| erflog 16, 1 | 4.647e-10 | 8.157e-10 | 1.170e-05 | 1.861e-04 | 4.220e-04 | 0.992 | 3.458e-06 | 1.184e-06 | 9.877e-07 |

### Table L. Band values in large boxes: the packet branch and the low-frequency branch (FLOAT)

Square-band periodic values of the complete 009 far piece (CORR b14s, 8 modes). The log rows are the second numerics agent's
(agent the second numerics agent, results/N2_BAND_ALOW_v01.md Tables 1 and 4, results/BAND_009_*.json; computed independently, they
reproduce this agent's L 128 values to six digits); the erflog rows are this agent's (runs/lowbr_1106.sh and its log
runs/lowbr_1106.log, code/far_box4.py, files runs/far_box2_erflog_lam8_b14s_L<L>_N<N>_k<kmax>_inf_K8[_W<Rw>-<Ww>].json). "packet": the
top vector is a high-frequency wave packet at the radius where SC is attained; "low": it is a low-frequency mode
spread over the far region. K' of the large-box rows is pi/(4h) or pi/(2h) as listed.

| split, rho | SC | L 128, Rw 50, 8 pi | L 256 to 528, Rw 50 or 200, 8 pi | low branch, larger boxes | L 128, 16 pi | lead of HSB at 8 pi |
|---|---|---|---|---|---|---|
| log 8, 1 | 0.9682 | 0.7284 (packet) | 0.7282, 0.7281 (packet) | - | 0.8577 (packet) | SC |
| log 8, 1.5 | 0.4471 | 0.3674 (packet) | 0.3673, 0.3673 (packet) | 0.2104 (L 2112, Rw 800, pi) | 0.4120 (packet) | SC |
| log 8, 2 | 0.2437 | 0.2109 (packet) | 0.2109, 0.2109 (packet) | 0.1807 (L 2112, Rw 800, pi) | 0.2297 (packet) | SC |
| log 16, 1 | 0.4275 | 0.3395 (packet) | 0.3394, 0.3394 (packet) | - | 0.3863 (packet) | SC |
| log 16, 1.25 | 0.2743 | 0.2275 (packet) | 0.2275, 0.2275 (packet) | - | 0.2529 (packet) | SC |
| log 16, 1.5 | 0.1874 | 0.1603 (packet) | 0.1656 (L 256), 0.1687 (L 528, Rw 200) (low) | 0.1699 (L 1056 to 4224, Rw 400 to 1600) | 0.1752 (packet) | SC |
| log 16, 1.75 | 0.1344 | 0.1446 (low) | 0.1522 (L 256), 0.1559 (L 528, Rw 200) (low) | - | 0.1446 (low) | band |
| log 16, 2 | 0.1001 | 0.1330 (low) | 0.1412 (L 256), 0.1455 (L 528, Rw 200) (low) | 0.1472 (L 2112, Rw 800, pi) | 0.1330 (low) | band |
| erflog 8, 0.9 | 0.5778 | 0.4735 (packet) | - | 0.2961 (L 128, 2 pi), 0.2982 (L 528, Rw 200, 2 pi), 0.2908 (L 1056, Rw 400, pi) | - | SC |
| erflog 8, 1 | 0.4598 | 0.3848 (packet) | - | 0.2635 (L 128, 2 pi), 0.2668 (L 528, Rw 200, 2 pi), 0.2650 (L 1056, Rw 400, pi) | - | SC |

Readings. The packet values change by less than 2e-4 relative with the box and the window. The low branch grows
with the box and the window by 1 percent at erflog 8 and by 6 to 11 percent at log 16, rho 1.5 to 2. It stays
below the 8 pi packet value at every row except log 16, rho >= 1.5, and below SC except at log 16, rho 1.75 and 2. The
SC column is this agent's (maximum over r <= Rw on the polar grid); the second numerics agent's FFT Hessian on the Cartesian grid differs
from it by up to 2 percent (FLOAT, both). The square band contains the disk band of Lemma HSB; the second numerics agent finds the disk
value 0.5 percent below the square value at log 16, rho 1.5.

## 5. Splits

All values in this section are FLOAT far values or HEURISTIC model prices (Tables U, P, K, T, W, L of section 4).
None is a bound. "Admissible at G" means that the FLOAT far value is at most G; the certified version needs the
inputs of section 3.

### 5.1 Best model split with Lemma HSB: erflog 8, rho 0.9 to 1

Among the computed HSB rows of the complete 009 far piece, the rows that are admissible at Gbar in FLOAT and have
the smallest model near prices are erflog 8 at rho 0.9 and rho 1 (configuration K' = 8 pi, K = K'/4):

| quantity | erflog 8, rho 0.9 | erflog 8, rho 1 | source |
|---|---|---|---|
| SC(a_f) (r <= Rw) | 0.5778 | 0.4598 | Table U |
| band value, 8 pi, L 128 (packet branch) | 0.4735 | 0.3848 | Table B |
| top band value in large boxes (K' 2 pi, L 528, Rw 200) | 0.2982 | 0.2668 | Table L |
| S_h^B (best of the five weights) | 0.0369 | 0.0227 | Table U |
| HSB | 0.6148 | 0.4825 | Table U |
| HSB-R | 0.6046 | 0.4766 | Table U |
| Gbar - HSB-R | 0.0471 | 0.1751 | |
| band budget Gbar - S_h^B (ratio to the band value) | 0.6147 (1.30) | 0.6290 (1.63) | Table K |
| SC margin Gbar - S_h^B - SC | 0.0369 | 0.1692 | Table K |
| level c - far/q | 1.522 | 1.583 | Table P |
| P_A/budget, P_B/budget at D161 | 0.334 / 0.621 | 0.384 / 0.737 | Table P |
| P_A/budget, P_B/budget at U22 | 0.469 / 0.873 | 0.541 / 1.04 | Table P |

Readings.
- At rho 0.85 the HSB-R value is 0.6880, above Gbar (level 1.483). The smallest scanned admissible radius at Gbar is
  therefore 0.9; no interpolated radius is offered as a threshold (AT-624).
- At both rows the lead of HSB is SC(a_f) and the band value is the high-frequency packet branch at K' = 8 pi. The
  low-frequency branch, computed in boxes of side 528 and 1056 with the window moved to Rw 200 and 400 (Table L),
  lies far below the packet value (0.27 to 0.30 against 0.38 to 0.47) and far below SC. The second numerics agent finds the packet
  branch stable under box and window changes below 2e-4 relative at the log rows (N2_BAND_ALOW_v01 section 3.4).
  So in FLOAT the certificate needed at these rows is A_low^+(8 pi) <= Gbar - S^+ with a target value of 0.47 (rho
  0.9) or 0.38 (rho 1), and SC^+ <= Gbar - S^+ with targets 0.578 and 0.460.
- Against log 16, rho 1 (HSB-R 0.4592, level 1.592, prices 0.669 / 1.35 at D161): erflog 8, rho 1 has a slightly
  larger far value and near prices of about 0.55 times those of log 16, rho 1, and erflog 8, rho 0.9 lowers them by
  a further 13 to 16 percent at a far margin of 7 percent. The near prices at erflog 8 equal those at log 8 at the
  same rho to 1 percent (Table P), so the gain over log 16 comes from lam (the near piece ends near lam rho), and the
  gain over log 8 is on the far side (SC 0.460 against 0.968 at rho 1).
- Resolution check (runs/scan20.log, runs/hsb_erflog_lam8_b14s_N3072_RW50.json): at N 3072 the rho 1 row gives
  SC 0.4608, S_h^B 0.0227, HSB 0.4835 and HSB-R 0.4776 (band value of N 2048), against 0.4598, 0.0227, 0.4825
  and 0.4766 at N 2048 (runs/hsbr_rows_1118.out). The
  change, 0.2 percent, comes from SC (the maximum of the Hessian expression is sampled on a finer grid); it is
  small against the margin 0.175 and is one reason why C1 asks for an interval evaluation, not a grid maximum.
- Pending in the queue of runs/scan20.sh (section 7): HSB at K' = 16 pi with the band at N 4096, the band rows of
  Corollary HSB-R at the window edge, and the rows erflog 8 at rho 0.5 and 0.6.

### 5.2 erflog 16, rho 1: the OMF baseline at G = 2

The OMF baseline osc + M2 + (q^2/2) M2[w_new] (AT-664 to AT-667) of the complete 009 far piece at erflog 16, rho 1
is 1.939 (N 2048, far_scan window Rw 96, h 0.124). The OMF value is admissible at G = 2 in FLOAT; G = 2 itself needs
s_* <= c - 2/q = 0.85793, and the OMF value alone needs s_* <= c - 1.939/q = 0.887.
Resolution and window checks (Table W): N 1024 gives 1.9314, N 4096 gives 1.9396; Rw 50 gives 2.0032 (above 2) and
Rw 150 gives 1.9350; osc(a_f) is 0.62091 in every run (it is attained inside the smallest window), and the change
comes from M2 and M2[w_new]. SC(a_f) is 0.1906 to 0.1912, so the lead of an HSB charge at this row would be far below
Gbar; the HSB row at this split is queued (runs/scan21.sh, after scan20).
Model prices (HEURISTIC, scanned near row at rho 1): P_A/D161 0.669, P_B/D161 1.35; U22 0.941 / 1.9. These equal
the log 16, rho 1 prices to the printed digits: the near sups S_- 13.4 and S_+ 16.5 agree to three digits, which
suggests that they are attained at small radii where both cuts are close to 0 (the erflog cut is 0.006 at r = rho
for lam 16). So at G = 2 the OMF baseline does not give a split with a P_B price below the budget.
The inputs to certify OMF at this split are O >= osc(a_f), m >= M2(a_f), w >= M2[w_new](a_f) for the unwindowed
a_f (AT-624 rule, v02 section 1 item Q4); with the window effect of Table W (3 percent between Rw 50 and 96) the
certified values must use the far asymptotics of the 009 coefficient beyond the window.

### 5.3 Proposition TS at log 16, rho 1.5

TS3 (Proposition TS with Lemma HB and Lemma HB', section 2): at K' = 8 pi, K = 14.37 (Table T):
Lambda_+(a_f) 0.0836, principal part (1/2)(1 + K^-2 + q^2) Lambda_+ = 0.2263, remainders R_Q + R_C = 0.0252,
A_hi = 0.2514, E(K, K') = 0.2020, band value 0.1603 (L 128) and 0.1699 (full plane, the second numerics agent), TS3 = A_hi + E = 0.4535 with either band value,
since the lead is A_hi. The band budget Gbar - E = 0.4496 is 2.6 times the full-plane
band value, and A_hi = 0.2514 is below it with margin 0.198. At K' = 16 pi the sum A_hi + E is 0.2744, and with the
the second numerics agent value 0.1752 of the 16 pi band (packet) TS3 would be 0.2744 (lead A_hi 0.2339).
Inputs to certify (section 3.2): T1 A_low^+(8 pi) <= 0.4496 (or A_low^+(16 pi) <= 0.6112 at 16 pi); T2
E^+(K, K') near 0.2020 (8 pi) or 0.0405 (16 pi), from a certified majorant of |a^|; T3 Lambda_+^+ near 0.0836 with
the remainder integrals near 0.0252 (8 pi) or 0.0078 (16 pi); T4 as for HSB.
Model prices at this row (HEURISTIC, runs/far_price_TS3_short_1007.out): P_A/D161 1.27, P_B/D161 2.64. The far side
fits with a large margin, but the near price at rho 1.5 exceeds every budget; this split is not usable unless the
near estimate improves by a factor of about 2.6.

### 5.4 Proposition TS at erflog 8, rho 1

At K' = 16 pi, K = 20.84: Lambda_+ 0.2110, A_hi 0.5819, E 0.0211, A_hi + E = 0.6030, band budget Gbar - E 0.6306.
If the 16 pi band value of this row is at most A_hi = 0.5819 (the 8 pi value is 0.3848; at log 8 and log 16 the
step from 8 pi to 16 pi raises the band value by 9 to 18 percent, Table L), then TS3 = 0.6030 <
Gbar, with the near prices of 5.1. This is a second route at the same split that needs no SC certificate and
no Schur rows: it needs Lambda_+^+ (the same interval Hessian evaluation as C1), E^+ and the remainder integrals
(from the majorant of C3) and A_low^+(16 pi) <= 0.6306. Its far margin (0.049) is smaller than that of HSB-R (0.175). The band value at 16 pi (N 4096) is in the
queue.

## 6. C2-N1-013 against C2-N1-009 at the HSB rows (FLOAT)

Answer to the coordinator 10:37Z item 3(c) and 10:26Z item 5(a), first given in the team notes entry of 10:57Z and
completed here with the rows log 16, rho 1 and erflog 8, rho 1. The 013 coefficient is the 007 background plus the
b18s2 correction (C2-N1-013-phi-007-sector-d8-leg24-lat-nf2; phi file copied to research/h4/far009/inputs013/,
SHA256 a16e9d85...c32c2a, equal to the snapshot SHA256SUMS), run through code/corr_datil.py into
runs/main_b18s2_datil.npy and runs/near_b18s2_datil.npy on the same polar grids as the b14s correction. sup |datil(013) -
datil(009)| on the sample grid is 4.7e-8 (near grid) and 2.5e-9 on r >= 4 (runs/corr_diff_b14s_b18s2_1046.out).
Everything else (cut, window, modes, grids, ramps, weights) is the same as for 009.

Table N of section 4 lists both centers at the same ramp configurations. At full precision (FLOAT):

| split, rho, configuration | HSB 009 | HSB 013 | HSB-R 009 | HSB-R 013 | SC 009 | SC 013 |
|---|---|---|---|---|---|---|
| log 8, 1, 8pi_K0.25 | 1.38437933 | 1.38437945 | 1.36782441 | 1.36782417 | 0.96817873 | 0.96817877 |
| log 8, 1.5, 8pi_K0.25 | 0.53338881 | 0.53338881 | 0.53060652 | 0.53060642 | 0.44709119 | 0.44709119 |
| log 16, 1, 8pi_K0.25 | 0.52770727 | 0.52770733 | 0.52454418 | 0.52454475 | 0.42754833 | 0.42754832 |
| erflog 8, 1, 8pi_K0.25 | 0.48250000 | 0.48250112 | 0.47659508 | 0.47660915 | 0.45981146 | 0.45981155 |

The largest change of a far value is 1.4e-5 (HSB-R at erflog 8, rho 1), which moves the level c - far/q by 7e-6.
The band value at erflog 8, rho 1 is 0.38475776 for both centers at the printed digits. Correction of the notes entry
of 10:57Z (AT-810, REFUTED as worded): that entry said that all columns of the log 8 comparison agree within 1.3e-7
and that the largest OMF of the difference is at most 8.5e-4. The HSB and SC columns of the log 8 rows agree within
1.3e-7, but the HSB-R difference (2.4e-7 at log 8, rho 1) and the band difference (3.1e-7 at log 8, rho 1)
exceed it; the largest
printed OMF of the difference is 8.509e-4. The statements of this section replace those of 10:57Z.

Linear transfer bound. The far form is linear in a, and the OMF baseline is an absolute bound that applies to d and
to -d, so for every test |B_(d_f)(g)| <= OMF(d_f) ||J^(-1) g||^2 with d_f = cut (atil(013) - atil(009)), and
A(013) <= A(009) + OMF(d_f) for every far constant A that is an upper of the form (the same holds with the roles
exchanged). Table D gives OMF(d_f) between 3.1e-4 and 8.509e-4 at the six splits computed; 99 percent of it comes from
M2[w_new] at |zeta| > 20, a high-frequency floor of the difference field on the grid, and the part from |zeta| <= 20
is 3e-6 to 6e-6. With the floor included the level moves by at most 8.509e-4/q = 4.06e-4. This is a FLOAT statement
about the windowed fields of the two FLOAT coefficient tables; a certified transfer needs a certified OMF bound of
the certified difference.

Near side (FLOAT, same near box and spacing): S_-, S_+ and ||(a_n)_+||_1 agree to six digits at all four rows; M4(a_n)
is lower for 013 by 5.1e-4 relative at all four rows (log 8, rho 1: 5057.79 against 5060.35; erflog 8, rho 1: 5017.93
against 5020.48); the model price ratios of Table N agree to the printed digits except for P_B, which is lower by at
most 1 in the third digit.

Reading. On the far side the two centers are indistinguishable at the resolution of these runs: no far quantity of
Table N changes by more than 1.4e-5, and at the six splits of Table D the linear transfer envelope bounds the change
of any far upper by 8.509e-4 in FLOAT. The decision between the centers can be made on the near side and on the certification side alone.

## 7. Requests and queue

Requests (decide-and-proceed: this agent continues with the queue below whatever the answers are).
1. The numerical auditor: the certification items of section 3.1 at erflog 8, rho 0.9 and rho 1 (K' = 8 pi, K = 2 pi), in the
   order C5 (regularity of the 009 coefficient across its radial panel boundaries, which decides whether a weight that
   is constant at infinity is allowed), C3 (majorant of |a^|), C1 (SC^+), C4 (rows), then C2 (band upper). The FLOAT
   targets are in 5.1. For C2 the target is A_low^+(8 pi) <= Gbar - S^+ (0.6147 at rho 0.9, 0.6290 at rho 1), not
   A_low^+ <= SC^+.
2. The second numerics agent: an independent replay of the erflog 8 rows of Table L (rho 0.9 and 1; the low branch in boxes up to L 1056
   or more, and the disk band value at 8 pi), and the packet value at 16 pi at erflog 8, rho 1 if the GPU queue allows
   (it decides the TS route of 5.4).
3. The first theory agent: Proposition HF1-NEAR at erflog 8, rho 0.9 and 1 (near inputs in item C7, files
   runs/far_scan_ts_erflog_lam8_b14s_N2048_K8.json, near spacing 0.0300); the model prices of 5.1 are the only near
   prices available for these rows.
4. The theory auditor: the corrected certification text C0 to C2 (window handled inside HSB for the unwindowed a_f; band budget
   G - S^+), the band-budget reading of Table K, the erflog rows of Table L, and the linear transfer statement of
   section 6.
5. The coordinator: on the far side the 009 and 013 centers are equal at the resolution of the runs (section 6); the far side
   gives no reason to prefer either.

Queue (runs/scan20.sh, one job at a time on core 40; each step logged in runs/scan20.log with its real start time):
HSB at erflog 8, rho 1 with N 3072 (resolution check; done 11:16:05Z, section 5.1); the band rows of Corollary HSB-R
at erflog 8, rho 1 and 0.85 (code/hsb_band_rows.py); HSB at erflog 8, rho 0.5 and 0.6; the 16 pi band at N 4096 and
HSB with K' = 16 pi at erflog 8, rho 1; HSB at erflog 16, rho 0.5 and 0.75; HSB at log 16, rho 1.5 and 2 with
K' = 4 pi and 8 pi; the sampling check of code/hsb_check.py at log 8, rho 1. Then runs/scan21.sh: HSB at erflog 16, rho 1 (5.2) and the
row erflog 8, rho 0.95 (band, near row and HSB). New rows will be added to the tables of
section 4 in a later version or in a notes entry.

## 8. Files and runs

All paths are relative to the agent directory the second theory agent. Nothing listed here is a certificate. Several run files are still
extended by the queue of section 7, so the files used by this version were copied at assembly time to
research/h4/far009/v02_snap/ (same subdirectories code/, runs/, inputs013/). The manifest
research/h4/far009/v02_snap/SHA256SUMS lists the SHA256 of the 121 copies (sha256sum format, paths relative to the agent); its own SHA256 is
969d6895e5fa791514668bffc45ac77c681995c85cf0c38750ad2ea888e40d8e.
- Code (code/; first 16 hex digits of the SHA256 of the copies):
  - code/hsb_far.py: 619a0fb18e5641b5
  - code/hsbr_rows.py: fc9f071545c5685b
  - code/hsb_band_rows.py: 9ed12f6ecc62321e
  - code/far_box4.py: 2f339523525d1539
  - code/far_scan_ts.py: 14a95319e1ef4931
  - code/far_upper3.py: ee3d148541db4010
  - code/far_price.py: e978e0d31c4d28a5
  - code/price3.py: a61ffa81b31193e1
  - code/osc_lowpass.py: 1a16ba52a91d2713
  - code/omf_check.py: 7d2adafec38c29e8
  - code/omf_diff.py: c4f3316cc2c44c88
  - code/corr_datil.py: c895e9a7c9cf7f56
  - code/make_v02_tables2.py: b8a9c6489139c9ff
  - code/make_v02_tables3.py: 0b6bead767751840
  - code/check_rE.py: 039fa7c74d4b052e
  - code/check_upper_kernels.py: c5f19b381523f200
  - code/hsb_check.py: c3c6f1f03eb85e39
  Roles: hsb_far.py, the rows of Lemma HSB (SC, osc, the Schur rows for the five weights, the ramp configurations;
  env KPS, KFR, CORR); hsbr_rows.py, Corollary HSB-R; hsb_band_rows.py, the band-restricted rows of AT-707;
  far_box4.py, the square-band periodic band values (Lanczos; env CORR); far_scan_ts.py, the far moments, SC and the
  near inputs per split; far_upper3.py, TS3 with Lemma HB, Lemma HB' and B_nu (Table T); osc_lowpass.py (Table O);
  omf_check.py (Table W); omf_diff.py (Table D); corr_datil.py, the odd-potential correction of a snapshot (b18s2
  for 013); far_price.py and price3.py, the HF-1 model prices and the budgets (Table P); check_rE.py and
  check_upper_kernels.py, sampling checks of the remainder rE and of the closed-form kernels (not part of a proof);
  hsb_check.py, the row-regularity check (queued); make_v02_tables2.py and make_v02_tables3.py, the tables.
- Runs (runs/): hsb_<cut>_lam<lam>_<corr>_N<N>_RW50.json and the row matrices hsb_*_rows.npz (Lemma HSB rows);
  hsbr_rows.json and hsbr_rows_1118.out (HSB-R); hsb_band_rows_erflog_lam8_b14s_N512_RW50.json (route (a) trial);
  far_box2_*.json (band values, Tables B and L); far_scan_ts_*.json (far moments, SC, near inputs); far_upper3_*.json
  and far_upper3_*.out (Table T); omf_check_* (Table W); omf_diff_1054.out (Table D); osc_lowpass_1020.out (Table O);
  far_price_*_short_*.out (model prices); ahat_decay_erflog8_rho1_N4096.out (Remark 3); corr_diff_b14s_b18s2_1046.out
  (section 6); lowbr_1106.sh and lowbr_1106.log (Table L, erflog rows); scan20.sh, scan20.log and scan21.sh (the
  queue, with real start times); pauses_shift4.log (every pause of a running job by SIGSTOP and SIGCONT in this
  shift, with the reason); the two table outputs of section 4.
- Inputs: inputs013/ (the C2-N1-013 phi file and the SHA256SUMS of its snapshot).
- Assembly: scratch/h4/assemble_v02.py and the section files scratch/h4/v02/sec*.txt.
