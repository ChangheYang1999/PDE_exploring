# T2_FAR_AE_PLAN_v01: priced plan (HEURISTIC) for a certified windowed band upper A_E^+(a_W) at Rw = Ww = 200 on route F-a, with Lemma SYM (CLAIMED) and a FLOAT feasibility test

Agent the second theory agent, written 2026-11-03 from 23:15Z, frozen 2026-11-03T23:17:11Z. Answers the coordinator's X7 note (21:52Z) item 5(d): "a priced
plan (theory, code, core and review hours; HEURISTIC) for a certified windowed upper A_E^+(a_W) at Rw = Ww = 200 with
max(SC^+, A_E^+) <= 1.3263305", for the X8 decision (item 4(c)). Recipients: the coordinator, the first theory agent (route F-a, notes 44
and 48), the theory auditor (audit). Code and run paths are relative to research/h4/far009/ of agent the second theory agent. Labels: Lemma SYM and
Proposition AE-CS are CLAIMED; every number in section 3 is FLOAT; every price in section 4 is HEURISTIC. No
certification code was written. The FLOAT runs of section 3 ran on core 41, one job at a time, with the scan22b row
(pid 2107555) paused by code/c1/with_pause.sh (runs/pauses_shift4.log).

## 0. Summary

- Target. A certified A_E^+ >= the AT-707 band bound of A_low(8 pi) for a_W, with max(SC^+, A_E^+) <= 1.3263305.
  Since SC(a_W) <= SC^+ = 4194197216881219/9007199254740992 (about 0.46565; AT-1366 to AT-1369, AT-1598), the
  condition is A_E^+ <= 1.3263305.
- Route. Lemma CS-S (row inequality CONFIRMED with radial coefficients, AT-1479, AT-1481) applied to the AT-707 band
  row, after a symmetrization zeta -> -zeta of the row kernel (Lemma SYM, section 2), which uses only that a_W is
  real. The field enters only through the certified energies D_s^+(a_W), s = 1, ..., 5, of Proposition DW (CONFIRMED
  conditionally, AT-1594 to AT-1596). No majorant of |a_W^| is needed, so the FA2 + FA3 route of
  notes/T2_013_FAR_OWNERS_v01.md section 2.6 (20 to 36 h) is not needed.
- FLOAT. With part_tau_p multipliers at tau = 9/8, p = 2, the weight h(t) = <t>^-193/100 for t <= 1/2 and
  h(t) = <1/2>^-193/100 (<t>/<1/2>)^-147/100 for t >= 1/2, and the integer orders 1, ..., 5: the sup over 165 sampled
  |xi| in [0, 25] of the lead plus the Cauchy-Schwarz bound is 1.18672, margin 0.13961 to 1.3263305. Every row may be
  overestimated by a factor 1.427 in its kernel integral before the margin is lost. Without Lemma SYM the same
  configuration gives 1.45495 (fails); the best unsymmetrized value found was 1.31351 (margin 0.0128, coarse grid).
- Price (HEURISTIC). The second theory agent: theory 1 h, code 3 to 5 h, run 0.3 to 1.5 core-hours on core 41, note 1 h (6 to 9 h
  wall-clock). The theory auditor: 3 to 6 h of review and a replay of 0.3 to 1.5 core-hours. From X8 (02:05Z) the second theory agent part ends
  at about 08:00Z to 11:00Z and the review at about 11:00Z to 17:00Z. The later end is after the final Part VII
  deadline (15:35Z).
- What it would give. Route F-a's far band inequality A_*(a_W + a_t) <= max(SC^+, A_E^+) + S_W^+ + OMF^+(a_t) <
  G(137/125) (FLOAT value 1.18672 + 0.17373975 = 1.36046, margin 0.13961), still conditional on (i) the numerical
  application of Theorem CS-B (AT-1540, OPEN), whose derivative records also carry D_s^+(a_W) and hence A_E^+, and
  (ii) the strain bound s^+ = 137/125 (AT-1599, OPEN). It gives no row C2, nothing at strain 3/2, no near bound, and
  does not change the verdict (NO; O3 unresolved).

## 1. Setting

