# T2_FAR_CS_v01: rows C3 and C4 by Cauchy-Schwarz: what a certified Schur upper S^+ <= Gbar - SC^+ would need without the majorant of C3 (Lemma CS-S, CLAIMED; FLOAT test; HEURISTIC cost)

Agent the second theory agent, written 2026-11-03T18:58Z for the coordinator X6 note 18:03Z item 5(d)(3): "for rows C3 and C4, what a certified Schur
upper S^+ <= q(c - 3/2) - SC^+ (above 0.186020, AT-1234) would need, with a HEURISTIC cost". Lemma CS-S (item 2) is
CLAIMED and submitted to the theory auditor. Rows C3 and C4 are those of notes/T2_013_FAR_OWNERS_v01.md section 2.1.
Code and runs paths are relative to research/h4/far009/ of agent the second theory agent, and notes/ paths to the agent directory. Every
number marked FLOAT is a sampled value, not a bound.

0. Summary.
   - Route A (rows C3 and C4 as written in the owner table) costs 24 to 38 hours of code plus 5 to 14 core-hours with
     8 modes, more with all modes (HEURISTIC). It cannot finish, with review, before the stop.
   - Route B (Lemma CS-S, item 2) replaces the pointwise majorant m >= |a_f^| of C3 by two inputs:
     - certified uppers of the whole-plane energies D_s(a_f), s = 1, ..., 5, from the existing engine;
     - a certified upper of an explicit kernel integral.
   - FLOAT results for route B, as sups over the sampled values of |xi| in [0, 500]:
     - h = <min(|xi|, 6.3)>^-1, the best sampled Schur weight, gives 0.0413 (28 values).
     - h = <xi>^-1/2 gives 0.0428 (28 values).
     - h = 1 gives 0.1241 (20 values).
   - The budget is Gbar - SC^+ = 8377636983468883/45035996273704960 > 0.186020. With the engine energies (item 3)
     the best value becomes at most 0.0417, a factor of 4.4 below the budget.
   - Route B costs 8 to 13 hours of code plus 2 to 4 core-hours (HEURISTIC), then review.
   - S^+ alone does not certify the far side. (F2), row C2 (A_low^+), stays blocked. Route B would certify (F1) and
     the SC half of (F3). It leaves Gbar - S^+ for A_low^+: about 0.61 at S^+ = 0.042, against the FLOAT band value
     0.3848.

1. Target and route A.
   (a) Target: (F1) and (F3) of Proposition F (notes/T2_FAR_F_v01.md section 2). We need a measurable h > 0 and a
       number S^+ with S_h^B(a_f; 2 pi, 8 pi, h) <= S^+ <= Gbar - SC^+, for a_f unwindowed with all angular modes (C0).
       The direct FLOAT row sups are 0.026142 (h = 1), 0.026803 (h = <xi>^-1/2) and 0.022633 (Perron weight). They come
       from code/hsb_far.py at N 6912, Rw 200, Ww 200 with 8 modes (runs/hsb_erflog_lam8_b18s2_N6912_RW200_WW200.json).
   (b) Route A, from the owner table (notes/T2_013_FAR_OWNERS_v01.md section 2.1, rows C3 and C4):
       - Row C3 needs a majorant m(zeta) >= |a_f^(zeta)| for every zeta. It is built from the Hankel transforms of
         all 161 complex angular modes, with continuity in |zeta|, and from closed-form transforms of the asymptotic
         profile for r > R_ext.
       - a_f is not in L^1 or L^2, because |a_f| decays like r^-0.448 (FLOAT: E_0 over -3 <= y <= Y grows like
         e^(1.104 Y)). So a_f^ has a singularity of order |zeta|^-1.552 at 0, and m must carry it in closed form.
       - Row C4 needs the Schur rows with m in place of |a_f^|, with continuity in xi and a large-|xi| tail.
       - HEURISTIC cost from the owner table:
         - C3: 16 to 30 hours of code plus 4 to 10 core-hours with 8 modes, more with all modes;
         - C4: 8 hours of code plus 1 to 4 core-hours.

