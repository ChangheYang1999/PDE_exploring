# S2_NUMERICAL_CERTIFICATES.md: numerical inequalities and their status (theory author's document)

Final version at the end of the run (2026-10-28, 18:20 UTC), published with the S2 theory report; the dated list that
follows records its revision history. Labels and verification record numbers (V001, ...) are as in the report.

First version 2026-10-28T03:03Z (theory author), updated 03:13Z (V037, V039), 03:25Z (V041, V042, Theorem C') 03:34Z (V043 to V046) 04:11Z (V047 to V054), 04:47Z (V055 to V061) 04:59Z (S0 certified by the numerics team; V064) 05:15Z (V066 to V068; Lemma Z) 05:26Z (box certificates of the margins, of (A), (CB) and kappa_*, and the (Z) data, by the numerics team) and 05:34Z (V069 to V072; every short decimal rounded outward from the stored endpoints) and 05:47Z (V073 to V076) and 05:57Z (V077 to V080: independent original-data certificates of (A), (H_m), (H_m') and (Z)) and 06:00Z (V081: C6 reproduced; refined single-team margins) and 06:16Z (V086: both margins at least 5/2, VERIFIED) and 06:39Z (V088, V090, V093, V095; second single-team margin refinement; second-moment grid values) 06:45Z (V099, V100) and 07:04Z (V102, V105: the INJ-Q input list and the lift constant). Every entry gives the quantity, the background, the method and the status. Updated 08:06Z (V107, V110, V111: the strong residual; NUMERICAL value and weight family) and 08:14Z (V120 to V122) and 08:31Z (V123 to V125) and 10:00Z (floating core section of S_1) and 11:50Z (V164 residual enclosure; V171, V172, V174 decoupled weight family) and 11:59Z (the S_1 section values corrected for a checkpoint double count) and 12:03Z (V179, V180) and 12:18Z (V181, V182) and 12:46Z (V183 high-norm lower bound) and 13:09Z (V185 to V194; the S_1 error-model caveats) and 13:18Z (V197: the margin 2.9270 VERIFIED) and 13:27Z (V199: the relative threshold 0.0507) and 13:52Z (V200: the no-TAU S0 value; V202: the exact pure-spline input Gram), and 14:12Z (V210: high conformity of the pure section), and 15:54Z (review corrections V250; V252 integrated: the completed three-mode pure section, section 5), and 15:59Z (the global m_a refinement: V197 and the finer outer cover of the numerics team) and 16:14Z (V259: m_a >= 3 VERIFIED) and 16:28Z (V260, V263: the shifted outer input Gram) and 16:36Z (V267: the complete S1J1 input Gram) and 16:48Z (V269: the high intersections of S1J1) and 16:52Z (V275: V269 is a THEOREM) and 16:56Z (V274: the decoupled family digits) and 16:58Z (V277: S1J1 output, floating) and 17:04Z (V279, V280: S1J1 row; table row repaired; the Gaussian test direction) and 17:10Z (V283: the Gaussian direction is a THEOREM) and 17:22Z (V282, V291: exact strain-zero subspaces of S1J1, input only) and 17:43Z (V300: the strict input-form bounds are stated for nonzero vectors) and 17:53Z (V304: c[d] != 0 in the strict residual-subtracted tests).
Status words:
- VERIFIED: an enclosure computed in exact or ball arithmetic and confirmed by the independent verifier (verdict given).
- CERTIFIED (one team): an outward ball-arithmetic enclosure by one team, not yet reproduced independently.
- PENDING: the certificate is being computed.
- NUMERICAL: floating-point grid evidence. It is not a bound.
The background is the exactly joined, exactly normalized modal trial rho~ (exact export with SHA-256
57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6, plus the scalar repair z), unless X3 is named.
Held constants: k = 1615536043799051/2^53, c_l = 1/k, A = 2 c_l - 1, D = 4 c_l - 1.

## 1. Normalization and the background

| Quantity | Enclosure | Method | Status |
|---|---|---|---|
| c0 = c[trial] before repair | [15.7260878319246786225638146971829, 15.7260878319246786225638146971831] | exact rational splines, exact Green moments | VERIFIED (V005) |
| normalization correction z | [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20] | exact real solve; spline Taylor remainder < 7.82e-183 | VERIFIED (V005) |
| normalization slope | [3386927.83874448932844599542335954, 3386927.83874448932844599542335956] | same | VERIFIED (V005) |
| c[rho~] - (3/k - 1) | [-1.62e-43, 1.62e-43] | independent code, 320-bit balls, three formulas (Green sum, B_1 route, cosine-mode identity), uniform over the z ball | CERTIFIED (numerics team, certificate C1); agrees with V005 |
| raw X3: c[X3] | (15.726087821623500282, 15.726087821623500289) | exact interval evaluation of the stored state | VERIFIED (V018) |
| raw X3: 3/k - 1 - c[X3] | (1.0301137738456e-8, 1.0301137743913e-8) | same | VERIFIED (V018) |
| origin regularity of rho~ | C^{4,1}, not C^5 (nonzero sin(521 theta) term at degree 5) | exact extraction of the degree-5 inner term | VERIFIED (V036) |

The X3 defect is the reason X3 cannot serve as the rigorous background: with the normalized exponent, F(X3) contains a
term that grows like r^k.

## 2. Source point

