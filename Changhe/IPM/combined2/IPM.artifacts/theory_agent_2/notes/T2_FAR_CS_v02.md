# T2_FAR_CS_v02: rows C3 and C4 by route B: S_h^B(a_f) <= S^+ = 0.059699233948103884 with h = <min(|xi|, 63/10)>^-1, and SC^+ + S^+ <= Gbar exactly (Theorem CS-B, CLAIMED)

Agent the second theory agent, written 2026-11-03T20:02Z as steps B1 to B3 of notes/T2_FAR_CS_v01.md item 4 (route B for rows C3 and C4 of
notes/T2_013_FAR_OWNERS_v01.md section 2.1). Everything here is CLAIMED and submitted to the theory auditor. Code and runs paths
are relative to research/h4/far009/ of agent the second theory agent, and notes/ paths to the agent directory. Numbers marked FLOAT are sampled
values used for steering or comparison only; no bound depends on them.

0. Summary.
   - Theorem CS-B (item 1, CLAIMED): with h = <min(|xi|, 63/10)>^-1,
       S_h^B(a_f; 2 pi, 8 pi, h) <= S^+ = 0.059699233948103884   (binary64),
     and SC^+ + S^+ <= Gbar holds exactly, with room 91024360093424573/720575940379279360 > 0.126321 (exact rational in the B3 file).
   - So (F1) of Proposition F (notes/T2_FAR_F_v01.md section 2) holds with this h and S^+, and so does the SC half of
     (F3). The other half of (F3) becomes A_low^+ <= Gbar - S^+ = 426560137443922093/720575940379279360 > 0.591971 (row C2, still OPEN; FLOAT band value 0.3848).
   - The FLOAT value of the same Cauchy-Schwarz bound is 0.0413 (T2_FAR_CS_v01 item 3), and the direct FLOAT row sup
     with h = 1 is 0.026142. The certified S^+ is larger because each |xi|-cell is refined only until its bound is at
     most TARGET = 0.06 (item 3(f)).
   - Inputs that are new here and need review: the energies D_s^+ (B1, item 2), the identity of Lemma KP (item 3(b)),
     the enclosure code (item 3(c)), Lemma KT for |xi| >= 200 (item 3(e)) and the assembly (item 4). Lemma CS-S itself
     is item 2 of T2_FAR_CS_v01 (CLAIMED, 18:58Z).

1. Statement.
   Setting: that of Proposition F (notes/T2_FAR_F_v01.md section 2): a_f = chi_E(|x|) atil_013(x) at erflog 8,
   rho 1, unwindowed and with all angular modes, q = 21/10, K = 2 pi, K' = 8 pi, r_B, Ktil, P, the ramp and S_h^B as in
   T2_FAR_v02 section 2.3, SC^+ = 0.46564943200002806 (Theorem C1), Gbar = q (c - 3/2) =
   14674311533937489/22517998136852480.
   Theorem CS-B (CLAIMED). Let h(xi) = (1 + min(|xi|, 63/10)^2)^(-1/2). Then
       S_h^B(a_f; 2 pi, 8 pi, h) <= S^+ = 0.059699233948103884,
   and S^+ <= Gbar - SC^+ = 8377636983468883/45035996273704960.
   Proof. Lemma CS-S (T2_FAR_CS_v01 item 2) with Sigma = {1, 2, 3, 4, 5}: h is positive, radial and continuous, and
   the D_s are finite by item 2. For every xi,
       rho_h^B(xi) <= (1/(4 pi)) (sum_s c_s D_s^2)^(1/2) K(xi)^(1/2)
   for any c_s >= 0 not all 0, which may depend on |xi|. On each cell t0 <= |xi| <= t1 of item 3(f) the c_s are fixed
   and listed in the cell file; for |xi| >= 200 they are those of the tail file. D_s <= D_s^+ (item 2), K <= the cell
   upper K^+ (items 3(a) to 3(d)) or the Lemma KT upper (item 3(e)), and the right side is increasing in each D_s and
   in K. So rho_h^B(xi) is at most the bound of the cell or of the tail that contains |xi|, and S^+ is the largest of
   these bounds (item 4). The comparison with Gbar - SC^+ is exact (item 4). QED.

