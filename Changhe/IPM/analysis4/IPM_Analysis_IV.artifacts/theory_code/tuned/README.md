# Tuned pure series at delta = 2/3 (Theorem T, Section 12.4 of the theory)

All scripts run from this directory with Python 3 (numpy, sympy, mpmath); single thread.

- `o6_sym.py 3`: exact first obstruction O_6 for f_1 = sin(theta) + b sin(3 theta); prints O_6 = P6(b)/35818438656000000.
- `irr.py`: P6 is irreducible over Q, content 1, and has exactly two real roots (isolating intervals (1/4,1/3), (1/2,1)).
- `sigma_sym.py`: exact response coefficients sigma_k (numeric k and symbolic k).
- `sigma_check.py` -> `sigma_check.json`: generic sigma(k) for k >= 7, gcd of its b-coefficients, sigma_infinity,
  exact sigma_2..sigma_6, values at both roots.
- `sigma_min.py` -> `sigma_min.json`: min over 2 <= k <= 10^5 of |sigma_k| at both roots (at k = 4).
- `r2_exact.py` -> `r2_exact.json`: R_2 computed in Q(b*) (reduction mod P6), nonzero of degree 5; exact H_6.
- `tuned.py`, `diag2.py N b 3`: double-precision tuned series (FFT, exact support imposed); outputs `diag2_root*_N*.txt`
  (every third order: l1 norm and its n-th root, the untuned comparison run with H = 0 and obstructions ignored,
  H_n, |H_n|^(1/n), finite-difference slope, residual obstruction).
- `fitroot.py`: least-squares fit log l1 = n log A + beta log n + c.
- `tuned_mp.py N dps root` -> `tuned_mp_root0_N30.json`: 40-digit tuned series with H_n = -R_k/sigma_k.
- `sigma_bound_check.py` -> `.out`: exact certificate |sigma_k| >= 1/100000 for every k >= 2 at both roots (k <= 6 by
  rational interval evaluation on isolating intervals of width 1e-30; k >= 7 by nonnegative coefficients in t after k = t+7).
- `sigma_bound_check2.py` -> `.out`: the same with the per-root bounds 3.8e-5 (b1) and 1.5e-3 (b2).
- `majorant_disk_check.py` -> `.out`: exact check of the explicit majorant disk z0 = 2^-120 (M = 2^55) with a = 2,
  kappa = 10, sigma_* = 1e-5 (radius r > 2^180 |eps|^(3/2)).
- `majorant_opt.py` -> `.out`: critical z of the majorant system with a = 1+b, kappa = 28/3 and the per-root sigma bounds
  (bisection, float), and an exact rational supersolution Phi(z1, Yhat) <= Yhat at z1 = 0.99 z_c (radii 2.6e16 and 4.7e14).
- sigma_inf_check.py / .out: exact certificate that inf_{k>=2}|sigma_k| = -sigma_4 at both roots, attained only at k=4
  (Corollary T.3(c)).
- component_box_check.py / .out: componentwise supersolution boxes B=2Qc for the majorant system (Corollary T.4 radii
  2^63, 2^57, 2^51; Corollary T.7 radius 2^72) and the scalar box of the three-mode family (2^240).
- o6_threemode.py / .out: exact O_6 for sin+b sin3+tau sin5 by the Fourier recurrence, comparison with an independent
  Cartesian computation, and the circle (Rouche) certificate of Corollary T.7.
- tq_sym.py Q M [kmax]: exact first obstruction O_2Q and response coefficients sigma_k at delta = 2/Q for
  f_1 = sin + b sin(M theta), in Q(k)[b] with k symbolic (valid for k >= QB/2+1) and for numeric k (theory Section 12.5).
  Validated at Q=3 against o6_sym.py / sigma_sym.py. Output for Q=5, M=3: tq_Q5_M3.out.
