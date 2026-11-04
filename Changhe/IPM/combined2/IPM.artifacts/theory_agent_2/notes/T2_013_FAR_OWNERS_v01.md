# T2_013_FAR_OWNERS_v01: owner table for the certified far inputs at the 013 splits erflog 8, rho 1 and log 16, rho 2

Agent the second theory agent, written 2026-11-03T13:16Z for the coordinator 11:38Z item 2(c), restated in 11:57Z item 2(d) (inputs to the
X5 reallocation) and 12:33Z item 2(c) (rows for route F-a). It takes into account the second numerics agent's band pricing (11:48Z) and
the coordinator's 11:57Z decision. Section 2.5 adds the rows for log 16, rho 2, the one split of T2_013_SPLITS_v01
(item 2(a)) that passes in FLOAT, and section 2.6 the rows of route F-a (the first theory agent's note 44, AT-911). A planning
document: nothing in it is certified. Every number is FLOAT (no bound) or HEURISTIC (a cost or a model price).
Paths are relative to research/h4/far009/ of agent the second theory agent unless another agent is named. Formulas and lemma names refer
to T2_FAR_v02 (notes/T2_FAR_v02.md, frozen 11:21:04Z) and to THEORY_NEW_RESULTS.md version 9 (NR-21 to NR-23).

## 1. The inequality to certify (direct 013 route)

Coefficient. a_f = chi(|x|) atil_013(x) on R^2, unwindowed, with all angular modes, where
- chi(r) = (1/2) (1 + erf(log(r/(rho lam^(1/2))) / (log(lam)/(2 pi^(1/2))))) with lam = 8, rho = 1 (the erflog cut of
  code/hsb_far.py, function cutf);
- atil_013 = (4 ubar.X - c)/(1 + 4|X|^2) with ubar = u_007 + (-phi_xy, phi_xx);
- u_007 is the unchanged Candidate 007 velocity (closed form: 2982 exact generators in data/C1-N1-007_exact.json);
- phi is the exact C2-N1-013 correction (12273 exact atoms; inputs013/phi_007_b18s2_phi_exact.json, SHA256
  a16e9d85..., the raw correction hash of the theory auditor's SOURCE013_CHAIN_CONDITIONS_v01).
So a_f has an analytic representation from exact JSON inputs. python-flint 0.9.0 (arb) is present in the shared
interpreter, so no installation is needed for interval evaluation.

Certified statement wanted. With (K, K') = (2 pi, 8 pi) and a weight h, Lemma HSB (T2_FAR_v02 section 2.3; the case B
form of NR-21, PROVED conditionally) gives the far constant of a_f at most max(SC^+, A_low^+(K')) + S^+. The split
is admissible at the strain target 3/2 when

  SC^+ <= Gbar - S^+  and  A_low^+(K') <= Gbar - S^+,   Gbar = q (c - 3/2) = 14674311533937489/22517998136852480,

or when the row-wise form of Corollary HSB-R is at most Gbar with the same certified pieces.

FLOAT reference values (013, N 2048, window 50/10, 8 angular modes; runs/hsb_erflog_lam8_b18s2_N2048_RW50.json and
runs/hsbr_rows_1127.out): SC 0.4598 (N 3072: 0.4608), band value 0.3848 (8 pi), S_h^B 0.0227 (Perron weight) and
0.0262 (h = 1), HSB 0.4825, HSB-R 0.4766, Gbar = 0.65167. Rooms at S = 0.0227: Gbar - S - SC = 0.1692 and
Gbar - S - band = 0.2442.

## 2. Owner table

"Confirmed" in the cost column means confirmed by the named owner. For rows whose owner is not the second theory agent the cost is a
pointer to the owner's own answer, or "to state". Costs are in hours of one agent's work (code and proofs) and in
core-hours (runs on one core).

### 2.1 Direct route (Lemma HSB, K' = 8 pi, K = 2 pi)

| ID | required inequality or hypothesis | FLOAT reference and room | proposed producer | HEURISTIC cost | audit dependency |
|---|---|---|---|---|---|
| D0 | Identity and arithmetic. Every certified number of this table is computed from the bound 013 identity (raw correction hash a16e9d85..., complete-field hash 3d5f08e0...) and the unchanged 007 exact JSON, in a containing arithmetic (arb balls or directed rounding). No binary64 table of this agent enters a certified number (AT-819 to AT-821). | none | every producer | inside each row | The theory auditor: one manifest binding per production job |
| C5a | a_f is real, bounded, and even in x_1 and in x_2, so that only cos(2k theta) modes occur and xi may be restricted to the closed first quadrant (v02 C4 (i)). For the 013 part this follows from the atoms: every atom has odd n and the factor sin(n theta), so phi is even in x_1 and odd in x_2; then v_1 = -phi_xy is odd in x_1 and even in x_2, v_2 = phi_xx is even in x_1 and odd in x_2, and v.X = x_1 v_1 + x_2 v_2 is even in both. For the 007 part, the same statement read off the generator list. | structural | The second theory agent | 1 hour; confirmed | The theory auditor |
| C5b | Hypotheses of NR-21 case B: a^ is a function with int \|a^\| (1 + \|zeta\|^2) finite, plus the two necessary and sufficient decay conditions of v02 Remark 3 of section 2.3 for the chosen weight (AT-797, AT-798). Route: a_f is C-infinity on R^2 (the erflog cut vanishes faster than every power of r at r = 0; the generators and atoms are smooth for r > 0), and D^j a_f = O(r^(-gamma - j)) at infinity with gamma near 0.448 (the second numerics agent, FLOAT), so Delta^j a_f is integrable for j >= 1 and \|a^(zeta)\| <= \|\|Delta^j a_f\|\|_1 \|zeta\|^(-2j) for every j >= 1; near zeta = 0, \|a^\| is of order \|zeta\|^(gamma - 2), which is integrable. Then both conditions hold for every s >= 0, including h = 1 and the Perron weight extended constantly. This removes, for the analytic representation, the obstacle of AT-800 (no decay envelope for the spline field). | FLOAT decay of the sampled field: v02 Remark 3 (local slopes -6 to -12 for 6 < \|zeta\| < 40) | The second theory agent (the argument, and explicit constants for the exterior and large-\|zeta\| bounds from the exponents of the generators and atoms) | 4 hours (1.5 for the argument, 2.5 for the explicit constants); confirmed | The theory auditor |
| C0 | Window and angular truncation. Every certified number (C1 to C4) is for the unwindowed a_f with all angular modes. The window Rw 50, Ww 10 of the FLOAT runs is a computational device only, so on this route no window-removal certificate is needed. The exterior r > R_ext enters C1 through certified bounds of D^2 a_f and C3 through the transform of the asymptotic profile. Angular truncation: a_f has finitely many angular modes (the 007 generators have angular order at most 79; the 013 atoms have odd n <= 159, so the 013 part of a_f has modes cos(2k theta) with 2k <= 160). A certified computation either keeps every mode (then no truncation error exists, at a cost proportional to the mode count in C1 and C3) or truncates at k0 and adds a certified bound of the omitted modes, for the field, its second derivatives (C1) and its transform (C3). | Omitted modes of the FLOAT runs (k >= 8; code/mode_tail013.py, runs/mode_tail013_1203.out; sampled sums on the 1200-radius grid, not bounds): for the total 013 coefficient, sup of cut times the sum of \|F_k\| over k >= 8 is 7.4e-5 (at r 211) and 1.0e-6 over k >= 16; with the weight (2k)^2/r^2 of the angular second derivatives, 1.6e-3 (at r 2.34) and 8.2e-5. The 007 part alone has a k >= 8 tail of 9.0e-4 (weighted 9.1e-2); the 013 correction has a tail of almost the same size (8.8e-4, weighted 9.0e-2) that cancels it in the sum. So a truncated certificate must bound the omitted modes of the sum, not of the two parts separately. The second numerics agent finds a mode-truncation effect of 2e-6 on the band value at a log row (009, all 88 modes). | The second theory agent (inside C1 and C3) | inside C1 and C3; keeping all modes multiplies the C3 run time by about the mode count over 8 | The theory auditor |
| C0-W | Only if a producer uses a windowed form a_W = a_f (1 - Sinf((r - Rw)/Ww)): a separate certified window removal A(a_f) <= A(a_W) + OMF(a_t), a_t = a_f - a_W (the split of route F-a, AT-911; the moments are part of the charge, AT-917). No lemma charges a slowly varying tail only at its own scale. FLOAT full tail charges (code/tail_omf.py, T2_013_SPLITS_v01 section 4): 0.751, 0.266, 0.148 at Rw 50, 100, 200 with Ww = Rw/5, and 0.227, 0.154, 0.109 with Ww = Rw, against the room Gbar - S_h^B - max(SC, band) = 0.1692 at this split. | fits at Rw 200 with Ww = Rw/5 (margin 0.021) and at Rw 100 and 200 with Ww = Rw (margins 0.015 and 0.060), if SC, band and S_h^B of the larger a_W stay at their Rw 50 values (not computed for S_h^B); the band problem of C2 then lives on r <= Rw + Ww (Landau order larger by ((Rw + Ww)/60)^2, 11 to 44) | not recommended for C1, C3, C4; C2 cannot avoid it (see C2) | not priced | The theory auditor |
| C1 | SC^+ >= sup over x in R^2 of max(0, (1/2)[(q^2 - 1) lambda_max D^2 a_f(x) + Delta a_f(x)]), with SC^+ <= Gbar - S^+. Method: radial panels. On each panel [r_i, r_(i+1)] with r_(i+1) <= R_ext, arb enclosures of the mode functions f_k and of f_k', f_k'' (from the closed forms of the generators and atoms), then a bound of the Hessian expression over theta from the mode sums; for r > R_ext the decay bounds of C5b. A two-dimensional branch and bound on (r, theta) boxes is the fallback. | SC 0.4598 (N 2048), 0.4608 (N 3072); room Gbar - S - SC 0.1692 at S = 0.0227 | The second theory agent (arb evaluation from the exact JSONs; independent of the numerical auditor's panels), or the numerical auditor's 013 complete-field evaluator if it supplies velocity derivatives to order 4 | The second theory agent: 6 hours of code (confirmed); run 3 to 30 core-hours (estimate). Measured: one arb evaluation of datil_013 at a point costs 0.458 s for the 12273 atoms at 128 bits (parsing 0.16 s; runs/arb_cost013_1203.out, code/arb_cost013.py); the panel count and the cost of derivative jets are not measured | The theory auditor (method and manifest) |
| C3 | A measurable majorant m(zeta) >= \|a^(zeta)\| on R^2, and signed enclosures of a^ with a modulus of continuity (needed by C2). Method: polar form. For a_f = sum_k f_k(r) cos(2k theta), a^(zeta) = 2 pi sum_k (-1)^k cos(2k omega) H_2k[f_k](\|zeta\|) with H_n[f](t) = int_0^infinity f(r) J_n(t r) r dr (omega the polar angle of zeta). Then m(zeta) = 2 pi sum_k \|H_2k[f_k](\|zeta\|)\| is a radial majorant. H_2k[f_k] on r <= R_ext by certified quadrature (arb), the part r > R_ext from the asymptotic profile (closed-form transforms of powers plus a remainder bound), large t from the bound of C5b, the omitted modes from C0, and continuity in t from bounds of d/dt on panels. One deliverable serves C2, C4, T2, T3 and X2. | not computed; a FLOAT check that the radial majorant keeps S near 0.0227 and E near 0.0211 is not yet run | The second theory agent | FLOAT check 4 hours (confirmed); certified version 16 to 30 hours of code (estimate) plus 4 to 10 core-hours with 8 modes, more with all modes | The theory auditor |
| C4 | S^+ >= sup over xi of rho_h^B(xi) (or the rows of Corollary HSB-R), computed with m of C3 in place of \|a^\|. Inputs (i) to (v) of v02 C4. With h = 1 the weight inputs (iv) disappear at a cost of 0.0035 in FLOAT. | S_h^B 0.0227 (Perron), 0.0262 (h = 1); S^+ may be as large as Gbar - max(SC^+, A_low^+), 0.19 at the FLOAT values | The second theory agent | 8 hours of code (confirmed); 1 to 4 core-hours (estimate) | The theory auditor |
| C2 | A_low^+(K') >= A_low(K'), the continuum band constant of the unwindowed complete form on the disk \|xi\| <= K', with A_low^+ <= Gbar - S^+. None of the absolute-kernel uppers evaluated so far fits (FLOAT): route (a) with the part_tau1_p2 multipliers is at least its oscillation charge O (floor CONFIRMED for that family, AT-882 to AT-885; O = osc(a_f) = 0.771 sampled), the low-pass route is at least osc(phi * a_f), 0.604 to 0.763 for K'' = 1 to 2 pi (NR-24, CONFIRMED with repairs, v282), OMF 3.81, TII-1 with CAW-F 6.2, against the budget 0.629. So the sign structure must enter. The second numerics agent's construction is a finite symmetric eigenproblem with a certified upper of its top eigenvalue, a projection error and the window charge of C0-W. Structural upper certificates of much smaller cost than a dense factorization are admissible in principle (AT-874, AT-875: a diagonal-plus-low-rank test, or a Ritz vector with a verified residual and a complement upper); none has been shown for this operator. | 8 pi: band value 0.3848 (L 128), 0.38476 (box and window changes below 2e-4, the second numerics agent); room 0.2442 at S = 0.0227. Smaller K' in section 2.4 | The second numerics agent (coordinator 11:38Z item 2(b)) | owner's answer (the second numerics agent 11:48Z, results/N2_BAND_PRICE_013_v01.md in agent the second numerics agent): the dense construction cannot finish before the stop (matrix order at least 1.1e6 at Rw 100 against an arb reach of about 1e4). This is a HEURISTIC implementation assessment, not an exclusion (AT-873 to AT-875). OPEN; no route (b) computation scheduled (coordinator 11:57Z) | The theory auditor (method acceptance) |
| C6 | Strain: a certified global strain bound s_* <= 3/2, so that G = Gbar; in general a certified s_* <= c - A^+/q for the certified far value A^+ (AT-858, AT-860). | far level c - HSB-R/q = 1.5834 (013), 0.0834 above 3/2 | The numerical auditor (cover; coordinator 11:25Z item 3(c)) | The numerical auditor to state | The theory auditor |
| C7 | Near side at the same split (HF1-NEAR, tail B, erflog 8, rho 1; PROVED conditionally, AT-691, AT-757). | P_HF B / P_B at the 013 budget: 0.09 / 0.17 of D (the first theory agent's note 40) | The first theory agent (coordinator 11:38Z item 2(d); the first theory agent's note 43 item 5 is that owner table) | The first theory agent to state | The theory auditor |
| F | Assembly: exact rational comparison of max(SC^+, A_low^+) + S^+ (or the HSB-R row maximum) with Gbar, and the statement of the far theorem with its hypotheses. | HSB-R 0.4766 against 0.65167 | The second theory agent | 1 hour; confirmed | The theory auditor |

### 2.2 Transfer route (AT-808), for comparison

| ID | required inequality or hypothesis | FLOAT reference and room | proposed producer | HEURISTIC cost | audit dependency |
|---|---|---|---|---|---|
| X1 | A certified upper A^+(009) of the complete 009 far form at the same split and test space. AT-808 transfers complete-form or common-band uppers, not the Schur costs one by one, so X1 needs rows C0 to C5 for 009 (b14s atoms) in full, including C2 for 009. | 009 HSB-R 0.47659508 against 0.47660915 for 013 | as C0 to C5 | the same as the direct route (the 007 part is common and only the correction atoms differ), so C2 blocks it in the same way | The theory auditor |
| X2 | E^+ >= osc(d) + M2(d) + (q^2/2) M2[w_new](d) for the difference d = chi (atil_013 - atil_009) = chi 4 (v_013 - v_009).X/(1 + 4\|X\|^2), same cut and window as X1 (unwindowed on this route), with the accepted OMF moment hypotheses. Method: arb evaluation of the two closed-form atom lists; osc(d) from interval bounds of d; M2 and M2[w_new] from integrals of \|zeta\|^2 \|d^\| bounded through L^2 norms of derivatives of d up to order 4 (Cauchy-Schwarz with an explicit radial weight; NR-25 of the first theory agent has this form), each an integral of a closed-form function with tail bounds from the atom exponents. | OMF(d_f) 7.08e-4 at rho 1 (window 50/10, N 2048, v02 Table D); 99 percent of it from \|zeta\| > 20 on the grid | The second theory agent, or the numerical auditor (the second numerics agent 11:48Z item 4: "the numerical auditor, hours") | The second theory agent: 8 to 16 hours of code (confirmed); 2 to 6 core-hours (estimate; 12273 atoms of 013 plus the 009 atoms) | The theory auditor (AT-808 hypotheses) |
| X3 | Window: X1 and X2 with the same cut and window. A windowed X1 needs C0-W, which is infeasible at Rw 50 for both widths computed. | as C0-W | none | none | The theory auditor |

The transfer charge is small (7.1e-4 against the far margin 0.175), but the route is never cheaper than the direct
one: X1 is the direct route for 009. It becomes useful only if a certified 009 far upper at this split exists for
another reason, and none is scheduled.

### 2.3 TS fallback at K' = 16 pi (T2_FAR_v02 section 5.4), conditional

TS: A = max(A_low^+(K'), A_hi^+(K)) + E^+(K, K') with K' = 16 pi, K = 20.84 (Proposition TS with Lemma HB and Lemma
HB'). It needs no SC^+ and no Schur rows. The condition of v02 section 5.4 (16 pi band value at most A_hi = 0.5819)
holds in FLOAT: the second numerics agent 11:34Z item 1 gives 0.42595. So TS3 = A_hi + E = 0.6030 in FLOAT, a far margin of 0.049
(against 0.175 for HSB-R).

| ID | required inequality or hypothesis | FLOAT reference and room | proposed producer | HEURISTIC cost | audit dependency |
|---|---|---|---|---|---|
| T1 | Band upper A_low^+(16 pi) <= Gbar - E^+. | band value 0.42595 (the second numerics agent); budget 0.6306; room 0.205 | The second numerics agent (as C2, on four times the area of the 8 pi disk) | The second numerics agent 11:48Z: four times the problem of C2; OPEN | The theory auditor |
| T2 | IMS error E^+(K, K') >= (2 pi)^-2 int m(zeta) eI(\|zeta\|) d zeta, m of C3. | E 0.0211 | The second theory agent | 2 hours after C3 (confirmed) | The theory auditor |
| T3 | High band A_hi^+(K) by Lemma HB': Lambda_+^+ >= sup_x lambda_max D^2 a_f (the radial-panel sweep of C1 without the Laplacian term) and the remainder integrals of Lemma HB' from m, with the minimum rE of AT-688, AT-733 (it belongs to this high-band remainder, not to the IMS error of T2, AT-860). A_hi^+ <= Gbar - E^+ is the tight condition: A_hi 0.5819 against 0.6306, and the principal factor (1/2)(1 + K^-2 + q^2) is 2.70615, so Lambda_+^+ may exceed its FLOAT value 0.2110 by at most 0.018 (8.5 percent) at the FLOAT remainders. | Lambda_+ 0.2110, A_hi 0.5819, room 0.0487 | The second theory agent | 4 hours after C1 and C3 (confirmed) | The theory auditor |
| T4 | C0, C5, C6, C7 as for the direct route. | | as above | as above | The theory auditor |

TS replaces C1 and C4 by T2 and T3 and keeps a band certificate, on four times the area; its band certificate T1 is
blocked as C2 is.

### 2.4 Smaller band radius K' (FLOAT, 013, erflog 8, rho 1)

Rows of code/kp_table.py (runs/kp_table_1204.out) from runs/kp_1149.sh (log runs/kp_1149.log; far_box4 band values at
kmax = K', L 128, N 2048, window 50/10; hsb_far with KPS = 2pi, 3pi, 4pi, 6pi, output
runs/hsb_erflog_lam8_b18s2_N2048_RW50_kp.json) and runs/hsbr_rows_kp_1203.out (Corollary HSB-R). SC = 0.4598 at every
row. The first theory agent's note 43 item 3 reproduces the 2 pi and 4 pi rows with the same code.

| K' | K | band value | S_h^B (weight) | HSB | HSB-R | Gbar - S - SC | Gbar - S - band | disk area / area at 8 pi |
|---|---|---|---|---|---|---|---|---|
| 2 pi | 1.571 | 0.2635 | 0.1834 (perron) | 0.6432 | 0.6180 | 0.0084 | 0.2048 | 0.062 |
| 2 pi | 3.142 | 0.2635 | 0.2016 (perron) | 0.6614 | 0.6613 | -0.0098 | 0.1866 | 0.062 |
| 3 pi | 2.356 | 0.2682 | 0.1092 (perron) | 0.5690 | 0.5479 | 0.0826 | 0.2743 | 0.141 |
| 3 pi | 4.712 | 0.2682 | 0.1310 (perron) | 0.5908 | 0.5906 | 0.0609 | 0.2525 | 0.141 |
| 4 pi | 3.142 | 0.3042 | 0.0712 (perron) | 0.5310 | 0.5162 | 0.1207 | 0.2763 | 0.250 |
| 4 pi | 6.283 | 0.3042 | 0.0925 (perron) | 0.5523 | 0.5445 | 0.0994 | 0.2549 | 0.250 |
| 6 pi | 4.712 | 0.3572 | 0.0370 (perron) | 0.4968 | 0.4877 | 0.1549 | 0.2575 | 0.562 |
| 6 pi | 9.425 | 0.3572 | 0.0538 (perron) | 0.5136 | 0.5066 | 0.1380 | 0.2407 | 0.562 |
| 8 pi | 6.283 | 0.3848 | 0.0227 (perron) | 0.4825 | 0.4766 | 0.1692 | 0.2442 | 1.000 |

Readings. S_h^B grows quickly as K' decreases (the Schur rows see more of a^ outside the band), and the band value
falls. The band room Gbar - S - band is largest at 3 pi and 4 pi (0.274 and 0.276, against 0.244 at 8 pi), and the
SC margin Gbar - S - SC falls from 0.169 (8 pi) to 0.121 (4 pi), 0.083 (3 pi) and 0.008 (2 pi). So K' = 4 pi keeps a
SC margin of 0.12 and gives a band disk of one quarter of the area, hence a Landau-Pollak order one quarter of the
8 pi order (the first theory agent's note 43: 3.6e4 at 4 pi against 1.4e5 at 8 pi for X = 60, after the parity factor 4). That is still
above the order of about 1e4 that the second numerics agent gives for certified dense tools, and it does not change C0-W, so it does
not unblock C2. The second numerics agent 11:48Z item 3 reads K' below 8 pi as leaving no room; on these rows every sampled margin is
positive, and at 2 pi it is only a narrow positive sampled margin, 0.0084 (the theory auditor AT-901 replays the 2 pi, 4 pi and 8 pi
margins 0.00844454, 0.12068294 and 0.16916922 from the saved arrays).

### 2.5 The split log 16, rho 2 (the coordinator 11:57Z item 2(c): rows for a split that passes in item 2(a))

Split: chi(r) = Sinf(log(r/rho)/log(lam)) with lam = 16, rho = 2 (the log cut of code/hsb_far.py, function cutf), so
chi = 0 for r <= 2 and chi = 1 for r >= 32. Same coefficient atil_013, K' = 8 pi, K = 2 pi. FLOAT values (013, N 2048,
window 50/10; T2_013_SPLITS_v01): osc 0.4704, SC 0.1001, route (a) A_E 0.5659 (tau 2, Schur weight s = 1.5; the
leading term is the floor O = 0.4704, so the integral part is 0.0955), S_h^B 0.0066 (Perron weight), HSB 0.5725, far
margin 0.0792; Lemma HS (part_tau1_p2): osc + S_HS = 0.4704 + 0.1128 = 0.5832, margin 0.0685. Two certified routes
are possible; neither has an eigenproblem.

| ID | required inequality or hypothesis | FLOAT reference and room | proposed producer | HEURISTIC cost | audit dependency |
|---|---|---|---|---|---|
| L0 | D0, C5a and C5b of section 2.1 for this cut. The log cut is C-infinity on R^2 and vanishes on r <= 2 (Sinf is smooth and flat at both ends), so the argument of C5b holds unchanged and is simpler near r = 0. | structural | The second theory agent | as C5a, C5b (5 hours); confirmed | The theory auditor |
| L0-W | Window, as C0 (unwindowed a_f through m of C3) and C0-W. Beyond r = 32 the cut is 1, so a_f - a_W is the same far piece as at erflog 8, rho 1, and the full tail charges (0.751, 0.266, 0.148 at Rw 50, 100, 200 with Ww = Rw/5; 0.227, 0.154, 0.109 with Ww = Rw) all exceed the margin 0.079. So the windowed form is not available on this split at any of these Rw. | C0-W infeasible here | The second theory agent (inside L1 to L3) | inside L2 and L3 | The theory auditor |
| L1 | Route HSB: SC^+ <= Gbar - S^+ (method of C1). | SC 0.1001; room 0.545; not binding | The second theory agent | as C1 (6 hours of code), with fewer panels because of the room | The theory auditor |
| L2 | Route HSB: A_E^+ >= the route (a) upper of AT-707 (family part_tau1_p2, tau and the Schur weight fixed in advance) for the unwindowed a_f, with m of C3 in place of \|a^\| in every integral, and O^+ >= O. O may be the actual osc(a_f) or an admitted upper of it used consistently in the decomposition (the theory auditor, AT-882 to AT-885), so O^+ may be an interval upper of osc(a_f) (the C1 panels without the Hessian); the min(osc(a), osc(P a)) option of AT-707 is then not needed, and no sampled identity has to be proved. A_E^+ <= Gbar - S^+ is the tight condition. | A_E 0.5659 (O 0.4704 plus integrals 0.0955); room 0.0792 at S = 0.0066: the integrals may grow by a factor 1.8, or O^+ may exceed the sampled osc by 0.079 | The second theory agent | 8 to 12 hours of code after C3 (estimate); runs inside C3's | The theory auditor (AT-707 hypotheses with m) |
| L3 | Route HSB: S^+ (method of C4) with m. | S_h^B 0.0066; room large | The second theory agent | as C4 (8 hours) | The theory auditor |
| L2' | Route HS instead of L1 to L3: osc^+ + S_HS^+ <= Gbar for Lemma HS of the first theory agent (AT-756) with the part_tau1_p2 split, osc^+ an interval upper of osc(a_f), S_HS^+ from m. No band and no SC^+. | 0.5832; room 0.0685 | The second theory agent | osc^+ about 3 hours of code (the C1 panels without derivatives of order 2), S_HS^+ about 8 hours after C3 (estimate) | The theory auditor (Lemma HS) |
| L5 | Strain C6 at this split: far level c - A^+/q; at the FLOAT value 1.5377, 0.038 above 3/2. | margin 0.079 as in L2 | The numerical auditor | The numerical auditor to state | The theory auditor |
| L6 | Near side C7 at log 16, rho 2 (HF1-NEAR, tail B, at the larger near inputs sup- 35.7, sup+ 53.2, L1+ 31.0). | P_HF B / D 0.57 and P_B / D 1.02 (this agent's replay of the first theory agent's model, T2_013_SPLITS_v01 section 5) | The first theory agent | The first theory agent to state | The theory auditor |
| L7 | Assembly, as F. | HSB 0.5725 or HS 0.5832 against 0.65167 | The second theory agent | 1 hour; confirmed | The theory auditor |

Total for the second theory agent on route HSB: L0 5, L1 6, C3 16 to 30, L2 8 to 12, L3 8, L7 1, that is 44 to 62 hours of one agent's
work plus runs. On route HS: L0 5, osc^+ 3, C3 16 to 30, S_HS^+ 8, L7 1, that is 33 to 47 hours. Both exceed the
about 28 hours left before the team stop. Both routes contain C3 (the majorant m), which is the expensive row.

### 2.6 Route F-a at erflog 8, rho 1 (the first theory agent's note 44 item 1, AT-911; the coordinator 12:33Z item 2(c))

Route F-a: with a_f = a_W + a_t, a_W = a_f (1 - Sinf((r - Rw)/Ww)) (Ww = Rw/5 in note 44; Ww = Rw is also computed), the far constant of a_f is at most
max(SC^+, A_E^+(a_W)) + S^+(a_W) + OMF^+(a_t), where A_E is the route (a) band upper of a_W and OMF(a_t) is the full
charge osc + M2 + (q^2/2) M2[w_new] of the tail (AT-911: CONFIRMED conditionally, for a common test space and H^-1
normalization with matched coefficient hypotheses; AT-917: the moments are part of the charge). It is admissible at a
certified strain bound s^+ when this sum is at most G = q (c - s^+); at s^+ = 1.096, G = 1.500070. No eigenvalue
upper enters. FLOAT column of T2_013_SPLITS_v01 section 4 (013 coefficient): with the width Ww = Rw/5 of note 44, the far value at erflog 8, rho 1 is 1.9103 at Rw 50 and 1.4227 at Rw 100, against G(1.096) = 1.500070, that is margins -0.4103 and 0.0774 (strain levels 0.9006 and 1.1328). With the wider transition Ww = Rw it is 1.3842 at Rw 50 (margin 0.1158, level 1.1512; S_h^B of Ww 10), because the moments of the tail charge come from the window transition. At log 16, rho 2 (Ww = Rw/5) the route gives 1.3232 and 0.8142 (levels 1.1802 and 1.4226). At strain 3/2 it fails at both splits, since A_E alone exceeds Gbar.

| ID | required inequality or hypothesis | FLOAT reference and room | proposed producer | HEURISTIC cost | audit dependency |
|---|---|---|---|---|---|
| FA0 | D0, C5a and C5b of section 2.1 for a_f, and the same for a_W and a_t (the window factor Sinf is C-infinity, so smoothness and the symmetry of C5a are kept). | structural | The second theory agent | as C5a, C5b (5 hours) | The theory auditor |
| FA1 | SC^+ (C1). On this route SC enters only through max(SC^+, A_E^+), and A_E^+ is far above SC, so a crude SC^+ suffices. | SC 0.4598 against A_E 1.1369 (Rw 50), 1.1345 (Rw 100), 1.1343 (Rw 50, Ww 50) | The second theory agent | as C1, with coarse panels | The theory auditor |
| FA2 | C3 for the windowed piece: a measurable majorant m_W >= \|a_W^\| with a modulus of continuity in xi (needed by the sup over xi in A_E and S). a_W vanishes for r >= Rw + Ww, so the Hankel integrals H_2k[f_k] have a finite range and the asymptotic profile of C3 is not needed; large \|zeta\| from derivative bounds of a_W. | not computed | The second theory agent | 12 to 24 hours of code (estimate), less than C3 for the unwindowed a_f; the quadrature cost grows with Rw (oscillation of J_2k(t r) for t r up to 2 K' (Rw + Ww)) | The theory auditor |
| FA3 | A_E^+(a_W): route (a) of AT-707 (family part_tau1_p2, tau and the Schur weight fixed in advance) with m_W in place of \|a_W^\|, and O^+ an interval upper of osc(a_W) used consistently (AT-882 to AT-885). | A_E (013): 1.1369 at Rw 50 (N 2048) and 1.1345 at Rw 100 (N 4096) with Ww = Rw/5, and 1.1343 at Rw 50 with Ww = Rw (N 3456), all at grid step 0.064, tau 1, Schur weight 1.5; the lead O = osc(a_W) = 0.7711 is attained near the cut, so the integral part (about 0.363 to 0.366) carries the majorant inflation | The second theory agent | 8 to 12 hours of code after FA2 (estimate) | The theory auditor |
| FA4 | S^+(a_W): C4 with m_W at the same Rw. | S_h^B: 0.0227 at Rw 50, Ww 10 (Perron weight); 0.0226 at Rw 100, Ww 20 (N 4096); Ww = Rw not computed | The second theory agent | as C4 (8 hours) | The theory auditor |
| FA5 | OMF^+(a_t) = osc^+(a_t) + M2^+(a_t) + (q^2/2) M2[w_new]^+(a_t), with the accepted OMF hypotheses (AT-665). osc^+ from interval panels on [Rw, R_ext] and the decay bounds of C5b beyond R_ext. M2^+ and M2[w_new]^+ through weighted L^2 norms of derivatives of a_t up to order 4 (Cauchy-Schwarz with an explicit radial weight; the method of X2 and of the first theory agent's NR-25). The tail is not compactly supported: every integral needs the exterior decay bounds of C5b (D^j a_f = O(r^(-gamma - j)), gamma near 0.448), which make the derivative norms of order j >= 1 finite. | FLOAT (code/tail_omf.py): with Ww = Rw/5: OMF(a_t) 0.7507, 0.2656, 0.1484 at Rw 50, 100, 200 (osc 0.2649, 0.1889, 0.1354; M2 0.1315, 0.0228, 0.0040; M2[w_new] 0.1607, 0.0244, 0.0041; Ro = 4 Rw, N 2048), moments 1.83, 0.41 and 0.10 times the oscillation, from the window transition; with Ww = Rw: 0.2273, 0.1542, 0.1094 (moments 0.016, 0.003, 0.0005). At N 4096 with Ro = 2, 4 and 7 Rw (Ww = Rw/5) the charge is 0.7575, 0.7515 and 0.7503 at Rw 50, 0.2666, 0.2656 and 0.2654 at Rw 100, and 0.1485, 0.1484 and 0.1483 at Rw 200 (runs/splitG_1245.log): halving the grid step at Ro = 4 Rw moves it by at most 0.0008, and Ro = 7 Rw moves it by at most 0.0012 more; the far-out cut at Ro = 2 Rw adds its own transition (0.007 at Rw 50). | The second theory agent (or the numerical auditor for the norms) | 8 to 16 hours of code (estimate) plus runs | The theory auditor |
| FA6 | Window removal: on this route the split a_f = a_W + a_t is the removal; no further window row (C0-W is replaced by FA5). | | | | The theory auditor (AT-911) |
| FA7 | Strain: a certified s^+ with A^+ <= q (c - s^+); at the FLOAT values of section 4, s^+ = 1.096 suffices at Rw 100 with Ww = Rw/5 and at Rw 50 with Ww = Rw, and not at Rw 50 with Ww = Rw/5; 3/2 suffices at no computed Rw or Ww. | level c - A/q: 0.9006 at Rw 50 and 1.1328 at Rw 100 (Ww = Rw/5), 1.1512 at Rw 50 with Ww = Rw (G(1.096) - A = -0.4103, 0.0774, 0.1158) | The numerical auditor | numerical audit exchange v184: no more than at 3/2 if the same containing cover lies below 1.096, otherwise unknown; the FLOAT sup 0.8103 of the strain does not price the cover | The theory auditor |
| FA8 | Near side C7 at erflog 8, rho 1, unchanged (the first theory agent's note 44: no near input depends on G). | P_HF B / P_B 0.09 / 0.17 of D | The first theory agent | The first theory agent to state | The theory auditor |
| FA9 | Assembly, as F, with the comparison against q (c - s^+). | | The second theory agent | 1 hour | The theory auditor |

Total for the second theory agent on route F-a: FA0 5, FA1 3 to 6, FA2 12 to 24, FA3 8 to 12, FA4 8, FA5 8 to 16, FA9 1, that is 45 to 72
hours of one agent's work plus runs, and a certified strain cover at 1.096 (the numerical auditor). It avoids the eigenproblem of C2
and the window problem of C0-W, at the price of the strain target. It is above the time left.

## 3. Readings

1. C2 (and T1) is the blocking row. Every far route at this split needs a certified band upper: the direct route
   (C2), the transfer route (X1 contains C2 for 009) and the TS fallback (T1, four times the area). The second numerics agent's answer
   (11:48Z) is that no construction of A_low^+(8 pi) <= Gbar - S^+ can finish before the stop. The coordinator
   (11:57Z) schedules no route (b) computation. The theory auditor (v279, AT-873 to AT-875) classifies that answer as a HEURISTIC
   implementation assessment: structural upper certificates of smaller cost are admissible, but none has been shown
   for this operator. So no row of this table closes the far side at erflog 8, rho 1 before the stop unless such a
   certificate or a theory result of coordinator 11:57Z item 2(b) changes C2. The rows other than C2 and T1 are
   priced so that their cost is known if that happens.
2. What the second theory agent can certify alone, and what it is worth. C5a, C5b, C1 and F do not depend on C2 or C3: 12 hours of code
   (1 + 4 + 6 + 1) plus 3 to 30 core-hours. They would give a certified SC^+ and the hypotheses of NR-21 case B for
   the 013 far piece. With C3 and C4 (another 24 to 38 hours of code), they would reduce the far theorem at this split
   to the single open inequality A_low^+(8 pi) <= Gbar - S^+. The total for the second theory agent's direct-route rows is 36 to 50
   hours of one agent's work plus the runs, more than the about 28 hours left before the team stop (2026-11-04T17:05:30Z).
   The second theory agent's recommendation for X5: do not allocate the far certificate at this split as a closure path. If a partial
   certified far result is wanted, the best value per hour is C5a, C5b and C1 (SC^+ <= Gbar - S^+ is then certified
   with the FLOAT S, and the remaining hypotheses are named).
3. The shared deliverable. C3 (the majorant m of |a^| and the signed enclosures) feeds C2, C4, T2, T3 and X2, so it is
   on the path of every route. It is also the most expensive the second theory agent row (16 to 30 hours of code). It has no value
   while C2 is blocked, except for X2 (the AT-808 charge), which the second numerics agent lists as feasible in hours.
4. The transfer route is not cheaper. X1 is the direct route for 009, so the transfer only adds X2. The FLOAT charge
   E(d) = 7.1e-4 is small against the margin 0.175, but it saves nothing while no 009 far certificate exists.
5. Windowed forms. C0-W prices the window removal by the full tail charge OMF(a_t) (AT-911, AT-917). The room on the
   HSB route at 8 pi is Gbar - S_h^B - max(SC, band) = 0.1692. With Ww = Rw/5 the charge is 0.751, 0.266 and 0.148
   at Rw 50, 100 and 200, so it fits only at Rw 200 (margin 0.021); with the wide window Ww = Rw it is 0.227, 0.154
   and 0.109, so it fits at Rw 100 (margin 0.015) and 200 (margin 0.060). These margins hold only if SC, the band
   value and S_h^B of the larger piece a_W stay at their Rw 50 values (the second numerics agent 11:33Z: band packet values move by 2e-4
   between Rw 50 and 200; S_h^B at larger Rw not computed). The price is in C2: the windowed band problem then lives
   on the support r <= Rw + Ww, which raises its Landau order by ((Rw + Ww)/60)^2, a factor 16 at Rw 200, Ww 40 and
   11 at Rw 100, Ww 100. On the direct route C1, C3 and C4 work with the unwindowed coefficient and need no window
   removal; C2 cannot avoid a window at present, which is part of why it is blocked.
6. Angular truncation. The FLOAT runs keep 8 modes; the omitted modes of the total 013 coefficient are small (7.4e-5
   in value, 1.6e-3 in the angular second-derivative scale), because the correction cancels the high modes of 007
   (each part alone has a tail of about 9e-4). A certificate must bound the omitted modes of the sum, or keep all
   modes (finitely many: 2k <= 160 for the 013 part).
7. Independence. C1 and C5 use arb evaluation from the exact JSONs (007 generators and 013 atoms), measured at 0.458 s
   per point for the 013 atoms. They do not depend on the numerical auditor's 013 panels; the identity binding (D0) is the theory auditor's.
8. Smaller K' (section 2.4). K' = 4 pi keeps an SC margin of 0.12 with a quarter of the band area. It lowers the order
   of the band eigenproblem by a factor of 4 but not below the reach that the second numerics agent gives, and it leaves C0-W unchanged.
   It is a useful configuration if a structural band certificate appears, because that certificate would then be
   needed on a smaller disk.
9. Separated target (coordinator 11:38Z item 2(a)). The second theory agent agrees with the wording of the first theory agent's note 43 item 6: theory_v11
   carries SC^+ <= G - S^+ and A_low^+ <= G - S^+ (AT-837 item 5, AT-857), with the hypotheses C0 to C7 of T2_FAR_v02
   (AT-860) and the FLOAT status of each input. Corollary HSB-R is the row-wise alternative with the same certified
   pieces. The second theory agent has no objection.
10. The split log 16, rho 2 (section 2.5). It is the one row of T2_013_SPLITS_v01 that passes in FLOAT through
   absolute-kernel uppers only (HSB with route (a): 0.5725; Lemma HS: 0.5832; Gbar 0.65167), so C2 and its
   eigenproblem are absent there. Its certified rows are those of the direct route without C2, plus L2 (route (a)
   with m and O^+) or L2' (Lemma HS). The expensive row is again C3, the majorant m, because the window cannot be
   removed by the tail charge (with the wide window Ww = Rw it is still 0.109 at Rw 200, above the margin 0.079). The total, 33 to 47 hours on
   route HS and 44 to 62 hours on route HSB, is above the time left, and the near side at this split has a smaller
   margin (P_HF B / D 0.57) and has not been priced by its owner. The second theory agent's recommendation for X5 is unchanged: no far
   certificate at either split is a closure path before the stop. Of the two splits, log 16, rho 2 is the one whose
   far side has a known route without an eigenproblem; it is the better target for work after the run.
11. Route F-a (section 2.6). It removes the eigenproblem of C2 and the window problem of C0-W at the price of the
   strain target. With the full tail charge (the moments of OMF(a_t) are tabulated now, AT-917) its FLOAT far value
   at erflog 8, rho 1 is 1.9103 at Rw 50 and 1.4227 at Rw 100 with the window width Ww = Rw/5 of note 44,
   and 1.3842 at Rw 50 with Ww = Rw, against G(1.096) = 1.500070. The moments of the tail charge come from the window
   transition, so the width matters more than the radius: the second theory agent recommends Ww = Rw for this route (whether AT-911
   covers that width is for the theory auditor to state). The certified strain bound must be at most 1.096 (the numerical auditor: cover cost not
   known). Its the second theory agent rows (45 to 72 hours) again contain a majorant of the transform (now of the windowed piece,
   FA2) and add the certified tail moments (FA5).