| Quantity | Enclosure | Status |
|---|---|---|
| source x_P (unique zero) | (4841405518533377, 4841405518533711)/2^49 | VERIFIED (V017) |
| rate mu at the source | (0.99999997745, 0.99999997750); so mu != 1 | VERIFIED (V017) |
| g at the source | (29, 30) | VERIFIED (V017) |
| eps_y = (mu - 1) g | (-6.8e-7, -6.6e-7): the trial is not stationary at P | VERIFIED (V017) |
| frozen source inverse on H^s | inverse norm at most 1/delta_s; 500/1687 at s = 31/10; admissible for s < 2373/680 uniformly on the coefficient box | VERIFIED (V011) |
| sharp frozen source threshold s_fast = (b_0 + g)/A_P (Riesz coupling retained) and the singular degree q = (1 + g)/A_P | 3.57854758171660 < s_fast < 3.57854758172942; 3.02929001866399 < q < 3.02929001867499; a fixed smooth forcing has no H^s solution for s >= s_fast | VERIFIED (V064; exact rational arithmetic from the V017 enclosure) |
| source neighbourhood perturbation | E <= 2536479/14000000; kappa - E >= 44699521/14000000 | VERIFIED (V024; 14672 polynomial values, 14616 Green derivative values, 1566 boundary checks, 448 cells) |
| source rectangle Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2] (p_-, p_+ the bracket of x_P) | ||D^2 V||_F < 1.159484 on Q (6048 covering polar cells, 512-bit Green data, 640-bit audit with 132048 polynomial, 131544 Green-derivative and 16182 boundary checks); S(DV) > 0.1801 I on Q; hence abs(V(X)) >= 0.1801 abs(X - P) on Q and P is the only zero in Q | VERIFIED (V070) |
| auxiliary source strain norm | 1/[8 sqrt(pi (s-1)(s-2))] = 0.0464011865967... at s = 3.1 | VERIFIED (V021) |

## 3. Origin, axis and normalization constants

| Quantity | Value | Status |
|---|---|---|
| kappa_0 of Theorem O (a = 7/2, b = 6/5, sigma = 7/10) | 16.54116035405294722844... | VERIFIED (V022) |
| frozen local strain adjoint K_A | K_A < 0.032162163072022018 | VERIFIED (V016) |
| strip coupling constant C_a (a = 7/2) | 1759/6 | VERIFIED (V026) |
| universal constants of the explicit axis-strip bound A_ax = sqrt(W_max)[C_a M_20 + (C_a s_0/2) M_21 + (D_a s_0^2/6) M_40 + (D_a s_0^3/24) M_41] | C_a = 593, D_a = 612 admissible (V095); sharpened at a = 17/4 to C_A < 38.436, C_B < 24.534, D_A < 38.762, D_B < 24.724, so A_ax = sqrt(W_max)[39 M_20 + (25 s_0/2) M_21 + (39 s_0^2/6) M_40 + (25 s_0^3/24) M_41]; trace constants B_0 < 0.134331, B_1 < 0.230829, B_2 < 0.718533 | VERIFIED (V095, V099; 256/384 bits); the four background suprema M_20, M_21 (axis rho_xx, rho_xxy) and M_40, M_41 (rho_xxxx, rho_xxxxy on the Taylor rectangle) are not enclosed |
| principal high-energy symbol at delta = 9/5 (Theorem H) | y-axis (factored) threshold 1.719076581741518, margin 142.5073992705142 at order 25/4; x-axis cylinder threshold 2.080923418258482, margin 0.9726087831924638 at order 41/20; margin at infinity 3.787681305320773 at gamma = -1/2 | VERIFIED (V088), with the metric caveat of the record; the earlier table value 2.0807 is corrected to 2.08092 |
| velocity radius of the geometric clause | for parity-preserving C^1 W with sup abs(DW) <= 1e-5: the three zeros persist, speed/r >= 0.00023 outside the source rectangles, symmetric derivative >= 0.18009 on Q, source shift <= 1/1801 | VERIFIED (V090; uses only the V070 and V080 constants) |
| diagnostic strain bound of V004 at the exact k, L | [0.00362844569114920751639699158385338, 0.00362844569114920751639699158385339] | VERIFIED (V005) |
| Corollary C1: C_c0 | < 0.013958 (a = 7/2, b = 6/5); < 0.017231 (a = 17/4, b = 0) | VERIFIED (V034) |
| far strain constant C_> | < 0.273629 | VERIFIED (V034) |
| Prop C2: C_cap | < 0.312093 (a = 7/2, b = 6/5); < 0.359253 (a = 17/4, b = 0) | VERIFIED (V034) |
| far angular moment s_3/pi | (37.63077494715565, 37.63077494715567) | VERIFIED (V034) |
| bordering denominator d = 3 c_l + k c[KP] | d >= 3 c_l > 0 for every smooth cutoff 0 <= chi_inf <= 1 supported in r >= 1 | VERIFIED (V034) |
| c on L^2(w_a), a = 17/4: c_R in Lemma C'4 of S2_L2_THEORY.md 5.2 | c_R = (1/pi)(int abs(cos)^{17/2} sin^2(3 theta))^{1/2} (2/9 + 4/11)^{1/2} = 0.2075698661066814348070539594304323... < 0.207570 | VERIFIED (V047; Arb at 384 and 768 bits). It is the exact norm of the strain functional on R, equal to ((58/99)(6618/725) B(3/2, 19/4)/pi^2)^{1/2} < 0.20757, and the same bound holds on D_R with the graph norm (VERIFIED, V093; directed 256- and 384-bit check) |
| angular constant I_a of Lemma C'1 | 2 Gamma(1/4) Gamma(3/2)/Gamma(7/4) = 6.992153... | exact formula |
| exact anisotropic energy limit at 0 for w_a: kappa_0 = (19/2) c_l - 13/4 | 49.71594480109468708445... | VERIFIED (V055; independent enclosure from the held k) |
| exact energy limit at infinity for w_a: kappa_inf = 1 + 3 c_l/8 | 3.09076097899057975333... | VERIFIED (V055); b_+ tends to 0 at both ends, so the margin is eventually positive at 0 and at infinity; in the V055 argument itself the cutoff radii and the annulus bound are not certified. Whole-plane certificates of the margin are given from V077 on (V077, V086, V197; section 4) |
| c[KP_shifted] for the numerics team's S0 column (log r - t_+ in the column) | [0.07037233698866423364632510451051059, 0.07037233698866423364632510451051061] | VERIFIED (V043; 512-bit, own de Boor recurrence, analytic remainder) |
| c[TAU] for the S0 column | [0.06854755426283814823722790430809866, 0.06854755426283814823722790430809868] | VERIFIED (V043) |
| denominator 3/k + k c[KP_shifted] | [16.73870985167530795255805332462072, 16.73870985167530795255805332462074] | VERIFIED (V043) |
| c of the unshifted log r column (theory convention) | 0.561035031494029527433908883862569 | reported by the verifier (V043 note); the two conventions differ by t_+ times the amplitude column |