2. Route B. Lemma CS-S (CLAIMED; elementary; for review by the theory auditor).
   Hypotheses:
   - a is real and a^ is a function.
   - h > 0 is measurable and radial.
   - Sigma is a finite subset of [1, infinity).
   - For every s in Sigma, the energy
       D_s = ||(-Delta)^(s/2) a||_2 = ((2 pi)^-2 int |zeta|^(2s) |a^(zeta)|^2 d zeta)^(1/2)
     is finite.
   - For each xi, the coefficients c_s(xi) >= 0 (s in Sigma) are not all 0. Put
       w_xi(zeta)^2 = sum_s c_s(xi) |zeta|^(2s),
       K(xi) = int r_B(xi, xi - zeta)^2 (h(xi - zeta)/h(xi))^2 w_xi(zeta)^-2 d zeta.
   Take r_B, K = 2 pi and K' = 8 pi as in T2_FAR_v02 section 2.3. Then
       rho_h^B(xi) = (2 pi)^-2 int (1/2) |a^(zeta)| |r_B(xi, xi - zeta)| h(xi - zeta)/h(xi) d zeta
                  <= (1/(4 pi)) (sum_s c_s(xi) D_s^2)^(1/2) K(xi)^(1/2).
   So S_h^B(a) is at most the supremum over xi of the right side. K depends on |xi| only, and so may the choice of c.
   Proof.
   - Apply Cauchy-Schwarz to the factors |a^| w_xi and |r_B| (h(xi - zeta)/h(xi)) w_xi^-1.
   - Plancherel gives int |a^|^2 w_xi^2 = (2 pi)^2 sum_s c_s D_s^2. The constant is (2 pi)^-2 (1/2) (2 pi) = 1/(4 pi).
   - For every rotation R, r_B(R xi, R eta) = r_B(xi, eta). Ktil and P are built from <xi>, <eta>, w.w', zeta.w,
     zeta.w' and |zeta|, and the ramp functions theta and phi are radial. Since h is radial too, K(R xi) = K(xi). QED.
   Remarks on D_s:
   - For integer s, D_s^2 = int |grad^s a|_F^2 dx.
   - For s = j + t with 0 < t < 1, Hoelder gives D_s^2 <= D_j^(2(1 - t)) D_(j+1)^(2t). So half-integer orders need
     only the integer energies.

