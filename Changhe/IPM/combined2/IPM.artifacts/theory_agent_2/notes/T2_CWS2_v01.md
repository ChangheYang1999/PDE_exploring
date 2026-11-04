# T2_CWS2_v01: exact upper bounds for the S1 homogeneous weight constant at the P-S2 weight (1 + |X|^2)^(7/10)

Version 1. Owner: the second theory agent (theory agent). Written 2026-11-02T23:39Z.
Requested by the coordinator 23:01Z item 6 and 23:19Z item 5 (c_W at the P-S2 weight (1 + |X|^2)^(7/10) by the AT-133 recipe;
next priority after T2_EXP_v01). Plain-text mathematics as in T2_EXP_v01. Paths are relative to the combined2 root.

Inputs used (read-only): theory_audit/research/homogeneous_weight_methods/PROOF.md (AT-131, SHA256
368c319c0aa1d30db960733b6cc7e1b8a1e4faa8597d3ad78dda84ba9efce0f5), moment_dual_tensor/PROOF.md (AT-132,
13adf3401e2a199fe4c476bd7fe6aea7fe9891bc86e8190fad700fc0ee111631), weight_certificate_arithmetic/PROOF.md (AT-133,
5f7eedd07d4fb29389f53ed441608301d33d5c87f8adb22f1d99903b8856d107), ps1_exact_endpoint/PROOF.md (AT-135,
e3c6cfcd7ffe61b621e3c6df05eb452e7ce33d0aa7f4cbda23421ab9ccaf67d8); exchange/theory_requirements/theory_v02.md
(SHA256 051f3c3abac2d25dbab58fdeb08ac5486412b94455db078a331ec545ba519a1b; T3.4d, T4.1); theory_agent_2/notes/T2_EXP_v01.md.
Scripts (theory_agent_2/research/explicit/, Python): cw_exact.py (the certificate), cw_exact_check.py (independent FLOAT check),
cw_ps2_float.py (power iteration), cw_exact_chain.sh (job chain), with outputs cw_exact_*.out, cw_exact_*.json,
cw_exact_check.out, cw_ps2_float.out. SHA256 values are in theory_agent_2/scratch/cws2/freeze.log.

## Summary

| ID | statement | label | section |
|---|---|---|---|
| T2-CW-PS2 | at (sigma, r0) = (7/5, 1): c^hom_(S1)(2) <= 14131/10000, c^hom_(S1)(3) <= 23707/10000, c^hom_(S1)(21/10) <= 7441/5000 | CLAIMED (EXACT UB; certificate in the AT-133 interface, not yet audited) | 2 |
| T2-CW-PS1R | regression at P-S1 = (1, 1/2): the same script gives 8853/5000, 40583/10000, 9619/5000, each below the AT-135 values | CLAIMED (EXACT UB); the AT-135 values stay the quoted ones | 3 |
| T2-CW-TUP | the same certificate at P-BG2 (c^hom_(S1)(5/2) <= 33783/10000), P-Q2 (c^hom_(S1)(12/5) <= 5), P-Q1/P-BG1 (c^hom_(S1)(13/5) <= 87317/10000) | CLAIMED (EXACT UB) | 3 |
| T2-CW-BE | with the certified constants, the T4.1 break-even 0.881 of N_q(F_*; P-S2)/N_q(F_*; P-S1) becomes 0.881 x 9635/7441 = 1.141 | HEURISTIC (compares upper bounds; T4.1 assumptions) | 4 |
| T2-CW-FL | power-iteration values at P-S2 | FLOAT | 5 |

## 1. Setting and routes

W(X) = (1 + |X|^2/r0^2)^(sigma/2), a = W^(-1) = b(X/r0) with b(Y) = (1 + |Y|^2)^(-sigma/2), s = |Y|^2, J = (1 - Delta)^(1/2),
S1 the functions even in x and odd in y, and c^hom_(S1)(m) = || |D|^m a J^(-m) || on S1 L^2 (T2_EXP_v01 section 2.1).
The routes are exactly those of AT-135, with general (sigma, r0); x_i = ||grad^i g||_2 (ordered tensor norms).
- Order two: ||grad^2(ag)||_2 <= x_2 + (2 A_1 + H_2) x_1, A_1 = sup |grad a|, H_2 = sup |X| |grad^2 a|_F (Leibniz, S1 Hardy
  ||g/|X|||_2 <= ||grad g||_2 of AT-131), then the closed form [1 + (1 + c^2)^(1/2)]/2 of AT-132 (2) with c = 2 A_1 + H_2.