Route F-a (AT-911, CONFIRMED): A_*(a_W + a_t) <= max(SC^+, A_E^+) + S^+ + OMF(a_t), where A_E^+ is any certified
upper of the band constant A_low(8 pi) of a_W (Lemma HSB, T2_FAR_v02 section 2.3: the band term is A_low(K') itself,
K' = 8 pi, so its upper may use a weight different from the Schur weight of S_h^B). With S_W^+ = 0.05970055144902641
(notes/T2_FAR_CSW_v02.md) and OMF^+(a_t) = 0.11403919054571054 (AT-1336 to AT-1338), S_W^+ + OMF^+ < 0.17373975 and
the far condition at s^+ = 137/125 (G = 1.5000703414199960) is max(SC^+, A_E^+) <= 1.3263305 (AT-1596, AT-1598;
the coordinator 22:03Z C1).

AT-707 (CONFIRMED; the theory auditor research/hs_rows_audit/PROOF.md): for E = {|xi| <= Kp}, Kp = 8 pi, any multipliers
phi_E, theta_E with values in [0, 1] and phi_E^2 + theta_E^2 <= 1, and any positive measurable weight h,
    A_low(Kp) <= ess sup_(xi in E) [ SC(a) phi_E^2 + osc_* theta_E^2 + rho_h^E(xi) ],
    rho_h^E(xi) = (2 pi)^-2 int_(|eta| <= Kp) (1/2) |a^(xi - eta)| |r_E(xi, eta)| h(eta)/h(xi) d eta,
    r_E = Ktil - phi_E phi_E' P - theta_E theta_E' |w - w'|^2,
with Ktil, P as in Lemma HS. For a = a_W: SC(a_W) <= SC^+ (above) and osc_* <= O^+ = 13905152014912945/
18014398509481984 (about 0.77190; AT-1238, valid for any window with values in [0, 1]).

## 2. Lemma SYM (CLAIMED) and Proposition AE-CS (CLAIMED)

Lemma SYM. Let a be real with a^ a function (a^(zeta) = int a(x) e^(-i x.zeta) dx), and g >= 0 measurable on R^2. Put
gbar(zeta) = (g(zeta) + g(-zeta))/2. Then int |a^| g = int |a^| gbar. If moreover D_s(a) = ||(-Delta)^(s/2) a||_2 is
finite for s in a finite set Sigma of positive orders and c_s >= 0 (not all 0), W(zeta) = sum_s c_s |zeta|^(2s), then
    int |a^| g <= 2 pi (sum_s c_s D_s(a)^2)^(1/2) (int gbar^2/W)^(1/2),
and int gbar^2/W <= int g^2/W.
Proof. a is real, so a^(-zeta) is the complex conjugate of a^(zeta) and |a^(-zeta)| = |a^(zeta)|. The substitution
zeta -> -zeta preserves Lebesgue measure, so int |a^(zeta)| g(-zeta) d zeta = int |a^(zeta)| g(zeta) d zeta, and the
average of the two is int |a^| gbar. Cauchy-Schwarz with the factors |a^| W^(1/2) and gbar W^(-1/2) (W > 0 off
zeta = 0) and Plancherel, int |zeta|^(2s) |a^|^2 = (2 pi)^2 D_s(a)^2, give the inequality (trivial if the last
integral is infinite). The last claim: W is even and ((x + y)/2)^2 <= (x^2 + y^2)/2. QED.

Proposition AE-CS. Let a = a_W, phi_E(t) = u/(u^2 + 1)^(1/2) with u = (t/tau)^2, theta_E = (1 - phi_E^2)^(1/2), h
radial and positive, Sigma = {1, ..., 5} and c_s(t) >= 0 for t = |xi| (not all 0). For xi in E put
    G_xi(zeta) = |r_E(xi, xi - zeta)| h(xi - zeta)/h(xi) 1_(|xi - zeta| <= Kp),   Gbar_xi = (G_xi(zeta) + G_xi(-zeta))/2,
    Kbar(xi) = int Gbar_xi^2 / W_xi,   W_xi(zeta) = sum_s c_s(|xi|) |zeta|^(2s).
Then
    A_low(8 pi) <= A_E^CS := sup_(|xi| <= 8 pi) [ SC^+ phi_E^2 + O^+ theta_E^2 + (1/(4 pi)) (sum_s c_s D_s^+2)^(1/2) Kbar(xi)^(1/2) ],
with D_s^+ = D_s^+(a_W) of runs/ds_window_v2_2158.json. Kbar depends on |xi| only (r_E(R xi, R eta) = r_E(xi, eta) for
rotations R, and h and W are radial).
Proof. AT-707 with the data above; rho_h^E(xi) = (2 pi)^-2 (1/2) int |a^| G_xi; Lemma SYM with g = G_xi; and
D_s(a_W) <= D_s^+ (Proposition DW). The factor is (2 pi)^-2 (1/2) 2 pi = 1/(4 pi). phi_E and theta_E take values in
[0, 1] with phi_E^2 + theta_E^2 = 1. QED.
The proposition is the CS-S form of Theorem CS-B with r_E for r_B and Gbar for G; Lemma SYM is the only new step.

## 3. FLOAT feasibility

Code: code/c1/ae_cs_wopt_float.py (polar zeta grid, log-spaced radii from RHOMIN to 2 Kp + 1, uniform angles;
c_s per |xi| by L-BFGS-B on log c; Nelder-Mead over tau and a piecewise log-linear h; SYM=1 applies Lemma SYM on the
grid; D_s^+ from runs/ds_window_v2_2158.json; lead SC^+ phi_E^2 + O^+ theta_E^2). Sampled |xi|: 20 values in
[1e-9, 25.1], or 165 values (1e-9, 0.05 to 4 in steps 0.05, 4.25 to 25 in steps 0.25).

| run | multipliers and weight | orders | grid (radii x angles) | sup of the total | at \|xi\| | margin to 1.3263305 |
|---|---|---|---|---|---|---|
| runs/ae_cs_opt_s2.out, best of 135 (no SYM) | tau 1.25; h: slope 2 to t = 0.5, then 1 | 1 to 5 by 1/2 | 2001 x 360 | 1.32940 | | -0.00307 |
| runs/ae_cs_wopt_eval.out (no SYM) | tau 1.25; slopes 2, 1.05 | 1 to 5 by 1/2 | 1201 x 240 | 1.31351 | | 0.01282 |
| runs/ae_cs_wopt_nm1.json (NM1, SYM) | tau 1.1265; slopes 1.9312, 1.4689 | 1 to 5 by 1/2 | 1201 x 240 | 1.18441 | 0.5 | 0.14192 |
| runs/ae_cs_v1_b.json (radii from 1e-12) | same | same | 2141 x 240 | 1.18441 | | |
| runs/ae_cs_v1_c.json | same | same | 4001 x 720 | 1.18442 | | |
| runs/ae_cs_v1_d.json (165 \|xi\|) | same | same | 1201 x 240 | 1.18700 | 0.65 | 0.13933 |
| runs/ae_cs_v1_e.json (no SYM) | same | same | 1201 x 240 | 1.45495 | 3.5 | -0.12862 |
| runs/ae_cs_v2_f.json | tau 9/8; slopes 193/100, 147/100 | 1 to 5 by 1/2 | 1201 x 240 | 1.18500 | 3.5 | 0.14133 |
| runs/ae_cs_v2_g.json | same | 1, ..., 5 | 1201 x 240 | 1.18500 | 3.5 | 0.14133 |
| runs/ae_cs_v2_h.json (165 \|xi\|) | same | 1, ..., 5 | 1201 x 240 | 1.18672 | 0.65 | 0.13961 |

Margin by band (runs/ae_cs_v1_d.json): 0.139 on [0, 1), 0.166 on [1, 2), 0.149 on [2, 3), 0.140 on [3, 4), 0.155 on
[4, 6.3), 0.353 on [6.3, 12), 0.501 on [12, 25]. The profile is nearly flat at 1.18 to 1.19 near |xi| = 0.65 and
|xi| = 3.6 (the two active constraints of the minimax). Allowed overestimate of Kbar, ((1.3263305 - lead)/CS)^2 at
each sampled |xi| of runs/ae_cs_v2_h.json: at least 1.427 (attained near |xi| = 3.65, where the CS part is 0.718).

Sanity check against the field (code/c1/ae_direct_float.py): the AT-707 total with the FFT |a_W^| of the sampled field
(N 6912, h 0.1273, |zeta| up to 24.7; the field as in code/c1/cs_route_float.py; maximum over the angles 0, 22.5, 45,
67.5 and 90 degrees of xi) at the NM1 configuration, runs/ae_direct_nm1.out (13 radii before the 585 s limit):

| \|xi\| | 0 | 0.25 | 0.5 | 0.75 | 1 | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 | 5 | 6.3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct total | 1.11213 | 1.09382 | 1.11348 | 1.10606 | 1.06965 | 1.00111 | 0.99290 | 0.98984 | 0.96057 | 0.89265 | 0.88748 | 0.82732 | 0.71577 |
| CS total (runs/ae_cs_v1_a.json) | 1.18439 | 1.16090 | 1.18441 | 1.18400 | 1.16054 | 1.12035 | 1.14726 | 1.17570 | 1.17668 | 1.18440 | 1.17099 | 1.06932 | 0.98336 |

Every Cauchy-Schwarz total lies above the direct total, as it must. The D2 symmetry of a_W (its far piece has the
modes cos(2 k theta) only) gives no further gain at the sup: there xi lies on a symmetry axis, where the D2 average
equals the zeta -> -zeta average (SYM=4 run in runs/ae_cs_wopt_eval.out).

## 4. Certification plan and prices (HEURISTIC)

A. Theory (the second theory agent, 1 h). Lemma SYM and Proposition AE-CS as in section 2, with rational data: tau = 9/8, p = 2,
   h as in section 0, Sigma = {1, ..., 5}.
B. Code (the second theory agent, 3 to 5 h): code/c1/ae_cells.py, adapted from code/c1/k_cells.py (Theorem CS-B):
   - the cancellation-free form, with om2 = |w - w'|^2 = 2 (1 - c) and Ktil = a b om2 + 4 a b sinh^2(q tau'/2)
     (k_cells.py notation),
         r_E = 4 a b (1 - phi phi') sinh^2(q tau'/2) + om2 [ (1 - phi phi') a b - theta theta' ] + phi phi' (Ktil - P),
     where Ktil - P has the identity already in k_cells.py and the bracket is >= 0 (phi phi' + theta theta' <= 1 and
     a b >= 1), so r_E/rho^2 is enclosed without cancellation near zeta = 0;
   - Lemma SYM on boxes: each zeta box is paired with its antipode, and the box upper of Gbar^2 is formed from the
     two box uppers of G; Gbar is even and symmetric under reflection in the xi axis, so the angular range is a
     quarter turn;
   - phi_E increasing and theta_E decreasing in t, h decreasing in |eta|, and the indicator |eta| <= Kp, each
     enclosed from the box ends;
   - |xi| cells on [0, 8 pi] only, with c_s fixed per cell (FLOAT choice) and the lead
     O^+ - (O^+ - SC^+) phi_E(t)^2 (decreasing in t) taken at the left end; the zeta domain is |zeta| <= 16 pi, so
     the tail lemma (code/c1/k_tail.py) and the RMAX part of k_cells.py are not needed;
   - arb ball arithmetic with outward rounding and the finiteness check of ds_window_v2.py;
   - tests: the identity against the direct formula (FLOAT at random points, arb at a few points), and cell bounds
     against code/c1/ae_cs_wopt_float.py at cell midpoints.
C. Run (the second theory agent core 41, 0.3 to 1.5 core-hours): about 130 cells (width 0.05 on [0, 6.3], 0.25 beyond); a cell
   stops refining when its bound is below 1.3263305 - 0.01 or its Kbar upper is within a factor 1.3 of the lower.
   Basis: the Theorem CS-B run (280 cells, 745472 boxes, 1129 s) refined to a factor 1.1; the room here is a factor
   1.43, but each box costs two evaluations (Lemma SYM).
D. Note (the second theory agent, 1 h): notes/T2_FAR_AE_v01.md with the statement, code and run hashes, the cell table and the value
   A_E^+.
E. Review (the theory auditor, 3 to 6 h, plus a replay of 0.3 to 1.5 core-hours): Lemma SYM and its use (0.5 to 1 h); the
   enclosures, the identity and the rounding of ae_cells.py (2 to 4 h; most of the box code is shared with
   k_cells.py, which the review of AT-1540 covers); the replay.
Total: the second theory agent 6 to 9 h wall-clock; the theory auditor 3 to 6 h after it. Risks: (1) the r_E boxes near zeta = 0 at small |xi| may
need the extra splitting that k_cells.py needed for r_B; (2) the theory auditor core serves the root reviews and the CS-B
replay first (X7 item 4(b)); (3) the certificate inherits whatever AT-1540 finds in the derivative records.

## 5. Dependencies and what this does not give

- A certified A_E^+ uses D_s^+(a_W) (Proposition DW), which rests on the B1 derivative records
  (runs/ds_upper_1926.json, runs/tail_deriv_1905.jsonl, runs/tail_deriv_1557.jsonl). Their review is part of the
  numerical application of Theorem CS-B (AT-1540, OPEN). So A_E^+ adds no new field input, but it is no more
  certain than those records.
- Route F-a also needs the global strain bound s^+ = 137/125 (AT-1599, OPEN) and the near side; none of them is
  touched here.
- Row C2 of Proposition F (strain 3/2, Gbar = 0.65167) stays OPEN; this plan does not address it (the FLOAT band
  value 1.187 of section 3 is far above Gbar).
- X7 item 4(c) schedules no far certificate before the stop; whether this step is coded is the X8 decision. Nothing
  in this note was coded beyond the FLOAT programs listed in section 6.
- Recommendation for X8: the route fits only if it starts at X8 and the theory auditor can review it by 15:35Z; otherwise
  record it in Part VII as a priced conditional step with the FLOAT margin 0.1396 and Lemma SYM for review.

## 6. Files (SHA256)

- code/c1/ae_cs_wopt_float.py 7003aabe1c0cadf4a3680091d5a4054e6512e390e8ba457d41bf7e7ce18b7052
- code/c1/ae_direct_float.py 4ff5e0d2ebcfefa4f704d061bc1af72a75292971ff2f0d06e92c2e1a521e8fb7
- code/c1/ae_cs_opt_float.py 8f35ceffd218d86f1d5d582e0fa29080e2f32c372ee924c7a4b8bf50041ee0a9
- code/c1/ae_cs_float.py c17bf4122089b03d851a35e95c16183d3dbd777682b3812f1b3a89c0a567bdfb
- runs/ds_window_v2_2158.json e26aeb71eadadf209a0140d50d8e9339aa1c8a3985e96cb8862893c3377abf6a (the D_s^+(a_W))
- runs/ae_cs_opt_s2.out f9f1d91c7654364b3f7ae1227c97cebcfa13950dca9affa912f592b577567340
- runs/ae_cs_opt_s2.json a8f52b0ad3183e0896818f1380f2866a150c3eee89baa4e648d74ce78864b410
- runs/ae_cs_wopt_nm.out d3e6233d8800c0aac286b316cc17637e37d77ae55e614d7526acf8de1311de5b
- runs/ae_cs_wopt_nm1.json 8ca71c10840473304159ab822de298c9252c87f0d40e95c9ce2e926b8405300d
- runs/ae_cs_v1_a.json 90cd6d67cfe7bbaac98be697ed3841b77cad4ea4ef7858c5003205a68b28659d
- runs/ae_cs_v1_b.json 8cb732de43bb9f5d1bc62720dd6d1e3618c03d6fb8df7feb778b6ce6f36eba57
- runs/ae_cs_v1_c.json cf610912dad686064ac6a707235468c8954d8160f77c720568a2b2a9beac6ef1
- runs/ae_cs_v1_d.json a1221a334df970ab1e3ba4775a8112a25d8b83af14b2c4717b4422b4532fcd7f
- runs/ae_cs_v1_e.json 2d28ec22e64571a545ced221f69fbfe8b62bd764c479a226f6251d159f6a3024
- runs/ae_cs_v2_f.json 7f3dd6b3533cb15637dfd46945afb2f6cb6856d381d18b99a367b1b8591d8bd4
- runs/ae_cs_v2_g.json 137c065fa167ef740e4976c5add5edfcd5f12085ba15690be94bbc1894b62e0a
- runs/ae_cs_v2_h.json c3684dfb82af3bf7e50aa6893b45550f8046247f54c3c469168f83b39324f02d
- runs/ae_direct_nm1.out bbaef87d62ce8e2c111fdad31f33ddd04967aa281f3e5d7dab5416f89ba0f959
- runs/ae_cs_v1.out 4244ac42e2a606d1ae06ba7cf717acc3dcdbe8ceeb2b362122eb13991227c0ed
- runs/ae_cs_v1b.out 32673f3a8141e60c55d6504b92a0a0d6c811fc88fdf73f6196c88682d7be8ce0
- runs/ae_cs_v2.out 1afc081528e7e003c4166f7344e6f6bd5cf43010ed8304b0a8c34d9a1a317d70
