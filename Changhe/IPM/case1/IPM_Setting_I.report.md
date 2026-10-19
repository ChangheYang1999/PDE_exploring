# Final report: full-plane IPM self-similar profiles with even-x / odd-y symmetry (Setting I)

STATUS: FINAL. YES, strong numerical existence evidence (the YES endpoint of the prompt), for the explicitly
distinguished weaker problem P_2 (rho in C^(2,alpha)_loc, a only continuous with a(0) = 1), as stated in section 4. It is numerical evidence and not a proof. The independent verifier
recomputed or checked every number of section 4 as written and confirmed the endpoint against the standard defined
before 4.1; every statement of section 3 was checked by the verifier and by an external referee. The posed strong
setting is not answered (section 4, items (i) and (ii)).

## Summary
T0 = 2026-10-17T17:37:12Z (start of the investigation). T_end = 2026-10-19T12:04:44Z. Elapsed time = 42.46 hours.
The prompt's minimum of 24 hours of elapsed research time was met.

YES, strong numerical evidence, for the explicitly distinguished problem P_2 (section 1: P_m with m = 2).

(i) The posed strong setting (a smooth and even near 0) is not answered by this result.
(ii) On the computed trial family the B_3 estimator is about 0.30 natural units x*^(2 - p_3): B_3 = 0.299 to 0.303 on
    the candidate (medians over the evaluation configurations of the two forms of the independent evaluator's estimator
    and of the original form of R10; variant extremes 0.291 to 0.311), 0.298 to 0.303 on its control, positive in every
    variant; in either form it changes by less than 0.005 along the angular refinement m <= 100 to m <= 250, under a
    further 20750 iterations and with fit rows to 9000 L (4.1). The trial's own coefficient of y^3 |x|^(p_3) is +0.046
    in the same units (positive; the difference is carried by the trial's defects in the y and y^3 coefficients of the
    equation on the x-axis, 4.1). A C^infinity profile has B_3 = 0 (R7, proved). If an exact profile exists near the
    trials and has a well-defined nonzero B_3, it is not C^infinity near 0 and does not solve the strong setting. The
    estimator value is numerical evidence for this; no estimate transfers it to an exact profile, so it is not proved.
    It is not a NO theorem, and other branches are not excluded.
(iii) The class is stated only as far as proved: P_2 requires rho in C^(2,alpha)_loc and a continuous with a(0) = 1. No
    higher regularity of an exact profile is claimed. The trial satisfies the regularity, parity, normalization and
    growth requirements of P_2; its transport residual is nonzero, so it is an admissible trial density, not a member of
    P_2. The numerical claim is the one of 4.1 (evidence consistent with the existence of an exact profile of P_2 near
    the trial; neither the proximity nor the exponent is established); it is not a proved statement. Uniqueness within
    P_2 is not claimed, and other branches are not excluded.
(iv) The computation does not determine c_l: the tested exponents that the rule of 4.3 does not exclude on the
    candidate's radial basis with angular cap m <= 150 span [5.5524653, 5.5793640] (an observed span, not an enclosure
    of the exponent of an exact profile). The candidate is computed with c_l held fixed at 5.5753626, and its density
    satisfies c_l = (1 + psi_xy(0))/3 with psi computed from it by the canonical inverse (to 3.2e-9). The value
    5.5753626 was selected by rules that compare residual maxima of fits (4.3); the equation does not single it out. Its
    equal-budget free control has c_l = 5.5763712 and is reported next to it. The residual tests do not select a value
    inside an interval containing [5.5524653, 5.5793640] (fixed-c_l fits on the candidate's radial basis with angular
    cap m <= 150, at one iteration budget, 4.3). On that basis, and continued to the candidate's angular cap m <= 200
    (4.3), the tested value 5.6004662 is excluded at the attained level; no value between 5.5793640 and 5.6004662, and
    none above 5.6004662, was tested on that basis, so the largest tested value not excluded is 5.5793640 and the
    smallest tested value above it, 5.6004662, is excluded. At the lower end, the L2 objective, and the whole-box N_f on
    both configurations, at the lowest tested value 5.5524653 are above those at 5.5604082, so the lower end is
    bracketed at this budget (these quantities stop decreasing toward smaller c_l) in the sense of fits from
    transplanted starts (4.3: that fit had not flattened, and its residual maxima are above those of the free reference
    fit F2 while its L2 objective is below), not by a minimum of an objective over c_l. Continued for a further 21500
    iterations at their exponents, the fits at 5.5524653 and 5.5604082 keep that order in the whole-box N_f and in the
    L2 objective, the latter by 0.5 percent, a margin that shrank at every linearization (4.3). The value 5.5524653 is
    not excluded and no smaller value was tested, so the interval of values not excluded has no measured lower end. The
    six-digit values label computed fits; they are not digits of an exact exponent.

The symbols above are defined in the body: P_2 in section 1; the source point P = (x*, 0), the exponent p_3,
the coefficient B_3 and the results R7 and R10 in section 3; the fits (the candidate X3, its control F3, the free
fit F2), the rule of 4.3 and the length unit L in section 4.
Sections: 0 timing and environment; 1 problem; 2 admissible class and velocity law; 3 rigorous results;
4 main deliverable (the statement above with its evidence); 5 reproducibility; appendix: verification timeline.

## 0. Timeline and environment
- T0 = 2026-10-17T17:37:12Z (start of the investigation).
- T_end = 2026-10-19T12:04:44Z. Elapsed time T_end - T0 = 42.46 hours (42 h 27 min 32 s), so the prompt's minimum
  of 24 hours of elapsed research time was met.
- The independent verifier's final confirmation (11:59 in the appendix) covers this report as of 2026-10-19T11:50:47Z
  and the accompanying artifacts of that time. After it, for publication, only the following changed: the end time
  and the elapsed time, the wording of the status line, the description of the accompanying artifacts in section 5,
  the wording of six earlier appendix entries that referred to earlier versions of the report, and the last two
  appendix entries (12:04). No number of sections 1 to 4 changed.
- The work ran in 8 consecutive sessions of at most six hours between T0 and T_end, with long fits continuing between
  sessions; no time outside that interval is counted.
- Environment: shared Linux x86_64 machine (Intel Xeon Platinum 8275CL; every CPU process single-threaded), Python
  3.9.25 with numpy 2.0.2, scipy 1.13.1 and sympy 1.14.0; one NVIDIA A100-SXM4-80GB GPU, used by the numerical
  workstream through PyTorch 2.8.0 (CUDA 12.8) for the matrix-vector products inside LSQR of the long fits, with the
  LSQR vector updates and the column-scaling probes (5 (b)).
- Organization: a lead researcher (analysis, specification, this report), a numerical researcher (solver), and an independent
  verifier (separately written residual evaluators and audits of all analytic steps). External referee audits were obtained
  for the analytic claims.
- The verification timeline (UTC) is in the appendix at the end of this report.

## 1. Problem
Find rho on R^2 and a real c_l with
   (c_l X + U).grad rho = rho,   U = (-psi_y, psi_x),   -Laplace psi = d_x rho   on R^2,
rho(-x,y) = rho(x,y), rho(x,-y) = -rho(x,y), psi odd in x and in y, rho = x^2 y a(x,y) near 0 with a even in x and y and a(0) = 1,
and c_l = (1 + psi_xy(0))/3.
Two variants are distinguished throughout. Both require rho in C^{2,alpha}_loc(R^2) for some alpha in (0,1), the velocity
law of section 2 and the growth condition (A3). This global regularity is the report's choice of admissible class of
classical profiles: the prompt states the regularity of a near the center only.
- P_inf (the strong setting of the prompt): in addition, a is C^infinity near 0.
- P_2 (a weaker problem, stated explicitly; the prompt allows a weaker condition at the center only if the resulting
  problem is explicitly distinguished): in addition, rho = x^2 y a near 0 with a continuous, even in x and in y, a(0) = 1.
  Only continuity of a is required (a smooth a is allowed). With the common global regularity, P_inf is contained in P_2,
  so numerical evidence for P_2 does not by itself answer the stated problem P_inf. P_2 implies rho = x^2 y + o(|X|^3),
  and the factorization is a strictly stronger local condition than this jet condition (rho = x^2 y + y^5 satisfies the
  jet condition but is not of the form x^2 y a with a continuous; this compares local conditions, not sets of exact
  profiles).
  More generally P_m (m >= 2) denotes the same problem with C^{m,alpha} in place of C^{2,alpha}; sections 2 and 3 are
  stated for general m.

## 2. Admissible class and velocity law
Class A_m (m >= 2 or m = infinity):
- (A1) rho is in C^{m,alpha}_loc(R^2), real, even in x and odd in y.
- (A2) rho = x^2 y a near 0 as above.
- (A3) |rho(X)| + (1+|X|)|grad rho(X)| <= C(1+|X|)^gamma for some gamma < 1.
- (A4) U is given by the canonical law below, and the profile equation holds pointwise.
The canonical velocity law has three equivalent descriptions.
- (V1) Modal Green function. Write d_x rho = sum_{n>=1} f_n(r) sin(2n theta). Then psi = sum psi_n(r) sin(2n theta) with
  psi_n(r) = (1/(4n)) [ r^{-2n} int_0^r s^{2n+1} f_n ds + r^{2n} int_r^inf s^{1-2n} f_n ds ].
- (V2) Symmetric truncation of the singular integral U = lim_{R->inf} [ -rho/2 e_2 + PV int_{|Y|<R} K(X-Y) rho(Y) dY ], with
  K = (K1, K2), K1(Z) = -(1/pi) z1 z2/|Z|^4, K2(Z) = (1/(2pi))(z1^2 - z2^2)/|Z|^4.
- (V3) U is the unique field with div U = 0, curl U = -d_x rho, the stated parities and |U(X)| = o(|X|).
Gauge. The harmonic term lambda x y in psi adds the linearly growing field lambda(-x, y). (V3) excludes it, so psi_xy(0) is a
functional of rho. Under (A2),
   c := psi_xy(0) = int_0^inf rho_1(r) r^{-2} dr = (1/pi) int rho sin(3 theta) r^{-3} dX,
where rho_1 is the sin(3 theta) coefficient of rho.

## 3. Rigorous results (checked by the verifier and by an external referee)
Each item below was rederived by the independent verifier and audited by an external referee; conditions found in those
audits are part of the statements.
R1 (velocity law). For rho with (A1) and (A3), the three descriptions (V1), (V2) and (V3) agree; for
   0 < gamma < 1 (the range in force in R2), |U(X)| <= C(1+|X|)^gamma.
R2 (forced regime). Every nonzero profile in A_m (m >= 2) has 0 < gamma < 1 and c_l >= 1/gamma > 1. Along an escaping
   characteristic with rho(X0) != 0, e^{-c_l s} X(s) converges to a nonzero vector, and |rho(X)| <= C(1+|X|)^{1/c_l} uniformly.
   In particular there is no nonzero profile in the class with c_l <= 1.
R3 (center). 3c_l - c = 1. The origin is a saddle of W = c_l X + U with eigenvalues 1 - 2c_l < 0 (x-axis) and 4c_l - 1 > 0
   (y-axis).
R4 (no cycles). div W = 2c_l > 0, so W has no periodic orbit and no graphic bounding a region. If the zero set of W is finite,
   every backward orbit converges to a zero of W, and the indices of the zeros sum to +1.
R5 (source on the x-axis). Let x* be the first positive zero of w(x) = W_1(x,0). For every A_2 profile, d_x W_1(x*,0) = 2c_l - 1,
   d_y W_2(x*,0) = 1 and rho_y(x*,0) > 0. So P = (x*,0) is a hyperbolic source and psi_xy(P) = 1 - c_l.
R6 (fixed-field rigidity). Write W_2 = y b. On the basin of P in the upper half plane, every C^1 solution of W.grad rho = rho
   vanishing on the x-axis equals rho_y(P) y exp(-int_{-inf}^0 [b(Phi_t X) - 1] dt). This is rigidity for a fixed field W. It is
   not uniqueness of the coupled profile.
R7 (regularity at the center). For A_3 profiles (or C^3 axis data), G_3(x) = d_y^3 rho(x,0)/6 solves a first-order
   linear ODE with a regular singular point at 0 and exponent p_3 = 6 + 2/(2c_l - 1), which lies in (6,8) and is never
   an even integer. If rho is C^infinity near 0, the coefficient B_3 of the homogeneous solution |x|^{p_3} e^{E(x)} in
   G_3 vanishes. The same holds for infinitely many higher odd j. The 2D statement that B_3 != 0 limits rho to C^6 or C^7
   is not proved.
R8 (weighted identities). For phi homogeneous of degree -d with 1/c_l + 2 < d < 5,
   (1 + (2 - d)c_l) int rho phi dX + int rho U.grad(phi) dX = 0.
   For phi = sin(3 theta) r^{-3}: int rho U.grad(phi) dX = pi (c_l - 1)(3c_l - 1).
R9 (positivity). Let rho be in A_2 and assume (Hmin): the zeros of W in the closed first quadrant are exactly 0 and P, and
   W_2(0,y) > 0 for y > 0. Then rho > 0 in the open first quadrant Q, rho(0,y) = 0 and k(y) = d_x^2 rho(0,y)/2 > 0 for all
   y > 0. (On the invariant y-axis, k(y_t) J(t)^2 = e^t k(y_0) with J(t) = exp int_0^t d_x W_1(0,y_s) ds, and k(y) = y a(0,y)
   > 0 near 0.) Positivity holds in Q, not in the whole upper half plane.
R10 (axis constraints and B_3 from the axis). Write w = W_1(x,0), h = d_y W_2(x,0), a2 = d_y^2 W_1(x,0)/2,
   b3 = d_y^3 W_2(x,0)/6, g = rho_y(x,0), A = 2c_l - 1, beta = 2/A, g0 = a(0) = 1.
   - For every A_2 profile: w' + h = 2c_l, h' - 2 a2 = -g', hence a2 = (g' - w'')/2; w g' = (1 - h) g, equivalently
     (w/g)' = A/g; |w(x)|/g(x) = A int_x^{x*} dt/g(t) on (0, x*]; and int_0^{x*} (1/g - 1/(g0 x^2)) dx = 1/(g0 x*).
   - For A_3 profiles (or C^3 axis data) also a2' + 3 b3 = 0, and the homogeneous solution of the G_3 equation is
     H = N g^{3+beta} |w|^{-beta}, N = A^beta / g0^{3+beta}, with H ~ x^{p_3} at 0, and
       B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^{beta - 1} dx,   m = |w|/g.
     So B_3 is determined by c_l and the single function w on [0, x*]. The finite part requires the even integrand factor to
     have an expansion k0 + k2 x^2 + k4 x^4 + O(x^6) at 0 (smooth axis data suffice; C^4 alone does not). At c_l = 3/2
     the integrand is a derivative and B_3 = a2(P)/(6 g(P)^3) = w''(P)(g(P) - 2)/(24 g(P)^3).
R11 (the limit c_l -> infinity is degenerate). The problem (X + U[F]).grad F = 0, F even in x and odd in y,
   psi_xy[F](0) = 3, has no solution with F in C^1, U[F] in C^1, U[F](X) = o(|X|) and finitely many zeros of X + U[F].
   (div(X + U) = 2, so there is no invariant Jordan curve; every alpha-limit set contains an equilibrium, F is constant on
   orbits, so F takes finitely many values and is 0 by oddness.) With F = rho/c_l, profiles with c_l -> infinity can only
   converge to a solution F of this problem, which the statement excludes when the limit field X + U[F] has finitely
   many zeros. This conclusion needs C^{1,alpha}_loc convergence and uniformly small far-field tails
   (sup_n int_{|Y|>R} |F_n|/|Y|^3 dY -> 0); without the tail condition it fails (F_n = R_n f(X/R_n)).
R12 (no local sign for B_3). The axis constraints of R10 do not determine the sign of B_3: for every A > 1 the compatible
   axis data w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L give B_3 = C_A L^{-4-2/A} (1 - S_A/L^2) with C_A > 0 and
   S_A = 6A(4A-3)/(8A-1), so B_3 takes both signs and the value 0. These are compatible axis data, not coupled profiles.

## 4. Main deliverable

YES, strong numerical evidence, for the explicitly distinguished problem P_2 (section 1: P_m with m = 2).

(i) The posed strong setting (a smooth and even near 0) is not answered by this result.
(ii) On the computed trial family the B_3 estimator is about 0.30 natural units x*^(2 - p_3): B_3 = 0.299 to 0.303 on
    the candidate (medians over the evaluation configurations of the two forms of the independent evaluator's estimator
    and of the original form of R10; variant extremes 0.291 to 0.311), 0.298 to 0.303 on its control, positive in every
    variant; in either form it changes by less than 0.005 along the angular refinement m <= 100 to m <= 250, under a
    further 20750 iterations and with fit rows to 9000 L (4.1). The trial's own coefficient of y^3 |x|^(p_3) is +0.046
    in the same units (positive; the difference is carried by the trial's defects in the y and y^3 coefficients of the
    equation on the x-axis, 4.1). A C^infinity profile has B_3 = 0 (R7, proved). If an exact profile exists near the
    trials and has a well-defined nonzero B_3, it is not C^infinity near 0 and does not solve the strong setting. The
    estimator value is numerical evidence for this; no estimate transfers it to an exact profile, so it is not proved.
    It is not a NO theorem, and other branches are not excluded.
(iii) The class is stated only as far as proved: P_2 requires rho in C^(2,alpha)_loc and a continuous with a(0) = 1. No
    higher regularity of an exact profile is claimed. The trial satisfies the regularity, parity, normalization and
    growth requirements of P_2; its transport residual is nonzero, so it is an admissible trial density, not a member of
    P_2. The numerical claim is the one of 4.1 (evidence consistent with the existence of an exact profile of P_2 near
    the trial; neither the proximity nor the exponent is established); it is not a proved statement. Uniqueness within
    P_2 is not claimed, and other branches are not excluded.
(iv) The computation does not determine c_l: the tested exponents that the rule of 4.3 does not exclude on the
    candidate's radial basis with angular cap m <= 150 span [5.5524653, 5.5793640] (an observed span, not an enclosure
    of the exponent of an exact profile). The candidate is computed with c_l held fixed at 5.5753626, and its density
    satisfies c_l = (1 + psi_xy(0))/3 with psi computed from it by the canonical inverse (to 3.2e-9). The value
    5.5753626 was selected by rules that compare residual maxima of fits (4.3); the equation does not single it out. Its
    equal-budget free control has c_l = 5.5763712 and is reported next to it. The residual tests do not select a value
    inside an interval containing [5.5524653, 5.5793640] (fixed-c_l fits on the candidate's radial basis with angular
    cap m <= 150, at one iteration budget, 4.3). On that basis, and continued to the candidate's angular cap m <= 200
    (4.3), the tested value 5.6004662 is excluded at the attained level; no value between 5.5793640 and 5.6004662, and
    none above 5.6004662, was tested on that basis, so the largest tested value not excluded is 5.5793640 and the
    smallest tested value above it, 5.6004662, is excluded. At the lower end, the L2 objective, and the whole-box N_f on
    both configurations, at the lowest tested value 5.5524653 are above those at 5.5604082, so the lower end is
    bracketed at this budget (these quantities stop decreasing toward smaller c_l) in the sense of fits from
    transplanted starts (4.3: that fit had not flattened, and its residual maxima are above those of the free reference
    fit F2 while its L2 objective is below), not by a minimum of an objective over c_l. Continued for a further 21500
    iterations at their exponents, the fits at 5.5524653 and 5.5604082 keep that order in the whole-box N_f and in the
    L2 objective, the latter by 0.5 percent, a margin that shrank at every linearization (4.3). The value 5.5524653 is
    not excluded and no smaller value was tested, so the interval of values not excluded has no measured lower end. The
    six-digit values label computed fits; they are not digits of an exact exponent.

Fits named in this section (all on the formula of 4.2 with 375 radial spline coefficients per angular mode; LSQR
iterations are inner iterations of the Gauss-Newton solver of 4.2):
  F0   free fit, angular cap m <= 150 (c_l from the identity during the fit).
  X1   F0 moved along its softest exponent direction by -1e-3 in c_l, refitted with c_l held at 5.5753626,
       750 LSQR iterations.
  F1   F0 continued with c_l free for the same 750 iterations (equal-budget free control of X1).
  F1r  X1 continued with c_l free for 1000 iterations.
  W1   X1 continued with extra weight on the x-axis between the origin and P (failed variant).
  X2   X1 continued with c_l held fixed for 20750 further LSQR iterations.
  F2   F1 continued with c_l free for the same 20750 iterations (equal-budget free control of X2).
  X3   X2 enriched to angular cap m <= 200 (the added coefficients start at zero) and continued with c_l fixed for 20750
       iterations on a 20480 x 960 grid.
  F3   F2 enriched to m <= 200 and continued with c_l free for the same 20750 iterations (equal-budget free control
       of X3).
The candidate is X3. Below, "the candidate" means X3 and "its control" means F3.
Conventions. Radii written n L are multiples of the length scale L of the trial formula (4.2; L = 7.6514246 on the
candidate, and each fit has its own L); the shape units of the timeline are the same unit. N_f and N_v are the two
normalizations of the residual (4.4). The verifier's evaluator, also called the separate or the independent evaluator,
is the separately written generator and residual evaluator of 5 (d); the third evaluator is the real-space quadrature of
the velocity of 4.5 (5 (e)); the lead's evaluator is the between-node scan of 5 (c). J is the characteristic defect of
4.4b (its spread over the 857 labels of 4.4b unless stated otherwise), and q0 and I(eps) are its axis profile and axis
integral (4.4b). "The standard" is the evidential standard for YES agreed with the verifier before any candidate
existed: normalized residual maxima between the fit nodes near 1e-6 in both normalizations, including next to P, on both
axes and at 0, recomputed by the verifier's own code; at least three resolutions and three domains, with systematic
improvement under refinement; c_l, x* and h(P) stable, with c_l checked by the identity and by one determination not
using it; far-field truncation and inverse errors quantified separately; J reported and decreasing under refinement.
Absolute values are reported too.

The objective (L2 objective) of a fit is the Euclidean norm of its weighted residual vector on its fit grid: the entries
R/(|rho| + |X.grad rho|) at the grid nodes with 1e-4 L <= r < 900 L (the fit radius; 90 L, 300 L or 9000 L for the
domain columns of 4.4) on every second angle of the grid, each multiplied by (14000/n)^(1/2) max(1, (0.04 L/r)^2), n the
number of these entries, together with 20 (h(P) - 1) and the centre defects E_c and D2 of 4.2 with weight 1. It is a
norm, not a mean square, and its value depends on the fit grid. E without index is the elliptic residual of 4.4.

### 4.1 What is claimed
- There is an explicit trial density rho_h (4.2) and the number c_l = 5.5753626 such that, with the canonical velocity
  law (V1)-(V3), the profile equation holds to a normalized residual of at most 7.2e-7 in the flux normalization N_f
  (6.83e-7 to 7.16e-7 over the three finer configurations of the verifier's evaluator; maximum next to P, 0.07 to the
  left of it and 0.06 to 0.07 above the x-axis) and 1.112e-6 in the second normalization N_v (maximum in the far field
  beyond the inverse domain, next to the y-axis at r about 3.7e4, where the candidate has no fit rows; a domain row
  fitted to 9000 L reads 0.03 of it over 1000 L to 9000 L, 4.5; for r <= 1000 at most 2.01e-7 with the evaluation
  columns next to the y-axis excluded and 2.5e-7 at 16875 x 768 without that exclusion), both defined in 4.4, at the
  sampled points of the plane between the fit nodes, including the neighbourhood of the source point P. The lead's scans
  of 5 (c) read the trial in its fit's own convention (the two-term closure at 1000 L, 4.4); next to P they give 6.94e-7
  and 7.27e-7 in N_f and 1.94e-7 and 2.04e-7 in N_v (32768 x 640 and 24576 x 960), and in that convention the verifier's
  evaluator reads 1 percent above its canonical value there. At the same c_l the residual decreases under refinement of
  the angular cap of the trial space in each quantity of the reading fixed before the runs (4.4: m <= 100, 150, 200; at
  the last step the N_v maximum beyond r = 1000 by about the configuration spread). The rows are not at equal total
  iterations (X3 continues X2 by 20750 iterations, and the m <= 250 row continues X3 by 20750); comparisons at equal
  iterations are in the third item of 4.1 and in 4.4 and 4.8. The m <= 250 refinement row, which is not a candidate,
  meets the same reading on all evaluation columns; with the evaluation columns next to the y-axis excluded it is 0.33
  to 0.74 times X3 in the interior maxima and 0.36 to 0.37 in J, and 0.23 to 0.44 percent above X3 beyond r = 1000, more
  than the spread between configurations (4.4). Fits on two smaller domains and on one with rows to 9000 L are compared
  with the candidate by a rule fixed before the runs (4.4: all three agree except at one configuration, where each is
  lower by more than the rule's factor; none is higher by more than that factor). Read under the canonical law (the
  formula continued, no closure) at equal budget, the fits with rows to 300 L, 900 L and 9000 L agree within 0.5 of P to
  a factor 1.4, and their far band follows the extent of their rows and inverse domains (4.4, 4.5); the 90 L fit is not
  an approximate full-plane profile in that reading (4.4). A separately written evaluator reproduces the residuals, and
  a third evaluator reproduces the velocity at sample points on X1, on a free fit of a smaller basis and on X3 (52, 51
  and 52 points; 4.5). The pair satisfies the identity c_l = (1 + psi_xy(0))/3 to 3.2e-9, and the consistency condition
  h(P) = 1 to the evaluator's grid error (|h(P) - 1| = 2.8e-7, 3.1e-8 and 1.8e-8 at 11250, 16875 and 22500 radial
  points). These results are numerical evidence consistent with the existence of an exact profile of P_2 near rho_h.
  They do not establish the proximity of an exact profile or determine its exponent: if such a profile exists and is
  isolated (4.8), its exponent may lie outside the tested span of (iv). It is not a proof.
