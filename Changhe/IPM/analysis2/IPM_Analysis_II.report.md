# S1 theory report: a posteriori analysis of the full-plane IPM self-similar y-leading profile (case 4)

Status: PARTIAL. No existence theorem for an actual profile near the S1 numerical profile was proved, so the endpoint
was not reached. What was proved, and confirmed by an independent verifier: conditional a posteriori existence theorems
with explicit constants, the linear theory they need, and local exclusion theorems. For the reference cases whose
other hypotheses are verified below, the remaining condition is that the residual be small enough.

## Summary

THEOREM: proof audited and numbers recomputed by an independent verifier. FLOAT: never a bound. PROPOSED: unverified.

- Setting (THEOREM). F(rho; c_l) = (c_l X + U[rho]).grad rho - rho = 0, U[h] = (-R_1 R_2 h, R_1^2 h), rho even in x
  and odd in y. Reference: state 131, the last accepted checkpoint of the case 4 860-generator run, reconstructed
  exactly. c_l = 4076476460239181/2^51 = 1.8103192..., a_0 = d_y rho(0) = 10.3002948..., gamma = 1/c_l = 0.552388...
  The strain is c[h] = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h r^-3 dX. Every parity-class solution that is C^(1,a)
  at 0 with d_y rho(0) != 0 satisfies c_l + c[rho] = 1 automatically. The 860-generator family contains no exact nonzero
  profile, and the checkpoint residual grows: |F(X)| <= (48707/200000) |X|^(2 gamma - 1) for |X| >= 300.
- Linear inverse (THEOREM). L_fix h = V.grad h - h + U[h].grad rho, V = c_l X + U[rho], is bijective from its generator domain
  onto the Sobolev space X_U of order 2 + 1/32, with inverse norm 20 and ||h||_Hdot^-1 + ||h||_C^(1/64) + M(h) + |c[h]| <= 240 ||L_fix h||.
  Certified inputs include M >= (19/5) I (in fact M >= (c_l + 2) I, equality only at 0), A >= -I/20 and N <= I.
- Theorem D (THEOREM; N_s, s = 2^-18). Assume hypotheses (B0), (B0n), (B1) to (B5), (B7) and (B9c), all certified for
  state 131. If N_s(F) <= 1/1572864 (about 6.36e-7), there is exactly one h with N_s(h) <= 2^-16 and c[h] = 0 such that
  rho + h is an exact normalized solution with the same leading profile. It does not apply to the checkpoint. Its
  residual is not in N_s, and its residual sector r^q E with q >= -2 rules out every exact solution in checkpoint + N_s.
- Theorem D_w (THEOREM; weighted, admits residual growth r^q with q < 1/5). The threshold is N^w_s(F) <= 2^-35 at
  s = 3 * 2^-31 (ball 5 * 2^-32). A second version gives 2^-30 at s = 3 * 2^-21 (ball 5 * 2^-27). For the checkpoint,
  every hypothesis on the reference and the membership of its residual are proved.
- Logarithmic theorem (THEOREM). Gain Q = (1 + tau log(1 - Delta))^beta with 1/2 < beta <= 1 and tau = 2^-24. The
  threshold is M(F) <= 2^-25 tau^beta (2 beta - 1)^(1/2) < 2^-37, and the solution satisfies M(h) <= 32 times that.
  A parametric form leaves the third and fourth derivative bounds free. For the exact rational refit d2, every
  reference hypothesis of the parametric form is proved on the whole plane (caps 2^191, 2^201, Astar = 2^189,
  tau = 2^-210), and its residual lies in the space.
- Local exclusions (THEOREM; in the stated norms, not global nonexistence). No exact solution of any exponent lies
  within weighted distance 2^-14 of the checkpoint or 2^-9 of the refits Mpen2 and d2 (2^57 and 2^21 if R >= 2^31), or
  within native logarithmic distance 2^77/(2^20+7) and 2^41/(2^20+7). These balls contain the theorem balls.
- Certified numbers (independently recomputed): all constants above; N^w_s(F_131) > 3.53e25 for every R >= 2^31 and
  > 1.21e28 for every R >= 2^35; for the checkpoint residual, ||omega D^2 F||_2 = 25.189... and
  ||omega D^3 F||_2 = 2.5042...; the C^(1/2) inverse constant 87 of the frozen principal operator on its little Hoelder realization.
- Exact remaining gap (the first missing inequality is residual smallness). The checkpoint misses Theorem D_w by
  factors > 2^119 (threshold 2^-35) and > 2^114 (threshold 2^-30) at every R >= 2^31, and misses the logarithmic
  theorem by > 2^121. Mpen2 and d2 miss the logarithmic theorem by > 2^67. For d2 in the parametric form, smallness is
  the only failing hypothesis, and it fails by a factor > 2^243. Theorem D_w also requires, at every point, the
  necessary condition |F(X)| < min(2^-44 (1 + |X|^2/R^2)^(11/10), 2^-38 max(1, |X|)^(1/5)).
- The seven questions (section 2). (1) L2: yes as a linear estimate together with the Hdot^-1 level; the nonlinear
  D^3 U[k] obstruction is removed by a fractional estimate; residual size remains. (2) C^alpha: yes, with h as the
  unknown and Sobolev forcing ([grad h]_C^(1/64) <= 100 ||L_fix h||); the frozen principal operator has a C^(1/2) inverse
  with constant 87 on its little Hoelder realization; a global Hoelder-to-Hoelder inverse of L_fix is not proved (not needed). (3) c[h]: not from low
  norms; yes from the common high inverse, |c[h]| <= 40 ||L_fix h||; in H^(2+s) the loss s^(-1/2) is unavoidable.
  (4) Scaling: yes, eliminated by fixing c_l and the leading profile. (5) Far field: lower sectors determined exactly;
  exponent and leading angular data fixed, not free. (6) Combined inverse: yes, one bijection controls low norm, Hoelder
  norm, center moment and strain. (7) Existence: closes conditionally; no available residual is small enough.

## Run record

T0 = 2026-10-28T00:20:16Z (logged start). T_end = 2026-10-28T18:22:04Z, when the run was stopped at its time cap.
Elapsed time is 18 h 01 min 48 s, so the planned 18-hour window ran to its cap. The lead's actual working time was
four sessions totalling 17 h 49 min, from 00:21:14Z to 18:11:58Z. The longest break between sessions was 30 s, and the
last session lasted under a minute. The numerics and verification work ran in parallel over the same window. From
01:50Z all computation shared one to three CPU cores of a loaded machine. The deliverables were frozen at
2026-10-28T17:48Z, and the independent verifier confirmed that version and its numerical artifacts at 17:50Z, 17:57Z
and 18:18Z. A final editorial pass after T_end added this summary and run record, removed internal references and
assembled the accompanying artifacts. That pass preserved the mathematics and numerical values.

## Detailed overview

No existence theorem for an actual profile has been proved. A
complete conditional a posteriori existence theorem is proved: it produces an exact solution near any reference
profile that satisfies an explicit list of certifiable inequalities and has a small enough residual. For one explicit
reference (a tail repair of the checkpoint) every hypothesis except the smallness of the residual is proved; its
residual is far too large. A second conditional theorem, in a weighted space that admits slowly growing residuals,
applies to the checkpoint itself: every hypothesis on the reference and the membership of its residual in the space
are proved, but the smallness hypothesis fails: the certified residual size exceeds that threshold by a factor of more than 2^119 (the certified ratio is about
1.2e36) at every weight radius R >= 2^31, which includes every radius at which the theorem is proved (more than 2^128
for R >= 2^35). Exact finite rational references whose
residual lies in the space also exist (algebraic tail repairs), but nine of the ten explicit variants violate the
energy-matrix hypothesis and all ten have a certified residual size N_s(F) > 11.48, far above the threshold. Nine
further exact references, obtained by least-squares fitting with every forbidden residual sector cancelled exactly
(eight with the six stationary far-field branches of the checkpoint, one with a seventh), have residuals in the
weighted space but miss its threshold: for every weight radius R >= 2^31, by factors of more than 2^65 for Mpen2 and
d2 (an annular test at 2^20 <= r <= 2^21), more than 2^59 for A2 and A3 (an annular test at r ~ 2^31) and more than
2^42 for the other five (certified point values); and, uniformly in the smoothness index and in every R >= 1, by more
than 2^37 for all nine. Each of the nine violates a derivative bound of the reference contract at a certified point
(for Mpen2 and d2 at off-axis points; at the eight points audited first they pass). For the unweighted theorem a uniform
bound holds: no choice of coefficients in the generator family of these fits, with the prescribed leading data,
brings the residual within a factor of 22986 of its threshold, and raising the radial degree of the family from 75 to
any value up to 3675 (1312740 coefficient slots before the affine constraints) still leaves it above the threshold;
for the family with a seventh stationary branch the same method decides nothing. For the weighted theorem no
decisive uniform statement is proved: for each fixed radial degree the residual norm over the whole six-branch family has
a positive lower bound, uniform in the smoothness index and the weight radius, but its value is not computed and it
is not compared with the threshold; the same holds for the seven-branch family, where a signed annular test removes the
earlier free sector. A weaker bound of the same kind is evaluated exactly; it is below 1e-50 for both families, so it
does not decide the threshold either. No closed realization of the linearization in the critical far-field space is Fredholm, even
after finitely many exact linear constraints or a compact perturbation; this persists in critical weighted Sobolev
spaces of every order m >= 3, where the strain is a continuous functional, and with finitely many added parameters and
equations. In the weighted Sobolev space of growth exponent b (-3 < b < 1) the whole line Re z = c_l b - 1 lies in the
spectrum, so an inverse at zero there has norm at least 1/|1 - c_l b|. A second version of the weighted
theorem, with a sharper commutator estimate and a larger smoothness index, raises its threshold from 2^-35 to 2^-30
(radius 5 * 2^-27); every reference above still misses it at the radii where it is proved, the checkpoint by a factor of more than 2^114
and every refit by more than 2^37 (more than 2^60 for Mpen2 and d2). Necessary local tests prove that no exact
solution, of any exponent, lies within weighted distance 2^-14 of the checkpoint or 2^-9 of the refits Mpen2 and d2,
for every admissible smoothness index and every weight radius R >= 1; for R >= 2^31 the excluded radii are 2^57
around the checkpoint and 2^21 around Mpen2 and d2; and none lies within distance 2^-21 of the seven other refits at
the smoothness index of the first version; these radii are much larger than the radii of the weighted theorems, so the balls of both versions
around the checkpoint, Mpen2 and d2, and the ball of the first version around every other refit, contain no exact
solution. A third conditional theorem works, within a scale of logarithmic gains, in the sharp open range of that scale in which
the strain is a bounded functional: a weighted space of order 2 with only the logarithmic gain (1 + tau log(1 - Delta))^beta, 1/2 < beta <= 1, tau = 2^-24,
in which first derivatives are continuous but have no Hoelder bound of any positive order. Under the numerical
hypotheses of the weighted theorem, polynomial growth of every density derivative and a nonzero leading profile, it
gives exactly one normalized solution when the residual norm is at most
2^-25 tau^beta (2 beta - 1)^(1/2), which is below 2^-37 for every beta. The checkpoint misses it by a factor of more
than 2^121 and Mpen2 and d2 by more than 2^67, and no exact solution of any exponent lies within native distance
2^56 of the checkpoint or 2^20 of Mpen2 and d2, more than 2^86 and 2^50 times the radius of that theorem. A parametric form of this theorem leaves the bounds on the third velocity derivative and on the third and
fourth density derivatives free, at the price of a larger first-derivative coefficient and a smaller tau. For the
refit d2 every hypothesis of this parametric theorem on the reference is proved on the whole plane (normalization,
leading profile, polynomial growth, the three matrix inequalities, every remaining derivative and decay bound, and
exact global caps for the three free bounds, at Astar = 2^189 and tau = 2^-210), and its residual lies in the space;
only the smallness of the residual fails, by a factor of more than 2^243. For every parameter choice the residuals
miss the threshold by factors of more than 2^119 (checkpoint) and 2^65 (Mpen2, d2), and the balls of radius 2^56 and
2^20 stay excluded. The energy-matrix hypothesis of
the weighted theorem has been weakened from M >= (19/5) I to M >= (5/2) I on the disc r <= R; it is no longer the
binding condition. No reference is known that satisfies all hypotheses. For the
checkpoint (states 88 and 131) and the early refits m4, m5, m10, m12 and m14, whose residuals keep a sector r^q E with
q >= -2, a necessary condition proves that no exact solution exists in the corresponding affine class of unweighted
corrections (in Hdot^-1 with bounded gradient) at all, of any size and for any value of the exponent. It does not apply
to the tail repairs or to the later exactly admissible refits, whose residuals lie in the space: for them nonexistence
in the affine class is open, and the failure of a sufficient hypothesis is not a nonexistence result.
Statements marked THEOREM have been checked by an independent verification (proof and, where numbers enter, an
independent recomputation); statements marked PROPOSED have not, and are not used as proved conclusions. Numbers marked
FLOAT are floating-point observations, never bounds.

## Detailed summary

- Background: the latest accepted checkpoint of the case 4 860-generator run (state 131), reconstructed exactly as a
  finite potential with rational coefficients: c_l = 4076476460239181/2251799813685248 = 1.810319210199998...,
  a_0 = d_y rho_bar(0) = 10.300294891831177..., gamma = 1/c_l = 0.552388..., lambda = 2 c_l - 1 = 2.620638420399996...
  (THEOREM). Except in the local square tests of section 6, where delta is the half-side of the test square,
  delta = 1 - gamma = 0.447611... is the far-field exponent step; the decay exponent of the weighted and logarithmic
  contracts is written d, a letter that a few passages also use, with a local definition, for other quantities (a
  strain bound, a derivative order).
- The strain functional needs a local term: c[h] = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h r^-3 dX (THEOREM).
- Formulation: c_l fixed. Every solution in the parity class with C^(1,a) regularity at 0 and d_y rho(0) != 0 is
  automatically normalized, c_l + c[rho] = 1 (THEOREM). No strain unknown or rank-one term is needed, and no extra
  scalar phase equation is imposed: scaling is removed by the class (fixed leading profile; corrections square-integrable in N_s and of order at most r^(1/5), below the leading order r^gamma, in N^w_s).
  The linear operator is L_fix h = V.grad h - h + U[h].grad rho_tilde, V = c_l X + U[rho_tilde].
- Fixed-background linear theory (THEOREMS, section 4): for state 131, and for every reference satisfying the same
  certified inequalities, L_fix is bijective from its generator domain onto a Sobolev-type space X_U of order
  2 + 1/32 with an unweighted Hdot^-1 bottom, with inverse norm 20. The same inverse controls, in one forcing norm, the Hdot^-1 norm, a Hoelder norm of h and of
  grad h, a singular moment at the center and the strain: ||h||_Hdot^-1 + ||h||_(C^(1/64)) + M(h) + |c[h]| <= 240 ||L_fix h||.
  It maps the forcing hyperplane {f_y(0) = 0} onto {c[h] = 0} within the generator domain.
- Rough-velocity high solvability (THEOREM, section 5): in the fractional norm N_s(g) = E_2((1 - Delta)^(s/2) g) the
  operator A_k = L_fix + U[k].grad generates a semigroup with decay rate
    1/10 - 1024 s M* - 128 N_s(k)/s^(1/2), where M* <= 2374 is a certified sum of coefficient suprema for state 131,
  and, keeping the eight coefficient suprema and the four energy components separate, with the sharper rate
  1/10 - 4800 s - 5 N_s(k)/s^(1/2) for s <= 1/1024; wherever the rate is positive (uniformly on a ball of k for small
  s) A_k is bijective with inverse at most the reciprocal of the rate. No third derivative of U[k] is used. This removes the obstruction that the third-derivative energy of A_k needs D^3 U[k].
- Conditional existence (THEOREM, section 5): if a reference (c_l, rho_tilde) satisfies the hypotheses (B0), (B0n),
  (B1) to (B5), (B7) and (B9c) of Appendix A (all certified for state 131) and its residual
  R_tilde = F(rho_tilde; c_l) satisfies N_s(R_tilde) <= 1/1572864 (about 6.3578e-7) at s = 2^-18, then there is exactly one h
  with N_s(h) <= 2^-16 and c[h] = 0 such that rho_tilde + h is an exact solution with the same c_l. It is normalized
  and satisfies ||h||_Hdot^-1 + ||h||_(C^(1/2)) + M'(h) + |c[h]| <= 24 * 2^11 N_s(R_tilde), where
  M'(h) = [int_(r<1) r^(-p-4) |h - h_y(0) y|^p dX]^(1/p) with p = 2^21. (A first version needs only
  the coefficient sum (B9) but a residual below 3.7e-10 at s = 2^-28.) If the reference has a leading profile
  r^gamma Theta_0 (hypothesis (B11), true for the checkpoint and its tail repair), the solution has the same leading
  profile and is transverse to scaling.
- Weighted conditional existence (THEOREM, section 5): a second conditional theorem in a weighted fractional space
  N^w_s that admits residuals growing like r^q with q < 1/5. At s = 3 * 2^-31, a reference satisfying explicit
  pointwise background bounds (all certified for state 131) whose residual has N^w_s(F) <= 2^-35 (about 2.9104e-11)
  has exactly one normalized correction h with N^w_s(h) <= 5 * 2^-32 such that the sum is an exact solution with the
  same leading profile. The checkpoint residual belongs to this space, but an explicit annular test function certifies
  N^w_s(F) > 7.09e26 > 2^89 for it, more than 2^124 times the threshold (THEOREM): the low-order weight amplifies
  the growing far-field sector out to r ~ 2^35 (a floating-point evaluation of the whole far-field contribution
  gives about 8.4e28, FLOAT). The weight radius can be lowered to 2^32, and, using that the density is real in the
  velocity and commutator estimates, to 2^31, with the same constants (THEOREM); the gaps at those radii are still
  more than 2^117 and 2^115. A second, independently written program confirms the single-mode bound
  N^w_s(F) > 1.77e26 > 2^87 at the radius 2^35 (gap more than 2^122) and gives a combined bound at all three radii
  that an independent audit recomputes (N^w_s(F) > 5.89e24 at R = 2^31). Transferring that test to every larger
weight radius (the weight ratio w_T/w_R is at most 1 and has nonnegative Laplacian outside r = T, so it does not
increase the test energy), with the Bessel factor 1 + 2^-12 C_T in place of 11/10, gives N^w_s(F) > 3.53e25, 1.52e26 and 1.21e28 for
every R >= 2^31, R >= 2^32 and R >= 2^35, gaps of more than 2^119, 2^121 and 2^128 over 2^-35 (THEOREM). The low matrix hypothesis can be weakened
  to M >= (5/2) I, or to the position-dependent floor 2/5 + (11/5) c r^2/(R^2 + r^2), on r <= R, with every other
  hypothesis and constant unchanged (THEOREM). Since N^w_s(F) >= (10/11) 2^(53/2) ||w F||_(Hdot^-1), N^w_s(F) >= 190000 ||w F||_2 and
  N^w_s(F) >= 1000 w(X) |F(X)| and N^w_s(F) >= 12 max(1, |X|)^(-1/5) |F(X)| (THEOREM, section 6), the threshold
  2^-35 requires ||w F||_(Hdot^-1) < 2^-61, ||w F||_2 < 2^-52 and
  |F(X)| < min(2^-44 (1 + |X|^2/R^2)^(11/10), 2^-38 max(1, |X|)^(1/5)) at every point (a necessary condition, not a
  sufficient one).
- Second weighted version (THEOREM, section 5): for a smooth reference the commutator of (1 - Delta)^(s/2) with the
  frozen operator costs at most 2^13 s in the energy (instead of 2^23 s), under derivative bounds that belong to the
  hypotheses of Theorem D_w. With the same hypotheses, at s = 3 * 2^-21 a residual with N^w_s(F) <= 2^-30 (about
  9.3132e-10) yields exactly one normalized h with N^w_s(h) <= 5 * 2^-27 such that the sum is an exact solution, with
  output bound 2^23 N^w_s(F). The threshold is 32 times larger. The checkpoint misses it by more than 2^114 for every R >= 2^31, and every
  exactly admissible refit by more than 2^37 (more than 2^60 for Mpen2 and d2).
- Logarithmic conditional existence (THEOREM, section 5): with Q = (1 + tau log(1 - Delta))^beta, tau = 2^-24,
  1/2 < beta <= 1, C = tau^-beta (2 beta - 1)^(-1/2), and the native norm
  M(g)^2 = ||omega_2 D^2 Q g||_2^2 + 2^22 ||omega_1 D Q g||_2^2 + 2^53 ||w g||_(Hdot^-1)^2 (R = 2^31), the operator A_k
  decays at rate 1/32 and has inverse 32 for M(k) <= r_0 = 2^-20 tau^beta (2 beta - 1)^(1/2) under the numerical
  hypotheses of Theorem D_w at R = 2^31 and polynomial growth of every derivative of rho; if also the leading angular
  function is nonzero (section 5), a residual with M(F) <= r_0/32 yields exactly one
  h with M(h) <= r_0 and c[h] = 0 such that rho + h is an exact solution with the same exponent and leading profile.
  In this class U[h].grad h is not continuous at 0 from the space into itself, so the iteration contracts in the low
  norm (factor 3/16) inside the M ball. The same inverse controls the low norm, an adapted C^(1/2) norm of the density,
  a projected singular moment at the center and the strain: L + H + M_3 + |c| <= 2^12 C M(A_k h). The certified native
  residual floors are M(F) > 3.535e25 (checkpoint) and M(F) > 1.935e9 (Mpen2 and d2), more than 2^121 and 2^67 times
  the threshold; these residuals lie in the native space, so the floors bound finite norms (THEOREM; the accompanying artifacts,
  P106). Parametric version (THEOREM, section 5): the bounds on D^3 u, D^3 rho and D^4 rho may be any finite
  constants U3, B3, B4 if the coefficient 2048 of the first-derivative and low components of M is raised to an Astar
  with 7 Astar^2 >= 200 ((198 + B3/24)^2 + 352) and tau is lowered below an explicit bound; the radius, threshold,
  inverse 32 and contraction 3/16 keep their form, and the exclusions and gaps persist for every parameter choice.
