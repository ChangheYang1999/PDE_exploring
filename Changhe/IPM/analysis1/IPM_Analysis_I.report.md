# Rigorous a posteriori error analysis of the full-plane IPM profile X3: final report

## Summary
- Status: UNRESOLVED. Neither decisive endpoint was reached: there is no rigorous a posteriori existence theorem
  (YES) and no properly scoped exclusion in a neighbourhood of X3 (NO), in `P_2`, in any `P_m` or in `P_infty`.
  Nothing here is a numerical-evidence YES.
- Run: T0 = 2026-10-20T12:44:23Z, T_end = 2026-10-22T13:02:18Z, elapsed 48 h 17 min (section 3). The
  reported research window reached the 48 h deadline, with interruptions; these session spans do not measure
  continuously active work or independently certify completion of the required research duration.
- Proved or certified results (exact scope in sections 1, 5, 6 and 7; individual verification limits in section 8):
  - X3, reconstructed from its coefficient file (md5 as stated), has certified central strain
    `c in [15.72608782162331, 15.72608782162370]`, normalization defect `3/k - 1 - c in [1.03009e-8, 1.03014e-8]`
    and a canonical residual that grows at infinity; an exact scalar-and-tail repair lies at factor distance
    `< 1.477e-5`.
  - An explicit modal trial rho~ fitted to X3 is exactly joined and exactly normalized, at a cost `< 4.080e-10`
    relative in a weighted factor norm. Its density is `C^{4,1}` but not `C^5` at the centre, and its factor is not
    `C^2` there, so it is not a `P_infty` trial (section 2). On the whole plane its residual satisfies, in the
    diagnostic weighted
    `H^1`-type norm X of section 10, `||eps~||_X < 1.49546805188731021373656` and
    `||eps~ - partial_t eps~||_X < 2464.68293019825564964515` (direct interval bounds, no unverified hypothesis).
  - A conditional two-norm (quasilinear) iteration theorem gives an exact solution near rho~ under all the space,
    mapping and uniform estimate hypotheses of section 7, once
    `K_H eta <= r`, `K_L C_B K_H eta < 1` and `C_V r <= r_V` hold in one realization.
  - Local exclusions centred at the trial, under the regularity, parity and canonical-velocity hypotheses of
    section 7: radius `2.2e-8` in four jet values at the source P; radii
    `2.1886e-8` (axis velocity suprema) and `3.2318e-7` (in `H^{153/50}(R^2)`) for a moving source; no exact solution
    `rho~ + h` with h in `L^2(R^2)`. None is known to contain X3 or a meaningful uncertainty ball, so none is a NO.
  - Obstructions: centre quasimodes exclude a same-norm inverse estimate, and any Fredholm closed realization
    containing them, for the linearization L at the trial in X, in each `X_m` and in the weighted factor supremum
    norm. In the axis-weighted norms `Y_(a,s)` with `a >= 0`, `s >= 3/2`, the frozen centre transport is invertible
    only where L fails to map all compact test densities into the space and the trial's residual is not in it; for every
    real a and finite `s >= 0` the quadratic term is not continuous at 0 from the graph norm of L into `Y_(a,s)` (on the
    class of 5(q)), and for `a < 5/2` the centre normalization is not a closed constraint (sections 5(p) to 5(r)).
- Best numerical evidence (floating point, never used as a bound): X3's published sampled residuals, reproduced by an
  independent evaluator (normalized maximum about `7e-7` near P, largest absolute residual about `1.9e-4` in the
  outermost sampled region; section 6). If the 19389 saved cell majorants of the derivative certificate are valid,
  the X bounds drop to `0.385656000027` and `585.874000000002` (a verified implication from unverified hypotheses).
  Finite sections of L show soft far-field directions; equal-residual states have `c_l` from 5.29 to 5.60.
- Exact remaining gap (first missing implication): a bounded inverse of L at the trial in one realization, that is,
  forcing spaces containing the trial's residual with a certified bound eta, constants `K_H` (high solvability) and
  `K_L` (low a priori estimate) uniform on a ball, a bilinear bound `C_B` for the quadratic term, and a closed
  treatment of the centre normalization and the strain c. No Fredholm realization of L is known in any class; the
  verified quasimodes show it must use norms or domains other than those tested (section 10, item 1). None of the
  obstructions implies that no exact profile exists near X3; all are specific to a method or a norm.
- Checks: section 8 records the independent computations, referee audits and their limits. Some checks share
  certified inputs; in particular, the full integral giving X3's central strain was not independently recomputed a
  second time (section 7). This summary and the end-of-run records postdate the verifier's last report audit. The
  final timing and editorial-only interval are reported by the research team, not independently certified by that
  audit. Scripts, data, commands and replay limitations are in the accompanying artifacts (section 9).

Status of this document: final report. Recorded original completion: 2026-10-22T13:02:18Z.
Verification scope is stated item by item: certified results, conditional implications, proposals and
calculations still under audit have distinct statuses. Unverified items are not used as proved conclusions.
Floating-point evidence is never used as a certified bound.

## 1. Verdict
Verdict: UNRESOLVED (final; T0 = 2026-10-20T12:44:23Z, T_end = 2026-10-22T13:02:18Z, elapsed 48 h 17 min; section 3).

Mathematical scope: neither the existence of an exact solution of the canonical full-plane problem near X3 nor an
exclusion meeting the X3-neighbourhood criterion has been established in `P_2`, in any intermediate class `P_m` or in
`P_infty`. Nothing below is a numerical-evidence YES.

What is proved (the verification of each item is recorded in section 8):
- exact identities, certified scalar enclosures for X3 and for an exactly normalized explicit trial, local and
  frozen-coefficient linear theorems, and a conditional quasilinear (two-norm) iteration theorem (section 7);
- direct upper bounds for the residual of the exactly joined and exactly normalized trial, using its verified
  regularity, in the diagnostic weighted `H^1`-type norm X of section 10, on the whole plane and without the
  unverified majorant hypotheses of the conditional bounds of section 6: `||eps~||_X < 1.49546805188731021373656` and
  `||eps~ - partial_t eps~||_X < 2464.68293019825564964515`; in X the linearization admits no same-norm inverse
  estimate on domains containing the quasimodes of section 5(p), and these bounds are not used in a closing argument
  in this report;
- a quantitative exclusion in a neighbourhood of radius `2.2e-8` in four jet values at the source P of the trial
  (`h_y(P)`, `h_xy(P)`, `W[h]_1(P)` and `d_y W[h]_2(P)` for the correction h, where `W[h] = U[h] + (c[h]/3) X` is the
  velocity increment including the strain part, section 2; not known to contain X3; no numerical-uncertainty ball
  around X3 is proved to lie inside it, and in our judgement it is too narrow to contain a meaningful one; so not an
  exclusion endpoint; section 7);
- two moving-source exclusions of the same kind for the trial, within the parity (even in x, odd in y) and the
  canonical velocity law of section 2. The first has sufficient radius `2.1886e-8` in the two axis velocity suprema of
  5(o), for real solutions `rho~ + h` of class `C^1` near the moved source `P_h` on the x-axis, with `W[h]` of class
  `C^1` near I, `eps_0 < m R_I` and `g_h = d_y rho(P_h) != 0` (I, m and `R_I` as in 5(o)). The second has sufficient
  radius `3.2318e-7` in `H^{153/50}(R^2)` for real h; the norm bound itself supplies the source, regularity and
  `g_h != 0` conditions. This Sobolev ball is centred at a trial whose difference from X3 lies in no `H^s(R^2)` with
  `s >= 0` (section 7);
- an obstruction to every exact solution `rho~ + h` with h in `L^2(R^2)`, for any value of the coefficient of
  `X.grad rho` in the equation, under the hypotheses of section 7 (a class that contains neither X3 nor any
  neighbourhood of the trial in the factor norm of the axis control of section 4, so that it gives no exclusion
  neighbourhood of X3; section 7);
- counterexamples to proposed inverse and nonlinear mapping estimates, among them:
  - in the diagnostic weighted `H^1`-type norm of section 10, and in each norm `X_m` of section 5(p) (fixed integer
    `m >= 2`), the linearization at the trial has quasimodes concentrated at the centre, so no same-norm inverse
    estimate holds there and no closed realization in that norm containing them is Fredholm (section 5(p));
  - in the weighted factor supremum norm of the axis control of section 4, on continuous factors vanishing at 0 and at
    infinity, the linearization at the trial has unit weak-null quasimodes with zero strain, concentrated near the
    centre, so no same-norm inverse estimate holds on any domain containing them, none with a bounded linear compact
    remainder, and no closed linear realization in that norm containing them is Fredholm (section 5(r));
  - in the axis-weighted norms `Y_(a,s)` with `a >= 5/2` of section 5(q), which for `s >= 3/2` include every norm
    with `a >= 0` in which the frozen centre transport is invertible (exactly those with `delta_Y < 0`), the
    linearization does not map every smooth compactly supported density with `J = c = 0` supported away from both
    axes into the space, and the trial's residual itself is not in the space (for `s = 153/50` and `a >= 0` it lies
    in `Y_(a,s)` exactly when `2k < a < 5/2`, where the frozen centre transport is not Fredholm; section 5(q));
  - for `s = 153/50` and every real a, no closed linear realization of the linearization in `Y_(a,s)` has a domain
    containing the maximal domain of the frozen centre transport (section 5(q));
  - for every real a and finite `s >= 0` the quadratic term is not continuous at 0 from the graph norm of the
    linearization at the trial into `Y_(a,s)`, on the compact-potential class of 5(q), on each of its linear subspaces
    of finite algebraic codimension, and on the zero set near 0 of any finitely many constraints that vanish at 0, are
    continuously Frechet differentiable in the graph norm and have onto derivative at 0 (section 5(q)).

The decisive missing input is a bounded inverse of the linearization: no Fredholm realization of it is known in any
class (section 10, item 1), so the inputs `K_H`, `K_L`, `C_B`, `C_V` and `eta` of the verified two-norm theorem of
section 7 are not available in one realization, and no residual bound of the trial in a norm with derivatives matched
to a realization is available (section 4).

Evidence, not proof: the floating-point calculations of this report (among them the finite sections of the
linearization, the Sobolev norms of the trial's residual near P, the sampled residual maxima of X3, the equal-residual
states with `c_l` between 5.29 and 5.60 and the jet quantities at P of X3 minus the trial) are listed in section 4 and
are never used as bounds.

## 2. Problem, admissible class, canonical inverse, normalization, candidate
- Equation: `F(rho) := (c_l X + U[rho]).grad rho - rho = 0` on R^2, `U = (-psi_y, psi_x)`, `-Lap psi = d_x rho`, where
  `c_l = c_l[rho] = (1 + psi_xy(0))/3` is the centre-normalized exponent (next bullet), so that F depends on rho
  alone, and U is given by the canonical whole-plane inverse: under the growth bound of `P_2` it is characterized by
  `div U = 0`, `curl U = -d_x rho`, the parity and `U(X) = o(|X|)` at infinity (no harmonic `lambda x y` term in psi),
  and computations use the angular-mode Green representation of the problem statement. rho even in x, odd in y. A held
  numerical exponent (X3, below) is named as such where it differs from `c_l[rho]`.
- Centre: `rho = x^2 y a` near 0, `a` continuous, `a(0) = 1`; `c_l = (1 + psi_xy(0))/3`. This is the `x^2 y`
  coefficient of the equation; it is verified under continuous factorization by a rescaled distributional limit, so it
  needs no derivative of `a`.
- `P_2`: `rho` in `C^{2,alpha}_loc` for some `0 < alpha < 1`, with this centre factorization (`a` merely continuous),
  the canonical velocity law, the stationary equation `F(rho) = 0` pointwise, and
  `|rho| + (1+|X|)|grad rho| <= C (1+|X|)^gamma` for some `gamma < 1`. `P_infty`: in addition `a` is `C^infty` near 0.
  `P_infty` constrains only the centre. It does not by itself give smoothness at the axis source P (verified scope
  statement). `P_m` denotes an intermediate class (for example `P_2` with `a` of class `C^m` near 0); the problem
  statement leaves it open, and no statement of this report depends on its exact definition.
- Linearization at rho: `L h = (V.grad - 1) h + W[h].grad rho`, with `V = c_l X + U[rho]` and
  `W[h] = U[h] + (c[h]/3) X`, where `c[h] = psi[h]_xy(0)` (the problem statement writes `c[h]` for `psi[h]_xy(0)/3`;
  this report's `c[h]` is three times that). The centre-normalized `c_l` is built into F, so the x^2 y coefficient of
  F vanishes identically and no separate scalar closure equation is needed; at a fixed exponent the term
  `(c[h]/3) X.grad rho` would be absent. (The letter L also denotes the length scale of X3 below; the length scale
  enters only through `u = r/L` and powers `L^{3-k}`.)
- Constants of X3: `k = 1615536043799051/2^53` exactly (decimal display 0.17936053129375418; `c_l`, A and D are
  defined from it), the held exponent `c_l = 1/k`, about 5.575362610641546, `A = 2c_l - 1`, about 10.1507252,
  `D = 2A + 1`, about 21.3014504, `L = 7.651424601381517` (the stored length scale, an exact dyadic). The axis source
  of X3 is at `x_*` about 8.600064 (problem statement); the trial's source is `P = (p, 0)` with `8.6 < p < 8.60006381`
  and `g = rho~_y(P)` about 29.7495 (section 7). In statements about a general profile or background, `x_*` denotes
  the abscissa of its axis source P. Decimal values in this report are rounded summaries; hypotheses use the exact
  expressions.
- Exponent `c_l` of X3 (soft direction). The problem statement reports that numerical fitting did not uniquely
  determine the held `c_l` of X3: nearby values gave competitive fits, the span `[5.5524653, 5.5793640]` of tested,
  not-yet-excluded fitting exponents is not a certified enclosure of the exponent of an exact solution, and an
  independently fitted fixed-`c_l` profile at `5.5683739` improved some residual diagnostics relative to X3. The held
  value is also not the centre-normalized value of X3's own canonical inverse: `c_l - (1 + c)/3 = (3/k - 1 - c)/3`,
  with `c = psi[X3]_xy(0)`, lies in `[3.4336e-9, 3.4339e-9]` (verified; section 3, entry 13:56; the problem statement
  gives about `3.2e-9`). The trial removes only this normalization defect, by construction (`c_l = 1/k` and
  `3 c_l - 1 - c[rho~] = 0` exactly; verified, section 3, entry 14:53); enforcing this scalar identity does not by
  itself resolve the ambiguity of the exponent. No result of this report certifies the exponent of an exact solution:
  in the formulation of 5(h) and section 10, where the leading far angular profile `Theta` is prescribed and the far
  exponent `k'` and a tail amplitude are unknowns, `c_l = 1/k'` is an unknown, its first-order variation along the
  conditional family is given by the functional `ell`, which is not computed (5(h)), and the first run observed
  equal-residual states with `c_l` between 5.29 and 5.60 (floating point; section 10, "Kernel, family or
  ill-conditioning").
- Candidate X3 was reconstructed exactly from its coefficient files; the hashes match the problem statement. The
  reconstruction reproduces the published independent generator to 1.3e-13 (floating-point comparison).
- New explicit trial `rho~`:
  - Form: `x^2 y sum_{m<260} a_m(r) cos(2 m theta)`, with `a_m` exponential-polynomial splines in `t = log r`.
  - Inner and outer pieces: near 0 each radial coefficient is
    `a_m = delta_{m0} + sum_{j=1}^{7} D_{mj} (r/r_-)^{2j} + (r/r_-)^{b_i} sum_{i=0}^{6} E_{mi} (log(r/r_-))^i` with
    `r_-` the first knot and `b_i` about 50 (the last sum is the exact join correction), so the factor is continuous
    with value 1 at 0 (`a_0(0) = 1`, `a_m(0) = 0` for `m > 0`); the sum over modes is not a Cartesian polynomial, the
    factor is not `C^2` at 0 (so the trial is not in `P_infty`), and the density is `C^{4,1}` but not `C^5` there
    (section 4); the `C^6` joins are at positive radii, and away from the origin the density is `C^6` (verified;
    timeline 10-21 20:26). Far out the coefficients are explicit power laws with the radial exponents of X3's
    far-field structure `u^{k-3}(1 + nu + nu^2 + ...)`, where `u = r/L`, `nu = u^{-(1-k)}` (with finitely many angular
    modes, so that the leading angular profile differs from that of X3; "Far tail" below). The trial satisfies the
    kinematic requirements of `P_2` (density `C^{2,alpha}` for every `alpha < 1`, continuous factor with `a(0) = 1`,
    the parities, a unique canonical sublinear velocity, density growth `r^k` with first derivatives `O(r^{k-1})`;
    verified, section 3, entry 14:53); it does not satisfy the equation (its far residual is nonzero, below), so it is
    not itself in `P_2`.
  - Green integrals in closed form.
  - Normalization: `c_l := 1/k`, and the dependent coefficients are defined exactly by the C^6 join equations and by
    `3 c_l - 1 - c[rho~] = 0`.
  - Fit: its modes agree with X3's to about `1e-9` relative (floating-point comparison; not a certified bound).
  - Floating-point evaluations: the numerical team's floating-point diagnostics for the modal trial quoted in this
    report, including the exploratory calculations in section 4, the jet comparison in section 7 and the diagnostics
    in section 10, use the stored coefficient representation. Its inner and outer join corrections and `A_00`, the
    leading outer coefficient of the factor mode `m = 0`, retain their values from the floating-point constrained
    least-squares fit; with these values the stored representation is discontinuous across both joins `r = R_i` and
    `r = R_e` (section 6) and is not in `H^1_loc` there (verified; section 10, next step 1). For rho~, the exact `C^6`
    join equations and normalization instead determine these dependent coefficients, with the independent stored
    coefficients held fixed. The numerical team's report describes the coefficient differences as "at most 1e-13 relative"
    (reported numerical comparison, not independently checked and not used as a bound). The certified exactification
    cost (`< 4.080e-10` relative in a weighted factor norm; section 4) does not by itself transfer these
    floating-point diagnostics to rho~; their errors relative to the corresponding quantities for rho~ are not
    certified. Certified statements about the modal trial concern rho~, subject to their stated hypotheses and scope,
    except where they explicitly concern the stored trial or saved numerical data (section 10, next step 1).
  - Far tail (verified; section 3, entry 05:22): uniformly in angle, `r^{-k} X3 -> Theta_X` and
    `r^{-k} rho~ -> Theta_M`. Here `Theta_M` is a trigonometric polynomial, while `Theta_X` contains the factor
    `exp(T(1) |cos theta|^{p_3-2} sin^2 theta)`, with `T(1) > 0` (exact) the endpoint value of the degree-5 Chebyshev
    factor of X3's formula and `p_3 = 6 + 2/(2 c_l - 1)` in `(6, 7)` (the exponent of the incoming saddle mode,
    section 10), and is not `C^7` at the y-axis. At `theta = pi/4` two interval engines give
    `8.2716924477e-10 < Theta_X - Theta_M < 8.2716924478e-10` and `90.8102098389788 < Theta_M < 90.8102098389789`, so
    the limiting relative difference `(Theta_X - Theta_M)/Theta_M` there lies in `(9.1087e-12, 9.1088e-12)`. Hence
    `X3 - rho~` lies in `L^2(R^2, <r>^{-2 beta} dX)` (the space `H_beta` in the notation of 5(m)) if and only if
    `beta > 1 + k`, and in no `H^s(R^2)` with `s >= 0`; the affine sets `rho~ + H^s(R^2)` and `X3 + H^s(R^2)` are
    disjoint, so no `H^s` correction ball about the trial contains X3. This comparison of two explicit functions is
    not a nonexistence statement for solutions, and no explicit radius beyond which the tails separate by a stated
    amount is certified.
  - Its only residual is the transport residual `eps~ = F(rho~)`; the elliptic equation holds exactly.
  - Far residual (verified; section 3, entry 05:37): uniformly in angle `eps~ = r^{2k-1} Eps(theta) + o(r^{2k-1})`,
    with Eps a finite odd sine polynomial whose `sin theta` coefficient `Eps_1` satisfies
    `-0.03688201144 < Eps_1 < -0.03688201143` (two interval engines; it is the physical form of the coefficient
    `e_0 in (-2.000282880e-4, -2.000282879e-4)` of `sin theta e^{(2k-1) tau}`, `tau = log(r/R_b)`, `R_b` the last
    knot, `Eps_1 = R_b^{1-2k} e_0`). Hence `eps~` tends to zero at infinity but lies in `L^2(R^2, <r>^{-2 beta} dX)`
    if and only if `beta > 2k`; it is not in unweighted `L^2(R^2)`, nor in `dot H^{-1}(R^2)` or `H^{-1}(R^2)`
    (verified, section 3, entry 06:32: the annular tests `eta(|X|/R) Eps(arg X)`, eta a fixed nonnegative, nonzero
    function in `C_c^infty((1, 2))`, have gradient norm independent of R and pairings of exact order `R^{2k+1}`, and
    their multiples by `R^{-1}` are bounded in `H^1(R^2)` with pairings of exact order `R^{2k}`).

- Shared interval archive and the canonical moment condition. The source computations of 5(o) and the zeroth-order
  residual certificates of section 6 use a shared archive of interval enclosures of the density polynomials and of the
  canonical density moments of the exact normalized trial, with the prescribed whole-plane boundary conditions
  (section 6). The two source evaluations and the two interval methods in each residual region share this archive.
  Their agreement does not by itself validate its enclosures. The source results and the middle-region and whole-plane
  residual bounds were previously stated under the canonical moment condition: the archived moment intervals used by
  each computation contain the corresponding canonical moments of the distinguished exactly normalized trial. The
  inner and exterior certificates also depend on the archive, through the first span's right-end J moments and the
  last span's left-end I moments, respectively. Earlier versions of this report did not state those dependencies
  explicitly. A separate complete computation by a second propagation method has since verified that every moment
  interval and every density polynomial interval of this archive contains the corresponding canonical moment or exact
  coefficient of the trial (timeline 10-21 21:13; section 8), and explicit dependency compositions have verified that
  the source computations of 5(o) and the middle-region, inner, exterior and whole-plane residual bounds of section 6
  use exactly these archived intervals (timeline 10-21 21:21 and 10-21 21:34; section 8). For these results the
  condition is therefore discharged: `M_V < 0.2972` and the quantities derived from it (the source constants, the
  variation of `DV` on the source disc and the source cutoff sign, the auxiliary inverse ceilings, the moving-source
  radii `2.1886e-8` and `3.2318e-7`, the Sobolev-ball coefficient `0.06970585` and the `K_1` bounds of 5(o)), and the
  zeroth-order residual bounds of section 6, hold for the trial without this additional condition. Every conclusion
  retains its other stated hypotheses, domain and regularity requirements, and the auxiliary inverse ceilings remain
  upper bounds for an auxiliary inverse only. The trial is the one exactly normalized trial: its normalization
  coefficient is fixed by the exact normalization identity and enclosed in an accepted interval, which serves only for
  interval inclusion; other values in that interval are not asserted to give normalized trials. The verified density
  polynomial enclosures, the density Hessian bound `M_rho < 0.5059`, the independently computed point scalars of
  section 4 with their jet-continuity exclusion, the point values at the trial's source quoted in 5(o) (the zero P,
  its uniqueness in the stated bracket, and A, mu and g) and the universal Fourier constants of the whole-plane
  Sobolev ball never required the condition. The exported Green boundary values of all middle cells and the radial
  Taylor models of the flow certificate on three middle cells (5(l)) were stated under the same condition; a further
  dependency composition has verified that they use exactly the archived intervals (timeline 10-21 21:54; section 8),
  so these memberships hold for the trial without the condition, with their other hypotheses and qualifications
  unchanged. For the same trial, the canonical input membership for the flow composition is also verified on the nine
  closed rectangles of 5(l), placing `s`, `v_2`, `v_1` and T in the 36 reported ranges, with continuous axis quotients
  (timeline 10-21 22:59; section 8); this applies the accepted composition without recomputing its modal products and
  retains all its other analytic and arithmetic hypotheses, including the qualifications of the runtime models. The
  radial Taylor models of the flow certificate on all 7809 middle cells, verified later as a finite-input statement,
  receive their canonical meaning for the trial through the same boundary and density memberships (timeline 10-22
  00:16 and 10-22 00:18; 5(l)). The derivative checks at the 13 sample log-midpoints and the derivative majorants
  verified on three middle cells in section 6 use separate inherited canonical moment certificates at the
  log-midpoints, computed without the archive as input, so the verification of the archive does not cover them; a
  second, independent integration of the canonical moment equations has verified these certificates (timeline 10-22
  00:23; section 8), so these results also hold for the trial without that condition. Timeline entries record each
  result in the form in which it was first verified, with a note where the condition was later discharged. General
  analytic theorems retain their stated hypotheses.

## 3. Timeline
- Timing reported by the research team: T0 = 2026-10-20T12:44:23Z (start of the analysis).
  T_end = 2026-10-22T13:02:18Z (recorded completion of this report). Elapsed wall time T_end - T0:
  48 h 17 min (truncated to whole minutes). The team reports that research ran
  until the limit of the run, 48 h after T0 (2026-10-22T12:44:23Z); the mathematical content of this report was last
  changed at 2026-10-22T12:21:04Z. Between that limit and T_end only editorial finalization was done (the summary at
  the top, this timing record, the description of the accompanying artifacts in section 9 and their assembly); no
  research or computation was started after the limit. The interval from T0 to the limit is the 48 h window
  requested by the problem statement, with the restart gaps listed below. Session spans are wall-clock spans,
  not measurements of continuously active work. The verifier's last report audit predates the reported final
  completion and does not certify that end time, the editorial-only interval or completion of 48 h of genuine
  research. No decisive endpoint was reached, so the verdict is UNRESOLVED.
- Sessions (UTC): consecutive sessions, restarted from the written record, of about 6 h each except the last two:
  10-20 12:44:23 to 18:44:24, 10-20 18:44:54 to 10-21 00:44:54, 10-21 00:45:24 to 06:34:17, 10-21 06:34:47 to
  12:19:44, 10-21 12:20:14 to 18:10:28, 10-21 18:10:58 to 10-22 00:01:01, 10-22 00:01:31 to 06:01:31, 10-22 06:02:01
  to 12:02:01, 10-22 12:02:31 to 12:40:05, and 10-22 12:40:35 to 12:41:21 (a closing check without change of this
  report); the checks of the verifier continued until the limit, and the finalization began at 10-22 12:49:48.
  Interruptions: nine gaps of 30 s between sessions. The proofs, scripts, data and evidence files of the computations
  and of the verification are in the accompanying artifacts (section 9); raw run logs are not published.
- Verification timeline (UTC, 2026-10-20 unless marked 10-21 or 10-22):
  - 13:13 X3 file identity and reconstruction; central strain formulas.
  - 13:31 to 14:00 numerical defects found in the numerical team's first evaluator and later repaired. The defects
    were a strain head bias, a shifted-stencil sign, a spline-span selection at exact knots, and an unstable
    primitive.
  - 13:56 exact X3 central strain `c in [15.72608782162331, 15.72608782162370]`; the held normalization defect is
    `3/k - 1 - c in [1.03009e-8, 1.03014e-8]`.
  - 14:07 conditional positive-axis source theorem (section 4).
  - 14:20 to 14:29 refutation of the first specification's inverse spaces; exact scalar-and-tail repair of X3 at
    factor distance `< 1.477e-5`.
  - 14:53 exactly normalized modal trial: the total exactification cost is `< 4.080e-10` relative. Also confirmed: the
    local source transport theorem and the conditional two-norm theorem.
  - 15:11 to 15:18 frozen coupled operator at the source: exact conjugation, same-order Sobolev inverse below
    threshold, and infinite cokernel above threshold. One proposed below-threshold obstruction (Weyl sequences) was
    refuted.
  - 15:30 scaling covariance, source functional, codimension-one index bookkeeping (conditional), and an
    interval-Newton derivative defect in the numerical team's source certificate.
  - 15:41 independent certification of the trial's source scalars, by all-mode density moments and exact sign
    bisection; independent check of 180 selected Green boundary values.
  - 15:53 direct interval axis velocities of X3 at x = 7 and x = 10.
  - 16:09 rigorous residual Wiener sums of the trial at 13 exact log-midpoints (independent density integration);
    conditional variable-coefficient source obstruction in ordinary Sobolev graph realizations (section 5(d)).
  - 16:14 complete-cell residual bounds at 13 selected middle-region cells, below the numerical team's values.
  - 16:29 uniform frozen coupled source inverse through `mu = 1`; the inferred `1/|mu~ - 1|` cost for the coupled
    inverse is refuted (section 5(c)).
  - 16:38 finite scalar borders and finite-rank changes preserve Fredholmness (with the index shift), so they cannot
    repair the obstruction of section 5(d).
  - 16:53 to 17:02 complete coarse zeroth residual majorant on the whole inner disc (section 6); a transport graph
    norm cannot carry a continuous quadratic transport term into the same Sobolev target (section 5(g)).
  - 17:07 to 17:20 weighted saddle model inverse and a sufficient exit-trace condition (section 5(e)); face velocity
    Taylor splitting with explicit constants, and a low-frequency obstruction to the coupling on face weights
    (section 5(f)). Both were also checked by a separate referee audit.
  - 17:43 to 17:44 conditional tail, kernel and family theorems (section 5(h)), with three corrections to our first
    version; complete coarse zeroth residual majorant on the whole exterior (section 6).
  - 17:46 separate referee audit of the tail and family theorems (one model); its corrections are included in 5(h).
  - 17:49 the isotropic energy symbol at the saddle (section 5, closing list), with a scope correction.
  - 17:58 exact leading far-field coefficient of the trial's residual (cancellation between equal exponents); tail
    bounds beyond `log(r/R_e) >= 9` (section 6).
  - 18:25 near/far splitting of the velocity and the coupling on bounded collars of the x-axis (section 5(i)), with
    two corrections (the far-weight endpoint and finite strain as a separate hypothesis); also referee-audited.
  - 18:33 complete exterior residual certificate for the trial (section 6), replacing the coarse exterior majorant.
  - 18:55 complete inner residual certificate for the trial (section 6), replacing the coarse inner-disc majorant.
  - 18:57 explicit Fourier formula for the frozen coupled inverse at the source, and a compact counterexample showing
    that the normalized linearization has no local solvability condition at P (sections 4 and 5(b)).
  - 19:05 structure of the velocity at the y-axis: swap identities, edge smoothing, local edge compactness, and the
    failure of classical density jets in weighted `L^2` (section 5(j)).
  - 19:06 exact feasibility margins at the revised weight parameters (section 5(e)).
  - 19:25 centre obstruction for the trial: its density is `C^{4,1}` but not `C^5` at the origin, and its residual is
    not square integrable near 0 in any corner product weight `|x|^{-2a} |y|^{-2b}` with `a + b >= 6` (section 4).
    Also checked by a separate referee audit.
  - 19:49 corner coefficients of the velocity (kernels, boundedness criteria, exact dual norms), the two leading
    coefficients of the normalized corner coupling, and the failure of a corner coupling bound on the global pure
    product weight (5(k), section 4). Derived independently by a separate referee.
  - 20:05 conditional global characteristic flow, weighted transport inverse with orbit-segment costs, and the far
    lower bound for the transport inverse (5(l)). Also checked by a separate referee audit.
  - 20:13 exterior flow certificate for the trial: radial drift for `r >= 3634`, and the stated uniform
    component-quotient bounds for `r >= 4000` (5(l)).
  - 20:26 box-crossing cost bound and the maximal-domain transport inverse, with the correction of a rounded
    constant (5(l)). Also checked by a separate referee audit.
  - 20:34 double Taylor remainder bound with explicit constants and its conormal commutators (5(k)). First derived
    by a separate referee.
  - 20:44 full middle-region zeroth-order residual certificate, one interval method plus output audit (section 6); the
    second method was then running and was accepted as complete on 10-21 at 16:10; both methods share the canonical
    density moment archive, and the bounds were conditional on it (10-21 16:10) until this condition was discharged
    (10-21 21:34). Primary assembly confirmed at 20:56 (exact final comparisons of every public bound).
  - 20:53 annular velocity traces of the corner splitting (5(k)). Also checked by a separate referee audit.
  - 21:08 local corner coupling for a `C^8` factor, with explicit constants (5(k)). Also checked by a separate
    referee audit.
  - 21:17 axis jets of the transport: P-row of the jet equation, corner cubic factor, homogeneous mode at P,
    normalized solution with its endpoint condition and a counterexample, conditional block bound (5(l)). Also
    checked by a separate referee audit.
  - 21:27 cubic axis coefficient `B_3`: axis identities, smoothness criterion with its exact hypotheses, cutoff
    multipliers, and the failure of low-norm continuity (section 10, centre coefficient). Also checked by a separate
    referee audit.
  - 21:34 exact resonant logarithms of the trial at the origin; the polynomial-only premise of the `B_3` criterion
    fails for the trial (section 10, centre coefficient). Also checked by a separate referee review.
  - 21:44 frozen source inverse on its maximal graph domain for `3 < sigma < 2373/680`, the full P-row, and the
    integrability condition of the origin matching (5(c), 5(l)). Also checked by a separate referee audit.
  - 21:53 velocity multipliers of a fixed transverse jet extension at the x-axis and a conditional finite-interval
    inverse (5(l)). Also checked by a separate referee review.
  - 21:58 transverse-scale term of a strip-to-disc energy design and its two conditional obstructions (section 10).
    Also checked by a separate referee review.
  - 22:13 axis crossing cell of the trial: on the radial cell containing `p`, `10.1494 < w' < 10.1525` and exactly one
    zero of `V_1(x, 0)` (5(l)). Also checked by a separate referee review.
  - 22:19 far domain of a jet-plus-remainder realization: an exact profile, `X.grad rho` and the scaling tangent lie
    outside the natural far space, and a compact core with nonzero strain maps outside it (5(m)). Also checked by a
    separate referee audit.
  - 22:27 y-axis jets: jet velocity coefficients, the vanishing cubic coefficient, the cancellation in the `x^2`
    row and the diagonal matching conditions of the `x^2` and `x^4` rows (5(m)). Also checked by a separate referee
    audit.
  - 22:36 tail coordinates of the far directions, the reduced scalar row and the dual norm of the strain functional
    (5(m)). Also checked by a separate referee audit.
  - 22:41 pure transport at a source: a smooth compact forcing whose transport-only solution has no `C^1`
    representative (and is not in `H^1_loc` when `A >= 3`), and the source eigenvalues `mu_P = 1`,
    `A_P = 2 c_l - 1` at every exact `C^1` solution (5(l)). Also checked by a separate referee review.
  - 23:03 obstructions at lower Sobolev order: frozen source examples with harmonic local forcing and limited
    regularity, the exact strain norm on `H^sigma` and its failure below order 2, regularity without factorization,
    the interpolation constant and the weight window (5(n)). Also checked by a separate referee review.
  - 23:24 flow margins of the trial on the whole inner disc and on the far tail `r >= e^{t_b + 9}`, and the exact
    vanishing of `rho` and `grad rho` on the y-axis (5(l)); a finite exact audit of the middle-region modal maps used
    by the numerical team's flow certificate (section 8).
  - 23:31 conditional radius theorem for the interval matrix products of the numerical team's residual arithmetic,
    under explicit floating-point hypotheses (section 8).
  - 23:58 angular part of the numerical team's flow certificate: exact mode-factor identities, all angular nodes and
    finite remainders, and the coefficient boxes at 221 cell centres (section 8). Also checked by a separate referee
    review.
  - 10-21 00:03 frozen Hoelder inverse at the source: the `L^2` bound, the Hoelder-Zygmund loss `(sigma - 1)/A` and
    its sharpness, the logarithm at order 1 and the regularity ceiling for smooth forcing (section 10). Also checked
    by separate referee reviews.
  - 10-21 00:22 finite cell scalars of the numerical team's flow certificate: scalar enclosures and exact radial
    geometry of all 19389 radial cells (section 8). Also checked by separate referee reviews.
  - 10-21 00:24 jet-continuity exclusion centred at the trial's source (section 7), the normalized face-coupling
    coefficient (5(f)) and a local `C^1` forcing without Dini modulus that has a `C^1` solution (5(a)). Also checked
    by a separate referee review.
  - 10-21 00:41 local a priori estimate for the linearization at the source at order 31/10, with forcing coefficient
    exactly `1/(kappa - E)` (5(o)). Also checked by separate referee reviews.
  - 10-21 00:46 auxiliary inverse at the source: maximal domain, semigroup bound and two-sided inverse (5(o)). Also
    checked by separate referee reviews.
  - 10-21 00:56 sign of the canonical raw strain in the local source analysis: its circular principal-value form and
    the rank-one denominator `1 + c[A_op^{-1} a_delta]` (5(o)); the opposite-sign identification in the verifier's
    first notes is refuted. Also checked by separate referee reviews.
  - 10-21 00:56 exact centre regularity of the numerical team's second trial and a nonzero change of its exterior
    stream coefficient (section 10, next step 2). Also checked by a separate referee review.
  - 10-21 01:03 radial defect criterion for the modal Green equations (5(l)). Also checked by a separate referee
    review.
  - 10-21 01:10 exact implication from a coefficient bound to the local source constants (`C_src < 13.34` on the disc
    of 5(o) at `delta = 0.0165` gives `E < 0.22011` and `K_1 < 0.318`); the coefficient bound itself is not verified,
    and three rows of the first version of the numerical team's fine pass are shown by exact comparisons to be
    inconsistent with its reported radial coverage (5(o)). Also checked by separate referee reviews.
  - 10-21 01:25 cell-cover geometry of the exported coordinate masks of the revised coefficient pass on the source
    discs; 01:32 an independent bound
    of the density Hessian on the disc of 5(o) at `delta = 0.0165`, `M_rho < 0.5059` (5(o)). Also checked by
    separate referee reviews.
  - 10-21 01:44 an independent bound of the velocity Hessian on the same disc, `M_V < 0.2972` (under the canonical
    moment condition, discharged 10-21 21:21; 5(o)). Also checked by separate referee reviews.
  - 10-21 01:49 the sum-of-squares coupling bound and its commutator and conjugation estimates, under stated global
    hypotheses (section 10, item 1). Also checked by separate referee reviews.
  - 10-21 01:52 the trial's local source constants at `delta = 0.0165` from the two Hessian bounds:
    `C_src < 13.91094`, `E < 0.22953051`, `K_1 < 0.3181` (5(o)). Also checked by separate referee reviews.
  - 10-21 02:04 conditional statements for an outer estimate with a source cutoff (section 10, item 1). Also checked
    by separate referee reviews.
  - 10-21 02:09 the trial instance of the hypotheses of the local source estimate and auxiliary inverse (exact source
    bracket, `D_P`, `grad rho~(P)` and coefficient regularity), and the source cutoff sign (5(o)). Conclusions using
    the whole-disc velocity bounds were stated under the canonical moment condition, discharged 10-21 21:21. The axis
    zero, its uniqueness in the stated bracket and the point data also follow from the independent point certificate
    of section 4 without that additional condition. Also checked by separate referee reviews.
  - 10-21 02:13 the strain part of the source velocity of the difference between X3 and the trial (section 7); a
    conditional implication from exponential semigroup decay to a stationary inverse (section 10, item 1). Also
    checked by separate referee reviews.
  - 10-21 02:22 the order family `s in [61/20, 31/10]` of the local source estimate (5(o)). Also checked by separate
    referee reviews.
  - 10-21 02:34 the source of perturbed profiles: location, source data, stationarity at the moved source and the
    transported local estimate (5(o), section 7). Also checked by separate referee reviews.
  - 10-21 02:39 finite-input verification of the radial Taylor models of the flow certificate on three selected middle
    cells, all 261 modes (5(l); canonical membership of the input boxes then open, verified later, 10-21 21:54;
    limited scope, later extended to all middle cells, 10-22 00:16 and 10-22 00:18). Also checked by separate referee
    reviews.
  - 10-21 02:55 an explicit bound of the auxiliary source inverse of the trial for one explicit cutoff, for every
    order in `[61/20, 31/10]` (5(o)). Also checked by separate referee reviews.
  - 10-21 03:03 the isotropic dilation corollary of the auxiliary source inverse: the same bound in the scaled norms
    `N_{1/ell}`, and in `H^s` with the factor `ell^{-s}` (5(o)). Also checked by separate referee reviews.
  - 10-21 03:18 explicit bounds of the auxiliary source inverse of the trial in the scaled norms, for the cutoff of
    the 02:55 entry: below 922 in `N_500` and below `1.223e11` in `H^s`, for every order in `[61/20, 31/10]` (5(o)).
    Also checked by separate referee reviews.
  - 10-21 04:16 the rough-coefficient extension of the local source estimate and of the auxiliary inverse
    (coefficients in `H^sigma`, `sigma > 3`), whose completion contains the whole-plane `H^s` functions with zero
    value and gradient at the origin (5(o)). Also checked by separate referee reviews.
  - 10-21 05:09 the whole-plane Sobolev ball: for corrections of norm at most 7/50 in `H^{153/50}(R^2)` the location,
    coefficient-box and Hessian hypotheses of the moving-source estimate hold, with `K_1 < 0.32123200` uniformly, and
    the trial is not stationary at its moving source on the ball of radius `3.2318e-7` (5(o), section 7). Also checked
    by separate referee reviews.
  - 10-21 05:22 the leading far tails of X3 and the trial differ: `X3 - rho~` is in `L^2(<r>^{-2 beta} dX)` exactly
    for `beta > 1 + k`, so in no `H^s(R^2)` with `s >= 0` (section 2). Also checked by a separate referee review.
  - 10-21 05:37 no exact solution `rho~ + h` with h in `L^2(R^2)` exists, for any value of the coefficient of
    `X.grad rho`, under the hypotheses of section 7; the trial's residual is `r^{2k-1}` times a nonzero angular
    profile at infinity, in `L^2(<r>^{-2 beta} dX)` exactly for `beta > 2k` (sections 2, 7). Also checked by separate
    referee reviews.
  - 10-21 05:53 exactly normalized tail repairs `rho_T` of the trial with residual in `L^2(R^2)` (norm not
    quantified), at factor distance below `0.334616 T^{k-1}` from the trial (section 10, item 4). Also checked by
    separate referee reviews.
  - 10-21 06:04 higher exactly normalized tail repairs `rho'_T` of the trial whose residual `eps'_T` has `r eps'_T` in
    `L^2(R^2)`, hence a finite homogeneous `dot H^{-1}` norm (not quantified), at factor distance from the trial
    tending to zero as `T -> infinity` (section 10, item 4). Also checked by separate referee reviews.
  - 10-21 06:32 the trial's residual is in neither `dot H^{-1}(R^2)` nor `H^{-1}(R^2)`; the residual norms of the tail
    repairs grow at least like `T^{2k}` (`L^2`, `H^{-1}`) and, for the higher repairs, at least like `T^{2k+1}`
    (`dot H^{-1}`), with explicit asymptotic constants (section 10, item 4). Also checked by separate referee reviews.
  - 10-21 06:39 for the higher tail repairs `rho'_T` also `liminf_{T -> infinity} T^{-2k-1} ||r eps'_T||_{L^2}`
    exceeds `0.0022215507882` (asymptotic statement; section 10, item 4). Also checked by a separate referee review.
  - 10-21 07:03 the `r^{3k-2}` residual row of the tail repairs `rho_T` is nonzero (strict enclosure of its
    `sin(theta)` coefficient), so their residual `eps_T` is not in `dot H^{-1}(R^2)` and `r eps_T` is not in
    `L^2(R^2)`; within a stated finite class of exterior expansions the `r^{3k-2}` counterterm of `rho'_T` is
    necessary (section 10, item 4). Also checked by a separate referee review and a separate recomputation by another
    route.
  - 10-21 07:19 the `r^{k-2}` residual row of the tail repairs `rho_T` is nonzero (exact coefficient with a strict
    enclosure), so their residual `eps_T` is not in `dot H^{-1}(R^2)` and `r eps_T` is not in `L^2(R^2)`; within a
    stated finite class of exterior expansions the `r^{k-2}` counterterm of `rho'_T` is necessary (section 10, item
    4). Also checked by a separate referee review and a separate recomputation.
  - 10-21 07:19 the tail repairs `rho_T` change the velocity at the trial's source P by less than `1e-8` (explicit
    interior harmonic bounds after the exact strain compensation), so `|partial_y F(rho_T, 1/k)(P)| > 3.69e-7` for
    every admissible T (section 10, item 4). Also checked by a separate referee review.
  - 10-21 07:19 explicit upper bounds for the factor distance of the higher tail repairs `rho'_T` (below `5.448e-4` at
    `T = 10^4`) and for their velocity change near the trial's source, so `|partial_y F(rho'_T, 1/k)(P)| > 3.69e-7`
    for every `T >= 10^4` (section 10, item 4). Also checked by a separate referee review and a separate recomputation
    of the counterterm coefficients from the original data.
  - 10-21 07:33 bounds for every component of the velocity change `U[rho'_T - rho~]` of the higher tail repairs and of
    its Cartesian partial derivatives through order 3 on `|X| <= 9`, valid for every admissible T, so
    `|partial_y F(rho'_T, 1/k)(P)| > 6.6989e-7` at the trial's source P for every admissible T (section 10, item 4).
    Also checked by a separate referee review with a separate reconstruction of the three angular rows from the
    original data.
  - 10-21 08:14 the density change `rho_T - rho~` of the tail repairs is exactly the first compensated row of
    `rho'_T - rho~` (same profile, cutoff, exponent and compensator), so the first-row case of the 07:33 bounds
    applies: on `|X| <= 9` every component of `U[rho_T - rho~]` and of its Cartesian partial derivatives of orders 0,
    1, 2, 3 is below `1.523891e-12`, `5.139245e-13`, `1.184002e-13`, `1.590300e-14` for every admissible T, so
    `|partial_y F(rho_T, 1/k)(P)| > 6.7015e-7` at the trial's source P (section 10, item 4). Also checked by a
    separate referee review.
  - 10-21 11:16 whole-plane zeroth-order residual bounds of the trial, joined from the inner, middle and exterior
    certificates (exact common endpoints, complete tails, exact sum of the squared norms; the middle input from its
    one complete interval method with output audit): `sup W < 4.2805798591e-4`, `sup W/m < 2.91625e-4`,
    `N_0 < 1.904e-3` and the two weighted suprema (section 6); recorded as provisional at that time because the second
    middle method was still running; that method was accepted as complete on 10-21 at 16:10. The resulting global
    bounds were conditional on the shared canonical moment archive; this condition is discharged (10-21 21:34).
  - 10-21 11:35 the composition step of the flow certificate (the four flow fields `s`, `v_2`, `v_1`, T from the modal
    Taylor models, with the complete product remainder) on nine rectangles formed by the middle cells 0, 4102, 7808
    and three angular cells: the certificate's ranges contain two independent enclosures (5(l); conditional on the
    finite input boxes, a condition discharged on these rectangles for the distinguished exactly normalized trial,
    10-21 22:59; limited scope).
  - 10-21 11:43 flow margins of the trial on `r >= e^{t_b + 5}` (`T < -0.22`, `s, v_1, v_2 > 5.57`, both axes
    included), by an analytic transfer of the verified exterior velocity decay; the uncovered finite annulus of the
    flow hypotheses shrinks to `e^{t_a} < r < e^{t_b + 5}` (5(l)). Also checked by a separate referee review.
  - 10-21 11:52 two statements about the diagnostic `H^1`-type norm of the conditioned finite sections: the
    indicator-type J references are not in that space, and the central coefficient `a(0)` is unbounded in it (section
    10, next step 1). Also checked by a separate referee review.
  - 10-21 12:09 for finite piecewise-`C^1` sections with the stated endpoint growth, membership in the diagnostic
    `H^1`-type space is equivalent to exact agreement of all value traces at piece endpoints (section 10, next step
    1). Also checked by a separate referee review.
  - 10-21 12:15 the integral form of the raw strain is bounded on the diagnostic space and equals `psi_xy(0)` under
    the stated identification hypotheses; every level set of the central coefficient is dense, at fixed strain, among
    the densities of the space of the form `x^2 y a` near the centre with `a` continuous (section 10, next step 1).
    Also checked by a separate referee review.
  - 10-21 12:24 every tested mode-zero interior spline column of the conditioned sections (90 and 187 columns at the
    two section sizes) has a nonzero jump of its saved radial polynomial pieces at a piece endpoint inside the
    external annulus, so the encoded densities are not in the diagnostic space, and the full external-join constraint
    kernel of the larger section contains such a direction before eigenvalue truncation; the retained combinations and
    the computed spectra are neither certified nor refuted (section 10, next step 1). Also checked by a separate
    referee review.
  - 10-21 12:30 in the exact spans of the saved polynomial pieces of the conditioned sections, the exactly continuous
    subspace has dimension at most 515 for the smaller section and 771 for the larger one; for the smaller section the
    1866 retained columns exceed 515, so their interpretation as an orthonormal list in the diagnostic space is
    refuted; the computed spectra are not refuted (section 10, next step 1). Also checked by a separate referee
    review.
  - 10-21 12:40 exact repairs of the tested spline columns lie in new continuous subspaces of the diagnostic space,
    with single-column, single-mode relative broken-energy errors below `8.45e-15` and `2.57e-14` at the two section
    sizes; no distance in the space from the discontinuous originals, no relative bound for arbitrary combinations and
    no matrix or spectral transfer is established (section 10, next step 1). Also checked by a separate referee
    review.
  - 10-21 12:53 for the selected repaired columns, with both the originals and the repairs normalized by the original
    broken-energy norms, the exact Gram matrices of the repairs differ from the exact broken-energy Gram matrices of
    the originals by less than `2.44e-11` and `2.31e-10` in spectral norm at the two section sizes; the stated
    relative comparison is conditional on a certified lower eigenvalue bound, which is not available (section 10, next
    step 1). Also checked by a separate referee review.
  - 10-21 13:04 of three encoded reference densities later used by the numerical team's third Gram version (as
    reconstructed from the checked source), two are of class `C^4` and lie in the diagnostic space, and the radial
    factor of the third has an outer-end value jump strictly between `1.2121e-13` and `1.2122e-13` in absolute value,
    so that density does not (section 10, next step 1). Also checked in two completed referee reviews.
  - 10-21 13:17 under stated regularity hypotheses on the background, the linearized image of a continuous compactly
    supported piecewise-`C^2` density of a finite angular form is `H^1` across a join exactly when all its radial
    first-derivative traces agree there; every join of every selected repaired column fails this, so each selected
    repaired single-mode column has an image outside `H^1_loc` (section 10, next step 1). Also checked by a separate
    referee review.
  - 10-21 13:28 exact `C^{2,1}` repairs of the tested spline columns, with single-column, single-mode relative
    broken-norm errors from the original columns below `1.15e-14` and `3.38e-14`, and relative distances in the
    diagnostic space from the continuous repairs below `1.993e-14` and `5.95e-14`; their images are locally `H^1`
    under the stated background hypotheses (section 10, next step 1). Also checked by a separate referee review.
  - 10-21 13:37 in the graph norm of the diagnostic weighted `H^1`-type space, under explicit background hypotheses,
    every level of the central coefficient is dense, also at fixed strain, so the centre constraint `J = 0` does not
    change the best constant of an inverse estimate there (sections 4 and 10, next step 1). Also checked by a separate
    referee review.
  - 10-21 13:47 for the exactly normalized modal trial the scaling tangent K belongs to an explicit graph domain of
    the diagnostic weighted `H^1`-type norm, with `J(K) = -2`, `c[K] = 0` and nonzero image `L K = eps~ - X.grad eps~`
    (its radial-degree-five sine coefficient at frequency 523 lies in `(-2.4e-11, -2.0e-11)`), so any inverse estimate
    there with `J = 0` and `c = 0` imposed has constant at least `||K||_X / ||L K||_X` (not evaluated then; bounded
    below at 10-22 11:47); K has the nonzero leading far term `(1 - k) r^k Theta` (section 10, next step 1). Also
    checked by a separate referee review.
  - 10-21 13:56 under the exact-profile hypotheses and for the comparison class specified in section 10, next step 1
    (an exact profile with explicit centre and far derivative bounds is assumed, not constructed), no
    residual-to-error modulus controls the distance to that chosen profile in the diagnostic weighted `H^1`-type norm
    at fixed centre coefficient and strain (dilate the profile, then restore the centre coefficient with zero-strain
    compact bumps); this is not a branch exclusion (sections 4 and 10, next step 1). Also checked by a separate
    referee review.
  - 10-21 14:04 under the same background hypotheses, the jump of the linearized image at a join of a continuous
    piecewise-`C^2` density and its term in finite-difference derivative rows are explicit; in a model example one
    derivative jump `1e-14` gives terms of about `9.94e-8` and `1.41e-8`, so a scalar bound on the derivative jumps
    does not by itself bound their row contributions by `1e-11`; and small diagnostic-norm errors do not by themselves
    control collocation rows (section 10, next step 1). Also checked in two completed referee reviews.
  - 10-21 14:10 the quadratic term `W[h].grad h` is not continuous at 0 in the diagnostic weighted `H^1`-type norm
    alone, even on compact densities with `J = c = 0` (four concentrating packets with an exact strain compensator),
    so no quadratic X-to-X estimate holds on any ball about 0 (sections 4 and 10, next step 1). This quadratic
    obstruction concerns X-to-X estimates only. Estimates with h measured in a stronger or graph norm, with the
    quadratic term measured in a weaker norm, or on a specified finite-dimensional class are not covered (for the
    graph norm of 10-21 13:37 see 10-21 23:27). Also checked in two completed referee reviews.
  - 10-21 14:36 a finite audit of all 19389 saved rows of the numerical team's residual derivative certificate: the
    maxima of the saved expressions A and B of section 6 are strictly below 0.4195 and 713.2 (exact rational
    calculation, enclosures by two interval methods); the reported physical derivative bounds remain unverified
    (sections 6 and 8). Also checked in two completed referee reviews.
  - 10-21 15:01 at the 13 sample log-midpoints, conditional on the inherited canonical moment certificates (a
    condition discharged 10-22 00:23), two interval calculations enclose the residual's log-radial derivatives through
    order 5, and the upper ends of the pointwise Wiener sums are at most the 138 saved derivative majorants available
    there; a sample check, not a cell bound (sections 6 and 8). Also checked in completed referee reviews, the last of
    which accepted a correction of its own explanatory algebra.
  - 10-21 15:20 whole-cell upper bounds for the residual's derivative Wiener sums through total order 5 on three
    middle-region cells, one of them containing the source point P (Taylor coefficients through degree 64 by two
    methods, Cauchy tail estimates; inherited canonical inputs, a condition discharged 10-22 00:23); all 63 exceed the
    saved majorants of those cells, so they neither validate nor refute them (sections 6 and 8). Also checked in three
    completed referee reviews.
  - 10-21 15:51 a Bernstein range refinement of the same degree-64 polynomials (eight fixed subintervals per cell,
    exact affine composition and midpoint subdivision, coefficient uncertainty and the same tails) gives whole-cell
    bounds at most all 63 saved derivative majorants of those three cells, which are therefore verified there,
    conditional on the inherited canonical inputs (discharged 10-22 00:23); no other cell, no location of a physical
    maximum and no global forcing norm (sections 6 and 8). Also checked in three completed referee reviews.
  - 10-21 15:53 for the two frozen finite sections of the diagnostic experiment, the exact source-defined matrices of
    the external `C^1` join conditions have full row rank 64 and 96 (determinant and elimination methods in exact
    arithmetic); a statement about these matrices, not about any floating singular value decomposition, retained space
    or spectrum (section 10, next step 1). Also checked in an initial referee review and a completed follow-up review;
    the first prompted a stronger binding to the source code.
  - 10-21 16:10 the second middle-region method completed on all 7809 cells: an independent reconstruction of the cell
    residual models from the density moment ODEs in 160-digit interval arithmetic, with exact integer convolutions and
    Bernstein bounds, an overlap check in every cell of all retained Taylor coefficient enclosures against the first
    method's regenerated models, its own output audit and a complete scalar scan at 220 digits. Every published middle
    value strictly exceeds the corresponding accepted joint bound of the two methods, so the middle-region and
    whole-plane zeroth-order bounds of section 6 rest on two interval methods, which share the canonical density
    moment archive; they were conditional on that archive enclosing the canonical moments of the exact trial, a
    condition discharged by the verification of the archive (10-21 21:13) and of its composition with these bounds
    (10-21 21:34; sections 6 and 8). Also checked in completed referee reviews.
  - 10-21 16:24 the joining of the three regions was repeated with the joint middle cell bounds of the two
    middle-region methods and the unchanged inner and exterior inputs: `N_0 < 1.903991978e-3`, and the four
    whole-plane supremum bounds of section 6 still hold, conditional on the same archive at that time (discharged
    10-21 21:34; section 6). Also checked in completed referee reviews.
  - 10-21 16:29 for the five saved arrays at each section size in the trapezoid-weighted derivative-row form with
    prescribed `C^1` external-join constraints, every external-join row value is exactly nonzero: 64 per vector for
    the smaller section and 96 for the larger. The maximum absolute row values over each family in the unscaled source
    rows are strictly below `1.672e-15` and `3.725e-15` respectively. Each saved array therefore lies outside the
    exact kernel of its corresponding source-defined matrix. This does not imply failure of the tolerance of the
    floating decomposition; the scope qualifications are given in section 10, next step 1. Also checked in a completed
    referee review and a completed follow-up review.
  - 10-21 16:42 the reported share of about 81 percent in the sine frequencies 1 and 3 for the smallest derivative-row
    direction of the larger section is contradicted by the saved profile of that direction, which gives about 87
    percent; about 81 percent is the share of the smallest trapezoid-weighted direction (saved floating values,
    agreeing with a separate floating evaluation on a finite radial interval; section 10, next step 1). Also checked
    in two completed referee reviews.
  - 10-21 16:56 the far expansion of the angular modes of `rho_x` of X3 and its remainder order stated in section 6,
    and the exact identity for the change of the central strain caused by a change of the exterior source of the
    canonical inverse; also the decimal roundings of the recorded maximum values and coordinates in our summary of the
    two saved runs, and the arithmetic of the audited closure-test comparisons of section 6 (the Repetition bullet
    excepted). The evaluator was not rerun, and no residual bound follows (section 6). Also checked in two completed
    referee reviews.
  - 10-21 17:07 analytic formulas for the angular coefficients of the four far powers, and exact strain moments of
    synthetic exterior sources defined by recorded least-squares fits for the tested configurations; these moments do
    not enclose the true exterior source of X3. Separate floating diagnostics show poor relative recovery of the
    subleading coefficients in the tested fits (section 6). Also checked in two completed referee reviews.
  - 10-21 17:12 the exported Green boundary values `A_n`, `B_n` of the trial's canonical inverse at all 7810 exact
    boundaries of the 7809 middle cells, for all 261 modes, contain the canonical values: two interval methods with
    different propagation identities and libraries enclose these values from the shared canonical density moment
    archive (4076820 containment comparisons per method), so the containment holds conditional on that archive
    enclosing the canonical inputs, a condition discharged 10-21 21:54. This is not a second integration of the
    canonical moments; the other inputs of the flow certificate remain open (5(l), section 8). Also checked in referee
    reviews of the proof, the code and the completed results.
  - 10-21 17:35 the saved cells of the numerical team's residual derivative certificate, read exactly, leave gaps
    within their combined hull in `log r`: the middle cells cover their hull, while the inner and outer cells leave
    1968 open gaps between consecutive cells, of total length about `1.1e-12` (two exact methods; for the coherent
    cells intended by the producer see 10-21 19:27; sections 6 and 8). Also checked in a completed referee review.
  - 10-21 17:46 for six preselected saved directions of two intermediate finite sections of section 10, the stored
    value-row and derivative-row quotients are reproduced, with absolute errors below `2e-12`, as exact finite
    functionals of the saved image arrays (two interval methods; the saved images are not certified operator images;
    section 8). Also checked in a completed referee review.
  - 10-21 18:02 for two saved images of source-labelled weakest directions of the angle-refined finite section of
    section 10, the stored energy share of output modes 32 to 39 is below 0.016 percent in each of four row
    functionals, and the ten stored cutoff and stride changes quoted there are recomputed in exact rational
    arithmetic, all nonzero (saved arrays and scalars only; section 8). Also checked in two completed referee reviews.
  - 10-21 18:14 the density polynomial boxes of the flow certificate on all 7809 middle cells (the Taylor coefficients
    at the exact cell left ends of the trial's 260 modal spline amplitudes, eight powers each; 16242720 boxes) contain
    the exact coefficients of the trial (exact rational B-spline arithmetic, and an outward interval reconstruction
    from the shared canonical density moment archive); the density polynomial balls of that archive on all 1558 knot
    spans contain the exact polynomials of the trial (3265568 coefficients, exact rational). The moment values of the
    archive are not covered by this check (they are verified separately, 10-21 21:13; 5(l), sections 6 and 8). Also
    checked in referee reviews of the proof and of the completed results.
  - 10-21 18:45 for the trial's canonical inputs, the radial Taylor models of the three-cell instance (middle cells 0,
    4102, 7808) enclose the canonical modal quantities `P = l psi/r^2` and `R = psi_r/r` of the trial for all 261
    modes on each whole cell, conditional on the shared canonical density moment archive containing the canonical
    scaled moment values in its declared balls, a condition discharged 10-21 21:54 (5(l), section 8). Also checked in
    referee reviews of the proof, the outputs and a follow-up.
  - 10-21 18:54 for the smaller finite section of section 10 at two, four and six collocation points per cell: the
    relative changes of the five smallest stored values of the four row functionals between consecutive densities
    (exact rational arithmetic from the stored binary64 values, two independent codes; all 40 nonzero), the byte
    identity of the selected encoded inputs of the twelve saved runs and the saved retained-column counts; no singular
    value, equality of the retained subspaces or convergence is certified (section 8). Also checked in a referee
    review.
  - 10-21 19:03 for the floating X norms of section 10, next step 1: the analytic jet and norm identities used, exact
    agreement of the code computing the residual mode jets with an independent implementation on synthetic integer
    inputs, and enclosures of the square roots of the stored squared norms; no floating error control on the trial, no
    quadrature error bound and no certified norm (section 8). Also checked in referee reviews of the proof and a
    follow-up.
  - 10-21 19:25 the first attempted full check of the radial Taylor models of the flow certificate stopped at middle
    cell 2955, mode 135, at the constant Taylor coefficient `R_0`. For that coefficient, two exact rational
    calculations, including separate decoding of the original inputs, show that its exact range over the independent
    input boxes lies strictly inside the unchanged candidate ball. The failed sufficient enclosure test therefore does
    not refute this candidate coefficient. This diagnosis certifies no complete cell; at that time the radial Taylor
    models on 7806 of the 7809 middle cells, including cell 2955, remained open (a later complete check covers all
    cells, 10-22 00:16; section 8). Also checked in completed referee reviews.
  - 10-21 19:27 for the numerical team's residual derivative certificate, cells with exact rational starts defined
    from the exact knots of the trial (the coherent cells intended by the producer) cover one closed annulus, about
    `5.155e-5 <= r <= 8.244e10`, without gaps; each exact start lies in the producer's input box for it, each exact
    width is at most the saved width, and the displacement of the saved starts changes the weight by a factor below
    `1.00000000000004`. Hence, if the saved majorants are valid throughout these cells and the residual has the
    regularity stated in section 6, they bound the X norms of the residual and of `eps~ - partial_t eps~` on that
    annulus (verified conditional theorem). The literal saved cells still leave the gaps of 10-21 17:35; the validity
    of the majorants remains open (sections 6 and 8); the two radial end regions outside the annulus are bounded
    separately (10-21 23:48). Also checked in referee reviews and a separate adjudication.
  - 10-21 19:58 under the hypotheses of the 19:27 entry, including the regularity premise of section 6, the X norms on
    the annulus E satisfy `||eps~||_{X(E)} < 0.385656` and `||eps~ - partial_t eps~||_{X(E)} < 585.874` (verified
    conditional theorem; two exact methods bind every saved row and both parameters to the cells, and two interval
    methods enclose the weight correction). The saved majorants remain open (section 6), and the two radial end
    regions outside E are bounded separately (10-21 23:48); the regularity premise holds for the trial (10-21 20:26).
    Also checked in a completed referee review and a separate adjudication.
  - 10-21 20:10 the dependence of the source results of 5(o) on the shared canonical moment archive, as stated in
    section 2 (shared interval archive): the density Hessian bound uses only the verified density polynomial
    enclosures; the point scalars of section 4, the four-point jet constants of section 7, the point values at the
    trial's source and the universal Fourier constants of the whole-plane Sobolev ball are independent of the archive;
    the velocity Hessian bound and the source constants, whole-disc bounds, auxiliary inverse ceilings, moving-source
    radii and Sobolev-ball coefficient and radius derived from it use its moment intervals (dependency audit with
    exact comparison of the inherited scalars; no new enclosure). Also checked in completed referee reviews and a
    separate adjudication.
  - 10-21 20:15 for the projection diagnostics of the smaller finite section of section 10, next step 1 (saved
    floating energies of the numerical team): the identity `||v - P v|| / ||v|| = (1 - ||P v||^2 / ||v||^2)^{1/2}` for
    a nonzero vector v and an exact orthogonal projection P in a Hilbert space, and outward enclosures of
    `100 (1 - E_proj / E_K)^{1/2}` for the saved energies read as exact dyadic numbers: `(1.81776, 1.81779)` for `C^1`
    joins, `(1.81764, 1.81766)` for `C^0` joins and `(1.76198, 1.76201)` with the free tail columns (in percent). The
    earlier reading of 99.5 percent captured energy as a distance of 0.5 percent is refuted (the identity gives about
    7.07 percent), and four earlier saved full-energy ratios exceed 1, so they cannot describe exact orthogonal
    projections in one Hilbert norm. These are intervals for arithmetic on saved floating numbers; no Gram matrix,
    projection, operator image or norm is certified. Also checked in a completed referee review and a separate
    adjudication.
  - 10-21 20:26 for the exactly joined and exactly normalized finite modal trial, the following statements hold on the
    punctured plane: the density is `C^6`, the canonical stream function is `C^7`, the velocity is `C^6` and the
    residual is `C^5`. In log-polar variables, `eps~ - partial_t eps~` is `C^4`. Every possibly nonzero odd sine
    coefficient of the residual (there are finitely many) is `C^5` in `t = log r` on the whole real line, including
    every spline knot and both radial joins. Thus the regularity premise in section 6 holds for this trial. The proof
    uses the B-spline derivative identity at simple knots, exact matching of derivatives of orders 0 through 6 at the
    two radial joins, and the convergent canonical Green integrals and their moment ODEs, with stream prefactor
    `r^4/2`. Two exact computations check all endpoint derivatives and joining corrections. These regularity
    statements hold for every finite real coefficient of the normalization correction, with the same exact joins;
    exact normalization selects the trial's coefficient. No numerical moment value or numerical enclosure of this
    coefficient is used in the regularity proof. The result does not certify the stored rounded joining coefficients,
    the saved derivative majorants or any radial tail bound. Also checked in completed referee reviews and a separate
    adjudication.
  - 10-21 21:03 the angular arrays of the numerical team's flow certificate on all cells: as regenerated from the
    frozen certificate source, every coefficient box of all 51000 angular cells of depth at most 7 (the value and the
    first two Taylor coefficients at the cell centre, for the three families of angular mode factors and all 261
    modes; 119799000 boxes) contains the exact coefficient, and the endpoint, outward angle and half-width outputs of
    every cell are valid. Methods: two interval engines of different implementations, a complete replay of every box
    at higher precision, and exact rational checks of all 102000 endpoint memberships, all 51000 half-widths and the
    4176 finite remainder inequalities; the 221 centres checked earlier agree. The identity of the regenerated arrays
    with those of the historical numerical run is not established; the radial models, the products, the coverage of
    the region and the cell field inequalities are not covered (section 8). Also checked in a completed referee review
    and a separate adjudication.
  - 10-21 21:13 the shared canonical density moment archive, by a second complete propagation method: on all 1558 knot
    spans, all 3265568 density polynomial coefficients and all 813276 boundary moments (the exponentially weighted
    integrals of the density modes over the inner and outer half-lines in `t = log r` from which the canonical stream
    modes are formed, 261 modes) lie in their unchanged archived intervals, for the exactly normalized trial. The
    method reconstructs the spline and angular coefficients exactly, evaluates the complete inner and outer tail
    integrals by exact analytic formulas (including the normalization correction, whose coefficient is carried
    affinely and enclosed in the accepted interval), and propagates forward and backward by an exact
    particular-solution identity in 200-digit interval arithmetic, different from the exponential-moment recurrence of
    the original archive; no archived moment is used as an input. A separate exact audit checks every saved output and
    all analytic anchors. This validates the archive itself. Applying it to a conclusion that is conditional on the
    archive requires a composition checking that the conclusion uses exactly these intervals (10-21 21:21, 10-21 21:34
    and 10-21 21:54 below; section 2, shared interval archive). Also checked in a completed referee review and a
    separate adjudication.
  - 10-21 21:13 for the assembled-image comparison of section 10, next step 1 (saved arrays of the numerical team):
    the exact sum, in two exact implementations, of the 42 saved partial image arrays, whose saved input-mode ranges
    partition `0 <= m < 260` (467 radii and 40 output modes; all 18680 entries), its entrywise comparison with the
    saved assembled and direct arrays, and enclosures of the four discrete row functionals by two outward interval
    methods. For the exact sum S and the direct image D the ratios `F(S - D)/F(D)` are about `5.365e-5`, `4.185e-5`,
    `5.788e-5` and `4.953e-5` (unweighted and trapezoid-weighted value rows, unweighted and trapezoid-weighted
    derivative rows); the saved assembled array differs from S by less than `7.11e-15` entrywise and by less than
    `1.032e-11` relative to D in each of the four row functionals. Nine proposed agreement tolerances with saved
    summary values fail and are retained as failures; only the coarse comparison and the stated discrepancy bounds are
    confirmed. No mode image is reassembled, and no continuous norm, quadrature or tail error, physical scaling image
    or projection is certified. Also checked in a completed referee review and a separate adjudication.
  - 10-21 21:21 the composition of the archive verification of 10-21 21:13 with the source results of 5(o): the seven
    archive span records copied into the source derivative calculations are exactly equal to the corresponding records
    of the archive, all 3654 moment boxes used there are checked by two exact endpoint methods, and the verification
    is bound to the same archive, exact trial and normalization interval. Hence the canonical moment condition holds
    for the exactly normalized trial and is discharged, by substitution in the accepted source theorems, for
    `M_V < 0.2972` and the quantities derived from it (the source constants, the variation of `DV` on the source disc
    and the source cutoff sign, the auxiliary inverse ceilings, the moving-source radii, the Sobolev-ball coefficient
    and radius, and the `K_1` bounds of 5(o)). All other hypotheses are unchanged, and the auxiliary inverse ceilings
    remain bounds for an auxiliary inverse only. Also checked in completed referee reviews and a separate
    adjudication.
  - 10-21 21:34 the composition of the same archive verification with the zeroth-order residual certificates of
    section 6: both middle-region methods, the inner and exterior certificates (which use the archived boundary
    moments of the first and the last knot span, through exact propagation identities across these spans) and both
    whole-plane joinings use exactly the archived intervals, for the exactly normalized trial. The checked dependency
    chains include the archived boundary moments used by the earlier inner and exterior majorants of section 6, whose
    velocity remainder and coefficient bounds the end-region X norms of 10-21 23:48 inherit. The checks rehash all
    1558 archive span records and the geometry records for all 7809 middle cells, decode the 4192 density coefficient
    balls and 1044 moment balls in the first and last span records by two exact methods, bind the 31 checked input
    dependencies to their accepted sources, and verify all 17748 exterior particular-solution identities by exact
    forward substitution in two arithmetic implementations. They also separately recompute the sums of regional
    squared norm bounds and the maxima of regional supremum bounds, with two interval square-root checks. The verified
    archive premise is applied separately to each accepted regional certificate and to each of the two accepted
    whole-plane joinings. For the distinguished exactly normalized trial, this discharges only the archive condition
    for their zeroth-order residual bounds, with unchanged values, other hypotheses and evidence qualifications. No
    regional enclosure computation was rerun. The Green boundary values and the radial models of the flow certificate
    are not covered by this composition (10-21 21:54; 5(l)). Also checked in a completed referee review and a separate
    adjudication.
  - 10-21 21:44 for the stored modal trial (without the exact joins and normalization) and the stored column recipe of
    the smaller finite section of section 10, next step 1: the scaling tangent of that trial lies outside a class of
    functions with a lower-growth part and two prescribed leading tails that contains the span of the section's
    columns (statement in section 10, next step 1). The proof uses the leading limit, the linear independence of the
    angular modes and a nonzero 2 x 2 coefficient minor, an exact rational in
    `(5.859714460078e-15, 5.859714460080e-15)` (exact rational arithmetic in two implementations and two interval
    evaluations), both for `k - 3` and for its binary64 value used by the stored recipe. The class with additional
    free leading tail columns, norm closures, distances, image estimates and the exactly normalized trial are not
    covered (for the exactly normalized trial see 10-21 23:14). Also checked in a completed referee review and a
    separate adjudication.
  - 10-21 21:54 the composition of the archive verification of 10-21 21:13 with the Green boundary values of 10-21
    17:12 and with the three-cell radial models of 10-21 18:45: for the distinguished exactly normalized trial, both
    results use exactly the archived intervals. The checks rederive the identities connecting the canonical moments
    with the Green boundary values and with the radial quantities P and R in two exact arithmetic implementations
    (9396 scalar coefficients each, all 261 modes), check the exact normalization corrections, match all 1558 archive
    span records and all 7810 cell boundaries, check the exact zero entries of the highest mode on every span, and
    recheck the coordinates, lengths and exponential targets of the three cells. Hence the archive condition is
    discharged for the containment of the canonical Green boundary values at all 7810 boundaries and for the
    three-cell radial models, with all other hypotheses and qualifications unchanged. No complete Green boundary or
    radial Taylor-model enclosure computation was rerun. The radial models of the other 7806 middle cells, the
    derivative majorants of section 6 with their inherited canonical moment certificates and the full flow certificate
    are not covered (the first two are covered later, 10-22 00:18 and 10-22 00:23). Also checked in a completed
    referee review and a separate adjudication.
  - 10-21 22:59 the canonical flow ranges on the nine rectangles of 10-21 11:35: for the distinguished exactly
    normalized trial, on the nine closed polar rectangles formed by the middle cells 0, 4102 and 7808 and the angular
    cells `[0, pi/51200]`, `[pi/4, pi/4 + pi/51200]` and `[pi/2 - pi/51200, pi/2]`, the canonical flow fields
    `s = X.V/r^2`, `v_2 = V_2/y`, `v_1 = V_1/x` and T, with the axis quotients taken as their continuous extensions,
    lie in the 36 ranges reported by the certificate. The three-cell radial result (10-21 18:45, with its archive
    condition discharged at 10-21 21:54) supplies the canonical radial inputs, the angular and scalar inputs are
    matched exactly with their verified sources, and the verified enclosures of the composition are applied unchanged.
    The checks decode all 66 packet arrays (91836 entries) by two methods, verify 21 radial and 45 angular array
    identities with the verified sources and 522 Chebyshev and cosine-sum polynomial identities, re-evaluate all 7047
    cubic remainder inequalities in two exact rational implementations, check the directed radial and angular geometry
    by two interval engines, and check that the 72 saved reference enclosures lie in their 36 target ranges. The modal
    products of the composition were not recomputed. All other hypotheses, including those of the runtime degree-12
    radial models with their order-20 remainder refinement, are unchanged; identity with the arrays of the historical
    numerical flow computation, any angular or annular cover beyond these rectangles and the full flow certificate are
    not covered. Also checked in a completed referee review and a separate adjudication.
  - 10-21 23:14 for the exactly joined and exactly normalized trial and the stored column recipe of the smaller finite
    section of section 10, next step 1: its scaling tangent lies outside two classes, each with a lower part of
    strictly lower polynomial-exponential rates and two prescribed leading tails, one with the exact rate `k - 3` and
    one with the recipe's binary64 rate; the span of the section's columns lies in the first or the second according
    to the reading of the recipe's tail rate (statement in section 10, next step 1). The proof uses the leading limit,
    the linear independence of the angular modes, the determinant `(A_0 + z) B_1 - A_1 B_0`, strictly between
    `5.859714459e-15` and `5.859714461e-15` for every z in the certified normalization interval (exact endpoint values
    in two rational implementations and two interval enclosures), and the exact rate gap. The class with additional
    free leading tail columns, norm closures, distances and image estimates are not covered. Also checked in a
    completed referee review and a separate adjudication.
  - 10-21 23:27 in the graph norm `||h||_X + ||L h||_X` of the diagnostic weighted `H^1`-type space, under the
    background hypotheses of 10-21 13:37 and the additional hypotheses that the transport field `V = c_l X + U[rho]`
    is locally `C^1` and vanishes at a point `P = (p, 0)` with `p > 4`, the quadratic term `W[h].grad h` is not
    continuous at 0, even on compact densities with `J = c = 0`: two translated packets at P and -P with an exact
    strain compensator have graph norm tending to 0, while the squared X norms of their quadratic images have limit
    inferior at least `p^2 w(p) E_H > 0`, with w the weight of X and `E_H` the positive gradient energy of 10-21
    14:10. The exactly normalized modal trial is an instance, with P its source (5(o)). Stronger Sobolev graph norms,
    the norms of the proposed realization, a weaker image norm and restricted finite-dimensional classes are not
    covered (section 10, next step 1). Also checked in two completed referee reviews and separate adjudications.
  - 10-21 23:48 for the exactly joined and exactly normalized trial, the X norms on the two radial end regions outside
    the annulus E of 10-21 19:58, each with the integration restricted to the region: on `r <= exp(b_- - 5)`,
    `||eps~||_X < 0.000002273735` and `||eps~ - partial_t eps~||_X < 0.000035059554`; on `r >= exp(b_+ + 17)`,
    `||eps~||_X < 0.000003926908` and `||eps~ - partial_t eps~||_X < 0.000006445150` (verified; own proof from the
    exact inner density expansion with the velocity remainder bounds of the earlier analytic inner majorant and the
    exact exterior expansion with the coefficient bounds of the earlier coarse exterior majorant of section 6, two
    exact reconstructions of all exterior coefficient bounds and two interval evaluations of all weighted radial
    integrals; section 6). Under the unverified majorant hypotheses of 10-21 19:58 on E the squared norms add, giving
    the full-plane bounds `||eps~||_X < 0.385656000027` and `||eps~ - partial_t eps~||_X < 585.874000000002` (verified
    conditional composition). Also checked in two completed referee reviews and separate adjudications.
  - 10-22 00:16 the radial Taylor models of the flow certificate on all 7809 middle cells, for all 261 modes, as a
    finite-input statement: for every choice of the inputs in their finite boxes, the runtime degree-12 models with
    their remainder budgets enclose the solutions of the radial modal equations on each whole cell. Two complete
    interval methods with different constructions each passed all 52991874 coefficient and 4076298 remainder
    containments, all 16305192 forcing coefficients were checked exactly against their images, and an independent
    output audit checked selected modes on every cell by a third method, with five complete replay cells. The first
    and third methods each needed an independently computed exact endpoint refinement at the same twelve constant
    coefficients `R_0`, with no change of target or remainder budget; the second method needed none. The check was
    rerun from the first cell after the stopped attempt of 10-21 19:25 (5(l), section 8). Also checked in a completed
    referee review and a separate adjudication.
  - 10-22 00:18 the canonical meaning of these models on all 7809 middle cells: for the distinguished exactly
    normalized trial, the canonical `P = l psi/r^2` and `R = psi_r/r` lie in the models of 10-22 00:16 on every closed
    middle cell for all 261 modes. The input boxes contain the canonical inputs by the verified Green boundary values
    (10-21 17:12, archive condition discharged 10-21 21:54) and density coefficients (10-21 18:14); a complete exact
    reader identifies every input array and cell record of the computation with these sources, two exact constructions
    check the forcing weights and the radial equations, and uniqueness for the linear modal equations identifies the
    canonical quantities with the enclosed solutions. No angular product, flow inequality, physical derivative bound
    or endpoint follows (5(l), section 8). Also checked in a completed referee review and a separate adjudication.
  - 10-22 00:23 the inherited canonical centre-moment certificates of the derivative checks of 10-21 15:01, 15:20 and
    15:51: a second integration of the canonical moment equations by a different method (exact particular polynomials
    of the spline pieces on all 1558 knot spans in each direction, outward interval exponentials, and exact analytic
    anchors that include the complete inner and outer tails) shows that all 6786 moment intervals at the 13 sample
    log-midpoints contain the canonical moments of the exactly normalized trial and that all 27248 local density
    coefficient intervals there contain its exact coefficients; an independent exact audit rereads every saved
    interval and reconstructs all 783 anchors. This discharges the inherited condition of the 13-point check and of
    the three-cell bounds and majorants (cells 4102, 4125 and 4211), with their other hypotheses unchanged; no other
    cell and no global derivative bound is covered (sections 6 and 8). Also checked in a completed referee review and
    a separate adjudication.
  - 10-22 02:07 in the diagnostic weighted `H^1`-type norm X of section 10, next step 1, at the exactly normalized
    modal trial: there are smooth compactly supported densities h_j of the required parities, vanishing near the
    centre, with `J(h_j) = c[h_j] = 0`, `||h_j||_X = 1` and `||L h_j||_X -> 0` (centre quasimodes, section 5(p)).
    Hence no finite C gives `||h||_X <= C ||L h||_X` on any perturbation domain containing them, in particular on the
    graph domain of 10-21 13:47 and on its subspace with `J = 0` and `c = 0`; as an obstruction this supersedes the
    lower bound `||K||_X / ||L K||_X` of 10-21 13:47. This is not an exact kernel, it concerns X on both sides only,
    and it says nothing about the existence of a profile. Also checked in two completed referee reviews and a separate
    adjudication.
  - 10-22 02:12 the sequence of 10-22 02:07 can be chosen small in `H^{5/2}`, supported in `r <= 2` and weakly null in
    X. Hence, on any domain containing it, no estimate `||h||_X <= C (||L h||_X + ||h||_{H^{5/2}})` holds, nor one
    with a compact remainder; every bounded linear `B: X -> X` has `sup ||h - B L h||_X >= 1` over unit vectors; and
    every closed realization of L in X containing the sequence fails to have both closed range and finite-dimensional
    kernel, so it is not Fredholm (section 5(p)). Which of the two fails is not determined, and other norms are not
    covered. Also checked in two completed referee reviews and a separate adjudication.
  - 10-22 02:23 for every fixed integer `m >= 2`, the conclusions of 10-22 02:07 and 02:12 also hold in the
    first-order norm `X_m` with the more singular centre weight `w_m = L^{2m+2} r^{-2m-2} (1 + r^2/L^2)^{m-k-1/2}`
    (`X_2 = X`), for a sequence whose velocity Taylor coefficients of degree at most `m - 2` at the centre also vanish
    (section 5(p)); the constants are not uniform in m. Also checked in completed referee reviews and a separate
    adjudication.
  - 10-22 02:37 the stored coefficient representation of the modal trial, from which the floating-point diagnostics
    are computed, is discontinuous across both radial joins and not in `H^1_loc` there; the open-region scaling
    identity for its piecewise scaling tangent contains an interface term and a strain term (the strain is positive,
    with a certified enclosure of order `4.5e-18`; the sum of the two terms has not been proved nonzero; section 10,
    next step 1). This concerns the stored representation only; for the exactly joined trial rho~ the identity is
    exact. Also checked in a completed referee review, a separate adjudication and a separate referee audit.
  - 10-22 02:44 the constraints `J = c = 0` alone do not keep the image of L in the norms `X_m` with `m >= 5`: at
    backgrounds with the finite-regularity hypotheses of section 5(p) (among them the exactly joined trial), the
    smooth density `r^4 eta(r) (sin 5 theta + sin 7 theta)` with `J = c = 0` lies in every `X_m`, while its image is
    `2 (x^4 y + 5 x^2 y^3) + O(r^7)` near the centre and lies in `X_2`, `X_3`, `X_4` and in no `X_m` with `m >= 5`.
    The sequences of 10-22 02:23 are not affected. Also checked in two completed referee reviews, a separate
    adjudication and a separate referee audit.
  - 10-22 02:45 in the axis-weighted logarithmic norm `Y_(a,s)` of section 5(q) the frozen centre transport is closed
    on its maximal domain and, when `delta_Y = D(s - 1/2) - A(a - 1/2) - 1 < 0` (with `A = 2 c_l - 1` and
    `D = 4 c_l - 1`), bijective with inverse norm at most `1/|delta_Y|`; at the exactly normalized trial and
    `(a, s) = (6, 153/50)` this bound is below 0.435298231926. This concerns the frozen operator only. Also checked in
    a completed referee review, a separate adjudication and a separate referee audit.
  - 10-22 02:49 for `a >= 5/2` and every `s >= 0` the full linearization, at backgrounds satisfying the local
    hypotheses of section 5(q) (among them the exactly joined trial), maps a smooth compactly supported density with
    `J = c = 0`, supported in `1 < r < 2` away from both axes and lying in every `Y_(a,s)`, outside `Y_(a,s)` (section
    5(q)). An inverse on a smaller domain is not excluded. Also checked in a completed referee review, a separate
    adjudication and a separate referee audit.
  - 10-22 02:57 on the smooth compact densities with `c = 0` supported in `1 < r < 2` away from both axes, for
    `a >= 5/2` and `s = 153/50`, membership of the image in `Y_(a,s)` is equivalent to the vanishing of every interior
    even harmonic moment; the compatible subspace is infinite-dimensional and has infinite algebraic codimension, so
    no subspace of finite codimension is mapped into `Y_(a,s)` (section 5(q)). No inverse on the compatible subspace
    is proved. Also checked in a completed referee review, a separate adjudication and a separate referee audit.
  - 10-22 03:08 the density of 10-22 02:49 is not mapped by L into the quadrant norms of the weighted saddle model of
    section 5(e) with `a >= 5/2`, for every real b and every number of Euler derivatives, in particular at its revised
    working point. Also checked in a completed referee review, a separate adjudication and a separate referee audit.
  - 10-22 03:13 the residual of the exactly joined trial satisfies `eps~_xx(0, y)/2 = Q y^3 + o(y^3)` on the y-axis
    with `6.087210e-6 < Q < 6.087213e-6` (two interval evaluations, by different algorithms, of scalars given in exact
    form), so, for `a >= 5/2`, it lies in no `Y_(a,s)` and in no quadrant norm of section 5(e) (section 5(q)). This
    concerns these forcing spaces for one trial. Also checked in two completed referee reviews, a separate
    adjudication and a separate referee audit.
  - 10-22 03:20 for the frozen centre transport, all weights of `Y_(a,s)` with `delta_Y < 0` at a given order s have
    `a > 5/2` exactly when `s >= 3/2` (at `s = 153/50` the threshold is about 5.7736836), and all weights of the
    quadrant norms of section 5(e) with `delta < 0` at a given b exactly when `b >= 3/2`; `delta < 0` is sufficient,
    not necessary, for invertibility. Also checked in a completed referee review, a separate adjudication and a
    separate referee audit.
  - 10-22 03:28 for the frozen centre transport in `Y_(a,s)` the spectrum is the strip
    `delta_- <= Re lambda <= delta_Y`, where `delta_- = -A a - (A + 3)/2`, and has no eigenvalues; `T_0` is invertible
    exactly when 0 lies outside `[delta_-, delta_Y]`, with inverse norm `1/dist(0, [delta_-, delta_Y])`, and is not
    Fredholm otherwise; for `a >= 0` it is invertible exactly when `delta_Y < 0` (section 5(q)). This concerns the
    frozen operator only. Also checked in a completed referee review with a follow-up exchange, a separate
    adjudication and a separate referee audit.
  - 10-22 03:39 inside the strip `delta_- < 0 < delta_Y` the frozen centre transport in `Y_(a,s)` has closed range of
    infinite codimension, cut out by Mellin moment conditions, and on its range a bounded inverse with the explicit
    norm bound of section 5(q) (the norm is exactly `k/(1 + k)`, about 0.15208, at `(a, s) = (0, 153/50)`; section
    5(q)). This concerns the frozen operator only. Also checked in a completed referee review with two follow-up
    exchanges, a separate adjudication and a separate referee audit.
  - 10-22 03:57 for `s = 153/50` and every real a, no closed linear realization of the linearization in `Y_(a,s)` has
    a domain containing the maximal domain of the frozen centre transport: compact potentials near the source give
    densities with compact velocities, bounded frozen graph norm and images in `Y_(a,s)` of norm tending to infinity
    (section 5(q)). This concerns the choice of domain only. Also checked in two completed referee reviews, a separate
    adjudication and a separate referee audit.
  - 10-22 04:08 the Mellin moments that cut out the range of the frozen centre transport inside the strip form a
    bounded map from `Y_(a,s)` onto a weighted `L^2` space in the Fourier variable `xi_z` dual to `z = log x`, with
    exact norm `sqrt N`, `N = Gamma(u/D) Gamma(v/D)/(2 Gamma(s))`, where `u = -delta_-`, `v = delta_Y` and Gamma is
    Euler's gamma function (`N` is about 1.10492 at `(a, s) = (0, 153/50)`), and the unweighted bound holds with the
    same norm (section 5(q)). This concerns the frozen operator only. Also checked in a completed referee review with
    a follow-up exchange, a separate adjudication and a separate referee audit.
  - 10-22 04:20 the regional bounds and relative changes of the fit-stability comparison of section 6 follow from the
    saved cell rows of the trial and its three variants; they are changes of upper bounds, conditional on the saved
    per-cell bounds, on coverage and on the reconstruction of the variants, and the displayed radial ranges are
    approximate labels. Also checked in a completed referee review with a follow-up exchange and a separate
    adjudication.
  - 10-22 04:28 for `s = 153/50` and `0 <= a < 5/2` the linearization at the exactly joined trial maps every smooth
    compact density of the required parities with `c = 0` supported away from both axes into `Y_(a,s)`; with 10-22
    02:49, among `a >= 0` the bound `a < 5/2` is exact for the inclusion of the image of the annular class `T_ann,0`
    (the smooth densities of the required parities with `c = 0` supported in `1 < r < 2` at positive distance from
    both axes; section 5(q)). This is setwise; no operator norm estimate is asserted. Also checked in a completed
    referee review with a follow-up exchange, a separate adjudication and a separate referee audit.
  - 10-22 04:41 for `s = 153/50` and `a >= 0` the residual of the exactly joined trial lies in `Y_(a,s)` exactly when
    `2k < a < 5/2`; the lower endpoint comes from a nonzero `sin 3 theta` coefficient of its `r^{2k-1}` tail, the
    upper from the axis coefficient Q (section 5(q)). This is qualitative; no norm bound is asserted, and at these
    weights the frozen centre transport is not Fredholm. Also checked in three completed referee reviews, a separate
    adjudication and a separate referee audit.
  - 10-22 04:50 the strain functional c extends to a bounded linear functional on `Y_(a,s)` for `s >= 0`,
    `0 <= a < 2`, `s + a > 2`, with an explicit upper bound for its norm (below 0.263445900665 at
    `(a, s) = (3/2, 153/50)`), and is unbounded for `a >= 2` (section 5(q)). This concerns one functional; no domain
    or inverse of L follows. Also checked in two completed referee reviews, a separate adjudication and a separate
    referee audit.
  - 10-22 04:57 the weak-weight mapping of 10-22 04:28 holds for `0 <= a < 5/2` and every order `0 <= s < 6 - a`; for
    each `0 <= s <= 7/2` the bound `a < 5/2` is exact for the inclusion of the image of `T_ann,0` (section 5(q)). This
    is setwise; no operator norm estimate is asserted. Also checked in three completed referee reviews, a separate
    adjudication and a separate referee audit.
  - 10-22 05:05 for `s = 153/50` and `a >= 0` the trial and `X.grad rho~` lie in `Y_(a,s)` exactly when
    `1 + k < a < 5/2`, the scaling term `(c[h]/3) X.grad rho~` of L is bounded on `Y_(a,s)` exactly when
    `1 + k < a < 2` (then of rank one and compact), and L maps every smooth compact density of the required parities
    supported away from both axes into `Y_(a,s)` exactly when `1 + k < a < 5/2` (section 5(q)). This is qualitative;
    no norm of the trial or of the scaling term is computed. Also checked in three completed referee reviews, a
    separate adjudication and a separate referee audit.
  - 10-22 05:16 for every real `a < 5/2` and every finite `s >= 0` the centre trace J is not closable on the smooth
    compact densities of the required parities with `c = 0` and smooth even-even factor `h/(x^2 y)` in `Y_(a,s)` or in
    the frozen graph norm: compact densities equal to `x^2 y` near 0 tend to 0 in both norms (section 5(q)). For the
    graph norm of L see the entry 10-22 05:31. Also checked in four completed referee reviews, a separate adjudication
    and a separate referee audit.
  - 10-22 05:31 for every real `a < 5/2` and every `0 <= s < 4` the same densities also satisfy
    `||h_delta||_Y + ||L h_delta||_Y -> 0`, so J is not closable in the graph norm of L on the smooth compact
    strain-zero densities with smooth even-even factor `h/(x^2 y)` and image in `Y_(a,s)` (section 5(q)). This gives
    neither closedness nor an inverse of L, no numerical bound for the constant `C_graph(a,s)` of the graph estimate,
    and nothing at `s >= 4`. Also checked in four completed referee reviews, a separate adjudication and a separate
    referee audit.
  - 10-22 05:40 for every real a and finite `s >= 0` the quadratic term `W[h].grad h` is not continuous at 0 from the
    graph norm of L at the exactly joined trial into `Y_(a,s)`, on the compact-potential class of 5(q) (supported away
    from both axes, `J = c = 0`, all centre jets zero); no quadratic bound holds on the intersection of that class
    with any graph ball about 0 (section 5(q)). Stronger domain norms, weaker image norms and scales of spaces are not
    covered. Also checked in three completed referee reviews, a separate adjudication and a separate referee audit.
  - 10-22 05:48 at the exactly joined trial, for every real `a < 5/2` and `0 <= s < 4`, on the strain-zero test class
    of 5(q), the best constant in `||h||_Y <= C ||L h||_Y` is the same with and without the centre normalization
    `J = 0` (finiteness is not shown); for every real a and finite `s >= 0` the quadratic discontinuity of 10-22 05:40
    persists in the kernel of finitely many graph-continuous linear constraints (section 5(q)). Also checked in two
    completed referee reviews, a separate adjudication and a separate referee audit.
  - 10-22 05:57 for every real a and finite `s >= 0` the quadratic discontinuity of 10-22 05:40 persists on every
    linear subspace of the compact-potential class of 5(q) of finite algebraic codimension, closed or not (any
    finitely many linear constraints, without continuity; section 5(q)). Infinitely many or nonlinear constraints,
    stronger domain norms and weaker image norms are not covered. Also checked in three completed referee reviews, a
    separate adjudication and a separate referee audit.
  - 10-22 06:07 for every real a and finite `s >= 0` the quadratic discontinuity of 10-22 05:40 persists on the zero
    set near 0 of any finitely many constraints on the compact-potential class of 5(q) that vanish at 0, are
    continuously Frechet differentiable in the graph norm of L and have onto derivative at 0 (section 5(q)). Singular
    or infinitely many constraints, stronger domain norms and weaker image norms are not covered. Also checked in two
    completed referee reviews, a separate adjudication and a separate referee audit.
  - 10-22 06:18 preliminary audit of the text of the draft of 10-22 06:12 by the verifier: the item on the quadratic
    term in 5(q) is consistent with the verified results at its stated scope (section 8); not a verification of a new
    result.
  - 10-22 06:42 preliminary audit of the text of the same draft by the verifier: section 1 and 26 results of this
    timeline are consistent with the accepted results at their stated scope (section 8); not a verification of a new
    result.
  - 10-22 07:07 audit of the text of the draft of 10-22 06:58 by the verifier: the section 1 wording on the four jet
    values and the moving-source hypotheses, and the record of the two preceding audits, match those audits (section
    8); not a verification of a new result.
  - 10-22 08:22 audit of the text of 5(h) of the draft of 10-22 07:23 by the verifier: the family wording is
    consistent with the verified proof for fixed far corrections; two clarifications adopted (section 8); not a
    verification of a new result.
  - 10-22 08:49 for the exactly normalized modal trial, the X norms of the residual and of `eps~ - partial_t eps~` on
    the whole plane without the majorant hypotheses of 10-21 19:58: `||eps~||_X < 245653983.313885102003858` and
    `||eps~ - partial_t eps~||_X < 30665526224.2484290248531` (verified; own proof, section 6; the computation was
    verified at 08:42 and the regional squares with the sum of their displayed values at 08:49). On the 7809 middle
    cells the velocity derivatives are obtained from the Green ODEs applied to the radial models of 10-22 00:16 and
    00:18, so that no remainder bound is differentiated, and all polynomial products of the Leibniz expansion are
    computed on every cell by two exact methods compared on every coefficient; the inner disc `r <= exp(b_-)` and the
    exterior `r >= exp(b_+)` are bounded from the exact inner expansion and the exterior coefficient majorants
    underlying 10-21 23:48, now integrated over these larger regions. The squared norms on the middle annulus
    `b_- <= log r <= b_+`, the inner disc and the exterior are at most 2.23642149354638943132127,
    67.9898116895358306437308 and 60345879517978469.8955085 for the residual and 6074661.94639141300035166,
    16132.4321701281783711136 and 940374498610062020934.552 for `eps~ - partial_t eps~`. The exterior term dominates,
    so these bounds are far larger than the conditional bounds of 10-21 23:48, which remain conditional, and no saved
    majorant of 10-21 19:58 is verified by them. Also checked in a completed referee review of the computation
    followed by a separate adjudication, and in a completed referee review of the regional composition with a
    corrective follow-up, followed by a separate adjudication.
  - 10-22 09:35 in the weighted factor supremum norm of the axis control, on continuous factors vanishing at 0 and at
    infinity, the linearization at the exactly normalized modal trial has unit weak-null quasimodes: smooth compactly
    supported densities vanishing near the centre, with zero strain and images tending to 0 (section 5(r)). So no
    same-norm inverse estimate holds on a domain containing them, none with a bounded linear compact remainder, and no
    closed linear realization in that space containing them is Fredholm. Hoelder or derivative norms of the factor,
    stronger domain norms and weaker target norms are not covered. Also checked in four completed referee reviews, two
    of them follow-ups, three separate adjudications and a separate referee audit.
  - 10-22 10:22 for the exactly normalized modal trial, sharper direct whole-plane bounds:
    `||eps~||_X < 8.38010956871949018314234` and `||eps~ - partial_t eps~||_X < 2467.95347982509225629694` (verified;
    own proof, section 6; the exterior computation was verified at 10:18 and the composition at 10:22). The exterior
    `r >= exp(b_+)` is divided at `log r = b_+ + 17`: on 89 cells covering `b_+ <= log r <= b_+ + 17` the derivatives
    of the exact exterior expansion are bounded through Taylor polynomials with analytic derivative remainders, the
    residual polynomial is formed before absolute values by two methods compared on every coefficient, and Bernstein
    bounds give whole-cell Wiener bounds; beyond `b_+ + 17` the end-region bounds of 10-21 23:48 are used. The squared
    exterior norms are at most 0.00000320066173968513189015735 and 0.0000192408718059828130775364; the middle and
    inner squares of 10-22 08:49 are unchanged, and the inner disc term dominates for `eps~` and the middle annulus
    term for `eps~ - partial_t eps~`. These bounds are still larger than the conditional bounds of 10-21 23:48, which
    remain conditional, and no saved majorant of 10-21 19:58 is verified by them. Also checked in a completed referee
    review of the exterior computation and one of the composition, each with a corrective follow-up and each followed
    by a separate adjudication.
  - 10-22 10:51 audit of the text of the draft of 10-22 10:32 by the verifier: section 1, read afresh in full, and
    every change since the draft of 10-22 07:23, including every displayed decimal they contain, are consistent with
    the verified results at their stated scope, with no required correction (section 8); not a verification of a new
    result.
  - 10-22 11:31 for the exactly normalized modal trial, sharper direct whole-plane bounds:
    `||eps~||_X < 1.49546805188731021373656` and `||eps~ - partial_t eps~||_X < 2464.68293019825564964515` (verified;
    own proof, section 6; the inner computation was verified at 11:20 and the composition at 11:31). The inner disc
    `r <= exp(b_-)` is divided at `log r = b_- - 5`: on 44 cells covering `b_- - 5 <= log r <= b_-` the canonical
    velocity modes, with the exact central strain subtracted, are obtained from their Green ODEs as Taylor polynomials
    with derivative errors from the exact ODE defect, and independently from a second pair of Green ODEs forced by the
    density modes; the residual polynomial is formed before absolute values by two methods compared on every
    coefficient, and Bernstein bounds give whole-cell Wiener bounds; below `b_- - 5` the end-region bounds of 10-21
    23:48 are used. The squared inner-disc norms are at most 0.00000000000749763727216539889936543 and
    0.00000000565879455607782317925245; the middle squares of 10-22 08:49 and the exterior squares of 10-22 10:22 are
    unchanged, and the middle annulus term dominates for both. These bounds are still larger than the conditional
    bounds of 10-21 23:48, which remain conditional, and no saved majorant of 10-21 19:58 is verified by them. Also
    checked in a completed referee review of the inner computation and one of the composition, each with a follow-up
    exchange and each followed by a separate adjudication.
  - 10-22 11:47 for the exactly normalized modal trial, a strict lower bound `||K||_X > 170.953964620623929217261` for
    the scaling tangent `K = rho~ - X.grad rho~` (verified; own proof). On the annuli of three whole knot spans of the
    middle region, with disjoint interiors, K and `X.grad K` are exact sine series in the odd frequencies whose
    coefficients are `r^3` times polynomials in `log r`; Parseval in the angle and the radial weight, which increases
    in r after the factor `r^6` is absorbed, evaluated at the inner radius of each annulus give a lower bound for the
    integral over each annulus, and the integrand is nonnegative elsewhere. The exact coefficients were formed by two
    spline constructions compared on every coefficient, the exact square integrals by two integration methods, and the
    endpoint weights in two interval engines. With `||L K||_X < 2464.68293019825564964515` of 10-22 11:31, every C
    with `||h||_X <= C ||L h||_X` for all h in a domain containing K satisfies `C > 0.069361443018`, and the same
    holds on `D cap {J = 0, c = 0}` of section 10, next step 1, through the approximants `K + 2 b_delta` described
    there. This is a necessary lower bound only: by 5(p) no finite C exists on D or on `D cap {J = 0, c = 0}`, and it
    gives no inverse estimate, closing argument or distance to a profile. Also checked in a completed referee review
    with a corrective follow-up, followed by a separate adjudication.
  - 10-22 12:02 audit of the text of the draft of 10-22 11:34 by the verifier: section 1, read afresh in full, and
    every change since the draft of 10-22 10:32, with the displayed decimals in them, are consistent with the verified
    results at their stated scope, with no required correction (section 8); not a verification of a new result.
  - 10-22 12:12 audit of the mathematical content of the draft of 10-22 12:00 by the verifier: section 1, read afresh
    in full, and the nine changed passages since the draft of 10-22 11:34 are consistent with the verified results at
    their stated scope; one wording recommendation, adopted; the timing statements of that draft were left open
    (section 8); not a verification of a new result.
  - 10-22 12:29 audit of the three changed passages of the version of 10-22 12:15 by the verifier: confirmed, except
    that its clause on the timing of the draft of 10-22 12:00 became correct only with the timing change of 10-22
    12:21 (section 8); not a verification of a new result.
  - 10-22 12:36 audit of the timing changes of the version of 10-22 12:21 by the verifier: confirmed; the statements
    about the actual end of the run were left open (section 8); not a verification of a new result.

## 4. Dependency chart
Dependency path of a YES and where it stops (each arrow reads "is an input of"):
- Exact trial, Green identities and exactification (verified) -> zeroth-order residual bounds (section 6; two interval
  methods in each region; the shared canonical density moment archive used in every region and its composition with
  these bounds are verified) -> the residual bound `eta` of section 7. Stops: no residual bound in a norm with
  derivatives matched to a realization (X is the diagnostic norm, not a norm matched to a realization; in X a direct
  whole-plane bound is verified but coarse (section 6), while the sharper X-norm bounds in section 6 on the annulus E
  remain conditional on unverified derivative majorants; the regularity premise is verified for the exactly joined
  trial, and the X norms on the two radial end regions outside E are verified, so that the sharper full-plane X bounds
  are conditional only on the majorants on E); the present trial's residual is not in the corner forcing space, nor in
  the axis-weighted and quadrant norms with `a >= 5/2` (below).
- Source identities, axis control and trial scalars (verified) -> local and frozen linear theorems (5(a) to 5(o) and
  the frozen inverse of 5(q); by 5(p) the diagnostic weighted `H^1`-type norm, and by 5(r) the weighted factor
  supremum norm, admit no same-norm inverse estimate on domains containing their respective quasimodes, and by 5(q)
  the full L does not map every compact test density into the axis-weighted norms with `a >= 5/2`, and no closed
  linear realization of L in these norms at `s = 153/50` has a domain containing the maximal frozen domain) -> an
  assembled realization and its Fredholm estimate -> `K_H`, `K_L`, `C_B`, `C_V`. Stops: no assembled realization
  (source disc, saddle, axes, conic region and infinity together) and no outer matching.
- `K_H`, `K_L`, `C_B`, `C_V`, `eta` in one realization -> the two-norm theorem (section 7, verified as an abstract
  statement) -> YES. Stops: none of the inputs is available, and for the formulation of section 10 the augmented
  nonlinear map is not constructed.
- Trial scalars (verified) -> the jet-continuity exclusion centred at the trial (section 7) -> an X3-centred NO.
  Stops: no certified bound on the jets at P of X3 minus the trial; no uncertainty ball around X3 is specified and
  proved to lie inside the neighbourhood, which in our judgement is too narrow to contain a meaningful one (section
  7).

Exact identities (verified):
- Centre normalization `3 c_l - c - 1 = 0` under continuous factorization.
- Source identities: `d_y V_2(P) = 1` and `d_x V_1(P) = 2 c_l - 1` at exact solutions with `rho_y(P) != 0`. They hold
  under C^1 regularity.
- Scaling covariance:
  - `rho_a(X) = a rho(X/a)` gives `F(rho_a) = (F rho)_a`, `c[rho_a] = c[rho]` and `J(rho_a) = a^{-2} J(rho)`, where
    `J(rho) := a(0)`.
  - The scaling tangent `K = rho - X.grad rho` satisfies `L K = eps - X.grad eps`, `c[K] = 0` and `J(K) = -2 J(rho)`.
  - These identities require `K` to belong to the chosen operator domain. The graph argument requires the dilation
    curve to be `C^1` in the chosen graph norm, `F` to be differentiable there, and both `J` and the relevant velocity
    derivative at the centre to be continuous there (for `a < 5/2` and finite `s >= 0`, 5(q) proves that J is
    discontinuous on its smooth compact strain-zero test class in `Y_(a,s)` and in the frozen graph norm, and for
    `0 <= s < 4` in the graph norm of L on the test densities with image in `Y_(a,s)`; so for `a < 5/2` and
    `0 <= s < 4`, J is not continuous on any linear domain containing these densities, equipped with the graph norm of
    L in `Y_(a,s)`). Alternatively, the direct spatial argument requires admissibility of `K` for the canonical
    inverse and requires `U - X.grad U` to have the necessary parity, sublinear growth and differentiability. In this
    alternative, `c[K] = 0` and `J(K) = -2 J(rho)` must also be justified from the actual velocity and centre trace
    hypotheses. Continuous centre factorization and `C^{2,alpha}` regularity alone do not imply these hypotheses: for
    the density `x^2 y [1 + chi(r) r^{1/10} sin(r^{-1/5})]`, with chi a smooth radial cutoff equal to one near 0,
    which has both properties near the origin, `K/(x^2 y)` has no continuous centre trace. This example is kinematic,
    not an exact `P_2` solution, and whether stationarity supplies the missing regularity is not established here. For
    the exactly normalized modal trial, K belongs to an explicit graph domain of the diagnostic weighted `H^1`-type
    norm and `L K` is not zero (section 10, next step 1).
- Source functional, valid for `rho` of class `C^2` and `h` of class `C^1` near P, with V and `W[h]` of class `C^1`
  near P: `d_y(L h)(P) = (mu - 1) h_y(P) + g d_y W[h]_2(P) + g' W[h]_1(P)`, with `mu = d_y V_2(P)` and
  `g' = rho_xy(P)`. At an exact solution with V of class `C^2` near P (assumed for this scaling-mode identity)
  `w'(x_*) g' + g mu'(x_*) = 0`, where `w(x) = V_1(x,0)`.
- Elementary Fredholm bookkeeping (abstract): restricting a Fredholm L to the kernel of a continuous, nonzero J
  lowers the index by one.

Certified inequalities (verified):
- Central strain of X3 and its normalization defect (section 3).
- Trial scalars, independently certified:
  - the trial's source `P = (p, 0)`: `p = 8.60006380515717832258` within `7.8e-21`;
  - `mu~ - 1 = -2.2528046115e-8` within `4.7e-19`;
  - `g = 29.7494906633335090153` within `9.2e-20`;
  - `g' = 0.273411443977248614` within `3.5e-19`.
- Axis control:
  - Hypothesis: `|h| <= eps x^2 |y| (1 + r^2/L^2)^{(k-3)/2}`.
  - Velocity bound: then `|U_1[h](x,0)| <= 53.50488918 eps |x|`.
  - Conditional uniqueness of the source: every exact normalized canonical `P_2` solution within `eps <= 0.01` of X3
    in this factor bound has `rho_y > 0` on the positive axis and exactly one positive-axis equilibrium, with
    eigenvalues `2 c_l - 1` and 1. Off-axis equilibria are not excluded.
  - Direct interval axis values of X3, which this theorem can use:
    - `U_1(7,0) in [-54.520, -54.459]` and drift `w(7) in [-15.492, -15.432]`;
    - `U_1(10,0) in [-41.680, -41.590]` and `w(10) in [14.07, 14.17]`.
    - Each displayed interval is rounded outward separately from a tighter internal enclosure, so the drift intervals
      are not obtained from the displayed velocity intervals by adding `c_l x`.
- Scalar strain bound: `|c[h]| <= eps L^2/(1 - gamma) (1/12 + 3 sqrt(3)/(8 pi))` whenever
  `|h| <= eps x^2 |y| (1 + r^2/L^2)^{(gamma-3)/2}`, `0 < gamma < 1`. Equivalently `|c[h]/3|` (the coefficient of X in
  `W[h]`) is at most `eps L^2/(1 - gamma) (1/36 + sqrt(3)/(8 pi))`. An earlier version of this report attached the
  second constant to `c[h]` itself (section 8).
- Exact repair of X3's scalar and far tail at factor distance `< 1.477e-5`; exactification cost of the modal trial
  `< 4.080e-10` relative.
- Strain part of the source velocity of the difference h between X3 and the trial:
  `-2.95309e-8 < p c[h]/3 < -2.95294e-8` (raw c; P = (p, 0) the trial's source; section 7).
- Leading far tails of X3 and the trial: `X3 - rho~` lies in `L^2(R^2, <r>^{-2 beta} dX)` if and only if
  `beta > 1 + k`, hence in no `H^s(R^2)` with `s >= 0` (section 2).
- Far residual of the trial: `-0.03688201144 < Eps_1 < -0.03688201143` for the `sin theta` coefficient of its
  `r^{2k-1}` profile (section 2).
- Tail repairs `rho_T` of the trial: factor distance below `0.334616 T^{k-1}`; for the higher repairs `rho'_T`,
  residual `eps'_T` with `||eps'_T||_{dot H^{-1}} <= ||r eps'_T||_{L^2} < infinity` (finite, not quantified) and
  factor distance below `0.334616 T^{k-1} + 947.4716170719 T^{2k-2} + 11225.91941797 T^{-2}` (section 10, item 4).
- Growth of the residual norms of the tail repairs (asymptotic lower bounds, no finite T certified):
  `liminf_{T -> infinity} T^{-2k} ||eps|| > 0.03135338258` in `L^2(R^2)` and `H^{-1}(R^2)` for either
  `eps = eps_T = F(rho_T, 1/k)` or `eps = eps'_T = F(rho'_T, 1/k)`, and `liminf_{T -> infinity} T^{-2k-1}` of
  `||eps'_T||_{dot H^{-1}}` and of `||r eps'_T||_{L^2}` above `0.0022215507882` (section 10, item 4).
- Source defect of the tail repairs: `|partial_y F(rho_T, 1/k)(P)| > 6.7015e-7` for every admissible T, and
  `|partial_y F(rho'_T, 1/k)(P)| > 6.6989e-7` for every admissible T, at the trial's source P (section 10, item 4).
- The `r^{k-2} sin(theta)` coefficient of the residual of `rho_T` at infinity:
  `184130.68809691 < L_d < 184130.68809692` for every admissible T (section 10, item 4).
- The `r^{3k-2} sin(theta)` coefficient of the residual of `rho_T` at infinity:
  `-2734.192205182 < C_{2,0} < -2734.192205181` for every admissible T, and the `sin(theta)` coefficient of the
  counterterm `H_2` of `rho'_T`, in `(-298.795137988, -298.795137987)` (section 10, item 4).
- Auxiliary source inverse of the trial for one explicit `C^4` cutoff at `delta = 0.0165`: norm below `1.2e35` in
  `H^s` for every s in `[61/20, 31/10]` from the unscaled constant, and, through the isotropic dilation, below
  `1.223e11` in `H^s` and below 922 in the scaled norm `N_500` for every such s (5(o); upper bounds only, not
  estimates of the true norm).
- Radial Taylor models of the flow certificate on all 7809 middle cells, all 261 modes (5(l)): finite-input
  verification on every cell, and for the trial's canonical inputs the models enclose the canonical modal quantities
  on every middle cell; on the nine rectangles formed by the middle cells 0, 4102 and 7808 and three angular cells,
  the composition of the modal models into `s`, `v_2`, `v_1` and T with its complete product remainder is enclosed by
  two independent methods, and the certificate's reported ranges contain these enclosures, and for the trial's
  canonical inputs they contain the canonical flow fields on these rectangles (axis quotients as continuous
  extensions); the exported Green boundary values of all middle cells contain the canonical values, and the exported
  density polynomial boxes of all middle cells contain the exact coefficients of the trial; the angular linkage beyond
  the nine tested rectangles and the full flow certificate are open.
- Residual derivative checks (section 6): on the middle cells 4102 (which contains the trial's source), 4125 and 4211,
  whole-cell upper bounds of the residual's derivative Wiener sums through total order 5 are at most the 63 saved
  derivative majorants of these cells, and at 13 sample log-midpoints the pointwise sums are at most the 138 saved
  majorants available there; the canonical centre moments used are verified. No bound on other cells, no location of a
  physical maximum and no derivative forcing norm from these checks (the direct bound is the next item).
- Direct whole-plane X norms of the residual (section 6): `||eps~||_X < 245653983.313885102003858` and
  `||eps~ - partial_t eps~||_X < 30665526224.2484290248531` for the exactly normalized trial, with velocity
  derivatives from the Green ODEs and the verified radial models on the middle cells, exact products by two methods on
  every cell, and the exact inner and exterior expansions. These first bounds are coarse (their exterior term
  dominates). A finer exterior computation, on 89 cells of the exact exterior expansion, sharpens them to
  `||eps~||_X < 8.38010956871949018314234` and `||eps~ - partial_t eps~||_X < 2467.95347982509225629694`, and a finer
  inner computation, on 44 cells of the exact inner expansion, further to `||eps~||_X < 1.49546805188731021373656` and
  `||eps~ - partial_t eps~||_X < 2464.68293019825564964515` (section 6); the middle annulus term dominates for both.
  All of these bounds are in the diagnostic norm X only, remain larger than the conditional bounds of section 6 and
  verify none of the saved majorants of its conditional theorem.

Conditional theorems (verified as conditional statements): the frozen and local theorems of section 5, including the
uniform frozen source inverse through `mu = 1` (5(c)), the variable-coefficient source obstruction (5(d)) and the
graph-norm quadratic obstruction (5(g)); the two-norm iteration theorem of section 7; the tail, kernel and family
theorems (5(h); also referee-audited), whose PDE hypotheses are all open; the local source estimate and the auxiliary
source inverse at order 31/10 and their order family (5(o)), all of whose hypotheses are verified for the trial at
`delta = 0.0165` (5(o)), the isotropic dilation corollary of the auxiliary inverse, the rough-coefficient extension
and the whole-plane Sobolev ball for the moving-source hypotheses (5(o)); the moving-source statements for perturbed
profiles (5(o)); the far-domain statements and the diagonal y-axis jet rows of a jet-plus-remainder realization (5(m);
first derived in referee audits). Model theorems (verified and audited): the weighted saddle inverse (5(e)), the face
velocity splitting (5(f)) and the collar coupling lemma (5(i)). Unconditional elementary lemma (verified): the tail
exponent and angular profile are determined by the solution modulo a far-weighted remainder (5(h)).

Refuted proposals and established counterexamples (verified failures of proposed statements or estimates, and the
counterexamples establishing them):
- No inverse of the linearization can gain a derivative (`C^{3,alpha} -> C^{4,alpha}`): compact flow-box waves.
- A logarithmic far weight admits tails `r^k log r Phi(theta)` whose images leave any decaying residual space plus one
  scalar direction.
- A weighted factor supremum alone cannot bound interior velocity or the bilinear coupling, even for compact smooth
  admissible perturbations. The low norm needs a genuine Hoelder (or equivalent) component.
- Energy positivity fails (each is the failure of one estimate; none implies instability or nonexistence):
  - the unweighted density energy pairing for every trial dilation with `c_l <= 6`;
  - the former `Phi` energy of the problem statement as a uniform coercivity claim: its matrix at the centre is
    `M_Phi(0) = diag(2 - c_l, 5 c_l)` (from `psi_xy(0) = 3 c_l - 1` and the parities), and its quadratic form has a
    negative direction on localized parity-compatible perturbations, even with `c[h] = 0`, whenever `c_l > 2`;
  - the former global positive-damping condition, since `d(P) = 2 - 2 c_l < 0`.
- The stored X3 with `c_l = (1 + c)/3` has an unbounded absolute far residual: a growing `r^k` term.
- Weyl sequences for the frozen whole-plane Sobolev realization below threshold (a claim of an earlier specification):
  false; the frozen operator is bijective there (section 5).
- Boundedness of the canonical coupling `h -> U[h].grad rho` on the pure face weight `L^2(|y|^{-2b})`, `b > 2`: false
  (dilation counterexample, section 5(f)). For the normalized coupling `W[h].grad rho` the same dilates give growth
  wherever `2 rho_y - x rho_xy != 0` on the collar (verified for the pure face weight and a background with
  nonvanishing coefficient, with its own proof; 5(f)). The fixed-cutoff Taylor modification of the velocity on these
  weights: unbounded (dilation counterexample; referee audit). A derivative gain larger than 2 for the edge forcing:
  false (the gain is `b - 3/2`).
- `f_y(P) = 0` as a necessary range condition of the normalized linearization (it is the condition of the pure
  transport germ in 5(a)): false. Write `P = (x_P, 0)`, `x_P != 0`, for the point at which the condition is tested,
  let `q(s, y) = s^2 y - y^3/3` (harmonic), `chi` a smooth cutoff, even in each coordinate, equal to 1 near 0 and
  supported in a disc of radius less than `|x_P|/2`,
  `k = chi(x - x_P, y) q(x - x_P, y) + chi(x + x_P, y) q(x + x_P, y)` and `h = -Lap k`. Then h is smooth and compactly
  supported, its support avoids the y-axis, the origin and neighbourhoods of `+-P` (it meets the x-axis, where h
  vanishes by oddness), it is even in x and odd in y, of the form `x^2 y a_h`, and it vanishes near P and near the
  origin. Its canonical stream function is `d_x k`, its velocity `(-k_xy, k_xx)` equals `(-2(x - x_P), 2y)` near P,
  and its strain is 0. For any `C^2` background with `grad rho(P) = (0, g)` the exactly normalized linearization
  satisfies `L h = U[h].grad rho` near P, so `d_y(L h)(P) = 2g`, which is nonzero when `g != 0`, although every jet of
  h at P vanishes. This shows that the nonlocal term `g d_y W[h]_2(P)` of the source functional cannot be replaced by
  local data; it proves no index statement.
- The present trial's residual as corner forcing data: false. Near 0 the trial's factor is
  `a = 1 + r^2 R^{-2} D(theta) + O(r^4)` with `D(theta) = sum_{m < M} d_m cos(2 m theta)`, `M = 260`, and
  `d_{M-1} != 0` (also `d_2 != 0`). Hence a is not twice differentiable at 0, the density is `C^{4,1}` but not `C^5`
  there, and `eps~ = r^5 E(theta) + O(r^7 (1 + |log r|))` (with the corresponding derivative bounds through order 7).
  The sine coefficient of E at frequency `2M + 3 = 523` is `c (M - 2) d_{M-1}/(8 R^2)`; with the trial's exact data it
  lies in `(5e-12, 6e-12)` (two independent interval evaluations). E is not the restriction of a homogeneous quintic,
  so for every pair of weight exponents with `a + b >= 6` neither `eps~` nor its double Taylor remainder
  `T_x^6 T_y^3 eps~` (either order of the two subtractions) lies in `L^2(|x|^{-2a} |y|^{-2b})` on any neighbourhood of
  0; the working weights have `a + b = 9.52`. This is an obstruction to one forcing space for one trial. It says
  nothing about exact solutions, and the zeroth-order certificates of section 6 (weight `m ~ r^3` at 0) are
  unaffected.
- The exactly joined trial's residual as forcing data when `a >= 5/2`, in either the axis-weighted norms `Y_(a,s)` of
  5(q) or the quadrant norms of 5(e): false (5(q)). On the y-axis `eps~_xx(0, y)/2 = Q y^3 + o(y^3)` with
  `6.087210e-6 < Q < 6.087213e-6`, so `|eps~|` is at least a positive constant times `x^2` on a rectangle adjacent to
  the y-axis. This includes `(a, s) = (6, 153/50)` and the revised working point of 5(e). Compared with the previous
  item (product weights with `a + b >= 6` near 0), it concerns weights singular along the whole y-axis and holds for
  `a >= 5/2` and every real b; like it, it concerns one trial and these forcing spaces only. For `s = 153/50` and
  `a >= 0` the residual lies in `Y_(a,s)` exactly when `2k < a < 5/2` (5(q)); at those weights the frozen centre
  transport is not Fredholm.
- A bound of the corner coupling remainder by the whole-plane pure product-weight norm: false. With `rho = x^2 y` near
  0, `S = a + b` and rescaled sources `h_R = R^{S-1} F(X/R)`, `d_7[F] != 0`, the norms `||h_R||_{L^2(w_{a,b})}` are
  constant while the `(6, 3)` double Taylor remainder of the coupling on `B_{1/2}` grows like `R^{S-8}` (`R^{38/25}`
  at the working point; 5(k)). No nonzero corner coefficient of the velocity is bounded on the whole-plane pure
  weight, for any real a, b.
- Classical density jets from weighted `L^2`: false. For every `a > 0` there is a compactly supported even-x, odd-y
  density in `L^2(|x|^{-2a} dX)`, a weighted-norm limit of smooth functions vanishing near `x = 0`, with no continuous
  representative across `x = 0` (spikes `psi(y) eta((x -+ 2^{-j})/eps_j)`, `eps_j = 2^{-j(2a+2)}/16`). Jets on the
  axes must therefore be defined as coefficients of the weighted decomposition (which are unique), not as traces.
- A local bootstrap at the source (local smoothness of `L_P u` implies high local Sobolev regularity of u), with the
  nonlocal term kept: false (5(n)).
- Control of the strain functional by unweighted `H^t(R^2)`, `t <= 2`: false, also on perturbations vanishing near the
  origin for `t < 2` (5(n)).
- Boundedness on `Y_(a,153/50)`, `a >= 0`, of the scaling term `h -> (c[h]/3) X.grad rho~` of L when `a <= 1 + k` or
  `a >= 2`: false (5(q)); for `1 + k < a < 2` it is bounded, of rank one and compact.
- `C^{2,alpha}` or `H^{3.1}` regularity with the parities implies the continuous centre factorization: false (5(n)).
- A transport-only inverse that is regular at the source when `mu_P = 1`: false (smooth compact forcing, 5(l)).
- The trial's residual as forcing data in unweighted `L^2(R^2)`, `H^{-1}(R^2)` or `dot H^{-1}(R^2)`: false (it is
  `r^{2k-1}` times a nonzero angular profile at infinity; section 2).
- The residual `eps_T` of the single tail repairs `rho_T` as forcing data in `dot H^{-1}(R^2)`, or with `r eps_T` in
  `L^2(R^2)`: false for every admissible T (nonzero `r^{3k-2}` and `r^{k-2}` rows; section 10, item 4).
- A stationary correction of the trial in `L^2(R^2)`, for some value of the coefficient of `X.grad rho`, under the
  hypotheses of section 7: false. That the class `rho~ + L^2(R^2)` contains a neighbourhood of the trial in the factor
  norm of the axis control: false (exactly normalized repairs at factor distance below `0.334616 T^{k-1}` lie outside
  it; section 10, item 4).
- That the centre constraint `J(h) = 0` (alone, or added to `c[h] = 0`) improves the best constant of an inverse
  estimate `||h||_X <= C ||L h||_X` in the graph topology `||h||_X + ||L h||_X` of the diagnostic weighted `H^1`-type
  norm of section 10: false under explicit background and domain hypotheses (compact bumps with `J = 1`, zero strain
  and graph norm tending to 0; section 10, next step 1); so it cannot restore a finite inverse estimate when the
  comparison domain contains a nonzero kernel vector. This does not exclude the algebraic removal of a kernel vector,
  and topologies that control the centre factor are not covered.
- A same-norm inverse estimate `||h||_X <= C ||L h||_X` in the diagnostic weighted `H^1`-type norm X of section 10 at
  the exactly normalized modal trial, on any perturbation domain that contains the smooth compactly supported
  densities of 5(p), which vanish near the centre and have `J = c = 0` (among them the graph domain D of section 10,
  next step 1, and its subspace with `J = 0` and `c = 0`): false (centre quasimodes, section 5(p)). Also false on such
  a domain, for the sequence of 5(p): the same estimate with an added `H^{5/2}` or compact remainder, and the Fredholm
  property of every closed realization of L in X that contains the sequence. The same holds in each of the more
  singular centre-weighted norms `X_m`, `m >= 2`, of 5(p). Estimates from a stronger forcing space into X or into a
  fixed `X_m`, other correction norms and domains that exclude these densities are not covered; a bounded right
  inverse is not excluded.
- A same-norm inverse estimate `||h||_F <= C ||L h||_F` in the weighted factor supremum norm of the axis control, on
  the space `B_F` of continuous factors vanishing at 0 and at infinity, at the exactly normalized modal trial, on any
  domain that contains the smooth compactly supported densities of 5(r), which vanish near the centre and have
  `c = 0`: false (5(r)). Also false on such a domain: the same estimate with a bounded linear compact remainder, and
  the Fredholm property of every closed linear realization of L in `B_F` whose domain contains the sequence. Hoelder
  or derivative norms of the factor, stronger domain norms, weaker target norms and domains that exclude these
  densities are not covered; a bounded right inverse is not excluded.
- That the linearization at the exactly joined trial maps the smooth compactly supported densities of the required
  parities with `J = c = 0`, supported away from both axes, into an axis-weighted space `Y_(a,s)` of 5(q) with
  `a >= 5/2` (for any `s >= 0`; this includes `(a, s) = (6, 153/50)`, where the frozen centre transport is
  invertible), or into a quadrant norm of 5(e) with `a >= 5/2` (for any b and m, including the revised working point):
  false (5(q), 5(e)). For `a >= 5/2`, `s = 153/50` and the densities supported in `1 < r < 2`, no subspace of finite
  codimension is mapped into `Y_(a,s)` either, and membership of the image is equivalent to the vanishing of every
  interior even harmonic moment. An inverse on a domain of compatible densities is not covered, and for `0 <= a < 5/2`
  and `0 <= s < 6 - a` all these densities are mapped into `Y_(a,s)` (5(q)).
- That the linearization at the exactly joined trial agrees on the compact-potential test sequence of 5(q) (frozen
  graph domain) with a bounded linear map from the maximal domain of the frozen centre transport `T_0` of 5(q), with
  the graph norm of `T_0`, into `Y_(a,s)`, or that some closed linear realization of it in `Y_(a,s)` (agreeing with it
  on that sequence) has a domain containing that maximal domain (for `s = 153/50` and any real a): false (5(q)). The
  same holds with `L - T_0` in place of L. Realizations on domains not containing the maximal frozen domain, such as
  the graph domain of the actual transport, are not covered.
- A residual-to-error modulus for the distance to an exact profile in the diagnostic weighted `H^1`-type norm X of
  section 10 alone, at fixed centre coefficient and strain: false under the exact-profile hypotheses of section 10,
  next step 1 (conditional on the existence of such a profile). No map omega with `omega(0) = 0` and `omega(t) -> 0`
  as `t -> 0` gives `||q - rho_*||_X <= omega(||F(q)||_X)` for every comparison density q of the class stated there
  (with `J(q) = 1` and `c[q] = c[rho_*]`) in any X-neighbourhood of rho_*; in particular no finite C gives
  `||q - rho_*||_X <= C ||F(q)||_X` throughout such a neighbourhood. This concerns the distance to the chosen exact
  profile in that class; the distance to a solution set, stronger norms controlling the centre factor and comparison
  classes with a prescribed leading far coefficient are not covered.
- A quadratic estimate `||W[h].grad h||_X <= C ||h||_X^2` for the quadratic term of section 7
  (`F(rho + h) = F(rho) + L h + W[h].grad h`) in the diagnostic weighted `H^1`-type norm X of section 10 alone, on an
  X-ball of positive radius about 0, also within the compact densities with a continuous even-even centre factor and
  `J(h) = c[h] = 0`: false (an explicit sequence of four concentrating packets with an exact strain compensator has
  `||h_n||_X -> 0` and `liminf ||W[h_n].grad h_n||_X > 0`; section 10, next step 1). Estimates with h in a stronger
  norm or in a graph norm (but see the next item), with the quadratic term in a weaker norm, or on a restricted
  finite-dimensional class are not covered.
- The same quadratic estimate with h measured in the graph norm, `||W[h].grad h||_X <= C (||h||_X + ||L h||_X)^2` on a
  graph ball of positive radius about 0, also within the compact densities with a continuous even-even centre factor
  and `J(h) = c[h] = 0`, at a background satisfying the hypotheses of section 10, next step 1, whose transport field V
  is locally `C^1` and vanishes at a point `(p, 0)` with `p > 4`, in particular at the exactly normalized modal trial
  (with this point its source): false (two translated packets at `(p, 0)` and `(-p, 0)` with an exact strain
  compensator have `||h_n||_X + ||L h_n||_X -> 0` and `liminf ||W[h_n].grad h_n||_X > 0`; section 10, next step 1).
  Stronger Sobolev graph norms, the norms of the proposed realization, a weaker image norm and restricted
  finite-dimensional classes are not covered. The logarithmic graph norms of 5(q) are treated in the next item.
- The same quadratic estimate in the logarithmic norms of 5(q), `||W[h].grad h||_Y <= C_r (||h||_Y + ||L h||_Y)^2` for
  the h of graph norm below some `r > 0`, at the exactly joined trial, for any real a and finite `s >= 0`, also on the
  compact-potential class `D_cp` of 5(q) (where `J = c = 0` and all centre jets vanish), in the kernel of any finitely
  many linear constraints on it, continuous or not, and on the zero set near 0 of finitely many constraints on it that
  vanish at 0 and are continuously Frechet differentiable in the graph norm with onto derivative at 0: false (packets
  transverse to the flow; 5(q)). Stronger domain norms, a weaker image norm and scales of spaces are not covered.

Not available in general: the canonical nonlocal coupling `h -> U[h].grad rho` has order zero (U is a matrix of
Fourier multipliers homogeneous of degree 0 applied to h). Its compactness, or an arbitrarily small coefficient in the
top Hoelder norm, would require a separate argument; neither is established or used in this report.

Exploratory calculations (floating point; evidence only, never used as bounds, not reproduced by the verifier
unless stated):
- X3's published sampled residual maxima, reproduced at three resolutions (section 6).
- Sobolev norms of the trial's residual near P, the localized norms that the source estimate must absorb, and
  band-restricted, coarse-knot and refined-knot refits (section 10, item 4).
- Sampled coefficient suprema near the source (5(o)).
- Orbit costs and principal energy rates for conic weights, and the nominal size of the gap (5(l), section 10, item 4
  and next step 2).
- Finite sections of the linearization with and without free tails (section 10, next step 1).
- Equal-residual states with `c_l` between 5.29 and 5.60 from a first investigation (section 10).
- The four jet quantities at P of the difference between X3 and the trial (section 7).

Unverified and not used: the structural realization analysis, the target formulation and the index reduction in
section 10; the near/far constants and the full coupling remainder at the y-axis (the structural part is verified,
5(j)), the derivative versions and edge matching of the double Taylor splitting at the corner (its corner-coefficient,
double-remainder, annular-trace and smooth-factor coupling parts are verified, 5(k); its factor-regularity hypothesis
fails for the present trial, section 4), and the full description of the singular structure of the frozen forward
inverse at P (a cusp of Hoelder order `d/A = 3.0293`, `d = 1 + g`; a statement about local regularity at P of the
frozen model, not about membership in the global classes `P_m`; its elementary Fourier parts, and separately the
frozen Hoelder mapping estimate, its sharpness and the smooth-forcing ceiling of section 10, are verified; the full
cusp expansion is not, 5(b)). All three have been referee-audited (one model; the y-axis lemma after repairs); their
verification is open.

## 5. Strongest linearized inverse theorem or obstruction
No inverse of the full variable-coefficient linearization L has been established in any space. The verified positive
linear statements are local, frozen, or concern parts of L (for example the pure transport inverse of 5(l)); none
gives an inverse of the full coupled operator. Section 5(p) is a whole-plane obstruction at the exactly normalized
trial: in the diagnostic weighted `H^1`-type norm of section 10 no same-norm inverse estimate holds on a domain
containing its quasimodes, and section 5(r) gives the same kind of obstruction in the weighted factor supremum norm of
the axis control. Section 5(q) shows that in axis-weighted norms with `a >= 5/2`, which for `s >= 3/2` include every
weight with `a >= 0` at which the frozen centre transport is invertible, the full L does not map every natural compact
test density into the space, and that for `s = 153/50` and every real a no closed linear realization of L in `Y_(a,s)`
has a domain containing the maximal domain of the frozen centre transport.

(a) Local source transport.
- Setting: `L_A h = A s h_s + y h_y - h` with `A > 1`, on a rectangle `D = [-S, S] x [-Y, Y]` centred at a linear
  source, on functions odd in y.
- Solvability: for `f in C^{m,alpha}` with `m >= 1`, the equation `L_A h = f` is solvable in `C^{m,alpha}` iff
  `f_y(0) = 0`. The kernel is spanned by y.
- Inverse: with `T_t(s, y) = (e^{-A t} s, e^{-t} y)`, `R f = int_0^inf e^t f(T_t X) dt` satisfies
  `||D^beta R f||_{L^inf(D)} <= ||D^beta f||_{L^inf(D)}/(A a + b - 1)` for `beta = (a, b)`, `2 <= a + b <= m`
  (supremum norms on the backward-invariant rectangle; the pointwise form is false), and the analogous Hoelder
  seminorm bound with denominator `A a + b - 1 + alpha`.
- There is no derivative gain. With `f` only `C^1` the resonant integral can diverge; a Dini modulus for `f_y` at 0 is
  a sufficient condition for convergence. It is not necessary (verified for the local transport model; first given in
  a referee review): with `t = log(1/|y|)`, `h = y int_t^inf sin(u)/u du` and `f = y sin(t)/t` are `C^1`, satisfy
  `(A s d_s + y d_y - 1) h = f`, and the modulus of continuity of `f_y` at 0 satisfies
  `omega(e^{-T}) >= 1/(T + 2 pi)`, which is not a Dini modulus.

(b) Frozen coupled source.
- Frozen operator: `L_P = A s d_s + y d_y - 1 - g M`, where `M` is the Fourier multiplier `xi^2/|zeta|^2`.
- Exact conjugation: with `a = g/(A-1)` (`= 3.2511`) and `Lambda = (-Lap)^{1/2}`,
  `Lambda^a L_P Lambda^{-a} = A s d_s + y d_y + a - 1`. On the homogeneous Sobolev space `dot H^a` (norm
  `||Lambda^a h||_{L^2}`) the inverse norm is exactly `1/|a - (A+3)/2|`.
- Below threshold: ordinary inhomogeneous `H^s` (with parity) has a bounded inverse for `0 <= s < s_fast`, where
  `s_fast = (g + (A+3)/2)/A`, about 3.57855 (`s_slow = b_0 = (A+3)/2`, about 6.5754).
- At threshold: at `s = s_fast` there are normalized critical sequences.
- Above threshold: for every `s > s_fast` the cokernel is infinite-dimensional, by explicit Fourier-characteristic
  adjoint kernels.
- Consequence: raising the isotropic order cannot repair this model. Every ordinary `H^s` with `s > s_fast` is beyond
  threshold; in particular every `H^s` that embeds in `C^3` (`s > 4`) is.
- Explicit inverse (verified; derived first by a referee). With `q = A + 2 - a` and
  `delta_r(xi, eta) = (r^A xi, r eta)`, the conjugation reads
  `|zeta|^a L_P^ |zeta|^{-a} = -(A xi d_xi + eta d_eta) - q` on the Fourier side, and for compactly supported smooth
  odd-y forcing the below-threshold inverse is
  `h^(zeta) = -|zeta|^{-a} int_0^1 r^{q-1} |delta_r zeta|^a f^(delta_r zeta) dr`, which is the negative-time semigroup
  integral. The profile integral `B_f(zeta) = int_0^inf r^{q-1} |delta_r zeta|^a f^(delta_r zeta) dr` satisfies
  `B_f(delta_R zeta) = R^{-q} B_f(zeta)`, and it is nonzero for explicit allowed data (`f = d_y(phi * phi(-.))`). The
  claimed consequence, a cusp of the forward solution at P with Hoelder order `d/A`, needs a finite-part construction
  and localization that are not verified (section 4).

(c) Source jet and near resonance.
- Pure transport: the isolated jet equation `(mu - 1) h_y(P) = f_y(P)` costs `1/|mu~ - 1|` (about `4.4e7` at the
  trial) when the coupling terms are treated as independent forcing.
- This does not transfer to the coupled operator. Verified frozen theorem: `A x d_x + mu y d_y - 1 - g M` is bijective
  from its maximal graph domain onto ordinary `H^{31/10}` (also on the even-x, odd-y subspace), with inverse norm at
  most `500/1687`, uniformly for `10 <= A <= 51/5`, `99/100 <= mu <= 101/100`, `29 <= g <= 30`. This box contains the
  trial's frozen source coefficients. The source derivative of the inverse is bounded by
  `(500/1687) [8 pi (s-1)(s-2)]^{-1/2}` times the forcing norm. At `mu = 1` the nonlocal term solves forcings with
  `f_y(0) != 0`. The earlier inference "every inverse that solves for `h_y(P)` costs `1/|mu~ - 1|`" is therefore
  withdrawn; the source functional is not the full cokernel functional of L.
- Extension (verified, 21:44). On the same box the frozen operator is bijective from its maximal distributional graph
  domain onto `H^sigma` for every `3 < sigma < 2373/680`, with output bound `500/1687` at `sigma = 31/10` and
  `200/489` at `sigma = 13/4`; the graph-norm bound is 1 plus that constant. The proof constructs the two-sided
  inverse (strong semigroup, Fourier-axis stitching) and does not infer surjectivity from an energy bound.
- P-row (verified, 21:44). For local `H^sigma`, `sigma > 2`, with explicit `C^1` hypotheses on `U[h]` and on the
  strain, `L h = f` implies the full P-row: `(mu_P - 1) h_y(P)` plus the coupling and strain terms at P equals
  `f_y(P)`. No second derivative of h at P enters, because `V(P) = 0`. This is an identity, not an inverse bound.

(d) Variable-coefficient source above threshold (verified conditional theorem). Let V be a real `C^1` field on the
plane with bounded first derivative, of class `C^{N+1}` near a fixed point P with `DV(P) = B`, `N > s`, and let the
coupling be a finite sum of bounded measurable coefficients (`C^N` near P) times Fourier multipliers with bounded
symbols homogeneous of degree zero. If the frozen model at P admits normalized approximate adjoint kernels in
`dot H^{-s}` (this holds for `A x d_x + y d_y - 1 - g M` whenever `(g + b_0)/A < s < b_0`), then no realization on a
Hilbert domain D continuously embedded in `H^s`, with `C_c^infty` dense in D and the operator bounded from D to `H^s`,
plus any bounded finite-rank map from D to `H^s`, is Fredholm (this covers the completion of the `C_c^infty` graph
domain whenever it embeds in `H^s`). So ordinary `H^s` realizations at P with `s_fast < s < b_0` are excluded for the
variable-coefficient operator too, under the hypotheses above (V globally `C^1` with bounded derivative and of class
`C^{N+1}` near P, `N > s`, coefficients of class `C^N` near P, the Hilbert domain as stated), not only for the frozen
model. Orders `s >= b_0` are not covered by this theorem. This is not a statement about `P_2` or `P_infty` solutions.
A verified abstract complement: restricting to a closed finite-codimension domain, adjoining finitely many scalar
unknowns and equations and adding bounded finite-rank terms preserves Fredholmness (index shifted by the counts), so
no finite normalization border bounded into `H^s` removes this obstruction. Other domains or targets (weighted,
anisotropic, or with infinitely many asymptotic data) and terms whose images leave `H^s` (such as the canonical
normalization term in the far target, 5(m)) are not covered and need separate arguments.

(e) Weighted saddle model (verified; also referee-audited). Let `T_0 = -A x d_x + D y d_y - 1` on the open quadrant,
with `D = 2A + 1` and `b_0 = (A+3)/2`, and let
`||h||^2 = sum_{i+j<=m} int x^{-2a} y^{-2b} |(x d_x)^i (y d_y)^j h|^2`. Put `delta = bD - aA - b_0`.
- If `delta != 0`, T_0 is bijective from its maximal domain onto the space. Its inverse has norm exactly `1/|delta|`
  in the base norm and `1 + 1/|delta|` into the sum graph norm.
- If `delta < 0`, the inverse is the forward integral `-int_0^inf e^{-t} f(e^{-At} x, e^{Dt} y) dt`.
- If `delta = 0`, the range is dense and not closed.
- The inverse gains no b-derivative.
- Hence at the saddle the weight decides solvability, not the regularity. The isotropic failure of section 5 is
  removed in this model.
- Sufficient exit-trace condition. Homogeneous solutions whose exit trace H is even, of class `C^{4,nu}` and satisfies
  `H(0) = 0` are `C^{2,alpha}` up to the stable axis apart from the term `H_4 x^4 sgn(y) |y|^{beta_2}`,
  `beta_2 = 2 - 1/D`, whenever `nu >= 2 alpha + (1+alpha)/A`. This is a sufficient condition, and the statement for
  the full solution needs in addition a particular solution of class `C^{2,alpha}`. Note that
  `T_0(x^2 y log|y|) = D x^2 y`.
- Weight versus trace. For `a = 9/2 + nu`, `b = 5/2 + alpha` one has `delta = A(2 alpha - nu) + 1 + alpha`, so
  `delta < 0` iff `nu > 2 alpha + (1+alpha)/A`: the strict form of the trace condition (which allows equality).
  The spaces nevertheless do not match: the generic remainder `|x|^{4+nu}` sits exactly at the critical x-weight, so
  a positive margin or a separate trace component is needed.
- Feasibility (exact rational arithmetic): the weight inequalities needed for a local embedding into `H^s` at the
  saddle (`b > s`) together with `delta < 0` are feasible for `alpha < 0.4061`. Example: `alpha = 2/5`,
  `s = 1701/500`, `b = 3403/1000`, `a = 1299/200`, with delta about -0.0154871. This is a feasibility point, not an
  operator estimate.
- Revised working point (exact rational arithmetic, verified at the exact modal exponent `k`): `alpha = 1/20`,
  `s = 153/50`, `b = 307/100`, `a = 129/20`, `gamma = 129/1000`, `gamma' = 1129/1000` satisfy
  `3 + alpha < s < b < beta_3 + 1/2` (`beta_3 = (6A+1)/D`), `11/2 < a < 13/2`, `delta < 0`,
  `a - 1/2 > [D(s - 1/2) - 1]/A`, `0 < gamma < k`, `gamma' = 1 + gamma < 2`, and the frozen source inequalities
  `s < (g + b_0)/A`, `s < b_0`; all 14 margins are positive. Here delta is about -6.65209, so the saddle inverse norm
  `1/|delta|` in the base norm is below 0.15033. In this window `|delta| < A - 3/2 - D alpha`, so the base inverse
  norm exceeds `1/(A - 3/2 - D alpha)` and the window requires `alpha < (A - 3/2)/D` (about 0.40611). Under `b > s`,
  `delta < 0` implies the inequality for `a - 1/2`. These are statements about the frozen saddle model; the trace and
  embedding statements at this point are open (the `C^{4,nu}` trace condition above uses `b = 5/2 + alpha` and does
  not apply at `b = 3.07`).
- Axis leakage of the full operator (verified, with its own proof; also checked in a completed referee review, a
  separate adjudication and a separate referee audit). For every real b, every integer `m >= 0` and every `a >= 5/2`,
  the full linearization, at backgrounds satisfying the hypotheses of the mapping obstruction of 5(q) (among them the
  exactly joined trial), maps the density h of that obstruction, whose quadrant restriction lies in every space of
  this family, outside the space: the squared norm contains the zeroth summand, `y^{-2b}` is bounded below by a
  positive constant on `[y_1, y_2]`, and `L h >= d_ax x^2` on the rectangle `(0, x_1) x (y_1, y_2)` of 5(q), so
  `int_0^{x_1} x^{4-2a} dx` diverges. This includes the revised working point (`a = 129/20`, `b = 307/100`). It
  concerns the sum norm as defined on the open quadrant (not a quotient norm, prescribed axis jets or a different
  residual variable), and it does not exclude an inverse of the full L on a smaller domain. Forward threshold
  (verified, with the same checks as in 5(q)): `delta < 0` holds exactly when `a > a_e(b) = (bD - b_0)/A`, and
  `a_e(b) - 5/2 = (D/A)(b - 3/2)`; so at a given b all weights with `delta < 0` have `a > 5/2`, and are subject to
  this leakage, if and only if `b >= 3/2`. The model is also bijective for `delta > 0` (first item; for example at
  `a = 0`, `b = 3/2`, where `delta = 5A/2`); such weights are not covered by this comparison.

(f) Face velocity splitting (verified; also referee-audited).
- Setting: on `L^2_b = L^2(R^2, |y|^{-2b} dx dy)`, subtract from the canonical velocity components its first N Taylor
  coefficients at `y = 0`. Call the coefficients `u_{i,j}`, `j < N`.
- Remainder bound: the remainder is bounded by `C_{N,b} ||h||_{L^2_b}` for `N - 1/2 < b < N + 1/2`.
  - The constant is explicit; it fails at both end points.
  - For `N = 3` the verified outward bounds are `C_{3,2.6} < 78.7988` and `C_{3,3.4} < 151.0602`.
  - The same constants apply after ordinary x-differentiation. For `Y = y d_y` the order-m estimate holds with a
    separate finite constant `C_{N,b,m}` and the input norms through order m; these constants are not instantiated.
- Edge coefficients: `||u_{i,j}||_{dot H^{b-j-1/2}} <= Gamma(2b+1)^{1/2} 2^{-b-1} ||h||_{L^2_b}/j!`, in the
  Fourier-side homogeneous space.
- Frequency-adapted extension: with `E_j u = y^j chi(y |D_x|) u`, the remainder `U - sum E_j u_{i,j}` is bounded in
  the same window, with constants `< 82.2601` (`b = 2.6`) and `< 156.1241` (`b = 3.4`). A fixed-cutoff extension
  `chi(y) y^j u_{i,j}` is unbounded.
- Obstruction (verified). The coupling itself is not bounded on `L^2_b` for `b > 2`.
  - Here the coupling is the canonical one, `h -> U[h].grad rho` (the edge forcing). Take F compactly supported away
    from both axes, even in x and odd in y, with `c[F] != 0`, and set `F_R = R^{b-1} F(X/R)`. These have constant
    norm, while `c[F_R] = R^{b-2} c[F]`.
  - The y-coefficient of `U[F_R].grad rho` on a fixed collar of the x-axis therefore grows like
    `R^{b-2} c[F] (rho_y - x rho_xy)(x, 0)`.
  - Normalized coupling (verified, with its own proof; our computation). For `W[F_R].grad rho` the scaling term adds
    `(c[F_R]/3)(rho_y + x rho_xy)(x, 0)`, so the y-coefficient becomes `(2/3) c[F_R] (2 G_1 - x G_1')`,
    `G_1 = rho_y(x, 0)`. It vanishes identically for `G_1 = x^2` and is nonzero near P for the trial
    (`2 g - p g' > 57.1`), so the obstruction persists for the normalized coupling on collars that meet a
    neighbourhood of P. It is a local coupling obstruction, not a statement about a global inverse.
  - The edge coefficients are controlled only in homogeneous norms. Their low frequencies must be controlled by a
    far-field weight; with the far weight `r^{-2 gamma'}`, `gamma' < 2`, the strain of the normalized dilates tends to
    0.
  - This near/far splitting is not proved.
  - The edge forcing gains `b - 3/2` derivatives relative to h, between 1 and 2 in the proposed window.

(g) Quadratic term in a transport graph norm (verified conditional theorem).
- Setting: `s >= 0`, `L = V.grad + B` with B bounded on `H^s` and V real and smooth near a compact coordinate patch
  with `V(P) != 0` at an interior point P. Let D be a linear subspace of the maximal domain of L in `H^s` that
  contains the compactly supported smooth functions in the patch, with a norm dominated on them by the `H^s` graph
  norm of L. Let f be a smooth member of D and W a real linear velocity assignment with `W[f]` smooth on the patch and
  transverse to V at P, such that `h -> W[h].grad f` is bounded from `H^s` to `H^s` on compactly supported smooth h in
  the patch.
- Conclusion: the cross term `W[f].grad h + W[h].grad f` is unbounded from D to `H^s`, through modulated packets
  `lambda^{-s} A cos(lambda v)` constant along the flow. Hence, if `Q(h) = W[h].grad h` is defined in `H^s` on the
  smooth perturbations `f + h` and `f - h` used, Q has no continuous extension at 0 from D to `H^s`, and no
  single-space quadratic bound `||Q(h)|| <= C ||h||_D^2` exists.
- Consequence: a single-space semilinear Newton scheme cannot close in a transport graph norm satisfying these
  hypotheses; whether they hold for the constrained, normalized, weighted realization proposed in section 10 is open.
  This is the reason for the two-norm design of section 7, where the quadratic term is measured from `E x X` into a
  weaker target `Y_L`. It is a statement about a Banach formulation, not about nonexistence. In the diagnostic
  weighted `H^1`-type norm X of section 10 the quadratic term is also not continuous at 0 in the graph norm
  `||h||_X + ||L h||_X` at a background satisfying the hypotheses stated there whose transport field V is locally
  `C^1` and vanishes at a point `(p, 0)`, `p > 4`, such as the exactly normalized modal trial at its source (verified;
  section 10, next step 1); that result uses packets at the zeros of V in place of the transversality hypothesis
  above. At the exactly joined trial the conclusion holds in the graph norms `||h||_Y + ||L h||_Y` of the logarithmic
  norms of 5(q) for every real a and finite `s >= 0`, proved directly on the compact-potential class of 5(q) with
  packets near a point where a plateau velocity is transverse to V (5(q), quadratic term in the graph norm of L); this
  does not verify the hypotheses above for the proposed realization.

(h) Tail data, kernel and family (verified as conditional statements; also referee-audited; corrections from both
are included).
- Setting (the fixed-tail formulation of section 10). Polar coordinates `r, theta`; `chi_far` is a smooth cutoff equal
  to 0 for `r <= R_1` and to 1 for `r >= 2 R_1`.
  - Remainder space X: it embeds continuously in `L^2({r > 2 R_1}, r^{-2 gamma'} dX)`, `gamma' = gamma_E + 1`, where
    `gamma_E < k` is the allowed remainder growth.
  - Profile space Tau: an infinite-dimensional Banach space of angular profiles with the parity of the problem,
    embedded in `L^2(S^1)` and containing `Theta_1`. Example: the `C^m` profiles vanishing on a fixed neighbourhood of
    the axis directions.
  - Ansatz: `rho = (1 - chi_far) rho~ + chi_far [r^{k'} (Theta + tau Theta_1) + C] + h`, where `Theta in Tau` is
    prescribed, `Theta_1` is a fixed independent profile, C are the trial's far corrections, fixed (independent of
    `Theta`, `k'` and `tau`), and `(h, k', tau)` are the unknowns. With `Phi = Theta + tau Theta_1 != 0`, the product
    rule gives `F(rho) = (c_l[rho] k' - 1) chi_far r^{k'} Phi + R`. Let `Y_-` be the forcing remainder space. If
    `R in Y_-` and `Y_- intersect span{chi_far r^{k'} Phi} = {0}` (mapping and directness hypotheses, open), every
    exact solution of this form has `c_l = 1/k'`.
- Tail uniqueness (elementary, unconditional). If `chi_far r^{k_1} Phi_1 + g_1 = chi_far r^{k_2} Phi_2 + g_2` on
  `r > 2 R_1`, with `g_i` in the weighted space, `k_i > gamma_E` and `Phi_i` nonzero in `L^2(S^1)`, then `k_1 = k_2`
  and `Phi_1 = Phi_2`. The same holds for the coefficient of an `r^k log r` term.
- Kernel (conditional). Hypotheses:
  - far mapping of tail increments: `L(chi_far r^{k'} Phi)` is an element of the fixed-tail target plus
    `s_Phi chi_far r^{k'}` times the tail, continuously and linearly in Phi; at an exact solution the product rule
    gives `s_Phi = k' c[chi_far r^{k'} Phi]/3`;
  - a bounded fixed-tail inverse at an exact fixed-tail solution `rho_*`, with unknowns `(g, dk, dtau)` in `X x R^2`;
    here `k_*` is the exact tail exponent of `rho_*`, with `gamma_E < k_* < 1`, and its leading profile is nonzero.
  Conclusion: on the extension `X_+` of X by the tails `chi_far r^{k_*} Phi` (`Phi in Tau`) and the log direction, the
  kernel of the linearization at `rho_*` is algebraically isomorphic to `Tau/span Theta_1`, which is
  infinite-dimensional. Let `Phi_*` be the total leading profile of `rho_*`, `T_*(Psi) = chi_far r^{k_*} Psi` and
  `K_* = rho_* - X.grad rho_*`. If in addition the scaling curve `s -> s rho_*(./s)` is differentiable in the extended
  realization needed to apply L and c, and `K_* - (1 - k_*) T_*(Phi_*)` belongs to X, then `K_*` is the kernel element
  corresponding to `(1 - k_*) Phi_*`, with zero exponent coordinate; these hypotheses do not follow from `C^{2,alpha}`
  regularity. `X_+` lies in a pointwise growth class only under extra embeddings: weighted `L^2` does not give
  pointwise growth bounds.
- Family (conditional). Suppose an independently justified nonlinear construction produces exact solutions `rho_Theta`
  of the displayed ansatz, unique in their stated fixed-tail balls, for every profile `Theta` in an open ball `U`
  about `Theta_0`. Assume `gamma_E < k'(Theta) < 1`, `Phi_Theta = Theta + tau(Theta) Theta_1 != 0`, that the complete
  remainder `g_Theta = (1 - chi_far) rho~ + chi_far C + h_Theta` belongs on the exterior to
  `L^2({r > 2 R_1}, r^{-2(gamma_E+1)} dX)`, and, for every `Theta in U`, that `R(rho_Theta) in Y_-` and
  `Y_- intersect span{chi_far r^{k'(Theta)} Phi_Theta} = {0}`. The theorem of section 7 does not supply this
  construction (it concerns additive corrections only). Then:
  - each `rho_Theta` is an exact solution with `c_l = 1/k'(Theta)`, unique in its ball for its profile;
  - the restriction of `Theta -> rho_Theta` to `(Theta_0 + Z) intersect U` is injective, where Z is a closed
    complement of `span Theta_1`;
  - assume also that the complete remainders `g_Theta` are locally `L^2`, that `J > 0` on the family and that
    `Theta_0` is not in `span Theta_1`; after normalization of `J` by exact rescaling, an injective normalized
    subfamily is indexed by the intersection of U with a codimension-two affine slice through `Theta_0`, which is
    still infinite-dimensional. Parametrization of the whole normalized family (for example by profile rays) would
    need a further compatibility hypothesis.
  - Non-isolation: assume continuity of `Theta -> (h, k', tau)` in `X x R^2` (continuity in X and of the two scalar
    coordinates is an additional hypothesis; low-norm contraction estimates alone do not supply parameter continuity),
    Tau embedded in `C^1(S^1)` and X embedded in the growth norm
    `G_gamma = sup (1 + r)^{-gamma}(|.| + (1 + r)|grad .|)` with `k'(Theta_0) < gamma < 1`. Then the exact solution is
    not isolated in `G_gamma`. Non-isolation after normalization additionally needs continuity of J on the family and
    continuity of scaling in `G_gamma`.
- Variation of `c_l` (conditional). Assume the family is differentiable at `Theta_0` in the realization needed to
  linearize F and c (a `C^1` curve of inputs and continuity of the outputs do not suffice). The first-order variation
  of `c_l` along it is `-c_l^2 ell(Phi)`, where `ell(Phi) = dk'` is a linear functional on Tau. It vanishes on
  `Theta_1`, and on the solution's own profile `Phi_*` under the scaling hypotheses of the kernel statement above; it
  is computable from the fixed-tail linear inverse alone.
  - If `ell != 0` at one solution, `c_l` varies along the family.
  - If `ell = 0` at one solution, only first-order stationarity follows. The inference "ell = 0 at a point implies
    that `c_l` is locally constant" is false (scalar example `k(t) = k_* + t^2`).
  - `ell` is not computed.
- Scope. All PDE hypotheses (fixed-tail mapping, inverse, uniform closure, continuity, differentiability) are open.
  None of this is an existence statement.

(i) Coupling on bounded collars of the x-axis (verified; also referee-audited, one model; corrections from both are
included).
- Setting: `5/2 < b < 7/2`, `0 < gamma' < 2`; a collar `I x (-d/2, d/2)`, `I = [x_1, x_2]` with `x_1 > 2d` (so it
  avoids the origin; the lemma concerns only the velocity and the coupling term, so the source P plays no role in it).
  Norm: with `I_t = [x_1 - t, x_2 + t]`, `N = (I_{2d} union -I_{2d}) x (-2d, 2d)` and
  `N_1 = (I_d union -I_d) x (-d, d)`, write `h = phi_e(y) c(x) + h_rem` on N, with a fixed smooth, odd, compactly
  supported edge profile `phi_e` equal to y near 0; the remainder `h_rem` is measured in `L^2(N, |y|^{-2b})`, the even
  edge coefficient c in `L^2`, and h outside `N_1` with the weight `(1 + |X|)^{-2 gamma'}`; the raw strain
  `sigma = psi[h]_xy(0)` (scaling term `sigma/3`) is a separate finite quantity, not implied by these norms.
- Velocity: with a fixed cutoff `chi_0(y)`, `U_i[h] = sum_{j<3} chi_0(y) y^j u_{i,j}[h](x) + R_i` on the collar, the
  edge coefficients of the near remainder in inhomogeneous `H^{b-j-1/2}` plus a smooth far part (the independent edge
  component `phi_e(y) c(x)` has trace bounds in `H^s` when the cut-off c belongs to `H^s`; for c only in `L^2` there
  is no regularity gain, the leading high-frequency `U_2` normal-trace multiplier being `-1`), `R_i` in
  `L^2(|y|^{-2b})` of the collar. The far part converges because the parity-symmetrized kernel decays like `|W|^{-3}`;
  this needs `gamma' < 2`.
- Coupling: `W[h].grad rho = chi_0(y) y q[h](x) + R_W[h]` with `R_W` in the collar's weighted space, for a background
  rho that is odd in y and `C^6` on a neighbourhood of the closure of N. The edge forcing q gains `b - 3/2`
  derivatives over the remainder of h; the near-remainder contribution to q belongs to `H^{b-3/2}`, and the
  independent edge contribution satisfies an order-zero estimate in this space provided the cut-off c belongs to
  `H^{b-3/2}`; such a bound does not follow from `L^2` edge data alone.
- Constants (interval arithmetic, two engines; `gamma' = 23/20`, `I = [1, 7]`, `d = 9/20`): near constant
  `K_n < 1211.755031744735` (`b = 3.403`) and `< 394.195496195032` (`b = 3`); far constants `A_0 < 1759.316412077765`,
  `K_f < 9345333.904801979607` (`b = 3.403`), `< 3561427.567789778522` (`b = 3`). These are large; the lemma gives
  boundedness, not a closing inequality.
- Corrections: the endpoint `gamma' = 2` fails, and finite strain does not follow from the collar norms alone
  (explicit examples).
- Not covered: the disc around P and its transition, the corner at the origin, the conic region at large x, the y-axis
  collars, derivative and Hoelder versions.

(j) Structure of the velocity at the y-axis (verified; also referee-audited, one model, after repairs). This is the
structural part of the y-axis analogue of 5(i); its near/far constants and the full remainder bound are not verified.
- Swap identities. With `(S h)(x, y) = h(y, x)`: `U_1 = S U_1 S` and `U_2 + I = -S U_2 S`. So the nonlocal part
  `U_2 + h` of the second component has the exchanged x-face kernel, and the full `U_2` keeps the local term `-h`.
- Edge smoothing. For `h = phi(x) e(y)` with phi even, smooth and compactly supported, the axis coefficients
  `v_{i,l} = d_x^l U_i(0, .)/l!` are Fourier multipliers in y. The full `U_2` (even l) maps `H^s -> H^{s+2}` and `U_1`
  (odd l) maps `H^s -> H^{s+1}`, for every real s, with constants
  `2 max(||phi^(l) - phi^(l)(0)||_inf, ||phi^(l+2)||_inf)/l!` and
  `sqrt(2) max(||phi^(l)||_inf, ||phi^(l+1)||_inf)/l!`, uniform at low frequency. If `phi = x^p` near `x = 0` (p = 2
  or 4), the maps for `v_{2,p}` and `v_{1,p+1}` are smoothing of every order; in `v_{2,2}` the local term cancels the
  leading part of the nonlocal term.
- Edge coupling. For a background even in x, vanishing on `x = 0` and in `W^{7,inf}` near a compact y-interval J, with
  `p_2 = rho_xx(0, y)/2`, `p_4 = rho_xxxx(0, y)/24`, the coefficients of `x^2` and `x^4` in `W[h].grad rho` along the
  axis are `q_2 = 2 p_2 (v_{1,1} + sigma/3) + p_2' (v_{2,0} + sigma y/3)` and
  `q_4 = 4 p_4 (v_{1,1} + sigma/3) + 2 p_2 v_{1,3} + p_4' (v_{2,0} + sigma y/3) + p_2' v_{2,2}`. On a bounded collar
  these maps send `L^2` edge data into `H^1(J)` and are therefore compact into `L^2(J)`; the strain term is separate
  and of finite rank when its functional is bounded. No statement is made on unbounded collars or for the whole
  coupling.
- Jets. Axis jets of weighted-`L^2` data are defined as coefficients of the weighted decomposition (unique, since a
  polynomial `sum_{l<6} x^l e_l(y)` in `L^2(|x|^{-2a})` near the axis, `5.5 < a < 6.5`, vanishes), not as classical
  traces (counterexample in section 4).

(k) Corner coefficients of the velocity and the corner coupling (verified; derived independently by a separate referee
and reproved by the verifier with exact algebra and two interval methods). Notation: `w_{a,b} = |x|^{-2a}|y|^{-2b}`
with `a, b > 0`, `S = a + b`; `T_x^N`, `T_y^N` remove the Taylor polynomials of order `< N` in x, resp. y.
- Expansion. For h even in x, odd in y, smooth and compactly supported away from both axes, near 0 one has
  `U_2 + i U_1 = i sum_{k odd} d_k z^k` with real `d_k` (`d_1 = -c`, c the strain). The corner coefficient
  `c_{i,l,j} = d_x^l d_y^j U_i(0)/(l! j!)` (degree `k = l + j` odd; l odd for `U_1`, l even for `U_2`) is the pairing
  of h with a kernel equal up to sign to `L_{lj} r^{-k-2} sin((k+2) theta)`, `L_{lj} = (k+1) binom(k, l)/(2 pi)`.
- Boundedness. No nonzero corner coefficient is bounded on the whole-plane `L^2(w_{a,b})`, for any real a, b
  (dilations of sector-supported data; at `S = k + 1` sums of disjoint dilates). The criteria below use `a, b > 0`;
  without an angular integrability condition the bounded-domain criterion fails (for example `a = -1`, `b = 5`,
  `k = 1`). For data supported in a bounded neighbourhood of 0 that contains a disc it is bounded iff `S > k + 1`; on
  the unit square `|c_{i,l,j}[h]| <= L_{lj} [J_k(a,b) 2^{S-k-1}/(2(S-k-1))]^{1/2} ||h||_{L^2(w_{a,b})}`, where
  `J_k(a,b) = int_0^{2 pi} |cos theta|^{2a} |sin theta|^{2b} sin^2((k+2) theta) d theta <= 2 B(a + 1/2, b + 1/2)`. On
  the composite weight `w_{a,b} (1 + r)^{2(S - gamma')}` it is bounded iff `S > k + 1` and `gamma' < k + 1`, with
  exact dual norm `L_{lj} [J_k(a,b) B(2(S-k-1), 2(k+1-gamma'))]^{1/2}`; the strain needs `gamma' < 2`. All 20
  coefficients of degrees 1, 3, 5, 7 and their norm enclosures were checked at
  `(a, b, gamma') = (129/20, 307/100, 1129/1000)`.
- Coupling coefficients. Let `rho = x^2 y alpha` near 0 with alpha of class `C^4` (evenness of alpha in x and in y is
  automatic in the parity class). The normalized coupling `G = U[h].grad rho + (c/3) X.grad rho` is even in x and odd
  in y, so its corner expansion has only odd degrees, with an `O(r^7)` remainder after degree 5. Its `x^2 y`
  coefficient is `J_c = 0` identically: the coupling never forces the corner mode `x^2 y`, which is the centre
  normalization seen in the linearization. Its `x^4 y` coefficient is `K_c = -alpha(0) d_3 - (2/3) c alpha_xx(0)`.
- Failure on the pure weight. For `rho = x^2 y`, the degree-7 homogeneous part `U^{(7)}` of the velocity gives
  `T_x^6 T_y^3 (2 x y U^{(7)}_1 + x^2 U^{(7)}_2) = -7 d_7 x^6 y^3` (the full velocity adds higher-degree terms), and
  the rescaled sources of section 4 make this remainder grow like `R^{S-8}` on `B_{1/2}` at constant norm. On the
  composite weight the degree-7 coefficient is bounded (previous item), so this particular obstruction disappears
  there.
- Double Taylor remainder (verified; first derived by a referee, then reproved by the verifier with a complete
  enumeration of the nine small/comparable/large source-target scale configurations). Let T be a convolution operator
  bounded on `L^2(R^2)` whose kernel off 0 is smooth and homogeneous of degree -2 with
  `|d_1^p d_2^q K(Z)| <= D_pq |Z|^{-2-p-q}`. If `N - 1/2 < a < N + 1/2` and `M - 1/2 < b < M + 1/2` (zero orders
  allowed), then `T_x^N T_y^M T`, defined on smooth data compactly supported away from the axes, extends to a bounded
  operator on `L^2(w_{a,b})`, with an explicit constant valid for arbitrary aspect ratios; the conormal derivatives
  `x d_x`, `y d_y` commute with the Taylor projections, and their commutators with T are again such operators with
  explicitly bounded kernels. For the IPM velocity at `(N, M) = (6, 3)` the constant is below `4.725e17` at
  `(a, b) = (6.45, 3.07)` and below `1.114e18` at `(6.495, 3.403)`. Effective, but far too large for a closing
  inequality; numerical constants for the derivative versions were not instantiated. The bounded extension does not
  bound the velocity itself or its individual corner coefficients on this weight (previous items).
- Annular velocity traces (verified, with a separate referee audit). For `5.5 < a < 6.5` and `2.5 < b < 3.5` the nine
  naturally subtracted traces of the `(6, 3)` double Taylor splitting satisfy dyadic annular Sobolev bounds with
  explicit constants; the proof treats nearby, distant and comparable source annuli, all six y-normal orders and the
  local identity term. Only the renormalized trace combination extends to the global pure-weight completion: seven
  of the nine rectangular subtractions are unbounded in this window (two are bounded), so the individual canonical
  moments are not continuous there. Numerical constants are instantiated only at the two weight pairs above.
- Local corner coupling for a smooth factor (verified, with a separate referee audit). Let `B_d` be the disc of
  radius `d = 1/2`, `Q_1 = (-1, 1)^2`, `rho = x^2 y alpha` near 0 with alpha of class `C^8`, and
  `G = W[h].grad rho`, `W[h] = U[h] + (c[h]/3) X`. For `5.5 < a < 6.5` and `2.5 < b < 3.5` the double remainder
  `T_x^6 T_y^3 G` is bounded on `B_d` in `L^2(w_{a,b})` by the pure-weight norm of h for h supported in `Q_1`, and by
  the composite norm `L^2(w_{a,b} (1 + r)^{2(S - gamma')})` for arbitrary h when `1 < gamma' < 2`. The constants are
  multiples of `||alpha||_{C^8}`; at `gamma' = 1.129` the composite constants are below `2.039e14` at
  `(a, b) = (6.45, 3.07)` and below `6.218e14` at `(6.495, 3.403)`. The proof reduces the variable factor, through an
  exact Taylor multiplier expansion, to the lower-order operators of the previous item. No smallness. It does not
  apply to the present trial, whose factor is not of class `C^2` at 0 (section 4).
- Not verified: derivative versions of these bounds and the corner edge matching.

(l) Global characteristic flow and the pure transport inverse (verified as conditional statements, with their own
proofs and two interval methods for the constants; audited twice by a separate referee, one model each; repairs from
all three are included). Let `V = c_l X + U` be a complete `C^1` field on the closed quadrant with both axes
invariant, at most linear growth and `div V = 2 c_l`, with flow `phi_t`; let `A_tr = V.grad - 1` (the transport part
of L) act on its maximal distributional domain in a weighted `L^2`.
- Flow. Assume: `V_1(x, 0) < 0` for `0 < x < x_*` and `> 0` for `x > x_*`; `DV(0) = diag(-A, D)` with `A, D > 0` and
  `DV(P)` with positive diagonal; `X.V >= kappa_0 |X|^2` for `|X| >= R_0`; and either the equilibria of the closed
  quadrant are only 0 and P with `V_2(0, y) > 0` for `y > 0`, or `V_2 >= m_0 y` on the open quadrant for some
  `m_0 > 0`. Then every orbit of the open quadrant tends to P as `t -> -inf` and to infinity as `t -> +inf` (in the
  second case `y(phi_t X) >= e^{m_0 t} y(X)` for `t >= 0`), crosses a global section once, and spends a uniformly
  bounded total time outside fixed neighbourhoods of 0, P and infinity. Orbits near the incoming separatrix spend
  unbounded time in a box at the saddle, so the neighbourhoods must be chosen inside the region where the weight
  margin below is already negative.
- Transport inverse. For a positive `C^1` weight `w_0` let `T_0 = -(1 + c_l) - (1/2) V.grad log w_0`, so that
  `Re <A_tr h, h>_{w_0} = int T_0 |h|^2 w_0`. For `kappa > 0` let `C_kappa` be the supremum over orbit segments of
  `int 2 (T_0 + kappa) dt`. If `C_kappa < inf`, then `||A_tr^{-1}||_{L^2(w_0)} <= e^{C_kappa/2}/kappa`.
- Box-crossing cost. Suppose y is nondecreasing along orbits and finitely many boxes
  `B_i = [x_{1,i}, x_{2,i}] x [0, y_{2,i}]` (`0 < x_{1,i} < x_{2,i}`) carry `V_1 <= -v_i < 0` (respectively
  `V_1 >= v_i x > 0`). Then each orbit visits `B_i` during one time interval, of length at most
  `t_i = (x_{2,i} - x_{1,i})/v_i` (respectively `log(x_{2,i}/x_{1,i})/v_i`), and, with `tau_i >= 0`,
  `T_0 + kappa <= sum_i tau_i 1_{B_i}` gives `C_kappa <= 2 sum_i tau_i t_i`. No equilibrium enumeration and no strict
  positivity of `V_2/y` are needed for this estimate.
- Instance (conditional; its inequalities are floating-point facts, not certified). For the conic weight
  `w_0 = |cos theta|^{-2a} |sin theta|^{-2b} M(r)`, `-(1/2) r M'/M = gamma' + (a + b - gamma')/(1 + (r/6)^4)`, at the
  working exponents, and the single box `[4.80, 6.82] x [0, 2.85]` with `V_1 <= -13` there, `T_0 <= 1.23` there and
  `T_0 <= -0.22` elsewhere: the bound is `5 exp(1111/5000)`, in `(6.244, 6.245)`, at `kappa = 1/5`, and
  `(50/11) exp(2929/13000)`, in `(5.694, 5.695)`, at `kappa = 11/50`. The analysis's first rounding of the former to
  `6.2` was wrong and is withdrawn. The floating-point margins of the trial's velocity on a `3000 x 256` grid are
  `sup T_0 = 1.226` and maximal segment cost 0.147 at `kappa = 0.2` (not reproduced).
- Far lower bound. If `U = O(r^k)` on sectors and `w_0 ~ r^{-2 gamma'} b(theta)` at infinity, then
  `||A_tr^{-1}||_{L^2(w_0)} >= 1/kappa_inf`, `kappa_inf = 1 + c_l (1 - gamma')`, which lies in `(0.2807, 0.281)` at
  `gamma' = 1129/1000` and the exact k of the trial. So no weight of this type gives a transport inverse below 3.55.
  This bounds the transport part only, not the coupled inverse.
- Exterior certificate for the trial (verified bound; two interval methods, all 261 velocity modes, homogeneous
  transients retained). For the exactly normalized modal trial, `X.V > 3.83 r^2` for `r >= 3634`. For `r >= 4000`:
  `|U_r/r| < 0.104 (4000/r)^{1-k}`, `|U_1/x| < 0.313 (4000/r)^{1-k}` and `|U_2/y| < 0.313 (4000/r)^{1-k}` (continuous
  extensions on the axes), `X.V > 5.47 r^2`, and `V_1/x > 5.26`, `V_2/y > 5.26`. This is the far hypothesis of the
  flow statement for the trial, and the uniform quotient tail used for the end values at infinity.
- Radial defect criterion (verified as an abstract statement; a limited instance below). For the angular mode l of the
  canonical stream function and `t = log r`, `P = l psi/r^2` and `R = psi_r/r` satisfy `P' = -2P + l R` and
  `R' = l P - 2R - f`, f the corresponding mode of the right-hand side, so `q_+ = P + R` and `q_- = P - R` solve
  `q_+' = (l - 2) q_+ - f` and `q_-' = -(l + 2) q_- + f`. On a cell `t = t_a + u`, `0 <= u <= h`, let
  `q' = lambda q + g` with real lambda (`lambda = 0`, the case `l = 2` for `q_+`, is included), p a `C^1` candidate
  with `|q(0) - p(0)| <= eps_0`, and `|g + lambda p - p'| <= sum_j D_j u^j` with `D_j >= 0`. Then
  `|q(u) - p(u)| <= eps_0 e^{lambda u} + sum_j D_j J_j(lambda, u)`,
  `J_j(lambda, u) = int_0^u e^{lambda (u - v)} v^j dv`; each `J_j` increases in u, so
  `eps_0 e^{max(lambda, 0) h} + sum_j D_j J_j(lambda, h)` bounds the error on the whole cell. The moments have a
  signed exponential-series enclosure with an exact geometric tail; the bound is tested against the Taylor-model
  radius. It is a route to the modal Taylor models of the flow certificate on the finite annulus. Limited instance
  (verified, two interval engines with separate methods and a high-precision spot check of five modes in each of the
  three cells; also checked by separate referee reviews): on the middle cells 0, 4102 and 7808 (of 7809) the radial
  Taylor-model coefficients and remainder bounds of the flow certificate are enclosed for all 261 modes, and an exact
  linkage check of 6264 saved boxes between two stages of the certificate passes. On the nine rectangles formed by
  these three cells and three angular cells, the composition of the modal models into `s`, `v_2`, `v_1` and T with its
  complete product remainder is enclosed by two independent methods (verified: exact rational Bernstein enclosures and
  interval de Casteljau subdivision), and each independent reference enclosure is contained in the corresponding
  reported range. An accepted correction of one sentence of an earlier review record, which had stated this
  containment in the reversed direction, leaves the computed enclosures, inequalities and reported ranges unchanged.
  The composition is conditional on its finite input boxes; their canonical input membership is verified below for the
  distinguished exactly normalized trial, on these rectangles only. For all 7809 middle cells, including these three,
  the exported Green boundary intervals are verified to contain the canonical values (section 8; the archive condition
  of this membership is discharged, section 2, shared interval archive); this boundary membership alone upgrades none
  of the conditional statements above. Separately (verified, two methods; also checked in referee reviews of the proof
  and of the completed results), on all 7809 middle cells every exported density polynomial box, that is, every box
  for a Taylor coefficient at the exact cell left end of one of the 260 modal spline amplitudes of the trial in
  `t = log r` (eight powers each, 16242720 boxes), contains the exact coefficient: by exact rational B-spline
  arithmetic, and by an outward interval reconstruction through the exact angular inversion from the density
  polynomial balls of the shared archive, which are themselves verified to contain the exact polynomials of the trial
  on all 1558 knot spans. The moment values of the archive are not covered by this check. Combining these memberships
  with the three-cell instance (verified, with its own derivation of the canonical modal equations, in which the
  canonical integral definitions fix the homogeneous constants, and of their unique solvability, exact comparisons of
  every input entry of the three cells with the verified source arrays, exact rational checks of the cell coordinates
  and lengths, three independent enclosures of `e^t` at each of the three cell left ends, and two exact constructions
  of all 6264 forcing-box images; the inherited coefficient and remainder calculations of the instance were not rerun;
  also checked in referee reviews of the proof, the outputs and a follow-up): on the middle cells 0, 4102 and 7808,
  for all 261 modes and on each whole exact cell, the radial Taylor models of the instance enclose the canonical
  quantities `P = l psi/r^2` and `R = psi_r/r` of the trial, and their coefficient boxes contain the exact Taylor
  coefficients at the cell left end. This was first verified conditional on the shared archive containing the
  canonical scaled moment values in its declared balls, which was the only open canonical input membership, given the
  exactly normalized modal trial, the fixed saved artifacts and the accepted analytic and arithmetic dependencies of
  the three composed results; no additional hypothesis about the cell coordinates, the values of `e^t` at the cell
  left ends, the cell lengths or the forcing boxes remains for these three cells. The archive's moment values and the
  composition of their verification with this instance are verified (section 8), so this condition is discharged. This
  conclusion concerns the accepted runtime radial Taylor models of degree 12, with their order-20 remainder refinement
  and coefficient enclosures of orders 0 through 12. All statements in this report about the flow certificate's radial
  Taylor models refer to these runtime models; identity with the arrays used in the historical numerical flow
  computation is not established. For the distinguished exactly normalized trial, the canonical flow fields `s`,
  `v_2`, `v_1` and T, with the axis quotients taken as their continuous extensions, lie in the certificate's 36
  reported ranges on these nine closed rectangles (verified, with exact matching of the radial, angular and scalar
  inputs against their verified sources, re-evaluation of all 7047 cubic remainder inequalities in two exact rational
  implementations and two interval engines for the geometry; the modal products of the composition were not
  recomputed; also checked in a referee review; section 8). This discharges the input-box condition of the composition
  on these rectangles only, under the same hypotheses on the runtime models. Complete radial instance (verified, two
  complete interval methods with different constructions, an independent output audit with a third method on selected
  modes of every cell and five complete replay cells; also checked in a completed referee review and a separate
  adjudication): on all 7809 middle cells, for all 261 modes and for every choice of the inputs in their finite boxes,
  the runtime degree-12 radial Taylor models with their remainder budgets enclose the solutions of the radial modal
  equations on each whole cell (52991874 coefficient and 4076298 remainder containments in each method, with all
  16305192 forcing coefficients checked exactly against their images). In the first method, for twelve constant
  coefficients `R_0` (twelve modes), the original ball enclosure did not fit inside its target; an exact rational
  endpoint refinement (the range of each of the two terms of the coefficient formula over the input box is attained at
  endpoint pairs of its input intervals) gave containment, and no target or remainder budget was changed; the second
  method passed every containment without refinement. The third method also needed independently computed endpoint
  refinements at the same twelve constant coefficients. For the distinguished exactly normalized trial (verified, with
  a complete exact reader that identifies every input array and scalar cell record of the computation with the
  verified sources and all 7810 cell boundaries with the partition, two exact constructions of the forcing weights and
  of the canonical radial equations, and the boundary and density memberships above with the archive condition
  discharged; also checked in a completed referee review and a separate adjudication), on every closed middle cell and
  for all 261 modes these models enclose the canonical quantities `P = l psi/r^2` and `R = psi_r/r`. At an original
  spline knot the coefficients are those of the right-hand polynomial continuation; no analyticity across knots is
  asserted. The angular linkage beyond the tested rectangles and the full flow certificate (the angular products, the
  classification of the spatial boxes and the flow inequalities) remain open.
- Axis jets of the transport (verified, with its own proof, exact symbolic identities and explicit counterexamples;
  audited by a separate referee, single model; a second referee derivation agrees with the P-row statement). For a
  solution of `(V.grad - 1) h = f` that is regular near the x-axis, the jet `b(x) = h_y(x, 0)` satisfies
  `w b' + (mu - 1) b = f_y(x, 0)`, with `w = V_1(x, 0)` and `mu = d_y V_2(x, 0) = 2 c_l - w'`.
  - At P (`w = 0`): `(mu_P - 1) b(P) = f_y(P)`. At an exact solution with `rho_y(P) != 0`, `mu_P = 1` (source
    eigenvalues, below), so this jet transport is not onto any forcing space containing data with `f_y(P) != 0`. For
    the trial (`mu~ - 1 = -2.25e-8`) any inverse of it has norm at least `||eval_P||_Y/(|mu_P - 1| ||eval_P||_X)`; the
    value `1/|mu_P - 1| = 4.4e7` holds for normalized evaluations. The P-row of the full linearization contains in
    addition the coupling and strain terms at P, so this is not a pole of the coupled inverse; it shows only that the
    transport jet cannot carry the P-row.
  - At the corner, for perturbations divisible by `x^2 y`, the cubic coefficient is multiplied by
    `-2A + D - 1 = 0` (because `D = 2A + 1`): the cubic forcing coefficient must vanish, and the cubic solution
    coefficient is a normalization.
  - Near P the homogeneous jet solution behaves like `|x - x_*|^{-(mu_P - 1)/A_P}`. A zero `x^2` coefficient at 0
    removes this mode on `(0, x_*)`. It does not control a separately continued branch beyond P, which is not `C^1`
    when the exponent lies in `(0, 1)`.
  - With `mu_P = 1` and H the homogeneous solution with `H/x^2 -> 1` at 0, the normalized solution on `(0, x_*)` is
    `b = H int_0^x f_y/(w H)` for `f_y = O(x^4)` at 0. With `F(x) = f_y(x, 0)`, the Dini condition
    `int |F(x)|/|x - x_*| dx < inf` near P is sufficient for a finite value at P, and if F itself is `C^1` with
    `F(x_*) = 0` the endpoint is `C^1` (a `C^1` PDE forcing does not imply this for its row F); necessity is not
    claimed. For merely continuous forcing with `f_y(P) = 0` the endpoint claim is false: an explicit rational flow
    with `f_y ~ 1/log(e/(x_* - x))` gives a divergent integral.
  - Origin matching (verified, 21:44). With `Phi/x^2 -> 1` at 0 and `R = f_y - J h` (J the coupling at the axis),
    the jet coefficient is `beta = b(x_1)/Phi(x_1) - int_0^{x_1} R/(w Phi)`. Absolute integrability of the integrand
    is a sufficient condition (it holds for example under a Dini modulus or `R = O(x^{2 + nu})`); `R/x^2 -> 0` alone
    does not suffice (an exact `log log` example). Adding the scaling vector removes its own direction only if K lies
    in the domain; at a trial `L K = (1 - X.grad) eps~`, so this adjustment changes the forcing.
  - Velocity of a transverse jet extension (verified, 21:53). For `h = y chi(y) b(x)` with chi even, `C^2`, compactly
    supported and equal to 1 near 0, put `I_chi(a) = int_0^inf z chi(z) e^{-a z} dz`. Then `U_1[h](x, 0) = B_chi b`
    and `d_y U_2[h](x, 0) = -P_chi b`, with x-Fourier multipliers `B_chi(k) = -i k I_chi(|k|)` and
    `P_chi(k) = k^2 I_chi(|k|)`; the strain is `-(P_chi b)(0)`. Here `P_chi = Id - S_chi`; `B_chi` gains one
    derivative and `S_chi` every finite order, but `S_chi` is not compact on the line (translated packets). The
    induced axis coupling is `N_chi b = G_1' B_chi b - G_1 P_chi b - (x G_1' + G_1)(P_chi b)(0)/3`, nonlocal, with
    leading local multiplier `-G_1`. For the even `C^2` cutoff supported in `[-2, 2]` and equal to 1 on `[-1, 1]` of
    the proof: `C_B = 3/pi < 0.955`, `C_S < 5.93`, and the `H^s -> H^{s+1}` bound of `B_chi` is below 1.617. With a
    bounded extension from a finite interval away from the zeros of w, the jet equation has a two-sided inverse of
    norm at most `M/(1 - M n)` when `M n < 1` (M the transport inverse, n the coupling bound). No trial-specific M, n
    is claimed.
  - Block bound (conditional): order the unknowns and equations as (remainder, jets). With two-sided inverses of
    norms `M_J` (jets) and `M_r` (remainder), a bounded upper-right block (the action of the jets on the remainder
    equation) of norm `b_*` and a zero lower-left block (the jet equations do not involve the remainder), the
    sum-norm inverse is at most `max(M_r, (1 + M_r b_*) M_J)`. None of these is available for the trial.
- Axis crossing cell for the trial (verified bound; two interval methods and a third audit integration; also checked
  by a separate referee review). On the exact logarithmic radial cell of the residual certificate that contains `p`
  (radii about 8.59867 to 8.60689), `10.1494 < w' < 10.1525` with `w = V~_1(x, 0)`, and `x w` has strict opposite
  signs at the two ends of the cell, so `V~_1(x, 0)` has exactly one zero there. The statement is restricted to the
  exact cell. It is a local piece of the bounded-region hypotheses below.
- Pure transport at a source (verified, with its own proof, exact identities and two interval methods; first derived
  in a separate referee audit and checked by a second referee review). On the frozen source chart let
  `T = A s d_s + y d_y - 1` with `A > 0` (s the coordinate along the x-axis, centred at P). For a smooth step chi (0
  for `s <= 1`, 1 for `s >= 2`), `phi = s chi'(s)`, an even cutoff `psi = 1 - chi(|y|)` and the smooth compactly
  supported forcing `f = y phi(s) psi(y)`, the unique solution along the characteristics that vanishes beyond the
  forcing is `h = -int_0^inf e^{-t} f(e^{A t} s, e^t y) dt`. It is compact and continuous, `h = -(y/A) Q(y s^{-1/A})`
  for `0 < s < 1` with Q smooth and not constant, and `h = 0` for `s <= 0`. Hence `h_y(s, 0) = -1/A` for `0 < s < 1`
  and 0 for `s <= 0`: h has no `C^1` representative and is not in `H^sigma_loc` for `sigma > 2`, and for `A >= 3` it
  is not in `H^1_loc`. The example extends using a smooth compactly supported divergence-free field U with the
  parities; the drift `V = c_l X + U` then has two reflected source patches. It concerns the transport part only and
  is not a defect of the full inverse; it is the reason why the remainder block near P must keep the nonlocal term
  (5(a), 5(b)).
- Source eigenvalues (verified; first derived in a separate referee audit and checked by us). At an equilibrium P of
  an exact solution with `rho, V in C^1` near P, `DV(P)^T grad rho(P) = grad rho(P)`. On the positive x-axis with the
  parities and `rho_y(P) != 0` this gives `mu_P = 1`, and with `div V = 2 c_l` also `A_P = 2 c_l - 1`. No second
  derivative of rho is used.
- Flow ends for the trial (verified bound; two interval methods and a third audit; the velocity moment majorants are
  shared with the earlier verified certificates). For the exactly normalized modal trial put `v_1 = V_1/x`,
  `v_2 = V_2/y`, `s = X.V/r^2` and `T = -1 - c_l + 6.45 v_1 + 3.07 v_2 + (mu - 9.52) s` with
  `mu = 1.129 + (9.52 - 1.129)/(1 + (r/6)^4)`; T is the margin `T_0` of the conic weight of the instance above at the
  working exponents `(a, b) = (6.45, 3.07)`, `gamma' = 1.129`.
  - On the whole inner disc `0 < r <= e^{t_a}` (about 0.00765142460138): `v_2 > 21.289`, `v_1 < -10.138` and
    `T < -6.53`.
  - On `r >= e^{t_b + 9}` (about 2.76555569e7): `s > 5.5752`, `v_1 > 5.5752`, `v_2 > 5.5752` and `T < -0.278`.
  - On `r >= e^{t_b + 5}` (about 5.0653e5; certified `20 < e^{t_b + 5} < 510000`), including both axes: `s > 5.57`,
    `v_1 > 5.57`, `v_2 > 5.57` and `T < -0.22` (verified, with its own proof: the verified velocity decay of the
    exterior certificate above from `tau = log r - t_b = 1` on, `|s - c_l| <= A_s e^{-omega (tau - 1)}` and
    `|v_i - c_l| <= A_v e^{-omega (tau - 1)}` with explicit rational constants and `omega = 1 - k`, is transferred to
    `tau >= 5`, and the identity `T = -1 + (mu - 1) c_l + 6.45 (v_1 - c_l) + 3.07 (v_2 - c_l) + (mu - 9.52)(s - c_l)`
    with `mu` decreasing in r gives the bound; the scalars are evaluated by two independent methods, ball arithmetic
    and exact rational enclosures of the exponentials by positive Taylor series with a geometric tail). Since the box
    of the instance lies in `r < 20`, this is the off-box margin `T_0 <= -0.22` of the instance there.
  - Every radial coefficient of the trial, including its scalar normalization repair, keeps the factor `x^2 y`. Hence
    `rho`, `rho_x` and `rho_y` vanish exactly on the y-axis, and `b+ = (|grad rho| - rho_y)/2` is exactly zero there.
    This cancellation gives neither an inverse nor an energy gap.
  These cover the two ends of the flow. The finite annulus `e^{t_a} < r < e^{t_b + 5}` is not covered by them.
- Not covered: the bounded-region hypotheses for the trial on the finite annulus `e^{t_a} < r < e^{t_b + 5}` (signs on
  the axes, `V_2 >= m_0 y`, the box and complement margins; their interval certification is incomplete: the verified
  canonical ranges on the nine closed rectangles above do not provide a full angular or annular cover; section 8); a
  smooth weight (the orbit-corrected weight `w_0 e^psi` is only measurable across orbits, so it cannot serve in a
  Garding argument); the coupled axis-jet system; any inverse of L.

(m) Far domain and y-axis jets of a jet-plus-remainder realization (verified as conditional statements, with their
own proofs and interval constants; the statements were first derived in two separate referee audits). They concern
the proposed realization of section 10: y-axis jets `x^2 a_2(y) + x^4 a_4(y)` plus a weighted remainder, with
natural far space `H_gamma = L^2(<r>^{-2 gamma})`.
- Far exclusions. For a nonzero exact profile with rho and U of class `C^1`, `c_l > 1`, `U = o(r)` and `div U = 0`,
  `rho` is not in `H_gamma` for `gamma < 1 + 1/c_l` (transport of a compact patch along the flow, with Jacobian
  `e^{2 c_l t}`). Under the sublinear `P_2` bound, `X.grad rho` and `K = rho - X.grad rho` are not in `H_gamma` for
  `1 < gamma < 1 + 1/c_l` (radial Hardy inequalities in logarithmic radius, constants `1/(gamma - 1)` and
  `1/(2 - gamma)`).
- Compact-core obstruction. A smooth compactly supported h with the parities, vanishing near both axes and near the
  origin, can have `c[h] > 0` (explicit example with `c[h] > 1.33e-7`). Outside its support
  `L h = U[h].grad rho + (c[h]/3) X.grad rho`. The first term lies in `H_gamma`, since
  `|U[h]| <= (4/pi) ||h||_{L^1}/r^2` far away; the second does not. So no domain containing such h is mapped by L into
  a forcing space embedded in `H_gamma`; a far scalar direction (a logarithmic tail) is the repair proposed in section
  10, under additional leading-tail and domain hypotheses. The jet-plus-remainder far norms embed into `H_gamma`; K is
  not in that space; the canonical velocity is scaling covariant (div-curl uniqueness under sublinear growth and
  parity). No index or kernel dimension follows.
- Jet velocity. Write `h = x^2 a_2(y) + x^4 a_4(y) + ...` near the y-axis and `B = U_2[h](0, .)`, so that
  `B^(eta) = |eta| int_0^inf e^{-|eta| z} h^(z, eta) dz` (Fourier transform in y). The x-Taylor coefficients of U[h]
  at the axis are `u_0 = B`, `u_2 = -a_2 - B''/2`, `u_4 = -a_4 + a_2''/12 + B''''/24` for `U_2` and `u_1 = -B'`,
  `u_3 = a_2'/3 + B'''/6`, `u_5 = -u_4'/5` for `U_1`, and `c[h] = B'(0)`. These identities are stated for smooth
  compactly supported h, and for noncompact h when the canonical velocity exists, is sufficiently differentiable and
  the expansions are justified; no extension to a conormal completion is asserted.
- Rows. For the cubic identity assume that rho and h are locally `C^3`, that `rho = x^2 y + o(r^3)` and
  `h = b x^2 y + o(r^3)`, that their canonical velocities are locally `C^1`, and that `3 c_l - c[rho] = 1`; then
  `[x^2 y] L h = b(3 c_l - c[rho] - 1) - c[h] + c[h] = 0` for arbitrary b, so h need not be normalized. In the smooth
  `x^2` row the three normalized coupling coefficients cancel (`-2c[h] + c[h] + c[h] = 0`). Let
  `T_j a = v a' + (2j u - 1) a` (`j = 1, 2`) be the diagonal operator of the `x^{2j}` row, with
  `u = c_l + partial_x U_1[rho](0, y)` and `v = V_2(0, y)`, and assume `c_l > 1` (`k = 1/c_l`), u even and v odd and
  smooth near 0, `v > 0` for `y > 0`, `v = D y + O(y^3)` and `u = -A + O(y^2)` near 0, and `v = c_l y + O(y^k)` and
  `u = c_l + O(y^{k-1})` at infinity, with the derivatives needed for the expansions used. For a known diagonal
  forcing F, smooth and odd near 0 and locally smooth on the positive axis, `1 < gamma < 1 + k` and the far norm
  `int_R^inf y^{4j + 1 - 2 gamma} |a|^2 dy` of the `x^{2j}` row (forcing in the same far space), the row has a unique
  solution in that far space, `a(y) = -H_j(y) int_y^inf F(z)/(v(z) H_j(z)) dz`, where `p_j = (2jA + 1)/D` (so
  `p_1 = 1` and `p_2 = 2 - 1/D`; for the normalized background `A = 2c_l - 1` and `D = 4c_l - 1`) and the positive
  homogeneous solution `H_j` is normalized by `H_j(y)/y^{p_j} -> 1` at 0, while `H_j(y)/y^{k-2j}` tends to a positive
  finite constant at infinity, with explicit weighted bounds. Decay alone does not select it: the homogeneous
  solutions also decay (`k < 1`), but their far norm diverges. The `x^2` row needs `F'(0) = 0` for `C^1` regularity,
  and an integral condition if the cubic coefficient of the perturbation is normalized. In the `x^4` row, with
  `S = F'(0) y chi/(D(1 - p_2))`, where chi is smooth, even, compactly supported and equal to 1 near 0, the finite
  integral `int_0^inf (F - T_2 S)/(v H_2) dy` does not depend on the cutoff chi, and under these hypotheses its
  vanishing is equivalent to a smooth odd local extension of the far-selected solution; the bare integral can diverge
  even for a smooth admissible solution. The excluded homogeneous mode `y^{p_2}`, `p_2 = (4A + 1)/D = 2 - 1/D`, is not
  in `H^s` for `s >= p_2 + 1/2` (equality included); at the trial's k, `p_2` lies in
  `(1.953054839965, 1.953054839966)`.
- Tail coordinates and the scalar row (verified as conditional statements). Near the y-axis
  `r^k Theta = theta_2 x^2 y^{k-2} + (theta_4 + (k - 2) theta_2/2) x^4 y^{k-4} + ...`, and the logarithmic tail adds
  `theta_2 y^{k-4}/2` to the `x^4` jet. The direction `Theta_1 = sin theta cos^2 theta (1 + (3 - k) cos^2 theta/2)`
  has a nonzero angular `cos^4 theta` coefficient but a zero Cartesian `x^4` jet (its `x^6` coefficient is nonzero),
  so a condition on angular coefficients is not a condition on jets. Removing the `x^2` and `x^4` jets can make the
  angular remainder integrable at the axis while the radial `r^k` tail still diverges in the remainder norm; the tail
  directions must be carried as full functions. Consider the block map
  `(h, kappa, tau) -> (A h + a kappa + b_tau tau, d(h) + m kappa + n tau)` between Banach spaces (the space of h
  possibly an established graph domain), with A and d bounded linear, `a` and `b_tau` in the target space and the far
  scalar row given by `d(h) = k c[h]/3`, `m = c_l + k c[q]/3`, `n = k c[t]/3` (q the logarithmic tail, t the
  tau-profile). If `m != 0`, eliminating kappa gives `T = A - a d/m` and the reduced column `b = b_tau - (n/m) a`. If
  T is injective with closed range of codimension one and `ell_0` spans its cokernel, the bordered operator is
  invertible iff `ell_0(b) != 0`, with explicit two-block and bordered inverse bounds under stated reference
  isomorphisms and Neumann-series hypotheses; energy inequalities alone give no onto statement. The cokernel and the
  value of `ell_0(b)` are open. Also confirmed: for a fixed compactly supported transverse cutoff chi equal to 1 near
  0, the y-axis trace multiplier of `x^{2j} chi(x) a(y)` is `M_j(nu) = nu int_0^inf e^{-nu x} x^{2j} chi(x) dx`,
  `nu = |eta|`, with leading high-frequency terms `2 nu^{-2}` and `24 nu^{-4}` for the `x^2` and `x^4` jets
  (exponentially small cutoff error), the half-plane strain kernel `c[h] = int_{x>0} 2y(3x^2 - y^2)/(pi r^6) h`, and,
  for the remainder weight `x^{-2a} (1 + r^2)^{a - gamma}` at `a = 6`, `gamma = 1.129`, a dual norm of the strain
  functional in `(0.13462722415340, 0.13462722415341)` (a norm of the moment functional, not a velocity bound on the
  completed space). Membership of the scaling direction `K - (1 - k) t_0`, with `t_0 = chi r^k Theta_0` the solution's
  own leading tail, in the conormal graph domain is an additional hypothesis; the radial bounds give only zeroth-order
  far membership.
- Scope. These are diagonal constraints on the forcing F of each row, which contains coupling terms in h; they are not
  cokernel functionals of f alone. Coupled trace bounds, the Fredholm property, the index and any inverse are open.

(n) Obstructions at lower Sobolev order (verified, with their own proofs, exact identities and two interval methods;
first derived in a separate referee audit and checked by us). They concern the lower-order variant of the proposed
realization of section 10, in which existence would be proved at a local order `2 < s < 3` and then upgraded.
- Local regularity does not propagate. For the frozen source operator `L_P = A s d_s + y d_y - 1 - g M` (nonlocal term
  kept) let n be odd, `p = (g + 1 - n)/A > 1` nonintegral, `b_0 = 1`,
  `b_{j+1} = -[(g + 2j(A - 1))(n - 2j)(n - 2j - 1)] / [2(j + 1)(A - 1)(p + 2j + 2)(p + 2j + 1)] b_j`, and
  `H_n = sum_{j <= (n-1)/2} b_j |s|^{p + 2j} y^{n - 2j}`. For a smooth product cutoff chi, `L_P(chi H_n)` is harmonic
  where `chi = 1`, while `chi H_n` lies in `H^t` exactly for `t < p + 1/2` (failure at equality). With the trial's
  constants, `n = 7` gives a function in `H^{2.5}` but not in `H^{3.1}`, and `n = 11` one that is not `C^2`. The
  forcing outside the cutoff is rough, so this does not contradict a global inverse; it shows that an upgrade needs
  injectivity and high-order surjectivity of one and the same operator on specified nested domains.
- Nonlinear identity. With `V[u] = X/3 + Gamma u` (`Gamma u = U[u] + (c[u]/3) X`), the exact equation for
  `rho = rho~ + h` is `A_h h = -f_0` with `A_h u = (V[rho].grad - 1) u + (Gamma u).grad rho~` and `f_0 = F(rho~)`,
  while `DF(rho) h = -f_0 + (Gamma h).grad h`. A high-order inverse of `DF(rho~)` is therefore not surjectivity of
  `A_h`, whose coefficients are only as smooth as the low-order solution.
- Strain functional. On `H^sigma(R^2)` (unitary Fourier transform), also on its even-x odd-y subspace, the functional
  `c[f] = psi[f]_xy(0)` has norm exactly `1/(8 sqrt(pi (sigma - 1)(sigma - 2)))` for `sigma > 2`. It is unbounded on
  `H^2`, and for `0 <= t < 2` it is unbounded even on smooth perturbations vanishing near the origin (dilates
  `eps^{t-1} phi(X/eps)` with `c[phi] != 0`). So the unaugmented low space `H^{s-1}`, `2 < s < 3`, does not control c,
  and a general bilinear estimate for `(Gamma e).grad u` in that space fails.
- Factorization. `rho_eps = chi(r) x^2 y r^{-eps}` is in `C^{2, 1-eps}` and in `H^sigma` for `sigma < 4 - eps`, but
  `rho_eps/(x^2 y)` has no continuous extension at 0 (for `eps = 1/4`: `C^{2,3/4}` and `H^{3.1}`). The continuity of
  the factor must come from the realization or the equation, not from regularity.
- Interpolation. `||v||_{H^s} <= ||v||_2^{1 - s/3} ||v||_{H^3}^{s/3}` for `0 <= s <= 3`, with constant 1, and an
  explicit Leibniz bound for the `H^3` norm of `chi f` from cellwise derivative bounds when f has genuine weak
  derivatives through order 3.
- Weight window. With `D = 2A + 1` and `c_0 = (A + 3)/2`, the conditions `9/2 < a < 13/2` and `-c_0 - aA + sD < 0`
  hold together exactly when `max(9/2, 2s - 1/2 + (s - 3/2)/A) < a < 13/2`; for a given `2 < s < 3` this is nonempty
  exactly when `s < (14A + 3)/(4A + 2)`, for every such s exactly when `A >= 3/2`; at `s = 5/2`, `a = 5` the rate is
  `1 - A/2`. Annular corner norm: with a fixed nonzero smooth radial cutoff `chi_A` supported in `1/2 < r < 2`,
  `N_{a,s}(u)^2 = sum_{j >= j_0} 2^{2j(a+s-1)} ||chi_A(Z) u(2^{-j} Z)||_{H^s_Z}^2`. A homogeneous term `r^m F(theta)`
  with `0 < ||chi_A r^m F||_{H^s} < inf` lies in this norm exactly when `m > a + s - 1`; equivalence of that norm with
  other fractional corner norms is not claimed.

(o) Local a priori estimate and auxiliary inverse at the source at order 31/10 (verified conditional theorems, with
their own proofs and interval arithmetic; first derived in a referee audit; also checked by separate referee reviews).
- Setting: `s = 31/10`, `t = 21/10`; inhomogeneous `H^r` with `J^r = (1 - Lap)^{r/2}` and the unitary Fourier
  transform; on an open set the restriction norm (infimum over extensions). `P = (p, 0)` with `V(P) = 0`,
  `D_P := DV(P) = diag(A, mu)` (a matrix; not the scalar D of section 2), `grad rho(P) = (0, g)`, and `(A, mu, g)` in
  the box `10 <= A <= 51/5`, `99/100 <= mu <= 101/100`, `29 <= g <= 30` (it contains the trial's source coefficients).
  V is `C^4` and rho is `C^5` on `B_{3 delta}(P)`, `0 < delta <= 1`, `3 delta < p/2`; stationarity of rho is not
  assumed. The estimated function u is smooth and compactly supported with `u(0) = 0`, `grad u(0) = 0`; the statements
  extend by completion in the displayed norms (u is not the coefficient correction h of the later bullets). L is the
  normalized linearization of section 2 with velocity V and background rho.
- Energy margin. Let `kappa = 1687/500`, theta a cutoff equal to 1 on `B_{2 delta}(P)` with support in
  `B_{3 delta}(P)`, `w = theta (V - D_P (X - P))`, `q = theta (grad rho - (0, g))`, and
  `A_op = (D_P (X - P)).grad - 1 - g M + w.grad + q.U` on the whole plane (M has symbol `xi_1^2/|xi|^2`). Then
  `Re <A_op u, u>_{H^s} <= -(kappa - E) ||u||_{H^s}^2 + R ||u||_{H^{s-1}} ||u||_{H^s}`, with
  `E = ||div w||_inf/2 + s ||Dw||_{inf,F} + ||q||_inf` and `R = T_s(w) + sum_i P_s(q_i)`, where, with
  `W_r(f) = (2 pi)^{-1} int <xi>^r |f^(xi)| dxi`, `alpha_r = 1/(2 sqrt(pi (r - 1)))` and
  `beta_r = 1/(2 sqrt(pi (r - 1)(r - 2)))`, `P_s(f) = s 2^{s-2} (W_1(f) + alpha_{s-1} ||f||_{H^s})` and
  `T_s(w) = s (s - 1) 2^{s-4} sum_i (W_2(w_i) + beta_{s-1} ||w_i||_{H^s})`. Only first derivatives of w and values of
  q enter E. Taylor's formula gives `E <= C_src delta` with `C_src = 41.7 M_V + 3 M_rho` for a cutoff with
  `delta ||grad theta||_inf <= 2`, where `M_V`, `M_rho` bound `||D^2 V||_F`, `||D^2 rho||_F` on `B_{3 delta}(P)`
  (`C_src` is not the velocity constant `C_V` of sections 7 and 10).
- Local estimate. If `E < kappa`, then with cutoffs `chi` (1 on `B_{5 delta/4}(P)`, support in `B_{7 delta/4}(P)`) and
  `tau` (1 on the support of chi, support in `B_{9 delta/4}(P)`),
  `||chi u||_{H^s} <= K_1 ||tau L u||_{H^s} + K_2 ||u||_{H^s(B_{2 delta}(P) \ B_delta(P))}`
  `+ K_3 ||u||_{H^t(B_{3 delta}(P))} + K_4 N_far(u)`,
  `N_far(u) = int_{|X - P| >= 5 delta/2} |u|/|X - P|^2 + int_{R^2 \ B_{3 delta}(P)} |u|/|X|^3`, with
  `K_1 = 1/(kappa - E)` exactly and `K_2, K_3, K_4` given by explicit formulas of the same kind (Wiener and Sobolev
  norms of the cutoffs and coefficients and constants of the remote velocity kernel; stated in the accompanying
  artifacts). At `delta = 33/2000` the condition `C_src <= 3374/33` (about 102.24) gives `K_1 <= 1000/1687`. For fixed
  coefficients, order s and cutoff shapes, `K_2 = O(delta^{3 - 2s})`, `K_3 = O(delta^{3 - 3s})`,
  `K_4 = O(delta^{-s-2})` as `delta -> 0`; the implied constants are not asserted to be uniform over a family of
  coefficients or corrections.
- The annular term is not removed by absorption: a nonnegative cutoff chi that is positive at a point whose forward
  orbit under V leaves the support of chi in finite time cannot satisfy `V.grad chi >= -eps chi`. The local estimate
  therefore retains the annular `H^s` term, and an outer estimate must bound the annular norm in ordinary `H^s` when
  the estimate is used for outer matching. Two estimates `S <= a_1 F + b_1 O + d_1 Q` and `O <= a_2 F + eps S + d_2 Q`
  (Q a remainder) combine iff `b_1 eps < 1` (as an inference from these inequalities alone).
- Auxiliary inverse. For real `C_c^4` fields w, q, `b = D_P (X - P) + w`, and `E < kappa`, the operator
  `A_op u = b.grad u - u - g M u + q.U u` with maximal domain `{u in H^s : b.grad u in H^s}` generates a semigroup
  with `||S(t)|| <= (1 + R/d)^s exp(-(kappa - E) t)` (t >= 0 the time variable here),
  `d = 1 + (A + mu)/2 - kappa + s ||Dw||_{inf,F} >= 3121/1000`, and has the two-sided inverse `-int_0^inf S(t) dt` of
  norm at most `(1 + R/d)^s/(kappa - E)`. Adding the localized strain term `a_delta c[u]`, with `a_delta` a
  localization of `a_rho = X.grad rho/3` and the raw strain `c[u] = psi[u]_xy(0)` of section 2 in the canonical
  convention, keeps it invertible iff `1 + c[A_op^{-1} a_delta] != 0`; a zero gives an explicit null vector. This
  assumes `a_delta in H^s` and a bounded strain functional on the domain. (The verifier's first notes used the
  opposite sign for the raw strain; the correction was verified separately. The bounds use `|c|` and do not change.)
- Scope: an a priori estimate for L near P and the inverse of an auxiliary operator with cut-off coefficients. It does
  not match outer data, and the rank-one denominator has not been enclosed. An inverse of L assembled directly from
  this auxiliary inverse bound carries its prefactor `(1 + R/d)^s`, the rank-one denominator and the constants of the
  outer matching; a sharper estimate or a different assembly would need additional analysis.
- Coefficient bounds on the disc `B_{0.0495}(P)` of `delta = 0.0165` (for every P in the exact source bracket):
  separate verified interval computations establish `M_rho < 0.5059` from the verified density polynomial enclosures
  and their stated partition and normalization audits, and establish `M_V < 0.2972` (its canonical moment condition is
  discharged; section 2, shared interval archive). Exact arithmetic (verified) then gives `C_src < 13.91094`,
  `E < 0.22953051` and `K_1 < 0.3181`, so the smallness condition `E < kappa` of the local estimate holds for the
  trial at `delta = 0.0165`. The other hypotheses are checked in the next bullet. The reported interval computation
  gives the tighter `C_src <= 13.34` (not verified); the verified exact implication is that `C_src < 13.34` on that
  disc gives `E < 0.22011` and `K_1 < 0.318`. Three larger-disc rows of the first version of that pass are
  inconsistent with its reported radial coverage (exact comparisons); the exported coordinate masks of the revised
  version cover the `delta = 0.0165` disc (verified), and its larger-disc rows have explicit missing points. The
  forcing the estimate must absorb is not small: floating point, `||tau eps~||_{H^{3.1}}` is about 1.56 at
  `delta = 0.0165` (section 10, item 4).
- Trial instance of the hypotheses (verified). The two complete source evaluations use independent interval
  propagation methods and share the archived canonical density moments used to construct the velocity. Their
  conclusions that use those inputs were first verified under the canonical moment condition, which is now discharged:
  the archive is verified by a separate computation, and its composition with these source conclusions is verified
  (section 8). The scalar enclosures for `p`, `mu~ - 1`, `g` and `g'` in section 4 follow from independently
  integrated density moments and do not require this condition. The independent point certificate behind them also
  gives, without the condition, the axis zero P, its uniqueness for p in the bracket below and the displayed
  enclosures for A, mu and g: its point enclosures lie inside the coarser ones below, and the x-derivative of the axis
  drift is positive on its initial bracket, which contains the bracket below. The whole-disc bounds of this bullet
  (`||DV - DV(P)||_op` and the source cutoff sign) use the archive, and their condition is discharged in the same way.
  The canonical trial velocity has a zero `P = (p, 0)`, unique in the bracket
  `4841405518533377/2^49 < p < 4841405518533711/2^49` (an interval of exact width `167/2^48`, near `8.6000638052`).
  There `DV(P) = diag(A, mu)` with `A` in `[10, 10.2]` and `mu` in `[0.9999999774, 0.9999999776]` (strictly below 1),
  and `grad rho~(P) = (0, g)` with `g` in `[29, 30]`, so the coefficient box holds. With a smooth cutoff the cut-off
  coefficient fields are `C_c^6` and `C_c^5`; with the explicit `C^4` cutoff two bullets below they are `C_c^4`, and
  the regularity hypotheses hold in both cases. With the bounds of the previous bullet, the local estimate holds for
  the trial at `delta = 0.0165` with `K_1 < 0.3181` and with every annular, lower-order and remote term retained, and
  the auxiliary operator has the stated maximal-domain inverse. `K_1` is not an inverse norm; the rank-one
  denominator, the outer matching and the global inverse are not evaluated or proved, and the constant R of the
  auxiliary inverse is evaluated only for one explicit cutoff (two bullets below). Also `sym DV(P) >= 0.99 I` and
  `||DV - DV(P)||_op < 0.0147114` on `B_{0.0495}(P)`, so the source cutoff sign of section 10, item 1 holds for the
  trial on that disc. These are statements about the trial, which is not stationary (`mu < 1`), not about X3 or an
  exact solution.
- Order family (verified; exact arithmetic at the parameter vertices, which suffices by multiaffinity, and two
  interval engines; also checked by separate referee reviews). The local estimate (with `t = s - 1` in its lower-order
  term) and the auxiliary inverse hold for each fixed s in `[61/20, 31/10]` with the energy margin
  `kappa(s) = 1301/200 - (101/100) s` in place of kappa and `C_src(s) = (12 s + 9/2) M_V + 3 M_rho` for a cutoff with
  `delta ||grad theta||_inf <= 2` (at `s = 31/10` these are `1687/500` and `41.7 M_V + 3 M_rho`). On the whole
  interval `d >= 3.0705` (box bound), and for the trial at `delta = 0.0165` `K_1 < 0.3181`, with `K_1 < 0.313753` at
  `s = 3.06`. The norm bound of the auxiliary inverse again contains `R_s`, the constant R at order s; for one
  explicit cutoff it is evaluated in the next bullet.
- Explicit auxiliary inverse bound (verified, two independent interval enclosure methods over the whole source disc
  and an output audit; also checked by separate referee reviews). For the trial at `delta = 0.0165` and one explicit
  compact `C^4` cutoff theta, equal to 1 on `B_{2 delta}(P)`, with support the closed ball of radius `23 delta/8`
  about P (strictly inside the open `B_{3 delta}(P)`) and with `delta ||grad theta||_inf <= 1472/819`, the auxiliary
  operator (without the rank-one strain term) is invertible on its maximal domain for every s in `[61/20, 31/10]`,
  with inverse norm in `H^s` below `1.2e35` (below `2.672e34` at `s = 61/20`, `3.518e34` at `s = 3.06` and `1.068e35`
  at `s = 31/10`). R is bounded through Frobenius bounds on the disc of the derivatives of orders 3 to 5 of rho and of
  orders 3 and 4 of U (for example `||D^5 rho|| < 3758450`) and the exact cutoff derivatives. These are upper bounds,
  not lower bounds on the true inverse norm, and they are not useful closing constants (section 10, item 4); the same
  cutoff gives much smaller certified bounds in scaled norms (next bullet).
- Isotropic dilation (verified, with its own proof, exact symbolic identities and interval checks of the norm
  identities; also checked by separate referee reviews). For `0 < ell <= 1` and each s in `[61/20, 31/10]`,
  `(D_ell u)(Y) = u(P + ell Y)` conjugates the auxiliary operator to one of the same form with coefficients
  `w(P + ell Y)/ell` and `q(P + ell Y)` (the multipliers M and U are homogeneous of degree 0), with exactly the same
  E, `kappa(s) - E` and d, and maps the maximal domains onto each other; no condition on the support size enters. With
  `N_lambda(u)^2 = int (lambda^2 + |xi|^2)^s |u^(xi)|^2 dxi` one has `||D_ell u||_{H^s} = ell^{s-1} N_{1/ell}(u)`, so
  the auxiliary inverse has norm at most `(1 + R_ell/d)^s/(kappa(s) - E)` in `N_{1/ell}` and at most `ell^{-s}` times
  that in `H^s`, where `R_ell` is the constant R computed from the conjugated coefficients. Anisotropic dilations
  change the multipliers and the Frobenius term and are not covered. Certified values (verified, exact weighted radial
  integrals of the derivative tensors of the cutoff, the derivative bounds of the previous bullet and the dilation;
  two interval methods and an output audit; also checked by separate referee reviews), for the trial at
  `delta = 0.0165` and the explicit `C^4` cutoff of the previous bullet: at `s = 31/10`, `R_ell < 679.382` with
  inverse bound below `5.7e6` in `N_{1/ell}` at `ell = delta`, `R_ell < 48.225` with bound below 1874 at
  `ell = 7/2000`, and `R_ell < 29.812` with bound below 473 at `ell = 1/500`. In `N_500` the bound is below 608, 554
  and 473 at `s = 61/20`, 3.06 and `31/10`, and below 922 for every s in `[61/20, 31/10]`. In `H^s` this gives below
  `5.743e10` at `s = 3.06` (`ell = 3/1000`), below `6.968e10` at `s = 31/10` (`ell = 11/4000`) and below `1.223e11`
  for every s in `[61/20, 31/10]` (`ell = 3/1000`). These are upper bounds for this cutoff at finitely many scales
  (not an optimization over ell), not lower bounds on the true inverse norm; they contain no rank-one strain term,
  outer matching or residual (section 10, item 4).
- Perturbed profiles and the moving source (verified, exact rational arithmetic and two interval engines; also checked
  by separate referee reviews). For `rho = rho~ + h` with h even in x and odd in y, the velocity
  `V[rho] = c_l[rho] X + U[rho]`, with the centre-normalized `c_l[rho] = (1 + c[rho])/3` of section 2 (equal to `1/k`
  for the trial), is `V~ + W[h]` with `W[h] = U[h] + (c[h]/3) X` (raw c); on the x-axis `V_2 = 0`, `d_x V_2 = 0`,
  `d_y V_1 = 0`, and `div V[rho] = 2/k + 2 c[h]/3`. Let `0 < R_I < 0.0495`, `I = [p - R_I, p + R_I]`,
  `m = A~ - M_V R_I` with `A~ = d_x V~_1(P) = 2/k - mu~ > 2/k - 1` (divergence identity at `h = 0` and `mu~ < 1`), so
  `m > 10.1360138` and `1/m < 0.09866`, and let `eps_0`, `eps_1`, `eps_2`, `eps_3` be the suprema over I (on the axis)
  of `|W[h]_1|`, `|d_x W[h]_1|`, `|d_y W[h]_2|` and `|h_y|`; each derivative used is assumed to exist.
  - Location: if `eps_0 < m R_I`, the axis velocity of rho has a zero in I, and every zero `p_h` in I satisfies
    `|p_h - p| <= eps_0/m`; if also `eps_1 < m` (with `W[h]_1` of class `C^1` on I), the zero is unique in I. A
    first-order formula `p_h - p = -W[h]_1(P)/A~ + O(eps_0 (eps_0 + eps_1))` holds with an explicit error bound.
  - Source data: at `P_h = (p_h, 0)`, `DV[rho](P_h) = diag(A_h, mu_h)` with `A_h + mu_h = 2/k + 2 c[h]/3`,
    `|mu_h - mu~| <= M_V eps_0/m + eps_2`, and `grad rho(P_h) = (0, g_h)` with `|g_h - g| <= M_rho eps_0/m + eps_3`.
    Explicit conditions (`M_V eps_0/m + eps_2 <= 0.0099999`, `(2/3)|c[h]| + M_V eps_0/m + eps_2 <= 0.0492747`,
    `M_rho eps_0/m + eps_3 <= 0.2505`) keep `(A_h, mu_h, g_h)` in the coefficient box (the margins use the certified
    trial scalars `mu~` and g of section 4 and `A~ = 2/k - mu~`).
  - Stationarity at the moved source: if rho solves `F(rho) = 0` classically near `P_h`, is of class `C^1` there, V is
    differentiable at `P_h` and `g_h != 0`, then `mu_h = 1`. Hence, by the source-data bound on `|mu_h - mu~|`, no
    exact solution `rho~ + h` of this kind with `W[h]` of class `C^1` near I, `eps_0 < m R_I` (so that Location gives
    a source `P_h` in I) and `eps_3 <= 29` (which gives `g_h > 0.7244` with the certified value of g in section 4 and
    `eps_0/m < R_I`; the coefficient box `g in [29, 30]` alone would not) has `M_V eps_0/m + eps_2 < 1 - mu~`. With
    the certified `1 - mu~ = 2.2528046115e-8` within `4.7e-19` (section 4; the interval printed in the trial-instance
    bullet is too coarse for this step), in particular none has `eps_0 <= 2.1886e-8` and `eps_2 <= 2.1886e-8`. Unlike
    the jet-continuity exclusion of section 7 this follows the source of the perturbed profile; it needs only `C^1`
    density near the source and `g_h != 0`, and no small density-jet increments or second density derivative; it is
    just as narrow (section 7) and is not an endpoint.
  - Transported local estimate: for the operators `L_h = L + W[h].grad` of the two-norm theorem (written `A_h` in
    section 7; here L is the linearization about rho~, so `L_h` has velocity `V~ + W[h]` and background `rho~`, and
    `A_h` denotes the source eigenvalue of the previous sub-bullets), assume the box conditions with `eps_3` omitted,
    `W[h]` of class `C^4` on `B_{0.0495}(P)` and `||D^2 W[h]||_F <= m_2` there. Then for every
    `0 < delta' <= delta_h = (0.0495 - |p_h - p|)/3` the hypotheses of the local estimate hold at `P_h`, except
    possibly `E < kappa`, with `E <= (41.7 (M_V + m_2) + 3 M_rho) delta'`. At `delta' <= 0.0165`, `m_2 <= 1` gives
    `K_1 <= 0.40709660` and `m_2 <= 2` gives `K_1 <= 0.56549268`, uniformly over every h with that budget (the scale
    0.0165 itself is admissible only when `p_h = p`; the values there are ceilings for the admissible smaller scales).
    These are local forcing coefficients, not inverse norms. `K_2`, `K_3`, `K_4`, the norms of cutoffs centred at
    `P_h`, the auxiliary inverse, the rank-one denominator and the outer matching are not made uniform. The `C^4`
    hypothesis on `W[h]` is removed for corrections h in the whole-plane space `H^s(R^2)`, s in `[61/20, 31/10]`, by
    the next bullet; for such h the Hessian budget holds with `m_2 = gamma_s ||h||_{H^s}`,
    `gamma_s = (2 pi (s - 1)(s - 2)(s - 3))^{-1/2}` (verified). Membership in `H^s(R^2)` alone does not give the
    location and coefficient-box conditions; for `s = 153/50` and `||h||_{H^s} <= 7/50` they are verified, together
    with the Hessian bound, in the bullet "Whole-plane Sobolev ball" below. For the weighted correction space of the
    proposed realization (section 10) neither the local regularity of `W[h]` nor these conditions have been derived
    from its norm.
- Rough coefficients (verified, with its own proof, exact symbolic identities and checks at the parameter vertices;
  also checked by separate referee reviews). For each s in `[61/20, 31/10]` and each `sigma >= s` with `sigma > 3`:
  - Auxiliary inverse: for compactly supported real coefficient fields w, q in `H^sigma` (in place of `C_c^4`) and
    `E < kappa(s)`, the auxiliary operator has on its maximal domain the two-sided inverse of norm at most
    `(1 + R/d)^s/(kappa(s) - E)` (existence and uniqueness on that domain); the isotropic dilation and its scaled
    bounds carry over (no new constants are evaluated).
  - Local estimate: it holds with the actual E for a velocity `V_0 + W`, with `V_0` of class `C^4` and W in `H^sigma`
    near `B_{3 delta}(P)`, and a fixed density of class `C^5`; one coefficient in the formula for `K_2` is replaced by
    a product bound, and the other constants are unchanged. The explicit budget `E <= C_src(s) delta` additionally
    uses `div V = A + mu` on `B_{3 delta}(P)`; for the velocities `V~ + W[h]` the divergence `2/k + 2 c[h]/3` is
    constant, so this holds at their source.
  - Completion: the extension of the local estimate by completion covers every u in `H^s(R^2)` with `u(0) = 0`,
    `grad u(0) = 0` and `tau' L u` in `H^s` near the support of tau (tau' a cutoff equal to 1 near the support of tau;
    L here is the operator being estimated, with velocity `V_0 + W`). For every u in `H^s(R^2)` with `u(0) = 0` and
    `grad u(0) = 0`, `N_far(u) <= [2 sqrt(pi)/(5 delta) + pi R_0 gamma_s + sqrt(pi/2) R_0^{-2}] ||u||_{H^s}` for every
    `R_0 > 0`; no such bound holds on all of `H^s` (the second term of `N_far` is infinite when the first-order jet at
    0 is nonzero). The whole completion is not characterized.
  - Consequence: for every fixed correction h in `H^s(R^2)` that satisfies the location, coefficient-box and Hessian
    conditions, the transported local estimate for `L_h` holds without the `C^4` hypothesis on `W[h]`, for smooth
    compactly supported u with `u(0) = 0`, `grad u(0) = 0` and for the completion class above with the graph condition
    `tau' L_h u` in `H^s`; its `K_1` ceilings (previous bullet; by the order family they also hold at `s = 3.06`) are
    uniform over these corrections and the admissible scales. Not covered: uniform `K_2`, `K_3`, `K_4` or R over a
    family of h, a rough-coefficient semigroup, a weighted far-field completion, the rank-one inverse, the outer
    matching, a high-norm residual and any closing inequality.
- Whole-plane Sobolev ball (verified, with its own proof, two interval engines and an independent output audit; also
  checked by separate referee reviews). Let `s = 153/50` and let h in `H^s(R^2)` be real, even in x and odd in y, with
  `||h||_{H^s} <= 7/50` (unitary Fourier transform, weight `(1 + |xi|^2)^s`). Then the axis velocity of `V~ + W[h]`
  has exactly one zero `p_h` in `[p - 0.049, p + 0.049]`, with `|p_h - p| < 0.00286036`; the source data stay in the
  coefficient box (`A_h` in `[10, 10.2]`, `mu_h` in `[0.99, 1.01]` and, the background rho~ being fixed,
  `d_y rho~(P_h)` in `[29, 30]`), the Hessian bound entering E follows from the bound on `D^2 U[h]` below, and
  `0.01554654 < delta_h <= 0.0165` (equality at h = 0). For every `0 < delta' <= delta_h` and cutoffs with
  `delta' ||grad theta||_inf <= 2` the local estimate of the rough-coefficient extension (previous bullet) holds at
  `P_h` for the velocity `V~ + W[h]`, with the fixed `C^5` background rho~ and under its graph-completion hypotheses,
  with `E < 0.30138506` and `K_1 = 1/(kappa(s) - E) < 0.32123200`, `kappa(153/50) = 3.4144`, uniformly over the ball.
  The ingredients are Cauchy-Schwarz bounds in Fourier variables, for example
  `sup |U_1[h]| <= (32 pi (s - 1))^{-1/2} ||h||_{H^s}`, `|c[h]| <= (64 pi (s - 1)(s - 2))^{-1/2} ||h||_{H^s}` and
  `sup ||D^2 U[h]||_F <= (4 pi (s - 1)(s - 2)(s - 3))^{-1/2} ||h||_{H^s}` (by the angular factor of the velocity
  symbol, `2^{-1/2}` times the constant `gamma_s` of the transported-estimate bullet), and the canonical whole-plane
  velocity `U[h]` of h (its uniqueness among sublinear solutions of the whole-plane div-curl system with the parity is
  part of the verified proof; `W[h]` itself contains the linear strain term). The radius 7/50 is a sufficient radius
  for these hypotheses, not a closing radius of any iteration. The uniformity concerns `K_1` and the named local
  hypotheses only. Not covered: uniform `K_2`, `K_3`, `K_4` or R, the auxiliary inverse at `P_h`, a weighted
  correction space (an embedding into `H^{153/50}(R^2)` with an explicit constant would be needed), the rank-one
  inverse, the outer matching, a high-norm residual and any closing inequality. With the stationarity sub-bullet
  above, the same bounds give a narrow statement about the trial: no such h with `||h||_{H^{153/50}} <= 3.2318e-7`
  makes `rho~ + h` a classical solution near `P_h` (section 7). Since `X3 - rho~` lies in no `H^s(R^2)` with `s >= 0`
  (section 2, far tail), neither of these correction balls about the trial contains X3, and this exclusion excludes no
  neighbourhood of X3.

(p) Centre quasimodes in the diagnostic weighted `H^1`-type norm and its more singular variants (verified, with its
own proof and two exact implementations of the scalar identities; also checked in two completed referee reviews and a
separate adjudication). Let X be the space of even-x, odd-y functions with
`||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX` finite, `w = L^6 r^{-6} (1 + r^2/L^2)^{3/2-k}` (section 10, next step
1), with `0 < k < 1/2`, `L > 0` and `c_l = 1/k`. Assume that rho is even in x and odd in y, `rho = x^2 y + O(r^5)`,
`|grad rho| <= C r^2` and `|D^2 rho| <= C r` near 0, rho is locally `C^{4,alpha}` for some `alpha > 0`, `U[rho]` is
`C^2` near 0 with `DU[rho](0) = diag(-c, c)`, `c = 3 c_l - 1`, and `|rho| + r |grad rho| + r^2 |D^2 rho| <= C r^k` at
infinity. The exactly normalized modal trial satisfies these hypotheses (its centre and far bounds are those of the
graph-domain statement of section 10, next step 1). Then there are smooth compactly supported densities h_j of the
required parities, vanishing near 0, with smooth global factors `h_j = x^2 y b_j`, such that `J(h_j) = c[h_j] = 0`,
`||h_j||_X = 1` and `||L h_j||_X -> 0`.
- Mechanism. The linear part of `V = c_l X + U[rho]` at 0 is `A_c = diag(-A, D) = diag(1 - 2 c_l, 4 c_l - 1)`, a
  saddle (a matrix; A and D are the scalars of 5(e)). With `p = (8 c_l - 3)/(6 c_l - 2)` and
  `q = (4 c_l - 1)/(6 c_l - 2)`, so that `p + q = 2`, `(1 - 2 c_l) p + (4 c_l - 1) q = 1`, `1 < p < 3/2` and
  `1/2 < q < 1`, the degree-two function `H = |x|^p sign(y) |y|^q` solves `(A_c X.grad - 1) H = 0` off the axes, and
  its angular factor lies in `H^1` of the circle because p and q exceed 1/2. The centre weight makes degree-two
  densities scale-critical: for a smooth angular function `Z(theta)` and a smooth compactly supported function eta of
  `t = log r`, `||r^2 eta(log r) Z(theta)||_X^2` equals
  `L^6 int int (1 + e^{2t}/L^2)^{3/2-k} [eta^2 Z^2 + (2 eta + eta')^2 Z^2 + eta^2 Z'^2] dt dtheta` (primes denote
  derivatives in t and theta). Fix `0 < delta < 1/4` such that the centre bounds hold on `r <= delta`, a smooth `zeta`
  with `0 <= zeta <= 1`, equal to 0 on `(-inf, 0]` and to 1 on `[1, inf)`, and put
  `eta_N(t) = zeta(t + N) zeta(log delta - t)` for `N > 2 - log delta`; it equals 1 on `-N + 1 <= t <= log delta - 1`,
  and its derivatives of each order are bounded uniformly in N. Angular cutoffs of H vanishing near the axes, times
  `eta_N(log r)`, have X norm at least a constant times `sqrt N`, and their images under the frozen centre operator
  are at most a constant times `sqrt N` times the `H^1` norm of the angular defect (which tends to 0 with the angular
  cutoff) plus a constant independent of N. The variable-coefficient error and the terms `U[h].grad rho` and
  `(c[h]/3) X.grad rho` are bounded uniformly in N (a dyadic `H^{5/2}` bound for the velocity, `grad rho = O(r^2)` at
  the centre and the far decay), and a fixed compact bump supported in `1 < r < 2` restores `c[h] = 0`. Choosing first
  the angular cutoff and then N gives the sequence.
- Consequences. No finite C gives `||h||_X <= C ||L h||_X` on any linear perturbation domain containing these
  densities: in particular on the graph domain D of section 10, next step 1, on its subspace with `J = 0` and `c = 0`,
  and on any subspace with vanishing leading far coefficient that contains them. The lower bound `||K||_X / ||L K||_X`
  stated there is therefore superseded as an obstruction. The sequence can moreover be chosen with
  `||h_j||_{H^{5/2}} -> 0`, support in `r <= 2` and `h_j -> 0` weakly in X (verified, with its own proof; also checked
  in two completed referee reviews and a separate adjudication). Hence, on any domain of densities h with h and `L h`
  in X that contains this sequence: no C gives `||h||_X <= C (||L h||_X + ||h||_{H^{5/2}})`, nor
  `||h||_X <= C (||L h||_X + ||Q h||_Z)` for a compact linear `Q` from X into a Banach space Z (compactness turns weak
  into norm convergence; no compact embedding is assumed); for every bounded linear `B: X -> X` the supremum of
  `||h - B L h||_X` over unit vectors of the domain is at least 1; and every closed realization of L in X whose domain
  contains the sequence, and which agrees with L on it, fails to have both closed range and finite-dimensional kernel,
  so it is not Fredholm. Which of these two properties fails is not determined. More singular centre weights do not
  remove the obstruction (verified, with its own proof and two exact implementations of the algebra; also checked in
  completed referee reviews and a separate adjudication): for every fixed integer `m >= 2` let `X_m` be defined like X
  with the weight `w_m = L^{2m+2} r^{-2m-2} (1 + r^2/L^2)^{m-k-1/2}` (so `X_2 = X`); then the conclusions above for
  domains containing the sequence (no same-norm inverse estimate, none with an `H^{m+1/2}` or compact remainder, the
  defect bound, no Fredholm closed realization) hold in `X_m`, for a sequence small in `H^{m+1/2}`, weakly null in
  `X_m`, supported in `r <= 2`, with `J = c = 0` and with all Taylor coefficients of `U[h_j]` at 0 of degree at most
  `m - 2` equal to zero (cancelled by finitely many fixed remote bumps through a positive definite angular Gram
  matrix); the constants are not uniform in m. The constraints `J = c = 0` alone do not keep the image in `X_m` for
  `m >= 5` (verified, with its own proof and two exact implementations of the algebra; also checked in two completed
  referee reviews, a separate adjudication and a separate referee audit): assume rho even in x and odd in y with
  `rho = x^2 y + R`, `|grad R| <= C r^4` and `|D^2 R| <= C r^3` near 0, rho `C^2` and `U[rho]` `C^1` on compact
  annuli, and `|grad rho| <= C r^{k-1}`, `|D^2 rho| <= C r^{k-2}` at infinity (the exactly joined trial satisfies
  these); then `h = r^4 eta(r) (sin 5 theta + sin 7 theta)`, with `eta >= 0` smooth, supported in `(1, 2)` and of
  integral 1, is smooth with a smooth global factor `x^2 y`, has `J = c = 0` and lies in every `X_m`, its interior
  stream is `(1/2) r^4 sin 4 theta + Gamma_6 r^6 sin 6 theta = 2 (x^3 y - x y^3) + Gamma_6 r^6 sin 6 theta` with
  `1/8 < Gamma_6 < 1/2`, and `L h = 2 (x^4 y + 5 x^2 y^3) + O(r^7)` near 0 (gradient remainder `O(r^6)`), so `L h`
  lies in `X_2`, `X_3` and `X_4` and in no `X_m` with `m >= 5`. The sequences above are not affected: for `m >= 5`
  their velocity Taylor coefficients of degree at most `m - 2`, in particular the cubic ones, vanish. In the two-norm
  theorem of section 7 the low a priori estimate fails at `h = 0` when E and `Y_L` are both normed by X and the low
  domain contains these sequences. Not covered: forcing norms stronger than X (a solution operator bounded from a
  stronger forcing space into X, of the kind `K_H` of section 7 requires, is not excluded, nor is a bounded right
  inverse), other correction norms (for example more derivatives at the centre, anisotropic weights such as
  `|x|^{-2a}` (for these see 5(q)), or explicit jet components), domains that exclude these sequences, exact kernels,
  and the existence of a profile.

(q) Axis-weighted logarithmic norms (verified, with their own proofs and two exact implementations of the algebra and
of the scalar enclosure; also checked in completed referee reviews, separate adjudications and a separate referee
audit). On the half-plane `x > 0` put `z = log x` and, for real a and `s >= 0`, let `Y_(a,s)` be the Hilbert space of
functions h with `||h||_Y = ||e^{(1/2-a) z} h(e^z, y)||_{H^s(R^2)}` finite (inhomogeneous Sobolev norm in the
variables `(z, y)`); its squared norm dominates `int_{x>0} x^{-2a} |h|^2 dx dy`, with equality for `s = 0`. For
`a > 0` this weight is singular along the whole y-axis, unlike the centre weights of 5(p). For densities on the plane,
membership refers to their restriction to `x > 0`.
- Frozen inverse. Let `T_0 = -A x d_x + D y d_y - 1` be the frozen centre transport of 5(e) (`A = 2 c_l - 1`,
  `D = 2A + 1 = 4 c_l - 1 > 0`) with its maximal domain in `Y_(a,s)`, and put `delta_Y = D(s - 1/2) - A(a - 1/2) - 1`
  (the exponent delta of 5(e) with b replaced by s). Then `T_0` is closed and generates the semigroup
  `S(t) h = e^{-t} h(e^{-At} x, e^{Dt} y)` with `||S(t)|| <= e^{delta_Y t}` for `t >= 0`; if `delta_Y < 0`, `T_0` is
  bijective from its maximal domain onto `Y_(a,s)`, with inverse `f -> -int_0^inf S(t) f dt` of norm at most
  `1/|delta_Y|`, and the same holds on the odd-y subspace. At the exactly normalized trial and `(a, s) = (6, 153/50)`,
  `delta_Y = 97/50 - (19/25) c_l` lies in `(-2.297275584089, -2.297275584087)`, so the inverse norm is below
  0.435298231926; by the classification below it equals `1/|delta_Y|`. The homogeneous solution `x^p sgn(y) |y|^q` of
  `T_0 H = 0` with `p + q = a + s - 1` is not in `Y_(a,s)`, even after multiplication by a cutoff equal to 1 near a
  compact piece of the positive y-axis, because `p - (a - 1/2) = delta_Y/(A + D) < 0` (at this point p is about
  5.42696 and q about 2.63304). This concerns the frozen operator only: the variable coefficients, the nonlocal term
  `U[h].grad rho`, the strain term and the far field are not estimated by this frozen result.
- Forward threshold (verified, with its own proof and two exact implementations; also checked in a completed referee
  review, a separate adjudication and a separate referee audit). Since `A > 0`, `delta_Y < 0` holds exactly when
  `a > a_Y(s) = 1/2 + (D(s - 1/2) - 1)/A`, and `a_Y(s) - 5/2 = (D/A)(s - 3/2)`. Hence all weights with `delta_Y < 0`
  at a given order s have `a > 5/2` if and only if `s >= 3/2`; for `s < 3/2` the weights with `a_Y(s) < a < 5/2` have
  `delta_Y < 0`. At `s = 153/50`, `a_Y(s)` lies in `(5.773683600530, 5.773683600531)`. So for `s >= 3/2` every weight
  at which the forward integral above inverts `T_0` has `a > 5/2`, where the mapping obstruction below applies. For
  unrestricted real a, the condition `delta_Y < 0` is sufficient, not necessary, for invertibility: with
  `delta_- = -A a - b_0`, `b_0 = (A + 3)/2`, the negative-time integral `int_0^inf S(-t) f dt` inverts `T_0` with norm
  at most `1/delta_-` when `delta_- > 0` (for example at `a = -1`, since `A > 3`). The remaining weights, with
  `delta_- <= 0 <= delta_Y`, are classified in the next item.
- Complete frozen classification (verified, with its own proof, the differential identities in two symbolic
  implementations and the scalars in two exact ones; also checked in a completed referee review with a follow-up
  exchange, a separate adjudication and a separate referee audit). Since `delta_Y = delta_- + D s`, one has
  `delta_- <= delta_Y`. On the complex space `Y_(a,s)` the spectrum of `T_0` (maximal domain) is the closed strip
  `delta_- <= Re lambda <= delta_Y`, and `T_0` has no eigenvalues. `T_0` is bijective from its maximal domain onto
  `Y_(a,s)` if and only if 0 lies outside `[delta_-, delta_Y]`, and then its inverse has norm exactly
  `1/dist(0, [delta_-, delta_Y])` in the norm of `Y_(a,s)`. If `delta_- < 0 < delta_Y`, `T_0` is injective and its
  range is closed and has infinite codimension (next item); if 0 is an endpoint of the interval, `T_0` is injective
  with dense range that is not closed; in both cases `T_0` is not Fredholm. The invertibility classification and the
  norms hold also on the real odd-y subspace (there the strip is the spectrum of the complexification). The proof uses
  Fourier variables `xi_z`, `xi_y` dual to z, y and `tau = log|xi_y| - (1/2) log(1 + xi_z^2)`; a unitary
  transformation takes `S(t)` to a direct sum of two groups, one for each half-line of `xi_y`, and on each copy
  `L^2(d xi_z d tau)` the generator is `-D d_tau + d(tau)`, with a bounded real potential d taking values between
  `delta_-` and `delta_Y`. Explicit kernel and adjoint solutions, together with translated wave packets, give the
  classification, the sharp inverse norm and the non-closed range at the endpoints. For `a >= 0` one has
  `delta_- < 0`, so among these weights `T_0` is invertible if and only if `delta_Y < 0`, that is `a > a_Y(s)`; for
  `s >= 3/2` every such weight has `a > 5/2`, where the mapping obstruction and the trial residual statement below
  apply. At `(a, s) = (6, 153/50)` the inverse norm is the rational number `4251410641576450/9766661864823671` (about
  0.4352982319). Weights with `delta_- > 0` (necessarily `a < 0`, for example `a = -1`) remain invertible. The
  classification concerns the frozen operator only; it says nothing about the full L, on its maximal domain or on a
  smaller one, nor about the quadrant norms of 5(e), which form a different family.
- Range inside the strip (verified, with its own proof, the quadratic minimum and the scalars in two exact
  implementations and the Mellin exponents checked analytically; also checked in a completed referee review with two
  follow-up exchanges, a separate adjudication and a separate referee audit). Let `delta_- < 0 < delta_Y`, put
  `u = -delta_-`, `v = delta_Y`, and let `m = min(u, v)^2` if `min(u, v) <= D` and
  `m = D^2 + 2D(u - D)(v - D)/(u + v - 2D)` otherwise. Then `||h||_Y <= m^{-1/2} ||T_0 h||_Y` on the maximal domain:
  in the variables of the previous item, with `d(tau) = -u + (u + v) e^{2 tau}/(1 + e^{2 tau})`, every transformed
  component `V_fr` satisfies `||(-D d_tau + d) V_fr||^2 = D^2 ||d_tau V_fr||^2 + int (d^2 + D d') |V_fr|^2`, and m is
  the infimum over real tau of `d^2 + D d'`. Hence `T_0` is injective with closed range, which is the orthogonal
  complement of the adjoint kernel of the previous item. Put `c_fr = -A(a - 1/2) - 1`,
  `F_f(z, y) = e^{(1/2-a) z} f(e^z, y)` and `f^(xi_z, xi_y) = (2 pi)^{-1} int e^{-i(z xi_z + y xi_y)} F_f(z, y) dz dy`
  (in the `L^2` sense). A forcing f in `Y_(a,s)` lies in the range if and only if
  `int_0^inf xi_y^{-c_fr/D + i A xi_z/D} f^(xi_z, +-xi_y) d xi_y = 0` for almost every `xi_z` and each sign (a Mellin
  moment in `xi_y`, absolutely convergent for almost every `xi_z`, not a trace at `xi_y = 0`). Write `J_+-(xi_z)` for
  the two moments and put `N = Gamma(u/D) Gamma(v/D)/(2 Gamma(s))` (here `u + v = D s`). Then
  `sum_+- int (1 + xi_z^2)^{v/D} |J_+-|^2 d xi_z <= N ||f||_Y^2`: the moment map from `Y_(a,s)` onto two copies of
  `L^2((1 + xi_z^2)^{v/D} d xi_z)` has norm exactly `sqrt N`, attained, and a right inverse of norm `1/sqrt N`, and
  its kernel is the range of `T_0`; the same bound without the weight holds, again with norm exactly `sqrt N`, which
  is then not attained. At `(a, s) = (0, 153/50)`, `1.104919423326 < N < 1.104919423327`. With the norm of `Y_(a,s)`
  on both forcing and solution, the inverse on the range has norm at most `m^{-1/2}`, and exactly `1/min(u, v)` when
  `min(u, v) <= D`. At `(a, s) = (0, 153/50)` one has `u = 1 + c_l < D < v`, and the exact norm is `k/(1 + k)` (about
  0.1520828674); this inverse requires the whole infinite family of moment conditions. The inverse statement also
  holds on the real odd-y subspace, where the two sign conditions coincide; the moment-map statements hold there with
  the same norm and the target restricted by `J_- = -J_+` and `J_+(-xi_z) = -conj J_+(xi_z)` (conj the complex
  conjugation). Consequently, for `a >= 0`, where `delta_Y = A(a_Y(s) - a)`, `T_0` is invertible if `a > a_Y(s)`, has
  dense non-closed range if `a = a_Y(s)`, and has closed range of infinite codimension if `0 <= a < a_Y(s)`; every
  non-invertible case is not Fredholm, and for `s >= 3/2` invertibility requires `a > a_Y(s) >= 5/2`. This concerns
  the frozen operator only; it does not identify the range of the full L.
- Mapping obstruction. Assume that rho is even in x and odd in y, locally `C^3` near 0, `rho = x^2 y + R` with
  `|D^j R| <= C r^{5-j}` for `0 <= j <= 3`, and `rho(0, y) = 0` for small y; the exactly joined trial satisfies these
  hypotheses. Then there is a smooth density h of the required parities, with a smooth global factor `x^2 y`,
  supported in `1 < r < 2` at positive distance from both axes (so `J(h) = 0`) and with `c[h] = 0`, which lies in
  every `Y_(a,s)`, while `L h` lies in no `Y_(a,s)` with `a >= 5/2` and `s >= 0`; this includes
  `(a, s) = (6, 153/50)`, where `T_0` is invertible. Mechanism: the angular factor is chosen, through the positive
  definite Gram matrix of `sin 3 theta` and `sin 5 theta` against a nonnegative angular bump vanishing near both axes,
  so that the third sine coefficient of h vanishes (hence `c[h] = 0`) and the fifth is a positive multiple of a fixed
  radial bump. In `r < 1` one has `L h = U[h].grad rho`, the stream there is `C_ax (x^3 y - x y^3) + O(r^6)` with a
  constant `C_ax > 0`, so `L h = C_ax (x^4 y + 5 x^2 y^3) + O(r^7)` (with differentiated remainders), and
  `L h >= d_ax x^2`, with a constant `d_ax > 0`, on a rectangle `(0, x_1) x (y_1, y_2)`, `0 < y_1 < y_2`, adjacent to
  the y-axis; `int_0^{x_1} x^{4-2a} dx` diverges for `a >= 5/2`. Only the zeroth-order part of the norm is used, and
  nothing at infinity is involved.
- Compatible test densities. Let `T_ann` be the space of smooth densities of the required parities supported in
  `1 < r < 2` at positive distance from both axes, and `T_ann,0` its subspace with `c[h] = 0`. For h in `T_ann` with
  sine coefficients `F_l(r) = (1/pi) int h(r, theta) sin(l theta) d theta` put
  `Gamma_n(h) = (1/2) int_0^inf r^{-n} F_{n+1}(r) dr` for even `n >= 2`; these are the coefficients of the interior
  stream `sum_n Gamma_n r^n sin(n theta)` in `r < 1`, and `c[h] = 2 Gamma_2(h)`. Under the hypotheses of the previous
  item and, for the sufficiency part, rho and `U[rho]` in `C^{4,1/2}_loc(R^2)` (satisfied by the exactly joined
  trial), for `a >= 5/2`, `0 <= s < 7/2` (in particular `s = 153/50`) and h in `T_ann,0` the following are equivalent:
  `L h` is in `Y_(a,s)`; the vertical velocity `U_2[h]` vanishes on the y-axis near 0; `Gamma_n(h) = 0` for every even
  `n >= 2`; the stream and velocity of h are compactly supported and vanish near both axes. The first condition
  implies the second for every `s >= 0`, and the last implies the first for every finite a and `0 <= s < 7/2`.
  Mechanism: for small `y > 0`, `(d_x^2 L h)(0, y)/2 = -2 b_ax u' + b_ax' u` with
  `b_ax(y) = rho_xx(0, y)/2 = y + O(y^3)` and `u = U_2[h](0, y)`, so membership forces `u/sqrt(b_ax)` to be constant
  there; since `u = O(y)` and `b_ax(y)/y -> 1`, the constant is 0, and since u is odd it vanishes near 0 on both
  sides; the Taylor coefficients of u are nonzero multiples of the `Gamma_n`; and harmonic continuation through the
  source-free strips along the axes gives the compact support. The common subspace is infinite-dimensional (it
  contains `-Lap f` for every f in `T_ann`) and has infinite algebraic codimension in `T_ann,0`: for every N the
  moments `Gamma_4, ..., Gamma_{2N+2}` map `T_ann,0` onto `R^N`. Hence, for `a >= 5/2` and `s = 153/50`, no subspace
  of `T_ann,0` of finite codimension is mapped by L into `Y_(a,s)`.
- Weak weights (verified, with its own proof, the factor identity and the Euler-derivative identities in two symbolic
  implementations and the exponents of the trial in two exact ones, with different libraries; also checked in a
  completed referee review with a follow-up exchange, a separate adjudication and a separate referee audit; the
  extension to the orders `s < 6 - a` verified separately, with its own proof, the factor identity and the derivative
  identities through total order 6 in two symbolic implementations, and checked in three completed referee reviews, a
  separate adjudication and a separate referee audit). Let h be a real smooth density of the required parities with
  compact support at positive distance from both axes and `c[h] = 0` (for example any h in `T_ann,0`), and let L be
  the linearization at the exactly joined trial. Then, for every `0 <= a < 5/2` and every order `0 <= s < 6 - a` (in
  particular `s = 153/50`), h and `L h` lie in `Y_(a,s)`. Mechanism, written for `s = 153/50`: the stream of h is
  `O(r^4)` near 0 (its interior harmonic expansion has only even sine modes from degree 2 on, and the degree 2
  coefficient is a multiple of `c[h]`) and `O(r^{-2})` at infinity (the source `d_x h` has vanishing mass and first
  moments), with derivatives, so the quotients `U_1[h]/x` and `U_2[h]/y` and their derivatives `D^alpha`, for
  Cartesian multi-indices with `|alpha| <= 4`, are bounded by `C r^{2-|alpha|}` near 0 and by `C r^{-4-|alpha|}` near
  infinity. Since `rho~` is `x^2 y` times an even factor with differentiated bounds through order 5 near 0 and near
  infinity (derived from the finite power and log-polynomial formulas of the trial using its checked exact exponents),
  `U[h].grad rho~ = x^2 y G_h` with `|D^alpha G_h| <= C r^{2-|alpha|}` near 0 and `<= C r^{k-7-|alpha|}` near infinity
  (`|alpha| <= 4`); the inherited `C^6` annular joins give `G_h` in `C^5` on compact annuli, and the same `x^2` factor
  handles their axis portions. The factor `x^2` survives the derivatives `x d_x` and `d_y`, and on a dyadic shell of
  radius `lambda` the weight and the Jacobian `dx dy/x` produce `int_0^{2 lambda} x^{4 - 2a} dx`, which is finite
  exactly when `a < 5/2`; the small shells are summed in `H^s` by interpolation between their `H^3` and `H^4` bounds
  (geometric rate `lambda^{6 - a - s}`), the large shells in `H^4`, with bound `C lambda^{k-3-a}`, which is summable
  since `k < 1/2` and `a >= 0`. The remaining terms of `L h` are compactly supported away from both axes and `C^4`.
  For the other orders `s < 6 - a` the factor of `rho~` is `W^{7,infinity}` on compact annuli (piecewise smooth, with
  matching derivatives through order 6 and bounded one-sided seventh derivatives), so `G_h` is `W^{6,infinity}` there
  and the local terms are `C^6`; using the factor's end bounds through order 7 and the velocity quotients' bounds
  through order 6, the shells have `H^n` bounds `C lambda^{6-a-n}` near 0 and `C lambda^{k-3-a}` at infinity, for
  integers `0 <= n <= 6`, and interpolation between `H^{floor(s)}` and `H^{ceil(s)}` gives the rate `lambda^{6-a-s}`.
  With the mapping obstruction (which fails already in the zeroth-order norm), for `a >= 0` and each order
  `0 <= s <= 7/2` the image `L(T_ann,0)` lies in `Y_(a,s)` if and only if `a < 5/2`; for `7/2 < s < 6` only the
  sufficient range `0 <= a < 6 - s` is proved. The statement is setwise: the constants may depend on h, a and s; no
  bound uniform in h, no continuity of L in the norm of `Y_(a,s)` or in the frozen graph norm (at `s = 153/50`, the
  frozen graph domain item applies at these weights as well) and no inverse is asserted; nothing is asserted here
  about the trial's residual, about `a < 0` or about the critical orders `s = 6 - a`.
- Trial residual (verified, with its own proof and two implementations using exact rational arithmetic and interval
  enclosures, with different algorithms and libraries; also checked in two completed referee reviews, a separate
  adjudication and a separate referee audit). For the exactly joined trial write, as `y -> 0+`,
  `rho~_xx(0, y)/2 = y + B y^3 + o(y^3)` and `U_2[rho~](0, y) = sigma y + A_3 y^3 + o(y^3)`, `sigma = 3 c_l - 1`, and
  let `F_5` be the fifth sine coefficient of rho~. The coefficient of `r^4 sin 4 theta` in the stream is
  `psi_4 = (1/2) int_0^inf r^{-4} F_5(r) dr - 1/64`; the term `-1/64` comes from the cubic density `x^2 y` at the
  centre (the moment formula in the Compatible test densities item assumes a density vanishing near 0), and
  `A_3 = -1/6 - 4 psi_4`. On the y-axis `eps~_xx(0, y)/2 = (2 c_l - 1 - 2 u') b_ax + (c_l y + u) b_ax'` with
  `b_ax = rho~_xx(0, y)/2` and `u = U_2[rho~](0, y)`; the linear terms cancel, and `eps~_xx(0, y)/2 = Q y^3 + o(y^3)`
  with `Q = 2 D B - 5 A_3 = 2 D B + 25/48 + 10 int_0^inf r^{-4} F_5(r) dr`. The integral is an exact rational number
  computed from the stored data (over all spline spans, with no quadrature error or tail truncation), B is an exact
  rational multiple of one exponential, and two interval evaluations by different algorithms give
  `6.087210e-6 < Q < 6.087213e-6`. Since eps~ is even in x and vanishes on the y-axis, `|eps~|` is at least a positive
  constant times `x^2` on a rectangle adjacent to the y-axis, so eps~ lies in no `Y_(a,s)` with `a >= 5/2` and
  `s >= 0` (in particular not in `Y_(6,153/50)`) and in no quadrant norm of 5(e) with `a >= 5/2` (every real b and
  integer `m >= 0`, in particular the revised working point). This is an obstruction to these forcing spaces for one
  trial (for `s = 153/50` and `0 <= a < 5/2`, see the next item); exact profiles, other residual spaces and correction
  domains are not concerned.
- Residual at weak weights (verified, with its own proof, and the exterior coefficient below in two implementations
  using exact rational decoding and interval arithmetic, with different algorithms and libraries; also checked in
  three completed referee reviews (the second after a written response and the third after a correction), a separate
  adjudication and a separate referee audit). For the exactly joined trial, `s = 153/50` and every `a >= 0`, the
  restriction of eps~ to `x > 0` lies in `Y_(a,s)` if and only if `2k < a < 5/2`. Sufficiency: by the exact
  normalization `c[rho~] = 3 c_l - 1` the transport field is `c_l X + U[rho~] = (-A x, D y) + U_rem` near 0, with
  `|D^alpha U_rem| <= C r^{3-|alpha|} (1 + |log r|^{M_log})` for `|alpha| <= 5` and a fixed nonnegative integer
  `M_log`, and `-2A + D - 1 = 0`, so the multiple of the even factor of `rho~` cancels exactly and `eps~ = x^2 y B_0`
  with `|D^alpha B_0| <= C r^{2-|alpha|} (1 + |log r|^{M_log})` near 0 (`|alpha| <= 4`); at infinity the factor
  operator `(3 c_l - 1) + c_l r d_r` annihilates the leading term `r^{k-3}` of the factor, and `eps~ = x^2 y B_inf`
  with `|D^alpha B_inf| <= C r^{2k-4-|alpha|}` (`|alpha| <= 4`). These bounds are derived from the finite power and
  log-polynomial formulas of the trial and of its canonical velocity, with the velocity quotients by the segment
  formula; on compact annuli the finite radial mode equations give a `C^6` velocity, so the residual quotient is `C^4`
  there. On dyadic shells, as in the weak weights item, the small shells decay at the geometric rate `lambda^{6-a-s}`
  up to powers of `|log lambda|` when `a < 5/2`, and the transformed large shells have `H^4` bound `C lambda^{2k-a}`,
  summable when `a > 2k`. Necessity: for `a >= 5/2` by the rectangle of the previous item; for `a <= 2k` by the
  exterior expansion `eps~ = e^{(2k-1) tau} Phi(theta) + o(e^{(2k-1) tau})`, uniform in angle (`tau = log(r/R_b)` as
  in section 2, so `Phi = R_b^{2k-1} Eps`), rederived in the proof: two computations using exact binary64 inputs and
  the shared normalization enclosure give the `sin 3 theta` coefficient of Phi,
  `-966216463877/10^15 < e_1 < -966216463875/10^15` (in the normalization of `e_0` in section 2). Hence
  `|eps~| >= c r^{2k-1}` for large r on a sector inside `x > 0` away from both axes, and the squared norm dominates a
  positive multiple of `int^infinity r^{4k-2a-1} dr`, which diverges exactly when `a <= 2k`. The statement is
  qualitative: no ceiling for the norm and no bound uniform in a near either endpoint is asserted. At these weights
  `a < 5/2 < a_Y(153/50)`, so `T_0` is not Fredholm there (range inside the strip item), and the frozen graph domain
  item applies; no inverse, forcing estimate, error bound for X3 or exclusion of an exact profile follows.
- Strain functional (verified, with its own proof, and the constant below in two implementations with different
  algorithms and libraries; also checked in two completed referee reviews, a separate adjudication and a separate
  referee audit). For a smooth compact density h of the required parities vanishing near 0,
  `c[h] = psi[h]_xy(0) = (1/pi) int h r^{-3} sin(3 theta) dX`. If `s >= 0`, `0 <= a < 2` and `s + a > 2`, c extends
  from the smooth compact densities of the required parities supported away from `x = 0` to a bounded linear
  functional on the real odd-y subspace of `Y_(a,s)`, with `|c[h]| <= C_(a,s) ||h||_Y` and
  `C_(a,s)^2 = Gamma(2a+1) Beta(2-a, s+a-2) / (pi 2^{2a+2})` (an upper bound, not claimed sharp; here `Gamma` and
  `Beta` denote Euler's gamma and beta functions); the extension agrees with the canonical strain for every h in
  `Y_(a,s)` with `|h| <= C r^3` near 0 and `|h| <= C (1 + r)^gamma`, `gamma < 1`, at infinity. Mechanism: c is the
  pairing of the restriction of h to `x > 0` with the kernel `2 y (3 x^2 - y^2) / (pi r^6) = d_x d_y P_x(y)`,
  `P_x(y) = x / (pi (x^2 + y^2))`, and this mixed-derivative kernel has unitary Fourier transform in y equal to
  `-(2 pi)^{-1/2} i eta |eta| e^{-x |eta|}`; the weight and the Jacobian `dx = x dz` turn it into a pairing on
  `R^2_(z,y)`, and Cauchy-Schwarz in the y-frequency gives the gamma and beta integrals. For every `a >= 2` and every
  finite `s >= 0`, c is unbounded on the smooth compact densities of the required parities supported away from both
  axes, measured in `Y_(a,s)`: for a dilation factor `R >= 1`, the rescaled annular densities `R^{a-1} h_*(X/R)` with
  `c[h_*] > 0` have bounded norm and strain `R^{a-2} c[h_*]` (for `a > 2`), and normalized sums over separated scales
  handle `a = 2`. Hence at `s = 153/50`, among `a >= 0`, c is bounded on `Y_(a,s)` exactly when `a < 2`. At
  `(a, s) = (3/2, 153/50)`, `0.263445900664 < C_(a,s) < 0.263445900665` (gamma quotients in ball arithmetic and,
  separately, a beta reduction with two positive series with rigorous tails and a Machin enclosure of pi in interval
  arithmetic), so the scaling coefficient of L satisfies `|c[h]|/3 <= 0.087815300222 ||h||_Y` there; `a = 3/2` lies in
  the membership interval of the trial's residual (previous item). No domain, inverse or operator bound of L follows.
- Scaling term (verified, with its own proof, the leading exterior coefficient below in two exact decoders and the
  centre identity in two symbolic implementations, with different libraries; also checked in three completed referee
  reviews (the second after a written response and the third after a correction), a separate adjudication and a
  separate referee audit). For the exactly joined trial and `s = 153/50`, among `a >= 0`, `rho~` and `X.grad rho~` lie
  in `Y_(a,s)` if and only if `1 + k < a < 5/2` (`1 + k` is about 1.17936). On the real odd-y subspace of `Y_(a,s)`,
  the scaling term `R_c h = (c[h]/3) X.grad rho~` of L, defined on the smooth compact densities of the required
  parities supported away from `x = 0`, extends to a bounded operator on that subspace if and only if `1 + k < a < 2`;
  there the extension is unique, of rank one and compact, with `||R_c|| <= C_(a,s) ||X.grad rho~||_Y / 3` (`C_(a,s)`
  of the previous item). For the smooth compact densities h of the required parities supported away from both axes,
  now without the condition `c[h] = 0`, all images `L h` lie in `Y_(a,s)` if and only if `1 + k < a < 5/2`, also when
  the supports are restricted to `1 < r < 2`; for one such h with `c[h] != 0` and `0 <= a < 5/2`, `L h` lies in
  `Y_(a,s)` if and only if `a > 1 + k`. Mechanism: with `E_x = x d_x`, near 0 the differences `rho~ - x^2 y` and
  `X.grad rho~ - 3 x^2 y` satisfy `|E_x^p d_y^q (.)| <= C x^2 r^{3-q}` (`p + q <= 4`), and smooth compact cut-offs of
  `x^2 y` lie in `Y_(a,N)` for every nonnegative integer N when `a < 5/2` (the axis integral is `int_0 x^{4-2a} dx`);
  at infinity `|E_x^p d_y^q g| <= C x^2 r^{k-2-q}` for `g = rho~` and `g = X.grad rho~`, so the transformed large
  shells have `H^4` bound `C lambda^{k+1-a}`, summable when `a > 1 + k`. Necessity: uniformly in angle
  `r^{-k} rho~ -> Theta_M` (section 2) and `r^{-k} X.grad rho~ -> k Theta_M`, where
  `Theta_M = R_b^{3-k} cos^2 theta sin theta P_tail(theta)` (`R_b` the last knot, section 2) with a cosine polynomial
  `P_tail` whose `cos 2 theta` coefficient is the exact nonzero dyadic rational
  `-5663579610707223/37778931862957161709568` decoded from the stored data (consistent with `Theta_M(pi/4) > 90`,
  section 2), so both functions are at least `c r^k` on a sector inside `x > 0` away from both axes for large r, and
  the squared norm dominates a positive multiple of `int^infinity r^{2k-2a+1} dr`, which diverges exactly when
  `a <= 1 + k`; at a fixed small `y > 0`, `rho~/x^2 -> y + O(y^3)` and `X.grad rho~ / x^2 -> 3 y + O(y^3)` as
  `x -> 0+`, which gives the axis rectangle for `a >= 5/2`. If `a <= 1 + k` or `a >= 5/2`, `X.grad rho~` is not in the
  space and an annular h with `c[h] > 0` gives `R_c h` outside it; for `2 <= a < 5/2` the rescaled densities of the
  previous item have bounded norm and unbounded strain. For the compact test images: near 0,
  `U[h] = c[h] (-x, y) + (x w_1, y w_2)` with `|D^alpha w_i| <= C r^{2-|alpha|}` (`|alpha| <= 4`), and, writing
  `rho~ = x^2 y f`, `U[h].grad rho~ + (c[h]/3) X.grad rho~ = x^2 y B_h` with
  `B_h = (c[h]/3)(-2 x d_x f + 4 y d_y f) + w_1 (2 f + x d_x f) + w_2 (f + y d_y f)` (the coefficients of `c[h] f` are
  `-2 + 1 + 1 = 0`), so `|D^alpha B_h| <= C r^{2-|alpha|}` near 0 for every value of `c[h]`, and the shell argument of
  the weak weights item applies for `a < 5/2`; at infinity `U[h].grad rho~ = O(r^{k-4})`, with the corresponding
  differentiated bounds (the source `d_x h` of the stream equation has vanishing mass and first moments), so for
  `c[h] != 0` the slowest term of `L h` is `(c[h]/3) k Theta_M r^k`. The statement is qualitative: no value of
  `||rho~||_Y`, `||X.grad rho~||_Y` or `||R_c||` is computed. At these weights `T_0` is not Fredholm (range inside the
  strip item), and the frozen graph domain item, whose densities have `c[h] = 0`, is unaffected; no inverse or
  operator bound of the full L follows.
- Frozen graph domain (verified, with its own proof, the phase, Laplacian and velocity identities in two symbolic
  implementations and the scalar bound in two exact ones, with different libraries; also checked in two completed
  referee reviews (the second for the compact construction), a separate adjudication and a separate referee audit).
  Let `Dom(T_0)` be the maximal domain of `T_0` in `Y_(a,s)` with the graph norm `||h||_Y + ||T_0 h||_Y` (a Banach
  space, since `T_0` is closed), and let L be the linearization at the exactly joined trial. For `s = 153/50` and
  every real a there are real smooth densities `h_n = -Lap f_n` (`n = 1, 2, ...`) of the required parities, with `f_n`
  supported in one fixed compact set at positive distance from both axes, such that
  `sup_n (||h_n||_Y + ||T_0 h_n||_Y) < infinity`, every `L h_n` lies in `Y_(a,s)`, and `||L h_n||_Y -> infinity`. The
  stream `d_x f_n` and the velocity `(-d_xy f_n, d_xx f_n)` are supported in the same set, and this velocity is
  `U[h_n]` (its difference from the canonical velocity is harmonic, sublinear and of the velocity parity, hence zero),
  so `J(h_n) = c[h_n] = 0` and all interior harmonic coefficients vanish; these densities are not in `T_ann` (their
  supports lie near the source P, where `r > 8`), but they share the last property of the compatible densities above.
  Mechanism: on the patch `x > 0`, `y > 0` the phase `phi_fr = D log x + A log y` satisfies
  `(-A x d_x + D y d_y) phi_fr = 0`, while for the transport field `V = c_l X + U[rho~]` of the trial
  `V.grad phi_fr = D V_1/x + A V_2/y` is at least `43590141723577828524328261933/4341702632208580842156250000` (above
  10.0398) on the rectangle `|x - p| < 10^{-4}`, `1/2000 < y < 3/2000`, by Taylor's formula with `V(P) = 0`,
  `DV(P) = diag(A_P, mu)`, `0 < A_P < 51/5`, `mu > 99/100`, `p > 43/5` and `||D^2 V||_F < 0.2972` on `B_{0.0495}(P)`
  (5(o), where `A_P = d_x V_1(P)` is denoted A; the closed rectangle lies in this disc). Take a fixed nonzero smooth
  function `g_0` with compact support in the image of this rectangle under `(x, y) -> (log x, y)`, put
  `f_n^C = n^{-s-2} x^{a-1/2} g_0(log x, y) e^{i n phi_fr}` on the original `(x, y)` rectangle, then extend evenly in
  x, oddly in y and by zero elsewhere. In the following conjugated formulas put `x = e^z` and read `phi_fr` as
  `D z + A log y`; `V.grad phi_fr` denotes the physical expression evaluated at `(e^z, y)`, and `g_0` means
  `g_0(z, y)`. For the complex densities `h_n^C = -Lap f_n^C`, on the positive patch `F_{h_n^C}` and `F_{T_0 h_n^C}`
  (notation of the range item) are sums of fixed smooth compactly supported amplitudes times
  `n^{-s-j} e^{i n phi_fr}`, `j = 0, 1, 2`, bounded in `H^s` by interpolation between `L^2` and `H^4` (the reflected
  pieces likewise); the velocity coupling has compactly supported `C^4` amplitudes at the same powers, since rho~ is
  `C^6` near the supports, and is bounded in the same way. With a smooth cutoff `chi_+` in the positive patch, equal
  to 1 near the support there, `F_{chi_+ L h_n^C} = i n^{1-s} q_fr e^{i n phi_fr} + E_n` with
  `q_fr = (D^2/x^2 + A^2/y^2) g_0 V.grad phi_fr` nonzero and `sup_n ||E_n||_{H^s} < infinity`, and a partial Fourier
  transform in z gives `||chi_+ L h_n^C||_Y >= c_1 n - C_1` for constants `c_1 > 0` and `C_1 >= 0` independent of n
  (they may depend on a). Finally `f_n` is the real or the imaginary part of `f_n^C`, whichever gives the larger
  localized image norm (a loss of at most a factor `sqrt 2`); multiplication by `chi_+` is bounded on `Y_(a,s)`, so
  the global norms `||L h_n||_Y` also tend to infinity. Consequence, by the closed graph theorem: no closed linear
  operator on `Y_(a,s)` whose domain contains `Dom(T_0)` agrees with L on these densities, and no bounded linear map
  from `Dom(T_0)` into `Y_(a,s)` agrees on them with L or with `L - T_0`; so, at the weights where the frozen inverse
  of the first item exists, it cannot be transferred to L by treating `L - T_0` as a `T_0`-bounded or `T_0`-compact
  perturbation on `Dom(T_0)`. Domains not containing `Dom(T_0)` (for example the graph domain of the actual
  transport), other norms, an inverse of L elsewhere and the existence question are not concerned.
- Centre trace (verified, with its own proof, the Laplacian, velocity, physical two-term scaling, conjugation and
  centre identities in two symbolic implementations (a computer algebra system and a separate rational differential
  ring), and the frozen coefficients of the trial in two exact decoders; also checked in four completed referee
  reviews (the second after a written response, the third and fourth after corrections), a separate adjudication and a
  separate referee audit). Let J be the centre trace of section 4 (the value at 0 of the factor `h/(x^2 y)`). For
  every real `a < 5/2` and every finite `s >= 0` there are real smooth compactly supported densities
  `h_delta = -Lap f_delta`, `0 < delta <= 1`, of the required parities, with
  `f_delta = -x^4 chi(x/delta) y chi(y) / 12` (chi a smooth even cutoff, equal to 1 on `[-1, 1]` and to 0 outside
  `[-2, 2]`), such that `h_delta = x^2 y` near 0, so `J(h_delta) = 1`, `h_delta / (x^2 y)` is smooth,
  `c[h_delta] = 0`, the canonical velocity `(-d_xy f_delta, d_xx f_delta)` has compact support, and
  `||h_delta||_Y + ||T_0 h_delta||_Y -> 0` as `delta -> 0`. Mechanism:
  `h_delta(x, y) = delta^2 H_2(x/delta, y) + delta^4 H_4(x/delta, y)` with fixed smooth `H_2`, `H_4` (symbols local to
  these two centre trace items; the subscripts are powers of delta), so in the variables `(z, y)` the transformed
  density is `delta^{5/2-a}` times a fixed function lying in every `H^N(R^2)`, translated by `log delta` in z, plus
  `delta^{9/2-a}` times another such function (the factor `x^{5/2-a}` makes all Euler and y derivatives square
  integrable at `z -> -infinity` because `a < 5/2`); translation in z is unitary on `H^s`, and `T_0` is conjugated to
  `-A d_z + D y d_y + A(1/2 - a) - 1`, which commutes with it. Consequently, on the smooth compact densities of the
  required parities with smooth factor `h/(x^2 y)` and `c[h] = 0`, J is not closable in the norm of `Y_(a,s)` or in
  the frozen graph norm, no closed linear functional extending J has a domain containing them, and the subspace
  `J = 0` is not closed and is dense in this class (`h - J(h) h_delta -> h`); the affine class `J = 1` is not closed
  either. So in these topologies the centre normalization (`J(h) = 0` for corrections, `J = 1` for profiles) is not a
  closed constraint; a trace norm, a stronger topology or a smaller domain would be needed. Nothing is asserted at
  `a >= 5/2` or about existence; the graph norm of L is treated in the next item.
- Centre trace in the graph norm of L (verified, with its own proof, the density, velocity, transport conjugation,
  coupling, weight-power, polynomial and radial Poisson identities in two symbolic implementations (a computer algebra
  system and a separate rational differential ring), and the parameters, the 1573 knots and the 260 angular source
  maps of the trial in two exact decoders; also checked in four completed referee reviews (the second after a written
  response, the third and fourth after corrections), a separate adjudication and a separate referee audit). Let L be
  the linearization at the exactly joined trial (section 2). For every real `a < 5/2` and every `0 <= s < 4` the
  densities `h_delta` of the centre trace item also satisfy
  `||h_delta||_Y + ||L h_delta||_Y <= C_graph(a,s) delta^{5/2-a}` for `0 < delta <= 1`, where `C_graph(a,s)` is finite
  and has no computed numerical bound (it is not the strain constant `C_(a,s)` of the strain item above). Mechanism:
  the scaling term vanishes because `c[h_delta] = 0`, and `U[h_delta]` has compact support. Near 0 the canonical
  velocity of the trial is a polynomial of degree at most 3 plus a remainder `R_U` with
  `|D^j R_U| <= C r^{5-j} (1 + |log r|^{M_log})`, `j <= 5`, for an integer `M_log >= 0` (the trial has finitely many
  angular modes, each solved by a radial Green function, and the sublinear gauge excludes further homogeneous
  velocities), so the coefficients `p_log = V_1/x = int_0^1 d_x V_1(t x, y) dt`, `V_2`, `d_x rho~` and `d_y rho~`,
  where `V = c_l X + U[rho~]`, are `C^{3,alpha}` for every `0 < alpha < 1` on a fixed rectangle containing the
  supports. Put `beta = 1/2 - a`, `F_delta(z, y) = e^{beta z} h_delta(e^z, y)`, `w = z - log delta` and
  `F_j(w, y) = e^{beta w} H_j(e^w, y)` for `j = 2, 3`, with `H_2` as in the centre trace item and
  `H_3(u, y) = (u^4 chi(u))' (y chi(y))' / 12`, so that `U_1[h_delta] = delta^3 H_3(x/delta, y)` and
  `U_2[h_delta] = -delta^2 H_2(x/delta, y)`. Then the weighted transport part of L is exactly
  `p_log(e^z, y) (d_z - beta) F_delta + V_2(e^z, y) d_y F_delta - F_delta`, and the weighted coupling is
  `delta^{7/2-a} d_x rho~(e^z, y) F_3(w, y) - delta^{5/2-a} d_y rho~(e^z, y) F_2(w, y)`. After extending each
  coefficient c with a compact cutoff, it is used in the form `c(delta phi(w), y)`, where `phi(w) = e^w` for
  `w <= log 2` and phi is positive, bounded and smooth with bounded derivatives; these pullbacks have `C^{3,alpha}`
  norms bounded uniformly in delta, hence uniform multiplier bounds on `H^s(R^2)`. This uses `s < 4`: functions with
  bounded `C^{m,alpha}` norm multiply `H^{m+theta}` for `m = floor(s) <= 3` and `s - m = theta < alpha`. Consequently,
  on the smooth compact densities of the required parities with smooth even-even factor `h/(x^2 y)`, `c[h] = 0` and
  `L h` in `Y_(a,s)`, J is not closable in the graph norm `||h||_Y + ||L h||_Y`, the subspace `J = 0` is not closed
  and is dense in this class, and the affine class `J = 1` is not closed. Hence the normalization does not improve the
  inverse inequality `||h||_Y <= C ||L h||_Y`: a finite C is valid on this class if and only if it is valid on its
  subspace `J = 0` (for fixed h, `h - J(h) h_delta -> h` in the graph norm and both sides pass to the limit;
  continuity of J is not used), so the two best constants in `[0, infinity]` agree, and the same holds for the
  closures of the two classes in the graph norm; neither constant is shown to be finite (verified separately, with its
  own proof, the polarization and correction identities in two symbolic implementations and eight manufactured rank
  cases rebuilt by exact elimination, as regression checks only; also checked in two completed referee reviews, a
  separate adjudication and a separate referee audit). For a closed linear realization of L in `Y_(a,s)` whose domain
  contains the `h_delta`, no linear functional on that domain that extends J is closed with respect to the graph norm.
  In particular, at `s = 153/50` and `1 + k < a < 2` the centre normalization is not a closed constraint in the graph
  norm of L either. Nothing is asserted at `s >= 4` (open) or `a >= 5/2`, on whether L is closed or invertible, on the
  size of `C_graph(a,s)`, or on existence.
- Quadratic term in the graph norm of L (verified, with its own proof and a mandatory addendum correcting its ball
  quantifier, the Poisson, plateau, wave expansion, transport phase, cross-term, reflection and polarization
  identities in two symbolic implementations (a computer algebra system and a separate rational differential ring),
  and the ten parameters of the trial in two exact decoders; also checked in three completed referee reviews (the
  second after the addendum, the third after a written response), a separate adjudication and a separate referee
  audit). Let L be the linearization at the exactly joined trial and `Q(h) = W[h].grad h` the quadratic term of
  section 7. Let `K_cp` be the union of a sufficiently small open disc about `P_cp`, chosen as below, and its three
  reflected copies, with closures avoiding both axes and lying in the punctured disc about 0 on which the centre
  formulas of the trial are smooth, and let `D_cp = {-Lap f : f in C_c^infty(K_cp), f even in x and odd in y}`. For
  these densities `J = c = 0`, every centre jet vanishes and the canonical velocity `(-d_xy f, d_xx f)` has compact
  support (the sublinear gauge admits no further harmonic velocity). For every real a and every finite `s >= 0` there
  are `g_cp` and `h_n`, `n >= 1`, in `D_cp` with
  `||g_cp||_Y + ||L g_cp||_Y + sup_n (||h_n||_Y + ||L h_n||_Y) < infinity` and
  `||U[g_cp].grad h_n + U[h_n].grad g_cp||_Y >= c_cp n - C_cp`, `c_cp > 0`. Mechanism: since `V_1(t, t) = -A t + o(t)`
  with `A > 0`, there is a point `P_cp = (t, t)` with `V_1(P_cp) != 0`; flowing the vertical line through `P_cp` along
  V gives a smooth first integral phi near `P_cp` with `V.grad phi = 0` and `phi_y > 1/2`. The density `g_cp` is
  `-Lap` of a cutoff of `(x - t)^2/2`, extended by parity, so that `g_cp = -1`, `grad g_cp = 0` and `U[g_cp] = (0, 1)`
  on a disc about `P_cp`. On the positive patch `h_n = -Lap(n^{-s-2} a_cp cos(n phi))`, with a nonzero smooth
  amplitude `a_cp` supported in that disc, and the potential is extended by parity. Then `h_n`, `U[h_n]` and `L h_n`
  are sums of `n^{-s-j}`, `j = 0, 1, 2`, times fixed smooth compact amplitudes times `cos(n phi)` or `sin(n phi)` (the
  transport does not differentiate the phase). In flow coordinates Fourier translation gives
  `n^{-s} ||B exp(i n v)||_{H^s} -> ||B||_2` for every fixed smooth compact amplitude B (the sine and cosine limits
  are `||B||_2/sqrt(2)`), and smooth chart changes and the logarithmic weight give equivalent norms on these fixed
  compact patches; hence these terms are bounded in `Y_(a,s)`. Globally `U[h_n].grad g_cp = 0`, since `U[h_n]` is
  supported where `grad g_cp = 0`, and on the positive patch `U[g_cp].grad h_n = d_y h_n`, whose leading term
  `-n^{1-s} a_cp |grad phi|^2 phi_y sin(n phi)` has `Y_(a,s)` norm at least a positive multiple of n after
  localization to that patch. With `v_n^{+-} = n^{-1/2} (g_cp +- h_n)`, the polarization identity
  `Q(h_1 + h_2) - Q(h_1 - h_2) = 2 (U[h_1].grad h_2 + U[h_2].grad h_1)` on `D_cp` (where `c = 0`) gives
  `||v_n^{+-}||_Y + ||L v_n^{+-}||_Y -> 0` and `liminf max(||Q(v_n^+)||_Y, ||Q(v_n^-)||_Y) >= c_cp > 0`; only the
  maximum is bounded below. Consequently Q has no continuous extension at 0 from `D_cp`, with the graph norm
  `||h||_Y + ||L h||_Y`, into `Y_(a,s)`: for every `r > 0` there is no constant `C_r` with
  `||Q(h)||_Y <= C_r (||h||_Y + ||L h||_Y)^2` for all h in `D_cp` of graph norm below r. The same holds on every
  larger domain whose norm on `D_cp` is at most a fixed multiple of this graph norm, and for the residual difference
  `F(rho~ + h) - F(rho~) = L h + Q(h)`. Conditions at the centre (J, c, any finite set of centre jets) do not remove
  these packets. More generally, for any real linear map `Lambda_cp` from `D_cp` to `R^m`, m finite, with no
  continuity assumption, the same conclusion holds on `ker Lambda_cp`, hence on every linear subspace of `D_cp` of
  finite algebraic codimension, closed or not. Proof: choose `(m+1)^2` disjoint discs inside the disc about `P_cp`, in
  `m+1` groups of `m+1`, each carrying a plateau potential as above. In each group the `m+1` images under `Lambda_cp`
  are linearly dependent; a nonzero dependence gives a combination in `ker Lambda_cp` that is nonzero (the potentials
  have disjoint supports) and has a plateau with zero density gradient and vertical velocity `(0, t_i)`, `t_i != 0`,
  on one disc `T_i` of the group. Their sum is a new background, again denoted `g_cp`, in `ker Lambda_cp` with `m+1`
  such plateaus. On each `T_i` place a packet `h_(i,n)` as above; for each n a nonzero dependence among the `m+1`
  images `Lambda_cp(h_(i,n))`, normalized so that its largest coefficient has absolute value 1, gives `k_n` in
  `ker Lambda_cp` with graph norm at most the sum of those of the `h_(i,n)`. Fix a smooth cutoff supported in each
  positive `T_i`, equal to 1 near the support of its packet amplitude. At an index whose coefficient has absolute
  value 1, multiplication by that cutoff selects exactly the coefficient times that packet's positive-patch cross term
  (a support identity). The finitely many fixed cutoffs have bounded multiplier norms on `Y_(a,s)`, uniformly in n, so
  `||U[g_cp].grad k_n + U[k_n].grad g_cp||_Y >= c_Lambda n - C_Lambda` with `c_Lambda > 0` and constants depending on
  `Lambda_cp`, m, a and s; the same polarization is applied to `n^{-1/2} (g_cp +- k_n)`, and again only the maximum of
  the two outputs is bounded below. (The case of graph-continuous `Lambda_cp` was verified first, with the
  inverse-constant statement of the preceding item and the same evidence, through a bounded finite correction into the
  kernel; the general finite case was verified separately with its own proof, two independent exact rational
  reconstructions of 56 manufactured finite systems covering rank zero, deficient and full rank, which test the two
  eliminations and do not prove the general statement, three completed referee reviews, a separate adjudication and a
  separate referee audit.) The preceding argument treats finite linear constraints only. Regular finite nonlinear
  constraints (verified with a separate proof, six quadratic perturbation identities in two exact implementations and
  21 manufactured scalar root and scaling examples rebuilt independently, as regression checks only; also checked in
  two completed referee reviews, a separate adjudication and a separate referee audit): write
  `||h||_G = ||h||_Y + ||L h||_Y`, let Omega be a neighbourhood of 0 in `D_cp`, open for this norm, and let
  `Phi_cp : Omega -> R^m`, m finite, be continuously Frechet differentiable for this norm, with `Phi_cp(0) = 0` and
  `DPhi_cp(0)` onto `R^m`. Then there are `z_n^+` and `z_n^-` in Omega with `Phi_cp(z_n^+) = Phi_cp(z_n^-) = 0`,
  `||z_n^+||_G + ||z_n^-||_G -> 0` and `liminf max(||Q(z_n^+)||_Y, ||Q(z_n^-)||_Y) > 0`; hence the conclusion above
  holds on the zero set of `Phi_cp` near 0, for Q and for `L h + Q(h)`, with constants depending on `Phi_cp`, m, a and
  s. Proof: the linear case applied to `Lambda_cp = DPhi_cp(0)` gives `g_cp` and `k_n` in its kernel; put
  `t_n = n^{-1/2}` and `y_n^{+-} = t_n (g_cp +- k_n)`. Choose `q_1, ..., q_m` in `D_cp` with `DPhi_cp(0) q_j = e_j`
  and put `R alpha = sum_j alpha_j q_j` for `alpha` in `R^m`. Since `Phi_cp(y) = o(||y||_G)` on the kernel and
  `||DPhi_cp(x) R - I|| <= 1/2` near 0, the map `alpha -> alpha - Phi_cp(y + R alpha)` is a contraction of the
  Euclidean ball of radius `2 |Phi_cp(y)|` into itself, so `Phi_cp(y_n^{+-} + R alpha_n^{+-}) = 0` with
  `|alpha_n^{+-}| = o(t_n)`; only the completeness of `R^m` is used, not that of `D_cp` or closedness of L. On `D_cp`
  (where `c = 0`) `Q(y + w) - Q(y) = U[y].grad w + U[w].grad y + Q(w)`; the packets satisfy `||U[k_n]||_Y <= C` and
  `||grad k_n||_Y <= C n`, and multiplication by `U[q_j]` and `grad q_j` is bounded on functions supported in `K_cp`,
  so the corrections change `Q(y_n^{+-})` by at most `C t_n n |alpha_n^{+-}| + C |alpha_n^{+-}|^2 = o(1)` and the
  positive lower limit of the maximum survives. The case `m = 0` is the linear case. Surjectivity cannot be dropped in
  a statement of this generality: `Phi_*(h) = ||h||_Y^2 + ||L h||_Y^2` is a continuous quadratic form in the graph
  norm, hence smooth, with `DPhi_*(0) = 0` and zero set `{0}`, on which Q is continuous. Singular constraints and
  infinitely many constraints are not treated, and a proposed normalization or phase condition is covered only after
  its graph differentiability and the surjectivity of its derivative at 0 have been proved. This proves the conclusion
  of 5(g) directly in these logarithmic graph norms at the trial, for every weight, including `1 + k < a < 2` at
  `s = 153/50`. Nothing is asserted for a stronger domain norm, a weaker image norm or a scale of spaces (the two-norm
  design of section 7 measures Q in a weaker target), on whether L is closed or invertible, on the size of the
  constants, or on existence.
- Scope. These results concern the frozen centre transport, the mapping of the compact test classes (into and out of
  the spaces), the frozen graph domain, the exactly joined trial and its residual, and the strain functional, the
  scaling term, the centre trace and the quadratic term. A domain on which L maps into `Y_(a,s)` with `a >= 5/2` must
  exclude every density of `T_ann,0` with a nonzero moment `Gamma_n`. A domain of a closed linear realization of L in
  `Y_(a,s)`, `s = 153/50`, cannot contain `Dom(T_0)`, for any real a. For every real `a < 5/2` and finite `s >= 0` the
  centre trace J is not closable on the smooth compact densities with `c[h] = 0` and smooth even-even factor
  `h/(x^2 y)` in `Y_(a,s)` or in the frozen graph norm (centre trace item), and for `0 <= s < 4` also in the graph
  norm of L on the densities of this class with `L h` in `Y_(a,s)` (centre trace in the graph norm of L item). For
  every real a and finite `s >= 0` the quadratic term is not continuous at 0 from the graph norm of L into `Y_(a,s)`,
  already on the compact-potential class `D_cp` (quadratic term in the graph norm of L item). A bounded inverse of the
  full L on a domain not containing `Dom(T_0)` (for example on the compatible densities, or on the graph domain of the
  actual transport) is neither proved nor excluded. For `0 <= a < 5/2` and `0 <= s < 6 - a` the compact test densities
  with `c[h] = 0` supported away from both axes are mapped into `Y_(a,s)` (weak weights item). The trial's residual
  lies in `Y_(a,153/50)`, `a >= 0`, exactly when `2k < a < 5/2`, where `T_0` is not Fredholm (residual at weak weights
  item). At `s = 153/50` the strain functional c is bounded on `Y_(a,s)`, `a >= 0`, exactly when `a < 2` (strain
  functional item). At `s = 153/50` the trial and `X.grad rho~` lie in `Y_(a,s)`, `a >= 0`, exactly when
  `1 + k < a < 5/2`, the scaling term of L is bounded there exactly when `1 + k < a < 2` (then of rank one and
  compact), and the compact test densities supported away from both axes with `c[h] != 0` are mapped into `Y_(a,s)`,
  `0 <= a < 5/2`, exactly when `a > 1 + k` (scaling term item). No full mapping classification outside the stated
  weight and order range is claimed here. The density of the mapping obstruction is not mapped into the quadrant norms
  of 5(e) with `a >= 5/2` either (5(e), last item). These results establish neither nonlinear closure nor a stationary
  profile.

(r) Centre quasimodes in the weighted factor supremum norm (verified, with its own proof and two exact implementations
of the finite identities; also checked in four completed referee reviews, two of them follow-ups, three separate
adjudications and a separate referee audit). Let `0 < k < 1`, `L > 0`, `W(r) = (1 + r^2/L^2)^{(k-3)/2}` (the weight of
the axis control of section 4), and let `B_F` be the real Banach space of densities `h = x^2 y W b` with b continuous
on the plane, even in both coordinates, `b(0) = 0` and `b -> 0` at infinity, normed by `||h||_F = sup |b|`. Assume
that `rho = x^2 y a` with a even in both coordinates, continuous, `a(0) = 1`, `C^1` off 0 and
`|a| + r |grad a| <= C W`, and that `U[rho]` is locally `C^1` with `|DU[rho](X) - diag(-c, c)| <= H r^alpha` for
`r <= 1`, some `alpha > 0` and `c = 3 c_l - 1`. The exactly normalized modal trial satisfies these hypotheses
(qualitatively, from its finite inner and outer formulas and the canonical velocity regularity; no constants are
computed). Then there are smooth compactly supported densities `z_j` in `B_F` of the required parities, vanishing near
0, with `J(z_j) = c[z_j] = 0` and `L z_j` in `B_F`, such that `||z_j||_F = 1`, `||L z_j||_F -> 0` and `z_j -> 0`
weakly in `B_F`.
- Construction. For a radial function chi supported in an annulus in `r <= delta <= 1`, with `|chi| <= 1`,
  `d_x (x^2 y chi)` has only the angular modes `sin 2 theta` and `sin 4 theta`, and the canonical stream modes are
  `psi_2 = (r^2 J_1 - r^{-2} I_5)/8` and `psi_4 = -r^{-4} I_7/8`, with `I_5 = int_0^r s^5 chi ds`,
  `I_7 = int_0^r s^7 chi ds` and `J_1 = int_r^inf s chi ds`. Hence `c[x^2 y chi] = (1/4) int_0^inf s chi ds` and, from
  explicit bounds of the two modes and their logarithmic derivatives, `||DU[x^2 y chi]||_inf <= (7 + 3 B_1/8) delta^2`
  with `B_1 = sup |r chi'|`. Put `h_n = x^2 y chi_n`, `chi_n(r) = beta((-log r - n)/n)`, with beta smooth and
  supported in (0, 1), `0 <= beta <= 1` and `max beta = 1`; then `h_n` is supported in `e^{-2n} < r < e^{-n}` and
  `sup |r chi_n'| <= sup |beta'|/n`. With `V_0 = diag(c_l - c, c_l + c) X`, the normalization `c = 3 c_l - 1` gives
  `V_0.grad(x^2 y) = x^2 y`, so `(V_0.grad - 1) h_n = x^2 y (r chi_n') V_0.X/r^2` has factor norm `O(1/n)`; the
  remainder `U[rho] - diag(-c, c) X` contributes `O(e^{-alpha n})`, and the coupling and scaling terms contribute
  `O(e^{-2n})`. Subtracting `(c[h_n]/c[q]) q`, of norm `O(e^{-2n})`, for a fixed radial bump `q = x^2 y zeta(r)`,
  `zeta >= 0` nonzero and supported in `1 < r < 2`, makes the strain zero; the stream function then vanishes near 0
  and for `r > 2` is a combination of `r^{-2} sin 2 theta` and `r^{-4} sin 4 theta`, so the image lies in `B_F`. Along
  `n_j = 3^j` the supports of the `h_(n_j)` are pairwise disjoint and every finite signed sum of them has norm at most
  `1/W(1)`, so the `h_(n_j)` are weakly null; the strain corrections tend to 0 in norm, so normalizing the corrected
  subsequence gives `z_j`.
- Consequences. On any domain containing this sequence, no C gives `||h||_F <= C ||L h||_F`, nor
  `||h||_F <= C ||L h||_F + ||T h||_Z` for a bounded linear compact T from `B_F` into a Banach space Z (compactness
  turns weak into norm convergence); and every closed linear realization of L in `B_F` whose domain contains the
  sequence, and which agrees with L on it, fails to have both closed range and finite-dimensional kernel (otherwise
  the open mapping theorem on the graph domain bounds the distance from `z_j` to the kernel by a constant times
  `||L z_j||_F`, which tends to 0, and a limit in the finite-dimensional kernel contradicts `||z_j||_F = 1` and the
  weak limit 0), so it is not Fredholm. Thus the weighted factor supremum fails as the norm of an inverse estimate at
  the trial even on smooth compact densities with zero strain and vanishing centre and far coefficients, in addition
  to failing to control the interior velocity (section 4). Not covered: Hoelder or derivative norms of the factor,
  stronger domain norms, weaker target norms, domains that exclude the sequence, a bounded right inverse, and the
  existence or nonexistence of a profile near X3.

Why no global inverse: six obstructions stand in the way.
- No realization is known in which the source, the saddle at the origin, the invariant axes and infinity are all
  controlled.
- The isotropic Sobolev energy pairing at the saddle is indefinite (verified): for the frozen saddle operator the real
  part of the homogeneous `H^s` pairing has symbol `s(-A xi_x^2 + D xi_y^2)/|xi|^2 - (1 + c_l)`, which is
  `sD - (1 + c_l) > 0` in the y-frequency direction (for `s > 0.309`) and `-sA - (1 + c_l) < 0` in the x-frequency
  direction. So no energy coercivity holds in this pairing. This does not by itself exclude every isotropic inverse
  estimate (a bounded invertible operator can have an indefinite energy).
- Above threshold at P the frozen model has infinite cokernel, and for `s_fast < s < b_0`, under the hypotheses of
  5(d), the variable-coefficient operator is not Fredholm in ordinary `H^s` graph realizations.
- At the orders `b_0/A < s < s_fast` (`b_0/A` is about 0.6478; these orders include the orders near `s = 153/50` used
  in 5(o)), the straight frozen homotopy from pure transport to the coupled operator, with the coupling multiplied by
  `0 <= tau <= 1`, crosses the moving threshold `s = (tau g + b_0)/A`. Fredholm indices therefore cannot be
  transported along it. For `0 <= s < b_0/A` the path stays below threshold.
- In the diagnostic weighted `H^1`-type norm of section 10 and in the norms `X_m` of 5(p) (fixed integer `m >= 2`),
  the saddle at the centre produces quasimodes (5(p)), so no same-norm inverse estimate, even with a compact
  remainder, holds on domains that contain these quasimodes, and no closed realization in that norm containing them is
  Fredholm. In the weighted factor supremum norm of the axis control, on the space `B_F` of 5(r), slowly varying
  logarithmic annuli at the centre, after an exact strain correction, give unit weak-null quasimodes with zero strain,
  with the same consequences for bounded linear compact remainders and closed linear realizations (5(r)).
- In the axis-weighted norms `Y_(a,s)` of 5(q) the frozen centre transport is invertible for `a >= 0` exactly when
  `delta_Y < 0` (and for `s >= 3/2` all such weights have `a > 5/2`), but for `a >= 5/2` the full linearization does
  not map every smooth compact density with `J = c = 0` supported away from both axes into the space, nor into the
  quadrant norms of 5(e) with `a >= 5/2` (for `0 <= a < 5/2` and `0 <= s < 6 - a` it maps all of them into `Y_(a,s)`);
  for `a >= 5/2` and those supported in `1 < r < 2`, membership of the image in `Y_(a,s)` requires the vanishing of
  every interior even harmonic moment, a condition of infinite codimension; for `s = 153/50` and every real a no
  closed linear realization of L in `Y_(a,s)` has a domain containing the maximal domain of the frozen centre
  transport; the trial's residual is not in any of these spaces with `a >= 5/2` either, and for `s = 153/50` and
  `a >= 0` it lies in `Y_(a,s)` exactly when `2k < a < 5/2`, where `T_0` is not Fredholm (5(q)).

See section 10.

## 6. Residual tables
Certified enclosures in a norm with derivatives (as the correction norms proposed in this report require, sections 7
and 10): the X norms on the two radial end regions outside the annulus E defined below and a coarse direct bound of
the X norms on the whole plane (verified; see below); the sharper bounds on E are conditional. The numerical team
reports first- and second-derivative bounds from its own interval certificate chain (`sup r |grad eps~|/m <= 0.4195`
and, for every second partial derivative, `sup r^2 |partial^2 eps~|/m <= 713.2`; the largest cell bounds lie, by its
report, at the lobe next to P). One passage gives the approximate annulus `5.155e-5 <= r <= 8.228e10`, while other
passages use `8.244e10` as the outer cutoff. The coherent cells below cover an annulus with the latter approximate
upper cutoff; this geometry check does not verify either reported physical derivative bound. Its saved certificate
gives, for each radial cell, values `W_ij` meant to bound the `(i, j)`-th derivative in `(t, theta)`, `t = log r`, of
the residual on the cell, and a value `m_inf` meant to bound m from below there; put `A = (W_10 + W_01)/m_inf` and
`B = (W_20 + 2 W_11 + W_02 + W_10 + 2 W_01)/m_inf`. Reading the saved numbers as the binary64 values they encode, two
exact rational calculations verified `max A < 0.4195` and `max B < 713.2` over all 19389 saved cells, and two interval
methods enclosed every evaluated expression; the maxima occur at saved middle-region rows 4124 and 4123 respectively
and are maxima of saved expressions, not certified physical maxima. If the `W_ij` bound those derivatives of the exact
residual throughout each cell, `m_inf > 0` bounds m from below there, and the cells cover the stated annulus, then A
bounds `r |grad eps~|/m` (Euclidean norm of the gradient) and B bounds `r^2 |partial_i partial_j eps~|/m` for each
`i, j` in `{x, y}`, but not in general the Frobenius norm of the Hessian (verified implication). Those hypotheses (the
cell majorants, apart from the 63 on three cells verified below, the producer's original Taylor models and arithmetic,
the link between the producing execution and its source, the numerical canonical-moment inputs, the lower bound for
the weight, the coverage of the cells (verified only for the coherent cells below) and the extension of the reported
normalized pointwise derivative ceilings to the two radial end regions omitted from those tables (upper bounds for
their X norms are given below)) are not independently verified; neither reported physical derivative bound is verified
or used here. The coverage hypothesis fails for the saved cells as stored: reading the saved start and width of each
cell exactly, as the binary64 values they encode, with the end computed exactly, the 7809 middle cells cover their
hull in `log r` and overlap the adjacent inner and outer cells at both joins, but the 2632 inner and 8948 outer cells
leave 405 and 1563 open gaps between consecutive cells, of total length about `1.6e-13` and `9.9e-13` in `log r`
(largest about `6.4e-16` and `1.8e-15`) (verified by two exact methods, a rational merge and an integer endpoint
sweep). The saved certificate supplies no derivative bounds on these gaps. The verifier has checked a coherent
interpretation of the cells, intended by the producer, in which no gaps arise. Let `b_-` and `b_+` be the exact first
and last distinct knots of the trial in `log r`, and define the cells by exact rational nodes: `b_- - 5 + 5i/2632`
(`0 <= i <= 2632`) for the 2632 inner cells, the exact equal subdivision of each knot span for the 7809 middle cells,
and `b_+ + 17i/8948` (`0 <= i <= 8948`) for the 8948 outer cells. These closed cells cover
`b_- - 5 <= log r <= b_+ + 17`, that is the annulus E of about `5.155e-5 <= r <= 8.244e10`; each exact start lies in
the producer's input box for that start, each exact width is at most the saved width `h_i`, and the saved starts
`ahat_i` differ from the exact starts by at most `delta = 1677/629659522901737472` (about `2.7e-15`) (two exact
methods for all 19389 cells, with an exact emulation of the producer's binary64 computation of the widths and starts
from its current source; the producing execution is not authenticated). With `v(t) = L^2 u^{-4} (1 + u^2)^{3/2 - k}`,
`u = e^t/L`, which is decreasing in t, the verified theorem states: if the saved `W_ij` bound the Wiener sums
`sum_N (2N + 1)^j |partial_t^i eps~_N|` throughout each exact cell for `(i, j)` in
`{(0, 0), (1, 0), (2, 0), (0, 1), (1, 1)}`, and `eps~(t, theta) = sum_{N >= 0} eps~_N(t) sin((2N + 1) theta)`, and
either the expansion is finite with each coefficient `C^2` in t on an open neighbourhood of `[b_- - 5, b_+ + 17]`, or
the expansion is countable and both `eps~` and `eps~ - partial_t eps~`, together with their weak first derivatives,
are limits of their partial sums in the weighted L2 spaces defining `X(E)`, then, with
`alpha_i = W_00^2 + W_10^2 + W_01^2` and `beta_i = (W_00 + W_10)^2 + (W_10 + W_20)^2 + (W_01 + W_11)^2` formed from
the saved values of cell i, the X norm with the integration restricted to E satisfies
`||eps~||_{X(E)}^2 <= pi exp(4 delta) sum_i h_i v(ahat_i) alpha_i` and
`||eps~ - partial_t eps~||_{X(E)}^2 <= pi exp(4 delta) sum_i h_i v(ahat_i) beta_i`, with
`exp(4 delta) < 1.00000000000004`; here `eps~ - partial_t eps~ = L K` (section 10). The regularity premise is needed.
If a coefficient `eps~_N` is continuous and piecewise `C^2`, a jump `J` in its first t-derivative at an interior cell
boundary `t_0` contributes a Dirac mass with coefficient `-J` to the distributional t-derivative of
`eps~_N - partial_t eps~_N`. A nonzero such term prevents a square-integrable weak derivative. A jump in the second
derivative alone does not produce this term. For the exactly joined and exactly normalized trial this regularity
premise holds. On the punctured plane, the density and canonical velocity are `C^6` and the residual is `C^5`. Each of
its finitely many possibly nonzero odd sine coefficients is therefore `C^5` in `t = log r` on the whole real line,
across all spline knots and both radial joins. This regularity proof uses no numerical moment value (verified;
timeline 10-21 20:26). Set `S_A^2 = pi sum_i h_i v(ahat_i) alpha_i` and `S_B^2 = pi sum_i h_i v(ahat_i) beta_i`, with
nonnegative square roots `S_A` and `S_B`. Two accepted interval calculations over all saved rows give `S_A < 0.385655`
and `S_B < 585.873`. These definitions include the factor pi and exclude the weight correction `exp(4 delta)`. The
verified composition therefore gives, under the stated hypotheses, `||eps~||_{X(E)} < 0.385656` and
`||eps~ - partial_t eps~||_{X(E)} < 585.874` (two exact methods bind every saved row and both parameters to the cells,
and two interval methods enclose the weight correction). These are conditional upper bounds. The remaining
quantitative hypotheses are not verified for the physical residual: the validity of the saved majorants on these
cells, the producer's derivative models, arithmetic and remainders, the numerical canonical-moment inputs, and the
agreement of the inner and outer cell formulas with the exact trial. The theorem says nothing about radii outside E,
and neither bound enters a conclusion of this report. The two radial end regions outside E are bounded separately and
without these hypotheses (verified; own proof, also checked in two completed referee reviews and separate
adjudications; timeline 10-21 23:48): for the exactly joined and exactly normalized trial, with the X norm restricted
to the region, `||eps~||_X < 0.000002273735` and `||eps~ - partial_t eps~||_X < 0.000035059554` on
`r <= exp(b_- - 5)`, and `||eps~||_X < 0.000003926908` and `||eps~ - partial_t eps~||_X < 0.000006445150` on
`r >= exp(b_+ + 17)`. On the inner region the exact density expansion of the trial below its first knot is
differentiated in t exactly (two exact methods), the velocity derivatives are bounded by substituting into the Green
ODEs the velocity remainder bounds of the earlier analytic inner majorant on the whole inner disc,
`||U^rem_r/r||_W <= C_r r^2` and `||U^rem_theta/r||_W <= C_theta r^2` with explicit constants `C_r`, `C_theta` of that
majorant (see the inner certificate below; no inequality is differentiated), and the Leibniz rule, Parseval's identity
and the explicit radial integral give the norms. Here `U^rem = U[rho~] - (-c[rho~] x, c[rho~] y)` with the trial's
central strain `c[rho~] = 3/k - 1`, and `||f||_W` is the sum of the absolute values of the angular Fourier
coefficients of f at fixed r. On the outer region the finite exact exterior expansion of the residual is
differentiated termwise. Two exact rational methods reconstruct all 2992 product blocks and 10 nonleading linear
blocks from the saved constituent bounds of the earlier coarse exterior majorant (see the exterior certificate below),
in whose exact expansion the leading linear coefficient vanishes (`c_l k = 1`), assembling 3508 coefficient bounds;
for each coefficient, the larger of the saved and reconstructed upper endpoints is used. Every weighted radial
integral is evaluated by the exact factorial formula in 512-bit Arb and independently by an integration-by-parts
recurrence in 200-digit interval arithmetic. Both bounds inherit these two earlier majorants with their discharged
archive premise (timeline 10-21 21:34) and the regularity premise above. Since E and the two end regions cover the
plane, their boundary circles have measure zero, the residual is `C^5` on the punctured plane and its weak derivatives
extend across the origin, the squared norms add; under the unverified hypotheses of the theorem above this gives the
full-plane bounds `||eps~||_X < 0.385656000027` and `||eps~ - partial_t eps~||_X < 585.874000000002` (verified
conditional composition), which do not enter a conclusion of this report either.

First coarse whole-plane bounds (verified; own proof; timeline 10-22 08:49). Without the majorant hypotheses above,
`||eps~||_X < 245653983.313885102003858` and `||eps~ - partial_t eps~||_X < 30665526224.2484290248531`. On each of the
7809 middle cells the density enters through its verified degree-7 polynomial coefficient boxes (exact dyadic centres
and radii) and the canonical modal velocity quantities through the verified radial Taylor models (section 8; timeline
10-22 00:16 and 00:18); their log-radial derivatives of orders 1 and 2 are expressed by the linear Green ODEs of the
modes through these quantities and the density forcing, so that no derivative of a remainder bound is used. The
Leibniz expansion of `partial_t^p eps~`, `p <= 2`, is formed from exact integer polynomial products in the cell
variable and the angle, computed on every cell by direct integer multiplication and, independently, by modular
multiplication with a separately coded Chinese remainder reconstruction; the two agree on every coefficient. The
errors from the coefficient radii, the model remainders and the factor `r^2 = e^{2t}` (a scalar enclosure and a Taylor
polynomial of degree 12 with its remainder) are bounded in the Wiener norm by submultiplicativity, the angular
derivatives through the largest residual frequency 1043, and the integral of the decreasing weight `v` above over each
cell by the exact cell width times its value at the left end. On the inner disc `r <= exp(b_-)` the exact density
expansion below the first knot is differentiated exactly and the velocity derivatives are bounded through the Green
ODEs from the same velocity remainder bounds as for the end region above; on the exterior `r >= exp(b_+)` the
coefficientwise exterior majorant of the end-region bound above is integrated from `exp(b_+)` with exact radial
integrals. Every cell bound and the inner-disc and exterior terms are enclosed in 512-bit Arb and, independently, in
200-digit interval arithmetic; for each, the outward-rounded upper endpoints are added in exact rational arithmetic,
and an output audit repeats the middle sums in a different order. Each regional squared norm below is displayed as a
terminating decimal above the larger of the two upper endpoints, and the square of each displayed whole-plane bound
exceeds the exact sum of the three displayed regional values (checked in 512-bit Arb and in 220-digit interval
arithmetic, and by an exact integer replay). The squared norms on the middle annulus `b_- <= log r <= b_+`, the inner
disc and the exterior are at most 2.23642149354638943132127, 67.9898116895358306437308 and 60345879517978469.8955085
for `eps~`, and 6074661.94639141300035166, 16132.4321701281783711136 and 940374498610062020934.552 for
`eps~ - partial_t eps~`. In these first bounds the exterior term dominates; they are therefore far larger than the
conditional ones above, which remain conditional, and they verify none of the saved majorants. The bound is in the
diagnostic norm X only and is not a residual bound in a norm matched to a realization (section 4).

Sharper exterior term (verified; own proof; timeline 10-22 10:22). On the exterior `r >= exp(b_+)`, with
`tau = log r - b_+`, the residual is `E + P D_rho + S H`, where the radial input factors E, P, `D_rho`, S and H
(density and velocity modes) are finite sums of terms `exp(lambda tau) c(tau)` with polynomial coefficients affine in
the enclosed normalization scalar and the enclosed canonical transient coefficients. On each of 89 cells covering
`0 <= tau <= 17`, with exact rational endpoints, each term is replaced by its Taylor polynomial about the cell centre,
whose derivatives of orders `p <= 2` have remainders bounded from the convergent series (no real inequality is
differentiated) and checked against a second expansion of the differentiated input; the residual polynomial, with the
products of the velocity and density factors, is formed before any absolute value, by interval convolution and
independently by exact integer centre-radius convolution, compared on every coefficient; whole-cell Wiener bounds
`B_p` of `partial_tau^p eps~`, `0 <= p <= 2`, and `C_p` of `partial_theta partial_tau^p eps~`, `0 <= p <= 1`, follow
from Bernstein coefficients together with the discarded-degree and analytic remainder bounds (the angular derivative
through the largest frequency 1043); since the weight `v` decreases, each cell contributes at most pi times its exact
width times the value of `v` at its left end times `B_0^2 + B_1^2 + C_0^2` for `eps~`, and times
`(B_0 + B_1)^2 + (B_1 + B_2)^2 + (C_0 + C_1)^2` for `eps~ - partial_t eps~`. Beyond `tau = 17` the end-region bounds
above are added. The squared exterior norms are at most 0.00000320066173968513189015735 for `eps~` and
0.0000192408718059828130775364 for `eps~ - partial_t eps~` (the exterior norms themselves are below 0.001789039335 and
0.004386441817); with the middle and inner squares of the previous paragraph, `||eps~||_X < 8.38010956871949018314234`
and `||eps~ - partial_t eps~||_X < 2467.95347982509225629694` on the whole plane (the square of each displayed bound
exceeds the exact sum of the displayed regional squares). With this exterior term and the first inner term, the inner
disc term dominated for `eps~` and the middle annulus term for `eps~ - partial_t eps~`. These bounds are still in the
diagnostic norm X only, remain larger than the conditional ones above and verify none of the saved majorants.

Sharper inner term (verified; own proof; timeline 10-22 11:31). On the inner disc `r <= exp(b_-)`, with
`tau = log r - b_-`, the density is `r^3` times a finite sine series whose radial coefficients are exact finite sums
of exponentials times polynomials. With `eta = rho~ - x^2 y`, the residual is `(partial_tau/k - 1) eta` plus the
action of the exact central strain velocity on `eta` plus the products of the remaining velocity `U^rem` (defined
above) with the derivatives of the full density; the cubic `x^2 y` drops out of the linear terms exactly, since its
transport by `c_l X` and the central strain velocity, minus itself, is `(3/k - c[rho~] - 1) x^2 y = 0`, and it is
removed algebraically before any interval operation. The velocity modes solve linear Green ODEs in tau forced by the
density; on each cell their Taylor polynomials are generated by these ODEs from their values at the cell midpoint,
fixed by the convergent canonical Green integrals (with the strain subtracted through a direct integral for the first
mode), with errors of orders `p <= 2` from the exact defect equation, so that no inequality is differentiated; an
independent construction uses a second pair of Green ODEs with different rates, forced by the density modes
themselves, and is compared on every coefficient. On each of 44 cells covering `-5 <= tau <= 0`, with exact rational
endpoints, the residual polynomial is formed before any absolute value, by interval convolution and independently by
exact integer centre-radius convolution, compared on every coefficient, and the Wiener bounds `B_p`, `C_p` and the
cell contributions are formed as for the exterior term. Below `tau = -5` the squares of the inner end-region norm
bounds above are added once. The squared inner-disc norms are at most 0.00000000000749763727216539889936543 for `eps~`
and 0.00000000565879455607782317925245 for `eps~ - partial_t eps~` (the inner-disc norms themselves are below
0.000002738182 and 0.000075224960); with the middle square of the first coarse bounds and the exterior square of the
previous paragraph, `||eps~||_X < 1.49546805188731021373656` and
`||eps~ - partial_t eps~||_X < 2464.68293019825564964515` on the whole plane (the square of each displayed bound
exceeds the exact sum of the displayed regional squares). Now the middle annulus term dominates for both. These bounds
are still in the diagnostic norm X only, remain larger than the conditional ones above and verify none of the saved
majorants.

As a sample check, at the 13 exact log-midpoints of the rigorous residual Wiener sums (timeline 10-20 16:09), and
using the canonical moment certificates inherited from that computation (verified separately, see below), two interval
calculations sharing those input boxes (no new canonical integration) enclose all 522 possibly nonzero odd sine
coefficients `eps~_N` of `D_t^i eps~`, `0 <= i <= 5`, and hence the pointwise Wiener sums
`V_ij = sum_N (2N + 1)^j |D_t^i eps~_N|`, `i + j <= 5`. For each of the 138 saved values `W_ij` available at the cells
containing these points, the upper end of the enclosure of `V_ij` is at most `W_ij` (the 135 higher-order fields are
absent from the saved certificate). The sample check alone establishes no derivative bound between the sampled radii.
On three closed middle-region cells (saved rows 4102, 4125 and 4211, whose radial endpoint pairs are approximately
`(8.5987, 8.6069)`, `(8.7897, 8.7981)` and `(9.9999, 10.0188)`; the first contains the radius of the source point P),
and using the same inherited canonical moment certificates, whole-cell upper bounds for
`sup_cell sum_N (2N + 1)^j |D_t^i eps~_N|`, `i + j <= 5` (63 bounds), are verified: Taylor coefficients through degree
64 of the analytically continued local residual of each cell are enclosed independently from the Green ODEs in ball
arithmetic and from the weighted density moment ODEs in interval arithmetic, both from the same inherited inputs, and
the remaining terms are bounded by Cauchy estimates on explicit complex discs in the local variable of each cell (for
the local continuations, not for the piecewise trial across knots). These first bounds all exceed the corresponding
saved majorants. A refinement of the same degree-64 polynomials gives smaller whole-cell upper bounds. Each cell is
split into eight equal closed subintervals in its local coordinate `z` (`t = t_c + h z`, `|z| <= 1`), fixed before the
range computations. On each subinterval, every derivative through order 5 of the polynomial formed from the midpoints
of the coefficient enclosures is bounded in absolute value by the largest modulus of its Bernstein coefficients. These
coefficients are computed by exact rational local affine composition and checked separately by a global Bernstein
conversion followed by three levels of midpoint subdivision in exact rational and in ball arithmetic; the two
calculations share the inherited coefficient enclosures and the proved power-to-Bernstein formula. The coefficient
uncertainty is bounded term by term using the radii of the exact intersections of the two enclosures. The angularly
weighted modal sums are formed on each subinterval, maximized over the eight subintervals and multiplied by `h^{-i}`,
and the same per-cell Cauchy tail bound is then added. All 63 refined bounds are at most the corresponding saved
majorants (exact rational comparison; the largest ratio is about 0.99), so on these three cells the 63 saved
derivative majorants for `i + j <= 5` are verified. These results were first verified conditional on the inherited
canonical moment certificates, which are not values of the shared archive; a second integration of the canonical
moment equations by a different method, from exact analytic anchors that include the complete inner and outer tails,
has since verified that all 6786 inherited moment intervals at the 13 points contain the canonical moments of the
exactly normalized trial and that all 27248 inherited local density coefficient intervals contain its exact
coefficients (timeline 10-22 00:23; section 8), so the sample check and the three-cell results hold for the trial
without that condition, with their other hypotheses unchanged. The saved maxima of A and B above occur at rows 4124
and 4123, respectively, which are not among these cells. This refinement does not verify A or B as physical derivative
bounds on any cell: the remaining hypotheses, including the lower bound for m, are not established. None of these
bounds is divided by m, and they give no bound outside these three cells, no location of a physical maximum and no
global forcing-norm bound. Complete zeroth-order certificates: the inner disc and the exterior (two interval methods
each) and the middle region (two complete interval methods with output audits, sharing the canonical density moment
archive). W denotes the modal Wiener sum of the trial's residual and `m = u^3 (1+u^2)^{(k-3)/2}`, `u = r/L`. The
trial's residual is not in unweighted `L^2(R^2)`: at infinity it is `r^{2k-1}` times a nonzero angular profile
(section 2), and it is not in `dot H^{-1}(R^2)` or `H^{-1}(R^2)` either, so no unweighted `L^2` or negative-norm
forcing bound exists for it; the normalized suprema below control the stated weighted supremum quantities and do not
provide an unweighted `L^2` forcing bound. The exactly normalized tail repairs `rho_T` of section 10, item 4, have
residuals in `L^2(R^2)` but not in `dot H^{-1}(R^2)` (section 4), and the higher repairs `rho'_T` there have residuals
of finite norm in the homogeneous space `dot H^{-1}(R^2)`; no upper bound for these norms is supplied, and as
`T -> infinity` they grow at least like `T^{2k}` (like `T^{2k+1}` in `dot H^{-1}(R^2)`; section 10, item 4). The
scaling source `X.grad rho'_T` of each higher repair has the leading term `k r^k Theta_M` of the trial and is not in
`dot H^{-1}(R^2)`, so a formulation in which the coefficient of `X.grad rho` varies cannot place the term
`delta c X.grad rho'_T` in that space.
- Verified selected-cell certificate: at 13 middle-region cells (radial cells numbered 0, 5, 100, 500, 1500, 2761,
  3925, 4102, 4125, 4211, 5622, 7038, 7808 of 7809), independently reconstructed density moments with degree-16
  interval Taylor models and an exact-rational Bernstein conversion give complete-cell bounds on W and `W/m`. Each is
  below the corresponding bound in the historical numerical output used for that comparison; the revised numerical
  output (rerun with repaired code on 10-20 from 22:54 to 23:38) is smaller at some cells, and its full arithmetic has
  not been independently accepted. At the cell containing the lobe near P (`r` about 8.79), `W/m < 2.91625e-4`. This
  is not a global norm.
- Verified inner certificate (two independent interval constructions, 384-bit Arb physical Green ODEs and 160-digit
  interval density-moment ODEs with exact integer convolution): on the whole inner disc `0 <= r <= R_i = e^{t_a}`
  (about 0.00765142460138; `t_a` is the first log knot of the trial), covered by 54 adjoining rational log-cells on
  `-7 <= log(r/R_i) <= 0` and an analytic fifth-order bound `W <= B_5 r^5` below: `sup W < 7.521952952e-15`,
  `sup W/m < 9.3284616604e-6`, `sup (1+u)^{1/2} W/m < 9.3328095471e-6`, `sup (1+u)^{1/2-k} W/m < 9.3312496355e-6`, and
  `N_in < 3.9690558060e-8`, where `N_in^2 = int_{r <= R_i} |eps~/m|^2 dX/(1 + (r/L)^2)`. The value at 0 is the proved
  limiting bound. Zeroth order; this certificate gives no derivative norm (the X norm on the smaller disc
  `r <= e^{t_a - 5}` is bounded above from the exact inner expansion and the velocity remainder bounds of the earlier
  analytic majorant below, and the direct bound above covers the whole disc). (The earlier coarse analytic majorant
  `W/m < 0.046607` on the same disc, a bound `W <= B_5 r^5` that does not exploit the small size of the fifth-order
  residual, is superseded as a residual bound; its velocity remainder bounds are used for the derivative norms above.)
- Verified exterior certificate (two independent interval constructions, 384-bit Arb and 160-decimal-digit interval
  arithmetic with exact integer convolution): on the whole exterior `r >= R_e = e^{t_b}` (about 3412.966858; `t_b` is
  the last log knot of the trial), covered by 89 adjoining rational log-cells on `0 <= log(r/R_e) <= 17` and an
  analytic tail: `sup W < 4.2805798591e-4`, `sup W/m < 9.495673840e-5`, `sup (1+u)^{1/2} W/m < 7.73796325669e-3`,
  `sup (1+u)^{1/2-k} W/m < 1.51008157506e-3`, and `N_ext < 1.83055041641e-3`, where
  `N_ext^2 = int_{r >= R_e} |eps~/m|^2 dX/(1 + (r/L)^2)`. The leading far coefficient (at `e^{(2k-1) tau}`,
  `tau = log(r/R_e)`) is computed exactly before absolute values are taken; on `tau >= 9`: `W < 2.04506e-5`,
  `W/m < 1.362864e-6`; on `tau >= 17`: `W < 6.6848357e-8`, `W/m < 1.060902e-9`. This is a zeroth-order bound; it gives
  no derivative norm (the X norm on `r >= e^{t_b + 17}` is bounded above from the exact expansion and the coefficient
  bounds of the earlier coarse majorant below, and the direct bound above covers the whole exterior). (An earlier
  coarse majorant, `W/m < 5740483`, which cancels the leading linear term exactly but discards the cancellations
  between the linear and nonlinear terms and between particular and transient Green terms, is superseded as a residual
  bound; its exact expansion and coefficient bounds are used for the derivative norms above.)
- Middle region, full pass (verified by two methods; both use the shared canonical density moment archive, which is
  verified together with its composition with these bounds, as described below; primary assembly: the verifier's own
  computation from its own reconstruction of the exact canonical density moments, which is independent of the
  numerical team's code, followed by an audit of every saved output and exact final comparisons; the audit does not
  regenerate the per-cell Taylor coefficients, which are not saved; the second method is described below): on the
  whole middle annulus `R_i <= r <= R_e`, covered by 7809 adjoining exact rational log-cells, a computation from the
  exact canonical density moments (384-bit Arb, degree-16 Taylor models, Bernstein enclosures and residual tails),
  followed by a separate exact coverage audit and a 150-digit interval audit of every reported scalar, gives
  `sup W < 1.34943e-4`, `sup W/m < 2.91625e-4`, `sup (1+u)^{1/2} W/m < 4.27591e-4`,
  `sup (1+u)^{1/2-k} W/m < 3.72741e-4` (for each of these four quantities the largest cell upper bound occurs in the
  cell containing the lobe near P, `r` about 8.79), and `N_mid < 5.23709e-4`,
  `N_mid^2 = int_{R_i <= r <= R_e} |eps~/m|^2 dX/(1 + (r/L)^2)`. Every cell bound is below the corresponding bound in
  the historical numerical output used for that comparison. A second method has been completed on all 7809 cells: it
  reconstructs the cell residual models from the density moment ODEs (a different intermediate representation from the
  physical Green ODEs of the first method) in 160-digit interval arithmetic with exact integer convolutions and
  Bernstein bounds, checks in every cell that all 8874 retained Taylor coefficient enclosures (522 modes, degrees 0 to
  16) overlap those of the first method's regenerated models, compares its cell bounds with the independent point
  enclosures at 13 preselected cells, and is followed by its own output audit and a complete scalar scan at 220
  digits. The coefficient overlaps are checks recorded by the reviewed producer; the scalar scan checks saved outputs,
  scalar inequalities and recorded comparison counts and does not regenerate the Taylor coefficients; coefficient
  overlap is a consistency check and does not replace the enclosure and remainder arguments. The published middle
  values strictly exceed the corresponding accepted joint bounds. The joint strict ceilings are `1.34942914e-4`,
  `2.91624061e-4`, `4.27590787e-4` and `3.72740952e-4` for the four supremum quantities in the order stated above, and
  `5.23708529e-4` for `N_mid`. The four supremum bounds use the maxima of the corresponding bounds from the two
  methods; the norm bound is the square root of the exact sum of the joint cell squared upper bounds. The largest
  joint cell upper bound for each of the four supremum quantities occurs in the lobe cell; this does not locate an
  actual maximum of the residual or of a weighted residual quantity. Both methods use the same accepted canonical
  density moment archive. Agreement between the two cell methods does not independently validate that archive. The
  independently certified point enclosures provide consistency checks of the cell bounds at the centres of 13
  preselected cells only. This archive is verified separately: all 3265568 density polynomial coefficients on the 1558
  knot spans and all 813276 prescribed boundary moments of the exactly normalized trial lie in their unchanged
  archived intervals, and an explicit dependency composition (verified) identifies the archived inputs, exact trial,
  normalization and moment conventions used by both middle-region methods, by the inner and exterior certificates
  (through the archived boundary moments of the first and the last knot span) and by the whole-plane joinings below
  with exactly these intervals (section 8). Hence the middle-region bounds above, the inner and exterior bounds and
  the whole-plane bounds below hold for the trial without the archive condition, with unchanged values and under their
  other stated hypotheses. (The earlier numerical computation reported `2.926e-4` as a proposed upper bound for
  `sup W/m` on the middle region (floating-point diagnostic). It is not used because its coefficient export did not
  enclose the exact dependent coefficients. Its repaired rerun, completed on 10-20 from 22:54 to 23:38, reports
  smaller values but is not used either, since its full arithmetic has not been independently accepted. At the lobe
  cell, the revised and historical numerical outputs are approximately `2.5964e-4` and `2.9260e-4`, respectively
  (floating-point diagnostics). Exact comparison of the saved numbers places the verified bound `2.91625e-4` strictly
  between those outputs.)
- Whole-plane zeroth-order consequence (inner, middle and exterior items together; the middle inputs used strictly
  exceed the accepted joint bounds of the two middle methods; the archive condition is discharged as stated in the
  middle item): `sup |eps~| <= sup W < 4.2805798591e-4` (the exterior bound), `sup W/m < 2.91625e-4`,
  `sup (1+u)^{1/2} W/m < 7.73796325669e-3`, `sup (1+u)^{1/2-k} W/m < 1.51008157506e-3`, and
  `N_0 = (N_in^2 + N_mid^2 + N_ext^2)^{1/2} < 1.904e-3` (exact rational check). The joining of the three regions
  (their exact common endpoint knots, the complete tails at the origin and at infinity, the region-wise maxima and the
  exact sum of the squared norms, with separate interval checks of the middle weight factors and integrals and of the
  final square root) is independently verified for these inputs. A second joining from the joint middle cell bounds of
  the two middle methods, with the same inner and exterior inputs, was also independently verified; it gives
  `N_0 < 1.903991978e-3`, and the largest regional bound is the exterior one for W and for the two weighted quantities
  and the middle one for `W/m` (bounds on majorants; this does not locate a maximum of the residual); `eps~/m` extends
  continuously by 0 to the origin by the fifth-order bound of the inner item, and eps~ and the three normalized
  weighted residuals tend to 0 at infinity. These are residual sizes in zeroth-order norms only. The correction norms
  proposed in this report contain derivatives (sections 7 and 10), and no inverse bound connecting these zeroth-order
  norms to such a norm is available, so they do not by themselves bound the distance to a solution.

Fit stability (per-cell bounds reported by the numerical team from its own outward-rounded certificate pipeline; not
used anywhere in this report): the same pipeline applied to three refitted variants of the trial (radial knot spacing
halved; 230 instead of 260 angular modes; last knot at about 1468 instead of 3413) gives middle-region supremum bounds
within 0.03 percent of its bounds for the trial itself (for `W/m` about `2.5964e-4` for the trial and at most about
`2.5970e-4`, for the variant with 230 modes, in the lobe next to P) and outer-region supremum bounds within 0.5
percent; the integral bounds of these two regions change by at most about 4.74 percent (for the variant with the
shorter knot range, whose middle region is shorter), and the much smaller inner-region bounds drop by about 41 percent
(supremum) and 80 percent (integral) under the halved knot spacing. The verifier recomputed these regional bounds from
all 78091 saved cell rows of the four trials (maxima of the row bounds, with the monotone radial weights enclosed at
the outer cell endpoints, and exact sums of the row integral bounds) and the exact relative changes of the published
aggregate bounds, in two implementations with different arithmetic libraries; this audit is conditional on the saved
per-cell bounds, on the coverage of each region by its cells and on the reconstruction of the variants, none of which
is audited (files presented by the numerical team as the output of a rerun of its fitting program from the published
data of X3 agree byte for byte with the four stored trial files, the base trial and its three variants, as checked by
the verifier; the verifier did not rerun the fitting, attest which process wrote these files, or verify byte equality
for the unavailable files of an earlier rerun). The changes are changes of upper bounds: two upper bounds `b` and `v`
are satisfied by equal actual values `min(b, v)/2`, and also by actual values `b/2` and 0, so they do not establish a
percentage change of the actual residual norms. These comparisons concern the finite cell regions, whose radial ranges
differ between the trials (the ranges displayed by the numerical team are rounded labels: 15 of their 24 endpoints lie
inside the nominal cell range); the separately bounded tails are not included (the reported outer-tail bounds of the
variant with the shorter knot range are up to about twice those of the trial). The variants are different trials.
These comparisons do not establish stability or convergence of the actual residual norms.

Floating-point reproduction of X3's published sampled maxima:
- Sampling: sampled on between-node grids; these are not bounds. For X3 the residual and both denominators below
  vanish on `y = 0` by odd-y symmetry and on `x = 0` by its `x^2` factorization. The independent evaluator sets the
  axis columns to their exact zero residual, which for the normalized columns amounts to excluding the axis samples
  from the maxima. The published normalized maxima in the regions `r <= 1000` also exclude, where so stated in the
  published report, the evaluation columns next to the y-axis (`pi/2 - theta < 0.006`); the published absolute maxima
  use all evaluation columns.
- Speed: X3 with its published held speed `c_l = 5.575362610641546` (not the centre-normalized speed, for which
  the far residual is unbounded, section 4, and not the exactified trial).
- Normalized error: with `eps = (c_l X + U).grad rho - rho`, `V = c_l X + U`, the columns N_f and N_v show
  `|eps|/N_f` and `|eps|/N_v`, where `N_f = |V_1 rho_x| + |V_2 rho_y| + |rho|` and
  `N_v = |rho| + |X.grad rho| + |U.grad rho|` (the denominators of the problem statement).
- Resolutions: three, namely the published evaluator rerun at 11250 x 384 (bit-identical) and an independent evaluator
  at 16875 x 512 and 22500 x 768 (log-radial grid on `1e-4 L <= r <= 1e6 L`; beyond it the inverse continues the
  angular modes of `rho_x` by fitted power laws).
- Published column: the published absolute maxima on the published 16875 x 512 and 22500 x 512 grids (one value where
  the two agree); in the row `1000 <= r <= 1000 L` the published N_v maxima on 11250 x 384 and 16875 x 512; in the
  last row the published absolute maxima over `1000 <= r <= 1e6 L`, attained beyond `1000 L`.

| region | N_f 16875 / 22500 | N_v 16875 / 22500 | abs 16875 / 22500 | published |
|---|---|---|---|---|
| r <= 0.1 | 2.6e-10 / 2.6e-10 | 5.6e-10 / 5.7e-10 | 3.8e-12 / 3.8e-12 | abs 1.71e-13 / 1.65e-13 |
| 0.1 <= r <= 2 | 2.3e-8 / 2.6e-8 | 4.5e-8 / 5.1e-8 | 1.05e-7 / 1.07e-7 | abs 8.92e-8 / 8.91e-8 |
| 2 <= r <= 10 | 6.80e-7 / 7.16e-7 | 1.90e-7 / 2.01e-7 | 6.96e-5 / 5.61e-5 | abs 6.03e-5 / 5.82e-5 |
| X near P (< 0.5) | 6.80e-7 / 7.16e-7 | 1.90e-7 / 2.01e-7 | 1.045e-5 / 1.12e-5 | abs 1.05e-5 / 1.05e-5 |
| 10 <= r <= 100 | 8.9e-8 / 8.9e-8 | 7.1e-8 / 6.8e-8 | 1.98e-5 / 2.02e-5 | abs 1.99e-5 / 1.98e-5 |
| 100 <= r <= 1000 | 1.59e-8 / 1.59e-8 | 6.5e-8 / 6.5e-8 | 6.26e-6 / 6.28e-6 | abs 6.03e-6 / 6.04e-6 |
| 1000 <= r <= 1000 L | 1.36e-8 / 1.37e-8 | 2.21e-7 / 2.19e-7 | 3.09e-5 / 3.15e-5 | N_v 2.15e-7 / 2.18e-7 |
| r > 1000 L | 1.31e-7 / 1.32e-7 | 1.091e-6 / 1.095e-6 | 1.881e-4 / 1.893e-4 | abs 1.897e-4 / 1.897e-4 |

The largest sampled absolute residual on the two saved grids occurs in the far field, at `r` about `4e4`, or about
`5.2e3 L`. This is a maximum over sampled points, not a global maximum.

The following table gives the locations of all sampled maxima in the saved outputs of the independent evaluator
(floating, not reproduced). Each entry lists `(r, theta)` for 16875 x 512 / 22500 x 768; theta is measured in radians
from the x-axis. The columns N_f, N_v and abs refer respectively to `|eps|/N_f`, `|eps|/N_v` and `|eps|`. The source
of X3 is `(x_*, 0)`, `x_*` about 8.6000638, and the source disc is `|X - (x_*, 0)| < 0.5`. Region labels refer only to
points included in the sampled grids.

| region | N_f | N_v | abs |
|---|---|---|---|
| r <= 0.1 | (0.09987, 0.0031) / (0.09996, 0.0020) | (0.09987, 0.0031) / (0.09996, 0.0020) | (0.09987, 0.6228) / (0.09996, 0.6218) |
| 0.1 <= r <= 2 | (1.999, 0.0031) / (1.999, 0.0020) | (1.999, 0.0031) / (1.999, 0.0020) | (1.999, 0.2700) / (1.999, 0.2536) |
| 2 <= r <= 10 | (8.527, 0.0092) / (8.523, 0.0082) | (8.527, 0.0092) / (8.523, 0.0082) | (8.811, 0.2884) / (8.807, 0.2904) |
| source disc | (8.527, 0.0092) / (8.523, 0.0082) | (8.527, 0.0092) / (8.523, 0.0082) | (8.539, 0.0491) / (8.532, 0.0573) |
| 10 <= r <= 100 | (10.00, 1.5677) / (10.01, 1.5688) | (73.15, 1.5616) / (87.99, 1.5626) | (13.94, 0.9235) / (13.94, 0.9224) |
| 100 <= r <= 1000 | (100.1, 1.5524) / (100.1, 1.5524) | (100.1, 1.5524) / (100.1, 1.5524) | (646.6, 1.3683) / (646.7, 1.3683) |
| 1000 <= r <= 1000 L | (7643, 1.5094) / (7649, 1.5094) | (7643, 1.5555) / (7649, 1.5565) | (7643, 1.4634) / (7649, 1.4624) |
| r > 1000 L | (3.273e4, 0.8468) / (3.272e4, 0.8447) | (3.656e4, 1.5677) / (3.639e4, 1.5688) | (4.012e4, 0.6596) / (4.006e4, 0.6422) |

The normalized maxima in the source disc are three and four angular grid steps from the x-axis. The far-field N_v
maxima are one angular grid step from the y-axis. Residuals on both axes are set to their exact zero. The absolute
maxima in `2 <= r <= 10` occur at the lobe, outside the source disc. Several other maxima occur within one radial grid
step of a region boundary; their locations alone do not establish the behaviour between samples or across those
boundaries.

We also performed floating tests of the outer extent, the radial sampling and the far continuation, with the numerical
team's evaluator and the held speed `c_l` fixed. The evaluator's inverse was last modified after the original saved
runs, and its driver was modified after our tests to add far-continuation options, so the precise source used for each
output is not independently attested. On the 16875 x 512 grid the 24 recorded maxima of our reference run differ from
the original saved values by at most 2.23 percent, with identical recorded maximizing coordinates; the cause of this
difference is unknown. All relative changes below use our reference run as the baseline. Beyond the grid the evaluator
continues the angular modes of `rho_x`, the source of its modal inverse, by a least-squares fit over the last radial
decade, with the fitted powers `k - 1`, `2k - 2`, `3k - 3` and `k - 3`. The tests gave the following results.
- Outer extent: extending the outer endpoint from `1e6 L` to `1e11 L` with the same nominal logarithmic step gives a
  largest relative change of `1.18e-9` among the 24 maxima. With endpoints `1e5 L` and `1e7 L` and 15188 and 18562
  radial points respectively, whose nominal steps differ from the reference step, the changes are at most 0.7 percent,
  except for the absolute maximum in `2 <= r <= 10`, which is 7.88 percent lower at `1e7 L`. These latter comparisons
  change both the outer extent and the radial sampling.
- Sampling: shifting the reference radial grid by half a step changes the maxima by at most 1.5 percent. The absolute
  maximum in `2 <= r <= 10` is `6.960e-5` on the reference grid, `6.984e-5` on the shifted grid, `6.948e-5` and
  `6.411e-5` on the `1e5 L` and `1e7 L` grids, and `5.611e-5` in the saved 22500 x 768 output (`6.959e-5` in the saved
  16875 x 512 output, a decrease of about 19.4 percent). These results do not establish a converged value for that
  maximum.
- Fit window: changing the fitting window from one decade to half a decade or two decades gives a largest relative
  change of `2.47e-6` among the maxima.
- Fitted powers: retaining only the leading fitted power `k - 1` changes the maxima by at most 0.5 percent in the
  source-disc and `2 <= r <= 10` rows and by at most 1.3 percent in `r > 1000 L`. In the other rows with `r >= 0.1`
  the relative changes range from 0.478 percent to 14 percent. In `r <= 0.1` they reach 44.8 percent; the reference
  maxima in that row are below `1e-9`.
- Zero continuation: setting the exterior `rho_x` source modes of the modal inverse to zero beyond the grid increases
  every sampled maximum by a factor between approximately 21.4 and 2892 and changes all maximizing locations. All
  three maxima in the far-field row then occur at the outer grid endpoint, `r = 1e6 L`.
- Repetition: the numerical team repeated our reference, leading-power-only and two-decade-window runs with the
  evaluator after its later modification, obtaining the same 24 recorded maximum values in each case. These
  repetitions use the same implementation and provide no check by an independent one. All comparisons here use the
  three columns of the report table. On grids with the reference inner endpoint and approximately the reference
  logarithmic spacing, ending near `1e5 L` and `1e7 L`, the magnitudes of the relative changes are at most 0.55 and
  0.011 percent respectively. The largest changes occur in `r <= 0.1`; over the listed regions contained in `r >= 2`
  they are at most `6.3e-5` and `1.1e-6` relative. With 16875 radial points on each range ending at `1e5 L` and
  `1e7 L`, the absolute maximum in `2 <= r <= 10` decreases by approximately 11.2 percent to `6.18e-5` and increases
  by approximately 3.6 percent to `7.21e-5` respectively. For each of the other 23 maxima the magnitude of the
  relative change is at most 0.93 percent. These 16875-point grids differ from the endpoint grids used in the Outer
  extent and Sampling bullets.

For the exact formula of X3 the verifier proved that `k - 1`, `2k - 2`, `3k - 3` and `k - 3` are the first four
allowed far powers of `rho_x`, in decreasing order, with a remainder of order `r^{4k-4}` uniformly in the angle; each
sine coefficient inherits this expansion. Individual coefficients may vanish, and the remainder constant has not been
evaluated. The fitted coefficients need not equal the asymptotic ones. In the verifier's floating comparison at the
reference endpoint, using floating evaluations of the analytic coefficient formulas, the four fitted coefficients of
the first sine mode have signed relative discrepancies `(A_fit - A_asym)/A_asym` of approximately `4.27e-12`,
`-1.89e-7`, `0.161` and `-0.337`. With the outer endpoint at `1e11 L` the last two discrepancies are approximately
-393 and 33800, although the sampled relative fit residual of that mode is approximately `1e-14`.

For exterior sources that agree inside R, the verifier proved that changing the first sine coefficient of `rho_x`
beyond R by `sum_j dA_j (r/R)^{q_j}`, with all `q_j < 0`, changes the canonical central strain by
`dc = (1/2) sum_j dA_j/(-q_j)`. Interpreting the amplitudes and exponents recorded in the verifier's fit diagnostic as
exact binary64 numbers, the resulting synthetic strain changes at the reference endpoint, relative to the reference
fit, are as follows; the last column gives the change of the central strain recorded by the evaluator in the
corresponding run of the tests above.

| exterior source variant | synthetic strain change (exact arithmetic on the verifier's fits, rounded) | change of the evaluator's recorded strain |
|---|---|---|
| half-decade window | `-5.2e-17` | 0 |
| two-decade window | `1.2e-14` | 0 |
| leading power only | `4.5e-9` | `4.5e-9` |
| zero continuation | `-2.9e-5` | `-2.9e-5` |

These exact computations concern the recorded synthetic sources. They do not enclose the true exterior source of X3 or
certify the changes of the evaluator's full computed strain.

Our own comparison of the recorded central strains with the verified enclosure
`[15.72608782162331, 15.72608782162370]` of the central strain of X3 (section 3) gives the following discrepancies.
The value `15.726087821661109` of our reference run lies approximately `3.74e-11` above the upper endpoint. The values
of the two original saved runs lie approximately `4.85e-8` and `4.87e-8` below the lower endpoint. This comparison
does not identify the causes of the discrepancies.

These tests measure changes in recorded sampled maxima for the listed configurations. They show sensitivity to the
choice of far continuation, but they do not validate the fitted continuation or establish independence from the outer
extent or fitting window. They provide no rigorous residual bounds, and no numerical convergence is claimed. The
verifier did not rerun the evaluator or independently recompute its sampled maxima. Using exact arithmetic on the
saved binary64 values, it checked the decimal roundings of the 48 recorded maximum triples (a value and its two
coordinates) in our summary of the two saved runs; we separately checked that the 16875 x 512 and 22500 x 768 entries
of the two tables above are correct roundings of the saved values and coordinates. It also checked the relative
changes and multipliers in our summary of the tests underlying the first five bullets, the comparison of our reference
run with the original saved values (at most 2.23 percent), and that the recorded far-field maxima of the zero
continuation lie at the recorded outer endpoint. These checks establish the transcription and arithmetic consistency
of saved records only. The Repetition bullet was outside the verifier's audit. In earlier verified computations
(above), the verifier computed rigorous residual Wiener sums for the exactified trial at 13 selected points and
complete-cell bounds at 13 cells, consistent with the historical numerical values; these are different quantities from
those in the tables.

## 7. A posteriori theorem / exclusion
No decisive endpoint has been established. The theorem that would be applied for a YES is the following
conditional two-norm iteration theorem (verified as an abstract statement); a limited exclusion centred at the
trial is stated after it.

Setting and hypotheses:
- Spaces: Banach spaces X and E of corrections with a continuous injective embedding of X into E (parity and
  normalization constraints built in); the ball `B_r = {h in X : ||h||_X <= r}` is closed in E. Banach forcing spaces
  `Y_H` and `Y_L`, continuously embedded in a common space Z of distributions, with `Y_H` embedded in `Y_L`; the
  residual `eps~ = F(rho~)` lies in `Y_H` with `||eps~||_{Y_H} <= eta`; a velocity space V.
- Operators: `Gamma h = W[h]`, `A_h u = L u + (Gamma h).grad u` and `B(e, u) = (Gamma e).grad u`. For each h in
  `B_r`, `A_h` acts on a linear low domain `D_h` in E containing X, with values in Z, and maps X into `Y_L`.
- Low a priori estimate: `||u||_E <= K_L ||A_h u||_{Y_L}` for every u in `D_h` with `A_h u` in `Y_L`.
- High solvability: for every f in `Y_H` there is `R_h f` in X with `A_h R_h f = f` and
  `||R_h f||_X <= K_H ||f||_{Y_H}`.
- Bilinear structure: for all h, g in `B_r` and u in X, `(A_h - A_g) u = B(h - g, u)` in Z and
  `||B(h - g, u)||_{Y_L} <= C_B ||h - g||_E ||u||_X`.
- Velocity bound: `||Gamma h||_V <= C_V ||h||_X`, with `C_V r <= r_V` if the operator hypotheses hold only for
  velocity increments bounded by `r_V`. All constants are uniform over `B_r`.

Closing conditions: `K_H eta <= r`, `K_L C_B K_H eta < 1` and `C_V r <= r_V`.

Conclusion: a unique h in `B_r` with `A_h h = -eps~`, that is `F(rho~ + h) = 0` (since
`F(rho~ + h) = eps~ + L h + W[h].grad h`), and `||h||_X <= K_H eta`.

Scope: the theorem concerns additive corrections `rho~ + h` in a fixed space. In the formulation of section 10 the
tail exponent and the amplitude tau are further unknowns. A finite exponent change is not an additive correction of
that kind (`r^{k + kappa} - r^k = r^k (e^{kappa log r} - 1)`), and the augmented nonlinear map, its domains, its
forcing spaces and its uniform difference estimates have not been constructed; the theorem does not apply to that
formulation until they are.

Jet-continuity exclusion centred at the trial (verified, with its own proof and interval constants; first derived in a
referee review). At the trial's source P one has `d_y F(rho~)(P) = (mu~ - 1) g`, of absolute value above `6.70197e-7`,
with `g = rho~_y(P)`, `g' = rho~_xy(P)` and `mu~ = d_y V~_2(P)` for the trial (section 4). For `rho = rho~ + h` of
class `C^2` near P with V, `W[h]` of class `C^1` there and h with the parity of section 2 (even in x, odd in y), which
is preserved by F, one has `d_y F(rho)(P) = (mu~ - 1) g + (mu~ - 1) z + g w + g' u + w z + u v` with `z = h_y(P)`,
`v = h_xy(P)`, `u = W[h]_1(P)`, `w = d_y W[h]_2(P)`. Hence `|d_y F(rho)(P) - d_y F(rho~)(P)| <= C delta + 2 delta^2`
whenever `max(|z|, |v|, |u|, |w|) <= delta`, with `C = |mu~ - 1| + |g| + |g'|`, `30.0229 < C < 30.0230`. At
`delta = 2.2e-8` the lower bound `|d_y F(rho~)(P)| - C delta - 2 delta^2` exceeds `9.69e-9`, so no exact solution
satisfying these hypotheses has `max(|z|, |v|, |u|, |w|) <= 2.2e-8`. The point P is the trial's source; the statement
does not follow the source of a perturbed profile. This is a quantitative exclusion in the neighbourhood of the
normalized trial defined by these four point values. No certified comparison places X3, or a specified uncertainty
neighbourhood of X3, inside it (no certified bound on all four jets at P of the difference between X3 and the trial is
available); consequently it does not establish the requested X3 NO endpoint. A floating comparison (not certified: the
four quantities of the difference between X3 and the trial, from a grid modal inverse of that difference at two
resolutions, which agrees to five digits with the certified enclosure of `c` of the difference) gives `|u|` about
`1.6e-8`, `|z|` about `5.6e-9`, `|w|` about `1.3e-9` and `|v|` below `4e-10`, so X3 plausibly lies inside the
neighbourhood; if these values were certified, the triangle inequality would guarantee only a set (not necessarily the
largest) of radius about `2.2e-8 - 1.6e-8 = 6e-9` about X3 (in the maximum of the absolute values of the four
quantities) inside the excluded set. Verified scalar arithmetic (exact rectangle arithmetic in two interval engines,
reproduced; its input, the enclosure of the central strain of X3 of section 3, comes from one rigorous summation of
the whole integral and has not been reproduced by a second independent one): with `u = U_1[h](P) + p c[h]/3` for the
difference h (raw c, P = (p, 0)), the strain part satisfies `-2.95309e-8 < p c[h]/3 < -2.95294e-8`, larger in modulus
than the radius; `U_1[h](P)` is not certified (floating value about `4.5e-8`), so neither membership nor
non-membership of X3 follows. Disclosure as required by the problem statement: no numerical-uncertainty ball around X3
is specified and proved to lie inside this set. The residual bounds of section 6 do not determine a perturbation
radius in these four quantities: they are upper bounds for a different quantity in a different norm, and no stability
estimate connects them. The set constrains only four point values and nothing in other directions. In our judgement
(not a proved statement; no numerical-uncertainty set for X3 is specified against which it could be checked) a set of
this kind, of radius `2.2e-8` and with a floating X3-centred margin of about `6e-9`, is too small to contain a
meaningful numerical-uncertainty ball, and the exclusion is not presented as a decisive result. For context only
(different quantities, and none of them an enclosure): the problem statement reports competitive fits over the
exponent span `[5.5524653, 5.5793640]`, of width about `2.7e-2`, and a discrepancy of about `3.2e-9` between the held
exponent of X3 and the value `(1 + psi_xy(0))/3` of its own canonical inverse.

Moving-source form (verified; 5(o)). Stationarity at the source of the perturbed profile forces `d_y V_2 = 1` there,
so no exact solution `rho~ + h` (classical and of class `C^1` near its source, with `eps_0 < m R_I`, so that a source
exists in I, with `g_h != 0`, for example from `eps_3 <= 29` and the certified value of g, and with the other
hypotheses stated in 5(o)) has both axis velocity increments `sup_I |W[h]_1|` and `sup_I |d_y W[h]_2|` at most
`2.1886e-8` on `I = [p - R_I, p + R_I]`. This form follows the moved source and needs no small density-jet increments
and no second density derivative, but it is just as narrow: the floating value of `W[h]_1(P)` for the difference
between X3 and the trial (about `1.6e-8`) is already of that order (a point value; the suprema are not computed), and
the same disclosure applies; it is not presented as a decisive result. In the whole-plane norm (verified; 5(o),
"Whole-plane Sobolev ball") the same argument excludes exact solutions `rho~ + h` with h in `H^{153/50}(R^2)`, even in
x and odd in y, and `||h||_{H^{153/50}} <= 3.2318e-7`. This is a statement about the trial: `X3 - rho~` lies in no
`H^s(R^2)` with `s >= 0` (section 2, far tail), so the excluded set neither contains X3 nor contains a neighbourhood
of X3.

Affine `L^2` class (verified; section 3, entry 05:37). No exact stationary profile `rho~ + h` exists with h in
`L^2(R^2)`, for any real value of the coefficient of `X.grad rho` in the equation (in particular for the
centre-normalized `c_l[rho]` and for any held exponent), among profiles that are locally regular enough for the
products of the equation to be defined, have the parities of section 2 and a canonical velocity with
`||U||_{L^2(B_S)} = o(S^2)` (every `P_2` profile satisfies these hypotheses); in particular there is none with h in
any (inhomogeneous) `H^s(R^2)`, `s >= 0`. Proof outline: the canonical velocity of an `L^2` difference is its `L^2`
Fourier multiplier (a Liouville argument excludes a harmonic strain); testing the difference of the two equations
against `S^{-1} phi(X/S)`, phi supported in `1 < |Y| < 2`, makes every term containing h tend to zero as
`S -> infinity`; the `r^k` term then forces that coefficient to be `1/k`, and the nonzero coefficient `Eps_1` of the
far residual (section 2) gives a pairing of order `S^{2k}`, a contradiction. No pointwise expansion of h is used. It
excludes every `L^2` ball about the trial within the stated class, but it is a statement about the trial: X3 is not in
`rho~ + L^2(R^2)` (section 2), and the class contains no neighbourhood of the trial in the factor norm of the axis
control (section 4), since the exactly normalized repairs `rho_T` of section 10, item 4, lie outside it at factor
distance below `0.334616 T^{k-1}` for every `T >= max(R_b, L, 1)` (these repairs are kinematically admissible and are
not claimed to be stationary). Consequently the affine `L^2` obstruction establishes no exclusion neighbourhood of X3
and does not resolve the requested neighbourhood question.

The global hypotheses needed to apply the two-norm theorem to IPM remain unproved: a common realization of the high
and low spaces, uniform inverse and bilinear bounds (`K_H`, `K_L`, `C_B`, `C_V`), and a residual bound `eta` in its
forcing space. (The local statements of section 5 and the auxiliary inverse bounds of 5(o) are established at their
stated scope.)

## 8. Independent-verifier notes
Independently rederived or recomputed by the verifier:
- the X3 file identity and reconstruction;
- the canonical Green identity and the central strain (interval quadrature with remainders, and an exact rational
  audit of the polynomial coefficients and quadrature nodes);
- the normalization identity under continuous factorization;
- the source identities and the axis-control constants;
- the exact repair of X3 and the exactification of the modal trial (two interval methods);
- the trial's source scalars, by a method different from the numerical team's (all 261 stream modes, density moments,
  exact sign bisection);
- the exported Green boundary values `A_n`, `B_n` of the trial's canonical inverse at all 7810 exact boundaries of the
  7809 middle cells, for all 261 modes, contain the canonical values: two interval methods with different propagation
  identities and libraries enclose these values from the shared canonical density moment archive (4076820 containment
  comparisons per method), so the containment holds conditional on that archive enclosing the canonical inputs, a
  condition discharged by the verified archive and its verified composition with this result (below). This is not a
  second integration of the canonical moments;
- the density polynomial boxes of the flow certificate (5(l)): on all 7809 middle cells, each of the 16242720 exported
  boxes for the Taylor coefficients in `t = log r` at the exact cell left end (eight powers, 260 modes) of the trial's
  modal spline amplitudes contains the exact coefficient, by exact rational B-spline evaluation and interpolation and,
  separately, by an outward interval reconstruction from the shared canonical density moment archive through an exact
  angular inversion; and the density polynomial balls of that archive on all 1558 knot spans contain the exact
  polynomials of the trial (3265568 coefficients, exact rational). A separate audit recomputed preselected and extreme
  entries, and four complete spans were replayed. The moment values of the archive (verified separately, next item),
  the radial models and the flow inequalities are not covered by this check;
- the shared canonical density moment archive, by a second complete propagation method different from the original
  one: on all 1558 knot spans, all 3265568 density polynomial coefficients and all 813276 boundary moments lie in
  their unchanged archived intervals, for the exactly normalized trial, with exact analytic formulas for the complete
  inner and outer tail integrals (including the normalization correction) and a separate exact audit of every saved
  output and analytic anchor. This validates the archive itself; its compositions with the source results of 5(o) and
  with the zeroth-order residual certificates of section 6 (next two items) and with the Green boundary values and the
  three-cell radial models of 5(l) (below) are verified;
- the composition of this archive verification with the source results of 5(o): the seven archive span records copied
  into the source derivative calculations equal the corresponding records of the archive exactly, all 3654 moment
  boxes used there are checked by two exact endpoint methods, and the verification is bound to the same archive, exact
  trial and normalization interval; by substitution in the accepted source theorems, `M_V < 0.2972` and the quantities
  derived from it hold for the trial without the canonical moment condition, under their other unchanged hypotheses
  (section 2, shared interval archive);
- the composition of the same archive verification with the zeroth-order residual certificates of section 6: both
  middle-region methods, the inner and exterior certificates (through the archived boundary moments of the first and
  the last knot span and exact propagation identities across these spans) and both whole-plane joinings use exactly
  the archived intervals. The checked dependency chains include the archived boundary moments used by the earlier
  inner and exterior majorants of section 6, whose velocity remainder and coefficient bounds the end-region X norms
  below inherit. The checks rehash all 1558 archive span records and the geometry records for all 7809 middle cells,
  decode the 4192 density coefficient balls and 1044 moment balls in the first and last span records by two exact
  methods, bind the 31 checked input dependencies to their accepted sources, and verify all 17748 exterior
  particular-solution identities by exact forward substitution in two arithmetic implementations. They also separately
  recompute the sums of regional squared norm bounds and the maxima of regional supremum bounds, with two interval
  square-root checks. The verified archive premise is applied separately to each accepted regional certificate and to
  each of the two accepted whole-plane joinings. For the distinguished exactly normalized trial, this discharges only
  the archive condition for their zeroth-order residual bounds, with unchanged values, other hypotheses and evidence
  qualifications. No regional enclosure computation was rerun;
- the canonical meaning of the three-cell instance of 5(l): on the middle cells 0, 4102 and 7808, for all 261 modes,
  the radial Taylor models enclose the trial's canonical `P = l psi/r^2` and `R = psi_r/r` on each whole exact cell,
  first verified conditional on the moment values of the shared archive (the only canonical input membership that was
  open), a condition discharged by the verified archive and its verified composition with this result (next item); by
  its own derivation of the canonical modal equations and their unique solvability, exact comparisons of all 21 input
  arrays of the three cells with the verified sources, exact rational checks of the cell coordinates and lengths,
  three independent enclosures of `e^t` at each of the three cell left ends, and two exact constructions of all 6264
  forcing-box images; the inherited coefficient and remainder calculations of the instance and the full computations
  of the boundary-value and density-polynomial membership checks were not rerun, and the composition on the nine
  rectangles is not covered by this result (it is treated two items below);
- the composition of the archive verification with the Green boundary values and the three-cell radial models of 5(l):
  for the distinguished exactly normalized trial both results use exactly the archived intervals; the identities
  connecting the canonical moments with the Green boundary values and with P and R are rederived in two exact
  arithmetic implementations (9396 scalar coefficients each, all 261 modes), the exact normalization corrections are
  checked, all 1558 archive span records and all 7810 cell boundaries are matched, the exact zero entries of the
  highest mode are checked on every span, and the coordinates, lengths and exponential targets of the three cells are
  rechecked. This discharges only the archive condition of these two results, with all other hypotheses and
  qualifications unchanged; no complete Green boundary or radial Taylor-model enclosure computation was rerun, and the
  radial models of the other 7806 middle cells and the derivative majorants of section 6 (whose inherited canonical
  moment certificates at the cell log-midpoints are not archive values) are not covered by this composition (both are
  treated below);
- the canonical flow ranges on the nine rectangles of 5(l): for the distinguished exactly normalized trial the four
  flow fields `s`, `v_2`, `v_1` and T, with continuous axis quotients, lie in the certificate's 36 reported ranges; by
  exact decoding of all 66 packet arrays (91836 entries) in two methods, exact checks of 21 radial and 45 angular
  array identities with the verified sources and of 522 Chebyshev and cosine-sum polynomial identities, all 7047 cubic
  remainder inequalities in two exact rational implementations, the directed geometry by two interval engines, and the
  containment of the 72 saved reference enclosures in their 36 targets. The modal products of the composition were not
  recomputed, and the qualifications of the runtime radial models are retained; identity with the historical flow
  arrays, cover beyond these rectangles, the flow certificate, a derivative forcing norm, an inverse and an endpoint
  are not covered;
- the radial Taylor models of the flow certificate on all 7809 middle cells (5(l)): for every choice of the inputs in
  their finite boxes and all 261 modes, the runtime degree-12 models with their remainder budgets enclose the
  solutions of the radial modal equations on each whole cell; by two complete interval methods with different
  constructions (exact integer integral weights with ball arithmetic, and a differentiated recurrence on a formal
  basis with separate interval substitution), each passing all 52991874 coefficient and 4076298 remainder
  containments, with all 16305192 forcing coefficients checked exactly against their images; an independent output
  audit regenerated 117135 arrays and checked 720642 coefficients and 55434 remainders by a third method (exact
  particular polynomials) on selected modes of every cell (27717 mode and cell pairs, including every refined
  coefficient), with five complete replay cells; in the first method twelve constant coefficients `R_0` needed the
  exact endpoint refinement described in 5(l), without any change of target or remainder budget, and the second method
  needed no refinement. The third method also needed independently computed endpoint refinements at the same twelve
  constant coefficients. The stopped first attempt of 10-21 19:25 contributes no accepted cell;
- the canonical meaning of these models on all 7809 middle cells: for the distinguished exactly normalized trial, the
  canonical `P = l psi/r^2` and `R = psi_r/r` lie in the models on every closed middle cell for all 261 modes; a
  complete exact reader compares all 54663 input arrays and all 7809 scalar cell records of the computation with the
  verified sources and all 7810 partition boundaries, two exact algebraic constructions check 19410 forcing weights,
  2088 forcing forms, 3132 coefficients of the radial equations and 1566 sum and 1566 difference coefficients, and the
  identities connecting the canonical moments with P and R are rederived; the Green boundary and density memberships,
  with the archive condition discharged, place the canonical input point in the input boxes, and uniqueness for the
  linear modal equations identifies its solution. At an original knot the coefficients are those of the right-hand
  polynomial continuation. No angular product, flow inequality, physical derivative bound, inverse or endpoint is
  covered;
- the axis velocities at x = 7 and 10 (one complete outward interval sum per point, with independent remainder
  bounds);
- the frozen conjugation, coercivity and cokernel theorems;
- the scaling identities and the abstract Fredholm bookkeeping (no Fredholm index is established for any proposed
  IPM realization);
- the weighted saddle model, including the exact feasibility arithmetic (rational, with an interval cross-check);
- the face velocity splitting, with the constants recomputed by two interval methods;
- the inner-disc residual majorant (two interval methods);
- the exterior residual majorant and the complete exterior certificate with the exact leading cancellation (two
  interval methods);
- the collar coupling lemma of 5(i), with its constants (two interval engines);
- the tail uniqueness lemma and the conditional kernel and family theorems of 5(h);
- the isotropic energy symbol at the saddle;
- the complete inner and exterior residual certificates (section 6);
- the middle-region residual certificate (section 6): two complete interval computations (from the physical Green ODEs
  and from the density moment ODEs, with a coefficient overlap check in every cell) based on the same accepted
  canonical density moment archive, reconstructed independently of the numerical team's code, with audits of every
  saved output; the archive condition of these bounds is discharged by the verified archive and its verified
  composition with them (above);
- the joining of the three regional residual certificates into the whole-plane zeroth-order bounds (section 6), with
  separate interval checks of the middle weight factors and integrals; its middle inputs dominate the bounds of both
  middle methods, and a second joining from the joint middle cell bounds gives `N_0 < 1.903991978e-3` (the archive
  condition is discharged in the same way);
- the explicit frozen source inverse formula and the counterexample to a local source condition (sections 4, 5(b));
- the y-axis swap, smoothing and compactness statements and the weighted-jet counterexample (5(j), section 4);
- the exact feasibility margins at the revised working point (5(e));
- the centre obstruction for the trial's residual in the corner product weights (section 4), by exact Fourier
  arithmetic on the stored coefficients (two independent reconstructions) and two independent interval evaluations of
  the frequency-523 coefficient;
- the corner coefficient kernels, their boundedness criteria and exact dual norms, the corner coupling coefficients
  `J_c = 0` and `K_c`, and the failure of a corner coupling bound on the whole-plane pure weight (5(k), section 4),
  with its own proof, exact algebra and two interval methods for the norm enclosures;
- the conditional flow, transport-inverse, box-cost and far lower bound statements of 5(l), with their constants by
  two interval methods, and the trial's exterior flow certificate (5(l)) from a standalone density-moment
  reconstruction of all velocity modes;
- the trial's flow margins on the inner disc and on `r >= e^{t_b + 9}`, by two interval methods and a third audit; its
  margins on `r >= e^{t_b + 5}` (`T < -0.22`, `s, v_1, v_2 > 5.57`), by analytic transfer of the verified exterior
  velocity decay and two independent rigorous scalar enclosures; and the exact vanishing of `rho` and `grad rho` on
  the y-axis, from the factor `x^2 y` (5(l));
- a finite exact audit of the middle-region modal maps used by the numerical team's flow certificate: for all 7809
  radial cells, the interval images of the frozen modal maps were compared exactly with the stored ones (48,915,576
  integer comparisons, all passed). This audit covers those finite maps only; it does not verify the subsequent flow
  fields, their arithmetic or the coverage of the region, and it does not establish the provenance of an older stored
  output;
- a finite audit of the angular part of the same flow certificate: exact identities for the angular mode factors,
  their axis limits, third-derivative bounds and the velocity formulas; endpoint and half-width enclosures of all
  51000 angular nodes of depth at most 7 by two interval methods; exact rational checks of all 4176 finite remainder
  values; all coefficient boxes at 221 cell centres (200 base centres and 21 refined ones) by three methods; and, for
  the angular arrays as regenerated from the frozen certificate source, every coefficient box at all 51000 cell
  centres (119799000 boxes) and the endpoint and half-width outputs of every cell, by two interval engines of
  different implementations and a complete higher-precision replay, with exact rational checks. The identity of the
  regenerated arrays with those of the historical numerical run, the radial models (apart from their verification on
  all middle cells, 5(l)), the assembled flow fields (apart from their composition on nine rectangles, 5(l)) and the
  coverage of the region are not verified;
- a finite scalar audit of the same flow certificate: for all 19389 radial cells (7809 middle, 8948 outer, 2632
  inner), independently reconstructed scalar enclosures and the exact radial geometry; exact rational checks of 523503
  step powers and 444 rational constants; the start-ball exponentials, reciprocals, rational images and radial
  endpoints by two interval methods and a third high-precision audit; the largest step of the flow integration is
  below 1. This scalar audit does not verify the radial Taylor models and their common anchoring, the integration and
  truncation tails, the matrix products, the complete angular coverage or the cell field inequalities; the separate
  canonical radial and flow-range results have the limited scope stated in 5(l);
- a finite scalar audit of all 19389 saved rows of the numerical team's residual derivative certificate (7809 middle,
  2632 inner, 8948 outer): two exact rational calculations verified `max A < 0.4195` and `max B < 713.2` for the saved
  expressions A and B defined in section 6, each expression also enclosed by two interval methods, and two independent
  derivations checked the conditional polar-to-Cartesian implication for the Euclidean gradient norm and each
  Cartesian second partial derivative. Checking every saved row establishes the completeness of the file audit, not
  the coverage of the region; read exactly, the saved cells leave gaps within their combined hull in `log r`: the
  middle cells cover their hull and overlap the adjacent cells at both joins, while the inner and outer cells leave
  405 and 1563 open gaps between consecutive cells, of total length `5294293/2^62` (about `1.1e-12`) in `log r` (two
  exact methods, a rational running-maximum merge and an integer endpoint sweep, with a separate exact check of the
  rounding of all 38778 decimal source values of the cell starts and widths); the coherent cells intended by the
  producer, with exact rational starts, cover the closed annulus `b_- - 5 <= log r <= b_+ + 17` without gaps, each
  exact start lying in the producer's input box for it and each exact width being at most the saved width, and the
  displacement of the saved starts changes the weight by a factor below `1.00000000000004` (two exact methods, with an
  exact emulation of the producer's binary64 width and start computations from its current source); this gives the
  conditional weighted-norm theorem of section 6 on that annulus, with the bounds 0.385656 for the residual and
  585.874 for `eps~ - partial_t eps~` under its majorant hypotheses, which are not verified (its regularity premise
  holds for the trial). The cell majorants (apart from the 63 on three cells validated below), the producer's original
  Taylor models and arithmetic, the link between the producing execution and its source, the numerical
  canonical-moment inputs, the weight lower bound, the extension of the reported normalized pointwise derivative
  ceilings to the two radial end regions omitted from those tables and, for the literal cells, derivative bounds on
  the gaps are not verified (the X norms on the two end regions outside the coherent annulus are bounded separately,
  next item). At the 13 sample log-midpoints of section 6, from the inherited canonical moment certificates (verified,
  see the centre-moment item below), two interval calculations enclose all odd sine coefficients of the residual's
  log-radial derivatives through order 5, and the upper ends of the resulting pointwise Wiener sums are at most the
  138 saved majorants available there; this is a sample check, not a cell bound; and whole-cell upper bounds for the
  same Wiener sums through total order 5 on three closed middle-region cells (rows 4102, 4125, 4211), from Taylor
  coefficients enclosed by two methods and Cauchy tail estimates, from the same inherited inputs; these first bounds
  exceed the saved majorants, but a Bernstein range refinement of the same polynomials on eight fixed subintervals per
  cell (exact affine composition and midpoint subdivision, coefficient uncertainty and the same tails) gives bounds at
  most all 63 saved majorants of those cells, which are therefore verified there;
- the X norms of the residual and of `eps~ - partial_t eps~` on the two radial end regions `r <= exp(b_- - 5)` and
  `r >= exp(b_+ + 17)` outside the coherent annulus (bounds in section 6): own proof; exact differentiation of the
  exact inner density expansion by two methods (14672 identities), with velocity derivative bounds from the Green ODEs
  and the velocity remainder bounds of the inner-disc residual majorant; reconstruction of all 2992 product blocks and
  10 nonleading linear blocks from the saved constituent bounds of the exterior residual majorant by two exact
  rational implementations, assembling 3508 exterior coefficient bounds and taking, for each coefficient, the larger
  of the saved and reconstructed upper endpoints; 10524 exact derivative-coefficient identities; all 3508 weighted
  radial integral factors by a factorial sum in 512-bit Arb and by an integration-by-parts recurrence in 200-digit
  interval arithmetic; every published ceiling compared exactly with both interval endpoints; also checked in two
  completed referee reviews and separate adjudications. This finite application inherits the inner-disc and exterior
  residual majorants (items above), their discharged archive premise and the regularity premise. The conditional
  full-plane bounds of section 6 follow by adding squared norms; the majorant hypotheses on the 19389 cells of the
  annulus remain unverified;
- the direct whole-plane X norms of the residual and of `eps~ - partial_t eps~` (bounds in section 6): own proof;
  velocity derivatives from the Green ODEs applied to the verified radial models on all 7809 middle cells; all
  polynomial products of the Leibniz expansion on every cell by exact integer multiplication and by modular
  multiplication with an independent Chinese remainder reconstruction, compared on every coefficient; Wiener error
  bounds and the inner-disc and exterior terms in 512-bit Arb and in 200-digit interval arithmetic, with exact
  rational accumulation of the outward-rounded upper endpoints; an output audit of every saved row with complete
  replays of seven cells, including both end cells, and of the inner-disc and exterior terms, and an exact
  recomputation of the final sums in a different order; directed decimal display of the regional squares and an exact
  check that the squares of the displayed whole-plane bounds exceed the corresponding sums of the regional squares;
  also checked in a completed referee review of the computation followed by a separate adjudication, and in a
  completed referee review of the regional composition with a corrective follow-up, followed by a separate
  adjudication. These first bounds are coarse because of their exterior term and do not verify the saved majorants of
  the conditional theorem of section 6;
- the sharper exterior term of the direct whole-plane X norms (bounds in section 6): own proof; 89 exterior cells with
  exact rational endpoints covering `b_+ <= log r <= b_+ + 17`; Taylor polynomials of the exact exterior expansion
  with analytic derivative remainders, checked against a second expansion of the differentiated input; the residual
  polynomial by interval convolution and by exact integer centre-radius convolution, compared on every coefficient;
  Bernstein whole-cell bounds; outward interval integration by the decreasing weight; the end-region tail of 10-21
  23:48 joined at `b_+ + 17` and added once; a complete output audit with full replays of four cells, including both
  end cells, and an independent exact rational reduction of all 89 saved rows; the composition with the middle and
  inner squares as before, with directed decimal display and an exact check that the squares of the displayed
  whole-plane bounds exceed the corresponding sums of the regional squares; also checked in a completed referee review
  of the exterior computation and one of the composition, each with a corrective follow-up and each followed by a
  separate adjudication.
- the sharper inner term of the direct whole-plane X norms (bounds in section 6): own proof; 44 inner cells with exact
  rational endpoints covering `b_- - 5 <= log r <= b_-`; the contribution of the cubic `x^2 y` to the linear residual
  cancelled exactly before interval arithmetic (the products with the velocity use the full density); Taylor
  polynomials of the velocity modes from their Green ODEs with the exact central strain subtracted and derivative
  errors from the exact ODE defect, compared on every coefficient with a second construction from a different pair of
  Green ODEs; the residual polynomial by interval convolution and by exact integer centre-radius convolution, compared
  on every coefficient; Bernstein whole-cell bounds; outward interval integration by the decreasing weight; the
  end-region tail of 10-21 23:48 joined at `b_- - 5` and added once; a complete output audit with full replays of four
  cells, including both end cells and the cell of largest contribution; the composition with the middle and exterior
  squares as before, with directed decimal display and an exact check that the squares of the displayed whole-plane
  bounds exceed the corresponding sums of the regional squares; also checked in a completed referee review of the
  inner computation and one of the composition, each with a follow-up exchange and each followed by a separate
  adjudication.
- the lower bound for `||K||_X` and the necessary inverse constant (section 10, next step 1): own proof; the annuli of
  three whole knot spans of the middle region, with exact rational endpoints in `log r` and disjoint interiors;
  angular Parseval for the exact sine series of K and `X.grad K`, the increasing radial weight evaluated at the inner
  endpoint, and the complement omitted as nonnegative; the 6264 exact rational coefficients each of the density, of K
  and of `X.grad K` on these annuli (18792 in all) compared literally between two spline constructions (Cox and de
  Boor recurrences); the three exact square integrals by monomial and by shifted-Legendre integration; the endpoint
  weights in 512-bit Arb and 220-digit interval arithmetic with different weight formulas; replay of all three annuli;
  strictly downward directed display with exact checks of the squared endpoints; the quotient with the direct bound
  for `L K` of section 6, and its transfer to `D cap {J = 0, c = 0}` by the graph approximants of next step 1; also
  checked in a completed referee review with a corrective follow-up, followed by a separate adjudication.
- the inherited centre-moment certificates of these derivative checks (section 6): a second integration of the
  canonical moment equations, from exact analytic anchors that include the complete inner and outer tails and the
  normalization term, using exact particular polynomials of the degree-7 spline pieces on all 1558 knot spans in each
  direction and outward interval exponentials (a method different from the original exponential-moment series), shows
  that all 6786 inherited moment intervals at the 13 sample log-midpoints contain the canonical moments of the exactly
  normalized trial and that all 27248 inherited local density coefficient intervals contain its exact coefficients; an
  independent exact audit rereads every saved interval and reconstructs all 783 exact anchors (it is not a third
  integration). This discharges the inherited canonical moment condition of the 13-point check (273 Wiener intervals)
  and of the whole-cell bounds and the 63 verified majorants on the cells 4102, 4125 and 4211, with their other
  hypotheses unchanged; no other cell and no global derivative bound is covered;
- the variable-coefficient source theorem above threshold (5(d)), the quadratic term in a transport graph norm (5(g))
  and the conditional two-norm iteration theorem (section 7, as an abstract statement);
- the further statements of 5(l): the axis jets of the transport, the trial's axis crossing cell and flow ends, pure
  transport at a source, the source eigenvalues, and the radial defect criterion (abstract), with its finite-input
  instance for all 261 modes (first on three middle cells, now on all middle cells) and the composition into the flow
  fields on nine rectangles formed by three of these cells (the Green boundary inputs and the density polynomial boxes
  are verified for all middle cells, the radial models are verified on all middle cells and enclose the canonical
  modal quantities there, and on the nine rectangles the canonical flow fields lie in the certificate's ranges, as
  listed above; the angular linkage beyond the nine tested rectangles and the full flow certificate are open; a first
  attempted full check of the radial models had stopped at middle cell 2955, mode 135, coefficient `R_0`, where two
  exact rational calculations, including separate decoding of the original inputs, placed this coefficient's exact
  range over the independent input boxes strictly inside the unchanged candidate ball);
- the far-domain facts and the diagonal jet rows of 5(m), and the lower-order obstructions of 5(n);
- the local a priori estimate and the auxiliary inverse at the source (5(o)) with their constants, the sign convention
  of the raw strain, the exact implication from a coefficient bound `C_src < 13.34` to `K_1 < 0.318`, independent
  bounds `M_rho < 0.5059` and `M_V < 0.2972` of the density and velocity Hessians on the source disc and the resulting
  `C_src < 13.91094`, `E < 0.22953051`, `K_1 < 0.3181` (the bound `M_V`, the displayed bounds derived from it, and
  numerical source applications that use archived canonical density moments were first verified under the canonical
  moment condition, since the two source propagation methods do not independently validate their shared moment inputs;
  the condition is discharged by the verified archive and its verified composition with these source results, above),
  and the cell-cover geometry of the exported coordinate masks of the numerical team's coefficient pass;
- the sum-of-squares coupling bound and the conditional statements for an outer estimate with a source cutoff
  (section 10, item 1), under their stated hypotheses;
- the trial instance of the hypotheses of the local source estimate, of the auxiliary inverse and of the source cutoff
  sign (exact source bracket, `D_P`, `grad rho~(P)`, regularity; 5(o));
- the jet-continuity exclusion of section 7, and the strain part of the source velocity of the difference between X3
  and the trial (section 7);
- the order family `s in [61/20, 31/10]` of the local source estimate, and the moving-source statements for perturbed
  profiles (location, source data, stationarity at the moved source, transported local estimate; 5(o), section 7);
- an explicit bound below `1.2e35` for the auxiliary source inverse of the trial with one explicit `C^4` cutoff, for
  every s in `[61/20, 31/10]` (5(o); an upper bound only);
- the isotropic dilation corollary of the auxiliary source inverse in the scaled norms `N_{1/ell}` (5(o));
- certified scaled bounds of the auxiliary source inverse of the trial for the same explicit cutoff: below 922 in
  `N_500` and below `1.223e11` in `H^s` for every s in `[61/20, 31/10]` (5(o); upper bounds only);
- the rough-coefficient extension of the local source estimate and of the auxiliary inverse, with the completion on
  whole-plane `H^s` functions with zero value and gradient at the origin and the global Hessian bound of `W[h]`
  (5(o));
- the whole-plane Sobolev ball: the moving-source hypotheses and `K_1 < 0.32123200` uniformly for corrections of norm
  at most 7/50 in `H^{153/50}(R^2)`, and the narrow non-stationarity of the trial at radius `3.2318e-7` in that norm
  (5(o));
- the leading-tail separation of X3 and the trial (weighted `L^2` membership of `X3 - rho~` in `L^2(<r>^{-2 beta} dX)`
  exactly for `beta > 1 + k`), with the angular witness at `theta = pi/4` from two interval engines and an exact audit
  of the coefficient files (section 2);
- the far residual of the trial (its `sin theta` coefficient from two interval engines) and the nonexistence of exact
  solutions in `rho~ + L^2(R^2)` (sections 2, 7);
- the exactly normalized tail repairs `rho_T`, with residual in `L^2(R^2)` and factor distance below
  `0.334616 T^{k-1}` (two interval engines and an exact rational audit of the linear map; section 10, item 4), and the
  higher repairs `rho'_T` with residual of finite homogeneous `dot H^{-1}` norm (two independent readings of the
  original binary64 coefficient data, exact nonresonance, exponent and identity checks, and an independent output
  audit; section 10, item 4);
- the asymptotic lower bounds for the residual norms of both tail repairs in `L^2(R^2)` and `H^{-1}(R^2)`, and for
  `rho'_T` in `dot H^{-1}(R^2)` and for `||r eps'_T||_{L^2}` (exact polynomial antiderivatives and, independently,
  Beta and logarithmic moments and a Simpson rule with a derivative bound, with an exact Peano-kernel check; section
  10, item 4);
- the nonzero `r^{3k-2}` and `r^{k-2}` residual rows of `rho_T` (its `r^{3k-2}` coefficient `C_{2,0}` and the
  counterterm coefficient `H_{2,0}`, by two interval engines with an exact support and exponent audit; its `r^{k-2}`
  coefficient `L_d` as an exact rational multiple of `R_b^{5-k}`, by two interval engines with an independent audit),
  and hence that the residual of every `rho_T` is not in `dot H^{-1}(R^2)` (section 4; section 10, item 4);
- the local velocity bounds of the tail repairs `rho_T` near the origin and the source and the resulting lower bound
  of their source defect at P (two interval engines, exact series and source audits and a separate replay; the referee
  review refuted one supporting claim, that the trial is of class `C^6` at the origin: it is `C^4` there and not
  `C^5`, and `C^3` suffices; section 10, item 4);
- the factor-distance constants of the higher tail repairs `rho'_T` (all coefficients of the two counterterm rows by
  two interval engines with different source forms, convolution arithmetic and quotient inversions, and an exact audit
  of the inputs, supports and quotient basis vectors; recomputed again from the original data in a separate referee
  review; section 10, item 4);
- the finite-mode local velocity bounds of the higher tail repairs `rho'_T` for every admissible T (the complete
  finite derivative sums in one interval engine and, independently, the coarser majorant with the `sin(5 theta)`
  coefficients separated and a proved geometric tail in another, with an exact audit of the inputs, projections,
  derivative weights and geometric sums and two complete reruns; the three angular rows, their `sin(5 theta)`
  coefficients and quotient sums reconstructed again from the original data in a separate referee review; section 10,
  item 4);
- the frozen Hoelder alternative at P, the axis identities and smoothness criterion for `B_3`, the trial's degree-five
  resonance, and the transition with collapsing transverse scale (section 10);
- the centre regularity of the numerical team's second trial and the nonzero change of its exterior stream
  coefficient relative to the first trial (section 10, by exact arithmetic);
- the far expansion of `rho_x` of X3, including its four leading allowed powers, remainder order and analytic angular
  coefficient formulas; the exact central-strain identity for changes of the exterior source; and exact strain moments
  of synthetic sources defined by the recorded fit amplitudes and exponents. Separately, exact-arithmetic checks
  established the rounding and arithmetic consistency of the recorded maxima, coordinates, relative changes and
  multipliers in the summaries underlying the closure tests of section 6. The evaluator was not rerun, and the
  numerical team's later repetitions were outside this audit;
- for the two frozen finite sections of the diagnostic experiment of section 10, next step 1: the exact source-defined
  matrices of the external `C^1` join conditions have full row rank 64 and 96 (determinant and elimination methods in
  exact arithmetic); every external-join row value of each of the five saved trapezoid-weighted derivative-row arrays
  with prescribed `C^1` external-join constraints is exactly nonzero, with maximum absolute values in the unscaled
  source rows strictly below `1.672e-15` and `3.725e-15`; and, in floating arithmetic on a finite radial interval, the
  shares of the diagnostic energy in the sine frequencies 1 and 3 of the smallest derivative-row and
  trapezoid-weighted directions computed from the saved profiles. The identification of the rows with the claimed
  physical trace constraints, the call-time inputs of the reported runs and the matrix decompositions reported for
  those runs remain unverified; the harmonic-share recomputations are floating-point diagnostics;
- for six preselected saved directions of the stride-refined and angle-refined finite sections of section 10, next
  step 1 (the source-labelled first, third and fifth weakest trapezoid-weighted value-row directions and the
  source-labelled weakest trapezoid-weighted derivative-row direction of the stride-refined section, and the
  source-labelled weakest direction of each of these two forms in the angle-refined section): for each selected saved
  image, the four quotients `Q_R = (E_R/g)^{1/2}`, formed from the exact finite energies `E_R` of the value-row and
  derivative-row forms with and without trapezoid factors and from that image's positive saved scalar g, agree with
  all 24 corresponding stored quotient values to absolute error strictly below `2e-12` (two interval methods, with
  independent import of the binary data). This concerns those literal arrays only: the saved images are not certified
  operator images, g is not certified to be a norm, the ranking of the directions is not certified, the selection is
  not representative, and no singular value, coercivity or convergence statement follows;
- for the two saved images of the source-labelled weakest direction of each trapezoid-weighted form in the
  angle-refined finite section of section 10, next step 1 (two of the six images of the preceding item): the share of
  the stored energy of output modes 0 to 39 that lies in modes 32 to 39 is below 0.016 percent in each of the four row
  functionals (two interval methods, with independent import of the binary data). Separately, the ten relative changes
  `|a - b|/|b|` of the five smallest stored trapezoid-weighted derivative-row values of that section under the output
  cutoff (`a` with 32 and `b` with 40 output modes; at most `2.734e-5`) and under the stride at output cutoff 32 (`a`
  with stride 8 and `b` with stride 16; at most `1.163e-3`) were recomputed from the stored binary64 values in exact
  rational arithmetic by two independent codes; all ten are nonzero. These are literal observations on saved arrays
  and scalars: the stored values are not certified singular values or minima, equal labels do not certify identical
  assembled spaces or forms, and no bound for output modes 40 and above and no convergence statement follows;
- for the smaller finite section of section 10, next step 1, at two, four and six collocation points per cell: the 40
  relative changes of the five smallest stored values of the four row functionals (value and derivative rows, with and
  without trapezoid factors) between consecutive densities, relative to the value at the coarser density, recomputed
  from the stored binary64 values in exact rational arithmetic by two independent codes (all nonzero; for the
  trapezoid-weighted forms at most `2.213e-4` and `2.447e-5` for the value rows and `3.240e-4` and `6.760e-5` for the
  derivative rows; for the smallest unweighted values increases of about 40.5 and 21.8 percent for the value rows and
  38.8 and 20.5 percent for the derivative rows); the byte identity across the twelve saved runs of all selected
  encoded inputs, among them the trial scalars, the column labels and the partial Gram arrays; and the saved
  retained-column counts. These are literal observations on saved arrays and scalars: the stored values are not
  certified singular values, equality of the retained subspaces is not certified, and no convergence statement
  follows;
- for the floating X norms of section 10, next step 1: the analytic identities used (the Leibniz and sine-product
  formulas for the residual and its first two derivatives in `t = log r` in terms of the modal amplitudes of density
  and stream function, and the expression of the weighted norm of an odd sine series through its modal coefficients);
  exact agreement, without tolerance, of the code computing the residual mode jets, in the checked source version,
  with an independent integer implementation on synthetic integer inputs at `t = 0` (10350 entries, and 1104 entries
  for 80 bilinear basis pairs); and outward enclosures of the square roots of the stored squared norms of the
  four-node calculation, in the version before the correction of the regional values, and of their quotient (about
  170.52). This gives no floating error control on the trial, is not a quadrature error bound or a certified norm,
  omits `r < 1e-4` and `r > 1e7`, and does not link the stored values to the executed code or to the canonical fields
  of the trial;
- for the projection diagnostics of section 10, next step 1: the Hilbert-space identity relating the relative distance
  to an exact orthogonal projection with the captured energy, and outward enclosures (59 independently decoded saved
  scalars; square roots by two interval methods) of the relative distances implied by the saved energies of the
  revised computation, read as exact dyadic numbers: `(1.81776, 1.81779)`, `(1.81764, 1.81766)` and
  `(1.76198, 1.76201)` percent for the `C^1`, `C^0` and free-tail variants of the smaller section. Objections raised
  and retained: the earlier reading of 99.5 percent captured energy as a distance of 0.5 percent is refuted (the
  identity gives about 7.07 percent), and four earlier saved full-energy ratios exceed 1, so they cannot describe
  exact orthogonal projections in one Hilbert norm. These are intervals for arithmetic on saved floating numbers; no
  Gram matrix, projection, operator image or norm is certified, and the angle-refined distance is not covered;
- for the assembled-image comparison of section 10, next step 1: the exact sum, in two exact implementations, of the
  42 saved partial image arrays (all 18680 entries), its entrywise comparison with the saved assembled and direct
  arrays, and enclosures of the four discrete row functionals by two outward interval methods; the ratios
  `F(S - D)/F(D)` for the exact sum S and the direct image D are about `5.365e-5`, `4.185e-5`, `5.788e-5` and
  `4.953e-5`, and the saved assembled array differs from S by less than `7.11e-15` entrywise and by less than
  `1.032e-11` relative to D in each of the four row functionals. Objections retained: nine proposed agreement
  tolerances with the saved summary values fail (the four difference functionals, their four normalized forms and the
  largest entry difference), so agreement with all printed digits of the saved summary is not established; only the
  coarse comparison and the stated discrepancy bounds are confirmed. The historical origin and accumulation order of
  the saved assembled array are not authenticated, no mode image is reassembled, and no continuous norm, quadrature or
  tail error, physical scaling image or projection is certified;
- for the explicitly paired stored modal trial and frozen column recipe of the smaller finite section of section 10,
  next step 1, the exclusion of the stored trial's scaling tangent from the tail class containing that recipe's column
  functions (statement in section 10, next step 1): two independent decodings of 523 stored section scalars and of the
  5996 scalars in the paired trial's stored outer coefficients, outer corrections, knots, `k`, `L` and outer
  correction rate; exact agreement of all 260 stored leading coefficients with the exact rational export of those
  stored coefficients; computation of the minor in two exact rational implementations and its enclosure by two
  interval implementations; and exact checks that all lower exponential rates, including the outer correction rate,
  lie strictly below the leading rate and that the scaling factor `-2 - lambda` is nonzero. The rate checks cover
  exact `lambda = k - 3` and the binary64-rate convention `lambda = fl(k - 3)` separately. This concerns the paired
  stored trial and stored column recipe only; no assembled matrix, executed run, exactly normalized trial, free-tail
  variant, angle-refined section, norm closure, distance or image estimate is certified by these checks;
- for the exactly joined and exactly normalized trial and the same frozen column recipe, the exclusion of its scaling
  tangent from the two exterior classes of section 10, next step 1 (leading tails at the exact rate `k - 3` or at the
  binary64 rate of the recipe, lower parts of rates at most mu): two independent decodings of all 523 saved section
  scalars and of all 2600 stored outer coefficients, exact checks of the 260 leading coefficients and of all 261
  entries of the stored second tail vector, reconstruction of the exact and the rounded rates by two methods with the
  exact gap `2^{-53}`, the endpoint values of the determinant over the certified normalization interval in two exact
  rational implementations and its enclosure by two interval implementations. This concerns these two exterior classes
  only; no free-tail or other span, norm closure, positive distance, assembled matrix, projection, forcing norm or
  inverse is certified;
- statements about the diagnostic `H^1`-type norm of section 10, next step 1: the indicator-type J references are
  outside the space (their quoted cosines use piecewise gradients); the central coefficient is unbounded in that norm
  (two exact arithmetic methods for the constants); the integral form of the raw strain is bounded in it (two
  arithmetic methods for the constants; its identification with `psi_xy(0)` is subject to the stated hypotheses);
  under the stated finite-piece and endpoint-growth assumptions, membership is equivalent to exact value continuity;
  and every tested mode-zero interior spline column of the conditioned sections (90 and 187 at the two section sizes)
  has a nonzero jump of its saved radial polynomial pieces (two exact methods), so its encoded density is outside the
  space; within the exact encoded spans the exactly continuous subspace has dimension at most 515 for the smaller
  section and 771 for the larger one (exact rational and independent modular rank methods), and for the smaller
  section the 1866 retained columns exceed 515, so their interpretation as an orthonormal list in the space is
  refuted; and exact repairs of the tested spline columns lie in new continuous subspaces of the space, with
  single-column, single-mode relative broken-energy error below `2.57e-14` (two methods); with both the originals and
  the repairs normalized by the original broken-energy norms, the exact Gram matrices of the selected repaired columns
  differ from the exact broken-energy Gram matrices of the originals by less than `2.31e-10` in spectral norm (two
  arithmetic methods for the bounds; the stated relative comparison is conditional on a lower eigenvalue bound that is
  not available); and, under the stated background regularity hypotheses, the linearized image of a continuous
  piecewise-`C^2` column of the stated finite angular form is `H^1` across a join exactly when all its radial
  first-derivative traces agree there, which fails at every join of every selected repaired column (two exact methods
  for the derivative traces); exact `C^{2,1}` repairs of the same columns have single-column relative broken-norm
  errors from the original columns below `3.38e-14` (two methods); the explicit jump of the image at such a join, its
  term in finite-difference derivative rows, and a model example in which one derivative jump `1e-14` gives terms of
  about `9.94e-8` and `1.41e-8` (symbolic and rational Fourier identities, two interval arithmetics), together with
  the unboundedness of a transport value row in this norm and a conditional transfer inequality for the smallest
  generalized singular value of a fixed finite section; of the three encoded reference densities of the numerical
  team's third version (section 10, next step 1), as reconstructed from the checked source, the radial factor of the
  third has an outer-end value jump strictly between `1.2121e-13` and `1.2122e-13` in absolute value, so that density
  is not in the space, while the other two are of class `C^4` (exact rational endpoint derivatives by two methods and
  an exact reconstruction of the rounded coefficients); and, in the graph norm `||h||_X + ||L h||_X` under explicit
  background and domain hypotheses, every level of the central coefficient is dense, also at fixed strain, so adding
  the constraint `J = 0` does not change the best inverse constant, on the domain or relative to its zero-strain
  subspace (two exact symbolic methods for the canonical stream function and strain of the bump); for the exactly
  normalized modal trial the scaling tangent lies in such a domain with a nonzero image, so every inverse constant
  with `J = 0` and `c = 0` imposed is at least the positive quotient `||K||_X / ||L K||_X` (later bounded below by
  0.069361443018; 5(p) later excludes every finite constant on this domain; symbolic identities against an independent
  differential-polynomial algebra, two exact data decoders, two interval evaluations of the leading coefficient of the
  image); and, under the exact-profile hypotheses of section 10, next step 1 (conditional on the existence of such a
  profile), every X-neighbourhood of it contains a sequence of comparison densities from the admissible class stated
  there, with `J = 1` and the same strain, whose residuals tend to 0 in X while their X distance from it has a
  positive limit, so no residual-to-error modulus controls the distance to that chosen profile in X alone (exact
  piecewise Green integration against an independent exact radial matching solve; two interval evaluations of the
  quadratic constant); and the quadratic term `W[h].grad h` is not continuous at 0 in X alone, even on compact
  densities with `J = c = 0` (four concentrating packets with an exact strain compensator; exact symbolic Green
  integration against an independent exact radial solve, a positive exact energy enclosed by two interval methods).
  This quadratic obstruction concerns X-to-X estimates only. Estimates with h measured in a stronger or graph norm,
  with the quadratic term measured in a weaker norm, or on a specified finite-dimensional class are not covered by it;
  in the graph norm `||h||_X + ||L h||_X`, at a background satisfying the hypotheses above whose transport field V is
  locally `C^1` and vanishes at a point `(p, 0)`, `p > 4`, in particular at the exactly normalized modal trial with
  this point its source, the quadratic term is not continuous at 0 either, even on compact densities with `J = c = 0`
  (two translated packets with an exact strain compensator; two exact methods for the axis strain of the packets and
  two exact rational re-summations of the inherited energy; also checked in two completed referee reviews and separate
  adjudications), while stronger Sobolev graph norms, the norms of the proposed realization, a weaker image norm and
  restricted finite-dimensional classes remain not covered. These results do not determine which retained vectors fail
  to be in the space or are dependent, and they do not refute the floating spectra.
- the centre quasimodes of 5(p) at the exactly normalized modal trial: an independent derivation of the degree-two
  homogeneous solution of the frozen centre transport and of its exponents, the angular and logarithmic cutoff
  estimates, the uniform bounds of the variable-coefficient and nonlocal terms and the exact strain correction, with
  the scalar identities in two exact implementations and the inherited trial hypotheses rechecked against their
  sources, and the choice of the sequence small in `H^{5/2}` and weakly null in X with its compact-remainder, defect
  and closed-realization consequences (graph-norm completeness, a finite-kernel projection and the inverse mapping
  theorem); also checked in a completed referee review and a separate adjudication; and the same construction for
  every more singular centre weight `r^{-2m-2}`, `m >= 2`, with the velocity Taylor coefficients of degree at most
  `m - 2` cancelled, in two exact implementations of the algebra (a side claim of one referee review, that
  perturbations with nonzero strain cannot be mapped into `X_m` for `m >= 3`, was refuted by an explicit annular
  density whose affine velocity and strain terms cancel at cubic order, and withdrawn);
- the centre quasimodes of 5(r) in the weighted factor supremum norm: an independent derivation of the two Green modes
  of `x^2 y chi(r)`, the strain formula, the primitive bounds and the derivative table behind
  `||DU[h]||_inf <= (7 + 3 B_1/8) delta^2`, the cancellation `V_0.grad(x^2 y) = x^2 y`, the exact strain subtraction
  and the decay of the image at infinity, with the finite identities in two exact implementations (symbolic
  differentiation and an exact rational differential ring); the weak convergence by disjoint signed sums and the
  compact-remainder and closed-realization consequences are handwritten arguments; a missing linearity hypothesis on
  the compact remainder, found in the verifier's own review, was added, and an arithmetic error in one referee review
  (a doubled term in the derivative table) was withdrawn in a follow-up; also checked in four completed referee
  reviews, two of them follow-ups, three separate adjudications and a separate referee audit;
- the axis-weighted results of 5(q): the semigroup bound, the identification of the generator domain with the maximal
  domain and the Bochner inverse of the frozen centre transport in `Y_(a,s)`, with the scalar enclosure at
  `(6, 153/50)` and the identities for the homogeneous candidate (two exact decoders of k, two interval evaluations);
  the sin3/sin5 Gram construction, the interior harmonic coefficients, the quartic stream, the degree-five image and
  the lower bound near the y-axis, with the identities in two exact implementations (rational polynomial and symbolic)
  and the hypotheses at the exactly joined trial rechecked against their sources; and the axis equation, the harmonic
  trace, the continuation through the axis gaps, the fractional Sobolev inclusion and the moment map, with the
  identities in two exact implementations; each also checked in a completed referee review and a separate
  adjudication, and all three in a separate referee audit;
- the degree-five density of 5(p): the sine-to-Cartesian identity of `sin 5 theta + sin 7 theta`, the cancellation of
  the third sine coefficient, the interior harmonic coefficients (with `1/8 < Gamma_6 < 1/2`), the cubic velocity of
  the quartic stream, the degree-five image and the two radial integrability exponents, in two exact implementations
  (rational polynomial and symbolic), with the finite-regularity hypotheses at the exactly joined trial rechecked
  against their sources; also checked in two completed referee reviews, a separate adjudication and a separate referee
  audit;
- the axis leakage in the quadrant norms of 5(e): the lower bound of the squared norm by its zeroth summand on a
  rectangle adjacent to the y-axis, with an exact rational check of the working exponent `4 - 2a = -89/10`; also
  checked in a completed referee review, a separate adjudication and a separate referee audit;
- the forward thresholds of 5(q) and 5(e): the identities `a_Y(s) - 5/2 = (D/A)(s - 3/2)` and
  `a_e(b) - 5/2 = (D/A)(b - 3/2)`, the converse below order 3/2, the strict enclosure of `a_Y(153/50)`, and the
  inverses at `delta > 0` (Fourier multiplier) and at `delta_- > 0` (negative-time integral), with the scalars in two
  exact implementations; also checked in a completed referee review, a separate adjudication and a separate referee
  audit;
- the axis coefficient of the trial residual (5(q)): the axis identity, the stream expansion with the origin term
  `-1/64`, the algebra of Q, the exact rational prefactor of B and the exact rational evaluation of the integral (a
  global spline antiderivative in one implementation, an exact eight-node rule on all 1558 spline spans in the other)
  and the enclosures of B and Q in two interval engines (different algorithms; their agreement corroborates the
  implementations, the analysis is separate); also checked in two completed referee reviews, a separate adjudication
  and a separate referee audit;
- the complete frozen classification in `Y_(a,s)` (5(q)): the unitary reduction of the group, the identification of
  the maximal domain, the explicit kernel and adjoint kernel, the wave packets for sharpness and non-closed range, the
  complex shift for the spectrum and the real odd-y restriction, with the differential identities in two symbolic
  implementations (one of them deriving the adjoint directly in the original Fourier variables) and the canonical
  scalars in two exact ones; also checked in a completed referee review with a follow-up exchange, a separate
  adjudication and a separate referee audit;
- the range inside the frozen strip (5(q)): the coercive identity with its plus sign, the infimum of the potential in
  all regimes, closed range and the projection onto the adjoint kernel, the Mellin form of the compatibility
  conditions (analytic; the code assertions on its exponents are not counted as independent evidence), sharpness by
  wave packets, with the quadratic, its minimum and the canonical scalars in two exact implementations; also checked
  in a completed referee review with two follow-up exchanges, a separate adjudication and a separate referee audit;
- the frozen graph domain in `Y_(a,s)` (5(q)): the phase identity, the lower bound of `V.grad phi_fr` on the rectangle
  near P (exact rational arithmetic and directed interval arithmetic, in two implementations with different libraries,
  with the imported source bounds rehashed), the Laplacian and velocity of the compact potentials (Cartesian symbolic
  differentiation and a separate differential-polynomial algebra), the uniqueness of the compact canonical velocity,
  the oscillation bounds, the partial Fourier lower bound and the closed graph consequence (analytic; the finite
  identity checks are not counted as evidence for them); also checked in two completed referee reviews, a separate
  adjudication and a separate referee audit;
- the centre trace in `Y_(a,s)` (5(q)): the compact-potential construction, the exact two-term scaling, the membership
  of the two weighted logarithmic profiles in every `H^N`, the conjugated frozen transport and the nonclosability and
  density arguments (analytic), with the Laplacian, velocity, physical two-term scaling, conjugation and centre
  identities in two symbolic implementations (a computer algebra system and a separate rational differential ring);
  also checked in four completed referee reviews, a separate adjudication and a separate referee audit;
- the centre trace in the graph norm of L (5(q)): the regularity of the canonical velocity of the trial near 0 from
  its finite modal form (`C^{4,alpha}`, and `C^{3,alpha}` for `V_1/x`), the uniform multiplier estimate on `H^s`,
  `s < 4`, for the transformed coefficients, the exact scaling of the transport and coupling terms and the
  nonclosability and density arguments (analytic), with the density, velocity, transport conjugation, coupling and
  radial identities in two symbolic implementations and the parameters, knots and angular source maps in two exact
  decoders; also checked in four completed referee reviews, a separate adjudication and a separate referee audit;
- the quadratic term in the graph norm of L (5(q)): the flow chart at a point of the trial where `V_1 != 0`, the
  plateau potential, the exact compact canonical velocities, the modulation limits and the coordinate and localization
  equivalences of the `H^s` norms on fixed patches, the exact vanishing of one cross term and the growth of the other,
  and the polarization argument (analytic), with the Poisson, plateau, wave expansion, phase, cross-term, reflection
  and polarization identities in two symbolic implementations (algebra only; they do not construct the flow chart or
  prove the Sobolev estimates); also checked in three completed referee reviews, a separate adjudication and a
  separate referee audit;
- the inverse constant and finite constraints in the graph norm of L (5(q)): the density of `J = 0`, the passage to
  the limit in the inverse inequality, the bounded finite correction into the kernel of finitely many graph-continuous
  constraints and the quotient argument for closed subspaces of finite codimension (analytic), with the polarization
  and correction identities in two symbolic implementations and eight manufactured rank cases rebuilt by exact
  elimination (regression checks only); also checked in two completed referee reviews, a separate adjudication and a
  separate referee audit;
- the quadratic term under arbitrary finite linear constraints (5(q)): the two finite eliminations (a nonzero
  dependence among `m+1` vectors of `R^m` for the plateau groups and, for each n, for the packets, normalized by the
  maximum absolute value of its coefficients), the nonvanishing of the combined plateau background by disjoint
  potential supports, the exact selection of one packet's cross term by a smooth cutoff, and the passage from finite
  algebraic codimension to a kernel through the algebraic quotient (analytic), with 56 manufactured finite systems (24
  plateau groups and 32 packet systems; 17 of rank zero, 19 rank deficient, 20 of full row rank) rebuilt by two
  separate exact rational eliminations and three polynomial identities (regression checks only); also checked in three
  completed referee reviews, a separate adjudication and a separate referee audit;
- the quadratic term under regular finite nonlinear constraints (5(q)): the finite-dimensional contraction for the
  correction into the zero set, the bound `|alpha| <= 2 |Phi_cp(y)|`, the packet bounds `||U[k_n]||_Y <= C` and
  `||grad k_n||_Y <= C n`, the correction error `C t_n n |alpha| + C |alpha|^2 = o(1)` and the singular example
  (analytic), with six quadratic perturbation identities rebuilt in a computer algebra system and a separate rational
  ring and 21 manufactured scalar root and scaling examples rebuilt by two separate methods (regression checks only;
  they prove neither the contraction argument nor anything about a particular constraint); also checked in two
  completed referee reviews, a separate adjudication and a separate referee audit;
- the moment map of the range inside the frozen strip (5(q)): the squared fibre norm `(1 + xi_z^2)^{-v/D} N` of the
  representing vector by substitution, the weighted Cauchy-Schwarz bound, surjectivity with the explicit right
  inverse, attainment of the weighted norm, the approximate extremizers and nonattainment for the unweighted bound and
  the real odd-y restriction (analytic), and the enclosure of `N` at `(a, s) = (0, 153/50)` by gamma functions in ball
  arithmetic and, separately, by the two halves of the beta integral as series with rigorous tails in interval
  arithmetic (different algorithms and libraries; both rest on the same beta identity); also checked in a completed
  referee review with a follow-up exchange, a separate adjudication and a separate referee audit;
- the weak-weight mapping of the compact test densities (5(q)): the parity and decay of the stream of h near 0 and at
  infinity (convergent harmonic expansions; the axis quotients by the segment formula), the factor identity for
  `U[h].grad rho~`, the dyadic shell bounds, the interpolation and the summation (analytic), with the factor identity
  and the 15 mixed Euler and y derivative identities in two symbolic implementations, and the exponents and knots of
  the trial behind its differentiated bounds in two exact implementations with different libraries; also checked in a
  completed referee review with a follow-up exchange, a separate adjudication and a separate referee audit;
- the residual at weak weights (5(q)): the exact cancellation of the centre term by the normalization, the
  differentiated factor bounds near 0 and at infinity from the finite formulas of the trial and of its canonical
  velocity (with the axis quotients by the segment formula and the annular regularity by the radial mode equations),
  the dyadic shell bounds, the interpolation and the summation, and the lower bounds at both endpoints (analytic); the
  coefficient `e_1` from the stored binary64 data decoded exactly, by the Green integrals of each mode and a Laurent
  convolution in ball arithmetic and, separately, by the radial Poisson coefficients and the frequency products in
  interval arithmetic (different decoders, algorithms and libraries; both use the same enclosure of the normalization
  scalar, and Q is inherited); also checked in three completed referee reviews, a separate adjudication and a separate
  referee audit;
- the extension of the weak-weight mapping to the orders `0 <= s < 6 - a` (5(q)): the local `W^{7,infinity}`
  regularity of the factor of the trial on compact annuli, the differentiated end bounds through order 7, the shell
  bounds in `H^n`, `n <= 6`, and the interpolation (analytic), with the factor identity and the derivative identities
  through total order 6 in two symbolic implementations, and the scalars, knots and exponents of the trial in two
  exact decoders; also checked in three completed referee reviews, a separate adjudication and a separate referee
  audit;
- the strain functional on `Y_(a,s)` (5(q)): the kernel and its partial Fourier transform, the Cauchy-Schwarz bound
  with the gamma and beta integrals, the density and identification arguments and the rescaled and separated-scale
  counterexamples for `a >= 2` (analytic), and the enclosure of `C_(3/2,153/50)` by gamma quotients and pi in ball
  arithmetic and, separately, by an exact beta reduction, two positive beta series with rigorous tails and a Machin
  enclosure of pi in interval arithmetic (different algorithms and libraries); also checked in two completed referee
  reviews, a separate adjudication and a separate referee audit;
- the scaling term on `Y_(a,153/50)` (5(q)): the membership of the trial and of `X.grad rho~` (the differentiated
  factor bounds near 0 and at infinity from the finite formulas of the trial, the cut-off centre polynomials, the
  shell summation, and the lower bounds from a far sector and an axis rectangle), the bounded rank-one extension and
  its failure outside `1 + k < a < 2`, the centre cancellation and the exterior degree count for the compact test
  images (analytic); the nonzero `cos 2 theta` coefficient of the unscaled cosine factor `P_tail`, decoded exactly
  from the stored binary64 data in rational arithmetic and, separately, by integer hexadecimal decoding with a
  different rational library, and the centre identity in two symbolic implementations (a computer algebra system and a
  separate rational differential ring); also checked in three completed referee reviews, a separate adjudication and a
  separate referee audit;
- the regional aggregation of the fit-stability comparison (section 6): from all 78091 saved cell rows of the trial
  and its three variants, the regional supremum bounds (maxima of the row bounds times the monotone radial weights at
  the outer cell endpoints, in interval arithmetic), the integral bounds (exact sums of the row bounds), the exact
  relative changes of the published aggregate bounds, 52 printed residual ceilings and the 16 printed scalar
  intervals, in two implementations with different binary64 decoders and arithmetic libraries; conditional on the
  saved per-cell bounds, on the coverage of each region by its cells and on the reconstruction of the variants, which
  are not audited; also checked in a completed referee review with a follow-up exchange and a separate adjudication.

Preliminary audits of the text of this report by the verifier (checks of the wording against the verified results, not
verifications of new results): at 10-22 06:18 the item on the quadratic term in 5(q) of the draft of 10-22 06:12
(which then treated finite linear constraints only) was confirmed against the verified proofs, with no repair
required; at 10-22 06:42 section 1 of the same draft and 26 results recorded in the verification timeline were found
consistent, with their time labels, with the accepted results at their stated scope, with no required correction, and
the elapsed time stated in that draft was confirmed. The two optional clarity items of the second audit (on the four
jet values and on the hypotheses of the moving-source forms) are adopted in section 1. These audits concern that
draft, not the later changes, and the second does not validate every entry of the timeline. Also checked in two and
three completed referee reviews respectively, with one separate adjudication for each audit. At 10-22 07:07 the
verifier further confirmed, for the draft of 10-22 06:58, that the section 1 wording on the four jet values and the
moving-source hypotheses, the preceding sentences of this paragraph and that draft's compound timeline entry on these
audits match the audits, with no required repair (also checked in two completed referee reviews and a separate
adjudication). At 10-22 08:22 the verifier checked the family wording in 5(h) of the draft of 10-22 07:23 against the
verified proof: that wording is consistent with the proof when the far corrections C are fixed, as in the ansatz, and
the statement that the corrections of the referee audit of these theorems are included need not be withdrawn; the two
clarifications it recommended (C independent of `Theta`, `k'` and `tau`; differentiability of the family in the
realization needed to linearize F and c) are adopted in 5(h) (also checked in two completed referee reviews and a
separate adjudication). At 10-22 10:51 the verifier checked the draft of 10-22 10:32: section 1, read afresh in full,
and every change since the draft of 10-22 07:23, including every displayed decimal they contain, the direct
whole-plane bounds and the description, corrected in that draft, of the exterior residual as products of input factors
affine in the enclosed scalars, are consistent with the verified results at their stated scope, with no required
correction (also checked in a completed referee review with a follow-up exchange and a separate adjudication). At
10-22 12:02 the verifier checked the draft of 10-22 11:34 in the same way: section 1, read afresh in full, and every
change since the draft of 10-22 10:32 (22 changed passages, among them six new timeline entries, with the displayed
decimals in them) are consistent with the verified results at their stated scope, with no required correction (also
checked in a completed referee review with two follow-up exchanges and a separate adjudication). Each audit concerns
its draft, not later changes; unchanged earlier text keeps the limited scope of the earlier audits. At 10-22 12:12 the
verifier checked the mathematical content of the draft of 10-22 12:00: section 1, read afresh in full, and the nine
changed passages since the draft of 10-22 11:34 (the lower bound for `||K||_X`, the necessary inverse constant and
their scope wording) are consistent with the verified results at their stated scope; its one wording recommendation
(6264 coefficients each of the density, of K and of `X.grad K`) is adopted (also checked in a completed referee review
with a corrective follow-up and a separate adjudication). That audit left the timing statements of that draft open;
they are superseded by section 3 of this version. At 10-22 12:29 the verifier checked the three changed passages of
the version of 10-22 12:15 (the records of these two audits and the adopted wording) and confirmed them, except that
the clause stating that the timing of the draft of 10-22 12:00 is superseded by section 3 was not yet correct in that
version, which still carried the earlier end time; it became correct with the timing change of 10-22 12:21. At 10-22
12:36 the verifier checked the timing changes of the version of 10-22 12:21 (nine sessions, eight gaps, the end time
of that version) and confirmed them, leaving open the statements about the actual end of the run. The finalization
after the limit of the run (the summary at the top, the end-of-run record of section 3 and the description of the
accompanying artifacts in section 9) summarizes the mathematical results at their recorded scope and was not
audited by the verifier; its final timing and editorial-only claims are reported, not independently certified.

Objections raised and resolved:
- The first specification's derivative-gaining inverse and logarithmic far space were refuted and replaced.
- The second specification's below-threshold Weyl assertion was refuted and withdrawn.
- A weight-convention ambiguity was corrected.
- An over-broad claim about `P_infty` solutions was withdrawn.
- A sign criticism of the residual code was withdrawn by the verifier after checking the right source snapshot.
- The analysis's inference of a necessary `1/|mu~ - 1|` cost for the coupled inverse was refuted by the uniform
  frozen inverse of section 5(c) and withdrawn.
- The analysis's claimed derivative gain larger than 2 for the edge forcing was refuted (the gain is `b - 3/2`),
  together with its bounded-coupling conclusion on pure face weights (5(f)). One regional constant of the face
  splitting was corrected (`2^{|b|}` in place of `2^b` for `N = 0`, `b < 0`; the stated total for `N = 3` is
  unaffected).
- The saddle inverse norm was made precise: `1/|delta|` in the base norm, `1 + 1/|delta|` into the sum graph norm.
- Tail and family theorems (5(h)): our first version claimed that `c_l` is locally constant on the family iff
  `ell = 0` at one solution (false; only first-order stationarity follows), used a profile set with profile-dependent
  support (not a Banach space; replaced by a fixed neighbourhood), and inferred pointwise growth from weighted `L^2`
  (false; extra embeddings added). The referee audit added: a bounded (not merely algebraic) fixed-tail inverse,
  parameter continuity of the solution (in X and in both scalar coordinates) as a separate hypothesis, nonzero total
  tail, a domain hypothesis for the scaling tangent, and differentiability of the family for `ell`. A proposed
  parametrization by profiles modulo positive multiples was withdrawn (the reverse inclusion is not established).
- Isotropic saddle energy: the verifier restricted the conclusion to the failure of coercivity in the displayed
  pairing; it does not imply that every isotropic inverse estimate fails.
- Collar coupling (5(i)): the referee audit found our first coupling corollary invalid as stated (it claimed edge
  forcing in `H^{b-3/2}` for `L^2` edge data; jump data refute this); the repaired version adds finite strain, Sobolev
  edge data and a finite-regularity background. The verifier refuted the far-weight endpoint `gamma' = 2` and the
  inference of finite strain from the collar norms, and recorded that some cutoff constants are computed from the same
  derived formula in both interval engines.
- Source cusp (section 4): the verifier refuted our inference from the frozen local regularity at P to membership in
  the global classes `P_2`, `P_3`, and refuted the proposed local source condition by an explicit compact
  counterexample; only the elementary Fourier statements were accepted.
- Corner coupling: our corner splitting assumed a factor of class `C^8` at the origin. The verifier showed that the
  present trial's factor is not even twice differentiable there and that its residual is not in the corner forcing
  space (section 4); we accepted this, and the corner lemma is restricted to centre-regular trials.
- Global flow (5(l)): the verifier refuted our rounding `<= 6.2` of the box-cost bound (the value is
  `5 exp(1111/5000) > 6.244`). The referee audits repaired the flow-box hitting time, the far quotient bound (a case
  split so that mean-value segments stay in the controlled region), and the statement `b+ = 0` on the y-axis (it needs
  `rho(0, y) = 0`; this holds identically for the trial, whose modal representation carries the global factor `x^2 y`,
  and in any realization that imposes this factor; for a general `P_2` profile, whose factorization is required only
  near 0, it needs a separate argument).
- y-axis velocity margin: an intermediate note of ours described `b+` on the y-axis as of the size of the residual;
  the verifier refuted this (it vanishes exactly for the trial, 5(l)).
- y-axis: our first version inferred classical zero jets on the axis from weighted approximation; the referee and the
  verifier refuted this (the verifier with a discontinuous weighted density), and the jets are now defined as
  decomposition coefficients. The referee also required product cutoffs in the localized decomposition.
- Referee review of this report (one model; each item checked by us against the verified proofs). The scalar strain
  bound of section 4 had been transcribed with the constant of `c[h]/3` (too small by the factor 3); it now carries
  the verifier's own constant for `c[h]`, and no other result used it. Further repairs: rounded thresholds replaced by
  exact expressions (`s_fast` is about 3.57855, so `3.5786` was not a safe bound); the variable-coefficient
  obstruction restricted to its window `s_fast < s < b_0` and hypotheses; the Dini condition stated as sufficient, not
  necessary; two sign or tail errors in scaling formulas corrected (`L K = (1 - X.grad) eps~`, `K - (1 - k) t_0`); the
  exit-trace hypotheses (even trace, `H(0) = 0`, regular particular solution) and the strict inequality in the weight
  comparison; the support of the compact source counterexample; the canonical versus normalized coupling in the
  face-dilation obstruction; the hypotheses of the two-norm theorem, of the Schur condition, of the kernel statement
  and of the unnormalized lower bound; the definitions in the `B_3` criterion; the scope of "`P_2` framework" and of
  the family; the centre structure of the trial; a sampled maximum previously called global; and labels and
  definitions.

- Second referee review of this report (sections 5 and 10; one model; each item checked against the verified proofs).
  It found omitted hypotheses and overstatements, now repaired: the supremum norms, rectangle and upper derivative
  order of the source transport bound (the pointwise form is false, explicit example); the global `C^1` and
  Hilbert-domain hypotheses of the variable-coefficient obstruction; separate constants for conormal derivatives of
  the face remainder; the domain and velocity hypotheses of the graph-norm obstruction; the mapping premise behind
  `c_l = 1/k'`; the scaling-domain hypothesis for the variation of `c_l`; the regularity of the independent edge
  component of the collar velocity; the time direction of the flow bound and the sign of the box weights;
  `rho_y(P) != 0` for `mu_P = 1`; the scalar row forcing for the `C^1` endpoint; uniqueness of the y-axis row solution
  in its far space (decay alone does not select it, since the homogeneous solutions decay); the exact y-axis trace
  multipliers (the values quoted earlier are their leading terms); the localization of the saddle monomial; the
  definition of the Wiener norms; and, in section 10, the index-homotopy step, the scope of the family statement and
  of the centre conditions, the reading of the finite-section diagnostics and a symbol clash (`ell_0` for the reduced
  cokernel functional).

- Referee review of sections 1 to 4 and 6 to 9 of this report (one model; each item checked against the verification
  records and the published report). It found a stale numerical comparison (the verified middle-region cell bounds are
  below the historical numerical bounds, not the revised ones), two exterior radii merged in one timeline entry, the
  stationary equation missing from the definition of `P_2`, a misleading introduction to the list of refuted
  proposals, missing artifact identification, an incomplete precision range, missing sampling conventions of the
  floating table (axis samples, grids, radial extent, closure), the localized-forcing audit missing from the open
  objections, resolved corrections listed as open, an overbroad statement about the hypotheses of the two-norm
  theorem, the missing display of `M_Phi(0)`, the elapsed time, and the X3 symbol `x_*` used for the trial's source;
  all are repaired. Its reading of the published inner absolute value as excluding the axis-evaluation floor was not
  adopted: the published report states that its absolute maxima use all evaluation columns.

- Rough coefficients (5(o)): our first note on the completion omitted the origin term of `N_far` and asserted
  continuity of `N_far` on all of `H^s`, and its summary of the local estimate omitted the hypothesis
  `div V = A + mu`. The verifier refuted the continuity assertion with an odd cubic example (mollification creates a
  linear jet at the origin, where the origin term diverges) and identified the divergence hypothesis as used only in
  the explicit budget for E. The repaired statements apply `N_far` only to zero-jet differences and state the
  divergence condition separately.

- Whole-plane Sobolev ball (5(o)): our note stated `delta_h < 0.0165` strictly, which fails at h = 0 (equality); an
  earlier version of its scope also inferred, from a comparison of the residual supremum with the `H^s` radius of the
  narrow statement, that this radius cannot contain a numerical-uncertainty ball. The verifier rejected that inference
  (the two quantities are of different kinds, so the comparison proves neither containment nor non-containment). The
  repaired statement uses `delta_h <= 0.0165` and makes no containment claim.

- Tail repair and affine `L^2` class (section 7; section 10, item 4): the verifier's first draft gave the central
  strain of `x^2 y b(r)` with the wrong sign; a referee review caught it, and the canonical value
  `+(1/4) int_0^infty r b(r) dr` was rederived from the odd kernel and from the Green source (the obstruction does not
  depend on it; the compensator uses the corrected value). A directly iterated interval recurrence for the angular
  quotient lost all precision (width about `2.9e5`) and was replaced by exactly collected integer coefficients; a
  reviewer's claim that the recurrence's unit-modulus roots force such interval growth was refuted, and the repairs
  themselves refute the claim that a correction small in the factor norm must lie in unweighted `L^2`.
- Higher tail repairs (section 10, item 4): a referee review asserted that both new cancellations are necessary, that
  is, that the residual rows of `rho_T` at `r^{3k-2}` and `r^{k-2}` are nonzero, and that every product with the
  `r^{k-2}` row has exponent `2k - 3`. The first was not proved there and is not used in the sufficiency proof; it was
  later proved separately for both rows (section 10, item 4); the second holds only as an upper bound (attained by the
  product with the `r^k` row), which is all the proof uses.
- Printed flow bounds (5(l)): two printed lower bounds of the flow certificate of the numerical computation were not
  implied by their stored aggregates, the outer-axis `V_1/x >= 5.5742` (stored aggregate about 5.5741666) and the
  inner-cell `V_2/y >= 21.30141` (aggregate about 21.3014052). These were inward rounding errors in printed
  statements, not field counterexamples, and the printed bounds have been lowered to `5.5741` and `21.30140`, which
  the stored aggregates imply; the whole-quadrant lower bound `m_0 = 0.98845` is not affected. The flow certificate as
  a whole remains unverified (below).
- Weighted `L^2` tails of the numerical computation (not used in this report): the verifier proved the conditional
  reduction used there, which bounds the squared residual integrals with the weight of `N_in` and `N_ext` (section 6)
  over the inner disc `r <= exp(b_- - 5)` and the exterior `r >= exp(b_+ + 17)` by polar integration of pointwise
  bounds `|eps|/m <= C_i` and `|eps|/m <= C_o (1 + r/L)^{-delta}`, `delta = 1/2 - k`, for the residual eps of the
  stored trial, and recomputed all ten scalars of this application by two interval methods. Two printed endpoints of
  that computation, of the inner tail and of the whole-plane total, are not outward (each lies below both computed
  lower endpoints of its expression), and one displayed sum of printed upper bounds exceeds its printed ceiling (the
  sum of the saved unrounded values does not); the printed ceilings `6.504e-16`, `3.819e-20` and `6.2899e-4` are
  outward for their expressions. These are labelling errors in scalar bounding expressions, not counterexamples to a
  residual bound; the numerical team has since replaced the two endpoints by outward decimal ceilings and the
  displayed sum by a valid one, and the verifier has confirmed this repair in the collected output (all five saved
  upper labels outward and the repaired sum valid, by two interval methods). The pointwise tail bounds, the
  finite-region integrals and their cover, which the reduction assumes, are not verified.
- Local source estimate (5(o)): the independent reconstruction records the circular principal-value form of the raw
  strain in the canonical convention, `c[h] = -h_y(0)/4 - PV (K_s * h)(0)` with `K_s = y (3x^2 - y^2)/(pi r^6)`, and
  the local velocity term `-h e_2/2`, after correcting the coefficient and the sign in its own notes (the sign
  correction was verified separately). With the vanishing jets of h at 0 the local terms drop out and no constant
  changes.
- Closure tests (section 6): our test script described the zero-continuation variant as continuing the density by zero
  beyond the grid. The verifier refuted this description: the variant sets the exterior `rho_x` source of the modal
  inverse to zero, and section 6 uses that description.
- Stored trial at the joins (section 10, next step 1): a numerical-team description stated the scaling identity
  `L K = eps - X.grad eps` for the stored coefficient representation without qualification. The verifier showed that
  this representation is discontinuous across both joins and that its open-region scaling identity contains an
  interface term and a strain term; their sum has not been proved nonzero for the stored density. The verifier also
  refuted the identification of the strain obtained by interval-by-interval Green integration of the source with the
  canonical strain of the stored density, and recorded that the join radii are the exponentials `R_i = e^{t_a}` and
  `R_e = e^{t_b}` of the first and last stored log knots, not separately stored radius parameters. The exactly joined
  trial rho~ is not affected.
- Degree-five density (5(p)): a referee analysis of ours gave the coefficient of the Cartesian quartic `x^3 y - x y^3`
  of the interior stream as `(1/2) int r^{-4} chi dr` (`chi = r^4 eta`). That is the coefficient of the polar harmonic
  `r^4 sin 4 theta`; since `r^4 sin 4 theta = 4 (x^3 y - x y^3)`, the Cartesian coefficient is `2 int r^{-4} chi dr`
  (verifier). A first version of the verifier's proof assumed the background smooth on compact annuli, which is not
  established for the trial; the accepted version assumes only `C^2` density and `C^1` velocity there.
- Forward qualifier (5(q), 5(e)): a first formulation of ours of the thresholds said that every weight with a frozen
  inverse and `b >= 3/2` has `a > 5/2`. The verifier and a referee audit refuted this: at `a = 0`, `b = 3/2` one has
  `delta = 5A/2 > 0`, and the saddle model is invertible there (base inverse norm `2/(5A)`); in `Y_(a,s)` the
  negative-time inverse at `delta_- > 0` gives further examples. The accepted statements concern the weights with
  `delta < 0` or `delta_Y < 0`; in `Y_(a,s)` with `a >= 0` the qualifier is not needed, since there the frozen inverse
  exists exactly when `delta_Y < 0` (5(q)).
- Finite sections (section 10, next step 1): the numerical team reported about 81 percent of the diagnostic energy in
  the sine frequencies 1 and 3 for the smallest derivative-row direction of the larger section. The verifier found
  that the saved profile of that direction gives about 87 percent and that about 81 percent is the share of the
  smallest trapezoid-weighted direction (floating values); section 10 uses the corrected attribution.
- Range inside the strip (5(q)): an ancillary remark in the verification record of the range theorem stated that no
  unweighted `L^2` bound in `xi_z` follows for the Mellin moments. The verifier refuted it: the weighted bound of 5(q)
  implies the unweighted one with the same constant, and that constant is sharp. The remark was not used by the range
  theorem or the inverse estimate and is withdrawn.
- Fit stability (section 6): the numerical team's comparison table describes its interval endpoints as outward, and
  its summary infers a change of actual integral mass at the 5 percent level. The verifier found that 15 of the 24
  endpoints of the displayed radial ranges lie inside the nominal cell ranges (rounded labels), and that the changes,
  about 4.74 percent at most, are changes of upper bounds, which do not establish a change of the actual integrals.
  Section 6 treats the ranges as approximate labels and the changes as changes of bounds.
- Residual at weak weights (5(q)): the first referee review asked for an explicit proof of the annular regularity of
  the velocity used in the shell bounds; the verifier supplied it from the finite radial mode equations (on compact
  annuli the density is `C^6`, so the stream is `C^7` and the velocity `C^6`). A later review misdescribed two details
  of the coefficient computation (a convolution index and the dependence of the leading angular coefficients on the
  normalization scalar); the verifier corrected the descriptions, and the code and the values were unchanged.
- Scaling term (5(q)): a referee review stated the divergence condition of the far-sector integral with the inequality
  reversed while reaching the correct threshold `a <= 1 + k`; the verifier corrected it (the integral of `r^{2k-2a+1}`
  diverges exactly when `2k - 2a + 2 >= 0`), and a further review withdrew it. The verifier also made explicit that
  the vanishing mass and first moments at infinity concern the source `d_x h` of the stream equation, not h itself.
- Centre trace (5(q)): referee reviews displayed two wrong signs in the expansion of `h_delta` (the proof and both
  programs have the positive signs and `J(h_delta) = 1`) and offered a nonzero linear strain as a sublinear velocity;
  the verifier corrected both, and the reviews withdrew them. The verifier also supplied the uniqueness of the
  canonical velocity under sublinear growth (mean-value estimate for the harmonic difference, then parity).
- Centre trace in the graph norm of L (5(q)): referee reviews asserted that the canonical velocity of the trial may
  contain infinitely many angular modes and that two exponent bounds of different strength conflict, called the exact
  degree label of the logarithmic velocity terms loose, asserted without proof that `C_graph(a,s)` diverges as
  `s -> 4`, and called the cubic velocity of the stream `-x^3 y/3` quadratic; the verifier corrected each (the density
  has odd sine frequencies at most 521 and the velocity frequencies at most 523; a stronger bound is consistent with a
  weaker one; a sufficient estimate that degrades at an endpoint gives no lower bound), and the reviews withdrew them.
  The case `s = 4` remains open.
- Quadratic term in the graph norm of L (5(q)): the first version of the proof stated the conclusion on a graph ball
  of positive radius containing `D_cp`, which is impossible for a nonzero linear space; a referee review identified
  this, and the verifier's addendum replaces both occurrences by the intersection of `D_cp` with every graph ball
  about 0 (the argument is unchanged). A later review wrote a lower bound for each sign of `v_n^{+-}`; only the
  maximum is proved, and the review withdrew it.
- Quadratic term under arbitrary finite constraints (5(q)): one referee review evaluated an exponential modulation
  limit with the constant of the sine and cosine limits; a later review withdrew this, and the limits in the proof are
  correct. The packets are supported where their potentials are; the support of a potential can be larger than that of
  its density, and every support statement refers to potentials. The separate referee audit noted that a sentence of
  the proof declaring all maps real linear should restrict this to the constraint maps (Q is quadratic, as the proof
  uses); a wording correction only.
- Quadratic term under regular finite nonlinear constraints (5(q)): a referee review remarked on the absorption of the
  fixed background term in the correction estimate and on the uniformity of the remainder estimate over the kernel of
  the derivative, including indices at which one tangent input vanishes; the verifier answered that `1 + n <= 2 n` and
  that the Frechet remainder is uniform on that kernel, without changing the statement. An optional extension to
  strictly differentiable constraints, suggested in a review, is not part of the result.
Objections open:
- The numerical team's residual arithmetic: coefficient export and import, cancellation allowance in polynomial
  products, Bernstein matrix exactness, outer exponent export, and gradual underflow in a matrix product. For the
  last item the verifier has proved a conditional theorem: the midpoint-radius matrix product encloses the exact
  interval image for inner dimensions 2 to 1024 under explicit hypotheses (binary64 round to nearest, gradual
  underflow, finite arithmetic and a stated summation tree), with an explicit underflow budget; the corresponding
  sums are also enclosing under the stated addition model. The library's actual evaluation model, the power bounds
  and the provenance of older outputs are not proved, so the objection stays open.
- The numerical team's interval-Newton derivative for the source. The independent root enclosure supersedes it.
- Coefficient bounds near the source (5(o)): the first version of the numerical team's fine interval pass reported
  rows for larger discs inconsistent with its reported radial coverage (exact comparisons), selected cells with a
  floating distance filter, and paired two different sub-interval enclosures. A revised version addresses all three
  and reproduces the bounds. The cover of its exported coordinate masks is verified for the `delta = 0.0165` disc; its
  larger-disc rows have explicit missing points. The density and velocity Hessians now have independent verified
  bounds (`M_rho < 0.5059`, `M_V < 0.2972`); the tighter values of the numerical pass and the Green, Taylor and
  Cartesian arithmetic of its pass are not checked.
- The flow certificate of the numerical computation as a whole (5(l)): the exported Green boundary values, the
  exported density polynomial boxes and the radial Taylor models are verified on all middle cells, with their
  canonical meaning, and the canonical flow fields lie in the reported ranges on the nine rectangles (section 4); the
  angular linkage beyond the nine tested rectangles and the full certificate (the angular products, the classification
  of the spatial boxes and the flow inequalities) are not verified.
- Localized forcing near the source (5(o); section 10, item 4): no interval upper bound of `||tau eps~||_{H^{31/10}}`
  or of `N_500(tau eps~)` is verified for the explicit polynomial `C^4` cutoff tau of the local estimate at
  `delta = 0.0165`. The numerical pass computed such bounds in several versions. For the versions below the
  independent audit confirmed the finite components (the geometry boxes, the cutoff entries and the sums of the saved
  per-cell rows, each by two interval methods) and the resulting ceilings, which are conditional on the validity of
  the saved per-cell bounds:
  - first version: 22 of its 36 printed ceilings were below the saved endpoints; the saved aggregates give `5.65330`
    and `8.87175` for the two norms, conditional also on per-cell Hessian bounds that its saved output does not
    contain; replacing those by the stronger saved cutoff bound on `|t''| + |t'|/r` (`tau = t(|X - P|)`) and by the
    bound `9363/1000000` on the Frobenius norm of the Hessian of eps~ throughout the cutoff disc `B_{9 delta/4}(P)`
    implied by its saved second-partial suprema gives `5.94978` and `9.12448`;
  - final version (the cutoff and the residual both as bivariate Taylor models; the per-cell scalar factors and
    remainders saved and the source and output fixed by SHA-256): `1.5700` and `3.5769` (and, at orders 3 and 4,
    `0.7759` and `893.16` at `lambda = 1`, `1.8107` and `1638.56` at `lambda = 500`); the saved data of its preceding
    run gave the same ceilings and received a separate conditional finite audit; the execution of that run is not
    attested. An intermediate version (products of suprema, the cutoff evaluated in centred form) reports `2.1207` and
    `4.2064` and was not audited separately.
  The open hypotheses concern the physical validity of the saved enclosures; for the final version they are: (H0) the
  identification of the saved quantities with the canonical trial's residual and its weak derivatives through order 4
  (odd parity, and the interface regularity that places the localized product in `H^4`); the local regularity of the
  trial checked earlier does not identify these numerical jets; (H1) the saved bounds on `|eps~|`, `|grad eps~|`,
  `|Delta eps~|`, `|grad Delta eps~|` and `|Delta^2 eps~|` on the 26079 rows where `tau = 1`, and these together with
  the Frobenius norm of the Hessian on the 1368 straddling rows; (H2) the five saved bounds on the same quantities for
  `tau eps~` on the 16502 rows of the cutoff transition; each bound must hold throughout its cell and uniformly over
  the source bracket. Separately, the 15 suprema of the partial derivatives of eps~ through order 4 on
  `B_{9 delta/4}(P)` and on `B_{3 delta}(P)` have their own unverified ancestry (the larger disc contains cells that
  are not among the saved rows). The earlier versions rest on the analogous hypotheses for their own saved rows. The
  program that produces these enclosures builds five radial jets of the nonlinear residual from enclosures of the
  density, of the radial stream-function modes (solutions of the modal ODEs) and of the velocity; these jets, their
  angular assembly, the Cartesian conversion, the recentring, the composition with the cutoff, the truncations and the
  conditions on the arithmetic kernels used are not verified; the verifier confirmed only the exact algebraic
  identities underlying the jets and selected source expressions (no numerical path and no physical jet). This report
  does not use these numbers.

## 9. Reproducibility
- Inputs: X3 coefficient file md5 `15f8095f7e79dbfa0c50d75e5fe8997a`; control F3 md5
  `0398af3f08a2a4f75e42c846edbaa375`. Both match the problem statement.
- Trial: its modal coefficient archive has SHA-256 `a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874`,
  and its exact export (binary64 dyadics as exact rationals), used by the verification, has SHA-256
  `57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6`; the exact normalization and joins are those of
  the verified exactification (section 2).
- Environment, single-threaded CPU: the numerical team used python 3.9, numpy 2.0.2, scipy 1.13.1, python-flint 0.6.0
  (Arb) and mpmath 1.3.0; the verifier used python 3.12.13, numpy 2.5.0, python-flint 0.9.0 and mpmath 1.3.0.
- The accompanying artifacts (their README gives the layout and the exact commands) contain:
  - the numerical team's code (reconstruction of X3, the modal trial, the interval certificate pipeline, the X-norm
    ceilings and the floating diagnostics), the trial file and the exactified coefficients, the certificate outputs
    and floating tables, and the numerical team's full report with its replay commands, run times and SHA-256 table;
  - the independent verification: one folder per verified topic with its proof, its adjudication records and its
    independently written code; the evidence outputs of all topics (large per-cell row files excepted, which the
    topic's code regenerates); the exact rational exports of X3 and of the trial; the verifier's own evaluators of
    X3; its reading guide and its chronological record of verdicts;
  - the specification followed by the team (final version, with its revision history);
  - the list of the files in which absolute local paths were rewritten at publication, with their original and
    published SHA-256 hashes (the hashes quoted inside the records refer to the original files).
- Commands: the README of the accompanying artifacts records the commands used to regenerate the trial from the published
  X3 coefficient file (stored files agree byte for byte with a rerun of the fitting program presented by the
  numerical team, as checked by the verifier, who did not rerun the fitting; section 6) and to compute the residual
  tables, the residual and derivative certificates, the X-norm bounds and the verification checks. Each verification
  topic contains its own scripts, its evidence files, and the SHA-256 hashes of its pinned inputs and of its verdict.
  Not published: the X3 coefficient file itself (it is in Changhe Yang's repository, with the Setting I artifacts),
  large regenerable intermediates, raw run logs, and the transcripts of the referee reviews by a second model.
  Full historical verification replay is not available from the published bundle alone: some computational scripts
  also require omitted review records, original source hashes, fresh output locations and the original run deadline.
  The accompanying artifacts provide a separate read-only command checking the saved regional aggregation and
  final rounding; that check does not regenerate the underlying interval bounds.
- Sampled versus certified: floating-point outputs are exploratory evidence and are never used as certified bounds.
- Interval settings: precision is certificate-specific and stated in each record; the recorded computations and audits
  use Arb (python-flint) at up to 4096 bits and mpmath.iv at up to 250 decimal digits; inner and exterior residual
  certificates in 384-bit Arb and 160-digit interval arithmetic; middle region in 384-bit Arb with a 150-digit
  interval audit, and a second middle-region construction in 160-digit interval arithmetic followed by a 220-digit
  scalar scan. Tool names and full environments
  are in the individual record of each certificate in the accompanying artifacts.

## 10. Ranked obstructions and next steps (if UNRESOLVED)
Method-specific failures (none of these implies nonexistence):
1. Global linear inverse. No Fredholm realization of L is known; in X no closed realization containing the sequence of
   5(p) is Fredholm, and in the space `B_F` of the weighted factor supremum norm of 5(r) no closed linear realization
   containing its sequence is Fredholm.
   - Isotropic Sobolev energy estimates fail at the saddle (indefinite energy symbol, verified); an isotropic inverse
     is not excluded by this alone.
   - In the diagnostic weighted `H^1`-type norm X of next step 1 the centre weight `r^{-6}` makes degree-two densities
     scale-critical, the frozen centre saddle `A_c X.grad - 1`, `A_c = DV(0)`, has a degree-two homogeneous solution
     with angular factor in `H^1` of the circle, and long logarithmic annuli give quasimodes of L with `J = c = 0`
     (verified, 5(p)). So no inverse estimate with X on both sides holds on a domain containing the sequence of 5(p),
     not even with an `H^{5/2}` or compact remainder, and no closed realization in X containing it is Fredholm; a
     realization with a lower bound or with the Fredholm property must use norms or a domain for which this sequence
     is no longer an obstruction; raising the power of the centre weight in this first-order norm does not suffice
     (norms `X_m` of 5(p)). 5(p) concerns these norms only; it does not exclude a bounded right inverse, or a solution
     operator from a stronger forcing space into X.
   - Weighted factor supremum (verified, 5(r)). In the factor norm of the axis control of section 4, on the space
     `B_F` of continuous factors vanishing at 0 and at infinity, slowly varying logarithmic annuli at the centre with
     an exact strain correction give unit weak-null quasimodes of L with `J = c = 0`, so no inverse estimate with this
     norm on both sides holds on a domain containing them, not even with a bounded linear compact remainder, and no
     closed linear realization in `B_F` containing them is Fredholm. Together with the failure of this norm to control
     the interior velocity (section 4), a realization with a lower bound or with the Fredholm property must use other
     norms (for example Hoelder or derivative norms of the factor, which 5(r) does not cover) or a domain that
     excludes the sequence.
   - Axis weights (verified, 5(q)). In the logarithmic norms `Y_(a,s)`, which for `a > 0` are singular along the whole
     y-axis, the frozen centre transport is invertible for `a >= 0` exactly when `delta_Y < 0` (at
     `(a, s) = (6, 153/50)` with inverse norm about 0.4353; for `s >= 3/2` all such weights have `a > 5/2`), but for
     `a >= 5/2` the full L does not map every smooth compact density with `J = c = 0` supported away from both axes
     into `Y_(a,s)`, and for those supported in `1 < r < 2` and `0 <= s < 7/2` membership of the image is equivalent
     to the vanishing of every interior even harmonic moment; the trial's residual lies in none of these spaces with
     `a >= 5/2`, and for `s = 153/50` and `a >= 0` it lies in `Y_(a,s)` exactly when `2k < a < 5/2` (qualitatively,
     without a norm bound, 5(q)), the strain functional c is bounded on `Y_(a,153/50)`, `a >= 0`, exactly when
     `a < 2`, the trial and `X.grad rho~` lie in `Y_(a,153/50)`, `a >= 0`, exactly when `1 + k < a < 5/2`, and the
     scaling term `(c[h]/3) X.grad rho~` of L is bounded there exactly when `1 + k < a < 2`, then of rank one and
     compact (5(q)). A realization in `Y_(a,s)` with `a >= 5/2` therefore needs a domain that carries these nonlocal
     compatibility conditions, or other weights, and for `s = 153/50` and every real a the domain of a closed linear
     realization cannot contain the maximal domain of `T_0` (compact densities with compact velocities near the source
     have bounded frozen graph norm and images of unbounded norm, 5(q)), so, where the frozen inverse exists, it does
     not pass to L by a `T_0`-bounded or `T_0`-compact perturbation on `Dom(T_0)`; for every real `a < 5/2` and finite
     `s >= 0` the centre trace J is not closable on the smooth compact densities with `c[h] = 0` and smooth even-even
     factor `h/(x^2 y)`, in `Y_(a,s)` or in the frozen graph norm, and for `0 <= s < 4` in the graph norm of L on
     those with `L h` in `Y_(a,s)`, so the centre normalization is not a closed constraint in these topologies (5(q));
     for `0 <= a <= a_Y(s)`, `T_0` from its maximal domain to `Y_(a,s)` is not Fredholm, and for `0 <= a < a_Y(s)` its
     closed range is cut out by one Mellin moment condition for almost every `xi_z` and each sign of `xi_y` (5(q));
     for `0 <= a < 5/2` and `0 <= s < 6 - a` every smooth compact density of the required parities with `c[h] = 0`,
     supported away from both axes, is mapped into `Y_(a,s)` (setwise, without a uniform bound, 5(q)), and at
     `s = 153/50` those with `c[h] != 0` exactly when also `a > 1 + k` (5(q)); so for `1 + k < a < 2` and `s = 153/50`
     the residual, the trial and `X.grad rho~` lie in the space, c is bounded, the scaling term is compact of rank one
     and every smooth compact density of the required parities supported away from both axes is mapped into the space,
     while `T_0` is not Fredholm there, the frozen graph domain obstruction applies, the centre normalization is not
     closed in the graph norm of L on linear domains containing the test densities of 5(q), and Q is not continuous at
     0 from the graph norm on `D_cp` of 5(q) into `Y_(a,s)`; whether L has a bounded inverse on a domain not
     containing `Dom(T_0)` is open.
   - Above threshold, at the source, the frozen cokernel is infinite (5(b)); for `s_fast < s < b_0` and under the
     hypotheses of 5(d) the variable-coefficient operator is not Fredholm in ordinary `H^s` graph form.
   - Below threshold, at the orders `b_0/A < s < s_fast`, the indices cannot be computed by the straight homotopy from
     pure transport (threshold crossing, section 5).
   - The weighted saddle model (5(e)), the face velocity splitting (5(f)), the collar coupling (5(i)) and the y-axis
     structure (5(j)) are verified local pieces of a candidate realization; in the quadrant norms of 5(e) with
     `a >= 5/2`, which include its revised working point and, for `b >= 3/2`, every weight with `delta < 0`, the full
     L maps the density of the mapping obstruction of 5(q) outside the space, so a realization of L in these norms
     must use a domain that excludes this density (5(e)); the trial's residual is not in these spaces either (5(q)).
     They do not yet assemble into a global estimate: the corner coupling, the y-axis near/far bounds, the conic
     region at large r, and the source-to-outer matching with its quantitative transition estimates are missing (the
     local source estimate itself is instantiated for the trial, 5(o)).
   - Coupling term (verified under stated global hypotheses, with its own proof; first derived in a referee audit;
     also checked by separate referee reviews). With `a = rho~_x`, `c = rho~_y` and the Riesz transforms `R_i` with
     the real symbols `xi_i/|xi|` (self-adjoint convention), the coupling `T v = U[v].grad rho~` has the form
     `T = b - S + sum_{i,j} [R_i, B_ij] R_j` with `S = sum_{i,j} R_i B_ij R_j` and `B = [[b + c, -a/2], [-a/2, b]]`,
     for real bounded coefficients and any real majorant `b >= (|grad rho~| - rho~_y)/2` on the whole plane (so that B
     is positive semidefinite everywhere and `S >= 0`) with finite Wiener norms
     (`W_r(f) = (2 pi)^{-1} int <p>^r |f_0^(p)| dp` for `f = f_inf + f_0` with `f_inf` constant, unitary Fourier
     transform); hence `Re <T v, v> <= <b v, v> + C ||v||_{L^2} ||v||_{H^{-1}}` with
     `C = 2 (W_1(b + c) + W_1(a) + W_1(b))`, together with first and second commutator bounds, a fractional
     conjugation estimate at order s and a localized form at the source. Near P the source box of 5(o) also has an
     unused directional margin (frozen rate at most `-1687/500 - (449/1000) n_1^2`). Open: the actual Wiener constants
     of the trial's coefficients, a global positive extension of the coefficient, weighted fractional errors, the axis
     jets, the far block and invertibility. No source constant is improved by it and no endpoint follows.
   - Outer estimate with a source cutoff (verified conditional statements, with their own proofs; first derived in a
     referee audit; also checked by separate referee reviews). If `V(P) = 0`, `DV(P)` is symmetric with smallest
     eigenvalue `mu_P` and `||DV - DV(P)||_op <= mu_P/2` on `B_delta(P)`, every nondecreasing radial cutoff `zeta_P`
     vanishing on `B_{delta/2}(P)` and equal to 1 outside `B_delta(P)` has `V.grad zeta_P >= 0`, so the cutoff term of
     the weighted transport identity has the favourable sign (for the trial the perturbation part is below `0.0148` on
     `B_{0.0495}(P)` by the Hessian bound of 5(o), and the base-point hypotheses hold for the trial, 5(o)). The
     coupling does not preserve the remainder block at the x-axis (an explicit jet projection is needed). A compactly
     supported correction with nonzero strain has `L h` outside the far forcing space for every admissible far
     exponent; its far response is `-(c[h]/(3 c_l^2)) r^k log r Theta` (raw c), which the proposal of next step 2
     carries as a separate unknown. The raw strain is bounded by the weighted `L^2` norm of the remainder, with
     constant below `0.0078149` at the working parameters (`a = 6.25`, `gamma' = 1.129`, `L_w = 0.5`, escape weight
     `e^phi` with `inf phi = 0`), when `h(0) = 0` and `h_y(0) = 0`. In the specified logarithmic-coordinate model
     spaces the embedding of the remainder space into the lower-order space is not compact; this transfers to the
     proposed realization only through norm comparisons that are open, so a compact-remainder Fredholm argument needs
     a separate justification (for example a low-norm estimate or a parametrix). Open: the actual escape weight, the
     weighted and conormal fractional norms, the parametrix and the assembly.
   - Dynamic rescaling (verified abstract implication, with its own proof; also checked by separate referee reviews).
     Let L generate a `C_0` semigroup S on a Banach space, let N be a closed subspace of finite codimension such that
     L maps the intersection of `D(L)` and N into N, let Q be a bounded projection onto N, and assume
     `||S(t)Q|| <= K e^{-lambda t}` with `lambda > 0`. Then the part of L in N (with domain the intersection of `D(L)`
     and N) is a bijection onto N, with inverse `f -> -int_0^infty S(t) f dt` (strong integral) of norm at most
     `K/lambda`. So a dynamic-rescaling route based on exponential decay of the realized linearized semigroup, after
     finitely many modulation directions are removed, supplies the stationary inverse on the same space and domain,
     and it must prove that decay bound, which is in general stronger than invertibility (`L = 1` is invertible and
     generates growth). This is not a statement that every dynamic method needs exponential decay. No IPM space,
     generator, domain, modulation complement or decay bound is supplied.
2. Source regularity window.
   - At P an ordinary Sobolev realization of order `s_fast < s < b_0` (`s_fast` about 3.57855) is excluded under the
     hypotheses of 5(d), and no finite border bounded into `H^s` repairs that; orders `s >= b_0` are not covered by
     that theorem, while the frozen model has infinite cokernel for every `s > s_fast`.
   - The near resonance `mu~ - 1 = -2.25e-8` is not an obstruction for the coupled frozen operator (5(c)). It costs
     `1/|mu~ - 1|` only in formulations that split off the transport jet equation.
3. Nonlinear closure in a single space. In a transport graph norm satisfying the domain and velocity hypotheses of
   5(g) the quadratic term is not continuous into the same target; those hypotheses have not been verified for the
   proposed realization. The tested transport graph formulation does not support the required direct quadratic
   estimate; the proposal here uses the two-norm theorem of section 7, and other formulations would need their own
   nonlinear mapping estimates. In the diagnostic weighted `H^1`-type norm alone the quadratic term is not continuous
   at 0, even on compact densities with `J = c = 0`, and the same holds in its graph norm `||h||_X + ||L h||_X` at any
   background satisfying the hypotheses of next step 1 whose transport field V is locally `C^1` and vanishes at a
   point `(p, 0)`, `p > 4`, in particular at the exactly normalized modal trial (next step 1 below). In the
   logarithmic norms `Y_(a,s)` of 5(q), for every real a and finite `s >= 0`, the quadratic term is not continuous at
   0 from the graph norm of L at the exactly joined trial into `Y_(a,s)`, already on the compact-potential class
   `D_cp` of 5(q), where `J = c = 0`, after any finitely many linear constraints, continuous or not, and on the zero
   set near 0 of finitely many constraints that vanish at 0 and are continuously Frechet differentiable in the graph
   norm with onto derivative at 0; this includes the window `1 + k < a < 2` at `s = 153/50`. These three quadratic
   obstructions concern the diagnostic X-to-X estimate, the specified graph-to-X estimate and the graph-to-Y estimate.
   Stronger domain norms, the norms of the proposed realization, weaker image norms, scales of spaces and specified
   finite-dimensional classes are not covered.
4. Residual certification. The certified residual norm still needs:
   - verification of the coefficient inputs used for the chosen derivative forcing computation, including any required
     composition with the validated archive;
   - certification of every region in the chosen derivative forcing norm (in the diagnostic X norm a direct
     whole-plane bound, sharpest `||eps~||_X < 1.49546805188731021373656` and `||L K||_X < 2464.68293019825564964515`,
     is verified but coarse; the earlier zeroth-order inner and exterior certificates of section 6 cover only the
     quantities stated there, while the X norms on the two radial end regions outside E are verified; the numerical
     team's physical derivative bounds quoted there remain unverified: the finite arithmetic on their saved values,
     the conditional polar-to-Cartesian implication and the 63 saved majorants of three middle cells (with verified
     canonical inputs) have been checked, and their saved inner and outer cells, read literally, leave 1968 open gaps
     of total length about `1.1e-12` in `log r`, while the coherent cells intended by the producer cover about
     `5.155e-5 <= r <= 8.244e10`, so that valid majorants on these cells would give `||eps~||_{X(E)} < 0.385656` and
     `||L K||_{X(E)} < 585.874` on E and, with the verified end regions, `||eps~||_X < 0.385656000027` and
     `||L K||_X < 585.874000000002` on the whole plane, and the regularity premise of section 6 is verified for the
     exactly joined trial; section 6);
   - a centre-regular trial: the present trial's residual is not in the corner product-weight forcing space at all
     (section 4), so no finite `eta` exists there for it;
   - an axis-compatible trial for the axis-weighted norms: the present trial's residual has
     `eps~_xx(0, y)/2 = Q y^3 + o(y^3)` on the y-axis with `Q > 0` and for `a >= 5/2` lies in no `Y_(a,s)` and in no
     quadrant norm of 5(e) (5(q)), so no finite `eta` exists in these norms for it;
   - a far tail compatible with an unweighted forcing space: the present trial's residual is `r^{2k-1}` times a
     nonzero angular profile at infinity and is not in `L^2(R^2)` (section 2). Verified construction (section 3, entry
     05:53; own proof, two interval engines and an exact output audit): for every `T >= max(R_b, L, 1)` the explicit
     profile `rho_T = rho~ + chi(r/T) r^{2k-1} H(theta) - lambda_T x^2 y b(r/T)`, with `H = k Eps/(1 - k)` (Eps of
     section 2), `b(s) = (s - 1)^8 (2 - s)^8` on `(1, 2)` and zero elsewhere, chi the normalized primitive of b, and
     `lambda_T` the exact multiple for which the raw central strain is unchanged, coincides with the trial on `r <= T`
     as a density (its velocity changes there), keeps the parities, `a(0) = 1`, `c_l = 1/k` and
     `3 c_l - 1 - c[rho_T] = 0` exactly, satisfies the kinematic requirements of `P_2` (stationarity is not claimed),
     has residual `eps_T = F(rho_T, 1/k)` in `L^2(R^2)` (no certified numerical estimate of its `L^2` norm at a finite
     T is supplied; the norm grows with T, see below), differs from the trial by a function that is not in `L^2(R^2)`,
     and has factor distance `sup |(rho_T - rho~)/(x^2 y (1 + r^2/L^2)^{(k-3)/2})| < 0.334616 T^{k-1}` (the quotient
     extended continuously to the axes; for example below `9.109e-8` at `T = 10^8`). A second verified construction
     (section 3, entry 06:04; own proof, two independent readings of the original binary64 coefficient data, exact
     nonresonance and identity checks, and an independent output audit) adds, with the same cutoff, the counterterms
     `chi(r/T) r^{3k-2} H_2(theta)` and `chi(r/T) r^{k-2} H_d(theta)`, where `H_2` and `H_d` are finite odd sine
     polynomials given by exact finite formulas in the trial's far coefficients (`H_d` removes the trial's own
     `r^{k-2}` density row), and replaces `lambda_T` by the exact multiple that again leaves the raw central strain
     unchanged. The resulting `rho'_T` has all the properties just listed for `rho_T` except the factor-distance
     constant, differs from `rho_T` by a function in `L^2(R^2)`, and for each fixed T its residual
     `eps'_T = F(rho'_T, 1/k)` satisfies `eps'_T = O(r^{4k-3} (1 + log r)^{12})` at infinity, with `4k - 3 < -2`
     because `k < 1/4`. Hence `r eps'_T` is in `L^2(R^2)` and
     `||eps'_T||_{dot H^{-1}} <= ||r eps'_T||_{L^2} < infinity`, where `||f||_{dot H^{-1}}` is the supremum of
     `|<f, phi>|` over `phi` in `C_c^infty(R^2)` with `||grad phi||_{L^2} <= 1`; the bound uses the zero mean of
     `eps'_T` on every circle (from the parities): with `Pi_T` the zero-mean angular primitive of `eps'_T`, the
     tangential field `r Pi_T e_theta` lies in `L^2(R^2)`, has divergence `eps'_T` and norm at most
     `||r eps'_T||_{L^2}`. No numerical estimate of either norm at a finite T is supplied. Its factor distance from
     the trial is at most `C_1 T^{k-1} + C_2 T^{2k-2} + C_d T^{-2}` with constants independent of T, `C_1 < 0.334616`,
     `C_2 < 947.4716170719` and `C_d < 11225.91941797` (verified, section 3, entry 07:19;
     `C_i = L^{k-3} (2^{(3-k)/2} N_i + 2^{-14} 5^{(3-k)/2} |I_i| / ((1 - a_i) J_b))`, `J_b = 1/145860`, where `a_i` is
     the exponent of the counterterm row `H_i`, `I_i` its `sin(3 theta)` coefficient and `N_i` the sum of the absolute
     cosine coefficients of `H_i / (cos^2 theta sin theta)`; `N_2` and `N_d` are below `108584.7279010` and
     `1155559.679346`), so it tends to zero as `T -> infinity`; for example it is below `5.448e-4` at `T = 10^4`,
     `4.134e-6` at `T = 10^6` and `9.116e-8` at `T = 10^8` (upper bounds, not computed distances). The residual norms
     grow (verified, section 3, entry 06:32): for either `eps = eps_T` or `eps = eps'_T`,
     `liminf_{T -> infinity} T^{-2k} ||eps||` exceeds `0.03135338258` in `L^2(R^2)` and in `H^{-1}(R^2)`, and
     `liminf_{T -> infinity} T^{-2k-1} ||eps'_T||_{dot H^{-1}}` exceeds `0.0022215507882`, hence so does
     `liminf_{T -> infinity} T^{-2k-1} ||r eps'_T||_{L^2}` by the bound
     `||eps'_T||_{dot H^{-1}} <= ||r eps'_T||_{L^2}` above (verified, section 3, entry 06:39) (asymptotic statements;
     no T from which they hold is certified). The reason is that on `T/2 < r < 3T/4` the density is the trial's and
     the added velocity is `O(T^{2k-1})`, so the residual there equals the trial's `r^{2k-1} Eps(theta)` up to
     `o(T^{2k-1})`. So the factor distance to the trial tends to zero while these residual norms tend to infinity, and
     in particular both constructions are non-stationary for all sufficiently large T. Near the origin and the source
     the repairs change the trial only through the velocity (verified, section 3, entry 07:19): the exact raw-strain
     compensation removes the quadratic interior stream term of the correction, so for `rho_T` and `2R <= T` every
     component of `U[rho_T - rho~]` and of its Cartesian derivatives of order `j <= 3` is bounded on `|X| <= R` by
     `Gamma_j R^{3-j} T^{2k-4}` with `Gamma_0 < 56.22`, `Gamma_1 < 206.2`, `Gamma_2 < 649.6`, `Gamma_3 < 2048.7`; on
     `|X| <= 9`, which contains P, and for `T >= R_b > 3412` the velocity and its first derivatives change by less
     than `1e-8`. Sharper: `rho_T - rho~` is exactly the first compensated row of `rho'_T - rho~` below (same profile
     `H_1 = H`, cutoff, exponent and compensator), and the first-row case of the finite-mode estimate below bounds
     these components on `|X| <= 9` by `1.523891e-12`, `5.139245e-13`, `1.184002e-13` and `1.590300e-14` for
     `j = 0, 1, 2, 3`, for every admissible T (verified, section 3, entry 08:14). The four-jet identity of section 7
     (here `z = v = 0`, since `rho_T = rho~` near P, and the raw strain is unchanged) then gives
     `|partial_y F(rho_T, 1/k)(P)| > 6.7015e-7` for every admissible T, so these repairs leave the trial's source
     defect in place. For `rho'_T`, with `u'_T = U[rho'_T - rho~]`, the finite-mode estimate applied to each of its
     three exactly strain-compensated rows, with the `sin(5 theta)` coefficient `h_{i,2}` of each row `H_i` separated
     (verified, section 3, entries 07:19 and 07:33), bounds the absolute value of every individual component of `u'_T`
     and of its Cartesian partial derivatives of order `j <= 3` on `|X| <= R`, `2R <= T`, by
     `R^{3-j} sum_i T^{a_i - 3} (2 (3)_j |h_{i,2}| / (3 - a_i) + (N_i / 2) m(a_i) (R/T)^2 Z_j)`, where i runs over
     `1, 2, d`, `H_1 = H`, `a_1 = 2k - 1`, `a_2 = 3k - 2`, `a_d = k - 2`, `(3)_j = 1, 3, 6, 6`,
     `m(a) = max(1/2, 2/(3 - a))`, `Z_j = 4/3, 68/9, 1016/27, 4600/27`, `N_i` is defined as above
     (`N_1 < 38.37961982`), and `h_{1,2}`, `h_{2,2}`, `h_{d,2}` are about `0.01721`, `-6.108` and `-1492.8`
     (explanatory approximations; the evaluation uses the certified coefficient and norm enclosures). These bounds
     decrease in T; evaluated at `R = 9` and `T = 3000 < R_b` they show that for every admissible T these components
     are below `1.006144e-11`, `3.394241e-12`, `7.827257e-13` and `1.056035e-13` on `|X| <= 9` for `j = 0, 1, 2, 3`,
     so `|partial_y F(rho'_T, 1/k)(P)| > 6.6989e-7` for every admissible T. The velocity change tends to zero in `C^3`
     on each compact set at rate `O(T^{2k-4})`, and the residual converges there in `C^2` to the trial's. These
     counterterms are sufficient, and both are necessary in the following sense (verified, section 3, entries 07:03
     and 07:19). For every T the coefficients of `r^{3k-2} sin(theta)` and of `r^{k-2} sin(theta)` in the expansion at
     infinity of the residual of `rho_T` are T-independent numbers `C_{2,0}` and `L_d` with
     `-2734.192205182 < C_{2,0} < -2734.192205181` and `184130.68809691 < L_d < 184130.68809692` (each from two
     interval engines with an exact audit of the input data; these coefficient enclosures alone supply no certified
     numerical lower bound for the full residual at a specified finite radius). `C_{2,0}` is `-(2(1 - k)/k)` times the
     `sin(theta)` coefficient of the trial's `r^{3k-2}` density row plus the frequency-one coefficient of the two
     quadratic products of the `r^k` and `r^{2k-1}` rows of `rho_T` (velocity of one against the gradient of the
     other), the only products with exponent `3k - 2`. No quadratic term has exponent `k - 2`, so
     `L_d = -(2/k) R_b^{5-k} b_d`, where `b_d` is the `sin(theta)` coefficient of the trial's stored `r^{k-2}` density
     row in the normalization of section 2, an exact rational
     (`b_d = -6077384870622209/39614081257132168796771975168`, about `-1.534e-13`; `R_b^{5-k}` is about `1.076e17`).
     In both rows the decaying homogeneous velocities, the compensator and the remainder contribute only other powers.
     Consequently, for every T, the residual of `rho_T` is not in `dot H^{-1}(R^2)` and `r eps_T` is not in
     `L^2(R^2)`, although `eps_T` is in `L^2(R^2)` and `H^{-1}(R^2)`: with `phi_S(X) = g(|X|/S) sin(arg X)`, g a
     nonnegative nonzero smooth bump supported in `(1, 2)`, `||grad phi_S||_{L^2}` does not depend on S, while
     `<eps_T, phi_S> = pi C_{2,0} S^{3k} int_1^2 g(s) s^{3k-1} ds + pi L_d S^k int_1^2 g(s) s^{k-1} ds + o(1)`, which
     is unbounded (either coefficient alone would suffice). Within the class of densities rho (residual
     `eps = F(rho, 1/k)`) whose part at infinity is a finite sum of rows at `r^k`, `r^{2k-1}`, `r^{3k-2}` and
     `r^{k-2}` (finite sine polynomials) and terms of order at most `r^{4k-3}` (finitely many powers, finite
     logarithmic degree, expansions that may be differentiated), with the same canonical law and `c_l = 1/k`, and
     whose `r^k` and `r^{2k-1}` rows are those of `rho'_T`, the condition `r eps in L^2(R^2)` forces the `r^{3k-2}`
     density row to be that of `rho'_T` and the `r^{k-2}` density row to vanish, as it does in `rho'_T`: a nonzero
     residual row at `r^{3k-2}` or at `r^{k-2}` makes `r eps` fail to be square integrable
     (`2(3k - 2) + 3 = 6k - 1 > -1` and `2(k - 2) + 3 = 2k - 1 > -1`) and the lower terms cannot cancel it, and the
     residual row at `r^{k-2}` is `-(2/k)` times the density row there. So `H_2` and `H_d` are necessary in that
     class; the `sin(theta)` coefficient of `H_2` is `k C_{2,0}/(2(1 - k))`, in `(-298.795137988, -298.795137987)`,
     and `H_d` is minus the trial's `r^{k-2}` row. For both constructions the leading far profile `r^k Theta_M` is
     that of the trial, so the leading-tail separation from X3 of section 2 is unchanged (`X3 - rho_T` and
     `X3 - rho'_T` lie in `L^2(R^2, <r>^{-2 beta} dX)` exactly for `beta > 1 + k`, while `rho_T - rho~` and
     `rho'_T - rho~` do exactly for `beta > 2k`; verified, section 3, entry 06:32), and the scaling source
     `X.grad rho'_T`, with leading term `k r^k Theta_M`, is not in `dot H^{-1}(R^2)` (the annular tests
     `eta(|X|/R) Theta_M(arg X)`, eta a fixed nonnegative, nonzero function in `C_c^infty((1, 2))`, have gradient norm
     independent of R and pairings of exact order `R^{k+2}`). What remains is a quantitative bound of such a residual
     in a forcing norm for which a linear inverse is available;
   - a trial whose residual is small in the forcing norm at P. For membership in `C^{2,alpha}` through Sobolev
     embedding in the plane, `H^s` with `s > 3 + alpha` on a disc around P suffices. Floating point (numerical team,
     not reproduced): on the disc of radius 0.5 the present trial's residual has `H^3` norm about 0.89, `H^{3.06}`
     norm about 1.21 and `H^{3.1}` norm about 1.48, although its supremum there is about `1.1e-5`. Localized to the
     source estimate of 5(o), `||tau eps~||_{H^{3.1}}` is about 1.56, 1.07, 0.81 and 1.37 for
     `delta = 0.0165, 0.05, 0.1, 0.2` (floating point, numerical team), so with `1/3.374 <= K_1 < 0.3181` (5(o); the
     upper bound is verified; the lower bound follows algebraically from `K_1 = 1/(kappa - E)`, `kappa = 1687/500` and
     `0 <= E < kappa`) the forcing term `K_1 ||tau eps~||_{H^{3.1}}` of the local upper estimate is about 0.46 to 0.50
     at `delta = 0.0165`; no correction norm has been computed or bounded below. On the disc of radius 0.5 the
     numerical team suggests structure at the knot scale (spacing 0.0165 in r) as the explanation of the size; there
     the product of the disc cutoff with a degree-5 least-squares polynomial fitted to the residual has `H^{3.1}` norm
     about 0.014, against 1.45 for the whole, which shows that this polynomial part is small but does not by itself
     identify the scale of the rest. For the localized norm a separate floating diagnostic (at `delta = 0.0165`
     reproduced by the numerical team with a second code, which gives 1.552, 1.559, 0.614 and 0.0288 for the four
     norms quoted below; grids `256^2` and `512^2` agree for this norm to 0.5 percent at `delta = 0.0165`; the values
     at the other two scales and for the `C^4` step come from one code) is consistent with a substantial contribution
     from the localization, the cutoff acting on the values of the residual; it does not determine how much comes from
     derivatives of the cutoff, from variation of the residual, or from their interaction. At
     `delta = 0.0165, 0.033, 0.066` it gives `||tau eps~||_{H^{3.1}}` about 1.56, 1.67 and 0.87, in each case 0.61 to
     0.65 times `||tau||_{H^{3.1}} sup |tau eps~|` (`||tau||_{H^{3.1}}` about `7.7e6`, `1.8e6`, `4.2e5`;
     `sup |tau eps~|` about `3.3e-7`, `1.4e-6`, `3.2e-6`); a `C^4` polynomial step of the same geometry gives 1.33,
     1.42, 0.79 (ratios 0.62 to 0.70). At `delta = 0.0165` the product of tau with a degree-5 least-squares polynomial
     fitted to eps~ on the support of tau has about the same norm (1.56; the remainder of the fit alone gives 0.61),
     77 percent of the `H^{3.1}` energy of `tau eps~` lies at `|xi| > 1000`, and eps~ under a Gaussian window of width
     0.01 (not an admissible cutoff for 5(o), and with a different spatial weighting) has `H^{3.1}` norm about 0.029.
     In these runs the localized norm stays of order 1 when delta changes, while `||tau||_{H^{3.1}}` decreases and
     `sup |tau eps~|` increases. For cutoffs of these shapes this suggests (not a proved statement) that a smaller
     localized forcing at P may need a residual that is smaller in value near P, not only one with less structure at
     the knot scale. In the numerical team's smoothing experiments, projections onto coarser knots raise the supremum
     to `1e-3` to `1e-1`, and Gauss-Newton re-solves in the coarser spline spaces do not recover it. Linearized
     re-solves on the trial's own knots near P lower the weighted residual (the peak over r of the sum over angular
     modes of the residual amplitudes, near `r = 8.8`) by 3-4 percent and a proxy for its third derivatives (third
     derivative in `t = log r` plus an angular proxy) by at most 13 percent, even when a smoothness penalty dominates.
     A refit on half the knot spacing with one Gauss-Newton step on 40 modes lowers the weighted residual peak by 13
     percent and raises the disc `H^3` norm from about 1.0 to about 4.9 (all floating point, numerical team, not
     reproduced). All these re-solves corrected the trial only on a band of radii around P. In the frozen source model
     the nonstationary characteristics leave a bounded neighbourhood of the source; for the trial's open-quadrant
     trajectories the corresponding global statement is conditional on the finite-annulus flow hypotheses of 5(l).
     Heuristically (transport part only), a correction that vanishes at the band exit is determined along each
     characteristic by the residual and need not have the `C^{2,alpha}` regularity at P required in 5(o), so a
     correction supported in the band cannot in general cancel a transport residual. These experiments therefore do
     not show that the trial is converged on its knots, and they do not locate the accuracy limit of its spline space.
     These floating values give no basis for a closing inequality with the present trial in such a norm. The candidate
     routes are a global re-solve in the trial's own spline space, a fit with a finer knot scale in the same branch,
     or a representation whose residual is smooth near P and small there in value and in its low derivatives.
   - Size of the gap (an illustration; floating point and nominal; not a bound). The bound `e^{C/2}/kappa` of 5(l) is
     proved only for the inverse of the pure transport part in a weighted `L^2` norm. With `kappa = 0.1` and the
     floating orbit costs at order 3.1 for a conic weight with `a = 6.25` (7.07 for the phase-space (bicharacteristic)
     form, 7.41 for the pointwise form) it equals 343 to 407. Used as a stand-in for `K_H`, the condition
     `K_L C_B K_H eta < 1` would need `eta` below `2.46e-3/(K_L C_B)` to `2.92e-3/(K_L C_B)`. This is a budget for one
     sufficient condition: it is not a bound on the coupled high inverse, it is not a necessary condition, and since
     it concerns the pure transport part only it is not a plausible budget for an assembled high inverse (next
     bullet). The localized unweighted norms above have not been compared with the global forcing norm; a numerical
     closing threshold needs a common realization and explicit comparisons between these norms.
   - Size of the auxiliary inverse bound at P. Certified (5(o), explicit auxiliary inverse bound): for one explicit
     `C^4` cutoff at `delta = 0.0165` the bound in `H^s` is below `1.2e35`, obtained from coarse derivative bounds on
     the disc. Through the isotropic dilation the same cutoff and derivative bounds give, also certified (5(o)),
     `R_ell < 679.382` at `ell = delta`, `R_ell < 48.225` at `ell = 7/2000` and `R_ell < 29.812` at `ell = 1/500` for
     `s = 31/10`, an inverse bound below 473 in `N_500` at `s = 31/10` (below 922 for every s in `[61/20, 31/10]`) and
     below `6.968e10` in `H^{31/10}` (at `ell = 11/4000`). The floating values below are for a different, smooth
     cutoff and are not term-by-term comparable with these. Floating point (not certified; evaluator of the trial and
     FFT on grids around P, with a smooth cutoff; at `delta = 0.0165` two resolutions agree to three or four digits,
     and the other rows use at least as many grid points per delta; at `delta = 0.0165` the values for the first
     cutoff shape, including the scaled ones at `ell = 1`, `delta`, `0.01`, `0.005`, `0.0035`, `0.0025` and `0.0015`
     below, are reproduced to the printed digits by a second code with its own field evaluation and FFT): for the
     trial, the constant `R = T_s(w) + sum_i P_s(q_i)` of the auxiliary inverse of 5(o) is about `4.4e4` at
     `delta = 0.0165` (`3.6e4` for a second cutoff shape), `2.2e4` at `delta = 0.033` and `1.3e4` at `delta = 0.066`
     (these two rows use discs larger than the one on which the coefficient bounds of 5(o) are certified; they are
     exploratory and are not trial instances of the theorem); it is dominated by the `H^{31/10}` norms of the cut-off
     density coefficient q, which scale roughly like `delta^{-1.1}`. With d about 3.26 to 3.44 the bound
     `(1 + R/d)^s/(kappa - E)` in `H^{31/10}` is about `2e12`, `2e11` and `4e10`, whereas `K_1 = 1/(kappa - E)` is
     about 0.30 to 0.33 (actual E about 0.07 to 0.33). Much of this size reflects the scale of the norm. The dilation
     `Y = (X - P)/ell` conjugates the auxiliary operator to one of the same form with coefficients `w(P + ell Y)/ell`
     and `q(P + ell Y)` (M and U are Fourier multipliers homogeneous of degree 0) and the same E and d, so the theorem
     of 5(o), applied to the conjugated operator, bounds the inverse in the norm
     `N_{1/ell}(u) = (int (ell^{-2} + |xi|^2)^s |u^(xi)|^2 dxi)^{1/2}` (verified as an analytic corollary, 5(o); the
     values of the scaled constant below are floating, certified values for the `C^4` cutoff are given above). For
     `delta = 0.0165` the constant `R_ell` of the conjugated operator is about 23 at `ell = delta` and about 5.4 at
     `ell = 0.0035`, and the inverse bound is about 190 and 6.4 in the respective norms (about 110 and 5.6 for the
     second cutoff shape; for `delta = 0.033` the smallest value, about 30, is near `ell = 0.007`). With
     `||u||_{H^s} <= N_{1/ell}(u) <= ell^{-s} ||u||_{H^s}` the best of these gives an `H^{31/10}` bound of about
     `5.5e7` (at `ell = 0.01`). The localized forcing in the same norms, `N_{1/ell}(tau eps~)`, is about 1.56 to 1.60
     for `ell >= 0.007`, 1.65 at `ell = 0.005` and 1.8 at `ell = 0.0035` (it varies moderately over these scales,
     since its spectral content lies mainly above `1/ell` (`1/ell <= 286` for `ell >= 0.0035`; in the floating
     diagnostic of the residual-certification list above about 77 percent of the `H^{3.1}` energy of `tau eps~` at
     `delta = 0.0165` lies at `|xi| > 1000`, which does not by itself identify the origin of that content); it is
     about 2.3 at `ell = 0.0025` and 6 at `ell = 0.0015`). Floating evaluations of the response-bound formula
     `B_ell N_{1/ell}(tau eps~)`, with `B_ell = (1 + R_ell/d)^s/(kappa - E)`, are about 290 at `ell = delta`, 55 at
     `ell = 0.01` and 11.4 at `ell = 0.0035` (the smallest among the tested scales, first cutoff shape); the separate
     unscaled evaluation (`ell = 1`) is about `3e12`. Since `||u||_{H^s} <= N_{1/ell}(u)` for `ell <= 1`, such a
     value, if certified, would also bound the `H^{31/10}` norm of the auxiliary inverse applied to the localized
     forcing, with no factor `ell^{-s}` (that factor enters only when an operator bound in `N_{1/ell}` is converted
     into one in `H^s`). In particular, with the certified bound below 473 in `N_500` for the `C^4` cutoff (5(o)), a
     certified value of `N_500(tau eps~)` for that cutoff would bound this response in `H^{31/10}` by 473 times that
     value (of order `1e3` if the floating forcing values of the smooth cutoff are indicative); no such forcing value
     is certified. None of these numbers is a lower bound on the true inverse norm, and the displayed estimates do not
     close the proposed constants. A closing argument also needs, in one compatible realization and norm, the outer
     matching and the low-norm, bilinear and velocity constants (products and the quadratic term transform under the
     dilation with explicit powers of ell; these constants have not been computed), inverse bounds uniform over the
     correction ball (5(o) gives no uniform inverse bound: it gives uniform ceilings only for the local forcing
     coefficient `K_1`, which is not an inverse norm, and only under location, coefficient-box and Hessian hypotheses
     on h, which hold on a ball of radius 7/50 in `H^{153/50}(R^2)` but have not been derived from the norm of the
     proposed weighted correction space), the rank-one denominator, comparisons between the localized and the global
     forcing norms, a certified high-norm residual, and both closing inequalities `K_L C_B K_H eta < 1` and
     `K_H eta <= r`, `C_V r <= r_V` (section 7).
   - Hoelder alternative at P (verified for the frozen model, with its own proof; also checked by separate referee
     reviews; the transfer to the variable-coefficient operator is not verified). A Hoelder formulation near P must
     account for the following verified regularity loss of the frozen `L^2`-selected inverse; its quantitative
     residual and closure requirements have not been evaluated. Let `A > 1` and `1 < a = g/(A - 1) < A + 1` (at the
     trial `a = 3.2511`). The frozen source operator with `mu = 1`, including its nonlocal coupling, has on the closed
     `L^2` dilation domain an inverse R of norm at most `2/(A + 3)`. Write `C_*^sigma` for the Hoelder-Zygmund space.
     For forcing supported in a fixed compact set, `||R f||_{C_*^{r(sigma)}} <= C ||f||_{C_*^sigma}` for
     `1 < sigma < a`, with `r(sigma) = sigma - (sigma - 1)/A`, and the output exponent `r(sigma)` is sharp. The loss
     cannot be removed, even for smooth forcing supported near P: for `1 < sigma < q = (1 + g)/A = 3.0293`, explicit
     packets `N^{-sigma} phi(s) psi(y) sin(N y)` produce local `C_*^sigma` output norms comparable to
     `N^{(sigma - 1)/(A - 1)}`. At `sigma = 1` a single logarithm is necessary (for `C^1` and for `C_*^1`). For
     `sigma > a` the output lies in `C_*^q`, and one fixed smooth forcing, even in s and odd in y, has an output with
     no local `C_*^beta` regularity for any `beta > q`. Whether a logarithm is necessary at `sigma = a` is open. In
     `C^{2,alpha}` terms, forcing in `C^{2+alpha}` gives at best `C^{2+alpha'}`, `alpha' = ((A - 1) alpha - 1)/A`,
     which is positive only for `alpha > 1/(A - 1) = 0.1093`; this mapping estimate gives output of order 2.5 only for
     forcing of order at least about 2.664. So the frozen model has no same-order Hoelder inverse at P. A local
     Sobolev order `3 + alpha < s < s_fast` near P, possibly combined with Hoelder norms elsewhere
     (`alpha < s_fast - 3`, about 0.57855), is not excluded by this obstruction; its interface and nonlocal estimates
     are open.
   - the derivative norms;
   - a norm matched to the realization of item 1.
5. Size of the exclusions. Each of the three source-based exclusions of section 7 divides a certified lower bound for
   a residual quantity of the trial at its source by a constant that bounds how fast that quantity can change over the
   excluded set. For the four-jet form the quantity is `|d_y F(rho~)(P)| > 6.70197e-7` and the constant is
   `C + 2 delta` with `C < 30.0230`, giving the sufficient radius `2.2e-8` (rounded down; the positive root of
   `30.0230 r + 2 r^2 = 6.70197e-7` is about `2.2322e-8`); for the moving-source form the quantity is `1 - mu~`, which
   section 4 encloses within `4.7e-19` of `2.2528046115e-8`, and the constant is `1 + M_V/m < 1.0293212`, giving
   `2.1886e-8` (rounded down); in the whole-plane norm of `H^{153/50}(R^2)` the same quantity divided by a bound of
   the moving-source increment per unit norm (`0.06970585`) gives `3.2318e-7` (rounded down; 5(o)). These are
   sufficient radii in the respective perturbation measures, not maximal ones. Both quantities measure the defect of
   the trial in the differentiated stationarity condition at its source (`d_y F(rho~)(P) = (mu~ - 1) g`); they do not
   measure its residual elsewhere (section 6: the normalized supremum is below `2.92e-4`, by two interval methods,
   with the largest cell upper bound at the lobe near `r = 8.79`, at a radius about 0.19 larger than that of P). In
   our judgement (not a proved statement), with residual quantities of this size an exclusion of this kind is unlikely
   to reach a meaningful uncertainty neighbourhood of X3. A NO statement for a specified neighbourhood must exclude
   exact solutions throughout that neighbourhood; the exclusions discussed here have not been shown to do so for any
   neighbourhood of X3 (the `H^{153/50}(R^2)` set does not contain X3; section 2), and the competitive exponent span
   quoted in section 7 does not itself define such a neighbourhood. The affine `L^2` obstruction of section 7 supplies
   no exclusion radius in the factor norm; the class it excludes contains neither X3 (section 2) nor any factor-norm
   neighbourhood of the trial (item 4).

Explicit unbounded or negative directions (each verified; each shows that a stated criterion fails in a stated space):
- Ordinary `H^s` at P with `s > s_fast` (frozen model, 5(b)), and with `s_fast < s < b_0` for the variable-coefficient
  operator under the hypotheses of 5(d): normalized approximate adjoint kernels concentrating at P.
- Isotropic derivative gain `C^{3,alpha} -> C^{4,alpha}`: flow-box waves with phase constant along V (section 4).
- Logarithmic far weight: tails `r^k log r Phi(theta)` with `Phi` not proportional to the profile's tail (section 4).
- Single-space quadratic bound: modulated packets `lambda^{-s} A cos(lambda v)`, with v a first integral of V, under
  the hypotheses of 5(g). At the exactly joined trial, compact-potential packets give the unconditional logarithmic
  graph obstruction of 5(q), including after any finitely many linear constraints, continuous or not, and on the zero
  set near 0 of finitely many constraints that vanish at 0 and are continuously Frechet differentiable in the graph
  norm with onto derivative at 0.
- Coupling on pure face weights, `b > 2`: constant-norm dilates `R^{b-1} F(X/R)` with `c[F] != 0` (5(f)).
- Corner coupling on the whole-plane pure product weight: constant-norm dilates `R^{S-1} F(X/R)`, `S = a + b`, with
  `d_7[F] != 0` (section 4, 5(k)).
- Transition with collapsing transverse scale (verified, 21:58). For a strip-to-disc energy weight
  `e^{phi(x)} (y^2 + lambda(x)^2)^{-b/2}` with an order-sigma metric of transverse scale lambda, the pure-transverse
  axis rate contains `(b - sigma) w lambda'/lambda`. If lambda tends to 0 at a finite endpoint with `w <= -w_0 < 0`,
  `b < sigma` and the other terms bounded below, this rate is unbounded above along a sequence. In an illustrative box
  around the source coefficients (`sigma = 13/4`, `b = 3.07`) the limiting pure-strip rate at P is at least 29.0443,
  i.e. positive. This shows that the specified Hamilton expression is not uniformly negative; it does not exclude an
  inverse of the full operator.
- Unnormalized formulations. For the scaling tangent `K = rho~ - X.grad rho~`, one has `L K = eps~ - X.grad eps~`. In
  any unnormalized pair of spaces satisfying the hypotheses of section 7 with K in both domains,
  `K_L C_B K_H eta >= eta ||B(K,K)||_{Y_L}/(||L K||_{Y_H} ||L K||_{Y_L})`. If in addition `||L K||_{Y_H} <= C_H eta`,
  `||L K||_{Y_L} <= C_L eta` and `||B(K,K)||_{Y_L} >= b_* > 0`, the product is at least `b_*/(C_H C_L eta)`, so the
  contraction cannot close for small eta. These size conditions are not proved in any realization; without them this
  is a potential conditioning obstruction, and if K belongs to the chosen domain, removing it by a closed linear
  normalization requires a continuous functional `ell` with `ell(K) != 0` (this alone gives no inverse estimate);
  under the background and domain hypotheses of next step 1 below, the centre constraint `J(h) = 0` leaves the best
  inverse constant unchanged in the graph topology of the diagnostic weighted `H^1`-type norm. For the exactly
  normalized modal trial K belongs to an explicit graph domain D of that norm with `0 < ||L K||_X < infinity` (D is
  defined in next step 1 below); thus every constant C satisfying `||h||_X <= C ||L h||_X` for all h in
  `D cap {J = 0, c = 0}` satisfies `C >= ||K||_X / ||L K||_X`, and by 5(p) no such finite constant exists. This
  quotient is bounded below only by 0.069361443018 (verified; next step 1 below, where a floating-point value computed
  from the stored coefficient representation of the trial, about 170, is also reported), and the size conditions above
  are not proved in that topology either. Under the exact-profile hypotheses and for the comparison class specified in
  next step 1 below, no residual-to-error modulus controls the distance to that chosen profile in that norm alone at
  fixed centre coefficient and strain.
- Isotropic energy at the saddle: Fourier cones near the y-frequency and x-frequency directions give energies of
  opposite signs (`sD - b_0 > 0` and `-sA - b_0 < 0`, with `b_0 = 1 + c_l`). This shows only that the energy method
  fails in the isotropic pairing.

Conditional criterion (an available abstract sufficient criterion; its application to the proposed formulation is
open; not shown to be optimal). Section 7 gives a sufficient criterion for additive corrections. Applying it to the
fixed-tail normalized formulation below, with its variable exponent, remains conditional on constructing the augmented
nonlinear map and proving its uniform high-solvability, low-estimate and difference hypotheses; the constants must
control the full normalized coupling, including the strain, on one compatible realization.
- Unknowns: the profile correction h, the tail exponent and one tail amplitude parameter tau. The prescribed leading
  profile `Theta_0` fixes the scale; tau is a transverse tail parameter. J is normalized afterwards by exact scaling,
  which requires `J > 0`.
- Unknown constants, all named and none bounded:
  - `K_H`: high inverse in the weighted realization (an inverse assembled directly from the auxiliary inverse bound of
    5(o) carries its prefactor `(1 + R/d)^s` (in the scaled norms `N_{1/ell}` of 5(o), `(1 + R_ell/d)^s`, with the
    factor `ell^{-s}` on conversion to `H^s`), the rank-one denominator and the outer matching constants, unless a
    sharper estimate is found; of the local constants only `K_1` is known to be uniform over perturbations, and only
    over those satisfying the moving-source hypotheses of 5(o) (source in I, coefficient box, a Hessian budget and an
    admissible moved scale; for corrections in the whole-plane space `H^s(R^2)` no further regularity of `W[h]` is
    needed, by the rough-coefficient extension of 5(o)); all of them hold on the ball of radius 7/50 in
    `H^{153/50}(R^2)` (5(o)), but they have not been derived from the norm of the proposed weighted correction space,
    for which an embedding into `H^{153/50}(R^2)` with an explicit constant would be needed);
  - `K_L`: low a priori estimate;
  - `C_B`: bilinear bound from `E x X` to `Y_L`;
  - `C_V`: velocity bound;
  - `eta`: certified residual in `Y_H`.
- Closing condition: `K_H eta <= r`, `K_L C_B K_H eta < 1`, `C_V r <= r_V`.
- Scope: in this formulation the remainder space admits the saddle incoming mode `|x|^{p_3} y^3` (cut off near the
  origin), so it admits the finite-regularity mode at the centre, and a YES there would not decide `P_infty`.
  Membership of the solution in `P_2` would need in addition, as consequences of the spaces: `C^{2,alpha}` regularity,
  the continuous centre factorization, the normalization, the canonical velocity and the pointwise growth bound.

Kernel, family or ill-conditioning (conditional answer, from the verified conditional theorems of 5(h)):
- Kernel. Under the hypotheses of 5(h) (the far mapping of tail increments and a bounded fixed-tail inverse at the
  exact solution), on the extension of the fixed-tail space by free far-field angular profiles the linearization at
  an exact fixed-tail solution has an infinite-dimensional kernel (isomorphic to `Tau/span Theta_1`), so an
  isolated-kernel picture is wrong there.
  In the fixed-tail space the linearization is invertible by hypothesis.
- Family. Under all hypotheses of the conditional family statement in 5(h), restricting the construction to
  `(Theta_0 + Z) intersect U` gives an injectively parametrized infinite-dimensional subfamily of exact solutions,
  indexed by far-field angular data, with `c_l = 1/k'` on each member; whether the fixed-tail balls lie in a stated
  neighbourhood of X3, and whether the family exhausts the solutions there, are separate open questions. Fixing the
  leading profile `Theta_0` selects one member and excludes the others only within that formulation; it does not
  exclude genuine neighbouring solutions with other tails. A family in `P_2` itself needs, in addition, local
  `C^{2,alpha}` regularity and the centre factorization of every member.
- Not claimed: that `c_l` varies along the family (the functional `ell` is undecided), or that the family exhausts the
  nearby solutions.
- Ill-conditioning. If the conditional family exists, a consistent discretization that resolves its tangent directions
  may exhibit small singular values. This is a heuristic interpretation; no such approximation theorem is proved here.
  The heuristic is consistent with a floating-point observation of the first run: equal-residual states with `c_l`
  between 5.29 and 5.60 whose softest directions are in the far field. That observation is not evidence for
  `ell != 0`.
- Scope. The family is a statement in the fixed-tail spaces (below threshold at P, free tails at infinity); its
  membership in `P_2` needs the additional properties listed under the conditional criterion. For classes smooth at
  P no index or count is claimed (H3).

Structural questions (working hypotheses, not results):
- (H2) A Newton argument in `P_2` needs a complement. The proposed one is the fixed-tail normalization above, in which
  one tail parameter balances one saddle compatibility condition.
- (H3) Withdrawn. An earlier version stated a formal normalized index -1 for classes smooth at P with free tails. It
  rested on the scalar count of the pure transport germ at P (kernel y, one condition `f_y(P) = 0`), which does not
  carry over to the coupled operator (verified counterexample, section 4). No count is claimed for these classes.
- (H4) Index reduction (conditional). Deform the coupling away from P while keeping it at P; this path crosses no
  known threshold. A norm-continuous path of Fredholm operators between fixed domain and target spaces would preserve
  the index; obtaining index 0 also needs a reference operator with computed index and a proved excision formula for
  the interfaces and borders. These are open, so invertibility is not reduced to injectivity. The hypotheses are as
  hard as the missing global estimate.

The centre coefficient `B_3` and `P_infty` (verified conditional statements; no claim about any exact solution):
- Definition. `B_3` is the coefficient of the incoming saddle mode `|x|^{p_3} y^3`, `p_3 = (3D - 1)/A` for the
  profile's own `c_l` (6.1970 at the trial), in the `y^3`-coefficient equation along the x-axis. As the problem
  statement records, smooth `a` near 0 forces `B_3 = 0`, and analogous conditions arise for the higher odd modes
  `|x|^{p_b} y^b`.
- Axis identities and the smoothness criterion (verified; conditional statements, 21:27Z). Here rho is an exact
  solution, `V.grad rho = rho` with `V = c_l X + U[rho]`. Write `G_1 = rho_y(x, 0)`, `G_3 = rho_yyy(x, 0)/6`,
  `w = V_1(x, 0)`, `w_2 = d_y^2 V_1(x, 0)/2`, `v_1 = d_y V_2(x, 0)`, `v_3 = d_y^3 V_2(x, 0)/6`,
  `p = (3D - 1)/A = 6 + 2/A`, `q = (3 v_1 - 1)/w`, `E(x) = -int_0^x (q(t) + p/t) dt` and `H = x^{-p} e^{-E}`, so that
  `H'/H = q` and `x^p H -> 1` at 0.
  - For `rho` and its velocity `C^3` near the open segment and near P, the cubic trace satisfies
    `w G_3' + (3 v_1 - 1) G_3 = f` with `f = -(w_2 G_1' + v_3 G_1)`. The coefficients come from the divergence and
    curl identities `w' + v_1 = 2 c_l`, `w_2' + 3 v_3 = 0`, `2 w_2 = G_1' - w''`. `C^{2,alpha}` does not supply
    cubic traces.
  - Geometry hypotheses: V of class `C^3` near `[0, x_*]`; w has simple zeros at 0 and `x_*` and `w < 0` on
    `(0, x_*)`; `w'(0) = -A` with `A = 2 c_l - 1 > 0` and `D = 2A + 1`; `G_1/x^2 -> 1` at 0; `G_1(x_*) != 0`.
  - At P, `G_1(x_*) != 0` forces `v_1(x_*) = 1`, hence `w'(x_*) = -w'(0)`. The solution bounded at P is unique, with
    `G_3(x_*) = f(x_*)/2`, and it defines `B_3 = -FP int_0^{x_*} H f/w` (Hadamard finite part at 0).
  - If `6 < p < 7`, the factor `a` is `C^{6,alpha}` near 0 with `alpha > p - 6`, and the separate remainder assumption
    `Q := x e^{-E} f/w = q_2 x^2 + q_4 x^4 + q_6 x^6 + O(x^8)` holds, then `B_3 = 0`. A `C^7` factor supplies the
    regularity premise but not by itself the remainder assumption. `P_infty` supplies both locally. So for exact
    profiles satisfying the axis geometry and `C^3` trace hypotheses above, centre smoothness implies `B_3 = 0`;
    applying this to every `P_infty` profile in a neighbourhood needs a separate proof of those axis hypotheses (the
    definition of `P_infty` gives no regularity at P). A nonzero `B_3` is not a `P_2` obstruction.
  - Cutoff: with `Phi_delta = -int_delta^{x_*} x^{-p-1} Q dx - sum_{j = 2, 4, 6} q_j delta^{j-p}/(j - p)` and K a
    constant with `|Q - q_2 x^2 - q_4 x^4 - q_6 x^6| <= K x^8` on `(0, delta)`, one has
    `|B_3 - Phi_delta| <= K delta^{8-p}/(8 - p)`. At the trial's p the physical multipliers are strictly below 0.1590
    (`delta = 1/2`) and 0.5547 (`delta = 1`).
  - Continuity of `B_3` holds in a pullback metric on the axis data Q that includes eighth-order remainder control
    at 0 and an L^1 bound near the endpoint P. It fails in `C^j` for `j <= 6`: with `supp phi` in `(1, 2)` and the
    exponent p above (`p > 6`), `Q_eps(x) = eps^p phi(x/eps)` tends to 0 in `C^j` while its contribution to `B_3`
    stays fixed. Realization of such axis data through densities is not addressed; no density-space continuity
    theorem, class-uniform constant or exclusion radius is known, so no exclusion follows.
  - The explicit trial does not satisfy the remainder assumption (verified, 21:34). The trial's degree-five density
    term produces a nonzero logarithmic resonance in the canonical velocity: the axis velocity w contains
    `lambda x^5 log x` with `lambda` in `(-4.267e-9, -4.265e-9)`, the forcing part of the quantity in the remainder
    assumption contains an `x^4 log x` term with coefficient in `(4.200e-9, 4.202e-9)`, and the full quantity
    (including the trial's cubic defect) an `x^6 log x` term with coefficient in `(-2.158e-12, -2.156e-12)`. So the
    polynomial criterion and the cutoff estimate above cannot be applied to this trial. A generalized logarithmic
    finite part can be defined, but no numerical value of it has been proved. This concerns the trial only and
    excludes nothing.
- No sign claim. No sign or nonvanishing statement about `B_3` of any exact solution is made here, so the continuity
  requirement for such a claim does not arise.
- Continuity is open. After multiplication by a smooth compactly supported cutoff equal to 1 near the origin, the mode
  `|x|^{p_3} y^3` belongs to the weighted spaces of 5(e) when `a < p_3 + 1/2` and `b < 7/2`, as at the feasibility and
  working points. Continuity of `h -> B_3(rho~ + h)` in those norms is not proved.
- Open question. Whether an exact `P_infty` profile near X3 can have `B_3 = 0` is open. One conditional route is to
  seek a member of the tail-parametrized family of 5(h) that satisfies all the necessary centre conditions `B_b = 0`
  (`b = 3, 5, ...`). This is not equivalent to the existence of a `P_infty` profile near X3 without further results
  (that the family covers the solutions in a neighbourhood, the axis regularity, sufficiency of the centre conditions,
  simultaneous solvability), none of which is proved. This is a count, not a result.

Prioritized next steps.
1. Diagnostic finite-section experiment for the inverse and for the family, floating point, run by the numerical team.
   - Compute paired finite sections of the linearization with the weights of 5(e) and 5(f) (face weights
     `|y|^{-2b}`, `b` in `(2.5, 3.406)`), with the fixed-tail normalization and the far weight `gamma' < 2`.
   - For the quadrant norms with `a >= 5/2`, check that every trial basis function and its image under L have finite
     norm in the continuum space, or specify the restricted domain or jet subtraction used: by the last item of 5(e),
     smooth compact densities can have images outside these spaces, which discrete singular values cannot detect.
   - Use three resolutions and record the smallest singular values and their singular vectors.
   - A smallest singular value that stays bounded away from 0 under refinement is evidence for a discrete lower bound
     in the stated norms (injectivity with closed range at best; surjectivity needs a separate range or adjoint
     argument).
   - Control 1: approximate an admissible scaling direction `K_n` and report `||L_n K_n||/||K_n||` in the stated
     norms; a near-kernel is predicted only if this ratio is small (at the trial `L K = (1 - X.grad) eps~` is not
     zero; proved for the exactly normalized modal trial in the next step 1 below).
   - Control 2 (a diagnostic prediction, not a consequence of the theorem at the non-stationary trial): if the kernel
     theorem of 5(h) applies, a consistent and well-conditioned section with a finite tail subspace `T_n` should show,
     before the centre normalization, `d_n = dim T_n - dim(T_n cap span Theta_1)` near-null directions with far-field
     singular vectors (the quotient kernel `Tau/span Theta_1` of 5(h)); imposing the centre normalization `J(h) = 0`
     subtracts the rank of J on that kernel (one when the scaling direction is represented and its centre trace is
     nonzero). This counts an algebraic rank reduction; under the hypotheses of the bullet on the normalization below,
     imposing `J(h) = 0` leaves the continuum inverse constant in the diagnostic graph norm unchanged, so the rank
     reduction does not establish an improved continuum inverse estimate.
   - With the fixed-tail sections, compute `ell(Phi)` for a few profiles Phi supported away from the axes, under
     refinement. These are finite-section diagnostics at a non-stationary trial: only at an exact family member with a
     validated linearization would a nonzero value prove that `c_l` varies in that direction, and zero values on
     finitely many profiles would establish neither first-order stationarity nor local constancy.
   - Status (floating point, numerical team, not reproduced): sections with one collocation point per cell at three
     resolutions are under-sampled (about 2000 of 7011 singular values below `1e-6` of the largest at the finest one).
     With four points per cell and the raw column basis (inner powers and outer power laws with sup-type scaling), the
     smallest singular direction mixed the normalization-amplitude column J with mode-0 splines, and with 16 free tail
     profiles one tail-dominated near-null direction appeared. With a conditioned column basis intended to conform to
     the diagnostic `H^1`-type norm below (1866 retained columns, join continuity imposed numerically, not certified;
     not conforming to the proposed `H^{3.06}` graph domain) and the inner product
     `int (h g + r^2 grad h.grad g) m^{-2} (1 + u^2)^{-3/2} dX` (first row density only), the smallest singular values
     are about 0.12 to 0.18, the median about 25 and the largest about `4e4`, and none of the smallest singular
     directions is strongly correlated with the J column or the tail span (squared cosines below 0.002). The reported
     correlations with the specified references are small in these finite diagnostics, and Control 2 is not confirmed.
     Their column form uses the weight of X with piecewise gradients (an X inner product only for conforming columns),
     and their rows carry a differently weighted norm of values. 5(p) (verified later) excludes a positive X-to-X
     lower bound at the exactly normalized trial on domains containing its quasimodes; it gives no conclusion about
     these singular values. The numerical team attributes the earlier small singular values to the raw basis; these
     observations do not exclude other J-related near-kernel directions. The `ell(Phi)` test is not resolved (relative
     residuals 0.08 to 0.57). At the same row density a face-weighted `L^2` inner product (smallest about 0.038,
     largest about `5.2e13`, a spread the computation attributes to the mismatch of its measure and the row weight)
     has also been reported, in floating point and not independently reproduced. A `C^1` join variant reported with
     these sections (smallest singular values about 0.12 to 0.18 at this density and 0.1164, 0.1582, 0.1893 under the
     row refinement described next, 1847 retained columns) has been withdrawn by the numerical team as a `C^1` join
     diagnostic. The team reports that its relative rank cutoff (`1e-10` times the largest singular value of the
     constraint matrix before row normalization) selected numerical ranks 48 of 64 (M = 16) and 72 of 96 (M = 24, the
     larger section below); it attributes the rank loss to the small outer value-continuity rows and reads the
     withdrawn variant as permitting value jumps at the outer join. Verified separately: the exact external matching
     matrices defined by the source code from the two frozen column datasets have full row ranks 64 and 96. Their four
     rows per angular mode are the jumps of `B_m` and of `B_m'` (derivative in `t = log r`) at each of the two
     external joins; since `[h] = R^3 sum_m [B_m] Phi_m` and `[partial_r h] = R^2 sum_m (3 [B_m] + [B_m']) Phi_m` at a
     join of radius R, together they match values and radial derivatives. In particular, if `[B_m'] = 0` for every m
     at a join, then `[partial_r h] = 3 [h]/R`, so a nonzero value jump entails a nonzero jump of the one-sided radial
     derivative; the team reports that the withdrawn constraint system admitted such nonconforming inputs at the outer
     join. Two further coordinates receive zero constraint columns in the source; their physical traces were not
     revalidated. These row functionals are independent, so an exact truncation to rank `r < 4M` imposes r independent
     linear combinations of them, and its coefficient kernel has `4M - r` more dimensions than the full one; this does
     not determine whether any subsequently retained vector violates a constraint, and since the retained combinations
     need not be a subset of the named rows, identifying the lost directions with the outer value rows requires a
     separate row-space calculation, which has not been done. Relating this result to a particular `C^1` execution
     requires call-time conditions that are not attested (the frozen columns bit for bit, the same modes and join
     radii, all column coordinates selected and finite strictly positive column scalings); the floating matrix
     evaluations and rank decisions were not reproduced. Refining the row density of the conditioned section (two,
     four and six collocation points per cell; 10760, 18680 and 26600 rows) gives smallest singular values 0.1208,
     0.1698, 0.2067 (`C^0` joins); divided by the square root of the number of rows these are `1.165e-3`, `1.242e-3`,
     `1.268e-3`; the largest values are `4.01e4`, `4.10e4`, `4.27e4`; the five smallest singular directions have
     squared cosines below `2e-6` with the J column, the tail span and the inner scaling direction at each density.
     With the face-weighted `L^2` inner product the smallest values are 0.0383, 0.0542, 0.0664, and the maximum
     squared cosine with the J column over the five smallest singular directions ranges from about `5.3e-5` to
     `5.7e-5` across the three densities (all floating point, not reproduced). Verified separately, as statements
     about this diagnostic norm and not about the spectrum: the J column and the inner scaling direction are `x^2 y`
     times the indicator of a disc, whose weak gradient contains a measure on the circle, so they do not lie in the
     `H^1`-type space of this inner product, and the squared cosines quoted with them for this inner product are
     correlations of the piecewise-gradient form that the computation uses, not angles in that space; moreover the
     central coefficient `a(0)` of `h = x^2 y a` is unbounded in this norm (for `0 < eps <= L`,
     `h_eps = x^2 y (1 - r^2/eps^2)_+^6` has `a(0) = 1` and norm below `L^3 eps`). The tail-span cosines are angles in
     that space if the tail references and the retained combinations are exactly continuous, which is not certified;
     these statements do not reject the floating spectrum on the intended continuous combinations. Also verified: a
     finite piecewise-`C^1` section with the stated endpoint growth lies in this space exactly when all its value
     traces at piece endpoints agree exactly (`C^1` matching is not needed), and the saved polynomial pieces of the
     conditioned spline columns do not meet this: every tested interior mode-zero spline column (90 in the section
     above, 187 in the larger section of the refinement mentioned next) has a nonzero value jump at a piece endpoint
     inside the external annulus (for one selected column of the larger section the jump of the radial coefficient is
     strictly between `1e-22` and `1e-14`), so these encoded columns are not in the space, and the full external-join
     constraint kernel of the larger section contains such a nonconforming direction before eigenvalue truncation, for
     every finite matching order and all four column selections. This does not show that the retained combinations or
     the computed singular values are wrong; a conforming reconstruction (continuous B-splines) remains possible, with
     an effect that is not quantified. Unlike the central coefficient, the raw strain in its integral form
     `c[h] = (1/pi) int h sin(3 theta) r^{-3} dX` (equal to `psi[h]_xy(0)` under additional hypotheses: h locally
     `C^2` with the stated parity, `|h| + r |grad h| = O(r^3)` at the centre and `O(r^gamma)`, `gamma < 1`, at
     infinity, and the canonical inversion) is a bounded functional in this norm on densities in the space (constant
     `1/(L^2 sqrt(10 pi (1 - 2k)))` for `0 < k < 1/2`, below 0.0038056 at the section's `L` and `k`), and every level
     set of `a(0)` remains dense at fixed strain among the densities of the space of the form `x^2 y a` near the
     centre with `a` continuous, so fixing the strain does not control `a(0)`. Within the span of the saved polynomial
     pieces of the section's columns, the exactly continuous functions form a subspace of dimension at most 515 (at
     most 771 for the larger section), while the computation retains 1866 columns (1847 in the withdrawn `C^1` join
     variant), so for this section the retained list cannot be orthonormal in the space as exact functions: it is
     linearly dependent or not contained in the space (which of the two, and for which vectors, is not determined);
     this does not refute the computed singular values. An exact affine endpoint repair produces 90 and 187
     independent continuous radial functions, giving 1440 and 4488 independent functions with their angular copies, in
     different continuous trial spaces contained in the space; for each tested column h in any single angular mode the
     repair `h_rep` satisfies `E_b(h_rep - h)/E_b(h) < 8.45e-15` (section above) and `< 2.57e-14` (larger section),
     where `E_b` is the square root of the diagnostic energy integral evaluated with piecewise classical gradients.
     These are broken-energy errors, not distances in the space from the discontinuous originals; no relative bound
     for arbitrary combinations and no transfer to the computed collocation matrix or its floating spectra is
     established. Also verified: for the selected 1440 (4488) columns, with each original column `h_j` and its repair
     both normalized by `E_b(h_j)`, the exact Gram matrix of the normalized repairs in the space differs from the
     exact normalized broken-energy Gram matrix G of the originals by less than `2.44e-11` (`2.31e-10`) in spectral
     norm (exact integrals; the bounds do not certify the computed quadrature matrices). With `eta = sqrt(N) delta`,
     where N is the number of columns and delta the single-column bound above, `eta < 3.21e-13` (`1.73e-12`), and the
     corresponding comparison of the two matrices in quadratic-form order is conditional on a certified bound
     `G >= gamma I` with `gamma > eta^2`; no such bound is available, and a Gram comparison alone transfers no
     operator row. Assume on the plane that `rho` is in `W^{2,infty}_loc`, that the canonical velocity `U[rho]` is in
     `W^{1,infty}_loc` and divergence-free, and that `c_l != 0` (background hypotheses; they hold for the exactly
     joined and exactly normalized trial, whose density is locally `C^{2,alpha}` and whose canonical velocity is
     locally `C^1`, by the normalization and scaling-tangent bullets below and timeline 10-21 20:26, and `c_l = 1/k`).
     For a continuous density supported in a compact annulus of the finite angular form
     `h = r^3 sum_m B_m(log r) Phi_m(theta)`, `Phi_m = cos^2 theta sin theta cos(2 m theta)`, with each `B_m` of class
     `C^2` up to the endpoints of finitely many radial pieces (the zero exterior included at the support boundaries),
     `L h` is `H^1` across a join exactly when every `B_m` has matching first derivatives in `log r` there (the proof
     uses `int_0^{2 pi} V_r(R, theta) d theta = 2 pi c_l R`, which is not zero, and the uniqueness of the finite
     angular expansion). The two exact audits of the derivative traces report nonzero derivative jumps at all 2493
     joins of the 277 selected radial repairs, so, under these background hypotheses, each selected repaired
     single-mode column has `L h` outside `H^1_loc`, and an image norm controlling the full weak `H^1` derivative near
     the joins requires, in this finite angular class, columns with exactly matching first derivatives; linear
     combinations may cancel the jumps, no retained vector is identified, and this does not bear on the `L^2`-type
     image rows used above. Exact quintic Hermite repairs of the same 277 radial functions (all value, first and
     second derivative traces matching exactly, the zero exterior included) give, for the two collections
     respectively, 1440 and 4488 independent single-mode columns of class `C^{2,1}`; their factors vanish near the
     centre, and under the background hypotheses just stated their images belong to `H^1_loc`. For each column the
     broken norm of the correction is below `1.15e-14` (`3.38e-14`) times the broken norm of the original column, and
     its distance in the space from the continuous repair above is below `1.993e-14` (`5.95e-14`) times the norm of
     that repair. These are single-column bounds; no comparison of images, no global image bound and no matrix
     transfer is established. Also verified, for the same class of densities and under the same background hypotheses:
     at a join `r = R` the jump of `L h` (the jump of its transport part; the other terms are in `H^1_loc`) is
     `V_r(R, theta) R^2 sum_m [B_m'] Phi_m(theta)`, where `[B_m']` is the jump (outer minus inner) of the first
     derivative in `log r`. Hence, in rows that discretize one derivative of `L h` by finite differences in `log r` of
     its sine coefficients, two nodes at spacing Delta on either side of the join pick up the term `wbar J_N / Delta`,
     or `wbar J_N / Delta^{1/2}` with trapezoid weights, where `J_N` is the sine coefficient of the jump and `wbar`
     the mean row weight of the two nodes (a term of an exact decomposition, not a bound for the row). In a model
     example (zero background with `c_l = 1/3`, `R = 100`, `Delta = 1/50` and one derivative jump `1e-14`; not the
     trial or its grid) these terms lie in `(9.9378689e-8, 9.9378690e-8)` and `(1.4054269e-8, 1.4054270e-8)`. So a
     bound of order `1e-14` on the derivative jumps does not by itself give the bound `1e-11` that the numerical team
     states for the contribution of the internal spline joins to its derivative rows; that stated bound is neither
     confirmed nor refuted (the verified derivative-jump audit above concerns the selected exact repairs, not the
     saved columns or their retained combinations). Small diagnostic-norm errors do not by themselves control
     collocation rows either: for `c_l != 0` the value row `h -> ((c_l X.grad - 1) h)_N` at a fixed radius R is
     unbounded in this norm (there are compactly supported annular `C^2` densities `h_eps` with `||h_eps||_X -> 0`
     whose rows `((c_l X.grad - 1) h_eps)_N` at R equal `c_l R^3/4` for `N = 0, 1`). A sufficient inequality
     transferring the smallest generalized singular value of a fixed finite section to a repaired one is proved under
     an explicit Gram comparison and an explicit bound on the difference of the row matrices; neither hypothesis is
     evaluated for the computed sections. Refining the section size at four collocation points per cell (more angular
     modes and a finer spline knot stride: 5259 columns, 48 constraints, 5126 retained (more than the bound 771 above;
     this comparison uses the reported count and was not part of the verifier's audit), 27360 rows; the image is
     observed with 32 instead of 40 outer modes) lowers the three smallest singular values to 0.1492, 0.1797, 0.1851
     (from 0.1698, 0.2028, 0.2131; divided by the square root of the number of rows `9.018e-4` against `1.242e-3`),
     while the largest value and the per-row 1 percent quantile change little (`4.10e4` to `4.28e4`, `4.15e-3` to
     `4.41e-3`); the squared cosines of the five smallest directions with the J column, the tail span and the inner
     scaling direction stay below `2.7e-6` (`H^1`-type inner product, `C^0` joins; floating point, not reproduced). So
     the two section sizes give no stable lower bound, and the comparison mixes the larger column space, the weaker
     observation of the image and the smaller number of rows per retained column. The numerical team expects the
     smallest value to decrease under refinement: the columns carry an `H^1`-type norm and the rows an `L^2`-type norm
     of `L h`, so the section tests a derivative-gaining lower bound, and flow-box waves with phase constant along V,
     verified in section 4 against derivative gain on the Hoelder scale, are the model counterexample; their version
     in the weighted spaces of this diagnostic is not verified. No conclusion about a near-kernel of the linearized
     operator, in either direction, is drawn from these sections.
   - Third version (floating point, numerical team, not reproduced): the constraint rows are normalized before the
     rank decision, and full rank is reported for all prescribed external-join constraint rows (for the `C^1` matrices
     constructed from the checked frozen data, the exact full row rank stated above is preserved by invertible row and
     column scalings, and so by row normalization; application to the reported version-3 runs remains conditional on
     the call-time conditions above, and their floating rank decisions have not been reproduced). Verified separately,
     the five saved arrays reported as the smallest directions of the trapezoid-weighted derivative-row form with
     prescribed `C^1` external-join constraints were checked at each section size. Interpreting their entries as exact
     dyadic coefficients in the original coordinates specified by the checked source, every external-join row value is
     nonzero: 64 per vector for the smaller section and 96 for the larger. Over all five arrays and all rows of each
     unscaled source matrix, the maximum absolute row value is strictly below `1.672e-15` for the smaller section and
     `3.725e-15` for the larger. Thus each saved array lies outside the exact kernel of its corresponding
     source-defined matrix. This does not imply that the floating decomposition failed its tolerance, and no relative
     residual size is assessed. The source matrix assigns zero columns to two additional field coordinates and to all
     extra coordinates; the saved extra coefficients are zero. Physical traces of the omitted components and possible
     cancellation with the checked traces are not examined. The source and metadata checks do not authenticate
     execution of the reported runs. According to the numerical team's corrected account, these sections use the full
     linearization, including the rank-one term from the variation of `c_l` with the strain of h, and no zero-strain
     constraint is imposed. For the larger section at four points per cell the `C^0` values above are reproduced, and
     with `C^1` joins the three smallest singular values are 0.1499, 0.1798, 0.1851 (largest `2.09e4`, 5078 retained
     columns). Rows that also discretize one derivative of `L h` (27360 value rows weighted in addition by
     `(1 + (2N + 1)^2)^{1/2}` for the sine mode of frequency `2N + 1`, and 27328 rows of finite differences in `log r`
     of the sine coefficients with the mean row weight; `C^1` joins) give 3.093, 4.029, 4.371 (largest `4.24e6`), and
     the same rows with radial trapezoid factors (`omega_i^{1/2}` on value rows, `Delta_i^{1/2}` on difference rows),
     which approximate an integral over `log r` and are meant for comparison across sections of different collocation
     density, give 0.3775, 0.4773, 0.5359 (largest `2.75e5`). In all four forms the squared cosines of the five
     smallest directions with the J column, the inner scaling direction, the tail span and three reference densities
     `x^2 y f(log r)`, with f a polynomial step from 1 to 0 across a window in `log r` (ending at the outer join,
     ending at the inner join, and spanning the spline region), are below `1e-3`, while the computation reports
     squared cosines 1.0000, 0.9297 and 1.0000 of these references with the retained space. These are floating
     correlations computed with the broken-energy form; reading them as angles in the diagnostic space requires the
     functions involved and the retained space to belong to that space, which is not certified for the retained space
     even where the reference conforms. The numerical team reports that the five smallest directions are nearly
     contained in the spline span (squared projection about 0.99999 in the broken-energy form). For the first three,
     the reported medians of their diagnostic energy distribution in r range from about 2.8 to 11.9, and their 10 to
     90 percent radial intervals lie within about `[1.07, 22.3]`, a range that contains the radius of P (about 8.6)
     and the length scale `L` of the weight (about 7.65); radial shells do not locate them at P. The team identifies
     the weighting as one possible contributor: for the stated weight against planar area measure, the ratio of the
     squared row weight to the density of the X measure in `t = log r` is `(1 + u)(1 + u^2)^{3/2}/(L^2 u^2)`,
     `u = r/L`, which has its unique minimum at `r = L`; its effect on the weakest directions also depends on the
     operator, the derivative terms and the sampling, so the localization mechanism remains unresolved. For the larger
     section the saved floating profiles give about 87 percent of the diagnostic energy in the sine frequencies 1 and
     3 for the smallest derivative-row direction and about 81 percent for the smallest trapezoid-weighted
     derivative-row direction; for the smaller section the corresponding shares are about 90 and 83 percent. The
     numerical team's claim of about 81 percent for the smallest derivative-row direction of the larger section is
     contradicted by the saved profile of that direction. A separate floating evaluation by the verifier on a finite
     radial interval agrees with all four percentages at the precision quoted here; it supplies neither a certified
     energy enclosure nor a bound for the omitted radial tails. Other weak directions have substantial high-frequency
     content: the third value-row direction of the larger section reportedly has about 73 percent of its energy in
     frequencies at least 33. For the smaller section at four points per cell the third version reproduces the `C^0`
     value 0.1698 and gives 0.1708, 0.2029, 0.2131 with `C^1` joins (1834 retained columns), 2.449, 3.230, 3.293 for
     the derivative rows (37320 rows, largest `3.45e6`) and 0.4131, 0.5200, 0.5465 for the trapezoid-weighted
     derivative rows (largest `2.25e5`). From the smaller to the larger section the three smallest trapezoid-weighted
     values thus decrease by about 8.6, 8.2 and 1.9 percent, while the largest value, the 1 percent quantile (1.75 to
     2.57) and the median (135 to 196) increase; with two sizes neither a plateau nor convergence to zero is
     established. The comparison changes the trial space, the output angular cutoff and the sampling, and its retained
     spaces are obtained section by section by Gram eigenvalue filtering, so nesting of the nominal trial spaces does
     not justify a monotonicity claim for these retained sections. Intermediate sections reported since (the same
     trapezoid-weighted derivative-row form, four points per cell, `C^1` joins; floating point, numerical team, not
     reproduced) give comparisons that change one named discretization parameter at a time: refining only the spline
     knot stride of the smaller section (the stride-refined section, 3386 retained columns) gives 0.4129, 0.5200,
     0.5460; refining only the angular trial modes from 16 to 24 (the angle-refined section, 2750 retained) gives
     0.3777, 0.4775, 0.5366 (largest `2.29e5`, 1 percent quantile 1.73, median 149); lowering only the output angular
     cutoff of the angle-refined section from 40 to 32 modes changes each of its five smallest values by less than
     `3e-5` relative; and refining the stride from there gives the larger section. At the tested settings the angular
     refinement produces the dominant observed decrease (about 8.6, 8.2, 1.8, 8.7 and 3.5 percent in the five smallest
     values); the stride refinements change them much less (at most about 0.12 percent, in the third value with 24
     modes), and the output cutoff less still. The verifier recomputed the ten relative changes with 24 modes, for the
     output cutoff and for the stride at output cutoff 32, in exact rational arithmetic from the stored binary64
     values (relative to the value with 40 output modes and to the value with stride 16 respectively; all ten nonzero,
     at most `2.734e-5` for the cutoff and `1.163e-3` for the stride), and found, in the two saved images of the
     source-labelled weakest direction of each trapezoid-weighted form in the angle-refined section, less than 0.016
     percent of the stored energy of output modes 0 to 39 in modes 32 to 39, in each of the four row functionals
     (section 8); these are observations on saved arrays and scalars, and no bound for output modes 40 and above
     follows. For the smaller section at two, four and six collocation points per cell (third version; floating point,
     numerical team; the values themselves are not recomputed; 10760, 18680 and 26600 collocation rows; the saved
     numbers of retained columns are the same at the three densities, 1866 for the value rows with `C^0` joins and
     1834 for the rows with `C^1` joins, and the column construction of the source code does not depend on the
     density, but equality of the retained subspaces is not certified), the three smallest trapezoid-weighted
     derivative-row values are (0.4130, 0.5200, 0.5463), (0.4131, 0.5200, 0.5465) and (0.41313, 0.52005, 0.54653), the
     three smallest trapezoid-weighted value-row values display as 0.02814, 0.03245, 0.03363 at all three densities,
     and the largest absolute relative changes of the five smallest stored values (the absolute difference divided by
     the value at the coarser density) are at most `2.213e-4` (value rows) and `3.240e-4` (derivative rows) from two
     to four points and at most `2.447e-5` and `6.760e-5` from four to six (exact rational recomputation by the
     verifier from the stored binary64 values; all 40 changes of the weighted and unweighted values are nonzero;
     section 8). The smallest unweighted values grow with the number of rows: 0.1208, 0.1698 and 0.2067 for the value
     rows with `C^0` joins (as in the row-density refinement above; increases of about 40.5 and 21.8 percent relative
     to the coarser density) and 1.764, 2.449 and 2.951 for the derivative rows (about 38.8 and 20.5 percent). These
     observations at three densities do not establish convergence in the row density and give no bound at any other
     density. In the sections for which direction diagnostics are reported, the radial energy medians of the three
     weakest directions agree within each angular size (about 3.6, 8.7 and 8.5 with 16 modes, about 2.8, 6.9 and 9.4
     with 24), and the smallest direction has 81 to 83 percent of its energy in the sine frequencies 1 and 3
     (`N = 0, 1`). The smallest value also depends on the Gram eigenvalue filtering: in the stride-refined section,
     retaining the eigenvalues of the equilibrated Gram matrix above `1e-12` or `1e-8` times the largest, instead of
     `1e-10` times it, moves the smallest value by about minus 1.7 and plus 0.5 percent. The value rows behave
     differently: with `C^0` joins their smallest value divided by the square root of the number of rows rises by
     about 3 percent under the stride refinement and falls by about 37 percent under the angular refinement, and with
     trapezoid factors and `C^1` joins their smallest values lie far below those of the derivative rows: they round to
     0.0281 in both the smaller and the stride-refined section, where the derivative-row values round to 0.4131 and
     0.4129, and to 0.0178 in the angle-refined section, so that from the smaller to the angle-refined section the
     reported decreases are about 37 percent for the value rows and 8.6 percent for the derivative rows. The numerical
     team reports that the third and fifth weakest directions of the trapezoid-weighted value rows in the
     stride-refined section are radially oscillatory thin shells; the third is localized near the radius of P, with
     99.6 percent of its diagnostic energy in `8 <= r < 16` and the 10 to 90 percent range of that energy in
     `8.58 <= r <= 8.97`, and the trapezoid-weighted derivative-row quotients of the same two vectors round to 4.36
     and 3.83, about ten times the reported smallest value of that form; this floating observation is consistent with
     the derivative-gain mechanism described above but does not establish it. Separately, for these two saved
     directions and four other preselected saved directions, the verifier reproduced all 24 stored row-quotient values
     as literal finite-array functionals, with absolute errors strictly below `2e-12` (section 8); this check concerns
     the stored values underlying the rounded displays and does not establish the reported shell localization, the
     energy percentages or a minimizing property. These comparisons establish neither convergence nor a positive lower
     bound in infinite dimensions; with two angular sizes no limit, positive or zero, is established, and a third
     angular size has not been computed. Verified separately, for the references reconstructed from the checked source
     at the section endpoints recorded in the third version's `C^0` output for the larger section: the first two
     references are of class `C^4` and lie in the diagnostic space; for the third, the radial factor f has inner trace
     strictly between `1.2121e-13` and `1.2122e-13` at the outer end of its window, while f vanishes outside, so this
     density has a nonzero value jump on open arcs of that circle and is not in the diagnostic space; the intended
     unrounded formula is of class `C^4`. This applies to the references of the reported runs only if they used the
     checked source at these endpoints; the source check does not authenticate execution of those runs. No conclusion
     about a near-kernel of the linearized operator is drawn from these sections either.
   - Normalization in the diagnostic graph topology (verified, with its own proof and two exact symbolic methods for
     the canonical stream function and strain of the bump; also checked by a separate referee review). Let X be the
     weighted `H^1`-type space of the Status above (any `L > 0`, `0 < k < 1`) and assume for the background, as
     hypotheses for this general statement, that rho is locally `C^{2,alpha}` for some `0 < alpha < 1` with
     `|grad rho| <= A r^{1+alpha}` and `|D^2 rho| <= A r^alpha` for `r <= 1`, `|grad rho| <= D r^{k-1}` and
     `|D^2 rho| <= D r^{k-2}` for `r >= 1`, and that V is of class `C^1` near the closed unit disc with `V(0) = 0`,
     `|V| <= B r` and `|DV| <= B` there. With `c[h]` taken from the fixed canonical inverse (for these bumps
     `c[h] = int_0^infty H_3(r) r^{-2} dr`, `H_3(r) = (1/pi) int_0^{2 pi} h(r, theta) sin(3 theta) d theta`), the
     bumps `h_delta = x^2 y (1 - r^2/delta^2)_+^6`, `0 < delta <= min(1, L)`, have `J(h_delta) = 1`,
     `c[h_delta] = delta^2/56`, `||h_delta||_X <= C delta` and
     `||L h_delta||_X <= C_1 delta + C_2 delta^{2+alpha} + (delta^2/168) ||X.grad rho||_X` with constants independent
     of delta, and `b_delta = (4 h_delta - h_{2 delta})/3`, `0 < delta <= min(1, L)/2`, has `J(b_delta) = 1` and
     `c[b_delta] = 0`. Let D be a real linear space of perturbations that contains all these bumps and whose elements
     have a continuous even-even factor near the centre (J is the value of that factor at 0; this does not make J
     continuous in any norm), a canonical strain, and h and `L h` in X. Then every level of J is dense in D for the
     graph norm `||h||_X + ||L h||_X`, also within each level of the strain, and for a fixed C the estimate
     `||h||_X <= C ||L h||_X` holds on `D cap {J = 0}` exactly when it holds on D, and on `D cap {J = 0, c = 0}`
     exactly when it holds on `D cap {c = 0}`; the same holds for any image norm equivalent to that of X. Consequently
     the constraint `J = 0` cannot restore a finite inverse estimate when the comparison domain contains a nonzero
     kernel vector of L (the normalized vectors `K - J(K) b_delta` are then approximate kernel vectors, although K
     itself need not remain a kernel vector after normalization). For the exactly normalized modal trial the scaling
     tangent belongs to such a domain and its image is not zero (next bullet); no kernel vector and no numerical
     singular vector is asserted. A topology that controls the centre factor, a stronger image norm for which the
     vanishing of the bump images is not proved, or a domain that excludes these bumps is not covered.
   - Scaling tangent of the exactly normalized modal trial in this topology (verified, with its own proof, symbolic
     differential identities checked against an independent differential-polynomial algebra, two independent exact
     decoders of the trial data and two interval evaluations of one coefficient; also checked by a separate referee
     review). Let L be the exactly normalized linearization at the exactly normalized modal trial rho~, with residual
     eps~, and let D be the real linear space of the even-x, odd-y functions h that are locally `C^{2,alpha}` for some
     `0 < alpha < 1`, equal `x^2 y b` near 0 with b continuous and even in both variables (`J(h) = b(0)`), satisfy
     `|h| + (1 + |X|) |grad h| <= C (1 + |X|)^gamma` for some `gamma < 1`, have a locally `C^1` canonical velocity
     (divergence-free, `curl U[h] = -d_x h`, of the stated parity, `o(|X|)` at infinity) with finite strain `c[h]`,
     and have h and `L h` in X. The trial satisfies the background hypotheses of the previous bullet (with constants
     that exist but are not evaluated), and D contains the bumps there. The scaling tangent `K = rho~ - X.grad rho~`
     belongs to D, with `J(K) = -2`, `c[K] = 0`, `U[K] = U - X.grad U` and `L K = eps~ - X.grad eps~` as an identity
     of functions, and `0 < ||L K||_X < infinity`: near the centre `L K = -4 r^5 E(theta) + O(r^7 (1 + |log r|))` with
     E the leading centre term of the residual (section 4), so the sine coefficient of the leading term at frequency
     523 lies in `(-2.4e-11, -2.0e-11)`. The vectors `K + 2 b_delta` have `J = 0` and `c = 0` and converge to K in the
     graph norm, so every estimate `||h||_X <= C ||L h||_X` on `D cap {J = 0, c = 0}` requires
     `C >= ||K||_X / ||L K||_X` (by 5(p), verified later, no finite C exists on this domain at all). K is not a kernel
     vector. The conditional bound `||L K||_{X(E)} < 585.874` of section 6, together with the verified end-region
     bounds there, gives `||L K||_X < 585.874000000002` on the whole plane, but only under the unverified majorant
     hypotheses on E. The direct bound `||L K||_X < 2464.68293019825564964515` of section 6 is verified but coarse.
     With the verified lower bound `||K||_X > 170.953964620623929217261`, from the annuli of three whole knot spans of
     the middle region (timeline 10-22 11:47), the direct bound gives `C > 0.069361443018` for every such estimate on
     `D cap {J = 0, c = 0}` and on every domain containing K; this necessary bound is a diagnostic only. The following
     norm values come from a reported floating-point computation that was not independently reproduced. The
     computation uses the stored coefficient representation of the modal trial, retaining its floating least-squares
     values of the joining corrections and of the normalization-dependent leading coefficient. This representation
     differs from that of the exactly joined and exactly normalized trial rho~. For the stored density rho_s (the
     stored binary64 coefficients and log knots, and the binary64 rates given by the stored rate expressions, read as
     exact dyadic numbers; the joins are at `R_i = e^{t_a}` and `R_e = e^{t_b}`) the following is verified (with its
     own proof, two independently implemented exact and interval enclosure paths on the stored data, which share that
     data and its mathematical interpretation, and a check of the end-growth hypotheses with the exponent 1/2, the
     leading far exponent of rho_s exceeding the stored binary64 value of k by `2^{-53}`; also checked in a completed
     referee review, a separate adjudication and a separate referee audit). At each of the joins `r = R_i` and
     `r = R_e` all 260 modal coefficient jumps are nonzero, so rho_s is not in `H^1_loc` across the joins, and
     quadratures of its piecewise derivatives are not a weak `H^1`-type norm of it. Write `[.]_j` for the jump from
     the inner to the outer side at the join radius `R_j`, the subscript pw for classical derivatives on the three
     open regions separated by the joins, and `M = sum_j R_j [rho_s]_j delta_j`, where `delta_j` is arc length measure
     on the circle `r = R_j`. Then `X.grad rho_s = (X.grad rho_s)_pw + M` as distributions. Hence, with
     `K_pw = rho_s - (X.grad rho_s)_pw`, the derivative at `a = 1` of the scaling family `a rho_s(X/a)` of section 4
     is the distribution `K_pw - M`. On each open region, with L linearized at rho_s, eps_s the classical residual of
     rho_s there (formed with the canonical velocity `U[rho_s]` and the same exponent as L) and `U[M]` the canonical
     velocity of M (section 2; for this compactly supported distribution
     `U[M] = (-partial_y, partial_x) partial_x (G * M)` with `G(X) = -log|X| / (2 pi)`, smooth away from the join
     circles), `L K_pw - (eps_s - X.grad eps_s) = U[M].grad rho_s + (c[K_pw]/3) X.grad rho_s`. The canonical strain is
     `c[K_pw] = sum_j [H_3]_j / R_j`, with `H_3(r) = (1/pi) int_0^{2 pi} rho_s(r, theta) sin(3 theta) d theta`, and
     lies in `(4.46796331677046e-18, 4.46796331677047e-18)`. The two correction terms can cancel, so the positive
     strain alone does not show that the correction is nonzero, and no bound on it is claimed. The strain obtained by
     Green integration of the source of rho_s interval by interval, which omits the contributions of the joins, minus
     the canonical strain of rho_s lies in `(-2.56259669151642e-17, -2.56259669151641e-17)`; this is a difference
     between two exact conventions, not an error bound for any saved floating-point value. The discontinuity and the
     nonzero strain concern the stored density only. For the exactly joined trial rho~, `M = 0`, `c[K] = 0` and
     `L K = eps~ - X.grad eps~` holds exactly. Write K_num for the numerical scaling data obtained from this
     representation. These data are intended to approximate K, without a certified identification or error estimate.
     The numerical image data are computed from the residual modes and their first two derivatives in `t = log r`,
     using the analytic modal jets of the stored representation. The calculation uses four Gauss nodes on each of its
     1558 knot cells and log-spaced cells on `1e-4 <= r < R_i` and `R_e < r <= 1e7`; radial integration is truncated
     to `1e-4 <= r <= 1e7`, and angular integration uses the analytic modal formula. The reported quadrature norms of
     K_num and of these numerical image data are about 7659.1 and 44.92, respectively (44.91 for the image calculation
     with six nodes on the cells of `4 <= r <= 16`), giving a floating-point quotient of about 170.5. In this
     truncated image calculation, the reported regional quadrature norms are about 44.91 on `4 <= r <= 16` near P,
     0.319 on `2 <= r < 4` and `r > 16` together, and `3.22e-3` on `r < 2`. In the reported six-node composition on
     that annulus, about 98.8 percent of the saved squared image-norm value comes from the radial derivative term. For
     the stored squared norms on that annulus in the version of the calculation before the correction of the regional
     values, the verifier computed `|S_6 - S_4| / S_4`, about `3.15e-4`, where `S_g` is the stored value with g nodes
     per cell; this comparison is not a quadrature error bound. The verifier also checked the analytic jet and norm
     identities used, under their stated hypotheses; exact agreement of the code computing the residual mode jets, in
     the checked source version, with an independent implementation on synthetic integer inputs at `t = 0`; and
     enclosures of the square roots of the stored squared norms of the four-node calculation in that version and of
     their quotient (about 170.52; section 8). These checks do not authenticate the executed runs or identify the
     stored inputs with the canonical fields of the trial; the corrected regional values above remain numerical-team
     evidence and are not covered by them; and there is no floating error control on the trial, no quadrature error
     bound and no certified norm. All radial regions quoted here are restricted to `1e-4 <= r <= 1e7`, and the omitted
     parts are not controlled. These values are evidence only and give no bound. As verified, the leading far term of
     K is `(1 - k) r^k Theta(theta)`, where `rho~ = r^k Theta + O(r^{2k-1})` with Theta not identically zero, so K is
     not in a linear perturbation space whose `r^k` coefficient vanishes, or whose elements are `o(r^k)` uniformly in
     angle. No retained numerical vector is identified with K. A further floating-point computation (numerical team,
     not independently reproduced by the verifier, who checked only arithmetic on its saved energies and image arrays;
     section 8) compares K_num with the smaller section of the finite-section diagnostics above: 16 angular trial
     modes, 1955 columns, four collocation points per cell at 467 radii in about `3.8e-4 <= r <= 7.7e5`, and output
     modes `0 <= N < 40`. The `C^1` section retains 1834 directions; the unweighted value-row minimum uses the `C^0`
     section with 1866 retained directions. A referee recomputed the saved image functionals, representative
     distances, radius quantiles and assembled mode sums, but did not rerun the complete assembler or the
     finite-section singular-value computation. The sections impose no normalization condition. Membership of K in the
     column classes of the section with additional free tail columns and of the angle-refined section is not claimed;
     the exclusion below concerns the span of the frozen column functions of the smaller section. For the explicitly
     paired stored modal trial and frozen column recipe of the smaller section, the following is verified, with its
     own proof, two exact rational and two interval implementations of the determinant check and two independent
     decodings of the stored data; it was also checked in a completed referee review and a separate adjudication
     (section 8). The stored trial retains its rounded joining and correction coefficients and is distinct from the
     exactly joined and exactly normalized trial of section 2. Use each of two rate conventions separately:
     `lambda = k - 3` in exact arithmetic, or `lambda = fl(k - 3)`, the binary64 rate value used by the stored recipe,
     with the corresponding lower rates. For each convention let rho_st be the stored trial interpreted as a real
     function with those rates, put `t = log r` and write
     `rho_st = r^3 sum_{m=0}^{259} a_m(t) cos^2(theta) sin(theta) cos(2 m theta)`; let A be its stored leading
     coefficient vector, which agrees exactly with the exact rational export of the same stored coefficients, and B
     the stored rounded coefficient vector of the recipe's second leading tail column (neither is replaced by
     coefficients of the exactly normalized trial or of an ideal cosine-product recipe). For `t >= t_0`, with `t_0`
     the stored outer join abscissa, every function in the span of the column functions defined by this recipe, hence
     in each of its `C^1` and `C^0` join-constrained subspaces, has radial coefficient vector
     `g(t) + alpha t A e^{lambda (t - t_0)} + beta B e^{lambda (t - t_0)}` with real constants alpha and beta and
     `e^{-lambda (t - t_0)} g(t) -> 0` componentwise. The other exponential-polynomial terms of the stored trial,
     including its outer correction, have strictly lower rates, so the radial coefficient vector of the scaling
     tangent `K_st = rho_st - partial_t rho_st`, multiplied by `e^{-lambda (t - t_0)}`, tends to `(-2 - lambda) A`;
     this factor is nonzero in both conventions and equals `1 - k` when `lambda = k - 3`. If K_st had the stated tail
     form, angular independence and the leading limit would force `alpha = 0` and then `(-2 - lambda) A = beta B`,
     contradicting the minor `A_0 B_1 - A_1 B_0`, an exact rational strictly between `5.859714460078e-15` and
     `5.859714460080e-15`. Thus K_st lies outside this tail class in each convention. This result concerns only the
     paired stored trial and frozen column recipe of the smaller section. For the exactly joined and exactly
     normalized trial rho~ and the same frozen recipe, an analogous statement is verified, with its own proof, two
     exact rational implementations and two interval methods for the determinant below, and two independent decodings
     of the stored data; it was also checked in a completed referee review and a separate adjudication (section 8). In
     this paragraph coefficient vectors have indices `m = 0, ..., 260`, with the trial and A padded by a zero final
     coordinate; the stored vector B has `B_260 = 0`. For large t the radial coefficient vector of rho~ is
     `C e^{(k - 3)(t - t_0)}` plus finitely many polynomial-exponential terms with strictly lower rates, where
     `C = A + z_* e_0`, `e_0` is the coordinate vector of the mode `m = 0` and `z_*` is the exact normalization
     correction of the leading outer coefficient of that mode; hence the radial coefficient vector of K, multiplied by
     `e^{-(k - 3)(t - t_0)}`, tends to `(1 - k) C`. Let mu be the largest of the lower exact outer rates, of their
     binary64 source values and of the outer correction rate. Then `mu < k - 3 < nu`, where `nu = fl(k - 3)` is the
     binary64 rate of the recipe and `nu - (k - 3) = 2^{-53}`. For `eta = k - 3` and for `eta = nu`, consider the
     class of functions whose radial coefficient vector, for all sufficiently large t, equals
     `g(t) + alpha t A e^{eta (t - t_0)} + beta B e^{eta (t - t_0)}` with real alpha and beta and g a finite sum of
     terms `p(t) e^{eta' t}`, p a vector polynomial and `eta' <= mu`. The span of the recipe's column functions lies
     in the first class when its tail rate is read as `k - 3`, and in the second when it is read as nu. K lies in
     neither class. For `eta = k - 3` the argument is the one above with the minor replaced by
     `(A_0 + z_*) B_1 - A_1 B_0`; the expression `(A_0 + z) B_1 - A_1 B_0` lies strictly between `5.859714459e-15` and
     `5.859714461e-15` for every z in the certified normalization interval, which contains `z_*`. For `eta = nu` the
     larger exponential first forces `alpha = beta = 0`, and then the nonzero leading term `(1 - k) C` of K
     contradicts the rate bound mu on g. The explicit gap `mu < k - 3` is essential in the second case. Replacing the
     lower class by all vector functions `g(t) = o(e^{nu (t - t_0)})` componentwise would admit the radial coefficient
     vector of K itself, so K would belong to the resulting enlarged exterior class. Neither result covers the section
     with additional free tail columns, the angle-refined section or any norm closure, and neither supplies a positive
     norm distance or image estimate. The following floating-point comparisons use numerical scaling data K_num from
     the same stored coefficient representation, with the evaluator's binary64 rates. Write p_num for the computed
     projection representative obtained with the section's computed Gram matrix. No certified identification or error
     estimate transfers these data, their sampled images or their quadrature distances to K. Norms and projection
     calculations in these diagnostics use quadrature over `1e-13 <= r <= 1e23` and are not certified X quantities.
     The reported relative quadrature distance from K_num to p_num is about 1.82 percent for the smaller `C^1`
     section, 1.82 percent with `C^0` joins, 1.76 percent with sixteen additional free tail columns, and 1.15 percent
     for the angle-refined section. Dividing the four sampled-image functionals of the direct image of K_num (computed
     from the residual jets of the stored representation, as the counterpart of `L K = eps~ - partial_t eps~`; for the
     stored density the open-region identity contains the interface and strain terms stated above) by the computed X
     norm of K_num gives about `3.7e-6` for the unweighted value rows, `7.9e-7` for the trapezoid-weighted value rows,
     `8.0e-4` for the derivative rows and `6.3e-5` for the trapezoid-weighted derivative rows; the corresponding
     section minima 0.1698, 0.0281, 2.4485 and 0.4131 are about `4.54e4`, `3.55e4`, `3.06e3` and `6.59e3` times these
     quotients. In the reported floating-point computation, the section's assembler is applied to all 260 input modes
     of K_num without using the scaling identity. With A the saved assembled array and D the saved direct array, the
     four ratios `F(A - D)/F(D)` are about `4.2e-5` to `5.8e-5`. Separately, the verifier enclosed `F(S - D)/F(D)` for
     the exact sum S of the 42 saved partial image arrays (section 8). It also verified
     `max_{i,N} |A_{i,N} - S_{i,N}| < 7.11e-15` and `F(A - S)/F(D) < 1.032e-11` for each of the four discrete row
     norms. The reverse triangle inequality therefore bounds the difference between the corresponding normalized
     discrepancy ratios for A and S by `1.032e-11`. These verifications concern saved arrays only. The reported
     partial sum over the input modes `m < 32` has unweighted value-row and trapezoid-weighted derivative-row
     functionals about `1.73e4` and `1.41e4` times those of D, floating evidence of cancellation between groups of
     input modes. Both routes share the background Green data, so their agreement is a consistency check of the
     perturbation assembly and the jet evaluation, with no independent validation of that background and no error
     bound. For the `C^1` representative p_num of the smaller section, the four quotients of its assembled image by
     its computed X norm are about 19.2, 7.00, 227 and 25.6 (about 19.6, 7.14, 126 and 20.5 for the angle-refined
     section). For both representatives the value-row part of the trapezoid-weighted derivative-row energy of the
     image has its 10 and 90 percent radius quantiles at about `8.5e4` and `5.8e5`, near the outermost collocation
     radius; for the direct image of K_num they are about 8.65 and 8.92, next to P. Thus these representatives are
     close to K_num in the computed X norm but have much larger sampled images, and in these floating diagnostics the
     section minima do not hold as lower bounds for the sampled quotients of K_num, despite a relative distance of
     about 1.82 percent. This concerns K_num itself and does not establish the same phenomenon for functions of the
     column class; transferring a lower estimate from the retained span requires control of the sampled image of the
     approximation error. The far-field concentration of the images of the representatives is consistent with the
     growth for large r of the weight ratio `(1 + u)(1 + u^2)^{3/2}/(L^2 u^2)` stated above, but does not isolate the
     contribution of that weight. The linear sampling map `h -> ((L h)_N(t_i))_{i,N}` has rank at most
     `467 * 40 = 18680`, and the difference rows are linear combinations of its value rows; so any linear space of
     sufficiently regular admissible functions of larger dimension, on which these evaluations are defined, contains a
     nonzero function with zero sampled image (which does not mean `L h = 0`), and a positive finite-section minimum
     is a property of the restriction to the retained span. The comparison uses K_num. The exact tangent K satisfies
     `J(K) = -2`. No sampled-image estimate is obtained for normalized replacements with `J(h) = 0`, and no coercivity
     estimate for the continuous operator in X follows. The verifier proved that for a nonzero vector v and an exact
     orthogonal projection P in a Hilbert space `||v - P v|| / ||v|| = (1 - ||P v||^2 / ||v||^2)^{1/2}`, and, reading
     the saved floating energies as exact dyadic numbers, enclosed the scalar expression
     `100 (1 - E_proj / E_K)^{1/2}` in `(1.81776, 1.81779)` for `C^1` joins, `(1.81764, 1.81766)` for `C^0` joins and
     `(1.76198, 1.76201)` with the free tail columns (in percent); these are intervals for arithmetic on saved
     floating numbers, not enclosures of projection errors, and the angle-refined distance is not covered. These
     scalar interval checks certify no Gram matrix, projection, operator image, quadrature error or bound for the
     omitted radial contributions to the diagnostic norms.
   - Nonlinear counterpart (verified, conditional on an exact profile; with its own proof, the two-scale compact
     stream function by exact piecewise Green integration and by an independent exact radial matching solve, and two
     interval evaluations of one constant; also checked by a separate referee review). Fix `L > 0` and `0 < k < 1`,
     and suppose that an exact profile rho_* exists: even in x, odd in y, locally `C^{2,alpha}` for some `alpha > 0`,
     `rho_* = x^2 y a` with a continuous and even in both variables and `a(0) = 1`, `|D^j rho_*| <= A r^{3-j}` for
     `r <= 1` and `|D^j rho_*| <= D r^{k-j}` for `r >= 1` (`j = 0, 1, 2`, finite A and D), with a locally `C^1`,
     divergence-free canonical velocity of the prescribed parity and sublinear growth at infinity, exponent
     `c_l = 1/k` and `F(rho_*) = 0` pointwise; no such profile is constructed here. F is taken on the unnormalized
     kinematic class: densities of the same parity, locally `C^{2,beta}` for some `beta > 0`, with a continuous
     even-even centre factor of any finite value, a canonical sublinear velocity with finite strain, and sublinear
     growth of the density and its gradient; so `F(rho_s)` and the linearization `L_s` at `rho_s` below are defined.
     The comparison class consists of the q in this class with `J(q) = 1`, `c[q] = c[rho_*]`, and `q - rho_*` and
     `F(q)` in X. A residual-to-error modulus is a map `omega: [0, infinity) -> [0, infinity)` with `omega(0) = 0` and
     `omega(t) -> 0` as `t -> 0` (no monotonicity is required). For every `eta > 0` there are `q_delta` in the
     comparison class with `0 < ||q_delta - rho_*||_X < eta`, `||F(q_delta)||_X -> 0` and
     `||q_delta - rho_*||_X -> d_s > 0`. Indeed, the dilate `rho_s = s rho_*(X/s)` with a fixed `s != 1` close to 1 is
     an exact solution with the same strain and `J(rho_s) = s^{-2}`, and `q_delta = rho_s + (1 - s^{-2}) b_delta` has
     `J = 1`. The compact-bump graph estimate applies at `rho_s` (its centre coefficient need not be 1) and gives
     `||b_delta||_X + ||L_s b_delta||_X -> 0`, the strain term of `L_s b_delta` vanishing since `c[b_delta] = 0`. Then
     `F(q_delta) = (1 - s^{-2}) L_s b_delta + (1 - s^{-2})^2 U[b_delta].grad b_delta`, and
     `||U[b_delta].grad b_delta||_X < 6.8e9 sqrt(pi C_w) delta^3` for `0 < delta <= 1/2`,
     `C_w = L^6 (1 + L^{-2})^{3/2-k}` (a bound for this explicit compact family only, not a bilinear estimate on X).
     Hence no residual-to-error modulus omega gives `||q - rho_*||_X <= omega(||F(q)||_X)` for all q of the comparison
     class in any X-neighbourhood of rho_*; in particular no finite C gives `||q - rho_*||_X <= C ||F(q)||_X`
     throughout such a neighbourhood. This concerns the distance to the chosen exact profile in the stated comparison
     class. It does not rule out residual bounds for the distance to a solution set: `q_delta -> rho_s` in X, where
     `F(rho_s) = 0` but `J(rho_s) = s^{-2} != 1`, so the distance of `q_delta` to the unnormalized solution set tends
     to 0, and nothing follows for the distance to the normalized solution set. Error bounds in a stronger norm
     controlling the centre factor, or for a comparison class with a prescribed leading far coefficient when such a
     coefficient is defined (if `rho_* = r^k Theta + o(r^k)` with Theta not identically zero, then
     `rho_s = s^{1-k} r^k Theta + o(r^k)`, so such a class excludes `rho_s` and `q_delta`), the existence of rho_* and
     the non-stationary trial are not covered; this is not an exclusion.
   - Quadratic term in X alone (verified, with its own proof: exact symbolic Green integration and a separate rational
     radial ODE solve with Cartesian convolution agree on all 451 Cartesian coefficients across H, its stream
     function, both velocity components, the unit advective polynomial `Q_H` and its two first derivatives; two exact
     moment formulas give the same positive gradient energy, separately enclosed by two interval methods; also checked
     in two completed referee reviews, one wording about packet distances corrected without change to any formula). No
     background profile is involved. With `H(Z) = Z_1^2 Z_2 (1 - |Z|^2)_+^6` (so `h_delta(X) = delta^3 H(X/delta)`),
     `epsilon = 1/n^2` and `a = 1/n`, `n >= 2`, the four packets `P_n = a sum_p H((X - p)/epsilon)` over
     `p = (+-4, +-4)` have `J(P_n) = 0` and `c[P_n] = -a epsilon^3/172032` exactly, and with the fixed compact
     compensator `g = -(56/3)(h_1 - h_2)` (`J(g) = 0`, `c[g] = 1`) the densities `h_n = P_n + (a epsilon^3/172032) g`
     are of class `C^5`, compactly supported, with a continuous even-even centre factor and `J(h_n) = c[h_n] = 0`, and
     satisfy `||h_n||_X <= C a -> 0` and `liminf ||W[h_n].grad h_n||_X > 0`. On the patch `|Z| <= 1/2` about one
     packet, `(W[h_n].grad h_n)(p + epsilon Z) = Q_H(Z) + O(epsilon^3)` in `C^1` of that disc with respect to Z, with
     `Q_H = U[H].grad H = -(1/56) Z_1^2 Z_2 + O(|Z|^5)` (the velocity operator has order zero and `a^2 = epsilon`);
     the factors `epsilon^{-2}` of the squared gradient and `epsilon^2` of the area cancel, and the gradient energy of
     `Q_H` on the disc `|Z| <= 1/2` is positive. Hence the quadratic map is not continuous at 0 in X, and no estimate
     `||W[h].grad h||_X <= C ||h||_X^2` holds on any X-ball of positive radius about 0 in this class. This concerns
     the X-to-X estimate only: estimates with h in a stronger norm (as in the two-norm theorem of section 7) or in a
     graph norm (but see the next bullet), with the quadratic term in a weaker norm, or on a restricted
     finite-dimensional class are not covered, and nothing is asserted about linearized residuals, profiles, inverses
     or endpoints.
   - Quadratic term in the diagnostic graph norm (verified, with its own proof: the axis strain of the translated
     packets by symbolic and by exact rational quotient differentiation, all seven numerator coefficients compared;
     the inherited exact gradient energy of the previous bullet re-summed by two exact rational moment formulas; also
     checked in two completed referee reviews and separate adjudications). Let X and the background hypotheses be
     those of the normalization bullet above, with the parities and canonical inverse of section 2. Assume in addition
     that the transport field `V = c_l X + U[rho]` is locally `C^1` on `R^2` and satisfies `V(P) = 0` for
     `P = (p, 0)`, `p > 4`; parity also gives `V(-P) = 0`. Use the decaying canonical velocity for compact
     perturbations. With H, `epsilon = 1/n^2`, `a = 1/n` and the compensator g of the previous bullet, the two packets
     `P_n = a [H((X - P)/epsilon) + H((X + P)/epsilon)]` have `J(P_n) = 0` and
     `c[P_n] = sigma_n = (a/336)(epsilon^3/p^4 + epsilon^5/p^6)` exactly, and the compact `C^5` densities
     `h_n = P_n - sigma_n g` have `J(h_n) = c[h_n] = 0`, `||h_n||_X + ||L h_n||_X <= C a -> 0` and
     `liminf ||W[h_n].grad h_n||_X^2 >= p^2 w(p) E_H > 0`, where `w(r) = L^6 r^{-6} (1 + r^2/L^2)^{3/2 - k}` is the
     weight of X and `E_H` is the positive gradient energy of `Q_H` on `|Z| <= 1/2`. In the graph bound,
     `V = O(epsilon)` on each packet support (V vanishes at the packet centre and DV is bounded nearby), so
     `V.grad P_n - P_n` and its gradient are `O(a)` and `O(a/epsilon)` on supports of area `O(epsilon^2)`; the
     nonlocal term `U[P_n].grad rho` is bounded by `C a` in X over the whole plane (on the packets, in shells about
     them, near the centre and at infinity), and the strain terms cancel exactly. Hence the quadratic term is not
     continuous at 0 in this graph norm on any domain containing these densities, and no estimate
     `||W[h].grad h||_X <= C (||h||_X + ||L h||_X)^2` holds on any graph ball of positive radius about 0 in a
     constrained perturbation domain containing these densities. For the residual statement assume also that the
     background exponent satisfies `c_l = (1 + c[rho])/3`. For compact h define
     `c_l[rho + h] = (1 + c[rho] + c[h])/3`, as in section 2. Canonical linearity gives `U[rho + h] = U[rho] + U[h]`,
     and therefore `F(rho + h_n) - F(rho) = L h_n + W[h_n].grad h_n`. Consequently
     `liminf ||F(rho + h_n) - F(rho)||_X >= sqrt(p^2 w(p) E_H) > 0`. This assertion concerns the residual difference
     and does not require the two residuals separately to belong to X. The exactly normalized modal trial is an
     instance: it satisfies the background hypotheses (scaling-tangent bullet above), and its transport field vanishes
     at its source `P = (p, 0)`, p the exact root in the verified bracket of 5(o), so `p > 43/5 = 8.6` (exact). This
     concerns this weak graph norm only: stronger Sobolev graph norms, the norms of the proposed realization (item 2
     below), a weaker image norm, restricted finite-dimensional families, inverse estimates and endpoints are not
     covered.
   - For the tail-profile column the relevant test is the transversality `ell_0(b) != 0` of the proposed realization
     below, not the angular coefficient of the column (an explicit tail profile with nonzero `cos^4 theta` coefficient
     has zero `x^4` jet at the y-axis).
2. Proposed realization (a proposal of this analysis, audited twice by a separate referee; its far-domain facts and
   its diagonal jet rows are verified, 5(m); the realization as a whole is not verified, its nonlinear map is not
   constructed (section 7 applies only after it is), and nothing below is claimed as a result).
   - Unknowns: `h = chi (x^2 a_2(y) + x^4 a_4(y)) + h_R`, the far scalar kappa of a log-tail direction
     `chi r^k log r Theta_0`, and the amplitude tau of a fixed tail profile `chi r^k Theta_1` (not proportional to
     `Theta_0`: proportionality admits the scaling direction if its remainder lies in the graph domain). The problem
     is solved without the normalization `a(0) = 1` and normalized afterwards by exact scaling.
   - Spaces: the jets carry one-dimensional norms (`H^{s'}_y` near 0, with local order `s' > p_2 + 1/2` so that the
     mode `y^{p_2}` is excluded, weight `<y>^{4j + 1 - 2 gamma'}` at infinity); `h_R` lies in a b-type space near the
     y-axis with weight `|x|^{-2a} (1 + (r/L_w)^2)^{a - gamma'} e^{+phi}`, where `V.grad phi >= 2 (E + kappa_0)^+` and
     E is the pointwise principal energy rate of the transport part in the norm without the factor `e^{phi}` (so the
     weighted rate is at most `-kappa_0`), at `a = 6.0`, `s = 3.06`, `gamma' = 1.129`; L acts on a graph domain, since
     transport loses a derivative. The target satisfies `[x^2 y] f = 0`, which holds identically for `L h`.
   - Conditional count 0: the `a_2` row is solvable from infinity with the single local condition `[x^2 y] f = 0` (the
     coupling terms cancel in that coefficient), the `a_4` row has one condition given by the regularized functional
     `int_0^inf (F - T_2 S_F)/(v H_2)`, and tau balances it. Invertibility then requires `ell_0(b) != 0` after
     eliminating kappa, for the cokernel functional `ell_0` of the reduced operator (5(m); ell is reserved for the
     exponent derivative of 5(h)). The verified row conditions are diagonal (5(m)); the coupled count is not verified.
   - Constants of the closing inequality, none bounded: diagonal inverses `C_J` (jets) and `C_R` (remainder), their
     perturbations `eps_JJ`, `eps_RR`, the off-diagonal couplings `C_JR`, `C_RJ` (no triangular structure), and the
     Schur constant `C_S`; the reduced condition is `C_J C_R C_JR C_RJ < (1 - C_J eps_JJ)(1 - C_R eps_RR)`, together
     with `C_J eps_JJ < 1`, `C_R eps_RR < 1`, two-sided (not only one-sided) diagonal inverses, `m != 0` for the
     elimination of kappa, and a quantitative lower bound for `|ell_0(b)|`.
   - Floating-point principal rates at `L_w/L` in `{0.5, 1}` (not certified): at most -2.27 for `r < 0.1`, -0.55 on
     the y-axis, -2.23 within distance 1 of P and -0.281 in the far field; positive off the axes (maximum 8.9-10.4),
     on part of the incoming x-axis and, at `L_w/L = 0.5`, partly in `0.1 <= r < 1`; orbit costs with margin
     `kappa_0 = 0.1` of 7.3-9.0, so the norm comparison alone loses a factor 39-91. A hypothetical target `K_H` of
     `1e3` to `1e4` (a referee's planning figure) would require quantitative source, matching, coupling and Schur
     estimates; no present calculation shows that it is attainable.
   - Missing analysis: the projected velocity estimate near the y-axis and the corner, the jet-extension transition,
     the matching of the local source estimate with the nonlocal term retained (5(o), available at the proposed order
     `s = 3.06` with `K_1 < 0.313753`; the pure-transport inverse is not regular at P when `mu_P = 1`) to the outer
     weighted estimate, the remaining local constants and their uniformity, uniformity at the far corner, the Fredholm
     property and a validated nonzero Schur complement.
   - Requirements on the trial: in the annular radial test (the norm `N_{a,s}` of 5(n)), a non-polynomial homogeneous
     term `r^m E(theta)` near 0 is admissible only for `m > a + s - 1 = 8.06` (the present trial has `m = 5`);
     applying this test to the fractional realization proposed here needs an equivalence or embedding theorem that is
     open. The residual must also be small in `H^s` near P. The norm also detects polynomial terms: a homogeneous
     polynomial of degree m has finite `N_{a,s}` only if `m > 8.06`, so a density beginning with `x^2 y` has infinite
     `N_{a,s}`, and the test applies to a remainder after subtraction of the Taylor polynomial through degree 8 (jets
     that the realization must carry as separate unknowns or project out; these projections and their boundedness are
     open). The numerical team's second trial passes the test for its non-polynomial terms (verified exactly for the
     inspected density: after canonical exact normalization its density and its local residual have first
     non-polynomial homogeneity 13, the residual statement being conditional on a canonical exactly normalized
     completion; local factor of class `C^9` but not `C^10`, density of class `C^12` but not `C^13` at the centre; no
     claim of high regularity across its `C^6` spline joins). This does not establish membership in the global spaces
     or a residual norm bound. Its exterior velocity is not exactly that of the first trial (the canonical exterior
     stream coefficient changes by a nonzero amount at frequency 522), and its normalization and residual bounds are
     not established.
   - Lower-order variant (proposal; not used in any conclusion; the obstructions quoted here are verified, 5(n)).
     Lowering the local order to `2 < s < 3` lowers the trial's residual norms near P (floating point, numerical team:
     on the disc of radius 0.5, `H^2` 7.3e-3, `H^{2.5}` 7.4e-2, `H^3` 0.89) and the orbit-cost factor (11-21 at
     `s = 2.5`, floating point), and keeps the corner window (`a = 5`, rate -4.08 at `s = 2.5`). A `C^{2,alpha}`
     conclusion then needs a separate regularity upgrade, which does not follow from local information: for the frozen
     source operator, `H_n = sum_j b_j |s|^{p + 2j} y^{n - 2j}` with `p = (g + 1 - n)/A` and an explicit recurrence
     for `b_j` satisfies `-Lap L_P H_n = 0`, so a localization of `H_n` has smooth forcing near P while it lies in
     `H^t` only for `t < p + 1/2` (`n = 7`: in `H^{2.5}`, not in `H^{3.1}`; `n = 11`: not `C^2`). Also the strain
     functional c is unbounded on the unweighted space `H^{s - 1}` when `s < 3` (dilates `eps^{s-2} phi(X/eps)`), and
     the centre condition `m > a + s - 1` (6.5 at `s = 2.5`, `a = 5`) still fails for the present trial. The upgrade
     would need a global tame estimate in the same realization at both orders.
3. Assemble the local pieces. Verified so far: the bounded-collar lemma at the x-axis (5(i)), the structural part at
   the y-axis (5(j)), and at the corner the coefficients, the double remainder, the annular traces and the local
   coupling for a `C^8` factor (5(k)). The y-axis near/far bounds and the singular structure at P are referee-audited
   but not verified (section 4). The corner part needs a background whose factor is smooth at the origin to high
   order, which the present trial is not (section 4). Still needed: the transition from the P disc to the collars, the
   conic region at large r (summation over annuli), and the derivative versions.
4. Fredholm estimate for the assembled realization, then `C_B`, `C_V` in it. A global analysis of the characteristic
   flow of V (no periodic orbits, every orbit in the open quadrant emanating from P and leaving to infinity, uniformly
   bounded transit outside neighbourhoods of 0, P and infinity, supremum and weighted `L^2` inverses of `V.grad - 1`
   along orbits, and construction of weights from orbit-segment costs) has been written and referee-audited; its
   transport part is verified as a conditional statement (5(l)), and for the trial the exterior hypothesis and the
   flow margins on the inner disc and on the far tail are certified (5(l)). The hypotheses on the finite annulus
   `e^{t_a} < r < e^{t_b + 5}` still require certification (of the numerical flow certificate for them, the radial
   modal Taylor models on the middle cells are verified with their canonical meaning; the angular linkage beyond nine
   rectangles, the products and the flow inequalities are not). The transport bound does not extend automatically to
   the axis jets (verified, 5(l)): the x-axis jet equation `w b' + (mu - 1) b = f_y` forces `(mu_P - 1) b(P) = f_y(P)`
   at P, so with `mu_P = 1` (exact solutions with `rho_y(P) != 0`) the jet transport is not onto, and the P-row must
   be carried by the nonlocal coupling; at the corner the cubic coefficient carries the factor `-2A + D - 1 = 0`, a
   compatibility condition.
5. A trial of finite centre regularity (for example, an inner expansion in which angular mode m enters at order
   `r^{2 min(m, 5)}` in the factor; this gives a factor of finite smoothness at 0, not a `P_infty` trial), then a
   certified residual in the norm of step 4. The numerical team's second trial (step 2) has the required centre
   homogeneity; no certified residual for it is available.