- The free control at the same LSQR budget, from the free start, has c_l = 5.5763712. On X3 against F3 the candidate is
  lower in whole-box N_f on every configuration (ratio 0.937, 0.935 and 0.938 at 16875 x 512, 16875 x 768 and 22500 x
  512 with the y-axis floor columns excluded; 0.83 at 16875 x 768 without that exclusion, where F3's maximum sits in the
  floor column at r 9.5; next to P 0.935 to 0.938 on all four configurations), lower in N_v for r <= 1000 (ratio 0.935
  to 0.987 with the same floor columns excluded; 0.825 at 16875 x 768 without that exclusion), lower in the 857-label
  characteristic defect J (ratio 0.937 at eps 0.03 and 0.01), and lower in the L2 objective on the fit grid (1.619e-6
  against 1.664e-6, a ratio between 0.960 and 0.973 at every check point of the two runs). In the far field beyond r
  1000 the two agree to 3e-9 (ratio 1.000 to 1.003, the candidate the higher), inside the spread of 2.4e-8 of F3's
  values between configurations; with the y-axis floor columns excluded the candidate is the higher by 4.5e-9 (0.4
  percent) on each configuration with 16875 or more radial points, about twice the spread between those configurations
  (the same offset in favour of the free c_l as in the m <= 250 pair of 4.4). The ratios X3 / F3 are thus 0.935 to 0.938
  in whole-box N_f, 0.937 in J, 0.935 to 0.987 in N_v for r <= 1000, 0.960 to 0.973 in the L2 objective and 1.000 to
  1.003 in the far field, where there is no margin. They are read at one budget and one basis; they are what the
  selection rule reads, not a determination of c_l.
- Raising the angular cap from 150 to 200 at the fixed c_l, with 20750 further iterations, lowered whole-box N_f by
  0.475 to 0.485 (X2: 1.42e-6 to 1.51e-6), N_v for r <= 1000 by 0.48 and J by 0.44; N_v on the outer part of the inverse
  domain (1000 <= r <= 7652, that is 1000 L) by 0.86 only (2.152e-7 against 2.513e-7); the near-P window y >= 1 of 4.4
  changed by the ratios 1.01 (11250 x 384, the under-resolved lobe of 4.3) and 0.81 (16875 x 512); beyond r 1000 L the
  formula's far field reads 1 to 2 percent lower. At equal budget (one linearization of 2500 iterations from X2 on each
  basis) the m <= 200 iterate is 0.71 to 0.72 times the m <= 150 iterate in N_f and 0.62 to 0.69 in J on 185 labels
  (every fourth label of family A of 4.4b); the m <= 150 iterate is 0.999 times X2 in N_f. The two equal-budget runs
  also differ in the number of collocation angles (960 against 720), so the gain is attributed to the m <= 200 setup
  (basis and grid together).
- The candidate is not the fit with the lowest whole-box N_f at every configuration. Rows continued beyond its budget
  are lower in whole-box N_f (columns within 0.006 of the y-axis excluded, as in 4.4) at the configurations read with at
  least 16875 radial points: the budget row and X3 continued with the inverse domain at 1e4 L (4.2, 4.5), the m <= 250
  row, its free control and its continuation with rows to 9000 L (4.4), and the 9000 L row, its free control and its
  continuation (4.4, 4.5); none of these is an equal-budget comparison. X1, the fixed-c_l fit before the long
  continuation, has its maximum next to P 4 to 6 percent below the candidate's at 16875 radial points (6.53e-7 against
  6.84e-7 at 512 angles, 6.70e-7 against 7.16e-7 at 768 angles), equal to it at 22500 x 512 and 2 percent above it at
  11250 x 384; its N_v for r <= 1000 is 2.8 times and its 857-label J twice the candidate's (2.74e-6 against 1.39e-6),
  and it fails the selection rule against its own equal-budget free control on J. All fits compared are listed in 4.3.
  The fixed-c_l fit at 5.5683739 (4.3), not a candidate by the rule fixed before that profile, has whole-box N_f 0.984
  times the candidate's and N_f within 0.5 of P 0.977 times at 16875 x 512, N_v for r <= 1000 1.038 times, and J (at
  16875 x 384) 0.954 (eps 0.03) and 0.882 (eps 0.01) times; at 11250 x 384 its whole-box maximum is 1.289 times the
  candidate's (both at the under-resolved off-axis lobe; within 0.5 of P 1.005 times). The bases differ, so this is a
  fact about two fits. On the candidate's basis, at the candidate's iteration count (the nested pair of 4.3), the fit at
  5.5683739 has a smaller L2 objective (0.820 times the candidate's), a smaller N_f within 0.5 of P (0.591 and 0.588
  times at 11250 x 384 and 16875 x 512) and a smaller J (0.562 at eps 0.03, 0.545 at eps 0.01) than the candidate; its
  whole-box N_f is 1.322 times the candidate's at 11250 x 384, at the off-axis lobe point that grid under-resolves, and
  0.691 times at 16875 x 512. The fixed-c_l fit at 5.5604082 on the m <= 150 basis continued to 43000 iterations (4.3),
  not a candidate, has whole-box N_f 0.922 times the candidate's at 16875 x 512 (at the off-axis lobe), N_f within 0.5
  of P 0.750 times, N_v for r <= 1000 0.924 times, and J (at 16875 x 384) 0.800 (eps 0.03) and 0.774 (eps 0.01) times;
  at 11250 x 384 its whole-box maximum is 1.689 times the candidate's, at the under-resolved off-axis lobe (within 0.5
  of P 0.823 times). It is not an equal-budget comparison. The residual does not distinguish the candidate's exponent or
  basis among the fits computed.
- The evidence concerns P_2. With the common global regularity of section 1, P_inf is contained in P_2, so numerical
  evidence for P_2 does not by itself establish a profile of P_inf (nor does it show that an exact profile near the
  trial fails to be in P_inf; (ii) gives numerical evidence on that, not a proof). Every trial satisfies the
  requirements of P_2 other than the equation: rho = x^2 y exp(H) with H(0) = 0. The integer angular spline terms of H
  are C^(6,1)_loc on the plane (polynomial degree 7 with simple interior knots) and analytic near 0 within the first
  knot interval (4.2). The fractional-power term is |x|^(p_3 - 2) y^2 (L^2 + r^2)^(-p_3/2) T(2q - 1) in Cartesian form.
  It makes H and a exactly C^(4,beta)_loc, with beta = p_3 - 6 = 2/(2 c_l - 1) = 0.19703 on the candidate, and the
  factor x^2 y makes rho_h exactly C^(6,beta)_loc (the least regular term of rho_h is |x|^(p_3) times a smooth factor;
  exact because T is not identically zero).
- Remark (structure, not part of the class). R7 and R10 identify, under their differentiability and finite-part
  hypotheses, a possible fractional homogeneous contribution B_3 |x|^(p_3) (times a smooth factor) to the axis
  coefficient G_3 = d_y^3 rho(x,0)/6, with B_3 an exact functional of the axis velocity w on [0, x*] (R10). No
  two-dimensional expansion of a is asserted. Evaluated on the computed trials by the original form of R10 and by the
  two forms of the independent evaluator's estimator, B_3 = 0.299 to 0.303 on the candidate (medians over the four
  evaluation configurations; the original form of R10 gives median 0.3027, range 0.3010 to 0.3040 over 16 quadrature and
  fit-window variants; the extremes over all variants of the three forms are 0.291 and 0.311) and 0.298 to 0.303 on its
  control. On the angular row of 4.4 (m <= 100, 150, 200, 250 on 375 radial functions), on X3 continued for a further
  20750 iterations and on the domain row with fit rows to 9000 L, the medians of the independent evaluator's
  integration-by-parts form are 0.2985, 0.2992, 0.2996, 0.3012, 0.3000 and 0.2998 and those of its original form
  0.3002, 0.3021, 0.3029, 0.3044, 0.3037 and 0.3032 (method spread within one row up to 0.0035 and 0.015); along the
  angular row each step is within the method spread. Over 136 evaluations of earlier fits by the independent evaluator,
  with c_l from 5.5752 to 5.6001, radial bases from 200 to 375 functions and angular caps 100 to 200, the medians of its
  integration-by-parts form lie between 0.296 and 0.302 and those of the original form of R10 between 0.277 and 0.311;
  every variant is positive (smallest single value 0.151). On earlier fits the value is unchanged when the trial's
  fractional-power functions are switched off and when the centre jet is repaired. A further form, an integration by
  parts with an end piece in closed form, is not quoted: its end piece does not converge in the quadrature order. The
  sign of dB_3/dc_l is not resolved by these values.
  The trial's own coefficient is a second measurement. The fractional-power term of 4.2 contributes
  T(-1) L^(-p_3) y^3 |x|^(p_3) to rho_h at the origin (T(-1) the value of its Chebyshev factor at q = 0), with T(-1) =
  1.6487 to 1.6488 on the candidate, on X2 and on the rows of 4.4 built from them (1.6485 on F3 and on the free control
  of the m <= 250 row): 5.50e-6, or +0.046 in the natural units above. For a trial, the original form of R10 evaluated
  on its axis data equals its own coefficient plus the finite part of int_0^{x*} (T_3 - (3 + beta) (G_3/g) T_1)/(w H)
  dx, with H as in R10 and T_1 = w g' + (h - 1) g, T_3 = w G_3' + (3h - 1) G_3 + a2 g' + b3 g the trial's defects in the
  y and y^3 coefficients of the equation on the x-axis (variation of constants in the G_3 equation; w' + h = 2c_l and
  a2' + 3 b3 = 0 hold for every trial since div U = 0; the finite-part step uses g > 0 on (0, x*] and even expansions
  of g/x^2 and |w|/x at 0, which these trials have; for a profile T_1 = T_3 = 0 and H is the homogeneous solution).
  So the difference, about +0.25, is carried by these defect terms; both measurements are positive. This is an estimator
  value on approximate profiles; B_3 of an exact profile is indicated, not proved.

### 4.2 Candidate
The trial density is given by an explicit formula with stored coefficients (accompanying artifacts). With u = r/L,
q = 1 - (1 + u^2)^(-(1-k)/2) and chi = u^2/(u^2 + r_0^2), r_0 = 0.02,
   rho_h = x^2 y exp(H),
   H = ((k - 3)/2) log(1 + u^2) + sum_{m=0}^{M} chi^max(m-1,0) b_m(q) cos(2 m theta)
       + (u^2/(1 + u^2))^(p_3/2) |cos(theta)|^(p_3 - 2) sin(theta)^2 T(2q - 1),
with M = 200, where b_m are clamped splines of polynomial degree 7 in q on [0, 1] with b_m(0) = 0 (375 coefficients
each; simple interior knots, spacing 0.0165 in r next to P, 6.3e-4 in q), T is a Chebyshev polynomial of degree 5,
p_3 = 6 + 2/(2 c_l - 1), and k = 1/c_l. Hence H(0) = 0, so a(0) = 1 exactly; rho_h is even in x and odd in y by
construction, so its psi under the canonical inverse is odd in x and in y, and U_1 = 0 on the y-axis, U_2 = 0 on the
x-axis and U(0) = 0 by these parities; each angular term is analytic near 0, within the first knot interval, because
there b_m(q(u^2))/u^2 is analytic in u^2 and r^(2m) cos(2 m theta) is a polynomial.
  - c_l = 5.5753626 (held fixed during the fit; 5.575362610641546 to all stored digits); k = 0.17936053; L = 7.6514246.
  - Far field. Since b_m is a polynomial near q = 1 and 1 - q = (1 + u^2)^(-(1-k)/2),
      rho_h = r^k Theta_0(theta) (1 + r^(k-1) Theta_1(theta) + O(r^(2k-2))),
    Theta_0(theta) = L^(3-k) cos(theta)^2 sin(theta) exp(sum_m b_m(1) cos(2 m theta) + T(1) sin(theta)^2
    |cos(theta)|^(p_3-2)), and Theta_1(theta) = -L^(1-k) (sum_m b_m'(1) cos(2 m theta) + 2 T'(1) sin(theta)^2
    |cos(theta)|^(p_3-2)) (b_m' with respect to q, T' with respect to its argument). The bracket extends continuously
    across the axes and the remainder is O(r^(2k-2)) uniformly in theta (the O(r^(-2)) terms from chi, (1 +
    u^2)^((k-3)/2) and (u^2/(1 + u^2))^(p_3/2) are smaller, since 2k - 2 = -1.64 > -2). The leading term is homogeneous
    of degree 1/c_l, the largest growth that the bound |rho| <= C (1 + |X|)^(1/c_l) of R2 allows, and the first
    correction is relative r^(k-1). This is the far-field model. The fit's residual rows are r < 900 L; its own inverse
    is computed on the inverse domain r <= 1000 L with the density replaced beyond it by its two-term exterior extension
    (the two-term closure); the residual at larger r is evaluated from the formula (4.5). In q the last interior knot of
    the radial splines is at r = 446 L, so on r > 446 L each b_m is one polynomial of degree 7 in q; the fit rows cover
    the first 44 percent of that knot interval in q, and the formula beyond 900 L (in particular the far-field band of
    4.5, at 86 percent of the interval) is the unfitted continuation of that polynomial, with b_m(1) and b_m'(1) its
    values at the end.
  - Source point: x* = 8.600064 (lead 8.6000638; independent evaluator's zero of W_1 on the x-axis 8.6000635). h(P) - 1
    is at the evaluator's grid error (2.84e-7, 3.11e-8 and -1.78e-8 at 11250, 16875 and 22500 radial points; lead
    evaluation -8.8e-9 / -5.3e-9 on its two grids). On the evaluation grid there is no further zero of W in the closed
    first quadrant: W_1 on the x-axis vanishes only at x*, W_2/y on the y-axis is at least 5.5756 (attained at y 7.5e6,
    where it tends to c_l), and no cell of the open quadrant has both components changing sign (a sampled check, not a
    validated exclusion); min |W| / (c_l |X|) is 0.0216, 0.0065, 0.0026 at |X - P| = 1, 0.3, 0.1.
  - Centre jet. With a = 1 + delta x^2 + gamma y^2 + O(r^4) and psi = c x y + alpha x y^3 + beta x^3 y + O(r^6),
    the x^4 y and x^2 y^3 coefficients of W.grad rho - rho are the centre defects E_c = beta - 2 (2 c_l - 1) delta
    and D2 = (8 c_l - 2) gamma - 5 alpha, which vanish for a profile; the relative defects are E_c/|beta| and
    D2/(5 |alpha|), with delta and gamma fitted on a window of r. They are at most 6e-9 on the candidate and on
    its control for every fit window inside r <= 0.1 (independent evaluator; windows [1e-3, 0.02] to [5e-3, 0.1];
    the values depend on the window at that level); on X2 at most 8.5e-9 for windows up to r 0.05 and 1.9e-8 on
    [5e-3, 0.1].
  - How it was obtained. F0 (Gauss-Newton with LSQR inner solves on a 20480 x 720 polar grid, c_l from the identity) was
    moved along its softest exponent direction by -1e-3 in c_l and refitted with c_l held fixed (X1, 750 LSQR iterations
    over two linearizations, objective 9.71e-6 to 8.47e-6), then continued at the fixed c_l by a GPU implementation of
    the same LSQR iteration (linearizations of 2500 iterations, damping 1e-8) for 20750 iterations to X2 (objective
    4.097e-6 on the fit grid). X3 is X2 enriched to M = 200 (the new coefficients start at zero, so the start is X2
    itself), continued at the fixed c_l by the same iteration for 20750 iterations on a 20480 x 960 grid: objective
    1.619e-6 on that grid against 4.050e-6 for X2 on the same rows. The objective still fell by about 2 percent per
    linearization at the end. X3 continued at the fixed c_l on its own rows and basis for a further 20750 iterations (a
    budget row, not a candidate) reaches 1.264e-6 on the same grid (0.781 of X3's) and, at 16875 and 22500 radial points
    with the columns next to the y-axis excluded, reads 0.61 to 0.74 times X3's whole-box N_f (its maximum moves from
    next to P to the lobe above P (4.4), where it equals X3's value there to 2.4 percent over four radial sampling
    phases), 0.50 to 0.54 within 0.5 of P, 0.64 to 0.77 in N_v for r <= 1000, 0.99 to 1.01 for r > 1000 and 0.48 (eps
    0.03) and 0.45 (eps 0.01) in J; its centre values are X3's. So X3 is limited by the iteration budget, except beyond
    r = 1000. Every shape is measured by the CPU evaluators of 4.4 and 4.5, not by the GPU code. Solver setting: plain
    damping 1e-8 was kept by a rule fixed before the test (a variant replaces it only if its objective after 2500
    iterations is at least 3 percent lower and its maximum next to P is not higher); damping 1e-12 gave the same
    objective to 6 digits, and reorthogonalization gave 1.3 percent, so neither change of the solver setting lowers the
    objective materially at this budget.

### 4.3 The exponent c_l and the choice of the candidate
Identity on the candidate. The verifier computed c = psi_xy(0) from the density, generated from the formula by its own
code, by its own inverse: (1 + c)/3 = 5.575362607 on every configuration (5.5753626074 at 16875 and 22500 radial points)
against the fixed value 5.5753626106 (difference -3.2e-9). For a fit with c_l held fixed this tests the fit: c_l enters
the transport equation, and psi_xy(0) is computed from rho. Holding c_l fixed does not suspend the identity. With
a(0) = 1 fixed, the fit has to find a density, its length scale L and its shape, whose own psi_xy(0) equals 3 c_l - 1,
and the final pair satisfies the identity to 3.2e-9. What is chosen, and stated here, is the point at which the family
of consistent pairs is sampled. The prompt's condition that c_l is not chosen independently is met in the sense that c_l
and the psi_xy(0) of rho agree; the choice of the sample point is disclosed. The identity-free condition h(P) = 1 avoids
the origin identity but is not an independent test of transport near P: it is the source limit of the normalized
transport equation (4.4a), so a small normalized residual approaching P implies it. Solved for c_l with rho fixed,
h(P) = 1 gives 7.0e-9 above the identity value on X3 (dh/dc_l = 1.079) and 6.3e-8 above it on F3 (identity value
5.576371152, 3e-9 from the stored 5.576371155); on X2 / F2 4.7e-9 below and 4.2e-8 above. It holds at both values, 1e-3
apart, and does not determine c_l at that level. It is a consistency test along the soft direction.

Selection rules. (1) Of each equal-budget pair (fixed c_l against the free control from the free start, same LSQR
count), the fixed fit is kept if its whole-box N_f is lower, its N_v (for r <= 1000 and in the far field separately) is
not higher by more than the spread between the verifier's configurations, and its 857-label J is not higher; otherwise
the free fit is kept.
(2) The candidate is the kept fit with the lowest whole-box N_f, all maxima taken at the same verifier configurations.
(3) The far-field band of rule (1) is all r > 1000 on the verifier's evaluator. Rule (1) was fixed before any residual
scan of X2 or F2 (the L2 objective of X2 after 2000 iterations, 4.993e-6, was known). Rules (2) and (3) were fixed after
the X2/F2 measurements (the earlier wording of (1) did not say where the band ends) and before any residual scan of X3
or F3 (the L2 objective of X3 at iterations 250 to 1000 was known). Read over the band
1000 <= r <= 7652 (that is 1000 L) only, X2's N_v is 2.9 to 3.1 percent higher than F2's (7.2e-9 to 7.5e-9 against a
spread of 2e-10), and by that reading F2 would be kept. Both readings are given here; the outcome of the X2/F2 pair
depends on it. For X3/F3 the two readings agree (that band: X3 2.152e-7 / 2.183e-7, F3 2.157e-7 / 2.195e-7). The reading
of whole-box N_f on the configurations with 16875 or more radial points was fixed by the verifier before any F3 row
existed: at 11250 radial points an off-axis lobe near (8.4, 2.7) (r 8.78, theta 0.31; not the lobe above P of 4.4) is
under-resolved (the residual there oscillates in r with period 0.036, two grid points per period) and pins the whole-box
value at 6.8e-7 to 7.0e-7 on every fit below that level.

Every fit compared by the selection rules (verifier maxima; configurations as stated; L2 objective on the fit grid):
     fit   c_l        cap    LSQR budget            L2          whole-box N_f        N_v r <= 1000      N_v r > 1000       J (857, eps 0.03)
     F0    5.5763624  150    start                  7.65e-6     2.28e-6 to 2.44e-6   6.4e-7 to 6.8e-7   1.12e-6 to 1.15e-6 3.85e-6
     X1    5.5753626  150    750                    8.47e-6     6.5e-7 to 7.0e-7     5.20e-7, 5.32e-7   1.13e-6, 1.15e-6   2.74e-6
     F1    5.5763640  150    750                    7.08e-6     2.09e-6, 2.22e-6     5.90e-7, 6.27e-7   1.46e-6, 1.47e-6   2.27e-6
     F1r   5.5753651  150    X1 + 1000 (free)       7.47e-6     1.04e-6, 1.02e-6     4.26e-7, 4.43e-7   1.09e-6, 1.10e-6   2.24e-6
     W1    5.5753626  150    X1 + reweighted        -           4.5e-6, 5.0e-6 (*)   1.31e-6, 1.45e-6 (box)               -
     X2    5.5753626  150    X1 + 20750             4.097e-6    1.42e-6 to 1.51e-6   3.98e-7 to 4.20e-7 1.10e-6 to 1.13e-6 3.14e-6
     F2    5.5763709  150    F1 + 20750 (free)      4.259e-6    1.57e-6 to 1.64e-6   4.39e-7 to 4.59e-7 1.10e-6 to 1.13e-6 3.41e-6
     X3    5.5753626  200    X2 + 20750             1.619e-6 +  6.83e-7 to 7.16e-7   1.91e-7 to 2.01e-7 1.09e-6 to 1.11e-6 1.39e-6
     F3    5.5763712  200    F2 + 20750 (free)      1.664e-6 +  7.28e-7 to 7.65e-7   1.95e-7 to 2.14e-7 1.09e-6 to 1.11e-6 1.48e-6
  Configurations: F0 over six configurations (11250 x 384, 16875 x 384, 512 and 768, 22500 x 384 and 512; radial x
  angular points); X1, F1, F1r, W1 at 11250 x 384 and 16875 x 512; X2, F2 also at 16875 x 768; X3, F3 at 16875 x 512,
  16875 x 768 and 22500 x 512 for whole-box N_f and at all four configurations of 4.4 otherwise. J is computed at
  16875 x 384 on every fit.
  Whole-box N_f and N_v for r <= 1000 exclude the evaluation columns next to the y-axis (pi/2 - theta < 0.006), where
  the evaluator's value is a cancellation floor; at 16875 x 768 that column holds 8.60e-7 on F3 (r 9.5) and 5.1e-7 on X3
  (r 10 to 100). N_v for r > 1000 is read on all columns.
  (*) W1's maximum sits on the first angle off the x-axis and grows as that angle shrinks: lower bounds of an axis
  limit. (+) on the 20480 x 960 fit grid of the m <= 200 runs (X2 reads 4.050e-6 there); the other L2 values are on
  20480 x 720. Fixed c_l values tried: 5.60 on a 244-function basis (3 h fixed, then 1500 iterations free: c_l moved by
  -8.6e-6; near-P N_f 6.5e-6 against 3.2e-6 for the free fit of that basis; undecided at that level); on the candidate's
  radial basis with angular cap m <= 150, the profile below.