2. B1: D_s^+ (code/c1/ds_upper.py; runs/ds_upper_1926.json).
   D_m^2 = ||grad^m a_f||^2 (Frobenius) = (2 pi)^-2 int |zeta|^(2m) |a_f^|^2, split at r0 = e^-4 and R1 = e^16:
   - E_II, e^-4 <= r <= e^16: the cell uppers Phi_m^+ of code/c1/tail_deriv.py (angular means of |grad^m a_f|_F^2),
     from two records that cover [-4, 16] without gaps: runs/tail_deriv_1905.jsonl (new, -4 <= y <= 3.75, 248
     panels, max panel remainder 1.14e-9) and runs/tail_deriv_1557.jsonl (3.75 <= y <= 16, the record whose code was
     CONFIRMED in AT1336-1342). A cell [ylo, yhi] adds pi Phi_m^+ (e^(2 yhi) - e^(2 ylo)).
   - E_III, r >= e^16: region3_env of code/c1/tail_moments_v2.py section 2(c), with m from 1 instead of 2.
   - E_I, r <= e^-4: Region I of code/c1/c1_tails.py to order 5, with the cut factors bounded by Hermite majorants
     whose sup over y <= -4 is at y = -4 (monotonicity asserted), and Leibniz.
   Results (arb, rounded up):
   | m | D_m^+ | E_II upper | E_III upper | FLOAT engine D_m | D_m^+ / engine |
   |---|---|---|---|---|---|
   | 1 | 2.1163361261353364 | 4.478783654239656 | 9.494454586680407e-05 | 2.111074 | 1.002493 |
   | 2 | 1.0811148704835174 | 1.1688093631805923 | 1.3947624732152818e-17 | 1.077206 | 1.003629 |
   | 3 | 1.3899825385469313 | 1.9320514574653713 | 6.916949400531326e-30 | 1.383243 | 1.004872 |
   | 4 | 3.34556428129887 | 11.192800360302822 | 6.333483133895034e-42 | 3.326287 | 1.005795 |
   | 5 | 12.481886685910556 | 155.7974952399112 | 9.293391384059124e-54 | 12.40048 | 1.006565 |
   The engine column is the FLOAT value of T2_FAR_CS_v01 item 3 (code/c1/far_energy_float.py); the last column is
   rounded to 6 digits.
   E_I is between 2.7e-53 and 4.6e-26 for every m. The FLOAT Cauchy-Schwarz sup 0.0413 of T2_FAR_CS_v01 item 3 was
   computed with the FFT energies (2.0965, 1.0772, 1.38302, 3.32147, 12.3026). The bound is increasing in each D_s,
   and the largest ratio D_m^+/FFT is 12.481886685910556/12.3026 < 1.01458, so with the D_m^+ it becomes at most
   0.0413 x 1.01458, about 0.0419 (FLOAT).