3. FLOAT test of route B (code/c1/cs_route_float.py).
   Method:
   - D_s comes from the FFT of the windowed sampled field, exactly as in hsb_far.py at N 6912, Rw 200, Ww 200 with 8
     modes.
   - K is a polar quadrature: 6001 log-spaced radii on [1e-6, 1e6] and 720 angles.
   - For each |xi|, the c_s for s in {1, 1.5, ..., 5} minimize the product, with the Hoelder form for half-integer s.
   - The table lists the rows. A "-" means the column was not sampled at that |xi|.

   | abs(xi) | direct h = 1 | CS h = 1 | direct h = <xi>^-1/2 | CS h = <xi>^-1/2 | CS h = <min(abs(xi), 6.3)>^-1 |
   |---|---|---|---|---|---|
   | 0 | 0.005623 | 0.1241 | 0.001551 | 0.02299 | 0.01945 |
   | 0.5 | 0.00512 | 0.1102 | 0.001495 | 0.02163 | 0.01932 |
   | 1 | 0.004309 | 0.08621 | 0.001419 | 0.01912 | 0.01911 |
   | 2 | 0.003543 | 0.05479 | 0.001482 | 0.01558 | 0.01921 |
   | 3 | 0.003825 | 0.04071 | 0.001936 | 0.01419 | 0.02018 |
   | 4 | 0.005011 | 0.0343 | 0.002952 | 0.01426 | 0.02217 |
   | 5 | 0.007397 | 0.03213 | 0.004923 | 0.01583 | 0.02569 |
   | 6.3 | 0.01372 | 0.03717 | 0.01036 | 0.0238 | 0.03717 |
   | 8 | 0.01687 | 0.03609 | 0.01468 | 0.0263 | 0.03632 |
   | 9.4 | 0.02009 | - | 0.01898 | 0.02971 | 0.03705 |
   | 11 | 0.02292 | 0.03656 | 0.02265 | 0.03295 | 0.03809 |
   | 12.6 | 0.02458 | - | 0.02481 | 0.03566 | 0.03919 |
   | 14 | 0.02557 | 0.03682 | 0.02609 | 0.0377 | 0.04007 |
   | 15.7 | 0.02614 | - | 0.02677 | 0.03975 | 0.04087 |
   | 17.5 | 0.02612 | 0.03616 | 0.0268 | 0.04139 | 0.0413 |
   | 18.8 | 0.02558 | - | 0.02635 | 0.04222 | 0.04128 |
   | 20.5 | 0.02427 | 0.03415 | 0.02516 | 0.04278 | 0.04075 |
   | 22 | 0.02171 | - | 0.02277 | 0.04266 | 0.03966 |
   | 23.6 | 0.01775 | - | 0.01898 | 0.04155 | 0.03748 |
   | 25.1 | 0.01479 | 0.0277 | 0.01605 | 0.04095 | 0.0362 |
   | 27 | 0.007769 | - | 0.008352 | 0.03052 | 0.02616 |
   | 30 | 0.004506 | 0.01155 | 0.004695 | 0.02396 | 0.01995 |
   | 34 | 0.003237 | - | 0.003285 | 0.019 | 0.01523 |
   | 40 | 0.002307 | 0.005785 | 0.002324 | 0.0145 | 0.01097 |
   | 60 | 0.001022 | 0.002578 | 0.001025 | 0.007776 | 0.004992 |
   | 100 | - | 0.0009781 | - | 0.003682 | 0.00188 |
   | 200 | - | 0.0002649 | - | 0.001323 | 0.0004726 |
   | 500 | - | 4.579e-05 | - | 0.0002789 | 5.857e-05 |
   Sources:
   - The direct columns are the max over 5 angles of the s0 and s0.5 rows of the hsb_far run of item 1(a). That run
     has no rows beyond |xi| = 60.
   - CS h = 1, and CS h = <xi>^-1/2 at the 20 |xi| of that run: runs/cs_route_1825.log, with JSON
     runs/cs_route_float_N6912_RW200_WW200_sh.json.
   - Capped weights and the other 8 |xi| of h = <xi>^-1/2:
     - runs/far_cs_1830.log for |xi| <= 4;
     - runs/cs_cap_1842.log for |xi| >= 5;
     - JSON runs/cs_route_float_N6912_RW200_WW200_cap.json, which holds the rows |xi| >= 5 only. The run in
       far_cs_1830.log was killed after its rows |xi| <= 5 (see the second theory agent work log 18:42Z).
   Other sampled weights, with their sups:
   - On the 28 values: h = <min(|xi|, T)>^-s gives 0.0421 for (s, T) = (0.75, 10), 0.0433 for (0.5, 20), 0.0470 for
     (0.75, 14) and 0.0500 for (1, 10).
   - On the 20 values: h = <xi>^-1 gives 0.1034 and h = <xi>^-3/2 gives 0.3925.
   - On |xi| <= 5 only: h = <xi>^-1/4 gives 0.0526 and h = <min(|xi|, 12)>^-1/2 gives 0.0358, both at xi = 0.
   The optimal c (FLOAT): only integer orders carry weight. At |xi| = 17.5 with h = <min(|xi|, 6.3)>^-1, c is
   proportional to 0.02, 0.042, 1 and 0.21 for s = 1, 2, 3 and 5, and below 1e-12 for the other orders.
   Engine check of the D_s (code/c1/far_energy_float.py -3 16 0.25 8 6 192; unwindowed, all 161 modes):
   - D_1 to D_5 = 2.111074, 1.077206, 1.383243, 3.326287, 12.40048. The Cartesian and Laplacian forms agree to 7
     digits.
   - The FFT values of the windowed field (2.0965, 1.0772, 1.38302, 3.32147, 12.3026) are lower by at most 0.8
     percent.
   - The part r > 200 is 2.7 percent of E_1. The last unit block 15 <= y < 16 carries 1.3e-5 of E_1.
   - At fixed c the bound is increasing in each D_s. So the engine values raise every FLOAT CS number above by a
     factor of at most 12.40048/12.3026 < 1.0080. For example, 0.0413 becomes at most 0.0417 and 0.1241 at most
     0.1251.
   Reading (FLOAT):
   - The loss of Cauchy-Schwarz is large where the direct row is small. At xi = 0 with h = 1, r_B vanishes unless
     |eta| > 2 pi, but D_s counts every frequency. A weight that decreases in |xi| removes this loss.
   - Near the row maximum (14 <= |xi| <= 22) the loss is a factor of 1.4 to 1.9.
   - The six weights sampled on all 28 values stay below the budget by a factor of at least 3.6, even after the engine
     correction. On the 20 values, h = 1 and h = <xi>^-1 stay below it only by factors of 1.5 and 1.8, and
     h = <xi>^-3/2 exceeds it.