Fixed-c_l profile (375 x m <= 150). Each row starts from F0 moved along the direction of X1 by d in c_l and holds c_l at
the value stored with that start, which is 5.5763624 + d + 0.18 d^2 to within 8e-7 (the table quotes the stored values);
it then runs 21500 LSQR iterations, the budget of F2 (750 + 20750), on the fit grid 20480 x 720. F2, the free fit of the
same lineage, basis, grid and budget, is the reference. Verifier values: L2 objective on the fit grid; whole-box N_f at
11250 x 384 and 16875 x 512 (columns next to the y-axis excluded as above); J at 16875 x 384; ratio to F2 in brackets.
     c_l        d        L2                   whole-box N_f                     J (857, eps 0.03)    reading
     5.5524653  -2.4e-2  3.301e-6 (0.775)     1.792e-6, 1.825e-6 (1.139, 1.159) 3.953e-6 (1.158)     undecided
     5.5604082  -1.6e-2  2.738e-6 (0.643)     1.127e-6, 7.630e-7 (0.716, 0.485) 1.754e-6 (0.514)     undecided
     5.5683739  -8e-3    3.157e-6 (0.741)     8.906e-7, 6.730e-7 (0.566, 0.427) 1.324e-6 (0.388)     undecided
     5.5723653  -4e-3    3.654e-6 (0.858)     1.119e-6, 1.123e-6 (0.711, 0.713) 2.412e-6 (0.707)     not determined
     5.5743631  -2e-3    3.945e-6 (0.926)     1.362e-6, 1.368e-6 (0.865, 0.869) 2.953e-6 (0.865)     not determined
     5.5753626  X2       4.097e-6 (0.962)     1.424e-6, 1.435e-6 (0.905, 0.911) 3.143e-6 (0.921)     (X2, table above)
     5.5763709  F2       4.259e-6             1.574e-6, 1.575e-6                3.414e-6             reference
     5.5783631  +2e-3    4.591e-6 (1.078)     1.791e-6, 1.792e-6 (1.138, 1.138) 3.956e-6 (1.159)     not determined
     5.5793640  +3e-3    4.748e-6 (1.115)     1.909e-6, 1.911e-6 (1.213, 1.214) 4.180e-6 (1.224)     not determined
     5.6004662  +2.4e-2  8.671e-6 (2.036)     4.587e-6, 4.590e-6 (2.915, 2.914) 9.800e-6 (2.871)     excluded
  Reading rule, fixed before these runs: "not determined at this level" if the L2 objective and the whole-box N_f on
  each configuration are within 30 percent of F2's and |h(P) - 1| <= 1e-6; "excluded at this level" if the fit has
  flattened (its objective changes by less than 2 percent over its last 1000 iterations) and its N_f maximum within 0.5
  of P is at least twice F2's on each configuration; "undecided" otherwise. At 16875 x 512 the whole-box maximum of N_f
  lies within 0.5 of P on every row except d = -8e-3, where it is 0.57 left of P on the x-axis side (0.7 percent above
  the maximum within 0.5 of P); at 11250 x 384 it is at the under-resolved off-axis lobe described above at d = -8e-3
  and d = -1.6e-2, and within 0.5 of P on the other rows. On every row N_v for r <= 1000 has, to within 0.03, the same
  ratio to F2's as the whole-box N_f on the same configuration. On every row the identity c_l = (1 + psi_xy(0))/3 holds
  to 3.2e-9. On the rows not excluded |h(P) - 1| is at most 6.9e-7 except at 5.5524653, where it is 1.46e-6 at
  11250 x 384, 2.6e-7 at 16875 x 512 and 6.3e-9 at 22500 x 384 (it falls with the radial resolution of the evaluation,
  as on the candidate); by the 11250 x 384 value that row reads "undecided", and with h(P) taken at 16875 or more radial
  points "not determined". On the excluded row it is 1.07e-6 and 2.45e-7. At equal budget the L2 objective increases
  with c_l from 5.5604082 up, near F2 by about 4 percent per 1e-3 in c_l, and is larger at 5.5524653 than at 5.5604082;
  the whole-box N_f and J increase with c_l from 5.5683739 up and fall faster than the objective from F2 down to
  5.5683739, and they are larger at 5.5604082 and larger again at 5.5524653 (whole-box N_f 0.427, 0.485 and 1.159 of
  F2's at 16875 x 512 at 5.5683739, 5.5604082 and 5.5524653; J 0.388, 0.514 and 1.158). Among the tested rows the L2
  objective is least at 5.5604082 and the residual maxima at 5.5683739. At 5.5524653 the L2 objective is below F2's
  while the residual maxima are above F2's; that fit had not flattened (its objective fell by 2.5 percent over its last
  1000 iterations; at that rate, assumed constant, it would need about 7400 more iterations to reach the objective at
  5.5604082). So every fixed-c_l fit below F2's exponent reaches a lower L2 objective than F2 at the same budget, while
  along the 20750 iterations from F1 to F2 the free c_l stays between 5.5763641 and 5.5763716 (F0: 5.5763624): at this
  budget F2's exponent is set by its start, not by a minimum of the objective; "free branch" in this report names the
  fits with c_l free, not a selected exponent. These are fits from transplanted starts at one budget; they do not locate
  an exponent or a minimum of an objective over c_l. Continued for a further 21500 iterations at their exponents (43000
  in all), the fits at 5.5604082 and 5.5524653 reach L2 objectives 2.2009e-6 and 2.2121e-6 (ratio 1.005) and whole-box
  N_f 1.167e-6 and 1.344e-6 at 11250 x 384 and 6.311e-7 and 1.301e-6 at 16875 x 512, their objectives changing by -0.148
  and -0.338 percent over the last 1000 iterations; by the rule fixed before these runs the bracket is kept at twice the
  budget. Neither continuation is at equal budget with F2 and both may still be falling, so this too concerns fits from
  transplanted starts at a stated budget, not where the objective minimized over shapes at fixed c_l has its minimum
  over c_l. The L2 gap between them fell at every linearization of the continuation, from 5.63e-7 at its start to
  1.12e-8 at its end; each of the four complete linearizations before the last reduced it by more than the 1.12e-8 that
  remains (the last, of 1500 iterations, by 5.9e-9), so the order in L2 is a fact at this budget only.
