# T2_FAR_C1_v01: row C1 of the 013 far owner table (a certified upper SC^+ of the Hessian term of Lemma HSB for the complete 013 far piece at erflog 8, rho 1)

Agent the second theory agent, written 2026-11-03T15:18Z for the coordinator 14:05Z item 4(b) ("the second theory agent takes, in order, C5a, C5b and C1, then the
assembly F ... each item goes to the theory auditor when it is ready"). Row C1 is that of notes/T2_013_FAR_OWNERS_v01.md section
2.1. Theorem C1 below is CLAIMED here and submitted to the theory auditor. It is a computer-assisted statement: the proof is the
argument of sections 1 to 4 together with the ball-arithmetic runs of section 6, whose code is listed there with its
SHA256. Paths are relative to research/h4/far009/ of agent the second theory agent unless another agent is named. The objects (c, q,
lambda, the two exact inputs, atil_013, the erflog cut and a_f) are those of notes/T2_FAR_C5_v01.md section 1; Theorems
C5a and C5b of that note are CONFIRMED by the theory auditor (AT-1147 to AT-1152, with the sentence correction AT-1151, which does
not concern this note).

## 0. Summary

1. Theorem C1. Let a_f = chi_E(|x|) atil_013(x) be the complete 013 far piece at the erflog cut lam = 8, rho = 1,
   unwindowed and with all angular modes, and q = 21/10. Then for every x in R^2
       E(x) = (1/2)[(q^2 - 1) lambda_max(D^2 a_f(x)) + Delta a_f(x)] <= SC^+ = 0.465650,
   where SC^+ is the binary64 number 0.46564943200002806. Hence SC(a_f) = sup_x max(0, E(x)) <= SC^+. The largest panel
   bound is attained on the panel |log r - 0.40625| <= 1/32 (1.4549 <= r <= 1.5489).
2. Comparison with Gbar = q (c - 3/2) = 14674311533937489/22517998136852480 (exact rational arithmetic on the
   binary64 value of SC^+): Gbar - SC^+ = 8377636983468883/45035996273704960 > 0.186020. So the C1
   inequality SC^+ <= Gbar - S^+ of T2_013_FAR_OWNERS_v01 section 1 holds for every certified S^+ <= 0.186020.
   The FLOAT values of S_h^B are 0.0227
   (Perron weight) and 0.0262 (h = 1) at Rw 50, Ww 10; at those values the room left in the C1 inequality is
   0.1633 and 0.1598. These are not bounds of S^+: S^+ is row C4, which needs the majorant of row C3.
3. By-products on the same cells and with the same proof (for row T3 and for comparisons; all at erflog 8, rho 1):
   sup_x lambda_max(D^2 a_f(x)) <= Lambda^+ = 0.2135 (FLOAT Lambda_+ 0.2110 in row T3), and
   -0.3355 <= a_f(x) <= 0.4365 for every x, so osc(a_f) <= 0.7719 (sampled osc(a_f) 0.7711).
4. FLOAT comparison (no bound): the sampled SC of the FLOAT runs is 0.4598 (N 2048) and 0.4608 (N 3072), on the
   windowed field with 8 angular modes; a point scan with the engine of this note (code/c1/scan_points.py,
   runs/c1_scan_points_1438.out; 128 angles per y, y step 0.1) gave 0.459053 at y = 0.4, theta = 0.0061. The
   certified SC^+ exceeds the larger sampled value by 0.0049, the price of the cell widths.
5. Cost. Region II (e^-4 <= r <= e^10): 263 kept panels (39 of the 224 base panels of half-width 1/32
   bisected once, none twice), 482 s on one core at 256 bits. Regions I and III: under 1 s.
6. Not done here. C1 certifies one of the inputs of the direct-route far inequality. A_low^+(8 pi) (row C2, blocked),
   S^+ (rows C3, C4), the identity binding (D0), the strain target (C6) and the near side (C7) remain open; the
   assembly row F states them. Row L1 (the same quantity at log 16, rho 2) needs a run with the log cut, which is not
   analytic at its two ends; section 5 item 4 says what that requires.

## 1. The quantity and two identities

Notation. x = (x_1, x_2) = (r cos theta, r sin theta), y = log r, d = (1/2)(d_1 - i d_2), dbar = (1/2)(d_1 + i d_2),
so Delta = 4 d dbar. Put k1 = (q^2 + 1)/4 = 541/400 and k2 = q^2 - 1 = 341/100.

Lemma E1. For every real C^2 function a and every x, lambda_max(D^2 a(x)) = Delta a(x)/2 + 2 |d^2 a(x)|, and hence
E(x) = k1 Delta a_f(x) + k2 |d^2 a_f(x)|.

Proof. For a real symmetric matrix with entries a_11, a_12, a_22 the larger eigenvalue is
(a_11 + a_22)/2 + (((a_11 - a_22)/2)^2 + a_12^2)^(1/2). Since d^2 a = (1/4)(a_11 - a_22 - 2 i a_12),
|d^2 a| = (1/2)(((a_11 - a_22)/2)^2 + a_12^2)^(1/2). Then (1/2)[(q^2 - 1)(Delta a/2 + 2 |d^2 a|) + Delta a] =
((q^2 + 1)/4) Delta a + (q^2 - 1) |d^2 a|. QED.

Lemma E2 (quadrant). E(R x) = E(x) for the reflections R of x_1 and of x_2, so SC(a_f) is the supremum of max(0, E)
over the closed first quadrant 0 <= theta <= pi/2. This is Theorem C5a (v).

Lemma M (mode calculus). For a C^1 function f of y and an integer n,
    d (f(y) e^(i n theta))    = (1/2) e^(-y) (f'(y) + n f(y)) e^(i (n - 1) theta),
    dbar (f(y) e^(i n theta)) = (1/2) e^(-y) (f'(y) - n f(y)) e^(i (n + 1) theta).
Proof. In the variables (y, theta), d = (1/2) e^(-y) e^(-i theta) (d_y - i d_theta) and
dbar = (1/2) e^(-y) e^(i theta) (d_y + i d_theta). QED.

Fields. With chi_007 the 007 potential (2982 generators) and phi the 013 correction (12273 atoms), put
Psi = d_1 d_2 chi_007 + d_1 phi. Then U_007 = (-psi_y, psi_x) with psi = d_1 d_2 chi_007, v = (-phi_xy, phi_xx), so
u_star = U_007 + v = (-Psi_y, Psi_x), u_star.X = -d_theta Psi and
    atil_013 = (-4 d_theta Psi - c)/(1 + 4 r^2),    a_f = chi_E atil_013.
With d_1 = d + dbar and d_1 d_2 = i (d^2 - dbar^2), every field is a finite sum over angular modes n of f_n(y)
e^(i n theta), and Lemma M computes the modes of Psi, atil_013, a_f, Delta a_f = 4 d dbar a_f and d^2 a_f exactly from
the mode functions of chi_007 and phi. A generator coef H_m (1 + r^2)^(p_j - m) T(t) contributes
(coef/2)(1 + r^2)^(p_j - m) T(t) r^(2m) to the modes 2m and -2m (the whole term to mode 0 if m = 0); an atom
coefficient_exact Im(z^n) r^(2h) (1 + r^2)^b (s + r^2)^(-d) P_k((r^2 - s)/(r^2 + s)) contributes -i/2 and i/2 times its
radial factor (including r^n) to the modes n and -n. Every angular mode is kept: there is no truncation.

Regions. Region I is r <= e^(Y0), Region II is e^(Y0) <= r <= e^(Y1) and Region III is r >= e^(Y1), with Y0 = -4 and
Y1 = 10. Theorem C1 is the maximum of the three bounds of sections 2 and 3 (and of 0, which is not needed).

## 2. Region II: Taylor models in y on panels

Lemma TM (Lagrange form for complex functions). Let F be a complex-valued C^M function on [y0 - delta, y0 + delta].
Let c_0, ..., c_(M-1) be complex balls (rectangles: a real ball plus i times a real ball) with F^(i)(y0)/i! in c_i,
and B a complex ball with F^(M)(xi)/M! in B for every xi in [y0 - delta, y0 + delta]. Then for every real tau with
|tau| <= delta, F(y0 + tau) lies in the ball-arithmetic value of sum_(i < M) c_i tau^i + B tau^M, and so in its value
at any real ball T that contains tau.

Proof. Taylor's formula with the Lagrange remainder for Re F gives Re F(y0 + tau) = sum_(i < M) Re(F^(i)(y0)/i!) tau^i
+ Re(F^(M)(xi_1)/M!) tau^M for some xi_1 between y0 and y0 + tau, and the same for Im F with some xi_2. Since tau is
real, these are the real and imaginary parts of sum_(i < M) c'_i tau^i + B' tau^M with c'_i in c_i and B' in B (B' has
real part Re F^(M)(xi_1)/M! in Re B and imaginary part Im F^(M)(xi_2)/M! in Im B, which is allowed because B is a
rectangle). Ball arithmetic is inclusion-monotone. QED.

Each mode function is real-analytic in y on R (every base 1 + e^(2y), s + e^(2y), e^(2y)/(1 + e^(2y)) and
1 + 4 e^(2y) is positive), so Lemma TM applies to every mode of Delta a_f, d^2 a_f and a_f on every panel.

Construction of the balls (code/c1/c1_sc.py, functions radial_pass, mode_pass, panel_models). Every radial
function is computed as a truncated power series in tau = y - y0 with ball coefficients (python-flint arb_series and
acb_series): first with the constant term the point y0 (the center pass) and then with the constant term the ball
[y0 - delta, y0 + delta] (the ball pass). The operations used (sums, products, inverses, exp, log, erfc of a series,
derivative, truncation) map enclosures of the first L Taylor coefficients of their arguments to enclosures of the first
L Taylor coefficients of the result, and for a ball constant term the result encloses the coefficients at every point
of the ball (inclusion monotonicity). The exact rationals of the inputs (c, coefficients, b_exact, scale_exact, p_j)
enter as arb enclosures num/den. The cut is chi_E = (1/2) erfc((yc - y)/sigma) with yc = log(rho lam^(1/2)) and
sigma = log(lam)/(2 pi^(1/2)) computed in arb. The series start with length N + 1 = 35; the derivative of a series of
valid length L has valid length L - 1. d_1 d_2 chi_007 uses two operations of Lemma M and d_1 phi one, so Psi,
atil_013 and a_f have valid length 33, and the two operations from a_f to Delta a_f and d^2 a_f leave 31. Exact
trailing zero coefficients, which python-flint drops from coeffs(), are restored to that length (panel_models). With
M = 30, c_i are the center-pass coefficients 0 to 29 and B is the ball-pass coefficient 30, as in Lemma TM (for a_f,
M = 32).

Cells. The panel |tau| <= delta is covered by nt = 8 cells T_it = [delta (2 it - 8)/8, delta (2 it - 6)/8],
it = 0, ..., 7, exact binary balls for dyadic delta, and the quadrant by nth = 128 cells
Theta_jt = [jt, jt + 1] (pi/2)/128 enclosed in arb. On a cell, Delta a_f lies in Re of
L = sum_n LV_n(T_it) e^(i n Theta_jt) and d^2 a_f in D = sum_n DV_n(T_it) e^(i n Theta_jt), where LV_n, DV_n are the
models of Lemma TM evaluated by Horner's rule at the ball T_it and e^(i n theta) is computed as exp(i n Theta_jt).
By Lemma E1, E <= k1 Re L + k2 |D| on the cell; the upper end of this ball, rounded upward to binary64 (function fup),
is the cell bound, and the panel bound is the largest cell bound. The same cells give lambda_max(D^2 a_f) <=
upper(Re L/2 + 2 |D|) and a_f in Re A with A = sum_n AV_n e^(i n Theta_jt) from the models of a_f (M = 32).

Panels. Region II is covered by 224 panels of half-width delta = 1/32 centered at -4 + (2 i + 1)/32. A panel whose
bound exceeds 0.55 or whose diagnostic max_n |B_n| delta^M exceeds 1e-3 is replaced by its two halves (at most three
times; code/c1/c1_region2.py). The diagnostic only steers the bisection: every kept panel bound is an upper bound by
the argument above, whatever its size. The kept panels cover [-4, 10] without gaps (checked exactly, section 6).

Result. 263 panels kept; maximum 0.46564943200002806 at y0 = 0.40625, delta = 1/32. Panel maxima by range of y
(binary64 uppers rounded up to 4 significant digits):

| y range | kept panels | max E upper | max lambda_max upper | a_f range (lower, upper) |
|---|---|---|---|---|
| [-4, -1] | 48 | 4.710e-30 | 3.747e-08 | [-6.36e-07, -4.03e-34] |
| [-1, 0] | 16 | 0.2110 | 0.09606 | [-0.00551, 0.00143] |
| [0, 0.25] | 4 | 0.4230 | 0.1928 | [-0.0224, 0.0108] |
| [0.25, 0.5] | 4 | 0.4657 | 0.2135 | [-0.0660, 0.0448] |
| [0.5, 0.75] | 4 | 0.4193 | 0.1976 | [-0.144, 0.123] |
| [0.75, 1] | 4 | 0.2560 | 0.1427 | [-0.238, 0.239] |
| [1, 2] | 26 | 0.2484 | 0.1078 | [-0.336, 0.437] |
| [2, 4] | 61 | 0.08472 | 0.04056 | [-0.289, 0.418] |
| [4, 10] | 96 | 0.01064 | 0.005007 | [-0.0943, 0.184] |

The bisected panels are the 39 consecutive base panels with y0 from 1.40625 to 3.78125, where the ball
pass at delta = 1/32 loses its accuracy: all of them had a diagnostic above 1e-3 (up to 0.24), and 25 of
them also a bound above 0.55. On their halves (delta = 1/64) the diagnostic is at most 7.3e-17. 54 kept
panels, all within -3.9375 <= y <= -0.5625, have a negative bound (E < 0 on the whole panel); this is
consistent with the theorem and not used. The a_f ranges are rounded outward to 3 significant digits.

## 3. Regions I and III

Lemma P (product rule). For c(x) = chi_E(|x|) and A = atil_013,
    |Delta (c A)| <= |c| |Delta A| + 4 |d c| (|d A| + |dbar A|) + |A| |Delta c|,
    |d^2 (c A)|   <= |c| |d^2 A| + 2 |d c| |d A| + |A| |d^2 c|,
with |d c| = |dbar c| = (1/2) e^(-y) |c_y|, Delta c = e^(-2y) c_yy and |d^2 c| <= (1/4) e^(-2y) (|c_yy| + 2 |c_y|).
Proof. Delta (c A) = c Delta A + 4 (d c dbar A + dbar c d A) + A Delta c and d^2 (c A) = c d^2 A + 2 d c d A + A d^2 c.
Lemma M with the mode -1 function (1/2) e^(-y) c_y of d c gives d^2 c = (1/4) e^(-2y) (c_yy - 2 c_y) e^(-2 i theta)
and 4 d dbar c = e^(-2y) c_yy. QED.
So E <= k1 |Delta a_f| + k2 |d^2 a_f| is bounded on a region by the suprema there of |A|, |d A|, |dbar A|,
|d^2 A|, |Delta A| and of the cut factors.

Lemma R1 (representation near 0). With w = r^2, every field X among A, d A, dbar A, d^2 A, Delta A is
X = sum_n w^(|n|/2) G_n(w) e^(i n theta), finite, with every G_n C-infinity on w > -1/8 (the bases 1 + w, s + w and
1 + 4 w are positive there; s ranges over the seven scales 1/8, 1/2, 1, 2, 9, 100, 900 of the atoms). For ' = d/dw,
    d:    (n, G) -> (n - 1, n G + w G') if n >= 1,   (n - 1, G') if n <= 0,
    dbar: (n, G) -> (n + 1, -n G + w G') if n <= -1,  (n + 1, G') if n >= 0.
Proof. For n >= 0, w^(n/2) e^(i n theta) G = z^n G(z zbar), and d (z^n G) = z^(n - 1)(n G + w G'), dbar (z^n G) =
z^(n + 1) G'; for n < 0 the field is zbar^|n| G and d (zbar^|n| G) = zbar^(|n| + 1) G', dbar (zbar^|n| G) =
zbar^(|n| - 1)(|n| G + w G'). An atom gives G = w^h (1 + w)^b (s + w)^(-d) P_k((w - s)/(w + s)) times constants, a
generator G = (1 + w)^(p_j - m) T(w/(1 + w)) times constants, and 1/(1 + 4 r^2) = (1 + 4 w)^(-1). QED.
Bound. Each G_n is computed as a truncated series in w with the constant term the ball [0, w0], w0 the binary64
upper of e^(2 Y0) (code/c1/c1_tails.py, function region1): its constant coefficient encloses G_n(w) for every w in
[0, w0], so sup_(r <= e^Y0) |X| <= sum_n w0^(|n|/2) |G_n([0, w0])|.
Cut factors on y <= Y0. With z = (y - yc)/sigma < 0: c = (1/2) erfc(|z|) <= e^(-z^2)/(2 |z| pi^(1/2)) (the Mills bound
erfc(t) <= e^(-t^2)/(t pi^(1/2)) for t > 0), c_y = e^(-z^2)/(sigma pi^(1/2)), |c_yy| = 2 |z| e^(-z^2)/(sigma^2 pi^(1/2)).
Each factor used, with its weight e^(-y) or e^(-2y), has the form e^(-k y) |z|^j e^(-z^2) with k in {0, 1, 2} and j in
{-1, 0, 1}; its logarithmic derivative in y is -k - j/(sigma |z|) + 2 |z|/sigma, which is positive for all y <= Y0
because 2 |z(Y0)|/sigma > 2 + 1/(sigma |z(Y0)|) (checked in arb; z(Y0) = -8.59) and the left side grows as y
decreases. So each supremum over y <= Y0 is the value at Y0.

Lemma R3 (representation at infinity). With v = r^(-2), every field X among A, d A, dbar A, d^2 A, Delta A is
X = sum over (n, tau) of e^(tau y) g(v) e^(i n theta), finite, with every g C-infinity on v > -1/900 (the bases
1 + v, 1 + s v and 4 + v are positive there), and with ' = d/dv
    d:    (n, tau, g) -> (n - 1, tau - 1, (1/2)((tau + n) g - 2 v g')),
    dbar: (n, tau, g) -> (n + 1, tau - 1, (1/2)((tau - n) g - 2 v g')).
Proof. For f = e^(tau y) g(e^(-2y)), f' = e^(tau y)(tau g - 2 v g'), and Lemma M. An atom has tau = n + 2h + 2b - 2d
and g = (1 + v)^b (1 + s v)^(-d) P_k((1 - s v)/(1 + s v)) times constants, a generator tau = 2 p_j and
g = (1 + v)^(p_j - m) T(1/(1 + v)) times constants, and 1/(1 + 4 r^2) = e^(-2y) (4 + v)^(-1). The exponents tau are
kept as exact rationals. QED.
Bound. Every tau that occurs in the five fields is negative (asserted; the largest is 2 p_max - 4 = -lambda = -0.4476
for A), so sup_(r >= e^Y1) |X| <= sum e^(tau Y1) |g([0, v1])|, v1 the binary64 upper of e^(-2 Y1).
Cut factors on y >= Y1. 0 < c < 1, and for z > 1 (z(Y1) = 15.3) the factors e^(-z^2), z e^(-z^2) and their products
with e^(-y), e^(-2y) are decreasing, so their suprema are the values at Y1.

Check of the representations (not a bound; code/c1/c1_tails_check.py, runs/c1_tails_check_1507.json): with the point
w = e^(2Y) (resp. v = e^(-2Y)) in place of the ball, the mode values of Lemma R1 at Y = -4.5 and -6 and of Lemma R3 at
Y = 10.5 and 12 agree with those of the Region II engine at the same y on all 161 modes, to 5.3e-67 or better.

Results (runs/c1_tails_1507.json):

| region | sup abs(A) | sup abs(d A), abs(dbar A) | sup abs(d^2 A) | sup abs(Delta A) | sup c | E upper | lambda_max upper | sup abs(a_f) |
|---|---|---|---|---|---|---|---|---|
| I (r <= e^-4) | 3.228e+05 | 1.895e+07 | 1.188e+09 | 6.044e+08 | 2.885e-34 | 6.173e-22 | 2.820e-22 | 9.308e-29 |
| III (r >= e^10) | 0.1504 | 5.872e-05 | 3.036e-08 | 1.207e-07 | 1 | 2.668e-07 | 1.211e-07 | 0.1504 |

The Region I suprema of A and its derivatives are crude (the ball [0, w0] loses the cancellations between the large
atom coefficients; atil_013(0) = -c, about -1.8103), but they are multiplied by cut factors below 1e-30. In Region III
the column sup c is the bound 1 of 0 < c < 1.

## 4. Theorem C1

Theorem C1. Let c, q = 21/10, Candidate 007 (data/C1-N1-007_exact.json, SHA256
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21), the C2-N1-013 correction
(inputs013/phi_007_b18s2_phi_exact.json, SHA256 a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a),
atil_013 and the erflog cut chi_E with lam = 8, rho = 1 be as in notes/T2_FAR_C5_v01.md section 1, and
a_f = chi_E(|x|) atil_013(x) on R^2 (unwindowed, all angular modes). Then for every x in R^2:
(i) E(x) = (1/2)[(q^2 - 1) lambda_max(D^2 a_f(x)) + Delta a_f(x)] <= 0.46564943200002806,
    so SC(a_f) <= SC^+ = 0.46564943200002806;
(ii) lambda_max(D^2 a_f(x)) <= 0.2134920580043215;
(iii) -0.33547165257164097 <= a_f(x) <= 0.436419343821821;
(iv) Gbar - SC^+ = 8377636983468883/45035996273704960 (exact), so SC^+ <= Gbar - S for every S <= 0.186020.

Proof. By Lemma E2 it suffices to take 0 <= theta <= pi/2. Region II: section 2 (every kept panel bound is an upper of
E on its panel times the quadrant; the kept panels cover -4 <= y <= 10). Regions I and III: section 3 (Lemmas P, R1,
R3 and the cut factors). The three regions cover R^2 (Region I contains x = 0, where the representation of Lemma R1
holds). The bound in (i) is the largest of the three region bounds, which is the Region II maximum; (ii) and (iii)
are the maxima (minimum) of the corresponding by-products over the three regions. (iv) is exact rational arithmetic
on the binary64 number SC^+. QED.

Hypotheses on the tools. The proof relies on the ball arithmetic of python-flint 0.9.0 (FLINT 3.6.0) being correct
(each operation returns a ball containing the exact result for all inputs in the input balls) and on the code of
section 6 implementing sections 2 and 3. The check runs below (FD check, representation check, the preliminary run)
are tests of the code, not parts of the proof.

## 5. Remarks

1. The engine is independent of the numerical auditor's 013 panels: it reads only the two exact JSON inputs.
2. Independent check of the field and of its second derivatives (code/c1/c1_fd_check.py, runs/c1_fd_check_1516.json;
   not a bound: the truncation error of order h^2 of the difference quotients is not enclosed). At five points, the
   Hessian of chi_E (atil_007 + datil_013) by central second differences with step 2^-60 of the Cartesian closed forms
   of code/c5_check.py (which were compared there with the FLOAT library) agrees with the mode sums of the engine at
   the same point (columns 4, 6 and 7 are absolute differences; column 4 is the upper end of an arb ball, columns 6 and
   7 are differences of midpoints, and column 8 is the arb radius of the difference quotient, which reflects the
   precision of the closed forms divided by h^2):

| r | theta | a_f (closed form) | a_f: modes - closed form | Delta a_f (modes) | Delta a_f: FD - modes | d^2 a_f: FD - modes | radius of the FD ball of Delta a_f | E (modes) |
|---|---|---|---|---|---|---|---|---|
| 1.49 | 0 | 0.0262910562085 | 7.3e-61 | 0.1994785271 | 0 in binary64 | 1.2e-24 | 9.1e-24 | 0.4592489172 |
| 1.5 | 1.2 | -0.0382401770222 | 2.7e-60 | -0.1612546716 | 0 in binary64 | 3.7e-24 | 2.9e-23 | -0.0809860386 |
| 0.7 | 0.6 | -0.000166913706891 | 6.2e-68 | -0.0130697490 | 0 in binary64 | 8.5e-32 | 6.6e-31 | -0.0054253006 |
| 3 | 0.9 | -0.125153468774 | 8.5e-57 | 0.1272549304 | 0 in binary64 | 1.2e-20 | 9.0e-20 | 0.2108555151 |
| 1.1 | 0.05 | 0.00320669061285 | 3.4e-63 | 0.1325037645 | 0 in binary64 | 4.6e-27 | 3.6e-26 | 0.2955526331 |

3. The preliminary run runs/c1_r2_1455.jsonl (engine before the patch that restores trailing zero coefficients and adds
   the by-products) gives the same 263 kept panels with identical panel bounds.
4. Row L1 (log 16, rho 2) needs the same computation with chi_L(r) = Sinf(log(r/rho)/log(lam)). Sinf is C-infinity but
   not analytic at t = 0 and t = 1, and its series cannot be formed on a ball that contains those points. Lemma TM only
   needs C^M, so panels that end exactly at y = log rho and y = log(rho lam) work on the open side, but the ball pass on
   a panel touching t = 0 needs a separate enclosure of the derivatives of exp(-1/t) near 0 (they vanish there). The
   room in row L1 is 0.545 (FLOAT SC 0.1001), so coarse panels suffice. Not started.
5. Rows T3 and L2' use lambda_max and osc. The values in (ii) and (iii) are for erflog 8, rho 1; T3 at this split
   needs Lambda_+^+ <= 0.2110 + 0.018 = 0.229 at the FLOAT remainders (row T3), and (ii) gives 0.2135.

## 6. Evidence

Interpreter: Python 3.12.13, python-flint 0.9.0 (FLINT 3.6.0), one core (taskset, nice 19, OMP_NUM_THREADS=1),
256-bit precision. Commands (from research/h4/far009/):
    python3 code/c1/c1_region2.py -4 10 0.03125 34 8 128 256 runs/c1_r2_1508.jsonl
    python3 code/c1/c1_tails.py -4 10 256 runs/c1_tails_1507.json
    python3 code/c1/c1_tails_check.py 256 runs/c1_tails_check_1507.json
    python3 code/c1/c1_fd_check.py 256 runs/c1_fd_check_1516.json

| file | role | SHA256 |
|---|---|---|
| code/c1/c1_sc.py | panel engine (sections 1, 2) | 87bd58e86ccc08c264fa04b053a5c49d1d0ca01fb318dd80ed3e984a2f992f51 |
| code/c1/c1_region2.py | Region II driver | 3740a161fc2ecf7b1dbeadddfdae3c94e9a01b755ac9b76a6078bb95c7743319 |
| code/c1/c1_tails.py | Regions I and III (section 3) | c65b24c13ec869e6a5071f4000bd96ee3823358baec7d4a16257049b4c2a1d9c |
| code/c1/c1_tails_check.py | representation check (not a bound) | b7d6ff6f4d70854e7f27ea337f57b6cc5728e90dc8f20a64c8640518bf2336b2 |
| code/c1/c1_fd_check.py | finite-difference check (not a bound) | fa508f31e0aa3b80c8120c1d29ef79a27b414b69407e727b9d020309bc4d5fc1 |
| code/lib/ipm_exact.py | canonical 007 terms for the FD check | de23cda3313f4a4e2dede0f20c69911f2fa11bc50de82fa331bfd576eb38470a |
| code/c5_check.py | source of the closed forms copied into the FD check | 8491a5be5983d27315f285eff72c7e11a9f9ae7ebca81c607ffa33b3ac08c395 |
| inputs013/phi_007_b18s2_phi_exact.json | 013 correction atoms (input) | a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a |
| data/C1-N1-007_exact.json | Candidate 007 generators (input) | ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21 |
| runs/c1_r2_1508.jsonl | Region II panels and summary | c094d5ab2f924c00c97a5894ed3af0352a48cd515c460f7c3bf893d260869bd3 |
| runs/c1_tails_1507.json | Regions I and III | 9c683ee8a79f3f1f597043242ffc951a75e3dc115e13d26b64a2a76656a9a8e8 |
| runs/c1_tails_check_1507.json | representation check | 4c13895109840174872d028fabdeff5a30ca244bf1800dcbaf78202f44fbe2bb |
| runs/c1_fd_check_1516.json | FD check | a05409244dfbec26982dfb595f6a2bfc14e58520ae72ced5cfba0d0cddd8dbcc |
| runs/c1_r2_1455.jsonl | preliminary Region II run (engine before the patch) | fb1bb36031830686c52fea36c1ea1637963be298fffaa12f888b71a260df8930 |

The panel file has one JSON line per panel (y0, delta, depth, upper, the diagnostic "remainder" = max_n |B_n| delta^M,
M, cell median, lambda_max and a_f bounds, seconds, and "bisected" for replaced panels) and a summary line. Coverage
check (exact, Fractions): the kept panels, sorted by y0, are [y0 - delta, y0 + delta] with consecutive ends equal,
from -4 to 10.