- Order three: ||grad^3(ag)||_2 <= x_3 + 3 A_1 x_2 + H_3 x_1 + K(1,3) ||t_2a||_2 ||g||_(H^3), H_3 = sup |X| |grad^3 a|_F,
  t_2^2 = 3 |grad^2 a|_F^2 + 6 |grad^2 a|_op^2 (tensor factor, AT-132 (3)), K(1,3) = 1/(4 pi^(1/2)) (AT-131); then the
  dual bound AT-132 (1) with rational t_i > 0 and a rational S >= sup_(p >= 0) Q_t(p)/(1 + p)^3,
  Q_t(p) = sum_i c_i p^i/(2 t_i), (c_1, c_2, c_3) = (H_3, 3 A_1, 1): the linear form is at most S + sum_i c_i t_i/2.
- Interpolation T2-EXP-HI (AT-131): c^hom_(S1)(q) <= c_2^(3-q) c_3^(q-2), proved for q = a/b by exact integer powers
  c_2^(3b-a) c_3^(a-2b) < C_q^b.
- Scaling: A_1 = A_1b/r0, H_2 = H_2b/r0, H_3 = H_3b/r0^2, ||t_2a||_2 = ||t_2b||_2/r0, and ||t_2b||_2^2 = pi I with
  I = int_0^inf t_2b^2 ds (polar measure dY = pi ds), so K(1,3) ||t_2a||_2 = I^(1/2)/(4 r0).

Certificate arithmetic (AT-133 interface; research/explicit/cw_exact.py). FLOAT is used only to propose rationals.
- Radial polynomials: |grad^l b|_F^2 = P_l(s)(1 + s)^(-sigma-2l) by exact differentiation of the ordered tensors on the
  x axis (sympy).
- Radial suprema: for sigma = n/d, a proposed rational h with h^2 (1 + s)^gamma - Q(s) > 0 on s >= 0 is proved after the
  substitution 1 + s = u^d, which turns (1 + s)^gamma into the integer power u^(gamma d): the polynomial is positive at
  u = 1, and a complete exact rational Sturm chain has the same number of sign variations at u = 1 and at +inf, so it
  has no root in (1, inf). The limit at infinity is included (degree Q < gamma in every case).
- Hessian integral: split at s = 2/sigma, where the larger Hessian eigenvalue changes (AT-133); exact antiderivatives
  in u = 1 + s give I = alpha + beta rho^(-n) with rational alpha, beta and rho = (1 + 2/sigma)^(1/d), enclosed by
  rationals lo <= rho <= hi with lo^d <= 1 + 2/sigma <= hi^d checked exactly. The upper end of I is used.
- Dual witness: S(1 + p)^3 - Q_t(p) > 0 on p >= 0 by a Sturm chain; t_i are rational and positive.
- All outward roundings are to rationals with denominators 10^4 or 10^6, checked exactly; the JSON files hold every
  rational, polynomial and Sturm count.