3. B2: the kernel integral K (code/c1/k_cells.py for |xi| <= 200, code/c1/k_tail.py for |xi| >= 200).
   (a) Reduction. K depends on t = |xi| only; take xi = (t, 0), zeta = rho (cos psi, sin psi), eta = xi - zeta,
       v = |eta|. The integrand is even in psi (reflection in the xi axis keeps |eta|, xi.eta, zeta.w and zeta.w'), so
       with psi = pi sigma
         K(t) = 2 pi int_0^1 int_0^inf R(t, rho, psi) g(rho) d rho d sigma,
         R = (r_B/rho^2)^2 H^2,  H^2 = (1 + min(t, TH)^2)/(1 + min(v, TH)^2),  TH = 63/10,
         g(rho) = rho^5/w(rho)^2 = rho^3/(c_1 + c_2 rho^2 + c_3 rho^4 + c_4 rho^6 + c_5 rho^8).
   (b) Lemma KP (exact identity). Write u = t, a = <u>, b = <v>, c = cos of the angle between xi and eta, omega = 1 - c,
       tau = log(a/b), f(tau) = sinh^2(q tau/2) - q^2 sinh^2(tau/2). Then
         Ktil = 2 a b omega + 4 a b sinh^2(q tau/2),
         Ktil - P = 2 omega (a b - u v) + q^2 omega (u - v)^2 + (q^2 + 1) u v omega^2 + 4 a b f(tau)
                    - q^2 (u - v)^2 (1/(a + u) + 1/(b + v)) (a + b + u + v)/(a + b)^2,
         r_B = 2 sin^2((alpha - beta)/2) Ktil + phi phi' (Ktil - P),
       where alpha, beta are the ramp angles at u, v and phi = sin alpha, phi' = sin beta.
       Proof.
       - |w - w'|^2 = 2 omega, and (a^q - b^q)^2 (a b)^(1 - q) = a b ((a/b)^(q/2) - (b/a)^(q/2))^2 = 4 a b sinh^2(q tau/2).
       - zeta.w = u - v c and zeta.w' = u c - v, |zeta|^2 = u^2 + v^2 - 2 u v c. Expanding P = |zeta|^2 c +
         (q^2 - 1)(u - v c)(u c - v) in powers of omega with u^2 + v^2 = (u - v)^2 + 2 u v gives
         P = q^2 (u - v)^2 + omega (2 u v - q^2 (u - v)^2) - (q^2 + 1) u v omega^2.
       - 4 a b sinh^2(q tau/2) - q^2 (u - v)^2 = 4 a b f(tau) + q^2 ((a - b)^2 - (u - v)^2), since
         4 a b sinh^2(tau/2) = (a - b)^2.
       - a - b = (u^2 - v^2)/(a + b), u - v = (u^2 - v^2)/(u + v), so (a - b)^2 - (u - v)^2 =
         -(u - v)^2 (a + b - u - v)(a + b + u + v)/(a + b)^2, and a + b - u - v = 1/(a + u) + 1/(b + v).
       - r_B = (1 - theta theta') Ktil - phi phi' P and 1 - theta theta' = 1 - cos(alpha - beta) + phi phi'. QED.
       Every term except the last of Ktil - P is >= 0, and each is a product of factors that can be enclosed without
       cancellation:
       - omega = rho^2 sin^2 psi/(v (v + eta_1)) when eta_1 > 0 (then also omega <= 1), else 1 - eta_1/v;
       - u - v = rho (2 t cos psi - rho)/(t + v), a - b = rho (2 t cos psi - rho)/(a + b), a b - u v =
         (1 + u^2 + v^2)/(a b + u v), tau = log1p((a - b)/b);
       - f(tau) = tau^4 F(tau^2), F(z) = sum_(n >= 2) z^(n - 2) (q^(2n) - q^2)/(2 (2n)!), all coefficients >= 0.
       The identity was also checked in FLOAT at random points against the direct formulas (scratch).
   (c) Enclosure of R on a box [t0, t1] x [rho0, rho1] x [pi sigma0, pi sigma1]. Binary64 intervals (lo, hi): +, -,
       *, / and sqrt are correctly rounded in IEEE binary64, and each result is moved one step outward by nextafter.
       Monotone transcendental functions are evaluated at the exact binary64 interval endpoints with arb (96 bits)
       and rounded outward: log1p(x)/x (decreasing), log1p(x) (increasing; tau and tau/rho are intersected with it),
       sinh(y)/y (increasing in |y|), F (increasing; for z <= 1 the partial sum to n = 12 plus at most z^11 (F(1) minus
       that partial sum at 1)), sin(pi l/2) and 2 sin^2(pi m/4) on [0, 1] (increasing), cos(pi s) and sin(pi s) on
       [0, 1]. The ramp coordinate l = clip((x - 2 pi)/(6 pi), 0, 1) is increasing. A lower end below 0 of a
       quantity that is >= 0 by construction (squares, 1 + t^2, e^2 + (rho sin psi)^2) is replaced by 0.
       Check: at 400 random point boxes the enclosure contains the FLOAT value of R; the largest relative width is
       2.2e-6 (scratch).
   (d) Integration and the two ends of rho.
       - A box adds 2 pi (sigma1 - sigma0) sup R int_rho0^rho1 g, with the integral of g bounded by 64 equal pieces,
         g <= p1^3/Q(p0) on [p0, p1] (g has increasing numerator and Q increasing); on a piece that starts at 0,
         min(p1^4/(4 c_1), p1^2/(2 c_2)). In arb.
       - Zero region: if t1 <= 2 pi and rho1 + t1 <= 2 pi, both |xi| and |eta| are at most 2 pi, both ramp angles
         are 0 and r_B = 0, so the box adds 0.
       - rho >= RMAX = 10^6 (T = 200 <= RMAX/4): |r_B| <= Ktil + |P| <= C rho^(1 + q) with C = 4 (1 + T) beta
         RMAX^(-q) + beta^(1 + q) + q^2 RMAX^(1 - q), beta = 5/4 + 1/RMAX (b <= 1 + T + rho <= beta rho, a <= 1 + T,
         Ktil <= 4 a b + b^(1 + q) for b >= a, |P| <= q^2 rho^2); H <= 1 since v >= 3 RMAX/4 > TH; w^2 >= c_5 rho^10.
         So this part of K is at most 2 pi C^2 RMAX^(2q - 6)/(c_5 (6 - 2q)) (about 5e-10 at c_5 near 0.4).
       - The initial grid is rho in {0, 1/32, 1/32 * 1.25^k} up to RMAX and 16 equal sigma intervals. Boxes are split
         into four (geometric mean in rho, or rho1/2 when rho0 = 0; midpoint in sigma) in decreasing order of their
         upper minus lower contribution. The certified K^+ is the arb sum of the final box uppers plus the rho >= RMAX
         part.
   (e) Lemma KT (|xi| >= T). Let T >= 64 and c_1, ..., c_5 >= 0 with c_5 > 0 and c_1 + c_2 > 0. For every t >= T,
         K(t) <= K1 + K2a + K2b,
         K1 = (2 pi/T^4) [I(P) + B_P log 2],  P = T/4,  I(P) = int_0^P (A2 + A4 rho^2)^2 rho^3/Q(rho) d rho,
              B_P = (A2/P^2 + A4)^2/c_5,  A2 = 5 + 4/T^2 + 2 q^2,  A4 = 6 (q^2 + 1) + 96 (1 + 1/T^2) F(1) + 2 q^2,
         K2a = 3 (1 + TH^2) (4/3)^10/(c_5 T^10) [16 alpha^2 T^2 pi ((T/4)^2 + (T/4)^4/2)
               + alpha^(2 + 2q) T^(2 + 2q) pi/(q - 2) + q^4 (5T/4)^4 pi T^2/16],  alpha = (1 + 1/T^2)^(1/2),
         K2b = (4 pi/c_5) [(4 gamma^2 + q^2)^2 (T/2)^-4/4 + gamma^(2 + 2q) (4/T)^(2q - 2) (T/2)^(2q - 6)/(6 - 2q)],
               gamma = 3 + 2/T,
       with Q(rho) = c_1 + c_2 rho^2 + ... + c_5 rho^8.
       Proof. The sets R1 = {rho <= t/2}, R2a = {v <= t/4} and R2b = {rho > t/2, v > t/4} cover the plane and the
       integrand is >= 0.
       - R1: v is in [t/2, 3t/2], eta_1 >= t/2, and t, v >= 32 > 8 pi and > TH, so theta = theta' = 0,
         phi = phi' = 1, H = 1 and r_B = Ktil - P. In Lemma KP: omega <= 2 rho^2/t^2; a b - u v <=
         (1 + t^2 + v^2)/(2 t v) <= 5/4 + 1/T^2; u v <= 3 t^2/2; |tau| <= |u - v|/min(u, v) <= 2 rho/t <= 1, so
         f(tau) <= tau^4 F(1); a b <= (3/2)(1 + 1/T^2) t^2; |u - v| <= rho; and the negative term is at most
         q^2 rho^2 (3/(2t)) (4/(3t)) = 2 q^2 rho^2/t^2. Hence |r_B| <= (A2 rho^2 + A4 rho^4)/t^2 and
         int_R1 <= (2 pi/t^4) int_0^(t/2) (A2 + A4 rho^2)^2 rho^3/Q. On [P, t/2], (A2 + A4 rho^2)^2 rho^3/Q <=
         (A2/P^2 + A4)^2/(c_5 rho). So int_R1 <= (2 pi/t^4)[I(P) + B_P log(t/(2P))], which is decreasing in t >= T
         because t/(2P) >= 2 and 4 log 2 > 1. I(P) is an upper Riemann sum (ratio 1.001 from 10^-3, a first piece
         as in (d)).
       - R2a: rho is in [3t/4, 5t/4], a >= b, Ktil <= 4 a b + a^(1 + q) b^(1 - q), |P| <= q^2 rho^2, a <= alpha t,
         H^2 <= 1 + TH^2, w^2 >= c_5 (3t/4)^10, (x + y + z)^2 <= 3 (x^2 + y^2 + z^2), int_(v <= t/4) b^2 =
         pi ((t/4)^2 + (t/4)^4/2) and int_(R^2) b^(2 - 2q) = pi/(q - 2).
       - R2b: a, b >= t/4, max(a, b) <= 1 + t + rho <= gamma rho, H = 1 (t, v >= 16 > TH), |r_B| <= (4 gamma^2 + q^2)
         rho^2 + gamma^(1 + q) (4/t)^(q - 1) rho^(1 + q), (x + y)^2 <= 2 x^2 + 2 y^2, w^2 >= c_5 rho^10.
       K2a and K2b are sums of negative powers of t, so all three parts take their sup over t >= T at t = T. QED.
       The c of the tail are chosen by a FLOAT minimization of the bound (any admissible c gives a valid bound).
   (f) Cells and results.
       - Cells (exact binary64 endpoints, contiguity asserted): [0, 30] in 120 cells of width 1/4, [30, 60] in 60 of
         width 1/2, [60, 120] in 60 of width 1, [120, 200] in 40 of width 2; 280 cells. The cell bound is
         (1/(4 pi)) (sum_s c_s (D_s^+)^2)^(1/2) (K^+)^(1/2), in arb, rounded up.
       - c per cell: FLOAT minimization of the FLOAT bound at the cell midpoint (2401 log radii on [1e-4, 1e6], 720
         angles, L-BFGS-B over log c, floor 1e-9). The c are stored in the cell file. Smallest c_5: 0.14999.
       - Stopping: EPS 0.3, NMAX 30000, TARGET 0.06. All 280 cells stopped by TARGET; none reached NMAX. Boxes per
         cell: 1264 to 9572 (745472 in all). Wall time 1129 s on one core.
       - The rho >= RMAX part of K is at most 1.48e-9 in every cell.
       Results (cell bounds; "FLOAT" is the FLOAT value at the cell midpoint; "lower" is the same bound evaluated at
       the lower Riemann sum of the final boxes, which is a lower bound of K on the cell for that c, reported for
       tightness only):
       | |xi| range | cells | largest cell bound | largest FLOAT | largest lower |
       |---|---|---|---|---|
       | [0, 6.25] | 25 | 0.0596915 | 0.03532 | 0.02209 |
       | [6.25, 30] | 95 | 0.0596992 | 0.04190 | 0.02988 |
       | [30, 60] | 60 | 0.0595992 | 0.01986 | 0.007828 |
       | [60, 120] | 60 | 0.0596182 | 0.004984 | 0.0009987 |
       | [120, 200] | 40 | 0.0574212 | 0.001342 | 0.0002509 |
       (The displayed bounds are rounded to 6 digits; the exact largest is 0.059699233948103884, at the cell
       [15.75, 16].) In every cell the FLOAT midpoint value lies between the lower and the bound. The largest FLOAT
       value, 0.041901 at [18, 18.25], is consistent with the FLOAT sampled sup 0.0413 of T2_FAR_CS_v01 item 3 (FFT
       energies) times max_s D_s^+/D_s(FFT) = 12.481886685910556/12.3026 < 1.01458, which is about 0.04190.
       - Lemma KT at T = 200 (code/c1/k_tail.py, runs/k_tail_2000.json): c = (1e-12, 1, 1e-12, 1e-12,
         0.7761365363491166); K1 <= 1.4517e-4, K2a <= 1.7469e-4, K2b <= 4.5005e-4 (displays rounded up); bound for
         every |xi| >= 200: 0.02439746168426851. The FLOAT value of the same expression is 0.024383.

4. B3: assembly (code/c1/cs_assembly.py; runs/cs_assembly_2001.json).
   - Checks in the code: the cell file is complete and not a test file (ALLOWGAP off), the 280 cells are sorted and
     contiguous from 0 to T = 200, the tail file has the same T and the same D_s^+ file, every bound is finite and
     positive.
   - S^+ = max(cell bounds, tail bound) = 0.059699233948103884 = 8603566328415511/144115188075855872 (the cell
     [15.75, 16]).
   - SC^+ = 0.46564943200002806 and Gbar are read as in code/c1/f_assembly.py. Gbar - SC^+ =
     8377636983468883/45035996273704960, and SC^+ + S^+ <= Gbar is True, with room
     Gbar - SC^+ - S^+ = 91024360093424573/720575940379279360 > 0.126321.
   - For row C2: Gbar - S^+ = 426560137443922093/720575940379279360 > 0.591971 is the room left for A_low^+.
   - f_assembly.py (which also needs A_low^+) is not run, since row C2 is OPEN.

5. For review by the theory auditor.
   - Lemma KP (item 3(b)) and its use in box_R of code/c1/k_cells.py (each factor and each monotonicity claim of
     item 3(c)).
   - The outward rounding of the binary64 interval operations and the arb endpoint evaluations (item 3(c)).
   - The rho >= RMAX part, the zero region and the first piece of the g integral (item 3(d)).
   - Lemma KT (item 3(e)) and code/c1/k_tail.py.
   - B1 (item 2): the Region I extension to order 5, Region III at m = 1, and the new tail_deriv record on
     -4 <= y <= 3.75 (same code as the CONFIRMED record).
   - The assembly (item 4): coverage of [0, 200] by contiguous cells, the same D_s^+ in both B2 files, and the exact
     comparison.
   - Lemma CS-S (T2_FAR_CS_v01 item 2).

6. Run notes.
   - All runs on one core (taskset, nice 19, OMP_NUM_THREADS=1). Each run held the req48 row 3 job of this agent
     (python 345729, FLOAT) with SIGSTOP through code/c1/with_pause_core.sh, logged in runs/pauses_shift4.log:
     tail_deriv 19:05:57Z to 19:25:22Z, ds_upper 19:26:05Z to 19:26:10Z, one-cell tests between 19:26:27Z and
     19:40:54Z, the cell run 19:41:06Z to 19:59:57Z, k_tail 20:00:56Z to 20:00:59Z.
   - Deviation from T2_FAR_CS_v01 item 5: the B1 run did not wait for the end of req48 row 3; it held row 3 instead.
   - Fixes made before the cell run, each found by a one-cell test (the second theory agent work log 19:52Z): zero lower ends moved
     below 0 by nextafter are clamped at 0 for quantities >= 0 by construction; the refinement loop resums with
     math.fsum (its running sums had lost accuracy, which ended a test early; the reported sum was always taken
     from the final boxes); omega/rho^2 <= 1/rho0^2 when eta_1 > 0, and the intersection of tau with log1p at the
     endpoints of x (both remove dependency blow-ups near eta = 0 and at large rho). code/c1/k_cells_1941_record.py
     is a byte copy of the version that ran.
   - The c, EPS, NMAX and TARGET only steer the work: any c >= 0 with c_5 > 0 and c_1 + c_2 > 0 gives a valid bound,
     and the reported upper is summed from the final boxes whatever the stopping rule.

7. Commands (from research/h4/far009/) and files.
   - python3 code/c1/tail_deriv.py -4 3.75 0.015625 34 8 5 256 runs/tail_deriv_1905.jsonl (1163.5 s)
   - python3 code/c1/ds_upper.py -4 256 runs/ds_upper_1926.json runs/tail_deriv_1905.jsonl runs/tail_deriv_1557.jsonl
     (4.4 s)
   - EPS=0.3 NMAX=30000 TARGET=0.06 python3 code/c1/k_cells.py runs/ds_upper_1926.json
     0:30:120,30:60:60,60:120:60,120:200:40 runs/k_cells_1941.json (log runs/k_cells_1941.log; 1129 s)
   - python3 code/c1/k_tail.py runs/ds_upper_1926.json 200 runs/k_tail_2000.json (1.6 s)
   - python3 code/c1/cs_assembly.py runs/k_cells_1941.json runs/k_tail_2000.json runs/cs_assembly_2001.json (< 1 s)
   Python 3.12.13, python-flint 0.9.0; numpy and scipy only for the FLOAT choice of c.
   SHA256:
   - code/c1/k_cells.py 68af822acae61a314befce6083de2de11a717deca79be89fb3db8a6a7843bf2c (= k_cells_1941_record.py)
   - code/c1/k_tail.py dc064662b5b2da39c8ef84d77f951f85f18738bd6dd5eb237cd470417e55b889
   - code/c1/cs_assembly.py bace4162214d1842b7510e39989caeac0e7bc9cc76e66397a08d5496d1c26290
   - code/c1/ds_upper.py 083c6ad0dc66598a193361892ad4ba0d19415092f2659deae008e87afe05d375
   - code/c1/tail_deriv.py d8451f80f7fd2779cbd1514b7fe556c3ec287b07249f273bdb54cdb04ae2a503
   - code/c1/c1_sc.py 87bd58e86ccc08c264fa04b053a5c49d1d0ca01fb318dd80ed3e984a2f992f51
   - code/c1/c1_tails.py c65b24c13ec869e6a5071f4000bd96ee3823358baec7d4a16257049b4c2a1d9c
   - runs/tail_deriv_1905.jsonl e483c240360adad7a0fb2712826c43c2765832676ce324e14fc08e3e466526ec
   - runs/tail_deriv_1557.jsonl ae179b9d78296b694b7006a45d329d3a83bc41258c3e2c3310b00b602c99a98d
   - runs/ds_upper_1926.json 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5
   - runs/k_cells_1941.json 38735c097f0367c0e287be0eb015ece869056c8487d7bedb964490567cc93d8b
   - runs/k_cells_1941.log d15e4b9bae14f96154aa2f1cc9dbc3fafac1c315ee8e8472b4c6bab8bb4ed1de
   - runs/k_tail_2000.json 9d17f52c5f98afffa2d46092b8561a78d035df021b90ce0fc1978c3e6c54bda6
   - runs/cs_assembly_2001.json 390481a858d191514e59fbbea671c0d1a90c1602c80649d5b457751188f7bdda