Nested pair (375 x m <= 200). The rows at 5.6004662 and 5.5683739 continued from their ends on m <= 150 to the
candidate's angular cap as X2 was continued to X3 (c_l held at the stored value, 20750 LSQR iterations on 20480 x 960);
F3, the free fit of that basis at the same budget, is the reference. Verifier values as in the profile above (whole-box
N_f at 11250 x 384 and 16875 x 512, J at 16875 x 384), ratios in brackets.
     c_l        L2 (to F3, to X3)           whole-box N_f (to F3)             J (to F3)            reading
     5.6004662  2.795e-6 (1.680, 1.726)     1.676e-6, 1.825e-6 (2.412, 2.499) 3.612e-6 (2.439)     excluded
     5.5683739  1.328e-6 (0.798, 0.820)     9.132e-7, 4.725e-7 (1.315, 0.647) 7.807e-7 (0.527)     undecided
     5.5753626  1.619e-6 (0.973, 1)         6.909e-7, 6.841e-7 (0.995, 0.937) 1.388e-6 (0.937)     (candidate)
     5.5763712  1.664e-6 (1, 1.028)         6.947e-7, 7.303e-7 (1, 1)         1.481e-6 (1)         reference
  Rule, fixed before these runs: the reading rule of the profile, against F3, for the interval (the reading column); for
  the fit at 5.6004662 the ratio Q of its objective to F3's (4.8). The objective changed by -0.96 percent over the last
  1000 iterations at 5.6004662 and by -0.61 percent at 5.5683739. |h(P) - 1| is at most 7.72e-7 on both fits and both
  configurations, and the identity c_l = (1 + psi_xy(0))/3 holds on both to 3.3e-9. The N_f maximum within 0.5 of P is
  2.412 and 2.499 times F3's at 5.6004662, where both whole-box maxima lie, and 0.554 and 0.551 times F3's (0.591 and
  0.588 times X3's) at 5.5683739, whose whole-box maxima on both configurations are at the off-axis lobe point described
  above (r 8.78, theta 0.30), which the 11250-point radial grid under-resolves.
Reading. Rule (1) keeps X1 against F1 in N_f and N_v but not in J (2.74e-6 against 2.27e-6), so X1 is not kept; X2 is
kept against F2 with the far band read as all r > 1000 (both readings in the paragraph above); X3 is kept against F3
(whole-box N_f 0.94, N_v for r <= 1000 0.94 to 0.99, far field within 3e-9, J 0.94). Rule (2) gives X3: its whole-box
N_f is lower than X2's by a factor 2.1 on every common configuration. F1r is a free continuation without an equal-budget
control and is listed, not ranked. Along the continuation X1 to X2 the L2 objective halves and the near-P maximum
doubles: the residual at the angular cap frequency of the basis (2 M = 300) moves from r 4 to 7.6 toward r 7 to 8.6 and
above P, where the small transport terms near the stagnation point divide it. Along F1 to F2 the L2 objective falls by
40 percent and the near-P maximum falls from 2.1e-6 to 2.3e-6 (range over the configurations) down to 1.6e-6, with the
cap-frequency residual at the same place as on X2. On the m <= 150 basis the long continuation lowered the maximum
residual on the free branch (F1 to F2) and raised it at the fixed c_l (X1 to X2). With the cap raised to 200 the
cap-frequency residual next to the x-axis (r 7.0 to 8.3) moves to angular frequencies 400 to 600 (about 2 M) and is 3.4
times lower at r 8.3; every window near P of 4.4 except y >= 1 falls by a factor 2.1 to 2.5, and the window y >= 1 rises
by 1 percent at 11250 x 384 (the under-resolved off-axis lobe near (8.4, 2.7) described above) and falls by a factor
1.23 at 16875 x 512. Since the minimum is taken over several fits, it is a selection; the table lists the fits compared
by the rules. Not in the table: the budget row (X3 continued on its own rows, 4.2 and 4.4), X3 continued on its own rows
with the inverse domain at 1e4 L (4.5), the m <= 250 refinement row and its free control and the domain columns (4.4),
the free control of the 9000 L row and its continuation (4.5), the m <= 250 row continued with rows to 9000 L (4.4),
none a candidate; the equal-budget m <= 150 iterate of 4.1, the solver-setting arms of 4.2 (damping 1e-12,
reorthogonalization) and the 244-function fit at c_l 5.60 below.

Interval. The quoted interval contains the c_l of the candidate and of its control and every c_l tested on the
candidate's radial basis with angular cap m <= 150 that the rule of the fixed-c_l profile does not exclude at the
attained level (5.5524653 to 5.5793640); 5.6004662 is excluded at that level, and so is its continuation to m <= 200
(the nested pair above: N_f within 0.5 of P 2.412 and 2.499 times F3's). The interval is quoted on the candidate's
radial basis; the 244-function fit at 5.60 (below) is undecided on its smaller basis.
Fits of comparable residual quality exist at c_l values 1e-3 apart, and the free continuations listed here move c_l by
at most 6.9e-6 at these budgets, under 1 percent of that separation (F2: +6.9e-6 in 20750 iterations, F3: +2.2e-7 in
20750, the free control of the m <= 250 row: -6.0e-7 in 20750, the free control of the 9000 L row of 4.5: -1.5e-6 in
20750, F1r: +2.5e-6 in 1000; F1r, started from the fixed value, moves toward the free branch, F2 and F3 away from the
fixed value, and the free controls of the m <= 250 row and of the 9000 L row toward it). This spread measures how weakly
the residual pins c_l; it is not an uncertainty interval for an exact profile, and the available diagnostics do not
calibrate the absolute exponent error. Earlier measurements on smaller bases: the least first-order cost of a unit
change of c_l on the 244-function basis is at most 3.6e-3 of the objective (still falling); the 244- and 302-function
trials moved along the soft direction stay within 30 percent of their fits in every diagnostic at -1e-3; the
244-function fit with c_l held at 5.60 reached 1.97 times the objective of the free fit in 3 h and was still falling;
continued for 1500 further LSQR iterations in the free formulation it kept c_l (5.5999914, a change of -8.6e-6) and
reached 1.36 times (falling 1.6 percent in the last 250 iterations); on the independent evaluator its residual is 2.0
times that of the free fit on that basis next to P, 1.3 to 1.4 times in the whole box and at 10 <= r <= 100, and its J
2.1 times, which is undecided at that level. The independent discretization (4.6) has fixed-c_l states over 5.52 to
5.71; those from 5.556 to 5.596 include both values and do not discriminate between them.

### 4.4 Residual tables
Normalizations. R = W.grad rho - rho with W = c_l X + U. N_f = |W_1 rho_x| + |W_2 rho_y| + |rho| (flux normalization;
it vanishes with W at P, so it is the stricter one next to P) and N_v = |rho| + |X.grad rho| + |U.grad rho| (stricter in
the far field). Every residual below is a maximum of |R|/N over a between-node grid of the verifier's evaluator (its own
generator of rho from the formula, its own inverse to R = 7.652e6), not over fit nodes. Configurations of the
independent evaluator: radial x angular points 11250 x 384, 16875 x 512, 16875 x 768, 22500 x 512 (log-radial points on
r in [7.652e-4, 7.652e6], angular points on the quarter, between fit nodes).

The candidate by region (N_f maxima at 11250 x 384 / 16875 x 512 unless stated; the columns next to the y-axis excluded
where stated):
     |X - P| < 0.5                         6.51e-7 / 6.84e-7 (X2: 1.42e-6 / 1.43e-6)
     strip y < 0.2, 6 <= x < 8.1           5.35e-7 / 5.56e-7
     y < 0.2, x > x*                       2.70e-7 / 1.83e-7
     y 0.2 to 1, |x - x*| < 1              5.34e-7 / 5.68e-7
     y >= 1                                6.91e-7 (under-resolved lobe at 11250 radial points, 4.3) / 4.32e-7
     r <= 0.1                              N_f 4.95e-9, N_v 1.07e-8 (*)
     0.1 <= r <= 2                         N_f 2.48e-8, N_v 4.83e-8 (*)
     2 <= r <= 10                          whole-box N_f maximum (the rows above)
     10 <= r <= 100                        N_f 8.66e-8, N_v 7.10e-8 (*)
     100 <= r <= 1000                      N_f 1.50e-8 to 1.60e-8 (the four configurations), N_v 6.49e-8 (*)
     r <= 1000, N_v                        1.92e-7, 1.92e-7, 2.01e-7, 1.91e-7 (the four configurations; y-axis columns
                                           excluded at 16875 x 768; 2.49e-7 there without that exclusion)
     1000 <= r <= 7652 (= 1000 L)          N_v 2.15e-7 / 2.18e-7 (at r 7647, theta 1.554, on the first; past the fit rows)
     r > 1000 L (formula beyond the fit)   N_v 1.090e-6, 1.101e-6, 1.111e-6, 1.103e-6 (next to the y-axis, r 3.61e4 to
                                           3.72e4); N_f 1.320e-7 to 1.323e-7 (r 3.3e4, theta 0.84)
  (*) 16875 x 512 with the evaluation columns next to the y-axis excluded (pi/2 - theta < 0.006). These maxima sit on
  the first column outside the cut and may still contain part of the evaluator's floor, so they may be raised by that
  floor; they are not floor-free values. Without the exclusion the N_f maxima lie in the floor column on almost every
  configuration: 1.45e-8 to 1.15e-7 for r <= 0.1, 2.20e-8 (at r 2, not in the column) to 1.05e-7 for 0.1 <= r <= 2, and
  1.37e-7 to 5.11e-7 at r 10.0 to 10.3 for 10 <= r <= 100. Off the y-axis (pi/2 - theta >= 0.2) the r <= 0.1 maximum is
  2.4e-11 on the independent evaluator and 2.3e-11 on a between-node scan of the formula, at the same place (r 0.1,
  theta near 0); within 0.2 of the y-axis the independent evaluator reads up to 5e-9 and the scan 3e-12, so the (*)
  values there are set by the evaluator floor. The same holds for 10 <= r <= 100: off the y-axis the two agree (8.2e-8
  against 8.0e-8 at r 13.9, theta 0.92).
Absolute values. The maxima of |R| itself on the same between-node grids (all evaluation columns; candidate, formula
beyond the fit; 16875 x 512 / 22500 x 512) and, as a scale, the maximum of |rho| over the region, which sits at the
outer radius of each region since rho grows like r^3 at the centre and like r^(1/c_l) at large r:
     region                 max |R|                  max |rho|      max |R| / max |rho| (16875 x 512)
     r <= 0.1               1.71e-13 / 1.65e-13      3.85e-4        4.4e-10
     0.1 <= r <= 2          8.92e-8 / 8.91e-8        2.94           3.0e-8
     2 <= r <= 10           6.03e-5 / 5.82e-5        111.7          5.4e-7
     |X - P| < 0.5          1.05e-5 / 1.05e-5        14.80          7.1e-7
     10 <= r <= 100         1.99e-5 / 1.98e-5        208.9          9.5e-8
     100 <= r <= 1000       6.03e-6 / 6.04e-6        319.2          1.9e-8
     1000 <= r <= 7.652e6   1.897e-4 / 1.897e-4      1590           1.2e-7
  The last column is a quotient of two suprema over the region, not a pointwise ratio. At 11250 x 384 and 16875 x 768
  the absolute maxima agree with these to 6 percent, except r <= 0.1 (1.3e-13 to 2.7e-13 over the four configurations,
  round-off level) and 2 <= r <= 10 at 11250 x 384 (1.10e-4, the under-resolved lobe of 4.3). The whole-box absolute
  maximum is the far value 1.897e-4 beyond 1000 L, where the candidate has no fit rows; over r <= 1000 (with or without
  the evaluation columns next to the y-axis) it is 6.03e-5 / 5.82e-5. Scaled by the size of rho the absolute residual is
  at most 7.1e-7 on these two configurations (next to P; 7.5e-7 at 16875 x 768), the order of the normalized maxima
  above.
Elliptic equation. The velocity is computed from rho by the canonical inverse (V1), so -Lap psi = d_x rho carries no
separate fitted residual; the numerical error of the inverse is reported in 4.5. As a check of the evaluator's inverse
(not a property of the trial), re-differentiating its psi (8th-order differences in log r, spectral in theta) gives for
the elliptic residual E = -Lap psi - d_x rho, on the candidate, sup|E| / sup|d_x rho| = 1.49e-6, 3.93e-7, 1.06e-7 on
1 <= r <= 10 at N = 11250, 16875, 22500 (falling with N; quotients of suprema over the region; sup |d_x rho| = 20.0
there, so sup|E| = 2.98e-5, 7.86e-6, 2.12e-6), at most 2.1e-9 for r >= 10 and 1.3e-8 to 5.2e-8 on 0.01 <= r <= 1; on
r <= 0.01 it is round-off of the second difference where psi ~ r^2 (up to 3.15e-4, rising as N^2). X1 and F0 give the
same to 10 percent.

Resolution rows (c_l held at 5.5753626 on each basis, each on its own fit grid; 16875 x 512) and domain columns:
     basis (radial x angular)       whole-box N_f   N_v r <= 1000   J (857, eps 0.03)   h(P) - 1 (11250 / 16875)
     244 x m <= 100                 3.74e-6         1.06e-6         5.58e-6             -2.7e-8, -6.9e-8
     375 x m <= 100                 3.11e-6         8.74e-7         5.28e-6             2.6e-7, 1.5e-8
     375 x m <= 150 (X2)            1.435e-6        4.00e-7         3.14e-6             2.2e-7, 1.6e-8
     375 x m <= 200 (X3)            6.84e-7         1.92e-7         1.39e-6             2.8e-7, 3.1e-8
     375 x m <= 250 (refinement)    4.23e-7 (a)     1.23e-7         5.00e-7             -, 3.2e-8
  (a) With the columns within 0.006 of the y-axis excluded; with them 5.38e-7, the evaluator's floor in the column next
  to the axis (4.4). The value is the lobe above P on the unshifted grid; over four radial sampling phases at 16875 x
  512 it is 4.22e-7 to 4.66e-7, and 4.88e-7 at 22500 x 512 (X3's lobe: 4.27e-7 to 4.74e-7 and 4.95e-7). The
  m <= 250 row is read at 16875 and 22500 radial points only: the exponent H of its density carries angular frequencies
  to 500 (cos(2 m theta), m <= 250), beyond the 479 modes of 11250 x 384; the agreement of 16875 x 512 and 16875 x 768
  (columns next to the y-axis excluded) is the aliasing check.
  Domain columns (c_l held at 5.5753626106; X3 continued 20750 iterations on each domain with the two-term closure at
  100 L, 333 L or 1e4 L beyond the fit radius; ratios to X3 in its own convention on the independent evaluator at 11250
  x 384, 16875 x 512, 22500 x 384):
     fit radius        2-10 N_f max ratio   10-100 N_f ratio raw (cut)  h(P) - 1 (N >= 16875)   J (857, eps 0.03)
     900 L (X3)        1                    1                           3.1e-8, -1.8e-8          1.39e-6
     300 L             0.99, 0.62, 0.74     0.89, 0.76 (cut 0.79), 0.96     5.1e-8, -3.1e-9          8.14e-7
     90 L              1.04, 0.62, 0.72     1.02, 1.23 (cut 0.84), 0.83     5.6e-8, 6.8e-10          5.53e-7
     9000 L            1.02, 0.66, 0.74     0.82, 1.42 (cut 1.05), 1.00     4.8e-8, -5.0e-9          9.11e-7
  ("cut": the columns with pi/2 - theta < 0.006 excluded, at 16875 x 512; the raw 10-100 maxima lie in that column. The
  9000 L row has fit rows to 9000 L and its inverse domain and closure at 1e4 L.)
  The m <= 250 row is a refinement row only (it is not a candidate; reading fixed before its run). Budget: the m <= 150
  and m <= 200 rows are at different budgets (X3 = X2 + 20750); the equal-budget comparison is in 4.1. The m <= 250 row
  is X3 with its angular cap raised to 250 and continued 20750 iterations at the fixed c_l, so it is at the budget
  X3 + 20750. The m <= 100 rows are fixed-c_l fits of their own bases continued for 20750 iterations, as X2 is on its
  basis (c_l 2.1e-9 above X3's at 375 and 1.7e-9 at 244).
Reading rule fixed before the runs: the domains agree if the 2-10 and 10-100 maxima are within a factor 1.5 of the
formula-global fit on the same basis (read two-sided, ratios between 1/1.5 and 1.5; each domain column falls below 1/1.5
at one configuration, being lower, not higher) and |h(P) - 1| < 1e-7; J is reported next to them. Domain fits with a
two-term closure beyond the fit radius are only C^1 across that radius; they are quoted as bounded-domain fits, not as
admissible trial densities. The domain columns hold c_l at the candidate's value and test whether the interior residual
and the consistency condition h(P) = 1 depend on the box in the closed problems; each continues X3 for 20750 iterations
on its own domain, so they also carry that further budget. They are not residuals of the domain fits under the canonical
velocity law. At interior points the velocity of a bounded-domain fit depends on what is assumed beyond its fit radius
(the two-term closure, or the formula's own continuation, which is not fitted there in any bounded-domain fit). In
normalized-residual terms (sampled maxima, earlier domain fits on the 375 x m <= 100 free basis) the dependence is
6.8e-7 (closure at 111 L; separate evaluator) and 8.6e-6 (closure at 100 L; real-space quadrature of the third
evaluator, most of it drift of the unfitted exterior formula over that fit's extra iterations) within 0.5 of P,
comparable to or larger than the interior residual, and 2.2e-8 within 0.5 of P and 2.7e-8 at 0.5 to 2.5 from P for the
closure at 333 L (separate evaluator). For the 90 L fit from X3 the residual within 0.5 of P is 1.9e-7 to 2.3e-7 in N_f
with the closure at 100 L (h(P) - 1 between -5e-9 and +6e-8 over two independent sets of grids) and about 3e-5 with the
formula continued beyond the fit radius (h(P) - 1 about -6e-5); in N_v it is 6.0e-8 with the closure and 9.4e-6 with the
formula continued (11250 x 384), and the real-space quadrature of the third evaluator gives 6.6e-6 at its sampled points
within 0.5 of P when the closure is replaced by the formula continued to infinity, with the closure-convention
denominator held fixed (velocity change 4.2e-4 there); for the 300 L fit the N_f residual within 0.5 of P is 3.9e-7 with
the closure at 333 L and 4.9e-7 with the formula continued (11250 x 384; the lead's evaluator gives 3.5e-7 and 4.0e-7).
By the reading rule the 90 L domain agrees with the candidate on the lead's evaluator (2-10 ratios 0.70 and 0.73, 10-100
ratio 0.82) and on two of the three configurations of the separate evaluator; on the third (16875 x 512) its 2-10
maximum is 0.62 times the candidate's, outside the factor 1.5 on the low side. Where it differs, it is lower: within 0.5
of P its residual is 3 times and its J 2.5 times below the candidate's (the gain sits in the strip next to the x-axis
left of P and in the band y 0.2 to 1; the lobe above P does not move and becomes the 2-10 maximum). That fit carries
both the smaller domain and the further budget, and it solves a different closed problem from its start (the closure at
100 L changes the interior velocity of the X3 shape; start objective 2.3e-4 on its rows), so it shows that X3's near-P
residual is not a floor of the m <= 200 basis in that closed problem; it does not show the same gain for the full-plane
problem. The 300 L domain agrees in the same way: on the lead's evaluator (2-10 ratios 0.74 and 0.72, 10-100 ratios
0.86) and on two configurations of the separate evaluator, with the 2-10 ratio 0.62 at 16875 x 512, where for both
domain columns the 2-10 maximum is the lobe above P (4.27e-7 and 4.23e-7), which no column moves, while the candidate's
lies next to P. The 300 L fit carries the same further budget as the 90 L fit and differs from it in the domain only:
within 0.5 of P its residual is 0.57 to 0.59 times the candidate's and its J 0.59 (eps 0.03; 0.56 at eps 0.01), against
0.32 to 0.33 and 0.40 for the 90 L fit, the strip left of P 0.67 against 0.41, the lobe above P 0.99 against 0.98. The
9000 L fit, whose rows reach 9000 L, carries the same further budget and agrees in the same way (2-10 ratio 0.66 at
16875 x 512, where its 2-10 maximum lies next to P; 10-100 ratio 1.42 there, 1.05 with the cut): within 0.5 of P its
residual is 0.66 to 0.68 times the candidate's and its J 0.66 (eps 0.03; 0.64 at eps 0.01), N_v for r <= 1000 1.02, 0.66
and 0.78 times, the lobe above P 1.00. Among these three domain columns the near-P gain at that budget therefore grows
as the domain shrinks; with the budget row below (900 L) included it is not monotone in the domain. X3 continued on its
own domain and rows for the same iterations (the budget row of 4.2) reads 0.50 to 0.54 times the candidate's within 0.5
of P and 0.48 in J (0.45 at eps 0.01). Against that row, by the reading fixed before it ran (ratios in [0.8, 1.25]
attribute the gain to the budget), the 300 L fit reads 1.08 to 1.09 within 0.5 of P and 1.21 in J (1.254 at eps 0.01,
0.004 above the interval), so its near-P gain over X3 is that of the budget; the 90 L fit reads 0.60 to 0.63 within 0.5
of P (0.82 in J) and the 9000 L fit 1.25 to 1.27 and 1.35 (1.42 at eps 0.01), outside the interval near P on all three
configurations (90 L) or on two of the three (9000 L, inside at 16875 x 512 only; its J is outside), so for these two
the ratios are stated without attribution. The closure and the formula readings of a domain fit measure its sensitivity
to two exterior continuations, not a closure error of a fitted far field. The domain columns are therefore a stability
observation within closed fitting problems, not an upper bound on the full-plane truncation error; they do not establish
domain independence of the full-plane problem (the reading of the same fits under the canonical law follows below). For
the formula-global fits, whose rows are r < 900 L and whose inverse domain is r <= 1000 L, the fits' own inverse
convention (the density replaced by its two-term exterior extension beyond 1000 L) was compared with the formula
continued to the evaluator's outer radius, on one grid of the separate evaluator (11250 x 384), maxima over all grid
points of the open first quadrant. On X1, which holds c_l fixed and therefore sees only the change of velocity, the
residual changes by at most 5.1e-9 in N_f and 1.5e-9 in N_v within 0.5 of P, 1.0e-8 in N_f and 3.2e-9 in N_v at
2 <= r < 10, and at most 2.0e-8 in N_v for r < 1000 (1.6e-8 for r <= 300): about 1 percent of X1's band maxima next to
P, 1.5 percent at 2 <= r < 10 and at most 7 percent at 300 to 1000. In the identity convention c_l also moves, by
3.4e-9. The free fit of the 375 x m <= 100 basis gives the same values to 2 percent. On X3 directly (separate evaluator,
11250 x 384 and 16875 x 512, the two grids agreeing to 3 digits) the changes are the same to two digits, and c_l moves
by 3.4e-9 in the identity convention (the identity in the fit's own convention returns the fixed c_l to 2.2e-10).
Relative to X3's band maxima the changes are 0.8 percent next to P, 1.5 percent at 2 <= r < 10 and 22 to 47 percent in
N_v at 10 <= r < 1000, where X3's band maxima are smaller than X1's; X3's band maxima themselves move by at most 1
percent next to P and at 2 <= r < 10, by at most 10 percent at 10 to 300 and by 18 to 23 percent (lower in the fit's
convention) at 300 to 1000. On X3's rows beyond r = 1000 (131 L to 900 L) the fit's convention reads 0.25 to 0.47 of the
formula reading. The residuals of 4.3 and 4.4, except the domain columns read in each fit's own convention, are the
formula (canonical) reading. These are grid maxima for one closure; they do not exclude other far-field defects.

Domain columns under the canonical law. Without its closure each domain fit is a global trial density (the formula of
4.2 with its own coefficients), so read with the formula continued beyond its fit radius (no closure) its residual is a
full-plane residual under the canonical law, comparable with the candidate's. No reading rule was fixed for this
comparison before it was computed. Independent evaluator (own inverse to 1e6 L) at 11250 x 384 / 16875 x 512 / 22500 x
384, columns within 0.006 of the y-axis excluded; each domain fit continues X3 for 20750 iterations, and the 900 L row
at that budget is the budget row of 4.2:
     fit rows to (iterations after X3)  N_f r <= 1000            N_f |X - P| < 0.5        N_v r <= 1000            N_v r > 1000
     90 L (20750; 11250 x 384 only)     1.02e-4                  3.11e-5                  9.87e-4                  1.32e-2
     300 L (20750)                      7.66e-7/5.28e-7/5.59e-7  4.86e-7/4.88e-7/4.87e-7  4.12e-7/4.14e-7/4.12e-7  3.54e-5/3.53e-5/3.54e-5
     900 L (20750, budget row)          6.97e-7/4.25e-7/4.86e-7  3.54e-7/3.59e-7/3.55e-7  1.94e-7/1.24e-7/1.42e-7  1.077e-6/1.077e-6/1.078e-6
     9000 L (20750)                     7.05e-7/4.49e-7/4.91e-7  4.45e-7/4.49e-7/4.51e-7  1.96e-7/1.26e-7/1.44e-7  3.27e-8/3.31e-8/3.28e-8
     900 L (0, the candidate X3)        6.91e-7/6.84e-7/6.61e-7  6.51e-7/6.84e-7/6.61e-7  1.92e-7/1.92e-7/1.85e-7  1.084e-6/1.074e-6/1.085e-6
Against the 900 L row at the same budget, the 9000 L row reads 1.01, 1.06 and 1.01 in N_f for r <= 1000, 1.25 to 1.27
within 0.5 of P, 1.01 to 1.02 in N_v for r <= 1000 and 0.030 to 0.031 beyond r = 1000; the 300 L row reads 1.10, 1.24
and 1.15, 1.36 to 1.38, 2.1 to 3.3 and 33. Under the canonical law the fits with rows to 300 L, 900 L and 9000 L thus
give the same N_f residual for r <= 1000 to a factor 1.24 and within 0.5 of P to a factor 1.4 (1.3 between 900 L and
9000 L); in N_v for r <= 1000 the 300 L fit is 2.1 to 3.3 times higher, and beyond r = 1000 the band follows the extent
of the fitted rows and of the inverse domain with its closure, which each domain fit has just beyond its rows (3.5e-5,
1.1e-6 and 3.3e-8; for the 9000 L row the inverse domain alone gives the factor 0.27 of its fall, 4.5). The 90 L fit is
not an approximate full-plane profile under the canonical law (3.1e-5 within 0.5 of P, 1.3e-2 beyond r = 1000): its
agreement in the reading of the domain rule holds only with its closure. These are grid maxima on three configurations,
not a convergence study in the domain; the closure readings above remain the sensitivity check of the closed problems.

Free-branch record (c_l from the identity; verifier between-node numbers; J on 857 labels):
     basis               c_l         J spread eps 0.03 / 0.01   I(0.03)     N_f max (**)
     215 x m <= 100      5.5763607   1.940e-5 / 1.940e-5        -2.97e-7    1.86e-5
     244 x m <= 100      5.5763633   4.746e-6 / 4.980e-6        -4.68e-7    4.6e-6
     302 x m <= 100      5.5763609   3.473e-6 / 3.607e-6        +5.08e-7    2.3e-6
     375 x m <= 100      5.5763622   3.679e-6 / 3.669e-6        +4.84e-7    2.44e-6
     375 x m <= 150 (F2) 5.5763709   3.414e-6 / 3.763e-6        -7.04e-7    1.57e-6
     375 x m <= 200 (F3) 5.5763712   1.481e-6 / 1.709e-6        -3.51e-7    6.95e-7 to 7.65e-7
  (**) For the four m <= 100 rows the N_f maximum on 2 <= r < 10, the band containing P (on the 244 row this is the
  whole-box maximum; within 0.5 of P that row reads 3.25e-6, the value compared in 4.3); for F2 the lowest whole-box
  value of the table of 4.3; for F3 the maximum within 0.5 of P over the four configurations.
Domains on 375 x m <= 100 (free; fit radii 900 L, 300 L, 100 L, each read with its own closure): J 3.679e-6, 4.052e-6,
4.000e-6 (eps 0.03); c_l 5.5763622, 5.5763628, 5.5763644.
Reading. Along the radial sequence at m <= 100 the J spread falls by a factor 4 from 215 to 244 functions and by 27
percent from 244 to 302, and rises by 6 percent from 302 to 375; it is not monotone at the last step. At the fixed c_l
(each fit continued for 20750 iterations at that c_l), the step from 244 to 375 radial functions at m <= 100 lowers the
whole-box N_f by the factor 0.83 to 0.86, the N_f maximum within 0.5 of P by 0.95, N_v for r <= 1000 by 0.83 to 0.85
(11250 x 384 and 16875 x 512) and the 857-label J by 0.95 (0.91 at eps 0.01). N_v for r > 1000 is equal within the
configuration spread (1.31e-6 and 1.35e-6 at 244, 1.325e-6 at 375, the maximum at 244 in the column next to the y-axis),
and with the columns next to the y-axis excluded (pi/2 - theta < 0.006) it is 6.4 percent higher at 375 (1.325e-6
against 1.245e-6, both at 3.3e3 to 3.4e3 L, theta 1.541). No reading of this pair was fixed before its run; these are
data. The radial rows at m <= 100 stall at the angular floor (on the 375 x m <= 100 fit, the only one of these rows
where it was measured, the J oscillation across family A is carried by residual at angular frequencies at or above the
cap). The angular rows are the test: at the fixed c_l, J falls from 3.14e-6 (m <= 150) to 1.39e-6 (m <= 200), on the
free branch from 3.41e-6 to 1.48e-6, and at equal budget the m <= 200 iterate has 0.62 to 0.69 times the J of the
m <= 150 iterate on 185 labels (every fourth label of family A). The angular row at the fixed c_l (m <= 100, 150, 200;
the last 20750 iterations of each at the fixed c_l, from different starts) was read by a rule fixed before the runs: the
residual improves systematically if none of whole-box N_f, N_f within 0.5 of P, N_v for r <= 1000, N_v for r > 1000 and
the 857-label J increases from one row to the next by more than the spread between the evaluation configurations. On the
independent evaluator (11250 x 384 and 16875 x 512; J at 16875 x 384) these are, for m <= 100, 150, 200: whole-box N_f
3.12e-6 / 3.11e-6, 1.42e-6 / 1.43e-6, 6.91e-7 / 6.84e-7 (the whole-box maximum lies within 0.5 of P except for m <= 200
at 11250 x 384, where the maximum within 0.5 of P is 6.51e-7); N_v for r <= 1000 (no evaluation column excluded) 8.73e-7
/ 8.74e-7, 3.98e-7 / 4.00e-7, 1.92e-7 / 1.92e-7; N_v for r > 1000 1.325e-6 / 1.325e-6, 1.10e-6 / 1.11e-6, 1.09e-6 /
1.10e-6; J 5.28e-6, 3.14e-6, 1.39e-6 (eps 0.03). Each decreases at both steps on both configurations: from m <= 100 to
150 by factors 0.46 to 0.63 (0.83 to 0.84 for N_v for r > 1000), from 150 to 200 by factors 0.44 to 0.49 except N_v for
r > 1000, which decreases by 1.26e-8 and 1.33e-8 (factor 0.99), about the configuration spreads (1.24e-8 and 1.17e-8).
That maximum is at 3.3e3 L, theta 1.541 for m <= 100 and next to the y-axis at 4.9e3 L for m <= 200 (4.5). The 375 x
m <= 100 fit has the same centre structure (identity c_l to 3.3e-9, h(P) - 1 2.6e-7 and 1.5e-8, a single zero of the
x-velocity on the axis at 8.60006, sampled).

The m <= 250 refinement row (X3 with the angular cap raised to 250, continued 20750 iterations at the fixed c_l; not a
candidate by the reading fixed before its run) is read at 16875 x 512, 16875 x 768 and 22500 x 512, with the ratio to X3
on the same configuration: whole-box N_f 5.38e-7, 9.82e-7, 5.41e-7 (0.79, 1.37, 0.79), N_f within 0.5 of P 2.41e-7,
2.95e-7, 2.26e-7 (0.35, 0.41, 0.33), N_v for r <= 1000 1.23e-7, 3.16e-7, 1.44e-7 (0.64, 1.27, 0.75), N_v for r > 1000
1.096e-6, 1.114e-6, 1.101e-6 (0.995, 1.003, 0.998), and J 5.00e-7 at eps 0.03 and 5.89e-7 at eps 0.01 (0.36 and 0.37;
16875 x 512). Its whole-box maxima on every configuration and its N_v maxima for r <= 1000 at 16875 x 768 and 22500 x
512 lie in the evaluation column next to the y-axis, and its increases over X3 at 16875 x 768 (2.7e-7 in N_f, 6.8e-8 in
N_v) are inside its own configuration spread (4.4e-7 and 1.9e-7), so the reading as fixed is met. In those columns the
values are the evaluator's floor, on X3 as on this row: on two angular resolutions they grow about like the inverse
square of the distance from the axis and change sign between the resolutions, while from distance 0.01 on the two agree
to 3 to 21 percent (to about 10 percent except next to a sign change of R at 0.013) at 1e-8 to 3e-8, which is 0.25 to
0.51 times X3's at the distances the two resolutions share (0.09 to 0.73 over all columns up to distance 0.039). With
the columns within 0.006 of the y-axis excluded, the whole-box N_f is 4.23e-7, 4.27e-7, 4.88e-7 (0.62, 0.60, 0.71; at
the lobe above P, r 8.72 to 8.74, theta 0.194, a maximum that moves with the radial sampling: 4.22e-7 to 4.66e-7 over
four radial sampling phases at 16875 x 512, where X3's lobe is 4.27e-7 to 4.74e-7, the same to 2 percent; 4.95e-7 for X3
at 22500 x 512) and N_v for r <= 1000 is 1.23e-7, 1.24e-7, 1.42e-7 (0.64, 0.62, 0.74). On that reading, whole-box N_f,
N_f within 0.5 of P, N_v for r <= 1000 and J decrease at each step of the row m <= 100, 150, 200, 250 on every
configuration, and N_v for r > 1000 rises at the last step by 2.5e-9 to 4.7e-9 (0.23 to 0.44 percent), more than the
spreads over these three configurations, 6.9e-10 and 2.2e-9, of the m <= 250 and m <= 200 rows (maximum at about 4800 L,
0.0065 to 0.0098 from the y-axis, on the first or second column beyond the cut). Along the row N_v for r > 1000 (ratios
on these three configurations over all evaluation columns 0.84 to 0.85, 0.98 to 0.99, 0.995 to 1.003 per step; at the
last step 1.002 to 1.004 with the columns next to the y-axis excluded) and the first-order far-field coefficient C at
the axis of 4.5 (0.944, 0.988, 0.998) level off: beyond r = 1000 the band is set by the far-field profile, which the
angular refinement leaves at X3's. The m <= 250 row is lower than the candidate in the interior and in J, and the
deliverable does not change. It is at the budget X3 + 20750 iterations, as is X3 continued on its own basis and rows
(4.2). At that budget, on the same three configurations, the m <= 250 row reads 0.97 to 1.00 times the budget row in
whole-box N_f and in N_v for r <= 1000 (columns within 0.006 of the y-axis excluded; for both rows the maximum is at the
lobe above P; in whole-box N_f 0.96 to 0.995 over four radial sampling phases at 16875 x 512), 0.63 to 0.82 within 0.5
of P, 1.001 to 1.002 in N_v for r > 1000 and 0.74 in J (0.82 at eps 0.01), and 0.38 to 0.54 in the bands 0.1 to 2, 10 to
100 and 100 to 1000 (16875 x 512). At the lobe above P the three rows agree to within 4 percent over four radial
sampling phases (the m <= 250 row 0.96 to 0.995 of the budget row, the budget row 0.98 to 1.02 of X3), so the whole-box
maxima of the m <= 250 row and of the budget row are the lobe value, which the further iterations do not lower and the
raised cap lowers by at most 4 percent; their whole-box ratios to X3 come from the fall next to P. Next to P and in the
bands away from P the raised cap lowers the residual further. These ratios at equal budget are stated without an
attribution threshold. Its free control (F3 enriched to m <= 250 and continued with c_l free for the same 20750
iterations; not a candidate) ends at c_l 5.5763706 (the free branch under the angular refinement: F2 5.5763709, F3
5.5763712, then 5.5763706). At m <= 250 and equal budget the free control and the fixed row agree in the whole-box and
r <= 1000 maxima to about 1 percent, with differences of both signs inside the configuration spread; the free control is
lower next to P (by 3 to 11 percent, inside the phase spread of that maximum) and beyond r = 1000 (by 0.1 to 0.4
percent); the fixed row is lower in the 857-label J (by 2 to 3 percent, beyond the spread of J between configurations).
By the selection rule the free control wins this pair on whole-box differences of about 1 percent, below the resolution
of that maximum. The pair is a refinement row and does not change the candidate. The centre values of the m <= 250 row
are X3's: the identity gives c_l 5.5753626074 (the fixed value 3.2e-9 above it, as for X3), h(P) - 1 is +3.2e-8 and
-1.8e-8 at 16875 and 22500 radial points (X3's to 1e-9; 5e-9 from the dense axis traces used for the identity-free root
of h(P) = 1 in 4.3), the x-velocity has a single zero on the axis at 8.600064, and the zero set passes the sampled check
of 4.2 (min |W| / (c_l |X|) 0.0216, 0.0067, 0.0023 at distance 1, 0.3, 0.1 from P). The m <= 250 row continued for 20750
iterations at the fixed c_l with rows to 9000 L and the inverse domain and closure at 1e4 L (a data row, not a
candidate; reading fixed before the run) reads 1.021 and 1.023 times the m <= 250 row in whole-box N_f for r <= 1000 and
0.665 and 0.712 within 0.5 of P (16875 x 512 and 22500 x 512), so the interior gain of the cap is kept with rows to 9000
L (the fall next to P mixes the further budget and the rows), and over 1000 L to 9000 L (formula continued) 0.608 and
0.610 times the 9000 L row continued for the same total iterations (4.5). The difference sits next to the y-axis at the
inner end of that band, where the 9000 L row continued has its maximum (3.29e-8 at 1070 L); the m <= 250 row continued
is at most 2.00e-8 in the band (in the fit convention at 22500 x 512 its largest value next to the y-axis, at 3944 L,
and its largest value away from it, at 8998 L and theta 0.62, agree to 3e-4), and over 9000 L to 1e4 L the ratio is
0.94. Against X3 it reads 0.234 and 0.235 within 0.5 of P and 0.631 and 0.730 in whole-box N_f for r <= 1000; it has
41500 iterations beyond X3, a larger cap and other rows, so this is not an equal-budget comparison.

### 4.4a P_2 consistency checks
For exact P_2 profiles, R5 and R6 give h(P) = 1 (C^(2,alpha) gives psi in C^(3,alpha)_loc, so W is C^2 near P; the local
form also needs rho_y(x,0) > 0 on (0, x*), which the axis equation of R10 supplies). For the trial, with rho = y g and
W_2 = y h near P, R/rho = h - 1 + W.grad log g off the axis; the right side is continuous across the x-axis (rho in
C^2, W in C^1, rho_y(P) > 0), and its value at P is h(P) - 1. So imposing h(P) = 1 enforces the source limit of the
normalized transport equation; near P, N_f is about 2|rho|, so a small N_f residual approaching P implies it. Values:
|h(P) - 1| = 2.8e-7, 3.1e-8 and 1.8e-8 on the candidate at 11250, 16875 and 22500 radial points, and 2.4e-7, 4.2e-8 and
1.9e-8 on its control, falling with the radial resolution of the evaluator (its grid error). These are consistency
checks of the trial, not accuracy bounds.

### 4.4b Characteristic defect
J_eps(X0) = int_{t_eps}^0 (R/rho)(Phi_t X0) dt along the backward characteristic of the trial's own W from X0 to the
cutoff |X - P| = eps. It is the logarithmic ratio log rho(X0) - log rho_tr,eps(X0), where rho_tr,eps(X0) = e^(-t_eps)
rho(Phi_{t_eps} X0) transports the trial's own density on the cutoff section by the frozen trial field W (e^J - 1 is the
difference relative to rho_tr,eps). Backward characteristics off the x-axis approach P along the slow vertical
eigendirection, and under Hoelder regularity J_eps = (h(P) - 1) log(1/eps)/h(P) + C(X0) + o(1) for each fixed off-axis
label; this O(1) is not uniform as labels approach the x-axis. The reported quantity is the spread of J_eps over a named
label set on r = 20: 737 angles uniform on [0.02, pi/2 - 0.02] (family A) and 60 angles at geometric distances 1e-4 to
0.02 from each axis (families B and C). On the candidate the 857-label spread is 1.388e-6 at eps = 0.03 and 1.602e-6 at
eps = 0.01 (family A: 1.341e-6 / 1.563e-6; family B 2.51e-7 / 2.55e-7; family C 7.23e-7 / 8.46e-7); on its control
1.481e-6 / 1.709e-6 (family A 1.432e-6 / 1.670e-6), ratio 0.937 / 0.937. Against X2 (3.143e-6 / 3.462e-6) the ratio is
0.44 / 0.46; it is below 1 on every family (A 0.43 / 0.45, B 0.39 / 0.39, C 0.51 / 0.54). On the candidate the 857-label
spread is estimated, from the sampled labels and their parabolic refinement, to equal the supremum minus the infimum of
J_eps over all labels on r = 20 at distance at least 1e-4 from the axes to about 1e-8 (at 16875 x 384; a parabola
through the sampled maximum and its neighbours peaks 5e-10 above it; the 369-label subset of family A used earlier gives
a spread 0.5 percent lower), and on earlier fits to about 2e-8. Closer to the y-axis J_eps grows like (3
c_l - psi_xy(0) - 1) log(1/d)/(2 c_l - 1), 9.6e-10 per factor e in the distance d from the axis (3
c_l - psi_xy(0) - 1 = 9.8e-9 on the candidate), and by the leading logarithmic term leaves the sampled range only for d
below e^(-1190). The spread removes the common logarithmic term but does not measure a transport error common to all
labels. At |h(P) - 1| of 3.1e-8 and 1.8e-8 on the two finer grids the logarithmic term is below 1.5e-7 at eps = 0.01. On
the candidate and on its control the 857-label maximum is at the family-A label theta0 1.520 (r_min 2.1), whose J
(8.2e-7 at eps 0.03) comes almost all from the disk |X - P| < 0.5. The minimum is at the family-B label theta0 1.555
(r_min 0.93), with J -5.7e-7 from the strip next to the x-axis and that disk in about equal parts. The labels within
about 1e-3 of the y-axis, whose characteristics follow the separatrix (down the y-axis, past the origin, along the
x-axis to P), have J -3.21e-7 to -3.24e-7, close to the axis integral I(0.03) below; farther from the axis family B
decreases monotonically to that minimum, at distance 0.015 from the y-axis. On the 375 x m <= 100 free fit and on X1 the
oscillation of J across family A is carried by angular frequencies at and above the cap; on F1 it is not. On X3 and F3
the residual in the band of angular frequencies 400 to 600 in the strip r 7.0 to 8.3 next to the x-axis is about 3.4
times smaller than on X2. Axis. On the x-axis between the origin and P, rho = 0 and W_2 = 0, and R/rho has an even
continuous limit q0(x); a label on the separatrix gains I(eps) = int_{0.01}^{x* - eps} q0(x)/|W_1(x, 0)| dx on the axis,
a label-free companion of the spread. On X3, I(0.03) = -3.30e-7 and I(0.01) = -4.13e-7 (independent evaluator; lead
-3.40e-7 and -4.04e-7; X2: -6.36e-7, -7.85e-7, independent evaluator); max |q0| = 1.29e-6 at x 6.64 (independent
evaluator; lead 1.33e-6 at x 6.67; X2 3.13e-6 at x 2.80); lead profile of X3: q0 = 3.8e-7 at x 1, 1.07e-6 at 2, 1.19e-6
at 3, 5.7e-7 at 4, -4.3e-7 at 5, -1.17e-6 at 6, -1.30e-6 at 7, -1.04e-6 at 8. |q0| is 0.99e-6 to 1.07e-6 on [8, 8.53]
(1.02e-6 to 1.07e-6 on [8, 8.49]), with its maximum on [8, x*) 1.07e-6 at x 8.36; beyond 8.53 it decreases, with the
ripple, to 9.5e-7 at 8.56, 7.1e-7 at 8.59 and 3.6e-7 at 8.595, the last evaluation node before x*; q0 is negative on
[7.5, x*) with no sign change (independent evaluator, at 33750 radial points, by the spectral axis value, which the
Richardson sequence approaches to 1.8e-8). It is the axis value of the residual ripple at the angular cap frequency
(carried by angular frequencies up to 600); the smooth part next to the axis is about 5e-8. On F3: I(0.03) = -3.51e-7
(independent evaluator; lead -3.61e-7), max |q0| 1.32e-6 (independent evaluator; lead 1.37e-6 at x 6.66). The long
continuation from X1 lowered q0 between the origin and x 5 by a factor 3 at m <= 150 (X1: max |q0| 1.07e-5 at x 3.57,
I(0.03) +2.04e-6), and the cap 200 by a further factor about 2.7 on [0, 5] (max |q0| there 1.16e-6 at x 3 on X3 against
3.13e-6 at x 2.80 on X2; 2.4 for the maxima over the whole segment). So R/rho on the axis segment between the origin and
P reaches 1.3e-6 on the candidate. N_f and N_v are both at least |rho| (each is |rho| plus nonnegative terms), so the
tables above show the same residual at a smaller size next to the axis; R/rho itself enters the report only through
J_eps, I(eps) and q0.

### 4.5 Far field and nonlocal inverse
Far field: the residual for r > 1000 is at most 1.324e-7 in N_f (at r 3.3e4, theta 0.84) and 1.112e-6 in N_v, with the
N_v maximum next to the y-axis at r 3.6e4 to 3.7e4, beyond the inverse domain, where the formula's far-field model (4.2)
is in force and the candidate has no fit rows; inside the inverse domain (1000 <= r <= 7652, that is 1000 L) N_v is at
most 2.15e-7 / 2.18e-7 (11250 x 384 / 16875 x 512). Next to the y-axis in the far field the residual is a residual of
the fit, not the evaluator's floor: on the axis column itself |R| is at most 8.9e-9, and over the first columns off the
axis the N_v maxima are 1.111e-6, 1.096e-6, 1.082e-6, 1.077e-6, 1.073e-6, 1.073e-6, a smooth profile flat to 4 percent
(on X2, R and N_v were measured to grow together as (pi/2 - theta)^2 over those columns). Beyond the fit rows the band
is hardly moved by any fit: without the column exclusion F0, X1, F1r, X2, F2, X3, F3 and the reorthogonalized arm of 4.2
read 1.08e-6 to 1.17e-6 there, F1 1.46e-6 to 1.47e-6 and W1 1.28e-6 to 1.31e-6. These fits have rows only to 900 L
(4.2). The 9000 L domain row of 4.4 (X3 continued for 20750 iterations at its c_l with rows to 9000 L, inverse domain
and two-term closure at 1e4 L; not a candidate) tests the band. Its N_v maximum over 1000 L < r <= 9000 L is 3.20e-8 /
3.04e-8 (16875 x 512 / 22500 x 384), 0.029 / 0.028 of X3's on the same configurations, at 1013 L and 1026 L near the
y-axis (theta 1.563 and 1.548), and over 9000 L < r <= 1e4 L it is 2.40e-8 / 2.41e-8 (0.025) at theta 0.62. Beyond 1e4
L, where it has no rows, its own two-term closure reads 2.3e-5 next to the y-axis at 2.3e4 L (the closure regions of the
300 L and 90 L fits read 5.1e-3 and 2.8e-2, also next to the y-axis), and the formula continued instead reads 3.28e-8
(0.035 of X3's, at 2.2e4 L, theta 0.62). With the formula continued its whole-box N_v maximum is in the interior,
1.256e-7 / 1.435e-7. Its interior is that of 4.4 (2-10 ratios 1.02, 0.66, 0.74; within 0.5 of P 0.66 to 0.68 times
X3's). So X3's far-band value is that of the unfitted continuation of its formula, and continuing X3 with rows to 9000 L
lowers it over 1000 L to 9000 L by the factor 0.028 to 0.029 (the rows, the larger inverse domain with its closure and
the further iterations together). Its equal-budget free control (F3 continued in the same way with c_l free; a data row,
not a candidate) moves c_l by -1.5e-6 in the 20750 iterations and reads 0.029 to 0.030 of F3's over 1000 L to 9000 L;
the 9000 L row's far bands are within 4 percent of it, and the 9000 L row is 0.93 to 0.94 times it within 0.5 of P and
in J, as X3 is against F3. The 9000 L row continued for a further 20750 iterations at its c_l on the same rows and
domain (a data row, not a candidate; reading fixed before the run: ratios in [0.8, 1.25] on both configurations mean
that the budget does not lower the band further, ratios of at most 0.5 that it falls further with the iterations) reads
1.028 and 1.024 of the 9000 L row's values over 1000 L to 9000 L (16875 x 512 and 22500 x 384) and 1.015 in C at the
axis, so the further budget does not lower its far band; within 0.5 of P it reads 0.612 and 0.578 and in J 0.579 (857
labels, eps 0.03, at 16875 x 384) of the 9000 L row's. Against X3 it reads 0.401 and 0.395 within 0.5 of P and 0.645 and
0.756 in whole-box N_f for r <= 1000 (on the same configurations) and 0.380 in J (eps 0.03); it has 41500 iterations
beyond X3, on other rows, so this is not an equal-budget comparison. X3 continued for 20750 iterations on its own rows
reads 0.993 to 1.003 of X3's over 1000 L to 9000 L and 1.0026 of X3's C at the axis. X3 continued for the same
iterations on its own rows with the inverse domain and two-term closure moved to 1e4 L (not a candidate) separates the
other two: the larger inverse domain with its closure, at the same rows and iterations, lowers the band to 0.27 of X3's
(0.266 to 0.273 on the two configurations, with and without the y-axis columns) and removes C at the axis (-0.024 of
X3's); the rows to 9000 L lower it by a further factor of 9 to 10 (the 9000 L row reads 0.10 to 0.11 of this
continuation there); C at the axis is already removed by the inverse domain (-0.024 against 0.035 for the 9000 L row).
Its interior is that of the budget row (same rows and iterations, inverse domain at 1000 L) to 2 percent in the
whole-box maximum and within 0.5 of P and to 8 percent in J (0.89 at 10 <= r <= 100 on one configuration). So the
further iterations alone do not move the band, and the fall of the 9000 L row is not attributable to its rows alone.
Under a termwise differentiable far-field expansion rho = r^k Theta_0 (1 + r^(k-1) Theta_1 + ...) (formal; a compact
change of the core adds multipoles that enter only at relative order r^(-4)), the equation determines Theta_1 from
Theta_0: with psi = r^(k+1) F the homogeneous inverse of r^k Theta_0, (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k
F' Theta_0, and on the y-axis Theta_1 = -(k+2) V_r/(c_l - 1), V_r = -F'. The formula's Theta_1 is set instead by the end
slopes of its radial splines (4.2). On X3 the two differ by 4.08e-3 on the y-axis (-42.5561 against the forced -42.5520,
computed three times independently) and by at most 7.9e-4 for theta < 1.4 (between 1.4 and pi/2 the difference rises to
the axis value); on the seven fits measured the axis difference is 4.07e-3 to 4.31e-3 and the maximum for theta < 1.4 is
7.0e-4 to 1.44e-3. This term alone gives R / N_v -> C r^(k-1) / (1+k) with C = (c_l - 1)(Theta_1 forced - Theta_1 of the
formula) = 0.0187 on the axis, 2.9e-6 at the band maximum, where the measured value is 1.1e-6 with the same sign. The
expansion of the trial to third order, computed three times independently and agreeing to 4 digits or more, gives next
to the y-axis (theta 1.568)
    R / N_v = 0.01582 delta - 88.78 delta^2 + 782.1 r^(-2) + 1.190e5 delta^3 + ...,   delta = r^(k-1);
these four terms give 1.26e-6 at 4700 L and 0.965e-6 at 9500 L against the measured 1.09e-6 and 0.945e-6 (measured /
series 0.59, 0.87, 0.98 at 3000, 4700, 9500 L; inside 2000 L the series is of no use). With the trial's velocity
computed to 1e7 L, the measured R / N_v from 3e4 L to 3e6 L equals the series plus the constant (c_l
k - 1)/(1+k) = -5.2e-10 (c_l the identity value of that inverse) to 1e-3 relative, next to the y-axis and at theta 0.82
(on the verifier's evaluator, which resolves this to about 1e5 L, to 2e-3 at 3e4 and 1e5 L); next to the axis its ratio
to the leading term is 0.92 at 1e5 L and 0.97 to 0.98 at 5e5 L (on the verifier's evaluator on the column 1.5634; its
columns within 0.006 of the axis are not resolved there), as predicted before those radii were evaluated. Off the axis
the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly (1.05 to 1.08 at 5e5 L
with c_l = 1/k). So the band is the sum of inconsistencies of the trial's far field at first, second and third order
(1e-4 relative in Theta_1; next to the y-axis, where the band maximum lies, 0.9 percent of the balancing terms at second
order and 22 percent at third order) and of the r^(-2) terms of 4.2, which are fixed by k, L and the end values b_m(1),
T(1), so that no choice of the end slopes removes them. Next to the y-axis the first- and second-order terms cancel at
the band maximum (2.81e-6 and -2.80e-6 at 4860 L), where the r^(-2) and the third-order terms give 5.7e-7 and 6.7e-7 of
the series sum 1.24e-6 (measured 1.10e-6); all four decay at infinity, the first-order one slowest. The inconsistencies
are common to the fits with rows to 900 L and the inverse domain at 1000 L (at second and third order 0.88 to 0.92
percent and 22 to 23 percent next to the y-axis on six fits); on the 900 L rows with the inverse domain at 1e4 L (C
-0.024 of X3's) they are 2.6e-6, 0.10 percent and 13 percent at orders 1, 2, 3. On the 9000 L domain row C at the axis
is 6.5e-4, 0.035 of X3's (V_r(pi/2) is unchanged, so the formula's Theta_1 moved toward the forced one), and the
inconsistencies at orders 1, 2, 3 next to the y-axis are 3.0e-6, 0.15 percent and 10 percent; its r^(-2) term is X3's,
its second-order coefficient 0.17 of X3's and its third-order coefficient of the opposite sign. At 4858 L next to the
y-axis its four terms (8.8e-8, -4.6e-7, 5.7e-7, -1.9e-7) sum to -2.5e-9, and on six columns within 0.072 of the y-axis
its measured R / N_v at 1000 L and 4701 L is -0.29 to +0.04 times its own first-order term (-0.30 to +0.15 over 11-node
radial windows around those radii; separate evaluator, formula continued): its band value is set by the higher orders,
and its fall is not the removal of the first-order term alone. So the 900 L fits' band value is not a floor of the
family; whether the remaining inconsistencies are is not established. The weighted identity R8 with phi = sin(3 theta)
r^(-3) holds on the candidate and on its control to a relative defect of 1.4e-9, and its integrand per unit log r decays
with the exponent 2k - 2 = -1.6413 of the far-field model (slope -1.64136 over the last decade, deviation 8e-5; the
decade deviations fall by the factor 10^(1-k) of the relative r^(k-1) correction). Inverse. At 52 sample points the
velocity of X1 (lead modal inverse on r <= 76520 with the two-term exterior) differs from the canonical inverse of X1's
density, computed by a third evaluator by real-space quadrature of the analytic source to |Y| = 1e18 (quadrature rules
clustered at P), by 8.4e-10 within 0.5 of P, 4.0e-8 within 0.5 to 2.5 of P, 6e-12, 5e-11, 1.0e-9, 4.6e-9 and 1.4e-8 at
r = 0.1, 1, 20, 100 and 300. The implied change of the normalized residual is at most 6.3e-10 within 0.5 of P and 2.8e-9
at 0.5 to 2.5 from P (median over the points 2.8e-11), against X1's residual maxima within 0.5 of P of 6.8e-7 (N_f) and
1.9e-7 (N_v). The same check on the free fit with 375 x m <= 100 functions (51 points, converged across three angular
rules and two ray rules, and confirmed at three points by a separately written modal inverse of an external referee)
gave the same pattern: 9e-10, 4e-8, 1e-9, 5e-9 and 1.5e-8 in the same regions and at most 3e-9 in the normalized
residual. "Converged" at r >= 100 means that the quadrature rules clustered at P agree with a 16384-angle midpoint rule.
These are sampled comparisons, not uniform bounds. X1 has the radial basis and c_l of the candidate and a lower angular
cap. The same check on the candidate X3 (52 points, the same export convention and quadrature rules) gives 1.0e-9 within
0.5 of P, 3.6e-8 at 0.5 to 2.5 from P, 7.7e-12, 5.1e-11, 9.8e-10, 4.9e-9 and 1.5e-8 at r = 0.1, 1, 20, 100 and 300; the
implied change of the normalized residual is at most 8.6e-10 within 0.5 of P and 2.6e-9 at 0.5 to 2.5 from P (median
2.7e-11), against X3's residual maxima within 0.5 of P of 6.5e-7 to 7.2e-7 (N_f) and 1.8e-7 to 2.0e-7 (N_v) (4.4). The
fit's own velocity (the inverse on r <= 1000 L with the two-term closure beyond) changes X1's residual by at most 5.1e-9
in N_f within 0.5 of P and 2.0e-8 in N_v for r < 1000, and X3's by the same to two digits (grid maxima; 4.4); at the 52
sampled points of X3 the same replacement changes the velocity componentwise by at most 9.2e-8 within 2.5 of P and
3.1e-6 at r = 300, with a frozen-denominator impact of at most 2.0e-9 within 0.5 of P, 3.1e-9 at 0.5 to 2.5 from P and
1.4e-8 at r = 20 to 300. Manufactured test of the separate evaluator: on rho = x^2 y e^(-r^2) with its closed-form
stream function and c_l = 1.3 (an arbitrary value) it gives max |R - R_exact| = 6.8e-10, 2.7e-12 and 2.8e-13 at 400, 800
and 1600 radial points (max |R_exact| = 0.485), max |E| at most 1e-10 and psi_xy(0) - 1/8 = -6e-14. The residuals of 4.3
and 4.4, except the domain columns read in each fit's own convention (4.4), are canonical residuals of the trial: the
verifier's evaluator generates rho from the formula and inverts it to 1e6 L.

### 4.6 Independent discretization
An independent discretization (polar Chebyshev-Radau x Fourier on a disk r <= R with the homogeneous far-field
extension, oversampled least squares with exact Jacobian and QR steps, c_l eliminated through the identity) did not
reach the standard. Its full-plane inverse was validated against the compactified Poisson inverse of the same workstream
(itself exact to 3.4e-15 in the rescaled stream function and 2.1e-14 in the velocity on the manufactured psi = x y (1 +
r^2/L^2)^((gamma-1)/2) (1 + 0.7 (x^2 - y^2)/(1 + r^2)), gamma = 0.6, L = 1.3, with N = 128 radial and 16 angular nodes
per quadrant): relative velocity difference on r <= 5 of 1.0e-6, 5.3e-8 and 2.2e-9 at R = 100, 300 and 1000, psi_xy(0)
to 3e-7, 2e-8 and 7e-10; its Jacobian agrees with finite differences to 5e-9 to 4e-7 relative per column. Between its
nodes its states satisfy the profile equation to a normalized residual of about 1e-6 rms away from P in its own
normalization; on the separate evaluator the maxima at 10 < r < 100 are 3e-5 to 6e-5 in N_v (4e-5 in N_f) for its free
iterates and 1.1e-5 to 1.2e-5 in N_v (6e-6 to 7e-6 in N_f) for its fixed-c_l states. Next to P its maxima are 9e-6 to
1.2e-4 in its own normalization (shell rms 3e-6 to 2e-5). The grids go up to 384 x 96 (unclustered) and 256 x 128
(clustered at P). At that level c_l is weakly constrained. The least first-order residual cost of a unit change of c_l
is 1e-3 to 6e-5, falling with resolution faster than the residual floor. On the clustered 256 x 64 grid, over 5.52 to
5.71 no fixed-c_l fit is worse than the one at 5.5763 by more than a factor 1.5 in its L2 residual or 1.3 in its near-P
maximum, and those above 5.5763 are better (near-P maxima from 3.0e-5 to 8.7e-6 across the range); its L2 residual is
flat to 20 percent over 5.556 to 5.596 and over 5.60 to 5.70. On the unclustered 320 x 80 grid the L2 minimum is near
5.575 and the fit at 5.68 is 25 percent worse; on the clustered 256 x 128 grid the L2 residual falls by 19 percent from
5.556 to 5.596. The discrete L2 minimizer moves by about 0.06 between grids, the zero of h(P) - 1 by 0.1 to more than
0.16. Free iterations, which use different weights and domains and are not one constrained family, drift between 5.29
and 5.59. Extra rows (h(P) = 1, characteristic matching, axis transport, a Taylor patch at P) do not change this.
Levenberg-Marquardt solves of its equations (identity row, c_l free), started from an early trial of the global trial
construction (c_l 5.5763) projected onto its grids, end at c_l between 5.5728 and 5.5823 on grids 128 x 32 to 320 x 80
with R = 1000 to 10000 (one run at R = 30000, marked unreliable there for its radial resolution, is not included),
without convergence under refinement; this is a variant spread, not an error bound. That workstream attributes the
spread to a nearly free far-field direction; the attribution rests on one singular-value computation of that workstream
and is not independently verified. The Gauss-Newton tangent prediction of the exponent step and its residual projection
diminish across the tested discretizations (+0.42 and 26 percent, +0.052 and 18 percent, +0.034 and 5 percent, at near-P
maxima 4.7e-5, 2.4e-5, 1.5e-5). This is a tangent prediction, not a stationarity test, and the nonlinear preferred
exponent of that discretization is grid dependent at the attained residual level. Its exported soft direction, added to
the 302-function trial along a fixed, unrefitted line that is linear in rho, is registered at offsets of 1e-3
(characteristic defect) to a few 1e-3 (near-P maximum). These are upper bounds on the cost of the offset, and the line
is a first-order statement beyond 1e-3. The result is a resolution statement: a least-squares residual of 1e-5 to 5e-5
next to P does not fix c_l to better than about 0.05 to 0.1 in that discretization. It neither establishes a competing
profile nor excludes one near 5.60 to 5.64, and it does not independently confirm the candidate's c_l nor its field at
the 1e-6 level. Its fixed-c_l states at 5.556 to 5.596 include the candidate's 5.5754 and its control's 5.5764 and do
not discriminate between them.

### 4.7 Adversarial checks
Hidden wall conditions: none (full-plane modal Green function, checked against (V2) and a real-space quadrature).
Harmonic gauge: excluded by (V3); c = psi_xy(0) is computed, not fitted. Parity: by construction, machine precision. The
x^2 y jet: a(0) = 1 by construction; centre relations (relative |E_c|, |D2| <= 6e-9 on the candidate, 4.2). Zero state:
excluded by a(0) = 1. Polynomial states: every polynomial density of the normalized class has total degree d >= 3, and
its supremum over the circle |X| = r is comparable to r^d, so it violates the bound |rho| <= C (1 + |X|)^(1/c_l),
1/c_l < 1, of R2; the trial has the leading homogeneous degree k = 1/c_l = 0.179 (4.2). Forgotten far-field terms: the
residuals are those of the canonical velocity of the trial density inverted to 1e6 L (4.4); the far-field residual
beyond the fit rows is measured and expanded term by term in 4.5, and the fits' two-term exterior closure is compared
with the formula continued in 4.4. Finite-box artifacts: the domain columns of 4.4 (closed problems on smaller and
larger fit domains, each with a further iteration budget, and the same fits read under the canonical law) and the
far-field and inverse checks of 4.5. Independence of c_l: 4.3.

### 4.8 Limits
Numerical evidence only. The residual values are maxima over sampled grids, not certified suprema. Neither the existence
of a nearby exact P_2 profile, nor its two-dimensional regularity class, nor a nonzero B_3 for it has been proved.
Residual tests cannot decide B_3; the B_3 value is an estimator value on approximate profiles of one lineage. Two
measurements of B_3 on the trial differ: the estimator from its axis data gives about 0.30, and the trial's own
coefficient of y^3 |x|^(p_3) is +0.046 (4.1); the difference is carried by the trial's defects in the y and y^3
coefficients of the equation on the x-axis, so the trial's own fractional term (+0.046) is about one sixth of the value
its axis data indicate. Both are positive. The trial's own regularity (H and a in C^(4,beta)_loc, rho_h in
C^(6,beta)_loc) follows from its explicit formula (4.1). Every fit has a sharp change of the third derivative of log a
across the characteristic leaving P (about +0.12 at P by separate polynomial fits on each side, changing sign near
height y = 0.5 and reaching about -0.4 at y = 1; on the candidate, its control and X1 by one estimator: +0.11 to +0.12
at P, -0.43 to -0.35 at y = 1; on earlier fits other estimators gave 0.05 to 0.16 at P). The fits are C^6, so this does
not show that a solution fails to be C^3. Under a conormal expansion along that characteristic with a nonzero linear
onset of the amplitude at the axis, a nonzero layer |x - gamma(y)|^lambda has exponent lambda = rho_y(P)/(2 c_l - 1),
about 2.93, and transverse regularity C^(2, lambda - 2), but no finite third-derivative jump (its third derivative
behaves like |x - gamma(y)|^(lambda - 3)). By an external referee's computation, not re-derived by the verifier, on a
regular positive branch its two amplitudes share a positive transport multiplier, so the nonzero leading layer
coefficient seen by a fixed estimator keeps its sign. The observed finite-window sign change does not establish such a
leading coefficient and does not exclude a layer in an exact solution; whether a solution has one is open, and all fits
share one lineage. The candidate was selected by rules that compare residual maxima of fits (rule (1) within
equal-budget pairs, rule (2) across the kept fits, which are at different budgets). In N_f the maximum sits next to P;
in N_v it sits in the far field beyond the inverse domain, where the fits with rows only to 900 L listed in 4.5, other
than F1 and W1, read 1.08e-6 to 1.17e-6; the domain row fitted to 9000 L reads 3.0e-8 to 3.2e-8 over 1000 L to 9000 L
(4.5). The ratios of the pair X3 / F3 read by the selection rule are 0.935 to 0.938 in whole-box N_f, 0.937 in J, 0.935
to 0.987 in N_v for r <= 1000 (y-axis floor columns excluded in N_f and N_v; without the exclusion 0.83 and 0.825 at
16875 x 768), 0.960 to 0.973 in L2 and 1.000 to 1.003 in the far field. X3 is limited by its iteration budget: continued
on its own rows for a further 20750 iterations it reads 0.61 to 0.74 in whole-box N_f, 0.50 to 0.54 within 0.5 of P and
0.48 in J (4.2), and at that budget the m <= 250 row reads 0.97 to 1.00 in whole-box N_f (both maxima are the lobe value
above P, common to X3 and the two rows within 4 percent over four radial sampling phases), 0.63 to 0.82 within 0.5 of P
and 0.74 in J of that continuation (4.4); beyond r = 1000 neither changes N_v by more than 1 percent. So its maxima are
values reached at that budget and cap, not converged values for the basis. X1 has a maximum next to P 4 to 6 percent
below the candidate's at 16875 radial points and equal to it at 22500, with N_v for r <= 1000 2.8 times and J twice the
candidate's. So the choice of the representative value inside the interval depends on the norm, on the band and on the
iteration budget, not on a property of the equation. On the m <= 150 basis the fixed-c_l fits below X2's c_l down to
5.5604082 have smaller L2 objectives and residual maxima than X2 at the same budget, the fit at 5.5524653 a smaller L2
objective but larger residual maxima, and the fit at 5.5683739 has whole-box and near-P maxima below the candidate's at
16875 x 512 (4.1) although its angular cap is lower. The requirement of the standard that c_l be stable holds for the
fitted values along each construction (the free c_l moves by less than 1e-5 over 20750 iterations), not for the exponent
of an exact profile: at equal budget, from transplanted starts, the L2 objective is least at 5.5604082 among the tested
exponents and the residual maxima at 5.5683739. A test fixed before the run at 5.6004662 was to separate two pictures: a
family of P_2 profiles through the free fit parametrized by c_l, and one isolated profile whose linearized operator has
a small singular value in the c_l direction at the resolutions used. Its ratio of objectives to F2 (2.036) would have
favoured the second picture at 2.96 or more and the first at 0.91 or less (thresholds from the ratios 1.97 and 1.36 of
the 244-function fit at 5.60 to its free fit); it does not separate them. At the attained resolution the residual pins
c_l only weakly; whether P_2 contains a family through the candidate or an isolated profile is open. One refinement step
of the experiment that would separate the two was done: the fits at 5.6004662 and 5.5683739 were continued from the
m <= 150 basis to the candidate's m <= 200 basis as X2 was continued to the candidate (4.3). By a rule fixed before the
runs, the ratio Q of the objective at 5.6004662 to F3's would have favoured the second picture at 3.05 or more (1.5
times its ratio 2.036 on m <= 150) and the first at 1.36 or less (2.036 / 1.5), provided the fit had flattened; it is
1.680, between the thresholds, so this step does not separate them either; the rule assigns no reading between the
thresholds, and the decrease from 2.036 to 1.680, one step, is read neither as evidence for either picture nor as a
trend. At 5.5683739 the continued fit, at the candidate's iteration count, has a smaller L2 objective than the candidate
(ratio 0.820, against 0.771 for the same fit to X2 on m <= 150), a smaller N_f within 0.5 of P (0.59 times on both
configurations) and a smaller J (0.56 and 0.55 times at eps 0.03 and 0.01); its whole-box N_f is 1.32 times the
candidate's at 11250 x 384, at the under-resolved off-axis lobe, and 0.69 times at 16875 x 512 (4.1, 4.3). Further steps
(more nested discretizations at several separated exponents, budgets large enough to estimate the optimization error)
were not done (section 5).

## 5. Reproducibility
The accompanying artifacts are arranged in six parts, (a) to (f); the file README.md at their top level lists the
directories of each part, maps the names of the fits used here (X1, X2, X3, F0 to F3, the rows of 4.3 to 4.5) to the
coefficient files and gives the commands below with paths relative to the artifacts. The records of the research run
itself (work logs, job drivers and queues, per-run solver logs) are not included.
(a) Trial coefficient files. One file per trial named in section 4: the candidate X3 and every fit of the tables of 4.3
    (the nested pair included), the free fit of the same trial space, the resolution rows at the candidate's c_l, the
    free resolution study (215, 244, 302, 375 radial functions with m <= 100, 375 with m <= 150), the soft-direction and
    fixed-c_l studies (with the two continued fits of the fixed-c_l profile, 4.3), the budget row, the m <= 250 row, its
    free control and its continuation with rows to 9000 L (4.4), X3 continued with the inverse domain at 1e4 L (4.5),
    and the bounded-domain fits with the free control of the 9000 L row and the 9000 L row continued (4.4, 4.5). The
    candidate X3 is c6g_shape.npz (md5 15f8095f7e79dbfa0c50d75e5fe8997a) and its control F3 is c6gF_shape.npz (md5
    0398af3f08a2a4f75e42c846edbaa375). A file holds the spline knots and order, the coefficient of every
    radial x angular function, the fractional-power coefficients, k = 1/c_l, L, c_l and the origin radius. The files of
    the candidate, its control, X2, F2, F0, F1, X1 and the start of X1 are the verified files byte for byte; in the
    other files a solver restart vector that no evaluator reads was removed for size, every other field unchanged (the
    md5 of each file as published and as verified is listed with them). Start files of continued fits are not included:
    the m <= 200 starts are the m <= 150 ends with the new angular coefficients set to zero, and the shifted starts are
    made by the transplant scripts of (b). The generator that evaluates rho, psi, U and the residuals from a
    coefficient file is in the same part.
(b) The fit: the Gauss-Newton / LSQR solvers (free and fixed-c_l), the GPU driver and the scan and export programs.
    The solvers log the objective, c_l, h(P), x*, centre jet E_c and D2 at each check; these run logs are not included.
    The fits X2, F2, X3, F3, the m <= 100 rows, the domain columns, the free control of the 9000 L row and the 9000 L
    row continued (4.5), the budget row, the m <= 250 row, its free control and its continuation with rows to 9000 L
    (4.4), X3 continued with the inverse domain at 1e4 L (4.5), the fixed-c_l profile with its two continued fits and
    the nested pair of 4.3 were computed with the same iteration, and the solver-setting arms of 4.2 with their stated
    changes, with the matrix-vector products, the vector updates of LSQR and the column-scaling probes carried out on a
    GPU, the products by a port of the CPU operator. Every table of the port is copied from the CPU objects. On the full
    fit grid it agrees with the CPU operator to 3e-14 relative in the products and 1e-13 in the adjoint products. The
    linearization, the acceptance test at each check (the CPU objective) and the saved coefficient files use the CPU
    code. Started from the same shape, the first linearization reproduced the CPU objective to 5e-5 relative after 250
    iterations. LSQR paths differ at the 1e-4 level after hundreds of iterations, so "equal budget" means equal
    iteration counts at the same relinearization schedule on the same backend (on the GPU 2500 iterations per
    linearization, damping 1e-8, check every 250), with two departures. On the CPU X1 ran 750 iterations over two
    linearizations (500 + 250) and F1 750 iterations in one linearization (--inner 2500), both stopped by the 1.8 h cap;
    the pairs X1 / F1, and through their starts X2 / F2 and X3 / F3, are therefore equal in iteration count but differ
    in the relinearization schedule of their first 750 iterations. The fits of the fixed-c_l profile of 4.3 are compared
    with X2 and F2 at equal total count: each runs 21500 iterations on the GPU, while X2 and F2 are the 750 CPU
    iterations of X1 and F1 followed by 20750 on the GPU. The CPU logs record under "predicted" the LSQR estimate
    |phibar|, which omits the damping term. The linear residual of the damped problem is sqrt(phibar^2 + res2), with
    res2 the sum of the squared damping rotations; the GPU logs record that value for every run from F2 on (the log of
    X2 has |phibar| only). The acceptance test always used the true objective. In each linearization the three long-fit
    drivers (long_solve.py, long_solve_fixcl.py and gpu_long_solve.py) scale the LSQR columns by the inverse square root
    of a stochastic estimate of the squared column norms of the Jacobian from 24 Rademacher probe vectors (seed 8128
    plus the linearization count); a column whose estimate is below 1e-18 of the largest gets scale 0 and is not moved
    in that linearization, and with c_l held fixed the column of k = 1/c_l gets scale 0 in every linearization. Every
    residual quoted is evaluated from the saved files by the evaluators of (c) and (d).
(c) The lead's between-node evaluation (scans by radial band and strip, both normalizations; the scan program
    quick_scan.py is with the fit code of (b)), the characteristic-defect code and the original-form B_3 evaluator, with
    their outputs for every trial of (a) (the larger outputs xz-compressed); and the far-field diagnostic of 4.5 (the
    forced and the stored first far-field correction from a coefficient file, on seven fits and on the domain fit with
    rows to 9000 L, with its outputs).
(d) The separately written generator and residual evaluator (own differentiation, own full-plane inverse), its audit
    wrappers and auxiliary scripts, the far-field checks of 4.5 (far1_ver.py, far2_ver.py, farP.py), the reference
    outputs of steps 1 and 2 below on the candidate (runs/reference), and the verification record that the appendix
    summarizes, copied after its last entry.
(e) The independent discretization of 4.6: solver, report; and the velocity check of 4.5 by real-space quadrature of the
    analytic source (52 sample points), with its outputs.
(f) The specification of the problem classes and diagnostics, the analysis notes behind section 3 with their audit
    record, and the external referee questions and answers (including the answer on the far-field identity of 4.5).

Reproduction of the headline numbers. All commands are single-threaded on the CPU (OMP_NUM_THREADS=1; the GPU driver of
step 5 also uses one GPU), with the software versions of section 0 (Python 3.9.25, numpy 2.0.2, scipy 1.13.1, and
PyTorch 2.8.0 for the GPU driver); the times are on one core of the machine used for the run. The wrappers of steps 1
and 2 stop a step after 2400 s (vaudit.py in gen_audit.sh) or 1200 s (mk_traces.py, vd14.py and vzeros.py in
extra_checks.sh), so a slower machine may need larger limits. Peak resident memory of the commands of steps 1 to 3 on
the candidate: 13.8 GiB for gen_audit.sh at 16875 x 768, the configuration with the most evaluation points (12.3 GiB at
22500 x 512, 9.2 GiB at 16875 x 512 and at 22500 x 384, 7.0 GiB at 16875 x 384, 4.7 GiB at 11250 x 384), and at most 7.5
GiB for each command of steps 2 and 3. They ran under an address-space limit of 15.3 GiB (ulimit -v 16000000), and every
output for which an earlier one exists equals it in every number (file names and timings aside): for steps 1 and 2 the
earlier outputs are in runs/reference of (d), for step 3 they are the candidate's scan files in (c). Step 1 at
16875 x 384, which section 4 does not use, had no earlier output; runs/reference holds the one from this measurement.
<coef> is a coefficient file from (a), <tag> any label. Paths in the commands are relative to the named directory of the
accompanying artifacts.
1. Residual tables of 4.4 by the separate evaluator (maxima of R/N_f and R/N_v by region, J, h(P) - 1), in the code
   directory of (d):
     bash gen_audit.sh <coef> <tag> "7.652e-4 7.652e6 11250 384 479;7.652e-4 7.652e6 16875 384 479;7.652e-4 7.652e6 16875 512 639;7.652e-4 7.652e6 16875 768 959;7.652e-4 7.652e6 22500 384 479;7.652e-4 7.652e6 22500 512 639"
   Each group is one configuration (inner radius, outer radius R of the inverse, radial nodes N, angular nodes, maximal
   mode); 2 to 8 minutes each. Output: runs/audit/<tag>_N<N>_q<nq>_R<R>.json and .log in (d).
2. Identity c_l = (1 + psi_xy(0))/3, the identity-free root of h(P) = 1 at fixed rho, the centre relations E_c and D2,
   and the zeros of W on the axes, same directory:
     bash extra_checks.sh <coef> <tag> "7.652e-4 7.652e6 11250 384 479"
   about 2 minutes; output runs/audit/<tag>_extra.log. The verifier's B_3 estimator on the traces this step writes:
     python3 vb3ibp.py ../runs/gen4/<tag>_traces.npz
   (the wrapper deletes the generated field and keeps the traces).
   The characteristic defect on the 857-label set of 4.4b and the axis integral I(eps) with the profile q0, same
   directory (the generated field is 52 MB and is deleted afterwards):
     python3 gen_shape.py <coef> 7.652e-4 7.652e6 16875 384 ../runs/gen4/<tag>.npz
     python3 vaxis.py ../runs/gen4/<tag>.npz 479 ../runs/audit/<tag>_ax.json
     python3 vchar_dense.py ../runs/gen4/<tag>.npz 479 20 737 60 1e-4 ../runs/audit/<tag>_jd2.json
   about 7 seconds, 2 minutes and 6 minutes; the arguments of vchar_dense.py are the maximal mode, the label radius, the
   number of uniform labels, the number of labels next to each axis and the smallest geometric distance from the axis.
3. The lead's scans, in (b) with the generator of (a) on the path:
     python3 quick_scan.py <coef> 32768 640 out.json
     python3 quick_scan.py <coef> 24576 960 out960.json
   under 30 seconds each on the candidate. They read the trial in its fit's own convention (the two-term closure at
   1000 L, 4.4) and on the candidate print whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P (4.1).
4. The lead's characteristic defect (185 uniform labels, a cross-check of step 2) and the original-form B_3 from an
   export (the export is about 1.4 GB and is not included; it is regenerated): with <name>_shape.npz in the working
   directory of (b),
     python3 export_fit.py <name> 24576 576
     python3 char_defect.py <name>_fields.npz 20 185
     python3 b3_ibp.py <name>_fields.npz mu1only
   (char_defect.py and b3_ibp.py are in (c)); on the candidate the export took about 80 seconds, b3_ibp.py under 15
   seconds and char_defect.py with 185 labels about 30 seconds. b3_ibp.py prints two forms per variant: "orig", the
   original form of R10, which is the lead value quoted in section 4, and "ibp", an integration by parts whose end piece
   does not converge in the quadrature order n (it moves by about +0.008 from n 40 to n 80 on the candidate); the "ibp"
   values are not quoted.
5. The fit itself, from its start file (the free fit moved by -1e-3 in c_l along its soft direction, also in (a)):
     python3 long_solve_fixcl.py <start> <out> --fix-cl --nr 20480 --nt 720 --hours 1.8 --inner 500 --check 250
   The free control F1 is segment 2 of the free run, from the free fit:
     python3 long_solve.py <free fit> <out> --nr 20480 --nt 720 --hours 1.8 --inner 2500 --check 250
   Both were stopped by the 1.8 h cap after 750 iterations, X1 over two linearizations (500 + 250) and F1 in one.
   The continuations X2, F2, X3, F3 use the GPU driver of (b):
     python3 gpu_long_solve.py <start> <out> --nr 20480 --nt 720 --hours 4.9 --inner 2500 --check 250 --fix-cl --max-its 20750 --damping 1e-8
   (--nt 960 for X3 and F3; without --fix-cl for F2 and F3). X2 and F2 were run with --hours 0.75 and no --max-its; the
   time cap stopped both at the check after 20750 iterations, the schedule that --max-its 20750 reproduces. The m <= 200
   starts are the m <= 150 ends with the new angular coefficients set to zero (make_angular.py in (b); the density is
   unchanged, residual difference 1.5e-15). The domain columns of 4.4 are the X3 end continued with the same driver and
   settings at --nt 960 with --fit-radius 90 or --fit-radius 300, and at --nt 960 on a 24576-point radial grid with
   --fit-radius 9000: the rows are then r < fit radius (in units of L) and the inverse domain is the fit radius / 0.9,
   with the two-term closure beyond; without the option the rows are r < 900 L and the inverse domain r <= 1000 L.
6. The velocity check of 4.5, in (e): an export of the coefficient file with the generator of (a)
     python3 export_fit.py <name> 24576 576
   (about 80 seconds; it writes <name>_fields.npz, regenerable and not included), then
     python3 raycheck.py cand <name>_shape.npz <name>_fields.npz out.json "Smax:1e18,smode:adapt,phimax:0.02,pcluster:1" full
   (about 32 minutes on X3 for the 52 points). It prints, per point, both velocities, their difference and the implied
   change of the normalized residual.
7. The far-field diagnostic of 4.5, in (c), with the generator of (a) on the path:
     python3 far1_axis.py <coef>            (axis limit of the forced and the stored first correction; seconds)
     python3 far1.py <coef>                 (the angular profile of both; seconds)
     python3 far1_check.py <coef> <export>; python3 far1_split.py <coef> <export>   (comparison with an export of step 6)
     python3 far2.py <coef>                 (the third-order series of R / N_v and its sums at the radii of 4.5; about 1 minute)
   and the measured far residual against that series, with the inverse continued to 1e7 L, run in the directory of the
   domain-fit code of (b) with ptest.py taken from (c) (it writes an export and deletes it afterwards; about 3 minutes):
     python3 <dir of (c)>/ptest.py <coef> 24576 576 1e7 out.json
   and, in the same way, the far-band maxima of |R| / N_v over 1000 L < r <= 9000 L, 9000 L < r <= 1e4 L and r > 1e4 L,
   with the inverse computed to <Rinv> L and the two-term exterior beyond (1e4 is the own convention of the domain fit
   with rows to 9000 L, 1e6 continues the formula; a cross-check of the band rows of 4.5 from (d); about 80 seconds, 4.8
   GB):
     python3 <dir of (c)>/band_nv.py <coef> 24576 576 <Rinv> out.json
Outstanding experiment (partly done). One refinement step of the experiment that would separate the two pictures of 4.8
was run: the fixed-c_l fits at 5.6004662 and 5.5683739 continued from m <= 150 to m <= 200 (4.3, 4.8); by the rule fixed
before the run its result is undecided (Q = 1.680 against the thresholds 1.36 and 3.05), so the two pictures are not
separated. Further nested discretizations at several separated exponents, with budgets large enough to estimate the
optimization error, were not run. The other rows of the fixed-c_l profile of 4.3 are on one basis (375 x m <= 150) at
one budget (21500 iterations), and the angular sequence m <= 150, 200, 250 at the candidate's c_l mixes approximation
and budget.

## Appendix. Verification timeline
UTC times; entries before the first dated break are on 2026-10-17. Each entry
records a check or audit as it happened; later entries supersede earlier readings where they say so. Notation is that
of section 4 (the conventions before 4.1). In the entries from 10:51 to 12:26 of 2026-10-18 "the candidate" is
X1, the fixed-c_l fit then under test; from the 16:44 entry of that day on it is X3.
- 17:54 specification v1 written (class, velocity law, lemmas).
- 18:00 to 18:05 verifier audit of specification v1: sound, one formula error in the far-field tail (corrected).
- 18:10 external referee audit of specification v1 received: velocity law confirmed; the proof of one lemma repaired,
  another lemma strengthened; the rigidity lemma replaced by an explicit form; the regularity lemma qualified.
- 18:13 specification v2 (all corrections).
- 18:21 to 18:28 verifier audit of specification v2 and of the analysis notes, sections 1 to 4: all confirmed, with one minor
  repair in the velocity bound; the 2D regularity statement is open.
- 18:45 external referee audit 2 received: positivity argument correct with a repair on the y-axis; the finite-part
  formula for B_3 is conditional on smooth axis data; a numerical defect in the B_3 tool found and fixed.
- 18:49 verifier audit of the first version of the report: only audited claims present.
- 19:22 external referee audit 3 received: closed-form B_3 formula correct with repair; Lemma R11 correct, its use for
  sequences conditional; B_3 has no sign from local axis constraints.
- 19:46 verifier audit (hand rederivation, numerical checks) of the positivity repair, the axis constraints, the
  closed-form B_3 formula, Lemma R11 and the no-sign result: all confirmed with the stated conditions.
- 20:10 verifier pre-candidate checks of the first trial fields of the global trial construction: whole-box residual,
  normalization and parity checks; acceptance list for a candidate agreed (section 4 standards).
- 20:51 verifier audit of the trial construction's final fit: the trial is reproduced by separately written code (its
  generator, inverse, residual evaluator and the identity for c_l); not at the YES standard (residual next to the
  source point, centre jet defect growing under refinement, no second solver).
- 21:28 verifier evaluation of the w-only finite part B_3 on the trial (end-treatment dominated spread).
- 22:02 verifier: plain dynamic rescaling from the trial does not settle (unstable linearized flow); the numerical
  workstream's reproduction is not at the standard; the integrated-by-parts form of the B_3 formula confirmed (with the
  condition 2/(2c_l - 1) not a positive integer); the rule for an explicitly distinguished finite-regularity problem
  agreed with conditions.
- 22:21 verifier: the characteristic defect J of the trial (section 4) recomputed with separate code; values confirmed.
- 22:28 verifier rulings on the standard: a second converged solver is desirable, not required; the independent check is
  the verifier's own residual evaluator on the exported density, the identity for c_l, and one determination of c_l that
  does not use the identity; c_l is quoted with its spread over constructions, which is not an error bound.
- 22:30 verifier hand audit: if rho is C^1 near the source P, W is C^2 there with A = d_x W_1(P) > 1, and rho_y(x,0) > 0
  on (0, x*) (true in P_2 by the axis equation w g' = (1 - h) g of R10; without it the statement fails, e.g. W = (2 xi,
  eta/3), rho = eta^3 in linear coordinates (xi, eta) at P; added 2026-10-18 after an external referee), then h(P) = 1
  and rho is a multiple of the linearizing coordinate eta near P (consistent with R5 and R6 of section 3).
