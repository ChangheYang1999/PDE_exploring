# T2_NEAR_R4_v01: certified (R4) near inputs at C2-N1-013 (Proposition R4: Lambda_+(a_n), sup((a_n)_- W^2), sup((a_n)_+ W^2), ||(a_n)_+||_1)

Agent the second theory agent, written 2026-11-04 in a work session, for item (R4) of NEAR_CHECK_v03 section 7 (the first theory agent agent,
research/closure_check/NEAR_CHECK_v03.md) and the plan posted in team notes of this agent at 2026-11-04T08:41Z.
Proposition R4 below is CLAIMED here and submitted to the theory auditor (theory audit) and the numerical auditor (replay). It is a
computer-assisted statement: the proof is the argument of sections 1 to 3 together with the ball-arithmetic runs of
section 4. The SHA256 of every file used (code, runs, parameter files, outputs and this note) is in
research/near_r4/SHA256SUMS_near_r4_v01 of agent the second theory agent, with paths relative to the agent directory; in the text, paths are
relative to research/h4/far009/ of agent the second theory agent unless another directory is named.

## 0. Summary

1. Objects. c = 4076476460239181/2251799813685248, the two exact inputs and atil = atil_013 = (4 u_star.X - c)/(1 + 4|x|^2),
   u_star = U_007 + v_013, are those of notes/T2_FAR_C5_v01.md section 1 and of Theorem C1 (notes/T2_FAR_C1_v01.md;
   engine code/c1/c1_sc.py, docstring). W^2 = 1 + 4|x|^2. The near cut is
       chi_n(r) = (1/2) erfc((log r - log 8^(1/2))/sigma),   sigma = log 8/(2 pi^(1/2)),
   so chi_n = 1 - chi_E with chi_E the erflog far cut at lam = 8, rho = 1 of Theorem C1, and
       a_n = chi_n(|x|) atil(x).
   This is the near coefficient of NEAR_CHECK_v03 and of the theory auditor's AT2364 (chi(r) = erfc(log(r/sqrt 8)/L)/2,
   L = log 8/(2 sqrt pi)), and the one of the FLOAT values of near_params_v02.json (the second theory agent 2026-11-03 11:32Z item 2).
2. Proposition R4. For every x in R^2 (binary64 numbers; their exact values are dyadic rationals, given in section 4):
       lambda_max(D^2 a_n(x)) <= U = 5901153228680477/281474976710656 = 20.96510780 (rounded up),
       a_n(x)_- W^2(x) <= 8.678463435,   a_n(x)_+ W^2(x) <= 8.547679596,
   and ||(a_n)_+||_1 <= 4.161116960 (decimals rounded up). Hence, with F = 8(2c - 1) = 2950576553396557/2^47
   (AT2364: Lambda_+(a_n) >= F, the origin value),
       F <= Lambda_+(a_n) = sup_x max(0, lambda_max(D^2 a_n(x))) <= U,   0 <= U - F <= 4.330309019e-7.
   By-products on the same cells: -1.810319210200 <= a_n(x) <= 0.4191136032 for every x (-c = -1.8103192102).
3. Status. Outward ball arithmetic (python-flint 0.9.0, arb, 256 bits) with the Taylor-model panel engine of Theorem
   C1, which the theory auditor CONFIRMED under its containing-arithmetic hypotheses (AT-1230 to AT-1234). The new code changes
   only the cut factor and adds outputs (section 2). Until an audit, the four values are UNAUDITED outward
   computations of this agent, not CONFIRMED inputs.