- The gap (sections 6 and 7): no known reference has a small enough residual.
  * The checkpoint residual is not in the space of the unweighted theorem (a growing far-field sector of exponent
    2 gamma - 1 = 0.1048); it is in the weighted space N^w_s, where its norm exceeds 2^84 for every R >= 2^31 and 2^93 for R >= 2^35, more
    than 2^119 and 2^128 times the weighted threshold.
  * In the logarithmic space of section 5 the native residual norms exceed 3.535e25 (checkpoint), 1935892108 (Mpen2)
    and 1936535207 (d2), more than 2^121 and 2^67 times its threshold (THEOREM). For every parameter choice of the
    parametric version these floors scale by Astar/2048 and the gaps exceed (Astar/2048) 2^119 and (Astar/2048) 2^65
    (THEOREM). The point-value bounds of the other refits have not been transferred to that norm, so no gap is stated
    for them there.
  * An explicit tail repair of the checkpoint (a potential-level splice to the six exact stationary far-field sectors
    outside radius R = 2^1024) keeps every center jet and satisfies every hypothesis except the smallness of the
    residual, that is (B0) to (B9c), (B11) and membership of the residual in the space (THEOREM); but its residual equals the checkpoint residual on r < R and has N_s norm at least 2^1028 (THEOREM).
  * Exact algebraic tail repairs (finite rational potentials of the canonical generator form, obtained by adding
    generators of high degree that fix the six far-field sectors and cancel two radial descendants) keep the center
    data exactly and put the residual in the space (THEOREM). Of the ten variants constructed (degree parameter
    K = 4, 8, 16, 256, 4096 for the checkpoint and the refit m10), every one with K <= 256 has a certified negative
    eigenvalue of the energy matrix M at some point, the checkpoint variant with K = 4096 has a certified point where
    the least eigenvalue is below 3.417 < 19/5, and certified point values give N_s(F) > 11.48 for all ten variants (THEOREM). For
    m10 with K = 8 and 16, certified whole-plane norms of all residual components give N_s(F) > 7.34e6 and
    N_s(F) > 3.60e6 at s = 2^-18 (THEOREM). None of them is a usable reference.
  * Projected refits (THEOREM for the facts stated): seven finite rational references (A2, A3, A4, A5, Mpen fitted with
    a penalty for the matrix condition, A6dpen fitted with a penalty for the next descendant sector, Mpen2 fitted with
    both penalties) obtained by
    least-squares fitting in the extended generator family with all eight residual sectors of degree at least -2
    cancelled exactly (first nonzero sector of exponent gamma - 6 delta = -2.133) have the exponent, the normalization
    and the full leading profile of the checkpoint, so their residuals lie in N_s and in N^w_s. For A2 and A3, an
    annular duality test with the exact leading sector and a certified remainder gives N^w_s(F) > 2.0e7 > 2^24 at
    R = 2^31, more than 2^59 times the threshold; certified point values give least eigenvalues of M of 2.2225 and
    3.1352 < 19/5 at (0, 1) and rho_yy(0, 1/10) > 4.717 and > 10.899, which violates the bound |D^2 rho| <= 3 of the
    weighted reference contract. For A4, A5, Mpen and A6dpen, certified point values of the residual give
    N^w_s(F) > 9/100, 0.0203, 0.0178 and 0.0073 (more than 2^27 times the threshold), and each violates the bound
    <r>^2 |D^4 rho| <= 512 of the contract at a certified point (for example more than 678 at (0, 0.8) for Mpen); A4
    violates three further derivative bounds. For Mpen2 the certified value F(6, 8) = -0.12357... gives
    N^w_s(F) > 0.0048 (more than 2^27 times the threshold); at all eight audited points it satisfies M >= (19/5) I,
    M_1, M_2 >= I/2 and every derivative bound of the contract (point values), but at certified off-axis points it
    violates three: <r>|D^3 u| <= 16 (more than 16.12 at (19/64, 7/16)), <r>^2 |D^3 rho| <= 32 (more than 39.23 there)
    and <r>^2 |D^4 rho| <= 512 (more than 1333 at (1/4, 15/32)) (THEOREM). Mpen and A5 have least eigenvalues of M above 19/5 at every sampled point
    (certified point values and FLOAT scans; not a proof on the plane). The leading sector r^(-2.133) has the same
    full-circle angular norm 3081.27 for every six-branch refit and repair audited: it is the forcing of the six exact stationary
    sectors at the next order. A seventh stationary branch removes it, and then the next fixed sector is r^(-2.581),
    with full-circle angular norm 9679.97, determined by the seven leading stationary orders alone (THEOREM).
    A first exactly admissible seven-branch refit (b6: its first seven potential branches are the stationary orders
    and nine residual sectors vanish exactly, so the residual lies in N_s and N^w_s) has the leading residual sector
    (2, 1) at r^(-2.343); certified point values give N^w_s(F) > 0.2306 (more than 2^32 times the threshold) and
    violate three bounds of the contract: M_2 >= I/2 at (3, 4), |D^2 rho| <= 3 at (0, 1/5) and
    <r>^2 |D^4 rho| <= 512 at (3, 4) (THEOREM). A further six-branch refit, d2, in which the first descendants of
    branches 0, 1 and 2 are also stationary (nine residual sectors vanish exactly), satisfies every pointwise
    hypothesis of the contract at the eight points audited (point values only), but violates <r>^2 |D^4 rho| <= 512 at
    certified off-axis points (more than 592 at (7/16, 7/64)); this is one of the three bounds left free by the
    parametric logarithmic theorem, and d2 has the exact global cap <r>^2 |D^4 rho| <= 2^201 (THEOREM); its leading
    residual sector is again r^(-2.133) (THEOREM). For d2 the three matrix bounds of the weighted
    theorem, M >= (19/5) I and the weighted principal matrices M_1, M_2 >= I/2, hold on the whole plane (THEOREM;
    the accompanying artifacts, P95: complete exact compactified covers with 41, 79 and 119 leaves at 512 bits, each rechecked
    independently at 640 bits), and so do the decay bounds of the form at R = 2^31 (decay exponent d = 4/9),
    r^(4/9) (|D rho| + r |D^2 rho|) <= 186, r^(-5/9) |u| <= 22, r^(4/9) |Du| <= 22, r^(13/9) |D^2 u| <= 56, and the
    five fixed bounds |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, |D^2 rho| <= 3, <r>|D^2 rho| <= 8 (THEOREM;
    the accompanying artifacts, P95: complete covers with 36, 121, 314 and 23 leaves, each rechecked independently at 640 bits).
    With the exact caps for the three free bounds, d2 therefore satisfies every hypothesis of the parametric
    logarithmic theorem on the reference at R = 2^31, Astar = 2^189, tau = 2^-210, and its residual lies in the
    native space; the residual has Mstar(F) > 2^178 * 1936535207, more than 2^243 times the threshold, for every
    1/2 < beta <= 1, and no exact solution of any exponent lies within Mstar-distance 2^-15 tau^beta of d2, at least
    32 times the radius of that theorem (THEOREM; the accompanying artifacts, P105). With the weighted amplitude bound N^w_s(F) >= 1000 w(X) |F(X)| of section 6, certified point values give,
    uniformly in s and in R >= 1, N^w_s(F) > 5195.0, 2850.1, 309.38, 40.58, 39.61, 19.21, 12.66, 1380.0 and 5.479 for
    A2, A3, A4, A5, Mpen, A6dpen, Mpen2, b6 and d2 (more than 2^37 times 2^-35 and more than 2^32 times 2^-30 in every
    case), and for R >= 2^31 more than 26524, 14449, 2308.4, 516.4, 451.7, 185.7, 123.5, 5849.1 and 16.71 (more than
    2^42 times 2^-35); an annular test on 2^20 <= r <= 2^21 gives N^w_s(F) > 1.759e9 for both Mpen2 and d2 for every
    R >= 2^31 (more than 2^65 times 2^-35). For the checkpoint the point values give N^w_s(F) > 0.0475, and its
    annular bounds are far larger (THEOREM).
  * Necessary local distance (THEOREM): every exact profile rho_bar + h with h in the space of the weighted theorem
    (any smoothness index 0 < s <= 2^-12, any weight radius R >= 1) has the exponent of the reference, because the
    fixed leading profile r^gamma Theta determines it (exponent rigidity). The difference of the two equations then
    bounds |F(X)| at every point, and the pairing of F with any test function supported in an annulus, by explicit
    quadratics in N^w_s(h). With the amplitude bounds |h(X)| <= (1/12) max(1, r)^(1/5) n and
    |U[h](X)| <= (3/16) max(1, r)^(1/5) n (n = N^w_s(h), uniform in s and R), an annular test of the checkpoint at
    r ~ 2^31 (the signed pairing with the exact leading residual sector) excludes every exact solution with
    N^w_s(h) <= 2^-14, and square tests (a smooth bump on a small square, with certified interval Taylor bounds over the
    whole square and, in the sharpest form, negative-order duality) exclude N^w_s(h) <= 2^-9 around Mpen2 and d2 (with the weighted amplitude bounds w |h| <= n/1000 and
    w |U[h]| <= n/400), for all s and R in these ranges. For R >= 2^31 the weighted L^2 bounds ||w h||_2 <= n/190000
    and ||w U[h]||_2 <= n/60000 with negative-order duality in annular tests exclude N^w_s(h) <= 2^57 around the
    checkpoint (an annulus at r ~ 2^31) and N^w_s(h) <= 2^21 around Mpen2 and d2 (on 2^20 <= r <= 2^21). At s = 3 * 2^-31 certified point values exclude exact
    solutions with N^w_s(h) <= 2^-11, 2^-13, 2^-18, 2^-21, 2^-21 and 2^-21 around A2, A3, A4, A5, Mpen and A6dpen,
    and with N^w_s(h) <= 2^-16 around b6. All these radii exceed the radii 5 * 2^-32 and 5 * 2^-27 of the two versions
    of the weighted theorem. These are local statements; they exclude nothing outside the balls.
  * Uniform obstruction in the fitting family (THEOREM): for every real choice of the coefficients of the generator
    family of these fits (branches j <= 5, angular index m <= 59 in cos(2 m theta), radial degree k <= 75) with the
    six leading stationary branches and the two descendants prescribed, the residual satisfies
    ||F||_(Hdot^-1) > 2.925e-5 and hence N_s(F) > 0.01461 at s = 2^-18, more than 22986 times the threshold of the
    unweighted theorem. With radial degree k <= K in place of k <= 75 the same conclusion (N_s(F) above the threshold)
    holds for every K <= 3675; the bound decreases with K and stops deciding at K = 3676. No generator of the family
    enters the sector r^(-2.133) linearly (it consists of quadratic interactions of the fixed leading branches), and
    an exact distance formula for one power from the span of finitely many others (a Muntz-type product), together
    with a bound for the logarithmic derivative on the corresponding span of exponentials that grows linearly in the
    number of powers, turns this fixed sector into a lower bound for the whole norm. The method gives no weighted bound: a smooth function with the same
    leading sector, cancellations and power structure has N^w_s below 3.461e-13 < 2^-35 (THEOREM; it is not shown to
    be the residual of any potential), so a uniform statement for the weighted theorem would have to use the nonlinear
    structure of the residual. It is open. A qualitative version holds (THEOREM): for each fixed radial degree the
    weighted residual norm over the whole six-branch family (six leading branches and two descendants prescribed) has
    a positive lower bound, uniform in 0 < s <= 2^-12 and R >= 1. It comes from the properness of the quadratic
    transport term on finite-dimensional density spaces (div(v U[v]) = 0 forces v = 0 for v in L^2) and an explicit
    formula in Gram and tail constants (for the angular band of these fits the velocity constant is the exact
    sin^2(pi/242)), which is not evaluated, so it does not decide the threshold. The same qualitative floor holds for each fixed radial
    degree of the seven-branch family (seven stationary branches, first descendants of branches 0 and 1 prescribed,
    the descendant (2, 1) free): the signed radial test b_0(t)(c_* - t), b_0 = (t - 1)^2 (2 - t)^2, annihilates the free
    sector r^(-2.343) exactly and pairs positively with the fixed sector r^(-2.581) (radial factor
    J_* > 1/67200), so the free sector cannot cancel it (THEOREM; again not evaluated). For the family with a seventh
    stationary branch (sector r^(-2.581) fixed) the analogous unweighted bound is valid but below 7e-13 times the unweighted threshold already at the smallest radial degree
    of that family, because the fixed power is much closer to the span of the others; so no quantitative uniform
    obstruction is known for seven branches (THEOREM for the bound; it says nothing about the residuals).
  * Refits with an exactly stationary first sector exist; their residuals are still outside Hdot^-1 (and, for m4,
    m5, m10 and m12, outside L^2; the m14 residual is in L^2). For the
    best one the certified whole-plane norms are ||grad F||_2 = 0.34447... and ||omega D^2 F||_2 = 5.0099... (THEOREM; certified intervals in section 6), so
    the gradient component of N_s(F) alone is at least 128 ||grad F||_2 > 44.09 for every s (a diagnostic for
    this reference, not a bound over other references).
  * Necessary condition (THEOREM, section 6): if the residual of a reference has a nonzero leading sector r^q
    E(theta) with q >= -2, no exact solution exists in the affine class reference + N_s, of any norm. This excludes
    the checkpoint (q = 0.1048) and the early refits (q = -0.343 for m4, m5, m10, m12; q = -1.238 for m14), but not the
    tail repairs or the later refits A2 to Mpen2, whose residuals lie in N_s; and it
    also excludes every other value of the exponent c_l in these classes: an exact solution near them needs a
    tail-repaired reference or a larger class with tail coordinates. For finite potentials of the canonical form the
    residual lies in the space if and only if eight explicit sectors vanish.
  * What is missing is one reference that has a small enough residual and satisfies the coefficient hypotheses at
    the same time. For the best early refit (m10) the gradient component alone exceeds the threshold by a factor of
    about 6.9e7, and its low-order components are infinite; the later refits A2 to d2 have residuals with finite
    norms and miss the weighted thresholds by the factors given above.

## 1. Setting

- Equation: F(rho; c_l) = (c_l X + U[rho]).grad rho - rho = 0, U = (-psi_y, psi_x), -Delta psi = d_x rho, rho even in x
  and odd in y. Canonical inverse: psi odd-odd and o(r^2); unique among such velocity fields. Equivalently
  U[h] = (-R_1 R_2 h, R_1^2 h).
- Strain: c[h] = psi_xy[h](0) = d_y U_2[h](0); formula above, proved for Schwartz parity functions; it extends to h that is
  C^(1,a) near 0 with h = O(r^beta), beta < 1, and the corresponding derivative decay at infinity (the kernel is then
  absolutely integrable at infinity).
- Scaling: rho_t(X) = t rho(X/t) maps solutions to solutions; K_bar = rho_bar - X.grad rho_bar satisfies
  L K_bar = R_bar - X.grad R_bar for the normalized linearization L (THEOREM), K_bar ~ (1 - gamma) r^gamma Theta_0.
- Far-field exponents: p_n = 1 - n(1 - gamma), rounded to four decimals: p_1 = gamma = 0.5524, p_2 = 0.1048, p_3 = -0.3428, p_4 = -0.7904,
  p_5 = -1.2381, p_6 = -1.6857, p_7 = -2.1333.
  * With Theta_0 and c_l fixed, the stationary angular data Theta_1, ..., Theta_5 are uniquely determined by an explicit
    nonresonant recursion, constructed exactly (THEOREM). A cutoff of this six-order expansion has residual O(r^(p_7)),
    which lies in Hdot^-1.
  * The checkpoint instead carries non-stationary sectors (E_1 != 0, residual ~ r^(2 gamma - 1) E_1 with
    2 gamma - 1 = 0.1048, ||E_1|| = 0.0910; THEOREM) and two nonintegrable binomial descendants (powers -1.4476, -1.8952).
    On the whole exterior the residual obeys |F(X)| <= (48707/200000) |X|^(2 gamma - 1) for |X| >= 300 (THEOREM;
    the accompanying artifacts, P101: exact sector algebra, a geometric bound for the omitted binomial tail and a complete directed
    cover of the compactified exterior, rechecked independently at 512 bits). This is an upper bound on a growing
    residual, not a smallness statement.
  * The finite 860-generator family contains no exact nonzero profile (THEOREM).

## 2. Answers to the seven questions

1. Can the L2 estimate close, and if not, what is the first precise obstruction?
   - As a linear estimate, yes, and it is part of a complete high-order linear inverse. There is an exact L2 identity
     -<L_fix h, h> = (c_l + 1)||h||^2 + sum_k <A grad d_k phi, grad d_k phi> - <N grad phi, grad phi>, phi = (-Delta)^-1 h,
     with A = [[rho_y, -rho_x/2], [-rho_x/2, 0]] >= -(1/20) I and
     N = (1/2) [[rho_yyy, -rho_xyy], [-rho_xyy, rho_xxy]] <= I (THEOREM).
   - In the present energy construction the L2 level cannot close alone: its lower-order term N is nonlocal and needs the Hdot^-1 level, where global matrix
     positivity M >= 19/5 holds (THEOREM).
   - Combined, they give decay 11/4 in E_0^2 = ||h||^2 + (20/21)||h||_Hdot^-1^2, then 1/2 at the H1 level, 1/10 at the
     weighted second level, and 1/20 on the order 2 + 1/32 space X_U (THEOREMS, section 4).
   - Obstructions by derivative level (THEOREMS) explain the form of the norms:
     (a) nonlinear: in the low Hoelder norm together with the center moments and strain, the quadratic term U[h].grad h
         is unbounded (explicit bump sequence with bounded low Hoelder norm, vanishing strain, moments and tails, and
         unbounded quadratic term). A direct contraction in this low norm is therefore unavailable; in the present contraction
         construction the high norm must control grad h in L^inf;
     (b) second-derivative level: the unweighted energy is not coercive at infinity. The level-k symbol with weight
         <r>^(k - 1 - sigma) tends to c_l(gamma - sigma) (principal part). Unweighted D^2 is sigma = 1 > gamma, so a
         growing weight on D^2 is needed;
     (c) third-derivative level: the symbol at the origin is c_l - 2 = -0.19 < 0, so an unweighted or same-weight D^3
         energy only gives a growth bound (proved: growth <= 3/2). For the frozen outgoing operator there is no bounded
         H^3-to-H^3 inverse (cone-packet counterexample). In the present energy construction the order is therefore 2 + theta with theta small.
   - The first obstruction to the nonlinear closure was the rough-velocity high estimate: for A_k = L_fix + U[k].grad
     with k only of order 2 + theta, the third-derivative energy needs D^3 U[k]. It is now resolved by a direct
     fractional estimate of order 2 + s (section 5, THEOREM). It is also resolved at the minimal logarithmic
     regularity of section 5, where the quadratic term U[h].grad h is not even continuous at 0 from the space into
     itself (THEOREM; the accompanying artifacts, P76): there the iteration stays in a ball of the logarithmic norm and contracts in
     the low norm (THEOREM; P85). The remaining obstruction is the size of the residual: no known approximate solution has a residual small enough in
     N_s (answer 7). For the checkpoint and the early refits m4, m5, m10, m12 and m14 the obstruction is stronger: their affine classes contain
     no exact solution at all, because a residual sector r^q E with q >= -2 is incompatible with any stationary
     correction in Hdot^-1 with bounded gradient (THEOREM, section 6).
2. Can a direct C^alpha inverse for h be proved?
   - Yes in the following form (THEOREM), with h itself as the unknown and no h_x reformulation. On X_U, with forcing of
     the same Sobolev order 2 + 1/32:
     [grad h]_(C^(1/64)) <= 100 ||L_fix h||, ||grad h||_inf <= 40 ||L_fix h||, ||h||_(C^(1/64)) <= 60 ||L_fix h||.
   - Uniformly under rough frozen velocities (THEOREM): in N_s, s = 2^-28, ||h||_(C^(1/2)) <= N_s(h) <= 20 N_s(A_k h)
     for every k with N_s(k) <= 2^-27.
   - Weighted alternative: an explicitly weighted C^(1/124) norm of h is bounded by 2^46 ||L_fix h|| on X_W (THEOREM).
   - For the frozen principal operator lambda x d_x + y d_y - 1 + a_0 R_1^2 there is a same-order Hoelder-to-Hoelder
     inverse on the completion of the parity Schwartz functions with compact Fourier support away from 0 (a little
     Hoelder space, not all of C^alpha): norm 1/(1 - alpha) in a heat-semigroup norm equivalent on that core to the
     homogeneous C^alpha seminorm, for every 0 < alpha < min(1, sigma), sigma = a_0/(lambda - 1), and, in the
     homogeneous C^(1/2) seminorm, 87 for both states (bounds 86.716 for state 88 and 86.451 for state 131: exact
     Gaussian finite differences in the reverse direction and a fractional heat representation of the kernel through
     the integer Gaussian kernels in the forward direction; the accompanying artifacts, P66 and P67; earlier bounds 98, then 97
     and 96; 70 at alpha = 1/4, 329 at alpha = 3/4; sufficient constants, not optimal norms) (THEOREM).
   - In the logarithmic class of section 5 (THEOREM; the accompanying artifacts, P87): the density has the adapted C^(1/2) bound
     H(h) <= 64 M(h) (the C^(1/2) norm on the disc of radius 2 plus the supremum over dyadic annuli
     2^j <= r <= 2^(j+1) of 2^(-j/4)(||h||_inf + 2^(j/2) [h]_(C^(1/2)))), and under the reference hypotheses
     H(h) <= 2^12 C M(A_k h). The gradient has no Hoelder bound of any positive order in this class (P70), so this is
     a density estimate, not a same-order Hoelder inverse.
   - Not proved: a global Hoelder-to-Hoelder inverse for L_fix. The closure does not need it, because the
     Sobolev-forcing inverses above control everything the nonlinear iteration uses.