- 22:34 verifier audit of an earlier version of this report: sections 0 to 3 confirmed; one inconsistency in the class
  statement found (resolved 23:43).
- 22:42 verifier audit of the centre-corrected trial: the centre jet defect reduced to about 1e-7 relative, confirmed on the
  export; the residual next to P unchanged; improvements measured only on a fitting grid are not accepted until
  reproduced on an export.
- 22:51 verifier: R/rho at P equals h(P) - 1, so J is reported by distance shells from P.
- 23:16 verifier: the headline "YES, strong numerical evidence, for the explicitly distinguished problem P_2" is
  admissible, under four stated conditions (definition where first used; existence near the trial is the numerical
  claim; P_2 consistency checks reported; uniqueness not claimed).
- 23:36 verifier recomputation of the residual by region and of J by distance shell on the centre-corrected trial:
  confirmed; the residual next to P (1.2e-4 in N_f) remains the obstacle to the standard.
- 23:43 verifier audit of section 1 (definition of P_2): confirmed, with one wording correction (applied).
- 2026-10-18 00:00 verifier evaluation of the locally refined trial between fit nodes (three resolutions, two inverse
  domains, own generator and evaluator): near-P residual lower by a factor of about 7 than on the centre-corrected
  trial; the characteristic defect J falls together with it, as expected for a representation limit;
  still above the standard (1.8e-5 in N_f, 5.1e-6 in N_v near P).