4. Use in NEAR_CHECK_v03 (a dry run, it proves nothing). The program near_check_v03.py of the first theory agent (copied unchanged,
   SHA256 264858463e52094d5fd5fde90764d12e38af0cdc585905298ca6aca5b08dc313) run on near_params_v02.json with only the
   four (R4) entries replaced by the values of item 2 (file research/near_r4/near_params_r4_v01.json of agent the second theory agent,
   status UNAUDITED) prints, at eps_rest = 0 and the regional beta_* = 704955805507/10^12 (AT2373, regional only):

   | quantity | plan of record (11/20, 72) | fallback (103/200, 68) |
   |---|---:|---:|
   | e_up | 154053513894/10^12 | 181888075312/10^12 |
   | e_up at the FLOAT (R4) values (NEAR_CHECK_v03) | 154017099351/10^12 | 181851660742/10^12 |
   | (a) cap-level margin, lower | 6.26569630599e-3 PASS | 1.34311348879e-2 PASS |
   | (a') H4 rate margin, lower | 9.02291613000e-4 PASS | 8.06773019500e-3 PASS |
   | (b) C_N_upper/D_lower, upper | 9.31103844156e-1 PASS | 9.15682880013e-1 PASS |
   | (c') D6(a_n) threshold of (a') | 63274.0 | 64756.8 |
   | required beta_* = b0 + e_up + eps_rest | 704053513894/10^12 + eps_rest | 696888075312/10^12 + eps_rest |

   The change of e_up against the FLOAT values, +3.6414543e-5 at the plan, is almost all the L1 term
   (t^-1 ||(a_n)_+||_1 nu^2/(8 sqrt(2 pi)), now 1.29691053832e-3): the certified L1 upper exceeds the FLOAT value by
   0.117 (2.9 percent), the price of the cell widths. The Lambda term costs (1 + q^2)(U - F)/(2 mu^2) <= 2.3e-10 at the plan.
   The other inputs of these rows (D4 to D6 of a_n, the whole-plane beta_*, eps_rest, the kernel uppers of the
   fallback) are as in near_params_v02.json and keep their statuses; H1 to H4 of NEAR_CHECK_v03 section 3 stay OPEN.
5. Not done here: D4, D5, D6 of a_n ((R1)), the whole-plane beta_*, eps_rest, and the hypotheses H1 to H4.

## 1. Reduction

Symmetry. atil is even in x_1 and in x_2 (Theorem C5a, CONFIRMED, AT-1147 to AT-1152) and chi_n is radial, so a_n,
a_n W^2 and lambda_max(D^2 a_n) are even in x_1 and in x_2. Suprema over R^2 equal suprema over the quarter plane
0 <= theta <= pi/2, and ||(a_n)_+||_1 is four times the integral over the quarter plane.

Hessian. For a real C^2 function f with d = (d_x - i d_y)/2, lambda_max(D^2 f) = Delta f/2 + 2 |d^2 f|, and for a
symmetric 2 x 2 matrix Y, lambda_max(Y) <= |tr Y|/2 + 2 |(Y_11 - Y_22 - 2 i Y_12)/4|.

Regions (y = log r): I: y <= Y0 = -22; II: -22 <= y <= 5; III: y >= Y1 = 5. Each bound of Proposition R4 is the
maximum (for the integral, the sum) of the three regional bounds.

## 2. Region II: panels

The panel engine is code/c1/an_sc.py on top of code/c1/c1_sc.py (frozen, unchanged). On a panel |y - y0| <= delta
every radial function is computed as a truncated power series in tau = y - y0 twice, with the center y0 and with
the constant term the ball [y0 +/- delta], which gives a Taylor model with Lagrange remainder for every field
(c1_sc.py docstring; Theorem C1 section 3). The functions mode_pass_n and panel_models_n are c1_sc.mode_pass and
c1_sc.panel_models with two changes:
- the cut series is (1/2) erfc((S - yc)/sigma) (chi_n) in place of (1/2) erfc((yc - S)/sigma) (chi_E), S the series of y;
- besides Delta a_n and d^2 a_n, the fields a_n = chi_n atil and a_n W^2 = chi_n (4 u_star.X - c) are kept; the
  numerator 4 u_star.X - c = -4 d_theta Psi - c is the one of c1_sc (atil times 1 + 4 r^2 before the division).
panel_bound_n splits a panel into nt tau-cells and the quarter circle into nth theta-cells and evaluates, on each
cell in ball arithmetic, lambda_max = Re(Delta a_n)/2 + 2 |d^2 a_n|, Re a_n and Re a_n W^2 (the sums over modes of
the Taylor models times e^(i n theta) on the theta ball); it returns the largest upper and smallest lower over the
cells, rounded outward to binary64. For the integral it adds, over the cells, an upper of the cell area times
max(0, upper of a_n on the cell); the cell {y_a <= y <= y_b, theta-cell} has area (pi/(2 nth)) (e^(2 y_b) - e^(2 y_a))/2.
The driver code/c1/an_region2.py covers [y_lo, y_hi] by panels of half-width 1/32 and bisects a panel whose
largest remainder term (the ball coefficient times delta^M, over the four models) exceeds 10^-3, at most 3 times.
code/c1/an_assemble.py checks that the kept panels of all panel files tile [Y0, Y1] with no gap or overlap and
that the files have the same N, nt, nth, precision, inputs, engine and cut.

## 3. Regions I and III

code/c1/an_tails.py uses the fields of atil and their sups from code/c1/c1_tails.py (region1, region3, cut_factors;
Theorem C1, unchanged) and differs from c1_tails.bound_E only in the cut factor in front of the atil terms.
With A = atil and c = chi_n, D^2(c A) = c D^2 A + Y where tr Y = 4 (dc dbarA + dbarc dA) + A Delta c and the
d^2-part of Y is 2 dc dA + A d^2 c; the cut derivatives of chi_n are minus those of chi_E, so c1_tails.cut_factors
bounds them (its monotonicity checks hold at Y0 = -22 and Y1 = 5).
- Region I (r <= e^-22; w = r^2 <= w0, w0 an upper of e^-44). 0 < chi_n <= 1, so lambda_max(c D^2 A) =
  c lambda_max(D^2 A) <= sup|Delta A|/2 + 2 sup|d^2 A| (sups of c1_tails over the disc), plus |tr Y|/2 + 2|d^2-part|
  bounded with the cut factors at Y0. The real upper of A on the disc, Re G_0([0, w0]) + sum_(n != 0)
  w0^(|n|/2) |G_n([0, w0])|, is -1.8103192101999979 < 0, so (a_n)_+ = 0 on the disc; |a_n W^2| <= sup|A| (1 + 4 w0).
- Region III (r >= e^5, z1 = (5 - log 8^(1/2))/sigma > 6.7). chi_n <= c0(z) = e^(-z^2)/(2 z pi^(1/2)), decreasing;
  lambda_max(D^2 a_n) <= c0(z1)(sup|Delta A|/2 + 2 sup|d^2 A|) + the cut terms; |chi_n'|/chi_n >= 2 z/sigma, so
  chi_n e^(2y) is decreasing for z >= sigma and |a_n W^2| <= c0(z1) e^(2 Y1) (e^(-2 Y1) + 4) sup|A| (sup|A| is a sum
  of e^(tau y)|g| with every tau < 0). The integral is at most 2 pi sup|A| e^(2 yc) sigma e^(sigma^2)
  erfc(z1 - sigma)/(4 z1), yc = log 8^(1/2) (from chi_n <= e^(-z^2)/(2 z1 pi^(1/2)) for z >= z1 and
  int_(z1)^inf e^(-z^2 + 2 sigma z) dz = e^(sigma^2) (pi^(1/2)/2) erfc(z1 - sigma)).
The step "Region I: the sup over the disc of |X| is at most sum_n w0^(|n|/2) |G_n([0, w0])|" is that of Theorem C1;
its ball [0, w0] overestimates the variation of the 013 atoms (the radius of the mode-0 coefficient of d^2 A grows
like w0 times about 3e12), which is why Y0 is -22 here and not -4 as in Theorem C1: at Y0 = -10 the same bound is
11491.6 (runs/an_tails_0900.json), at Y0 = -18 it is 20.966398210285284 = F + 1.29e-3, at Y0 = -22 it is U.

## 4. Runs (core 41, nice 19, one thread, Python 3.12.13, python-flint 0.9.0, 256 bits)

| run | command (from research/h4/far009/) | time | result |
|---|---|---|---|
| Region II, -10 <= y <= 5 | python3 code/c1/an_region2.py -10 5 0.03125 34 8 128 256 runs/an_r2_0847.jsonl | 717 s | 254 kept panels (240 base, 14 bisected once); lambda_max <= 20.96510713256535, a_n W^2 in [-8.678463434459818, 8.547679595702215], integral <= 4.161116959482913 |
| Region II, -22 <= y <= -10 | python3 code/c1/an_region2.py -22 -10 0.03125 34 8 128 256 runs/an_r2in_0901.jsonl | 467 s | 192 panels; lambda_max <= 20.96510736319997, a_n W^2 in [-1.8103192168807678, -1.8103192035192284], integral 0 |
| Regions I, III | python3 code/c1/an_tails.py -22 5 256 runs/an_tails_0910.json | 0.6 s | I: lambda_max <= 20.96510779623087, a_n < 0, a_n W^2 >= -1.8103192101999983; III: lambda_max <= 3.1e-14, a_n W^2 <= 2.8e-9, integral <= 2.1e-10 |
| assembly | python3 code/c1/an_assemble.py runs/an_r2in_0901.jsonl,runs/an_r2_0847.jsonl runs/an_tails_0910.json runs/an_r4_0910.json | < 1 s | item 2; exact rationals in the JSON |
| near check (dry run) | python3 -B near_check_v03.py near_params_r4_v01.json > near_check_v03_r4.out (in research/near_r4/ of agent the second theory agent) | < 1 s | item 4 |

Exact values (runs/an_r4_0910.json): U = 5901153228680477/2^48; sup((a_n)_- W^2) <= 2442770293098857/2^48;
sup((a_n)_+ W^2) <= 4811915830260861/2^49; ||(a_n)_+||_1 <= 21605754517791033335004488160772637/2^112 (the
parameter file uses the decimal 4.161116960, rounded up).

Checks (not bounds; scratch/an_fd_test.py of the agent directory): per mode, a_n + a_f - atil = 0 to 5e-66 at four radii
(a_f from c1_sc.mode_pass, so the two cuts add to 1); lambda_max of the engine agrees with a central-difference
Hessian of a_n (from point evaluations of the engine) to 1.6e-6 at y = -2 and to 1e-8 at y = 0.3, 1.1, 2.0.

## 5. Observations (FLOAT, not part of the proof)

- The Region II bound itself is at most F: the outward binary64 panel upper of lambda_max is F - 2.3e-7 or less for
  y >= -10 and exactly F (the binary64 number F) on the panels of -22 <= y <= -10, so lambda_max(D^2 a_n) <= F for
  e^-22 <= |x| <= e^5. The largest bound, U, is the Region I bound; U - F comes from the ball [0, w0] of Region I.
  Nothing here proves that the supremum is attained at the origin, and Proposition R4 does not need it.
- The certified sup((a_n)_+ W^2) and sup((a_n)_- W^2) exceed the FLOAT values 8.5262260 and 8.6524467 by 0.0215 and
  0.0260; their maxima lie on the panels |y - 1.03125| <= 1/32 and |y - 0.84375| <= 1/32.