3. Can c[h] be controlled without a high-order Hoelder estimate?
   - Not from low norms: C^alpha and Hdot^-1 bounded, c[h] unbounded (THEOREM).
   - Yes from the common high inverse: |c[h]| <= ||DU[h]||_inf <= 40 ||L_fix h||_(X_U), and the full sum
     ||h||_Hdot^-1 + ||h||_(C^(1/64)) + M(h) + |c[h]| <= 240 ||L_fix h||_(X_U) (THEOREM). This is a Sobolev estimate of
     order 2 + 1/32, not a high-order Hoelder estimate. The jet-subtracted moment
     M(h) = [int_(r<1) r^-260 |h - h_y(0) y|^256]^(1/256) is controlled by the same norm. The rough-velocity version is
     ||h||_Hdot^-1 + ||h||_(C^(1/2)) + M'(h) + |c[h]| <= 2^16 N_s(h), with a moment of exponents p = 2^31, kappa = p + 4
     (THEOREM).
   - Within the fractional scale H^(2+s), a surplus s > 0 is necessary, and the loss s^(-1/2) in strain control cannot
     be avoided in these norms (THEOREM; the accompanying artifacts, P69); the logarithmic scale below replaces the power surplus. On real S1 functions in H^(2+s) the exact dual norm of c is
     1/[8 (pi s (s + 1))^(1/2)] (4.513 at s = 2^-12), and on {h: h_y(0) = 0} it is 1/[8 (2 pi s (s + 1))^(1/2)] (3.191).
     The first is one quarter of the gradient constant c_s of section 5. In the weighted norm N_(s,R) of Theorem D_w,
     keeping its coefficients 2^22 and 2^53, the norm C_R(s) of c satisfies s^(1/2) C_R(s) -> 1/(8 pi^(1/2)), and on
     {h_y(0) = 0} the limit is 1/(8 (2 pi)^(1/2)). Both limits are uniform in R >= 1. At s = 0, c is unbounded even on
     functions with vanishing center jet: along frequency cutoffs at M the ratio grows like (log M/(64 pi))^(1/2).
     So every bound of |c[h]| by N_(s,R)(h) carries the factor s^(-1/2). In the route of answer 6, which applies such a
     trace bound after the inverse, only the constant can improve. Whether c composed with the inverse has a smaller
     norm is not decided.
   - A logarithmic gain is enough for the trace alone (THEOREM; the accompanying artifacts, P70). Replace J^s by
     Q_beta = (1 + log(1 - Delta))^beta, both in H_beta = ||J^2 Q_beta h||_2 and in the weighted norm E_R(Q_beta h).
     Then c is bounded if and only if beta > 1/2. Below and at the threshold it is unbounded even on functions with
     vanishing center jet. In H_beta, ||c|| = D_beta^(1/2)/(8 pi^(1/2)) with D_beta = 1/(2 beta - 1) - e Gamma(1 - 2 beta, 1),
     and at beta = 1 the norms are below 1/18 and, on {h_y(0) = 0}, below 1/25. In the weighted norm,
     (2 beta - 1)^(1/2) times the norm tends to 1/(8 pi^(1/2)), uniformly in R >= 1. This space gives classical first
     derivatives but no gradient Hoelder estimate of any positive order. The transport inverse, the center moment and
     the nonlinear theorem have since been carried over (next bullet). The certified size of the residual does carry over
     (THEOREM; the accompanying artifacts, P71). For 0 < beta <= 1 the kernel of Q_beta^(-1) is a positive probability density, and
     Q_beta^(-1) enlarges the low norm L_R by at most the factor 1 + D_R, with D_R < 2^-27 for R >= 2^31. Hence the
     logarithmic norm of the state 131 residual exceeds 3.535 * 10^25 for every R >= 2^31 (the same as in N_(s,R) up
     to a relative 4 * 10^-9), and that of the two refits Mpen2 and d2 exceeds 1.935 * 10^9. They exceed the threshold of the logarithmic theorem
     below by more than 2^121 and 2^67.
   - Strain control in the sharp open range beta > 1/2 of the logarithmic scale (THEOREM; the accompanying artifacts, P72, P74, P75, P77, P83 to P87).
     (i) The circular cutoff T_eps h of the strain kernel at radius eps equals the average of the field
     C h = d_y U_2[h] + (1/4) d_y h over the disc of radius eps against the probability density
     2(1 - r^2/eps^2)_+/(pi eps^2), so on the logarithmic completion (beta > 1/2) the principal value is literal:
     since C h(0) = c[h] + h_y(0)/4, c[h] = -h_y(0)/4 + lim T_eps h(0) (P72). At the endpoint beta <= 1/2
     an explicit compact C^1 density with Dh(0) = 0 lies in every such space and has circular strain integrals
     tending to infinity like log log log(1/eps) (P74).
     (ii) With Q = (1 + tau log(1 - Delta))^beta the transport inverse carries over: for the fixed background with
     tau = 2^-20 (inverse 29, P75 and P77) and, in the native norm M of section 5 with tau = 2^-24, uniformly for rough
     frozen velocities U[k] with M(k) <= r_0 (inverse 32, P83 to P85).
     (iii) The strain has the contact-corrected form c[h] = -h_y(0)/4 + int_0^1 a_3(r) dr/r^2
     + (1/pi) int_(r >= 1) sin(3 theta) h r^-3 dX, a_3(r) the sin(3 theta) coefficient of h on the circle of radius r,
     and with C = tau^-beta (2 beta - 1)^(-1/2): |c[h]| <= 4 C M(h), the projected singular moment
     M_3(h) = int_0^1 |a_3(r)| dr/r^2 = (1/4) int_(r<1) r^-3 |P_3(h - h_y(0) y)| dX is at most 6 C M(h), and
     L + H + M_3 + |c| <= 128 C M(h) <= 2^12 C M(A_k h) (P87). The angular projection is taken before the absolute
     value; finiteness of the absolute moment of h - h_y(0) y is not claimed, and it fails in this class: the full
     absolute moment int_(r<1) r^-3 |h - h_y(0) y| dX is bounded in the norm ||(1 - Delta)(1 + log(1 - Delta))^beta h||_2
     exactly when beta > 3/2, and one compactly supported C^1 function with zero jet, zero strain and zero third
     harmonic lies in these spaces for every beta <= 3/2, in the corresponding weighted logarithmic spaces (the weighted
     norm E_R(Q_beta h) above) and in the native spaces of section 5, but has infinite absolute moment (THEOREM;
     the accompanying artifacts, P97). It lies in none of the fractional weighted spaces of Theorem D_w: for 0 < s <= 2^-12 and
     R >= 1 the full absolute moment is at most 2^14 pi s^(-3/2) (1 + s/2)^(-1) N_(s,R)(h), from the Hoelder estimate
     of the gradient in those spaces (THEOREM; the accompanying artifacts, P102).
     (iv) The nonlinear theorem holds with threshold 2^-25 tau^beta (2 beta - 1)^(1/2) < 2^-37 (P85), and the three
     references with certified low witnesses miss it (P86).
   - In the fixed-c_l formulation c[h] does not have to be solved for. The inverse restricts to a bijection from
     {f: f_y(0) = 0} onto {h: c[h] = 0}, by the exact range identity f_y(0) = (c_l + c[rho_tilde] - 1 + c[k]) h_y(0)
     + a_0 c[h] for f = A_k h (THEOREM); for a normalized reference and c[k] = 0 it reads f_y(0) = a_0 c[h], so c[h] = 0
     is preserved along the iteration because R_tilde_y(0) = 0.
4. Is the scaling freedom correctly eliminated? Yes, by the choice of class (THEOREM):
   - in the unweighted correction space, corrections lie in H^(2 + s) and tend to 0 at infinity together with their
     gradients; in the weighted class they may grow, but are O(r^(1/5)) (section 5), and in the logarithmic class an
     eventual tail r^q (log r)^(-a) Theta with Theta nonzero is admissible only for q <= 1/5 (P108), far below r^gamma; in each case
     they cannot change the leading profile r^gamma Theta_0, while scaling changes it to t^(1 - gamma) r^gamma Theta_0;
   - K_bar ~ (1 - gamma) r^gamma Theta_0 and the exponent variation r^gamma log r Theta_0 are excluded; in an augmented
     space with a leading-tail coordinate the scaling derivative of that coordinate is (1 - gamma)||Theta_0||^2 != 0;
   - no additional scalar phase equation is imposed; the fixed leading profile (hypothesis (B11), which holds for the
     checkpoint and its tail repair) and the correction class (corrections square-integrable in N_s and of order at most r^(1/5), below the leading order r^gamma, in N^w_s) remove scaling. Automatic normalization alone
     does not remove it;
   - the endpoint sigma = gamma is not admissible: in the realization Z_gamma with norm
     ||<r>^(-1-gamma) h||_2 the full L_fix is not bounded below (THEOREM: logarithmically
     long annular approximate null vectors). This persists when any finite list of linear constraints, continuous or
     not, is imposed exactly and under any compact perturbation, so no closed realization containing the constrained
     compact core is Fredholm (THEOREM). The same holds in the critical weighted Sobolev space of any order m >= 3,
     sum_(j <= m) ||<r>^(j-1-gamma) D^j h||_2^2, where U is bounded and c[h] is continuous, and for closed operators with
     finitely many added parameters and equations: none is even upper semi-Fredholm (THEOREM; the accompanying artifacts, P64).
     Multiplying the weights by any power (1 + log <r>)^kappa does not help, and neither do tail coordinates in an
     arbitrary, even infinite-dimensional, Banach space, as long as the remainder space is unchanged and the operator
     acts on the constrained compact core as (h, 0) -> (B h + K h, Q h) with K and Q compact (THEOREM; the accompanying artifacts,
     P68);
   - the theorem fixes (c_l, Theta_0). Profiles are expected in families and no isolation in a larger class is claimed.
5. Are the far-field exponent and angular perturbations rigorously accommodated? No theorem allowing free exponent and
   leading-angular variations is proved; the present theorems fix them, and they are not solved for:
   - the exponent variation and every free tail r^gamma Theta lie outside the high classes (THEOREM);
   - the lower sectors are determined by the exact stationary recursion (THEOREM);
   - in X_W the original residual, with its growing E_1 sector, is admitted (THEOREM), at the price of very large
     low-order weights;
   - in X_U and N_s a residual with a nonzero pure-power angular sector r^p Theta must have p < -2 (borderline
     logarithmic sectors are a separate case). The approximate solution must therefore carry the sectors Theta_1, ..., Theta_5 exactly and have no descendants of
     power above -2;
   - this is not only a requirement of the method: a nonzero residual sector r^q E with q >= -2 excludes every exact
     solution in the affine class reference + N_s (THEOREM, section 6), so these tail sectors must be built into the
     reference (or into a larger unknown with tail coordinates);
   - exact cancellation of the eight sectors can be combined with a least-squares fit in the extended generator family
     (THEOREM for the two audited files), but in both audited cases at the cost of the matrix condition and of a residual
     of order 10 near r ~ 1 (answer 7);
   - this can be achieved exactly while keeping all center data (THEOREM): splicing the potential of the checkpoint to
     the six exact homogeneous stationary potentials outside radius R gives a reference that coincides with the
          checkpoint on r < R, equals the stationary expansion on r > 2R, and has residual of order r^(p_7), p_7 < -2, at
     infinity;
   - it can also be achieved by an exact finite rational potential of the canonical generator form (THEOREM): adding
     one generator of high degree per branch and mode for the sectors 3 to 6 and two adjacent ones for the sectors 1
     and 2 (which also cancels the two descendants) fixes all six far-field sectors with unchanged potential Taylor
     coefficients below degree 2K; the residual is then O(r^(p_7)) and lies in N_s. For finite potentials of this form, membership
     of the residual in N_s is equivalent to the vanishing of eight explicit sectors (THEOREM);
   - the exponent is not a free parameter in these classes: if c differs from 1/gamma, the residual acquires the sector
     (c - 1/gamma) gamma r^gamma Theta_0, so no exact solution with a different exponent exists in reference + N_s
     (THEOREM).
6. Can the three parts (L2 or low inverse, Hoelder/high inverse, strain) be combined into one inverse?
   - Yes (THEOREM): one bijection on one forcing space (X_U for the fixed background, N_s uniformly for A_k with k in a
     ball) controls the low norm, the Hoelder norm, the center moment and the strain, with the normalization handled
     by the hyperplane bijection of answer 3.
      - All inputs of the two-norm theorem are proved: high solvability (N_s inverse 20 on the ball of radius 2^-27 at
     s = 2^-28, or inverse 24 on the ball of radius 2^-16 at s = 2^-18 under the component bounds (B9c));
     the low a priori bound K_L = 1/(19/5 - ||sym DU[k]||_inf) < 1; the bilinear bound
     ||U[z].grad g||_Hdot^-1 <= ||z||_Hdot^-1 ||grad g||_inf with ||grad g||_inf <= c_s N_s(g); completeness of the
     constrained high ball in the Hdot^-1 metric.
   - The same holds in the weighted space of Theorem D_w (THEOREM, section 5): for 0 < s <= 2^-12 and every k with
     positive decay rate beta = 1/20 - 2^23 s - 400 N^w_s(k)/s^(1/2) (2^13 s in place of 2^23 s for the second
     version; the balls of the theorems satisfy this), one bijection A_k on N^w_s controls the weighted low norm ||w h||_Hdot^-1, an adapted Hoelder norm, the center
     moment and |c[h]|, with constant 2^8 s^(-3/2)/beta for the decay rate beta of A_k (2^58 at s = 3 * 2^-31 on the
     ball of the first version, where beta > 1/40);
     bounding the strain directly as a trace of the velocity gradient improves this to 146/(beta s^(1/2)), at most
     2^28 at s = 3 * 2^-31 on that ball (THEOREM, section 5; at most 2^23 on the ball of the second version at
     s = 3 * 2^-21, where also beta > 1/40), and, when
     c[k] = 0, its inverse maps
     {f_y(0) = 0} onto {c[h] = 0}.
   - The same holds in the logarithmic class (THEOREM, section 5; the accompanying artifacts, P85, P87): one bijection A_k with
     inverse 32 in the native norm M controls the low norm, an adapted C^(1/2) density norm, a projected singular
     moment at the center and the strain, L + H + M_3 + |c| <= 2^12 C M(A_k h), and for c[k] = 0 its normalized
     restriction maps {f_y(0) = 0} onto {c[h] = 0}.
7. Can the residual and nonlinear estimates close an existence theorem?
      - The nonlinear estimates close (THEOREM, section 5): for any reference satisfying (B0), (B0n), (B1) to (B5), (B7)
     and (B9c), a residual with N_s(R_tilde) <= 1/1572864 (about 6.3578e-7) (s = 2^-18) yields a unique exact solution in the
     ball N_s(h) <= 2^-16, c[h] = 0, normalized, with direct Hoelder, moment and strain bounds, and with the leading
     profile fixed when (B11) also holds. The contraction constant is below 1/1000. Under the weaker sum hypothesis (B9) the same holds with
     threshold 3.7e-10 at s = 2^-28.
      - Optimizing s with the same proved constants gives 6.53e-7 at s = 1/240000, only 3 percent more. In general the
     optimal threshold is (16/25) mu_0^(5/2) (5 C_bg)^(-1/2)/(4 c_U) (mu_0 = 1/10 the E_2 decay rate, C_bg = 4800 the
     background and c_U = 5 the rough constant), so further gains from sharper constants are slow; and the weights
     2^7, 2^9 of the low-order components of E_2 make the residual norm itself large.
   - The residual norm is E_2-like: E_2(R)^2 = ||omega D^2 R||^2 + 2^14 ||grad R||^2 + 2^18 ||R||^2
     + 2^18 (20/21)||R||_Hdot^-1^2, and N_s(R) <= E^(1 - s)(2 Q^2 + 16410 E^2)^(s/2) + 34 s E with E = E_2(R),
     Q = ||omega D^3 R|| (THEOREM). So certified bounds of ordinary weighted derivative norms suffice.
      - Checkpoint: hypotheses (B0) to (B9) and (B9c) hold (THEOREM), but its residual is not in N_s (the Hdot^-1 and L^2 components
     diverge), and no exact solution exists in the affine class checkpoint + N_s (THEOREM, section 6). Its certified
     whole-plane norms are ||omega D^2 R||_2 = 25.189... and ||omega D^3 R||_2 = 2.5042... (THEOREM; certified intervals in section 6).
   - Checkpoint in the weighted space (THEOREM, Theorem D_w of section 5): its residual belongs to N^w_s, whose
     weights admit growth r^q with q < 1/5, and all background hypotheses of Theorem D_w hold for it; the nonlinear
     estimates close there with threshold N^w_s(F) <= 2^-35 (about 2.9104e-11) at s = 3 * 2^-31. But
     N^w_s(F) > 7.09e26 > 2^89 (certified annular test function at r ~ 2^35), more than 2^124 times that threshold
     (a FLOAT evaluation of the whole far-field contribution gives about 8.4e28; the low-order weight amplifies the
     growing far-field sector out to r ~ 2^35). With the smaller weight radius 2^32, which the theorem also allows
     (THEOREM), the certified bound is N^w_s(F) > 8.9e24 > 2^82, still more than 2^117 times the threshold, and with the
     smallest proved radius 2^31 (THEOREM) it is N^w_s(F) > 2.07e24 > 2^80, more than 2^115 times the threshold. An
     independently written program confirms N^w_s(F) > 1.77e26 at the radius 2^35, and its combined test with exact
     radial integration, recomputed by an independent audit, gives N^w_s(F) > 5.89e24, 2.53e25 and 2.01e27 at
     R = 2^31, 2^32 and 2^35 (gaps more than 2^117, 2^119 and 2^125; THEOREM). Transferring that test to every larger
     weight radius, with the Bessel factor 1 + 2^-12 C_T in place of 11/10, gives N^w_s(F) > 3.53e25, 1.52e26 and 1.21e28 for all
     R >= 2^31, 2^32 and 2^35 (gaps more than 2^119, 2^121 and 2^128; THEOREM). So for the checkpoint itself the
     gap is purely quantitative, but closing it needs the far field accurate out to r ~ 2^31 or beyond.
   - Second weighted version (THEOREM, section 5): a smooth-commutator estimate (cost 2^13 s instead of 2^23 s)
     allows s = 3 * 2^-21, radius 5 * 2^-27 and threshold N^w_s(F) <= 2^-30 under the same hypotheses, with output
     bound 2^23 N^w_s(F). The checkpoint misses this threshold by more than 2^114 (the annular bounds above hold for
     every 0 < s <= 2^-12), and every exactly admissible refit by more than 2^37 (more than 2^60 for Mpen2 and d2;
     section 6).
   - Logarithmic version (THEOREM, section 5): in the native norm M (tau = 2^-24, 1/2 < beta <= 1) and under the
     numerical hypotheses of Theorem D_w at R = 2^31, polynomial growth of every derivative of rho and a nonzero
     leading angular function, the threshold is
     M(F) <= 2^-25 tau^beta (2 beta - 1)^(1/2), at most 1.083e-12 (its maximum 2^-37 (24 e log 2)^(-1/2) = 1.08199e-12, about 2^-39.75, is attained at
     beta = (1 + 1/(24 log 2))/2, about 0.530) and below 2^-37 for every beta. The certified annular low witnesses give M(F) > 3.535e25 for the checkpoint and M(F) > 1.935e9 for
     Mpen2 and d2, more than 2^121 and 2^67 times the threshold, and no exact solution of any exponent lies within
     M-distance 2^25 tau^beta of the checkpoint or 2^-11 tau^beta of Mpen2 and d2 (THEOREM; the accompanying artifacts, P86), at
     least 2^45 and 512 times the radius of the theorem; a direct comparison of the norms enlarges these radii to
     2^77/(2^20 + 7) > 2^56 and 2^41/(2^20 + 7) > 2^20, for every 0 < tau <= 2^-20 and 0 <= beta <= 1, in particular for tau = 2^-24 (THEOREM; the accompanying artifacts, P111). The three residuals lie in the native space, so these floors
     are lower bounds of finite norms (THEOREM; the accompanying artifacts, P106). Lowering the regularity to this sharp range therefore does not
     help with the residual: the threshold is smaller than in the fractional versions and these gaps are larger.
     The parametric form (THEOREM, section 5; the accompanying artifacts, P89 to P91) makes the bounds on D^3 u, D^3 rho and
     D^4 rho free parameters, which removes every certified derivative violation of Mpen2 and d2 (exact global caps
     2^191 and 2^201), but for every parameter choice the threshold stays below 2^-35 and the gaps stay above
     (Astar/2048) 2^119 and (Astar/2048) 2^65, where Astar >= 2048 is the enlarged hierarchy coefficient; at the
     parameters needed for Mpen2 and d2 (Astar = 2^189) the gap exceeds 2^243. For d2 every hypothesis of the
     parametric form on the reference is proved at these parameters (tau = 2^-210; THEOREM; the accompanying artifacts, P95, P91
     and P105): d2 fails only the smallness of its residual, by a factor of more than 2^243, and the closed
     Mstar-ball of radius 2^-15 tau^beta about d2, which contains the ball of the theorem, contains no exact
     solution of any exponent.
      - Tail repair of the checkpoint at R = 2^1024 (THEOREM): all hypotheses (B0) to (B9), (B9c) and (B11) hold, and the
     residual is in N_s ((B10m)); but N_s(R_tilde) >= 512 ||R_tilde||_2 >= 2^1028, because on r < R the residual is that of the
     checkpoint, whose leading sector grows like r^(0.1048). For this splice ||R_tilde||_2 grows like R^(1.1048) as R
          increases, so a smaller radius does not help unless the reference is already accurate out to that radius.
      - Algebraic tail repairs of the checkpoint and of the best refit (THEOREM): the residual is in N_s, but (B1) fails
     for nine of the ten variants (certified point values of M; for K <= 256 a negative eigenvalue), and certified
     point values with ||f||_inf <= N_s(f) give N_s(R_tilde) > 1305 for K = 4, 8 and 16, > 208 for K = 256 and > 11.48 for K = 4096. For the
     m10 variants with K = 8 and 16, certified whole-plane norms of all components give
     7344656 < N_s(R_tilde) < 19372856 and 3600047 < N_s(R_tilde) < 16301199 at s = 2^-18, more than 10^12 times
     the threshold.
   - Projected refits (THEOREM): seven exactly admissible references (A2, A3, A4, A5, Mpen, A6dpen, Mpen2) from least-squares
     fitting with the eight forbidden sectors cancelled exactly. For A2 and A3 an annular duality test built from their
     exact leading sector r^(-2.133) E with a certified remainder gives N^w_s(F) > 2.0e7 > 2^24 at R = 2^31, more than
     2^59 times the weighted threshold; both also violate the bound |D^2 rho| <= 3 of the weighted reference contract at
     (0, 1/10) and the original matrix floor 19/5 at certified points. For A4, A5, Mpen and A6dpen certified point
     values give N^w_s(F) > 309.3, 40.58, 39.61 and 19.21 for every R >= 1 (more than 2^37 times the threshold), and
     each violates
     the bound <r>^2 |D^4 rho| <= 512 at a certified point. For Mpen2 certified point values give N^w_s(F) > 12.66 for every R >= 1, and an annular test gives
     N^w_s(F) > 1.759e9 for every R >= 2^31 (more than 2^65 times the threshold); M >= (19/5) I and every derivative
     bound of the contract hold at the eight audited points, but three derivative bounds fail at certified off-axis
     points (THEOREM). The weakened matrix condition M >= (5/2) I (THEOREM) is not
     certified for any of them on the whole disc. The first exactly admissible seven-branch refit b6 gives
     N^w_s(F) > 0.2306 at a certified point and violates M_2 >= I/2, |D^2 rho| <= 3 and <r>^2 |D^4 rho| <= 512 at
     certified points (THEOREM). A further refit d2 satisfies every pointwise hypothesis at the eight audited points
     but violates <r>^2 |D^4 rho| <= 512 at a certified off-axis point, and has N^w_s(F) > 5.479 uniformly in s and
     R >= 1 and N^w_s(F) > 1.759e9 for R >= 2^31 (THEOREM); its matrix bounds M >= (19/5) I and M_1, M_2 >= I/2, the
     decay bounds of the form at R = 2^31 and the five fixed derivative bounds not left free by the parametric
     theorem hold on the whole plane (THEOREM; the accompanying artifacts, P95). No exact solution of any exponent lies within
     N^w_s-distance 2^-14 of the checkpoint or 2^-9 of Mpen2 and d2 (for every s <= 2^-12 and R >= 1; for R >= 2^31
     the radii are 2^57 and 2^21), or
     within distance 2^-21 of A2, A3, A4, A5, Mpen and A6dpen and 2^-16 of b6 (at s = 3 * 2^-31) (THEOREM, necessary
     local tests); so the ball of Theorem D_w around each of these references, and the ball of its second version
     around the checkpoint, Mpen2 and d2, contain no exact solution. This is stronger than the failure of the
     threshold, but it is local.
   - Uniform obstruction (THEOREM): in the generator family of these fits (branches j <= 5, m <= 59, k <= 75), every
     choice of coefficients with the prescribed leading data has ||F||_(Hdot^-1) > 2.925e-5 and N_s(F) > 0.01461, more
     than 22986 times the unweighted threshold, because the sector r^(-2.133) is the same for all members; for radial
     degree k <= K the residual stays above the threshold for every K <= 3675. A seventh stationary branch removes that
     sector; the next fixed sector, r^(-2.581), then has full-circle angular norm 9679.97, more than three times the old
     3081.27 (THEOREM), but for the seven-branch family the same method gives only a positive bound below
     7e-13 times the threshold, which decides nothing (THEOREM). No such
     uniform bound follows for the weighted theorem from the leading sector and the power structure alone: an explicit
     smooth function with these properties has N^w_s < 3.461e-13 (THEOREM; not shown to be a residual). For each fixed
     radial degree the weighted residual norm over the six-branch family, and over the seven-branch family, does have a
     positive lower bound, uniform in s and R (THEOREM), but it is not evaluated and decides nothing about the threshold.
     An explicit version (exact radial power representation, the Muntz distance of the fixed power to all other powers,
     and N^w_s(h) >= 2045 ||<r>^(-6/5) h||_2) is fully evaluated: above 6e-55 for six branches at radial degree 75 and
     above 3.46e-75 for seven branches at degree 69, far below the threshold (THEOREM; the accompanying artifacts, P62).
   - What a reference must achieve for Theorem D_w: since N^w_s(F) >= (10/11) 2^(53/2) ||w F||_(Hdot^-1),
     N^w_s(F) >= 190000 ||w F||_2, N^w_s(F) >= 1000 w(X) |F(X)| and N^w_s(F) >= 12 max(1, |X|)^(-1/5) |F(X)| for every
     F in the space (THEOREM, section 6), the threshold 2^-35 needs ||w F||_(Hdot^-1) < 2^-61 (about 4.3e-19),
     ||w F||_2 < 2^-52 and |F(X)| < min(2^-44 (1 + |X|^2/R^2)^(11/10), 2^-38 max(1, |X|)^(1/5)) everywhere (2^-56,
     2^-47, 2^-39 and 2^-33 for the threshold 2^-30 of the second version). The checkpoint residual is about 1e-6 at r = 1 (FLOAT), so even its near field is short by a factor of
     about 2^24 pointwise (2^19 for the second version), and the weight 2^53 of
     the low component makes the low-order requirement far stronger.
   - Improved references: refits with E_1 = 0 exactly exist (exactness THEOREM for the first family). Their residuals
     are outside Hdot^-1 (THEOREM): for m4, m5, m10, m12 E_(2,0) != 0 at exponent -0.343, so they are also outside
     L^2; for m14 the leading sector (4,0) has exponent -1.238, so it is in L^2 but not in Hdot^-1; so their affine classes contain no exact
     solution (THEOREM, section 6). For the best one ||omega D^2 F||_2 = 5.0099..., ||grad F||_2 = 0.34447... and
     ||omega D^3 F||_2 = 12.331... (THEOREM, certified whole-plane values, truncated), so the gradient component of N_s(F)
     alone is at least 128 ||grad F||_2 > 44.09.
   - The answer is therefore: complete conditional theorems (one in N_s, one in the weighted space N^w_s in two
     versions, one in the logarithmic space M), no unconditional one. Membership of the residual and the
     coefficient hypotheses are attainable together (tail repair), and membership is attainable within finite rational
     potentials (algebraic repair), so what remains is smallness achieved simultaneously with the coefficient hypotheses. For the
     best early refit (m10) the gradient component alone exceeds the threshold by a factor of about 6.9e7 (128 ||grad F||_2 > 44.09
     against 6.357e-7), the gradient (weight 2^7) binds before the weighted Hessian, and the L^2 and Hdot^-1 components
     (weight 2^9) are infinite; this is a diagnostic for that reference, not a lower bound over other references.
     Closing it needs an approximate solution whose residual is below the threshold on the whole plane (for a tail
     repair: on r < R and across the transition annulus), certified upper bounds of E and Q (the exact-integration method
     of section 6 applies to finite rational potentials), and the certificates (B0)
          to (B9c) for it (for the cutoff splice of a certified reference only the exterior needs new estimates; an
     algebraic repair or a new refit needs all of them).