- 00:10 verifier: the method of the bounded-domain fits (equation fitted only inside a fit radius, two-term exterior
  closure outside) reproduced in the verifier's own generator; numbers preliminary.
- 00:14 verifier hand rederivation of the far-field closure error of a disk model (error in c of order R^(2k-2) with a
  one-term exterior and R^(3k-3) with two terms, conditional on the far-field expansion); the verifier's own inverse
  follows the R^(2k-2) law, and its values of c_l and h(P) at the largest domain are converged in domain to about 1e-9.
- 00:16 verifier: along the locally refined fit, c_l rose by 3.4e-5 while the near-P residual fell by a factor of 7;
  the argument that c_l is insensitive to the near-P defect is a heuristic, not a bound.
- 00:20 and 00:51 verifier audits of earlier versions of this report: confirmed, with one wording note; fits closed by
  an exterior expansion are only C^1 across the closure radius and are quoted as bounded-domain fits, not as admissible
  trials.
- 00:45 verifier audit of the domain series (fit radii 200, 300 and 900 shape units): c_l agrees to 1.5e-6 across the
  fit domains at that fit stage and the near-P residual is that of the best trial to 10 percent, but the series does not
  contain the best trial (a fit of the global formula on one domain); standard not met.
- 01:02 verifier: continuing the fit on a fixed radial basis (215 functions) lowered the residual away from P (band
  10 <= r <= 100 from 4.8e-6 to 2.9e-6) but not the near-P maximum (1.86e-5).
- 01:10 verifier map of the near-P residual: it sits on the refined-knot ring 8.2 <= r <= 9.4 near the slow curve above P
  and changes sign from one radial knot interval to the next, with its angular content inside the angular cutoff; read
  as a radial representation error at the knot scale (a numerical reading, to be tested by refinement).
- 01:14 verifier: fits whose c_l differ by 3e-5 have the same near-P residual and differ by a smooth global
  deformation; the spread of c_l over fits (about 3e-5) measures reproducibility, not an error bar (if the exponent is
  unique, one of two such fits is off by at least half the spread); a bracketing test (two starts, same basis, grid
  and budget) requested.
- 01:33 verifier check of an external referee's answer on counting conditions for the linearized problem: an index
  count that treats the linearization as transport plus a compact perturbation is not justified (the velocity term is
  of order zero with nonzero symbol on the transverse covector); whether the normalized profile is isolated is open.
- 01:41 verifier intermediate check of the fit with halved knot spacing near P (244 radial functions) part way through
  a fit segment: near-P maximum lower by a factor of 5.5 and the J spread by 4.5, together; the residual just outside the
  refined band unchanged. Intermediate, not a candidate.
- 01:43 verifier audit of the first-order analysis of the c_l error of a trial (the error is the residual weighted by a
  dual solution, under an unproved invertibility hypothesis for the linearized problem): confirmed as a heuristic, with
  one precision in the decay hypothesis at P (a Hoelder rate, not o(|X - P|)).
- 02:17 verifier audit of an external referee's corrections to a heuristic on why c_l is weakly determined: the
  proposed mechanism (a cheap residual for a shifted exponent) holds for frozen transport only, the nonlocal velocity
  feedback contributing a term without the 1/T decay of the transport term (T the cutoff time of that heuristic); the
  proposed estimator of the c_l error from the characteristic defect is wrong as stated (counterexample); its
  replacement, the Gauss-Newton exponent step of the least-squares problem,
  estimates, to first order, the least-squares minimizer of a trial basis in c_l, not the exponent of the profile; at
  a least-squares floor the residual rises only quadratically along the soft direction. Confirmed, with the condition
  that the six-digit c_l is never quoted without the statement that the spread of fits is a reproducibility number.
- 03:17 verifier audit of the trials with 244 and 302 radial functions after one fit segment each, evaluated between
  the fit nodes with an independent inverse at three resolutions: the measured residuals were confirmed (302 functions:
  flux-normalized maximum 2.3e-6 for 2 <= r <= 100, velocity-normalized maximum 1.4e-6, h(P) - 1 of order 1e-8). The
  reading that the near-P residual is a radial knot-scale error was confirmed for the stem component (the residual in the
  ring 8.2 <= r <= 9.4, 0.1 <= theta <= 0.5 above P) and refuted for the near-P maximum as a whole: on the 302 basis
  that maximum sits in a strip next to the x-axis whose angular content is at the edge of the trial's angular space.
  Neither trial meets the residual standard.
- 03:17 verifier audit of the lead's B_3 estimator: its integrated-by-parts end piece is not converged in the
  quadrature order (the increments grow by a factor about 3 per doubling, explained by a non-integrable remainder); the
  original form is converged to 5e-4 and agrees with the verifier's estimator, B_3 about 0.30 on the three latest bases.
  Values from the unconverged form were withdrawn.
- 03:45 verifier evaluation of fixed-c_l states of the independent discretization over c_l 5.52 to 5.71: at their
  residual level next to P (15 to 60 times that of the 302-function trial) a c_l change of 1e-2 is not detected; every
  near-P diagnostic improves monotonically toward larger c_l in that discretization, a property of its error at P and
  not evidence for a larger exponent.
- 04:34 verifier evaluation of the 302-function trial plus multiples of a fixed c_l direction, not re-optimized: an
  offset of -1e-4 is not detected by the residual for r <= 1000 or by the characteristic defect J (within 4 percent);
  only h(P) - 1 (3.5e-7) moves. At +1e-4 the characteristic defect J is 1.74 times larger. So six-digit c_l values are
  not determined by the residual at that level and any quoted uncertainty is at least 1e-4; along this direction the
  near-P maximum doubles between offsets 1e-3 and 3e-3 (upper bounds on the cost, since nothing was re-optimized).
- 04:56 verifier audit of the trial with 375 radial functions after one fit segment, between the fit nodes: the radial
  step 302 to 375 lowers the band 10 <= r <= 100 by a factor 2.9 to 8.0e-7 and does not lower the near-P maximum
  (2.44e-6, up 7 to 9 percent) or the far-field velocity-normalized maximum (1.46e-6); J did not fall. Not at the
  residual standard.
- 04:56 verifier evaluation of the 244-function trial moved along its optimized soft c_l direction (offsets 1e-4 to
  3e-3, linear tangent shapes, not refitted): at offset -1e-3 every between-node maximum is within 0.76 to 1.06 of the
  fit and |h(P) - 1| = 3.4e-8, so c_l is not determined to 1e-3 at that level. The diagnostics prefer different sides:
  the near-P maximum and J fall toward lower c_l, the linearised least-squares step points to higher c_l.
- 05:06 verifier evaluation of the independent discretization at a doubled angular resolution: three of its near-P
  diagnostics (h(P) - 1, the maximum within 0.5 of P, J at 0.01) now prefer smaller c_l, the reverse of the 03:45
  entry, which confirms that the preferred side at that residual level is a property of that discretization.
- 05:09 verifier audit of the lead's analysis of the soft direction (cost per unit c_l at most 3.58e-3 on the 244
  basis): the facts were confirmed; the claim that the Gauss-Newton exponent step grows like the inverse cost was
  refuted (it is not converged); the reading "the objective resolves c_l only at the 1e-2 level" was refuted: the
  linear model doubles the objective only beyond 8.9e-3, but the measured second-order term doubles it along the tangent
  shapes at about 4.1e-3, and the minimum of a fixed-c fit can only be lower. A third reading was added (the
  second-order term, not the linear one, may pin c_l).