4. What route B needs for a certificate, with HEURISTIC costs.
   (B1) Certified uppers D_s^+ >= D_s(a_f) for s = 1, ..., 5, unwindowed, with all modes. Item 3 shows that s = 1, 2,
        3 and 5 suffice in FLOAT.
        Pieces that exist:
        - the cell uppers Phi_k of code/c1/tail_deriv.py, for the angular means of |grad^k a_f|_F^2 with k <= 5 on
          3.75 <= y <= 16 (used for the tail moments; CONFIRMED, AT1336-1342);
        - the Region III bound of code/c1/tail_moments_v2.py section 2(c), for m = 2, ..., 5;
        - Region I of code/c1/c1_tails.py, for orders <= 2.
        To add:
        - a tail_deriv run on -4 <= y <= 3.75 (20 to 40 min of one core);
        - Region I to order 5, and Region III at m = 1;
        - the sum, rounded up.
        Cost: 2 to 4 hours of code.
   (B2) A certified upper of the supremum over |xi| of (1/(4 pi)) (sum_s c_s D_s^+2)^(1/2) K^(1/2), with c fixed on
        |xi|-cells. It needs:
        - an enclosure of K over each cell, by interval quadrature in (|zeta|, angle) of the elementary integrand;
          the ramp kinks and the point eta = 0 are handled by enclosure, with |w - w'|^2 <= 4;
        - explicit tails at both ends of |zeta|:
          - near zeta = 0, |r_B| <= C(xi) |zeta|^2 for |xi| >= 2 pi, while r_B = 0 when |xi| and |eta| are both below
            2 pi;
          - at infinity, a power bound on |r_B| with w^2 >= c_5 |zeta|^10;
        - a lemma for |xi| >= T. In FLOAT the h = 1 CS row falls to 0.0115 at 30 and 4.6e-5 at 500.
        Cost: 5 to 8 hours of code, including the two tail lemmas, plus 1 to 3 core-hours.
   (B3) The assembly, with an exact comparison to Gbar - SC^+ (code/c1/f_assembly.py takes S^+). Cost: under 1 hour.
   Total: 8 to 13 hours of code plus 2 to 4 core-hours, then review by the theory auditor.
   Scope:
   - Route B also gives S^+ for the windowed a_W of route F-a. The FFT D_s above are those of a_W at Rw 200, Ww 200,
     and the transition cells of tail_moments_v2.py section 2(a) give windowed energies.
   - It does not give what the other consumers of C3 need (C2 signed enclosures, T2, T3, X2).

5. Plan. Unless X7 decides otherwise, the second theory agent writes the B1 code now. The B1 run waits until req48 row 3 ends, which
   has moved to about 20:15Z after this shift's holds (HEURISTIC). B2 follows.

6. Commands (from research/h4/far009/; 8 modes, N 6912, Rw 200, Ww 200 are the defaults or set as shown):
   - python3 code/c1/cs_route_float_1825_record.py 6912 (the default |xi| list and weights 0, 0.5, 1, 1.5). This is
     the version that ran at 18:25Z, kept byte for byte. code/c1/cs_route_float.py adds only the 's@T' weights and
     CSOUT. Its rows for h = <xi>^-1/2 agree with those of the record run at all 14 common |xi|, to the last binary64
     digit.
   - SH='0.25,0.5,0.5@12,0.5@20,0.75@10,0.75@14,1@6.3,1@10' python3 code/c1/cs_route_float.py 6912 <|xi| list>
   - SH='0.5,0.5@20,0.75@10,0.75@14,1@6.3,1@10' python3 code/c1/cs_route_float.py 6912
     5,6.3,8,9.4,11,12.6,14,15.7,17.5,18.8,20.5,22,23.6,25.1,27,30,34,40,60,100,200,500
   - python3 code/c1/far_energy_float.py -3 16 0.25 8 6 192
   Files (SHA256):
   - code/c1/cs_route_float.py 74c10fce526261f0fc99e95e4367f96da535e94f21c69db30c54c5c5d5d7e99b
   - code/c1/cs_route_float_1825_record.py c6a00eab8d8e878f8c73fba29f1e4b8c57f6706778def334171f4b4875d060e4
   - code/c1/far_energy_float.py c87fea91d8a6f2ec45b7d9c4ad499806aefafedeaef28151650413b3e89b9f9d
   - code/c1/near_energy_float.py 8aaead3a179f3a276bf2a0452b6c2d96f25fbc0764803a8ebfcab0d4dfb7bfc9
   - code/hsb_far.py 805dc2c35a3a9ecc9b49dc392ba692161ce95d2f58b1fc2c7ff38a2a6c39a253
   - runs/cs_route_1825.log b8f5755efaa7bd52e55484a4364009bbc40e33d7afac37d8bca8067d9e00cc49
   - runs/far_cs_1830.log db793ef8371e6986f630fbca0e7755ea251465025a17660b95d025515e0c17ed
   - runs/cs_cap_1842.log 9629bbd8c3f5f96ed2e14cc58d6d2f8c53da14a16b96e1f22ce2875424a72799
   - runs/cs_route_float_N6912_RW200_WW200_sh.json 0d7dcdb7400f91347b15f3056a91203d0c7e2848605b009382c2305e78296315
   - runs/cs_route_float_N6912_RW200_WW200_cap.json cfc9775ce68245797ccce8f7c3761313b213c9767f67e534877ccac075d50af1
   - runs/hsb_erflog_lam8_b18s2_N6912_RW200_WW200.json fe48a8a62244a0608be6ae01861ead2431190dc12614f8492a426d697e179335