## 3. Adopted formulation and the two-norm theorem (precise statements in the accompanying artifacts)

- Unknown h, c_l fixed: R_tilde + L_fix h + U[h].grad h = 0, R_tilde = F(rho_tilde; c_l), rho = rho_tilde + h.
- Automatic normalization (THEOREM): if rho in the parity class is C^1 near 0 with Hoelder (or little-o) remainders,
  U[rho] is differentiable at 0, F(rho; c_l) = o(|X|) and d_y rho(0) != 0, then c_l + c[rho] = 1. In the iteration the slope stays positive because ||grad h||_inf <= c_s r, which is below 2^-13 in version (a) and equals
  0.0022039... < 1/400 in version (b), both below a_0; for every admissible reference, parity, (B0n) and
  M_1 >= (9/10) I at the origin give a_0 >= c_l - 11/10 > 7/10.
- Frozen-velocity map: for k in the high ball, T(k) is the solution g of A_k g = -R_tilde,
  A_k g = (V + U[k]).grad g - g + U[g].grad rho_tilde. The fixed point h = T(h) solves the equation.
- Two-norm theorem (THEOREM, abstract): if (H1) A_k g = -R has a unique solution with ||g||_H <= K_H ||R||_(Y_H) for k
  in a ball B of radius r that is complete in the low metric, (H2) ||g||_L <= K_L ||A_k g||_(Y_L) on differences, and
  (H3) ||(A_(k_1) - A_(k_2)) g||_(Y_L) <= C_B ||k_1 - k_2||_L ||g||_H, then K_H eta <= r and q = K_L C_B K_H eta < 1
  give a unique fixed point in B with ||h||_H <= K_H eta, eta = ||R_tilde||_(Y_H), and geometric convergence of the
  iterates with ratio q.
- The residual enters only through eta, the high norm. The low norm is applied only to differences of iterates.
- Reference independence (THEOREM): the unweighted Route U linear theory of section 4 and the unweighted
  rough-velocity and conditional existence theorems of section 5 use the reference only through the explicit
  hypotheses (B0) to (B11) of Appendix A and exact identities of the operator. The weighted theorem D_w and the
  logarithmic and parametric theorems use it only through their own hypothesis lists, stated with them in section 5.
  The weighted alternative X_W of section 4 is proved for the checkpoint only. For a new reference the certificates
  must be recomputed, or the difference to the checkpoint treated by a proved perturbation bound. For the
  unweighted contract (B0) to (B11) this has been done for the tail repair of the checkpoint (all hypotheses except
  the smallness of the residual, by the original certificates on the unchanged interior and direct estimates on the
  exterior), and for no refit beyond (B1). For the exact refit d2 the complete reference contract of the parametric
  logarithmic theorem is certified (section 5); only its residual smallness hypothesis fails.

## 4. Linear theorems for the fixed background (THEOREMS)

Common facts: state 131 (the low level and Route U hold for any reference satisfying (B0) to (B8); the weighted
alternative X_W is proved for state 131 only); parity class; Hdot^-1 is the parity homogeneous
negative space; <r> = (1 + r^2)^(1/2).

- Low level: global matrix positivity M(X) = (2 c_l + 1) I + sym DU_bar + A >= (19/5) I. Hence a bijective inverse of
  norm <= 5/19 on parity Hdot^-1. Under a frozen divergence-free Lipschitz parity field W with W(0) = 0 and
  d = ||sym DW||_inf < 19/5: ||(L_fix + W.grad)^-1||_(Hdot^-1) <= 1/(19/5 - d), with no second derivative of W needed.
  Bilinear: ||U[h].grad g||_Hdot^-1 <= ||h||_Hdot^-1 ||grad g||_inf.
- Route U norms:
  * E_0^2 = ||h||^2 + (20/21)||h||_Hdot^-1^2 (decay 11/4; inverse 4/11);
  * E_1^2 = ||grad h||^2 + 16 E_0^2 (decay 1/2; inverse 2);
  * E_2^2 = ||omega D^2 h||^2 + 2^14 E_1^2, omega = (1 + 4 r^2)^(2/5) (decay 1/10; inverse 10);
  * E_3^2 = ||omega D^3 h||^2 + 2^173 E_2^2 (growth at most 3/2);
  * X_U = [E_2, E_3]_theta by complex interpolation, theta = 1/32.
  On X_U the common semigroup decays like exp(-t/20), and L_fix is bijective from its generator domain onto X_U with
  ||L_fix^-1|| <= 20. Further:
  * ||h||_(H^(2 + theta)) <= ||h||_(X_U);
  * ||grad h||_inf, ||DU[h]||_inf <= [2 (pi theta (1 + theta))^(1/2)]^-1 ||h|| <= 2 ||h||;
  * [grad h]_(C^(1/64)), [DU[h]]_(C^(1/64)) <= 5 ||h||;
  * ||h||_(C^(1/64)) <= 3 ||h||;
  * M(h) <= 5 ||h|| for the moment M(h) = [int_(r<1) r^-260 |h - h_y(0) y|^256]^(1/256);
  * ||h||_Hdot^-1 + ||h||_(C^(1/64)) + M(h) + |c[h]| <= 240 ||L_fix h||_(X_U).
  The inverse restricts to {f_y(0) = 0} -> {c[h] = 0}. Closed X_U balls are closed in Hdot^-1.
  Inputs (for state 131: exact compactified Bernstein certificates with independent 384-bit recomputation):
  * matrix inequalities M >= (19/5) I, A >= -(1/20) I, N <= I, M_1 = I - sym DU_bar + A >= (9/10) I,
    M_2 >= (1/2) I and M_3 >= -(5/4) I (Appendix A, (B1) to (B6)); an independent recomputation from the exact
    original potential gives M_1 >= 0.972875 I, M_2 >= 0.587238 I, M_3 >= -1.230876 I and ||sym DU_bar|| <= 0.810792
    < 17/20 on the whole plane (compactified Bernstein certificates of 99, 144, 164 and 49 leaves at 384 bits, each
    leaf rechecked by direct restriction at 448 bits; THEOREM; the accompanying artifacts, P96); a second, independent certificate of the first
    (48 compactified Bernstein leaves, two directed computations at 320 and 384 bits) gives M >= 3.8103 I on the
    whole plane, against the exact center value c_l + 2 = 3.8103192... (THEOREM; the accompanying artifacts, P92); a third, by a
    different method (degree-8 Taylor enclosures with Lagrange remainders on 58640 polar cells covering
    1/200 <= r <= 10066.9, an origin square and an exact far-field sector bound), gives M >= 3.810156 I, and its
    completeness and its annular and far-field numbers are confirmed by separate Bernstein certificates of 51 and 4
    leaves (THEOREM; the accompanying artifacts, P93); and the bound is sharp: M >= (c_l + 2) I on the whole plane, with
    lambda_min(M) = c_l + 2 only at the origin (THEOREM; the accompanying artifacts, P94: near the origin, in t = r^2/(1 + r^2) <= 1/40001,
    the first diagonal entry of M - (c_l + 2) I is at least 10, the second at least t/4 and the off-diagonal entry at most
    20 t, so the determinant is at least t (5/2 - 400/40001), positive for 0 < t <= 1/40001 (it vanishes at the
    origin t = 0); elsewhere the annular bound of P93 exceeds c_l + 2);
    further complete directed covers with independent rechecks, using no floating-point trigonometric bound, give
    A >= -(1/20) I and d_y rho_bar >= (1 + r^2)^(-delta/2) > 0 on the whole plane, and for r >= 10^4 the exterior
    bounds M >= 4.595633 I and, for the matrices of (B4) to (B6), M_1 >= 0.990775 I, M_2 >= 0.620899 I and
    M_3 >= -1.194644 I (THEOREM; the accompanying artifacts, P99);
  * coefficient bounds |D^2 rho_bar| <= 3, |omega D^2 rho_bar| <= 8, |omega D^3 rho_bar| <= 10, |omega D^2 U_bar| <= 3,
    |D(omega^2 grad rho_bar)|/omega <= 28 and an explicit scalar term |S| <= 40 (Frobenius norms), plus coarse
    third-level bounds up to <r>^2 |D^4 rho_bar| < 2^84 used only for the E_3 growth bound;
  * the weighted Riesz bound 9/5 on centrally odd functions (below), flow-derivative bounds and an onto argument by the
    semigroup integral.
  Not an input, but certified for the same exact state: near the center, on r <= 1/10, with D = DU_bar,
  |d_y rho_bar - a_0| <= 3.04 r^2, |d_x rho_bar| <= 1.24 r^2, |D_11 - (c_l - 1)| = |D_22 - (1 - c_l)| <= 0.65 r^2,
  |D_12| <= 0.59 r^2, |D_21| <= 0.66 r^2, |U_bar_1 - (c_l - 1) x| <= 0.285 r^3 and |U_bar_2 - (1 - c_l) y| <= 0.293 r^3
  (THEOREM; the accompanying artifacts, P98: exact Taylor division of the binomial branch factors with a rational tail bound and
  complete covers at 384 bits, rechecked at 448 bits; an independent interval cover in the accompanying artifacts
  confirms these bounds).
- Weighted Riesz constants: for |beta| < a, on L^2(r^(2 beta)) the Beurling transform has norm
  (a + |beta|)/(a - |beta|), a = 1 in general and a = 2 on centrally odd functions (the formula is valid only in that
  range); for the weight omega the velocity bound on centrally odd input is below 9/5, and below 16/3 without parity.
- Weighted alternative X_W:
  * w = (1 + r^2/R^2)^(-11/10), R = 2^179;
  * omega_0 = <r>^(-6/5), omega_1 = <r>^(-1/5), omega_2 = (1 + 4 r^2)^(2/5);
  * E_1^2 = ||omega_1 D h||^2 + 2^112 ||w h||_Hdot^-1^2;
  * E_2^2 = ||omega_2 D^2 h||^2 + 2^72 E_1^2;
  * E_3^2 = ||omega_2 D^3 h||^2 + 2^195 E_2^2;
  * X_W = [E_2, E_3]_(1/62).
  Results: inverse bound 40; the velocity is bounded on X_W with norm <= 2^35; a weighted C^(1/124) norm, the moment
  (p = 256, kappa = 260) and c[h] are bounded by 2^46 ||L_fix h||. X_W contains the original residual. The bottom radius
    R = 2^179 makes every low-order quantity of a slowly decaying residual very large, so this realization is not useful
  for closure. The velocity bound 2^35 can be replaced by 13/2: for the regularized weight (1 + r^2/R^2)^(-s/2),
  0 <= s < 3, the operator (d_x - i d_y)^2 (-Delta)^(-1) has norm exactly 3(s + 1)/(3 - s) on centrally odd functions
  in the weighted Hdot^-1 norm, uniformly in R (THEOREM; 12 at s = 11/5). With the pure homogeneous weight r^(-11/5)
  the same norm holds, but the frozen energy is not coercive: for state 131 there are parity functions with c[h] = 0
  on which Re <L_0 h, h> divided by the squared norm tends to an exact rational Q_* in [12.7048, 12.7049] (THEOREM),
  so that weight cannot give an energy estimate.
- Logarithmic linear inverse (THEOREM; the accompanying artifacts, P75, P77). Under the numerical hypotheses of Theorem D_w at
  R = 2^31 (section 5) and polynomial growth of every derivative of rho and u, with Q_tau = (1 + tau log(1 - Delta))^beta, 0 < beta <= 1, tau = 2^-20, and N_tau(h) = E^w(Q_tau h)
  (E^w the weighted energy of section 5), the maximal realization of L_fix decays at rate 1/29 and is a bijection
  with inverse at most 29 in N_tau. N_tau and the norm N_beta(h) = E^w((1 + log(1 - Delta))^beta h) define the same
  space, with N_tau <= (29/7) N_beta and N_beta <= (2 tau^-beta + 16) N_tau, and for 1/2 <= beta <= 1 the inverse is
  below 2^(8 + 20 beta) in N_beta. For beta > 1/2 and a nonzero leading profile (as in the logarithmic theorem below)
  the normalized operator has domain D(L_fix) intersected with
  {c[h] = 0} and range exactly {f_y(0) = 0}. The commutator of the logarithmic multiplier with the transport needs
  only Lipschitz coefficients (P79, P81).
- Negative results (THEOREMS):
  * no bounded inverse at the far threshold sigma = gamma in the realization Z_gamma with norm ||<r>^(-1-gamma) h||_2,
    even after imposing finitely many exact linear constraints or adding a compact operator (no closed realization
    containing the constrained compact core is Fredholm; the accompanying artifacts, P61);
  * the same in the critical weighted Sobolev space X_(gamma,m), m >= 3, with norm squared
    sum_(j <= m) ||<r>^(j-1-gamma) D^j h||_2^2: U is bounded there, h and U[h] are locally C^(1,a) and c[h] is
    continuous, yet slowly cut-off packets r^gamma sin(5 theta) chi((log r - L)/L) with defect O(1/L + e^(-(1-gamma)L/2))
    show that no closed operator on X_(gamma,m) + R^p into X_(gamma,m) + R^q acting as B + K on the constrained compact
    zero-strain core is upper semi-Fredholm (the accompanying artifacts, P64);
  * the same with logarithmic weights (1 + log <r>)^kappa, any real kappa, and for closed block operators on
    X + E into X + F, E and F arbitrary Banach spaces of tail coordinates, acting as (B h + K h, Q h) on the
    constrained compact core with K and Q compact (angular and exponent boundary equations have Q = 0 there). A tail
    r^gamma sum_(q = 0..N) (log r)^q Theta_q, smoothly cut off near the origin, with Theta_q in H^m(S^1) and Theta_N
    not identically zero, lies in the logarithmic space exactly when kappa < -N - 1/2, and then its highest
    asymptotic coefficient is not a continuous trace (the accompanying artifacts, P68). Not covered: a noncompact bulk observation,
    a changed remainder norm, or a domain without the compact core;
  * the strain trace is not continuous at s = 0, even on functions with vanishing center jet, and in N_(s,R) its norm is
    asymptotic to 1/(8 (pi s)^(1/2)) uniformly in R >= 1 (1/(8 (2 pi s)^(1/2)) on {h_y(0) = 0}; the accompanying artifacts, P69).
    With the logarithmic gain (1 + log(1 - Delta))^beta in place of J^s, the trace is continuous exactly when
    beta > 1/2, and no positive gradient Hoelder exponent is controlled for any beta (the accompanying artifacts, P70); the
    certified residual lower bounds hold in that space as well (P71). At the endpoint beta <= 1/2 an explicit compact
    C^1 density with vanishing first derivatives at the origin lies in the space and its circular strain integrals
    diverge like log log log(1/eps) (P74), and for beta > 1/2 the quadratic term U[h].grad h is not continuous at 0
    from the space into itself, even on {h_y(0) = c[h] = 0} (P76);
  * a far-field spectral line: in X_(b,m), -3 < b < 1, oscillatory packets r^(b + i tau) give approximate eigenvectors
    for every point c_l b - 1 + i c_l tau of the full normalized operator (with finite augmentations and compact
    perturbations). Hence any resolvent point z satisfies ||(T - z)^-1|| >= 1/|Re z - (c_l b - 1)|, an inverse at zero
    has norm at least 1/|1 - c_l b| (at b = 1/5 this is 5/(5 - c_l) = 11258999068426240/7182522608187059 = 1.5676...),
    none exists at b = gamma, and a C0 semigroup cannot decay faster than e^(-(1 - c_l b)t) (the accompanying artifacts, P65). These
    statements concern X_(b,m); they are not transferred to N_s or N^w_s;
  * no bounded H^3 inverse for the frozen outgoing operator;
  * the weighted quantity ||r (1 + r^2)^-1 F||_2 does not bound ||F||_Hdot^-1 (annular dilation counterexample);
  * the correct Hardy bound on odd-in-y functions is ||F||_Hdot^-1 <= ||r F||_2.

## 5. Rough-velocity inverse and conditional existence (THEOREMS)

The hypothesis lists are in Appendices A and B; the accompanying artifacts give the full statements, arithmetic
and complete proofs.

- Norm: N_s(g) = E_2(J^s g), J = (1 - Delta)^(1/2), 0 < s <= 1/2, with E_2 as in section 4. N_s embeds with norm 1 in
  H^(2+s); ||grad g||_inf, ||DU[g]||_inf <= c_s N_s(g), c_s = [2 (pi s (1 + s))^(1/2)]^-1; ||g||_(C^(1/2)) <= N_s(g).
- Coefficient sum: M* = |c_l| + ||DU_bar||_S + ||omega D^2 U_bar||_S + ||omega D^3 U_bar||_S + ||D rho_bar||_S
  + sum_(j=2..4) ||omega D^j rho_bar||_S, where ||T||_S is the sum of the suprema of all ordered components. For state
  131, M* <= 2 + 6 + 24 + 160 + 22 + 32 + 80 + 2048 = 2374 (THEOREM; certified sups including omega |D^3 U_bar| <= 10 and
  omega |D^4 rho_bar| <= 128 in Frobenius norm).
- Rough-velocity theorem. If the reference satisfies the structural hypotheses (B0) and (B0n), the E_2 decay 1/10, the
  low decay 19/5 and M* <= 4096, then for every k with N_s(k) finite the maximal
  distributional realization of A_k = L_fix + U[k].grad in N_s generates a semigroup with
  ||exp(t A_k)|| <= exp[-t (1/10 - 1024 s M* - 128 N_s(k)/s^(1/2))]; when the rate is positive A_k is bijective with
  inverse bounded by its reciprocal. Ingredients: the exact Bessel kernel of J^s (second moment 2s, weighted first
  moments 17s and 54s), [J^s, X.grad] J^-s = s(I - J^-2), a Taylor bound for the coefficient commutators
    (background loss 1024 s M*), a weighted Kato-Ponce type commutator and product bound for the rough transport with
  W = U[k] in H^(2+s), the weighted Riesz bound 9/5 for the top term, and smooth approximation of k with
  identification of the limit generator.
- Sharper rate (THEOREM). Under the eight separate bounds (B9c) (|c_l| <= 2, ||DU_bar||_S <= 6,
  ||omega D^2 U_bar||_S <= 24, ||omega D^3 U_bar||_S <= 160, ||D rho_bar||_S <= 22, ||omega D^j rho_bar||_S <= 32, 80,
  2048 for j = 2, 3, 4; certified for state 131) and 0 < s <= 1/1024 the rate is 1/10 - 4800 s - 5 N_s(k)/s^(1/2).
  The proof keeps the four components (P, 128 a, 512 b, 512 (20/21)^(1/2) H) of E_2 separate: each background
  coefficient acts only at its own derivative level, the commutator energy is s e^T K e with an explicit 4 x 4 matrix
  whose symmetric part has row sums at most 19053/4 < 4800, and the rough transport cost per unit n E^2/s^(1/2)
  (n = N_s(k), E = N_s(g)) is at most A_s x^2 + B_s x + (13/10)(1 - x^2) with x = P/E, which is increasing on [0, 1]
  with maximum 217/50 + (1049/5) s < 5.