- 05:16 (addendum 05:24) verifier evaluation of the 302-function trial plus multiples of the optimized 244 soft
  direction (field level, not refitted; between-node resolution N 16875, offsets 0 and -1e-3 repeated at N 22500):
  every diagnostic stays within 30 percent of
  the fit for offsets -1.5e-3 to +3e-4 (c_l 5.57486 to 5.57666, |h(P) - 1| <= 4.5e-8); no offset up to -3e-3 or +1e-3
  is excluded. The lower bound on the c_l uncertainty at the 302 level is 1e-3 (lower side 1.5e-3, upper side 3e-4).
- 05:28 verifier check of the start of a fit with c_l held fixed at 5.60 (offset +2.4e-2) on the 244 basis: the start
  objective is dominated by the second-order term of the tangent law (intermediate check, no reading).
- 05:35 verifier audit of the entries 04:34 to 05:16 and of the lead's account of the soft-direction intervals: confirmed
  with wording corrections (applied); both interval widths, 1.3e-3 (244) and 1.8e-3 (302), are lower bounds, and
  nothing shows that the width shrinks with the basis.
- 05:53 verifier evaluation of the trial with 375 radial functions after one fit segment, plus multiples of the
  optimized 244 soft direction (field level, not refitted; between-node resolution N 16875, offsets 0, -1e-3 and -1.5e-3
  repeated at N 22500): at offset -1e-3 (c_l 5.57536) the global between-node maximum falls to 0.73 to 0.74 of the fit
  (1.8e-6 from 2.44e-6; it sits in the strip next to the x-axis left of P), J at 0.01 to 0.68 and the far-field
  velocity-normalized maximum to 0.96; only the bands 10 <= r <= 100 and 0.1 <= r <= 2 rise (by 3 to 16 percent, to
  values at least two times below the global maximum). So along this direction the c_l that minimizes the maximum norm
  of the residual lies about 1e-3 below the least-squares value 5.57636. The lower bound on the c_l uncertainty at the
  375 level is 1.5e-3 below and 3e-4 above the fit value, as at 302; no offset from -3e-3 to +1e-3 is excluded. A
  field-level statement; 1.8e-6 is not at the residual standard.
- 05:53 verifier audit of the trial with 375 radial functions and angular modes up to m = 150 after 500 iterations of its
  first fit segment (intermediate): every band away from P falls (10 <= r <= 100 by a factor 1.8 to 2.2, the far-field
  velocity-normalized maximum to 1.14e-6, the plane rms by 2.1), while the strip next to the x-axis left of P stays at
  2.40e-6 and remains the global maximum, and J from all start angles rises by a factor 2.1 to 2.5 through
  characteristics that start next to the axis. Intermediate, no reading. (The sentence first written here, that the strip
  is not an effect of the angular truncation, was refuted at 06:54.)
- 06:17 verifier check of the soft direction carried exactly into the coefficients of the 375-function trial (a line in
  the trial class, not refitted): the carried direction is the 244-level soft direction as a function on the plane to
  3e-4 relative. Along this line the global between-node maximum is smallest at -1.5e-3 (0.71 of the fit), flat to 4
  percent over -2e-3 to -1e-3; J is smallest at -1.5e-3 (0.64); the least-squares objective is smallest at about +5e-4.
  The field-level line of the 05:53 entry agrees with it at -1e-3 and is a first-order statement only beyond 1e-3.
  Unrefitted lower bound on the c_l uncertainty at the 375 level: 2e-3 below and 3e-4 above the fit value. The same
  field-level test on the trial with angular modes up to m = 150 (iterate 500): the strip moves with c_l as before;
  the global maximum falls by 23 to 25 percent at -1e-3 to -1.5e-3.
- 06:18 verifier check of the proposed account of the independent discretization (section 4.6): confirmed with
  corrections; one sentence (fixed-c_l fits over 5.52 to 5.71 "equally good to 20 percent") refuted as worded. The
  corrected text, with the grid qualifier of 06:56, is the one in section 4.6.
- 06:33 verifier audit of the trial with 375 radial functions and angular modes up to m = 150 after its first fit
  segment (750 iterations): c_l from the identity 5.5763624; |h(P) - 1| <= 1.7e-7 at the largest box (between-node N 11250 to 22500); global between-node
  maximum 2.28e-6 to 2.44e-6 in the strip next to the x-axis left of P, 2.44e-6 converged in the between-node grid
  (06:54), equal to the m <= 100 trial; plane rms 0.44, band 10 <= r <= 100 0.58 and far-field velocity-normalized
  maximum 0.77 (1.12e-6) of the m <= 100 trial, but J 2.2 to 2.7 times larger (3.1e-6 at 0.03). Centre jet, the single
  stagnation point on the x-axis, no other zero of the field on the evaluation grid and the lower bound on |W| / (c_l
  |X|) confirmed as for the m <= 100 trial. The starts of the fixed-c_l fits at -1e-3, -3e-3 and -1e-2 (this trial
  plus the carried direction, not refitted) have global maxima 0.94, 1.44 and 6.0 of the fit; the c_l identity holds
  on them to 3e-7.
- 06:54 verifier audit of the strip next to the x-axis left of P on the trials with angular modes up to m = 100 and up to
  m = 150: the between-node maximum of the m <= 150 trial converges to 2.44e-6 in the between-node grid (as for m <= 100).
  Next to the axis the residual oscillates in theta at a local frequency close to the angular cap of each basis (n 186
  to 196 in sin(n theta) for m <= 100, 264 to 306 for m <= 150). Raising the cap from 100 to 150 lowers the normalized
  residual next to the axis by 2.3 to 4.8 times farther than about 0.3 from P and leaves its maximum unchanged; the
  maximum moves toward P. The exponent content added by the cap step is confined to theta < 0.08, has the same angular
  profile at every r from 7.6 to 8.56, grows toward P and changes sign at P; the angular spectrum of the exponent there
  decays algebraically. So the strip is an oscillation at the top of the angular basis and it also moves with c_l. The
  value h(P) - 1 = 2.8e-6 in the characteristic-defect output was an interpolation error; on the exported axis trace
  h(P) - 1 is at the 1e-8 level.
- 06:56 verifier check of the section 4.6 paragraph, version 2: confirmed with one correction (the comparison of fixed-c_l
  fits over 5.52 to 5.71 holds on one grid of the independent discretization only; the replacement sentence is in 4.6).
  06:58 the numerical researcher confirmed version 2 against the records of the independent discretization.
- 07:11 verifier check of the fit with c_l held fixed 1e-3 below the free fit (c_l 5.5753626, 375 radial functions,
  m <= 150) after 250 iterations (intermediate): global between-node maximum 1.50e-6 (2.43e-6 for the free fit, same
  between-node grid), still in the strip, now 0.07 from P; J 1.5 times lower; the L2 objective 15 percent higher; h(P) = 1
  to 2e-8 at both c_l values; the bands away from P unchanged to 10 to 15 percent. Not yet a c_l effect: the fixed fit has
  250 more iterations than the free fit; the control is the free continuation at the same iteration count. The standard
  (about 1e-6 including next to P) is not met.
- 07:45 verifier check of the same fixed-c_l fit after 500 iterations (intermediate): global between-node maximum
  9.84e-7 in the finest configuration, J 1.35e-6 at 0.03 and 1.58e-6 at 0.01.
- 07:59 verifier check of the domain study. In the convention of each fit (closure at the fit's own inverse radius)
  the trials fitted to radii 900, 300 and 100 shape units agree inside their fit radii: maxima next to P 2.44e-6,
  2.63e-6 and 2.54e-6, c_l 5.5763622, 5.5763628 and 5.5763644, h(P) = 1 to 5e-8. Numbers computed with the fitted
  formula continued beyond its fit radius are not numbers of the fit and were not used in that check (the same fits
  read with the formula continued are reported in 4.4). The independent velocity check at 51 nodes was confirmed for
  the third quadrature configuration (agreement 1e-9 next to P and 5e-9 at r = 100).
- 08:32 verifier check of a structure shared by all fits at the source point P: the third derivative of log a changes
  sharply across the characteristic leaving P (about +0.12 at P on the x-axis, 0.05 to 0.16 depending on the
  estimator, decaying to 0 by 0.2 from P; off the axis the change follows the characteristic and changes sign near
  height y = 0.5). The fits are C^6, so this does not show that a solution fails to be C^3; whether a solution has a
  singularity there is open. The fits share one lineage, so the agreement between them does not separate a property
  of the fitted family from a property of a solution. The main deliverable does not depend on it.
- 09:05 verifier audit of the fit with c_l held fixed 1e-3 below the free fit, final state (750 iterations after the
  shift along the soft direction), in both normalizations at six evaluator configurations: whole-box maximum 6.5e-7 to 7.0e-7 in N_f, next to P
  (free fit 2.28e-6 to 2.44e-6); in N_v 1.13e-6 to 1.17e-6, in the far field next to the y-axis (free fit within 3
  percent), and at most 5.7e-7 for r <= 1000; J 1.0e-6 on 24 labels (free fit 3.1e-6; corrected at 10:51 below); identity c_l = (1 + psi_xy(0))/3 to 3.2e-9;
  h(P) = 1 at both c_l values to the evaluator's grid error. In the strip next to the x-axis left of P the fixed fit is
  lower by a factor 3.4 in both normalizations; next to the x-axis at r 2 to 6 it is higher by up to 26 percent. The
  fits differ in iteration budget, so the share of the difference due to c_l is open until the equal-budget free
  control. The criteria for a fixed-c_l candidate were confirmed with six amendments (equal-budget control, both
  normalizations and J, every fixed c_l tried listed, h(P) = 1 not used to select, resolution study with J, evaluator
  floor exclusions stated). The standard is not yet met: resolution and domain studies at the fixed c_l are pending.
- 09:14 verifier check of the inverse-error row (confirmed on the free fit with 375 x m <= 100 functions: velocity
  differences 9e-10 within 0.5 of P to 1.5e-8 at r = 300, impact on the normalized residual at most 3e-9) and of the
  effect of the fits' far-field closure (measured with the closure at 111 L and 333 L, the inverse radii of the fits
  with rows to 100 L and 300 L; the domain fits are tests of the closed problems, not residuals under the canonical
  velocity law). It also completed the selection rules for several fits
  (a free continuation's drift of c_l, the number of fits compared, the resolution and domain studies at the chosen
  fit's own c_l) and corrected an earlier version of this section in wording and numbers.
- 10:20 external referee audit of six analytic statements of section 4 received (the trial's regularity class, its
  far-field expansion, the limit of R/rho at P, the characteristic defect J, the exclusion of polynomial states, and
  the reading of the third-derivative feature at P): four correct with qualifications, now in the text (rho_h is in
  C^(6,beta)_loc and log a in C^(4,beta)_loc; J refers to transport by the frozen trial field and its spread over a
  fixed label set does not measure a common transport error); the polynomial-state sentence was wrong as worded and is
  replaced; the inference that the feature at P is not a single conormal layer was not justified and is withdrawn.
- 10:51 (addendum 10:53) verifier evaluation of the equal-budget free control (the free fit continued to the same 750
  iterations as the candidate) and of the characteristic defect on a resolved label set. The 24 labels used until then
  do not resolve J in the start angle; on 857 labels on r = 20 (737 uniform, 60 next to each axis) the candidate has
  J(0.03) = 2.74e-6 and J(0.01) = 2.68e-6 (1.91e-6 and 2.02e-6 on the 737 uniform labels), and every earlier 24-label J
  is a lower bound. The largest values come from labels whose characteristics run along the x-axis between the origin
  and P, where R/rho on the axis reaches 1.04e-5 on the candidate (8.0e-6 on the free control). At the equal budget the
  free control is lower in J and in the L2 objective, the candidate lower in the strip maximum (factor 3.4 in N_f) and in
  the far field in N_v; the two fits are not ordered, and the criterion for a fixed-c_l candidate (residual and J not
  higher than the equal-budget free fit) is not met at 750 iterations. Also confirmed: the six referee wordings of the
  10:20 entry as applied, and the effect of the fits' far-field closure (at most 1 percent of the residual next to P and 7
  percent for r < 1000, maxima over all grid points). The standard is not met. (Corrected by the verification entries
  of 12:09 and 12:26: the maxima of R/rho on the axis are 1.07e-5 on the candidate and 8.2e-6 on the free control, and
  the axis carries only the maximum at a label next to the y-axis; the other extremes take their J from the strip next to
  the x-axis and from the disc around P in comparable parts.)
- 12:09 verifier evaluation of the domain fits, a second fixed-c_l basis and the residual structure next to the x-axis.
  The fits on a domain cut to 90 L (free c_l) and to 300 L (fixed c_l), both at angular cap m <= 100, agree with the
  full-domain fits of the same basis by rules fixed beforehand. Their maxima next to P are 1.07 to 1.11 times those of
  the full-domain fits, the 10 < r < 100 band 0.71 to 0.95 times, and c_l moves by +4.9e-6 for the free fit. The 90 L
  formula continued beyond 90 L is not a solution there. At the fixed c_l, the step from cap m <= 100 to m <= 150 lowers
  every residual band and the spread of J (at unequal iteration budgets). Next to the x-axis, from r about 4 to P, the
  residual oscillates in the angle at the angular frequency of the basis cap. The axis quantities q0 and I(eps) are
  differences of band parts larger than themselves. A domain study at cap m <= 150 does not exist yet.
- 12:26 verifier evaluation of the free continuation of the candidate and of the origin of the J oscillation.
  - The oscillation of J in the start angle is carried by the residual at angular frequencies at or above the basis cap,
    on the candidate and on the m <= 100 fit. On the equal-budget free fit no single frequency band carries it.
  - On the radial nodes of a grid with spacing 0.012, |q0| reaches 1.3e-6 on [8, x*).
  - Continuing the candidate with c_l free for 1000 iterations moves c_l by +2.5e-6. It lowers the L2 objective by 12
    percent and J by 18 percent, and raises the maximum next to P by 1.5 times.
  - The two free fits are 1e-3 apart in c_l, and neither moves measurably toward the other at these budgets, so c_l is
    quoted as an interval of at least [5.5753, 5.5764].
  - A variant with extra weight on the axis between the origin and P failed: its maximum next to P was 6.5 to 7.7 times
    the candidate's.
- 13:41 verifier evaluation of the long continuations: the fixed-c_l fit and its equal-budget free control (the free fit at
  the same 750 iterations), each continued for 20750 further LSQR iterations on the same basis (angular cap m <= 150).
  - By the selection rule fixed before the runs, the fixed-c_l continuation is kept against the free one when the
    far-field band is read as all r > 1000 (inside the configuration spread there). Read over the band
    1000 <= r <= 7652 (1000 L) only, its far-field N_v is higher by about 3 percent, beyond the spread, and the free
    one would be kept. The lead fixed the band as all r > 1000 at 13:54, after these measurements, and both readings
    are reported (4.3).
  - The margins are small: 9 percent in whole-box N_f, 8 percent in J, 0.5 to 3 percent in the far-field N_v.
  - The fixed-c_l continuation halved the L2 objective and doubled the maximum next to P (N_f 6.5e-7 to 7.0e-7 before,
    1.4e-6 to 1.5e-6 after, ranges over the configurations). The free continuation lowered its L2 objective by 40
    percent and its maximum next to P from 2.1e-6 to 2.3e-6 down to 1.6e-6. The fixed-c_l fit before the continuation
    keeps the lowest whole-box N_f of the fits measured by then, with a higher N_v and a lower J than the continued
    one, so the fits are not ordered, and continuing on this basis gives no systematic improvement of the maximum
    residual. On both continuations the residual at the angular cap frequency sits next to the x-axis from r 7 to P.
  - On the fit before the continuation, at half the node spacing, |q0| reaches 1.3e-6 on [8, x*) and stays below 1e-6 on
    [8.4, x*).
  - Along the radial sequence of the free fits at m <= 100, the 857-label J falls from 1.9e-5 to 3.5e-6 and then rises by
    6 percent, to 3.7e-6; it is not monotone at the last step.
  - Neither a lower damping nor reorthogonalization lowered the objective by the 3 percent fixed beforehand, so the solver
    setting was kept.
- 15:31 verifier evaluation of the fixed-c_l continuation at angular cap m <= 200 (the continued m <= 150 fixed-c_l fit,
  enriched to m <= 200 with the new coefficients at zero and continued at the fixed c_l for 20750 LSQR iterations).
  - Whole-box N_f, N_v for r <= 1000 and the 857-label J fell by a factor of about 2: whole-box N_f 6.8e-7 to 7.2e-7
    (0.48 times the m <= 150 fit), N_v for r <= 1000 1.9e-7 to 2.0e-7, J 1.39e-6 (0.44 times). Not every band fell by
    that factor: N_v on the band 1000 <= r <= 7652 (1000 L) fell by 0.86, and the residual in the window y >= 1 above
    P changed by the ratios 1.01 and 0.81 on two grids. Beyond r 1000 the far-field N_v reads 1.09e-6 to 1.11e-6, 1 to
    2 percent lower than on the m <= 150 fit.
  - At equal budget (one linearization of 2500 iterations from the same start on each basis) the m <= 200 iterate is 0.71
    to 0.72 times the m <= 150 iterate in N_f and 0.62 to 0.69 in J on 185 labels (every fourth label of one family of
    the 857).
  - The residual at the angular cap frequency next to the x-axis moved to the band of angular frequencies 400 to 600, two
    to three times the new cap, with its peak at 399, at the lower edge of that band.
  - Next to the y-axis beyond r 1000 the residual is a residual of the fit, not the evaluator's floor, so the far band is
    read on all columns; the columns next to the y-axis are excluded only in the near field. At 11250 radial points an
    off-axis lobe is under-resolved, and whole-box N_f is read on the configurations with 16875 or more radial points
    (fixed at 15:54, before any row of the free control existed).
- 16:44 verifier evaluation of the equal-budget free control at m <= 200 (the continued m <= 150 free fit, enriched to
  m <= 200 and continued with c_l free for 20750 iterations), and the choice of the candidate.
  - By the selection rule fixed before the runs, the fixed-c_l fit is kept on every part and in every fixed reading:
    whole-box N_f 0.83 to 0.94 times the free control's (on the configurations with 16875 or more radial points),
    N_v for r <= 1000 lower, the far-field N_v equal to 3e-9 (inside the
    spread between configurations), 857-label J 0.94 times. By the second rule it becomes the candidate.
  - The free control's c_l moved by +2.2e-7 over its 20750 iterations, so the two fits stay 1e-3 apart.
  - B_3 on the candidate is 0.299 to 0.303 by the converged estimator forms. Values of the integrated form, whose end
    piece does not converge in the quadrature order, are not quoted.
  - On the x-axis |q0| on [8, x*) is at most 1.07e-6 on the candidate, the axis value of the ripple at the angular cap
    frequency.
  - The standard is not met yet: the domain columns at the candidate's basis, the angular row at m <= 100 and the
    report text are outstanding.
