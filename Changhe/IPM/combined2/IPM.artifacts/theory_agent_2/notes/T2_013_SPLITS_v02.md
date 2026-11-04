# T2_013_SPLITS_v02: consolidated split table for C2-N1-013 (far certificate without a large eigenproblem, and the near price)

Agent the second theory agent, written 2026-11-03T14:49Z for the coordinator 11:57Z item 2(a) (the second numerics agent supplies the band values), with the
K' options of the coordinator 12:10Z item 4(a) and the column of the first theory agent's note 44 item 1(a). Every far number is FLOAT (grid
samples and FFT sums of a sampled windowed field) and every near price is HEURISTIC (the first theory agent's HF1-NEAR model at FLOAT
near inputs). Nothing in this note is certified and nothing in it is a bound. Paths are relative to research/h4/far009/
of agent the second theory agent unless another agent is named. Gbar = q (c - 3/2) = 0.651670 (q = 21/10, c = 4076476460239181/2^51).

Changes against v01 (published 13:16Z to 13:17Z, not edited): (1) Section 4: the Rw 200 rows of Table 4 (route (a) A_E
and S_h^B at Rw 200, Ww 40) and the computed rows of Table 4b (Ww = Rw); (2) section 4 intro: the two tails are not
equal (AT-971), with the FLOAT charge of their difference; every tail charge is that of the tail cut at Ro = 4 Rw, and
the exterior part is not charged (AT-973); (3) the readings of section 4 and the route F-a paragraph of section 1 follow
the new rows; (4) the Rw 200 row of Table 4b (A_E at Rw 200, Ww 200) and the near side of log 16, rho 2 in condition 3
of section 1 (the first theory agent's notes 46 and 47). Sections 2, 3 and 5 are unchanged.

## 1. Answer

Question (11:57Z item 2(a)): is there a split where the far certificate needs no large eigenproblem and the near price
stays below the allowance?

In FLOAT one requested row passes: log 16, rho 2 (013 coefficient, N 2048, window 50/10, K' = 8 pi, K = 2 pi).
- Lemma HSB with the route (a) band upper: max(SC, A_E) + S_h^B = max(0.1001, 0.5659) + 0.0066 = 0.5725, against
  Gbar 0.6517: far margin 0.079, strain level c - 0.5725/q = 1.5377.
- Lemma HS of the first theory agent with the part_tau1_p2 split and no band: osc + S_HS = 0.4704 + 0.1128 = 0.5832: far margin 0.068.
- Both are absolute-kernel uppers (integrals of |a^| and an oscillation term), so neither needs an eigenvalue upper.
- Near price (HEURISTIC, 013 budget): P_HF B / D = 0.57 and P_B / D = 1.02. So the tail-B price of HF1-NEAR stays below
  the allowance D (by a factor 1.76, against 11.5 at erflog 8, rho 1), and the P_B price does not. These two prices use
  the kernel constants of the theory_v11 model. With the first theory agent's kernel uppers of note 46 (condition 3 below) the tail-B
  price is P/D 0.971 at mu 41.5 (b0 0.55), and the near test holds only for mu from 41.38 to about 41.86; with the
  variant of note 47 it is 0.798 at mu 41.5. The first theory agent (note 46 item 3) reads the first as: with the present kernel
  constants log 16, rho 2 is not a usable near split; with the variant it has the mu windows of condition 3, conditional
  on the audit of the variant.

No other requested row passes. At the rows with osc(a_f) above Gbar (erflog 8 up to rho 1.25, erflog 16 rho 0.5 and
0.75, log 8 rho 1 and 1.5) every evaluated absolute-kernel upper exceeds Gbar, and route (a) is at least its floor O
(AT-882). At the other rows with osc(a_f) below Gbar, route (a) is the cheapest evaluated upper and lies above Gbar:
0.8227 (erflog 8, rho 1.5), 0.8035 (erflog 16, rho 1), 0.6968 (log 16, rho 1.5), 0.7923 (log 8, rho 2), 0.7951
(log 16, rho 1.25), 1.1584 (log 16, rho 1).

Route F-a (section 4, the first theory agent's note 44) also needs no eigenvalue upper, but not at strain 3/2. At erflog 8, rho 1, with the
window width Ww = Rw/5 of note 44, its far value is 1.9103, 1.4227 and 1.3053 at Rw 50, 100 and 200 (A_E and S_h^B
computed at each window), against G(1.096) = 1.500070: it passes at Rw 100 and 200 with the margins 0.0774 and 0.1948
(strain levels 1.1328 and 1.1888) and fails at Rw 50, because the moments of the tail charge (0.486 at Rw 50), which
come from the window transition, are larger than its oscillation. With the wide window Ww = Rw (inputs matched to the
width at Rw 50 and 100, AT-1012; at Rw 200 S_h^B is the Rw 50 value) the far value is 1.3842, 1.3111 and 1.2664 at Rw
50, 100 and 200, with the margins 0.1159, 0.1890 and 0.2337. At log 16, rho 2 it gives 0.8142 at Rw 100, Ww 20 (level
1.4226).

Conditions of the log 16, rho 2 reading (each one is open):
1. Window. The values are for the windowed coefficient a_W (Rw 50). The far piece beyond Rw is the same as at erflog
   8, rho 1 (the cut is 1 for r >= 32). The full tail charge OMF(a_t), with its moments (section 4), is 0.751, 0.266
   and 0.148 at Rw 50, 100 and 200 with Ww = Rw/5, and 0.227, 0.154 and 0.109 with Ww = Rw; the oscillations alone
   (0.265, 0.189, 0.135 with Ww = Rw/5, the second numerics agent: 0.29, 0.21, 0.15; 0.212, 0.151, 0.109 with Ww = Rw) already exceed the
   far margin 0.079. So the window cannot be removed by a tail charge at these Rw, and the row passes only if route
   (a) (or Lemma HS) and the Schur rows are certified for the unwindowed a_f directly, through a majorant m of |a_f^|
   (row C3 of T2_013_FAR_OWNERS_v01). At Rw 100 (Ww 20, N 4096, the same grid step 0.064) route (a) gives
   A_E = 0.5420 at this split (tau 2, Schur weight s = 1.5; 0.5511 at tau 1;
   runs/hsb_band_rows_log_lam16_b18s2_N4096_RW100.json), 0.024 below the Rw 50 value, with the same sampled osc and SC.
   So the windowed band upper does not grow with the window here. Route F-a at this split gives 1.323 and 0.814 at
   Rw 50 and 100, above Gbar.
2. Floor and majorant. A certified A_E^+ needs a certified O^+ (the oscillation floor of AT-882 is reached as r -> 0 in
   the diagonal of the part_tau1_p2 family) and the route (a) integrals with m in place of |a^|; m >= |a^| raises every
   integral, and the FLOAT check of C3 (how much) is not run. The margin 0.079 is the room for these changes.
3. Near side. The near inputs grow with rho (sup- 35.7, sup+ 53.2, L1+ 31.0 at log 16, rho 2 against 8.65, 8.53, 4.04 at
   erflog 8, rho 1), so the near certificate at this split has a smaller margin (0.43 of D on P_HF B in the model of
   section 5) and the P_B route is closed. The first theory agent has priced this split with arb kernel uppers that are not audited (note
   46; every other near input FLOAT, every P/D HEURISTIC). With the Psi_1 cut the near test at log 16, rho 2 holds only
   for mu from 41.38 to about 41.86 at b0 0.55 (P/D 0.971 at mu 41.5) and at b0 0.60 it fails at every mu >= 45.91 (P/D
   1.048 at mu 46), against P/D 0.150 at erflog 8, rho 1, mu 41. With the exp(-|xi|^4) variant (note 47; a change of the
   proposition in v12_n6 (f) 1, not audited) the windows are mu 41.36 to about 44.1 at b0 0.55 (P/D 0.798 at 41.5) and
   45.89 to about 47.4 at b0 0.60 (0.892 at 46), against 0.123, 0.190 and 0.304 at erflog 8, rho 1, mu 41, 46 and 52.
   The second theory agent has no smaller uppers of the near inputs sup- 35.72, sup+ 53.21 and L1+ 30.99 of this split (note 46 item 6),
   so these near prices stand as the first theory agent gives them.
4. Strain. The level 1.5377 is 0.038 above 3/2, so the target 3/2 serves this split in FLOAT.

## 2. Table 1: requested splits (013, K' = 8 pi, K = 2 pi, N 2048, window 50/10; FLOAT far values, HEURISTIC near prices)

Rows of scan22 first (the coordinator 11:57Z), then the other requested rows. Output of code/split_table013.py (split_table013_1256.out); n/c means not computed.

| split | rho | far | osc(a_f) | band value 8 pi | route (a) A_E | OMF(b), b = a_(2K') | OMF(a_f) | TII-1 + CAW-F | U | SC | S_h^B | Gbar - S_h^B | max(SC, U) + S_h^B <= Gbar | Lemma HS (part_tau1_p2) | P_HF B / D | P_B / D |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| erflog 8 | 1.25 | 013 | 0.7033 | 0.2443 | >= O (AT-882) | n/c | 2.455 | 2.782 | 2.4550 (OMF) | 0.2820 | 0.0092 | 0.6425 | no | 0.9763 | 0.13 | 0.25 |
| erflog 8 | 1.5 | 013 | 0.6505 | 0.1984 | 0.8227 | n/c | 1.777 | 2.143 | 0.8227 (route (a)) | 0.1874 | n/c | n/c | no (with S >= 0) | n/c | 0.18 | 0.34 |
| erflog 16 | 1 | 013 | 0.6209 | 0.1972 | 0.8035 | n/c | 1.939 | 2.207 | 0.8035 (route (a)) | 0.1912 | n/c | n/c | no (with S >= 0) | n/c | 0.15 | 0.27 |
| erflog 16 | 0.5 | 013 | 0.8266 | n/c | >= O (AT-882) | n/c | 9.501 | 6.772 | 6.7724 (TII-1) | 0.8989 | n/c | n/c | no (with S >= 0) | n/c | 0.05 | 0.10 |
| erflog 16 | 0.75 | 013 | 0.7023 | n/c | >= O (AT-882) | n/c | 3.433 | 3.377 | 3.3766 (TII-1) | 0.3653 | n/c | n/c | no (with S >= 0) | n/c | 0.10 | 0.19 |
| erflog 8 | 0.95 | 013 | 0.7871 | n/c | >= O (AT-882) | n/c | 4.247 | 4.223 | 4.2233 (TII-1) | 0.5141 | n/c | n/c | no (with S >= 0) | n/c | 0.08 | 0.16 |
| log 16 | 1.5 | 013 | 0.5383 | 0.1603 | 0.6968 | n/c | 1.954 | 1.984 | 0.6968 (route (a)) | 0.1874 | n/c | n/c | no (with S >= 0) | n/c | 0.34 | 0.62 |
| log 16 | 2 | 013 | 0.4704 | 0.1330 | 0.5659 | n/c | 1.134 | 1.317 | 0.5659 (route (a)) | 0.1001 | 0.0066 | 0.6450 | yes | 0.5832 | 0.57 | 1.02 |
| erflog 8 | 0.75 | 013 | 0.8626 | 0.6716 | >= O (AT-882) | n/c | 7.310 | 6.242 | 6.2420 (TII-1) | 0.8536 | 0.0817 (009) | 0.5700 | no | 1.8568 | 0.05 | 0.11 |
| erflog 8 | 0.85 | 013 | 0.8223 | 0.5291 | 1.5059 (009) | n/c | 5.437 | 5.056 | 1.5059 (route (a)) | 0.6535 | 0.0479 (009) | 0.6038 | no | 1.5441 | 0.07 | 0.13 |
| erflog 8 | 0.9 | 013 | 0.8041 | 0.4736 | >= O (AT-882) | n/c | 4.778 | 4.605 | 4.6046 (TII-1) | 0.5778 | 0.0369 | 0.6147 | no | 1.4289 | 0.07 | 0.14 |
| erflog 8 | 1 | 013 | 0.7711 | 0.3848 | 1.1369 | n/c | 3.812 | 3.898 | 1.1369 (route (a)) | 0.4598 | 0.0227 | 0.6290 | no | 1.2475 | 0.09 | 0.17 |
| log 8 | 1 | 013 | 0.8051 | 0.7284 | >= O (AT-882) | n/c | 14.419 | 7.778 | 7.7782 (TII-1) | 0.9682 | 0.4162 | 0.2355 | no | 2.4714 | 0.09 | 0.17 |
| log 8 | 1.5 | 013 | 0.6800 | 0.3674 | >= O (AT-882) | n/c | 4.919 | 3.845 | 3.8455 (TII-1) | 0.4484 | 0.0863 | 0.5654 | no | 1.1980 | 0.18 | 0.34 |
| log 8 | 2 | 013 | 0.5986 | 0.2109 | 0.7923 | n/c | 2.515 | 2.427 | 0.7923 (route (a)) | 0.2437 | 0.0275 (009) | 0.6242 | no | 0.8529 | 0.31 | 0.56 |
| log 16 | 1 | 013 | 0.6464 | 0.3395 | 1.1584 | n/c | 4.956 | 3.753 | 1.1584 (route (a)) | 0.4275 | 0.1002 | 0.5515 | no | 1.1807 | 0.17 | 0.31 |
| log 16 | 1.25 | 013 | 0.5851 | 0.2275 | 0.7951 | n/c | 2.901 | 2.618 | 0.7951 (route (a)) | 0.2743 | 0.0414 (009) | 0.6103 | no | 0.8847 | 0.25 | 0.46 |

Columns of Table 1 (all far columns are for the windowed far coefficient a_f = chi atil_013 (1 - W) of the FLOAT runs;
none is a bound):
- far: 013 is the C2-N1-013 coefficient (CORR b18s2); 009 marks a row taken from the 009 coefficient (CORR b14s) where
  no 013 row exists. At erflog 8, rho 0.9 and 1 the two differ by at most 2e-7 in osc and SC, 1.1e-6 in S_h^B and
  1.7e-5 in HSB-R (the second theory agent 11:32Z); the theory auditor AT-877 refutes agreement to 1e-7 in every far quantity, and no transfer
  accuracy follows for other rows.
- osc(a_f): sampled sup minus inf of a_f. SC: sampled sup of max(0, (1/2)[(q^2 - 1) lambda_max D^2 a_f + Delta a_f]).
  Both are the larger of two samples: code/far_scan_ts.py (window Rw = max(50, 6 lam rho), grid step 2.64 Rw/2048) and,
  where the route (a) row exists, code/hsb_band_rows.py (Rw 50, step 0.064).
- band value 8 pi: FLOAT top eigenvalue of the 8 pi band problem (square band, L 128, N 2048, window 50/10, 8 angular
  modes), from the second numerics agent 12:09Z (009 coefficient) or from this agent's code/far_box4.py where marked t2. It is not an upper;
  it shows what an eigenvalue route would have to certify.
- route (a) A_E: the absolute-kernel band upper of AT-707 (code/hsb_band_rows.py, family part_tau1_p2), smallest over
  tau in {0.5, 1, 2} and the five Schur weights, at K' = 8 pi, N 2048, Rw 50 / Ww 10. A_E >= O for this family (AT-882,
  CONFIRMED); the code samples O as osc(a_f), which does not certify O = min(osc(a), osc(Pa)) (AT-883 to AT-885).
  Where the row is marked ">= O (AT-882)", A_E was not computed: there osc(a_f) > Gbar.
- OMF(b): OMF(b) = osc(b) + M2(b) + (q^2/2) M2[w_new](b) for the sharp low-pass b = a_(2K') of the far_scan_ts field
  (code/lowpass_omf.py, AT-806). Other admissible b have only the floor osc(phi * a) of NR-24 (AT-886). Where the grid
  Nyquist pi/h of that field is below 2K' = 16 pi the filter removes nothing on the grid and OMF(b) = OMF(a_f) (marked).
- OMF(a_f) and TII-1 + CAW-F: code/far_scan_ts.py (OMF with the asinh weight w_new, key M2a_af).
- U: the smallest of the four uppers of the row. S_h^B: the Schur cost of Lemma HSB at K' = 8 pi, K = 2 pi, best weight
  (code/hsb_far.py, N 2048, Rw 50). Test: max(SC, U) + S_h^B <= Gbar = 0.651670.
- P_HF B / D and P_B / D: HEURISTIC near prices of the first theory agent's HF1-NEAR model (tail B) at the 013 budget (beta_0* 7/4,
  f 7.97e-7, N 0.0055), each minimized over b0 in {0.55, 0.60}, evaluated by this agent from the 013 near inputs of
  far_scan_ts (research/h4/near013/price_split013.py, which executes copies of the first theory agent's hf1_price_e8.py and
  tab_price013g.py; SHA256 values in research/h4/near013/copied_sha256.txt).

## 3. K' options at erflog 8, rho 1 (the coordinator 12:10Z item 4(a))

013, N 2048, window 50/10, K = K'/4 (code/kp_table.py, runs/kp_table_1204.out; the first theory agent's note 43 item 3 reproduces the
2 pi, 4 pi and 8 pi rows, and the theory auditor AT-901 replays their margins from the saved arrays). The room for the band upper
is Gbar - S_h^B. The Landau order is the first theory agent's count K'^2 X^2/16 for the window X = 60 after the parity factor 4 (note
43: 8.9e3, 3.6e4, 1.4e5); the 3 pi and 6 pi entries are the same count (this agent's arithmetic). It is the size of the
uniform lattice representation, not a lower bound for every certificate (the second numerics agent 12:14Z item 1(b), AT-876, AT-878).

| K' | band value (FLOAT) | S_h^B | room Gbar - S_h^B | Gbar - S_h^B - band | Gbar - S_h^B - SC | Landau order (X = 60) |
|---|---:|---:|---:|---:|---:|---:|
| 2 pi | 0.2635 | 0.1834 | 0.4683 | 0.2048 | 0.0084 | 8.9e3 |
| 3 pi | 0.2682 | 0.1092 | 0.5425 | 0.2743 | 0.0826 | 2.0e4 |
| 4 pi | 0.3042 | 0.0712 | 0.5805 | 0.2763 | 0.1207 | 3.6e4 |
| 6 pi | 0.3572 | 0.0370 | 0.6147 | 0.2575 | 0.1549 | 8.0e4 |
| 8 pi | 0.3848 | 0.0227 | 0.6290 | 0.2442 | 0.1692 | 1.4e5 |

SC = 0.4598 at every row. At 2 pi the SC margin is only a narrow positive sampled margin (AT-901). Only 2 pi is near the
order of about 1e4; there the binding condition is SC^+ + S^+ <= Gbar with 0.0084 of room, and every computed tail
charge of section 4 (at least 0.109) exceeds that room, so the window cannot be removed by it at 2 pi. No
absolute-kernel band upper is evaluated at K' below 8 pi; at 8 pi route (a) gives 1.1369.

## 4. Far value with A_E and the tail charge (the first theory agent's note 44 item 1(a), the coordinator 12:33Z item 2(c))

Route F-a (the first theory agent's note 44, AT-911): A_*(a_f) <= max(SC, A_E(a_W)) + S_h^B(a_W) + OMF(a_t) for a_f = a_W + a_t, a_W = a_f
(1 - Sinf((r - Rw)/Ww)), with Ww = Rw/5 (note 44) in Table 4 and Ww = Rw in Table 4b. The strain level c - A/q must be
at least the certified strain bound s^+; at s^+ = 1.096 the far budget is G(1.096) = q (c - 1.096) = 1.500070. FLOAT,
013, K' = 8 pi, K = 2 pi. A_E is from code/hsb_band_rows.py at the grid step 0.064 (Rw 50 at N 2048, Rw 100 at N 4096)
or 0.129 (Rw 200 at N 4096); S_h^B is from code/hsb_far.py at the matched Rw where it was computed, else the Rw 50 value
(marked "(Rw 50)"). The tail charge is from code/tail_omf.py: OMF(a_t) = osc(a_t) + M2(a_t) + (q^2/2) M2[w_new](a_t),
with osc the grid max(0, sup) - min(0, inf), the moments as FFT sums of the sampled tail, the far-out cut at Ro = 4 Rw
(width Ro/5) and the grid N 2048 (env TAILN 2048; the N 4096 rows are in the readings). The log 16, rho 2 rows use the
erflog 8, rho 1 tail. The two tails are not equal (AT-971): for r >= Rw >= 32 the log cut at rho 2 is exactly 1, so they
differ by d = a0 (1 - chi_E) w_R, w_R = Sinf((r - Rw)/Ww), and the FLOAT charge OMF(d) is 4.5e-13, 1.5e-19 and 4.8e-27
at Rw 50, 100 and 200 with Ww = Rw/5 and at most 1.2e-15 with Ww = Rw (code/tail_diff.py, runs/tail_diff_1319.out); a
certified transfer needs OMF^+(d). Every OMF(a_t) in this section is the charge of the tail cut once more at Ro = 4 Rw,
a_t (1 - Sinf((r - Ro)/Wo)), Wo = Ro/5 (AT-973): the exterior part a_t Sinf((r - Ro)/Wo) is not charged. Table 4 is the
output of code/fa_column.py (runs/fa_column_1336.out).

Table 4 (Ww = Rw/5; tail cut at Ro = 4 Rw, exterior part not charged):

| split | rho | Rw (N, h) | A_E(a_W) (tau, weight) | SC | S_h^B | tail osc | tail M2 | tail M2[w_new] | OMF(a_t) | far value A | level c - A/q | G(1.096) - A | Gbar - A |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| erflog 8 | 1 | 50 (2048, 0.064) | 1.1369 (tau1, s1.5) | 0.4598 | 0.0227 | 0.2649 | 0.1315 | 0.1607 | 0.7507 | 1.9103 | 0.9006 | -0.4103 | -1.2587 |
| erflog 8 | 1 | 100 (4096, 0.064) | 1.1345 (tau1, s1.5) | 0.4598 | 0.0226 | 0.1889 | 0.0228 | 0.0244 | 0.2656 | 1.4227 | 1.1328 | 0.0774 | -0.7710 |
| erflog 8 | 1 | 200 (4096, 0.129) | 1.1343 (tau1, s1.5) | 0.4591 | 0.0226 | 0.1354 | 0.0040 | 0.0041 | 0.1484 | 1.3053 | 1.1888 | 0.1948 | -0.6536 |
| log 16 | 2 | 50 (2048, 0.064) | 0.5659 (tau2, s1.5) | 0.1001 | 0.0066 | 0.2649 | 0.1315 | 0.1607 | 0.7507 | 1.3232 | 1.1802 | 0.1769 | -0.6715 |
| log 16 | 2 | 100 (4096, 0.064) | 0.5420 (tau2, s1.5) | 0.1001 | 0.0066 (Rw 50) | 0.1889 | 0.0228 | 0.0244 | 0.2656 | 0.8142 | 1.4226 | 0.6859 | -0.1625 |
| log 16 | 2 | 200 (4096) | not computed | | 0.0066 (Rw 50) | 0.1354 | | | 0.1484 | not available | | | |

Readings of Table 4 (FLOAT; none of these numbers is a bound):

- The moments of the tail charge are not small at Rw 50 with Ww = Rw/5. OMF(a_t) is 0.7507 there, of which the
  oscillation is 0.2649, M2 is 0.1315 and (q^2/2) M2[w_new] is 0.3543. At Rw 100 and 200 the moments add 0.0767 and
  0.0130 to the oscillations 0.1889 and 0.1354. The oscillation alone (here 0.2649, 0.1889, 0.1354; the second numerics agent: 0.29,
  0.21, 0.15) is 35, 71 and 91 percent of the full charge at Rw 50, 100 and 200.
- The moments come from the transition of the window, not from the far field. At Rw 50 (code/tail_spec.py,
  runs/tail_spec_1300.out): 82 percent of M2 sits at |zeta| in [0.5, 5), far above the angular frequencies 2k/r of
  the field on r >= 50 (at most 0.28 for the 8 modes kept), and the mode cos(2 theta) alone has M2 0.127;
  sup |Laplacian a_t| is 0.0183, about 100 times the Laplacian 1.8e-4 of the mode cos(2 theta) of the far field at
  r = 50 and of the size of a_f(Rw) Sinf''/Ww^2 at the transition; the FFT moment, an integral of |zeta|^2 |a_t^|,
  spreads this over the ring Rw <= r <= Rw + Ww. A wider transition removes most of it (same Rw and Ro,
  runs/tail_omf_wwf_1302.out): at Rw 50 the full charge is 0.7507 at Ww = Rw/5, 0.2885 at Ww = Rw/2 and 0.2273 at
  Ww = Rw (moments 0.486, 0.048 and 0.016).
- Wide window, erflog 8, rho 1 (Table 4b, code/fa_column.py with WWF 1, runs/fa_column_ww1_1444.out): with Ww = Rw the
  tail charge is 0.2273, 0.1542 and 0.1094 at Rw 50, 100 and 200. Every input is now computed at its own window at Rw 50
  and 100 (AT-1012: Ww = Rw is admissible once its inputs are matched to the width): the route (a) value of the wider
  piece a_W (support r <= Rw + Ww) is A_E = 1.1343 at both radii (tau 1, grid step 0.064; 1.1369 at Rw 50, Ww 10), and
  S_h^B is 0.0226 at both (N 3456, grid steps 0.064 and 0.127). The far value is 1.3842 at Rw 50, below G(1.096) by
  0.1159 (level 1.1512), and 1.3111 at Rw 100, below G(1.096) by 0.1890 (level 1.1860). At Rw 200, A_E at Ww 200 is
  1.1343 as well (N 6912, grid step 0.127, runs/hsb_band_rows_erflog_lam8_b18s2_N6912_RW200_WW200.json); S_h^B is not
  computed at Ww 200, and the row uses the Rw 50, Ww 10 value 0.0227 (0.0226 or 0.0227 at every window where it is
  computed). The far value at Rw 200 is 1.2664, below G(1.096) by 0.2337 (level 1.2073). So the window width, a free
  parameter of the split a_f = a_W + a_t, decides whether route F-a passes at Rw 50: it fails at Ww = Rw/5 by 0.41 and
  passes at Ww = Rw with the margin 0.116 in FLOAT. A wider transition does not raise A_E here; it makes a_W larger in
  support (Rw + Ww), which raises the quadrature cost of FA2. At Rw 100 the two widths give 1.4227 (Ww 20) and 1.3111
  (Ww 100).

  Table 4b (Ww = Rw; tail cut at Ro = 4 Rw, exterior part not charged):

  | split | rho | Rw (N, h) | A_E(a_W) (tau, weight) | SC | S_h^B | tail osc | tail M2 | tail M2[w_new] | OMF(a_t) | far value A | level c - A/q | G(1.096) - A | Gbar - A |
  |---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
  | erflog 8 | 1 | 50 (3456, 0.064) | 1.1343 (tau1, s1.5) | 0.4608 | 0.0226 | 0.2116 | 0.0048 | 0.0049 | 0.2273 | 1.3842 | 1.1512 | 0.1159 | -0.7325 |
  | erflog 8 | 1 | 100 (6912, 0.064) | 1.1343 (tau1, s1.5) | 0.4608 | 0.0226 (N 3456) | 0.1514 | 0.0009 | 0.0009 | 0.1542 | 1.3111 | 1.1860 | 0.1890 | -0.6594 |
  | erflog 8 | 1 | 200 (6912, 0.127) | 1.1343 (tau1, s1.5) | 0.4598 | 0.0227 (Rw 50, Ww 10) | 0.1089 | 0.0002 | 0.0002 | 0.1094 | 1.2664 | 1.2073 | 0.2337 | -0.6147 |

- Window removal on the direct route (row C0-W of T2_013_FAR_OWNERS_v01). The same split removes the window from
  Lemma HSB with the band value. The room is Gbar - S_h^B - max(SC, band) = 0.1692 at erflog 8, rho 1, 8 pi. The full
  tail charge fits at Rw 200 with Ww = Rw/5 (0.1484, margin 0.021) and at Rw 100 and 200 with Ww = Rw (0.1542 and
  0.1094, margins 0.015 and 0.060), if SC, the band value and S_h^B of the larger piece stay at their Rw 50 values.
  The band problem then lives on r <= Rw + Ww. At log 16, rho 2 every computed tail charge exceeds the margin 0.079.
- erflog 8, rho 1, Ww = Rw/5 (Table 4). A_E(a_W) barely depends on Rw (1.1369, 1.1345 and 1.1343 at Rw 50, 100 and
  200, all at tau 1, the minimizer over tau in {0.5, 1, 2} at Rw 50; Rw 100 and 200 were run at tau 1 only), because
  its lead O = osc(a_W) = 0.7711 is attained near the cut, not in the tail. S_h^B is 0.0227, 0.0226 and 0.0226 at
  Rw 50, 100 and 200, each computed at its own window. The far value is 1.9103 at Rw 50, above G(1.096) = 1.500070
  by 0.4103; 1.4227 at Rw 100, below G(1.096) by 0.0774 (level 1.1328); and 1.3053 at Rw 200, below G(1.096) by
  0.1948 (level 1.1888). The Rw 200 row has the grid step 0.129 (N 4096 on the larger box), twice the step of the
  other rows; its SC is 0.4591 against 0.4598 at the step 0.064. At strain 3/2 (Gbar 0.651670) route F-a fails at
  this split for every window, because A_E alone exceeds Gbar by 0.48.
- log 16, rho 2. A_E is 0.5659 at Rw 50 and 0.5420 at Rw 100 (tau 2). The far value is 1.3232 at Rw 50 (level 1.1802)
  and 0.8142 at Rw 100 (level 1.4226) with Ww = Rw/5. The direct route at this split (section 2, no window) passes at
  3/2 in FLOAT with 0.5725 (HSB with route (a)) and 0.5832 (Lemma HS); route F-a is not the better route there.
- Tail convergence (Ww = Rw/5, erflog 8, rho 1; runs/splitG_1245.log): at N 4096 with Ro = 2, 4 and 7 Rw the charge
  is 0.7575, 0.7515 and 0.7503 at Rw 50, 0.2666, 0.2656 and 0.2654 at Rw 100, and 0.1485, 0.1484 and 0.1483 at Rw 200.
  Halving the grid step at Ro = 4 Rw (Table 4 uses N 2048, steps 0.258, 0.516 and 1.031) moves it by at most 0.0008,
  and Ro = 7 Rw moves it by at most 0.0012 more; the far-out cut at Ro = 2 Rw adds its own transition (0.007 at Rw 50).
  The spectrum at Rw 50 decays above |zeta| = 5 (0.2 percent of M2 above 10, against the grid limit 12.2 at N 2048).
- Tail convergence (Ww = Rw, erflog 8, rho 1; runs/splitH_1321.log, code/tail_omf.py with WWF 1 at N 4096): with
  Ro = 2, 4 and 7 Rw the charge is 0.2888, 0.2273 and 0.2209 at Rw 50, 0.1644, 0.1542 and 0.1530 at Rw 100, and
  0.1112, 0.1094 and 0.1092 at Rw 200. At Ro = 2 Rw the outer cut starts where the window transition ends, which
  adds a moment (M2 0.0230 at Rw 50 against 0.0048 at Ro = 4 Rw). Between Ro = 4 and 7 Rw the charge moves by 0.0064,
  0.0012 and 0.0002; Table 4b uses Ro = 4 Rw (AT-973: the exterior part is not charged).
- Grid step of A_E (erflog 8, rho 1, Rw 50, Ww 10, tau 1, Schur weight s1.5): A_E is 1.136929 at the step 0.064
  (N 2048) and 1.136902 at the step 0.129 (N 1024, runs/hsb_band_rows_erflog_lam8_b18s2_N1024_RW50.json), a change of
  2.7e-5; SC is 0.4598 and 0.4591. So the decrease of A_E from 1.1369 at Rw 50 to 1.1343 at Rw 200 (step 0.129) is
  not an effect of the coarser step.
- Not checked: S_h^B at Rw 200, Ww 200 (the Rw 50, Ww 10 value 0.0227 is used); S_h^B at log 16, rho 2, Rw 100 (the Rw
  50 value 0.0066 is used); the angular truncation (8 modes) of every FLOAT row (T2_013_FAR_OWNERS_v01 reading 6).

## 5. Near prices

research/h4/near013/price_split013.py executes copies of the first theory agent's hf1_price_e8.py and tab_price013g.py up to their row
loops and evaluates the tail-B model at the 013 near inputs of far_scan_ts (runs/price_split013_1224.out and .json in
that directory). At the eight rows that the first theory agent's tab_price013g.out also lists it reproduces the first theory agent's two-digit values
(erflog 8, rho 0.75, 0.85, 0.9, 1; log 8, rho 1, 1.5; log 16, rho 1, 1.5). At erflog 16, rho 1 it gives 0.15 / 0.27
against the first theory agent's 0.17 / 0.31: this agent's 013 row has a near grid step 0.0332, above the 0.030 of every other row, so
that row's near inputs (M4 3959 against about 5010 elsewhere) are not comparable; it needs a finer near grid. These are
model prices, not certified near bounds.

## 6. What the table does not show

- No entry is a bound. SC and osc are grid maxima; every integral of |a^| is an FFT sum of the sampled windowed field;
  the sup over xi is a maximum over sampled xi.
- The far columns are for the windowed coefficient. On the direct route every certified number must be for the
  unwindowed a_f (row C0 of T2_013_FAR_OWNERS_v01).
- The 009 entries (marked) are not 013 values; no transfer accuracy is claimed for them (AT-877).
- S_h^B was not computed at erflog 8, rho 1.5, erflog 16, rho 0.5, 0.75 and 1, erflog 8, rho 0.95 and log 16, rho 1.5;
  at each of these rows max(SC, U) alone exceeds Gbar, so the test fails for every S_h^B >= 0.