- Conditional existence, version (b) (THEOREM). With s = 2^-18 and radius r = 2^-16 under (B9c): rate
  >= 1/10 - 4800/2^18 - 5/128 = 873/20480 > 1/24, K_H <= 24, d = c_s r = 0.0022039... < 1/400,
  K_L <= (19/5 - d)^-1 < 1, C_B = c_s, contraction constant d/(19/5 - d) < 1/1000. If
  N_s(R_tilde) <= r/24 = 1/1572864 = 6.3578287760416...e-7, there is exactly one h with N_s(h) <= 2^-16, c[h] = 0 and
  F(rho_tilde + h; c_l) = 0, and ||h||_Hdot^-1 + ||h||_(C^(1/2)) + M'(h) + |c[h]| <= 2^11 N_s(h) <= 24 * 2^11
  N_s(R_tilde) (M' the center moment with exponents p = 2^21, kappa = p + 4).
- Conditional existence, version (a) (THEOREM). With s = 2^-28 and radius r = 2^-27 under (B9) alone: background
  loss <= 2^22 s = 1/64, rough loss 128 r/s^(1/2) = 1/64, rate >= 11/160, K_H <= 20, contraction constant
  <= c_s r < 2^-13; the threshold is N_s(R_tilde) <= 2^-27/20 = 3.7252902984619140625e-10, with the constant 2^16 in
  place of 2^11 (p = 2^31).
- Verification status of one step: an external adversarial referee of the version (a) proof confirmed every constant
  and asked for one step to be written out in full: the construction of the low-space semigroup on Hdot^-1 and its
  agreement with the L^2 realization, which justifies applying K_L to differences of iterates. That step is now part of
  the verified proof (the accompanying artifacts, P8): the low semigroup is the extension by density of the high semigroup, the
  density is simultaneous in Hdot^-1 and L^2, and the L^2 Duhamel identity places every contraction difference in the
  low generator domain. Both versions stand with unchanged constants.
- Residual conversion: N_s(R) <= E^(1 - s)(2 Q^2 + 16410 E^2)^(s/2) + 34 s E, E = E_2(R), Q = ||omega D^3 R||_2. At
  s = 2^-18 this is at most 1.0003 E whenever Q <= e^25 E (at s = 2^-28, at most 1.0001 E + 2^-22 E whenever
  Q <= exp(10^4) E). So version (b) applies as soon as E_2(R_tilde) <= 6.355e-7 and Q <= e^25 E_2(R_tilde) are
  certified. Conversely (THEOREM), N_s(f) >= (1 - 34 s) E_2(f) for 0 < s < 1/34, and any partial square sum of the
  components of E_2 may replace E_2 on the right; this turns certified ordinary norms into lower bounds for N_s.
- Threshold arithmetic (interval arithmetic in an accompanying script; all constants proved):
  * version (b) (C_bg = 4800, c_U = 5): as stated 6.357e-7; best radius at s = 2^-18: 6.51e-7; optimal s = 1/240000:
    6.53e-7;
  * version (a) (C_bg = 1024 M*, c_U = 128): as stated 3.7e-10; best radius at s = 2^-28: 8.4e-10; optimal s: 8.6e-10;
    optimal s with M* <= 2374: 1.1e-9.
  In every case c_s r < 1/400, so the slope and contraction conditions hold with a wide margin.
- Weighted variant, Theorem D_w (THEOREM; a second conditional theorem, independent of (B1) to (B10m)). Weights
  <r> = (1 + r^2)^(1/2), omega_1 = <r>^(-1/5), omega_2 = (1 + 4 r^2)^(2/5) and w = (1 + r^2/R^2)^(-11/10) with
  R = 2^35; E^w(g)^2 = ||omega_2 D^2 g||_2^2 + 2^22 ||omega_1 D g||_2^2 + 2^53 ||w g||_(Hdot^-1)^2 and
  N^w_s(g) = E^w(J^s g), on the completion of the compactly supported smooth functions of the parity class. Hypotheses
  on the reference (global pointwise inequalities, Frobenius norms; u = U[rho] canonical, V = cX + u,
  A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]): the parity and
  growth structure, 9/5 < c < 37/20, a_0 = d_y rho(0) >= 1, exact normalization c + c[rho] = 1; the low matrix
  (2c + 1) I + sym Du + A >= (19/5) I (weakened to (5/2) I on r <= R below) with four decay-coefficient bounds (for
  example sup r^(2/5)|Du| <= 18); the
  weighted matrices (1 + c + V.D log omega_k) I - k sym DV + A >= I/2 for k = 1, 2 (omega_1 = <r>^(-1/5)); and
  |Du| <= 14/5, <r>|D^2 u| <= 3, <r>|D^3 u| <= 16, |D rho| <= 16, |D^2 rho| <= 3, <r>|D^2 rho| <= 8,
  <r>^2|D^3 rho| <= 32, <r>^2|D^4 rho| <= 512 (full list in Appendix B). All are certified for state
  131 (independent directed recomputations of three decay quantities give sup r^(2/5)|D rho| <= 19.94465,
  sup r^(2/5)|Du| <= 1.85619 and sup r^(-3/5)|u| <= 0.97743; THEOREM; the accompanying artifacts, P104). They imply energy decay of the frozen linearization at rate 1/5 in the low component and 1/20 in E^w. Then
  for 0 < s <= 2^-12 the maximal realization of A_k decays in N^w_s at the rate 1/20 - 2^23 s - 2^19 N^w_s(k)/s^(1/2). With s = 2^-30: if
  N^w_s(F(rho; c)) <= 2^-46 (about 1.4210e-14; sharpened to 2^-35 below), there is exactly one h with N^w_s(h) <= 2^-41 and c[h] = 0 such that
  F(rho + h; c) = 0 (high inverse 32, low inverse 6, contraction factor 3/1024 in the low metric), and the
  Hdot^-1 norm of w h, an adapted Hoelder norm, the center moment and |c[h]| are together at most 2^68 N^w_s(F). Since
  |h(X)| <= 2^13 max(1, r)^(1/5) N^w_s(h) and gamma > 1/5, the solution keeps the leading profile r^gamma Theta_0.
  The space admits residuals growing like r^q with q < 1/5, so the checkpoint residual (q = 0.1048) belongs to it and
  Theorem E does not apply. But the residual is large in N^w_s (THEOREM). The low component amplifies a far-field
  sector r^q E(theta) with -2 < q < 1/5 by a factor of order 2^(53/2) R^(q+2), because in two dimensions the Hdot^-1
  norm of a profile of size T^q on the annulus r ~ T is of order T^(q+2). This is made rigorous by duality: from
  L(J^-s g) <= 6 L(g) (improved to 11/10 in section 6, which would multiply every annular lower bound below by 60/11;
  the bounds are stated with the factor 6), N^w_s(F) >= (2^(53/2)/6) L(F), and L(F) >= |<w F, phi>|/||D phi||_2 for the explicit parity
  test function phi = chi(r/R) sum_m (e_m/d_m) sin(m theta), chi(t) = (t - 1)^2 (2 - t)^2 on 1 <= t <= 2,
  d_m = 1/35 + m^2/630, m = 1, 3, ..., 39, where e_m are the exact angular coefficients of the leading residual sector
  r^q E_1. On r >= R = 2^35 the residual equals the exact finite sector expansion built from the first two binomial
  orders of the four potential branches, up to a certified uniform error below 1.762e-18 r^q, so each sin(m theta) coefficient keeps the sign of e_m with an explicit lower bound.
  This gives L(F) > 4.4839e19 and N^w_s(F) > 7.0925e26 > 2^89 for every 0 < s <= 2^-12, more than 2^135 times the
  threshold 2^-46 and more than 2^124 times the sharper threshold 2^-35 below (768-bit certificate with an independent reconstruction of the 860 coefficients from the original
  checkpoint). A floating-point evaluation of the whole far field (all radii, mode-wise radial Green functions) gives
  L(F) of about 8.8e20 and 2^(53/2) L(F) of about 8.4e28 (FLOAT), about 120 times the certified bound. So membership in
  N^w_s is cheap, but smallness requires the far field to be accurate out to r ~ R = 2^35.
  Smaller radius (THEOREM). Theorem D_w also holds with R = 2^32, with the same s, r_0, eta and constants, if the four
  decay-coefficient bounds are taken with exponent 4/9 instead of 2/5 (bounds 190, 23, 23, 56; this needs
  4/9 < 1 - gamma). The radial commutator factor is then below 14.573 and the low energy margin above 0.2060571 > 1/5;
  the other estimates are uniform in R >= 1. For state 131 these bounds are certified from the original checkpoint,
  and the annular test at R = 2^32 gives L(F) > 5.6305e17 and N^w_s(F) > 8.906e24 > 2^82, a gap of more than 2^128
  over 2^-46 (2^117 over 2^-35).
  Lowering R reduces the norm of a growing residual only by about (R'/R)^(q + 2), far less than the gap.
  An earlier, much weaker certified bound, N^w_s(F) > 2^-18 from F(0, 1000) > 1/8 and the pointwise embedding
  |g(X)| <= 2^13 max(1, r)^(1/5) N^w_s(g), is superseded. A first version of this
  theorem (same space, background loss 2^92 s through a cruder low-order commutator) had the threshold 2^-78/24,
  about 1.38e-25.
  Sharper constants (THEOREM). Keeping the coefficients 2^-11 that the norm puts on the two lower derivative components
  (so ||<r>^(-6/5) h||_2, ||omega_1 D h||_2 <= E^w(h)/2048) in the localization step improves every later constant
  without changing the space or the hypotheses: ||D g||_inf <= 4 N^w_s(g)/s^(1/2), |g(X)| <= 16 max(1, r)^(1/5) N^w_s(g),
  the rough loss becomes 400 N^w_s(k)/s^(1/2) (instead of 2^19 N^w_s(k)/s^(1/2)), and the low bilinear constant 1820.
  The decay rate of A_k is 1/20 - 2^23 s - 400 N^w_s(k)/s^(1/2) for 0 < s <= 2^-12. At s = 3 * 2^-31, r_0 = 5 * 2^-32:
  if N^w_s(F) <= 2^-35 (about 2.9104e-11), there is exactly one normalized h with N^w_s(h) <= r_0 and F(rho + h; c) = 0
  (decay rate above 6283/245760 > 1/40, high inverse 40, low inverse 6, contraction factor below 2/5 in the low
  metric, output bound 2^58 N^w_s(F), improved to 2^28 N^w_s(F) below). This holds at R = 2^35 and at R = 2^32; it improves the threshold by a factor
  2048. The checkpoint gaps over it are more than 2^124 (R = 2^35) and 2^117 (R = 2^32).
  Smallest radius (THEOREM). For a real density the positive and negative angular modes of the input have equal
  energy. Keeping this pairing and the cross term in ||(B - I)h/2||^2, where B = (d_x - i d_y)^2 (-Delta)^-1 and
  U_2 + i U_1 = (B - I)h/2, a weighted Schur test on the resulting three-diagonal comparison matrix bounds the canonical
  velocity in the weighted Hdot^-1 norm by sqrt(75/4) < 13/3 (instead of 13/2), uniformly in R and 0 <= sigma <= 11/5;
  the same pairing lowers the radial commutator coefficient from 14.573 to 10.339 < 21/2. With the decay-coefficient
  bounds (186, 22, 22, 56) (exponent 4/9, certified for state 131 from the original checkpoint) the low energy margin
  at R = 2^31 is above 14093/70000 > 1/5, so Theorem D_w holds at R = 2^31 with the constants of the previous
  paragraph (threshold 2^-35). The annular test at R = 2^31 gives L(F) > 1.3084e17 and N^w_s(F) > 2.0697e24 > 2^80,
  a gap of more than 2^115.
  Independent recomputation of the gap. A program of the numerical work, written separately from the verification
  programs, bounds L(F) from below at R = 2^35 with a different test function (a single mode sin(theta) and a smooth
  log-radial bump on 2^34 <= r <= 2^36), from its own exact sectors and rigorous adaptive integration; an independent
  audit of it recomputed the pairing from freshly reconstructed sectors and confirms L(F) > 1.1221e19 and
  N^w_s(F) > 1.77498e26 > 2^87, a gap of more than 2^122 over 2^-35 (THEOREM). The same program also evaluates the
  combined test (all leading modes, as above) with exact integration of the radial weight; an independent audit
  (fresh reconstruction of the 860 coefficients, its own exterior sectors and remainder, 384-bit log-coordinate
  quadrature) confirms L(F) > 3.7247e17, 1.6026e18, 1.2761e20 and N^w_s(F) > 5.8916e24, 2.5351e25, 2.0186e27 at
  R = 2^31, 2^32, 2^35, gaps of more than 2^117, 2^119 and 2^125 over 2^-35 (THEOREM). These are larger than the
  twenty-mode bounds above because the radial weight and the test energy are integrated exactly.
  Weaker matrix hypothesis (THEOREM). In the hypotheses of Theorem D_w at R = 2^31, the low matrix condition
  (2c + 1) I + sym Du + A >= (19/5) I can be replaced by M >= (5/2) I on r <= R (outside R the original baseline
  argument gives a margin above 853/2000 without any matrix floor), or by the position-dependent floor
  M >= 2/5 + (11/5) c r^2/(R^2 + r^2) on r <= R; every other hypothesis (the parity and growth structure, the weighted
  matrices, the derivative bounds including |D^2 rho| <= 3, the decay-coefficient bounds), the low margin
  14093/70000 > 1/5 and every later constant are unchanged. The floor 19/5 entered only as a baseline in the
  low-energy identity, where 5/2 - (11/10)(37/20) = 93/200 suffices. For a reference with other decay coefficients the
  finite radius beyond which the position-dependent floor is implied must be recomputed.
  Output constant (THEOREM). The strain is the origin trace c[h] = d_y U_2[h](0) of the canonical velocity gradient
  (including the local term of its kernel representation). Its multiplier -i xi_y xi_x^2/|xi|^2 has modulus
  |xi| a (1 - a)^(1/2), a = xi_x^2/|xi|^2, at most (2/(3 sqrt 3)) |xi| since 4/27 - a^2 (1 - a) = (a - 2/3)^2 (a + 1/3);
  with the Fourier bound (2 pi)^(-1) int |xi| |h_hat| <= 2 (2595/2048) N^w_s(h)/s^(1/2) of the embedding constants this
  gives |c[h]| <= N^w_s(h)/s^(1/2) (because (4 * 2595)^2 < 27 * 2048^2), and the bound extends to the completed space by
  uniform convergence of the velocity gradients. Adding the low norm (at most N^w_s(h)), the adapted Hoelder norm (at
  most 128 N^w_s(h)/s^(1/2)) and the center moment (at most 16 N^w_s(h)/s^(1/2)) gives
  L(h) + C_ad(h) + M(h) + |c[h]| <= 146 N^w_s(h)/s^(1/2) for s <= 2^-12, so the four-output constant of the inverse is
  146/(beta s^(1/2)), and at s = 3 * 2^-31 the solution of Theorem D_w satisfies
  L(h) + C_ad(h) + M(h) + |c[h]| <= 2^28 N^w_s(F) (since (40 * 146 * 2^16)^2 < 6 * 2^56). The threshold 2^-35, the
  radius 5 * 2^-32 and the contraction factor are unchanged.
- Second version: smooth commutator (THEOREM; the accompanying artifacts, P43). The background loss 2^23 s of the decay rate comes
  from the commutator of J^s with the frozen operator L_0 h = (cX + u).Dh - h + U[h].D rho. For a smooth reference it
  is smaller. Write J^s f = f + int kappa_s(z) (f(X) - f(X - z)) dz and J^-s f = b_s * f with explicit positive
  kernels (heat-semigroup subordination) whose moments are Gamma-function quotients of order s, for example
  int |z| b_s <= 2s and int |z|^2 b_s = 2s; split u(X) - u(Y) into its linear part, which gives the exact term
  -s Du : D^2 J^-2 f, and a second-order remainder of zero divergence, which needs only the kernel derivative; and
  factor the low component through q = D(-Delta)^-1(w h), with the parity Hardy inequality for the weight-derivative
  terms. For R >= 2^31 and 0 < s <= 2^-12, under |c| <= 2, |Du| <= 14/5, |D^2 u| <= 3, <r>|D^3 u| <= 16,
  |D^2 rho| <= 3, <r>^2 |D^3 rho| <= 32 and <r>^2 |D^4 rho| <= 512 (all part of the hypotheses of Theorem D_w), this
  gives E^w([J^s, L_0] J^-s H) <= (9325421/1200) s E^w(H) <= 2^13 s E^w(H). The decay rate of A_k becomes
  1/20 - 2^13 s - 400 N^w_s(k)/s^(1/2). At s = 3 * 2^-21 and r_0 = 5 * 2^-27 the two quantities 2^13 s and
  r_0/s^(1/2) equal 2^23 s and r_0/s^(1/2) of Theorem D_w at s = 3 * 2^-31, r_0 = 5 * 2^-32, so every estimate of
  the proof transfers (high inverse 40, low inverse 6, contraction factor 15/(16 sqrt 6) < 2/5, 40 eta = r_0): under
  the hypotheses of Theorem D_w (at R = 2^31, 2^32 or 2^35), if N^w_s(F) <= 2^-30 (about 9.3132e-10) at
  s = 3 * 2^-21, there is exactly one normalized h with N^w_s(h) <= 5 * 2^-27 and F(rho + h; c) = 0, and
  L(h) + C_ad(h) + M(h) + |c[h]| <= 40 * 146 s^(-1/2) N^w_s(F) <= 2^23 N^w_s(F). The threshold is 32 times larger than
  in the first version. For the checkpoint the annular bounds above (valid for every 0 < s <= 2^-12) give gaps of
  more than 2^112, 2^114 and 2^120 at R = 2^31, 2^32 and 2^35 (2^114, 2^116 and 2^123 with the exterior transfer of
  section 6); every exactly admissible refit misses it by more than 2^37 (2^60 for Mpen2 and d2; section 6). A consolidated audit of this theorem (maximal distributional domains and their identification with the generator domains, consistency of the low and high inverses on the nonlinear differences, the exact normalized range N_0 = {f : d_y f(0) = 0} and domain D(A_k) cap ker c, completeness of the normalized ball in the low metric) found no defect and rechecked every constant (the accompanying artifacts, P63). Checks: the rational constants are recomputed exactly and the kernel moments in interval
  arithmetic by a separate program.
- Logarithmic version (THEOREM; the accompanying artifacts, P83 to P88). Fix R = 2^31, tau = 2^-24, 1/2 < beta <= 1,
  epsilon = 2 beta - 1, C = tau^-beta epsilon^(-1/2), Q = (1 + tau log(1 - Delta))^beta, omega_0 = <r>^(-6/5),
  omega_1 = <r>^(-1/5), omega_2 = (1 + 4 r^2)^(2/5), w = (1 + r^2/R^2)^(-11/10), P_j(g) = ||omega_j D^j g||_2,
  L(g) = ||w g||_(Hdot^-1) and M(g)^2 = P_2(Q g)^2 + 2^22 P_1(Q g)^2 + 2^53 L(g)^2, on the completion of the compact
  smooth S1 core (a space of tempered distributions with continuous first derivatives and a continuous strain, P83,
  P84). Hypotheses on a smooth sublinear S1 reference rho with u = U[rho]: 9/5 < c < 37/20, a_0 = rho_y(0) >= 1,
  c + c[rho] = 1; with V = cX + u and A = [[rho_y, -rho_x/2], [-rho_x/2, 0]], the matrices
  M_low = (2c + 1) I + sym Du + A and M_j = (1 + c + V.D log omega_j) I - j sym DV + A satisfy
  M_low >= (2/5 + (11/5) c r^2/(R^2 + r^2)) I on r <= R and M_1, M_2 >= I/2 everywhere; the decay bounds
  sup r^(4/9)(|D rho| + r |D^2 rho|) <= 186, sup r^(-5/9)|u| <= 22, sup r^(4/9)|Du| <= 22, sup r^(13/9)|D^2 u| <= 56;
  the derivative bounds |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, <r>|D^3 u| <= 16, |D^2 rho| <= 3,
  <r>|D^2 rho| <= 8, <r>^2 |D^3 rho| <= 32, <r>^2 |D^4 rho| <= 512; polynomial growth of every derivative of rho
  (with the velocity bound this gives polynomial growth of every derivative of u, by interior estimates for
  Delta u_1 = rho_xy, Delta u_2 = -rho_xx; THEOREM; the accompanying artifacts, P103); and a nonzero leading profile:
  T^(-1/c) rho(TX) -> r^(1/c) Theta(theta) uniformly on compact annuli as T -> infinity, with Theta continuous and not
  identically zero. Comparing the two lists, the numerical hypotheses are those of
  Theorem D_w at R = 2^31 (polynomial growth is a separate qualitative hypothesis, supplied by P91 for finite
  potentials); an independent consolidated
  dependency and domain audit (P88) confirms this, and shows that the third density derivative enters the top energy
  directly, through the term (16/3) B3 P_0 P_2 with B3 = sup <r>^2 |D^3 rho|. Conclusions (P85): for M(k) <= r_0 = 2^-20 tau^beta epsilon^(1/2) the maximal
  operator A_k h = (cX + u + U[k]).Dh - h + U[h].D rho generates a semigroup with ||exp(t A_k)|| <= e^(-t/32) and is a
  bijection with M(A_k^-1 f) <= 32 M(f); the normalized operator has domain D(A_k) intersected with {c[h] = 0} and, if
  c[k] = 0, range {f : f_y(0) = 0} with inverse at most 32; if M(F) <= eta = r_0/32 there is exactly one h with
  M(h) <= r_0 and c[h] = 0 such that rho + h is an exact solution with the same exponent and leading angular function,
  and every solution in that ball has c[h] = 0. Because U[h].grad h is not continuous at 0 from M into M (P76), the
  fixed-point map is a contraction of factor 3/16 in the low metric L on the M ball. The derivative commutator needs
  only a Lipschitz velocity (P81), the products are controlled by the logarithmic estimates of P78, P80, P82 and P84,
  and the native M norm and the norm N(g), which is M with the low component L(g) replaced by L(Q g), define the same
  completion (P83). In the native norm the fixed operator decays at rate 1/25 - 2^16 tau, with inverse at most 28 at tau = 2^-24
  (P83); the inverse bound 29 of the logarithmic linear inverse above refers to the tau = 2^-20 norm N_tau (P75).
  Equivalence of the norms does not transfer these operator constants. Outputs (P87): H(h) <= 64 M(h) for the adapted C^(1/2) density norm of answer 2,
  M_3(h) <= 6 C M(h) for the projected singular moment (the projection onto the third harmonic cannot be dropped: the
  full absolute moment is unbounded on these spaces, P97), |c[h]| <= |h_y(0)|/4 + M_3(h) + P_0(h) from the contact form of
  the strain, |c[h]| <= 4 C M(h), and L + H + M_3 + |c| <= 128 C M(h) <= 2^12 C M(A_k h). The threshold
  eta = 2^-25 tau^beta epsilon^(1/2) is at most 1.083e-12 (its maximum 2^-37 (24 e log 2)^(-1/2) = 1.08199e-12 is
  attained at beta = (1 + 1/(24 log 2))/2, about 0.530) and below 2^-37 for every beta. Exclusions (P86): N_beta(h) <= 2^32 tau^-beta M(h) for the tau = 1 norm of answer 3, so by P73 the closed M balls
  of radius 2^25 tau^beta about the checkpoint and 2^-11 tau^beta about Mpen2 and d2 contain no exact solution of any
  exponent; and M(F) >= 2^(53/2) L(F) with the certified low witnesses gives M(F) > 35350195123413029343106947
  (checkpoint), M(F) > 1935892108 (Mpen2) and M(F) > 1936535207 (d2). These floors are lower bounds of finite norms
  (THEOREM; the accompanying artifacts, P106): a smooth S1 function f with |D^m f| <= C_m <r>^(q-m) for m <= 4 and some q < 1/5 lies
  in the completion of the compact smooth core under M_A for every finite R >= 1, A > 0, tau > 0 and 0 <= beta <= 1,
  and the actual residuals of the checkpoint (q = 2 gamma - 1) and of Mpen2 and d2 (q = gamma - 6 delta < 0) satisfy
  this. No upper bound on these norms is asserted. The power 1/5 is sharp (THEOREM; the accompanying artifacts, P108): a smooth S1
  function equal to r^q (log r)^(-a) Theta(theta) for r >= e^2, with Theta nonzero, lies in the completion for every
  such R, A, tau, beta if q < 1/5, for none if q > 1/5, and at q = 1/5 exactly when a > 1/2. In particular the leading
  profile direction (exponent gamma > 1/5) is not in the correction space, in agreement with the fixed leading profile
  of the theorem. Checks: every rational constant, the floors (from
  the stored witness records, with their hashes) and the contact formula on five Gaussian inputs against an exact
  Fourier evaluation of the strain are recomputed by separate programs (the accompanying artifacts).
- Parametric logarithmic version (THEOREM; the accompanying artifacts, P89 to P91). Retain every hypothesis of the logarithmic
  version except the three bounds replaced below: R = 2^31, the structure and normalization, the matrix and decay
  hypotheses, the five bounds |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, |D^2 rho| <= 3, <r>|D^2 rho| <= 8,
  polynomial growth of every derivative of the reference and the nonzero leading profile; replace the other three by <r>|D^3 u| <= U3, <r>^2 |D^3 rho| <= B3, <r>^2 |D^4 rho| <= B4 with arbitrary finite constants.
  Put a = 198 + B3/24, G3 = a^2 + 352, choose Astar >= 2048 with 7 Astar^2 >= 200 G3, put
  Kstar = max(525, 432 + (272 U3 + 816 B3)/Astar, 312 + (1088/3) B3 + (2176/(3 Astar)) B4), take
  0 < tau <= min(2^-20, 1/(768 Kstar)) and Mstar(h)^2 = P_2(Qh)^2 + Astar^2 P_1(Qh)^2 + Astar^2 2^31 L(h)^2. Then every
  conclusion of the logarithmic version holds in Mstar with the same r_0 = 2^-20 tau^beta epsilon^(1/2),
  eta = r_0/32, inverse 32, low inverse 6 and contraction 3/16; the decay rate is
  1/25 - (3/2) Kstar beta tau (1 + 11 tau)^3 - 2^12 C Mstar(k) > 1/32 (P89). Astar depends on B3 because U[h].D^3 rho
  enters the top energy before any logarithmic commutator; for B3 <= 4096 Astar = 2048 suffices, and U3 = 16,
  B3 = 32, B4 = 512 recover the logarithmic version. Exclusions for every parameter choice (P90):
  N_beta(h) <= 2^36 tau^-beta Mstar(h), so the closed Mstar balls of radius 2^21 tau^beta about the checkpoint and
  2^-15 tau^beta about Mpen2 and d2 contain no exact solution of any exponent (at least 2^41 and 32 times r_0), and the
  residual floors are Astar/2048 times those of the logarithmic version, more than (Astar/2048) 2^119 and
  (Astar/2048) 2^65 times eta < 2^-35. A direct comparison of the norms enlarges all these excluded balls (THEOREM;
  the accompanying artifacts, P111): E_R(h) <= (1 + 2 pi tau beta) Mstar(h) <= (1 + 7 tau) Mstar(h) whenever R >= 2^31,
  Astar >= 2048, 0 < tau <= 2^-20 and 0 <= beta <= 1 (so also for M), by a positive gamma-mixed heat kernel
  representation of Q^-1 with first moment at most pi tau beta, while P73 excludes E_R(h) <= 2^57 about the
  checkpoint and E_R(h) <= 2^21 about Mpen2 and d2. Hence the closed native balls of radius 2^77/(2^20 + 7) > 2^56
  about the checkpoint and 2^41/(2^20 + 7) > 2^20 about Mpen2 and d2 contain no exact solution of any exponent, for
  every 0 < tau <= 2^-20 and 0 <= beta <= 1; residual floors and thresholds are unchanged. Caps (P91): for a finite potential
  chi = sum a_(j,m,k) (x^2 + y^2)^(k-m) Re(x + iy)^(2m) (1 + r^2)^(p_j - k), p_j = (3 + gamma - j delta)/2, an explicit
  rational C_d (a sum of ceil|a_(j,m,k)| times a combinatorial factor) gives |D^d chi| <= C_d <r>^(3 + gamma - d) on
  the whole plane, hence U3 = B3 = 2 C_6 and B4 = 2 C_7 are valid, and every derivative has polynomial growth. For the
  checkpoint this gives U3 = B3 = 2^107, B4 = 2^114, Astar = 2^105, tau = 2^-126 (not needed there: it satisfies the
  fixed bounds); for Mpen2 and d2, U3 = B3 = 2^191, B4 = 2^201, Astar = 2^189, tau = 2^-210. All certified derivative
  violations of Mpen2 and d2 (section 6) are of these three kinds, so with these parameters no certified violation
  excludes them, and at these parameters the gaps of P90 exceed 2^243. For d2 every hypothesis on the reference is
  verified (P105): the source audit gives the parity, the finite potential form, c + c[rho] = 1 and
  a_0 = 47238706681952399067752453371665/4589704466829443526249565650944 > 1, with 9/5 < c < 37/20; the leading
  potential is that of the checkpoint, so T^(-gamma) rho(TX) converges on compact annuli to its nonzero leading
  density; P91 gives polynomial growth and the three caps; P95 gives M >= (19/5) I, which implies the low matrix
  condition because 2/5 + (11/10) c <= 487/200 < 19/5, M_1, M_2 >= I/2, the five fixed bounds and the four decay
  bounds (the two density halves 93 + 93 give 186); and the parameter rule holds exactly
  (7 Astar^2 >= 200 G3 with ratio about 1.26, 768 Kstar tau = 0.53125...). Hence for d2 the residual hypothesis is
  the only one that fails, with Mstar(F) > (Astar/2048) 1936535207 = 2^178 * 1936535207 and
  Mstar(F)/eta > 2^(178 + 30 + 35) = 2^243; the residual is in the native space (P106). For Mpen2 the other global
  hypotheses are not verified.
  Checks: the rational constants, the parameter rule on random rational inputs, the combinatorial lemmas of P91 against
  symbolic derivatives, and C_6, C_7 and the parameters of the three references (from the exact coefficients of the
  checkpoint and the stored coefficient ceilings of the refits) are recomputed by a separate program.

## 6. Approximate solutions and residual (THEOREMS where marked; otherwise FLOAT)

- Checkpoint (THEOREM): with omega_2 = (1 + 4 r^2)^((1 - sigma)/2),
  * ||omega_2 D^2 R_bar||_2 > 2.50924 for every 2 gamma - 1 < sigma <= 2/5;
  * the bound is > 59.44, 25.17, 7.108, 4.146 at sigma = 0.15, 0.2, 0.3, 0.35;
  * the norm is infinite for sigma <= 2 gamma - 1;
  * method: exact finite potential through angular order 10, all 157 residual sectors, exact radial integration over
    r >= 100, 384-bit interval arithmetic.
    Its residual lies outside X_U and N_s because its L^2 and Hdot^-1 tails diverge.
- Certified whole-plane residual norms (THEOREM). For an exact finite rational potential, every derivative of the
  residual is an exact rational polynomial in the compactified variables t = r^2/(1 + r^2), cos 2 theta and
  w = (1 - t)^((1 - gamma)/2), times explicit factors, so the weighted L^2 norms reduce to exact beta integrals, with a
  rigorously enclosed series for the weight omega = (1 + 4 r^2)^(2/5); there is no quadrature. An independent second
  program (different variable u = 1 - t, all ordered cross terms, point comparisons with Cartesian potential jets)
  recomputes the values at 640 bits. Results:
  * checkpoint: ||omega D^2 R||_2 in [25.1892236171285365, 25.1892236171285379], ||omega D^3 R||_2 in
    [2.5042775321848363, 2.5042775321848366]; ||R||_2, ||r R||_2 and ||grad R||_2 infinite;
  * best refit (m10, below): ||grad F||_2 in [0.3444735104934888, 0.3444735104934889], ||omega D^2 F||_2 in
    [5.0099247071386049, 5.0099247071386053], ||omega D^3 F||_2 in [12.3311345810175309, 12.3311345810175319];
    ||F||_2 and ||r F||_2 infinite.
- FLOAT residual profile of the checkpoint:
  * near 0 it is small (at r = 1: |F| about 1e-6 to 6e-6, |D^2 F| about 3e-3);
  * the weighted norms are dominated by r > 1e3 (the growing E_1 sector) and 10 < r < 1e3;
  * a radial cutoff of the sector difference does not reduce these norms, since the cutoff error on the transition
    annulus has the size of the tail it removes.
- Improved exact finite potentials (FLOAT fit; exact rational coefficients; exactness checked in rational arithmetic):
  * construction: the 860 generators plus up to 340 new ones; Theta_0, c_l and the center condition unchanged;
  * the first far-field sector is exactly stationary (E_1 = 0), so the residual exponent is p_3 = 3 gamma - 2, about -0.343;
  * independent exact audit (THEOREM) of the two best refits of the first family (up to 1020 generators): Theta_0 and
    c_l are preserved, the center condition holds and E_(0,0) = E_(1,0) = 0; E_(2,0) is nonzero (angular quarter norms
    0.771 and 0.596), so their residuals are outside unweighted Hdot^-1; their center slopes are 10.29706 and 10.29584;
  * for one of them the global matrix bound M >= (19/5) I is certified independently (1346 leaves, 384-bit
    recomputation), so the low inverse 5/19 transfers to it (THEOREM). The high-level certificates have not been
    transferred;
  * two refits with 1200 generators and Legendre radial blocks in the mid field (m10, m12) have the same exact
    properties (independent exact audit, THEOREM): E_(0,0) = E_(1,0) = 0, E_(2,0) nonzero (quarter norms 0.29865 and
    1.11081), center slopes 10.29563 and 10.28661;
  * best refit so far (m10): weighted norms at sigma = 0.3
    (||<r>^-1.3 F||, ||<r>^-0.3 DF||, ||<r>^0.7 D^2 F||) 0.012, 0.076, 1.85 against 0.050, 0.436, 4.39 for the
    checkpoint on the same grid (FLOAT); the certified whole-plane values are listed above; E_2 at exponent -0.343 is
    still present, so ||F||_2 is infinite; its near field is worse than the checkpoint's (|F| at r = 1 about 8e-5);
    * a refit m14 with three exact stationary sectors (independent exact audit, THEOREM: Theta_0, c_l and the
    normalization unchanged, a_0 = 9.92526..., sectors (0,0) to (3,0) zero) still has the nonzero sectors (4,0),
    (0,1), (5,0) and (1,1) of exponent >= -2 (quarter-plane angular norms 172.84, 668.58, 131.36, 8245.33), so by the
    necessary condition below its affine class contains no exact solution;
  * the near-field and mid-field residual levels of these fits are observations of particular optimization outputs,
    not lower bounds over their finite families.
  * None of these is in X_U or N_s yet: that needs residual exponent below -2, i.e. five exact sectors and no
    descendants above -2.
- Each derivative multiplies the residual norm by about 15 to 25 (FLOAT). For the best refit, with the weights of E_2,
  the gradient component 128 ||grad F||_2 = 44.09... (THEOREM) dominates the finite part of the norm, ahead of the
    omega-weighted Hessian (5.0099, THEOREM), whose mass lies mostly in 32 < r < 256 (FLOAT); the L^2 and Hdot^-1 components
  are infinite.
- Angular resolution of FLOAT diagnostics (THEOREM). The quarter-plane midpoint rule with N angles misses entirely the
  nonzero smooth parity function eta(r) sin(theta) [1 + cos(4 N theta)]^2, all of whose derivatives through order 3
  vanish at the nodes. For a finite potential of largest angular frequency 2M, N >= 2M + 6 angles integrate the
  squared angular norms of all residual derivatives through order 3 exactly (in exact arithmetic); for the repaired
  potentials (M = 59) 128 angles suffice. Floating-point norms of enlarged potentials computed with fewer angles are therefore not
  controlled. No FLOAT value is used in a THEOREM.
- Tail repair of the checkpoint (THEOREM). With chi_0 the exact checkpoint potential and chi_inf the sum of the six exact
  homogeneous stationary potentials (finite cosine polynomials from an exact triangular inversion), and a fixed smooth
  radial cutoff eta_R equal to 0 on r <= R and 1 on r >= 2R, the potential chi_R = chi_0 + eta_R (chi_inf - chi_0)
  gives a density and canonical velocity equal to the checkpoint's on r < R and to the stationary sums on r > 2R. For
  R = 2^1024: on r >= R, |D^j rho_R|_F + |D^j u_R|_F <= 2^206 r^(gamma - j) for j <= 7, which gives every coefficient
    inequality there (for example M_2 >= (4082593/6579200) I, M_3 >= -(1011919/822400) I, the component bounds (B9c)),
    the residual lies in N_s, and N_s(F(rho_R)) >= 2^1028.
- Algebraic tail repair (THEOREM). Write a reference potential in the canonical generators
  G_(j,m,k) = r^(2k)(1 + r^2)^(a_j - k) cos(2m theta), a_j = (3 + gamma - j(1 - gamma))/2, and let L_(j,m) and D_(j,m)
  be its leading and first-descendant moments in branch j and mode m. For an integer K >= 3 add, for j = 2, ..., 5,
  the multiple (C_(j+1)(m) - L_(j,m)) G_(j,m,m+K), and for j = 0, 1 the unique combination of G_(j,m,m+K) and
  G_(j,m,m+K+1) (determinant -1) that sets the leading moment to C_(j+1)(m) and the first descendant moment to 0, where
  C_n are the exact stationary potentials. The result is a finite rational potential with unchanged potential Taylor
  coefficients below degree 2K (so a_0, c[rho] and the normalization are exact), all eight residual sectors with
  exponent >= -2 equal to zero, first nonzero sector r^(p_7) (full-circle angular norm 3081.2744...), and residual in
  N_s. Ten variants (checkpoint and m10, K = 4, 8, 16, 256, 4096) are constructed and audited in exact arithmetic. Two
  independent 640-bit evaluators agree at eight points for each of the four variants with K = 4 and 16; at X = (1, 1) the least eigenvalue of M is about -395.20,
  -315.68, -167.09 and -9.156 for checkpoint K = 4, m10 K = 4, checkpoint K = 16 and m10 K = 16, and
  N_s(F) >= 4564, 11919, 2386 and 289. A scan of all ten variants on a 73 x 65 polar grid (radii 2^(i/4) from 2^-6
  to 2^12), with every minimizing point re-evaluated by both evaluators, certifies a negative eigenvalue of M for
  every variant with K <= 256 and least eigenvalue below 3.417 < 19/5 at r = 2^4.75, theta = 0 for the checkpoint
  variant with K = 4096. The residual values at the same certified points give N_s(F) > 9281, 13448, 7618, 4575, 4825,
  1305, 605 and 208 for checkpoint and m10 with K = 4, 8, 16 and 256. For the m10 variant with K = 4096 no sampled
  point fails (this is not a positivity proof), and
  the certified point value |F(30, 40)| > 11.48 gives N_s(F) > 11.48 (25.44 for the checkpoint variant). For the m10
  variant with K = 8 the whole-plane Hessian residual ||omega D^2 F||_2 lies in [863401.8215612798, 863401.8215612799]
  (1024-bit ball arithmetic in two independent radial bases, checked against Cartesian jets). The same method
  (1280 bits, all ten Cartesian components through order 3 checked at seven points) gives all residual norms of the m10
  variants with K = 8 and 16: ||r F||_2 = 35870.578..., ||F||_2 = 10040.631..., ||grad F||_2 = 40432.726...,
  ||omega D^3 F||_2 = 6366619.69... for K = 8 and 31813.818..., 5544.173..., 17065.380..., 366729.212...
  (||omega D^2 F||_2), 2153660.01... for K = 16. With the residual conversion, the reverse comparison and the parity
  Hardy bound ||F||_Hdot^-1 <= ||r F||_2, at s = 2^-18: 7344656 < N_s(F) < 19372856 (K = 8) and
  3600047 < N_s(F) < 16301199 (K = 16). The repair changes the field at all radii beyond the center jets, so no
  certificate of the original reference transfers; these numbers concern only the explicit variants.

- Uniform residual bound for the fitting family (THEOREM). Let chi = sum a_(j,m,k) G_(j,m,k) over 0 <= j <= 5,
  0 <= m <= 59, m <= k <= 75 with arbitrary real coefficients, subject only to the affine conditions that the leading
  cosine polynomial of branch j is the exact stationary profile C_(j+1) (j = 0, ..., 5) and that the first descendant
  polynomials of branches 0 and 1 vanish. Write F for the residual, p* = gamma - 6 delta = 1 - 7 delta and
  e(theta) = sum_m e_m sin(m theta) for its coefficient of r^(p*). Then e is the same for every such chi (full-circle
  norm 3081.2744...; odd m <= 139), and
    ||F||_(Hdot^-1)^2 >= (pi/2) D^2 sum_m e_m^2 / (m^2 + (1 + 2 C_D)^2) > (2.6775e-7)^2,
  where, for the 1852 exponents a_0 < a_1 < ... of the set {l delta/2 + k - 2 : 1 <= l <= 12, 0 <= k <= 154} that are
  >= a_0 = 7 delta/2 - 2, D = (2 a_0 + 1)^(-1/2) prod_(j >= 1) (a_j - a_0)/(a_j + a_0 + 1) = 4.974e-5 and
  C_D^2 = sum a_j^2 + sum_(i<j) (2 a_i + 1)(2 a_j + 1), C_D = 202394.39. With N_s >= (1 - 34 s) E_2 and
  E_2 >= 2^9 (20/21)^(1/2) ||F||_(Hdot^-1), N_s(F) > 1.3376e-4 at s = 2^-18, more than 210 times 1/1572864. Proof
  outline: in u = 1/(1 + r^2) each sine mode of F is sqrt(1 - u) u^(-1/2) H_m(u) with H_m a sum of u^(l delta/2) times
  polynomials of degree <= 153 in 1 - u (a derivative count; one Cartesian derivative maps u^a t^k to u^(a + 1/2)
  t^(k - 1/2) times a linear polynomial in t = 1 - u). The eight imposed conditions remove exactly the eight powers
  below a_0, and the coefficient of u^(a_0) in w_m = (1 - u) u^(-2) H_m is e_m, because no branch j = 6 is present and
  the quadratic interactions entering that power involve only the fixed leading branches. The L^2(0, 1) distance of
  u^(a_0) from the span of the other powers is D (Mellin transform of the orthogonal residual). The dilation u d/du
  has a triangular matrix in the Gram-Schmidt basis whose entries are a_j on the diagonal and of absolute value
  ((2 a_i + 1)(2 a_j + 1))^(1/2) above it, so its norm on the span is at most C_D. On the cylinder s = log r the
  Hdot^-1 energy of a mode is pi <g, (-d_s^2 + m^2)^(-1) g> with g = r^2 F_m = (u(1 - u))^(1/2) w_m, and
  Cauchy-Schwarz with ||g'|| <= (1 + 2 C_D) ||g|| and ||g|| >= |e_m| D/sqrt(2) gives the bound. The constants were
  computed in 384- and 512-bit ball arithmetic and recomputed independently. The bound concerns this family only: a
  seventh branch or a different leading profile changes the argument.
- Sharper constant and higher radial degree (THEOREM). Replace k <= 75 by k <= K for any K >= 59, so that w_m lies
  in the span of the n_K = 12(2K + 5) - 8 powers {l delta/2 + k - 2 : 1 <= l <= 12, 0 <= k <= 2K + 4} that are
  >= a_0, and let D_K be the corresponding distance product. Then
    ||F||_(Hdot^-1)^2 >= (pi/2) D_K^2 sum_m e_m^2 / (m^2 + Q_n),  Q_n = (2n(n^2 + 2) + 1)/3, n = n_K.
  Proof outline: with tau = -log u and f(tau) = e^(-tau/2) w(e^(-tau)) (a unitary map from L^2(0, 1; du) to
  L^2(0, infinity; d tau) onto a span of n decaying exponentials e^(-b tau), b = a + 1/2 > 0), the orthonormal basis
  with Laplace transforms (2b_j)^(1/2)/(z + b_j) prod_(i<j) (z - b_i)/(z + b_i) gives ||tau f'||^2 <= n(n^2 + 2)/6
  ||f||^2 (a Hilbert-Schmidt bound, by explicit Cauchy-density moments). The cylinder identity
  ||d_s g||^2 = (1/2) ||u f + 2(1 - u) f'||^2 = 2 ||(1 - u) f'||^2 + (1/2) int (2u - 3u^2) |f|^2, together with
  1 - u <= tau and 2u - 3u^2 <= 1/3, gives ||d_s g||^2 <= Q_n ||g||^2, which replaces (1 + 2 C_D)^2. (A first
  sharpening, by writing the dilation matrix as the compression of the Volterra operator int_x^S minus I/2, gives
  ||u d/du|| <= (4S^2/pi^2 + 1/4)^(1/2) with S = sum (2a + 1), ratio more than 233 at K = 75 and K <= 349; it is
  superseded.) At K = 75: n = 1852, ||F||_(Hdot^-1) > 1.665e-6, N_s(F) > 8.320e-4, more than 1308 times
  1/1572864. At K = 779 (270180 coefficient slots) the ratio is more than 1.0035; at K = 780 the bound gives less
  than 0.99955 and decides nothing. The families are nested in K, so the case K = 779 implies every smaller degree.
  Constants: 384-bit gamma-function products and 512-bit direct products agree in all 21 recorded rows, and a third
  computation with interval arithmetic in a different library reproduces B_75, B_779 and B_780.
- Recursive dilation constant and radial degree up to 3675 (THEOREM). On the span of n exponentials e^(-b tau)
  (distinct rates b > 0) the operator A f = tau f' + f/2, the skew-adjoint part of the dilation, satisfies
  ||A f|| <= q_n ||f|| with q_1 = 1/2 and q_n^2 = (q_(n-1) + 1)^2 + 1/4, hence q_n <= c_n = n - 1/2 + log(2n - 1)/8.
  Proof outline: in the Laplace picture, with k_b = (2b)^(1/2)/(z + b) and the Blaschke factor B_b = (z - b)/(z + b),
  every F in the span is d k_b + B_b G with G in a span of dimension n - 1; A acts as -F/2 - z F', so
  A k_b = B_b k_b/2 and A(B_b G) = B_b A G - z B_b' G with |i omega B_b'(i omega)| <= 1 on the axis, and the triangle
  inequality with Cauchy-Schwarz over the two orthogonal pieces gives the recursion. Since Re <A f, f> = 0,
  ||tau f'||^2 = ||A f||^2 + ||f||^2/4, and the cylinder identity of the previous item gives
  ||d_s g||^2 <= (4 c_n^2 + 4/3) ||g||^2, which replaces Q_n = (2n(n^2 + 2) + 1)/3. At K = 75 (n = 1852):
  ||F||_(Hdot^-1) > 2.925e-5 and N_s(F) > 0.01461, more than 22986 times 1/1572864. At K = 3675 (n = 88252,
  1312740 coefficient slots) the ratio is more than 1.0004726; at K = 3676 the bound gives less than 0.9997658 and
  decides nothing. Constants: two computations in 512-bit ball arithmetic and a third in interval arithmetic in a
  different library agree.
- Seven branches (THEOREM for the bound; inconclusive). For potentials with branches j <= 6 whose first seven leading
  potentials are the stationary orders and with the residual sectors (h, 0), 0 <= h <= 6, (0, 1) and (1, 1) cancelled
  (and (2, 1) as well, in a second variant; these are the residual sector indices of the next item, which the proof in
  the accompanying artifacts writes with the shifted first index h + 1), the residual modes lie in the span of n = 14(2K + 5) - 9 (or - 10) powers of u, the
  distinguished power a* = 4 delta - 2 (the one of the radial power p_8) carries the fixed coefficient E_7, and the same
  argument (distance of u^(a*) from the span of the other powers, which need not all lie above it, and the recursive
  dilation constant) gives a valid lower bound. It is below 7e-13 times the unweighted threshold at K = 69 (below
  3e-12 in the second variant), the smallest radial degree admitted by the angular range m <= 69 of the seventh order,
  and it decreases with K. The cause is the distance factor: for large a each factor (a - a*)/(a + a* + 1) is about
  1 - (2 a* + 1)/a, and 2 a* + 1 = 0.581 against 0.133 for six branches. So this method gives no obstruction for seven
  branches.
- An exactly admissible seven-branch refit (THEOREM for the facts stated). The refit b6 of the numerical work (2902
  generators, 1842 canonical terms, branches j <= 6) is reconstructed exactly: its first seven leading potentials equal
  the stationary orders, the nine sectors (l, 0), l <= 6, (0, 1) and (1, 1) vanish, its slope at the center is
  a_0 = 15.42079..., and its residual sectors have first-quadrant angular norms 2521.06 for (2, 1) at r^(-2.343),
  4839.98 for (7, 0) (the sector E_7 of the previous item) and 9364.93 for (8, 0). So its residual lies in N_s and
  N^w_s. Certified point values give M_2(3, 4) < 0.46618 < 1/2, |D^2 rho(0, 1/5)| > 10.33 > 3 and
  <r>^2 |D^4 rho(3, 4)| > 27670 > 512, which violate three bounds of the weighted reference contract, and
  |F(6, 8)| gives N^w_s(F) > 0.23066, more than 2^32 times the threshold 2^-35.
- Necessary local distance (THEOREM). Let rho_bar be a smooth reference of the parity class with residual F and with
  the leading profile r^gamma Theta of the checkpoint (Theta not identically zero, U[rho_bar] = O(r^gamma)), and let
  n = N^w_s(h) for a correction h in the space of Theorem D_w (0 < s <= 2^-12, any R >= 1). Exponent rigidity: if
  rho = rho_bar + h is an exact solution for some exponent c', then c' = c. Indeed G_T(X) = T^(-gamma) rho(TX)
  converges uniformly on annuli to the homogeneous function G = r^gamma Theta (since |h| <= 16 max(1, r)^(1/5) n and
  gamma > 1/5), the rescaled equation is c' X.D G_T - G_T + T^(gamma - 1) U_T.D G_T = 0 with U_T bounded, the
  nonlinear term tends to zero in weak form, and the limit c' X.D G = G together with X.D G = gamma G forces
  c' = 1/gamma. No condition on the slope at the center is needed. With kappa = s^(-1/2), a = 4 kappa and
  g = max(1, r)^(1/5), the embeddings give |Dh| <= a n, |h| <= min(a|y|, 16 g) n and |U[h]| <= min(a r, 104 g) n,
  and the difference of the two equations, 0 = F + V_bar.Dh - h + U[h].D rho_bar + U[h].Dh, gives at every point
  |F(X)| <= A n + Q n^2, A = a|V_bar| + min(a|y|, 16 g) + B|D rho_bar|, Q = a B, B = min(a r, 104 g).
  The right side increases with n, so one certified point with |F(X)| > A q + Q q^2 excludes every exact solution with
  N^w_s(h) <= q. At s = 3 * 2^-31, certified enclosures at nine points give the dyadic radii q = 2^-11 (A2), 2^-13
  (A3), 2^-18 (A4), 2^-21 (A5, Mpen and A6dpen), 2^-22 (Mpen2) and 2^-16 (b6); all eight share the exact exponent
  and the leading potential moments of the checkpoint. For the checkpoint the point test gives only 2^-30, but an
  annular test does better. Integrating the difference equation against a C^1 test zeta supported in T <= r <= 2T
  moves the derivative off h:
    int F zeta = int h [V_bar.D zeta + (2c + 1) zeta] - int U[h].D rho_bar zeta + int h U[h].D zeta.
  With |zeta| <= Z, |D zeta| <= C/T, |U[rho_bar]| <= 22 r^(5/9) and |D rho_bar| <= 186 r^(-4/9) the right side is at most
  A_T n + Q_T n^2, A_T = 3 pi T^2 {H_T [V_T C/T + (2c + 1) Z] + B_T D_T Z}, Q_T = 3 pi T H_T B_T C, where
  H_T = 16 (2T)^(1/5), B_T = 104 (2T)^(1/5), V_T = 2cT + 22 (2T)^(5/9) and D_T = 186 T^(-4/9). For the test
  zeta_T = w_T chi(r/T) sum a_m sin(m theta) of the weighted residual bound (chi(t) = (t - 1)^2 (2 - t)^2 on [1, 2],
  a_m = e_m/(1/35 + m^2/630) from the exact leading residual sector, Z = S_0/16 and C = 91 S_0/160 + S_1/16 with
  S_0 = sum |a_m|, S_1 = sum m |a_m|) the certified pairing exceeds A_T q + Q_T q^2 at q = 2^-22 for T = 2^31, 2^32
  and 2^35. So no exact solution, of any exponent, has N^w_s(h) <= 2^-22, for every 0 < s <= 2^-12 and R >= 1; since
  2^-22 > 5 * 2^-32, the ball of Theorem D_w around the checkpoint contains no exact solution. Checks: for the point
  tests two exact computations (Cartesian Taylor jets and polar differentiation in ball arithmetic), an independent
  rational comparison and a third evaluation by numerical differentiation at 40 and 60 digits; for the annular test a
  computation in ball arithmetic, an independent rational audit with freshly recovered coefficients and a third
  computation in interval arithmetic from the audited pairings. The statements are local: they exclude nothing
  outside the balls.
- Square tests uniform in the smoothness index (THEOREM; the accompanying artifacts, P41). Let S be a closed square with center X_0
  and halfside delta on which F has one strict sign, |F| >= f, |V_bar| <= V, |D rho_bar| <= D and
  max(1, r)^(1/5) <= g_S. Pair the difference equation with zeta(X) = phi((x - x_0)/delta) phi((y - y_0)/delta),
  phi(t) = (1 - t^2)^2 on [-1, 1]: zeta has mass M = (16/15)^2 delta^2 and int |D zeta| <= (15/(4 delta)) M. Using
  only amplitude bounds |h| <= H n and |U[h]| <= B n (no gradient bound, so no dependence on s), every exact solution
  satisfies f <= A n + Q n^2 with A = H (V d + |2c + 1|) + B D, Q = H B d, d = 15/(4 delta), for every 0 < s <= 2^-12
  and R >= 1. The bounds over S are interval Taylor expansions at X_0 with the exact center jets (derivatives of the
  potential up to order 7) and enclosures of the highest derivatives over the whole square. With the first amplitude
  constants H = 16 g_S, B = 104 g_S this excluded N^w_s(h) <= 2^-22 around Mpen2 (square at (0, 4/5)) and 2^-23
  around d2 (at (0, 2/5)), halfside 2^-10. Checks: 640-bit interval computation; an independent rational audit of
  the 45 strict comparisons and of the 80 center residual derivatives against a Cartesian Taylor product; a third
  computation in bivariate interval Taylor arithmetic.
- The refit d2 (THEOREM for the facts stated; the accompanying artifacts, P42). A further six-branch refit of the numerical work
  (2382 generators, 1322 canonical terms, branches j <= 5) is reconstructed exactly: its six leading potential branches
  are the stationary orders of the checkpoint, the first descendants of branches 0, 1 and 2 vanish, nine residual
  sectors vanish exactly and the first surviving power is gamma - 6 delta < -2, so its residual lies in N_s and
  N^w_s. Its slope at the center is a_0 = 10.29231991..., it shares the exponent and the leading potential moments of
  the checkpoint, and all eight selected points pass every pointwise hypothesis of the weighted contract (point
  values only). The global bound <r>^2 |D^4 rho| <= 512 fails at certified off-axis points, for example
  (1 + |X|^2) |D^4 rho(X)| > 592 at X = (7/16, 7/64) (THEOREM, below). This is one of the three bounds left free
  by the parametric logarithmic theorem of section 5, for which d2 has the exact global caps <r> |D^3 u| <= 2^191,
  <r>^2 |D^3 rho| <= 2^191 and <r>^2 |D^4 rho| <= 2^201 (THEOREM; the accompanying artifacts, P91). On the whole plane d2
  satisfies the three matrix bounds M >= (19/5) I and M_1, M_2 >= I/2 of the weighted contract, with the weights
  omega_1 = (1 + r^2)^(-1/10) and omega_2 = (1 + 4 r^2)^(2/5) (THEOREM; the accompanying artifacts, P95: in t = r^2/(1 + r^2),
  z = cos 2 theta and w = (1 - t)^(delta/2) every entry of M - (19/5) I and M_1 - I/2, and of (1 + 3t)(M_2 - I/2) with
  1 + 3t > 0, is an exact polynomial in t, z, w (times (1 - z^2)^(1/2) for the off-diagonal fourth derivatives); complete binary covers of [0, 1] x [-1, 1] with 41, 79 and 119 leaves by directed
  512-bit Bernstein enclosures, each leaf rechecked by direct restriction at 640 bits). On the whole plane d2 also
  satisfies |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, |D^2 rho| <= 3, <r>|D^2 rho| <= 8 and, with decay exponent d = 4/9,
  r^(4/9) |D rho| <= 93, r^(13/9) |D^2 rho| <= 93, r^(-5/9) |u| <= 22, r^(4/9) |Du| <= 22 and r^(13/9) |D^2 u| <= 56
  (THEOREM; the accompanying artifacts, P95: the same exact polynomial representation, complete covers with 36 leaves for the
  first-derivative group, 121 for D^2 u, 314 for D^2 rho and 23 for u, directed 512-bit Bernstein enclosures, each
  leaf rechecked independently at 640 bits; full ordered Euclidean tensor norms). Together with the caps of P91 this
  completes every hypothesis of the parametric logarithmic theorem on the reference (THEOREM; the accompanying artifacts, P105).
  A floating-point sample of these ten quantities on 129 radii from 10^-4 to 10^12 and 91 angles, from fields
  checked against finite differences of the exact potential, gives maxima 0.05 to 0.87 times the caps, the
  closest being |D^2 rho| (about 2.600 against 3; FLOAT, a consistency check, not a certificate).
- Smaller amplitudes (THEOREM; the accompanying artifacts, P44). For every h in the space of Theorem D_w (R >= 1,
  0 < s <= 2^-12), with g = max(1, |X|)^(1/5) and n = N^w_s(h), |h(X)| <= (1/12) g n and |U[h](X)| <= (3/16) g n
  (instead of 16 g n and 104 g n). The planar Fourier inequality ||f||_inf <= (1/2) (||f||_2 ||D^2 f||_2)^(1/2) is
  applied, after a dyadic partition of unity, to the two norms ||<r>^(-6/5) h||_2 <= (2051/4194304) n and
  ||omega_2 D^2 h||_2 <= (1025/1024) n; the first is small because the norm gives its two lower components the large
  coefficients 2^22 and 2^53, and the Bessel kernel moments control the passage from J^s h to h. The velocity is
  treated in the same way through the weighted Riesz bounds 8/3, 3/2 and 9/5. The constants follow from exact
  rational comparisons (C_h^2 < 1/144, C_U^2 < 9/256; with the raw constants also 2/25 and 11/60). Hence
  N^w_s(F) >= 12 |F(X)|/g(X) at every point for every F in the space. Checks: the rational constants are recomputed
  exactly by a separate program.
- Improved distances and residual point bounds (THEOREM; the accompanying artifacts, P45). With these amplitude constants the same
  certified data give: the annular test of the checkpoint excludes N^w_s(h) <= 2^-14 (T = 2^31 and 2^32; 2^-15 at
  T = 2^35), and the square tests exclude 2^-15 around Mpen2 and 2^-16 around d2, all for every 0 < s <= 2^-12 and
  R >= 1; and the 93 certified residual point enclosures give, under the same uniformity and conditional only on F
  belonging to the space (proved for all ten references), N^w_s(F) > 0.01713995 (checkpoint), 277.09 (A2), 143.71
  (A3), 17.968 (A4), 3.910 (A5), 3.420 (Mpen), 1.406 (A6dpen), 0.9356 (Mpen2), 59.586 (b6) and 0.14095 (d2), that is
  more than 2^24 times the threshold 2^-30 of the second version for the checkpoint point value and more than 2^27
  times it for every refit. Checks: a directed interval implementation and a separate rational implementation (with
  pi < 22/7); a third computation in interval arithmetic reproduces every point bound and the square and annular
  radii.
- Centered tests (THEOREM; the accompanying artifacts, P46). The sign condition on F over the square can be dropped. Under the
  probability measure zeta dX/M the displacement Z = X - X_0 has mean zero, E Z_x Z_y = 0 and
  E Z_x^2 = E Z_y^2 = delta^2/7, so Taylor's formula gives |int F zeta/M - T| <= (sqrt 2/21) delta^3 sup_S |D^3 F| for
  T = F(X_0) + (delta^2/14) Delta F(X_0), and f = |T| - (sqrt 2/21) delta^3 sup_S |D^3 F| replaces the pointwise
  lower bound. Each term of the weak identity may also be bounded by weighted Cauchy-Schwarz, with
  ||<r>^(-6/5) h||_2 <= a_0 n, ||<r>^(-6/5) U[h]||_2 <= (8/3) a_0 n (a_0 = 2051/4194304) and the exact test norms
  ||D zeta||_2/M = 5 sqrt 6/(7 delta^2), ||zeta||_2/M = 5/(7 delta), ||D zeta||_inf/M <= 25 sqrt 6/(32 delta^3);
  the amplitude constants 2/25 and 11/60 may be used. All 48 recorded squares then give positive centered pairings;
  the best exclude N^w_s(h) <= 2^-14 around Mpen2 (square at (0, 4/5)) and 2^-15 around d2 (at (0, 2/5)), halfside
  2^-10, for every s and R in the ranges above. Checks: an interval computation and an independent rational
  computation; the rational constants are recomputed by a separate program.
- Weighted Bessel bound and negative-order tests (THEOREM; the accompanying artifacts, P47). For R >= 1 and 0 < s <= 2^-12,
  L(J^-s h) <= (1 + s C_R) L(h) <= (11/10) L(h), C_R = 41/(5R) + 17/R^2 + 327/(5R^3) + 1309/(10R^4) + 924/(5R^5)
  (at most 4063/10). Proof: with B = J^-s, T = w B w^-1, q = D(-Delta)^-1(w h) and a = D log w, the exact identity
  w B h = B(w h) - div((T - B) q) + [a, T] q holds; the first term has norm at most L(h), the second is bounded by
  Young's inequality with the moderate weight ratio (1 + t/R)^3, and the third is centrally odd, so the parity Hardy
  inequality ||f||_(Hdot^-1) <= ||r f||_2 and the kernel moments (int |z|^5 b_s <= 84 s) bound it. Hence
  L(h) <= (11/10) 2^(-53/2) n and L(U[h]) <= (13/3)(11/10) 2^(-53/2) n. Negative Sobolev duality,
  |int h f| <= L(h) ||D(w^-1 f)||_2, then bounds the two linear terms of the weak identity with the test norm
  ||D^2 zeta||_2/M = 45/(7 delta^3), and derivative bounds certified on a larger concentric square remain valid on
  every smaller one. With highest-derivative enclosures from squares of halfside 1/256, no exact solution has
  N^w_s(h) <= 2^-11 around Mpen2 (square at (0, 2/5), halfside 5/2048: f > 0.00194302, A < 2.741991, Q = 22.528) or
  N^w_s(h) <= 2^-12 around d2 (same center, halfside 1/512: f > 0.00193453, A < 5.261981, Q = 28.16), for every
  0 < s <= 2^-12 and R >= 1. Checks: a 512-bit interval implementation and a separate rational implementation verify
  all 294 positive pairings; the rational constants and the kernel moments are recomputed by a separate program.
- Weighted amplitudes from the negative component (THEOREM; the accompanying artifacts, P48). For every h in the space (R >= 1,
  0 < s <= 2^-12, n = N^w_s(h)), w(X) |h(X)| <= n/1000 and w(X) |U[h](X)| <= n/400, w = (1 + r^2/R^2)^(-11/10). The
  planar Fourier inequality ||f||_inf <= 2^(-5/6) 3^(-1/4) ||f||_(Hdot^-1)^(1/3) ||D^2 f||_2^(2/3) is applied to
  f = w h and f = w U[h]; the negative norm carries the coefficient 2^53 of the norm (with the Bessel bound of P47),
  and ||D^2 (w h)||_2 <= (8436585/8388608) n, ||D^2 (w U[h])||_2 <= (7604905/4194304) n follow from the weight
  derivatives. The constants are fixed by exact rational comparisons of twelfth powers. Hence
  N^w_s(F) >= 1000 w(X) |F(X)| at every point. The 93 certified residual point enclosures give, uniformly in s,
  N^w_s(F) > 5195.0 (A2), 2850.1 (A3), 309.38 (A4), 40.58 (A5), 39.61 (Mpen), 19.21 (A6dpen), 12.66 (Mpen2),
  1380.0 (b6), 5.479 (d2) and 0.0475 (checkpoint) for every R >= 1, and 26524, 14449, 2308.4, 516.4, 451.7, 185.7,
  123.5, 5849.1, 16.71 and 3.587 for every R >= 2^31. With these amplitudes the centered square tests exclude
  N^w_s(h) <= 2^-9 around Mpen2 (square at (0, 2/5), halfside 1/512) and d2 (same center, halfside 3/2048), for every
  s and R >= 1. Checks: an interval implementation and a separate rational implementation; a third computation
  reproduces the constants, all 93 point bounds and the square radii.
- Weighted L^2 bounds and the negative-order annular distance (THEOREM; the accompanying artifacts, P49). Since
  ||g||_2 <= ||g||_(Hdot^-1)^(2/3) ||D^2 g||_2^(1/3), the same inputs give ||w h||_2 <= n/190000 and
  ||w U[h]||_2 <= n/60000. In the annular weak identity for the checkpoint (test zeta_T = w_T chi(r/T) sum a_m sin(m
  theta) as above) the two linear terms are then bounded by negative-order duality and the quadratic term by these L^2
  bounds, which removes the amplitude factor from the quadratic coefficient. For R >= 2^31 and 0 < s <= 2^-12 the
  certified pairings at T = 2^31, 2^32 and 2^35 exclude N^w_s(h) <= 2^57, 2^57 and 2^55: no exact solution, of any
  exponent, lies within N^w_s-distance 2^57 of the checkpoint. Checks: an interval implementation, an independent
  rational audit and a third computation.
- Exterior transfer of annular witnesses (THEOREM; the accompanying artifacts, P51). For R >= T, q >= 1 and a test phi supported in
  r >= T, the ratio a = w_T/w_R satisfies 0 < a <= 1 and Delta a >= 0 there (exact formula
  Delta a/a = 4 q D_0 [z^2 + q D_0 z - T^2 R^2]/[(T^2 + z)^2 (R^2 + z)^2], z = r^2, D_0 = R^2 - T^2), so
  ||D(a phi)||_2 <= ||D phi||_2 and ||w_R F||_(Hdot^-1) >= |<w_T F, phi>|/||D phi||_2. One annular witness at radius T
  therefore serves every R >= T. With the Bessel factor 1 + 2^-12 C_T (P47), the checkpoint pairings give
  N^w_s(F) > 3.535e25, 1.521e26 and 1.211e28 for every R >= 2^31, 2^32 and 2^35 and every 0 < s <= 2^-12, gaps of
  more than 2^119, 2^121 and 2^128 over 2^-35 (2^114, 2^116 and 2^123 over 2^-30). Checks: symbolic verification of
  the weight identity, exact test energy, interval bounds; an independent audit and a third computation.
- Annular distances for Mpen2 and d2 (THEOREM; the accompanying artifacts, P52). For both refits the far-field residual is
  reconstructed exactly as a finite sum of sectors r^(gamma - j delta - 2q) sum c_n e^(i n theta) (q <= 3, exact
  rational Laurent polynomials), every sector above r^(gamma - 6 delta) vanishes and the leading one is a nonzero sine
  series; the rest is bounded by an explicit tail constant. The annular weak identity with the test built from the
  leading sector and the weighted L^2 bounds of P49 give, for every R >= 2^31 and 0 < s <= 2^-12,
  N^w_s(F) > 1759901917 (Mpen2) and 1760486552 (d2) from the annulus 2^20 <= r <= 2^21 (more than 2^65 times 2^-35)
  and exclude every exact solution with N^w_s(h) <= 2^21 around either. The tested annuli with inner
  radius at most 2^16 give no positive pairing. Checks: an interval implementation, an independent exact audit and a third computation from the source
  coefficients (exact sector reconstruction, interval evaluation of every annulus, Cartesian check of the expansion).
- Off-axis derivative failures of d2 and Mpen2 (THEOREM; the accompanying artifacts, P54 and P58). Certified point values refute
  global bounds of the reference contract that hold at the eight points audited first: for d2,
  <r>^2 |D^4 rho| > 592 at (7/16, 7/64) (also > 578 at (27/64, 7/64) and > 513 at (7/16, 3/32)) against 512; for
  Mpen2, <r> |D^3 u| > 16.12 against 16 and <r>^2 |D^3 rho| > 39.23 against 32 at (19/64, 7/16), and
  <r>^2 |D^4 rho| > 1333.12 at (1/4, 15/32) (also > 1250.40 at (17/64, 29/64)) against 512. Hence each of the nine
  exactly admissible refits violates the contract. For Mpen2 and d2 every currently certified violation concerns one
  of the three bounds left free by the parametric logarithmic theorem (section 5, P89), and both have exact global
  caps 2^191 and 2^201 for them (P91), so these failures do not exclude them from that theorem. For d2 every other
  global hypothesis is verified (P95, P105); for Mpen2 unchecked inequalities are not presumed to hold. Both
  residuals miss its threshold for every parameter choice (P90). Checks: Cartesian Taylor jets and an independent polar recurrence
  (768-bit), a rational endpoint audit, and a third computation from the source coefficients.
- Positive residual floors for fixed finite families (THEOREM; the accompanying artifacts, P56, P57 and P59). For every nonzero real
  v in L^2, div(v U[v]) is a nonzero distribution (testing against y times a radial cutoff gives ||R_1 v||_2^2 = 0).
  Hence on a fixed finite-dimensional density space the quadratic part of the residual is proper, and for the
  six-branch family with any fixed radial degree K (six leading branches and the two descendants prescribed, all
  remaining coefficients free) the weighted residual norm has a positive lower bound delta_K, uniform in
  0 < s <= 2^-12 and R >= 1. The proof gives a formula for delta_K from Gram, tail and remainder constants; for the
  angular band of these fits (density modes sin((2j + 1) theta), j < 60) the velocity constant is exact,
  ||U[v]||_2^2 >= sin^2(pi/242) ||v||_2^2 (sharp, from the spectrum of a tridiagonal angular matrix), and a density
  tail fraction at most 1/57000^2 beyond radius L gives N^w_s(div(v U[v])) >= 7 ||v||_2^2/[396 L^3 (1 + 4 L^2)^(11/10)].
  The remaining constants are not evaluated, so no value of delta_K is known and the thresholds 2^-30 and 2^-35 are not
  decided. Without finite dimension the statement fails: dilated annular densities of unit L^2 norm have
  N^w_s(div(v U[v])) tending to zero. Checks: independent review of every step and exact or interval checks of the
  scalar constants.
- Seven-branch floor (THEOREM; the accompanying artifacts, P60). For the seven-branch family (seven stationary leading branches, first
  descendants of branches 0 and 1 zero, the descendant of branch 2 free, any fixed radial degree K >= 69), the residual
  is r^q a(theta) + r^p E_7(theta) + O(r^(p - beta)) with q = gamma - 2 delta - 2 = -2.343 (free), p = gamma - 7 delta
  = -2.581 (fixed, angular norm 9679.97) and beta = 2 - 4 delta; no other sector lies in between (exact exponent
  comparisons and nonresonance). The radial test b(t) = b_0(t)(c_* - t), c_* = I(q + 2)/I(q + 1),
  I(z) = int_1^2 t^z b_0(t) dt, annihilates the q-sector, and J_* = int_1^2 t^(p+1) b(t) dt = 1.0642e-4 >
  d 2^(p+q+1)/840 > 1/67200 (d = q - p; the symmetrized moment determinant is 1/25200). With the coefficient bound
  from the angular coercivity of P59 (mu_70 = sin^2(pi/282) > 1/8100) and negative-order duality, N^w_s(F) has a
  positive lower bound on the family, uniform in 0 < s <= 2^-12 and R >= 1, by a finite-constant formula that is not
  evaluated. Checks: exact exponent comparisons and moments, 512-bit and separate 300-bit interval values of J_*.
- Exact constraints at the endpoint (THEOREM; the accompanying artifacts, P61). In Z_gamma = L^2(<r>^(-2-2gamma) dX), for any finite
  list of real linear functionals on the compact zero-strain core (not necessarily continuous) and any compact
  operator K, disjoint logarithmic annular packets r^gamma sin(5 theta) chi((log r - L)/L) combined through a null vector
  of the constraint matrix give unit vectors with every constraint exactly zero, c[h] = 0, weakly null, and
  ||(B + K) h|| -> 0. Hence no closed realization containing this core is Fredholm. This concerns only the critical
  space; the conditional theorems in N_s and N^w_s are unaffected.
- Evaluated weighted floor (THEOREM; the accompanying artifacts, P62). For J = 6 or 7 stationary branches, any radial degree
  K >= 10J - 1, the first descendants of branches 0 and 1 zero, and the descendant of branch 2 free (epsilon = 0) or
  zero (epsilon = 1), every residual satisfies, for all R >= 1 and 0 < s <= 2^-12,
  N^w_s(F) >= [2048/(1 + 6s)] E_J D/sqrt(2) > 2045 E_J D/sqrt(2). Here E_J is the angular L^2 norm of the fixed sector
  (3081.27 for J = 6, 9679.97 for J = 7) and D = (2a* + 16/5)^(-1/2) prod |a - a*|/(a + a* + 16/5) over the finite set
  of exponents a = l delta/2 + k - 2 (1 <= l <= 2J, 0 <= k <= 2K + 4, without the prescribed ones), a* = (J + 1) delta/2 - 2.
  Proof: P0(h) = ||<r>^(-6/5) h||_2 <= (1 + 6s) N^w_s(h)/2048 by duality and the Bessel kernel moments; with
  u = (1 + r^2)^-1 the exact power representation gives P0(F)^2 >= (pi/2) sum_m ||u^(11/10) v_m||^2, v_m a combination of the
  powers u^a whose u^(a*) coefficient is the fixed e_m; the Muntz (Cauchy determinant) distance gives D. Values
  (rounded to nearest, so a displayed value is not itself a lower bound; for example the seven-branch value at K = 69
  lies strictly between 3.46e-75 and 3.47e-75):
  six branches 3.79e-52, 6.00e-55, 2.37e-57 at K = 59, 75, 92 (descendant free) and 8.83e-51, 1.40e-53, 5.51e-56
  (descendant zero); seven branches 3.47e-75, 1.53e-76, 7.02e-80 at K = 69, 75, 92 and 7.76e-74, 3.42e-75, 1.57e-78.
  All are far below 2^-30; the bound is a lower bound over a linear enlargement of the residual set, so a small value
  says nothing about the true minimum. Checks: a 512-bit gamma-product evaluation, a 768-bit factor-by-factor
  evaluation, and a third program that recomputes the six-branch sector from the source potentials of three refits
  and forms D^2 as an exact rational.
- Scope of the annular test. For any residual F in Hdot^-1 and any test phi supported in 1 < |X| < 2, the dilated
  pairings satisfy sum_j |<F, phi(./(3^j R_0))>|^2 <= ||D phi||_2^2 ||F||_(Hdot^-1)^2 (disjoint supports, and the
  homogeneous H^1 norm is dilation invariant in two dimensions). So the necessary condition below can never exclude a
  reference whose residual lies in N_s, such as the tail repairs and the exactly admissible refits (THEOREM).
- Limits of this argument in the weighted norm (THEOREM). There is a smooth function f of the parity class, with the
  same coefficient e of r^(p*), the same eight vanishing sectors and the same finite power structure, for which
  N^w_s(f) < 3.461e-13 < 2^-35 at R = 2^31, uniformly in 0 < s <= 1/2: each mode is e_m times an exact minimal-norm
  combination of the allowed powers in L^2(u^(11/5) du) (a weighted Muntz projection), multiplied by a factor that
  vanishes to high order at the center. f is not shown to be the residual of any potential. Hence a uniform weighted
  obstruction for the family would have to use the nonlinear structure of the residual.
- The seventh stationary order and the next fixed sector (THEOREM; a finite formal statement). Let C_1 be the exact
  leading cosine potential of state 131 (degree 18 in theta), rho_1 = -d_y Laplace(r^(p_1 + 3) C_1) and
  p_n = 1 - n delta. There are unique odd sine density polynomials Theta_n and even sine stream polynomials Psi_n,
  n <= 8, of degrees at most 20n - 1 and 20n, solving the angular Poisson equations
  [-d_theta^2 - (p + 1)^2] Psi = p cos(theta) Theta - sin(theta) Theta' and cancelling the formal stationary
  coefficients through order 8 (the recurrence Theta_n = S_n/((n - 1)(c - 1)), with
  S_n = sum_(i+j=n) [(p_i + 1) Psi_i Theta_j' - p_j Psi_i' Theta_j], is nonresonant at every order). For every potential
  with branches j = 0, ..., 6 whose first seven leading homogeneous potentials are these stationary orders, the residual
  sector of radial power p_8 = 1 - 8 delta = -2.5809 is E_7 = S_8 = 7(c - 1) Theta_8; no coefficient of the radial
  descendants of those branches changes it, and within this generator architecture only an eighth branch cancels it.
  Its full-circle angular norm is
  9679.9655801992743519 (first quadrant 4839.98279...), against 3081.27 for the six-branch sector at p_7 and 4331.16
  for the six-branch residual at p_8 (which omits the interactions of orders 1 and 7). Ordering: the descendant sector
  (2, 1), of power gamma - 2 delta - 2 = -2.3428 > p_8, decays more slowly and comes first unless its coefficients
  vanish exactly; a penalty only makes it small, and whether a small nonzero coefficient is compatible with the
  weighted threshold is not decided. Checks: two independent exact reconstructions from the original state (a real sine
  recurrence and a complex Fourier convolution), a third computation by 60-digit Cartesian differentiation of the
  homogeneous functions at four points (relative error below 3e-59), and the numerical work's exact seventh-order
  coefficients agree. It says nothing about convergence of the stationary series or about a small residual. The uniform
  bounds above concern six branches; for seven branches the corresponding bound decides nothing (below).
- Necessary condition in the affine class (THEOREM). Let rho_bar be a smooth reference of the parity class with bounded
  gradient and velocity u with |u| <= C r^gamma, |Du| <= C r^(gamma - 1) for r >= R_0 >= 1. If rho_bar + h is stationary
  at the same c_l, with h in Hdot^-1 and C^1 with bounded gradient (every h in N_s qualifies), then for every smooth phi
  supported in 1 < |X| < 2 the annular moments m_j = int F_bar(X) phi(X/(3^j R_0)) dX are square-summable, with
  (sum m_j^2)^(1/2) <= [K + ||D phi||_2 (||D rho_bar||_inf + ||Dh||_inf)] ||h||_Hdot^-1 and an explicit constant K
  (the accompanying artifacts, Theorem E). A leading residual sector r^q E(theta), E not identically zero, gives m_j of order
  3^(j(q + 2)), so it excludes every such h when q >= -2. Proof: test the correction equation on disjoint dyadic-type
  annuli; the transport adjoint applied to a dilated test has an R-independent homogeneous H^1 norm in two dimensions,
  and the nonlinear term is in Hdot^-1 through the identity U[h].grad v = -div(psi D^perp v), psi = d_x (-Delta)^-1 h.
    * Consequence: there is no h in N_s, of any norm, with F(rho_bar + h; c_l) = 0 when rho_bar is the checkpoint
    (state 131 or state 88; q = 2 gamma - 1 = 0.1048 and 0.1059 respectively, gamma differing) or one of the audited refits m4, m5, m10, m12 (q = 3 gamma - 2 = -0.343) or m14 (q = p_5 = -1.238).
  * Exponent rigidity: since F_c(rho_bar) = F_(c_l)(rho_bar) + (c - c_l) X.grad rho_bar and, under the differentiated
    expansion X.grad rho_bar = gamma r^gamma Theta_0 + o(r^gamma) (a hypothesis in addition to (B11); it holds for
    every finite potential considered here), a change of c creates the sector (c - c_l) gamma r^gamma Theta_0
    with exponent gamma > -2; the theorem holds for every c, so no exact solution with any other exponent exists in
    these classes either, and for an admissible reference an exact solution in reference + N_s must keep c = c_l.
  * For a reference of the canonical finite generator form, an exact solution in the affine class can exist only if all
    residual sectors with exponent >= -2 vanish: the sector defects at p_2, ..., p_6 and the descendants at gamma - 2
        and 2 gamma - 3. There are no other sectors with exponent >= -2. Their vanishing is necessary and sufficient for
    the residual to lie in N_s, 0 < s <= 1/2.
  * A companion theorem along characteristics gives the forced correction: for gamma - 1 < q, c_l q < 1 and bounded h
    with bounded Lipschitz U[h], h = r^q E/(1 - c_l q) + o(r^q); for the refits this is a nonzero r^(-0.343) tail, not
    in L^2.
  * Scope: fixed c_l, one affine class. Weighted correction spaces, spaces with explicit tail coordinates and the tail
    repairs (whose residuals start at r^(p_7), p_7 < -2) are not affected. It is not a nonexistence theorem for the
    profile.

## 7. Open items

1. A reference in the class with a small residual. Membership is solved by the two tail repairs (THEOREM). The cutoff
   splice to the exact stationary far-field potentials outside radius R leaves the residual unchanged on r < R, so the
   reference must already be accurate on r < R and close to the stationary expansion at r about R, and the transition
   annulus must be bounded. The algebraic repair stays within finite rational potentials, so the exact norm method
   applies, but the explicit variants have large residuals (N_s(F) > 11.48 for all ten) and nine of the ten fail (B1).
   A refit inside the affine set of finite potentials whose eight sector conditions hold (these conditions are linear
   in the potential coefficients once the leading sector is fixed) has been carried out for two iterates of a
   least-squares fit in the extended family; both are exactly admissible but fail (B1) near (0, 1) and have residuals
   of order 10 at r ~ 1 to 5 (THEOREM, section 2, answer 7). Later iterates (with penalties for the matrix
   condition and for the next descendant sector) keep the leading residual sector r^(-2.133) unchanged: in this
   generator family the sector is fixed by the six leading branches, and for every choice of coefficients it keeps the
   unweighted norm above 22986 times the unweighted threshold (THEOREM); raising the radial degree up to 3675 does not
   remove it (THEOREM). In the weighted space it gives a gap of more
   than 2^59 for the two refits where it was tested, but no uniform weighted bound follows from it alone (THEOREM, by
   an explicit function). A usable reference should therefore cancel this sector, which needs a seventh stationary
   branch (generators of the next far-field order matched to the seventh stationary profile). With seven branches the
   next fixed sector is r^(p_8), p_8 = -2.581, of full-circle angular norm 9679.97, more than three times the old one
   (THEOREM, section 6); with the seven leading branches fixed and in this generator architecture it is cancelled only
   by an eighth branch. The descendant sector (2, 1), of exponent gamma - 2 delta - 2 = -2.343 < -2, lies in the
   unweighted residual space, and no theorem forces its exact cancellation for the weighted threshold; cancelling it
   exactly is a possible next constraint (a numerical strategy), since a penalty only makes it small and in the
   first seven-branch fit it is large. The first
   seven-branch fit of the numerical work (b6) is exactly admissible, with the old sector exactly zero and the sector
   (7, 0) equal to the theorem's value, but its leading sector is (2, 1); certified point values give
   N^w_s(F) > 1380 and violate three bounds of the contract (THEOREM, section 6), and no exact solution lies within
   N^w_s-distance 2^-16 of it. For seven branches the uniform method gives no bound exceeding the residual threshold
   (THEOREM, section 6), so no obstruction is known for that family. A further six-branch refit, d2, with one more descendant sector cancelled,
   passes every pointwise hypothesis at the audited points but fails one off-axis (a bound that the parametric
   logarithmic version of section 5 leaves free; every reference hypothesis of that version holds for d2 on the whole
   plane, THEOREM, section 5), has N^w_s(F) > 5.479 (and
   N^w_s(F) > 1.759e9 for R >= 2^31), and no exact solution lies within N^w_s-distance 2^-9 of it (2^21 for
   R >= 2^31) (THEOREM, section 6). The reference must reach ||w F||_(Hdot^-1) < 2^-61 and |F| < 2^-44 near the
   origin for the first version of Theorem D_w (2^-56 and 2^-39 for the second; answer 7), and M(F) < 2^-37 for the
   logarithmic version (which needs ||w F||_(Hdot^-1) < 2^-63.5; below 2^-35 for every parameter choice of its
   parametric form), far beyond the accuracy of every fit computed so far. For each fixed radial degree of the six-branch family a positive lower bound of the
   weighted residual norm is proved but not evaluated (THEOREM, section 6); a weaker bound of the same kind is evaluated
   exactly and is below 1e-50 for both families (THEOREM, section 6), so it decides nothing. Evaluating the sharper
   bound, or finding a family member below the threshold, is the open quantitative question.
2. Size: N_s(R_tilde) <= 6.357e-7, certified by interval upper bounds of E_2(R_tilde) and ||omega D^3 R_tilde|| over
   the whole plane. The best early refit (m10) is about eight orders of magnitude away in its finite components (certified
   128 ||grad F||_2 > 44.09 against 6.357e-7, a factor of about 6.9e7; a diagnostic for that reference
   only), and its low-order components are infinite; the later refits have finite norms and miss the weighted
   thresholds by the factors in item 1.
3. Certificates (B0) to (B9c) for that reference, or a proved perturbation bound from the checkpoint. For an algebraic
   repair or a new refit they must be redone; the Bernstein method of the certificates applies to any finite rational
   potential of the canonical form.
4. A larger unknown. The checkpoint and the five audited unrepaired refits admit no N_s correction (section 6). The
   tail repairs escape that obstruction, but no checked repair satisfies the hypotheses of Theorem D. The
   alternatives are a better tail-repaired reference (items 1 to 3) or a correction class with explicit tail coordinates for
   the sectors Theta_1, ..., Theta_5; the second needs a new inverse theorem and is not developed here. Such coordinates
   must be added to a strictly subcritical correction space: in the critical weighted Sobolev space no closed
   realization with finitely many added parameters and equations is even upper semi-Fredholm (THEOREM, section 4).
5. Regularity is not the bottleneck. The logarithmic theorem of section 5 works in the sharp open range beta > 1/2 of
   its logarithmic scale, in which the strain is continuous (at beta <= 1/2 it is not, P74; no least admissible beta
   is attained) and still needs a residual below 2^-37, while the
   certified residual floors in its norm are more than 2^121 (checkpoint) and 2^67 (Mpen2, d2) times larger. Freeing
   the higher derivative bounds (the parametric form) does not change this: the gaps only grow with the hierarchy
   coefficient. A smaller residual, not a weaker correction space or weaker derivative bounds, is what an existence
   proof near these references requires.

The accompanying artifacts contain the proofs, certificates, closure statement, hypothesis list and reproduction
instructions, together with a published subset of the original full reproduction packet. The full packet contained
697 certificate files with a SHA-256 manifest (about 491 MB: the certificate programs and data of parts P1 to P32,
the inputs of the independent recomputations of the later parts, and the certificate records of the later global
bounds with every program and record their rechecks and audits read) and the scripts. Some inputs are omitted from
the published subset; the accompanying artifacts identify them, give their hashes and explain the resulting limits
on reproduction. The following successful reruns used the full packet, not the published subset alone.

For that full packet, one command restored the layout the programs expected; a second reran all 113 check programs
and compared every output with the recorded file (20 to 40 minutes on one core of a loaded machine); a third, on a
second fresh restore, reran the 32 independent recomputations of the later parts and compared them with their
records (about 20 minutes); a fourth, on a third fresh restore, reran the 26 independent rechecks and exact audits
of the later global bounds of the original state and of the refit d2 (about 28 minutes). The certificate searches
were rerun with the check driver. On fresh restores every check, every recomputation and every late recheck and
audit reproduced the recorded values, and every search reproduced its certificate, except that the search for
the matrix certificate of one refit stops at a fixed time limit of 480 s and, on the loaded machine, produced only
the first 1005 of its 1346 leaves, identical to the recorded ones; that certificate was checked independently by
one of the checks (see the reproduction instructions in the accompanying artifacts, sections 3, 4 and 9).

## Appendix A. Hypotheses (B0) to (B11) of the unweighted theorems

Spaces: omega(X) = (1 + 4 r^2)^(2/5); E_0(h)^2 = ||h||_2^2 + (20/21) ||h||_(Hdot^-1)^2,
E_1(h)^2 = ||grad h||_2^2 + 16 E_0(h)^2, E_2(h)^2 = ||omega D^2 h||_2^2 + 2^14 E_1(h)^2, N_s(h) = E_2((1 - Delta)^(s/2) h),
all completions of the smooth compactly supported functions of the parity class. Ubar = U[rho_tilde],
V = c_l X + Ubar, R_tilde = F(rho_tilde; c_l), gamma = 1/c_l.

Notation: A = [[rho_tilde_y, -rho_tilde_x/2], [-rho_tilde_x/2, 0]],
N = (1/2) [[rho_tilde_yyy, -rho_tilde_xyy], [-rho_tilde_xyy, rho_tilde_xxy]], v = omega^2,
S = (v_xy rho_tilde_x - v_xx rho_tilde_y - v_x rho_tilde_xy + v_y rho_tilde_xx)/2, <r> = (1 + r^2)^(1/2).
Matrix inequalities hold pointwise on R^2 in the sense of symmetric matrices. Tensor bounds are Frobenius suprema except
in (B9), where ||T||_S is the sum over ordered indices I of ||T_I||_inf. (A Frobenius bound gives the component sum only
with the factor equal to the number of components, not its square root, because the component maxima may occur at
different points.)

- (B0) Structure. 9/5 < c_l < 37/20. rho_tilde is smooth, in the parity class, of sublinear growth, with canonical
  velocity Ubar; a_0 = d_y rho_tilde(0) > 0; the functions D rho_tilde, <r> D^2 rho_tilde, <r>^2 D^3 rho_tilde,
  <r>^2 D^4 rho_tilde, D Ubar, <r> D^2 Ubar and <r> D^3 Ubar are bounded.
- (B0n) Normalization. c_l + c[rho_tilde] = 1.
- (B1) M = (2 c_l + 1) I + sym D Ubar + A >= (19/5) I.
- (B2) A >= -(1/20) I.
- (B3) N <= I.
- (B4) M_1 = I - sym D Ubar + A >= (9/10) I.
- (B5) M_2 = (1 + c_l + V.grad log omega) I - 2 sym DV + A >= (1/2) I.
- (B6) M_3 = (1 + c_l + V.grad log omega) I - 3 sym DV + A >= -(5/4) I.
- (B7) ||D^2 rho_tilde||_inf <= 3, ||omega D^2 rho_tilde||_inf <= 8, ||omega D^3 rho_tilde||_inf <= 10,
  ||omega D^2 Ubar||_inf <= 3, ||D(v grad rho_tilde)/omega||_inf <= 28, ||S||_inf <= 40.
- (B8) ||D^2 Ubar||_inf <= 35, ||D^2 rho_tilde||_inf <= 77, ||<r> D^3 Ubar||_inf <= 2^14,
  ||<r> D^3 rho_tilde||_inf <= 2^14, ||<r>^2 D^4 rho_tilde||_inf <= 2^84.
- (B9) M* = |c_l| + ||D Ubar||_S + ||omega D^2 Ubar||_S + ||omega D^3 Ubar||_S + ||D rho_tilde||_S
        + sum_(j=2..4) ||omega D^j rho_tilde||_S <= 4096.
- (B9c) Component form of (B9): |c_l| <= 2, ||D Ubar||_S <= 6, ||omega D^2 Ubar||_S <= 24, ||omega D^3 Ubar||_S <= 160,
  ||D rho_tilde||_S <= 22, ||omega D^2 rho_tilde||_S <= 32, ||omega D^3 rho_tilde||_S <= 80,
  ||omega D^4 rho_tilde||_S <= 2048. (It implies (B9) with M* <= 2374.)
- (B10m) Membership: R_tilde = F(rho_tilde; c_l) lies in the N_s space (for instance R_tilde in the E_3 completion).
- (B10s) Smallness: N_s(R_tilde) <= eta, where (s, eta) = (2^-28, 2^-27/20 = 3.7252902984619140625e-10) for the first version
  of the unweighted conditional existence theorem and (s, eta) = (2^-18, 2^-16/24 = 1/1572864 = 6.3578287760416...e-7)
  for the second (section 5).
  (B10) denotes (B10m) and (B10s) together.
- (B11) Leading profile (used only for the statements about Theta_0 and scaling). rho_tilde - r^gamma Theta_0(theta)
  tends to 0 relative to r^gamma, uniformly in theta, for some nonzero Theta_0.

These are the hypotheses through which the unweighted Route U theory (section 4) and the unweighted rough-velocity
and conditional existence theorems (section 5) use the reference: (B0) to (B5) and (B7) give the E_0, E_1, E_2
theory; adding (B6) and (B8) gives the E_3 and interpolation theory; (B0n) is needed for the normalized range
statements; the rough-velocity theorem and the first existence theorem use (B9), the sharper rate and the second
existence theorem use (B9c), and existence uses (B10m) and (B10s).

## Appendix B. Hypotheses of Theorem D_w

Weights and norms. <r> = (1 + r^2)^(1/2), R = 2^35, w = (1 + r^2/R^2)^(-11/10), omega_1 = <r>^(-1/5),
omega_2 = (1 + 4 r^2)^(2/5), P_1(g) = ||omega_1 D g||_2, P_2(g) = ||omega_2 D^2 g||_2, L(g) = ||w g||_Hdot^-1,
E^w(g)^2 = P_2(g)^2 + 2^22 P_1(g)^2 + 2^53 L(g)^2, N^w_s(g) = E^w(J^s g), J = (1 - Delta)^(1/2). The space is the
completion of the compactly supported smooth functions of the parity class (even in x, odd in y).

Hypotheses on the reference rho (all pointwise and global; Euclidean norms of the ordered derivative tensors;
V = cX + u, u = U[rho] canonical, A = [[rho_y, -rho_x/2], [-rho_x/2, 0]]):
(W0) rho smooth, even in x, odd in y, sublinear, with canonical sublinear velocity; 9/5 < c < 37/20;
     a_0 = d_y rho(0) >= 1.
(Wn) c + c[rho] = 1 exactly (with the local term of the strain formula).
(W1) M = (2c + 1) I + sym Du + A >= (19/5) I, and with the decay exponent d = 2/5: sup r^d (|D rho| + r |D^2 rho|)
     <= 152, sup r^(d - 1) |u| <= 18, sup r^d |Du| <= 18, sup r^(1 + d) |D^2 u| <= 45 (d is not delta = 1 - gamma).
(W2) M_k = (1 + c + V.D log omega_k) I - k sym DV + A >= I/2 for k = 1, 2 (weighted principal matrices; for k = 1 this
     is not the unweighted first-derivative matrix).
(W3) |Du| <= 14/5, |D rho| <= 16, <r>|D^2 u| <= 3, <r>|D^3 u| <= 16, |D^2 rho| <= 3, <r>|D^2 rho| <= 8,
     <r>^2 |D^3 rho| <= 32, <r>^2 |D^4 rho| <= 512.
(Wm) F(rho; c) belongs to N^w_s.  (Ws) N^w_s(F(rho; c)) <= eta: 2^-46 at s = 2^-30, or 2^-35 at s = 3 * 2^-31 with the
     sharper constants (section 5).
(Wt) (for the tail and scaling conclusions only) r^(-gamma) rho -> Theta_0 != 0 uniformly, gamma = 1/c.

At R = 2^31 the theorem holds with the decay exponent d = 4/9 and the constants 186, 22, 22, 56 in (W1), and the
low matrix condition M >= (19/5) I may be weakened to M >= (5/2) I, or to M >= (2/5 + (11/5) c r^2/(R^2 + r^2)) I, on
r <= R (section 5). With the last form, (W0) to (W3) at R = 2^31 are the numerical hypotheses of the logarithmic
theorem, which adds polynomial growth of every derivative of rho and the leading-profile hypothesis stated with it in
section 5. For state 131 every condition except (Ws) is certified.