- 17:35 verifier evaluation of the first domain column: the candidate continued for 20750 iterations at the same c_l
  with residual rows r < 90 L and its own inverse on r <= 100 L with the two-term closure beyond.
  - By the domain rule fixed before the runs (the N_f maxima on 2 <= r <= 10 and on 10 <= r <= 100 within a factor 1.5
    of the candidate's, read two-sided, and |h(P) - 1| < 1e-7) it agrees on the lead's evaluator (2 <= r <= 10: 0.70
    and 0.73; 10 <= r <= 100: 0.82) and on two of the verifier's three configurations; on the third (16875 x 512) its
    2-10 maximum is 0.62 times the candidate's, outside the factor 1.5 on the low side. The verifier's ratios are
    1.04, 0.62, 0.72 on 2 <= r <= 10 and 1.02, 1.23, 0.83 on 10 <= r <= 100; h(P) - 1 = 5.6e-8 and 6.8e-10 on the
    configurations with 16875 or more radial points. (The verifier first read the rule one-sided and wrote "agree"; it
    corrected this at 18:42.)
  - Where it differs it is lower: next to P its N_f is 0.32 to 0.33 times the candidate's and the 857-label J 0.40
    times (eps 0.03; 0.37 at eps 0.01), while the lobe above P does not move (0.98). The column carries both a smaller
    domain and a further budget, so it does not separate the two; the 300 L column is the control.
  - With the formula continued beyond its fit radius instead of the closure, the 90 L fit has N_f about 3e-5 next to P
    and h(P) - 1 about -6e-5: it is a fit of the closed problem only.
- 17:50 the verifier confirmed from the code that the residual rows of every formula-global fit end at 900 L (the
  earlier version had said 1000 L), and that those of the earlier m <= 100 domain series end at 900, 300, 100 and 90 L.
- 17:59 to 18:25 far field of the trial (4.5). The verifier confirmed the identity
  (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k F' Theta_0 as formal algebra and, with its own inverse of Theta_0
  on the candidate, the axis values (forced -42.5520, stored -42.5561, C = 0.0187 on the axis); the external referee
  audited the formal orders, the formula side and the residual limit (correct, with the qualifications stated in 4.5).
  - Prediction fixed at 18:04, before the radii were evaluated: next to the y-axis the ratio of R / N_v to the leading
    term C r^(k-1) / (1+k) is within 0.15 of 1 at 1e5 L and closer at 5e5 L, and likewise at theta 0.82. Measured by
    the verifier in the formula convention to 1e8 L: 0.921 and 0.981 next to the axis, 1.111 and 1.046 at theta 0.82
    (with c_l = 1/k); confirmed, with the node scatter within 0.006 of the axis not resolving "closer" there.
  - Off the axis the ratio crosses 1 near 9500 L, overshoots to 1.15 to 1.18 at 3e4 L and returns toward 1 slowly; an
    earlier statement (18:13) that off the axis the leading term is reached inside 1e4 L was refuted and withdrawn.
- 18:25 the canonical-inverse check of 4.5 repeated on the candidate itself (52 points) was confirmed against the
  numerical workstream's tables: velocity differences 1.0e-9 within 0.5 of P, impact on the normalized residual at
  most 8.6e-10 there.
- 18:25 re-audit of the section 4 text: confirmed subject to eight wording corrections (C1 to C8), all applied; no
  number read by a selection rule changed.
- 18:33 the verifier confirmed the third-order series of R / N_v of 4.5 with its own code (written from the
  definitions, its coefficients equal to the lead's to 7 digits in the leading one): measured / series 0.59, 0.87,
  0.98 at 3000, 4700, 9500 L; on its evaluator the measured far residual equals the series plus the drift constant to
  2e-3 at 3e4 and 1e5 L (the agreement to 1e-3 out to 3e6 L stated in 4.5 is on the lead's evaluator).
- 18:42 verifier audit of the first port of section 4 into this report and of the first version of section 5: confirmed
  subject to corrections of the far-field paragraph and of four items of section 5, all applied; the reading of the
  domain rule was corrected to two-sided (17:35 entry).
- 19:03 verifier evaluation of the second domain column: the candidate continued for 20750 iterations at the same c_l
  with residual rows r < 300 L and its own inverse on r <= 333 L with the two-term closure beyond, the same further
  budget as the 90 L column.
  - By the domain rule, read two-sided, it agrees on the lead's evaluator (2 <= r <= 10: 0.74 and 0.72;
    10 <= r <= 100: 0.86) and on two of the verifier's three configurations; on the third (16875 x 512) its 2-10
    maximum is 0.62 times the candidate's, on the low side, as for the 90 L column: there both columns' 2-10 maximum
    is the lobe above P, which no column moves, while the candidate's is next to P. The verifier's ratios are 0.99,
    0.62, 0.74 on 2 <= r <= 10 and 0.89, 0.76 (0.79 with the columns next to the y-axis cut), 0.96 on 10 <= r <= 100;
    h(P) - 1 = 5.1e-8 and -3.1e-9 on the configurations with 16875 or more radial points. No domain column run by then
    (90 L, 300 L) is higher than the candidate by more than the factor 1.5 in the bands of the rule (largest ratio
    1.23).
  - Domain against budget: next to P the 300 L fit is 0.57 to 0.59 times the candidate's and its 857-label J 0.59
    (0.56 at eps 0.01), against 0.32 to 0.33 and 0.40 for the 90 L fit at the same budget. In the closed problems the
    near-P gain at that budget grows as the domain shrinks; the budget part for the full-plane problem is not measured
    by these columns.
- 19:10 verifier audit of this report's update: confirmed except two items, both corrected. The decomposition of the
  far-field band in 4.5 had omitted the third-order inconsistency, which next to the y-axis carries, with the r^(-2)
  terms, the band maximum where the first two orders cancel; the verifier withdrew its 18:33 confirmation of that
  sentence. A statement on the domain columns was restricted to the bands of the domain rule.
- 19:35 verifier evaluation of the angular row at the candidate's c_l: the fit with angular cap m <= 100 continued for
  20750 iterations at that c_l, read with the m <= 150 and m <= 200 fits (the last 20750 iterations of each at the
  fixed c_l) by the rule fixed before the runs (none of whole-box N_f, N_f within 0.5 of P, N_v for r <= 1000, N_v
  for r > 1000 and the 857-label J increases from one row to the next by more than the configuration spread).
  - For m <= 100, 150, 200 at 16875 x 512 (J at 16875 x 384): whole-box N_f 3.11e-6, 1.43e-6, 6.84e-7; N_v for
    r <= 1000 8.74e-7, 4.00e-7, 1.92e-7; N_v for r > 1000 1.325e-6, 1.11e-6, 1.10e-6; J 5.28e-6, 3.14e-6, 1.39e-6.
    Every quantity decreases at both steps on both configurations measured, the far-field N_v maximum at the last step
    by about the configuration spread. The m <= 250 refinement row has not run.
- 19:54 verifier evaluation of the radial companion: the fit with 244 radial functions at angular cap m <= 100,
  continued for 20750 iterations at the candidate's c_l, against the 375-function fit of the 19:35 entry. The
  375-function fit is lower in whole-box N_f (0.83 to 0.86 times), next to P (0.95), in N_v for r <= 1000 (0.83 to
  0.85) and in J (0.95); N_v for r > 1000 is equal within the configuration spread, and 6.4 percent higher at
  375 with the columns next to the y-axis excluded. No reading of this pair was fixed in advance; it is reported as
  data.
- 20:03 verifier audit of this report's updates from 19:10 on: confirmed except three items, all corrected: three
  values of the m <= 150 fit rounded up in the third digit, the last far-field step of the angular row described as
  smaller than the configuration spread (it is about equal to it), and the description of the two m <= 100 rows.
- 20:44 verifier evaluation of the domain row fitted to 9000 L (X3 continued for 20750 iterations at its c_l with rows
  to 9000 L and the inverse domain and two-term closure at 1e4 L; not a candidate), read by the rule fixed before the
  run and its addition fixed before the run. Interior: the domain rule holds except at one configuration, where the
  2-10 maximum is lower than the candidate's by more than the factor (0.66), the pattern of the other two domain rows.
  Far band: over 1000 L to 9000 L the N_v maximum falls to 0.028 to 0.029 of the candidate's on both configurations;
  beyond 1e4 L it falls to 0.035 with the formula continued, while the fit's own closure there reads 25 times the
  candidate's value. The first-order mismatch coefficient at the y-axis is 0.035 of the candidate's, and the second-
  and third-order coefficients changed with it (the second-order one to 0.17 of the candidate's, the third-order one
  to the opposite sign); the fall is not the removal of the first-order term alone. The candidate's far-band value is
  therefore that of the unfitted continuation of its formula. Whether the rows or the 20750 further iterations
  produce the fall is not separated by this row.
- 21:02 verifier audit of this report's text on the domain row fitted to 9000 L: confirmed except two items, both
  corrected: one sentence of the 20:44 entry as first written attributed the fall to the removal of most of the
  first-order inconsistency (the higher orders changed as well and set the row's band value), and one comparison of
  an implied velocity change normalized like N_v with the candidate's N_f maxima (its N_v maxima were added); two
  optional wordings were adopted.
- 21:24 verifier closure row measured directly on the candidate (two grids of the separate evaluator): the changes of
  the residual between the fit's inverse convention and the formula continued are those of the earlier row to two
  digits; relative to the candidate's band maxima they are 0.8 percent next to P and 1.5 percent at 2 <= r < 10, but
  22 to 47 percent in N_v at 10 <= r < 1000, so the earlier row's percentages do not transfer beyond r = 10; in
  section 4.4 the sentence carrying them over to the candidate was replaced by the candidate's own numbers, and the
  earlier row keeps its own percentages.
- 21:28 verifier audit of the corrected text of 21:02: confirmed; one rounding and two optional precision notes (the
  column range next to the y-axis, and the row values against their radial windows) were adopted.
- 22:24 verifier audit of the text of 21:24 and 21:28 and of the record of the later reading rules in the
  specification: confirmed; the record of one control's reading omitted that it holds on both configurations with
  16875 or more radial points and that the first-order far-field coefficient is computed as for the 9000 L row; both
  were added, with two optional precision notes.
- 22:28 verifier measurement of the m <= 250 refinement row (not a candidate): the row m <= 100, 150, 200, 250 meets
  the reading fixed before the runs; with the evaluation columns next to the y-axis excluded (shown there to be the
  evaluator's floor on two angular resolutions) its interior maxima are 0.33 to 0.74 times the candidate's and its J
  0.36 to 0.37, and beyond r = 1000 it is 0.23 to 0.44 percent above the candidate. The deliverable does not change.
  The row has 20750 iterations more than the candidate; its comparison at equal budget was open (23:07).
- 22:38 verifier audit of the text of 22:24 and 22:28: confirmed with four range or wording corrections (the far band
  of the m <= 250 row is 0.23 to 0.44 percent above the candidate's rather than within 0.4 percent of it; the
  agreement of the two angular resolutions next to the y-axis, the ratio to the candidate there, and the column of the
  far-band maximum), all applied; the centre values of the m <= 250 row were measured and are the candidate's.
- 23:07 verifier measurement of the budget row (the candidate continued 20750 iterations on its own rows; not a
  candidate): 0.61 to 0.74 of the candidate in whole-box N_f, 0.50 to 0.54 within 0.5 of P, 0.48 in J, unchanged
  beyond r = 1000 (within 1 percent). By the readings fixed before it ran, the far-band fall of the 9000 L row comes
  with its rows, the 300 L row's near-P gain is that of the budget, and the 90 L and 9000 L rows' ratios to it are
  stated; at equal budget the m <= 250 row equals the budget row to 3.2 percent at the lobe above P on the sampled
  grids (to 4 percent over four radial sampling phases, 23:35) and is lower next to P and away from P. Sections 4.2,
  4.3, 4.4, 4.5 and 4.8 were updated.
- 23:18 verifier audit of the text of 23:07: confirmed with two wording corrections (the lobe ratio 0.98 is at one
  radial sampling; the 90 L and 9000 L ratios lie outside the interval on all three and on two of the three
  configurations), both applied. The near-P maximum of the m <= 250 row on the first column off the x-axis was shown
  to be a value of the row (same sign and size on three angular resolutions), not an evaluator floor.
- 23:35 verifier scan of four radial sampling phases at 16875 x 512 for the candidate, the budget row and the m <= 250
  row: the lobe value above P is common to the three within 4 percent (the lobe maximum moves with the sampling by 9
  to 12.5 percent on each row, and lies about 4 percent higher, 3.7 to 4.5, at 22500 x 512); the near-P maxima are
  phase-stable for the candidate and the budget row (within 1 percent), and the m <= 250 row's narrow value on the
  first column off the x-axis varies by 21 percent, the unshifted grid giving the largest, so the near-P ratios stand.
  The whole-box maxima of the budget row and of the m <= 250 row are this lobe value. Sections 4.2, 4.4 and 4.8 were
  updated.
- 23:38 verifier audit of the text of 23:07 to 23:35: confirmed with two corrections (the lobe at 22500 x 512 lies 3.7
  to 4.5 percent higher, not 4 to 5; the raised cap lowers the lobe above P by at most 4 percent over the sampling
  phases, so the lobe is not unchanged by the cap), both applied.
- 23:41 verifier evaluation of B_3 along the rows (its estimator on axis traces from its own inverse; the lead's
  values were reproduced to all printed digits with the same code and traces, a reproduction, not an independent
  recomputation): the medians of the integration-by-parts form are 0.2985 to 0.3012 on the angular row m <= 100 to
  250, on the budget row and on the 9000 L row (original form 0.3002 to 0.3044; method spread within one row up to
  0.0035 and 0.015); each step along the angular row is within the method spread, and B_3 is about 0.30 on every row.
  Item (ii) and 4.1 were updated.
- 2026-10-19 00:16 verifier finding that the report gave normalized residuals only: the maxima of |R| itself by
  region, with the size of rho as a scale, and the absolute elliptic residual were measured and added to 4.4.
- 00:32 verifier audit of the text of 23:41 to 00:16: confirmed as to content, with two formatting corrections, one
  label (the far-band ratios of the angular row are over all evaluation columns), one sentence of the definition of
  the standard ("Absolute values are reported too") and one range ("to 6 percent"), all applied.
- 00:34 verifier check, item by item, of an external referee report on the text of 23:41: three conditions missing
  from statements of section 3 (the velocity bound of R1 holds for 0 < gamma < 1, the range used in R2; R7 and the
  parts of R10 with three y-derivatives need C^3 axis data; the limit statement of R11 needs a finite zero set of the
  limit field), one notation (|cos theta|), one missing quantity (the trial's own B_3 coefficient, +0.046 against the
  estimator's 0.30), a reading of the domain fits under the canonical velocity law (measured by the verifier), and
  wording items. None changes a number of the candidate or the choice of X3. Applied in sections 3, 4 and 5.
- 00:41 verifier measurement of the free control of the m <= 250 row (not a candidate): c_l 5.5763706 (drift -6.0e-7
  in 20750 iterations, toward the fixed value). Against the m <= 250 row the whole-box and r <= 1000 maxima agree to
  about 1 percent with differences of both signs inside the configuration spread, the free control is lower next to P
  and beyond r = 1000, the fixed row lower in J; by the selection rule the free control wins the pair on differences
  below the resolution of that maximum. Recorded; the deliverable does not change. With the columns next to the y-axis
  excluded the candidate's far band is 0.4 percent above its control's, about twice the spread between configurations;
  4.1, 4.3 and 4.4 were updated.
- 00:56 verifier audit of the candidate continued for 20750 iterations on its own rows with the inverse domain and
  two-term closure moved from 1000 L to 1e4 L (not a candidate; reading fixed before the run): over 1000 L to 9000 L
  its far band is 0.266 to 0.273 of the candidate's on both configurations with 16875 or more radial points, the
  branch "falls"; C at the axis -0.024 of the candidate's; its whole-box and near-P maxima are the budget row's to 2
  percent (J to 8 percent). Of the fall of the 9000 L row to 0.029, the inverse domain with its closure gives the
  factor 0.27 and all of C at the axis, the rows the remaining factor 0.10 to 0.11. This refines the reading of 23:07
  (the fall "comes with its rows"): the fall is not attributable to the rows alone. Two wording corrections of the
  prepared text, both applied; 4.1, 4.3, 4.4 and 4.5 were updated. It changes neither the candidate nor its interior
  values.
- 01:13 verifier diff audit of the report as revised at 01:01 (17 items): confirmed in content, with two corrections
  (the component tests quoted in 4.6 belong to the compactified discretization of the same workstream, replaced by the
  disk discretization's own validation; one range in 4.5) and one wording correction in 4.8; applied.
- 01:15 verifier reading of the fixed-c_l fit at d = -2e-3 from F0 on the m <= 150 basis (rule fixed before the run):
  L2 objective 0.926 of F2's, whole-box N_f 0.865 / 0.869, J 0.865 / 0.859, |h(P) - 1| <= 2.8e-7: "not determined at
  this level". It widens the quoted c_l interval down to 5.5743631. At equal budget the profile over d = -2e-3, -1e-3,
  0 is monotone in every measured quantity, so the lower end of the tested span is not bracketed by this fit; two
  fits further down were requested (4.3).
- 01:16 external referee audit of the identity relating the two B_3 measurements of a trial (4.1): with the function
  H of R10 the defect term combines the trial's defects in the y and y^3 coefficients of the equation on the x-axis;
  correct under conditions the trials satisfy (g > 0 on (0, x*], even expansions of g/x^2 and |w|/x at 0). The
  wording of 4.1, 4.8 and (ii) was corrected accordingly; no value changed.
- 01:38 verifier reading of the fixed-c_l fit at c_l 5.5783631 (d = +2e-3) from F0 on the m <= 150 basis: L2 objective
  1.078 of F2's, whole-box N_f 1.138 on both configurations, J 1.159, |h(P) - 1| <= 8.2e-8: "not determined at this
  level". It widens the quoted c_l interval up to 5.5783631. At equal budget every measured quantity increases with
  c_l over the four rows from 5.5743631 to 5.5783631 (4.3).
- 01:51 verifier diff audit of the report as revised at 01:22 (6 items, including the identity of the 4.1 remark and
  its conditions checked on the candidate's axis traces): confirmed.
- 02:45 verifier reading of the fixed-c_l fit at c_l 5.6004662 (d = +2.4e-2) from F0 on the m <= 150 basis: L2
  objective 2.036 of F2's, flattened (-0.49 percent over the last 1000 iterations), N_f within 0.5 of P 2.915 and
  2.914 of F2's: "excluded at this level". It does not widen the interval. The test of 4.8 fixed before the run (ratio
  to the free fit against the reference on the 244-function basis) is undecided at 2.036.
- 02:57 verifier reading of the fixed-c_l fit at c_l 5.5723653 (d = -4e-3): L2 objective 0.858 of F2's, whole-box N_f
  0.711 / 0.713, J 0.707, |h(P) - 1| <= 3.6e-7: "not determined at this level". It widens the quoted interval down to
  5.5723653; the objective still falls toward smaller c_l there, and the fit at d = -8e-3 was run (4.3).
- 03:11 verifier check of an external referee's reading of the fixed-c_l profile: at equal budget the free iteration
  did not move c_l toward the lower objective (its c_l stayed in [5.5763641, 5.5763716] over 20750 iterations), so
  F2's exponent is set by its start at this budget and is not a minimizer of the objective; the experiment that would
  separate a family of profiles from an isolated profile (fixed-c_l fits at separated exponents through nested
  discretizations) is not in the data. Two conditions for the endpoint followed: the wording of 4.1 (evidence
  consistent with existence; neither the proximity of an exact profile nor its exponent is established) and the
  statement in 4.3 that the fixed-c_l fits below F2's exponent reach lower objectives than F2 at equal budget. Both
  were applied; the missing experiment is named in 4.8 and section 5.
- 03:48 verifier reading of the fixed-c_l fit at c_l 5.5793640 (d = +3e-3): L2 objective 1.115 of F2's, whole-box N_f
  1.213 / 1.214, J 1.224, |h(P) - 1| <= 5.5e-8: "not determined at this level". It widens the quoted interval up to
  5.5793640, the largest value tested on the candidate's radial basis that is not excluded; the next value tested on
  it, 5.6004662, is excluded at this level (4.3).
- 04:01 verifier reading of the fixed-c_l fit at c_l 5.5683739 (d = -8e-3): L2 objective 0.741 of F2's, whole-box N_f
  0.566 / 0.427, J 0.388, |h(P) - 1| <= 4.5e-7: below the 30 percent band of the rule on the low side, so "undecided
  at this level" by its letter; it widens the quoted interval down to 5.5683739 and does not bracket the lower end. On
  16875 x 512 its whole-box and near-P maxima are 2 percent below the candidate's and its J is lower, on a smaller
  angular cap; the report does not say that the candidate has the smallest residual maxima among the fits computed.
- 04:03 verifier endpoint statement: the YES endpoint for P_2, as numerical evidence and not a proof, meets the
  standard as written, on conditions carried by the text: the wording of 4.1 and (iv) (the exponent is not determined;
  the interval and its lower end as measured), the statements of 4.3 on the fixed-c_l profile, the limits of 4.8 and
  section 5 (the family and isolated-profile pictures not separated), the status line and timing, the artifacts, the
  variant spread of the independent discretization (4.6), and a diff audit of the final version.
- 04:07 verifier location of the whole-box N_f maxima: within 0.5 of P at 16875 and more radial points on every
  audited fit except the fixed-c_l fit at d = -8e-3 (0.57 left of P on the x-axis side); at 11250 x 384 the candidate
  and that fit have it at the under-resolved off-axis lobe of 4.3.
- 05:03 verifier reading of the fixed-c_l fit at c_l 5.5604082 (d = -1.6e-2): L2 objective 0.643 of F2's, whole-box
  N_f 0.716 / 0.485, J 0.514, |h(P) - 1| <= 6.9e-7: "undecided at this level". It widens the quoted interval down to
  5.5604082. The L2 objective is below that of the fit at d = -8e-3, its residual maxima and J are above it, so the
  lower end is not bracketed; among the tested exponents the residual maxima are least at 5.5683739. Its residual
  maxima are above the candidate's on both configurations.
- 05:51 verifier reading of the equal-budget free control of the fixed-c_l fit with rows to 9000 L (a data row, not a
  candidate): its c_l moves by -1.5e-6 over 20750 iterations, its far bands are within 4 percent of the fixed-c_l
  fit's, and the fixed-c_l fit is 0.93 to 0.94 times it within 0.5 of P and in J, as the candidate is against F3
  (4.5).
- 06:06 verifier reading of the fixed-c_l fit at c_l 5.5524653 (d = -2.4e-2): L2 objective 0.775 of F2's, whole-box
  N_f 1.139 / 1.159, J 1.158; |h(P) - 1| is 1.46e-6 at 11250 x 384 and 2.6e-7 at 16875 x 512, so "undecided at this
  level" by the letter of the rule ("not determined" with h(P) at 16875 or more radial points). It widens the quoted
  interval down to 5.5524653. Its L2 objective and whole-box N_f are above those at 5.5604082, so the lower end is
  bracketed at this budget in the sense of fits from transplanted starts; that fit had not flattened, and its L2
  objective is below F2's while its residual maxima are above F2's (4.3).
- 06:23 verifier diff audit of section 4 with the fixed-c_l profile: every number confirmed; four wording
  corrections required and applied: the computation does not determine c_l (the tested exponents not excluded span an
  observed interval), the class statement aligned with 4.1, the stored exponents of the profile given to within 8e-7,
  and the selection rules stated with their budgets (4 (iii), (iv), 4.3, 4.8).
- 06:23 verifier check of an external referee's hostile audit of the 04:03 endpoint statement: its checkable
  claims confirmed. One clause of that statement was an overstatement: an attained objective bounds the objective
  minimized over shapes only from above, so the fits do not show that a computed c_l fails to minimize it; corrected
  to the wording of 4.3 ("set by its start, not by a minimum of the objective"). The artifacts did not yet contain the
  coefficient files and code of the GPU fits; they were added (section 5).
- 06:36 verifier diff audit of those corrections and of the suggested wordings (the scope of the table and the basis
  of the interval in 4.3, two statements in 4.4b and two earlier entries of this timeline): confirmed; no measured
  value changed. Check of the artifacts as then assembled: the coefficient files of the candidate and its control are
  byte-identical to the audited files, and from a copy of the artifacts the packaged evaluator and the lead's scan
  reproduce the recorded outputs on the candidate (every field identical except the timing and the file name).
- 07:12 and 07:16 verifier diff audits of presentation corrections (item references and point counts in 4.1, the
  wording of the P_inf clause (4.1) and of the domain ordering (4.4), the definition of equal budget and the column
  scaling of the LSQR iterations in section 5): confirmed with one correction, that the free control F1 ran its 750
  CPU iterations in one linearization, not two; applied. No measured value changed.
- 07:55 verifier reading of the nested pair: the fixed-c_l fits at 5.6004662 and 5.5683739 continued from the m <= 150
  basis to the candidate's m <= 200 basis at the candidate's iteration count. At 5.6004662 the L2 objective is 1.680
  times F3's, between the thresholds 1.36 and 3.05 fixed before the run, so the step is undecided and the family and
  isolated-profile pictures are not separated; its N_f within 0.5 of P is 2.41 and 2.50 times F3's, so it is excluded
  at this level as on m <= 150, and the interval is unchanged. At 5.5683739 the L2 objective is 0.820 times the
  candidate's, N_f within 0.5 of P 0.59 times and J 0.56 times; its whole-box N_f is 1.32 times the candidate's at
  11250 x 384 (the under-resolved off-axis lobe) and 0.69 times at 16875 x 512 (4.1, 4.3, 4.8).
- 07:57 verifier diff audit of that correction: confirmed; no measured value changed.
- 08:09 and 08:21 verifier diff audits of the nested-pair statements: confirmed with two corrections, applied: the
  upper end of the tested values not excluded is stated as a reading of tested values (on the candidate's radial basis
  the largest tested value not excluded is 5.5793640 and the next tested value, 5.6004662, is excluded), in item (iv)
  of section 4 and in the 03:48 entry; and one digit of a quoted maximum in the nested-pair table of 4.3. No other
  quoted value changed.
- 09:36 verifier reading of the 9000 L row continued for a further 20750 iterations at its c_l (a data row, not a
  candidate): its N_v maximum over 1000 L to 9000 L is 1.028 and 1.024 times that row's, in [0.8, 1.25] by the rule
  fixed before the run, so the further budget does not lower the far band; within 0.5 of P it is 0.61 and 0.58 times
  and in J 0.58 times that row's (4.5).
- 10:10 verifier reading of the m <= 250 row continued for 20750 iterations with rows to 9000 L and the inverse domain
  and closure at 1e4 L (a data row, not a candidate): whole-box N_f 1.02 times and N_f within 0.5 of P 0.67 and 0.71
  times the m <= 250 row's, so by the rule fixed before the run the interior gain of the cap is kept with rows to
  9000 L; over 1000 L to 9000 L its N_v is 0.61 times that of the 9000 L row continued for the same total iterations,
  outside [0.8, 1.25], so the ratio is stated; the difference sits next to the y-axis at the inner end of that band
  (4.4).
- 10:20 verifier diff audit of the statements on the two data rows: confirmed with one correction, applied (a clause
  on the far band of the m <= 250 row continued is replaced by the two maxima measured, 4.4); the statements of (iv),
  4.1 and 4.3 on the tested exponents and on the fits lower than the candidate checked over the whole text with both
  rows included. Two suggested wording changes applied: the rows continued beyond the candidate's budget that are
  lower in whole-box N_f are named in section 4, and the 13:41 entry reads "of the fits measured by then".
- 10:27 verifier diff audit of those changes: confirmed with one correction, applied (the sentence on the rows
  continued beyond the candidate's budget now gives the column convention and names all eight rows that are lower in
  whole-box N_f at the configurations with at least 16875 radial points).
- 10:29 verifier diff audit of that correction: confirmed.
- 10:30 verifier check of the accompanying artifacts against the report (interim): every file unchanged since the
  08:31 check, and the candidate's scan and residual audit reproduced from a fresh copy; for the final assembly it
  listed the coefficient files of the nested pair and of the two data rows with the log lines of their runs, the final
  copy of the verification record, and the fits to be named in section 5 (a).
- 10:42 verifier check of an external hostile-referee pass on the report: no sentence found that calls the numerical
  evidence a proof, claims convergence to an exact profile or a determined exponent, or says that X3 has the smallest
  residual; the headline numbers consistent. Three corrections required and applied: no definite article for an exact
  profile whose existence is not established (item (ii) of section 4 and 4.1), three upper bounds that had been
  rounded down (4.1, 4.5), and the far-field N_v range of 4.8 restricted to the fits with rows only to 900 L. Three
  recommended wording changes applied (4.1, 4.4b).
- 10:46 verifier check of an external reproduction from the accompanying artifacts: the md5 of the candidate and its
  control, the identity, the root of h(P) = 1, x* and the centre relations reproduced; the residual scans did not run
  under a 2 GB memory cap (a memory failure, not a disagreement; they ran and reproduced the stored outputs under the
  limits of this run). The exit statuses of two evaluator wrappers corrected (numerics unchanged). The software
  versions, the thread setting and the time limits of the wrappers added to section 5.
- 11:06 verifier reading of the fits at 5.5604082 and 5.5524653 on the m <= 150 basis, each continued for a further
  21500 iterations at its exponent (43000 in all): L2 objectives 2.2009e-6 and 2.2121e-6 (ratio 1.005), whole-box N_f
  1.167e-6 and 1.344e-6 at 11250 x 384 and 6.311e-7 and 1.301e-6 at 16875 x 512; by the rule fixed before the runs the
  lower-end bracket is kept at twice the budget. The L2 margin shrank at every linearization (from 5.63e-7 to
  1.12e-8), so the order in L2 is a fact at this budget only. Identity c_l to 3.2e-9 on both, centre relations and the
  condition (Hmin) of R9 checked. The fit at 5.5604082 is below the candidate in whole-box N_f at 16875 x 512 (0.922
  times) and in J (0.800); it is named in 4.1 (not an equal-budget comparison, not a candidate).
- 11:21 verifier diff audit of the presentation rounds and of the reading of the two continued lower-end fits:
  confirmed, with four corrections required and applied: 4.1 names the evaluator whose maxima the bounds 7.2e-7 and
  2.01e-7 are and gives what the lead's scans read in the fit's own convention (6.94e-7 and 7.27e-7 in N_f next to P;
  the same in section 5 step 3); the sentence on the shrinking L2 margin restricted to the complete linearizations;
  two ratios of 4.1 rounded correctly. The bounds 1.112e-6 and 1.324e-7 confirmed for both evaluators.
- 11:31 verifier measurement of the peak memory and wall time of the commands of section 5 steps 1 to 3 on a fresh
  copy of the accompanying artifacts, under an address-space limit of 15.3 GiB: 13.8 GiB for the residual tables at
  16875 x 768 (the configuration with the most evaluation points), at most 7.5 GiB for each command of steps 2 and 3,
  the stated wall times met, every output equal to the stored one. The memory statement added to section 5.
- 11:49 verifier measurement of the three remaining configurations of step 1 (16875 x 384, 16875 x 512, 22500 x 384):
  7.0, 9.2 and 9.2 GiB, the stated wall times met; the outputs at 16875 x 512 and 22500 x 384 equal the earlier ones,
  16875 x 384 had none. The reference outputs of steps 1 and 2 added to (d).
- 11:59 verifier final entry on the report of 11:50:47Z and the accompanying artifacts of that time: the endpoint of
  section 4 confirmed as meeting the standard, with all its stated conditions met.
- 12:04 end of the run (T_end). For publication the accompanying artifacts were reduced to the material the report
  relies on, under 50 MB: the run records (work logs, job drivers and queues, per-run solver logs) and the start files
  of continued fits were left out, the larger scan outputs were compressed, a solver restart vector was removed from
  the coefficient files other than the eight named in section 5 (a), directory prefixes of the machine were removed from
  the scripts and records, and a README with the map of fit names and the commands was added. Section 5 was adjusted
  to describe this. No number of sections 1 to 4 changed.
