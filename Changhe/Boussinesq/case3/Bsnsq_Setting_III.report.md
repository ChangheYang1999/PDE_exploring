UNRESOLVED: investigation stopped at the 48-hour wall-clock cap; required active duration unverified

Solution class to which this headline applies: class A of section 1 (stated in full in section 3), the smooth
whole-plane profiles (Theta, Omega, beta), beta > 0, of the moving-center system (B2-P) with Theta even and Omega odd
in x, no symmetry in y, Theta = a0 x^2 + O(|X|^3) with a0 != 0 and Theta(0,y) = 0, polynomially growing Theta,
vorticity with a uniform power decay |Omega| <= C(1+|X|)^{-delta} for some delta > 0, and the canonical whole-plane
velocity U = o(|X|). There is no profile with beta < 2 (4.2). By 4.15 this is the class of all smooth B2 profiles with
U = o(|X|) and polynomially bounded vorticity, and at beta = 2 the class of all smooth B2 profiles with U = o(|X|).
Neither accepted endpoint has been reached: no rigorous nonexistence theorem covers class A, and no computed state is
an independently validated numerical profile. The restricted theorems of section 4 hold under the hypotheses stated
with each.

# Full-plane 2D inviscid Boussinesq, Setting B2 (x-reflection symmetry only, moving material center)

## Summary for the reader

Status: UNRESOLVED (final). Neither endpoint was reached. NO: no theorem excludes every class A profile with beta >= 2.
YES: no computed state solves the unforced system (B2-P) to small independent residuals. The analytic results below
have written proof arguments and recorded independent reviews; the numerical values have independent evaluations.
Numerical evidence is not a proof. The analytic results are restricted or necessary-condition results, none a NO endpoint.

- Range: if 0 < beta < 2, every continuous Theta transported by a C^1 field W = beta X + o(|X|) vanishes, with no parity
  or tail hypotheses (4.2); bounded nonzero temperature forces beta = 2 (4.3, 4.4). Class A is the broad target:
  sublinear velocity and polynomially bounded vorticity imply its bounds, and at beta = 2 sublinear velocity alone (4.15).
- Far field of every class A profile: Omega = r^{-1/beta}(a(theta) + o(1)) with a continuous and not identically zero;
  faster tails are excluded; Omega is in no L^p, 1 <= p <= 2 beta, Theta in no L^p, 0 < p < infinity; the drift
  integral never converges absolutely, so only U - U(0) is determined (4.5, 4.8, 4.9, 4.11, 4.12). No profile is
  exactly homogeneous outside a ball (4.25). The leading tails fix the second and, for beta > 2, the third terms (4.16,
  4.26(a)); for 2 < beta <= 3 a constant velocity given by a global integral enters (4.26(b), 4.27); for beta > 2 off
  explicit countable sets the exterior dipole coefficient and the renormalized energy vanish (4.36 to 4.38).
- Structure: for beta > 2, Theta = a0 xi^2 on the basin of the center and sup_{|X|=r} |Theta| ~ r^{1-2/beta} (4.3,
  4.10). For irrational beta and beta = P/Q in lowest terms with P, Q odd, a zero of the axis velocity nearest to the
  center, if any, is degenerate (4.13). No temperature is a polynomial in x of bounded degree with y-dependent
  coefficients (4.39(a)) or of the form H(x/rho(y)) near the whole axis (4.43). At beta = 2 (4.7): no profile has U real
  analytic near an endpoint of the zero arc of W through the center; near an endpoint the vorticity and velocity are in
  no quasianalytic Denjoy-Carleman class, and at the endpoints of 4.7(xix), (xx) in no Gevrey class of order <= 2.
  Near a finite end of the component of {Theta_xx(0, .) != 0} containing 0 at which W_2(0, .) has a simple zero, Theta
  and Omega factor as in 4.59, 4.60.
- Consistency (beta > 2): fields that are not profiles satisfy (T) on R^2, the center data, the canonical inverse and the
  slow tail together with (V) to all orders at the center, or exactly on any disk, or on a disk and outside a ball
  (4.28 to 4.34). An obstruction cannot come from those conditions alone.
- Best numerical evidence (6.1): approximate solutions of forced problems only. Along a forcing homotopy from
  lambda = 0.99 to 0.94 (lambda = 0 is (B2-P); beta 3.002 to 3.024) the forced residual ratios fall with resolution,
  but independently evaluated (B2-P) maximal residual ratios stay at 0.74 to 0.75 (temperature) and 0.45 to 0.49
  (vorticity), and absolute temperature residuals are unbounded (exactly nonzero tail coefficients of positive order).
  With beta prescribed up to 3.092, lambda fell only to about 0.9317 while forced residuals grew; a second path stopped
  at lambda = 0.989975, its center temperature residual ratio tending to a limit above 3/5 (exact arithmetic).
- Remaining gap. For NO, the first missing implication is a global obstruction using (V) on all of R^2 with the slow
  tail: for beta > 2, whether (V), (T), the center data and the canonical inverse are compatible on R^2 in class A
  (either vorticity sign; the positive-vorticity and global-source subclasses are also open); for beta = 2, profiles
  whose zero arc through the center has flat endpoints, where the exact local reduction at an outgoing endpoint
  (4.7(xviii)) has neither a known solution nor a known obstruction. For YES, an unforced (lambda = 0) state with small
  independent residuals and a controlled far field is missing.

## Run record

Start time T0 = 2026-10-20T12:44:11Z. End time T_end = 2026-10-22T13:05:25Z, the time at which this report was
finalized. Elapsed wall-clock time from T0 to T_end: 48 h 21 min 14 s. This includes final assembly and does not
establish the requested active-research duration. The run was stopped by its 48-hour wall-clock cap at
2026-10-22T12:44:11Z. The analysis ran in 9 recorded sessions from T0 to 2026-10-22T12:44:01Z (47 h 59 min 50 s after T0); their total is 47 h
55 min 50 s, the remainder being 8 restart gaps of 30 s each. The research text of this report was fixed at
2026-10-22T12:43:20Z, before the cap. After the cap only this summary, this run record, the removal of internal
working references, the assembly of the accompanying artifacts and their description in section 8 were done, with no
new research; the only computation run was a regeneration of the consolidated residual table from the published files,
which reproduced it byte for byte (section 8). The prompt asked for 48 hours of elapsed active research unless an
endpoint was reached earlier: the full 48-hour wall-clock allowance was used, active research time was not separately
metered, and 48 hours of active research is not claimed. The analysis, the numerical work and the independent
verification had overlapping sessions with their own recorded start and end times. No earlier report on this setting
was published.

## 1. Solution class to which the headline applies

Class A (stated in full in section 3): smooth whole-plane profiles (Theta, Omega, beta), beta > 0, of the
moving-center system (B2-P) with Theta even and Omega odd in x, no symmetry in y, Theta = a0 x^2 + O(|X|^3) with
a0 != 0 and Theta(0,y) = 0, polynomially growing Theta, vorticity with a uniform power
decay |Omega| <= C(1+|X|)^{-delta} for some delta > 0, and the canonical whole-plane velocity law U = o(|X|) (unique
up to a constant; only U - U(0) enters the equations).
Class A coincides with the prompt's broad target (smooth profiles with the stated jet and parity, a canonical
whole-plane velocity with U = o(|X|) and polynomially controlled tails): by 4.15, every smooth B2 profile with
U = o(|X|) and polynomially bounded vorticity, |Omega| <= C(1+|X|)^k for some finite k, is in class A (the decay of
Omega, the bound on Theta and the canonical inverse follow from the equations), and at beta = 2 every smooth B2 profile
with U = o(|X|) is in class A, with no condition on the vorticity. The power decay in the definition of class A is
therefore not an extra restriction. By 4.12, every class A profile in fact has the slow polar vorticity tail Omega = r^{-1/beta}(a(theta) + o(1)),
with a continuous and not identically zero. Every restricted result below states its extra hypotheses explicitly.
This is an equivalence of classes of solutions of (T), (V) and the div-curl system, not of arbitrary fields with the
listed decay; for beta > 2 the polynomial bound on the vorticity is used, and sublinearity is uniform
(sup_{|X|=r} |U - U(0)|/r -> 0 as r -> infinity). Only U_rel = U - U(0) is determined by a profile; for the
reconstruction of a physical solution the observer representative U = U_rel (v0 = 0) is declared, and every other
vertical representative is obtained by the observer change of (A5).

## Detailed summary of findings

Neither endpoint is reached. No theorem here excludes every class A profile with beta >= 2, no profile is constructed,
and no computed state meets the independent residual criteria. Every statement below holds under the hypotheses of
the cited item.
- Exclusions and necessary structure. There is no profile with beta < 2 (4.2). Every class A profile has the slow
  vorticity tail Omega = r^{-1/beta}(a(theta) + o(1)) with a continuous and not identically zero, and every uniformly
  faster tail is excluded; Omega is in no L^p with 1 <= p <= 2 beta and Theta in no L^p with 0 < p < infinity (4.5,
  4.8, 4.9, 4.11, 4.12). The unsubtracted drift integral never converges absolutely, so only U_rel is determined and
  the vertical drift is a gauge ((A5), 4.11). Class A is the broad target class: its decay and growth bounds follow
  from sublinear velocity and polynomially bounded vorticity, and at beta = 2 from sublinear velocity alone (4.15).
- Temperature and axis. For beta > 2, Theta = a0 xi^2 on the basin of the center, and the supremum of |Theta| on the
  circle |X| = r is comparable to r^{1-2/beta} (4.3, 4.10); at beta = 2 Theta is bounded and the zero arc through the
  center has the structure of 4.7. On the invariant axis the second-order data solve a linear system (4.13(i)). At a
  finite nondegenerate zero of the axis velocity b nearest to the center, smoothness forces integrality and parity
  conditions, which fail for irrational beta and for beta = P/Q in lowest terms with P, Q odd; for these beta the
  nearest zero of b on each half-axis, if any, is degenerate, and the profile is in G if every zero of W on the axis
  is nondegenerate or Theta is real analytic near the axis (4.13(ii), (vi), 4.19(e)). The vertical tails are
  determined in 4.21. No temperature is a polynomial in x of bounded degree with coefficients depending on y
  (4.39(a)).
- Axis ratios. For every beta >= 2 the ratios d_x^{2j} Theta(0, y)/Theta_xx(0, y)^j with j = 2 and j = 3 are not both
  constant on the component of {Theta_xx(0, .) != 0} that contains 0 (4.42(b), 4.43); so no temperature has the form
  H(x/rho(y)) with rho > 0 on a neighbourhood of the whole axis (4.7(xxiv), 4.43). For beta > 2 the ratio with j = 2
  has no limit other than 0 in [-infinity, infinity] at an infinite end of that component (4.44, 4.45); for every
  beta >= 2 its absolute value is not bounded below by c |y|^s with c > 0 and s > -1 + 2/beta near such an end
  (4.45); with the same axis relations alone the exponent -1 + 2/beta cannot be improved (4.46), and |y|^{1 - 2/beta}
  times the ratio can diverge like a power of log |y| (4.47); at beta = 2, a0 times the ratio with j = 2 does not
  tend to +infinity at such an end (4.47). For class A profiles, which at beta = 2 are all smooth B2 profiles with
  sublinear velocity (4.15), |y|^{(j - 1)(1 - 2/beta)} times the ratio with index j has a finite limit at such an end
  for every j >= 2 (4.48); so this logarithmic divergence does not occur for them, and at beta = 2 every ratio has a
  finite limit. Whether that component can be bounded is not decided: smooth fields of compact support with the
  canonical inverse, which are not profiles, satisfy (T) and (V) to every order on the axis with the component
  (-3, 3), and a0 times the ratio with j = 2 tends to -infinity at both of its ends (4.49); the same holds with (T)
  on all of R^2, for fields with Psi and Omega of compact support that are again not profiles (4.50). For a profile,
  a0 times that ratio tends to -infinity at every finite end of that component at which W_2(0, .) vanishes to a
  finite order p >= 2, and d_x^4 Theta(0, y)/Theta_xx(0, y) is asymptotic to a negative multiple, fixed by beta and
  p, of the inverse square of the distance to that end (4.51). At an end at which W_2(0, .) vanishes to infinite
  order, the axis relations used for 4.51 force no sign of a0 times the ratio with j = 2 (4.52). At an end at which
  W_2(0, .) has a simple zero, that ratio has a limit in [-infinity, infinity], and the same relations allow every
  finite and both infinite limits, at beta = 2 also with the signs and integrality required of a profile (4.53); at
  beta = 2 the same holds when the relation for d_x^3 Omega(0, .) on the axis is added (4.54), and in the family of
  4.54 (a) the axis relations of every order can be met near the end by formal series in x whose coefficients are real
  analytic on one interval about the end, two free constants being fixed at each order (4.55, 4.56), and the formal
  temperature series of that family is c x^2 times the tenth power of a formal series in x^2 and y_* - y, with a
  constant c != 0 (4.57, 4.58). For a profile, near (0, y_*) at a finite end y_* of that component at which W_2(0, .)
  has a simple zero, Theta = c_1 x^2 phi^n and Omega = c_2 x phi^m Y, where c_1 and c_2 are nonzero constants of the
  same sign, n > m are integers fixed by beta and the slope of W_2(0, .) at y_*, and n - m is even, Y is smooth and
  positive, and phi is smooth, has nonzero gradient on its zero set, and vanishes exactly on the local unstable
  manifold of the zero (0, y_*) of W, a smooth curve through (0, y_*) symmetric under x -> -x; so there Theta and
  Omega vanish exactly on the axis and on that curve, and x Omega Theta > 0 off them (4.59, 4.60).
- Far field and identities. The leading vorticity and temperature tails determine the second terms (4.16) and, for
  beta > 2, the third terms (4.26(a)); for 2 < beta <= 3 the next terms involve in addition a constant velocity C
  given by a global integral (4.26(b), 4.27); and no profile is exactly homogeneous outside a ball (4.25). The
  equations are equivalent to a family of homogeneous-weight identities; the strain identity among them has no sign
  and is consistent with the sign, center and decay conditions (4.23). For beta > 2 the exterior fields of a class A
  profile have finite power-logarithmic expansions through the dipole term (4.37); for beta outside explicit countable
  sets its exterior dipole coefficient (the renormalized impulse) and its renormalized energy vanish (4.36 to 4.38);
  these necessary conditions do not decide existence.
- Global-source subclass G (beta > 2, the center the only zero of W): a global area-preserving normal form, two
  excluded shape classes of vorticity, the temperature tail and the axis subsystem (4.18, 4.21, 4.22, 4.35).
- Consistency of partial conditions (beta > 2). Configurations that satisfy (T) exactly on R^2, positivity, the center
  data, the canonical inverse and the slow tail can also satisfy: (V) to all orders at the center (4.28); (V) exactly
  on any prescribed disk with every derivative of the residual of (V) zero at every point of the axis (4.29 to 4.31);
  (V) exactly on a prescribed disk and outside a large ball, with a nonzero compactly supported residual (4.34); if
  the vorticity may change sign, also with vanishing affine moments of that residual, a vanishing exterior dipole
  coefficient (beta not in Z_crit) and any prescribed real value of the renormalized energy (6.3). None of them is a
  profile (4.32). A horizontal primitive reformulation gives one scalar equation for Psi and necessary angular
  cancellation and horizontal-offset conditions (4.33). For beta > 2 the compatibility identity E_comp = 0, necessary
  for every profile, is also sufficient, for a stream odd in x with Psi_xy(0) = 1 + beta/2, for (T) and (V) with the
  normalized primitive near the center when Psi_xxx(0) != 0, and on R^2 for real analytic streams with sublinear
  velocity (4.32(d)).
- Open core. For beta > 2, the slow-tail branch: whether (V), (T), the center data and the canonical inverse are
  compatible on all of R^2 in class A, with vorticity of either sign, including the positive-vorticity subclass and G.
  For beta = 2, smooth profiles whose zero arc through the center has flat endpoints (4.7(iii), 6.3). At beta = 2,
  configurations that are not profiles satisfy (T) on R^2, the center data, the canonical inverse and (V) near the
  center and on an open neighbourhood of the open zero arc, with flat endpoints as in 4.7(iii); they can be chosen
  with strong unstable curves at the endpoints that agree with no real analytic curve germ, as 4.7(vi) requires, and
  in addition with Theta constant and Omega = 0 on open sets adjacent to the endpoints (6.3).

  Write Z = {W = 0}, gamma for its component through the center, p_+ and its mirror image p_- for the endpoints of
  gamma, and L = Theta(p_+) = Theta(p_-). No profile has U real analytic on a neighbourhood of an endpoint
  (4.7(xii)(a)) or Theta constant on a neighbourhood of an endpoint (4.7(xxi)). At an outgoing endpoint, U real
  analytic along the normal line through it together with Omega real analytic along the nearby parallel lines beyond
  it is impossible (4.7(xii)(c)), and so is a representation of W, on the side of the strong unstable curve beyond it,
  as a finite sum of products a_j(s) B_j(z) in the coordinates (s, z) of 4.7(iv) with the coefficient regularity of
  4.7(xii)(d). At every endpoint, Theta - L and Omega vanish to every order along the strong unstable curve, whose
  Taylor series is determined by that of the curvature of the zero curve. If the strong unstable curve meets the side
  beyond the endpoint in every neighbourhood of the endpoint, in particular if some odd-order derivative of the
  curvature there is nonzero, the transverse analyticity excluded in 4.7(xii)(c) is impossible at that endpoint as
  well. Incoming endpoints force zeros of W off gamma (4.7(xiii)). If the endpoints are incoming and these zeros are
  isolated, then near each endpoint Theta = L and Omega = 0 on the side of the strong unstable curve beyond it, the
  transverse analyticity of 4.7(xii)(c) is impossible at the endpoints with no condition on the strong unstable curve,
  and that curve is not real analytic at the endpoints. If, in addition, these zeros are nondegenerate, the center is
  the only zero of W on the axis (4.7(xiv)). If some neighbourhood of an accumulating endpoint contains no arc of
  zeros of W off gamma, the zeros off gamma near it are isolated, Theta = L and Omega = 0 on the side of the strong
  unstable curve beyond it near it, and, as at incoming endpoints, the transverse analyticity of 4.7(xii)(c) is
  impossible there and the strong unstable curve is not real analytic there (4.7(xx)). No profile has Theta constant
  on a nondegenerate straight segment of zeros of W. Suppose Theta = L on a nondegenerate subarc of gamma ending at an
  endpoint p. Then Theta = L and Omega = 0 near p on the strong unstable curve and on its side containing gamma. Such
  p must be incoming with at least one nonisolated zero of W off gamma, or accumulating with an arc of zeros of W off
  gamma in every neighbourhood of p. In the incoming case, Theta is constant on no neighbourhood of any point of the
  exterior center branch. In the accumulating case, every neighbourhood of p contains an arc of zeros of W off gamma
  on which Theta is not constant (4.7(xxii)). At an outgoing endpoint, and at an incoming one when every zero of W off
  gamma is isolated, neither Theta - L nor Omega vanishes identically on a neighbourhood of any point of the orbits of
  the strong unstable curve, so U is not harmonic near any such point (4.7(xv)(a), (b)).

  When Z = gamma, let C^_+ be the union of p_+ and its two strong unstable orbits, and C^_- its mirror image. These
  are disjoint properly embedded lines, and their complement has exactly three components, each simply connected: the
  open parts O_+ and O_- of the basins of p_+ and p_- (the points not on C^_+ whose backward limit is p_+, and their
  mirror images), with boundaries C^_+ and C^_-, and a region F containing the axis. O_+ and O_- are components of the
  interior of {Omega = 0} and of the interior of {Theta = L}, and Theta = L and Omega = 0 outside F (4.7(xv)(c),
  (xvi)).

  Near each endpoint, neither the vorticity nor the velocity of a profile is in any quasianalytic Denjoy-Carleman
  class C{m} of 4.7(xvii) (m_k = k! gives the real analytic functions), and the temperature is in no such class on a
  connected open set containing gamma (4.7(xvii)). At an outgoing endpoint, and at an incoming one when the zeros of W
  off gamma are isolated, the same holds near every point of the orbits of the strong unstable curve (4.7(xvii)(c)).
  Fix a family of parallel lines transverse to an arc of these orbits. Outside one meager set of lines, the same for
  all these classes, the restrictions of Theta - L and Omega to the lines are flat nonzero germs, hence in no such
  class. For each class, outside a meager set of lines that may depend on the class, the restrictions of the velocity
  are not in that class near the arc (4.7(xvii)(d)). Let p be an outgoing endpoint, an incoming endpoint when the
  zeros of W off gamma are isolated, or an accumulating endpoint some neighbourhood of which contains no arc of zeros
  of W off gamma. Then neither the velocity on the side of the strong unstable curve beyond p, uniformly up to p, nor
  the vorticity on a neighbourhood of p satisfies bounds c A^n (n!)^2 for its derivatives of order n in one fixed
  direction. In particular neither U nor Omega is in a Gevrey class of order at most 2 on a neighbourhood of p; when
  Z = gamma, this holds at both endpoints (4.7(xix), (xx)(d)). Gevrey orders greater than 2 are not excluded.

  Near an outgoing endpoint the equations reduce exactly, with a converse, to one curl equation for a normal form of
  the flow on the closed side of the strong unstable curve that contains gamma and to a one-sided Cauchy problem for a
  potential of W on the basin side, with the full gradient prescribed on that curve (4.7(xviii)); neither a local
  solution nor a local obstruction of this reduced problem is known.
- Numerics (6.1, 6.2). The saved states of the numerical continuation are approximate solutions of forced problems.
  Along a forcing homotopy from lambda = 0.99 to 0.94 (beta from 3.002 to 3.024; lambda = 0 is (B2-P)), the forced
  residual ratios of these states fall with resolution, while their (B2-P) maximal residual ratios stay at 0.74 to
  0.75 (temperature) and 0.45 to 0.49 (vorticity), their absolute temperature residuals are unbounded (exactly nonzero
  tail coefficients of positive order), and the discrepancy between the two finest angular resolutions grows along the
  path. Continued at a fixed resolution with beta prescribed (3.024 to 3.062), lambda decreases only to 0.9317, by
  shrinking steps, while the forced residual ratios grow, so the accuracy of these fits deteriorates. At
  beta = 3.0315, 3.04, 3.05 and 3.062 the stored 32- and 40-mode states, obtained with different initial and stopping
  histories, differ in lambda by at most 1.1e-7. The forced ratios of the 40-mode states are smaller by factors of
  about 1.4 to 4. The (B2-P) ratios agree to the displayed precision except the vorticity ratio at beta = 3.062 (0.58
  with 40 and 0.74 with 32 modes, attained beyond r = 300). Their C2 enclosures differ by 0.1, 0.4, 1.0 and 2.4
  percent. Separately, on a common grid, form at each sampled radius the angular maximum of |d_phi G_40 - d_phi G_32|
  divided by the angular maximum of |d_phi G_40|, where G = Omega/x; its maximum over the sampled radii is 0.068,
  0.097, 0.13 and 0.16 at the four values of beta (0.0039 at lambda = 0.95). These are comparisons at four values of
  beta, not a result on the limit of increasing resolution. Continued with 40 modes to beta = 3.076, where no 32-mode
  state was computed, lambda = 0.931657, the forced maxima grow to 0.056/0.12 and the (B2-P) vorticity maximum to
  0.95, attained beyond r = 300; at beta = 3.092, lambda = 0.932671 and the forced maxima are 0.088/0.15. With 48
  modes the stage at beta = 3.076 kept the inherited lambda while changing the fields, and at beta = 3.092
  lambda = 0.932670, 4.8e-7 below the 40-mode value; the forced maxima of these two states are 0.010/0.025 and
  0.020/0.042 and their (B2-P) vorticity maxima beyond r = 300 are 0.30 and 0.70, so the far-field values of the
  40-mode states depend on the resolution. A further 48-mode run of the first path, started from the state at
  beta = 3.092, gives lambda = 0.931658 at beta = 3.076 (5.7e-7 above the 40-mode value) and 0.931683 at 3.062 (7.2e-7
  below it), with forced maxima 0.010/0.025 and 0.0044/0.012. A second path, from a different seed and source, has
  (B2-P) maxima 0.74/0.42 at its first state; at its next stage
  (lambda = 0.98) its seven computed states, recomputed and stored with beta fixed between 2.83 and 3.47, and the one
  state saved by the continuation all fail the center-strain condition on independent evaluation. It was continued
  with beta prescribed from 3.088 to 3.25 (no state was accepted at beta = 3.3) and from 3.088 down to 3.0. Among the
  twenty-four stored states of these two continuations, the smallest stored lambda is 0.989975, at beta = 3.0925 and
  3.095. A further state, used for the Jacobian diagnostic of 6.1, has (beta, lambda) = (3.0952, 0.989973); neither
  observation establishes a fold. At each of the twenty-four stored states, at four states computed with 32 angular
  modes (beta = 3.085, 3.0925, 3.1, 3.11), at five computed with 40 (beta = 3.076, 3.085, 3.0925, 3.1, 3.11) and at
  two computed with 48 (beta = 3.085, 3.1), the normalized (B2-P) temperature residual tends at the center to a limit
  above 3/5 (exact rational arithmetic). Sign-changing two-lobe external sources were sampled at the start of the
  forcing homotopy (6.1): for a weakly signed family the center-strain match is bracketed numerically, and no
  strain-matched sign-changing seed was constructed or continued. The independent fits that target (B2-P) directly
  were all refuted. According to the run records, the original runs of the two paths used 12 Gauss points per radial
  quadrature cell in the computation's inverse; restarted with 48 points, six stored stages accepted their inherited
  lambda, so none was redetermined; solved again from a displaced start with 12 and with 48 points, the 32-mode stage
  at beta = 3.062 gave two values of lambda 1.76e-8 apart, 1.74 times the nominal tolerance scale; without an
  inner-solve error bound or a root enclosure at either order, this establishes neither existence of exact discrete
  roots at both orders nor a difference between them; and at r = 1e9 the maxima from the computation's later 48-point
  evaluations of the stored relative velocities differ from those of an independent full-plane evaluation by 5.8 to 73
  percent for six states (a conditional diagnostic, not an error bound). No state meets the independent residual
  criteria; this concerns the computed states and gives no distance to the solution set.

## 2. Problem statement

Physical system on R^2 (sign convention of the problem):
  w_t + u.grad w = d_{z1} theta,  theta_t + u.grad theta = 0,  u = (-psi_{z2}, psi_{z1}),  -Lap psi = w.
With this convention w = -curl u, where curl u = d1 u2 - d2 u1.
Ansatz, with tau = T - t and z_c(t) = (0, z_{c,2}(t)) a material point (z_c' = u(t, z_c)):
  X = (z - z_c(t))/tau^beta, w = tau^{-1} Omega(X), theta = tau^{beta-2} Theta(X), u = tau^{beta-1} U(X),
  psi = tau^{2 beta - 1} Psi(X).
The B2 velocity parity gives U_1(0) = 0 (a horizontal constant is incompatible with the reflection), so
v0 = U(0) = (0, v0_2); then z_c' = tau^{beta-1} v0 and
z_c = z_* - v0 tau^beta / beta. Substitution gives the stationary system
  (B2-P)  W.grad Omega + Omega = Theta_x,  W.grad Theta = (beta-2) Theta,  W = beta X + U(X) - U(0),
          -Lap Psi = Omega,  U = (-Psi_y, Psi_x).
The pressure p (used only in (A5)) refers to the momentum form u_t + u.grad u + grad p = -theta e_2, whose negative curl
is the vorticity equation above. Below, (T) denotes the Theta equation and (V) the Omega equation, U_rel = U - U(0), and phi_t is the flow of W.
Elementary facts used throughout: div W = 2 beta, curl W = -Omega, and, by x-reflection symmetry, U_rel,1(0,y) = 0, so
the y-axis is invariant under the flow.

## 3. Admissible class, canonical inverse, gauges

(A1) beta > 0. (A2) Theta smooth, even in x, Theta(0,y) = 0, Theta = a0 x^2 + O(|X|^3), a0 != 0,
|Theta| <= C(1+|X|)^m. (A3) Omega smooth, odd in x, |Omega| <= C(1+|X|)^{-delta}, delta > 0.
(A4) Canonical inverse: U is divergence free with -curl U = Omega and U = o(|X|). Such U is unique up to an additive
constant (the difference of two such fields has harmonic components of sublinear growth, hence is constant by the
interior gradient estimate), so U_rel = U - U(0) is canonical:
  U_rel(X) = int [K(X-Y) - K(-Y)] Omega(Y) dY,  K(Z) = (1/(2 pi)) (Z_2, -Z_1)/|Z|^2,
an absolutely convergent integral under (A3), with |U_rel(X)| <= C(1+|X|)^{1-eps} for some eps > 0. No strain,
harmonic correction, wall or fitted drift is added.
(A5) The drift v0 = U(0) does not enter (B2-P); it is a gauge of (B2-P). If int |Omega(Y)|/(1+|Y|) dY < infinity, one
may select the unsubtracted Biot-Savart representative U_BS = K * Omega, for which
U_BS(0) = (0, (1/(2 pi)) int Y_1 Omega(Y)/|Y|^2 dY); every other admissible velocity differs by a constant. For every
class A profile, 4.8 and 4.9 imply that int |Omega(Y)|/(1+|Y|) dY diverges, and 4.11(ii) shows that even the scalar
vertical component integral int |Y_1 Omega(Y)|/|Y|^2 dY diverges (a property of solutions, not of arbitrary fields: a smooth
odd field concentrated in a parabolic neighbourhood of the y-axis can have divergent mass integral and convergent
component integral). So for class A the unsubtracted representative is not given by an absolutely convergent integral:
the canonical inverse fixes U_rel only, and any numerical value of v0 = U(0) is a declared convention (for example a
renormalized or averaged inverse), not a consequence of (B2-P). Observer change: if (theta, w, u, p) solves the physical
system and a(t) is a C^2 path, then theta(t, z - a(t)), w(t, z - a(t)), u(t, z - a(t)) + a'(t), p(t, z - a(t)) - a''(t).z
is again an exact solution. To preserve the reflection axis and a center of the form (0, z_{c,2}), restrict to vertical
a(t). With a(t) = -v tau^beta / beta (v vertical) the self-similar profile (Theta, Omega, U_rel) is unchanged, U(0)
becomes v0 + v and the center path becomes z_c(t) + a(t). Also, with Y = X - v0/beta, the translated fields
Theta~(Y) = Theta(Y + v0/beta), Omega~(Y) = Omega(Y + v0/beta), U~(Y) = U(Y + v0/beta) solve the fixed-center profile
equations with transport field beta Y + U~(Y) (since W(X) = beta Y + U(Y + v0/beta)); the material point is then
Y = -v0/beta, where the quadratic temperature jet is centered.
Relation to the broad target. (A2) with some m and (A3) with some delta > 0 are not extra restrictions: by 4.15, for
beta >= 2 every smooth profile with the parity and jet of (A2), the velocity law (A4) and polynomially bounded vorticity
|Omega| <= C(1+|X|)^k (any finite k) satisfies (A2) with some m < 1, (A3) with every delta < 1/beta, and the integral
formula of (A4); at beta = 2 no bound on Omega is needed. (For beta < 2 there is no nontrivial profile with U = o(|X|),
4.2.)
(A6) Scaling: Theta_l = l Theta(X/l), Omega_l = Omega(X/l), U_l = l U(X/l), l != 0 real, is an exact symmetry with
a0 -> a0/l (l = -1 is the y-reflection Theta -> -Theta(x,-y), Omega -> -Omega(x,-y)). The normalization a0 = 1 fixes it
completely and excludes no branch.

## 4. Results that have completed verification

The following results have the hypotheses stated individually below. Each was checked by an independent derivation
and by an independent analytic review (section 7); the written proofs of the independent verification are in the
accompanying artifacts (section 8), and the essential steps are given here. A step proved only under an additional hypothesis is marked where
it is used. Unless a result states separate hypotheses, it assumes class A. Then W is smooth and has a complete flow (since
U_rel = o(|X|)), and canonical inversion with Omega odd in x gives U_rel,1 odd and U_rel,2 even in x. (Oddness of Omega
alone would not suffice: a harmonic strain could be added; the sublinear normalization excludes it.)
Notation. a(theta) denotes the angular vorticity tail of 4.12, except in 4.13, 4.18, 4.29, 4.30 and Q2(c), where a(y)
is the axis coefficient Theta_xx(0,y)/2 (written a_ax(y) in 4.7(v) and 4.35); in 4.30, 4.31 and 4.35, where both
occur, the vorticity tail is written a_tail(theta); A(theta) denotes the temperature tail of 4.10 (written h in 4.7,
4.16, 4.21 and 4.22), and A_tr(Y) the trajectory amplitude of 4.6, 4.11 and 4.12; b(y) = W_2(0,y) in 4.13, 4.18, 4.21,
4.29 to 4.32 and 4.35, while in 4.16 and 4.25 b denotes the second vorticity coefficient; d = 1/beta in 4.17,
4.21-4.23 and 4.35, while d = 1/kappa in 4.13(ii) and in 4.16 and 4.25 d denotes the second temperature coefficient;
in 4.24 nu = 1/beta in (a), and the mode coefficients f, g, h, the exponents p, q, the radial function eta and the
constants mu, D, E are local to 4.24; in 4.25, k = 2 - s, and C, D, J, P, Q, e1, e3, sigma, t are local; in 4.26, C is
the constant velocity and k1, k2, f2, eta, c0, c_jn, C2 are local; in 4.27, A2, alpha, g2, B, w2, C, chi, L_chi, zeta,
Q_omega, Q_theta, omega3, theta3, c0, c_+, c_-, p, q, c are local. J_- (v1, v2) = (v2, -v1) and J_+ (v1, v2) = (-v2,
v1) are the rotations by -pi/2 and +pi/2. c denotes the center strain Psi_xy(0) = 1 + beta/2 of 4.1, except in 4.19
and 4.20, where c = beta - 2 is the growth rate in (T), and in 4.27(d), where p, q and c are constants of an example.
m = 1 - 2/beta (the temperature homogeneity) in 4.10 and 4.16, while m is the axis exponent of q in 4.13(ii) and the
weight exponent 2 - 1/beta in 4.23(e). q(y) = Omega_x(0, y) is the axis function of 4.7(v), 4.13, 4.19, 4.29 to 4.32,
4.35 and Q2(c), while q and g in 4.22(d) are angular factors and q = (1 - d)/2 in the proof of the first construction
of 4.23(c) is an exponent (the letters of the third construction are local to it). P and Q are the divided fields of
4.17, except where beta = P/Q in lowest terms (4.13, 4.19, Q1, section 6) and in 4.29 and 4.30, where P is the cubic
polynomial solution of 4.29(a) and Q the bounded axis solution of 4.29(e) and 4.30; in 4.29 the letters K, f0, gamma,
m, nu, t0, R1, Phi, kappa, zeta, eta, chi, N, d, f, u, H, F, G_n and r_n are local, and the letters local to 4.30,
4.31, 4.32 and 4.35 to 4.60 are listed at the end of each. psi(y) in step (4) of the proof of 4.7(v)-(vii) is the axis
value of the scattering map, not a stream function. kappa is the axis eigenvalue -b'(y_*) in 4.13(ii) and the resonant
coefficient in 4.18, 4.22 and 4.35. S is the reflection (x, y) -> (-x, y) in 4.7, 4.21 and 4.22; other auxiliary
letters defined inside an item or a proof step (for example S in 4.13, 4.17, 4.18 and 4.19, F_t in 4.18, F_r in 4.22)
are local to it.

4.1 Center identities. Let c = Psi_xy(0) (equivalently c = (1/pi) int x y Omega / |X|^4 dX, absolutely convergent).
Then W(0) = 0, DW(0) = diag(beta - c, beta + c). Writing b = Omega_x(0), the quadratic part of (T) gives
2(beta - c) = beta - 2 and the linear part of (V) gives (beta - c + 1) b = 2 a0, so
  c = 1 + beta/2,   DW(0) = diag((beta - 2)/2, 1 + 3 beta/2),   Omega = (4 a0 / beta) x + O(|X|^2).
In particular the 2-jet of Theta is a0 x^2 (Theta(0) = 0, grad Theta(0) = 0, Theta_xy(0) = Theta_yy(0) = 0).

4.2 Theorem A (no profile with beta < 2). Let 0 < beta < 2, let W in C^1 satisfy W(X) = beta X + o(|X|), and let Theta be
continuous with Theta(phi_t Y) = e^{(beta-2)t} Theta(Y) (the characteristic form of (T); every C^1 solution of (T)
satisfies it). Then Theta = 0. Hence class A has no member with beta < 2.
Proof. Choose R0 with W(X).X >= (beta/2)|X|^2 for |X| >= R0. Then d/dt |phi_{-t} Y|^2 = -2 W.X < 0 whenever
|phi_{-t} Y| >= R0, so every backward orbit stays in the closed ball of radius max(|Y|, R0). Along it,
Theta(phi_{-t} Y) = e^{(2-beta)t} Theta(Y), and Theta is bounded on the ball, so Theta(Y) = 0. (No decay of Theta, no use
of (V) or of the Biot-Savart law beyond sublinearity.) For Omega, Theta in C^1 satisfying (V), the same
trapping gives Omega(Y) = int_0^infty e^{-t} Theta_x(phi_{-t} Y) dt; so Theta = 0 forces Omega = 0.

4.3 Proposition B (beta > 2, structure). (i) Theta = 0 on K = {Y : forward orbit bounded}; bounded Theta forces
Theta = 0; along escaping orbits Theta(phi_t Y) = e^{(beta-2)t} Theta(Y). (ii) The origin is a hyperbolic source
(eigenvalues (beta-2)/2 < 1 + 3beta/2). On its open, invariant basin of repulsion R(0),
  Theta = a0 xi^2,  where xi is the unique C^1 solution of W.grad xi = ((beta - 2)/2) xi with xi = x + o(|X|),
and xi = 0 exactly on the y-axis within R(0); so Theta has the sign of a0 on R(0) off the axis. A C^2 solution of (T)
on R(0) is determined by its 2-jet. (No global statement about the size of R(0) is made.)
Proof outline. (i) follows from characteristic transport and boundedness on bounded orbits. (ii) Put lambda = (beta-2)/2.
By parity and smoothness W_1 = x(lambda + b(X)) with b smooth, b(0) = 0. Backward orbits near the source satisfy
|phi_{-t} Y| + ||D phi_{-t}(Y)|| <= C_Y e^{-lambda t} (lambda is the smaller eigenvalue), locally uniformly, so
  xi(Y) = lim e^{lambda t} (phi_{-t} Y)_1 = x exp(- int_0^infty b(phi_{-s} Y) ds)
is C^1, satisfies W.grad xi = lambda xi, and vanishes exactly where x = 0. Transporting the Taylor expansion of Theta
backward, Theta(Y) = e^{2 lambda t} Theta(phi_{-t} Y) = e^{2 lambda t}[a0 (phi_{-t} Y)_1^2 + O(e^{-3 lambda t})] -> a0 xi(Y)^2.
For two C^2 solutions with the same 2-jet the difference is o(|X|^2), and multiplying its value along a backward orbit by
e^{2 lambda t} proves uniqueness; the first-order version gives uniqueness of xi.

4.4 Proposition C (beta = 2, local). Theta is constant along orbits and globally bounded (W.X >= |X|^2 outside a large
ball, so every backward orbit enters that ball, and Theta is constant along it). DW(0) = diag(0, 4), and W vanishes
on a C^1 arc through 0 tangent to the x-axis (implicit function theorem on W_2 = 0, then Theta_x != 0 off the axis
forces W_1 = 0 on the arc). On the arc Omega = Theta_x and U_rel = -2X; at each of its points DW has eigenvalues 0, 4.

4.5 Temperature integrability. For every beta > 0 in class A and every 0 < p < infinity, Theta is not in L^p(R^2).
Proof. The flow has Jacobian e^{2 beta s} and Theta o phi_s = e^{(beta-2)s} Theta, so
int |Theta|^p = e^{(2 beta + p(beta - 2)) s} int |Theta|^p for all s. A finite nonzero value forces beta = 2p/(p+2) < 2,
which Theorem A excludes.

4.6 Theorem E (exclusion of integrable vorticity tails, with far-field derivative control). Let beta >= 2, U, Theta,
Omega in C^1 satisfy (T), (V), div U = 0, -curl U = Omega, U = o(|X|), and
  (D) eps(R) := sup_{|Y| >= R} int_0^infty |DU_rel(phi_t Y)| dt -> 0 as R -> infinity
      (implied by the power bounds (H1) |U_rel(X)| <= C|X|^{1-delta}, |DU_rel(X)| <= C|X|^{-delta} for |X| >= 1, some
      delta in (0,1], since then |phi_t Y| >= c e^{beta t}|Y| gives eps(R) <= C R^{-delta});
  (H2) EITHER int |Omega|(1+|X|)^{-gamma} dX < infinity for some gamma <= 2 - 2/beta, OR Omega in L^p for some
       0 < p <= beta.
Then: if beta > 2, Theta = 0 (no reflection symmetry or axis condition needed); if beta = 2, Theta is constant, hence
Theta = 0 under Theta(0,y) = 0. In both cases Omega = 0 and U_rel = 0. In particular, under (D), no member of class A
has an absolutely convergent drift integral int |Omega|/(1+|Y|) dY (gamma = 1 <= 2 - 2/beta), and no member has finite
enstrophy (p = 2).
Proof outline. (1) The set K of bounded forward orbits lies in a ball and has measure zero (|phi_t K| = e^{2 beta t}|K|);
its complement E is open, dense, invariant, and every orbit in E escapes with |phi_t Y| comparable to e^{beta t}
(upper and lower bounds), locally uniformly on E. (2) D phi_t = e^{beta t} N_t with N_t' = DU_rel(phi_t Y) N_t, det N_t = 1;
by (D) and Gronwall N_t -> M_Y locally uniformly on E, with |M_Y - I| <= e^{eps(|Y|)} - 1 for large |Y|. From
D phi_t(Y) W(Y) = W(phi_t Y) one gets e^{-beta t} phi_t(Y) = e^{-beta t} Y + int_0^t e^{-beta(t-s)} N_s(Y) W(Y) ds, so
Phi(Y) = lim e^{-beta t} phi_t(Y) = M_Y W(Y)/beta, D Phi = M, and Phi(Y) = Y + o(|Y|), D Phi(Y) = I + o(1) at infinity;
also |phi_t Y| is comparable to e^{beta t}|Y| for all large |Y| and t >= 0, uniformly. Phi is a C^1 area-preserving
diffeomorphism of E onto R^2 \ {0} with Phi o phi_s = e^{beta s} Phi (exterior injectivity and surjectivity: for large z
the map X -> z - (Phi(X) - X) is a contraction of the ball B(z, |z|/2) into itself; global injectivity and surjectivity by
equivariance; Phi is bounded on bounded subsets of E, through the first exit point of a large transverse circle). (3) F = Theta o Phi^{-1} is C^1 and homogeneous of degree 1 - 2/beta,
and grad Theta(phi_t Y) = e^{-2t}(grad F(Phi(Y)) + o(1)). (4) From (V), along escaping orbits
  Omega(phi_t Y) = e^{-t} A_tr(Y) - e^{-2t}(g(Y) + o(1)),  g = (d_1 F) o Phi,
  A_tr(Y) = Omega(Y) + int_0^infty e^s Theta_x(phi_s Y) ds  (locally uniformly convergent on E),
with A_tr(phi_s Y) = e^{-s} A_tr(Y), g(phi_s Y) = e^{-2s} g(Y) (a trajectory expansion, not a fixed-angle expansion). (5) In escape coordinates (t, sigma), sigma on a large circle S,
dX = e^{2 beta t}(W.n)(sigma) dt dl(sigma); (H2) makes the time integrals of e^{(2 beta - gamma beta) t}|Omega(phi_t sigma)| (or
e^{2 beta t}|Omega|^p) finite for almost every sigma (Tonelli); since (2 - gamma) beta - 1 > 0 and
(2 - gamma) beta - 2 >= 0 (resp. 2 beta - p > 0 and 2 beta - 2p >= 0), the lower bounds |Omega(phi_t sigma)| >= |A_tr| e^{-t}/2
and, when A_tr = 0, >= |g| e^{-2t}/2 for large t force A_tr = 0 and then g = 0 almost everywhere on S, hence everywhere on S by
continuity, hence on E by the transport identities. (6) So d_1 F = 0: F = C_+ |Z_2|^alpha
on Z_2 > 0 and C_- |Z_2|^alpha on Z_2 < 0, alpha = 1 - 2/beta. Continuity and differentiability of F at (1, 0) give
C_+ = C_- = 0 if alpha > 0, and C_+ = C_- if alpha = 0. Then Theta is constant, (V) becomes homogeneous and backward
trapping gives Omega = 0; U_rel is harmonic and sublinear, hence constant, hence 0.
Scope. (D) is NOT implied by smoothness, sublinear growth, the B2 parity and the center data: the bounded shear
U_rel = (0, cos x - 1) (vorticity sin x) has x(t) = e^{beta t} x_0 along its orbits, so
int_0^infty |DU_rel(phi_t Y)| dt = (1/beta) int_{|x_0|}^infty |sin u|/u du = infinity for x_0 != 0, and a compactly
supported correction of the stream function imposes the center data without changing this. Such fields do not solve
(T) and (V). Within class A the profile equations do imply (D), with eps(R) <= C R^{-1/beta} (4.12). (H1) in turn is not implied by integrability
or smoothness of Omega.

4.7 beta = 2: analytic exclusion and a necessary flat jet. Let beta = 2, U smooth, div U = 0, U = o(|X|),
W = 2X + U - U(0), DW(0) = diag(0, 4), and let Theta be C^3 (C^infinity for (ii)), even in x, Theta(0,y) = 0,
Theta = a0 x^2 + O(|X|^3), a0 != 0, W.grad Theta = 0.
(i) U cannot be real analytic on a neighborhood of the zero set Z = {W = 0}.
(ii) If U and Theta are C^infinity, there is an accumulation point p of Z at which every derivative of Theta of
order >= 1 vanishes. If in addition Omega is C^infinity and satisfies (V), every derivative of Omega (of order >= 0)
vanishes at p.
Proof outline. By 4.4, Z contains an arc through 0; W.X = 2|X|^2 + o(|X|^2) makes Z compact, so its set Z' of
accumulation points is compact and nonempty. At p in Z', DW(p) is not invertible (p is not isolated) and has trace
div W = 4, so it has rank one with eigenvalues 0 and 4. (i) With analytic W, one component has a regular analytic
zero graph near p and the other component, restricted to it, is analytic in one variable with accumulating zeros,
hence vanishes: near p, Z = Z' is a regular analytic curve. So Z' is a compact 1-manifold without boundary; a component
is a simple closed curve C with interior D, and 4|D| = int_D div W = int_C W.n = 0, a contradiction. (ii) In coordinates
(s, n) diagonalizing DW(p), W = (0, 4n) + O(|(s,n)|^2). If Theta - Theta(p) had a first nonzero homogeneous Taylor part
P_m, the degree-m part of (T) gives n d_n P_m = 0, so P_m = k s^m, k != 0; on the graph {W_n = 0} the s-derivative of
Theta is nonzero for small s != 0, so (T) forces W_s = 0 there, and Z = Z' is locally that graph. If this held at every
p in Z', the argument of (i) would give the same contradiction. Hence Theta cannot be real analytic on R^2: analyticity
at the flat point would make it locally constant, and analytic continuation would contradict a0 != 0. (The conclusion
does not assert Theta(p) = 0, nor exclude analyticity on a neighbourhood not containing p.) For Omega: Theta_x is flat at
p, so (V) gives Omega(p) = 0; if Q_m (m >= 1) were the first nonzero homogeneous Taylor part of Omega at p, the degree-m part
of (V) in the coordinates (s, n) would read (4 n d_n + 1) Q_m = 0, and 4 n d_n + 1 acts on the monomial s^{m-j} n^j as
multiplication by 4j + 1 > 0, so Q_m = 0. Flatness is a statement about Taylor coefficients, not vanishing near p.
(iii) Arc through the center (smooth profiles). In (iii)-(vii) assume the full smooth B2 system: U, Theta, Omega are
C^infinity, div U = 0, -curl U = Omega, U = o(|X|), (T) and (V) hold, with the velocity and scalar parities, the axis
condition Theta(0,y) = 0 and the center jet above. Then the connected component gamma of Z containing 0 is a compact smoothly embedded
arc with two endpoints (not a point and not a closed curve). It is invariant under S(x, y) = (-x, y), meets the axis only
at 0, and its endpoints satisfy p_- = S p_+ with x(p_+) > 0. At both endpoints every derivative of Theta - L of every
order and every derivative of Omega of every order vanish, where L = Theta(p_+) = Theta(p_-) (the sign of L is not
determined), and DW(p_+-) = 4 n (x) n with n the unit normal of gamma. Consequently Theta is not real analytic on any
connected neighbourhood of gamma, and the flat point of (ii) can be taken to be an endpoint of the arc through the
center. On the interior of gamma, with tau the unit tangent, n = (-tau_y, tau_x) and theta(s) = Theta(gamma(s)) in
arclength, DW = (4 n + lambda tau) (x) n, Omega = lambda, grad Theta = theta'(tau - lambda n/4) and
lambda [1 - theta' tau_y/4] = theta' tau_x. It is not asserted that either half of gamma is a graph over x.
(iv) Endpoint alternative. At an endpoint p, take orthonormal coordinates (s, z) with s tangent to gamma and increasing
away from it, let z = k(s) be the zero curve of the normal component of W (k(0) = k'(0) = 0) and t = z - k(s), and write
W_s = f(s) + c1(s, t) t, W_z = c2(s, t) t, c2(0, 0) = 4. Then f vanishes for s <= 0 near 0 and exactly one of the following
holds: (a) zeros of W not on gamma accumulate at p from s > 0; (b) f > 0 on some interval (0, eps) (outgoing case);
(c) f < 0 on some interval (0, eps) (incoming case). In case (b) there is a nonempty open set O, invariant in both time
directions and consisting of orbits whose backward limit is p, with Theta = L and Omega = 0 on O (so U is harmonic on
O); O contains escaping orbits, and the asymptotic angles of the escaping orbits in O fill a nonempty open arc of the
circle on which the vorticity tail a of 4.12(d) vanishes and the temperature limit A of 4.10 equals L. In cases (a)
and (c) no further conclusion is claimed here (for case (c) with isolated zeros of W off gamma, see (xiv), and for
case (a), see (xx)). The mirror endpoint has the same alternative.
Proof outline of (iii)-(iv). U = o(r) gives W.X >= r^2 outside a large disk, so Z is compact, and the flow is complete.
At every zero, trace DW = 4, so some component of W has a nonzero differential and Z lies locally in a smooth embedded
curve. A compact connected set locally contained in smooth embedded curves is a compact one-dimensional manifold with
possible boundary: in a straightened chart around a point of the component, with a closed chart disk D in which Z lies
in a line segment and which does not contain the whole component, every component of (component) cap D meets the
boundary of D (boundary bumping for continua), so near each of its points the component is an interval or a
half-interval of the segment (a singleton component is excluded by 4.4 for the component through 0). It is therefore
an arc or a circle; a circle C bounding D would give 4|D| = int_D div W = int_C W.n = 0. By 4.4 the component through
0 is not a point, so it is an arc. Harmonic uniqueness gives U_rel(SX) = S U_rel(X), so S maps gamma to itself and reverses
the tangent at 0; a decreasing homeomorphism of an interval has exactly one fixed point, and the fixed set of S is the
axis. Flatness at an endpoint p is the argument of (ii): if Theta - L had a first nonzero homogeneous part P_m, then
P_m = c s^m and (T) would force W = 0 on the whole normal nullcline through p, making p interior to a zero arc, which
contradicts maximality of the component; the Omega step is as in (ii). Omega(p) = 0 makes DW(p) symmetric, and its
eigenvalues 0, 4 give DW(p) = 4 n (x) n. Theta(p_-) = Theta(p_+) by evenness. Analyticity near gamma would make Theta
locally constant at p and then constant on the neighbourhood, contradicting the center jet. The interior formulas
follow from DW tau = 0, trace DW = 4, curl W = -Omega, (DW)^T grad Theta = 0 (differentiate (T) at a zero) and (V) on Z,
where W = 0 gives Omega = Theta_x. For (iv), f vanishes on the arc (s <= 0, t = 0), and the zeros near p with s > 0 are the
points t = 0, f(s) = 0, which gives the alternative. In case (b), for s > 0 put rho = t/f(s); in backward time u,
  ds/du = -f - c1 t,  d rho/du = (-c2 + k' c1) rho + k' + f' rho (1 + c1 rho).
Since k'(0) = f'(0) = 0 and c2(0, 0) = 4, for a fixed eta > 0 and small eps the wedge N = {0 < s < eps, |t| < eta f(s)} is
backward invariant, and along backward orbits in N, -3f/2 <= ds/du <= -f/2 and f(s) <= C s, so s decreases to 0 without
reaching it in finite time and t = rho f -> 0: every backward orbit in N tends to p. Transport gives Theta = L on N, hence
Theta_x = 0 there, and (V) gives Omega(phi_{-u} Y) = e^u Omega(Y) for Y in N; boundedness of Omega near p forces
Omega(Y) = 0. O = union over u >= 0 of phi_u N is open, invariant in both directions, and Theta = L, Omega = 0 on O.
If no orbit of O escaped, the forward images of a fixed small open subset of N would stay in a fixed disk while their
area grows like e^{4u}; so O contains an escaping orbit, hence an open set of escaping launch points on a large circle,
and the C^1 scattering map of 4.12 step (7) carries them onto an open arc of asymptotic angles. On that arc a = 0,
because the trajectory amplitude Omega + int_0^infty e^s Theta_x(phi_s .) ds of 4.12 step (7) vanishes on O (Omega = 0
and Theta_x = 0 along forward orbits in O), and the temperature limit of 4.10 equals L (at beta = 2 the temperature is
constant on orbits and m = 0). Every class A requirement used here holds at beta = 2 by 4.15(iv).
Scope of (iii)-(iv). These are necessary conditions, not an exclusion. Theta - L and Omega vanish on O and, by
smoothness, to every order on its boundary, but their vanishing on a neighbourhood of a boundary point (across the
boundary) is not established, and the vanishing of every derivative on the boundary does not by itself give a harmonic
continuation of U across it (no such continuation has been established); this is the step missing in the attempted
closures at beta = 2 described in section 6.3. By (xv), at the boundary points that lie on the orbits of the strong
unstable curve of the endpoint (the endpoint itself included, where the conclusion is that of (xii) and (xiv)(c)),
neither Theta - L nor Omega vanishes on a neighbourhood, and U is not harmonic on one; when Z = gamma, O lies in the
basin O_+ of (xv)(c), every boundary point of which is of this kind for p_+ or for p_-. A harmonic extension of the
restriction of U to O across such a boundary point other than the endpoint, differing from U beyond it, is not
excluded by (xv) and has not been established. Through the endpoint itself, a harmonic extension of the restriction of
U to the side of the strong unstable curve beyond the endpoint, even one differing from U on the other side, is
impossible at outgoing endpoints, at incoming endpoints when the zeros of W off gamma are isolated, and at
accumulating endpoints some neighbourhood of which contains no arc of zeros of W off gamma ((xix)(a), (e), (xx)(d)).
Cases (a) and (c) are not excluded. By (xii)(a), Omega does not vanish on a whole neighbourhood of an endpoint. By
(xxi), Theta - L does not vanish on a whole neighbourhood of any endpoint (this also follows from (vii) and (xii)(a));
at outgoing endpoints, at incoming endpoints when the zeros of W off gamma are isolated, and at accumulating
endpoints, (xii)(b), (xiv)(c) and (xx)(a) give it by other arguments. A proof that Omega or Theta - L does would
exclude smooth profiles at beta = 2.
(v) The subclass Z = gamma. Assume in addition that W has no zero off the arc gamma of (iii), and write h = A for the
temperature limit of 4.10 (as in 4.16). Then both endpoints are outgoing (case (b) of (iv)), the set K of points with
bounded forward orbit equals gamma, every point off gamma has a backward limit that is a single point of gamma, and the
circle of asymptotic directions is the disjoint union, in cyclic order, of two open arcs Gamma_+, Gamma_- (directions
of the orbits whose backward limits are interior points of gamma, on its two sides) and two nondegenerate closed arcs
I_+, I_- = S I_+ (directions of the orbits issuing from p_+, p_-), with I_+ inside the open right semicircle, pi/2 in
Gamma_+ and 3 pi/2 in Gamma_-. On I_+ and I_-, h = L and a = 0, and Theta(R^2) = Theta(gamma) = h(S^1). If W has no
zero on the axis other than 0 (in particular if Z = gamma) and a0 > 0 (a0 < 0 reduces to this by the signed scaling
(A6) with l = -1, which exchanges the upper and lower half-axes), then the axis coefficients a_ax(y) = Theta_xx(0,y)/2 and
q(y) = Omega_x(0,y) of 4.13 are positive on the whole axis, a_ax(y) y^2 -> A_+- > 0 as y -> +-infinity, and h has strict
local minima h(pi/2) = h(3 pi/2) = 0 with h''(pi/2) = 2 A_+ and h''(3 pi/2) = 2 A_-.
(vi) Analytic boundary exclusion. At any outgoing endpoint p (case (b) of (iv), with or without Z = gamma) the strong
unstable curve of p, which bounds the basin O near p, does not agree near p with any regular real analytic embedded
curve through p (a condition on its germ at p, on both branches; analyticity away from p does not suffice). In
particular there is no profile with Z = gamma in which the strong unstable curve of an endpoint is real analytic at
that endpoint (for example a straight segment).
(vii) Scattering identities. Let Phi be the scattering map of 4.12 step (7) and X(t, alpha) = phi_t(Phi^{-1}(e(alpha))).
Then det D Phi = 1, dX = 2 e^{4t} dt d alpha and Theta_x(X(t, alpha)) = -(h'(alpha)/2) e^{-4t} W_2(X(t, alpha)). Hence
h'(alpha) = 0 implies Omega = 0 on the whole orbit X(., alpha) (its backward orbit is bounded) and a(alpha) = 0, and on an arc of directions whose
orbits have backward limits p(alpha) at interior points of gamma (all of Gamma_+ and Gamma_- when Z = gamma),
  a(alpha) = -(3 h'(alpha)/2) int_R e^{-3t} (X_2(t, alpha) - p_2(alpha)) dt     (absolutely convergent).
Consequently, if W has no zero on the axis other than 0 and a0 > 0, then a'(pi/2) < 0 and a'(3 pi/2) > 0: a > 0 just
inside the right half-plane next to both vertical directions (no sign is obtained elsewhere). For every C^1 function F
on the range of Theta,
  int F(Theta) Omega^3 Theta_x dX = (1/2) int_0^{2 pi} F(h(alpha)) a(alpha)^4 d alpha.
Proof outline of (v)-(vii). (1) Limit sets. For a complete C^1 planar field with constant divergence c != 0, no compact
alpha- or omega-limit set contains a regular point: successive crossings v_n of a flow-box transversal are monotone and
tend to a limit; Green's theorem on the Jordan domain D_n closed by the transversal segment [v_n, v_{n+1}] gives
|c| |D_n| <= C |v_{n+1} - v_n| -> 0, while one of the two adjacent half-boxes lies in D_n, so |D_n| is bounded below.
(2) Incoming endpoints. In case (c) the exterior center branch is one orbit C_+ with forward limit p_+; its alpha-limit
is a nonempty connected subset of Z by (1); if it met gamma it would be one point (near interior points of gamma
backward orbits converge to the base point of their fibre), and C_+ with a subarc of gamma (or a homoclinic loop) would
be an invariant Jordan curve bounding a domain whose area grows like e^{4t}. So Z = gamma excludes (c); it excludes (a)
by definition. (3) K = gamma: on a tube around gamma and the two outgoing center branches the normal component grows
and the center branches leave, so every nonstationary orbit leaves the tube forward, while by (1) a bounded forward
orbit has its omega-limit in gamma. Local endpoint basin: in C^4 coordinates (u, v) straightening a center manifold to
v = 0 and the strong unstable curve to u = 0, with the equilibrium arc at u <= 0, u' = g(u) + u v c(u, v) and
v' = v d(u, v), d > 2, c bounded, g = 0 for u <= 0 and g > 0 for u > 0; backward, |v| decays like e^{-2 sigma}, so v c
is integrable in backward time. On u < 0 (where g = 0) log |u| changes by at most C |v(0)|, so u has a nonzero negative
limit and these orbits converge to interior points of gamma. On u > 0 the function w = u exp(-int_0^t v c ds) satisfies
w' = g(u) exp(-int_0^t v c ds) > 0, so w decreases backward to a limit; a positive limit would give u -> u_* > 0 and
u' -> g(u_*) > 0 as t -> -infinity, which contradicts the convergence of u. So u -> 0, and orbits with u > 0 converge to p. The interior of the local backward basin of p is the side u > 0 of the
strong unstable curve, for any choice of center manifold; the basin also contains p and the two branches u = 0,
v != 0 of the strong unstable curve (u = 0 is invariant and |v| decays backward). Interior points of gamma have exactly two nonstationary backward fibres. This gives the orbit
classification, and the scattering map of 4.12 step (7) gives the partition of the circle. (4) Axis: b has the single
zero 0, so a_ax and q are positive (4.13(i) with y_+- infinite), (log(a_ax y^2))' is integrable at infinity, and
Theta_xx(0, y) = h''(pi/2) b(y)^2/(4 psi(y)^4), where Phi(0, y) = (0, psi(y)), psi' = 2 psi/b, (D Phi)_11 = 1/psi' on the
axis and psi(y)/y -> 1. (5) For (vi): on the basin side W = grad H with Delta H = 4 and zero normal derivative on the
strong unstable curve Sigma; if Sigma is analytic, choose (Cauchy-Kovalevskaya) an analytic P near p with Delta P = 4
and P = d_n P = 0 on Sigma; then H - P is harmonic with zero normal derivative on Sigma (the Dirichlet trace of H is not
used), straightening Sigma conformally and reflecting evenly extends H - P harmonically, and W = grad(H - P) + grad P
extends analytically to a field W~ near p with the jet of W at p; the reduced field of W~ on its analytic normal nullcline has the flat Taylor series of f, hence vanishes, and
its zero arc for s > 0 lies in the basin, where W~ = W, so W would vanish at points of O. (A separate proof by complex
reflection was also checked.) (6) For (vii): M_t = e^{-2t} D phi_t solves dM/dt = DV M with |DV(phi_t Y)| <= C e^{-t}, so
D Phi = lim M_t and det M_t = 1; Theta = h(arg Phi) and det D Phi = 1 give the formula for Theta_x; on arcs of interior
fibres, a(alpha) = int_R e^s Theta_x(phi_s Y_alpha) ds and one integration by parts (the integrand is O(e^t) as
t -> -infinity and O(e^{-t}) as t -> +infinity) give the formula for a; the sign of a'(pi/2) follows from h'(pi/2) = 0,
h''(pi/2) > 0 and the positive vertical displacement of the upper axis orbit. The F-weighted identity is the divergence
theorem for F(Theta) W Omega^4 (divergence 4 F(Theta) Omega^3 Theta_x, integrand O(r^{-5/2}), flux 2 int F(h) a^4).
Scope of (v)-(vii). (vi) is a restricted exclusion (analytic boundary orbit at an outgoing endpoint); (v) and (vii) are
necessary conditions. The smooth subclass Z = gamma is not excluded: harmonic reflection needs an analytic boundary, and
flatness of a harmonic function at one boundary point does not force it to vanish (exp(-z^{-sigma}), 0 < sigma < 1, on
the right half-plane).
(viii) Strict-sign exclusion. Assume only the hypotheses of the opening paragraph, with U, Theta of class C^1 and the
sublinearity U = o(|X|) uniform in direction, and let Omega be C^1 and satisfy (V); no elliptic relation and no far-field
rate are used. Let sigma = sign(a0) and M_* = sup over {x > 0} of sigma Theta. Then 0 < M_* < infinity, and M_* is attained
along a whole nonconstant orbit contained in {x > 0} that escapes to infinity forward; on this orbit grad Theta = 0 and
Omega = 0. Consequently the zero set of Omega in the open right half-plane contains a complete unbounded orbit: Omega is
not strictly positive there, not strictly negative there, and not nowhere zero there, and its zero set there is neither
bounded nor discrete (likewise in the left half-plane). For the full smooth system of (iii), the asymptotic direction
alpha_* of this orbit lies in the open right semicircle and a(alpha_*) = 0, where a is the angular vorticity tail of 4.12;
in particular a = A_0 cos(alpha) with A_0 != 0 is impossible at beta = 2.
Proof outline. (1) Choose R with |V(X)| <= |X| for |X| >= R; then W.X >= |X|^2 there, the flow is complete (|W| <= C(1 + |X|)),
|phi_{-t} X| <= max(R, |X|) for t >= 0, and a forward orbit that reaches the circle Sigma = {|X| = R} escapes. The set K of
points with bounded forward orbit is the intersection over t >= 0 of phi_{-t}(B_R), compact and invariant, and
|K| = |phi_t K| = e^{4t} |K| gives |K| = 0, so its complement E is open and dense; each orbit of E crosses Sigma exactly once.
(2) Theta is constant along orbits ((T) with beta = 2) and vanishes on the axis, so an orbit on which sigma Theta > 0
cannot meet the axis (no invariance of the axis is assumed); hence every E orbit through a point of {x > 0} with
sigma Theta > 0 stays in {x > 0} and crosses the open right semicircle Sigma_+, where Theta takes the same value.
(3) sigma Theta(x, 0) = |a0| x^2 + O(x^3) > 0 for small x > 0, so sigma Theta > 0 on an open subset of {x > 0}, which meets E,
and transport carries a positive value to Sigma_+. The continuous function sigma Theta on the closed right semicircle has a
positive maximum, attained at an interior point P (both endpoints lie on the axis, where Theta = 0), and P lies in E. By (2)
(points with sigma Theta <= 0 satisfy the bound trivially), density of E and continuity, sigma Theta <= M_* :=
sigma Theta(P) on all of {x > 0}. (4) sigma Theta = M_* > 0 on the orbit of P,
which therefore lies in the open half-plane by (2), so every point of that orbit is an interior maximum and grad Theta = 0 there; then (V)
reads d Omega/dt = -Omega along the orbit, so e^s |Omega(P)| = |Omega(phi_{-s} P)| <= sup over B_R of |Omega| for s >= 0,
whence Omega(P) = 0. W(P).P > 0, so the orbit is nonconstant. (5) Corollary: the scattering map Phi of 4.12 step (7)
commutes with S, preserves E and is injective, and {x > 0} is invariant (W_1(0, y) = 0 by the B2 parity of the full
system), so Phi_1 >= 0 on E n {x > 0} with equality impossible (it would give Phi(SY) = Phi(Y)); hence alpha_* = arg
Phi(P) lies in the open right semicircle, and the uniform polar tail of 4.12 gives |a(alpha(t))| <= sup over alpha
of |r^{1/2} Omega(r e(alpha)) - a(alpha)| at r = |phi_t P|, which tends to 0, so a(alpha_*) = 0 by continuity.
Scope of (viii). A restricted exclusion (a strict sign of Omega in a half-plane, or a nowhere-vanishing leading tail on
the right semicircle). Omega >= 0 on {x > 0} with zeros is not excluded, nor is a with zeros. The argument needs
uniform sublinearity (a raywise version fails for the kinematic steps) and does not extend to beta > 2, where
Theta(phi_t Y) = e^{(beta-2)t} Theta(Y) grows along escaping orbits and a maximum on the crossing circle has
grad Theta != 0.
(ix) Weak vorticity sign. (A) holds for every beta >= 2 and (B) for beta = 2. Let (Theta, Omega, U) be a class A
profile with beta >= 2 and assume Omega >= 0 on {x > 0}, or Omega <= 0 there (zeros allowed). (A) No forward-escaping
orbit in {x > 0} lies on a horizontal line, and none is eventually horizontal: on every line y = y0,
W_2(x, y0) x^{-(1-1/beta)} tends as x -> +infinity to a nonzero limit with the sign opposite to that of Omega.
(B) If beta = 2, every critical point of h in the open right semicircle is degenerate: h'(alpha) = 0 with
|alpha| < pi/2 implies h''(alpha) = 0, and along the orbit X(., alpha) one has Omega = grad Omega = grad Theta =
D^2 Theta = 0. Since h has an interior extremum on that semicircle (the direction alpha_* of (viii)), h is not a Morse
function there.
Proof outline. (A) Let s = 1/beta, k = 2 - s in [3/2, 2) and f as in 4.16 (velocity terms), -(f'' + k^2 f) = a, so that
V(r e) = r^{1-s}[-f'(theta) e + k f(theta) e_perp] + o(r^{1-s}) uniformly in theta (f is the leading coefficient of
the stream function Psi). Oddness of Omega gives a(pi - theta) = -a(theta); since k is not an integer, the periodic
solution is unique, so f(pi - theta) = -f(theta) and f(+-pi/2) = 0, and on J = (-pi/2, pi/2) f is the Dirichlet
solution, -f(0) = int_J G(0, t) a(t) dt with G(0, t) = sin(k pi/2) sin(k(pi/2 - |t|)) / (-k sin(k pi)) > 0 on J (both
numerator factors are positive and sin(k pi) < 0 for 3/2 <= k < 2). By the weak sign, a has one sign on J, and a is not
identically 0 on J (otherwise a = 0 on the circle by oddness, contrary to 4.12), so f(0) != 0 with sign opposite to
that of Omega. On y = y0, as x -> infinity, r/x -> 1 and the angle arctan(y0/x) tends to 0; the uniformity in theta
allows evaluation at this varying angle, and beta y0 x^{-(1-s)} -> 0, so W_2 = beta y0 + V_2 = k f(0) x^{1-s}(1 + o(1)).
(B) Omega is bounded on R^2 (uniform tail of 4.12 and continuity). At a critical direction alpha_* of h, Theta = h(alpha)
along X(t, alpha), where alpha = arg Phi is a C^1 coordinate with grad alpha = (-W_2, W_1)/(2 e^{4t}) != 0 (4.7(vii));
the orbit lies in {x > 0} ((viii) step (5)). So grad Theta = 0 on X(., alpha_*), and Omega = 0 there as in (viii)
step (4). Under the weak sign each point of that orbit is an interior extremum of Omega, so grad Omega = 0 along it, and
the x_j-derivative of (V) reduces there to d_j d_x Theta = 0. Since alpha(Y + z) - alpha_* = grad alpha(Y).z + o(|z|) and
h'(alpha_*) = 0, Theta(Y + z) = Theta(Y) + (1/2) h''(alpha_*)(grad alpha(Y).z)^2 + o(|z|^2), so
D^2 Theta = h''(alpha_*) grad alpha (x) grad alpha on the orbit, and h''(alpha_*) d_x alpha = 0; if h''(alpha_*) != 0,
then d_x alpha = -W_2/(2 e^{4t}) = 0 along the whole orbit, which would be horizontal, contradicting (A).
Scope of (ix). A restricted exclusion under an additional sign hypothesis. Degenerate critical points of finite order
(for example a quartic maximum), flat extrema and plateaus of h, and general sign-changing vorticity, are not excluded.
The angular statement (B) does not extend directly to beta > 2, where Theta = e^{(beta-2)t} H(alpha) along orbits and a
critical point of H with H != 0 is not a critical point of Theta.
(x) Finite-order critical directions under a weak sign (beta = 2). Assume the hypotheses of (ix) with beta = 2
(Omega >= 0 on {x > 0}, or Omega <= 0 there). Let alpha_* be a direction in the open right semicircle with
h^{(j)}(alpha_*) = 0 for 1 <= j < N and h^{(N)}(alpha_*) != 0 for some N >= 2, and let C_* = X(., alpha_*) be its orbit.
Suppose that the backward orbit of C_* converges to a single point p and that DW(p) has no negative eigenvalue (for
example when Z = gamma: then p lies on gamma and DW(p) has eigenvalues 0 and 4 by (v)). Then N is odd. Consequently, at
every local extremum alpha_* of h in the open right semicircle at which this backward-limit condition holds (for
example at the maximum direction of (viii) when Z = gamma), h is flat: h(alpha_* + s) - h(alpha_*) = o(|s|^m) as s -> 0
for every m; and then Theta - h(alpha_*) and Omega are flat (every derivative of positive order of Theta, and every
derivative of Omega, vanishes) at every point of C_*.
Proof outline. (1) Near C_*, Theta = h(alpha) with alpha = arg Phi of class C^1 and grad alpha = (-W_2, W_1)/(2 e^{4t}) != 0
on X(t, alpha) (4.7(vii)). For Y in C_*, alpha(Y + z) - alpha_* = grad alpha(Y).z + o(|z|), so Theta(Y + z) - h(alpha_*) =
(h^{(N)}(alpha_*)/N!)(grad alpha(Y).z)^N + o(|z|^N); since Theta is smooth, uniqueness of Taylor polynomials gives
D^j Theta = 0 on C_* for 1 <= j < N and D^N Theta = h^{(N)}(alpha_*) (grad alpha)^{(x)N} != 0. Hence D^n Theta_x = 0 on C_* for
n <= N - 2 and D^{N-1} Theta_x = h^{(N)}(alpha_*) d_x alpha (grad alpha)^{(x)(N-1)}. Also Omega = 0 on C_* ((ix)(B), whose
argument uses only grad Theta = 0 on C_*).
(2) Jet equations. Let J_n(t) = D^n Omega(X(t)), a symmetric n-tensor, X(t) = X(t, alpha_*), A(t) = DW(X(t)). Differentiating
(V) n times along C_* gives
  dJ_n/dt + L_n(t) J_n = D^n Theta_x - sum_{j=2}^{n} binom(n, j) Sym(D^j W . D^{n-j+1} Omega),
where (L_n(t) T)(v_1, ..., v_n) = T(v_1, ..., v_n) + sum_{i=1}^{n} T(v_1, ..., A(t) v_i, ..., v_n), Sym is the
symmetrization over the n slots, and D^j W . D^{n-j+1} Omega is the contraction of the vector slot of D^j W (with j
free slots) into one slot of D^{n-j+1} Omega; the sum involves only J_m with m <= n - 1.
(3) Backward growth. Omega(p) = 0 by continuity, so DW(p) is symmetric (curl W = -Omega), and its eigenvalues lambda,
mu are >= 0. The operator L_n(p) is symmetric for the inner product of symmetric tensors induced by the Euclidean one, with
eigenvalues 1 + k lambda + (n - k) mu >= 1 (0 <= k <= n). Suppose J_m = 0 on C_* for m < n and D^n Theta_x = 0 on C_*. In
backward time tau = -t, dJ_n/dtau = L_n(-tau) J_n and L_n(-tau) -> L_n(p), so d|J_n|^2/dtau >= |J_n|^2 for tau large; a
nonzero J_n would grow exponentially, while J_n is bounded because the backward semiorbit has compact closure. So
J_n = 0 on C_*. By induction J_n = 0 on C_* for every n <= N - 2.
(4) Weak sign. For Y in C_* and small z, Omega(Y + z) = J_{N-1}(z, ..., z)/(N - 1)! + o(|z|^{N-1}) has one sign; if N is
even, the leading form has odd degree and must vanish, so J_{N-1} = 0 on C_*. Then (2) at order N - 1 gives
D^{N-1} Theta_x = 0 on C_*, so d_x alpha = -W_2/(2 e^{4t}) = 0 along C_*: C_* would be a forward-escaping orbit in {x > 0} on a
horizontal line, which (ix)(A) excludes. Hence N is odd.
(5) Extrema. h is smooth (4.16). At a local extremum alpha_* the leading term (h^{(N)}(alpha_*)/N!) s^N of a finite first
nonzero order N could not change sign, so N would be even, contrary to (4); hence every derivative of h vanishes at alpha_*
and h(alpha_* + s) - h(alpha_*) = o(|s|^m) for every m. For Y in C_*, |alpha(Y + z) - alpha_*| <= C|z|, so
Theta(Y + z) - Theta(Y) = o(|z|^m) for every m, and every positive-order derivative of the smooth Theta vanishes on C_*.
Then D^n Theta_x = 0 on C_* for all n, step (3) applies at every order, and every J_n vanishes on C_*.
Scope of (x). A restricted statement under the weak-sign hypothesis and the backward-limit condition. Critical
directions of odd finite order (inflection type), flat extrema and plateaus of h are not excluded; flatness along one orbit
does not imply vanishing on a neighborhood. Backward limits at saddles of W (eigenvalues -nu < 0 and 4 + nu) are covered
by the argument only when 1 - (N - 2) nu > 0, that is nu < 1/(N - 2) for even N >= 4. At equality the coercivity estimate
of step (3) fails, and no conclusion is asserted there. (For even m >= 2 the local fields W = (-x/m, (4 + 1/m) y -
x^{m+1}/(m + 1)), Omega = x^m >= 0, Theta = 0 satisfy div W = 4, -curl W = Omega, (T) and (V); along the escaping orbit
on the y-axis, whose backward limit 0 is a saddle with nu = 1/m, the jet D^m Omega keeps its nonzero value, so step (3)
fails at order m = N - 2 when nu = 1/(N - 2). These fields are not profiles: Theta = 0, they lack the B2 parity and
sublinear velocity, and they say nothing about the order of a critical direction of h.)
(xi) Sign accumulation on interior fibres (beta = 2, weak sign). Assume the hypotheses of (ix) with beta = 2
(Omega >= 0 on {x > 0}, or Omega <= 0 there), and let alpha_* be a direction in the open right semicircle whose orbit
X(., alpha_*) has its backward limit at an interior point of gamma. Then h' does not take both positive and negative
values in every neighbourhood of alpha_*. In particular h has no strict local extremum at alpha_* (by the mean value
theorem both signs of h' occur in every neighbourhood of a strict local extremum; this contains the finite-order case of
(x)), and alpha_* is not a flat critical point of h at which both signs of h' accumulate. If moreover
Z = gamma, a0 > 0 and Theta is not constant on any open subarc of gamma, then Theta increases strictly along the right
half of gamma from the center to the endpoint p_+, L = Theta(p_+) > 0, and Theta(R^2) = [0, L]; in particular
Theta >= 0 on R^2.
Proof outline. (1) Asymptotic phase. Near a compact subarc of the relative interior of gamma choose smooth coordinates
(u, v) with the subarc on v = 0; then W = v (A(u, v), B(u, v)) with B(u, 0) = 4, and B >= b0 > 0 after shrinking. In
backward time |v| decays like e^{-b0 s}, so u has a limit S(u, v) with |S - u| <= C|v|. The variational equations
for (du, dv), with int_0^infinity |v| ds <= C|v(0)| and Gronwall's inequality, give |du| <= C(|du(0)| + |dv(0)|) and
exponential decay of dv, so the finite-time maps converge in C^1: S is C^1, S(u, 0) = u and S_u != 0 near v = 0. On each
side of the subarc the level sets of S are the fibres (single orbits converging to the base points). On the side
containing X(., alpha_*), the points of a section v = const near the orbit lie in the escape set E (E is open), and the
scattering angle is there a C^1 function of the base point with nonzero derivative (if alpha_u = 0 at a point of the
section, W.grad alpha = 0 and W_v = v B != 0 give grad alpha = 0, against grad alpha = (-W_2, W_1)/(2 e^{4t}) != 0 of
(ix)(B)). Hence alpha = A_ph(S) with A_ph of class C^1, and for every point Y of the orbit there are a neighbourhood U_Y in E
and C_Y with |d_x alpha(phi_{-s} Z)| <= C_Y for Z in U_Y and s >= 0.
(2) Resolvent. On this open family I(Y) = int_0^infinity e^{-s} d_x alpha(phi_{-s} Y) ds converges absolutely and is
continuous, and (V) along backward orbits (bounded, so the endpoint term vanishes) with Theta = h(alpha) gives
Omega(Y) = h'(alpha(Y)) I(Y), also where h' = 0; moreover d/dt I(phi_t Y) + I(phi_t Y) = d_x alpha(phi_t Y).
(3) Suppose both signs of h' accumulate at alpha_*. The orbit X(., alpha_*) lies in {x > 0}: its direction is in the
open right semicircle, so it has points with x > 0, and the axis is invariant. Let Y_* be an arbitrary point of
X(., alpha_*) and take a transversal through Y_* in U_{Y_*} n {x > 0}, on which alpha is a coordinate. Under the weak
sign, I has one weak sign at points of the transversal where h' > 0 and the opposite weak sign where h' < 0, and both
kinds of points accumulate at Y_*, so I(Y_*) = 0. Since Y_* was arbitrary, I = 0 along the whole orbit, d_x alpha = 0
there by (2), and W_2 = 0 there by the formula for grad alpha: the orbit is a forward-escaping orbit in {x > 0} on a
horizontal line, which (ix)(A) excludes.
(4) Corollary. Under Z = gamma every nonstationary orbit with backward limit in the interior of gamma escapes ((v)), and
its direction lies in the open right semicircle when its base point lies on the right half of gamma ((viii) step (5)).
Parametrize the right half of gamma by arclength s in (0, s_e) and put g(s) = Theta(gamma(s)). Theta is constant along
orbits (beta = 2) and continuous at their backward limits, so g(s) = h(A_ph(s)) on each of the two fibre families, with
A_ph' continuous and nonzero; hence both signs of g' cannot accumulate at any point of (0, s_e). The zero set of g' has
empty interior by assumption, so the closures of {g' > 0} and {g' < 0} relative to (0, s_e) cover this interval, and a
common point would be such an accumulation point; so one of the two sets is empty. gamma is tangent at 0 to the kernel
of DW(0) = diag(0, 4), so g(s) = a0 s^2 + O(s^3); hence g' >= 0 and g is strictly increasing. By (v),
Theta(R^2) = Theta(gamma), and gamma is symmetric with Theta even in x, so Theta(R^2) = [0, L].
Scope of (xi). A restricted statement under the weak-sign hypothesis. It excludes neither a plateau boundary (h' = 0
on an open interval on one side of alpha_* and one sign on the other), nor critical directions whose orbits issue
from an endpoint of gamma, nor constant subarcs of Theta on gamma in the corollary. At an endpoint the bound of step (1)
can fail: for the local fields W = ((4 - 3y^2) x, y^3) on y > 0 (div W = 4) the first integral x y^3 exp(2/y^2) has
x-derivative (y0^{-2} + 2s)^{-3/2} exp(2/y0^2 + 4s) along the backward orbit of (0, y0), so the integral of step (2)
diverges (these fields are not profiles).
(xii) No harmonic neighbourhood of an endpoint; no isothermal neighbourhood, no analytic transverse data and no finite
separated representation at an outgoing endpoint (beta = 2). In the setting of (iii), let p be an endpoint of gamma
and L = Theta(p).
(a) U is not real analytic on any neighbourhood of p; in particular Omega does not vanish identically on any
neighbourhood of p.
(b) If p is outgoing (case (b) of (iv)), Theta - L does not vanish identically on any neighbourhood of p.
Equivalently, Theta is not constant on any nondegenerate subarc of gamma that has p as an endpoint.
(c) Let p be outgoing and let (s, z) be the orthonormal coordinates of (iv) at p, so that the lines s = const are
parallel to the normal of gamma at p; write U and Omega in these coordinates. There is no delta > 0 such that
z -> U(0, z) is real analytic on (-delta, delta) and, for every s in (0, delta), z -> Omega(s, z) is real analytic on
(-delta, delta). In particular, on no square {|s| < delta, |z| < delta} is U a polynomial in z of bounded degree with
coefficients smooth in s.
(d) Let p be outgoing, (s, z) the coordinates of (c), and sigma the function of (xiii), defined on (-eps_0, eps_0),
with C = {s = sigma(z)} near p. There are no eps in (0, eps_0), integer N >= 1, real functions a_1, ..., a_N
continuous on [0, eps) and continuously differentiable on (0, eps), and maps B_1, ..., B_N from (-eps, eps) to R^2
such that W(s, z) = sum_{j <= N} a_j(s) B_j(z) on S_+ = {(s, z): |z| < eps, max(0, sigma(z)) < s < eps}. No regularity
of the B_j is assumed. In particular, on no such set S_+ is W, or U, a polynomial in z of bounded degree with
coefficients smooth on [0, eps).
Proof outline. (a) If U is real analytic on a disk N_p around p, so is W. By (iii), DW(p) = 4 n (x) n, with n a fixed
unit normal of gamma at p, so the component W.n has nonzero differential at p and, after shrinking N_p, its zero set
in N_p is a regular analytic curve Gamma_p through p; Z n N_p lies in Gamma_p, and gamma n N_p is the part of Gamma_p
on one side of p. For a fixed unit vector tau orthogonal to n, the restriction of W.tau to Gamma_p is a real analytic
function of one variable that vanishes on that side, so it vanishes on Gamma_p, and Gamma_p lies in Z: the component
of Z containing gamma would contain points of Gamma_p beyond p, contradicting that p is an endpoint of this component.
If Omega = 0 on N_p, U is divergence free and curl free on N_p, hence harmonic and real analytic there. (b) Suppose
Theta = L on a disk N_p around p. Take the coordinates (u, v) of step (3) of the proof of (v)-(vii), centered at p, on
a rectangle Q = {|u| <= rho, |v| <= rho} in N_p, in which u' = g(u) + u v b(u, v), v' = v d(u, v), |b| <= B (b is the
coefficient c of step (3)), d > 2, g = 0 for u <= 0 and g > 0 for u > 0, and the arc gamma is {v = 0, u <= 0} near p
(this local part of step (3) uses only case (b), not Z = gamma). While a backward orbit stays in Q, |v(-s)| <= |v(0)|
e^{-2s}, so the integral of |v| over backward time is at most |v(0)|/2; if u(0) < 0, log |u| changes by at most B
|v(0)|/2 (g = 0 there); if u(0) > 0, w = u exp(-int_0^t v b) increases forward, so 0 < u(-s) <= u(0) e^{B |v(0)|/2};
and u = 0 is invariant. Hence backward orbits from Q' = {|v| < rho/2, |u| < (rho/2) e^{-B rho/4}} never leave Q. On
N_p, Theta_x = 0 and (V) reads d Omega(phi_t Y)/dt = -Omega(phi_t Y), so Omega(Y) = e^{-s} Omega(phi_{-s} Y) for Y in
Q' and s >= 0; Omega is bounded on Q, so Omega = 0 on Q', which (a) excludes. Equivalence: if Theta = L on a
nondegenerate subarc of gamma ending at p, then, for rho small, the backward limit of a point of Q' is p (if u >= 0,
by step (3)) or a point (u_-, 0) of gamma with |u_-| <= |u(0)| e^{B rho/4} < rho/2 (if u < 0), which lies on that
subarc; Theta is constant on orbits and continuous, so Theta = L on Q'. The converse is immediate.
Proof outline of (c). Suppose such delta exists. Since W = 2X + U - U(0) with X affine in (s, z), z -> W(0, z) is real
analytic on (-delta, delta); moreover curl W = -Omega and div W = 4. Let N = {0 < s < eps, |t| < eta f(s)} be the set
of the proof of (iv), on which Omega = 0, and choose 0 < delta' <= min(delta, eps) with |k(s)| + eta f(s) < delta for
0 < s < delta'. For each such s, Omega(s, .) vanishes on the nonempty open interval |z - k(s)| < eta f(s), so by the
identity theorem it vanishes on (-delta, delta). Thus W has divergence 4 and zero curl on
R_+ = (0, delta') x (-delta, delta), and both components are harmonic there (Delta W_s = d_s div W - d_z curl W and
Delta W_z = d_z div W + d_s curl W, with curl W = d_s W_z - d_z W_s). Extend w_0(z) = W(0, z) componentwise to a
holomorphic function near z = 0, real on the real axis, and put A(s, z) = [w_0(z + i s) + w_0(z - i s)]/2, a real
analytic harmonic field near p with A(0, z) = w_0(z). On a smaller rectangle (0, delta'') x (-delta'', delta''), W - A
is harmonic, continuous up to s = 0 and zero on s = 0, so by the Schwarz reflection principle its odd extension across
s = 0 is harmonic. Hence the restriction of W to that rectangle extends to a real analytic field W^an on a
neighbourhood of p (A plus the odd extension). W is smooth up to s = 0, so W^an and W have the same derivatives of
every order at p, and DW^an(p) = 4 n (x) n by (iii). By the analytic implicit function theorem the zero set of the
normal component (W^an)_z near p is an analytic graph z = k^an(s), which coincides with z = k(s) for small s > 0, and
f^an(s) = (W^an)_s(s, k^an(s)) is real analytic near 0 and equal to f(s) for small s > 0. The functions k and f are
smooth (d_z W_z(p) = 4), and f vanishes for s <= 0 by (iv), so every derivative of f, hence of f^an, vanishes at 0;
then f^an = 0 near 0 and f = 0 on an interval (0, delta'''), contrary to case (b). In the polynomial case, Omega(s, .)
and U(0, .) are polynomials in z.
Proof outline of (d). Suppose that eps, the a_j and the B_j exist; the representation persists when eps is decreased.
The points of gamma near p other than p (z = k(s), s < 0, with sigma(k(s)) = O(s^4)) lie in {s < sigma(z)}, so for a
small disk D about p, D_- = D n {s < sigma(z)} and D_+ = D n {s > sigma(z)} in the notation of (xviii)(a), and by
(xviii)(b) W = grad H with Lap H = 4 on D_+, so W is real analytic there. Decrease eps so that S_+ lies in D, hence in
D_+. Put a = (a_1, ..., a_N) and let E be the span of the vectors a(s), 0 < s < eps. E != {0}, since otherwise W = 0
on the nonempty open set S_+, while the zeros of W in D are the points of gamma (case (b) of (iv)). Choose
s_1, ..., s_m in (0, eps) such that a(s_1), ..., a(s_m) is a basis of E, and write a(s) = sum_i c_i(s) a(s_i); the c_i
are linear functions of a(s) (E is closed, so a(0) is in E), hence continuous on [0, eps) and continuously
differentiable on (0, eps). Choose delta in (0, eps) with sigma(z) < min_i s_i for |z| < delta. Then
T_i(z) = W(s_i, z) = sum_j a_j(s_i) B_j(z) is real analytic on (-delta, delta), and V(s, z) = sum_i c_i(s) T_i(z),
defined on [0, eps) x (-delta, delta), equals W at the points of S_+ in this set. For fixed s in (0, eps), div V - 4
and curl V are real analytic functions of z on (-delta, delta) (finite sums of terms c_i'(s) T_i, c_i(s) T_i' and a
constant) that vanish on the open set {|z| < delta, sigma(z) < s}, which contains a neighbourhood of 0; so they vanish
on (-delta, delta), and div V = 4, curl V = 0 on (0, eps) x (-delta, delta). Write V = (V_s, V_z) and w = s + i z.
Then K = V_s - i V_z + 4 i z is holomorphic in w on (0, eps) x (-delta, delta) (the Cauchy-Riemann equations for K are
div(V - (0, 4 z)) = 0 and curl(V - (0, 4 z)) = 0), continuous up to s = 0, and its trace
F(z) = K(0, z) = sum_i c_i(0) ((T_i)_s(z) - i (T_i)_z(z)) + 4 i z is real analytic. Let G be the holomorphic function
near 0 with G(i z) = F(z) for small real z (extend F holomorphically and put G(w) = F(-i w)). On a half-disk
{s > 0, |w| < rho}, K - G is holomorphic, continuous up to s = 0 and zero there; its extension by 0 to
{s <= 0, |w| < rho} is continuous and, by Morera's theorem, holomorphic, so it is zero and K = G on the half-disk.
Hence W^an = (Re G, 4 z - Im G) is a real analytic field on {|w| < rho} that equals V on the half-disk, and W on the
open set S_+ n {|z| < delta, |w| < rho}, whose closure contains p (it contains (s, 0) for small s > 0). W is smooth
near p, so W^an and W have the same derivatives of every order at p. As in the proof of (c), the zero set of (W^an)_z
near p is an analytic graph z = k^an(s), and by implicit differentiation (d_z W_z(p) = 4) k^an and
f^an(s) = (W^an)_s(s, k^an(s)) have the Taylor series of k and f at 0; f vanishes for s <= 0, so f^an is flat at 0,
hence f^an = 0 near 0. Since k'(0) = 0 and sigma(0) = sigma'(0) = 0, k^an(s) = O(s^2) and sigma(k^an(s)) = O(s^4) < s
for small s > 0, so (s, k^an(s)) lies in S_+, where W = W^an. There W_z = 0, so k^an(s) = k(s), and f(s) = f^an(s) = 0
on an interval (0, delta'), contrary to case (b). In the polynomial case take B_j(z) = z^l e with e a unit vector of
the coordinates; for U, W = 2X + U - U(0) with X affine in (s, z) adds three separated terms.
Scope of (xii). (a) and (b) are necessary conditions, (c) and (d) are restricted exclusions. The flatness of Theta - L
and Omega at p in (iii) is consistent with (a) and (b): these exclude identical vanishing on a neighbourhood of p, not
zeros of Omega or of Theta - L accumulating at p. The conclusion of (b) also holds at incoming endpoints if the zeros
of W off gamma are isolated ((xiv)(c)), and at accumulating endpoints, in its second form if some neighbourhood of the
endpoint contains no arc of zeros of W off gamma, or if Theta is constant on each such arc in some neighbourhood of
the endpoint ((xx)(a), (c), (xxii)(d)); at incoming endpoints without the isolation of these zeros its first form
holds by (xxi) (it also follows from (vii) and (a)), and its second form is not established; (xxii)(b) and (c) give
necessary conditions for its failure there. By (a), a proof that Omega vanishes on some neighbourhood of an endpoint
would exclude smooth profiles at beta = 2, and by (xxi) so would a proof that Theta - L does; by (c), a proof that U
and Omega have the transverse analyticity assumed in (c) at every outgoing endpoint would exclude smooth profiles with
an outgoing endpoint (in particular the subclass Z = gamma, by (v)). The hypotheses of (c) are not derived from (T),
(V) and the regularity of class A; they concern the fixed lines s = const of the coordinates (s, z) and are unchanged,
after shrinking delta, by the shear t = z - k(s) of the proof of (iv), which translates each such line, while
analyticity along the curves of another smooth coordinate system is not covered; the analyticity of z -> U(0, z)
assumed in (c) does not follow from that of the functions z -> Omega(s, z) together with the local structure at p (the
zero set and endpoint type of (iv), the flatness of (iii) and div W = 4): the second configuration of the 6.3 bullet
beta = 2, which is not a profile, has this structure and Omega = 0 on a half-disk beyond each endpoint, while
W_s(0, z) is flat at z = 0 and nonzero at points arbitrarily close to 0, so z -> U(0, z) is not real analytic on any
interval about 0; (c) gives nothing at incoming or accumulating endpoints (but see (xiii)(c), (xiv)(d) and (xx)(c)),
and none of (b), (c) and (d) excludes profiles without an outgoing endpoint. At outgoing endpoints (c) strengthens
(a): real analyticity of U on a neighbourhood of p is replaced by real analyticity of U along the normal line through
p and of Omega along the parallel lines beyond p.
(d) excludes in particular the polynomial case of (c), even with the polynomial form required only on the side of C
beyond p, where Omega = 0; it assumes no analyticity of U(0, .) or of the B_j: the real analytic slices z -> W(s_i, z)
inside D_+ supply the analytic trace V(0, .) of an auxiliary field V equal to W on S_+ (the analyticity of W(0, .)
itself is not established). It concerns the fixed coordinates (s, z), is stated only at outgoing endpoints, and says
nothing about fields that are not finite sums of this form. Under Z = gamma both endpoints are outgoing (v), so (b)
removes the part of the hypothesis of the corollary of (xi) that concerns subarcs ending at p_+ or p_-; the weak sign
and the hypothesis for the other subarcs remain.

(xiii) Flatness along the strong unstable curve; curvature and index at the endpoints (beta = 2). In the setting of
(iii), let p be an endpoint of gamma, L = Theta(p), (s, z) the coordinates of (iv) at p, with the z axis along n, and
C the strong unstable curve of p: the smooth locally invariant curve through p tangent to n consisting of the points
whose backward orbits converge to p at the rate e^{-4T}. It exists for every type of p (at an outgoing endpoint it is
the curve of (vi)), and near p it is a graph s = sigma(z) with sigma smooth and sigma(0) = sigma'(0) = 0.
(a) Every derivative of every order of Theta - L and of Omega vanishes at every point of C near p, whatever the type
of p in (iv).
(b) Let kappa(l) = k''(s)(1 + k'(s)^2)^{-3/2} be the signed curvature of the curve z = k(s) of (iv), which contains
gamma near p, at the arclength l = int_0^s (1 + k'^2)^{1/2} from p. The Taylor series of W and of sigma at p are
determined by that of k at 0. If 2j + 1 is the least odd order with kappa^(2j+1)(0) != 0, then
sigma(z) = (-1)^j kappa^(2j+1)(0) z^{2j+3}/((2j+3)(2j+3)!) + O(z^{2j+4}); in particular
sigma(z) = kappa'(0) z^3/18 + O(z^4). If every odd-order derivative of kappa vanishes at 0, sigma is flat at 0.
(c) Suppose that C meets {s > 0} in every neighbourhood of p; by (b) this holds when some odd-order derivative of
kappa at 0 is nonzero. Then, whatever the type of p, there is no delta > 0 such that z -> U(0, z) is real analytic on
(-delta, delta) and, for every s in (0, delta), z -> Omega(s, z) is real analytic on (-delta, delta).
(d) Suppose that p_+, and hence p_- = S p_+, is not of the accumulating type (a) of (iv). Then both endpoints have the
same type, gamma is an isolated subset of Z, and its index (the degree of W/|W| on the boundary of a thin tube around
gamma) is +1 if the endpoints are outgoing and -1 if they are incoming. In the incoming case W has degree 2 on the
boundary of the region between that tube and a large circle, with the induced boundary orientation, so W has zeros off
gamma. If, in this incoming case, the zeros of W off gamma are isolated, they are finitely many, each has index
-1, 0 or +1, the numbers N_{+1} and N_{-1} of zeros of index +1 and -1 satisfy N_{+1} - N_{-1} = 2, and some zero q of
index +1 lies in {x > 0}. Every isolated zero q of index +1 is a source (the backward orbits of all points of a
neighbourhood of q converge to q), and Theta = Theta(q) and Omega = 0 on a neighbourhood of q; S q has the same
properties.
Proof outline. (a) Write W(p + h) = M h + N(h) with M = 4 n (x) n and N(h) = O(|h|^2), and put P_4 = n (x) n,
P_0 = I - P_4. For small r the equation h(t) = r e^{4t} n + int_{-infinity}^t [P_0 + e^{4(t-v)} P_4] N(h(v)) dv,
t <= 0, is a contraction in the norm sup_{t <= 0} e^{-4t} |h(t)| on a small ball, and its solution h_r depends
smoothly on r; by uniqueness under time shifts C = {p + h_r(0)} is locally invariant (invariant while the orbit stays
in the chosen neighbourhood), and phi_{-T} q - p = r e^{-4T} n + O(r^2 e^{-8T}) for q = p + h_r(0). For each m the
derivatives of order 1 to m of phi_{-T} at points of C are O(e^{K_m T}) (variational equations). Differentiating
Theta - L = (Theta - L) o phi_{-T} m times at q in C gives a finite sum of derivatives of Theta - L at phi_{-T} q,
which are O(e^{-4NT}) for every N by the flatness at p (iii), times derivatives of phi_{-T}; letting T -> infinity
gives (a) for Theta. For Omega, (V) gives Omega = e^{-T} Omega o phi_{-T} + int_0^T e^{-t} Theta_x o phi_{-t} dt; the
derivatives of the integrand vanish at q, since phi_{-t} q lies in C, and those of the first term tend to 0 in the
same way. (b) curl W = -Omega is flat at p and div W = 4, so the Taylor series of W at p is the gradient of a formal
series H with Lap H = 4 and H(p) = 0. W vanishes on gamma, so H and grad H vanish on the Taylor series of z = k(s); in
the variable z - k(s) the Cauchy problem for Lap H = 4 is noncharacteristic, and the coefficients of H are determined
recursively by the Taylor series of k. Invariance of C, sigma'(z) W_z(sigma(z), z) = W_s(sigma(z), z), determines the
coefficient sigma_m of z^m from the lower ones (with the factor 4m). Each sigma_m is a polynomial with rational
coefficients in k_i = k^{(i+2)}(0); the dilations of the plane make it homogeneous of weight m - 1 when k_i has weight
i + 1, and the reflection s -> -s makes it odd under k_i -> (-1)^i k_i. With D_l = (1 + k'^2)^{-1/2} D_s,
kappa^(r)(0) = D_l^r [k''(1 + k'^2)^{-3/2}] at s = 0; since k'(0) = 0, this is k_r plus a polynomial in
k_0, ..., k_{r-1}, and since the reflection s -> -s sends kappa^(r)(0) to (-1)^r kappa^(r)(0), for odd r each monomial
of that polynomial contains a factor k_i with i odd. Hence, if 2j + 1 is the least odd order with
kappa^(2j+1)(0) != 0, then k_i = 0 for odd i < 2j + 1, sigma_m = 0 for m < 2j + 3 and
sigma_{2j+3} = c_j kappa^(2j+1)(0) with a constant c_j. To determine c_j, put F(s) = s^{2j+3}/(2j+3)!, k = eps F and
H = 2(z - eps F)^2 + eps q + O(eps^2). Then Lap q = 4z F'' and q = q_z = 0 on z = 0, so for q = sum q_l(s) z^l one has
q_0 = q_1 = q_2 = 0, q_3 = 2F''/3 and q_{l+2} = -q_l''/((l+2)(l+1)) for l >= 2; for sigma = eps eta + O(eps^2),
invariance gives 4z eta' = 4(-1)^j z^{2j+3}/(2j+3)!, hence c_j = (-1)^j/((2j+3)(2j+3)!). If every odd-order derivative
of kappa vanishes, the Taylor series of k is even and the parity gives a flat sigma. Exact symbolic computation
confirms the coefficients of sigma up to z^6 and the constants c_j up to the order 15. (c) Choose z_* with
|z_*| < delta and a = sigma(z_*) in (0, delta). For 0 < s_0 < a the line s = s_0 meets C at a point with |z| <= |z_*|
(intermediate value theorem), where Omega(s_0, .) is flat by (a); it is real analytic, so Omega = 0 on
(0, a) x (-delta, delta). From here the proof of (xii)(c), with R_+ replaced by this rectangle, gives f = 0 on an
interval (0, delta'''); then the arc z = k(s), 0 < s < delta''', lies in Z and is connected to gamma through p, which
contradicts the maximality of the component gamma for every type of p. (d) Near interior points of gamma, Z lies in a
regular nullcline and coincides with gamma, and at a nonaccumulating endpoint f != 0 on (0, eps); so gamma is isolated
in Z. In a thin tube around gamma the zero set of the normal component is a regular curve along gamma and beyond its
endpoints, and a homotopy without zeros on the boundary reduces the index to the signs of the tangential component at
the two ends of that curve, which are -eps_- and eps_+ with eps = +1 for an outgoing and -1 for an incoming endpoint;
this gives the index (eps_- + eps_+)/2. S conjugates the flow to itself and exchanges p_+ and p_-, so the types agree,
and W = 2X + o(|X|) has degree 1 on large circles. Choose an open neighbourhood U_gamma of gamma with
Z cap U_gamma = gamma; the exterior zeros form the compact set Z minus U_gamma, which is finite if its points are
isolated; trace DW = 4 gives each a nonzero eigenvalue, and the reduction to a center manifold when DW is singular
gives indices in {-1, 0, +1}, so the count follows. On the axis W_1(0, y) = 0 and DW is diagonal; the zeros of
b(y) = W_2(0, y) other than 0 have total one-dimensional index 0 (b has degree 1 on a large interval, as at 0); at
each of them DW = diag(4 - d, d) with d = b'(y), and the planar index is at most the one-dimensional one: if d != 4,
reduction using W_1 multiplies the one-dimensional index by sgn(4 - d), and that index is +1 when d > 4, while if
d = 4 the one-dimensional index is +1 and the planar one is at most +1; so the off-axis indices sum to at least 2 and
come in pairs q, S q of equal index, and some zero of index +1 lies in {x > 0}. At a zero q of index +1 with DW(q)
nonsingular, (T) differentiated at q gives DW(q)^T grad Theta(q) = 0, so grad Theta(q) = 0, Omega(q) = Theta_x(q) = 0
by (V), and DW(q) is symmetric with trace 4 and positive determinant; if DW(q) has eigenvalues 0 and 4, coordinates
straightening a center manifold and the strong unstable curve give u' = g(u) + u v B, v' = v D with D > 2 and
g(u)/u > 0 for small u != 0. In both cases small backward invariant neighbourhoods (in the second case |v| < eps,
|u| e^{K|v|} < eta with K large) have all backward orbits converging to q; transport gives Theta = Theta(q) there, and
(V), as in the proof of (xii)(b), gives Omega = 0.
Scope of (xiii). (a), (b) and (d) are necessary conditions, (c) is a restricted exclusion. Flatness along C does not
give vanishing on a neighbourhood of any point of C (at outgoing endpoints, and at incoming endpoints with isolated
zeros off gamma, such a vanishing is impossible by (xv)), and the potential H in the proof of (b) is only a formal
series satisfying Lap H = 4; no convergent potential or harmonic neighbourhood is obtained. At outgoing endpoints (c)
adds nothing to (xii)(c), which needs no condition on C; at incoming and accumulating endpoints it needs, besides the
transverse analyticity of (xii)(c), which is not derived from the equations, the condition that C meets {s > 0} in
every neighbourhood of p, which is not derived from the equations when every odd-order derivative of kappa vanishes
at 0. The degree 2 in (d) is not a contradiction, and the source pair is derived under the isolation of the exterior
zeros. When the endpoints are incoming and the zeros of W off gamma are isolated, the condition on C in (c) can be
dropped ((xiv)(d)), and so it can at an accumulating endpoint if some neighbourhood of it contains no arc of zeros of
W off gamma ((xx)(c)). Neither incoming nor accumulating endpoints are excluded in general for smooth profiles.
(xiv) Incoming endpoints with isolated zeros off the arc (beta = 2). In the setting of (iii), suppose that the
endpoints of gamma are incoming (case (c) of (iv); the two endpoints have the same type by (xiii)(d)) and that every
zero of W off gamma is isolated. Let p be an endpoint, L = Theta(p), C the strong unstable curve of p of (xiii), C_+
the orbit of step (2) of the proof of (v)-(vii) (the exterior center branch at p, with forward limit p), and, for a
zero q of W, B(q) the set of points whose backward orbits converge to q.
(a) The zeros of W off gamma are finitely many, and the backward orbit of every point converges to a single zero of W.
The set K of points with bounded forward orbit is the union of gamma, the zeros off gamma and finitely many orbits,
each converging in both time directions to zeros of W; K is connected and contains no Jordan curve.
Theta(R^2) = Theta(gamma).
(b) Near p, C_+ divides the side of C beyond p (the side not meeting gamma) into two sectors. Each of them,
intersected with a small enough disk around p, lies in the interior of B(q) for a zero q off gamma that is a source
(the backward orbits of all points of a neighbourhood of q converge to q) or a zero of index 0 at which DW(q) has
eigenvalues 0 and 4; no equality between the zeros for the two sectors, or of either with the backward limit of C_+,
is asserted. Consequently there is a disk N around p such that Theta = L and Omega = 0 at the points of N on C and on
the side of C beyond p, and U is harmonic on that side in N.
(c) Theta - L does not vanish identically on any neighbourhood of p. Equivalently, Theta is not constant on any
nondegenerate subarc of gamma that has p as an endpoint.
(d) There is no delta > 0 such that, in the coordinates (s, z) of (iv) at p, z -> U(0, z) is real analytic on
(-delta, delta) and, for every s in (0, delta), z -> Omega(s, z) is real analytic on (-delta, delta); that is, the
conclusion of (xii)(c) holds at p without the condition on C in (xiii)(c).
(e) C does not agree near p with any regular real analytic embedded curve through p; equivalently, at least one of the
two branches of C at p has no real analytic extension through p.
(f) If moreover DW(q) is invertible at every zero q of W off gamma, every derivative of Theta of order >= 1 vanishes
at every point of gamma that is a backward or forward limit of an orbit of K not contained in gamma. Consequently W
has no zero on the axis other than 0, and each open half-axis is one orbit, with backward limit 0, that escapes to
infinity.
Proof outline. (a) By the proof of (iii), W.X >= |X|^2 outside a large disk D_R, so D_R is backward invariant, every
backward orbit enters it, and a forward orbit is bounded exactly when it stays in D_R; by step (1) of the proof of
(v)-(vii), every alpha-limit set, and the omega-limit set of every bounded forward orbit, is a nonempty compact
connected subset of Z. Near interior points of gamma, Z coincides with gamma, and f < 0 on (0, eps) at both endpoints,
so gamma has a neighbourhood containing no other zero of W; Z is compact, so the isolated zeros off gamma are finitely
many, and a connected subset of Z is one zero off gamma or a subset of gamma. Near a compact subarc of the interior of
gamma, in coordinates (a, b) with gamma = {b = 0}, a' = b A and b' = b D, D >= d0 > 0, a backward orbit from a thin
neighbourhood satisfies |b(-t)| <= |b(0)| e^{-d0 t} and |a(-t) - a(0)| <= sup|A| |b(0)|/d0 and converges to one point
of gamma; so an alpha-limit set that meets the interior of gamma is a single point, and one in {p_+, p_-} is a single
point since it is connected. For a shorter interior subarc and a normal width small compared with its tangential
margin, every nonstationary orbit starting close enough to that subarc leaves the thin neighbourhood forward through
an edge |b| = const, so repeated approaches of a forward orbit to an interior point of gamma would give a regular
omega-limit point on that edge, contrary to step (1); hence the omega-limit set of a bounded nonstationary forward
orbit is one zero off gamma or one endpoint. At a zero q off gamma, trace DW(q) = 4: if det DW(q) < 0, q is a saddle
with two forward-stable orbits; if det DW(q) > 0, q is a source; if DW(q) has eigenvalues 0 and 4, coordinates
straightening a center manifold and the strong unstable curve give u' = g(u) + u v B, v' = v D with D > 2 and g of one
sign on each side of 0, the forward-stable orbits are the sides of {v = 0} on which u g(u) < 0, and q is a source if
u g(u) > 0 on both sides; at p the only forward-stable orbit off gamma is C_+. Hence K consists of gamma, the zeros
off gamma and finitely many connecting orbits. A Jordan curve in K consists of orbits and zeros, so its bounded
interior D is invariant, which contradicts |phi_t D| = e^{4t} |D|. K is the intersection of the nested compact disks
phi_{-t}(D_R), t >= 0, hence connected, so every zero off gamma is joined to gamma by a chain of connecting orbits;
Theta is constant on orbits and continuous, so Theta(X) = Theta(alpha(X)) for every X, and Theta takes at each zero
off gamma a value of Theta on gamma. (b) Take the coordinates (u, v) of step (3) of the proof of (v)-(vii) at p, with
C = {u = 0}, gamma near p in {u <= 0, v = 0} and C_+ in {u > 0, v = 0}, now with g < 0 for u > 0 (case (c)). Choose
u_0 > 0 small and then delta > 0 so that g(u_0) + u_0 v c(u_0, v) < 0 for |v| <= delta. Along the backward orbit of a
point with 0 < u(0) < u_0 and |v(0)| <= delta, in backward time tau, |v(tau)| <= |v(0)| e^{-2 tau}; with
A(tau) = int_0^tau v c and w = u e^A, |A| <= sup|c| |v(0)|/2 and dw/dtau = -g(u) e^A > 0, so u cannot stay in (0, u_0)
(it would have a positive limit, and dw/dtau a positive lower bound), and the orbit reaches
J = {u = u_0, |v| <= delta} with v of unchanged sign, after a time at least log(u_0/u(0))/M, where M bounds
|g(u)/u| + delta sup|c|; so |v| at J tends to 0 uniformly as u(0) -> 0, and the exit map extends continuously by the
point of C_+ on J. The same passage holds at every zero off gamma along each of its forward-stable orbits: at a
hyperbolic saddle, in coordinates with u' = -u E_1 and v' = v E_2, E_1, E_2 > 0, each side of an unstable branch
passes backward to the adjacent side of a stable branch, with exit height tending to 0; at a zero with eigenvalues 0
and 4 the same integrating-factor argument applies on each incoming center side, and an outgoing center side lies in
the open backward basin. Follow the half of J with v > 0 backward along C_+ to q_0 = alpha(C_+): if a small
half-segment of J next to C_+ lies in the interior of B(q_0), stop; otherwise the passage at q_0 carries a small
half-segment next to C_+ to a small half-segment next to a forward-stable orbit q_1 -> q_0 on the same side, and the
step is repeated at q_1. The chain q_k -> ... -> q_0 -> p never reaches gamma and never repeats a zero, since
otherwise it would close, with a subarc of gamma or by itself, to a Jordan curve in K; so after finitely many steps it
reaches a zero q such that the half-segment lies in the interior of B(q), and q is a source or a zero of index 0 with
an open basin on one side. A composition of finitely many continuous passage maps sends a small half of J, hence the
whole sector near p on the side v > 0, into the interior of B(q). On that open invariant set Theta = Theta(q) by
transport, and Omega(Y) = e^{-T} Omega(phi_{-T} Y) -> 0 as T -> infinity by (V), since Theta_x = 0 there and backward
orbits are bounded; Theta(q) = L because the sector accumulates at p. The sector v < 0 is treated in the same way, and
Theta = L, Omega = 0 on C near p by continuity. (c) If Theta = L on a disk around p, the backward orbits from a
smaller disk in {u <= 0} stay in the first disk (as in the proof of (xii)(b); g = 0 for u <= 0), so Omega = 0 there by
(V); with (b), Omega = 0 on a neighbourhood of p, contrary to (xii)(a). If Theta = L on a nondegenerate subarc of
gamma ending at p, the points near p with u < 0 have backward limits on that subarc, so Theta = L there, and (b) gives
Theta = L for u >= 0. The converse is immediate. (d) For small s > 0, C_+ is a graph z = m(s), and the points (s, z)
with z slightly above m(s) lie in one of the sectors of (b), where Omega = 0. If delta as in (d) existed, the identity
theorem would give Omega = 0 on (0, a) x (-delta, delta) for some a > 0, and the proof of (xii)(c), with R_+ replaced
by this rectangle, would give an arc z = k(s), 0 < s < delta''', in Z and connected to gamma through p, contradicting
the maximality of the component gamma (as in the proof of (xiii)(c)); only one sector is used. (e) If C agreed near p
with a regular real analytic curve, (b) would give Omega = 0 on the side of C beyond p in a small disk, and step (5)
of the proof of (v)-(vii), applied to that side, would give a real analytic field W~ near p with the jet of W at p and
equal to W on that side; the reduced field of W~ on its analytic normal nullcline has the flat Taylor series of f,
hence vanishes, and its zero arc for s > 0 lies on that side, so W would vanish on an arc z = k(s), 0 < s < delta''',
contradicting the maximality of gamma. If both branches of C had real analytic extensions through p, these would have
the same Taylor series at p, since C is smooth, and would form one regular real analytic curve containing C near p.
(f) Let T be a component of the union of the zeros off gamma and the orbits of K joining two of them. T is a finite
tree, and exactly one orbit of K joins T to gamma: at least one since K is connected, and two would close, with a path
in T and a subarc of gamma, or at a common point of gamma, to a Jordan curve in K. If every DW(q) is invertible, each
zero off gamma is a source or a saddle, and a saddle has two forward-stable orbits in K; so a vertex of T at which
only one orbit of K ends, which exists (a leaf of T not joined to gamma, or the single vertex of T), is a source, near
which Theta is constant. If every derivative of Theta of order >= 1 vanishes at a hyperbolic zero q, the same holds at
every point of an orbit converging to q in forward or backward time, since the convergence is exponential and the
derivatives of phi_t of each order grow at most exponentially (as in the proof of (xiii)(a)), and then, by continuity,
at the other limit of that orbit. Passing from that source along T and then along the orbit joining T to gamma gives
the assertion at its point on gamma. At 0, Theta_xx(0) = 2 a0 != 0. If W had a zero on the axis other than 0, the
nearest one above or below 0 would be the forward limit of the axis orbit issuing from 0 (W_1(0, y) = 0,
W_2(0, y) = 4y + O(y^2), and these zeros are finitely many), an orbit of K with backward limit 0, which is impossible;
hence W_2(0, y) != 0 for y != 0, and W.X > 0 for large |X| makes each open half-axis one orbit that escapes to
infinity.
Scope of (xiv). The conclusions assume incoming endpoints and isolated zeros of W off gamma, and (f) assumes in
addition that every zero off gamma is nondegenerate; these hypotheses are not derived from the equations. Accumulating
endpoints are treated in (xx). Part (b) gives at an incoming endpoint the structure that (iv) gives at an outgoing
one: Theta = L and Omega = 0 on the whole side of C beyond p near p, the two open sectors lying in basins of zeros off
gamma; (c), (d) and (e) are the analogues of (xii)(b), (xii)(c) and (vi): (c) and (e) are necessary conditions, and
(d) is a restricted exclusion that needs the transverse analyticity of (xii)(c), which is not derived from the
equations. The vanishing of Theta - L or of Omega on a whole neighbourhood of p is excluded by
(c) and (xii)(a); the vanishing of Omega on a neighbourhood of a point of C other than p is impossible ((xv)(b)), so,
as at outgoing endpoints, U is not harmonic on any neighbourhood of any point of C, and a harmonic extension of the
restriction of U to the side beyond C across a point of C other than p, differing from U on the other side, is not
established; through p itself it is impossible ((xix)(a), (e)). The backward limit q_0 of C_+ is not asserted to have
an open basin: a smooth planar field W with div W = 4, the parity of (iii), W - 2X bounded, DW(0) = diag(0, 4), a
compact zero arc through 0 with flat incoming endpoints and finitely many other zeros
(four sources and two saddles) has a saddle as the backward limit of the exterior center branch at each endpoint; this
field is not the W of a profile, since near 0 it equals (0, 4y), so that Omega = 0 there and (V) would give
Theta_x = 0, contrary to a0 != 0. Part (f) gives the flatness of Theta at every attachment point on gamma
and excludes only a zero of W on the axis other than 0. Smooth profiles with incoming endpoints are not excluded, in
particular not those whose zeros off gamma are finitely many and nondegenerate and which satisfy the necessary
conditions (c), (e) and (f).
(xv) No isothermal and no harmonic neighbourhood of a point of the strong unstable orbits (beta = 2). In the setting
of (iii), let p be an endpoint of gamma that is outgoing (case (b) of (iv)), or incoming (case (c)) with every zero of
W off gamma isolated; let L = Theta(p), let C be the strong unstable curve of p ((xiii)), and let C^ be the union of
the orbits of the points of C (p and the two orbits that contain the two components of C minus p). Then:
(a) Theta - L does not vanish identically on any neighbourhood of any point of C^.
(b) Omega does not vanish identically on any neighbourhood of any point of C^; equivalently, U is not real analytic on
any neighbourhood of any point of C^.
(c) If Z = gamma, let O_+ be the set of points not in C^_+ (the set C^ of p_+) whose backward limit is p_+, and
O_- = S O_+. Then O_+ is open, connected and invariant, Theta = L and Omega = 0 on O_+, the boundary of O_+ is
contained in the union of C^_+ and C^_- = S C^_+, and O_+ is a connected component of the interior of the zero set of
Omega and of the interior of the level set {Theta = L}; likewise for O_-.
Proof outline. Take the coordinates (u, v) and the rectangles Q, Q' of the proof of (xii)(b) at p, so that C = {u = 0}
and gamma = {v = 0, u <= 0} near p, g = 0 for u <= 0, and g > 0 (outgoing) or g < 0 (incoming) for u > 0. Let Q'' be
an open rectangle about p with closure contained in Q', and set E = Q'' n {u > 0}; at an outgoing endpoint choose Q''
so that every backward orbit from Q'' stays in Q', and at an incoming endpoint choose Q'' inside the disk of (xiv)(b).
Then Theta = L and Omega = 0 on E: at an incoming endpoint by (xiv)(b); at an outgoing endpoint because the backward
orbits from Q' stay in Q and, for u > 0, converge to p (step (3) of the proof of (v)-(vii)), so Theta = L on
Q' n {u > 0}, and (V) gives Omega(Y) = e^{-sigma} Omega(phi_{-sigma} Y) -> 0 for Y in E, as in the proof of (xii)(b).
Every point X of C^ other than p is X = phi_T X_1 with T >= 0 and X_1 = (0, v_1) in Q'', v_1 != 0. For X = p, (a) is
(xii)(b) or (xiv)(c), and (b) is (xii)(a). (a) Suppose Theta = L on a disk N around X. Theta is constant on orbits, so
Theta = L on the neighbourhood phi_{-T} N of X_1. For u < 0 small, the backward orbit of (u, v_1) stays in Q, where
u' = u v b and |v(-sigma)| <= |v_1| e^{-2 sigma}; so it converges to a point (u_-(u), 0) of gamma,
|log|u_-(u)| - log|u|| <= B|v_1|/2, and the convergence is uniform in u (the integral of |v b| over backward times
after sigma is at most B |v_1| e^{-2 sigma}/2). Hence u_- is continuous and negative on a small interval (-eps, 0) and
tends to 0 as u -> 0-, so, by the intermediate value theorem, its image contains the interval (-eta, 0) with
eta = -u_-(-eps/2) > 0; the points (u, v_1) with -eps < u < 0 lie in phi_{-T} N for small eps, so Theta = L on the
nondegenerate subarc {(u, 0) : -eta < u < 0} of gamma ending at p, which (xii)(b) and (xiv)(c) exclude. (b) Suppose
Omega = 0 on a disk N around X. Then div U = 0 and curl U = 0 on N, so U is harmonic and W is real analytic on N; (V)
gives Theta_x = 0 on N, and then (T) gives W_2 Theta_y = 0 on N. If W_2 is not identically 0 on N, its zero set in N
has empty interior, so Theta_y = 0 on N, Theta is constant on N and equal to Theta(X) = L, which (a) excludes. If
W_2 = 0 on N, let G be the union of N and of the sets phi_r(E), 0 <= r <= T. Theta = L on the open set phi_r(E), so
Theta_x = 0 there, and (V) gives Omega(phi_r Y) = e^{-r} Omega(Y) = 0 for Y in E; G is open and connected (E is
connected, each point of phi_r(E) is joined to E by an orbit segment in G, and N meets phi_T(E) because X_1 lies on
the boundary of E), and U is harmonic on G. The real analytic function W_2 vanishes on N, hence on G; then
d_x W_1 = div W = 4 and d_y W_1 = d_x W_2 + Omega = 0 on G, so W = (4x + c, 0) on G for a constant c. In particular
DW = 4 e_1 (x) e_1 on E, with e_1 = (1, 0), and continuity at p and DW(p) = 4 n (x) n give n = +-e_1, so the tangent
of gamma at p is +-e_2, e_2 = (0, 1). Write C as a graph s = sigma(z); since k(s) = O(s^2) and sigma(z) = O(z^2),
s - sigma(k(s)) = s + O(s^4) > 0 for small s > 0, so the points (s, k(s)) of (iv) with small s > 0 lie on the side
u > 0 and in Q'', hence in E, and there W is f(s) times that unit tangent, so W_2 = +-f(s) != 0 for small s > 0 in
cases (b) and (c) of (iv): a contradiction. If U is real analytic on a disk N around X, so is Omega, which vanishes on
the nonempty open set N n phi_T(E), hence on N; conversely Omega = 0 on N makes U harmonic. (c) By (v), both endpoints
are outgoing and every point off gamma has a backward limit that is one point of gamma. A point of O_+ has a backward
orbit that enters Q'' and stays there; at those times u != 0, since u < 0 would give a backward limit (u_-, 0) != p_+
and u = 0 would put the point on C^_+, so u > 0 and the point lies in phi_T(E) for some T >= 0; conversely the points
of E have backward limit p_+ and are not in C^_+, because u stays positive along their backward orbits while the
backward orbit of a point of C^_+ ends on {u = 0}. So O_+ is the union of the sets phi_T(E), T >= 0, which is open,
connected and invariant, with Theta = L and Omega = 0 as in (b). Let F be the set of points whose backward limit is an
interior point of gamma, including these points themselves. F is open: near an interior point of gamma, in coordinates
(a~, b~) with gamma = {b~ = 0}, a~' = b~ A~ and b~' = b~ D~ with D~ >= d_0 > 0, so |b~| decreases backward and
|a~(-t) - a~(0)| <= sup|A~| |b~(0)|/d_0, and a small neighbourhood of a subarc of interior points lies in F; the
forward images of such neighbourhoods cover F. So the complement of the disjoint open sets F, O_+ and O_- is C^_+
united with C^_-, and it contains the boundary of O_+. A connected open set on which Omega = 0 that contains O_+ and
is larger would contain a boundary point of O_+ together with a neighbourhood on which Omega = 0, which (b), at p_+ or
at p_-, excludes; likewise for {Theta = L} with (a), since Theta(p_-) = Theta(p_+) = L.
Scope of (xv). (a), (b) and (c) are necessary conditions. Theta - L and Omega vanish to every order on C^ ((xiii)(a)
and invariance), and Theta = L, Omega = 0 on the side of C beyond p near p, so by (a) and (b) every neighbourhood of a
point X = phi_T X_1 of C^ contains points at which Theta != L and points at which Omega != 0, although both vanish on
phi_T(E), on one side of the orbit of X near X. Hence, for a profile in the setting of (xv), neither Theta - L nor
Omega vanishes on a whole neighbourhood of a point of C^, and U is not harmonic on any such neighbourhood; when
Z = gamma this holds at every boundary point of O_+ and O_-. So the closure step described in the Scope of (iii)-(iv)
and in 6.3, read as such a vanishing at a boundary point of the basin or as the harmonicity of U itself near it,
cannot be derived at a point of C^ unless the class is empty. At a point of C^ other than p, (xv) does not exclude a
harmonic extension of the restriction of U to phi_T(E), or to O_+, that differs from U on the other side of the orbit.
Nothing is claimed at the points of the strong unstable orbits other than the endpoint for accumulating endpoints or
for incoming endpoints without the isolation of the zeros off gamma (at the endpoint itself, (xii)(a) and (xxi)
apply), or for boundary points of the basins of (iv) and (xiv)(b) that are not in C^ when Z != gamma. No profile is
excluded.
(xvi) Global decomposition in the subclass Z = gamma (beta = 2). Assume Z = gamma, let L = Theta(p_+) = Theta(p_-),
let C^_+, C^_- = S C^_+, O_+ and O_- = S O_+ be as in (xv)(c), and let F be the set of points whose backward limit is
an interior point of gamma, these points included (proof of (xv)(c)). Then:
(a) C^_+ is a smooth embedded curve, closed in R^2 and homeomorphic to R (a properly embedded line); each of the two
orbits in C^_+ other than p_+ has backward limit p_+ and escapes to infinity in forward time. C^_+ and C^_- are
disjoint, and C^_+ lies in {x > 0}.
(b) F, O_+ and O_- are the three connected components of the complement of the union of C^_+ and C^_-, and each of
them is simply connected. The boundary of O_+ is C^_+, that of O_- is C^_-, and that of F is the union of C^_+ and
C^_-. F = S F contains gamma minus its endpoints and the whole axis {x = 0}, and O_+ lies in {x > 0}.
(c) Theta = L and Omega = 0 on the closed set R^2 minus F, which is the union of the closures of O_+ and O_-, and U is
harmonic on its interior, the union of O_+ and O_-. Every point of the boundary of F is a limit of points of F at
which Theta != L and of points of F at which Omega != 0.
(d) In the notation of (v), the asymptotic directions of the orbits in O_+ form the interior of the arc I_+, and the
asymptotic directions of the two orbits in C^_+ other than p_+ are the two endpoints of I_+; likewise for O_-, C^_-
and I_-, and the asymptotic directions of the orbits in F other than the points of gamma form the union of Gamma_+ and
Gamma_-.
Proof outline. (a) Let X^1 and X^2 be points of the two components of C minus p_+ in the rectangle Q'' of the proof of
(xv). Their backward orbits stay on C and tend to p_+ (C is the strong unstable curve), and the two orbits are
distinct, since the backward orbit of a point of one component stays in that component. By (v), the set of points with
bounded forward orbit is gamma = Z, and X^1, X^2 are not zeros of W; so the forward orbits of X^1 and X^2 are
unbounded, and since d|X|^2/dt = 2 W.X >= 2|X|^2 outside a large disk (proof of (iii)-(iv)), |X(t)| -> infinity. The
intersection of C^_+ with Q'' is C n Q'': backward orbits from Q'' stay in Q'; for a point with u(0) < 0, u' = u v b
gives u(-sigma) -> u_- = u(0) exp(-int_0^infinity (v b)(-r) dr) < 0, since the integral has absolute value at most
B |v(0)|/2, so the point lies on gamma or has an interior point of gamma as backward limit; a point with u(0) > 0 lies
in E and keeps u > 0 backward, so it is not in C^_+: the backward orbit of a point of C^_+ lies exactly on {u = 0} at
all sufficiently negative times (its backward tail lies in C n Q''); and the points with u = 0 lie on C. Define
c(t) = phi_{log(-t)} X^1 for t < 0, c(0) = p_+ and c(t) = phi_{log t} X^2 for t > 0. The two branches cover the two
complete orbits; the backward limits give continuity at 0; the distinctness of the orbits and the absence of periodic
orbits (both escape) give injectivity; and the forward escape gives |c(t)| -> infinity as |t| -> infinity. So c is
proper, hence a closed embedding. Its image C^_+ is a smooth embedded curve: near p_+ it is the arc C n Q'', which is
smooth by (xiii), and near any other point it is an arc of an orbit along which W != 0 (flow box). C^_+ and C^_- are
disjoint, since their points have different backward limits. A point Y of C^_+ on the axis would satisfy Y = S Y,
which lies in C^_-, so C^_+ does not meet the axis; it is connected and contains p_+, with x(p_+) > 0, so it lies in
{x > 0}. (b) By (v) every point off gamma has a backward limit that is one point of gamma, so R^2 is the disjoint
union of F, O_+, C^_+, O_- and C^_-; F, O_+ and O_- are open (proof of (xv)(c)). Each is connected: O_+ by (xv)(c),
O_- = S O_+, and F because each of its points is joined within F to its backward limit by its backward orbit, and
gamma minus its endpoints is connected. Three disjoint nonempty connected open sets whose union is an open set are its
components. Since c is proper, c extends to an embedding of the circle obtained from R by adding one point into the
sphere obtained from R^2 by adding the point infinity, so by the Jordan curve theorem R^2 minus C^_+ has two
components, each with boundary C^_+. The one, A, that does not contain the connected set C^_- is open, connected and
disjoint from C^_+ and C^_-, and it is closed in the complement of their union (its closure is the union of A and
C^_+), so A is one of F, O_+, O_-. The closures of F and of O_- contain p_- (F contains gamma minus its endpoints, and
O_- contains the set S E, which has p_- in its closure), while the closure of A, the union of A and C^_+, does not; so
A = O_+, and the boundary of O_+ is C^_+; likewise for O_-. A point Y of C^_+ is a limit of points of the other
component of R^2 minus C^_+, which is the union of F, O_- and C^_-; the closed set formed by O_- and C^_- does not
contain Y, so these points lie in F near Y. Hence the boundary of F, which is contained in the union of C^_+ and C^_-,
is that union. A connected open subset of R^2 whose complement in the sphere is connected is simply connected. The
complement in the sphere of each of F, O_+, O_- is connected (it is the union of the connected set formed by C^_+,
C^_- and the point infinity, and of the closures of the other two components, whose boundaries lie in that set), so
each of them is simply connected. The axis is connected, contains 0, which lies on gamma minus its endpoints, and does
not meet C^_+ or C^_-, so it lies in F. O_+ is connected, does not meet the axis and contains E, near p_+, so it lies
in {x > 0}. S F = F, because W(SX) = S W(X) makes S map orbits to orbits and S maps gamma minus its endpoints to
itself. (c) Theta = L and Omega = 0 on O_+ by (xv)(c), hence on O_- = S O_+ (Theta is even and Omega is odd), and by
continuity on the closures of O_+ and O_-, whose union is R^2 minus F by (b). On the open set formed by O_+ and O_-,
div U = 0 and curl U = 0, so U is harmonic. By (xv)(a) and (b), applied at p_+ and at p_-
(Theta(p_-) = Theta(p_+) = L), every neighbourhood of a point of C^_+ or C^_- contains points at which Theta != L and
points at which Omega != 0, and these points lie in F. (d) By (v), the set of points with bounded forward orbit is
gamma, and every unbounded forward orbit escapes, so the escape set of 4.12 step (7) is R^2 minus gamma. The profile
is in class A by 4.15 (case beta = 2), so 4.12 step (7) gives a C^1 diffeomorphism Phi of R^2 minus gamma onto
R^2 minus 0 with Phi o phi_s = e^{2s} Phi. Thus each orbit off gamma is mapped onto an open ray, its asymptotic
direction is Phi(Y)/|Phi(Y)|, and distinct orbits have distinct directions. Since O_+ is nonempty, open, connected and
invariant, the set J_+ of directions of its orbits is nonempty, open and connected, and Phi(O_+) is the set of points
with direction in J_+; J_+ is not the whole circle, since the upper half-axis lies in F. By (b), the boundary of O_+
relative to R^2 minus gamma is C^_+ minus p_+, which Phi maps onto the two rays of the directions of the two orbits in
C^_+ other than p_+; so these two distinct directions form the boundary of J_+ in the circle, J_+ is an open arc, and
its closure is a nondegenerate closed arc with these two endpoints. The orbits with backward limit p_+ are those in
O_+ and the two orbits in C^_+ other than p_+, so this closure is I_+ as defined in (v). Reflection gives the
assertion for O_-, C^_- and I_-, and the directions of the orbits in F off gamma form the union of Gamma_+ and Gamma_-
by the definition in (v).
Scope of (xvi). (a) to (d) are necessary conditions; no profile is excluded. In the subclass Z = gamma all points at
which Theta != L or Omega != 0 lie in the simply connected region F, bounded by the two disjoint mirror lines C^_+ and
C^_- that pass through the endpoints and escape to infinity at both ends. Outside F, Theta = L and Omega = 0, and U is
harmonic on O_+ and on O_-; Theta - L and Omega vanish to every order on the two lines ((xiii)(a) and invariance, or
continuity of the derivatives from the basins), but neither vanishes identically near any point of either line, and U
is not harmonic near any such point ((xv)). By (d), the closed arcs I_+ and I_- of (v), on which h = L and a = 0, are
exactly the asymptotic directions of the escaping orbits in the closures of O_+ and of O_-, respectively (the
stationary points p_+ and p_- omitted); this does not identify them with the set of all zeros of a or with the set of
all directions at which h = L. The two lines and the harmonic velocity on the basins are not determined. Nothing is
claimed about the existence of such a configuration or about profiles with zeros of W off gamma.
(xvii) Quasianalytic Denjoy-Carleman classes (beta = 2). Let m = (m_k)_{k >= 0} be a sequence of positive numbers with
m_0 = 1, m_k^2 <= m_{k-1} m_{k+1} for k >= 1, D_m = sup_{k >= 1} (m_{k+1}/m_k)^{1/k} < infinity and
sum_{k >= 1} m_{k-1}/m_k = infinity. For an open set G of R^2, let C{m}(G) be the set of smooth functions f on G such
that for every compact set K in G there are constants A > 0 and B > 0 with |d^alpha f| <= A B^{|alpha|} m_{|alpha|} on
K for every multi-index alpha; a vector field is in C{m}(G) when its components are. For m_k = k! this is the set of
real analytic functions on G.
(a) In the setting of (ii), Theta is not in C{m}(R^2).
(b) In the setting of (iii), let p be an endpoint of gamma. For no open neighbourhood N of p is Omega or U in C{m}(N),
and for no connected open set G containing gamma is Theta in C{m}(G).
(c) In the setting of (b), suppose in addition that p is outgoing, or incoming with every zero of W off gamma
isolated. Then for no open neighbourhood N of a point of the set C^ of (xv) is Theta, Omega or U in C{m}(N).
(d) In the setting of (c), let A be a smooth open arc contained in C^ (for example the relative interior of a
sufficiently short compact subarc of C through p, or of a compact segment of one of the two orbits in C^), and let
(s, t) be positively oriented orthonormal coordinates in which A = {(s, g(s)) : s in I} for an open interval I and a
smooth function g on I. Call a subset of I meager when it is contained in a countable union of closed subsets of I
with empty interior; the complement of a meager set is dense in I. There is a meager set M_0 in I such that for every
s in I minus M_0 the functions t -> Theta(s, t) - L and t -> Omega(s, t) vanish to infinite order at t = g(s) and
vanish identically on no open interval containing g(s); in particular, for every sequence m as above, neither is in
C{m} on any open interval containing g(s). For every sequence m as above there is a meager set M_m in I such that for
every s in I minus M_m the vector function t -> U(s, t) is not in C{m} on any open interval containing g(s). Here a
smooth function of one variable is in C{m} on an open interval J when for every compact subinterval K of J there are
A > 0 and B > 0 with |h^(k)| <= A B^k m_k on K for every k >= 0. For countably many sequences m the union of M_0 and
the sets M_m is again meager.
Proof outline. Three facts about C{m}. (1) If f is in C{m}(G), q is in G, e is a unit vector and the open disk D(q, r)
lies in G, then g(t) = f(q + t e) satisfies, on every compact subinterval of I = {t : q + t e in D(q, r)},
|g^(k)(t)| = |(e.grad)^k f(q + t e)| <= sum_{|alpha| = k} (k!/alpha!) |e_1|^{alpha_1} |e_2|^{alpha_2} |d^alpha f| <=
A (2B)^k m_k, with A, B the constants of the image compact set, since sum_{|alpha| = k} (k!/alpha!)
|e_1|^{alpha_1} |e_2|^{alpha_2} = (|e_1| + |e_2|)^k <= 2^k. (2) C{m}(G) is a vector space containing the constants,
and partial derivatives of its elements are in it: |d^alpha d_j f| <= A B^{k+1} m_{k+1} <=
A B max(m_1, 1) (B D_m)^k m_k for |alpha| = k, because m_{k+1} <= D_m^k m_k for k >= 1. (3) If f is in C{m}(G), G is
connected and f vanishes to infinite order at one point of G, then f = 0 on G. Indeed, we use the Denjoy-Carleman
theorem in the following form: let J = [a, b], a < b, and let g be smooth on a neighbourhood of J with |g^(k)(t)| <=
A B^k m_k for every t in J and k >= 0, where A > 0, B > 0 and m is positive and log-convex with m_0 = 1 and
sum_{k >= 1} m_{k-1}/m_k = infinity; if every derivative of g vanishes at some point t_0 of J (possibly an endpoint),
then g = 0 on J. (Replacing g by g/A and m_k by B^k m_k keeps log-convexity and multiplies the series by 1/B.) With
(1), if f vanishes to infinite order at q and D(q, r) is as in (1), then for every e the function g vanishes to
infinite order at t = 0, its derivatives there being (e.grad)^k f(q) = 0, so g = 0 on every compact subinterval of I
containing 0, hence on I, and f = 0 on D(q, r). So the set of points of G at which f vanishes to infinite order is
open; it is closed in G, nonempty, and equal to G. (a) By (ii) there is a point p at which every derivative of Theta
of order >= 1 vanishes. If Theta were in C{m}(R^2), (3) applied to Theta - Theta(p) (in C{m}(R^2) by (2)) would give
Theta = Theta(p) on R^2, which contradicts a0 != 0. (b) By (iii), Omega and Theta - L vanish to infinite order at p.
If Omega were in C{m}(N), then Omega = 0 on a disk around p by (3), so U would be divergence free and curl free on
that disk, hence harmonic and real analytic there, which (xii)(a) excludes. If U were in C{m}(N), then so would be
Omega = -curl U, by (2). If Theta were in C{m}(G), (3) would give Theta = L on G, which contradicts
Theta = a0 x^2 + O(|X|^3), a0 != 0, near the point 0 of G. (c) Theta - L and Omega vanish to infinite order at every
point of C^. At p and on C this is (xiii)(a). Every other point of C^ is phi_t Y with Y on C and t real; by (T),
Theta - L = (Theta - L) o phi_{-t} near phi_t Y, and phi_{-t} is a smooth diffeomorphism, so all derivatives of
Theta - L vanish at phi_t Y; by (V), Omega(phi_t Y') = e^{-t} Omega(Y') + int_0^t e^{-(t - s)} Theta_x(phi_s Y') ds
for Y' near Y (an oriented integral if t < 0), and all derivatives of both terms with respect to Y' vanish at Y' = Y,
since Omega vanishes to infinite order at Y, Theta_x vanishes to infinite order at every point phi_s Y of the orbit
segment (by the first step) and the maps phi_s are smooth. So Omega o phi_t, and hence Omega, vanishes to infinite
order at phi_t Y. No regularity of the flow beyond smoothness is used. If Theta or Omega were in C{m}(N), (3) would
give Theta = L or Omega = 0 on a disk around the point, which (xv)(a) or (xv)(b) excludes; for U use (2) as in (b).
Proof outline of (d). By the proof of (c), Theta - L and Omega vanish to infinite order at every point of A, so all
their t-derivatives vanish at (s, g(s)) for s in I; by (xv)(a) and (b) neither vanishes identically on a neighbourhood
of a point of A. Fix a nondegenerate compact subinterval K of I and an integer n_0 >= 1 such that the closed strip
{(s, t) : s in K, |t - g(s)| <= 1/n_0} lies in the coordinate patch, and let n >= n_0. (Scalar part.) For
f = Theta - L or f = Omega let E_n be the set of s in K with f(s, g(s) + u) = 0 for all |u| <= 1/n. E_n is closed by
the continuity of f and g. If E_n contained an interval of positive length, with interior J, f would vanish on the
open set {(s, t) : s in J, |t - g(s)| < 1/n}, a neighbourhood of points of A, which is excluded; so E_n has empty
interior. The union of the sets E_n is the set of s in K at which t -> f(s, t) vanishes on an open interval containing
g(s). For s outside this union, if t -> f(s, t) were in C{m} on an open interval J containing g(s), the one-variable
form of fact (3) (applied on the compact subintervals of J containing g(s)) would give f(s, .) = 0 on J. (Velocity
part.) Write U_s and U_t for the components of U along d/ds and d/dt, and let H_n be the set of s in K with
|d_t^k U_s(s, g(s) + u)| <= n^{k+1} m_k and |d_t^k U_t(s, g(s) + u)| <= n^{k+1} m_k for all k >= 0 and all |u| <= 1/n.
H_n is closed, since each of these conditions is closed in s. If s is in K and t -> U(s, t) is in C{m} on an open
interval containing g(s), with constants A, B (for both components) on a compact interval [g(s) - r, g(s) + r] in it,
then s lies in H_n for every n >= max(n_0, A, B, 1/r). Suppose that H_n contains an interval of positive length, with
interior J. On J x (-1/n, 1/n) put P(s, u) = U_s(s, g(s) + u), Q(s, u) = U_t(s, g(s) + u) and
O(s, u) = Omega(s, g(s) + u). Since Omega = -curl U = d_t U_s - d_s U_t and
d_s Q = (d_s U_t)(s, g(s) + u) + g'(s) d_u Q, we have O = -d_s Q + d_u P + g'(s) d_u Q. For phi smooth with compact
support in J, integration by parts in s gives F(u) = int O(s, u) phi(s) ds = int Q(s, u) phi'(s) ds +
d_u int (P(s, u) + g'(s) Q(s, u)) phi(s) ds. The bounds of H_n and m_{k+1} <= max(1, m_1) D^k m_k, D = max(1, D_m),
give |F^(k)(u)| <= c (n D)^k m_k for |u| < 1/n and every k >= 0, with
c = n ||phi'||_1 + n^2 max(1, m_1) (1 + sup |g'|) ||phi||_1 (the sup over the support of phi). Every u-derivative of O
vanishes at u = 0, so F vanishes to infinite order at u = 0, and by the one-variable form of (3) F = 0 on (-1/n, 1/n).
Since phi is arbitrary and O is continuous, O = 0 on J x (-1/n, 1/n), that is, Omega = 0 on the open set
{(s, t) : s in J, |t - g(s)| < 1/n}, which (xv)(b) excludes. So H_n is closed with empty interior. The sets E_n (for
both functions) and H_n, n >= n_0, are countably many closed subsets of K with empty interior, and a countable union
of such sets has dense complement in K (choose nested closed intervals avoiding them one by one). Closedness and
interior here are relative to K; sets closed in K with empty interior in K are closed in I with empty interior in I.
Choosing countably many nondegenerate compact subintervals K of I whose interiors cover I gives M_0 and M_m; M_0 does
not depend on m.
Scope of (xvii). For m_k = k!, (a) is the statement of (ii) that Theta is not real analytic on R^2, and (b) and (c)
contain (xii)(a) and the corresponding statements of (xv)(a), (b). Some admissible sequences give classes strictly
larger than the real analytic class. For example m_k = k! (log(k + e))^k = k! exp(H(k)) with H(t) = t log log(t + e)
satisfies the four conditions: H''(t) = ((t + 2e) log(t + e) - t)/((t + e)^2 (log(t + e))^2) > 0 for t >= 0, so m is
log-convex; k log(k + e) <= m_k/m_{k-1} <= e k log(k + e), so D_m < infinity and sum_k m_{k-1}/m_k diverges like
sum_k 1/(k log k). The function f(x, y) = sum_{n >= 2} exp(-n/log n) cos(n x) is in C{m}(R^2): with
S = sum_{n >= 2} n^{-2}, D = D_m and C = max(m_2, D), the inequality x^j exp(-x/log x) <= 8^j j! (log(j + e))^j for
x > 1 and integers j >= 1 (with t = log x and L = log(j + e): if t <= 8L, then exp(x/log x) >= (x/t)^j/j! gives the
bound j! t^j; if t > 8L, then, since exp(t)/t^2 is increasing for t > 2, exp(t)/t^2 >
exp(8L)/(8L)^2 >= (j + e)^6/64 > j, so the left side is exp(j t - exp(t)/t) < 1), applied with j = k + 2, gives
sum_{n >= 2} n^k exp(-n/log n) <= S 8^{k+2} m_{k+2} <= 64 S C (8 D^2)^k m_k for every k >= 0, so all the
differentiated series converge uniformly and |d^alpha f| <= 64 S C (8 D^2)^{|alpha|} m_{|alpha|}. It is not real
analytic, since a real analytic 2 pi-periodic function of x has Fourier coefficients O(e^{-c n}) for some c > 0, while
exp(-n/log n) decays more slowly than every exponential. A class that contains a smooth function vanishing to infinite
order at a point of an interval without vanishing on the interval is not covered by (xvii); for example, for s > 1 the
Gevrey class of order s contains the function equal to exp(-t^{-1/(s-1)}) for t > 0 and to 0 for t <= 0. The
nontrivial smooth flat corrections of the configuration of the 6.3 bullet beta = 2 built from exp(-z^{-1/2}) vanish to
infinite order at their endpoint without vanishing near it, so by (3) they belong to no class C{m} on a neighbourhood
of that endpoint. In the setting of (iii), profiles for which Omega or U belongs to a class C{m} as above on a
neighbourhood of even one endpoint of gamma are excluded. This criterion alone gives no exclusion under an assumption
of mere smoothness or of Gevrey regularity of order s > 1 near the endpoints. At outgoing endpoints, at incoming
endpoints when the zeros of W off gamma are isolated, and at accumulating endpoints when some neighbourhood of the
endpoint contains no arc of zeros of W off gamma, Gevrey regularity of U or of Omega of order s <= 2 on a
neighbourhood of the endpoint is excluded by (xix)(b), (c), (e) and (xx)(d). It proves neither the existence of such
profiles nor any Gevrey regularity of the configurations of 6.3.
Scope of (d). (d) concerns one family of parallel lines, transverse to A, at a time; no statement is made
simultaneously for all directions. The exceptional sets cannot be removed by this argument: the function
f(s, t) = s^2 h(t), with h(t) = exp(-1/t^2) for t < 0 and h(t) = 0 for t >= 0, vanishes to infinite order on the line
t = 0 and identically on no neighbourhood of any of its points, and t -> f(0, t) is identically zero. This example
concerns the assumptions used in the argument; it does not exhibit exceptional lines in a profile. For m_k = k!, (d)
says that on a dense set of such lines the restrictions of Theta, Omega and U are not real analytic on any interval
around their intersection with A (outside the meager set M_0 united with M_m); unlike (xii)(c), it concerns lines
transverse to A, while the lines of (xii)(c) are parallel to the tangent of C at p. For each fixed sequence m as
above, profiles for which, near some point of C^, the restriction of U to the lines of one transverse direction is in
C{m} on an open interval around its intersection with A for every line of a nonmeager set of these lines (for example
for every line meeting a subarc of A) are excluded. Like (b) and (c), (d) gives no exclusion under mere smoothness or
Gevrey regularity of order greater than 1.
(xviii) Exact local reduction at an outgoing endpoint (beta = 2). In the setting of (iii), let p be an outgoing
endpoint (case (b) of (iv)), L = Theta(p), and C the strong unstable curve of p ((xiii)). Parametrize gamma near p by
arclength, a -> gamma(a) for -delta_0 <= a <= 0 with gamma(0) = p, and put tau = gamma', n = (-tau_y, tau_x),
theta(a) = Theta(gamma(a)) and lambda(a) = Omega(gamma(a)); points of the plane are written X = (x, y) in the original
Cartesian coordinates. Only the equations div W = 4, Omega = -curl W, (T) and (V) on a neighbourhood of p and the
facts of (iii) and (iv) at p are used.
(a) There are delta in (0, delta_0) and a smooth map X(a, r) = (x(a, r), y(a, r)) on a neighbourhood of
R = [-delta, 0] x [-delta, delta], injective there, with X(a, 0) = gamma(a), X_r(a, 0) = n(a) + lambda(a) tau(a)/4,
det(X_a, X_r) = 1 and W(X(a, r)) = 4 r X_r(a, r) on R, such that r -> X(0, r) parametrizes C near p and, on R,
Theta(X(a, r)) = theta(a), Omega(X(a, r)) = (theta'(a)/4) int_0^1 u^{-3/4} y_r(a, u r) du, and therefore
(E): 4 d_r(r X_a.X_r) - 4 r d_a |X_r|^2 = (theta'(a)/4) int_0^1 u^{-3/4} y_r(a, u r) du. For every sufficiently small
disk D about p, C n D is an arc that divides D into two components; the closure in D of the component D_- that
contains the points of gamma near p other than p is X(R) n D, and the points of the other component D_+ have backward
limit p. Conversely, if X is a smooth map on a neighbourhood of a rectangle R as above, injective there, with
det(X_a, X_r) = 1, and theta is a smooth function such that (E) holds on R, then the fields defined on X(R) by
W(X(a, r)) = 4 r X_r(a, r), Theta(X(a, r)) = theta(a) and the formula above for Omega satisfy div W = 4,
Omega = -curl W, (T) and (V) on the interior of X(R).
(b) Let D, D_- and D_+ be as in (a), and c(r) = X(0, r). There is a smooth function H on the closure of D_+ in D with
W = grad H and Lap H = 4 there, d_nu H = 0 on C n D for a unit normal nu of C, and grad H(c(r)) = 4 r c'(r); in
particular H(c(r)) = H(p) + int_0^r 4 rho |c'(rho)|^2 d rho. Conversely, let D be a disk, c a smooth embedded arc
through D that divides it into two components D_- and D_+, X and theta as in the converse of (a) with X(0, r) = c(r)
and X(R) n D equal to the closure of D_- in D, theta - L vanishing to infinite order at a = 0, and H a smooth function
on the closure of D_+ in D with Lap H = 4 and grad H(c(r)) = 4 r c'(r) at the points c(r) in D. Then the fields of (a)
on the closure of D_- and W = grad H, Theta = L, Omega = 0 on the closure of D_+ agree to infinite order on c n D and
define smooth fields on D that satisfy div W = 4, Omega = -curl W, (T) and (V).
(c) Near an interior point of gamma use the coordinates Y(a, h) = gamma(a) + h n(a), write W = P tau + Q n, and let
P_j, Q_j, T_j and O_j be the coefficients of h^j in the Taylor expansions in h at h = 0 of P, Q, Theta and Omega
(functions of a). Put d_m = 4m + 1 - tau_y theta'/(4(m + 1)). Where d_m != 0 for every m >= 0 (in particular where
|theta'| < 4), all these coefficients are determined, recursively in m, by gamma and theta. Conversely, for every
smooth arc gamma parametrized by arclength and every smooth function theta on it with |theta'| < 4, the recursion
defines formal power series in h with P_0 = Q_0 = 0 and T_0 = theta that satisfy div W = 4, Omega = -curl W, (T) and
(V) to every order in h.
Proof outline. (a) Extend gamma to a smooth unit-speed curve on -delta_0 <= a <= delta_0, define tau = gamma' and
n = (-tau_y, tau_x) on the extension, extend lambda smoothly, and put M(a) = (4n + lambda tau) (x) n, P_4 = M/4
and P_0 = I - P_4. By (iii), M(a) = DW(gamma(a)) for a <= 0 (lambda(0) = 0 and DW(p) = 4 n (x) n); M^2 = 4M
because n.(4n + lambda tau) = 4, so exp(tM) = P_0 + e^{4t} P_4, and b = n + lambda tau/4 satisfies M b = 4 b and
det(tau, b) = 1; shrinking delta_0, |b| <= 3/2. The projections P_0 and P_4 need not be orthogonal. Let N(a, h) =
W(gamma(a) + h) - W(gamma(a)) - DW(gamma(a)) h; N and all its derivatives in a are O(|h|^2) uniformly, and N(a, h)
= W(gamma(a) + h) - M(a) h for a <= 0. For small |r| the map sending h to the function t -> r e^{4t} b(a) +
int_{-infinity}^t [P_0 + e^{4(t - v)} P_4] N(a, h(v)) dv, t <= 0, is a contraction of the ball of radius 2|r| in
the norm sup_{t <= 0} e^{-4t} |h(t)|, uniformly in a (the two kernels applied to e^{8v} give e^{8t}/8 and
e^{8t}/4), and its fixed point h(a, r, t) depends smoothly on (a, r) (on a fixed small ball of the space with the
norm sup_{t <= 0} e^{-4t} |h(t)|, the map h -> N(a, h) is smooth into the space with the norm sup_{t <= 0} e^{-8t}
|h(t)|, with all its derivatives in a, the kernels map that space boundedly back, and the derivative in h of the
operator has norm less than one, so the implicit function theorem gives smooth dependence of every order on (a,
r), including r = 0); the extension to a > 0 is auxiliary, and the identities below are asserted only for a <= 0.
Put X(a, r) = gamma(a) + h(a, r, 0). For a <= 0, t -> gamma(a) + h(a, r, t) solves X' = W(X) on t <= 0 and tends
to gamma(a), and uniqueness of the fixed point gives h(a, r, t + t') = h(a, e^{4t'} r, t) for t' <= 0; hence phi_t
X(a, r) = X(a, e^{4t} r) for t <= 0 and W(X(a, r)) = 4 r X_r(a, r). Moreover X(a, 0) = gamma(a), X_r(a, 0) = b(a),
and DX(0, 0) has the columns tau(0), n(0), so for small delta X is a diffeomorphism of a neighbourhood of R onto a
neighbourhood of p. In coordinates with area density J = det(X_a, X_r) the field 4 r d_r has divergence J^{-1}
d_r(4 r J) = 4 + 4 r J_r/J, so div W = 4 gives J_r = 0 for r != 0, hence on R by continuity, and J = J(a, 0) =
det(tau, b) = 1. The curve r -> X(0, r) is invariant, passes through p tangent to n(0) (lambda(0) = 0), and
phi_{-T} X(0, r) = X(0, e^{-4T} r) converges to p at the rate e^{-4T}, so it is C near p. Theta is constant on
orbits and continuous, so Theta(X(a, r)) = theta(a). Since J = 1, the inverse map satisfies a_x = y_r, so
Theta_x(X(a, r)) = theta'(a) y_r(a, r), and (V) along t -> X(a, e^{4t} r) reads 4 r d_r omega + omega = theta' y_r
for omega = Omega o X. On r > 0 and on r < 0 its solutions differ from the stated integral by multiples of
|r|^{-1/4}, and Omega is bounded, which gives the formula (multiply by e^t along r e^{4t}, integrate over t <= 0
and put u = e^{4t}). The pull-back of W_1 dx + W_2 dy by X is 4 r (X_a.X_r) da + 4 r |X_r|^2 dr, its exterior
derivative is (4 r d_a |X_r|^2 - 4 d_r(r X_a.X_r)) da ^ dr, and dx ^ dy = J da ^ dr = da ^ dr; so curl W o X is
this coefficient, and Omega = -curl W gives (E). For the disks, take the coordinates (u, v) and the rectangles Q
and Q' of the proof of (xii)(b), in which C = {u = 0}, points with u > 0 have backward limit p, and points with
u < 0 have as backward limit a point of gamma near p. Choose eta > 0 so that X is injective on a neighbourhood of
R u V, V = (-delta, eta) x (-delta/2, delta/2), and let A be the first component of the inverse of X on X(V). For
every sufficiently small disk D about p with closure in X(V) n Q', C n D = {A = 0} n D is a regular arc through
the center of D that divides D into the two components {A < 0} n D and {A > 0} n D, and X(R) n D = {A <= 0} n D by
injectivity. The component {A < 0} n D contains the points of gamma near p other than p, and so does {u < 0} n D;
both are components of D minus the same arc, so they agree, X(R) n D = D n {u <= 0}, and D_+ = D n {u > 0}.
Conversely, given X and theta, the fields defined by the formulas satisfy div W = J^{-1} d_r(4 r J) = 4, W.grad
Theta = 4 r d_r theta(a) = 0, W.grad Omega + Omega = 4 r omega_r + omega = theta' y_r = Theta_x (by the
computation above, since J = 1), and Omega = -curl W by (E). (b) By the proof of (xv) (outgoing case), Theta = L
and Omega = 0 on Q' n {u > 0}, so div W = 4 and curl W = 0 on the simply connected set D_+, which is bounded in D
by the arc C n D; hence W = grad H with Lap H = div W = 4 and H unique up to an additive constant, and H is smooth
up to C n D (integrate the closed form W_1 dx + W_2 dy locally in coordinates in which C is a straight segment). C
is invariant, so W is tangent to C and d_nu H = W.nu = 0, and grad H(c(r)) = W(c(r)) = 4 r c'(r) by (a).
Conversely, Theta - L = theta(a) - L and Omega o X = theta'(a) (1/4) int_0^1 u^{-3/4} y_r(a, u r) du vanish to
infinite order on a = 0, since theta - L and theta' do, so they agree to infinite order on c with L and 0. W is
continuous across c, since grad H(c(r)) = 4 r c'(r) = W(X(0, r)). In coordinates along c, div W = 4 and curl W =
-Omega express the normal derivative of W at points of c through the tangential derivative of W, the curvature of
c and the values of div W and curl W; differentiating, every normal derivative of W on c is determined by the
tangential derivatives of W on c and the derivatives of lower order of div W and curl W there. These data agree
from the two sides (div W = 4 on both, and every derivative of curl W = -Omega vanishes on c from both sides), so
all one-sided derivatives of W agree on c, and the glued fields are smooth; the equations hold on D_- and D_+ and,
by continuity, on c. (c) With J = 1 - kappa h (tau' = kappa n), div W = P_a/J + Q_h - kappa Q/J, Omega = P_h -
(Q_a + kappa P)/J, W.grad = (P/J) d_a + Q d_h and Theta_x = (tau_x/J) Theta_a + n_x Theta_h. Here P_0 = Q_0 = 0,
T_0 = theta, and the coefficient of h^0 in div W = 4 gives Q_1 = 4. Suppose P_j, Q_j, T_j for j <= m and O_j for j
< m are known. The coefficient of h^m in div W = 4 gives Q_{m+1}. The coefficient of h^m in the curl relation
gives P_{m+1} = O_m/(m + 1) + (known terms), the coefficient of h^{m+1} in (T) gives 4(m + 1) T_{m+1} = -theta'
P_{m+1} + (known terms), and the coefficient of h^m in (V) is (4m + 1) O_m - n_x (m + 1) T_{m+1} = (known terms).
Substituting, d_m O_m = (known terms), since n_x = -tau_y. Every coefficient of every equation is used exactly
once in this recursion (the coefficient of h^0 in (T) holds because P_0 = Q_0 = 0), so it determines the
coefficients when every d_m is nonzero, and for |theta'| < 4, where d_m > 4m + 1 - 1/(m + 1) >= 0, it defines
formal series satisfying all equations to every order.
Scope of (xviii). Since only local facts are used, (a) and (b) hold for every smooth solution of div W = 4,
Omega = -curl W, (T) and (V) on a disk about p whose zero set there is an arc ending at p of the outgoing type of (iv)
(the facts of (iii) used at p follow from the equations near p, as in the proof of (iii)). After shrinking the
neighbourhoods, such local solutions are therefore equivalent to the data of (a) and (b): the curve c, the map X with
det(X_a, X_r) = 1 satisfying (E) and covering the closure of D_- in D, the trace theta with theta - L flat at a = 0,
and the solution H (unique up to an additive constant) of the one-sided Cauchy problem Lap H = 4, grad H(c(r)) =
4 r c'(r) on the closure of D_+, with the additional requirement that the glued field W have zero set exactly gamma
near p and be of the outgoing type of (iv) in the following chart sense: there are C^4 coordinates (u, v) about p as
in step (3) of the proof of (v)-(vii), with C = {u = 0}, gamma = {v = 0, u <= 0}, g > 0 for u > 0 and d > 2, oriented
so that the side {u > 0} of C is exactly the side D_+ on which H is given; every backward orbit that starts in D_+
close enough to p then stays in this fixed chart and tends to p (step (3)). Neither this requirement nor the zero set
is implied by (E) and the trace condition on grad H. This requirement cannot be dropped: X(a, r) = (a, r), theta = L
and H = 2y^2 on {x > 0} satisfy all the other conditions with c(r) = (0, r), and the glued field W = (0, 4y) vanishes
on a whole line. Once the sign requirement holds, theta is not constant on any subarc ending at a = 0 ((xii)(b)) and
the image of c is not a regular real analytic embedded curve germ at p, that is, no real analytic embedded arc through
p with nonzero tangent agrees with C near p ((vi)), both by local arguments. Neither such data nor a general
obstruction to them is established; the research consultations on this local problem described in 6.3 found neither,
and obtained, among other conclusions, the restricted exclusions of (xii)(c), (d) and (xix)(b), (c). A local
obstruction would exclude every smooth profile at beta = 2 with an outgoing endpoint (by (v), in particular the
subclass Z = gamma); a local solution would rule out every contradiction derived from these outgoing-endpoint
hypotheses alone, and would not establish compatibility with the center, the other endpoint, the canonical inverse or
the far field. The proofs of (xii)(a) and (b), and of (xv)(a) and (b) at outgoing endpoints, also use only the
equations near p (for (xv), near the orbit segments involved), and in the coordinates of (a) the proof of (xii)(b)
reads: theta = L on [-eps, 0] gives Omega = 0 on X([-eps, 0] x [-delta, delta]), which, for a disk D small enough that
X([-eps, 0] x [-delta, delta]) covers the closure of D_- in D, together with Omega = 0 on D_+ gives a neighbourhood of
p on which U is harmonic, excluded by (xii)(a). By (c), the expansion in the normal distance along the interior of
gamma imposes no condition on gamma and theta where |theta'| < 4; (c) concerns formal series only: their convergence
is not claimed, a smooth field with these jets (by Borel's lemma) satisfies the equations only up to errors that
vanish to infinite order on gamma, and (c) says nothing at the endpoint. No profile is excluded.
(xix) Continuation and Gevrey bounds at an outgoing endpoint, and at an incoming endpoint with isolated zeros off the
arc; support of the vorticity (beta = 2). In the setting of (iii), let p be an outgoing endpoint (case (b) of (iv)),
(s, z) the coordinates of (iv) at p with the z axis along n, w = s + i z, W_s and W_z the components of W in these
coordinates, k and f as in (iv), C = {s = sigma(z)} the strong unstable curve of (xiii) near p, and O = {s > sigma(z)}
near p the side of C beyond p, on which Theta = L, Omega = 0 and W = grad H with Lap H = 4 (the side D_+ of
(xviii)(a), (b)). For a unit vector e write d_e = e.grad, and let B_eps be the open disk of radius eps about p.
(a) There is no real analytic vector field V on a neighbourhood of p that equals W on a measurable subset N of O such
that N n B has positive area for every disk B about p; in particular there is none that equals W on an open subset of
O whose closure contains p.
(b) There are no eps > 0, c_0 > 0, A > 0 and unit vector e such that |d_e^n W| <= c_0 A^n (n!)^2 on O n B_eps for
every n >= 0. In particular, for no s in [1, 2] is U in the Gevrey class of order s (bounds c_0 A^n (n!)^s for all
derivatives of order n, uniformly on compact sets) on a neighbourhood of p, and for no s in [1, 2] does the
restriction of W to O n B_eps satisfy such bounds uniformly up to p.
(c) For every unit vector e, every disk B about p in the domain of the fields and every A > 0,
sup_{n >= 0} sup_B |d_e^n Omega|/(A^n (n!)^2) = infinity. In particular, for no s in [1, 2] and no unit vector e does
Omega satisfy bounds |d_e^n Omega| <= c_0 A^n (n!)^s on a neighbourhood of p, although every derivative of Omega
vanishes at p itself ((iii)).
(d) Suppose that the tangent of gamma at p is not vertical, tau_x(p) != 0, and let X(a, r),
R = [-delta, 0] x [-delta, delta] and theta be as in (xviii)(a). After decreasing delta, the set
J = {a in (-delta, 0): theta'(a) != 0} is open and has 0 in its closure, and, for (a, r) in
(-delta, 0) x [-delta, delta], Omega(X(a, r)) != 0 exactly when a is in J. The set of directions in which nonzero
vorticity accumulates at p, that is, of the limits v of (Y_j - p)/|Y_j - p| over sequences Y_j -> p with Y_j != p and
Omega(Y_j) != 0, is the closed half circle {v_s <= 0} of unit vectors in the coordinates (s, z).
(e) Let p be an incoming endpoint (case (c) of (iv)) and suppose that every zero of W off gamma is isolated. Then (a),
(b) and (c) hold at p, with O replaced by the side O' = {s > sigma(z)} of C beyond p near p, on which Theta = L,
Omega = 0 and U is harmonic ((xiv)(b)).
Proof outline. (a) Take a square Q = {|s| < eps, |z| < eps} in the domains of V and W with |sigma(z)| < eps/2 for
|z| < eps. Then O n Q = {(s, z) in Q: s > sigma(z)} is connected (each of its points is joined horizontally to the
segment {s = 3 eps/4, |z| < eps}, which lies in it), and W is real analytic on it, since
Delta W_s = d_s div W - d_z curl W = 0 and Delta W_z = d_z div W + d_s curl W = 0 there. A real analytic function on a
connected open set that vanishes on a set of positive area vanishes identically (by Fubini, on a set of lines
s = const of positive measure in a rectangle its zero set has positive length, so it vanishes on these lines and then
on the rectangle); since V - W vanishes on N n Q, which has positive area, V = W on O n Q. Since p is in the closure
of O n Q and W is smooth, V and W have the same derivatives of every order at p. As in the proof of (xii)(c), the zero
set of V_z near p is an analytic graph z = k^an(s), and f^an(s) = V_s(s, k^an(s)) has the Taylor series of f at 0,
which is zero since f = 0 for s <= 0; so f^an = 0 near 0. Since k^an(s) = O(s^2) and sigma(z) = O(z^2),
sigma(k^an(s)) = O(s^4) < s for small s > 0, so (s, k^an(s)) lies in O n Q, where W_z = V_z = 0; hence k^an(s) = k(s)
(d_z W_z(p) = 4) and f(s) = f^an(s) = 0 on an interval (0, delta'), contrary to case (b). The last steps of the proofs
of (xii)(c) and (d) are this argument for the real analytic fields W^an constructed there. (b) Put
d_wbar = (d_s + i d_z)/2 and K = W_s - i W_z + 4 i z. Then
d_wbar K = (div W - 4)/2 + (i/2)(d_z W_s - d_s W_z) = i Omega/2, so K is holomorphic in w on O, and K(p) = 0 and
DK(p) = 0, since W(p) = 0 and DW(p) = 4 n (x) n. Put S = w - K/2, S*(w) = conj S(conj w) and R = conj S. Then
W_s + i W_z = 2 (w - R(w)), S(w) = w + O(|w|^2), S is holomorphic on O and S* on O* = {conj w : w in O}, and every
derivative of d_wbar S = -i Omega/4 vanishes at p ((iii)). Let E(w) = S*(S(w)) - w = R(R(w)) - w, a smooth function
near p. (1) Choose m_1 and m_2 with |S(w) - w| <= m_1 |w|^2 and |sigma(z)| <= m_2 z^2 near p, and M > m_1 + 4 m_2
large. The open disk D_M = {Re w > M |w|^2}, of diameter 1/M and tangent to the z axis at p, lies in O, and for w in
D_M, Re S(w) > (M - m_1) |w|^2 > 4 m_2 |w|^2 >= sigma(-Im S(w)) (since |S(w)| <= 2 |w|), so S(w) lies in O*; hence E
is holomorphic on D_M. (2) The Taylor series of S at p contains only powers of w, and so do those of S* and E. On
gamma near p, W = 0, so R(w) = w and E = 0 there. Restricting the Taylor series of E to w = s + i k(s), s < 0, a first
nonzero term d_m w^m would give d_m s^m + o(|s|^m) = 0; so every derivative of E vanishes at p. (3) Let
kappa(s) = s + i k(s). For small s > 0, R(kappa(s)) = kappa(s) - f(s)/2, the horizontal segment from kappa(s) - f(s)/2
to kappa(s) lies in O (f(s) = o(s), k(s) = O(s^2)), and d_s R = conj S' on it, so
E(kappa(s)) = -(f(s)/2) [1 + int_0^1 conj S'(kappa(s) - t f(s)/2) dt] = -f(s) (1 + O(s)), which is nonzero. (4) If the
bound of (b) holds in the direction e = (e_s, e_z), then d_e^n K = (e_s + i e_z)^n K^(n) on O, where K^(n) is the
complex derivative, so |K^(n)| <= c_1 A^n (n!)^2 on O n B_eps for n >= 2 and, after increasing c_1, for all n; bounds
of the same form hold for S on O n B_eps and for S* on O* n B_eps. For holomorphic b and h with
|b^(k)| <= C_b A_b^k (k!)^2 and |h^(j)| <= C_h A_h^j (j!)^2, the Taylor coefficient form of the chain rule
(Faa di Bruno) and the inequality k! j_1! ... j_k! <= n! for j_1 + ... + j_k = n, j_i >= 1, give
|(b o h)^(n)| <= C_b A_h^n (n!)^2 x (1 + x)^(n - 1) with x = A_b C_h, for n >= 1. Taking M so large that D_M and
S(D_M) lie in B_eps, E satisfies |E^(n)| <= c_2 A_2^n (n!)^2 on D_M for every n; only the bounds for S at the points
of D_M and of R(D_M), which lie in O n B_eps, enter, since (S*)^(j)(S(w)) = conj S^(j)(R(w)). (5) A holomorphic
function G on D_M, smooth up to p with every derivative zero at p, that satisfies these bounds is zero. Taylor's
formula along the segment from p to w, which lies in D_M except for p, gives |G(w)| <= c_2 A_2^n n! |w|^n for every n,
and the choice n = floor(1/(2 A_2 |w|)) gives |G(w)| <= c_3 exp(-c/|w|) on D_M, with c > 0. The map zeta = 1/w takes
D_M onto the half plane Re zeta > M, and P(zeta) = G(1/zeta) satisfies |P(zeta)| <= c_3 exp(-c |zeta|) there. If
P(x_0) != 0 for some real x_0 > M, put d = x_0 - M and g(u) = P(M + d (1 + u)/(1 - u)) for |u| < 1; the submean
inequality for log |g| gives, for 0 < r < 1,
log |g(0)| <= log c_3 - (c/(2 pi)) int_{-pi}^{pi} |M + d (1 + r e^{it})/(1 - r e^{it})| dt, and the integral tends to
infinity as r -> 1 (for 1 - r <= t <= 1/4 the integrand is at least d/(2 t) - M), a contradiction. So P = 0 on
(M, infinity), hence P = 0. Applied to G = E, this contradicts (3), since kappa(s) lies in D_M for small s > 0
(M |kappa(s)|^2 = O(s^2) < s). (c) Suppose that |d_e^n Omega| <= c_0 A^n (n!)^2 on a disk B about p. Choose a smooth
cutoff chi with compact support in B, equal to 1 near p, with |d_e^n chi| <= c_4 A_4^n (n!)^2: a product of a function
of e.X and a function of the orthogonal coordinate, the second smooth with compact support and equal to 1 near 0, the
first the convolution of the indicator of an interval with a rescaled multiple of the function beta_0 equal to
exp(-1/(1 - t^2)) on (-1, 1) and to 0 elsewhere. With d = 1 - |t|, the holomorphic extension of beta_0 is bounded by
exp(-c_6/d) on the disk of radius c_5 d about t, for small c_5 > 0, so the Cauchy estimates give
|beta_0^(n)(t)| <= n! (c_5 d)^(-n) exp(-c_6/d) <= c_7^n (n!)^2. By the Leibniz rule, q = i chi Omega/2 satisfies
|d_e^n q| <= c_8 A_8^n (n!)^2. Let F = T q with T q(w) = (1/pi) int q(zeta)/(w - zeta) dA(zeta). Then d_wbar F = q, so
K - F is holomorphic near p; d_e^n F = T[d_e^n q]; and |T g| <= c_9 sup |g| on a fixed disk about p for every bounded
g supported in the support of chi. With the Cauchy estimates for K - F on a smaller disk, K, and hence
W = (Re K, 4 z - Im K), satisfies the bound of (b) in the direction e on O n B_eps for small eps, which (b) excludes.
(d) By (xviii)(a), Omega(X(a, r)) = theta'(a) mu(a, r) on R, with mu(a, r) = (1/4) int_0^1 u^{-3/4} y_r(a, u r) du,
and mu(0, 0) = y_r(0, 0) = n_y(p) = tau_x(p), since X_r(0, 0) = n(p) (lambda(0) = Omega(p) = 0). After decreasing
delta, mu != 0 on R, so Omega(X(a, r)) != 0 exactly when theta'(a) != 0. If 0 were not in the closure of J, theta
would be constant on [-delta', 0] for some delta' > 0, which (xii)(b) excludes. In the coordinates (s, z),
X(0, 0) = p, X_a(0, 0) = tau(p) = (1, 0) and X_r(0, 0) = (0, 1). For a unit vector v with v_s < 0 choose a_j in J with
a_j -> 0, and put t_j = a_j/v_s > 0 and r_j = t_j v_z; then X(a_j, r_j) - p = t_j v + O(t_j^2) and
Omega(X(a_j, r_j)) != 0. For v = (0, 1) and v = (0, -1) take r_j = |a_j|^{1/2} and r_j = -|a_j|^{1/2}. Conversely,
Omega = 0 on the closure of O near p, so Omega(Y) != 0 implies s(Y) < sigma(z(Y)) = O(z(Y)^2), and every limit
direction has v_s <= 0. (e) Of O and of the type of p, the proofs of (a) to (c) use only that Omega = 0 on O near p,
that C is a graph s = sigma(z) with sigma(0) = sigma'(0) = 0 ((xiii)), and that f(s) != 0 for small s > 0. At an
incoming endpoint with isolated zeros off gamma these hold with O' in place of O, by (xiv)(b) and case (c) of (iv),
where f < 0 on an interval (0, eps). In step (3) of (b) the horizontal segment from kappa(s) to kappa(s) - f(s)/2 =
kappa(s) + |f(s)|/2 then lies in {Re w >= s}, hence in O' for small s > 0, and E(kappa(s)) = -f(s) (1 + O(s)) != 0 as
before; in (a) the contradiction is with f < 0 on (0, eps).
Scope of (xix). Only the equations near p are used, as in the Scope of (xviii), so (a) to (d) hold for the local
solutions described there. (a) is a necessary condition; at outgoing endpoints it is stronger than the statement of
(xii)(a) that U is not real analytic on a neighbourhood of p, since it also excludes real analytic fields that agree
with W only on a measurable subset of O of positive area in every neighbourhood of p and differ from it on the other
side of C. (b) and (c) are restricted exclusions: profiles with an outgoing endpoint at which W satisfies the bound of
(b) on O in one direction, or Omega the bound excluded in (c) on a neighbourhood of the endpoint, are excluded, in
particular profiles for which U or Omega is in a Gevrey class of order at most 2 on a neighbourhood of an outgoing
endpoint; by (v), when Z = gamma it suffices that this hold near one of the two endpoints. For s > 1 the Gevrey class
of order s is not quasianalytic (Scope of (xvii)), so this exclusion is not contained in (xvii). The bound of (b) is
weaker than real analytic continuation of W from O across C: the function
b(w) = int_0^infinity e^{-t} (1 + t w)^{-1} dt is holomorphic on Re w > 0 and smooth up to Re w >= 0,
with |b^(n)| <= (n!)^2 there, and its Taylor series at 0, with coefficients (-1)^n n!, diverges; so a holomorphic
function on a disk tangent to C at p can satisfy the bound of (b) without extending analytically through p, and (b) is
not a direct consequence of (a). The proof of (b) uses the bound only on a disk {s > L (s^2 + z^2)} contained in O
(take M > m_1 + 4 L; then D_M and R(D_M) lie in it), so the bound on one such disk, tangent to C at p, already
suffices. No exclusion is obtained under mere smoothness, under Gevrey regularity of order greater than 2, or under
bounds that hold only on a sector {|z| < m s} with vertex p or on individual lines. (c) concerns bounds on a whole
neighbourhood of p, uniform in the point. (d) is a necessary condition on the shape of {Omega != 0}: near p the
nonzero vorticity occupies whole fibres a = const of the chart of (xviii)(a), with a in J, and meets every open sector
with vertex p that contains a direction v with v_s <= 0, arbitrarily close to p; it is not asserted that such a sector
lies in {Omega != 0} near p, and no statement of this kind is made when the tangent of gamma at p is vertical.
By (e), (a) to (c) also hold at incoming endpoints when the zeros of W off gamma are isolated; (d) is not
extended, since the chart of (xviii)(a) is constructed at outgoing endpoints. By (xx)(d), (a) to (c) also hold
at accumulating endpoints when some neighbourhood of the endpoint contains no arc of zeros of W off gamma.
Incoming endpoints with nonisolated zeros off gamma, and accumulating endpoints every neighbourhood of which
contains an arc of zeros of W off gamma, are not covered, so (a) to (c) exclude no profile whose endpoints are
of these kinds. No local solution or profile is constructed.
(xx) Accumulating endpoints (beta = 2). In the setting of (iii), let p be an accumulating endpoint (case (a) of (iv)),
L = Theta(p), (s, z), k and f as in (iv), C = {s = sigma(z)} the strong unstable curve of p of (xiii), and
O' = {s > sigma(z)} near p the side of C beyond p. In (b) to (d) suppose in addition that for some eps > 0 the set
F = {s in (0, eps): f(s) = 0} has empty interior; equivalently, some neighbourhood of p contains no arc of zeros of W
off gamma.
(a) Theta - L does not vanish identically on any neighbourhood of p.
(b) There is a disk N about p such that Theta = L and Omega = 0 on N n (C u O'), and U is harmonic on N n O'. After
decreasing eps, every point of F is an isolated zero of f, so the zeros of W off gamma near p are isolated and
accumulate only at p.
(c) Theta is not constant on any nondegenerate subarc of gamma that has p as an endpoint, and the conclusions of
(xiv)(d) and (e) hold at p.
(d) The statements (a), (b) and (c) of (xix) hold at p, with O replaced by O'.
Proof outline. Near p the zeros of W are the points (s, k(s)) with f(s) = 0 ((iv)), so an arc of zeros off gamma near
p is the graph of k over an interval contained in F, which gives the equivalence. Take the coordinates (u, v) of step
(3) of the proof of (v)-(vii) at p on a square Q = {|u| <= rho, |v| <= rho}: u' = g(u) + u v c(u, v), v' = v d(u, v),
d > 2, c bounded, C = {u = 0}, gamma = {v = 0, u <= 0} and O' = {u > 0} near p, and g = 0 for u <= 0 (this part of
step (3) does not use the sign of g for u > 0). Since v' = v d, the zeros of W in Q are the points (u, 0) with
g(u) = 0, and those off gamma are the points (u, 0) with u in G = {u in (0, rho): g(u) = 0}. So 0 is in the closure of
G, and under the hypothesis of (b) to (d) G contains no interval near 0, since {v = 0} is a C^1 curve and an interval
in G would give an arc of zeros off gamma. Since g is C^1 and vanishes for u <= 0, g'(u) -> 0 as u -> 0. (1) A
backward invariant region. Let q_1 = (u_1, 0) with u_1 in G small. In the coordinates, the linearization of the field
at q_1 is conjugate to DW(q_1), so it has trace 4; it has the eigenvector (1, 0) with the eigenvalue
lambda_1 = g'(u_1), |lambda_1| < 1, and hence the eigenvalue 4 - lambda_1, with an eigenvector whose v component is
nonzero. The construction of the proof of (xiii)(a), carried out in the original coordinates at q_1 instead of p, with
the weight e^{-(4 - lambda_1) t}, the leading term r e^{(4 - lambda_1) t} e_1, e_1 an eigenvector of DW(q_1) for
4 - lambda_1, and the kernel e^{lambda_1 (t - v)} P_0 + e^{(4 - lambda_1)(t - v)} P_4, P_0 and P_4 the spectral
projections for lambda_1 and 4 - lambda_1, gives a smooth curve C_1 through q_1 tangent to e_1 that consists of q_1
and two orbits with backward limit q_1; in the coordinates (u, v) its tangent at q_1 has a nonzero v component, so for
some rho_1 > 0 it is in Q a graph u = sigma_1(v), |v| <= rho_1, with sigma_1(0) = u_1. The backward limits on C and on
C_1 are p and q_1, so C_1 does not meet C, and sigma_1 > 0. After decreasing rho_1, the region
R = {(u, v): 0 < u < sigma_1(v), |v| < rho_1} lies in {0 < u < 2 u_1, |v| < rho_1} and contains
{0 < u < m, |v| < rho_1}, m = min sigma_1 > 0. R is invariant under the backward flow: its boundary in the strip
|v| < rho_1 consists of p, q_1 and four orbit arcs of C and C_1, and |v| decreases backward. Choosing u_1 and then
rho_1 small, R lies in any given disk about p, and contains the points with u > 0 of a smaller disk about p. (2) (a).
Suppose Theta = L on a disk D about p, and take R in D. For Y in R the backward orbit stays in R, where Theta_x = 0,
so (V) gives Omega(Y) = e^{-T} Omega(phi_{-T} Y) for T >= 0, and Omega(Y) = 0 since Omega is bounded on Q. The
backward orbits from a smaller disk in {u <= 0} stay in D (as in the proof of (xii)(b): g = 0 for u <= 0, and u = 0 is
invariant), so Omega = 0 there as well. Thus Omega = 0 on a neighbourhood of p, contrary to (xii)(a). (3) (b). Let Y
be in R. Its backward orbit stays in the closure of R, a compact subset of Q, so by step (1) of the proof of (v)-(vii)
its alpha-limit set is a nonempty compact connected set of zeros of W in the closure of R, that is, of points (u, 0)
with u in {0} u G and u <= u_1; since G contains no interval near 0, it is one point q_* = (u_*, 0). On the invariant
line v = 0, (T) gives g(u) d_u Theta(u, 0) = 0, so d_u Theta(u, 0) = 0 on [0, u_1] minus G, which is dense in
[0, u_1], hence on [0, u_1] by continuity, and Theta(u, 0) = Theta(p) = L for 0 <= u <= u_1. Theta is constant on
orbits and continuous, so Theta(Y) = Theta(q_*) = L. Thus Theta = L on the open set R, and Omega = 0 on R as in (2).
Choose the disk N with N n O' in R; by (xiii)(a), Theta = L and Omega = 0 on N n C. On N n O', div U = 0 and
curl U = -Omega = 0, so U is harmonic and W is real analytic there. The points (s, k(s)), 0 < s < eps', lie in N n O'
for small eps' (k(s) = O(s^2), sigma(z) = O(z^2)), so k and f are real analytic on (0, eps') (the zero curve of W_z,
with d_z W_z near 4). f does not vanish identically on (0, eps'): otherwise W would vanish on the arc z = k(s),
0 <= s < eps', connected to gamma through p, contradicting the maximality of the component gamma. So the zeros of f in
(0, eps') are isolated. (4) (c). If Theta = L on a nondegenerate subarc of gamma ending at p, the points near p with
u < 0 have backward limits on that subarc (as in the proof of (xii)(b)), so Theta = L there, and (b) gives Theta = L
on a neighbourhood of p, contrary to (a). The proofs of (xiv)(d) and (e) apply with (b) in place of (xiv)(b): in (d),
for 0 < s < a, a > 0 small, the point (s, 0) lies in the open set N n O', where Omega = 0, so z -> Omega(s, z)
vanishes on an interval about 0 and, by the identity theorem, on (-delta, delta), which gives Omega = 0 on
(0, a) x (-delta, delta) as in that proof; in (e), Omega = 0 on the side of C beyond p in a small disk. (5) (d). The
proofs of (xix)(a) to (c) use, of O and of the type of p, only that Omega = 0 on O near p, that C is a graph
s = sigma(z) with sigma(0) = sigma'(0) = 0, and that f(s) != 0 for some s in every interval (0, delta): in (a) the
contradiction is with f = 0 on an interval (0, delta'), and in step (3) of (b) the points kappa(s) with f(s) != 0,
which lie in D_M for small s, give E(kappa(s)) != 0. These hold with O' in place of O, by (b) and by the maximality of
gamma, as in (3). For such s the horizontal segment from kappa(s) to kappa(s) - f(s)/2 lies in {Re w >= s - |f(s)|/2},
hence in O' for small s, since f(s) = o(s), k(s) = O(s^2) and sigma(z) = O(z^2), and
E(kappa(s)) = -f(s) (1 + O(s)) != 0 as in (xix).
Scope of (xx). Only the equations near p are used. (a) holds at every accumulating endpoint; for profiles, the
vanishing of Theta - L on a neighbourhood of an endpoint is excluded at endpoints of every type by (xxi) (and also by
(vii) with (xii)(a)). The hypothesis of (b) to (d) is not derived from the equations. Under it, (b) gives at an
accumulating endpoint the structure that (iv) gives at an outgoing one and (xiv)(b) at an incoming one; (a) and the
first statement of (c) give the analogue of (xii)(b), the rest of (c) the analogues of (xii)(c), without the condition
on C of (xiii)(c), and of (vi), and (d) the continuation statement and the restricted exclusions of (xix)(a) to (c).
(a), the first statement of (c) and the conclusion of (xiv)(e) are necessary conditions; the conclusion of (xiv)(d)
and (d) are restricted exclusions. Nothing is asserted on the zeros of W off gamma near p beyond their isolation, on
their backward basins, or on a global structure of the kind of
(xiv)(a) and (f). When every neighbourhood of p contains an arc of zeros of W off gamma, (T) does not determine Theta
on these arcs, and (b) to (d) are not established; the first statement of (c) holds if Theta is constant on each such
arc in some neighbourhood of p ((xxii)(d)). Accumulating endpoints are not excluded in general for smooth
profiles, and no local solution or profile is constructed.
(xxi) Open sets on which Theta is constant (beta = 2). In the setting of (iii), let D be a nonempty open set on which
Theta is constant, and let V be the union of the orbits of W through the points of D. Then V is open and invariant,
Theta is constant on V, Omega = 0 on V, and U is harmonic on V. In particular, the interior of every level set of
Theta is invariant and contained in the interior of the zero set of Omega, and at every endpoint p of gamma, whatever
its type in (iv), Theta - L, L = Theta(p), does not vanish identically on any neighbourhood of p.
Proof outline. Since U = o(|X|), |W(X)| <= c (1 + |X|), so the flow phi_t of W is defined for all real t and each
phi_t is a diffeomorphism of R^2; V, the union of the sets phi_t(D), is open and invariant. By (T), Theta is constant
on orbits, so Theta takes on V its constant value on D, and Theta_x = 0 on V since V is open. For Y in V the orbit of
Y lies in V, so (V) gives d Omega(phi_t Y)/dt = -Omega(phi_t Y) and Omega(Y) = e^{-T} Omega(phi_{-T} Y) for T >= 0. As
in the proof of (xiv)(a), W.X = 2 |X|^2 + (U(X) - U(0)).X >= |X|^2 for |X| >= R, R large, so the disk D_R = {|X| <= R}
is backward invariant and every backward orbit enters it; hence Omega is bounded along the backward orbit of Y, and
T -> infinity gives Omega(Y) = 0. On V, div U = 0 and curl U = -Omega = 0, so U is harmonic there. If D is the
interior of a level set of Theta, then V is open with Theta constant on it, so V is contained in D, and D = V. If
Theta = L on a disk about an endpoint p, then Omega = 0 on that disk, which (xii)(a) excludes. Omega = 0 on V also
follows from (vii): the escaping set E is open and dense (proof of (viii)), Theta = h(arg Phi) on E with det D Phi =
1, so h' = 0 on the open set of directions arg Phi(V n E), and (vii) gives Omega = 0 on V n E, hence on V by
continuity.
Scope of (xxi). The proof uses the boundedness of backward orbits, a global property of profiles, and the conclusion
fails for local solutions without such backward trapping: W = (-x/2, 9y/2 - x^3/3), Omega = x^2 and Theta = 0 satisfy
div W = 4, Omega = -curl W, (T) and (V) on R^2, with Theta constant and Omega != 0 off the axis (here W - 2X is not
sublinear). The proofs of (xii)(b) and (xx)(a) use only the equations near p. The conclusion also follows from the
scattering identities (vii), as noted in the proof outline, and the consequence at endpoints from (vii) and (xii)(a);
neither was stated before, in particular not at incoming endpoints with nonisolated zeros of W off gamma. The second
form of the conclusion of (xii)(b) (Theta not constant on any nondegenerate subarc of gamma ending at p) is not
established at these endpoints, nor at accumulating endpoints every neighbourhood of which contains an arc of zeros of
W off gamma; (xxii) gives necessary conditions for its failure there. (xxi) is a necessary condition. Open sets on
which Theta = L whose closure contains an endpoint, such as the side of the strong unstable curve beyond an outgoing
endpoint ((iv)), are not excluded, and no smooth profile is excluded.
(xxii) Constant temperature on zero arcs (beta = 2). In the setting of (iii):
(a) Theta is not constant on any nondegenerate straight segment contained in the zero set Z of W.
In (b) to (d) let p be an endpoint of gamma, L = Theta(p), C the strong unstable curve of p of (xiii) and (u, v) the
coordinates of step (3) of the proof of (v)-(vii) at p (C = {u = 0} and gamma = {v = 0, u <= 0} near p), and suppose
that Theta = L on a nondegenerate subarc gamma' of gamma that has p as an endpoint. By (xii)(b), (xiv)(c) and (xx)(c),
p is then either incoming and some zero of W off gamma is not isolated, or accumulating and every neighbourhood of p
contains an arc of zeros of W off gamma.
(b) There is a disk N about p such that Theta = L and Omega = 0 at the points of N on C and on the side of C that
meets gamma, U is harmonic on that side in N, and gamma n N minus p is a real analytic curve.
(c) If p is incoming, Theta is not constant on any neighbourhood of any point of the exterior center
branch C_+ at p (the orbit of step (2) of the proof of (v)-(vii), {v = 0, u > 0} near p, with
forward limit p). In particular, no point of the backward limit set of C_+ is a relative interior
point of an arc contained in Z on which Theta is constant.
(d) If p is accumulating, every neighbourhood of p contains an arc of zeros of W off gamma on which Theta is not
constant. Hence, if Theta is constant on each arc of zeros of W off gamma in some neighbourhood of an accumulating
endpoint, Theta is not constant on any nondegenerate subarc of gamma that has this endpoint as an endpoint.
Proof outline. (a) Let I be such a segment, Theta = c on I, and take positively oriented orthonormal coordinates (s,
z) with I in {z = 0}, w = s + i z, and W_s, W_z the components of W. At every zero trace DW = 4, and DW vanishes on
the tangent of I, so, as in the proof of (xiv)(a) for gamma, near a compact subarc of the relative interior of I there
are coordinates (a, b) with I = {b = 0}, a' = b A, b' = b D and D >= d0 > 0, and the backward orbit of each point of a
thin neighbourhood of a shorter subarc I_0 converges to a point of I. Theta is constant on orbits and continuous, so
Theta = c on that neighbourhood. Let V_0 be the component of the interior of {Theta = c} that contains it. By (xxi)
the interior of {Theta = c} is invariant and Omega = 0 on it; V_0 is invariant, since orbits are connected. As in the
proof of (xix)(b), K = W_s - i W_z + 4 i z satisfies d_wbar K = (div W - 4)/2 + (i/2)(d_z W_s - d_s W_z) = i Omega/2,
so K is holomorphic on V_0; K = 0 on I_0, where W = 0 and z = 0, so K = 0 on V_0, that is, W_s = 0 and W_z = 4 z on
V_0. V_0 contains a point Y with z(Y) = z_0 != 0; its orbit lies in V_0, so s(phi_t Y) = s(Y) and
z(phi_t Y) = z_0 e^{4t} for all t. As t -> infinity, |phi_t Y| -> infinity, and U = W - 2X + U(0) equals 2 z e_z plus
a constant vector along this orbit (e_z the unit vector of the z axis), so |U(phi_t Y)|/|phi_t Y| -> 2, contrary to
U = o(|X|). (b) Take the rectangles Q and Q' of the proof of (xii)(b) at p, with Q so small that gamma n Q lies in
gamma'; the steps of that proof used here concern the points with u <= 0 and need only g = 0 for u <= 0 and the
invariance of u = 0, not the type of p. The backward orbits from the points of Q' with u <= 0 stay in Q; for such a
point with u = 0 the backward limit is p, and for one with u < 0 it is a point (u_-, 0) of gamma n Q, hence of gamma'.
Theta is constant on orbits and continuous, so Theta = L on Q' n {u <= 0}. By (xxi), applied to the open set
Q' n {u < 0}, Omega = 0 and U is harmonic there, and Omega = 0 on Q' n {u <= 0} by continuity. Take N in Q'. At a
point q of gamma n N other than p, W is real analytic near q and, by (iii) with Omega(q) = 0, DW(q) = 4 n (x) n, with
n the unit normal of gamma at q; so W.n has nonzero differential at q, its zero set near q is a regular real analytic
curve, Z lies in it near q, and gamma coincides with it near q. (c) Here g < 0 for u > 0 (case (c)). Suppose Theta = c
on a disk D about a point Y_1 of C_+. C_+ has forward limit p, so Theta = L on C_+ and c = L. Take u_0, delta and
J = {u = u_0, |v| <= delta} as in the proof of (xiv)(b); that passage uses only g < 0 for u > 0, not the isolation of
the zeros of W off gamma. Let Y_J be the point of C_+ on J; then Y_J = phi_T(Y_1) for some T, so Theta = L on the
neighbourhood phi_T(D) of Y_J, hence at the points of J with |v| < eta for some eta > 0. By the passage, for u_1 > 0
small enough the backward orbit of every point with 0 < u < u_1 and |v| < delta reaches J at a height |v| < eta, so
Theta = L at these points. With (b), Theta = L on a neighbourhood of p, which (xxi) excludes. For the second
statement, let q be a relative interior point of an arc A contained in Z with Theta = c on A. The argument of (a) for
a compact subarc of the relative interior of A containing q (which uses only that it is a smooth arc of zeros) gives
Theta = c on a disk about q. If q is in the backward limit set of C_+, C_+ meets this disk, which the first statement
excludes. (d) Write G = {u in (0, rho): g(u) = 0}; as in the proof of (xx), the zeros of W in Q off gamma are the
points (u, 0) with u in G, and 0 is in the closure of G. For u_1 in G small, take the curve C_1 through q_1 = (u_1, 0)
and the backward invariant region R = {0 < u < sigma_1(v), |v| < rho_1} of step (1) of the proof of (xx); that step
does not use the hypothesis of (xx)(b) to (d). For Y in R the backward orbit stays in the closure of R, so its
alpha-limit set is a nonempty set of zeros of W in the closure of R (step (1) of the proof of (v)-(vii)), contained in
{(u, 0): 0 <= u <= u_1}. Put theta(u) = Theta(u, 0). On the invariant line v = 0, (T) gives g(u) theta'(u) = 0. If
theta' = 0 on (0, u_1), then theta = L on [0, u_1], and Theta(Y) = L for Y in R, since Theta takes the value Theta(Y)
on the alpha-limit set of Y. Theta = L on C near p, since the backward orbits on C tend to p, and R contains
{0 < u < m, |v| < rho_1} with m > 0; with (b), Theta = L on a neighbourhood of p, contrary to (xx)(a). So
theta'(u_2) != 0 for some u_2 in (0, u_1), and then theta' != 0 on an interval I_2 in (0, u_1) about u_2; g = 0 on
I_2, so {(u, 0): u in I_2} is an arc of zeros of W off gamma on which Theta = theta is not constant. Since u_1 can be
taken arbitrarily small and R then lies in any given disk about p, this holds in every neighbourhood of p. The second
statement of (d) is the contrapositive.
Scope of (xxii). (a) is a necessary condition for profiles, with no hypothesis on the zero set; its proof uses (xxi),
hence the boundedness of backward orbits, and the sublinearity of U at infinity. It concerns straight segments only:
the constancy of Theta on a curved subarc of Z is not excluded. (b) to (d) are necessary conditions at the two kinds
of endpoints at which the second form of the conclusion of (xii)(b) is not established; they do not decide whether
Theta can be constant on a subarc of gamma ending at such an endpoint. At an incoming endpoint, the passage of the
proof of (xiv)(b) gives Theta(Y) = b(v_J(Y)) for the points Y beyond C near p, with b(eta) = Theta(u_0, eta), b(0) = L
and v_J(Y) the height at which the backward orbit of Y reaches J; by the proof of (c), a constant subarc requires that
b be nonconstant on every interval about 0, and nothing more is established about b. At an accumulating endpoint, (d)
replaces the absence of arcs of zeros off gamma near p in the first statement of (xx)(c) by the constancy of Theta on
each of them; the other conclusions of (xx)(b) to (d) are not obtained. The contradiction of (xix)(b) is not available
at these endpoints: its proof evaluates the function E at the points (s, k(s)), s > 0, on the side of C beyond p,
while here Omega = 0 is known only on the side that meets gamma. The existence of a smooth profile remains undecided,
and no local solution or profile is constructed.
(xxiii) Temperatures constant on the horizontal dilates of one curve (beta = 2). Let rho be a positive function of
class C^2 on R, let H be a real function of class C^1 on R, and let Theta(x, y) = H(x/rho(y)), so that Theta is
constant on each curve x = k rho(y).
(a) If H'(k_j) != 0 for a sequence k_j -> +infinity, there is no vector field W of class C^1 on R^2 with
W.grad Theta = 0, div W = 4 and W_1(x, y)/x -> 2 as x -> +infinity for every fixed y.
(b) If H is not constant and rho is bounded above on [y_0, infinity) or on (-infinity, y_0] for some y_0, there is no
vector field W of class C^1 on R^2 with W.grad Theta = 0, div W = 4 and W(X) = 2X + o(|X|) as |X| -> infinity.
In particular, no field satisfying the hypotheses of the opening paragraph, and no profile at beta = 2, has a
temperature as in (a) or (b).
Proof outline. Under the opening paragraph, W - 2X = U - U(0) = o(|X|), which gives the growth conditions of (a) and
(b), and the center jet makes H nonconstant. The map (k, y) -> (k rho(y), y) is a C^2 diffeomorphism of R^2 with
Jacobian rho(y) > 0. Put V(k, y) = W_2(k rho(y), y) and Q(k, y) = W_1(k rho(y), y) - k rho'(y) V(k, y). In these
coordinates the flow of W is k' = Q/rho, y' = V, and direct differentiation gives d_k Q + d_y(rho V) = rho div W, with
d_y at fixed k. (T) reads H'(k) Q/rho = 0. So on every open interval I on which H' != 0, Q = 0 on I x R, hence
d_y(rho V) = 4 rho there, and with R(y) = int_0^y rho(t) dt, rho(y) V(k, y) = 4 R(y) + rho(0) V(k, 0) for k in I and
every real y. (a) Each k_j lies in such an interval; put C_j = rho(0) V(k_j, 0). Since Q = 0 there, at
x_j = k_j rho(y) this gives W_1(x_j, y)/x_j = rho'(y) (4 R(y) + C_j)/rho(y)^2. For fixed y, x_j -> +infinity, so the
right side tends to 2 as j -> infinity. If rho'(y_1) = 0, the right side vanishes at y_1 for every j; so rho' has no
zero, and, at every fixed y, C_j converges to 2 rho(y)^2/rho'(y) - 4 R(y). The limit C of the sequence C_j does not
depend on y, so 4 R + C = 2 rho^2/rho' on R. Differentiating, 4 rho = 4 rho - 2 rho^2 rho''/rho'^2, so rho'' = 0 and
rho is affine; being positive on R, it is constant, which contradicts rho' != 0. (b) The reflection (x, y) -> (x, -y),
with W replaced by (W_1(x, -y), -W_2(x, -y)) and rho by rho(-y), preserves the hypotheses, so let rho <= M on
[y_0, infinity). Since H is not constant, H' != 0 on some open interval; take k_* in it and put
S(y) = rho(y) V(k_*, y) = 4 R(y) + rho(0) V(k_*, 0), so S' = 4 rho. Along (k_* rho(y), y) the first coordinate is
bounded, so V(k_*, y) = W_2(k_* rho(y), y) = 2y + o(y) as y -> +infinity, and for large y, y <= V <= 3y,
0 < S <= 3 M y and S'/S = 4/V >= 4/(3y). Integration gives S(y) >= c y^{4/3} for large y with c > 0, a contradiction.
The letters rho, H, k, k_j, k_*, I, x_j, V, Q, R, S, M, C_j and C are local to (xxiii).
Scope of (xxiii). (xxiii) is a restricted exclusion. (a) uses only (T), div W = 4 and the growth of W_1 along
horizontal half-lines, and (b) only (T), div W = 4 and W = 2X + o(|X|); neither uses (V), the inverse, the parities or
the center data, and both use the value 2 of beta through the form of (T) (for beta != 2, (T) is
W.grad Theta = (beta - 2) Theta and the argument does not apply). Temperatures of this form can satisfy the conditions
of the opening paragraph on Theta: for H(k) = k^2/(1 + k^2) and smooth rho, Theta = x^2/(x^2 + rho(y)^2) is even in x,
vanishes on the axis and equals x^2/rho(0)^2 + O(|X|^3) near 0, and H' != 0 for all k > 0. The hypothesis on H' in (a)
cannot be dropped: for constant H, W = 2X satisfies the three conditions for every rho. The limit argument of (a), as
x -> +infinity at fixed y, gives no exclusion when H is constant on [K, infinity) for some K, and (b) excludes this
case only when rho is bounded above on a half-line. For some rho unbounded at both ends, the hypotheses of the opening
paragraph do not exclude this case: for rho(y) = (1 + y^2)^{1/2}, k = x/rho(y), a smooth even H with H(k) = k^2 near 0
and H' = 0 for |k| >= 1, and psi = 2 F(k) arsinh(y) with F(k) = k chi(k), chi smooth and even, equal to 1 on [-1, 1]
and to 0 outside [-2, 2], the fields U = (-psi_y, psi_x) (bounded, U(0) = 0), W = 2X + U and Theta = H(k) satisfy all
the hypotheses of the opening paragraph; W(x, 0) = 0 and Omega(x, 0) = -Lap psi(x, 0) = 0 for small x, while
Theta_x(x, 0) = 2x, so (V) fails. The final contradiction of (a) uses the representation for all real y: if it holds
only for y in an open interval J on which rho > 0, the same argument, with R replaced by a primitive of rho based at a
point of J, shows only that rho is affine and nonconstant on J, and this case occurs: for rho(y) = a y + b, a != 0,
W = 2X + (0, 2b/a) satisfies the three conditions of (a) for y in J (the curves x = k rho(y), y in J, are portions of
rays issuing from (0, -b/a)). In the setting of (iii), (xxiv) excludes every temperature admitting a representation
Theta(x, y) = H(x/rho(y)) on a neighbourhood of the whole axis, and therefore every globally represented temperature
of this form. Temperatures with no such representation near the whole axis are not covered by (xxiii) or (xxiv), and
the existence of a smooth profile remains undecided.
(xxiv) No temperature constant on the horizontal dilates of one curve near the axis (beta = 2). In the setting of
(iii), there are no neighbourhood N of the axis {x = 0}, function rho: R -> (0, infinity) and function H defined at
x/rho(y) for every (x, y) in N such that Theta(x, y) = H(x/rho(y)) for every (x, y) in N. No regularity of rho or H is
assumed.
In particular, Theta is not of the form H(x/rho(y)) on R^2, whatever H and rho > 0.
Proof outline. The reflection of 4.8 (Theta -> -Theta(x, -y), U -> S_y U(S_y X), S_y(x, y) = (x, -y)) maps this class
to itself (H -> -H, rho -> rho(-y), N -> S_y N), so let a0 > 0. Put rho_0 = rho(0). Then H(k) = Theta(k rho_0, 0) for
small |k|, so H is smooth and even near 0, H(0) = 0 and A := H''(0) = 2 a0 rho_0^2 > 0;
Theta_xx(0, y) = A/rho(y)^2, so rho = (A/Theta_xx(0, y))^{1/2} is smooth. Replacing H(k) by H(k/rho_0) and rho by
rho/rho_0, which does not change Theta, let rho_0 = 1 and A = 2 a0. (1) Near the axis. H'(k) = A k + O(k^3), so
H' != 0 for 0 < |k| < eps_1, for some eps_1 > 0. For Y > 0 choose eps_Y in (0, eps_1] such that the points
(k rho(y), y) with |k| <= eps_Y and |y| <= Y lie in N. With V(k, y) = W_2(k rho(y), y) and Q = W_1 - k rho' V as in
the proof of (xxiii), (T) gives Q = 0 for 0 < |k| < eps_Y, |y| <= Y, hence for |k| < eps_Y, and
d_k Q + d_y(rho V) = 4 rho gives rho V = 4 R + c(k) there, with R(y) = int_0^y rho and c(k) = V(k, 0) = W_2(k, 0),
which does not depend on Y and is smooth and even with c(0) = 0; write c(k) = c_2 k^2 + c_4 k^4 + O(k^6). So
W_2 = (4 R + c(x/rho))/rho and W_1 = (x rho'/rho) W_2 for |y| <= Y and |x| < eps_Y rho(y). (2) Axis.
phi(y) := W_2(0, y) = 4 R(y)/rho(y) vanishes only at 0, and phi(y) = 2 y + o(|y|) since U = o(|X|). From
d_x^2 W_2(0, y) = 2 c_2/rho^3 and d_x W_1(0, y) = 4 - phi' (div W = 4 on the axis),
q(y) := Omega_x(0, y) = -2 c_2/rho^3 - phi''. The zeros of b = phi nearest to 0 are at -infinity and +infinity, so
q > 0 on R by 4.13(i). (3) If c_2 >= 0, then phi'' = -q - 2 c_2/rho^3 < 0 on R, so phi' > phi'(0) = 4 on
(-infinity, 0) and phi(y)/y > 4 for y < 0, contrary to phi(y) = 2 y + o(|y|). (4) Let c_2 < 0. Put
L(f) = 4 R f' + rho f, a_1 = rho^{-2}, a_2 = rho'^2/rho^2,
a_3 = rho phi'' = -4 R rho''/rho - 4 rho' + 8 R rho'^2/rho^2 and a_4 = -rho''/rho + 2 rho'^2/rho^2. Direct
differentiation gives, at (k rho(y), y) with |y| <= Y and |k| < eps_Y, with c = c(k), rho (W.grad Omega + Omega) =
-(c' L(a_1) + k^2 c' L(a_2) + k L(a_3) + k c (L(a_4) + a_3') + c c' a_1' + k^2 c c' a_2' + k c^2 a_4'), and (V)
makes this equal to rho Theta_x = H'(k) = A k + B k^3 + O(k^5). The coefficients of k and k^3 give, for every real
y, E_1: L(a_3) + 2 c_2 L(a_1) + A = 0, which is -rho^2 times the second equation of 4.13(i), and
E_3: 4 c_4 L(a_1) + 2 c_2 L(a_2) + c_2 (L(a_4) + a_3') + 2 c_2^2 a_1' + B = 0. Let r_n be the Taylor coefficients
of rho at 0 (r_0 = 1). The coefficient of y^n in E_1 is -4 (n+1)^2 (4n+1) r_{n+1} plus a polynomial in
r_1, ..., r_n, c_2 and A; so A = 2 (2 r_1 - c_2), and every r_n is a polynomial in r_1 and c_2. In E_3 the
coefficient of y^0 determines B, and that of y is -r_1 (219 c_2^3 + 6026 c_2^2 r_1 + 32 c_2 r_1^2 + 12960 c_4)/360.
If r_1 != 0, this fixes c_4, and then, with t = c_2/r_1, the coefficients of y^2 and y^3 are nonzero multiples
(c_2 != 0, 2 r_1 - c_2 = A/2 != 0) of P_2(t) = -130509 t^2 + 4496958 t + 12320 and
P_3(t) = -405889875 t^3 + 30302578176 t^2 + 58633849676 t + 1213256384, whose resultant is
-50076093926441217209396936743211581440 != 0 (exact computation). So r_1 = 0, c_2 = -A/2, and the Taylor series of
rho at 0 is that of the constant 1, which solves E_1 for c_2 = -A/2. With Z = (rho, y rho', y^2 rho'', R/y), E_1
and R' = rho read y Z' = F(y, Z) near y = 0, with F smooth near (0, (1, 0, 0, 1)) (R/y = int_0^1 rho(s y) ds) and
F(y, (1, 0, 0, 1)) = 0 for small y, since rho = 1 solves E_1 for c_2 = -A/2. Then D = Z - (1, 0, 0, 1) is flat at 0
and y D' = M(y) D with |M| <= K, so |D(y_1)| <= |D(y)| (y_1/y)^K for 0 < y < y_1, which gives D(y_1) = 0; likewise
for y < 0. Hence rho = 1 near 0 and, since E_1 is a regular fourth order equation for R where R != 0, rho = 1 on R.
Then phi = 4 y, contrary to phi(y) = 2 y + o(|y|). The letters S_y, N, rho, rho_0, H, A, B, eps_1, eps_Y, Y, k, V, Q,
R, c, c_2, c_4, phi, q, b, L, a_1 to a_4, E_1, E_3, r_n, t, P_2, P_3, Z, F, D, M, K and y_1 are local to (xxiv).
Scope of (xxiv). In the full smooth setting of (iii), (xxiv) excludes any representation Theta(x, y) = H(x/rho(y)) on
a neighbourhood of the whole axis, with rho: R -> (0, infinity) and H defined at x/rho(y) for every (x, y) in the
neighbourhood; neither function is initially assumed regular. Unlike (xxiii), it uses (V), the center jet (a0 != 0
makes rho smooth and makes H'(k) nonzero for all sufficiently small k != 0), the axis system 4.13(i), and U = o(|X|)
along the axis; it uses neither the inverse, class A, nor bounds on Omega. Since only a neighbourhood of the axis
enters, it covers the case of the Scope of (xxiii) in which H is constant on [K, infinity); the example given there
satisfies (T) but not (V). The case c_2 < 0 rests on an exact computation of finitely many Taylor coefficients and of
one resultant and on the uniqueness argument at the singular point y = 0 of E_1; no numerical evaluation is used. A
representation on a neighbourhood of a bounded part of the axis only is not covered: (3) uses phi on the whole half
axis y < 0, and (4) uses E_1 on the whole axis and the growth of phi. Temperatures not of this form near the axis are
not covered, and the existence of a smooth profile remains undecided.
4.8 Vorticity mass lower bound (no far-field derivative control). Let beta >= 2 and let U, Omega, Theta be smooth
solutions of (T), (V), div U = 0, -curl U = Omega, with the B2 parity, Theta(0,y) = 0 and Theta = a0 x^2 + O(|X|^3),
a0 != 0, and |U_rel(X)| <= C(1+|X|)^{1-eps} for some eps > 0. (In class A this power bound holds automatically: it follows
from |Omega| <= C(1+|X|)^{-delta} by splitting the subtracted Biot-Savart integral.) Then
  M(R) := int_{|X|<R} |Omega| dX >= c R^{2-2/beta}   for all large R.
Consequences: Omega is not uniformly o(r^{-2/beta}); int |Omega|(1+|X|)^{-gamma} dX = infinity for every gamma <= 2 - 2/beta;
Omega is not in L^p for 1 <= p <= beta (and, if bounded, for 0 < p < 1). So in class A the (H2) conclusions of Theorem E hold
without (D). (At the endpoint gamma = 2 - 2/beta use int (1+|X|)^{-gamma}|Omega| = gamma int_0^infty (1+r)^{-gamma-1} M(r) dr;
at p = beta, finite L^beta norm gives M(R) = o(R^{2-2/beta}) by splitting off a fixed ball and applying Hoelder on the
complement. These consequences are superseded by 4.9.)
Proof outline. Normalize a0 > 0 by the exact reflection Theta -> -Theta(x,-y), Omega -> -Omega(x,-y),
U -> S U(SX), S(x,y) = (x,-y). Choose f smooth, 0 <= f <= 1, f = 0 on (-infinity, a/4], f = 1 on [a/2, infinity),
g(t) = int_0^t f. Both transport equations give the exact identity
  div[ W Omega f(Theta) - g(Theta) e_x ] = [ (2 beta - 1) f(Theta) + (beta - 2) Theta f'(Theta) ] Omega.
Integrate it against h_R(x,y) = eta(x/R) chi(y/R) on the half plane x > 0 (no axis flux since f(Theta) = g(Theta) = 0 on
x = 0; eta smooth on [0, infinity), nonincreasing, eta' <= -c0 on [0,1], zero on [2, infinity); chi in C_c^infty((-2,2)),
0 <= chi <= 1, chi = 1 on [-1,1]). Since |W| <= C(1+|X|),
  int_{(0,R) x (-R,R)} g(Theta) <= C R M(3R).
For s >= a, g(s) >= s/2. A relatively compact patch D in {x > 0} with Theta >= a > 0 is carried by the flow into
{x > 0} with area e^{2 beta t}|D|, temperature >= a e^{(beta-2)t}, and, by the power bound, radius <= C e^{beta t}, so it
contributes at least c e^{(3 beta - 2)t} to the integral of g(Theta). Taking R = C e^{beta t} gives
c R^{3-2/beta} <= C R M(3R).
Extension under sublinear velocity only. If the power bound is replaced by U_rel = o(|X|) alone (U the canonical
velocity), then Omega is not in L^p(R^2) for any 1 <= p <= beta; this includes finite enstrophy at beta = p = 2.
Proof outline. (a) 1 <= p < beta: the flow bound becomes |phi_t X| <= C_rho e^{(beta + rho) t} for every rho > 0, and the
argument above gives M(R) >= c_rho R^{kappa_rho}, kappa_rho = (3 beta - 2)/(beta + rho) - 1 -> 2 - 2/beta, which
contradicts M(R) <= C R^{2 - 2/p} ||Omega||_p for small rho. (b) p = beta > 2: the kernel difference K(X - .) - K(-.) has
L^{p'} norm C|X|^{1 - 2/p}, so Omega in L^p forces U - U(0) to be the subtracted Biot-Savart integral (the difference is
harmonic and sublinear, hence constant) with |U_rel(X)| <= C ||Omega||_p |X|^{1 - 2/p}; the power bound holds, so
M(R) >= c R^{2 - 2/beta}, while splitting off a large ball and using Hoelder on the tail gives M(R) = o(R^{2 - 2/p}).
(c) p = beta = 2: U is tempered; write DU = H + P, with H in L^2 the matrix of Riesz-type multipliers applied to Omega
and P a polynomial matrix. Sublinearity gives DU(R .) -> 0 in distributions, and H(R .) -> 0 by its L^2 bound, so P = 0
and Plancherel gives ||DU||_2 = ||Omega||_2 (Frobenius norm). Poincare on balls and telescoping of the ball means give ||U_rel||_{L^2(B_R)} <= C R (1 + log R).
For a patch D with Theta >= a > 0, the scaled positions Z_t = e^{-beta t} phi_t satisfy
||dZ_t/dt||_{L^2(D)} = e^{-2 beta t} ||U_rel||_{L^2(phi_t D)} <= C (1 + t) e^{(rho - beta) t}, so they stay bounded in
L^2(D); by Chebyshev, for each t there is a measurable D_t in D with |D_t| >= |D|/2 and phi_t(D_t) in B_{C e^{beta t}}
(D_t may depend on t), and the mass argument applied to phi_t(D_t) gives M(R) >= c R, while finite enstrophy gives
M(R) = o(R).

4.9 Circulation of material domains and the slow-tail mass bound. Let beta >= 2 and let U, Omega, Theta be smooth
solutions of (T), (V), div U = 0, -curl U = Omega, with the B2 parity, Theta(0,y) = 0, Theta = a0 x^2 + O(|X|^3), a0 != 0,
and U_rel = o(|X|). Then there is a bounded domain D in {x > 0} and a number A_D with a0 A_D > 0 such that, for every
eta in (0,1),
  int_{phi_t D} Omega dX = e^{(2 beta - 1) t} [A_D + O(e^{-(1 - eta) t})],
and, for all large R,
  int_{B_R cap {x > 0}} ((sign a0) Omega)_+ dX >= c_eta R^{(2 beta - 1)/(beta + eta)}.
Under the power bound |U_rel(X)| <= C(1+|X|)^{1-eps} (automatic in class A) the error is O(e^{-t}) and
  int_{B_R cap {x > 0}} ((sign a0) Omega)_+ dX >= c R^{2 - 1/beta},   so M(R) >= c R^{2 - 1/beta}.
Consequences. (i) Omega is not in L^p(R^2) for any 1 <= p <= 2 beta, under U_rel = o(|X|) alone (this supersedes the
range p <= beta of 4.8). (ii) Under the power bound, int |Omega|(1+|X|)^{-gamma} dX = infinity for every
gamma <= 2 - 1/beta, and Omega is not uniformly o(|X|^{-1/beta}); in particular no profile has a vorticity tail bounded
by C(1+|X|)^{-2/beta}. (iii) Under U_rel = o(|X|) alone, Omega is not uniformly o(|X|^{-1/beta}) (such a vorticity lies in L^p for every
finite p > 2 beta, and then the subtracted Biot-Savart velocity obeys the power bound, see (b) below), and the weighted
integral in (ii) diverges for every gamma < 2 - 1/beta. The endpoint gamma = 2 - 1/beta is proved here only under the
power bound; by 4.15 it therefore holds throughout the polynomially controlled target class.
The statement does not assert that the signed integral of (sign a0) Omega over a half-ball is large (opposite-sign
vorticity outside phi_t D may cancel it), and it gives no pointwise limit of e^t Omega(phi_t X) or angular expansion of
Omega; those would need a separate convergence theorem.
Proof outline. (1) Flow bounds: sublinearity gives |phi_t X| <= C_{K,eta} e^{(beta + eta) t} on compact sets K, and the
power bound gives |phi_t X| <= C_K e^{beta t} (differential inequality for (1 + |phi_t X|)^eps). The flow preserves
{x > 0} by axis invariance. (2) For a bounded piecewise smooth D and J(t) = int_{phi_t D} Omega, Reynolds transport,
div W = 2 beta and (V) give
  J' = (2 beta - 1) J + B(t),   B(t) = int_{phi_t D} Theta_x = oint_{boundary of phi_t D} Theta dy.
Pulling the boundary back with Theta o phi_t = e^{(beta - 2) t} Theta and integrating by parts on the closed curve,
  B(t) = - e^{(beta - 2) t} oint_{boundary of D} (phi_t X)_2 dTheta,
so |B(t)| <= C_D e^{(2 beta - 2 + eta) t}, which is integrable against e^{-(2 beta - 1) t}. Hence J(t) e^{-(2 beta - 1) t}
converges to
  A_D = int_D Omega - oint_{boundary of D} H dTheta,   H(X) = int_0^infty e^{-(beta + 1) s} (phi_s X)_2 ds,
with H continuous (locally uniform convergence; Fubini) and differentiability of H not needed. (3) The y-axis is
invariant and the origin is an equilibrium, so (phi_s(0,b))_2 > 0 for b > 0 and all s >= 0; hence H(0,b) > 0 = H(0,0).
Near the origin Theta = x^2 a(x,y) with a(0,0) = a0, and xi = x (a/a0)^{1/2} is an orientation-preserving coordinate with
Theta = a0 xi^2. Let D be the image of a small rectangle 0 < xi < h, 0 < y < b. On its vertical sides dTheta = 0, and
  -oint_{boundary of D} H dTheta = 2 a0 int_0^h xi [H(xi, b) - H(xi, 0)] dxi,
which has the sign of a0 for h small (continuity of H); int_D Omega has the sign of a0 since Omega = (4 a0/beta) x + O(|X|^2).
So a0 A_D > 0. Only continuity is used, so flat jets elsewhere and beta = 2 are covered. (4) For large t,
(sign a0) J(t) >= |A_D| e^{(2 beta - 1) t}/2, and this is at most the integral of ((sign a0) Omega)_+ over phi_t D, which
lies in {x > 0} and in a ball of radius C e^{(beta + eta) t} (resp. C e^{beta t}); every large R is of that form.
(a) 1 <= p < 2 beta: Hoelder gives M(R) <= C ||Omega||_p R^{2 - 2/p}, and 2 - 2/p < (2 beta - 1)/(beta + eta) for small eta.
(b) p = 2 beta (>= 4): for p > 2 the subtracted kernel satisfies ||K(X - .) - K(-.)||_{L^{p'}} <= C_p |X|^{1 - 2/p}, so the
subtracted Biot-Savart integral of Omega in L^p is a continuous field with |V(X)| <= C ||Omega||_p |X|^{1 - 2/p}; U_rel differs
from it by a harmonic sublinear field vanishing at 0, hence by nothing. Thus the power bound holds and
M(R) >= c R^{2 - 1/beta}, while splitting off a large ball and applying Hoelder on the complement gives M(R) = o(R^{2 - 1/beta}).
(c) For 0 < gamma <= 2 - 1/beta the weighted statement follows from the identity int_{|X|>1} |Omega|
|X|^{-gamma} = gamma int_1^infty R^{-gamma-1}(M(R) - M(1)) dR (Tonelli) and M(R) >= c R^{2 - 1/beta}; for gamma <= 0
it follows from M(R) -> infinity, since |X|^{-gamma} >= 1 on |X| > 1; the weights |X|^{-gamma} and (1+|X|)^{-gamma}
are comparable on |X| > 1. Finally, uniform o(|X|^{-1/beta}) decay gives M(R) = o(R^{2 - 1/beta}) directly.

4.10 Temperature far field. Let beta >= 2, let U_rel be smooth and divergence free with the B2 velocity parity and
|U_rel(X)| <= C(1+|X|)^{1-delta}, delta > 0 (automatic in class A), put W = beta X + U_rel, and let Theta be smooth,
solve (T), and satisfy the B2 temperature parity, Theta(0,y) = 0 and the jet Theta = a0 x^2 + O(|X|^3) with a0 > 0
(after the reflection of 4.8). No hypothesis (D), no decay of DU_rel and no vorticity equation is used.
With m = 1 - 2/beta there is a continuous 2 pi-periodic function A such that
  r^{-m} Theta(r e(theta)) -> A(theta) uniformly in theta,   e(theta) = (cos theta, sin theta),
with A(+-pi/2) = 0 and A > 0 at some angle strictly inside the right semicircle. In particular |Theta| <= C(1+|X|)^m,
so sup_{|X|=r} |Theta| is comparable to r^m (A vanishes on the axis, so this is not a lower bound on every ray; for
beta = 2, Theta is bounded and tends to an angular function).
Proof outline. Choose rho with W.e_r >= beta r/2 for r >= rho. The trajectory from rho e(sigma) meets each circle r >= rho
once, at time s(r, sigma) and angle h_r(sigma). Then d_r s = 1/(beta r) + O(r^{-1-delta}) and d_r h_r = O(r^{-1-delta})
uniformly, so tau_r = s - (1/beta) log(r/rho) and h_r converge uniformly. Since div W = 2 beta, the Jacobian of the flow
coordinates gives exactly h_r'(sigma) = rho w_r(rho, sigma) e^{2 beta s(r,sigma)} / [r w_r(r, h_r(sigma))], w_r = W.e_r,
which converges uniformly to a positive continuous limit; so h_infty is a C^1 circle diffeomorphism and the inverses
converge uniformly. Transport gives r^{-m} Theta(r e(h_r(sigma))) = rho^{-m} e^{(beta-2) tau_r(sigma)} Theta(rho e(sigma)),
and composing with h_r^{-1} gives the limit. The invariant axis has Theta = 0, so A(+-pi/2) = 0. A patch in {x > 0} with
Theta >= a > 0 cannot stay in B_rho (its area grows like e^{2 beta t}); its escaping orbits give A > 0 at their limiting
angles, which are not axis angles.

4.11 Sector circulation, the drift integral and the leading trajectory coefficient. Let beta >= 2 and let U, Omega,
Theta be smooth solutions of (T), (V), div U = 0, -curl U = Omega, with the B2 parity, Theta(0,y) = 0,
Theta = a0 x^2 + O(|X|^3), a0 != 0, and |U_rel(X)| <= C(1+|X|)^{1-eps}, eps > 0 (automatic in class A).
(i) There are 0 < a < b, eps0 > 0 and c > 0 such that, with the sector-annulus K = {a <= |X| <= b, x >= eps0 |X|},
  int_{RK} ((sign a0) Omega)_+ dX >= c R^{2-1/beta}   for all large R.
(ii) Consequently int_{|X|>1} |x| |X|^{-gamma-1} ((sign a0) Omega)_+ dX = infinity for every gamma <= 2 - 1/beta. For
gamma = 1, for all large R,
  (1/pi) int_{B_R cap {x>0}} x |X|^{-2} ((sign a0) Omega)_+ dX >= c R^{1-1/beta},
so the vertical component (1/(2 pi)) int Y_1 Omega(Y) |Y|^{-2} dY of the unsubtracted Biot-Savart velocity at the center
is not absolutely convergent for any such profile, beta = 2 included. If moreover a0 > 0 and Omega >= 0 on {x > 0} (the
sign of the Chen-Hou production mechanism), the truncations (1/pi) int_{B_R cap {x>0}} x Omega |X|^{-2} dX are
nondecreasing and tend to +infinity at least like R^{1-1/beta}.
(iii) If (D) of 4.6 also holds (automatic in class A by 4.12), the leading coefficient A_tr in the trajectory expansion
Omega(phi_t Y) = e^{-t} A_tr(Y) - e^{-2t}(g(Y) + o(1)) of step (4) of 4.6 is not identically zero on E.
Proof outline. (1) Assume a0 > 0 (reflection of 4.8). Near the origin Theta = a0 xi^2 with the coordinate xi of 4.9 and
Omega = x b(x,y), b(0,0) = 4 a0/beta. The function H of 4.9 is strictly increasing along the positive y-axis, since
distinct axis trajectories keep their order. Choose 0 < b1 < b2 small with W_2 > 0 on {0} x [b1, b2], and h > 0 small, so
that for 0 < u < v < h the coordinate rectangle D = {u < xi < v, b1 < y < b2} has Omega > 0 on D and
  A_D = int_D Omega dX + 2 a0 int_u^v xi [H(xi, b2) - H(xi, b1)] dxi > 0
(the sides xi = u and xi = v contribute nothing to the boundary term -oint H dTheta of 4.9, since Theta is constant on
them; their contributions to the flux oint Theta dy of 4.9 are in general nonzero).
(2) The closure of D can be taken inside the escape set E. For beta > 2 this holds because Theta != 0 on it and
Theta(phi_t X) = e^{(beta-2)t} Theta(X). For beta = 2, Sard's theorem gives a regular value c0 = a0 xi0^2 of Theta with
0 < xi0 < h. Each component of {Theta = c0} is a properly embedded line: a closed component would be a closed curve to which
W is tangent, so the divergence theorem would give 4 times its enclosed area = 0. At a zero of W on such a line, DW maps
into the tangent line and has trace 4, so the zero is a simple repeller of the induced one-dimensional flow; hence every
nonstationary point of the level escapes to infinity. The segment {xi = xi0, b1 <= y <= b2} has no zero of W (W_2 > 0), so
it lies in the open set E, and so does a thin coordinate rectangle around it.
(3) For sigma on a large circle |X| = rho, the arrival angle h_r(sigma) at radius r converges uniformly to a C^1 circle
diffeomorphism h_infty (flux Jacobian of 4.10), which fixes the two vertical angles. Hence
Phi(X) = lim e^{-beta t} phi_t X exists locally uniformly on E, is continuous and nonzero, and Phi_1 > 0 on E cap {x > 0}.
The extrema of |Phi| and Phi_1/|Phi| on the compact closure of D give a, b, eps0 with phi_t D contained in e^{beta t} K
for large t. By 4.9 (power-bound case), int_{phi_t D} Omega >= (A_D/2) e^{(2 beta - 1) t}, and the positive-part integral
over e^{beta t} K dominates it; put R = e^{beta t}.
(4) On RK, |x| |X|^{-gamma-1} >= d_gamma R^{-gamma} with d_gamma = eps0 min(a^{-gamma}, b^{-gamma}); this gives (ii), using
the disjoint annuli R_j K, R_j = R_* q^j, q > b/a, at the endpoint gamma = 2 - 1/beta. For (iii): if A_tr = 0 on E, then
e^{2t} Omega(phi_t Y) converges locally uniformly on E, so |Omega(phi_t Y)| <= C_D e^{-2t} on the closure of D and
|int_{phi_t D} Omega| <= C_D |D| e^{(2 beta - 2) t}, contradicting the growth e^{(2 beta - 1) t} in (3).
Remarks. (a) By (A5), (ii) means that the drift v0 = U(0) of a class A profile is not given by an absolutely
convergent ordinary Biot-Savart integral; it is fixed only by a declared convention, and changing it changes the reconstructed center path
z_c(t) = z_* - v0 tau^beta / beta but not the profile. (b) An independent argument (testing the rescaled vorticity
equation against a compactly supported function in {x > 0}, using the temperature limit Theta_infty = r^m A(theta) of
4.10 and the fact that the distributional derivative d_x Theta_infty does not vanish on {x > 0}: otherwise the
continuous function Theta_infty would be constant along horizontal segments there and hence zero, by its zero axis
values, whereas A > 0 at some angle of the right semicircle) gives the weaker sector bound int_{RK'} |Omega| >= c
R^{2-2/beta}; it is superseded by (i).

4.12 Theorem D (automatic far-field derivative control and the polar vorticity tail in class A). Every class A profile
(necessarily beta >= 2 by Theorem A) satisfies, outside a sufficiently large ball, with r = |X|:
  (a) the admissible decay exponent obeys delta <= 1/beta, and |DU_rel(X)| <= C r^{-delta};
  (b) (D) of 4.6 holds, with eps(R) <= C R^{-delta};
  (c) |grad Theta(X)| <= C r^{-2/beta};
  (d) there is a continuous function a on the unit circle, not identically zero, with a(pi - theta) = -a(theta), such that
        sup_theta | r^{1/beta} Omega(r e(theta)) - a(theta) | -> 0   as r -> infinity;
  (e) consequently |Omega| <= C r^{-1/beta}, so delta = 1/beta is admissible and is the largest admissible exponent, and
      |DU_rel(X)| <= C r^{-1/beta}, |U_rel(X)| <= C r^{1-1/beta};
  (f) with eps0 the constant of the sector K of 4.11(i), (sign a0) a(theta) > 0 on a nonempty open arc of angles with
      cos theta > eps0, and hence, by the parity of a, (sign a0) a < 0 on its mirror arc in the left half-plane;
  (g) (critical flux identity) the integral below converges absolutely and
        int_{R^2} |Omega|^{2 beta - 2} Omega Theta_x dX = (1/2) int_0^{2 pi} |a(theta)|^{2 beta} d theta > 0,
      although Omega is not in L^{2 beta} (4.9).
Together with 4.10, the far field of every class A profile is Omega = r^{-1/beta}(a(theta) + o(1)),
Theta = r^{1-2/beta}(A(theta) + o(1)), uniformly in theta. Constants depend on the profile (no bound uniform over
profiles is asserted). This is not a nonexistence result: the homogeneous pair r^{-1/beta} a(theta),
r^{1-2/beta} A(theta) solves the leading-order (dilation) part of (T) and (V) for arbitrary angular functions, because
the forcing Theta_x and the advection by U_rel enter at lower orders.
Proof outline. Write V = U_rel, W = beta X + V, r = |X|; all cutoffs are frozen when a convolution is differentiated.
(0) Exponent bound. If delta > 1/beta, choose 1/beta < d < min(delta, 2); then 4.9 gives
c R^{2-1/beta} <= int_{B_R} |Omega| <= C R^{2-d}, a contradiction. So 0 < delta <= 1/beta <= 1/2.
(1) Modulus. Omega is bounded and in L^p for a finite p > max(1, 2/delta). Splitting the kernel at distances h and 1
gives |V(P) - V(Q)| <= C h (1 + log(1/h)) for h = |P - Q| <= 1 and <= C h for h >= 1 (Hoelder with the L^{p'} norm of the
kernel derivative outside the unit ball, then subdivision into segments). Hence |W(P) - W(Q)| <= C r^{1/2} |P - Q|^{1/2} for
|P| = r >= 1 and |P - Q| <= r. No bound on DV is used.
(2) Directional commutator lemma. Let X be large, f smooth with support in B(X, r/4), |f| <= A and |W.grad f| <= C A there,
Z = K * f, w = |W(X)| >= c r, e = W(X)/w. The distributional derivative of K is the principal value of its classical
derivative plus (1/2) J delta_0, J = J_- the rotation by -pi/2, so
  w DZ(X) e = int K(X - Y) div(W f)(Y) dY + int DK(X - Y) [W(X) - W(Y)] f(Y) dY,
with the two delta contributions cancelling exactly. Since div(W f) = 2 beta f + W.grad f, the first term is <= C A r; by
(1) the commutator kernel is <= C r^{1/2} |X - Y|^{-3/2}, so the second is <= C A r. Thus |DZ(X) e| <= C A. Since Z is
divergence free with -curl Z = f, DZ is trace free with antisymmetric part determined by f, and a trace-free 2 x 2 matrix
is determined by its value on a unit vector and its antisymmetric part (the linear system has determinant 1); so
|DZ(X)| <= C(|DZ(X) e| + |f(X)|) <= C A.
(3) Temperature potential. Let chi_X = 1 on B(X, r/8), supported in B(X, r/4), |grad chi_X| <= C/r. By (T),
W.grad(chi_X Theta) = (beta - 2) chi_X Theta + Theta W.grad chi_X, so (2) applies to f = chi_X Theta with
A_X = sup_{B(X, r/4)} |Theta| <= C r^{1-2/beta} (4.10): |D(K * (chi_X Theta))(X)| <= C A_X. Hence the integral on the
left of the following identity is <= C A_X:
  int K(X - Y) chi_X(Y) Theta_x(Y) dY = d_1 [K * (chi_X Theta)](X) - int K(X - Y) (d_1 chi_X)(Y) Theta(Y) dY
(4) Strain. DV(X) = D[K * (chi_X Omega)](X) + int DK(X - Y)(1 - chi_X(Y)) Omega(Y) dY; the second integral converges
absolutely (the subtraction constant of the canonical inverse does not enter DV) and is <= C r^{-delta} since delta < 2.
For the first, apply the identity of (2) with f = chi_X Omega. By (V), div(W f) = 2 beta chi_X Omega + chi_X(Theta_x - Omega) +
Omega W.grad chi_X; the terms other than chi_X Theta_x, and the commutator, contribute C r^{1-delta}, and the
chi_X Theta_x term contributes C A_X by (3). Dividing by w and using the div-curl algebra,
|DV(X)| <= C (r^{-delta} + r^{-2/beta}) <= C r^{-delta}, by (0). This is (a).
(5) Escape and (D). |V| <= C r^{1-delta} gives |log(|phi_t Y|/|Y|) - beta t| <= C |Y|^{-delta} uniformly for large |Y| and
t >= 0; integrating (a) along orbits gives (b).
(6) Gradient. Differentiating (T), q = grad Theta satisfies d/dt q(phi_t Y) = -(2I + DV^T) q(phi_t Y). Every exterior
point lies on an orbit from a fixed large circle; Gronwall with (b) gives |q(phi_t Y)| <= C e^{-2t}, which by (5) is (c).
(7) Polar tail. By (b), steps (1)-(4) of 4.6 apply. The scattering map Phi(Y) = lim e^{-beta t} phi_t Y is a C^1
area-preserving diffeomorphism of the escape set E onto R^2 \ {0} with Phi o phi_s = e^{beta s} Phi, and, for large |Y|,
|D Phi(Y) - I| <= e^{eps(|Y|)} - 1 and |Phi(Y) - Y| <= C |Y|^{1-delta}. The amplitude
A_tr(Y) = Omega(Y) + int_0^infty e^s Theta_x(phi_s Y) ds is continuous on E with A_tr(phi_s Y) = e^{-s} A_tr(Y), and, by (c) and (5),
  |Omega(phi_t Y) - e^{-t} A_tr(Y)| = e^{-t} | int_t^infty e^s Theta_x(phi_s Y) ds | <= C |Y|^{-2/beta} e^{-2t}
uniformly for |Y| >= R. Define a(omega) = A_tr(Phi^{-1}(omega)) for |omega| = 1; it is continuous, and the scaling identities give
A_tr(Y) = |Phi(Y)|^{-1/beta} a(Phi(Y)/|Phi(Y)|). Combining these with the bounds on Phi,
  sup_omega | r^{1/beta} Omega(r omega) - a(omega) | <= C r^{-1/beta} + C ||a||_infty r^{-delta} + mod_a(C r^{-delta}),
mod_a the modulus of continuity of a; this is (d). Since Phi is onto R^2 \ {0}, a = 0 would give A_tr = 0 on E, which 4.11(iii)
excludes. The parity of a follows from Omega odd in x.
(8) Rate. (d) gives |Omega| <= C r^{-1/beta}; repeating (4) with delta = 1/beta gives (e).
(9) Sign. By (d), int_{RK} ((sign a0) Omega)_+ dX = R^{2-1/beta} [int rho^{1-1/beta} d rho int ((sign a0) a(theta))_+ d theta +
o(1)], the radial integral over the radii of K and the angular integral over {cos theta >= eps0}; 4.11(i) bounds the left side below by c R^{2-1/beta}, so the
angular integral is positive, and continuity of a gives (f). No pointwise global sign of Omega or of a is implied.
(10) Critical flux. For p = 2 beta >= 4 the function |s|^p is C^1, and by div W = 2 beta and (V),
div(W |Omega|^p) = (2 beta - p)|Omega|^p + p |Omega|^{p-2} Omega Theta_x, whose first term vanishes identically at
p = 2 beta (no division by Omega). By (c) and (e) the remaining integrand is <= C r^{-(p-1)/beta - 2/beta} = C r^{-2-1/beta},
integrable on R^2. On B_R the divergence theorem gives the boundary term
int [beta R + V(R e).e] R^{-2}(|a(theta)|^p + o(1)) R d theta -> beta int |a|^p d theta, by (d) and V = o(R); the volume
integral converges absolutely, and dividing by p gives (g). The right side is positive because a is continuous and not
identically zero. The integrand of (g) is not asserted to be pointwise nonnegative; the identity is a necessary condition
and a numerical consistency check, not an obstruction.
Remarks. (i) The center data and 4.9 enter only through (0) and through the identification of the sharp exponent; without
them (4) gives |DV| <= C(r^{-eta} + r^{-2/beta}) for 0 < eta < min(delta, 2). (ii) By (b), the hypothesis (D) of 4.6 and of
4.11(iii) holds automatically in class A, and the trajectory expansion of 4.6 step (4) holds for every class A profile. (iii)
An independent second proof replaces (3) by a Hoelder estimate for Theta on rescaled annuli, obtained from the
exact transport formula, and a second integration by parts against the Hoelder temperature; it gives the same conclusions.
(iv) The shear example in the scope remark of 4.6 satisfies the kinematic hypotheses but not (T) and (V); the proof above
uses both equations, (T) in (3) and (V) in (4).

4.13 Axis structure (necessary conditions on the invariant axis). Let beta >= 2 and let U, Omega, Theta be smooth
solutions of (T), (V), div U = 0, -curl U = Omega, U = o(|X|), with the B2 parity, Theta(0,y) = 0 and
Theta = a0 x^2 + O(|X|^3), a0 > 0 (after the reflection of 4.8). Put
  b(y) = W_2(0,y),  a(y) = Theta_xx(0,y)/2,  q(y) = Omega_x(0,y),  Lambda = 3 beta + 2,  M = 2 beta + 1
(in 4.13 and in Q2(c), a denotes this axis coefficient, not the angular vorticity tail of 4.12).
(i) Axis system. b a' = (2b' - Lambda) a and b q' + (M - b') q = 2a, with b(0) = 0, b'(0) = Lambda/2, a(0) = a0,
q(0) = 4 a0/beta. Let y_+ in (0, infinity] and y_- in [-infinity, 0) be the zeros of b nearest to 0 above and below. Then
a > 0 and q > 0 on (y_-, y_+), and at a finite endpoint y_*: b'(y_*) <= 0 and a(y_*) = q(y_*) = 0.
(ii) Nondegenerate nearest zero. If y_* is finite and kappa := -b'(y_*) > 0, then, with s = |y - y_*| on the central side,
a = A_* s^n (1 + o(1)) and q = Q_* s^m (1 + o(1)) with A_*, Q_* > 0, n = 2 + Lambda/kappa, m = 1 + M/kappa; smoothness
forces n, m to be integers. Consequently d := 1/kappa and r := beta d are positive integers, n = 2 + 3r + 2d,
m = 1 + 2r + d, and r + d is odd. Writing beta = P/Q in lowest terms, d = Qk and r = Pk with k(P + Q) odd. In particular
there is no finite nondegenerate nearest axis zero when beta is irrational or when P and Q are both odd (for example for
every odd integer beta >= 3). If moreover Omega >= 0 on {x > 0}, then P is even and Q, k are odd.
(iii) Degenerate nearest zero. If b'(y_*) = 0 at a finite endpoint, a and q are flat at y_* (all derivatives vanish).
(iv) Center imbalance (class A). For a class A profile, by oddness of Omega, the center identity 4.1 reads
  (2/pi) int_{x>0} x y (x^2 + y^2)^{-2} Omega(x, y) dX = 1 + beta/2 > 0,
so int_{x>0, y>0} x y (x^2 + y^2)^{-2} [Omega(x, y) - Omega(x, -y)] dX = (pi/2)(1 + beta/2) > 0 (absolutely convergent
in class A): the right-half vorticity is weighted upward. Any vorticity even in y gives c = 0.
(v) Arbitrary axis zeros. On each connected component of {y : b(y) != 0}, a vanishes identically or nowhere. Let y_* be a
zero of b with a != 0 on an adjacent component, and k = b'(y_*). If k > 0 then k = Lambda/2 or k = Lambda; if k < 0 then
Lambda/|k| is a positive integer; if k = 0 then a and q are flat at y_*. A transition between a component on which a = 0
and one on which a != 0 occurs only at a degenerate zero (k = 0), and a degenerate zero cannot border a component on
which a != 0 and the axis flow dy/dt = b(y) moves away from y_*. At a repelling simple zero with k in {Lambda/2, Lambda},
q equals a smooth particular solution plus a multiple of the homogeneous solution |y - y_*|^mu (smooth positive factor),
mu = 1 - M/k in {-beta/(3 beta + 2), (beta + 1)/(3 beta + 2)}; smoothness forces that multiple to vanish on each side.
(vi) Real-analytic axis data. If Theta is real analytic on a neighbourhood of the whole axis, every zero of b is simple
and satisfies (v); if beta is irrational, or beta = P/Q in lowest terms with P and Q odd, then 0 is the only zero of b on
the axis, b has the sign of y, and each open half-axis is a single orbit of the axis flow with backward limit 0.
(vii) Third-order center conditions. a'(0) = 4 b''(0) a0/Lambda and M q'(0) = b''(0)(q(0) + 8 a0/Lambda), with
q(0) = 4 a0/beta. These are necessary for every profile and give an inexpensive test of numerical candidates.
Proof outline. (i) On the axis W_1 = 0 and Omega = 0, so d_y W_1 = 0 and, by curl W = -Omega, d_x W_2 = 0; div W = 2 beta
gives d_x W_1(0,y) = 2 beta - b'(y). Expanding Theta = a x^2 + O(x^4), Omega = q x + O(x^3), W_1 = (2 beta - b') x + O(x^3),
W_2 = b + O(x^2), the x^2 coefficient of (T) and the x coefficient of (V) give the two equations; the center values come from
4.1. On (0, y_+), b > 0 and the first equation is linear homogeneous with nonvanishing leading coefficient, so a keeps the
sign of a0. Parametrizing by the axis flow dy/dt = b(y), dq/dt + (M - b') q = 2a > 0 preserves q > 0 forward in time, and
every point of (0, y_+) is reached from points near 0, where q > 0. At a finite endpoint b'(y_*) <= 0 by the sign of b on the
central side, and evaluating the equations there gives a(y_*) = 0 (since 2b' - Lambda < 0) and then q(y_*) = 0 (since
M - b' > 0). (ii) a'/a = (2b' - Lambda)/b has residue n at y_*, which gives the asymptotics of a; for q, compare with the
positive homogeneous solution H_0 = C s^m (1 + O(s)): d/dt(q/H_0) = 2a/H_0 > 0 and its time integral is finite because
n - m = 1 + (beta + 1)/kappa > 0, so q/H_0 has a finite positive limit. A smooth function with a one-sided asymptotic
C s^gamma, C != 0, has finite vanishing order gamma, so n and m are integers; the identities n - 2 = (3 beta + 2) d and
m - 1 = (2 beta + 1) d give d = 2(n - 2) - 3(m - 1) and r = 2(m - 1) - (n - 2). Parity of r + d: just beyond y_+ the signs
of a and q are (-1)^n and (-1)^m. Since b < 0 just beyond y_+ and b = beta y + o(|y|) is positive near +infinity, there is a
next zero z > y_+ with b < 0 on I = (y_+, z), and a != 0 on I. At z, mu = b'(z) >= 0; mu = 0 is impossible (backward orbits in
I tend to z and d/dt log|a| = 2b' - Lambda <= -Lambda/2 near z, so |a| would be unbounded); for mu > 0, a = C s^N with
N = 2 - Lambda/mu in {0, 1}, and in both cases q/a > 0 near z. Along the axis flow from z to y_+,
d/dt(eps_a q) + (M - b') eps_a q = 2|a| > 0 (eps_a the sign of a on I), so q/a > 0 on I. Hence (-1)^n = (-1)^m, that is
n - m = 1 + r + d is even. The lower endpoint follows by y -> -y. Under Omega >= 0 on {x > 0}, q >= 0 on both sides of y_*,
so m is even. (iii) b = O(z^2), z = y - y_*. If a had finite order j, then b a' = O(z^{j+1}) while (2b' - Lambda) a has a
nonzero z^j term; so a is flat, and then the same argument applied to b q' + (M - b') q = 2a shows that q is flat.
(iv) is 4.1 with the integrand split by the sign of y. (v) Away from zeros of b, a = a(y_0) exp(int (2b' - Lambda)/b), so
a vanishes identically or nowhere on a component. At a simple zero write b = z c(z), c(0) = k; then
(2b' - Lambda)/b = nu/z + (smooth), nu = 2 - Lambda/k, so a = C|z|^nu H(z) with H smooth, H(0) = 1. Smoothness and
non-flatness force nu to be a nonnegative integer: nu in {0, 1} if k > 0 (as nu < 2), nu = 2 + Lambda/|k| if k < 0. At a
degenerate zero, a finite Taylor order j of a is impossible (b a' = O(z^{j+1}) against -Lambda times the order-j term), so
a is flat; then the q equation, with flat forcing, makes q flat. A zero side forces flatness at y_*, incompatible with the
finite order on a nonzero simple side. If the flow leaves a degenerate y_* on a component with a != 0, backward orbits
tend to y_* and d/dt log|a| = 2b' - Lambda <= -Lambda/2 near y_*, so |a| would be unbounded. The q statement: writing
q = H_q u reduces the equation to z u' - mu u = g with g smooth, which has a unique smooth solution since mu < 1, mu != 0;
mu < 0 contradicts continuity and 0 < mu < 1 differentiability. (vi) a is analytic with a(0) = a0 != 0, so it is never flat
and vanishes on no interval; by (v) every zero of b is simple. A nearest zero (above or below) is then nondegenerate, and (ii)
excludes it for the stated beta. b(y) = beta y + o(|y|) makes the axis flow complete with the stated orbits.
(vii) Differentiate both axis equations once at 0, using b(0) = 0 and b'(0) = Lambda/2 (in the second, the two b'q' terms
cancel, leaving b q'' + M q' - b'' q = 2a').
Scope. These are necessary conditions; they do not exclude class A as a whole, only the axis configurations excluded
in (ii), (v) and (vi). A one-equation example shows that the transport equation, positivity and the center data cannot
by themselves exclude the positive-vorticity configuration: for every
beta > 2 and a0 > 0 put p = (beta - 1)/(2 beta), c = 1 + beta/2, L = 3c sqrt(beta)/(4 a0), h = sqrt(beta) L,
S = L^2 + x^2 + (y - h)^2, B = c/[2p h (L^2 + h^2)^{p-1}], Psi = -B x S^p. Then U = (-Psi_y, Psi_x) is smooth, U - U(0) is the
canonical inverse of Omega = 4Bp x S^{p-2}[2L^2 + (p + 1)(x^2 + (y - h)^2)] > 0 on {x > 0}, Psi_xy(0) = 1 + beta/2,
Omega_x(0) = 4 a0/beta, U = O(r^{1-1/beta}), DU = O(r^{-1/beta}), the whole plane is the backward basin of the source at 0,
and the temperature Theta = a0 xi^2 of 4.3(ii) solves (T) on all of R^2 with Theta >= 0, Theta(0,y) = 0 and the jet
a0 x^2. The vorticity has a nonzero r^{-1/beta} tail. Basin and smoothness: W_1/x = beta + 2Bp (y - h) S^{p-1}, and
the maximum of 2Bp |y - h| S^{p-1} over R^2 is c, attained at x = 0, |y - h| = h; hence W_1/x >= beta - c = (beta - 2)/2 > 0,
and likewise b'(y) = beta - 2Bp (y - h) S(0,y)^{p-1} >= beta - c > 0 with b(0) = 0. DU is bounded, so the flow is complete;
backward in time |x| decays exponentially, |W_2(x,y) - b(y)| <= C|x| (Psi_xx is bounded), and y b(y) >= ((beta - 2)/2) y^2
then gives y -> 0, so every backward orbit tends to 0. At 0, DW(0) = diag(lambda1, lambda2) with lambda1 = (beta - 2)/2,
lambda2 = 1 + 3 beta/2; since k lambda1 + j lambda2 > lambda1 for k + j >= 2 there is no resonance, and the smooth local
solution xi = x + O(|X|^2) of W.grad xi = lambda1 xi (unique among such solutions, hence odd in x) extends to a smooth
function on R^2 by xi = e^{lambda1 t} xi o phi_{-t} (t large); Theta = a0 xi^2. But (V) fails already at the x y Taylor
coefficient of R_Omega = W.grad Omega + Omega - Theta_x at 0, which is the second third-order condition of (vii): here
b''(0) = 0 and a'(0) = 0, so (vii) requires q'(0) = 0, while
  q'(0) = 32 a0^2 (3 beta + 5)/(9 beta^2 (beta + 1)(beta + 2)) > 0,
  d_x d_y R_Omega(0) = M q'(0) = 32 a0^2 (2 beta + 1)(3 beta + 5)/(9 beta^2 (beta + 1)(beta + 2))   (784 a0^2/405 at beta = 3).
So any exclusion of this configuration must use (V) beyond the leading center identities. Since the example already
fails a local third-order consequence of (V), it does not rule out an obstruction that uses only higher local or axis
consequences of (V). By 4.28 to 4.31, no such obstruction comes from (V) exactly on any prescribed disk together with
every derivative of (V) at every point of the axis (4.31(b)); under the hypotheses of 4.29(d) (a0 > 0, Theta = a0 xi^2
on its own whole-plane backward basin and the canonical relative inverse), a compactly supported change of the
vorticity of this example cannot make d_x R_Omega(0, .) vanish on the whole axis (4.29(d)), and no configuration that
coincides with this example on an open set is a profile (4.32).

4.14 Published results and their scope for class A. The primary texts were retrieved and the exact statements checked
against class A. None of the theorems audited here has been shown to decide class A; the survey is not exhaustive, the
Ju theorem in (e) remains unchecked, and the Euler abstract check in (e) is not a theorem-level audit.
(a) Chen and Hou (arXiv:2210.07191v4, 16 Aug 2026, Theorem 1 (informal), Theorem 3 (abbreviated, Section 2.2) and
Theorem 4 (full, Section 5.10); computer-assisted part arXiv:2305.05660v3; C^{1,alpha} predecessor arXiv:1910.00173):
stable nearly self-similar blowup in the upper half-plane with the no-flow wall, omega odd and theta even in x, around a
numerically constructed approximate profile; their text states that "Theorem 3 does not imply asymptotically
self-similar blowup".
If the profile were exact and steady, the substitution beta = -c_l/c_omega, (Omega, U, Theta) =
(omega/|c_omega|, u/|c_omega|, theta/|c_omega|^2) would give the half-plane form of (B2-P) with beta = 2.92056000535
(published c_l = 3.00649798, c_omega = -1.02942517, their (2.14) in v4; v3 lists c_l = 3.00649898,
c_omega = -1.02942516 in its (2.23)); the published u_x(0) = -2.532674 reproduces the strain identity
c = 1 + beta/2 of 4.1 to about 1.6e-7, which checks conventions and normalizations (c_omega = c_l/2 + u_x(0),
incompressibility); these numbers do not check the vorticity-gradient identity or the profile equations. Their decay
bounds ((Decay) in Section 2 of v4: vorticity bounded by C<x>^{alpha_1}, alpha_1 in [-0.343, -0.342], close to
-1/beta) are consistent with the slow tail of 4.12 but are properties of an approximate profile. The wall supplies an invariant line on which
the equations for (theta_x, omega) close; in class A the only imposed invariant line is the axis x = 0, on which
Omega = grad Theta = 0. An approximate half-plane profile is not a whole-plane B2 profile.
(b) Abe, Ginsberg and Jeong (arXiv:2410.21765): classification of rotational stationary (-alpha)-homogeneous solutions
with an additional x_2-symmetry; beta = 1/(1 + alpha), so beta >= 2 corresponds to -1 < alpha <= -1/2, where regular
profiles are stated to be open (their Remark 1.4). No class A profile is homogeneous: Theta would be homogeneous of degree
1 - 2/beta < 2 and C^2 at 0, so D^2 Theta(X) = s^{1+2/beta} D^2 Theta(sX) -> 0 as s -> 0, contradicting a0 != 0. Class A
profiles are not stationary physical solutions (theta_xx at the converging material center grows like tau^{-beta-2}), and
a homogeneous final-time state need not solve the stationary equations. No inclusion or exclusion follows.
(c) Chae (Commun. Math. Phys. 273 (2007), Theorem 2.4): excludes self-similar Boussinesq profiles with Theta in two
L^p spaces (p_1 < p_2 <= infinity) and velocity in H^m, m > 2. Both hypotheses fail in class A: Theta is in no L^p with
p < infinity (4.5), and H^m velocity would put Omega in L^2, excluded by 4.9. The conservation mechanism is 4.5 (the
moving center does not matter: ||theta(t)||_p^p = tau^{p(beta - 2) + 2 beta} ||Theta||_p^p).
(d) Chae and Tsai (J. Nonlinear Sci. 25 (2015)): their leading profile equations for the near-wall axisymmetric Euler
ansatz become the half-plane form of (B2-P) after Theta = U^2 and a rotation, but the proof of their Theorem 1 also uses the
next-order Euler identity d_R Psi = 0 of the exact ansatz, which has no B2 counterpart, and the identification requires a
smooth square root of Theta. Their decay hypothesis is decay as the wall-parallel variable tends to infinity, with no
decay in the other variable assumed. The theorem does not apply to class A.
(e) Chae and Shvydkoy (Arch. Ration. Mech. Anal. 2013; abstract checked): Euler, not the forced system. Ju
(J. Math. Anal. Appl. 484 (2020) 123671): the theorem text could not be obtained, so no claim is made about it.
(f) Chen, Huang and Li (arXiv:2604.01868v1, 2 Apr 2026) numerically investigate asymptotically self-similar blowup for
the 1D Hou-Luo model and, in their Section 6, for the 2D Boussinesq equations in the half-plane R x R_+, where the stream
function is recovered with the inverse of the negative Laplacian with zero Dirichlet data on the wall (their (6.1)).
They report regular profiles (Stage 1 and their Scenario 2; "regular" there means bounded and continuous, not a proved
smoothness statement) and locally unbounded profiles (Stage 2); in the 2D Scenario 2 the temperature converges modulo a
time-dependent additive constant. Their rigorous statement, Theorem 2.3 (made precise and proved in their Section 5),
gives explicit singular stationary solutions of the 1D physical and rescaled equations in the approximation sense
specified there. The 2D blowup scenarios are numerical, and their Lemma 6.1 is conditional on convergence of the
rescaled solution and of the scaling parameters. These results are in the boundary setting of (a); they neither
construct a smooth whole-plane profile with the canonical relative inverse (A4) nor prove nonexistence for class A.
(g) Elgindi and Pasqualotto (arXiv:2310.19780v1, Theorem 1.1) prove finite-time singularity formation for some
finite-energy initial velocity and temperature in C^{1,alpha*}(R^2), smooth away from the origin, with alpha* > 0. In
their construction (their Section 2) the vorticity is odd in both coordinates and the temperature is odd in the first
coordinate and even in the second. Their forcing is the derivative of the density in their second coordinate and ours
is Theta_x, so the coordinates are exchanged: the fields Omega(x, y) = -omega(y, x), Theta(x, y) = -rho(y, x) and
U(x, y) = (u_2(y, x), u_1(y, x)) satisfy -curl U = Omega and carry the forcing Theta_x. The temperature is therefore even in x and odd in
y; rescaling about the symmetry center preserves this parity, so any corresponding profile has Theta(x, 0) = 0 for all
x, which is incompatible with Theta(x, 0) = a0 x^2 + O(|x|^3), a0 != 0. The construction supplies no class A profile at
its symmetry center, and it does not establish nonexistence for class A.
(h) Type I regularity criteria. Chae and Wolf (arXiv:1709.02030v3, Theorems 1.2 and 1.4) prove continuation of solutions
of the whole-plane system with data in W^{2,p}(R^2), p > 2, under any one of: (i) limsup (-t) ||grad v||_inf < 2; (ii)
int (-t) ||grad theta||_inf dt < infinity; (iii), (iv) conditions on the Bdot^0_{inf,inf} norm of the vorticity together
with (-t) or (-t)^2 weights on grad theta; or (Theorem 1.4) limsup (-t)^2 log(-1/t) ||grad theta||_inf <= eps. Chae and
Constantin (arXiv:2103.10672v1, Theorem 2.1 global and Theorem 2.2 in a ball B(x0, r); as printed, Theorem 2.2 refers to
system (E) and (2.5) has inner lower limits 0, and the argument below applies equally to the intended local Boussinesq
statement with inner lower limits T - r) give conditions on the pressure Hessian P = (d_i d_j p), the velocity gradient
U = (d_i u_j) and the direction xi = grad^perp theta/|grad^perp theta|, with alpha = xi.U xi, rho = xi.P xi and
zeta = U grad^perp theta/|U grad^perp theta|: (2.3) limsup (T - t)^2 ||[zeta.P xi]_-||_inf < 2, (2.4) limsup (T - t)^2
||[|U xi|^2 - 2 alpha^2 - rho]_+||_inf < 2, or the integral forms (2.1), (2.2) (local forms (2.5)-(2.8)). These are
sufficient conditions for regularity, and every one of them fails for the solution generated by a class A profile
(tau = T - t, u = tau^{beta-1} U(X), so grad u = tau^{-1} DU, grad theta = tau^{-2} grad Theta, and the pressure Hessian
is tau^{-2} D^2 Pi):
  - The data are not in W^{2,p}(R^2): Theta is in no L^p, p < infinity (4.5), and U is unbounded (by Stokes' theorem on
    the annular sectors {R < r < 2R, theta in I}, with I an arc on which the tail a of 4.12(d) has one sign, the
    circulation is at least c R^{2-1/beta} for large R, while the boundary length is O(R)). In the local Theorem 2.2 of
    Chae and Constantin, on a ball of radius rho about the limit point of the center, the qualitative hypotheses do
    hold: by 4.12, |u| = tau^{beta-1} |U(X)| <= C (tau^{beta-1} + rho^{1-1/beta}) on the ball, so int ||u||_{L^inf} dt
    is finite. Only its quantitative conditions matter.
  - At the center DU(0) = diag(-k, k), k = c = 1 + beta/2 >= 2 (4.1), so (-t) ||grad u||_inf >= k >= 2 for every t (for
    the operator, Frobenius or entrywise norm), and condition (i) fails. Since grad Theta is bounded and not 0,
    (-t) ||grad theta||_inf = (-t)^{-1} sup |grad Theta|, so the integral in (ii) diverges and the quantity in
    Theorem 1.4 tends to infinity. The Bdot^0_{inf,inf} seminorm is finite and positive for the bounded, decaying,
    nonzero Omega, and is comparable under all dilations with constants independent of the factor (exactly invariant
    only under dyadic ones), so ||omega(t)|| >= C^{-1} tau^{-1} ||Omega|| and the vorticity integrals in (iii), (iv)
    diverge (the weighted temperature supremum in (iv) is finite, so (iv) fails through its vorticity condition).
  - Differentiating the profile momentum equation (1 - beta) U + W.grad U + grad Pi = (buoyancy) at X = 0, where
    W(0) = 0, DW(0) = beta I + DU(0) and the buoyancy gradient vanishes (grad Theta(0) = 0), gives D^2 Pi(0) =
    -(DU(0) + DU(0)^2) = diag(k - k^2, -k - k^2). Along a ray X = s(1, 1), s -> 0+, Theta = a0 x^2 + O(|X|^3) gives xi
    -> (0, sign a0), so zeta -> xi, zeta.P xi -> -(k + k^2) and |U xi|^2 - 2 alpha^2 - rho -> k^2 - 2k^2 + k + k^2 = k,
    after the factor tau^{-2}. Every ball about the limit point of the center contains, for t near T, points X near 0 on
    this ray, so (the index convention of their gradient array is immaterial, DU(0) being symmetric) the limsups in
    (2.3), (2.7) are at least k(k + 1) >= 6 and those in (2.4), (2.8) at least k >= 2. In the integral forms the norms
    are at least k (T - s)^{-2} for s >= t1 with t1 close to T, so for t > t1 the inner double integral is at least
    k log((T - t1)/(T - t)) - k and the outer integrand at least e^{-k} (T - t1)^k (T - t)^{1-k}, which is not
    integrable at T for k >= 2.

So these criteria neither exclude nor admit class A profiles. They show only that such a profile would give a blowup
with the Type I gradient rates ||grad u||_inf = O(tau^{-1}) and ||grad theta||_inf = O(tau^{-2}) (sup |DU| and
sup |grad Theta| are finite by 4.12), outside the global Sobolev class of these papers, with velocity-gradient constant
at least k >= 2, at or above the threshold 2 of condition (i).

(i) Half-plane Liouville statements. Zhang (arXiv:2306.09515v5, Proposition 2.3) excludes self-similar and
asymptotically self-similar solutions of the upper half-plane Boussinesq system with buoyancy h^2 and the wall condition
V^(2) = 0 on the horizontal base, with H, V^(1) odd and V^(2) even in z^(1), for local C^{2,gamma} profiles with
uniformly bounded gradients and Hessians and exponents (his alpha, beta, written here alpha, b) with 2b = 1 - alpha,
alpha < 0, 0 < b < |alpha|. The B2 scaling gives alpha = 1 - beta, b = beta/2, so the relation is the Boussinesq balance
and the inequality is beta > 2; the exponents are therefore not an obstruction for beta > 2, provided the temperature is
the square of a smooth function with the required parity (in G, Theta = a0 xi^2 by 4.18; for a general class A profile
no such square root is established). Part (i) further assumes signs of both velocity components and of d_1(H^2) in the
open first quadrant, sublinear velocity, bounded angular coefficients in prescribed vorticity and radial velocity tails,
an inequality sup_r W(r, theta_2) > sup_r W(r, theta_1) between radial suprema at two angles, and a nonnegative
vorticity with a strict maximum W(z0) > 0 over the closed sector between these angles and W(z0) > d_1(H^2)(z0); part
(ii) uses instead rectangle, maximum, forcing-dominance and transport-sign conditions. His Remark 2.6 states that
Proposition 2.3 does not rule out all ASSS. The wall, the tangential parities and the sign and maximum hypotheses do not
follow from B2: the B2 invariant line through the center is the vertical axis, and taking it as the wall after a
rotation does not supply the required parities or sign conditions.

(j) Numerical profiles with a wall. Wang et al. (arXiv:2509.14185v1, "Discovery of Unstable Singularities") report
neural-network profiles of the 2D Boussinesq equations with a boundary, with scaling parameters lambda = 1.9205599746927
(stable), 1.3990961221852, 1.2523481636489, 1.1842500861997 (first to third unstable; a fourth, 1.1448833556188, is
stated to be unvalidated) and maximum residuals of order 1e-8 to 1e-7 (grid maxima of factored residual functions; their
instability spectra are restricted to the imposed symmetry class). Their ansatz y = (1 - t)^{-(1+lambda)} x gives
beta = 1 + lambda, that is beta = 2.92056, 2.39910, 2.25235, 2.18425; their identity lambda = -3 - 2 d_{y1}U_1(0, 0) is
the center identity c = 1 + beta/2 of 4.1, and their vorticity tail |y|^{-1/(1+lambda)} is the exponent 1/beta of
4.12. Earlier, Wang, Lai, Gomez-Serrano and Buckmaster (arXiv:2201.06780v3) computed a neural-network profile on the
half plane x_2 >= 0 with u_2(x_1, 0) = 0, U_1 odd and U_2 even in y_1. Their ansatz u = (1 - t)^lambda U(y),
y = x/(1 - t)^{1+lambda}, gives beta = 1 + lambda; they report lambda = 1.917 +- 0.002, hence beta = 2.917 +- 0.002 (a
reported numerical spread, not an enclosure), and describe the equation residues as about five orders of magnitude
smaller than the solution. These are numerical boundary profiles without certified error control; they are not shown
to extend to whole-plane B2 profiles with the canonical inverse (A4), and they establish neither existence nor
nonexistence in class A.

4.15 Class reduction: sublinear velocity with polynomially bounded vorticity. Let beta >= 2 and let U, Omega, Theta be
smooth on R^2 with div U = 0, -curl U = Omega, (T), (V) and U(X) = o(|X|) as |X| -> infinity (uniformly:
sup_{|X| = r} |U|/r -> 0). No bound on Theta, no derivative bound and no integral representation of U is assumed.
Suppose one of
  (i) Omega(X) -> 0 as |X| -> infinity (no rate);  (ii) Omega is bounded;
  (iii) |Omega(X)| <= C(1+|X|)^k for some finite k >= 0;  (iv) beta = 2 (no assumption on Omega).
Then for every eta > 0, |Omega(X)| <= C_eta (1+|X|)^{-1/(beta+eta)}; |Theta(X)| <= C(1+|X|)^{p_Theta} for some p_Theta < 1 (Theta is
bounded if beta = 2); and U_rel = U - U(0) is the canonical relative integral of (A4), absolutely convergent. Hence a
smooth profile with the B2 parity, Theta(0,y) = 0, Theta = a0 x^2 + O(|X|^3), a0 != 0, U = o(|X|) and bounded vorticity
belongs to class A, and so does every such profile with U = o(|X|) and polynomially bounded vorticity, and every such
profile with U = o(|X|) at beta = 2, with no condition on the vorticity. Class A therefore coincides with the class of
smooth B2 profiles with sublinear velocity and polynomially bounded vorticity, and all of 4.1-4.13 and 4.16 apply to it.
Proof outline. Write V = U_rel, W = beta X + V, r = |X|, phi_t the flow of W, q = grad Theta.
(1) Escape. Fix 0 < eps < 1 and R with |V| <= eps |X| outside B_R. Every exterior point is phi_t Z for a unique Z on the
circle S_R and t >= 0, with R e^{(beta-eps)t} <= |phi_t Z| <= R e^{(beta+eps)t}, and w(t) = |W(phi_t Z)| satisfies
C^{-1} e^{(beta-eps)(t-s)} <= w(t)/w(s) <= C e^{(beta+eps)(t-s)} for t >= s >= 0, with C independent of Z. By (T),
Theta(phi_t Z) = e^{(beta-2)t} Theta(Z), so |Theta| <= C r^{p_Theta} with p_Theta = (beta-2)/(beta-eps) < 1.
(2) Moving frame. Along an exterior orbit put e = W/w, n = J_+ e, and write DV = [[alpha, b], [c, -alpha]] in the basis
(e, n) (DV is trace free; b - c = Omega is its antisymmetric part). Then w'/w = beta + alpha and e' = c n. Differentiating
(T) gives q' = -(2I + DV^T) q along orbits, and the components q_par = q.e, q_perp = q.n satisfy exactly
  q_par' = -(2 + alpha) q_par,   q_perp' = (-2 + alpha) q_perp - (b + c) q_par
(q_par = (beta-2) Theta/w by (T)). Since int_s^t alpha = log(w(t)/w(s)) - beta(t - s), (1) gives
  |q(phi_t Z)| <= C e^{-(2-eps)t} [1 + int_0^t |DV(phi_sigma Z)| d sigma].
(3) beta = 2. Then q_par = 0, so q_perp(t) = q_perp(0) e^{-4t} w(t)/w(0) and |q(phi_t Z)| <= C e^{-(2-eps)t}, with no bound on DV.
(4) Local strain bound in cases (i)-(iii). With M = max(1, sup_{B(X,r/2)} |Omega|) and A = sup_{B(X,r/4)} |Theta|, for
large |X|: |DV(X)| <= C [M + A/r] log(2 + M), with C independent of X. This is proved as in 4.12 steps (1)-(4), but
locally: V is a localized Biot-Savart integral plus a harmonic field bounded by C r(1 + M) on B(X, 3r/8); the localized
part is log-Lipschitz with constant C M, and |V(P) - V(Q)| <= C r on the ball; using the smaller of the two moduli,
|V(P) - V(Q)| <= C min{r, M rho [1 + log(r/rho)]} for rho = |P - Q| <= r/4, and
int_0^{cr} min{r, M rho [1 + log(r/rho)]} rho^{-1} d rho <= C r log(2 + M) (split at rho = r/M), the directional
commutator identity of 4.12 step (2) costs only a factor log(2 + M) (the delta terms of the kernel derivative
cancel in the commutator); the forcing Theta_x is handled through the temperature potential of 4.12 step (3), with
W.grad(chi Theta) bounded by C A by (T), and A <= C r^{p_Theta} by (1). Only sup bounds on Omega and Theta enter. Since A/r -> 0,
DV is bounded in cases (i), (ii), and |DV| <= C r^k (1 + log r) in case (iii).
(5) Decay. In cases (i), (ii), by (2)-(4), |q(phi_t Z)| <= C(1 + t) e^{-(2-eps)t}, and integrating (V),
e^t Omega(phi_t Z) = Omega(Z) + int_0^t e^sigma Theta_x(phi_sigma Z) d sigma gives |Omega(phi_t Z)| <= C e^{-t}
<= C' |phi_t Z|^{-1/(beta+eps)}. In case (iv) the bound of (3) and the same integration of (V) give
|Omega(phi_t Z)| <= C e^{-t}. In case (iii), (4) gives |DV(phi_s Z)| <= C(1 + s) e^{k(beta+eps)s}, hence
|q(phi_t Z)| <= C(1 + t^2) e^{alpha t} with alpha = k(beta + eps) - 2 + eps, and the same integration gives
|Omega(phi_t Z)| <= C(1 + t^3) e^{max(-1, alpha) t}. Converting with (1) (using R e^{(beta-eps)t} <= r for a nonnegative
exponent and r <= R e^{(beta+eps)t} for a negative one) gives |Omega| <= C r^{k'} with k' arbitrarily close to
max(-1/beta, k - 2/beta); choosing the loss at most 1/(2 beta) gives k' <= max(0, k - 1/beta). After at most
ceil(beta k) such steps, each with its own eps and constants and a compact core absorbed into C, Omega is bounded and
case (ii) applies.
(6) Canonical inverse. With |Omega| <= C(1+r)^{-delta}, the integral B(X) = int [K(X-Y) - K(-Y)] Omega(Y) dY converges
absolutely, and splitting |Y| < r/2, r/2 <= |Y| <= 2r, |Y| > 2r gives |B(X)| <= C(1 + r^{1-delta}). B is divergence free
with -curl B = Omega, so V - B is entire harmonic, sublinear and zero at 0, hence zero.
Remarks. (a) The reduction uses (T) and (V) along the flow; it is not a statement about arbitrary vector fields. (b) Case
(iv) is the reason the whole beta = 2 branch of the problem lies in class A: there the temperature gradient decays along
every escaping orbit at the exact rate e^{-4t} w(t)/w(0), whatever the vorticity does. (c) Only the relative velocity
V = U - U(0) is identified with the canonical integral; U(0) is a free constant (the observer gauge of (A5)), so the
statement does not assert U = B. (d) Sublinearity is used uniformly outside large balls (a common escape circle); raywise
sublinearity would not suffice. (e) The endpoint exponent delta = 1/beta is not obtained here; it is 4.12(d).

4.16 Second far-field terms. Let (Theta, Omega, U) be a class A profile, s = 1/beta, m = 1 - 2s, e = (cos theta, sin theta),
e_perp = (-sin theta, cos theta), and let a and h = A be the angular limits of 4.12(d) and 4.10. Then a and h are smooth
on the circle. Put omega0 = r^{-s} a(theta), theta0 = r^m h(theta), let u0 be the canonical relative inverse of omega0
(homogeneous of degree 1 - s), u0r = u0(e).e and u0t = u0(e).e_perp, and
  b = u0t a' - s u0r a - d_x theta0(e),   d = u0t h' + m u0r h.
Then, uniformly in theta and with remainders that are o in every C^j(S^1) (angular derivatives),
  Omega(r e) = r^{-s} a + r^{-2s} b + o(r^{-2s}),   Theta(r e) = r^m h + r^{m-s} d + o(r^{m-s}).
These are necessary asymptotics of a hypothetical profile; they neither exclude nor construct one.
Proof outline. (1) Physical rescaling. For t = -tau, 0 < tau <= 1, u(t,z) = tau^{beta-1} V(tau^{-beta} z),
omega(t,z) = tau^{-1} Omega(tau^{-beta} z), theta(t,z) = tau^{beta-2} Theta(tau^{-beta} z) solve the physical system
(observer with the material center at rest, (A5)). By 4.12(d), 4.10 and dominated convergence in the relative
Biot-Savart integral (majorant |y|^{-s}, integrable against the kernel difference since 0 < s < 1), (u, omega, theta)
converges, as tau -> 0, locally uniformly on R^2 \ {0} to the homogeneous state (u0, omega0, theta0); on circles,
r^s Omega(r e) = omega(-tau, e) and r^{-m} Theta(r e) = theta(-tau, e) with tau = r^{-s}.
(2) Local regularity up to and including t = 0. On every ball whose closure avoids the origin, 4.12(c)-(e) and 4.10,
rescaled, bound omega, Du, theta and grad theta uniformly for 0 < tau <= 1. Let k >= 2 and suppose that on every such
ball D^{j-1} omega and D^j theta are bounded in every finite L^q, uniformly in tau, for j < k. Fix a ball B(z*, 2 rho0)
of this kind, a nonincreasing smooth eta with eta = 1 on [0, rho0/2] and eta = 0 on [rho0, infinity), M_u >= sup |u| on
the ball, a start time t1 in (-1, 0) with M_u |t1| < rho0/4, and the shrinking cutoff chi = eta(|z - z*| + M_u (t - t1)), so
that (d_t + u.grad) chi <= 0 and chi = 1 on B(z*, rho0/4) for t1 <= t <= 0. Fix q > 2 (lower exponents then follow by
Hoelder's inequality on the bounded ball). Whole-plane div-curl estimates applied to chi u give
  (E1)  ||chi D^k u||_q <= C ||chi D^{k-1} omega||_q + C0,
since every cutoff error contains at most k - 1 derivatives of u or k - 2 derivatives of omega. A = D^{k-1} omega and
B = D^k theta satisfy transport equations whose right sides are D^{k-1} d_x theta and commutator sums; the intermediate
products are bounded by the preceding L^{2q} bounds (at k = 2 these sums are empty), and the highest term
chi D^k u grad theta is controlled by (E1). For E = ||chi A||_q^q + ||chi B||_q^q this gives E' <= C(E + 1), so E stays
bounded up to and including t = 0. The induction bounds every derivative uniformly on compact subsets of R^2 \ {0};
by compactness and uniqueness of the known locally uniform limit, the convergence holds in every C^j on compact subsets
of R^2 \ {0}, and the limits, hence a and h, are smooth. No Biot-Savart representation is used in this step. The case
k = 2 also follows independently from the local regularity theorem for the generalized Boussinesq system of Chae and
Wolf (arXiv:1712.07434v6, Theorem 2.1, printed page 7), applied after the rescaling z = z* + R y with coefficients
a = 1, b = (1/R, 0), d = 1, e = 0; its hypotheses were checked against the primary text, and it gives strong convergence
in W^{2,q} for every finite q.
(3) Second terms. Integrating the physical equations from t = -tau to 0 and using the C^j convergence,
omega(-tau) = omega0 + tau (u0.grad omega0 - d_x theta0) + o(tau) and theta(-tau) = theta0 + tau u0.grad theta0 + o(tau);
on the unit circle u0.grad omega0 = u0t a' - s u0r a and u0.grad theta0 = u0t h' + m u0r h. With tau = r^{-s} this is the
claim. A constant term in the far-field expansion of V scales like tau^{beta-1} -> 0 and does not affect b or d.
Remark. The formula agrees with the formal next order obtained by expanding (T) and (V) in r: the corrections
r^{-2s} b and r^{m-s} d are the unique ones of these degrees forced by the advection u0.grad of the leading terms and by
the forcing d_x theta0. An expansion to all orders is not asserted.
Velocity terms. Let f be the unique smooth periodic solution of -(f'' + (2 - s)^2 f) = a (no resonance, since
3/2 <= 2 - s < 2); then u0(r e) = r^{1-s}[-f'(theta) e + (2 - s) f(theta) e_perp].
(a) If beta > 2, let g be the unique smooth periodic solution of -(g'' + (2 - 2s)^2 g) = b (no resonance, since
1 < 2 - 2s < 2) and u1(r e) = r^{1-2s}[-g' e + (2 - 2s) g e_perp], the canonical relative inverse of r^{-2s} b. Then
  V(r e) = u0(r e) + u1(r e) + o(r^{1-2s})   in every C^j(S^1).
(b) If beta = 2 (s = 1/2), the source r^{-1} b is resonant in its first harmonic. The sine part vanishes by the
reflection (b(pi - theta) = -b(theta)); put b1 = (1/pi) int_0^{2 pi} b cos theta d theta and let g be the smooth periodic
solution of -(g'' + g) = b - b1 cos theta orthogonal to cos theta and sin theta. Then there is a unique constant C,
determined by the whole profile through the canonical inverse, such that
  V(r e) = u0(r e) - (b1/2) log r (0, 1) + B_b(theta) + C (0, 1) + O(r^{-1/2} log r)   in every C^j(S^1),
  B_b = -g' e + g e_perp + (b1/2)(cos theta sin theta, -cos^2 theta).
The logarithm is present exactly when b1 != 0; that b1 != 0 is not asserted. At beta = 2 the remainders of the scalar
expansions above improve to O(r^{-3/2} log r) for Omega and O(r^{-1} log r) for Theta, in every C^j(S^1). Since the
angular mean of B_b is -(b1/4)(0, 1), the constant is recovered from a computed velocity as
  C = lim_{r -> infinity} [ mean over theta of (V - u0 + (b1/2) log r (0, 1))_2 ] + b1/4.
Proof outline. With the rescaled fields of step (1), the bounds of 4.12 and of the expansions above give globally
|omega_tau - omega0| <= C min(rho^{-s}, tau rho^{-2s}), rho = |z|, and u_tau = K_rel omega_tau exactly. (a) For beta > 2,
2s < 1, so rho^{-2s} is integrable against the relative kernel at 0 and at infinity; dominated convergence gives
(u_tau - u0)/tau -> K_rel(r^{-2s} b) uniformly on compact annuli, and the interior estimate for
Delta v = (d_2 omega, -d_1 omega) upgrades this to every C^j; tau = r^{-s} gives (a). (b) For beta = 2 the only borderline
contribution is int_0^c min(rho^{-1/2}, tau rho^{-1}) d rho <= C tau(1 + |log tau|) near the origin, so
||u_tau - u0||_{C^j(K)} <= C tau(1 + |log tau|); inserting this into the rescaled transport equations and integrating in
tau gives the improved scalar remainders. For the velocity, with a smooth radial cutoff chi (0 for r <= 1, 1 for r >= 2)
put eta = Omega - omega0 - chi r^{-1} b = O(r^{-3/2} log r); its ordinary Biot-Savart integral U_eta converges absolutely and is
O(r^{-1/2} log r) on large circles (split |Y| < r/2, r/2 <= |Y| <= 2r, |Y| > 2r), so K_rel eta = -U_eta(0) + O(r^{-1/2} log r). The source chi r^{-1} b is inverted mode by mode: the harmonics of order >=
2 give the stream r g(theta) up to O(r^{-2}) velocity corrections, and the first cosine harmonic has the relative stream
coefficient P1(r) = (b1/2)[r^{-1} int_0^r rho chi d rho - r int_0^r chi/rho d rho] = -(b1/2) r log r + b1(1/4 - L_chi/2) r + O(1/r),
L_chi = lim_{R -> infinity} (int_0^R chi/rho d rho - log R); the stream -(b1/2) x log r has velocity
(b1/2)(cos theta sin theta, -log r - cos^2 theta). Hence C = b1(1/4 - L_chi/2) - [U_eta(0)]_2, which is absolutely
convergent and independent of chi (a change of chi changes both terms by -(b1/2) int d(chi)/rho d rho).

4.17 Divided fields, decay with the axis factor and quadratic identities (class A, beta > 2). Let (Theta, Omega, U) be a
class A profile with beta > 2, put d = 1/beta, V = U_rel, W = beta X + V, D = {x > 0}, and define the smooth quotients
(smooth by the parity and the axis vanishing)
  P = Theta/x^2,   Q = Omega/x,   v = V_1/x,   S = Theta_x/x = 2P + x P_x.
None of them is assumed to have a sign. Then:
  (a) |P| + |S| <= C(1 + r)^{-1-2d},  |Q| <= C(1 + r)^{-1-d},  |v| <= C(1 + r)^{-d}; consequently the angular limits
      of 4.10 and 4.12(d) satisfy |A(theta)| <= C cos^2 theta and |a(theta)| <= C |cos theta|;
  (b) with every bulk integral absolutely convergent,
        int_D (1 + v) P^2 dX = 0,      int_D (1 + v) Q^2 dX = int_D Q S dX,
        int_D v |P|^k dX = [beta/k - (beta + 2)/2] int_D |P|^k dX   for every real k > 2 beta/(beta + 2);
  (c) (critical horizontal weight) with alpha = 2 - d, both sides converging absolutely,
        beta int_{-pi/2}^{pi/2} a(theta) cos^{-alpha} theta d theta = alpha int_D x^{1-alpha} (P - v Q) dX.
Since P(0) = a0 != 0 and v(0) = -(beta + 2)/2 < -1, the first identity in (b) forces v > -1 at some point where P != 0.
These are necessary identities; v is a signed nonlocal kernel and P, Q, S may change sign, so none of them has a sign
that excludes a profile.
Proof outline. (a) Fix rho with X.W >= (beta/2)|X|^2 for |X| >= rho and let tau(X) be the backward hitting time of the
circle |X| = rho, so e^{beta tau} is comparable to r. By 4.12(e), |DV| <= C r^{-d}, which is integrable along escaping
orbits, so the backward flow from X to the hitting point X_tau has |D phi_{-t}| <= C e^{-beta t}, and the horizontal
coordinate obeys |x_tau| <= C |x| e^{-beta tau} (W_1 = x(beta + v) with v bounded). On the circle, smoothness and parity
give |Theta| <= C x^2, |grad Theta| <= C|x|, |Omega| <= C|x|. Transport for the finite time tau,
Theta(X) = e^{(beta - 2) tau} Theta(X_tau), and its derivative give |Theta| <= C x^2 r^{-1-2d} and
|grad Theta| <= C |x| r^{-1-2d}; the finite-time vorticity formula Omega(X) = e^{-tau} Omega(X_tau) +
int_0^tau e^{-t} Theta_x(phi_{-t} X) dt gives |Omega| <= C |x| r^{-1-d}. The bound on v follows from V_1(0, y) = 0
and |DV| <= C(1 + r)^{-d} by the mean value theorem on horizontal segments (if |x| < r/2, the whole segment lies at
radius >= |y| > r/2). Every bound carries the axis factor, so division by x or x^2 keeps the decay. No sign of Theta
is used. (b) From (T), W.grad P = -(beta + 2 + 2v) P, so
div(W |P|^k) = [2 beta - k(beta + 2) - 2kv] |P|^k (|s|^k is C^1 for k > 1, and the range of k exceeds 1 for beta > 2);
W_1 = 0 on the axis, and the flux through the semicircle of radius R is O(R^{2 - k(1 + 2d)}) -> 0 for k > 2 beta/(beta + 2);
k = 2 gives the first identity. From (V), W.grad Q = S - (1 + beta + v) Q, so div(W Q^2) = 2 Q S - 2(1 + v) Q^2, with
semicircle flux O(R^{-2d}). (c) div(W Omega x^{-alpha}) = x^{-alpha}(Theta_x - alpha v Omega), because
2 beta - 1 - alpha beta = 0. Integrate over the cut half disks {x > eps, |X| < R}: the flux through x = eps is
O(eps^d); the flux through the semicircle tends to beta int a cos^{-alpha} by dominated convergence with the bound
|r^d Omega| <= C cos theta from (a) (uniform convergence alone does not suffice, since cos^{-alpha} is not integrable);
x^{-alpha} Theta_x is replaced by alpha x^{1-alpha} P by the divergence theorem for Theta x^{-alpha} e_1 on the same domains,
whose boundary terms are O(eps^d) and O(R^{-d}) by |Theta| <= C R^{1-2d} cos^2 theta.

4.18 The global-source subclass. Let G be the set of class A profiles with beta > 2 for which W has no zero other than
the center (a0 > 0 after the reflection of 4.8). For profiles in G:
  (a) the set K of 4.3 is {0}, the basin of the center is R^2, every backward orbit tends to 0, Theta = a0 xi^2 >= 0 on
      R^2 with xi as in 4.3(ii), and Theta_xx(0, y) > 0, Omega_x(0, y) > 0 for every y;
  (b) there are smooth global coordinates (xi, eta), xi odd and eta even in x, with det D(xi, eta) = 1, in which
        W = lambda1 xi d_xi + (lambda2 eta + kappa xi^k) d_eta,   lambda1 = (beta - 2)/2, lambda2 = 1 + 3 beta/2,
      where kappa = 0 unless lambda2 = k lambda1 for an even integer k;
  (c) no profile in G has a vorticity of the form Omega = x g(x^2 + (y - y0)^2) with g smooth and y0 real;
  (d) if Omega(s, y0 + z) = Omega(s, y0 - z) for all s, z (reflection about a horizontal line y = y0), then
      b(y0) != 0 and b(y0)^2 q''(y0) = 4(beta + 1)^2 (beta + 2) q(y0)/(beta - 1) > 0, with b, q as in 4.13; in particular
      q has a strict local minimum at y0, and Omega(s, .) cannot have a maximum at y = y0 for every s > 0.
Proof outline. (a) X.W >= (beta/2)|X|^2 outside a large ball and X.W >= (lambda1/2)|X|^2 on a small ball about 0, so K
is compact and invariant and 0 lies in no omega-limit set of a point other than 0. A periodic orbit would bound an open
invariant domain, impossible since div W = 2 beta > 0 makes its area grow. Since 0 is the only zero of W, the
Poincare-Bendixson theorem leaves K = {0}, and every alpha-limit set, being a nonempty compact invariant subset of K, is
{0}. Then 4.3(ii) gives Theta = a0 xi^2 on R^2, and 4.13(i) with y_+ = +infinity, y_- = -infinity gives the axis
positivity. (b) Near 0 the function u = x (P/a0)^{1/2} (P as in 4.17) is smooth, odd in x, has u_x > 0, and solves
W.grad u = lambda1 u. With x = chi(u, y) the inverse in the first variable, the area coordinate
eta0 = int_0^y chi_u(u, s) ds satisfies det D(u, eta0) = 1 and W.grad eta0 = lambda2 eta0 + f(u) with f even in u.
The scalar equation lambda1 u F' - lambda2 F = -f(u) has a smooth solution except at the resonance u^k, lambda2 = k lambda1,
so the even shear eta = eta0 + F(u) leaves at most the term kappa u^k; reflection forces kappa((-1)^k - 1) = 0, so
kappa = 0 for odd k. These local coordinates Xi are extended to R^2 by Xi(Y) = F_t(Xi(phi_{-t} Y)) for t large, F_t the
flow of the model field: by (a) every backward orbit enters the local domain, the value does not depend on t, local
injectivity gives global injectivity, the conjugacy gives det D Xi = 1, and the flow preserves the axis and the
parities; transport then gives Theta = a0 xi^2 with xi the first coordinate. The normalized linearization
is not unique: eta -> eta + c |xi|^{lambda2/lambda1} is again a C^1 conjugacy tangent to the identity, so the parity of
the coordinates is obtained from this construction and not from a uniqueness argument. (d) The reflection makes
V_2(0, y0 + z) - V_2(0, y0) even in z (an absolutely convergent paired integral, since the subtracted kernel difference is
O(|Y|^{-2}) against |Omega| <= C |Y|^{-1/beta}). Hence b'(y0) = beta, b'''(y0) = 0 and q'(y0) = q'''(y0) = 0.
Differentiating the axis system of 4.13(i) up to twice at y0 gives
  b^2 q'' - b b'' q = -(beta + 1)(beta + 2) q   and   (5 beta + 3) b^2 q'' = 4(beta + 1) b b'' q   at y0,
whose difference eliminates b b'' q and gives the identity, since 4(beta + 1) - (5 beta + 3) = 1 - beta. As q(y0) > 0 by
(a), b(y0) != 0 and q''(y0) > 0. If Omega(s, .) had a maximum at y0 for every s > 0, then q = lim Omega(s, .)/s would
have a maximum there. (c) Such an Omega has the horizontal reflection of (d). With S = x^2 + (y - y0)^2 and F
solving 4(2F' + S F'') = g one has Lap(x F(S)) = 4x(2F' + S F'') = Omega, so the relative stream function is
Psi_rel = -x F(S) + F(y0^2) x, with velocity V_1 = 2x(y - y0)F'(S), V_2 = F(y0^2) - F(S) - 2x^2 F'(S); here F'(S) = (1/4) int_0^1 u g(S u) du, and g > 0 because
q(y) = g((y - y0)^2) > 0 by (a); the resulting velocity is sublinear and equals V by the Liouville argument for harmonic
fields. On the axis b(y) = beta y + F(y0^2) - F((y - y0)^2). The center strain c = 2 y0 F'(y0^2) = 1 + beta/2 > 0 gives
y0 > 0, so b(y0) > 0, while b''(y0) = -2F'(0) < 0. This contradicts b b'' q > 0 at y0, which follows from the second
displayed relation in (d) and q''(y0) > 0.
Scope. (c) and (d) are restricted exclusions (shape hypotheses on Omega); (b), 4.17 and the axis conditions are necessary
conditions. G itself is not excluded. The explicit example in the scope remark of 4.13 has a global source at the
center and satisfies (T), parity, the canonical inverse and all center data, and violates only (V); so any exclusion of
G must use (V) beyond the leading center identities.
4.19 Zeros of W off the center (class A, beta > 2). Let (Theta, Omega, U) be a class A profile with beta > 2, a0 > 0
(after the reflection of 4.8), V = U_rel = U - U(0), W = beta X + V, Z = {W = 0}, K as in 4.3, c = beta - 2, and b, q and a_ax (the axis
coefficient a) the axis functions of 4.13. A zero z is a hyperbolic source, a hyperbolic saddle or degenerate according to the signs of
the eigenvalues of DW(z); the basin of a source z is the open set of points whose backward orbit tends to z.
  (a) Linear types. At every zero z, DW(z)^T grad Theta(z) = c grad Theta(z) and Omega(z) = Theta_x(z). If
      grad Theta(z) != 0, z is a hyperbolic source with eigenvalues c and beta + 2. Otherwise DW(z) is symmetric, so every
      zero has real eigenvalues, with sum 2 beta: a hyperbolic source, a hyperbolic saddle, or a degenerate zero with
      eigenvalues 0 and 2 beta. At a degenerate zero Theta and Omega are flat (every derivative vanishes).
  (b) Limit sets. Every backward orbit, and every forward orbit in K, converges to a single zero. Hence K is Z together
      with the orbits that connect two zeros; K is connected and has measure zero.
  (c) Vanishing sets. Theta = grad Theta = Omega = 0 on the unstable manifold of every hyperbolic saddle, and on the
      boundary of the basin of every hyperbolic source, in particular on the boundary of the basin R(0) of the center
      (no hypothesis on the other zeros).
  (d) Axis reduction. If b has no zero other than 0, then 0 is the only zero of W, so the profile belongs to G (4.18).
      In particular the center together with one mirror pair of off-axis zeros is impossible.
  (e) Consequences. If beta is irrational, or beta = P/Q in lowest terms with P and Q both odd (for example every odd
      integer beta >= 3), then on each half-axis the nearest zero of b, if any, is degenerate and a_ax and q are flat
      there (4.13(ii)-(iii)); so either the profile belongs to G or W has a degenerate zero on the axis. For such beta, if
      every zero of W on the axis is nondegenerate (in particular if every zero of W is hyperbolic), or if Theta is real
      analytic on a neighbourhood of the axis (4.13(vi)), the profile belongs to G.
  (f) Hyperbolic configurations. If every zero of W is hyperbolic, Z is finite, the numbers N_s of sources and N_h of
      saddles satisfy N_s - N_h = 1, K is a finite tree, Theta is not flat at any zero, and Theta is not identically zero
      on the basin of any source.
Proof outline. (a) Differentiate (T) at z and evaluate (V) at z. If grad Theta(z) != 0 it is an eigenvector of DW(z)^T
with eigenvalue c, and the trace gives the other eigenvalue 2 beta - c. If grad Theta(z) = 0, then Omega(z) = 0, so
curl W(z) = 0 and DW(z) is symmetric. At a degenerate zero, in eigencoordinates the degree-N part of (T) for the first
nonzero Taylor term P_N reads (DW(z) Y).grad P_N = c P_N, with monomial eigenvalues 2 j beta (0 <= j <= N), none equal to
c in (0, beta); so all Taylor terms of Theta vanish, and the degree-N part of (V) has monomial eigenvalues 2 j beta + 1 > 0.
(b) Backward semiorbits are bounded; by 4.7 step (1) of (v)-(vii) compact limit sets contain no regular point, so they are
connected subsets of Z. A connected limit set of equilibria with more than one point contains an arc of a C^1 curve of
equilibria (DW != 0 since its trace is 2 beta); near an interior point of that arc, in graph coordinates u = x - h(y),
v = y of the arc (after a rotation), integral factorization in u gives du/dt = u A(u, v), dv/dt = u B(u, v) with A, B
continuous and A(0, v) = tr DW = 2 beta > 0, so backward orbits entering a neighbourhood converge to one point, and a forward orbit
returning infinitely often would be stationary. K is the nested intersection of the disks phi_{-t}(B_R), and Liouville
gives |K| = 0. (c) Put Q = J_+ grad Theta = (-Theta_y, Theta_x). From L_W(dTheta) = c dTheta and L_W(area) = 2 beta area one gets
[W, Q] = -(beta + 2) Q, so D phi_t(p) Q(p) = e^{(beta+2)t} Q(phi_t p). On a saddle unstable curve Theta = C |rho|^{c/mu}
in a linearizing parameter rho, and c/mu < 1 with smoothness forces C = 0; then Q = fW with f(phi_t p) = e^{-(beta+2)t} f(p),
bounded backward since |Q| <= C|X - z| and |W| >= C^{-1}|X - z| on the local curve, so f = 0; and
Omega(p) = int_{-infinity}^0 e^t Theta_x(phi_t p) dt = 0. On a basin boundary: if Theta(p) != 0, then
det(W, Q) = c Theta(p) != 0, the Q-transversal through p contains basin points q, and its backward images have length at
most e^{-(beta+2)t} |s| sup|Q|, so p converges backward to the same source, a contradiction. If Theta = 0 but Q(p) != 0 at a
regular boundary point, then W(phi_{-t} p) = f(p)^{-1} e^{-(beta+2)t} Q(phi_{-t} p) is integrable, the backward limit z
cannot have Q(z) = 0 (the distance S(T) to z would satisfy S(T) <= C e^{-(beta+2)T} S(T)), and Q(z) != 0 makes z a source
whose open basin contains p, a contradiction. Omega = 0 follows from the same integral formula. (d) Since Theta(0, y) = 0 and
Theta is even in x, Taylor's integral formula in x gives Theta = x^2 H with H(x, y) = int_0^1 (1 - s) Theta_xx(sx, y) ds
continuous and H(0) = a0 > 0; so on a small circle C_0 about 0 off-axis points have Theta > 0, they are not in K (Theta = 0 on K by 4.3(i)) and escape; the
two axis points escape because b has no other zero. By compactness there is T with phi_T(C_0) outside a disk B_R
containing Z; phi_T(D_0) is a disk containing 0 whose boundary misses the connected set B_R, so it contains B_R, hence
every zero; zeros are fixed points, so they lie in D_0, where 0 is the only zero. (e) 4.13(ii) excludes a nondegenerate
nearest axis zero for these beta; 4.13(iii) gives flatness at a degenerate one; then apply (d) (the center is a
hyperbolic source, so a nearest axis zero exists whenever b has another zero on that half-axis). (f) Hyperbolic zeros are
isolated and Z is compact. The index of W on a large circle is 1 (W is homotopic to beta X there), sources have index 1 and
saddles -1. K = Z together with the stable branches of saddles; a cycle in this graph would be an invariant Jordan curve
whose interior area grows by div W = 2 beta, so the graph is a forest with N_s + N_h vertices and 2 N_h edges, connected
by (b), so a tree. Along a connecting orbit, which converges exponentially at both ends, the jet vector of Theta of order
N obeys a linear system with bounded coefficients, so flatness at one end (decay faster than every exponential)
propagates to every point of the orbit and to the other end; flatness at any zero would reach 0, where Theta_xx = 2 a0.
A source with Theta = 0 on its basin would be a flat zero.
Scope. Necessary conditions and restricted exclusions only. For beta = P/Q with P + Q odd (for example beta = 4) the
necessary arithmetic resonance conditions of (e) do not rule out additional axis zeros (exact integer tuples satisfying
them exist, for example at beta = 4 and beta = 8/3); these arguments neither construct such a profile nor show that such a
configuration satisfies the global conditions. Degenerate zeros, at which a dead basin cannot be excluded by these
arguments, are not excluded for any beta.
4.20 Critical points of Theta on escaping orbits under a weak vorticity sign (class A, beta >= 2). Let (Theta, Omega, U)
be a class A profile with beta >= 2, V = U_rel = U - U(0), W = beta X + V, c = beta - 2, and assume Omega >= 0 on {x > 0}, or
Omega <= 0 there (zeros allowed; since Omega_x(0) = 4 a0/beta, the sign is necessarily that of a0). Let C_* be a complete
orbit of W contained in {x > 0} whose forward part leaves every compact set, and suppose grad Theta(Y_0) = 0 at one
point Y_0 of C_*.
  (a) Along all of C_*: grad Theta = 0, D^2 Theta = 0, Omega = 0 and grad Omega = 0; Theta is constant on C_*, and Theta = 0
      on C_* if beta > 2. The closure of C_* does not contain the center.
  (b) Suppose moreover that the backward orbit of C_* converges to a single point p and that DW(p) has no negative
      eigenvalue. If Theta - Theta(Y_0) has a first nonzero homogeneous Taylor polynomial of finite degree N at some point
      of C_*, then N is the same at every point of C_* and N is odd (so N >= 3). Consequently, if Theta has a local extremum
      at a point of C_*, every positive-order derivative of Theta and every derivative of Omega vanishes at every point
      of C_*.
Proof outline. (1) Since V = o(|X|) uniformly, X.W >= (beta/2)|X|^2 outside a large ball and |W| <= C(1 + |X|) on R^2;
the second bound and Gronwall's inequality give completeness of the flow, and the first makes -W point strictly inward
on large circles, so the backward semiorbit of C_* has compact closure and all fixed-order derivatives of the smooth fields
are bounded on it. Write X(t) for C_*, A(t) = DW(X(t)), g = grad Theta(X(t)). Differentiating (T) gives
g' = (c - A^T) g, a linear ODE, so g = 0 on C_*; then c Theta = W.grad Theta = 0 on C_*, and Theta is constant on C_*. Thus
Theta_x = 0 on C_* and (V) gives d Omega/dt = -Omega there; boundedness on the backward semiorbit gives Omega = 0 on C_*.
Every point of C_* lies in the open sign domain {x > 0}, so it is a local extremum of Omega and grad Omega = 0 on C_*.
(2) The gradient of (V) along C_* gives d(grad Omega)/dt + (I + A^T) grad Omega = grad Theta_x, so M e_1 = 0 on C_*, where
M = D^2 Theta(X(t)); differentiating g = 0 along C_* gives M W = 0. By 4.7(ix)(A), C_* is not contained in a horizontal line,
so W_2 != 0 at some point of C_*, where e_1 and W span R^2 and M = 0. Twice differentiating (T) and using g = 0 gives
M' = c M - A^T M - M A (the terms with D^2 W are contracted with g), a linear ODE, so M = 0 on all of C_*. By continuity
grad Omega = 0 and D^2 Theta = 0 on the closure of C_*, while Omega_x(0) = 4 a0/beta != 0; so the center is not in the
closure of C_*, and in (b) p != 0.
(3) For (b): with T_n = D^n Theta(X(t)), the n-th derivative of (T) gives T_n' = (c - sum over slots of A^T) T_n plus
terms that are linear in T_m, 1 <= m < n, so a block of vanishing positive-order jets propagates along C_* and the first
nonzero order N is the same at every point of C_*. Differentiating T_{N-1} = 0 along C_* gives T_N(W, v_2, ..., v_N) = 0.
Since Omega(p) = 0 by continuity, DW(p) is symmetric with eigenvalues >= 0, and the vorticity jets J_n = D^n Omega
satisfy the jet equations of 4.7(x) step (2), J_n' + L_n J_n = D^n Theta_x - (terms in J_m, 1 <= m < n), with L_n(p)
symmetric with eigenvalues >= 1; the backward-growth argument of 4.7(x) step (3) gives J_n = 0 on C_* for n <= N - 2.
Suppose N is even. At a point Y of C_* the Taylor expansion of Omega begins at degree N - 1, Omega(Y + z) =
J_{N-1}(z, ..., z)/(N - 1)! + o(|z|^{N-1}); this term has odd degree and, by the weak sign, cannot take both signs, so it
vanishes: J_{N-1} = 0 on C_*. The order-(N - 1) jet equation then gives D^{N-1} Theta_x = 0, that is
T_N(e_1, v_2, ..., v_N) = 0, on C_*; at a point of C_* with W_2 != 0 the vectors e_1 and W span R^2, so T_N = 0 there, a
contradiction. At a local extremum a finite first order would be even, so Theta - Theta(Y_0) is flat at each point of C_*,
D^n Theta_x = 0 on C_* for every n, and every J_n vanishes by the same backward-growth argument.
Scope of 4.20. A restricted statement under the weak-sign hypothesis; it concerns physical critical points of Theta, and
no profile and orbit satisfying its hypotheses is known. For beta > 2 a critical point of the angular amplitude H
(Theta = e^{(beta-2)t} H along orbits) with H != 0 is not a critical point of Theta. On the subclass G (4.18)
grad Theta = 0 only on the axis, so the hypothesis of (a) never holds there. Off G, grad Theta = 0 on the unstable
manifold of every hyperbolic saddle (4.19(c)); a branch of such a manifold lying in {x > 0} and escaping forward would
satisfy the orbit hypotheses of (a) under the weak sign, but its backward limit is a saddle, which (b) does not cover. For
beta = 2, (a) contains the orbit statement of 4.7(ix)(B), and (b) is the physical analogue of 4.7(x), with the order taken
for Theta itself rather than for h. Odd-order critical points, flat extrema and plateaus are not excluded; flatness along
one orbit does not imply vanishing on a neighbourhood.
4.21 Axis tails and angular tails at the vertical directions (class A, beta >= 2). Let (Theta, Omega, U) be a class A
profile with beta >= 2 and a0 > 0 (after the reflection of 4.8), let b, y_+ and y_- be as in 4.13, let a and h = A be the
angular limits of 4.12(d) and 4.10 (smooth by 4.16), and put d = 1/beta. (The constants P_+-, Q_+- below are not the
quotients P, Q of 4.17.)
  (a) Upper half-axis. If y_+ = +infinity (b > 0 on (0, infinity)), there are constants P_+, Q_+ > 0 with
        Theta_xx(0, y) = P_+ y^{-1-2d} (1 + O(y^{-d})),   Omega_x(0, y) = Q_+ y^{-1-d} (1 + O(y^{-d}))   as y -> +infinity,
      and h''(pi/2) = P_+, a'(pi/2) = -Q_+. Hence h(theta)/cos^2 theta -> P_+/2 and a(theta)/cos theta -> Q_+ as
      theta -> pi/2 (two-sided limits over cos theta != 0), and h > 0, a > 0 on (pi/2 - delta, pi/2) for some delta > 0.
  (b) Lower half-axis. If y_- = -infinity (b < 0 on (-infinity, 0)), the same holds with |y| as y -> -infinity and
      constants P_-, Q_- > 0: h''(-pi/2) = P_-, a'(-pi/2) = Q_-, h/cos^2 theta -> P_-/2 and a/cos theta -> Q_- as
      theta -> -pi/2.
  (c) Both hypotheses hold for every profile in G (4.18(a)). Let beta > 2. On each half-axis satisfying the hypothesis of
      (a) or (b), in particular on both half-axes for every profile in G, the decay bounds of 4.17(a) for Theta/x^2,
      Theta_x/x and Omega/x are sharp (their axis values are Theta_xx(0, y)/2, Theta_xx(0, y) and Omega_x(0, y)), and the
      angular bounds |h| <= C cos^2 theta, |a| <= C |cos theta| are sharp at the
      corresponding vertical direction (sharpness of the bound for v = V_1/x is not asserted). At beta = 2, (a) and (b)
      add rates and the identification of the vertical slopes of a with the axis constants to the axis statements of
      4.7(v) and 4.7(vii) (there P_+- = 2A_+-).
  (d) If the profile is in G and Theta_x >= 0 on {x > 0}, then Omega > 0 on {x > 0} and a(theta) > 0 for |theta| < pi/2.
Proof outline. (1) Rates. With a_ax(y) = Theta_xx(0, y)/2 (as in 4.7(v)) and q(y) = Omega_x(0, y), 4.13(i) gives b a_ax'
= (2b' - Lambda) a_ax, b q' + (M - b') q = 2 a_ax, and a_ax, q > 0 on (0, infinity). By 4.12(e), |V| <= C r^{1-d} and
|DV| <= C r^{-d}, so b = beta y (1 + O(y^{-d})) and b' = beta + O(y^{-d}); hence (2b' - Lambda)/b = -(1 + 2d)/y +
O(y^{-1-d}) and (b' - M)/b = -(1 + d)/y + O(y^{-1-d}), with error terms whose integrals from y to infinity are
O(y^{-d}). Integrating the logarithmic derivative of a_ax from y0 > 0 gives a_ax = (P_+/2) y^{-1-2d} (1 + O(y^{-d}))
with P_+ > 0 (a positive value times the exponential of a convergent integral). In the same way the solution q_h of b
q_h' = (b' - M) q_h with q_h(y0) = 1 satisfies q_h = c_h y^{-1-d} (1 + O(y^{-d})), c_h > 0. Writing q = q_h R gives R' =
2 a_ax/(b q_h) > 0 and R' = O(y^{-1-d}), so R increases to a finite limit R_inf >= R(y0) > 0 with R_inf - R(y) =
O(y^{-d}), and Q_+ = c_h R_inf. On the lower half-axis the substitution z = -y, B(z) = -b(-z), a_ax(-z), q(-z) gives the
same equations with B > 0. No step uses beta > 2.
(2) Angular matching. At (0, r), r > 0, polar differentiation gives exactly
  Omega_x(0, r) = -r^{-1} d_theta Omega(r e(theta)),   Theta_xx(0, r) = r^{-1} d_r Theta(r e(theta)) + r^{-2} d_theta^2 Theta(r e(theta))
at theta = pi/2, and d_r Theta = 0 there because Theta(0, y) = 0. The expansions of 4.16 hold in every C^j(S^1), so
d_theta Omega(r e) = r^{-d} (a' + O(r^{-d})) and d_theta^2 Theta(r e) = r^{1-2d} (h'' + O(r^{-d})) uniformly in theta.
Comparison with (1) gives a'(pi/2) = -Q_+ and h''(pi/2) = P_+ (note 2 - (1 - 2d) = 1 + 2d). Since a(pi/2) = 0 and
h(pi/2) = h'(pi/2) = 0 (Theta = 0 on the axis, and h is even under theta -> pi - theta), Taylor expansion gives the limits
of a/cos theta and h/cos^2 theta. At theta = -pi/2 the first formula holds with the opposite sign, which gives
a'(-pi/2) = Q_-. Only the uniform derivative asymptotics of 4.16, proved for exact profiles, are used; nothing here
licenses termwise differentiation of an approximate fit.
(3) Positivity in G. Write Theta = x^2 F with F smooth, even in x and F(0) = a0 > 0; then Theta_x = x (2F + x F_x) > 0 for
small |X| with x > 0. The half-planes are invariant and every backward orbit tends to 0 (4.18(a)), so along an orbit
starting in {x > 0}, Theta_x >= 0 at all times and Theta_x > 0 at all sufficiently negative times. Integrating (V) along
the orbit, with Omega bounded,
  Omega(Y) = int_{-infinity}^0 e^s Theta_x(phi_s Y) ds > 0,   A_tr(Y) = int_{-infinity}^{infinity} e^s Theta_x(phi_s Y) ds > 0,
the second integral converging because |grad Theta| <= C r^{-2d} (4.12(c)) and |phi_s Y| is comparable to e^{beta s} for
s >= 0, so that its forward integrand is O(e^{-s}). In G the escape set is R^2 \ {0}, so Phi is a bijection of
R^2 \ {0} (4.12 step (7)). The flow commutes with the reflection S(x, y) = (-x, y), hence so does Phi, and Phi_1 >= 0 on
{x > 0} (the half-planes are invariant); Phi_1(Y) = 0 with x > 0 would give Phi(Y) = Phi(SY) with SY != Y. So Phi
maps {x > 0} onto {x > 0}, and A_tr(Y) = |Phi(Y)|^{-d} a(Phi(Y)/|Phi(Y)|) gives a > 0 on the open right semicircle.
Remark (a second proof of the vertical slopes in G, without 4.16). With xi as in 4.18(b), Theta_x = 2 a0 xi xi_x and
xi(phi_s Y) = e^{lambda1 s} xi(Y), so A_tr = xi Qt with Qt(Y) = 2 a0 int_R e^{(1 + lambda1) s} xi_x(phi_s Y) ds,
continuous on R^2 \ {0}: on compact sets the forward integrand is O(e^{-s}), since N_s = e^{-beta s} D phi_s and its
inverse are bounded (N_s converges, det N_s = 1) and grad xi(phi_s Y) = e^{(lambda1 - beta) s} N_s(Y)^{-T} grad xi(Y),
and the backward integrand is O(e^{(1 + lambda1) s}) because backward orbits converge to 0 locally uniformly. With
H_t(Y) = 2 a0 int_t^infinity e^{(1 + lambda1) s} xi_x(phi_s Y) ds = O(e^{-t}) one has
Omega(phi_t Y) = e^{-t} xi(Y) (Qt(Y) - H_t(Y)). At Y0 = (0, y0) a difference quotient in x, in which only the vanishing
factor xi is differentiated, gives e^t Omega_x(phi_t Y0) k_t = xi_x(Y0) (Qt(Y0) - H_t(Y0)) with k_t = d_x (phi_t)_1 (Y0).
With Phi(Y0) = (0, sigma rho), rho > 0, sigma = +-1, and e^{-beta t} k_t -> k = D Phi_11(Y0) > 0, the rates of (1) give
d_x A_tr(Y0) = Q_sigma k rho^{-1-d}, and since D Phi(Y0) is diagonal, a'(sigma pi/2) = -sigma Q_sigma.
Scope. Necessary conditions. On each half-axis without an axis zero of W, a numerical candidate must show positive
limits of |y|^{1+2d} Theta_xx(0, y) and |y|^{1+d} Omega_x(0, y), and its angular tails must leave the vertical
directions with the matching slopes; a representation that builds these powers in by construction can satisfy the
matching without solving the equations, so only a verified failure provides an exclusion, and that requires the branch
hypothesis and control of the asymptotic error (the constants and the onset of the asymptotic regime depend on the
profile). (d) gives no contradiction: no result of this report excludes, for beta > 2, a tail that is positive on the
whole open right semicircle (the strict-sign argument of 4.7(viii) uses beta = 2). G is not excluded.
4.22 The temperature tail in G. Let the profile be in G (beta > 2, a0 > 0), Phi the scattering map of 4.12 step (7)
(a bijection of R^2 \ {0} in G, 4.21 step (3)), h = A and a the angular limits of 4.10 and 4.12(d), d = 1/beta,
m = 1 - 2d, e(theta) = (cos theta, sin theta), and P_+-, Q_+- the constants of 4.21.
  (a) Theta(Y) = |Phi(Y)|^m h(Phi(Y)/|Phi(Y)|) for every Y != 0. Theta > 0 off the axis, and h > 0 at every direction
      with cos theta != 0; the only zeros of h are the vertical directions, where h''(+-pi/2) = P_+- > 0.
  (b) The function h_c = h/cos^2 theta, extended by P_+-/2 at theta = +-pi/2, is smooth and positive on the circle, and
        r^{1+2d} Theta(r e(theta))/(r cos theta)^2 = h_c(theta) + O(r^{-d})   uniformly in theta (including the axis).
      Consequently there are constants 0 < c <= C with c (1 + r)^{-1-2d} <= Theta/x^2 <= C (1 + r)^{-1-2d} on R^2
      (Theta/x^2 extended by Theta_xx(0, y)/2 on the axis): in G the upper bound of 4.17(a) is two-sided.
  (c) Level curves. Let T > 0 and delta = min(d, 1 - 2d). For all sufficiently large y > 0 the level set
      {Theta = T, x > 0} meets the horizontal line at height y in exactly one point (x_T(y), y), x_T is smooth, and
        x_T(y) = (2T/P_+)^{1/2} y^{1/2+d} (1 + O(y^{-delta})),   Omega(x_T(y), y) = Q_+ (2T/P_+)^{1/2} y^{-1/2} (1 + O(y^{-delta}));
      likewise with P_-, Q_- and |y| as y -> -infinity. The exponent -1/2 does not depend on beta.
  (d) Linearizable case. Let kappa = 0 in 4.18(b), with the normalization xi_x(0) = 1 of the construction there, and put
      alpha = lambda1/beta, gamma = lambda2/beta (so alpha + gamma = 2). Then Phi is a smooth diffeomorphism of R^2 \ {0},
        (xi, eta)(Phi^{-1}(r e(theta))) = (r^alpha q(theta), r^gamma g(theta))   with q, g smooth,
      q = sign(cos theta) (h/a0)^{1/2} = cos theta (h_c/a0)^{1/2}, and
        alpha q g' - gamma q' g = 1.
      In particular g(pi/2) = gamma^{-1} (2 a0/P_+)^{1/2} > 0, g(-pi/2) = -gamma^{-1} (2 a0/P_-)^{1/2} < 0, and g has
      exactly one zero in each open semicircle, which is simple.
Proof outline. (a) By (T), Theta(phi_t Y) = e^{(beta-2)t} Theta(Y); by 4.10, Theta(phi_t Y) = |phi_t Y|^m (h(arg phi_t Y) + o(1)),
and e^{-beta t} phi_t Y -> Phi(Y) != 0. Since beta m = beta - 2, letting t -> infinity gives the formula. If xi(Y) = 0
for the coordinates (xi, eta) of 4.18(b), then (xi, eta)(SY) = (xi, eta)(Y) with S(x, y) = (-x, y), so SY = Y by
injectivity; hence Theta = a0 xi^2 > 0 off the axis. Phi maps each open half-plane onto itself (4.21 step (3)), so
h > 0 at every nonvertical direction; the values at the vertical directions are those of 4.21.
(b) h is smooth (4.16) with h(+-pi/2) = h'(+-pi/2) = 0, so h_c is smooth, and positive by (a) and 4.21. Put
E_r(theta) = r^{-m} Theta(r e(theta)) - h(theta). By 4.16, ||E_r||_{C^2} <= C r^{-d}, and E_r, E_r' vanish at
theta = +-pi/2 (axis vanishing and evenness under theta -> pi - theta). Taylor's formula with integral remainder gives
|E_r(theta)| <= C r^{-d} cos^2 theta near the vertical directions, and the same bound holds away from them since
|cos theta| is bounded below there; dividing by cos^2 theta gives the uniform expansion and the two-sided bound outside a
large disk. Inside it, Theta/x^2 = int_0^1 (1 - s) Theta_xx(s x, y) ds is continuous and positive: off the axis by (a),
on the axis since Theta_xx(0, y) > 0 (4.18(a)).
(c) By the lower bound in (b), Theta = T forces x^2 <= (T/c)(1 + r)^{1+2d}, so at large heights every point of the
level set satisfies x <= K_T y^{1/2+d} and r/y = 1 + O(y^{-m}). On {0 <= x <= K y^{1/2+d}} one has
theta - pi/2 = O(y^{-m/2}); h_c is even about pi/2, so h_c(theta) = P_+/2 + O((theta - pi/2)^2), and (b) gives
Theta(x, y) = (P_+/2) x^2 y^{-1-2d} (1 + O(y^{-delta})) uniformly there for every fixed K. Comparing the values at
c1 y^{1/2+d} and c2 y^{1/2+d}, 0 < c1 < (2T/P_+)^{1/2} < c2, gives a root with the stated asymptotics. Uniqueness: the
rescaled temperature R^{-m} Theta(R z) converges in C^2 on compact subsets of R^2 \ {0} to |z|^m h(arg z) (4.16 step
(2)), whose xx-derivative at (0, 1) is h''(pi/2) = P_+ > 0 (the term r^{-1} d_r vanishes on the axis); hence
Theta_xx > 0 on a cone {0 <= x <= eps y, y > R}, which contains every root at large heights since 1/2 + d < 1, and with
Theta_x(0, y) = 0, Theta is strictly increasing in x there. The implicit function theorem gives smoothness. For Omega,
F_r(theta) = r^d Omega(r e(theta)) - a(theta) has ||F_r||_{C^1} = O(r^{-d}) (4.16) and vanishes at pi/2, so first-order
Taylor division gives Omega/x = r^{-1-d} (a_c(theta) + O(r^{-d})) with a_c = a/cos theta smooth, even about pi/2 and
a_c(pi/2) = Q_+ (4.21); as above Omega/x = Q_+ y^{-1-d} (1 + O(y^{-delta})) on the cusp, and substituting x_T gives the
formula, since (1/2 + d) - 1 - d = -1/2. The lower ends are treated in the same way.
(d) Smoothness of Phi. The normalized flow z(t, Y) = e^{-beta t} phi_t Y solves d_t z = B_t(z) with
B_t(z) = e^{-beta t} V(e^{beta t} z). The convergence in every C^j of the rescaled velocities in 4.16 step (2) gives
|D^k V(X)| <= C_k |X|^{1-d-k} for large |X|, so |D_z^k B_t| <= C_k e^{-t} on compact annuli (beta d = 1). Since z(t, .)
converges to Phi locally uniformly on R^2 \ {0} and Phi != 0, differentiating the flow equation and induction on k give
local uniform convergence of every derivative, so Phi is smooth; det D Phi = 1, so Phi^{-1} is smooth. Identity. With
L_t(xi, eta) = (e^{lambda1 t} xi, e^{lambda2 t} eta), the conjugacies (xi, eta) o phi_t = L_t o (xi, eta) (4.18(b),
kappa = 0) and Phi o phi_t = e^{beta t} Phi give H(rho Z) = (rho^alpha H_1(Z), rho^gamma H_2(Z)) for the smooth map
H = (xi, eta) o Phi^{-1}. Both factors preserve area and orientation, and the polar Jacobian of H at r e(theta) is
r^{alpha + gamma - 1} (alpha q g' - gamma q' g) = r (alpha q g' - gamma q' g), which gives the identity. By (a) and
Theta = a0 xi^2, q^2 = h/a0; xi has the sign of x (xi is odd, nonzero off the axis by (a), and xi_x(0) = 1), and Phi
preserves the half-planes, so q has the sign of cos theta. Hence q'(pi/2) = -(P_+/(2 a0))^{1/2} and
q'(-pi/2) = (P_-/(2 a0))^{1/2}; at a vertical direction q = 0, so -gamma q' g = 1, which gives the values of g there. On
(-pi/2, pi/2), where q > 0, (g q^{-gamma/alpha})' = 1/(alpha q^{1 + gamma/alpha}) > 0, and g q^{-gamma/alpha} tends to
-infinity and +infinity at the two ends, so g has exactly one zero there, and it is simple. The reflection (q odd, g even
under theta -> pi - theta) gives the left semicircle.
Scope. Necessary conditions in G; (c) is a numerical diagnostic along temperature level curves. The identity in (d)
does not determine the sign of xi_x. Example (beta = 3, so alpha = 1/6, gamma = 11/6): with theta0(u) = u - (5/12) sin 2u,
w(u) = theta0'(u) = (1/6) cos^2 u + (11/6) sin^2 u > 0, H0(r e(theta0(u))) = (r^alpha cos u, r^gamma sin u),
f(theta) = theta + (1/196) sin 98 theta, p = f' = 1 + (1/2) cos 98 theta > 0 and Sigma(r e(theta)) = r p(theta)^{-1/2} e(f(theta)),
the map H = H0 o Sigma is a smooth, area- and orientation-preserving diffeomorphism of R^2 \ {0} that commutes with the
reflection, is weighted homogeneous as in (d) and has H_1 > 0 on {x > 0}. At theta = pi/4 (p = 1, p' = -49),
d_x H_1(r e(theta)) = r^{alpha - 1} L with L = 2^{-1/2} (-(47/12) cos u* + sin u*/w(u*)), u* = theta0^{-1}(pi/4 + 1/196);
theta0(pi/3) < pi/4 + 1/196 < theta0(3 pi/8) gives cos u* > 1/3 and w(u*) > 11/8, so L < 2^{-1/2} (-47/36 + 8/11) < 0
(numerically L = -0.7912). So H_1 d_x H_1 < 0 near the direction pi/4: these geometric properties alone do not imply
Theta_x >= 0, and a proof of that sign requires additional profile information. The map is not a profile. G is not
excluded.

4.23 Homogeneous weights, the strain identity and their limits (class A, beta >= 2). Let (Theta, Omega, U) be a class A
profile, V = U_rel, d = 1/beta, k0 = 2 - d, kT = 2 - 2d. For complex k and a smooth function phi on the circle such that
f_k = r^{-k} phi(theta) is odd in x, put g_k = d_x f_k (homogeneous of degree -k-1, even in x). For large r = |X|,
  |Omega| <= C r^{-d},  |grad Omega| <= C r^{-1-d},  |Theta| <= C r^{1-2d},  |grad Theta| <= C r^{-2d},  |V| <= C r^{1-d}   (*)
(4.10, 4.12(c)-(e), and the uniform local regularity of step (2) of 4.16 for grad Omega).
  (a) (homogeneous identities) With all integrals absolutely convergent,
        beta (k - k0) int f_k Omega = int Omega V.grad f_k - int Theta g_k        for k0 < Re k < 3,
        beta (k - kT) int g_k Theta = int Theta V.grad g_k                         for kT < Re k < 3
      (sufficient strips; a particular phi may allow more). For k = 2 and f = K_c = x y/|X|^4, so that
      int K_c Omega = pi c = pi (1 + beta/2) by 4.1, and with d_x K_c = y (y^2 - 3x^2)/|X|^6, this gives the strain identity
        (S)   pi (1 + beta/2) = int Omega V.grad K_c - (1/2) int Theta V.grad(d_x K_c).
      Its right side is quadratic in the pair (Omega, Theta) (V is linear in Omega) and is invariant under the signed
      scaling (A6).
  (b) (completeness) Conversely, let Theta, Omega be smooth with the parities of (A2), (A3), Theta(0, y) = 0 for all y,
      V the canonical relative velocity (A4), and the bounds (*). If the two identities of (a) hold for every such phi
      and every real k in the stated strips, then (V) and (T) hold. So the family is an equivalent reformulation of the
      equations, not a weakening of them.
  (c) (kernel; no sign) int Omega V.grad K_c = int int Omega(X) Omega(Y) H(X, Y) dX dY with the symmetric kernel,
      homogeneous of degree -4 jointly,
        2H(X, Y) = L(X, Y).grad K_c(X) + L(Y, X).grad K_c(Y),   L(X, Y) = K(X - Y) + K(Y)   (K as in (A4)),
      that is 2H = K(X - Y).[grad K_c(X) - grad K_c(Y)] + K(Y).grad K_c(X) + K(X).grad K_c(Y); the grouped integrand
      |Omega(X)| |Omega(Y)| |L(X, Y)| |grad K_c(X)| is integrable. The terms with K(Y), K(X) come from the subtraction in the
      canonical inverse and cannot be dropped. This form has no sign on {Omega >= 0 on x > 0}: for smooth radially
      symmetric blobs of masses +Gamma at (a, b) and -Gamma at (-a, b), a, b > 0, shrinking to points, the center strain
      tends to 2 Gamma a b/(pi (a^2 + b^2)^2) > 0 and the form tends to
      Gamma^2 (b^2 - 3a^2)(a^2 - 3b^2)/(2 pi (a^2 + b^2)^4), which equals pi c^2/2 > 0 at b = a and -88 Gamma^2/(625 pi a^4) < 0
      at b = a/2 (radial symmetry is used: the self-interaction of a radial blob vanishes, that of a nonradial one need
      not). Moreover, for every beta > 2 there are smooth fields Theta, Omega with the parities, Theta(0, y) = 0, the
      canonical inverse, the center conditions DV(0) = (1 + beta/2) diag(-1, 1), Theta = a0 x^2 + O(|X|^4), a0 > 0,
      Omega_x(0) = 4 a0/beta, the bounds (*) and those of 4.17(a), Theta > 0 and Omega > 0 on {x > 0}, which satisfy (S)
      exactly and violate both (V) and (T). So (S) is consistent with these sign, center and decay conditions.
      Second, for every beta > 2 there are smooth fields Theta, Omega with the parities, Theta = 0 exactly on the axis
      and Theta > 0 off it, the canonical inverse, the center conditions DV(0) = (1 + beta/2) diag(-1, 1),
      Theta = a0 x^2 and Omega = (4 a0/beta) x on a neighborhood of 0 (where both (T) and (V) hold), the bounds (*), the
      tail Omega = mu r^{-d} cos theta with mu > 0 for all large r, W with no zero but 0, every nonzero forward orbit
      escaping and every backward orbit tending to 0 (the flow condition in the definition of G in 4.18; these fields
      are not profiles, so they are not in G), (T) exact on R^2 and (S) exact, for which (V) fails on a whole interval
      of the positive x-axis; their vorticity changes sign in {x > 0}. So (S) is also consistent with exact (T) and
      these center, decay and flow conditions. With (T) exact, (S) is equivalent to the single identity of the first
      family of (a) at k = 2, f = K_c, while by (b) some member of the first family fails, since (V) fails.
      Third, for every beta > 2 there are smooth fields Theta, Omega with the parities, Theta = 0 exactly on the axis
      and Theta > 0 off it, Omega > 0 on {x > 0}, the canonical inverse, DV(0) = (1 + beta/2) diag(-1, 1),
      Omega = (4 a0/beta) x + O(|X|^3) and Theta = a0 x^2 + O(|X|^3) with a0 > 0, the bounds (*), the tail
      Omega = mu r^{-d} cos theta + O(r^{-d-2}) with mu > 0, W.X >= kappa |X|^2 for some kappa > 0 (so 0 is the only
      zero of W and the flow condition of G holds), (T) exact on R^2 and (S) exact, for which (V) fails at every
      sufficiently large point of the positive x-axis. So (S) is also consistent with exact (T), the vorticity sign
      and these center, decay and flow conditions.
  (d) (critical residue) Omega = r^{-d} a(theta) + O(r^{-2d}) uniformly in theta (a the tail of 4.12(d)), and the moment
      k -> int f_k Omega continues meromorphically from k0 < Re k < 3 to kT < Re k < 3 with at most a simple pole at k0,
      of residue A_phi = int_0^{2 pi} phi(theta) a(theta) d theta; moreover, with both integrals absolutely convergent,
        beta A_phi = int Omega V.grad f_{k0} - int Theta V.grad g_{k0}.
  (e) (weighted horizontal identity, beta > 2) With m = 2 - d (the exponent alpha of 4.17(c)), D = {x > 0} and P, v
      of 4.17, C_m = 1 + (m + 1) v, both integrals converging absolutely,
        int_D x^{1-m} C_m P dX = 0,
      obtained from (T) with the weight d_x(x^{-m}) on D, a companion of 4.17(c). Since P(0) = a0 and
      C_m(0) = 1 - (3 - d)(beta + 2)/2 < 0, it forces a0 C_m P > 0 somewhere in D (with C_m < 0 and a0 P < 0 not
      excluded by the identity alone). A point with C_m > 0 and a0 P > 0 exists anyway: C_m -> 1 by 4.17(a), and by 4.10
      a0 P > 0 for all large radii on a ray strictly inside D. So the identity has no sign that excludes a profile.
  (f) (restricted exclusions) (i) No class A profile has Omega(x, y) <= Omega(x, -y) for all x, y > 0; in particular
      no class A profile has Omega even in y. (ii) For beta > 2, with L_x = sup |Omega/x| and
      A_x = sup_{X != 0} |X|^{1+d} |Omega/x| (finite by 4.17(a)),
        |c| <= (4 (beta + 1)/(3 pi)) L_x^{1/(beta+1)} A_x^{beta/(beta+1)},
      so every profile has L_x^{1/(beta+1)} A_x^{beta/(beta+1)} >= 3 pi (beta + 2)/(8 (beta + 1)); this product is
      invariant under the signed scaling (A6).
These are necessary conditions; they establish neither existence nor nonexistence of class A profiles. Within the class
of (b), the full family of (a) is equivalent to (V) and (T). For beta > 2, (c) proves that (S) is compatible with the
listed sign, center and decay conditions (first construction), and with exact (T), hence with every identity of the
second family of (a), and the center, decay and flow conditions listed for the second construction, and in the third
construction moreover with Omega > 0 on {x > 0}; it does not show that (S) can hold together with further members of
the first family. An exclusion through these weights would therefore need further members of the
family (by (b), ultimately the equations) or other information. No contradiction is derived from (d) or (e),
and (f) gives only the two stated restricted exclusions; nothing further is derived for the subclass G of 4.18.
Items (a), (b), (d), (f)(i) and the kernel and blob assertions of (c) hold for beta >= 2; the three constructions in (c),
(e) and (f)(ii) are proved for beta > 2.
Proof outline. (a) Multiply (V) by f_k and (T) by g_k and integrate by parts on {eps < |X| < R}. Since X.grad f_k =
-k f_k, X.grad g_k = -(k + 1) g_k and div W = 2 beta, the bulk coefficients are 1 - (2 - k) beta = beta (k - k0) and
(2 - k) beta - 2 = -beta (k - kT). Near 0, Omega, V, W = O(r) and Theta = O(r^2); with (*) and W = O(r) the four bulk
integrands are O(r^{2-Re k}) dr at 0 and O(r^{1-Re k-d}), O(r^{1-Re k-2d}), O(r^{1-Re k-2d}), O(r^{1-Re k-3d}) dr at
infinity (for int f_k Omega, int Omega V.grad f_k, int Theta g_k, int Theta V.grad g_k); the inner boundary terms are
O(eps^{3-Re k}), the outer ones O(R^{2-Re k-d}) (vorticity flux) and O(R^{2-Re k-2d}) (the two temperature terms). For
k = 2 and f = K_c the second identity reads 2 int Theta d_x K_c = int Theta V.grad(d_x K_c), and the first becomes (S)
after int K_c Omega = pi c. Scaling: under (A6) the area, V and grad K_c contribute l^2, l, l^{-3} to the first term
and Theta, V, grad d_x K_c and the area contribute l, l, l^{-4}, l^2 to the second; for l < 0 the parities of K_c and
d_x K_c under X -> -X give the same.
(b) Let E_V = W.grad Omega + Omega - Theta_x (odd in x, O(r) at 0, O(r^{-d}) at infinity by (*)) and
E_T = W.grad Theta - (beta - 2) Theta (even, O(r^2) at 0, O(r^{1-2d}) at infinity). The integrations of (a) show that
the two identities are int f_k E_V = 0 and int E_T d_x f_k = 0. Both sides are holomorphic in k on the strips (the
power margins dominate the logarithms produced by differentiation in k), so they hold for k = sigma + i tau. With r = e^t
the first says that the Fourier transform of the L^1 function e^{(2 - sigma) t} int phi(theta) E_V(e^t, theta) d theta
vanishes; hence every odd angular projection of E_V vanishes at every radius, and E_V = 0. Superposing the second over
k = sigma - i tau with rapidly decreasing coefficients (Fourier inversion in t = log r; differentiation in x costs a
factor 1 + |tau|) gives int E_T d_x(eta(r) phi(theta)) dX = 0 for eta in C_c^infinity(0, infinity); finite sums of such
products are dense, with first derivatives, among smooth odd test functions on compact annuli, so d_x E_T = 0 off 0. On
{x > 0} therefore E_T(x, y) = E_T(0, y) = W_1 Theta_x + W_2 Theta_y - (beta - 2) Theta at (0, y), which is 0 because W_1(0, y) = 0
and Theta(0, y) = Theta_y(0, y) = 0; E_T is even, so E_T = 0.
(c) With L the subtracted kernel, int Omega V.grad K_c = int int Omega(X) Omega(Y) L(X, Y).grad K_c(X) dY dX. The bound
int |L(X, Y)| |Omega(Y)| dY <= C min(|X|, |X|^{1-d}) (mean value theorem for |Y| > 2|X|, direct estimates otherwise)
gives integrability of the grouped integrand (radial majorants C dr at 0 and C r^{-1-2d} dr at infinity), and averaging
over X <-> Y gives H. Blobs: the self-induced velocity of a radial blob is tangent to its level circles, so
div(omega_blob u_self) = 0 and its self term vanishes; the cross and center terms converge. At (a, b) the blob at
(-a, b) induces (0, Gamma/(4 pi a)) and U(0) = (0, Gamma a/(pi (a^2 + b^2))), so V(a, b) = (0, (Gamma/pi)(1/(4a) - a/(a^2 + b^2)));
with d_y K_c(a, b) = a (a^2 - 3b^2)/(a^2 + b^2)^3 and the equal contribution of the mirror blob this gives the limit, and
the center strain is (1/pi) sum Gamma_i K_c(X_i) over the blob centers X_i. Construction (beta > 2, c_* = 1 + beta/2 > 2): radial blobs at b = a,
normalized to c = c_*, give a quadratic term N = int Omega V.grad K_c near pi c_*^2/2 > pi c_*; add mu Omega_1, Omega_1 = -Laplacian Psi_1,
Psi_1 = -x (1 + r^2)^q, q = (1 - d)/2 (Omega_1 > 0 on x > 0, even in y, so c(Omega_1) = 0, tail r^{-d}; its stream
velocity minus its value at 0 is the canonical inverse by the Liouville argument of (A4)), and put
Theta_0 = a0 x^2 (1 + r^2)^{-(1+2d)/2} with a0 = 2 beta q mu, so Omega_x(0) = 8 q mu = 4 a0/beta. For small mu the defect
2(N - pi c_*) - int Theta_0 V.grad(d_x K_c) is positive; adding s Theta_1, Theta_1 >= 0 an even bump supported in a narrow cone about
the downward axis near 0 and away from the axis (there V.grad(d_x K_c) = c_*(-x d_x + y d_y) d_x K_c + O(r^{-2}), with
value -3 c_*/y^3 > 0 on the axis below 0), with the appropriate s > 0, makes (S) exact. On the positive x-axis far out,
E_T/Theta = (beta + 2) x^{-2} + O(x^{-3}) > 0 and E_V = -a0 (1 - 2d) x^{-2d} + o(x^{-2d}) != 0.
Second construction (beta > 2; c = 1 + beta/2, s0 = beta - c = (beta - 2)/2; chi smooth and nonincreasing on
[0, infinity), equal to 1 on [0, 1] and 0 on [2, infinity), eta = 1 - chi). Put
  Psi = c x y chi(r/R) + b_4 r^2 sin(4 theta) eta(r) chi(r/R) + delta x^3 chi(r) + mu Psi_t,
  Psi_t = -r^{2-d} cos(theta) eta(r/(4R))/((2 - d)^2 - 1),
with 0 <= b_4 <= s0/16, delta < 0 and mu > 0 small, and R > 4 with A_R = 12 log R - C_chi > 32/s0,
where C_chi = 12 int_1^2 chi(s)(1 - chi(s)) ds/s + 9/2 + (3/2) int_1^2 s chi'(s)^2 ds. Every term is smooth (the angular
modes are multiplied by functions vanishing near 0) and odd in x. Omega = -Delta Psi, and
V = (-Psi_y, Psi_x) = O(r^{1-d}) differs from the velocity (A4) of Omega by a harmonic field of sublinear growth vanishing at 0,
so V is the canonical inverse; -Delta(mu Psi_t) = mu r^{-d} cos theta for r >= 8R.
For a stream r^2 p2(r) sin(2 theta) + r^2 p4(r) sin(4 theta), Omega has the modes 2 and 4 with
coefficients -5 r p2' - r^2 p2'' and 12 p4 - 5 r p4' - r^2 p4'', and V.grad K_c has a mode 4 term from p2 and
mode 2 and 6 terms from p4, so only products between the two stream modes survive the angular integration; one
integration by parts (boundary term -2 r p2 p4' + r p4 p2' - (r^2/2) p2' p4' + p2 p4, which vanishes at both ends here)
gives
  int Omega V.grad K_c = pi int_0^infinity [24 p2 p4/r + 9(p4 p2' - p2 p4') - 3 r p2' p4'] dr,
which for the first two terms of Psi (p2 = (c/2) chi(r/R), p4 = b_4 eta(r) chi(r/R), where eta' and the derivative
of chi(r/R) have disjoint supports) equals pi c b_4 A_R. For r < 1, Psi = c x y + delta x^3,
so W = (s0 x, (beta + c) y + 3 delta x^2), Omega = -6 delta x,
and Theta = a0 x^2 with a0 = -3 beta delta/2 > 0 solves (T) and (V) there; c, the center jets and V(0) = 0 do not depend
on b_4, mu, and int K_c Omega = pi c (only the mode 2 term contributes). The radial component of W is at
least (beta - c - 4 b_4 - 6 |delta| - s0/8) r >= (s0/2) r for |delta| < s0/48 and mu small, and |W| <= C(1 + r), so the
flow phi_t of W is complete, 0 is its only zero, every nonzero forward orbit escapes and every backward orbit
enters r < 1 and tends to 0. Put xi(Y) = e^{s0 T} (phi_{-T} Y)_1 for any T >= 0 with phi_{-T} Y in r < 1 (independent
of T, since x' = s0 x there) and Theta = a0 xi^2: it is smooth, even in x, zero exactly on the axis (the axis is
invariant and the flow commutes with the reflection), equal to a0 x^2 near 0,
and xi(phi_t Y) = e^{s0 t} xi(Y) gives (T) on R^2;
integrating d(log r)/dt = beta + O(r^{-d}) and d_t grad Theta = -(2I + DV^T) grad Theta along orbits
gives Theta = O(r^{1-2d}) and grad Theta = O(r^{-2d}), uniformly for small parameters and with a factor |delta|. The
difference D(b_4, delta, mu) of the two sides of (S) is continuous on a small parameter rectangle (dominated
convergence; the integrands have parameter-independent integrable majorants, of radial
order C dr at 0 and C r^{-1-2d} dr at infinity),
with D(0, 0, 0) = -pi c and D(s0/16, 0, 0) = pi c (s0 A_R/16 - 1) > pi c (Theta = 0 at delta = 0);
fixing delta < 0 and mu > 0 so small that both signs persist for every b_4 in [0, s0/16], the intermediate value theorem
gives b_4 in (0, s0/16) with (S) exact. On 2R < r < 4R every term of Psi vanishes and W = beta X,
so (T) gives Theta(x, 0) = C x^{1-2d} with C > 0 for 2R < x < 4R, and
there W.grad Omega + Omega - Theta_x = -(1 - 2d) C x^{-2d} < 0. On 2 < r < R, Omega = 12 b_4 sin(4 theta), which takes
both signs in {x > 0}. With (T) exact, the second identity of (a) holds for all k in its strip and all phi, and (S) is
equivalent to the first identity at k = 2 with f = K_c.
Third construction (beta > 2, s0 = beta - c = (beta - 2)/2; the letters below are local to it). A dot denotes
r d/dr. Let eta be as in the second construction, M0 >= 48 with 4 |12 eta - 4 eta. - eta..| <= M0 eta(2r) for all r,
chi_1 smooth and nonincreasing on the real line, equal to 1 on (-infinity, 0] and 0 on [1, infinity), zeta smooth,
supported in [0, 1], with zeta >= |chi_1'| + |chi_1''|, b_* > 0 with 4 b_* <= s0/8, M0 b_* <= s0/8 and
b_* < 36 c/M0^2, and S0 so large that (c + 4 b_*) (4/S0 + 1/S0^2) sup zeta <= s0/8. For R > 2 put
chi_R(r) = chi_1(log(r/R)/S0), J_R(r) = (4/S0 + 1/S0^2) zeta(log(r/R)/S0), and for 0 <= b_4 <= b_* and
0 <= delta, mu <= s0/16
  w = M0 b_4 eta(2r) chi_R + (c + 4 b_4) J_R + delta r exp(-r^2) + mu r (1 + r^2)^{-(1+d)/2},
  Psi = p(r) cos theta + (c/2) r^2 sin(2 theta) chi_R + b_4 r^2 sin(4 theta) eta chi_R,
  p(r) = -(1/2) (r int_0^r w ds - r^{-1} int_0^r s^2 w ds).
Then -Delta(p cos theta) = w cos theta, p = O(r^3) at 0, (p/r)' = -r^{-3} int_0^r s^2 w ds, and
p = -mu r^{2-d}/((1 - d)(3 - d)) + C r + O(r^{-d}) + O(r^{-1}) at infinity; V = (-Psi_y, Psi_x) differs from the
velocity (A4) of Omega = -Delta Psi by a harmonic field of sublinear growth vanishing at 0, so V is the canonical
inverse. Omega = w cos theta + w2 sin(2 theta) + w4 sin(4 theta) with w2 = -(c/2)(4 chi_R. + chi_R..) and
w4 = b_4 (12 eta chi_R - 4 (eta chi_R). - (eta chi_R)..); since eta' and chi_R' have disjoint supports,
2 |w2| <= c J_R and 4 |w4| <= M0 b_4 eta(2r) chi_R + 4 b_4 J_R, so
w >= 2 |w2| + 4 |w4| + delta r exp(-r^2) + mu r (1 + r^2)^{-(1+d)/2}, and |sin 2 theta| <= 2 |cos theta|,
|sin 4 theta| <= 4 |cos theta| give Omega > 0 on {x > 0} when delta + mu > 0. Near 0, Psi = c x y + O(r^3) and
Omega = (delta + mu) x + O(r^3). From 0 <= w <= 3 s0/8, |p| <= s0 r^2/8; the radial velocities of the three terms of
Psi are p sin theta/r, -c r cos(2 theta) chi_R and -4 b_4 r cos(4 theta) eta chi_R, so
W.X >= (beta - c - 4 b_* - s0/8) r^2 >= (3 s0/4) r^2. With the complete flow phi_t of W,
xi(X) = x exp(int_0^infinity (s0 - W_1/x)(phi_{-t} X) dt) (the integrand is smooth, even and O(|phi_{-t} X|), and
the reversed flow contracts exponentially near 0 with all derivatives) is smooth, odd, of the sign of x, with
W.grad xi = s0 xi, and Theta = a0 xi^2 with a0 = beta (delta + mu)/4 solves (T) on R^2; along outgoing orbits
log r = beta t + O(1) and D phi_t = e^{beta t} M(t) with M, M^{-1} bounded give Theta = O(r^{1-2d}) and
grad Theta = O(r^{-2d}). By the second identity of (a) at k = 2, (S) reads D = N - int Theta d_x K_c - pi c = 0 with
N = int Omega V.grad K_c. K_c has angular frequency 2, so only the mode pairs (1, 1) and (2, 4) contribute to N;
N1 = (pi/2) int_0^infinity w (p' - p/r) r^{-2} dr = -(3 pi/2) int_0^infinity ((p/r)')^2 dr/r <= 0, and the formula
of the second construction gives N24 = 12 pi c b_4 log R + O(1). At delta = mu = 0, (p/r)' = -M0 b_4/3 - C0 r^{-3} on
2 < r < R with C0 independent of R, and the outer transition is a fixed profile in r/R, so
N = pi (12 c b_4 - M0^2 b_4^2/6) log R + O(1) uniformly in R. Fix R with D(b_*, 0, 0) > 0; D(0, 0, 0) = N1 - pi c < 0.
D is continuous on the parameter box (parameter-independent integrable majorants; xi^2 obeys the bounds above
uniformly on the box, so int Theta d_x K_c = a0 int xi^2 d_x K_c = O(delta + mu)); fix delta, mu > 0 so small
that both signs persist, and the intermediate value theorem gives b_4 with (S) exact (R is fixed before delta, mu
are chosen). For r > R e^{S0} only the first mode remains; on the positive x-axis V_1 = Omega_y = 0 and
W.grad Omega + Omega = beta r w' + w = mu (beta + 1) r (1 + r^2)^{-(3+d)/2} + delta r exp(-r^2) (beta + 1 - 2 beta r^2)
= O(r^{-2-d}). The asymptotic map Z(a) = lim e^{-beta t} phi_t(a) on a large circle satisfies
det(beta Z, Z') = det(W(a), a') > 0 (det D phi_t = e^{2 beta t}), so the angle map Z/|Z| is a circle diffeomorphism
of degree one fixing the vertical directions, and the horizontal direction is the image of a point a_* with x > 0; writing
(r, 0) = phi_{t_r}(a_r), a_r -> a_* gives Theta(r, 0) = r^{1-2d} (H0 + o(1)) with H0 = Theta(a_*)/|Z(a_*)|^{1-2d} > 0.
By (T) on the positive x-axis, Theta_x(r, 0) = (1 - 2d) Theta(r, 0)/r - V_2 Theta_y/(beta r)
= (1 - 2d) H0 r^{-2d} + o(r^{-2d}), which exceeds W.grad Omega + Omega for all large r.
(d) From (V) and (*), beta r d_r Omega + Omega = Theta_x - V.grad Omega = O(r^{-2d}), so d_r(r^d Omega) = O(r^{-1-d}) and
integration from r to infinity gives Omega = r^{-d} a + O(r^{-2d}) uniformly. Splitting the moment as int_{r<1} +
int_{r>1} f_k (Omega - r^{-d} a) + A_phi/(k - k0) continues it with the stated pole. The right side of the first identity
of (a) is holomorphic on kT < Re k < 3, and beta (k0 - kT) = 1 turns the second identity at k0 into
int Theta g_{k0} = int Theta V.grad g_{k0}; taking the limit of beta (k - k0) times the moment at k0 gives (d).
(e) Integrate (T) against g = d_x(x^{-m}) = -m x^{-m-1} on {x > eps, |X| < R}. Since g is homogeneous of degree -m-1,
the bulk coefficient is (2 - m) beta - 2 = -1; int Theta g = -m int x^{1-m} P and int Theta V.grad g = m (m + 1) int x^{1-m} v P.
The outward temperature flux through x = eps (normal (-1, 0)) is +m eps^{2-m} int P(eps, y)(beta + v(eps, y)) dy = O(eps^d)
uniformly in R (P = O((1 + |y|)^{-1-2d}), v bounded, 4.17(a)); on the arc it is
O(R^{3-m} (1 + R)^{-1-2d}) int (cos theta)^{1-m} d theta = O(R^{-d}). The area densities are bounded by C r^{-2-d} (cos theta)^{1-m}
and C r^{-2-2d} (cos theta)^{1-m} at infinity and by C x^{1-m} near the origin and the axis; (cos theta)^{1-m} is integrable
because 1 - m = d - 1 > -1. The limit gives int Theta g = int Theta V.grad g, which is (e). Since v(0) = -c =
-(beta + 2)/2, a0 C_m P < 0 on a small half-ball at the origin, so absolute convergence and the zero integral give
a0 C_m P > 0 elsewhere in D. Independently, |v| <= C(1 + r)^{-d} (4.17(a)) gives C_m -> 1, and 4.10 (A > 0 at an angle
strictly inside the right semicircle after the reflection of 4.8 making a0 > 0) gives a0 P > 0 for all large radii on
a ray strictly inside D.
(f) (i) By parity, c = (2/pi) int_{x, y > 0} x y |X|^{-4} (Omega(x, y) - Omega(x, -y)) dX <= 0, against c = 1 + beta/2. (ii)
c = (1/pi) int int cos theta sin theta Omega d theta dr/r and |Omega| <= |cos theta| min(L_x r, A_x r^{-d}); int_0^{2 pi}
cos^2 theta |sin theta| d theta = 4/3 and int_0^infinity min(L_x r, A_x r^{-d}) dr/r = (1 + beta) L_x^{1/(beta+1)} A_x^{beta/(beta+1)}
(split at R = (A_x/L_x)^{beta/(beta+1)}). Under (A6), L_x -> |l|^{-1} L_x and A_x -> |l|^d A_x.

4.24 Finite angular Fourier support (restricted exclusion, beta >= 2). For a function f on R^2 and an integer
n put f_n(r) = (1/(2 pi)) int_0^{2 pi} f(r e(theta)) e^{-i n theta} d theta; f has finite angular support of degree
at most L if f_n = 0 for every |n| > L and every r > 0.
  (a) No class A profile has a vorticity Omega of finite angular support, and none has a stream function of finite
      angular support (Psi with V = U_rel = (-Psi_y, Psi_x), Psi(0) = 0).
  (b) (the form in which (a) is proved) Let beta >= 2 and 0 < nu <= 1/2. Let Psi, Omega, Theta be smooth on R^2 with
      Omega = -Delta Psi, V = (-Psi_y, Psi_x), V(0) = 0, W = beta X + V, satisfying (V) and (T), with Psi and Omega odd
      and Theta even in x, Psi_xy(0) != 0 and Theta = a0 x^2 + O(|X|^3), a0 != 0, and for large r
        |D^j Omega| <= C r^{-nu-j} (j <= 2),  |Psi| <= C r^{2-nu},  |grad Psi| <= C r^{1-nu},  |Theta| <= C r^{1-2nu}.
      Then Psi and Theta do not both have finite angular support.
  (c) (Fourier division) Let f be smooth with |D^alpha f(X)| <= C_alpha (1 + |X|)^{m-|alpha|} for every multi-index
      alpha, for some real m < 1. If d_x f has finite angular support of degree at most L, L >= 1, then f has finite
      angular support of degree at most L - 1. The derivative bounds cannot be dropped: f = e^{-y^2} - e^{-|X|^2} is
      smooth and bounded, d_x f = 2x e^{-|X|^2} has degree 1, and f has infinitely many angular modes on every circle.
This is a restricted exclusion: it does not exclude class A profiles with infinitely many angular modes, and it gives
no lower bound for the residual of a finite-mode approximation and no obstruction to convergence as the angular degree
tends to infinity. The vorticity representations of section 6 (Omega = x G with G a finite sum of angular modes)
therefore cannot carry an exact class A profile at any fixed angular resolution; this does not explain the residual
levels observed there. The proof uses neither analyticity, nor a sign of Omega or Theta, nor the subclass G.
Proof outline. (a) Class A gives the bounds of (b) with nu = 1/beta: |Omega| and |V| by 4.12(e), |Theta| by 4.10,
|Psi| <= r sup |V| on the segment [0, X], and |D^j Omega| <= C r^{-1/beta-j}, |D^j Theta| <= C r^{1-2/beta-j} for
every j by the uniform C^j bounds of the rescaled fields of step (2) of 4.16 on compact annuli (if
omega(-tau, z) = tau^{-1} Omega(tau^{-beta} z) has bounded D^j on 1/2 <= |z| <= 2, then
|D^j Omega(X)| <= C tau^{1+beta j} at |X| = tau^{-beta}, and likewise for Theta); with smoothness, these bounds take the
global form required in (c). If Omega has degree at most N0, every stream mode with |n| > N0 solves
psi_n'' + psi_n'/r - n^2 psi_n/r^2 = 0, so psi_n = A_n r^{|n|} by smoothness at 0, and |psi_n| <= C r^{2-nu} gives
A_n = 0 for |n| >= 2; reflection removes n = 0. Hence Psi has a finite degree N, and N >= 2 since c != 0. Then
V.grad Omega = r^{-1}(Psi_r Omega_theta - Psi_theta Omega_r) has degree at most 2N and beta r Omega_r + Omega degree at
most N, so Theta_x has degree at most 2N by (V), and (c) with m = 1 - 2/beta gives degree at most 2N - 1 for Theta.
Now (b) applies.
(b) Let N and M be the maximal degrees of Psi and Theta; N >= 2 (Psi_xy(0) != 0) and M >= 2 (a0 != 0). omega_N is not
identically zero (otherwise psi_N = A r^N, excluded by the growth of Psi). The degree M + 1 coefficient of Theta_x is
(theta_M' - M theta_M/r)/2; if M + 1 > 2N it vanishes by (V), so theta_M = C r^M, excluded by the growth of Theta.
Hence M <= 2N - 1. By reality and the reflection parity, psi_N = f and omega_N = g if N is odd, psi_N = i f and
omega_N = i g if N is even, with f, g real and g = -f'' - f'/r + N^2 f/r^2.
Case M + 1 < 2N. The degree 2N coefficient of (V) is a nonzero multiple of (f'g - f g')/r, so f'g - f g' = 0. On a
component of {f != 0}, g = lambda f and f solves the regular equation f'' + f'/r - N^2 f/r^2 + lambda f = 0; a nonzero
solution has only simple zeros, and continuity of g' at such a zero carries the same lambda to the next component, so
g = lambda f on (0, infinity) with one constant. lambda = 0 gives f = A r^N, excluded. For lambda < 0, multiplying by
r f and integrating gives int_0^infinity (r f'^2 + N^2 f^2/r + |lambda| r f^2) dr = 0 (boundary terms O(r^{2N}) at 0
and O(r^{-2 nu}) at infinity, from f = g/lambda and the bounds on Omega). For lambda > 0, E = f'^2 + lambda f^2
satisfies E' >= -(2/r + N^2/(lambda^{1/2} r^2)) E, so E >= c r^{-2} for large r, while f = g/lambda, the bounds on
Omega and its first two derivatives and the equation give f = O(r^{-nu-2}) and f' = O(r^{-nu-1}), so
E = O(r^{-2-2 nu}).
Case M = 2N - 1. Then theta_M = i (-1)^{N+1} h with h real, and the coefficients of degree N + M of (T) and of degree 2N
of (V) are N f h' - M f' h = 0 and 2N (f'g - f g') = r h' - M h. On a component of {h != 0}, f has no zero (otherwise
f = 0 on the component, h = C r^M there, so the component is (0, infinity) and f = 0 everywhere). With
eta = |f|/r^N > 0 (a radial function local to this proof) the first equation gives h = C_h r^M eta^q, q = M/N = 2 - 1/N,
C_h != 0, and the second, divided by eta^2 and integrated once, gives
  eta'' + ((2N + 1)/r) eta' + mu eta + D eta^p = 0,   p = 1 - 1/N,   D = q C_h/2 != 0,
with a constant mu. No infinite tail: if the component reaches infinity, the growth bounds give eta, eta' -> 0. For
D > 0 critical points are strict maxima, eta is eventually decreasing, and integrating
-(r^{2N+1} eta')' >= c r^{2N+1} eta^p over [r/2, r] gives -eta' >= c r eta^p; for D < 0 critical points are strict
minima, eta' < 0 eventually, eta'' >= c eta^p, and integration to infinity gives -eta' >= c eta^{(p+1)/2}. Both force a
zero of eta at a finite radius. No finite endpoint R: smoothness of h = C_h |f|^q, 1 < q < 2, forces f(R) = f'(R) = 0.
The energy E = eta'^2/2 + mu eta^2/2 + D eta^{p+1}/(p+1) has E' = -((2N + 1)/r) eta'^2; for D > 0 it is positive for
small eta > 0 and Gronwall contradicts E(R) = 0. For D < 0, -eta' >= c eta^{(p+1)/2} near R gives eta >= c (R - r)^{2N},
and comparing the lowest Taylor orders of eta'' and D eta^p in the equation shows that the smooth function f/r^N has a
zero of order exactly 2N at R. Then h has a zero of order exactly 4N - 2 and is nonzero just beyond R; on that side the
same equations hold with constants C_+, mu_+, and the Taylor coefficients of order 4N - 2 of h and of order 2N of the
equation give C_+ = C_h and mu_+ = mu. So E is defined with the same constants, vanishes at R and is strictly
decreasing beyond R; it can neither vanish at a later endpoint (where again eta = eta' = 0) nor tend to 0 at infinity.
(c) For k != 0 the Fourier transform of f is smooth (that of Delta^K f is C^j when 2K > m + j + 2). Rotations commute
with the Fourier transform, so on each circle |k| = rho > 0 the function i k_x f^(k) has degree at most L; as a Laurent
polynomial A(z), z = e^{i theta}, it vanishes at z = i and z = -i, so A/cos theta = 2z A/(z^2 + 1) has degrees between
1 - L and L - 1. Hence g = f - Pi f, with Pi the projection onto the angular degrees at most L - 1, has Fourier
transform supported at 0; g is a polynomial with |g| <= C (1 + |X|)^m, m < 1, hence constant, and Pi g = 0 gives g = 0.

4.25 The homogeneous limit is not stationary (class A, beta >= 2). Let (Theta, Omega, U) be a class A profile and let
s, m, a, h, f, u0, b, d be as in 4.16 (k = 2 - s). Then b and d do not both vanish identically. Equivalently, the
homogeneous state (u0, omega0, theta0) of step (1) of 4.16, the locally uniform limit on R^2 \ {0} of the associated
physical solution as t -> 0, does not solve the steady equations u0.grad omega0 = d_x theta0, u0.grad theta0 = 0 on
R^2 \ {0}. In particular no class A profile has Omega = r^{-s} a(theta) and Theta = r^m h(theta) for all large r, nor
Omega - r^{-s} a = o(r^{-2s}) and Theta - r^m h = o(r^{m-s}) uniformly in theta.
If moreover one of the half-axes {x = 0, y > 0}, {x = 0, y < 0} carries no zero of W (the hypothesis of 4.21(a) or
(b); in particular for every profile in G), then d does not vanish identically.
Proof outline. By 4.16, u0r = -f' and u0t = k f, and d_x theta0 = m cos theta h - sin theta h' on the unit circle, so
  d = k f h' - m f' h,   b = k f a' + s f' a - m cos theta h + sin theta h'.
Suppose b = d = 0. Oddness of Omega gives a(pi - theta) = -a(theta), hence f(pi - theta) = -f(theta) by uniqueness of
f, so f(pi/2) = f(-pi/2) = 0. Let J be a component of the open set {f != 0}; it is an open arc not containing +-pi/2,
and its endpoints are zeros of f. On J, d = 0 gives (h |f|^{-m/k})' = 0, so h = C |f|^{m/k} with a constant C, and
then b = 0 can be written
  (|f|^{s/k} a)' = (C m/k) (sin theta sgn(f) |f|^{-1/k})'   (using m + s - k = -1),
so a = (C m/k) sin theta sgn(f) |f|^{-(1+s)/k} + D |f|^{-s/k} on J with a constant D. a is bounded (4.16: a is
smooth). If beta > 2 (m > 0), J has an endpoint theta_e with sin theta_e != 0 (both endpoints in {0, pi} would force
J to contain pi/2 or -pi/2); multiplying by |f|^{(1+s)/k} and letting theta -> theta_e gives C sin theta_e = 0, so
C = 0, and then boundedness of D |f|^{-s/k} gives D = 0. If beta = 2 (m = 0), d = 0 gives h' = 0 on J, and b = 0
reduces to k f a' + s f' a = 0, so a = D |f|^{-s/k}, and D = 0 in the same way. In both cases a = 0 on J. On the
interior of {f = 0}, a = -(f'' + k^2 f) = 0. The union of {f != 0} and the interior of {f = 0} is dense in the
circle, so a = 0 everywhere by continuity, contrary to 4.12 (a is not identically 0). For the consequence on homogeneity: exact
homogeneity outside a ball, or the stated o-bounds, give b = 0 and d = 0 by uniqueness of the expansions of 4.16.
For the half-axis statement, the reflection of 4.8 maps (f, h, d)(theta) to (-f, -h, -d)(-theta) and exchanges the
two half-axes, so we may assume a0 > 0. Let theta_0 = sigma pi/2 (sigma = +1 or -1) be the direction of the half-axis
without zero. By 4.21(a), (b), h(theta_0) = h'(theta_0) = 0, h''(theta_0) = P > 0 and a'(theta_0) = -sigma Q with
Q > 0. Put t = theta - theta_0. Since f(pi - theta) = -f(theta) and h(pi - theta) = h(theta), f is odd and h is even
in t, so d is even in t, and f = e1 t + e3 t^3/6 + O(t^5), h = P t^2/2 + O(t^4). Substitution gives
  d = (k - m/2) e1 P t^2 + O(t^4),   k - m/2 = 3/2.
If d = 0, then e1 = 0; a = -(f'' + k^2 f) gives a'(theta_0) = -e3, so e3 = sigma Q != 0, and then
  d = (2k - 3m) e3 P t^4/12 + O(t^6),   2k - 3m = 1 + 4s > 0,
a contradiction. Only the Taylor expansions of f to order 3 and of h to order 2 at theta_0 are used, and beta = 2
(m = 0) is included.
Scope. A necessary condition on the far field (the second far-field terms of 4.16 cannot both vanish); it does not
exclude any profile with nonzero second terms.
If both half-axes carry zeros of W, the vanishing of d alone is not excluded by this argument (on each component of
{f != 0}, d = 0 means h = C |f|^{m/k} with a constant C depending on the component, and such h can be smooth across
zeros of f of suitable finite or infinite order; for beta = 8, f = cos^5 theta and h = cos^2 theta give d = 0 with
smooth data of the required parities, but a = -(f'' + k^2 f) has a'(+-pi/2) = 0, so these data violate the
conclusion of 4.21 at both vertical directions; whether data with d = 0 arise from a profile is not decided).

4.26 Third far-field terms and the constant velocity (class A, beta > 2). Let (Theta, Omega, U) be a class A profile
with beta > 2 and let s, m, e, e_perp, a, h, b, d, f, g, omega0, theta0, u0, u1 be as in 4.16 (k = 2 - s,
k1 = 2 - 2s, V = U_rel). Put omega1 = r^{-2s} b(theta), theta1 = r^{m-s} d(theta) and
  omega2 = (u0.grad omega1 + u1.grad omega0 - d_x theta1)/2,   theta2 = (u0.grad theta1 + u1.grad theta0)/2,
homogeneous of degrees -3s and m - 2s; on the unit circle
  2 omega2(e) = k f b' + 2s f' b + k1 g a' + s g' a - (m - s) cos theta d + sin theta d',
  2 theta2(e) = k f d' - (m - s) f' d + k1 g h' - m g' h.
(a) In every C^j(S^1), Omega(r e) = omega0 + omega1 + omega2 + o(r^{-3s}) and
Theta(r e) = theta0 + theta1 + theta2 + o(r^{m-2s}).
(b) Let 2 < beta < 3 and eta = Omega - omega0 - omega1. Then |eta(y)| <= c0 |y|^{-2s} for 0 < |y| <= 1 and
|eta(y)| <= c0 |y|^{-3s} for |y| >= 1 with a constant c0, the vertical constant C = (0, C2),
  C2 = -(1/(2 pi)) int (y1/|y|^2) eta(y) dy,
is an absolutely convergent integral, the ordinary Biot-Savart integral u2 of omega2 (absolutely convergent off 0)
is u2(r e) = r^{1-3s}[-f2' e + k2 f2 e_perp] with k2 = 2 - 3s and -(f2'' + k2^2 f2) = omega2(e), and, in every
C^j(S^1),
  V(r e) = u0 + u1 + C + u2 + o(r^{1-3s}),
  Omega(r e) = omega0 + omega1 + omega2 + (C.grad omega0)/beta + o(r^{-1-s}),
  Theta(r e) = theta0 + theta1 + theta2 + (C.grad theta0)/beta + o(r^{m-1}).
If C != 0, neither C.grad omega0 nor C.grad theta0 vanishes identically.
(c) Let 2 < beta < 3. If, outside a ball, Omega is a finite sum of terms r^{-s-js-2n} c_{jn}(theta) (j, n nonnegative
integers) up to o(r^{-1-s}) in every C^j(S^1), as for the radial representation of section 6.1 with basis exponent
b_rep = beta, then C = 0.
(d) (Noninteger beta > 2, under stated expansions.) Let beta > 2 be noninteger and N = floor(beta), and suppose that,
uniformly in theta,
  Omega(r e) = sum_{l=1}^{N+1} r^{-ls} a_l(theta) + O_1(r^{-(N+2)s}),
  Theta(r e) = sum_{j=0}^{N-1} r^{1-(j+2)s} f_j(theta) + O_1(r^{1-(N+2)s}),
with smooth a_l, f_j and a_1 = a; here O_1(r^{-sigma}) denotes a function bounded by M r^{-sigma} for large r whose
Cartesian gradient is bounded by M r^{-sigma-1}. For l <= N let u_{l-1} be the velocity of the stream function
r^{2-ls} g_l(theta) with -(g_l'' + (2 - ls)^2 g_l) = a_l (uniquely solvable since 1 < 2 - ls < 2; u_0 = u0 and
u_1 = u1). Then V(r e) = sum_{l<=N} u_{l-1} + C + O(r^{1-(N+1)s}) with a constant C = (0, C2), and C = 0. For 2 < beta < 3 this C is
the constant of (b). Consequently, for every noninteger beta > 2, a radial representation as in (c), stored with basis
exponent b_rep = beta, whose Omega and Theta have exactly these expansions outside a ball, can be the field of a class A
profile only if its own constant C vanishes.
Proof outline. (a) With the rescaled fields of step (1) of 4.16 (t = -tau), d_tau omega = u.grad omega - d_x theta and
d_tau theta = u.grad theta. By 4.16 and 4.16(a), u = u0 + tau u1 + o(tau), omega = omega0 + tau omega1 + o(tau) and
theta = theta0 + tau theta1 + o(tau) in every C^j on compact subsets of R^2 \ {0}, so the right sides are
omega1 + tau(u0.grad omega1 + u1.grad omega0 - d_x theta1) + o(tau) and theta1 + tau(u0.grad theta1 + u1.grad theta0) +
o(tau); integration from 0 to tau gives omega = omega0 + tau omega1 + tau^2 omega2 + o(tau^2) and the same for theta,
and tau = r^{-s} gives (a). The angular formulas follow from u0r = -r^{1-s} f', u0t = k r^{1-s} f,
u1r = -r^{1-2s} g' and u1t = k1 r^{1-2s} g. No time derivative of the velocity is used.
(b) Now 1/3 < s < 1/2, so 2s < 1 < 3s. The bounds on eta follow from smoothness at 0 and from (a). Hence
U_eta(x) = int K(x - y) eta(y) dy, K(z) = (z2, -z1)/(2 pi |z|^2), converges absolutely for every x, including x = 0,
and since u0 and u1 are the canonical inverses of omega0 and omega1 (4.16), V = u0 + u1 + U_eta - U_eta(0) exactly;
C = -U_eta(0), whose first component vanishes by the parity of eta. Splitting the integral over |y| < r/2,
r/2 <= |y| <= 2r and |y| > 2r gives U_eta = O(r^{1-3s}). With eta_R(y) = R^{3s} eta(R y), |eta_R(y)| <= c0 |y|^{-3s}
for R >= 1 and eta_R -> omega2 locally smoothly off 0 by (a), so R^{3s-1} U_eta(R x) -> u2(x) uniformly on compact
annuli by dominated convergence, and in every C^j by interior estimates for the div-curl system; u2 is homogeneous of
degree 1 - 3s and equals the angular formula (k2 is not an integer; the difference is an entire harmonic field, the
boundary terms at 0 being O(eps^{2-3s}), and it decays at infinity). In rescaled variables
u = u0 + tau u1 + tau^{beta-1} C + tau^2 u2 + o(tau^2) with 1 < beta - 1 < 2. Inserted with the expansions of (a)
into the transport equations, every other product is O(tau^2) = o(tau^{beta-1}), so
d_tau omega = omega1 + 2 tau omega2 + tau^{beta-1} C.grad omega0 + o(tau^{beta-1}) and the same for theta (with
C.grad theta0); integration gives the terms tau^beta (C.grad omega0)/beta and tau^beta (C.grad theta0)/beta, which are
the displayed terms of degrees -1 - s and m - 1. If C != 0 and C.grad theta0 = 0, theta0 depends only on x in each
half-plane, so theta0 = c_+ x^m on {x > 0} and c_- |x|^m on {x < 0}, which is not C^1 across the axis off 0 unless
c_+ = c_- = 0 (0 < m < 1), contradicting h != 0; in the same way C.grad omega0 = 0 would give omega0 = c_+- |x|^{-s},
contradicting continuity across the axis unless a = 0.
(c) Since 3s > 1, the exponents s + js + 2n not larger than 1 + s are s, 2s and 3s (n = 0, j <= 2), and 1 + s is
not among them (js = 1 would need j = beta). So Omega(r e) = c_00 r^{-s} + c_10 r^{-2s} + c_20 r^{-3s} + o(r^{-1-s});
comparing with (b) term by term (uniqueness of such expansions), the homogeneous term (C.grad omega0)/beta of degree
-1 - s is o(r^{-1-s}), hence 0, and C = 0 by the last sentence of (b). In the representation of section 6.1,
outside the last radial knot Omega = x G with G a finite sum of angular modes, each the product of (1 - t)^{b_rep+1},
for odd indices the factor r (L^2 + r^2)^{-1/2}, and a polynomial in z = 1 - t = (L^2/(L^2 + r^2))^{1/(2 b_rep)}; since
z^{b_rep} = L (L^2 + r^2)^{-1/2}, expansion in r^{-2} gives exactly the exponents s + js + 2n when b_rep = beta.
(d) Put eta = Omega - sum_{l<=N} r^{-ls} a_l. Since Ns < 1 < (N + 1)s < 2, eta = O(1 + r^{-Ns}) near 0 and
O(r^{-(N+1)s}) at infinity, so its Biot-Savart velocity U_eta converges absolutely at every point, is continuous at
0, and is O(r^{1-(N+1)s}) by the splitting of (b); no derivative bound on the remainder is used here. The homogeneous
streams have degree 2 - ks > 1, so their Laplacians carry no mass at 0 and their velocities vanish continuously
there; two sublinear velocities with the same curl and divergence differ by a constant (harmonic derivative
estimates), so V = sum u_{l-1} + U_eta - U_eta(0), C = -U_eta(0), and C1 = 0 by parity. In the vorticity equation,
(beta X.grad + 1)(r^{-ls} a_l) = (1 - l) r^{-ls} a_l, and d_x Theta and the products u_{j-1}.grad(r^{-ls} a_l), of
degree -(j + l)s, give only powers r^{-ns} with n <= N + 1, up to O(r^{-(N+2)s}) (this uses the O_1 bounds); the C
term is C.grad(r^{-s} a) + O(r^{-1-2s}). Since beta is not an integer, 1 + s is not a multiple of s, and
(N + 1)s < 1 + s < (N + 2)s and 1 + s < 1 + 2s. Comparing coefficients gives C.grad(r^{-s} a) = 0 on R^2 \ {0}, and
the last argument of (b) gives C = 0. The representation statement follows because, for b_rep = beta, the expansion of
the stored fields in r^{-2} (as in (c)) has exactly these exponents, with convergent, termwise differentiable series.
Scope. Necessary asymptotics of a hypothetical profile; they neither exclude nor construct one. Whether C vanishes,
and whether omega2 or theta2 vanish, is not decided; (b) and (c) are restricted to 2 < beta < 3 (at beta = 3 the
constant and the third velocity term have the same degree and a logarithm can occur, see 4.27); for noninteger
beta > 3 the vanishing conclusion C = 0 under the pure-ladder expansions displayed in (d) is available only in that
conditional form, while (a) holds for every beta > 2. (d) is an implication from the displayed expansions, which for
beta > 3 are hypotheses, not derived from class A; it excludes only fields with these expansions whose constant C is
nonzero, and no profile outside them. It is not an exclusion of the expansion class: with lambda =
(1 - s)(3 - s), chi a smooth radial cutoff (0 for r <= 1, 1 for r >= 2), Psi = chi(r) x r^{1-s}, Omega = -Lap Psi,
V = (-Psi_y, Psi_x), F = (beta X + V).grad Omega + Omega and Theta(x, y) = Theta_inf(-3, y) + int_{-3}^x F(t, y) dt,
Theta_inf = -(lambda/s) y r^{-2s}, the fields are smooth with the B2 parities, V(0) = 0, V is sublinear, (V) holds on
R^2 by construction, and outside r = 2 one has Omega = -lambda x r^{-1-s}, V = u0 and Theta = Theta_inf (the
horizontal integration path from x = -3 stays outside r = 2 for exterior points with x < 0, and Theta is even in x);
so the expansions hold with a_1 = -lambda cos theta, f_0 = -(lambda/s) sin theta, all other coefficients and the
remainders zero outside r = 2, and C = 0. This field does not satisfy (T) and is not a profile. At integer beta the argument fails:
1 + s = (beta + 1)s lies on the ladder, and the stream of degree 1 is resonant (4.27 for beta = 3).
The condition C = 0 of (c) concerns that family of representations only.
4.27 The resonance at beta = 3 (class A). Let (Theta, Omega, U) be a class A profile with beta = 3, so s = m = 1/3,
and let omega0, theta0, u0, u1, omega1, theta1, omega2, theta2 be as in 4.26 (V = U_rel). Write
omega2(r e) = r^{-1} A2(theta) and alpha = (1/pi) int_0^{2 pi} A2(theta) cos theta dtheta (A2 is odd in x, so its mean
and its sin theta coefficient vanish). Let g2 be the smooth periodic solution of -(g2'' + g2) = A2 - alpha cos theta
orthogonal to cos theta and sin theta, and put
  B(theta) = -g2' e + g2 e_perp + (alpha/2)(cos theta sin theta, -cos^2 theta).
(a) There is a real constant C such that, with w2(r e) = -(alpha/2)(log r)(0, 1) + B(theta) + (0, C), in every
C^j(S^1)
  V(r e) = u0 + u1 + w2 + O(r^{-1/3} log r),
  Omega(r e) = omega0 + omega1 + omega2 + O(r^{-4/3} log r),   Theta(r e) = theta0 + theta1 + theta2 + O(r^{-2/3} log r).
For a smooth radial chi with chi = 0 on r <= 1 and chi = 1 on r >= 2, put
L_chi = lim_{R -> infinity} (int_0^R chi(rho)/rho drho - log R) and zeta = Omega - omega0 - omega1 - chi r^{-1} A2;
then
  C = alpha (1/4 - L_chi/2) - (1/(2 pi)) int (y1/|y|^2) zeta(y) dy,
an absolutely convergent integral, and C does not depend on chi.
(b) Put
  Q_omega = w2.grad omega0 + u1.grad omega1 + u0.grad omega2 - d_x theta2,
  Q_theta = w2.grad theta0 + u1.grad theta1 + u0.grad theta2,
  omega3 = Q_omega/3 - (alpha/6) d_y omega0,   theta3 = Q_theta/3 - (alpha/6) d_y theta0.
Then, in every C^j(S^1),
  Omega(r e) = omega0 + omega1 + omega2 + omega3 + O(r^{-5/3} log r),
  Theta(r e) = theta0 + theta1 + theta2 + theta3 + O(r^{-1} log r),
where omega3 (theta3) is the sum of a term homogeneous of degree -4/3 (-2/3) and the logarithmic term
-(alpha/6)(log r) d_y omega0 (-(alpha/6)(log r) d_y theta0). If alpha != 0, both logarithmic terms are nonzero.
(c) If, outside a ball, Omega is a finite sum of terms r^{-(1+j)/3-2n} c_jn(theta) (j, n nonnegative integers) up to
o(r^{-4/3}) in C^0(S^1), as for the radial representation of section 6.1 with basis exponent b_rep = 3 (the expansion is
described there), then alpha = 0.
(d) Positivity and reflection parity of the leading data do not force alpha to vanish or fix its sign: for omega0 = r^{-1/3} p cos theta and
theta0 = r^{1/3} cos^2 theta (q + c sin theta) with constants p > 0 and q > |c| (so omega0 > 0 on {x > 0} and
theta0 > 0 off the axis), the formulas of 4.16 and 4.26 give alpha = -3p(27p^2 - 41c)/320, which vanishes for
p = q = 1, c = 27/41 and takes both signs. These data are not shown to be the tails of any profile.
Proof outline. (a) By smoothness at 0 and 4.26(a) (whose proof gives the rescaled expansions in every C^j on compact
subsets of R^2 \ {0}), eta = Omega - omega0 - omega1 satisfies |eta(y)| <= c0 min(|y|^{-2/3}, |y|^{-1}). With
the rescaled fields of step (1) of 4.16 (u_tau = tau^2 V(tau^{-3} z), omega_tau = tau^{-1} Omega(tau^{-3} z),
theta_tau = tau Theta(tau^{-3} z), t = -tau) this reads
|omega_tau - omega0 - tau omega1| <= c0 min(tau |z|^{-2/3}, tau^2 |z|^{-1}). In the relative inverse of this difference,
on a compact annulus, every part is O(tau^2) except the subtracted kernel near 0, which contributes at most
int_0^1 min(tau rho^{-2/3}, tau^2 rho^{-1}) drho <= c0 tau^2 (1 + |log tau|) (split at rho = tau^3); so
u_tau = u0 + tau u1 + O(tau^2 (1 + |log tau|)), in every C^j by interior estimates for the div-curl system. Inserted
with 4.26(a) into d_tau omega_tau = u_tau.grad omega_tau - d_x theta_tau and d_tau theta_tau = u_tau.grad theta_tau,
this gives right sides omega1 + 2 tau omega2 and theta1 + 2 tau theta2 up to O(tau^2 (1 + |log tau|)); integration
from 0 gives the scalar expansions of (a). Hence zeta = O(r^{-4/3} log r) at infinity and O(r^{-2/3}) near 0, so
U_zeta(x) = int K(x - y) zeta(y) dy converges absolutely for every x, including 0, and U_zeta(r e) = O(r^{-1/3} log r)
(split of the integral over |y| < r/2, r/2 <= |y| <= 2r and |y| > 2r; derivatives by interior estimates). The cutoff
source chi r^{-1} A2 is inverted mode by mode: the cos theta stream coefficient
  P1(r) = (alpha/2)(r^{-1} int_0^r rho chi drho - r int_0^r chi/rho drho)
is regular with zero linear term at 0 and equals -(alpha/2) r log r + alpha (1/4 - L_chi/2) r + O(r^{-1}) for r >= 2,
and the other modes have the exterior stream r g2(theta) plus decaying homogeneous terms; this mode solution grows like
log r and vanishes at 0, so it is the canonical relative inverse (a harmonic field of sublinear growth is constant).
Since u0 and u1 are the canonical inverses of omega0 and omega1, V = u0 + u1 + (mode solution) + U_zeta - U_zeta(0),
which gives the velocity expansion with the stated C (the second component of U_zeta(0) is
(1/(2 pi)) int (y1/|y|^2) zeta, the first vanishes by parity). A compactly supported change delta chi changes L_chi by
int delta chi/rho and that component by -(alpha/2) int delta chi/rho, so C does not change.
(b) Since w2(lambda z) = w2(z) - (alpha/2)(log lambda)(0, 1), (a) reads
u_tau = u0 + tau u1 + tau^2 (w2 + (3 alpha/2)(log tau)(0, 1)) + O(tau^3 (1 + |log tau|)). In the transport equations
the orders tau^0 and tau^1 give omega1, 2 omega2 (theta1, 2 theta2), the order tau^2 gives
Q_omega + (3 alpha/2)(log tau) d_y omega0 (and the same with theta), and all other products are
O(tau^3 (1 + |log tau|)). Integration with int_0^tau t^2 log t dt = tau^3 (log tau/3 - 1/9) and tau = r^{-1/3} gives
(b); the term (alpha/2)(log tau) d_y omega0 is the logarithmic part of Q_omega/3. As a check, with
L_omega = 3 X.grad + 1 and L_theta = 3 X.grad - 1, L_omega omega3 = -Q_omega and L_theta theta3 = -Q_theta, the
next-order parts of (V) and (T). If d_y theta0 = 0, theta0 = c_+ x^{1/3} on {x > 0} and c_- |x|^{1/3} on {x < 0},
which is not C^1 across the axis off 0 unless theta0 = 0; in the same way d_y omega0 = 0 would force omega0 = 0.
(c) The exponents (1 + j)/3 + 2n not larger than 4/3 are 1/3, 2/3, 1 and 4/3 (n = 0) and carry no logarithm;
comparison with (b) at the order r^{-4/3} log r gives alpha d_y omega0 = 0, hence alpha = 0.
(d) Finite Fourier computation: u0 has stream -(9p/16) r^{5/3} cos theta, omega1 and theta1 follow from 4.16, the
stream r^{4/3} g of u1 solves -(g'' + (16/9) g) = r^{2/3} omega1 term by term, and alpha is the cos theta coefficient of
r omega2 from 4.26; the result was checked symbolically.
Scope. Necessary asymptotics of a hypothetical profile at beta = 3; they neither exclude nor construct one. Whether
alpha vanishes for a profile is not decided, and (d) shows that sign and parity conditions on the leading data do not
decide it. No expansion to all orders is claimed. The condition alpha = 0 of (c) concerns that family of
representations only.

4.28 Center Taylor conditions of (V) (beta > 2). Notation: R_Omega = W.grad Omega + Omega - Theta_x, U = (-Psi_y,
Psi_x), Omega = -Lap Psi, lambda1 = (beta - 2)/2, lambda2 = 1 + 3 beta/2, c = Psi_xy(0), Lambda and M as in 4.13; for
f smooth at 0, f_n is its homogeneous Taylor part of degree n at 0, and P_n^odd is the space of homogeneous
polynomials of degree n that are odd in x. The example of 4.13 is written Psi^e, Omega^e, U^e.
(a) Formal structure. Let beta > 2 and a0 != 0. Let Psi be smooth near 0, odd in x, with c = 1 + beta/2, and let Theta
be a smooth solution of (T) near 0 with Theta = a0 x^2 + O(|X|^3). Then A := DW(0) = diag(lambda1, lambda2), and for
every n >= 1
  (R_Omega)_n = (A X.grad + 1) Omega_n + N_n,
where N_n is a polynomial in a0 and the coefficients of Psi_3, ..., Psi_{n+1} (it does not involve Psi_m for m >= n +
2). The operator A X.grad + 1 multiplies x^i y^j by i lambda1 + j lambda2 + 1 >= 1 and is invertible on each P_n^odd.
The map -Lap : P_{n+2}^odd -> P_n^odd is onto, with one-dimensional kernel spanned by the harmonic polynomial h_{n+2}
= Re (x + i y)^{n+2} if n is odd and Im (x + i y)^{n+2} if n is even. Consequently:
(i) (R_Omega)_1 = 0 is the identity Omega_x(0) = 4 a0/beta of 4.1, and (R_Omega)_2 = 0 is the second condition of
4.13(vii) (A X.grad + 1 acts on x y by lambda1 + lambda2 + 1 = M);
(ii) R_Omega vanishes to order N at 0 (that is, (R_Omega)_n = 0 for n <= N) if and only if Omega_n = -(A X.grad +
1)^{-1} N_n for 1 <= n <= N, and then Psi_{n+2} is determined by Psi_3, ..., Psi_{n+1} up to an arbitrary multiple of
h_{n+2};
(iii) for every a0 != 0, every Psi_3 in P_3^odd with -Lap Psi_3 = (4 a0/beta) x, every sequence of real numbers
(eta_m)_{m >= 4} and every choice of complements V_m of span(h_m) in P_m^odd, there is exactly one formal series Psi =
c x y + Psi_3 + sum_{m >= 4} Psi_m, odd in x, with Psi_m - eta_m h_m in V_m for m >= 4, for which the formal series of
R_Omega vanishes. So the Taylor conditions of (V) at the center determine the Taylor series of Omega from a0 and the
harmonic coordinates of Psi, and impose no condition on those coordinates. (A linear term l x of Psi changes only U(0)
and does not enter W.)
(b) Realization. For every beta > 2 and a0 > 0 there are smooth Psi, Omega = -Lap Psi, Theta with the B2 parity such
that: (T) holds on R^2, Theta >= 0, Theta > 0 off the y-axis, Theta = a0 x^2 + O(|X|^3) and |Theta| <= C (1 +
|X|)^{2(beta - 2)/beta}; Omega > 0 on {x > 0}; U - U(0) is the canonical inverse of Omega (A4), c = 1 + beta/2 and
Omega_x(0) = 4 a0/beta; Omega and U coincide outside a compact set with Omega^e and U^e (so U = O(r^{1-1/beta}), DU =
O(r^{-1/beta}), and Omega has a nonzero r^{-1/beta} tail); the whole plane is the backward basin of the source at 0;
and R_Omega vanishes to infinite order at 0 (all its derivatives vanish at 0).
Proof outline. (a) By parity Psi_xx(0) = Psi_yy(0) = 0, so A = diag(beta - c, beta + c) = diag(lambda1, lambda2). By
4.3(ii) Theta is determined near 0 by its 2-jet; its Taylor series satisfies the formal form of (T), whose degree-m
part (m >= 3) reads (A X.grad - 2 lambda1) Theta_m + sum_{k=2}^{m-1} W_k.grad Theta_{m+1-k} = 0, with W_k = (-d_y
Psi_{k+1}, d_x Psi_{k+1}). On x^i y^j with i + j >= 3 the factor i lambda1 + j lambda2 - 2 lambda1 is positive (it is
(i - 2) lambda1 >= lambda1 if j = 0 and at least lambda2 - 2 lambda1 = 3 + beta/2 if j >= 1), so Theta_m is determined
by a0 and Psi_3, ..., Psi_m, and is even in x. In (R_Omega)_n = sum_{k=1}^{n} W_k.grad Omega_{n+1-k} + Omega_n - d_x
Theta_{n+1}, the term k = 1 is A X.grad Omega_n; the terms k >= 2 involve W_k (from Psi_{k+1}, k + 1 <= n + 1) and
Omega_{n+1-k} = -Lap Psi_{n+3-k} (n + 3 - k <= n + 1); and Theta_{n+1} involves Psi_3, ..., Psi_{n+1}. This gives the
displayed form. Lap maps P_{n+2} onto P_n with kernel spanned by Re and Im (x + i y)^{n+2} and commutes with x -> -x,
so it maps P_{n+2}^odd onto P_n^odd (dim P_{n+2}^odd = dim P_n^odd + 1); exactly one of Re, Im (x + i y)^{n+2} is odd
in x, namely Re for n + 2 odd and Im for n + 2 even. (i) For n = 1, N_1 = -d_x Theta_2 = -2 a0 x and Omega_1 =
Omega_x(0) x, which gives (lambda1 + 1) Omega_x(0) = 2 a0. For n = 2, (R_Omega)_2 is a multiple of x y and equals [M
q'(0) - b''(0)(q(0) + 8 a0/Lambda)] x y in the notation of 4.13, using a'(0) = 4 b''(0) a0/Lambda. (ii) and (iii)
follow by induction on n: with P_m^odd = V_m + span(h_m), -Lap is an isomorphism from V_m onto P_{m-2}^odd, so at
stage m the residual determines the V_m-component of Psi_m and eta_m h_m supplies the rest; the recursion of the
Theta_m involves only already determined coefficients. No convergence is claimed.
(b) Start from the example. Its Taylor parts of degree <= 3 satisfy c = 1 + beta/2 and Omega^e_x(0) = 4 a0/beta; it
has the linear term l x, l = Psi^e_x(0) = -B (L^2 + h^2)^p. Take V_m spanned by the odd monomials x^i y^{m-i} other
than x^m (m odd) or x^{m-1} y (m even); these are complements, since the corresponding coefficients of h_m are 1 and
m. By (a)(iii) applied to Psi^e - l x, with eta_m the h_m-coordinate of Psi^e_m relative to V_m, there is a formal
series Psi* agreeing with Psi^e - l x up to degree 3 whose R_Omega vanishes formally; put D_m = Psi*_m - Psi^e_m in
P_m^odd (m >= 4). Let chi be a smooth radial cutoff, chi = 1 on |X| <= 1 and chi = 0 on |X| >= 2, and choose 0 < eps_m
<= 1 with ||chi(./eps_m) D_m||_{C^{m-1}} <= 2^{-m} eta (possible since ||chi(./eps) D_m||_{C^k} <= C_{k,m} eps^{m-k}
for k < m). Then delta = sum_{m >= 4} chi(./eps_m) D_m converges in every C^k, is smooth, odd in x, supported in |X|
<= 2, has Taylor series sum D_m at 0, and ||delta||_{C^3} <= eta. Put Psi = Psi^e + delta. Since delta has compact
support and vanishes to order 4 at 0, U - U(0) = U^e - U^e(0) + grad^perp delta is divergence free, sublinear, with
-curl U = Omega, hence the canonical inverse of Omega (A4), and c and Omega_x(0) are unchanged. Positivity: Omega^e/x
= 4Bp S^{p-2}[2L^2 + (p + 1)(x^2 + (y - h)^2)] is at least some c0 > 0 on |X| <= 2; Lap delta is odd in x and |d_x Lap
delta| <= 2 ||delta||_{C^3} <= 2 eta, so |Lap delta/x| <= 2 eta and Omega/x >= c0 - 2 eta > 0 on {x > 0, |X| <= 2} for
eta < c0/2; outside, Omega = Omega^e. Basin: in 4.13, W_1/x >= lambda1 and b' >= lambda1; the perturbations of W_1/x
(by -delta_y/x) and of b' (by delta_xy(0, y)) are bounded by ||delta||_{C^2} <= eta. Take eta < min(c0/2, lambda1/2)
and gamma = lambda1 - eta. Then W_1/x >= gamma on R^2 and b' >= gamma on R; DU is bounded, so the flow is complete;
along a backward orbit |x(t)| <= |x(0)| e^{-gamma t}, and since b(0) = 0 gives y b(y) >= gamma y^2 and |W_2(x, y) -
b(y)| <= C |x| (Psi_xx bounded), D^+|y(t)| <= -gamma |y(t)| + C |x(0)| e^{-gamma t}, so |y(t)| <= e^{-gamma t}(|y(0)| +
C |x(0)| t) -> 0. DW(0) is unchanged, and with W_1 = x (lambda1 + beta_1), beta_1(0) = 0, the backward flow and all
its spatial derivatives decay exponentially on a small backward-invariant neighbourhood of 0, so I(X) = int_0^infty
beta_1(phi_{-s} X) ds converges there in every C^k; xi = x e^{-I} is smooth, odd in x, solves W.grad xi = lambda1 xi
with xi = x + O(|X|^2), and extends to R^2 by xi = e^{lambda1 t} xi o phi_{-t}; Theta = a0 xi^2 solves (T) on R^2, is
even in x, vanishes exactly on the axis and has the jet a0 x^2. Sublinearity gives X.W >= (beta/2)|X|^2 for |X| >= R0,
so a backward orbit from radius r enters the ball of radius R0 within time (2/beta) log(r/R0), and transport gives the
polynomial bound on Theta. Finally the Taylor series of Psi - l x at 0 is Psi*, the Taylor series of Theta is the
formal solution of (T) for Psi* (uniqueness in the recursion of (a)), so the Taylor series of R_Omega is the formal
R_Omega of Psi*, which vanishes.
Scope. (b) gives configurations, not profiles: (T) holds exactly, with the parity, positivity, the center data, the
canonical inverse, the slow tail and every Taylor condition of (V) at the center, but R_Omega is not claimed to vanish
away from 0. The unchanged example of 4.13 is excluded by its nonzero degree-two residual; but no condition on the
Taylor coefficients of R_Omega at the center, of any order (such as 4.13(vii)), together with the other listed
properties, can exclude the class of positive-vorticity configurations that it represents. The formal center equations
with freely prescribed harmonic coordinates give no obstruction; for a profile, those coordinates (relative to fixed
complements) are determined by the global vorticity through the canonical inverse. This does not establish solvability
of (V) on a neighbourhood of 0, along the axis, or globally; the stronger realizations of 4.29 to 4.31 and 4.34 are
collected in the compatibility summary after 4.31. The particular configurations of (b) are not profiles: outside a
compact set they agree with the example, and there d_x R_Omega(0, .) vanishes on no open interval of the axis. Indeed,
with H = b q' + (M - b') q and F = b H' - (2b' - Lambda) H, the axis system 4.13(i) and b a' = (2b' - Lambda) a force
F = 0, while for the example F_e is real analytic on R with F_e'(0) = (Lambda/2) M q_e'(0) > 0 (119/15 at beta = 4,
a0 = 1).

4.29 Realizations near the center and along the axis (beta > 2). Notation as in 4.13 and 4.28; b(y) = W_2(0, y), a(y)
= Theta_xx(0, y)/2, q(y) = Omega_x(0, y), q0 = 4 a0/beta, l = Psi^e_x(0), q^e = Omega^e_x(0, .), s = 2p = 1 - 1/beta
and Q_e = 4 B p (p + 1). A configuration is a triple of smooth Psi, odd in x, Omega = -Lap Psi and Theta, even in x
and vanishing on the axis, solving (T) on R^2, with the center data Theta = a0 x^2 + O(|X|^3), a0 != 0, and Psi_xy(0)
= c = 1 + beta/2 of 4.1, where U = (-Psi_y, Psi_x) and W = beta X + U - U(0). For every configuration
  d_x R_Omega(0, y) = b q' + (M - b') q - 2a   (y in R),
so the second axis equation of 4.13(i) says exactly that R_Omega vanishes to first order in x on the axis. Moreover b
= beta y + g1 - g1(0) and q = -(g1'' + 6 g3), where g1 = Psi_x(0, .) and g3 = Psi_xxx(0, .)/6, and b a' = (2b' -
Lambda) a; since 2b'(0) = Lambda, a = a0 exp(int_0^y (2b' - Lambda)/b) near 0, and on R if b has no zero other than 0.
(a) Exact polynomial solution. P = l x + c x y - (q0/6) x^3 with Theta = a0 x^2 solves (T) and (V) on R^2, with Omega
= q0 x and W = (lambda1 x, lambda2 y - q0 x^2/2), and P is the cubic Taylor polynomial of Psi^e at 0. P is the
polynomial solution of 6.2; it is not a profile (U is not o(|X|)).
(b) Exactness on a small disk. For every beta > 2 and a0 > 0 there are rho > 0 and a configuration with all properties
of 4.28(b) for which R_Omega = 0 on |X| < rho; there Psi = P, Theta = a0 x^2 and Omega = q0 x.
(c) Finite axis segments. For every beta > 2, a0 > 0 and Y0 > 0 there is a configuration with all properties of
4.28(b) for which every derivative of R_Omega vanishes at every point (0, y) with |y| <= Y0; it can be chosen with g1
= g1^e (so b = b^e), or so that, in addition, R_Omega = 0 on a disk |X| < rho as in (b); not both, since Psi = P on a
disk makes g1 affine on an axis interval, while g1^e is real analytic with (g1^e)'''(0) = -2 B (beta^2 - 1) h L^2 (L^2 +
h^2)^{p-3}/beta^2 < 0.
(d) Obstruction for compact modifications. Let a configuration with a0 > 0 have Theta = a0 xi^2, with xi as in 4.28(b)
for its own W (whole-plane backward basin; then a = a0 xi_x(0, .)^2 > 0 on R), let U - U(0) be the canonical inverse
of Omega (A4), and let Omega - Omega^e have compact support (this holds in particular if Omega and U coincide with
Omega^e and U^e outside a compact set). Then
  b q' + (M - b') q = -2 B Q_e |y|^{-1-2/beta} (1 + o(1))   as y -> -infinity,
so d_x R_Omega(0, y) < 0 for all sufficiently negative y, and (V) does not hold to first order in x on the whole axis.
If moreover Psi - Psi^e has compact support and vanishes to order 3 at 0 (as for the configurations of 4.28(b) and of
(b), (c)), then d_x R_Omega(0, .) vanishes on no open interval of the axis outside that support.
(e) The whole axis. For every beta > 2 and a0 > 0 there is a configuration with all properties of 4.28(b) except
agreement with the example outside a compact set, which is replaced by: Omega - Omega^e vanishes outside a strip |x|
<= x0 and is bounded by C |x| (1 + |y|)^{-1-1/beta}, and |U - U^e| <= C (1 + |y|)^{-1-1/beta} (so U = O(r^{1-1/beta}),
DU = O(r^{-1/beta}), and the leading r^{-1/beta} tail of Omega is that of the example, uniformly in theta); and such
that d_x R_Omega(0, y) = 0 for every y in R. In it b = b^e (single zero 0, b' >= lambda1), a = a^e, and q is the
unique solution Q of b q' + (M - b') q = 2a that is bounded at 0; Q > 0 on R, and Q/q^e has finite positive limits as
y -> +-infinity.
Proof outline. The identity is the x coefficient computation in the proof of 4.13(i); it uses only div W = 2 beta and
the parity (checked symbolically for Psi = x g1 + x^3 g3 + x^5 g5 and Theta = a2 x^2 + a4 x^4 with arbitrary functions
of y).
(a) Direct substitution: W.grad Theta = 2 lambda1 Theta and (W.grad + 1)(q0 x) = (lambda1 + 1) q0 x = 2 a0 x =
Theta_x. With g1^e = Psi^e_x(0, .) = -B (L^2 + (y - h)^2)^p one has (g1^e)''(0) = -2 B p (L^2 + h^2)^{p-2} [L^2 +
(2p - 1) h^2] = 0, since 2p - 1 = -1/beta and h^2 = beta L^2; so the cubic part of Psi^e is a multiple of x^3, equal to
-(q0/6) x^3 because Omega^e_x(0) = q0, and the parts of degree 1 and 2 are l x + c x y (exact rational checks at
(beta, a0) = (4, 1) and (3, 7/10)).
(b) Put Psi = Psi^e + chi(X/rho)(P - Psi^e), chi as in 4.28(b). Since P - Psi^e vanishes to order 4 at 0,
||chi(./rho)(P - Psi^e)||_{C^k} <= C rho^{4-k} for k <= 3, so for small rho positivity (Omega/x >= m0 - C rho with m0
the minimum of Omega^e/x on a fixed ball), the canonical inverse, the center data, the exterior agreement and the
margins W_1/x >= lambda1/2, b' >= lambda1/2 follow as in 4.28(b), and so do the basin, xi and Theta = a0 xi^2. On |X|
< rho, X.W = lambda1 x^2 + lambda2 y^2 - (q0/2) x^2 y >= (lambda1 - q0 rho/2) |X|^2, so for rho <= lambda1/q0 the disk
is backward invariant and x(t) = e^{-lambda1 t} x(0) along backward orbits in it; hence xi = x and Theta = a0 x^2
there, and (a) gives (T) and (V) on the disk.
(c) Write the Taylor expansions in x along the axis as Psi ~ sum x^n g_n(y), Omega ~ sum x^n w_n(y) (n odd) and Theta
~ sum x^{2m} a_{2m}(y) (m >= 1, a_2 = a). Then w_n = -g_n'' - (n + 1)(n + 2) g_{n+2}; b a_{2m}' + (2m (2 beta - b') -
2 lambda1) a_{2m} is a polynomial in g_3, ..., g_{2m-1}, a_2, ..., a_{2m-2} and their first derivatives; and the x^n
coefficient of R_Omega on the axis is
  r_n = b w_n' + (n (2 beta - b') + 1) w_n + G_n - (n + 1) a_{n+1}
(n = 2k + 1, with G_n a polynomial in g_3, ..., g_n, w_1, ..., w_{n-2} and their first derivatives; the full
recurrences were checked symbolically for m <= 3 and n <= 5). Keep g1 equal to that of the reference configuration
(the example, so that b = b^e and b' >= lambda1; or, for the disk, the configuration of (b), with b' >= lambda1/2).
Each equation has the form b u' + d u = f with d(0) > 0 (d(0) = 2k lambda1 for a_{2k+2}, k >= 1, and n lambda1 + 1 for
w_n), and such an equation has exactly one solution bounded at 0, which is smooth (regular singular point, explicit
integral representation). Solving successively for a_{2k+2}, for w_{2k+1} with r_{2k+1} = 0, and then for g_{2k+3},
defines all jets on R uniquely; w_1 = q is the bounded solution of b q' + (M - b') q = 2a, positive with q(0) = q0. On
|y| <= Y1, Y1 > Y0, the jets are realized by a cubic correction -(1/6) kappa(y) x^3 chi(x), with kappa = zeta (q -
q^r) for a cutoff zeta in y, where q^r and g_n^r are the axis coefficients of the chosen reference (q^e and g_n^e for
the example) and the slowly varying cutoff chi(x) = eta(1 + log(|x|/eps)/N) (eta smooth, nonincreasing, 1 on
(-infinity, 0] and 0 on [1, infinity)), which satisfies |x chi'| + |x^2 chi''| <= C/N; the negative Laplacian of the
correction divided by x is kappa (chi + x chi' + x^2 chi''/6) + kappa'' x^2 chi/6, whose leading part makes q^r + chi
kappa a convex combination of q^r and q^r + kappa = zeta q + (1 - zeta) q^r, both positive, so N large and then eps
small keep Omega/x positive and the basin margins. The jets of order at least 5 are realized by a Borel sum of x^n
zeta(y)(g_n - g_n^r) chi0(x/eps_n) that is small in C^3. To keep the disk of (b), use the configuration of (b) as
reference: on its central interval g1 = l + c y, g3 = -q0/6 and g_n = 0 for n >= 5, and there b = lambda2 y, a = a0, q
= q0 and all higher coefficients vanish, which are the unique bounded solutions (for a_2 with the normalization a_2(0)
= a0); so target and reference coefficients agree there, and all corrections vanish on a horizontal strip containing a
smaller disk.
(d) On the lower axis put y = h - r, r -> infinity. There q = q^e, and b = b^e + C0 + O(r^{-2}), b' = b^e' +
O(r^{-3}): the compactly supported vorticity perturbation is odd in x, hence has zero mass, and its velocity is
O(r^{-2}) with derivative O(r^{-3}). From U_2^e(0, h - r) = -B (L^2 + r^2)^p and q^e(h - r) = 4 B p (L^2 + r^2)^{p-2}
[2 L^2 + (p + 1) r^2]: b^e(h - r) = -beta r - B r^s + C1 + O(r^{s-2}), b^e'(h - r) = beta + B s r^{s-1} + O(r^{s-3}),
q^e(h - r) = Q_e r^{s-2} (1 + O(r^{-2})) and q^e'(h - r) = (2 - s) Q_e r^{s-3} (1 + O(r^{-2})). Since M = 2 beta + 1
and beta (2 - s) = beta + 1, the terms of order r^{s-2} cancel, and b q' + (M - b') q = -B Q_e ((2 - s) + s) r^{2s-3} +
O(r^{s-3}) = -2 B Q_e r^{-1-2/beta} + O(r^{-2-1/beta}), while 2a >= 0 (only a >= 0 is used). For the second
statement put H = b q' + (M - b') q and F = b H' - (2b' - Lambda) H; if H = 2a on an interval then F = 0 there,
because b a' = (2b' - Lambda) a. Outside the support b = b^e and q = q^e (U(0) = U^e(0)), so F = F_e there, and F_e is
real analytic on R with F_e'(0) = (Lambda/2) M q_e'(0) > 0 (exactly 119/15 at beta = 4, a0 = 1); so F_e vanishes on no
open interval.
(e) Step 1. b^e has the single zero 0 and b^e' >= lambda1 (4.13). Near 0 the equation b^e Q' + (M - b^e') Q = 2 a^e
has exactly one bounded solution, which is smooth with Q(0) = q0, as in (c); it continues to R by the regular
equation, and it is positive (at a first zero y1 of Q on either side of 0, b^e Q'(y1) = 2 a^e(y1) > 0 is incompatible
with Q > 0 between 0 and y1). As y -> +-infinity, b^e = beta y + O(|y|^{1-1/beta}), b^e' = beta + O(|y|^{-1/beta}) and
b^e'' = O(|y|^{-1-1/beta}), so a^e = C_{+-} |y|^{-1-2/beta} (1 + o(1)) and an integrating factor E > 0 of the Q
equation is E = c_{+-} |y|^{1+1/beta} (1 + o(1)), with C_{+-}, c_{+-} > 0; (E Q)' = 2 a^e E/b^e has the sign of y and
is O(|y|^{-1-1/beta}), so E Q increases to finite positive limits as |y| -> infinity, and Q = (const) |y|^{-1-1/beta}
(1 + o(1)) with positive constants. Since q^e = Q_e |y|^{-1-1/beta} (1 + o(1)), Q/q^e is continuous and positive with
finite positive limits, so K^{-1} <= Q/q^e <= K on R for some K >= 1. (Floating-point evaluations of Q/q^e at |y| =
10^48 and 10^96, by two independent integrations of the equation, give limits of about 5.47e-5 as y -> +infinity and
3.32e3 as y -> -infinity at (beta, a0) = (4, 1), and about 1.44e-4 and 971 at (3, 1); these are not enclosures. So K
is large; this affects only the constants nu, t0 and eps.) The equation and its derivative give |Q'| + |Q''| <= C (1 +
|y|)^{-2-1/beta}; the same holds for q^e, so f0 = Q - q^e satisfies |f0| + |f0'| + |f0''| <= C q^e.
Step 2. Fix nu in (0, 1/2] with nu (K - 1) <= 1/2. There is a smooth even gamma with gamma = 1 on [-1, 1], gamma = 0
outside [-t0, t0] and |gamma| <= 1 such that m(t) = (t^3 gamma(t))''/(6t) satisfies -nu <= m <= 1: take a smooth even
m with m = 1 on [-1, 1], -nu <= m <= 1, m = 0 for |t| >= t0 and int_0^infinity t m = int_0^infinity t^2 m = 0 (for
instance m = rho1 - d2 rho2 + d3 rho3 with bumps 0 <= rho_i <= 1 of disjoint supports in increasing order, rho1 = 1 on
[0, 1]; the two moment conditions give d2 = mu1 (t3 - t1)/(mu2 (t3 - t2)) and d3 = mu1 (t2 - t1)/(mu3 (t3 - t2)), with
mu_i = int t rho_i and t_i = int t^2 rho_i/mu_i, and if rho2 and rho3 are smoothings of fixed width of the indicators
of [3, R1] and [R1 + 1, R1 + 2] then d2 = O(R1^{-2}) and d3 = O(R1^{-1}), so d2 <= nu and d3 <= 1 for large R1). Put
Phi(t) = int_0^t (t - s) 6 s m(s) ds for t >= 0, extended oddly; then Phi'' = 6 t m, Phi = t^3 on [0, 1], Phi = 0 for
t >= t0 by the moment conditions, and -nu t^3 <= Phi(t) <= t^3, so gamma = Phi/t^3 has the stated properties.
Step 3. For eps in (0, 1] put Psi^1 = Psi^e - (f0(y)/6) x^3 gamma(x/eps). Then
  Omega^1/x = Omega^e/x + f0(y) m(x/eps) + (f0''(y)/6) x^2 gamma(x/eps)
(checked symbolically). The correction is O(x^3) and odd in x, so g1, b, the 2-jet at 0 and U(0) are unchanged, and
q^1 = q^e + f0 = Q (gamma = m = 1 near x = 0). Positivity: outside |x| < eps t0, Omega^1 = Omega^e. Inside, |d_x^2
(Omega^e/x)| <= C S^{p-2} <= C' q^e(y), so Omega^e/x >= q^e (1 - C x^2); if f0(y) >= 0 then f0 m >= -nu (K - 1) q^e >=
-q^e/2, and if f0(y) < 0 then f0 m >= f0, so q^e + f0 m >= Q >= q^e/K; with |f0''| <= C q^e and |gamma| <= 1 this
gives Omega^1/x >= q^e (1/(2K) - C'' eps^2 t0^2) > 0 for small eps. The field grad^perp of the correction is bounded
by C (1 + |y|)^{-1-1/beta}, vanishes at 0 and is divergence free with negative curl Omega^1 - Omega^e, so U^1 - U^1(0)
is the canonical inverse of Omega^1 (A4), and the bounds on Omega^1 - Omega^e and U^1 - U^e hold. Basin: W^1_1/x
differs from W^e_1/x by at most (eps t0)^2 sup |f0'|/6 <= lambda1/2 for small eps, b is unchanged, DU^1 and Psi^1_xx
are bounded, and the argument of 4.28(b) gives the whole-plane basin, xi and Theta^1 = a0 xi^2 with the polynomial
bound. Since b = b^e has the single zero 0, a^1 = a^e on R, and the identity gives d_x R_Omega(0, y) = b^e Q' + (M -
b^e') Q - 2 a^e = 0 for all y.
Step 4. Run the recursion of 4.28(a) on Psi^1, choosing at each stage the solution D of -Lap D = delta Omega_n in
P_{n+2}^odd whose x y^{n+1} coefficient is 0 (this fixes the harmonic part, whose x y^{n+1} coefficient is +-(n + 2),
so these are admissible complements). By induction, suppose that all earlier corrections lie in x^5 P; they do not
change g1 or g3, so the identity still gives d_x R_Omega(0, .) = 0 near 0, and the x y^{n-1} coefficient of
(R_Omega)_n, which is the coefficient of y^{n-1} in the Taylor series of d_x R_Omega(0, .) at 0, is 0. So delta
Omega_n has zero x y^{n-1} coefficient, and since the x y^{n-1} coefficient of -Lap(d_1 x y^{n+1} + d_3 x^3 y^{n-1} +
...) is -(n + 1) n d_1 - 6 d_3, also d_3 = 0, which completes the induction. Hence every D_m lies in x^5 P_{m-5},
every x-derivative of order at most 4 of each summand chi(./eps_m) D_m of the Borel sum delta of 4.28(b) vanishes on
the axis, and by convergence in every C^k so does that of delta; in particular delta_x(0, .) = delta_xxx(0, .) = 0; b,
a, q and the axis identity are unchanged, R_Omega is flat at 0, and the other properties follow as in 4.28(b), since
Omega^1/x has a positive minimum on |X| <= 2.
Scope. These are configurations. Those of (b), (c) and 4.28(b) are not profiles, by (d); those of (e) are not
profiles, by 4.32. The collections of conditions of (V) realized in (b), (c) and (e), each with the properties listed
in the compatibility summary after 4.31, are contained in its item (ii) (the cutoff family of (b) loses positivity as
rho -> infinity, and 4.31 uses another family). Under the hypotheses of (d) (including a0 > 0, Theta = a0 xi^2 on its
own whole-plane backward basin and the canonical relative inverse), a compactly supported change of the vorticity of
the example cannot make d_x R_Omega(0, .) vanish on the whole axis, so the strip in (e) cannot be replaced by a
compact set. (V) on open sets away from the center is not addressed here.

4.30 The vorticity equation to all orders on the whole axis (beta > 2). Notation as in 4.29 (configuration, P, q0,
q^e, and the expansions Psi ~ sum x^n g_n(y), Omega ~ sum x^n w_n(y) (n odd), Theta ~ sum x^{2m} a_{2m}(y) along the
axis). For every beta > 2 and a0 > 0 there is a configuration with all properties of 4.28(b) except agreement with the
example outside a compact set, which is replaced by: Omega - Omega^e vanishes outside a strip |x| <= x0 and is bounded
by C |x| (1 + |y|)^{-1-1/beta}, and |U - U^e| <= C (1 + |y|)^{-1-1/beta} (so U = O(r^{1-1/beta}), DU = O(r^{-1/beta}),
and the leading r^{-1/beta} tail of Omega is that of the example, uniformly in theta; convergence of its angular
derivatives is not asserted); such that
  d_x^i d_y^j R_Omega(0, y) = 0   for all i, j >= 0 and all y in R,
and Psi = P, Omega = q0 x and Theta = a0 x^2 on a disk |X| < rho for some rho > 0, so that (T) and (V) hold exactly
there. In it b = b^e outside a compact interval, b' >= lambda1/2, and q is the solution bounded at 0 of b q' + (M -
b') q = 2a, which is positive. No bound on derivatives of Psi of order higher than three is asserted at infinity; the
class (A1)-(A4) requires none.
Proof outline. Reference. Let Psi^0 be the configuration of 4.29(b), with disk radius rho0: it equals the example
outside a compact set, W^0_1/x >= lambda1/2, b' >= lambda1/2, Omega^0/x > 0, q^0 = Omega^0_x(0, .) > 0, and on |y| <
rho0 its axis data are g1 = l + c y, g3 = -q0/6, g_n = 0 (n >= 5), so b = lambda2 y there. Moreover Omega^0/x >=
q^0(y)(1 - C x^2) for |x| <= 1, since Omega^0/x is even in x and |d_x^2 (Omega^0/x)| <= C q^0 (for the example |d_x^2
(Omega^e/x)| <= C S^{p-2} <= C' q^e).
First order. Keep g1 = g1^0, so b = b^0; put a = a0 exp(int_0^y (2b' - Lambda)/b) and let Q be the solution bounded at
0 of b Q' + (M - b') Q = 2a. Since b = b^e outside a compact interval, the argument of 4.29(e) Step 1 gives Q > 0 on
R, Q = Q_{+-} |y|^{-1-1/beta} (1 + o(1)) with Q_{+-} > 0, |Q'| + |Q''| <= C (1 + |y|)^{-2-1/beta}, hence K^{-1} <=
Q/q^0 <= K for some K >= 1 and f = Q - q^0 satisfies |f| + |f'| + |f''| <= C q^0. On |y| < rho0, b = lambda2 y, 2b' -
Lambda = 0 and M - b' = beta/2, so uniqueness gives a = a0, Q = q0 and f = 0 there. Put Psi^1 = Psi^0 - (f/6) x^3
gamma(x/eps) with gamma, m and nu as in 4.29(e) Step 2. As in 4.29(e) Step 3, for small eps: g1, b, U(0) and the
center data are unchanged, q^1 = Q, Psi^1 = Psi^0 on the band |y| < rho0, Omega^1/x >= c1 q^0(y) on |x| <= a1 for some
a1, c1 > 0 (a1 larger than the support width eps t0), Omega^1 = Omega^0 for |x| >= eps t0, W^1_1/x >= lambda1/4, and
U^1 - U^1(0) is the canonical inverse.
Higher coefficients. With g1 fixed and a_2 = a, w_1 = Q, g3 = -(Q + g1'')/6, solve successively, for k = 1, 2, ...,
the temperature recurrence for a_{2k+2}, the equation r_{2k+1} = 0 of 4.29(c) for w_{2k+1}, and w_{2k+1} =
-g_{2k+1}'' - (2k + 2)(2k + 3) g_{2k+3} for g_{2k+3}. Each of the first two is b u' + d u = f with d(0) = 2k lambda1 >
0, respectively (2k + 1) lambda1 + 1 > 0, and has exactly one solution bounded at 0, which is smooth on R (4.29(c));
no bound at infinity is needed. On |y| < rho0 the polynomial values (a_{2m} = 0 for m >= 2, w_n = 0 for n >= 3, g_n =
0 for n >= 5) solve these equations, so by uniqueness the solutions take these values there. Put f_n = g_n - g_n^1 for
odd n >= 5 (g_n^1 the coefficients of Psi^1); f_n = 0 on |y| < rho0.
Weighted Borel sum on the noncompact axis. Let (eta_j)_{j in Z} be a smooth partition of unity on R with supp eta_j in
[j - 1, j + 1] (translates of one bump divided by their periodic sum), so at most three eta_j are nonzero at any
point; put q_j = min of q^0 on [j - 1, j + 1] and tau_j = eta_* min(1, q_j), with eta_* > 0 to be fixed; let chi0 be
smooth and even, chi0 = 1 on [-1, 1], chi0 = 0 outside [-2, 2]. For odd n >= 5 and j in Z choose eps_{n,j} in (0,
a1/2] with ||x^n eta_j(y) f_n(y) chi0(x/eps_{n,j})||_{C^{n-1}} <= 2^{-n} tau_j, which is possible since each
derivative of order k < n of this term is O(eps_{n,j}^{n-k}). The sum delta of all these terms converges in C^k on
every compact set for every k (a compact set meets finitely many supports in y, and for fixed k the terms with n > k
are summable in C^k), so delta is smooth, odd in x, vanishes for |x| >= a1 and on the band |y| < rho0, and its x
Taylor coefficients on the axis are the f_n (chi0 = 1 near 0 and sum eta_j = 1). For every derivative of order at most
3, |d^nu delta(x, y)| <= C eta_* q^0(y) (at most three j contribute at y and q_j <= q^0(y)); since Lap delta and
delta_y are odd in x, the mean value theorem in x gives |Lap delta/x| <= 2 C eta_* q^0(y) and |delta_y/x| <= C eta_*
q^0(y). Put Psi = Psi^1 + delta. For eta_* small, Omega/x >= c1 q^0/2 > 0 on {0 < x <= a1} and Omega = Omega^1
for |x| >= a1; W_1/x >= lambda1/8 (as sup q^0 < infinity); b is unchanged (delta = O(x^5)), so b' >= lambda1/2; Psi_xx
is bounded; and U - U(0) is the canonical inverse of Omega, since grad^perp delta minus the canonical inverse of -Lap
delta is a harmonic, sublinear field vanishing at 0 (the once-subtracted integral converges for the decay of -Lap
delta), hence 0. The bounds on Omega - Omega^e and U - U^e follow from those of 4.29(e) and |d^nu delta| <= C q^0 =
O((1 + |y|)^{-1-1/beta}), |nu| <= 3.
Temperature, identification, disk. The basin, xi and Theta = a0 xi^2 with the polynomial bound follow from the margins
as in 4.28(b). The x Taylor coefficients of the actual Theta along the axis satisfy the temperature recurrences and
are smooth at 0, hence equal the prescribed a_{2m} (uniqueness of the solution bounded at 0, and for a_2 the
normalization a_2(0) = a0); the coefficients of the actual Omega = -Lap Psi are the w_n. So r_n = 0 on R for every odd
n. R_Omega is odd in x, so its even x derivatives vanish on the axis; its odd ones are n! r_n = 0, and differentiation
in y gives the mixed derivatives. All corrections after the reference vanish on |y| < rho0, so Psi = P on |X| < rho0;
for rho <= min(rho0, lambda1/q0) the disk |X| < rho is backward invariant (4.29(b)), so Theta = a0 x^2 there and (T),
(V) hold there by 4.29(a).
A second proof gives a variant with bounds on all derivatives. In the classes S^s of smooth f with |f^{(j)}(y)| <= C_j
(1 + |y|)^{s-j}, the coefficients satisfy a_{2m} in S^{1-2/beta-2m}, w_n in S^{-n-1/beta} and g_n in S^{2-1/beta-n},
with limits of |y|^{-s} f(y) as y -> +-infinity: every forcing term is smaller than the homogeneous solution by a
factor O(|y|^{-1/beta}), so no resonant logarithm occurs at the leading order (lower-order logarithmic terms are not
excluded and are not needed). With the conic cutoffs gamma(x/(eps (1 + y^2)^{1/2})) and chi0(x/(eps_n (1 +
y^2)^{1/2})) in place of gamma(x/eps) and the partition (the estimates, written out for a general reference, are those
of the proof of 4.31(b): weighted seminorms of the terms through order n - 1, summably small, and the angular limit
from a finite sum with differentiated limits plus a uniformly summable tail), this gives a configuration with the same
axis and disk properties, |D^k U| <= C_k (1 + |X|)^{1-1/beta-k} and |D^k Omega| <= C_k (1 + |X|)^{-1/beta-k} for every
k, Omega - Omega^e supported, outside a compact set, in an arbitrarily narrow cone around the axis, and r^{1/beta}
Omega(r e(theta)) -> a_tail(theta) in C^infinity(S^1), with a_tail not identically 0 and equal to the coefficient of
the example outside the cone. (Exact symbolic checks of the recurrences through a_8, w_7, g_9 and of the conic cutoff
derivatives; exact rational checks of finite localizations of the partition construction, 20 cells and degrees 5 to
11; floating-point integrations of the first-order equation with the disk reference to |y| = 10^48, which are not
enclosures.)
Scope. These are configurations; by 4.32 they are not profiles. With 4.28 and 4.29 they give (V) exactly on a small
disk around the center together with every derivative of (V) at every point of the axis, with the properties listed in
the compatibility summary after 4.31; 4.31(b) replaces the small disk by any prescribed disk (item (ii) there). (V) on
an open neighbourhood of the whole axis is not addressed: the Taylor coefficients in x along the axis do not determine
a smooth function near the axis (x exp(-1/x^2) h(y), extended by 0, is odd, flat on the axis and nonzero arbitrarily
close to it). The letters nu, gamma, m, t0, eps, f, f_n, a1, c1, eta_j, q_j, tau_j, eta_*, chi0, eps_{n,j}, eps_n,
delta and rho0 are local to 4.30.

4.31 Exactness on arbitrarily large disks (beta > 2). Notation as in 4.28 and 4.29 (configuration, q0 = 4 a0/beta, P0
= c x y - (q0/6) x^3, W_P = (lambda1 x, lambda2 y - q0 x^2/2)).
(a) For every beta > 2, a0 > 0 and R > 0 there is a configuration with all properties of 4.28(b) except agreement with
the example of 4.13 outside a compact set, which is replaced by Psi = Psi_L outside a compact set, with the
anisotropic field Psi_L defined below (so U = O(r^{1-1/beta}), DU = O(r^{-1/beta}) and Omega =
r^{-1/beta}(a_tail(theta) + O(1/r)) uniformly in theta, with a_tail smooth, not identically 0 and positive where cos
theta > 0), such that Psi = l_L x + P0, Omega = q0 x and Theta = a0 x^2 on |X| < R, where l_L = Psi_x(0); in
particular (T) and (V) hold exactly on |X| < R. Moreover W_1/x >= lambda1/2 on R^2 and b' >= lambda1/2 on R.
Consequently (V) can hold exactly on any prescribed bounded set, and every derivative of R_Omega vanishes on the axis
segment |y| < R; this extends the exactness conclusions of 4.29(b) and (c) (on a disk, and on a finite axis segment)
to arbitrarily large bounded sets, at the price of replacing the exterior of the example by that of Psi_L. As in
4.29(d), d_x R_Omega(0, y) < 0 for all sufficiently negative y, and d_x R_Omega(0, .) vanishes on no open interval of
the axis outside B_{2D}. For mu > 0 the scaling (mu^2 Psi(X/mu), Omega(X/mu), mu Theta(X/mu)) maps a0 to a0/mu and R
to mu R and preserves all the listed properties; so a0 R is invariant, and the statement for all (a0, R) is equivalent
to the statement at one fixed radius for every a0 > 0 (scaling a single configuration does not make a0 R large).
(b) Combination with the whole axis. For every beta > 2, a0 > 0, R > 0 and sigma > 0 there is a configuration with all
properties of 4.28(b) except agreement with the example of 4.13 outside a compact set, which is replaced by Psi =
Psi_L outside the union of a compact set and the double cone |x| <= sigma |y| (Psi_L as in (a), for some finite L),
such that Psi = l_L x + P0, Omega = q0 x and Theta = a0 x^2 on |X| < R (so (T) and (V) hold exactly there) and every
derivative of R_Omega vanishes at every point of the axis (as in 4.30). Moreover b is that of (a), W_1/x has a
positive lower bound on R^2, |D^k U| <= C_k (1 + |X|)^{1-1/beta-k} and |D^k Omega| <= C_k (1 + |X|)^{-1/beta-k} for
every k >= 0, r^{1/beta} Omega(r e(theta)) -> a_tail(theta) in C^infinity(S^1) as r -> infinity with a_tail smooth and
not identically 0, and 0 <= Theta <= C (1 + |X|)^{1-2/beta}.
Proof outline. (a) Anisotropic family. Put p = (beta - 1)/(2 beta), d = 6c/q0 and kappa = 9c^2/(beta q0^2); for L >=
sqrt(kappa) put eta = kappa/L^2 in (0, 1], h = sqrt(beta) L/sqrt(eta), S = L^2 + x^2 + eta (y - h)^2, S0 = (1 + beta)
L^2, B = (q0/(6p)) S0^{1-p}, Psi_L = -B x S^p and l_L = -B S0^p (eta = 1 gives the example of 4.13). Then eta h = d/2,
eta h^2 = beta L^2, S = S0 + x^2 - d y + eta y^2, and
  Omega_L = 2 B p x S^{p-2} [(3 + eta) L^2 + (1 + 2p + eta) x^2 + eta (3 + (2p - 1) eta)(y - h)^2]
with positive bracket coefficients (2p - 1 = -1/beta, eta <= 1), so Omega_L > 0 on {x > 0}. For every L, (Psi_L)_xy(0)
= 2 B p eta h S0^{p-1} = c, (Psi_L)_xxx(0) = -6 B p S0^{p-1} = -q0 and (Psi_L)_xyy(0) = 0. Margins: (W_L)_1/x = beta +
2 B p eta (y - h) S^{p-1} and b_L' = beta - 2 B p eta (y - h)(L^2 + eta (y - h)^2)^{p-1}; since t (L^2 + t^2)^{p-1}
has derivative (L^2 + t^2)^{p-2}(L^2 + (2p - 1) t^2), both perturbations are bounded in absolute value by 2 B p
sqrt(eta beta) L S0^{p-1} = c, so (W_L)_1/x >= lambda1 and b_L' >= lambda1 uniformly in L. Tail: S = r^2
H_eta(theta)(1 + O(1/r)) with H_eta = cos^2 theta + eta sin^2 theta >= eta gives the stated form of Omega_L with
a_tail(theta) = 2 B p cos theta H_eta^{p-2} [(1 + 2p + eta) cos^2 theta + eta (3 + (2p - 1) eta) sin^2 theta], and U_L
= O(r^{2p}), DU_L = O(r^{2p-1}).
Convergence to the polynomial. With T_L = x^2 - d y + eta y^2 and z_L = T_L/S0 one has exactly Psi_L - l_L x = -(q0/6)
x T_L J_L with J_L = int_0^1 (1 + u z_L)^{p-1} du, so E_L := Psi_L - l_L x - P0 = -(q0/6) x [eta y^2 + T_L (J_L - 1)].
The norm ||f||_{3,N} = sum_{i+j<=3} ||d_x^i d_y^j f||_{L^infinity(B_N)}/(i! j!) is submultiplicative (Leibniz), and
the binomial coefficients of (1 + z)^{p-1} have absolute value at most 1; hence, with H = N + 1 and C0 = 2 +
d, ||E_L||_{3,N} <= D_N/L^2, D_N = (q0/6)[kappa H^3 + 2 C0^2 H^5/(1 + beta)], as soon as L^2 >= 2 C0 H^2/(1 + beta).
Replacement. Let chi be the radial cutoff of 4.28(b) and C_chi = sum_{i+j<=3} ||d_x^i d_y^j chi||_infinity/(i! j!);
put k = q0/(2 (lambda2 - 2 lambda1)), D = 1 + 2R + k R^2, N = 2D and Psi = Psi_L - chi(X/D) E_L, with L so large that
L^2 > max{kappa, 2 C0 (N + 1)^2/(1 + beta), 16 (1 + C_chi) D_N/q0, 2 C_chi D_N/lambda1}. Then Psi = l_L x + P0 on B_D
and Psi = Psi_L outside B_{2D}. On B_N, F_p := Psi - l_L x - P0 = (1 - chi(X/D)) E_L satisfies ||F_p||_{3,N} <= (1 +
C_chi) D_N/L^2 and is odd in x, so |Lap F_p/x| <= sup |d_x Lap F_p| <= 8 ||F_p||_{3,N} and Omega/x >= q0/2 on {x > 0}
in B_N; outside B_N, Omega = Omega_L > 0. With delta = -chi(X/D) E_L (odd in x), the correction changes W_1/x by
-delta_y/x and b' by delta_xy(0, .), both bounded by sup |delta_xy| <= ||delta||_{3,N} <= C_chi D_N/L^2 < lambda1/2,
so W_1/x >= lambda1/2 and b' >= lambda1/2. The correction has compact support, so U - U(0) is the canonical inverse of
Omega (A4) and the tail is that of Psi_L; DU is bounded, and the backward basin of 0 is the whole plane by the
argument of 4.28(b).
Temperature and exactness. On B_D, W = W_P. For 0 < rho < min(D, lambda1/q0) the disk B_rho is backward invariant
(X.W_P >= (lambda1 - q0 rho/2)|X|^2 there), and xi(X) = e^{lambda1 t} (phi_{-t} X)_1, for any t with phi_{-t} X in
B_rho, is independent of t (on B_rho the first coordinate decays exactly like e^{-lambda1 t}), smooth (one t serves a
neighbourhood of X), odd in x, zero exactly on the axis, and satisfies W.grad xi = lambda1 xi; Theta = a0 xi^2 solves
(T) on R^2, and the polynomial bound on Theta follows as in 4.28(b). For X0 = (x0, y0) in B_R the backward W_P orbit
is x(t) = e^{-lambda1 t} x0, y(t) = e^{-lambda2 t} y0 + k x0^2 (e^{-2 lambda1 t} - e^{-lambda2 t}) and stays in |X|
<= |x0| + |y0| + k x0^2 < D, so it is the backward W orbit, and xi(X0) = x0. Hence Theta = a0 x^2 and Omega = q0 x on
B_R, and (T), (V) hold there by 4.29(a). (Exact symbolic checks of the vorticity identity, the center data, the
relations eta h = d/2 and eta h^2 = beta L^2, the margin maximum c, the identity for Psi_L - l_L x and the polynomial
orbit at (beta, q0, L) = (4, 1, 6), (9, 1/2, 20) and (3, 2, 3).)
Axis obstruction. Outside B_{2D}, Psi = Psi_L, and on the axis q_L = 2 B p S^{p-2} [(3 + eta) L^2 + eta (3 -
eta/beta)(y - h)^2] with S = L^2 + eta (y - h)^2. The proof of 4.29(d) applies with s = 2p, B replaced by B eta^p and
Q_e by Q_eta = 2 B p eta^{p-1} (3 - eta/beta) > 0: b q' + (M - b') q = -2 B eta^p Q_eta |y|^{-1-2/beta} (1 + o(1)) as
y -> -infinity, while 2a >= 0. With H and F as there, F = F_L outside B_{2D}, F_L is real analytic, b_L''(0) = 0 and
q_L'(0) = c (3 (beta + 1) + 2 eta)/(beta (beta + 1) L^2) > 0, so F_L'(0) = lambda2 M q_L'(0) > 0 and F_L vanishes on
no open interval.
(b) Reference. Let Psi^0 be the configuration of (a) (so D > 2R + k R^2), with axis coefficients g_n^0 and q^0 =
(Omega^0)_x(0, .), and put <y> = (1 + y^2)^{1/2}; keep g1 = g1^0, hence b and U(0). The second construction of 4.30
(symbol classes S^s and conic cutoffs) was written for a reference equal to the example outside a compact set; for the
present reference its inputs are as follows. For the fixed L, H_eta >= eta > 0, the explicit formula for Psi_L and the
compact replacement give |d^nu Psi^0| <= C_nu (1 + |X|)^{2-1/beta-|nu|} for every nu, and the rescaled streams
r^{-2+1/beta} Psi^0(r X) converge in C^infinity on compact annuli to -B x (x^2 + eta y^2)^p. The axis coefficients
satisfy g_n^0 in S^{2-1/beta-n}, with leading powers |y|^{2-1/beta-n} at both ends, differentiated, and remainders
smaller by a factor |y|^{-1/beta}; in particular b = beta y - B eta^p |y|^{1-1/beta} + O(1) and q^0 =
Q_eta |y|^{-1-1/beta} (1 + O(|y|^{-1})) with the corresponding derivative bounds, so q^0 (positive by the proof of
(a)) is comparable to <y>^{-1-1/beta} on R. Since Omega^0 is odd in x, Omega^0/x = int_0^1 Omega^0_x(t x, y) dt, and
so |d_x^2 (Omega^0/x)| <= C <y>^{-3-1/beta} <= C' q^0 <y>^{-2}.
Coefficients. Let a_2 = a0 exp(int_0^y (2b' - Lambda)/b) (on |y| < D, b = lambda2 y and the equation of a_2 reduces to
lambda2 y a_2' = 0, whose bounded solutions are all constants, so a_2 is selected by a_2(0) = a0 and not by
boundedness), let w_1 = Q be the solution bounded at 0 of b Q' + (M - b') Q = 2 a_2, and determine a_{2j+2}, w_{2j+1}
and g_{2j+3} (j >= 1) as in 4.30, as the solutions bounded at 0 of the equations of 4.29(c). At either end a_2 =
A_{+-} |y|^{-1-2/beta} + S^{-1-3/beta} with A_{+-} > 0; Q > 0, and since an outward integrating factor E of the Q
equation is of order |y|^{1+1/beta} and (E Q)' > 0 is integrable, Q = Q_{+-} |y|^{-1-1/beta} + S^{-1-2/beta} with
Q_{+-} > 0, so K^{-1} <= Q/q^0 <= K for some K >= 1. The higher equations have the form b u' + e u = f~ with e - beta
h_* in S^{-1/beta} at either end (h_* = 2j - 1 + 2/beta for a_{2j}, h_* = n + 1/beta for w_n); an integrating factor
is E = |y|^{h_*} (c_{+-} + S^{-1/beta}), so f~ in S^{-h_*-1/beta} gives (E u)' in S^{-1-1/beta} and u =
C_{+-} |y|^{-h_*} + S^{-h_*-1/beta}. The forcing of the temperature equation for a_{2j} lies in S^{1-3/beta-2j} and
that of the vorticity equation for w_n, including (n + 1) a_{n+1}, in S^{-n-2/beta}, so induction gives a_{2j} in
S^{1-2/beta-2j}, w_n in S^{-n-1/beta} and g_n in S^{2-1/beta-n}, with differentiated leading powers and remainders
gaining |y|^{-1/beta} (no leading logarithm occurs). On |y| < D the reference axis data are g1 = l_L + c y, g3 = -q0/6
and g_n = 0 (n >= 5); there the normalization gives a_2 = a0, and bounded uniqueness gives Q = q0, g3 = -q0/6 and the
polynomial values of all higher coefficients (as in 4.30). So f = Q - q^0 in S^{-1-1/beta} and f_n = g_n - g_n^0 in
S^{2-1/beta-n} (odd n >= 5) vanish on |y| < D.
First correction. Let gamma, m, nu and t0 be as in 4.29(e) Step 2, with nu (K - 1) <= 1/2 for the present K; for 0 <
eps <= 1 put kappa_1 = eps t0, t = x/(eps <y>) and Psi^1 = Psi^0 - (f/6) x^3 gamma(t). Then Omega^1/x = Omega^0/x + f
m(t) + (x^2/6) d_y^2 (f gamma(t)), and with v = <y>'/<y>, d_y^2 (f gamma(t)) = f'' gamma - (2 v f' + v' f) t gamma' +
v^2 f (t gamma' + t^2 gamma''), which is O(<y>^{-3-1/beta}). On the cone |x| <= kappa_1 <y>, q^0 + f m >= min(1/2,
1/K) q^0 (for f >= 0 by m >= -nu; for f < 0 by m <= 1, which gives q^0 + f m >= Q), so Omega^1/x >= (min(1/2, 1/K) - C
kappa_1^2) q^0, and W_1/x changes by O(kappa_1^2 <y>^{-1/beta}); for eps small, Omega^1/x >= c1 q^0 on the cone for
some c1 > 0, and W^1_1/x >= lambda1/4. Outside the cone Psi^1 = Psi^0. The correction is O(x^3), gamma = 1 near 0 and
f = 0 on |y| < D, so g1, b, U(0), the center data and the axis coefficients of order at least 5 are unchanged, and the
cubic one becomes -(Q + g1'')/6, so that q^1 = Q.
Higher coefficients. For odd n >= 5 put F_n = x^n f_n(y) chi0(x/(eps_n <y>)), with chi0 as in 4.30. For k < n and
eps_n <= 1, sup <y>^{|zeta| - 2 + 1/beta} |d^zeta F_n| <= C_{n,k} eps_n^{n-k} for |zeta| <= k; choose eps_n decreasing
to 0 with 2 eps_n <= kappa_1 so that these weighted seminorms with k <= n - 1 are at most tau 2^{-n}. Then delta = sum
F_n converges in every such weighted C^k seminorm, is smooth and odd in x, vanishes on the band |y| < D and has the
axis coefficients f_n; since Lap delta and delta_y are odd in x, the bounds of order at most 3 give |Lap delta/x| <= C
tau <y>^{-1-1/beta} and |delta_y/x| <= C tau <y>^{-1/beta}. Put Psi = Psi^1 + delta. For tau small, Omega/x > 0 on
{x > 0} (outside the cone Omega = Omega^0) and W_1/x has a positive lower bound on R^2; b is unchanged
(delta = O(x^5)).
Cone, symbol bounds, angular limit. All corrections are supported in |x| <= kappa_1 <y>, which for |y| >= 1 lies
in |x| <= sqrt(2) kappa_1 |y|; with sqrt(2) kappa_1 < sigma, Psi = Psi_L outside the union of a compact set and the
double cone |x| <= sigma |y|. On the supports <y> is comparable to 1 + |X|, so the weighted bounds give |D^k U| <= C_k
(1 + |X|)^{1-1/beta-k} and |D^k Omega| <= C_k (1 + |X|)^{-1/beta-k}. Symbol bounds alone do not give an angular limit
(r^{-1/beta} (2 + sin log r) cos theta satisfies them); here each correction has a smooth homogeneous limit after
rescaling, by the differentiated leading powers of f and f_n (for F_n, on y > 0 and on y < 0, the limit is x^n
f_{n,+-} |y|^{2-1/beta-n} chi0(x/(eps_n |y|)), extended by 0), and for each derivative order k the rescaled terms with
n > k are uniformly summable on annuli by the bound tau 2^{-n}. Discarding this tail and passing to the limit in the
finite sum, r^{-2+1/beta} Psi(r X) converges in C^infinity on compact annuli to a homogeneous Psi_infinity, so
r^{1/beta} Omega(r e(theta)) -> a_tail(theta) := (-Lap Psi_infinity)(e(theta)) in C^infinity(S^1); at theta = 0 all
corrections vanish and a_tail(0) = 2 B p (1 + 2p + eta) > 0.
Basin, temperature, disk, inverse. DU is bounded, so the flow is complete; with b' >= lambda1/2 (unchanged), the
positive lower bound of W_1/x and |W_2(x, y) - b(y)| <= C |x|, the argument of 4.28(b) shows that the whole plane is
the backward basin of 0, and xi and Theta = a0 xi^2 are defined by finite backward entry into a small
backward-invariant disk as in (a), with the stated parity and signs. The x Taylor coefficients of Theta along the axis
satisfy the temperature recurrences and are smooth at 0, so by the normalization a_2(0) = a0 and bounded uniqueness
they are the a_{2j}; those of Omega are the w_n; hence, as in 4.30, every derivative of R_Omega vanishes at every
point of the axis. All corrections vanish on |y| < D, so W = W_P on B_D; the backward W_P orbits from B_R stay in B_D
(proof of (a)), so Theta = a0 x^2 and Omega = q0 x on B_R. Since Omega = O((1 + |X|)^{-1/beta}), the once-subtracted
Biot-Savart integral of Omega converges absolutely and is sublinear; its difference from U - U(0) is harmonic,
sublinear and zero at 0, hence 0, which is (A4). Finally X.W >= beta |X|^2 - C |X|^{2-1/beta} bounds the backward
entry time into a fixed large ball by (1/beta) log |X| + C, and transport from its boundary gives 0 <= Theta <= C
(1 + |X|)^{1-2/beta}. All constants depend on the fixed parameters, including L and sigma.
Scope. These are configurations; (V) is not asserted outside B_R. They are not profiles: every correction has zero
gradient at 0, so U(0) is that of Psi_L, the relative velocity and the vorticity agree with those of Psi_L on a
nonempty exterior open set, and 4.32(c) applies. (b) is item (ii) of the compatibility summary below: for a bounded
set K fixed in advance, (V) exactly on K and every derivative of (V) at every point of the axis, with the properties
listed there, do not exclude the slow-tail branch. This does not classify the possible exclusion arguments, and (V) on
an open neighbourhood of the whole axis is not established. The construction supplies no fixed exterior and no
estimates uniform as R -> infinity: L, eta, a_tail and all constants depend on R (and in (b) on sigma). For fixed beta
and a0 and R_j -> infinity, the constructed Omega_j equal q0 x on B_{R_j}, so they converge to q0 x in C^infinity_loc,
and this limit violates (A3). The letters p, d, kappa, eta, h, S, S0, B, L, T_L, z_L, J_L, E_L, D_N, H, C0, C_chi, k,
D, N, F_p, rho, sigma, Q_eta, A_{+-}, K, A, <y>, Psi^0, Psi^1, q^0, Q_{+-}, E, e, u, f~, h_*, f, f_n, F_n, gamma, m,
nu, t0, eps, eps_n, kappa_1, t, v, c1, tau, delta, chi0 and Psi_infinity are local to 4.31.
Compatibility summary (beta > 2; 4.28 to 4.31 and 4.34). Fix beta > 2 and a0 > 0. Each of the following collections of
conditions of (V) is satisfied by a configuration that also satisfies (T) on R^2 with the whole-plane backward basin,
the parity, Omega > 0 on {x > 0}, the center data, the canonical inverse and the slow tail: (i) every Taylor condition
of (V) at the center (4.28(b)); (ii) for every R > 0 and sigma > 0, (V) exactly on B_R and every derivative of R_Omega
zero at every point of the axis (4.31(b); it contains the partial combinations of 4.29(b), (c), (e) and 4.30); (iii)
for every R0 > 0, (V) exactly on B_R0 and on |X| > R1 for some R1 > R0, with R_Omega a nonzero smooth function
supported in R0 <= |X| <= R1 (4.34; whole-axis flatness is not asserted there). The configurations depend on R, sigma
or the chosen reference; no common exterior and no bounds uniform in these parameters are supplied. None of them is a
profile (4.32), so they give no evidence for existence; they show only that each listed collection is consistent with
the listed properties. An exclusion of the slow-tail branch must use more, for instance (V) on the connecting annulus
as well, (V) on an open neighbourhood of the whole axis, or a global argument. Sections 5 and 6 refer to this summary.

4.32 Agreement with the analytic fields of 4.13 and 4.31 on an open set. Let beta > 2 and k = beta - 2. For smooth W =
(W_1, W_2) and Omega on an open set O of R^2 put
  F = W.grad Omega + Omega,  J = d_x W_2,  D = (k - d_x W_1) F - W.grad F,  Z = W_1 F J + W_2 D,
  E_comp = J d_y Z - Z d_y J - k D J.
(a) If a C^2 function Theta on O satisfies W.grad Theta = k Theta and Theta_x = F on O, then E_comp = 0 on O. Thus
E_comp = 0 on R^2 for every profile, with W = beta X + U - U(0).
(b) Let Psi_L = -B x S^p, S = L^2 + x^2 + eta (y - h)^2, eta = kappa/L^2 in (0, 1], be a field of 4.31 (L^2 = kappa,
eta = 1, is the example of 4.13), W = beta X + U - U(0) and Omega = -Lap Psi_L. Then E_comp is real analytic on R^2
and its x^2 y Taylor coefficient at 0 is
  q0 (2 beta + 4) lambda2 M q'(0) > 0,   q'(0) = Omega_xy(0) = c (3 (beta + 1) + 2 eta)/(beta (beta + 1) L^2)
(for eta = 1, q'(0) = 32 a0^2 (3 beta + 5)/(9 beta^2 (beta + 1)(beta + 2)) as in the Scope of 4.13). So, for every
such L, there is no nonempty open set on which this W and Omega satisfy (T) and (V) with any C^2 temperature.
(c) Consequently a configuration whose relative velocity U - U(0) and vorticity coincide with those of the example, or
of some Psi_L, on a nonempty open set is not a profile. This applies to the configurations of 4.28(b), 4.29(b), (c),
(e), 4.30 (both versions) and 4.31(a), (b).
(d) (Converse.) Let Psi be smooth near 0 and odd in x with Psi_xy(0) = c = 1 + beta/2, Omega = -Lap Psi, W = beta X +
U - U(0), F, J and E_comp as above, Theta = int_0^x F(u, y) du and t = W.grad Theta - k Theta. Then
  E_comp = J^2 t_y - J W_2 t_xy + (W_2 J_y + J (k - d_y W_2)) t_x.
(i) If Psi_xxx(0) != 0 and E_comp = 0 on a neighbourhood of 0, then t = 0, so (T) and (V) hold for (Psi, Theta), on a
smaller neighbourhood of 0.
(ii) Let J be not flat at 0, with first nonzero homogeneous Taylor part J_d of degree d >= 1. If t is not flat at 0,
with first nonzero homogeneous part t_N, then the first nonzero homogeneous part of E_comp has degree N + d - 1 and
equals -lambda2 y J_d d_xy t_N + (lambda2 y d_y J_d + (k - lambda2) J_d) d_x t_N. Hence E_comp is flat at 0 if and
only if t is.
(iii) If Psi is real analytic on R^2 and |U(X)|/|X| -> 0 as |X| -> infinity, then J is not flat at 0, and E_comp = 0
on R^2 if and only if (T) and (V) hold on R^2 for (Psi, Theta).
Proof outline. (a) Differentiating W.grad Theta = k Theta in x and using Theta_x = F gives (d_x W_1) F + W.grad F + J
Theta_y = k F, that is J Theta_y = D. Multiplying the transport equation by J gives k J Theta = W_1 F J + W_2 J
Theta_y = Z. Differentiating this in y and multiplying by J gives k J (d_y J) Theta + k J (J Theta_y) = J d_y Z, that
is Z d_y J + k J D = J d_y Z, which is E_comp = 0. No division is used, so zeros of J or W are allowed; only
derivatives of Theta of order at most 2 occur.
(b) S >= L^2 > 0, so Psi_L, W, Omega, F, J, D, Z and E_comp are real analytic on R^2. Write Psi_L = x g1 + x^3 g3 +
O(x^5), Omega = x q + O(x^3), b = W_2(0, .) and A = 2 beta - b'. Then W_1 = x A + O(x^3), W_2 = b + O(x^2), J = x C +
O(x^3) with C = 6 g3, F = x H + O(x^3) with H = b q' + (M - b') q, D = -x G + O(x^3) with G = b H' - (2b' - Lambda) H
(since k - 2A = 2b' - Lambda), Z = -x b G + O(x^3), and the x^2 coefficient of E_comp is E2 = -C (bG)' + bG C' + k C
G. The cubic Taylor polynomial of Psi_L is l x + c x y - (q0/6) x^3 (4.29(a) for eta = 1; 4.31 in general), so b(0) =
0, b'(0) = lambda2, b''(0) = 0 and C(0) = -q0. Since Lambda = 2 lambda2, G(0) = 0, H'(0) = M q'(0) and G'(0) = lambda2
M q'(0); differentiating E2 at 0 and using b(0) = G(0) = 0 gives E2'(0) = C(0)(k - 2 lambda2) G'(0) = q0 (2 beta + 4)
lambda2 M q'(0). For q'(0): with s(y) = S(0, y), Omega_x(0, y) = B (6 p s^{p-1} + (s^p)''), s'' = 2 eta, s(0) = S0 and
s'(0) = -2 eta h; so q'(0) = B p (p - 1) S0^{p-3} s'(0) (6 (1 + eta) S0 + (p - 2) s'(0)^2), and with eta h^2 = beta
L^2 and 4 (2 - p) beta = 6 beta + 2 the last factor is L^2 (6 (1 + beta) + 4 eta) > 0, while B > 0, p - 1 < 0 and
s'(0) < 0; with S0 = (1 + beta) L^2 and 2 B p eta h S0^{p-1} = c this is the stated value. By the identity theorem,
E_comp vanishes on no nonempty open set; (a) gives the conclusion.
(c) E_comp is determined by W and Omega on O, and W = beta X + U - U(0). The configurations listed coincide with the
example (4.28(b), 4.29(b), (c), (e), 4.30) or with Psi_L (4.31) outside a compact set, or outside the union of a
compact set and a strip |x| <= x0 (4.29(e), 4.30) or a closed cone around the axis (the variant of 4.30, and 4.31(b)
with Psi_L), and U(0) is that of the analytic field (the corrections vanish to order at least 3 at 0); so a profile
among them would contradict (b) on an exterior open set. (Exact rational checks of the x^2 y coefficient of E_comp
from Taylor series truncated at degree 10: 476/5 at (beta, a0) = (4, 1) for the example, and 8127/160, 1746927/100000
and 408093191/28800000 for Psi_L at (beta, q0, L) = (4, 1, 6), (4, 1, 10) and (9, 1/2, 20), each equal to the formula
in (b).)
(d) For any C^3 function Theta, differentiating t = W.grad Theta - k Theta in x and substituting Theta_x = F - f
gives, with f = F - Theta_x, the identity E_comp = L_1 f + J^2 t_y - J W_2 t_xy + (W_2 J_y + J (k - d_y W_2)) t_x,
where L_1 is a linear differential operator of order at most 2 with coefficients polynomial in k and the derivatives
of W of order at most 2 (L_1 f = J d_y z - (d_y J) z - k J g with g = (k - d_x W_1) f - W.grad f and z = W_1 J f + W_2
g); here f = 0. By the parity and the center data, W(0) = 0, W_2 is even in x, W_2 = lambda2 y + O(|X|^2), d_y W_2 =
lambda2 + O(|X|), J is odd in x, and t is even in x and divisible by x^2 (Theta is, and W_1 is odd). (i) On a small
rectangle centred at 0, J = x j with j smooth and nonzero (j(0) = Psi_xxx(0)), d_y W_2 > k, each vertical segment
meets {W_2 = 0} exactly once, and t_x = x tau with tau smooth. Then mu = t_x/J = tau/j and nu = t - W_2 mu are smooth,
nu_x = -W_2 mu_x, and the identity gives E_comp = J^2 (nu_y + k mu) for x != 0; so nu_y = -k mu (on the axis by
continuity), and the mixed derivatives give W_2 (mu_x)_y + (d_y W_2 - k) mu_x = 0. If v is smooth near y0 with v(y0) =
0 and v'(y0) > max(k, 0), the nonzero solutions phi of v phi' + (v' - k) phi = 0 are unbounded near y0 (they behave
like |y - y0|^{k/v'(y0) - 1}); applied at the zero of W_2(x, .), with ordinary uniqueness away from it, this gives
mu_x = 0, so mu = mu0(y) and t = (W_2 - b) mu0 with b = W_2(0, .). Then nu_y = -k mu0 reads b mu0' + (b' - k) mu0 = 0,
and the same argument at y = 0 gives mu0 = 0. (ii) d_x t_N != 0 because t is divisible by x^2. The term J^2 t_y has
order at least 2d + N - 1, and the other terms give the displayed part at degree N + d - 1. Writing J_d = y^i P and
d_x t_N = y^n Q with P(x, 0), Q(x, 0) nonzero, the coefficient of y^{i+n} in it is (lambda2 (i - n - 1) + k) P(x, 0)
Q(x, 0), which is nonzero because 0 < k/lambda2 < 2/3 and i - n - 1 is an integer. (iii) J = 0 near 0 would give J = 0
on R^2, so Psi = x w(y) by oddness and U_1 = -x w'(y); sublinearity at fixed y and |x| -> infinity forces w' = 0,
contradicting Psi_xy(0) = c. Theta is real analytic on R^2, so E_comp = 0 makes t flat at 0 by (ii), hence t = 0 near
0 and on R^2 by the identity theorem; (V) holds because Theta_x = F. The converse in (i) and (iii) is (a).
Scope. (a) is a necessary condition for a profile. By (d), for a prescribed stream with the parity and Psi_xy(0) = c,
it is also sufficient for (T) and (V) with the normalized primitive Theta = int_0^x F: on a neighbourhood of 0 when
Psi_xxx(0) != 0, and on R^2 when Psi is real analytic on R^2 with sublinear velocity. This primitive satisfies
Theta(0, .) = 0; identifying it with the temperature of a given profile uses that normalization (4.33(b)). The
canonical inverse and the remaining class conditions are separate conditions, and profiles are only assumed smooth.
For smooth Psi, (d) gives no sufficiency beyond a neighbourhood of 0, and (ii) gives only the equivalence of flatness
at 0, provided J is not flat there. The hypothesis Psi_xxx(0) != 0 of (i) is not implied by the center data and cannot
be dropped: Psi = c x y - (q0/2) x y^2 has Psi_xy(0) = c, Omega_x(0) = q0, J = 0 and E_comp = 0, but t = 4 a0^2 x^2 y
(12 a0 y + 5 beta^2 + 2 beta)/beta^3 (a local example, not a profile). The proof of (i) uses only lambda2 > max(k, 0)
and holds for every beta > 0; the argument of (ii) fails at beta = 2, where the coefficient vanishes for i = n + 1.
E_comp = 0 is not claimed to have no solutions in the class, and no nonexistence assertion follows from (d). (b) and
(c) exclude particular configurations as profiles; they are not a nonexistence statement. They give no conclusion for
configurations, perturbations or limits whose relative velocity and vorticity agree, on no nonempty open set, with
those of the example or of any Psi_L. For an odd compactly supported stream perturbation phi the relative velocity
changes by grad^perp phi - grad^perp phi(0). If grad phi(0) = 0, the relative velocity and the vorticity agree with
those of the reference outside the support, so (c) applies; otherwise this exterior-agreement argument does not apply.
Compact support of a vorticity perturbation alone does not give agreement of both fields on a nonempty open set
(4.29(d) treats such perturbations on the axis). The letters F, J, D, Z, E_comp, H, G, C, A, s, k, t, f, L_1, g, z, j,
tau, mu, nu, mu0, v, y0, phi, J_d, d, N, t_N, P, Q, i, n and w are local to 4.32.

4.33 Horizontal primitive reformulation and angular compatibility (beta > 2). Notation as in 4.28; s = 1/beta,
m = 1 - 2s.
(a) Reformulation. Let Psi be smooth on R^2 and odd in x, Omega = -Lap Psi, U = (-Psi_y, Psi_x), W = beta X + U - U(0)
and F = W.grad Omega + Omega. There is exactly one smooth Theta with Theta_x = F and Theta(0, y) = 0, namely Theta =
int_0^x F(u, y) du; it is even in x. With the smooth even functions A = W_1/x, B = W_2, Q = Omega/x, H = (A + 1) Q + x
A Q_x + B Q_y and S = int_0^1 t H(t x, y) dt one has F = x H, Theta = x^2 S, 2S + x S_x = H and
  W.grad Theta - (beta - 2) Theta = x^2 [A H + B S_y - (beta - 2) S],
so (T) and (V) hold for (Psi, Theta) if and only if the single equation A H + B S_y - (beta - 2) S = 0 holds on R^2.
If Psi_xy(0) = 1 + beta/2 and Omega_x(0) = 4 a0/beta, then S(0) = a0 and Theta = a0 x^2 + O(|X|^3). The canonical
inverse and the other conditions of the class are separate hypotheses.
(b) Axis normalization. For a smooth solution of (T) with these center data, t(y) = Theta(0, y) satisfies b t' =
(beta - 2) t with b'(0) = lambda2, so t vanishes near 0 (a nonzero solution behaves like |y|^{2(beta-2)/(3beta+2)}); t
vanishes on R if b has no zero other than 0, or if all zeros of b are simple (other proved propagation conditions may
replace these sufficient hypotheses). In general the smooth temperatures with Theta_x = F are int_0^x F + t(y), and
(a) is a reformulation of the subclass with Theta(0, .) = 0. (The scalar axis equation alone does not force t = 0 when
b has a degenerate zero: b = (y - 1)^2 near 1 admits t = C exp(-(beta - 2)/(y - 1)) for y > 1, 0 for y <= 1; this is
not a profile.)
(c) Angular compatibility. Let 0 < m < 1 and f smooth on R^2 \ {0}, homogeneous of degree m - 1 and odd in x; T =
int_0^x f(u, y) du (improper at the origin when y = 0), T(0, 0) = 0. Then T is continuous, homogeneous of degree m and
even in x, with T(0, y) = 0. With a = f(1, 0) the finite parts C_sigma = lim_{R -> infinity} [int_0^R f(u, sigma) du -
a R^m/m] (sigma = +-1) exist, and T = H0 + C_{sign y} |y|^m for x > 0, y != 0, with H0 smooth across y = 0. Hence T is
C^1 near the nonzero points of the horizontal axis if and only if C_+ = C_- = 0, if and only if T is smooth off 0. For
f = x r^{m-2}, C_+ = C_- = -1/m and T = (r^m - |y|^m)/m; the source x (1 + r^2)^{(m-2)/2} has a globally smooth
normalized primitive with this nonsmooth rescaled limit. The conditions concern the normalized primitive: adding
c_{sign y} |y|^m changes them to C_sigma + c_sigma = 0.
(d) Conditional application. Let a profile have Theta(0, .) = 0 and, uniformly in the angle at large radius, |V| <= C
r^{1-s}, |DV| <= C r^{-s} and F = f + O(r^{m-1-delta}) with delta > 0 and f as in (c) for m = 1 - 2s. Then r^{-m}
Theta(r e(theta)) converges in C^1(S^1) to the primitive T of f, and C_+ = C_- = 0.
(e) Horizontal offsets. Let a profile satisfy Theta(0, .) = 0, and let F be as in (a). Then, uniformly for y in
bounded sets,
  lim_{L -> infinity} int_0^L (F(x, y) - F(x, 0)) dx = 0.
Proof outline. (a) Parity and the fundamental theorem of calculus; h/x = int_0^1 h_x(t x, y) dt for odd smooth h. (b)
k/b = alpha/y + smooth, alpha = (beta - 2)/lambda2 in (0, 1); ODE uniqueness where b != 0; at a simple zero a nonzero
branch has a finite power behaviour and cannot join zero smoothly. (c) Taylor expansion of f(u, sigma) for u >= 1
(exponent m - 2 < -1), scaling, and differentiation under the integral for H0; the difference quotient in y contains
sigma C_sigma |y|^{m-1}. (d) Dominated convergence for the rescaled primitive (majorant C u^{m-1}); in tau = log r the
exact (T) for u = r^{-m} Theta reads u_tau + a u_theta = d u with ||a||_{C^1} + ||d||_{C^1} <= C e^{-s tau}, so the
angular flow and u converge in C^1; then (c). (e) The integral equals Theta(L, y) - Theta(L, 0) = int_0^y Theta_y(L,
y') dy', and |grad Theta| <= C r^{-2/beta} outside a large ball by 4.12(c), so for |y| <= A and large L it is at most
C A L^{-2/beta}.
Scope. (d) is a necessary condition under its hypotheses, which are not supplied by the slow-tail notation alone (an
additional symbol term r^{-s-eps} B(theta), 0 < eps < s, contributes -beta eps r^{-s-eps} B(theta) before degree -2s).
A finite quadrature approximation of int_0^x F must be differentiated as the field it actually defines; prescribing
its x derivative to be F is not a verification. (e) is a further necessary condition, not implied by the leading
angular conditions of (c) and (d): the source F = Theta_x with Theta = x^2 (1 + r^2)^{(m-2)/2} + (1/2) e^{-y^2} (1 -
e^{-x^2}) has a homogeneous leading part of degree m - 1, smooth on R^2 \ {0}, whose normalized primitive has C_+ =
C_- = 0, and its offset is (e^{-y^2} - 1)/2 (this source is not claimed to come from a stream). No existence or
nonexistence statement follows. Checks: the verification's exact and symbolic controls for (a) to (e); the eighteen
fits of the first horizontal-primitive search described at the end of section 6.2 meet the exterior hypotheses of (d)
but not (T).

4.34 Exactness on a prescribed disk and outside a large ball (beta > 2). Notation as in 4.28 and 4.31; s = 1/beta, m =
1 - 2s, lambda1 = (beta - 2)/2.
For every beta > 2, a0 > 0 and R0 > 0 fix a configuration of 4.31(a) for the radius R0 (the reference, with fields
Psi_*, U_*, Omega_*, Theta_*), and a radius R_ext > R0 with Psi_* = Psi_L on |X| > R_ext. There is a finite R_crit >
R_ext such that for every R >= R_crit there is a smooth configuration (Psi, Omega = -Lap Psi, Theta) with the B2
parity and the following properties. (i) It coincides with the reference on |X| < R (stream function, relative
velocity, vorticity, temperature and center data); in particular Psi = l_L x + P0, Omega = q0 x and Theta = a0 x^2
on |X| < R0, and Psi = Psi_L on the nonempty annulus R_ext < |X| < R. (ii) (T) holds on R^2; Theta = a0 xi^2 with xi
as in 4.3 (smooth, odd in x, positive on x > 0, W.grad xi = lambda1 xi), so Theta >= 0 with Theta = 0 exactly on the
axis; the whole plane is the backward basin of the source at 0; Omega > 0 on x > 0; U - U(0) is the canonical inverse
of Omega (A4). (iii) For every k >= 0, |D^k (U - U(0))| <= C_k (1 + |X|)^{1-s-k}, |D^k Omega| <= C_k (1 + |X|)^{-s-k}
and |D^k Theta| <= C_k (1 + |X|)^{m-k}, and Theta >= 0. (iv) r^s Omega(r e(theta)) -> a_tail(theta) in C^infinity(S^1)
as r -> infinity, with a_tail(pi - theta) = -a_tail(theta) and a_tail(theta) >= c_tail cos theta for cos theta >= 0,
for some c_tail > 0. (v) With R1 = 8R, R_Omega = 0 on |X| < R0 and on |X| > R1.
So (T) on R^2, (V) exactly on a prescribed disk and (V) exactly on an exterior domain are consistent together with (i)
to (iv). By (i) and 4.32 such a configuration is not a profile: R_Omega is a nonzero smooth function, odd in x, with
support in R0 <= |X| <= R1, and its nonzero set is a nonempty open subset of {R0 < |X| < R1, x != 0}.
Proof outline. (Reference.) Let N(theta) = cos^2 theta + eta sin^2 theta and p = (1 - s)/2 (B, eta as in 4.31(a)).
Outside a large disk, Omega_* = r^{-s} cos theta J(theta) + x h(X) with |D^j h| <= C_j r^{-2-s-j} and J(theta) = 2 B p
N^{p-2} [(2 - s + eta) cos^2 theta + eta (3 - s eta) sin^2 theta]; J > 0. Hence there are R_ref > 0 and kappa > 0 with
Omega_* >= kappa x r^{-1-s} on {x > 0, r >= R_ref}, and |D^j V_*| <= C_j r^{1-s-j}, |D^j Omega_*| <= C_j r^{-s-j} for
r >= R_ref. With tau = log r, H = r^{-m} Theta_* satisfies H_tau + b_* H_theta = -m (V_*.e_r/r) H/(beta + V_*.e_r/r),
b_* = (V_*.e_perp/r)/(beta + V_*.e_r/r), whose coefficients are O(r^{-s}) with all derivatives in (tau, theta);
integration along the angular flow gives |D^j Theta_*| <= C_j r^{m-j}. The dilation part annihilates the leading
vorticity term, so the reference residual Res_* = W_*.grad Omega_* + Omega_* - d_x Theta_* satisfies |D^j Res_*| <=
C_j r^{-2s-j}, and |Res_*| <= C |x| r^{-1-2s} by oddness. (Norms and linear estimates.) Fix 0 < alpha < 1. For real
gamma and j >= 0 put ||f||_{gamma;j,alpha} = sup over |z| = r >= 1 of [sum_{l <= j} r^{gamma+l} |D^l f(z)| +
r^{gamma+j+alpha} [D^j f]_alpha], the Hoelder seminorm taken on B(z, |z|/8) intersected with {|y| >= 1} (equivalently,
the C^{j,alpha} norm of r^gamma f on unit cells in (log r, theta), uniformly in the cell), and ||f||_{gamma;0,0} = sup
over |z| >= 1 of |z|^gamma |f(z)|. Let chi, rho be smooth radial cutoffs with values in [0, 1], chi = 0 on |z| <= 1,
chi = 1 on |z| >= 2, rho = 0 on |z| <= 5, rho = 1 on |z| >= 8. For e odd in z_1 with e = 0 on |z| < 5 let Q e(z) = int
[G(z - y) - G(-y) - grad G(-y).z] e(y) dy with G(z) = -(2 pi)^{-1} log |z| (the subtraction makes the integral
converge for e = O(r^{-s})), v[e] = grad^perp(chi Q e), and b[e] = -Lap(chi Q e) - e, supported in 1 <= |z| <= 2.
Splitting the kernel at |y| = 2r and near z gives (I) ||v[e]||_{s-1;j+1,alpha} <= C_j ||e||_{s;j,alpha}
and ||b[e]||_{C^j} <= C_j ||e||_{s;0,0}. For a drift w = beta z + u on |z| >= 1 with beta + u.e_r/r >= beta/2 and the
needed derivatives of u/r in (log r, theta) bounded by C r^{-s}, all characteristics leave |z| = 1 outward, and for
nu0 = beta gamma the solution of (w.grad + nu0) f = g with prescribed trace on |z| = 1 satisfies
(II) ||f||_{gamma;j,alpha} <= C [||f restricted to |z| = 1||_{C^{j,alpha}} + ||g||_{gamma+s;j,alpha}], by integrating
the equation for r^gamma f along the characteristics in (log r, theta); for j = 0 the angular flow is uniformly
Lipschitz because its coefficient b = (u.e_perp/r)/(beta + u.e_r/r) satisfies int_0^infinity sup_theta |d_theta b(tau,
theta)| d tau < infinity, which the O(r^{-s}) bounds ensure. (Scaling.) For R >= R_ref put delta = R^{-s} and rescale
z = X/R: omega_R(z) = R^s Omega_*(R z), v_R(z) = R^{s-1} V_*(R z), theta_R(z) = R^{-m} Theta_*(R z), g_R(z) = R^{2s}
Res_*(R z); these have symbol bounds uniform in R. Seek an auxiliary vorticity source Omega_c(R z) = R^{-2s} e(z) with
e odd in z_1 and e = 0 on |z| < 5; the actual vorticity change is R^{-2s} (e + b[e])(z). The scaled drift is w_e =
beta z + delta v_R + delta^2 v[e]; theta_e solves (T) for w_e with the trace of theta_R on |z| = 1; and the map is e
-> Te, where (w_e.grad + 1) Te = rho [-g_R + d_1(theta_e - theta_R) - delta v[e].grad omega_R] with zero trace on |z|
= 1 (so Te = 0 on |z| <= 5). (Fixed point.) Let the strong ball be the set of odd e vanishing on |z| < 5
with ||e||_{s;1,alpha} <= K, with the weak metric ||e_1 - e_2||_{s;0,alpha}. By (I) and (II), ||theta_e -
theta_R||_{-m;2,alpha} <= C delta^2 ||e||_{s;1,alpha}, ||theta_{e_1} - theta_{e_2}||_{-m;1,alpha} <= C delta^2 ||e_1 -
e_2||_{s;0,alpha}, ||Te||_{s;1,alpha} <= C_*(1 + delta K) and ||Te_1 - Te_2||_{s;0,alpha} <= C_* delta (1 + K) ||e_1 -
e_2||_{s;0,alpha}; the term delta^2 v[e_1 - e_2].grad Te_2, which loses a derivative, is controlled by the strong
bound on Te_2. With K = 2 C_* and delta small, T maps the strong ball into itself and has contraction factor at most
1/2 in the weak metric. The strong ball is complete in the weak metric: a Cauchy sequence has locally uniformly
bounded first derivatives with uniform alpha-Hoelder bounds, so a subsequence converges in C^1 on compact sets to the
weak limit, and the weighted bounds, the parity and the support condition pass to the limit. So T has a fixed point e,
the weak limit of the iterates e_{n+1} = T e_n, e_0 = 0, each of which is smooth by (I) and (II) at every order.
(Smoothness at one radius.) Put v_n = v[e_n], u_n = delta v_R + delta^2 v_n, w_n = beta z + u_n and P_n = grad
theta_{e_n}, so that (w_n.grad + 2) P_n = -(D u_n)^T P_n. All derivative tensors carry their Euclidean
(Hilbert-Schmidt) norms. The fixed low-order reference bounds give constants M_1, M_2, independent of n and of R >=
R_crit, with |u_n|/r + |D u_n| <= M_1 r^{-s} and |P_n| <= M_2 r^{-2s}; on the collar 3 <= |z| <= 4 every derivative of
v_n and of P_n is bounded uniformly in n. With eps = s/4, H_k = 8 M_1 (k + 2) and the weights w_{gamma,k} =
r^{gamma+k-1-eps} exp(H_k r^{-s}/2), define on r > 4 the energies E_{n,k} = ||w_{s,k} D^k e_n||_{L^2}, T_{n,k}
= ||w_{2s,k} D^k P_n||_{L^2} and B_{n,k} = ||w_{s,k} D^{k+1} v_n||_{L^2}. For gamma = s or 2s the weighted transport
coefficient of the k-th derivative is 1/4 - (gamma + k - 1 - eps) u_n.e_r/r + (H_k s/2)(beta + u_n.e_r/r) r^{-s}, and
the last term absorbs the (k + 1) |D u_n| commutator terms, leaving at least 1/4; so a differentiated transport
equation with weighted source norm F gives an energy at most 4F + C_k. The planar div-curl identity applied to a_k D^I
v_n (|I| = k, a_k = zeta w_{s,k}, zeta = 0 on r <= 3 and zeta = 1 on r >= 4; div v_n = 0 and curl v_n = -e_n there)
gives B_{n,k} <= E_{n,k} + C_k, with coefficient 1, because grad a_k is one weight power lower, so that its term is
controlled by the velocity energy of order k - 1. All intermediate products are of lower order by Sobolev embedding on
rescaled annuli, and the only top-order couplings give T_{n,k} <= 4 delta^2 M_2 4^{-s} E_{n,k} + C_k and E_{n+1,k} <=
16 delta^2 M_2 4^{-2s} E_{n,k} + C_k. The single condition 32 delta^2 M_2 <= 1, independent of k, gives bounds uniform
in n at every order k (the constants C_k depend on k but do not change R). The contraction gives e_n -> e locally
uniformly and the temperature difference estimate gives theta_{e_n} -> theta_e locally in C^1; hence for every k,
subsequences of (e_n, grad theta_{e_n}) converge weakly in H^k_loc to (e, grad theta_e), distributional
differentiation identifies all derivative limits, and e and theta_e are smooth. These bounds give |D^j e| <= C_j
r^{-s+eps-j}; commuting derivatives through the fixed-point equations (damping 1 + j beta for D^j e, 2 + j beta for
D^j P_inf) and integrating along the outgoing characteristics restore |D^j e| <= C_j r^{-s-j} and |D^j P_inf| <= C_j
r^{-2s-j} for P_inf = grad theta_e, and (I) gives the velocity bounds; scaled back, the bounds on P_inf and those on
Theta_* give the temperature derivative bounds of (iii). (Conclusion.) Psi = Psi_* + chi(X/R) Phi[Omega_c], where
Phi[Omega_c](R z) = R^{2-2s} (Q e)(z); the correction vanishes on |X| <= R, which gives (i) and (v) on |X| < R0.
For |X| > 4R the vorticity equation of the fixed point reads R_Omega = (rho(X/R) - 1){Theta_x - W.grad Omega_* -
Omega_*} (W and Theta of the new configuration, Omega_* of the reference), which vanishes for |X| > 8R. Positivity
follows from |e + b[e]| <= C K |z_1| |z|^{-1-s} and the lower bound of Omega_*, for delta small. The relative velocity
is the canonical inverse by (A4); the basin and Theta = a0 xi^2 follow as in 4.31(b) by transporting the reference xi
from |X| = R with eigenvalue lambda1. Angular limit: for |X| > 8R the vorticity equation holds exactly, and with a =
r^s Omega, tau = log r, v_r = V.e_r/r and v_t = V.e_perp/r it reads a_tau + [v_t/(beta + v_r)] a_theta = [s -
1/(beta + v_r)] a + r^s Theta_x/(beta + v_r). Since s = 1/beta, the coefficients v_t/(beta + v_r) and s - 1/(beta +
v_r) and the forcing r^s Theta_x/(beta + v_r) are O(r^{-s}) with all derivatives in (tau, theta), hence integrable in
tau; integration along the angular flow gives the limit a_tail in C^infinity(S^1), and the bound Omega >= (kappa/2) x
r^{-1-s} on x > 0 outside B_R gives c_tail = kappa/2. R_crit = max{R_ref, R_ext + 1, R0 + 1, delta0^{-beta}}, where
delta0 satisfies a finite set of low-order outgoingness, contraction, positivity and coupling conditions; no
enlargement depending on the derivative order is needed. The complete derivation, with the proofs of (I), (II) and of
the weighted energy estimates, is in the proof packet listed for 4.34 in Table 8.1.
Scope. A compatibility statement for a compactly forced configuration, not a profile and not an exclusion. It holds
for every fixed beta > 2, a0 > 0 and R0 > 0, with R1 depending on these through the chosen reference (for each fixed
reference and each R >= R_crit the construction gives R1 = 8R); it gives no closed bound on R1 and no bound uniform
over reference choices. R_Omega is not identically zero (4.32). For a fixed reference, the configurations agree with
it on |X| < R by (i), so they converge to it in C^infinity on compact sets as R -> infinity, and the reference is not
a profile (4.32). Since (T) holds on R^2, the identity in the proof of 4.32(d) gives E_comp = L_1 R_Omega, with the
operator L_1 of order at most 2 written there. On the annulus R_ext < |X| < R the relative velocity and the vorticity
are those of Psi_L (U(0) = U_L(0), as in 4.32(c)), so E_comp is that of Psi_L, which vanishes on no nonempty open set
(4.32(b)). Hence R_Omega vanishes on no nonempty open subset of that annulus, and on every fixed ball whose closure
lies in |X| > R_ext it equals the residual of the reference for all large R. Whole-axis flatness as in 4.31(b) is not
claimed, nor (V) on any part of the intermediate annulus, nor a prescribed angular tail (a_tail is that of the
construction), nor the restricted expansions of 4.26(d). The constant c_tail is existential; it is not asserted to
equal any center constant.

4.35 The axis subsystem in G: relations, a compatible positive vorticity and the axis coefficient (beta > 2). Let
beta > 2, a0 > 0, lambda1 = (beta - 2)/2, lambda2 = 1 + 3 beta/2, ell = lambda2/beta, d = 1/beta, and let b, a_ax =
Theta_xx(0, y)/2 and q = Omega_x(0, y) be the axis functions of 4.13 (a_ax is the coefficient written a in 4.13(i)),
with Lambda = 2 lambda2 and M = 2 beta + 1 as there. Q_+ is the constant of 4.21(a); a_tail denotes an angular
vorticity tail.
(a) (Axis relations.) Let the profile be in G and (xi, eta) the coordinates constructed in the proof of 4.18(b); they
satisfy Theta = a0 xi^2 and D(xi, eta)(0) = I. Put eta_ax(y) = eta(0, y) and H_ax(y) = lim_{x -> 0} (Omega/xi)(x, y).
Then eta_ax(0) = 0, eta_ax'(0) = 1, eta_ax' > 0 and
  a_ax = a0/eta_ax'^2,   q = H_ax/eta_ax',   b eta_ax' = lambda2 eta_ax,   b H_ax' + (beta/2) H_ax = 2 a0/eta_ax'.
Conversely, let b be smooth with b(0) = 0, b'(0) = lambda2, and let N be a connected half-axis interval adjoining 0 on
which b != 0. Among solutions of the axis system 4.13(i) on N that are continuous at the center with a_ax(0) = a0 and
q bounded there, the substitutions b eta_ax' = lambda2 eta_ax, eta_ax(0) = 0, eta_ax'(0) = 1, H_ax = eta_ax' q give an
equivalence with the displayed relations. This holds also when kappa != 0 in 4.18(b).
(b) (A positive canonical vorticity compatible with the axis subsystem.) For every beta > 2 and a0 > 0 there are a
smooth Psi, odd in x, with Omega = -Lap Psi, and smooth functions b, eta_ax, H on R, such that: Omega > 0 on {x >
0}; |Omega| <= C (1 + |X|)^{-d}, and r^d Omega(r (cos theta, sin theta)) -> a_tail(theta) uniformly in theta, with
a_tail continuous and positive on the open right semicircle; U_rel = U - U(0) is the canonical inverse (A4) of Omega,
U(0) = 0 and |U_rel| <= C (1 + |X|)^{1-d}; Psi_xy(0) = 1 + beta/2; b(y) = beta y + U_rel,2(0, y) has the sign of y;
eta_ax(0) = 0, eta_ax' > 0, eta_ax'(0) = 1, H > 0; and b eta_ax' = lambda2 eta_ax, Omega_x(0, y) = H/eta_ax', b H' +
(beta/2) H = 2 a0/eta_ax'. Then a_ax := a0/eta_ax'^2 and q := Omega_x(0, y) satisfy 4.13(i) with a_ax(0) = a0, and
a_ax, q > 0. One construction has, for every L >= L_*(beta, a0),
  b = b_L,   b_L(y) = lambda2 y (1 + (y/L)^2)/(1 + ell (y/L)^2),   eta_ax(y) = y (1 + (y/L)^2)^{(ell - 1)/2}.
(c) (The axis coefficient as a functional of b.) Let b be smooth on [0, infinity) with b(0) = 0, b'(0) = lambda2, b >
0 on (0, infinity) and b(y) = beta y + O(y^{1-d}) as y -> infinity. Put p1 = (2 beta + 1)/lambda2, r1 = (beta +
1)/lambda2 and zeta_b(y) = y exp int_0^y (lambda2/b(s) - 1/s) ds. Then the axis system 4.13(i) on [0, infinity) with
a_ax(0) = a0 has exactly one solution with q bounded near 0, namely
  a_ax = a0 b^2/(lambda2^2 zeta_b^2),   q = (2 a0/lambda2^2) b zeta_b^{-p1} int_0^y zeta_b(s)^{-r1} ds,
and zeta_b(y) = C_b y^ell (1 + O(y^{-d})) with C_b > 0, so that
  Q_+(b) := lim_{y -> infinity} y^{1+d} q(y) = (2 a0 beta/lambda2^2) C_b^{-p1} int_0^infinity zeta_b(s)^{-r1} ds   in (0, infinity).
If b1 >= b2 on (0, infinity), then Q_+(b1) >= Q_+(b2), with equality only if b1 = b2. For the functions b_L of (b),
Q_+(b_L) = (a0 beta/lambda2^2) B(1/(4 ell), 1/(2 beta)) L^{1+d} for every L > 0, where B is Euler's Beta function. For
a class A profile with y_+ = infinity, b satisfies these hypotheses (4.12(e)) and Q_+(b) is the constant Q_+ of
4.21(a). On the lower half-axis the same holds for Q_- with y -> -y and b replaced by -b(-y), so the order of the
signed functions b is reversed there.
(d) (Weighted vorticity integrals in G.) Let the profile be in G with Theta_x > 0 on {x > 0} and kappa = 0 in 4.18(b).
On {x > 0} put xi = exp(lambda1 t), eta = sigma exp(lambda2 t), and let w = exp(-nu t) F(sigma) with F in
C_c^infinity(R) nonnegative and not identically zero. Then int_{x>0} Omega w dX is finite exactly when 2 beta - 1 < nu
< 2 beta + lambda1, and in this range
  (nu + 1 - 2 beta) int_{x>0} Omega w dX = int_{x>0} Theta_x w dX > 0.
Proof outline. (a) In the proof of 4.18(b), u_x(0) = 1 (P(0) = a0), the area coordinate has eta0_y(0) = 1 and the
shear term added there is even in u, so D(xi, eta)(0) = I. By parity xi = 0, xi_y = 0 and eta_x = 0 on the axis, and
det D(xi, eta) = 1 gives xi_x(0, y) eta_ax'(y) = 1; both factors are continuous, nonzero and equal to 1 at 0, so both
are positive on the whole axis, and the normal form at 0 gives eta_ax(0) = 0. Theta = a0 xi^2 gives a_ax = a0 xi_x(0,
y)^2; Omega and xi are odd in x with xi_x(0, y) != 0, so Omega/xi extends smoothly across the axis and q = H_ax
xi_x(0, y). Since W_1 = 0 on the axis and xi^k = 0 there, the normal form of 4.18(b) gives b eta_ax' = lambda2 eta_ax.
Differentiating, b eta_ax'' = (lambda2 - b') eta_ax'; substituting q = H_ax/eta_ax' in b q' + (M - b') q = 2 a_ax and
using M - lambda2 = beta/2 gives the H_ax relation, and the a_ax relation of 4.13(i) follows from a_ax = a0/eta_ax'^2
in the same way. The resonant term kappa xi^k vanishes on xi = 0, so kappa != 0 changes nothing. Conversely, on N the
function eta_ax(y) = y exp int_0^y (lambda2/b(s) - 1/s) ds is the unique solution of b eta_ax' = lambda2 eta_ax with
eta_ax(0) = 0, eta_ax'(0) = 1, and eta_ax' > 0 there; the first equation of 4.13(i) then fixes a_ax = a0/eta_ax'^2,
the substitution for q is invertible, and boundedness at the center gives q(0) = 4 a0/beta. (b) Unit scale. Let tau =
(ell - 1)/2, n1 = 1/(2 ell), k1 = tau (1 - n1), s1 = (1 + d)/2 and c = 1 + beta/2. Take eta_1(y) = y (1 + y^2)^tau and
b_1(y) = lambda2 y (1 + y^2)/(1 + ell y^2); then eta_1' = (1 + y^2)^{tau - 1} (1 + ell y^2) > 0, b_1 eta_1' = lambda2
eta_1 and f(y) := b_1(y) - beta y = c y/(1 + ell y^2). The function H_1(y) = (2/lambda2) (1 + y^2)^{-tau n1} int_0^1
u^{n1 - 1} (1 + y^2 u^2)^{-k1} du is smooth, even and positive, solves b_1 H_1' + (beta/2) H_1 = 2/eta_1' (multiply by
eta_1^{n1} and integrate), and H_1(0) = 4/beta. Writing k_1 = H_1/eta_1', the gamma integral for each factor and
Tonelli give k_1(y) = int_0^infinity exp(-t y^2) g(t) dt with a density g > 0 satisfying g(t) <= C t^{s1 - 1}, g(t) <=
C exp(-c0 t) for t >= 1 and g(t) ~ g0 t^{s1 - 1} as t -> 0 with g0 > 0 (with z = y^2 and alpha1 = tau (1 + n1), (1 +
z)^{1 - alpha1}/(1 + ell z) = (1/ell)(1 + z)^{-alpha1} + (1 - 1/ell)(1 + z)^{-alpha1}/(1 + ell z), and g is a positive
combination of convolutions of the Laplace densities t^{alpha1 - 1} e^{-t}/Gamma(alpha1), e^{-t/ell}/ell and t^{n1/2 -
1} Gamma(d/2, t)/(2 Gamma(k1)) of the factors, Gamma(a, t) the upper incomplete Gamma function). The kernel K_t = x^3
T^{-3/4} exp(-t y^2/T), T = 1 + 4 t x^2, has Lap K_t = x T^{-3/4} exp(-w) P_K(z, w) with z = 4 t x^2/T in [0, 1), w =
t y^2/T and P_K = 6 - 11 z + (21/4) z^2 + z (15 - 14 z) w + 4 z^2 w^2 = 1/4 + (1 - z)(23 - 21 z)/4 + z (15 - 14 z) w +
4 z^2 w^2 >= 1/4 on z in [0, 1], w >= 0, together with (K_t)_x(0, y) = 0 and (Lap K_t)_x(0, y) = 6 exp(-t y^2). So U_1
= (1/6) int_0^infinity K_t g(t) dt is smooth and odd in x, with (U_1)_x(0, y) = 0, (Lap U_1)_x(0, y) = k_1(y), and c'
x (1 + r^2)^{-s1} <= Lap U_1 <= C x (1 + r^2)^{-s1} on {x > 0}: Lap K_t = x Phi_t with 0 < Phi_t <= C (1 + t
r^2)^{-3/4} (1 + t r^2 = T (1 - 3z/4 + w)), the upper bound uses s1 < 3/4, and the lower bound uses the interval
t0/(2(1 + r^2)) <= t <= t0/(1 + r^2) with t0 small, on which g(t) >= c t^{s1 - 1}. The substitution t = v/r^2, g(t) ~
g0 t^{s1 - 1} and the majorant C v^{s1 - 1}(1 + v)^{-3/4} give a uniform continuous angular limit of r^d Lap U_1 (2 s1
= 1 + d), positive on the open right semicircle. Also |grad K_t| <= C x^2 (1 + t r^2)^{-3/4}, so |grad U_1| <= C x^2
(1 + r^2)^{-s1} <= C (1 + r)^{1 - d}. The strain block psi_c = c x y/(1 + ell r^2) + j(y) x^3/(6 (1 + x^2)^3), j(y) =
4 c ell y (3 + ell y^2)/(1 + ell y^2)^3, satisfies (psi_c)_x(0, y) = f(y), (Lap psi_c)_x(0, y) = 0 and |Lap psi_c| <=
C x (1 + r^2)^{-3/2} on {x > 0}. For every A >= A_*, with A_* > sup_{x > 0} |Lap psi_c|/Lap U_1 (finite by these
bounds), Psi = psi_c - A U_1 has Omega = A Lap U_1 - Lap psi_c > 0 on {x > 0} with the tail of A Lap U_1; Psi_x(0, y)
= f(y) gives b = b_1 and U(0) = 0, Psi_xy(0) = c, Omega_x(0, y) = A k_1 = H/eta_1' with H = A H_1, and the H relation
holds with a0 = A. The once-subtracted Biot-Savart integral of Omega converges absolutely and is O(1 + r^{1-d}); its
difference from U (sublinear by the bounds on grad U_1 and grad psi_c) is harmonic, sublinear and zero at 0, hence 0.
Scaling. For prescribed a0 put L = A/a0 and Psi_L(X) = L^2 Psi(X/L); then Omega_L(X) = Omega(X/L), b becomes L
b_1(y/L) = b_L, eta_ax becomes L eta_1(y/L), H becomes H(y/L)/L = a0 H_1(y/L) (A = a0 L), and the axis source
coefficient becomes A/L = a0; L >= A_*/a0 =: L_* is arbitrary. (c) With b = W_2(0, y), the first equation of 4.13(i)
and zeta_b' = lambda2 zeta_b/b give (a_ax zeta_b^2/b^2)' = 0, and a_ax(0) = a0 fixes the constant since zeta_b/y -> 1
and b/y -> lambda2. Writing q = b h, the second equation becomes (zeta_b^{p1} h)' = (2 a0/lambda2^2) zeta_b^{p1 - 2},
and p1 - 2 = -r1; the bounded solution is the one displayed (the homogeneous solution b zeta_b^{-p1} is unbounded at 0
since p1 > 1), and p1 + r1 = 2 gives q(0) = 2 a0/(lambda2 (1 - r1)) = 4 a0/beta. From lambda2/b - ell/y = O(y^{-1-d})
one gets zeta_b = C_b y^ell (1 + O(y^{-d})); since ell r1 = 1 + d > 1 the integral converges, and p1 ell - 1 = 1 + d
gives the limit. If b1 >= b2 then zeta_{b1} <= zeta_{b2} and C_{b1} <= C_{b2} (log(C_{b1}/C_{b2}) = lambda2
int_0^infinity (1/b1 - 1/b2) ds <= 0), so the integral increases and C^{-p1} increases; if b1 != b2 the inequality is
strict on an interval and so is the conclusion. For b_L, zeta_{b_L} = y (1 + (y/L)^2)^{(ell - 1)/2}, C_{b_L} = L^{1 -
ell}, and the substitution y = L u^{1/2} gives int_0^infinity zeta_{b_L}^{-r1} = (L^{1 - r1}/2) B(1/(4 ell), 1/(2
beta)); the exponent of L is p1 (ell - 1) + 1 - r1 = 1 + d. For a class A profile, b = beta y (1 + O(y^{-d})) by
4.12(e), q is bounded at 0, and the limit is Q_+ by 4.21(a). (d) The normalized coordinates of (a) map R^2 onto R^2
(the flow of W is complete, W having linear growth, and every point of the model plane enters a neighbourhood of 0
under the backward model flow), with {xi > 0} = {x > 0}. For kappa = 0 the field W is d_t in the coordinates (t,
sigma), and dX = d xi d eta = lambda1 exp(2 beta t) dt d sigma (lambda1 + lambda2 = 2 beta). As t -> -infinity, Omega
= (4 a0/beta) x (1 + o(1)) with x comparable to exp(lambda1 t) uniformly on supp F; as t -> infinity, r -> infinity
uniformly on supp F (properness of the conjugacy), and r'/r = beta + O(r^{-d}) gives first r >= c exp(beta t/2) and
then, the error being integrable in t, c exp(beta t) <= r <= C exp(beta t) uniformly on supp F, so Omega <= C exp(-t)
by 4.12(e), and exp(t) Omega is increasing in t since d_t (exp(t) Omega) = exp(t) Theta_x > 0, which gives a matching
positive lower bound. Hence the integral is finite exactly in the stated range of nu. There the boundary terms of int
(d_t Omega + Omega) exp((2 beta - nu) t) dt vanish, and integration by parts on finite time intervals and monotone
convergence (Theta_x w >= 0) give the identity.
Scope. (a) and (c) are necessary relations on the axis, and (d) is a necessary property of the profiles to which it
applies; none is an exclusion. (b) is a compatibility statement: the fields of (b) come with no temperature field and
neither off-axis equation is verified for them, so they are not shown to extend to profiles, do not establish
existence in G, and do not exclude axis arguments that use further information on a profile. Their positive Omega has
the sign of 4.21(d), but no Theta satisfying the hypothesis of 4.21(d) is supplied. Together (b) and (c) show that, at
fixed beta and a0, Q_+(b) has no finite upper bound among the fields of (b) (Q_+(b_L) -> infinity as L -> infinity;
the constants in the bounds of (b) may depend on L); this gives no unboundedness of Q_+ among profiles in G and does
not preclude bounds that use further equations. Rescaling one fixed field, Psi(X) -> L^2 Psi(X/L), changes a0 to a0/L
and Q_+ to L^d Q_+; the family of (b) also changes the unit-scale amplitude (A = a0 L), which gives the exponent 1 +
d. (d) concerns these nonnegative weights only and gives no sign contradiction; sign-changing weights and identities
combining the off-axis inverse with transport are not addressed. The letters eta_ax, H_ax, H, N, b_L, L, L_*, p1, r1,
zeta_b, C_b, tau, n1, k1, s1, alpha1, f, eta_1, b_1, H_1, k_1, g, g0, c0, K_t, Phi_t, T, z, w, P_K, U_1, psi_c, j, A,
A_*, c', t, t0, sigma, nu and F are local to 4.35.

4.36 Renormalized impulse under a far-field expansion (beta > 2). Notation as in 4.34; Z_crit = {M/N > 2 : M, N
coprime positive integers, N <= 3}.
Let beta > 2. Let Psi (odd in x) and Theta (even in x) be smooth on R^2, Omega = -Lap Psi, V = (-Psi_y, Psi_x) with
V(0) = 0 and W = beta X + V, with (T) on R^2, x R_Omega in L^1(R^2), and Omega = O(r^{-s}), V = O(r^{1-s}), Theta =
O(r^{1-2s}). Suppose that outside a ball Psi = P + delta Psi and Theta = H + delta Theta, where P and H are finite
sums of terms r^e (log r)^j c(theta) with j a nonnegative integer and smooth angular coefficients, terms with equal e
and j combined; the degrees e of P lie in {2 - K s - n : K, n integers, K >= 1, n >= 0}, apart from homogeneous
harmonic terms, without logarithmic factors, of the degrees 1, -1, -2, ...; the degrees of H lie in {1 - L s - n : L,
n integers, L >= 2, n >= 0}; and, uniformly in theta, delta Psi = o(r^{-1}), |grad delta Psi| = o(r^{-2}), |D^2 delta
Psi| = o(r^{-3}) and delta Theta = o(r^{-2}). Let F_rho(P, H) be the right side of the boundary identity in the proof
outline below with Psi, Theta replaced by P, H. Then
  int x R_Omega dX = [rho^0 (log rho)^0] F_rho(P, H),
the coefficient of rho^0 (log rho)^0 in this finite sum of terms rho^alpha (log rho)^j. If beta is not in Z_crit, and
D denotes the coefficient of x/|X|^2 in P, then
  int x R_Omega dX = 2 pi (1 - 3 beta) D.
(a) Every class A profile with beta not in Z_crit and such an expansion has D = 0. Equivalently, the coefficient of
rho^0 (log rho)^0 in the expansion of int_{|X| < rho} x Omega dX, which equals 2 pi D, vanishes: the renormalized
impulse of such a profile is zero.
(b) Positivity alone, even together with parity, the normalization V(0) = 0, the stated growth, (T) and an exact
finite exterior expansion, does not determine the sign of D. For Omega = x f(r) with f > 0 smooth (smooth in r^2
near 0) and f = r^{-s-1} for r >= 1, the stream with V(0) = 0 is Psi = x h(r), h(r) = -int_0^r u^{-3} I(u) du, I(u) =
int_0^u t^3 f(t) dt, and D = (I(1) - 1/(3 - s))/2, which takes every value in (-1/(2(3 - s)), infinity) for suitable
f. With Theta = 0 these fields satisfy (T); they violate (V) arbitrarily far out, so they do not satisfy the
hypothesis x R_Omega in L^1.
Proof outline. With p = Psi_x, q = Psi_y and n the outward normal, integration by parts, div(x W) = 3 beta x + V_1,
V_1 Omega = d_x(p q) + d_y((q^2 - p^2)/2), int_{|X|<rho} x Omega dX = oint (Psi n_x - x d_n Psi) ds and (3 beta - 2)
int_{|X|<rho} Theta dX = oint Theta W.n ds (from (T)) give
  int_{|X|<rho} x R_Omega dX = oint_{|X|=rho} [(x Omega + Theta/(3 beta - 2)) W.n - x Theta n_x - p q n_x
                               - ((q^2 - p^2)/2) n_y + (1 - 3 beta)(Psi n_x - x d_n Psi)] ds.
The left side tends to int x R_Omega dX. The remainder bounds make the error of substituting P and H on the right o(1)
(the largest linear errors are O(rho^3) o(rho^{-3}) and O(rho^2) o(rho^{-2}); the quadratic errors are o(rho^{-s}); no
bound on third derivatives is needed); a finite sum of terms rho^alpha (log rho)^j with a finite limit has no terms
with alpha > 0 and a constant zero-power part, which gives the first formula. A stream term of degree e enters with
the power e + 1 (linear terms) and e + e' - 1 (quadratic terms, e' a second stream degree), and a temperature term of
degree g with g + 2 and g + e; logarithms do not alter these powers, although differentiation can lower the
logarithmic powers and contribute to the log-free coefficient when the power is zero. For the ordinary degrees above,
a zero power requires an integer multiple of s to equal 1, 2 or 3, so beta in Z_crit; pairs with the harmonic term of
degree 1 (c x) require an integer multiple of s equal to 1 or 2; the harmonic terms of degree <= -2 have negative
linear powers and give no zero power in pairs, and the pair of harmonic degrees (1, -1) has power -1. For beta not in
Z_crit no ordinary stream term has degree -1, so the odd terms of degree -1 are D r^{-1} cos theta; a term r^e
c(theta) contributes (1 - e) rho^{e+1} oint c(theta) cos theta d theta to oint (Psi n_x - x d_n Psi), and the dipole
has no vorticity; this gives 2 pi (1 - 3 beta) D. (b) Lap(x h(r)) = x (h'' + 3 h'/r) = -x f, I(r) = O(r^4) at 0, and
for r >= 1, I(r) = r^{3-s}/(3 - s) + c0 with c0 = I(1) - 1/(3 - s), so Psi = -r^{2-s} cos theta/((3 - s)(1 - s)) + C r
cos theta + (c0/2) r^{-1} cos theta with C = (1/(1 - s) - int_0^1 t f(t) dt)/2 (so V(0) = 0 does not force C = 0);
int_{|X|<rho} x Omega dX = pi I(rho); I(1) is arbitrarily small for f small on most of [0, 1], and arbitrarily large
after adding an interior bump; for r >= 1, R_Omega = x y [2 r^{-2s-2}/((3 - s)(1 - s)) - (s + 1) C r^{-s-3} + (1 - s)
D r^{-s-5}].
Scope. A necessary condition under an expansion hypothesis. 4.16 and 4.26 give only the first terms of Omega and
Theta; the expansion and remainder hypotheses are proved for class A profiles with beta > 2 in 4.37, so that (a)
applies to every class A profile with beta > 2 not in Z_crit. For beta in Z_crit the first formula still holds, but
further terms can contribute to the coefficient (at beta = 3: stream pairs of degrees (5/3, -2/3), (4/3, -1/3), (1,
0), (2/3, 1/3), temperature and stream degrees adding to 0, the stream degree -1 with its logarithms, and the
temperature degree -2), and the reduction to D is not established there. Conversely, every beta in Z_crit permits
additional zero-power candidates in these degree lists; this does not assert that they occur with nonzero coefficients
in a solution. Global (T) is essential: for Psi = 0 and a nonzero, nonnegative, compactly supported temperature even
in x, D = 0 and R_Omega = -Theta_x is compactly supported, but int x R_Omega dX = int Theta dX > 0. No sign
contradiction with the other identities of this report was found. For configurations satisfying all the hypotheses
above, including global (T) and beta not in Z_crit, the residual moment int x R_Omega dX of 6.3 is determined by the
exterior dipole coefficient; in particular it is unchanged by interior modifications that preserve these hypotheses
and the exterior fields. Checks: the verification's independent proof and its exact controls, including the example of
(b) and the boundary identity. The letters p, q, P, H, delta Psi, delta Theta, F_rho, D, K, L, M, N, n, j, e, e', g,
f, h, I, c0 and C are local to 4.36.

4.37 Finite exterior expansions (beta > 2). Notation as in 4.36; m = 1 - 2s. For a smooth function f outside a ball
and a real nu, write f in S^nu if for every integer j >= 0 there are C_j and R_j with |D^j f(X)| <= C_j r^{nu-j} for
r >= R_j, uniformly in the angle; E = {K s + n : K, n integers, K >= 1, n >= 0}.
Let beta > 2. Let Psi (odd in x) and Theta (even in x) be smooth on R^2, Omega = -Lap Psi and V = (-Psi_y, Psi_x) with
V(0) = 0, with Omega in S^{-s}, V in S^{1-s} and Theta in S^m, and with (T) and (V) outside a ball. Then for every mu
in (3, 4) not in E there are finite sums P, odd in x, and H, even in x, of terms r^e (log r)^j c(theta) (j a
nonnegative integer, c smooth), the degrees of P in {2 - K s - n : K >= 1, n >= 0} together with homogeneous harmonic
terms C x and D x/|X|^2 without logarithmic factors, and the degrees of H in {1 - L s - n : L >= 2, n >= 0}, such that
  Psi - P in S^{2-mu},   Theta - H in S^{1-s-mu}.
The terms of P of degree above 2 - mu and of H of degree above 1 - s - mu are determined by Psi and Theta. In
particular P, H and the remainders satisfy the expansion and remainder hypotheses of 4.36; the identity of 4.36
additionally requires (T) on R^2 and x R_Omega in L^1(R^2), which holds here because (V) outside a ball makes R_Omega
compactly supported, and its reduction to 2 pi (1 - 3 beta) D requires beta not in Z_crit.
(a) Every class A profile with beta > 2 satisfies these hypotheses. Hence the expansion hypothesis of 4.36(a) holds
for every class A profile with beta > 2, and every class A profile with beta > 2 not in Z_crit has D = 0.
Proof outline. (1) Leading terms. In polar coordinates (T) and (V) read (beta r d_r + 1) Omega = -V.grad Omega +
Theta_x and (beta r d_r - (beta - 2)) Theta = -V.grad Theta, with right sides in S^{-2s} and S^{1-3s}; integrating
d_{log r}(r^s Omega) and d_{log r}(r^{-m} Theta) from infinity gives Omega = r^{-s} a + S^{-2s} and Theta = r^m A +
S^{m-s} with smooth a and A. (2) Poisson remainder lemma. If rho is smooth on R^2, odd in x and in S^{-mu} outside a
ball, 0 < mu < 4, mu != 1, 3, then the unique smooth stream Z, odd in x, with -Lap Z = rho, grad Z(0) = 0 and
sublinear gradient lies in S^{2-mu} if mu < 1, equals C x + S^{2-mu} if 1 < mu < 3, and equals C x + D x/|X|^2 +
S^{2-mu} if 3 < mu < 4, where C = -(1/(2 pi)) int y_1 rho(Y)/|Y|^2 dY and D = (1/(2 pi)) int y_1 rho(Y) dY (absolutely
convergent in the respective ranges). The proof represents Z by the twice-subtracted logarithmic kernel, splits the
integral at |Y| = r/2 and |Y| = 2r, removes the first multipole for mu > 3, and obtains the derivative bounds from
local Newton potentials and interior harmonic estimates on balls of radius comparable to r. (3) Power-logarithmic
inversion. Since Lap(r^e Q(log r, theta)) = r^{e-2}[(d_theta^2 + e^2) Q + 2 e d_t Q + d_t^2 Q] (t = log r), every
source r^{e-2} B(log r, theta), B polynomial in log r with smooth odd coefficients, has a particular stream r^e Q with
Q polynomial in log r (angular resonances add at most one power of log r; at e = 0 the angular kernel has no odd
element). (4) Induction. All weights used below lie in (s, 4) and outside E and {1, 3}. If Omega and Theta have finite
expansions of the stated kinds with remainders in S^{-mu} and S^{1-s-mu}, then (3), applied term by term with a cutoff
near 0, and (2) give P with remainder S^{2-mu}, and the products in -V.grad Omega + Theta_x and -V.grad Theta have
degrees in -E and in the temperature family, up to remainders in S^{-mu-s} and S^{1-mu-2s}; the radial integration u =
-(r^{-s}/beta) int_r^infinity t^{s-1} g(t, theta) dt of (beta r d_r + 1) u = g (and its analogue for Theta) improves
the remainders by s, with no resonance below the leading degrees. To reach a prescribed mu in (3, 4) not in E, start
from (1) with a weight mu_0 in (s, 2s) not in E and, while mu_k <= mu - s, choose mu_{k+1} in (mu_k + s/3, mu_k +
2s/3) outside E and {1, 3}; after finitely many steps mu - s < mu_k < mu, and the last step goes to mu. Every
increment is less than s, and every Poisson inversion uses a weight below 4 other than 1 and 3. Uniqueness: after
equal powers of r and log r are combined, the angular coefficients of P above degree 2 - mu and of H above degree 1 -
s - mu are unique, since a highest nonzero term of a difference cannot lie in the lower symbol class; in each resonant
particular inversion of (3) the log-free angular-kernel coefficient is set to zero, and C and D denote the total
log-free coefficients of x and x/|X|^2. Since 3 is in E exactly when beta is in Z_crit, outside Z_crit no ordinary
term of P has degree -1, and D is the coefficient of 4.36. (5) Class A. For a class A profile with beta > 2, U - U(0)
= V is the canonical relative inverse of (A4), and the physical fields of 4.16 step (1) have derivatives of every
order bounded on 1 <= |z| <= 2 uniformly for 0 < tau <= 1 (4.16 step (2)); with r = tau^{-beta}, D_z^alpha omega(-tau,
z) = r^{s+|alpha|} (D^alpha Omega)(r z), D_z^alpha theta(-tau, z) = r^{-m+|alpha|} (D^alpha Theta)(r z) and D_z^alpha
u(-tau, z) = r^{s-1+|alpha|} (D^alpha V)(r z), which are the symbol bounds. Class A profiles satisfy (T) and (V) on
R^2, and 4.36(a) gives D = 0 outside Z_crit.
Scope. A structural statement about the far field. It does not determine the sign of D or prove D != 0, does not
assert convergence of an infinite expansion, gives no estimate uniform as beta tends to 2 or to infinity, and does not
apply at beta = 2. With (a), the condition D = 0 of 4.36(a) is a proved necessary condition for every class A profile
with beta > 2 not in Z_crit; it does not decide existence. Checks: the verification's independent proof and its
controls (Poisson inversions of power and logarithmic sources at ordinary and resonant weights, scalar Euler
inversions, exponent schedules and radial source controls with exact inverse formulas). The letters f, nu, a, A, E,
mu, mu_k, P, H, C, D, Z, rho, Q, B, t, u and g are local to 4.37.

4.38 Renormalized energy (beta > 2). Notation as in 4.36 and 4.37; Z_E = {M/N > 2 : M, N coprime positive integers, N
<= 4}, which contains Z_crit.
Let beta > 2 and let Psi, Theta, Omega, V and W be as in 4.36 (smooth on R^2, Psi odd and Theta even in x, V(0) = 0),
with (T) on R^2. For every rho > 0, with n the outward normal of {|X| < rho},
  int_{|X|<rho} Psi R_Omega dX = -(4 beta - 2) int_{|X|<rho} (|V|^2/2 + y Theta) dX + B_rho(Psi, Theta),
  B_rho(Psi, Theta) = oint_{|X|=rho} [Psi Omega W.n + beta (d_n Psi X.grad Psi - (X.n) |grad Psi|^2/2) + (2 beta - 1) Psi d_n Psi - Psi Theta n_x + y Theta W.n] ds.
Suppose in addition that R_Omega has compact support, that Omega in S^{-s}, V in S^{1-s} and Theta in S^m, and that
for some mu with 4 - s < mu < 4, Psi - P in S^{2-mu} and Theta - H in S^{1-s-mu} with P and H as in 4.37. Then
int_{|X|<rho} (|V|^2/2 + y Theta) dX is a finite sum of terms rho^alpha (log rho)^j with alpha > 0 or j > 0, plus a
constant, plus o(1); the constant is denoted f.p. int (|V|^2/2 + y Theta) dX.
(a) (4 beta - 2) f.p. int (|V|^2/2 + y Theta) dX = [rho^0 (log rho)^0] B_rho(P, H) - int Psi R_Omega dX.
(b) If beta is not in Z_E, and C and D denote the coefficients of x and of x/|X|^2 in P, then
  (4 beta - 2) f.p. int (|V|^2/2 + y Theta) dX = -2 pi beta C D - int Psi R_Omega dX.
(c) Every class A profile with beta > 2 satisfies these hypotheses (4.37(a), with mu in (4 - s, 4) not in E). If beta
is not in Z_E, then beta is not in Z_crit, so D = 0 by 4.37(a), and (b) with R_Omega = 0 gives f.p. int (|V|^2/2 + y
Theta) dX = 0: the renormalized energy of the profile, in the relative velocity and on disks centered at the material
center, vanishes.
(d) Positivity of Omega on {x > 0} does not determine the sign of this finite part, even when D = 0. For Theta = 0 and
Omega = x f(r) with f > 0 smooth (smooth in r^2 near 0), f = r^{-s-1} for r >= 1 and int_0^1 t^3 f(t) dt = 1/(3 - s)
(so that D = 0 in 4.36(b)),
  f.p. int |V|^2/2 dX = (pi/2) (int_0^1 I(r)^2 r^{-3} dr - 1/(2 (2 - s) (3 - s)^2)),   I(r) = int_0^r t^3 f(t) dt,
and both signs occur among such weights: at beta = 3, a weight that is small on [0, 0.99], joins the tail smoothly on
[0.99, 1] and carries a smooth bump that restores the moment gives a finite part above 1.50 for a bump supported in
(1/8, 1/4) and below -0.040 for a bump supported in (9/10, 19/20); the same construction works for every beta > 2.
These fields satisfy (T) and parity, have Theta = 0 and Psi_xy(0) = 0 instead of the center data of class A, and
violate (V) on every exterior annulus.
Proof outline. With T = W.grad Theta - (beta - 2) Theta, direct differentiation gives
  Psi R_Omega = -(4 beta - 2) (|V|^2/2 + y Theta) - y T + div[Psi Omega W + (2 beta - 1) Psi grad Psi + beta ((X.grad Psi) grad Psi - X |grad Psi|^2/2) - Psi Theta e_1 + y Theta W],
from V.grad Psi = 0, the two-dimensional Pohozaev identity div((X.grad Psi) grad Psi - X |grad Psi|^2/2) = (X.grad
Psi) Lap Psi, Psi Omega = |grad Psi|^2 - div(Psi grad Psi), and V_2 Theta = div(y Theta W) - (4 beta - 2) y Theta - y
T (from W.grad(y Theta) = y W.grad Theta + W_2 Theta and div W = 2 beta); with T = 0 and the divergence theorem this
is the identity above. For large rho the left side equals int Psi R_Omega dX. Substituting P and H in B_rho changes it
by O(rho^{4-s-mu}) = o(1) (the largest errors come from the Pohozaev, the (2 beta - 1) and the dilation terms; the
cubic and temperature-stream errors are O(rho^{4-2s-mu})), and the energy density differs from its truncation by an
integrable O(r^{2-s-mu}); B_rho(P, H) and the truncated energy integral are finite sums of terms rho^alpha (log
rho)^j, which gives the expansion and (a). A pair of stream terms of degrees e, e' enters B_rho with the power e + e',
the cubic flux Psi Omega V.n (which does not cancel in general) with e1 + e2 + e3 - 2, the terms with a temperature
degree g and a stream degree e with g + e + 1, and the dilation part beta y Theta X.n with g + 3; logarithms do not
alter these powers. For all combinations other than the harmonic pair of degrees (1, -1), a zero power requires K s =
d for integers K >= 1 and 1 <= d <= 4, so beta in Z_E (a harmonic term cannot be the Laplacian factor of the cubic
flux). For P_h = (C r + D r^{-1}) cos theta the term (2 beta - 1) oint P_h d_r P_h = (2 beta - 1) pi (C^2 rho^2 - D^2
rho^{-2}) has no constant part, and the Pohozaev term (beta/2) oint (rho^2 (d_r P_h)^2 - (d_theta P_h)^2) d theta
gives -2 pi beta C D; the other terms of B_rho vanish for harmonic P_h with H = 0. This gives (b). (c) The depth mu in
(4 - s, 4) is reached by the induction of 4.37 (steps of length less than s). (d) For Psi = x h(r) as in 4.36(b) (h' =
-I(r) r^{-3}) and phi = r h, the angular integral of |grad Psi|^2 is pi (phi'^2 + phi^2/r^2), and (phi'^2 + phi^2/r^2)
r = (r^2 h^2)' + I^2 r^{-3}; hence int_{|X|<rho} |V|^2/2 dX = (pi/2) (rho^2 h(rho)^2 + int_0^rho I(r)^2 r^{-3} dr).
For rho >= 1 and D = 0, rho h(rho) = -rho^{2-s}/((3 - s)(1 - s)) + C rho (C as in 4.36(b)), whose square has no
constant term, and I(r) = r^{3-s}/(3 - s), so int_1^rho I^2 r^{-3} dr contributes the constant -1/(2 (2 - s) (3 -
s)^2). For D = 0 the residual on r > 1 is x y (2 r^{-2s-2}/((3 - s)(1 - s)) - (s + 1) C r^{-s-3}), with two distinct
powers and a nonzero first coefficient.
Scope. A necessary condition for class A profiles outside Z_E, like 4.36(a), and not a sign contradiction; part (d)
concerns fields that violate (V), and no contradiction combining (c) with 4.36, 4.37 or the other identities of this
report was found in this investigation. The factor 4 beta - 2 agrees with the scaling exponent of the formal energy
(1/2) int |u|^2 + int z_2 theta of the momentum form of section 2 under spatial, velocity and temperature dilations of
degrees beta, beta - 1 and beta - 2. The identity concerns the relative fields (V = U - U(0) is unchanged by the
observer changes of (A5)) and disks centered at X = 0; comparison with the physical energy or with other observer or
cutoff conventions requires a separate calculation. For beta in Z_E the identity (a) still holds, but further terms
can contribute to the coefficient (every beta = M/N in Z_E admits, for example, the temperature degree 1 - M s - (4 -
N) = -3, whose dilation term has power 0); this does not assert that such terms occur with nonzero coefficients in a
solution, and the reduction (b) is not established there. The family of (d) does not satisfy the center data or (V),
so (d) shows only that positivity, parity, (T) and D = 0 do not fix the sign. Configurations with the center data, (T)
on R^2, the canonical inverse, Theta >= 0, vorticity of both signs and a nonzero compactly supported residual whose
affine moments vanish, with D = 0 for beta not in Z_crit, realize every real value of the finite part (6.3); they are
not profiles. Checks: a symbolic check in the analysis of the pointwise identity, of the harmonic pair and of the
formula of (d) for twelve weights; a separate referee audit (symbolic checks of the identity, the harmonic boundary
integrals and the radial formula; the two sign examples by exact bounds); the verification's independent proof and
checks. The letters P, H, B_rho, T, C, D, f, h, phi, I, e, e', e1, e2, e3, g, K, d, M, N and mu are local to 4.38.
4.39 Fixed-degree polynomial dependence on x, and global horizontal dilates for beta > 2 (restricted exclusions). In
this item W is a C^1 vector field on R^2 with div W = 2 beta and W(X) = beta X + o(|X|) uniformly as |X| -> infinity
(sup over |X| >= r of |W(X) - beta X|/|X| tends to 0 as r -> infinity), and Theta is a C^1 function on R^2 with
W.grad Theta = (beta - 2) Theta. Every smooth B2 profile with sublinear velocity satisfies these hypotheses with
W = beta X + U - U(0), and has W(0) = 0.
  (a) (beta > 0) If Theta(x, y) = sum_{j=0}^N f_j(y) x^j on R^2 for one integer N >= 0 and functions f_j of class C^1
      on R, then f_j = 0 for every j >= 1; if moreover Theta(0, .) = 0, then Theta = 0. Hence no smooth B2 profile
      with sublinear velocity has a temperature that is a polynomial in x of bounded degree with coefficients
      depending on y (for a smooth Theta the coefficients of such a representation are smooth: evaluate at N + 1
      distinct values of x and invert the Vandermonde matrix).
  (b) (beta > 2) Assume in addition W(0) = 0. There are no functions rho: R -> (0, infinity) and H: R -> R of class
      C^2 with H(0) = H'(0) = 0, H''(0) != 0 and Theta(x, y) = H(x/rho(y)) on R^2. For a smooth B2 profile every
      representation Theta(x, y) = H(x/rho(y)) on R^2 with rho > 0 has these properties: H(k) = Theta(k rho(0), 0) is
      smooth with H(0) = H'(0) = 0 and H''(0) = 2 a0 rho(0)^2 != 0, and rho = (H''(0)/Theta_xx(0, y))^{1/2} is smooth.
      Hence for beta > 2 no smooth B2 profile with sublinear velocity has a temperature of this form on R^2, for any
      rho > 0 and H.
Proof outline. (a) Suppose some f_j with j >= 1 is not identically zero; let N >= 1 be the largest such j, f = f_N, J
a component of {f != 0} and K = N beta - (beta - 2) = (N - 1) beta + 2 > 0. At fixed y, W_1/x -> beta and W_2/x -> 0
as x -> infinity. If f' vanished at a point of J, dividing (T) by x^N there would give K f = 0 in the limit (Theta_y
is of degree at most N - 1 in x there). So f' != 0 on J, and solving (T) for W_2 gives
W_2(x, y) -> g(y) = -K f(y)/f'(y) as x -> infinity, for each y in J. Integrating div W = 2 beta over
[t, 2t] x [y_1, y_2], with y_1 < y_2 in J, dividing by t and letting t -> infinity (W_1/x -> beta uniformly for y in
[y_1, y_2], and the averages of W_2(., y_i) over [t, 2t] tend to g(y_i)) gives g(y_2) - g(y_1) = beta (y_2 - y_1), so
g(y) = beta y + d on J. Then f'/f = -K/(beta y + d) and f = c_f |beta y + d|^{-K/beta} on J with c_f != 0. At a finite
endpoint e of J continuity gives f(e) = 0, while this expression tends to a nonzero finite limit or diverges; so
J = R, and then beta y + d vanishes in J, contrary to g != 0. Hence f_j = 0 for j >= 1, and Theta(0, .) = f_0 = 0
gives Theta = 0.
(b) Put lambda = beta - 2, k = x/rho(y), R(y) = int_0^y rho, V(k, y) = W_2(k rho(y), y) and Q = W_1 - k rho' V, both
evaluated at (k rho(y), y). Then W.grad Theta = H'(k) Q/rho and d_k Q + d_y(rho V) = 2 beta rho. Where H'(k) != 0, (T)
gives Q = rho q with q = lambda H/H', and integration in y gives rho V = (2 beta - q'(k)) R + C(k) and
W_1 = rho q + k rho' V, with C(k) = rho(0) W_2(k rho(0), 0) defined for every k. The center jet gives
q(k)/k -> lambda/2 and q'(k) -> lambda/2 as k -> 0 (H' != 0 for small k != 0), so q is C^1 across 0, and W(0) = 0 and
the limit k -> 0 give the axis identity b(y) = W_2(0, y) = d0 R(y)/rho(y), d0 = 1 + 3 beta/2, without division by
H'(0). Since b(y)/y -> beta at both ends, y R'/R -> d0/beta, and integrating the resulting bounds gives
c_1 |y|^{gamma - eps} <= rho(y) <= C_1 |y|^{gamma + eps} for large |y| and every small eps > 0, with
gamma = 1/2 + 1/beta in (1/2, 1); so rho -> infinity, rho = o(|y|) and |y| rho(y) -> infinity at both ends. Let (0, L)
be the component of {k > 0 : H'(k) != 0} adjacent to 0. For fixed k in (0, L), k rho(y) = o(y), so V(k, y)/y -> beta
as y -> infinity, while the identity for rho V gives V(k, y)/y -> (2 beta - q'(k)) beta/d0; hence
q' = alpha := (beta - 2)/2, q = alpha k, k H' = 2 H and H = H''(0) k^2/2 on (0, L), and L = infinity because
H'(L) = H''(0) L != 0 otherwise. At a minimum point y_m of rho, which exists since rho -> infinity at both ends,
rho'(y_m) = 0 and W_1(x, y_m) = alpha x for every x > 0, whereas W_1(x, y_m)/x -> beta > alpha as x -> infinity.
Scope. (a) and (b) use only (T), div W = 2 beta, the uniform sublinearity of W - beta X and, in (b), W(0) = 0; they
use neither (V), the inverse, parity, a sign of Theta, nor bounds on derivatives at infinity, and (a) uses no center
jet. The isotropic sublinearity is essential: Theta = x^2 and the linear field W = (alpha x, d0 y) satisfy (T),
div W = 2 beta and W(0) = 0. The whole y-axis is essential in (a): on {y > 0}, W = beta X and Theta = x^N y^{-K/beta}
satisfy (T) and div W = 2 beta. Temperatures that are only polynomially bounded, polynomial representations whose
degree in x is not bounded in y, and for beta > 2 representations H(x/rho(y)) on a neighbourhood of the axis only, are
not covered by 4.39 (see 4.40 and 4.43).
(b) does not apply at beta = 2 (there gamma = 1 and lambda = 0); at beta = 2, in the full smooth B2 setting of
4.7(iii), the form H(x/rho(y)) on a neighbourhood of the whole axis is excluded under (V) by 4.7(xxiv). The existence
of a profile is not decided. Checks: the verification's own proofs with exact symbolic controls (49 for (a), 34 for
(b)); a separate referee audit of both proofs (VALID as written; 19 symbolic checks; the two examples above). The
letters N, f, f_j, J, K, g, d, c_f, t, y_1, y_2, e, lambda, k, rho, H, R, V, Q, q, C, d0, gamma, eps, c_1, C_1, L,
alpha and y_m are local to 4.39.
4.40 Horizontal dilates near the whole axis for beta > 2 (restricted exclusion, class A). Let beta > 2, s = 1/beta and
m = 1 - 2s.
  (a) Let Theta, Omega and W be smooth on R^2 with div W = 2 beta, Omega = d_y W_1 - d_x W_2, W(0) = 0,
      W(X) = beta X + o(|X|) uniformly as |X| -> infinity, (T) and (V); Theta and W_2 even and Omega and W_1 odd in x;
      Theta(0, .) = 0 and Theta = a0 x^2 + O(|X|^3) with a0 != 0; and, for |y| large, with constants C_j and D_j,
        |d_x^j Theta(0, y)| <= C_j |y|^{m-j} (j >= 0),   |d_x^j W_2(0, y)| <= D_j |y|^{1-s-j} (j >= 1).   (S)
      Then there are no open neighbourhood N of the axis {x = 0}, function rho: R -> (0, infinity) and function H
      defined at x/rho(y) for every (x, y) in N such that Theta(x, y) = H(x/rho(y)) for every (x, y) in N. No
      regularity of rho or H is assumed.
  (b) Every class A profile with beta > 2 satisfies the hypotheses of (a) with W = beta X + U - U(0): (S) is the
      restriction to the axis of the symbol bounds |D^alpha Theta| <= C r^{m-|alpha|} and
      |D^alpha V| <= C r^{1-s-|alpha|} (r >= 1, V = U - U(0)) of 4.37 step (5), since d_x^j (beta y) = 0 for j >= 1.
      Hence no class A profile with beta > 2 has a temperature of the form H(x/rho(y)) on a neighbourhood of the whole
      axis, for any rho > 0 and H.
Proof outline. (0) By the reflection of 4.8, which preserves the hypotheses and (S) and maps N to its mirror image,
a0 > 0. The slice y = 0 gives H(k) = Theta(k rho_0, 0) near 0, rho_0 = rho(0), so H is smooth there with
H''(0) = 2 a0 rho_0^2, and Theta_xx(0, y) = H''(0)/rho(y)^2 makes rho smooth. Replacing H by H(k/rho_0) and rho by
rho/rho_0, rho_0 = 1 and A := H''(0) = 2 a0 > 0.
(1) Put k = x/rho(y), R(y) = int_0^y rho, alpha = (beta - 2)/2, d0 = 1 + 3 beta/2 = 2 beta - alpha, and near k = 0,
q = (beta - 2) H/H' and d = 2 beta - q'; q is smooth and odd with q'(0) = alpha, and d(0) = d0. For each Y > 0 some
strip {|k| <= eps_Y, |y| <= Y} lies in N, with H' != 0 for 0 < |k| <= eps_Y; there, with V(k, y) = W_2(k rho(y), y),
the computation of 4.39(b) gives rho V = d(k) R + C(k) and W_1(k rho, y) = rho q + k rho' V, with the same smooth even
C(k) = W_2(k, 0) for every Y, C(0) = 0. No uniform width of N is needed.
(2) b(y) = W_2(0, y) = d0 R/rho vanishes only at 0, and b(y)/y -> beta at both ends; as in 4.39(b),
c_1 |y|^{gamma - eps} <= rho(y) <= C_1 |y|^{gamma + eps} for large |y| and every small eps > 0, gamma = 1/2 + 1/beta
in (1/2, 1). So rho -> infinity at both ends.
(3) d_x^j Theta(0, y) = H^(j)(0)/rho(y)^j. If H^(j)(0) != 0 for some j > 2, the upper bound for rho and (S) give
c |y|^{-j(gamma + eps)} <= C_j |y|^{m-j}, impossible for small eps since j(1 - gamma) - m = (j/2 - 1) m > 0. So
H - A k^2/2, q - alpha k and d - d0 are flat at k = 0 (no identity on an interval is claimed).
(4) Hence d_x^j W_2(0, y) = C^(j)(0)/rho(y)^{j+1} for j >= 1, and (S) gives C^(j)(0) = 0 for j > 3 beta/(beta - 2),
since then j(1/2 - 1/beta) - 3/2 > 0. Let P be the Taylor polynomial of C at 0 of degree floor(3 beta/(beta - 2));
C - P is flat at 0, and P(0) = 0.
(5) Write C(k) = c_2 k^2 + O(k^4). On the axis, by div W = 2 beta and the parities,
eta(y) := Omega_x(0, y) = -b'' - 2 c_2/rho^3, and eta > 0 on R by 4.13(i), since b vanishes only at 0 (directly:
r = rho eta solves b r' + (beta/2) r = A/rho, so r(y_0) = A int_{-infinity}^0 e^{beta t/2}/rho(y(t)) dt > 0 along the
backward flow of y' = b(y) from y_0). If c_2 >= 0, then b'' < 0 on R, so b' > b'(0) = d0 on {y < 0} and
b(y)/y > d0 > beta there, contrary to b(y)/y -> beta. So c_2 < 0, and P has a highest nonzero coefficient p_n, with
n >= 2.
(6) Comparison fields on R^2, in the coordinates (k, y): F = d0 R + P(k), W~_2 = F/rho,
W~_1 = rho alpha k + k rho' F/rho, Theta~ = A k^2/2. They satisfy div W~ = 2 beta and (T) (W~ is not claimed
sublinear). By (1), (3) and (4), W - W~ and Theta - Theta~, with all their derivatives in y, are flat in x at x = 0
for each y, so the residual E~ = W~.grad Omega~ + Omega~ - Theta~_x of Omega~ = d_y W~_1 - d_x W~_2 has zero x-jet on
the whole axis. With B = rho''/rho - 2 rho'^2/rho^2, Omega~ = d0 k rho' + k F B - (1 + k^2 rho'^2) P'(k)/rho^2, and
rho E~ = rho alpha k d_k Omega~ + F d_y Omega~ + rho Omega~ - A k (d_y at fixed k) is a polynomial in k with
coefficients smooth in y. Hence E~ = 0 identically, although the flat remainders of the true fields need not vanish.
(7) With p = rho'/rho, the coefficient of k^{n+1} in Omega~ is p_n (B - n p^2), and the only term of degree 2n + 1 in
rho E~ comes from P d_y Omega~, with coefficient p_n^2 (B - n p^2)'. So B - n p^2 is constant; since B = p' - p^2,
p' - (n + 1) p^2 = K for a constant K, and v = rho^{-(n+1)} > 0 solves v'' + (n + 1) K v = 0. By (2), v -> 0 at both
ends, which no nonzero solution does (it is affine for K = 0, trigonometric for K > 0, and a combination of e^{mu y}
and e^{-mu y}, mu > 0, for K < 0).
Scope. 4.40 uses (T), (V), the parities, the center jet, the uniform sublinearity and (S); for class A, (S) comes from
the symbol bounds of 4.37 step (5). It assumes no analyticity, no uniform width of N as |y| -> infinity and no
regularity of rho or H; the Taylor coefficients of H and C at k = 0 enter only through exact identities, and P is not
claimed to equal C near 0. A representation on a neighbourhood of a bounded part of the axis only is not covered ((2)
to (4) use |y| -> infinity), nor are temperatures without such a representation. For class A profiles with beta > 2 it
contains the profile case of 4.39(b), with no regularity assumed for rho and H; 4.39(b) itself holds outside class A.
At beta = 2 the threshold of (4) is lost (1/2 - 1/beta = 0); that case, under (V) and without (S), is 4.7(xxiv). 4.41
strengthens (b) and 4.7(xxiv) to finitely many axis derivatives of Theta, and 4.43 proves (a) without (S). The
existence of a profile is not decided. Checks: the verification's own proof with 53 exact algebra controls and 23
controls of the rescaling and of the dependencies; symbolic checks in the analysis of (6), (7), the comparison fields,
the top coefficient and the axis formula for eta; a separate referee audit (VALID, with 36 symbolic checks). The
letters s, m, C_j, D_j, c, N, rho, rho_0, H, A, k, R, alpha, d0, q, d, eps_Y, Y, V, C, b, gamma, eps, c_1, C_1, P,
c_2, eta, r, y_0, p_n, n, F, W~, Theta~, Omega~, E~, B, p, K, v and mu are local to 4.40.
4.41 Finitely many axis derivatives of the temperature (restricted exclusions). Let W, Theta and Omega be smooth on
R^2 with div W = 2 beta, Omega = d_y W_1 - d_x W_2, W(0) = 0, W(X) = beta X + o(|X|) uniformly as |X| -> infinity, (T)
and (V); Theta and W_2 even and Omega and W_1 odd in x; Theta(0, .) = 0 and Theta = a0 x^2 + O(|X|^3) with a0 != 0.
Assume that Theta_xx(0, y) != 0 for every real y, and put I_j(y) = d_x^{2j} Theta(0, y)/Theta_xx(0, y)^j for j >= 2.
  (a) Let beta > 2, s = 1/beta and m = 1 - 2s, let N be the greatest even integer <= 3 beta/(beta - 2), and M = 2N + 4
      ((N, M) = (8, 20), (6, 16) and (4, 12) for beta = 3, 4 and 5, and (2, 8) for beta > 8). If, for every even j
      with N + 2 <= j <= 2N + 2, |d_x^j W_2(0, y)| <= D_j |y|^{1-s-j} for |y| large, then d_x^j Theta(0, .) is not
      identically zero for at least one even j with 4 <= j <= M. For a class A profile with beta > 2
      (W = beta X + U - U(0)), at least one of I_2, ..., I_{N+2} is nonconstant.
  (b) Let beta = 2. Then I_2 and I_3 are not both constant.
In either case a temperature H(x/rho(y)) on a neighbourhood of the whole axis, with rho > 0, satisfies the assumption
on Theta_xx and makes every I_j constant: by step (0) of 4.40, Theta_xx(0, y) = H''(0)/rho(y)^2 != 0 and
I_j = H^(2j)(0)/H''(0)^j. So (a) contains 4.40(b), and (b) contains 4.7(xxiv).
Proof outline. (0) The reflection of 4.8 preserves the hypotheses, including the bounds on W_2 in (a), and the
constancy of each I_j, and it reverses the sign of a0; so let a0 > 0. Put A = 2 a0, rho = (A/Theta_xx(0, y))^{1/2}
(smooth and positive, rho(0) = 1), k = x/rho(y), R(y) = int_0^y rho, S(k, y) = Theta(k rho(y), y),
V(k, y) = W_2(k rho(y), y), Q = W_1(k rho(y), y) - k rho' V and b(y) = W_2(0, y). Below, O(k^r) means k^r times a
function that is smooth on a strip {|k| <= eps_Y, |y| <= Y}, for every Y > 0, with eps_Y so small that S_k/k != 0
there. The second x-derivative of (T) on the axis gives (rho b)' = d0 rho with
d0 = 2 beta - (beta - 2)/2 = 1 + 3 beta/2, so b = d0 R/rho, and b(y)/y -> beta at both ends.
(1) Case (a). The bounds on rho of 4.40 (2) hold. By parity and the vanishing of d_x^j Theta(0, .) for the even j with
4 <= j <= M, S = A k^2/2 + O(k^{M+2}). (T), in the form (Q/rho) S_k + V S_y = (beta - 2) S, gives
Q = rho alpha k + O(k^{M+1}) with alpha = (beta - 2)/2, and div W = 2 beta, in the form
d_k Q + d_y(rho V) = 2 beta rho, gives rho V = d0 R + C(k) + O(k^M) with the same C(k) = W_2(k, 0) for every Y. So
d_x^j W_2(0, y) = C^(j)(0)/rho(y)^{j+1} for 1 <= j < M, and, as in 4.40 (4), the bounds on W_2 give C^(j)(0) = 0 for
the even j with N + 2 <= j <= 2N + 2, since then j(1/2 - 1/beta) - 3/2 > 0; for odd j, C^(j)(0) = 0 by parity. Hence
C - P = O(k^M), with P the Taylor polynomial of C at 0 of degree N, and 4.40 (5) gives c_2 < 0 and the degree n of P,
2 <= n <= N. For the comparison fields of 4.40 (6), W_2 - W~_2 = O(k^M), W_1 - W~_1 = O(k^{M+1}) and
Theta - Theta~ = O(k^{M+2}); since d_x lowers the order by one and d_y at fixed x preserves it,
Omega - Omega~ = O(k^{M-1}) and rho E~ = O(k^{M-1}). As rho E~ is a polynomial in k of degree at most 2N + 1 < M - 1,
E~ = 0, and 4.40 (7) gives the contradiction. For class A, the symbol bounds of 4.37 step (5) give the bounds on W_2
and |d_x^l Theta(0, y)| <= C_l |y|^{m-l}. If I_2, ..., I_{N+2} were constant, then d_x^l Theta(0, y) = h_l/rho(y)^l
with constants h_l (l = 4, 6, ..., M), and h_l != 0 would contradict this bound as in 4.40 (3), since (l/2 - 1) m > 0;
so every d_x^l Theta(0, .) with even 4 <= l <= M would vanish.
(2) Case (b). Here d0 = 4, and S_kk(0, y) = A, d_k^4 S(0, y) = A^2 I_2 and d_k^6 S(0, y) = A^3 I_3 are constant, so by
parity S = A k^2/2 + B k^4/4 + D k^6/6 + O(k^8) with constants B and D. Then S_y = O(k^8), (T) gives Q = O(k^7), and
div W = 4 gives rho V = 4 R + c(k) + O(k^6) with c(k) = W_2(k, 0) = c_2 k^2 + c_4 k^4 + O(k^6). So
W_2 = (4 R + c(x/rho))/rho + O(k^6) and W_1 = (x rho'/rho) W_2 + O(k^7), and the expansion of
rho (W.grad Omega + Omega) in step (4) of 4.7(xxiv) holds up to O(k^5), as does
rho Theta_x = S_k = A k + B k^3 + O(k^5). The coefficients of k and k^3 give E_1 and E_3 exactly (D does not enter),
and steps (2) to (4) of 4.7(xxiv) apply without change: c_2 < 0, r_1 = 0 by the resultant, rho = 1 near 0 and then on
R, so b = 4 y, contrary to b(y) = 2 y + o(|y|).
Scope. 4.41 assumes no representation of Theta, no analyticity and no uniform width of the strips; it uses (T), (V),
the parities, the center jet, Theta_xx(0, .) != 0 on the whole axis and the sublinearity (only through
b(y)/y -> beta), and (a) uses in addition the finitely many bounds on W_2, which for class A come from 4.37 step (5).
The orders M and N + 2 in (a) and the two ratios in (b) suffice for these arguments and are not claimed optimal. The
sublinearity is essential in (b): W = (0, 4 y + c(x)), Theta = -c(x) and Omega = -c'(x), with c an even polynomial,
c(0) = 0 and c''(0) < 0, satisfy all the other hypotheses, with I_2 and I_3 constant. Profiles for which
Theta_xx(0, .) has a zero (see 4.42 and 4.43 for these; for beta > 2, 4.43 needs only I_2 and I_3 and no additional
derivative bounds at infinity), and profiles whose ratios I_j vary, are not covered; the existence of a profile is not
decided. Checks: the verification's own proofs with exact controls (81 for (a), 32 for (b)); separate referee audits
(for (a), VALID, 64 exact checks, including the deduction of 4.40(b); for (b), VALID, 37 exact checks,
including the deduction of 4.7(xxiv)). The letters s, m, N, M, D_j, I_j, A, rho, k, R, S, V, Q, b, eps_Y, Y, d0,
alpha, C, P, c_2, n, W~, Theta~, Omega~, E~, C_l, h_l, l, B, D, c and c_4 are local to 4.41; E_1 and E_3 are as in
4.7(xxiv).
4.42 The axis component containing the center (restricted exclusions). Assume the hypotheses of the first paragraph of
4.41, except that Theta_xx(0, .) may vanish. Let J be the connected component of {y : Theta_xx(0, y) != 0} that
contains 0, and put I_j(y) = d_x^{2j} Theta(0, y)/Theta_xx(0, y)^j for y in J and j >= 2. No condition on
Theta_xx(0, .) outside J is imposed.
  (a) J = (y_-, y_+), where y_+ is the least positive zero of W_2(0, .) and y_- the greatest negative one, with
      y_+ = infinity (y_- = -infinity) if there is none, as in 4.13(i). So J is unbounded if and only if W_2(0, .) has
      no zero on at least one of the two open half-axes.
  (b) Let beta = 2. Then I_2 and I_3 are not both constant on J.
  (c) Let beta > 2, let s, m, N and M be as in 4.41(a), and let J be unbounded. If the bounds on W_2 of 4.41(a) hold
      for y in J with |y| large at one infinite end of J, then d_x^j Theta(0, .) is not identically zero on J for at
      least one even j with 4 <= j <= M. If moreover |d_x^l Theta(0, y)| <= C_l |y|^{m-l} at that end for the even l
      with 4 <= l <= M, then at least one of I_2, ..., I_{N+2} is nonconstant on J. For a class A profile with
      beta > 2 both families of bounds hold (4.37 step (5)); so if W_2(0, .) has no zero on one of the open half-axes,
      at least one of I_2, ..., I_{N+2} is nonconstant on J.
With J = R, (b) and (c) contain 4.41.
Proof outline. (0) The reflection of 4.8 maps J to -J and I_j(y) to (-1)^{j+1} I_j(-y), so it preserves the constancy
of each I_j and the unboundedness of J; it maps the bounds in (c) at one end to the same bounds at the mirrored end,
and it reverses the sign of a0; so let a0 > 0. Define A, rho, k, R, S, V, Q, b and d0 as in step (0) of 4.41, now for
y in J (rho is smooth and positive on J, rho(0) = 1), and let O(k^r) refer to strips {|k| <= eps_K, y in K} over
compact intervals K of J that contain 0. With T = Theta_xx(0, .), the second x-derivative of (T) on the axis gives
b T' + (3 beta + 2 - 2 b') T = 0 on all of R, and on J again (rho b)' = d0 rho; so b = d0 R/rho has the sign of y on
J.
(1) Proof of (a). At a finite end y_* of J, T(y_*) = 0 by continuity and the maximality of J. If b(y_*) != 0, the
equation for T is a regular homogeneous linear first-order equation near y_*, and T(y_*) = 0 forces T = 0 near y_*,
which is false inside J. So b(y_*) = 0, while b != 0 on J except at 0; and rho(y) -> infinity as y -> y_* in J.
(2) c_2 < 0 on every J. For (b), suppose I_2 and I_3 constant on J. For the first statement of (c), suppose
d_x^j Theta(0, .) vanishes identically on J for every even j with 4 <= j <= M. The derivations of 4.41 (1) and (2) are
local and hold on J: rho V = d0 R + C(k) + O(k^M) in case (c) and rho V = 4 R + c(k) + O(k^6) in case (b), with one
germ C(k) = c(k) = W_2(k, 0) = c_2 k^2 + O(k^4) for every K. In both cases d_x^2 W_2(0, y) = 2 c_2/rho^3 on J, and, as
in 4.40 (5), eta = Omega_x(0, .) satisfies eta = -b'' - 2 c_2/rho^3, and r = rho eta solves b r' + (beta/2) r = A/rho
on J. The backward orbit of y' = b(y) from a point of J stays between that point and 0, so r > 0 and eta > 0 on J. If
c_2 >= 0, then b'' < 0 on J. If y_- = -infinity, this contradicts b(y)/y -> beta as in 4.40 (5). If y_- is finite, b
is continuous on [y_-, 0], concave on (y_-, 0) and zero at both ends by (1), so b >= 0 on (y_-, 0), contrary to b < 0
there. Hence c_2 < 0.
(3) Proof of (b). By 4.41 (2), E_1 and E_3 hold on J. With c_2 < 0 from (2), the elimination and the uniqueness
argument in step (4) of 4.7(xxiv) are local at y = 0 and give rho = 1 near 0. On J \ {0}, R != 0 and rho > 0, so E_1
is a regular fourth-order equation for R there, and rho = 1 continues along each half of J. Then T = A on J: a finite
end y_* contradicts T(y_*) = 0, and J = R gives b = 4 y, contrary to b(y) = 2 y + o(|y|).
(4) Proof of (c). At the infinite end, b(y)/y -> beta and the bounds on rho of 4.40 (2) hold, with the same proof.
With them and the bounds on W_2 at that end, 4.41 (1) applies on J: C - P = O(k^M) with P the Taylor polynomial of C
of degree N, c_2 < 0 by (2), the residual polynomial vanishes on J, and, with p = rho'/rho and n the degree of P,
p' - (n + 1) p^2 = K_0 on J for a constant K_0; so v = rho^{-(n+1)} solves v'' + (n + 1) K_0 v = 0 on J. If J = R,
step (7) of 4.40 gives the contradiction. If J has a finite end y_*, then v = (T/A)^{(n+1)/2} and
v' = ((n + 1)/2)(T/A)^{(n-1)/2} T'/A tend to 0 at y_* (n >= 2), so the solution of this linear equation on R that
equals v on J has zero value and derivative at y_* and vanishes identically, contrary to v > 0 on J. The ratio
statement follows as in 4.41 (1), with the bounds on rho and on Theta at the infinite end.
Scope. 4.42 uses what 4.41 uses, with the condition on Theta_xx(0, .) restricted to J; the sublinearity enters only
through b(y)/y -> beta at the infinite ends of J ((2) when y_- = -infinity, (3) when J = R, and (4)), and for class A
also through 4.37 step (5). In (b) no condition on the zeros of Theta_xx(0, .) or of W_2(0, .) is needed. For
beta > 2, (c) does not cover a bounded J (W_2(0, .) with zeros on both open half-axes): there the bounds at infinity
cannot be used and C is not reduced to a polynomial; the ratio statement for I_2 and I_3 holds on every J by 4.43, and
the coefficients of (T) and (V) of every order on the axis do not exclude a bounded J (4.49), and neither do (T) on
R^2 and the coefficients of (V) of every order on the axis (4.50). Profiles whose ratios I_j vary on J are not
covered; the existence of a profile is not decided. Checks: the verification's own proof with 52 exact controls (it
reproduces the local elimination of 4.7(xxiv)); a separate referee audit (VALID, 56 exact checks). The letters J, y_-,
y_+, I_j, T, y_*, eps_K, K, eta, r, p, n, K_0 and v are local to 4.42; s, m, N, M, C_l, l, A, rho, k, R, S, V, Q, b,
d0, C, c, c_2, P, E_1 and E_3 are as in 4.41 and 4.7(xxiv).
4.43 Two constant ratios on the axis component for beta > 2 (restricted exclusion). Assume the hypotheses of the first
paragraph of 4.42, with beta > 2, and let J and I_j be as there. Then I_2 and I_3 are not both constant on J. No
additional derivative bounds at infinity, no class A and no condition on the ends of J are assumed. With 4.42(b): for
every beta >= 2, I_2 and I_3 are not both constant on J. For beta > 2 this contains, with fewer hypotheses:
  (i) the first statements of 4.41(a) and 4.42(c), with j = 4, 6 and without the bounds on W_2: d_x^4 Theta(0, .) and
      d_x^6 Theta(0, .) do not both vanish identically on J (that would make I_2 = I_3 = 0);
  (ii) the ratio statements of 4.41(a) and 4.42(c), with I_2, I_3 in place of I_2, ..., I_{N+2}, for every J and
      without their derivative bounds at infinity or class A;
  (iii) 4.40(a) without (S): a temperature H(x/rho(y)) on a neighbourhood of the whole axis, with rho > 0, makes J = R
      and every I_j constant (4.41).
Proof outline. (0) Two symmetries. The reflection of 4.8 acts as in 4.42 (0). For real lambda != 0 the dilation
W^l(X) = W(lambda X)/lambda, Theta^l(X) = Theta(lambda X)/lambda, Omega^l(X) = Omega(lambda X) satisfies all the
hypotheses with lambda a0 in place of a0 (also for lambda < 0, by the parities), J^l = J/lambda and
I_j^l(y) = lambda^{j-1} I_j(lambda y); so constancy of I_2 and I_3 is preserved. Steps (1) to (4) do not use the sign
of a0: put A = 2 a0, T = Theta_xx(0, .) (which has the sign of A on J) and rho = (A/T)^{1/2} on J, and let k, R, S, V,
Q, b and d0 be as in 4.42 (0); then b = d0 R/rho on J.
(1) Jets. Suppose I_2 and I_3 constant on J. Since d_k^2 S(0, y) = A, d_k^4 S(0, y) = A^2 I_2 and
d_k^6 S(0, y) = A^3 I_3, parity gives S = S~(k) + O(k^8), S~ = A k^2/2 + B k^4/4 + D k^6/6, with the constants
B = A^2 I_2/6 and D = A^3 I_3/120.
(2) Two exact identities. As in 4.41 (2), S_y = O(k^8), (T) gives Q = rho q(k) + O(k^7) with q = (beta - 2) S~/S~_k =
alpha k - alpha B k^3/(2 A) + O(k^5), alpha = (beta - 2)/2, and div W = 2 beta gives rho V = d(k) R + c(k) + O(k^6)
with d = 2 beta - q' = d0 + 3 alpha B k^2/(2 A) + O(k^4) and c(k) = W_2(k, 0) = c_2 k^2 + c_4 k^4 + O(k^6). The
comparison fields built, as in 4.40 (6), from the Taylor polynomials of q of degree 5 and of c of degree 4 and from S~
differ from W_2, W_1 and Theta by O(k^6), O(k^7) and O(k^8); so their residual in (V), times rho, is O(k^5), and its
coefficients E_1 of k and E_3 of k^3 vanish on J. Explicitly, 4 A rho^3 E_1 = A [(3 beta + 2)^2 R^2
(rho^2 rho''' - 5 rho rho' rho'' + 4 rho'^3) + (3 beta + 2)(7 beta + 4) rho^3 R rho'' - 4 (2 beta + 1)(3 beta + 2)
rho^2 R rho'^2 + 8 (3 beta + 2) c_2 R rho' + beta (3 beta + 2) rho^4 rho' - 4 rho^2 (A rho + beta c_2)] +
6 (beta - 2) B [(3 beta + 2) R^2 rho' - (2 beta + 1) rho^2 R]; at beta = 2, E_1 is -1 times the E_1 of 4.7(xxiv). E_3
is longer, linear in c_4 and in D.
(3) Taylor coefficients at 0. Let r_n = rho^{(n)}(0)/n!, so r_0 = 1 (no convergence of the Taylor series is used). The
Taylor coefficient at 0 of y^n in 4 A rho^3 E_1 is A lambda_{n+1} r_{n+1} plus a polynomial in beta, A, B, c_2,
r_1, ..., r_n, where lambda_m = (3 beta + 2) m^2 ((3 beta + 2) m - 2 beta - 2) > 0 for m >= 1; for n = 0 it gives
A = beta ((3 beta + 2) r_1 - 4 c_2)/4. In 12 A^2 rho^3 E_3, the coefficient of y^0 is linear in c_4 with coefficient
-24 (3 beta - 4) A^2, and the coefficient of y, after c_4 is eliminated, is linear in D with coefficient -80
(beta - 2)(3 beta - 1) A; both coefficients are nonzero, since beta > 2 and A != 0.
(4) Elimination. Under the dilations r_n, A, c_2, B, c_4 and D are multiplied by lambda^n, lambda, lambda, lambda^3,
lambda^3 and lambda^5. So one may take r_1 = 1 (chart 1, with t = c_2), or r_1 = 0 and then, by (3), c_2 != 0 and
c_2 = -1, A = beta (chart 0). Solving the coefficients of y^1, ..., y^8 of E_1 for r_2, ..., r_9 and those of
y^0 and y of E_3 for c_4 and D turns the coefficients of y^2, ..., y^6 of E_3 into rational functions of beta, B and
(chart 1) t, whose denominators are products of A and of linear factors positive for beta > 2. In chart 0 their
numerators are, up to such factors, B F_j(B, beta), where F_2 has degree one in B with coprime coefficients, and the
resultants in B of F_2 with F_3 and with F_4 have greatest common divisor
18 beta^2 (3 beta - 4)(3 beta + 2)^2 (5 beta + 3)(13 beta + 8), which has no root > 2; so B = 0. In chart 1 let
F_j(B, t, beta), j = 2, ..., 6, be the numerators of these coefficients after removal of factors nonzero for beta > 2
and A = beta (3 beta + 2 - 4 t)/4 != 0, as in the accompanying computation; the resultants in B of F_2 with F_3, F_4
and F_5 are, up to such factors, t (3 beta + 2 - 4 t)^{m_j} G_j(t, beta), and the
resultants in t of G_3 with G_4 and with G_5, integer polynomials in beta of degrees 744 and 945, have greatest common
divisor c_0 beta (216 beta^3 + 677 beta^2 + 420 beta + 64)(5 beta + 3)^4 (3 beta - 1)^6 (13 beta + 8)^9
(7 beta + 4)^12 (3 beta - 4)^17 (beta - 2)^21 (2 beta + 1)^42 (3 beta + 2)^104, with an integer c_0 != 0, which has no
root > 2; so t = 0. At t = 0, F_j = kappa_j B h_j(B, beta) with kappa_j nonzero for beta > 2, h_2 has degree one in B
with coprime coefficients, and the resultants in B of h_2 with h_3 and with h_4 have greatest common divisor
256 beta^2 (beta - 2)^2 (2 beta + 1)^2 (3 beta - 1)(3 beta + 2)^4 (7 beta + 4), which has no root > 2; so B = 0. The
resultants are formed with the formal degrees, so a common zero makes them vanish also where leading coefficients
vanish. The two large resultants were computed exactly, by evaluation and interpolation modulo primes of 62 bits and
Chinese remaindering up to a rigorous bound for their coefficients, and checked against exact determinants at four
values of beta.
(5) Chart 1 is impossible. There B = 0 and c_2 = 0, and both are preserved by the reflection, so let a0 > 0. Since
B = 0, d = d0 + O(k^4), so d_x^2 W_2(0, y) = 2 c_2/rho^3 on J, and 4.42 (2) gives c_2 < 0, a contradiction.
(6) Chart 0 is impossible. There B = 0, r_1 = 0 and A + beta c_2 = 0, so rho = 1 solves E_1. If rho - 1 = O(y^m) with
m >= 2, the coefficient of y^{m-1} in 4 A rho^3 E_1 is A lambda_m r_m, so r_m = 0: rho - 1 is flat at 0. With
Z = (rho, y rho', y^2 rho'', R/y), E_1 and R' = rho read y Z' = F(y, Z) with F smooth near Z* = (1, 0, 0, 1) and
F(y, Z*) = 0, and, as in step (4) of 4.7(xxiv), rho = 1 near 0. On J \ {0} the coefficient (3 beta + 2)^2 R^2/(4 rho)
of rho''' in E_1 is nonzero, so rho = 1 on J. Then T = A on J, so J has no finite end (T(y_*) = 0 there), and on
J = R, b = d0 y, contrary to b(y)/y -> beta, since d0 - beta = 1 + beta/2 > 0.
Scope. 4.43 uses (T), (V), the parities, the center jet and, only through b(y)/y -> beta at an infinite end of J ((5)
when y_- = -infinity, (6) when J = R), the sublinearity; it assumes no additional derivative bounds at infinity, no
class A, no representation of Theta and no analyticity. The elimination in (4) is exact computer algebra over Q(beta)
and Q(beta, t), with the large resultants in exact integer arithmetic; the independent certificate script is among the accompanying
artifacts (section 8). Only E_1 and E_3 are used. The sublinearity is essential: W = (alpha x, d0 y - x^2), Theta = beta x^2/2 and
Omega = 2 x satisfy all the other hypotheses, with J = R and I_2 = I_3 = 0. Profiles whose ratios I_2, I_3 vary on J
are not covered (for beta > 2, 4.44 excludes a nonzero finite limit of I_2 at an infinite end of J); the existence of
a profile is not decided. Checks: exact checks in the analysis of the displayed E_1, of lambda_m, of the relation
between A, r_1 and c_2, of the flatness step, of F(y, Z*) = 0 and of the example; a separate referee audit (VALID,
with its own derivation of E_1 and E_3, of both charts and of the two large resultants); the verification's own proof
(CONFIRMED, with its own derivation of E_1 and E_3 in physical coordinates, 101 exact controls of the identities and
both charts, and an exact certificate of 563 checks for the elimination and the two large resultants). The letters
lambda, S~, A, T, rho, B, D, q, alpha, d, c, c_2, c_4, E_1, E_3, r_n, lambda_m, t, F_j, G_j, m_j, c_0, kappa_j, h_j,
Z, Z*, F, y_* and the superscript l are local to 4.43; k, R, S, V, Q, b and d0 are as in 4.42.
4.44 One ratio at an infinite end of the axis component for beta > 2 (restricted exclusion). Assume the hypotheses of
the first paragraph of 4.42, with beta > 2, and let J and I_2 be as there. If J has an infinite end, then I_2(y) does
not tend to a nonzero finite limit as y tends to that end. No additional derivative bounds at infinity, no class A, no
condition on I_3 or on the higher ratios and no condition at the other end of J are assumed. In particular:
  (i) if I_2 is constant on a neighbourhood of an infinite end of J, the constant is 0; if J is unbounded and I_2 is
      constant on J, then d_x^4 Theta(0, .) = 0 on J and I_3 is not constant on J (4.43);
  (ii) if K = (y_1, infinity) or K = (-infinity, -y_1) is contained in J, there are no H, smooth near 0, and
      sigma: K -> (0, infinity) with H''''(0) != 0 and Theta(x, y) = H(x/sigma(y)) on a neighbourhood of {0} x K:
      there I_2 = H''''(0)/H''(0)^2 would be a nonzero constant.
Proof outline. (0) The reflection of 4.8 maps J to -J and I_2(y) to -I_2(-y) (and reverses the sign of a0); so let the
infinite end be +infinity. The sign of a0 is not fixed: put A = 2 a0, T = Theta_xx(0, .) (which has the sign of A on
J) and rho = (A/T)^{1/2} on J, and let R, b and d0 be as in 4.42 (0); then b = d0 R/rho on J. Put B = A^2 I_2/6, so
that d_x^4 Theta(0, .) = 6 B/rho^4 on J.
(1) An exact identity. On J write W_1 = x w_1 + x^3 w_3 + O(x^5), W_2 = b + x^2 v_2 + O(x^4) and
Theta = x^2 T/2 + x^4 B/(4 rho^4) + O(x^6). The coefficients of x^0 and x^2 of div W = 2 beta give w_1 = 2 beta - b'
and 3 w_3 + v_2' = 0, and with them the coefficient of x^4 of (T) gives
(rho^3 v_2)' = (3/(4 A))(2 alpha rho B + d0 R B'), alpha = (beta - 2)/2. Since v_2(0) = c_2, where
W_2(x, 0) = c_2 x^2 + O(x^4) as in 4.42 (2), integration by parts gives on J
rho^3 v_2 = c_2 + (A/8) [d0 R I_2 - ((beta + 6)/2) int_0^y rho I_2]. For constant I_2 this is the k^2 coefficient
c_2 + 3 alpha B R/(2 A) of rho V in 4.43 (2).
(2) The axis vorticity. As in 4.42 (2), eta = Omega_x(0, .) = -b'' - 2 v_2 on J, r = rho eta solves
b r' + (beta/2) r = A/rho, and the backward-orbit formula there, r(y) = A int_{-infinity}^0 e^{beta s/2}/rho(y(s)) ds,
gives r/A > 0 and |r(y)| <= (2 |A|/beta)/min_{[0, infinity)} rho for y >= 0; the minimum is positive because rho is
positive and, by (3), tends to infinity.
(3) Bounds at the end. As in 4.42 (4), b(y)/y -> beta and, with gamma = 1/2 + 1/beta, for every small eps > 0 there
are positive constants c, C with c y^{gamma - eps} <= rho(y) <= C y^{gamma + eps} for large y.
(4) Contradiction. Suppose I_2(y) -> I_inf != 0. Since R -> infinity, int_0^y rho I_2 = I_inf R + o(R), and since
d0 - (beta + 6)/2 = 2 alpha, (1) gives rho^3 v_2 = (A alpha I_inf/4) R + o(R). Fix eps with
0 < 3 eps < (beta - 2)/(2 beta). By (3), R/rho^3 = b/(d0 rho^2) >= c y^{-2/beta - 2 eps}, and by (2) and (3),
|r|/rho <= C y^{-gamma + eps}, a smaller power. With sigma the sign of A I_inf,
sigma b'' = -2 sigma v_2 - sigma r/rho <= -c y^{-p} for large y, where p = 2/beta + 2 eps < 1 and c, C denote positive
constants. Integrating twice gives sigma b(y) <= C y - c y^{2 - p} for large y, with 2 - p > 1, contrary to
b(y)/y -> beta.
Scope. 4.44 uses, on the axis, (T) to order x^4, div W to order x^2, the curl relation and (V) to order x, together
with the parities, the center jet and, only through b(y)/y -> beta at the infinite end, the sublinearity. beta = 2 is
not covered (there alpha = 0 and gamma = 1, so neither the leading term in (4) nor the gap of exponents remains), and
a bounded J is not covered. For a class A profile, at every beta >= 2, |y|^{1 - 2/beta} I_2(y) has a finite limit at
an infinite end of J, with an error O(|y|^{-1/beta}) (4.48), hence I_2 -> 0 if beta > 2; 4.44 does not use class A.
Profiles for which I_2 tends to 0 or to an infinite limit, or has no limit, at the infinite ends of J are not covered
by 4.44 (4.45 excludes the infinite limits); the existence of a profile is not decided. Checks: exact symbolic checks
in the analysis of the coefficients of (T), div W, the curl relation and (V) used in (1) and (2), of the identity in
(1) and its integrated form, of the equation for r and of the exponents in (4); a separate referee audit (VALID WITH
FIXES, 17 independent symbolic checks; its fixes, a signed A in step (0) and the tail wording of (i) and (ii), are
adopted); the verification's own proof (CONFIRMED, 42 exact controls, with the same repair of step (0)). The letters
y_1, K, H, sigma, B, w_1, w_3, v_2, alpha, gamma, eps, c, C, I_inf and p are local to 4.44; A, T, rho, R, b, d0, c_2,
eta and r are as in 4.42.
4.45 Power restrictions for the ratio I_2 at an infinite end of the axis component (restricted exclusion). Assume the
hypotheses of the first paragraph of 4.42, with beta >= 2, and let J and I_2 be as there; let J have an infinite end
and put m = 1 - 2/beta. Then for every s > -m, liminf |y|^{-s} |I_2(y)| = 0 as y tends to that end; that is, there are
no c > 0 and no interval K = (y_1, infinity) or K = (-infinity, -y_1) contained in J at that end with
|I_2(y)| >= c |y|^s on K. No additional derivative bounds at infinity, no class A, no condition on I_3 or on the
higher ratios, no monotonicity or other asymptotic regularity of I_2 and no condition at the other end of J are
assumed. In particular:
  (a) if I_2(y) = L |y|^q (1 + o(1)) as y tends to that end, with real q and L != 0, then q <= -m;
  (b) if beta > 2 and I_2(y) has a limit in [-infinity, infinity] as y tends to that end, the limit is 0; so an I_2
      that is monotone near that end tends to 0, and 4.44 is contained;
  (c) at beta = 2, where m = 0, |I_2(y)| >= c |y|^s near that end is excluded for every s > 0.
Proof outline. (0) As in 4.44 (0), let the end be +infinity and keep the sign of A; the reflection maps
|I_2(y)| to |I_2(-y)|. Let v_2 and gamma be as in 4.44; steps (1) to (3) of 4.44 do not use beta > 2. Put
kappa = (beta + 6)/2, G = int_0^y rho I_2 and, for y >= 1, h = exp(int_1^y kappa/b), Phi = G/h, P = rho^3/(b h),
E = b' - beta and f = eta + 2 c_2/rho^3. Since I_2 is continuous, |I_2| >= c y^s > 0 on K forces one sign of I_2 on K;
so it suffices to exclude, for sigma = 1 and for sigma = -1, that sigma A I_2(y) >= c y^s for y >= Y_0, with s > -m.
Put delta = s + m > 0 and fix a small eps > 0.
(1) Estimates. As in 4.44 (3), b(y)/y -> beta and c y^{gamma - eps} <= rho <= C y^{gamma + eps} for large y; also
c y^{kappa/beta - eps} <= h <= C y^{kappa/beta + eps}, and since 3 gamma - 1 = kappa/beta,
c y^{-4 eps} <= P <= C y^{4 eps}. For y >= Y > 0, mu = exp(int_Y^y beta/(2 b)) satisfies
c y^{1/2 - eps} <= mu <= C y^{1/2 + eps}, and the equation for r in 4.44 (2) gives
(mu r)' = A mu/(b rho) = O(y^{-1 - 1/beta + 2 eps}), which is integrable for 2 eps < 1/beta; so
|r| <= C y^{-1/2 + eps}, |eta| <= C y^{-1 - 1/beta + 2 eps} and, as 3 gamma > 1 + 1/beta,
|f| <= C y^{-1 - 1/beta + 2 eps}. Integrating the hypothesis with the weight rho >= c y^{gamma - eps}, where
s + gamma + 1 > gamma + 1 - m > 0, and using gamma + 1 - kappa/beta = m gives sigma A Phi >= c y^{delta - 2 eps} for
large y.
(2) Exact identities. Since d0 R I_2 = b G', the identity of 4.44 (1) reads 2 v_2 = 2 c_2/rho^3 + (A/4) Phi'/P; since
rho'/rho = (d0 - b')/b and 3 d0 - kappa = 4 beta, b P' = -4 P E; and h Phi = G, h' = kappa h/b. With
eta = -b'' - 2 v_2 from 4.44 (2) it follows that A Phi' = -4 P (E' + f) and that Q = A Phi + 4 P E satisfies
Q' = -16 P E^2/b - 4 P f.
(3) The sign sigma = 1. By (1) the last term of Q' is integrable, so Q <= C_1 for large y. Then
b P' = A Phi - Q >= c y^{delta - 2 eps} for large y, so P >= c y^{delta - 2 eps}, contrary to P <= C y^{4 eps} when
6 eps < delta.
(4) The sign sigma = -1. Put t = log y, a dot for d/dt and u(t) = b(e^t)/e^t, so u -> beta, and Z = -A Phi, so
Z >= c e^{nu t} with nu = delta - 2 eps > 0. By (2), E = u-dot + u - beta, P-dot/P = -4 E/u, Z-dot = 4 P (E-dot + y f)
and Z-dot + (kappa/u) Z = -A y rho I_2/h >= 0; so E-dot >= -kappa Z/(4 u P) - y f, and y f -> 0 by (1). Fix
theta = nu/4 and u_0 < beta so close to beta that on a later tail 0 < chi(u) < theta/2 and |lambda(u)| < theta/2,
where w = (u/u_0)^4, chi(u) = kappa (w - 1)/u and lambda(u) = -4 (u - beta)/u. Then P_1 = P w satisfies
P_1-dot/P_1 = lambda(u), so P_1 <= C e^{theta t/2}, and multiplying the lower bound for E-dot by -4 (P_1 - P) < 0
gives, for M = Z - 4 P_1 E, M-dot <= chi(u) M + 4 P_1 (chi(u) - lambda(u)) E + 4 P_1 y f. With
F(u) = kappa (u^4 - beta^4)/u_0^4 + 16 (u - beta) - 4 (kappa + 4 beta) log(u/beta), so that F' = 4 (chi - lambda),
N = M - P_1 F(u) satisfies N-dot <= chi(u) N + P_1 {(chi(u) - lambda(u)) (F(u) + 4 (u - beta)) + 4 y f} <=
chi(u) N + C P_1, the terms with u-dot cancelling. The integrating factor exp(-int chi(u) dt), which needs no sign of
N, gives N <= C e^{theta t}; hence M <= C e^{theta t}, 4 P_1 E = Z - M >= c e^{nu t} and E >= c e^{3 nu t/4} for large
t. Then u-dot = E - (u - beta) >= 1 for large t, contrary to u -> beta.
(5) Consequences. (a): if q > -m, then |I_2| >= (|L|/2) y^q near the end, contrary to the theorem with s = q. (b): for
beta > 2, s = 0 > -m, and a nonzero finite limit or an infinite limit gives |I_2| >= c > 0 near the end; a monotone
function has a limit in [-infinity, infinity]. (c): m = 0 at beta = 2.
Scope. 4.45 uses what 4.44 uses; beta > 2 enters only through m > 0 in (b). It is a necessary condition at an infinite
end of J and gives no pointwise decay: I_2 may have large excursions along sequences, and an I_2 without a limit is
not excluded. The exponent s = -m is not decided (there the lower bound for sigma A Phi in (1) degenerates); the
relations used here do not decide it, for either sign of A I_2, since axis data that satisfy all of them can have I_2
of exact order |y|^{-m} (4.46) and |y|^m |I_2| -> infinity, for either sign of I_2 if beta > 2 (4.47). At beta = 2,
4.45 excludes neither nonzero finite limits nor A I_2 -> -infinity more slowly than every positive power, and 4.47 (c)
excludes A I_2 -> +infinity; a bounded J is not covered. For a class A profile, at every beta >= 2, |y|^m I_2 has a
finite limit at an infinite end of J (4.48); at beta = 2 every profile under the present hypotheses is in class A
(4.15), so there I_2 has a finite limit at an infinite end of J. The proof of 4.45 does not use class A. The existence
of a profile is not decided. Checks: exact symbolic checks in the analysis of the identities in (2) and (4) and of the
exponent algebra in (1) and (3); a separate referee audit (VALID WITH FIXES for the one-sided proposal and VALID for
(a), for the monotone case of (b) and for sigma = 1, 15 independent exact checks; the fix, the argument of (4) for
sigma = -1, is the referee's and is adopted); the verification's own proofs (CONFIRMED: 59 exact controls for (a) and
the monotone case of (b), 61 for sigma = 1, 50 for both signs). The letters m, s, K, y_1, L, q, c, C, kappa, G, h,
Phi, P, E, f, sigma, Y_0, delta, eps, mu, Y, Q, C_1, t, u, Z, nu, theta, u_0, w, chi, lambda, P_1, M, F and N are
local to 4.45; v_2 and gamma are as in 4.44; A, T, rho, R, b, d0, c_2, eta and r are as in 4.42.
4.46 The exponent of 4.45 for the axis relations (an example of axis data, not a profile). Let beta >= 2, let m, kappa
and gamma be as in 4.45 and d0 = 1 + 3 beta/2, and call axis data smooth real functions b, rho, eta, v_2 and I_2 on R
and a constant A > 0 such that, with T = A/rho^2, R = int_0^y rho, r = rho eta and c_2 = v_2(0): rho > 0,
rho = 1 near 0 and rho b = d0 R; b r' + (beta/2) r = A/rho and eta = -b'' - 2 v_2;
rho^3 v_2 = c_2 + (A/8) [d0 R I_2 - kappa int_0^y rho I_2]; and b(y)/y -> beta as |y| -> infinity. These are the
relations between b, T, eta, v_2 and I_2 that the proofs of 4.44 and 4.45 use (4.44 (1) to (3), here with J = R).
  (a) For beta > 2 and each sigma in {1, -1} there are axis data with I_2(y) = L y^{-m} + O(y^{-1 + 1/beta}) as
      y -> infinity and sigma L > 0.
  (b) At beta = 2, where m = 0, there are axis data for which I_2(y) tends to any prescribed real number as
      y -> infinity.
So for every beta >= 2 the condition s > -m in 4.45 cannot be weakened to s >= -m, for either sign of A I_2, by an
argument that uses only these relations. The fields Theta = T x^2/2 + T^2 I_2 x^4/24, W_2 = b + v_2 x^2,
W_1 = (2 beta - b') x - v_2' x^3/3 and Omega = d_y W_1 - d_x W_2 built from axis data have the parities of 4.42,
div W = 2 beta, W(0) = 0, Theta(0, y) = 0 and Theta = (A/2) x^2 + O(|X|^3) at 0, and they satisfy the coefficients of
x^2 and x^4 of (T) and of x of (V) on the axis; they do not satisfy W = beta X + o(|X|), since W_2(x, 0) = c_2 x^2 and
the relations at y = 0 give c_2 = -A/beta, and the higher coefficients of (T) and (V) are not imposed. So axis data
are not shown to be the axis values of a profile, and 4.46 says nothing about whether a profile can have I_2 of exact
order |y|^{-m}.
Proof outline. Steps (0) to (4) prove (a). (0) Transport. Let e_0(t) = exp(-1/t) for t > 0 and e_0(t) = 0 for t <= 0,
and chi(y) = e_0(y^2 - 1)/(e_0(y^2 - 1) + e_0(4 - y^2)); chi is smooth and even, chi = 0 on |y| <= 1, chi = 1 on
|y| >= 2 and chi' > 0 on (1, 2). Let b be the odd function with b(0) = 0 and b' = d0 + (beta - d0) chi. Since
beta - d0 = -(1 + beta/2) < 0: b = d0 y on |y| <= 1, beta <= b' <= d0, b > 0 and b'' <= 0 on y > 0, and
b = beta (y + y_0) for y >= 2, with y_0 = (d0 - beta) int_0^2 (1 - chi)/beta > 0; so b(y)/y -> beta.
(1) Density. Let rho = 1 on [-1, 1] and rho'/rho = (d0 - b')/b elsewhere. Then rho is smooth, even, positive and
nondecreasing on y > 0, (rho b)' = d0 rho, so that R = rho b/d0, and for y >= 2, rho = C z^gamma with z = y + y_0 and
a constant C > 0. T = A/rho^2 satisfies b T' + (3 beta + 2 - 2 b') T = 0.
(2) Vorticity. With a = beta/(2 d0) put r = (A/d0) R^{-a} int_0^y R^{a - 1} for y > 0 and extend r evenly. Then
r = 2A/beta on |y| <= 1, r > 0, b r' + (beta/2) r = A/rho, and r = D z^{-1/2} - (A/C) z^{-gamma} for y >= 2 with a
constant D > 0. Put eta = r/rho and v_2 = -(b'' + eta)/2; on |y| <= 1, v_2 = -A/beta = c_2.
(3) The ratio. Let G = 0 on [-1, 1] and solve b G' - kappa G = (8/A)(rho^3 v_2 - c_2) on y > 1 and on y < -1;
the right side vanishes on |y| <= 1 and b != 0 for y != 0, so G is smooth on R. Put I_2 = G'/rho; since
d0 R = rho b, this is the identity for rho^3 v_2. For y >= 2,
G = K z^{kappa/beta} + (4 D C^2/A) z^{1/2 + 2/beta} - 2 C z^gamma + 8 c_2/(A kappa) with a constant K, and since
kappa/beta - 1 - gamma = -m, I_2 = L z^{-m} + O(z^{-1 + 1/beta}) with L = kappa K/(beta C); also
z^{-m} = y^{-m} + O(y^{-m - 1}) and -m - 1 < -1 + 1/beta < -m.
(4) The sign of L. b, rho, r/A and eta/A do not depend on A; so G = G_b/A + G_e, where G_b and G_e vanish on [-1, 1],
b G_b' - kappa G_b = -4 rho^3 b'' and b G_e' - kappa G_e = -4 u with u = rho^2 r/A - 2/beta. With
h = exp(int_1^y kappa/b), a positive multiple of z^{kappa/beta} for y >= 2, (G_b/h)' = -4 rho^3 b''/(b h) is >= 0,
positive on (1, 2) and zero for y >= 2, and (G_e/h)' = -4 u/(b h). On y > 0, u = 0 on [0, 1] and
b u' = (2 d0 - beta/2 - 2 b') u + (4/beta)(d0 - b') + rho - 1, whose last two terms are >= 0 and positive for y > 1;
so u > 0 for y > 1, and u/(b h) = O(y^{-1 - 1/beta}) is integrable. Hence K = K_b/A + K_e with constants K_b > 0 > K_e
that do not depend on A, and sigma L > 0 for A < K_b/|K_e| if sigma = 1 and for A > K_b/|K_e| if sigma = -1.
(5) Proof of (b). Steps (0) to (3) hold at beta = 2. Then kappa = d0 and b R' - kappa R = 0, so G + I_0 R solves the
equation of (3) for every real I_0, and replaces I_2 by I_2 + I_0; by (3) with m = 0, I_2 has a finite limit, which is
thus arbitrary.
(6) The fields. div W = 2 beta and the parities are immediate. The coefficient of x^2 of the residual of (T) is
(b T' + (3 beta + 2 - 2 b') T)/2 = 0, the coefficient of x of the residual of (V) is
b eta' + (2 beta + 1 - b') eta - T = 0 by (2), and 24 times the coefficient of x^4 of the residual of (T),
b Q' + (7 beta + 2 - 4 b') Q - 8 v_2' T + 12 v_2 T' with Q = T^2 I_2, equals
(A^2/rho^4) (b I_2' + (beta - 2) I_2 - 8 (rho^3 v_2)'/(A rho)), which vanishes by the derivative of the identity for
rho^3 v_2 (d0 - kappa = beta - 2). At beta = 2 and |y| < 1 the residual of (V) is -(A^2 I_0/6) x^3.
Scope. 4.46 concerns only the listed relations and is neither a profile nor an exclusion. It shows that 4.44 and 4.45
are optimal for those relations: excluding |I_2| >= c |y|^{-m} at an infinite end of J, or at beta = 2 a nonzero
finite limit, needs further information, for example higher coefficients of (T) and (V) on the axis (as used in 4.41
to 4.43) or the equations off the axis. For a class A profile, at every beta >= 2, |y|^m I_2 has a finite limit at an
infinite end of J, with an error O(|y|^{-1/beta}) (4.48); so for such profiles |I_2| = O(|y|^{-m}) there, and whether
the exact order |y|^{-m} occurs is not decided. The existence of a profile is not decided. Checks: exact symbolic
checks in the analysis of the identities in (1) to (4) and (6), of the tail formulas and of the identity for u;
separate referee audits (VALID, 56 exact checks for the construction and 19 for the variant); the verification's own
construction and controls (CONFIRMED, 48 + 22 exact controls, for the construction, and 57 for the concave variant).
The letters sigma, L, e_0, chi, y_0, z, C, a, D, G, K, G_b, G_e, u, h, K_b, K_e, I_0 and Q, and Theta, W and Omega
(the last three for the fields of the example only) are local to 4.46; m, kappa and gamma are as in 4.45; v_2 is
as in 4.44; A, T, rho, R, b, d0, c_2, eta and r are as in 4.42.
4.47 Logarithmically enhanced critical tails for the axis relations (examples of axis data, not profiles, and a
restricted exclusion at beta = 2). Let beta >= 2, let m and kappa be as in 4.45 and d0 = 1 + 3 beta/2, let axis data
be as in 4.46, and let ell > 0.
  (a) There are axis data with I_2(y) = L y^{-m} (log y)^ell (1 + o(1)) as y -> infinity and L < 0.
  (b) Let beta > 2. For each sigma in {1, -1} there are axis data with b' >= beta and b'' <= 0 on y > 0 and
      I_2(y) = L y^{-m} (log y)^ell (1 + o(1)) as y -> infinity and sigma L > 0.
  (c) Let beta = 2. Under the hypotheses of the first paragraph of 4.42, with J and I_2 as there and A = 2 a0,
      A I_2(y) does not tend to +infinity as y tends to an infinite end of J; equivalently, liminf A I_2 < +infinity
      there. For axis data, I_2(y) does not tend to +infinity as y -> infinity.
So the relations used in 4.45 do not bound |y|^m |I_2| near an infinite end: at the exponent -m the conclusion of 4.45
fails for them even in the form liminf |y|^m |I_2| < infinity. At beta = 2, where m = 0, they allow I_2 -> -infinity
(in (a) with |I_2| = o(|y|^s) for every s > 0, consistent with 4.45 (c)) and every finite limit (4.46 (b)), but not
I_2 -> +infinity; for profiles at beta = 2, A I_2 -> +infinity at an infinite end of J is excluded. For beta > 2 they
allow I_2 -> 0 with |y|^m |I_2| -> infinity, for either sign of I_2. As in 4.46, axis data are not shown to be the
axis values of a profile (the polynomial fields built from them in 4.46 violate W = beta X + o(|X|), and the higher
coefficients of (T) and (V) are not imposed), and (a) and (b) by themselves say nothing about whether a profile can
have such a tail; for class A profiles, and so for every profile at beta = 2, 4.48 excludes it.
Proof outline. (0) Notation. For y >= 1 let G, h, Phi, P, E, f and Q be as in 4.45 (1) and (2). For axis data, and
under the hypotheses of 4.42 at an infinite end +infinity of J, the bounds of 4.45 (1) on b, rho, h, P, r, eta and f
(4.45 (1) integrates the equation for r from a finite point, so the backward-orbit formula of 4.44 (2) is not needed)
and the identities b P' = -4 P E, A Phi' = -4 P (E' + f) and Q' = -16 P E^2/b - 4 P f of 4.45 (2) hold; by 4.45 (1),
int^infinity |P y f| dt < infinity. Put t = log y, a dot for d/dt, u(t) = b(e^t)/e^t and H = A Phi, so that
E = u-dot + u - beta. Since R'/R = d0/b, h = C_h R^{kappa/d0} and P = d0^3 R^{4 beta/d0}/(C_h b^4) with a constant
C_h > 0, and differentiating G = h Phi gives the exact formula
(*) A I_2 = (C_h/d0) R^{kappa/d0 - 1} (u H-dot + kappa H), where kappa - d0 = -beta m.
(1) Proof of (a). Let a = (ell/(2 - m/2))^{1/2} and p = 2 a^2. Choose t_0 > max(2, 16 a^2) and, with flat cutoffs
built from e_0 as in 4.46 (0), a smooth odd b with b = d0 y on |y| <= 1, b > 0 on y > 0, b(y)/y -> beta, and
b(y) = beta y (1 + w(t)) with w(t) = a t^{-1/2} sin t for t >= t_0 + 1. Let rho, r, eta, v_2, G and I_2 be defined
from b as in 4.46 (1) to (3) (only the definitions there are used); these are axis data. On the tail
R-dot/R = d0/u = (d0/beta)/(1 + w), and 1/(1 + w) = 1 - w + w^2 - w^3/(1 + w) with w^2 = a^2 (1 - cos 2t)/(2t); the
integrals of w, of the oscillating part of w^2 and of the last term converge, so
R = C_R y^{d0/beta} t^{d0 a^2/(2 beta)} (1 + o(1)) with C_R > 0, and by (0) P = P_0 t^p (1 + o(1)) with P_0 > 0.
Further E = beta a (sin t + cos t) t^{-1/2} + O(t^{-3/2}) and E^2 = beta^2 a^2 (1 + sin 2t)/t + O(t^{-2}); integrating
Q-dot = -16 P E^2/u - 4 P y f, in which the oscillating part and the error terms contribute o(t^p), gives
Q = -8 beta P_0 t^p + o(t^p). Since P E = O(t^{p - 1/2}), H = Q - 4 P E = -8 beta P_0 t^p + o(t^p), and the exact
equation H-dot = -4 P (E-dot + y f) gives H-dot = o(t^p). By (*), since
R^{kappa/d0 - 1} = C_R^{-beta m/d0} y^{-m} t^{-m a^2/2} (1 + o(1)), I_2 = L y^{-m} t^ell (1 + o(1)) with
ell = p - m a^2/2 = a^2 (2 - m/2) and L = -8 kappa d0^2 C_R^2/(A beta^3) < 0.
(2) Proof of (b). Let a = ell/m and mu = (d0 - beta)/(beta a). With e_0 as in 4.46 (0) put
zeta(s) = e_0(s)/(e_0(s) + e_0(1 - s)) and g(t) = int_0^t zeta, and let b be the odd function with b(0) = 0 and
b'(y) = beta + (d0 - beta)/(1 + mu g(log |y|)) for y != 0. Then b = d0 y on |y| <= 1, beta <= b' <= d0, b'' < 0 for
y > 1, and for log y >= 1, b' = beta + beta a/(t + k) with a constant k such that t + k > 0, so
b(y) = beta y (1 + a/t + O(t^{-2})) and b(y)/y -> beta. Let rho, r, eta, v_2, G and I_2 be defined from b as in 4.46
(1) to (3) (only the definitions there are used). Then R = C_R y^{d0/beta} t^{-d0 a/beta} (1 + O(1/t)) with C_R > 0,
P = P_0 t^{-4a} (1 + O(1/t)) with P_0 > 0 by (0), and r/A = D_1 y^{-1/2} t^{a/2} (1 + o(1)) with D_1 > 0. As in 4.46
(4), G = G_b/A + G_e, (G_b/h)' = -4 P b'' > 0 for y > 1 and (G_e/h)' = -4 u_e/(b h) < 0 for y > 1, where
u_e = rho^2 r/A - 2/beta (the function u of 4.46 (4), positive for y > 1). Since P b'' = O(y^{-1} t^{-4a - 2}) and
u_e/(b h) = O(y^{-1 - 1/beta} t^{(1/beta - 2) a}), G_b/h -> K_b > 0 and G_e/h -> K_e < 0, with constants that do not
depend on A, and the same equations give (G_b/h)-dot -> 0 and (G_e/h)-dot -> 0. With (*) and
R^{kappa/d0 - 1} = C_R^{-beta m/d0} y^{-m} t^{m a} (1 + O(1/t)), I_2 = L y^{-m} t^ell (1 + o(1)) with ell = m a and
L = (kappa C_h/d0) C_R^{-beta m/d0} (K_b/A + K_e); so sigma L > 0 for A < K_b/|K_e| if sigma = 1 and for A > K_b/|K_e|
if sigma = -1.
(3) Proof of (c). The reflection of 4.8 maps J to -J and A I_2(y) to A I_2(-y) (4.42 (0)); so let the end be +infinity
(for axis data, A > 0). Here d0 = kappa = 4, and (*) reads H-dot + (4/u) H = (4/(C_h u)) A I_2. Suppose
A I_2 -> +infinity. Since 4/u lies between positive constants on a tail, comparison with constants gives
H -> +infinity. Put N(t) = 4 int_t^infinity P(e^s) e^s f(e^s) ds, which tends to 0, and q = Q - N. Then
q-dot = -16 P E^2/u <= 0, and with D = -E, 4 P D = H - q - N -> +infinity, since q is bounded above on a tail; so
D > 0 on a tail and P-dot = 4 P D/u -> +infinity. If q(t_1) < 0 for some large t_1, then z = -q/P > 0 for t >= t_1,
z-dot = (4 D/u)(4 D - z) and P (4 D - z) = H - N > 0 on a tail; so z increases there, z >= z_0 > 0 and D >= z_0/4, and
u-dot = 2 - u - D <= -z_0/8 for large t, contrary to u -> 2. Otherwise q >= 0 on a tail; then q has a finite limit and
int^infinity P D^2 dt < infinity, so F = P^{1/2}, with F-dot = 2 P^{1/2} D/u, has a square integrable derivative; by
the Cauchy-Schwarz inequality F(t) = o(t^{1/2}), that is P = o(t), contrary to P-dot -> +infinity.
Scope. (a) and (b) concern only the relations of 4.46 and are neither profiles nor exclusions; excluding
|y|^m |I_2| -> infinity at an infinite end of J, for beta > 2 or at beta = 2 with A I_2 -> -infinity, needs further
information, as in the scope of 4.46. In the data of (a) and (b), b(y) - beta y is not O(|y|^{1 - 1/beta}) (in (b) it
is asymptotic to beta a y/log y); so they are not the axis values of a class A profile, for which
b(y) - beta y = O(|y|^{1 - 1/beta}) at an infinite end of J at every beta >= 2 (4.48 (b)). (c) is a necessary
condition at beta = 2 that 4.45 (c) does not contain; it uses only the relations of 4.46 and b(y)/y -> 2, excludes
neither finite limits, nor A I_2 -> -infinity, nor limsup A I_2 = +infinity with a finite liminf, and does not cover a
bounded J. For profiles at beta = 2, 4.48 (b) contains (c): there I_2 has a finite limit at an infinite end of J. The
existence of a profile is not decided. Checks: exact symbolic checks in the analysis of (*), of the identities and
exponents in (1) and (2) and of the equations for z and F in (3); separate referee audits (A157, VALID, 27 exact
checks; A158, VALID WITH FIXES, 37 exact checks, with the stated wording and finite-point ODE clarification adopted;
A159, VALID, 24 exact checks); the verification's own constructions, proof and controls (P266, 62 exact controls;
P270, 65 exact controls; P271, 46 exact controls; P274, the complete entry, 236 controls, CONFIRMED 2026-10-22 04:29
to 04:31). The letters ell, L, sigma, C_h, H, t, u, a, p, t_0, w, C_R, P_0, mu, zeta, g, k, D_1, u_e, G_b, G_e, K_b,
K_e, N, q, D, t_1, z, z_0 and F are local to 4.47; m and kappa, and G, h, Phi, P, E, f and Q, are as in 4.45; e_0 is
as in 4.46; v_2 is as in 4.44; A, T, rho, R, b, d0, c_2, eta and r are as in 4.42.
4.48 Critical limits of the axis ratios at an infinite end of the axis component (necessary conditions). Let
beta >= 2, let m and kappa be as in 4.45 and gamma as in 4.44, and assume the hypotheses of the first paragraph of
4.42, with J and I_n as there; let J have an infinite end.
  (a) Suppose that for some delta > 0 and constants C_0 and C_2, |W_2(0, y) - beta y| <= C_0 |y|^{1 - delta} and
      |d_y^2 W_2(0, y)| <= C_2 |y|^{-1 - delta} for |y| large at that end. Then, with eps = min(delta, 1/beta), there
      is a real L such that I_2(y) = L |y|^{-m} + O(|y|^{-m - eps}) as y tends to that end; L = 0 is not excluded. The
      proof uses only the relations of 4.46 at that end, so the same holds for axis data (4.46) with b in place of
      W_2(0, .) as y -> infinity.
  (b) Let (Theta, Omega, W - beta X) be a class A profile; by 4.15 this holds for every profile under the present
      hypotheses at beta = 2, and for beta > 2 if Omega is polynomially bounded. Then the bounds of (a) hold at every
      infinite end of J with delta = 1/beta (and so do the bounds
      |d_y^j (W_2(0, y) - beta y)| <= C_j |y|^{1 - 1/beta - j} for every j), and for every n >= 2 there is a real L_n
      with I_n(y) = L_n |y|^{-(n - 1) m} + O(|y|^{-(n - 1) m - 1/beta}) as y tends to that end. In particular
      I_2(y) = L_2 |y|^{-m} + O(|y|^{-1 + 1/beta}), and at beta = 2 every I_n has a finite limit at every infinite end
      of J.
  (c) The bound on d_y^2 W_2(0, y) cannot be omitted from (a), even for concave transport: for every beta >= 2 and
      0 < delta < 1 there are axis data (4.46) with |b(y) - beta y| <= C_0 y^{1 - delta} and
      |b'(y) - beta| <= C_1 y^{-delta} for y >= 1 and b'' <= 0 on y > 0, for which
      limsup_{y -> infinity} y^m I_2(y) = +infinity. At beta = 2, where m = 0, this I_2 is unbounded above; 4.47 (c)
      excludes only A I_2 -> +infinity.
So for class A profiles, and at beta = 2 for every profile under the hypotheses of 4.42, |y|^m I_2 has a finite limit
at each infinite end of J; in particular I_2 = O(|y|^{-m}) there. For them this contains 4.44 and the conclusions of
4.45 and 4.47 (c) at those ends, which assume neither class A nor the bounds of (a), and it excludes
I_2(y) = L' |y|^{-m} (log |y|)^ell (1 + o(1)) with L' != 0 and ell > 0 at every beta >= 2: the axis data of 4.47 (a)
and (b) are not the axis values of a class A profile, which does not affect them as axis data. The data of 4.46 (a)
satisfy the bounds of (a) with delta = 1 (b = beta (y + y_0) for y >= 2, 4.46 (0)), and 4.46 (a) gives sigma L > 0 for
each sigma; so for the relations of 4.46 the case L != 0 occurs, with either sign, for beta > 2. Whether a profile can
have L != 0 is not decided.
Proof outline. (0) The reflection of 4.8 maps J to -J, I_n(y) to (-1)^{n+1} I_n(-y) and g(y) = W_2(0, y) - beta y to
-g(-y), and it preserves class A; so let the end be +infinity, and keep the sign of A = 2 a0. Let G, h, Phi, P, E and
f be as in 4.45 (0), and H = A Phi.
(1) Asymptotics. Since R'/R = d0/b and d0/b - d0/(beta y) = O(y^{-1 - delta}) is integrable,
R = C_R y^{d0/beta} (1 + O(y^{-delta})) with C_R > 0, and rho = d0 R/b = C_rho y^gamma (1 + O(y^{-delta})) with
C_rho = d0 C_R/beta; in the same way h = C_h y^{kappa/beta} (1 + O(y^{-delta})) and, for a fixed Y > 0,
mu = exp(int_Y^y beta/(2 b)) = C_mu y^{1/2} (1 + O(y^{-delta})), with positive constants C_h and C_mu. As in 4.45 (1),
(mu r)' = A mu/(b rho) = O(y^{-1 - 1/beta}), so r = O(y^{-1/2}), eta = O(y^{-1 - 1/beta}) and, since
3 gamma > 1 + 1/beta, f = O(y^{-1 - 1/beta}); and since 3 gamma - 1 = kappa/beta, P = P_inf (1 + O(y^{-delta})) with
P_inf > 0. Only the bound on W_2(0, y) - beta y is used here, and no asymptotic formula is differentiated.
(2) Proof of (a). By 4.45 (2), H' = -4 P (b'' + f) (E' = b''), which is O(y^{-1 - eps}) by (1) and the bound on b''.
So H = H_inf + O(y^{-eps}) with a real H_inf, and b H' = O(y^{-eps}). Differentiating G = h H/A and using
h' = kappa h/b gives I_2 = h (kappa H + b H')/(A b rho), and
h/(b rho) = (C_h/(beta C_rho)) y^{-m} (1 + O(y^{-delta})), since kappa/beta - 1 - gamma = -m; this gives (a) with
L = kappa C_h H_inf/(A beta C_rho). Only the relations of 4.46 are used (through 4.44 (1) and (2) and 4.45 (2)).
(3) The bounds for class A. With V = W - beta X, the rescaled fields of 4.16 step (1) and their uniform bounds in 4.16
step (2) give, by the identities of 4.37 step (5), |D^alpha V(X)| <= C_alpha |X|^{1 - 1/beta - |alpha|} for |X| >= 1;
this derivation does not use beta > 2. At x = 0, W_2(0, y) - beta y = V_2(0, y), so the bounds of (a) hold with
delta = 1/beta.
(4) Higher ratios. Let t, u, theta and theta0 be as in 4.16 steps (1) and (2), with t = -tau. Since
d_t theta = -u.grad theta and, by 4.16 step (2), u and theta have bounded derivatives of every order near e_2 = (0, 1)
uniformly in 0 < tau <= 1, theta(-tau, .) = theta0 + O(tau) in every C^j near e_2. With tau = y^{-1/beta},
Theta(x, y) = tau^{2 - beta} theta(-tau, (x/y, 1)), so d_x^{2n} Theta(0, y) = y^{m - 2n} (a_n + O(y^{-1/beta})) with
a_n = d_{z_1}^{2n} theta0(e_2). By (1) and (3), T = A/rho^2 = (A/C_rho^2) y^{m - 2} (1 + O(y^{-1/beta})), since
2 gamma = 2 - m; so a_1 = A/C_rho^2 != 0, and I_n = d_x^{2n} Theta(0, .)/T^n gives (b) with L_n = a_n/a_1^n, since
m - 2n - n (m - 2) = -(n - 1) m. At beta = 2, m = 0.
(5) Proof of (c). Let chi be smooth and nondecreasing on R, with chi = 0 on (-infinity, 0], chi = 1 on [1, infinity)
and chi'(s_0) > 0 for some s_0 in (0, 1). For n >= N let w_n = 2^{n (1 - delta)}/n and q_n = k 2^{-n delta}, where N
is so large that w_n <= 2^n/4 for n >= N and k > 0 is chosen so that the sum of the q_n over n >= N is d0 - beta. Let
b be the odd function with b(0) = 0 and b' = beta + sum_{n >= N} q_n (1 - chi((y - 2^n)/w_n)) for y >= 0. The
intervals [2^n, 2^n + w_n] are disjoint and only finitely many of them meet a bounded set, so b is smooth, b = d0 y on
|y| <= 2^N, b'' <= 0 on y > 0 and the integral of -b'' over y > 0 is d0 - beta; and for 2^i <= y < 2^{i + 1}
with i >= N, 0 < b' - beta <= sum_{n >= i} q_n = k 2^{-i delta}/(1 - 2^{-delta}) <
k 2^delta y^{-delta}/(1 - 2^{-delta}), which gives the two bounds, the first by integration since delta < 1. Define
rho, r, eta, v_2, G and I_2 from b as in 4.46 (1) to (3), with [-1, 1] replaced by [-2^N, 2^N]; these are axis data.
By (1), which uses only the first bound, y^m h/(b rho) -> H_0 = C_h/(beta C_rho) > 0, P -> P_inf > 0 and b f -> 0; so
Phi' = -(4/A) P (b'' + f) is integrable on y > 0 and Phi has a finite limit. By the extraction formula of (2),
y^m I_2 = (y^m h/(b rho)) (kappa Phi - (4/A) P b (b'' + f)). At p_n = 2^n + s_0 w_n only the term with index n varies,
-b''(p_n) = q_n chi'(s_0)/w_n = k n 2^{-n} chi'(s_0) and p_n/2^n -> 1, so -b b''(p_n) = beta k chi'(s_0) n (1 + o(1))
and, since A > 0, p_n^m I_2(p_n) -> +infinity.
Scope. (a) uses what 4.45 uses and, at that end, the bounds on W_2(0, y) - beta y and its second derivative; (b) uses
in addition the class A theory of 4.15, 4.16 steps (1) and (2) and 4.37 step (5); (c) concerns axis data only and uses
the relations of 4.46 and its steps (1) to (3), and it does not bear on class A profiles, for which (b) gives the
bound on the second derivative. Neither (a) nor (b) treats a bounded J, gives the sign of L or decides whether L != 0
for a profile; the existence of a profile is not decided. Checks: exact symbolic checks in the analysis of the
exponent identities, of the identity for H', of the extraction formula, of the transport equation of the rescaled
temperature, of the scaling of the symbol bounds and of the scalings in (5); separate referee audits (A160, VALID WITH
FIXES, exact symbolic checks of the axis coefficients, the integrated quartic identity, the extraction formula, the
identity for P and the exponents, with its fixes adopted; A158, VALID WITH FIXES, 37 exact checks, for the
construction of (c) with the repair of A160); the verification's own proofs and controls (P272, 79 exact controls;
P275, 91 exact controls; P276, the complete entry with its recorded p_n notation correction, 273 controls, CONFIRMED
2026-10-22 04:44 to 04:47). The letters delta, C_0, C_2, C_j, eps, L, L', ell, L_n, g, C_R, C_rho, C_h, Y, mu, C_mu,
P_inf, H, H_inf, V, alpha, C_alpha, tau, e_2, z_1, a_n, chi, s_0, N, w_n, q_n, k, i, H_0 and p_n are local to 4.48; t,
u, theta and theta0 are as in 4.16; m, kappa, G, h, Phi, P, E and f are as in 4.45; gamma is as in 4.44; sigma and y_0
are as in 4.46; J, I_n, A, T, rho, R, b, d0, eta and r are as in 4.42.
4.49 A bounded axis component is consistent with all axis equations (examples, not profiles). Let beta >= 2,
d0 = 1 + 3 beta/2, A != 0 and c0 real. There are smooth Psi, Theta and Omega of compact support on R^2, Psi and Omega
odd and Theta even in x, with Theta(0, .) = 0 and Omega = -Lap Psi, such that, with U = (-Psi_y, Psi_x),
W = beta X + U - U(0), R_Theta = W.grad Theta - (beta - 2) Theta and R_Omega = W.grad Omega + Omega - Theta_x:
  (a) div U = 0, -curl U = Omega and U has compact support, so (A4) holds; U is the Biot-Savart velocity K * Omega of
      (A5), and U(0) = (0, c0). Near 0, Theta = (A/2) x^2, Omega = (2A/beta) x and
      W = ((beta - 2) x/2, d0 y - (A/beta) x^2), so (T) and (V) hold on a neighbourhood of 0, a0 = A/2 and
      Psi_xy(0) = 1 + beta/2;
  (b) d_x^i d_y^j R_Theta and d_x^i d_y^j R_Omega vanish at every point of the axis, for all i, j >= 0;
  (c) b = W_2(0, .) is odd on [-4, 4], its zeros there are -3, 0 and 3, and b = (y - 3)^2 near 3; J = (-3, 3) is the
      component of {Theta_xx(0, .) != 0} that contains 0; every d_x^{2n} Theta(0, .) and every d_x^{2n+1} Omega(0, .)
      is flat at -3 and 3; and, with T = Theta_xx(0, .), D = d_x^4 Theta(0, .), I_2 = D/T^2 and s = 3 - |y|,
      D/T = -(6 d0/beta) s^{-2} (1 + o(1)) and A I_2 -> -infinity as |y| -> 3 inside J;
  (d) int Theta R_Theta dX = 2 (1 - beta) int Theta^2 dX < 0, so R_Theta is not identically 0, and these fields are
      not profiles.
So these data alone cannot exclude a bounded J: the coefficients of (T) and (V) of every order on the whole axis,
together with the parities, the center jet and (A4), are consistent with a bounded J at every beta >= 2, and with
A I_2 -> -infinity at its finite ends. An exclusion of profiles with a bounded J needs information from the equations
beyond their axis jets, or a property not implied by the conditions listed, for example real analyticity near the axis
(see the scope below), a sign of Omega or a tail of Omega.
Proof outline. (0) Transport. With e_0 as in 4.46 (0), let chi_1(y) = e_0(y - 1)/(e_0(y - 1) + e_0(2 - y)) (smooth, 0
for y <= 1 and 1 for y >= 2) and chi_4(y) = chi_1(y - 3), let, for y >= 0, b_1 = (1 - chi_1) d0 y + chi_1 (y - 3)^2
and b_* = (1 - chi_4) b_1 + chi_4 beta y; extend b_* oddly and put b = b_* - c0 chi_4(|y|). Then b = d0 y on |y| <= 1,
b = (y - 3)^2 on [2, 4], b = -(y + 3)^2 on [-4, -2] and b = beta y - c0 for |y| >= 5. On [1, 2] and on [4, 5], b_*
interpolates between two positive functions, so on [-4, 4] the zeros of b are -3, 0 and 3, and b has the sign of y on
J; no zero of b with |y| > 4 is used.
(1) The second jet. Let rho = 1 on [-1, 1] and rho'/rho = (d0 - b')/b on the rest of J (the coefficient vanishes to
every order at -1 and 1), a_1 = A/(2 rho^2) on J and a_1 = 0 outside J. On 2 <= |y| < 3, with tau = 1/s,
rho = C tau^2 exp(d0 tau) and a_1 = (A/(2 C^2)) tau^{-4} exp(-(3 beta + 2) tau) with one constant C > 0 (rho is even);
each y-derivative of a_1 is a polynomial in tau and 1/tau times this exponential, so a_1 is smooth and flat at -3 and
3, and b a_1' + (3 beta + 2 - 2 b') a_1 = 0 on R.
(2) The axis equations. For the formal series Theta ~ sum_{n >= 1} a_n x^{2n}, W_2 ~ b + sum_{j >= 1} v_{2j} x^{2j},
W_1 ~ (2 beta - b') x - sum_{j >= 1} v_{2j}' x^{2j+1}/(2j + 1) (so that div W = 2 beta) and
Omega ~ sum_{n >= 0} q_n x^{2n+1}, the relation Omega = d_y W_1 - d_x W_2 reads
q_n = -v_{2n}''/(2n + 1) - (2n + 2) v_{2n+2} (n >= 0, with v_0'' := b''), and the coefficients of x^{2n} in R_Theta
and of x^{2n+1} in R_Omega vanish exactly when
  (T_n) b a_n' + [(4n - 1) beta + 2 - 2n b'] a_n = sum_{j=1}^{n-1} [2 (n - j) v_{2j}' a_{n-j}/(2j + 1) -
      v_{2j} a_{n-j}'] (n >= 1),
  (V_n) b q_n' + [(4n + 2) beta + 1 - (2n + 1) b'] q_n = 2 (n + 1) a_{n+1} + sum_{j=1}^{n}
      [(2 (n - j) + 1) v_{2j}' q_{n-j}/(2j + 1) - v_{2j} q_{n-j}'] (n >= 0).
Let q_0 = 2A/beta on [-1, 1] and solve (V_0) on the rest of J; put v_2 = -(b'' + q_0)/2 (= -A/beta on [-1, 1]); solve
(T_2) on J with a_2 = 0 on [-1, 1]; and for n >= 1 in turn solve (V_n) for q_n, put
v_{2n+2} = -(q_n + v_{2n}''/(2n + 1))/(2n + 2), and solve (T_{n+2}) for a_{n+2}, with q_n = a_{n+2} = 0 on [-1, 1]. On
[-1, 1] these constant and zero coefficients solve their equations; the coefficients match to every order at -1 and 1,
where b is nonzero, so the solutions attach smoothly. Each a_n and q_n is extended by 0 outside J, and each v_{2j} is
defined on R by the curl relation.
(3) Flatness at the ends. On 2 <= |y| < 3, b d_y = d_tau, b' = -2/tau and d_y = sgn(y) tau^2 d_tau. For sigma > 0 let
E_sigma be the set of functions of tau >= 1 whose tau-derivatives of order k are bounded by
C_k tau^{N_k} exp(-sigma tau); E_sigma is closed under d_y and under multiplication by polynomials in tau and 1/tau,
E_sigma E_sigma' is contained in E_{sigma + sigma'}, E_sigma' is contained in E_sigma for sigma' > sigma, and a
function in E_sigma extends by 0 smoothly across s = 0. If mu > sigma > 0 and g is in E_sigma, every solution of
z_tau + (mu + nu/tau) z = g is in E_sigma (integrating factor). Let Lambda = 3 beta + 2 and M = 2 beta + 1 as in 4.13.
Then a_1 is in E_Lambda; (V_0) reads (q_0)_tau + (M + 2/tau) q_0 = 2 a_1, so q_0 = tau^{-2} exp(-M tau)
(c_1 + int^tau t^2 exp(M t) 2 a_1 dt) with a convergent integral (Lambda > M), and q_0 is in E_M. Since b'' = 2 near 3
and b'' = -2 near -3, v_2 + 1 is in E_M near 3 and v_2 - 1 is in E_M near -3. By induction in the order of (2), a_n is
in E_Lambda, q_n is in E_M and v_{2j}, j >= 2, is in E_M: the constant coefficients satisfy (4n - 1) beta + 2 > Lambda
(n >= 2) and (4n + 2) beta + 1 > M (n >= 1), the forcing is in E_Lambda, respectively E_M, and the curl relation gives
v_{2n+2} in E_M (for n = 1 since v_2'' = -q_0''/2 near -3 and 3). So all a_n and q_n are smooth and flat at -3 and 3,
and (T_n) and (V_n) hold on R (outside J because a_n = q_n = 0 there). Outside J, v_{2j} = (-1)^j b^{(2j)}/(2j)!,
which is 0 for |y| >= 5 and, for j >= 2, near -3 and 3; so every a_n, q_n and v_{2j} vanishes for |y| >= 5.
(4) Realization. With chi smooth and even, chi = 1 on |x| <= 1/2 and chi = 0 on |x| >= 1, and g1 = b - beta y + c0,
let Psi = g1 x chi(x) + sum_{j >= 1} v_{2j} x^{2j+1} chi(x/eps_j)/(2j + 1) and
Theta = sum_{n >= 1} a_n x^{2n} chi(x/delta_n). For f of compact support, f(y) x^l chi(x/eps) has C^k norm at most
C_{f,l,k} eps^{l - k} for k < l and 0 < eps <= 1; with eps_j <= 2^{-j} and delta_n <= 2^{-n} chosen so that the j-th
(n-th) term has C^k norm at most 2^{-j} (2^{-n}) for k <= j (k <= n), both series converge in every C^k, so Psi and
Theta are smooth, supported in [-1, 1] x [-5, 5], Psi odd and Theta even in x, and their x-Taylor coefficients on the
axis are g1, v_{2j}/(2j + 1) and a_n. Then g1 = Psi_x(0, .) is the g1 of 4.29, W_2(0, .) = beta y + g1 - c0 = b, W_1
and W_2 have the expansions of (2) (g1' = b' - beta and g1'' = b''), the x-Taylor coefficients of Omega = -Lap Psi are
the q_n, and by (T_n) and (V_n) every x-Taylor coefficient of R_Theta and of R_Omega is the zero function of y, which
is (b). Near 0 only the first terms remain: Psi = c0 x + (d0 - beta) x y - A x^3/(3 beta) and Theta = A x^2/2, which
gives the near-origin part of (a). Theta_xx(0, .) = 2 a_1, so J = (-3, 3).
(5) Inverse and defect. U = (-Psi_y, Psi_x) is divergence free with -curl U = Omega and has compact support. Psi has
compact support, so Gamma * Omega = (-Lap Gamma) * Psi = Psi with Gamma(Z) = -(1/(2 pi)) log |Z|; hence U = K * Omega
with K of (A4), and U(0) = (-Psi_y(0), Psi_x(0)) = (0, c0). Since Theta has compact support and div W = 2 beta,
int Theta W.grad Theta dX = -beta int Theta^2 dX, which gives (d).
(6) The ends of J. T = 2 a_1, Omega_x(0, .) = q_0 and D = 24 a_2, and 24 (T_2) is
b D' + (7 beta + 2 - 4 b') D - 8 v_2' T + 12 v_2 T' = 0. Inside J near either end it reads
D_tau + (7 beta + 2 + 8/tau) D = F with F = 8 v_2' T - 12 v_2 T'; there v_2 = -sgn(y) - q_0/2 and
T'/T = -sgn(y)(4 tau + 2 d0 tau^2), so F/T + 24 d0 tau^2 + 48 tau is in E_M. D/T solves
(D/T)_tau + (4 beta + 4/tau) (D/T) = F/T, so tau^{-2} D/T tends to -6 d0/beta, and A I_2 = rho^2 D/T tends to
-infinity.
Scope. For A > 0 (for A < 0 after the reflection of 4.8), the ends -3 and 3 of J are degenerate zeros of b toward
which the axis flow moves from J, and a = T/2 and q = Omega_x(0, .) of 4.13 are positive on J and flat at the ends, as
4.13 (i), (iii) and (v) and 4.42 (a) require of a profile. The fields satisfy every hypothesis of 4.42 except the
simultaneous global equations (T) and (V): both hold near 0 and to every order on the axis, while (T) fails globally;
4.42 (b) and 4.43 concern every J, and here I_2 is not constant on J. By 4.13 (vi), a Theta that is real analytic near
the axis has only simple zeros of b, so the degenerate ends of this J need a Theta that is not real analytic; for beta
irrational, or beta = P/Q in lowest terms with P and Q odd, such a Theta gives J = R. 4.42 (c), 4.44, 4.45, 4.47 (c)
and 4.48 concern infinite ends of J and are not affected. Compact support gives the bounds of (A2) and (A3), but Omega
has no nonzero tail, and Omega is not of one sign on x > 0, since int x Omega dX = -int Psi Lap x dX = 0; so 4.49 does
not bear on exclusions that use a sign or a tail of Omega. 4.30 (beta > 2: (T) on R^2 and every axis coefficient of
R_Omega zero, with J = R) and 4.49 are not comparable; (T) on R^2 together with every axis coefficient of (V) allows a
bounded J by 4.50. No statement about profiles with a bounded J follows from 4.49 beyond the fact that
the axis equations do not exclude them; the existence of a profile is not decided. Checks: exact symbolic checks in
the analysis of the near-origin fields, of (T_n) and (V_n), of the second jet, of the equation for D/T and of the
identity in (d); separate referee audits (A161, VALID WITH FIXES, 36 exact checks, for the ends of J, with its fixes
adopted; A162, correct with editorial fixes, symbolic checks through T_4 and V_3, for the fields and the ends of J,
with its fixes adopted); the verification's own proofs and controls (P273, 65 exact controls; P278, 93 exact controls,
15 scope controls and 25 + 16 supplementary controls; P282, the complete entry, 223 controls, CONFIRMED with two exact
wording corrections 05:32 to 05:35). The letters c0, chi_1, chi_4, chi, b_1, b_*, C, s, tau, a_n, q_n, v_{2j}
(j >= 2), T_n, V_n, E_sigma, sigma, sigma', C_k, N_k, mu, nu, z, g, c_1, eps_j, delta_n, f, eps, l, k, Gamma, F, D,
R_Theta and R_Omega are local to 4.49; e_0 is as in 4.46; Lambda, M, a and q are as in 4.13; g1 is as in 4.29; K is as
in (A4); v_2 is as in 4.44; J, I_2, rho, b, d0, A and T are as in 4.42.
4.50 Exact temperature transport is consistent with a bounded axis component (examples, not profiles). Let beta >= 2,
d0 = 1 + 3 beta/2, A != 0 and c0 real. There are smooth Psi, Theta and Omega on R^2, Psi and Omega odd in x and of
compact support and Theta even in x, with Theta(0, .) = 0 and Omega = -Lap Psi, such that, with U, W, R_Theta and
R_Omega as in 4.49:
  (a) U has compact support, (A4) holds, U is the Biot-Savart velocity K * Omega of (A5) and U(0) = (0, c0); near 0,
      Theta = (A/2) x^2, Omega = (2A/beta) x and W = ((beta - 2) x/2, d0 y - (A/beta) x^2), so (T) and (V) hold on a
      neighbourhood of 0, a0 = A/2 and Psi_xy(0) = 1 + beta/2;
  (b) (T) holds on R^2, that is R_Theta = 0, and d_x^i d_y^j R_Omega vanishes at every point of the axis, for all i,
      j >= 0;
  (c) the x-Taylor coefficients of Theta and of Omega on the axis are those of 4.49 (all zero outside (-3, 3)), and b
      = W_2(0, .) equals that of 4.49 on [-4, 4]; so 4.49 (c) holds: J = (-3, 3), these coefficients are flat at -3
      and 3, D/T = -(6 d0/beta) s^{-2} (1 + o(1)) and A I_2 -> -infinity as |y| -> 3 inside J;
  (d) with X_c = (0, c0/beta), there is r_0 > 0 such that U = 0, W = beta (X - X_c) and Theta(X_c + e^t Y) = e^{(1 -
      2/beta) t} Theta(X_c + Y) for |Y| >= r_0 and t >= 0; so the derivatives of order k of Theta are O(|X|^{1 -
      2/beta - k}), Theta is bounded at beta = 2, (A2) holds with m = 1 - 2/beta and (A3) holds with every delta > 0;
  (e) R_Omega is not identically 0, so (V) fails off the axis, and these fields are not profiles; int x Omega dX = 0,
      so Omega is not of one sign on x > 0.
So (T) on all of R^2, together with the coefficients of (V) of every order on the whole axis, the parities, the center
jet and (A2) to (A4), is consistent with a bounded J at every beta >= 2, and with A I_2 -> -infinity at its finite
ends. An exclusion of profiles with a bounded J needs (V) away from the axis, or a property not implied by the
conditions listed, for example real analyticity near the axis, a sign of Omega or a tail of Omega.
Proof outline. (0) Correction along the flow. Let W be smooth on R^2, of at most linear growth, with bounded
derivatives of every positive order, W_1 odd and W_2 even in x, and let Phi_t be its flow (defined for all real t).
Let Theta_0 be smooth, even in x and of compact support, R_0 = W.grad Theta_0 - (beta - 2) Theta_0, and assume that
every derivative of R_0 vanishes on the axis and that, for some C >= 1 and kappa > 0, |x(Phi_t Z)| >= C^{-1} exp(kappa
t) |x(Z)| for every Z in supp R_0 and t >= 0. Then Theta_1(X) = int_{-infinity}^0 exp(-(beta - 2) t) R_0(Phi_t X) dt
is smooth, even in x and flat on the axis, and W.grad Theta_1 - (beta - 2) Theta_1 = R_0. Indeed, |D^l R_0(Z)| <=
C_{l,N} |x(Z)|^N for all l and N (Taylor's formula in x and compact support), and |D^k Phi_t| <= C_k exp(L_k |t|) for
k >= 1 (variational equations and Gronwall). A derivative of order k of the integrand is nonzero only if Phi_t X is in
supp R_0, and then |x(Phi_t X)| <= C exp(kappa t) |x(X)| for t <= 0 (the hypothesis at Phi_t X for the time -t); so it
is bounded by C_{k,N} |x(X)|^N exp((N kappa - beta + 2 - B_k) t), with B_k independent of N. For N kappa > beta - 2 +
B_k these bounds are integrable on t <= 0, locally uniformly in X, so Theta_1 is smooth, and since N is arbitrary
every derivative of Theta_1 vanishes to every order in x on the axis. Theta_1(Phi_u X) = int_{-infinity}^u exp((beta -
2)(u - t)) R_0(Phi_t X) dt gives the equation at u = 0, and x -> -x commutes with Phi_t and preserves R_0. So Theta =
Theta_0 - Theta_1 satisfies (T) on R^2 and has the axis jets of Theta_0, and replacing Theta_0 by Theta changes
R_Omega by d_x Theta_1, which is flat on the axis.
(1) Exterior drift. Let chi_1 and b_1 be as in 4.49 (0), and extend b_1 from [0, 4] oddly to [-4, 4]. Since chi_1' >=
0 and (y - 3)^2 - d0 y <= 0 on [1, 2], b_1' <= d0 on [-4, 4]; at beta = 2 moreover b_1' <= y - 1 <= 1 on [3/2, 2]
(there chi_1 >= 1/2), b_1' = 2 (y - 3) <= 2 on [2, 4], and 0 <= b_1 - 2y <= 2y on [1, 3/2] (there chi_1 <= 1/2). Let
bbar be smooth and odd, equal to b_1 on [-4, 4] and to beta y outside a compact interval, with sup bbar' < 2 beta if
beta > 2, and with bbar' <= 4 on R and bbar' <= 3 for |y| >= 3/2 if beta = 2: for y >= 4, prescribe bbar' as 2 (y - 3)
on a short interval, then a short smooth transition to the constant slope 3 beta/2 (5/2 at beta = 2), this slope on an
interval, and a short smooth transition to the slope beta; the length of that interval is chosen so that bbar - beta
y, which is negative at 4, vanishes at the end of the last transition. Let eta be smooth and even with values in [0,
1], equal to 1 on a neighbourhood of supp(bbar - beta y) and to 0 far out, with its transition where bbar = beta y and
so wide that |c0 eta'| is below any prescribed bound, and put b = bbar + c0 eta - c0. Then b = b_1 on [-4, 4], as in
4.49, and b = beta y - c0 outside a compact interval.
(2) Coefficients. Steps (1) to (3) of 4.49 apply to this b: J, rho, a_n and q_n are those of 4.49, and so are the
v_{2j} on [-4, 4]; outside J, v_{2j} = (-1)^j b^{(2j)}/(2j)!, which vanishes outside a compact interval since b is
affine there. So all a_n, q_n and v_{2j} are smooth and of compact support, and (T_n) and (V_n) hold on R.
(3) Realization. Let chi_0, chi_c, chi_j and zeta_n (j, n >= 1) be smooth even functions of x with values in [0,
1], equal to 1 near 0 and of compact support, with chi_j(x) = chi(x/eps_j) and zeta_n(x) = chi(x/delta_n) for chi
as in 4.49 (4), and put Psi = (bbar - beta y) x chi_0(x) + c0 eta(y) x chi_c(x) + sum_{j >= 1} v_{2j} x^{2j+1}
chi_j(x)/(2j + 1) and Theta_0 = sum_{n >= 1} a_n x^{2n} zeta_n(x). As in 4.49 (4), eps_j, delta_n -> 0 can be
chosen so that both series converge in every C^k; the term with index j contributes at most C_j eps_j^{2j} to sup
|W_1/x| and to sup |W_2| (W_1/x is the smooth even function equal to W_1/x off the axis), so the eps_j can also be
chosen so that the contributions H_1 and H_2 of all terms with j >= 1 to W_1/x and to W_2 are below any prescribed
bounds. Then W_1/x = beta - (bbar' - beta) chi_0 - c0 eta' chi_c + H_1 and W_2 = beta y + (bbar - beta y)(chi_0 + x
chi_0') + c0 eta (chi_c + x chi_c') - c0 + H_2. Psi_x(0, .) = b - beta y + c0 is the g1 of 4.29, so W_2(0, .) = b,
and as in 4.49 (4) every x-Taylor coefficient of R_0 and of R_Omega (computed with Theta_0) is the zero function of
y; R_0 is even in x and has compact support, and W satisfies the hypotheses of (0) since U has compact support.
(4) Expansion, beta > 2. Let kappa = min(beta, 2 beta - sup bbar')/2 > 0 and take |c0 eta'| <= kappa/2 and
|H_1| <= kappa/2. Since 0 <= chi_0, chi_c <= 1, beta - (bbar' - beta) chi_0 >= 2 kappa, so W_1/x >= kappa on R^2 and
|x(Phi_t Z)| >= exp(kappa t) |x(Z)| for all Z and t >= 0: the hypothesis of (0) holds with C = 1.
(5) Expansion, beta = 2. Fix r_1 > 0 and take chi_0(x) = h_0(1 + log(|x|/r_1)/L) for x != 0, with h_0 smooth,
decreasing, 1 on (-infinity, 0] and 0 on [1, infinity), and L >= 4 sup |h_0'|; so chi_0 = 0 for |x| >= r_1 and
chi_0 + x chi_0' >= -1/4. Take chi_c = 1 on [-r_1, r_1], chi_j supported in [-r_1, r_1], zeta_n supported where
chi_0 = 1, |c0 eta'| <= 1/4, |H_1| <= 1/4 and |H_2| <= 1/4. Then W_1/x >= -1/4 on R^2 (where eta' = 0 since
bbar' <= 4, and where eta' != 0 since bbar' = 2 there), and W_1/x >= 1/2 on G_0 = {|y| >= 3/2} union {|x| >= r_1}
(bbar' <= 3 for |y| >= 3/2, and chi_0 = H_1 = 0 for |x| >= r_1). On the band 1 <= y <= 3/2, |x| <= r_1, eta =
chi_c = 1, so W_2 = 2y + (bbar - 2y)(chi_0 + x chi_0') + H_2 >= 3y/2 - 1/4 >= 5/4 by 0 <= bbar - 2y <= 2y; likewise
W_2 <= -5/4 on the reflected band. On |y| <= 1, bbar' = 4, a_1 = A/2, a_n = 0 (n >= 2), v_2' = 0, v_{2j} = 0 (j >= 2)
and eta' = 0, so Theta_0 = (A/2) x^2 zeta_1(x) and W_1 = 2x (1 - chi_0), and W.grad Theta_0 = 0 there; so R_0 = 0 on
|y| <= 1 and supp R_0 is contained in {|x| <= r_1, 1 <= |y| <= 3}. G_0 is forward invariant (on its boundary the flow
points into G_0), and the trajectory of a Z in supp R_0 outside G_0 crosses its band with |W_2| >= 5/4 toward |y| =
3/2 and enters G_0 within time 1/2. So |x(Phi_t Z)| >= exp(t/2 - 3 min(t, 1/2)/4) |x(Z)| >= exp(-3/8) exp(t/2) |x(Z)|:
the hypothesis of (0) holds with C = exp(3/8) and kappa = 1/2.
(6) Center, inverse and axis data. Put Theta = Theta_0 - Theta_1 and Omega = -Lap Psi. On |y| < 1 only the terms
with chi_0, chi_c, chi_1 and zeta_1 are nonzero, so near 0, as in 4.49 (4), Psi = c0 x + (d0 - beta) x y - A x^3/(3
beta), Theta_0 = A x^2/2 and R_0 = 0. The backward trajectory of a point (x, y) near 0 is (e^{(beta - 2) t/2} x,
e^{d0 t} (y - k_0 x^2) + k_0 e^{(beta - 2) t} x^2), t <= 0, with k_0 = A/(beta (d0 - beta + 2)), as long as it stays
in that neighbourhood, and its components are bounded by |x| and |y| + 2 |k_0| x^2; so it stays there, Theta_1 = 0
near 0, and the near-origin part of (a) follows. The rest of (a) follows as in 4.49 (5), since Psi has compact
support. Theta_1 is flat on the axis, so Theta has the axis jets of Theta_0, which gives (c) as in 4.49 (3), (4) and
(6) and, with (0), (b).
(7) Far field and defect. Take r_0 with supp U contained in the disk |X - X_c| < r_0. Outside it W = beta X - U(0) =
beta (X - X_c), so (T) reads (X - X_c).grad Theta = (1 - 2/beta) Theta there, which gives (d). If (V) held on R^2,
then outside a rectangle containing supp U and supp Omega it would give Theta_x = 0; so Theta = 0 on the lines with
|y| large (Theta(0, .) = 0), and Theta = f_+(y) for large x > 0 and f_-(y) for large -x, with f_+ and f_- of compact
support; there (T) gives (beta y - c0) f_+' = (beta - 2) f_+, so f_+ = 0 on each side of c0/beta, and likewise
f_- = 0. Then Theta would have compact support, and int Theta R_Theta dX = 2 (1 - beta) int Theta^2 dX < 0, as in 4.49
(5), would contradict R_Theta = 0. So R_Omega is not identically 0; by (b) it vanishes on the axis. Finally
int x Omega dX = -int Psi Lap x dX = 0 and Omega_x(0) = 2A/beta != 0, so the odd function Omega is not of one sign on
x > 0.
Scope. The fields satisfy every hypothesis of 4.42 except (V) away from the axis: (T) holds on R^2, (V) holds near 0
and to every order on the axis, and (A2) to (A4) hold. 4.50 strengthens 4.49, whose fields satisfy (T) only near 0 and
to every order on the axis, and establishes the stronger compatibility statement: (T) on R^2 together with every axis
coefficient of (V) allows a bounded J, at every beta >= 2 (for beta > 2, 4.30 gives these properties with J = R).
Theta does not have compact support (by the identity in (7), no nonzero Theta of compact support satisfies (T)). As in
4.49, the degenerate ends of J need a Theta that is not real analytic near the axis (4.13 (vi)), and Omega has compact
support, so no nonzero tail, and is not of one sign on x > 0; so 4.50 does not bear on exclusions that use (V) away
from the axis, real analyticity, a sign of Omega or a tail of Omega. 4.42 (b) and 4.43 concern every J, and here I_2
is not constant on J; 4.42 (c), 4.44, 4.45, 4.47 (c) and 4.48 concern infinite ends of J and are not affected. No
statement about profiles with a bounded J follows from 4.50 beyond the fact that (T) and the axis coefficients of (V)
do not exclude them; the existence of a profile is not decided. Checks: separate referee audits (A162, whose review of
the fields of 4.49 proposed the correction along the flow; A164, valid with clarifications, for the construction at
every beta >= 2, with its clarifications adopted); the verification's own proofs and controls (P283, 55 controls, of
which 45 exact or literal and 10 numerical quadratures of the correction without error bounds, and 15 supplementary
exact controls; P290, 165 controls for the complete entry text). The letters c0, Phi_t, Theta_0, Theta_1, R_0, C,
kappa, Z, C_{l,N}, C_k, L_k, B_k, N, l, k, t, u, bbar, eta, chi_0, chi_c, chi_j, zeta_n, eps_j, delta_n, H_1, H_2,
r_1, h_0, L, G_0, k_0, X_c, r_0, Y, f_+ and f_- are local to 4.50; chi_1, b_1, chi, a_n, q_n, v_{2j}, T_n, V_n, s, D,
R_Theta and R_Omega are as in 4.49; g1 is as in 4.29; K is as in (A4); J, I_2, rho, b, d0, A and T are as in 4.42.
4.51 Finite ends of the axis component at which the axis velocity vanishes to finite order (necessary conditions).
Assume the hypotheses of the first paragraph of 4.42, with J, I_2, A, T, b = W_2(0, .) and d0 as there, and let y_* be
a finite end of J, so that b(y_*) = 0 (4.42 (a)). Suppose that b vanishes to a finite order p >= 2 at y_*, and put s =
|y - y_*|, D = d_x^4 Theta(0, .) and eta = Omega_x(0, .). Then:
  (a) b = sgn(y_*) c_p s^p (1 + O(s)) on J near y_* with c_p > 0, so the axis flow moves from J toward y_*; T, eta and
      D are flat at y_*;
  (b) D/T = -(3 d0/beta) p (p - 1) s^{-2} (1 + o(1)) as y -> y_* in J, and A I_2 -> -infinity there; the coefficient
      depends only on beta and p, not on c_p;
  (c) for every beta > 0 the same conclusions hold for smooth solutions near y_* of the four relations (T_1), (V_0),
      q_0 = -b'' - 2 v_2 and (T_2) of 4.49 (2) (with T = 2 a_1, eta = q_0 and D = 24 a_2) for which b vanishes to the
      order p >= 2 at y_* and T != 0 on one side of y_*, with A any constant such that A/T > 0 on that side, with J in
      (a) and (b) replaced by that side, and with sgn(y_*) in (a) replaced by epsilon when that side is y = y_* -
      epsilon s, epsilon in {-1, 1}; and for every beta > 0, every p >= 2, every c_p > 0 and both sides such local
      solutions exist.
So at such an end the behaviour of I_2 found in 4.49 (c) and 4.50 (c), where p = 2, is forced for every p >= 2, and
the relations used here do not exclude such an end.
Proof outline. (0) By the reflection of 4.8, which maps J to -J and I_2(y) to -I_2(-y) and reverses the sign of A, and
which preserves the four relations, A I_2 and D/T, let y_* > 0, so that y_* = y_+ of 4.42 (a). With y = y_* - s and
B(s) = b(y_* - s), the relations read (primes d/ds in (0) to (3)) B T' = (Lambda + 2 B') T, B eta' = (M + B') eta - T,
v_2 = -(B'' + eta)/2 and the corresponding form of (T_2), with Lambda and M as in 4.13 and Lambda = 2 d0. For (c),
translation and, if needed, reflection give the same reduction to the chosen side y < y_*.
(1) Sign and flatness. T and eta are flat at y_* by the induction of 4.13 (iii) (Lambda, M > 0). The relation (T_2) at
y_*, differentiated n times, gives (7 beta + 2) D^{(n)}(y_*) = 0 once the lower derivatives vanish, since b(y_*) =
b'(y_*) = 0 and its right side 8 v_2' T - 12 v_2 T' is flat; so D is flat. Write B = c_p s^p (1 + O(s)). On J, T != 0
and T = C B^2 exp(Lambda int_{s_0}^s du/B) with C != 0; if c_p < 0 the integral tends to +infinity like
s^{1-p}/(|c_p| (p - 1)) and |T| would be unbounded, so c_p > 0 (for profiles this is also the sign of b
on J, 4.42 (0)).
(2) Ratio equation. Dividing (T_2) by T and using the other three relations, K = D/T satisfies exactly -B K' + (4
beta + 2 B') K = Q on J near y_*, with Q = 4 B''' - 6 B'' (Lambda + 2 B')/B - [(10 beta + 8 + 8 B') eta + 4 T]/B (one
uses 4 M - 6 Lambda = -(10 beta + 8)).
(3) Limit. Put t = int_s^{s_0} du/B, which tends to +infinity as s -> 0 since p >= 2, and Z = s^2 K. Then dZ/dt + (4
beta + 2 B' + 2 B/s) Z = s^2 Q. As s -> 0, s^2 B''/B -> p (p - 1), s^2 B''' -> 0, B' -> 0, B/s -> 0, and s^2 eta/B and
s^2 T/B tend to 0 since eta and T are flat and B vanishes only to the order p, so the coefficient tends to 4 beta and
s^2 Q to -6 Lambda p (p - 1). A solution of dz/dt + alpha(t) z = f(t) with alpha -> alpha_* > 0 and f -> f_* tends to
f_*/alpha_*, so Z -> -6 Lambda p (p - 1)/(4 beta) = -(3 d0/beta) p (p - 1). On J, A/T > 0, and A/T -> +infinity since
T is flat, so A I_2 = (A/T)(D/T) -> -infinity. Steps (1) to (3) use only the four relations, which gives the first
part of (c) for every beta > 0.
(4) Local solutions. Take B = c_p s^p, t = (s^{1-p} - s_0^{1-p})/(c_p (p - 1)), T = C B^2 exp(-Lambda t) with C != 0,
eta = B exp(-M t) [H + C int_0^t B(s(u)) exp(-(Lambda - M) u) du] with H real, v_2 from the curl relation, and K from
the ratio equation of (2) with any value at an interior point; every derivative of T, eta and D = T K tends to 0 as
s -> 0 (exponentials in t times factors polynomial in 1/s). Continue b beyond y_* by the polynomial c_p (y_* - y)^p
and put T = eta = D = 0 and v_2 = -b''/2 there; the four relations hold on both sides and, by continuity, at y_*.
Scope. (a) and (b) are necessary conditions at such an end; they do not exclude a bounded J or a degenerate finite
end, and (c) shows that the four relations allow them; 4.49 and 4.50 realize p = 2 with every axis coefficient of (T)
and (V). Ends at which b has a simple zero, where 4.13 (ii) and (v) apply, and ends at which b vanishes to infinite
order are not covered; at the former I_2 has a limit and the four relations allow every finite and both infinite
limits (4.53), and at the latter the four relations alone force no sign of A I_2 (4.52). By 4.13 (vi), a Theta
that is real analytic near the axis has no degenerate zero of b. 4.42 (c), 4.44, 4.45, 4.47 (c) and 4.48 concern
infinite ends of J. The existence of a profile is not decided. Checks: exact symbolic checks in the analysis of the
ratio equation of (2) and of the limit in (3); a separate referee audit (A166, VALID, 53 exact checks, for the
endpoint law and local solutions, with its precision in step (3) adopted); the verification's own proofs and controls
(P286, 114 exact controls; P292, the complete entry, 152 controls with scope repairs). The letters y_*, epsilon, p, s,
c_p, D, eta, B, C, s_0, n, K, Q, t, Z, z, alpha, alpha_*, f, f_* and H are local to 4.51; Lambda and M are as in 4.13;
T_n, V_n, a_n, q_n and v_2 are as in 4.49; J, I_2, A, T, b and d0 are as in 4.42.
4.52 Ends of the axis component at which the axis velocity vanishes to infinite order: the four axis relations force
no sign (local examples). Let beta > 0 and y_* != 0, let s = |y - y_*| on the side of y_* that contains 0, put
d0 = 1 + 3 beta/2, and let B be one of B_0(s) = exp(-1/s) and B_1(s) = exp(-1/s) (2 + sin(s^{-2})). For every constant
A != 0 there are smooth functions b, T, eta, v_2 and D on a neighbourhood of y_*, all flat at y_* and all zero on the
side of y_* away from 0, that satisfy the four relations (T_1), (V_0), q_0 = -b'' - 2 v_2 and (T_2) of 4.49 (2) (with
T = 2 a_1, eta = q_0 and D = 24 a_2), with b = sgn(y_*) B(s) and A/T > 0 on the side of y_* that contains 0. So b
vanishes to infinite order at y_*, and the axis flow moves toward y_* as in 4.51 (a). On that side K = D/T satisfies
K = -(3 d0/beta) B''(s)/B(s) + o(1) as s -> 0 (primes d/ds), and, with I_2 = D/T^2:
  (a) for B = B_0, K = -(3 d0/beta) (s^{-4} - 2 s^{-3}) + o(1), and A I_2 -> -infinity;
  (b) for B = B_1, K = (4 d0/beta) s^{-6} (1 + o(1)) along s = (pi/2 + 2 pi n)^{-1/2} and K = -(12 d0/beta)
      s^{-6} (1 + o(1)) along s = (3 pi/2 + 2 pi n)^{-1/2}, as n -> infinity; so A I_2 has subsequences tending
      to +infinity and to -infinity.
So, unlike at ends of finite order (4.51), the four relations alone force neither a sign nor a limit of A I_2 at an
end at which b vanishes to infinite order.
Proof outline. (0) By the reflection of 4.8, as in 4.51 (0), let y_* > 0 and y = y_* - s, so that b(y) = B(s) for
y < y_* and the relations take the form of 4.51 (0). Write B = exp(-1/s) h with h = 1 or h = 2 + sin(s^{-2}); then
1 <= h <= 3, and every derivative of h and of 1/h is bounded by a power of 1/s near s = 0.
(1) Time and flatness. Put t = int_s^{s_0} du/B. Comparison with int exp(1/u) du gives c_1 s^2 exp(1/s) <=
t <= c_2 s^2 exp(1/s) for small s, with c_1, c_2 > 0. Every derivative of B is exp(-1/s) times a factor bounded by a
power of 1/s, and every derivative of 1/B, and so every derivative of t of positive order, is exp(1/s) times such a
factor. Hence s^{-N} exp(C'/s) exp(-mu t) -> 0 as s -> 0 for every mu > 0 and all C' and N, and the j-th derivative of
exp(-mu t) is exp(-mu t) times a factor bounded by exp(j/s) times a power of 1/s.
(2) T, eta and v_2. Take T = C B^2 exp(-Lambda t) with A/C > 0, eta = B exp(-M t) [H + C int_0^t B(s(u))
exp(-(Lambda - M) u) du] with H real, and v_2 = -(B'' + eta)/2, as in 4.51 (4). They satisfy the first three
relations. The bracket is bounded since Lambda - M = beta + 1 > 0, and its derivative in s is
-C exp(-(Lambda - M) t); so by (1) T, eta and v_2 are flat at y_*.
(3) Ratio and D. With D = T K, the relation (T_2) is equivalent to the ratio equation of 4.51 (2) for K, whose
derivation does not use the finite order; let K be any solution for y < y_*. Put F = B''/B and c = 3 d0/beta, so that
4 beta c = 6 Lambda, and R = K + c F. Then dR/dt + (4 beta + 2 B') R = H_0 with H_0 = 4 B''' +
(2 c - 12) B' F - c B F' - [(10 beta + 8 + 8 B') eta + 4 T]/B. Every derivative of
F = s^{-4} - 2 s^{-3} + 2 s^{-2} h'/h + h''/h is bounded by a power of 1/s, so the first three terms of H_0 tend to 0;
eta/B and T/B tend to 0 by (1) and (2). Hence H_0 -> 0 and, by the limit lemma of 4.51 (3), R -> 0. Writing the ratio
equation as K' = [(4 beta + 2 B') K - Q]/B, induction gives |K^{(j)}| <= C_j exp(j/s) s^{-N_j}, so D = T K is flat at
y_* by (1). Put b = T = eta = v_2 = D = 0 for y >= y_*; the four relations hold on both sides and, by continuity, at
y_*.
(4) Limits. B_0''/B_0 = s^{-4} - 2 s^{-3}, and, with q = s^{-2}, B_1''/B_1 = s^{-4} - 2 s^{-3} + [-4 s^{-6} sin q +
(6 s^{-4} - 4 s^{-5}) cos q]/(2 + sin q), which is -(4/3) s^{-6} + O(s^{-4}) where sin q = 1 and 4 s^{-6} + O(s^{-4})
where sin q = -1. Since A/T > 0 and T is flat, A/T -> +infinity, and A I_2 = (A/T) K gives (a) and (b).
Scope. These are local solutions of the four relations near one point, not profiles and not asserted to be parts of
profiles: no global inverse, center data or further axis relation is imposed, and b is 0 beyond y_*. They show only
that the law of 4.51 (b) cannot be derived from the four relations at ends of infinite order; whether a profile can
have such an end, and which sign of A I_2 further relations would force there, is not decided. By 4.13 (vi), a Theta
that is real analytic near the axis has no such end. Ends at which b has a simple zero are treated in 4.13 (ii), (v)
and 4.53, not here. The existence of a profile is not decided. Checks: exact symbolic checks in the analysis of H_0,
of B_0''/B_0 and B_1''/B_1, of the two constants in (b) and of the first two relations for T and eta; a separate
referee audit (A165, VALID, 37 exact checks, for the local solutions and their limits); the verification's own proofs
and controls (P289, 51 exact controls; P293, the complete entry, 158 controls with the local scope correction). The
letters y_*, s, s_0, B, B_0, B_1, h, n, D, eta, K, t, c_1, c_2, N, C', mu, j, C, H, F, c, R, H_0, Q, C_j, N_j and q
are local to 4.52 (s, t, K and Q are used as in 4.51); Lambda and M are as in 4.13; v_2, q_0, a_1 and a_2 are as in
4.49; J, I_2, A, T, b and d0 are as in 4.42.
4.53 Ends of the axis component at which the axis velocity has a simple zero (necessary conditions and local
examples). Assume the hypotheses of the first paragraph of 4.42, with J, I_2, A, T, b and d0 as there, let y_* be a
finite end of J at which b has a simple zero, and put s = |y - y_*|, D = d_x^4 Theta(0, .) and eta = Omega_x(0, .).
Then kappa = -b'(y_*) > 0 and T = C s^n (1 + O(s)) on J near y_*, with C != 0 of the sign of A and n = 2 + 2 d0/kappa
an integer (4.13 (i), (ii)). Moreover:
  (a) I_2 has a limit in [-infinity, infinity] as y -> y_* in J: if D vanishes to a finite order j at y_*, then
      s^{2n - j} |I_2| has a finite positive limit, so I_2 tends to 0, to a nonzero real number or to an infinite
      limit according as j > 2n, j = 2n or j < 2n; if D is flat at y_*, I_2 -> 0;
  (b) if b''(y_*) != 0, then D/T = -6 n sgn(y_*) b''(y_*) (4 beta + 3 kappa)^{-1} s^{-1} (1 + o(1)) and A I_2 ->
      -sgn(y_* b''(y_*)) infinity as y -> y_* in J;
  (c) for every beta > 0, the assertion on T before (a), with n = 2 + Lambda/kappa, and conclusions (a) and (b) hold
      for smooth solutions near y_* of the four relations (T_1), (V_0), q_0 = -b'' - 2 v_2 and (T_2) of 4.49 (2) (with
      T = 2 a_1, eta = q_0 and D = 24 a_2) for which b(y_*) = 0, b'(y_*) = -kappa < 0 and T != 0 on one side of y_*,
      with A any constant such that A/T > 0 on that side, with J replaced by that side and sgn(y_*) by epsilon when
      that side is y = y_* - epsilon s, epsilon in {-1, 1};
  (d) let beta = 2 and kappa = 1, which 4.13 (ii) allows (n = 10, and m = 6 in 4.13 (ii)). For each A != 0, each C
      with A/C > 0 and all real H and E, with u = y_* - y, the polynomials b = u, T = C u^10, eta = H u^6 -
      (C/4) u^10, v_2 = -eta/2 and D = E u^20 - (36/5) C H u^15 + 5 C^2 u^19 satisfy the four relations of (c) on R,
      and I_2 = E/C^2 - (36 H/(5 C)) u^{-5} + 5 u^{-1} for u != 0; so, as y -> y_*, A I_2 tends to -sgn(H) infinity
      from below and to sgn(H) infinity from above if H != 0, and to sgn(A) infinity from below and to -sgn(A)
      infinity from above if H = 0. For A, C and H as before and every real ell there are also real analytic solutions
      of the four relations on a neighbourhood of y_* with b'(y_*) = -1, T = C u^10 (1 + O(u)), eta = u^6 (H + O(u)),
      v_2 = 0 and D = ell T^2, so that I_2 = ell for y != y_* near y_*;
  (e) let beta = 2, kappa = 1 and A, C, H and u be as in (d). For every real k != 0 there are real analytic solutions
      of the four relations of (c) on a neighbourhood of y_* with b = u + k u^2 - (C k/260) u^13, T = C u^10
      (1 + O(u)) and eta = u^6 (H + O(u)), for which I_2 = -(120 k/(11 C)) u^{-11} (1 + O(u)) for u != 0; here
      b''(y_*) = 2 k, and A I_2 tends to -sgn(k) infinity as y -> y_* from below and to sgn(k) infinity from above, as
      (b) requires;
  (f) for every beta > 0, every A != 0 and each side of y_* there are real analytic solutions of the four relations of
      (c) near y_* with kappa = Lambda, so that n = 3, with A/T > 0 on that side and with A I_2 tending on that side
      to any prescribed value in [-infinity, infinity]; for them the homogeneous vorticity exponent m = 1 + M/kappa is
      not an integer, while the actual vanishing order of eta is three; eta = -(C/(4 beta + 3)) s^3 (1 + O(s)) on that
      side, where T = C s^3 (1 + O(s)), so that eta has the sign of -A there; so they have neither the integrality of
      4.13 (ii) nor the signs of 4.13 (i).
At a simple end I_2 has an extended real limit; 4.52 includes examples with no such limit. The four relations, even
with the signs that profiles have on J (T and eta of the sign of A, 4.13 (i), so H/A > 0 in (d) and (e)) and the
integrality of 4.13 (ii), allow every finite limit of I_2 and both infinite limits of A I_2 on the side y < y_* of a
point y_* > 0, which is the side occupied by J if y_* is an end of J ((d) and (e)), and by the reflection of 4.8 at an
end y_* < 0; when b''(y_*) != 0, (b) forces A I_2 -> -sgn(y_* b''(y_*)) infinity at an end y_* of J. So the
law of 4.51 (b) cannot be derived from the four relations at simple ends.
Proof outline. (0) By the reflection of 4.8, as in 4.51 (0), let y_* > 0 and y = y_* - s, B(s) = b(y_* - s) = kappa
s + k s^2 + O(s^3) with k = b''(y_*)/2; the relations take the form of 4.51 (0). For (c), translation and, if
needed, reflection give the same reduction. kappa > 0 since b > 0 on J near y_* (4.42 (0)) and the zero is simple.
(1) Finite order of T and the limit. Write B = s a(s) with a smooth, a(0) = kappa. Then T'/T = (Lambda + 2 B')/B =
n/s + G'(s) with G smooth, so T = C_0 s^n exp(G); T is therefore not flat, a smooth function with this one-sided
asymptotic vanishes to the finite order n, so n is an integer, and T = C s^n tau with tau smooth, tau(0) = 1. A
smooth D is flat or D = d_j s^j (1 + o(1)), d_j != 0, at a finite order j; in the first case D = o(s^{2n}) and
I_2 -> 0, in the second I_2 = (d_j/C^2) s^{j - 2n} (1 + o(1)). No further relation is used, which gives (a) in (c).
(2) Curvature law. (V_0) at y_* gives (M + kappa) eta(y_*) = T(y_*) = 0. K = D/T satisfies the ratio equation of 4.51
(2), -B K' + (4 beta + 2 B') K = Q, whose derivation does not use the finite order. By Taylor's theorem s Q -> -12 k
(Lambda + 2 kappa)/kappa = -12 k n, the terms with eta and T tending to 0 since eta(y_*) = T(y_*) = 0. Put
t = int_s^{s_0} du/B, which tends to +infinity, and Z = s K. Then dZ/dt + (4 beta + 2 B' + B/s) Z = s Q, the
coefficient tends to 4 beta + 3 kappa > 0, and the limit lemma of 4.51 (3) gives Z -> -12 k n/(4 beta + 3 kappa). With
A/T -> +infinity this gives (b), and, undoing the reflection, sgn(y_*) b''(y_*) in place of b''(y_*).
(3) The polynomials. At beta = 2, Lambda = 8, M = 5 and 7 beta + 2 = 16. With ' = d/dy, b = u and b' = -1, (T_1) reads
u T' + 10 T = 0, (V_0) reads u eta' + 6 eta = T, the curl relation gives v_2 = -eta/2 since b'' = 0, and (T_2) reads
u D' + 20 D = 8 v_2' T - 12 v_2 T' = -4 eta' T + 6 eta T'; direct differentiation verifies all four.
(4) The analytic solutions. With s = u = y_* - y as a signed variable and primes d/ds, seek B = s (1 + x), b = B, T =
s^10 g, eta = s^6 h with x(0) = z(0) = 0, h(0) = H, g(0) = C, and s x' = z - x, s z' = -s^7 h, (1 + x) s h' =
(z - 6 x) h - s^4 g, (1 + x) s g' = (2 z - 10 x) g. Then B' = 1 + z, B'' = -eta (the curl relation with v_2 = 0), and
the last two equations are (V_0) and (T_1). For D = ell T^2 and v_2 = 0, (T_2) reduces to ell T^2 (7 beta + 2 - 2
Lambda) = (beta - 2) ell T^2 = 0. The system has the form s X' = A_0 X + R(s, X) for X = (x, z, h - H, g - C), with
A_0 of eigenvalues -1, 0, 0, 0, R analytic, R(s, 0) = O(s^4) and D_X R = O(|s| + |X|); then ||r^{-A_0}|| <= C_1 (1 +
|log r|^q) on (0, 1], and X = int_0^1 r^{-A_0} R(r s, X(r s)) dr/r is a contraction on analytic functions on a small
disc with the norm sup |X(s)|/|s|; its fixed point is real and solves the system.
(5) The solutions of (e). With u as a signed variable and primes d/du, let B = u + k u^2 + c_13 u^13 and b = B. Since
(8 + 2 B')/B - 10/u and (5 + B')/B - 6/u are analytic at 0, T = C u^10 exp(F_1) and Y = u^6 exp(F_2), with F_1 and F_2
their primitives vanishing at 0, are analytic; with eta = Y (H - F_3), F_3 the primitive vanishing at 0 of T/(B Y) =
O(u^3), and v_2 = -(eta + B'')/2, the relations (T_1), (V_0) and the curl relation hold. At beta = 2, 7 beta + 2 = 2
Lambda, so for D = T^2 I_2 the relation (T_2) is equivalent to B T^2 I_2' = 6 (B'' + eta) T' - 4 (B''' + eta') T. The
right side divided by B T^2 is meromorphic at 0, equal to (120 k/C) u^{-12} (1 + O(u)), and its residue is 48 k/5 +
2496 c_13/C (exact series computation), which vanishes for c_13 = -C k/260. It then has a meromorphic primitive I_2 =
-(120 k/(11 C)) u^{-11} (1 + O(u)), and D = T^2 I_2 is analytic since T^2 = C^2 u^20 (1 + O(u)). For c_13 = 0 the
nonzero residue 48 k/5 would force a term u^20 log|u| in D.
(6) The solutions of (f), constructed in the verification. With epsilon and s as in (c) (s a signed variable), sigma
in {0, 1} and ell real, seek B = s (Lambda + x), b = epsilon B, T = s^3 g, eta = s^3 h, v_2 = s^{4 - sigma} w and D =
ell s^{6 - sigma} g^2, so that I_2 = ell s^{-sigma}. With B' = Lambda + z the four relations become a singular
analytic system s X' = A_0 X + R(s, X) for X = (z, x, g - C, h + C/(4 beta + 3), w - w_0), w_0 = epsilon ell C (beta -
2 + sigma Lambda)/(4 (1 + 2 sigma)), with A_0 lower triangular of diagonal 0, -1, 0, -(4 beta + 3)/Lambda, (1 + 2
sigma)/2, R(s, 0) = O(s^4) and D_X R = O(|s| + |X|); a contraction as in (4), with ||r^{-A_0}|| <= C_1 r^{-(1 + 2
sigma)/2} (1 + |log r|) and the norm sup |X(s)|/|s|^2, has a real analytic fixed point. sigma = 0 with ell = R/A gives
the finite limit R of A I_2, and sigma = 1 with A ell of the sign of the desired infinity gives the infinite limits;
M/Lambda lies in (0, 1).
Scope. (a), (b) and the assertion on kappa and T before (a) are necessary conditions at a simple end of J; (d), (e)
and (f) consist of local solutions of the four relations near one point, not profiles and not asserted to be parts of
profiles: no global inverse, center data or further axis relation is imposed. At beta = 2, the local examples in (d)
and (e), with H/A > 0, have T and eta of the sign of A and the admissible exponents n = 10 and m = 6; they attain
every finite limit of I_2 and both infinite limits of A I_2 from the side y < y_* of a point y_* > 0, the side
occupied by J at a positive end of J. For every beta > 0, (f) attains every extended-real limit of A I_2, with eta of
the sign of -A and without the integrality requirement on m. Thus the four relations alone do not universally force
divergence or a fixed sign. When b''(y_*) != 0, however, (b) and (c) force A I_2 -> -sgn(epsilon b''(y_*)) infinity on
the side y = y_* - epsilon s, s > 0; at an end y_* of J, epsilon = sgn(y_*). Whether a profile can have a simple
finite end, and which limits further relations would force, is not decided; for the next vorticity relation see 4.54.
With 4.51 and 4.52, every finite end of J is now treated: the order of the zero of b there is 1, finite and at least
2, or infinite. 4.42 (c), 4.44, 4.45,
4.47 (c) and 4.48 concern infinite ends of J. The existence of a profile is not decided. Checks: exact symbolic checks
of the ratio equation, of the limit in (2), of the polynomials of (3) on both sides, of the reductions in (4) and of
the series and the residue in (5); a separate referee audit (A167, VALID, and A169, VALID with the scope corrections);
the verification's own proofs and controls (P296, 147 controls; P299, 318 controls; P303, 131 controls; P304, complete
entry, 167 controls with seven wording corrections). The letters y_*, s, s_0, kappa, C, C_0, n, m, epsilon, j, d_j, k,
B, a, G, tau, K, Q, t, Z, H, E, ell, x, z, h, g, u, X, A_0, R, r, q, C_1, c_13, F_1, F_2, F_3, Y, sigma, w and w_0 are
local to 4.53 (s, t, K and Q are used as in 4.51); D and eta are as in 4.51; Lambda and M are as in 4.13; v_2, q_0,
a_1, a_2, (T_1), (V_0) and (T_2) are as in 4.49; J, I_2, A, T, b and d0 are as in 4.42.
4.54 The next vorticity relation at a simple end of the axis component (local examples, beta = 2). Let beta = 2,
kappa = 1, and let y_*, u = y_* - y, A, C and H be as in 4.53 (d), so that n = 10 and m = 6 in 4.13 (ii). Put gamma =
d_x^3 Omega(0, .) = 6 q_1. The relation (V_n) of 4.49 (2) with n = 1, multiplied by 6, reads at beta = 2
  (V_1) b gamma' + (13 - 3 b') gamma = D + 2 v_2' eta - 6 v_2 eta',
with D = 24 a_2 and eta = q_0 as in 4.53. The five relations are the four relations of 4.53 (c) and (V_1). Then:
  (a) for every real k with C k != 0, let b = u + k u^2 - (C k/260) u^13 and T, eta, v_2 and D be as in 4.53 (e), with
      D = T^2 I_2 for any primitive I_2 (so D is fixed up to adding ell T^2, ell real). Then (V_1) has a solution
      gamma that is smooth on a neighbourhood of y_* if and only if H = -k^7/231; otherwise no solution of (V_1) on a
      one-sided neighbourhood of y_* is of class C^16 up to y_*. With H/A > 0 and C/A > 0, the signs that profiles
      have on J (4.13 (i)), H = -k^7/231 holds only if A k < 0, and then I_2 tends to +infinity as y -> y_* from
      below, so A I_2 tends to sgn(A) infinity there;
  (b) for every real k != 0 let c_9 = k (231 H + k^7)/6930 and c_13 = -C k/260 - 2642 c_9 k^4/6435. There are real
      analytic solutions of the five relations on a neighbourhood of y_* with b = u + k u^2 + c_9 u^9 + c_13 u^13,
      T = C u^10 (1 + O(u)), eta = u^6 (H + O(u)), D = -(120 C k/11) u^9 (1 + O(u)) and gamma = O(u^5), for which
      I_2 = -(120 k/(11 C)) u^{-11} (1 + O(u)) for u != 0; here b''(y_*) = 2 k, and A I_2 tends to -sgn(k) infinity as
      y -> y_* from below and to sgn(k) infinity from above, for either sign of k and all A, C and H with A/C > 0 and
      H/A > 0;
  (c) the polynomials of 4.53 (d) satisfy (V_1) with the polynomial gamma = -(12/5) H^2 u^11 + (4/5) C H u^15 +
      F u^16 - (5/4) C^2 u^19 - (E/4) u^20 for every real F, and the real analytic solutions of 4.53 (d) with v_2 = 0
      and D = ell T^2 satisfy (V_1) with a real analytic gamma = O(u^16).
So at beta = 2 the five relations, even with the signs that profiles have on J and the integrality of 4.13 (ii), allow
every finite limit of I_2 ((c)) and both infinite limits of A I_2 ((b)) at an end y_* > 0, below which J lies, and by
the reflection of 4.8 at an end y_* < 0. The sign restriction in (a) is a property of the family of 4.53 (e), not of
the five relations. With the analytic data entering the inhomogeneous term fixed, each further scalar relation of 4.49
(2), (T_n) with n >= 3 or (V_n) with n >= 2, has at a simple end with beta = 2 and kappa = 1 a homogeneous part with
the integer indicial exponent 10 n or 10 n + 6. Analyticity at that order may therefore impose one scalar residue
condition of the kind in (a); this makes no assertion that these conditions are independent or cannot be removed by
free data, or that the transverse series converges (in the family of (a) all further conditions beyond H = -k^7/231
can be met by a choice of the free constants, 4.55 and 4.56; convergence is not decided).
Proof outline. (0) The relation. (V_n) of 4.49 (2) with n = 1 is b q_1' + (6 beta + 1 - 3 b') q_1 = 4 a_2 + v_2'
q_0/3 - v_2 q_0'; multiplying by 6 and putting beta = 2 gives (V_1). With u as a signed variable, primes d/du and
B(u) = b(y_* - u), (V_1) reads -B gamma' + (13 + 3 B') gamma = D - 2 v_2' eta + 6 v_2 eta'. The homogeneous parts of
(T_n) and (V_n) read -B f' + [(4 n - 1) beta + 2 + 2 n B'] f = 0 and -B f' + [(4 n + 2) beta + 1 + (2 n + 1) B']
f = 0, with indicial exponents 10 n and 10 n + 6 at beta = 2 and B'(0) = 1.
(1) Residue criterion. Let B = u (1 + O(u)) be analytic and let the right side R of (V_1) be analytic at 0. Since
(13 + 3 B')/B - 16/u is analytic at 0, Z = u^16 exp(F_4), with F_4 its primitive vanishing at 0, is an analytic
solution of the homogeneous equation, Z = u^16 (1 + O(u)); the value of r below refers to this normalization of Z,
whether r vanishes does not depend on it. With gamma = Z w, (V_1) becomes w' = g := -R/(B Z), which is meromorphic at
0 with a pole of order at most 17; let r be its residue. If r = 0, g has a meromorphic primitive w_0 with a pole of
order at most 16, and gamma = Z (w_0 + const) is analytic for every constant. If r != 0, every solution on a one-sided
neighbourhood of 0 is Z (w_0 + r log|u| + const) with w_0 meromorphic; the terms other than r Z log|u| are analytic,
and the 16th derivative of r Z log|u| = r u^16 (1 + O(u)) log|u| is unbounded, so the solution is not of class C^16 up
to 0. Replacing D by D + ell T^2 changes g by -ell T^2/(B Z) = O(u^3), which has no residue, so r does not depend on
ell.
(2) The residues. For B = u + k u^2 + c u^9 + a u^13 with real k, c and a, let T, eta and v_2 be as in 4.53 (5), which
uses only that B = u (1 + O(u)) is analytic, so that (T_1), (V_0) and the curl relation hold. As in 4.53 (5), for D =
T^2 I_2 the relation (T_2) is equivalent to I_2' = G with G meromorphic at 0, and exact series computation gives the
residue of G as rho = 16 (99 C k + 25740 a + 10568 c k^4)/(165 C); so (T_2) has an analytic solution D if and only if
rho = 0. Let I_0 be the meromorphic function with I_0' = G - rho/u and zero constant term; D_0 = T^2 I_0 is analytic.
With D_0 in place of D the right side of (V_1) is analytic, g of (1) is meromorphic, and exact series computation
gives its residue as r = (-1386 C H k + 187110 C c - 27 C k^8 + 1261260 H a + 517832 H c k^4)/1155. Where rho = 0, D_0
solves (T_2) and r is the residue of (1); where rho != 0, the solutions of (T_2) are T^2 (I_0 + rho log|u| + const),
and r is only the coefficient of u^{-1} in the part of g without logarithm. For c = 0 and a = -C k/260, the family of
4.53 (e), rho = 0 and r = -9 C k (231 H + k^7)/385, which with (1) gives the first assertion of (a). Where rho = 0, r
= C (187110 c - 6237 H k - 27 k^8)/1155, which vanishes for c = c_9; a = c_13 gives rho = 0 for c = c_9, and (1) gives
(b). The leading terms of I_2 and D are those of 4.53 (5), since the term c_9 u^9 of B does not enter them, and the
coefficient of u^5 in (V_1) gives gamma = -(36 k H/11) u^5 + O(u^6).
(3) Signs. In (a), H = -k^7/231 and H/A > 0 give A k^7 < 0, so A k < 0; since C/A > 0, k/C < 0, and
I_2 = -(120 k/(11 C)) u^{-11} (1 + O(u)) tends to +infinity as u -> 0 from above, which is y -> y_* from below. In
(b), A I_2 = -(120/11) (A/C) k u^{-11} (1 + O(u)) has the sign of -k for small u > 0 and of k for small u < 0, and c_9
and c_13 are defined for either sign of k.
(4) The examples of (c). For the polynomials of 4.53 (d), b = u, b'' = 0 and v_2 = -eta/2, so the right side of (V_1)
is D + 2 eta eta' with ' = d/dy, and direct differentiation verifies (V_1) for the stated gamma; u^16 solves the
homogeneous equation. For the analytic solutions of 4.53 (d), v_2 = 0, so the right side of (V_1) is ell T^2 = O(u^20)
and g = O(u^3) in (1); its primitive is analytic and gamma = Z (w_0 + const) = O(u^16).
Scope. (a) concerns one explicit family; (b) and (c) consist of local solutions of the five relations near one point,
not profiles and not asserted to be parts of profiles: no global inverse, center data or further axis relation is
imposed. They show only that the five relations at beta = 2, with the signs and integrality of 4.13 (i), (ii), force
neither an infinite limit of I_2 at a simple end nor the sign of A I_2 there, except through the sign of b''(y_*) in
4.53 (b). Whether the further relations of 4.49 (2), or a profile, force any additional restriction on the attainable
limit or its sign at a simple end is not decided (for the further relations in the family of (a) see 4.55 and 4.56),
and the existence of a profile is not decided. Checks: exact symbolic series computation of both residues of (2) for
B = u + k u^2 + c u^p + a u^13 with p = 3 to 13 (for p = 10 to 13 the terms in c drop out of r where rho = 0, for p =
3 to 9 they do not); an independent exact rational check of (b) by undetermined coefficients for eleven parameter
triples (ten with k != 0, with both signs of k and of C, and one with k = 0), with the control that a shift of c_9 by
1/1000 leaves the defect of (V_1) at u^16 equal to 162 C/1000, as the formula for r predicts; an exact symbolic check
of the polynomials in (c); a separate referee audit (A170, VALID with three corrections: the sign of A I_2 in (a), the
normalization of Z and the meaning of r where rho != 0); the verification's own proofs and controls (P306, 594
controls; P311, 739 controls; P312, complete entry, 242 controls and three wording corrections). The letters k, c, a,
p, c_9, c_13, B, f, F, F_4, R, Z, w, w_0, g, r, G, rho, I_0 and D_0 are local to 4.54; y_*, u, kappa, n, m, A, C, H, E
and ell are as in 4.53 (d); D and eta are as in 4.51; v_2, q_0, q_1, a_2, (T_n), (V_n), (T_1), (V_0) and (T_2) are as
in 4.49; J, I_2, T and b are as in 4.42.
4.55 Two further axis relations in the family of 4.54 (a) (local, beta = 2). Let beta = 2, kappa = 1, let y_*, u, A,
C and H be as in 4.53 (d), and for real k with C k != 0 let b, T, eta, v_2, D and gamma be as in 4.54 (a) with
H = -k^7/231. The real analytic solutions D of (T_2) and gamma of (V_1) then form a two-parameter family: D is fixed
up to adding ell T^2, and for each D, gamma is fixed up to adding mu Z, with ell and mu real and Z as in 4.54 (1).
Put a_1 = T/2, a_2 = D/24, q_0 = eta, q_1 = gamma/6 and v_4 = -(q_1 + v_2''/3)/4, the curl relation of 4.49 (2) with
n = 1. For the coefficients a_3 of x^6 in Theta and q_2 of x^5 in Omega on the axis, the relations (T_n) of 4.49 (2)
with n = 3 and (V_n) with n = 2 read at beta = 2
  (T_3) b a_3' + (24 - 6 b') a_3 = (4/3) v_2' a_2 - v_2 a_2' + (2/5) v_4' a_1 - v_4 a_1',
  (V_2) b q_2' + (21 - 5 b') q_2 = 6 a_3 + v_2' q_1 - v_2 q_1' + (1/5) v_4' q_0 - v_4 q_0'.
Then exactly one pair (D, gamma) of the family has the property that (T_3) has a solution a_3 and (V_2) has a solution
q_2 which are smooth on a neighbourhood of y_*. For that pair every such a_3 and q_2 is real analytic, a_3 is fixed up
to adding a multiple of T^3, and for each a_3, q_2 is fixed up to adding a multiple of a solution u^26 (1 + O(u)) of
the homogeneous part of (V_2). For every other pair of the family, either no solution of (T_3) on a one-sided
neighbourhood of y_* is of class C^30 up to y_*, or (T_3) has smooth solutions and for none of them has (V_2) a
solution on a one-sided neighbourhood of y_* that is of class C^26 up to y_*. So in this family (T_3) and (V_2), whose
homogeneous parts have the exponents 30 and 26, impose no further condition on b, T and eta; they fix the two free
constants of D and gamma.
Proof outline. (0) Form of the relations. With u as a signed variable, primes d/du and B(u) = b(y_* - u) as in 4.54
(0), (T_3) and (V_2) take the form -B f' + (alpha + c B') f = R with (alpha, c) = (24, 6) and (21, 5), where R is the
right side with each derivative replaced by minus the u-derivative. Let t and Y be the analytic solutions u^10
(1 + O(u)) and u^6 (1 + O(u)) of the homogeneous parts -B f' + (8 + 2 B') f = 0 of (T_1) and -B f' + (5 + B') f = 0 of
(V_0). Then T = C t and Z = t Y, and t^3 and t^2 Y, with logarithmic derivatives (24 + 6 B')/B and (21 + 5 B')/B,
solve the homogeneous parts of (T_3) and (V_2).
(1) Residues. As in 4.54 (1) with t^3 and t^2 Y in place of Z, (T_3) has a smooth solution if and only if the residue
r_3 at 0 of the meromorphic function -R/(B t^3) vanishes; its smooth solutions are then analytic and differ by
multiples of t^3, and if r_3 != 0 every solution on a one-sided neighbourhood of 0 is an analytic function plus r_3
t^3 log|u| and is not of class C^30 up to 0. For an analytic a_3 the same holds for (V_2) with the residue r_2 of
-R/(B t^2 Y), t^2 Y and 26. Adding a multiple of t^3 to a_3 changes -R/(B t^2 Y) by a multiple of t/(B Y) = O(u^3), so
r_2 does not depend on that multiple. Where r_3 != 0, r_2 is defined in the same way with t^3 w_0 in place of a_3,
where w_0 is the meromorphic primitive of -R/(B t^3) - r_3/u with zero constant term: only the coefficients of a_3
through u^26 enter r_2, since B t^2 Y vanishes to order 27, and the solutions of (T_3) differ from t^3 w_0 by r_3
t^3 log|u| plus a multiple of t^3; where r_3 = 0, t^3 w_0 is one of the analytic solutions.
(2) The dependence on the free constants. Let G be the primitive of t/(B Y) vanishing at 0, so that eta = Y (H - C G)
and t^2/(B Z) = G'. Let D_* and gamma_* be the members of the family given by primitives with zero constant term in
their Laurent series, and write D = D_* + 24 E t^2 and q_1 = gamma_*/6 - 4 E Z G + F_1 Z with real E and F_1; by
variation of constants in (V_1) these are all members of the family, and E differs from C^2 ell/24 by a constant.
Every term of the right sides of (T_3) and (V_2) contains at most one of a_2, q_1, v_4, a_3 and q_2 and otherwise
fixed data, so r_3 and r_2 are affine in (E, F_1), and their coefficients are residues formed from the
variations E t^2 of a_2 and -4 E Z G + F_1 Z of q_1 and from b, t, Y, eta and v_2. These coefficients were computed
with B = u + k u^2 + a u^13 for general real C, k, H and a; then t = u^10 (1 + k u)^{-6} (1 + O(u^12)), Y = u^6
(1 + k u)^{-4} (1 + O(u^12)) and G = sum_{i=4}^{15} (-1)^i binom(i - 2, 2) k^{i - 4} u^i/i + O(u^16), and the
integrands for these coefficient variations have poles of order at most 12, which relative corrections of order u^12
do not change, so the term a u^13 enters them only through B'' and B'''. The result: r_3 does not depend on F_1 and
its coefficient of E is 416 a + (52/25) C k; the coefficient of F_1 in r_2 is 390 a + (21/20) C k; the coefficient of
E in r_2 is -(6/385) k^8 - (63/25) H k. For a = -C k/260 and H = -k^7/231 these are 12 C k/25, -9 C k/20 and
-9 k^8/1925, and the determinant of the coefficient matrix is -27 C^2 k^2/125. So r_3 = 0 fixes E, then r_2 = 0 fixes
F_1, and (1) gives the assertion.
Scope. 4.55 concerns one explicit family and the relations up to (T_3) and (V_2); its solutions are local solutions of
axis relations near one point, not profiles and not asserted to be parts of profiles, and no solution of (T) and (V)
on a neighbourhood of a point is constructed. The sign restriction A k < 0 of 4.54 (a), under the sign conditions
stated there, is unchanged, since the free constants do not enter b, T and eta. The relations (T_n) with n >= 4 and
(V_n) with n >= 3 can also be met in this family, by a unique choice of further free constants (4.56); which
restrictions the relations of 4.49 (2) impose at other simple ends and the existence of a profile are not decided by
4.55. Checks: the verification's general-parameter proof by residue integration, with exact controls (P308, 256 exact
and 23 symbolic controls; P320, adjudication of the audit, 34 controls; P319, complete entry, 129 controls); a
separate referee audit in exact arithmetic over the rationals in C, k, H and a (A171, VALID, with one intermediate
display corrected in its adjudication (P320)); an independent implementation in the analysis of (T_n), (V_n) and the curl
relation of 4.49 (2) in exact rational Laurent series for six pairs (C, k) with both signs of C and of k, which gives,
for a = -C k/260 and H = -k^7/231, the three coefficients above (computed in ell and mu and converted), the
independence of r_3 from F_1, the affine dependence at a further pair of constants, and r_3 = r_2 = 0 at the computed
pair. The letters alpha, c, f, R, t, Y, G, r_3, r_2, w_0, D_*, gamma_*, E, F_1, a, i and mu are local to 4.55; y_*, u,
kappa, A, C, H and ell are as in 4.53 (d); k, B and Z are as in 4.54; D and eta are as in 4.51; v_2, v_4, q_0, q_1,
q_2, a_1, a_2, a_3, (T_n), (V_n), (T_1), (V_0) and (T_2) are as in 4.49; T and b are as in 4.42.
4.56 The axis relations of every order in the family of 4.54 (a) (local, formal in x, beta = 2). Let beta = 2,
kappa = 1, let y_*, u, A, C and H be as in 4.53 (d), and for real k with C k != 0 let b, T, eta, v_2, D and gamma be
as in 4.54 (a) with H = -k^7/231, so that (T_1), (V_0) and the curl relation of 4.49 (2) with n = 0 hold for a_1 = T/2
and q_0 = eta. Then there is exactly one sequence of germs at y_* of smooth functions a_n (n >= 2), q_n (n >= 1) and
v_{2n} (n >= 2) such that the relations (T_n) of 4.49 (2) for n >= 2, (V_n) for n >= 1 and the curl relation
q_n = -v_{2n}''/(2n + 1) - (2n + 2) v_{2n+2} for n >= 1 hold near y_*. All these germs, and T, eta and v_2, have real
analytic representatives on the one interval |y - y_*| < R_* with R_* = min(1, 1/(4 |k|), (65/|C k|)^{1/12}), the same
for all n, on which the relations hold; a_2 = D/24 and q_1 = gamma/6 for the pair (D, gamma) of 4.55. Hence, with
these coefficients, the formal series Theta, Omega, W_1 and W_2 of 4.49 (2) satisfy R_Theta = 0, R_Omega = 0 and
Omega = d_y W_1 - d_x W_2 at every order in x: the coefficient of each power of x vanishes on |y - y_*| < R_*. So in
this family the axis relations of 4.49 (2) of every order impose no condition beyond H = -k^7/231 (4.54 (a)); at each
order n >= 2 they fix the two free constants of a_n and q_{n-1}.
Proof outline. (0) Residues. With u, B, t, Y and G as in 4.55 (0) and (2), the homogeneous parts of (T_n) and (V_n) at
beta = 2 read -B f' + (8 n + 2 n B') f = 0 and -B f' + (8 n + 5 + (2 n + 1) B') f = 0; since n (8 + 2 B') =
8 n + 2 n B' and n (8 + 2 B') + 5 + B' = 8 n + 5 + (2 n + 1) B', they are solved by t^n and t^n Y, which vanish to the
orders 10 n and 10 n + 6. Let n >= 2 and let the data of (T_{n+1}) and (V_n) other than a_{n+1} be analytic. As in
4.55 (1), (T_{n+1}) has a smooth solution if and only if the residue r_n at 0 of -R/(B t^{n+1}) vanishes, R its right
side in the form of 4.55 (0); its smooth solutions are then analytic and differ by multiples of t^{n+1}, and if r_n !=
0 no solution on a one-sided neighbourhood of 0 is of class C^{10n+10} up to 0. For an analytic a_{n+1} the same holds
for (V_n) with the residue s_n of -R/(B t^n Y), t^n Y and the class C^{10n+6}. Adding a multiple of t^{n+1} to a_{n+1}
changes -R/(B t^n Y) by a multiple of t/(B Y) = O(u^3), so s_n does not depend on that multiple. Where r_n != 0, s_n
is defined with t^{n+1} w_n in place of a_{n+1}, w_n the meromorphic primitive of -R/(B t^{n+1}) - r_n/u with zero
constant term; only the coefficients of a_{n+1} through u^{10n+6} enter s_n, since B t^n Y vanishes to order 10 n + 7,
and the term r_n t^{n+1} log|u| begins at order 10 n + 10. For n = 2, r_n and s_n are r_3 and r_2 of 4.55 (1).
(1) The free constants. Let n >= 2, let a_1, ..., a_{n-1}, q_0, ..., q_{n-2} and v_2, ..., v_{2n-2} be analytic near 0
and satisfy (T_1) to (T_{n-1}), (V_0) to (V_{n-2}) and the curl relations up to the one that gives v_{2n-2}, and let
(T_n) and (V_{n-1}) have analytic solutions. These are a_n = a_n^* + E_n t^n and, for each E_n, q_{n-1} =
q_{n-1}^* - 2 n E_n t^{n-1} Y G + F_n t^{n-1} Y with real E_n and F_n, where a_n^* and q_{n-1}^* are given by
primitives with zero constant term in their Laurent series: a_n enters (V_{n-1}) only through 2 n a_n, and
t^n/(B t^{n-1} Y) = G'. With v_{2n} = -(q_{n-1} + v_{2n-2}''/(2n - 1))/(2n), the right side of (T_{n+1}) contains a_n
only in its term with j = 1 and v_{2n} only in its term with j = n, multiplied by v_2 and by a_1, and the right side
of (V_n) contains a_{n+1} once, q_{n-1} only in its term with j = 1 and v_{2n} only in its term with j = n, multiplied
by v_2 and by q_0; since n >= 2 these terms are distinct, so r_n and s_n are affine in (E_n, F_n).
(2) The coefficients. The coefficients of r_n and s_n in (E_n, F_n) were computed, for every n >= 2, as in 4.55 (2)
with B = u + k u^2 + a u^13 and general real a and H: the integrands for the coefficient variations have poles of
order at most 12 for every n, so the relative corrections of order u^12 in t, Y and G do not change them, and the
term a u^13 enters only through B'' and B'''. The result: r_n does not depend on F_n and its coefficient of E_n is
208 n a + (12/5) (n/3 + 1/(2 n + 1)) C k; the coefficient of F_n in s_n is (208 n - 26) a +
((n + 1) (8 n - 9)/(10 n)) C k; the coefficient of E_n in s_n is -(3 n/385) k^8 -
(3 (n + 1) (6 n - 5)/(5 (2 n + 1))) H k. For a = -C k/260 and H = -k^7/231 these are 12 C k/(5 (2 n + 1)),
-9 C k/(10 n) and -(2 n + 5) k^8/(385 (2 n + 1)), for n = 2 those of 4.55 (2), and the determinant of the coefficient
matrix is -54 C^2 k^2/(25 n (2 n + 1)) != 0. So r_n = 0 fixes E_n, and then s_n = 0 fixes F_n.
(3) Induction. For n = 2 the hypothesis of (1) holds by 4.53 (e) and 4.54 (a), and E_2, F_2 are E, F_1 of 4.55 (2),
with a_2^* = D_*/24 and q_1^* = gamma_*/6. If E_n and F_n are fixed by (2), then by (0) (T_{n+1}) and (V_n) have
analytic solutions, and with a_n, q_{n-1} and v_{2n} so fixed the hypothesis of (1) holds with n + 1 in place of n.
Each step fixes a_n, q_{n-1} and v_{2n} and changes no germ fixed before; this gives the sequence. Conversely, in any
sequence as in the statement each a_n and q_{n-1} is analytic and of the form in (1), by (0) applied one order lower,
and smooth solutions of (T_{n+1}) and (V_n) exist only for the values of E_n and F_n fixed by (2); v_{2n} is given by
the curl relation. This gives the uniqueness, and the assertions on the formal series follow from 4.49 (2) and (4).
(4) A common interval. For complex u with |u| < R_*, |B/u - 1| <= |k| |u| + |C k| |u|^12/260 < 1/4 + 1/4, so u = 0 is
the only zero of B there, and t u^{-10} and Y u^{-6} are the exponentials of the primitives vanishing at 0 of
(-6 k - (4 C k/65) u^11) u/B and (-4 k - (7 C k/260) u^11) u/B; so t, Y, t/(B Y), G, T = C t, eta = Y (H - C G) and
v_2 are holomorphic on the disk |u| < R_*. If R is holomorphic on that disk and z is t^m or t^m Y with m >= 1, then
R/(B z) is holomorphic on the punctured disk with a pole at 0 of order at most the order of z plus 1; if its residue
vanishes, its primitive with zero constant term is single valued there with a pole of order at most the order of z,
and z times it extends holomorphically to the disk. This applies to the solutions in (0) and (1); since derivatives
and products of functions holomorphic on the disk are holomorphic there, the steps of (3) show that every a_n, q_n and
v_{2n} of the sequence extends holomorphically to the disk and is real for real u, and the relations hold on its real
diameter.
Scope. 4.56 concerns one explicit family at one simple end and only the axis jets: it is a statement about formal
series in x whose coefficients are real analytic on one interval about y_*. No bound on a_n, q_n or v_{2n} in terms of
n, no convergence of the series in x (a common interval for the coefficients does not give it), no solution of (T) and
(V) on a neighbourhood of a point, no attachment to the center jet or to a whole axis component, no use of the
whole-plane velocity, and no profile is obtained. Unlike 4.49, where b has double zeros at the ends of J and the axis
coefficients are flat there, here b has a simple zero at y_* and T vanishes there to the order 10 of 4.13 (ii). The
sign restriction A k < 0 of 4.54 (a), under the sign conditions stated there, is unchanged. So in this family no
obstruction arises from the axis relations at any finite order in x; whether the formal series converges, which
restrictions the relations of 4.49 (2) impose at other simple ends, and the existence of a profile are not decided.
Checks: the verification's proofs, for every n >= 2 by residue integration and of the common interval (4), with exact
controls (P321, 192 controls; P326, 88 controls; P325, complete entry, 611 controls); separate referee audits (A173 of
(0) to (3), VALID, with exact rational checks for n = 2, 3 and 4 at three pairs (C, k); A174 of (4), VALID); an
independent implementation in the analysis of (T_n), (V_n) and the curl relation of 4.49 (2) in exact Laurent series, over the
rationals for n = 2 and 3 and two pairs (C, k), and modulo the primes 2^61 - 1 and 10^18 + 3 for n = 2 to 8 and six
pairs (C, k) with both signs of C and of k, which agrees, for a = -C k/260 and H = -k^7/231 and at each order with the
constants computed at the lower orders, with the tuned values of the three coefficients above, the independence of r_n
from F_n, the variation -2 n E_n t^{n-1} Y G of q_{n-1}, the affine dependence at a further pair of constants, and
r_n = s_n = 0 at the computed pair. The letters f, R, R_*, r_n, s_n, w_n, z, a_n^*, q_{n-1}^*, E_n, F_n and a are
local to 4.56; t, Y, G, E, F_1, D_* and gamma_* are as in 4.55; y_*, u, kappa, A, C and H are as in 4.53 (d); k, B and
gamma are as in 4.54; D and eta are as in 4.51, with the value of D fixed in 4.55; a_n, q_n, v_{2n}, W_1, W_2,
R_Theta, R_Omega, (T_n) and (V_n) are as in 4.49; T, b and J are as in 4.42.
4.57 The leading part of the temperature series at the end in the family of 4.54 (a) (local, formal, beta = 2). Let
beta = 2, kappa = 1, let y_*, u = y_* - y and C be as in 4.53 (d), let k be as in 4.56 and let a_n (n >= 1) be the
coefficients of 4.56, so that a_1 = T/2. Replace each a_n by its Taylor series at y_* in powers of u, and put r = x^2.
Then the formal power series Theta = sum_{n >= 1} a_n x^{2n} in r and u has no term of total degree less than 11, and
its part of total degree 11 is (C/2) r (u - k r/11)^10. Equivalently, for 1 <= l <= 11 the function a_l vanishes at
y_* to order at least 11 - l, and the coefficient of u^{11-l} in its Taylor series is
(C/2) binom(10, l - 1) (-k/11)^{l-1}; in particular a_11(y_*) = (C/2) (k/11)^10 != 0. As a series in x and u, Theta
has no term of total degree less than 12, and its only term of degree 12 is (C/2) x^2 u^10.
Proof outline. With d_y = -d_u and primes d/du, the series of 4.49 (2) are W_1 = (4 + B') x + sum_{j >= 1} v_{2j}'
x^{2j+1}/(2j + 1) and W_2 = B + sum_{j >= 1} v_{2j} x^{2j}, so in r and u the relation R_Theta = 0 at beta = 2 reads
2 r (4 + B' + sum_{j >= 1} v_{2j}' r^j/(2j + 1)) d_r Theta - (B + sum_{j >= 1} v_{2j} r^j) d_u Theta = 0; its
coefficient of r^n is (T_n), so by 4.56 it holds in the ring of formal power series in r and u. Since B = u +
O(u^2), B' = 1 + O(u) and v_2(y_*) = -k (by the curl relation with n = 0, since B''(0) = 2 k and eta vanishes at y_*
to order 6), the vector field has the linear part L = 10 r d_r + (k r - u) d_u, and its other terms have total
degree at least 2. With w = u - k r/11, L r = 10 r and L w = -w, so L (r^i w^j) = (10 i - j) r^i w^j: on homogeneous
polynomials of degree d the kernel of L is 0 unless d is a multiple of 11, and for d = 11 it is spanned by r w^10.
Since a_1 = (C/2) t, Theta contains the term (C/2) r u^10 of degree 11; let Theta_d be its nonzero part of least
total degree d, so that 1 <= d <= 11 (Theta is divisible by r). The part of degree d of the relation is L Theta_d =
0, since the other terms of the field and the parts of Theta of higher degree contribute only in degrees above d.
Hence d = 11 and Theta_11 = c r w^10, with c = C/2 from the coefficient of r u^10. Expanding (u - k r/11)^10 gives
the coefficients of the a_l. For l <= 11 the term a_l x^{2l} has degree at least 11 + l in x and u, with the single
term (C/2) x^2 u^10 of degree 12 when l = 1, and for l >= 12 it has degree at least 2 l >= 24.
Scope. 4.57 is a statement about the formal series of 4.56 at the point (0, y_*): it uses only (T_1) to (T_11), the
analyticity of the coefficients, B, eta and v_2(y_*), and each degree involves finitely many Taylor coefficients. It
does not show that Theta vanishes on a curve through (0, y_*) other than the axis, and it gives no conclusion on the
sign of Theta near (0, y_*). The whole series vanishes on x = 0, since it is divisible by x^2; the substitution
u = k x^2/11 removes its part of degree 11, and 4.57 does not determine the terms of higher degree that remain. No
convergence in x, no solution of (T) and (V) on a neighbourhood of a point and no profile is obtained. Checks: the
verification's proof with exact controls (P328, 156 controls; P332, complete entry, 1983 controls); a separate referee
audit (A175, VALID for the proof, with an exact rational computation of finite Taylor jets of a_1, ..., a_11 at C = k
= 1; its approval of the earlier wording of this Scope is superseded by the correction made in the complete-entry
verification); an independent computation in the analysis of a_1, ..., a_11 from the implementation of 4.56 modulo the primes
2^61 - 1 and 10^18 + 3 at six pairs (C, k) with both signs of C and of k, and of a_1, ..., a_4 over the rationals at
two pairs, which agrees with the vanishing orders and the coefficients above. The letters r, w, L, d, Theta_d, c, i, j
and l are local to 4.57; t is as in 4.55; y_*, u, kappa and C are as in 4.53 (d); k and B are as in 4.54; eta is as in
4.51; a_n, v_{2j}, W_1, W_2, R_Theta and (T_n) are as in 4.49; T is as in 4.42.
4.58 A factorization of the temperature series at the end in the family of 4.54 (a) (local, formal, beta = 2). Let
beta = 2, kappa = 1, let y_*, u, C, k, r and Theta be as in 4.57, so that Theta is a formal power series in r and u
with real coefficients, and replace B and each v_{2j} by its Taylor series at y_* in powers of u. Put p_1 = 2 (4 +
B' + sum_{j >= 1} v_{2j}' r^j/(2j + 1)), p_2 = -B - sum_{j >= 1} v_{2j} r^j and V = r p_1 d_r + p_2 d_u, so that
V Theta = 0 is the relation in the proof of 4.57. Then: (a) there is exactly one formal power series
h(r) = sum_{m >= 1} h_m r^m with p_2(r, h(r)) = r p_1(r, h(r)) h'(r), and h_1 = k/11; (b) there is exactly one
formal power series Z in r and u whose part of degree 1 is u - k r/11 and for which Theta = (C/2) r Z^10, and Z is
the product of u - h(r) and a formal power series with constant term 1; (c) V Z = -(p_1/10) Z, and the formal series
I = x Z(x^2, u)^5 in x and u, which is odd in x, satisfies W_1 d_x I - W_2 d_u I = 0 and Theta = (C/2) I^2. The part
of degree 1 of Z gives 4.57 again.
Proof outline. (a) By the proof of 4.57, p_1 - 10 has no term of total degree 0 in r and u, and p_2 - k r + u has no
term of total degree below 2. In p_2(r, h) - r p_1(r, h) h' the coefficient of r is k - 11 h_1. For m >= 2 the
coefficient of r^m is -(10 m + 1) h_m plus a polynomial in h_1, ..., h_{m-1} and finitely many Taylor coefficients of
B and of v_2, ..., v_{2m}: the term -u of p_2 gives -h_m, the constant 10 of p_1 gives -10 m h_m, and the other terms
of p_2 and of p_1 - 10 have total degree at least 2 and at least 1. So the h_m are determined one after the other.
(b) Put z = u - h(r); r and z are formal coordinates, with u = z + h(r). By (a), V z = p_2 - r p_1 h' vanishes on
z = 0, so V = r e_1 d_r + z e_2 d_z with formal series e_1, e_2 in r and z, e_1(0, 0) = 10 and e_2(0, 0) = -1. Every
term of Theta contains r, so Theta = r f, and we write f = sum_{j >= 0} f_j(r) z^j. Since V r = r e_1, V Theta = 0
divided by r reads r e_1 d_r f + z e_2 d_z f + e_1 f = 0. If f_0 = ... = f_{j-1} = 0, its coefficient of z^j is
r e_1(r, 0) f_j' + (e_1(r, 0) + j e_2(r, 0)) f_j = 0, and if f_j had a lowest term c r^m with c != 0, the coefficient
of r^m would be (10 m + 10 - j) c, which is not 0 for j < 10. Hence f_0 = ... = f_9 = 0 and f = z^10 g with g a
formal series in r and z; at r = 0 one has f = a_1 = (C/2) t and z = u, so g(0, 0) = C/2. The series 2 g/C has
constant term 1, so the binomial series gives a tenth root (2 g/C)^{1/10} with constant term 1, and Z = z (2
g/C)^{1/10}, written in r and u, has the part of degree 1 u - k r/11 and satisfies Theta = (C/2) r Z^10. If Z_1 is
another such series, then at z = 0 its tenth power vanishes, so Z_1 vanishes there and is divisible by z. Write Z_1 =
z L_1. Its prescribed part of degree 1 gives L_1(0, 0) = 1, and L_1^10 = 2 g/C. The normalized tenth root is unique,
so Z_1 = Z. (c) Applying V to Theta = (C/2) r Z^10 gives 0 = (C/2) r Z^9 (p_1 Z + 10 V Z), and the ring of formal
power series in r and u has no zero divisors, so V Z = -(p_1/10) Z. With r = x^2 the operator W_1 d_x - W_2 d_u acts
on series in r and u as V, since 2 x W_1 = r p_1 and -W_2 = p_2, and it maps x to W_1 = x p_1/2; so it maps x Z^5 to
x Z^5 (p_1/2 - 5 p_1/10) = 0.
Scope. 4.58 is a statement in the ring of formal power series in r and u with real coefficients about the series of
4.56 at the point (0, y_*). Unlike 4.57 it uses (T_n) for every n, although each coefficient of h and of Z involves
only finitely many of them and finitely many Taylor coefficients. In this formal sense Theta is (C/2) times the square
of the odd formal first integral I, and it vanishes to order 10 on the formal invariant curve u = h(x^2). It does not
show that h, Z, I or Theta converge, that Theta vanishes on a curve through (0, y_*) other than the axis, or that
Theta has the sign of C off the axis near (0, y_*); no solution of (T) and (V) on a neighbourhood of a point and no
profile is obtained. Checks: the verification's proof with exact controls (P331, 184 controls; P336, complete entry,
1107 controls); a separate referee audit (A176, VALID, with exact rational checks at C = k = 1 of the graph equation
through r^8 and of 68 coefficients of Theta in r and u - h(r)); an independent computation in the analysis from the
implementation of 4.56 modulo the primes 2^61 - 1 and 10^18 + 3 at six pairs (C, k) with both signs of C and of k, and
over the rationals at two pairs, which finds h_1 = k/11, the coefficient -(10 m + 1) of h_m for m <= 11 (m <= 5 over
the rationals), g(0, 0) = C/2, and no term r^l z^j with l <= 11 (l <= 5) and j < 10 in Theta written in r and z; the
same test fails, as it should, with h_2 changed or with u^8 added to a_3. The letters p_1, p_2, V, h, h_m, m, z, e_1,
e_2, f, f_j, j, c, g, Z, Z_1, L_1 and I are local to 4.58; r and Theta are as in 4.57; t is as in 4.55; y_*, u, kappa
and C are as in 4.53 (d); k and B are as in 4.54; a_n, v_{2j}, W_1, W_2 and (T_n) are as in 4.49.
4.59 The temperature near a simple end of the axis component (necessary conditions). Assume the hypotheses of the
first paragraph of 4.42, with J, T and b as there, let y_* be a finite end of J at which b has a simple zero, and let
kappa, n and C be as in 4.53. Put u = y_* - y, epsilon = sgn(y_*), C_u = epsilon^n C and k = -d_x^2 W_2(0, y_*)/2, and
write W_1 = x w with w smooth and even in x. Then there is a connected neighbourhood N of (0, y_*), symmetric under
x -> -x, such that: (a) there is a smooth even function H with H(0) = H'(0) = 0 and
H(x) = k x^2/(4 beta + 3 kappa) + O(x^4) whose graph u = H(x) in N is invariant under the flow of W; it is the local
unstable manifold of the zero (0, y_*) of W, and every invariant C^1 graph u = H_1(x) with H_1(0) = H_1'(0) = 0 agrees
with it near x = 0; (b) Theta = (C_u/2) x^2 Z^n on N with Z = (u - H(x)) L, where L is smooth, even in x and positive
on N and L = 1 at (0, y_*); Z is the only smooth function on N with d_u Z = 1 at (0, y_*) and Theta = (C_u/2) x^2 Z^n;
(c) W . grad Z = ((beta - 2 - 2 w)/n) Z on N; if n is even, I = x Z^{n/2} is smooth and odd in x,
W . grad I = ((beta - 2)/2) I and Theta = (C_u/2) I^2; (d) on N, Theta = 0 exactly on the axis and on the curve
u = H(x); at the points of the curve with x != 0 it vanishes to the order n exactly in u, and off the two curves
sgn Theta = sgn(C_u) sgn(u - H(x))^n. So Theta has the sign of C on N off the two curves if n is even, and changes
sign across the curve u = H(x) at its points with x != 0 if n is odd. For beta >= 2, 4.13 (ii) gives n = 2 + 3 r + 2 d
with r + d odd, so n is even exactly when d = 1/kappa is odd. At beta = 2 and kappa = 1, n = 10,
H(x) = k x^2/11 + O(x^4) and I = x Z^5 with W . grad I = 0; in the family of 4.54 (a), where v_2(y_*) = -k, this is
the curvature k/11 of 4.57 and the form of the formal statement 4.58.
Proof outline. (0) In the variables x and u, W . grad = x w d_x + P d_u with P = -W_2, and w and P are smooth and even
in x. At (0, y_*): P = 0, d_u P = b'(y_*) = -kappa and d_x^2 P/2 = k, and div W = 2 beta gives w = 2 beta + kappa. Put
lambda = beta - 2, so that (T) reads x w d_x Theta + P d_u Theta = lambda Theta; note
2 (2 beta + kappa) - lambda = kappa n. (1) The axis. As a function of u, T satisfies u T_u = (n + u rho(u)) T near
u = 0 with rho smooth (the axis relation b T' + (Lambda - 2 b') T = 0 of 4.42 (0), as in 4.53 (1)). So
Q = T exp(-int_0^u rho) satisfies u Q_u = n Q, Q = c_+ u^n for u > 0 and Q = c_- |u|^n for u < 0, and since T is
smooth the n-th derivatives from the two sides agree, c_- = (-1)^n c_+; on J, Q = C s^n by 4.53, so T = C_u u^n R(u)
with R smooth, R(0) = 1, on both sides of y_*. (2) Division by x^2. Since Theta(0, .) = 0 and Theta is even in x,
Theta = x^2 F with F = int_0^1 (1 - t) Theta_xx(t x, u) dt smooth and even, F(0, u) = T/2, and
x w F_x + P F_u + (2 w - lambda) F = 0, first for x != 0 and then by continuity. (3) The curve. The linear part of W
at (0, y_*) is diag(2 beta + kappa, -kappa), so (0, y_*) is a saddle with unstable direction along the axis of x. The
smooth local stable manifold theorem for -W (Dutilleul, arXiv:1804.06126, Theorem 1.1, with a smooth cutoff away from
(0, y_*)) gives a smooth graph u = H(x), the set of points whose backward orbit stays near (0, y_*) and tends to it at
an exponential rate; the reflection x -> -x maps W to itself, so H is even. Near x = 0 a C^1 invariant graph tangent
to u = 0 lies in this set, which gives the uniqueness in (a). The coefficient of x^2 in P(x, H) = x w(x, H) H' is
k - kappa h_2 = 2 (2 beta + kappa) h_2, h_2 the coefficient of x^2 in H. (4) Divisibility. In the coordinates x and
q = u - H(x), W . grad = x alpha d_x + q delta d_q with alpha and delta smooth, alpha = 2 beta + kappa and
delta = -kappa at (0, 0), since the q-component vanishes on q = 0 by invariance. Then f(x, q) = F(x, q + H(x))
satisfies x alpha f_x + q delta f_q + (2 alpha - lambda) f = 0. Put f_j(x) = d_q^j f(x, 0)/j!. If
f_0 = ... = f_{j-1} = 0, then x alpha(x, 0) f_j' + (2 alpha(x, 0) - lambda + j delta(x, 0)) f_j = 0, and at x = 0 the
quotient of the bracket by alpha is kappa (n - j)/(2 beta + kappa) > 0 for j < n; a solution that is not zero on
0 < x < x_0 then grows at least like a negative power of x as x -> 0, contrary to boundedness. So f_j = 0 for x > 0,
likewise for x < 0, and at x = 0 by continuity; this excludes flat solutions as well. Hence f_0 = ... = f_{n-1} = 0
and Taylor's formula in q gives f = q^n K with K smooth and even, and K(0, q) = (C_u/2) R(q) by (1). Take for N a set
|x| < x_1, |u - H(x)| < q_1 with x_1, q_1 so small that the above holds and 2 K/C_u > 0 there; N is connected, and
L = (2 K(x, u - H(x))/C_u)^{1/n} (positive root) and Z = (u - H(x)) L give (b) and (d). If Z_1 is another such
function, Z_1^n = Z^n for x != 0 and then on N by continuity, so Z_1 vanishes exactly on the curve and Z_1 = (u -
H(x)) M with M smooth; then M^n = L^n, M/L is a continuous real n-th root of 1 on the connected set N, and M/L = 1 at
(0, y_*) since d_u Z_1 = 1 there; so Z_1 = Z. (5) Transport. Applying W . grad to Theta = (C_u/2) x^2 Z^n and using
W . grad x^2 = 2 w x^2 gives (C_u/2) x^2 Z^{n-1} (n W . grad Z + (2 w - lambda) Z) = 0; so the identity of (c) holds
where x Z != 0, a dense set, and then on N by continuity; for even n,
W . grad I = x Z^{n/2} (w + (lambda - 2 w)/2) = (lambda/2) I.
Scope. 4.59 consists of necessary conditions at a simple end of J for every profile that has one. Statements (a) to
(d) are local and use (T), div W = 2 beta, the parity, Theta(0, .) = 0, smoothness and the axis law of 4.53; they do
not use (V), the inverse or the center data. The additional parity remark uses 4.13 (ii), including its vorticity-axis
argument. It does not show that a profile, or a solution of (T) and (V) near (0, y_*), with a simple finite end of J
exists, and it does not show that the formal series of 4.56 converge or are the Taylor series of a solution; the sign
in (d) is a property of actual smooth solutions, and the formal statements 4.57 and 4.58 alone do not give it (a
function that differs from a solution of (T) by a function flat in x can have the same Taylor series in x at every
point of the axis and take the sign of -C at points arbitrarily close to (0, y_*)). The existence of a profile is not
decided. Checks: the verification's proof with exact controls (P334, the case beta = 2, kappa = 1, 53 controls; P337,
74 controls; P338, complete entry, 271 controls); a separate referee audit (A177, VALID with two fixes, both adopted:
the hypothesis Theta(0, .) = 0 is used directly, which covers beta < 2, and N is taken connected for the uniqueness of
Z; with exact checks at (beta, kappa) = (1, 5), (1, 5/2) and (2, 1)). The letters u, epsilon, C_u, k, w, N, H, H_1,
h_2, Z, Z_1, L, M, I, P, lambda, rho, Q, c_+, c_-, R, F, t, q, alpha, delta, f, f_j, j, x_0, x_1, q_1 and K are local
to 4.59; y_*, kappa, n, C and s are as in 4.53; r and d are as in 4.13 (ii); Lambda is as in 4.13; v_2 is as in 4.49;
J, T and b are as in 4.42.
4.60 The vorticity near a simple end of the axis component (necessary conditions). Let beta >= 2, assume the
hypotheses of 4.59, with u, epsilon, C_u, w, N, H and Z as there, and let eta and s be as in 4.53. By 4.13 (ii),
m = 1 + (2 beta + 1)/kappa is an integer and eta = E s^m (1 + o(1)) on J near y_*, with E != 0 of the sign of C. This
sign relation holds in the original coordinates: the reflection of 4.8 changes the signs of both C and E and preserves
E/C. Put E_u = epsilon^m E. Then there is a connected neighbourhood N' of (0, y_*), contained in N and symmetric under
x -> -x, such that: (a) Omega = E_u x Z^m Y on N', where Y is smooth, even in x and positive on N' and Y = 1 at
(0, y_*); Y is the only function on N' with this property; (b) on N', Omega = 0 exactly on the axis and on the curve
u = H(x) of 4.59 (a); at the points of the curve with x != 0 it vanishes to the order m exactly in u, and off the two
curves sgn Omega = sgn(E_u) sgn(x) sgn(u - H(x))^m. So near (0, y_*), off the axis, Omega and Theta vanish on the same
curve, the local unstable manifold of the zero (0, y_*) of W. By 4.13 (ii), n - m = 1 + r + d is even; since E/C > 0
this gives sgn(E_u) = sgn(C_u), and with 4.59 (d), x Omega Theta > 0 on N' off the two curves. At beta = 2 and
kappa = 1, m = 6 and n = 10.
Proof outline. (0) As in 4.59 (0), W . grad = x w d_x + P d_u, and (V) reads
x w d_x Omega + P d_u Omega + Omega = d_x Theta, where d_x is taken at fixed u (fixed y). Since Omega is odd in x,
Omega = x G with G = int_0^1 Omega_x(t x, u) dt smooth and even and G(0, u) = eta; by 4.59 (b), d_x Theta = x S with
S = C_u Z^n + (C_u n/2) x Z^{n-1} d_x Z smooth. Hence x w G_x + P G_u + (w + 1) G = S, first for x != 0 and then by
continuity. (1) The axis. Since eta is smooth, eta = E s^m (1 + o(1)) on J and u = epsilon s on J, the derivatives of
order less than m of eta in u vanish at u = 0 and the m-th divided by m! is E_u; so G(0, u) = E_u u^m + O(u^{m+1}) on
both sides of u = 0. (2) Divisibility. In the coordinates x and q = u - H(x) of 4.59 (4),
W . grad = x alpha d_x + q delta d_q, and g(x, q) = G(x, q + H(x)) satisfies
x alpha g_x + q delta g_q + (alpha + 1) g = S, where S, as a function of x and q, is divisible by q^{n-1} since
Z = (u - H(x)) L (d_x Z need not vanish on the curve, which costs one power of q). Since
n - m = 1 + (beta + 1)/kappa > 1, d_q^j S(x, 0) = 0 for j < m. Put g_j(x) = d_q^j g(x, 0)/j!. If
g_0 = ... = g_{j-1} = 0 and j < m, then x alpha(x, 0) g_j' + (alpha(x, 0) + 1 + j delta(x, 0)) g_j = 0, and at x = 0
the quotient of the bracket by alpha is
(2 beta + kappa + 1 - j kappa)/(2 beta + kappa) = kappa (m - j)/(2 beta + kappa) > 0; as in 4.59 (4) this gives
g_j = 0, including flat solutions. Hence g_0 = ... = g_{m-1} = 0 and Taylor's formula in q gives g = q^m K with K
smooth and even, and K(0, 0) = E_u by (1). (3) Take for N' a set |x| < x_2, |u - H(x)| < q_2 inside N with K/E_u > 0
there, and Y = K(x, u - H(x))/(E_u L^m), with L as in 4.59 (b); then Omega = x G = E_u x Z^m Y, and Y is smooth, even,
positive and Y = 1 at (0, y_*). If Omega = E_u x Z^m Y_1 on N', then Y_1 = Y where x Z != 0, a dense set, and so on N'
by continuity. (b) follows from the positivity of L and Y; at a point (x_0, H(x_0)) with x_0 != 0 the derivatives of
Omega in u of order less than m vanish and the m-th is m! E_u x_0 L^m Y != 0. The consequence after (b):
sgn(E_u) sgn(C_u) = epsilon^{n - m} sgn(E C) = 1, so off the two curves
sgn(Omega Theta) = sgn(x) sgn(u - H(x))^{n + m} = sgn(x) by (b) and 4.59 (d).
Scope. 4.60 consists of necessary conditions at a simple end of J for every profile with beta >= 2 that has one. (a)
and (b) are local: they use (T), (V), the parity, Theta(0, .) = 0, smoothness, 4.59 and the asymptotics of eta in
4.13 (ii), which come from the axis system of 4.13 (i) between 0 and y_*; the sentence on x Omega Theta also uses the
parity of n - m in 4.13 (ii), which uses the axis beyond y_* and W(X) = beta X + o(|X|). 4.60 does not use the
inverse. It does not show that a profile, or a solution of (T) and (V) near (0, y_*), with a simple finite end of J
exists. Checks: the verification's proof with exact controls (P339, 183 controls, among them fields that satisfy (T)
and (V) near (0, y_*) but not Omega = d_y W_1 - d_x W_2; P342, complete entry, 533 controls); two separate referee
audits (A178, of (a) and (b), VALID with no corrections and 204 exact symbolic checks; A179, of the text of 4.60,
VALID with no corrections and exact sign checks at both orientations). The letters E, E_u, N', Y, Y_1, G, t, S, g,
g_j, j, K, x_0, x_2 and q_2 are local to 4.60; u, epsilon, C_u, w, N, H, Z, L, P, q, alpha and delta are as in 4.59;
y_*, kappa, n, C, s and eta are as in 4.53; m, r and d are as in 4.13 (ii); J is as in 4.42.

## 5. Answers to the specific questions of the problem

Q1. Existence of a smooth whole-plane moving-center B2 profile with a0 != 0 and beta > 0. Not decided: no theorem here
excludes every class A profile, and no profile is constructed. The restrictions of section 4 are indexed below; each
holds under the hypotheses of the cited item. Unconditional statements hold for every class A profile, hence (4.15)
for every smooth B2 profile with sublinear velocity and polynomially bounded vorticity, and at beta = 2 for every
smooth B2 profile with sublinear velocity. In sign statements a0 > 0 (the signed scaling (A6) with l = -1, which
exchanges the upper and lower half-axes, reduces a0 < 0 to this case).
- Range: beta >= 2 (4.2).
- Temperature: for beta > 2, Theta = 0 on the set of bounded forward orbits and Theta = a0 xi^2 on the basin of the
  center (4.3), and sup_{|X|=r} |Theta| is comparable to r^{1-2/beta}, with a continuous angular limit (4.10); at beta
  = 2, Theta is bounded (4.4); Theta is in no L^p with 0 < p < infinity (4.5).
- Vorticity mass and far field: Omega is in no L^p for 1 <= p <= 2 beta, every tail that is uniformly o(r^{-1/beta})
  is excluded, and the ordinary drift integral is never absolutely convergent (4.8, 4.9, 4.11); Omega =
  r^{-1/beta}(a(theta) + o(1)) uniformly, with (D) and the derivative bounds of 4.12; the leading terms determine the
  second terms (4.16) and, for beta > 2, the third terms (4.26(a)); for 2 < beta <= 3 the next terms involve in
  addition a constant velocity C given by a global integral (4.26(b), 4.27); and no profile is exactly homogeneous
  outside a ball (4.25); 4.26(c), (d) and 4.27(c) are necessary conditions for fields with power expansions of the
  stated forms (for noninteger beta > 3, 4.26(d) is an implication from assumed expansions).
- Axis: the linear system of 4.13 for a = Theta_xx/2 and q = Omega_x on the axis, with a, q > 0 up to the nearest
  additional zeros of b; integrality and parity conditions at a finite nondegenerate nearest zero, which fail for
  irrational beta and for beta = P/Q with P, Q odd, and flat axis data at a degenerate one (4.13); zeros of W off the
  center and the reduction to G (4.19(d), (e)); the axis tails and their constants (4.21).
- Partial conditions of (V), beta > 2: the Taylor conditions of (V) at the center impose no condition on the harmonic
  coordinates of the stream function (4.28(a)); the configurations of the compatibility summary after 4.31 (4.28(b),
  4.29 to 4.31, 4.34) are not profiles (4.32); under the hypotheses of 4.29(d), a compactly supported change of the
  vorticity of the example of 4.13 cannot make d_x R_Omega(0, .) vanish on the whole axis.
- Reformulation, beta > 2: one scalar equation for Psi when Theta(0, .) = 0, the necessary angular cancellation
  conditions C_+ = C_- = 0 under the exterior bounds of 4.33(d), and vanishing horizontal offsets (4.33(e)) (4.33);
  for a stream odd in x with Psi_xy(0) = 1 + beta/2, the compatibility identity E_comp = 0 of 4.32(a) is equivalent to
  (T) and (V) for the normalized primitive near the center when Psi_xxx(0) != 0, and on R^2 for real analytic streams
  with sublinear velocity (4.32(d)).
- Global-source subclass G (W has no zero other than the center; beta > 2): the area-preserving normal form and two
  excluded shape classes of vorticity (4.18); Theta_x >= 0 on {x > 0} implies Omega > 0 on {x > 0} (4.21(d)); the
  temperature tail, the bounds on Theta/x^2 and the decay of the vorticity along level curves of Theta (4.22); the
  axis relations, and the axis coefficient Q_+ of 4.21(a) as the value of a strictly increasing functional of the axis
  velocity; this functional is unbounded at fixed beta and a0 along the axis velocities of the positive canonical
  vorticities of 4.35(b), which are not shown to belong to profiles (4.35).
- Identities: the critical flux identity (4.12(g)); for beta > 2 the quadratic and critical-weight identities for
  Theta/x^2 and Omega/x (4.17); for beta >= 2 the equivalent family of homogeneous-weight identities, including the
  strain identity, whose vorticity term has no fixed sign under positivity of Omega on {x > 0} and which smooth
  non-profiles satisfy together with the conditions of 4.23(c); the center strain excludes vorticity dominated by its
  reflection below the center and, for beta > 2, vorticity of small scale-invariant size of Omega/x (4.23); for beta >
  2 the exterior fields of a class A profile have finite power-logarithmic expansions through the dipole term (4.37),
  and its renormalized impulse vanishes for beta outside the countable set Z_crit and its renormalized energy for beta
  outside the countable set Z_E (4.36 to 4.38).
- Finite angular content: no class A profile has a vorticity or a stream function with finitely many angular Fourier
  modes (4.24); infinitely many modes are not excluded.
- Restricted temperature representations: for every beta no smooth B2 profile with sublinear velocity has a
  temperature that is a polynomial in x of bounded degree with coefficients depending on y (4.39(a)). For every
  beta >= 2, on the component J of {Theta_xx(0, .) != 0} that contains 0, whose finite ends are the nearest zeros of
  W_2(0, .) on the two half-axes (4.42(a)), the ratios d_x^{2j} Theta(0, y)/Theta_xx(0, y)^j with j = 2 and j = 3 are
  not both constant (4.42(b), 4.43); so no such profile has a temperature H(x/rho(y)), rho > 0, on a neighbourhood of
  the whole axis (4.7(xxiv), 4.43). For beta > 2 the ratio with j = 2 has no limit other than 0 in
  [-infinity, infinity] at an infinite end of J (4.44, 4.45), and for every beta >= 2 and s > -1 + 2/beta its absolute
  value is not bounded below by c |y|^s, c > 0, near such an end (4.45); the exponent -1 + 2/beta is the best possible
  for the axis relations used there, which allow |y|^{1 - 2/beta} times the ratio to diverge like a power of log |y|,
  with either sign for beta > 2 and to -infinity at beta = 2 (4.47), and at beta = 2 they allow every finite limit
  (4.46); at beta = 2, for profiles, the ratio with j = 2 does not tend to +infinity at an infinite end of J (4.47).
  For class A profiles more holds: for every j >= 2, |y|^{(j - 1)(1 - 2/beta)} times the ratio with index j has a
  finite limit at an infinite end of J (4.48), so the logarithmic divergence of 4.47 does not occur for them; at
  beta = 2, where every smooth B2 profile with sublinear velocity is in class A (4.15), every ratio has a finite limit
  there. Whether J can be bounded is not decided; the coefficients of (T) and (V) of every order on the axis, with the
  canonical inverse, do not exclude it (4.49), and neither do (T) on R^2 and the coefficients of (V) of every order on
  the axis (4.50). At a finite end of J at which W_2(0, .) vanishes to a finite order p >= 2, the ratio with j = 2 of
  a profile tends to -infinity, and d_x^4 Theta(0, y)/Theta_xx(0, y) is asymptotic to -(3 d0/beta) p (p - 1) times the
  inverse square of the distance to that end, with d0 = 1 + 3 beta/2 (4.51). At an end y_* at which b = W_2(0, .) has
  a simple zero, that ratio has a limit in [-infinity, infinity], equal to -sgn(y_* b''(y_*)) infinity if
  b''(y_*) != 0, and the axis relations used for 4.51 allow every finite and both infinite limits, at beta = 2 also
  with the signs and integrality required of a profile (4.53); at beta = 2 the same holds when the relation for d_x^3
  Omega(0, .) on the axis is added, although that relation restricts the examples of 4.53 (e) to one sign of b''(y_*)
  (4.54), and in the family of 4.54 (a) the relations for d_x^6 Theta(0, .) and d_x^5 Omega(0, .) can then be met near
  y_* by the choice of two free constants (4.55), and the axis relations of every order, as formal series in x whose
  coefficients are real analytic on one interval about y_*, by a unique choice of two free constants at each order
  (4.56); at an end at which b vanishes to infinite order they force neither a sign nor a limit of the ratio (4.52).
  Apart from the examples, which are not profiles, these are necessary conditions on the axis data of the profiles
  concerned; whether the limits at the infinite ends of J are nonzero, which limit a profile has at a simple end, and
  the existence of a profile, are not decided. For a profile, near (0, y_*) at a finite end y_* of J at which b has a
  simple zero, Theta = c_1 x^2 phi^n and Omega = c_2 x phi^m Y, where c_1 and c_2 are nonzero constants of the same
  sign, n = 2 + (3 beta + 2)/kappa and m = 1 + (2 beta + 1)/kappa with kappa = -b'(y_*) are integers and n - m is
  even, Y is smooth and positive, and phi is smooth, has nonzero gradient on its zero set, and vanishes exactly on the
  local unstable manifold of the zero (0, y_*) of W, a smooth curve through (0, y_*) symmetric under x -> -x; so near
  (0, y_*), Theta and Omega vanish exactly on the axis and on that curve, and x Omega Theta > 0 off them (4.59, 4.60).
  In the family of 4.54 (a), the formal temperature series of 4.56 is c x^2 times the tenth power of a formal series
  in x^2 and y_* - y, with a constant c != 0 (4.57, 4.58).
- Weak vorticity sign (Omega >= 0 on {x > 0}, or Omega <= 0 there, zeros allowed; beta >= 2): restrictions on
  forward-escaping orbits in {x > 0} and on critical points of Theta on them (4.7(ix)(A), 4.20).
- beta = 2, smooth profiles: the compact zero arc gamma of W through the center, its flat endpoints and their three
  types, and the failure of analyticity near gamma (4.7(i) to (iv), (vi), (viii)). The scattering identities
  (4.7(vii)), and, when W has no zero off gamma, the backward limits of the orbits and the arcs of asymptotic
  directions (4.7(v)). Under the weak sign and the further hypotheses stated in each item, the critical points of h
  and the monotonicity of Theta along gamma (4.7(ix)(B), (x), (xi)). No neighbourhood of an endpoint on which U is
  real analytic or Theta is constant, and no outgoing endpoint at which U is real analytic along the normal line and
  Omega along the nearby parallel lines beyond it, or at which W is, beyond the strong unstable curve, a finite sum of
  products of functions of s and of z as in 4.7(xii)(d) (4.7(xii), (xxi)). The flatness of Theta - L and Omega along
  the strong unstable curve of every endpoint, the leading term of that curve in terms of the curvature of the zero
  curve, the conclusion of (xii)(c) at every endpoint whose strong unstable curve meets {s > 0} in every neighbourhood
  of the endpoint, and, when the endpoints are nonaccumulating, the index of gamma, with zeros off gamma forced by
  incoming endpoints (4.7(xiii)). For incoming endpoints with isolated zeros off gamma, Theta = L and Omega = 0 on the
  side of the strong unstable curve beyond each endpoint near it, the analogues of (vi), (xii)(b) and (xii)(c) at the
  endpoints, and, if these zeros are nondegenerate, no zero of W on the axis other than 0 (4.7(xiv)). At outgoing
  endpoints, and at incoming ones with isolated zeros off gamma, no neighbourhood of a point of the orbits of the
  strong unstable curve on which Theta - L or Omega vanishes (4.7(xv)(a), (b)). When Z = gamma, the open parts O_+ and
  O_- of the endpoint basins (without the endpoint and its strong unstable orbits) as components of the interior of
  {Omega = 0} and of the interior of {Theta = L} (4.7(xv)(c)), and the decomposition of the complement of the two
  strong unstable lines C^_+ and C^_- into O_+, O_- and a simply connected region F containing the axis, with
  Theta = L and Omega = 0 outside F (4.7(xvi)). Near each endpoint, vorticity and velocity in no quasianalytic
  Denjoy-Carleman class, and the temperature in none on a connected open set containing gamma. At outgoing endpoints,
  and at incoming ones with isolated zeros off gamma, temperature, vorticity and velocity in no such class near any
  point of the orbits of the strong unstable curve. For each fixed family of parallel lines transverse to an arc of
  these orbits: outside one meager set of lines, restrictions of Theta - L and Omega that are flat nonzero germs,
  hence in no such class; for each class, outside a meager set of lines that may depend on the class, restrictions of
  U not in that class (4.7(xvii)). Near an outgoing endpoint, an exact local reduction, with a converse, of the
  equations to one curl equation in a normal form on the arc side and a one-sided potential Cauchy problem, with the
  full gradient trace, on the basin side (4.7(xviii)). At an outgoing endpoint: no real analytic field equal to W on a
  subset of the side beyond the strong unstable curve of positive area in every neighbourhood of the endpoint; no
  bound c A^n (n!)^2 for the derivatives of order n in one direction of W on that side, uniformly up to the endpoint,
  or of Omega on a neighbourhood of the endpoint; and, when the tangent there is not vertical, the decomposition of
  {Omega != 0} near the endpoint into whole fibres of the normal form of 4.7(xviii)(a), with directions of
  accumulation filling the closed half circle on the side of gamma (4.7(xix)). At accumulating endpoints, Theta not
  constant on any neighbourhood of the endpoint; if some neighbourhood of the endpoint contains no arc of zeros of W
  off gamma, the isolation of the zeros off gamma near it, Theta = L and Omega = 0 on the side of the strong unstable
  curve beyond it, the analogues of 4.7(vi), (xii)(b) and (xii)(c), and the first two conclusions just listed for an
  outgoing endpoint, which also hold at incoming endpoints with isolated zeros off gamma (4.7(xix)(e), (xx)). Every
  open set on which Theta is constant lies in an open invariant set on which Theta is constant and Omega = 0
  (4.7(xxi)). No nondegenerate straight segment of zeros of W on which Theta is constant; at an endpoint at which
  Theta is constant on a subarc of gamma ending there, Theta = L and Omega = 0 on the side of the strong unstable
  curve that meets gamma near it, no point of the exterior center branch with a neighbourhood on which Theta is
  constant if the endpoint is incoming, and arcs of zeros of W off gamma with nonconstant Theta in every neighbourhood
  of it if it is accumulating (4.7(xxii)). No temperature of the form H(x/rho(y)) with rho positive and of class C^2
  on R and either H' nonzero at arbitrarily large arguments, or H nonconstant and rho bounded above on a half-line
  [y_0, infinity) or (-infinity, y_0] (4.7(xxiii)). Under (V), no temperature of the form H(x/rho(y)) on a
  neighbourhood of the whole axis, for any rho > 0 and H (4.7(xxiv)).

Open: the branch beta > 2 with the slow tail, including the subclass G, and at beta = 2 smooth profiles with all the
properties listed; profiles with beta > 2, sublinear velocity and vorticity growing faster than every polynomial are
not covered (4.15). No admissible numerical candidate was found (section 6).

Q2. Chen-Hou's mechanism without the wall. (a) The B2 center reproduces the published corner data: with beta =
-c_l/c_omega the published c_l, c_omega and u_x(0) satisfy the strain identity c = 1 + beta/2 of 4.1 (4.14(a)); this
checks normalizations, not the vorticity-gradient identity or the equations. (b) The wall is an invariant line through
the corner on which (theta_x, omega) obey a sign-preserving transport system; in B2 the only imposed invariant line
through the center is the symmetry axis, on which Omega = grad Theta = 0, and the horizontal line through the center
is invariant only in the special case U_2(x, 0) = U_2(0) (4.14(a)). (c) Axis transport: a = Theta_xx/2 and q = Omega_x
on the axis solve a closed linear system driven by b = W_2(0, y); for a0 > 0 they are positive up to the nearest
additional zeros of b and vanish there, with integrality and parity conditions at nondegenerate zeros and flatness at
degenerate ones (4.13(i)-(iii), (v), (vi)). (d) Center drift: v0 = U(0) is a gauge of (B2-P); its unsubtracted
Biot-Savart integral is not absolutely convergent for any class A profile (3 (A5), 4.11(ii)); no conclusion about
signed principal values is asserted without a sign assumption (with a0 > 0 and Omega >= 0 on {x > 0} the truncations
tend to +infinity, 4.11(ii)). (e) Nonlocal kernel: the center strain c = 1 + beta/2 is the moment (1/pi) int x y
Omega/|X|^4; by the oddness of Omega this gives int_{x>0, y>0} x y [Omega(x, y) - Omega(x, -y)]/|X|^4 dX =
(pi/2)(1 + beta/2) > 0 (4.13(iv)), an integral statement with no pointwise comparison of Omega(x, y) and Omega(x, -y).
(f) The explicit example in the scope remark of 4.13 satisfies (T), parity, the canonical inverse, all center data,
Omega > 0 on x > 0, a global source at the center and the slow tail, for every beta > 2, and fails (V), already at the
second third-order center condition 4.13(vii). So the transport equation, positivity, the center data, the canonical
inverse and the slow tail do not by themselves exclude the positive-vorticity production mechanism; an exclusion must
use (V) beyond the leading center identities. The further conditions of (V) collected in the compatibility summary
after 4.31 (at the center, on bounded sets together with the whole axis, and on a disk together with an exterior
domain) do not suffice either; the configurations realizing them are not profiles (4.32). (g) Published criteria and
wall profiles: each of the continuation criteria of Chae-Wolf and Chae-Constantin listed in 4.14(h) fails for the
solution generated by a class A profile (center strain k = 1 + beta/2 >= 2), so these criteria neither exclude nor
admit the class; Zhang's half-plane Liouville statement has exponents compatible with B2 for beta > 2 but needs a wall
and sign and maximum hypotheses that B2 does not supply (4.14(i)); the numerical wall profiles of Wang et al.
correspond to beta = 1 + lambda between 2.18 and 2.93 and match the center identity and the tail exponent of 4.1 and
4.12, but are not whole-plane profiles (4.14(j)).

Q3. No condition at y = 0; center drift. No boundary condition at y = 0 and no half-plane inverse is used anywhere;
the inverse is the whole-plane relative law (A4). Since the drift integral is not absolutely convergent in class A, only U_rel is
computed and compared; for the physical reconstruction the observer representative U = U_rel (v0 = 0, material center at
rest) is declared, and any other v0 follows from the exact observer change of (A5). The independent whole-plane inverse reproduces the exact
relative velocity of manufactured fields with a slow tail Omega ~ r^{-1/3} to about 7e-15 when the exterior of the
computational square is included (a sampled implementation test, not an error bound), and errs by O(1) (1.1 to 1.8)
when the exterior is omitted (section 7, 13:12 entry):
truncating the inverse to a box is not a valid closure for this tail class.

Q4. beta = 2 bounded temperature, tail classes, finite data. Every class A profile has Theta in no L^p with
0 < p < infinity (4.5). For beta > 2, Theta is unbounded, with sup_{|X|=r} |Theta| comparable to r^{1-2/beta} (4.3(i),
4.10), so a profile cannot give a finite nonzero sup |theta| for all times; at beta = 2, Theta is bounded (4.4),
compatible with the conservation of sup |theta|, and the branch is restricted by 4.7. Integrable vorticity tails,
finite enstrophy, tails uniformly o(r^{-1/beta}) and tails O(r^{-2/beta}) are excluded (4.6, 4.8, 4.9); within class A,
sup_{|X|=r} |Omega| is comparable to r^{-1/beta} (4.12), and by 4.15 the same holds for every smooth B2 profile with the
stated parity and center jet, sublinear velocity and polynomially bounded vorticity (at beta = 2 no vorticity growth
hypothesis is needed). Omega is in no L^p for 1 <= p <= 2 beta, and U_rel = u0 + o(r^{1-1/beta}) with u0 a nonzero
field homogeneous of degree 1 - 1/beta (4.12, 4.16), so the velocity is unbounded. An exact profile would therefore
give an exact whole-plane self-similar solution with unbounded velocity (and, for beta > 2, unbounded temperature); no
localized finite-energy construction is established here.

Q5. Scaling gauge. Theta_l = l Theta(X/l), Omega_l = Omega(X/l), U_l = l U(X/l), l real nonzero, is exact, with
a0 -> a0/l and beta unchanged (A6); a0 = 1 fixes it and excludes no branch (l < 0 covers the sign of a0 through the
y-reflection). U(0) = 0 is not a condition on profiles; it is the declared observer convention of Q3.

## 6. Restrictions and limitations

- No theorem here excludes all smooth class A profiles with beta >= 2, and none is constructed. The results indexed in
  Q1 restrict them, but they leave open the branch beta > 2 with the slow tail (the far field of every class A
  profile, 4.12), including the global-source subclass G (the additional structural results specific to G are in 4.18,
  4.21, 4.22 and 4.35; all class A restrictions also apply to G under their stated hypotheses; none excludes all
  profiles in G), and at beta = 2 smooth profiles with all the necessary properties of 4.7.
- Conditional results apply only under their stated hypotheses: the integrality conditions of 4.13 and 4.19(e) (beta
  irrational or P/Q with P, Q odd, nondegenerate zeros), the weak-sign results 4.7(ix)-(xi) and 4.20, the shape
  classes of 4.18, 4.21(d), and the necessary conditions 4.26(c), (d) and 4.27(c) for fields with power expansions;
  for noninteger beta > 3, 4.26(d) is an implication from assumed expansions. Profiles with beta > 2, sublinear
  velocity and vorticity growing faster than every polynomial are not covered (4.15).
- The constructions (the example of 4.13, the configurations of the compatibility summary after 4.31 (4.28(b), 4.29 to
  4.31, 4.34), the fields of 4.23(c), the field in the scope paragraph of 4.26(d)) are not profiles (for 4.28(b) to
  4.31 and 4.34 by 4.32); they show only that the particular conditions each satisfies do not force a contradiction;
  compatibility with all other necessary conditions has not been established.
- None of the published theorems audited in 4.14 decides the class.
- No admissible numerical candidate meeting the independent residual and stability criteria has been found in the
  computations reported here.

### 6.1 Numerical status and independent residual tables

No numerical result here is evidence of existence or of nonexistence. Two forcing homotopies of the transporting
velocity were used: W_eps = beta X + U_rel[eps Omega + (1 - eps) Omega_ext], with a fixed external vorticity Omega_ext
whose center strain is 1 + beta/2, where eps = 1 is (B2-P); and W = beta X + U_rel[Omega + lambda f] with a source f,
where lambda = 0 is (B2-P) (described below). Residuals called forced are those of the homotopy problem; all other
residuals below are those of (B2-P) itself, with U_rel the whole-plane inverse of the state's own vorticity, evaluated
by evaluators written independently of the solver: their own value reconstruction from the saved coefficients,
seven-point Cartesian finite differences (with two or three step sizes, depending on the evaluation), and an
independently computed whole-plane inverse (a Cartesian inverse with Duffy quadrature on three square cores plus the
compactified infinite exterior, three quadrature orders; for the wide-grid evaluations of Tables 6.1d and 6.1e, an
adaptive sine-mode inverse in the physical radius).
Definitions. R_Theta = W.grad Theta - (beta - 2) Theta and R_Omega = W.grad Omega + Omega - Theta_x, with
N_Theta = |W_1 Theta_x| + |W_2 Theta_y| + |beta - 2| |Theta| and N_Omega = |W_1 Omega_x| + |W_2 Omega_y| + |Omega| + |Theta_x|.
With F = Theta/x^2, G = Omega/x, A = W_1/x and B = W_2, the desingularized residuals are
  R_F = A(2F + x F_x) + B F_y - (beta - 2) F,   R_G = A(G + x G_x) + B G_y + G - (2F + x F_x),
  N_F = |A(2F + x F_x)| + |B F_y| + |beta - 2| |F|,   N_G = |A(G + x G_x)| + |B G_y| + |G| + |2F + x F_x|,
so that R_Theta = x^2 R_F, R_Omega = x R_G, N_Theta = x^2 N_F and N_Omega = |x| N_G, and off the axis the divided ratios
equal the Cartesian ones (largest discrepancy 2.2e-10 at the points of Table 6.1a and 2.9e-10 on the regional
raw arrays). Table 6.1a uses the eleven points (0.00013, 0.00027),
(0.031, 0.023), (0.13, 0.27), (0.63, -0.42), (1.13, 0.73), (0, 0.81), (0, -0.81), (-0.63, -0.42), (0.47, 0), (2.03, -1.17),
(4.7, 8.2), finite-difference steps 8e-5, 4e-5, 2e-5, and the inverse with core sizes 12, 24, 48 and quadrature orders
24, 48, 72; the values shown use the finest step, core 24 and order 72. Table 6.1b uses the seven points (0.13, 0.27),
(0.63, -0.42), (1.13, 0.73), (0, 0.81), (-0.63, -0.42), (0.47, 0), (2.03, -1.17), steps 1e-3, 5e-4, 2.5e-4, and the
state's own inverse at core 12 and order 48 (the inverse study for these states used cores 6, 12, 24 and orders 16, 32,
48). All tabulated values are sampled empirical diagnostics (IEEE double precision; finite differences and quadrature
without certified error bounds), not certified bounds; they are values at finitely many points, so the suprema over
the domain may be larger. Ratios use no denominator floor (0/0 = 0, nonzero/0 = infinity). Cartesian ratios at the axis points (x = 0) are
omitted, since they are vacuous there; R_F and R_G, with their axis limits, are used there. Among the retained off-axis
Cartesian ratios and the divided ratios no computed zero denominator was reported; underflow locations are not certified.

Table 6.1a. The three intermediate states at eps = 0.34 of the homotopy (beta = 3, 2.5, 3), 16:49.

| state | beta | max abs R_Theta | max abs R_Theta/N_Theta | max abs R_Omega | max abs R_Omega/N_Omega | max abs R_F | max abs R_F/N_F | max abs R_G | max abs R_G/N_G |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 8.20 | 0.358 | 2.22 | 0.839 | 4.02 | 0.559 | 10.6 | 0.839 |
| 2 | 2.5 | 3.37 | 0.532 | 3.63 | 0.743 | 4.89 | 0.762 | 7.73 | 0.743 |
| 3 | 3 | 4.59 | 0.391 | 3.83 | 0.590 | 4.78 | 0.611 | 7.27 | 0.634 |

Center data of these states: a0 - 1 = 3.6e-5, -1.5e-4, -1.7e-4; Omega_x(0) - 4a0/beta = 2.93e-2, 3.42e-2, 5.40e-2; the
center strain equals 1 + beta/2 to 1e-15 because it is imposed by projection (an independently computed source-moment
quadrature of the strain, using angular orthogonality and exact spline integration, agrees); R_G(0) = 4.4e-2, 4.3e-2, 8.1e-2, in
agreement with R_G(0) = (beta/2)(Omega_x(0) - 4 a0/beta), valid when the strain is exact. Inverse
uncertainty: the change from quadrature order 48 to 72 is at most 1.31e-4 and the spread over three core sizes at most
1.2e-5 (empirical diagnostics, not certified bounds); omitting the exterior of the computational square changes the
velocity by 3.99 to 10.3. Sampled parity defects are at most 7e-15. The elliptic residual, divergence and
vorticity-reconstruction error of the solver's own velocity interpolant were not evaluated for these states (they
were computed with the velocity interpolation rule discussed in the item "Numerical closures" of 6.2); the independent
evaluator's inverse passes off-knot div-curl checks at 1e-9 to 1e-8 for the Table 6.1a states.

Table 6.1b. The eps = 0 starting states (fixed beta), true (B2-P) residuals with the state's own whole-plane inverse,
independent evaluation at the seven original points (Cartesian whole-plane self inverse, finite differences with steps
1e-3, 5e-4, 2.5e-4; finest step shown), 17:12.

| beta | max abs R_Theta | max abs R_Theta/N_Theta | max abs R_Omega | max abs R_Omega/N_Omega | max abs R_F | max abs R_F/N_F | max abs R_G | max abs R_G/N_G |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 6.64 | 0.592 | 3.37 | 0.404 | 7.21 | 0.654 | 3.57 | 0.404 |
| 2.5 | 7.08 | 0.701 | 4.34 | 0.388 | 6.56 | 0.770 | 3.93 | 0.388 |

For comparison, the same states have much smaller residuals for the forced transport they were computed for
(W = beta X + U_rel[Omega_ext], eps = 0 of the homotopy; this is not (B2-P)): maxima of abs R_Theta 9.94e-2 and
1.97e-1, of abs R_Omega 2.28e-1 and 7.86e-1, of abs R_Theta/N_Theta 6.66e-3 and 1.50e-2, of abs R_Omega/N_Omega 2.82e-2 and
6.38e-2 (15:43). Center data: a0 - 1 = 2.5e-3, 3.6e-3; Omega_x(0) - 4a0/beta = 2.2e-4, 2.6e-4 (Omega_x(0) - 4/beta =
3.5e-3, 6.0e-3); R_G(0) = 3.3e-4, 3.3e-4. Spread of the velocity over three cores at most 1.8e-9; omitting the
exterior changes the self-induced velocity by 0.75 to 2.7. For these two states, finite differences of the independent
whole-plane inverse of their own vorticity (core 12, order 72, step 1e-3) reproduce the imposed center strain to about
1e-11 at beta = 3 and 2e-12 at beta = 2.5, with sampled -curl V - Omega at most about 2e-11 and sampled divergence at
most about 2e-11 (18:07); these are empirical values that validate the inverse on these two states, do not reduce their
transport residuals, and are not asserted for the states of Table 6.1a.

Remark on the role of beta. At eps = 1, a0 is a scaling gauge (A6) and beta is an unknown. A residual floor at one
fixed beta is a failure of that computation, not evidence about existence at that beta, and scanning beta is a
reasonable experiment. No count of equations against unknowns for the discretized problem is asserted.

Continuation at fixed beta with a later solver. A safeguarded Anderson-accelerated fixed-point iteration on the
characteristic formulation follows the same forcing homotopy from eps = 0 in small steps of eps; beyond eps of about
0.054 the amplitude a0 is prescribed in each stage and eps is solved from the center strain condition. At beta = 3,
with the residual angles oversampled, the fitted states have eps = 0.057682, 0.058298 and 0.056050 at a0 = 2.1, 2.4
and 2.7 (16 angular modes, 56 radial intervals), and eps = 0.057685, 0.058301 and 0.056052 at a0 = 2.1, 2.4 and 2.7
with 20 modes and 72 intervals; among the sampled amplitudes eps increases and then decreases, with its largest
sampled value near 0.0583; no turning point of a continuous branch is validated. The independently evaluated residuals
of the forced problem (maxima of R_F/N_F and R_G/N_G with the forced velocity, the evaluator of this section on its
own wide point set) are 0.0039/0.0055, 0.0037/0.0058 and 0.0039/0.0068 at the three amplitudes (16 modes) and
0.0013/0.0029, 0.0015/0.0033 and 0.0017/0.0037 at a0 = 2.1, 2.4 and 2.7 (20 modes); the (B2-P) residuals of the same
states, with their own whole-plane inverse, are 0.76 to 0.83 (R_F/N_F) and 0.83 to 0.95 (R_G/N_G). At beta = 2.5
(12 modes, forced residuals 0.16 to 0.17/0.11) the sampled values decrease from eps = 0.0592 at a0 = 1.9 to 0.0588 at
a0 = 2.1. At beta = 3.5 (12 modes, forced residuals 0.012 to 0.013/0.022 to 0.025) the states at a0 = 2.4, 2.7 and 3.0
have eps = 0.058554, 0.058587 and 0.056732. With a second external dipole at beta = 3 (12 modes) the states at a0 = 7,
8, 10, 12, 15 and 20 have eps = 0.01771, 0.01837, 0.01755, 0.01600, 0.01377 and 0.01096, again with a sampled maximum
among the evaluated amplitudes; the independently evaluated forced residuals of the states at a0 = 7, 8 and 10 are
0.012 to 0.016/0.019 to 0.025 and at a0 = 12, 15 and 20 are 0.017/0.027, 0.019/0.030 and 0.020/0.032, and their (B2-P)
residuals are 0.91 to 1/0.95 to 0.99. At beta = 2.25 a state that the solver flagged as converged
(a0 = 1, eps = 0.042550) has forced residuals 0.79/0.37 on the independent evaluator; solver convergence flags are
therefore not used as evidence.
A continuum forced branch, a turning point of it and a controlled bound on eps have not been validated. A turning
point of this homotopy at fixed beta is a property of the homotopy and carries no information about existence. With a0
fixed and beta free instead, the first stage (eps = 0.02) gives beta = 2.504 with forced residuals 0.15/0.12; it is an
approximate forced fit, not a converged root; the next stages (eps = 0.025, beta = 2.4402, and eps = 0.03,
beta = 2.3886) have forced residuals 0.19/0.14 and 0.23/0.16 and (B2-P) residuals 0.86/0.54 and 0.88/0.61 on the
independent evaluator (all inverse flags zero), the stage eps = 0.035 (beta = 2.3465) has 0.30/0.20 and 0.89/0.68, and
the stage eps = 0.04 (beta = 2.3119) has 0.41/0.24 and 0.90/0.75. A second beta-free path adds a source f to the
vorticity in the transporting field, W = beta X + U_rel[Omega + lambda f], with a0 fixed and lambda decreasing from 1
to 0 (where the problem is (B2-P)). At lambda = 1 the stored starting state is not an exact root: it has the residual
of the fitted seed from which f was built. The present implementation also re-projects f onto the fit basis when beta
changes, so the physical source is not exactly fixed along the path. Its state at lambda = 0.97
(beta = 3.0035, a0 = 1.0116), evaluated independently on 96 angles and 145 radii from 1e-5 to 1e8 (Table 6.1d), has
maxima R_F/N_F = 0.036 and R_G/N_G = 0.050 for the forced problem with the intended fixed source, and 0.75 and 0.48
for (B2-P) with its own whole-plane inverse; the source coefficients used at run time were not saved, so the first
pair is not the residual of the problem the solver actually solved, and that run is not fully reproducible. Restarted
versions that keep the source exactly fixed in the seed basis (exponent 3.0; this also freezes the exponent of the
represented tail while beta varies) reach beta = 3.0019 with 12 and beta = 3.0020 with 16 angular modes at
lambda = 0.99; on the independent evaluator (96 angles, radii from 1e-5 to 1e8) their sampled maxima are 0.037/0.051
and 0.0060/0.011 for the forced problem (the effective source reproduced exactly) and 0.75/0.49 and 0.75/0.48 for
(B2-P). At lambda = 0.98 (beta = 3.0027 with 12 and 3.0029 with 16 modes) the values are 0.036/0.050 and 0.0063/0.010
(forced) and 0.75/0.49 and 0.75/0.47 ((B2-P)); at lambda = 0.97 and 0.96 (beta = 3.0037 and 3.0061, 12 modes) they are
0.036/0.050 and 0.035/0.050 (forced) and 0.75/0.48 and 0.74/0.48 ((B2-P)); at lambda = 0.97 and 0.96
(16 modes, beta = 3.0038 and 3.0060) they are 0.0061/0.0094 and 0.0063/0.0086 (forced) and 0.75/0.47 and 0.75/0.46
((B2-P)). For these two 16-mode stored temperatures, written Theta = x^2 F, an exact certificate in rational
arithmetic on the stored binary coefficients (lower bounds by Bernstein coefficients on a finite subdivision of the
closed rectangle of (t, eta), eta = -sin theta, with 101 and 109 positive leaves) proves F > 0 and 2F + x F_x > 0 on
R^2; hence Theta > 0 off the axis and Theta_x > 0 on {x > 0} for these stored fields. Neither run was continued beyond
lambda = 0.96.
Versions in which the unknown fields are stored with b_rep = beta (the source still fixed in its seed basis, exponent
3.0) reach, with 16 angular modes, beta = 3.0020, 3.0029, 3.0038, 3.0046 and 3.0060 at lambda = 0.99, 0.98, 0.97,
0.965 and 0.96; on the independent evaluator their sampled maxima are 0.0059/0.011, 0.0061/0.010, 0.0062/0.0094,
0.0060/0.0090 and 0.0060/0.0086 for the forced problem and 0.75/0.48, 0.75/0.47, 0.75/0.47, 0.75/0.47 and 0.75/0.46
for (B2-P) (with 12 modes at lambda = 0.99: beta = 3.0018, 0.037/0.051 and 0.75/0.49; with 24 modes and the same 56
radial cells at lambda = 0.96 and 0.955: beta = 3.0060 and 3.0082, forced maxima 0.00041/0.00066 and 0.00039/0.0014,
and (B2-P) maxima 0.75/0.46 and 0.74/0.46; at lambda = 0.96, from 16 to 24 modes the forced maxima fall by factors of
about 15 and 13 while the (B2-P) maxima are unchanged to the digits shown; at lambda = 0.95 the 24-mode step, which
the acceptance rule of the computation rejected, gives beta = 3.0114 and forced maxima 0.0015/0.0043, and the 32-mode
continuation from the 24-mode state at 0.955 gives beta = 3.0114 and forced maxima 0.00025/0.00086, both with (B2-P)
maxima 0.74/0.46). For each of these ten stored pairs the self-interaction coefficient E_T of the expansion below is
exactly nonzero (at theta = 0 and without its positive factor L^{1+3 s_rep}, rounded: -0.0526 for the 12-mode state,
0.746, 11.8, 14.5, 14.0 and 13.7 for the 16-mode states, 13.3, 12.2 and 11.8 for the 24-mode states and 9.82 for the
32-mode state), so the absolute temperature residual of (B2-P) is unbounded (growth r^{1-3/beta}); the forced residual
also contains a term of the distinct positive order r^{2/3-2/beta} coming from the source, whose basis exponent
differs, and is also unbounded. Continued from the 32-mode state at lambda = 0.95, the 32-mode state at lambda = 0.945
(accepted by the acceptance rule; beta = 3.0163) has forced maxima 0.00069/0.0021 and (B2-P) maxima 0.74/0.46, and the
32-mode step to lambda = 0.94 (rejected by that rule; beta = 3.0239) has 0.0036/0.0074 and 0.74/0.45; a 40-mode solve
at lambda = 0.95, started from the 32-mode state at lambda = 0.95 with a changed strain tolerance, kept its stored
beta = 3.0114 (the stored 24-mode value differs by 2.1e-6), with forced maxima 0.00024/0.00032 and (B2-P) maxima
0.74/0.46 (all on the independent evaluator; for these three states the exact
rational tail computation of the verification gives exactly nonzero temperature tail coefficients of the positive
order r^{1-3/beta}, so their absolute temperature residuals are unbounded). At lambda = 0.95 the independent
verification compared the 24-, 32- and 40-mode states (same source, 56 radial intervals) at 61 common radii from 1e4
to 1e8 on three angular grids of up to 2982 points: with the envelope r^{1+1/beta}, the largest discrepancy of G =
Omega/x, divided by the largest enveloped value of the finer state, is 0.0040 (24 to 32 modes) and 0.00028 (32 to 40
modes), and that of the angular derivative of G is 0.036 and 0.0031 (reductions by factors 14.7 and 11.8; normalized
radius by radius, the 32-to-40 derivative value is 0.0039). This is a finite sampled refinement at fixed forcing: it
is not a convergence proof, the stored upper-axis slopes (95.42, 95.82, 95.85) are not the transported axis
functional, and it concerns the forced problem only. Continuing the 40-mode states along the path, lambda = 0.945
(beta = 3.0163) and 0.94 (beta = 3.0239) give forced maxima 0.00025/0.00094 and 0.00069/0.0026 and (B2-P) maxima
0.74/0.46 and 0.74/0.45 on the independent evaluator (the largest absolute (B2-P) Cartesian temperature residual on
the sampled grid of the second is 178.4, and both have exactly nonzero temperature tail coefficients of positive order,
so their absolute temperature residuals are unbounded); the same 32-to-40 comparison gives 0.0017 and 0.0051 for G
and 0.015 and 0.040 for its angular derivative at lambda = 0.945 and 0.94, against 0.00028 and 0.0031 at 0.95, so the
angular discrepancy between the two resolutions grows along the path. An equal-count comparison at lambda = 0.95
controls the number of iterations: from one common seed (the 24-mode state at lambda = 0.955, transplanted to 32 and
40 modes), with beta = 3.0113961 and lambda prescribed, 56 radial intervals, the same solver settings and exactly 20
evaluations of the inner map at each of 24, 32 and 40 angular modes (the angular count of the fit changing with them;
none of the three runs met the convergence criterion of the solver), the final values of the fit objective are in the
ratios 49.8 (24 to 32 modes) and 4.61 (32 to 40 modes), and 66.4 and 5.77 per residual point, and each of them stays
within 5 percent of its final value from evaluation 10, 16 and 16 on. On the independent evaluator the three final
states have forced maxima 0.0015/0.0043, 0.00025/0.00086 and 0.00024/0.00032 and (B2-P) maxima 0.74/0.46, C2 in
[-4384.234, -4384.233], [-4384.068, -4384.067] and [-4384.048, -4384.047], and exactly nonzero temperature tail
coefficients of positive order, so their absolute temperature residuals are unbounded. At equal evaluation count the
differences of the fit objectives between the resolutions persist, so they are not explained by a longer iteration
history at the finer resolutions; equal evaluation counts are not equal computational budgets, and the comparison does
not establish the smallest residual attainable at a given resolution.
A 32-mode run with beta fixed per stage and lambda solved (the fit-growth multiplier set to 1e9), continued from the
32-mode state at lambda = 0.945, gives lambda = 0.940011, 0.936736, 0.934345, 0.932636 and 0.931684 at
beta = 3.023855, 3.0315, 3.04, 3.05 and 3.062, with forced maxima 0.0036/0.0074, 0.0096/0.018, 0.020/0.037,
0.040/0.067 and 0.068/0.11 and (B2-P) maxima 0.73 to 0.74/0.45 (0.73/0.74 at beta = 3.062) on the independent
evaluator, and exactly nonzero temperature tail coefficients of positive order at each of these states. Beta and
lambda change together at fixed resolution, so this is not a convergence comparison, and the growth of the forced
maxima shows that the accuracy of these forced fits deteriorates; these states alone do not tell whether the
resolution or the nonlinear convergence is the cause. The shrinking decrements of lambda suggest that lambda(beta)
levels off near 0.93 on this branch of the forced family; at this resolution that is not established, and it says
nothing about the forcing-free problem. A 40-mode run of the same kind, started from the 40-mode state at
lambda = 0.94, gives at beta = 3.0315 and 3.04 lambda = 0.936737 and 0.934345, which differ by 6e-8 and 2e-8 from the
32-mode values, forced maxima 0.0024/0.0056 and 0.0063/0.015 against 0.0096/0.018 and 0.020/0.037 with 32 modes, the
same (B2-P) maxima 0.74/0.45 and 0.73/0.45 on the independent evaluator, and exactly nonzero temperature tail
coefficients of positive order (so their absolute temperature residuals are unbounded). At each of these two values of
beta the two runs share the source and the seed basis but not their initial and stopping histories, so these are
finite comparisons at two values of beta; they establish neither a limit as the resolution increases nor the levelling
of lambda(beta). Continued from its state at beta = 3.04, the 40-mode run gives at beta = 3.05 lambda = 0.932636,
which differs by -1.0e-7 from the 32-mode value, forced maxima 0.014/0.036 against 0.040/0.067 with 32 modes, the same
(B2-P) maxima 0.73/0.45 on the independent evaluator, exactly nonzero temperature tail coefficients of positive order,
and C2 in [-4870.395, -4870.394] against [-4821.233, -4821.232] with 32 modes (a difference of 1.0 percent); the
larger of its (B2-P) maxima of R_F/N_F and R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8 is
0.61, 0.46 and 0.287 (0.61, 0.46 and 0.421 for the 32-mode state in the same evaluation), and it is not among the 73
states of the regional comparison below. This is a third finite comparison, with the same limitations. Continued from
its state at beta = 3.05, the 40-mode run gives at beta = 3.062 lambda = 0.931684, which differs by 2.4e-8 from the
32-mode value, forced maxima 0.029/0.077 against 0.068/0.11 with 32 modes, (B2-P) maxima 0.73/0.58 against 0.73/0.74
with 32 modes on the independent evaluator (both vorticity maxima are attained beyond r = 300), exactly nonzero
temperature tail coefficients of positive order, and C2 in [-5096.426, -5096.425] against [-4979.108, -4979.107] with
32 modes (a difference of 2.4 percent); the larger of its (B2-P) maxima of R_F/N_F and R_G/N_G on the intervals from r
= 3 to 30, 30 to 300 and 300 to 1e8 is 0.61, 0.46 and
0.58 (0.61, 0.46 and 0.74 for the 32-mode state in the same evaluation), and it is not among the 73 states of the
regional comparison below. This is a fourth finite comparison, with the same limitations; along these four values of
beta the relative difference of the two C2 enclosures, 100 |c_40 - c_32|/|c_32| for c_K in the enclosure of the K-mode
state, is 0.1, 0.4, 1.0 and 2.4 percent while the two values of lambda differ by at most 1.1e-7, and no cause of the
C2 difference is inferred. The independent verification also compared the stored 32- and 40-mode fields at these four
values of beta on a common grid of 224 radii from 1e-6 to 1e8 and three angular grids of up to 3083 points (identifier
E542). For H = G = Omega/x and for H = d_phi G (the angular derivative), let d_H(r) be the maximum over the sampled
angles of |H_40 - H_32| at the radius r divided by the maximum over the sampled angles of |H_40| there (no denominator
floor; no zero denominator occurred). The largest value of d_H over the sampled radii is 0.010, 0.016, 0.025 and 0.034
for H = G and 0.068, 0.097, 0.13 and 0.16 for H = d_phi G, all attained at the largest sampled radius; with the same
definition, the derivative value for the 32- and 40-mode states at lambda = 0.95 is 0.0039. These are finite sampled
distances between stored forced fields, not residuals of (B2-P) and not a refinement limit; along the path the
far-field agreement of the two resolutions degrades while their values of lambda stay within 1.1e-7 of each other. In
the area L2 norm over the whole plane, the relative distance ||H_40 - H_32||/||H_40|| at the same four values of beta
is 0.0016, 0.0033, 0.0061 and 0.011 for H = G and 0.027, 0.048, 0.076 and 0.11 for H = d_phi G (exact rational
enclosures, identifier P187, for the fields defined by the stored coefficients with exact powers and unclipped splines
on a common regenerated knot vector, not for the floating-point evaluation used in the computation); these distances
are of the stored G, not of Omega or of any residual, and increase along the path.
Continued from its state at beta = 3.062, the 40-mode run gives at beta = 3.076, where no 32-mode state was computed,
lambda = 0.931657 (2.7e-5 below its value at beta = 3.062), forced maxima 0.056/0.12,
(B2-P) maxima 0.73/0.95 on the independent evaluator (the vorticity maximum is attained beyond r = 300), exactly
nonzero temperature tail coefficients of positive order, and C2 in [-5289.577, -5289.576]; the larger of its (B2-P)
maxima of R_F/N_F and R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8 is 0.60, 0.46 and 0.95, and
it is not among the 73 states of the regional comparison below. Its forced maxima exceed those of the 40-mode state at
beta = 3.062 by factors of 1.9 and 1.6, so the accuracy of the 40-mode fits also deteriorates along the run. The next
stage of the same run, at beta = 3.092, gives lambda = 0.932671, 1.0e-3 above its value at beta = 3.076, forced maxima
0.088/0.15, (B2-P) maxima 0.72/0.97 (the vorticity maximum again beyond r = 300), exactly nonzero temperature tail
coefficients of positive order and C2 in [-5279.508, -5279.507]; the larger of its (B2-P) maxima of R_F/N_F and
R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8 is 0.60, 0.46 and 0.97. Its forced maxima exceed
those at beta = 3.076 by factors of 1.6 and 1.3. The sampled 40-mode values of lambda thus decrease from beta = 3.05
to 3.076 and increase from 3.076 to 3.092; since these fits deteriorate along the run and no 32-mode states exist at
the last two values, this is not evidence of a turning point of a continuum branch. The 40-mode state at beta = 3.076
was transplanted to 48 angular modes (96 residual angles, the same source and 56 radial intervals) and continued at
beta = 3.076 and 3.092. At beta = 3.076 the stage accepted the inherited lambda = 0.931657 after 11 inner iterations
that changed the fields (the discrete fit objective fell from 2700 to 621), so this value of lambda is not a new
determination; at beta = 3.092 five secant steps gave lambda = 0.932670, 4.8e-7 below the 40-mode value (fit objective
8743 with 40 and 2530 with 48 modes). On the independent evaluator these two 48-mode states have forced maxima
0.010/0.025 and 0.020/0.042, smaller than with 40 modes by factors of 3.6 to 5.4, and (B2-P) maxima 0.73/0.46 and
0.72/0.70; the larger of their (B2-P) maxima of R_F/N_F and R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and
300 to 1e8 is 0.60, 0.46 and 0.30 at beta = 3.076 and 0.60, 0.46 and 0.70 at beta = 3.092, so the (B2-P) vorticity
maxima beyond r = 300 of the 40-mode states (0.95 and 0.97) change substantially with the angular resolution. In exact
rational arithmetic the limit of the normalized (B2-P) temperature residual at the center is 1.6e-6 and 9.9e-8
(exactly nonzero; the center strain of the inverse of their own vorticity differs from 1 + beta/2 by
1.7e-6 and -1.1e-7), their temperature tail coefficients of positive order are exactly nonzero (so their absolute
temperature residuals are unbounded), and C2 lies in [-5465.884, -5465.883] and [-5705.298, -5705.297], larger in
magnitude than for the 40-mode states by 3.3 and 8.1 percent. The increase of the sampled lambda from beta = 3.076 to
3.092 is thus reproduced with 48 modes to within 1e-6, with the value at 3.076 inherited; this is a finite comparison
of two discretizations of the forced family, with fits that remain far from small residuals, not a continuum or fold
statement, and neither state is among the 73 states of the regional comparison below. A second 48-mode run, started
from the 48-mode state at beta = 3.092, solved beta = 3.076 and then 3.062 by four secant steps each. At beta = 3.076
it gives lambda = 0.931658, 5.7e-7 above the 40-mode value (here lambda is determined by the run; fit objective 621
against 2700 with 40 modes), and at beta = 3.062 lambda = 0.931683, 7.2e-7 below the 40-mode and 7.0e-7 below the
32-mode value (fit objectives 122, 702 and 3370 with 48, 40 and 32 modes). On the independent evaluator these two
states have forced maxima 0.010/0.025 and 0.0044/0.012 and (B2-P) maxima 0.73/0.46 and 0.73/0.45; at beta = 3.076 the
forced and (B2-P) maxima agree with those of the first 48-mode state to three digits. The larger of their (B2-P)
maxima of R_F/N_F and R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8 is 0.60, 0.46 and 0.30 at
beta = 3.076 and 0.61, 0.46 and 0.29 at beta = 3.062 (0.61, 0.46 and 0.58 for the 40-mode state at 3.062). In exact
rational arithmetic the limit of the normalized (B2-P) temperature residual at the center is 8.4e-6 and 3.6e-7
(exactly nonzero; the center strain of the inverse of their own vorticity differs from 1 + beta/2 by 9.0e-6 and
-3.9e-7), their temperature tail coefficients of positive order are exactly nonzero (so their absolute temperature
residuals are unbounded), and C2 lies in [-5465.870, -5465.869] and [-5159.298, -5159.297] (at beta = 3.062 larger in
magnitude than for the 40-mode state by 1.2 percent). The stored 48-mode values of lambda at beta = 3.062, 3.076 and
3.092 (0.931683, 0.931658 and 0.932670) are smallest at 3.076, as are the 40-mode values; this is a finite comparison
of stored stage values of fits that remain far from small residuals, with acceptance flags that are not error bounds,
not evidence of a turning point or a fold, and neither state is among the 73 states of the regional comparison below.
A second path of the same kind (family L2 of Table 6.1e) starts from a different seed: the eps = 0 state for an
external Gaussian dipole centered at y0 = 2.5 (24 angular modes, fit error 7.9e-5), rescaled to a0 = 1, so that its
fixed source carries most of the center strain (equal lambda therefore does not mean equal forcing on the two paths).
Its first state, at lambda = 0.99, has beta = 3.0867, forced maxima 0.00025/0.00026 and (B2-P) maxima 0.74/0.42 on the
independent evaluator, exactly nonzero temperature tail coefficients of positive order (so its absolute temperature
residuals are unbounded) and C2 in [-425.908, -425.907]. The larger of its (B2-P) maxima of R_F/N_F and R_G/N_G
decreases with the radius (0.31, 0.16 and 0.099 on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8, below the
values of the other 72 states of the regional comparison below); it is not a candidate. The next stage of this path,
at lambda = 0.98, failed: none of the seven computed inner states reported there met the center-strain condition. The
one saved state of that stage (beta = 3.0415, not accepted) was evaluated independently: the center strain of its
transporting velocity (own vorticity plus lambda times the source) is 2.49183 against the required 2.52077 (two
independent inverses agree to 2.5e-8); its forced maxima are 0.027/0.0094 and its (B2-P) maxima 0.75/0.42, its
temperature tail coefficients of positive order are exactly nonzero, and C2 lies in [-228.011, -228.010] (Table 6.1e).
The seven inner states of that stage were then recomputed and stored at beta = 2.8323, 3.0415, 3.0867, 3.1066, 3.1167,
3.2067 and 3.4734; these fixed values are within 5.1e-5 of the corresponding logged sample values, and none of the
recomputed states was accepted. The center strain c of a stored velocity is a linear expression in the stored
coefficients (only the angular modes 1 and 3 and the integrals of the B-splines enter); evaluated in exact rational
arithmetic on the stored binary values, the mismatch m = c - (1 + beta/2) of the transporting velocity of these seven
states is -0.135, -0.0289, -0.0290, -0.0310, -0.0324, -0.0561 and -0.206 respectively (each enclosed in an interval of
width 1e-15), and their temperature amplitude a at the center is positive, so the divided temperature residual at the
center, -2 m a, is nonzero and none of them meets the center-strain condition; with the own vorticity alone
(the unforced problem) m lies between -2.10 and -1.91.
Negative values of m at finitely many values of beta do not exclude a root between them, and no fold of the forced
family is inferred.
The second path was then continued from its first state at the same resolution (24 angular modes), with beta
prescribed at each stage and lambda solved from the center-strain condition. The stored states at beta = 3.088, 3.09,
3.0925, 3.095, 3.1, 3.105, 3.11, 3.12, 3.14, 3.17, 3.2 and 3.25 have lambda = 0.99, 0.989987, 0.989975, 0.989975,
0.989983, 0.990022, 0.990085, 0.990279, 0.990904, 0.992326, 0.994211 and 0.998139; evaluated in exact rational
arithmetic on the stored binary values, the center-strain mismatch of their transporting velocity lies between -7.2e-6
and 1.3e-5. Among these twelve states, the smallest stored value of lambda, 0.989975, is attained at beta = 3.0925 and
3.095 (equal values that are outcomes of the acceptance tolerance), and the stored values are larger on both sides.
This is numerical evidence for a sampled minimum of lambda near (beta, lambda) = (3.095, 0.98997) on this computed
24-mode forced branch, and nothing more: finite samples do not show that the stored states lie on one continuous
branch, do not exclude roots of the center-strain condition between the sampled values of beta, and do not establish a
fold (no validated error for lambda, no resolution study establishing the sampled minimum and no nondegeneracy proof
are available). A finite-difference Jacobian of the inner fixed-point map, on the 1332 active coefficients of one
further stored state of this branch near the sampled minimum, at (beta, lambda) = (3.0952, 0.989973) with 24 angular
modes (forward differences with step 1e-6), gives the following linearized diagnostics: the smallest singular value of
J_T - I is 0.034 in coefficient space and 0.015 in the full-plane weighted L2 metric of the corresponding
perturbations of G = Omega/x, with weight r^{1/4} + r^{-1/4} (condition numbers 253 and 2111), the spectral radius of
J_T is 0.43, and the finite-difference linear-response estimates of the derivatives of the center-strain mismatch
obtained from it are 2.87 with respect to lambda and 2.1e-4 with respect to beta. No bound on the finite-difference
error is available, and these values establish no contraction, no exact fixed point, no differentiable branch and no
fold. The stored state, the definition of the map, the frozen finite-difference matrix, the weighted metric and the
independent check of the matrix are recorded under identifier P208; the two derivative estimates were also recomputed
independently from the frozen matrix (identifier P216). The same finite-difference Jacobian was formed at the 24-mode
state of the first path at lambda = 0.96 (beta = 3.0060478, a0 = 1.011258; the same 1332 active coefficients and the
same step). This stored state is not an exact fixed point: its inner defect has norm 2.29e-5 (largest entry 4.5e-6),
and its forced center-strain mismatch is +4.93e-5, accepted under the tolerance 5e-5 of that run. The smallest
singular value of J_T - I is 0.0069 in coefficient space (condition number 4229) and 0.0037 in the full-plane weighted
L2 metric above (condition number 22497). The spectral radius of J_T is 1.85, with two eigenvalues of modulus greater
than 1, so the stored Picard linearization is unstable at this state, while the Anderson-accelerated run that produced
the state met its stopping criteria; the actual derivative of the map and the reason for the convergence of that run
are not established. The linear-response estimates of the derivatives of the mismatch are 0.965 with respect to lambda
and 2.83 with respect to beta, so the linearized tangent dlambda/dbeta of the zero set of the mismatch is -2.93 (the
centred secant of the stored path, -2.83, uses an endpoint computed with 16 modes and transplanted to 24, so it mixes
resolutions), and the linear responses of the fixed point to lambda and to beta have norms 1045 and 311, against 151
and 53 at the state of the second path. With the column of the derivative of the map with respect to beta and the row
of the mismatch added to J_T - I, the smallest singular value is 0.0063, against 3.7e-6 for the same augmented matrix
at the state of the second path (identifier P216): the nearly singular augmented direction found there is much weaker
here, which is consistent with the sampled minimum of the computed lambda(beta) of the second path but establishes no
stationary point. The singular direction of the smallest singular value of J_T - I has 44 percent of its squared
coefficient norm on the last three radial coefficients (a statement about coefficients, not a localization in the
plane), and the direction generated by the dilations of G is not a near-null direction (with a0 and the source fixed,
the forced problem has no dilation symmetry). The two states have different sources and amplitudes, so the comparison
does not isolate the effect of the sampled minimum. These are linearized diagnostics of two stored forced states
without error bounds; they establish no root, branch, fold or error bound and say nothing about (B2-P). The frozen
matrix and its independent check are recorded under identifier P234, the repaired statements under identifiers P241
and P244.

For (B2-P), the same exact center computation, with the inverse of each state's own vorticity (whose center strain
falls short of 1 + beta/2 by about 1.9), gives for each of the twelve stored fields at beta = 3.088 to 3.25 a limit of
the normalized temperature residual at the center, along points off the axis, of approximately 0.606 (beta = 3.25) to
0.636 (beta = 3.088); so the normalized (B2-P) temperature residual of each of them exceeds 3/5 near the center, and
none is a profile. Full regional evaluations of the states at beta = 3.105, 3.2 and 3.25 (Table 6.1e) give forced
maxima 3.1e-4/3.1e-4, 6.2e-4/7.1e-4 and 7.9e-4/1.5e-3, (B2-P) maxima 0.74/0.42, 0.73/0.41 and 0.72/0.41, exactly
nonzero temperature tail coefficients of positive order (so their absolute temperature residuals are unbounded) and C2
in [-517.428, -517.427], [-1243.684, -1243.683] and [-1871.948, -1871.947]; the larger of their (B2-P) maxima of
R_F/N_F and R_G/N_G is 0.31, 0.16 and 0.097 (beta = 3.105), 0.31, 0.15 and 0.089 (beta = 3.2) and 0.31, 0.14 and 0.086
(beta = 3.25) on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8. These three states are not among the 73
states of the regional comparison below. At beta = 3.3 the continuation stored no accepted state: the values of lambda
requested by the solver (1.002067 and 1.002834) were clipped to 1, and the run was stopped. The two saved intermediate
evaluations, at lambda = 1 and 0.999, are not exact roots of the forced center-strain condition (exact mismatch
-0.0120 and -0.0162) and, with their own vorticity, have a nonzero normalized (B2-P) temperature residual limit at the
center (0.598 for both), so neither is a profile; a clipped evaluation at lambda = 1 is not evidence that the branch
returns to lambda = 1, and nothing follows on roots at beta = 3.3 or on the continuation beyond 3.25. Two states of
this continuation were also computed with 32 angular modes: at beta = 3.0925, started from the 24-mode state and
accepted with its value lambda = 0.989975 after three inner iterations (so this value of lambda is not an independent
determination), and at beta = 3.085, continued from it (lambda = 0.990033). Evaluated in exact rational arithmetic,
their forced center-strain mismatch is -4.0e-7 and -7.8e-7, the center strain of the inverse of their own vorticity is
0.6426 and 0.6388 (against 1 + beta/2 = 2.54625 and 2.5425), and the limit of the normalized (B2-P) temperature
residual at the center is 0.635 and 0.637, above 3/5, so neither is a profile; at beta = 3.0925 these center values
differ from those of the 24-mode state by less than 1e-6. Their full regional evaluations (Table 6.1e) give forced
maxima 2.7e-4/2.8e-4 and 2.5e-4/2.5e-4, (B2-P) maxima 0.74/0.42 for both, exactly nonzero temperature tail
coefficients of positive order and C2 in [-453.408, -453.407] and [-417.563, -417.562]; the larger of their (B2-P)
maxima of R_F/N_F and R_G/N_G on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8 is 0.31, 0.16 and 0.098
(beta = 3.0925) and 0.31, 0.16 and 0.099 (beta = 3.085); neither is among the 73 states of the regional comparison
below. The stored fields of these two states and of the 24-mode state at beta = 3.0925 are not C^5: at the point of
the positive x-axis on each interior knot circle the fifth x-derivatives of Theta and of Omega are discontinuous
(exact arithmetic); this is a property of the representation, not used above, and says nothing about nearby smooth
fields. Two further 32-mode states, at beta = 3.1 and 3.11 (lambda = 0.989984 and 0.990085), computed in the
sequential continuation through beta = 3.0925, 3.085, 3.1 and 3.11, were evaluated at the center only, in exact
rational arithmetic: the center strain of the inverse of their own vorticity is 0.6464 and 0.6512
(against 1 + beta/2 = 2.55 and 2.555), the limit of the normalized (B2-P) temperature residual at the center is 0.634
and 0.632, above 3/5, so neither is a profile, and their forced center-strain mismatch is -1.2e-8 and -2.3e-6; no
regional evaluation was made for them. The 32-mode state at beta = 3.0925 was also transplanted to 40 angular modes
(80 residual angles, the same source) and continued to beta = 3.085 and 3.1 and from beta = 3.1 to 3.11 and 3.076: at
beta = 3.0925 the inherited lambda = 0.989975 was accepted after one inner iteration (again not an independent
determination), and at beta = 3.085, 3.1, 3.11 and 3.076 the solver gave lambda = 0.990033, 0.989983, 0.990085 and
0.990199. The stored values of lambda with 24, 32 and 40 modes lie within 3.3e-7, 5.3e-7 and 1.5e-7 at beta = 3.085,
3.1 and 3.11, and those with 24 and 40 modes within 5.2e-7 at beta = 3.076 (a finite comparison of stored values, not
a convergence result). Evaluated in exact rational arithmetic, the forced center-strain mismatch of these five 40-mode
states (beta = 3.0925, 3.085, 3.1, 3.11 and 3.076) is -4.0e-7, -7.8e-7, -1.4e-6, -1.9e-6 and -1.6e-6, the center
strain of the inverse of their own vorticity is 0.6426, 0.6388, 0.6464, 0.6512 and 0.6339, and the limit of the
normalized (B2-P) temperature residual at the center is 0.635, 0.637, 0.634, 0.632 and 0.639, above 3/5, so none of
them is a profile. Their independent regional evaluations (161 radii from 1e-5 to 1e8, 96 angles; Table 6.1e) give
(B2-P) maxima 0.741 to 0.746 and 0.418 to 0.420, forced maxima 2.2e-4 to 3.3e-4, exactly nonzero temperature tail
coefficients of positive order (so their absolute temperature residuals are unbounded) and C2 in [-453.408, -453.407],
[-417.562, -417.561], [-491.147, -491.146], [-544.647, -544.646] and [-376.874, -376.873]; at beta = 3.0925, 3.085 and
3.1 these lie within 1e-5 relative of the enclosures of the 56-interval states with fewer modes (the radial refinement
below changes C2 by more than 50 percent). None of these five states is among the 73 states of the regional comparison
below. The 40-mode state at beta = 3.085 was also transplanted to 48 angular modes (96 residual angles, the same
source) and continued at beta = 3.085 and 3.1: at beta = 3.085 the stage accepted the inherited lambda after one inner
iteration that left the vorticity coefficients unchanged and changed the temperature coefficients by at most 1.1e-8
(an evaluation, not a new determination), and at beta = 3.1 three secant steps gave lambda = 0.989984. With 24, 32, 40
and 48 modes the stored values of lambda lie within 3.3e-7 at beta = 3.085 and 5.3e-7 at 3.1 (unequal iteration
budgets and warm starts; a finite comparison of stored values, not a convergence result). In exact rational arithmetic
the limit of the normalized (B2-P) temperature residual at the center of these two 48-mode states is 0.637 and 0.634,
above 3/5, their forced center-strain mismatch is -7.8e-7 and -1.2e-8, and their temperature tail coefficients of
positive order are exactly nonzero; their independent regional evaluations give (B2-P) maxima 0.745/0.420 and
0.742/0.419, forced maxima 2.5e-4/2.5e-4 and 2.9e-4/3.0e-4, and C2 in [-417.562, -417.561] and [-491.150, -491.149].
Neither is among the 73 states of the regional comparison below. The 24-mode continuation was also run toward smaller
beta from its stored state at beta = 3.088, with the outer tolerance on the center-strain mismatch reduced to 5e-6:
the stored states at beta = 3.0865, 3.085, 3.083, 3.08, 3.076, 3.072, 3.066, 3.06, 3.05, 3.04, 3.02 and 3.0 have
lambda = 0.990016, 0.990033, 0.990060, 0.990112, 0.990199, 0.990311, 0.990527, 0.990808, 0.991438, 0.992313, 0.995066
and 0.999999, so the stored values of lambda increase as beta decreases from 3.0925 to 3.0 (the inner solves of the
stages at beta = 3.02 and 3.0 ended with inner residuals 1.1e-4 and 3.8e-5, above their tolerance 3e-5; the first
stopped by stagnation). At the next stage, beta = 2.95, the value of lambda requested by the predictor (1.0123) was
clipped to 1, and the run was stopped after ten inner iterations without a stage result; this stopped run gives no
conclusion on roots with lambda <= 1 at beta = 2.95. Evaluated in exact rational arithmetic, the forced center-strain
mismatch of these twelve states is nonzero and at most 3.1e-6 in absolute value, and the limit of the normalized
(B2-P) temperature residual at the center lies between 0.636 and 0.658, above 3/5, so none of these twelve fields is a
profile. The stored state at beta = 3.0 is close to, but not identical with, the seed of this path (which also has
beta = 3 and the same source): the largest differences of their stored coefficients of F = Theta/x^2 and G = Omega/x
are 1.6e-5 and 3.7e-5 (relative to the largest seed coefficient, 5.2e-6 and 1.1e-5), and at 4386 sampled points the
differences of Theta and of Omega reach 0.0090 and 7.5e-6 (sampled values, not suprema). Finitely many stored states
do not show that the continuation returns to the seed along one continuous branch. At beta = 3.085 the 24-mode and the
32-mode values of lambda differ by 3.3e-7, and the center strain of the inverse of the own vorticity, the center
limits of the normalized (B2-P) residuals and the forced center-strain mismatch of the two stored fields differ by
less than 1e-6; this is one comparison of two stored fields with different histories and stopping errors, not a
convergence result. No regional evaluation was made for these twelve states. Three states of the second path were also
computed with 84 instead of 56 radial intervals (24 angular modes), starting from a refit of the 56-interval state at
beta = 3.0925 on the new cells: at beta = 3.0925, 3.085 and 3.105 their stored values of lambda, rounded to six
digits, are 0.989975, 0.990033 and 0.990022, the same as for the 56-interval states at these values of beta (three
comparisons at two radial resolutions, not a convergence result). At beta = 3.0925 the 84-interval state was accepted
at the inherited value of lambda at the first outer step, after four inner iterations, so the equality there records
that acceptance and is not a new determination of lambda; at 3.085 and 3.105 the stored values differ from the
56-interval ones by -1.1e-7 and 9.1e-9. Evaluated in exact rational arithmetic, the forced center-strain mismatch of
the three 84-interval states is -8.2e-7, -1.4e-6 and -2.5e-6, the center strain of the inverse of their own vorticity
is 0.6426, 0.6388 and 0.6488 (against 1 + beta/2 = 2.54625, 2.5425 and 2.5525), and the limit of the normalized (B2-P)
temperature residual at the center is 0.635, 0.637 and 0.633, above 3/5, so none of them is a profile (their regional
evaluation is described below). The constant C2 of 4.26 (closed form below) is not stable under this radial
refinement: at beta = 3.0925 the exact enclosures are [-453.405, -453.404] for the 56-interval 24-mode state,
[-453.408, -453.407] for the 56-interval 32-mode state, [-525.074, -525.073] for the refitted 84-interval fields
before re-solving and [-693.980, -693.979] for the re-solved 84-interval state (changes of 15.8 and 53.1 percent
relative to the first), and the 84-interval states at beta = 3.085 and 3.105 give [-637.318, -637.317] and [-797.121,
-797.120] (against [-417.562, -417.561] for the 56-interval 24-mode state and [-417.563, -417.562] for the 56-interval
32-mode state at beta = 3.085, a change of 52.6 percent at the same angular resolution, and [-517.428, -517.427] for
the 56-interval 24-mode state at beta = 3.105). Two states recomputed with 56 radial intervals and 24 modes but
tighter tolerances (1e-5 for the inner iteration and 2e-6 for the center-strain mismatch), from the 56-interval state
at beta = 3.0925, have at beta = 3.0925 and 3.1 stored lambda differing from the earlier states by 0 (again the
inherited value, accepted after four inner iterations) and 3.4e-7, forced center-strain mismatch -1.6e-7 and -1.7e-7,
limits of the normalized (B2-P) temperature residual at the center 0.635 and 0.634, above 3/5, so neither is a
profile, and C2 in [-453.409, -453.408] and [-491.151, -491.150], against [-453.405, -453.404] and [-491.147,
-491.146] for the earlier states: in these stored fields C2 changes by less than 1e-5 relative under the tighter
tolerances, and by 52.6, 53.1 and 54.1 percent under the radial refinement at beta = 3.085, 3.0925 and 3.105.
Independent regional evaluations of the three 84-interval states and of the two tighter-tolerance states (Table 6.1e;
189 radii for the 84-interval states) give sampled normalized (B2-P) maxima 0.7415 to 0.7449 (temperature) and
0.4188 to 0.4200 (vorticity), forced maxima 1.6e-4 to 2.9e-4 and 1.6e-4 to 3.0e-4, and, on the intervals from
r = 3 to 30, 30 to 300 and 300 to 1e8, larger (B2-P) maxima of R_F/N_F and R_G/N_G of 0.31, 0.16 and 0.097 to 0.099;
their temperature tail coefficients of positive order are exactly nonzero, so their absolute temperature residuals are
unbounded. These are finite-grid diagnostics, not certified suprema or a convergence result, and these five states are
not among the 73 states of the regional comparison below.

Quadrature order of the computation's inverse. According to the run records, the earlier runs of the two paths above
used 12 Gauss points per radial quadrature cell in the computation's modal whole-plane inverse, which agrees with the
default of the code. The stored states do not record this setting, so this history is attributed to the run records
rather than certified from the stored coefficients. Six stored stages of the two paths (the 32-mode state at
beta = 3.062, the 40-mode states at 3.076 and 3.092, the 48-mode state at 3.092 and the 48-mode state of the second
48-mode run at 3.062 of the first path, and the 40-mode state of the second path at beta = 3.085) were restarted with
48 points for the unknown and for the fixed source, with the same discretization and source representation. Each
restart accepted its inherited lambda at the first secant step, with logged center-strain mismatches below 1.5e-6 in
absolute value; recomputed from the saved fields, the mismatches differ from the logged ones by up to 4.54e-7, and
that of the 40-mode state at beta = 3.092 is -1.57e-6. So no new value of lambda was determined and no shift of a root
is resolved. The fit objectives increased by 0.475 to 3.50 percent on the first path and by 0.027 percent on the
second; the sources are unchanged, every stored temperature changed, and so did every stored vorticity except that of
the second path (one inner iteration). On the independent evaluator (rows q48 of Table 6.1e) the six restarted states
have normalized (B2-P) maxima equal, to the three digits of Table 6.1e, to those of the original states, normalized
forced maxima within 5 percent of theirs, and, on the intervals from r = 3 to 30, 30 to 300 and 300 to 1e8, larger
(B2-P) maxima of R_F/N_F and R_G/N_G equal to two digits to the values quoted above for the five original states of
the first path (0.31, 0.16 and 0.099 for the state of the second path). In exact rational arithmetic their limits of
the normalized (B2-P) temperature residual at the center are nonzero (8.9e-8 to 1.4e-6 on the first path and 0.637 on
the second), their temperature tail coefficients of positive order are exactly nonzero (so their absolute temperature
residuals are unbounded), and C2 lies in [-5149.015, -5149.014], [-5514.655, -5514.654], [-6004.355, -6004.354],
[-5983.681, -5983.680], [-5140.086, -5140.085] and [-417.562, -417.561] (in the order listed): larger in magnitude
than for the original states by 3.4, 4.3, 13.7 and 4.9 percent for the 32-mode state, the two 40-mode states and the
48-mode state at beta = 3.092, smaller by 0.37 percent for the 48-mode state at 3.062, and unchanged on the second
path, whose vorticity did not change. None of the six is a profile, and they are not among the 73 states of the
regional comparison below. The computation reconstructs modal streams by interpolating their scaled values in the
compactified radius and restoring the radial factors before differentiation. The independent evaluator reconstructs
the full-plane inverse separately. For six stored forced states, namely the 32-mode states at beta = 3.062 and at
lambda = 0.95 (row blam32v_lambda0.95 of Table 6.1e), the 40-mode state at beta = 3.092, the 48-mode state at 3.092
and the 48-mode state of the second 48-mode run at 3.062 of the first path, and the 40-mode state of the second path
at beta = 3.085, the computation reports, at the eight radii r = 100, 1e3, ..., 1e9, the maximum M48, over 181 angles
of the half circle of radius r in {x > 0} and over both Cartesian components, of its relative velocity U = W - beta X
computed with 48 points, and the maximum D of the difference between its 48- and 12-point versions; the component
arrays were not stored with these maxima, and D has not been reproduced independently. At r = 1e9, D/M48 is 0.29,
0.019, 0.70, 0.79, 0.44 and 1.6e-4 (in the order listed), at r = 1e8 at most 0.024, and at r = 1e6 at most 1.2e-3. An
independent full-plane evaluation of the same relative velocity U_rel[Omega + lambda f] at the same angles (two
quadrature tolerances, agreeing to 1.2e-11 relative) gives maxima M for which |M48 - M|/M is 0.29, 0.058, 0.30,
0.31, 0.29 and 0.73 at r = 1e9; at r = 1e8 it is 0.0054 to 0.018 for the five states of the first path and 0.081 for
the state of the second path, at r = 1e7 at most 7.0e-4 and 5.1e-3, and at the radii from 100 to 1e6 at most 3.0e-5
and 1.6e-4. If the reported maxima and the independent evaluation are accurate, the 48-point velocity of the
computation therefore differs from the full-plane relative velocity by at least |M48 - M| at some sampled point of
that circle (reverse triangle inequality), and at least one of the two runtime orders differs from it by at least D/2
at a possibly different sampled point of that circle. A small difference between the two quadrature orders is thus no
bound on the error of either: for the state of the second path at r = 1e9, D/M48 is 1.6e-4 while the two maxima differ
by 73 percent. These are conditional numerical diagnostics, not error bounds, and their source (interpolation,
quadrature, implementation or provenance) is not determined. They concern later evaluations of the stored states with
the computation's velocity routine at the two quadrature orders: the forced residuals of Table 6.1e use the
independent inverse, so they are residuals of the intended forced problem, not of the discretized problem that the
computation solved.

Two redeterminations of one value of lambda. The 32-mode stage of the first path at beta = 3.062 was solved again for
lambda by the computation's scalar secant method, once with 12 and once with 48 Gauss points per radial quadrature
cell for the unknown and for the fixed source, with the same radial and angular representation and fixed source, apart
from the quadrature order, from the trial values lambda = 0.93171 (2.6e-5 above the stored value) and 0.93161, with a
mismatch tolerance of 1e-7 and an inner tolerance of 3e-6. In each run the first two center-strain mismatches have
opposite signs (2.59e-4 and -7.29e-4), two secant steps follow, and every inner solve reported convergence. The saved
values are lambda = 0.9316837662 with 12 points and 0.9316837838 with 48 points, 3.9e-9 below and 1.4e-8 above the
stored value 0.9316837702; recomputed from the saved fields, the forced center-strain mismatches are
4.2e-9 and 4.7e-9. The two values differ by 1.76e-8, which is 1.74 times the nominal tolerance scale 1.01e-8 (the
mismatch tolerance divided by the finite slope 9.88 of the first two trials, the same at both orders to three digits).
These are two computed finite secant states: the signs of the mismatches give no continuity, no enclosure of a root
and no convergence in the discretization, and the error of the inner solves in the mismatch is not bounded, so these
computations establish neither existence of exact discrete roots at both orders nor a difference between such roots.
On the independent evaluator (rows root12 and root48 of Table 6.1e) the two saved fields have sampled normalized
forced maxima 0.0678, 0.109 and 0.0677, 0.109 and normalized (B2-P) maxima 0.730, 0.744 at both orders. In exact
rational arithmetic their limits of the normalized (B2-P) temperature residual at the center are nonzero
(3.9e-9 and 4.4e-9), their temperature tail coefficients of positive order are exactly nonzero, so their absolute
temperature residuals are unbounded, and C2 lies in [-4979.102, -4979.101] and [-5148.985, -5148.984]. Neither is a
profile, and they are not among the 73 states of the regional comparison below.

Sign-changing sources at eps = 0. No external vorticity used above changes sign on {x > 0}. At eps = 0 the
transporting field W = beta X + U_rel[Omega_ext] is prescribed, with beta = 2 (c_in - 1) for the center strain c_in of
Omega_ext, and Theta and Omega are obtained by transport along backward characteristics from the center jet; the
transported vorticity has the center strain 1 + beta/2 required in (B2-P) if and only if its center strain c_out
equals c_in. Eighteen sign-changing sources Omega_ext = A x sum_i a_i exp(-(x^2 + (y - y_i)^2)/(2 s_i^2)) with two
lobes on the y-axis (a_1 = 1, a_2 < 0, A fixed by c_in; sixteen with c_in = 2.5, beta = 3, and two with c_in = 2.2 and
3.0) were computed with 16 angular modes. The results checked independently are these. For the pair antisymmetric in y
(a_2 = -1, y_2 = -y_1 = -2.87, equal widths) c_out = 0, by the additional symmetry y -> -y of the prescribed transport
(an exact parity argument, valid if every point is reached by a characteristic from the center and the strain integral
converges absolutely). For a weak negative lobe (a_2 = -0.03 at y_2 = -2, unit widths) and the positive lobe at
y_1 = 3.3 and 3.5, an independent evaluation with the literal Gaussian source gives c_out = 2.209 and 2.838 (the
computation, with a fitted source, gives 2.270 and 2.952), so c_out - c_in changes sign between these heights in both
evaluations; this is a numerical bracket for this family, not a computed strain-matched source, and neither a root nor
continuity in y_1 is established. In three configurations (a lobe a_2 = -0.3 of width 1.5 at y = 0 with the positive
lobe at y_1 = 2.87 or 3, and a narrow positive lobe of width 0.7 at y_1 = 3 with a_2 = -0.1 at y = -2) the computation
gave negative values of G = Omega/x at some sampled points (most negative reported values -0.018, -0.014 and -0.0099).
Independent transport of the gradient of Theta along the characteristics of the literal source gives positive G at
these points (0.025, 0.024 and 0.076), and the negative values are reproduced (-0.018, -0.014 and -0.010) when, as in
the computation, the temperature is first fitted with 16 angular modes on 12 sampled angles; on that sampling the fit
matrix has rank 519 on its 691 active coefficients (exact), so a 172-dimensional space of coefficient perturbations
vanishes at every sample, and such perturbations can change Theta_x. These negative values are therefore outputs of
the fitted map, not values of the transport of the literal source, and the positive values are numerical evidence at
these points only, not a sign statement on the plane. For the source with a_2 = -0.3 of width 1.5 at y = 0 and the
positive lobe at y_1 = 4 the transport was incomplete (backward trajectories of the computation did not reach the
center), and for the literal source of that configuration an exact certificate in rational arithmetic shows two
further zeros of W_2(0, .), a repelling one in (-6.681, -6.680) and a saddle in (-1.884, -1.883), so some backward
trajectories never reach the center. No strain-matched sign-changing source was constructed and no third path was
started; this is a coarse sample of two-lobe sources on the y-axis at one discretization, not an exclusion of
sign-changing profiles.

Stored representation. The states of the following paragraph are stored, on {x >= 0} with
phi = theta + pi/2 (so that cos(k phi) = T_k(-sin theta)), as
  Theta = x^2 sum_{k<K} f_k(r) cos(k phi),   Omega = x sum_{k<K} g_k(r) cos(k phi),
  f_k = (1 - t)^{b_rep+2} rho_k(r) sigma^F_k(t),   g_k = (1 - t)^{b_rep+1} rho_k(r) sigma^G_k(t),
  t = 1 - (L^2/(L^2 + r^2))^{1/(2 b_rep)} in [0, 1),
with rho_k = 1 for even k and rho_k = r (L^2 + r^2)^{-1/2} for odd k, and sigma^F_k, sigma^G_k clamped splines of
degree 5 in t whose coefficients are stored; the knots are not stored explicitly but are determined by the stored cell
count N_t and grading exponent g: the cell edges are the double-precision values of (i/N_t)^g, i = 0, ..., N_t, simple
in the interior and of multiplicity 6 at t = 0 and t = 1. The basis exponent b_rep (fixed for each state, and possibly
different from the state's beta) and the radial scale L are stored parameters; s_rep = 1/b_rep. Values and derivatives
of the splines at t = 1 are one-sided limits from the last cell. With z = 1 - t one has z^{b_rep} = L (L^2 + r^2)^{-1/2},
so beyond the last interior knot the stored fields are finite sums of powers of z times these factors and expand at
infinity in powers r^{-j s_rep - 2n}. Constants computed from a stored field are written C_rep and alpha_rep. If a
stored field were an exact class A profile with beta = b_rep, uniqueness of its asymptotic expansion would identify
them with the C of 4.26 and the alpha of 4.27, and the necessary conditions 4.26(c) and 4.27(c) would force C_rep = 0,
respectively alpha_rep = 0. (Exact profiles with finitely many angular modes are already excluded by 4.24; the checks
below diagnose additional radial restrictions.)
An exact expansion of this representation at infinity shows that the temperature residual R_Theta of a stored state
continued to the whole plane is
  2 (1 - beta s_rep) L^{1+2s_rep} r^{1-2s_rep} H_0(theta) + L^{1+3s_rep} r^{1-3s_rep} E_T(theta) + O(r^{1-4s_rep})
for the velocity of the state's own vorticity. The transporting velocity of a forced problem whose source is stored
with the same basis exponent b_rep gives an expansion of the same form, with the source contribution included in E_T;
a source stored with a different exponent adds further powers (for the states above stored with b_rep = beta, the
term of order r^{2/3-2/beta}). H_0 and E_T are trigonometric polynomials determined by the endpoint values and slopes
of the radial splines (for E_T, those of the vorticity that generates the velocity), and their nonvanishing was
decided in exact rational arithmetic on the stored coefficients.
For both lambda = 0.99 states (b_rep = 3, beta != 3) H_0 is not identically zero, so their absolute temperature
residuals, for (B2-P) and for the forced problem, are unbounded (growth r^{1/3}); along the positive x-axis
|R_Theta|/N_Theta and |R_Omega|/N_Omega tend to 6.2e-4 and 3.1e-4 (12 modes) and 6.6e-4 and 3.3e-4 (16 modes). For
the beta = 3.5 state at a0 = 3.0 (b_rep = beta) the second coefficient is not identically zero and the absolute
temperature residual grows like r^{1/7}; for the beta = 3 states with 20 modes at a0 = 2.4 and 2.7 (b_rep = beta = 3)
it tends to a nonzero angular profile. These are properties of the stored representations, not of the problem: a
state stored with b_rep != beta and H_0 not identically zero cannot be an exact profile, and for 2 < beta < 3 a state
stored with b_rep = beta can be exact only if C_rep = 0, and for beta = 3 a state stored with b_rep = 3 only if
alpha_rep = 0. The four beta-free states at eps = 0.025, 0.03, 0.035 and 0.04 are stored with b_rep = beta exactly.
The constant C_rep = (0, C2) of the velocity of each state's own vorticity has a closed form for the stored
representation (valid for 2 < b_rep < 3): C2 = -b_rep L^2 B / [2(b_rep - 1)(b_rep - 2)] with
B = S'(0) - (b_rep - 2) S(0) + int_0^1 (1-t)^{2-b_rep} S''(t) dt, where S is the first cosine coefficient of the stored
source and L the stored radial scale. On each spline cell the integral is a finite sum of rational multiples of powers
v^{3-b_rep+j}, and enclosing these powers by rational series bounds with explicit remainders gives, in exact rational
arithmetic on the stored binary coefficients and the resulting knots, C2 in [-6.308, -6.307], [-7.224, -7.223], [-8.299, -8.298]
and [-9.450, -9.449] for eps = 0.025, 0.03, 0.035 and 0.04 (no floating-point value is trusted; these agree with
a separate floating-point inverse; the exact inputs, their hashes and the certificate intervals are kept in the
working archives, section 8). Hence C_rep != 0, and 4.26(c) shows that none of these stored fields is the vorticity of a
class A profile, that is, their residuals cannot all vanish identically on R^2, whatever the residual levels on the
sampled grids.
For 3 < b_rep < 4 the same reduction, with three subtracted homogeneous terms and three integrations by parts (S is
C^4 on [0, 1], since the interior knots are simple and the degree is 5), gives C2 = -(b_rep L^2/2) J with
  J = -S(0)/D_1 + S'(0)/D_2 - S''(0)/D_3 - D_3^{-1} int_0^1 (1-t)^{3-b_rep} S'''(t) dt,   D_k = (b_rep - 1)...(b_rep - k)
(for two subtracted terms this is the formula above, with J = B/D_2). For the 16-mode states of the lambda path stored
with b_rep = beta, the same exact rational arithmetic gives C2 in [-4012.809, -4012.808], [-4077.563, -4077.562],
[-4218.152, -4218.151], [-4298.710, -4298.709] and [-4351.392, -4351.391] at lambda = 0.99, 0.98, 0.97, 0.965 and
0.96, C2 in [-4351.008, -4351.007], [-4385.870, -4385.869] and [-4386.803, -4386.802] for the 24-mode states at lambda
= 0.96, 0.955 and 0.95, C2 in [-4381.480, -4381.479], [-4392.002, -4392.001] and [-4445.383, -4445.382] for the
32-mode states at lambda = 0.95, 0.945 and 0.94, and C2 in [-4383.740, -4383.739], [-4392.303, -4392.302] and
[-4446.483, -4446.482] for the 40-mode states at lambda = 0.95, 0.945 and 0.94; for the 32-mode states of a run with
beta fixed per stage and lambda solved, C2 in [-4446.238, -4446.237] at beta = 3.023855 (lambda = 0.940011) and
[-4537.558, -4537.557] at beta = 3.0315 (lambda = 0.936736), [-4664.378, -4664.377] at beta = 3.04 (lambda =
0.934345), [-4821.233, -4821.232] at beta = 3.05 (lambda = 0.932636) and [-4979.108, -4979.107] at beta = 3.062
(lambda = 0.931684); C2 in [-4541.890, -4541.889], [-4681.595, -4681.594], [-4870.395, -4870.394],
[-5096.426, -5096.425], [-5289.577, -5289.576] and [-5279.508, -5279.507] for the 40-mode states of such a run at beta
= 3.0315 (lambda = 0.936737), 3.04 (lambda = 0.934345), 3.05 (lambda = 0.932636), 3.062 (lambda = 0.931684), 3.076
(lambda = 0.931657) and 3.092 (lambda = 0.932671), and C2 in [-5465.884, -5465.883] and [-5705.298, -5705.297] for the
48-mode states of such a run at beta = 3.076 (lambda = 0.931657) and 3.092 (lambda = 0.932670), and C2 in [-5465.870,
-5465.869] and [-5159.298, -5159.297] for the 48-mode states of a second such run at beta = 3.076 (lambda = 0.931658)
and 3.062 (lambda = 0.931683). These enclosures are exact for the stored fields; for b_rep > 3 their values depend on
the representation (on the second path, the refinement from 56 to 84 radial intervals changed C2 by 53 percent at
beta = 3.0925, with the sign unchanged, see above, and on the first path the change from 40 to 48 angular modes
changed it by 3.3 and 8.1 percent at beta = 3.076 and 3.092 and by 1.2 percent at 3.062), and no limiting value or
sign of C2 under refinement is claimed; for 2 < b_rep < 3 no radial refinement of C2 was made. Beyond the radius at
which t passes the last interior knot (and for r > L), these stored pairs have the Omega and Theta expansions assumed
in 4.26(d) with beta = b_rep, so by 4.26(d) none of them is a class A profile (that the stored vorticity alone is not
the vorticity of one already follows from 4.24). The obstruction need not be uniform as b_rep -> 3: these pointwise
exclusions alone do not rule out convergence of such a sequence to an exact profile; that conclusion would require
additional control of the limit and its asymptotics. The two beta = 3 states with 20 modes
(a0 = 2.4 and 2.7) are stored with b_rep = beta = 3 exactly; for each, the resonance coefficient of the state's own
vorticity is alpha_rep = L^2 S''(1)/2, where S is the combination of the stored radial splines that gives the first
cosine coefficient (the mode-0 spline minus half the mode-2 spline in the Chebyshev angular basis) and L the stored
radial scale. Its exact rational evaluation on the stored binary coefficients and the resulting knots is nonzero for
both states; the rounded values are -9.2257 and -12.3246 (the exact values and their inputs are kept in the working
archives, section 8). Beyond the radius at which the radial spline variable passes its last interior knot, the stored vorticity
is a finite sum of the powers in 4.27(c) up to O(r^{-5/3}), so 4.27(c) shows that neither stored field is the
vorticity of a beta = 3 class A profile. These are again properties of the representations; they say nothing about
nearby profiles outside the representation or about the class.

Inverse tests (manufactured fields, exact answers known): the whole-plane inverse reproduces the relative velocity of a
field with the slow tail Omega ~ r^{-1/3} to about 7e-15 with the exterior included (a sampled implementation test,
not an error bound) and errs by 1.1 to 1.8 without it (Q3). The target of the problem (between-node maxima near 1e-6 in both normalizations, with convergence under
resolution and domain changes) is not approached by any state: in every row of Table 6.1e the larger of the two
normalized (B2-P) maxima is at least 0.63 (Tables 6.1a to 6.1d give further sampled maxima, with their own sampling
and normalizations). No complete resolution and domain stability study, stagnation-point audit, or numerical
validation of the leading and next-order far field has been completed for these states; the sampled stagnation search
and the next-order far-field comparison of Table 6.1c are diagnostics of seven stored fields each, and the map-scale
re-solves of six. The vorticity representations used here have finitely many angular modes, so by 4.24 none of them
can be an exact class A profile at a fixed angular resolution; 4.24 gives no bound for their residuals and does not
account for the observed levels.

Table 6.1c. Completion of the numerical verification programme of the problem statement. No state of the unforced
problem (B2-P) with small residuals has been found, so every check that presupposes a candidate is not done; the entries for
forced states concern forced problems only, and manufactured-field tests do not replace checks on a candidate.

| check | status |
|---|---|
| three fitted profile resolutions | forced states only: 12, 16 and 20 angular modes with 40, 56 and 72 radial intervals (beta = 3), 16 and 24 angular modes with 56 radial intervals at lambda = 0.96, and 24, 32 and 40 angular modes at lambda = 0.95 (different optimization histories and strain tolerances; independent common-grid comparison: discrepancies of G 0.0040 and 0.00028, of its angular derivative 0.036 and 0.0031; finite sampled refinement, not a convergence proof); 32 and 40 angular modes at beta = 3.0315, 3.04, 3.05 and 3.062 on the first path (lambda differs by at most 1.1e-7; independent common-grid comparison E542, angular maximum of the difference over angular maximum of the 40-mode field, largest over the sampled radii: discrepancies of G 0.010 to 0.034 and of its angular derivative 0.068 to 0.16, at the largest sampled radius, growing with beta; finite sampled distances); 40 and 48 angular modes at beta = 3.062, 3.076 and 3.092 on the first path (two 48-mode states at 3.076: one stage accepted the inherited lambda after changing the fields, and a second run, from the 48-mode state at 3.092, solved lambda 5.7e-7 above the 40-mode value, with the same forced and (B2-P) maxima to three digits; differences of -7.2e-7 at 3.062 and -4.8e-7 at 3.092; forced maxima smaller by factors of 3.6 to 6.7 with 48 modes; the (B2-P) maxima of R_G/N_G beyond r = 300 are 0.58, 0.95 and 0.97 with 40 and 0.25, 0.30 and 0.70 with 48 modes at beta = 3.062, 3.076 and 3.092; C2 changed by 1.2, 3.3 and 8.1 percent; finite comparison, not a convergence result); 24, 32, 40 and 48 angular modes at beta = 3.085 and 3.1, 24, 32 and 40 at 3.11 and 24 and 40 at beta = 3.076 on the second path (the stored values of lambda lie within 3.3e-7, 5.3e-7, 1.5e-7 and 5.2e-7, the 48-mode state at 3.085 being an evaluation at the inherited lambda, and at 3.085 the center quantities of the 24- and 32-mode states differ by less than 1e-6; different histories; finite comparison of stored values and center quantities, not a convergence result); 56 and 84 radial intervals at beta = 3.0925, 3.085 and 3.105 on the second path (24 modes; the same stored lambda to six digits, at 3.0925 by acceptance of the inherited value, and center values above 3/5 at both; relative to the matched 56-interval 24-mode fields, the magnitude of C2 increases by approximately 52.6, 53.1 and 54.1 percent at beta = 3.085, 3.0925 and 3.105; sampled regional (B2-P) maxima 0.742 to 0.745 and 0.419 to 0.420 at 84 intervals, finite-grid diagnostics); tighter tolerances at beta = 3.0925 and 3.1 on the second path (lambda changes by 0 and 3.4e-7, C2 by less than 1e-5 relative; sampled regional (B2-P) maxima 0.744/0.419 and 0.742/0.419); not done for (B2-P) |
| three fit and inverse domains | forced states: two map scales of the fit, and three (L = 1, 1.5 and 2.5) for one forced state at beta = 3 with 12 angular modes (forced maxima 0.030 to 0.032 / 0.043 to 0.044, (B2-P) maxima 0.76/(0.83 to 0.84) across the three scales) and for the two states of the Jacobian diagnostics of 6.1, re-solved at their fixed (beta, lambda) (forced center-strain mismatch 5.6e-6, 5.1e-6 and 4.8e-6 at the state of the second path and 4.2e-5, 4.9e-5 and 5.7e-5 at the state of the first path; the fit objectives decrease with L and the exact C2 changes substantially with L; (B2-P) maxima about 0.74/0.42 and 0.75/0.46, so none is a profile; identifier P217); a map scale moves the radial nodes over the same whole plane, so these are not three inverse domains and not an equal-budget comparison; evaluator inverse: three core sizes and three quadrature orders; three fit domains for (B2-P) not done |
| equal-budget comparisons (optimization versus resolution) | partial: one equal-count comparison for the forced problem at lambda = 0.95 (same seed, prescribed beta, 20 map evaluations at 24, 32 and 40 angular modes; the ratios 49.8 and 4.61 of the final fit objectives persist, 6.1); equal evaluation counts, not equal computational budgets; no bound on the attainable residual |
| free-beta runs | rational fits with free beta and ten free-beta fits in a smooth stream-function trial space (section 6.2), and the two beta-free continuation paths above (forced problems; no state near (B2-P)) |
| several fixed beta | forced problems at beta = 2.25, 2.5, 3, 3.5; no fixed-beta continuation reached (B2-P) |
| distinct initializations | rational fits (42 trials of one method), collocation from generic starts, two different external dipoles in the forcing homotopy; eighteen sign-changing two-lobe external sources sampled at eps = 0 only, without a strain-matched seed (6.1); no lineage reached (B2-P) |
| different representations and solvers | characteristic formulation with Levenberg-Marquardt and with Anderson-accelerated fixed point, collocation, rational fits; none converged for (B2-P) |
| separately implemented residual and inverse evaluator | done (all tabulated states) |
| regional residuals, absolute and normalized | sampled maxima in Tables 6.1a, 6.1b; absolute and normalized maxima on six radial intervals, original and divided equations, forced and own velocity, for 73 saved states and, separately, thirty-three later states: seventeen of the second path (three with 24, two with 32, five with 40 and two with 48 angular modes, three with 84 radial intervals and two with tighter tolerances) and the 40-mode states at beta = 3.05, 3.062, 3.076 and 3.092 and four 48-mode states, at beta = 3.062, 3.092 and twice at 3.076, of the first path, six stored stages of the two paths restarted with 48 quadrature points per radial cell, and two redeterminations of lambda for the 32-mode stage of the first path at beta = 3.062 with 12 and 48 quadrature points (Tables 6.1d, 6.1e and the accompanying artifacts); also the six fields of the map-scale comparison (identifier P217) |
| desingularized residuals and axis limits | evaluated for the states of Tables 6.1a, 6.1b and the forced continuation states |
| stagnation points and separatrices | sampled only: for six stored fields (the forced states at the sampled minimum of the second path, at lambda = 0.96 with 24 modes and at beta = 3.076 and lambda = 0.94 with 40 modes on the first path, and at beta = 3, a0 = 2.4 of a fixed-beta run with 12 modes, and the unforced field of the stored vorticity at the sampled minimum) W.X > 0 at every point of a grid of 92 radii from 0.001 to 1e5 by 241 angles in the independent evaluation, and of the computation's grid of 400 radii from 0.02 to 1e5 by 181 angles (sampled minima of abs W/(beta r) 0.148 to 0.177 for the forced fields and 0.792 for the unforced one), and W.X > 0 at every point of a shifted independent grid of 92 radii from 0.001 to 1e5 by 241 angles for the forced 40-mode state of the second path at beta = 3.085 (sampled minimum of abs W/(beta r) 0.176, identifier P253); samples do not exclude zeros between grid points (a field with div W = 2 beta, the same samples, center and far field and saddles between the samples can be constructed, identifier P194); separatrices not classified; not done for a candidate |
| leading and next-order far field | derived analytically (4.12, 4.16; the third scalar terms for every beta > 2 in 4.26(a); the constant velocity for 2 < beta < 3 in 4.26(b), (c), its analogue for noninteger beta > 3 under stated expansions in 4.26(d); the beta = 3 resonance in 4.27); for forced states, local power-law exponents of Theta, Omega, U over three decades and signed strain-shell diagnostics were measured, and for seven stored forced states the exact next-order endpoint coefficients of the representation (of r^{-2/beta} in Omega and of r^{1-3/beta} in Theta) were compared with the values that the next-order relation, with the velocity of the leading vorticity tail, gives from their leading coefficients: relative L2 differences over the angle 0.19 and 0.058 with 12 modes and 0.014 and 0.0019 with 20 modes for a fixed-beta state at beta = 3, a0 = 2.4, and 0.95 to 1.09 for five states of the two paths, whose representation lacks the mixed powers that their source generates at the next order (this does not by itself account for differences of that size; identifier P196, and identifier P253 for the fifth, the 40-mode state of the second path at beta = 3.085, with 0.97 and 1.07); joint validation of leading and next-order coefficients for a candidate not done |
| inverse uncertainty for a candidate | not applicable (no candidate); evaluator tested on manufactured fields and on the states above; for the forced 40-mode state of the second path at beta = 3.085, the curl and divergence defects of the evaluator's whole-plane inverse of the stored vorticity, sampled at 210 points from r = 1e-5 to 1e7 with two quadrature tolerances and three difference steps, are at most 1.2e-7 and 1.3e-7 in absolute value (identifier P253); these are finite sensitivity measurements, not an error bound for the inverse; for six forced states the maxima over 181 angles from the computation's later 48-point evaluations of the stored relative velocities differ at r = 1e9 from those of an independent full-plane evaluation by 5.8 to 73 percent (identifier P291; a conditional numerical diagnostic, not an error bound; 6.1) |
| near-kernel directions of the Jacobian | partial: discrete singular-value, relative-gradient and gain diagnostics recorded; projection and undersampling null directions identified; no independent normalized near-kernel study at a B2 candidate; for the forced map, finite-difference Jacobians at one state of the second path near its sampled minimum (smallest singular value of J_T - I 0.034 in coefficient space and 0.015 in a full-plane weighted L2 metric of G, spectral radius of J_T 0.43; identifier P208) and at one state of the first path (0.0069 and 0.0037, spectral radius 1.85; identifier P234); linearized diagnostics without an error bound (6.1) |
| physical time-dependent reconstruction | derived analytically (section 3); not performed numerically |
| regeneration files | the coefficient files that enter the consolidated residual table and one complete evaluation packet are among the accompanying artifacts (section 8), the other intermediate states are in the working archives; none is a candidate |

Table 6.1d. Regional sampled maxima for the additive-forcing state at lambda = 0.97 (beta = 3.0035), independent
evaluation, 22:28 (96 angles on each of 145 radii from 1e-5 to 1e8, the separately implemented whole-plane inverse,
seven-point finite differences; halving the step changes the global normalized maxima by at most 5.1e-11, the regional
normalized maxima by at most 1.2e-10 and the regional absolute maxima by at most 3.4e-6; no denominator floor and no
zero denominators; Cartesian ratios omit the two axis angles, the divided ratios include them). Upper block: (B2-P)
with the inverse of the state's own vorticity. Lower block: the forced problem with the intended fixed source (not the
source used at run time, which was not saved).

| radii | max abs R_Theta | R_Theta/N_Theta | max abs R_Omega | R_Omega/N_Omega | max abs R_F | R_F/N_F | max abs R_G | R_G/N_G |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| (B2-P) 0 to 0.03 | 2.16e-5 | 0.0465 | 7.88e-4 | 0.0159 | 0.101 | 0.0466 | 0.0668 | 0.0160 |
| (B2-P) 0.03 to 0.3 | 0.0238 | 0.338 | 0.0857 | 0.136 | 1.24 | 0.338 | 0.763 | 0.136 |
| (B2-P) 0.3 to 3 | 23.5 | 0.747 | 7.77 | 0.464 | 22.5 | 0.747 | 8.48 | 0.464 |
| (B2-P) 3 to 30 | 74.4 | 0.654 | 12.1 | 0.477 | 24.4 | 0.654 | 13.5 | 0.482 |
| (B2-P) 30 to 300 | 109 | 0.505 | 5.20 | 0.413 | 0.0964 | 0.505 | 0.215 | 0.413 |
| (B2-P) 300 to 1e8 | 145 | 0.326 | 1.87 | 0.287 | 1.36e-3 | 0.326 | 7.79e-3 | 0.287 |
| forced 0 to 0.03 | 9.32e-9 | 8.89e-6 | 2.24e-7 | 2.41e-6 | 1.81e-5 | 8.89e-6 | 9.75e-6 | 2.41e-6 |
| forced 0.03 to 0.3 | 7.61e-7 | 1.04e-5 | 3.52e-6 | 7.06e-6 | 2.28e-5 | 1.04e-5 | 3.35e-5 | 7.06e-6 |
| forced 0.3 to 3 | 0.597 | 0.0274 | 0.251 | 0.0233 | 0.264 | 0.0295 | 0.271 | 0.0233 |
| forced 3 to 30 | 1.04 | 0.0356 | 0.432 | 0.0498 | 0.373 | 0.0356 | 0.456 | 0.0498 |
| forced 30 to 300 | 0.146 | 1.54e-3 | 0.0199 | 8.13e-3 | 1.37e-4 | 1.54e-3 | 8.18e-4 | 8.13e-3 |
| forced 300 to 1e8 | 1.03 | 1.06e-3 | 0.0195 | 9.36e-3 | 1.66e-6 | 1.06e-3 | 6.78e-5 | 9.36e-3 |

The same regional maxima were computed by the independent evaluator, from its saved raw arrays, for 73 saved states
with distinct coefficient archives (including one manufactured test state and one state transplanted to a different
map scale before refitting; the failed state at lambda = 0.98 of the second path is not among them). In every one of
them the larger of the (B2-P) maxima of R_F/N_F and R_G/N_G is at least 0.0987 on each of the four intervals beyond r
= 0.3 (at least 0.2889 for all of them except the first state of the second path above), and the overall (B2-P) maxima
lie between 0.73 and 1. The represented Theta has the envelope r^{1 - 2 s_rep} of its basis
(s_rep = 1/b_rep, with b_rep possibly different from beta), an actual leading term only when its coefficient is
nonzero. Both absolute and pointwise normalized residuals are reported; some stored states have unbounded absolute
residuals although their limiting normalized ratios are small, as shown above.

Table 6.1e. Stored states of this section with an independent residual evaluation (97 states). The residual columns
give the values of the independent evaluator, rounded to three significant digits. Families: H the forcing homotopy in
eps (the eps = 0 starting states of Table 6.1b and the eps = 0.34 states of Table 6.1a), F the fixed-beta forced
continuation beyond eps = 0 (including the states near the largest sampled eps, beta = 2.25 and the second dipole
family), B the free-beta continuation, L3 and Lb the additive-forcing path in lambda stored with b_rep = 3 and with
b_rep = beta, L2 the second such path (different seed and source, b_rep = beta; R84 marks its three states with 84
radial intervals and tight its two states with the tighter tolerances of the text); in Lb, K48b marks the two states
of the second 48-mode run, in Lb and L2 the prefix q48 marks the six restarts with 48 quadrature points per radial
cell, and in Lb the prefixes root12 and root48 mark the two redeterminations of lambda with 12 and 48 points (6.1). K
is the number of modes; acc. records whether the continuation step was accepted (recorded
only for the states stored with b_rep = beta; y*: stored as accepted by a run with fixed beta with the fit-growth
multiplier set to 1e9); a0 marked * is the center value F(0)
(the homotopy states store no a0). "Forced" is the residual of the forced problem for which the state was computed
(for blam1_lambda0p97, whose run-time source projection was not saved, the residual with the intended fixed source),
and (B2-P) the unforced equations with the whole-plane inverse of the state's own vorticity. The ratios are the maxima
of R_F/N_F and R_G/N_G (axis points included) and the absolute values the maxima of |R_Theta| and |R_Omega|. Sampling:
96 angles on 145, 161, 177 or 189 radii from 1e-5 to 1e8 with step 1e-5 max(1, r) for families F, B, L2, L3, Lb; the
seven points of Table 6.1b for eps = 0 and the eleven points of Table 6.1a for eps = 0.34. (s): the forced ratios at
eps = 0.34 use the separate-term normalizers (|2 A F| + |A x F_x| in place of |A (2F + x F_x)|, and similarly in N_G),
which coincide with N_F and N_G on the axis. Evaluation: identifier of the independent evaluation (section 8). Exact
certificate: P89 the tail witnesses of serialized states, P95 alpha_rep != 0, P102 the positivity certificate, P104
the constant C2 of the beta-free states; for the states stored with b_rep = beta, E_T != 0 is the exact tail witness
of this section and C2 the rational enclosure of the inverse constant, both in the evaluation packet. In every row the
larger (B2-P) normalized maximum is at least 0.63, and it is 1.00 to three digits in the second dipole family at
a0 = 10 to 20; no state is a candidate.

| state | fam. | beta | eps or lambda | a0 | K | b_rep | acc. | forced R_F/N_F, R_G/N_G | forced abs R_Theta, R_Omega | (B2-P) R_F/N_F, R_G/N_G | (B2-P) abs R_Theta, R_Omega | evaluation | exact certificate |
|---|---|---:|---|---:|---:|---|---|---|---|---|---|---|---|
| fb25b_eps0 | H | 2.5 | eps 0 | 1.003585* | 12 | =beta | - | 0.0150, 0.0638 | 0.197, 0.786 | 0.770, 0.388 | 7.08, 4.34 | E046 | - |
| fb30b_eps0 | H | 3 | eps 0 | 1.002473* | 12 | 3 | - | 0.00666, 0.0282 | 0.0994, 0.228 | 0.654, 0.404 | 6.64, 3.37 | E046 | - |
| fb25d_eps0.34 | H | 2.5 | eps 0.34 | 0.9998493* | 12 | =beta | - | 0.0881 (s), 0.688 (s) | 0.0796, 3.45 | 0.762, 0.743 | 3.37, 3.63 | E043 | - |
| fb30e_eps0.34 | H | 3 | eps 0.34 | 0.9998265* | 8 | 3 | - | 0.0389 (s), 0.650 (s) | 0.0566, 3.29 | 0.611, 0.634 | 4.59, 3.83 | E043 | - |
| fb30d_eps0.34 | H | 3 | eps 0.34 | 1.000036* | 12 | 3 | - | 0.0141 (s), 0.840 (s) | 0.188, 3.28 | 0.559, 0.839 | 8.20, 2.22 | E043 | - |
| beta225_K12_a010 | F | 2.25 | eps 0.0425505 | 1 | 12 | =beta | - | 0.794, 0.367 | 2.84, 2.34 | 0.913, 0.779 | 43.1, 16.6 | E090 | - |
| beta25_K12_a019 | F | 2.5 | eps 0.0592322 | 1.9 | 12 | =beta | - | 0.161, 0.113 | 2.77, 1.60 | 0.871, 0.934 | 100, 20.4 | E087 | - |
| beta25_K12_a021 | F | 2.5 | eps 0.0587704 | 2.1 | 12 | =beta | - | 0.166, 0.112 | 3.25, 1.85 | 0.906, 0.963 | 124, 28.4 | E089 | - |
| beta3_K12_L1_a021 | F | 3 | eps 0.0576559 | 2.1 | 12 | 3 | - | 0.0306, 0.0437 | 1.50, 0.614 | 0.765, 0.830 | 206, 13.1 | E088 | - |
| K12_N24 | F | 3 | eps 0.0576566 | 2.1 | 12 | 3 | - | 0.0315, 0.0439 | 1.49, 0.615 | 0.765, 0.836 | 206, 13.1 | E081 | - |
| a0c1L25_a02.1 | F | 3 | eps 0.0576567 | 2.1 | 12 | 3 | - | 0.0298, 0.0427 | 1.48, 0.615 | 0.765, 0.830 | 206, 13.1 | E155 | - |
| K16_N32 | F | 3 | eps 0.0576819 | 2.1 | 16 | 3 | - | 0.00386, 0.00553 | 0.188, 0.0736 | 0.765, 0.826 | 209, 13.0 | E081 | - |
| beta3_K16_a024 | F | 3 | eps 0.0582984 | 2.4 | 16 | 3 | - | 0.00375, 0.00579 | 0.219, 0.0915 | 0.775, 0.911 | 269, 17.1 | E087 | - |
| beta3_K16_a027 | F | 3 | eps 0.0560503 | 2.7 | 16 | 3 | - | 0.00393, 0.00675 | 0.418, 0.129 | 0.831, 0.946 | 365, 22.9 | E088 | - |
| beta3_K20_a021 | F | 3 | eps 0.0576849 | 2.1 | 20 | 3 | - | 0.00130, 0.00289 | 0.0606, 0.0385 | 0.765, 0.834 | 210, 13.1 | E087 | - |
| beta3_K20_a024 | F | 3 | eps 0.0583006 | 2.4 | 20 | 3 | - | 0.00148, 0.00326 | 0.0796, 0.0511 | 0.775, 0.910 | 270, 17.2 | E089 | P89: nonzero finite limit of R_Theta; P95: alpha_rep != 0 |
| beta3_K20_a027 | F | 3 | eps 0.0560517 | 2.7 | 20 | 3 | - | 0.00170, 0.00368 | 0.104, 0.0672 | 0.831, 0.945 | 367, 22.9 | E090 | P89: nonzero finite limit of R_Theta; P95: alpha_rep != 0 |
| a0cy25_a07 | F | 3 | eps 0.0177129 | 7 | 12 | 3 | - | 0.0125, 0.0189 | 0.849, 0.518 | 0.912, 0.952 | 533, 45.8 | E091 | - |
| a0cy25_a08 | F | 3 | eps 0.0183679 | 8 | 12 | 3 | - | 0.0137, 0.0213 | 1.07, 0.658 | 0.964, 0.966 | 713, 67.7 | E091 | - |
| a0cy25_a010 | F | 3 | eps 0.0175475 | 10 | 12 | 3 | - | 0.0158, 0.0248 | 1.52, 0.949 | 1.00, 0.980 | 1160, 127 | E091 | - |
| a0cy25_a012 | F | 3 | eps 0.0159978 | 12 | 12 | 3 | - | 0.0173, 0.0272 | 1.98, 1.27 | 1.00, 0.986 | 1700, 208 | E092 | - |
| a0cy25_a015 | F | 3 | eps 0.0137673 | 15 | 12 | 3 | - | 0.0188, 0.0297 | 2.68, 1.75 | 1.00, 0.990 | 2730, 371 | E092 | - |
| a0cy25_a020 | F | 3 | eps 0.0109621 | 20 | 12 | 3 | - | 0.0205, 0.0322 | 3.90, 2.56 | 1.00, 0.994 | 5000, 749 | E096 | - |
| beta35_K12_a024 | F | 3.5 | eps 0.0585536 | 2.4 | 12 | =beta | - | 0.0119, 0.0220 | 195, 0.306 | 0.693, 0.734 | 2750, 13.2 | E090 | - |
| beta35_K12_a027 | F | 3.5 | eps 0.0585871 | 2.7 | 12 | =beta | - | 0.0125, 0.0237 | 251, 0.373 | 0.701, 0.848 | 3730, 15.1 | E090 | - |
| beta35_K12_a030 | F | 3.5 | eps 0.0567322 | 3 | 12 | =beta | - | 0.0131, 0.0255 | 313, 0.451 | 0.712, 0.910 | 4950, 18.6 | E090 | P89: R_Theta unbounded (second term) |
| betafree_eps002 | B | 2.504021 | eps 0.02 | 1 | 12 | =beta | - | 0.148, 0.122 | 1.82, 1.02 | 0.849, 0.511 | 53.7, 11.7 | E089 | - |
| bfree1os3_eps0.025 | B | 2.4402319 | eps 0.025 | 1 | 12 | =beta | - | 0.191, 0.140 | 2.03, 1.20 | 0.864, 0.540 | 50.8, 11.5 | E096 | P104: C2 = -6.3077 < 0 |
| bfree1os3_eps0.03 | B | 2.3886178 | eps 0.03 | 1 | 12 | =beta | - | 0.232, 0.162 | 2.22, 1.38 | 0.877, 0.612 | 48.8, 12.0 | E099 | P89: no divergence conclusion; P104: C2 = -7.2239 < 0 |
| bfree1os3_eps0.035 | B | 2.3465247 | eps 0.035 | 1 | 12 | =beta | - | 0.305, 0.200 | 2.40, 1.58 | 0.888, 0.683 | 47.1, 12.6 | E100 | P104: C2 = -8.2986 < 0 |
| bfree1os3_eps0.04 | B | 2.3118919 | eps 0.04 | 1 | 12 | =beta | - | 0.410, 0.240 | 2.57, 1.78 | 0.897, 0.750 | 46.0, 13.4 | E104 | P104: C2 = -9.4498 < 0 |
| blam12g_lambda0.99 | L3 | 3.0018501 | lambda 0.99 | 1.011631 | 12 | 3 | - | 0.0373, 0.0509 | 1.05, 0.442 | 0.751, 0.492 | 132, 12.7 | E099 | P89: R_Theta unbounded (leading term) |
| blam16f_lambda0.99 | L3 | 3.001986 | lambda 0.99 | 1.011258 | 16 | 3 | - | 0.00601, 0.0109 | 1.25, 0.0869 | 0.751, 0.479 | 132, 12.7 | E099 | P89: R_Theta unbounded (leading term) |
| blam12g_lambda0.98 | L3 | 3.0027083 | lambda 0.98 | 1.011631 | 12 | 3 | - | 0.0364, 0.0502 | 1.46, 0.436 | 0.749, 0.487 | 139, 12.4 | E100 | - |
| blam16f_lambda0.98 | L3 | 3.0028657 | lambda 0.98 | 1.011258 | 16 | 3 | - | 0.00629, 0.0102 | 1.78, 0.0801 | 0.750, 0.474 | 142, 12.4 | E100 | - |
| blam12g_lambda0.97 | L3 | 3.0036563 | lambda 0.97 | 1.011631 | 12 | 3 | - | 0.0356, 0.0498 | 2.13, 0.432 | 0.747, 0.482 | 146, 12.1 | E101 | P95: alpha_rep != 0 |
| blam16f_lambda0.97 | L3 | 3.0037735 | lambda 0.97 | 1.011258 | 16 | 3 | - | 0.00615, 0.00944 | 2.58, 0.0747 | 0.748, 0.469 | 148, 12.1 | E102 | P95: alpha_rep != 0; P102: F > 0, 2F + x F_x > 0 |
| blam12g_lambda0.96 | L3 | 3.0060795 | lambda 0.96 | 1.011631 | 12 | 3 | - | 0.0348, 0.0505 | 5.91, 0.428 | 0.745, 0.477 | 151, 11.8 | E105 | P89: R_Theta unbounded (leading term) |
| blam16f_lambda096 | L3 | 3.0060249 | lambda 0.96 | 1.011258 | 16 | 3 | - | 0.00626, 0.00863 | 4.90, 0.0689 | 0.745, 0.464 | 151, 11.9 | E107 | P102: F > 0, 2F + x F_x > 0 |
| blam12v_lambda0.99 | Lb | 3.0018497 | lambda 0.99 | 1.011631 | 12 | =beta | y | 0.0374, 0.0509 | 1.05, 0.442 | 0.751, 0.492 | 132, 12.7 | E156 | E_T != 0, R_Theta unbounded |
| blam16v_lambda0.99 | Lb | 3.0019856 | lambda 0.99 | 1.011258 | 16 | =beta | y | 0.00592, 0.0109 | 0.279, 0.0868 | 0.751, 0.479 | 133, 12.7 | E118 | E_T != 0, R_Theta unbounded; C2 in [-4012.809, -4012.808] |
| blam16v_lambda0.98 | Lb | 3.002861 | lambda 0.98 | 1.011258 | 16 | =beta | y | 0.00615, 0.0102 | 0.440, 0.0803 | 0.750, 0.474 | 142, 12.4 | E130 | E_T != 0, R_Theta unbounded; C2 in [-4077.563, -4077.562] |
| blam1_lambda0p97 | Lb | 3.0035422 | lambda 0.97 | 1.011631 | 12 | =beta | - | 0.0356, 0.0498 | 1.04, 0.432 | 0.747, 0.482 | 145, 12.1 | E091 | - |
| blam16v_lambda0.97 | Lb | 3.0037732 | lambda 0.97 | 1.011258 | 16 | =beta | y | 0.00617, 0.00944 | 0.759, 0.0749 | 0.748, 0.469 | 149, 12.1 | E130 | E_T != 0, R_Theta unbounded; C2 in [-4218.152, -4218.151] |
| blam16v_lambda0.965 | Lb | 3.0046354 | lambda 0.965 | 1.011258 | 16 | =beta | y | 0.00601, 0.00905 | 1.03, 0.0721 | 0.747, 0.467 | 149, 12.0 | E130 | E_T != 0, R_Theta unbounded; C2 in [-4298.71, -4298.709] |
| blam16v_lambda0.96 | Lb | 3.0060323 | lambda 0.96 | 1.011258 | 16 | =beta | n | 0.00596, 0.00862 | 1.52, 0.0692 | 0.745, 0.464 | 152, 11.9 | E148 | E_T != 0, R_Theta unbounded; C2 in [-4351.392, -4351.391] |
| blam24v_lambda0.96 | Lb | 3.0060478 | lambda 0.96 | 1.011258 | 24 | =beta | y | 4.08e-4, 6.58e-4 | 1.11, 0.00480 | 0.745, 0.464 | 157, 11.9 | E148 | E_T != 0, R_Theta unbounded; C2 in [-4351.008, -4351.007] |
| blam24v_lambda0.955 | Lb | 3.0081642 | lambda 0.955 | 1.011258 | 24 | =beta | y | 3.85e-4, 0.00138 | 1.63, 0.00488 | 0.744, 0.461 | 162, 11.8 | E153 | E_T != 0, R_Theta unbounded; C2 in [-4385.87, -4385.869] |
| blam24v_lambda0.95 | Lb | 3.0113981 | lambda 0.95 | 1.011258 | 24 | =beta | n | 0.00147, 0.00432 | 2.67, 0.00570 | 0.743, 0.458 | 164, 11.7 | E161 | E_T != 0, R_Theta unbounded; C2 in [-4386.803, -4386.802] |
| blam32v_lambda0.95 | Lb | 3.0113961 | lambda 0.95 | 1.011258 | 32 | =beta | y | 2.49e-4, 8.56e-4 | 2.22, 0.00157 | 0.743, 0.458 | 167, 11.7 | E168 | E_T != 0, R_Theta unbounded; C2 in [-4381.48, -4381.479] |
| blam40v95_lambda0.95 | Lb | 3.0113961 | lambda 0.95 | 1.011258 | 40 | =beta | y | 2.45e-4, 3.19e-4 | 2.17, 3.91e-4 | 0.743, 0.458 | 167, 11.7 | E189 | E_T != 0, R_Theta unbounded; C2 in [-4383.74, -4383.739] |
| blam32v_lambda0.945 | Lb | 3.0162609 | lambda 0.945 | 1.011258 | 32 | =beta | y | 6.92e-4, 0.00206 | 3.45, 0.00407 | 0.741, 0.455 | 173, 11.5 | E174 | E_T != 0, R_Theta unbounded; C2 in [-4392.002, -4392.001] |
| blam40v_lambda0.945 | Lb | 3.0162738 | lambda 0.945 | 1.011258 | 40 | =beta | y | 2.50e-4, 9.40e-4 | 3.12, 0.00138 | 0.741, 0.455 | 169, 11.5 | E208 | E_T != 0, R_Theta unbounded; C2 in [-4392.303, -4392.302] |
| blam32v_lambda0.94 | Lb | 3.0238546 | lambda 0.94 | 1.011258 | 32 | =beta | n | 0.00359, 0.00744 | 6.15, 0.00986 | 0.738, 0.452 | 188, 11.4 | E189 | E_T != 0, R_Theta unbounded; C2 in [-4445.383, -4445.382] |
| K40_l094 | Lb | 3.0238548 | lambda 0.94 | 1.011258 | 40 | =beta | y | 6.87e-4, 0.00257 | 5.16, 0.00430 | 0.738, 0.452 | 178, 11.4 | E219 | E_T != 0, R_Theta unbounded; C2 in [-4446.483, -4446.482] |
| K32_beta3.023855 | Lb | 3.023855 | lambda 0.940011 | 1.011258 | 32 | =beta | y* | 0.00359, 0.00743 | 6.14, 0.00985 | 0.738, 0.452 | 188, 11.4 | E248 | E_T != 0, R_Theta unbounded; C2 in [-4446.238, -4446.237] |
| K32_beta3.0315 | Lb | 3.0315 | lambda 0.936736 | 1.011258 | 32 | =beta | y* | 0.00957, 0.0181 | 15.8, 0.0175 | 0.736, 0.449 | 217, 11.2 | E271 | E_T != 0, R_Theta unbounded; C2 in [-4537.558, -4537.557] |
| K40_beta3.0315 | Lb | 3.0315 | lambda 0.936737 | 1.011258 | 40 | =beta | y* | 0.00240, 0.00559 | 7.96, 0.00888 | 0.736, 0.449 | 193, 11.2 | E365 | E_T != 0, R_Theta unbounded; C2 in [-4541.890, -4541.889] |
| K32_beta3.04 | Lb | 3.04 | lambda 0.934345 | 1.011258 | 32 | =beta | y* | 0.0204, 0.0366 | 35.8, 0.0324 | 0.734, 0.447 | 270, 11.1 | E304 | E_T != 0, R_Theta unbounded; C2 in [-4664.378, -4664.377] |
| K40_beta3.04 | Lb | 3.04 | lambda 0.934345 | 1.011258 | 40 | =beta | y* | 0.00633, 0.0154 | 15.0, 0.0157 | 0.734, 0.447 | 217, 11.1 | E377 | E_T != 0, R_Theta unbounded; C2 in [-4681.595, -4681.594] |
| K32_beta3.05 | Lb | 3.05 | lambda 0.932636 | 1.011258 | 32 | =beta | y* | 0.0397, 0.0674 | 73.6, 0.0649 | 0.732, 0.449 | 367, 11.0 | E304 | E_T != 0, R_Theta unbounded; C2 in [-4821.233, -4821.232] |
| K40_beta3.05 | Lb | 3.05 | lambda 0.932636 | 1.011258 | 40 | =beta | y* | 0.0142, 0.0364 | 34.8, 0.0252 | 0.732, 0.449 | 262, 11.0 | E525 | E_T != 0, R_Theta unbounded; C2 in [-4870.395, -4870.394] |
| K32_beta3.062 | Lb | 3.062 | lambda 0.931684 | 1.011258 | 32 | =beta | y* | 0.0678, 0.109 | 143, 0.119 | 0.730, 0.744 | 600, 10.9 | E325 | E_T != 0, R_Theta unbounded; C2 in [-4979.108, -4979.107] |
| K40_beta3.062 | Lb | 3.062 | lambda 0.931684 | 1.011258 | 40 | =beta | y* | 0.0293, 0.0773 | 76.1, 0.0461 | 0.730, 0.580 | 346, 10.9 | E530 | E_T != 0, R_Theta unbounded; C2 in [-5096.426, -5096.425] |
| K40_beta3.076 | Lb | 3.076 | lambda 0.931657 | 1.011258 | 40 | =beta | y* | 0.0559, 0.120 | 155, 0.0889 | 0.727, 0.954 | 636, 10.8 | E548 | E_T != 0, R_Theta unbounded; C2 in [-5289.577, -5289.576] |
| K40_beta3.092 | Lb | 3.092 | lambda 0.932671 | 1.011258 | 40 | =beta | y* | 0.0877, 0.151 | 291, 0.154 | 0.724, 0.966 | 1180, 10.6 | E557 | E_T != 0, R_Theta unbounded; C2 in [-5279.508, -5279.507] |
| K48_beta3.076 | Lb | 3.076 | lambda 0.931657 | 1.011258 | 48 | =beta | y* | 0.0103, 0.0251 | 55.5, 0.0304 | 0.727, 0.456 | 296, 10.8 | P262 | E_T != 0, R_Theta unbounded; C2 in [-5465.884, -5465.883] |
| K48_beta3.092 | Lb | 3.092 | lambda 0.932670 | 1.011258 | 48 | =beta | y* | 0.0195, 0.0424 | 122, 0.0486 | 0.724, 0.703 | 545, 10.6 | P267 | E_T != 0, R_Theta unbounded; C2 in [-5705.298, -5705.297] |
| K48b_beta3.076 | Lb | 3.076 | lambda 0.931658 | 1.011258 | 48 | =beta | y* | 0.0103, 0.0251 | 55.5, 0.0304 | 0.727, 0.456 | 296, 10.8 | P277 | E_T != 0, R_Theta unbounded; C2 in [-5465.870, -5465.869] |
| K48b_beta3.062 | Lb | 3.062 | lambda 0.931683 | 1.011258 | 48 | =beta | y* | 0.00435, 0.0115 | 22.4, 0.0178 | 0.730, 0.452 | 233, 10.9 | P280 | E_T != 0, R_Theta unbounded; C2 in [-5159.298, -5159.297] |
| q48K32_beta3.062 | Lb | 3.062 | lambda 0.931684 | 1.011258 | 32 | =beta | y* | 0.0677, 0.109 | 145, 0.120 | 0.730, 0.744 | 604, 10.9 | P287 | E_T != 0, R_Theta unbounded; C2 in [-5149.015, -5149.014] |
| q48K40_beta3.076 | Lb | 3.076 | lambda 0.931657 | 1.011258 | 40 | =beta | y* | 0.0560, 0.120 | 160, 0.0894 | 0.727, 0.954 | 639, 10.8 | P287 | E_T != 0, R_Theta unbounded; C2 in [-5514.655, -5514.654] |
| q48K40_beta3.092 | Lb | 3.092 | lambda 0.932671 | 1.011258 | 40 | =beta | y* | 0.0869, 0.151 | 303, 0.155 | 0.724, 0.966 | 1190, 10.6 | P287 | E_T != 0, R_Theta unbounded; C2 in [-6004.355, -6004.354] |
| q48K48b_beta3.062 | Lb | 3.062 | lambda 0.931683 | 1.011258 | 48 | =beta | y* | 0.00452, 0.0116 | 19.1, 0.0177 | 0.730, 0.452 | 232, 10.9 | P287 | E_T != 0, R_Theta unbounded; C2 in [-5140.086, -5140.085] |
| q48K48_beta3.092 | Lb | 3.092 | lambda 0.932670 | 1.011258 | 48 | =beta | y* | 0.0190, 0.0423 | 103, 0.0490 | 0.724, 0.703 | 536, 10.6 | P287 | E_T != 0, R_Theta unbounded; C2 in [-5983.681, -5983.680] |
| root12K32_beta3.062 | Lb | 3.062 | lambda 0.9316837662 | 1.011258 | 32 | =beta | y* | 0.0678, 0.109 | 143, 0.119 | 0.730, 0.744 | 600, 10.9 | P294 | E_T != 0, R_Theta unbounded; C2 in [-4979.102, -4979.101] |
| root48K32_beta3.062 | Lb | 3.062 | lambda 0.9316837838 | 1.011258 | 32 | =beta | y* | 0.0677, 0.109 | 145, 0.120 | 0.730, 0.744 | 604, 10.9 | P294 | E_T != 0, R_Theta unbounded; C2 in [-5148.985, -5148.984] |
| L2K24_lambda0.99 | L2 | 3.0866746 | lambda 0.99 | 1.0 | 24 | =beta | y | 2.53e-4, 2.59e-4 | 2.25, 1.44e-4 | 0.745, 0.420 | 18.5, 2.68 | E339 | E_T != 0, R_Theta unbounded; C2 in [-425.908, -425.907] |
| L2K24_lambda0.98 | L2 | 3.0415471 | lambda 0.98 | 1.0 | 24 | =beta | n | 0.0270, 0.00943 | 0.782, 0.0499 | 0.752, 0.423 | 14.6, 2.72 | E354 | E_T != 0, R_Theta unbounded; C2 in [-228.011, -228.010] |
| L2K24_beta3.105 | L2 | 3.105 | lambda 0.990022 | 1.0 | 24 | =beta | y* | 3.09e-4, 3.15e-4 | 2.98, 1.43e-4 | 0.742, 0.419 | 20.1, 2.64 | E409 | E_T != 0, R_Theta unbounded; C2 in [-517.428, -517.427] |
| L2K24_beta3.2 | L2 | 3.2 | lambda 0.994211 | 1.0 | 24 | =beta | y* | 6.21e-4, 7.14e-4 | 8.81, 3.55e-4 | 0.727, 0.414 | 31.4, 2.51 | E429 | E_T != 0, R_Theta unbounded; C2 in [-1243.684, -1243.683] |
| L2K24_beta3.25 | L2 | 3.25 | lambda 0.998139 | 1.0 | 24 | =beta | y* | 7.89e-4, 1.53e-3 | 13.5, 6.91e-4 | 0.720, 0.412 | 39.9, 2.45 | E440 | E_T != 0, R_Theta unbounded; C2 in [-1871.948, -1871.947] |
| L2K32_beta3.0925 | L2 | 3.0925 | lambda 0.989975 | 1.0 | 32 | =beta | y* | 2.70e-4, 2.75e-4 | 2.47, 9.18e-5 | 0.744, 0.419 | 18.9, 2.67 | E447 | E_T != 0, R_Theta unbounded; C2 in [-453.408, -453.407] |
| L2K32_beta3.085 | L2 | 3.085 | lambda 0.990033 | 1.0 | 32 | =beta | y* | 2.48e-4, 2.53e-4 | 2.19, 8.46e-5 | 0.745, 0.420 | 18.3, 2.68 | E447 | E_T != 0, R_Theta unbounded; C2 in [-417.563, -417.562] |
| L2R84_beta3.0925 | L2 | 3.0925 | lambda 0.989975 | 1.0 | 24 | =beta | y* | 1.70e-4, 1.75e-4 | 1.56, 1.39e-4 | 0.744, 0.420 | 18.0, 2.67 | E517 | E_T != 0, R_Theta unbounded; C2 in [-693.980, -693.979] |
| L2R84_beta3.085 | L2 | 3.085 | lambda 0.990033 | 1.0 | 24 | =beta | y* | 1.57e-4, 1.61e-4 | 1.40, 1.32e-4 | 0.745, 0.420 | 17.6, 2.69 | E517 | E_T != 0, R_Theta unbounded; C2 in [-637.318, -637.317] |
| L2R84_beta3.105 | L2 | 3.105 | lambda 0.990022 | 1.0 | 24 | =beta | y* | 1.92e-4, 1.97e-4 | 1.86, 1.46e-4 | 0.742, 0.419 | 19.0, 2.65 | E517 | E_T != 0, R_Theta unbounded; C2 in [-797.121, -797.120] |
| L2tight_beta3.0925 | L2 | 3.0925 | lambda 0.989975 | 1.0 | 24 | =beta | y* | 2.70e-4, 2.77e-4 | 2.47, 1.37e-4 | 0.744, 0.419 | 18.9, 2.67 | E517 | E_T != 0, R_Theta unbounded; C2 in [-453.409, -453.408] |
| L2tight_beta3.1 | L2 | 3.1 | lambda 0.989983 | 1.0 | 24 | =beta | y* | 2.93e-4, 3.00e-4 | 2.77, 1.41e-4 | 0.742, 0.419 | 19.6, 2.65 | E517 | E_T != 0, R_Theta unbounded; C2 in [-491.151, -491.150] |
| L2K40_beta3.0925 | L2 | 3.0925 | lambda 0.989975 | 1.0 | 40 | =beta | y* | 2.70e-4, 2.75e-4 | 2.47, 9.18e-5 | 0.744, 0.419 | 19.0, 2.67 | P248 | E_T != 0, R_Theta unbounded; C2 in [-453.408, -453.407] |
| L2K40_beta3.085 | L2 | 3.085 | lambda 0.990033 | 1.0 | 40 | =beta | y* | 2.48e-4, 2.53e-4 | 2.19, 8.46e-5 | 0.745, 0.420 | 18.3, 2.68 | P248 | E_T != 0, R_Theta unbounded; C2 in [-417.562, -417.561] |
| L2K40_beta3.1 | L2 | 3.1 | lambda 0.989983 | 1.0 | 40 | =beta | y* | 2.93e-4, 2.98e-4 | 2.77, 9.85e-5 | 0.742, 0.419 | 19.6, 2.65 | P248 | E_T != 0, R_Theta unbounded; C2 in [-491.147, -491.146] |
| L2K40_beta3.11 | L2 | 3.11 | lambda 0.990085 | 1.0 | 40 | =beta | y* | 3.24e-4, 3.27e-4 | 3.19, 1.06e-4 | 0.741, 0.418 | 20.6, 2.63 | P251 | E_T != 0, R_Theta unbounded; C2 in [-544.647, -544.646] |
| L2K40_beta3.076 | L2 | 3.076 | lambda 0.990199 | 1.0 | 40 | =beta | y* | 2.21e-4, 2.27e-4 | 1.87, 7.93e-5 | 0.746, 0.420 | 17.6, 2.70 | P251 | E_T != 0, R_Theta unbounded; C2 in [-376.874, -376.873] |
| L2K48_beta3.085 | L2 | 3.085 | lambda 0.990033 | 1.0 | 48 | =beta | y* | 2.48e-4, 2.53e-4 | 2.19, 8.46e-5 | 0.745, 0.420 | 18.3, 2.68 | P254 | E_T != 0, R_Theta unbounded; C2 in [-417.562, -417.561] |
| L2K48_beta3.1 | L2 | 3.1 | lambda 0.989984 | 1.0 | 48 | =beta | y* | 2.93e-4, 2.98e-4 | 2.77, 9.84e-5 | 0.742, 0.419 | 19.6, 2.65 | P254 | E_T != 0, R_Theta unbounded; C2 in [-491.150, -491.149] |
| q48L2K40_beta3.085 | L2 | 3.085 | lambda 0.990033 | 1.0 | 40 | =beta | y* | 2.48e-4, 2.53e-4 | 2.19, 8.46e-5 | 0.745, 0.420 | 18.3, 2.68 | P287 | E_T != 0, R_Theta unbounded; C2 in [-417.562, -417.561] |

### 6.2 Methods tested and their limitations

- Published theorems (4.14): none of the audited Liouville, self-similar-exclusion or blow-up criteria has been shown
  to decide class A; one cited paper could not be obtained and no claim is made about it.
- Kinematics and a single transport equation: the far-field derivative condition (D) is not implied by kinematics
  (shear example, 4.6); the axis conditions of 4.13 are necessary conditions only; the explicit example of 4.13
  satisfies the conditions listed in Q2(f) and fails (V) at the third-order center condition 4.13(vii), so an
  exclusion must use (V) beyond the leading center identities; the further conditions of (V) in the compatibility
  summary after 4.31 can be met as well, so an exclusion must use more; by 4.32 none of these configurations is a
  profile.
- Decay and integrability: these exclusions remove every tail to which they apply (4.5, 4.6, 4.8, 4.9) and leave only
  the slow homogeneous tail (4.12, 4.15). The leading dilation balances alone impose no angular equation on the
  coefficients of the powers r^(-1/beta) (vorticity) and r^(1-2/beta) (temperature), and the second terms are
  determined by the leading ones (4.16). Actual profile tails are smooth and obey the parity, axis and further
  compatibility conditions proved in section 4. No global profile is obtained from these leading balances.
- Integral identities (4.12(g), 4.17): each pairs a positive quantity with a signed one (the nonlocal kernel v =
  V_1/x, the product Omega Theta_x, or quotients that may change sign), so none excludes a profile by sign. In G the
  profile is determined by W (4.18); the additional results specific to G (4.18, 4.21, 4.22, 4.35) exclude profiles
  only under additional shape hypotheses on Omega, all class A restrictions also apply to G under their stated
  hypotheses, and none excludes all profiles in G.
- Horizontal monotonicity in G: Theta_x >= 0 on {x > 0} would give Omega > 0 there and a positive vorticity tail on
  the open right semicircle (4.21(d)), which no result here excludes for beta > 2; the properties of the conjugating
  coordinates do not imply that sign (explicit map, 4.22).
- Axis subsystem in G (4.35): in the normalized coordinates of 4.18(b) the axis relations are equivalent to 4.13(i)
  (4.35(a)); they are compatible with a smooth canonical vorticity that is positive on {x > 0}, has the slow tail and
  the center strain, and has axis velocity of the sign of y (4.35(b)); the axis coefficient Q_+ of 4.21(a) is a
  strictly increasing functional of the axis velocity and is unbounded along these fields at fixed beta and a0
  (4.35(c)); and the nonnegative transport weights of 4.35(d) give no sign contradiction. The fields of 4.35(b) supply
  no Theta and solve neither (T) nor (V) off the axis.
- Strain identity (4.23): it is invariant under the signed scaling, its vorticity part takes both signs on pairs of
  radial blobs, and the nonprofiles of 4.23(c) satisfy it together with the conditions listed there, so those
  conditions and the identity force no contradiction; compatibility with the other identities of the family, which
  together are equivalent to the equations, has not been established.
- Numerical closures: in the tested fields, omitting the exterior of the inverse caused the velocity differences
  reported in Q3 and in the inverse tests of 6.1 (empirical comparisons, not a uniform lower bound over the tail
  class); a compact-cutoff polynomial field with exact core equations (core absolute residuals at most 2.5e-9 for (T) and
  8.8e-11 for (V)) has transport defects that grow from 2.7e3 to 4.5e4 (temperature) and from 5.4e4 to 2.3e5
  (vorticity) in its cutoff annulus as the radius doubles from 8 to 32, so small core residuals are not evidence;
  42 rational fits (three degrees, fixed and free beta; different trials of one method) all had large residuals and unstable extrapolation;
  unconstrained collocation from generic starts converged to the exact polynomial solution Theta = a x^2,
  Omega = (4a/beta) x, U_rel = (-(beta + 2) x/2, (beta + 2) y/2 - 2a x^2/beta), which solves (T) and (V) for every beta
  (direct substitution) but violates U = o(|X|); a velocity interpolation rule that loses exact divergence
  (manufactured divergence defect about 1.4e-2) was identified and replaced, but the replacement has not been validated:
  its cell traces jump and its parity-only factors leak high angular modes at the center, so it is neither globally
  smooth nor exactly divergence free, and no state computed with either rule is a candidate.
- A representation in which the temperature equation holds exactly (global-source subclass with Theta_x > 0 on
  {x > 0}): the unknown is a generating function S(xi, y) of the conjugating coordinates of 4.18 (x = S_y, eta = S_xi,
  Theta = a0 xi^2), so that only the vorticity equation remains, solved by least squares with beta free and a forcing
  homotopy. Three saved states (Chebyshev bases of sizes 14 x 14 and 20 x 20 with a far-field block; two at the end
  of the homotopy, one saved before a solver failure) are not candidates: an independent evaluation by separate
  high-precision differentiation finds maximal ratios of the (B2-P) vorticity residual to its normalizer of 0.97 to
  1.0 and Omega < 0 at points of {x > 0}. The representation assumes kappa = 0 in 4.18(b) (linear normal form), which
  holds automatically unless lambda2 = k lambda1 for an even integer k.
- Dynamic rescaling (evolution of the rescaled equations with Theta_xx(0) and Omega_x(0) held fixed, so that a steady
  state with negative vorticity rescaling rate c_w would be a profile, with beta = -c_l/c_w for the spatial rate c_l; polar mapped Chebyshev times Fourier discretization with a
  modal whole-plane inverse): from Gaussian and from algebraic initial data with Theta_x > 0 and Omega > 0 on
  {x > 0} the center strain was not sustained (for the algebraic data it fell from 2.11 to 1.15 by rescaled time 0.75,
  by which c_w had changed sign from -0.85 to 0.12, and positivity was lost later; reproduced independently), and steady Newton
  and homotopy solves of the rescaled profile equations stalled far from the unforced problem with both signs lost
  (not reproduced independently). The modal inverse was validated only on rapidly decaying fields: for the slow-tail
  field Omega = 2xy(1 + r^2)^{-7/6}, whose strain is exactly 1.5, it returns 1.516 to 1.566 at the radial
  resolutions tested and values that drift with the quadrature order (1.507 to 1.586), because the interpolated source
  does not vanish at the compactified endpoint. These are failures of this discretization only.
- A separately implemented smooth trial space (stream function and temperature as Chebyshev sums in a mapped radius
  and in angle with shifted inverse-radius powers, the center identities imposed as linear constraints, the canonical
  inverse exact on the trial space), fitted by weighted least squares at beta = 2.25 to 4.25 with two to three basis
  sizes: all sixteen fits have held-out maximal residual ratios 0.82 to 1 for (T) and 1 for (V), and the twelve
  regularized ones have negative vorticity samples on {x > 0}; with the same solver and no regularization,
  manufactured forced problems are recovered to weighted residual about 1e-10, while a coefficient regularizer of 1e-5
  biases them (0.013 and 0.058), and removing it still does not give small defining residuals for the unforced
  problem. With beta free in [2.02, 8] (starting values 2.25, 2.75, 3.25, 4.25 and 6.5, two basis sizes each, no
  regularizer), all ten fits stop at the lower bound beta = 2.02 with held-out maximal ratios 0.98 to 1 for (T) and
  0.81 to 1 for (V); this determines no value of beta and says nothing about beta = 2. For each of these ten stored
  fields, exact rational arithmetic on its coefficients shows that the residuals of (V), in stream-function form, and
  of (T) have nonzero terms at fractional powers of r in the far field; this is a property of those stored fields
  only, not a lower bound for nearby fields. The coefficient map of this trial space can have kernels at integer beta,
  depending on the radial degree; they come from the representation and its affine gauge, not from symmetries of
  solutions. In a variant with a free fractional tail parameter, the center data and the two first tail identities
  imposed exactly, and no regularizer (twelve fits: beta fixed at 2.2, 2.5 or 2.8, or free in [2.02, 2.98], two basis
  sizes each), the held-out maximal ratios are 0.92 to 1 for (T) and 1 for (V), and all six free-beta fits stop at the
  lower bound (beta within 2e-5 of 2.02); exact rational arithmetic on the twelve stored fields gives nonzero center
  coefficients that involve the third-order jet of the fields (x^2 y in the residual of (T), 6.17 to 10.98; x y in
  R_Omega, 10.60 to 19.38), so none of them is a local solution at the center (again a property of these fields only).
  In the horizontal primitive representation of 4.33 (stream function only, Theta = int_0^x F; eighteen fits, beta
  fixed at 2.25, 2.75 or 3.5 or free, three resolutions), every stored field has a nonzero rational Taylor coefficient
  of the residual of (T) of degree at most 4 and nonzero leading angular primitive moments, and the free-beta fits
  stop at the lower bound 2.05; again this concerns these fields only. In a second search in this representation
  (eighteen fits: beta fixed at 2.25, 2.75 or 3.5, or free from these starting values; three levels on which the basis
  size and the fit radius 10, 30, 100 increase together, so that this is not an isolated convergence study; every
  stage stopped at a cap of 90 evaluations), the center data, the two leading angular moments and the Taylor
  coefficients of the residual of (T) through degree 4 are imposed and hold exactly in every stored field; the
  held-out maximal ratio for (T) is 1 in all eighteen, every stored field has a nonzero Taylor coefficient of degree 5
  of the residual of (T), and the six final fields have nonzero horizontal offsets at y = 1 (4.33(e); from -12.16 to
  0.18, nonzero by exact algebraic certificates). The free-beta fits end at beta = 2.124 to 2.146, above the lower
  bound 2.05. Again this concerns these fields only.

### 6.3 Main obstacles

- beta > 2: the slow-tail branch. The leading dilation balances impose no angular equation on the leading tail
  coefficients ("Decay and integrability" in 6.2); the further necessary conditions of section 4 restrict the tails
  but have not excluded this branch. By the compatibility summary after 4.31, for every fixed beta > 2 and a0 > 0, (V)
  to all orders at the center, (V) exactly on any prescribed disk together with every derivative of its residual at
  every point of the axis, and (V) exactly on a prescribed disk together with the exterior of a large ball are each
  consistent with (T) on R^2 and the other properties listed there; the configurations depend on the parameters, with
  no common exterior and no uniform bounds, are not profiles (4.32) and give no evidence for existence. The identity
  E_comp = 0 of 4.32(a) is a necessary condition for every profile; by 4.32(d) it is also sufficient, for a stream odd
  in x with Psi_xy(0) = 1 + beta/2, for (T) and (V) with the normalized primitive, near the center when
  Psi_xxx(0) != 0 and on R^2 for real analytic streams with sublinear velocity (the class conditions remain separate).
  The example of 4.13 ((T) exact, positivity, the center data, the canonical inverse, the slow tail and a global
  source, with a third-order center condition of (V) failing) shows the same within the global-source flow class
  (4.18).
- beta > 2, the compact residual of 4.34: it is not removed here, and one candidate invariant is excluded. Let eta
  be smooth, odd in x and supported in two mirror disks inside |X| < R0, away from the axis, let Phi_eps be the
  area-preserving flow of grad^perp(eps eta), and set W_eps = (Phi_eps)_* W, Theta_eps = Theta o Phi_eps^{-1} and
  Omega_eps = -curl(W_eps - beta X) (the vorticity is recomputed from the new drift, not transported). This
  preserves (T), the parity, the center data, the canonical inverse, positivity for small eps, the backward basin
  and all fields outside the disks; the residual stays compactly supported. The moment int p0 R_Omega dX, with p0
  = x y/r^4, has first variation int eta A p0 dX at eps = 0, where A is the adjoint of the linearized residual
  along these conjugations and A p0(x, 0) = -3 q0 (17 beta + 28)/(2 x^3) < 0 for x > 0; for a suitable eta this
  variation is nonzero. So this moment is not determined by the center data and the exterior fields among such
  configurations. The perturbation creates residual in the disks and leaves the residual of 4.34 outside them
  unchanged; no other obstruction is excluded by this. Not every residual moment is free, however. Let two smooth
  configurations satisfy (T) exactly and have drifts and temperatures that agree outside a compact set, so that
  their relative streams and temperatures differ by compactly supported functions chi and tau. Then the residual
  differences satisfy int delta R_Omega dX = int y delta R_Omega dX = 0, int x delta R_Omega dX = int tau dX and
  int delta R_Theta dX = -(3 beta - 2) int tau dX, where R_Theta = W.grad Theta - (beta - 2) Theta; since R_Theta
  = 0 for both, int tau dX = 0. Hence the moment int x R_Omega dX of a compactly supported vorticity residual is
  unchanged by every such modification, the conjugations above included (under the B2 parity the residual is odd
  in x, so its total and y-moments vanish identically). A repair of a configuration of 4.34 into a profile by a
  modification that keeps the drift and the temperature outside a compact set therefore requires int x R_Omega dX
  = 0. This is only a necessary condition, and it does not constrain modifications that change the exterior drift
  or temperature. For a fixed reference of 4.34 the limit A(theta) = lim r^{-m} Theta_*(r e(theta)) >= 0 exists
  (Theta_* = r^m A + O(r^{m-s})), and, with rho the cutoff of the proof of 4.34, as R -> infinity int x R_Omega dX
  = R^{3-2s} [C_rho m1 + O(R^{-s})], C_rho = int_0^8 (1 - rho(r)) r^{2-2s} dr > 0, m1 = int_0^{2 pi} [1 - (3 - 2s)
  cos^2 theta] A(theta) d theta. When m1 != 0, the configurations of 4.34 with large R therefore admit no such
  repair. The weight 1 - (3 - 2s) cos^2 theta takes both signs, and the value of m1 for the references of 4.34 is
  not determined here. By 4.37 the configurations of 4.34 have the far-field expansion of 4.36, so that for beta
  not in Z_crit the moment equals 2 pi (1 - 3 beta) D, with D the coefficient of x/|X|^2 in the exterior stream.
  The gluing of 4.34 does not use the sign of the reference vorticity. It applies to a continuous one-parameter
  family of references, obtained as follows. Cut the relative stream of a reference of 4.34 off outside a large
  disk, so that far out the drift is beta X and the temperature is r^m A_0(theta), and compose with an
  area-preserving diffeomorphism, commuting with the reflection and equal to the identity near the prescribed
  disk, that agrees far out with the homogeneous map (r, theta) -> (r f'(theta)^{-1/2}, f(theta)) for a circle
  diffeomorphism f commuting with theta -> pi - theta and equal to the identity near the vertical directions; the
  transported temperature has the amplitude A_f(phi) = A_0(g(phi)) g'(phi)^{-m/2}, g = f^{-1}. Making g' small on
  a chosen interval where the weight 1 - (3 - 2s) cos^2 theta has a prescribed strict sign, while keeping it
  bounded below outside a slightly larger such interval, gives two such references with m1 of opposite strict
  signs. Interpolating g linearly between them and restoring the stream Psi_L of the original reference outside
  one fixed large disk (which changes the amplitudes by O(N^{-s}) when that disk has radius N, so N can be chosen
  to keep both signs) gives a continuous family with a common exterior stream, symbol bounds uniform in the
  parameter and vorticity taking negative values somewhere in {x > 0} for every member. Applied to the two end
  members, the expansion of the x-moment above gives, at each fixed sufficiently large gluing radius, moments of
  opposite strict signs. The gluing estimates use uniform bounds, transversality of the exterior drift and the
  damping, and not the sign of the reference vorticity, so one threshold for the gluing radius serves the whole
  family. At such a radius the gluing maps are contractions with a common constant on a common ball, and they depend
  continuously on the parameter uniformly on that ball (the exterior drift is common, and only the incoming
  temperature trace varies), so the fixed point depends continuously on the parameter in the metric of the
  contraction; after an integration by parts of the compensator term the x-moment involves no derivatives of the fixed
  point, so it is a continuous function of the parameter, and the intermediate value theorem gives a member with zero
  x-moment (no continuous dependence on the gluing radius is claimed). This gives, for every beta > 2, a0 > 0,
  prescribed disk and sufficiently large gluing radius, a configuration that has the polynomial core of 4.34(i) on the
  disk, the canonical inverse, (T) on R^2, Theta >= 0, the bounds of 4.34(iii) and a nonzero compactly supported
  vorticity residual with int R_Omega dX = int y R_Omega dX = int x R_Omega dX = 0; Omega takes negative values on
  {x > 0}, the configuration is not a profile, and for beta not in Z_crit its D vanishes, by 4.37 and 4.36 as in the
  preceding sentence. Among these configurations the finite part of 4.38 is not invariant under compact modifications
  that preserve (T) and the exterior fields, whereas int x R_Omega dX is. For a conjugacy as above with eta supported
  in two mirror disks away from the axis inside a disk on which Theta = a0 x^2, Omega = q0 x and R_Omega = 0, the
  three affine residual moments and all fields outside the support of eta are unchanged, and the derivative of f.p.
  int (|V|^2/2 + y Theta) dX at eps = 0 is -4 a0 (5 - 1/beta) int x eta dX, which is nonzero when int x eta dX != 0.
  Applied to the zero-moment configurations inside a polynomial core larger than the prescribed disk, with the
  supports of eta outside that disk, this gives for every beta > 2 arbitrarily small deformations with a nonzero
  finite part that keep all the properties listed for those configurations (the exterior, and hence D, is unchanged).
  Among these configurations the finite part moreover takes every real value. (Twists.) Let B be a closed disk of
  center X_B and radius r_B in {x > 0}, inside that polynomial core and outside the prescribed disk, let varphi be
  smooth on [0, r_B] with compact support in (0, r_B) and varphi' not identically zero, and let eta be the odd
  function equal to -int_{|X - X_B|}^{r_B} t varphi(t) dt on B, to -eta(-x, y) on the mirror disk and to 0 elsewhere.
  Then Phi_eps rotates B about X_B by the angle eps varphi(|X - X_B|) and the mirror disk by the reflected angle;
  every real eps, not only small eps, gives a configuration with all the properties listed, and f.p. int
  (|V|^2/2 + y Theta) dX = a_tw eps^2 + O(1 + |eps|) uniformly in eps, with a_tw >= 2 pi beta^2 int_0^{r_B}
  varphi'(r)^2 r^5 dr > 0. (Far annuli.) If the gluing radius is large enough, the leading exterior vorticity
  Omega_inf = r^{-s} a(theta) of 4.37 satisfies a(theta) >= c_tail cos theta for cos theta >= 0 and some c_tail > 0,
  as in 4.34(iv). Let zeta >= 0 be smooth on (0, infinity), not identically zero, with support in (1, 2), let
  h_ann(X) = zeta(|X|) Omega_inf(X), and for R > 0 conjugate as above by the time-eps flow Phi^R_eps of grad^perp
  h_ann,R, h_ann,R(X) = R^{2-s} h_ann(X/R), which is the identity on |X| <= R and on |X| >= 2R. For fixed eps, as
  R -> infinity, the finite part changes by R^{4-2s} (eps k_1 + eps^2 k_2/2 + o(1)), where k_1 = -(4 beta - 1) int
  zeta(|X|) Omega_inf^2 dX < 0 and k_2 = beta^2 int |grad(X.grad h_ann - 2 h_ann)|^2 dX > 0; for eps = -k_1/k_2 it
  tends to -infinity. The cutoff zeta, the functions h_ann and h_ann,R and the coefficients k_1, k_2 are local to this
  construction. Given a real number E_0, one such annulus beyond a disk that contains the polynomial core, a point
  where R_Omega != 0 and a point of {x > 0} where Omega < 0, with R so large that the finite part falls below E_0,
  followed by twists, whose finite part is continuous in eps, gives a configuration with all the properties listed
  (the constants of the bounds of 4.34(iii) depend on the deformation) and finite part E_0. So for beta not in Z_E the
  necessary condition f.p. int (|V|^2/2 + y Theta) dX = 0 of 4.38(c) holds, together with the vanishing of the three
  affine residual moments and, for beta not in Z_crit, D = 0, in configurations that are not profiles
  ((V) on R^2 is not imposed); this gives no reduction of the residual.
- beta = 2: smooth profiles whose zero arc through the center has flat endpoints (4.7(iii)); near each endpoint their
  vorticity and velocity are in no quasianalytic Denjoy-Carleman class (4.7(xvii)); this criterion gives no exclusion
  under mere smoothness or Gevrey regularity of order greater than 1 there. At an outgoing endpoint Gevrey regularity
  of U or of Omega of order at most 2 on a neighbourhood of the endpoint is excluded: neither W on the side of the
  strong unstable curve beyond the endpoint, uniformly up to the endpoint, nor Omega on a neighbourhood of the
  endpoint satisfies bounds c A^n (n!)^2 for its derivatives of order n in one fixed direction (4.7(xix)(b), (c));
  mere smoothness and Gevrey regularity of order greater than 2 are not excluded. At an outgoing endpoint
  the velocity is harmonic on an open invariant region O that reaches infinity (4.7(iv)), and Theta - L and Omega
  vanish on O and to every order on its boundary. They do not vanish on a neighbourhood of any point of the orbits of
  the strong unstable curve of the endpoint (4.7(xii) at the endpoint itself, 4.7(xv) elsewhere), and U is not
  harmonic near any such point. When Z = gamma, O lies in the open part O_+ or O_- of the basin of the endpoint (the
  basin without the endpoint and its strong unstable orbits), which is a component of the interior of {Omega = 0} and
  of the interior of {Theta = L} (4.7(xv)(c)). The boundary of that open part is the line C^_+ or C^_- formed by the
  endpoint and its two strong unstable orbits, and the complement of the two lines consists of O_+, O_- and a simply
  connected region containing the axis (4.7(xvi)). So Theta - L and Omega vanish on a neighbourhood of no boundary
  point of O_+ or O_-; in the other cases this is not decided at boundary points of O not on these orbits. A harmonic
  extension of the restriction of U to O across a boundary point other than the endpoint, differing from U beyond it,
  is neither excluded by 4.7(xv) and (xvi) nor established. At the endpoint itself, no real analytic field equals W on
  an open subset of O whose closure contains the endpoint (4.7(xix)(a)). No unique continuation argument across such a
  flat boundary has been established in this investigation. A comparable open region has been established at incoming
  endpoints only when the zeros of W off gamma are isolated (Theta = L and Omega = 0 on the side of the strong
  unstable curve beyond the endpoint near it, 4.7(xiv)(b)), and at accumulating endpoints only when some neighbourhood
  of the endpoint contains no arc of zeros of W off gamma (4.7(xx)(b)), although at every endpoint Theta - L and Omega
  vanish to every order along the strong unstable curve (4.7(xiii)(a)). If in addition U is real analytic along the
  normal line through an outgoing endpoint and Omega along the nearby parallel lines beyond it, harmonicity does
  continue from O to a half-square beyond the endpoint, and the continued field extends analytically through the
  endpoint, which is impossible (4.7(xii)(c)); these transverse analyticity properties are not derived from the
  equations. The same contradiction follows if, near the endpoint and on the side of its strong unstable curve beyond
  it, W is a finite sum of products of functions of s and of z in the coordinates of 4.7(iv), with the regularity
  stated in 4.7(xii)(d); this form is not derived from the equations either. The same transverse analyticity is
  impossible at an incoming or accumulating endpoint whose strong unstable curve meets the side {s > 0} of 4.7(iv) in
  every neighbourhood of the endpoint, in particular when some odd-order derivative of the curvature of the zero curve
  at the endpoint is nonzero (4.7(xiii)(b), (c)). Profiles with incoming endpoints have zeros of W off gamma and, if
  these are isolated, an off-axis pair of sources near which Theta is constant and Omega = 0 (4.7(xiii)(d)). If these
  zeros are isolated, the exclusions of 4.7(xii)(b), (xii)(c) and (vi) hold at incoming endpoints, the second without
  the condition on the strong unstable curve (4.7(xiv)(c) to (e)), as do the continuation statement and the Gevrey
  exclusions of 4.7(xix)(a) to (c) (4.7(xix)(e)); if they are moreover nondegenerate, W has no zero on the axis other
  than 0 (4.7(xiv)(f)). At accumulating endpoints Theta - L does not vanish identically on any neighbourhood of the
  endpoint, and, if some neighbourhood of it contains no arc of zeros of W off gamma, the exclusions of 4.7(xii)(b),
  (xii)(c) and (vi) and those of 4.7(xix)(a) to (c) hold there as well (4.7(xx)); these results were obtained in a
  research consultation on accumulating endpoints. For profiles, Theta - L does not vanish identically on any
  neighbourhood of any endpoint, since every open set on which Theta is constant lies in an open invariant set on
  which Omega = 0 (4.7(xxi); this also follows from the scattering identities of 4.7(vii)); the proof uses the
  boundedness of backward orbits, not only the equations near the endpoint. A research consultation on incoming and
  accumulating endpoints found no general exclusion and no local solution of the endpoint equations; the results of it
  that were verified are in 4.7(xiii). A second consultation, on the backward basins at incoming endpoints, gave the
  results entered in 4.7(xiv) and the planar field of its Scope, and no exclusion of incoming endpoints. A further
  consultation, on the global structure when Z = gamma (the open parts of the basins as domains with free boundary,
  the region containing the axis near the strong unstable lines, and integral identities over these regions), found
  further necessary conditions and no exclusion; none of them is entered in section 4. A later consultation, on the
  two cases in which the second form of 4.7(xii)(b) is not established (Theta constant on a subarc of gamma ending at
  an incoming endpoint with nonisolated zeros of W off gamma, or at an accumulating endpoint every neighbourhood of
  which contains an arc of zeros of W off gamma), decided neither case; the necessary conditions obtained in it that
  were verified are in 4.7(xxii). Six other research consultations on the local problem at an outgoing endpoint
  (smooth W and Theta on a disk around it with div W = 4, Omega = -curl W, (T) and (V), the zero set of W an arc
  ending there and the flatness of 4.7(iii)) found neither a local solution nor a general obstruction; they obtained
  reductions and restricted obstructions, the exact reduction obtained in the third is entered, with its proof, as
  4.7(xviii), the restricted exclusion obtained in the fifth as 4.7(xii)(d), the continuation statement, the
  restricted exclusions and the support statement obtained in the sixth as 4.7(xix), and the fourth obtained the
  following exact solutions of the local equations, which limit what these equations force at interior points of a
  zero arc. For every smooth function h of one variable and every constant C, W = (0, 4y - h(x)), Theta = C + h(x) and
  Omega = h'(x) satisfy div W = 4, Omega = -curl W, (T) and (V) on R^2, and the zero set of W is the graph y = h(x)/4.
  Let F(x) = sum_{j >= 1} exp(-j^2) cos(2^j x); F is smooth, and
  |F^{(2m)}(0)| >= exp(m^2 (log 2)^2 - 1/4) for m >= 1 (all terms of F^{(2m)}(0) have the same sign; take the term
  with j nearest to m log 2), so F is in no Gevrey class near 0. With C = 0 and
  h(x) = a0 x^2 + F(x) - F(0) - F''(0) x^2/2, the fields have the parities and the center jet of a profile (W(0) = 0,
  DW(0) = diag(0, 4), Theta = a0 x^2 + O(x^4), Omega = 2 a0 x + O(x^3)), while h, and hence the zero graph, is in no
  Gevrey class near 0. For every smooth t, W = (4x, 0), Omega = 0 and Theta = t(y) also satisfy these equations, with
  the analytic zero line x = 0 and the temperature trace t on it, which may be taken in no Gevrey class (for example
  t(y) = y + F(y) - F(0)). In neither family is U = W - 2X sublinear, so these are not profiles. Thus the local
  equations force neither analyticity nor Gevrey regularity of a zero arc, even together with the center jet of a
  profile, nor Gevrey regularity of the temperature trace on an analytic zero arc (the example is a vertical line).
  Regularity on a prescribed analytic nonvertical arc, and within the class of profiles, is not decided. The fifth
  also determined the type of the equations of 4.7(xviii)(a) with a as the evolution variable. Write X_r = rho e,
  e = (cos phi, sin phi), alpha = X_a.X_r/rho^2 and omega = Omega o X; det(X_a, X_r) = 1 gives
  X_a = alpha X_r - rho^{-1} (-sin phi, cos phi), and the compatibility X_ar = X_ra together with (E) gives, for
  r != 0, rho_a = alpha rho_r - rho^{-1} phi_r + alpha rho/r - omega/(4 r rho), phi_a = alpha phi_r + rho^{-3} rho_r
  and alpha_r = alpha/r - 2 rho^{-2} phi_r - omega/(4 r rho^2). The first two equations have the characteristic
  speeds alpha +- i rho^{-2}, so they form an elliptic system; the third contains no derivative in a, and, for
  prescribed theta, the determinant of the principal symbol of the whole system for (rho, phi, alpha),
  eta ((xi - alpha eta)^2 + rho^{-4} eta^2) for the covector (xi, eta) dual to (a, r), vanishes on the conormal of
  C = {a = 0}. At r = 0 the equations before the division by r degenerate and require, in particular,
  alpha rho^2 = omega/4. With the data of 4.7(xviii)(b) on C, and with theta as a further unknown, this is a Cauchy
  problem for an elliptic system coupled to a characteristic constraint; neither its solvability nor an obstruction
  is established. Both equations can hold near the center and along the open zero arc in smooth configurations that
  are not profiles. For every a0 > 0 and R0 > 0 there are smooth Psi and Theta on R^2, Psi odd and Theta even in x,
  Theta >= 0 with zero set exactly the axis, such that U = (-Psi_y, Psi_x) is the canonical whole-plane inverse of
  Omega = -Lap Psi, with an absolutely convergent Biot-Savart integral, U(0) = 0 and U = O(1/|X|). The field
  W = 2X + U satisfies (T) on R^2, and Psi = 2xy - a0 x^3/3 and Theta = a0 x^2 on {|X| <= R0}, so both equations and
  the center data of 4.1 hold there. The zero set of W is one compact smoothly embedded arc through 0, with all the
  properties of the arc listed in 4.7(iii), and (V) holds on an open neighbourhood of the arc minus its endpoints. At
  both endpoints every derivative of Omega and of Theta - L vanishes, with L > 0. Both endpoints are of the outgoing
  type (b) of 4.7(iv); for each there is a nonempty open set O', invariant in both time directions and consisting of
  orbits with backward limit at that endpoint, on which Theta = L but Omega is not identically zero, so (V) does not
  hold identically on O'. Along each ray from 0 into {x > 0, y > 0} close enough to the positive y-axis, |X| R_Omega
  has a negative limit at infinity, and Omega changes sign on {x > 0}. Near each endpoint its strong unstable curve
  is a straight segment, so the condition of 4.7(vi) is not met. A further compactly supported area-preserving
  diffeomorphism, commuting with the reflection, equal to the identity near the disk {|X| <= R0} and near every
  interior point of the arc, and flat relative to the identity at both endpoints, replaces these segments by smooth
  curves that agree with no regular real analytic embedded curve germ through the endpoint; all other properties
  asserted above for the constructed configuration are preserved. At each endpoint (V) then fails to hold identically
  on a nonempty open set invariant in both time directions, and it fails at points of the new strong unstable curve
  arbitrarily close to the endpoint. So these properties of the configuration, together with the necessary condition
  of 4.7(vi), do not imply the profile equations; the deformation does not make the basin of an endpoint harmonic,
  and it is not a nonexistence result. The same construction, with a temperature on the arc equal to L on a subarc
  ending at each endpoint and a compactly supported correction of Psi near each endpoint, flat at the endpoint and
  built from exp(-z^{-1/2}) in a complex coordinate z centered there, gives another configuration that is not a
  profile. It has all the properties listed above for the configuration before the further deformation, except that
  its strong unstable curves agree with no regular real analytic embedded curve germ through the endpoints. In
  addition, near each endpoint, Omega = 0 and Theta = L on its strong unstable curve and on its local outgoing side,
  so both equations hold there, including on a nonempty open set whose backward orbits stay near the endpoint and
  converge to it. In the coordinates (s, z) of 4.7(iv) at either endpoint, on a sufficiently small half-disk s >= 0,
  W = (Re g, 4z - Im g) with g = exp(-w^{-1/2}), w = s + i z (principal branch for w != 0, and g = 0 at w = 0), so
  Omega = 0 there and the hypothesis of 4.7(xii)(c) on Omega holds; but W_s(0, z) = exp(-a) cos a for z != 0,
  a = (2|z|)^{-1/2}, extends by 0 to a flat function that is nonzero at points arbitrarily close to 0, so z -> U(0, z)
  is not real analytic on any interval about 0 and the hypothesis of 4.7(xii)(c) on U(0, .) fails. For this
  configuration too, the invariant set O' at each endpoint can be chosen so that Theta = L on O' and Omega is not
  identically zero on O', so (V) does not hold identically on O'; since Theta = L on a whole neighbourhood of each
  endpoint, (V) fails at points arbitrarily close to each endpoint, as 4.7(xii)(b) requires. It also fails in the
  exterior. The original configuration is obtained by deforming a transport configuration whose zero set of W is a
  segment of the x-axis by a compactly supported area-preserving map; near that segment this first map is the shear
  (x, y) -> (x, y + Theta_b(x, 0)/4), with Theta_b the temperature of the base configuration. So the center data, (V)
  near the center and along the open arc and the flatness of 4.7(iii) at the endpoints are compatible, and an
  exclusion of smooth profiles at beta = 2 must use (V) elsewhere, for example on whole neighbourhoods of the
  endpoints (4.7(iv), (vi), (xii)).
- Numerics: the slow algebraic tail r^{-1/beta} makes the whole-plane inverse with its exterior mandatory and the far
  field poorly determined; for beta > 2 the center is a source with eigenvalue ratio (3 beta + 2)/(beta - 2), and a
  representation must enforce smooth Taylor compatibility at 0 as well as parity to avoid non-smooth resonant terms
  (at beta = 2 the eigenvalues at the center are 0 and 4); beta is an unknown; and no state with small residuals has
  been reached.

## 7. Verification timeline (UTC)

All times are UTC. This section gives the dated milestones of the verification, one entry per result or group of
results, ordered by first time; a time range runs from the first derivation or report to the last check. The complete
timeline, with every verification report, referee audit and correction and the time at which each correction was
adopted, is among the accompanying artifacts. Table 8.1 identifies for each result of section 4 its independent proof
packets and analytic consultations, and Table 8.2 the exact certificates of sections 6.1 and 6.2. "Verification" is
the independent verification (separate derivations and code; numerical audits with a separate evaluator, inverse and
residual code and no solver code imported), "referee" an independent analytic referee, and "analysis" the derivations
of the authors of this report. Each result of section 4 carries a verification verdict and a referee verdict (Table
8.1); for 4.5 and 4.10 the first referee verdict is that of 2026-10-21 03:00 to 03:11.
- 2026-10-20 12:44 Start of the investigation (analysis, numerical computation and independent verification carried
  out separately).
- 2026-10-20 12:55 to 13:16 The independent verification rederived (B2-P), the reduced equations and the center
  identities (CONFIRMED) and tested a modal and a Cartesian whole-plane inverse (the latter with Duffy quadrature and
  a compactified exterior, 13:12) on manufactured fields, including a slowly decaying one. 13:03 Specification of the
  admissible class, canonical inverse and diagnostics fixed.
- 2026-10-20 13:23 to 14:04 4.1 to 4.8. Referee audits: 13:23 (4.1 to 4.4 and the vorticity representation: VALID or
  VALID WITH FIXES), 13:42 (4.6: VALID WITH FIXES, with the stronger conclusion now stated), 14:04 (4.7(i) VALID WITH
  FIXES, 4.7(ii) VALID, 4.8 VALID WITH FIXES). Independent verification: 13:25 (4.6, with scope repairs; own proof of
  4.5), 13:34 (4.2 to 4.4), 13:46 (4.8 by its own derivation; also the material-center translation eigenmode of the
  dynamic-rescaling linearization, rate 1 + 3 beta/2). The independently derived proofs of 4.7(i), (ii) checked in the
  analysis 13:49. Fixes adopted.
- 2026-10-20 13:46 to 18:47 First independent numerical audits (separate evaluator, no solver code imported): 13:46
  the 42 rational-fit trials of one method REFUTED as candidates; 14:11 an intermediate solver state REFUTED
  (non-smooth center terms) and the compact-cutoff polynomial trap CONFIRMED as a finite-box artifact; 15:13 and 17:15
  defects of the solver's velocity interpolation CONFIRMED; 15:43 and 17:12 the eps = 0 starting states evaluated,
  with their true (B2-P) residuals (Table 6.1b) after the audit of 17:12 found that the evaluation of 15:43 had used
  the external forcing velocity; 16:49 the three eps = 0.34 states REFUTED as candidates (Table 6.1a); 18:07 to 18:47
  a self-source check of the independent inverse and the correction of its attribution.
- 2026-10-20 14:03 to 14:35 4.8 under sublinear velocity only (Omega not in L^p, 1 <= p <= beta): CONFIRMED by the
  verification and VALID (referee 14:29). 4.9: derived in the analysis 14:18; CONFIRMED with repairs by the
  verification 14:28 to 14:34 (positive-part form; the critical case p = 2 beta under sublinear velocity alone);
  referee 14:33: VALID, one signed half-ball claim INVALID and replaced by the positive-part statement.
- 2026-10-20 14:04 to 15:07 4.10 and 4.11: 4.10 proposed with proof by a referee (14:04) and derived independently by
  the verification (14:15); the sector bound 4.11(i) derived by the verification 14:32 to 14:35 and checked in the
  analysis 14:58; referee 15:06: 4.11(i), (ii) and the flatness of Omega in 4.7(ii) VALID, 4.11(iii) VALID WITH FIXES
  (adopted); verification 15:07: 4.11(ii), (iii) CONFIRMED.
- 2026-10-20 14:51 First referee review of the full interim report: the principal arguments sound under the class A
  hypotheses; requested clarifications adopted.
- 2026-10-20 15:00 to 15:30 4.6 restated under the orbit-integral hypothesis (D): CONFIRMED by the verification 15:00
  to 15:04; referee 15:28: VALID, one exponent inequality corrected, and (D) not implied by smoothness, sublinearity,
  parity and the center data (shear example); entered 15:30.
- 2026-10-20 15:12 to 16:28 4.13: (i) to (iii) and the one-equation example from a referee report, extended in the
  analysis to the sign-free case (15:12 to 15:22); (v) to (vii) derived in the analysis 15:22 to 15:41; verification
  15:26 to 16:07: CONFIRMED by independent proofs; referee 15:28 ((i) to (iii) VALID, with the stronger arithmetic and
  the parity of r + d) and 16:27 ((v), (vi) VALID WITH FIXES, (vii) VALID); entered 16:16 and 16:28.
- 2026-10-20 15:35 to 16:16 First items of 4.14 (literature): primary texts retrieved and quoted; verification 16:07:
  verdicts CONFIRMED with corrections; referee 16:08: VALID WITH FIXES, one decay inference INVALID as written;
  corrections adopted 16:15. Citation details of 4.14(a) checked against two arXiv versions at 19:29.
- 2026-10-20 15:53 to 16:27 4.12: (a) to (c) proposed with proof by a referee and rederived in the analysis 15:55 to
  16:00; verification 16:02: CONFIRMED by an independent second proof, including (d) and (e); referee 16:06: VALID
  WITH FIXES (adopted); entered 16:11; (f) CONFIRMED and VALID at 16:27.
- 2026-10-20 16:04 to 16:53 4.15: derived in the analysis 16:04; referee 16:18: VALID WITH FIXES; verification 16:27
  to 16:31: CONFIRMED; the extension to polynomially bounded vorticity CONFIRMED by the verification 16:37 and VALID
  (referee 16:47, one wording fix); exponent iteration checked in the analysis 16:53.
- 2026-10-20 16:15 to 17:12 4.16: second far-field terms CONFIRMED by the verification 16:15 and VALID (referee
  16:37); velocity terms CONFIRMED 16:31 to 16:47 (with a manufactured inverse test) and VALID (referee 17:11);
  entered 17:12.
- 2026-10-20 16:44 to 17:05 4.7(iii), (iv) and 4.12(g): derived by a referee (research question) and the identity
  generalized in the analysis to every beta >= 2 (16:44 to 16:48); referee audit 16:58: VALID, the endpoint
  alternative VALID WITH FIXES; verification 17:02: CONFIRMED by independent proofs; entered 17:05.
- 2026-10-20 17:21 to 17:44 4.17 and 4.18: derived by a referee (research question); verification 17:27: the argument
  by uniqueness of the linearization for the parity of the coordinates REFUTED (an explicit second C^1 conjugacy) and
  the coordinates CONFIRMED by an explicit construction; referee 17:37: VALID, the coordinates VALID WITH FIXES;
  verification 17:39: CONFIRMED, including the class A extension; entered 17:44.
- 2026-10-20 17:34 to 18:13 4.7(v) to (vii): derived by a referee (research question); referee audit 17:52: VALID, two
  items VALID WITH FIXES; verification 18:01: CONFIRMED, with a separate proof of 4.7(vi); entered 18:13.
- 2026-10-20 17:56 Second referee review of the full interim report (state of 17:37); clarifications and scope
  corrections adopted 17:57 to 18:10.
- 2026-10-20 18:01 to 18:23 4.7(viii): CONFIRMED by the verification (own proof); referee 18:23: VALID, the analogue
  for beta > 2 INVALID; entered 18:23.
- 2026-10-20 18:16 to 18:36 4.7(ix): CONFIRMED by the verification (own proof); referee 18:34: VALID WITH FIXES;
  entered 18:36.
- 2026-10-20 18:17 to 18:53 4.19: derived by a referee (research question); referee audit 18:27: VALID, with proof
  completions; verification 18:32: CONFIRMED; entered 18:37; scope correction requested by the verification 18:42
  (necessary arithmetic conditions do not establish resonant configurations), made 18:53.
- 2026-10-20 18:26 to 19:03 4.7(x): derived in the analysis; referee 18:45: VALID WITH FIXES; verification 18:56:
  CONFIRMED; entered 19:03.
- 2026-10-20 18:32 to 23:39 4.7(xi): complete proof by the verification 18:32, CONFIRMED 18:39 (the corollary 18:54);
  referee 23:13: VALID; the draft CONFIRMED against the proof 23:21; entered 23:33; entered text CONFIRMED 23:39.
- 2026-10-20 18:34 to 19:19 4.20: proposed by a referee; verification 18:56: CONFIRMED, with the extension to odd
  finite order; referee audit 19:16: VALID WITH FIXES; entered 19:19.
- 2026-10-20 18:47 to 19:01 Convention audits by the verification: the stream function in the proof of 4.18(c) had the
  wrong sign (the velocity used and the exclusion were correct), corrected 19:01; the attribution of a self-source
  inverse check corrected to Table 6.1b at 19:00.
- 2026-10-20 19:33 to 20:00 4.21: derived by a referee; re-proved in the analysis 19:39; referee audits 19:43 and
  19:58: VALID WITH FIXES; verification 19:47: CONFIRMED, with a strengthening (adopted); entered 20:00.
- 2026-10-20 19:37 Second re-read of 4.7(x), 4.9(iii), 4.13, 4.16(2) and 4.20 as entered: no gap at the stated
  hypotheses; three wording repairs.
- 2026-10-20 19:53 to 20:15 4.22: CONFIRMED by the verification (19:56; the draft text 20:00); referee 20:03: (a) to
  (c) VALID, (d) VALID WITH FIXES; entered 20:06; re-read of 4.21 and 4.22 by the verification 20:14: CONFIRMED, a
  summary sentence of Q1 REFUTED as worded and corrected 20:15.
- 2026-10-20 20:07 to 21:50 Forced continuation states at fixed beta (two to three resolutions, two map scales; forced
  residuals 1e-3 to 7e-3, (B2-P) residuals 0.76 to 0.95; REFUTED as candidates; the turning of the fitted states
  CONFIRMED as an empirical property), the first beta-free state (21:29; not a converged root) and further states at
  beta = 3.5 and 2.25 (21:50; one, flagged converged by the solver, REFUTED as a small-residual forced state).
- 2026-10-20 20:19 to 21:06 4.23(a) to (f): derived in the analysis 20:19 and independently 20:36; verification 20:46
  and 20:59: CONFIRMED, with scope repairs; referee 20:50: VALID WITH FIXES and 21:01: VALID, with the sign inference
  of (e) corrected and the scope paragraph restricted; entered 21:06.
- 2026-10-20 20:43 to 21:06 4.14(f), (g): verification 20:43: CONFIRMED with two repairs; literature referee 21:04:
  VALID WITH FIXES; entered 21:06.
- 2026-10-20 21:41 to 22:05 Third referee review of the full interim report (20 items; no YES or NO supported),
  adopted 21:50; the proof repairs CONFIRMED by the verification 21:57, one precision adopted 22:05.
- 2026-10-20 22:14 to 22:50 Second construction of 4.23(c): proof by the verification 22:14; checked in the analysis
  22:25; referee 22:38: VALID WITH FIXES; entered 22:43; entered text CONFIRMED 22:50.
- 2026-10-20 22:18 to 23:45 Additive-source states, second-dipole states and the beta-free stages eps = 0.025 and 0.03
  (evaluations 22:28, 22:42 to 22:50, 23:10 to 23:37 and 23:27 to 23:45; forced residuals 0.006 to 0.23, (B2-P)
  residuals 0.75/0.48 to 1/0.99); Tables 6.1c and 6.1d with regional maxima from the saved raw arrays; all REFUTED as
  small-residual (B2-P) states; wording corrections of 6.1 adopted 22:20, 22:36 and 22:52.
- 2026-10-20 22:20 to 22:28 4.14(h) to (j): CONFIRMED by the verification against independently retrieved primary
  texts and VALID WITH FIXES (literature referee); entered 22:25; entered text CONFIRMED 22:28.
- 2026-10-20 22:34 to 23:01 4.24: proofs by the verification 22:34 and 22:41; partial referee audits 22:40 and 22:43:
  VALID; re-derived in the analysis 22:46 to 22:49; referee audit of both texts 22:57: confirmed without gaps; entered
  23:01.
- 2026-10-20 23:09 to 23:43 4.25: derived in the analysis 23:09; referee: VALID WITH FIXES (adopted 23:17);
  verification 23:21: CONFIRMED by an independent proof; entered 23:33; entered text CONFIRMED 23:39. Second part
  (free half-axis): proposed and proved by the verification 23:17 to 23:25; re-derived in the analysis 23:36; draft
  CONFIRMED against the proof 23:39; referee 23:42: VALID; entered 23:43.
- 2026-10-20 23:12 to 23:44 Third construction of 4.23(c): proof by the verification 23:12; referee 23:27: VALID WITH
  FIXES; verification 23:21: CONFIRMED, one local estimate of the draft REFUTED (a weaker bound suffices; corrected
  23:31); entered 23:33; entered text CONFIRMED 23:39.
- 2026-10-20 23:35 to 23:56 Exact endpoint expansion of six stored representations (exact rational arithmetic):
  CONFIRMED by the verification; referee: VALID WITH FIXES; entered in 6.1 at 23:56.
- 2026-10-20 23:45 to 2026-10-21 00:08 4.26(a) to (c): derived and CONFIRMED by the verification (23:45 and 23:51,
  with exact Cartesian identities and a manufactured inverse); re-derived in the analysis; referee 00:07: VALID WITH
  FIXES; entered 00:08.
- 2026-10-20 23:53 to 2026-10-21 00:23 4.27: derived and CONFIRMED by the verification (23:53; example (d) 00:09 to
  00:20); re-derived in the analysis 00:13 to 00:16; referee 00:21: VALID; entered 00:23.
- 2026-10-20 23:56 to 2026-10-21 05:20 Forcing homotopy (lambda path) and beta-free stages: independent evaluations at
  lambda = 0.98 to 0.94 with 12 to 40 angular modes and of the beta-free stages eps = 0.035 and 0.04; exact positivity
  certificates of the temperatures (01:46), exactly nonzero temperature tail coefficients and exact C2 enclosures; all
  CONFIRMED as diagnostics and REFUTED as candidates; re-reads 03:21 and 04:00 with bookkeeping corrections (60 saved
  states with distinct archives; a third map scale of one forced state, evaluated at 01:32).
- 2026-10-21 00:26 to 02:55 Far-field constants of the stored states: the closed form for the constant C (2 < b < 3;
  referee VALID WITH FIXES 00:34), the logarithmic constant at beta = 3 (00:31 to 01:22; referee VALID WITH FIXES
  01:21), exact C2 enclosures for the four beta-free states (01:48 to 02:11) and for the 16-mode states (3 < b_rep <
  4; 02:36; referee VALID WITH FIXES; draft re-read 02:49); entered 01:00 to 02:55.
- 2026-10-21 01:00 to 02:44 Methods of 6.2 that failed: the transport-exact generating-function representation
  (formulas CONFIRMED 01:13; pilot closed 01:37; saved states REFUTED 02:03), the dynamic-rescaling pilot
  (time-stepping failure reproduced 02:33; a slow-tail defect of its inverse found 02:31) and an independently
  implemented stream-function trial space (sixteen fits 02:16 to 02:41, all REFUTED); entered 02:23 and 02:44.
- 2026-10-21 01:03 to 02:03 4.26(d): own proof of the verification (01:03, CONFIRMED 01:06); referee 01:30 to 01:38:
  VALID, the first step VALID WITH FIXES; draft CONFIRMED 01:47; entered 01:52; entered text CONFIRMED 02:03.
- 2026-10-21 02:07 to 07:16 4.35 (axis subsystem in G): the construction and the formula for Q_+ proved by the
  verification 02:07 to 02:18 (CONFIRMED); referee: VALID WITH FIXES (corrected paragraph adopted); entered in 6.2 at
  02:55; stated as the numbered result 4.35 at 06:48; the numbered statement CONFIRMED by the verification 06:55;
  separate audit 06:46 to 06:56: VALID WITH FIXES for (a), (b), (d) and the Scope, (c) VALID; fixes adopted 07:16.
- 2026-10-21 02:18 to 02:38 Fourth referee review of the full interim report (state of 02:11): the new theorems
  survive with their stated hypotheses; required changes adopted 02:38.
- 2026-10-21 02:57 to 04:07 Further trial spaces of 6.2: ten free-beta fits in the stream-function trial space, all at
  the imposed lower bound beta = 2.02 (REFUTED 03:13, entered 03:23), and twelve fits of its fractional-tail variant
  (nonzero third-order center coefficients, REFUTED 03:54, entered 04:07).
- 2026-10-21 03:00 to 03:11 Referee audit of 4.5, 4.10, 4.11 and 4.12(f): 4.5, 4.10 and 4.12(f) VALID, 4.11 VALID WITH
  FIXES (adopted 03:11); the first referee verdict for 4.5 and 4.10.
- 2026-10-21 03:37 to 04:02 4.28: derived in the analysis with exact rational self-checks; referee 03:54: (a) VALID,
  (b) and the Scope VALID WITH FIXES; verification 03:55: CONFIRMED (own recursion through degree 12); entered 04:02.
- 2026-10-21 03:44 to 04:52 4.29: (b) to (d) obtained in an external research consultation, (e) derived in the
  analysis; referees 04:11 ((e) VALID WITH FIXES) and 04:13 ((b) to (d) VALID); verification 04:19, 04:28 and 04:33:
  CONFIRMED; entered 04:37; entered text CONFIRMED 04:52.
- 2026-10-21 04:27 to 05:29 4.30, 4.31(a) and 4.32: 4.30 and 4.32 obtained in the verification (CONFIRMED 04:42 and
  04:51), 4.30 also by a second route and 4.31(a) in external research consultations; referees 04:59 (4.31(a) VALID
  WITH FIXES) and 05:12 (4.30 VALID; 4.32(a) to (c) VALID; the Scope of 4.32 INVALID as written and replaced);
  verification 05:03: 4.31(a) CONFIRMED; entered 05:15; entered text CONFIRMED 05:25 except one Scope sentence of 4.32
  (REFUTED; corrected 05:29).
- 2026-10-21 05:11 to 06:01 4.31(b): obtained in the verification (CONFIRMED 05:11); referee 05:12: the combination
  VALID; entered 05:20; adversarial referee audit of the entered text 05:28 to 05:44: VALID WITH FIXES (statement
  unchanged; proof and Scope replaced 05:52); revised proof CONFIRMED paragraph by paragraph 06:01.
- 2026-10-21 05:23 to 06:51 4.34: a first external research consultation (05:23 to 05:39) without a construction; a
  second (05:46 to 06:12) with the construction; referee audit 06:14 to 06:25: VALID WITH FIXES; verification 06:14 to
  06:28: CONFIRMED by its own proof; entered 06:32; entered text CONFIRMED 06:45, with a scope clarification of 4.31
  adopted 06:51.
- 2026-10-21 05:33 to 06:28 Angular refinement at fixed forcing: common-grid comparison of the 24-, 32- and 40-mode
  states at lambda = 0.95 (CONFIRMED as a finite sampled refinement, 05:37; entered 05:41), and the 40-mode states at
  lambda = 0.945 and 0.94 with the 32-to-40 comparisons (CONFIRMED as measurements, REFUTED as profiles; 05:54 to
  06:28).
- 2026-10-21 05:39 to 06:48 Fifth referee review of the full interim report (state of 05:39): no YES or NO supported;
  seventeen requested changes; the substantive ones adopted 06:06 to 06:12, the numbered statement of the axis
  assertions of 6.2 (4.35) and the quantifier wording of 6.3 at 06:39 to 06:48; the remaining editorial items
  (traceability of the section 4 opening, shortening, the artifact manifest) at the end of the run.
- 2026-10-21 05:46 to 06:45 4.33: verification 05:46 and 06:17: CONFIRMED; referee audit 06:04 to 06:20: VALID WITH
  FIXES; entered 06:27; entered text CONFIRMED 06:45.
- 2026-10-21 06:09 Horizontal primitive representation (section 6.2): 18 fits run by the verification (fixed beta
  2.25, 2.75 and 3.5 and free beta, three resolutions), all refuted as exact fields by exact Taylor and angular-moment
  tests; no candidate.
- 2026-10-21 06:26 to 07:14 Removal of the compact residual of 4.34 (separate research consultation): no obstruction
  identity and no cokernel element found; surjectivity of the coupled linearization and global estimates left open;
  nothing entered.
- 2026-10-21 06:31 to 08:52 Second search in the horizontal primitive representation (section 6.2): 18 fits run by the
  verification 06:31 to 08:48 with the center data, the leading angular moments and the Taylor conditions of (T)
  through degree 4 imposed exactly; final summary 08:50: all eighteen stored fields refuted as exact B2 profiles by a
  nonzero degree-five Taylor coefficient of the residual of (T); nonzero horizontal offsets additionally certified for
  the six final fields; entered 08:52.
- 2026-10-21 06:45 to 07:38 4.32(d) (converse of the compatibility identity), 4.33(e) (horizontal offsets) and a Scope
  sentence of 4.34: verification 06:45, 06:54, 07:03 and 07:17: CONFIRMED; separate audits 07:14 to 07:20 (VALID WITH
  FIXES for each part) and 07:19 to 07:22 (the smooth local statement VALID); entered 07:25; entered text CONFIRMED
  07:38.
- 2026-10-21 06:55 to 07:01 Summary of findings: verification read 06:55: five scope corrections required (no distance
  to the solution set; approximate forced states; the circle supremum of Theta; vorticity of either sign in the open
  core; the hypotheses of the axis integrality conditions), adopted 07:01.
- 2026-10-21 07:28 to 07:58 Whole-report review (separate referee, answered 07:46): ten items; adopted 07:52 to 07:58:
  every exact certificate of 6.1 and 6.2 indexed in Table 8.2, two stale cross-references corrected, the
  leading-balance wording of 6.2 and 6.3 made precise, a compact state table (Table 6.1e) added, and the proof outline
  of 4.34 expanded (norms, trace problem, completeness, weighted energies, coefficient-one div-curl estimate,
  angular-limit equation); separate audit of the revision asked 07:57; verification of the revisions 08:07: CONFIRMED,
  with two caption and index repairs adopted 08:09; headline deferred to completion.
- 2026-10-21 07:36 to 07:45 Compact conjugacy in the polynomial disk of 4.34 (section 6.3): verification 07:36:
  CONFIRMED; separate audit 07:38 to 07:43: VALID WITH FIXES (a suitable generator for the nonzero variation;
  restriction to configurations with a nonzero residual); entered 07:45.
- 2026-10-21 07:47 to 07:58 State table of 6.1 (Table 6.1e, 57 states with independent evaluations); prose of 6.1
  corrected against it at 07:56; the state at beta = 3.0315 (verification 07:49: REFUTED as an unforced profile; C2 in
  [-4537.558, -4537.557]) entered 07:58.
- 2026-10-21 07:52 to 07:58 Compact-conjugacy sentence of 6.3: verification 07:52: CONFIRMED with a definition
  clarification (the vorticity is recomputed from the new drift), adopted 07:58.
- 2026-10-21 07:57 to 08:04 Revised proof outline of 4.34: separate audit 07:57 to 08:02: VALID WITH FIXES (the
  seminorm domain and the zero-order norm defined; the potential operator renamed and the auxiliary vorticity source
  distinguished from the vorticity change; the uniform Lipschitz bound of the angular flow from an integrable angular
  coefficient; M_1, M_2 uniform in the iterates and in R; the identification of weak limits stated; R1 = 8R in Scope);
  all adopted 08:04; verification 08:07: CONFIRMED against the complete proof.
- 2026-10-21 08:00 to 08:21 Invariant x-moment of a compact residual (section 6.3): verification 08:00: CONFIRMED;
  separate audit 08:07 to 08:12: VALID WITH FIXES (the drift and the temperature, not the physical velocity, fixed
  outside a compact set; a necessary condition only); entered 08:16; verification of the entered sentences 08:21:
  CONFIRMED.
- 2026-10-21 08:13 to 08:40 Large-R x-moment of the residual of 4.34 (section 6.3): separate audit 08:13 to 08:23:
  VALID WITH FIXES (0 <= rho <= 1 explicit; an L^1 bound of the temperature difference on B_8; remainder O(R^{-s}));
  verification 08:36: CONFIRMED for a fixed reference (the reference temperature r^m A + O(r^{m-s})); entered 08:40.
- 2026-10-21 08:27 to 09:05 4.36 (renormalized impulse under a far-field expansion): research consultation (asked
  08:27, answered 08:37) deriving the boundary formula, the critical set Z_crit and (a), (b); separate audit of the
  draft 08:41 to 08:50: VALID WITH FIXES (all adopted 08:53); verification 09:01: CONFIRMED by its own proof and exact
  controls; entered 09:02 to 09:05; the entered text and its cross-references re-read 09:14: CONFIRMED.
- 2026-10-21 08:54 to 09:17 Beta-parameterized 32-mode states at beta = 3.04, 3.05 (verification 08:54) and 3.062
  (verification 09:14): REFUTED as unforced profiles (forced ratios growing to 0.068/0.11; exact thermal-tail
  witnesses; C2 enclosures excluding 0); entered in Table 6.1e, the C2 list and a 6.1 paragraph on the run, with a
  Summary sentence and the Table 8.2 row, 09:15 to 09:17.
- 2026-10-21 09:05 to 10:04 4.37 (finite exterior expansions): verification 09:23: CONFIRMED by its own proof and
  controls, including the class A application; the draft of the analysis checked by the verification 09:47: CONFIRMED
  with one normalization fix (the remainder stream odd in x), adopted 09:50; separate audit of the draft 09:40 to
  09:52: VALID WITH FIXES ((T) on R^2 for the identity of 4.36 and beta not in Z_crit for its reduction to the dipole
  coefficient; the unique odd smooth remainder stream; an explicit weight schedule; uniqueness after combining terms),
  all adopted 09:53; entered 09:55, with the Scope of 4.36 and the cross-references in the Summary, Q1, 6.3 and
  section 8 updated 09:55 to 09:57; the entered text re-read by the verification 10:01: CONFIRMED with one precision
  fix (the identity of 4.36 needs (T) on R^2 and x R_Omega in L^1, only its reduction to D needs beta not in Z_crit),
  adopted 10:04.
- 2026-10-21 09:21 to 10:01 4.38 (renormalized energy): research consultation (asked 09:21, answered 09:31) deriving
  the identity, the power count, the set Z_E and the reduction, with the cubic flux term added to the power count;
  separate audit of the draft 09:36 to 09:45: VALID WITH FIXES (the sign examples of (d), the scaling and observer
  scope, the comparison with 4.36), adopted 09:47; verification 09:47: CONFIRMED by its own proof and 181 exact
  controls, including the depth of 4.37 and fields with D = 0 of either energy sign that violate (V); entered 09:55;
  the entered text re-read 10:01: CONFIRMED.
- 2026-10-21 09:24 to 09:37 Regional residual reduction extended to 72 saved states (verification 09:24): the overall
  range 0.73 to 1 CONFIRMED; the lower bound 0.29 on the four outer intervals REFUTED for 72 states (0.288964 at beta
  = 3.04) and replaced by 0.2889; the beta-run paragraph CONFIRMED, with the cause of the growing forced residuals
  (resolution or nonlinear convergence) left open; corrected text entered 09:37.
- 2026-10-21 09:30 to 10:34 Section 6.3: the glued configurations with vorticity of both signs and zero affine
  residual moments (verification 09:30: CONFIRMED) and the variation of the finite part of 4.38 under compact
  conjugacies (verification 09:59: CONFIRMED), with the temperature derivative bounds of 4.34(iii) (noted by the
  verification 10:01 as proved in the gluing packet): separate audit 10:07 to 10:15: VALID, and VALID WITH FIXES for
  the finite part (the comparison with 4.38 only for beta not in Z_E; mirror supports; the list of retained
  properties), all adopted; the draft checked by the verification 10:11: CONFIRMED, with the same restriction to beta
  not in Z_E; 4.34(iii) and its proof, the end of the 6.3 bullet and the Table 8.1 row of 4.34 entered 10:17 to 10:20;
  entered text re-read by the verification 10:34: CONFIRMED.
- 2026-10-21 09:38 to 10:04 First state of a second forced path (24 modes, lambda = 0.99, beta = 3.0867, a different
  seed and source; verification 09:38): REFUTED as an unforced profile (forced ratios 0.00025/0.00026, (B2-P) ratios
  0.74/0.42, exact positive-power thermal-tail witnesses, C2 in [-425.908, -425.907]); regional reduction extended to
  73 states (verification 09:42): the common outer bound 0.0987 (0.2889 without this state) and the overall range 0.73
  to 1 CONFIRMED; entered in Table 6.1e, a 6.1 paragraph, the regional sentence, Table 6.1c, the Summary and the
  reproduction row of Table 8.2, 09:48 to 09:55; re-read 10:01: CONFIRMED, with L2 added to the sampling list of Table
  6.1e 10:04.
- 2026-10-21 10:01 to 10:24 Targeted review of the text entered since 09:06 (separate referee, asked 10:01, answered
  10:16): 4.37 and 4.38 survive; no YES or NO supported; adopted 10:17 to 10:24: the parameter restriction made
  explicit in 4.38(c), the compared quantity defined in the regional sentence of the L2 paragraph, two table
  references of this section and one caption wording corrected, three line-initial list markers removed (the
  distinction of identity and reduction in 4.37 already adopted 10:04); the completion items (end time, elapsed time,
  artifact manifest and registry) at the end of the run.
- 2026-10-21 10:11 to 10:34 Saved failed stage of the second path (lambda = 0.98, beta = 3.0415; verification 10:21):
  the failure of the center-strain condition CONFIRMED (2.49183 against 2.52077, by two independent inverses), REFUTED
  as an unforced profile (forced ratios 0.027/0.0094, (B2-P) ratios 0.75/0.42, exact positive-power thermal-tail
  witnesses, C2 in [-228.011, -228.010]); the other six states of that stage not available for checking, and no fold
  inferred; entered in 6.1, Table 6.1e, the Summary and the reproduction row of Table 8.2, 10:24 to 10:25; re-read by
  the verification 10:34: CONFIRMED.
- 2026-10-21 10:13 to 11:05 Section 6.3: every real value of the finite part of 4.38 on the zero-moment
  configurations. Compact twists for every real parameter, with finite part a_tw eps^2 + O(1 + |eps|) and a_tw > 0
  (verification 10:24: CONFIRMED), and far-annulus conjugacies along which the finite part tends to -infinity
  (verification 10:38: CONFIRMED; its first numerical controls failed a quadrature tolerance at 10:32 and passed after
  refinement of the quadrature at 10:33); separate audits 10:31 to 10:38 (the twists) and 10:35 to 10:44 (the combined
  text): VALID; the combined text read against both proofs by the verification 10:47: CONFIRMED; entered at the end of
  the 6.3 bullet, in the Summary, the Scope of 4.38 and the Table 8.1 row of 4.34, 10:46 to 10:48; verification
  re-read 11:05: CONFIRMED.
- 2026-10-21 10:31 to 11:05 40-mode state of the fixed-beta run at beta = 3.0315 (computed 10:31; verification 10:39):
  REFUTED as an unforced profile (forced ratios 0.0024/0.0056 against 0.0096/0.018 with 32 modes, (B2-P) ratios
  0.74/0.45, exact positive-power thermal-tail witnesses, C2 in [-4541.890, -4541.889]); lambda differs from the
  32-mode value by 6e-8; a finite comparison at one beta, with different initial and stopping histories; entered in
  6.1, Table 6.1e, the C2 list, the Summary and the reproduction row of Table 8.2, 10:55 to 10:56; verification
  re-read 11:05: CONFIRMED (63 rows, the accepted continuation flag).
- 2026-10-21 10:41 to 11:11 Section 6.3, beta = 2: both equations near the center and along the open zero arc in a
  configuration that is not a profile. Verification 10:49 (17 exact and 22 flow controls): CONFIRMED; a compact
  Hamiltonian shear of a transport configuration gives (T) on R^2, the center data, the canonical inverse and (V) near
  the center and along the open arc, with flat endpoints, and the exterior residual shows that it is not a profile.
  Verification 11:01 to 11:05 (12 exact checks at 11:02): both endpoints are outgoing, (V) fails on a nonempty open
  invariant set of orbits issuing from each endpoint, and the arc identities of 4.7(iii) hold. Separate audit (asked
  10:52, answered 11:02): VALID WITH FIXES, the wording of the endpoint statements adopted. Verification of the draft
  11:05: CONFIRMED with one wording precision, adopted. Entered at the end of the 6.3 bullet, in the Summary and in
  the Table 8.1 row of 4.7(iii)-(iv), 11:06; entered text re-read by the verification 11:11: CONFIRMED.
- 2026-10-21 11:01 to 11:49 Targeted review of the text entered since 10:01 (separate referee, asked 11:01, answered
  11:15): no mathematical error found; adopted 11:18: the exact zero x-moment of the residual in 6.3 derived
  explicitly (continuity in the family parameter and the intermediate value theorem), the qualifications of 6.1
  restored in the Summary numerics sentence, two timeline ranges extended to their last re-read, local notation in the
  far-annulus construction, the wording of the 48-hour requirement in section 8; not adopted: the removal of the
  software versions from section 8 (the problem requires machine and software versions); adopted text re-read by the
  verification 11:49: CONFIRMED.
- 2026-10-21 11:02 to 11:51 40-mode state of the fixed-beta run at beta = 3.04 (computed 11:02; verification 11:09):
  REFUTED as an unforced profile (forced ratios 0.0063/0.015 against 0.020/0.037 with 32 modes, (B2-P) ratios
  0.73/0.45, exact positive-power thermal-tail witnesses, C2 in [-4681.595, -4681.594]); lambda differs from the
  32-mode value by 2e-8; a finite comparison at one beta, with different initial and stopping histories; entered in
  6.1, Table 6.1e, the C2 list, the Summary and the reproduction row of Table 8.2, 11:18; entered text re-read by the
  verification 11:49: CONFIRMED with one precision fix (the bound on the two lambda differences is 6.1e-8), adopted
  11:51.
- 2026-10-21 11:07 to 11:47 Second path, lambda = 0.98: the seven inner states of the failed stage recomputed and
  stored with beta fixed at 2.8323 to 3.4734 (stored 11:07 to 11:37). Verification 11:40 (exact rational center-strain
  certificates of the stored binary fields, separate integer checker, 66 manufactured controls): CONFIRMED that the
  center-strain mismatch is negative (-0.206 to -0.0289) with positive temperature amplitude at the center for all
  seven, so none meets the center-strain condition; no exclusion between the sampled beta and no fold inferred;
  entered in 6.1, the Summary and Table 8.2, 11:47.
- 2026-10-21 11:14 to 11:49 Section 6.3, beta = 2: the configuration of 6.3 deformed by a further compactly supported
  area-preserving map, flat relative to the identity at the endpoints, so that the strong unstable curves agree with
  no real analytic curve germ through the endpoints. Verification 11:23 (10 exact, 56 flow and 24 finite-difference
  Jacobian controls): CONFIRMED; all other properties of the configuration are kept, and (V) still fails on an open
  invariant set at each endpoint and at points of the new strong unstable curves. Separate audit (asked 11:27,
  answered 11:37): VALID WITH FIXES (the preserved properties are those of the constructed configuration; (V) fails to
  hold identically on the invariant set, not at each of its points); entered with these fixes 11:39; entered text
  re-read by the verification 11:49: CONFIRMED.
- 2026-10-21 11:29 to 12:14 4.7(xii), beta = 2 (U not real analytic on any neighbourhood of an endpoint; Theta not
  constant on any neighbourhood of an outgoing endpoint, equivalently on no subarc of the zero arc ending there), and
  the 6.3 configuration with Theta = L and Omega = 0 on open sets adjacent to the endpoints. Verification: the
  configuration CONFIRMED 11:47 (209 controls); an independent proof of (xii)(b), with a general proof of (xii)(a),
  CONFIRMED 11:56 (12 exact and 60 flow controls); entry drafts (written 11:55) CONFIRMED 11:58. Separate audit (asked
  11:55, answered 12:09): (a), (b), the equivalence and the construction VALID; the 6.3 paragraph and the relation to
  (iii)-(iv) VALID WITH FIXES (the exception that (V) is not asserted to fail on O removed, since (V) fails somewhere
  on each such set; notation); entered with these fixes 12:11 to 12:14.
- 2026-10-21 11:48 to 12:06 Tenth targeted referee review (changes since 11:01; answered 12:04): no incorrect formula;
  adopted 12:00 to 12:06: boundary-vanishing wording in 4.7 Scope of (iii)-(iv) and 6.3, "(V) does not hold
  identically on O", and the construction of the signed reference family and the continuity argument behind the zero
  x-moment configurations of 6.3 (from P147 and P148, both CONFIRMED); verification precision fix 11:58 (beta within
  5.1e-5 of the logged values) adopted 12:00.
- 2026-10-21 11:49 to 11:52 Method descriptions in section 6.1 (verification audit of the numerical checklist, 11:49):
  the number of finite-difference steps of each evaluation, the inverse of the wide-grid evaluations, and the 40-mode
  solve at lambda = 0.95 (started from the 32-mode state with a changed strain tolerance, so that its beta is the
  stored 32-mode value) corrected; the comparison of 24, 32 and 40 modes at lambda = 0.95 qualified by its different
  optimization histories and strain tolerances; adopted 11:51 to 11:52.
- 2026-10-21 12:06 to 12:52 Second path continued with beta prescribed (beta = 3.088 to 3.2, 24 modes). Verification
  12:06, 12:28 and 12:44 (exact rational center certificates of the eleven stored states, separate integer checks, 45
  manufactured controls): the normalized (B2-P) temperature residual tends at the center to approximately 0.614 to
  0.636 (re-read 13:00: CONFIRMED with this rounding repair, adopted 13:05), REFUTED as unforced profiles; forced
  center-strain mismatch between -6.2e-6 and 1.3e-5; full regional evaluations at beta = 3.105 (12:12) and 3.2
  (12:44): REFUTED as unforced profiles (forced ratios 3.1e-4/3.1e-4 and 6.2e-4/7.1e-4, (B2-P) ratios 0.74/0.42 and
  0.73/0.41, exact positive-power thermal-tail witnesses, C2 in [-517.428, -517.427] and [-1243.684, -1243.683]);
  inference from the samples audited 12:48: a sampled minimum of lambda only, no fold, no branch continuity and no
  exclusion of roots between the samples; entered in 6.1, Tables 6.1c and 6.1e, the Summary and Table 8.2, 12:52.
- 2026-10-21 12:08 to 12:12 Verification re-read of the 12:00 to 12:06 changes (12:08): CONFIRMED, with two repairs to
  the 6.3 summary of the signed reference family (the angular diffeomorphism is not compactly supported; g' is made
  small on the chosen interval and kept bounded below outside a slightly larger one); adopted 12:12.
- 2026-10-21 12:18 to 12:44 4.7(xii)(c), beta = 2 (no outgoing endpoint at which U is real analytic along the normal
  line and Omega along the nearby parallel lines beyond it). Verification: the polynomial case CONFIRMED 12:18; the
  general statement, with only the value trace analytic, CONFIRMED 12:35 (101 exact and 2 negative controls). Separate
  audit (asked 12:31, answered 12:36): VALID, the analytic normal derivative trace redundant; notation fixes; entered
  with the weaker hypothesis and the Schwarz reflection step 12:44.
- 2026-10-21 12:23 to 12:28 Verification re-read of the 12:11 to 12:14 entries (12:23): 4.7(xii), the boundary
  statements in 4.7 and 6.3, the 6.3 paragraph on the configuration with Theta = L and Omega = 0 on open sets adjacent
  to the endpoints, and the repaired summary of the zero-moment configurations: CONFIRMED; a clarification (the
  invariant set O at each endpoint can be chosen so that Omega is not identically zero on it) adopted 12:28.
- 2026-10-21 12:33 to 15:39 Second path with 84 radial intervals (24 angular modes) at beta = 3.0925, 3.085 and 3.105,
  from a refit of the 56-interval state at 3.0925: stored lambda equal to the 56-interval values to six digits.
  Verification 15:18 and 15:30 (exact rational center certificates and C2 enclosures): normalized (B2-P) temperature
  residual at the center 0.633 to 0.637, REFUTED as unforced profiles; C2 negative for every stored field but changed
  by 15.8 percent by the refit and 53.1 percent after re-solving at 3.0925, so for b_rep > 3 the C2 digits depend on
  the radial representation; entered in 6.1, Table 6.1c and Table 8.2 15:39.
- 2026-10-21 12:46 to 13:03 Targeted review of the text entered since 11:48 (separate referee, asked 12:46, answered
  13:00): 4.7(xii)(a) to (c) valid, including the Schwarz reflection step with continuity only; adopted 13:03: the
  heading of 4.7(xii) and both Scope paragraphs restricted to what the outgoing case gives (no exclusion of profiles
  without an outgoing endpoint), the continuation wording of the Scope of 4.7(iii)-(iv) and of 6.3 (no continuation
  across the boundary established, rather than none possible), the curl relation and the restricted obstructions in
  the sentence on the two local consultations, the sign wording of the signed family of 6.3, and the beta values of
  the seven recomputed states of 6.1 identified as the fixed values; the completion items at the end of the run.
- 2026-10-21 12:46 to 13:13 Whole-report review (separate referee, asked 12:46, answered 13:04): the verdict
  UNRESOLVED confirmed; no error in the proof outlines checked other than an incorrect example in the Scope of
  4.7(xii); adopted 13:13: that example replaced (the hypotheses of 4.7(xii)(c) are unchanged by the shear t = z -
  k(s)), the stream hypotheses of the converse 4.32(d) stated in the Summary, section 5 and 6.3, the further
  hypotheses of 4.7(x), (xi) noted in section 5, the fields of 4.35(b) marked as not shown to belong to profiles, the
  far-field determination restricted to the second and third terms (later terms involve the constant velocity of
  4.26(b), 4.27), the Scope of 4.13, the exact moment of 4.13(iv) in 4.13(iv) and Q2(e), the citation scope of Q2(g),
  beta > 0 and the decay exponent in section 1, the two homotopies at the start of 6.1, the largest sampled eps in
  place of a turning point, the bound 0.63 for the (B2-P) maxima of Table 6.1e, the coverage of the C2 enclosures in
  Table 8.2, and the orbit of 4.7(x) and 4.20 renamed C_* (O' for the invariant sets of the configurations of 6.3);
  not adopted: the removal of software names and versions from section 8 (the problem asks for them) and a shortening
  of the repeated summaries; the completion items at the end of the run.
- 2026-10-21 12:54 to 13:20 Second path at beta = 3.25 and 3.3. Verification 12:54 (exact rational center certificate,
  separate integer check): at beta = 3.25 (lambda = 0.998139) the normalized (B2-P) temperature residual tends at the
  center to 0.6056, REFUTED as an unforced profile; forced mismatch -7.19e-6; regional evaluation 13:04: forced ratios
  7.9e-4/1.5e-3, (B2-P) ratios 0.72/0.41, exact positive-power thermal-tail witnesses, C2 in [-1871.948, -1871.947];
  at beta = 3.3 no accepted state (requested lambda clipped to 1); the two saved intermediate evaluations are not
  exact forced center roots and not profiles (13:04); entered in 6.1, Tables 6.1c and 6.1e, the Summary and Table 8.2,
  13:20.
- 2026-10-21 12:59 to 13:27 The hypothesis of 4.7(xii)(c) on U(0, .) does not follow from its hypothesis on Omega and
  the local structure at an outgoing endpoint (the second configuration of the 6.3 bullet beta = 2, not a profile).
  Verification CONFIRMED 12:59; separate audit (asked 13:18, answered 13:26): VALID with fixes (the full value trace
  is not flat, only its tangential component and the remainder of its normal component; the orientation of the
  normal); entered in the Scope of 4.7(xii) and the 6.3 bullet beta = 2 13:27.
- 2026-10-21 13:20 to 13:32 Second path with 32 angular modes at beta = 3.0925 and 3.085. Verification 13:20 (exact
  rational center certificates, separate integer check; independent regional evaluation): own center strain 0.6426 and
  0.6388 against 2.54625 and 2.5425, normalized (B2-P) temperature residual at the center 0.635 and 0.637, REFUTED as
  unforced profiles; forced mismatch -4.0e-7 and -7.8e-7; forced ratios 2.7e-4/2.8e-4 and 2.5e-4/2.5e-4, (B2-P) ratios
  0.74/0.42, exact positive-power thermal-tail witnesses and C2 enclosures; the value of lambda at 3.0925 inherited
  from the 24-mode state; the stored fields (and the 24-mode field at 3.0925) not C^5 at the interior knots (exact);
  entered in 6.1, Tables 6.1c, 6.1e, the Summary and Table 8.2, 13:32.
- 2026-10-21 13:28 to 13:32 Re-reading of the adopted whole-report review: the revisions CONFIRMED; two further scope
  repairs adopted 13:32 (the third scalar far-field terms stated for every beta > 2 in Table 6.1c; the Scope of 4.26
  restricts the conditional form (d) to the conclusion on the constant velocity).
- 2026-10-21 13:33 to 13:57 Whole-report review (separate referee, asked 13:33, answered 13:55): the verdict
  UNRESOLVED and the class statement confirmed; the new endpoint passages and the 32-mode center values confirmed;
  adopted 13:57: the case gamma <= 0 of the weighted integral in the proof of 4.9(c), a stale parenthesis on
  refinement in 6.1, the clipped run at beta = 3.3 in Table 8.2, and four line breaks inside formulas; not adopted:
  the removal of software names and versions from section 8 (the problem asks for them).
- 2026-10-21 13:40 to 13:51 Second path with 32 angular modes at beta = 3.1 and 3.11, computed in the sequential
  continuation through 3.0925, 3.085, 3.1 and 3.11 (this history wording corrected 14:41 after a re-reading at 14:34).
  Verification 13:40 (exact rational center certificates, separate integer check): own center strain 0.6464 and 0.6512
  against 2.55 and 2.555, normalized (B2-P) temperature residual at the center 0.634 and 0.632, REFUTED as unforced
  profiles; forced mismatch -1.2e-8 and -2.3e-6; no regional evaluation; entered in 6.1, the Summary and Table 8.2
  13:51, with the vanishing conclusion C = 0 named in the Scope of 4.26 (re-reading 13:40).
- 2026-10-21 13:52 to 14:37 4.7(xiii), beta = 2 (Theta - L and Omega flat along the strong unstable curve of every
  endpoint; the leading term of that curve in terms of the curvature of the zero curve; the conclusion of 4.7(xii)(c)
  at every endpoint whose strong unstable curve meets s > 0 in every neighbourhood of it; the index of the arc and its
  consequences). Research consultation answered 13:52; separate audits (asked 13:58 and 14:03, answered 14:12 and
  14:11): VALID, with fixes to the proof of (b); audit of the text (asked 14:20, answered 14:33): VALID, with wording
  fixes, adopted; verification (two independent packets) CONFIRMED 14:27; entered 14:37.
- 2026-10-21 13:53 to 14:41 Second path with 24 angular modes continued downward from beta = 3.088 (outer tolerance
  5e-6): eight states at beta = 3.0865 to 3.06, lambda 0.990016 to 0.990808. Verification 13:53 and 14:31 (exact
  rational center certificates, separate integer check): normalized (B2-P) temperature residual at the center 0.6366
  to 0.6425, REFUTED as unforced profiles; forced mismatch nonzero, at most 8.0e-7; at 3.085 the 24-mode and 32-mode
  lambda differ by 3.3e-7 (one comparison, different histories); no regional evaluation; entered in 6.1, Table 6.1c,
  the Summary and Table 8.2 14:41.
- 2026-10-21 14:52 to 15:26 4.7(xiv), beta = 2 (incoming endpoints with isolated zeros of W off the arc: finitely many
  such zeros, singleton backward limits and a tree of bounded orbits; Theta = L and Omega = 0 on the side of the
  strong unstable curve beyond each endpoint; the analogues of 4.7(vi), (xii)(b) and (xii)(c) at the endpoints; with
  nondegenerate zeros, no axis zero other than the center). Research consultation (asked 14:25, answered 14:52); audit
  of the text (asked 14:57, answered 15:07): VALID, with fixes to the proofs of (a) and (b) and to the wording of the
  Scope, adopted; verification (two independent packets) CONFIRMED 15:12 and 15:24; entered 15:26.
- 2026-10-21 14:58 to 15:24 Second path with 24 angular modes, last four downward stages: beta = 3.05, 3.04, 3.02 and
  3.0, lambda 0.991438, 0.992313, 0.995066 and 0.999999 (inner residuals above tolerance at 3.02 and 3.0; at 2.95 the
  requested lambda was clipped to 1 and the run stopped without a stage result). Verification 14:58 and 15:18 (exact
  rational center certificates): normalized (B2-P) temperature residual at the center 0.6448 to 0.658, REFUTED as
  unforced profiles; forced mismatch nonzero, at most 3.1e-6; the 3.0 state close to the seed (coefficient differences
  at most 3.7e-5), not identical; no regional evaluation. Re-reading 14:59 of the entered 4.7(xiii), the eight earlier
  left states and the repaired 32-mode history wording: CONFIRMED. Entered in 6.1, the Summary and Table 8.2 15:24.
- 2026-10-21 15:21 to 15:46 4.7(xv), beta = 2 (at an outgoing endpoint, and at an incoming one with isolated zeros of
  W off the arc, neither Theta - L nor Omega vanishes identically on a neighbourhood of any point of the orbits of the
  strong unstable curve; when Z = gamma the open parts of the endpoint basins (without the endpoint and its strong
  unstable orbits) are components of the interior of {Omega = 0} and of the interior of {Theta = L}, with boundary in
  these orbits; wording of the open parts made precise 16:50 after a whole-report review). Derived from 4.7(xii),
  (xiii) and (xiv); audit of the text (asked 15:21, answered 15:32): VALID, with fixes to the proofs of (a), (b) and
  (c) and to the Scope, adopted; verification (independent packet) CONFIRMED 15:39; entered 15:46.
- 2026-10-21 15:28 to 16:02 Second path with tighter tolerances (56 radial intervals, 24 modes; inner 1e-5, mismatch
  2e-6) at beta = 3.0925 and 3.1: stored lambda changed by 0 and 3.4e-7. Verification 15:51 (exact rational center
  certificates and C2 enclosures): normalized (B2-P) temperature residual at the center 0.635 and 0.634, REFUTED as
  unforced profiles; at beta = 3.0925 both this run and the 84-interval run accepted the inherited lambda after four
  inner iterations (not a new determination); C2 changed by less than 1e-5 relative under the tighter tolerances and
  by 52.6 percent under the radial refinement at beta = 3.085; entered in 6.1 and Table 8.2 16:02.
- 2026-10-21 15:46 to 16:19 4.7(xvi), beta = 2 (for Z = gamma: for each endpoint the orbits of the strong unstable
  curve and the endpoint form a properly embedded line; the complement of the two mirror lines has exactly three
  components, the open parts of the two endpoint basins and a simply connected region containing the axis; Theta = L
  and Omega = 0 outside that region). Derived from 4.7(v) and (xv); audits of the text (asked 15:48 and 15:51,
  answered 15:59 and 16:00): VALID, with fixes to the proofs of (a), (b) and (d) and to the Scope, adopted;
  verification (independent packet) CONFIRMED 16:17, with a wording fix, adopted; entered 16:19; wording of the open
  parts made precise 16:50.
- 2026-10-21 15:49 to 16:00 Planar field example in the Scope of 4.7(xiv) (a smooth field with div W = 4, the parity,
  a flat incoming zero arc through the center and four sources and two saddles off it, in which the exterior center
  branch at each endpoint has a saddle as backward limit; not the W of a profile). From the research consultation of
  14:25 to 14:52; verification (independent construction, exact checks) CONFIRMED 15:49; entered 16:00.
- 2026-10-21 16:01 to 16:50 Second path, independent regional evaluation of the three 84-interval states and the two
  tighter-tolerance states (verification 16:13; 189 radii for the 84-interval states): sampled normalized (B2-P)
  maxima 0.7415 to 0.7449 and 0.4188 to 0.4200, forced maxima 1.6e-4 to 2.9e-4 and 1.6e-4 to 3.0e-4, exact
  positive-power thermal-tail witnesses (absolute temperature residuals unbounded), C2 enclosures as before; REFUTED
  as unforced profiles; finite-grid diagnostics, not a convergence result; entered in 6.1, Tables 6.1c, 6.1e and 8.2
  16:50.
- 2026-10-21 16:01 to 16:50 40-mode state of the fixed-beta run at beta = 3.05 (saved 16:01, continued from the
  40-mode state at 3.04; verification 16:38): REFUTED as an unforced profile (forced ratios 0.014/0.036 against
  0.040/0.067 with 32 modes, (B2-P) ratios 0.73/0.45, exact positive-power thermal-tail witnesses, C2 in [-4870.395,
  -4870.394]); lambda differs from the 32-mode value by -1.0e-7; a finite comparison at one beta, with different
  initial and stopping histories; entered in 6.1, Table 6.1e, the C2 list, the Summary and Table 8.2 16:50.
- 2026-10-21 16:20 to 16:50 Whole-report review (separate referee, asked 16:20, answered 16:39): the verdict
  UNRESOLVED and the class statement confirmed; no false theorem and no circularity found; adopted 16:50: the open
  parts O_+ and O_- of the endpoint basins distinguished from the full basins in the Summary, section 5, 6.3 and the
  entries of 4.7(xv) and (xvi) in this section; the change of C2 under the radial refinement at beta = 3.105 (54.1
  percent) added and the bound 53 percent of Table 6.1c corrected; the regional evaluation of the 84-interval and
  tighter-tolerance states entered; the endpoint sentences of the Summary and 6.3 split, with the notation defined in
  the Summary; two source-format repairs; the registry and the archives to be rebuilt after the final content freeze;
  not adopted: moving the software versions of section 8 to a separate record (the problem asks for them).
- 2026-10-21 16:32 to 17:03 40-mode state of the fixed-beta run at beta = 3.062 (saved 16:32, continued from the
  40-mode state at 3.05; verification 16:59): REFUTED as an unforced profile (forced ratios 0.029/0.077 against
  0.068/0.11 with 32 modes, (B2-P) ratios 0.73/0.58 against 0.73/0.74, positive exact center mismatch, exact
  positive-power thermal-tail witnesses, C2 in [-5096.426, -5096.425] against [-4979.108, -4979.107]); lambda differs
  from the 32-mode value by 2.4e-8 and C2 by 2.4 percent; a finite comparison at one beta, with different initial and
  stopping histories; entered in 6.1, Tables 6.1c and 6.1e, the C2 list, the Summary and Table 8.2 17:03.
- 2026-10-21 16:37 to 17:00 4.7(xvii), beta = 2 (near each endpoint of the zero arc the vorticity and the velocity of
  a profile are in no quasianalytic Denjoy-Carleman class, and the temperature is in none on a connected open set
  containing the arc; likewise near the orbits of the strong unstable curves under the hypotheses of 4.7(xv)). Derived
  from 4.7(ii), (iii), (xii)(a), (xiii)(a), (xv) and the Denjoy-Carleman theorem; audit of the text (asked 16:37,
  answered 16:50): VALID, with fixes to the proof outline and the Scope, adopted; verification (independent packet)
  CONFIRMED 16:57, requiring the same summation step in the Scope example as the audit; entered 17:00.
- 2026-10-21 16:56 to 17:59 4.7(xviii), beta = 2 (exact local reduction at an outgoing endpoint: a normal form X(a, r)
  of the flow on the closed side of the strong unstable curve that contains the arc, with W o X = 4 r X_r, unit
  Jacobian and Theta o X = theta(a), in which the equations reduce to one curl equation; a one-sided Cauchy problem,
  with the full gradient trace, for a potential of W on the basin side; smooth gluing when theta - L is flat at the
  endpoint; the formal normal expansion along the arc is unobstructed). From a research consultation (asked 16:56,
  answered 17:11), with its proofs rederived; audit of the text (asked 17:22, answered 17:34): VALID, with
  justifications in the proof and a repair of the Scope, adopted; independent verification (17:55): CONFIRMED as a
  conditional local equivalence, with two repairs of the Scope, adopted; entered 17:59; re-reading of the entered text
  (18:02): CONFIRMED, with a repair of the label of the basin problem in the Summary, section 5 and this entry,
  applied 18:06.
- 2026-10-21 17:03 to 17:19 4.7(xvii)(d), beta = 2 (under the hypotheses of 4.7(xvii)(c), for each family of parallel
  lines transverse to an arc of the orbits of the strong unstable curve: outside one meager set of lines the
  restrictions of Theta - L and Omega are flat nonzero germs, hence in no quasianalytic Denjoy-Carleman class, and for
  each class C{m}, outside a meager set of lines that may depend on m, the restriction of U is not in C{m};
  quantifiers restated 17:56 after a whole-report review). Derived from 4.7(xv) and (xvii), the proof first in an
  independent verification packet; verification (independent packet) CONFIRMED 17:09; audit of the text (asked 17:08,
  answered 17:18): VALID, with wording fixes, adopted; entered 17:19.
- 2026-10-21 17:10 to 17:46 40-mode state of the fixed-beta run at beta = 3.076 (saved 17:10, continued from the
  40-mode state at 3.062; verification 17:42): REFUTED as an unforced profile (forced ratios 0.056/0.12, (B2-P) ratios
  0.73/0.95, positive exact center mismatch, exact positive-power thermal-tail witnesses, C2 in [-5289.577,
  -5289.576]); lambda 0.931657, 2.7e-5 below the 40-mode value at 3.062; no 32-mode state at this beta; entered in
  6.1, Tables 6.1c and 6.1e, the C2 list, the Summary and Table 8.2 17:46.
- 2026-10-21 17:20 to 18:08 Whole-plane L2 distances (P187) of the stored 32- and 40-mode states at beta = 3.0315,
  3.04, 3.05 and 3.062, for G and its angular derivative (verification 17:58: exact rational enclosures for the fields
  defined by the stored coefficients with exact powers and unclipped splines); entered in 6.1 and Table 8.2 18:08;
  re-reading of the entered text (18:12): CONFIRMED.
- 2026-10-21 17:21 to 17:30 Common-grid comparison (E542) of the stored 32- and 40-mode states at beta = 3.0315, 3.04,
  3.05 and 3.062 (verification 17:21 to 17:26): angular maximum of the difference over angular maximum of the 40-mode
  field, largest over the radii: discrepancies of G = Omega/x 0.010 to 0.034 and of its angular derivative 0.068 to
  0.16, at the largest sampled radius; CONFIRMED as finite sampled distances of forced fields, not a refinement limit;
  entered in 6.1, Table 6.1c and the Summary 17:30.
- 2026-10-21 17:31 to 17:56 Whole-report review of the completion preview (tenth): no mathematical error found;
  adopted: the endpoint hypotheses and the quantifiers of 4.7(xvii)(c), (d) in section 5, the Summary and the
  timeline, the boundary description in the Scope of (iii)-(iv), the definitions of the common-grid distances and of
  the C2 percentages, a table-cell repair, and paragraph and sentence splits in the Summary; the rebuild of the
  registry and the archives after the final content freeze, with the session count recomputed, is part of the
  completion steps; not adopted: moving the software versions out of section 8 (the documentation of machine and
  software versions is required); entered 17:56.
- 2026-10-21 17:49 to 18:00 40-mode state of the fixed-beta run at beta = 3.092 (saved 17:49, continued from the
  40-mode state at 3.076; verification 17:55): REFUTED as an unforced profile (forced ratios 0.088/0.15, (B2-P) ratios
  0.72/0.97, nonzero exact center mismatch, exact positive-power thermal-tail witnesses, C2 in [-5279.508,
  -5279.507]); lambda 0.932671, 1.0e-3 above the 40-mode value at 3.076; no 32-mode state at this beta; entered in
  6.1, Tables 6.1c and 6.1e, the C2 list, the Summary and Table 8.2 18:00; re-reading of the entered text (18:08):
  CONFIRMED.
- 2026-10-21 18:00 to 2026-10-22 03:12 Sampled stagnation search of six stored fields and next-order far-field
  coefficients of six stored forced states (computation from 18:00; referee corrections of the far-field computation
  adopted 18:56): verification on a separate grid (P194): sampled positivity CONFIRMED 18:59, the inference from
  samples to the absence of zeros between them REFUTED by a manufactured field; verification of the far-field
  coefficients (P196): CONFIRMED 19:05, the implication that the missing mixed powers force the observed differences
  REFUTED; verification of the entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-21 18:11 to 22:05 Finite-difference Jacobian of the inner fixed-point map at the state of the second path at
  (beta, lambda) = (3.0952, 0.989973) (computation 18:11 to 21:22): smallest singular value of J_T - I, spectral
  radius of J_T and finite-difference linear-response estimates of the derivatives of the center-strain mismatch;
  matrix audit of the frozen array 21:23 to 21:32 (P208): CONFIRMED as linearized diagnostics (own full-plane weighted
  metric; no contraction, fixed-point, branch or error statement); entered 22:05.
- 2026-10-21 18:16 to 18:42 4.14(j), addition: the earlier half-plane neural-network profile of arXiv:2201.06780v3
  (inferred lambda = 1.917 +- 0.002, beta = 2.917 +- 0.002; residues stated to be about five orders of magnitude below
  the solution); verification against the primary text 18:32 to 18:40: CONFIRMED; whole-report review 18:20 to 18:36:
  claims supported, two-sentence wording proposed and adopted; entered 18:42.
- 2026-10-21 18:20 to 18:38 Whole-report review of the completion preview (eleventh): no mathematical error found in
  4.7(xvii) and (xviii) (normal form, unit Jacobian, transport formulas, curl equation, full gradient trace on the
  basin side rederived) and no numerical inconsistency in the 40-mode and L2 distance sentences; adopted: an
  antecedent repair and sentence and paragraph splits in the Summary, a sentence split of the beta = 2 list in section
  5, and the scope of the rounding in the caption of Table 6.1e; the rebuild of the registry and the archives after
  the final content freeze is part of the completion steps; not adopted: moving the software versions out of section 8
  (the documentation of machine and software versions is required); entered 18:38.
- 2026-10-21 18:33 to 2026-10-22 03:12 Three map scales (L = 1, 1.5 and 2.5) for the two states of the Jacobian
  diagnostics, re-solved at fixed (beta, lambda) (computation 18:33 to 21:26): independent evaluation 22:26 to 22:43
  (P217): CONFIRMED as finite diagnostics of forced states, every field REFUTED as a profile; verification of the
  entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-21 18:39 to 18:59 Section 6.3, beta = 2: exact solutions of the local equations from the fourth
  outgoing-endpoint consultation (a zero graph in no Gevrey class with the center jet of a profile; a vertical zero
  line with a temperature trace in no Gevrey class; neither family has sublinear velocity): separate audit 18:40 to
  18:44: VALID WITH FIXES (the center-jet example, the scope of the conclusion), all adopted; verification 18:48 to
  18:58: CONFIRMED; entered 18:59.
- 2026-10-21 18:47 to 19:27 4.7(xii)(d), beta = 2 (no outgoing endpoint at which W is, on the side of the strong
  unstable curve beyond it, a finite sum of products of functions of s and of z), with the related Scope and summary
  sentences, and Section 6.3, beta = 2 (the type of the equations of 4.7(xviii)(a) with a as evolution variable):
  research consultation 18:47 to 19:03; separate audit 19:10 to 19:16: VALID WITH FIXES (representation domain, trace
  of the auxiliary field, symbol determinant and r = 0, regularity in the summaries), all adopted; verification 19:14
  to 19:24: CONFIRMED; entered 19:27.
- 2026-10-21 19:23 to 20:09 4.7(xix), beta = 2 (no real analytic field agreeing with W on the basin side of an
  outgoing endpoint near it; no Gevrey bounds of order 2 in one fixed direction for the velocity on the basin side,
  uniformly up to the endpoint, or for the vorticity on a whole neighbourhood of the endpoint; the support of the
  vorticity at a nonvertical outgoing endpoint), with the related summary, Scope and 6.3 sentences: research
  consultation 19:23 to 19:36; separate audit 19:51 to 19:58: VALID WITH FIXES (the Scope sentence on bounds on parts
  of O; the wording of the summary, 6.3 and Scope sentences), adopted; verification 19:51 to 20:04: CONFIRMED; entered
  20:09.
- 2026-10-21 20:02 to 20:35 4.7(xix)(e), beta = 2 (the statements (a) to (c) of 4.7(xix) at incoming endpoints when
  the zeros of W off gamma are isolated), with the related heading, Scope, summary and 6.3 sentences: derived from the
  proofs of 4.7(xix) and 4.7(xiv)(b); separate audit 20:03 to 20:09: VALID WITH FIXES (deletion of the Scope clause on
  profiles without an outgoing endpoint), adopted; verification 20:09 to 20:29: CONFIRMED; entered 20:35.
- 2026-10-21 20:13 to 20:56 4.7(xx), beta = 2 (accumulating endpoints: no neighbourhood on which Theta is constant,
  and, without arcs of zeros of W off gamma near the endpoint, the structure beyond the strong unstable curve and the
  analogues of 4.7(vi), (xii)(b), (xii)(c) and (xix)(a) to (c)), with the related Scope, summary and 6.3 sentences:
  research consultation 20:13 to 20:27; a second proof outline, by a barrier argument; separate audit 20:42 to 20:49:
  VALID; verification 20:42 to 20:55: CONFIRMED; entered 20:56.
- 2026-10-21 20:57 to 21:17 4.7(xxi), beta = 2 (open sets on which Theta is constant: their invariant hull, on which
  Omega = 0; no endpoint of any type with Theta constant on a neighbourhood of it), with the related Scope, summary
  and 6.3 sentences: direct derivation, not from a research consultation; separate audit 20:58 to 21:03: VALID WITH
  FIXES (the conclusion is also a corollary of 4.7(vii); the wording on local solutions; the related Scope sentences),
  adopted; second audit 21:05 to 21:09: VALID (the Q1 sentence on the scattering identities corrected), adopted;
  verification 20:59 to 21:14: CONFIRMED; entered 21:17.
- 2026-10-21 21:01 to 21:35 Whole-report review of the changes since the eleventh (twelfth, targeted): UNRESOLVED
  confirmed; no mathematical error found in 4.7(xii)(d), (xix) and (xx) (the barrier, the alpha-limit step, the
  constancy of Theta on the invariant line, the Gevrey-2 argument and the transfers rederived); adopted: the
  description of 4.7(xix) in this section, the harmonic extension through the endpoint in the Scopes of (iii)-(iv) and
  (xiv), the measure condition in the Scope of (xix), the quantifiers in the proof of (xx)(c), sentence splits in the
  Summary and the removal of two Summary clauses now covered by 4.7(xxi), and line-break repairs; not adopted: the
  temperature list of the Scope of (iii)-(iv) (superseded by 4.7(xxi)); verification 21:23 to 21:32: CONFIRMED;
  entered 21:35.
- 2026-10-21 21:26 to 22:49 Equal-count comparison of the forced problem at lambda = 0.95 with 24, 32 and 40 angular
  modes (same seed, prescribed beta, 20 map evaluations each; runs 21:26 to 21:48): verification of the histories and
  seeds and of the final states on the independent evaluator, with exact center and tail checks, 22:09 to 22:20:
  CONFIRMED as a finite comparison (the stored fields are not profiles; no attainable-residual bound); entered 22:49.
- 2026-10-21 21:30 to 22:18 4.7(xxii), beta = 2 (no nondegenerate straight segment of zeros of W on which Theta is
  constant; at an endpoint at which Theta is constant on a subarc of gamma ending there, Theta = L and Omega = 0 on
  the side of the strong unstable curve that meets gamma, and the restrictions at incoming and accumulating
  endpoints), with the related Scope, summary and 6.3 sentences: research consultation 21:30 to 21:43; separate audit
  21:53 to 22:10: VALID; verification 21:54 to 22:14: CONFIRMED; entered 22:18.
- 2026-10-21 21:48 to 2026-10-22 03:12 Finite-difference Jacobian at the 24-mode state of the first path at lambda =
  0.96 (computation 21:48 to 2026-10-22 01:09): audit of the frozen matrix 01:06 to 01:07 (P234): CONFIRMED as
  linearized diagnostics (own full-plane weighted metric); scope repairs of the account 01:16 to 01:36 (P241, P244):
  CONFIRMED after repair, the causal explanation of the convergence of the run REFUTED; verification of the entry text
  02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-21 22:19 to 23:08 Whole-report review of the completion preview (thirteenth): UNRESOLVED confirmed; no
  mathematical error or circularity found in 4.7(xxi) and (xxii); adopted: the qualification of the smallest stored
  lambda in the Summary and 6.1, the identifier of the Jacobian diagnostic and the name of its derivative estimates,
  the split of the Summary sentence on 4.7(xxii) with its qualifiers, blank lines ending two unintended lists, and
  line-break repairs; the refresh of the session count and active duration is part of the finalization; verification
  22:49 to 23:00: CONFIRMED; entered 23:08.
- 2026-10-21 22:30 to 23:32 4.7(xxiii), beta = 2 (no temperature H(x/rho(y)), rho > 0 of class C^2 on R, with H'
  nonzero at arbitrarily large arguments, or with H nonconstant and rho bounded above on a half-line): proof of (a) by
  the verification, written 22:30, symbolic controls 22:36: CONFIRMED 22:39; referee audit (asked 22:54, answered
  23:03): (a) VALID, two Scope sentences to be fixed, and a derivation of (b) and of the plateau example of the Scope,
  adopted 23:05; review of the revised text (asked 23:05, answered 23:12): VALID WITH FIXES (one step of the proof of
  (b), one Scope sentence), adopted; verification of (b), of the Scope and of the entry text 23:02 to 23:31:
  CONFIRMED; entered 23:32.
- 2026-10-21 23:17 to 2026-10-22 00:01 4.7(xxiv), beta = 2 (no temperature H(x/rho(y)) near the axis, any rho > 0 and
  H, under (V)): derivation by the analysis 23:17 to 23:32; referee audit (asked 23:33, answered 23:41): VALID WITH
  FIXES (the rescaling of Step 0), adopted 23:42; review of the entry text (asked 23:45, answered 23:54): VALID WITH
  FIXES (wording of the two scope passages), adopted; verification 23:40 to 23:59: CONFIRMED; entered 00:01.
- 2026-10-21 23:31 to 2026-10-22 00:25 4.39 (no temperature polynomial in x of bounded degree, any beta; for beta > 2
  no temperature H(x/rho(y)) on R^2, rho > 0): proof of (b) by the verification, written 23:31, symbolic controls
  23:33: CONFIRMED 23:35; proof of (a) by the verification, written 23:44, symbolic controls 23:45, CONFIRMED 23:47;
  referee audit of both proofs (asked 23:59, answered 00:05): VALID; verification of the entry text 00:17 to 00:23:
  CONFIRMED; entered 00:25.
- 2026-10-21 23:56 to 2026-10-22 00:34 4.40, beta > 2 (no temperature H(x/rho(y)) on a neighbourhood of the whole
  axis, any rho > 0 and H, for class A): proof by the verification, written 23:56, 53 exact controls 23:57; controls
  of the rescaling and of the dependencies 00:03; CONFIRMED 00:04; referee audit (asked 00:08, answered 00:16): VALID;
  symbolic checks in the analysis 00:14; verification of the entry text 00:24 to 00:33: CONFIRMED; entered 00:34.
- 2026-10-22 00:05 to 03:12 Sign-changing two-lobe external sources at eps = 0 (computation 00:05 to 00:40):
  verification 00:43 to 01:02 (P236): the bracket of the strain match for the weakly signed family CONFIRMED
  numerically, c_out = 0 for the antisymmetric pair CONFIRMED under its hypotheses, the negative transported G not
  reproduced for the literal sources; exact certificate of two further zeros of W_2(0, .) for the incomplete case
  (P238): CONFIRMED 01:01; exact rank of the temperature fit (P239): CONFIRMED 01:12; negative values reproduced
  through the fitted temperature and positive values by direct transport (P240, P247): CONFIRMED 01:46 and 01:58;
  verification of the entry text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-22 00:09 to 00:44 4.41 (finitely many axis derivatives of Theta, Theta_xx(0, .) without zeros: for beta > 2,
  under finitely many axis bounds on W_2, the even axis derivatives of orders 4 to M do not all vanish, and for class
  A the ratios I_2 to I_{N+2} are not all constant; at beta = 2, I_2 and I_3 are not both constant): proof of (a) by
  the verification, written 00:09, 81 exact controls 00:10, CONFIRMED 00:13; proof of (b) by the verification, written
  00:14, 32 exact controls 00:15 to 00:16, CONFIRMED 00:18; referee audits of (a) (asked 00:17, answered 00:25):
  VALID, and of (b) (asked 00:20, answered 00:29): VALID; checks of the thresholds in the analysis 00:22; verification
  of the entry text 00:35 to 00:37: CONFIRMED; entered 00:44.
- 2026-10-22 00:38 to 01:40 4.42 (the component J of {Theta_xx(0, .) != 0} containing 0: its ends are the zeros of
  W_2(0, .) nearest to 0; at beta = 2, I_2 and I_3 are not both constant on J; for beta > 2 and J unbounded, the
  statements of 4.41(a) on J, with the bounds at one infinite end): derivation in the analysis with symbolic checks,
  00:38 to 00:39; referee audit (asked 00:39, answered 00:47): VALID; proof by the verification, written 00:50, 52
  exact controls 00:51, CONFIRMED 00:54; verification of the entry text 01:26 to 01:31: CONFIRMED; entered 01:40.
- 2026-10-22 00:45 to 02:09 4.43 (beta > 2: I_2 and I_3 are not both constant on the axis component J, without
  additional derivative bounds at infinity or class A): derivation in the analysis with exact computer algebra, 00:45
  to 01:19; referee audit (asked 01:19, answered 01:37): VALID; proof by the verification, 01:19 to 01:52 (101 exact
  controls; exact certificate of 563 checks 01:48 to 01:49), CONFIRMED 01:52; verification of the entry text 01:43 to
  02:00: CONFIRMED; entered 02:09.
- 2026-10-22 01:09 to 03:12 40-mode states of the second path at beta = 3.0925, 3.085, 3.1, 3.11 and 3.076
  (computation 01:09 to 02:08): independent regional, exact center and tail evaluations 01:57 to 02:13 (P248) and
  02:19 to 02:25 (P251): CONFIRMED as finite diagnostics, every field REFUTED as a profile; verification of the entry
  text 02:42 to 03:03 (P256): CONFIRMED; entered 03:12.
- 2026-10-22 01:52 to 05:15 Diagnostics of the 40-mode state of the second path at beta = 3.085: curl and divergence
  defects of the inverse, sampled transport geometry and next-order endpoint coefficients (computation 01:52 to
  01:53): independent checks 02:28 to 02:34 (P253): CONFIRMED as finite diagnostics, no error bound for the inverse
  and no exclusion of unsampled stagnation points; verification of the entry text 05:07 to 05:13 (P279, 309 controls):
  CONFIRMED after the three exact wording corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 01:54 to 02:27 Referee consistency review of 4.39 to 4.43 with the Summary, the Q1 bullet and Table 8.1
  (asked 01:54, answered 02:07): no error in the statements or proofs; adopted: integrality and parity conditions in
  the Summary, the sublinearity of W - beta X in the Scope of 4.39, the hypotheses of the first paragraph in 4.42 and
  4.43, the Taylor coefficients and the chart 1 and t = 0 polynomials in 4.43 (3) and (4), the reflection symbol S_y
  in 4.7(xxiv), completed letter lists of 4.7(xxiv) and 4.40 to 4.43, and a shorter Summary sentence and Q1 bullet;
  verification of the corrections P250 (02:14 to 02:18): CONFIRMED; entered 02:27.
- 2026-10-22 02:10 to 05:15 48-mode states of the second path at beta = 3.085 (an evaluation at the inherited lambda)
  and 3.1 (computation 02:10 to 02:27): independent regional, exact center and tail evaluations 02:33 to 02:40 (P254):
  CONFIRMED as finite diagnostics, both fields REFUTED as profiles; the acceptance flags of the fifteen earlier
  fixed-beta states of the second path in Table 6.1e marked y* (the fit-growth multiplier was set to 1e9 in their
  runs); verification of the entry text 05:07 to 05:13 (P279, 309 controls): CONFIRMED after the three exact wording
  corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 02:30 to 05:15 48-mode states of the first path at beta = 3.076 (the inherited lambda, with the fields
  reoptimized) and 3.092 (computation 02:30 to 03:30): independent regional, exact center and tail evaluations 03:17
  to 03:23 (P262) and 03:46 to 03:52 (P267): CONFIRMED as finite diagnostics, both fields REFUTED as profiles; the
  sampled rise of lambda from 3.076 to 3.092 reproduced to within 1e-6, a finite comparison, not a fold statement;
  verification of the entry text 05:07 to 05:13 (P279, 309 controls): CONFIRMED after the three exact wording
  corrections on the fit-growth multiplier; entered 05:15.
- 2026-10-22 02:40 to 03:12 4.44 (beta > 2: I_2 has no nonzero finite limit at an infinite end of the axis component
  J, without derivative bounds at infinity or class A): derivation in the analysis with exact symbolic checks, 02:40
  to 02:42; referee audit (asked 02:42, answered 02:50): VALID WITH FIXES, fixes adopted; proof by the verification,
  02:48 to 02:51 (42 exact controls), CONFIRMED 02:51; verification of the entry text 03:04 to 03:10: CONFIRMED;
  entered 03:12.
- 2026-10-22 02:53 to 03:51 4.45 (for every beta >= 2 and s > -1 + 2/beta, |I_2| is not bounded below by a positive
  multiple of |y|^s near an infinite end of the axis component J; for beta > 2 every finite or infinite limit of I_2
  there is 0): proof by the verification of (a) and of the monotone case of (b), 02:53 to 02:58 (59 exact controls),
  CONFIRMED 02:58; derivation in the analysis for the positive sign of a0 I_2 with exact symbolic checks, 02:58 to
  03:05; referee audit (asked 03:04, answered 03:17): VALID WITH FIXES, the fix being the referee's proof for the
  negative sign, adopted; proofs by the verification for the positive sign, 03:11 to 03:14 (61 exact controls),
  CONFIRMED 03:14, and for both signs, 03:24 to 03:28 (50 exact controls), CONFIRMED 03:28; re-derivation in the
  analysis for the negative sign with exact symbolic checks, 03:27 to 03:28; verification of the entry text 03:36 to
  03:49 (one repair, the range beta >= 2 stated in the opening, adopted): CONFIRMED; entered 03:51.
- 2026-10-22 03:27 to 04:01 4.46 (the exponent -1 + 2/beta of 4.45 is optimal for the axis relations used there, for
  either sign of a0 I_2, and at beta = 2 every finite limit of I_2 is compatible with them; an example of axis data,
  not a profile): construction by the verification for L < 0 and for beta = 2, 03:27 to 03:38 (48 + 22 exact
  controls), CONFIRMED 03:38; exact symbolic checks in the analysis of the construction, 03:35 to 03:39, and
  derivation of the concave variant with exact symbolic checks, 03:39 to 03:41; referee audits of the construction
  (asked 03:38, answered 03:47) and of the variant (asked 03:40, answered 03:48): VALID; verification of the variant
  03:48 to 03:55 (57 exact controls): CONFIRMED; verification of the entry text 03:56 to 03:58 (203 controls):
  CONFIRMED; entered 04:01.
- 2026-10-22 03:34 to 05:51 48-mode states of a second 48-mode run of the first path, started from the 48-mode state
  at beta = 3.092, at beta = 3.076 and 3.062 (computation 03:34 to 04:51): independent regional, exact center and tail
  evaluations 04:48 to 04:54 (P277) and 04:59 to 05:05 (P280): CONFIRMED as finite diagnostics, both fields REFUTED as
  profiles; lambda solved at 3.076, 5.7e-7 above the 40-mode value, and the stored 48-mode values of lambda smallest
  at 3.076, a finite comparison, not a fold statement; verification of the entry text 05:44 to 05:45 (P284, 206
  controls): CONFIRMED; entered 05:51.
- 2026-10-22 03:50 to 04:36 4.47 (logarithmically enhanced critical tails I_2 = L y^{-m} (log y)^ell for the axis
  relations of 4.46: L < 0 for every beta >= 2 and either sign for beta > 2, examples of axis data, not profiles; at
  beta = 2, A I_2 does not tend to +infinity at an infinite end of the axis component): P266, P270 and P271
  independently proved and checked; A157 VALID (27 checks), A158 VALID WITH FIXES (37 checks), A159 VALID (24 checks);
  entry verified P274 CONFIRMED, 236 controls, 2026-10-22 04:29 to 04:31; entered 04:36.
- 2026-10-22 04:12 to 04:53 4.48 (critical limits of the axis ratios at an infinite end of the axis component: I_2 = L
  |y|^{-m} + O(|y|^{-m - eps}) under bounds on W_2(0, y) - beta y and its second derivative; for class A profiles,
  hence for every profile at beta = 2, |y|^{(n - 1) m} I_n has a finite limit for every n; for axis data the bound on
  the second derivative cannot be omitted): P272 (79 exact controls) and P275 (91 exact controls), CONFIRMED; A160,
  VALID WITH FIXES, and A158, VALID WITH FIXES (37 exact checks), with their repairs adopted; independent verification
  of the complete entry 04:44 to 04:47: P276, 273 controls, CONFIRMED after the exact p_n notation correction; entered
  04:53.
- 2026-10-22 04:31 to 05:37 4.49 (a bounded axis component is consistent with all axis equations: smooth fields of
  compact support with the canonical inverse, not profiles, satisfy (T) and (V) to every order on the axis, at every
  beta >= 2, with J = (-3, 3) and A I_2 -> -infinity at both ends of J): independent proofs of the bounded axis data
  and endpoint limits (P273, 65 exact controls) and of the smooth fields with all axis jets (P278, 93 exact controls,
  15 scope controls and 25 + 16 supplementary controls): CONFIRMED; referee audits A161 (VALID WITH FIXES, 36 exact
  checks) and A162 (correct, with editorial fixes), with their fixes adopted; independent verification of the complete
  entry text 05:32 to 05:35 (P282, 223 controls): CONFIRMED with two exact wording corrections; entered 05:37.
- 2026-10-22 05:23 to 06:21 4.50 (exact temperature transport is consistent with a bounded axis component: smooth
  fields, not profiles, with Psi and Omega of compact support and the canonical inverse, satisfy (T) on R^2 and (V) to
  every order on the axis, at every beta >= 2, with J = (-3, 3) and A I_2 -> -infinity at both ends of J): independent
  proof of the fields (P283, 55 controls, of which 45 exact or literal and 10 numerical quadratures of the correction
  without error bounds, and 15 supplementary exact controls): CONFIRMED; referee review A162, which proposed the
  correction along the flow, and referee audit A164 (valid with clarifications, adopted); independent verification of
  the complete entry text 06:02 to 06:04 (P290, 165 controls): CONFIRMED; entered 06:21.
- 2026-10-22 05:23 to 06:59 restarts of six stored stages of the two paths with 48 Gauss points per radial quadrature
  cell of the computation's inverse (computation 05:23 to 05:44) and the runtime velocity norms reported by the
  computation (05:45): independent regional, exact center, tail and inverse-constant evaluations 05:53 to 06:15
  (P287): CONFIRMED as finite diagnostics, all six fields REFUTED as profiles, every inherited lambda accepted and
  none redetermined; independent full-plane relative velocity norms at the same angles 06:11 to 06:17 (P291):
  CONFIRMED as a finite comparison, a conditional diagnostic and not an error bound, the runtime difference arrays not
  reproduced; verification of the entry text 06:41 to 06:56 (P298): CONFIRMED, 468 controls; entered 06:59.
- 2026-10-22 05:50 to 07:50 redeterminations of lambda for the 32-mode stage of the first path at beta = 3.062 with 12
  and 48 Gauss points per radial quadrature cell of the computation's inverse (computation 05:50 to 06:21):
  independent regional evaluations 06:26 to 06:31, with exact center and tail checks and summary by 06:37 (P294, 141
  controls): CONFIRMED as finite diagnostics, both fields REFUTED as profiles, the two values of lambda 1.76e-8 apart,
  without establishing existence of exact discrete roots at both orders or a difference between them; verification of
  the entry text 07:26 to 07:38 (P305): CONFIRMED, 342 controls; six wording corrections; entered 07:50.
- 2026-10-22 05:52 to 06:31 4.51 (finite ends of the axis component at which the axis velocity vanishes to a finite
  order p >= 2: the axis flow moves toward the end, T, Omega_x(0, .) and d_x^4 Theta(0, .) are flat there, D/T = -(3
  d0/beta) p (p - 1) s^{-2} (1 + o(1)) and A I_2 -> -infinity; necessary conditions, realized by local solutions of
  the four axis relations): independent proof (P286, 114 exact controls): CONFIRMED; referee audit A166 (VALID, 53
  exact checks, precision in step (3) adopted); independent verification of the complete entry text 06:20 to 06:27
  (P292, 152 controls): CONFIRMED with scope repairs; entered 06:31.
- 2026-10-22 06:01 to 06:31 4.52 (ends of the axis component at which the axis velocity vanishes to infinite order:
  local solutions of the four axis relations with b = sgn(y_*) exp(-1/s) (2 + sin(s^{-2})), flat at the end, for which
  A I_2 has subsequences tending to +infinity and to -infinity, and with b = sgn(y_*) exp(-1/s), for which A I_2 ->
  -infinity; so 4.51 (b) does not extend to such ends on the strength of these relations): independent proof (P289, 51
  exact controls): CONFIRMED; referee audit A165 (VALID, 37 exact checks); independent verification of the complete
  entry text 06:23 to 06:28 (P293, 158 controls): CONFIRMED with the local scope correction; entered 06:31.
- 2026-10-22 06:40 to 07:33 Whole-report review of the completion preview (fourteenth, A168): UNRESOLVED confirmed; no
  mathematical error found in 4.7(xxiii), (xxiv) and 4.39 to 4.52; adopted: the finite ends of the axis component
  (4.51 to 4.53) in the Q1 bullet on restricted temperature representations, the wording of the Scope of 4.50 on 4.49,
  the word "earlier" in the entry on the 48-mode states of the second path (fifteen flags were changed there; the two
  new states were stored with y*), and a split of the Summary bullet on temperature and the axis; not adopted: the
  replacement of the software versions in section 8 (they are part of the required documentation) and the joining of
  short source lines before displayed formulas; the controlling run instructions cap the wall-clock run at 48 h;
  finalization records the real elapsed time and the gaps between sessions separately, without counting gaps as active
  research; verification of the changes 07:22 to 07:30 (P307): CONFIRMED, 81 controls; one duration correction;
  entered 07:33.
- 2026-10-22 06:43 to 07:27 4.53 (ends of the axis component at which the axis velocity has a simple zero: I_2 has a
  limit in [-infinity, infinity]; if b''(y_*) != 0, D/T is asymptotic to -6 n sgn(y_*) b''(y_*) (4 beta + 3
  kappa)^{-1} s^{-1}; local polynomial and real analytic solutions of the four axis relations with every finite limit
  of I_2 and both infinite limits of A I_2, at beta = 2 with the signs and integrality of 4.13 and for every beta > 0
  without them): independent proofs P296, P299 and P303: CONFIRMED; referee audits A167 (VALID) and A169 (VALID with
  scope corrections); complete-entry verification 07:11 to 07:21 (P304, 167 controls): CONFIRMED with the seven
  wording corrections; entered 07:27.
- 2026-10-22 07:16 to 08:19 4.54 (the next vorticity relation at a simple end of the axis component, beta = 2: in the
  family of 4.53 (e) it has a smooth solution only if H = -k^7/231, which with the signs of a profile gives A k < 0
  and I_2 -> +infinity from below; other local real analytic solutions of the five axis relations, with the signs and
  integrality of 4.13, have every finite limit of I_2 and both infinite limits of A I_2): independent proofs P306 and
  P311: CONFIRMED; referee audit A170 (VALID with three corrections); complete-entry verification 08:08 to 08:16
  (P312, 242 controls): CONFIRMED, three wording corrections; entered 08:19.
- 2026-10-22 07:26 to 08:50 4.55 (two further axis relations at a simple end of the axis component, beta = 2: in the
  family of 4.54 (a) with H = -k^7/231 the relations for the coefficients of x^6 in Theta and of x^5 in Omega on the
  axis have smooth solutions for exactly one choice of the two free constants of D and gamma, the coefficient matrix
  of the two residues having determinant -27 C^2 k^2/125): independent proof P308: CONFIRMED; referee audit A171
  (VALID; one intermediate display corrected in its adjudication P320); complete-entry verification 08:42 to 08:49
  (P319, 129 controls): CONFIRMED; entered 08:50.
- 2026-10-22 08:36 to 09:26 4.56 (the axis relations of every order at a simple end of the axis component, beta = 2:
  in the family of 4.54 (a) with H = -k^7/231 the relations (T_n), (V_n) and the curl relation of 4.49 (2) of every
  order have solutions that are real analytic on one interval about the end for exactly one choice of the two free
  constants at each order, the coefficient matrix at order n having determinant -54 C^2 k^2/(25 n (2 n + 1)); formal
  in x, no convergence, no profile): independent proofs P321 (192 controls) and P326 (88 controls): CONFIRMED; referee
  audits A173 (VALID) and A174 (VALID); complete-entry verification 09:13 to 09:22 (P325, 611 controls): CONFIRMED;
  entered 09:26.
- 2026-10-22 09:05 to 09:57 4.57 (the leading part of the temperature series at a simple end of the axis component,
  beta = 2: in the family of 4.56 the series Theta in x^2 and u = y_* - y has no term of total degree below 11, and
  its part of degree 11 is (C/2) x^2 (u - k x^2/11)^10; formal, no zero curve, no convergence, no profile):
  independent proof P328 (156 controls): CONFIRMED; referee audit A175 (VALID for the proof); complete-entry
  verification 09:35 to 09:49 (P332, 1983 controls): CONFIRMED, one correction of the Scope; entered 09:57.
- 2026-10-22 09:26 to 10:16 4.58 (a factorization of the temperature series at a simple end of the axis component,
  beta = 2: in the family of 4.56, Theta = (C/2) x^2 Z^10 with a formal series Z in x^2 and u = y_* - y whose part of
  degree 1 is u - k x^2/11, Z being u - h(x^2) for a formal invariant curve times a formal unit, and Theta = (C/2) I^2
  for the odd formal first integral I = x Z^5; formal, no convergence, no off-axis zero curve, no profile):
  independent proof P331 (184 controls): CONFIRMED; referee audit A176 (VALID); complete-entry verification 10:02 to
  10:15 (P336, 1107 controls): CONFIRMED; entered 10:16.
- 2026-10-22 10:00 to 10:33 4.59 (the temperature near a simple end of the axis component, necessary conditions, every
  positive beta: near (0, y_*), Theta = (C_u/2) x^2 Z^n with Z = (u - H(x)) L, L > 0 smooth and u = H(x) the smooth
  unstable curve of W, H = k x^2/(4 beta + 3 kappa) + O(x^4); Theta vanishes there exactly on the axis and on this
  curve, has the sign of C off them if n is even and changes sign across the curve at its points with x != 0 if n is
  odd; no profile): independent proofs P334 (beta = 2, kappa = 1, 53 controls) and P337 (74 controls): CONFIRMED;
  referee audit A177 (VALID with two fixes, both adopted); complete-entry verification 10:14 to 10:33 (P338, 271
  controls): CONFIRMED; entered 10:33.
- 2026-10-22 10:16 to 10:43 4.60 (the vorticity near a simple end of the axis component, necessary conditions, beta at
  least 2: near (0, y_*), Omega = E_u x Z^m Y with Y smooth and positive, Z and the curve u = H(x) as in 4.59 and m =
  1 + (2 beta + 1)/kappa; Omega vanishes there exactly on the axis and on the same curve as Theta, to the order m off
  the axis, and x Omega Theta is positive off the two curves; no profile): independent proof P339 (183 controls):
  CONFIRMED; referee audits A178 (VALID, no corrections) and A179 (the text of the entry, VALID, no corrections);
  complete-entry verification 10:27 to 10:42 (P342, 533 controls): CONFIRMED; entered 10:43.
- 2026-10-22 10:46 to 10:59 Summary and section 5 sentences on 4.57 to 4.60 (the formal factorization of the
  temperature series at beta = 2 and the factorizations of Theta and Omega near a simple end of the axis component):
  referee audit A180 (VALID, no corrections); complete-entry verification 10:55 to 10:57 (P345, 246 controls):
  CONFIRMED, two wording clarifications; entered 10:59.
- 2026-10-22 12:43 Completion of the research text of the report: the headline (UNRESOLVED; neither accepted
  endpoint reached), the recorded session durations and the position of the end of the analysis relative to the 48 h
  wall-clock cap. The remaining editorial items of the fifth referee review are settled as follows: the section 4
  results are traced to their packets and consultations in Table 8.1, and the timeline is condensed in this section
  (the complete timeline is among the artifacts).
- 2026-10-22 12:44 End of the run at the 48 h wall-clock cap.
- 2026-10-22 13:05 Finalization, with no new research: the summary and the run record at the head of the report, the
  removal of internal working references, and the assembly of the accompanying artifacts of section 8, including the
  regeneration of the consolidated residual table from the published files (identical to the stored table).

## 8. Accompanying artifacts

The accompanying artifacts are published beside this report; Table 8.3 describes their contents. The accompanying
artifacts include instructions and commands that regenerate the consolidated residual table, recompute an independent
regional residual evaluation with its exact center and inverse-constant certificates, run the tests of the independent
inverses and regenerate the numerical states. There is no candidate profile to regenerate.

- Proof notes: section 4 contains proof outlines. The accompanying artifacts contain the written proof of every
  packet P cited in this report, the available summaries, a reading-order index, a chronological catalog and the
  final synthesis of the independent verification. Tables 8.1 and 8.2 identify the packets by result.
- Specification of the admissible class, canonical inverse and numerical diagnostics, with its change log, in the
  accompanying artifacts.
- Numerical code in the accompanying artifacts: the characteristic (semi-Lagrangian) solver with Levenberg-Marquardt continuation on the
  vorticity coefficients, the collocation solver, the forcing-homotopy continuation and the modal whole-plane
  Biot-Savart inverse, the evaluation and diagnostic scripts and tests on manufactured solutions; the solver commands
  with their arguments are listed in the accompanying artifacts.
- Independent verification code in the accompanying artifacts: the independent Cartesian whole-plane inverse and
  adaptive modal Green inverse, center-strain quadrature, residual and regional-grid evaluators, the exact
  rational-arithmetic certificate scripts, the symbolic checks of section 4 and their tests on manufactured solutions.
- Coefficient files and residual tables in the accompanying artifacts: the 59 stored states and the independent
  evaluation snapshots are the inputs of the consolidated residual table (123 independently evaluated states, 5904
  rows of absolute and normalized residuals in six radial bands). Evaluation packet P287 contains the six
  quadrature-resolved states, their comparison states, recorded regional residuals and exact certificates. None of
  these states is a candidate profile (section 6). When the accompanying artifacts were assembled, the consolidated
  table was regenerated from the published files alone; the result was identical to the stored table (SHA-256
  9367a7e40633d1c26b8d62469090983ca9612dad388eb9fd1826c24061f6c60d).
- Complete verification timeline in the accompanying artifacts: every verification report, referee audit and
  correction, with the time at which each correction was adopted (section 7 gives the dated milestones).
- Not published, because of their size (about 1.2 GB): the working archives, with the work logs, the run logs, the
  other intermediate coefficient files, the inputs and outputs of the other verification packets (among them the
  certificate files of Table 8.2 other than those of P287), the records of the independent evaluations and runs (E,
  R) and the records of the consultations with the external referee (A).
- Computing environment and budgets: one shared Linux host (Linux 6.12, x86_64, Intel Xeon Platinum 8275CL); the
  analysis and the numerical solvers used Python 3.9.25 with NumPy 2.0.2, SciPy 1.13.1, mpmath 1.3.0 and SymPy 1.14.0,
  the GPU solvers also PyTorch 2.8.0 (CUDA 12.8) on a single NVIDIA A100-SXM4-80GB; the independent verification used
  a separate environment, Python 3.12.13 with NumPy 2.5.0, SciPy 1.18.0, mpmath 1.3.0 and SymPy 1.14.0. All CPU work
  was single-threaded, each process under 16 GB of memory, and each interactive command under 10 minutes; longer jobs
  ran detached under a wall-clock timeout, with their logs and periodically saved coefficient files kept as restart
  inputs. The task asked for at least 48 hours of elapsed active research unless a decisive endpoint was attained and
  independently audited earlier. The controlling run instructions capped wall-clock elapsed time at 48 hours from T0.
  The real start, end, elapsed time and recorded session durations are given at the head of this report. Active
  research time was not separately metered, and no claim of 48 hours of elapsed active research is made. Failed and
  abandoned attempts are listed in section 6 and in the timeline; their logs are in the working archives.

Identifiers. P denotes a proof or check packet of the independent verification, E an independent evaluation or
verification report, R an independent search or computation run of the verification, A an analytic consultation
(referee audit, research consultation, literature check or whole-report review). The packets P are published as
described above; the records E, R and A are in the working archives, and the results they support are stated in this
report with their verdicts.

Table 8.1. Section 4 results: independent proof packets (P), analytic consultations (A) with their verdicts as finally
adopted. "Derivation" marks a consultation that derived the result without a verdict word. Every INVALID item listed
was not used in the report (removed, or the statement restricted), as recorded in the complete verification
timeline.

| Result | Independent proof or check | Analytic consultations |
|---|---|---|
| 4.1 | P03; verification log, center constraints (2026-10-20 12:55 to 13:16) | A01: center jet and 2-jet VALID WITH FIXES, canonical velocity VALID |
| 4.2 | P01 | A01: VALID (with the backward-trapping lemma VALID) |
| 4.3 | P04; P01 (conditional growth) | A01: VALID, three items VALID WITH FIXES; A09 (whole-report review) |
| 4.4 | P02 | A01: VALID (local statement) |
| 4.5 | P06 | A02: derivation; A65: VALID |
| 4.6 | P05, P23, P32, P33 | A03: VALID, some steps VALID WITH FIXES; A12: VALID, one item VALID WITH FIXES |
| 4.7(i)-(ii) | P08 | A02: derivation; A04: VALID WITH FIXES and VALID; A10: flatness of Omega VALID |
| 4.7(iii)-(iv) | P45; P44 (related); P156, P158 (6.3: both equations near the center and along the open arc, on a configuration that is not a profile); E379 (the 6.3 text before entry, read against P156 and P158): CONFIRMED; P159 (6.3: the same configuration deformed so that the strong unstable curves are not real analytic): CONFIRMED; P161 (6.3: the configuration with Theta = L and Omega = 0 on open sets adjacent to the endpoints): CONFIRMED; E401 (the 6.3 text before entry, read against P161): CONFIRMED; E415 (the P161 paragraph after entry): CONFIRMED, with a clarification of the choice of the sets O, adopted | A20: derivation; A22: VALID, one item VALID WITH FIXES; A99 (6.3 addition): VALID WITH FIXES (wording of the endpoint statements); A102 (6.3 addition on P159): VALID WITH FIXES (scope of the preserved properties, the invariant set on which (V) fails); A104 (6.3 addition on P161): VALID WITH FIXES ((V) fails somewhere on each invariant set O; the exception removed) |
| 4.7(v)-(vii) | P53, P54 | A25: derivation; A27: VALID, two items VALID WITH FIXES |
| 4.7(viii) | P55 | A30: VALID (a beta > 2 analogue INVALID) |
| 4.7(ix) | P56 | A32: VALID WITH FIXES |
| 4.7(x) | P59 | A33: VALID WITH FIXES (an additional contradiction claim INVALID) |
| 4.7(xi) | P58 | A49: VALID |
| 4.7(xii) | P162 (independent proof of (b), with a general proof of (a)): CONFIRMED; E401 (the text of (xii) before entry): CONFIRMED; E415 (the text of (xii) and the boundary statements after entry): CONFIRMED; P164 (the polynomial case of (c)), P166 (independent proof of (c), with only the value trace analytic): CONFIRMED; P168 (the hypothesis of (c) on U(0, .) not implied by that on Omega and the local structure, in the second configuration of 6.3): CONFIRMED; P199 (independent proof of (d)): CONFIRMED | A104: VALID ((a), (b), the equivalence), wording fixes (notation; the boundary statement of Scope of (iii)-(iv)); A106 ((c)): VALID, the analytic normal derivative trace redundant, notation fixes; A109 (P168): VALID with fixes (the full trace of U is not flat, only W_s(0, .) and the remainder of W_z(0, .); orientation of the normal); A130 (research consultation): derivation of (d); A131 ((d) and the related text): VALID WITH FIXES (representation domain, trace of the auxiliary field, symbol determinant and r = 0, regularity in the summaries), all adopted |
| 4.7(xiii) | P174 (independent proof of (a), (c), (d) and of the cubic term of (b)): CONFIRMED; P175 (independent proof of the general odd-order formula of (b)): CONFIRMED | A110 (research consultation): Derivation of (a), (c) and (d); A113 ((a) to (d)): VALID, with fixes to the proof of (b) (the potential is formal; the contradiction in (c) is the extension of gamma beyond p; the curvature convention); A112 (the higher-order formula of (b)): VALID, with a fix to the linearized recurrence; A114 (the text of (xiii) and of the related summary sentences): VALID, with wording fixes (local invariance, the incoming case of the count, the local entry condition, the formal potential) and two expanded proof steps (the linearized constant, the axis index inequality) |
| 4.7(xiv) | P177 (independent proof of the conclusion of (b), of (d) and of (e)): CONFIRMED; P178 (independent proof of (a), of the sector clause of (b), of (c) and of (f), with a check of the text of (a) to (f) before entry): CONFIRMED; P180 (independent construction and check of the planar field of the Scope): CONFIRMED | A115 (research consultation): derivation of (a) to (f) and of the planar field of the Scope; A116 ((a) to (f), the Scope and the related sentences): VALID, with fixes to the proof of (a) (forward limits near the interior of gamma) and of (b) (the backward passage near p and at the zeros off gamma) and to the wording of the Scope |
| 4.7(xv) | P179 (independent proof of (a), (b) and (c) and of the assertion of the Scope, with a different argument in the case W_2 = 0 of (b)): CONFIRMED | A117 ((a) to (c), the Scope and the related sentences): VALID, with fixes to the choice of Q'' and E, the interval step of (a), the position of the points (s, k(s)) in (b), the openness of F in (c), and the Scope (a harmonic extension of the restriction of U to the basin side is not excluded) |
| 4.7(xvi) | P182 (independent proof of (a) to (d) and of the Scope, with the reflection and the position of the axis proved without a y parity condition): CONFIRMED, with a wording fix to the proof of (a) (the backward tails of the strong unstable orbits lie exactly on {u = 0}), adopted | A118 ((a) to (c) and the Scope): VALID, with fixes to the local picture in Q'' (the negative backward limit of u), the parametrization c, the simple-connectedness criterion and the Scope (harmonicity only on the interior of the complement of F); A119 ((d) and the Scope): VALID, with a fix to the proof of (d) (class A by 4.15, boundary of J_+) and to the Scope (stationary endpoints omitted) |
| 4.7(xvii) | P185 (independent proof of the compact-interval Denjoy-Carleman statement, the line and open-closed step, the closure under derivatives, (a) to (c) under the stated hypotheses, and the Scope example with the constant 8 bound and the summation step): CONFIRMED | A122 ((a) to (c), the definition, facts (1) to (3) and the Scope): VALID, with fixes to the statement of the Denjoy-Carleman theorem used, the constants and the notation, the hypotheses of (c), the transport of flatness along C^, the summation step and the constant 8 bound of the example, and the wording of the Scope |
| 4.7(xvii)(d) | P186 (independent proof of the scalar and velocity assertions on a residual set of lines of one transverse family, for each sequence m and for countably many at once; U as a vector function): CONFIRMED | A124 ((d), its proof outline and Scope): VALID, with wording fixes (open arcs of C^, nondegenerate compact intervals, the scope of the scalar example, a fixed sequence m in the exclusion) |
| 4.7(xviii) | P188 (independent proof of (a), (b), (c) and of the converse, with exact algebraic controls): CONFIRMED, with two Scope repairs (the outgoing requirement as an oriented chart condition; the image germ of c), adopted; P195 (6.3: the exact local solutions at interior points of a zero arc): CONFIRMED; P199 (6.3: the type of the equations of (a) with a as evolution variable): CONFIRMED | A125 ((a), (b), (c), the proof outline and the Scope): VALID, with justifications (extension of the frame, smooth dependence, disk coverage by the chart, uniqueness of H) and a Scope repair (the outgoing sign requirement in the equivalence; the consequence of a local solution); A129 (6.3, the exact local solutions): VALID WITH FIXES (scope of the conclusion; the example with the center jet), adopted; A130 (research consultation): the type of the equations of (a); A131 (6.3, that type): VALID WITH FIXES (representation domain, trace of the auxiliary field, symbol determinant and r = 0, regularity in the summaries), all adopted |
| 4.7(xix) | P203 (independent proof of (a) to (d) and of the assertions of the Scope): CONFIRMED; P204 ((e)): CONFIRMED | A132 (research consultation): derivation of (a) to (d); A133 ((a) to (d), the Scope and the related text): VALID WITH FIXES (the Scope sentence on bounds on parts of O; the wording of the summary, 6.3 and Scope sentences), adopted; A134 ((e) and the related text): VALID WITH FIXES (deletion of the Scope clause on profiles without an outgoing endpoint), adopted |
| 4.7(xx) | P206 (independent proof of (a) to (d) and of the assertions of the Scope): CONFIRMED | A135 (research consultation): derivation of (a) to (d), with a different proof; A136 ((a) to (d), the proof outline, the Scope and the related text): VALID |
| 4.7(xxi) | P207 (independent proof of the statement and of the assertions of the Scope): CONFIRMED | A137 (the statement, the proof outline, the Scope and the related text): VALID WITH FIXES (the conclusion is also a corollary of (vii); the wording on local solutions; the Scopes of (iii)-(iv), (xv) and (xx)), adopted; A138 (the revised text): VALID (the Q1 sentence on the scattering identities corrected), adopted |
| 4.7(xxii) | P214 (independent proof of (a) to (d) and of the assertions of the Scope): CONFIRMED | A140 (research consultation): derivation of (a) to (d); A141 ((a) to (d), the proof outline, the Scope and the related text): VALID |
| 4.7(xxiii) | P218 (own proof of (a), with eleven symbolic controls): CONFIRMED; P222 ((b), the assertions of the Scope and the entry text): CONFIRMED | A143 (referee audit of (a); derivation of (b) and of the plateau example of the Scope): VALID WITH FIXES (two Scope sentences), adopted; A144 (the revised text): VALID WITH FIXES (one step of the proof of (b), one Scope sentence), adopted |
| 4.7(xxiv) | P227 (independent check of the proof and of the entry text): CONFIRMED | A145 (referee audit of the derivation): VALID WITH FIXES (the rescaling of Step 0), adopted; A146 (the entry text, including the neighbourhood form): VALID WITH FIXES (wording of the two scope passages), adopted |
| 4.8 | P09 | A02: derivation; A04: VALID WITH FIXES; A06: VALID (sublinear extension) |
| 4.9 | P17, P21 | A07: VALID, one item VALID WITH FIXES (a signed half-plane step INVALID); A05: beta = 2 source |
| 4.10 | P14 | A04: derivation; A10: temperature limit VALID as used in 4.11(ii); A65: VALID |
| 4.11 | P18, P15; verification log (2026-10-20 15:07) | A10: (i), (ii) VALID, (iii) VALID WITH FIXES; A65: VALID WITH FIXES |
| 4.12 | P33 ((a)-(e)), P44 ((g)); verification log (2026-10-20 16:27) for (f) | A14: derivation; A15: VALID WITH FIXES, one item VALID under its condition; A18: (f) VALID; A22: (g) VALID; A65: (f) VALID |
| 4.13 | P27, P28, P30 | A11: derivation; A12: VALID; A18: VALID, two items VALID WITH FIXES (one item INVALID as stated) |
| 4.14 | E041, E063, E071, P192; P70, P82 | A44, A48: literature checks without verdict words; A13, A64: literature consultations that retrieved no primary text (no network access; failed name resolution); A16, A42, A45: VALID WITH FIXES (one item of A16 INVALID); A127: whole-report review including the 4.14(j) addition |
| 4.15 | P39, P40 | A17: VALID WITH FIXES (a bounded-vorticity remark INVALID); A21: VALID, one item VALID WITH FIXES |
| 4.16 | P35, P36, P38 | A19: VALID; A23: VALID |
| 4.17 | P49, P50 | A26: VALID, one item VALID WITH FIXES (shared with 4.18) |
| 4.18 | P48, P49, P51; P52 (a special case of 4.24) | A24: derivation; A26 (shared with 4.17) |
| 4.19 | P57 | A29: derivation; A31: VALID, two items VALID WITH FIXES |
| 4.20 | P60 | A34: VALID WITH FIXES (one further possibility INVALID) |
| 4.21 | P61, P65 | A35: derivation; A36, A37: VALID WITH FIXES |
| 4.22 | P61, P66; P67 (overlaps (d)) | A38: VALID, (d) VALID WITH FIXES |
| 4.23 | P69, P81, P87 | A39: derivation; A40, A41: VALID or VALID WITH FIXES (a scope claim INVALID); A46, A51: VALID WITH FIXES |
| 4.24 | P83, P84 | A47: both claims confirmed under the stated hypotheses |
| 4.25 | P88 | A50: VALID WITH FIXES; A52: VALID |
| 4.26(a)-(c) | P90 | A54: VALID WITH FIXES |
| 4.26(d) | P99, P113; P98 (related) | A59: VALID, one step VALID WITH FIXES; A61 (whole-report review) |
| 4.27 | P91, P92 ((d)) | A55: VALID |
| 4.28 | P119 | A66: (a) VALID, (b) and the Scope VALID WITH FIXES |
| 4.29(a)-(d) | P121 (also P122 for the combined text) | A67 (research consultation: derivation of (b)-(d)); A69: VALID |
| 4.29(e) | P122 | A68: VALID WITH FIXES |
| 4.30 | P123 | A71 (research consultation: second proof, the conic variant); A73: VALID (the second proof VALID WITH FIXES) |
| 4.31(a) | P126 | A70 (research consultation: derivation); A72: VALID WITH FIXES |
| 4.31(b) | P127 | A71 (research consultation: the whole-axis construction and its conic variant); A73 (combination with the reference of 4.31(a)): VALID; A75 (adversarial audit of the entered text): VALID WITH FIXES (proof of (b) and Scope replaced); E212 (verification re-read of the revised text, 2026-10-21 06:01): CONFIRMED |
| 4.32 | P124; P126 (anisotropic fields); P137, P138, P139 ((d)) | A73: (a), (b) VALID, (c) VALID with a proof-text fix, the Scope INVALID as written (replaced); A82 ((d)(ii), (iii) and the Scope): VALID WITH FIXES (flat cases separated, normalization wording); A83 ((d)(i)): VALID |
| 4.33 | P128, P129, P133; P136 ((e)) | A78 (referee audit): VALID WITH FIXES (normalized subclass; exterior hypotheses of (d) not supplied by the slow-tail notation); A82 ((e)): VALID WITH FIXES (beta > 2; leading part smooth off 0) |
| 4.34 | P135 (own standalone proof, exact algebra controls); P137 (Scope sentence on the residual); P140 (6.3: compact conjugacy and the residual moment); P142 (6.3: the invariant x-moment of the residual); P145 (6.3: the large-R asymptotic of the x-moment); P147, P148 (6.3: the configurations with zero residual moments); E408 (the 6.3 summary of P147 and P148 after entry): CONFIRMED with two wording repairs, adopted; P152 (6.3: the variation of the finite part of 4.38); P154, P155 (6.3: every real value of the finite part); E282 (expanded proof outline, checked against P135); E293 (6.3 sentences on the invariant x-moment, checked against P142); E348 (the temperature derivative bounds of (iii), checked against P135); E363 (re-read of the entered bounds of (iii) and 6.3 text): CONFIRMED; E368 (the 6.3 text before entry, read against P154 and P155): CONFIRMED | A77 (research consultation: derivation); A79 (referee audit): VALID WITH FIXES (signs, R > R_ext, existential c_tail, Lipschitz hypothesis); A80 (research consultation: removing the residual; no obstruction found, nothing entered); A82 (Scope sentence): VALID WITH FIXES (matching of the relative velocity); A84 (6.3 sentence on the compact conjugacy): VALID WITH FIXES (a suitable generator; configurations with a nonzero residual); A86 (referee audit of the expanded proof outline): VALID WITH FIXES (notation, the Lipschitz bound of the angular flow, constants uniform in the iterates and in R, identification of weak limits); A87 (6.3 sentences on the invariant x-moment): VALID WITH FIXES (the drift and the temperature, not the physical velocity, fixed outside a compact set; a necessary condition only); A88 (research consultation and audit of the large-R asymptotic): VALID WITH FIXES (0 <= rho <= 1; the L^1 bound of the temperature difference; remainder O(R^{-s})); A95 (the temperature bounds of (iii) and the end of the 6.3 bullet, with the zero-moment configurations and the finite part): VALID, and VALID WITH FIXES for the finite part (the comparison with 4.38 only for beta not in Z_E; mirror supports; the list of retained properties); A97 (6.3, the twists for every real parameter): VALID; A98 (6.3, every real value of the finite part): VALID; A100 (targeted review of the 6.3 text): no error found, the derivation of the zero x-moment made explicit |
| 4.35 | P106 ((a), (b), (d)), P107 ((c)) | A63 (referee audit): (a) VALID; (b) to (d) and the Scope VALID WITH FIXES (rescaling to prescribed a0, nonnegative compactly supported F, scope wording); A81 (referee audit of the entered text): (c) VALID; (a), (b), (d) and the Scope VALID WITH FIXES (coordinates of 4.18(b), converse on a half-axis interval, explicit Laplace densities and bounds) |
| 4.36 | P149 (own standalone proof and exact controls, including the example of (b)); E313, E319, E324 (checks of the first draft, of the revised draft and of the entered version) | A89 (research consultation; derivation of the boundary formula, the critical set and (a), (b), each VALID or VALID WITH FIXES); A90 (referee audit of the draft): VALID WITH FIXES (integer indices; harmonic exceptional terms without logarithms; the coefficient [rho^0 (log rho)^0] and its form at critical beta; (a) restricted to beta not in Z_crit; the wording of (b) and the violation of (V) far out; global (T) essential; x R_Omega in L^1 suffices) |
| 4.37 | P150 (own standalone proof and controls, including the class A application); P151 (continuation of the induction to 4 - s < mu < 4); the verification's check of the draft (normalization of the remainder stream) | A94 (referee audit of the draft): VALID WITH FIXES ((T) on R^2 for the identity of 4.36 and beta not in Z_crit for its reduction; the odd normalization of the Poisson remainder stream; the explicit weight schedule; uniqueness after combining terms and the coefficient convention at resonances) |
| 4.38 | P151 (own standalone proof, including the cubic flux, the exceptional set, the depth of 4.37 and the sign examples with D = 0); E341 (181 exact controls) | A92 (research consultation; the identity, the power count with the cubic flux, Z_E and the reduction, each VALID or VALID WITH FIXES); A93 (referee audit of the draft): VALID WITH FIXES (wording of the sign examples of (d), the scaling and observer scope, the comparison with 4.36) |
| 4.39 | P228 ((a), own proof, 49 exact controls): CONFIRMED; P226 ((b), own proof, 34 exact controls): CONFIRMED; P232 (the entry text): CONFIRMED | A147 (referee audit of both proofs, 19 symbolic checks): VALID |
| 4.40 | P229 (own proof, 53 exact algebra controls, 23 controls of the rescaling and of the dependencies): CONFIRMED; P233 (the entry text, including the application to class A through 4.37 step (5)): CONFIRMED | A148 (referee audit of the proof and of the implication from the symbol bounds to (S)): VALID |
| 4.41 | P230 ((a), own proof, 81 exact controls): CONFIRMED; P231 ((b), own proof, 32 exact controls): CONFIRMED; P235 (the entry text): CONFIRMED | A149 (referee audit of (a), 64 exact checks): VALID; A150 (referee audit of (b), 37 exact checks): VALID |
| 4.42 | P237 (own proof, 52 exact controls): CONFIRMED; P243 (the entry text): CONFIRMED | A151 (referee audit, 56 exact checks): VALID |
| 4.43 | P242 (own proof, 101 exact controls, exact certificate of 563 checks): CONFIRMED; P246 (the entry text): CONFIRMED | A152 (referee audit, 24 derivation checks, exact certificates for both charts): VALID |
| 4.44 | P257 (own proof, 42 exact controls): CONFIRMED; P260 (the entry text): CONFIRMED | A153 (referee audit, 17 symbolic checks): VALID WITH FIXES, fixes adopted |
| 4.45 | P258 ((a) and the monotone case of (b), own proof, 59 exact controls): CONFIRMED; P261 (the positive sign, own proof, 61 exact controls): CONFIRMED; P263 (both signs, own proof, 50 exact controls): CONFIRMED; P265 (the entry text, with one repair adopted): CONFIRMED | A154 (referee audit, 15 exact checks): VALID WITH FIXES (the negative sign is not open; the referee's proof of it is adopted) |
| 4.46 | P264 (the construction, own proof, 48 + 22 exact controls): CONFIRMED; P268 (the concave variant, both signs, 57 exact controls): CONFIRMED; P269 (the entry text, 203 controls): CONFIRMED | A155 (referee audit of the construction, 56 exact checks): VALID; A156 (referee audit of the variant, 19 exact checks): VALID |
| 4.47 | P266 (oscillating axis construction, 62 exact controls): CONFIRMED; P270 (concave construction, both signs, 65 exact controls): CONFIRMED; P271 (beta2 signed exclusion, 46 exact controls): CONFIRMED; P274 (the entry text, 236 controls): CONFIRMED | A157 (referee audit of P266, 27 exact checks): VALID; A158 (referee audit of P270, 37 exact checks): VALID WITH FIXES; A159 (referee audit of P271, 24 exact checks): VALID |
| 4.48 | P272 (critical limits, 79 exact controls): CONFIRMED; P275 (the peaks construction of (c), 91 exact controls): CONFIRMED; P276 (the complete entry with its recorded notation correction, 273 controls): CONFIRMED | A160 (referee audit of P272 and the repaired peaks construction): VALID WITH FIXES; A158 (referee audit containing the peaks construction, 37 exact checks): VALID WITH FIXES |
| 4.49 | P273 (the ends of J, 65 exact controls): CONFIRMED; P278 (the fields, 93 exact controls, 15 scope controls and 25 + 16 supplementary controls): CONFIRMED; P282 (the complete entry text, 223 controls): CONFIRMED with two exact wording corrections | A161 (referee audit of P273, 36 exact checks): VALID WITH FIXES; A162 (referee audit of P278 and of the ends of J): correct, with fixes |
| 4.50 | P283 (the fields, 55 controls and 15 supplementary exact controls): CONFIRMED; P290 (the complete entry text, 165 controls): CONFIRMED | A162 (referee review of 4.49, which proposed the correction along the flow): correct, with fixes; A164 (referee audit of the construction at every beta >= 2): valid with clarifications |
| 4.51 | P286 (the endpoint law and local solutions, 114 exact controls): CONFIRMED; P292 (the complete entry text, 152 controls): CONFIRMED | A166 (referee audit of P286, 53 exact checks): VALID with its precision in step (3) adopted |
| 4.52 | P289 (the local solutions and their limits, 51 exact controls): CONFIRMED; P293 (the complete entry text, 158 controls): CONFIRMED | A165 (referee audit of P289, 37 exact checks): VALID |
| 4.53 | P296, P299 and P303 (local proofs): CONFIRMED; P304 (complete entry, 167 controls): CONFIRMED | A167: VALID; A169: VALID with scope corrections |
| 4.54 | P306 and P311 (local proofs): CONFIRMED; P312 (complete entry, 242 controls): CONFIRMED, three wording corrections | A170: VALID with three corrections |
| 4.55 | P308 (local proof, 256 + 23 controls): CONFIRMED; P320 (adjudication of the audit, 34 controls): CONFIRMED; P319 (complete entry, 129 controls): CONFIRMED | A171: VALID; one intermediate display corrected in its adjudication (P320) |
| 4.56 | P321 (local proof, 192 controls): CONFIRMED; P326 (common interval, 88 controls): CONFIRMED; P325 (complete entry, 611 controls): CONFIRMED | A173: VALID; A174: VALID |
| 4.57 | P328 (local proof, 156 controls): CONFIRMED; P332 (complete entry, 1983 controls): CONFIRMED, one correction of the Scope | A175: VALID (proof) |
| 4.58 | P331 (local proof, 184 controls): CONFIRMED; P336 (complete entry, 1107 controls): CONFIRMED | A176: VALID |
| 4.59 | P334 (special case beta = 2, kappa = 1, 53 controls): CONFIRMED; P337 (proof, 74 controls): CONFIRMED; P338 (complete entry, 271 controls): CONFIRMED | A177: VALID with two fixes, both adopted |
| 4.60 | P339 (proof, 183 controls): CONFIRMED; P342 (complete entry, 533 controls): CONFIRMED | A178: VALID, no corrections; A179 (text of the entry): VALID, no corrections |

Whole-report reviews: A09, A28, A43, A61, A76, A85, A108, A111, A121, A126, A127; targeted reviews of the text changed
between them: A91, A96, A100, A103, A107. Section 6: A53 (P89), A56 (P93), A58 (P95), A62 (P111) audit the exact
certificates; A57 and A60 concern the methods of 6.2; A63 audits 4.35 (formerly part of 6.2).

Table 8.2. Exact rational-arithmetic certificates of sections 6.1 and 6.2 (the written proofs are in the accompanying artifacts;
the inputs with SHA-256 hashes of the stored states, the certificate files and the independent check outputs are in
the working archives).

| Certificate | Packet | Audit |
|---|---|---|
| exact tail witnesses H_0, E_T of six stored states | P89 | A53 |
| closed form of the constant C of 4.26 for a stored state with 2 < b_rep < 3 | P93 | A56 |
| alpha_rep != 0 for the beta = 3 states with 20 modes (and two fixed-basis states) | P95 | A58 |
| mixed-exponent tail witnesses of the states stored with b_rep = beta (source exponent 3) | P101 | verification CONFIRMED 2026-10-21 01:32 (additional written reviews E109 to E112) |
| F > 0 and 2F + x F_x > 0 on R^2 for the 16-mode fixed-basis states at lambda = 0.97, 0.96 | P102 | verification CONFIRMED 2026-10-21 01:46 (additional written reviews E115, E116) |
| C2 < 0 for the four beta-free states at eps = 0.025 to 0.04 | P104 | verification CONFIRMED 2026-10-21 01:56 (additional written reviews E117, E119 to E121); formula of P93: A56 |
| C2 enclosures of the 16-mode states stored with b_rep = beta, 3 < b_rep < 4 | P111 | A62 |
| center-strain mismatch m < 0 (with a > 0) of the seven states of the second path computed at lambda = 0.98 with beta fixed at 2.8323 to 3.4734 | P160 | verification CONFIRMED 2026-10-21 11:40 (E388, E391, E393) |
| limit above 3/5 of the normalized (B2-P) temperature residual at the center, and the forced center-strain mismatch, of the twelve states of the second path at beta = 3.088 to 3.25 | P163 | verification CONFIRMED 2026-10-21 12:06, 12:28, 12:44, 12:54 (E404, E406, E418, E428, E433) |
| limit above 3/5 of the normalized (B2-P) temperature residual at the center, and the nonzero forced center-strain mismatch, of the twelve states of the second path continued downward from beta = 3.088 to 3.0 (24 modes); the center comparison of the 24-mode and 32-mode states at beta = 3.085 | P163 | verification CONFIRMED 2026-10-21 13:53, 14:31, 14:58, 15:18 (E461, E477, E485, E493) |
| nonzero forced center-strain mismatch and nonzero (B2-P) center temperature residual of the two saved intermediate evaluations of the clipped run at beta = 3.3 (lambda = 1, 0.999) | P163 | verification CONFIRMED 2026-10-21 13:04 (E439) |
| limit above 3/5 of the normalized (B2-P) temperature residual at the center, and the forced center-strain mismatch, of the four 32-mode states of the second path at beta = 3.085, 3.0925, 3.1 and 3.11 | P163 | verification CONFIRMED 2026-10-21 13:20, 13:40 (E448, E455); continuation history re-read 14:34 (E479); repaired wording re-read 14:59 (E488) |
| limit above 3/5 of the normalized (B2-P) temperature residual at the center, and the forced center-strain mismatch, of the three 84-radial-interval states of the second path at beta = 3.0925, 3.085 and 3.105; C2 enclosures of these states, of the refitted fields before re-solving and of the 56-interval states at beta = 3.0925 (24 and 32 modes) | P163 | verification CONFIRMED 2026-10-21 15:18, 15:30 (E493, E498) |
| the acceptance of the inherited lambda at beta = 3.0925 (84 intervals and tighter tolerances); the stored lambda differences; limit above 3/5 of the normalized (B2-P) temperature residual at the center and forced mismatch of the two tighter-tolerance states at beta = 3.0925 and 3.1; C2 enclosures of these states and of the 56-interval 24-mode states at beta = 3.085 and 3.1 | P163 | verification CONFIRMED 2026-10-21 15:51 (E507) |
| discontinuity of the fifth x-derivatives of Theta and Omega on the positive x-axis at every interior knot circle, for the stored fields of the two 32-mode states of the second path and of its 24-mode state at beta = 3.0925 | P169 | verification CONFIRMED 2026-10-21 13:20 |
| relative area L2 distances over the whole plane of G = Omega/x and of d_phi G between the stored 32- and 40-mode states at beta = 3.0315, 3.04, 3.05 and 3.062, for the fields defined by the stored coefficients with exact powers and unclipped splines | P187 | verification CONFIRMED 2026-10-21 17:58 |
| forced center-strain mismatch, C2 enclosures and nonzero temperature tail coefficients of positive order of the six fields of the map-scale comparison (the two states of the Jacobian diagnostics at L = 1, 1.5 and 2.5) | P217 | verification CONFIRMED 2026-10-21 22:43 |
| two zeros of W_2(0, .) on the negative y-axis, with positive and with negative derivative, for the prescribed transporting field of one literal two-lobe source at eps = 0 | P238 | verification CONFIRMED 2026-10-22 01:01 (additional written review 01:05) |
| rank 519 on 691 active coefficients of the temperature value-fit matrix with 16 angular modes on 12 sampled angles of the signed eps = 0 scan | P239 | verification CONFIRMED 2026-10-22 01:12 |
| limit above 3/5 of the normalized (B2-P) temperature residual at the center, the forced center-strain mismatch, C2 enclosures and nonzero temperature tail coefficients of positive order of the three 40-mode states of the second path at beta = 3.0925, 3.085 and 3.1 | P248 | verification CONFIRMED 2026-10-22 02:13 |
| the same for the two 40-mode states of the second path at beta = 3.11 and 3.076 | P251 | verification CONFIRMED 2026-10-22 02:25 |
| the same for the two 48-mode states of the second path at beta = 3.085 and 3.1 | P254 | verification CONFIRMED 2026-10-22 02:40 |
| exact next-order endpoint coefficients of the 40-mode state of the second path at beta = 3.085 (relative discrepancies from the next-order relation of its own leading vorticity tail) | P253 | verification CONFIRMED 2026-10-22 02:34 |
| nonzero limit of the normalized (B2-P) temperature residual at the center, the forced center-strain mismatch, C2 enclosure and nonzero temperature tail coefficients of positive order of the 48-mode state of the first path at beta = 3.076 | P262 | verification CONFIRMED 2026-10-22 03:23 |
| the same for the 48-mode state of the first path at beta = 3.092 | P267 | verification CONFIRMED 2026-10-22 03:52 |
| the same for the 48-mode state of the second 48-mode run of the first path at beta = 3.076 | P277 | verification CONFIRMED 2026-10-22 04:54 |
| the same for the 48-mode state of the second 48-mode run of the first path at beta = 3.062 | P280 | verification CONFIRMED 2026-10-22 05:05 |
| nonzero limits of the normalized (B2-P) temperature residual at the center, the forced center-strain mismatches, C2 enclosures and nonzero temperature tail coefficients of positive order of the six stored stages of the two paths restarted with 48 quadrature points per radial cell | P287 | verification CONFIRMED 2026-10-22 06:15 |
| nonzero limits of the normalized (B2-P) temperature residual at the center, the forced center-strain mismatches, C2 enclosures and nonzero temperature tail coefficients of positive order of the two redeterminations of lambda for the 32-mode stage of the first path at beta = 3.062 with 12 and 48 quadrature points per radial cell | P294 | verification CONFIRMED 2026-10-22 06:37 |
| tail coefficients of the states stored with b_rep = beta at lambda = 0.99 (12, 16 modes), 0.98 to 0.965, 0.96 (16, 24 modes), 0.955 (24 modes), 0.95 (24, 32, 40 modes), 0.945 (32, 40 modes), 0.94 (32, 40 modes), and of the states at beta = 3.023855, 3.0315, 3.04, 3.05 and 3.062 (32 modes, lambda = 0.9400, 0.9367, 0.9343, 0.9326 and 0.9317), of the 40-mode states at beta = 3.0315, 3.04, 3.05, 3.062, 3.076 and 3.092 (lambda = 0.9367, 0.9343, 0.9326, 0.9317, 0.9317, 0.9327), and of the first state of the second path (beta = 3.0867, lambda = 0.99, 24 modes), its saved failed state at lambda = 0.98 (beta = 3.0415), and its states at beta = 3.105, 3.2 and 3.25 (lambda = 0.990022, 0.994211, 0.998139; 24 modes) and 3.0925 and 3.085 (lambda = 0.989975, 0.990033; 32 modes), its three 84-radial-interval states at beta = 3.0925, 3.085 and 3.105 and its two tighter-tolerance states at beta = 3.0925 and 3.1 (24 modes), and C2 enclosures of all of them except the 12-mode state at lambda = 0.99 (for which E156 gives the thermal-tail witness only) | E156, E118, E130, E148, E153, E161, E168, E189, E174, E208, E219, E248, E271, E304, E325, E365, E377, E525, E530, E548, E557, E339, E354, E409, E429, E440, E447, E517 (Table 6.1e gives the evaluation of each state) | none |
| nonzero exact residual coefficients of the stored trial fields of section 6.2: fractional far-field powers for the ten free-beta stream-function fits; center coefficients for the twelve fractional-tail fits; thermal Taylor coefficients of degree at most 4 and leading angular primitive moments for the eighteen fits of the first horizontal-primitive search; thermal Taylor coefficients of degree 5 for all eighteen stored fields of the second horizontal-primitive search, and nonzero horizontal offsets for its six final fields | P114, P115, E152; P116, P118, E164; P128, R087; P134, P136, E311, E312 | none |

Table 8.3. Recorded inventory of the accompanying artifacts before publication edits (sizes in bytes; 1244 files
and 20.5 MB in total, no file larger than 1.5 MB).

| component | files | bytes | contents |
|---|---:|---:|---|
| Reproduction instructions | 1 | 8019 | contents, software versions and the commands for regeneration and recomputation |
| Mathematical specification | 1 | 87509 | admissible class, canonical inverse, normalization, identities and numerical diagnostics, with the change log |
| Numerical sources and summaries | 137 | 1899459 | solver, continuation, evaluation and diagnostic scripts, tests, seed states, evaluation summaries, consolidated residual tables, reproduction instructions |
| Stored coefficient states | 59 | 4567620 | stored coefficient files (NPZ) entering the consolidated residual table |
| Independent residual inputs | 124 | 5238610 | independent regional residual evaluations and the coefficient snapshots they evaluated |
| Independent verification sources | 437 | 2052876 | independent inverses, evaluators, exact certificate scripts, symbolic checks and tests |
| Evaluation packet P287 | 48 | 2796026 | evaluation packet P287: states, manifest, regional residuals, center and inverse-constant certificates |
| Proofs and summaries | 435 | 3642521 | written proofs and summaries of the packets P, reading-order index, chronological catalog |
| Verification synthesis | 1 | 14861 | final synthesis of the independent verification |
| Verification timeline | 1 | 172388 | complete verification timeline |