- tq5_cert.py / .out: certificate for Corollary T_5(a): P10 primitive and irreducible (factorization and an irreducibility
  test modulo 11), six real roots in rational intervals of width 1e-30, the generic sigma(k) for k >= 11 against direct
  values at k = 11..16, the nonvanishing arguments, sigma_inf; then floating values (about 85 s).
- tq5_bounds_radius.py / .out: certificate for Corollary T_5(b): all-k response lower bounds s_i (interval evaluation for
  k <= 10, positive-coefficient test in t = k-11 for k >= 11) and the box certificates G(z0, 2Y0) <= 2Y0 for the
  generating system of Section 12.5 Step 4 (radii 2^140 to 2^175, common 2^185; about 85 s).
- tq_cert.py Q / tq_cert_Q4.out: the certificate of tq5_cert.py for general Q (f_1 = sin + b sin 3 theta, k0 = 2Q+1).
  Irreducibility of P_2Q by factorization and, independently, by intersecting the factor-degree patterns modulo two good
  primes. Q = 4 gives Corollary T_4(a): P_8 irreducible, six real roots, generic sigma(k) for k >= 9 equal to the direct
  values at k = 9..14, sigma_inf (about 17 s).
- tq_bounds_radius.py Q / tq_bounds_radius_Q4.out, _Q5.out: the certificate of tq5_bounds_radius.py for general Q with
  automatic constants a_i = ceil(100(1+|b_i|))/100 and s_i the largest power of 2 below 0.9 times the floating minimum;
  reports the smallest passing z0 = 2^-q for each root and a common one. Q = 4 gives Corollary T_4(b) (radii 2^82 to
  2^98 times eps^2, common 2^104; about 15 s); Q = 5 reproduces Corollary T_5(b) with automatic constants.
- tq_minima.py Q k_1 .. k_m / tq_minima_Q5.out: exact minima of |sigma_k(b_i)| over all k >= 2 (Corollary T_5(c)):
  interval gaps for k < k0, and for k >= k0 a positive-coefficient test in t = k - k0 of
  eps_inf N(k0+t,b) - |sigma_(k_i)(b)| D(k0+t); then rational bounds s_i with three significant digits and the box
  certificates with these s_i (radii 2^127.5 to 2^165, common 2^172.5; about 45 s). Run as tq_minima.py 5 5 8 5 6 5 5.
- tq_sym3.py / tq_sym3_Q3.out: three-mode profile sin + b sin 3 theta + tau sin 5 theta at delta = 2/3 in Q(k)[b, tau]:
  O_6, sigma_inf(b, tau), generic-versus-direct checks at k = 10..14, sigma_2..9, the resultant Res_b(O_6, sigma_inf)
  (degree 18) and its real roots (Proposition T.9; about 18 s).
- tq3_disk_check.py / .out: independent check of Corollary T.10: Rouche circle ratios for the root branches b(tau),
  finite responses k = 2..9 and the all-k tail on the complex disks, and the Step 4 box at Q = 3, B = 6, kappa = 14
  (radii 2^63 and 2^57; about 15 s).
- tq_minima.py, k_i = 0 mode / tq_minima_Q4.out, tq_minima_Q6.out: k_i = 0 means that the infimum is |sigma_inf(b_i)|
  and is not attained; the target is then sigma_inf(b) D(k0+t), whose top t-coefficient must cancel identically, and all
  other coefficients must be strictly positive. Run as tq_minima.py 4 5 3 0 5 5 5 (Corollary T_4(c)) and
  tq_minima.py 6 6 5 6 0 0 6 (Corollary T_6(b)). In these two outputs the final "(A) PASS" sentence, written before the
  k_i = 0 mode was reworded, says that every minimum is attained; the per-root rows are correct: root 3 at Q = 4 and
  roots 4 and 5 at Q = 6 have unattained infima. The script now prints the exception.