Independent check (research/explicit/cw_exact_check.py, .out; mpmath at 30 digits, not a certificate): the radial data
are recomputed by one-variable calculus (|grad^2 b|_F^2 = f''^2 + (f'/r)^2, |grad^3 b|_F^2 = f'''^2 +
3 (f''/r - f'/r^2)^2 for radial f in the plane), the suprema by root finding, I by quadrature, and the dual witness
polynomial by sympy count_roots. Every certified rational lies above the corresponding mpmath value.

## 2. P-S2 = (21/10, 7/5, 1) [T2-CW-PS2, CLAIMED]

Radial data (sigma = 7/5, r0 = 1):
- |grad b|^2 = (49/25) s (1 + s)^(-17/5); |grad^2 b|_F^2 = (49/625)(169 s^2 - 70 s + 50)(1 + s)^(-27/5) (this is
  sigma^2 {[(sigma + 1) s - 1]^2 + (1 + s)^2}); |grad^3 b|_F^2 = (42483/15625) s (73 s^2 - 70 s + 100)(1 + s)^(-37/5).
- A_1 = sup |grad b| < 499883/10^6 (FLOAT 0.4998818; attained at s = 1/(sigma + 1) = 5/12), H_2 < 528107/10^6 (FLOAT
  0.5281059), H_3 < 1747079/10^6 (FLOAT 1.7470770). With 1 + s = u^5 the three polynomial tests have degrees 17, 27 and 37
  in u; their Sturm chains (lengths 7, 17, 22) have 3, 8 and 10 sign variations at u = 1 and at +inf.
- Hessian integral: the split point is s = 10/7; I = 1911/220 + (69629/31790) rho^(-7), rho = (17/7)^(1/5), so
  I = 9.3187877142 (mpmath quadrature 9.31878771415458) and K(1,3) ||t_2a||_2 = I^(1/2)/4 <= 763169/10^6.
- Order two: c = 2 A_1 + H_2 <= 1527873/10^6 = 1.527873; [1 + (1 + c^2)^(1/2)]/2 = 1.413016 < 14131/10000.
- Order three: c_1 = H_3 <= 1.747079, c_2 = 3 A_1 <= 1.499649, c_3 = 1; t = (267/1000, 3289/10000, 1213/2000),
  S = 206101/250000, and
  S(1 + p)^3 - Q_t(p) = (513/303250000) p^3 + (159037317/822250000) p^2 - (26648987/33375000) p + 206101/250000,
  positive on p >= 0 (Sturm; sympy count_roots gives 0). The linear form is at most S + sum c_i t_i/2 <= 1.607506 (the
  FLOAT dual optimum of the same majorant is 1.607498), and c^hom_(S1)(3) <= 1.607506 + 0.763169 < 23707/10000.
- Interpolation at q = 21/10: (14131/10000)^9 (23707/10000) < (7441/5000)^10, so c^hom_(S1)(21/10) <= 7441/5000 = 1.4882.

These are valid constants for the fixed weight W = (1 + |X|^2)^(7/10) on S1, not the optimal ones. They do not certify
any background, source norm, inverse remainder or closure.

## 3. Regression at P-S1 and the other tuples [T2-CW-PS1R, T2-CW-TUP, CLAIMED]

At P-S1 = (21/10, 1, 1/2) the script reproduces the AT-135 radial polynomials (5 s^2 - 2 s + 2 and
63 s^3 - 54 s^2 + 108 s) and the exact Hessian integral I = 199/36, and gives c^hom_(S1)(2) <= 8853/5000 = 1.7706,
c^hom_(S1)(3) <= 40583/10000 = 4.0583, c^hom_(S1)(21/10) <= 9619/5000 = 1.9238 (AT-135: 1773/1000, 508/125, 1927/1000).
The routes are the same, so the difference is only the rounding of the rationals; the AT-135 values stay the quoted
ones at P-S1.

The same script at the other AT-064 tuples (research/explicit/cw_exact_PBG2.out, cw_exact_PQ2.out, cw_exact_PQ1.out
and the .json files; the profile suprema depend on sigma only and are scaled by r0):

| tuple (q, sigma, r0) | c^hom_(S1)(2) <= | c^hom_(S1)(3) <= | c^hom_(S1)(q) <= | cw_hom_ub.out value (FLOAT, AT-133) |
|---|---|---|---|---|
| P-S2 (21/10, 7/5, 1) | 14131/10000 | 23707/10000 | 7441/5000 = 1.4882 | not computed there |
| P-S1 (21/10, 1, 1/2) | 8853/5000 | 40583/10000 | 9619/5000 = 1.9238 | 1.923637 |
| P-BG2 (5/2, 7/5, 1/2) | 21077/10000 | 13537/2500 | 33783/10000 = 3.3783 | 3.378171 |
| P-Q2 (12/5, 1, 1/4) | 2889/1000 | 56919/5000 | 5 | 4.999789 |
| P-Q1, P-BG1 (13/5, 7/5, 1/4) | 8991/2500 | 157729/10000 | 87317/10000 = 8.7317 | 8.731537 |

So the FLOAT values of cw_hom_ub.out that T2_EXP_v01 used for P-BG2, P-Q2 and P-Q1/P-BG1 (sections 2.4 and 4, table (a))
are now covered by containing upper bounds of the same routes, larger by a relative amount below 5e-5. Table (a) of
T2_EXP_v01 is not recomputed here; it stays HEURISTIC for its other inputs in any case.

## 4. Consequence for the tuple comparison [T2-CW-BE, HEURISTIC]

The level L6 of the gradient-only criterion is proportional to 1/c_W (theory_v02 T3.4d), and the admissible N(F) of
(CF3) scales exactly like 1/c (T2_EXP_v01 section 4, (S-c)). The certified constants available to the two criteria are
1927/1000 at P-S1 (AT-135) and 7441/5000 at P-S2 (section 2); their ratio is (7441/5000)/(1927/1000) = 7441/9635 =
0.7723. theory_v02 T4.1 compares the tuples at equal c_W (AT-142 item 4). With the certified constants and the other T4.1
assumptions unchanged (equal R_* and delta_0, the stated b values), P-S2 is better than P-S1 exactly when
N_q(F_*; P-S2)/N_q(F_*; P-S1) < 0.881 x 9635/7441 = 1.141.
- The FLOAT ratios reported so far (0.755 to 0.805; the coordinator 23:01Z item 2) lie below both 0.881 and 1.141. The weight
  caveat of theory_v02 T3.4c reading 5 is unchanged: W at P-S2 exceeds W at P-S1 beyond r = 5.389, so a far-field
  defect can still reverse the ordering. The window for that is now wider (a ratio up to 1.141 is tolerated).
- For the complete F_* of the grid center (theory_v02 T3.4c), N_2/L6 = 3.95 to 4.03 at P-S2 with c_W = 1 becomes at
  most 5.88 to 6.00 with c_W <= 7441/5000, against 8.32 to 8.49 at P-S1 with 1927/1000 (HEURISTIC orientation).
- This compares upper bounds. Both optimal constants are at least 1 (AT-124); the FLOAT values (section 5) are
  1.0473 at P-S1 and 1.0095 at P-S2, ratio 0.964.

## 5. FLOAT values at P-S2 [T2-CW-FL]

Power iteration on the periodic box (research/explicit/cw_ps2_float.py, .out; L = 40, N = 2048, S1 homogeneous).
The derivative jump of a at the box faces is 2 sigma (L/2)(1 + L^2/4)^(-sigma/2-1) = 0.0021 (T2_EXP_v01 section 2.5).
Every power-iteration value is a Rayleigh quotient, hence a lower estimate of the discrete operator norm.

| m | FLOAT value | iterations | certified UB (section 2) | UB/FLOAT |
|---|---|---|---|---|
| 2 | 1.00537 (the iteration cap 600 was reached) | 600 | 14131/10000 | 1.41 |
| 21/10 | 1.00952 | 414 | 7441/5000 | 1.47 |
| 3 | 1.15039 | 45 | 23707/10000 | 2.06 |

The L = 80 repetition of the 21/10 row was stopped before it finished, to free the core (logged in the .out file). As at
P-S1, most of the slack sits in the m = 2 endpoint (exponent 9/10) and comes from the Leibniz majorant and Hardy, not from
the dual step. The FLOAT values are close to the lower bound 1 of AT-124. At P-S1 the FLOAT values are 1.03262, 1.04730
and 1.44308 (T2_EXP_v01 section 2.5): the FLOAT ratio P-S2/P-S1 at q = 21/10 is 0.964, while the ratio of the certified
bounds is 0.772. So part of the gain in section 4 is a gain in the bound, not in the optimal constant.

## 6. Requests

- The theory auditor: please audit research/explicit/cw_exact.py and cw_exact_PS2.json against the AT-133 interface (radial
  polynomials, Sturm chains after 1 + s = u^5, the enclosure of (17/7)^(1/5), the dual witness, the interpolation
  powers), and the regression at P-S1 against AT-135.
- The first theory agent (theory_v03): quote c^hom_(S1)(21/10) <= 7441/5000 at P-S2 as CLAIMED (EXACT UB) until audited, with the
  endpoints 14131/10000 and 23707/10000; keep 1927/1000 at P-S1 (AT-135). In T4.1, the break-even at the certified
  constants is 1.141 instead of 0.881 (section 4).
- The coordinator: c_W at the P-S2 weight is done (section 2). The next the second theory agent items are C_eps_bar and Cbar (owner split of
  the coordinator 23:01Z item 6).

## 7. Files

- research/explicit/cw_exact.py: exact certificate, generic (sigma, r0, q); usage cw_exact.py NAME n d r0num r0den qnum
  qden. Outputs cw_exact_NAME.out (log) and cw_exact_NAME.json (all exact data).
- research/explicit/cw_exact_check.py (+ cw_exact_check.out): independent mpmath check for PS1 and PS2.
- research/explicit/cw_ps2_float.py (+ .out): power iteration, periodic box (section 5).
- research/explicit/cw_exact_chain.sh (+ cw_exact_chain.log): job chain for the other tuples.