## 4. Margins (the hypotheses (H_m) and (H_m'))

| Quantity | Value | Status |
|---|---|---|
| m_* = inf (b_0 + mu~' q/2 - b_+) for the piecewise affine mu~ | m_* >= 1.029821 (weakest box at t = 2.145, theta about 45.7 degrees); inner half-line >= 5.3065, outer half-line >= 3.0888; grid minimum 2.590 | CERTIFIED (one team, 05:10Z): all 1569 radial cells (spline cells, inner and outer sub-cells and both half-lines) times 64 angular boxes of width pi/128, every cell computed, 0 negative boxes, adaptive refinement available and not needed; repaired range method (V061, V068). Coverage, retention of the refined arrays and the directed aggregation VERIFIED (V072: all 100416 boxes, every applicable entry finite, exact dyadic minimum 1.0298211720474706 reproduced), conditional on the exported cell enclosures; the verifier's own original-data computation gives the larger VERIFIED bound m_R >= 1.78605 (row of the independent certificates below, V077). Refinement (one team, 05:58Z): the 855 cells with a bound below 2.5 recomputed with adaptive angular bisection to depth 5 (17242 boxes into 133255 leaves, 0 negative, all finite) give m_* >= 2.471224 (argmin r = 4.46, theta about 51 degrees, at the bisection depth floor). The VERIFIED bound is now m_R >= 5/2 (V086, row of the independent refinement below). Second single-team round (06:16Z; depth 6 on the 1027 cells below the targets 2.55 and 3.0; 31127 boxes into 263417 leaves, 0 negative, full coverage): m_* >= 2.482724 at r = 4.46, theta about 51 degrees, at the depth floor (CERTIFIED, one team) |
| m_a = inf (kappa_{w_a} - b_+) for w_a, a = 17/4, one knot at r = 1 (hypothesis (M) of Theorem C') | m_a >= 0.965918 (weakest box near the x-axis at r about 52); 0 negative and 0 nonfinite boxes; grid minimum 3.0908 | CERTIFIED (one team, 05:10Z; same run and cover). The first box run (04:00Z) had returned lower bounds near -4e77 (interval blow-up on inner cells); V068 had REFUTED the archived merge, which the numerics team repaired before the production merge; coverage and directed aggregation VERIFIED (V072; exact minimum 0.9659182260060386), conditional on the exported cell enclosures. Refinement (one team, 05:58Z; same run as for m_*, with the sharper anisotropic tail bound abs(sin(2n theta)/cos theta) <= min(2n, 1/min cos theta) for n > 8): m_a >= 2.500023, every refined box reaching the target 2.5. The verifier's own targeted refinement gives the VERIFIED bound m_a >= 5/2 (V086, row below). Second single-team round (06:16Z): m_a >= 2.871539, limited by the radial width of the first outer sub-cell next to the x-axis (CERTIFIED, one team); third round (12:44Z, eight cells of width 1/16 on that sub-cell): m_a >= 2.9270, now attained at the cell [t_+ + 1, t_+ + 2]; VERIFIED (V197) by an independent whole-plane refinement from the original data (1352 retained radial roots, 65947 parents replaced by 82041 leaves, exact cover audit, 34 replays at 640 bits, both analytic ends) |
| axis rate d = V_2(0, y)/y, hypothesis (A) of Theorem C' and of V041 | d in [5.575203, 21.301451] on the whole axis; sup abs(d') <= 5.6012; sup_{t<=0} abs(d - D) e^{-2t} <= 0.100883, sup_{t<=0} abs(d') e^{-2t} <= 0.202073; sup_{t>=0} abs(d - c_l) e^{(1-k)t} <= 89.3342, sup_{t>=0} abs(d') e^{(1-k)t} <= 73.3113 | CERTIFIED (one team, 05:10Z), conditional on the exact normalization (V005) for one dropped constant of d - D at the origin (a ball -4.3e-37 +/- 2.0e-35 that equals c[rho~] - (3 c_l - 1) and is exactly 0 for the repaired trial). History: the first script hypA.py was audited (V054; coverage and float-radius conversion REFUTED; near-resonant inner Green correction of mode 27 with exponent 75/2^46); the range code was rewritten, its first union REFUTED (V058) and the repaired exact-dyadic union with resonance merging CONFIRMED (V061, V068); coverage and directed aggregation of the run VERIFIED (V072; exact minimum 5.575203976688894), conditional on the exported cell enclosures |
| lift constants of Lemma C'1 (M_Q = sup abs(a_1), M_P = sup max(e^{-2t}, 1) abs(a_0); hypothesis (CB) of V046, (L) of V047) | M_Q <= 337.66, M_P <= 1075.52 (the e^{-2t}-weighted part on t <= 0 is 1.09); the sizes come from the slow decay in n of the far angular modes near the y-axis | CERTIFIED (one team, 05:10Z); not needed for the Fredholm statement |
| transport margin kappa_* = ess inf kappa_{w_a} (Lemma C'2, V046 (2)) | kappa_* >= 3.037693 (far limit 3.0908, V055); sup kappa_w <= 125.4206 | CERTIFIED (one team, 05:10Z) |
| other box bounds | sup b_+ <= 11.2281; sup abs(grad rho~) <= 30.4196 (finite cells); sup du <= 125.7436, where du = abs(psi_rr) + 2 abs(psi_rtheta)/r + abs(psi_thetatheta)/r^2 + abs(psi_r)/r + abs(psi_theta)/r^2 is a component-sum bound of the Euclidean operator norm of DU[rho~] (V068), so c_l + sup du is a global Lipschitz constant of V; sup kappa_w <= 125.4206; q in [-10.150726, 21.301451] | CERTIFIED (one team, 05:10Z) |
| independent original-data certificates (the verifier's own code: all 1558 spline spans and 261 stream modes rebuilt from the original data, 512-bit Green moments, 3276 radial cells (two per span plus 160 for the exact outer continuation) times 128 angular cells, both infinite ends bounded analytically; separate 640-bit audit of 3276 cells, adjacency, aggregation, endpoint formulas, 32886 source-boundary overlaps and 432 moment identities) | d >= 5.5752 on the whole axis; m_a >= 0.53072 for w_a; m_R >= 1.78605 for mu~; kappa >= 1.6377 on the finite cells with positive analytic ends | VERIFIED (V077). This closes (A) (with the qualitative endpoint estimates of V055), (H_m') and (H_m); Theorems R and C' hold for the actual background. The sharper single-team values above keep the status CERTIFIED (one team) |
| independent refinement of both margins (the verifier's code: 1754 certified radial cells retained, the other 1522 recomputed from the original profile coefficients and the audited Green cache, exact finite angular recurrence for every quotient mode, a sharper equivalent positive-rho_y formula for b_+; 512-bit refinement with 194816 roots and 213985 accepted terminal leaves, maximum depth 5; separate audit of every partition, every saved directed lower bound, both infinite ends and all hashes, with a 640-bit replay of 136 boxes) | m_a >= 5/2 for w_a and m_R >= 5/2 for mu~ (unrounded saved lower endpoints about 2.5001654 and 2.5000140); d >= 5.5752 stays that of V077 | VERIFIED (V086; full result SHA-256 8b08b110e1dcf307482bee1bfda59751d73978c1207ba8543475ff3d5cbd3581) |
| margin of the decoupled weight family (inner radial weight unchanged, far weight r^(-37/20), i.e. Delta = 0.3, angular exponent a in [18/5, 4]) | >= 1.13 at a = 4 (raised to >= 1.2501 by an independent refinement of the first outer sub-cell, V191) and >= 1.10534 at a = 18/5, hence >= 1.10534 on the whole interval by affine interpolation (512-bit Arb from the original data on 3276 roots and 423719 leaves, no failed cell, end bounds > 1.41; independent cover check and 38 selected 640-bit replays) | VERIFIED (V171); the low mapping and Fredholm theory of that family, with remainder strain norms < 0.239392 (a = 18/5) and < 0.230190 (a = 4), is a THEOREM (V172) |
| global refinement of m_a for w_a (a = 17/4) | m_a >= 2.9270 over the whole plane (independent certificate from the original data: 1352 radial roots kept with 199494 leaves, 65947 parents replaced by 82041 leaves, exact cover audit, 34 640-bit replays, both analytic tails). A later finer cover of the outer region by the numerics team (16 outer cells refined to angular depth 6, merged with the production arrays) gives m_a >= 3.000000, then attained in the bulk at r about 176; inf m >= 2.482724 and the decoupled family value at a = 4 are unchanged (directed six-decimal lower value 1.250190 of the numerics team, floating 1.2501909638..., single-team; the independently verified bound remains 1.2501, V191, and V259 does not verify the sharper digits) | 2.9270: VERIFIED (V197). m_a >= 3: VERIFIED (V259; independent original-data refinement of the V197 cover, 512-bit production, complete cover audit and 640-bit replay, 1335 radial roots and 264525 angular rectangles kept, 19186 parents replaced by 36196 rectangles, both analytic half-lines; no array of the numerics team is an input). The 3.000000 of the numerics team is consistent with it. These are coefficient bounds of the margin only |
| best margin with a free radial mu' | 2.977 | NUMERICAL |

A sampled positive margin does not discharge the global hypothesis (V023). The box certificate encloses q, b_+ and
|grad rho~| on a cover of the quadrant by the trial's radial cells times angular boxes. A box that touches a knot
carries both slopes. For the anisotropic weight, the angular term is enclosed mode by mode with
sin(2n theta)/cos(theta) = 2 sum_{j=1}^{n} (-1)^{n-j} sin((2j-1) theta).

## 5. Finite sections (Avenue IV)

| Quantity | Status |
|---|---|
| identity test of the exact operator machinery (fixture trial, 42 modes) | PASSED to 1.7e-46; a consistency check, not a bound |
| verified lower bound of sigma_min(Q_M L P_N), section S0 (169 conforming columns plus TAU, 12 output modes, 69 test splines per mode, 256 bits) | sigma_min >= 4.3337e-07 with the TAU column (float value 4.4222e-07; the weakest direction is TAU, whose compensated image lies mostly beyond the last test knot t = 16.14); sigma_min >= 2.0685e-02 without TAU (float 2.1107e-02; weakest: the far power columns of modes m = 0, 1). Method: K - s^2 G_X positive semidefinite in ball arithmetic after the whitening T = L^{-T} from an exact-midpoint Cholesky (||T^T G_X T - I||_inf = 1.753e-27, the value found independently in V056). The 03:59Z failure was the binary64 rounding of the Gram midpoints (V054, V056) | with TAU: VERIFIED as a conditional matrix certificate (V066: independent decoding of the exported intervals, own whitening and Arb inversion, positivity residual < 4.351e-12 at the exact dyadic s = 4093149700530291/2^73 = 4.33379e-07; conditional on the exported entries enclosing the exact pairings). Without TAU: VERIFIED as a conditional matrix certificate with the same input condition (V200: independent 384-bit direct test-Gram inversion, positivity error < 4.036e-11, domain and test Gram errors < 1.754e-27 and 6.449e-62; the stored value 0.020684559 rounds up to 0.020685, and the direct check establishes the printed value without that rounding). A finite statement only (Prop IV.O) |
| off-basis bound for (I - Q_M) L P_N, section S0 | PENDING; code defects V027 and V033 repaired, repairs CONFIRMED in V037; the two remaining V037 obligations (a positive-subnormal discard, the float inflation of the tail bound) reported fixed at 03:00Z, re-audit pending |
| L_fix section in L^2(e^{mu~}) (realization of Theorem R; 169 conforming columns, modes m = 0 to 3, 69 test splines times 12 output modes, 256 bits) | sigma_min(Q_M L_fix P_N) >= 0.510914 (float 0.52134); both Grams (spanning 68 orders of magnitude) whitened exactly from exact midpoints, whitened Grams positive definite with residuals 1e-38 and 9e-45, positivity check of K - s^2 G with residual 4.4e-12; weakest direction: inner power columns of modes 0 and 1 (r < 0.0077) | VERIFIED as a conditional matrix certificate (V081: independent decoding of all entries, own exact-midpoint whitening at 384 bits, test Gram inverted in ball arithmetic, positivity of the image Gram minus s^2 times the domain Gram at the exact s = 255457/500000 with residual < 4.532e-12; conditional on the exported balls enclosing the exact pairings; matrix export SHA-256 277e6af0...44da). A finite statement: Lemma IV.1 applies in this realization, but the split (S) and the adjoint certificates are missing |
| floating core section of S_1 = T_R + C_R on R = L^2(w_a), R norm both sides, 42 columns x^2 y b_i(t)(cos 2 theta + 1) (first angular remainder mode only), all 531 output sine modes, exact jet split and cos^4 quotient | smallest generalized singular values 4.155 (resolved to about 1 percent; outer power columns beyond r about 3400), 6.08, 23.3 (not resolved; Gram condition number 1.5e13), 51.6, ...; 10.1, 13.6, 51.0 without the seven nearly dependent directions; 50.3 on the 33 pure spline columns (each cell counted once; cell coverage of this parts-only assembly CONFIRMED, V180); the value 4.44 on c[h] = 0 came from an assembly that counted checkpointed cells twice (default assembler REFUTED as a once-per-cell sum, V180) and is withdrawn pending recomputation | NUMERICAL (computed 10:00Z from the numerics team's run of 09:46Z; recomputed values on c[h] = 0 from the once-per-cell sum: 4.456, 6.084, 23.31, 51.70). The input quotients by cos^4 used a padded pseudoinverse instead of the exact templates Q_j = 2 (-1)^(m-1-j) (2m - 2j - 1) (V189), which changes the domain Gram by about 1e-7 relative (V187); the image division error is not covered by any error model, so "resolved" means with respect to accumulation rounding only (V187: REFUTED as a total error bound). The exact image bandwidth is 264 to 266 raw odd sine slots (V193). Two angular modes (84 columns): 2.344, 2.921, 3.501, 3.829, ...; the 52 pure spline columns give 3.456, 4.248, 5.460, 6.942 against 50.3 and 25.5 for the single modes (three modes: V252 row below). These floating values approximate upper bounds of the infimum over the subspace only within the accumulation-only rounding model (image division and quadrature errors uncertified, V187); they are not rigorous upper bounds, and an exact complete-image Rayleigh quotient would be needed for one (a projected-output singular value would not give it); certification estimated at about 18 h on four cores, not feasible in this run |
| exact input Gram and strain of the pure-spline S_1 columns (coarse degree-7 B-splines at stride 60 of the original knots, sp4 to sp29, angular modes m = 1, 2, 3; 78 columns) | exact rational spline polynomials checked against an independent de Boor recursion and all interior C6 joins; 512-bit exponential Taylor moments with a 640-bit antiderivative replay; exact Beta-function angular factors. For the stored 52-column two-mode section: abs(v^T (G_float - G_exact) v) < 2.37e-6 v^T G_exact v for all nonzero v; every stored pure-column strain coefficient (both three-mode and two-mode runs) has relative error below 2.71e-16 | VERIFIED (V202). Input side only: output pairings, image-side division errors and any singular value of the actual operator remain uncertified. All 78 columns are low-conforming; only i = 7..26 (60 columns) lie in the maximal high graph domain, and i = 6..27 (66 columns) in the high input space (THEOREM, V210) |
| completed floating three-mode pure-spline section of S_1 on R = L^2(w_a), R norm both sides (sp4 to sp29, angular modes m = 1, 2, 3, 78 columns, complete images with all output modes) | smallest floating generalized singular values 2.7655, 3.2685, 4.3913 (independent assembly by the verifier: 2.765547309, 3.268491498, 4.391313969); 2.7662 on the floating strain-zero hyperplane c[h] = 0 (stored binary strain row); sub-block m <= 2: 3.4557, 4.2477, 5.4604 (reproduces the two-mode value 3.456 above); single modes alone: 50.32 (m = 1), 25.47 (m = 2), 12.11 (m = 3). Section value against the angular cutoff: 50.32 (m <= 1), 3.456 (m <= 2), 2.766 (m <= 3), decreasing with the cutoff and not converged in m. The 60 high-graph-conforming columns sp7 to sp26 (V210) give 2.8648 in the LOW norms of this computation (not a high-norm value). Normalized input Gram condition number about 6.4e5 | NUMERICAL (V252). Accounting CONFIRMED (V252): all 1569 cells exactly once, the 1531 retained checkpoint cells excluded as duplicate prefixes. Input side CONFIRMED (V252): abs(v^T (G_float - G_exact) v) < 2.688e-6 v^T G_exact v for every nonzero v, against the exact V202 input Gram (directed 640-bit interval comparison); rigorous on the input side only. Output division and quadrature uncertified (accumulation-only rounding model, V187), so the values are floating observations: not a lower bound, not an exact operator bound, not a certificate |
| exact input Gram of the five shifted outer columns of a far-junction section of S_1 (h_q = r^3 p(theta)(cos 2 theta + 1) b_q(log r), q = 5..9, b_q = an outer exponential minus its Lagrange interpolant on the four leading outer exponents, zero before t_+ + 1) | closed form G_qr = 8 Beta(3/2, 1/4) exp(27 t_J/4) sum_(i,j) B_qi B_rj/(-27/4 - alpha_i - alpha_j), all denominators positive; exact rational joins (C^3, nonzero fourth jump), exact rational LDL positive definiteness, Laplace-transform identity check, 512/640-bit interval enclosures from the original k and t_+ | VERIFIED (V260, review recorded as V263). Input side only. The span meets the high input space in dimension 3 and the high graph domain in dimension 2 (THEOREM, V260, V263); no output Gram, singular value or complement inverse |
| exact scaled input Gram and strain of all 38 input columns of the far-junction section S1J1 (four inner-extended splines, three extra inner powers, 26 pure splines, five shifted outer columns) | computed from the read-only original data, not from the assembled matrix: 640-bit balls with exact dyadic endpoints, all 1444 entries replayed by a separate moment formula; exact disjoint-support blocks 33 and 5; agreement with V202 on the 676 pure entries and with V260 on the outer block; every stored strain coefficient with relative error below 2.701e-16 and absolute error below 2.053e-17 | VERIFIED (V267). Input side only; low conformity and positive definiteness proved analytically; no additional high dimension from this computation (the span meets the high input space in dimension 32 and the high graph domain in dimension 29 by exact jump ranks: THEOREM, V269, V275); output values floating |
| floating output of the completed far-junction section S1J1 (S_1 on L^2(w_a), first angular remainder mode, 38 columns, all 1569 cells once; complete projected core images after the exact jet split, not full A_0 images; low norms) | smallest generalized singular values 4.7481, 15.142, 34.29, 44.21 (about 4.7481 on the hyperplane of the stored binary strain row; in the low input metric the exact kernel of that row lies within relative distance 6.244e-16 of the exact strain kernel, true strain-zero dimensions 37, 31, 28 for the whole span and its high subspaces, input only: THEOREM, V282, V291); weakest direction concentrated in the outer power columns, Rayleigh quotient in [3.74, 5.59] under the accumulation-only model (not an enclosure); 50.32 without the outer columns; 5.8703 and 7.4692 restricted to the exact high input and high graph subspaces, still low-norm S_1 core values; input form within relative 0.000431058 of the exact Gram, which does not control the output | NUMERICAL (output floating, accuracy and operator meaning unresolved; the outer-column concentration does not show the small value spurious, V279; input comparison certified, V277); no output, high-norm or inverse bound |

By Prop IV.O of S2_BASIS_CERTIFICATION.md (THEOREM, V039), the S0 numbers cannot be uniform in the angular dimension and
cannot give an inverse bound. They are finite statements only, and conditional matrix certificates (valid if the
exported entry balls enclose the exact pairings).

Assembly audits. Summing the final blocks together with the retained cumulative checkpoints counts cells twice, and a
resumed run assembled from its final blocks alone omits cells (V180). The section, L^2-section and norm reductions use
the final worker files only and do not have this mechanism. The endpoint and finite-entry checks of the optional outer
margin merge do not prove coverage of the replaced region (exact radial and angular counterexamples, V181); a
replacement bound needs a complete exact radial cover and a finite bound for every angular box and every reported
quantity, or the retained old bound where no new one exists. No accepted original-data certificate in this file
depends on that merge, and none is withdrawn. The family combination takes maxima and minima of lower bounds and is
valid for matching boxes; its floating slack is not certified.

## 6. What still has to be certified for the closure (S2_CLOSURE.md 3.3)

- (A), (H_m) and (H_m') are VERIFIED (V077, section 4); both margins are at least 5/2 (V086). r_V follows from the perturbation formula of S2_CLOSURE.md
  3.5(a): for the fixed background the margin kappa_w - b_+ decreases by at most |c[h]|/3 + (51/4) ||D W[h]||_infinity
  for a = 17/4, plus ||grad h||_infinity when the coupling background moves (THEOREM, V075), so r_V needs the
  high-space constants C_c, C_W (and C_g) of these quantities.
- Hypothesis (Z) of Lemma H1: VERIFIED (V080). The verifier's own original-data cover (512-bit Green and Taylor
  enclosures on 3276 radial times 128 angular boxes and both analytic half-lines; 419220 boxes positive at once, 108
  refined exactly into 140 positive terminal boxes and 47 boxes inside the exact rectangle Q of V070; zero unresolved;
  separate 640-bit audit) gives |V|/r >= 3/12500 outside Q in the closed first quadrant away from 0. Full cover
  SHA-256 e10701a9aee56c3f1067dbb49aae63cdf236d9faf272f10e54bbdd45064346c7. The numerics team's own refinement
  (zrefine.py, rectangle mode) has its 34 exclusions inside the exact Q (V078), but 463 was its node count (359 terminal
  leaves: 34 inside, 325 positive) and only the minimum of the positive leaves is stored, so it is not a replayable
  certificate on its own; V080 does not use it.
- For Lemma IV.1 of S2_BASIS_CERTIFICATION.md: the split constant delta of the compact part, the adjoint defects
  eps_i and the norms ||psi_i||.
- For Theorem C' (S2_L2_THEORY.md 5.2): the axis-rate hypothesis (A) and the margin (M) are VERIFIED (V077), so
  Theorem C' is unconditional for the modal background (V047, V049 to V053, V055). The lift constant C_E and the
  coupling constants are needed only for an inverse bound.
- eta (the residual of rho~ in the forcing norm, including its axis jet; membership in Y_lo is THEOREM, V042, and in the
  fractional high target of order 25/4 for every origin exponent 0 < delta < 2, THEOREM, V076; the angular part of the
  norm is exact, ||f||_Y^2 = int omega(t)[gamma^2 + 2 B(1/4, 3/2) H(q)] dt, omega = e^{-t/2} (t < 0) and e^{27t/4}
  (t >= 0), gamma the axis value of the cofactor and H a rational Gram form in the cosine coefficients of
  (B - gamma)/cos^2(theta), moments m_0 = 1, m_1 = -5/7, (4n + 7) m_{n+1} = -10 m_n + (4n - 7) m_{n-1}, VERIFIED, V100,
  with directed code). Complete enclosure VERIFIED (V164): 6049.11 < ||F(rho~)||_Y < 8601.42, from interval integration
  of the exact normalized original modal trial over all angular modes, 1757 base intervals refined to 1860 leaves on
  -40 <= t <= 20, 3720 arithmetic checks, both analytic tails and thirteen 640-bit degree-36 replays; the two
  independent inner-tail bounds differ below 1e-140 and the larger is kept. Decoupled family VERIFIED (V174):
  ||F(rho~)||_(Y_a) < 485.632 = 60704/125 for every a in [18/5, 4] (squared upper enclosure about 235837.62), by
  pointwise domination of the angular weights and exact radial reintegration of the V164 envelopes with e^(123t/20) in
  place of e^(27t/4), at 384 and 768 bits, both half-lines included. Lower bound in the same family VERIFIED (V179):
  ||F(rho~)||_(Y_a) > 3.270 for every a in [18/5, 4], from eight disjoint radial windows of the V164 partition with
  fresh interval Taylor bounds in the new angular norm (all residual sine modes, exact beta-Chebyshev moments of the
  angular weight, 384 and 640 bit replays); since |cos theta|^(8 - 2a) increases with a, the bound at a = 18/5 holds
  for the whole interval. It is a partial lower bound, not a tight value. Both are low norms. High norm VERIFIED
  (V182) as a deliberately loose majorant: with a_* = e^(9t/5)(1 + e^t)^(-53/10), an explicit angular cutoff
  chi(theta) = S((16 - 144 cos^2 theta)/7) and an explicit square Littlewood-Paley partition for the variable order
  (an equivalent norm on the high target of Theorem E), ||F/(r^3 p a_*)||_(H^(25/4)) < 1.195e93 and eta_* < 6.321e129,
  from the exact angular cofactor division (l1 factor 2 * 522^2 * 1045), the radial L^1 norm and the total variation
  of the sixth radial derivative over all 1559 joins, exact cancellations at both ends and integral Green bounds
  (512 and 768 bits, separate 1024-bit scalar audit; an earlier direct end representation gave 1e163). It is an
  upper bound only, not an estimate, and does not test (S). High norm lower bound VERIFIED (V183): for every real t,
  eta_* >= |g_axis^(5)(t)| / C_5 with C_5^2 = Gamma(11/2) Gamma(3/4) / (2 pi Gamma(25/4)), C_5 = 0.234994524014653...,
  because the fifth derivative is bounded pointwise by the H^(25/4) norm of the axis summand alone (independent of the
  cutoff chi and of the Littlewood-Paley partition); at t = 8 the directed evaluation from the original data gives
  eta_* > 1906360017. Stronger lower bound VERIFIED (V192, after V186): the fractional difference inequality
  |f^(5)(t) - f^(5)(u)|^2 <= [8/(3 sqrt(2 pi))] |t - u|^(3/2) ||f||^2_(H^(25/4)(R)) (unitary transform; exact integral
  of (1 - cos x) x^(-5/2)) at t = 8 and u = 1001/125, where the two certified fifth derivatives differ by 1.0668240e9,
  gives eta_* > 38666592266 (V186: 36400585492 with the elementary constant sqrt(8 sqrt2/(3 pi))); so
  3.866e10 < eta_* < 6.321e129. A floating check by the theory author gives g_axis^(5)(1001/125) = -6.188399e8 (NUMERICAL). The size comes from knot-scale structure of the C^5 spline
  residual (knot spacing about 0.008 near t = 8) under the weight 1/a_* (a_*(8) about 6.9e-13): g(8) about 0.158 and
  g^(5)(8) about 4.48e8 (floating cross-check by the theory author by central differences at steps 2^(-17) to 2^(-20), agreeing with the
  certified value to about ten digits, NUMERICAL). In this norm (S) requires K_L C K_H < 1/eta_* < 2.6e-11; this is not
  a refutation, since K_H, K_L and C are not computed and change with the equivalent norm. Floating fifth differences
  at every fourth span midpoint (theory author, once) put the knot-scale structure in t in [1.92, 2.62] (|g_axis^(5)| up to
  6.06e9) and t in [7.9, 8.135] (up to 1.93e9), with at most 2.1e6 elsewhere, so the actual eta_* is probably much
  larger than its certified lower bound (NUMERICAL). Necessary consequences of (I) and (S) without constants (THEOREMS,
  V185, V194, V199): eta_0 |c[d]| <= N4 ||A_0 d|| with 0 < N4 < 9.06, and, if c[d] != 0, ||R_d|| > 1956082280 |c[d]| and
  ||R_d|| > 0.0507 eta_0 |c[d]| for the residual-subtracted image R_d = A_0 d - c[d] f_0/(ell_0 n'_0); no upper bound
  for either quotient is certified. An exact admissible direction with c[d] = 1 (a Gaussian density, report 6.5 item 10;
  THEOREM, V273, verifier proof, independent audit recorded as V283) makes each test one explicit norm computation;
  it has not been done.
  Earlier lower bound
  VERIFIED (V110): ||F(rho~)||_Y > 933.47, from the remainder energy on the window 9.9 <= t <= 10.1 in directed
  arithmetic; six point densities VERIFIED (V107). NUMERICAL value (theory author, once; original data, all angular modes,
  exact quotient moments of V100, 81 radii on [0, 20] at spacing 1/4 plus points to t = 60, log-linear quadrature and a
  tail at the fitted rate): eta about 7240.7, squared norm 5.2427e7, axis energy about 123.4 (axis norm about 11.1);
  halving the step changes the squared norm by about 1 percent; 69.8 percent of the energy on 8.135 <= t <= 12 and
  25.0 percent on 12 <= t <= 20; the far density decays at the rate 4k - 5/4. The quadrature arithmetic is CONFIRMED
  (V122: 7240.660899292548 reproduced, coarser nodes 7202.41, trapezoids 7253.47; no interpolation, inner-tail or
  outer-tail bound, so it is not a certified value). The far rate is a THEOREM (V120): the residual has a nonzero term
  of degree 2k - 1, remainder energy coefficient in (4577286933.12061, 4577286933.12062) in the t variable, and the
  remainder energy at t = 33/4 lies in (4618467.1665640262, 4618467.1665640263); this asymptotic statement is not a
  finite-radius tail bound. Far tail VERIFIED (V125): the full Y energy beyond t = 20 lies in (203443.34, 203445.56),
  beyond 25 in (14192.84666678, 14192.84666680), beyond 30 in (990.0012675088110412, 990.0012675088110415); V123: < 3175
  beyond 40, < 0.666 beyond 45. The interval [0, 20] is covered by the enclosure of V164. The energy is a layer at the vertical axis (94 to 99.7
  percent within 0.01 rad for 4 <= t <= 10), and truncated angular projections at 60 or 120 modes miss most of it (the
  raw-sine section is not contractive, V111). Weight family (NUMERICAL): eta about 7241, 1006, 212 at a = 17/4 and far
  shift Delta = 0, 0.2, 0.4; 791, 83, 14 at a = 3.8; 396, 38, 5.3 at a = 3.6 (weight factor e^(-2 Delta t) for t >= 0).
  These are floating values from ball inputs without a quadrature error bound; they are not certificates. The margin
  variation formula is CONFIRMED, and in the tied family a <= 4 loses the finite-J scalar inverse, V121), K_H, K_L,
  C_B and C_V (finite for the fractional high space, V073; not computed).
- For the finite-rank split of Lemma IV.1: grid scale estimates of the required rank are in S2_BASIS_CERTIFICATION.md
  6.1 (NUMERICAL). With the first-order commutator bound: about 1e9 (global), about 1e2 to 1e4 for local sup-norm
  proxies. With the second-order principal energy (V096): grid values sum_ij S2(B_ij) about 2.15e4 and S2(b_eta) about
  3.46e4 at eta = 0.1, giving about 3.4e4 to 5.2e4 low modes per parity class (global moments), 1.3e4 to 2.8e4 with
  radial localization or the vertical-axis strip removed, and about 130 for the local sup-norm proxy. Enclosures of the
  moments, of the first moments S_1(g_j) of the full Mellin error (V098) and of M_20, M_21, M_40, M_41 (V095, V099) are
  needed for any certified count. The complete input list of the certificate is INJ-Q (CONDITIONAL THEOREM, V102):
  eps (from c_loc, the regular-patch bounds E_j, eps_small and the finite-rank errors delta_l), delta_F, the Gram bounds
  e, p, d of the output, adjoint-witness and residual columns, and M_C >= ||C_R||; then ||S_1^{-1}||_R <=
  (1 + e p)/(5/2 - eps - delta_F - e d). The lift error of the axis strip needs M_gamma = sup [|alpha'' - alpha| N_0/y +
  |alpha - alpha'| N_1 + 2|alpha| y N_2] on the window, with the closed majorants N_j of V105 and enclosures of the axis
  coefficient alpha and its first two derivatives (not done).
Besides (A), (H_m), (H_m') and (Z), which are VERIFIED, the low and high residual enclosures above (V164, V174, V179,
V182, V183, V192) and the other constants marked VERIFIED in this list are available. Still missing at this version: the inverse
constants (K_H, K_L, C_E and the Gram bounds e, p, d of INJ-Q), the finite-rank split (delta of Lemma IV.1; eps,
delta_F and M_gamma of INJ-Q), the adjoint constants (eps_i, ||psi_i||) and the nonlinear constants (C_c, C_W, C_g,
C, C_B, C_V).