- check_supersolutions.py / check_supersolutions_Q5.out: independent check of the explicit rational supersolutions of
  Corollary T_5(c): rebuilds Phi from Step 4 of Section 12.5, reads only (a, s, z0, Y, R) from the supplied JSON,
  re-derives the root intervals and checks 1+|b_i| <= a_i, s_i, Phi(z0,Y) < Y exactly and R^2 z0^5 > 1.
- tq_cert.py 6 / tq_cert_Q6.out: Corollary T_6(a) (delta = 1/3): P_12 irreducible (patterns [3,9] mod 13, [1,11]
  mod 19), six real roots, generic sigma(k) for k >= 13 (degree 197 in k) equal to the direct values at k = 13..18,
  sigma_inf, all sigma_k and sigma_inf nonzero at the roots (about 180 s).
- tq_symh.py Q h M [kmax]: tq_sym.py for every rational delta = 2h/Q (gcd(h,Q) = 1, 2h < Q; every rational delta in
  (0,1) has this form). For h >= 2 the resonances are n = kQ, k >= 1, with stream mode 2hk-2, and the obstruction is the
  density mode 2hk-3 (theory Section 12.6). Validated at h = 1: tq_symh.py 5 1 3 6 reproduces tq_Q5_M3.out line by line.
  tq_symh_Q9h2_M3.out is the partial output of a run stopped after O_9, its factorization and the real roots.
- tq_certh.py Q h / tq_certh_Q9h2.out: certificate of Corollary T_{9,2} (delta = 4/9): primitive P_9, irreducibility by
  modular patterns, five real roots; the generic two-mode sigma(k) for k >= k0 = ceil((4Q+2)/(2h)), its numerator
  reduced modulo the monic P_9 and the gcd in Q[k] of the remainder coefficients (no integer root >= k0; this test is
  an equivalence), the denominator, the comparison with direct values at k0..k0+5, sigma_inf and the finite k from 1
  to k0-1, each checked nonzero and not divisible by P_9.
- tq_radiush.py Q h k_1 .. k_m: tq_minima.py for h >= 2 (responses from k = 1, k0 = ceil((4Q+2)/(2h))), with the box test
  of the shifted system of Section 12.6 Step 4 (unknowns V_1..V_(Q-1), E, W; kappa = B(Q-2h)(3-2h/Q)/h); radius
  z0^(-Q/(2h)) times |eps|^(Q/(2h)). At h = 1 it uses the system of Section 12.5.
- tq_boxh.py Q h [B=bandwidth] a_1 s_1 ...: box certificates from given rational inputs (a_i >= ||f_1||_1,
  s_i <= inf_k |sigma_k|), the box part of tq_radiush.py; B defaults to 4. tq_boxh_Q9h2_ver150.out replays the two-mode
  4/9 boxes of Corollary T_{9,2}; tq_boxh_Q9h2_B20_ver158.out replays Corollary T_{9,2}.C (B = 20, a = 1139/1000,
  s = 2^-28: z0 = 2^-259 passes with ratio 0.82056, 2^-258 fails; radius 2^(2331/4) |eps|^(9/4)).
- cand_sigma.py Q h dps profile b0 kmax [klarge ...]: floating (mpmath) responses sigma_k at delta = 2h/Q for a general
  finite sine profile, from the Fourier form of the recurrence (independent of tq_symh.py). Validated by
  cand_sigma.py 9 2 30 two 0.0634 12 50 against tq_certh.py 9 2. cand_sigma_root3.out: Candidate 007 exact leading
  profile (B = 20) with the sin 3 coefficient at the third root of O_9: root, ||f_1||_1, sigma_1..60 and sigma_k at
  k = 100..5000 (about 200 s); used to cross-check Corollary T_{9,2}.C.
- tq_radiush.py k:KT syntax: KT is the start of the tail test for that root (default k0); the generic sigma(k) is cached
  in tq_sigma_Q<Q>h<h>.cache.json and reused on reruns (these cache files, 4.5 MB, are not published; the first rerun
  regenerates them).
- tq_radiush_Q9h2.out: tq_radiush.py 9 2 7 4 13:24 0 5 (about 31 min). Exact infima of |sigma_k| at the five two-mode
  roots at delta = 4/9 (unique minimizers k = 7, 4, 13, none, 5; tail test from k = 24 at the third root), certified s_i
  and boxes with coarse a_i. tq_boxh_Q9h2_exact.out: the boxes replayed with the tighter a_i of Corollary T_{9,2}(b) and
  these s_i (Corollary T_{9,2}(c)). cand_sigma.py 9 2 40 two 0.2698308394 24 gives the signs of sigma_1..24 at the third
  root (sign change between k = 12 and 13).
- tq_boxh_init.py Q h profile b0 s [kappa=old|star] [L=half|sharp] [eps=1e-40]: box certificates at h >= 2 with the
  actual initial norms d_j >= j||f_j||_1 (j <= Q) in place of the Catalan bounds, optionally with the reduced bilinear
  constant kappa_* = B(2-delta+max(delta,1-delta))(1-delta)(Q+1)/(delta Q) and the sharp Poisson constant
  L_Q = 3Q^2/(4(3Q-1)) (theory Section 12.6, Remark 4). The root of O_Q is enclosed by a sign change in interval
  arithmetic (mpmath iv, 90 digits, enclosure width 2 eps), f_1..f_Q are evaluated over the enclosure, d_j is the
  interval upper bound rounded up to 10 significant digits, and the box test 2 Y0 is exact rational arithmetic.
  profile: 'two' (B = 4) or a JSON file as in cand_sigma.py.
- run_boxh_init.sh / tq_boxh_init_Q9h2.out: the five two-mode roots at delta = 4/9 with the three refinement levels
  ((i) initial norms; (i)+(ii) kappa_*; (i)+(ii)+(iii) L_9 = 243/104), each with the proved lower bounds s of
  Corollary T_{9,2}(b) and the exact infima s' of Corollary T_{9,2}(c), and the Candidate 007 roots 2 and 3 (B = 20).
  About 2.5 s per two-mode run and 35 s per B = 20 run.
- candidate007_leading_exact.json: the exact leading density profile of Candidate 007 (frequencies 1..19, a_1 about
  18.5678), the input of cand_sigma.py and tq_boxh_init.py for Corollary T_{9,2}.C.
- cand_sigma_root2.out: cand_sigma.py 9 2 40 candidate007_leading_exact.json 0.0420056861532581 60 100 200 500 1000 2000,
  the floating cross-check of Corollary T_{9,2}.C(c) (second root of O_9 in the Candidate 007 family).
- tq_block.py: the resonance-block majorant at delta = 2h/Q, h >= 2, with M = 1 (theory Section 12.6, Remark 5(a)).
  Same root enclosure, initial norms d_j and constants as tq_boxh_init.py; then the 2Q-component block map in w = z^Q,
  Y = (V_1..V_(Q-1), E, X_1..X_Q). Before the box test the formal solution of the block system (3 coefficients per
  component, 6Q identities) is checked in exact arithmetic against the direct total-order scalar recursion with eta_n = 0
  off the multiples of Q, which does not use the residue projections; then the affine form at w = 0, strict lower
  triangularity of J, Y0 = (I-J)^(-1) c0, the box 2 Y0, the smallest passing w0 = 2^-q and the failure at 2^-(q-1).
  usage: tq_block.py Q h profile b0 s [kappa=old|star] [L=half|sharp] [eps=1e-40] [kchk=3]
- run_block.sh / tq_block_Q9h2.out: the five two-mode roots at delta = 4/9, each with the bounds s of Corollary
  T_{9,2}(b) and the exact infima of (c), and the Candidate 007 roots 2, 3, 4 (B = 20), all with kappa_* and L_9.
  Results q = 156/152, 152/146, 167/161, 156/151, 171/147 and 194, 200, 198. About 15-18 s per two-mode run, 50 s per
  B = 20 run.
- tq_block_cand1.out: tq_block.py 9 2 candidate007_leading_exact.json -0.152635000561798 1/16384 kappa=star L=sharp
  (Corollary T_{9,2}.C(e), first root): q = 197, normalized radius 2^(197/4).
- cand_sigma_root1.out: cand_sigma.py 9 2 40 candidate007_leading_exact.json -0.152635000561798 60 100 200 500 1000 2000,
  the floating cross-check of Corollary T_{9,2}.C(e).
- tq_prefix_block.py: the resonance-block majorant of Remark 5(a) for general M (prefix N = MQ), h >= 2. The root of O_Q
  is enclosed by an interval sign change; the uniquely tuned prefix f_1..f_N is computed over that enclosure in interval
  arithmetic (Fourier form): at n = kQ the obstruction mode 2hk-3 is checked to contain 0 and set to 0, and H_n is the
  interval -R0/(R1-R0) from two provisional continuations to n+Q (H_n = 0, 1), with R1-R0 excluding 0. Then
  d_j >= j||f_j||_1, e_a >= aQ|H_aQ| (rounded up), kappa_N, L_Q, the 2Q-component block map checked against the direct
  total-order scalar recursion (2 coefficients per component), affine form and strict triangularity at w = 0, and two
  box families (2 Y0, and an adaptive box from a floating iteration, verified exactly).
  usage: tq_prefix_block.py Q h profile b0 s M [L=sharp|half] [eps=1e-40] [kchk=2]
- run_prefix_block.sh / tq_prefix_block_Q9h2.out: the five two-mode roots at delta = 4/9 with the exact infima s and
  M = 4 (N = 36). Checks: M = 1 at the fourth root gives q = 151 (as tq_block.py); M = 2 gives q = 123 (2 Y0) and 122
  (adaptive). M = 4 at roots 1..4: q = 130/129, 126/125, 130/129, 122/121 (2 Y0 / adaptive), the exponents of the
  independent certificate. Root 5 at 90 digits stops at n = 27 (response interval contains 0): rerun at 200 digits by
  run_prefix_block_root5.sh -> tq_prefix_block_root5.out (M = 2, 4; option dps=200 eps=1e-150).
- run_prefix_block_cand.sh / tq_prefix_block_cand.out: Candidate-shaped roots 1..4 (B = 20) with M = 3 (N = 27).

- tail_moment_check.py: exact rational check of the moment identity used in the explicit remainder bounds (theory Section
  12.6, Remark 6): sum_{k>=K} (m+Qk)^(d-1) t^k = (m + Q t d/dt)^(d-1) [t^K/(1-t)] for d = 1..4 and the d = 0 bound,
  against 400-term partial sums (270 cases; prints "bad 0").

- hh_tune_mod.py: hh_tune.py carried out in a prime field F_p (every divisor checked to be a unit mod p, so every residue
  is the reduction of the exact rational; a nonzero residue proves the exact value nonzero). Usage: hh_tune_mod.py Q h
  profile kmax p. hh_tune_mod_Q9h2_sin15_p1.out (p = 2^61 - 1) and _p2.out (p = 4611686018427387847): sin(15 theta) at
  delta = 4/9, residues of R_1..R_4, sigma_1..sigma_4, H_9, H_18, H_27 (sigma_1..sigma_3 and R_4 nonzero, sigma_4 = 0
  mod p; 36 to 40 s each). The exact polar run hh_tune.py 9 2 15 4 was stopped during k = 3 (k = 2 took 473 s).

Periods seven to ten (Corollaries T_7 to T_10, delta = 2/7, 1/4, 2/9, 1/5):
- tq_cert.py Q / tq_cert_Q7.log, _Q8.log, _Q9.log (and .out): the exact certificates of Corollaries T_7(a), T_8(a), T_9(a)
  and the exact response certificate in their proofs (primitive P_2Q, factor_list, modular factor-degree patterns, Sturm
  root isolation to width 1e-30, the generic response N(k,b)/D(k) for k >= 2Q+1 with its factor structure, sigma_2..sigma_2Q).
  tq_cert_Q10.log: the same at Q = 10 through the irreducibility of P_20 (patterns [3,17] mod 31, [2,2,3,13] mod 41,
  [1,1,3,7,8] mod 59, [1,8,11] mod 61) and the fourteen isolated real roots; the run was stopped after that step and
  replaced by tq_bounds_radius_v2.py 10.
- tq_bounds_radius.py Q / tq_bounds_radius_Q7.out, _Q8.out: all-k response lower bounds and the explicit (crude) Section
  12.5 Step 4 radii. tq_bounds_radius_v2.py: the same, plus per-root floating information (b, sigma_inf, the sampled
  minimum over 2 <= k <= 3000 and the limit) and the exact generic response written to tq_generic_sigma_Q<Q>.txt.
  Tested at Q = 5 (same output as tq_bounds_radius_Q5.out, 50 s). tq_bounds_radius_Q10.out: the run at Q = 10.
- rh_top_Q78.py, rh_top_Q9.py, rh_top_Q10.py (and .out): the necessary radii (|b_i|/R_H)^(1/delta) of part (d) of
  Corollaries T_7 to T_10 (theory Section 12.6, Remark 3), with R_H checked against the scalar top recursion to order 1500.
- aQ_poly.py Q / aQ_poly_Q4..Q8.log, aQ_Q9.out, aQ_Q10.out: the order-Q potential-logarithm coefficient a_Q(b) = [sin theta] f_Q
  (exact; degree Q in b for 3 <= Q <= 10, so it cannot vanish at a root of the irreducible degree-2Q polynomial P_2Q).
- hh_float.py / hhf_Q<Q>h1_root<i>_N<N>_f64.out: double-precision tuned runs at the roots (NUMERICAL EVIDENCE);
  fit_hhf.py: block-maximum line fits (fit_hhf_Q7Q8.txt, fit_hhf_Q9_N306.out). Orders 301, 304, 306 at Q = 7, 8, 9;
  order 602 at Q = 7 (all ten roots; fit_hhf_Q7_N602_r6to10.out for roots 6..10) and 600 at Q = 8 (fit_hhf_Q8_N600.out with
  --lo=100,200,300,400; fit_hhf_Q8_N600_cmp.out compares the windows 100,150,200 at orders 600 and 304, root 1 against the
  amplitude-1/16 run N304_f64e16); order 300 at Q = 10 (fit_hhf_Q10_N300.out) and 600 (fit_hhf_Q10_N600.out with
  --lo=100,200,300,400; fit_hhf_Q10_N600_cmp.out compares with order 300); order 612 at Q = 9 (fit_hhf_Q9_N612.out,
  fit_hhf_Q9_N612_cmp.out compares with order 306). fit_cmp.sh Q NEW OLD roots... writes these
  comparison lines (OLDFILE_<root>=name overrides a baseline file). fit_ranges.py prints the same density fits at full precision with
  ranges rounded outward (fit_ranges_Q10_N600.out, fit_ranges_Q9_N612.out); the report quotes these ranges. The amplitude (last argument of hh_float.py)
  is a power of two chosen so that A*eps is near 1; the printed norms are rescaled to unit amplitude exactly.
- run_after_queue12.sh .. run_after_queue15.sh: the detached job queues (their operational .log files are not published). Queue 15 (started
  2026-10-31T20:35:08Z) runs tq_bounds_radius_v2.py 10, then hh_float.py at the fourteen Q = 10 roots to order 300,
  then Q = 7 roots 6..10 to order 602 and Q = 8 roots 1..10 to order 600.
  It ended at 22:28:35Z (the Q = 10 radius step was stopped by hand at 21:34:53Z, superseded by the independent certified
  prefixes). Queue 16 (started 22:28:35Z, ended 23:49:58Z) ran Q = 10 roots 1..14 to order 600 and Q = 9 roots 1..10 to
  order 612.
