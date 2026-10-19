# IPM Setting II: fully asymmetric full-plane self-similar profiles with a moving center

Status: FINAL. NOT REACHED: neither admissible endpoint was reached, neither NO (rigorous nonexistence) nor YES
(strong numerical existence evidence). No nonexistence theorem has been proved for a natural full-plane class (in
particular not for the class S of Section 2 or for its subclasses S^+ and S^+_even of Section 3), and no candidate
profile passed the parity-free YES checks. Remaining gap for NO: for a general profile in S the proved structure
(c_l >= 1/gamma > 1 and the far field r^p A(th), Theorems A and 3.1) is not followed by any bound on c_l or any
obstruction; the angular conditions on A obtained so far (Section 4.18(e)) are met by explicit angular functions at
every c_l > 1 with 4c_l not an integer, so they exclude nothing beyond c_l > 1. Remaining gap for YES: no state
meeting both matching conditions of Section 5.8 was found, and the parity-free solvers tested did not converge at
x-odd data, so there is no candidate to which the resolution, domain and residual checks of the task could be
applied. The report records partial results with complete proofs, their verification and the outstanding gaps
(Section 7, item 7).

## 0. Timeline and environment
- T0 = 2026-10-17T17:37:18Z (start of the research run). The run was stopped at its fixed execution limit, 48 hours
  after T0 (2026-10-19T17:37:18Z); no research was done after that time. T_end = 2026-10-19T17:49:26Z (the time
  of this final version, written after the stop). Elapsed time T_end - T0 = 48 h 12 min.
- The 24-hour minimum. The prompt's minimum of 24 hours was met: the elapsed time exceeds 24 hours. The lead
  analyst's work ran in ten consecutive working sessions of at most six hours each from T0 to the stop, each after
  the first started automatically 30 seconds after the previous one ended, and the other two roles worked in sessions
  of the same kind; the state was carried between sessions by written, timestamped logs (work logs, run logs with job
  times, the verifier's dated report and the dated entries of Section 6). Elapsed time measures duration only; the
  work done in it is what Sections 2-9 and the dated entries of Section 6 record.
- Terminal status. Neither admissible endpoint was reached. The task permits a successful terminal research result
  only when the NO or the YES standard has been met, and passing 24 hours alone does not permit stopping while
  further research remains possible. The investigation was ended by the fixed execution limit, not by a result. This
  report therefore records partial results and the limitation; it is not a successful terminal research result. The
  outstanding gaps are listed in Section 7, item 7.
- Organisation. Three roles worked in parallel: a lead analyst (admissible class, velocity law, analysis and
  this report), a numerical researcher (solvers and searches, Sections 5 and 8) and an independent verifier with its
  own code and hand derivations; in addition the written proofs and the report were read in separate adversarial
  audits by an external referee, a second model. Section 6 records these checks.
- Environment: Linux (x86_64), Python 3.9 with numpy 2.0, scipy 1.13 and sympy 1.14 (CPU, single thread) for analysis
  and exploratory computations; GPU computations (one A100 each, float64, PyTorch 2.8 in the solver code) for the main
  solver and the independent verifier. Section 8 describes the algorithms and gives selected data.
- Accompanying artifacts. The accompanying artifacts contain the code of the three numerical implementations of
  Section 8 (LP1, LP2 and PG) and of the spectral and characteristic solvers of Section 5.1, the independent
  verifier's symbolic and numerical check scripts, and a small set of computed records, with a README that lists the
  contents and the commands for the validation tests and checks. Most computed states and run logs are not included,
  so not every number of Sections 5 and 8 can be recomputed from the folder alone. Section 5 is not by itself
  reproducible YES evidence, and none is claimed. The proofs printed here do not depend on the accompanying artifacts
  or on any external proof record.

## 0a. Summary of the outcome
This summary restates results that are stated, proved or measured in the sections cited; it adds none, and the
statements there, with their hypotheses, are the authoritative ones.
1. Outcome. Neither admissible endpoint was reached. No nonexistence theorem is proved for a natural full-plane class
   (in particular not for the class S below, nor for its subclasses S^+ and S^+_even of Section 3), and no candidate
   profile passed the parity-free YES checks (Sections 5 and 7).
2. Reduction. The moving-centre ansatz gives the profile system of Section 1, and the quadratic Taylor comparison at
   the centre together with the Poisson equation at 0 gives c_l = 1/2 + psi_xy(0), psi_yy(0) = psi_xx(0) = 0 and grad
   U(0) = diag(-c, c) with c = psi_xy(0) (Section 1).
3. Admissible class and velocity law (Section 2). In the class S, rho is C^3 with the jet and
   |rho| <= C(1 + |X|)^gamma, |grad rho| <= C(1 + |X|)^(gamma - 1) for some gamma in [0, 1). The velocity is the
   once-subtracted Biot-Savart field W, the unique field with div W = 0, curl W = -d_x rho, W(0) = 0 and W = o(|X|),
   so no gauge remains in S: a harmonic addition such as lambda x y to psi adds the velocity lambda(-x, y), which
   W = o(|X|) excludes. For every family of bounded measurable sets D_R containing B(0, R), the centred velocities of
   the truncated densities converge to W in C^2_loc (Proposition 2.1(a)). The formal solution rho = x^2, psi = -x^3/3
   has growth 2 and lies outside S. In the growth classes 1 <= gamma < 2 the twice-subtracted law leaves a linear
   strain, which the jet fixes for a profile; for higher growth harmonic stream-polynomial gauges remain, and in a
   suitable gauge rho = x^2 is a formal solution for every real c_l (Section 9.14).
4. Structure of profiles in S (complete proofs in Section 9). Every nonzero profile in S has c_l >= 1/gamma > 1, so it
   focuses in finite time, and has the far field r^p A(th) with p = 1/c_l and A not identically zero
   (Theorems A and 3.1). Every critical point of rho is a zero of rho, rho has no nonzero local extrema, and every
   zero of V is a zero of rho (Theorem B); the moment law Q[rho] = pi c (c - 1/2) holds (Theorem C). In S^+ (0 the
   only zero of V) rho = xi^2 >= 0, the zero set is the strong unstable manifold of 0, and A has exactly two zeros,
   both quadratic (Theorems B and 3.2).
5. Restricted nonexistence (complete proofs). No profile in S equals r^p A(th) exactly outside a disk, and for every
   profile in S the far-field correction r^(2p-1) J_p[A]/(l - 1) is forced and nonzero in the distributional scaling
   sense of Theorem 3.16(a) (Theorem 3.16, Proposition 3.18(c)). In S^+_even (the x-even part of S^+) no profile has
   g = d_x^2 W_2(0, y) >= 0 on {y <= 0}, W_2 the second component of W (Proposition 3.14), and none has
   A''(-pi/2) <= A''(pi/2) together with w_e <= 0 on (0, inf), or both inequalities reversed, except with equal
   curvatures and w_e = 0 identically (Proposition 3.17, with the notation there); neither sign condition is known for
   a general profile. In the growth classes 1 <= gamma < 2, no profile has the form f(x) or f(x) + h(y)
   (Section 2, proof in Section 9.14). The exclusions of Propositions 2.3-2.6 require additional hypotheses, which
   differ between the statements: a sublinear or power bound on the twice-subtracted velocity and, in some statements,
   a Hessian bound, x-evenness with nondegenerate zeros of V, rho >= 0 (for gamma = 1), or parameter conditions
   (Propositions 2.3(c), 2.4(c), 2.5(c)-(e) and 2.6(c)-(e), restated in Section 7, item 1); these hypotheses are not
   derived from the class bounds, and for 1 < gamma < 2 the class bounds alone do not imply the sublinear bound
   W_2 = o(r) (Proposition 2.7(e)). Without that bound, still for 1 < gamma < 2, no profile is even in y and none
   satisfies rho(-X) = rho(X), and under the Hessian bound |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2) every homogeneous
   limit at infinity of a profile is 0 or of the form a(r + sigma x)^gamma, and is 0 if the profile is even in
   x (Proposition 2.8(c), (f)); whether a profile can have such a nonzero limit is not decided, but
   rho - a(r + sigma x)^gamma with a != 0 is not O(r^q) for any q < 1, with or without the Hessian bound, and the same
   holds for the other homogeneous stationary functions vanishing in only one direction (Proposition 2.8(h)). For a
   limit f = F(e.X) != 0 as in Proposition 2.7(d) with rho - f = O(r^q), 0 <= q < 1, and q(2l - 1/gamma) < 1, also
   without the Hessian bound, f has a positive amplitude, both amplitudes are nonzero if l >= 1/6, they have opposite
   signs if l > 1/4, and no such limit exists if l = 1/4 or l > 5/12; so rho - a|x|^gamma is not O(r^q) for a < 0, nor
   for a != 0 if l >= 1/4 (Proposition 2.8(h)). If the profile is C^m for an integer m >= 3, both amplitudes are
   nonzero already if l >= 1/(2m), for 1/4 + 1/(2m) <= l <= 5/12 it can have such a limit only if l = 1/4 + 1/(2n)
   with n an odd integer, and both amplitudes are positive if 3/16 < l < 1/4 and (m - 1)(2l - 1/4) >= 1; if the
   profile is C^infinity and 0 < l < 1/4, both amplitudes are positive (Proposition 2.8(h)). The other cases, namely
   limits with a positive amplitude for l < 1/4 or 1/4 < l <= 5/12 (among them a|x|^gamma with a > 0 and l < 1/4),
   q(2l - 1/gamma) >= 1, and limits whose remainder is not O(r^q) for any q < 1, are not decided. The angular
   conditions on A listed in Section 4.18(e) hold for explicit angular functions at every c_l > 1 with 4c_l not an
   integer, so they give no bound on c_l beyond c_l > 1; no density or velocity on the plane is constructed there.
6. Numerics (Section 5). The searches of 5.3-5.5 either drifted toward c_l = 1 or broke down. In a forced continuation
   in c_l (5.7) none of the branches comes near zero forcing relative to the field on its resolved range. In the
   forward reformulation of 5.8, on x-even data, a crossing of the discrete scalar diagnostic m1 = 1/2 was located
   numerically, to the quoted accuracy, in a one-parameter family at p = 0.5, and the functional condition fails
   there. In the x-even states computed, the functional condition fails through an up-down asymmetry D of the
   near-node density (renormalised as in 5.8(iv) when m1 != 1/2). Among the states where D is resolved in the limited
   sense of Section 7, item 5, D ranges from -1.55 to -0.26; the upper end occurs at p = 0.35 with m1 about 0.505, not
   at a crossing, and its inner and outer radius checks are incomplete. This range is not a bound on D. In parity-free
   tests at one x-even state (5.8(vii)) no tested solver converged at x-odd data. These are observations about the
   discretisations used; they give neither existence nor nonexistence.
7. Open. Existence or nonexistence of profiles in S, in S^+ and in S^+_even, and in the growth classes
   1 <= gamma < 2 without the additional hypotheses, remains open (Section 7).

## 1. Problem and conventions
Physical system on R^2: d_t varrho + u.grad varrho = 0, u = grad-perp Psi = (-Psi_{z2}, Psi_{z1}), -Lap Psi = d_{z1}
varrho. With gravity along -e_2, u = -grad P_phys - varrho e_2, where P_phys is the pressure. Ansatz
X = C_l(t)(Z - Z_*(t)), varrho = C_rho(t) rho(X), Psi = (C_rho/C_l) psi(X), with -C_rho'/(C_rho^2 C_l) = 1,
c_l = C_l'/(C_rho C_l^2) constant and Z_*' = C_rho U(0).
The profile system is
    V.grad rho = rho,   V := c_l X + W,   W := U - U(0),   U = (-psi_y, psi_x),   -Lap psi = d_x rho   on R^2,
with the jet rho(0) = 0, grad rho(0) = 0, rho_xx(0) = 2, rho_xy(0) = rho_yy(0) = 0. Notation: c := psi_xy(0),
p := 1/c_l. Verified facts about the reduction: substituting the ansatz reproduces exactly this system (symbolic
check); P := C_rho C_l satisfies dP/dt = (c_l - 1) P^2. On the focusing branch C_rho, C_l > 0 (so P > 0), c_l > 1
means focusing in finite time T with P = 1/((c_l - 1)(T - t)), c_l = 1 exponential focusing, 0 < c_l < 1 focusing only
as t -> infinity; all focusing statements below refer to this branch.
Quadratic Taylor comparison plus the Poisson equation at 0 give c_l = 1/2 + c, psi_yy(0) = psi_xx(0) = 0,
grad U(0) = diag(-c, c), grad V(0) = diag(1/2, 2c_l - 1/2). Among the coordinate reflections, only
x -> -x (rho(-x,y), psi -> -psi(-x,y)) preserves the jet; y -> -y and X -> -X require rho -> -rho.

## 2. Admissible class and the full-plane velocity law
Class S (primary). rho in S if rho in C^3(R^2), satisfies the jet, and for some gamma in [0, 1)
    |rho(X)| <= C (1 + |X|)^gamma,   |grad rho(X)| <= C (1 + |X|)^(gamma - 1).
Velocity law in S: W is the once-subtracted Biot-Savart integral (absolutely convergent at infinity, principal value
at Y = X)
    W(X) = p.v. int [K(X - Y) - K(-Y)] rho(Y) dY - (rho(X) - rho(0))/2 e_2,
    K(Z) = (-sin 2th_Z, cos 2th_Z)/(2 pi |Z|^2),
equivalently the unique vector field with div W = 0, curl W = -d_x rho, W(0) = 0 and W(X) = o(|X|). Uniqueness:
two such fields differ by the gradient of a harmonic function with sublinear gradient, hence by a constant, which
W(0) = 0 removes (complete proof: Section 9.0, Steps 1-2). Consequently there is no gauge freedom in S: adding a
harmonic polynomial of degree >= 2 to psi adds a velocity of degree >= 1 (for example lambda xy gives lambda(-x, y)),
which violates W = o(|X|); constants in U are removed by the moving-centre subtraction. The formal solution of the
task statement, rho = x^2, psi = -x^3/3, solves the differential equations but has growth 2 and lies outside S, so the
canonical law does not apply to it; relative to the particular solution -x(x^2 + y^2)/4 its stream function contains
the harmonic cubic -(x^3 - 3 x y^2)/12, whose velocity is quadratic and which W = o(|X|) excludes in S.
Why S. (i) It is a natural class in which the full-plane law is canonical (one subtraction, no constants, a unique
velocity). (ii) Every nonzero profile in S is a finite-time focusing profile (Theorem A below), with a
time-independent Holder far field at the focusing time. (iii) Profiles with c_l <= 1 are excluded from S by Theorem A.
Classes with growth exponent gamma in [1, 2) (rho in C^3 with the jet and the bounds of S with such a gamma): the
growth bounds no longer give absolute convergence of the once-subtracted integral, and a twice-subtracted field W_2,
normalized by W_2(0) = 0 and DW_2(0) = 0, is used; |W_2| <= C r log(2 + r) for gamma = 1 and |W_2| <= C r^gamma for
1 < gamma < 2. Every C^1 velocity field with the same divergence and curl, W(0) = 0 and W = o(|X|^2) is W_2 + MX with
M symmetric and traceless: the strain at 0 is not fixed by the Poisson equation. For a profile the jet forces
M = diag(1/2 - c_l, c_l - 1/2), so DV(0) is the same as in S, and V = AX + W_2 with the constant matrix
A = diag(1/2, 2c_l - 1/2). This matrix A is not the angular far-field function A(th) of the class S, and the strain M
in the first-order condition of Proposition 2.8(d) below is a different constant matrix, the coefficient of the linear
term in the expansion of W_2 at infinity. These bounds do not give the sublinear velocity used in
Theorem A. Under the separate hypothesis W_2 = o(r), orbit growth and density growth give the necessary condition
c_l >= 1/4 + 1/(2 gamma). This does not exclude c_l <= 1 and proves no existence. Under the same hypothesis, an x-even
profile must have a zero of V other than 0 (Proposition 2.3), and every locally uniform subsequential limit of
R^(-gamma) rho(RZ) is layered:
    a_+ y_+^(1/beta) + a_- (-y)_+^(1/beta),   beta = 2c_l - 1/2
(Proposition 2.4); the coefficients may both vanish. For Proposition 2.5, assume in addition that every zero of V is
nondegenerate and |W_2| <= C(1 + r)^(1 - delta) for some delta > 0. Put nu = min(beta - 1/2, beta delta). Under these
assumptions no x-even profile exists if beta gamma < 1 + nu, or if |D^2 rho| <= C(1 + r)^(gamma - 2) and
beta gamma < 1 + 2 nu. With bounded W_2 and this Hessian bound the latter inequality holds for every gamma in [1, 2)
and every c_l >= 1/4 + 1/(2 gamma); this application of Proposition 2.5 still assumes nondegenerate zeros and
x-evenness. Without any symmetry assumption and whatever the zeros of V, if
|W_2| <= C(1 + r)^(1 - delta) with 0 < delta <= 1, |D^2 rho| <= C(1 + r)^(gamma - 2) and
gamma < min(2 delta + (1 - delta)/beta, 3 delta + 2/beta - 1), which holds for every gamma in [1, 2) when
W_2 is bounded, then no density in these classes is a profile, and the same holds without the Hessian bound if the
condition on gamma is replaced by beta gamma < 1 + min(beta - 1/2, beta delta) and beta > 1 - delta/2, for example for
gamma = 1 and bounded W_2, or, with the Hessian bound, by gamma < 1/beta + 1 + delta, gamma < 2/beta - 1 + 3 delta and
beta > 1 - delta/2 (Proposition 2.6(d), (e)). These extra hypotheses (W_2 = o(r), the power bound, the Hessian bound)
are not derived from the class bounds, so whether these classes contain global C^3 profiles with the jet is not
decided here; they contain no profile of the form rho = f(x) or rho = f(x) + h(y) (velocity W_2 + MX). For
1 < gamma < 2 the class bounds alone do not imply W_2 = o(r) (Proposition 2.7(e)). Without it, the locally uniform
limits of R^(-gamma) rho(RZ) for a profile solve a stationary equation with solutions that are not functions of y
alone, and they are all functions of y alone exactly when W_2 = o(r^gamma) (Proposition 2.7). Without W_2 = o(r), no
profile is even in y or satisfies rho(-X) = rho(X); the nonzero homogeneous stationary functions are the
a_+ (e.X)_+^gamma + a_- (-e.X)_+^gamma, e a unit vector, and, for each of the two horizontal directions, a family
vanishing only in that direction and parametrized up to amplitude by an open disk, whose only members with a locally
Lipschitz gradient on the punctured plane are the a(r + sigma x)^gamma; every homogeneous limit at infinity of a
profile with the Hessian bound is 0 or an a(r + sigma x)^gamma, and for a profile even in x, every homogeneous limit
at infinity is a|x|^gamma or a function of y alone, and is 0 if the profile satisfies the Hessian bound; under the
Hessian bound no nonzero function of y alone is a limit at infinity of a density, so that rho = o(r^gamma) exactly
when W_2 = o(r^gamma); for a profile, a remainder O(r^q), q < 1, about a homogeneous limit f gives the first-order
condition ((A + M)X).grad f = f with a constant traceless strain M, whose consequence for |x|^gamma is met by a
density that is not a profile; and, also without the Hessian bound, such a remainder is impossible for a profile if f
is a member of one of the two families vanishing only in a horizontal direction, in particular if
f = a(r + sigma x)^gamma with a != 0, the proof using that the two positive sectors of rho at 0 lie in different
components of {rho > 0} when l > 1/2 and the flow is complete; for a limit F(e.X) != 0 with such a remainder and
q(2l - 1/gamma) < 1, the same argument shows that it takes positive values, and positive values on both sides of the
line e.X = 0 if also l > 1/2, while for l > 5/12 an area comparison between the quadratic zero of rho at 0 and the
growth gamma < 2 shows that it vanishes on a half-plane, and for 1/4 < l <= 1/2 a second area comparison, at zeros of
rho at which grad rho vanishes, shows that it does not vanish on a half-plane; so for l > 5/12 no such limit exists,
also without the Hessian bound. For 1/4 < l <= 5/12 such a limit also takes negative values, by an area comparison
along the flow at such zeros and a growth bound from the basin of 0 of the backward flow, and so it does at l = 1/4,
by an area comparison along long flow tubes and the absence of closed level curves around zeros of rho; at l = 1/4 no
such limit exists, since, by an identity special to div V = 1/2, inside a region bounded by an arc in {rho > 0} and a
segment through 0 the zeros of rho with nonzero Hessian form curves of zeros of V, and the one starting at 0 would be
a compact curve with a single end point; for 1/6 <= l <= 1/4 it does not vanish on a half-plane, by a third area
comparison next to a region where rho vanishes, and for a C^m profile, m >= 3, this holds for 1/(2m) <= l <= 1/4. For
such a profile and 1/4 + 1/(2m) <= l <= 5/12, the minimum in x of rho near 0 leaves only l = 1/4 + 1/(2n) with n
odd; for every profile and 1/4 < l <= 5/12 such a limit needs gamma <= 1/(2l), since otherwise the forward orbit of a
zero of rho far out in the direction e-perp would be unbounded, while the gradient of rho transported along the
forward orbit of a zero at which V does not vanish keeps that orbit bounded; and for a C^infinity profile and
0 < l < 1/4 such a limit takes positive values on both sides of the line
e.X = 0, since otherwise, inside a region bounded by an arc in {rho > 0} and a segment through 0, the zeros of rho at
which V does not vanish would form finitely many orbits, each with two ends at zeros of V, while every zero of V there
other than 0 would be an end an even number of times and 0 exactly once; this uses an area comparison along long flow
tubes, smooth normal forms at the zeros of V, and, at the zeros of V there at which DV is singular, area-preserving
coordinates in which the flow carries the curves of fastest expansion to one another: in them the density equation and
the bound on the order of vanishing of rho along its zero orbits make such zeros form arcs of zeros of V; by
compactness these arcs would lie on closed curves of zeros of V, and the flow would map the region inside such a curve
onto itself while multiplying its area by e^(2lt); for 3/16 < l < 1/4 the same holds for a C^m profile
with (m - 1)(2l - 1/4) >= 1, since an expansion along the strong unstable curve shows that a zero of V there at which
D^2 rho vanishes is a source whose eigenvalues allow a C^(m - 1) linearization in place of the normal forms
(Proposition 2.8). For gamma in
[n, n + 1), n >= 2, far-field Taylor subtraction of the kernel through degree n (with a cutoff vanishing near the
origin) gives, among centered velocities (W(0) = 0) with W = o(|X|^(n+1)), a harmonic stream-polynomial ambiguity of
degrees 2, ..., n + 1. In a suitable such gauge (relative to the radially truncated integral, a harmonic cubic and a
harmonic quadratic are added to the stream function), growth 2 contains rho = x^2, psi = -x^3/3 + (c_l - 1/2) x y for
every real c_l. The statements above on the subtracted laws, the gauges, the orbit bound c_l >= 1/4 + 1/(2 gamma), the
forms f(x) and f(x) + h(y) and the polynomial solution have complete proofs in Section 9.14. The further conclusions
of Propositions 2.3-2.6 have complete proofs in Sections 9.20-9.23, those of Proposition 2.7 in Section 9.27 and those
of Proposition 2.8 in Section 9.28. No result selecting or excluding the added strain by matching to an outer flow is
proved here. Proposition 2.1 treats the different question of which velocities arise from truncating the density.
Proposition 2.1 (truncation limits: which velocities the density selects). For a bounded measurable function g with
compact support let U[g] = grad-perp d_x(N * g), N(Z) = -(1/(2 pi)) log|Z|, be the velocity of the compactly supported
density g (derivatives in distributions). If D is a bounded measurable set containing a disk B(0, r) and rho is C^3
with the jet, then U[rho 1_D] is C^2 on B(0, r) (Section 9.17, Step 1), and the centered truncated velocity
W_D := U[rho 1_D] - U[rho 1_D](0) is defined there. In each part D_R is a family of bounded measurable sets, L >= 1 is
fixed, and the limits are uniform on |X| <= L together with the first two derivatives.
(a) Class S. Let rho be in S with growth exponent gamma < 1 and let D_R contain B(0, R). Then for |X| <= L <= R/2
    W_{D_R}(X) - W(X) = -int_{R^2 \ D_R} [K(X - Y) - K(-Y)] rho(Y) dY,   |W_{D_R}(X) - W(X)| <= C L R^(gamma - 1),
so every such exhaustion, whatever the shape of D_R, gives the canonical velocity W of this section.
(b) Growth gamma in [1, 2). Let rho be C^3 with the jet and the growth bounds above for some gamma in [1, 2), and let
D_R contain B(0, R). Then M_R := DW_{D_R}(0) is symmetric and traceless, and |W_{D_R}(X) - M_R X - W_2(X)| <= C L^2
R^(gamma - 2) for |X| <= L <= R/2. So the centered fields converge if and only if M_R converges, and the limit is then
W_2 + MX with M = lim M_R. In general the density does not determine the limiting strain: for rho_gamma = x^2
(1 + r^2)^((gamma - 2)/2), which satisfies these hypotheses, every symmetric traceless M is the limit of M_R along a
family of star-shaped domains D_R containing B(0, R), and along some such families M_R has no limit (for a density
with compact support, by contrast, all such families give the same limit).
(c) Growth two, rho = x^2. Let rho_0 and delta be bounded measurable functions on the circle with rho_0 >= m > 0, and
let D_R = {s e_phi : 0 <= s < R rho_0(phi) + delta(phi)}, e_phi = (cos phi, sin phi). Write vectors (u_1, u_2) as
complex numbers u_1 + i u_2, X = x + iy, Xbar = x - iy, and put (integrals over [0, 2 pi])
    G = int cos^2 phi e^{3i phi} rho_0 dphi,   I = int cos^2 phi e^{3i phi} delta dphi,
    J = int cos^2 phi e^{4i phi} log rho_0 dphi.
Then for R >= 4L/m + 2 sup|delta|/m and |X| <= L
    W_{D_R}(X) = W_circ(X) + (i/pi)(R G + I) Xbar + (3i/(2 pi))(J + E_R) Xbar^2 + F_R(X),
with |E_R| <= 4 pi sup|delta|/(m R), |F_R| <= 20 L^3/(m R) and W_circ = (xy/4, -(7x^2 + y^2)/8), the field of the
disks (Section 9.14, Step 11). If G != 0 the strain diverges and there is no limit. If G = 0 the limit is
    W_{rho_0, delta} := W_circ + (i/pi) I Xbar + (3i/(2 pi)) J Xbar^2.
Here c Xbar is the strain field [[Re c, Im c], [Im c, -Re c]] X, and c Xbar^2 is the velocity of the harmonic cubic
stream function Re(beta X^3) with c = 3i betabar. Every strain and every harmonic cubic occurs: rho_0 = exp(a
cos 4phi + b sin 4phi) gives G = 0 and J = (pi/2)(a + ib), and delta = alpha_1 cos phi + alpha_2 sin phi gives
I = (pi/4)(alpha_1 + i alpha_2). The density x^2 solves the profile equations with velocity W_{rho_0, delta} and
parameter c_l if and only if J = -pi/12 and I = i pi (c_l - 1/2), and then W_{rho_0, delta} = ((1/2 - c_l) x,
(c_l - 1/2) y - x^2) is the polynomial solution stated above (stream function -x^3/3 + (c_l - 1/2) xy); an example is
rho_0 = exp(-cos(4 phi)/6), delta = 4(c_l - 1/2) sin phi. Centered disks (rho_0 = 1, delta = 0) give J = 0 and the
limit W_circ, with which x^2 does not solve the profile equations. Centered ellipses x^2/A^2 + y^2/B^2 < R^2 give
G = I = 0 and J = (pi/12)((1 - mu)^3 - 1), where mu in (-1, 1) is defined by (B^2 - A^2)/(B^2 + A^2) = 2
mu/(1 + mu^2); for fixed A and B, J is never -pi/12, and the same holds for every rotated copy, so the homothetic
copies of a fixed centered ellipse give the polynomial solution for no c_l. As B/A -> infinity (vertical strips) the
limit fields tend to (0, -x^2), the velocity of the formal solution rho = x^2, psi = -x^3/3 mentioned above (the case
c_l = 1/2), and the centered ellipses with semi-axes R and B_R, B_R/R -> infinity, give (0, -x^2) directly. If bounded
measurable sets D_R containing B(0, R) are all symmetric under y -> -y and their centered fields converge pointwise to
a velocity with which x^2 solves the profile equations with parameter c_l, then c_l = 1/2. Consequently, for rho in S,
every family of bounded measurable sets D_R containing B(0, R) gives the canonical velocity W: in S the velocity is
determined by the density. For growth in [1, 2) every such family gives W_2 up to the strain, and in general the
limiting strain depends on the family (the example rho_gamma). For rho = x^2, every strain and every homogeneous
harmonic cubic correction to W_circ is realized, independently, by the truncations of (c), and within (c) the
polynomial solution with parameter c_l is the limit exactly when G = 0, J = -pi/12 and I = i pi (c_l - 1/2). It is the
limit for no family of disks, centered or not (Section 9.17, Step 6), and for no homothetic copies of a fixed centered
ellipse; it is the limit for the centered ellipses with semi-axes R and B_R, B_R/R -> infinity, when c_l = 1/2; and
when c_l != 1/2 it is the limit for no family of domains symmetric under y -> -y. So the polynomial solution is a
possible truncation limit, but for rho = x^2 the limit velocity depends on the truncation and is not determined by the
density alone. In this sense the polynomial velocity is a truncation
(gauge) artifact, not a velocity selected by the density; no selection or exclusion of it by matching to an outer flow
is proved. Complete proof: Section 9.17.

Proposition 2.2 (polynomial solutions with the jet). Let l be real and let rho and psi be real polynomials with
    -Lap psi = rho_x,   (lX + grad-perp psi).grad rho = rho,   rho = x^2 + O(|X|^3),   psi = O(|X|^2)
(both remainders are as X -> 0; thus W(0) = 0). No quadratic jet of psi is assumed. If deg rho <= 3, then rho = x^2
and psi = -x^3/3 + (l - 1/2)xy.
Write NR for the condition that l > 1/4 and 2l - 1/2 is not in {1/n : n an integer, n >= 3}. Under NR the same
conclusion holds if deg rho <= 7; in particular, through density degree seven it holds for every l > 5/12, hence for
every l > 1. Under NR, if x^2 divides rho, then rho is even and psi is odd in x, the same conclusion holds if
deg rho <= 11, and if rho != x^2, then rho has an irreducible factor over C other than x, of degree at least two and
of multiplicity at least three. For l > 1/4 (NR is not needed here) no solution has a density rho = x^2 (by + g(x))^k
with b real and nonzero, g a real polynomial with g(0) = 1 and k a positive integer. For l > 1/4 the excluded values
l = 1/4 + 1/(2n), n >= 3, are exactly those at which the linear transport operator of the jet,
D_k(x^i y^j) = (i/2 + (2l - 1/2)j - 1) x^i y^j on homogeneous polynomials of degree k >= 3, has a nonzero kernel. For
every l the degrees N = deg rho and M = deg psi satisfy N >= 2 and 3 <= M <= N + 1; if M = N + 1, the top parts are
rho_N = mu (e.X)^N and psi_{N+1} = lambda (e.X)^(N+1) with |e| = 1, e_1 != 0, mu lambda != 0 and
lambda(N + 1) = -mu e_1, and if M <= N they are rho_N = mu y^N and psi_M = lambda y^M. Uniqueness in density degree
eight or more is not proved in general. Under NR, the additional assumption that x^2 divides rho gives uniqueness
through degree eleven. For l > 1, Proposition 3.15b covers every degree in y and in psi when the density has degree at
most three in x.
Complete proof: Section 9.19.

Proposition 2.3 (sublinear W_2 in the growth classes: the zero set and x-even profiles). Let 1 <= gamma < 2, let rho
be C^3 with the jet and the bounds of S with this gamma, and let V = lX + W_2 + MX with M = diag(1/2 - l, l - 1/2)
(the velocity law of these classes, Section 9.14, Step 6), so that V = AX + W_2 with A = diag(1/2, beta),
beta = 2l - 1/2. Suppose that V.grad rho = rho and that W_2(X) = o(|X|) as |X| -> infinity, uniformly in direction.
Then beta >= 1/gamma > 1/2, the flow Phi_s of V is complete, rho(Phi_s X) = e^s rho(X), and:
(a) every forward orbit that escapes to infinity has a limiting direction lim X/|X| equal to one of +-e_1, +-e_2; rho
vanishes on every orbit with limiting direction +-e_1; along an orbit with rho != 0 the direction tends to +-e_2 and
log|rho| / log|X| -> 1/beta; and for each of e_1 and -e_1 there is an orbit with that limiting direction;
(b) if V vanishes only at 0, then rho = xi^2 with xi in C^2, xi = x + O(|X|^2) at 0, V.grad xi = xi/2 and grad xi
nowhere zero; the zero set of rho is a properly embedded C^2 line through 0, tangent to the y-axis at 0, formed by 0
and the two orbits that leave 0 tangentially to the y-axis, and these two orbits have the limiting directions e_1 and
-e_1 respectively; every orbit other than these two and 0 has rho > 0 and limiting direction e_2 or -e_2;
(c) if rho is even in x, then V vanishes at some point other than 0. In particular no x-even profile in these classes
with W_2 = o(r) has 0 as the only zero of V. Whether the classes contain any profile, x-even or not, is not decided;
(c) leaves x-even profiles with further zeros of V open (Proposition 2.5(c)-(e) and Proposition 2.6(d), (e) exclude
them under further hypotheses); (c) does not apply to densities that are not x-even, and Proposition 2.6(c) excludes
the configuration of (b) for them under further hypotheses.
Complete proof: Section 9.20.

Proposition 2.4 (sublinear W_2 in the growth classes: the far field). Assume the hypotheses of Proposition 2.3 and put
p = 1/beta (not the exponent 1/c_l of Section 1), so that p <= gamma.
(a) The rescaled densities f_R(Z) = R^(-gamma) rho(RZ), R >= 1, are precompact for locally uniform convergence on the
plane, and every limit along a sequence R -> infinity has the layered form
    f(x, y) = a_+ y^p (y > 0),   f(x, y) = a_- (-y)^p (y < 0),   f(x, 0) = 0,
with constants a_+, a_- depending on the sequence. If beta gamma > 1, then rho(X) = o(|X|^gamma) as |X| -> infinity,
uniformly in direction. If, for some g >= 1, R^(-g) rho(RZ) converges locally uniformly on the plane minus 0 to a
nonzero function homogeneous of degree g, then g = 1/beta, the limit has the layered form above with p = g, and
1/2 < l <= 3/4.
(b) Suppose moreover |W_2(X)| <= C(1 + |X|)^(1 - delta) for some delta > 0. Then every forward orbit that escapes to
infinity satisfies |Phi_s X| = c_X e^(s/2) (1 + o(1)) if its limiting direction is +-e_1 and
|Phi_s X| = c_X e^(beta s) (1 + o(1)) if it is +-e_2, with c_X > 0, and along every orbit with rho != 0
    rho(Phi_s X) / |Phi_s X|^p -> rho(X) c_X^(-p) != 0   (s -> infinity).
If in addition beta gamma = 1, there are constants a_+, a_-, not both zero, such that uniformly in th
    rho(r cos th, r sin th) = r^gamma [a_+ (sin th)_+^gamma + a_- (-sin th)_+^gamma] + o(r^gamma)   (r -> infinity),
where t_+ = max(t, 0); if rho >= 0, then a_+ >= 0 and a_- >= 0.
(c) Under the hypotheses of (b) with beta gamma = 1, suppose also |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2). Then
gamma = 1 (so l = 3/4) and rho takes negative values. In particular, under these hypotheses there is no profile with
1 < gamma < 2, and none with rho >= 0 (as in Proposition 2.3(b), where V vanishes only at 0) for gamma = 1. The extra
hypotheses (W_2 = o(r), its power-decay version in (b), the Hessian bound in (c)) are not derived here from C^3
regularity and the growth bounds, so these are necessary conditions on profiles satisfying them, not nonexistence
results for the growth classes; by Proposition 2.6(d), (e), no profile satisfies the hypotheses of (c).
Complete proof: Section 9.21.

Proposition 2.5 (sublinear W_2 in the growth classes: the weak orbits and x-even profiles with nondegenerate zeros).
Assume the hypotheses of Proposition 2.3.
(a) For each of e_1 and -e_1 there is exactly one orbit with that limiting direction. For every sufficiently
large R the circle |X| = R meets each of these two orbits in exactly one point, and of the two open arcs into which
the two points divide the circle, the one containing R e_2 is the set of points of the circle whose orbits have
limiting direction e_2, and the one containing -R e_2 is the set of those with limiting direction -e_2.
(b) Suppose that every zero of V is nondegenerate (det DV != 0). Then the zeros are finitely many, the eigenvalues of
DV at each zero are real, and each zero is a source (both eigenvalues positive) or a saddle; there are no periodic
orbits and no cycles of saddle connections; every backward orbit converges to a single zero, and every nonstationary
forward orbit escapes to infinity or converges to a saddle; the plane is the disjoint union of the basins B(Z) of the
sources Z (B(Z) the set of points whose backward orbits converge to Z), which are open, and the unstable manifolds of
the saddles; and rho = 0 on the stable and unstable manifolds of every saddle.
(c) Suppose, in addition to the hypothesis of (b), that rho is even in x, that |W_2(X)| <= C(1 + |X|)^(1 - delta) for
some delta > 0 (as in Proposition 2.4(b)) and that beta gamma = 1 (so 1/2 < l <= 3/4). Then these hypotheses are
contradictory: no profile satisfies them.
(d) Part (c) remains true when beta gamma = 1 is replaced by beta gamma < 1 + nu, where
nu = min(beta - 1/2, beta delta).
(e) Part (c) also remains true when beta gamma = 1 is replaced by beta gamma < 1 + 2 nu (nu as in (d)) together with
the Hessian bound |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2) of Proposition 2.4(c). Since beta >= 1/gamma
(Proposition 2.3) and gamma < 2, for given gamma and delta the values of beta allowed in (d), and those allowed in
(e), form an interval [1/gamma, b) with b > 1/gamma. In (d), b = infinity for gamma = 1 and bounded W_2 (delta = 1),
so (d) covers every l >= 3/4, which is the whole range that Proposition 2.3 leaves for gamma = 1. In (e), b = infinity
whenever delta >= gamma/2, in particular for bounded W_2, so (e) covers every gamma in [1, 2) and every l allowed by
Proposition 2.3. Parts (c)-(e) extend Proposition 2.3(c), which excludes x-even profiles whose velocity vanishes only
at 0 and needs neither the power bound nor a condition on beta gamma, to x-even profiles whose zeros of V are all
nondegenerate, whatever their number and position, at the price of the power bound and a condition on beta gamma
(and, in (e), the Hessian bound). The extra hypotheses W_2 = o(r), the power bound, the condition on beta gamma, the
Hessian bound and nondegenerate zeros are not derived here from C^3 regularity and the growth bounds. Parts (c)-(e)
make no exclusion claim for x-even densities with W_2 = o(r) that satisfy none of their sets of hypotheses; other
results of the report, such as Propositions 2.3(c) and 2.4(c), apply to such densities under their own hypotheses.
Complete proof: Section 9.22.

Proposition 2.6 (sublinear W_2 in the growth classes: amplitude rigidity and exclusion without symmetry). Assume the
hypotheses of Proposition 2.3, put p = 1/beta as in Proposition 2.4, and suppose that, for some delta in (0, 1],
|W_2(X)| <= C(1 + |X|)^(1 - delta) (a bound with delta > 1 implies the bound with delta = 1). Put q = 1 - delta and
Q = max(p/2, q), and call |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2) (as in Proposition 2.4(c)) the Hessian bound.
(a) Under the Hessian bound, |DW_2(X)| + |d_x rho(X)| <= C(1 + |X|)^kappa with kappa = (gamma - 1 - delta)/2.
(b) Suppose that V vanishes only at 0. Then for every X the limit Y(X) = lim e^(-beta s) [Phi_s X]_2 (s -> infinity)
exists; Y is continuous, |Y(X) - y| <= C(1 + |X|)^q, Y vanishes exactly on the zero set of rho, and Y is positive on
the orbits with limiting direction e_2 and negative on those with limiting direction -e_2. If moreover
p > Q + gamma - 1, or the Hessian bound holds and p > Q + kappa, then, for some constants A_+ > 0 and A_- > 0,
    rho(X) = A_+ Y(X)_+^p + A_- (-Y(X))_+^p   for every X,
where t_+ = max(t, 0): all orbits with limiting direction e_2 carry one amplitude A_+, and all those with -e_2 one
amplitude A_-. The condition p > Q + gamma - 1 is equivalent to beta gamma < 1 + min(beta - 1/2, beta delta), the
condition of Proposition 2.5(d), and p > Q + kappa is equivalent to gamma < p + 1 + delta together with
gamma < 2p - 1 + 3 delta.
(c) Under the Hessian bound, if
    gamma < min(2 delta + (1 - delta) p, 3 delta + 2p - 1),
then V vanishes at some point other than 0. This condition holds for every beta allowed by Proposition 2.3 when
delta >= (gamma + 1)/3, in particular when W_2 is bounded, and for every delta in (0, 1] when beta gamma = 1.
(d) Assume the Hessian bound and the condition on gamma in (c), but not that V vanishes only at 0. Then the limit Y(X)
in (b) still exists for every X, with |Y(X) - y| <= C(1 + |X|)^q, and: if beta != 1, these hypotheses are
contradictory (no profile satisfies them); if beta = 1 (that is, l = 3/4), then rho = A Y on the plane for some
constant A != 0, so that |rho(X) - A y| <= C(1 + |X|)^q and rho takes both signs. No symmetry of rho is assumed.
(e) Without assuming that V vanishes only at 0, suppose that beta > 1 - delta/2 and that either p > Q + gamma - 1, or
the Hessian bound holds and p > Q + kappa. Then these hypotheses are contradictory (no profile satisfies them). The
hypotheses of (d) are contradictory as well: for beta != 1 by (d), and for beta = 1 by (e), since the condition on
gamma in (c) implies p > Q + kappa. In particular, with bounded W_2 no profile satisfies the Hessian bound, for any
gamma in [1, 2), and no profile satisfies beta gamma < beta + 1/2, a condition that holds for every beta when
gamma = 1.
Part (b) gives amplitude rigidity, not an exclusion by itself. Part (c) extends the exclusion in Proposition 2.3(c) of
x-even densities whose velocity vanishes only at 0 to densities without symmetry, at the price of the power bound, the
Hessian bound and the condition on gamma; for beta gamma = 1 it also follows from Proposition 2.4(c), since
rho = xi^2 >= 0 when V vanishes only at 0. Part (d) contains (c): for beta = 1 it gives negative values of rho, while
rho = xi^2 when V vanishes only at 0. Parts (d) and (e) need no assumption on the zeros of V and no symmetry. The
proof of (e) compares areas: near 0 the backward flow, transport and the jet give rho = u^2 with a C^1 coordinate u,
and a band {|u| < c e^(-T/2)} near 0, of area of order e^(-T/2), is carried by Phi_T, which multiplies areas by
e^((1/2 + beta) T), into a part of the strip {|Y| <= C} of area O(e^((1 - delta/2) T)). Thus no profile in the growth
classes satisfies the power bound, the Hessian bound and the condition on gamma, which holds for every gamma in [1, 2)
when W_2 is bounded, with or without symmetry and whatever the zeros of V. By (e), no profile with beta > 1 - delta/2
satisfies the power bound together with either beta gamma < 1 + min(beta - 1/2, beta delta), or the Hessian bound,
gamma < p + 1 + delta and gamma < 2p - 1 + 3 delta. The extra hypotheses, namely W_2 = o(r), the power bound and,
where it is used, the Hessian bound, are not derived here from C^3 regularity and the growth bounds; (d) and (e)
exclude only profiles that satisfy them together with the stated conditions on gamma and beta, and whether the growth
classes contain other profiles is not decided. Complete proof: Section 9.23.

Proposition 2.7 (growth 1 < gamma < 2 without W_2 = o(r): the limits at infinity). Let 1 < gamma < 2. For C > 0 let
E_gamma(C) be the set of locally Lipschitz functions g on the plane with |g(X)| <= C|X|^gamma and
|grad g(X)| <= C|X|^(gamma - 1) for almost every X, and for g in E_gamma(C) define W_2[g] by the formula for W_2 in
Section 9.14, Step 3, with g in place of rho.
(a) The integral defining W_2[g] converges at every X (circular principal value at Y = X), W_2[g] is continuous,
|W_2[g](X)| <= C_gamma C |X|^gamma with C_gamma depending only on gamma, div W_2[g] = 0 and curl W_2[g] = -d_x g in
distributions, and W_2[g] vanishes at 0 and is differentiable there with derivative 0. It is the only continuous field
with this divergence and curl, growth O(|X|^gamma), value 0 at 0 and derivative 0 at 0. For t > 0,
W_2[t^(-gamma) g(t.)](X) = t^(-gamma) W_2[g](tX). If g_n and g are in E_gamma(C) and g_n -> g locally uniformly, then
W_2[g_n] -> W_2[g] locally uniformly.
(b) Let rho be C^3 with the jet and the bounds of S with this gamma, and no further hypothesis. Then rho is in
E_gamma(C_0) for some C_0, W_2[rho] is the field W_2 of this section, and the rescaled densities
f_R(Z) = R^(-gamma) rho(RZ), R >= 1, lie in E_gamma(C_0) and are precompact for locally uniform convergence. Every
limit f along a sequence R_n -> infinity, called a limit at infinity of rho, is in E_gamma(C_0), and
R_n^(-gamma) W_2(R_n Z) = W_2[f_(R_n)](Z) converges to W_2[f](Z) locally uniformly. If moreover rho is a profile with
the velocity law of these classes (V.grad rho = rho with V = AX + W_2 as in Proposition 2.3, for some real l), then
every limit at infinity, possibly 0, satisfies div(f W_2[f]) = 0 in distributions, equivalently
W_2[f].grad f = 0 almost everywhere: at this order the linear part AX drops out. No bound on W_2 beyond Section 9.14,
Step 4, no Hessian bound and no condition on l is assumed.
(c) Without the profile equation: every limit at infinity of rho is layered, that is, a function of y alone, if and
only if W_2(X) = o(|X|^gamma) as |X| -> infinity. If f in E_gamma(C) is a function of y alone, then W_2[f] = 0.
(d) The stationary equation of (b) has solutions in E_gamma(C) that are not functions of y alone. For a unit vector
e = (e_1, e_2) and real a_+, a_-, the function f(X) = F(e.X),
F(s) = a_+ s_+^gamma + a_- (-s)_+^gamma (s_+ = max(s, 0)), has W_2[f] = (e_1 e_2, -e_1^2) F(e.X), which is orthogonal
to grad f; for example f = |x|^gamma, which is nonnegative and even in x, has W_2[f] = (0, -|x|^gamma). For
sigma = 1 or -1 and real a, f = a(r + sigma x)^gamma has W_2[f] = grad-perp psi with psi = -sigma a gamma
(r + sigma x)^(gamma + 1)/((gamma + 1)(2 gamma + 1)), a function of r + sigma x, and for c > 0 the level set
{r + sigma x = c} is the parabola y^2 = c^2 - 2 sigma c x. Whether any of these solutions occurs as a limit at
infinity of a profile is not decided; the stationary equation alone does not force the layered limits of
Proposition 2.4(a).
(e) For every q with 1 < q < gamma there is a smooth density rho, nonnegative and even in x, with the jet and the
bounds of S with this gamma, whose only limit at infinity is |y|^gamma, for which |W_2(X)| <= C|X|^q and
W_2(0, -r) = -(0, r^q)/(q + 2) + o(r^q) as r -> infinity, so that W_2 = o(r^gamma) but W_2 is not o(r); for every real
l the field AX + W_2 of Proposition 2.3 has an orbit on the negative y-axis that escapes to infinity in finite time,
and rho is not a profile. Removing the layered part gives a density with the same velocity and the same conclusions on
W_2, on the orbit and on profiles, which in addition satisfies the Hessian bound
|D^2 rho(X)| <= C(1 + |X|)^(gamma - 2) and whose only limit at infinity is 0. Thus for 1 < gamma < 2 the class bounds,
also together with a unique nonzero layered limit at infinity or with the Hessian bound, do not imply W_2 = o(r), the
hypothesis of Propositions 2.3-2.6; whether the profile equation together with the class bounds implies it is not
decided.
Complete proof: Section 9.27.

Proposition 2.8 (growth 1 < gamma < 2 without W_2 = o(r): homogeneous limits, symmetry and the first order). Let
1 < gamma < 2, and let E_gamma(C), W_2[g], the limits at infinity and the velocity law V = AX + W_2,
A = diag(1/2, beta), beta = 2l - 1/2, be as in Proposition 2.7. A function g in some E_gamma(C) is called stationary
if div(g W_2[g]) = 0 in distributions, and homogeneous if g(tX) = t^gamma g(X) for all t > 0 and X. Write
k = gamma + 1 and X = r(cos th, sin th). No hypothesis W_2 = o(r), no bound on W_2 beyond Section 9.14, Step 4, and,
except in (g) and where stated in (h), no condition on l is assumed.
(a) Let rho be C^3 with the jet and the bounds of S with this gamma. Its set of limits at infinity is nonempty,
compact and connected for locally uniform convergence, and invariant under the dilations g -> t^(-gamma) g(t.), t > 0.
If it has only one element f, then R^(-gamma) rho(RZ) -> f locally uniformly as R -> infinity, and f is homogeneous.
(b) The homogeneous elements of the classes E_gamma(C) are the functions f = r^gamma P(th) with P Lipschitz and
2 pi-periodic. For such f, W_2[f] = grad-perp(r^k Q(th)), where Q is the unique 2 pi-periodic solution of
    Q'' + k^2 Q = -gamma cos(th) P + sin(th) P',
and f is stationary if and only if k Q P' = gamma Q' P almost everywhere, equivalently if and only if on each
component I of {P != 0} one has Q = c_I |P|^(k/gamma) for a constant c_I. Let f != 0 be homogeneous and stationary.
Then P has a zero, and exactly one of the following holds.
(i) f = F(e.X) for a unit vector e, with F as in Proposition 2.7(d).
(ii) P vanishes in exactly one direction, which is e_1 or -e_1, and has one sign elsewhere. Let I be the open arc of
length 2 pi on which P != 0, eps = sign P on I, s = eps sign(c_I) and v = (k |c_I|/gamma) |P|^(1/gamma). Then
c_I != 0, v is smooth and positive on I, v and v' tend to 0 at both ends of I, and on I
    v v'' + gamma v'^2 + k v^2 = s(v' sin(th) - v cos(th)),   gamma(v'^2 + v^2) + s(v cos(th) - v' sin(th)) < 0.
In kind (ii) with zero direction e_1 one has s = 1, and the functions v that occur are exactly the solutions of the
first equation in (ii) with s = 1 and data (v(pi), v'(pi)) in the open disk D_gamma = {(a, b) : gamma(a^2 + b^2) < a}:
for every (a, b) in D_gamma this solution is positive on (0, 2 pi), v and v' tend to 0 at 0 and 2 pi, and
f = a_0 (r v(th))^gamma for 0 < th < 2 pi, f = 0 on the ray th = 0, is homogeneous, in some E_gamma(C), and stationary
of kind (ii) for every a_0 != 0; distinct data give distinct v. The functions of kind (ii) with zero direction -e_1
are the f(-X) with f of kind (ii) with zero direction e_1; passing from f to f(-X) replaces v by v(th + pi) and s by
-s. The data (2/(2 gamma + 1), 0) give v = (1 - cos th)/(2 gamma + 1) and the solutions a(r - x)^gamma of
Proposition 2.7(d); the data (1/(2 gamma), 0) give solutions of kind (ii) that are not of the form
a(r + sigma x)^gamma, and data (a, 0) give solutions even in y. Consequently {P != 0} has at most two components, and
the set of zero directions of f is a pair of opposite directions, a closed half-circle, or a single horizontal
direction. If f is even in x, then f = a|x|^gamma or f = a_+ y_+^gamma + a_- (-y)_+^gamma with real a, a_+, a_-
(both stationary by Proposition 2.7(d)), and f >= 0 exactly when these amplitudes are >= 0.
(c) Let rho be a profile with this velocity law, even in x. Every homogeneous limit at infinity of rho is a|x|^gamma
or a_+ y_+^gamma + a_- (-y)_+^gamma (possibly 0). If rho has only one limit at infinity f and at least one of f(0, 1),
f(0, -1) is nonzero, then f is a function of y alone and W_2 = o(r^gamma). Independently of the profile equation and
of symmetry: if a density rho as in (a) satisfies the Hessian bound |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2), then each
of its limits at infinity is C^1 on the punctured plane with locally Lipschitz gradient there, no nonzero F(e.X)
as in (b)(i) and no nonzero function of y alone is a limit at infinity, and W_2 = o(r^gamma) holds if and only if
rho = o(r^gamma). The functions a(r + sigma x)^gamma, sigma = 1 or -1, are C^2 on the punctured plane; for every other
function f of kind (ii), (v^gamma)'' is unbounded near each end of I, with v as in (b)(ii), and grad f is not
Lipschitz on any neighborhood of a point of the zero ray of f. Since the limits at infinity of a profile are
stationary (Proposition 2.7(b)), every homogeneous limit at infinity of a profile with the Hessian bound is therefore
0 or of the form a(r + sigma x)^gamma with a != 0, and an x-even profile with the Hessian bound has no nonzero
homogeneous limit at infinity; if it has only one limit at infinity, then rho = o(r^gamma) and W_2 = o(r^gamma); this
does not give W_2 = o(r).
(d) Let rho be as in (a), let f be homogeneous and in some E_gamma(C), and suppose that h = rho - f satisfies
|h(X)| <= C(1 + |X|)^q for some 0 <= q < 1. Then f is the only limit at infinity of rho, the integral
M = -int DK(-Y) h(Y) dY, with DK(-Y) as in Section 9.14, Step 4, converges absolutely, M is symmetric and traceless,
and
    W_2(X) = W_2[f](X) + MX + O((1 + |X|)^q log(2 + |X|)).
If rho is a profile with this velocity law, then f is stationary and ((A + M)X).grad f = f in distributions.
Consequently: if f = F(e.X) != 0, then (A + M)e = e/gamma, so that for f = a|x|^gamma, a != 0, M_11 = 1/gamma - 1/2
and M_12 = 0; if f is of kind (ii), then A + M = I/gamma and l = 1/gamma; if M = 0, then f is a function of y alone
(possibly 0), W_2 = o(r), and if moreover f != 0, then beta gamma = 1.
(e) The necessary condition of (d) for the limit |x|^gamma is met by a density that is not a profile. Let
alpha = 1/gamma - 1/2 and f_gamma(x) = x^2 (1 + x^2)^((gamma - 2)/2). There is a smooth density rho_*, nonnegative and
even in x, with the jet and the bounds of S with this gamma, such that rho_* - |x|^gamma is bounded
(so (d) applies with f = |x|^gamma and q = 0), M = diag(alpha, -alpha), and
    W_2[rho_*](X) = (alpha x + O(r^(-2)), -alpha y - f_gamma(x) + O(1))   as r -> infinity.
For every real l the field V = AX + W_2[rho_*] has a complete flow, and V.grad rho_* - rho_* is bounded on the plane
and not identically 0, so rho_* is not a profile. Thus the normalization W_2(0) = 0, DW_2(0) = 0, nonnegativity,
evenness in x, a unique limit at infinity with a bounded remainder and the condition of (d) do not, together, remove
the far-field strain M_11 = 1/gamma - 1/2.
(f) No profile with this velocity law is even in y, and no such profile satisfies rho(-X) = rho(X). No limit at
infinity, sign condition or bound on W_2 is assumed; the jet is compatible with both symmetries.
(g) Let rho be a profile with this velocity law and l > 1/2, and suppose that the flow of V is complete. Then there is
delta_0 > 0 such that for 0 < delta < delta_0 the points (-delta, 0) and (delta, 0) lie in different connected
components of the open set {rho > 0}. No symmetry, limit at infinity or further bound on W_2 is assumed.
(h) Let rho be a profile with this velocity law, and let f, h and q be as in (d). Then f is not of kind (ii); in
particular, rho - a(r + sigma x)^gamma is not O((1 + r)^q) for any a != 0, sigma = 1 or -1 and q < 1. Consequently
f = 0 or f = F(e.X) != 0 with (A + M)e = e/gamma as in (d), and if rho also satisfies the Hessian bound of (c), then
f = 0, so that |rho(X)| <= C(1 + |X|)^q. Let f = F(e.X) != 0 with F(s) = a_+ s_+^gamma + a_- (-s)_+^gamma as
in Proposition 2.7(d), and suppose that q(2l - 1/gamma) < 1 (for every 0 <= q < 1 this holds if l <= (1 + 1/gamma)/2).
Then l != 1/4, and a_+ > 0 or a_- > 0; if l >= 1/6, then a_+ != 0 and a_- != 0; if l > 1/4, then a_+ a_- < 0 and
gamma <= 1/(2l); if l > 5/12, then a_+ = 0 or a_- = 0; and if l > 1/2, then a_+ > 0 and a_- > 0. If moreover rho is
C^m for an integer m >= 3, then a_+ != 0 and a_- != 0 already if l >= 1/(2m), and if 1/4 + 1/(2m) <= l <= 5/12, then
l = 1/4 + 1/(2n) for an odd integer n with 3 <= n <= m. If rho is C^infinity and 0 < l < 1/4, then a_+ > 0 and
a_- > 0. If 3/16 < l < 1/4, m is an integer with (m - 1)(2l - 1/4) >= 1 (for example m = 9) and rho is C^m, then
a_+ > 0 and a_- > 0. Consequently, for f as in (d), if l = 1/4, or if l > 5/12 and q(2l - 1/gamma) < 1, then f = 0 and
|rho(X)| <= C(1 + |X|)^q, and the same holds if rho is C^infinity, l > 1/4, q(2l - 1/gamma) < 1 and l is not
1/4 + 1/(2n) for any odd integer n >= 3. In particular, if q(2l - 1/gamma) < 1, then rho - a|x|^gamma is not
O((1 + r)^q) for any a < 0, and for any a != 0 if l >= 1/4. The Hessian bound and conditions on l are assumed only
where stated; completeness of the flow is not assumed.
Not decided: whether a profile can have a nonzero limit at infinity a|x|^gamma or of kind (ii); whether the profile
equation together with the class bounds implies W_2 = o(r^gamma) or W_2 = o(r); and whether a profile with the Hessian
bound can have a limit at infinity a(r + sigma x)^gamma with a != 0. By (h), rho - f is not O(r^q), q < 1, for f of
kind (ii), in particular for f = a(r + sigma x)^gamma with a != 0, and, if q(2l - 1/gamma) < 1, for every
f = F(e.X) != 0 if also l = 1/4 or l > 5/12, and for f = a|x|^gamma with a < 0, or with a != 0 if l >= 1/4. For
f = F(e.X) != 0 and a profile without the Hessian bound, the cases of a remainder O(r^q), q < 1, that (h) leaves open
are q(2l - 1/gamma) >= 1, which requires l > (1 + 1/gamma)/2, and the limits with a positive amplitude for l < 1/4 or
1/4 < l <= 5/12; for these, both amplitudes are nonzero if l >= 1/6, and of opposite signs, with gamma <= 1/(2l), if
l > 1/4, and for a C^m profile, m >= 3, both are nonzero if l >= 1/(2m), and if l > 1/4, then l < 1/4 + 1/(2m) or
l = 1/4 + 1/(2n) with n odd and 3 <= n <= m, and if 3/16 < l < 1/4 and (m - 1)(2l - 1/4) >= 1, both are positive, and
for a C^infinity profile with 0 < l < 1/4 both are positive. For an x-even profile without the Hessian bound,
a|x|^gamma with a != 0 is the only homogeneous limit at infinity not a function of y alone that (c) leaves.
Complete proof: Section 9.28.

## 2a. Analytic results in S (statements checked; complete proofs in Section 9)
Status of the analytic results in Sections 2a-4. Whether a complete proof is given and whether a statement carries
extra hypotheses are recorded separately: a conditional statement (one whose extra hypotheses are part of the
statement) may have a complete proof or only an outline. Complete proofs in Section 9 are given for the velocity law
of Section 2, for its growth-class statements on subtracted laws, gauges, the orbit bound, the forms f(x) and
f(x) + h(y) and the polynomial solution (Section 9.14), for
Propositions 2.1-2.8 (Sections 9.17, 9.19-9.23, 9.27 and 9.28), and for every numbered result of Sections 2a and 3:
Theorem A and Theorem B (F1), (F2), (F4), Section 9.0 (the stronger regularity statement in the parenthesis of Theorem
A: Section 9.2); Theorem B (F3) together with the coverage B(0) = R^2, Section 9.1; Theorem 3.1 with the far-field
regularity, Section 9.2; Theorem 3.16, Section 9.3; Theorems 3.2, 3.3 and 3.13, Section 9.4; Lemma 3.7, Theorem 3.8
and Proposition 3.9, Section 9.5 (the last clause of 3.8(e): Section 9.6); Proposition 3.10 and Theorem 3.11, Section
9.6; Proposition 3.15, Section 9.7; Proposition 3.15a, Section 9.16; Proposition 3.15b, Section 9.18; Theorems C, D
and 3.5 and Propositions 3.4 and 3.12, Section 9.8; Propositions 3.6 and 3.14, Section 9.9; Proposition 3.17,
Section 9.10; Proposition 3.17a, Section 9.25; and Proposition 3.18, Section 9.24. In Section 4, Section 4.16 has a
complete proof in Section 9.11, Proposition 4.13a in Section 9.12, Section 4.17 in Section 9.13, Section 4.18 in
Section 9.26, Theorem 4.9, Corollary 4.10 and Remark 4.11 in Section 9.15, and Proposition 4.7 and Corollary 4.8 in
Section 4.7 itself. Identities and explicit formulas that can be checked directly (algebra, symbolic computation) are
recognisable as such from the displayed formulas. The other structural statements of Section 4 are not proved in
Section 9; where no complete argument is printed with them
(in particular for the label-coordinate assertions of 4.6, the construction in 4.7(v), Proposition 4.12 and the
rigidity claim of 4.15(f)), only an outline ("proof idea") is given or the proof is omitted, as stated where they
occur. Checks by the independent verifier and by separate audits of an outlined argument are checks of the statement
and of the outline; they do not replace written proofs, and Section 6 records the versions that completed checks
concern. Numerical checks are not proofs. The steps that earlier versions listed here as not supplied by the outlines
(the zero set of A in Theorem 3.8(e), the passage remainders of Proposition 3.10, Theorem 3.11 and the uniqueness
statement of Proposition 3.15) now have complete proofs in Sections 9.6 and 9.7.
Theorem A and Theorem B (F1), (F2), (F4) have complete proofs in Section 9.0.
Theorem A (growth and regime). If rho in S is a nonzero profile then gamma > 0 and c_l >= 1/gamma > 1 (finite-time
focusing),
c = c_l - 1/2 > 1/2, rho = O(r^p) with p = 1/c_l, rho is not o(r^p), |W(X)| <= C|X|^p (1 + log|X|) for |X| >= 1, and
r^{-p} rho(r, th) -> A(th) uniformly, with A Holder continuous and not identically zero (by Theorem 3.1, A is in fact
C^{2,alpha} for every alpha < 1 and |r^{-p} rho - A| <= C r^{p-1}). The origin is a hyperbolic
source of V with eigenvalues 1/2 and 2c_l - 1/2 > 3/2.
Complete proof: Section 9.0, Steps 1-6 (the parenthetical statement from Theorem 3.1: Section 9.2). Outline:
rho(Phi_s X) = e^s rho(X)
along the flow of V; orbits grow at most like e^{(c_l + eps) s} for every eps > 0 because |W(X)| <= eps |X| + C_eps;
comparison of the two growth rates at a point with rho(X) != 0 gives gamma (c_l + eps) >= 1 for every eps, so a
nonzero profile is unbounded, gamma > 0 and c_l >= 1/gamma; the backward-time comparison gives the sharp bound; the
far-field limit follows from c_l r^{p+1} d_r(r^{-p} rho) = -W.grad rho and the bound on W.
Theorem B (structure). (F1) every critical point of rho is a zero of rho, rho has no nonzero local extrema, each
component of {rho != 0} is unbounded, and every zero of V is a zero of rho. (F2) X.V > 0 for |X| large; backward
orbits are bounded; there are no periodic orbits (div V = 2 c_l > 0). (F3) On the basin B(0) of the centre,
rho = xi^2 with xi = lim_{s->inf} e^{s/2} x(Phi_{-s} X) a C^2 solution of V.grad xi = xi/2; the zero set of rho in
B(0) is the strong unstable manifold Gamma of 0 (a curve tangent to the y-axis), where rho vanishes to second order.
If 0 is the only zero of V then B(0) = R^2 and rho >= 0. (F4) along either branch of Gamma minus 0, h = d_n^2 rho
obeys d/ds log(h/|V|^2) = 1 - 4 c_l. (F1), (F2) and (F4) have complete proofs in Section 9.0, Step 7 ((F2) concerns
nonstationary periodic orbits; 0 is a stationary one), and (F3), with the coverage statement, in Section 9.1.
Theorem C (moment law). For phi = r^{-3} sin 3th and Q[rho] := int rho W[rho].grad phi dX, every rho in S with the
jet (not necessarily a profile) satisfies int (V.grad rho - rho) phi dX = pi c (c - 1/2) - Q[rho], with V = (1/2 + c)
X + W[rho] (absolutely convergent). Hence a profile has Q = pi c (c - 1/2) > 0, i.e. kappa := Q/(pi
c^2) = 1 - 1/(2c) = 2(1 - p)/(2 - p). Since kappa is invariant under the jet-preserving rescaling rho -> L^2 rho(X/L),
this is a condition on the shape of rho only. Under dynamic rescaling d_s rho = rho - V.grad rho (c_l(s) = 1/2 + c(s))
one has dc/ds = c (1/2 - c) + Q/pi, but only while psi_yy(0) = 0 along the evolution (for instance for x-even data)
and under time-uniform class-S bounds; for asymmetric data the fixed jet is not preserved by the evolution. More
generally, for every C^3 density with the growth bounds of S, rho(0) = 0 and grad rho(0) = 0 (any Hessian at 0) and
every real s, int rho phi = pi c and int ((sX + W).grad rho - rho) phi dX = (s - 1) pi c - Q[rho]. Complete proof:
Section 9.8, Steps 1-2 (the evolution identity is conditional on the existence of a classical
evolution that keeps the jet). (Verified algebraically and numerically by the verifier; confirmed by a separate
audit.)
Theorem D (free orientation). For the jet (e.X)^2, e = (cos f, sin f), the second-order compatibility conditions
are c = k cos 2f, psi_yy(0) = k sin 2f, k = c_l - 1/2 (necessary and sufficient for the quadratic part of the profile
equation; not sufficient for a profile). Under X = R_f z, the density rho(R_f z), the stream function psi(R_f z) and
the velocity R_{-f} W(R_f z) satisfy the profile system with the jet z_1^2 and gravity rotated by -f, whose velocity
law is -Lap psi~ = cos f d_1 rho~ - sin f d_2 rho~. This is covariance with gravity rotated together with the density;
rotating the density alone, with the law -Lap psi = rho_x kept fixed, is not a symmetry. Setting II is f = 0.
Complete proof: Section 9.8, Step 6. (Verified; confirmed by a separate audit.)

## 3. Analytic results: structure of profiles in S (statements checked; complete proofs in Section 9)
The statements in this section were checked by the independent verifier and by a separate adversarial audit;
corrections from both are incorporated. Every result of this section has a complete proof in Sections 9.2-9.10, 9.16,
9.18, 9.24 and 9.25 (each result names its subsection); the outlines given with some statements summarise those
proofs. Throughout, except in the layered classifications of Propositions 3.15-3.15b, rho denotes a profile in S.
Write l = c_l, p = 1/l, and let Phi_s be the flow of V. S^+ := {profiles rho in S : V has no zero besides 0},
S^+_even := {rho in S^+ : rho(-x,y) = rho(x,y)}. W = (W_1, W_2) in components, so W_2 is the second component of the
canonical velocity W. In the growth-class statements of Section 2 and their proofs
(Sections 9.14, 9.17, 9.20-9.23, 9.27 and 9.28), W_2 instead denotes the twice-subtracted vector field; the summaries
in Sections 6 and 7 inherit these local meanings.

Theorem 3.1 (scattering map). Fix R with V.X >= l|X|^2/2 for |X| >= R. For each a, the forward orbit of R e_a has
r(s) = L(a) e^{ls}(1 + O(e^{-(l-1)s})) and polar angle Theta(a) + O(e^{-(l-1)s}), uniformly in a, with
0 < L < infinity.
L and Theta are C^2, Theta is an orientation-preserving circle diffeomorphism, Theta'(a) = R V_r(R e_a)/(l L(a)^2),
and A(Theta(a)) = L(a)^{-p} rho(R e_a). Moreover |r^{-p} rho(r e_th) - A(th)| <= C r^{p-1}, A is C^{2,alpha} for every
alpha < 1, and for large |X|: |grad rho| <= C|X|^{p-1}, |W| <= C|X|^p, |DW| <= C|X|^{p-1} and
|D^2 rho| + |D^2 W| <= C|X|^{p-2}. The points whose forward orbit stays in |X| < R form a closed set of measure zero
that contains 0 and is contained in {rho = 0} (this is not a statement about the whole zero set of rho). Complete
proof: Section 9.2. The C^1 statements need the bound on DW along orbits; the proof obtains it from the profile
equation (through the vorticity law V.grad omega = (1 - l) omega + d_x W.grad rho, omega = -rho_x) together with the
bounds defining S (Section 9.2, Step 2).

Theorem 3.2 (S^+). If rho in S^+, then rho = xi^2 >= 0 on R^2, the zero set is the strong unstable manifold Gamma of 0
(two components of Gamma minus 0, each a single orbit crossing every large circle once and transversally), and A has
exactly two zeros theta_1 != theta_2, each quadratic with positive coefficient: with q(a) = xi(R e_a) and
Theta(a_j) = theta_j, A''(theta_j) = 2 L(a_j)^{-p} q'(a_j)^2 / Theta'(a_j)^2 > 0; A > 0 elsewhere. The signed root
B(Theta(a)) := L(a)^{-p/2} q(a) is C^2, B^2 = A and B'(theta_j) != 0. Complete proof: Section 9.4.

Theorem 3.3 (S^+_even: the vertical wall). If rho in S^+_even, then Gamma is the y-axis, rho > 0 for x != 0,
C_1 x^2 (1 + |X|)^{p-2} <= rho <= C_2 x^2 (1 + |X|)^{p-2}, and the restriction to x > 0 is a self-similar IPM profile
in the half plane with an impermeable VERTICAL wall (parallel to gravity), centre on the wall and density vanishing
on it. With b(y) = V_2(0,y) = l y + w(y), h(y) = rho_xx(0,y) > 0:
    b h' = (1 - 4l + 2b') h,   h ~ H_+- |y|^{p-2} (y -> +-infinity),   int h w' dy = ((l - 1)/3) int h dy > 0.
The integral identity is the integrated wall equation; its content is that w' = psi_xy(0, y) is a nonlocal
functional of rho (an absolutely convergent kernel integral, Section 9.9, Step 2). A sign int h w' <= 0 would exclude
S^+_even; no derivation of that sign for every profile in this class is known (Section 4 records the test-density
calculations). Complete proof: Section 9.4 (the relative error in h ~ H_+- |y|^{p-2} is O(|y|^{p-1})).

Proposition 3.4 (flux identities). For every smooth Phi on the circle,
    int rho W.grad(r^{-2-p} Phi(th)) dX = l int A Phi dth,
and for every m in (2 + p, 4) and smooth Phi, (1 + 2l - ml) int rho r^{-m} Phi + int rho W.grad(r^{-m} Phi) = 0
(absolutely convergent; in the integration by parts the boundary terms are O(eps^{4-m}) on |X| = eps, from
rho = O(r^2), and O(R^{2+p-m}) on |X| = R, from rho = O(r^p) and |V| = O(r)). The case m = 3, Phi = sin 3th recovers
the profile consequence Q = pi c (c - 1/2) of Theorem C. In S^+: int rho W_r r^{-3-p} dX = -(l/(2 + p)) int A dth < 0.
At m = 2 + p the integrals int rho r^{-2-p} Phi and int rho X.grad(r^{-2-p} Phi) are not absolutely convergent when A
Phi is not identically 0; the first identity is the limit of the annular flux. Complete proof: Section 9.8, Step 3.

Theorem 3.5 (restricted nonexistence). Let rho in S be a profile whose far-field coefficient A has a zero beta with
A(beta) = A'(beta) = 0 < A''(beta) (every profile in S^+ has two, Theorem 3.2). Then H_p[A].grad(r^p A) (H_p[A] the
degree-p canonical velocity of r^p A) does not vanish identically on either one-sided neighbourhood of beta, and rho
does not equal r^p A(th) exactly outside any disk. Only A in C^1 (Theorem 3.1) and the existence of A''(beta) are
used. In particular no profile in S^+ equals r^p A(th) exactly outside a disk; by Proposition 3.18(c), whose proof
uses that A is C^2, no profile in S does. Complete proof: Section 9.8, Step 4.
Outline: for an exterior that is exactly r^p A the velocity there is H_p[A] plus a constant plus O(r^{-2}), so the
transport equation forces the leading balance H_p[A].grad(r^p A) = 0; this gives Psi = C A^{(p+1)/p} for the angular
stream function on each arc where A > 0, and the angular ODE Psi'' + (p+1)^2 Psi = -(p cos th A - sin th A') is
violated at a quadratic zero of A. This does not exclude profiles with corrected tails r^p A + r^{2p-1} B + ... .

Proposition 3.6 (Fourier pairing in S^+_even). Let rho in S^+_even, h as in Theorem 3.3, w' = d_y W_2(0, y), and
rho^(x, k) = int e^{-iky} rho(x, y) dy, h^(k) = int e^{-iky} h(y) dy. Then, with absolutely convergent integrals
(||rho(x, .)||_{L^1} <= C x^2 (1 + x)^{p-1} by the bound of Theorem 3.3, and |h^(k)| <= C/(1 + |k|) for real k,
because h and h' are integrable),
    ((l - 1)/3) int h dy = int h w' dy = -(1/pi) int_0^inf int_0^inf k^2 e^{-kx} Im( rho^(x, k) conj(h^(k)) ) dk dx.
Consequently no profile in S^+_even has Im(rho^(x, k) conj h^(k)) >= 0 for a.e. x, k > 0; this excludes, for
example, densities with rho(x, y_0 + t) = rho(x, y_0 - t) for all x, t and one common height y_0, and densities with
rho(x, .) = mu_x * h for almost every x > 0, mu_x real even signed measures of finite total variation (no positivity
or uniform bound in x needed). Complete proof: Section 9.9, Steps 1-4. Outline: w'(y) = -int_{x>0} rho(x, z)
K_x(y - z) dz dx with K_x = d_x d_t P_x, P_x the half-plane Poisson kernel (the contact term vanishes on the wall);
oddness of K_x turns the pairing into int_{x>0} rho d_x H with H the bounded harmonic extension of h'; Parseval. The
phase condition is a statement about the vertical offset of the interior density relative to the wall curvature h; no
derivation of it from positivity, rho_x > 0 and the two-sided bound of Theorem 3.3 is known (Section 4).

Lemma 3.7 (equilibria). Let rho in S be a profile and Z a zero of V, M = DV(Z). Then rho(Z) = 0,
M^T grad rho(Z) = grad rho(Z) and M_21 - M_12 = -rho_x(Z) (curl V = Lap psi = -rho_x). Hence, if 1 is not an
eigenvalue of M, grad rho(Z) = 0 and M is symmetric; if 1 is an eigenvalue, the other is 2l - 1. In particular V has
no focus and no defective (Jordan) node. Complete proof: Section 9.5.

Theorem 3.8 (flow topology and vanishing outside S^+). Let rho in S be a profile whose zeros of V are nondegenerate
(det DV != 0; there are then finitely many, all in a fixed disk). Then:
(a) there are no sinks, no periodic orbits and no cycles of saddle connections (div V = 2l > 0: the bounded region D
    enclosed by such a curve would be invariant with |D| = e^{2ls}|D|); every zero is a source (a node) or a saddle,
    and #sources = #saddles + 1;
(b) every backward orbit converges to a single zero, so R^2 is the disjoint union of the open source basins
    B(0), B(Z_1), ..., B(Z_m) and the unstable manifolds of the saddles; every nonstationary forward orbit escapes to
    infinity or converges to a saddle; every basin has infinite area (|B| = e^{2ls}|B| by Liouville), hence is
    unbounded;
(c) rho = 0 on the stable and unstable manifolds of every saddle;
(d) on the basin of an extra source with eigenvalues 0 < lambda_1 <= lambda_2, if lambda_1 > 1/3 and lambda_1 is not
    1/2 or 1, then rho = 0 identically on the basin (a dead basin): the density jets vanish through order 3 by the
    transport equation at Z, and rho(X) = e^s rho(Phi_{-s} X) = o(e^{(1 - 3 lambda_1)s});
(e) a saddle stable branch emanating from 0 is a branch of Gamma; if every extra source is as in (d), then
    rho = xi^2 1_{B(0)} >= 0 and the zero set of A is the image under the scattering map of finitely many points
    (escaping saddle branches and Gamma) together with finitely many closed arcs (closures of the directions of dead
    basins).
Extra sources with lambda_1 in (0, 1/3] or in {1/2, 1} are not covered by (d) and are not excluded; the range
(0, 1/3) is open, so (e) is not a genericity statement. Theorem 3.8 restricts what a profile outside S^+ must look
like; it is not a nonexistence result. Complete proof: Section 9.5 ((a)-(d) and the first two clauses of (e)) and
Section 9.6, Step 9 (the last clause of (e)).

Proposition 3.9 (source rigidity). Let Z be an extra source with eigenvalues 0 < alpha <= 1 < beta'. There is a C^2
function eta on the basin B(Z) with V.grad eta = alpha eta and D eta(Z) != 0 (the weak eigenfunction,
eta(X) = lim_{t->inf} e^{alpha t} e*.(Phi_{-t} X - Z)), and constants d_+, d_- with
    rho = d_+ |eta|^{1/alpha} on {eta > 0},   rho = d_- |eta|^{1/alpha} on {eta < 0},   rho = 0 on {eta = 0}.
If rho is not identically zero on B(Z), C^3 regularity at Z requires 1/alpha in {1, 2, 3} with d_- = (-1)^{1/alpha}
d_+, or 1/alpha > 3 (a necessary form only). (Separately, an extra source with both eigenvalues > 1 has a dead basin,
by Theorem 3.8(d).) Complete proof: Section 9.5. In outline, in coordinates (eta, v) the field
is alpha eta d_eta + B d_v with B_v(Z) = beta' > 1, and differentiating rho(Phi_t X) = e^t rho(X) in v shows that a
nonzero rho_v would grow like e^{(beta' - 1 - eps)T} along backward orbits.

Proposition 3.10 (saddle passage). Let Y be a saddle with eigenvalues -sigma < 0 < b = 2l + sigma. If rho = D|s|^k
(1 + o(1)), D != 0, on one side of a transversal to an incoming stable branch, then on a transversal to the adjacent
outgoing unstable branch rho = C|t|^{q_k}(1 + o(1)) with q_k = (kb - 1)/sigma and sgn C = sgn D. No linearisation is
used (Holder remainders are integrable along the passage). If the incoming branch is a branch of Gamma (k = 2),
q_2 = 2 + (4l - 1)/sigma > 2. Consequently, if the far side of such an outgoing branch is dead, C^m regularity
(integer m >= 3) needs sigma < (4l - 1)/(m - 2); this configuration is impossible for C^infinity profiles. Complete
proof: Section 9.6, Steps 1-3.

Theorem 3.11 (profiles whose zeros of V are exactly 0, an extra source Z and a saddle Y, all nondegenerate). (a) Both
unstable branches of Y escape and, with Y, form a proper line separating R^2 into B(0) and B(Z); one stable branch of
Y is a branch of Gamma, the other comes from Z; rho and its derivatives of order <= 3 vanish at Y. (b) For a
C^infinity profile, B(Z) is live, Z is a quadratic source (alpha = 1/2, rho = d eta^2 on B(Z)), q_2 = N is an integer
and sigma = (4l - 1)/(N - 2), with d > 0 only for N even >= 4 and d < 0 only for N odd >= 3 (and matching coefficients
at both outgoing branches). (c) In the x-even case Z and Y lie on the y-axis with Y strictly between 0 and Z,
psi_xy(Y) = -(l + sigma), and a live source with weak eigenvalue 1 or 1/3 is impossible. (d) No dead basin is a
half-plane. (e) No such profile is exactly r^p A(th) outside a disk.
Complete proof: Section 9.6, Steps 4-8 (the proof of (d) does not use the assumption on the zeros of V).

Proposition 3.12 (translated moment law and analytic profiles). At any zero P of V with grad rho(P) = 0,
Q_P := int rho W_P.grad(|z|^{-3} sin 3 arg z) = pi (l - 1) psi_xy(P) (z = X - P, W_P = W - W(P)), and DV(P) is
symmetric with eigenvalues l +- |(psi_xy(P), psi_yy(P))|; D^2 rho(P) has rank at most one and is nonzero only if
the smaller eigenvalue is 1/2 (no condition on D^2 rho(P) is needed for the moment law). A real-analytic profile has
no degenerate zero of V and no dead open set (for a C^infinity profile the argument gives only that rho is flat at a
degenerate zero of V). Complete proof: Section 9.8, Step 5.

Propositions 3.9-3.10 and Theorem 3.11 are necessary conditions on profiles outside S^+; the translated moment law and
the spectrum statement of Proposition 3.12 apply at any zero P of V with grad rho(P) = 0, including the origin of a
profile in S^+, and the statement on real-analytic profiles concerns every zero of V.

Further structure in S^+.

Theorem 3.13 (conjugacy to the dilation). Let rho in S^+. The limit S(X) = lim_{t -> infinity} e^{-lt} Phi_t(X)
exists, uniformly on compact sets, and defines a homeomorphism of R^2 fixing 0 that preserves Lebesgue measure, with
S(Phi_t X) = e^{lt} S(X) and S(X) = X + O(|X|^p) as |X| -> infinity. S is a C^2 diffeomorphism of R^2 minus 0 with
DS(X) = I + O(|X|^{p-1}) as |X| -> infinity, and S is not Lipschitz at 0. Exactly,
    rho = |S|^p A(arg S),   xi = |S|^{p/2} B(arg S)   (B the signed root of Theorem 3.2).
Each level set {xi = c}, c != 0, is one proper C^2 line whose two ends go to infinity in the two zero directions of A.
The level sets of xi are exactly the strong unstable leaves of the basin of 0: under the backward flow, distinct
points X, Y of one level set approach each other like |d_XY| e^{-(2l - 1/2)t} with d_XY != 0, and points of different
level sets like |xi(X) - xi(Y)| e^{-t/2}; only {xi = 0} = Gamma contains 0. Complete proof: Section 9.4. In outline:
e^{-lt} Phi_t X - X = int_0^t e^{-ls} W(Phi_s X) ds converges because |W| = O(|X|^p) and |Phi_s X| grows at most like
e^{ls}; S(Phi_s(R e_a)) = e^{ls} L(a) e_{Theta(a)}, so S is a bijection; the maps e^{-lt} Phi_t have Jacobian 1 and
are uniformly proper, so int f(e^{-lt} Phi_t X) dX = int f dX passes to the limit for continuous compactly supported
f, which gives measure preservation without convergence of derivatives at 0. Consequence: in S^+ the flow of V is
topologically conjugate to the dilation, and a profile is an exactly homogeneous function composed with an
area-preserving homeomorphism. Every existing S^+ profile has this representation; the theorem does not say that
arbitrary angular data A and area-preserving homeomorphisms S give a velocity and density solving the profile system.
Constructing a sufficiently regular pair (A, S) that satisfies the Darcy coupling remains open.

Proposition 3.14 (wall curvature in S^+_even; restricted exclusions). With the notation of Theorem 3.3 and
g(y) := d_x^2 W_2(0, y): b'' = -h - g (because Lap W_2 = -rho_xx), w'(y) = O(|y|^{p-1}), and the one-sided improper
integrals of g exist and satisfy
    int_{-inf}^0 g dy = -c - int_{-inf}^0 h dy < 0,     int_R g dy = -int_R h dy
(the improper integrals exist because g = -h - b'' is continuous, h is integrable and b' -> l at both ends;
absolute integrability of g, from |g(y)| <= C|y|^{p-2} for large |y| by Theorem 3.1, is not used). Consequently no
profile in S^+_even has g >= 0 on {y <= 0}, and none has g = 0 on (-beta, 0) (a fortiori on [-beta, 0]),
beta = 2l - 1/2: there the wall system integrates to h = 2 beta^4/(beta + y)^4 on (-beta, 0), where
b < 0, so h is finite inside the interval and blows up at the endpoint y = -beta, against the continuity of h. Both
are restricted exclusions; neither hypothesis on g is known for a general profile. The identities and both exclusions
hold equally with g defined from the twice-subtracted field (d_x^2 of the removed linear field is 0); the decay
w' = O(|y|^{p-1}) and Proposition 3.6 need w' = d_y W_2(0, y) with W_2 the component of W. Complete proof: Section
9.9, Step 5.

Proposition 3.15 (exact local curved-layer solution). For l > 1 and beta = 2l - 1/2,
    rho = x^2 (beta/(beta + y))^4,   psi = x (b(y) - l y),   b(y) = beta (beta + y)/3 - beta^4/(3 (beta + y)^2),
with W = (-psi_y, psi_x), solve -Lap psi = rho_x and (l X + W).grad rho = rho on {y > -beta}, with
rho = x^2 + O(|X|^3) at 0, W(0) = 0, c = psi_xy(0) = l - 1/2, and V = 0 only at 0 in that half plane. Within the
ansatz rho = x^2 f(y), psi = x s(y), with f in C^1(I) and s in C^2(I) on an open interval I containing 0, this
solution is unique and I is contained in (-beta, inf) (the ansatz reduces to b b'' = (3b' - beta)(b' - beta)/2 with
b(0) = 0, b'(0) = beta, b''(0) = -2; complete proof: Section 9.7). It is not in S (pole at y = -beta, quadratic growth
in x). It shows that the local wall system of Theorem 3.3 is consistent and that the obstruction to profiles of this
layered form is global.

Proposition 3.15a (layered solutions quadratic in x; x-parity is forced). Let l > 1, beta = 2l - 1/2, I an open
interval containing 0, f, g, k in C^1(I) and n, m, s, t in C^2(I), and on R x I let
    rho = f(y) x^2 + g(y) x + k(y),   psi = n(y) x^3 + m(y) x^2 + s(y) x + t(y),   W = (-psi_y, psi_x),   V = lX + W.
Suppose -Lap psi = rho_x and V.grad rho = rho on R x I, rho = x^2 + O(|X|^3) at 0 and W(0) = 0. Then g, k and m vanish
identically on I, t is constant, and n is constant with n = 0 or n = -1/3.
(a) If n = 0, then I is contained in (-beta, inf) and (rho, W) is the solution of Proposition 3.15.
(b) If n = -1/3, then rho = x^2 and psi = -x^3/3 + (l - 1/2)xy + t on R x I: the polynomial solution of Section 9.14,
Step 12 (growth 2, not in S).
In both cases rho is even in x and psi - t is odd in x. This symmetry is not assumed: the terms g x of rho and m x^2
and a nonconstant t of psi, which would break it, are excluded by the equations, the jet and W(0) = 0. In particular
the polynomial solution is the only solution of this ansatz on the whole plane (I = R). Complete proof: Section 9.16.

Proposition 3.15b (layered solutions cubic in x, stream function of any degree in x). Let l > 1, beta = 2l - 1/2, I an
open interval containing 0, N <= 3 and M >= 0 integers, f_0, ..., f_N in C^1(I) and q_0, ..., q_M in C^2(I), and on
R x I let
    rho = sum_{j=0}^N f_j(y) x^j,   psi = sum_{j=0}^M q_j(y) x^j,   W = (-psi_y, psi_x),   V = lX + W.
Suppose -Lap psi = rho_x and V.grad rho = rho on R x I, rho = x^2 + O(|X|^3) at 0 and W(0) = 0. Then, up to an
additive constant in psi, (rho, psi) is either the solution of Proposition 3.15, with I contained in (-beta, inf), or
the polynomial solution rho = x^2, psi = -x^3/3 + (l - 1/2)xy. Thus the conclusions of Proposition 3.15a (x-parity is
forced; only the polynomial solution exists when I = R) persist when the density is cubic in x and the stream function
has arbitrary degree in x. In particular, among real polynomial pairs whose density has degree at most three in x,
with no bound on the degree in y or on the degree of psi, the polynomial solution is the only one with the jet and
W(0) = 0. In arbitrary degree the proof gives a reduction that uses only the two differential equations and the stated
regularity: if the actual x-degrees satisfy M > N >= 2, then M = N + 1, q_M is a nonzero constant, and every f_j and
q_j is a polynomial with deg f_j <= N - j and deg q_j <= M - j. No classification in arbitrary density degree is
claimed. Complete proof: Section 9.18.

Far field beyond the leading term.

Theorem 3.16 (forced far-field correction). Let rho in S, F = r^p A(th), let Psi be the periodic solution of
Psi'' + (p+1)^2 Psi = (sin th A)' - (p+1) cos th A (unique since p + 1 is not an integer),
H = H_p[A] = r^p(-Psi' e_r + (p+1) Psi e_th) the canonical velocity of F, and J_p[A] = (p + 1) Psi A' - p Psi' A (for
Holder A this is the distribution (p + 1)(Psi A)' - (2p + 1) Psi' A, Psi being C^1).
(a) W = H + o(r^p) uniformly in angle, and R^{1-2p} [rho(R .) - R^p F] -> r^{2p-1} J_p[A]/(l - 1) in distributions on
R^2 minus 0.
(b) If A has a positive quadratic zero beta (A(beta) = A'(beta) = 0 < A''(beta); A is C^1 by Theorem 3.1, and only the
existence of A''(beta) is used), J_p[A] is
not identically zero on either one-sided neighbourhood of beta.
(c) Hence, if A has a positive quadratic zero (this holds for every profile in S^+ and for every profile as in
Theorem 3.11), int_{R<r<2R} |rho - r^p A|^2 dX >= C R^{4p} for all large R. In
particular int_{r>1} r^{-4p} |rho - r^p A|^2 dX = infinity, rho - r^p A is not in L^2(r > 1), it is not o(r^{2p-1})
uniformly, and it is not in L^q(r > 1) for 1 <= q <= 2/(1 - 2p) (for every finite q >= 1 if p >= 1/2). These
conclusions use only that J_p[A] is not identically zero; by Proposition 3.18(c) they hold for every profile in S.
(d) Uniformly in th (A is C^1 by Theorem 3.1),
    rho = r^p A + r^{2p-1} J_p[A]/(l - 1) + o(r^{2p-1}),
and the annular integral in (c) divided by R^{4p} tends to (2^{4p} - 1)/(4p (l - 1)^2) int |J_p[A]|^2 dth.
Complete proof: Section 9.3. In outline, f_t(X) = e^{-pt} rho(e^t X) satisfies d_t f_t = -p e^{-(1-p)t} div(f_t w_t),
w_t the rescaled velocity; this gives a rate for f_t -> F on annuli, and with it w_t -> H uniformly on annuli
(uniform convergence of f_t to a Holder limit alone would not suffice; Section 9.3, Step 3 uses the rate and the
gradient bound); integrating in t gives (a), with the limit div(F H)/(l - 1) = r^{2p-1} J_p[A]/(l - 1). For (b),
J_p[A] = 0 forces Psi = C A^{(p+1)/p} on a one-sided interval where A > 0, which is o(t^4) at a quadratic zero, while
the angular equation gives
Psi ~ a sin(beta) t^3/3, or a (2 - p) cos(beta) t^4/12 when sin(beta) = 0. (c) is Holder's inequality on dyadic
annuli against a test function with nonzero pairing. (d): on the exterior rho = F o S with the scattering map
S(X) = X + H(X)/(l - 1) + o(r^p), and a first-order Taylor expansion of F. The verifier also checked (a) and (d)
numerically on a manufactured exterior flow (V = lX + H exactly, rho = F o S): over the tested radii the normalised
remainder decayed consistently with R^{p-1}.
This is a restriction on tail conditions; it does not show that S^+ is empty and gives no bound on c_l. It sharpens
Theorem 3.5: for profiles whose far-field coefficient has a positive quadratic zero (including every profile in S^+),
the first correction r^{2p-1} J_p[A]/(l - 1) is nonzero, so an exactly homogeneous exterior is impossible and the
correction decays only by the factor r^{p-1} relative to the leading term. Proposition 3.18(c) removes the hypothesis
on A: J_p[A] is not identically zero for every profile in S. Where A != 0, a box solver that imposes a pure power tail
rho = r^p A at radius L makes the leading relative error L^{p-1} J_p[A]/((l - 1) A); its size depends on the angular
coefficients, and the ratio is not an appropriate error measure at the zeros of A. The first correction should
therefore be part of any far-field boundary condition used for a candidate (Section 5).

Proposition 3.17 (axis identity in S^+_even). Let rho in S^+_even, with b(y) = V_2(0, y) = l y + w(y), h and H_+- as
in Theorem 3.3, and beta = 2l - 1/2. For r > 0 put B_+(r) = b(r) and B_-(r) = -b(-r) (the outward speeds on the two
half-axes; both are positive), b_o = (B_+ + B_-)/2 and w_e = (B_+ - B_-)/2 = (w(r) + w(-r))/2, so that B_+
B_- = b_o^2 - w_e^2 > 0. Then, with absolutely convergent integrals,
    H_+- = A''(+-pi/2) = (2 l^2/beta^2) exp(-2 beta J_+-),
    J_+- = int_0^1 (1/B_+- - 1/(beta r)) dr + int_1^inf (1/B_+- - 1/(l r)) dr,
    log(A''(-pi/2)/A''(pi/2)) + 4 beta int_0^inf w_e/(b_o^2 - w_e^2) dr = 0
(A''(-pi/2) means A''(3pi/2)). Hence int_0^inf w_e/(B_+ B_-) dr has the sign of log(A''(pi/2)/A''(-pi/2)), and if the
two curvatures are equal, w_e either vanishes identically on (0, inf) or takes both signs there. This is the profile
case of 5.8(v): in S^+_even every hypothesis of 5.8(v) holds (B_+- > 0, the common node exponent n = beta, the common
far-field speed l r, and transverse coefficients equal to the angular curvatures), h = 2 k^2 on the axis gives
G(+inf) = G(-inf) = 1, so D = 0, and with A = cos^2 th e^F the formula of 5.8(v) is the identity above. Restricted
exclusion: no profile in S^+_even has A''(-pi/2) <= A''(pi/2) and w_e <= 0 on (0, inf) except with equal curvatures
and w_e = 0 identically, and likewise with both inequalities reversed. Neither the curvature ratio nor a sign of w_e
is known for a general profile (Section 4.2 records test densities, not profiles, on which w_e takes both signs).
Complete proof: Section 9.10.

Proposition 3.17a (curvature law on the two branches of Gamma in S^+). Let rho in S^+, p = 1/l, beta = 2l - 1/2, let
Gamma_1 and Gamma_2 be the two components of Gamma minus 0 (Theorem 3.2), and let th_j = arg S(z) for z in Gamma_j
(S as in Theorem 3.13; th_1 and th_2 are the two zeros of A, and Gamma_j escapes to infinity in the direction th_j).
Parametrise Gamma_j by arclength q > 0 from 0, z = z_j(q), and put v_j(q) = |V(z_j(q))| > 0. Then, with absolutely
convergent integrals,
    A''(th_j) = (2 l^2/beta^2) exp(-2 beta T_j),
    T_j = int_0^1 (1/v_j(q) - 1/(beta q)) dq + int_1^inf (1/v_j(q) - 1/(l q)) dq,
and log(A''(th_2)/A''(th_1)) = -2 beta (T_2 - T_1). For every z in Gamma_j, with h = d_n^2 rho = 2|grad xi|^2 as in
Theorem B (F4),
    A''(th_j) = l^2 h(z) |S(z)|^(4 - p)/|V(z)|^2,
and as q -> 0, |S(z_j(q))| q^(-l/beta) tends to a limit k_j > 0 with A''(th_j) = (2 l^2/beta^2) k_j^(4 - p). In
S^+_even the components are the two half-axes, q = |y| and v_j = B_+-, and the first two formulas are those of
Proposition 3.17 for H_+-. No parity is assumed. No sign of T_2 - T_1 is known for a general profile; T_j and k_j
depend on the whole branch, so these formulas do not determine A'' from a finite jet at 0. Complete proof:
Section 9.25.

Proposition 3.18 (sublevel areas, critical zeros of A and the forced correction). Let rho in S be a profile and write
|E| for the area of a set E.
(a) For every h > 0 there are c > 0 and R_0 such that |{0 <= rho < h} cap {|X| <= R}| >= c R^(2 - p/2) for every
R >= R_0.
(b) There are two distinct components of {A > 0} that are open arcs with two distinct endpoints each, and every
endpoint of these two arcs is a zero of A at which A' = 0. In particular A has two distinct zeros th_1 and th_2 with
A(th_j) = A'(th_j) = 0, and A > 0 on an open arc adjacent to each th_j.
(c) J_p[A] (Theorem 3.16) is not identically zero. Hence the conclusions of Theorem 3.16(c) hold for rho, the limit of
the annular integral in Theorem 3.16(d) is positive, and rho does not equal r^p A(th) exactly outside any disk.
The proof of (a) uses a band at 0: near 0, rho = xi^2 (Theorem B (F3)), so a band {|xi| < c e^(-T/2)} inside a fixed
coordinate rectangle at 0 has area of order e^(-T/2) and carries 0 <= rho < c^2 e^(-T), and Phi_T multiplies its area
by e^(2lT) and keeps it in a disk of radius of order e^(lT). For (b), rho = xi^2 vanishes at exactly two points of a
small circle C_eps around 0, quadratically, and is positive on the two complementary arcs; every orbit through these
arcs reaches the circle {|X| = R} of Theorem 3.1, and the induced map H between the two circles satisfies the exact
flux identity R V_r(R e_H) f(H)^(-2l) H' = eps V_r(eps e_s) g(s)^(-2l), where g and f are the restrictions of rho to
the two circles. At an end of either arc the right side is not integrable, which forces f = 0 at the corresponding
endpoint of the image arc, and a simple zero there would make the travel time from C_eps tend to -infinity. For (c),
J_p[A] = 0 on an arc adjacent to a zero th_0 as in (b) would make the angular stream function Psi a multiple of
A^((p+1)/p), which the angular equation does not allow; Theorems 3.5 and 3.16(b) use this at a zero with
A''(th_0) > 0. No assumption on the zeros of V is made. The zeros in (b) are not shown to be quadratic; if a branch of
Gamma minus 0 (Theorem B (F3)) is unbounded, A has a zero at which A'' > 0, by the argument of Section 9.6,
Step 8 (Section 9.24, Step 8). In S^+, (b) is contained in Theorem 3.2 (A > 0 except at two quadratic zeros), and for
0 < a < b the area of {a < rho < b} cap {|X| <= R} is asymptotic to a positive multiple of R^(2 - p/2)
(Section 4.16(b)); taking b <= h, this gives (a) in S^+ directly. Outside S^+, (b) excludes, for example, far-field
coefficients A <= 0, coefficients for which {A > 0} is connected, and coefficients all of whose zeros have A' != 0.
These are necessary conditions on profiles; they do not establish that S is empty. Complete proof: Section 9.24.

## 4. Nonexistence attempts and why they do not close
Every identity in Sections 2a and 3 is a necessary condition; a sign that contradicts one of them for every profile in
the class would give nonexistence. Other obstructions are not excluded, and the tests below do not exhaust the
possible nonexistence arguments. This section contains necessary conditions for profiles, conditional limit
statements, angular tests, statements on the linearisation at a hypothetical x-even profile (4.17), and exact or
numerical tests on test densities (functions with the jet and the growth of S that are not required to solve
the profile equation); with exact or numerical counterexamples where they exist, it records why the sign arguments
tried here do not close. A sign that fails on such test densities is refuted only as a consequence of the hypotheses
that those densities satisfy; an argument that uses further conditions forced by the profile equation is not excluded.
The proof-status inventory in Section 2a distinguishes complete proofs, outlined or omitted arguments, additional
hypotheses and numerical tests; those distinctions apply to every subsection below.

4.1 Moment law (Theorem C). A profile needs Q[rho] = pi c(c - 1/2) > 0. Q has no sign on nonnegative x-even
densities: for rho_a = x^2 (1 + a y)^2 e^{-r^2} one has c = a/4, psi_xx(0) = 0 and
    Q(rho_a) = pi [3a^4/512 + (51 log 2/32 - 265/256) a^2 + 3 log 2/8 - 21/64],
which is negative at a = 0 and a = 1/2 and positive at a = 1 (closed form; independently recomputed to 2e-15). Since
kappa = Q/(pi c^2) is scale invariant, the moment law is one scalar condition on the shape of rho; no contradiction
for profiles has been obtained from it.

4.2 Wall identity (Theorem 3.3). In S^+_even a sign int h w' <= 0 would exclude the class. On nonnegative x-even
test densities rho = x^2 (1 + a y/<r>)^2 <r>^{p-2} (<r> = (1 + r^2)^{1/2}, |a| < 1, zero set exactly the axis, A
vanishing only at +-pi/2), the scale-invariant ratio kappa_w/c with kappa_w := int h w'/int h takes values 0.26-0.39
for p in {0.3, 0.5, 0.7}, a in {0.3, 0.6, 0.9}, while a profile with growth exponent p needs
(1 - 1/(2c))/3 = 2(1 - p)/(3(2 - p)) (c = 1/p - 1/2), i.e. 0.27, 0.22, 0.15 for p = 0.3, 0.5, 0.7. The computed
positive values contradict the proposed sign numerically (a rigorous counterexample would need an analytic evaluation
or a certified error bound, which is not given; the exact Gaussian example of 4.1 is of that kind), and the identity
is again a single shape condition of the same size as the values found on simple test densities. The Fourier
form (Proposition 3.6) turns it into a phase condition; no derivation of a sign of the phase from positivity,
from rho_x > 0 on x > 0, or from the two-sided bound of Theorem 3.3 is known.

Both conditions can be met at once to numerical accuracy. For rho = x^2 exp(2F)(1 + r^2)^{-3/4} (growth exponent 1/2),
with F a two-parameter combination of bounded smooth features with prescribed angular limits at infinity and F(0) = 0,
Newton in the two parameters gives kappa = 3 kappa_w/c = 2/3 (the values a profile with p = 1/2 needs) with residuals
about 1e-7 at converged resolution, in two independent evaluators. The densities are smooth, x-even, with the growth
of S, positive off x = 0, their angular profile has exactly two quadratic zeros, and the sampled velocity V = l X + W
had no zero besides 0. These are test densities with S^+_even-type geometry, not profiles (transport is not imposed);
exact joint satisfaction and the global absence of further zeros of V are not certified. So these two conditions alone
are unlikely to give a density-only obstruction under the tested geometric assumptions.

The axis identity (Proposition 3.17) gives a restricted exclusion in S^+_even: A''(-pi/2) <= A''(pi/2) together with
w_e <= 0 on (0, inf), or both inequalities reversed, is impossible unless the curvatures are equal and w_e = 0
identically. No condition placing every profile in one of these excluded cases has been proved. On test densities w_e
has no fixed sign, even with the node of a profile: rho_* = x^2 (1 + 6y + 10y^2) e^{-r^2} is positive off the axis,
has the jet x^2 + O(|X|^3) and c = 3/4 = l - 1/2 at l = 5/4 (so DV(0) = diag(1/2, 2)), and
w_e(1) = 293/8 - 395/(4e) > 0 > w_e(10) (closed form; w_e depends only on the y-even part x^2 (1 + 10y^2) e^{-r^2}).
It is not a profile: E = b h' - 2(b' - beta) h (beta = 2) has E'(0) = 35/2. The integral has no sign from the geometry
and the absence of other zeros of V either: for rho = x^2 (1 + M y^2/L^2) e^{-r^2/L^2} with L = 1/100 and l = 2, V has
no zero besides 0 (|DW| <= 37 sqrt(pi)/200 < l), and int_0^inf w_e/(B_+ B_-) dr is negative for M = 0 and positive for
M = 3 (about -5.9e-4 and 4.2e-5; writing I_M for the integral and I_M^0 = (L/l^2) sqrt(pi) (5M - 14)/105, the bound
|I_M - I_M^0| < (3/9999) |I_M^0| holds for M = 0 and M = 3). These densities have c = 0 and are not profiles.
Derivation of the two bounds (not used in the proof of Proposition 3.17): by Fourier inversion, with the velocity
multiplier bounded in norm by 1 and |rho^(k)| <= pi L^4 exp(-L^2|k|^2/4) (1/2 + L^2|k|^2/4) (1 + M/2 + M L^2|k|^2/4),
sup |DW| <= L sqrt(pi) (2 + 11M/2), which is sqrt(pi)/50 for M = 0 and 37 sqrt(pi)/200 for M = 3; since W(0) = 0,
|V(X)| >= (l - sup |DW|) |X|. Next w(r) = L^2 f_M(r/L) with f_M the y-even axis velocity of x^2 (1 + M y^2) e^{-r^2},
B_+ B_- = l^2 r^2 - w(r)^2, so I_M = (L/l^2) int_0^inf (f_M(s)/s^2) / (1 - (L/l)^2 f_M(s)^2/s^2) ds and int_0^inf
f_M(s)/s^2 ds = sqrt(pi) (5M - 14)/105.
The representation f_M(s) = (1/4) int_0^1 (3t - 1) [(1 + M/2 - Mt/2)(exp(-t s^2) - 1) + M t^2 s^2 exp(-t s^2)] dt,
with 1 - exp(-z^2) <= min(z^2, 1), z exp(-z^2) <= 1/2 and int_0^1 |3t - 1| t^{1/2} dt < 2/3, gives |f_M(s)|/s < 1/2
and int_0^inf |f_M(s)|/s^2 ds < sqrt(pi) (1 + M/2)/6, hence |I_M - I_M^0| <= 175/639996 |I_M^0| for M = 0 and 3.

4.3 Mass removal and the sign of c. The rule "removing density above the centre lowers c" is false: the change of c
is -(1/pi) int delta rho y(3x^2 - y^2)/r^6, whose kernel changes sign in the upper half plane; removing mass from
y > 2(1 + x^2)^{1/2} raises c. Hence dead regions (Theorem 3.8(d)) cannot be assigned a sign of c by their position.

4.4 Energy and virial identities. The potential-energy functional int y rho diverges: int |y| |rho| = infinity for
every nonzero profile in S, since rho ~ r^p A with A not identically 0 (Theorem A); for test densities in S it can be
finite (rho = x^2 e^{-r^2}). Localised versions carry pressure and transport
fluxes through the cut-off of the same order as the localised quantity, so they give no sign.
Three further routes were examined in S^+, using the label-coordinate assertions of 4.6, whose proofs are omitted
here. The following label calculations retain that limitation. Write N = (1/2) u d_u + (2l - 1/2) v d_v, and let Pi be
the potential with grad Pi = V + rho e_2. (i) Variational. Under the area, regularity, jet and far-field constraints,
the profile system is the distributional closedness of the 1-form (N X).dX + u^2 dy. The corresponding force 1-form on
area-preserving maps, T_X(Z o X) = int (N X + u^2 e_2).(Z o X) du dv (Z divergence-free with compact support away from
0), is not closed: its exterior derivative at (Z o X, H o X) is int ((V.grad Z).H - (V.grad H).Z) dX. For a fixed unit
vector e, a nonzero smooth bump f supported where V.e > 0 and R(s, t) = (-t, s), the fields
Z_k = R grad(f sin(k e.X)/k), H_k = R grad(f cos(k e.X)/k) make it k int f^2 (V.e) dX + O(1), with
int f^2 (V.e) dX > 0. So no C^2 scalar functional of the label map has this force 1-form as its first variation; the
dilation term does not change this (int l X.(Z o X) du dv = 0), and stationarity of the potential-energy part alone
would force rho_x = 0, against the jet (self-similarity does not imply that stationarity). Other variational
formulations are not excluded. (ii) Commuting fields. The fields Y_1 = DX(u d_u) and Y_2 = DX(v d_v) are C^1 (they use
xi in C^2; Y_2 = eta R grad xi and V = Y_1/2 + (2l - 1/2) Y_2), commute with V and with each other, have divergence 1
and satisfy Y_1.grad rho = 2 rho, Y_2.grad rho = 0. The identities they give contain the label geometry, but no sign
that gives a contradiction was found: rho = x^2 with V = (x/2, (2l - 1/2) y - x^2) and labels
X(u, v) = (u, v + u^2/(2l - 3/2)) solves transport and the differential Darcy coupling,
V + rho e_2 = grad(x^2/4 + (2l - 1/2) y^2/2), with the jet for every l > 1, has both commuting fields, and its strain
contractions take both signs: with b = 2l - 1/2, h = 1/(b - 1) and S_i = (DY_i + DY_i^T)/2,
V.S_1V = x^2(1/4 + 2hby - 2hx^2) and V.S_2V = (by - x^2)(by - (1 + h)x^2), and for fixed x != 0 each changes sign as y
varies. It has growth 2 and violates W = o(r), so it refutes sign arguments that use only these
differential properties, not an inequality that uses the full class S^+. (iii) Circulation along Gamma. On Gamma, grad
Pi = V, so Pi increases along both branches; but in the loop formed by the two branches and an arc of a circle of
sufficiently large radius R the branches enter with opposite orientations, and q = Pi - l|X|^2/2 satisfies
q(P_2) - q(P_1) = int_arc (W.dX + rho dy) (P_1, P_2 the points of Gamma on the circle). Both sides are O(R^{p+1}) and
their leading coefficients agree identically (A of Theorem A, Psi the angular stream function of Theorem 3.16; with
Q = (A sin th - Psi')/(p + 1), Q' = (p + 1) Psi + A cos th); that coefficient is not shown to be nonzero. For a
material loop, I = oint V.dX satisfies I' = I - oint rho dV_2, whose last term has no universal sign (both signs occur
for small loops near (+-eps, 0)). These calculations give no contradiction; a further argument needs information not
established here, for example an estimate linking the label geometry to the sublinear velocity.

4.5 Far fields. Theorem 3.5 uses that the exterior is exactly homogeneous. By Theorem 3.16 and Proposition 3.18(c),
the correction r^{2p-1} J_p[A]/(l - 1) is present for every profile in S (Theorem 3.16 alone gives this when A has a
positive quadratic zero), and Theorem 3.16(c) excludes every remainder that is small in the critical weighted L^2
sense; profiles with such corrected tails are not excluded, and the formal far-field expansion (degrees p, 2p - 1,
3p - 2, ... and terms from the core) has no resonance at degree p, so it gives no contradiction by itself. The
weighted Darcy energy identity
    E_m = (1 + 3l - m l) M_m - m int r^{-m-2} (P + y rho) W.X dX,   p + 3 < m < 4,
(E_m = int r^{-m} |W|^2, M_m = int r^{-m} y rho dX, P the pressure with W = -grad P - rho e_2, P(0) = 0) is exact,
but as m -> 4 the pressure term supplies a pole 2 pi c^2/(4 - m) equal to that of E_m, so the identity yields no sign.

4.6 A possible next direction. In S^+ the density is xi^2 with xi constant on the strong unstable leaves of the
basin of 0, and every density-only condition tested above is met, exactly or to numerical accuracy, by suitable test
shapes. A nonexistence proof in S^+ (or S^+_even) along the lines of this section would have to use the coupling
between the leaf geometry and the Biot-Savart velocity, for example by a sign of the phase in Proposition 3.6 derived
from the transport equation. No such argument was found, and other mechanisms are not excluded.
Label coordinates for S^+ (statements checked by the verifier; proofs not reproduced). For rho in S^+ there is a
global C^1 map Phi = (xi, eta) with det D Phi = 1, V.grad xi = xi/2 and V.grad eta = (2l - 1/2) eta (xi the signed
root of Theorem 3.2, with its sign fixed; eta an area companion, unique up to adding a function of xi of the form C_+
|xi|^{4l-1} on xi > 0 and C_- |xi|^{4l-1} on xi < 0). Thus Phi conjugates V to the linear field N = (1/2) u
d_u + (2l - 1/2) v d_v, and V = (1/2) xi J grad eta - (2l - 1/2) eta J grad xi with J grad g = (g_y, -g_x). In these
labels the profile system is equivalent, under the growth bounds of S and V - l X = o(r), to one equation for the
area-preserving inverse map X(u, v): the 1-form (N X).dX + u^2 dy is closed (in the distributional sense; X is C^1),
so (DX)^T N X + u^2 grad y = grad P with P in C^1; the condition is second order in X (third order in a generating
function of X). Two limits of this formulation: global C^2 regularity of Phi is not proved (the general implication
from a C^3 density with a nondegenerate zero line to C^2 area-preserving coordinates is false; an explicit
counterexample, not an IPM profile, has a C^2 but not C^3 root chart and no C^2 area companion), and the linearised
label operator is not Fredholm in any bounded realization, with norms locally equivalent to H^3 and L^2, that admits
compactly supported interior variations (sequences oscillating in the orbit label v/|u|^{4l-1} are not controlled).
These two statements are recorded with their proofs omitted: the counterexample and the operator, its function spaces
and the oscillating sequences are not reproduced here; the operator is not the forward-map operator of Section 5.8.
The formulation yields no existence or nonexistence statement and no restriction on l beyond l > 1.

4.7 The regime c_l -> 1+ (conditional results). Write eps = 1 - p; Psi_p[A], H_p[A] and J_p[A] are as in Theorem 3.16.
(i) Scaling. T_L rho = L^2 rho(X/L) preserves the jet and kappa but is not a symmetry of the profile system: for a
profile rho and l_L = 1/2 + Lc, the residual of T_L rho is L^2 (L - 1)[rho - (1/2) Y.grad rho](X/L), Y = X/L. The only
scaling symmetry is rho -> a rho(X/a) (velocity a W(X/a)), which changes the jet coefficient to 1/a.
(ii) Correction relation. If a profile has rho = r^p A + r^{2p-1} B + o(r^{2p-1}) uniformly, then (l - 1) B = J_p[A]
(Theorem 3.16).
Proposition 4.7 (no steady angular pair at p = 1). There is no periodic C^2 pair (A, Psi) with A >= 0 having exactly
two zeros, both positive quadratic, such that Psi'' + 4 Psi = -cos th A + sin th A' and 2 Psi A' - Psi' A = 0.
(Proof: Psi = C A^2 on each positive arc; at a zero beta the forcing is 2a sin(beta) t + o(t), so sin(beta) = 0, and
then C = cos(beta)/(12 a), which is positive at 0 and negative at pi, on the same arc.)
Corollary 4.8 (regular endpoint). Let rho_n in S^+ with p_n -> 1 each have the expansion of (ii) with A_n, B_n in C^2,
and suppose A_n/M_n -> A_* and Psi_{p_n}[A_n]/M_n -> Psi_* in C^2 (M_n = sup A_n, c_n = 1/p_n - 1/2), where A_* has
exactly two zeros, both positive quadratic. Put J_1[A_*] := 2 Psi_* A_*' - Psi_*' A_* (at p = 1 the angular equation
of Theorem 3.16 is resonant in mode 2, so Psi_* and hence J_1[A_*] are not determined by A_* alone). Then
(1 - p_n) c_n B_n/M_n^2 -> J_1[A_*]/2 uniformly, and J_1[A_*] is not identically zero; hence
(1 - p_n) ||c_n B_n/M_n^2||_inf -> ||J_1[A_*]||_inf/2 > 0, and there are d, D > 0, depending on the sequence, with
d/(1 - p_n) <= ||c_n B_n/M_n^2||_inf <= D/(1 - p_n) for all large n. (Passing to the limit in the angular equation
gives Psi_*'' + 4 Psi_* = sin th A_*' - cos th A_*, so J_1[A_*] != 0 by Proposition 4.7. With Abar_n = A_n/M_n,
Psibar_n = Psi_{p_n}[A_n]/M_n and kappa_n = 2(1 - p_n)/(2 - p_n), the normalised correction satisfies
(p_n + 1) Psibar_n Abar_n' - p_n Psibar_n' Abar_n = kappa_n c_n B_n/M_n^2, and kappa_n/(1 - p_n) -> 2; the left side
tends to J_1[A_*] uniformly.) In words: along any such regular sequence the supremum norm of the normalised far-field
correction is comparable to 1/(1 - p); this is a norm comparison, not a pointwise lower bound, and no bound uniform
over profiles without these convergence hypotheses is proved.
(iii) Far-field resolution scale. For A = cos^2 th the exterior expansion is explicit: Psi_p[A] = -(3p+2)/(4p(p+2))
cos th - cos 3th/(4(p+4)), B_p = sin th cos^2 th [2(p+1) + p(2-p) cos^2 th]/((1-p)(p+4)), and the residual of r^p
A + r^{2p-1} B_p is O(r^{3p-2}). The stream coefficient of the correction has
(1-p)^2 [Psi_{2p-1}[B_p]]_{sin 2th} -> 19/320 (exactly, the coefficient is p(-5p^2 + 25p + 18)/(64 (1-p)^2
(p+1)(p+4))), so the ratio of the two velocity terms is comparable to eps^{-2} r^{-eps} uniformly near p = 1, and in
the joint limit eps -> 0 it tends to zero iff eps log r - 2 log(1/eps) -> infinity. The crossover scale
R_*(eps) = eps^{-2/eps}, at which eps^{-2} r^{-eps} = 1, is about 16, 7 x 10^2, 10^7 and 8 x 10^22 for c_l = 2, 1.5,
1.25, 1.1; the condition r/R_* -> infinity alone does not give separation (r = R_*/eps gives eps^{-2}
r^{-eps} = eps^eps -> 1). These are statements about the two homogeneous terms for A = cos^2 th, not bounds for
general profiles or lower bounds on the domain size needed by every solver.
(iv) No density-only tail control. Put M = max |A|, m_3(A) = int A sin 3th dth, and
    c_in(R) = (1/pi) int_{|X|<R} rho r^{-3} sin 3th dX,
    d_R = sup_{r >= R, th} |rho(r, th) - r^p A(th)|/(M r^p),   T_R = M R^{-eps}/c.
For a profile in S, c = l - 1/2 > 0 and M > 0. Splitting its strain integral gives
    |m_3(A)|/M <= (pi eps/T_R) |1 - c_in(R)/c| + 4 d_R.
Let chi_out be a smooth radial cutoff, zero for r <= 1 and one for r >= 2, with 0 <= chi_out <= 1. The x-even test
densities x^2 (1 + r^2)^{(p-2)/2} [1 + a chi_out(r/R_p) y/r], R_p = e^{(1-p)^{-2}}, have c -> 0 while m_3(A) = a pi/4.
Thus individual far-field convergence does not give uniform density-only tail control as p -> 1.
(v) What transport alone allows (complete construction proof omitted). Let chi_in be smooth, radial, equal to one
near 0 and zero outside a disk, with 0 <= chi_in <= 1. For every l > 1, the non-Darcy field
W = grad-perp((l - 1/2)xy chi_in(r)) is asserted to admit a transported density x^2 g(X), g > 0, with an exact
homogeneous exterior, an area-preserving scattering map and the flux identities. If so, these properties without the
Darcy coupling give neither a positive gap above l = 1 nor a finite upper bound on l. The field does not satisfy the
Darcy law, so this is not an IPM profile, and no complete proof of the construction is supplied in this report.
None of (i)-(v) is an absolute gap above c_l = 1 or an upper bound on c_l. The envelope bound
1/gamma <= l <= 1/2 + (4/pi)(H + C/(1 - gamma)) (|rho| <= H r^2 for r <= 1, |rho| <= C r^gamma for r >= 1) holds but
is not uniform over S. Proposition 4.13a (in 4.8) sharpens it for rho >= 0, and its parts (c) and (d) concern p -> 1.

4.8 The regime c_l -> infinity (conditional results). Put l = c_l and p = 1/l for a profile rho in S, and rescale
    f_p(Z) = p^2 rho(Z/p),   w_p = W[f_p] = p^2 W[rho](Z/p),   b_p = Z + w_p = p^2 V(Z/p).
Then exactly
    b_p.grad f_p = p f_p,   div b_p = 2,   curl b_p = -d_x f_p,   b_p(0) = 0,
    f_p(0) = 0,   grad f_p(0) = 0,   D^2 f_p(0) = diag(2, 0),   f_p = z_1^2 + O_p(|Z|^3),
    Db_p(0) = diag(p/2, 2 - p/2),   c[f_p] = 1 - p/2,   kappa[f_p] = (1 - p)/(1 - p/2).
Here c[g] = psi[g]_{xy}(0) = (1/pi) int g r^{-3} sin(3 th) dZ is the strain of the canonical velocity, and
kappa[g] = Q[g]/(pi c[g]^2), Q[g] = int g W[g].grad(r^{-3} sin(3 th)) dZ, as in Theorem C. The jet remainder need not
be uniform in p. Under the convergence in Theorem 4.9 the differential equations pass to p = 0. The identity
b = Z + W[f] additionally requires justification of the nonlocal limit; it holds under part (b) and under Corollary
4.10, as proved in Section 9.15. Nothing in S makes a family of profiles converge, so convergence is assumed
explicitly below.
Theorem 4.9 (regular large-l limits). Let rho_n in S be profiles with p_n -> 0, and suppose f_n := f_{p_n} -> f in
C^2_loc and b_n := b_{p_n} -> b in C^1_loc.
(a) The limit satisfies
    b.grad f = 0,   div b = 2,   curl b = -f_x,   b(0) = 0,
    f = z_1^2 + o(|Z|^2),   Db(0) = diag(0, 2).
There are delta > 0 and a C^1 function h with h(0) = h'(0) = 0 such that b(x, h(x)) = 0 for |x| < delta and f(x,
h(x)) > 0 for 0 < |x| < delta. For each fixed nonzero x in this interval, (x, h(x)) is not the limit of zeros of
b_{n_j} along any subsequence n_j -> infinity. The origin is itself a zero of every b_n. On a common neighborhood of 0
the nullclines b_{n,2} = 0 are C^1 graphs y = h_n(x), with h_n(0) = h_n'(0) = 0 and h_n -> h in C^1 on smaller closed
intervals. On these graphs,
    b_{n,1}(x, h_n(x)) = (p_n x/2)(1 + eps_n(x)),
    eps_n(0) = 0,   sup_n sup_{0 < |x| <= t} |eps_n(x)| -> 0   as t -> 0.
(b) If moreover sup_{|Z| = r} |b(Z) - Z|/r -> 0 as r -> infinity, then f is bounded and attains its maximum M > 0 at a
zero q of b with grad f(q) = 0. Every connected component of a nonempty regular level set of f is a properly embedded
line carrying exactly one zero of b. The field b is not real-analytic on R^2. Also b = Z + W[f], with W[f] given by
the once-subtracted integral, which converges for this bounded C^2 density. For all sufficiently large n,
    |b_n(q) - b(q)| |grad f_n(q) - grad f(q)| >= M p_n/2.
Consequently neither error is O(p_n), and there is no regular first-order expansion in p at q. No sign condition on f
or rho_n is assumed; M > 0 follows from the quadratic jet.
(c) If f_n -> z_1^2 in C^2_loc, then for every fixed R > 0,
    (1/pi) int_{|Z| > R} f_n r^{-3} sin(3 th) dZ -> 1.
Thus the strain escapes every bounded disk, in the sense of this signed moment.
Complete proof: Section 9.15.
Corollary 4.10 (conditional bound). For constants C, M, a > 0 and gamma, eta in (0, 1), let S(C, M, a, gamma, eta)
consist of the profiles in S whose rescaled data satisfy
    |w_p(Z)| <= C(1 + |Z|)^gamma,
    ||D^2 f_p||_inf + [D^2 f_p]_{C^eta} <= M,
    ||D^k b_p||_inf <= M a^{-k} k!   for every integer k >= 1.
Then l <= L_*(C, M, a, gamma, eta) < infinity on S(C, M, a, gamma, eta).
Complete proof: Section 9.15. It is not known whether these subclasses are nonempty, so this is a statement about
uniform bounds, not an upper bound on c_l over S.
Remark 4.11 (far field as c_l -> infinity). Fix a real 2 pi-periodic A in C^2, independently of p, with mean Abar and
second Fourier coefficients a_2, b_2, normalized by
    Abar = (1/(2 pi)) int_0^{2 pi} A(th) dth,
    a_2 = (1/pi) int_0^{2 pi} A(th) cos(2 th) dth,
    b_2 = (1/pi) int_0^{2 pi} A(th) sin(2 th) dth.
The periodic stream coefficient of Theorem 3.16 satisfies
    [Psi_p]_{cos th} = -Abar/(p + 2) - a_2/(2p),   [Psi_p]_{sin th} = -b_2/(2p),
    (p/(1 - p)) J_p[A] -> -(1/2)(a_2 cos(th) + b_2 sin(th)) A'   uniformly as p -> 0.
This limit is identically zero if and only if a_2 = b_2 = 0. Thus the coefficient B_p = J_p[A]/(l - 1) has a nonzero
limit when the second mode is nonzero, whereas B_p = O_A(p) when that mode vanishes. For fixed r > 0 and A(th) != 0,
the ratio of the displayed correction r^{2p-1} B_p to r^p A tends to
    -(a_2 cos(th) + b_2 sin(th)) A'(th)/(2 r A(th)).
This is a fixed-A comparison of the displayed terms. Theorem 3.16 does not supply a remainder uniform in p, and the
comparison gives no lower bound uniform over radii tending to infinity or over varying families A_p.
For a profile in S^+, a positive level rho = m has radius R_m(th) = (m/A(th))^{1/p} in the coordinates of the
scattering map of Theorem 3.13, wherever A(th) > 0. In particular,
    R_m(th_1)/R_m(th_2) = (A(th_2)/A(th_1))^{c_l}.
There are directions with A(th_2) = 2 A(th_1) > 0, giving radius ratio 2^{c_l}. These fixed-A formulas and the exact
radius ratio describe possible anisotropy; no universal domain-size requirement is proved.
Complete proof: Section 9.15.
The limit problem. Under the hypotheses of Theorem 4.9(b) the limit (f, Y) := (f, b) solves
    (P0)  f in C^2, Y in C^1, Y.grad f = 0, div Y = 2, curl Y = -f_x, Y(0) = 0, Y - Z = o(|Z|) as |Z| -> infinity
          uniformly in direction, f = z_1^2 + o(|Z|^2) as Z -> 0.
(P0) is exactly the problem of a self-similar gradient blow-up of the IPM equation with bounded density,
varrho(z, t) = f((z - z_*(t))/(T - t)), with the centre moving with the fluid, for the canonical once-subtracted
velocity law of Section 2 (a spatially constant velocity is absorbed by the motion of the centre).
Proposition 4.12 (structure of (P0); proof outlined, not supplied in full). Let (f, Y) solve (P0).
(a) DY(0) = diag(0, 2), so c[f] = 1 is forced. The zero set E of Y is compact; each connected component of E with
more than one point is a compact embedded C^1 arc (no branching, crossing, closed curve or unbounded component); the
component through 0 is such an arc, with f > 0 on it near 0 except at 0. Further arcs, single-point components and
accumulation of distinct components are neither excluded nor constructed. On an arc with unit tangent t, normal n and
F = f along the arc, DY has the matrix [[0, f_x], [0, 2]] in the frame (t, n), and grad f = F' t - (1/2) f_x F' n; in
particular F' = 0 exactly where grad f = 0.
(b) At an endpoint e of an arc, Df(e) = 0 and D^2 f(e) = 0; if f is C^k, all derivatives of f of orders 1 through k
vanish at e. (This does not make f locally constant near e.)
(c) grad P = Y + f e_2 defines a global P, and L = P - y f satisfies Y.grad L = |Y|^2 with L = r^2/2 + o(r^2) as
r -> infinity. Every backward orbit converges to a single point pi(Z) of E, and f(Z) = f(pi(Z)). The interior of the
set of points whose backward limit is a given equilibrium e is, if nonempty, unbounded with infinite area; there
f = f(e) and the velocity w = Y - Z is a gradient.
(d) |grad f| <= C/(1 + r); the velocity is the canonical one, w = W[f], and w = C_A log r + B(th) + d + o(1) with
C_A = (b_2/2, -a_2/2), where a_2, b_2 are the second Fourier coefficients of the angular limit A; f = A(th) + O(log
r/r) with A in C^1 nonconstant; f is not exactly homogeneous of degree 0 outside any disk.
(e) min f = min_E f = min A and max f = max_E f = max A.
Proof idea. (a) tr DY = 2 at every equilibrium gives a component of Y with nonzero differential, whose zero set is a
local C^1 graph containing E; a closed component is excluded by 0 = int_{boundary} Y.n = 2 |interior|; on the central
nullcline f_x = 2x + o(x) and transport force Y_1 = 0. (b) At a regular equilibrium, coordinates (f, eta) and
div Y = 2 give a tangential derivative 2 and equilibria on both density sides, so arcs cannot end there; at an
endpoint with D^2 f(e) != 0 the quadratic part is a u^2, which again continues the arc. (c) curl(Y + f e_2) = 0; along
a backward orbit L decreases with int |Y|^2 dt finite, and in a straightened chart of an arc v decays exponentially
backward while the tangential drift is O(|v|), which traps the orbit. (d) The orbit angle map is a C^1 circle map by
div Y = 2, which gives the gradient bound, then a logarithmic bound on the canonical integral and harmonic uniqueness,
and then the explicit resonant stream r log r Q + r Psi. (e) Regular level components are proper lines with one
equilibrium; approximate the extrema by regular values.
Existence for (P0) remains open. Proposition 4.12, whose proof is only outlined, asserts that the equilibrium set E is
compact and each component with more than one point is a compact embedded C^1 arc; it does not exclude single-point
components or accumulation of components. At arc endpoints it asserts Df = D^2 f = 0, and, if f is C^k, vanishing of
derivatives of orders 1 through k. It also asserts constant density on nonempty interiors of backward basins and a
possible logarithmic far-field term. These assertions require complete proofs before being used as established
structure. The exact anisotropy comparison of Remark 4.11 is a separate result proved in Section 9.15.
Remark 4.13 (a weighted balance at finite c_l). For a profile in S, grad P = V + rho e_2 is a gradient, L = P - y rho
satisfies V.grad L = |V|^2 - y rho and L = (c_l/2) r^2 + o(r^2) as r -> infinity, so for every lambda > 0
    int e^{-lambda L} (|V|^2 - y rho) dX = (2 c_l / lambda) int e^{-lambda L} dX > 0.
The integrand has no sign (not even in S^+, where rho >= 0), so this gives no bound on c_l.
Proposition 4.13a (positive-density bounds and endpoint angular tests; complete proof in Section 9.12). Let rho in S^+
(so rho >= 0, Theorem 3.2) and p = 1/l.
(a) For every radial envelope 0 <= rho(r, th) <= M(r), l - 1/2 <= (2/pi) int_0^inf M(r) r^{-2} dr. Hence rho <= H r^2
for r <= 1 and rho <= C r^gamma for r >= 1, with 0 < gamma < 1, imply 1/gamma <= l <= 1/2 + (2/pi)(H + C/(1 - gamma))
(the envelope bound of 4.7, which holds in S without a sign of rho, has the constant 4/pi; rho >= 0 halves it).
(b) H_2 := sup_{X != 0} rho(X)/|X|^2 and C_p := sup_{X != 0} rho(X)/|X|^p are finite and positive, H_2 >= 1, and
H_2^(1 - p) C_p >= (pi (l - 1)/4)^(2 - p). Consequently H_2 <= H and C_p <= C imply l <= 1 + (4/pi) max(C, sqrt(H C)),
and along a sequence of such profiles with l_n -> infinity and H_2(rho_n) <= H, liminf
C_{p_n}(rho_n)/l_n^2 >= pi^2/(16 H). These are bounds on the whole density, not on max A alone.
(c) (Formulas for a given angular function, not for profiles.) Write A = a_0 + sum_{n >= 1} (a_n cos n th + b_n sin n
th). The periodic stream coefficient of Theorem 3.16 has [Psi_p]_cos 2th = a_3/(2(1 - p)) - a_1/(2(p + 3)) and
[Psi_p]_sin 2th = b_3/(2(1 - p)) - b_1/(2(p + 3)). For fixed nonnegative A in C^2 with exactly two zeros, both
positive quadratic, and (a_3, b_3) != (0, 0), put eps = 1 - p and P_3 = a_3 cos 2th + b_3 sin 2th; then, uniformly in
th as p -> 1, B_p := J_p[A]/(l - 1) = (2 P_3 A' - P_3' A)/(2 eps^2) + O(1/eps), and 2 P_3 A' - P_3' A is not
identically zero. So for a fixed angular function with a nonzero third mode ||B_p||_inf is comparable to eps^{-2},
while along the sequences of Corollary 4.8 (whose hypotheses force the third mode of A_n/M_n to be O(eps_n),
eps_n = 1 - p_n) the normalised quantity ||B_n||_inf/M_n^2 is comparable to eps_n^{-1} (c_n -> 1/2); no bound of that
order for ||B_n||_inf itself follows without control of M_n. The function
A_f = cos^2 th (1 + 16 sin^6 th) = 9/8 - cos 4th/2 + cos 6th/2 - cos 8th/8 has exactly two zeros, at pi/2 and 3pi/2,
both quadratic with A_f(pi/2 + t) = 17 t^2 + O(t^4), no modes 1, 2 or 3, and Psi_p[A_f] bounded uniformly for
0 < p < 1. This is angular compatibility only, not the construction of a profile.
(d) (A restricted gap.) Let A_0 = cos^2 th, Psi_ref = -5 cos th/12 - cos 3th/20 (the stream coefficient of A_0 at
p = 1, 4.7(iii)), m = max A and ||f||_{C^1} = max(sup |f|, sup |f'|). For every K > 0 there is no profile in S^+ with
1 < l < min(100/99, 1 + 1/(4K)) whose angular coefficient satisfies ||A/m - A_0||_{C^1} <= 1/100,
||Psi_p[A]/m - Psi_ref||_{C^1} <= 1/100 and ||B_p||_inf/m^2 <= K (B_p = J_p[A]/(l - 1), the coefficient of the forced
correction of
Theorem 3.16).
None of (a)-(d) excludes an interval of l for unrestricted S^+; (d) is a restricted exclusion only.
None of 4.9-4.13a bounds c_l over S or constructs a profile. The convergence hypotheses of Theorem 4.9, its far-field
condition in (b) and the uniform bounds of Corollary 4.10 are additional hypotheses, not derived here for general
profiles in S. Proposition 4.12 concerns the limit problem.

4.14 Strain carried by the near-node core (local and conditional statements). Parts (a)-(e) concern comparison
densities or local stationary x-even models with m1 = 1/2 exactly (the horizontal node eigenvalue is then exactly 1/2,
which the eigenfunction equation below requires); part (f) reports finite-radius diagnostics for nearby numerical
states of the forward reformulation (5.8), which have m1 close to but not equal to 1/2 and at which the up-down
asymmetry D of 5.8(iv) is the quantity that would have to vanish. Write G_+ and G_- for the node coefficients on the
upper and lower sides of the weak axis: on each side xi = x(1 + alpha_+- y + ...) solves V.grad xi = xi/2 and
rho = G_+- xi^2 (so rho/x^2 = G_+- (1 + 2 alpha_+- y + ...)), and D = log(G_-/G_+). Put Delta = G_+ - G_-,
Sigma = G_+ + G_-, Gbar = Sigma/2, n = 2l - 1/2, K = 14/(15 pi) and c_<R = (1/pi) int_{r<R} rho r^{-3} sin 3th dX, so
that c = psi_xy(0) = c_<R + c_>=R.
(a) Flat half-discs. For rho = G_+ x^2 on {y > 0, r < R} and G_- x^2 on {y < 0, r < R}, c_<R = K Delta R exactly
    (int_0^pi cos^2 th sin 3th dth = 14/15).
(b) Separatrix and velocity. Suppose the separatrix of the node is y = kappa x^2 + o(x^2) and V has the one-sided
    quadratic expansion compatible with the Poisson equation, V_1 = x/2 + a x y + Delta x|y|, V_2 = n y + b x^2 - a
    y^2/2 - Delta y|y|/2 with b = a/2 - Gbar. Then alpha_+- = -(a +- Delta)/n and kappa = (Gbar - a/2)/(n - 1). The
    isolated contribution of the comparison density G_+- x^2 cut by the separatrix is K Delta R - Delta kappa^2
    R^3/pi + o(R^3) (there is no term linear in kappa). If in addition the density remainder is o(r^3) in the
    angularly weighted sense, including the transition region between the core and the outer field (the velocity
    expansion does not supply this), then c_<R = K Delta R - (a Sigma + Delta^2) R^2/(8n) + o(R^2); for a smooth core
    (G_+ = G_- = G) this is G alpha R^2/4 + o(R^2).
(c) Size of the flat mismatch term. From (b), Gbar = (n - 1) kappa - (n/2)(alpha_+ + alpha_-)/2, and |Delta| = Sigma
    |tanh(D/2)|.
    Hence, if G_+- > 0, n >= 1 and |kappa| R, |alpha_+-| R <= eps, then Gbar R <= (3n/2 - 1) eps and
    K |Delta| R <= 2K (3n/2 - 1) |tanh(D/2)| eps. The hypothesis caps Gbar R, so the flat term is O(eps) for every D;
    D -> 0 adds only the factor |tanh(D/2)|. This does not show that the core strain c_<R vanishes as D -> 0: at D = 0
    the smooth term G alpha R^2/4 remains (bounded by (3n/2 - 1) eps^2/4), and the higher remainders are not uniformly
    controlled.
(d) Comparison bound. With rho_flat = G_+- x^2 on the two sides and E_R = (1/pi) int_{r<R} |rho - rho_flat| r^{-3}
    |sin 3th| dX, |c_<R - K G_+ (1 - e^D) R| <= E_R; and if |rho| <= C r^gamma for r >= L with gamma < 1,
    |c_>=L| <= 4C L^{gamma - 1}/(pi (1 - gamma)).
    Write c_(R,L) for the part of c from R <= r < L. Along a sequence with E_R -> 0 at fixed R and G_+ |1 - e^D| -> 0
    (for example D -> 0 with G_+ bounded) one gets c_<R -> 0, so that c = l - 1/2 (> 1/2 at m1 = 1/2) must be carried
    by c_(R,L) and c_>=L. D -> 0 alone does not suffice: a growing node coefficient can keep a nonzero flat mismatch
    contribution (G_+ = j, G_- = j - 1 in the comparison model gives D -> 0, E_R = 0 and c_<R = K R). No control of
    E_R is available.
(e) No local obstruction at D = 0. rho = G x^2, psi = c x y - G x^3/3 with c = l - 1/2 solves -Delta psi = d_x rho and
    V.grad rho = rho for V = (x/2, n y - G x^2); eta = y - G x^2/(n - 1) satisfies V.grad eta = n eta, and
    eta/|x|^{2n} is invariant. The open part is global: an exterior density that supplies this interior field and
    solves its own exit-map equation.
(f) Numerical reading. On the six-mode family state at a_2 = -1.228 (eta13 = 0.0802 in 5.8(vi)), splitting c by the
    exit angle of the orbit through each point at frozen velocity: the core log r < -10 carries 0.374, entirely
    through orbits that exit next to the zeros of A (upper +0.716, lower -0.342); the band -10 < log r < -6 carries
    2.013 (orbits exiting in the bulk 1.53, next to the zeros 0.48). Two independent codes agree to 0.03 in the split
    and 6e-3 in the totals. Off m1 = 1/2 the node limits defining G_+- in (a)-(e) change character, so here G_+- (R)
    denotes the median of rho/x^2 over the ring r = R, |cos th| > 1/2, on the upper and lower side, and Gbar R = (G_+
    (R) + G_- (R)) R/2. On the family states Gbar R at R = e^t for t = -13, -12, -11, -10 is 0.07, 0.19, 0.52, 1.35
    (a_2 = -1.1), 0.25, 0.68, 1.76, 3.72 (a_2 = -1.228, eta13 = 0.0802) and 0.69, 1.82, 3.93, 7.36 (a_2 = -1.3).
    Neglecting a and estimating |kappa| R by Gbar R/(n - 1) gives the indicative radii log R of about -11.2, -12.5 and
    -13.5 below which |kappa| R <= 0.1; the full hypotheses of (c) have not been checked, because alpha_+- were not
    measured. Under this approximation the estimated radius decreases along these three states, over which D rises
    from -0.31 to about -0.25 and then stays level; with the nonmonotonicity and convergence limits of 5.8(vi) this is
    not an established trend along a branch.
None of (a)-(f) is a nonexistence argument; (a), (b) and (e) are local identities, (c) and (d) are conditional
bounds and (f) is a reading of data.

4.15 Singular limits of the x-even family (local and conditional statements). Use the notation of 4.14; d = 1 - e^D,
so d ~ |D| as D -> 0 from below. The sampled finite-radius values Gbar R of 4.14(f) increase along the sampled states
a_2 = -1.1, -1.228, -1.3, over which D rises from -0.31 to about -0.25 and then stays level. They do not establish a
trend of limiting node coefficients along a branch. Parts (a)-(i) discuss possible limiting behavior; part (j) reports
numerical observations. No limit with D -> 0 is established.
(a) Circulation bound for a perturbative core. If on the square [R/4, R/2]^2 one has |rho/(G x^2) - 1| <= 1/5 on the
    two vertical sides and |V - diag(1/2, n) X| <= eps R on the boundary, then G R <= 32 eps. (curl V = -d_x rho; on
    each horizontal segment rho(R/2, y) - rho(R/4, y) >= G R^2/8, so the circulation is at least G R^3/32, and the
    linear field is a gradient, so the hypothesis bounds the circulation by eps R^2.) A uniformly perturbative
    quadratic core therefore carries flat mismatch strain K G d R <= 32 K eps d, which tends to 0 with d. This
    excludes a persistent flat mismatch strain in such a core; it does not bound the deformation part of the core
    strain, and it does not show that a transition region at R ~ 1/G exists.
(b) Core velocity. The two flat half-discs of 4.14(a) give U(0) = (0, Sigma R^2/16) (kernel cos 2th/(2 pi r^2) for
    U_2, int_0^pi cos^2 th cos 2th dth = pi/4), of order G R^2 rather than G R^3. Anchoring subtracts this, so a small
    core mass alone does not decouple the core from the anchored outer velocity.
(c) Matching law (conditional). Let a_* = max_th rho(r, th)/r^p in the far field, L = a_*^{1/(1-p)} (the radius at
    which a_* r^p = r) and Q = log(G_+ L). Suppose that a core of radius R_c carries strain kappa_c ~ K G_+ d R_c with
    kappa_c -> kappa_0 > 0, that it matches an outer cusp H|x|^g at R_c (G_+ R_c^2 ~ H R_c^g), and that h = H L^{g-1}
    tends to h_0 > 0. With s = R_c/L, e^Q ~ h s^{g-2} and d ~ (kappa_c/(K h)) s^{1-g}. In the shrinking-core limit
    s -> 0, d -> 0 at fixed g this forces g < 1 and Q = -((2-g)/(1-g)) log d + O(1), so a slope magnitude a of Q
    against log d corresponds to g = (a-2)/(a-1); the O(1) remainder does not make the slope converge, and without
    s -> 0 the two relations also admit g > 1. Without the matching hypotheses: if c_<R_c >= kappa_0 and
    E_{R_c} <= kappa_0/2 (E_R as in 4.14(d)), then Q >= log(kappa_0/(2K)) - log d - log s, and if moreover e^Q
    s^{2-g} <= h_1 with 0 < g < 1, then Q >= ((2-g)/(1-g)) log(kappa_0/(2K d)) - log(h_1)/(1-g).
(d) Cusp strain. Half-annuli H_+ |x|^g (y > 0) and H_- |x|^g (y < 0) on R_c < r < R_0 carry
    c = K_g (H_+ - H_-) (R_0^{g-1} - R_c^{g-1})/(g - 1) (with log(R_0/R_c) for the last factor at g = 1),
    K_g = 2(3g + 1)/(pi (g + 1)(g + 3)), K_2 = K. Hence a limit with an outer cusp H_+- |x|^g, 0 < g <= 1, at the node
    and a finite circular strain has H_+ = H_- (otherwise the strain diverges with a fixed sign as R_c -> 0). At g = 1
    (heuristic) a persistent strain needs log(R_0/R_c) of order 1/(H d), so Q grows like 1/d.
(e) Limits (conditional). (i) Let stationary states with l_j -> l > 1 satisfy a common bound |rho_j| <= C
    (1 + r)^gamma, gamma < 1, rho_j(0) = 0 and common local Holder bounds including the origin, and converge locally
    uniformly. Then the limit solves div(rho (l X + W[rho])) = (1 + 2l) rho in distributions, with W the anchored
    velocity (the subtraction U - U(0) kept inside the kernel; U_j(0) need not exist separately). Growth bounds alone
    do not give this.
    (ii) If the limit has a finite circular strain c_out, and m1_inf = lim_j m1_j and the iterated limit below exist,
    the strain defect kappa := lim_{R -> 0} lim_j c_{j,<R} equals l - m1_inf - c_out (c_j = l_j - m1_j for x-even
    states; stationarity alone does not fix m1_inf); under the additional normalization m1_j -> 1/2, that is
    c_j -> l - 1/2, this is l - 1/2 - c_out.
    This is an iterated limit: core strains measured at radii R_j -> 0 need not converge to it unless the shrinking
    annuli in between are controlled.
    (iii) If the limit has a regular root, rho = H |xi|^g with V.grad xi = xi/g and xi = x + O(r^2), and W_1 = -c_out
    x + o(r) on the horizontal axis, then 1/g = l - c_out; under the normalization m1_j -> 1/2 of (ii) this is
    1/2 + kappa, and then kappa = 0 gives g = 2.
    Identifying this horizontal derivative with the circular strain is a hypothesis; DV(0) need not exist.
(f) Rigidity of x-even regular-root power profiles (conditional; proof outlined). Let rho = H |xi|^g globally with
    0 < g < 2, V.grad xi = xi/g, xi in C^3 and odd in x with D xi(0) = e_x, V continuous, anchored and C^1 off the
    zero set of xi (the distributional div-curl equations imply this), and W = o(r) along the y-axis. Then xi_x = 1 on
    the whole y-axis and l = 1/g, so g = p; with the identification of (e)(iii), c_out = 0 and all of c = l - 1/2 sits
    in the defect.
    Proof idea: in coordinates (t, s) with t = xi and unit Jacobian, V = (t/g) X_t + (beta s + b(t)) X_s with
    beta = 2l - 1/g (from div V = 2l); the curl equation gives |X_s|^2 b'(t) + R(t, s) = -H g sgn(t) |t|^{g-1} xi_x
    with R = O(|t|) (from the oddness of the terms of the inverse chart x = chi(t, y), which is C^3), and dividing by
    |t|^{g-1} and letting t -> 0, which is possible since g < 2, shows that xi_x/|grad xi|^2 is constant along the
    zero segment; on the axis xi_y = 0 by oddness, so xi_x = 1, V_2(0, y) = beta y and W_2(0, y) = (l - 1/g) y, which
    W = o(r) forces to vanish. The statement concerns the zero component through the origin; it does not exclude other
    zero components and does not show that the profile is layered. For 1 <= g < 2 it gives l <= 1, which is not
    admissible: there is no x-even solution of this form with a C^3 odd regular root, W = o(r) on the axis and l > 1.
    No estimate is known that forces a C^3 root (rho = H|xi|^g is only C^{1,g-1} across the axis for 1 < g < 2, so the
    regularity of rho does not give it; the layers of (g) have xi = x). For 1 < g < 2 a formal root xi = a(y) x + d(y)
    x|x|^g + ..., which is C^{2,g-1} and not C^3, satisfies the local equations at the two leading orders in x with
    a' != 0 when d != 0 (d = 0 on an interval forces a' = 0 there); whether such roots occur in a global solution is
    open. At g = 2 the argument gives nothing (the remainder and the source are of the same order). At g = 1 the layer
    rho = H|x|, V = (x, y - H|x|) solves the equations with l = 1 and W of linear growth, outside S; its angular pair
    A = H|cos th|, Psi = -(H/2) cos th |cos th| satisfies both angular equations of Proposition 4.7 (the first in the
    sense of distributions), but A is not C^1 at its (linear) zeros, so the C^2 / quadratic-zero hypothesis there
    cannot be dropped. A branch of x-even solutions of the jet-order problem of (h) (datum |cos th|^g e^F, m1 = 1/g)
    that agrees with the layered diagonal p = g for g < 1 and enters g > 1 with p < 1 cannot be C^1 in g at g = 1;
    this uses only p < 1 and does not exclude a corner, a singular parametrisation or a separate branch approaching
    (1, 1).
(g) Layered solutions. For 0 < g < 1, rho = H |x|^g with W = (0, -H |x|^g) and l = 1/g is an exact stationary state
    with the canonical velocity (the stream function depends on x only). It is not C^1 and lies outside S. DV(0) does
    not exist (eta = y - H |x|^g/(l - 1) satisfies V.grad eta = l eta), and c = 0 only as a horizontal derivative or
    circularly regularised strain; the absolutely convergent strain formula does not apply. By (f), a regular-root
    x-even cusp limit of a family with p = 1/l has the exponent g = p of these solutions; whether the family of
    5.8(vi) approaches such a limit is not known.
(h) Generalised axis law (conditional). Under the hypotheses of 5.8(v) with the transverse order 2 replaced by k, that
    is rho(x, +-r) = h_+-(r) |x|^k + o(|x|^k) on the two half-axes (r > 0), with B_+- as in 5.8(v) and node exponents
    m1 and n = 2l - m1: d/dr log(h_+-/B_+-^k) = (1 - 2kl)/B_+-, and
        log(C_-/C_+) = log(A_-/A_+) + (2kl - 1) J,   J = int_0^inf (1/B_- - 1/B_+) dr = 2 int_0^inf w_e/(B_+ B_-) dr,
    where C_-/C_+ and A_-/A_+ are the limits of h_-/h_+ at the node and at infinity. At k = 2, m1 = 1/2 this is 5.8(v)
    (2kl - 1 = 2n). Power matching at the node gives the exponent (1 - k m1)/n for the node coefficient, so a finite
    positive coefficient needs k = 1/m1. For the jet-order problem in which the datum is |cos th|^q e^F and the
    condition is m1 = 1/q, the coefficient of J is 2ql - 1 = q n (that of int w_e/(B_+ B_-) is 2 q n). No sign follows
    from these relations.
(i) Moment law with inner flux. For phi = r^{-3} sin 3th put N_eps = int_{r > eps} rho W.grad phi dX and
    B_eps = eps^{-2} int_0^{2 pi} rho(eps, th) V_r(eps, th) sin 3th dth. For a stationary state with vanishing outer
    flux and finite circular strain c, lim_{eps -> 0} (N_eps + B_eps) = pi (l - 1) c, which is pi c (c - 1/2) of
    Theorem C when l = 1/2 + c. Here I_eps = int_{r > eps} rho r^{-3} sin 3th dX, and finite circular strain c means
    I_eps -> pi c as eps -> 0. Since V.grad rho = rho, div V = 2l and X.grad phi = -3 phi,
    div(rho phi V) = (1 - l) rho phi + rho W.grad phi; integrating over eps < r < R and letting R -> infinity
    (vanishing outer flux) gives N_eps + B_eps = (l - 1) I_eps, which proves the limit.
    Under the local bounds rho = O(r^g), W = O(r) with g > 1, B_eps = O(eps^{g-1}) -> 0. For the layers of (g),
    B_eps = -H^2 C_g eps^{2g-2} and N_eps = H^2 C_g eps^{2g-2} with C_g = (6g/(g + 2)) B(3/2, g + 1/2) > 0
    (C_1 = pi/4): both diverge and cancel exactly. In a singular limit the inner flux cannot be dropped; dropping it
    produces a false obstruction.
(j) Numerical reading. On the six-mode family states of 5.8(vi) at a_2 = -1.1, -1.2, -1.228 (eta13 = 0.0802), -1.25
    and -1.3 (512 angles) the local exponent sigma = d log rho/d log r on the ray th = 0 falls from 2 to about 0.6
    between log r of about -12 and -3.5, monotonically to within 0.03 and with slope about -0.15 per unit of log r on
    [-8, -4], has a minimum between -0.02 and 0.11 at log r between -1.74 and -1.50, and is within 0.05 of p for log r
    above about -0.1. Its crossings of the levels 1.9, 1.0 and 0.6 lie at log r = -10.09, -11.00, -11.20, -11.50,
    -12.06; -5.84, -6.45, -6.59, -6.79, -7.18; and -3.54, -3.82, -3.90, -3.96, -4.11 (same order of states): along the
    family the inner end of the crossover moves inward by 2.0 and the outer end by 0.6. Between the crossings of 1.9
    and 0.6, the smallest range (maximum minus minimum) of sigma over a window of unit width in log r is 0.157, 0.136,
    0.133, 0.126 and 0.115 (same order), so no intermediate exponent plateau with range below 0.11 is resolved and
    these states show no intermediate range rho ~ H r^g on that ray, and the matching law (c) with a fixed g has no
    support at these parameters. Two codes (node differences, and exact differentiation of panel interpolants) agree
    on the crossings to 0.01 in log r; 1024 angles move them by at most 0.02 and an inner radius e^-17 by at most
    0.01. Off the ray, sigma has negative minima in log r between -3 and -2 at every tested angle from 30 to 85 deg.
None of (a)-(j) establishes nonexistence for all of S. Parts (a), (b), (d), (g) and (i) give the stated bounds or
identities; (i) retains its integrability hypotheses and the g = 1 remark in (d) is heuristic. Parts (c), (e) and (h)
retain their additional hypotheses; (j) describes sampled data. Part (f) is a restricted exclusion with only an
outline supplied: it asserts l = 1/g under its global regular-root and velocity hypotheses, hence excludes
1 <= g < 2 when l > 1. The circulation bound (a) rules out a persistent flat mismatch contribution as D -> 0 in a
uniformly perturbative quadratic core. It does not control the full core strain or prove that such a limit exists.

4.16 Scattering-domain inertia and distribution functions (proved necessary conditions in S^+ and density tests;
none gives nonexistence). In (a)-(c), rho is a profile in S^+, l = c_l > 1, p = 1/l, and S is the map of Theorem 3.13.
Set F = r^p A(theta), D_R = S^{-1}(B_R), a_j = A''(beta_j)/2 > 0 at the two zeros of A, and C_A = sum_j a_j^{-1/2}
(a positive scalar, unrelated to the vector C_A of Proposition 4.12(d)).
Let Psi solve Psi''+(p+1)^2 Psi = sin(theta) A'-p cos(theta) A periodically,
H = r^p(-Psi' e_r+(p+1)Psi e_theta), and E_A = int_0^{2pi}(Psi')^2 dtheta.
(a) For I(R) = int_{D_R}|X|^2 dX and Q(R) = int_{D_R}X.W dX, one has E_A > 0 and, for every R > 0,
|D_R| = pi R^2, I(R) >= pi R^4/2, and l R I'(R) = 4l I(R)+2Q(R).
As R->infinity, I(R)-pi R^4/2 = E_A R^{2p+2}/(l-1)^2+o(R^{2p+2}),
and Q(R) = -E_A R^{2p+2}/(l-1)+o(R^{2p+2}).
For large R, D_R is star-shaped with radius s_R(theta) = R+R^p Psi'(theta)/(l-1)+o(R^p), uniformly,
and exactly I(R)-pi R^4/2 = (1/4)int_0^{2pi}(s_R^2-R^2)^2 dtheta.
For the pressure W = -grad P-rho e_2, Q(R) = 2int_{D_R}P-int_{boundary D_R}P X.n-int_{D_R}y rho.
Its homogeneous term is P_H = r^{p+1}(Psi'-A sin(theta))/(p+1), with H = -grad P_H-F e_2.
The coefficients obey the material identity because lp = 1; the pressure formula gives the same work.
No estimate Q(R) >= 0 or I(R)-pi R^4/2 = o(R^{2p+2}) has been proved.
(b) For fixed 0 < a < b < infinity and Omega_R equal to either D_R or B_R,
|{a < rho < b} intersect Omega_R| = 2C_A(sqrt(b)-sqrt(a))R^{2-p/2}/(2-p/2)+o(R^{2-p/2}).
For every measurable g:[0,infinity)->[0,infinity] with int_0^infinity g(t)t^{2/p-1}dt > 0,
int_{R^2}g(rho)dX = infinity. For every R > 0 and q > -1/2,
int_{D_R}rho^q dX = R^{2+pq}int_0^{2pi}A^q dtheta/(2+pq).
For q <= -1/2 this integral diverges locally along Gamma = {xi = 0}, where rho = xi^2.
Exactly, int_{Gamma intersect D_R}|grad xi|^{-1}ds = C_A R^{2-p/2}/(2-p/2).
Thus nonzero nonnegative continuous functions of rho cannot give finite whole-plane Casimirs.
(c) Let zeta be C^2 with compact support in an annulus avoiding 0, and G in C^1([0,infinity)).
For L_R = int zeta(X/R)[G(rho(X)/R^p)-G(F(X)/R^p)]dX,
lim_{R->infinity}R^{-p-1}L_R = (l-1)^{-1}int zeta G'(F)H.grad F = -(l-1)^{-1}int G(F)H.grad zeta. The equality is
integration by parts using div H = 0.
This yields no additional angular condition. Removing the cutoff is unjustified for the positive Casimirs above;
no contradiction from a defined higher-order renormalization has been proved.
(d) (density tests only). For M >= 0, let rho_M = x^2(1+r^2)^{-3/4}[1+M y^6/(1+r^2)^3].
These densities belong to S, are even in both variables, and are positive exactly off the vertical axis.
Their canonical streams satisfy grad-perp psi_M = W[rho_M], psi_M(0,y) = 0, and
psi_M(r,0) = r^{3/2}Psi_M(0)+O(r), with Psi_0(0) = -34/45 and Psi_100(0) = 148474/255255.
Their angular densities A_M = cos^2(theta)[1+M sin^6(theta)] have precisely two positive quadratic zeros.
Moreover (rho_0)_x = x(1+r^2)^{-7/4}[2+x^2/2+2y^2] > 0 on x > 0.
Nevertheless c = 0, DW(0) = 0, and (2X+W).grad rho_M-rho_M = 3x^2+O(r^3); none is a profile.
For each fixed M, small jet-preserving scalings rho_{M,L} = L^2 rho_M(X/L) also give V = 2X+W only one zero.
These tests refute a stream sign from positivity, the wall and canonical growth alone; rho_0 also refutes
the inference -Lap psi > 0 and zero wall data imply psi >= 0 under this growth. They do not exclude profiles.
Complete proof: Section 9.11.
4.17 Odd perturbations of an x-even profile (proved statements about the linearisation at a hypothetical profile in
S^+_even; none decides whether profiles in S^+ are x-even). Let rho_0 be in S^+_even, l = c_l > 1, p = 1/l,
V_0 = lX + W[rho_0] with flow Phi_s, and rho_0 = xi^2 with xi the signed root of Theorem 3.2, taken positive on x > 0
(by Theorem 3.3, Gamma is the y-axis and xi is odd in x). Put R(x, y) = (-x, y). For rho_0 + eps h and l + eps lambda
the profile residual has the derivative Lh + lambda X.grad rho_0, where Lh = V_0.grad h + W[h].grad rho_0 - h and W is
the canonical law of Section 2. Since W[h o R] = R W[h] o R, L maps x-odd functions to x-odd functions; for x-odd h
the term lambda X.grad rho_0, which is x-even, must vanish separately, so lambda = 0 in the x-odd part
of the linearised problem. The growth class below is: h in C^3(R^2), h = O(r^3) at 0, and |h(X)| <= C(1 + |X|)^mu,
|grad h(X)| <= C(1 + |X|)^{mu-1} for some 0 <= mu < 1. For such h, c[h] and d[h] denote the values of psi_xy(0) and
psi_yy(0) for the stream function of W[h], so that DW[h](0) = [[-c[h], -d[h]], [-d[h], c[h]]].
(a) For x-odd h in the growth class, c[h] = 0 and d[h] = -(1/pi) int h r^{-3} cos 3th dX (an absolutely convergent
integral); the variations of c = psi_xy(0) and of m1 vanish, while that of psi_yy(0) is d[h]. Moreover
Lh = -2 d[h] xy + O(r^3) at 0. Hence Lh = 0 implies d[h] = 0: in this direct formulation the orientation condition
psi_yy(0) = 0 is the second-order Taylor coefficient of the linearised equation, not a further condition on its
solutions.
(b) (reflection comparison). For chi(s) = exp(-1/((s - 1)(2 - s))) on 1 < s < 2 and chi = 0 otherwise, the function
h = chi(r) cos^3 th (1 + 4 sin^2 th) = chi(r)(5 cos th - cos 5th)/4 is smooth, x-odd and nonnegative on x > 0, with
c[h] = d[h] = 0. For r > 2 its canonical velocity has the polar components
W[h]_r = -D_1 r^{-3} sin 2th - D_5 r^{-7} sin 6th and W[h]_th = D_1 r^{-3} cos 2th + D_5 r^{-7} cos 6th, with
D_1 = (5/4) int_1^2 s^2 chi ds > 0 and D_5 = -(3/4) int_1^2 s^6 chi ds < 0. On the ray th = -pi/4 this velocity is
radial and outward, on th = pi/4 radial and inward. There h vanishes with all its derivatives for r > 2, and
-Lh = -W[h].grad rho_0 is negative on the first ray and positive on the second for large r. For small eps > 0,
rho_0 + eps h and rho_0 - eps h are nonnegative, have the jet x^2, the growth of S and the strain moments of rho_0,
and lX + W[rho_0 +- eps h] has no zero besides 0; they are not profiles. Thus the pointwise positive minimum principle
for -L on x-odd functions fails even under these constraints: h >= 0 on x > 0 and h(X) = 0 at a point X with x > 0 do
not imply -Lh(X) >= 0, and the other ray shows that they do not imply -Lh(X) <= 0 either. This does not decide
a comparison theorem that assumes a sign of the residual throughout the half plane, or one restricted to stationary
solutions.
(c) (Fredholm property). Fix p < mu < 1 and <X> = (1 + |X|^2)^{1/2}. Let X_mu be the C^1 functions on R^2 that are C^3
on the closed disc B_2, with zero two-jet at 0 and finite norm
||h||_{C^3(B_2)} + sup <X>^{-mu}|h| + sup <X>^{1-mu}|Dh|, let Y_mu be the continuous functions that are C^2 on
the closed disc B_1, with norm ||f||_{C^2(B_1)} + sup <X>^{-mu}|f|, and let X_mu^odd and Y_mu^odd be their x-odd
subspaces. The residual map (h, lambda) -> ((l + lambda)X + W[rho_0 + h]).grad(rho_0 + h) - rho_0 - h is a polynomial
of degree two from X_mu x R to Y_mu, hence C^1, and commutes with the reflection; its derivative at (0, 0) on x-odd
directions is L: X_mu^odd -> Y_mu^odd. This L is bounded and is not Fredholm; neither is its restriction to
{d[h] = 0}, nor the map h -> (Lh, d[h]). An explicit sequence: for X_0 in x > 0 with 0 < |X_0| < 1/2, e a unit vector
orthogonal to V_0(X_0) and zeta a smooth cutoff supported in the unit disc and equal to 1 near 0,
f_n = n^{-3} zeta(n^{1/2}(X - X_0)) sin(n e.(X - X_0)) and h_n = f_n - f_n o R are bounded above and below in X_mu,
have no convergent subsequence, and ||Lh_n||_{Y_mu} -> 0 (oscillation across the flow, on which the transport part is
small). The count of unknowns and conditions of Section 5.8 (index 0 for x-even data, -1 in the full class) is
therefore not a theorem in this realization; a realization with different control along and across the flow, or one
built on the forward formulation, is not constructed.
(d) (conditional rigidity). Let H be a C^1 map between Banach spaces U and Z, each with a bounded linear involution
(the reflection), with H equivariant and H(u_0) = 0 at a reflection-invariant u_0. If ||w||_U <= C ||DH(u_0) w|| for
every reflection-odd w in U (no surjectivity is needed), then every zero of H in a small U-neighbourhood of u_0 is
reflection-invariant. A trivial odd kernel alone does not give this estimate, and by (c) the estimate fails for
the residual map of (c). No realization with this estimate is established here, so this argument does not reduce
the parity-free search to x-even data, even near an x-even profile.
(e) (the remaining step). Let h be an x-odd solution of Lh = 0 in the growth class with p < mu < 1. Then
eta = h/(2 xi) extends to a C^1 function, even in x, with eta = O(r^2) at 0, and (V_0.grad - 1/2) eta = -W[h].grad xi.
For a prescribed continuous field v with v = O(r^2) at 0, there is exactly one continuous eta with eta = O(r^2) at 0
that is differentiable along the flow and satisfies d/dt eta(Phi_t X) = eta(Phi_t X)/2 - (v.grad xi)(Phi_t X), namely
eta(X) = -int_{-inf}^0 e^{-s/2} (v.grad xi)(Phi_s X) ds; full spatial C^1 regularity is not asserted for arbitrary
continuous v. Let E_mu be the set of x-even C^1 functions eta with eta = O(r^2) at 0 such that h = 2 xi eta is in
the growth class with exponent mu and d[h] = 0, and for eta in E_mu put
B eta(X) = int_{-inf}^0 e^{-s/2} (W[2 xi eta].grad xi)(Phi_s X) ds (convergent, since c[h] = d[h] = 0 gives
W[h] = O(r^2) at 0). An x-odd kernel element in the growth class gives eta in E_mu with eta = -B eta; conversely, if
eta in E_mu satisfies eta = -B eta, then L(2 xi eta) = 0. Whether such a nonzero eta, equivalently a nonzero x-odd
kernel element, exists is open: no bounded action of B on an invariant Banach space and no estimate sufficient to
settle the equation is established, and uniqueness for a prescribed velocity does not give uniqueness when
the velocity depends on eta. Complete proof: Section 9.13.
(f) (the backward-flow operator in a Holder norm). Fix 0 < alpha < 1 and p < mu < 1, put q = mu - p/2,
A_r = {r/2 < |X| < 2r} and |f|_{alpha,r} = sup_{A_r} |f| + r^alpha [f]_{alpha,A_r}, with [f]_{alpha,A} the
alpha-Holder seminorm on A, and let E be the space of x-even functions on R^2, alpha-Holder on compact subsets of R^2
minus 0, with f(0) = 0 and ||f||_E = sup_{0<r<=1} r^{-2} |f|_{alpha,r} + sup_{r>=1} r^{-q} |f|_{alpha,r} finite. There
are eta_n in E_mu cap E, each with h_n = 2 xi eta_n in C_c^inf supported in a fixed compact subset of x != 0 and
d[h_n] = 0, and constants C, c_* > 0, such that ||eta_n||_E <= C, B eta_n -> 0 uniformly on compact sets, and
||B eta_n||_E >= c_* whenever B eta_n is in E. Hence no subsequence of (B eta_n) lying in E converges in E, and no
compact map from E_mu cap E, with the norm of E, into E agrees with B on E_mu cap E; neither that B maps E_mu cap E
into E nor that it is bounded there is asserted. The mechanism is transport across the flow: for h = -Lap phi with phi
in C_c^inf vanishing near 0, W[h] = (-phi_xy, phi_xx) exactly, and for phi = n^{-2-alpha} b sin(n z) with
V_0.grad z = 0 the forcing W[h].grad xi carries the factor sin(n z), which is constant on each orbit, with a leading
coefficient of fixed sign. The sequence h_n of (c), also after the correction of Section 9.13, Step 8, that gives
d[h_n] = 0, satisfies ||h_n/(2 xi)||_E <= C n^{alpha-3}, so it does not show that I + B fails to be Fredholm in this
norm. Whether I + B is Fredholm in a realization of this kind is open: noncompactness of B does not decide it (B = I
gives 2I), and no decomposition of B into a compact part and a part of Volterra type along the flow is established.
Complete proof: Section 9.13, Step 11.
4.18 Singular flux, finite parts and the angular conditions
(proved statements in S^+ and for explicit angular functions; none gives nonexistence). In (a)-(c), rho is a profile
in S^+, l = c_l > 1, p = 1/l, alpha = 4l, beta = 2l - 1/2, and S, xi and B are as in Theorem 3.13.
(a) (Exact flux form.) Off Gamma the one-form omega = rho^(-2l) (V_1 dy - V_2 dx) is closed and equals the pull-back
by S of l A(th)^(-2l) dth. So for every C^1 arc in R^2 minus Gamma transverse to V, the integral of omega over it is
l int A^(-2l) dth over the arc of its scattering angles arg S; this is the flux identity (9.24.3)-(9.24.4) between any
two such arcs. On every compact set of angles on which A > 0, uniformly,
    R V_r(R e_th) rho(R e_th)^(-2l) = l A^(-2l) + R^(p-1) ((l + 1)/(l - 1)) (Psi A^(-2l))' + o(R^(p-1)),
with Psi as in Theorem 3.16: the limiting flux weight is l and the first correction is an angular derivative. This
expansion is not asserted uniformly up to a zero of A.
(b) (Renormalisation at the two zeros.) Near 0 there are C^1 area-preserving coordinates (u, v), with u = xi and
(u, v)(0) = 0, in which V = (u/2, beta v + f(u)) with f continuous. Cut each of the two arcs of {rho > 0} on a small
circle around 0 at the two points where |xi| = delta, let D(delta) > 0 be the difference of the v coordinates of the
two cut points and I(delta) the arc of their scattering angles. Then, exactly, l int_{I(delta)} A^(-2l)
dth = delta^(1 - alpha) D(delta)/2 for all small delta > 0. Subtracting this whole endpoint expression, with the cut
points transported by S, leaves exactly 0; this is a consequence of the conjugacy and of div V = 2l, not an
independent condition, and it expresses the angular integral through D(delta), not through A and a finite jet of rho
and V at 0. With only the regularity available in S^+, an ordinary angular Hadamard finite part of int A^(-2l) dth is
not determined: for every alpha > 4 the endpoint coordinate change t = s + c s^alpha, which is C^4 and preserves every
derivative of order less than alpha at the endpoint, changes the finite part of int t^(-alpha) dt by -c, for any real
c (a statement about singular integrals, not about profiles).
(c) (Conditional finite part.) Assume in addition that xi is C^infinity on R^2, that S is a C^infinity diffeomorphism
of R^2 minus 0 and that alpha = 4l is not an integer. Then on each component I of {A > 0} the ordinary Hadamard finite
part of int_I A^(-2l) dth (in the angular distance to the endpoints) exists and equals 0. It is the value at q = -2l
of the meromorphic continuation of int_I A^q dth, which is holomorphic there, and it follows by continuation from the
one-arc form of the identity int_{D_R} rho^q dX = R^(2 + pq) int A^q dth/(2 + pq) of 4.16(b) (q > -1/2); so it is a
consequence of the area conjugacy, not an independent Darcy condition. For integer alpha, with the same smoothness,
the continued value is (p/2) d_{alpha - 1}, where sigma is the sign of B on I and d_j is the coefficient of u^j in the
Taylor expansion at 0 of the coarea density of sigma xi on D_R (Section 9.26, Step 5); in that case no identification
with an ordinary finite part is asserted. The extra smoothness is a hypothesis; it is not known to follow from
membership in S^+.
(d) (The second moment family is equivalent to transport.) Let 0 < p < 1, l = 1/p, rho in C^2, W in C^1 with div
W = 0, rho = O(r^2), grad rho = O(r) and W = O(r) near 0, and rho = O(r^p), grad rho = O(r^(p-1)) and W = O(r^p) at
infinity. If (1 + 2l - ml) int rho r^(-m) Phi dX + int rho W.grad(r^(-m) Phi) dX = 0 for every smooth Phi on the
circle and every m in (2 + p, 4) (the second family of Proposition 3.4), then (l X + W).grad rho = rho on R^2; the
converse is Proposition 3.4. So for W = W[rho] and rho with the jet and the growth of S this family is equivalent to
the profile equation, and no count of finitely many scalar conditions decides whether it is compatible.
(e) (The angular conditions give no bound on l.) For l > 1 with 4l not an integer let A_l(th) = cos^2 th
(cos^2 th + (4l - 1) sin^2 th)^(-1/(2l)). A_l is smooth and nonnegative, invariant under th -> pi - th, and has
exactly the two zeros pi/2 and 3pi/2, both quadratic, with A_l'' = 2 (4l - 1)^(-1/(2l)) there. On (-pi/2, pi/2),
A_l^(-2l) = (sin th (cos th)^(1 - 4l))', so the finite part of (c) is 0 on this arc, and likewise on the other.
J_p[A_l] is not identically zero on either side of either zero (Theorem 3.16(b)), and E_A > 0 for A = A_l
(as in 4.16(a)). Perturbations of A_l^(-2l) by derivatives of smooth functions supported in the interior of the right
arc, reflected to the left arc, give infinitely many further angular functions with the same properties, whose
differences from A_l are linearly independent. So the conditions on the angular coefficient in (c), Theorem 3.2,
Theorem 3.16(b), Proposition 3.18(b), (c) and 4.16(a) hold together for 4l arbitrarily close to 4 and arbitrarily
large: they give neither a gap l >= 1 + eps nor an upper bound on l. This is angular compatibility only, as for A_f in
4.13a(c); no density or velocity on the plane is constructed. Complete proof of (a)-(e): Section 9.26.

## 5. Numerical program
No candidate profile was found, and no state has passed the complete candidate verification package (resolution and
domain checks, jet, Poisson residual, transport residual, artifact checks). The computations below are partial
numerical studies. The section distinguishes independently reproduced computations, single-code refinements, and
withdrawn readings retained to document numerical failures; their verification status is stated individually. All of
them are evidence, none is a proof, and none is a search of the whole class.

5.1 Codes. Three implementations share no code.
(i) A spectral polar solver: all Fourier modes in th (no parity), Chebyshev collocation in log(1 + r^2/L^2), the exact
per-mode class-S inverse (modes 0 and +-1 renormalised at 0 so that U(0) is removed, modes |m| >= 2 with an analytic
power-law exterior), the jet imposed as six linear conditions, and Levenberg-Marquardt, Picard and homotopy drivers on
rho or on the signed square root zeta (rho = zeta^2; the runs on zeta are restricted to nonnegative densities, whereas
S is not assumed nonnegative).
(ii) A characteristic-marching transport solver with Gauss-Legendre radial panels up to radius 10^10 and its own
polar-mode Biot-Savart quadrature, with Newton-GMRES and pseudo-arclength continuation using exact forward-mode
Jacobian-vector products, plus a Cartesian Ewald-split full-plane inverse (agreement 4e-15 on localised and 1.6e-12 on
growing r^0.6 test data).
(iii) A log-polar dynamic-rescaling code (exploratory; c reproduced to 4e-10 on x^2 (1 + a y)^2 e^{-r^2}, where
c = a/4 exactly).

5.2 Benchmarks reproduced by two codes. For rho_a = x^2 (1 + a y/<r>)^2 <r>^{-3/2} (<r> = (1 + r^2)^{1/2}):
c[rho_a] = a to ten digits in one code and to six in the other; psi_xyy(0) = (a^2 - 1)/4; after one frozen transport
step the xy coefficient of zeta is (a^2 - 1)/(8a + 2) to six digits. The moment identity of Theorem C holds
numerically on asymmetric growing data with the measured defect consistent with the predicted truncation rate L^{p-1}.

5.3 One-step characteristic map. Freezing V from rho_a (with c_l = 1/2 + a) and solving the linear transport problem
gives a new density with c = 0.0502 (a = 1.5) and 0.065 (a = 3), agreeing between the two codes to 3e-4 and 3e-3. A
fixed point would need the output c to equal the input c > 1/2. This concerns one family of inputs only; it does not
show that the map contracts in general.

5.4 Self-consistent homotopy in S. H(v, s) = F(v) - s F(v_0) (F the profile residual written through the marching map,
with p = 1/c_l a separate unknown), continued by pseudo-arclength from the x-even start a = 1.5, p_0 = 0.5. On the
angularly resolved part of the path the parameter s has a turning point at s = 0.449 (box 10^4) and 0.476 (box 10^10)
and then increases again; the path does not reach s = 0 (a zero of F). The later part of the path is under-resolved at
64 angles.

5.5 Forced homotopy from linear transport. V_h = c_l X + h W[rho] + (1 - h) E with the y-reflection-symmetric strain
E = grad-perp(mu x y e^{-r^2/4}) and c_l = 1/2 + h c + (1 - h) mu; at h = 0 the problem is linear transport with a
solution xi^2 of class-S growth, at h = 1 it is the profile system. Two independent codes agree on the converged
states (c to 2e-3 and c_l to six digits at mu = 3, h <= 0.5). The following
concerns this one continuation branch, not the class. For mu = 1 converged states were found up to the fold
h* = 0.2221 at 128 angles (box 1e4; 0.2213 at 64 angles) and h* = 0.2352 (box 1e10, not converged in the angular
resolution); at 256 angles (box 1e10, one code) the mu = 1 fold is at h* = 0.2387 with c_l = 1.009 (1.023 at 128
angles), the minimum of c_l along that branch is 1.0085 (1.0227 at 128 angles), the states are resolved for r < 1e5
only, and the fold value of c_l moves towards 1 under angular refinement; for mu = 3 up to the fold h* = 0.657-0.659.
At 128 angles c_l at the folds is 1.022-1.026 (1.025-1.053 at 64 angles), close to the boundary c_l = 1 of S. For
mu = 3 the value of c_l at the fold falls under angular refinement (1.053 -> 1.022) and the states are not resolved
beyond r = 1e2, so whether that branch folds above c_l = 1 is open.
A continuation of the mu = 3 branch at 256 angles (one code) gives the same fold, h* = 0.6595 with
c_l = 1.024 (1.022 at 128 angles), resolved for r < 1e3. Past the fold c_l decreases to 1.0034 (h = 0.6545) and then
increases, but those states are not resolved for r > 1e3 at 64, 128 or 256 angles, and the minimum of c_l along the
branch (1.048, 1.015,
1.0034 at 64, 128, 256 angles) is not converged; whether the branch reaches c_l = 1 is open.
Every converged state has c < 0, whereas an unforced profile in S needs c = c_l - 1/2 > 1/2. Back branches are not
resolved.

5.6 Summary of the searches of 5.3-5.5. Every tested nonlinear search there (Levenberg-Marquardt with c_l free or with
the strain identity imposed, Picard and damped Picard, run with code (i); Newton-GMRES and the two homotopies above,
run with code (ii) and for 5.5 also with code (iii)) either drifts toward the boundary c_l -> 1+
of S with a non-small residual or breaks down; none produced a converged unforced profile. No exact class-S profile
can have c_l <= 1 (Theorem A). A nonzero power tail with exponent p = 1/c_l >= 1 lies outside S. For 1 <= p < 2, the
twice-subtracted law leaves a linear strain among centered velocities of subquadratic growth. At higher growth, higher
harmonic stream-polynomial ambiguities occur (Section 2). States continued beyond S require an explicit prescription
for these choices. The later searches of 5.7 and 5.8 stay away from c_l = 1 and fail for the different reasons stated
there.
These observations are consistent with nonexistence in S but do not exclude disconnected or unstable solutions, and
they do not meet the standard for either endpoint.

5.7 Forced continuation in c_l. With the signed square root zeta (rho = zeta^2, so the densities are nonnegative;
this restricts the search), consider the forced problem (c_l
X + W[zeta^2]).grad zeta - zeta/2 = lambda f_0, where f_0 is the residual at c_l = 2 of the compatible seed
rho_0 = zeta_0^2 = rho_a with a = 1.5 (Section 5.2), so that lambda = 1 at the seed and lambda = 0 would be a profile.
The jet and the compatibility c_l = 1/2 + psi_xy(0) are imposed, c_l is prescribed and lambda is an unknown. Code (i)
continues this branch in c_l with zeta_m = (r/(1 + r^2)^{1/2})^{kappa_m} q_m for the angular modes (q_m Chebyshev
in a radial variable, an explicit tail beyond the box radius R). An independent evaluation (separate reconstruction
of the states, separate velocity solver) gives the following. For c_l in [1.2, 2] every stage solves its discrete
equations (lambda reproduced to 1e-5), and between the collocation nodes the full residual is at most about 1% of
the forcing on r <= 1000 (about 0.3% at (N_r, N_th, R) = (64, 48, 300)); the remaining defect comes from the angular
truncation. lambda(c_l) changes by at most 6e-5 under refinement ((48, 32) against (64, 48) at R = 300 on
c_l in [1.5, 1.9]; 48 against 80 radial nodes at R = 1000 at c_l = 1.2, 1.3, 1.5, 1.8) and by at most 3.5e-3 between
R = 300 and R = 1000; with R = 3000 the successive differences at c_l = 1.3, 1.5, 1.8 drop to 5e-4 or less, and at
c_l = 1.2 they stay below 1e-3. Along the branch lambda = 1 at c_l = 2, has a local minimum 0.767 at c_l = 1.8, is
about 0.81 on [1.5, 1.6], 0.75 at 1.3 and 0.70 at 1.2. At c_l = 1.1, lambda = 0.65 +- 0.01, with the outer third of
the box not resolved. The stages at c_l = 1.05 are not converged at R = 300, 1000 or 3000 (their lambda, 0.58-0.61, is
an indication only). Continued upward from c_l = 2 at (40, 24, 100), lambda = 1.20, 1.41, 1.64, 1.90 at c_l = 2.1,
2.2, 2.3, 2.4 (two radial representations agree to 4e-4); from c_l = 2.5 on the stages are not converged. A second
compatible seed (c_l = 1.5 at the seed) gives a converged branch on [1.2, 1.5] with lambda between 0.967 and 1.0
relative to its own forcing, and a seed with a random x-odd perturbation gives forced states with the same shape
(minimum about 0.83 near c_l = 1.75) but only at the 1-4% level (about 8% at R = 1000). A third compatible seed
(c_l = 3.5 at the seed) gives discrete forced states with lambda decreasing from 1 to 0.179 at c_l = 1.8 (R = 300 and
R = 1000 agree to 5e-4 on [1.8, 3.1]) and to 0.087-0.088 at c_l = 1.2, 1.1 at (48, 32, 300) (|res| 1.4e-4, 2.4e-4; the
stages at 1.6, 1.4 and 1.05 are not converged). These values vary across grids and boxes: at R = 1000 (64 radial
nodes) the stages at c_l = 1.4, 1.3, 1.2, 1.1 converge (|res| <= 9e-6) with lambda = 0.138, 0.138, 0.133, 0.123 (1.6,
1.5 and 1.05 not converged), and with 80 radial nodes at R = 300 lambda is 0.078-0.079 at c_l = 1.2, 1.1 (|res| about
5e-4). These states are resolved to a few percent only on r <= 100. Here lambda is measured in units of this seed's
own residual, which is large (6.6 max|zeta/2| on r <= 1 at the seed); in units of the field the forcing at c_l = 1.2
is 1.1, 0.45, 0.10, 0.016 times max|zeta/2| on 0 < r <= 1, 1-10, 10-100, 100-300, against 1.5, 1.2, 0.69, 0.25 on the
c_l0 = 2 branch. On every branch the forcing near the centre is of the size of the field. The representation imposes
no parity. None of these branches comes near zero forcing relative to the field on its resolved range (on the c_l0 = 2
branch, lambda >= 0.63 at the sampled stages with c_l in [1.1, 2.4]); no bound between stages or on other branches is
proved.

5.8 Forward reformulation. For p = 1/c_l write rho = r^p g and evolve, in log-polar variables, d_s g = V.grad
g + p (W_r/r) g with V = l X + W[rho], with inflow g = A(th) on the outer circle r = r_max (r_max = e^10 in the runs
below).
The velocity W is computed with rho = r^p A beyond r_max, where V.grad rho = rho holds only asymptotically; so the
states below are stationary states of a truncated problem, and "profile" in (c) refers to the full-plane problem only
in the limit r_max -> infinity. The truncation error is not measured by the flux term of the forward moment identity
below. In a box sequence (128 angles) m1 moves by 1.5-1.6e-3 at p = 0.5 between r_max = e^10 and e^20 (A = cos^2 th:
0.6084 to 0.6099), by 2.2e-4 at p = 0.3, and is not converged in r_max at p >= 0.8.
A stationary state solves V.grad rho = rho on r < r_max with rho = r_max^p A on the outer circle, and along
characteristics rho(X) = e^{-T(X)} r_max^p A(th_exit(X)), where T is the exit time of the orbit of V through X. On
every state below the origin is a source node of V (checked on each state), with eigenvalues m1 <= m2 of DV(0),
m1 + m2 = 2l, and the formula for rho applies along orbits with finite exit time. The following elementary statements
were checked independently (hand derivation and symbolic checks). (a) Near the node rho = |xi|^{1/m1} G(tau), where xi
is the weak eigen-coordinate (V.grad xi = m1 xi), tau labels the orbits, and G is constant along orbits; xi ~ r^{p m1}
Xi(th) at large r. (b) A C^2 state with rho = d x^2 + O(r^3), d != 0, forces DV(0) = diag(1/2, 2l - 1/2), hence
m1 = 1/2. (c) Restrict to full-plane stationary states with the bounds of S, the canonical velocity, the origin as the
only zero of V (with the global orbit coverage and regularity used in the signed-root construction, Theorem B (F3) and
Theorem 3.2) and the weak eigenvector horizontal (automatic for x-even data; in the asymmetric problem m1 = 1/2 does
not fix it). In this class a state with m1 = 1/2 and G constant equals G xi^2; after the spatial-amplitude
normalisation rho -> a rho(X/a) it has the prescribed jet, and it is a profile if it also has the C^3 regularity of S;
conversely every profile in S^+ is such a state. (A weaker hypothesis, the origin as the only source, would also admit
degenerate zeros of V, which Theorem 3.8 does not cover; it is not used.)
The finite-box computations below test these necessary matching conditions only. Within this restricted full-plane
class, and subject to the orientation, regularity and orbit-coverage hypotheses above, the proposed matching
conditions on a datum A and an exponent p are two: the scalar condition m1[A, p] = 1/2 and the functional condition
that Gt = A/|Xi|^2 is constant on the exit circle. These two conditions do not by themselves certify the C^3
regularity or, in the asymmetric problem, the horizontal weak eigenvector. (d) If V.grad
rho = lambda rho with lambda != 0 and V = l X + W[rho], then rho/lambda solves the transport equation with
c_l = l/lambda (W is linear; the focusing range c_l > 1 needs 0 < lambda < l), and a further spatial rescaling
restores the jet coefficient; this does not remove the scalar condition. A count of unknowns and conditions for the
linearised problem (index 0 for x-even data, -1 in the full class) holds only under a Fredholm hypothesis that is not
proved (in the direct realization of Section 4.17(c) the linearisation on x-odd functions is not Fredholm). The
numerical findings below are evidence only; the reproduction status of each is stated with it:
(i) A = cos^2 th, p = 0.5: a stationary state with DV(0) = diag(0.6085, 3.3915) (agreement to 2e-4; halving the time
step from 0.02 to 0.01 changes m1 by 4.5e-4; a further, unsettled halving by 1.4e-3), stationary to about 1.5% of the
field on r >= 1 and to a few percent on (1e-3, 1); the angular layers at the node are not resolved at 128 angles.
Since m1 != 1/2 it is not a profile.
(ii) A = cos^2 th at smaller p: m1 = 0.564 +- 2e-3 (p = 0.1), 0.557 (0.12), 0.550 (0.15), 0.547 +- 1e-3 (0.2), 0.552
+- 1e-3 (0.3), 0.608 (0.5), all above 1/2. Earlier readings of a crossing m1 = 1/2 near p = 0.14-0.2, obtained with a
semi-Lagrangian scheme at time step 0.02, violate the forward form of the moment identity of Theorem C,
Q = pi (l - 1)(l - m1) (for a whole-plane stationary state with the bounds of S and horizontal weak direction, where
c = l - m1; on the box the outer-circle flux term of the identity is included in the test)
by 8e-3 to 6.8e-2 in m1 and are discretisation artefacts (mainly the time step). The readings near p = 0.2 were
withdrawn by the code that produced them; the reading p* ~ 0.143 from the other code is refuted as evidence by the
same identity and was withdrawn by its producer.
(iii) A_b = cos^2 th exp(-b sin 3th) (x-even), p = 0.5: a crossing of the discrete scalar diagnostic m1 = 1/2 is
located numerically at b* = 0.1235-0.1237 (three grids in one code;
m1(b*) = 0.49996, 0.50030, 0.50036 at 128, 256, 512 angles in the other). At b* the quantity log Gt varies by
1.65-1.74 over the exit circle in both codes (orbit tracers with a manufactured-flow check; inner stop and step count
changes below 5e-3), with G(-inf)/G(+inf) about 0.21 (axis law of (iv), orbit-free) and, relative to the orbits
tangent to the weak axis, G(-inf) : G(0) : G(+inf) about 0.18-0.20 : 1 : 0.85-0.92 (axis law of (iv) and a refined
tracer, two codes; the G(0)-relative values move with the tracer resolution, 0.185 : 1 : 0.861 at 256 and 0.197 : 1 :
0.916 at 512 angles). By these tracer and axis diagnostics the state fails the numerical functional matching test.
The values m1(b*) are approximate; the quoted G ratios are not measurements of distinct finite quadratic Taylor
coefficients of an exact state. Away from m1 = 1/2 the axis quantity has the renormalised interpretation in (iv).
Within this family the scalar diagnostic crosses 1/2 to the quoted accuracy, but the state is not a profile and
provides no evidence of a profile. The value b* refers to r_max = e^10; in the box sequence above it moves to about
0.1253.
(iv) A six-mode x-even datum A = cos^2 th e^{F(th)}, F = sum_j x_j phi_j, phi_j = sin j th (j odd), cos j th (j even),
with (x_1, ..., x_6) = (0.23901, -0.71412, -0.20966, 0.12195, 0.10705, -0.02705) and p = 0.49568, found by a Newton
search on a residual weighted by A, has m1 = 0.5007 / 0.4993 at two resolutions in the code that produced it and
m1 = 0.4969 in an independent solver (the core-corrected strain moments give m1 = 0.497 in two codes; the larger
readings omit the core term of 8.4(a)). log Gt is constant to about 0.03 on most of the exit circle, with dips in
windows around the zeros of A: log Gt - mean = -0.13 at 89 deg and -0.90 to -0.97 at 269-270 deg (512 angles; three
codes agree to 0.05-0.1; values relative to the mean carry about 0.04 of tracer resolution error, and readings within
1-2 deg of the zeros are the least reliable; the dips and the asymmetry below change by less than 3e-3 between
r_max = e^10 and e^20). An orbit-free check: on the y-axis of an x-even stationary state put h(y) = rho_xx(0, y),
b(y) = V_2(0, y) and k(y) = d_x xi(0, y), which solves b k' + (d_x V_1 - m1) k = 0, k(0) = 1. The transport equation
gives b (log h/k^2)' = 1 - 2 m1, so at m1 = 1/2 the ratio h/k^2 is constant on each half-axis and equals 2 G(+inf)
above and 2 G(-inf) below the node. For a state with m1 != 1/2 the literal limits G(+-inf) are both 0 or both
infinite; the value quoted in this section as log G(-inf)/G(+inf), and written D, is then the renormalised axis
quantity q_- - q_+, with q_+- = log(h/k^2)(+-r) - (1 - 2 m1) int_{r_min}^{r} ds/B_+-(s) at distance r from the node on
the upper / lower half-axis (B_+- the outward axis speeds of (v), k = 1 at the inner grid radius r_min on both
half-axes; one implementation instead adds an estimate of the integral below r_min, see 8.4(b)). Where the axis
law holds q_+- does not depend on r; at m1 = 1/2 the quantity is log G(-inf)/G(+inf). Tracer values of D are
differences of log Gt next to the two zeros. The law
holds on the computed states (for log r >= -2), and log G(-inf)/G(+inf) = -0.69 to -0.72 on this state from the axis
law in two codes (tracer values next to the zeros agree with it once the backward tracer is started close enough to
the node, at radius e^-12; started at e^-9 they are biased by about -0.1 near the lower zero because the velocity has
a large quadratic term at the node; -1.54 to -1.55 for the state of (iii), r_max = e^10 to e^30). The asymmetry is not
rigid at fixed m1: a localised change of A near the lower zero, with a compensating change of another coefficient that
holds m1 at its base value (0.497), moves log G(-inf)/G(+inf) at rates between 0.3 and 2.6 per unit amplitude,
depending on the compensating direction (one datum, 256 angles). With D = -0.69 to -0.72, the renormalised axis
quantities q_+ and q_- differ between the two half-axes; since m1 is about 0.497, they are not measured finite
quadratic Taylor coefficients at the node. The state fails the functional matching condition and is not a profile.
Further Newton searches with window-adapted unknowns did not converge; no state meeting both matching conditions has
been found.
(v) An exact formula for the asymmetry (derived independently by the verifier and checked by a separate audit; the
hypotheses are stated, not proved for the computed states). On the y-axis of an x-even stationary state with m1 = 1/2
let B_+(r) = V_2(0, r) and B_-(r) = -V_2(0, -r) (r > 0) be the outward speeds on the two half-axes. Assume B_+ > 0 and
B_- > 0, B_+(r) = n r + O(r^{1+alpha}) and B_-(r) = n r + O(r^{1+alpha}) at r = 0 with n = m2 = 2l - m1 and some
alpha > 0, B_+(r) = l r + O(r^p) and B_-(r) = l r + O(r^p) at infinity, and that rho and its transverse second
derivative on the axis approach those of the datum A = cos^2 th e^{F(th)}. Put b_o = (B_+ + B_-)/2 and
w_e = (B_+ - B_-)/2; w_e(r) is the part of W_2(0, y) even in y, evaluated at y = r. Integrating the equation for k of
(iv) on each half-axis and using the axis law gives
    D := log G(-inf)/G(+inf) = F(-pi/2) - F(pi/2) + 4n int_0^inf w_e/(b_o^2 - w_e^2) dr,
with an absolutely convergent integral. Because the kernel of W_2 on the axis is even in the vertical variable, w_e
depends only on the part of rho even in y, and the node strain only on the part odd in y. In the far field
w_e ~ e_p r^p with e_p = -2(p+1)/(p(p+2)(p+4)) < 0 for A = cos^2 th (general formula for A vanishing at +-pi/2, as
cos^2 th e^F: e_p = -((p+1)/sin(pi p/2)) int_0^{pi/2} A_e cos((p+2) th) dth, A_e the part of A even in y; checked
against the computed six-mode state to 0.3%). Consequence: if F(-pi/2) <= F(pi/2) and w_e <= 0 on the axis, then
D <= 0, and D < 0 unless F(-pi/2) = F(pi/2) and w_e vanishes identically on the axis. The identity alone does not fix
the signs of its two terms: on the six-mode state of (iv) the band r < e^-4 contributes about +0.84 to n int_0^inf
(1/B_- - 1/B_+) dr, which is half the integral term of D (w_e > 0 near the node, two codes), the bands (e^-4, e^2) and
r > e^2 about -0.47 and -0.17, which with F(-pi/2) - F(pi/2) = -1.111 gives D about -0.71; the formula gives -0.716
against the axis-law value -0.720 in the independent solver. To
turn the identity into an exclusion for profiles requires additional bounds on its terms (for profiles in S^+_even all
hypotheses above hold, D = 0, and the formula is the identity of Proposition 3.17). The hypothesis that D depends at
first order only on the part of A even in y was tested and refuted in the independent solver: a localised pair of
changes of A at the two zeros, odd in y, moves D by 0.72 per unit amplitude (one datum, 256 angles, away from
m1 = 1/2).
(vi) Coupling of the zero windows to the scalar condition, and a 64-mode search. At fixed velocity the characteristic
formula is linear in A, and when V_r > 0 every orbit exits at r_max; so a factor f applied to A on a set of exit
angles multiplies rho by f on the whole family of orbits with those exits. Near the node the orbits with exits in
narrow windows around the zeros of A fill most of the two half-discs (on the six-mode state of (iv), 512 angles, the
backward orbits of the lower-window exits 260-275 deg already sweep 173-310 deg at radius e^-6; the upper-window exits
reach the x-axis by e^-9). Heuristically, on such a half-disc rho is close to G(+-inf) x^2 (the two half-discs are
separated by the separatrix through the node, which leaves it tangent to the weak axis along a curve y = kappa x^2; on
the 32-mode iterates below kappa is 1130-2050 and the curve lies 3-17 deg off the x-axis at log r between -10 and
-8.5, and rho jumps by about |D| across it), and since int_0^pi cos^2 th sin 3th dth = 14/15 the two half-discs
enter c = psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX with opposite signs, in proportion to G(+inf) - G(-inf). Measured
on the six-mode state (512 angles, two codes): raising A on |cos th| < sin 12 deg so as to remove the deficit of
log Gt at the zeros moves m1 from 0.497 to 0.719 at fixed velocity (lower window alone +0.272, upper alone -0.050),
and to 0.740 (two codes, to 1e-3) after the velocity is relaxed with it; the asymmetry is then about -0.13, a value
that is not converged in the inner radius. So the window values and the scalar condition are strongly coupled. This
particular finite modification raises m1 by about 0.22 before and 0.24 after relaxation of the velocity; a
continuation using it would need compensating changes of the other modes. These are finite-amplitude measurements at
one state, not a linear-response calculation and not a restriction on other paths.
A Newton search on 64 x-even Fourier modes of log A and on p (256 angles; residual m1 - 1/2 and the non-constant part
of log Gt) lowered its residual from 0.21 to 0.075 in seven iterates, with residual 0.076 and m1 = 0.518 at its fifth
iterate (p = 0.5345) in the code that produced it. In two other codes the same datum has m1 = 0.561 +- 0.001 (512 and
1024 angles; unchanged to 6e-4 under r_min e^-12 -> e^-16 and halving the radial step) and 0.558-0.565 (512 and 1024
angles), and log G(-inf)/G(+inf) = -0.31 +- 0.03. The 256-angle state is not a fixed point of the exact characteristic
map for log r < -6, next to the upper zero: one application of the map with the velocity of that same state moves m1
from 0.522 to 0.565. So the iterate is about 0.06 away from m1 = 1/2, its residual was underestimated by the coarse
grid, and it is not a candidate. The tested 256-angle states failed this check; 512 angles were the minimum used
afterwards. Some 512-angle states still fail it, and angular refinement alone does not resolve the radial defect. Two
later iterates (the seventh, and the second of a variant with weight 10 instead of 3 on m1 - 1/2) have m1 = 0.5595 and
0.555 in an independent solver at 512 angles, against 0.519 / 0.532 (256 / 512 angles) and 0.503 in the producing
code; their log G(-inf)/G(+inf) is -0.35 and -0.24. The producing code's 512-angle state is still not a fixed point of
the exact map (one step moves m1 by +0.023, all of it from log r < -6), so doubling the angles there removed only half
of the discrepancy, and the search was reducing the scalar residual of a map whose inner core is off by 0.04-0.05.
The cause is the producing code's foot interpolant in its semi-Lagrangian step (a local tensor cubic Lagrange
interpolant on a 4 x 4 stencil). With the same velocity and the same feet, on a state consistent with the exact map,
it drifts in the core next to the x-axis and along the upper zero (by 0.05-0.1 per unit pseudo-time at the upper zero
in the verifier's measurement; a larger reading from another implementation was not reproduced), where an
interpolating cubic B-spline drifts much less; the drift does not shrink with the step. So the two
schemes have different fixed points: at frozen velocity, on the 512-angle state of the fifth iterate, the Lagrange
fixed point has m1 = 0.530-0.532 (pseudo-time steps 0.01-0.04), the B-spline fixed point 0.554-0.561 and one exact
characteristic map step 0.5596; at 1024 angles the Lagrange shift is 0.014. This shift at frozen velocity has the size
of the whole discrepancy, so no velocity error is needed to explain it. The second iterate of the 64-mode search
continued at 512 angles, which reached a residual 0.046 with m1 = 0.501 in the producing code, has m1 = 0.557-0.558
in two other codes. All results of these searches are
withdrawn as evidence about the data. A B-spline semi-Lagrangian state still moves with the pseudo-time step (0.007
in m1 between steps 0.01 and 0.04 at frozen velocity), so every state used as evidence is also tested against one
exact characteristic map step.
A Newton search on 32 x-even modes and p with the B-spline scheme (512 angles; same residual, with a penalty on the
axis-law spread) then moved p from 0.496 to 0.384 in eight iterates (a ninth, with p = 0.374, ended the run). In an
independent exit-map code its iterates have m1 = 0.521, 0.522, 0.520, 0.519, 0.520, 0.519, 0.519 and 0.511, and from
the third iterate on one exact characteristic map step moves m1 by 1.3e-3 to 3.2e-3 (4.2e-3 at 1024 angles on the
eighth), more than the 1e-3 required, with the defect at log r between -10 and -8. The one-step change overstates the
displacement of the fixed point: at the sixth iterate's datum the exact-map fixed point has m1 = 0.5197 and 0.5208 in
two codes (D = -0.36 in both), against 0.5194 for the iterate. So these iterates stay at least 0.011 above m1 = 1/2
and none is a candidate.
On a tested state with V_r < 0 regions and a slow window next to a zero of A (the six-mode x-even family below at
p = 0.35, a_2 = -1.1, close to m1 = 1/2) the B-spline semi-Lagrangian implementation did not converge under changes of
the pseudo-time step, even at frozen velocity: at 512 angles its fixed point has m1 = -8.5, 0.36 and 0.80 at
pseudo-time steps 0.005, 0.02 and 0.04, while the fixed point of the exact characteristic map with the same velocity
has m1 = 0.511, which supplies the reference value.
Such states are therefore computed
directly as fixed points of the exact map, rho = e^{-T} r_max^p A(th_exit), by Anderson-accelerated iteration with the
velocity recomputed at each iteration and orbits integrated in arclength. On the x-even family
A = cos^2 th exp(sum_{j=1}^6 x_j phi_j), phi_j = sin j th (j odd), cos j th (j even), with
(x_1, ..., x_6) = (0.31474, a_2, -0.13666, 0.122, 0.107, -0.027), at p = 0.35 these fixed points give:
- a_2 = -1.1: m1 = 0.509 (512 angles, defect 1e-4) and 0.508 (1024 angles); D = -0.31 at both (direct form, see below:
  -0.30 and -0.31);
- a_2 = -1.2: m1 = 0.504 (512 angles, defect 3e-6) and 0.505 (1024 angles); D = -0.27 and -0.26 (direct form -0.26 at
  both);
- a_2 = -1.25 (512 angles only, defect 4e-4): m1 = 0.497, D = -0.23 (direct form -0.25).
At 1024 angles the iteration stalls at a defect of 3e-3 to 8e-3 with m1 steady to 2e-4 over the stalled iterations.
This is not the accuracy of m1: in one exact-map implementation the radial representation of the a_2 = -1.2 and -1.228
states is under-resolved in the upper slow window (log r between -8 and -3, 75-100 deg; jumps of the panel
interpolants up to
0.23 in log rho/r^p), and one map step then changes m1 by up to 1.7e-3 under refinement of the transfer grid, without
a convergence order, so these m1 values carry an uncertainty of about 2e-3 (smaller at a_2 = -1.1). At a_2 = -1.228,
eta13 = 0.0802 (eta13 is the parameter of the two-parameter extension defined below, not the strain), halving the
radial panel width (not converged, defect 4e-3) changes m1 by -5e-4 and D by +1.3e-3 (divergence form) and +2.2e-3
(direct form). Under this one radial refinement the moments changed by about 1e-3; this is a refinement difference,
not a certified error estimate, and the uncertainty of about 2e-3 is retained. The panel-edge jumps in the upper slow
window are not reduced: that window is not resolved pointwise at either radial resolution. At the size 2e-3 the
bracket of m1 = 1/2 at a_2 = -1.228 below moves by about 1.3e-3 in eta13 and about 3e-3 in D. Lowering the inner
radius from e^-14 to e^-17 (512 angles) moves m1 by -5e-5 and +4.2e-4 and D (divergence form) by +0.005 and +0.014 at
a_2 = -1.1 and -1.2 (direct form +0.005 and +0.013); at -1.2 the change of D exceeds half the tolerance of 8.6(c), so
D is not converged in the inner radius there. At a_2 = -1.228, on the three converged states of the two-parameter
extension below (eta13 = 0.0744, 0.0773, 0.0802, x-even projection unchanged, independent implementation), the same
change moves m1 by -5.1e-4, +5e-5 and +8.9e-4 and D by +0.019 in the divergence form and +0.015 to +0.017 in the
direct form. At eta13 = 0.0773 a further step to inner radius e^-20 moves D by +0.0008 in both forms and m1 by -8e-7,
so at that datum the e^-17 values agree with e^-20 to about 1e-3 (one eta13 value, 512 angles, x-even projection; no
other datum was refined to e^-20). The
shifts +0.005 and +0.014 (a_2 = -1.1, -1.2, original family) and +0.019 (a_2 = -1.228, two-parameter extension) are
larger at the sampled states nearer the crossing; they are not samples of one continuation path. The outer radius has
not been varied. The asymmetry is taken from the axis law of (iv) with the transverse rate d_x V_1 on the axis
computed through div V = 2l, as 2l - d_y V_2, which uses derivatives along the axis only; it moves by at most 0.006
between 512 and 1024 angles. With the rate computed directly (the direct form, with the angular derivative taken by
local fourth-order differences) the asymmetry agrees with these values to 0.016 on the converged 512-angle states and
to 0.0023 at 1024 angles. An earlier evaluation of the direct form with a spectral angular derivative differed by up
to 0.12 on the converged states (0.16 on an unconverged one); that was an artefact of Gibbs oscillation at the angular
layers of rho next to the zero. Pointwise the two transverse rates still differ (by up to 0.35 on the upper half-axis
for log r between -8 and 0 on the 1024-angle state at a_2 = -1.2), although the integrated asymmetries agree. So the
512-angle values bracket m1 = 1/2 between a_2 = -1.2 and -1.25, and linear interpolation puts the crossing near
a_2 = -1.228 with D about -0.25 (secant slopes of D
0.41 and 0.70 per unit decrease of a_2 on the two intervals). This is interpolation, not a computed matching state. At
a_2 = -1.228 itself the exact-map iteration does not converge at 512 angles (defect oscillating between 2e-3 and 1e-2,
m1 between 0.4957 and 0.4970; D = -0.215 in the divergence form and -0.25 in the direct form, upper divergence-form
spread 0.047). These unconverged iterates suggest a different location (about a_2 = -1.214 by interpolation in m1, D
about -0.24) but do not refine the bracket. Converged states at a_2 = -1.228 exist in a two-parameter extension of the
family in which x_1 and x_3 are both shifted by eta13 - 0.07 (x_1 - x_3, and with it the endpoint values of F,
unchanged; eta13 = 0.07 is the family above; the strain of these states is c = l - m1, about 2.35): at eta13 = 0.0744
and 0.0802 (512 angles, defects 3.2e-6 and 5.7e-6) m1 = 0.49673 and 0.50543 and D = -0.238 and -0.250 in the
divergence form (-0.254 and -0.249 in the direct form; upper divergence-form spreads 0.034 and 0.020). At
eta13 = 0.0773, started from the eta13 = 0.0744 and from the eta13 = 0.0802 state, the iteration gives m1 = 0.5034 and
0.5031 and D = -0.240 and -0.243 (defects 2e-4 and 1e-4). The two starts produced nearby diagnostics and no second
branch was found; the departure from linear dependence on eta13 (about 2e-3 in m1 at eta13 = 0.0773) is comparable to
the m1 uncertainty. Linear interpolation using the adjacent states eta13 = 0.0744 and 0.0773 gives a
crossing near 0.0759, with D about -0.240 in the divergence form and -0.25 in the direct form at inner
radius e^-14 (one angular resolution). The printed m1 values give crossings 0.07582 or 0.07589 for the
two starts at 0.0773; a 0.002 change in m1 corresponds to about 0.0009 in eta13 and about 0.001 in D.
Using only the endpoints 0.0744 and 0.0802 gives 0.07658 and a sensitivity of about 0.0013 in eta13.
A quadratic fit through the three states (independent
implementation) puts the crossing at eta13 = 0.07568 at inner radius e^-14 and 0.07580 at e^-17 (linear
interpolation in that implementation: 0.0759 and 0.0760; the difference 1.2e-4 is a refinement difference, not an
accuracy), and D at the crossing moves from e^-14 to e^-17 by +0.019 in the divergence form and +0.016 in the direct
form, to about -0.222 and -0.235. Transferring the shift +0.0008 from e^-17 to e^-20 measured at eta13 = 0.0773
(above) gives about -0.221 in the divergence form and -0.234 in the direct form at the crossing (512 angles, x-even
projection). These are estimates: the crossing itself (eta13 about 0.0758) has not been computed at e^-20, and the
transfer of the shift is not verified. The total uncertainty, which would include the difference between the two
forms, the inner-radius limit and the absent angular and domain refinement, is not established. This two-parameter
bracket does not confirm the interpolated crossing on the original one-parameter family. Restarted at eta13 = 0.0744
from the eta13 = 0.0802 state, the iteration returns to the same state, so a second state at that datum was not found.
At a_2 = -1.0, eta13 = 0.045 the exact-map fixed points of two codes (1024 angles, defect 5e-6; 512 angles, defect
5e-11) have m1 about 0.504 +- 0.002 (with the core term of 8.4(a)) and D about -0.36 (both forms, within 0.007): a
second state of the two-parameter extension close to m1 = 1/2, with D further from 0 than at a_2 = -1.228.
At a_2 = -1.3, off m1 = 1/2 (m1 = 0.486, defect 7e-3), D = -0.24 and -0.25 in the two forms: this unconverged iterate
shows no further increase of D at inner radius e^-14; since larger inner-radius shifts were observed at the sampled
states nearer the crossing (see above), this does not show that the inner-radius limit of D stops increasing, and the
trend along the branch remains unresolved. In the same direction the upper zero window
slows (minimum of |V|/r over 80-100 deg, sampled at integer log r, about 0.67, 0.42 and 0.35; over all radial nodes
0.37 at a_2 = -1.228 (eta13 = 0.07 iterate; 0.38 on the converged eta13 = 0.0744 and 0.0802 states) and 0.27 at -1.3)
and the minimum of V_r/r falls from -0.92 (a_2 = -1.1) to -2.75 (-1.25) and -3.69 (-1.3), and the axis-law spread on
the upper half-axis grows (0.014 to 0.043 at 512 angles). This is one datum family; whether the asymmetry reaches 0 on
m1 = 1/2 before the upper window stagnates is not determined.
Parity. The x-even searches cannot see states that break the reflection symmetry x -> -x. At the a_2 = -1.1 state of
this family (512 angles), a 48-step finite-difference Arnoldi iteration of the discrete fixed-datum exit map,
restricted to x-odd perturbations, has a real Ritz value 0.969 (Arnoldi residual 1.4e-10 at 48 steps, 7e-8 at 40). Its
Ritz vector is concentrated on two mirror grid nodes in the slow region (log r = -6.46, th = 76 and 104 deg; 78 % of
the norm), the true residual is 0.12 to 0.20, and the Rayleigh quotient depends on the difference step (0.82 to 1.06
for relative steps 1e-5 to 1e-3). This is not evidence of an x-odd eigenvalue of the exit-map derivative near 1; it is
a discretisation-scale feature of the discrete map at this resolution. The two nodes lie in a thin fan of orbits (a
change of 0.1 deg in the start angle moves the exit angle through about 150 deg), and the x-odd matching residual of
the Ritz vector, computed on independent backward orbits, is 3.8 per unit norm against 0.36 to 1.9 for four comparison
vectors, so the vector does not satisfy the x-odd matching conditions (its residual is the largest of the five unit
vectors tested). At a_2 = -1.2 and -1.228 the real x-odd Ritz value nearest 1 (0.83, 0.88) again belongs to a vector
concentrated on a mirror pair of grid nodes (57 % and 72 % of the norm, inside 80-100 deg), with the largest matching
residual of five vectors tested. The smallest singular value of the assembled rectangular Arnoldi matrix Hbar of J - I
(residual row retained) at a_2 = -1.1 is 0.0067 at 48 steps. For a fixed linear operator B with orthonormal bases and
B Q = Q_+ Hbar + E, ||E|| <= eps, this gives sigma_min(B) <= 0.0067 + eps. Here the columns are directional finite
differences (T(u + hv) - T(u))/h, which are not exactly linear in v, and E has not been bounded, so the bound on the
smallest singular value of J - I is conditional.
A fresh finite-difference evaluation along the real Ritz vector v = Qy of the same Krylov sequence (40 steps) differs
from Q_+ Hbar y by about 0.115, against 0.0067, and depends on the difference step; so the defect of the Arnoldi
relation is not small along that direction, and the bound is not informative as it stands.
It is not an eigenvalue statement; the operator is non-normal. For the map restricted to smooth x-odd perturbations (a
fixed smoothing: angular modes |k| <= 32 and a Gaussian of width 0.5 in log r) at a_2 = -1.1, the real Ritz value
nearest 1 is
0.318 at 512 angles (24 steps, converged in the Krylov dimension, true residual 3 % for the smoothed operator) and
0.594 at 1024 angles (40 steps, converged in the Krylov dimension, true residual 7 % to 31 % depending on the
difference step, at a state with fixed-point defect 3e-3), so this value is not converged under angular refinement.
The unsmoothed map sends that smooth vector to a large non-smooth remainder, so this is not a statement about the
x-odd spectrum of the map or of the continuum operator. No Ritz value of the smoothed operator, real or complex, lies
within 0.68 of 1 at 512 angles or within 0.40 of 1 at 1024 angles; the largest-modulus pair is 0.845 +- 1.225i
(modulus 1.49) at 512 angles and 0.791 +- 1.212i (modulus 1.45) at 1024 angles. At 1024 angles (one
refinement of the a_2 = -1.1 state) the real x-odd Ritz value nearest 1 of a 40-step iteration of the unsmoothed map
is 0.846; its vector is again grid-scale but concentrated elsewhere (log r about -10, 21 deg), its true residual is
0.9 to 2.5 and its Rayleigh quotient changes by a factor of about 3 with the difference step, so the value 0.969 does
not persist under this refinement (one refinement step and a 40-dimensional Krylov space; nothing follows about the
continuum spectrum). The dominant x-odd Ritz values of the discrete map at 512 angles are a complex pair of modulus
2.03 (next 1.48; no validated residuals); independently, an unprojected run at a_2 = -1.3 left the x-even subspace.
These observations suggest that plain iteration of the unprojected discrete map is unstable in x-odd directions; they
do not establish linear instability. If a simple real x-odd eigenvalue crossed 1 transversally along the family and
I - K were Fredholm of index 0 (neither is established; the spectrum of the continuum operator is not known), these
conditions, together with C^2 smoothness of the map, would give a symmetry-breaking branch by the
Crandall-Rabinowitz theorem (stationary states at the same x-even datum that are not x-even, related in pairs by the
reflection; a nonzero bifurcation coefficient would in addition fix its pitchfork shape). The profile question is
different: it concerns the x-odd part of the profile Jacobian with the datum varied and the matching and orientation
(psi_yy(0) = 0) conditions included, which has not been obtained (no linear-response column of 5.8(vii) meets its
acceptance rule). No parity-free profile search has been completed.
Scope. The searches of 5.8(iv)-(vi) and the Newton searches on 64 and 32 x-even modes are restricted x-even
exploratory searches: the x-even form of the datum (and, in some runs, an x-even projection of the state) is imposed
by the ansatz, so they do not satisfy the parity-free search requirement of the task, whatever their outcome. Runs
without a projection (5.4, the asymmetric seed of 5.7, the unprojected runs below and the parity-free tests of
5.8(vii)) are partial work in that direction and do not change the scope of 5.8.
Without the projection, the iteration at x-even data converged at a_2 = -1.1 and -1.2 (x-odd part about 4e-7) and
left the x-even subspace at a_2 = -1.3 (5.8(vi)). Started from the x-even fixed point at a_2 = -1.0 with both zeros of
the datum rotated by 0.01 rad, the unprojected iteration did not converge in 21 evaluations (first defect 1580; best
defect 0.50, at a state with m1 = 21.4 against 0.504 at the start). This run changes the datum and drops the
projection together, so it does not separate their effects. Local uniqueness of the x-even fixed points among states
that are not x-even was tested twice, without a decision. An unprojected Newton-GMRES iteration (30 Krylov vectors,
finite-difference Jacobian-vector products with relative step 1e-2, backtracking on the residual norm) of the
256-angle exit map, with the zeros of the datum slaved to the exit angles of the strong manifold of the current
velocity, was started from the 256-angle x-even fixed point at a_2 = -1.0 (m1 = 0.509) multiplied by 1 + 1e-3 cos th.
In five steps the residual norm fell by 42 %; the run ended at its iteration limit with defect rms 2.05e-3 (against
8e-5 at the x-even fixed point), the x-odd part of the iterate at 4.3e-4 of the x-even part (rms; 8.1e-4 imposed)
after a rise to 2.2e-3, and the strong exits within 0.02 deg of 90 and 270 deg. A first run of the same test from the
same start (relative step 1e-4, 20 Krylov vectors) was stopped after three steps, also without a decision. The
realised decreases were far below the linear predictions, so the linear model built from the finite-difference
Jacobian-vector products does not describe the realised map on the scale of these steps; neither a return to the
x-even state nor a fixed point that is not x-even is established.
(vii) Parity-free tests at one x-even state. The base is an x-even exit-map fixed point at 512 angles with 16 x-even
modes of log A, a_2 = -1.0 and p = 0.337, obtained from the a_2 = -1.0 state of (vi) with eta13 = 0.045 (its
1024-angle fixed point subsampled to 512 and re-converged, m1 = 0.5043 with the core term, D = -0.36) by two
Gauss-Newton steps at frozen a_2 in p, in a_1 and a_3 to a_16 and in an orbit-coefficient offset, with the rows
m1 - 1/2 and the 16 coefficients of log Gt and no axis row, then re-converged: defect 1.3e-4 (maximum) and 8e-7 (rms),
m1 = 0.4882 (with the core term of 8.4(a), here 1.5e-3), axis mismatch D = -0.356. It is not a stationary point of the
x-even least-squares functional (gradient of |F|^2 of norm 94 at |F|^2 = 3.52, |F| = 1.88). The parity-free
formulation adds the 16 x-odd modes of log A to the 16 x-even ones and p, lets the zeros of A follow the computed
exits of the strong manifold (variant: fixed zeros with two shift unknowns and two matching rows), and uses the rows
m1 - 1/2, the 32 coefficients of log Gt in both parities, the axis mismatch, two differences of one-sided band means
of log Gt at the zeros and the orientation moment psi_yy(0) (weights 50, 1, 5, 5, 50; the matching rows of the variant
50); the state iteration is not projected onto either parity. At x-even states the rows reproduce the x-even results
and the unweighted x-odd rows vanish to 1e-13. Fixed-point iteration of the map diverges at x-odd data (a 2 per cent
x-odd change of the datum moves the upper strong exit by 4.3 degrees at 256 angles while the warm start keeps its
zeros; the feedback state -> exits -> zeros -> image is unstable). The x-odd block of the Jacobian was therefore
sought by the linear response at the base, with an acceptance rule fixed before the last five of the columns below:
true residual below 0.1 and agreement of the column within 10 per cent between two finite-difference steps on the
plateau established by the verifier (relative steps up to 3e-6). None of nine columns for the first x-odd mode passed:
unsmoothed, true residual 32; smoothed with slaved zeros, 7.7 at step 1e-3 and 0.30 / 0.29 at 3e-6 / 1e-6 with the two
columns differing by 150 per cent; smoothed with fixed zeros, 952; with the core below log r = -8.5 frozen,
0.19 / 0.042 (slaved) and 0.113 / 0.173 (fixed) with the pairs differing by 147 and 129 per cent relative to the 3e-6
column (sign changes in the dominant rows for the fixed-zero pair, in one band row for the slaved pair). A masked
smoothed Newton-GMRES state solver at x-odd amplitude 0.01 reduced its merit from 67030 to 2172 in five accepted steps
and stalled at defect 0.33 (at amplitude 0.05 the warm start has its upper exit 78 degrees from the zero), so the
planned second-order test of the parity-free functional along x-odd directions was not validated: with such states the
second difference is uncontrolled (error bound: row error over squared amplitude), and the x-even rows at nonzero
x-odd amplitude are proxies with a bias of the order of the curvature sought. The sensitivity of the strong exit to
the state, which obstructed both routes, is the same at 256, 512 and 1024 angles: within 0.15 per cent for the first
x-odd mode (2.35 degrees per 1e-3 relative change of the state in the discrete l2 norm of the density over its core
scaling r^(2-p), a norm that is 94 to 98 per cent core, hence the large gain in these units; linear within 0.1 per
cent up to a relative step of 3e-4) and within 0.3 per cent for a smooth far-field and an inner perturbation of the
same norm (39 and 0.43 degrees; linear up to 3e-5 and 3e-3), while the number of core cells next to the separatrix
that switch exit branch under a fixed perturbation about doubles with each doubling of the number of angles. The
agreement of the core-frozen first-mode column between the steps 3e-6 and 1e-6 (relative difference of its x-odd part)
is 0.84, 1.47 and 0.15 at 256, 512 and 1024 angles, with true residuals 0.089 / 0.175, 0.19 / 0.042 and 0.081 / 0.179:
no column meets the rule at any resolution. Repeated at 1024 angles with 40 instead of 25 Krylov vectors, the pair
gave 0.24 (true residuals 0.036 / 0.160), and the x-odd part of the column changed by 44 per cent at the step 3e-6 and
by 24 per cent at 1e-6 (relative to the 40-vector column): at 1024 angles the column is converged neither in the step
nor in the Krylov dimension. An amplitude continuation with the unprojected fixed-point solver (at most 40 evaluations
per amplitude; each run stopped after 18 to 22, when the step damping reached its floor) converged at none of the
x-odd amplitudes 1e-4, 3e-4, 1e-3, 3e-3 and 1e-2 at 512 angles: at every amplitude the starting guess, taken from the
base, already had defect 0.29 to 3.0 (maximum), no iterate reduced its rms defect, and the returned iterate had an rms
defect 8 to 10 times larger (final maxima 0.38 to 4.4, against 1.3e-4 at the base); the 256-angle repeat behaved in
the same way at all five amplitudes (starting maxima 0.29 to 1.8, no iterate reduced the rms defect, returned rms
8 to 10 times the start, final maxima 0.28 to 4.4 against 0.023 at the 256 base). A Newton run for the 256-angle base
state with an approximate variational tangent of the discrete exit map, obtained from the linearised transport
equation along the stored characteristics with the two datum zeros as unknowns and checked against finite differences
on selected directions, did not converge at amplitude 1e-3 of the first x-odd mode: full steps increased the residual,
and strong damping produced little progress. The full linear-response correction to that mode increased the residual
at every tested amplitude from 1e-5 at 256 angles and from 1e-3 at 512 angles; truncating the Krylov least-squares
solve at singular values below 1e-4 of the largest gave corrections that reduced the residual 3.6-fold (256 angles)
and 4.3-fold (512 angles) at amplitude 1e-3, and Newton with the same truncation at 256 angles stalled at 29 per cent
of its starting residual. In an independent evaluation with a separately written exit map, with the datum zeros set to
that map's own strong exits, the truncated correction reduced the x-odd part of the residual 2.5-fold at amplitudes
1e-5 to 1e-3 at 256 angles, but at 512 angles only 1.1-fold at 1e-5 and 1e-4, and it increased it 1.14-fold at 1e-3;
the full one increased it about 4.5-fold at 256 angles and 6 to 9-fold at 512 angles. On log r >= -4 both reduced it
at both resolutions (31-fold and 205-fold at 256 angles, 28-fold and 68-fold at 512 angles, at amplitude 1e-3), and
the differences lie at log r < -4, where that map holds the base state much less accurately than on log r >= -4. These
tests do not isolate the cause of the failure and do not establish angular convergence. No profile, x-even or
asymmetric, was found. The verifier recomputed the residual diagnostics and the column comparisons from the stored
data. Evaluated directly on the base states at 256, 512 and 1024 angles (721 radial nodes on -14 <= log r <= 10, three
end rows excluded) with a velocity computed independently of the solver, the transport residual V.grad rho - rho has
rms, relative to the ring maximum of rho, 2.3e-5, 1.03e-5 and 1.03e-5 on -2 <= log r < 2 and 5.6e-7, 5.5e-7 and 5.6e-7
on 2 <= log r <= 10; with the solver's own velocity the corresponding values are 2.0e-5, 4.5e-7 and 4.3e-7, and
3.4e-8, 3.3e-8 and 3.2e-8. A comparison at 512 and 1024 angles with the radial spacing halved (from 1/30 to 1/60 in
log r) is consistent with second-order radial discretisation error in the solver's velocity routine as the source of
the velocity difference there (its Richardson extrapolation agrees with the independent velocity to about 3e-8 rms,
relative to the ring maximum of |W|, on -2 <= log r < 2). In the core, with radial derivatives from quintic splines
and local eighth-order angular differences, the residual has maxima of order 1 along the curve y = a x^2 (a about
4.3e3) and at the separatrix of the strong-exit sector; outside 10-degree sectors around the weak axis and 3-degree
windows around the two strong exits its rms on -14 <= log r < -11 is 1.2e-3 to 1.6e-3 at 512 and 1024 angles and
7.5e-3 to 8.4e-3 at 256 angles. Spectral angular differentiation gives 0.38 to 0.42 there on -13 <= log r < -11, owing
to the jump across the curve: on the tested rows with log r <= -12, rho/x^2 changes within one angular cell by a
factor 0.699 to 0.704, close to exp(D) = 0.70, while on the tested rows with log r >= -9 the largest change per cell
decreases with angular refinement. These diagnostics are consistent with the axis mismatch D in these three discrete
states; they give no existence or nonexistence result.

## 6. Independent verification timeline
Two kinds of independent check were used: an independent verifier (separate code and hand derivations, no shared code)
and separate adversarial audits of the written proofs. The timeline records the checks performed and their
limitations; a confirmation recorded here does not substitute for a complete written proof or for a numerical error
estimate, and Sections 2a-5 state the status of each claim. Superseded values are kept in the timeline and marked as
superseded. All times are UTC; undated entries are on 2026-10-17
(from the system clock at the time of writing or from file times). Entries that mention an artifact index refer to
a working index of the run records, which is not part of the accompanying artifacts.
- 17:37  start (T0 = 17:37:18Z).
- 18:06  first separate audit of the reduction, the velocity law and the growth bound (Theorem A); correction: the
         density gradient at the centre is zero; counterexample to "Q <= 0 for nonnegative rho" (4.1).
- by 18:20  verifier: reduction, compatibility identities, cubic jet, polynomial trap (formal only), symmetries,
         strain moment formulas, independent Cartesian inverse, the closed form of Q(rho_a) to 1e-15.
- 18:47  verifier: free orientation (Theorem D), moment law (Theorem C, algebra and numerics), basic S^+ structure,
         benchmarks of 5.2, one-step map 5.3 (independent code).
- 19:07  verifier: states with c_l <= 1 (outside S) depend on the choice of the added harmonic strain; first
         independent Newton-GMRES and homotopy runs.
- 19:07-19:17  verifier check of the first structure write-up (Theorems 3.1-3.5): confirmed with wording corrections;
         agreement with the separate audit (19:12) on every theorem; the dynamic version of the moment law holds only
         while psi_yy(0) = 0.
- 19:42  separate audit of Proposition 3.6 and the flow topology outside S^+ (Lemma 3.7, Theorem 3.8): confirmed,
         with corrections (no sign rule for removing mass; no genericity; basins have infinite area).
- 19:57  verifier: forced homotopy of 5.5 reproduced; the verifier's own earlier "converged state at h = 0.3" and the
         self-consistent homotopy results beyond the first turning point withdrawn (an inner scalar loop was not
         converged); redone with p as an unknown (5.4).
- 19:59  verifier: Proposition 3.6, Lemma 3.7, Theorem 3.8 confirmed (agrees with the 19:42 audit).
- 20:01  separate audit of Propositions 3.9-3.12 and Theorem 3.11: confirmed with two corrections (Prop 3.9 needs rho
         not identically zero on the basin; a sign in the short proof).
- 20:14  verifier: Propositions 3.9-3.12, Theorem 3.11 confirmed; three wording notes (applied).
- 20:18-20:23  verifier: Theorem 3.13, Proposition 3.14 and Proposition 3.15 (symbolic check) confirmed; remark that
         differentiability of S is not proved in that version (the statement does not use it; Section 9.4 now proves
         that S is C^2 off 0 and not Lipschitz at 0).
- 20:27  separate audit of Theorem 3.13, Propositions 3.14, 3.15, the leaf reduction and the test-density
         constructions: all confirmed under the stated hypotheses (the integrals of g are improper).
- 20:56  separate audit of the c_l -> 1+ results (4.7): confirmed (one typo in a display).
- 21:08  separate audit of Theorem 3.16 and the weighted energy identity (4.5): confirmed (scope: every profile whose
         A has a positive quadratic zero; S^+ is not needed).
- 21:08  verifier: the joint satisfiability of the moment law and the wall identity on smooth test densities (4.2)
         confirmed numerically with an independent evaluator; the first test densities used a feature with a
         non-decaying gradient (outside S) and were replaced by smooth ones. The 4.7 statements confirmed as stated
         (conditional ones as conditional); the reading of the resolution scale in 4.7(iii) is heuristic.
- 21:15  verifier: Theorem 3.16 and the weighted energy identity confirmed (hand derivation, symbolic algebra, a
         numerical check of the canonical velocity of r^p A and a manufactured exterior flow), as a restriction on
         tails and not a nonexistence theorem.
- 21:33  verifier: the forced continuation of 5.7 evaluated independently: discrete solutions confirmed; resolved
         approximation of the forced problem at R = 100 confirmed as evidence; the R = 300 stages are not resolved
         beyond r ~ 50 (the earlier reading "reproduced at R = 300" refuted as a statement about the PDE).
- 21:36  separate audit of the large-c_l statements (Theorem 4.9, Corollary 4.10, Remark 4.11): confirmed, with one
         typographical correction and one inference (the curvature of the limiting zero curve) found incomplete and
         not used.
- 21:38-21:42  verifier: the large-c_l statements of 4.8 confirmed (hand derivation, symbolic algebra), including the
         strain escape and a numerical check of the envelope bound of 4.7 on seven densities; agreement with the
         21:36 audit on every item.
- 21:47  verifier check of a draft of this report: Sections 0-4 and 5.1-5.4 confirmed; the first wording of 5.5 read a
         statement about one branch as a statement about the class and used outdated fold values (refuted as worded,
         corrected); a qualifier added in 4.7(i).
- 22:03  separate audit of the structure of the limit problem (Proposition 4.12): confirmed, with corrections to the
         Taylor wording at arc endpoints (incorporated) and to the scope of the compactness bound (whether the
         subclass of Corollary 4.10 is nonempty is unknown). The weighted balance of Remark 4.13 was derived in the
         same audit.
- 22:09  verifier: the limit-problem results behind Proposition 4.12 confirmed (hand derivation, symbolic algebra
         with 37 checks, and an independent numerical check of the logarithmic far-field coefficient C_A to eight
         digits between r = 1e4 and 1e7).
- 22:17  verifier: final wording of 4.8-4.12 and Remark 4.13 confirmed, with wording points (the velocity law named
         in the self-similar reading of (P0), the asymptotic statements qualified as |Z| -> infinity, the proof idea
         of Theorem 4.9(a) to use transport on the nullcline at finite p_n), all incorporated; a 256-angle
         continuation of the mu = 3 branch of 5.5 (incorporated).
- 22:20  separate audit of the label coordinates for S^+ (Section 4.6): confirmed with corrections (global C^2 is not
         proved and the shortcut through the regularity of the signed root is false, by an explicit counterexample;
         the non-Fredholm statement holds for realizations locally equivalent to H^3 -> L^2).
- 22:25  verifier: the sampled stages of the forced continuation in 5.7 confirmed as discrete solutions and as
         1%-level approximations of the forced problem on r <= 1000 for the tested c_l in [1.2, 2]. At the compared
         parameter values lambda changes by at most 6e-5 under refinement and 3.5e-3 between R = 300 and 1000.
         The c_l = 1.1 stage is marginal; the c_l = 1.05 stages are not converged. A forcing bound stated on
         [1.05, 2.4] was refuted as worded; the supported lower bound concerns only sampled stages in [1.1, 2.4],
         not a continuous interval. The upward stages c_l = 2.1-2.4 were confirmed at R = 100 only.
- 22:32  verifier: the label coordinates for S^+ confirmed (global C^1; global C^2 not proved; 39 symbolic checks,
         including the counterexample to the root-regularity shortcut), in agreement with the 22:20 audit on every
         item.
- 22:38  verifier check of the 22:23 revision of this report: confirmed except the 5.5 sentence on the 256-angle run
         (outdated by the end of that run; replaced by the verifier's text) and 5.7 (superseded by the 22:25 data;
         rewritten, and amended again after the 22:41 entry).
- 22:41  verifier: the check of the forced continuation of 5.7 extended to box radius R = 3000.
- 22:45  verifier: the wording of the label-coordinate paragraph of 4.6 checked clause by clause (sign of xi,
         distributional closedness, order count, Fredholm qualification); the principal part of the linearisation
         checked by an independent symbolic computation.
- 23:00  verifier (addendum 23:09): forced states from the third seed of 5.7 (c_l = 3.5) confirmed as discrete states
         at sampled stages in [1.8, 3.5] and at c_l = 1.2, 1.1, resolved to a few percent only on r <= 100, with
         forcing of the size of the field near the centre: not a candidate.
- 23:09  verifier check of the 22:46 revision of this report: confirmed except the omission of the third-seed branch
         in 5.7 and Section 7 and wording in 4.6 and 5.7 (all applied).
- 23:20-23:24  verifier: normalisation and equilibrium relations of the forward reformulation (5.8) checked by hand;
         DV(0) of the forward state 5.8(i) confirmed with an independent inverse (2e-4); stationarity at the percent
         level for r >= 1e-3, node layers unresolved.
- 23:44  verifier: the node structure 5.8(a) confirmed (hand derivation, 16 symbolic checks).
- 2026-10-18 00:05  verifier: the crossing m1 = 1/2 in the family of 5.8(iii) confirmed with an independent stationary
         solver; G not constant (log Gt range 1.65-1.74 in two codes): not a profile. A reading of this crossing as "a
         codimension-one family of profiles" refuted.
- 2026-10-18 00:24-00:36  verifier: two readings of a small-p crossing m1(cos^2) = 1/2 (from two codes with the same
         time-stepping scheme) refuted as evidence (violation of the moment identity of Theorem C); independent values
         of 5.8(ii).
- 2026-10-18 00:38  verifier: 5.8(b)-(d) confirmed as conditional or algebraic statements; audit of the 00:01 revision
         of this report: the forward reformulation was missing (Section 5.8 added).
- 2026-10-18 00:56  verifier check of Section 5.8 and Conclusion item 5: confirmed with three required corrections
         (truncated-problem sentence, the identity violated by the small-p readings, the withdrawal status), applied.
- 2026-10-18 01:58  verifier: the earlier truncation sentence of 5.8 (small flux, hence small truncation error) is
         wrong; box sequence in r_max gives the m1 shifts now stated in 5.8 and moves b* of 5.8(iii) (applied).
- 2026-10-18 02:10-02:38  verifier: the six-mode datum of 5.8(iv) with an independent solver (256 and 512 angles):
         m1 0.4969, the dips at the zeros confirmed as a datum property, box-independent between r_max = e^10 and
         e^20; the y-axis law re-derived by hand and confirmed on the verifier's states.
- 2026-10-18 02:49-03:01  verifier: the asymmetry log G(-inf)/G(+inf) of 5.8(iii) and (iv) confirmed to 0.05 with an
         independent solver and axis test (-1.54 to -1.55; -0.69 to -0.72).
- 2026-10-18 04:09  verifier: the exact formula of 5.8(v), the parity separation, the conditional sign and e_p
         confirmed (own derivation; formula -0.716 against the axis law -0.720 on the six-mode state); the hypothesis
         that D depends at first order only on the y-even part of A refuted in the independent solver.
- 2026-10-18 04:15  separate audit of the derivation of 5.8(v): confirmed under the stated hypotheses (regularity
         B = n r + O(r^{1+alpha}) at the node, differentiated far-field limits, matching at the node); two prose
         inferences of the draft corrected (no exclusion of a core contribution to derivatives; a nonexistence proof
         need not prove D < 0).
- 2026-10-18 04:15  verifier: the 03:33 revision of 5.8 confirmed except two corrections (d != 0 in (b); the ratio in
         (iii)); both applied, with the recommended caveats in (iv).
- 2026-10-18 04:30  verifier check of the 04:20 revision (5.8(iv), 5.8(v), Conclusion item 5): confirmed, with two
         precisions (the non-rigidity statement holds at fixed m1; the far-field coefficient formula of 5.8(v) is for
         data vanishing at +-pi/2), applied.
- 2026-10-18 04:49-05:01  verifier: the backward orbit tracer, stopped at radius e^-9, biases log Gt within a few
         degrees of the lower zero by about -0.1 (large quadratic part of the velocity at the node); stopped at e^-12
         it agrees with the axis law. The tracer value previously quoted in 5.8(iv) was removed (applied 05:40).
- 2026-10-18 05:39-05:55  verifier: corrected velocity routine of the code used for 5.8(iv) confirmed (4e-3); base
         six-mode state with it: log G(-inf)/G(+inf) -0.716 / -0.719 (axis law) and -0.669 (tracer stopped at radius
         e^-11.5) confirmed in a second code (-0.707 to -0.720; -0.679); m1 = 0.497 by the moment with core term in
         both codes (the value 0.501 quoted earlier is a ring fit). Window coupling of 5.8(vi) at fixed velocity
         measured independently: +0.222 (both windows), +0.272 / -0.050 (lower / upper window).
- 2026-10-18 06:03  verifier: the window update of 5.8(vi) with relaxed velocity, m1 0.740, confirmed to 1e-3; its
         asymmetry -0.13 (-0.12 / -0.14 in the two forms of the axis law) confirmed as a number, not converged in the
         inner radius.
- 2026-10-18 06:12-06:25  verifier: the 64-mode iterate of 5.8(vi) in an independent solver: m1 0.561 +- 0.001 (512
         and 1024 angles, inner radius e^-12 and e^-16, radial step halved); the 256-angle value 0.518 refuted as a
         property of the datum (one exact characteristic map step moves m1 to 0.565);
         log G(-inf)/G(+inf) = -0.31 +- 0.03, confirmed against the second code (-0.308 / -0.309 at 512 / 1024 angles
         with one form of the axis law, -0.313 / -0.314 with the other).
- 2026-10-18 06:44  verifier: two later iterates of the 64-mode search (5.8(vi)) in an independent solver: m1 0.5595
         and 0.555 (512 angles), asymmetry -0.35 and -0.24; the producing code's 512-angle state fails the one-step
         test of the exact characteristic map (+0.023).
- 2026-10-18 07:09-07:20  verifier: the second iterate of the 64-mode search at 512 angles (residual 0.046, m1 0.501
         in the producing code): m1 0.5566 in an independent solver (0.558 in a second code), not a fixed point of the
         exact map (one step +0.055); its asymmetry -0.22 / -0.26 not resolved (axis-law spread 0.28; the producing
         code gives -0.19 for the first form). The cause of the producing code's bias (its local cubic Lagrange foot
         interpolant) confirmed by an independent implementation: frozen-velocity fixed points m1 0.530-0.532
         (Lagrange), 0.554-0.561 (B-spline), 0.5596 (one exact step), at 512 angles; 1024 angles: Lagrange shift
         0.014. The verifier measured 0.05-0.10 for the one-step drift near the upper zero; the larger 0.18-0.60
         reading of the second code was not reproduced and is not used.
- 2026-10-18 07:42  verifier: semi-Lagrangian fixed points (B-spline kernel) do not converge in the pseudo-time step
         where V_r < 0 regions or slow windows are present (m1 -8.5 / 0.36 / 0.80 at steps 0.005 / 0.02 / 0.04, frozen
         velocity, against 0.511 from the exact map); fixed points of the exact characteristic map on the six-mode
         family at p = 0.35, a_2 = -1.1 / -1.2: m1 0.509 / 0.504, asymmetry -0.31 / -0.27 (5.8(vi)).
- 2026-10-18 07:50  verifier: the 07:24 revision of 5.8(vi), the timeline and Conclusion item 5 confirmed against the
         underlying checks.
- 2026-10-18 08:03  verifier: the same fixed points at 1024 angles (m1 to 1.3e-3; asymmetry by the divergence form of
         the axis law to 0.006; the direct form not converged in angle) and the next state a_2 = -1.25 (512 angles):
         m1 0.497, asymmetry -0.23. Linear interpolation places the m1 = 1/2 crossing near a_2 = -1.23; this is not a
         computed matching state.
- 2026-10-18 08:11  criterion change (bears on the reading of Section 7 item 5): for search states the asymmetry is
         taken in the divergence form of the axis law if that form is angle-converged (moves by at most 0.02 under 512
         -> 1024 angles), with the direct form reported next to it; a candidate needs both forms. Accepted by the
         verifier (08:38).
- 2026-10-18 08:12  verifier: one exact characteristic map step on the first eight iterates of the 32-mode B-spline
         search: m1 0.511-0.522 in the verifier's code, the 1e-3 consistency requirement fails from the third iterate
         on (5.8(vi)).
- 2026-10-18 08:35-08:38  verifier: the exact-map fixed point at the sixth iterate's datum, m1 0.5197 (0.5208 in a
         second code), D -0.36 in both; the remaining exact-map mismatch of those iterates sits at the cells next to
         the separatrix through the node (the curve y = kappa x^2), across which rho jumps by about |D|; the six-mode
         family at a_2 = -1.228 (no convergence at 512 angles, m1 0.4957-0.4970, D -0.215 in the divergence form; the
         direct-form value -0.06 recorded then used a spectral angular derivative and is superseded by the 10:03
         check, -0.25) and -1.3 (m1 0.486, D -0.24); the 08:11-08:16 revisions of 5.8(vi) and Section 7 item 5
         confirmed, with a wording change on the crossing (applied).
- 2026-10-18 09:09-09:21  verifier: converged exact-map states at a_2 = -1.228 in the two-parameter extension of the
         six-mode family (eta13 = 0.0744 / 0.0802: m1 0.4967 / 0.5054, D -0.238 / -0.250 in the divergence form), and
         no second state at eta13 = 0.0744; the window minima of |V|/r quoted in 5.8(vi) confirmed to 0.016 in the
         panel code; t_min = -17 moves m1 at a_2 = -1.1 by 5e-5 (5.8(vi)).
- 2026-10-18 09:21  verifier: the 08:51 revision and Section 8 (09:03) confirmed with amendments (the 5.8(c) wording
         on the source, implementation details in Section 8, the list of fully checked arguments in 2a; applied
         09:30); the cross-implementation accuracy figures of 8.2-8.3 traced to the checks that produced them.
- 2026-10-18 09:22  separate audit of Section 8 against the implementations and the stored data: the lists of 8.7
         confirmed (all 96 coefficients and both exponents to the printed digits); the normalisation of 8.6(f) was
         wrong (dividing by the node coefficient changes the velocity and destroys stationarity; replaced by the
         spatial-amplitude scaling of 5.8(c)); the descriptions of the implementations corrected (Newton polishing
         does not supply an exit-map residual; exit truncation, defect definitions, iteration limits, axis-law
         conventions, tracer stops and centring sets). One audit item, that the six-mode residual is not weighted by
         A, refers to a different implementation; the search that produced the six-mode datum used the weight
         A / max A (8.5).
- 2026-10-18 09:30  verifier: large upper axis-law drifts (0.5-2.0) reported by the main solver on its exit-map states
         at a_2 = -1.0 and -1.1 come from the FFT evaluation of h (Gibbs oscillation next to the zero of A); with the
         local second difference the drifts are 0.005-0.013 in the divergence form, and the moments agree with the
         verifier's to 4e-6 once the core term is added (the main solver confirmed this in its own code at 09:40, with
         D in the divergence form unchanged to 7e-4 by the choice of h and to 3e-4 between 512 and 1024 angles).
- 2026-10-18 09:38  verifier: the 09:31 revision confirmed with five amendments (h method in 8.4(b), projection and
         iteration counts in 8.8, the 1024-angle m1 range and the inner-radius sentence in 5.8(vi), one timeline
         value); the normaliser of the residual in 8.6(f) corrected (applied 09:43-09:47).
- 2026-10-18 09:41  verifier: x-odd spectrum of the exact-map derivative at the six-mode family states a_2 = -1.1 and
         -1.2 (16 Arnoldi steps on the x-odd subspace): the dominant x-odd eigenvalues are complex pairs of modulus
         about 2 (so plain Picard iteration of the unprojected map is unstable in x-odd directions) [later reading:
         Ritz values without validated residuals, which suggest but do not establish x-odd instability; 5.8(vi)], no
         converged Ritz value lies near 1, and the test is too small to exclude an x-odd eigenvalue near 1. Open:
         neither an x-odd neutral mode (symmetry-breaking bifurcation) nor isolation of the x-even states against
         x-odd perturbations is established.
- 2026-10-18 09:46  verifier: frozen-velocity split of c by exit angle on the six-mode family state at a_2 = -1.228
         (4.14(f)) confirmed in an independent code (split to 0.03, totals to 6e-3; the near-zero windows are net
         negative outside the core only summed over log r in [-10, -2]).
- 2026-10-18 09:53  verifier: the core-imbalance statements of 4.14 (a), (d), (e) confirmed; (b) confirmed once
         alpha_+- is defined through xi (with rho/x^2 = G(1 + alpha y) the alpha formulas are off by a factor 2); (c)
         confirmed under G_+- > 0, n >= 1, with the remark that the bound holds for every D; the Gbar R readings of
         4.14(f) supplied.
         Earlier separate audit (09:47): (a), (d) confirmed; (b) valid as an isolated geometric contribution with an
         o(r^3) remainder needed; (c) inequality confirmed but the core strain need not vanish with D.
- 2026-10-18 10:01  verifier: the second exact-map implementation is converged in its arclength step (3e-6 in m1) but
         not in its transfer grid (one map step moves m1 by up to 1.7e-3 at a_2 = -1.2, without a convergence order),
         traced to an under-resolved radial representation in the upper slow window; m1 uncertainty about 2e-3 at
         a_2 = -1.2 and -1.228 (5.8(vi)). The main solver's exact-map states at a_2 = -1.0 and -1.1 are fixed points
         of the verifier's map to 1.3e-3 and 1.5e-3 in m1 per step; the two fixed points at a_2 = -1.1 agree to 3e-4
         in m1.
- 2026-10-18 10:03  verifier: the direct form of the axis law with a local fourth-order angular derivative agrees with
         the divergence form to 0.016 (512 angles) and 0.0023 (1024 angles) on the six-mode family states; the earlier
         large differences and the 512 -> 1024 jump came from a spectral angular derivative (Gibbs oscillation at the
         window layers); direct-form values in 5.8(vi) and Section 7 replaced (applied 10:16). Hysteresis test at
         a_2 = -1.228: two starts at eta13 = 0.0773 agree to 3.6e-4 in m1 and 2.5e-3 in D. Linear interpolation of
         sampled values places the m1 = 1/2 crossing near eta13 = 0.0759 with D about -0.240 in the divergence form
         (5.8(vi)); this is not a computed matching state.
- 2026-10-18 10:07  verifier: the 09:43-09:47 edits confirmed, with the direct-form values to be replaced as above.
- 2026-10-18 10:13  verifier: the algebra of the singular-branch and jet-order statements (circulation bound for a
         perturbative core, core velocity at the node, cusp half-annulus strain, the layered solutions, the moment law
         with inner flux, the generalised axis law, the regular-root restriction) confirmed; now 4.15.
- 2026-10-18 10:14  verifier: 4.14 and the 10:07 changes confirmed with two wording amendments (4.14 (d), (f); applied
         10:16).
- 2026-10-18 10:15  separate audit of the statements of 4.15: (a), (e), (f) confirmed; (c), (h), (i) confirmed with
         corrections (the shrinking-core limit in (c), the coefficient q n of J in the jet-order case of (h), the
         local bounds for B_eps -> 0 in (i)); scope remarks on (a), (e)(iii) and (f) added. 4.15 entered with these
         corrections (10:22); verifier check of the corrected wording requested.
- 2026-10-18 10:19  verifier: the 10:16 revision confirmed with one amendment (the spectral direct form differed by up
         to 0.12 on the converged states, 0.16 on an unconverged one; applied 10:24). The local exponent on the ray
         th = 0 (4.15(j)) confirmed in an independent code, with the slope and the minimum corrected (applied 10:24).
- 2026-10-18 10:26  verifier: radial resolution test at a_2 = -1.228, eta13 = 0.0802 (panel width halved; not
         converged, defect 4e-3): m1 changes by -5e-4, D by +1.3e-3 and +2.2e-3 (two forms), a single refinement
         difference (not a certified error estimate; the m1 uncertainty of about 2e-3 is retained); the
         upper slow window is not resolved pointwise at either resolution; m1 = 1/2 crossing unchanged within its
         uncertainty. Confirmed for the moments; the pointwise structure is open. Wording entered in 5.8(vi) at 10:34.
- 2026-10-18 10:36  verifier: x-odd Arnoldi with 48 steps at a_2 = -1.1: a real x-odd eigenvalue 0.969 of the
         fixed-datum exit-map derivative (converged within the Krylov space from k 32 on), sigma_min of the projected
         J - I at most
         0.0067 [the rectangular Arnoldi matrix, residual row retained]; supersedes the 09:41 "no converged Ritz value
         near 1" (the mode was not yet in the 16-step space).
         Confirmed as a finding of the discrete map at 512 angles; true residual, step and resolution dependence, and
         the eigenvector open. Entered in 5.8(vi) at 10:49. The eigenvalue reading was withdrawn at 11:01 (below).
- 2026-10-18 10:46  verifier: 4.15 and the 10:24 / 10:34 edits confirmed with one amendment ((e)(ii) needs
         m1_j -> 1/2; in general kappa = l - m1_inf - c_out); applied 10:49.
- 2026-10-18 10:47  verifier: extension of 4.15(f) to 0 < g < 2 (axis rigidity for C^3 odd regular roots, no
         admissible solution of that form for 1 <= g < 2, formal C^{2,g-1} roots, the g = 1 layer) confirmed with
         three wording amendments; separate audit (10:35) confirmed the rigidity with the off-axis C^1 hypothesis and
         downgraded the claim that the equations do not force a C^3 root to an open question. Entered as 4.15(f) at
         10:49.
- 2026-10-18 10:48  verifier: the main solver's state at a_2 = -1.0, eta13 = 0.045 (1024 angles) reproduced by an
         independent fixed point (512 angles): m1 about 0.504 +- 0.002 and D about -0.36 in two codes; the main
         solver's m1 omitted the core term (1.3e-3 on this state). Entered in 5.8(vi) at 11:03.
- 2026-10-18 10:51  separate audit of the report version of 10:40 (major revision): the inference from the core-strain
         limit to D -> 0 needs G_+ |1 - e^D| -> 0; strain c and the family parameter eta13 were conflated in places;
         normalisation in 4.15(e); exact m1 = 1/2 in 4.14; "only source" versus "only zero"; the x-even searches are
         not parity-free; proof-status language in 3.x and Section 7; wording of Theorem 3.13; numerical statements to
         be stated as observations; timeline and tag consistency in Section 6; the L^q tail consequence of 3.16(c);
         conventions in 8.4 and 8.6. All items applied 10:53-11:02 (status paragraphs, 3.x, 4.14, 4.15, 5.x, Section
         6, Section 7 rewritten, Section 8); verifier check of the revised text requested.
- 2026-10-18 10:53  separate audit of the linearisation statements behind the bordered x-odd profile Jacobian: the
         derivative formula of the exit map at a fixed point and the translation and rotation modes confirmed; the
         continuum realisation of the derivative is open; "index zero implies an isolated fixed point" is false (not
         used in this report); a positive smallest singular value of a matrix truncation does not exclude a continuum
         fixed point without a validated lower bound; the smallest singular value of a projected Arnoldi matrix
         (rectangular, residual row retained) is an upper bound on the global minimum and gives pseudospectral
         information, not an eigenvalue (consistent with the wording of 10:36). [Qualified after the 13:29 separate
         audit: for a fixed linear operator; with finite-difference columns the defect E of the Arnoldi relation must
         also be bounded (5.8).]
- 2026-10-18 10:54  verifier: the 10:49 edits confirmed with one substantive amendment (the closing sentence of 4.15
         needs l > 1 and W = o(r) on the axis; the g = 1 layer is a counterexample otherwise) and four wording points
         (4.15(f) formal roots for 1 < g < 2; the g = 1 pair is not C^1 at its zeros; the moduli 2.03 and 1.48; the
         pitchfork stated under simplicity, transversality and Fredholm hypotheses); applied 11:03. [The pitchfork
         wording was revised after the separate audit of 12:39 and the verifier check of 12:52: a nonzero bifurcation
         coefficient is needed for the pitchfork shape, not for the existence of the branch.]
- 2026-10-18 11:01  verifier: the real x-odd Ritz value 0.969 at a_2 = -1.1 has a Ritz vector concentrated on two
         mirror grid nodes (78 % of the norm), true residual 0.12-0.20 and step-dependent Rayleigh quotient 0.82-1.06;
         the reading "an x-odd eigenvalue 0.969" of 10:36 is withdrawn (not established). 5.8(vi) and Section 7 item 4
         amended at 11:03.
- 2026-10-18 11:10  verifier: the two nodes of that Ritz vector lie in a thin orbit fan (0.1 deg of start angle sweeps
         the exit angle through about 150 deg; no stagnation point nearby), a discretisation-scale feature of the
         512-angle map, as in 5.8(vi); its x-odd matching
         residual on independent backward orbits is 3.81 per unit norm (comparison vectors 0.36-1.88). Entered in
         5.8(vi) at 11:13.
- 2026-10-18 11:16  separate audit of the complete written proof of Theorem B (F3) and the coverage B(0) = R^2 (C^2
         convergence on compact subsets of the basin, rho = xi^2, the zero set as the strong unstable line, coverage
         by the Poincare-Bendixson theorem): confirmed without correction.
- 2026-10-18 11:22  verifier: the versions of 11:04 and 11:13 (all items of the separate audit, the 10:48-11:10
         entries, the recomputed 4.14(f) table and indicative radii, the L^q tail consequence of Section 7 item 2 for
         every q >= 1) confirmed with wording amendments (the matching-residual sentence, Ritz values rather than
         eigenvalues of modulus 2.03 and 1.48, "discretisation-scale feature", two minor wording points, timeline
         order) applied at 11:23; an index from run labels to the accompanying artifacts is required before the
         terminal version.
- 2026-10-18 11:26  verifier: the condensed proof of Section 9.1 re-derived step by step from the stated hypotheses
         and confirmed as a complete proof of Theorem B (F3) and coverage, with three missing one-line reasons (D
         xi != 0 on the basin; backward invariance of the local arc and the line property of Gamma; the choice of R in
         the coverage step) and three presentation points; applied, and Section 9.1 inserted, at 11:30.
- 2026-10-18 11:31  verifier: the complete written proof of Theorem 3.1 (scattering map, with the stronger statements
         now in Theorem 3.1: rates, C^2 of L and Theta, A in C^{2,alpha}, derivative bounds) re-derived independently,
         with symbolic checks of the identities: confirmed.
- 2026-10-18 11:32  verifier: the version of 11:31 (the amendments from the separate audit and the inserted Section
         9.1) checked against the audited draft: confirmed; the artifact index referred to in Section 9.1 still to be
         added.
- 2026-10-18 11:35  separate audit of the complete written proof of Theorem 3.1: confirmed without repair.
- 2026-10-18 11:37  separate audit of the complete written proof of Theorem 3.16 (including the rate for the rescaled
         density on annuli, which the earlier outline lacked): confirmed without correction.
- 2026-10-18 11:44  verifier: the condensed proof of Section 9.2 checked against the full proof. Steps 1-6 confirmed,
         with four one-clause additions; Step 7 (second derivatives) judged an outline as drafted and completed with
         the missing estimates named by the verifier. Additions applied and the section inserted at 11:47.
- 2026-10-18 11:47  verifier: the condensed proof of Section 9.3 checked against the full proof and re-derived, with
         symbolic checks of the identities: confirmed, with wording amendments (equation label, one-sided statement in
         (b), the weighted-integral line of (c), citations and the order of choices in Step 3), all applied; inserted
         at 11:52.
- 2026-10-18 11:52  verifier: inner radius e^-14 -> e^-17 at the three sampled states (eta13 = 0.0744, 0.0773, 0.0802)
         of the two-parameter extension with a_2 = -1.228, independent implementation. Quadratic interpolation
         through these states places the m1 = 1/2 crossing at eta13 = 0.07568 (e^-14) and 0.07580 (e^-17); the
         difference 1.2e-4 is a refinement difference, not an accuracy. The estimated D at the interpolated crossing
         moves by +0.019 (divergence form) and +0.016 (direct form). Confirmed as a measurement; these are estimates
         from sampled states, not a computed matching state. The inner-radius statements of 5.8(vi) and Section 7
         item 5 were amended at 11:57. [Later qualification: the verifier's remark that the shift grows along the
         branch was withdrawn after the 12:39 audit, since the samples are not one continuation path; at
         eta13 = 0.0773 the shift from e^-17 to e^-20 is +0.0008 (12:35); the inner-radius limit of D is not
         established.]
- 2026-10-18 11:55  separate audit of the complete written proofs of Theorems 3.2, 3.3 and 3.13 (global chart,
         the limit S with S - X = O(|X|^p), regularity and measure preservation of S, the leaves and their rates, the
         wall system): confirmed without correction.
- 2026-10-18 12:00  verifier: Section 9.2 as inserted, the restatement of Theorem 3.1 and the edits of 11:47-11:52
         re-derived and confirmed; one optional clause on the cutoffs of Step 7 (applied at 12:12).
- 2026-10-18 12:02  verifier: at a_2 = -1.2 and -1.228 the real x-odd Ritz value nearest 1 again belongs to a vector
         concentrated on a mirror pair of grid nodes, with the largest matching residual of five vectors tested;
         confirmed as a measurement of the discrete map, the continuum x-odd spectrum remains open (5.8(vi) amended).
- 2026-10-18 12:06  verifier: the complete written proofs of Theorems 3.2, 3.3 and 3.13 checked: confirmed; they
         give Theorem 3.13 in a stronger form (S - X = O(|X|^p), S a C^2 diffeomorphism off 0).
- 2026-10-18 12:07  separate audit of the complete written proofs of Lemma 3.7, Theorem 3.8 (a)-(d) and the near-field
         part of (e), and Proposition 3.9 (source estimates without gap condition, the cycle argument behind the
         Poincare-Bendixson step, vanishing on saddle manifolds, the jet test, the C^2 weak coordinate): confirmed
         without correction.
- 2026-10-18 12:12  separate audit of the complete written proofs of Proposition 3.10, Theorem 3.11 (a)-(e) and the
         far-field part of Theorem 3.8(e): confirmed without correction.
- 2026-10-18 12:13  verifier: the inner-radius edits of 11:57 confirmed, with a wording amendment (convergence of D at
         inner radius e^-17 at a_2 = -1.228 is not established by a single step), applied at 12:18.
- 2026-10-18 12:13  verifier: the condensed proof of Section 9.4 (Theorems 3.2, 3.13, 3.3) and the restated
         Theorems 3.2, 3.3 and 3.13 checked against the full proof: confirmed, with one clause added (the reflection
         identity for xi taken from its definition in Section 9.1); inserted at 12:19.
- 2026-10-18 12:14  separate audit of the written uniqueness proof of Proposition 3.15: confirmed with two
         corrections (an auxiliary remark rewritten without division by zero; the regularity hypotheses stated as
         classical hypotheses, without a minimality claim), both applied.
- 2026-10-18 12:15  verifier: the x-odd Arnoldi iteration at a_2 = -1.1 restricted to a smoothed subspace has no real
         Ritz value within 0.68 of 1 (nearest 0.318); confirmed for the smoothed operator at 512 angles, not a
         statement about the continuum spectrum (5.8(vi) amended).
- 2026-10-18 12:21  verifier: the complete written proofs of Lemma 3.7, Theorem 3.8 (a)-(d) and the near-field part
         of (e), and Proposition 3.9 re-derived: confirmed (agrees with the 12:07 audit); they do not cover the last
         clause of Theorem 3.8(e).
- 2026-10-18 12:25  verifier: the condensed proof of Section 9.5 checked against the full proof: confirmed, with one
         wording correction (Step 7 names the steps that give rho = 0 off B(0)) and two notation points; inserted at
         12:29.
- 2026-10-18 12:25  verifier: at 1024 angles the real x-odd Ritz value nearest 1 at a_2 = -1.1 is 0.846, again a
         grid-scale vector, concentrated elsewhere, with true residual 0.9 to 2.5: the 512-angle value 0.969 does not
         persist under refinement (5.8(vi) and Section 7 item 4 amended).
- 2026-10-18 12:27  verifier: the report version of 12:20 (the 12:13-12:15 integrations and Section 9.4 as inserted)
         checked against the previous version: confirmed.
- 2026-10-18 12:34  verifier: the complete written proofs of Proposition 3.10, Theorem 3.11 and the far-field part of
         Theorem 3.8(e) re-derived: confirmed (agrees with the 12:12 audit); the condensed proof of Section 9.6
         confirmed with one wording correction (Step 9: extra sources as in Theorem 3.8(d)) and two recommended
         clauses (Step 8: D xi != 0 on Gamma; Step 7 heading), all applied; inserted at 12:46.
- 2026-10-18 12:34  verifier: the report version of 12:29 (Section 9.5 as inserted and the 12:21-12:27 integrations)
         checked against the previous version: confirmed.
- 2026-10-18 12:35  verifier: inner radius e^-20 at a_2 = -1.228, eta13 = 0.0773 moves D by +0.0008 and m1 by -8e-7
         from their e^-17 values. At this datum the e^-17 and e^-20 values of D agree to about 1e-3; this does not
         establish the inner-radius limit or its accuracy. Only this eta13 value was refined to e^-20, with 512 angles
         and x-even projection. [Qualified after the 13:29 audit: the earlier fitted-crossing shift from e^-14 to
         e^-17 was +0.019 in the divergence form and +0.016 in the direct form. Transferring the +0.0008 shift to the
         crossing gives estimates -0.221 and -0.234, respectively. The crossing was not computed at e^-20 and the
         transfer is unverified. The corresponding statements in 5.8(vi) and Section 7 item 5 were amended.]
- 2026-10-18 12:37  verifier: the written proof of Section 9.7 (Proposition 3.15) re-derived: confirmed under
         f in C^1, s in C^2, with one optional wording point (applied); inserted at 12:46.
- 2026-10-18 12:38  verifier: complex Ritz values of the smoothed x-odd operator at a_2 = -1.1: none within 0.68 of 1;
         largest-modulus pair 0.845 +- 1.225i (5.8(vi) amended).
- 2026-10-18 12:39  second separate audit of the 12:27 version (Section 9 as proofs, consistency, overclaims, numbers,
         format, Section 7): no fatal error in Sections 9.1-9.4; ten findings, all applied at 12:46: the projected
         singular value specified as that of the rectangular Arnoldi matrix; the pitchfork sentence revised (the
         states are not x-even rather than x-odd; the audit's statement that a nonzero bifurcation coefficient is
         needed was corrected by the verifier at 12:52: it is needed for the pitchfork shape only); the x-odd
         instability stated as suggested, not established; the completeness of Section 9 stated relative to Theorem A
         and Theorem B (F2); the inner-radius shift of +0.019 attributed to the two-parameter extension and the trend
         sentence withdrawn; the quadratic-fit crossings 0.07568 / 0.07580 stated with the same estimator; absolute
         integrability of g in Proposition 3.14 (from Theorem 3.1); the trapped-set sentence of 9.2 Step 6 corrected;
         E_m and eta defined in 9.2 Step 7; the artifact index to be identified (not done at that time).
- 2026-10-18 12:44  verifier: the unprojected rotated-datum run at a_2 = -1.0 re-read: it leaves the neighbourhood of
         the x-even fixed point, but it changes the datum and drops the projection together; the unprojected
         iteration did converge at x-even data at a_2 = -1.1 and -1.2, so it is not stated that the projection is
         what makes the iteration converge (Scope paragraph of 5.8). A second-order finite-difference effect does
         not explain the step dependence of the x-odd Rayleigh quotients (their scaling is not of that form).
- 2026-10-18 12:46  separate audit of the complete written proofs of the velocity law, Theorem A and Theorem B (F1),
         (F2), (F4): confirmed with corrections (cutoff specified; uniqueness after the growth bound; the not-o(r^p)
         argument started inside the disk; the Holder exponent of A is every alpha < (1 - gamma)/(1 - p), not the
         endpoint, when p < gamma; periodic orbits nonstationary; (F4) on the open basin), all applied.
- 2026-10-18 12:50  verifier: the written proof of the velocity law, Theorem A and Theorem B (F1), (F2), (F4)
         re-derived (symbolic checks, and an exact nonlinear example for the transport law of (F4)): confirmed,
         with one correction (the not-o(r^p) argument), the same as the audit's, and four optional points (two of them
         the same as audit corrections); all
         applied; inserted as Section 9.0 at 13:00.
- 2026-10-18 12:52  verifier: the report version of 12:46 (Sections 9.6 and 9.7 as inserted, the findings of the
         separate audit as applied) checked against the previous version: confirmed, with one correction (under
         simplicity, transversality, Fredholm index 0 and C^2 smoothness the Crandall-Rabinowitz theorem gives the
         branch; a nonzero bifurcation coefficient is needed only for the pitchfork shape), applied.
- 2026-10-18 13:02  separate audit of the growth classes 1 <= gamma < 2 and of the proposed growth-class sentences of
         Section 2: confirmed with corrections (the orbit comparison under W_2 = o(r) is a necessary condition that
         does not exclude c_l <= 1; profiles meant as global C^3 profiles with the jet; the polynomial solution of
         growth 2 solves the profile equations only in a suitable higher gauge; the "generic outer flow" sentence
         replaced by a statement of what is not proved), all applied.
- 2026-10-18 13:03  verifier: Section 9.0 as inserted, the use of Section 9.0 in Section 9.1 (only Steps 1-6 and (F2);
         no circularity), the status statements of Sections 2a, 3 and 9, and the corrected bifurcation sentence:
         confirmed.
- 2026-10-18 13:04  verifier: the smoothed x-odd Ritz computation of 5.8 repeated at 1024 angles: the largest-modulus
         pair persists (modulus 1.45 against 1.49); the real Ritz value nearest 1 moves from 0.318 to 0.594, so it is
         not converged under angular refinement; 5.8 revised accordingly.
- 2026-10-18 13:10  verifier: the growth-class statements re-derived (twice-subtracted law by independent quadrature
         on exact test densities, uniqueness up to a strain, jet forcing, the condition c_l >= 1/4 + 1/(2 gamma), the
         restricted nonexistence, the families): confirmed, with two optional precisions, applied.
- 2026-10-18 13:17  verifier: the corrected growth-class text and the Section 7, item 1 summary: confirmed, with one
         correction ("subtraction at infinity"), applied. The gauge statement for rho = x^2 was checked exactly (in
         the gauge of the radially truncated integral with only a strain added, x^2 does not solve the profile
         equations; the harmonic cubic and quadratic that make it a solution are unique) and by an independent
         quadrature of the truncated law (relative error <= 1.1e-9). The Section 2 sentences and Section 7, item 1
         replaced; one optional precision in 5.8 applied.
- 2026-10-18 13:18  separate audit of three further routes in S^+ (variational, commuting fields, circulation along
         Gamma) and of the paragraph of 4.4 describing them: the identities confirmed (23 symbolic checks), two items
         with corrections (precise first-variation statement; O(R^{p+1}) with a coefficient that may vanish; the
         closing sentence a suggested direction, not a proved requirement), all applied.
- 2026-10-18 13:23  verifier: the 4.4 paragraph confirmed (exterior derivative re-derived by hand; the oscillatory
         integrand exactly k f^2 (V.e) + O(1/k); the polynomial example, its commuting fields and strain signs, the
         circulation identities and the material-loop law, 25 symbolic and quadrature checks); three optional
         precisions applied; the paragraph appended to 4.4.
- 2026-10-18 13:26  verifier: the integration of the growth-class text checked against the confirmed texts (one
         correction, the order of the timeline, applied); the replacement of the closing clause of Section 7
         confirmed, with its optional fuller form, applied.
- 2026-10-18 13:29  third separate audit, of the 13:18 version (Section 9 as proofs, consistency of repeated numbers,
         Section 7, the proposed growth-class and 4.4 texts): Sections 9.0-9.7 judged complete for the named results,
         the dependency order legitimate, no outlined prerequisite promoted to a complete proof; one error (the
         integer-order matching clause of 9.6 needs C^infinity or an order at most m), one overclaim (the inner-radius
         statement at the crossing of 5.8(vi) and Section 7 rests on one refined datum), one gap (the singular-value
         bound of the rectangular Arnoldi matrix holds for a fixed linear operator only), two inconsistencies (the
         source-eigenvalue clause of Section 7; stale references to a list of omitted steps) and four format points
         (the artifact index; the far-field subtraction; the strain contractions of 4.4; line wrapping). Corrections
         to all points except the artifact index and line wrapping applied at 13:33; verifier check requested. (The
         Section 9.2, Step 7 of that version was later found to be condensed; see 14:12 and 14:38.)
- 2026-10-18 13:36  verifier: the ten corrections in Sections 5 and 8 from a cross-check of the report's numbers
         against the run records, each re-read in its record: confirmed.
- 2026-10-18 13:38  separate audit of complete proofs of Theorems C and D, Proposition 3.4, Theorem 3.5 and
         Proposition 3.12 (26 exact checks): all confirmed; Theorem D to be stated as an explicit covariance (density,
         stream function, velocity and gravity rotated together), the m = 3 case of Proposition 3.4 as the profile
         consequence of Theorem C, and the sentence after Proposition 3.12 with the zero-gradient condition; applied.
- 2026-10-18 13:44  verifier: the corrections of 13:33 checked: seven confirmed; the strain contractions of 4.4 named
         a pair of contractions of fixed sign, replaced at 13:50 by the contractions V.S_iV of the symmetric strains,
         each of which changes sign; one optional precision in 5.8 (the defect of the Arnoldi relation along the Ritz
         direction is of order 0.1, so the conditional bound is not informative) applied.
- 2026-10-18 13:51  separate audit of the complete proofs of Propositions 3.6 and 3.14 (the pairing identity on the
         wall with its Fourier form and the two exclusion classes; the integral of g on the lower half-axis and the
         integrated wall system; 16 symbolic checks): confirmed (one missing plus sign in a displayed estimate of the
         audited proof record; the report text was not affected).
- 2026-10-18 14:03  verifier: Section 9.8 (the proofs of Theorems C, D and 3.5 and Propositions 3.4 and 3.12) and the
         corresponding statement edits re-derived by hand (46 symbolic and quadrature checks, among them the moment
         identity for a density with a generic Hessian, the exterior velocity of an exact homogeneous tail and the
         rotation covariance): confirmed; one optional precision (the role of the zero-gradient condition in
         Proposition 3.12) applied; Section 9.8 inserted.
- 2026-10-18 14:12  separate audit of the condensed Sections 9.8 and 9.9 under the criterion that the report itself
         must contain the complete proof: Theorems C and D and Propositions 3.4 and 3.12 complete; Proposition 3.6
         complete with one correction (the Fourier bound for real k); gaps in Theorem 3.5 (the kernel law for the
         singular homogeneous density in 9.8 Step 4) and in Proposition 3.14 (absolute integrability of g); Section
         9.2, Step 7 condensed with its estimates outside the report, so the higher-regularity part of Theorem 3.1 not
         yet proved in the report. Repairs: Theorems 3.5 and 3.16(b), Sections 9.3 and 9.8 use only A in C^1 and the
         existence of A''(beta); Section 9.2, Step 7 to be written out in full.
- 2026-10-18 14:21  separate audit of Proposition 3.17 (the axis identity in S^+_even), its proof and the two
         test-density computations of the paragraph at the end of 4.2: confirmed; corrections to the wording of the
         exclusion, to the form of the error bound and to one ambiguous sentence of the Conclusion applied.
- 2026-10-18 14:26  verifier: Section 9.9 re-derived (34 checks, among them the Fourier sign and the factor 1/pi of
         the pairing identity, the closed forms of the integrated wall system and the two exclusion classes of
         Proposition 3.6): confirmed; one required status correction (the growth-class statements at the end of
         Section 2 had no status) and three optional precisions applied.
- 2026-10-18 14:29  verifier: correction of the coverage verdict of 14:26: Section 9.2, Step 7 was then condensed, so
         the higher-regularity part of Theorem 3.1, and the version of Proposition 3.14 that used it, were complete
         only given that step; the coverage statements of Sections 2a, 3 and 7 were held back.
- 2026-10-18 14:38  separate audit of the full proof of Section 9.2, Step 7 (rescaled transport on a finite time
         interval, transported cutoffs, the commutator and localized elliptic estimates, the weighted interpolation
         inequality, the two energy inequalities with a mollification argument, the rescaling to the second-derivative
         and Holder bounds, the second derivatives of W, and the C^2 regularity of the scattering map): confirmed; one
         notation correction (the cutoff of the final step has closed support) applied.
- 2026-10-18 14:40  verifier: the repairs of 14:12 to Theorems 3.5 and 3.16(b) and Sections 9.3 and 9.8 re-derived
         (the kernel field of a homogeneous Holder density; the cubic and quartic contradictions from
         A'(beta + t) = 2at + o(t); A''(beta) = 2 B'(beta)^2 > 0 in S^+ from the C^1 signed root): confirmed, with the
         hypothesis line of Section 9.8 corrected so that it no longer cites Section 9.2, Step 7; applied.
- 2026-10-18 14:40  verifier: Section 9.9 rebased on the repairs of 14:12 (Proposition 3.14 uses only the bounds of
         Section 9.2, Step 5): confirmed, with its hypothesis line corrected accordingly.
- 2026-10-18 14:43  separate audit of Steps 2 and 5 of Section 9.10, rewritten to use only first derivatives of the
         conjugation and of the signed root: confirmed without corrections.
- 2026-10-18 14:49  fourth separate audit, of a frozen version containing the edits then under check (coverage of
         Sections 2a and 3 by Section 9, Sections 9.8-9.10 as proofs, overclaims, repeated numbers, format): no
         circular dependency and no fatal gap in the numbered results, the stronger regularity clauses being
         conditional on the separate audit of the new Section 9.2, Step 7; Section 9.10, Step 2 uses only first
         derivatives. Required corrections: categorical statements that density-only information gives no sign,
         narrowed to "no derivation is known"; the statement that a nonexistence proof must contradict one of the
         listed identities, removed; the artifact index named; a band decomposition in 5.8 that mixed two codes,
         reduced to one code; the status wording for edits then under check (met by inserting each edit only after
         its check, recorded here). Seven optional precisions applied, the naming of the interpolation pair in 5.8
         after a check against the run records.
- 2026-10-18 15:08  verifier: the full Section 9.2, Step 7 re-derived sub-step by sub-step from the report text alone
         (36 checks); Section 9.10 and the test-density numbers of 4.2 re-derived (the closed form of the integral of
         w_f/s^2, the two quadratures of I_M within 1e-7 relative of I_M^0, the bound on DW); Section 9.9 as rebased
         and the definition of the artifact index checked. With Step 7 written out, every result of Sections 2a and 3
         has a complete proof in Section 9: confirmed.
- 2026-10-18 15:18  separate audit of a research text on scattering domains S^{-1}(B_R) and distribution functions in
         S^+ (the inertia excess and radial work with their coefficients, the material identity, the band areas and
         the weighted zero-curve length, the localized correction, and the stream-sign test densities): confirmed,
         with two notation repairs (position vectors e_r(theta); the auxiliary angular mode renamed); the scattering
         displacement used is the one already proved in Section 9.3, Step 7. Inserted as 4.16 and Section 9.11.
- 2026-10-18 15:26  verifier: the corrections from the fourth separate audit checked hunk by hunk against the audit
         and re-derived where they contain mathematics (the endpoint term of 5.8 recomputed from the printed
         coefficients, -1.11144 exactly, and the band triple traced to one code; the derivation of the two bounds of
         the 4.2 test family; the interpolation pair of 5.8 against the run records): confirmed, with one required
         change (two further sentences of 5.8 narrowed as the audit proposed; applied). Four optional wording
         precisions applied.
- 2026-10-18 15:30  separate audit of an analysis of the regimes c_l -> 1+ and c_l -> infinity (envelope bounds for
         nonnegative densities, frequency-two resonance, the endpoint p -> 1): its statements confirmed apart
         from one ancillary majorant (false as written and not needed) and two wording cautions, much of it already in
         4.7 and 4.8; it found that Corollary 4.8 understated its own conclusion (under its convergence hypotheses
         (1 - p) times the normalised correction has a nonzero uniform limit). The corollary and the Section 7 summary
         corrected; its new restricted bounds and endpoint tests inserted as Proposition 4.13a with the proof in
         Section 9.12.
- 2026-10-18 15:31  verifier: the 5.8 paragraph on the test of local uniqueness of the x-even fixed points among
         states that are not x-even checked against the run records: numbers confirmed; two wording changes
         required (the method is Newton-GMRES; the records show that the linear model failed on the scale of the
         steps, not that the Jacobian is wrong), applied, with three optional precisions.
- 2026-10-18 16:09  verifier: the insertions of the edits checked at 15:26 and 15:31 compared line by line with the
         checked texts: confirmed. Two optional precisions of the wording of the 15:26 entry applied.
- 2026-10-18 16:15  verifier: Section 4.16 and its proof in Section 9.11 re-derived step by step from the report text
         (symbolic checks of the exact formulas and rationals, and an independent implementation of the velocity law
         for the two test densities of 4.16(d)): confirmed without required changes. Two optional precisions applied
         (a definition in Step 2 of Section 9.11; the scope sentence of the Section 4 opening).
- 2026-10-18 16:16  separate audit of a candidate version of the whole report (saved at 15:34; it contained
         Proposition 4.13a and Sections 4.16, 9.11 and 9.12 before their insertion): the proofs of Sections 9.11 and
         9.12 and the corrected Corollary 4.8 found complete, with no gap, wrong constant or hidden parity assumption,
         and the displayed numbers rechecked; no endpoint reached. Required changes: the notation and norm statement
         of Corollary 4.8; the normalisation in 4.13a(c); the joint-limit criterion of 4.7(iii) and its Section 7
         summary; the proof-status inventories of Sections 2a, 4, 7 and 9, with proof availability separated from
         audit history; removal of five ancillary examples whose arguments were only in the artifacts; the coverage
         statement of the artifact index; an explicit checkpoint statement. Applied, with four optional precisions
         (4.15(i), 4.16, Section 7 item 3, the heading of 8.6); verifier check requested.
- 2026-10-18 16:22  verifier: the insertion of the edit checked at 16:15, with the optional precisions of 16:09 and
         16:15, compared line by line with the checked texts: confirmed.
- 2026-10-18 16:25  verifier: the corrected Corollary 4.8 re-derived from its hypotheses, Proposition 4.7 and Theorem
         3.16 (the constants checked symbolically), and the Section 7 summary and the 15:30 entry read against the
         audit: confirmed, with one required change (the 15:30 entry now records the false ancillary estimate and the
         two wording cautions of the audit; applied) and one optional precision (a definition of J_1[A_*]) applied.
- 2026-10-18 16:39  verifier: Proposition 4.13a and its proof in Section 9.12 re-derived from the report text (all
         formulas and constants checked, 34 scripted checks), and the edits of the openings of Sections 7
         and 9 read: confirmed without required changes. Two optional precisions applied (a citation in Step 2 of
         Section 9.12; a cross-reference to 4.13a at the end of 4.7).
- 2026-10-18 16:40  verifier: the insertion of the edit checked at 16:25, with its required change and two optional
         precisions, compared line by line with the checked texts: confirmed.
- 2026-10-18 16:44  verifier: the insertion of the edit checked at 16:39, with its two optional precisions, compared
         line by line with the checked texts: confirmed.
- 2026-10-18 16:51  verifier: the corrections from the separate audit of 16:16 compared with the audit and the report
         text (formulas re-derived, 18 scripted checks): confirmed, with two required changes to status sentences
         (the status of the growth-class statements of Section 2 and of Corollary 4.10 to be stated where they
         occur; the coverage of the artifact index, which lists proof records by subsection only for Sections
         9.0-9.8) and four optional precisions (the labelling sentence of Section 2a, the definition of c_n in
         Corollary 4.8, the wording of the 16:16 entry, line breaks in three places); all applied at insertion.
- 2026-10-18 16:55  verifier: the insertion of the edit checked at 16:51, with its two required changes and four
         optional precisions, compared line by line with the checked texts: confirmed.
- 2026-10-18 17:03  verifier: a line-length reflow of the whole report compared with the preceding version: the word
         sequence is identical apart from the save-time stamp, and headings and paragraph structure are unchanged.
         Confirmed, with one optional format point (continuation lines that begin with an operator token).
- 2026-10-18 17:05  verifier: the installation of the reflow compared with the checked version: only the save-time
         stamp differs. Confirmed.
- 2026-10-18 17:10  verifier: the format edit for the optional point of 17:03 rebuilt and compared with the installed
         version: the words and the structure are identical, and no continuation line begins with an operator token
         except list items and display alignments. Confirmed.
- 2026-10-18 17:25  verifier: a pre-check of the draft Sections 4.17 and 9.13 (odd perturbations of an x-even
         profile): every step re-derived by hand, the cited inputs located, and the explicit velocity of the test
         perturbation recomputed by direct quadrature of the integral law (agreement to about 2e-16): confirmed, with
         four presentation points (the solution concept along the flow, two citations and one one-line reason;
         applied).
- 2026-10-18 17:34  separate audit of Sections 4.17 and 9.13: reflection, moments and first variations, the test
         perturbation and its ray signs, the residual map and the explicit sequence, the conditional rigidity lemma
         and the backward-flow formula confirmed, with an independent quadrature of the test velocity. Required
         repairs (applied): the growth exponent made explicit and nonnegative, the eigenvalue variation written at the
         base point, the minimum-principle conclusion restricted to the pointwise principle that fails, the solution
         concept and the domain of the backward-flow operator stated, the converse of the kernel equivalence proved.
- 2026-10-18 17:34  verifier: the first candidate of Sections 4.17 and 9.13 rebuilt and compared; all
         cross-references checked and Steps 1-10 re-derived by hand (the signs of the strain matrix, the constants of
         the test velocity, the powers of n in the sequence, the residual map): confirmed, with two optional wording
         points.
- 2026-10-18 17:47  verifier: the revised Sections 4.17 and 9.13 (the audit repairs, the pre-check points of 17:25
         and the first wording point of 17:34 applied) rebuilt and compared hunk by hunk; each changed statement
         re-derived, including the new converse of 4.17(e): confirmed, with three optional wording points.
- 2026-10-18 17:56  verifier: the installed Sections 4.17 and 9.13 and the four preceding timeline entries checked
         against their sources (accurate), and the three wording points of 17:47 (the class of the root variable,
         the scope of the failed minimum principle in Section 7, the name of an annulus constant; applied) checked:
         confirmed.
- 2026-10-18 18:09  verifier: the installed wording points of 17:47 and the timeline entry of 17:56 checked against
         their sources: confirmed.
- 2026-10-18 18:19  separate audit of Section 4.17(f) and Section 9.13, Step 11 (the backward-flow operator in a
         Holder norm): the regularity of the flow, the orbit chart, the construction and admissibility of the test
         sequence, the forcing and its sign, the sequence of 4.17(c) and the dependencies confirmed; one gap (the
         lower bound for the images was written without the images lying in the Holder space; repaired: the
         statement now concerns compact maps into that space agreeing with the operator, as in 4.17(f)).
- 2026-10-18 18:33  verifier: the revised Section 4.17(f), Section 9.13, Step 11 and the changed sentence of Section 7
         rebuilt and compared; every step re-derived by hand, independent symbolic checks of the second-derivative
         display and of the forcing identity, and a quadrature test of the powers of n on an explicit linear model
         field: confirmed, with one optional wording point (the target space in Section 7, item 3; applied in a
         later version).
- 2026-10-18 18:46  separate audit of Section 9.14 (the growth classes gamma >= 1) and the sentences citing it: the
         twice-subtracted law, its regularity and growth, the failure of absolute convergence of one subtraction for
         an explicit density, the Liouville lemma and the forced center strain, the conditional lower bound for c_l,
         the exclusion of densities f(x) and f(x) + h(y), the higher-order subtractions with their harmonic
         ambiguity, and the polynomial solution at growth 2 confirmed; one false documentary statement (Section 0 said
         that the artifact index did not cover the growth classes; repaired).
- 2026-10-18 18:54  verifier: the installed Section 4.17(f), Section 9.13, Step 11 and the timeline entries of 18:19
         and 18:33 checked against their sources: confirmed.
- 2026-10-18 18:54  verifier: Section 9.14 and the changed sentences rebuilt and compared; every step re-derived by
         hand, independent symbolic checks, and independent quadratures of the defining integral for the layer
         densities and of the compact field of the truncated density x^2: confirmed, with the Section 0 repair of the
         separate audit required and three optional wording points (all applied).
- 2026-10-18 19:03  separate audit of Section 9.15 (Theorem 4.9, Corollary 4.10, Remark 4.11) and the revised
         statements of Section 4.8: the rescaling and its normalisations, the nullcline graphs and the uniformity of
         their error term, the compactness of the zero set, the structure of the regular level sets, the Morse-Sard
         step, the product bound, the exclusion of analyticity, the canonical velocity of the limit, the escape of
         the strain, the compactness behind Corollary 4.10, the far-field formulas of Remark 4.11 and the
         dependencies confirmed; one inaccurate sentence (the end of Step 8 attributed to Steps 4-8 the velocity
         identity proved in Step 9; repaired).
- 2026-10-18 19:17  verifier: Section 9.15, the revised Section 4.8 and the changed sentences rebuilt and compared;
         every step re-derived by hand, independent symbolic checks of the rescaling and of the far-field formulas,
         and an independent spectral solution of the angular equation of Remark 4.11 for three densities: confirmed.
- 2026-10-18 19:26  separate audit of Proposition 3.15a and Section 9.16 (the layered ansatz quadratic in x for the
         density and cubic in x for the stream function): the coefficient equations, the strain at the centre, the
         lemma on b k' = k, the constancy of the cubic stream coefficient, the reduction to Proposition 3.15, the
         singular linear system, the branch with a nonzero cubic coefficient, the parity conclusion and the local
         solution spaces (without the centring condition W(0) = 0 there are local solutions with the jet) confirmed;
         no repair.
- 2026-10-18 19:27  verifier: Proposition 3.15a, Section 9.16 and the changed sentences rebuilt and compared; every
         step re-derived by hand, with independent symbolic checks of the coefficient equations and of the local
         solution spaces described by the separate audit: confirmed, with two optional wording points (a blank line
         before Section 9.16; the qualifications of "exactly two" in Section 7, item 1; both applied).
- 2026-10-18 20:17  verifier: the research texts behind Propositions 2.2 and 3.15b (polynomial solutions of density
         degree at most three for every l and at most six for l > 1/4 off resonances; layered solutions of degree
         at most three in x for l > 1) checked before installation; every step re-derived, independent symbolic
         tests and a Groebner cross-check in degrees three and four, including resonant l: correct as stated.
- 2026-10-18 20:26  separate audit of Proposition 2.1 and Section 9.17 (truncation limits of the defining integral):
         the kernel and the local term, part (a) for S, the strain moments of part (b) and the family without a
         limit, the decomposition and remainder bound of Step 4, the profile conditions G = 0, J = -pi/12 and
         I = i pi (c_l - 1/2), the disk, ellipse and reflection arguments confirmed; one false clause (that no family
         of centered ellipses gives the polynomial velocity: the ellipses with semi-axes R and B_R, B_R/R -> infinity,
         give it at c_l = 1/2; repaired, with the exclusion restricted to homothetic copies of a fixed ellipse), a
         missing minus sign in Step 3, an unnecessary continuity argument in Step 6 and the scope of "selected" and
         "artifact" (all repaired); disks with moving centres and rotated ellipses added and confirmed.
- 2026-10-18 20:28  separate audit of Proposition 3.15b and Section 9.18 (layered solutions of degree at most three
         in x, stream function of any degree in x): coefficient equations and jet consequences, the descent and
         exponent count, the exclusion of M > N + 1, the cubic case, the reduction to Proposition 3.15 and the
         arbitrary-degree reduction for M > N >= 2 confirmed on all nine audit items; no gap found.
- 2026-10-18 20:38  verifier: Proposition 2.1, Section 9.17 and the changed sentences rebuilt and compared, before
         and after the repairs of the separate audit; every step re-derived by hand, independent symbolic checks and
         independent quadratures of the truncated integrals of x^2 (disks with any centre, fixed and rotated
         ellipses, tall ellipses, tuned truncations at four values of l): confirmed, with one required repair of
         scope in the concluding paragraph (the dependence on the truncation is proved for rho = x^2, not for every
         density of growth two; applied) and three optional points.
- 2026-10-18 20:39  separate audit of Proposition 2.2 and Section 9.19 (uniqueness of the polynomial solution):
         the squarefree harmonic top part, the cubic equations, the formal square root and Gauss's lemma, the
         Cauchy data on the axis and the critical-point eliminations confirmed; no mathematical gap; the pointer
         in the statement to Proposition 3.15b could not be checked from the audited sources (see 20:45).
- 2026-10-18 20:45  verifier: Propositions 2.2 and 3.15b, Sections 9.19 and 9.18 and the changed sentences rebuilt
         and compared word by word; both sections compared step by step with the research texts and re-derived;
         independent tests of the kernel, the resonances and both layered alternatives: confirmed, with one
         required repair (the pointer to Proposition 3.15b omitted its hypothesis l > 1; applied) and two
         optional points.
- 2026-10-18 20:51  verifier: the installed report of 20:41 checked against the expected text; the combined
         candidate with Propositions 2.2 and 3.15b and the changes to Proposition 2.1 and Section 9.17 rebuilt
         byte-identically from its sources and compared word by word; the pointer to Proposition 3.15b checked
         against its hypotheses: confirmed, no required repair; one recommended layout point and one optional
         wording point.
- 2026-10-18 21:12  verifier: the installed report of 21:04 checked against the expected text, including its five
         new timeline entries: confirmed; the layout candidate with the two points of 20:51 applied (a blank
         line before Proposition 3.15b; "for c_l > 1" in Section 7, item 1) rebuilt and compared word by word:
         confirmed, no other word changed.
- 2026-10-18 21:25  verifier: the wording and layout candidate (the formal solution of the task statement named as
         such; the Section 3 preamble; the title of Section 9.14, Step 12 and the added sentence that x^2 does
         not solve the equation with the radial inverse and a linear velocity; uniform names for the checks;
         the kernel bounds in Section 9.17, Step 3 attributed to their sources; "x^2 solves the profile
         equations" in place of "x^2 is a profile") rebuilt byte-identically and compared word by word, every
         changed word assigned to a listed item, the two changes with mathematical content re-derived:
         confirmed, with two recommended layout repairs and three optional points.
- 2026-10-18 21:35  separate audit of the research text behind Proposition 2.3 (growth classes 1 <= gamma < 2 with
         W_2 = o(r)): the flow and the bound beta >= 1/gamma, the vanishing on orbits in thin x-sectors, the
         limiting directions, the zero orbits toward e_1 and -e_1, the square root rho = xi^2 when 0 is the only
         zero of V and the x-even exclusion confirmed; no gap found.
- 2026-10-18 21:35  separate audit of Proposition 2.3 and Section 9.20 (report version): the statement and the
         conclusions of Steps 1-8 confirmed; three omitted arguments supplied (in Step 3, that orbits with rho != 0
         escape; in Step 6, the derivatives of the integrand; in Step 7, that every orbit leaving 0 tangentially to
         the y-axis lies in the zero set), all applied; no change to the statement.
- 2026-10-18 21:46  verifier: Proposition 2.3 and Section 9.20 (the version sent for the separate audit) checked
         step by step by hand and re-derived (the flow, the limiting directions, the zero orbits, the square root,
         the x-even exclusion): confirmed, no error found; two recommended additions (that orbits with rho != 0
         escape; that no orbit outside the zero set leaves 0 tangentially to the y-axis) and three optional
         points; both additions and one optional point are among the repairs of the separate audit.
- 2026-10-18 21:49  verifier: the installed report of 21:36 checked against the expected text: confirmed; the
         candidate with Proposition 2.3, Section 9.20 with the three repairs of the separate audit, the pointers
         and the two layout repairs of 21:25 rebuilt byte-identically from its sources and compared word by word,
         the three repairs re-derived: confirmed, no required repair.
- 2026-10-18 22:00  separate audit of the research text behind Proposition 2.4 (the far field in the growth classes):
         the precompactness and the layered form of the rescaled limits, the bound o(r^gamma) for beta gamma > 1,
         the homogeneous limits, the radial rates under a power bound on W_2, the layered expansion at
         beta gamma = 1 and the exclusions under the Hessian bound confirmed; one side remark of the research text
         that the report does not use (on affine terms in the velocity) corrected.
- 2026-10-18 22:06  separate audit of Proposition 2.4 and Section 9.21 (report version) and of the pointer sentences
         in Section 2 and Section 7, item 1: the statement against the proof, the rescaled limits and their
         equations, the rates under the power bound, the layered far field, the Hessian bound and the
         cross-references confirmed; no correction.
- 2026-10-18 22:12  verifier: the installed report of 22:00 checked against the expected text: confirmed.
- 2026-10-18 22:23  verifier: Proposition 2.4 and Section 9.21 (report version) checked step by step by hand against
         the cited steps of Sections 9.14 and 9.20 and Proposition 2.3, with exact checks of the scalings and limit
         equations; the pointer sentences and the two audit entries checked: confirmed, no error found; one
         optional notation point (p = 1/beta beside p = 1/c_l).
- 2026-10-18 22:34  verifier: the installed report of 22:29 checked against the expected text: confirmed.
- 2026-10-18 22:38  separate audit of the research text behind Proposition 2.5 (the weak orbits and x-even profiles
         with nondegenerate zeros): the uniqueness of the orbits with directions e_1 and -e_1 and the arcs of
         large circles, the flow topology with nondegenerate zeros (with the bound nu > 1 at saddles), the x-even
         exclusion at beta gamma = 1 and the shorter route through Proposition 2.4(b) confirmed; no correction.
- 2026-10-18 22:41  separate audit of Proposition 2.5 and Section 9.22 (report version) and of the pointer sentences
         in Section 2, Proposition 2.3(c) and Section 7, item 1: the uniqueness of the weak orbits and the arcs,
         the zeros under nondegeneracy (including a Jordan block at l = 1), the transfer of Section 9.5, Steps 3-5,
         the two axis orbits near 0, the amplitudes and the contradiction, the scope sentences and the
         cross-references confirmed; no correction.
- 2026-10-18 22:56  verifier: Proposition 2.5 and Section 9.22 (report version) checked step by step by hand, with
         the pointer sentences and the two audit entries; confirmed, with one required wording repair, applied:
         in Propositions 2.4 and 2.5 the extra hypotheses are now said to be not derived here from C^3 regularity
         and the growth bounds (instead of not implied by them, which the report does not prove).
- 2026-10-18 23:08  verifier: the installed report of 23:06 checked against the expected text: confirmed.
- 2026-10-18 23:12  separate audit of Proposition 2.5(d), (e) and Section 9.22, Step 7 (report version) and of the
         pointer sentences in Section 2, Proposition 2.3(c) and Section 7, item 1: the reduction to the dichotomy
         of Step 6, the angle rate along orbits with direction e_2, the comparison with the axis (by the gradient
         bound, and by evenness with the Hessian bound), the comparison at equal heights and the parameter ranges
         confirmed; one scope sentence at the end of Proposition 2.5 corrected (other results, such as Proposition
         2.4(c), exclude further cases), and the range of c_l made explicit in two pointer sentences.
- 2026-10-18 23:26  verifier: Proposition 2.5(d), (e) and Section 9.22, Step 7 (report version) checked step by step
         by hand, with numerical checks of the angle bounds, of the parameter ranges and of the rate on a
         manufactured flow; the corrected scope sentence, the explicit ranges of c_l and the audit entry checked:
         confirmed, no required repair. The verifier withdrew its earlier confirmation of the closing sentence of
         Proposition 2.5 in the previous version, which overstated what the report leaves open (Proposition 2.4(c)
         excludes some of those densities); no proof was affected.
- 2026-10-18 23:27  verifier: Section 5.8(vii) (parity-free tests at one x-even state) checked against the stored
         runs, in checks made between 19:19 and 23:27: the Hessenberg residuals and the comparisons of the linear
         response columns recomputed at 256, 512 and 1024 angles and read against the acceptance rule, the
         exit-angle sensitivities and the switching separatrix cells recomputed with an independent velocity and
         orbit tracer, the defects of the states returned by the amplitude continuation recomputed with an
         independent evaluator at 256 and 512 angles, and every figure of the text checked: confirmed, no required
         change. The linear x-odd response is not established at any of the three resolutions.
- 2026-10-18 23:32  verifier: the installed report of 23:28 checked against the expected text: confirmed.
- 2026-10-18 23:35  separate audit of the extension of Proposition 2.2 (density degree seven under NR; parity,
         degree eleven and a repeated factor when x^2 divides the density; no density x^2 (by + g(x))^k) and of
         Section 9.19, Steps 15-21, with the pointer sentences in Section 9.19, Step 7 and Section 7, item 1: the
         axis equation in all degrees, the multiplicity lemma, the parity induction, the exclusion of the graph
         powers, the degree-eleven count and the cases deg P = 2, 3 confirmed; three wording repairs made (the
         closing sentence of Proposition 2.2 states NR for the degree-eleven case, the Section 7 pointer states that
         k is a positive integer and that b and g are real, and Step 20 separates degree in the original coordinates
         from degree after the change of coordinates).
- 2026-10-18 23:38  verifier: the installation text of Section 5.8(vii), with the changed sentences of Section 5.8
         and Section 7, item 4 and the new timeline entries, rebuilt from the confirmed draft and checked against
         the stored runs: confirmed for installation.
- 2026-10-18 23:44  verifier: the extension of Proposition 2.2 and Section 9.19, Steps 15-21 (report version, before
         the audit repairs) checked step by step by hand, the multiplicity lemma included, with symbolic checks of the
         resonant set, the axis equation, the exclusion of the graph powers and the cases deg P = 2, 3: confirmed; the
         Section 7 pointer needed the statement that k is a positive integer (k = 0 gives rho = x^2), which the
         separate audit had already supplied.
- 2026-10-18 23:46  verifier: the installed report of 23:38 checked against the expected text: confirmed.
- 2026-10-18 23:47  verifier: the version with the three audit repairs, rebuilt from the confirmed draft and checked
         against it and against the audit: confirmed for installation.
- 2026-10-18 23:55  separate audit of Proposition 2.6(a)-(c) (amplitude rigidity and the exclusion without symmetry of
         the configuration in which V vanishes only at 0) and of Section 9.23, Steps 1-8, on a version before part (d)
         and Step 9 were added, with the pointer sentences and the ranges: the interior gradient bound with its
         constants, the derivative bound of (a), the scattering coordinate Y and its bound, amplitude rigidity with
         both amplitudes positive, the Taylor contradiction above the zero line, the parameter ranges and the
         conversions in the pointers confirmed; one wording point (a sentence of the closing paragraph of that
         version, saying that nothing was claimed about densities whose velocity has further zeros, overlooked part
         (a)); that sentence is not in the present text.
- 2026-10-18 23:58  verifier: the installed report of 23:49 checked against the expected text: confirmed. The entry at
         23:44 said that the multiplicity lemma had been checked symbolically; it was checked by hand only, and that
         entry has been corrected.
- 2026-10-19 00:03  verifier: Proposition 2.6(a)-(c) and Section 9.23, Steps 1-8 (report version, before part (d) and
         Step 9 were added) checked step by step by hand, with symbolic checks of the integral and the constants of
         the interior gradient bound, the exponents, the equivalences of the conditions, the choice of k and the
         ranges, and checks on an exact rational grid of 20000 parameter points: confirmed; the one wording point was
         the same as that of the separate audit of 23:55, and that sentence is not in the present text.
- 2026-10-19 00:07  separate audit of Proposition 2.6(d) (no assumption on the zeros of V) and of Section 9.23, Step
         9, with the closing paragraph of Proposition 2.6, the titles and the pointer sentences in the growth-class
         paragraph of Section 2 and in Section 7, item 1: the transfer of Steps 1-6 without the assumption that V
         vanishes only at 0, the classification of points by their forward orbits, the amplitude formula with
         amplitudes of either sign, the two Taylor estimates at the zero line, the exclusion of beta != 1 and the form
         rho = A Y for beta = 1 confirmed; one wording repair made (the opening of Step 9 names the unconditional
         inputs of Step 1 instead of all of Steps 1-3).
- 2026-10-19 00:09  verifier: Proposition 2.6(d) and Section 9.23, Step 9 (report version, before the wording repair
         of 00:07) checked step by step by hand, with symbolic checks of the two Taylor estimates, the exponent
         identity and the case p = 1, and checks on an exact rational grid of 20000 parameter points of the interval
         for k, the argument with two values of k and the condition of Step 6: confirmed, no required repair. The
         verifier made the same wording point as the separate audit and suggested two additions (the reason why
         r(s) > 0 in Step 4, and a pointer from Proposition 2.3(c) to Proposition 2.6(d)), which have been made.
- 2026-10-19 00:11  verifier: a test of Proposition 2.6(d) on the layered densities rho = A_+ y_+^p + A_- (-y)_+^p
         (p = 1/beta) with W_2 = 0 (W_2 extended by truncated velocities as in the entry of 00:31), which solve the
         transport equation and the elliptic law for every beta: such a density is C^2 with the Hessian bound only for
         p = 1 and A_- = -A_+, that is rho = A y, in agreement with (d); no proof rests on this test. A remark on the
         stratified density rho = A y suggested by this test was withdrawn after the audit of 00:20.
- 2026-10-19 00:14  verifier: the repeat of the 1024-angle pair of Section 5.8(vii) with 40 Krylov vectors, recomputed
         from the stored data (residual diagnostics, column comparisons with the 25-vector pair, the rule): the pair
         fails the rule, and the 1024 column depends on the Krylov dimension. The sentence on this repeat in 5.8(vii)
         reports these results.
- 2026-10-19 00:19  verifier: the report version with Proposition 2.6(d), Section 9.23, Step 9 and the repairs of
         00:07 and 00:09, rebuilt from its sources and compared line by line with the version checked at 00:09:
         confirmed, including a remark after (d) on the stratified density rho = A y, which was withdrawn after the
         audit of 00:20.
- 2026-10-19 00:20  separate audit: the pointer from Proposition 2.3(c) to Proposition 2.6(d), the remark on the
         stratified density rho = A y after (d), and the opening of Section 9.23, Step 9. The pointer and the opening
         were confirmed. The remark has a gap: Section 9.14 defines W_2 only for densities with the jet (for rho = A y
         one of its subtracted integrals diverges at 0), and the remark holds only with an explicit extension of the
         definition of W_2. The remark was withdrawn.
- 2026-10-19 00:31  verifier: the gap found in the audit of 00:20 confirmed; the verifier withdrew its own
         confirmations of the remark on rho = A y (entries 00:11 and 00:19). With W_2 extended by truncated
         velocities, W_2 = lim (U_R - U_R(0) - DU_R(0)X) as R -> infinity, where U_R is the Biot-Savart velocity of
         chi(X/R) rho(X) for a smooth compactly supported radial chi equal to one near 0, one has W_2 = 0 for
         rho = A y: checked by hand (mode-2 Green function) and by direct quadrature. The remark was not reinstated.
- 2026-10-19 00:37  verifier: the installed report of 00:31 rebuilt from its sources and compared with the candidate
         confirmed at 00:19: confirmed; it differs from that candidate exactly by the announced changes (the remark on
         rho = A y removed, one sentence added to Section 5.8(vii), Section 6 and the date line).
- 2026-10-19 00:44  verifier: Proposition 2.6(e) and Section 9.23, Steps 10 and 11 (working draft, before the repairs
         below) checked step by step by hand against Section 9.23, Steps 1-9: the band at 0 with rho = u^2 for a C^1
         coordinate u and its area bound, the transfer of Step 9 up to (9.23.6) without the Hessian bound and without
         assuming that V vanishes only at 0, the bound on Y near 0, the area comparison with the condition
         beta > 1 - delta/2, the consequences and the pointer sentences: confirmed. One required repair (the
         hypothesis sentence of (e) could be read as imposing beta > 1 - delta/2 in one alternative only) and one
         optional precision (in Step 11 the sign of rho near 0 comes from Step 10) were made.
- 2026-10-19 00:48  verifier: a proof, offered for independent checking, that the far-field coefficient A of every
         profile in S vanishes on a set of directions of positive measure or has a zero at which A' = 0 and near which
         A takes positive values (the area of the image under Phi_T of a shrinking band at 0 compared with the area of
         the region outside the circle of Theorem 3.1 reached in time at most T); this was Proposition 3.18(b) in the
         version of 01:27 and is implied by the present Proposition 3.18(b).
- 2026-10-19 00:50  separate audit of Proposition 2.6(e), Section 9.23, Steps 10 and 11 and the changed pointer
         sentences: the backward invariance near 0 and rho = u^2, the transfer of Step 9, the bound on Y, the area
         comparison and the consequences confirmed. It made the same point on the hypothesis sentence of (e) as the
         verifier at 00:44 and one further wording repair (the closing paragraph of Proposition 2.6 attributed
         rho = u^2 near 0 to the jet alone; it follows from the backward flow, transport and the jet), both made.
- 2026-10-19 00:52  verifier: the candidate with Proposition 2.6(e) rebuilt from its sources and compared with the
         draft checked at 00:44: same mathematics, confirmed, with the repair of the hypothesis sentence of (e)
         required before installation.
- 2026-10-19 00:55  verifier: the separate audit of 00:50 compared with the checks of 00:44 and 00:52: consistent; its
         further wording repair confirmed (rho = x^2 - y^4 has the jet and takes negative values near 0, so the jet
         alone does not give rho = u^2).
- 2026-10-19 00:59  verifier: scope of the claim of 00:48: if a branch of the zero curve Gamma of rho at 0 is
         unbounded, the argument of Section 9.6, Step 8 already gives a zero of A at which A'' > 0; the claim adds
         information only when both branches are bounded.
- 2026-10-19 01:01  separate audit of the first version of Proposition 3.18 (sublevel areas; a zero of A at which
         A' = 0) and Section 9.24: confirmed; no assumption on the zeros of V is used. Its wording points (the band
         lies in a fixed coordinate rectangle at 0; in S^+ the conclusion already follows from Theorem 3.2) were made.
- 2026-10-19 01:09  separate audit of Proposition 3.18 with part (b) in the form of 00:48 and of Section 9.24,
         Steps 1-8: confirmed item by item, with exact arithmetic checks of the exponents and of the integral over the
         neighbourhoods of simple zeros. Its optional points (the variable radius in Step 4 distinguished from the
         fixed radius, null sets under Theta and Theta^(-1), notation) were made.
- 2026-10-19 01:09  verifier: the repaired candidate with Proposition 2.6(e) compared with the candidate
         checked at 00:52: the four changed passages are exactly the announced repairs; confirmed.
- 2026-10-19 01:10  verifier: the candidate with Proposition 3.18 rebuilt from its sources and checked line by line
         against Section 9.24: confirmed for installation, with two optional precisions (the band in a fixed
         coordinate rectangle, and a sentence on an unbounded branch of Gamma), both made.
- 2026-10-19 01:11  verifier: a separate audit, commissioned by the verifier, of the proof of 00:48 read and checked:
         confirmed independently. The same audit gave two stronger results, re-derived by the verifier and
         confirmed: two arcs of {A > 0} whose endpoints are zeros of A with A' = 0 (a flux identity between a
         small circle around 0 and the circle of Theorem 3.1), and J_p[A] not identically zero for every profile
         in S. These are Proposition 3.18(b) and (c).
- 2026-10-19 01:13  verifier: the installed report of 01:03 rebuilt from its sources: confirmed; it differs from the
         candidate confirmed at 01:09 exactly by the date line and Section 6, and the new Section 6 entries are
         accurate.
- 2026-10-19 01:15  verifier: the revised candidate checked against the candidate of 01:10: the band wording, the
         scope sentence of 00:59, the points of the audit of 01:09 and the new Section 9.24, Step 9 (now Step 8: an
         unbounded branch of Gamma gives a zero of A with A'' > 0) confirmed for installation. One optional precision
         in Step 9 (monotonicity of y along orbits on the local arc) was made.
- 2026-10-19 01:17  separate audit of the same revision: confirmed. One error in a dependency description (Step 9 said
         that it did not use Steps 2-7, but it cites Step 5) was corrected, and three optional clarifications (in the
         paragraph after Proposition 3.18 and in Section 7) were made.
- 2026-10-19 01:19  separate referee reading of the whole report of 01:03 (its statements, summaries, proof
         destinations and repeated numerical values; the proofs of Section 9 were not re-derived): every numbered
         proof destination correct (the overbroad scope of the references to Section 9.14 excepted), no unexplained
         disagreement between repeated numerical values, and no restricted exclusion presented as full nonexistence.
         Fourteen required corrections of scope, hypotheses, notation and proof-status labels, mainly in the summaries
         of Section 0 and Section 7, and four optional ones. All were made, several adapted to the current text,
         except one malformed replacement (its expression for the transverse curvature of the vertical velocity was
         wrong; the notation point it served was made elsewhere) and one optional definition whose premise was false
         (the names concerned are defined where they first occur).
- 2026-10-19 01:28  verifier: the separate audit of 01:17 read and checked: confirmed; the dependency error it found
         had been missed in the check of 01:15 and was corrected before installation.
- 2026-10-19 01:28  verifier: the transport residual V.grad rho - rho of the three base states of Section 5.8
         recomputed with a velocity and a differentiation independent of the solver: confirmed in the core to two
         digits, with the order-one residual confined to the jump curve and the separatrix of the strong-exit sector
         (about 1e-3 elsewhere in the deep core with local angular differences at 512 and 1024 angles); qualified in
         the outer region, where on -2 <= log r < 2 the residual with the independent velocity is about 1e-5 at 512
         and 1024 angles, against 4.5e-7 and 4.3e-7 with the solver's own velocity (2.3e-5 and 2.0e-5 at 256 angles).
         The ratio across the jump agrees with the axis mismatch D. These discrete states are not profiles.
- 2026-10-19 01:31  verifier: the installed report of 01:27 rebuilt from its sources: confirmed; it differs from the
         candidate checked at 01:15 by the dependency correction and three optional clarifications of the audit of
         01:17, the precision of 01:15, the date line and Section 6, and the new Section 6 entries are accurate.
- 2026-10-19 01:34  separate audit of Proposition 3.18(b), (c) in their present form and of Section 9.24, Steps 5-8:
         confirmed, with one error: in Step 6 an integral along an arc was written as a signed integral, which is
         negative at one end of the arc, while positive asymptotics were stated. Corrected by integrating over arcs
         (both sides of (9.24.4) are positive); the conclusions are unchanged. Three optional clarifications (two
         components of {A > 0} are asserted, not exactly two; the regularity used for Proposition 3.18(c); the
         wording of Section 4.5) were made.
- 2026-10-19 01:35  verifier: the candidate with Proposition 3.18(b), (c) and Section 9.24, Steps 6 and 7 rebuilt from
         its sources and checked line by line: confirmed, with one required precision: Proposition 3.18(b) and Section
         7, item 2 are to assert at least two components of {A > 0}, which is what the proof gives. One optional
         wording point in Section 9.8, Step 4 was made at installation.
- 2026-10-19 01:36  verifier: the audit of 01:34 read and checked: its sign error confirmed; it had been missed in the
         check of 01:35. The argument is intact with unsigned integrals.
- 2026-10-19 01:39  verifier: the repaired candidate rebuilt from its sources: both corrections made and correct;
         confirmed for installation.
- 2026-10-19 01:49  verifier: the installed report of 01:42 rebuilt independently from its sources: confirmed; it
         differs from the candidate confirmed at 01:39, with the wording point of 01:35, exactly by the date line and
         Section 6, and the new and extended Section 6 entries are accurate. The verifier also noted that the entry of
         01:17 should speak of three optional clarifications, as that of 01:31 does; corrected.
- 2026-10-19 01:55  verifier: the outer residual of 01:28 tested by a comparison of three velocities: it is the
         second-order radial discretisation error of the solver's velocity routine (the Richardson extrapolation of
         that routine agrees with the independent velocity to 3e-8 rms on -2 <= log r < 2). In the core the velocity
         sets the residual floor only for log r < -8; on -8 <= log r < -2 the angular resolution sets it.
- 2026-10-19 02:04  verifier: consistency read of the installed report of 01:42 against its proofs, the numerical
         report and the run records. Two required repairs: the range |X| >= 1 of the bound on W in Theorem A, and the
         third-seed values of lambda in Section 5.7 and Section 7, item 4, which did not match the run records. Two
         recommended additions: the Hessian alternative of Proposition 2.6(e) in its three summaries, and the notation
         sentence for W_2 in Section 3. All four were made. Of the optional points, the two on the opening and closing
         paragraphs of Section 4.15 were made by the corrections of 01:19; a pointer to Section 9.3, Step 3 and three
         precisions of run records in Section 5 were made after 02:18; the rest (on wording and cross-references) were
         not.
- 2026-10-19 02:18  separate audit of the revision made after 02:04 (the corrections of 01:19 and 02:04 and a new
         sentence on the residuals of Section 5.8(vii)), against the report of 01:42, the verifier's records and the
         numerical report: every change faithful except one numerical error in the new sentence, which attributed the
         value 4e-7 obtained with the solver's own velocity to all three resolutions (at 256 angles it is 2.0e-5);
         required precisions on the radial bands, resolutions and differentiation behind that sentence, on the range
         of l left open by transport alone (Section 4.7(v)), and on the two summaries of Proposition 4.12; one
         indentation error in Section 7. All were corrected.
- 2026-10-19 02:24  verifier: the revision of 02:08 (the corrections of 01:19 and 02:04 and the new residual sentence
         of Section 5.8(vii)) rebuilt identically from its sources and checked change by change against the
         statements, the earlier checks and the numerical records: confirmed for installation once three points were
         fixed (the solver-velocity residual of the new sentence attributed to all three resolutions, the indentation
         of Section 7, item 6, and the description of the referee reading of 01:19 in this section); its four
         recommended precisions coincided with those of the audit of 02:18. All were made, together with three
         optional wording points (in Section 0, in Section 4.14(f) and the opening of Section 4.15, and in Section 7,
         item 1).
- 2026-10-19 02:28  verifier: the corrected revision rebuilt identically and checked change by change against the
         audit of 02:18, the check of 02:24 and the numerical report: every change correct, and every required and
         recommended point of 02:18 and 02:24 met in the body; two required corrections in this section (the
         descriptions of the readings of 01:19 and 02:04), both made. Two optional precisions of the residual sentence
         of Section 5.8(vii) (the windows around the strong exits excluded from the core statistic, and "consistent
         with" in place of "corroborate") were also made.
- 2026-10-19 02:37  verifier: the revision with the optional points of 02:24 and 02:28 rebuilt identically and checked
         change by change against its sources: every change correct, every required, recommended and optional point of
         02:24 and 02:28 applied, and the draft of this section accurate. Confirmed for installation.
- 2026-10-19 02:40  verifier: the installed report of 02:39 rebuilt independently from its sources: confirmed; it
         differs from the candidate confirmed at 02:37 exactly by the save line and Section 6, and the new Section 6
         entries are accurate.
- 2026-10-19 02:49  separate referee reading of the whole report installed at 02:39 (read before installation, without
         the Section 6 entries added then; its statements, summaries, proof destinations and timeline entries; the
         proofs of Section 9 were not re-derived): twelve required corrections (three of a non-implication worded as a
         proved one, "not consequences of" for hypotheses not derived here; one of the dependency paragraph opening
         Section 9; one of the reading of the node diagnostics at the m1 = 1/2 crossing in Section 5.8(iii); and seven
         of timeline entries on interpolated crossings, sampled continuation stages, inner-radius refinements and the
         description of an audited result) and seven optional ones, among them the naming of the construction of
         4.7(v) among the outlined results. All were made, several adapted to the numerical records, except one
         optional correction whose premise does not hold for the installed text.
- 2026-10-19 02:51  verifier: an analysis of the renormalised flux in S^+ (the source of Proposition 3.17a and
         Section 4.18) re-derived step by step against the statements it uses, with numerical evidence (not proof) on
         manufactured fields for the curvature law and high-precision evaluations of the finite parts for A_l:
         confirmed as research text. It proves no nonexistence and no bound on c_l. The verifier noted that for 4l = 5
         and 7 the finite part of A_l^(-2l) on each arc is not zero. [Corrected by the verifier at 03:12: the remark
         also said that these values agree with the integer case of the source; for integer 4l that case gives a
         continued value of the angular integral, which in general differs from the finite part.]
- 2026-10-19 02:59  verifier: the corrections of 02:49 checked in advance against the text and the numerical records:
         the twelve required corrections confirmed (one graded recommended), the optional correction with a false
         premise confirmed as not applicable, and two additions recommended for one timeline entry (its verdict and
         the e^-20 shift), which were made.
- 2026-10-19 03:05  separate audit of Proposition 3.17a, Section 4.18 and their proofs in Sections 9.25 and 9.26,
         every step re-derived: correct with repairs. The proof that the second moment family implies transport for an
         arbitrary density with the jet and the growth of S used the decay of profiles before transport was
         established; the repaired proof works with the growth exponent of the class until transport is proved.
         Further repairs: a step missing from a citation in Section 9.25, a clash of notation for a Holder exponent in
         Section 9.26, the sign convention of the integer case of 4.18(c), and the linear independence and the scope
         of the angular family of 4.18(e). All were made; its correction of the dependency paragraph opening Section 9
         was superseded by the corrections of 02:49.
- 2026-10-19 03:12  verifier: the revision of 02:54 (Proposition 3.17a, Section 4.18, their proofs in Sections 9.25
         and 9.26, the proof pointers and the Section 7 summary) rebuilt identically from its sources and checked step
         by step, with numerical evidence (not proof) for 4.18(c) on an explicit model with every property that its
         proof uses: confirmed apart from one required repair, the same as the main point of the audit of 03:05 (the
         part of 4.18(d) on arbitrary densities with the jet and the growth of S), one recommended wording point in
         4.18(b) and two optional ones in 4.18(e). All were made.
- 2026-10-19 03:18  separate audit of the repaired passages of the revision of 03:09 (the second moment family for an
         arbitrary density with the jet and the growth of S before transport is known, the integer case of 4.18(c),
         the angular family of 4.18(e), the citations of Sections 9.25 and 9.26, and the dependency paragraph opening
         Section 9, with a scan of Section 9 for references to later subsections), every step re-derived: all correct
         as printed; no change required.
- 2026-10-19 03:26  verifier: the revisions of 03:09 and 03:19 and a dry run of the installation rebuilt identically
         from their sources; the corrections of 02:49 as applied, the repairs of 03:05 (the class-S part of 4.18(d)
         re-derived step by step) and the points of 03:12 checked, and the dependency paragraph opening Section 9
         checked by two scans of Section 9: confirmed for installation. It noted that its check of 03:12 had missed
         the omission of Section 9.4, Step 3 from the list of steps used in Section 9.25, which the audit of 03:05
         found. One recommended wording point and two optional ones in this section were made.
- 2026-10-19 03:30  separate referee reading of the Newton tests with a variational tangent of the discrete exit map
         (records added to the numerical program at 02:10-03:23, not yet in this report), requested by the numerical
         researcher: the tangent approximates the derivative of the implemented map but is not its exact Jacobian, and
         its agreement with finite differences depends on the direction; the reading that the failure of the full
         Newton steps is caused by non-differentiability of the discrete map at the grid scale is not established,
         since a small derivative error amplified by the ill-conditioned solve could produce the same records; one
         transcription correction (the decreases of the two accepted Newton steps and the damping of the second). The
         sentence on these tests in Section 5.8(vii) uses the corrected reading.
- 2026-10-19 04:05  separate referee reading of the whole report in its proposed final form (status line, Sections 0
         and 0a, Section 7 with a new item 7; body as installed at 03:28 apart from the Newton sentence of 5.8(vii),
         then under check; read before installation; the proofs of Section 9 were not re-derived): five required
         corrections, one correction conditional on the verifier's check of the Newton sentence of 5.8(vii), and three
         optional ones. The required ones: the time statement should state only what the session log records; the
         artifact paragraph described an index that did not cover this version; the growth-class and angular summaries
         of Section 0a did not keep the differences between the hypotheses of the statements; the numerical summary of
         Section 0a joined the scalar crossing at p = 0.5 to the range of D, whose upper end is at p = 0.35 off a
         crossing; and Section 7, item 7 said that the growth-class hypotheses were not shown to fail for a profile,
         although some combinations are proved incompatible with a profile. The first and the last three were made,
         adapted (the session counts are taken from the session log at the final save); for the second, the artifact
         paragraph was rewritten to describe the index generated from the final version, and the reference to the
         accompanying artifacts was kept. One optional correction (the wording of Proposition 2.1(a) in Section 0a)
         was made; the other two were not needed for the text as revised.
- 2026-10-19 04:10  verifier: installation of the version saved at 03:28 confirmed (rebuild, comparison, the 03:26
         entry). The figures of the Newton sentence of Section 5.8(vii) in the corrected reading of 03:30 (the
         increase of the residual under the full correction at every tested amplitude, the 3.6-fold and 4.3-fold
         reductions under the truncated one, the stall at 29 per cent) checked against the records. With the
         verifier's own exit map, the datum zeros set to that map's strong exits, the truncated correction at 256
         angles reduced the x-odd part of the residual 2.5-fold at amplitudes 1e-5 to 1e-3 and the full one increased
         it about 4.5-fold, both reducing it by large factors on log r >= -4; the verifier's earlier interim finding
         that the truncated response is not reproduced in that map (which had used zeros that are not its exits) was
         withdrawn. Recommended: "at 256 angles" in Section 7, item 4; made, together with the verifier's sentence on
         the independent evaluation in Section 5.8(vii).
- 2026-10-19 04:13  follow-up referee reading of the revised final form (read before installation; the proofs of
         Section 9 were not re-derived): one required correction: the artifact paragraph of Section 0 described the
         index as mapping results to their supporting records, whereas it locates records, matches Section 6 entries
         by timestamps and states its coverage and gaps, and matching does not verify the content of a record; the
         sentence on executable materials opening Section 8 repeated the availability claim; both made as suggested.
         It found the time arithmetic of Section 0 correct and the revised summaries of Section 0a consistent with the
         statements cited, and asked that the session checks of the build be made as strict as the time statement
         (sessions of at most six hours, gaps of exactly 30 seconds) and be run on the session log at the final save;
         done. Both optional clarifications (the terminal status in Section 0 and the qualifications of the numerical
         summary in Section 0a) were made, the second adapted. The conditional correction of 04:05 (to remove the
         Newton sentence of 5.8(vii) unless the verifier confirmed it) lapsed, since the verifier confirmed it at
         04:10.
- 2026-10-19 04:21  verifier: advance check of the proposed final form read at 04:05: rebuilt identically; the time
         statement of Section 0 checked against the session logs of the three roles and against the task statement,
         and the restatements of Section 0a and of Section 7, item 7 against the statements they cite: correct. Two
         required corrections, both also required by the reading of 04:13: the Environment paragraph of Section 0
         referred to run labels that the report does not use, and the artifact paragraph misdescribed how the index
         matches records and what it lists as missing. Required release checks: the save time, the statement on the
         execution limit and the session counts against the final session log, and the index generated from the
         released version. Recommended: naming the lead analyst's session log, describing the reformulation of 5.8 as
         applied to x-even data rather than as restricted to x-even states, two corrections of the entry of 04:05,
         stricter session checks in the build, and Section 4.18 in the proof map of the index; all made. The four
         optional points (the status line and Section 0a, items 2, 5 and 6) were made.
- 2026-10-19 04:25  verifier: the revised Newton sentence of Section 5.8(vii) (with the independent evaluation) and
         the clause of Section 7, item 4 rebuilt identically and checked against the verifier's records; confirmed for
         installation.
- 2026-10-19 04:27  verifier: the revised final form with the corrections of 04:13 rebuilt identically; the two
         required corrections of 04:21 confirmed as made, and the terminal status, the numerical summary of
         Section 0a, the sentence opening Section 8 and the stricter session checks found correct. One further
         correction of the wording of the 04:13 entry recommended; made.
- 2026-10-19 04:30  verifier: its independent exit map of 04:10 run at 512 angles: the reductions on log r >= -4 and
         the location of the differences at log r < -4 confirmed, but the reduction of the whole x-odd residual by the
         truncated correction is a 256-angle result (at 512 angles 1.1-fold at amplitudes 1e-5 and 1e-4, and an
         increase at 1e-3). Recommended: the 512-angle figures in the sentence of Section 5.8(vii); made in the
         verifier's wording.
- 2026-10-19 04:35  verifier: installation of the version saved at 04:32 confirmed (rebuild, comparison with the text
         confirmed at 04:25, the entries 03:30, 04:10 and 04:25). One optional precision of the 03:30 entry (the
         transcription correction also changed the first accepted decrease); made.
- 2026-10-19 04:44  verifier: the proposed final form with the corrections of 04:21 to 04:35 rebuilt identically; the
         time statement of Section 0 checked against the session logs of the three roles, the revised status line and
         summaries of Section 0a against the statements they cite, the new sentence of Section 5.8(vii) against the
         verifier's records, and the entries of this section from 04:05 to 04:35 against the checks they describe:
         confirmed as the terminal text. Recommended: that the index of the accompanying artifacts also search the
         records of the readings requested by the numerical researcher, so that the entry of 03:30 is matched; made.
         The optional points (in Section 0a, item 5, "parameter conditions" and the hypothesis rho >= 0 for gamma = 1;
         "28-fold" in Section 5.8(vii); the follow-up referee reading classed as an audit in the index; the final save
         to check its output before it replaces the report) were made.
- 2026-10-19 04:48  verifier: advance reading of the analysis on which Proposition 2.7 is based (the twice-subtracted
         field on locally Lipschitz densities with the growth bounds, the compactness of the rescaled densities and
         the stationary equation of their limits, the criterion for limits that are functions of y alone, the explicit
         stationary solutions, also checked symbolically, and the density with W_2 = o(r^gamma) but not o(r)), every
         step re-derived: correct; two wording points, that no limit is claimed nonzero and that the examples are
         densities, not profiles, both met in the text.
- 2026-10-19 05:04  verifier: Proposition 2.7, its proof in Section 9.27 and the changed sentences of Sections 0, 2, 7
         and 9, in the version of 04:57, rebuilt identically from its sources and checked step by step against
         Sections 9.0 and 9.14 (the stream function of the example of 2.7(e) also symbolically): confirmed for
         installation; two optional precisions in Section 9.27 (in Step 5 the class with exponent gamma is reached by
         Step 2 with that exponent; in Step 1 the Laplacian identities of Section 9.14, Step 5 are used in
         distributions for a continuous field), both made.
- 2026-10-19 05:07  separate audit of Proposition 2.7, Section 9.27, the changed sentences and the dependency
         paragraph opening Section 9, every step re-derived: correct with two repairs, both made. In Step 1 the
         translated kernel term is not absolutely integrable near Y = X (only the two subtraction terms are; the
         translated term is taken as a circular principal value, as the proof then does). The closing sentence of
         Step 5 included the case of a nonzero layered limit together with the Hessian bound, which cannot occur,
         since under the Hessian bound every layered limit is 0; it now states the two examples separately, as
         Proposition 2.7(e) does.
- 2026-10-19 05:22  verifier: the revised Proposition 2.7 and Section 9.27, with the two repairs of the separate audit
         and the two optional precisions, rebuilt identically from its sources and checked against the previous
         version: both repairs correct (the 05:04 check had not caught either point); the closed forms of the
         twice-subtracted field for the explicit densities of 2.7(d) and of Step 5 of Section 9.27 also compared with
         an independent direct quadrature (largest error 8.0e-6 over 37 evaluations, decreasing as the grid is
         refined), as a check of the formulas, not as part of a proof: confirmed for installation.
- 2026-10-19 05:25  verifier: the proposed final form with the points of 04:44 rebuilt identically by an independent
         replay of the build; the changed wording of Section 0a, item 5 and of Section 5.8(vii), the output check of
         the build and the revised index generator confirmed. Recommended: that the final save not be blocked, and the
         session sentence of Section 0 stay true, if a session log records a session slightly longer than six hours or
         a restart gap other than 30 seconds before T_end; the build now states the actual values in that case and is
         otherwise unchanged.
- 2026-10-19 05:28  verifier: installation of the version saved at 05:23 confirmed (rebuild, comparison with the text
         confirmed at 05:22, the entries 04:48, 05:04, 05:07 and 05:22).
- 2026-10-19 05:34  verifier: the proposed final form with Proposition 2.7 as installed at 05:23 rebuilt identically,
         with the build before and after the change recommended at 05:25; the new clause of Section 0a, item 5, the
         new sentence of Section 7, item 7 (ii) and the entry of 04:44 checked against the statements and the check
         they cite: confirmed as the terminal text. The revised build tested on synthetic session logs (a session
         longer than six hours, other restart gaps, a gap beyond the hard limit, which stops the save before anything
         is written): correct. The index generator confirmed in its counts and matches. Recommended: that the full
         texts of two audit answers recovered from their run logs not begin with a stray diff header line, and that
         the index name the generator that produced it in its reproduction command; both made. Optional: "a similar
         pattern" instead of "the same pattern" when the figures for the other two roles differ from the lead
         analyst's; made.
- 2026-10-19 05:47  verifier: the proposed final form as saved at 05:36 rebuilt identically; its only changes since
         the version confirmed at 05:34 are the save time and three entries of this section, all accurate: confirmed
         as the terminal text. The revised build (tested again on synthetic session logs), the index generator and the
         two repaired audit texts confirmed. Open: the release checks at the final save.
- 2026-10-19 06:08  verifier: advance reading of the analysis on which Proposition 2.8 is based (the set of limits at
         infinity, the angular equations of homogeneous stationary functions and their classification, the x-even
         case, the consequences for profiles including the Hessian bound, the first order under a density rate, the
         strain example and the two symmetries), every step re-derived, the angular identities also symbolically and
         the strain example also numerically: correct; recommended: the report's notation for the strain matrix, the
         first-order consequence for every function with a single zero direction, and a statement that the class
         bounds are not shown to give W_2 = o(r^gamma); all met in the text.
- 2026-10-19 06:21  verifier: advance reading of the analysis of the stationary functions with a single zero direction
         (the disk of data, existence and exhaustion, the construction of the stream function from the data, the
         reflection, evenness in y and the first-order consequence S = I/gamma), every step re-derived, the identities
         also symbolically and the stream functions and fields of several members also numerically, as a check of the
         formulas, not as part of a proof: correct; required: that the text not suggest that the solutions
         a(r + sigma x)^gamma exhaust this class, and that the complete text of that analysis, which its run log
         holds, be the one cited; both met.
- 2026-10-19 06:24  verifier: correction of its reading of 06:21: whether the members other than a(r + sigma x)^gamma
         have a locally Lipschitz gradient near their zero direction was decided neither by that analysis nor by the
         numerics, and the report was not to use either answer; it was then listed as not decided in Proposition 2.8
         (it is decided in part (c) by the later analysis checked at 07:05, 07:18 and 07:24).
- 2026-10-19 06:34  verifier: Proposition 2.8, its proof in Section 9.28 and the changed sentences of Sections 0, 2, 7
         and 9, in the version of 06:26, rebuilt identically from its sources and checked step by step against the two
         analyses above and Sections 9.14 and 9.27 (the integrated angular identity and the equation for G also
         numerically for four members with a single zero direction, as a check of the formulas, not as part of a
         proof): confirmed for installation, no change requested.
- 2026-10-19 06:37  separate audit of the same version of Proposition 2.8, Section 9.28, the changed sentences and the
         dependency paragraph opening Section 9, every step re-derived, including the open disk of data for the
         functions with a single zero direction: correct with three repairs, all made. In Section 9.28, Step 10, the
         translated kernel term is not absolutely integrable near Y = X where the bump is nonzero (only the two
         subtraction terms are; the translated term is taken as a circular principal value). In the summaries of
         Sections 2 and 7 the first-order condition was stated without the hypothesis, present in Proposition 2.8(d),
         that the density is a profile; both now state it.
- 2026-10-19 06:53  verifier: the three repairs of 06:37, as the only changes from the version of 06:26 (rebuilt
         identically from its sources and compared word by word), each checked against Proposition 2.8(d) and
         Section 9.14, Step 3: confirmed for installation, no change requested.
- 2026-10-19 07:05  verifier: the analysis showing that, among the stationary functions with a single zero direction,
         every member other than the a(r + sigma x)^gamma has an unbounded second angular derivative of v^gamma near
         its zero direction (an energy that tends to infinity faster than the logarithmic angle, downward crossings of
         a fixed value of the slope ratio v'/sin(th) with unbounded curvature, and a lower bound for the second
         derivative at these crossings), and the shorter argument for the crossings used in the report, every step
         re-derived, the identities also symbolically and the second derivative at the first crossings also
         numerically for three members, as a check of the formulas, not as part of a proof: correct; required for the
         report: both ends of the arc, both zero directions, and the bounds and equations of the analysis on which the
         argument rests, which the draft did not yet print.
- 2026-10-19 07:18  separate audit of the version of 07:10 of Proposition 2.8(c), the "Not decided" paragraph after
         it, Section 9.28, Step 8 and the two changed summary sentences of Sections 2 and 7, every step re-derived
         (the energy identity, the limiting equilibrium and its linearization, the Lyapunov matrix, the parabolic
         solution and the constants at the crossings also symbolically): correct with one repair, made: the summaries
         of Sections 2 and 7 now say that the members of the family with a locally Lipschitz gradient have it on the
         punctured plane, since no nonzero homogeneous function of degree gamma, 1 < gamma < 2, has a Lipschitz
         gradient near the origin.
- 2026-10-19 07:24  verifier: the version of 07:10 and its revision of 07:19 (after the audit of 07:18), each rebuilt
         independently from the same inputs and found identical; every step of Section 9.28, Step 8 re-derived by hand
         and the identities also with its own symbolic script; Proposition 2.8(c), the "Not decided" paragraph after
         it and the summaries of Sections 2 and 7 checked against the proof: correct; it found independently the one
         repair of the audit of 07:18 (the punctured plane in the two summaries), which the revision contains, and
         confirmed the revision for installation.
- 2026-10-19 07:36  separate referee reading of a preview of the terminal version (built at 07:13 on the version of
         07:10 of Proposition 2.8): the coverage statements, the restatements of Propositions 2.7 and 2.8 against
         their statements, overclaims, numbers quoted in several places, the session arithmetic of Section 0 and the
         format: one required correction, the punctured plane in the summaries of Sections 2 and 7, already made in
         the version of 07:19; no wrong proof pointer, no other mismatch between a summary and its statement, no
         unexplained disagreement between numbers quoted in several places and no claim of either endpoint found (the
         proofs of Section 9 were not re-derived in this reading); five optional corrections, all made: the matrix A
         of the velocity law defined in Section 2, where it is first used; in Section 0a the additional hypotheses
         attributed to the exclusions of Propositions 2.3-2.6; a disjunction in Proposition 2.8(c) made unambiguous;
         the entry of 06:24 put in the past tense with a pointer to the later decision; two broken lines of Section 8
         rejoined.
- 2026-10-19 08:05  separate audit of the version of 08:01 of Proposition 2.8(c), (g) and (h), the "Not decided"
         paragraph after them, Section 9.28, Steps 8, 12 and 13, and the changed summary sentences of Sections 2 and
         7, every step re-derived (the backward flow near 0 and the convergence of the linearizing coordinate for
         every beta > 1/2, the Jordan curve and the area argument, the bound for the velocity of the limit, the
         completeness of the flow, the growth comparison for every q < 1 and every gamma in (1, 2), both signs of the
         amplitude and the connectedness of the large positive set): correct; one presentation error, made: the
         opening paragraph of Proposition 2.8 said that no condition on l is assumed, while (g) assumes l > 1/2; four
         small points, made: "further bound on W_2" in (g), the word union in place of a letter already used for a
         remainder velocity, "without the Hessian bound" in the last sentence of the "Not decided" paragraph, and the
         convolution integral named in Step 12.
- 2026-10-19 08:08  verifier: the version with the five optional corrections of the referee reading of 07:36, rebuilt
         independently from the same inputs and found identical; each correction checked against the text it replaces
         and against the statements and proofs it refers to: faithful, with no change to any statement or proof;
         confirmed for installation.
- 2026-10-19 08:15  verifier: the revision of 08:07 of the version of 08:01 (after the audit of 08:05), rebuilt
         independently from the same inputs and found identical, its difference from the version of 08:01 consisting
         exactly of the repairs of the audit; every step of Section 9.28, Steps 8, 12 and 13 re-derived (the backward
         flow near 0 and the linearizing coordinate, the Jordan curve and the area argument, the bound for the
         velocity of the limit, the completeness of the flow, the growth comparison, both signs of the amplitude and
         the connectedness of the large positive set); Proposition 2.8(c), (g) and (h), the "Not decided" paragraph
         and the summaries of Sections 2 and 7 checked against the proofs: correct; confirmed for installation.
- 2026-10-19 08:19  separate audit of the version of 08:15 of Proposition 2.8(h) for limits F(e.X), Section 9.28,
         Step 14, and the changed summary sentences of Sections 2 and 7, every step re-derived (the eigenvalues of the
         strain matrix S = A + M, the bound for the velocity of the limit, the transfer of the completeness and growth
         arguments of Step 13, the case f <= 0, the connectedness of the large positive set when exactly one amplitude
         is positive, and the consequence for a|x|^gamma): correct; one required repair, made in the revision of
         08:32: the summaries of Sections 2 and 7 did not say f != 0, and for f = 0 the argument gives no eigenvalue
         of S and proves nothing; small points, made: the range 0 <= q < 1 written out, the profile hypothesis
         repeated at the start of Step 14, and two wordings.
- 2026-10-19 08:27  verifier: the version of 08:15, rebuilt independently from the same inputs and found identical;
         every step of Section 9.28, Step 14 re-derived: correct, and Proposition 2.8(h) states exactly what it
         proves; the summaries of Sections 2 and 7 refuted as worded, since they omit f != 0 (found independently of
         the audit of 08:19); not confirmed for installation until repaired.
- 2026-10-19 08:34  separate audit of the version of 08:27 of Proposition 2.8(h) for limits F(e.X) != 0 with both
         amplitudes nonzero, Section 9.28, Step 15, and the changed summary sentences of Sections 2 and 7, every step
         re-derived (the bound for |e.X| on the set where the density is small, the choice of the growth rate and of
         the exponent gap, the linearizing coordinate near 0 for l > 5/12 and the vanishing on the y-axis for profiles
         even in x, the thin sets at 0, the comparison of the area of their images under the flow with the area of a
         rectangle, and the consequences in (h)), also tested against the density of (e), which does not solve the
         profile equation, and against f = 0: correct; one required repair, made in the revision of 08:36: the summary
         of Section 7 could be read as including f = 0; small points, made: the cases left open stated with their
         scope in the "Not decided" paragraph, and three letters already used earlier in Section 9.28 replaced.
- 2026-10-19 08:35  verifier: the version of 08:27 audited at 08:34, rebuilt independently from the same inputs and
         found identical; every step of Section 9.28, Step 15 re-derived: correct, and Proposition 2.8(h) and the "Not
         decided" paragraph state exactly what it proves; the summary of Section 7 could be read as including f = 0
         (found independently of the audit of 08:34); not confirmed for installation until repaired.
- 2026-10-19 08:39  verifier: the revision of 08:32, rebuilt independently from the same inputs and found identical;
         its difference from the version of 08:15 is exactly the repair and the small points of 08:19 and 08:27; both
         summaries now state f != 0 and claim no more than Step 14 proves; confirmed for installation.
- 2026-10-19 08:42  verifier: the revision of 08:36 of the version audited at 08:34, rebuilt independently from the
         same inputs and found identical; its difference from the version of 08:27 checked in full: the repair of
         08:34 and 08:35 made, so that no part of the summary of Section 7 includes f = 0; the list of open cases in
         the "Not decided" paragraph checked against Steps 14 and 15 and found exact; the renamed letters changed
         everywhere in Step 15 and nowhere else; confirmed for installation.
- 2026-10-19 08:59  verifier: the installed report of 08:52 checked against the expected text, including its timeline
         entries of 08:34, 08:35 and 08:42: confirmed.
- 2026-10-19 09:09  verifier: a version of 09:01 of Proposition 2.8(h) for one-sided limits a(e.X)_+^gamma, a > 0,
         with 1/4 < l <= 1/2 under an extra condition on q, gamma and l, with Section 9.28, Step 16, rebuilt
         independently from the same inputs and found identical; every step re-derived: correct; withdrawn before
         installation in favour of the version of 09:12, which needs no extra condition. The lower cut on the density
         in Step 16(vii), which sends every orbit of the thin set to the side e.X > 0 of the line at the final time,
         follows an independent argument of the verifier for 5/12 < l <= 1/2, which was audited separately before
         09:09 and found correct; that argument is not reproduced in this report.
- 2026-10-19 09:13  verifier: the version of 09:12, rebuilt independently from the same inputs and found identical;
         every step of Section 9.28, Step 16 re-derived (the exponents, the sign of the density, the invariant region
         on which it vanishes, the thin sets, the orbit bounds, the choice of levels by summation and the area
         comparison); Proposition 2.8(h), the "Not decided" paragraph and the summaries of Sections 2 and 7 checked
         against Steps 14, 15 and 16: correct, and the list of open cases exact; confirmed for installation.
- 2026-10-19 09:18  separate audit of the version of 09:12 of Proposition 2.8(h) for limits a(e.X)_+^gamma, a > 0,
         with 1/4 < l <= 1/2, Section 9.28, Step 16, and the changed summary sentences of Sections 2 and 7, every step
         re-derived (the choice of exponents, the sign of the density, the invariant region where it vanishes and the
         first exit argument, the thin sets at zeros where the gradient vanishes and their measurability, the orbit
         bounds, the summation argument for the levels, the flow Jacobian and the exponent identity, the consequences
         in (h) and the list of open cases): correct; small points: the words "double zeros" in the summary of
         Section 2 mean zeros of the density at which its gradient vanishes, not necessarily of exact multiplicity
         two, and the scope of one clause in the list of open cases could be made plainer.
- 2026-10-19 09:19  verifier: two arguments proposed for Proposition 2.8(h), checked before any report text existed:
         that two positive amplitudes are impossible for 1/4 < l <= 1/2 (flow boxes at zeros of the density at which
         its gradient vanishes, the basin of 0 of the backward flow and a growth bound), and a cube-root lower bound
         for the thin sets of a nonnegative C^3 density next to a region where it vanishes, with which a one-sided
         limit a(e.X)_+^gamma, a > 0, is impossible for 1/6 <= l <= 1/4; both re-derived: correct.
- 2026-10-19 09:26  verifier: the installed report of 09:22 checked against the expected text, including its timeline
         entries of 08:59, 09:09, 09:13 and 09:18: confirmed.
- 2026-10-19 09:33  verifier: a working version of 09:30 of Section 9.28, Steps 17 and 18, and of the changed parts of
         Proposition 2.8(h), the "Not decided" paragraph and the summaries of Sections 2 and 7, rebuilt independently
         from the same inputs and checked against the arguments of 09:19: no error found; one optional point (cite the
         regularity of the twice-subtracted field at 0 next to the expansion of V in Step 17(ii)).
- 2026-10-19 09:39  separate audit of the version of 09:32 of Proposition 2.8(h) for limits F(e.X) with two positive
         amplitudes and with one positive amplitude, Section 9.28, Steps 17 and 18, and the changed summary sentences
         of Sections 2 and 7, every step re-derived (the flow boxes at zeros where the gradient vanishes and the reuse
         of the area comparison of Step 15, the sign of the density, the basin of 0 and its openness and closedness,
         the growth bound and the contradiction on the line e.X = 0, the region where the density vanishes, the
         cube-root bound for the thin sets, the monotonicity and compactness argument for the third derivative,
         measurability, the bounded orbits and the area comparison, also at l = 1/6, the consequences in (h) and the
         list of open cases): correct; two small points, made in the revision of 09:41: the regularity of the
         twice-subtracted field at 0 (Section 9.14, Step 3) cited for the expansion of V in Step 17(ii), as also
         suggested by the verifier at 09:33, and the index of an integration identity in Step 18(ii) renamed, since k
         is already used.
- 2026-10-19 09:51  verifier: the revision of 09:41 rebuilt independently from the same inputs and compared with the
         version of 09:30 checked at 09:33: the only changes are the two points of the audit of 09:39, both correct
         (the regularity of the twice-subtracted field at 0 holds under the hypotheses of the profile and gives the
         quadratic bound on the nonlinear part of V for every l; the integration identity holds for every index); the
         installation procedure replayed independently with the same result: confirmed for installation.
- 2026-10-19 10:00  verifier: the installed report of 09:54 checked against the expected text, including its timeline
         entries of 09:19, 09:26, 09:33, 09:39 and 09:51: confirmed. The sentences of Section 0a, item 5 and of
         Section 7, item 7 (ii) of the proposed final form, revised since 05:47 to restate Proposition 2.8 as
         extended, read at 09:51 in their present wording against Proposition 2.8(h) of the version of 09:41: correct;
         the proposed final form built on the report of 09:54 rebuilt identically.
- 2026-10-19 10:23  verifier: the proposed final form built at 10:08 on the report of 09:54 rebuilt identically, its
         only changes being the save time and the entry of 10:00. Section 0a and Section 7, item 7 of it read in full
         against the report of 09:54, every restated result against its statement, every pointer and every list of
         undecided cases: correct. Optional: "0 <= q < 1" for "q < 1" in the remainder hypothesis of Section 0a,
         item 5; made.
- 2026-10-19 10:28  verifier: three arguments proposed for Proposition 2.8(h), checked before any version of the
         report contained them: a lower bound of order xi^(1/m) for the thin sets of a nonnegative C^m density next to
         a region where it vanishes, with which a one-sided limit a(e.X)_+^gamma, a > 0, is impossible for
         1/(2m) <= l <= 1/4; at l = 1/4, that zeros of the density at which its gradient vanishes are stationary and
         that two positive amplitudes are impossible; and, for a C^m density with 1/4 < l <= 5/12, from the minimum of
         the density across the x-direction near 0, that 1/beta > m or 1/beta is an odd integer; all re-derived:
         correct.
- 2026-10-19 10:34  verifier: a working draft of Section 9.28, Step 19 (the C^m form of Step 18) checked against Steps
         14, 16 and 18: correct. Optional: a letter other than k for the order of differentiability, since
         k = gamma + 1 in Proposition 2.8; made.
- 2026-10-19 10:46  verifier: the version of 10:38 of Section 9.28, Steps 19, 20 and 21, and of the changed parts of
         Proposition 2.8(h), the "Not decided" paragraph and the summaries of Sections 2 and 7, rebuilt independently
         from the same inputs and checked against Steps 12 to 18 and the arguments of 10:28 and 10:34: correct,
         confirmed for installation; optional points, made in the revision of 10:54: other letters for the error term
         in Step 21(ii) and the coefficient in Step 21(i), next to the unit vector e and the amplitudes, and for the
         orbit constant in Step 20(iii), and the hypotheses besides which Step 19 uses only the stated facts.
- 2026-10-19 10:46  separate audit of the version of 10:38 of Proposition 2.8(h), Section 9.28, Steps 19, 20 and 21,
         and the changed summary sentences of Sections 2 and 7, every step re-derived (the parts of Step 18 reused for
         l < 1/6, the vanishing of the derivatives up to order m at non-isolated zeros, the bound of order xi^(1/m)
         for the thin sets, the compactness argument for the m-th derivative and the area comparison, also at
         2l = 1/m; at l = 1/4 the absorbing disk, the absence of periodic orbits, the long flow tubes, the sign of the
         density, the bounded set of zeros, the closed level curves and the half-plane argument; for 1/4 < l <= 5/12
         the curve of minima across the x-direction and its equation, the signs of its two coefficients, the
         connectedness of the set where the density is positive, the Jordan curve and half-disk argument and the
         Taylor parity argument; the consequences in (h) and the list of open cases): no error; three points of
         presentation, made in the revision of 10:54: the header of Step 19 now states that Step 18(v) is reused only
         up to the disk containment, since the clause introducing its last display uses l >= 1/6; a letter other than
         k for the order of differentiability; a letter other than e for the error term in Step 21(ii).
- 2026-10-19 10:49  verifier: the audit of 10:46 read as a claim against the check of 10:46: in agreement; its point
         on the header of Step 19 correct, a matter of wording only; the proposed sentences of Section 0a, item 5 and
         of Section 7, item 7 (ii) of the proposed final form, restating Proposition 2.8(h) as extended in the version
         of 10:38: correct.
- 2026-10-19 10:58  verifier: the revision of 10:54 rebuilt independently from the same inputs and compared word by
         word with the version of 10:38 checked at 10:46: the only changes are the points of the audit of 10:46 and
         the optional points of 10:46 and 10:49 (renamed letters, the header of Step 19 stating that Step 18(v) is
         reused only up to the disk containment, and one sentence of Section 2 stating m >= 3): correct; confirmed for
         installation.
- 2026-10-19 11:07  verifier: the installed report of 11:04 checked against the expected text, including its timeline
         entries of 10:00 to 10:58: confirmed; the proposed final form built on it rebuilt identically.
- 2026-10-19 11:13  verifier: an argument proposed for Proposition 2.8(h), checked before any version of the report
         contained it: for a C^3 density at l = 1/4, an identity special to div V = 1/2 by which, near a zero of V at
         which the density and its gradient vanish and its Hessian has a positive direction, the zeros of the density
         form a curve of zeros of V; and with it, that amplitudes of opposite signs are impossible at l = 1/4 (a
         region bounded by an arc where the density is positive and a segment through 0, the component through 0 of
         the zeros with nonzero Hessian in it, and the strong unstable manifold at a zero with vanishing Hessian);
         re-derived, the identity also symbolically: correct.
- 2026-10-19 11:23  verifier: the identity of 11:13 for a general divergence, where it has an additional term
         vanishing only for div V = 1/2; a sector argument in the eigen-coordinates of DV at a zero with vanishing
         Hessian, replacing the strong unstable manifold; that the proof in Step 21(v) that the set where the density
         is positive is connected applies at l = 1/4; and a working draft of Section 9.28, Step 22 checked against
         Steps 12 to 21: correct. Optional: a letter other than C_0 for the component of the zeros, since C_0 is a
         class constant in Proposition 2.7(b); made.
- 2026-10-19 11:29  separate audit of the version of 11:23 of Proposition 2.8(h), the "Not decided" paragraph,
         Section 9.28, Step 22 and the changed summary sentences of Sections 2 and 7, every step re-derived (the
         hypotheses at l = 1/4 and where they are proved, the three differentiated equations and the identity with its
         sign and denominator, the vanishing of the density along the curve of minima, the connectedness of the set
         where the density is positive and the half-disk argument, the zeros with nonzero Hessian as a manifold with 0
         as its only boundary point, the sector argument with its exit sets and the decay of the density, the
         classification of compact one-dimensional manifolds, and the consequences in (h)): no error; three points of
         presentation, two of them made in the revision of 11:32: that the eigenvectors in Step 22(iv) need not be
         orthogonal and the components of V there are coefficients in their basis, and a clearer grouping of the open
         cases in the "Not decided" paragraph; the third, a restatement at the start of Step 22 of where its
         hypotheses are proved, was not needed.
- 2026-10-19 11:38  verifier: the version of 11:23 and its revision of 11:32 (after the audit of 11:29), each rebuilt
         independently from the same inputs and found identical; Section 9.28, Step 22 compared word by word with the
         working draft checked at 11:23, the revision changing only the points of 11:23 and 11:29; Proposition 2.8(h),
         the "Not decided" paragraph and the summaries of Sections 2 and 7: correct; the audit of 11:29 read as a
         claim: in agreement; the proposed sentences of Section 0a, item 5 and of Section 7, item 7 (ii) of the
         proposed final form, restating Proposition 2.8(h) as extended: correct; confirmed for installation, with one
         repair of wording in the entry of 11:13 of this section, made: it now states that the zero of the density is
         a zero of V.
- 2026-10-19 11:47  verifier: the installed report of 11:45 checked against the expected text, including its timeline
         entries of 11:07 to 11:38: confirmed; the proposed final form built on it rebuilt identically. Optional: the
         entry of 11:29 should state that the audit named three points of presentation, two of which were made; made.
- 2026-10-19 12:00  separate check of an argument proposed for Proposition 2.8(h), before any version of the report
         contained it: for a C^infinity density and 0 < l < 1/4, that amplitudes of opposite signs force 1/(2l) to be
         an even integer; every step re-derived: correct, with a direct proof of the smooth conjugacy to the normal
         form at a zero of V with two positive eigenvalues, which the argument cites.
- 2026-10-19 12:03  verifier: the argument of 12:00, checked before any version of the report contained it (an area
         comparison along long flow tubes by which every zero of the density at which V does not vanish has finite
         even order, a transport identity for the leading coefficient along an orbit of such zeros, the strong
         unstable manifold at a zero of V with singular derivative, smooth normal forms at saddles and at zeros of V
         with two positive eigenvalues, and a count of the ends of the orbits of zeros in a region bounded by an arc
         where the density is positive and a segment through 0); re-derived: correct.
- 2026-10-19 12:05  verifier: a simplified form of the area comparison of 12:03 and a count of orbit ends replacing a
         graph construction: correct; the check of 12:00 read as a claim: in agreement.
- 2026-10-19 12:33  verifier: a working version of Section 9.28, Step 23, of Proposition 2.8(h), of the "Not decided"
         paragraph and of the changed summary sentences of Sections 2 and 7, rebuilt independently and checked step by
         step against Steps 14 to 22 and the arguments of 12:00 to 12:05: correct. Optional: a more exact wording in
         Section 2 (the zeros of the density at which V does not vanish form the orbits that are counted); made.
- 2026-10-19 12:42  verifier: the version frozen at 12:33, rebuilt independently from the same inputs and found
         identical; it differs from the working version checked at 12:33 only by two points of wording in
         Section 9.28, Step 23(vi) and (ix), both correct.
- 2026-10-19 12:47  separate audit of the version frozen at 12:33 of Proposition 2.8(h), the "Not decided" paragraph,
         Section 9.28, Step 23 and the changed summary sentences of Sections 2 and 7, every step re-derived (the
         hypotheses at 0 < l < 1/4 and where they are proved, the two lemmas on functions of one variable, the
         absorbing disk, the area comparison along long flow tubes, also at 2lm = 1, the even order of the zeros at
         which V does not vanish and the transport identity for their leading coefficient, the strong unstable
         manifold at a zero of V with singular derivative, the normal forms at saddles and at zeros of V with two
         positive eigenvalues and the parity of the number of half-arcs, the origin and the Jordan region, the limit
         sets of the orbits of zeros and the count of their ends, and the consequences in (h)): Step 23 correct; one
         error of scope: the "Not decided" paragraph stated the positivity of both amplitudes for C^infinity densities
         with l < 1/4 instead of 0 < l < 1/4; points of presentation: a corner of the square in Step 23(v), the
         integer of the resonant term in Step 23(vi) when there is no resonance, the smoothness of the strong unstable
         curve on a fixed neighborhood, the shrinking of a flow box, and letters used with two meanings; all made in
         the revision of 12:58.
- 2026-10-19 12:52  verifier: the audit of 12:47 read as a claim against the checks of 12:33 and 12:42: in agreement;
         the error of scope in the "Not decided" paragraph confirmed, which those checks had missed, so that the
         version frozen at 12:33 was not to be installed without its repair; the other points correct, none affecting
         a proof.
- 2026-10-19 13:06  verifier: the revision of 12:58 rebuilt independently from the same inputs and compared word by
         word with the version frozen at 12:33: its only changes are the repair of scope and the points of
         presentation of 12:47 and the optional point of 12:33, each checked, including the new argument for the
         smoothness of the strong unstable curve and the choice of the integer of the resonant term: correct;
         confirmed for installation.
- 2026-10-19 13:17  verifier: installation of the version saved at 13:10 confirmed (an independent replay of the
         build, byte-identical with the saved version; the entries 11:47 to 13:06 checked against the checks they
         describe). In the proposed final form built on it, the new clause of Section 7, item 7 (ii) stated the range
         l < 1/4 where 0 < l < 1/4 is meant, the error of scope recorded at 12:47 and 12:52; corrected.
- 2026-10-19 13:27  verifier: the proposed final form built on the version saved at 13:10, with the correction of
         13:17, rebuilt identically by an independent replay of the build; its one new entry, that of 13:17, accurate:
         confirmed as the terminal text.
- 2026-10-19 13:46  separate audit of the version frozen at 13:39 of Proposition 2.8(h), the "Not decided" paragraph,
         Section 9.28, Step 24 and the changed summary sentences of Sections 2 and 7, every step re-derived (the
         arithmetic of the ranges of l and m, the smoothness of the field and of its flow and the two lemmas in finite
         smoothness, the zeros at which V does not vanish, the eigenvalues at a zero of V at which the second
         derivative of the density does not vanish, the exclusion of an eigenvalue above 1/4 where it vanishes, the
         saddles, the linearization at the zeros of V with two positive eigenvalues and the polynomial form of the
         density there, also in the case of equality, the reuse of the parity argument and of the count of orbit ends,
         and the consequences in (h)): Step 24 correct; points of presentation, four of them made in the revision
         of 13:47 (the range of the Holder exponent, the rate of convergence that defines the strong unstable curve,
         the indices in the higher variational equations, and which hypothesis the linearization and the polynomial
         form each use).
- 2026-10-19 13:55  verifier: the version frozen at 13:39 and its revision of 13:47 rebuilt independently from the
         same inputs and found identical, every step of Section 9.28, Step 24 re-derived (the arithmetic also in exact
         rational arithmetic on a grid of values of l), the four changes of 13:47 checked, and the audit of 13:46 read
         as a claim: in agreement; the revision of 13:47 confirmed for installation. In the proposed final form built
         on it, eleven entries of this section, those of 04:05 to 05:47, were missing; restored.
- 2026-10-19 14:10  verifier: installation of the version saved at 14:03 confirmed (replay of the installation,
         comparison with the revision of 13:47 confirmed at 13:55, the save time and the entries 13:17, 13:27, 13:46
         and 13:55); the proposed final form built on it, with the eleven entries of 04:05 to 05:47 restored, rebuilt
         identically: confirmed as the terminal text. Required: that the written procedure for the final save state
         that these eleven entries are kept; made.
- 2026-10-19 14:13  verifier: two counts in the check of 14:10 corrected (the number of lines of the report, and the
         numbers of entries, now with the entries for a time range), its verdicts unchanged; the corrected procedure
         for the final save and a new check that the final form keeps every entry of this section confirmed; a dry run
         of the release checks on the proposed final form: in agreement.
- 2026-10-19 14:41  separate audit of the version frozen at 14:32 of Proposition 2.8(h), the "Not decided" paragraph,
         Section 9.28, Step 25 and the changed summary sentences of Sections 2 and 7, every step re-derived (the
         transfer of Step 23 before its part (viii) to l = 1/(4n), the rescaled and periodized field, the persistence
         of the invariant circle, its rates and the bunching condition of the cited theorem on the smoothness of the
         fibration, the equivariance of the projection, the position and tangent of the circle at the zero, the
         area-preserving coordinates and their smoothness, the first nonzero Taylor coefficient of the density across
         the curve, the vanishing of the first component of the field and the arc of zeros, the area contradiction,
         the parity count also at resonant sources, and the consequences in (h)): Step 25 correct; points of
         presentation (the definition of the cut-off remainder away from the zero, five letters with two meanings
         each, the place where the symmetry of DV at a zero of V is shown, and the wording of the summary in
         Section 2).
- 2026-10-19 14:42  verifier: the version frozen at 14:32 rebuilt independently from the same inputs and found
         identical, its changes against the version saved at 14:03 exactly the five listed regions, every step of
         Section 9.28, Step 25 re-derived and the cited theorems checked against their hypotheses: confirmed for
         installation; the entries 14:10 and 14:13 accurate. In the proposed final form, Section 0a and item 7 of
         Section 7 still stated the exception l = 1/(4n), n >= 2, that Step 25 removes; removed.
- 2026-10-19 14:50  verifier: installation of the version saved at 14:44 confirmed (replay of the installation,
         identical; its changes against the version frozen at 14:32 only the save time and the entries 14:10, 14:13,
         14:41 and 14:42, each accurate); the proposed final form built on it rebuilt identically, every entry of the
         previous final form kept: confirmed as the terminal text. The two points of presentation of the audit of
         14:41 on the citation of the symmetry of DV at a zero of V and on the letters with two meanings checked; they
         were not noted in the check of 14:42, whose verdict stands.
- 2026-10-19 15:02  verifier: the polished version frozen at 14:53 rebuilt independently from the same inputs and
         found identical; its changes against the version saved at 14:44 only of presentation (the remainder in
         Step 25 defined on the whole plane, letters renamed so that each has one meaning in Step 25, the citation of
         the first two sentences of Step 23(iv) in Step 25(iv), the separation of the local and the global step in the
         summary of Section 2, and the wording of the entry 14:41), no change of argument; the renaming complete; the
         entry 14:50 accurate; confirmed for installation.
- 2026-10-19 15:07  verifier: installation of the version saved at 15:03 confirmed (replay of the installation,
         identical; its changes against the version frozen at 14:53 only the save time and the entries 14:50 and
         15:02, each accurate); the proposed final form built on it rebuilt identically, every entry of the previous
         final form kept: confirmed as the terminal text.
- 2026-10-19 15:09  verifier: the numerical report and the numerical part of the accompanying artifacts, as frozen at
         12:29, checked: unchanged, every file checksum recorded at the freeze correct and every copy of a script or
         record equal to its original; the closing time line of the numerical report still to be checked.
- 2026-10-19 15:11  verifier: the entry 15:07 accurate; the proposed final form with it rebuilt identically, every
         entry of the previous final form kept: confirmed as the terminal text.
- 2026-10-19 15:20  verifier: the entries 15:09 and 15:11 accurate; the proposed final form with them rebuilt
         identically, every entry of the previous final form kept: confirmed as the terminal text; the restatements of
         the results on limits at infinity in Sections 0a, 2 and 7 checked against their statement: consistent.
- 2026-10-19 15:22  verifier: the entry 15:20 accurate; the changed wording of the session sentence as stated and the
         sentence true; the proposed final form with them rebuilt identically, every entry of the previous final form
         kept: confirmed as the terminal text.
- 2026-10-19 16:19  verifier: two claims of an audit answer, that a zero of the density at which neither the velocity
         nor the gradient vanishes has a bounded forward orbit if l < 1/2, and that for l = 1/4 + 1/(2n), n odd, a
         limit F(e.X) with amplitudes of opposite signs needs gamma <= 1/(2l), re-derived against Section 9.28, Steps
         14, 15 and 17(i), and the class bounds: correct; the argument of the second needs only 1/4 < l <= 5/12.
- 2026-10-19 16:39  verifier: the version proposed for installation at the final save, with Section 9.28, Step 26
         (gamma <= 1/(2l) for a limit F(e.X) of a profile with 1/4 < l <= 5/12) and the changed sentences of
         Proposition 2.8(h), of the paragraph after it and of Sections 2 and 7: replay of the change identical; every
         step of Step 26 re-derived (the gradient along the forward orbit of a zero, the bounded forward orbit, the
         zeros far out, their escape if 2l - 1/gamma > 0, and the use of Step 17(i)): correct, and the changed
         sentences state exactly what Step 26 proves; the proposed final form built on it rebuilt identically, every
         entry of the previous final form kept: confirmed for installation and as the terminal text.
- 2026-10-19 17:00  verifier: the closing time line of the numerical report checked: its only change since the freeze,
         with its end time and elapsed time correct; the entries 16:19 and 16:39 as proposed; the proposed final form
         with them rebuilt identically, every entry of the previous final form kept: confirmed as the terminal text.
- 2026-10-19 17:04  verifier: the final version saved at 17:01 checked as the released report: rebuilt identically
         from its sources, the statements of Section 0 on times and sessions true, the entries 16:19, 16:39 and 17:00
         as proposed: confirmed as the released final report, an accurate partial-results report.
- 2026-10-19 17:37  the run stopped at its fixed execution limit (48 hours after T0).
- 2026-10-19 17:49  lead, after the stop: final edit of the status paragraph, of Section 0 (end time, elapsed time,
         number of sessions, accompanying artifacts), of the sentences of Sections 8 and 9 that refer to the
         accompanying artifacts, and of this timeline; no statement, proof or number of Sections 0a-5 and 7-9 was
         changed. This edit was made after the run had ended and was not checked by the verifier.
(End of the timeline.)

## 7. Conclusion
Neither endpoint has been reached. Partial analytic results and numerical observations follow. All numbered results of
Sections 2a and 3 have complete proofs in Sections 9.0-9.10, 9.16, 9.18, 9.24 and 9.25. Section 4.16,
Proposition 4.13a and Section 4.17 have complete proofs in Sections 9.11-9.13, respectively, and Section 4.18 in
Section 9.26. The Section 2 statements on subtracted laws, gauges, the orbit bound, the forms f(x) and f(x) + h(y) and
the polynomial solution are proved in Section 9.14. Proposition 2.1 is proved in Section 9.17, Propositions 2.2-2.6 in
Sections 9.19-9.23, respectively, Proposition 2.7 in Section 9.27 and Proposition 2.8 in Section 9.28. Theorem 4.9,
Corollary 4.10 and Remark 4.11 are proved in Section 9.15. Proposition 4.7 and Corollary 4.8 have proofs in Section
4.7 itself. The detailed proof inventory in Section 2a applies throughout this summary. Additional hypotheses and
proof availability are separate matters: a conditional implication may have a complete proof or only an outline. The
other structural statements of Section 4 are not proved in Section 9. In particular, the omitted label-coordinate
arguments of 4.6, the omitted construction of 4.7(v) and the outlines of Proposition 4.12 and of 4.15(f) are not
promoted to complete proofs here. Numerical observations retain their stated verification limits.
1. In S the once-subtracted velocity is unique and no strain gauge remains. Every profile in S has c_l > 1, focuses
   in finite time and has leading far field r^p A(th), with p = 1/c_l (Theorem A). For growth exponents
   1 <= gamma < 2, the twice-subtracted law leaves a symmetric traceless linear strain, fixed for a profile by the
   jet. Existence in these growth classes is unresolved. The exclusions of densities f(x) and f(x) + h(y) concern
   those forms with the velocity W_2 + MX (Section 9.14). Under the extra hypothesis W_2 = o(r), put
   beta = 2c_l - 1/2. Necessarily beta >= 1/gamma > 1/2. Every escaping orbit has limiting direction among +-e_1 and
   +-e_2. Orbits with directions +-e_1 exist, carry zero density, and each of those two directions carries exactly one
   orbit. An x-even profile must have a zero of V other than 0 (Propositions 2.3 and 2.5(a), Sections 9.20 and 9.22).
   Under W_2 = o(r), the family R^(-gamma) rho(RZ) is precompact for locally uniform convergence. Each subsequential
   limit is a_+ y_+^(1/beta) + a_- (-y)_+^(1/beta), possibly zero. If beta gamma > 1, then rho = o(r^gamma) uniformly
   in direction. If R^(-g) rho(RZ) has a nonzero locally uniform limit on the punctured plane that is homogeneous of
   degree g >= 1, then g = 1/beta and 1/2 < c_l <= 3/4 (Proposition 2.4(a), Section 9.21). Suppose also
   |W_2| <= C(1 + r)^(1 - delta), delta > 0. With the Hessian bound |D^2 rho| <= C(1 + r)^(gamma - 2),
   Proposition 2.4(c) first reduces the critical case beta gamma = 1 to gamma = 1 and a density taking negative
   values. Proposition 2.6(d),(e) excludes that remaining case. For the x-even exclusions of Proposition 2.5, assume
   every zero of V is nondegenerate and put nu = min(beta - 1/2, beta delta). No such x-even profile exists if
   beta gamma < 1 + nu, or if the Hessian bound holds and beta gamma < 1 + 2 nu. With bounded W_2, the first condition
   holds for gamma = 1 and every allowed beta; with bounded W_2 and the Hessian bound, the second holds for every
   gamma in [1, 2) and every allowed beta. These statements of Proposition 2.5 retain the nondegeneracy assumption
   (Section 9.22). Proposition 2.6(d),(e) gives exclusions without symmetry and without any assumption on the zeros of
   V. For 0 < delta <= 1, the power bound, the Hessian bound and
       gamma < min(2 delta + (1 - delta)/beta, 3 delta + 2/beta - 1)
   are incompatible with a profile. Part (d) first leaves only beta = 1 and rho = A Y, A != 0, where
   Y(X) = lim e^(-s) [Phi_s X]_2; part (e) excludes that case by an area comparison. Without the Hessian bound, the
   power bound is incompatible with a profile when beta gamma < 1 + min(beta - 1/2, beta delta) and
   beta > 1 - delta/2. The power and Hessian bounds are also incompatible with a profile when beta > 1 - delta/2,
   gamma < 1/beta + 1 + delta and gamma < 2/beta - 1 + 3 delta (Proposition 2.6(e)). Thus bounded W_2 with the Hessian
   bound excludes every gamma in [1, 2); bounded W_2 alone excludes gamma = 1 (Section 9.23). These are restricted
   exclusions: W_2 = o(r), the power bound and the Hessian bound are not derived here from C^3 regularity and the
   growth-class bounds. For 1 < gamma < 2 the class bounds do not imply W_2 = o(r), also together with a unique
   nonzero layered limit at infinity or with the Hessian bound (Proposition 2.7(e), by densities that are not
   profiles). Without that hypothesis the locally uniform limits f of R^(-gamma) rho(RZ) for a profile solve div(f
   W_2[f]) = 0, which has solutions that are not functions of y alone, such as |x|^gamma, and they are all functions
   of y alone exactly when W_2 = o(r^gamma) (Proposition 2.7, Section 9.27). Without W_2 = o(r), no profile is even in
   y or satisfies rho(-X) = rho(X); the nonzero homogeneous stationary functions are the
   a_+ (e.X)_+^gamma + a_- (-e.X)_+^gamma, e a unit vector, and, for each of the two horizontal directions, a family
   vanishing only in that direction and parametrized up to amplitude by an open disk, whose only members with a
   locally Lipschitz gradient on the punctured plane are the a(r + sigma x)^gamma; the homogeneous limits at infinity
   of a profile with the Hessian bound are 0 or a(r + sigma x)^gamma, and those of a profile even in x are a|x|^gamma
   or functions of y alone, and are 0 if the profile satisfies the Hessian bound; under the Hessian bound
   rho = o(r^gamma) exactly when W_2 = o(r^gamma); for a profile, a remainder O(r^q), q < 1, about a homogeneous limit
   f gives the condition ((A + M)X).grad f = f with a constant traceless strain M, whose consequence for f = |x|^gamma
   is met by a density that is not a profile; and such a remainder is impossible, also without the Hessian bound, if f
   is a member of one of the two families vanishing only in a horizontal direction, in particular if
   f = a(r + sigma x)^gamma with a != 0, and, for f = F(e.X) != 0 with q(2l - 1/gamma) < 1, if l = 1/4 or l > 5/12, or
   l > 1/4 and gamma > 1/(2l), or
   f <= 0, or f >= 0 and l >= 1/4, or f vanishes on a half-plane and l >= 1/6, and, for a C^m profile, m >= 3, if f
   vanishes on a half-plane and l >= 1/(2m), or 1/4 + 1/(2m) <= l <= 5/12 and l is not 1/4 + 1/(2n) with n odd, or
   3/16 < l < 1/4, (m - 1)(2l - 1/4) >= 1 and f takes negative values, and, for a C^infinity profile, if 0 < l < 1/4
   and f takes negative values (Proposition 2.8, Section 9.28). Higher growth leaves further harmonic
   stream-polynomial gauges. In a suitable gauge, rho = x^2 with psi = -x^3/3 + (c_l - 1/2)xy is a formal solution for
   every real c_l (Section 9.14). Proposition 2.1 concerns truncation limits (Section 9.17). For rho in S and every
   family of bounded measurable sets D_R containing B(0, R), the centered velocities of rho 1_{D_R} converge to the
   canonical W in C^2_loc. For rho = x^2, suitable truncations independently realize every linear strain and every
   homogeneous harmonic cubic correction to the stream function of the circular truncation. Suitable truncations
   produce the polynomial solution for each c_l, but no family of disks and no homothetic copies of a fixed centered
   ellipse do so. Centered ellipses with semi-axes R and B_R, B_R/R -> infinity, produce it for c_l = 1/2. For
   c_l != 1/2, no family of bounded measurable sets D_R containing B(0, R) and symmetric under y -> -y produces it.
   The density alone does not select this velocity. No selection or exclusion of it by matching to an outer flow is
   proved. For c_l > 1, the ansatz rho = f(y)x^2 + g(y)x + k(y), with psi cubic in x, the jet and W(0) = 0, has
   exactly the local curved-layer solution of Proposition 3.15 and the polynomial solution, up to the interval of
   definition and a constant in psi. Both are x-even, although parity is not assumed; the curved solution has a pole
   at y = -(2c_l - 1/2) (Proposition 3.15a, Section 9.16). The same classification holds for density degree at most
   three in x and any finite degree in x for psi (Proposition 3.15b, Section 9.18). Among polynomial solutions with
   the jet and W(0) = 0, rho = x^2 is the only density of degree at most three for every c_l. Under NR, namely
   c_l > 1/4 and c_l != 1/4 + 1/(2n) for integers n >= 3, uniqueness holds through degree seven, and through degree
   eleven if x^2 divides rho. In particular the degree-seven conclusion holds for every c_l > 5/12. For c_l > 1/4, no
   density x^2 (by + g(x))^k occurs when b is real and nonzero, g is a real polynomial with g(0) = 1, and k is a
   positive integer. General polynomial uniqueness in arbitrary degree is not proved (Proposition 2.2, Section 9.19).
2. Necessary conditions in S include the moment law (Theorem C) and the flux identities (Proposition 3.4), both
   proved in Section 9.8. The zero structure in S^+ and the vertical-wall system in S^+_even are given by Theorems 3.2
   and 3.3 and Proposition 3.6 (complete proofs in Sections 9.4 and 9.9). Outside S^+, the flow-topology and vanishing
   results of Theorem 3.8 assume that all zeros of V are nondegenerate; its dead-basin conclusion has the stated
   source-eigenvalue restrictions. Extra sources with weak eigenvalue in (0, 1/3] or in {1/2, 1} are not forced to
   have dead basins by 3.8(d). Proposition 3.9 assumes source eigenvalues 0 < alpha <= 1 < beta', and Proposition 3.10
   assumes the stated nonzero incoming power asymptotic at a saddle. Theorem 3.11 concerns exactly three nondegenerate
   zeros; its part (b) additionally assumes C^infinity, and the proof of its part (d) (no dead basin is a half-plane)
   does not use the assumption on the zeros of V. These results are proved in Sections 9.5 and 9.6. Proposition 3.12
   (Section 9.8) applies its translated moment law at any zero P with grad rho(P) = 0, including 0 in S^+; its
   analytic-profile conclusions concern all zeros. Every existing profile in S^+ has rho = |S|^p A(arg S) through the
   area-preserving homeomorphism S conjugating the flow to dilation (Theorem 3.13). This representation does not
   construct profiles; the Darcy coupling between A and S remains unresolved.
   Restricted nonexistence: no profile in S has an exactly homogeneous exterior (Proposition 3.18(c); for S^+ and for
   the profiles of Theorem 3.11 this was shown earlier in Theorems 3.5, 3.11(e) and 3.16); no profile in S^+_even has
   nonnegative transverse curvature g = d_x^2 W_2(0, y) of the vertical velocity on {y <= 0}, or g = 0 on
   (-(2l - 1/2), 0) (Proposition 3.14). In addition, no profile in S^+_even has A''(-pi/2) <= A''(pi/2) and
   w_e <= 0 on (0, inf), or both inequalities reversed, unless A''(-pi/2) = A''(pi/2) and w_e = 0 identically
   (Proposition 3.17, an exact identity between the two wall curvatures and the y-even part w_e of the vertical axis
   velocity, and the profile case of 5.8(v); complete proof in Section 9.10). Far field: for every profile
   in S (Proposition 3.18(c); Theorem 3.16(b) when A has a positive quadratic zero), the correction
   r^{2p-1} J_p[A]/(l - 1) is forced and nonzero in the distributional scaling sense of Theorem 3.16(a), and it is a
   uniform asymptotic expansion (Theorem 3.16(d); A is C^1 for every profile in S by Theorem 3.1). Consequently
   int_{R<r<2R} |rho - r^p A|^2 >= C R^{4p}: the remainder rho - r^p A is not in L^2(r > 1), nor in L^q(r > 1) for
   1 <= q <= 2/(1 - 2p) when p < 1/2 or for any finite q >= 1 when p >= 1/2 (Theorem 3.16(c)); these are tail
   obstructions, not nonexistence of S. Near c_l = 1, along sequences in S^+ satisfying the hypotheses of
   Corollary 4.8, ||c_n B_n/M_n^2||_inf is comparable to 1/(1 - p_n), with constants depending on the sequence.
   Also (1 - p_n)c_n B_n/M_n^2 converges uniformly to J_1[A_*]/2, which is not identically zero. The comparison of
   norms requires the stated convergence hypotheses. For the explicit exterior family A = cos^2 th, the correction
   velocity is negligible relative to the leading velocity in the joint limit eps = 1 - p -> 0 if and only if
   eps log r - 2 log(1/eps) -> infinity (4.7(iii)). This compares the displayed velocity terms; it is not a
   domain-size requirement for every solver.
   For every profile in S and every h > 0 there are c_h > 0 and R_h such that the area of
   {0 <= rho < h} cap {|X| <= R} is at least c_h R^(2 - p/2) for all R >= R_h (Proposition 3.18(a)).
   Without any assumption on the zeros of V, the far-field coefficient A of every profile in S has two distinct zeros
   at which A' = 0, and {A > 0} has at least two components that are open arcs ending at such zeros
   (Proposition 3.18(b), from an exact flux identity between a small circle around 0 and the circle of Theorem 3.1);
   consequently J_p[A] is not identically zero, so the conclusions of Theorem 3.16(c) and the exclusion of an exactly
   homogeneous exterior hold for every profile in S (Proposition 3.18(c), Section 9.24). In S^+, (b) is contained in
   Theorem 3.2. In S^+, A'' at the two zeros of A is determined by the renormalised passage times of the two branches
   of Gamma (Proposition 3.17a, an extension of Proposition 3.17 without parity), and the profile equation has an
   exact flux form off Gamma, an exact renormalisation at the zeros of A and, under additional smoothness and for 4l
   not an integer, a vanishing finite part (Section 4.18(a)-(c)); with the jet and growth of S, the second moment
   family of Proposition 3.4 is equivalent to the profile equation (4.18(d)). The explicit angular functions A_l of
   4.18(e) satisfy the conditions on the angular coefficient in 4.18(c), Theorem 3.2, Theorem 3.16(b), Proposition
   3.18(b), (c) and 4.16(a) for every l > 1 with 4l not an integer, so these conditions give no bound on c_l; no
   density or velocity on the plane is constructed (Sections 9.25 and 9.26).
   As c_l -> infinity, suppose the rescaled fields of 4.8 converge with f_n -> f in C^2_loc and b_n -> b in C^1_loc.
   Theorem 4.9(a) gives an equilibrium graph through 0, with positive density on that graph near 0 except at 0 itself.
   If also b(Z) - Z = o(|Z|), then f is bounded and has a maximum M > 0 at a zero q of b. The velocity b is not
   real-analytic. The product of the errors in b_n(q) and grad f_n(q) is at least M p_n/2 for all large n, so neither
   error is O(p_n) (Theorem 4.9(b)). Membership in S does not supply these convergence hypotheses. Under the
   hypotheses of Theorem 4.9(b) the limit solves (P0) (Section 4.8). Proposition 4.12, whose proof is only outlined,
   asserts a compact equilibrium set whose components with more than one point are compact embedded C^1 arcs;
   single-point components and accumulation are not excluded. At arc endpoints it asserts Df = D^2 f = 0, with
   vanishing of derivatives of orders 1 through k if f is C^k. It also asserts constant density on nonempty interiors
   of backward basins and a possible logarithmic far-field term. These assertions have no complete proofs here.
   Existence for (P0) remains open.
3. No nonexistence theorem for S, for S^+, or for the x-even part S^+_even is proved here. The scalar identities found
   are shape conditions; the two tested jointly (the moment law and the wall identity) are met to numerical accuracy
   by test densities with S^+_even-type geometry, which are not profiles (Section 4). Sections 4.14 and 4.15 constrain
   how x-even states could approach D = 0. The circulation bound of 4.15(a) makes the flat mismatch strain of a
   uniformly perturbative quadratic core vanish with D. Section 4.15(f) outlines, under its global C^3 odd
   regular-root and velocity hypotheses, the assertion that an x-even regular-root cusp limit has exponent g = p. Its
   proof is not supplied in full, and the exact layered states rho = H|x|^p are outside S. These observations are
   local or conditional and exclude nothing in S. Section 4.17 does not reduce
   the parity-free problem to x-even data. At a hypothetical profile in S^+_even, the linearisation -L fails
   the pointwise positive minimum principle on the x-odd perturbation of Section 4.17(b), which is nonnegative on
   x > 0 (this does not rule out every comparison theorem for stationary solutions), and in the direct realization
   of Section 4.17(c) the x-odd linearisation is not Fredholm, and no compact map from E_mu cap E, with the norm of
   the Holder space E of Section 4.17(f), into E agrees with the backward-flow operator of 4.17(e); whether the
   x-odd kernel is trivial is open.
4. Numerically, no candidate, and no state has passed the complete candidate verification package. The searches of
   Sections 5.3-5.6 approached c_l = 1 or failed to converge; the later searches (5.7, 5.8) stay away from that
   boundary and fail for the reasons described there. A forced continuation in c_l from the seed c_l0 = 2, resolved on
   r <= 1000 for c_l in [1.2, 2], with the forcing amplitude stable under the reported resolution and domain changes
   at the sampled parameter values (the forced-problem residual is about 1% of the forcing), has lambda >= 0.63 at the
   sampled stages with c_l in [1.1, 2.4] (Section 5.7). This is not a certified interval bound. The c_l = 1.1 state is
   only marginally resolved, and c_l > 2 was checked at one box size only. A branch from the third seed (c_l0 = 3.5)
   reaches lambda = 0.09 relative to its own forcing at c_l = 1.2 with R = 300 and 48 radial nodes, and 0.13 with
   R = 1000 and 64 radial nodes. These readings vary across grids and boxes; the states are unresolved beyond r = 100,
   and relative to the field their forcing near the centre is still of order one. The searches of 5.8(iv)-(vi) are
   restricted x-even exploratory searches and do not satisfy the parity-free search requirement of the task. At one
   x-even family state the x-odd fixed-datum spectrum of the discrete exit map was sampled; a real Ritz value 0.969
   found there belongs to a grid-scale vector and is not evidence of an x-odd eigenvalue near 1, and it does not
   persist when the angular resolution is doubled (nearest real Ritz value 0.846, again a grid-scale vector; 5.8(vi)).
   No parity-free profile search has been completed. In parity-free tests at one x-even state (5.8(vii)) no
   linear-response column for an x-odd mode met the acceptance rule at 256, 512 or 1024 angles, an amplitude
   continuation off the x-even subspace converged at none of five x-odd amplitudes, and a Newton run at 256 angles
   with an approximate variational tangent of the exit map did not converge at amplitude 1e-3 of the first x-odd mode;
   no profile, x-even or asymmetric, was found.
5. In the forward reformulation (Section 5.8), within the restricted class of stationary states of 5.8(c) and subject
   to its orientation, regularity and orbit-coverage hypotheses, the proposed matching conditions on a datum A and an
   exponent p are one scalar condition (m1 = 1/2) and one functional condition (Gt constant). A crossing of the
   discrete scalar diagnostic m1 = 1/2 is located numerically, to the quoted accuracy, inside a one-parameter x-even
   datum family at p = 0.5; the functional condition fails at that state. No state meeting both has been found; in the
   x-even states computed, the functional condition fails through an up-down asymmetry of the near-node density,
   D = log G(-inf)/G(+inf) (renormalised as in 5.8(iv) when m1 != 1/2), measured independently of the orbit tracers by
   a y-axis law. On the states where D is resolved in the sense used for search states it lies between -1.55 and
   -0.26; for the upper end this means both forms of the axis law, angle-converged, while the inner and outer radius
   and the full candidate tests are not resolved there, so no fully resolved aggregate range of D is claimed. The
   upper end -0.26 (direct form -0.26) is on a six-mode family at p = 0.35 with m1 = 0.505 (5.8(vi)). On that family
   the 512-angle values bracket m1 = 1/2 between a_2 = -1.2 and -1.25, with D about -0.24 to -0.25 at the crossing by
   interpolation (from inner radius e^-14 states; the inner radius e^-17 moves D by +0.014 at a_2 = -1.2); next to the
   crossing the exact-map iteration stops converging at 512 angles, and at a_2 = -1.3, off m1 = 1/2,
   the unconverged iterate has D = -0.24, which shows no further increase at inner radius e^-14 (larger inner-radius
   shifts were observed at sampled states nearer the crossing, so this says nothing about the inner-radius limit); the
   trend along the branch is unresolved. Values above -0.26 occur only where they are not resolved (the state
   a_2 = -1.25 of that family, -0.23 with m1 = 0.497, at one angular resolution and with axis-law spread 0.04; the
   unconverged state at a_2 = -1.228, -0.215 in the divergence form; two converged 512-angle states bracketing
   m1 = 1/2 at a_2 = -1.228 in a two-parameter extension of the family, -0.238 / -0.250, without a 1024-angle check,
   and the same states at inner radius e^-17, -0.220 / -0.232 in the divergence form and -0.237 / -0.234 in the direct
   form; a further step to inner radius e^-20 at the middle state moves D by +0.0008, and transferring that shift
   gives about -0.221 (divergence form) and -0.234 (direct form) at the m1 = 1/2 crossing of the extension, estimates
   only (the crossing itself was not computed at e^-20; one angular resolution); the window update of 5.8(vi),
   -0.12 / -0.14 in the two forms of the axis law (about -0.13), not converged in the inner radius; two 64-mode
   iterates, -0.24, and -0.19 to -0.22 (divergence form, two codes) / -0.26 (direct form), with axis-law spreads
   0.1-0.3); so -0.26 is not an upper bound on the asymmetry. This quantity has an exact expression through the
   endpoint values of F = log(A/cos^2 th) and the y-even part of the vertical velocity on the axis (5.8(v)); no sign
   is known to follow from the axis relations alone, and at fixed m1 the asymmetry moves under changes of A, so these
   computations give no obstruction, only the absence of a found solution. The values of A in narrow windows at its
   zeros are strongly coupled to m1 (5.8(vi)); a 64-mode search that appeared to approach both conditions at 256
   angles is, at 512-1024 angles, 0.06 away from m1 = 1/2 with asymmetry -0.31; its apparent progress came from a
   transport interpolant whose fixed point lies 0.025-0.03 lower in m1 at 512 angles. A 32-mode search with a
   corrected interpolant stays at least 0.011 above m1 = 1/2 (5.8(vi)).
6. Relation to broader classes: results stated for S do not cover growth exponents >= 1. Those growth bounds do not
   guarantee absolute convergence of the once-subtracted law or sublinear velocity. For growth in [1, 2), with the
   twice-subtracted law the jet fixes the added strain for a profile; higher growth leaves further harmonic gauges.
   The additional hypotheses of Propositions 2.3-2.6 (W_2 = o(r), the power and Hessian bounds, nondegenerate zeros)
   are not derived here from C^3 regularity and the growth bounds; for 1 < gamma < 2 the growth bounds alone do not
   imply W_2 = o(r) (Proposition 2.7(e)), and Proposition 2.8 does not assume it. Results stated for S^+ or S^+_even
   concern subclasses and are not nonexistence results for all of S.
7. Outstanding gaps. (i) Existence or nonexistence of profiles in S, in S^+ and in S^+_even is open. The identities
   proved in Sections 3 and 4 are necessary conditions under their stated hypotheses; the two tested jointly are met
   to numerical accuracy by test densities that are not profiles (item 3), and the angular conditions listed in
   4.18(e) give no bound on c_l beyond c_l > 1. In S^+, the Darcy coupling between the far-field datum A and the
   conjugacy S of Theorem 3.13 is not resolved. (ii) In the growth classes 1 <= gamma < 2 the additional hypotheses of
   Propositions 2.3-2.6 are not derived from the profile equation and the class bounds; the exclusions hold only under
   them (item 1), and these classes without them are open. For 1 < gamma < 2 the class bounds alone do not give
   W_2 = o(r), and without it the limits at infinity of a profile solve a stationary equation that also has solutions
   that are not functions of y alone; whether such limits occur, and whether the profile equation gives W_2 = o(r), is
   not decided (Propositions 2.7 and 2.8; under the Hessian bound a homogeneous limit at infinity of a profile
   is 0 or a(r + sigma x)^gamma, and by Proposition 2.8(h) a profile has no such nonzero limit with a remainder
   O(r^q), q < 1; without the Hessian bound, by the same part, no function vanishing in only one horizontal direction
   is a limit with such a remainder, no nonzero F(e.X) is one if l = 1/4, or if l > 5/12 and q(2l - 1/gamma) < 1, and
   for the other l <= 5/12 such a limit F(e.X) has a positive amplitude, two nonzero amplitudes if l >= 1/6, and
   amplitudes of opposite signs if l > 1/4, with the further restrictions of Proposition 2.8(h) for C^m profiles,
   m >= 3, among them two positive amplitudes if 3/16 < l < 1/4 and (m - 1)(2l - 1/4) >= 1, and, for C^infinity
   profiles with 0 < l < 1/4, two positive amplitudes). (iii) Numerically, no candidate was obtained. The matching
   conditions of Section 5.8 (m1 = 1/2 and Gt constant) are stated for the restricted class of stationary states of
   5.8(c) under its hypotheses, and meeting them would not by itself verify a candidate: a YES candidate must come
   from a parity-free search and pass the checks required by the task (Section 8). No state meeting both matching
   conditions was found, and the parity-free solvers tested at one x-even base state did not converge at x-odd data
   (Section 5.8(vii)).

## 8. Appendix: numerical methods, acceptance protocol and data
This appendix specifies the principal discretisations and diagnostic conventions of the computations of Section 5.8;
it adds no results. Reproduction of individual historical comparisons additionally requires the experiment-specific
data and settings listed with each comparison (8.8); where a setting was not recorded, this is said. Three numerical
implementations were used: two on uniform log-polar grids, called LP1 (it produced the Newton searches of 5.8(iv) and
5.8(vi)) and LP2, and one on a Gauss-Legendre panel grid, called PG. LP1 and LP2 share related algorithms and were
cross-checked against each other (8.3(a)); PG was written separately. The code of LP1, LP2 and PG and a small set
of records are in the accompanying artifacts (Section 0); most computed states and configurations are not included.

8.1 Representation. A state is (A, p, g) with g = r^-p rho and l = 1/p, on t = log r in [t_min, t_max]; outside
r_max = e^{t_max} the density is r^p A(th). x-even data are A = cos^2 th e^{F(th)}, F = sum_{j=1}^K x_j phi_j,
phi_j = sin j th (j odd), cos j th (j even).
Log-polar grids: uniform nodes in t and N uniform angles th_j = 2 pi j / N. The 32- and 64-mode data of 8.7 and the
LP1 and LP2 states of 5.8(vi) use 721 nodes on t in [-14, 10]; the six-mode search of 5.8(iv) used 661 nodes on [-12,
10] (8.8). Other computations of Section 5.8 use the resolutions and outer radii stated alongside their results,
including 128-angle calculations and outer radii e^20 and e^30.
Panel grid: P = round((t_max - t_min) ppu) panels with radial edges 0 and exp(t_min + j (t_max - t_min) / P),
j = 0, ..., P (edges uniform in t; the first panel [0, e^{t_min}] is the core panel), ppu = 3 for production states
and 5 or 6 in convergence runs, t_min = -12, -14, -16 or -17, t_max = 10. Each panel carries eight Gauss-Legendre
nodes in r; within a panel the density is the polynomial of degree seven in r through them. Angles: N uniform. For
orbit computations the fields are transferred to a grid uniform in t with spacing 0.01 (the angles stay on the N-angle
grid, spacing 2 pi / N), with t clamped to [t_min, t_max], so that below t_min the fields are held at their t_min
values.

8.2 Velocity. W is the field of Section 2 (div W = 0, curl W = -d_x rho, W(0) = 0, W = o(|X|)), computed per angular
Fourier mode, f_m = N^-1 sum_j f(th_j) e^{-i m th_j}, f = sum_m f_m e^{i m th}.
Log-polar (LP1, LP2): q = d_x rho = r^-1 (cos th d_t rho - sin th d_th rho), with d_th by FFT and d_t either sixth
order (derivative of the degree-six polynomial through seven points, the first or last seven at the ends) or fourth
order (second-order formulas in the first and last two rows). Sign conventions: -Delta psi = q, W_r = -r^-1 d_th psi,
W_th = d_r psi. For |m| >= 2
    psi_m(r) = (1/(2|m|)) [r^-|m| int_0^r s^(|m|+1) q_m ds + r^|m| int_r^inf s^(1-|m|) q_m ds];
for |m| = 1 the whole outer term (including its factor r) is replaced, so that
    psi_{+-1}(r) = (1/2) [r^-1 int_0^r s^2 q_{+-1} ds - r int_0^r q_{+-1} ds],
which fixes W(0) = 0; for m = 0, W_th,0 = -(1/r) int_0^r s q_0 ds. The Nyquist mode is dropped. The radial
convolutions run in t: with H_m(t) = e^{2t} q_m(e^t), k = |m|, Delta = t_{i+1} - t_i and z = k Delta, the inward
integral obeys L_i = e^{-z} L_{i-1} + w_far H_{i-1} + w_near H_i, and the outward one the same recurrence with
reversed indexing. LP1 and the corrected LP2 routine use w_near = Delta (z - 1 + e^-z) / z^2 and w_far = Delta
(1 - (1 + z) e^-z) / z^2 (limits Delta/2), which integrate the piecewise-linear interpolant of H_m against the
exponential kernel exactly; the original LP2 routine used the trapezoid weights Delta/2 on the exponentially weighted
integrand; LP2 results computed before 2026-10-18 05:20, which include the 128-angle box sequences of 5.8, used the
original routine. Initial values: L_0 = H_0 / (k + 2); for k >= 2 the outward start is H_last / (k - 1 - p); for
k = 1, J = int r q_1 by the trapezoid rule in t from J_0 = r_min q_1(r_min), and the outer term is -r J; for m = 0 the
trapezoid rule in t from H_0(t_min)/2. These initialisations hold q_m constant below r_min; they are not the quadratic
core extrapolation of 8.4(a). The part r > r_max is added in closed form from q_m(r) = q_m(R) (r/R)^(p-1), matched to
the computed endpoint value q_m(R); this is not the value r^(p-1) (p cos th A - sin th A') of an exterior density
exactly equal to r^p A, and the two need not agree numerically.
Panel (PG): with -Delta varphi = rho and d_z = (d_x - i d_y)/2, the once-subtracted complex field is
w = sum_m b_m(r) e^{i(m-2) th}, where
    4 b_m = -rho_m + 2(1 + |m|) r^(-|m|-2) int_0^r s^(|m|+1) rho_m(s) ds        (m <= 0),
    4 b_1 = -rho_1,
    4 b_2 = -rho_2 - 2 int_0^r rho_2(s) ds / s,
    4 b_m = -rho_m + 2(m - 1) r^(m-2) int_r^inf s^(1-m) rho_m(s) ds              (m >= 3),
and W = (2 Im w, 2 Re w - rho/2). Density modes |m| <= N/2 - 3 are kept in w; the local term -rho/2 uses the
unfiltered density. Full-panel integrals use eight-point Gauss quadrature; for a partial panel the panel polynomial is
interpolated to an eight-point Gauss rule on the subinterval. rho_m(R) is obtained by extrapolating the last panel
polynomial and continued as rho_m(R) (r/R)^p in the exterior integrals, which are evaluated in closed form.
Recorded velocity comparisons: (1) on one state filtered to angular modes |m| <= 32, PG and LP1 (at doubled
resolution) differ by at most 2.5e-3 in V_r/r and V_th/r on every radial band; (2) on one 1024-angle state, PG and the
corrected LP2 routine differ by at most 4e-3 in V_r/r (5e-3 in V_th/r) on t >= -8, and by 0.05 on [-11.5, -8], where
the inner closures differ.

8.3 Transport. (a) Semi-Lagrangian pseudo-time relaxation (LP1, LP2) of d_s g = V.grad g + p (W_r/r) g. W is frozen
during each step; the transport velocity and p W_r/r are evaluated at the midpoint foot, and the midpoint source
enters the exponential: g_new(X) = g(foot) exp(ds p (W_r/r)(midpoint)). If the foot lies outside r_max, the new value
is A at the foot angle. Frozen-velocity comparisons keep the same W for all steps. Steps ds = 0.005 to 0.04 as stated.
Interpolants: LP1 used tensor cubic Lagrange interpolation on four nodes per coordinate until 2026-10-18 07:06 and
cardinal cubic B-splines afterwards; their prefilter pads the array with 12 replicated inner rows, two outer inflow
rows and 12 further replicated outer rows, solves the radial tridiagonal system with diagonal 4/6 and off-diagonal
entries 1/6, and divides the angular Fourier coefficients by (4 + 2 cos(2 pi k / N)) / 6. A second B-spline version of
the LP1 step, used for cross-checks, uses the kernel sqrt(3) (sqrt(3) - 2)^|j| truncated to |j| <= 24, with periodic
angular and replicated radial extension; this approximates the inverse prefilter. LP2 uses a cubic interpolating
B-spline with 24 columns of periodic angular padding and nearest-value radial extension, the interpolated value
clipped to the range of the four surrounding data values.
(b) Exact characteristic map. For a frozen V, T[rho](X) = e^{-T(X)} r_max^p A(th_exit(X)), with T(X) the exit time of
the forward orbit from X through r = r_max and th_exit its exit angle. Put alpha = V_r/r, beta = V_th/r.
LP1 and LP2: classical RK4 in physical time at step 0.01 for dt/ds = alpha, dth/ds = beta, the fields interpolated by
tensor cubic splines (LP1 clips the interpolated velocity components to the range of the surrounding values; LP2 does
not clip). When an increment (Delta t, Delta th) crosses the outer circle, both increments and the elapsed-time
increment are multiplied by (t_max - t) / Delta t, i.e. the completed RK4 step is truncated linearly.
PG: tensor cubic Lagrange interpolation (4 x 4) of alpha and beta on the transfer grid. Radial integration solves
dth/dt = beta/alpha, ds/dt = 1/alpha with 800 equal RK4 steps from each starting t_0 to t_max (requires alpha > 0).
Arclength integration solves d(t, th, s)/d sigma = (alpha, beta, 1) / sqrt(alpha^2 + beta^2) in the (t, th) plane,
with step 0.03 and at most 6000 (default) or 8000 steps; the crossing step is recomputed as a radial RK4 step ending
at t_max.
All PG exit-map fixed points quoted in 5.8(vi) use arclength orbits at all points. On one state (the first 32-mode
iterate) one application of the map with the two orbit integrations differs by max |T_s - T_t| / r^p = 1.7e-5.
(c) Characteristic test (LP2). The characteristic image replaces g on the selected rows (t <= -4, or all rows) and the
other rows are left unchanged before the moment is recomputed; reported are the change of m1 and the maximum of
|log g - log(T[rho]/r^p)| by radial band. This maximum is taken over the cells with g_ij > 1e-3 max_j g_ij only (a
masked maximum); the moment of this test omits the core term of 8.4(a), and its angular exclusion is the fixed 6 deg
sector. The radius-dependent exclusion of 8.6(h) is not implemented in it.
(d) Exact-map fixed points rho = T[rho], with V recomputed from rho at each iteration, by Anderson-accelerated Picard
iteration: with residual f_n = T(u_n) - u_n and difference matrices Delta X, Delta F of at most six columns,
gamma = argmin ||f_n - Delta F gamma||_2 and u_{n+1} = u_n + f_n - (Delta X + Delta F) gamma (unit mixing). LP1
iterates on u = g / (r^2/(1 + r^2))^(1 - p/2), forms the physical state by projecting max(s u_{n+1}, 0) (s the inverse
scaling) and keeps the unprojected u_{n+1} internally; PG iterates on u = rho / r^p and restarts with Picard steps
damped by 0.5^(n_fail - 1) after invalid orbit evaluations. The x-even projection g(th) <- (g(th) + g(pi - th))/2 is
applied in LP1 and optionally (to T(rho)) in PG; the states computed with it are x-even by construction (scope remark
at the end of 5.8). Defects, with T_g = r^-p T[rho] and M_i = max_j g_ij: PG reports max_ij |T_g - g|; LP1
reports max |T_g - g| / M_i over the cells with g_ij > 1e-3 M_i. These are different quantities. Default limits: LP1
30 iterations and tolerance 1e-5, returning the final iterate; PG 60 iterations and tolerance 1e-11, returning the
iterate of smallest defect. An iteration stopped by its limit is unconverged; the LP1 map constructs an image even
when its orbit limit is exhausted, so its results are used only with zero unfinished orbits. These fixed points are
the reference values of 5.8(vi).

8.4 Diagnostics. (a) Node strain: m1 = l - c, c = psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX. With
S(r) = pi^-1 int rho(r, th) sin 3th dth, the corrected log-polar moment is
    c = trapz_t (e^-t S(e^t)) + R^(p-1) / (pi (1 - p)) int A(th) sin 3th dth + S(r_min) / r_min,
the last term assuming rho(r, th) = (r/r_min)^2 rho(r_min, th) below the grid. Older log-polar moments omit the core
term, and one of them gives both endpoints of the t grid full weight; values obtained without the core term are marked
as such in Section 5.8. PG applies eight-point Gauss-Legendre quadrature to S(r) / r^2 (S the real sine moment above;
in the complex convention of 8.2, S = -2 Im rho_3) on all panels including the core panel (exact only for polynomial
integrands of degree <= 15 in the panel variable) and adds the exterior part S(R) / (R (1 - p)) in closed form; its
m1 = l - sqrt(c^2 + b^2) is the smaller eigenvalue of [[l - c, -b], [-b, l + c]]
(b = 0 to 1e-16 on x-even states). The ring fit (reported only where stated): least-squares fit of V = M X on one grid
ring (in LP1 the ring of index 20 counted from zero), m1 the smaller eigenvalue of the symmetric part of M.
(b) Axis law and D (5.8(iv)). On the vertical axis B_+(r) = V_2(0, r) and B_-(r) = -V_2(0, -r) are the outward speeds,
a_div = 2l - B_+-'(r) and a_dir = alpha + d_th beta (equal for the exact velocity), and h_+- = r^(p-2) d_th^2 g (FFT
or local second difference). Finite-inner-radius convention:
    log k_+-(r) = int_{r_min}^r (m1 - a_+-(s)) / B_+-(s) ds,
    q_+- = log|h_+-| - 2 log k_+- - (1 - 2 m1) int_{r_min}^r ds / B_+-(s),     D = q_-(R) - q_+(R);
the absolute value records the implemented diagnostic, and reading D as a log ratio of transverse densities requires
h_+- > 0. The drift of a half-axis is the range (max - min) of q over the stated window. LP2 integrates in r by the
trapezoid rule with second-order radial differences and takes the drift on [-8, t_max]. LP1 integrates in t by the
trapezoid rule with sixth-order radial differences, takes the drift on [-6, 9.5], and adds K_+- = C_+- e^{t_min} to
log k_+-, where C_+- is the mean of e^-t r (m1 - a_+-) / B_+- over [t_min + 0.2, t_min + 2.2] (an estimate of the
integral below r_min); its D is converted to the finite-inner-radius convention by adding 2 (K_- - K_+). PG uses the
same q, with the a fields on the 0.01 transfer grid, k = 1 at the panel t_min, D taken at t = 9.5 and the drift on
[-8, 9.5]; the PG values quoted in 5.8(vi) use h by the local second difference (the FFT h gives the same D to 1e-3
but upper drifts of 1.6-6 from Gibbs oscillation next to the zero of A, which are not axis-law failures). On the
six-mode base state of 5.8(iv) the three implementations, each in its own convention, agree to 0.013 in D.
The band values of the D formula quoted in 5.8(v) are finite-grid integrals over the stated bands; the full formula
also needs the inner and outer tails, which one implementation adds as a fitted inner tail and the outer tail
4 (2l - m1) e_p R^(p-1) / (l^2 (1 - p)). The two are not interchangeable finite-grid quantities.
(c) log Gt on the exit circle. With e_1 the unit weak eigenvector at the node (horizontal for x-even states), X_0 the
end point and T the travel time of the backward orbit dX/ds = -V from the exit point,
    L_raw = log A(th_exit) - 2 log |e_1.X_0| - 2 m1 T,     log Gt = L_raw + 2 m1 p log R.
Angle differences do not depend on the added constant. At m1 = 1/2 a constant Gt, with converged node tracing, is the
node coefficient d of 8.6(f). Orbits by RK4. The LP1 tracer of the many-mode searches starts at t_max - 1e-9 and
interpolates the final crossing linearly (defaults: step 0.01, 1440 rays, stop at log radius -13); the LP1 tracer of
the six-mode search had the defaults 512 rays, step 0.02 and stop radius e^-9. The LP2 tracer starts at t_max, uses
step 0.01, and keeps the first full RK4 step that crosses the stop radius, using the point actually reached. Rays (512
to 2048) and stop radii (e^-9 to e^-13; e^-11.5 for the value quoted in Section 6, 05:39-05:55) are stated with the
results; a stop at e^-9 biases log Gt next to the lower zero by about -0.1 (Section 6, 04:49-05:01). Every centred
value states its averaging set: the many-mode residual centres over |cos th| > 0.02, the six-mode residual with the
weight A / max A, and the displayed LP2 values over |cos th| > 0.3 or > 0.05 as stated. Values at zeros of A are
interpreted through the axis limits; a numerical logarithm floor is not a measurement of that limit.
(d) Moment identity, finite-radius form (PG; 5.8(ii)). With phi = r^-3 sin 3th, I_R = int_{r<R} rho phi dX and
Q_R = int_{r<R} rho W.grad phi dX, the finite-radius transport defect is
    (1 - l) I_R + Q_R - R^(p-2) int A(th) sin 3th [l R + W_r(R, th)] dth,
computed with the radial Gauss weights multiplied by r 2 pi / N and the boundary velocity from the extrapolated last
panel.
The whole-plane comparison Q = pi (l - 1)(l - m1) of Theorem C is reported separately from this defect.

8.5 Newton searches. Six-mode search of 5.8(iv) (LP1; grid of 8.8): unknowns (x_1, ..., x_6, p); residual
R_0 = m1 - 1/2 (older moment of 8.4(a), without the core term) and R_j = sum_i w_i phi_j(th_i) (log Gt_i - mean_w
log Gt) / sum_i w_i, j = 1, ..., 6, with w = A / max A on 512 exit angles and e_1 from the ring fit; each evaluation
relaxed to dg/ds of order 1e-13; damped Gauss-Newton with Levenberg-Marquardt scaling and one-sided finite
differences (increment 0.02 in x), steps clipped to |dx| <= 0.5 and |dp| <= 0.1, started from A = cos^2 th at
p = 0.143. It stopped at its iteration limit with |F|_2 = 5.45e-3: the six-mode datum is not a converged root of
this residual.
Many-mode searches of 5.8(vi) (LP1): unknowns x_1, ..., x_K, p, optionally Gaussian bumps of log A centred at 90 and
270 deg, exp(-wrap(th - th_0)^2 / (2 sigma^2)) with sigma in radians (for each width the upper bump first). Residual:
(w_m (m1 - 1/2), C_1, ..., C_K and the bump coefficients), w_m = 3 or 10, C the least-squares coefficients of the
sampled log Gt on [1, phi_1, ..., phi_K and the bump columns] over |cos th| > 0.02 (pseudoinverse cutoff 1e-8);
optionally rows w_d times the direct-form upper and lower drifts on [-6, 9.5] and, since 2026-10-18 08:51, the row w_D
D (divergence form).
Steps: (J^T J + mu Dm) delta = -J^T F with Dm_ii = max((J^T J)_ii, max(1e-12 max_j (J^T J)_jj, 1e-14)); mu starts at
1e-2, is divided by 3 after an acceptance (floor 1e-6) and multiplied by 10 after a failure, four attempts; one-sided
finite-difference Jacobian (increments 0.01 in x, 0.004 in p) computed in one batch; step caps 0.3 in x and 0.03-0.04
in p; trial fractions 1, 0.6, 0.35, 0.2, 0.1; trial exponents clipped to [0.12, 0.9]; each trial compared with a
separately relaxed zero-displacement control; default relaxation lengths 1500 steps initially, 700 for the Jacobian
batch and 900 for trials. Optional exit-map polishing is applied to the initial state and to a selected trial before
acceptance. During step formation, however, the base state and residual are refreshed by semi-Lagrangian evolution, so
this implementation does not consistently use an exit-map residual with an approximate Jacobian, and polishing does
not by itself certify the acceptance protocol; the protocol (8.6(h)) requires residual values on exit-map fixed points
for any residual offered as evidence after 2026-10-18 07:52. Exit-map polishing in this implementation is restricted
to Fourier-only data; combined with bump unknowns it does not preserve the datum. If an axis diagnostic fails, the
optional penalty rows are left zero, and such a trial does not satisfy the axis-row requirement.

8.6 Additional acceptance checks for the restricted x-even search (diagnostics, never a proof). These checks are
supplementary: passing them would not by itself meet the YES standard of the task, which also requires a parity-free
search, three resolutions and three expanding domains, the Poisson and jet residuals in absolute norms, and
conditioning and harmonic-mode checks. Within the x-even search a state is a candidate only if all of the following
hold, an independent implementation reproduces (b)-(f), and (a)-(d) hold on exit-map fixed points in two
implementations.
(a) Stationarity: for semi-Lagrangian states max |d_s g| <= 1e-8 (the numerical definition of the diagnostic stated);
the exit-map defect (8.3(d), with its definition) is reported separately; the same state, to the tolerances below,
from a second start.
(b) |m1 - 1/2| <= 2e-3 by the core-corrected moment and the ring fit, with the node regime reached on the grid (a
within 0.02 of m1 at r_min on both half-axes).
(c) log Gt constant to 0.03 over all exit angles, including the zero-window limits from the axis law; |D| <= 0.02 and
drift <= 0.02 on both half-axes, in both forms of the axis law and in two implementations; the deep-stop tracer values
(stop log radius at least 1.5 below the beginning of the measured node regime, converged under deeper stopping) agree
with the axis limits. For search states (not candidates) the divergence form is admitted only if it changes by at most
0.02 under 512 -> 1024 angles, and the direct form is always reported next to it.
(d) The values of (b)-(c) move by less than half their tolerance under 512 -> 1024 angles, halved radial and
pseudo-time steps, r_max e^10 -> e^14 and r_min e^-12 -> e^-16, one change at a time.
(e) p < 1; |V|/r bounded away from 0 (no zero of V other than 0), with min |V|/r and min V_r/r reported;
|a_dir - a_div| <= 0.005 on both whole half-axes.
(f) Let rho_0 = r^p g and d its positive node coefficient, rho_0 = d x^2 + o(r^2). Normalise by the spatial-amplitude
scaling rho^(X) = d rho_0(X/d), W^(X) = d W[rho_0](X/d), which preserves the self-consistent transport equation, makes
the coefficient of x^2 equal to one, and has outer radius d r_max and leading exterior datum d^(1-p) A. With rho^ and
a velocity computed by an independent implementation, the relative residual |V.grad rho - rho| / (r^2
(1 + r^2/R_*^2)^((p-2)/2)), R_* = d^((1-p)/(2-p)) (a reference radius balancing r^2 and d^(1-p) r^p), is at the
discretisation level and decreases under (d); |log(rho^/x^2)| <= 0.02 at the node from both half-planes (when D != 0
the two half-planes have different coefficients); c_l = 1/2 + psi_xy(0). (Dividing rho_0 by its coefficient instead
would change the velocity and destroy stationarity.)
(g) The candidate calculation uses the corrected exterior and boundary value rho_ext = r^p A + r^(2p-1)
J_p[A] / (l - 1), with J_p[A] as in Theorem 3.16, and reports the change of (b)-(c) when the correction is omitted.
Homogeneous-tail calculations do not establish this test.
(h) Consistency, for every implementation whose m1 or log Gt enters a Newton residual, on each accepted iterate:
Newton residual values are evaluated on exit-map fixed points of the producing implementation; states with V_r < 0
lobes or slow windows are reported from exit-map reference solves, and other semi-Lagrangian results with their
one-step moment change and a pseudo-time-step comparison. (i) One exact-map step changes m1 by less than 1e-3. (ii)
max |log g - log(T[rho]/r^p)| <= 0.1 on t <= -8. For iterates (not for a candidate) the cells adjacent to the
exit-angle discontinuity on each ring (the two neighbouring grid points whose orbits exit at different zeros of A, and
one further cell on each side) are excluded; on t <= -9.5 the sector |sin th| < sin(max(6 deg, 2 kappa r)) about the
weak axis may be excluded instead, with m2 = 2l - m1, V_2(x, 0) = -k x^2 + ..., kappa = k / (m2 - 2 m1), k measured
from -beta(t, 0)/r on t <= -10 and reported with its radial variation (angles in radians). The excluded maximum is
reported separately. A candidate satisfies (ii) at all angles, with limiting ratios at the zeros of the density.
(i) A Newton residual offered for a candidate contains the row w_D D (divergence form, on the exit-map fixed point),
w_D of the order of w_m, and |F| is reported with and without that row.
No state in this report passed (a)-(i).

8.7 Data of the states quoted in 5.8 (coefficients x_j of F = log(A / cos^2 th) in the basis of 8.1). These lists
specify the boundary data (A, p), not the interior state g. The 32-mode state is an exit-map re-evaluation of the
sixth-iterate datum on 512 angles; the 64-mode datum was produced on 256 angles and copied unchanged into its
512-angle re-evaluation.
The 32- and 64-mode states have 721 log-radius nodes on [-14, 10].
- (iii): A_b = cos^2 th exp(-b sin 3th), p = 0.5, b* = 0.1235-0.1237 at r_max = e^10.
- (iv): the six-mode coefficients and p stated there.
- (vi), six-mode family: (x_1, ..., x_6) = (0.31474, a_2, -0.13666, 0.122, 0.107, -0.027), p = 0.35, a_2 in [-1.3,
-1.0].
- (vi), 32-mode search, sixth iterate: p = 0.405177, (x_1, ..., x_32) =
    0.084214, -0.761048, -0.280624, 0.206986, 0.138250, -0.093066, -0.030293, 0.060277,
    0.015319, -0.039138, -0.011946, 0.035362, 0.005625, -0.033404, -0.002423, 0.028887,
    0.002361, -0.024727, 0.001140, 0.024766, -0.004057, -0.023042, 0.006220, 0.023012,
    -0.009197, -0.020883, 0.007636, 0.013004, -0.003274, -0.007026, 0.001755, 0.004677
- (vi), 64-mode search, fifth iterate: p = 0.534476, (x_1, ..., x_64) =
    0.067750, -0.840399, -0.210269, 0.192504, 0.153544, -0.085350, -0.052794, 0.081960,
    0.011098, -0.064653, -0.014049, 0.027330, 0.030575, -0.008432, -0.023362, 0.017578,
    0.000830, -0.030955, 0.014687, 0.031721, -0.012819, -0.022142, 0.006123, 0.014608,
    -0.004556, -0.013254, 0.006364, 0.014263, -0.008219, -0.013980, 0.007506, 0.011077,
    -0.004765, -0.007818, 0.002476, 0.005928, -0.001798, -0.005301, 0.001904, 0.004711,
    -0.000988, -0.003345, -0.000081, 0.002253, 0.000380, -0.001895, -0.000346, 0.001736,
    0.000127, -0.001832, 0.000446, 0.002235, -0.000967, -0.002373, 0.000950, 0.001972,
    -0.000592, -0.001540, 0.000296, 0.001258, -0.000325, -0.001346, 0.000498, 0.001323

8.8 Settings of the principal quoted states. Settings not listed here or in the text were not recorded in this report.
- 5.8(iv), six-mode search: LP1, 661 nodes on [-12, 10], 256 angles, local cubic Lagrange interpolant, semi-Lagrangian
  relaxation with ds = 0.02, tracer as in 8.4(c), residual and steps as in 8.5.
- 5.8(vi), six-mode family at p = 0.35 (exit-map fixed points): PG, ppu 3, t_min -14 (checks at -17), 512 angles
  (checks at 1024), arclength orbits at all points, Anderson depth 6, x-even projection of T(rho) (an imposed
  restriction; not applied on the two earliest 512-angle states at a_2 = -1.1 and -1.2, inner radius e^-14, whose
  x-odd part is about 4e-7), 20-40 iterations, defects stated with the values.
- 5.8(vi), 32- and 64-mode searches: LP1, 721 nodes on [-14, 10], 512 angles (32 modes) and 256 or 512 angles (64
  modes), Lagrange interpolant before 2026-10-18 07:06 and B-spline afterwards, ds = 0.02, tracer 1440 rays to
  log radius -13 at step 0.01, w_m = 3 (one 64-mode run w_m = 10), step rules of 8.5; exit-map re-evaluations by LP1
  (8.3(d)) and PG.

## 9. Appendix: complete proofs of structural steps
This appendix gives complete proofs of the velocity law of Section 2 and of its growth-class statements on subtracted
laws, gauges, the orbit bound, the forms f(x) and f(x) + h(y) and the polynomial solution, of Propositions 2.1-2.8,
all numbered results of Sections 2a and 3, Sections 4.16-4.18, Proposition 4.13a, Theorem 4.9, Corollary 4.10 and
Remark 4.11. The arguments needed for these proofs are included below; longer drafts and audit records of the run
are not published with this report and are not used as inputs. Section 6
records the completed checks of each subsection and the versions they concern; an audit of an earlier research text is
not a check of every later insertion or wording change. Section 9.0 proves the velocity law, Theorem A and Theorem B
(F1), (F2), (F4) from the definitions of Section 2. Its proof of (F4) uses Section 9.1, which uses only Section 9.0,
Steps 1-6 and (F2). The stronger parenthetical conclusion of Theorem A is proved in Section 9.2. The last clause of
Theorem 3.8(e) is deferred from Section 9.5 to Section 9.6. The added general-S consequences in Section 9.3, Step 7,
and Section 9.8, Step 4, use Proposition 3.18(c), proved in Section 9.24, and the closing remark of Section 9.14 on
the polynomial solution refers to Proposition 2.1, proved in Section 9.17. These are later consequences or remarks;
they are not used in the arguments that precede them or in Sections 9.17 and 9.24. Apart from these references, each
of Sections 9.1-9.28 uses only Section 9.0 and earlier subsections.

### 9.0 The velocity law, Theorem A and Theorem B (F1), (F2), (F4)
Hypotheses: rho in C^3(R^2) with the jet and |rho(X)| <= C(1 + |X|)^gamma, |grad rho(X)| <= C(1 + |X|)^{gamma-1} for
some gamma in [0, 1); for Steps 3-7, rho is a nonzero profile: V.grad rho = rho with V = l X + W, l real. Notation:
r = |X|, K(Z) = (-sin 2th_Z, cos 2th_Z)/(2 pi |Z|^2) (even, homogeneous of degree -2, zero mean on circles), C a
constant depending on rho, Phi_s the flow of V.

Step 1 (the velocity law). For fixed X the integral W(X) = p.v. int [K(X - Y) - K(-Y)] rho(Y) dY - (rho(X)/2) e_2
converges: at Y = X as a principal value (K has zero mean on circles and rho is C^1), at Y = 0 absolutely
(rho(Y) = O(|Y|^2) by the jet), and at infinity absolutely (|K(X - Y) - K(-Y)| <= C|X||Y|^{-3} for |Y| >= 2|X|, and
gamma < 1). W(0) = 0. With rho_R = chi(./R) rho, chi in C_c^inf, chi = 1 on |X| <= 1, chi = 0 on |X| >= 2,
W_R := U_R - U_R(0), U_R the Biot-Savart velocity of the compactly supported rho_R (U_R = (-psi_y, psi_x), -Lap
psi = d_x rho_R), is given by the same formula with rho_R, and for |X| <= R/2 the difference W_R(X) - W(X) is an
integral over |Y| >= R bounded by C|X| R^{gamma-1}. So W_R -> W locally uniformly, and div W = 0, curl W = -rho_x, in
distributions. Then Lap W_1 = rho_xy, Lap W_2 = -rho_xx are in C^{0,alpha}_loc for every alpha < 1; W is continuous,
so on a ball W_j minus the Newtonian potential of a localized right side is a harmonic distribution, hence smooth
(Weyl's lemma), and interior Schauder estimates give W in C^{2,alpha}_loc. Uniqueness (using W = o(|X|) from Step 2,
which does not use uniqueness): if W' is C^1 with the same divergence and curl, W'(0) = 0 and W' = o(|X|), each
component h of W' - W is harmonic and o(|X|); the gradient estimate |grad h(a)| <= (C/R) sup_{B(a,R)} |h| with
R -> inf gives grad h = 0, so h is constant, hence 0.

Step 2 (growth of W). Let |X| = r >= 2 and split W(X) + (rho(X)/2) e_2 = I_1 + I_2 + I_3 + I_4 with
    I_1 = p.v. int_{|Y - X| < 1} K(X - Y) rho(Y) dY = int_{|Y - X| < 1} K(X - Y)(rho(Y) - rho(X)) dY,
    I_2 = int_{|Y| < 2r, |Y - X| >= 1} K(X - Y) rho(Y) dY,   I_3 = -int_{|Y| < 2r} K(-Y) rho(Y) dY,
    I_4 = int_{|Y| >= 2r} [K(X - Y) - K(-Y)] rho(Y) dY.
Suppose |rho(Y)| <= C_q (1 + |Y|)^q for some q in [0, 1) (q = gamma is the class bound). Then |I_1| <= C sup_{B(X,1)}
|grad rho| <= C r^{gamma-1}; |I_2| <= C_q C r^q int_{1 <= |Z| <= 3r} |Z|^{-2} dZ <= C r^q log r; |I_3| <= C + C_q C
int_1^{2r} s^{q-1} ds <= C r^q log r; |I_4| <= C_q C r int_{2r}^inf s^{q-2} ds <= C r^q. Hence
    (9.0.1)   |W(X)| <= C (1 + r)^q (1 + log(1 + r))   for all X,
in particular W(X) = o(|X|).

Step 3 (flow; l >= 1/gamma). V is C^{2,alpha}_loc with |V(X)| <= C(1 + |X|), so the flow is complete; d/ds rho(Phi_s
X) = (V.grad rho)(Phi_s X) = rho(Phi_s X) gives rho(Phi_s X) = e^s rho(X). Fix eps > 0 and C_eps with
|W| <= eps|X| + C_eps. For m(s) = (1 + |Phi_s X|^2)^{1/2} and l^+ = max(l, 0), dm/ds = (l|Phi_s X|^2 + Phi_s
X.W)/m <= (l^+ + eps) m + C_eps, so m(s) <= (m(0) + C_eps s) e^{(l^+ + eps)s}. If rho(X) != 0, then e^s
|rho(X)| = |rho(Phi_s X)| <= C m(s)^gamma, and letting s -> inf gives 1 <= gamma (l^+ + eps) for every eps > 0. Since
rho is not identically zero, gamma > 0 and l >= 1/gamma > 1; put p = 1/l, so p <= gamma < 1.

Step 4 (the jet and the source at 0). With M = DV(0) = l I + DW(0): rho = x^2 + O(|X|^3), grad rho = (2x,
0) + O(|X|^2) (rho in C^3) and V = MX + O(|X|^2) (V in C^2) give V.grad rho = 2 M_11 x^2 + 2 M_12
xy + O(|X|^3) = x^2 + O(|X|^3), so M_11 = 1/2 and M_12 = 0. div W = 0 and curl W(0) = -rho_x(0) = 0 make DW(0)
symmetric and traceless, DW(0) = [[-c, 0], [0, c]] with c = psi_xy(0) (psi the stream function of W, W = (-psi_y,
psi_x)); hence l = 1/2 + c, psi_xx(0) = psi_yy(0) = 0 and DV(0) = diag(1/2, 2l - 1/2), with 2l - 1/2 > 3/2.

Step 5 (radial dynamics and the bound rho = O(r^p)). Fix R >= 2 with |W(X)| <= (l/2)|X| for |X| >= R and such that
r^{gamma-1}(1 + log r) is decreasing on [R, inf). There V.X >= (l/2)
|X|^2. For |Y| = R let r(s) = |Phi_s Y|; then dr/ds >= l r/2, so r(s) >= R e^{ls/2}, and by (9.0.1) with q = gamma,
|d/ds log r - l| <= C r^{gamma-1}(1 + log r) <= C (1 + s) e^{-(1 - gamma) l s/2}, which is integrable, uniformly in
Y. Hence c_R e^{ls} <= r(s) <= b_R e^{ls} with constants independent of Y. For |X| > R the backward orbit of X has
|Phi_{-s} X| strictly decreasing while it is >= R, at rate >= lR/2, so it meets the circle |Y| = R at exactly one time
t(X) (it cannot leave the closed disk backward, since V.X > 0 on its boundary); with Y = Phi_{-t(X)} X,
|X| = r(t(X)) >= c_R e^{l t(X)}, and
    |rho(X)| = e^{t(X)} |rho(Y)| <= max_{|Y| = R} |rho| (|X|/c_R)^p.
So |rho(X)| <= C(1 + |X|)^p. Not o(r^p): take X_0 = (x_0, 0) with 0 < |x_0| < R so small that rho(X_0) > 0 (the jet);
|rho(Phi_s X_0)| = e^s |rho(X_0)| -> inf and rho is bounded on compact sets, so the forward orbit meets |Y| = R at
some Y with rho(Y) != 0, and along the forward orbit of Y, |rho| = e^s |rho(Y)| >= (r(s)/b_R)^p |rho(Y)|, with
r(s) -> inf.

Step 6 (Theorem A: far field). Step 2 with q = p gives |W(X)| <= C|X|^p (1 + log|X|) for |X| >= 2, hence for |X| >= 1
with a larger C (W is bounded on 1 <= |X| <= 2). In polar
coordinates the profile equation reads l r d_r rho - rho = -W.grad rho, that is
    l r^{p+1} d_r (r^{-p} rho) = -W.grad rho,
so |d_r(r^{-p} rho)| <= C r^{gamma-2}(1 + log r), which is integrable on [2, inf). Hence r^{-p} rho(r, th) -> A(th)
uniformly in th, with |r^{-p} rho(r, th) - A(th)| <= C r^{gamma-1}(1 + log r); A is continuous, and not identically
zero by the last part of Step 5. Holder continuity: for |th_1 - th_2| = d small and r = d^{-1/(1-p)},
    |A(th_1) - A(th_2)| <= 2C r^{gamma-1}(1 + log r) + r^{-p} r d sup_{|Z| = r} |grad rho| <= C d^beta (1 + log(1/d)),
beta = (1 - gamma)/(1 - p) in (0, 1]. If p < gamma, then beta < 1 and A is Holder continuous of every exponent
alpha < beta (because of the logarithm this argument does not give alpha = beta). If p = gamma, the bound
|r^{-p} rho(r, th_1) - r^{-p} rho(r, th_2)| <= r^{1-p} d sup_{|Z| = r} |grad rho| <= C d holds uniformly in r and
passes to the limit, so A is Lipschitz. (The C^{2,alpha} regularity of A and the rate C r^{p-1} are Theorem 3.1,
Section 9.2, whose proof uses Steps 1-6; they are not used here.) Together with Steps 3-5 this is Theorem A.

Step 7 (Theorem B (F1), (F2), (F4)). (F1): at a critical point Z of rho, rho(Z) = V.grad rho(Z) = 0; so rho has no
nonzero local extrema; at a zero of V, rho = V.grad rho = 0. A component U of {rho != 0} is invariant (rho(Phi_s
X) = e^s rho(X) does not vanish, so the connected orbit segment from X to Phi_s X lies in {rho != 0}, hence in U, for
every real s), and if U were bounded, |rho(Phi_s X)| = e^s |rho(X)| would be
unbounded on the compact closure of U; so U is unbounded. (F2): V.X >= (l/2)|X|^2 > 0 for |X| >= R (Step 5); for
|X| >= R, d/ds |Phi_{-s} X|^2 = -2 (V.X)(Phi_{-s} X) < 0 while |Phi_{-s} X| >= R, so |Phi_{-s} X| <= max(|X|, R) for
all s >= 0. A nonstationary periodic orbit (0 is a stationary one) contains no zero of V, and, parametrized with its
minimal period, it is a C^1 Jordan curve; its bounded complementary component D is invariant (Phi_s is a
homeomorphism preserving the curve, and Phi_s of the closure of D is compact) while |Phi_s D| = e^{2ls}|D| (div
V = 2l), which is impossible for 0 < |D| < inf. (F4): Section 9.1 uses only Steps 1-6 and (F2), so it may be used
here. By Section 9.1, Steps 4-6, rho = xi^2 on the open set B(0), which contains Gamma, with xi in C^2, D xi != 0 on
B(0) and Gamma = {xi = 0}; so rho = 0 and grad rho = 2 xi grad xi = 0 on Gamma. On a branch of Gamma minus 0 (an
orbit, V != 0), H := D^2 rho = h N N^T with N the unit normal and h = 2|grad xi|^2 > 0 (grad xi is normal to
Gamma, since xi = 0 on Gamma). Differentiating V.grad rho = rho twice on R^2 and then using
grad rho = 0 on Gamma gives, along the orbit, dH/ds = H - DV^T H - H DV (this uses rho in C^3 and V in C^2). Since
HN = hN and N.N' = 0, dh/ds = N^T (dH/ds) N = h(1 - 2 N^T DV N), and N^T DV N = div V - T^T DV T = 2l - d/ds log|V|
(T = V/|V|, d/ds |V|^2/2 = V^T DV V). Hence d/ds log(h/|V|^2) = 1 - 4l (s the flow time).

### 9.1 Theorem B (F3) and the coverage B(0) = R^2
Hypotheses: rho in S is a profile, l = c_l > 1. Used from Section 9.0 (Theorem A and Theorem B (F2)): V(0) = 0,
DV(0) = A := diag(a, b) with a = 1/2 and b = 2l - 1/2 > a; div V = 2l; |W(X)| <= C|X|^p (1 + log|X|) for |X| >= 2;
X.V(X) > 0 for |X| >= R. Notation: Phi_t is the flow of V, B(0) = {X : Phi_{-t} X -> 0 as t -> +inf},
xi_t(X) = e^{at} x(Phi_{-t} X).

Step 1 (regularity and completeness). On a compact set of X, |K(X - Y) - K(-Y)| <= C|Y|^{-3} and the m-th X-derivative
of the kernel difference is O(|Y|^{-2-m}) for large |Y|; with |rho| <= C(1 + |Y|)^gamma, gamma < 1, the far part of
the integral is smooth, and the near part is continuous (principal value against a C^1 density). From div W = 0 and
curl W = -rho_x, in distributions, Lap W_1 = rho_xy and Lap W_2 = -rho_xx. Since rho is C^3, these right sides are in
C^{0,alpha}_loc for every alpha < 1, and interior Schauder estimates give W, V in C^{2,alpha}_loc. The proof
uses only that DV is locally Lipschitz and D^2 V is continuous. By Theorem A, |V(X)| <= C_*(1 + |X|); Gronwall gives
completeness of the flow, and the maps Phi_t are C^2 diffeomorphisms.

Step 2 (contracting ball). Write V(Z) = AZ + N(Z). Fix R_0 > 0 and M >= max(1, sup_{|Z| <= R_0} ||D^2 N(Z)||), so
|N(Z)| <= M|Z|^2/2 and ||DN(Z)|| <= M|Z| for |Z| <= R_0. Fix delta < R_0 with M delta <= a/2, put mu = a/2, and let
B_delta be the open ball of radius delta. For Z in B_delta and z(t) = Phi_{-t} Z,
    (1/2) d|z|^2/dt = -z.Az - z.N(z) <= -mu |z|^2,
so B_delta is backward invariant and |z(t)| <= e^{-mu t}|Z|. Dividing by |z|^2 gives d log|z|/dt <= -a + (M/2)|z|,
and int_0^inf |z| dt <= delta/mu; with C_0 := exp(M delta/mu),
    (9.1)  |z(t)| <= C_0 e^{-at} |Z|   (t >= 0).
The evolution operator E(t, s) of q' = -(A + DN(z(t))) q satisfies ||E(t, s)|| <= C_0 e^{-a(t-s)} (energy inequality,
q.Aq >= a|q|^2). Hence F := D_Z z satisfies ||F(t)|| <= C_0 e^{-at}. The second derivative H := D_Z^2 z solves
H' = -(A + DN(z)) H - D^2 N(z)[F., F.], H(0) = 0, and variation of constants gives ||H(t)|| <= C_H e^{-at} with
C_H = M C_0^3/a. All constants are independent of Z in B_delta.

Step 3 (the local coordinate). The first component of the backward equation is z_1' = -a z_1 - N_1(z), so
    xi_t(Z) = x - int_0^t g_s(Z) ds,   g_s(Z) := e^{as} N_1(z(s, Z)).
By Step 2, |g_s| <= (M/2) C_0^2 |Z|^2 e^{-as} and ||Dg_s|| <= M C_0^2 |Z| e^{-as}; since
D^2 g_s[h, k] = e^{as}(D^2 N_1(z)[Fh, Fk] + DN_1(z) H[h, k]), also ||D^2 g_s|| <= M C_0 (C_0 + C_H delta) e^{-as}.
Hence xi_t converges in C^2(B_delta), uniformly, to xi_loc := x - int_0^inf g_s ds, with
||D^j(xi_t - xi_loc)|| <= C e^{-at} for j = 0, 1, 2; moreover xi_loc(0) = 0, D xi_loc(0) = (1, 0) and
xi_loc = x + O(|Z|^2). No nonresonance condition enters: d_ij xi_loc(0) = -d_ij N_1(0)/(lambda_i + lambda_j - a),
with lambda_1 = a, lambda_2 = b, and all denominators are positive.

Step 4 (the basin). B(0) is the increasing union of the open sets Phi_n(B_delta), n = 0, 1, 2, ...; it is open and
invariant. For X in B(0) with Phi_{-T} X in B_delta, xi_t(X) = e^{aT} xi_{t-T}(Phi_{-T} X) for t >= T, so the limit
xi(X) = e^{aT} xi_loc(Phi_{-T} X) exists and does not depend on T. A compact set K in B(0) lies in a single
Phi_T(B_delta); by the chain rule with the fixed map Phi_{-T}, xi is C^2 near K and xi_t -> xi in C^2(K) at the rate
e^{-at}. From xi(Phi_s X) = e^{as} xi(X) one gets V.grad xi = xi/2. Finally,
D xi(0) = D xi_loc(0) = (1, 0), so D xi_loc != 0 on a neighbourhood U of 0; for X in B(0) take T so large that
Phi_{-T} X lies in U; then D xi(X) = e^{aT} D xi_loc(Phi_{-T} X) D Phi_{-T}(X) != 0, since D Phi_{-T} is invertible.

Step 5 (rho = xi^2). Along backward orbits rho(Phi_{-t} X) = e^{-t} rho(X) = e^{-2at} rho(X). Taylor's theorem with
the jet and rho in C^3 gives rho(Z) = z_1^2 + R(Z), |R(Z)| <= C_rho |Z|^3 on B_delta (delta reduced if necessary).
Hence rho(Z) = (e^{at} z_1(t))^2 + e^{2at} R(z(t)), and by (9.1) |e^{2at} R(z(t))| <= C_rho C_0^3 |Z|^3 e^{-at}.
Letting t -> inf gives rho = xi_loc^2 on B_delta, and the scaling of Step 4 gives rho = xi^2 on B(0). The argument
never divides by z_1, so orbits that approach 0 along the strong direction are included.

Step 6 (the zero set). By Step 4, 0 is a regular value of xi, so Gamma := xi^{-1}(0) is an embedded C^2 curve,
invariant under the flow, and near 0 a graph x = h(y) with h(0) = h'(0) = 0. On this graph the backward equation is
y' = -by - q(y) with |q(y)| <= C y^2. Fix beta_0 in (a, b) and eta > 0 with C eta <= b - beta_0; then
|q(y)| <= (b - beta_0)|y| on |y| <= eta, so the local arc {|y| <= eta} is backward invariant, y keeps its sign,
|y(t)| <= e^{-beta_0 t}|y(0)|; since d/dt log|e^{bt} y| = -q(y)/y and |q(y)/y| <= C|y(t)| is integrable, e^{bt} y(t)
converges to a nonzero constant. Hence points of the local arc satisfy |Phi_{-t} X| = O(e^{-bt}), and, after a finite
entry time, so do all points of Gamma. Conversely, if |Phi_{-t} X| = O(e^{-beta t}) for some beta > a, then
xi(X) = lim e^{at} x(Phi_{-t} X) = 0. So Gamma is the strong unstable manifold of 0, characterised by faster backward
decay; it is the increasing union of the forward images of a local arc through 0, hence connected, and it is a line,
not a circle: a compact circle covered by the increasing open arcs would lie in one of them. Differentiating
rho = xi^2 twice gives D^2 rho = 2 D xi (x) D xi on Gamma, so the second normal derivative is 2|D xi|^2 > 0 and rho
vanishes exactly to second order on Gamma.

Step 7 (coverage). Assume V has no zero besides 0. Choose R with Z.V(Z) >= l|Z|^2 - C|Z|^{1+p}(1 + log|Z|) > 0 for
|Z| >= R (possible by the growth bound on W and p < 1). Since d|z|^2/dt = -2 z.V(z) < 0 for |z| >= R along backward
orbits, every backward orbit stays in the ball of radius max(|X|, R), and its limit set L is nonempty, compact and
invariant. There are no nonconstant periodic orbits: for the bounded interior D of such an orbit, Green's theorem
gives 0 = int_{dD} V.n ds = int_D div V dX = 2l|D| > 0. The Poincare-Bendixson theorem (for a C^1 planar field, if a
forward semiorbit lies in a compact set and its limit set contains no equilibrium, then the limit set is a periodic
orbit), applied to -V, shows that 0 is in L. So the orbit enters B_delta and then converges to 0 by (9.1). Hence
B(0) = R^2, Step 4 applies on every compact subset of the plane, xi is C^2 on R^2 and rho = xi^2 >= 0.

Regularity used here: rho in C^3 gives xi in C^2, which is all that Theorem B (F3) states; no third derivative of
xi is used.

### 9.2 Theorem 3.1 (scattering map) and the regularity of A
Hypotheses: rho in S is a profile, l = c_l > 1, p = 1/l, lambda := l - 1. Used: |grad rho(X)| <= C(1 + |X|)^{gamma-1}
with gamma < 1 (class S), |W(X)| <= C|X|^p (1 + log|X|) for |X| >= 1 (Theorem A), div V = 2l, the global C^2 flow and
W in C^2_loc (9.1, Step 1); omega := curl W = -rho_x;
J(x, y) = (-y, x); X_a(s) = Phi_s(R e_a) with polar coordinates (r_a(s), th_a(s)), th_a(0) = a.

Step 1 (vorticity law). Differentiating V.grad rho = rho in x and using d_x V = l e_1 + d_x W gives
    V.grad omega = (1 - l) omega + d_x W.grad rho.

Step 2 (local derivative estimate). Let |X_0| = r be large, d = r/8, B = sup |W| and G = sup |grad rho| over
B(X_0, d), and M(t) = sup |DW| over B(X_0, t). For Z in B(X_0, t), 0 < t < u < d, h = u - t, take a cutoff chi on
B(Z, h) equal to 1 on B(Z, h/2), |grad chi| <= C/h, and Q = Bs * (chi omega) with Bs(Y) = JY/(2 pi |Y|^2). Then
H = W - Q is harmonic on B(Z, h/2), |Q| <= ChG there and |DH(Z)| <= C(B/h + G). With E = V(Z)/|V(Z)| and
v = |V(Z)| >= c l r,
    d_E Q(Z) = int Bs(Z - Y) [(d_E chi) omega + chi d_E omega](Y) dY,
    v d_E omega(Y) = V(Y).grad omega(Y) + (V(Z) - V(Y)).grad omega(Y).
By Step 1, |V.grad omega| <= (l - 1 + M(u)) G on B(Z, h), so the convolution of the first part with Bs(Z - .) chi is
at most ChG(l + 1 + M(u)); in the second, integration by parts onto Bs(Z - Y) chi(Y) (V(Z) - V(Y))
(|Bs(Z - Y)| <= C|Z - Y|^{-1}, |D Bs(Z - Y)| <= C|Z - Y|^{-2}, |V(Z) - V(Y)| <= (l + M(u))|Z - Y|, div_Y
(V(Z) - V(Y)) = -2l; the boundary term on a small circle about Z vanishes in the limit) bounds every term by
ChG(l + 1 + M(u)). Hence |d_E Q(Z)| <= CG + (ChG/v)(l + 1 + M(u)). Since div W = 0 and curl W = omega, the matrix
DW(Z) is determined by DW(Z)E and omega(Z), |DW(Z)| <= C(|d_E W(Z)| + |omega(Z)|), so
    M(t) <= C(B/h + G) + C G (h/r) M(u).
For r large, C G/8 <= 1/4 (G <= C r^{gamma-1} -> 0); iterating along t_n = d(1 - 2^{-n-1}) gives
M(d/2) <= C(B/d + G) (the iteration converges because M(d) < inf, W being C^1 on the closed ball), and with
Theorem A
    |DW(X)| <= C (|X|^{p-1} (1 + log|X|) + |X|^{gamma-1})   (|X| large).
This bound uses the vorticity law of Step 1 as well as the bounds defining S.

Step 3 (positions). Fix R with V.X >= l|X|^2/2 for |X| >= R. There r_a' = V_r >= l r_a/2 and th_a' = W_th/r_a, so
r_a(s) >= R e^{ls/2}, and |d/ds log(e^{-ls} r_a)| + |th_a'| <= C r_a^{p-1}(1 + log r_a) has an integrable majorant
uniform in a. Hence c_R e^{ls} <= r_a(s) <= b_R e^{ls}, and e^{-ls} r_a -> L(a) in [c_R, b_R], th_a -> Theta(a),
uniformly in a with error C(1 + s) e^{-lambda s}. Every X with |X| > R has a unique backward hitting time of the
circle |X| = R, C^1 in X by the implicit function theorem (V_r > 0 there), so (a, s) -> Phi_s(R e_a) is a C^1
diffeomorphism of S^1 x [0, inf) onto {|X| >= R}.

Step 4 (first derivatives and the formula for Theta'). P_s(a) := e^{-ls} D Phi_s(R e_a) solves d_s P_s = DW(X_a(s))
P_s, P_0 = I, and F_s(a) := e^{-ls} X_a(s) satisfies d_a F_s = P_s R J e_a. By Steps 2 and 3, sup_a
|DW(X_a(s))| <= k(s) with k integrable on [0, inf). Gronwall bounds ||P_s|| and ||P_s^{-1}|| uniformly and gives
||P_t - P_s|| <= C int_s^t k, so P_s -> P_inf uniformly in a. Integrating d_a F_s over intervals and passing to the
limit gives F = L e_Theta in C^1 with F' = P_inf R J e_a; hence L, Theta are C^1 and d_a(e^{-ls} r_a) -> L',
d_a th_a -> Theta' uniformly. From det D Phi_s = e^{2ls} (div V = 2l), det P_inf = 1; from
D Phi_s(X) V(X) = V(Phi_s X) and e^{-ls} W(X_a(s)) -> 0, P_inf V(R e_a) = l F(a). Therefore
    l L^2 Theta' = det(l F, F') = det(P_inf V(R e_a), P_inf R J e_a) = det(V(R e_a), R J e_a) = R V_r(R e_a) > 0,
so Theta is a C^1 covering map of the circle. The lift fixed by th_a(0) = a satisfies th_{a+2pi}(s) = th_a(s) + 2pi,
hence Theta(a + 2pi) = Theta(a) + 2pi; the degree is one and Theta is an orientation-preserving C^1 circle
diffeomorphism.

Step 5 (bootstrap and rates). Differentiating rho(Phi_s X) = e^s rho(X) gives
grad rho(X_a(s)) = e^{(1-l)s} P_s^{-T} grad rho(R e_a), so |grad rho(X)| <= C|X|^{p-1}. With this bound the
four-region estimate of the velocity law in its density form (near field: the kernel has zero angular mean and
|grad rho| <= C r^{p-1}; far field: the growth bound) gives |W(X)| <= C|X|^p (no logarithm), and Step 2 gives
|DW(X)| <= C|X|^{p-1}. All errors in Steps 3 and 4 are then O(e^{-lambda s}), uniformly in a.

Step 6 (amplitude). Along characteristics rho(X_a(s)) = e^s rho(R e_a) = e^{pls} rho(R e_a). Stopping the orbits on
|X| = r gives circle diffeomorphisms b_r with b_r -> Theta and e^{-l t_r(a)} r -> L(a) uniformly, and
r^{-p} rho(r e_{b_r(a)}) = (e^{-l t_r(a)} r)^{-p} rho(R e_a). Hence r^{-p} rho(r e_th) -> A(th) uniformly, with
A(Theta(a)) = L(a)^{-p} rho(R e_a); A is C^1 and |r^{-p} rho(r e_th) - A(th)| <= C r^{p-1}. Points whose forward orbit
stays in |X| < R satisfy rho = 0 (by rho(Phi_s X) = e^s rho(X) and boundedness); they form a closed set of
measure zero (det D Phi_s = e^{2ls}) containing 0.

Step 7 (second derivatives; A in C^{2,alpha}).
7a. Put T = 1/lambda, tau = (1 - e^{-lambda s})/lambda, f(tau,Z) = e^{-s} rho(e^{ls}Z),
u(tau,Z) = e^{-s} W(e^{ls}Z). Changing variables in the once-subtracted kernel formula preserves its subtraction
and contact term, so u is the canonical velocity of f and div u = 0. The profile equation gives
    d_s f = -f + l Z.grad f = -e^{-lambda s} u.grad f, hence d_tau f + u.grad f = 0.
Step 5, extended across bounded sets using rho(0) = W(0) = 0 and local C^1 regularity, gives, for Z != 0,
    |f| + |u| <= C_0 |Z|^p,   |grad f| + |Du| <= C_0 |Z|^{p-1}   (0 <= tau < T).
Fix q > 2. Choose M >= 1 with c := C_0(8M)^p and cT <= M/8; p < 1 permits this choice. Write r = |Z| and
Omega = {M/4 < r < 8M}. All constants below may depend on q,l,C_0,M, the fixed cutoff function below,
the fixed kernel, and ||rho||_{W^{3,q}(Omega)}, but not on tau. Holder constants may also depend on alpha.
Scattering constants may also depend on R, the constants from Steps 3-4, and the local C^2 norm of W on
the compact orbit image of the finite initial time interval used in 7j.

7b. Set b(t) = exp(-1/t) for t > 0 and b(t) = 0 otherwise; h(t) = b(t)/(b(t) + b(1-t)).
Thus h is smooth, nondecreasing, zero for t <= 0 and one for t >= 1. Define
    eta_2 = h(4(r-M/2-c tau)/M) h(4(6M-c tau-r)/M),   chi_2 = eta_2^4,
    eta_3 = h(4(r-5M/4-c tau)/M) h(4(4M-c tau-r)/M),  chi_3 = eta_3^4.
Their supports lie respectively in [M/2+c tau,6M-c tau] and [5M/4+c tau,4M-c tau] in radial coordinates.
Each inner factor has transport derivative 4h'(-c+u_r)/M <= 0; each outer factor has
4h'(-c-u_r)/M <= 0. Thus (d_tau+u.grad)chi_i <= 0. Moreover chi_2 = 1 on M <= r <= 5M, and
chi_3 = 1 on A_0 := {7M/4 < r < 7M/2}. All spatial derivatives through order three are bounded uniformly.
Use fixed cutoffs psi_2 = h(16r/M-6)h(14-2r/M), psi_3 = h(8r/M-8)h(18-4r/M).
Their supports are [3M/8,7M] and [M,9M/2]; their regions of value one are [7M/16,13M/2] and [9M/8,17M/4].
Thus psi_i = 1 near every supp chi_i, with gap at least M/16, and chi_2 = 1 near supp psi_3.
For these fixed cutoffs |(d_tau+u.grad)psi_i| <= Cc/M; no sign is needed because they are not energy weights.

7c. Write T_0 g = p.v. K*g - g e_2/2. The Calderon-Zygmund theorem gives
||T_0 g||_q <= C_q ||g||_q: K is smooth off zero, homogeneous of degree -2 and has zero circular mean.
For a smooth compactly supported chi we also have
    ||[chi,T_0] d_j H||_q <= C_{q,chi} ||H||_q,   [chi,T_0] = chi T_0 - T_0 chi.
Indeed integration by parts gives the distributional kernel, with z = X-Y,
    (chi(X)-chi(Y)) d_j K(z) + K(z) d_j chi(Y).
For |z| < 1 its leading part is sum_k d_k chi(X) d_j(z_k K(z)); its remainder is bounded by
C||D^2 chi||_inf |z|^{-1}, whose integrals in either variable are bounded. The leading kernels have degree -2
and zero circular mean: their integral on an annulus is zero since its two boundary fluxes agree by homogeneity.
Their distributional extensions can include a delta mass. Calderon-Zygmund bounds for truncated kernels and
the bounded delta term control this part. For |z| >= 1 the d_j K terms have an integrable majorant.
The term K(z)d_j chi(Y) is bounded on a fixed bounded X-region by Holder; outside it the bound is
C(1+|X|)^{-2}||H||_q, integrable to power q > 1. These estimates prove the claim, by density for H in L^q.
Here C_{q,chi} depends only on q, a support radius and ||chi||_{C^2}; it is uniform for chi_2,chi_3.

7d. For m = 2,3 and (chi,psi) = (chi_m,psi_m), the canonical formula gives locally
u = T_0(psi f) + H_0, with d^j H_0(Z) = int d^j K(Z-Y)(1-psi(Y))f(Y) dY for j >= 1.
The subtraction disappears only after differentiation. On supp chi these derivatives are uniformly bounded:
on bounded Y-sets the separation is at least M/16 and |f(Y)| <= C_0|Y|^p; for |Y| > 16M their bound is
C int_{16M}^inf t^{p-1-j} dt < inf. The contact term of (1-psi)f vanishes near supp chi.
Commuting derivatives with T_0 and using 7c with H = D^{m-1}(psi f) gives
    ||chi_m D^m u||_q <= C(||chi_m D^m f||_q + ||psi_m f||_{W^{m-1,q}} + 1).
Indeed chi_m D^m(psi_m f) = chi_m D^m f, and the commutator uses only m-1 derivatives of psi_m f.
All norms here and below are spatial norms, with tensors given their Euclidean norm; finite component sums
only change constants. The same decomposition gives u in W^{3,q}_loc for each compact time interval in [0,T).

7e. Here is the required weighted interpolation, including its cutoff dependence. For eta = eta_3, put
B = ||grad v||_{L^inf(Omega)}, a = ||eta^2 D^2 v||_{2q}, b_3 = ||eta^4 D^3 v||_q,
d = ||eta grad eta||_{2q} <= ||grad eta||_inf |supp eta|^{1/(2q)}.
Integration by parts in int eta^{4q}|D^2 v|^{2q}, writing D^2 v = D(grad v), gives
    a^{2q} <= C_q B(a^{2q-2} b_3 + d a^{2q-1}).
For the first term use eta^{4q} = eta^{4q-4}eta^4 and Holder exponents q/(q-1),q; for the cutoff term use
eta^{4q-1}|D^2v|^{2q-1}|D eta| = |eta^2D^2v|^{2q-1}eta|D eta| and exponents 2q/(2q-1),2q.
There is no boundary term since eta is compactly supported in Omega. Dividing by a^{2q-2} and solving the
quadratic (a = 0 is immediate) gives a <= C_q(B^{1/2}b_3^{1/2} + dB), which is the stated inequality.
For v in W^{3,q}_loc with bounded gradient, convolution on a neighborhood of supp eta proves it by passage
to the limit; boundedness of the mollified gradient and Fatou suffice. It applies to both f and u.

7f. Set E_m = 1 + ||chi_m D^m f||_q and U_m = ||chi_m D^m u||_q. For a multi-index beta of length m,
    (d_tau+u.grad)d^beta f = G_beta,
    G_beta = -sum_{0 < nu <= beta} binom(beta,nu) (d^nu u).grad d^{beta-nu}f.
Thus the second-order sources are contractions of Du,D^2f and D^2u,grad f; the third-order sources also
contain D^2u,D^2f and D^3u,grad f. The weighted L^q energy, using div u = 0 and the sign in 7b, gives
    E_2' <= C(E_2+U_2),   E_3' <= C(E_3+U_3+||chi_3(D^2u)(D^2f)||_q).
Precisely, its cutoff term in (1/q)d_tau int chi_m^q |D^m f|^q is
int chi_m^{q-1}(d_tau+u.grad)chi_m |D^m f|^q <= 0; there are no other cutoff-transport terms.
By 7a, ||psi_2 f||_{W^{1,q}} <= C; hence 7d gives U_2 <= CE_2 and Gronwall bounds E_2 uniformly.
Since chi_2 = 1 near supp psi_3, this bounds ||psi_3 f||_{W^{2,q}}; therefore U_3 <= CE_3.
The gradients of f,u are bounded on Omega, so 7e and Holder give
    ||chi_3(D^2u)(D^2f)||_q <= ||eta_3^2D^2u||_{2q} ||eta_3^2D^2f||_{2q}
      <= C(U_3^{1/2}+1)((E_3-1)^{1/2}+1) <= CE_3.
Consequently E_3' <= CE_3. Both initial energies are finite since f(0) = rho is C^3 on the bounded annulus.

7g. These are integrated energy inequalities; their justification requires no fourth derivative of f or
classical third derivative of u. Fix t_0 < T, U = {7M/16 < r < 25M/4}, U_+ = {3M/8 < r < 13M/2}.
Both energy supports lie in U, its closure lies in U_+, and the closure of U_+ lies in Omega. On [0,t_0],
f is continuous into W^{3,q}(U_+), u is continuous into C^1 and locally bounded in W^{3,q}, and every
G_beta is in L^1([0,t_0];L^q(U_+)). For the W^{3,q} assertion use psi_0 = h(16r/M-4)h(16-2r/M):
its support is [M/4,8M], it is one on [5M/16,15M/2], and |(d_tau+u.grad)psi_0| <= Cc/M.
The decomposition in 7d and the L^q bound for T_0 D^3(psi_0 f) apply on U_+; rho in C^3 and 9.1
supply all the other compact-time bounds, including bounded D^2u. No uniform third derivative is assumed.
The differentiated equations hold in distributions by the product rule, justified by local convolution.
Let zeta be b(1-|Z|^2) divided by its integral and zeta_eps(Z) = eps^{-2}zeta(Z/eps).
Its support is |Z| <= eps; put C_zeta = int |Z||grad zeta(Z)| dZ. Take eps < M/64, so U-Y lies in U_+
for |Y| <= eps. For h_m = D^m f, convolve its equation spatially. The commutator is
    R_eps(X) = int (u(X)-u(X-Y)).grad zeta_eps(Y) [h_m(X-Y)-h_m(X)] dY.
The omitted constant h_m(X) has integral zero, exactly because div u = 0. Minkowski gives
    ||R_eps||_{L^q(U)} <= C_zeta ||Du||_{L^inf(U_+)}
      sup_{|Y|<=eps} ||h_m(.-Y)-h_m||_{L^q(U)} -> 0.
Translation continuity and domination by the finite W^{3,q} bounds on U_+ give convergence in L^1 time.
The mollified sources also converge in L^1 L^q.
Apply the smooth spatial energy calculation with chi_m to this equation and pass to the limit; regularizing
the norm at zero gives the integrated inequalities in 7f. On [0,t_0] time regularity follows from the
mollified equation itself. Gronwall's constants are independent of t_0, so sup_{tau<T}(E_2+E_3) < inf.

7h. Since chi_2 = chi_3 = 1 on A_0, we have sup_{tau<T} ||f(tau)||_{W^{3,q}(A_0)} < inf.
This is a bounded smooth planar annulus. Weak compactness in W^{3,q} and the uniform limit from Step 6
identify every subsequential weak limit at T as f_T(Z) = |Z|^p A(arg Z). Morrey embedding
W^{3,q}(A_0) -> C^{2,1-2/q}(closure A_0) has a constant depending only on q,A_0.
Restriction to |Z| = 2M gives A in C^{2,alpha} for every 0 < alpha < 1, by taking q large enough.
The same uniform embedding before T, with s = l^{-1}log(r/(2M)) for r >= 2M, gives
    |D^2 rho(X)| <= C r^{p-2},   [D^2 rho]_{C^alpha(B(X,r/32))} <= C_alpha r^{p-2-alpha},   |X| = r.
Indeed e^{-ls}B(X,r/32) lies inside A_0, D^2 f = e^{(2l-1)s}D^2 rho, and a Holder quotient adds
e^{alpha ls}. For a prescribed alpha choose q with 1-2/q >= alpha; constants remain independent of r.

7i. Fix large r = |X| and a = r/64. Take the fixed local cutoff xi(Y) = h(2-|Y-X|/a), equal to one
on B(X,a), with support {Y : |Y-X| <= 2a}, and |D^j xi| <= C_j r^{-j}. Freeze X and r when differentiating
the velocity in its evaluation variable. Transfer two derivatives onto xi rho in the local convolution.
Leibniz gives g = D^2(xi rho) = xi D^2 rho + D xi (x) D rho + D rho (x) D xi + rho D^2 xi,
so |g| <= Cr^{p-2} by Step 5 and 7h. On B(X,a), g = D^2 rho and its Holder seminorm
is <= C_alpha r^{p-2-alpha}. Circular cancellation of K gives the local bound
    |int_{|Y-X|<a} K(X-Y)(g(Y)-g(X)) dY|
      <= C_alpha r^{p-2-alpha} int_0^a t^{alpha-1} dt <= C_alpha r^{p-2}.
The transition a <= |Y-X| <= 2a costs Cr^{p-2} int_a^{2a} dt/t. The contact term is -D^2 rho(X)e_2/2.
In the remaining once-subtracted integral differentiate K twice; the subtraction has derivative zero.
For |Y| <= 2r, |X-Y| >= a on its integrand's support, giving Cr^{-4} int_{|Y|<=2r}|Y|^p dY.
For |Y| > 2r the bound is C int_{2r}^inf t^{p-3} dt. Both are Cr^{p-2}; thus |D^2 W(X)| <= Cr^{p-2}.

7j. The C^2 finite-time flow of 9.1 gives Q_s := d_a^2 F_s and
    d_s Q_s = DW(X_a(s)) Q_s + e^{ls} D^2W(X_a(s))[d_a F_s,d_a F_s],   Q_0 = -R e_a.
Steps 3-5 give c_R e^{ls} <= |X_a(s)| <= b_R e^{ls} and bounded d_a F_s. Hence both the coefficient
DW(X_a(s)) and the forcing above are bounded by C_R e^{-lambda s} for large s; the initial compact
time interval is bounded by local C^2 regularity. Gronwall bounds Q_s uniformly in a,s, and integration gives
sup_a |Q_t-Q_s| <= C_R e^{-lambda s} for t >= s sufficiently large. Thus Q_s has a uniform continuous limit.
The identity d_a F_s(b)-d_a F_s(a) = int_a^b Q_s(v) dv passes to the limit using Step 4, proving F in C^2.
Since |F| = L >= c_R > 0, taking norm and local angle (with the lift of Step 3) gives L,Theta in C^2.

### 9.3 Theorem 3.16 (forced far-field correction)
Hypotheses: rho in S is a profile, l > 1, p = 1/l. Used: |rho(X)| <= C|X|^p on R^2 (Theorem A and rho = O(|X|^2) at
0), |W(X)| <= C|X|^p (1 + log|X|) for |X| >= 2, |grad rho(X)| <= C(1 + |X|)^{gamma-1} with gamma < 1, and
r^{-p} rho(r e_th) -> A(th) uniformly with A Holder of some exponent alpha in (0, 1) (Theorem A; by Section 9.2, A is
in fact C^{2,alpha}). F := r^p A(th), and B[g] denotes the canonical once-subtracted velocity of a density g.

Step 1 (the homogeneous velocity and div(F H)). With lambda = p + 1, the angular equation is a first-order system for
(Psi, Q), Q = Psi' - sin th A, with constant matrix of monodromy e^{2 pi B}, eigenvalues e^{+-2 pi i lambda} != 1; so
the periodic solution is unique, Psi in C^{1,alpha}. The kernel integral B[F](X) converges for X != 0 (cancellation
near Y = X by the zero angular mean of K and the Holder modulus of F; |K(-Y) F(Y)| <= C|Y|^{p-2} near 0;
|K(X - Y) - K(-Y)| <= C|X||Y|^{-3} at infinity), is continuous away from 0 and homogeneous of degree p. Truncating F
by cutoffs chi_L and passing to the limit (tail error C M L^{p-1} on |X| <= M) gives div B[F] = 0 and
curl B[F] = -d_x F in distributions; writing B[F] = r^p(b_r e_r + b_th e_th), the divergence gives
(p + 1) b_r + b_th' = 0 and the curl gives the angular equation for b_th/(p + 1). By uniqueness B[F] = H. Integrating
by parts in r and differentiating in th in distributions,
    <div(F H), phi> = int_0^inf r^{2p} < (p + 1)(Psi A)' - (2p + 1) Psi' A, phi(r, .) > dr,
that is div(F H) = r^{2p-1} J_p[A] on R^2 minus 0, without differentiating A.

Step 2 (the rescaled density and a rate). Put f_t(X) = e^{-pt} rho(e^t X) and w_t(X) = e^{-pt} W(e^t X). The profile
equation gives Z.grad rho(Z) = p rho(Z) - p W(Z).grad rho(Z), and with div w_t = 0
    d_t f_t = -p e^{-(1-p)t} div(f_t w_t).
On a fixed annulus a <= |X| <= b, |d_t f_t| <= C e^{(gamma-1)t}(1 + t), so with R = e^t
    (9.3.1)  ||f_R - F||_{L^inf(a <= |X| <= b)} <= C R^{gamma-1}(1 + log R),   ||grad f_R||_{L^inf} <= C R^{gamma-p}.

Step 3 (uniform convergence of the velocity). By homogeneity of K, w_R = B[f_R], so with G_R = f_R - F,
w_R - H = p.v. int [K(X - Y) - K(-Y)] G_R(Y) dY - G_R(X) e_2/2. On a <= |X| <= b split the integral (eps and L are
chosen first, then R is taken large; Step 2 is applied on the annulus 3a/4 <= |Y| <= b + a/4): |Y| < eps
(at most C(eps^p + eps^{p+2}), since |G_R(Y)| <= C|Y|^p uniformly in R); |Y| > L (at most C L^{p-1}); the ball
|Y - X| < eta = a/4, where for 0 < s < eta the gradient bound and the Holder modulus of F give
|int_{|Z| < s} K(Z)(G_R(X - Z) - G_R(X)) dZ| <= C(R^{gamma-p} s + s^alpha) and (9.3.1) gives
|int_{s < |Z| < eta} ...| <= C R^{gamma-1}(1 + log R) log(eta/s); with s = R^{-m}, m > max(gamma - p, 0), both tend to
0; the remaining bounded region tends to 0 by uniform convergence of G_R. Hence w_R -> H uniformly on compact annuli,
W = H + o(r^p) uniformly in angle, and |W(X)| <= C|X|^p for large |X|. The argument uses the rate
(9.3.1) and the gradient bound, not only the uniform convergence f_R -> F.

Step 4 (the distributional correction). For phi in C_c^inf(R^2 minus 0), d_t := <div(f_t w_t),
phi> -> d_inf := <div(F H), phi> and d_t is bounded (both by Step 3). Integrating Step 2,
    <f_t - F, phi> = p int_t^inf e^{-(1-p)s} d_s ds,
    e^{(1-p)t} <f_t - F, phi> = p int_0^inf e^{-(1-p)u} d_{t+u} du -> (p/(1 - p)) d_inf = d_inf/(l - 1),
by dominated convergence. Since e^{(1-p)t}(f_t - F) = R^{1-2p}[rho(R .) - R^p F], this is (a).

Step 5 (a positive quadratic zero forces J != 0). Let A be C^1 near beta, A(beta) = A'(beta) = 0, a := A''(beta)/2 > 0
(only the existence of A''(beta) is used: A'(beta + t) = 2a t + o(t) and A(beta + t) = a t^2 + o(t^2)), and suppose
J = 0 on a one-sided interval I adjacent to beta on which A > 0. There J = (p + 1) Psi A' - p Psi' A
pointwise, so (Psi A^{-kappa})' = 0 with kappa = (p + 1)/p > 2, Psi = C A^kappa = O(|t|^{2 kappa}) = o(t^4)
(t = th - beta), and Psi(beta) = Psi'(beta) = 0. The angular equation has continuous right side
q(t) = sin(beta + t) A'(beta + t) - p cos(beta + t) A(beta + t) near beta, so Psi is C^2 there and
    Psi(beta + t) = int_0^t sin(lambda(t - s)) q(s) ds / lambda.
If sin beta != 0, q = 2a sin beta t + o(t) and Psi = (a sin beta/3) t^3 + o(t^3); if sin beta = 0, q = a(2 - p)
cos beta t^2 + o(t^2) and Psi = (a(2 - p) cos beta/12) t^4 + o(t^4). Both contradict Psi = o(t^4) on I. Hence J is not
identically zero on any one-sided neighbourhood of beta; since J is continuous near beta, J_p[A] != 0 as a
distribution; this is (b).

Step 6 (lower bounds). With E = rho - F, choose phi = chi(r) eta(th), chi >= 0 in C_c^inf((1, 2)), with
<J, eta> != 0. By (a), |<R^{1-2p} E(R .), phi>| >= c_0 for R >= R_0. Holder's inequality (q' = inf for q = 1) and the
change of variables Y = RX give int_{R < |X| < 2R} |E|^q dX >= c_q R^{2 + q(2p-1)}; q = 2 is the R^{4p} bound. Summing
over dyadic annuli, E is not in L^q(r > 1) when 2 + q(2p - 1) >= 0 (q <= 2/(1 - 2p) for p < 1/2, endpoint included;
every finite q >= 1 for p >= 1/2); each dyadic annulus contributes at least c 2^{-4p} to int_{r>1} r^{-4p} |E|^2 dX,
which is therefore infinite; and E = o(r^{2p-1}) uniformly would give <R^{1-2p} E(R .), phi> -> 0. This is (c).

Step 7 (the scattering map and the expansion). For |X| = R >= R_2 the forward orbit satisfies r' >= l r/2 and
r(tau) <= C_0 R e^{l tau}; with Z_tau = e^{-l tau} Phi_tau(X),
    S(X) := lim Z_tau = X + int_0^inf e^{-ls} W(Phi_s X) ds,   |S(X) - X| <= C_1 R^p.
Since W = H + o(r^p) uniformly, H(Phi_s X) = e^s H(Z_s) (homogeneity, p l = 1) and H is uniformly continuous on
1/2 <= |Y| <= 2, S(X) = X + H(X)/(l - 1) + o(R^p) uniformly in angle. Along the forward orbit
rho(X) = e^{-tau} rho(Phi_tau X) = F(Z_tau) + O(|Z_tau|^p sup_th |s^{-p} rho(s e_th) - A(th)|) with s = |Phi_tau
X| -> inf, so rho = F o S on |X| >= R_2 (no hypothesis on backward orbits). If A is C^1, grad F = r^{p-1}(p A e_r + A'
e_th) is uniformly continuous on 1/2 <= |Y| <= 2, and the first-order Taylor formula with |S(X) - X| <= C_1 R^p gives
F(S(X)) = F(X) + grad F(X).H(X)/(l - 1) + o(R^{2p-1}) uniformly, with grad F.H = r^{2p-1}((p + 1) Psi A' - p Psi'
A) = r^{2p-1} J. The annular limit follows from uniform convergence of R^{1-2p} E(R .) on 1 <= |X| <= 2 and
int_1^2 r^{4p-1} dr = (2^{4p} - 1)/(4p). This is (d). For every profile in S, A is C^1 (Section 9.2, Step 6), so the
hypothesis "A in C^1" of (b) and (d) holds automatically; (b) also needs a zero with A''(beta) > 0; without it,
Proposition 3.18(c) (Section 9.24, Step 7) shows that J_p[A] is not identically zero for every profile in S.

### 9.4 Theorems 3.2, 3.13 and 3.3 (profiles in S^+)
Hypotheses: rho in S^+, l = c_l > 1, p = 1/l, lambda := l - 1, b = 2l - 1/2. Used: Section 9.1 (V in C^{2,alpha}_loc,
the complete C^2 flow, B(0) = R^2, xi in C^2 with D xi(0) = (1, 0), D xi != 0, xi(Phi_t X) = e^{t/2} xi(X),
xi = x + O(|X|^2) near 0, rho = xi^2, Gamma = xi^{-1}(0) a C^2 line with |Phi_{-t} X| = O(e^{-bt}) on Gamma,
D^2 rho = 2 D xi (x) D xi on Gamma, the backward invariant ball B_delta and (9.1)); Theorem 3.1 with Section 9.2 (R
with V.X >= l|X|^2/2 for |X| >= R, L, Theta, A(Theta(a)) = L(a)^{-p} rho(R e_a), and |W| <= C|X|^p, |DW| <= C|X|^{p-1}
for large |X|). J(x, y) = (-y, x), e_a = (cos a, sin a).

Step 1 (compact attraction, escape, global chart). The open sets Phi_n(B_delta) increase (B_delta is backward
invariant) and cover R^2, so a compact K lies in one of them, Phi_{-T_K} K is in B_delta, and by (9.1)
    (9.4.1)  sup_{X in K} |Phi_{-t} X| <= C_K e^{-t/2}   (t >= T_K).
If X != 0 had a bounded forward orbit with closure K, then |X| = |Phi_{-t}(Phi_t X)| <= C_K e^{-t/2} for all t >= T_K,
so X = 0. Hence every nonzero forward orbit is unbounded; on |X| >= R, r' = V_r >= l r/2 > 0, so an orbit that reaches
|X| = R never returns inside and escapes. Every nonzero orbit therefore crosses each circle |X| = r_0 >= R exactly
once, transversally, and P(a, s) := Phi_s(R e_a) is a C^2 bijection of S^1 x R onto R^2 minus 0. Its partial
derivatives are D Phi_s(R e_a) applied to R J e_a and to V(R e_a), and det(V(R e_a), R J e_a) = R V_r(R e_a) > 0, so P
is a local, hence a global, C^2 diffeomorphism.

Step 2 (Theorem 3.2). rho = xi^2 >= 0 and {rho = 0} = Gamma. V is tangent to Gamma (V.grad xi = xi/2 = 0 there) and
nonzero on Gamma minus 0, so the orbits in a component of Gamma minus 0 are relatively open in it; the component is
connected, hence a single orbit, which by Step 1 crosses every circle |X| = r_0 >= R once and transversally. Let
R e_{a_1}, R e_{a_2} be the crossing points with |X| = R (one per component, distinct) and q(a) := xi(R e_a), a C^2
function with exactly the zeros a_1, a_2. Then q'(a_j) = D xi(R e_{a_j}).R J e_{a_j} != 0: the kernel of D xi there is
the tangent of Gamma, spanned by V, and V_r > 0 makes V not parallel to J e_{a_j}. By Theorem 3.1,
A(Theta(a)) = L(a)^{-p} q(a)^2, so A >= 0 with exactly the zeros theta_j := Theta(a_j), A'(theta_j) = 0 and
    A''(theta_j) = 2 L(a_j)^{-p} q'(a_j)^2 / Theta'(a_j)^2 > 0.
The signed root B(Theta(a)) := L(a)^{-p/2} q(a) is C^2 on the circle, B^2 = A, and
B'(theta_j) = L(a_j)^{-p/2} q'(a_j)/Theta'(a_j) != 0, so B changes sign at both zeros.

Step 3 (the limit S). By Theorem 3.1 and local boundedness |W(X)| <= C(1 + |X|)^p on R^2. For u(t) = 1 + |Phi_t X|,
u' <= l u + C u^p, so d/dt u^{1-p} <= lambda u^{1-p} + (1 - p) C; since (1 - p)/lambda = p and lambda/(1 - p) = l,
    1 + |Phi_t X| <= C_0 (1 + |X|) e^{lt}   (t >= 0).
Then S_t(X) := e^{-lt} Phi_t X = X + int_0^t e^{-ls} W(Phi_s X) ds, and the integrand is at most C_1 (1 + |X|)^p
e^{-lambda s} (l p = 1). Hence S := lim S_t exists uniformly on compact sets, S is continuous, S(0) = 0,
    |S(X) - X| + |S_t(X) - X| <= C_2 (1 + |X|)^p,   |S(X) - S_t(X)| <= C_2 (1 + |X|)^p e^{-lambda t},
and S(Phi_tau X) = e^{l tau} S(X) for every real tau. In particular S(X) = X + O(|X|^p), with no logarithm.

Step 4 (homeomorphism; C^2 off 0; not Lipschitz at 0). By Theorem 3.1 and Step 3, S(P(a, s)) = e^{ls} L(a)
e_{Theta(a)}, and the right side is a C^2 diffeomorphism of S^1 x R onto R^2 minus 0 (inverse a = Theta^{-1}(arg Y),
s = l^{-1} log(|Y|/L(a))); with Step 1, S is a C^2 diffeomorphism of R^2 minus 0 onto itself. If Y_n -> 0, Y_n != 0,
then s_n -> -inf (L has a positive minimum) and, by (9.4.1) on the circle |X| = R,
|S^{-1}(Y_n)| = |Phi_{s_n}(R e_{a_n})| <= C e^{s_n/2} -> 0; so S is a homeomorphism of R^2 fixing 0. For large
r = |X|, Step 3 gives |Phi_t X| >= (r/2) e^{lt}, hence |DW(Phi_t X)| <= C r^{p-1} e^{-lambda t}; Q_t := DS_t solves
d_t Q_t = DW(Phi_t X) Q_t, Q_0 = I, so ||Q_t - I|| <= exp(C r^{p-1}) - 1, Q_t converges uniformly on compact subsets
of the exterior, and DS(X) = I + O(|X|^{p-1}). At 0: for P in Gamma minus 0, |Phi_{-t} P| <= C_P e^{-bt} while
|S(Phi_{-t} P)| = e^{-lt}|S(P)|, so |S(Z)|/|Z| >= c_P e^{(l - 1/2)t} along Z = Phi_{-t} P -> 0, and S is not Lipschitz
(in particular not differentiable) at 0.

Step 5 (measure). det D Phi_t = e^{2lt} (div V = 2l), so det DS_t = 1 and int f(S_t X) dX = int f dY for f in
C_c(R^2). If supp f lies in |Y| <= M and f(S_t X) != 0, then |X| <= M + C_2 (1 + |X|)^p, which (p < 1) confines X to
a ball independent of t; the same holds for S. Dominated convergence gives int f(S X) dX = int f dY. The Borel measure
E -> |S^{-1}(E)| is locally finite (S^{-1} is continuous) and has the same integrals of C_c functions as Lebesgue
measure, hence agrees with it on open sets and, by regularity, on Borel sets; applied to S(E) (S is a homeomorphism)
this gives |S(E)| = |E| for Borel E, and completeness extends both statements to Lebesgue measurable sets. No
convergence of DS_t at 0 is used.

Step 6 (formulas and leaves). For X = P(a, s), rho(X) = e^s q(a)^2 and xi(X) = e^{s/2} q(a); with Steps 2 and 4 and
l p = 1,
    rho = |S|^p A(arg S),   xi = |S|^{p/2} B(arg S)   (both sides 0 where S = 0),
and B is the only continuous signed root with the second property (evaluate at S(R e_a) = L(a) e_{Theta(a)}). For
c != 0 let I_c be the open arc between theta_1 and theta_2 on which B has the sign of c. S maps {xi = c} onto
{(c/B(th))^{2/p} e_th : th in I_c}, a proper embedded line whose radius tends to infinity at both ends of I_c; so
{xi = c} is one proper C^2 line (D xi != 0), and since S(X) - X = O(|X|^p) its ends go to infinity in the directions
theta_1 and theta_2. Rates: by (9.4.1) and the backward equation y' = -b y + O(e^{-t}) near 0, y(Phi_{-t}
X) = O(e^{-t}) (b > 1), and xi = x + O(|X|^2) gives e^{t/2} Phi_{-t} X -> (xi(X), 0); so |Phi_{-t} X - Phi_{-t} Y| ~
|xi(X) - xi(Y)| e^{-t/2} when xi(X) != xi(Y). If xi(X) = xi(Y) and X != Y, use the C^2 chart (u, v) = (xi, y) near 0,
with inverse x = chi(u, v), chi_v(0, 0) = 0: the backward flow is u' = -u/2, v' = -g(u, v) with g(0, 0) = 0 and
Dg(0, 0) = (0, b), both orbits have the same u(t), and delta := v_X - v_Y satisfies delta' = -(b + eps(t)) delta with
|eps(t)| <= C e^{-t/2} and delta(T) != 0; so e^{bt} delta(t) -> d_XY != 0 and e^{bt}(Phi_{-t} X - Phi_{-t}
Y) -> d_XY e_2. Hence for every eta in (1/2, b), {Y : |Phi_{-t} Y - Phi_{-t} X| = O(e^{-eta t})} = {xi = xi(X)}: the
level sets of xi are the strong unstable leaves of the basin of 0, permuted by the flow (Phi_s
{xi = c} = {xi = e^{s/2} c}); only {xi = 0} = Gamma contains 0, and it is the strong unstable manifold of 0.

Step 7 (Theorem 3.3). Let rho(-x, y) = rho(x, y) and R(x, y) = (-x, y). K(RZ) = R K(Z), R e_2 = e_2, and the change of
variables Y -> RY respects the principal value and the once-subtracted integral (the kernel difference is O(|Y|^{-3})
against |rho| <= C(1 + |Y|)^gamma), so W(RX) = R W(X), Phi_t R = R Phi_t, S R = R S and xi(-x, y) = -xi(x, y) (from
xi = lim_{t -> inf} e^{t/2} x(Phi_{-t} X), Section 9.1). Thus the y-axis lies in Gamma; near 0, Gamma is a graph
x = g(y) that contains the nearby axis, so g = 0; every point of Gamma enters this neighbourhood under the backward
flow and the axis is invariant, so Gamma = {x = 0}, rho > 0 for x != 0, xi > 0 on {x > 0}, xi_x(0, y) > 0 and
h(y) := rho_xx(0, y) = 2 xi_x(0, y)^2 > 0. The function b(y) := V_2(0, y) = l y + w(y) is C^2 with b(0) = 0 and
b'(0) = 2l - 1/2, and has no other zero (V_1(0, y) = 0 and V^{-1}(0) = {0}).
Differentiating V.grad rho = rho twice in x and evaluating on the axis (where V_1 = rho = rho_x = rho_y = rho_xy = 0
and V_{1x} = 2l - b') gives b h' = (1 - 4l + 2b') h on all of R, without division by b. With w = O(|y|^p),
w' = O(|y|^{p-1}) (Theorem 3.1) and l(p - 2) = 1 - 2l, on both tails
    d/dy log(h |y|^{2-p}) = (2 y w' - (p - 2) w) / (y (l y + w)) = O(|y|^{p-2}),
which is integrable, so h ~ H_+- |y|^{p-2} with H_+- > 0 (relative error O(|y|^{p-1})). Hence h is in L^1,
b h = O(|y|^{p-1}) -> 0, h w' = O(|y|^{2p-3}) is in L^1, and integrating (b h)' = (1 - l + 3 w') h over R gives
int h w' dy = ((l - 1)/3) int h dy > 0. Two-sided bound: the zeros of A are pi/2 and 3pi/2 (the scattering directions
of the two axis branches) and are quadratic (Step 2), so A(th)/cos^2 th extends to a continuous positive function and
m_A cos^2 <= A <= M_A cos^2; by Step 6, m_A S_1^2 |S|^{p-2} <= rho <= M_A S_1^2 |S|^{p-2}. For large r = |X|, |S| lies
between r/2 and 2r; if |y| >= r/2, S_1(0, y) = 0 and |d_x S_1(tx, y) - 1| <= C|y|^{p-1} <= 1/2 (Step 4) give
|x|/2 <= |S_1(x, y)| <= 3|x|/2; if |y| < r/2, then |x| > (3^{1/2}/2) r and |S_1(X) - x| <= C r^p <= |x|/2 give the
same.
On the remaining disk xi = x d(x, y) with d = int_0^1 xi_x(tx, y) dt continuous and positive, and rho = x^2 d^2. Hence
C_1 x^2 (1 + |X|)^{p-2} <= rho <= C_2 x^2 (1 + |X|)^{p-2} on R^2. Finally W_1 = V_1 = 0 on the invariant axis, so the
restriction to x > 0 is a half-plane profile with an impermeable vertical wall on which rho = 0.

### 9.5 Lemma 3.7, Theorem 3.8 and Proposition 3.9 (zeros of V other than 0)
Hypotheses: rho in S is a profile, l = c_l > 1; V may vanish away from 0; for Theorem 3.8 (Steps 3-7) every zero of V
is nondegenerate (det DV != 0). Used: Section 9.1 (V in C^{2,alpha}_loc, the
complete C^2 flow, xi in C^2 on B(0) with rho = xi^2 there, D xi != 0, Gamma = xi^{-1}(0) a C^2 line whose two
components minus 0 are complete orbits); Section 9.2 (R with V.X >= l|X|^2/2 for |X| >= R, so all zeros of V lie in
|X| < R, and an orbit reaching |X| >= R escapes). B(Z) = {X : Phi_{-t} X -> Z as t -> inf} for a source Z; W^s, W^u
are the forward and backward convergence sets of a saddle (equilibrium included); a branch is a complete nonstationary
orbit. From V.grad rho = rho and div V = 2l: rho(Phi_t X) = e^t rho(X) and |Phi_t(E)| = e^{2lt}|E| (Liouville).
Classical inputs: the C^2 stable and unstable manifold theorem at a hyperbolic zero (local C^2 graphs tangent to the
eigenspaces; a semiorbit staying near the zero lies on the corresponding local graph), and the generalized
Poincare-Bendixson theorem for C^1 planar fields (an omega-limit set of a bounded semiorbit containing finitely many
zeros is a zero, a periodic orbit, or zeros together with orbits whose alpha- and omega-limits are zeros in the set;
no cycle structure is assumed).

Step 1 (Lemma 3.7). At V(Z) = 0 the equation gives rho(Z) = 0; differentiating once, M^T g = g with M = DV(Z),
g = grad rho(Z); curl V = -rho_x gives M_21 - M_12 = -rho_x(Z); tr M = 2l. If 1 is not an eigenvalue, g = 0 and M is
symmetric; if 1 is an eigenvalue, the other is 2l - 1 > 1. Either way M is real diagonalizable (no focus, no Jordan
node). If det M != 0, the eigenvalues are real, nonzero, with positive sum: a source node or a saddle; a source has
eigenvalues 0 < a <= b with b >= l > 1; a repeated eigenvalue forces M = l I.

Step 2 (source estimates; no gap condition). At a source Z with eigenvalues 0 < a <= b write X = Z + Pz,
P^{-1}V = Az + N(z), A = diag(a, b), N(0) = DN(0) = 0, |D^2 N| <= M_N on |z| < delta, M_N delta <= a/2. The backward
orbit z(t) solves z' = -Az - N(z); |z|^2/2 has derivative <= -a|z|^2/2, so the ball is backward invariant and
|z(t)| <= |z_0| e^{-at/2}; then d/dt log|z| <= -a + M_N|z|/2 integrates to |z(t)| <= C_0 e^{-at}|z_0|. The first and
second variational equations give ||D_{z_0} z(t)|| <= C_1 e^{-at} and ||D^2_{z_0} z(t)|| <= (M_N C_1^3/a) e^{-at}.
B(Z) is the increasing union of the open connected sets Phi_n(E_Z), E_Z the ball; so B(Z) is open, connected,
invariant, every compact subset lies in one Phi_n(E_Z), and |Phi_{-t} X - Z| <= C_X e^{-at} for large t.

Step 3 (Theorem 3.8(a)). Zeros are isolated (det DV != 0) and lie in the closed disk |X| <= R, so they are finite.
An invariant Jordan curve C is impossible: Phi_t maps the bounded component D onto itself, while |Phi_t
D| = e^{2lt}|D| with 0 < |D| < inf. A periodic orbit is such a curve. A cycle of saddle connections (homoclinic loops
included) contains one: connections are injective orbits with disjoint interiors, adjoining their endpoints gives
simple arcs, and removing repeated vertices from a directed cycle leaves a Jordan curve that is a union of invariant
sets. Index count: on |X| = L >= R the homotopy (1 - s)V + sX is nonzero, so the winding number of V is 1; it is the
sum of the indices at the zeros (Stokes for the angular form on the disk minus small disks), +1 at a source and -1 at
a saddle (sign of det DV). Hence #sources = #saddles + 1; there are no sinks by Step 1.

Step 4 (Theorem 3.8(b)). Let F = V or -V and let a bounded nonstationary forward F-semiorbit have omega-limit set K
(nonempty, compact, connected, invariant). A sink of F in K attracts the semiorbit, so K is that point. A source Q of
F is not in K: near Q, d|z|^2/dt >= c|z|^2 in diagonal coordinates, so orbits leave a small ball and cannot re-enter.
If K is not a single point, then by Poincare-Bendixson and Step 3 it consists of saddles and connections. Every
saddle Q in K has an outgoing connection in K: take a small closed ball N about Q with a point of K outside it, times
a_n -> inf with Psi_{a_n} X -> Q, and first exit times b_n > a_n from N; Gronwall gives
b_n - a_n >= L_Q^{-1} log(delta_Q/|Psi_{a_n} X - Q|) -> inf, a limit point Y of Psi_{b_n} X lies in K on the boundary
of N and has its whole backward semiorbit in N, so Y is on W^u(Q), and its forward limit is a saddle in K. Following
one outgoing connection from each saddle of K gives a directed cycle, excluded by Step 3. So K is one zero and the
semiorbit converges to it. Backward orbits are bounded (|Phi_{-t} X| <= max(|X|, R)), so every backward orbit
converges to one zero: R^2 is the disjoint union of the source basins and the saddle unstable manifolds. A
nonstationary forward orbit either reaches |X| >= R and escapes, or is bounded and converges to a zero, which is not a
source (the argument above with F = V) and not a sink (Step 1): it is a saddle. Each basin is open, invariant and
nonempty; if its area were finite, |B| = |Phi_s B| = e^{2ls}|B| would fail, so it has infinite area and is unbounded.

Step 5 (Theorem 3.8(c)). Let S be a saddle with eigenvalues mu < 0 < nu, nu = 2l - mu > 2. On W^s(S),
rho(X) = e^{-t} rho(Phi_t X) -> 0. On W^u(S) minus S, the backward orbit lies eventually on the local C^2 unstable
graph, where dv/dt = -nu v + O(v^2), so |Phi_{-t} X - S| <= C_X e^{-(nu - eps)t} with eps < nu - 1; as rho(S) = 0 and
rho is locally Lipschitz, |rho(X)| = e^t |rho(Phi_{-t} X)| <= C_X e^{(1 - nu + eps)t} -> 0. (The rate nu > 1 is
needed.)

Step 6 (Theorem 3.8(d)). At a source Z with 0 < a <= b (a + b = 2l, b > 1) put f(z) = rho(Z + Pz), so
(Az + N(z)).Df = f. If the Taylor terms of degree < k vanish (k <= 3), the homogeneous degree-k part P_k satisfies
(Az).DP_k = P_k (substitute z = r zeta, divide by r^k, let r -> 0; only N = O(|z|^2) is used), i.e.
(ia + jb - 1)c_ij = 0 for the coefficient of z_1^i z_2^j. Since b > 1, a monomial with j >= 1 is never resonant; the
only resonances of degrees 1, 2, 3 are a = 1, 1/2, 1/3. If a > 1/3 and a is not 1/2 or 1, D^j rho(Z) = 0 for j <= 3,
so |rho(Z + H)| <= omega(|H|)|H|^3 with omega(r) -> 0, and for X in B(Z), by Step 2,
|rho(X)| = e^t |rho(Phi_{-t} X)| <= C_X^3 omega(C_X e^{-at}) e^{(1 - 3a)t} -> 0: the basin is dead. For a < 1/3 the
jets through order 3 still vanish but the bound does not decay; at a = 1, 1/2, 1/3 a jet of degree 1, 2, 3 in the weak
direction is allowed by the transport equation.

Step 7 (Theorem 3.8(e), near-field part). If a saddle stable branch C has backward limit 0, then C is in B(0) and
rho = 0 on C (Step 5), so xi = 0 on C and C is in Gamma; C and the components of Gamma minus 0 are complete orbits, so
C is one of them. If every extra source is as in Step 6, then rho = xi^2 on B(0) (Section 9.1), rho = 0 on the other
basins (Step 6) and on the saddle unstable manifolds (Step 5), and by Step 4 these sets cover R^2; so rho = xi^2
1_{B(0)} >= 0. (The last clause of (e), on the zero set of A, is proved in Section 9.6, Step 9.)

Step 8 (Proposition 3.9: the weak coordinate). Let 0 < alpha <= 1 < beta' be the eigenvalues at Z, e* a left
alpha-eigenvector, and choose P with first coordinate z_1 = e*(X - Z) (second column a beta'-eigenvector). In the ball
of Step 2, eta_t(z_0) := e^{alpha t} z_1(t, z_0) = z_{0,1} - int_0^t G_s ds with G_s = e^{alpha s} N_1(z(s, z_0)), and
by Step 2 |G_s| <= C|z_0|^2 e^{-alpha s}, |DG_s| <= C|z_0| e^{-alpha s}, |D^2 G_s| <= C e^{-alpha s}. So eta_t
converges in C^2 of the ball to eta_loc, at rate e^{-alpha t}, with eta_loc = z_1 + O(|z|^2); no gap or nonresonance
condition enters (a slow resonance would need i alpha + j beta' = alpha with i + j >= 2, impossible). For X in B(Z)
and Phi_{-T} X in the ball, eta(X) = e^{alpha T} eta_loc(P^{-1}(Phi_{-T} X - Z)) is the limit
lim e^{alpha t} e*(Phi_{-t} X - Z), independent of T, C^2 on B(Z), eta(Phi_s X) = e^{alpha s} eta(X),
V.grad eta = alpha eta, D eta(Z) = e*, and D eta != 0 everywhere (D eta(X) = e^{alpha T} D eta(Y) D Phi_{-T}(X)).

Step 9 (Proposition 3.9: no dependence on the fast coordinate). The C^2 chart (u, v) = (eta_loc(z), z_2) turns the
field into alpha u d_u + B(u, v) d_v with B in C^2, B(0) = 0, B_v(0) = beta'. Fix 1 < c < beta', shrink to a backward
invariant set Omega with B_v >= c, and put f = rho in these coordinates (C^2), M_f = sup |f_v| < inf. Backward
orbits have u_T = e^{-alpha T} u, so J_T = d v_T/d v satisfies J_T' = -B_v J_T, 0 < J_T <= e^{-cT}; differentiating
f(u_T, v_T) = e^{-T} f(u, v) in v gives |f_v(u, v)| = e^T |f_v(u_T, v_T)| J_T <= M_f e^{-(c - 1)T} -> 0 (here
beta' > 1 is used). So f = g(u) on a rectangle, alpha u g' = g, and f = d_+ u^{1/alpha} (u > 0), d_- |u|^{1/alpha}
(u < 0), 0 (u = 0). Transporting by rho(X) = e^T rho(Phi_{-T} X), eta(Phi_{-T} X) = e^{-alpha T} eta(X) gives
rho = d_+- |eta|^{1/alpha} on {+-eta > 0} and rho = 0 on {eta = 0} on all of B(Z); the basin is dead iff
d_+ = d_- = 0.

Step 10 (Proposition 3.9: the C^3 restriction). Let e be the right alpha-eigenvector with e*(e) = 1; then
eta(Z + te) = t + O(t^2) and r(t) := rho(Z + te) is C^3 with r(t) = d_+- |t|^q (1 + O(|t|)) on +-t > 0,
q = 1/alpha >= 1.
If q < 3 is not an integer and some d_+- != 0, then r = o(|t|^n) with n = floor(q) forces the Taylor terms through
order n to vanish, so r = O(|t|^{n+1}) by Taylor's theorem, contradicting |r|/|t|^q -> |d_+-| > 0. If q = j in {1, 2,
3}, r = c t^j + o(|t|^j) gives d_+ = c and d_- = (-1)^j c. If q > 3, rho = O(|X - Z|^q) and no condition on d_+-
follows.
Only two derivatives of eta are used.

### 9.6 Proposition 3.10, Theorem 3.11 and the far-field part of Theorem 3.8(e)
Hypotheses: rho in S is a profile, l = c_l > 1, p = 1/l. Used: Sections 9.1, 9.2, 9.3 and 9.5, in particular
rho(Phi_t X) = e^t rho(X), rho = xi^2 on B(0) with D xi != 0 and D^2 rho = 2 D xi (x) D xi on Gamma, rho = 0 on both
manifolds of every saddle, the partition of the plane and the forward-limit alternative (escape or a saddle), the
absence of periodic orbits and saddle cycles (homoclinic loops included), and A(Theta(a)) = L(a)^{-p} rho(R e_a).
A saddle Y has eigenvalues -sigma < 0 < b with b - sigma = 2l.

Step 1 (passage chart). Translate Y to 0 and diagonalize DV(Y) = diag(b, -sigma) by a constant linear map. With the
local C^2 graphs z_1 = h_s(z_2), z_2 = h_u(z_1) of the stable and unstable manifolds, H(u, v) = (u + h_s(v),
v + h_u(u)) is a C^2 diffeomorphism near 0 with DH(0) = I, and the pulled-back field F = DH^{-1} V(H) is C^1 with
DF(z) = diag(b, -sigma) + O(|z|) (differentiate the formula; only V in C^2 and H in C^2 are used). Axis invariance
gives F_1 = u(b + f), F_2 = v(-sigma + g) with f, g continuous and |f| + |g| <= K(|u| + |v|).

Step 2 (passage time and exit height). In a rectangle [0, u_0] x [0, v_0] with |f| <= b/2, |g| <= sigma/2, the orbit
from (eps, v_0) exits through u = u_0 at a time T_eps with (2/(3b)) log(u_0/eps) <= T_eps <= (2/b) log(u_0/eps), and
v <= v_0 e^{-sigma t/2}, u <= u_0 e^{-b(T_eps - t)/2} on [0, T_eps]. Hence the integrals I_f, I_g of f, g along the
passage converge, as eps -> 0, to the sums I_f^*, I_g^* of their (absolutely convergent) integrals along the stable
axis from (0, v_0) and along the backward unstable axis from (u_0, 0): on [0, M] and on [T_eps - M, T_eps] by
continuous dependence, on the middle interval by the bound K[(2u_0/b) e^{-bM/2} + (2v_0/sigma) e^{-sigma M/2}].
Integrating log u and log v exactly, log(u_0/eps) = b T_eps + I_f and log(tau_eps/v_0) = -sigma T_eps + I_g, so
    T_eps = b^{-1} log(1/eps) + C_T + o(1),   tau_eps = C_tau eps^{sigma/b} (1 + o(1)),   C_tau > 0.
The exit map eps -> tau_eps is continuous and injective (v decreases along the passage), hence monotone, onto all
small heights, and its inverse tends to 0 at 0.

Step 3 (Proposition 3.10). For two C^1 transversals through points P and Phi_a P of one regular orbit, the implicit
function theorem gives a C^1 hitting time a(s) and a parameter map r(s) = cs + o(s), c != 0 (c = 0 would make the
first transversal parallel to V), and rho on the second transversal is e^{a(s)} rho on the first: the order k is
preserved and the coefficient is multiplied by e^a |c|^{-k} > 0. So rho(H(eps, v_0)) = D_0 eps^k (1 + o(1)),
sgn D_0 = sgn D, and
    rho(H(u_0, tau)) = e^{T_eps} rho(H(eps, v_0)) = D_0 e^{C_T} C_tau^{-q_k} tau^{q_k} (1 + o(1)),
    q_k = (kb - 1)/sigma,
which transfers to any transversal at any regular point of the outgoing branch. Since rho = 0 on that branch, kb > 1
whenever the premise holds. If the incoming branch is a branch of Gamma, xi(S(s)) = a s + o(s), a != 0, on a
transversal (ker D xi is spanned by V on Gamma), so k = 2 on both sides and q_2 = 2 + (4l - 1)/sigma > 2 with C > 0.
Taylor fact: if h is C^m on a straight transversal with h(t) = C|t|^q(1 + o(1)), C != 0, on one side, then either
h vanishes to order m (then q > m) or q is the order n <= m of the first nonzero Taylor coefficient, and then
h(t) = (-1)^n C|t|^n(1 + o(1)) on the other side. So a dead far side with rho in C^m forces q_2 > m, that is
sigma < (4l - 1)/(m - 2), impossible for C^infinity; for a C^infinity profile two live sides of finite orders force
equal integer orders N and C_- = (-1)^N C_+ (with rho only C^m this holds when one side has order at most m;
h(t) = |t|^{7/2} is C^3 with two live sides of non-integer order).

Step 4 (Theorem 3.11(a)). Assume the zeros of V are exactly 0, Z, Y, nondegenerate (then 0, Z are sources and Y a
saddle by the index count). Each unstable branch of Y escapes: its forward limit is a saddle or infinity, and Y itself
would give a homoclinic loop. The branches do not meet or self-intersect (no periodic orbits), so W^u(Y) is an
injective proper image of R, hence a proper embedded line, and its closure on the sphere is a Jordan curve. Its
complement has two components, and by the partition it is B(0) disjoint union B(Z); each basin is connected, so the
components are exactly B(0) and B(Z). The two local stable half-arcs lie on opposite local sides of W^u(Y), hence
(since the Jordan curve bounds both components at Y) in different basins: one stable branch comes from 0 and is a
branch of Gamma (Section 9.5, Step 7), the other comes from Z. The other branch of Gamma cannot end at Y, so it
escapes. Jets at Y: rho(Y) = 0 and grad rho(Y) = 0 (1 is not an eigenvalue); in linear eigen-coordinates the
homogeneous Taylor parts satisfy (b u d_u - sigma v d_v) P_j = P_j; the weights 2b, 2l, -2sigma of degree 2 are not 1;
of degree 3 only uv^2 (weight 2l - sigma) can have weight 1, when sigma = 2l - 1, and then P_3 = c u v^2; since
grad rho = 0 on the incoming branch of Gamma, the graph u = h_s(v) = O(v^2), 0 = d_u rho(h_s(v), v) = c v^2 + o(v^2),
so c = 0. Thus D^j rho(Y) = 0 for j <= 3. (The transport identity alone does not exclude uv^2: rho = uv^2 with
V = ((4l - 1)u, -(2l - 1)v) satisfies V.grad rho = rho and div V = 2l; it is not a profile.)

Step 5 (Theorem 3.11(b), rho in C^infinity). On the B(0) side of an outgoing branch rho has order q_2 > 2, so a dead
B(Z) contradicts Step 3. By Theorem 3.8(d) the weak eigenvalue alpha at Z is 1/2 or 1 or lies in (0, 1/3]; so
alpha <= 1 < beta' and Proposition 3.9 applies. On the straight line Z + se (e the weak right eigenvector),
rho = d_+- |s|^{1/alpha}(1 + O(s)), so by the Taylor fact 1/alpha = m is an integer and d_- = (-1)^m d_+ with
d_+ d_- != 0 (for every m, not only m <= 3). Then {rho = 0} in B(Z) is {eta = 0}, which contains the connection from Z
to Y (rho = 0 there); on a transversal to it both sides have order m with nonzero coefficients, and they pass (Step 3,
through the four quadrants of the chart) to the B(Z) sides of the two outgoing branches with order q_m. Matching with
q_2 on the B(0) side forces m = 2: alpha = 1/2 and rho = d eta^2. Then q_2 = N is an integer,
sigma = (4l - 1)/(N - 2), and on a signed straight transversal at each outgoing branch rho = C_0j t^N (1 + o(1))
(t > 0, B(0) side, C_0j > 0) and d K_Zj |t|^N (1 + o(1)) (t < 0, K_Zj > 0), with d K_Zj = (-1)^N C_0j. Hence d > 0
needs N even (N >= 4) and d < 0 needs N odd (N >= 3).

Step 6 (Theorem 3.11(c), x-even, rho in C^3). Evenness gives W(-x, y) = (-W_1, W_2)(x, y) (the kernel commutes with
the reflection), so the flow commutes with it, the reflection fixes 0 and hence Z and Y, and both lie on x = 0. On the
axis DV(0, y) = diag(2l - B'(y), B'(y)) with B(y) = V_2(0, y) = l y + o(|y|) at +-inf; the three simple zeros of B
have derivative signs +, -, + in increasing order, and sources have B' > 0, so Y is the middle zero, B'(y_Y) = -sigma
and psi_xy(Y) = B'(y_Y) - l = -(l + sigma). The axis intervals between a source and Y are the stable connections. If
B(Z) is live with alpha = 1 or 1/3, then rho = d eta^j (j = 1/alpha odd, d != 0) by Proposition 3.9; eta = 0 on the
vertical connection, so D eta(Z) is horizontal and eta(-x, y) = -eta(x, y) by the limit formula; then rho is odd in x
on B(Z), and also even, so rho = 0 there, a contradiction.

Step 7 (Theorem 3.11(d), any dead basin; exactly three zeros not assumed). If a dead basin is a half-plane
H = {n.X > d}, its boundary line is invariant, so V.n = 0 there and h = W.n + l d vanishes on the line; on H all
derivatives of rho vanish, so Lap W_1 = rho_xy = 0 and Lap W_2 = -rho_xx = 0, and h is harmonic, C^2 up to the line
and o(|X|). Its odd reflection is an entire harmonic function of sublinear growth, hence constant (gradient estimate
on large disks), hence 0. Then V.n = l(n.X - d) > 0 on H, so V has no zero in H, but the source of the basin lies in
it.

Step 8 (Theorem 3.11(e)). The escaping branch of Gamma crosses |X| = R once and transversally at R e_{a_0} (V.X > 0;
D xi != 0 on Gamma and its kernel is the tangent line of Gamma, so xi(R e_a) has a simple zero at a_0). There
f_0(a) = rho(R e_a) = xi(R e_a)^2 has f_0(a_0) = f_0'(a_0) = 0 < f_0''(a_0), and A(Theta(a)) = L(a)^{-p} f_0(a)
gives A(beta) = A'(beta) = 0 < A''(beta) = L^{-p} f_0''/Theta'^2 at beta = Theta(a_0). By Theorem 3.16, J_p[A] is not
identically 0 and rho = r^p A + r^{2p-1} J_p[A]/(l - 1) + o(r^{2p-1}), so rho is not r^p A outside any disk.

Step 9 (far-field part of Theorem 3.8(e)). Assume all zeros nondegenerate and every extra source as in Theorem
3.8(d) (so its basin is dead); let s be the number of saddles. On C_R = {|X| = R}, every point escapes forward; a
point outside all source basins lies on a saddle unstable manifold and is regular, so on an escaping branch. Each
escaping branch crosses C_R once, transversally, and distinct branches at distinct points; so the set E_R of such
crossings has at most 2s points, and the set G_R of crossings of Gamma at most 2. The complement of E_R in C_R is a
union of at most 2s open arcs (the whole circle if E_R is empty, and then there is one source and no saddle), each in
a single basin by connectedness; every basin meets C_R (it is unbounded and its backward orbits tend to its source
inside the disk). rho = xi^2 on B(0) (zero exactly on Gamma) and rho = 0 on every extra basin and every saddle
unstable manifold, so {a : rho(R e_a) = 0} = E_R u G_R u (the arcs in extra basins), and replacing the arcs by their
closures adds only points of E_R. Since L > 0, A^{-1}(0) = Theta(E_R u G_R u the closed arcs), with finitely many
arcs; a dead basin cannot meet C_R in infinitely many arcs.

### 9.7 Proposition 3.15 (the exact curved-layer solution and its uniqueness in the ansatz)
Setting: l > 1, beta = 2l - 1/2, I an open interval containing 0, f in C^1(I), s in C^2(I),
rho = x^2 f(y), psi = x s(y), W = (-psi_y, psi_x) = (-x s'(y), s(y)), V = l X + W, on the strip R x I. Assume
-Lap psi = rho_x and V.grad rho = rho there, f(0) = 1 (the jet rho = x^2 + O(|X|^3)) and s(0) = 0 (W(0) = 0).
Claim: I is contained in (-beta, inf) and, with b(y) := V_2(0, y) = l y + s(y),
    f = (beta/(beta + y))^4,   b(y) = beta (beta + y)/3 - beta^4/(3 (beta + y)^2).
Conversely these functions solve both equations on {y > -beta} (direct substitution; also checked symbolically), and
V = 0 there only at 0.

Step 1 (reduction). -Lap psi = -x s'' and rho_x = 2x f, so s'' = -2f; hence s is C^3 and b'' = s'' = -2f. Further
V_1 = x(l - s') = x(2l - b') and V_2 = b, so V.grad rho - rho = x^2 [2(2l - b') f + b f' - f]; since 1 - 4l = -2 beta,
the transport equation is
    b f' = 2(b' - beta) f   on I.
At y = 0 this gives 0 = 2(b'(0) - beta), so b'(0) = beta: the vertical strain is forced, DV(0) = diag(1/2, beta) and
c = psi_xy(0) = s'(0) = beta - l = l - 1/2. Also b(0) = s(0) = 0 and b''(0) = -2. With f = -b''/2 the transport
equation reads b b''' = 2(b' - beta) b''.

Step 2 (first integral). E := b b'' - (3b'^2 - 4 beta b')/2 is C^1 with
E' = b' b'' + b b''' - (3b' - 2 beta) b'' = b''(b' + 2b' - 2 beta - 3b' + 2 beta) = 0, so E = E(0) = beta^2/2 and
    b b'' = (3b' - beta)(b' - beta)/2   on I.
With v := b' - beta this is b v' = (beta + 3v/2) v, v(0) = 0, v'(0) = -2.

Step 3 (separation on each side of 0). Since b(0) = 0 and b'(0) = beta > 0, there is delta > 0 with b(y) y > 0,
v(y) y < 0 and beta + 3v/2 > 0 for 0 < |y| < delta (v(y) = -2y + o(y)). There
    d/dy [log|v| - (1/3) log(beta + 3v/2)] = v'(beta + v)/(v (beta + 3v/2)) = (beta + v)/b = b'/b,
using the partial fractions (beta + v)/(v(beta + 3v/2)) = 1/v - (1/2)/(beta + 3v/2). Hence
|v| (beta + 3v/2)^{-1/3} = K_+ |b| on (0, delta) and = K_- |b| on (-delta, 0), and letting y -> 0 from either side
(|v|/|b| -> 2/beta) gives K_+ = K_- = 2 beta^{-4/3}. With the signs of v and b,
    G(v) := v (beta + 3v/2)^{-1/3} = -2 beta^{-4/3} b   on (-delta, delta).
G is real-analytic near v = 0 with G'(0) = beta^{-1/3} != 0, so v = phi(b) with phi real-analytic near 0, and b solves
the autonomous equation b' = beta + phi(b), b(0) = 0, whose right side is locally Lipschitz. By uniqueness b agrees
near 0 with the explicit function (which satisfies G(v) = -2 beta^{-4/3} b identically, as one checks with
t = beta/(beta + y): v = (2 beta/3)(t^3 - 1), beta + 3v/2 = beta t^3, b = (beta^2/3)(1/t - t^2)). Remark (not used):
if b''(0) = -2 is replaced by b''(0) = a (still b(0) = 0, b'(0) = beta), then on 0 < |y| < delta
(G(v)/b)' = (G'(v) v' b - G(v) b')/b^2 = 0, since G'(v) = (beta + v)(beta + 3v/2)^{-4/3} and b v' = (beta + 3v/2) v;
this needs no division by v, so it covers a = 0. Hence G(v) = C b with C = a beta^{-4/3} on both sides: a
one-parameter family through 0 without logarithmic terms (a = 0 gives b = beta y and f = 0), and the jet f(0) = 1
selects a = -2.

Step 4 (continuation). Let b_* be the explicit function on (-beta, inf); b_* vanishes only at 0
((beta + y)^3 = beta^3) and b_* -> -inf, f_* = (beta/(beta + y))^4 -> inf as y -> -beta from above. On I' := I
intersect (-beta, inf), the set where (b, b', b'') = (b_*, b_*', b_*'') is relatively closed, contains a neighbourhood
of 0 by Step 3, and is open at every other point because b_* != 0 there and b''' = 2(b' - beta) b''/b is a regular ODE
near such a point. I' is an interval, so b = b_* and f = -b''/2 = f_* on all of I'. If I contained a point y <= -beta,
it would contain [-beta, 0], and f = f_* on (-beta, 0] would be unbounded near -beta, contradicting continuity of f on
I. So I is contained in (-beta, inf) and the solution is the explicit one.

Zeros of V: V = (x(2l - b'(y)), b(y)) vanishes only where b(y) = 0, i.e. y = 0, and then x(2l - beta) = x/2 = 0.
The solution is not in S (Section 2): it is not defined on the line y = -beta (f has a pole there, so rho does not
extend continuously to R^2), and on {y > -beta} it violates the growth bound |rho| <= C(1 + |X|)^gamma, gamma < 1,
since rho(x, 0) = x^2.

### 9.8 Theorems C, D and 3.5, Propositions 3.4 and 3.12 (moments, fluxes, exact tails, equilibria)
Hypotheses and notation: rho in C^3(R^2) with rho(0) = 0, grad rho(0) = 0 and the growth bounds of S (gamma in [0,
1)); W the canonical velocity, with W in C^2_loc, div W = 0, curl W = -rho_x, W(0) = 0 and |W(X)| <= C(1 + |X|)^gamma
(1 + log(1 + |X|)) (Section 9.0, Steps 1-2, which use only rho = O(|X|^2) at 0). W = J grad psi with psi(0) = 0, grad
psi(0) = 0; c = psi_xy(0), b = psi_yy(0), and psi_xx(0) = -b because Lap psi(0) = -rho_x(0) = 0. phi = r^{-3} sin 3th;
h = r^{-2} sin 2th is harmonic on r > 0 and d_x h = -2 phi. Omega = {eps < r < R} with outward normal n. For profiles:
l > 1, p = 1/l, c = l - 1/2 and b = 0 (Section 9.0, Step 4), |rho| + |W| <= C r^p and |grad rho| + |DW| <= C r^{p-1}
for large r (Section 9.2, Step 5), r^{-p} rho(r e_th) -> A(th) uniformly with A not identically 0 (Section 9.0, Step
6), and A in C^1 (Section 9.2, Step 6).

Step 1 (moment identity for an arbitrary quadratic jet). For real s, V_s = s X + W, I = int rho phi and Q = int rho
W.grad phi,
    I = pi c,   int (V_s.grad rho - rho) phi dX = (s - 1) pi c - Q,
with absolutely convergent integrals; no condition on D^2 rho(0) is used. Convergence: near 0, rho = O(r^2), grad
rho = O(r) and W = O(r), so rho phi, (V_s.grad rho - rho) phi and rho W.grad phi are O(r^{-1}); at infinity they are
O(r^{gamma-3}), O(r^{gamma-3}) and O(r^{2 gamma-4}(1 + log r)). Moment: integrating by parts in x and then using
rho_x = -Lap psi and Green's formula,
    int_Omega rho phi = -(1/2) oint rho h n_x ds - (1/2) oint (h d_n psi - psi d_n h) ds.
On r = R, |grad psi| <= C R^gamma (1 + log R) and |psi| <= C R^{gamma+1} (1 + log R) (integrate grad psi from 0), so
the three outer terms are O(R^{gamma-1} (1 + log R)). On r = eps the density term is O(eps); psi = psi_2 + O(r^3) with
psi_2 = (r^2/2)(c sin 2th - b cos 2th), n = -e_r and d_n h = 2 eps^{-3} sin 2th, so oint h d_n psi -> -pi c and oint
psi d_n h -> pi c. Hence I = pi c. b multiplies cos 2th, which is orthogonal to sin 2th, so it does not enter (the
same calculation with r^{-2} cos 2th gives int rho r^{-3} cos 3th dX = -pi b). Transport: with div V_s = 2s and X.grad
phi = -3 phi,
    int_Omega (V_s.grad rho - rho) phi = oint rho phi V_s.n ds + (s - 1) int_Omega rho phi - int_Omega rho W.grad phi,
and the boundary terms are O(eps) and O(R^{gamma-1}). Letting eps -> 0 and R -> inf gives the identity.

Step 2 (Theorem C). For the jet of S, s = 1/2 + c gives int (V.grad rho - rho) phi dX = pi c (c - 1/2) - Q[rho] for
every rho in S, profile or not. Here b is arbitrary and V.grad rho - rho = -2b xy + O(r^3) is in general only O(r^2),
which suffices for Step 1. For a profile, s = l and c = l - 1/2 > 1/2, so Q = pi c (c - 1/2) > 0 and kappa = Q/(pi
c^2) = 1 - 1/(2c) = 2(1 - p)/(2 - p). The constant is the inner Green boundary term of the stream function; the
transport flux through r = eps tends to 0. Rescaling: for rho_L(X) = L^2 rho(X/L), L > 0 (same jet), psi_L(X) = L^3
psi(X/L), W_L(X) = L^2 W(X/L), c_L = L c and Q_L = L^2 Q, so kappa is unchanged when c != 0 (rho_L is in general not a
profile for the same l). Evolution: for a classical solution of d_s rho = rho - V.grad rho, V = (1/2 + c(s)) X + W,
which keeps the jet (in particular b = 0) and satisfies the class-S bounds uniformly on compact time intervals, the
majorants of Step 1 allow differentiation of c = pi^{-1} int rho phi under the integral, and Step 1 with s = 1/2 + c
gives dc/ds = c (1/2 - c) + Q/pi. Neither the existence of such an evolution nor the preservation of the jet is shown
here; the quadratic part of the evolution gives d_s D^2 rho(0) = [[0, 2b], [2b, 0]], so the jet is kept only while
b = 0.

Step 3 (Proposition 3.4). Let rho in S be a profile, Phi smooth on the circle and f_m = r^{-m} Phi(th). Since div(rho
V) = (1 + 2l) rho, div(rho V f_m) = (1 + 2l - ml) rho f_m + rho W.grad f_m on r > 0, and on Omega
    (1 + 2l - ml) int_Omega rho f_m + int_Omega rho W.grad f_m = B_m(R) - B_m(eps),
    B_m(r) = oint_{|X| = r} rho f_m V.e_r ds,
with |B_m(eps)| <= C eps^{4-m} and |B_m(R)| <= C R^{2+p-m}. The two bulk integrands are O(r^{2-m}) at 0 and
O(r^{p-m}), O(r^{2p-m-1}) at infinity, so for 2 + p < m < 4 both are absolutely integrable and the limit gives the
second identity. At m = 2 + p the coefficient vanishes on every annulus; rho W.grad f_{2+p} is absolutely integrable
(O(r^{-p}) at 0, O(r^{p-3}) at infinity), B_{2+p}(eps) = O(eps^{2-p}) -> 0, and
    B_{2+p}(R) = l int R^{-p} rho(R e_th) Phi dth + R^{-1-p} int (rho W_r)(R e_th) Phi dth -> l int A Phi dth,
since the second term is O(R^{p-1}). This gives the first identity: its left side is an absolutely convergent integral
and equals the limit of the annular flux, whereas int rho r^{-2-p} Phi alone is not absolutely convergent when A Phi
is not identically 0 (the integral of its absolute value over r < R grows like log R), so it cannot be obtained by
subtracting full-plane integrals. Phi = sin 3th and m = 3 give (1 - l) pi c + Q = 0, the profile case of Theorem C.
Phi = 1 in the first identity gives int rho W_r r^{-3-p} dX = -(l/(2 + p)) int A dth. In S^+, rho >= 0 (Theorem B
(F3), Section 9.1), hence A >= 0, and A is not identically 0, so this integral is negative.

Step 4 (Theorem 3.5). Let 0 < p < 1, A in C^1, q = sin th A' - p cos th A and lambda = p + 1. Psi'' + lambda^2 Psi = q
has a unique 2 pi-periodic solution (the monodromy T of the homogeneous system has det(I - T) = 2 - 2 cos 2 pi
lambda > 0), and Psi is C^2 (q is continuous). H := r^p (-Psi' e_r + lambda Psi e_th) = J grad(r^{p+1} Psi), H(0) = 0,
is continuous, homogeneous of degree p, and satisfies div H = 0 and curl H = r^{p-1} (Psi'' + lambda^2 Psi) = -d_x F,
F = r^p A, on R^2 minus 0. H is the canonical velocity of F: by Section 9.3, Step 1 (which needs only A Holder), the
kernel field B[F] converges for X != 0, is continuous away from 0, homogeneous of degree p, satisfies div B[F] = 0 and
curl B[F] = -d_x F in distributions, and equals H by the uniqueness of the periodic angular solution. So
H = H_p[A]. Moreover H.grad F = r^{2p-1} J_p[A] with
J_p[A] = lambda Psi A' - p Psi' A.
(i) If A(beta) = A'(beta) = 0 < A''(beta), J_p[A] does not vanish identically on either one-sided neighbourhood of
beta. On an arc where A > 0 and J_p[A] = 0, (Psi A^{-k})' = A^{-k} (Psi' - k Psi A'/A) = 0 with k = (p + 1)/p > 2, so
Psi = C A^k there (C = 0 allowed). With a = A''(beta)/2 (only its existence is used) and t = th - beta,
A'(beta + t) = 2a t + o(t) and A = a t^2 + o(t^2), so
Psi = O(|t|^{2k}) = o(t^4), Psi(beta) = Psi'(beta) = 0, and Psi(beta + t) = lambda^{-1} int_0^t sin(lambda (t - u))
q(beta + u) du. If sin beta != 0, q(beta + u) = 2a sin beta u + o(u) and Psi(beta + t) = (a sin beta/3) t^3 + o(t^3);
if sin beta = 0, q(beta + u) = (2 - p) a cos beta u^2 + o(u^2) and Psi(beta + t) = ((2 - p) a cos beta/12)
t^4 + o(t^4). Both contradict Psi = o(t^4).
(ii) If a profile equals F outside |X| = R_0, then g = rho - F (with F(0) := 0) is supported in |X| <= R_0, integrable
and O(|X|^p) at 0, and for |X| > R_0
    W(X) - H(X) = B_0 + T_g(X),   B_0 = -int K(-Y) g(Y) dY,   T_g(X) = int K(X - Y) g(Y) dY = O(|X|^{-2})
(the contact term vanishes because g(X) = 0 there; |K(X - Y) - K(X)| <= C|X|^{-3}|Y|). Since l X.grad F = F, the
profile equation there is W.grad F = 0, that is, 0 = r^{2p-1} J_p[A] + r^{p-1} B_0.(p A e_r + A' e_th) + O(r^{p-3})
uniformly in th; multiplying by r^{1-2p} and letting r -> inf gives J_p[A] = 0.
For a profile in S^+, A is C^1 (Section 9.2, Step 6) and A = B^2 with the signed root B of Section 9.4, Step 2,
which is C^1 by the first-derivative statements of Theorem 3.1 and has simple zeros; at a zero beta, A' = 2 B B' and
(A'(beta + t) - A'(beta))/t = 2 (B(beta + t)/t) B'(beta + t) -> 2 B'(beta)^2 > 0, so A''(beta) exists and is
positive. Hence (i) excludes H_p[A].grad(r^p A) = 0 and, with (ii), an exactly homogeneous exterior. Only A in C^1 and
one zero with A = A' = 0 < A'' are used, so both conclusions hold for every profile in S whose A has such a zero.
Section 9.24, Step 7, shows without the condition A'' > 0 that J_p[A] is not identically zero for every profile in S,
so by (ii) no profile in S has an exactly homogeneous exterior. Both conclusions say nothing about corrected tails:
by Section 9.3, rho = r^p A + r^{2p-1} J_p[A]/(l - 1) + o(r^{2p-1}), and the correction cancels the leading
self-advection.

Step 5 (Proposition 3.12). Let rho in S be a profile and P a point with V(P) = 0 and grad rho(P) = 0; then rho(P) = 0.
With z = X - P, f(z) = rho(P + z) and W_P(z) = W(P + z) - W(P), V(P + z) = l z + W_P(z) because l P + W(P) = 0; f
satisfies the growth bounds of S (with constants depending on P), f(0) = 0, grad f(0) = 0, and W_P is the canonical
velocity of f (Section 9.0, Step 1 uses no Hessian normalisation). Step 1 for f with s = l and zero residual gives
Q_P = pi (l - 1) psi_xy(P), whatever the rank of D^2 rho(P); the condition grad rho(P) = 0 is needed (with a linear
term at P the integrals are not absolutely convergent and the inner boundary term of the density does not vanish).
Since Lap psi(P) = -rho_x(P) = 0, DV(P) = [[l - psi_xy(P), -psi_yy(P)], [-psi_yy(P), l + psi_xy(P)]] is symmetric with
eigenvalues l +- |(psi_xy(P), psi_yy(P))|. Differentiating the profile equation twice at P gives M^T H + H M = H for
M = DV(P), H = D^2 rho(P); in an eigenbasis of M this reads (2 lambda_- - 1) H_11 = (2l - 1) H_12 = (2 lambda_+ - 1)
H_22 = 0 with lambda_+ >= l > 1, so H_22 = H_12 = 0, H has rank at most one, and H != 0 only if lambda_- = 1/2.
Real-analytic profiles. The set where all derivatives of rho vanish is closed, and open by analyticity; a dead open
set would make it nonempty, hence all of R^2, against the jet. At a zero P of V with det DV(P) = 0, rho(P) = 0, M^T
grad rho(P) = grad rho(P) and tr M = 2l (Section 9.5, Step 1), so the eigenvalues of M are 0 and 2l, 1 is not an
eigenvalue, grad rho(P) = 0 and M is symmetric; in an orthonormal eigenbasis, V(P + z) = (0, 2l v) + O(|z|^2), z = (u,
v). If the Taylor series of rho at P had a first nonzero homogeneous part f_n = sum_j a_j u^{n-j} v^j (n >= 2), the
degree-n part of the profile equation would give 2l v d_v f_n = f_n, that is (2lj - 1) a_j = 0 for every j, so
f_n = 0. Hence rho vanishes near P, which was excluded. For a C^infinity profile the argument shows only that rho is
flat to all orders at a degenerate zero of V.

Step 6 (Theorem D). Replace the jet by rho = (e.X)^2 + O(|X|^3), e = (cos f, sin f), keeping the velocity law -Lap
psi = rho_x. M = DV(0) = l I + [[-c, -b], [-b, c]] is symmetric. The quadratic part of the profile equation is 2
(e.X)(e.MX) = (e.X)^2, so M e = e/2 and, since tr M = 2l, M Je = (2l - 1/2) Je. Hence DW(0) = k (I - 2 e e^T),
k = l - 1/2, that is psi_xy(0) = k cos 2f and psi_yy(0) = k sin 2f; conversely these give M e = e/2 and the quadratic
equation. They are therefore exactly the second-order compatibility conditions (not a sufficient condition for a
profile). Covariance: with X = R_f z, rho~(z) = rho(R_f z), psi~(z) = psi(R_f z) and W~(z) = R_{-f} W(R_f z), one has
W~ = J grad psi~, V~(z) := R_{-f} V(R_f z) = l z + W~(z), V~.grad rho~ = rho~ and rho~ = z_1^2 + O(|z|^3), while -Lap
psi~ = (R_{-f} e_1).grad rho~ = cos f d_1 rho~ - sin f d_2 rho~. This is the Darcy law with the gravity vector e_2
replaced by R_{-f} e_2 (U = -grad P - rho q gives -Lap psi = (-Jq).grad rho), and W~ is its canonical velocity (the
kernel formula rotates with determinant one; or by the uniqueness of Section 9.0, Step 1). So rho(R_f X) solves the
problem with the jet of Setting II and gravity rotated by -f. Rotating the density alone, with the fixed law -Lap
psi = rho_x, is not a symmetry: for f = pi/2 and rho = x^2 near 0, rho~ = v^2 near 0 and -Lap psi~ = -d_v rho~ = -2v,
whereas d_u rho~ = 0. Setting II is f = 0.

### 9.9 Propositions 3.6 and 3.14 (Fourier pairing and wall curvature in S^+_even)
Hypotheses: rho in S^+_even, l > 1, p = 1/l, c = l - 1/2, beta = 2l - 1/2. W = (u, v) is the canonical velocity; in
Propositions 3.6 and 3.14, W_2 denotes its second component v (not the twice-subtracted field of Section 2).
w(y) = v(0, y), b(y) = V_2(0, y) = l y + w(y), h(y) = rho_xx(0, y), g(y) = v_xx(0, y). Used: Section 9.0, Steps 1 and
4 (the kernel formula, W in C^2_loc, Lap v = -rho_xx, DV(0) = diag(1/2, beta), so w'(0) = c); Section 9.2, Step 5
(|W| <= C|X|^p, |DW| <= C|X|^{p-1} for large |X|); Section 9.4, Step 7 (the axis is invariant, W(-x, y) = (-u, v)(x,
y), rho = 0 on the axis and rho > 0 off it, b has no zero besides 0, b(0) = 0, b'(0) = beta, h(0) = 2, b
h' = (1 - 4l + 2b') h on R, h ~ H_+- |y|^{p-2}, int h w' dy = ((l - 1)/3) int h dy > 0, and C_1 x^2
(1 + |X|)^{p-2} <= rho <= C_2 x^2 (1 + |X|)^{p-2}). For x > 0, P_x(t) = x/(pi (x^2 + t^2)) and K_x(t) = d_x d_t
P_x(t) = 2t (3x^2 - t^2)/(pi (x^2 + t^2)^3); K_x is odd, K_x(t) = x^{-3} K_1(t/x), ||K_x||_1 = C x^{-2} and
||K_x||_inf = C x^{-3}.

Step 1 (bounds on the wall data). Since rho(x, y) = h(y) x^2/2 + o(x^2) for fixed y, the two-sided bound gives 2C_1
(1 + |y|)^{p-2} <= h(y) <= 2C_2 (1 + |y|)^{p-2}, so h is positive, C^1 and integrable. For large |y|, |b(y)| >= l|y|/2
and the wall equation gives |h'| <= |1 - 2l + 2w'| h/|b| <= C|y|^{p-3}; hence h' is in L^1 and L^inf and tends to 0 at
both ends. Integrating by parts, (h')^(k) = ik h^(k), so |h^(k)| <= C/(1 + |k|). From the density bound and
1 + |X| >= (1 + x + |y|)/2^{1/2},
    ||rho(x, .)||_inf <= C x^2 (1 + x)^{p-2},   ||rho(x, .)||_1 <= C x^2 (1 + x)^{p-1}   (x > 0),
and rho >= 0. By Section 9.2, Step 5, w' = O(|y|^{p-1}) and b' -> l at both ends.

Step 2 (kernel representation of w'). The vertical component of K is q(a, t) = (a^2 - t^2)/(2 pi (a^2 + t^2)^2), even
in a, and for x > 0, q(x, t) = -(1/2) d_x P_x(t) and 2 d_t q(x, t) = -K_x(t). On the axis the contact term -(rho(0,
y) - rho(0))/2 vanishes, and the principal value is an ordinary integral: near Y = (0, y), rho(a, z) <= C_y a^2, so
|q(a, y - z) rho(a, z)| <= C_y; at Y = 0 the subtraction is O(1) by the jet; at infinity the kernel difference is
O(|Y|^{-3}) against |rho| <= C(1 + |Y|)^gamma. By evenness in a,
    w(y) = 2 int_0^inf int_R [q(x, y - z) - q(x, -z)] rho(x, z) dz dx.
For every y, int rho(x, z)|K_x(y - z)| dz is at most ||rho(x, .)||_inf ||K_x||_1 <= C for x <= 1 and ||rho(x, .)||_1
||K_x||_inf <= C x^{p-2} for x >= 1, which is integrable in x. Hence D(y) = int_0^inf int_R rho(x, z) K_x(y - z) dz dx
is bounded, and continuous by dominated convergence (the x-integrand is continuous in y, as an L^inf-L^1 convolution,
and bounded by C min(1, x^{p-2}) uniformly in y), and 2[q(x, y - z) - q(x, -z)] = -int_0^y K_x(s - z) ds with an
absolutely integrable triple integral (bounded by C|y|), so Fubini gives w(y) = -int_0^y D(s) ds and
    w'(y) = -int_0^inf int_R rho(x, z) K_x(y - z) dz dx.
The same majorants give int_0^inf int int rho(x, z)|h(y)||K_x(y - z)| dy dz dx <= C ||h||_1 < inf.

Step 3 (harmonic pairing and the Fourier formula). H(x, z) = (P_x * h')(z) is the bounded harmonic extension of h'
(|H| <= ||h'||_inf, H -> h' uniformly as x -> 0). Integrating by parts in the convolution variable (the boundary terms
d_x P_x(z - y) h(y) = O(|y|^{-2} |y|^{p-2}) vanish), d_x H = K_x * h. By Step 2, Fubini and the oddness of K_x,
    int h w' dy = -int_0^inf int rho(x, z) (int h(y) K_x(y - z) dy) dz dx = int_0^inf int rho(x, z) d_x H(x, z) dz dx.
For x > 0, P_x(t) = (2 pi)^{-1} int e^{ikt} e^{-x|k|} dk, so K_x(t) = (2 pi)^{-1} int (-ik|k|) e^{-x|k|} e^{ikt} dk
and (K_x * h)(z) = (2 pi)^{-1} int (-ik|k|) e^{-x|k|} h^(k) e^{ikz} dk. Multiplying by rho(x, z) and integrating in z
(Fubini: ||rho(x, .)||_1 ||h||_1 int k^2 e^{-x|k|} dk < inf), with int rho(x, z) e^{ikz} dz = conj(rho^(x, k)) and the
substitution k -> -k,
    int rho(x, z) (K_x * h)(z) dz = (2 pi)^{-1} int ik|k| e^{-x|k|} A_x(k) dk,   A_x(k) = rho^(x, k) conj(h^(k)).
Since A_x(-k) = conj(A_x(k)), the contributions of k and -k add to -2k^2 e^{-xk} Im A_x(k), so this equals -(1/pi)
int_0^inf k^2 e^{-xk} Im A_x(k) dk. Absolute convergence in (x, k): by Step 1 the double integral of k^2 e^{-kx}
|rho^(x, k)| |h^(k)| is at most C int_0^inf x^2 (1 + x)^{p-1} (int_0^inf k^2 (1 + k)^{-1} e^{-kx} dk) dx; the inner
integral is at most x^{-2} for x <= 1 and 2x^{-3} for x >= 1, so the x-integrand is bounded on (0, 1] and O(x^{p-2})
on [1, inf). Integrating in x and using Section 9.4, Step 7 gives Proposition 3.6:
    ((l - 1)/3) int h dy = int h w' dy = -(1/pi) int_0^inf int_0^inf k^2 e^{-kx} Im(rho^(x, k) conj(h^(k))) dk dx,
all integrals absolutely convergent.

Step 4 (the exclusions in Proposition 3.6). The left side is strictly positive (l > 1, h > 0), and the weight k^2
e^{-kx} is positive, so Im(rho^(x, k) conj(h^(k))) >= 0 for almost every (x, k) in (0, inf)^2 is impossible. If rho(x,
y_0 + t) = rho(x, y_0 - t) for all x, t and one common height y_0, then h(y_0 + t) = h(y_0 - t), rho^(x,
k) = e^{-iky_0} R_x(k) and h^(k) = e^{-iky_0} H_0(k) with R_x, H_0 real (transforms of even integrable functions), so
A_x(k) is real and the right side vanishes: a contradiction. If for almost every x > 0, rho(x, .) = mu_x * h with mu_x
a real even signed Borel measure of finite total variation (no positivity and no uniform bound in x are needed), then
rho^(x, k) = mu_x^(k) h^(k) with mu_x^ real, A_x(k) = mu_x^(k) |h^(k)|^2 is real, and the same contradiction follows.

Step 5 (Proposition 3.14). From div W = 0 and curl W = -rho_x, Lap v = -rho_xx (Section 9.0, Step 1), so on the axis
b'' = v_yy(0, y) = -h - g; evenness gives v_x(0, y) = 0 but not v_xx(0, y) = 0. So g = -h - b'' is continuous (b is
C^2). Integrating b'' = -h - g over [-A, 0] and [-A, B] and letting A, B -> inf, with b'(0) = beta, b'(+-inf) = l and
h integrable (the improper integrals of g exist; absolute integrability of g, which follows from
|g| + |b''| <= C|y|^{p-2} in Section 9.2, Step 7, is not used),
    int_{-inf}^0 g dy = l - beta - int_{-inf}^0 h dy = -c - int_{-inf}^0 h dy < 0,   int_R g dy = -int_R h dy
(and int_0^inf g dy = c - int_0^inf h dy, of no definite sign). So g >= 0 (even almost everywhere) on (-inf, 0] is
impossible. Suppose g = 0 on (-beta, 0) (this covers g = 0 on [-beta, 0]). There b'' = -h, so b is C^3 on (-beta, 0)
(h is C^1 because rho is C^3), b h' = 2(b' - beta) h, b(0) = 0, b'(0) = beta, h(0) = 2. Since h > 0,
b'(y) = beta + int_y^0 h > beta and b(y) < 0 on (-beta, 0); put q = b' - beta > 0. Substituting h = -b'' gives b
b''' = 2(b' - beta) b'', so b b'' - (3/2)(b')^2 + 2 beta b' is constant, equal to beta^2/2 (its limit at 0), that is
-b h = b b'' = q (2 beta + 3q)/2. Then h'/h = 2q/b = -4h/(2 beta + 3q) = 4q'/(2 beta + 3q), and h(0) = 2 gives
h = 2(1 + 3q/(2 beta))^{4/3}; a = (1 + 3q/(2 beta))^{-1/3} has a' = 1/beta and a(0) = 1, so
    h(y) = 2 beta^4/(beta + y)^4,   b(y) = beta (beta + y)/3 - beta^4/(3 (beta + y)^2)   (-beta < y < 0).
Here b < 0 on the open interval (b = beta (t^3 - beta^3)/(3t^2) with t = beta + y in (0, beta)), so the formula is
finite inside the interval and blows up only as y -> -beta. Since rho is C^3, h is continuous at -beta, a
contradiction. The argument does not exclude g = 0 on an interval (-beta', 0) with beta' < beta, and neither
hypothesis on g is known for a general profile. With the twice-subtracted field T = W - DW(0) X (T(0) = 0, DT(0) = 0)
one has T_2(0, y) = w(y) - c y, so d_y T_2(0, y) = w' - c -> -c at both ends and int h d_y T_2(0, .) dy = -(beta/3)
int h dy; d_x^2 T_2 = g is unchanged, so this step holds for either reading of g, whereas Proposition 3.6 and the
decay w' = O(|y|^{p-1}) require w' = d_y v(0, y).

### 9.10 Proposition 3.17 (the axis identity in S^+_even)
Hypotheses: rho in S^+_even, l > 1, p = 1/l, beta = 2l - 1/2. Used: the first-derivative conclusions of
Theorem 3.1 (Section 9.2, Steps 1-6: w = O(|y|^p) for large |y|; A, L and Theta in C^1 with Theta' > 0); the local
regularity xi in C^2 and V in C^{2,alpha}_loc from Section 9.1; and Section 9.4, Steps 2, 4, 6 and 7 (b is C^2 with
b(0) = 0,
b'(0) = beta and no other zero; h is continuous and positive with h(0) = 2; b h' = 2(b' - beta) h on R, the wall
equation of Theorem 3.3, since 1 - 4l = -2 beta; h(y) |y|^{2-p} -> H_+- > 0 as y -> +-inf; h = 2 xi_x(0, y)^2; S is a
homeomorphism of R^2 fixing 0 and a C^1 diffeomorphism of R^2 minus 0, with S R = R S for R(x, y) = (-x, y),
S(X) = X + O(|X|^p) and DS = I + O(|X|^{p-1}) for large |X|; xi = Xi o S with Xi(Y) = |Y|^{p/2} B(arg Y) and the
signed root B(Theta(a)) = L(a)^{-p/2} xi(R e_a), which is C^1 with A = B^2; the zeros of B are pi/2 and 3pi/2, and B'
does not vanish there). The C^2 statements of Theorem 3.1 (Section 9.2, Step 7) are not used.

Step 1 (the half-axis formulas). Since b(y) = beta y + O(y^2) and b has no zero besides 0, b > 0 on (0, inf) and b < 0
on (-inf, 0), so B_+- > 0, B_+-(r) = beta r + O(r^2) as r -> 0 and B_+-(r) = l r + O(r^p) as r -> inf. The integrands
of J_+- are O(1) on (0, 1] and O(r^{p-2}) on [1, inf), so J_+- converge absolutely. With h_+(r) = h(r) and
h_-(r) = h(-r) one has B_-'(r) = b'(-r) and h_-'(r) = -h'(-r), so the wall equation gives B_+- h_+-' = 2(B_+-' - beta)
h_+- on (0, inf) for both signs; dividing by B_+- h_+- > 0, (log(h_+-/B_+-^2))' = -2 beta/B_+-. The positive function
    E_+-(r) = 2 (B_+-(r)/(beta r))^2 exp(-2 beta int_0^r (1/B_+-(s) - 1/(beta s)) ds)
has the same logarithmic derivative on (0, inf), and both E_+- and h_+- tend to 2 as r -> 0, so h_+- = E_+-. For
r >= 1 the integral in E_+- equals J_+- + (1/l - 1/beta) log r - int_r^inf (1/B_+- - 1/(l s)) ds, the last term is
O(r^{p-1}), and -2 beta (1/l - 1/beta) = 2 - (4l - 1) p = p - 2. Since also B_+-(r)/(beta
r) = (l/beta)(1 + O(r^{p-1})), h_+-(r) = (2 l^2/beta^2) exp(-2 beta J_+-) r^{p-2} (1 + O(r^{p-1})), and H_+- = (2
l^2/beta^2) exp(-2 beta J_+-).

Step 2 (the curvatures). At a zero th_0 of B, A''(th_0) exists and equals 2 B'(th_0)^2 > 0: A' = 2 B B' is continuous
and (A'(th_0 + t) - A'(th_0))/t = 2 (B(th_0 + t)/t) B'(th_0 + t) -> 2 B'(th_0)^2. From S R = R S, S_1(0, y) = 0 and
d_x S_2(0, y) = 0, and S(0, y) = (0, S_2(0, y)) is not 0 for y != 0. Xi is C^1 off 0, and at Y = (0, z), z != 0, B(arg
Y) = 0 and d_1 arg Y = -1/z give d_1 Xi(0, z) = -sgn(z) |z|^{p/2-1} B'(sgn(z) pi/2). Since xi = Xi o S with both maps
C^1 on R^2 minus 0, the chain rule gives
    xi_x(0, y) = d_1 Xi(S(0, y)) d_x S_1(0, y),
    h(y) = 2 xi_x(0, y)^2 = 2 |S_2(0, y)|^{p-2} B'(sgn(S_2(0, y)) pi/2)^2 (d_x S_1(0, y))^2
(y != 0; the term containing d_x S_2(0, y) = 0 drops out). As |y| -> inf, S_2(0, y) = y + O(|y|^p) and d_x S_1(0,
y) = 1 + O(|y|^{p-1}), so h(y) |y|^{2-p} -> 2 B'(+-pi/2)^2 = A''(+-pi/2) as y -> +-inf, and H_+- = A''(+-pi/2)
(A''(-pi/2) := A''(3pi/2)). Only first derivatives of S and Xi enter, and no convergence of second derivatives of
R^{-p} rho(R .) is used.

Step 3 (the identity). J_- - J_+ = int_0^inf (1/B_- - 1/B_+) dr, as the difference of two absolutely convergent
integrals with the same subtracted terms, and 1/B_- - 1/B_+ = (B_+ - B_-)/(B_+ B_-) = 2 w_e/(b_o^2 - w_e^2), where
b_o^2 - w_e^2 = B_+ B_- > 0 and w_e = (b(r) + b(-r))/2 = (w(r) + w(-r))/2 (the terms l r and -l r cancel). By Step 1,
log(H_-/H_+) = -2 beta (J_- - J_+), which with Step 2 is the identity. The integrand is O(1) near 0 (w_e = O(r^2) and
B_+ B_- >= beta^2 r^2/2 for small r) and O(r^{p-2}) at infinity (w_e = O(r^p) and B_+ B_- >= l^2 r^2/2 for large r),
so the integral converges absolutely; the integrals of 1/B_+- themselves diverge at both ends.

Step 4 (consequences). Since beta > 0, the integral has the sign of log(A''(pi/2)/A''(-pi/2)). If the curvatures are
equal the integral vanishes, and a continuous w_e that is not identically 0 and has one sign would give it that strict
sign against the positive weight 1/(B_+ B_-); so w_e is 0 or changes sign. If A''(-pi/2) <= A''(pi/2) and w_e <= 0 on
(0, inf), both terms of the identity are <= 0 and their sum is 0, so both vanish: the curvatures are equal, and
int_0^inf w_e/(B_+ B_-) dr = 0 with w_e <= 0 continuous gives w_e = 0. The reversed case is the same with all signs
changed.

Step 5 (relation to 5.8(v)). A/cos^2 th = (B/cos th)^2 extends continuously and positively over pi/2 and 3pi/2 (B/cos
th -> -B'(th_0)/sin th_0 != 0 at both zeros th_0), so F = log(A/cos^2 th) is continuous, 2 e^{F(+-pi/2)} = A''(+-pi/2)
and log(A''(-pi/2)/A''(pi/2)) = F(-pi/2) - F(pi/2). The hypotheses of 5.8(v) hold with m1 = 1/2 and
n = 2l - m1 = beta: B_+- > 0, B_+- = beta r + O(r^2) at 0 and l r + O(r^p) at infinity (Step 1), and the transverse
coefficients at infinity are those of A (Step 2). The function k of 5.8(iv) is xi_x(0, y): differentiating V.grad
xi = xi/2 in x on the axis, where V_1 = xi = xi_y = 0, gives b k' + (d_x V_1 - 1/2) k = 0 with k(0) = 1. Hence
h/k^2 = 2 on both half-axes, G(+inf) = G(-inf) = 1, D = 0, and the formula of 5.8(v) becomes the identity of
Proposition 3.17.

### 9.11 Section 4.16 (scattering-domain inertia, distribution functions and the stream-sign tests)
1. For 4.16(a)-(c) assume rho in S^+, put p = 1/l in (0,1), and write e_r(theta) = (cos(theta),sin(theta)).
Set e_theta = (-sin(theta),cos(theta)), F = r^p A, D_R = S^{-1}(B_R), I(R) = int_{D_R}|X|^2, Q(R) = int_{D_R}X.W.
Let Psi be the periodic solution of Psi''+(p+1)^2 Psi = sin(theta) A'-p cos(theta) A,
and put H = r^p(-Psi' e_r+(p+1)Psi e_theta), E_A = int_0^{2pi}(Psi')^2 dtheta.
Use Theorems 3.1, 3.2 and 3.13: rho = F o S, F = r^p A, rho = xi^2 with grad xi != 0, and S preserves area.
Also S is a homeomorphism fixing 0 and a C^2 diffeomorphism off 0, with DS = I+O(r^{p-1}).
Section 9.3, Steps 1, 3 and 7 identify this H as the canonical field of F and give W = H+o(r^p) and
S(X) = X+H(X)/(l-1)+o(r^p), uniformly as r = |X|->infinity. Set T = S^{-1}.
Since S(X) = X+O(r^p), T(Y) = Y+O(|Y|^p); substituting X = T(Y) in the expansion, homogeneity and
uniform continuity of H on compact annuli give T(Y) = Y-H(Y)/(l-1)+o(|Y|^p), uniformly.
For every R > 0, D_R is bounded and has C^2 boundary, since T is C^2 near the circle |Y| = R.
Area preservation gives |D_R| = pi R^2. For any set D of this area,
int_D|X|^2-pi R^4/2 = int_{D\B_R}(|X|^2-R^2)+int_{B_R\D}(R^2-|X|^2) >= 0.
2. For large R the boundary of D_R lies in |r-R| <= C R^p. The inner disk is in D_R and the exterior is outside:
use |S(X)-X| <= C(1+|X|)^p, increasing r-C(1+r)^p for large r, and boundedness of S on compact sets.
On the enclosing annulus, d_r|S(r e_r(theta))| = 1+O(R^{p-1}) > 0, using DS and S/r = e_r+O(r^{p-1}).
Hence each ray crosses the boundary once. Writing its radius s_R(theta), the expansion for S gives
R = s_R+s_R^p h_r(theta)/(l-1)+o(R^p), so s_R = R+R^p Psi'/(l-1)+o(R^p), since
h_r(theta) := e_r(theta).H(e_r(theta)) = -Psi'(theta).
The area constraint int s_R^2 = 2pi R^2 and polar integration give
I(R)-pi R^4/2 = (1/4)int(s_R^2-R^2)^2 = E_A R^{2p+2}/(l-1)^2+o(R^{2p+2}).
Because div W = 0, int_{B_R}X.W = (R^2/2)int_{boundary B_R}W.n = 0.
Thus Q(R) = int_0^{2pi}int_R^{s_R(theta)}r^2 W_r dr dtheta, with oriented inner integrals.
Uniformly on this annulus r^2 W_r = -R^{p+2}Psi'+o(R^{p+2}); multiplication by s_R-R proves its asymptotic.
3. If E_A = 0, Psi is constant. At a quadratic zero beta of A the angular equation makes that constant zero.
It would follow that sin(theta)A'-p cos(theta)A = 0. Write theta = beta+t, A = a t^2+o(t^2), A' = 2a t+o(t).
If sin(beta) != 0 the left side is 2a sin(beta)t+o(t); if sin(beta) = 0 it is
a(2-p)cos(beta)t^2+o(t^2). Both are nonzero to leading order because a > 0 and 0 < p < 1. Thus E_A > 0.
4. Conjugacy gives Phi_t(D_R) = D_{exp(lt)R}. Differentiating the bounded-domain moment along this smooth flow,
l R I'(R) = int_{D_R}[V.grad|X|^2+|X|^2 div V] = 4l I(R)+2Q(R).
These operations are legitimate for every R > 0 because the boundary avoids 0; no derivative of S at 0 is needed.
The coefficients agree since l(2p+2) = 4l-2(l-1). The identity itself also gives the asymptotic of I',
without differentiating a little-o remainder. In particular (I/R^4)' = 2Q/(l R^5) < 0 for all large R.
Since curl(W+rho e_2) = 0 on the plane, define P by grad P = -W-rho e_2, uniquely up to a constant.
For either D = D_R or D = B_R, integration by parts gives
int_D X.W = 2int_D P-int_{boundary D}P X.n-int_D y rho.
For q_H = (Psi'-A sin(theta))/(p+1), the angular equation gives q_H' = -(p+1)Psi-A cos(theta).
The radial and angular derivatives of P_H = r^{p+1}q_H therefore give H = -grad P_H-F e_2.
Moreover grad(P-P_H) = -(W-H)-(rho-F)e_2 = o(r^p); radial integration gives P-P_H = o(r^{p+1}).
To evaluate work at order R^{2p+2}, subtract the exact ball identity first: the difference is
-int_{D_R-B_R}X.grad P-int_{D_R-B_R}y rho = int_0^{2pi}int_R^{s_R}r^2 W_r dr dtheta.
Here D_R-B_R denotes an oriented integral. In this shell, the error from grad(P-P_H) and rho-F is
o(R^{p+1}) times O(R^{p+1}) = o(R^{2p+2}). Substitution of P_H,F reproduces the coefficient of Q.
5. At the two zeros beta_j of A set a_j = A''(beta_j)/2 > 0, C_A = sum_j a_j^{-1/2}, and
m(t) = |{theta:A(theta) < t}|.
Near beta_j, for arbitrary small epsilon > 0,
(a_j-epsilon)s^2 <= A(beta_j+s) <= (a_j+epsilon)s^2; outside fixed neighborhoods A has a positive minimum.
Squeezing these sublevel intervals and then sending epsilon to zero gives m(t) = 2C_A sqrt(t)+o(sqrt(t)).
Also m(t) <= C sqrt(t) for all t > 0, by this estimate near zero and m(t) <= 2pi elsewhere.
Area preservation turns |{a < rho < b} intersect D_R| into int_0^R r[m(b/r^p)-m(a/r^p)]dr.
Positive level sets of F have area zero, since on each ray with A > 0 the positive levels have one radius.
Thus strict endpoints do not affect the preceding equality, even if A has a positive plateau.
The integrand is 2C_A(sqrt(b)-sqrt(a))r^{1-p/2}+o(r^{1-p/2}); its bounded-radius part is finite.
Integration gives the stated band asymptotic. For physical balls, S(B_R) and B_R differ only in
|r-R| <= C R^p, by the bounds for S and T. In this annulus {a < F < b} has angular measure O(R^{-p/2}),
so its area is O(R^{1+p/2}) = o(R^{2-p/2}), since p < 1. Changing variables by S proves the ball formula.
6. For measurable g >= 0 with int_0^infinity g(t)t^{2/p-1}dt > 0, substitute t = r^p A(theta) where A > 0. Tonelli
gives
int g(F)dX = (1/p)[int A^{-2/p}dtheta][int_0^infinity g(t)t^{2/p-1}dt].
Interpret this by first restricting to angles away from the zeros and then increasing to their complement.
The angular factor diverges like int |theta-beta_j|^{-4/p}dtheta. If the second factor is positive,
the result is infinity, including when that factor is infinite. Area preservation gives the assertion for rho.
For q > -1/2, int A^q < infinity and 2+pq > 0, so polar integration gives
int_{D_R}rho^q = R^{2+pq}int A^q/(2+pq). For q <= -1/2, use local coordinates (xi,v) along Gamma:
their Jacobian is bounded above and below by positive constants, and int_{-epsilon}^{epsilon}|xi|^{2q}dxi diverges.
Every D_R contains a nontrivial segment of Gamma. The value assigned to rho^0 on Gamma is immaterial.
7. S maps the two branches of Gamma to the zero rays of F and maps boundary D_R to the circle |Y| = R.
At the two intersection points S is a C^2 diffeomorphism, so Gamma and boundary D_R meet transversely.
On the compact closure of D_R, grad xi != 0. Interior coordinates (xi,v), and boundary coordinates at these
transverse endpoints, show that J(u) = int_{{xi = u} intersect D_R}|grad xi|^{-1}ds is continuous at u = 0:
use a finite partition of unity; in each chart integrate a continuous Jacobian over intervals with continuous
endpoints.
The coarea formula then gives |{0 < rho < t} intersect D_R|/(2sqrt(t))->J(0).
In scattering coordinates the numerator is int_0^R r m(t/r^p)dr, as the zero rays have zero area.
After division by 2sqrt(t), the integrand tends to C_A r^{1-p/2} and is bounded by C r^{1-p/2}.
Dominated convergence therefore gives J(0) = C_A R^{2-p/2}/(2-p/2), for every R > 0.
8. Let zeta be C^2 with compact support in an annulus avoiding 0, G in C^1([0,infinity)), and
L_R = int zeta(X/R)[G(rho(X)/R^p)-G(F(X)/R^p)]dX. Put epsilon_R = R^{p-1}, S_R(Y) = S(RY)/R and T_R = S_R^{-1}.
On each compact annulus,
S_R = Id+epsilon_R H/(l-1)+o(epsilon_R), T_R = Id-epsilon_R H/(l-1)+o(epsilon_R), uniformly.
Homogeneity and rho = F o S give rho(RY)/R^p = F(S_R(Y)). Since F is C^1 away from 0,
Taylor expansion of F and G yields R^{-p-1}L_R->(l-1)^{-1}int zeta G'(F)H.grad F.
Alternatively, area preservation gives L_R/R^2 = int[zeta(T_R(Y))-zeta(Y)]G(F(Y))dY.
The support lies in one fixed enlarged annulus for all large R, by the bounds for S_R and T_R.
Taylor expansion of zeta gives the other limit, -(l-1)^{-1}int G(F)H.grad zeta.
Their difference is -(l-1)^{-1}int zeta G(F)div H = 0. No angular constraint beyond div H = 0 results.
9. For 4.16(d) set p = 1/2 and rho_M = x^2(1+r^2)^{-3/4}[1+M y^6/(1+r^2)^3], with M fixed and nonnegative.
The bracket lies in [1,1+M], is smooth and even, and has gradient O(r^{-1}) at infinity.
Direct differentiation gives rho_M = x^2+O(r^4), |rho_M| <= C(1+r)^{1/2}, and |grad rho_M| <= C(1+r)^{-1/2}.
Thus rho_M belongs to S as a density. Its tail is F_M = r^{1/2}A_M, with A_M as stated;
the error d = rho_M-F_M is O(r^{-3/2}) and grad d = O(r^{-5/2}) at infinity, and d is Holder of exponent 1/2 near 0.
The unsubtracted velocity U[d] = PV int K(X-Y)d(Y)dY-d(X)e_2/2 exists by local Holder cancellation and tail decay.
For r = |X| large, |Y| < r/2 contributes O(r^{-2}int_{|Y| < r/2}|d|) = O(r^{-3/2}).
On |Y-X| < r/4 subtract d(X); the contribution is O(r sup|grad d|) = O(r^{-3/2}).
The remaining part with |Y| <= 2r has |K(X-Y)| <= C r^{-2} and mass O(r^{1/2}); the tail |Y| > 2r is O(r^{-3/2}).
The local term has the same bound. Hence U[d](X) = O(r^{-3/2}), W[d] = U[d]-U[d](0) = O(1), and
W[rho_M] = H_M+O(1), using linearity and the homogeneous canonical law of Section 9.3, Step 1.
Reflection in x makes W_1 odd in x and W_2 even in x, so W_1(0,y) = 0. A stream with grad-perp psi = W
is constant along the axis; set that constant to zero. W(0) = 0 also gives grad psi(0) = 0.
Since (H_M)_2(r,0) = (3/2)r^{1/2}Psi_M(0), integrating psi_x = W_2 from 0 to r proves the stream asymptotic.
10. Write A_* = cos^2(theta)sin^6(theta) = 5/128-cos(2theta)/32-cos(4theta)/32+cos(6theta)/32-cos(8theta)/128.
The angular operator sends cos(n theta) to ((3/2)^2-n^2)cos(n theta). For a cosine mode a_n cos(n theta), n >= 1,
the forcing contributes -(n+p)a_n cos((n-1)theta)/2+(n-p)a_n cos((n+1)theta)/2; a_0 contributes -p a_0 cos(theta).
Consequently Psi_0 = -(7/10)cos(theta)-(1/18)cos(3theta), and
Psi_* = cos(theta)/64-cos(3theta)/144+5cos(5theta)/728-61cos(7theta)/23936+cos(9theta)/2688.
Substitution verifies every mode; uniqueness of the periodic solution follows because 3/2 is not an integer.
Thus Psi_0(0) = -34/45, Psi_*(0) = 2048/153153, and Psi_100(0) = Psi_0(0)+100Psi_*(0) = 148474/255255.
11. Differentiation gives the stated positive formula for (rho_0)_x. Reflection in y makes W_2 even in y,
so c = partial_y W_2(0) = 0. Reflection in x makes partial_x W_2(0) = partial_y W_1(0) = 0; div W = 0 gives DW(0) = 0.
Hence W = O(r^2), grad rho_M = 2x e_1+O(r^3), and (2X+W).grad rho_M-rho_M = 3x^2+O(r^3).
The jet of a profile requires l = 1/2+c = 1/2, while a nonzero profile in S with this growth requires l >= 2.
Thus these are not profiles for any l. The two positive quadratic zeros of A_M have coefficients a_1 = a_2 = 1+M.
12. For completeness C_M = sup|DW[rho_M]| < infinity: first and second derivatives of rho_M are bounded,
and grad rho_M belongs to L^q for q > 4. In the differentiated canonical operator, cancellation on |Z| < 1
is controlled by the second derivatives, while Holder's inequality on |Z| >= 1 uses K in L^{q'} there,
q' = q/(q-1) > 1.
Differentiation is justified by truncation and integration by parts; the outer boundary error is O(R^{-1/2}).
Kernel scaling gives W[rho_{M,L}](X) = L^2 W[rho_M](X/L), so |W[rho_{M,L}](X)| <= L C_M |X|.
If L C_M < 2, X.(2X+W) >= (2-L C_M)|X|^2 > 0 off 0. The velocity has exactly one zero.
The scaled stream is L^3 psi_M(X/L), preserving both signs and the zero wall. Its c remains zero and its residual
still has leading term 3x^2. These examples therefore invalidate only the stated density-based sign implications.

### 9.12 Proposition 4.13a (positive-density bounds and endpoint angular tests)
1. Let rho in S^+. By Theorems A and 3.2, 0 < p < 1, rho >= 0, rho = O(r^p) at infinity, and the angular coefficient A
is not identically zero. The jet gives rho = O(r^2) near 0 and rho(x, 0)/x^2 -> 1 as x -> 0, so H_2 >= 1; H_2 and C_p
are finite (rho/r^2 = O(r^{p-2}) at infinity and rho/r^p = O(r^{2-p}) near 0) and positive.
2. (a). Theorem C (Section 9.8, Step 1) gives pi c = int rho r^{-3} sin 3th dX, and c = l - 1/2 (Section 9.0, Step 4),
    so l - 1/2 = (1/pi) int_0^inf int_0^{2pi} rho(r, th) sin 3th dth r^{-2} dr,
absolutely convergent (radial majorants O(1) at 0 and O(r^{p-2}) at infinity). On each circle 0 <= rho <= M(r) gives
int rho sin 3th dth <= M(r) int (sin 3th)_+ dth = 2 M(r), which proves the first inequality. With M = H r^2 on (0, 1]
and M = C r^gamma on (1, inf) the integral of M r^{-2} is H + C/(1 - gamma). At an angle with A > 0, rho/r^p -> A, so
rho <= C r^gamma forces p <= gamma, i.e. l >= 1/gamma.
3. (b). Take M(r) = min(H_2 r^2, C_p r^p), an envelope by the definitions, and R = (C_p/H_2)^(1/(2 - p)), where the
two branches meet. Then
    int_0^inf M r^{-2} dr = H_2 R + C_p R^{p-1}/(1 - p) = ((2 - p)/(1 - p)) H_2^((1-p)/(2-p)) C_p^(1/(2-p)).
With l - 1/2 = (2 - p)/(2p) and (1 - p)/p = l - 1, (a) gives l - 1 <= (4/pi) H_2^((1-p)/(2-p)) C_p^(1/(2-p)); raising
both sides to the power 2 - p gives the inequality of (b). If H_2 <= H and C_p <= C, the right side is at most (4/pi)
(sqrt(H C))^(2(1-p)/(2-p)) C^(p/(2-p)) <= (4/pi) max(sqrt(H C), C), since the two exponents add to 1. If H_2 <= H,
then C_p >= H^(p-1) (pi/4)^(2-p) (l - 1)^(2-p); after division by l^2, as l -> infinity (p = 1/l, (l - 1)^(-p) -> 1,
((l - 1)/l)^2 -> 1, H^(p-1) -> 1/H) the right side tends to pi^2/(16 H).
4. (c). Theorem 3.16 gives Psi'' + (p + 1)^2 Psi = sin th A' - p cos th A for Psi = Psi_p[A]. Mode 2 of the right side
comes only from modes 1 and 3 of A; the product formulas give the coefficients ((1 - p) a_1 - (p + 3) a_3)/2 of
cos 2th and ((1 - p) b_1 - (p + 3) b_3)/2 of sin 2th, and division by (p + 1)^2 - 4 = (p - 1)(p + 3) gives the two
formulas. For fixed A in C^2, on the complement of mode 2 the inverse of d^2/dth^2 + (p + 1)^2 is bounded from L^2 to
H^2 uniformly for p near 1 (the multipliers (1 + n^2)/|(p + 1)^2 - n^2|, n != 2, are bounded there); H^2 embeds in C^1
on the circle, and the equation then bounds Psi''. Hence Psi = P_3/(2 eps) + O(1) in C^2. Since l - 1 = eps/p,
B_p = (p/eps)((p + 1) Psi A' - p Psi' A); substituting, and replacing p by 1 in the leading coefficient at a cost
O(eps) eps^{-2}, gives the expansion. If 2 P_3 A' - P_3' A vanished identically, then (P_3/A^2)' = -(2 P_3 A' - P_3'
A)/A^3 = 0 on every positive arc of A, so P_3 = C A^2 there with a constant C for each arc. A nonzero P_3 has four
simple zeros and at most two of them are zeros of A, so one lies inside a positive arc; on that arc C = 0, so P_3
vanishes on an open interval, which is impossible for a nonzero trigonometric polynomial.
For A_f, expanding cos^2 th (1 + 16 sin^6 th) gives the displayed Fourier sum; the factor 1 + 16 sin^6 th is positive,
so the zeros are those of cos th, and A_f(pi/2 + t) = sin^2 t (1 + 16 cos^6 t) = 17 t^2 + O(t^4), likewise at 3pi/2.
Its modes are 0, 4, 6 and 8, so the forcing sin th A_f' - p cos th A_f has only the odd frequencies 1, 3, 5, 7, 9. For
odd n >= 3, |(p + 1)^2 - n^2| >= 5 when 0 < p < 1; at n = 1 the cos th coefficient of the forcing is -p a_0 - (p + 2)
a_2/2 = -9p/8 (a_2 = 0) and the multiplier is 1/(p (p + 2)), which gives -9/(8 (p + 2)); the sin th coefficient
vanishes. So Psi_p[A_f] is bounded uniformly for 0 < p < 1.
5. (d). Suppose a profile satisfies the hypotheses, and put delta = 1/100, a = A/m and psi = Psi_p[A]/m (Psi_p is
linear, so psi = Psi_p[a]). Since l < 100/99, p lies in (99/100, 1). Here sup |A_0| = sup |A_0'| = 1,
sup |Psi_ref| <= 5/12 + 1/20 = 7/15 and sup |Psi_ref'| <= 5/12 + 3/20 = 17/30. With J_p(a, psi) = (p + 1) psi a' - p
psi' a, writing each product as a difference against the reference pair and using p + 1 <= 2, p <= 1 and sup |a|,
sup |a'| <= 1 + delta,
    sup |J_p(a, psi) - J_p(A_0, Psi_ref)| <= 2 delta (1 + delta) + 2 (7/15) delta + delta (1 + delta) + (17/30) delta
      = (9/2 + 3 delta) delta,
and replacing p by 1 in J_p(A_0, Psi_ref) changes it by at most (1 - p)(7/15 + 17/30) = (31/30)(1 - p) <= 31/3000.
Direct evaluation gives J_1(A_0, Psi_ref)(pi/4) = 9 sqrt(2)/40, and with sqrt(2) > 7/5,
    9 sqrt(2)/40 - (9/2 + 3/100)/100 - 31/3000 > 63/200 - 453/10000 - 31/3000 > 1/4.
Hence sup |J_p[A]|/m^2 = sup |J_p(a, psi)| > 1/4 (J_p[A] = (p + 1) Psi_p[A] A' - p Psi_p[A]' A is quadratic in A).
Theorem 3.16 gives J_p[A] = (l - 1) B_p, so (l - 1) K >= (l - 1) ||B_p||_inf/m^2 > 1/4, i.e. l > 1 + 1/(4K), which
contradicts the hypothesis on l.

### 9.13 Section 4.17 (odd perturbations of an x-even profile)
Step 1 (setting). rho_0 is in S^+_even, l > 1, p = 1/l, V_0 = lX + W[rho_0], and Phi_s is its flow. Used inputs:
rho_0 = xi^2 with xi in C^2(R^2), V_0.grad xi = xi/2, D xi(0) = (1, 0) and D xi != 0 everywhere (Theorems B (F3), 3.2
and Section 9.1, Steps 4 and 7), and Gamma = {xi = 0} is the y-axis (Theorem 3.3); with xi > 0 on x > 0, xi o R = -xi,
since xi(X) = lim e^{s/2} x(Phi_{-s} X) (Theorem B (F3)) and Phi_s o R = R o Phi_s for x-even rho_0 (Step 2).
C_1 x^2 (1 + |X|)^{p-2} <= rho_0 <= C_2 x^2 (1 + |X|)^{p-2} (Theorem 3.3); l > 1 and DV_0(0) = diag(1/2, 2l - 1/2)
(Section 9.0, Steps 3 and 4); |r^{-p} rho_0(r e_th) - A(th)| <= C r^{p-1}, |grad rho_0| <= C r^{p-1} and
|W[rho_0]| <= C r^p for large r (Theorem 3.1), and A(th) >= C_1 cos^2 th (the lower bound of Theorem 3.3 and the limit
of Theorem 3.1); V_0.X >= (l/2)|X|^2 for |X| >= R_0 (Section 9.0, Step 5); B(0) = R^2, so every backward orbit of V_0
tends to 0 (Theorem B (F3)). For h in the growth class of 4.17, Section 9.0, Steps 1-2, apply to h (they use only h in
C^3, h = O(r^2) at 0 and the growth bounds): W[h] is C^2_loc, divergence free, with curl -h_x, W[h](0) = 0 and
|W[h]| <= C(1 + r)^mu (1 + log(1 + r)).
Step 2 (reflection; lambda = 0). K(RZ) = R K(Z) for the kernel K of Section 9.0, and R e_2 = e_2. Substituting Y -> RY
in the integral gives W[h o R](X) = R W[h](RX). Since rho_0 o R = rho_0, also V_0(RX) = R V_0(X) and
grad rho_0(RX) = R grad rho_0(X), so L(h o R) = (Lh) o R. The derivative of the residual
((l + eps lambda)X + W[rho_0 + eps h]).grad(rho_0 + eps h) - rho_0 - eps h at eps = 0 is Lh + lambda X.grad rho_0, by
linearity of W. For x-odd h, Lh is x-odd and lambda X.grad rho_0 is x-even, so both vanish if their sum does (compare
the values at X and RX); X.grad rho_0 is not identically 0, so lambda = 0.
Step 3 (4.17(a)). DW[h](0) is trace free (div W[h] = 0) and symmetric (curl W[h](0) = -h_x(0) = 0).
Section 9.8, Step 1, applied to h (it uses only h in C^3, h(0) = 0, grad h(0) = 0 and the growth bounds of S) gives
pi c[h] = int h r^{-3} sin 3th dX and -pi d[h] = int h r^{-3} cos 3th dX, absolutely convergent, where
c[h] = psi_xy(0) and d[h] = psi_yy(0) for the stream function of W[h] (the same calculation as in Section 9.8, Step 1,
with psi_2 = (r^2/2)(c[h] sin 2th - d[h] cos 2th)); with W[h] = (-psi_y, psi_x),
DW[h](0) = [[-psi_xy, -psi_yy], [psi_xx, psi_xy]](0) and psi_xx(0) = -psi_yy(0) by the symmetry, which is the stated
form. Under th -> pi - th, sin 3th is even and cos 3th is odd, so c[h] = 0 for x-odd h. Along rho_0 + eps h at fixed l
(lambda = 0 by Step 2), with V_eps = lX + W[rho_0 + eps h], the strain is c(eps) = c(0) + eps c[h] with c(0) = l - 1/2
and c[h] = 0, and psi_yy(0) = eps d[h] (it is 0 for rho_0, since DV_0(0) = diag(1/2, 2l - 1/2)); so
DV_eps(0) = [[l - c(eps), -eps d[h]], [-eps d[h], l + c(eps)]]. Its smaller eigenvalue is
m1(eps) = l - (c(eps)^2 + eps^2 d[h]^2)^{1/2}; at eps = 0 it equals 1/2, is simple and has the eigenvector e_1, and
m1'(0) = -c[h] = 0. For eps d[h] != 0, e_1 is not an eigenvector of DV_eps(0). The first variation of psi_yy(0) is
d[h]. Expansion at 0: W[h] in C^2 gives W[h](X) = (-d[h] y, -d[h] x) + O(r^2), and rho_0 in C^3 with the jet gives
grad rho_0 = (2x, 0) + O(r^2); hence W[h].grad rho_0 = -2 d[h] xy + O(r^3). Further V_0 = O(r), grad h = O(r^2) and
h = O(r^3), so V_0.grad h - h = O(r^3). Thus Lh = -2 d[h] xy + O(r^3), and Lh = 0 forces d[h] = 0.
Step 4 (4.17(b): the velocity). h = chi(r) f(th) with f = cos^3 th (1 + 4 sin^2 th); the identity
cos 5th = 16 cos^5 th - 20 cos^3 th + 5 cos th gives f = (5 cos th - cos 5th)/4. Since f(pi - th) = -f(th) and f >= 0
for |th| <= pi/2, h is x-odd and nonnegative on x > 0; it is smooth because chi(r) is smooth with support in
1 <= r <= 2 and f(th) = (x/r)^3 (1 + 4 y^2/r^2) is smooth off 0. Its angular modes are cos th and cos 5th, which are
orthogonal to sin 3th and cos 3th, so c[h] = d[h] = 0. For a density a(r) cos n th with a smooth and supported in [1,
2], n >= 1, a solution of -Lap u = a(r) cos n th is u = u_n(r) cos n th with
    u_n(r) = (1/(2n)) [r^{-n} int_0^r s^{n+1} a(s) ds + r^n int_r^inf s^{1-n} a(s) ds]
(variation of constants for u'' + u'/r - n^2 u/r^2 = -a with the solutions r^n and r^{-n}, whose Wronskian is -2n/r).
Let u be the sum of the two modes for h (a = 5 chi/4 for n = 1, a = -chi/4 for n = 5), so -Lap u = h and u is smooth,
and let v = (-u_xy, u_xx), which corresponds to psi = u_x in Section 9.0, Step 1. Then div v = 0,
curl v = d_x Lap u = -h_x, and v is smooth. For r < 1, u_1(r) cos th is a multiple of x and u_5(r) cos 5th a multiple
of Re (x + iy)^5, so the second derivatives of u, and hence v, are homogeneous cubics there, and v = O(r^3) at 0. For
r > 2, u = C_n r^{-n} cos n th with C_1 = (5/8) int_1^2 s^2 chi ds and C_5 = -(1/40) int_1^2 s^6 chi ds. With
z = x + iy, r^{-n} cos n th = Re z^{-n}, so u_xx = n(n + 1) C_n Re z^{-n-2} and u_xy = -n(n + 1) C_n Im z^{-n-2}, and
    v = n(n + 1) C_n r^{-n-2} (-sin (n + 2)th, cos (n + 2)th),
    v_r = -n(n + 1) C_n r^{-n-2} sin (n + 1)th,   v_th = n(n + 1) C_n r^{-n-2} cos (n + 1)th.
So v is bounded, v(0) = 0 and v = o(|X|); by the uniqueness in Section 9.0, Step 1, v = W[h]. With D_1 = 2 C_1 and
D_5 = 30 C_5 this gives the formulas of 4.17(b). At th = -pi/4: sin 2th = -1, sin 6th = 1 and cos 2th = cos 6th = 0,
so v_th = 0 and v_r = D_1 r^{-3} - D_5 r^{-7} > 0. At th = pi/4: sin 2th = 1, sin 6th = -1, cos 2th = cos 6th = 0, so
v_th = 0 and v_r = -D_1 r^{-3} + D_5 r^{-7} < 0.
Step 5 (4.17(b): the signs). For r > 2, h vanishes near X with all derivatives, so
-Lh(X) = -v(X).grad rho_0(X) = -v_r d_r rho_0 on these rays. The profile equation gives
l r d_r rho_0 = rho_0 - W[rho_0].grad rho_0, and by the bounds of Theorem 3.1 listed in Step 1
rho_0 = r^p A(th) + O(r^{2p-1}) and W[rho_0].grad rho_0 = O(r^{2p-1}); since lp = 1,
d_r rho_0 = p r^{p-1} A(th) + O(r^{2p-2}), uniformly in th. A(+-pi/4) >= C_1/2 > 0, so d_r rho_0 > 0 on both rays for
large r, and -Lh < 0 on th = -pi/4, -Lh > 0 on th = pi/4 there.
Step 6 (4.17(b): the perturbed densities). On supp h, 1 <= r <= 2, |h| <= C|x|^3 and rho_0 >= C_1 3^{p-2} x^2 (Theorem
3.3), so |h| <= C' rho_0 there and rho_0 +- eps h >= 0 for eps <= 1/C'. Both are C^3, equal rho_0 near 0 and outside
r <= 2, so they keep the jet x^2 and the growth bounds of S; their strain moments are those of rho_0 because
c[h] = d[h] = 0. The velocity is V_0 +- eps v. Near 0, |V_0(X)| >= c_0 r (DV_0(0) is invertible) and |v| <= C r^3; for
r >= R_0, |V_0| >= l r/2 (Step 1) and v is bounded; on the compact set {r_0 <= r <= R_0}, V_0 has no zero (rho_0 in
S^+) and so |V_0| >= c_1 > 0. Hence k_0 := sup_{X != 0} |v(X)|/|V_0(X)| < inf, and for eps k_0 < 1 the field
V_0 +- eps v vanishes only at 0. Outside supp h the residual of rho_0 +- eps h is +- eps v.grad rho_0 (the terms
W[h].grad h and V_0.grad h - h vanish there), which is nonzero on the two rays for large r by Step 5; so neither
density is a profile.
Step 7 (4.17(c): boundedness and the residual map). Let h be in X_mu with norm N. Zeroth order: let r = |X| >= 4 and
split the integral of W[h](X) + (h(X)/2) e_2 into |Y| < r/2, |Y - X| < r/2, |Y| > 2r and the rest. On |Y| < r/2,
|K(X - Y)| <= C r^{-2} and |K(-Y)| <= C|Y|^{-2}, and |h(Y)| <= C N min(|Y|^3, (1 + |Y|)^mu) (the zero two-jet and
the C^3 bound on B_2 give |h| <= C N |Y|^3 on B_2); since mu > 0 the contribution is at most C N r^mu. On
|Y - X| < r/2 the principal value of K(X - Y) is taken against h(Y) - h(X) (K has zero mean on circles), with
|h(Y) - h(X)| <= C N r^{mu-1}|Y - X|, which gives C N r^mu; the K(-Y) part is at most C r^{-2} N r^mu r^2. On
|Y| > 2r, |K(X - Y) - K(-Y)| <= C r |Y|^{-3} and int_{|Y|>2r} r |Y|^{mu-3} dY = C r^mu because mu < 1. On the rest
both kernels are at most C r^{-2} on a set of area C r^2, and |h| <= C N r^mu. Hence |W[h](X)| <= C N <X>^mu for
|X| >= 4, and the same splitting with a fixed radius gives |W[h]| <= C N on |X| <= 4. Local C^2 bound: with a cutoff
zeta_0 in C_c^inf(B_2) equal to 1 on B_{3/2}, write h = zeta_0 h + (1 - zeta_0) h. W[(1 - zeta_0) h] is smooth on B_1,
and its derivatives up to order 2 there are absolutely convergent integrals bounded by C N. For the compactly
supported g = zeta_0 h in C^3, ||g||_{C^3} <= C N, the second derivatives of W[g] are the principal-value integrals
of K against D^2 g plus the local term -(D^2 g)/2 e_2. On |Y - X| < 1, D^2 g(X) is subtracted, using the zero angular
mean of K, and the Lipschitz bound |D^2 g(Y) - D^2 g(X)| <= C N |Y - X| makes this part absolutely integrable and
bounded by C N; on |Y - X| >= 1, K is integrated against D^2 g itself, whose support and supremum are bounded. The
lower derivatives and the subtraction constant in W[g] are bounded in the same way, and continuity follows from these
locally uniform integrable bounds, so ||W[g]||_{C^2(B_1)} <= C N. So ||W[h]||_{C^2(B_1)} + sup <X>^{-mu}|W[h]| <= C N.
Each term of the residual map is then in Y_mu with a bound by the norms of its factors: for factors h_1, h_2 in X_mu
with norms N_1, N_2, |W[h_1].grad h_2| <= C N_1 N_2 <X>^{2mu-1} <= C N_1 N_2 <X>^mu, |X.grad h_2| <= C N_2 <X>^mu,
|W[rho_0].grad h_2| + |W[h_1].grad rho_0| <= C (N_1 + N_2) <X>^{mu+p-1}, |X.grad rho_0| + rho_0 <= C <X>^p, and
the C^2(B_1) norms of the products are bounded by the C^3(B_2) norms of h_1, h_2, rho_0 and the C^2(B_1) norms
of W[rho_0], W[h_1]. So the residual map is a continuous polynomial of degree two, hence C^1, and it vanishes at (0,
0) since rho_0 is a profile. It commutes with h -> h o R by Step 2, and in x-odd directions (lambda = 0, Step 2) its
derivative is L, which is bounded.
Step 8 (4.17(c): the sequence and the Fredholm property). Fix X_0, e and zeta as in 4.17(c), and let n be large enough
that the disc of radius n^{-1/2} about X_0 lies in x > 0 and in B_1 minus 0; the supports of f_n and f_n o R are then
disjoint, and h_n in X_mu^odd. Derivatives of f_n of order k are sums of terms n^{-3} n^a n^{b/2} with a + b = k (a
derivatives on the sine, b on the cutoff), so ||h_n||_{C^2} <= C/n, sup |Dh_n| <= C n^{-2}, sup |h_n| <= n^{-3}, and
||h_n||_{C^3(B_2)} <= C; near X_0 the cutoff equals 1, so D^3 f_n(X_0) = -e (x) e (x) e, while f_n o R vanishes near
X_0; hence |D^3 h_n(X_0)| = 1 and ||h_n||_{C^3(B_2)} >= 1. Since h_n -> 0 uniformly with its first two derivatives,
a subsequence converging in X_mu would have the limit 0, which contradicts ||h_n||_{C^3(B_2)} >= 1; so (h_n) has no
convergent subsequence. Transport term: on supp f_n, |V_0.e| = |(V_0(X) - V_0(X_0)).e| <= C n^{-1/2}. In V_0.grad f_n
and its derivatives up to order 2, a term with all oscillatory derivatives carries the factor V_0.e, and is at most
C n^{-3} n^3 n^{-1/2}; every other term has at least one derivative on the cutoff or on V_0 and is at most
C n^{-3} (n^2 n^{1/2} + n^2) <= C n^{-1/2}. So ||V_0.grad h_n||_{C^2(B_1)} <= C n^{-1/2}, and since it has compact
support, also its weighted sup. The term h_n is O(1/n) in C^2. Nonlocal term: by Step 7 with a fixed radius,
transferring two derivatives to h_n, the C^2(B_1) norm of W[h_n] is bounded by the principal value integrals of K
against D^2 h_n, for which sup |D^2 h_n| <= C/n and the Lipschitz constant of D^2 h_n is at most C; splitting at
|Y - X| = 1/n gives C(1/n) + C(log n)/n. The weighted sup of W[h_n] is at most C(sup |h_n| + sup |Dh_n|) <= C n^{-2},
since h_n is supported in a fixed compact set away from 0 (the zeroth-order estimate of Step 7 uses only these two
quantities there). Multiplying by grad rho_0 preserves these bounds in Y_mu. Hence ||Lh_n||_{Y_mu} -> 0. The
orientation moment: g = chi(r) cos 3th is in X_mu^odd and
d[g] = -(1/pi) int_1^2 chi(r) r^{-2} dr int_0^{2pi} cos^2 3th dth = -int_1^2 chi(r) r^{-2} dr < 0, while
|d[h_n]| <= C n^{-3} n^{-1}, because the kernel r^{-3} cos 3th is bounded on the supports, of area C/n. So
h_n - (d[h_n]/d[g]) g satisfies d = 0, differs from h_n by O(n^{-4}) in X_mu, and has the same three properties. If L,
or its restriction to {d[h] = 0}, or h -> (Lh, d[h]), were Fredholm, its kernel N would be finite dimensional and its
range closed, and by the open mapping theorem the distance of h to N would be at most C times the norm of the image;
for the sequence above these distances tend to 0, so a subsequence would converge (bounded sequences in N have
convergent subsequences), a contradiction.
Step 9 (4.17(d)). Let u be a zero of H and put u_+ = (u + Ru)/2, w = (u - Ru)/2, with R the involution; w is odd and
u = u_+ + w, Ru = u_+ - w. Equivariance gives H(u_+ - w) = R H(u) = 0, so
0 = H(u_+ + w) - H(u_+ - w) = int_{-1}^1 DH(u_+ + t w) w dt. If u is close to u_0, so are u_+ and u_+ +- w (R is
bounded and Ru_0 = u_0), and continuity of DH gives ||DH(u_+ + t w) - DH(u_0)|| <= 1/(4C) for |t| <= 1. Then
2 ||DH(u_0) w|| = ||int_{-1}^1 (DH(u_0) - DH(u_+ + t w)) w dt|| <= ||w||/(2C), so ||w|| <= C ||DH(u_0) w|| <= ||w||/4,
and w = 0. For the residual map of (c), the sequence of Step 8 has ||h_n|| >= 1 and DH(0) h_n = Lh_n -> 0, so
the estimate fails.
Step 10 (4.17(e)). Let h be as in 4.17(e). By 4.17(a), d[h] = 0 and c[h] = 0, so DW[h](0) = 0, and W[h] in C^2 gives
W[h] = O(r^2) at 0. Regularity: near a point of the y-axis, xi(x, y) = x k(x, y) and h(x, y) = x m(x, y) with
k = int_0^1 xi_x(tx, y) dt in C^1 and m = int_0^1 h_x(tx, y) dt in C^2, and k(0, y) = xi_x(0, y) != 0 because
grad xi != 0 and xi_y = 0 on the axis; so eta = h/(2 xi) = m/(2k) is C^1 near the axis, and it is C^2 off the axis.
eta is even in x because h and xi are odd. At 0, m = O(r^2) because h has zero two-jet, so eta = O(r^2). Equation: on
x != 0, substitute h = 2 xi eta, rho_0 = xi^2 and V_0.grad xi = xi/2 in Lh = 0:
2 eta (xi/2) + 2 xi V_0.grad eta + 2 xi W[h].grad xi - 2 xi eta = 0, and division by 2 xi gives
(V_0.grad - 1/2) eta = -W[h].grad xi, which extends to the axis by continuity. For a continuous function g that is
differentiable along the flow, V_0.grad g(X) denotes d/ds g(Phi_s X) at s = 0; for C^1 g this is the pointwise
derivative, and solutions below are meant in this sense. Backward formula: near 0 the symmetric part of DV_0 is at
least (1/2 - delta) I (DV_0(0) = diag(1/2, 2l - 1/2)), so d|Phi_{-t} X|^2/dt <= -(1 - 2 delta)|Phi_{-t} X|^2 once
the backward orbit has entered a small disc, which it does (Step 1); hence |Phi_{-t} X| <= C_X e^{-(1/2 - delta) t}.
Take delta < 1/4. For continuous v with v = O(r^2) at 0 and grad xi bounded near 0, the integrand
e^{-s/2} (v.grad xi)(Phi_s X), s < 0, is at most C_X e^{|s|/2} e^{-(1 - 2 delta)|s|}, which is integrable since
delta < 1/4, locally uniformly in X (a compact set enters the small disc after a common time). So
eta_v(X) := -int_{-inf}^0 e^{-s/2} (v.grad xi)(Phi_s X) ds is continuous; for |X| small, |Phi_s X| <= |X|
e^{-(1/2 - delta)|s|} and the integrand is at most C|X|^2 e^{|s|/2} e^{-(1 - 2 delta)|s|}, so eta_v = O(r^2) at 0. The
substitution s -> s + t gives eta_v(Phi_t X) = -e^{t/2} int_{-inf}^t e^{-u/2} (v.grad xi)(Phi_u X) du, so eta_v is
differentiable along the flow with V_0.grad eta_v = eta_v/2 - v.grad xi. If eta_1 is another continuous solution with
eta_1 = O(r^2) (differentiable along the flow), the difference g satisfies d/ds [e^{-s/2} g(Phi_s X)] = 0, so
|g(X)| = e^{t/2} |g(Phi_{-t} X)| <= C_X e^{t/2} e^{-(1 - 2 delta) t} -> 0; hence g = 0. Applied with v = W[h], which
is continuous with v = O(r^2), this gives the formula for eta, and with h = 2 xi eta the equation eta = -B eta, with
eta in E_mu by 4.17(a) and the regularity above. Conversely, let eta be in E_mu with eta = -B eta and put
h = 2 xi eta; h is x-odd, so c[h] = 0, and W[h] is continuous with W[h] = O(r^2) at 0 (Step 1 and c[h] = d[h] = 0), so
the integral defining B eta converges and eta = eta_v with v = W[h]. Hence V_0.grad eta = eta/2 - W[h].grad xi,
pointwise since eta is C^1, and with grad rho_0 = 2 xi grad xi and V_0.grad xi = xi/2,
    Lh = 2 eta V_0.grad xi + 2 xi V_0.grad eta + 2 xi W[h].grad xi - 2 xi eta = 0,
since 2 eta V_0.grad xi = xi eta and 2 xi V_0.grad eta = xi eta - 2 xi W[h].grad xi. The open part is as stated.
Step 11 (4.17(f)). Regularity: by Section 9.0, Step 1, W[rho_0], hence V_0, is in C^{2,beta}_loc for every beta < 1,
and so is the flow (s, X) -> Phi_s X (differentiable dependence on initial data). Fix beta in (alpha, 1). Orbit chart:
since V_0(X) = DV_0(0) X + O(|X|^2) and DV_0(0) = diag(1/2, 2l - 1/2), there is delta > 0 with X.V_0(X) > 0 for
0 < |X| <= delta. Let X != 0. Its backward orbit tends to 0 (Step 1), and |Phi_s X| is strictly increasing at every s
with |Phi_s X| <= delta; so the orbit cannot enter the closed disc of radius delta from outside, and it does not stay
in that disc for all large s: otherwise |Phi_s X| would increase to a limit r_inf in (0, delta], and the omega-limit
set would be a nonempty invariant subset of the circle |Y| = r_inf, along whose orbits |Y| would be strictly
increasing. Hence every orbit in R^2 minus 0 meets the circle |Y| = delta exactly once, and
P(th, t) = Phi_t(delta e_th), with e_th = (cos th, sin th), is a bijection of (R/2 pi Z) x R onto R^2 minus 0. It is
C^{2,beta}, and DP is invertible: d_t P = DPhi_t V_0(delta e_th) and d_th P = delta DPhi_t e_th^perp (DPhi_t taken at
delta e_th) are the images under the invertible DPhi_t of two vectors that are independent because
e_th.V_0(delta e_th) > 0. So P is a C^{2,beta} diffeomorphism; write P^{-1} = (Th, T). Since
Phi_s P(th, t) = P(th, t + s), V_0.grad Th = 0 and V_0.grad T = 1; grad Th != 0, and V_0 != 0 on R^2 minus 0 (a second
zero would not lie in B(0)), so grad Th = kappa J V_0 with J(v_1, v_2) = (-v_2, v_1) and kappa continuous and
nowhere 0. T < 0 on the punctured disc of radius delta (an orbit is inside the disc before it meets the circle), so T
is bounded above on every compact set minus 0. The half plane x > 0 is invariant, since V_0(RX) = R V_0(X) (Step 2)
gives V_{0,1} = 0 on the y-axis. The sequence: V_{0,2}(s, s) = (2l - 1/2) s + O(s^2) > 0 for small s > 0. Choose a
closed rectangle Q = [th_1, th_2] x [t_1, t_2] such that P(Q) is a neighbourhood of such a point (s, s) contained in
{x > 0, V_{0,2} > 0}, a rectangle Q' = [th_3, th_4] x [t_3, t_4] in the interior of Q, and b in C_c^inf with support
in the interior of P(Q), b >= 0 and b > 0 on P(Q'). Since x > 0 is invariant, cos th > 0 on [th_1, th_2], so
th_2 - th_1 < pi and on P(Q) Th is a single-valued C^{2,beta} function with values in [th_1, th_2]. Put
phibar_n = n^{-2-alpha} b sin(n Th) on P(Q), phibar_n = 0 at the other points of x >= 0, and
phibar_n(x, y) = -phibar_n(-x, y) for x < 0; phibar_n is C^{2,beta} and x-odd, with support in P(Q) cup R P(Q). On
P(Q),
    D^2 phibar_n = n^{-2-alpha} sin(n Th) D^2 b + n^{-1-alpha} cos(n Th) M_1 - n^{-alpha} b sin(n Th) G
with G = grad Th (x) grad Th, M_1 = b D^2 Th + grad b (x) grad Th + grad Th (x) grad b in C^beta. For a in
C^beta(P(Q)), the bound |sin(n u) - sin(n u')| <= 2 n^alpha |u - u'|^alpha and the Lipschitz bound of Th give
||a sin(n Th)||_{C^alpha} <= C ||a||_{C^beta} (1 + n^alpha), and the same with cos; hence
||phibar_n||_{C^{2,alpha}} <= C. Let K_1 be a compact neighbourhood of P(Q) in x > 0 and omega_eps a radial mollifier.
Since phibar_n is C^{2,beta} with compact support, ||phibar_n * omega_eps - phibar_n||_{C^{2,alpha}} -> 0 as eps -> 0;
choose eps_n so that phi_n = phibar_n * omega_{eps_n} has support in K_1 cup R K_1 and
||phi_n - phibar_n||_{C^{2,alpha}} <= 1/n. phi_n is smooth and x-odd. Put h_n = -Lap phi_n, eta_n = h_n/(2 xi) on K_1
cup R K_1 and eta_n = 0 elsewhere. The field v_n = (-d_x d_y phi_n, d_x d_x phi_n) is smooth with compact support, div
v_n = 0, curl v_n = d_x Lap phi_n = -d_x h_n and v_n(0) = 0, so v_n = W[h_n] by the uniqueness in Section 9.0, Step 1
(W[h_n] = o(|X|) by Step 1); it vanishes near 0, so c[h_n] = d[h_n] = 0. xi is C^2 and nonzero on K_1, so eta_n is
C^2, x-even and 0 near 0, and eta_n is in E_mu. Since 1/xi is C^1 on K_1 and ||h_n||_{C^alpha} <= C, also
||eta_n||_{C^alpha} <= C; the support of eta_n meets A_r only for r in a fixed compact subinterval of (0, inf), so
||eta_n||_E <= C. The forcing: let f_n = W[h_n].grad xi = -(d_x d_y phi_n) xi_x + (d_x d_x phi_n) xi_y, and let fbar_n
be the same expression with phibar_n. Then ||f_n - fbar_n||_{C^alpha} <= C/n, both vanish outside K_1 cup R K_1, and
on x > 0
    fbar_n = n^{-alpha} g sin(n Th) + n^{-1-alpha} a_1 cos(n Th) + n^{-2-alpha} a_2 sin(n Th),
where g = b Th_x (Th_y xi_x - Th_x xi_y) and the bounded a_1, a_2 vanish, as g does, outside the support of b. With
grad Th = kappa(-V_{0,2}, V_{0,1}) and V_0.grad xi = xi/2, Th_y xi_x - Th_x xi_y = kappa V_0.grad xi = kappa xi/2, so
g = -(1/2) b kappa^2 V_{0,2} xi; hence g <= 0, and g < 0 on P(Q') because xi > 0 on x > 0. In particular
sup |f_n| <= C n^{-alpha}. The images: by 4.17(e), B eta_n(X) = int_{-inf}^0 e^{-s/2} f_n(Phi_s X) ds, and the
integral converges since f_n vanishes near 0. K_1 cup R K_1 lies in {tau_1 <= T <= tau_2} for some tau_1, tau_2. Let
K_2 be compact and T_2 = max(0, sup_{K_2 minus 0} T - tau_1). Since T(Phi_s X) = T(X) + s, the integrand vanishes for
s < -T_2, so |B eta_n| <= T_2 e^{T_2/2} sup |f_n| <= C n^{-alpha} on K_2, and B eta_n -> 0 uniformly on compact sets.
For X = P(th, t_4) with th in [th_3, th_4] the orbit stays in x > 0 and Th(Phi_s X) = th, and the substitution
u = t_4 + s gives
    B eta_n(X) = e_n + n^{-alpha} sin(n th) b_* + n^{-1-alpha} cos(n th) a_1^* + n^{-2-alpha} sin(n th) a_2^*,
with all functions on the right evaluated at th, where b_*(th) = int_{-inf}^{t_4} e^{(t_4 - u)/2} g(P(th, u)) du,
a_1^* and a_2^* are defined in the same way from a_1 and a_2 and are bounded, and e_n(th) is the same integral of
f_n - fbar_n. The integrands vanish for u < tau_1, so the Lipschitz bound of P on [th_3, th_4] x [tau_1, t_4] and
||f_n - fbar_n||_{C^alpha} <= C/n give |e_n(th) - e_n(th')| <= C n^{-1} |th - th'|^alpha. Moreover
b_*(th) <= -(t_4 - t_3) min_{P(Q')} |g| =: -c_0 < 0 for th in [th_3, th_4], since g <= 0 and the factor
e^{(t_4 - u)/2} is at least 1. For large n choose th in [th_3, th_4] with sin(n th) = 1 and th' = th + pi/n in
[th_3, th_4], so that sin(n th') = -1 and cos(n th) = cos(n th') = 0. With X = P(th, t_4) and X' = P(th', t_4) this
gives
    |B eta_n(X) - B eta_n(X')| >= n^{-alpha} (|b_*(th)| + |b_*(th')|) - C n^{-1-alpha} >= c_0 n^{-alpha},
while |X - X'| <= L pi/n, with L the Lipschitz constant of P on [th_3, th_4] x {t_4}. These points X lie in a fixed
set {r_3 <= |X| <= r_4} with r_3 > 0, and for large n both X and X' lie in A_{|X|}; so, whenever B eta_n is in E,
||B eta_n||_E >= min(1, r_4^{-q}) r_3^alpha c_0 (L pi)^{-alpha} =: c_* > 0. If a subsequence lying in E converged in E
to some F, it would converge to F uniformly on compact subsets of R^2 minus 0 (the norm of E dominates the supremum on
each A_r), so F = 0, against ||B eta_n||_E >= c_*. A compact map from E_mu cap E, with the norm of E, into E that
agrees with B there would produce such a subsequence, since ||eta_n||_E <= C; so there is no such map. The sequence of
(c): there sup |h_n| <= n^{-3} and sup |Dh_n| <= C n^{-2} (Step 8), and
|h_n(X) - h_n(X')| <= (2 sup |h_n|)^{1-alpha} (sup |Dh_n| |X - X'|)^alpha, so ||h_n||_{C^alpha} <= C n^{alpha-3}; the
supports lie in a fixed compact subset of x != 0, on which 1/xi is C^1, so ||h_n/(2 xi)||_E <= C n^{alpha-3}. The
orientation correction of Step 8 changes h_n by O(n^{-4}) times the fixed function chi(r)
cos 3th = x chi(r)(4x^2 - 3r^2)/r^3, whose quotient by 2 xi is C^1 (as in Step 10) and in E.

### 9.14 Section 2, growth gamma >= 1: subtracted laws, gauges, orbit bound, f(x) and f(x) + h(y), polynomial solution
Step 1 (hypotheses and conventions). Write X = (x, y), r = |X|, e_2 = (0, 1), and l = c_l. Throughout Steps 1-8 assume
    rho in C^3(R^2),   rho(0) = 0,   grad rho(0) = 0,
    rho_xx(0) = 2,   rho_xy(0) = rho_yy(0) = 0,
    |rho(X)| <= C(1 + r)^gamma,   |grad rho(X)| <= C(1 + r)^(gamma - 1),   1 <= gamma < 2.
A profile additionally satisfies V.grad rho = rho, where V = lX + W, W(0) = 0, div W = 0, and curl W = -rho_x. Here
curl F = d_x F^{(2)} - d_y F^{(1)} and grad-perp psi = (-psi_y, psi_x). The notation W_2 in this subsection denotes
the twice-subtracted vector field, not a second component. All bounds at infinity and all little-oh statements are
uniform in direction. Constants may depend on gamma, the density bounds, and the density near zero.
We use Section 9.0, Step 1, for the compactly supported Biot-Savart formula, its local regularity, and the fact that a
distributionally harmonic function is smooth. These are local or compactly supported facts; we do not apply the
class-S law directly to a density with gamma >= 1. The comparison with Section 9.0, Step 3, below concerns its
hypothesis on the total velocity remainder. All other arguments needed here are given in this subsection.
The kernel, its homogeneity bounds, and its circular cancellation are
    K(Z) = (-sin(2 th_Z), cos(2 th_Z))/(2 pi |Z|^2),
    |D^j K(Z)| <= C_j |Z|^(-2-j),   int_0^{2 pi} K(s cos th, s sin th) dth = 0.
The derivative bound follows by differentiating a smooth homogeneous function on the unit circle. We use circular
principal values only at the translated singularity Y = X. Terms combined inside one integral at infinity are not to
be integrated separately.
Step 2 (compact densities and the center derivative). Choose chi in C_c^inf(R^2), equal to one on |Y| <= 1 and zero on
|Y| >= 2, and put rho_R(Y) = chi(Y/R) rho(Y), with R >= 1. Let U_R denote the ordinary Biot-Savart field of rho_R and
B_R = DU_R(0). The standard compact Biot-Savart formula and Section 9.0, Step 1, give
    U_R(X) = p.v. int K(X - Y) rho_R(Y) dY - rho_R(X) e_2/2,
    div U_R = 0,   curl U_R = -(rho_R)_x,
    U_R - U_R(0) in C^{2,alpha}_loc(R^2)   for every 0 < alpha < 1.
Only U_R - U_R(0) and DU_R(0) enter below; the local term and its sign are fixed by that formula. We claim
    B_R e_j = int DK(-Y) e_j rho_R(Y) dY,   j = 1, 2.
To justify the derivative, differentiate the compact convolution in distributions and put the derivative on rho_R. The
resulting kernel expression is continuous near zero: on a small ball about its singularity, subtracting the value of
d_j rho_R leaves an integrable kernel, since this derivative is locally Lipschitz; off that ball continuity follows by
dominated convergence. Its value at zero is therefore the classical derivative of U_R. Since d_j rho_R(0) = 0, it is
    d_j U_R(0) = int K(-Y) d_j rho_R(Y) dY.
This integral is absolutely convergent near zero because d_j rho_R(Y) = O(|Y|). Integrate by parts outside |Y| = eps.
The outer boundary vanishes by compact support. The inner boundary has size at most C eps, since K = O(eps^(-2)),
rho_R = O(eps^2), and its length is 2 pi eps. Also d_{Y_j} K(-Y) = -DK(-Y) e_j. Sending eps to zero proves the claim.
The resulting integral is absolutely convergent at zero because DK(-Y) rho_R(Y) = O(|Y|^(-1)).
The divergence and curl equations at zero show that B_R is symmetric and traceless. Consequently
    W_{2,R}(X) := U_R(X) - U_R(0) - B_R X,
    W_{2,R}(X) = p.v. int [K(X - Y) - K(-Y) - DK(-Y)X] rho_R(Y) dY - rho_R(X)e_2/2
has W_{2,R}(0) = 0, DW_{2,R}(0) = 0, div W_{2,R} = 0, and curl W_{2,R} = -(rho_R)_x. Thus subtracting the derivative
at zero preserves both elliptic equations.
Step 3 (the twice-subtracted field). Define
    W_2[rho](X) := p.v. int [K(X - Y) - K(-Y) - DK(-Y)X] rho(Y) dY - rho(X)e_2/2.
For X != 0, near Y = 0 the translated kernel is smooth, while the two subtracted kernels times rho(Y) have sizes O(1)
and O(|X|/|Y|). These are integrable in two dimensions. Near Y = X choose a disk avoiding zero. Subtract rho(X) from
the translated-kernel integrand on that disk. Circular cancellation removes the constant, and the remaining absolute
integrand is bounded by C_X |X - Y|^(-1). The other terms are smooth there. At infinity, Taylor's formula gives
    |K(X - Y) - K(-Y) - DK(-Y)X| <= C |X|^2 |Y|^(-4)   for |Y| > 2|X|.
Outside a further unit disk the absolute radial majorant is C |X|^2 s^(gamma-3) ds, integrable because gamma < 2. At
X = 0 the combined kernel vanishes identically away from zero, and the local term also vanishes. This defines W_2 at
every point.
The convergence also preserves derivatives at zero, which cannot be inferred just from the pointwise cancellation. Fix
L and take R > 2L + 2. In W_2 - W_{2,R} the density difference vanishes on |Y| <= R and the local term vanishes on
|X| <= L. For the combined kernel and its first two X derivatives the bounds on this set are, respectively,
    C_L |Y|^(-4),   C_L |Y|^(-4),   C |Y|^(-4).
For the first derivative use DK(X - Y) - DK(-Y); for the second derivative use D^2 K(X - Y). Their integrals against
|rho(Y)| over |Y| > R are bounded by C_L R^(gamma-2), which tends to zero. Thus W_{2,R} -> W_2 in C^2 on every compact
set. For a fixed R > 2L + 2 the same tail is smooth on |X| <= L: every derivative of order k >= 2 has an integrable
majorant C_{k,L}|Y|^(gamma-2-k). The compact field has the regularity in Step 2, so
    W_2 in C^{2,alpha}_loc(R^2)   for every 0 < alpha < 1,
    W_2(0) = 0,   DW_2(0) = 0,   div W_2 = 0,   curl W_2 = -rho_x.
Step 4 (growth and failure of one subtraction). Let |X| = r >= 2. On |Y| > 2r the estimate in Step 3 bounds the
integral by
    C r^2 int_{2r}^inf s^(gamma-3) ds <= C_gamma r^gamma.
On |Y| < 2r first estimate the translated kernel on B(X, r/2). The entire disk lies in |Y| < 2r, so cancellation is
available on it. The gradient bound along the segment from X to Y gives |rho(Y) - rho(X)| <= C r^(gamma-1)|Y - X|.
Hence this part has size at most
    C r^(gamma-1) int_0^{r/2} ds <= C r^gamma.
On the rest of |Y| < 2r, |K(X - Y)| <= C r^(-2), the area is O(r^2), and |rho(Y)| <= C r^gamma, giving another C
r^gamma. The constant subtraction is bounded by
    C + C int_1^{2r} s^(gamma-1) ds <= C_gamma r^gamma.
Here the first constant covers the locally integrable part at zero. The linear subtraction is bounded by
    C r + C r int_1^{2r} s^(gamma-2) ds.
Finally, |rho(X)e_2/2| <= C r^gamma. Evaluating the last integral proves
    |W_2(X)| <= C r log(2 + r)   if gamma = 1,
    |W_2(X)| <= C_gamma r^gamma   if 1 < gamma < 2.
In particular W_2 = o(r^2). The constants for gamma > 1 need not remain bounded as gamma decreases to one.
Failure of absolute convergence with only one subtraction occurs for densities satisfying every stated hypothesis. To
see this for each 1 <= gamma < 2, choose a smooth radial eta equal to zero for r <= 1 and one for r >= 2, and set
    rho_*(X) = (1 - eta(r)) x^2 + eta(r) r^gamma.
This density is smooth, has the jet, and satisfies the density and gradient bounds. Direct differentiation of K gives,
for Y = s(cos th, sin th),
    DK(-Y) = (1/(pi s^3)) [[-sin(3 th), cos(3 th)], [cos(3 th), sin(3 th)]].
The matrix inside the brackets is orthogonal. Therefore, for fixed X != 0,
    |DK(-Y)X| = |X|/(pi s^3),
    K(X - Y) - K(-Y) = DK(-Y)X + E(X,Y),   |E(X,Y)| <= C|X|^2 s^(-4).
For s larger than a fixed multiple of |X| and larger than two, this implies |K(X - Y) - K(-Y)| >= |X|/(2 pi s^3). The
absolute tail integral against rho_* therefore dominates a positive constant times
    |X| int_{s_0}^inf s^(gamma-2) ds,
which diverges. This proves a failure of absolute convergence, without claiming failure for every individual density
or for every conditional truncation.
Step 5 (a harmonic growth lemma). If h is an entire scalar harmonic function and h(X) = o(|X|^m), where m >= 1 is an
integer, then h is a polynomial of degree at most m - 1. Here is the derivative estimate and its proof. The circular
mean about a point a is constant: its derivative at radius t is
    (1/(2 pi t)) int_{B(a,t)} Lap h(Y) dY = 0,
by the divergence theorem, and its limit at t = 0 is h(a). Choose a smooth radial function zeta supported in the unit
disk with integral one, and let zeta_R(Y) = R^(-2) zeta(Y/R). Integrating the circular-mean identity against its
radial weight gives
    h(a) = int zeta_R(a - Y) h(Y) dY.
This identity holds at every a. Differentiating it m times, which is justified by the smooth compact kernel, yields
    |D^alpha h(a)| <= C_alpha R^(-m) sup_{B(a,R)} |h|   for |alpha| = m.
For any eps > 0 there is R_eps such that |h(Y)| <= eps |Y|^m outside B(0,R_eps). If C_eps bounds h on that ball, then
    sup_{B(a,R)} |h| <= C_eps + eps (R + |a|)^m.
First send R to infinity in the derivative estimate and then send eps to zero. Every derivative of order m vanishes at
every a. Taylor's formula, whose order-m remainder is now zero, expresses h as its polynomial of degree at most m - 1
at the origin. This proves the lemma.
If H is a C^1 vector field with zero divergence and curl, its components satisfy, in distributions,
    Lap H^{(1)} = d_x div H - d_y curl H = 0,
    Lap H^{(2)} = d_y div H + d_x curl H = 0.
They are smooth harmonic functions by the local harmonic-distribution fact in Section 9.0, Step 1. Thus the lemma
applies to such fields component by component.
Step 6 (all subquadratic velocities and the jet). Let W be any C^1 field with the same divergence and curl as W_2,
W(0) = 0, and W = o(r^2). Then H = W - W_2 has zero divergence and curl and is o(r^2). Step 5 with m = 2 makes H
affine. Its value at zero removes the constant part. The zero divergence and curl of its linear part give
    W = W_2 + MX,   M = [[a, b], [b, -a]].
Conversely, every such M preserves the elliptic equations, centering, and o(r^2) growth. This representation is
unique, and M = DW(0) because DW_2(0) = 0. In particular, the elliptic equations alone do not fix the center strain.
For a profile, whose remainder W is a field as in the first paragraph of this Step, so that W = W_2 + MX, Taylor's
theorem and Steps 1 and 3 give
    rho(X) = x^2 + O(r^3),   grad rho(X) = (2x, 0) + O(r^2),   W_2(X) = O(r^2),
    V.grad rho = 2(l + a)x^2 + 2bxy + O(r^3).
To compare coefficients rigorously, put X = tZ in V.grad rho = rho, divide by t^2, and let t tend to zero for each
fixed Z. The resulting equality of quadratic polynomials gives l + a = 1/2 and b = 0. Hence
    M = diag(1/2 - l, l - 1/2),   DV(0) = diag(1/2, 2l - 1/2).
For a stream function of the centered field, W = (-psi_y, psi_x), the same matrix gives psi_xy(0) = l - 1/2 and
psi_xx(0) = psi_yy(0) = 0. These conclusions use transport as well as the elliptic equations, and agree with the local
compatibility in S.
Step 7 (the conditional orbit comparison). Assume in addition that W_2(X) = o(r). This assumption is separate from the
bounds in Step 4. For a profile Step 6 gives
    V(X) = AX + W_2(X),   A = diag(1/2, 2l - 1/2),   lambda = max(1/2, 2l - 1/2).
The field is locally C^1 and |V(X)| <= C(1 + |X|). The local ODE flow is complete in both time directions: integrating
|d_s |X(s)|| <= C(1 + |X(s)|) bounds each orbit on every bounded time interval, and local existence and uniqueness
then extend it across any finite endpoint. Along this flow the chain rule and transport give
    rho(Phi_s X) = e^s rho(X).
The jet supplies X_0 with rho(X_0) != 0, for example (x_0, 0) for sufficiently small nonzero x_0. Its orbit cannot
meet zero, where V vanishes, by uniqueness. Write r(s) = |Phi_s X_0|. Given eps > 0, choose C_eps so that
|W_2(X)| <= eps |X| + C_eps everywhere. Since A is symmetric,
    r'(s) <= (lambda + eps) r(s) + C_eps.
The number lambda + eps is positive. Multiplication by e^(-(lambda+eps)s) and integration from zero to s >= 0 give
    r(s) <= (r(0) + C_eps/(lambda + eps)) e^((lambda+eps)s) - C_eps/(lambda + eps).
Combining this estimate with the density bound proves
    e^s |rho(X_0)| <= C_{X_0,eps} e^(gamma(lambda+eps)s).
Taking logarithms, dividing by s, and sending s to infinity gives 1 <= gamma(lambda + eps). Since eps was arbitrary,
gamma lambda >= 1. Because gamma < 2, gamma/2 < 1; therefore lambda cannot equal 1/2. It must equal 2l - 1/2, and
    l >= 1/4 + 1/(2 gamma).
At gamma = 1 the lower bound is 3/4; for 1 < gamma < 2 it lies strictly between 1/2 and 3/4. Thus the numerical
condition leaves the interval [1/4 + 1/(2 gamma), 1] unexcluded. It constructs no profile, proves no existence for
l <= 1, and makes no assertion that the bound is optimal for the coupled equations. The total remainder here is
W = W_2 + MX. Its sublinearity, used in Section 9.0, Step 3, for Theorem A, is not supplied by sublinearity of W_2 or
by Step 4. No inference of this lower bound is made here without the extra hypothesis W_2 = o(r).
Step 8 (exclusion of layers and additive separation). First let rho(x,y) = f(x). Its jet gives f(0) = f'(0) = 0 and
f''(0) = 2. The field F(x,y) = (0, -f(x)) satisfies div F = 0, curl F = -rho_x, F(0) = 0, DF(0) = 0, and F = o(r^2),
by the density bound. Step 6 applied to F shows F = W_2 + NX for a constant symmetric traceless N. Differentiating at
zero gives N = 0. Consequently W_2 = (0, -f(x)). For a profile the forced M in Step 6 reduces transport to
    (x/2) f'(x) = f(x).
For x != 0 this is equivalent to
    d_x(f(x)/x^2) = (x f'(x) - 2f(x))/x^3 = 0.
Thus f(x) = C_+ x^2 on x > 0 and f(x) = C_- x^2 on x < 0. The jet gives f(x)/x^2 -> 1 on both sides of zero, so
C_+ = C_- = 1 and f = x^2 everywhere. This contradicts |f(x)| <= C(1 + |x|)^gamma with gamma < 2.
Now let rho(x,y) = f(x) + h(y). Constants can be reassigned between the two functions so that f(0) = h(0) = 0. They
are then the restrictions rho(x,0) and rho(0,y), and are C^3 with the corresponding growth bounds. The jet gives
f'(0) = h'(0) = 0, f''(0) = 2, and h''(0) = 0. Again F = (0, -f(x)) has the elliptic data of rho, zero value and
derivative at zero, and is o(r^2). The same argument gives W_2 = F without a separate inverse for h. Transport is
    (x/2) f'(x) + ((2l - 1/2)y - f(x)) h'(y) = f(x) + h(y).
At y = 0, h(0) = h'(0) = 0 reduces this to the preceding ODE, so f = x^2. Restriction of the density bound to y = 0 is
again contradicted. This proves both exclusions for all real l in the stated velocity class. It does not decide
existence for general two-variable densities.
The distinction between the growth bounds and sublinearity can also be witnessed by smooth densities. For any
1 <= gamma < 2 put
    f_gamma(x) = x^2 (1 + x^2)^((gamma-2)/2),
    f_gamma'(x) = x(2 + gamma x^2)(1 + x^2)^((gamma-4)/2).
These formulas give f_gamma = x^2 + O(x^4) near zero, |f_gamma(x)| <= C(1 + |x|)^gamma, and
|f_gamma'(x)| <= C(1 + |x|)^(gamma-1), by separating |x| <= 1 and |x| >= 1. Since gamma - 1 >= 0, these imply the
full-plane bounds for rho(x,y) = f_gamma(x). The elliptic argument above gives W_2 = (0, -f_gamma(x)), whose size on
the x-axis is asymptotic to |x|^gamma. It is not o(r). Nor can any added MX make the total field sublinear:
    (W_2 + MX)(t,0) + (W_2 + MX)(-t,0) = (0, -2f_gamma(t)).
If both terms on the left were o(t) as t tends to infinity, so would be the right side, whereas f_gamma(t)/t tends to
one for gamma = 1 and to infinity for gamma > 1. These examples are densities obeying the elliptic law, not profiles.
Step 9 (higher growth and a cutoff inverse). Now let n >= 2 be an integer, assume n <= gamma < n + 1, and retain the
C^3 regularity, the jet, and both density and gradient bounds of Step 1 with this value of gamma. Choose eta in
C^inf(R^2), radial, zero on |Y| <= 1 and one on |Y| >= 2. For Y != 0 define the homogeneous Taylor terms
    P_j(X,Y) = D^j K(-Y)[X, ..., X]/j!,   j >= 1.
The centered inverse obtained by subtracting through degree n at infinity is
    W^{[n]}(X) = p.v. int [K(X - Y) - K(-Y) - eta(Y) sum_{j=1}^n P_j(X,Y)] rho(Y) dY - rho(X)e_2/2.
The constant term is subtracted globally to center the velocity; its product with rho is integrable near zero. This is
also what results by cutting off the entire degree-n Taylor polynomial at infinity and then subtracting the value of
that field at zero. The cutoff avoids a singularity in the higher derivative terms at zero: already D^2 K(-Y) rho(Y)
is bounded only by C |Y|^(-2) there, whose absolute radial majorant is logarithmically divergent.
For |Y| > max(2|X|, 2), Taylor's formula gives the bound on the combined kernel
    C_n |X|^(n+1) |Y|^(-n-3).
Its absolute radial majorant after multiplication by rho is C_n |X|^(n+1) s^(gamma-n-2) ds, integrable because
gamma < n + 1. Near Y = X the cancellation argument in Step 3 applies, and near Y = 0 the higher terms vanish by the
cutoff. At X = 0 the formula gives W^{[n]}(0) = 0.
Each P_j, as a polynomial vector field in X, has zero divergence and curl. Indeed div_X K(X - Y) = curl_X K(X - Y) = 0
near X = 0 when Y != 0, as follows directly from the formula for K. Differentiating its Taylor polynomial gives, for
j >= 1,
    div_X P_j(X,Y) = D^(j-1)(div K)(-Y)[X, ..., X]/(j-1)! = 0,
    curl_X P_j(X,Y) = D^(j-1)(curl K)(-Y)[X, ..., X]/(j-1)! = 0.
For rho_R as in Step 2 the displayed inverse is U_R - U_R(0) minus a polynomial obtained by integrating eta P_j rho_R.
These coefficient integrals are finite, and the polynomial has zero divergence and curl. Thus the compact inverse has
the required elliptic equations. On a fixed disk |X| <= L, for R > 2L + 2, its tail difference from W^{[n]} and its
first two derivatives are bounded by
    C_{n,L} int_R^inf s^(gamma-n-2) ds = C_{n,L,gamma} R^(gamma-n-1).
For derivatives of order k <= n + 1 use the Taylor remainder of D^k K, of order n + 1 - k; for k = n + 1 use
|D^(n+1)K| directly. Higher derivatives have the integrable majorants C_{k,L}|Y|^(gamma-2-k). The tail is therefore
smooth locally. Passing to the limit as in Step 3 gives W^{[n]} in C^{2,alpha}_loc for every 0 < alpha < 1 and
    div W^{[n]} = 0,   curl W^{[n]} = -rho_x,   W^{[n]}(0) = 0.
For completeness, this inverse has the velocity growth needed for the claimed ambiguity. Let r = |X| >= 2. The tail
|Y| > 2r is bounded by
    C_n r^(n+1) int_{2r}^inf s^(gamma-n-2) ds <= C_{n,gamma} r^gamma.
The translated kernel, constant subtraction, and local density term are each O(r^gamma), by the estimates in Step 4,
which apply for every gamma >= 1. The j-th cutoff term on |Y| < 2r is bounded by
    C_j r^j int_1^{2r} s^(gamma-j-1) ds.
If gamma > n, every gamma - j is positive, and all these quantities are O(r^gamma). If gamma = n, the terms j < n are
O(r^n), while j = n is O(r^n log(2 + r)). Hence
    |W^{[n]}(X)| <= C r^n log(2 + r)   if gamma = n,
    |W^{[n]}(X)| <= C r^gamma   if n < gamma < n + 1.
In either case W^{[n]} = o(r^(n+1)).
Step 10 (the exact higher harmonic ambiguity). Suppose W is C^1, has the same divergence and curl as W^{[n]}, is
centered by W(0) = 0, and satisfies W = o(r^(n+1)). Then H = W - W^{[n]} is centered, has zero divergence and curl,
and is o(r^(n+1)). Step 5 with m = n + 1 makes its components polynomials of degree at most n. Define
    Q(x,y) = int_0^x H^{(2)}(s,0) ds - int_0^y H^{(1)}(x,t) dt.
This is a polynomial of degree at most n + 1. It has Q(0) = 0 and Q_y = -H^{(1)}. Using div H = 0 gives
    Q_x(x,y) = H^{(2)}(x,0) + int_0^y d_t H^{(2)}(x,t) dt = H^{(2)}(x,y).
Thus H = grad-perp Q, and Lap Q = curl H = 0. Centering gives grad Q(0) = 0, so Q has no linear term; its constant has
already been set to zero. In its homogeneous decomposition, the Laplacians of distinct degrees have distinct degrees,
so each homogeneous part is harmonic separately. The only possible effective stream degrees are therefore
    2, 3, ..., n + 1.
Conversely, adding grad-perp Q for any harmonic polynomial with only these degrees preserves centering and both
elliptic equations, and its velocity is O(r^n) = o(r^(n+1)). This proves that the list gives exactly the ambiguity,
not just a collection of examples. Each degree k has two real parameters: writing its homogeneous part as r^k q(th),
harmonicity gives q'' + k^2 q = 0, so it is a linear combination of Re(x + iy)^k and Im(x + iy)^k. Changing the cutoff
is included in this ambiguity. These statements concern the elliptic inverse; an arbitrary harmonic addition need not
preserve transport for a fixed density. Without centering, a constant velocity, equivalently a linear stream term,
would also remain.
Step 11 (the radially truncated integral for x^2). The growth-two example requires its own normalization calculation.
Let R > 0 and let F_R denote the Newtonian potential of the sharply truncated density Y_1^2 1_{|Y|<R}:
    F_R(X) = -(1/(2 pi)) int_{|Y|<R} log|X - Y| Y_1^2 dY.
It satisfies -Lap F_R = x^2 on |X| < R. We compute it there, including the terms that centering will remove. Put
e_th = (cos th, sin th). For 0 < r < R and s != r, expansion of the logarithm gives
    log|r e_th - s e_phi| = log b - sum_{k=1}^inf (a/b)^k cos(k(th - phi))/k,
    a = min(r,s),   b = max(r,s).
For a/b < 1 this follows by taking the real part of the power series for log(1 - z); the series converges absolutely.
Integration against cos^2 phi selects only modes zero and two, and yields
    (1/(2 pi)) int_0^{2 pi} log|r e_th - s e_phi| cos^2 phi dphi = (1/2) log b - (1/8)(a/b)^2 cos(2 th).
The original logarithmic kernel is locally integrable on the bounded integration region, so Fubini applies; the
exceptional radius s = r has measure zero. Splitting the radial integral at s = r therefore gives
    F_R(r e_th) = -(1/2) I_0(r) + (cos(2 th)/8) I_2(r),
    I_0(r) = (r^4/4) log r + int_r^R s^3 log s ds,   I_2(r) = r^(-2) int_0^r s^5 ds + r^2 int_r^R s ds.
Using the antiderivatives s^4 log s/4 - s^4/16, s^6/6, and s^2/2 in this order, one obtains
    F_R(X) = C_R + R^2(x^2 - y^2)/16 - (x^2 + y^2)^2/32 - (x^4 - y^4)/24,
    C_R = -R^4 log R/8 + R^4/32.
The identity extends to X = 0 by continuity. Since -Lap F_R equals the truncated density distributionally, its
ordinary velocity is U_R = grad-perp d_x F_R. Equivalently this is the compact Biot-Savart formula, obtained by
differentiating the same Newtonian kernel. Its use with a sharp boundary is justified by smooth radial cutoffs
approaching the disk indicator. On every smaller disk the approximating densities equal x^2, and the differences are
supported in a shrinking annulus separated from that disk. The derivatives of the Newtonian kernel and K are bounded
on these separated sets, so the potential derivatives and velocity formulas converge locally there. Inside the disk
the explicit expression is
    d_x F_R = R^2 x/8 - (7x^3 + 3xy^2)/24,
    U_R(X) = (xy/4, R^2/8 - (7x^2 + y^2)/8),   U_R(0) = (0, R^2/8),   DU_R(0) = 0.
The centered stream is d_x F_R - R^2 x/8. Consequently, for every |X| < R, both centering alone and centering with a
derivative subtraction give the R-independent field
    psi_circ(X) = -(7x^3 + 3xy^2)/24,
    W_circ(X) = (xy/4, -(7x^2 + y^2)/8).
More explicitly, the radially truncated twice-subtracted expression is
    p.v. int_{|Y|<R} [K(X - Y) - K(-Y) - DK(-Y)X] Y_1^2 dY - x^2 e_2/2 = W_circ(X)   for |X| < R.
Indeed the first two terms center U_R, and the derivative subtraction integrates to zero: DK is odd, Y_1^2 is even,
and their product is absolutely integrable near zero on this finite disk. Thus the limit as R tends to infinity is
precisely W_circ. This construction specifies a radial truncation, not an assertion of absolute convergence at growth
two.
Step 12 (the cubic correction and the polynomial solution). Define the two added stream terms
    Q_3(X) = -(x^3 - 3xy^2)/24,   Q_2(X) = (l - 1/2)xy.
They are harmonic: Lap(x^3) = 6x and Lap(3xy^2) = 6x, while Lap(xy) = 0. Their velocity contributions and the
corrected stream are
    grad-perp Q_3 = (-xy/4, (-x^2 + y^2)/8),
    grad-perp Q_2 = ((1/2 - l)x, (l - 1/2)y),
    psi_circ + Q_3 + Q_2 = -x^3/3 + (l - 1/2)xy.
The cubic correction cancels the horizontal quadratic velocity and changes the vertical quadratic velocity to -x^2.
With rho = x^2 and psi equal to the last display, one has
    W = grad-perp psi = ((1/2 - l)x, (l - 1/2)y - x^2),
    W(0) = 0,   V = lX + W = (x/2, (2l - 1/2)y - x^2),
    div W = (1/2 - l) + (l - 1/2) = 0,
    curl W = -2x = -rho_x,   -Lap psi = 2x = rho_x,
    V.grad rho = (x/2)(2x) = x^2 = rho.
The density has the required jet, |rho| <= r^2 and |grad rho| <= 2r; the velocity is O(r^2), hence o(r^3). All
identities hold globally for every real l, without a sign restriction. Step 10 with n = 2 places this field in the
allowed quadratic and cubic harmonic gauge class relative to any centered cutoff inverse of Step 9.
The cubic addition cannot be replaced by an affine strain alone. For any symmetric traceless M = [[a, b], [b, -a]],
the field W_circ + MX would give
    (lX + W_circ + MX).grad(x^2) = 2(l + a)x^2 + 2bxy + x^2 y/2.
The cubic term x^2 y/2 cannot agree with the purely quadratic right side x^2. Thus the polynomial solution requires
the indicated higher harmonic gauge; with the radial inverse and only a free linear velocity added, x^2 does not solve
the profile equation. The polynomial solution has growth 2 and is not in S; in the sense of Proposition 2.1 it is a
truncation (gauge) artifact. The results for 1 <= gamma < 2 prove the two specified exclusions and the conditional
necessary bound, without establishing general existence or general nonexistence. The growth-two construction concerns
the explicitly allowed elliptic gauge and does not select that gauge by an outer-flow matching condition. No assertion
of such selection or exclusion is made here.

### 9.15 Theorem 4.9, Corollary 4.10 and Remark 4.11 (the regime c_l -> infinity)
Step 1 (hypotheses, normalization and rescaling). Throughout, a profile in S has the hypotheses of Sections 1 and 2.
Explicitly, rho is C^3 on R^2, rho(0) = 0, grad rho(0) = 0 and D^2 rho(0) = diag(2, 0), and for some C_rho > 0 and
gamma_rho in [0, 1),
    |rho(X)| <= C_rho (1 + |X|)^{gamma_rho},
    |grad rho(X)| <= C_rho (1 + |X|)^{gamma_rho - 1}.
Its velocity is the canonical once-subtracted law, and it solves V.grad rho = rho with V = l X + W[rho]. Theorem A and
Section 9.0, Steps 1-4, give l > 1, p = 1/l in (0, 1), the divergence and curl of W, and the matrix DV(0). Different
profiles may have different C_rho and gamma_rho. No sign condition on rho is imposed. All local convergence below is
on every compact subset of the full plane.
Here and below curl v means d_x v_2 - d_y v_1. Write e_2 = (0, 1), Z = (z_1, z_2) = (x, y), r = |Z| and th = arg Z.
For a density g with this jet and growth the canonical law is
    K(Z) = (-sin(2 th), cos(2 th))/(2 pi r^2),
    W[g](X) = p.v. int_{R^2} [K(X - Y) - K(-Y)] g(Y) dY - (g(X) - g(0)) e_2/2.
For a density g with the regularity, growth and jet of S, define
    phi(Z) = r^{-3} sin(3 th),
    c[g] = psi[g]_{xy}(0) = (1/pi) int_{R^2} g(Z) phi(Z) dZ,
    Q[g] = int_{R^2} g W[g].grad phi dZ,   kappa[g] = Q[g]/(pi c[g]^2)   if c[g] != 0.
The stream function here satisfies W[g] = (-psi[g]_y, psi[g]_x). Its additive constant does not affect c[g]. These are
the strain and shape functional of Theorem C; the integral identities and absolute convergence are proved in Section
9.8, Steps 1-2. In particular, for a profile,
    c[rho] = l - 1/2,   Q[rho] = pi c[rho](c[rho] - 1/2).
Set f_p(Z) = p^2 rho(Z/p). This density is again in S, with constants that may depend on p. In the once-subtracted
integral, substitute Y = p X and use K(p X) = p^{-2} K(X). The principal-value balls scale with the same substitution,
and the local term scales by p^2. Thus
    w_p(Z) = W[f_p](Z) = p^2 W[rho](Z/p),
    b_p(Z) = Z + w_p(Z) = p^2 V(Z/p).
The chain rule, applied at X = Z/p, gives
    grad f_p(Z) = p grad rho(X),   Db_p(Z) = p DV(X),
    b_p.grad f_p = p^3 V.grad rho = p f_p,
    div b_p = p div V = 2,   curl b_p = p curl V = -d_x f_p,
    b_p(0) = 0,   f_p(0) = 0,   grad f_p(0) = 0,   D^2 f_p(0) = diag(2, 0),
    f_p(Z) = z_1^2 + O_p(|Z|^3),   Db_p(0) = diag(p/2, 2 - p/2).
One may take psi[f_p](Z) = p^3 psi[rho](Z/p), up to an additive constant. Also phi has degree -3 and grad phi has
degree -4. Changing variables in the defining integrals therefore gives
    c[f_p] = p c[rho] = 1 - p/2,
    Q[f_p] = p^2 Q[rho] = pi (1 - p/2)(1 - p),
    kappa[f_p] = kappa[rho] = (1 - p)/(1 - p/2).
The remainder O_p in the jet need not be uniform in p. The density f_p satisfies the rescaled transport equation with
right side p f_p; it need not be a profile with right side f_p.
Step 2 (the limit and the local nullclines). Assume the hypotheses of Theorem 4.9: rho_n are profiles in S, p_n -> 0,
f_n = f_{p_n} -> f in C^2_loc and b_n = b_{p_n} -> b in C^1_loc. Step 1 and these convergences imply
    b.grad f = 0,   div b = 2,   curl b = -f_x,   b(0) = 0,
    f(0) = 0,   grad f(0) = 0,   D^2 f(0) = diag(2, 0),   Db(0) = diag(0, 2).
Taylor's theorem for the C^2 function f gives f(Z) = z_1^2 + o(|Z|^2). These are local differential conclusions.
Identification of b - Z with the canonical integral of f requires an additional argument; Steps 9 and 12 supply it
under the hypotheses of part (b) and of Corollary 4.10, respectively.
Convergence in C^1 on compact sets implies that the family Db_n, together with Db, is equicontinuous on a fixed small
closed disk. Finite initial portions of the sequence cause no difficulty. Since d_y b_{n,2}(0) = 2 - p_n/2 > 3/2 and
d_y b_2(0) = 2, a common rectangle about 0 has d_y b_{n,2} >= 1 and d_y b_2 >= 1. Moreover b_{n,2}(0) = d_x
b_{n,2}(0) = 0, so
    |b_{n,2}(x, 0)| <= omega(|x|) |x|,   omega(t) -> 0 as t -> 0,
with omega independent of n; the same bound holds for b_2. Strict monotonicity in y and the intermediate value theorem
give unique roots y = h_n(x) and y = h(x) on a common interval |x| < delta. Indeed, at y = +-2 omega(|x|)|x| the two
signs bracket zero; the case omega(|x|) = 0 has root y = 0. Shrinking delta keeps these points in the rectangle. The
implicit-function theorem gives C^1 graphs and
    h_n(0) = h_n'(0) = h(0) = h'(0) = 0,
    |h_n(x)| <= 2 omega(|x|)|x|,   h_n'(x) = -d_x b_{n,2}(x, h_n(x))/d_y b_{n,2}(x, h_n(x)).
Thus h_n(x) = o(|x|) and h_n'(x) = o(1), uniformly in n. The corresponding statements hold for h. The lower bound on
d_y b_{n,2}, local uniform convergence of b_n, and the displayed derivative formula also give h_n -> h in C^1 on each
smaller closed interval. All nullcline assertions concern this common neighborhood; no global graph assertion is made.
Step 3 (zeros and the uniform longitudinal speed). The family D^2 f_n is equicontinuous near 0 and has the common
value diag(2, 0) there. Taylor's formula, the common value and gradient at 0, and the uniform estimate h_n(x) = o(|x|)
imply
    f_n(x, h_n(x)) = x^2 + o(x^2),
    d_x f_n(x, h_n(x)) = 2x + o(|x|),
uniformly in n as x -> 0. Here d_x denotes the partial derivative, not differentiation along the graph. The same
formulas hold for f and h. For sufficiently small nonzero x the second expression is nonzero, and f(x, h(x)) > 0.
Restriction of the transport equation to b_{n,2} = 0 gives
    b_{n,1}(x, h_n(x)) d_x f_n(x, h_n(x)) = p_n f_n(x, h_n(x)),
    b_{n,1}(x, h_n(x)) = (p_n x/2)(1 + eps_n(x)),
    eps_n(x) = 2 f_n(x, h_n(x))/(x d_x f_n(x, h_n(x))) - 1.
Set eps_n(0) = 0. The uniform Taylor estimates show that this is continuous at 0 and
    sup_n sup_{0 < |x| <= t} |eps_n(x)| -> 0   as t -> 0.
For the limit, b_2(x, h(x)) = 0 and b_1(x, h(x)) f_x(x, h(x)) = 0. Hence b(x, h(x)) = 0 for 0 < |x| < delta, and also
at x = 0. For any fixed nonzero x in this interval, put z = (x, h(x)). If z_j were zeros of b_{n_j}, with
n_j -> infinity and z_j -> z, Step 1 would give f_{n_j}(z_j) = 0. Local uniform convergence would imply f(z) = 0, a
contradiction. Thus the positive-density zeros on this punctured arc cannot be limits of zeros of the approximating
fields. The origin is excluded from this assertion: b_n(0) = 0 for every n. This proves part (a), with its uniformity
and local scope explicit.
Step 4 (outward flow and the range of f). For the rest of part (b), assume in addition the directional uniform
sublinearity stated there:
    sup_{|Z| = r} |b(Z) - Z|/r -> 0   as r -> infinity.
Choose R > 1 such that
    Z.b(Z) >= |Z|^2/2   for |Z| >= R.
The C^1 field b has at most linear growth, so its flow is complete: on any finite time interval the inequality
|b(Z)| <= C(1 + |Z|) and Gronwall's inequality prevent escape to infinity, and local uniqueness and continuation
apply. Every backward orbit remains in the disk of radius max(R, |Z|). An orbit starting outside B_R reaches its
boundary in backward time at most 2 log(|Z|/R), because its radius decreases at rate at least half that radius while
it is outside. The disk is backward invariant by the strict inward direction of -b on its boundary.
The identity b.grad f = 0 makes f constant on every orbit. Consequently every value of f is already attained on the
compact disk with radius R. Thus f is bounded and attains both its maximum and its minimum. Write M = max f. The jet
gives f(x, 0) = x^2 + o(x^2) > 0 for sufficiently small nonzero x, so M > 0. This uses no global sign condition and no
positivity theorem for the approximating profiles. The zero set E = {b = 0} is closed and contained in B_R, hence
compact.
Step 5 (regular level components and their unique zeros). Let a be a regular value of f with a nonempty inverse image.
This means grad f != 0 at every point of {f = a}. The implicit-function theorem makes this inverse image a C^2
one-dimensional manifold without boundary. A connected component C is closed in the plane, since {f = a} is closed and
its components are closed. On a neighborhood of C where grad f != 0, put
    g = |grad f|,   J(u, v) = (-v, u),   T = J grad f/g.
The unit field T is C^1 and tangent to C. Its integral curves on C extend for all arclength times: over a finite time
interval their speed is one, and any finite endpoint belongs to the closed set C, where the local existence theorem
continues the curve. Each orbit is relatively open in C, so connectedness makes C one orbit. If this orbit repeats a
point, uniqueness gives a periodic orbit, and C is a simple closed C^2 curve. Otherwise its arclength parametrization
z: R -> C is an injective surjective local diffeomorphism, hence a homeomorphism and a C^2 embedding. Since C is
closed, that embedding is proper: the inverse image of a compact plane set is compact.
A closed component would bound a bounded Jordan domain D of positive area. The field b is tangent to its boundary by
b.grad f = 0, and Green's theorem would give
    0 = int_{boundary D} b.n ds = int_D div b dZ = 2 |D| > 0.
Thus every component is a properly embedded line. On the regular neighborhood define the C^1 scalar
    lambda = (b.J grad f)/g^2,   b = lambda J grad f.
The second equality follows because b is orthogonal to grad f. Since div(J grad f) = 0, one has
    (J grad f).grad lambda = 2,
    d/ds lambda(z(s)) = 2/g(z(s)) > 0.
This proves that C has at most one zero of b. To prove existence, properness gives |z(s)| -> infinity at both ends
s -> +-infinity. On the sufficiently negative tail, where |z(s)| > R, the radius has a point with negative derivative:
otherwise it could not decrease from arbitrarily large radii to any fixed point on that tail. The mean value theorem
makes this argument precise by taking two such points with decreasing radii. Similarly the sufficiently positive tail
has a point with positive radial derivative. With r(s) = |z(s)|, the outward inequality and b = lambda g T give on
both tails
    0 < z(s).b(z(s)) = lambda(z(s)) g(z(s)) r(s) r'(s).
Thus lambda takes a negative and a positive value. It has exactly one zero by continuity and strict monotonicity. The
arclength speed v = lambda g satisfies v' = 2 at that zero, which gives the speed assertion without assuming any
unproved transverse derivative identity.
Step 6 (the Sard statement at C^2 regularity). The version of the Morse-Sard theorem needed here is that critical
values of a C^2 map from R^2 to R have one-dimensional Lebesgue measure zero. The differentiability threshold in these
dimensions is k > 2 - 1, so k = 2 suffices. For completeness, it has the following direct proof.
First, for a C^1 function u on an interval, its critical values have measure zero. On a compact subinterval, divide
into intervals of length at most d. If one meets {u' = 0}, uniform continuity of u' bounds |u'| throughout that
interval by a modulus omega(d) tending to zero. Its image has length at most d omega(d). There are O(d^{-1})
intervals, so the outer measure of the critical values is zero. An exhaustion by compact subintervals proves the
assertion on the original interval.
For f, split its critical set into points where D^2 f != 0 and points where D^2 f = 0. Near a point of the first kind,
some first derivative f_i has nonzero gradient. Its zero set is a C^1 graph containing the critical points in that
neighborhood. Restrict f to a C^1 parametrization of this graph. Every critical point of f is a critical point of this
restriction, so its image has measure zero by the preceding one-dimensional assertion. A countable collection of these
neighborhoods suffices, since the plane is second countable.
For points of the second kind in a fixed closed disk B_N, use a square grid of side d < 1. In each square meeting this
set choose a point q with grad f(q) = 0 and D^2 f(q) = 0. Uniform continuity of D^2 f on B_{N+2} and Taylor's integral
formula give, throughout that square,
    |f(z) - f(q)| <= C d^2 omega_N(C d),   omega_N(t) -> 0   as t -> 0.
Only O_N(d^{-2}) squares meet B_N. Their images of the critical set are covered by intervals of total length at most
C_N omega_N(C d), which tends to zero. Exhaustion in N completes the proof. In particular, every nonempty real
interval contains values that are not critical values of f.
Step 7 (a maximizing equilibrium and the rate obstruction). The range of f contains [0, M], by continuity along a
segment from 0 to a point where f = M. Using Step 6, choose regular values a_j in (0, M) with a_j -> M. Each level is
nonempty. By Step 5, any chosen component contains a zero q_j of b. All q_j belong to the compact set E from Step 4,
so a subsequence converges to q in E. Continuity gives f(q) = M, and the differentiability of f at its global maximum
gives grad f(q) = 0.
Since f_n(q) -> M > 0, for all sufficiently large n the exact rescaled equation yields
    (M/2) p_n <= p_n f_n(q) = b_n(q).grad f_n(q),
    b_n(q).grad f_n(q) = (b_n(q) - b(q)).(grad f_n(q) - grad f(q)),
    |b_n(q) - b(q)| |grad f_n(q) - grad f(q)| >= (M/2) p_n.
Both errors tend to zero. Dividing this inequality by either error shows, more precisely, that each error divided by
p_n tends to infinity. In particular neither error is O(p_n), and a regular first-order expansion in p at this point
is impossible.
Step 8 (the failure of real analyticity). Suppose, for contradiction, that b is real-analytic on the plane. Let E' be
the set of accumulation points of E = {b = 0}. It is a closed subset of the compact set E and is nonempty by the arc
in Step 3. At every point of E, tr Db = 2, so Db has rank at least one. At a point of E' its rank cannot be two, since
the inverse-function theorem would make that zero isolated. Thus its rank is one.
Fix q in E'. Some component of b has nonzero differential at q. The analytic implicit-function theorem expresses the
zeros of that component near q as one analytic graph. The other component restricted to the graph is a real-analytic
function of one variable. Zeros of b distinct from q accumulate at q, so the one-variable identity theorem makes this
restricted function identically zero on a smaller interval. Hence E near q is exactly an open analytic arc, every
point of which belongs to E'. This also excludes isolated zeros accumulating beside such an arc.
It follows that E' is a nonempty compact embedded one-dimensional manifold without boundary. A connected component is
a circle by the classification of connected one-dimensional manifolds. It is an embedded smooth Jordan curve, and b
vanishes on it. Green's theorem on its bounded interior gives the same contradiction 0 = 2 |D| as in Step 5. Therefore
b is not real-analytic. The rank argument is essential: compact analytic zero sets are not being assumed nonsingular
without proof. Steps 4-8 prove the dynamical, geometric and rate assertions of part (b); Step 9 proves the canonical
velocity identity and completes part (b).
Step 9 (identifying the canonical velocity under part (b)). This step also justifies the canonical-law interpretation
of the limit under the additional sublinearity assumption. We use the boundedness of f from Step 4, not the growth
bounds of an unproved limiting member of S. Put w = b - Z. The once-subtracted expression
    B[f](X) = p.v. int_{R^2} [K(X - Y) - K(-Y)] f(Y) dY - f(X) e_2/2
is well-defined. Near 0 the subtracted term is integrable because f(Y) = O(|Y|^2); near Y = X, subtract f(X) in the
singular kernel and use local C^1 regularity and its zero angular mean. At infinity, boundedness of f and the bound
C|X||Y|^{-3} give absolute convergence.
Here is a growth argument that avoids any assumed decay of grad f. Choose a smooth radial cutoff chi equal to one on
B_2 and zero outside B_4, put f_R(Y) = chi(Y/R) f(Y), and let U_R be the usual compact-source velocity. The kernel and
distribution identities in Section 9.0, Step 1, also hold for C^2 compactly supported densities: mollification
converges in C^1, which passes through the local principal values by the zero angular mean and the first-derivative
estimate. The kernel difference at infinity then gives, for R >= 1,
    sup_{|X| <= R} |B[f](X) - (U_R(X) - U_R(0))| <= C ||f||_inf.
For each fixed compact set the same tail estimate is O(R^{-1}), so the cutoff velocities converge locally uniformly to
B[f]. Consequently B[f] is continuous, B[f](0) = 0, and its divergence and curl are 0 and -f_x in distributions. At 0,
direct integration using the quadratic vanishing inside B_1 and boundedness outside gives
    |U_R(0)| <= C_f (1 + log R).
The Fourier multiplier of the compact-source velocity is
    (xi_1 xi_2, -xi_1^2)/|xi|^2,
whose Euclidean norm is at most one. Plancherel's theorem therefore gives
    ||U_R||_{L^2(R^2)} <= ||f_R||_{L^2(R^2)} <= C R ||f||_inf.
Cauchy-Schwarz on B_R, the preceding pointwise tail bound and the estimate at 0 imply
    (1/|B_R|) int_{B_R} |B[f]| dX <= C_f (1 + log R).
Each component of H = w - B[f] is a harmonic distribution, since its divergence and curl vanish; Weyl's lemma makes it
a smooth harmonic function. The sublinearity of w and the last estimate give
    (1/|B_R|) int_{B_R} |H| dX = o(R).
For a harmonic function, differentiating its mean-value identity with a smooth radial averaging kernel supported in
B(a, R) gives
    |grad H_j(a)| <= C R^{-3} int_{B(a,R)} |H_j(X)| dX.
For fixed a the right side tends to zero by the averaged bound on B_{R+|a|}. Hence H is constant, and H(0) = 0 makes
it zero. Thus w = B[f] = W[f], where W here denotes the same integral extended to this bounded C^2 density. This does
not assert that f belongs to S. The identification uses divergence, curl and growth; it does not assume uniform
absolute tails for the sequence f_n.
Step 10 (escape of the strain). For part (c), suppose f_n -> z_1^2 in C^2_loc. For every fixed R > 0 the strain
integrals of f_n are absolutely convergent by Step 1. Put H_n = ||D^2(f_n - z_1^2)||_{L^inf(B_R)}; then H_n -> 0. The
common value and gradient at 0 imply
    |f_n(Z) - z_1^2| <= H_n |Z|^2/2   for |Z| <= R,
    (1/pi) int_{|Z| < R} |f_n(Z) - z_1^2| r^{-3} |sin(3 th)| dZ <= R H_n.
The integral of z_1^2 against r^{-3} sin(3 th) on every disk is zero, because
    int_0^{2 pi} cos^2(th) sin(3 th) dth = 0.
Splitting the absolutely convergent strain identity c[f_n] = 1 - p_n/2 at radius R now gives
    (1/pi) int_{|Z| > R} f_n(Z) r^{-3} sin(3 th) dZ -> 1.
This is strain escape in the signed moment specified in the report. It assigns no globally convergent strain integral
to z_1^2, which is outside S. No convergence of b_n is needed for this part once the exact identities of Step 1 and
the stated C^2_loc convergence are available.
Step 11 (compactness in Corollary 4.10). Fix C, M, a > 0 and gamma, eta in (0, 1), and restrict to the profiles in S
satisfying the three bounds in Corollary 4.10. Suppose their l values are unbounded. Choose a sequence with
l_n -> infinity, so p_n -> 0. The uniform Hessian bound and the common jet give on every disk
    |grad f_n(Z)| <= M |Z|,   |f_n(Z)| <= M |Z|^2/2.
The global C^eta bound on D^2 f_n makes these Hessians equicontinuous. Arzela-Ascoli, first for all derivatives of
order at most two on a disk and then diagonally over increasing disks, gives f_n -> f in C^2_loc along a subsequence.
The limits of the derivatives are the derivatives of f: this follows by integrating each first derivative along line
segments and passing to the limit, and then doing the same for the second derivatives. Also b_n(0) = 0 and the k = 1
bound control b_n on every disk, while the k = 2 bound makes Db_n equicontinuous. A further diagonal subsequence gives
b_n -> b in C^1_loc. Thus Theorem 4.9(a) applies.
The velocity envelope passes pointwise to this limit and gives
    |b(Z) - Z| <= C(1 + |Z|)^gamma,
    sup_{|Z| = r} |b(Z) - Z|/r <= C(1 + r)^gamma/r -> 0.
The hypothesis of Theorem 4.9(b) is therefore satisfied. In particular f is bounded, and b cannot be real-analytic.
The next two steps check both the nonlocal passage and the contrary analyticity forced by the derivative bounds.
Step 12 (uniform tails and passage through the velocity integral). The same envelope provides a common R >= 1 such
that
    Z.b_n(Z) >= |Z|^2/2   for |Z| >= R,   for every n.
Each b_n has a complete flow by the uniform linear growth bound. An exterior point Z has a backward hitting point Y on
|Y| = R and a hitting time t with
    0 <= t <= 2 log(|Z|/R),   f_n(Z) = e^{p_n t} f_n(Y).
After discarding finitely many indices, p_n <= 1/4. With the local Hessian bound on B_R this implies a uniform,
strictly sublinear density envelope, irrespective of the original exponents in S:
    |f_n(Z)| <= (M R^2/2)(|Z|/R)^{2p_n}   for |Z| >= R,
    |f_n(Z)| <= C_0 (1 + |Z|)^{1/2}   for every Z.
The latter bound also holds for f by pointwise convergence. Hence, for a fixed compact set K of X and L larger than 2
sup_{X in K}|X| + 2, both the f_n and f integral tails obey
    sup_{X in K} int_{|Y| > L} |K(X - Y) - K(-Y)| |f_n(Y)| dY <= C_K L^{-1/2}.
For clarity, continuity of the bounded part of the integral can be checked without a limiting principal-value
interchange. Let G_n = f_n - f, fix such an L, and choose a fixed small d > 0 with B(X, d) contained in B_L for all X
in K. The zero angular mean of K gives
    p.v. int_{|Y-X| < d} K(X-Y) G_n(Y) dY = int_{|Y-X| < d} K(X-Y)(G_n(Y) - G_n(X)) dY.
Its norm is at most C d ||grad G_n||_{L^inf(B_L)}, uniformly in X. The remaining part of the first kernel on B_L is
bounded by C_{K,L,d} ||G_n||_{L^inf(B_L)}. For the subtracted kernel, the common value and gradient at 0 give
    |G_n(Y)| <= |Y|^2 ||D^2 G_n||_{L^inf(B_L)}/2,
    int_{|Y| < L} |K(-Y) G_n(Y)| dY <= C L^2 ||D^2 G_n||_{L^inf(B_L)}.
The local term -G_n(X)e_2/2 tends uniformly to zero as well. First take n -> infinity with L and d fixed, then
L -> infinity in the uniform tail estimate. This proves
    W[f_n] -> W[f]   locally uniformly,   b = Z + W[f].
Thus the limit velocity is the once-subtracted integral of f itself. The proof supplies the needed uniform integrable
tails; local convergence with unrelated p-dependent growth constants would not by itself supply this passage.
Step 13 (analyticity from the factorial derivative bounds). For every integer k >= 1, the bounds on D^k b_n and
D^{k+1} b_n give boundedness and equicontinuity of D^k b_n on compact disks. A diagonal subsequence for all k
converges locally uniformly with all derivatives; integration along segments again identifies the limits as
derivatives of b. Hence b is C^infinity and inherits, for every k >= 1,
    ||D^k b||_inf <= M a^{-k} k!.
To see explicitly that these bounds imply real analyticity, fix X and one component of b. For h = (h_1, h_2), Taylor's
formula along X + t h, 0 <= t <= 1, and the multinomial formula bound the remainder after degree N by
    M ((|h_1| + |h_2|)/a)^{N+1}.
Indeed, each partial derivative of order N + 1 is bounded by M a^{-(N+1)}(N+1)!, and the coefficients of the
directional derivative sum to (|h_1| + |h_2|)^{N+1}. The remainder tends to zero whenever |h_1| + |h_2| < a. The
multivariate Taylor series therefore represents b near every X. This contradicts Step 8. There can be no sequence in
the stated class with l_n -> infinity, which is exactly the existence of a finite bound L_*(C, M, a, gamma, eta). If
the class is empty the bound is vacuous. No nonemptiness assertion and no bound over all of S are proved.
Step 14 (the two resonant Fourier coefficients). For Remark 4.11 fix a real 2 pi-periodic A in C^2, independently of p
in (0, 1), and define
    Abar = (1/(2 pi)) int_0^{2 pi} A(th) dth,
    a_2 = (1/pi) int_0^{2 pi} A(th) cos(2 th) dth,
    b_2 = (1/pi) int_0^{2 pi} A(th) sin(2 th) dth.
The periodic coefficient of Theorem 3.16 and Section 9.3, Step 1, is the unique solution of
    Psi_p'' + (p + 1)^2 Psi_p = g_p,   g_p = sin(th) A' - p cos(th) A.
Uniqueness holds because p + 1 lies strictly between 1 and 2 and is not an integer. Integration by parts and the
elementary product identities for sines and cosines give
    [g_p]_{cos th} = -p Abar - (p + 2) a_2/2,
    [g_p]_{sin th} = -(p + 2) b_2/2.
For example, the first derivative term in the cosine projection is
    int_0^{2 pi} sin(th) cos(th) A'(th) dth = -int_0^{2 pi} cos(2 th) A(th) dth = -pi a_2,
and the cosine product term is -p pi(Abar + a_2/2). The sine projection uses int sin^2(th) A' dth = -pi b_2 and
int sin(th) cos(th) A dth = pi b_2/2, with the same limits. Dividing by (p + 1)^2 - 1 = p(p + 2) yields the exact
formulas
    [Psi_p]_{cos th} = -Abar/(p + 2) - a_2/(2p),
    [Psi_p]_{sin th} = -b_2/(2p).
Put P_2(th) = a_2 cos(th) + b_2 sin(th). The remaining modes are uniformly bounded in C^1 as p -> 0. Here is a direct
justification. For 0 < p <= 1/2, g_p is uniformly bounded in C^1, so its complex Fourier coefficients at nonzero
integer m are bounded by C_A/|m|, by integration by parts. Away from m = +-1, the denominators (p + 1)^2 - m^2 are
bounded away from zero for bounded m and have magnitude at least a fixed multiple of m^2 for large m. The solution
coefficients are consequently O_A(|m|^{-3}); their once differentiated series converge absolutely and uniformly. The
mean is bounded too. The bounded first-mode term -Abar cos(th)/(p + 2) completes the estimate
    Psi_p = -P_2/(2p) + R_p,   ||R_p||_{C^1} <= C_A.
Using the definition J_p[A] = (p + 1) Psi_p A' - p Psi_p' A now gives, uniformly in th,
    (p/(1 - p)) J_p[A] = ((p + 1)/(1 - p))(p Psi_p) A' - (p/(1 - p))(p Psi_p') A -> -(1/2) P_2 A'.
If (a_2, b_2) != (0, 0), the first harmonic P_2 is nonzero except at two points of the circle. If P_2 A' vanished
identically, A' would vanish off those points and hence everywhere by continuity. Then A would be constant and
a_2 = b_2 = 0, a contradiction. Thus the displayed limit vanishes identically if and only if a_2 = b_2 = 0.
Step 15 (the scope of the far-field comparison and the radius ratio). Write B_p = J_p[A]/(l - 1) = p J_p[A]/(1 - p).
Step 14 proves a uniform fixed-A coefficient limit for B_p. If a_2 = b_2 = 0, its proof also gives B_p = O_A(p). For a
fixed radius r > 0, at any angle with A(th) != 0 the ratio of the displayed correction term to the leading term is
    (r^{2p-1} B_p(th))/(r^p A(th)) = r^{p-1} B_p(th)/A(th) -> -P_2(th) A'(th)/(2 r A(th)).
When the second mode is nonzero this limiting angular expression is not identically zero on {A != 0}. Indeed P_2 A' is
nonzero on some open interval, and A cannot vanish throughout that interval. This statement concerns the displayed
terms for fixed A. The remainder in Theorem 3.16, proved in Section 9.3, Step 7, is an asymptotic for each fixed
profile and is not asserted to be uniform as p -> 0. Even for fixed A, if r = r(p) -> infinity, then for p <= 1/2
r^{p-1} <= r^{-1/2}, so the displayed relative correction tends to zero at any fixed angle with A != 0. There is
therefore no lower bound on that ratio uniform over joint choices of p and r, and no conclusion for arbitrary varying
families A_p follows from the fixed-A calculation alone.
Finally suppose rho is a profile in S^+, as defined in Section 3. Theorem 3.13, proved in Section 9.4, Step 6, gives
exactly rho = |S|^p A(arg S) in the scattering coordinates S. For a positive density level m and a direction where
A(th) > 0, its radius in those coordinates is
    R_m(th) = (m/A(th))^{1/p},   R_m(th_1)/R_m(th_2) = (A(th_2)/A(th_1))^l.
By Theorem 3.2 and Section 9.4, Step 2, A is continuous, positive away from exactly two zeros, and not identically
zero. Choose th_2 with A(th_2) = max A and, by continuity between that point and a zero, choose th_1 with
A(th_1) = A(th_2)/2 > 0. The radius ratio is then exactly 2^l; smaller positive values at th_1 give larger ratios.
Both directions have positive A; the zero directions have no point on this positive level. This is the claimed
anisotropy in scattering coordinates. Together with the fixed-A formulas it supplies no universal physical domain-size
requirement. This completes the proof of Remark 4.11.

### 9.16 Proposition 3.15a (layered solutions quadratic in x; x-parity is forced)
Setting and notation as in Proposition 3.15a: rho = f x^2 + g x + k and psi = n x^3 + m x^2 + s x + t on R x I, with
f, g, k in C^1(I) and n, m, s, t in C^2(I). As in Section 9.7 put b(y) := V_2(0, y) = l y + s(y); also put u := t'.
Step 1 (coefficient equations). -Lap psi = -(n'' x^3 + m'' x^2 + (s'' + 6n) x + t'' + 2m) and rho_x = 2f x + g, so the
Poisson equation -Lap psi = rho_x on R x I is equivalent to
    n'' = 0,   m'' = 0,   s'' = -2f - 6n,   t'' = -g - 2m   on I.
W = (-(n' x^3 + m' x^2 + s' x + u), 3n x^2 + 2m x + s), so V_1 = x(l - s') - n' x^3 - m' x^2 - u and V_2 = b + 2m
x + 3n x^2, and V.grad rho - rho is a polynomial of degree at most 4 in x with coefficients depending on y. The
coefficients of x^4, x^3, x^2, x and 1 give
    (E4)  3n f' - 2f n' = 0,
    (E3)  2m f' - 2f m' + 3n g' - n' g = 0,
    (E2)  2f (l - s') - g m' + b f' + 2m g' + 3n k' = f,
    (E1)  g (l - s') - 2f u + b g' + 2m k' = g,
    (E0)  b k' - g u = k,
all on I. The jet is equivalent to f(0) = 1, g(y) = O(y^2) and k(y) = O(|y|^3): put x = 0, then x = |y| and x = -|y|,
and subtract and add; conversely these give |(f - 1) x^2| + |g x| + |k| <= C |X|^3 near 0, since f - 1 = O(|y|).
W(0) = 0 means s(0) = 0 and u(0) = 0. In particular g(0) = g'(0) = 0, k'(0) = 0, b(0) = 0 and u(y) = O(|y|). Since
n'' = m'' = 0, n = n_0 + n_1 y and m = m_0 + m_1 y with constants n_0, n_1, m_0, m_1.
Step 2 (strain, and m(0) = 0). At y = 0, (E2) gives 2(l - s'(0)) = 1, so s'(0) = l - 1/2 and
b'(0) = 2l - 1/2 = beta > 0, as in Section 9.7, Step 1. Hence b(y) = beta y + o(y), and b(y) != 0 for small y != 0. By
(E0), k' = (k + g u)/b there, with k + g u = O(|y|^3), so k'(y) = O(y^2). Divide (E1) by y and let y -> 0: the terms g
(l - s')/y, b g'/y, 2m k'/y and g/y tend to 0 (g = O(y^2), g'(0) = 0, b/y -> beta, k' = O(y^2)), and 2f
u/y -> 2u'(0) = 2t''(0). Hence t''(0) = 0, and the relation t'' = -g - 2m at y = 0 gives m_0 = m(0) = 0.
Step 3 (a lemma on b k' = k). Let I_0 be an open interval with 0 in I_0, contained in I, on which b
vanishes only at 0 and b k' = k. Then k = 0 on I_0. Indeed, let y_0 in I_0 with y_0 > 0. Then b > 0 on (0, y_0]
(b'(0) > 0), and for 0 < y < y_0
    k(y) = k(y_0) exp(-int_y^{y_0} d eta/b(eta)).
Since b(eta) = beta eta + o(eta), there is delta_1 in (0, y_0) with b(eta) >= (4 beta/5) eta on (0, delta_1]. For
0 < y < delta_1, int_y^{y_0} d eta/b <= (5/(4 beta)) log(delta_1/y) + C_3 with C_3 := int_{delta_1}^{y_0} d eta/b, so
|k(y)| >= |k(y_0)| e^{-C_3} (y/delta_1)^{5/(4 beta)}, and 5/(4 beta) < 5/6 < 1 because beta > 3/2. Since
k(y) = O(|y|^3), k(y_0) = 0. For y_0 < 0 the same argument with |b| (b < 0 on [y_0, 0)) gives k(y_0) = 0, and
k(0) = 0.
Step 4 (n is constant, and the two cases). If n_0 = 0 and n_1 != 0, then on an interval (0, eps) where f > 0 and
n != 0, (E4) gives (f^3/n^2)' = f^2 (3n f' - 2f n')/n^3 = 0, so f^3 = C n_1^2 y^2 -> 0 as y -> 0+, against f(0) = 1.
So n_0 = 0 implies n = 0 on I; Steps 5-7 treat this case. The case n_0 != 0 is Step 8.
Step 5 (case n = 0: m = 0 and the even part). Let J be the component of {y in I : f(y) != 0} containing 0. With n = 0,
(E3) gives (m/f)' = (m' f - m f')/f^2 = 0 on J, so m = m(0) f/f(0) = 0 on J; m is affine on I and vanishes on the open
interval J, so m = 0 on I. Then (E2) reads 2f (l - s') + b f' = f, and l - s' = 2l - b', so b f' = (1 - 4l + 2b')
f = 2(b' - beta) f. Together with s'' = -2f, f(0) = 1 and s(0) = 0, these are exactly the relations to which Section
9.7, Step 1, reduces the ansatz of Proposition 3.15, and Steps 2-4 of Section 9.7 use nothing else (f in C^1(I), s in
C^2(I)). Hence I is contained in (-beta, inf) and, on I,
    f = (beta/(beta + y))^4,   b = beta (beta + y)/3 - beta^4/(3 (beta + y)^2).
In particular b vanishes on I only at y = 0, b(y) y > 0 for y != 0 ((beta + y)^3 - beta^3 has the sign of y),
b'(0) = beta and b''(0) = -2.
Step 6 (case n = 0: g = 0 and t constant). With n = m = 0, (E1) (using l - s' = 2l - b') and the relation for t'' read
    b g' = (1 - 2l + b') g + 2f u,   u' = -g   on I.
Since 1 - 2l + b'(0) = 1 - 2l + beta = 1/2, the coefficient q := (1 - 2l + b')/b satisfies q(y) = kappa/y + O(1) as
y -> 0, where kappa := 1/(2 beta) lies in (0, 1/3). Fix delta in (0, 1) with [-delta, delta] contained in I and
|b(y)| >= beta |y|/2 there. On (0, delta] let phi(y) := exp(int_delta^y q); then phi > 0, phi' = q phi, and
phi(y) = y^kappa theta(y) with theta continuous and positive on [0, delta] (q - kappa/y is bounded), so there is C_1
with phi(y)/phi(eta) <= C_1 (y/eta)^kappa for 0 < eta <= y <= delta. On (0, delta], (g/phi)' = 2f u/(b phi). Since
u(0) = 0 and u' = -g = O(y^2), u = O(|y|^3), so the right side is O(y^{2 - kappa}) and integrable at 0; and g/phi -> 0
as y -> 0+ because g = O(y^2) and phi >= c y^kappa. Therefore
    g(y) = phi(y) int_0^y 2f(eta) u(eta)/(b(eta) phi(eta)) d eta,   0 < y <= delta.
Let N(y) := max_{[0, y]} |g|. For 0 < eta <= y, u(eta) = -int_0^eta g gives |u(eta)| <= eta N(y), and with
F := max_{[-delta, delta]} |f|,
    |g(y)| <= (4F C_1/beta) N(y) int_0^y (y/eta)^kappa d eta = C_2 y N(y),   C_2 := 4F C_1/(beta (1 - kappa)).
The right side is nondecreasing in y, so N(y) <= C_2 y N(y), and N(y) = 0 for 0 < y < min(delta, 1/C_2). The same
argument on [-delta, 0), with phi(y) := exp(int_{-delta}^y q) and |y| in place of y, shows that g = 0 on a
neighbourhood of 0; then u = 0 there, since u(0) = 0 and u' = -g. On each of the intervals I cap (0, inf) and I cap
(-inf, 0), b != 0 by Step 5, so (g, u) solves a linear system of ordinary differential equations with continuous
coefficients and vanishes on a subinterval; by uniqueness g = 0 and u = 0 on I. Hence t' = u = 0 and t is constant on
I.
Step 7 (case n = 0: conclusion). With g = 0, (E0) reads b k' = k on I, and b vanishes on I only at 0 (Step 5), so Step
3 with I_0 = I gives k = 0. Thus m = g = k = 0, t is constant, rho = x^2 f and W = (-x s', s), and by Step 5 these are
the functions of Proposition 3.15 on I, with I contained in (-beta, inf): case (a).
Step 8 (case n_0 != 0). At y = 0, (E3) gives 2m(0) f'(0) - 2f(0) m_1 + 3n_0 g'(0) - n_1 g(0) = -2m_1 = 0 (Step 2,
f(0) = 1, g(0) = g'(0) = 0), so m = 0 on I. Let J be the component of {y in I : n(y) != 0} containing 0. On J, (E3)
gives (g^3/n)' = g^2 (3n g' - n' g)/n^2 = 0, so g^3 = C n with C n_0 = g(0)^3 = 0; hence g = 0 on J, and u = 0 on J
since u(0) = 0 and u' = -g - 2m = 0. Choose an open interval I_0 with 0 in I_0, contained in J, on which b vanishes
only at 0, f > 0 and z := 1 + c y > 0, where c := n_1/n_0. On I_0, (E0) reads b k' = k, so k = 0 there by Step 3; then
(E2) reads b f' = 2(b' - beta) f as in Step 5, and (E4) gives (f^3/n^2)' = 0, so f^3 = n^2/n_0^2 = z^2 and
f = z^{2/3}. Suppose c != 0. Then f'/f = 2c/(3z), so b' = beta + c b/(3z), and with b(0) = 0, (b z^{-1/3})' = beta
z^{-1/3} gives
    b = (3 beta/(2c)) (z - z^{1/3}),   b'' = (beta c/3) z^{-5/3}   on I_0.
But s'' = -2f - 6n gives b'' = -2 z^{2/3} - 6 n_0 z, so z^{7/3} + 3 n_0 z^{8/3} = -beta c/6 for z in the open interval
{1 + c y : y in I_0} around 1. The first and second derivatives at z = 1 give 7/3 + 8 n_0 = 0 and 28/9 + (40/3)
n_0 = 0, which are incompatible. Hence c = 0: n = n_0 is constant and nonzero on I, J = I, and g = m = u = 0 on I. Now
(E4) gives f' = 0, so f = 1 on I. On I_0, k = 0 and (E2) reads 2(l - s') = 1, so s'' = 0 there, and s'' = -2f - 6n
gives n_0 = -1/3. On I, (E2) then reads 2(l - s') - k' = 1, so k' = 2(l - s') - 1 is C^1 with k'' = -2s'' = 0
(s'' = -2 + 2 = 0); k is affine on I and vanishes on I_0, so k = 0 on I, s' = l - 1/2 and, with s(0) = 0,
s = (l - 1/2) y. Thus rho = x^2 and psi = -x^3/3 + (l - 1/2) x y + t with t constant: case (b). Conversely this is a
solution on R^2 (Section 9.14, Step 12).
Step 9 (parity). In both cases g = m = 0, t is constant and k = 0, so rho = x^2 f is even in x and psi - t = n x^3 + s
x is odd in x. Case (a) requires I to lie in (-beta, inf), so on I = R only case (b) occurs.

### 9.17 Proposition 2.1 (truncation limits)
Notation as in Proposition 2.1: l = c_l, K(Z) = (-sin 2th_Z, cos 2th_Z)/(2 pi |Z|^2), and in complex notation a vector
(u_1, u_2) is u_1 + i u_2, X = x + iy, Xbar = x - iy, Y = s e_phi. Constants C depend only on the indicated data.
Step 1 (the velocity of a truncated density). Let g be bounded and measurable with compact support. Then N * g is C^1,
and U[g] = grad-perp d_x(N * g) is a distribution. Let O be an open set on which g = rho, with rho in C^3. We claim
that U[g] is C^2 on O and that
    U[g](X) = p.v. int K(X - Y) g(Y) dY - g(X) e_2/2,   X in O.
Fix X_0 in O, a ball B(X_0, 2 eps) contained in O, and chi in C_c^inf(B(X_0, 2 eps)) equal to one on B(X_0, eps).
Split g = chi rho + (1 - chi) g. The first part is C^3 with compact support, and the compact Biot-Savart formula of
Section 9.14, Step 2, gives its velocity in the displayed form, as a C^2 field. The second part vanishes on B(X_0,
eps). On B(X_0, eps/2) its Newtonian potential is smooth and may be differentiated under the integral, and grad-perp
d_x N(Z) = K(Z) for Z != 0, so its velocity there is int K(X - Y)(1 - chi(Y)) g(Y) dY, again smooth. Adding the two
parts gives the claim on B(X_0, eps/2). If 0 is in O, the same splitting about X_0 = 0, the derivative formula of
Section 9.14, Step 2, applied to chi rho, and differentiation under the integral in the second part give
    DU[g](0) e_j = int DK(-Y) e_j g(Y) dY,   j = 1, 2,
an absolutely convergent integral, because rho(0) = 0, grad rho(0) = 0 and DK(-Y) rho(Y) = O(|Y|^(-1)) near 0. On O,
div U[g] = 0 and curl U[g] = -rho_x; since rho_x(0) = 0, DU[g](0) is then symmetric and traceless. For a bounded
measurable set D containing B(0, r) we write U_D = U[rho 1_D] and W_D = U_D - U_D(0) on B(0, r). Since rho(0) = 0,
    (9.17.1)   W_D(X) = p.v. int_D [K(X - Y) - K(-Y)] rho(Y) dY - rho(X) e_2/2,   |X| < r,
where K(-Y) rho(Y) is bounded near Y = 0, so the integral is absolutely convergent there.
Kernel series and real forms. Since K(Z) = i e^{2i th_Z}/(2 pi |Z|^2) = i/(2 pi Zbar^2), expansion of
(1 - Xbar/Ybar)^(-2) gives, for |X| <= |Y|/2,
    (9.17.2)   K(X - Y) = (i/(2 pi)) sum_{k >= 0} (k + 1) Xbar^k Ybar^(-k-2),
with the k-th term bounded by (k + 1) 2^(-k) |Y|^(-2). The term k = 1 is DK(-Y) X = (i/pi) Xbar Ybar^(-3). For complex
c = c_1 + i c_2 and beta,
    c Xbar = (c_1 x + c_2 y, c_2 x - c_1 y),   grad-perp Re(beta X^3) = 3i betabar Xbar^2.
The first is the product (c_1 + i c_2)(x - iy). For the second, grad-perp psi = (-psi_y, psi_x) corresponds to
i(psi_x + i psi_y) = 2i d_Xbar psi, and d_Xbar Re(beta X^3) = (3/2) betabar Xbar^2. Thus c Xbar runs over all strain
fields MX with M = [[c_1, c_2], [c_2, -c_1]] symmetric and traceless, and c Xbar^2 over the velocities of all harmonic
cubics (every homogeneous harmonic cubic is Re(beta X^3) for some complex beta). For the terms of Section 9.14, Step
12, Q_3 = -Re(X^3)/24 and Q_2 = (l - 1/2) xy,
    grad-perp Q_3 = -(i/8) Xbar^2,   grad-perp Q_2 = (1/2 - l) Xbar,
which agrees with the real forms printed there.
Step 2 (part (a)). Let D_R contain B(0, R) and |X| <= L <= R/2. By Section 2 and Step 1 with rho(0) = 0, the canonical
velocity W is (9.17.1) with D replaced by R^2. For |X| < R both principal values concern the same neighbourhood of
Y = X, so
    W_{D_R}(X) - W(X) = -int_{R^2 \ D_R} [K(X - Y) - K(-Y)] rho(Y) dY,
absolutely convergent. On R^2 \ D_R we have |Y| >= R >= 2|X|, hence |K(X - Y) - K(-Y)| <= C|X||Y|^(-3) (Section 9.0,
Step 1), and
    |W_{D_R}(X) - W(X)| <= C L int_{|Y| >= R} |Y|^(-3) (1 + |Y|)^gamma dY <= C L R^(gamma - 1)/(1 - gamma).
The j-th X-derivatives of the kernel difference are those of K(X - Y), bounded by C|Y|^(-2-j) on this set, so the
first and second derivatives of the difference are bounded by C R^(gamma - 1) and C R^(gamma - 2). This proves (a).
Step 3 (part (b)). By Step 1, M_R = DU_{D_R}(0) is symmetric and traceless and equals DW_{D_R}(0). Subtracting M_R X
from (9.17.1) by the derivative formula of Step 1 gives, for |X| < R,
    W_{D_R}(X) - M_R X = p.v. int_{D_R} [K(X - Y) - K(-Y) - DK(-Y) X] rho(Y) dY - rho(X) e_2/2.
The twice-subtracted field W_2 of Section 9.14, Step 3, is the same expression with D_R replaced by R^2. For
|X| <= L <= R/2 the difference is
    W_{D_R}(X) - M_R X - W_2(X) = -int_{R^2 \ D_R} [K(X - Y) - K(-Y) - DK(-Y) X] rho(Y) dY,
where |Y| >= R. The bound C|X|^2|Y|^(-4) of Section 9.14, Step 3 for the combined kernel, the bound C|X||Y|^(-4) for
its first X-derivative (the mean value theorem applied to DK(X - Y) - DK(-Y)) and the bound C|Y|^(-4) of the same step
for its second X-derivative give
    |W_{D_R}(X) - M_R X - W_2(X)| <= C L^2 R^(gamma - 2),
and the bounds C L R^(gamma - 2) and C R^(gamma - 2) for the first two derivatives. If the centered fields converge at
X = e_1 and X = e_2, then M_R e_1 and M_R e_2 converge; conversely, convergence of M_R gives convergence of the
centered fields to W_2 + MX. This proves the first part of (b).
For the example, rho_gamma = x^2 (1 + r^2)^((gamma - 2)/2) is smooth, equals x^2 + O(r^4), and satisfies
|rho_gamma| <= (1 + r^2)^(gamma/2) and |grad rho_gamma| <= C(1 + r)^(gamma - 1). Let delta >= 0 be bounded and
measurable on the circle, and let D_R = {s e_phi : s < t_R(phi)} with t_R = (R^(gamma - 1) + delta)^(1/(gamma - 1)) if
gamma > 1 and t_R = R e^delta if gamma = 1. These are bounded star-shaped sets containing B(0, R). By Step 1 and the
term k = 1 of (9.17.2), M_R X = (i/pi) N_R Xbar with
    N_R = int_{D_R} rho_gamma(Y) Ybar^(-3) dY,   h(s) = (1 + s^(-2))^((gamma - 2)/2),
    N_R = int_0^{2 pi} cos^2 phi e^{3i phi} int_0^{t_R(phi)} s^(gamma - 2) h(s) ds dphi.
Since int_0^{2 pi} cos^2 phi e^{3i phi} dphi = 0, the part s < R vanishes. Also int_R^{t_R} s^(gamma - 2) ds = c_gamma
delta(phi), with c_gamma = 1/(gamma - 1) for gamma > 1 and c_gamma = 1 for gamma = 1, and 0 <= 1 - h(s) <= s^(-2).
Hence
    |N_R - c_gamma Delta| <= 2 pi c_gamma sup delta R^(-2),   Delta = int_0^{2 pi} cos^2 phi e^{3i phi} delta dphi,
and M_R X -> (i/pi) c_gamma Delta Xbar. Only the constant 1/2 of cos^2 phi = (1 + cos 2phi)/2 contributes to the
integrals of cos^2 phi e^{3i phi} against 1, sin 3phi and cos 3phi, which are 0, i pi/2 and pi/2. So
delta = a(1 +/- sin 3phi) + b(1 +/- cos 3phi) with a, b >= 0 gives Delta = (pi/2)(+/- b +/- ia) with the corresponding
signs, every complex number occurs, and by Step 1 every symmetric traceless M is a limit of M_R. Alternating two such
choices of delta along a sequence R_n -> infinity gives a family for which M_R has no limit. This proves (b).
Step 4 (part (c): reduction to angular moments). Let rho = x^2, put S = sup|delta|, t_R = R rho_0 + delta and r_R = R
m/2, and let R >= 4L/m + 2S/m. Then t_R >= r_R, so D_R is the disjoint union of B(0, r_R) and A_R = {s e_phi :
r_R <= s < t_R(phi)}, and L <= r_R/2. The velocity is linear in the density. By Section 9.14, Step 11, with radius
r_R, the centered field of x^2 1_{B(0, r_R)} equals W_circ on B(0, r_R). The density x^2 1_{A_R} vanishes on B(0,
r_R), so by Step 1 its velocity at |X| <= r_R/2 is int_{A_R} K(X - Y) Y_1^2 dY. On A_R we have |Y| >= r_R >= 2|X|; the
series (9.17.2) is dominated there by sum (k + 1) 2^(-k) |Y|^(-2) Y_1^2 <= 4, and A_R is bounded, so it may be
integrated term by term:
    W_{D_R}(X) = W_circ(X) + (i/(2 pi)) sum_{k >= 1} (k + 1) M_k Xbar^k,
    M_k = int_{A_R} Y_1^2 Ybar^(-k-2) dY = int_0^{2 pi} cos^2 phi e^{i(k+2) phi} int_{r_R}^{t_R(phi)} s^(1-k) ds dphi.
For k >= 1, int_0^{2 pi} cos^2 phi e^{i(k+2) phi} dphi = 0, because cos^2 phi has only the Fourier modes 0 and +-2, so
the lower limit r_R does not contribute. For k = 1 this gives M_1 = int cos^2 phi e^{3i phi} t_R dphi = R G + I. For
k = 2, log t_R = log R + log rho_0 + log(1 + delta/(R rho_0)), the constant log R does not contribute, and |delta/(R
rho_0)| <= 1/2, |log(1 + u)| <= 2|u| for |u| <= 1/2, so M_2 = J + E_R with |E_R| <= 4 pi S/(m R). For k >= 3,
|M_k| <= 2 pi int_{r_R}^inf s^(1-k) ds <= 2 pi r_R^(2-k). With q = L/r_R <= 1/2,
    |(i/(2 pi)) sum_{k >= 3} (k + 1) M_k Xbar^k| <= r_R^2 sum_{k >= 3} (k + 1) q^k <= 10 r_R^2 q^3 = 20 L^3/(m R),
using sum_{j >= 0} (j + 4) 2^(-j) = 10. The remainder F_R is a convergent power series in Xbar, and the same majorants
give its first and second derivatives the bounds C L^2/(m R) and C L/(m R). These bounds use only m and S, not an
upper bound for rho_0, so they hold also when rho_0 depends on R with a fixed lower bound m. This proves the
expansion. If G != 0, the strain term has size at least |G| R |X|/pi - C|X| and the other terms stay bounded, so there
is no limit; if G = 0, the limit is W_{rho_0, delta}.
Step 5 (realised gauges and the profile condition). Write cos^2 phi = 1/2 + (e^{2i phi} + e^{-2i phi})/4. If
rho_0 = exp(a cos 4phi + b sin 4phi), then rho_0 has period pi/2, so it has only Fourier modes divisible by 4, while
cos^2 phi e^{3i phi} has only the modes 1, 3 and 5; hence G = 0. Also log rho_0 = ((a - ib)/2) e^{4i
phi} + ((a + ib)/2) e^{-4i phi}, and in J only the constant 1/2 of cos^2 phi meets a mode of log rho_0, which gives
J = (1/2)(2 pi)(a + ib)/2 = (pi/2)(a + ib). If delta = alpha_1 cos phi + alpha_2 sin phi = ((alpha_1 - i alpha_2)/2)
e^{i phi} + ((alpha_1 + i alpha_2)/2) e^{-i phi}, only the term e^{i phi}/4 of cos^2 phi e^{3i phi} meets a mode of
delta, and I = (1/4)(2 pi) (alpha_1 + i alpha_2)/2 = (pi/4)(alpha_1 + i alpha_2). By Step 1, c = (i/pi) I and
c' = (3i/(2 pi)) J are then arbitrary, so every strain and every harmonic cubic velocity occurs in W_{rho_0, delta}.
Let W = W_circ + c Xbar + c' Xbar^2 with c = (i/pi) I and c' = (3i/(2 pi)) J. Then W(0) = 0, div W = 0 and curl
W = -2x = -rho_x, since W_circ has these properties (Section 9.14, Step 11) and the added strain and cubic velocities
are divergence free and curl free. With V = lX + W, V.grad(x^2) = 2x(lx + W^{(1)}), so x^2 solves the profile equation
with parameter l if and only if W^{(1)} = (1/2 - l) x for x != 0, and then everywhere by continuity. By Step 1,
    W^{(1)} = xy/4 + (Re c) x + (Im c) y + (Re c')(x^2 - y^2) + 2(Im c') xy,
so the condition is c = 1/2 - l and c' = -i/8, that is, I = i pi (l - 1/2) and J = -pi/12. Then, by Step 1,
W = W_circ + grad-perp Q_2 + grad-perp Q_3, which is the polynomial solution of Section 9.14, Step 12. The example
follows from the formulas above with a = -1/6, b = 0, alpha_1 = 0 and alpha_2 = 4(l - 1/2).
Step 6 (disks, ellipses and symmetric domains). For centered disks, rho_0 = 1, delta = 0 and G = I = J = 0; the limit
W_circ has W_circ^{(1)} = xy/4, which is not (1/2 - l) x. The same holds for disks with moving centers. Let
B_d = B(d, s) contain 0, d = (d_1, d_2), and put z = X - d. Inside B_d, up to additive constants,
N * 1_{B_d} = -|z|^2/4 and N * (z_1 1_{B_d}) = s^2 z_1/4 - z_1 |z|^2/8: each has -Lap equal to the density in B_d and
matches, in value and radial derivative at |z| = s, the exterior potential -(s^2/2) log|z|, respectively
s^4 z_1/(8|z|^2), of the same density (the difference is then harmonic on R^2 and tends to a constant at infinity). So
U[1_{B_d}] is constant in B_d and U[z_1 1_{B_d}] = (z_2/4, -3 z_1/4) + const in B_d, while the field of z_1^2 1_{B_d}
is W_circ(z) + const in B_d (Section 9.14, Step 11, translated). Since x^2 = z_1^2 + 2 d_1 z_1 + d_1^2, centering
gives, wherever 0 and X lie in B_d,
    W_{B_d}(X) = W_circ(X - d) - W_circ(-d) + (d_1/2)(y, -3x) = W_circ(X) + (i/4)(d_1 + i d_2) Xbar,
independently of s. Hence for a family B(d_R, s_R) the centered fields converge if and only if d_R converges, and
every limit has first component xy/4 + (d_1 y - d_2 x)/4, which is not (1/2 - l) x: no family of disks gives a
velocity with which x^2 solves the profile equation. For the ellipse x^2/A^2 + y^2/B^2 < R^2, delta = 0 and
rho_0 = (cos^2 phi/A^2 + sin^2 phi/B^2)^(-1/2). It is even and of period pi, so it has only even Fourier modes and
G = I = 0. With q = (B^2 - A^2)/(B^2 + A^2) = 2 mu/(1 + mu^2), mu in (-1, 1),
    cos^2 phi/A^2 + sin^2 phi/B^2 = (1/2)(A^(-2) + B^(-2))(1 + q cos 2phi),
    1 + q cos 2phi = |1 + mu e^{2i phi}|^2/(1 + mu^2),
and log|1 + mu e^{2i phi}|^2 = 2 Re log(1 + mu e^{2i phi}) gives
    log rho_0 = const + sum_{n >= 1} ((-mu)^n/n) cos(2n phi).
For an even function f = sum_j f_j cos(j phi), int cos^2 phi e^{4i phi} f dphi = (pi/4)(f_2 + 2 f_4 + f_6). Hence
    J = (pi/4)(-mu + mu^2 - mu^3/3) = (pi/12)((1 - mu)^3 - 1).
Since 0 < (1 - mu)^3 < 8, J lies in (-pi/12, 7 pi/12) and is never -pi/12, so by Step 5 x^2 does not solve the profile
equation with the limit field of the homothetic copies of a fixed centered ellipse. For the ellipse rotated by an
angle theta, replacing cos(2n phi) by cos(2n(phi - theta)) in the same calculation gives G = I = 0 and
    J = (pi/12)((1 - mu e^{2i theta})^3 - 1),
which equals -pi/12 only if mu e^{2i theta} = 1, impossible for |mu| < 1. As B/A -> infinity, q -> 1, mu -> 1 and
J -> -pi/12, so the limit fields tend to W_circ - (i/8) Xbar^2 = W_circ + grad-perp Q_3 = (0, -x^2). For semi-axes R
and B_R, rho_0 = (cos^2 phi + (R/B_R)^2 sin^2 phi)^(-1/2) >= 1 depends on R, G = 0, delta = 0, and M_2 = J_R exactly,
where J_R is the value of J for this rho_0; by the uniformity noted in Step 4,
W_{D_R} - (0, -x^2) = (3i/(2 pi))(J_R + pi/12) Xbar^2 + F_R tends to 0 when B_R/R -> infinity.
Finally let sigma(x, y) = (x, -y), and let sigma D_R = D_R. Then g = x^2 1_{D_R} satisfies g(sigma Y) = g(Y). Since
th_{sigma Z} = -th_Z, K^{(1)}(sigma Z) = -K^{(1)}(Z) and K^{(2)}(sigma Z) = K^{(2)}(Z). Substituting Y = sigma Y' in
Step 1 (the disks of the principal value are mapped to disks of the same radius, and the local term has no first
component) gives U^{(1)}_{D_R}(sigma X) = -U^{(1)}_{D_R}(X), so W^{(1)}_{D_R} is odd in y, and so is the pointwise
limit W^{(1)}; in particular W^{(1)}(x, 0) = 0. If x^2 solves the profile equation with W and parameter l, this
equation at (x, 0), x != 0, reads 2x (l x + W^{(1)}(x, 0)) = x^2, that is 2l x^2 = x^2. Hence l = 1/2; no continuity
of the pointwise limit is used. The concluding sentences of Proposition 2.1 summarize (a), (b) and Steps 4-6.

### 9.18 Proposition 3.15b (layered solutions cubic in x)
Notation as in Proposition 3.15b; {F, G} = F_x G_y - F_y G_x, and a constant added to psi changes no equation.
Step 1 (coefficient equations and the jet). Degrees are actual degrees in x. The jet gives N >= 2 and the Poisson
equation gives N - 1 <= M. For every index d the transport equation is
    (ld - 1) f_d + ly f_d' + sum_{j+k=d+1} (j q_j f_k' - k q_j' f_k) = 0,
with zero coefficients outside the two index ranges, and the Poisson equations are
    q_j'' + (j + 2)(j + 1) q_{j+2} = -(j + 1) f_{j+1}.
When N <= 3 and M <= 3 write rho = a x^3 + f x^2 + g x + k, psi = n x^3 + m x^2 + s x + t, b = ly + s and u = t'. The
equations become
    n'' = 0,   m'' = -3a,   b'' = -2f - 6n,   u' = -g - 2m,
    3n a' - 3a n' = 0,
    3n f' - 2f n' + 2m a' - 3a m' = 0,
    3n g' - n' g + 2m f' - 2f m' + b a' + (3(2l - b') - 1) a = 0,
    3n k' + 2m g' - m' g + b f' + 2(beta - b') f - 3a u = 0,
    2m k' + b g' + (2l - b' - 1) g - 2f u = 0,
    b k' - g u = k.
The jet and W(0) = 0 give f(0) = 1, g(y) = O(y^2), k(y) = O(|y|^3) and b(0) = u(0) = 0: set x = 0, then x = |y| and
x = -|y|, and add or subtract (the bounded cubic coefficient contributes only order three); in particular
g'(0) = k'(0) = 0. The coefficient of x^2 at 0 gives b'(0) = beta, so b is nonzero for small nonzero y. Since
u = O(|y|), the constant coefficient equation gives k' = O(y^2). Dividing the coefficient of x by y and letting
y -> 0, every term except -2fu/y tends to 0; hence u'(0) = 0 and m(0) = 0. Finally the coefficient of x^3 at 0 gives
m'(0) = a(0)/4. Only the stated regularity is used here; the equations supply further derivatives where these are used
below.
Step 2 (a nonconstant top stream coefficient is impossible when M > N). Here N >= 2 and M > N are arbitrary. The two
top coefficient equations are
    q_M'' = 0,   M q_M f_N' - N q_M' f_N = 0.
Suppose q_M is nonconstant, with zero y_*. On a component where q_M is nonzero, the second equation makes f_N a
constant times |y - y_*|^(N/M). If y_* were in I, C^1 regularity at y_* would force both constants to vanish, since
0 < N/M < 1, against the actual degree N. So y_* is not in I and f_N never vanishes on I. After a reflection about y_*
put z = |y - y_*|, so that z > 0 on I and d/dy = +-d/dz, and for nonzero real A and p
    q_M = p z,   f_N = A z^(N/M),   d = N + N/M < M.
All coefficient functions extend uniquely to z > 0 as finite sums of terms z^r (log z)^s with r real and s a
nonnegative integer; these extensions are algebraic devices, not an extension of the profile across y_*. Indeed,
interleave the equations in descending x-degree. Having found f_h for h > j, first determine the q_i needed in the
coefficient of x^(M+j-1) by integrating their Poisson equations: the smallest needed index is i = M + j - N, and its
forcing involves f_{i+1}, with index at least j + 2, and q_{i+2}, which are already known. Then solve the transport
equation for f_j: after division by a nonzero constant its left side is z d_z f_j - (j/M) f_j, and the only linear
transport term that enters occurs for M = N + 1, j = 0 and depends on the known f_N. Integration, multiplication,
differentiation and the solution of this Euler equation preserve finite power-log sums. After f_0, the remaining q_i
follow from the Poisson equations. Every coefficient identity continues to hold on z > 0, because its residual is real
analytic there and vanishes on an open interval.
The same induction gives asymptotics that may be differentiated termwise:
    q_i(z) = h_i z^(M+1-i) + o(z^(M+1-i)),   f_j(z) = r_j z^(d-j) + o(z^(d-j)),   r_N = A.
In a Poisson equation the density contribution, after two integrations, has exponent at most d - i + 1 < M + 1 - i,
and integration constants have degree at most one, which is below the stated leading degree except at the prescribed
top coefficient. In the equation for f_j each leading product from higher density coefficients has exponent d - j, the
homogeneous solution has exponent j/M, and
    d - j - j/M = (N - j)(1 + 1/M) > 0   for j < N,
so the leading exponent is nonresonant and carries no logarithm; the possible linear transport forcing has exponent
N/M < d, and terms below a leading exponent stay below it (logarithms may occur at lower resonances).
Define for z > 0
    H(x, z) = sum_{i=0}^M h_i x^i z^(M+1-i),   R(x, z) = sum_{j=0}^N r_j x^j z^(d-j) = z^d P(x/z).
The leading Poisson equation is Lap H = 0 with H homogeneous of degree M + 1, x^M coefficient p z and no x^(M+1) term,
so H(x, z) = p Im((x + iz)^(M+1))/(M + 1) (in polar form the angular factor solves h'' + (M + 1)^2 h = 0, and the two
leading coefficients fix it). The leading transport equation is {H, R} = 0 (in x, z): its bracket has degree
M + d - 1 > d, while the linear transport terms have degree at most d; a reflection of y only changes its sign.
Euler's identities for H and R give, at z = 1,
    M H(x, 1) P'(x) - N P(x) H_x(x, 1) = 0.
The polynomial H(x, 1) has degree M and M distinct real roots (write x + i in polar form and use the zeros of
sin((M + 1) theta) for 0 < theta < pi). At such a simple root, if P has multiplicity k (k >= 0), the first nonzero
coefficient of the last identity gives Mk = N, impossible since 0 < N < M. So q_M is constant.
Step 3 (the polynomial reduction for M > N). Now q_M is a nonzero constant and the top transport equation makes f_N
constant. The descent of Step 2 now gives polynomials with deg f_j <= N - j and deg q_i <= M - i: a needed q_i is
found by integrating q_{i+2} and f_{i+1} twice, with degree bounds M - i and N - i + 1 <= M - i; the equation for f_j
has the constant nonzero coefficient M q_M on f_j', and all its other products have degree at most N - j - 1 (for
M = N + 1, j = 0 the additional linear transport term is constant). Integration proves the bounds, and the remaining
q_i follow from the Poisson equations. Thus rho and psi have total degrees exactly N and M. If M > N + 1, let F and H
be the top homogeneous parts of rho and psi. Poisson makes H harmonic and transport gives {H, F} = 0. A nonzero real
homogeneous harmonic polynomial of degree M has M distinct real linear factors (its polar form is r^M (A cos(M
theta) + B sin(M theta)) with (A, B) nonzero). Take a finite simple root of H(x, 1) (at most one projective root is
missed in this chart); Euler's identities give M H(x, 1) F_x(x, 1) - N F(x, 1) H_x(x, 1) = 0, and the multiplicity
comparison again gives Mk = N, impossible for M > N. Hence M = N + 1, which is the reduction stated in Proposition
3.15b.
Step 4 (M > N with N <= 3). Suppose first that the reduction gives total degrees three for rho and four for psi, with
top homogeneous parts rho_3 and psi_4. Their Jacobian vanishes, and Euler's identities make both partial derivatives
of rho_3^4/psi_4^3 vanish, so this rational function is constant. By unique factorization each irreducible
multiplicity in rho_3 is divisible by three, so
    rho_3 = mu L^3,   psi_4 = lambda L^4
for a real linear form L and nonzero real mu, lambda. The top Poisson equation forces L_x != 0; rescale to L = x + ty.
The constant and linear parts of rho vanish and its quadratic part is x^2; centring removes the linear part of psi.
Writing its quadratic part as A(x^2 - y^2)/2 + Bxy + C(x^2 + y^2)/2, Poisson and quadratic transport give
    -2C = 0,   (2l - 1 - 2B) x^2 + 2(A - C) xy = 0,
so psi_2 = (l - 1/2) xy. The linear transport operator at this jet acts by
    (V_lin.grad - 1)(x^p y^q) = (p/2 + beta q - 1) x^p y^q.
Write psi_3 = A_3 x^3 + B_3 x^2 y + C_3 x y^2 + D_3 y^3. The y coefficient of the cubic Poisson equation and the x^3
and x y^2 coefficients of the cubic transport equation give
    2B_3 + 6D_3 = 0,   mu/2 - 2B_3 = 0,   3 mu t^2 (2 beta - 1/2) - 6D_3 = 0,
hence 1 + 6t^2 (2 beta - 1/2) = 0, impossible since beta > 3/2. If instead the reduction gives total density degree
two, the jet fixes rho = x^2; transport and Poisson give psi_y = (l - 1/2)x, psi = (l - 1/2)xy + F(x) with F'' = -2x,
and centring removes the linear term of F, which is the polynomial solution. This classifies N <= 3 when M > N.
Step 5 (a cubic density with M <= 2). In the notation of Step 1 set n = 0. Then m'' = -3a, so m is C^3, and the
highest transport equation with the values at 0 gives
    2m a' - 3a m' = 0,   m(0) = 0,   m'(0) = a(0)/4.
At 0 this gives a(0) = m'(0) = 0. Substituting a = -m''/3 and integrating once (the constant is 0 at the origin),
    2m m''' - 3m' m'' = 0,   4m m'' - 5(m')^2 = 0.
On a component where m is nonzero, (|m|^(-1/4))'' = |m|^(-9/4)(5(m')^2 - 4m m'')/16 = 0, so |m|^(-1/4) is affine
there. Such a component has an endpoint in I between it and 0 at which m tends to 0, so the affine function would tend
to infinity at a finite endpoint, which is impossible. Hence m = a = 0 on I.
Step 6 (the cubic case M = 3). Now n is affine. If n(0) = 0 and n' != 0, the equation 3n a' - 3a n' = 0 at 0 gives
a(0) = 0, and the next equation at 0 then gives -2n' = 0, a contradiction; so n(0) = 0 implies n = 0, the case of Step
5. Suppose n_0 = n(0) != 0 and work first on the component of {n != 0} containing 0. Put
    A = a(0),   C = A/n_0,   c = n'/n_0,   z = 1 + cy.
The two highest transport equations, Poisson and Step 1 give
    n = n_0 z,   a = A z,   m = A(y/4 - 3y^2/2 - c y^3/2),   f = C m + h,
with h = z^(2/3) if c != 0 and h = 1 if c = 0 (fractional powers are used near 0, where z > 0). For the formula for f,
subtracting C times the m terms in the second highest equation leaves 3n h' - 2n' h = 0 with h(0) = 1. Define r and v
by g = C b + r and v = k' - C u. Substitution into the lower equations of Step 1 gives
    b'' = -2C m - 2h - 6n,
    3n r' - n' r = 2h m' - 2m h' - (6l - 1) C n,
    u' = -C b - r - 2m,
    3n v = -b h' + 2(b' - beta) h - 2 beta C m - 2m r' + r m',
    E := 2m v + b r' + (2l - b' - 1) r + C(2l - 1) b - 2h u = 0,
with b(0) = r(0) = u(0) = 0 and b'(0) = beta. We show A = 0 by a leading-coefficient contradiction.
Step 7 (c = 0). Suppose A != 0. Then m, b, r, u and v are polynomials, and the five displayed equations give
successively the leading terms
    m = -3A y^2/2 + ...,   b = A^2 y^4/(4n_0) + ...,   r = -A y^2/n_0 + ...,
    u = -A^3 y^5/(20 n_0^2) + ...,   v = -A^2 y^3/(3 n_0^2) + ...,
where the dots are lower powers of y. For example 3n_0 r' = 2m' - (6l - 1)A determines r, and the leading coefficient
of v is (8(A^2/(4n_0)) - 2(-3A/2)(-A/n_0))/(3n_0). The coefficient of y^5 in E is therefore
    2(-3A/2)(-A^2/(3 n_0^2)) - 2(A^2/(4n_0))(-A/n_0) + A^3/(10 n_0^2) = 8A^3/(5 n_0^2) != 0,
which is impossible for a polynomial vanishing on an open interval. So A = 0.
Step 8 (c != 0). Suppose A != 0. In the variable z > 0 all functions of Step 6 extend as finite power-log sums
(integrate the equation for b, solve the Euler equation for r, integrate u, use the formula for v); they are real
analytic on z > 0, so E = 0 there. As z -> inf, with the same asymptotics for derivatives,
    m = -A z^3/(2c^2) + ...,   b = A^2 z^5/(20 n_0 c^4) + ...,   r = -A z^(8/3)/(3 n_0 c^2) + ...,
    u = -A^3 z^6/(120 n_0^2 c^5) + ...,   v = 7A^2 z^(11/3)/(270 n_0^2 c^3) + ...,
where the dots have strictly smaller exponents (logarithms allowed). For r the operator after division by n_0 c is 3z
d_z - 1, with multiplier seven on z^(8/3). With m_3 = -A/(2c^2), b_5 = A^2/(20 n_0 c^4) and r_{8/3} = -A/(3 n_0 c^2),
the leading coefficient of v is c(28 b_5 - 7 m_3 r_{8/3})/(9 n_0), the value displayed. The largest exponent in E is
20/3, with coefficient
    2(-A/(2c^2))(7A^2/(270 n_0^2 c^3)) - (7c/3)(A^2/(20 n_0 c^4))(-A/(3 n_0 c^2)) + A^3/(60 n_0^2 c^5)
    = 4A^3/(135 n_0^2 c^5) != 0,
contradicting E = 0. So A = 0, and a = 0 on the component of {n != 0} containing 0. If the affine n has a zero in I,
a/n is constant on both sides, and continuity of a' at the simple zero forces the constant on the other side to be 0.
So a = 0 on I, the actual density degree is two with M = 3, and Steps 2-4 give the polynomial solution.
Step 9 (N = 2 and M <= 2). In the notation of Step 1, a = n = 0 and m is affine. Near 0, f > 0, the coefficient of x^3
gives (m/f)' = 0 there and m(0) = 0, so m = 0 near 0 and, being affine, on I. The remaining even equations are
    b f' = 2(b' - beta) f,   b'' = -2f,   f(0) = 1,   b(0) = 0,   b'(0) = beta.
Put p = b' - beta; then p' = -2f, so p is C^2, and
    b p'' = 2p p',   b p' = beta p + 3p^2/2,
the second by differentiating both sides and evaluating the constant at 0. Since p'(0) = -2, p is nonzero for small
nonzero y; there p' = -2f gives f' = -4f^2/(beta + 3p/2) and f = (1 + 3p/(2 beta))^(4/3) (the derivative of
log f - (4/3) log(1 + 3p/(2 beta)) is 0 and its limit at 0 is 0). With h = (1 + 3p/(2 beta))^(-1/3),
    h' = 1/beta,   h = 1 + y/beta,   f = h^(-4),   b = beta^2 (h - h^(-2))/3,
which is Proposition 3.15 near 0. Away from b = 0 the equations for b, b' and f are an ordinary differential equation
with locally Lipschitz right side; the displayed solution has f > 0 and no zero of b other than 0 on (-beta, inf), so
by uniqueness the equality cannot stop at a finite interior point larger than -beta, and it cannot stop at -beta
inside I because f -> inf there, against continuity. Hence I is contained in (-beta, inf) and the formulas hold on I.
Step 10 (the odd density term and the remaining gauge). With m = n = a = 0 the equations for g and u are
    b g' = (1 - 2l + b') g + 2f u,   u' = -g,   u(0) = 0.
By Step 9, b = beta y + O(y^2) and (1 - 2l + b')/b = kappa/y + O(1) with kappa = 1/(2 beta) < 1. On a small positive
interval choose a positive integrating factor phi with phi'/phi = (1 - 2l + b')/b; it is y^kappa times a positive
continuous function bounded above and below, so phi(y)/phi(eta) <= C (y/eta)^kappa for 0 < eta <= y. Since g = O(y^2),
u' = -g and u(0) = 0 give u = O(y^3), and variation of constants from 0 is valid:
    g(y) = phi(y) int_0^y 2f(eta) u(eta)/(b(eta) phi(eta)) d eta.
With H(y) = max_{0 <= eta <= y} |g(eta)|, |u(eta)| <= eta H(y) and |b(eta)| >= beta eta/2 give
    |g(y)| <= C H(y) int_0^y (y/eta)^kappa d eta = C y H(y)/(1 - kappa),
and taking the maximum forces H(y) = 0 for small y. The same estimates hold on the negative side, so g = u = 0 near 0;
b is nonzero on either side throughout I, and uniqueness for the linear system gives g = u = 0 on I, so t is constant.
Finally b k' = k; on either punctured side its nonzero solutions are C_+- |y|^(1/beta) exp(O(|y|)) (integrate
1/b = 1/(beta y) + O(1)), and k = O(|y|^3) with 1/beta < 1 forces C_+ = C_- = 0; uniqueness away from 0 gives k = 0 on
I.
Step 11 (verification). For Proposition 3.15 direct differentiation gives b'' = -2f, b f' = 2(b' - beta) f,
-Lap(x(b - ly)) = 2fx = rho_x and V.grad(f x^2) = (2(2l - b') f + b f') x^2 = f x^2, with f(0) = 1, b(0) = 0 and
b'(0) = beta, which give the jet and W(0) = 0. For the polynomial solution, V = (x/2, beta y - x^2), -Lap psi = 2x and
V.grad(x^2) = x^2. An interval containing 0 on which the first solution is smooth cannot contain -beta, so it is not
R. All arguments keep the actual degree M unrestricted; the classification through degree three in x, and only that,
follows.

### 9.19 Proposition 2.2 (polynomial solutions with the jet)
Notation as in Proposition 2.2: {F, G} = F_x G_y - F_y G_x, beta = 2l - 1/2, rho_k and psi_k are the homogeneous parts
of degree k (absent parts are zero), N = deg rho and M = deg psi. The transport equation reads l(x rho_x + y
rho_y) + {psi, rho} = rho.
Step 1 (the quadratic jet). The hypotheses remove the constant and linear parts of rho and psi and give rho_2 = x^2.
Writing psi_2 = a(x^2 - y^2)/2 + bxy + c(x^2 + y^2)/2, the constant part of the Poisson equation and the quadratic
part of the transport equation give
    -Lap psi_2 = -2c = 0,   (2l - 1)x^2 + {psi_2, x^2} = (2l - 1 - 2b)x^2 + 2(a - c)xy = 0,
so a = c = 0 and psi_2 = (l - 1/2)xy. For the asserted solution, V = (lx - psi_y, ly + psi_x) = (x/2, beta y - x^2),
-Lap psi = 2x = rho_x and V.grad rho = x^2 = rho, for every real l.
Step 2 (the homogeneous recursion). For k >= 3 put D_k R = (kl - 1)R + {psi_2, R} on homogeneous polynomials of degree
k. Then, with p + q = k,
    {psi_2, x^p y^q} = (l - 1/2)(q - p) x^p y^q,   D_k(x^p y^q) = (p/2 + beta q - 1) x^p y^q,
with no off-diagonal term, while {-x^3/3, R} = -x^2 R_y raises the degree by one. Homogeneous comparison gives
    -Lap psi_k = (rho_{k-1})_x,   D_k rho_k + {psi_k, x^2} + sum_{i=3}^{k-1} {psi_i, rho_{k+2-i}} = 0,
the sum being empty for k = 3. The Poisson equation determines psi_k up to a homogeneous harmonic polynomial of degree
k (a two-dimensional space); a particular solution of Lap P = S for homogeneous S is the terminating sum
P = sum_{j >= 0} (-1)^j (I_x^2)^(j+1) (d_y^2)^j S, where I_x^2 is the double antiderivative in x with zero constants,
whose Laplacian telescopes to S. For l > 5/12, beta > 1/3 and p/2 + beta q - 1 >= (p + q) min(1/2, beta) - 1 > 0 for
p + q >= 3, so the recursion is invertible, in particular for every l > 1.
Step 3 (homogeneous Jacobians). Let f and g be nonzero homogeneous polynomials of positive degrees m and n. Euler's
identities give
    m f g_x - n g f_x = -y {f, g},   m f g_y - n g f_y = x {f, g},
and d_j(g^m/f^n) = g^(m-1) f^(-n-1)(m f d_j g - n g d_j f). If {f, g} = 0, both partial derivatives of the rational
function g^m/f^n vanish, so it is constant (in characteristic zero, regard it first as a rational function of x over
R(y), then of y): g^m = kappa f^n for a nonzero real kappa.
Step 4 (degree bounds and top parts). The jet gives N >= 2, and the term 2x of rho_x forces psi_3 != 0, so M >= 3. The
terms of degree M + N - 2 of the transport equation give {psi_M, rho_N} = 0, hence rho_N^M = kappa psi_M^N (the linear
terms have degree at most N and there are no other brackets of that degree). If M > N + 1, the Poisson equation makes
psi_M harmonic, psi_M = A z^M + Abar zbar^M with z = x + iy and A != 0, which as a polynomial in z/zbar has M distinct
nonzero roots and no factor zbar; its linear factors are distinct, and comparing the multiplicity of one of them in
the power identity shows that M divides N, against M > N + 1. So M <= N + 1. If M = N + 1, the degrees are coprime,
and unique factorization in R[x, y] makes every irreducible multiplicity of rho_N divisible by N, so rho_N = mu
(e.X)^N with |e| = 1, and the power identity gives psi_{N+1} = lambda (e.X)^(N+1). The top part of the Poisson
equation is
    -lambda N(N + 1)(e.X)^(N-1) = mu N e_1 (e.X)^(N-1),
so lambda(N + 1) = -mu e_1 and e_1 != 0. If M <= N, the term of degree N - 1 of rho_x has no counterpart in -Lap psi,
so (rho_N)_x = 0 and rho_N = mu y^N; then the top Jacobian identity mu N y^(N-1) (psi_M)_x = 0 gives psi_M = lambda
y^M.
Step 5 (density degree two). If N = 2, then rho = x^2, and transport reduces to (2l - 1)x^2 - 2x psi_y = 0, so
psi_y = (l - 1/2)x and psi = (l - 1/2)xy + F(x); Poisson gives F'' = -2x, F = -x^3/3 + Ax + B, and the hypotheses give
A = B = 0.
Step 6 (density degree three). Suppose N = 3. If M = 3, Step 4 gives psi_3 = lambda y^3, and -Lap psi_3 = -6 lambda y
cannot equal (rho_2)_x = 2x. So M = 4, and Step 4 with e_1 != 0 allows rho_3 = mu (x + ty)^3 with mu != 0 and t real.
Write psi_3 = A x^3 + B x^2 y + C x y^2 + D y^3. The Poisson equation in degree one gives 6A + 2C = -2 and
2B + 6D = 0, and the transport equation in degree three (Step 2) gives
    mu/2 - 2B = 0,   3 mu t beta - 4C = 0,   3 mu t^2 (2 beta - 1/2) - 6D = 0,   mu t^3 (3 beta - 1) = 0.
The first and third, substituted into 2B + 6D = 0, give 1 + 6t^2 (2 beta - 1/2) = 0. This is impossible if t = 0; if
t != 0, the fourth gives beta = 1/3 and then 1 + t^2 = 0, impossible for real t. So N = 3 does not occur, for every l.
Step 7 (resonances). Let l > 1/4, so beta > 0. A resonant monomial of degree at least three satisfies p/2 + beta q = 1
with p + q >= 3. The case q = 0 would give p = 2, so q > 0, and then p = 0 (beta = 1/q, q >= 3) or p = 1
(beta = 1/(2q), q >= 2); the second family is contained in the first (n = 2q), and the resonant values are
l = 1/4 + 1/(2n), n >= 3, the largest being l = 5/12. The cubic resonances l = 5/12 (y^3) and l = 3/8 (x y^2) are
covered by Step 6. A zero diagonal entry leaves a density coefficient potentially free and is only a compatibility
condition; Steps 8-14 prove the degree-six assertion away from the resonances, and Steps 15-21 the remaining
assertions.
Step 8 (a repeated irreducible factor through 0). From now on l > 1/4, beta is not resonant, and, seeking a
contradiction, 4 <= N <= 6. Let D be the polynomial derivation V.grad. The equations give
    div V = 2l,   curl V = -rho_x,   V(0) = 0,   V_1 = (x/2, beta y),
V_1 the linear part of V. There is a unique formal power series h = x + O(|X|^2) with D h = h/2: in degree k >= 2 the
diagonal coefficient of x^p y^q is p/2 + beta q - 1/2, which is positive if p >= 1 and vanishes for p = 0 only at
beta = 1/(2q), q >= 2, which is excluded. The series h^2 solves D(h^2) = h^2 with the quadratic jet of rho, and in
every degree at least three the difference rho - h^2 meets the invertible diagonal operator of Step 2; hence rho = h^2
in R[[x, y]] (no convergence of h is used). Since h_x(0) = 1, there is a unique formal series f(y) with f(0) = 0 and
h(f(y), y) = 0, so rho(f(y), y) = rho_x(f(y), y) = 0. The series f is algebraic over R(y), since rho is a nonzero
polynomial involving x; clearing the denominators of its minimal polynomial gives a primitive irreducible P in R[x,
y], and Gauss's lemma gives P | rho and P | rho_x. As P depends on x it does not divide P_x, so factoring rho and
differentiating in x shows P^2 | rho. Also P(0) = 0, and since rho has order exactly two at 0, P has order one with
linear part a nonzero multiple of x, normalized to x:
    rho = P^2 Q,   P = x + O(|X|^2),   Q(0) = 1,   1 <= deg P <= 3.
P does not divide Q (Q(0) = 1); applying D and cancelling one P gives 2Q DP + P DQ = PQ, so P | DP and the curve
{P = 0} is invariant.
Step 9 (an invariant coordinate axis). Let (u, v) be polynomial coordinates with polynomial inverse and nonzero
constant Jacobian, fixing 0, with P = u and rho = u^2 Q(u, v), Q(0, 0) = 1. Such changes preserve the divergence.
Write Du = u A(u, v), Dv = T(u, v), F(v) = Q(0, v) and T_0(v) = T(0, v). The density equation (after cancelling u^2,
on u = 0) and the divergence equation give
    2A(0, v) F + T_0 F' = F,   A(0, v) + T_0' = 2l.
At v = 0, centring and F(0) = 1 give A(0, 0) = 1/2, hence T_0(0) = 0, T_0'(0) = beta and T_0 F' = 2(T_0' - beta)F. If
deg F <= 3, then T_0 = beta v and F = 1: with m = deg T_0 >= 1 (beta > 0) and d = deg F, if m >= 2 the coefficient of
degree m + d - 1 gives d = 2m >= 4; so T_0 = beta v, and beta v F' = 0 gives F = F(0) = 1.
Step 10 (a linear factor). If deg P = 1, then P = x. By Step 4 the top density part is a power of one real linear
form, divisible by x^2, so rho_N = mu x^N, Q_{N-2} = mu x^(N-2) and deg Q(0, y) <= N - 3 <= 3. Step 9 in the original
coordinates gives invariance of {x = 0} with tangential velocity beta y:
    psi(0, y) = 0,   psi_x(0, y) = (beta - l) y = (l - 1/2) y,
the first from psi_y(0, y) = 0 and psi(0, 0) = 0. These are the Cauchy data of the polynomial solution. In degree
three the Poisson equation makes psi_3 + x^3/3 harmonic with zero Cauchy data on {x = 0}; a harmonic polynomial
H = sum h_j(y) x^j with H(0, y) = H_x(0, y) = 0 vanishes, since (j + 2)(j + 1) h_{j+2} = -h_j'' and h_0 = h_1 = 0. So
psi_3 = -x^3/3, and the invertible transport equation gives rho_3 = 0. Inductively each further stream correction is
harmonic with zero Cauchy data and each density correction vanishes, so (rho, psi) is the polynomial solution, against
N >= 4.
Step 11 (nonlinear coordinate squares). Suppose rho = P^2 with P = x + f(v), v = ax + by, b != 0, f(0) = f'(0) = 0 and
deg f >= 2. Put u = P and K = a^2 + b^2; (u, v) has constant Jacobian b and polynomial inverse. The density equation
gives Du = u/2, and div V = 2l gives a polynomial H(u) with
    Dv = beta v + H(u),   H(0) = 0,   H'(0) = a(1/2 - beta),
the last from the linear velocity (x/2, beta y) at 0. With g = f'(v) and T = beta v + H(u),
    V_x = u/2 - g T,   V_y = (T - a V_x)/b,   d_x = (1 + a g) d_u + a d_v,   d_y = b g d_u + b d_v,
and direct differentiation gives
    b curl V = (1 + 2a g + K g^2) H'(u) + K f''(v) H(u) + K beta v f''(v) + (beta - 1/2)(a + K g),
while curl V = -rho_x gives b curl V = -2b u(1 + a g). Since K > 0 and f'' is a nonzero polynomial, a degree r >= 2 of
H would leave the term K f'' H alone in degree r in u; so H(u) = r_0 u with r_0 = a(1/2 - beta), and comparing the
coefficients of u gives K r_0 f''(v) = -2b(1 + a f'(v)). If a != 0 the right side has degree deg f - 1 in v and the
left side smaller degree or is zero; if a = 0 then r_0 = 0 and the identity reads 0 = -2b. Both are impossible.
Step 12 (a quadratic factor). If deg P = 2, then P_2^2 divides the top density part, and Step 4 gives P = x + c L^2,
L = ax + by, c != 0; b = 0 would make P divisible by x, so b != 0. In the coordinates u = P, v = L (Jacobian b), deg
Q <= 2 with top part a power of L if Q is nonconstant, and substituting x = u - c v^2, y = (v - a(u - c v^2))/b gives
Q(u, v) = 1 + alpha u + gamma v + delta v^2. Step 9 applies (deg F <= 2) and gives gamma = delta = 0, so rho = u^2
(1 + alpha u), and the density equation becomes (2 + 3 alpha u) Du = u(1 + alpha u). If alpha != 0, at u = -2/(3
alpha) the left side vanishes and the right side is -2/(9 alpha). So alpha = 0, rho = P^2, and Step 11 excludes this
P.
Step 13 (a cubic factor has no complex critical point). If deg P = 3, then N = 6, Q = 1, rho = P^2, DP = P/2 and
P = x + P_2 + P_3 with P_3 = c L^3, c != 0 (Step 4). The real irreducible cubic P is irreducible over C (nonreal
irreducible factors come in conjugate pairs of equal degree, and a conjugation-invariant factor is real up to a
scalar). By DP = P/2 every complex critical point lies on {P = 0}. The singular points are finite: P and P_x are
coprime, and the Euclidean algorithm over C(y) with cleared denominators puts a nonzero polynomial in y in their
ideal; at each such y, P is a nonzero polynomial in x (a vertical line is not a factor of P). V vanishes at each
singular point: along the local flow of V,
    D P = P/2,   D(grad P) = (1/2) grad P - (DV)^T grad P,
so uniqueness for these linear ordinary differential equations preserves P = grad P = 0, and a continuous local orbit
in a finite set is constant (only the local flow is used). Translate a singular point to 0, let A be the linear part
of V there (tr A = 2l) and write P = H_2 + H_3; H_2 != 0, since otherwise P would be a binary cubic form, which
factors over C. The quadratic part of DP = P/2 is (AZ).grad H_2 = H_2/2. If H_2 is nondegenerate with symmetric
Hessian S, then A^T S + S A = S/2 and 2 tr A = 1, so l = 1/4. If H_2 has rank one, in complex linear coordinates with
H_2 = u^2 the linear velocity has D_1 u = u/4 and D_1 v = c_0 u + d_0 v; the coefficient h of v^3 in H_3 is nonzero
(otherwise u | P), and the cubic part of DP = P/2 restricted to u = 0 gives 3 d_0 h = h/2, so d_0 = 1/6 and
2l = tr A = 1/4 + 1/6, i.e. l = 5/24. Both contradict l > 1/4, so P has no complex critical point.
Step 14 (end of the cubic case). If L is proportional to x, write P = x + A x^2 + B xy + C y^2 + c x^3. If C != 0,
P_y = 0 gives y = -Bx/(2C) and P_x = 0 becomes a quadratic in x with leading coefficient 3c, which has a complex root;
if C = 0 and B != 0, (0, -1/B) is critical; if B = C = 0, x divides P. So L = ax + by with b != 0, and in the linear
coordinates t = x, v = L, P = t + A t^2 + B t v + C v^2 + c v^3. If A != 0, solving P_t = 0 for t and substituting
into P_v = 0 gives a quadratic in v with leading coefficient 3c, hence a complex critical point; if A = 0 and B != 0,
put v = -1/B and solve P_v = 0 for t. So A = B = 0 and P = x + C L^2 + c L^3, which Step 11 (f(v) = C v^2 + c v^3)
excludes. The cases deg P = 1, 2, 3 are exhausted, which proves the degree-six assertion.
Step 15 (all degrees: the axis equation). Steps 15-17 and 19-21 assume l > 1/4 and beta not resonant, but no bound on
N; Step 18 assumes only l > 1/4. Without the bound N <= 6 the arguments of Steps 8 and 9 still give rho = P^2 Q with
P irreducible over R, P = x + O(|X|^2), Q(0) = 1, P not dividing Q and P | DP, and, in coordinates (u, v) as in
Step 9, T_0(0) = 0, T_0'(0) = beta and T_0 F' = 2(T_0' - beta)F; the bound enters there only through
1 <= deg P <= 3 and the last two sentences of Step 9. Let m = deg T_0 >= 1. If m = 1, then T_0 = beta v and
F = 1 (Step 9). Let m >= 2 and d = deg F. With leading coefficients tau of T_0 and phi of F, the coefficient of degree
m + d - 1 gives d tau phi = 2m tau phi (the term -2 beta F has degree d < m + d - 1), so d = 2m. Let r be a complex
zero of T_0 of order j and let k >= 0 be the order of F at r. If j >= 2, then T_0'(r) = 0, so the right side has order
exactly k at r while the left side has order at least k + 1; hence every zero of T_0 is simple. If F(r) = 0 and
T_0(r) != 0, the left side has order k - 1 at r and the right side order at least k; hence every zero of F is a zero
of T_0. At a zero r of T_0 the coefficients of (v - r)^k give
    (2 - k) T_0'(r) = 2 beta,
so k != 2, and k >= 3 gives T_0'(r) = -2 beta/(k - 2) < 0. At the complex point Z_r with coordinates (0, r),
Du = 0 and Dv = T_0(r) = 0, so V(Z_r) = 0; there A = 2l - T_0'(r) and d_v T = T_0'(r).
Step 16 (a formal saddle lemma). Let (u, v) be as in Step 9 and let Z_0 be the complex point with coordinates (0, r).
Suppose Dv(Z_0) = 0, lambda = A(Z_0) > 0 and mu = (d_v T)(Z_0) < 0, and let G be a polynomial with DG = cG for a
polynomial c and G(0, v) = (v - r)^k e(v), k >= 1, e(r) != 0. Then G = R^k H with R irreducible over C, R(Z_0) = 0,
H(Z_0) != 0 and R not dividing H; so R has multiplicity exactly k in G, and no other irreducible factor of G vanishes
at Z_0. Proof. Translate v so that r = 0 and work in C[[u, v]]. For a series f with f(0) = 0 the equation
T(u, f(u)) = f'(u) u A(u, f(u)) has in degree j >= 1 the coefficient (j lambda - mu) f_j plus terms in f_1, ...,
f_(j-1), so it has a unique solution. With w = v - f(u), the series Dw = T - f'(u) u A vanishes on w = 0, so
Du = u a_1 and Dw = w a_2 with a_1(0) = lambda and a_2(0) = mu (the term d_v(uA) vanishes at 0). On u = 0 we have
w = v and Du = 0, so DG = cG reads w a_2(w) d_w(w^k e(w)) = c(0, w) w^k e(w) there, and c(0) = k mu. On the monomials
u^p w^q the operator G -> DG - cG has the diagonal entries p lambda + q mu - k mu = p lambda + (k - q)|mu|, which are
positive for q < k, and its other terms raise the total degree and preserve the ideal (w^k); hence DG = cG gives
G = w^k U with U(0) != 0 (as G(0, w) = w^k e(w)). Since G(u, f(u)) = 0 and G is a nonzero polynomial in v over C(u),
f is algebraic over C(u); let R in C[u, v] be its minimal polynomial, made primitive. As d_v^j G(u, f(u)) = 0 for
j < k, Gauss's lemma gives R | d_v^j G for j < k. Write G = R^e H with R not dividing H. If e < k, then d_v^e G = e!
(R_v)^e H modulo R, and R divides neither R_v (which is nonzero and of smaller degree in v) nor H, against R | d_v^e
G; so e >= k. In C[[u, w]] the element w is prime and divides R; comparing the orders in w of w^k U = R^e H gives
e = k, R = w R_1 and U = R_1^k H, so R_1 and H are units. Hence H(Z_0) != 0 and R(Z_0) = 0. Steps 15 and 16 with
G = Q and c = 1 - 2A (from D(u^2 Q) = u^2 Q) give: every zero r of F of order k >= 3 is a zero of R(0, v) for an
irreducible factor R of Q over C of multiplicity exactly k, and no other irreducible factor of Q vanishes at the point
with coordinates (0, r); here lambda = 2l - T_0'(r) > 0 and mu = T_0'(r) < 0.
Step 17 (x^2 divides rho: parity). Suppose x^2 | rho. Since x does not divide Q (Q(0) = 1) and P is irreducible,
P = x, and we take (u, v) = (x, y) in Step 9. As x | Dx = lx - psi_y, psi_y(0, y) = 0, and psi(0, y) = 0 since
psi(0) = 0. Suppose that rho_j is even and psi_j is odd in x for 2 <= j < k, where k >= 3 (for j = 2 by Step 1). The
part E of psi_k even in x satisfies Lap E = 0, as (rho_(k-1))_x is odd in x, and E(0, y) = psi_k(0, y) = 0,
E_x(0, y) = 0; by the Cauchy-data argument of Step 10, E = 0. Then {psi_k, x^2} and the brackets {psi_i, rho_(k+2-i)},
3 <= i <= k - 1, are even in x, and the transport equation of Step 2, whose operator D_k is diagonal on monomials and
invertible, makes rho_k even. So rho is even and psi is odd in x, and by Step 4 rho_N = mu x^N with N even. If
m = 1 in Step 15, then ly + psi_x(0, y) = Dy(0, y) = T_0(y) = beta y, which with psi(0, y) = 0 gives the Cauchy data
of Step 10, and the argument there gives the polynomial solution.
Step 18 (densities x^2 (by + g(x))^k). Let l > 1/4 and suppose rho = x^2 S^k with S = by + g(x), b real and nonzero,
g a real polynomial with g(0) = 1 and k >= 1. If deg g <= 1, the top density part x^2 (by + g_1 x)^k has two
non-proportional linear factors, against Step 4; so d = deg g >= 2. Cancelling x S^(k-1) in D rho = rho gives
2S Dx + kx DS = xS; as x does not divide S, Dx = xA with a polynomial A, and then DS = (1 - 2A)S/k. In the coordinates
(x, S), which have constant Jacobian b and polynomial inverse, A is a polynomial in (x, S), and div V = 2l reads
    k x A_x - 2 S A_S + (k - 2) A = 2kl - 1.
At 0, where (x, S) = (0, 1), the linear part (x/2, beta y) of V (Step 1: psi_2 = (l - 1/2)xy) gives A(0, 1) = 1/2. The
operator on the left multiplies x^p S^q by kp - 2q + k - 2. If k = 2, the constant term gives 0 = 4l - 1. If k is odd,
no monomial with p = 0 is in the kernel, so A(0, S) = (2kl - 1)/(k - 2), and A(0, 1) = 1/2 gives l = 1/4. Both are
excluded, so k = 2m with m >= 2, the kernel is spanned by the monomials x^p S^(m(p+1)-1) = S^(m-1) (x S^m)^p, and
    A = C + S^(m-1) H(x S^m),   C = (4ml - 1)/(2m - 2),   H a polynomial,
with H(0) = 1/2 - C = -m beta/(m - 1) != 0. Let n = deg H and let g_d be the leading coefficient of g. In (x, y) the
term S^(m-1) (x S^m)^p has degree p + (m(p + 1) - 1)d, increasing in p, and its top part is a multiple of a power of
x; so the top part of A is a nonzero multiple of x^a, a = n + (m(n + 1) - 1)d. In the original coordinates
    Dx = xA,   b Dy = DS - g'(x) Dx = (1 - 2A)S/(2m) - x g'(x) A,
and the top part of b Dy is -(d + 1/m) g_d x^d times the top part of A, a nonzero multiple of x^(a+d). Since d >= 2,
deg d_y(Dx) <= a < a + d - 1 = deg d_x(Dy), so deg curl V = a + d - 1 = (md + 1)n + md - 1, while deg rho_x = 2md + 1.
As curl V = -rho_x, (md + 1)n = md + 2, which has no integer solution n since md + 1 < md + 2 < 2(md + 1). This proves
the assertion on the densities x^2 (by + g(x))^k.
Step 19 (x^2 divides rho: density degree at most eleven). Assume NR, x^2 | rho and rho != x^2. By Step 17, P = x and
m >= 2 in Step 15, so deg F = 2m. As F(0) = 1, every zero of F is one of the m - 1 nonzero zeros of T_0, so some zero
r of F has order k >= 3, and Steps 15 and 16 give an irreducible factor R of Q over C with multiplicity k and
R(0, r) = 0. By Step 17 the top part of every factor of Q is a multiple of a power of x; a factor of degree one is
then a multiple of x + e with e != 0 (x does not divide Q) and has no zero on x = 0. So deg R >= 2, R != x, and
R(0, y) has degree at most deg R - 1; this proves the last assertion on x^2 | rho. Now let N <= 11. Then
N <= 10 (Step 17), deg Q <= 8 and k deg R <= 8, so deg R = 2 and k is 3 or 4. If k = 3, the product of the other
factors of Q has degree at most 2 and top part a multiple of a power of x, so its restriction to x = 0 has degree at
most 1, and deg F <= 3 + 1 = 4; hence deg F = 4, m = 2, and F has a zero r' of order one, with r' != r by Step 16; but
then r and r' are two nonzero zeros of the quadratic T_0, which has only one. If k = 4, then Q = R^4, and after
normalizing R(0) = 1, R = by + g(x) with g of degree 2 and g(0) = 1; R is real, since otherwise its conjugate would be
a further factor of Q, and b != 0 since R(0, r) = 0. Step 18 excludes this. So N <= 11 forces rho = x^2.
Step 20 (density degree seven: a quadratic factor). Assume NR and N = 7, so 2 deg P <= 7 in Step 8. If deg P = 1, then
P = x, against N odd (Step 17). Let deg P = 2. As in Step 12, P = x + c L^2, L = ax + by, c != 0, b != 0. In the
original (x, y) coordinates, Q has degree 3 and cubic part a nonzero multiple of L^3. In the polynomial coordinates
u = P, v = L, substituting x = u - c v^2, y = (v - a(u - c v^2))/b shows deg F <= 4. If m >= 2 in Step 15, then m = 2,
deg F = 4 and all zeros of F equal the nonzero zero of the quadratic T_0, a zero of order 4. Steps 15 and 16 then give
a factor of multiplicity 4 of Q. Polynomial automorphisms preserve factor multiplicities, so this would give a factor
of multiplicity 4 of the original cubic Q, which is impossible. So T_0 = beta v and F = 1, and P divides Q - 1. Since
Q - 1 has degree 3 in the original coordinates and cubic part a multiple of L^3, Q = 1 + u(alpha + gamma v) with
gamma != 0. Put w = alpha + gamma v; the coordinates (u, w) have constant Jacobian and polynomial inverse. With
Du = uA and Dw = Y, the density equation for rho = u^2 (1 + uw) gives uY = 1 - 2A + uw(1 - 3A), so A = 1/2 + uB with a
polynomial B, Y = -2B - w/2 - 3uwB, and div V = 2l becomes
    u^2 B_u - uB - (2 + 3uw) B_w = 2l.
Give u the weight 1 and w the weight -1. Each term of the operator on the left raises the weight by one, so the
constant 2l comes from the part of B of weight -1, which is w H(uw) with a polynomial H; with z = uw,
    u^2 (wH)_u - uwH - (2 + 3uw)(wH)_w = -2 (z(z + 1)H(z))'.
So (z(z + 1)H)' = -l, z(z + 1)H = -lz, and z = -1 gives l = 0, a contradiction.
Step 21 (density degree seven: a cubic factor). Let deg P = 3, so deg Q = 1, and by Step 4 the top parts of P and
Q are multiples of powers of one linear form. Put v = Q and let t be the linear form with grad t a unit vector
orthogonal to grad v. The coordinates (t, v) have constant Jacobian J, Lap = d_t^2 + K d_v^2 with K = |grad v|^2 > 0,
x d_x + y d_y = t d_t + (v - 1) d_v and {F, G} = J {F, G}_(t,v). As the cubic part of P is a multiple of (v - 1)^3,
P = kappa t^2 + s(v) t + h(v) with kappa real, deg s <= 1 and deg h = 3. Suppose first kappa != 0. Then rho = P^2
v = sum_(j<=4) f_j(v) t^j with f_4 = kappa^2 v and f_3 = 2 kappa s(v) v. Write psi = sum_j q_j(v) t^j, of degree M' in
t. The right side of the Poisson equation has degree at most 4 in t, so if M' > 4 its coefficient of t^(M') gives
q_(M')'' = 0, and the coefficient of t^(M'+3) in the transport equation, to which only the bracket contributes, gives
M' q_(M') f_4' - 4 q_(M')' f_4 = 0, that is M' q_(M') = 4v q_(M')', which no nonzero polynomial of degree at most one
satisfies when M' > 4. So M' <= 4, and the coefficient of t^7 in the transport equation gives
4 kappa^2 (q_4 - v q_4') = 0, that is q_4 = Cv with C real (C = 0 if M' < 4). The coefficient of t^4 in the Poisson
equation is -K q_4'' = kappa^2 d_x v, so d_x v = 0: Q = 1 + b_0 y with b_0 != 0, and we may take t = x and K = b_0^2.
Write s(v) = alpha v + delta. The coefficient of x^3 in the Poisson equation gives
    -b_0^2 q_3'' = 4 kappa^2 v,
so q_3 has degree three, and the coefficient of x^6 in the transport equation,
4 q_4 f_3' - 3 q_4' f_3 + 3 q_3 f_4' - 4 q_3' f_4 = 0, becomes
    4v q_3' - 3 q_3 = (C/kappa)(10 alpha v^2 + 2 delta v).
On v^j the left side is multiplication by 4j - 3 != 0, so q_3 has degree at most two, a contradiction. Hence
kappa = 0 and P = s(v) t + h(v), with s != 0, since otherwise P would be a real cubic in v alone, which is reducible.
If s is a nonzero constant, the coordinates (P, v) have constant Jacobian and polynomial inverse, DP = P a_1 with a
polynomial a_1, Dv = v(1 - 2a_1), and div V = 2l gives on P = 0
    1 - a_1(0, v) - 2v d_v a_1(0, v) = 2l,
so a_1(0, v) = 1 - 2l; at 0, where (P, v) = (0, 1), V = 0 gives Dv = 0 and a_1(0, 1) = 1/2, hence l = 1/4, which is
excluded. If s has a zero v_*, then h(v_*) != 0, since otherwise v - v_* would divide P. If v_* != 0, at the point
with v = v_* and 2 v_* (s'(v_*) t + h'(v_*)) + h(v_*) = 0 both derivatives of rho = P^2 v vanish while
rho = h(v_*)^2 v_* != 0, against D rho = rho. If v_* = 0, write s = sigma v and c = h(0) != 0, and put w = sigma
t + (h(v) - c)/v, a polynomial; (w, v) has constant Jacobian and P = vw + c. On the curve P = 0, parametrized by
v != 0 with w = -c/v, let Y(v) be the value of Dv and a_0(v) that of DP/P; both are Laurent polynomials in v. In the
coordinates (P, v), valid for v != 0, the area form is a constant multiple of v^(-1) dP dv, so div
V = d_P(DP) + d_v(Dv) - Dv/v, and transport and divergence on P = 0 give
    2 a_0 + Y/v = 1,   a_0 + Y' - Y/v = 2l,
hence Y' - (3/2) Y/v = beta. On a Laurent monomial y_j v^j the left side gives (j - 3/2) y_j v^(j-1), so Y = -2 beta
v. But at 0, where P = 0 and v = 1, V = 0 gives Y(1) = 0, against beta > 0. This excludes deg P = 3 and proves the
degree-seven assertion.

### 9.20 Proposition 2.3 (sublinear W_2 in the growth classes)
Step 1 (the flow). Assume the hypotheses of Proposition 2.3 and write a = 1/2, d = beta - a, r = |X|. Section 9.14,
Steps 3 and 6, give W_2 in C^{2,alpha}_loc, W_2(0) = 0, DW_2(0) = 0 and V = AX + W_2, so V is C^2 and V(Z) = AZ + N(Z)
with |N(Z)| <= C|Z|^2 and |DN(Z)| <= C|Z| near 0. Section 9.14, Step 7, gives completeness of the flow,
rho(Phi_s X) = e^s rho(X) and gamma beta >= 1; since gamma < 2, beta >= 1/gamma > 1/2 = a and d > 0. For every eta > 0
there is R_eta with |W_2(X)| <= eta r for r >= R_eta. In polar coordinates X = r(cos th, sin th), for r >= R_eta,
    r'/r = a + d sin^2 th + e_r,   th' = d sin th cos th + e_th,   |e_r| + |e_th| <= 2 eta,
with e_r = X.W_2/r^2 and e_th = (x W_{2,2} - y W_{2,1})/r^2 (W_{2,j} the components). Fix R_0 = R_{1/8}. Then
r' >= r/4 for r >= R_0. Hence a backward orbit never leaves the closed disk B_0 = {r <= R_0} once inside it and cannot
stay outside it for all negative times; every backward orbit is bounded. A forward orbit that is outside B_0 at some
time stays outside and r(s) grows at least like e^(s/4); it escapes.
Step 2 (rho vanishes in thin x-sectors). Choose eps in (0, pi/4) and eta in (0, 1/8] with q := a + d sin^2
eps + 2 eta < 1/gamma (possible since gamma a < 1) and R >= max(R_0, R_eta). If the forward orbit of X stays for all
s >= 0 in S_+ = {r >= R, |th| <= eps}, then r(s) <= r(0) e^(qs), so e^s |rho(X)| = |rho(Phi_s X)| <= C(1 + r(0)
e^(qs))^gamma, and gamma q < 1 gives rho(X) = 0. The same holds for the sector S_- around th = pi, and for any orbit
that stays in S_+ or S_- from some time on.
Step 3 (limiting directions). Fix eps in (0, pi/8) and enlarge R so that 2 eta <= (d/4) sin(2 eps) for an eta in (0,
1/8] with R_eta <= R. On {r >= R} the angular field th' then has the sign of sin(2 th) and modulus at least (d/4)
sin(2 eps) wherever th is at angular distance at least eps from the four axis directions. Consider an escaping orbit
at times when r >= R. On a band eps <= th <= pi/2 - eps (and its images under th -> th + k pi/2) th moves
monotonically toward the nearer y direction at speed at least (d/4) sin(2 eps), so the orbit crosses each band in
bounded time, never toward an x direction. The y-sectors {|th - pi/2| <= eps}, {|th + pi/2| <= eps} are therefore
forward invariant at such times, and an orbit that leaves an x-sector {|th - k pi| <= eps} never returns to it. Hence
the orbit either stays from some time on in one x-sector or from some time on in one y-sector. The same alternative
holds for every smaller eps' in (0, eps) (with a larger R), and an orbit in the x-sector of width eps that leaves the
one of width eps' at a large time must then leave the wider one; an orbit in a y-sector of width eps enters the one of
width eps' in bounded time. So th(s) converges, mod 2 pi, to 0, pi/2, pi or 3 pi/2: the orbit has a limiting direction
among +-e_1, +-e_2. By Step 2, rho = 0 on orbits with limiting direction +-e_1. If rho(X) != 0, then
    e^s |rho(X)| <= C(1 + |Phi_s X|)^gamma
forces |Phi_s X| -> infinity; its limiting direction is therefore +-e_2, so r'/r -> a + d = beta and
    log r(s) = beta s + o(s),   log|rho(Phi_s X)| = s + log|rho(X)|.
Hence log|rho| / log|X| -> 1/beta along the orbit.
Step 4 (zero orbits in both x-sectors). Take eps, R as in Step 3 and put S_+ = {r >= R, |th| <= eps}. On S_+ the
radial speed is positive, th' > 0 on th = eps and th' < 0 on th = -eps. Suppose every orbit starting on the arc
Lambda = {r = R, |th| <= eps} leaves S_+. It cannot leave through Lambda (r' > 0 there), so its first exit point lies
on one of the two sides, where the crossing is transverse. By transversality and continuous dependence on initial data
the set of starting angles whose first exit is through th = eps is relatively open in [-eps, eps], and so is the set
for th = -eps: on [0, s_0 - delta] the orbit of a starting point with first exit time s_0 keeps a positive distance
from both sides (touching a side means leaving, since the crossing is strict), and near s_0 it is close only to its
exit side. The endpoints th = eps and th = -eps leave at once through different sides. This splits the interval
[-eps, eps] into two disjoint nonempty relatively open sets, which is impossible. So some orbit stays in S_+ for all
s >= 0; it escapes, has limiting direction e_1 by Step 3, and carries rho = 0 by Step 2. The same argument around
th = pi gives an orbit with limiting direction -e_1 and rho = 0. This proves the first assertions and (a).
Step 5 (backward orbits under the hypothesis of (b)). Assume now that V vanishes only at 0. The alpha-limit set of a
backward orbit is nonempty and compact by Step 1. There is no periodic orbit: it would bound a Jordan domain D, and
the divergence theorem would give 0 = int_D div V = 2l |D| with l > 1/2. By the Poincare-Bendixson theorem (the form
used in Section 9.1, Step 7), applied to -V, the alpha-limit set contains an equilibrium, which is 0. Near 0,
X.V(X) >= (a/2)|X|^2 on a small ball B_1 about 0, so every ball about 0 contained in B_1 is invariant under the
backward flow; a backward orbit whose alpha-limit set contains 0 enters B_1 and stays there, and
d log|z|/dt <= -a + C|z| along z(t) = Phi_{-t} Z gives |z(t)| <= C e^(-at)|Z| on B_1. So every backward orbit tends to
0. Likewise no forward orbit other than 0 is bounded: by the same theorem its omega-limit set would contain 0, so for
every ball B about 0 in B_1 the orbit would lie in B at arbitrarily large times, hence, by backward invariance of B,
at all earlier times; so it would be the zero orbit. Hence every nonzero orbit escapes (forward).
Step 6 (the square root). On B_1 (shrunk if necessary) the variational equations d(D_Z z)/dt = -DV(z) D_Z z and
d(D_Z^2 z)/dt = -DV(z) D_Z^2 z - D^2 V(z)[D_Z z, D_Z z], with |DV(z) - A| <= C|z| and |D^2 V| bounded, give
|D_Z z(t)| <= C e^(-at) and, by variation of constants (forcing at most C e^(-2at), propagator between u and t at most
C e^(-a(t-u))), |D_Z^2 z(t)| <= C e^(-at). Since d(e^(at) z_1)/dt = -e^(at) N_1(z),
    e^(at) z_1(t) = x - int_0^t g_u du,   g_u(Z) = e^(au) N_1(z(u, Z)).
The first two Z-derivatives of the integrand are
    D_Z g_u = e^(au) DN_1(z) D_Z z,   D_Z^2 g_u = e^(au) (D^2 N_1(z)[D_Z z, D_Z z] + DN_1(z) D_Z^2 z),
so g_u and both derivatives are at most C e^(-au) uniformly for Z in B_1, and g_u and D_Z g_u are at most
C|Z|^2 e^(-au) and C|Z| e^(-au). So e^(at) z_1(t) converges in C^2(B_1) to xi_loc = x + O(|Z|^2), with
D xi_loc = (1, 0) + O(|Z|) and hence D xi_loc != 0 on B_1 after shrinking. Transport and the jet give
rho(Z) = e^t rho(z(t)) = (e^(at) z_1(t))^2 + e^t O(|z(t)|^3), and e^t |z(t)|^3 <= C e^(-t/2) since a = 1/2. So
rho = xi_loc^2 on B_1. The limit formula gives xi_loc(Phi_{-s} Z) = e^(-as) xi_loc(Z). For X in the plane choose T
with Phi_{-T} X in B_1 (Step 5) and put xi(X) = e^(aT) xi_loc(Phi_{-T} X); this does not depend on T, is C^2 (the
condition holds on a neighbourhood of X for the same T, and Phi_{-T} is C^2), satisfies rho = xi^2 and
xi(Phi_s X) = e^(as) xi(X), i.e. V.grad xi = xi/2, and grad xi(X) = e^(aT) D xi_loc(Phi_{-T} X) D Phi_{-T}(X) != 0.
Step 7 (the zero set). Gamma = {rho = 0} = {xi = 0} is a closed embedded C^2 curve, invariant under the flow. Choose
delta > 0 and then delta' in (0, delta) such that the rectangle Q = [-delta, delta] x [-delta', delta'] lies in B_1,
d_x xi_loc > 0 on Q, and xi_loc(delta, y) > 0 > xi_loc(-delta, y) for |y| <= delta'. Then Gamma meets the interior of
Q exactly in the local arc Gamma_0 = {(h(y), y) : |y| < delta'} of a C^2 function h with h(0) = h'(0) = 0 (implicit
function theorem; xi_loc = x + O(|Z|^2)), and V_2(h(y), y) = beta y + O(y^2) on it. Every point of Gamma has its
backward orbit in Gamma and tending to 0, hence eventually in Gamma_0; so Gamma is the union of the connected sets
Phi_T(Gamma_0), T >= 0, all containing 0, and it is connected. It is not compact, since it contains the escaping zero
orbits of Step 4; so Gamma is a properly embedded line. The flow fixes 0 and preserves Gamma, so it preserves each of
the two components of Gamma minus 0; these are connected, free of equilibria and tangent to V, so each is a single
orbit leaving 0 tangentially to the y-axis (y' = beta y + O(y^2) on the local arc). Conversely, if X != 0 and the
backward orbit z(t) = Phi_{-t} X tends to 0 tangentially to the y-axis, then z_1(t) = o(|z(t)|), and
|z(t)| = O(e^(-at)) by Step 5, so the limit formula of Step 6 gives
    xi(X) = lim_{t -> infinity} e^(at) z_1(t) = 0,
i.e. X lies in Gamma. So these two orbits are the only orbits that leave 0 tangentially to the y-axis. The two zero
orbits of Step 4 lie in Gamma and have different limiting directions; so they are the two halves, with limiting
directions e_1 and -e_1. Off Gamma rho > 0, and by Steps 3 and 5 every nonzero orbit off Gamma has limiting direction
+-e_2. This proves (b).
Step 8 (x-even densities). Let J(x, y) = (-x, y) and rho(JX) = rho(X). The kernel satisfies K(JZ) = J K(Z) (K_1 is odd
and K_2 even under reflection of the angle), hence DK(JZ)J = J DK(Z), and the combined kernel k(X, Y) of Section 9.14,
Step 3, satisfies k(JX, JY) = J k(X, Y). The substitution Y -> JY preserves the principal value and the density, and
J e_2 = e_2, so W_2(JX) = J W_2(X). Since JA = AJ, V(JX) = J V(X) and V_1(0, y) = 0: the y-axis is invariant. Assume V
vanishes only at 0. For X on the y-axis the backward orbit stays on the y-axis, so z_1(t) = 0 and xi(X) = 0: the
y-axis lies in Gamma, so h = 0 and Gamma_0 is a segment of the y-axis. The zero orbit of Step 4 with limiting
direction e_1 lies in Gamma; its backward orbit tends to 0 inside Gamma, hence meets Gamma_0, a subset of the y-axis,
which is invariant; so the whole orbit lies on the y-axis. This contradicts its limiting direction e_1. Hence V has a
zero other than 0, which proves (c).

### 9.21 Proposition 2.4 (sublinear W_2 in the growth classes: the far field)
Step 1 (rescaled limits). Assume the hypotheses of Proposition 2.3; Section 9.20 applies, with its notation a = 1/2,
d = beta - a > 0, and p = 1/beta <= gamma since gamma beta >= 1. For R >= 1 and |Z| <= L the growth bounds give
    |f_R(Z)| <= C R^(-gamma) (1 + R|Z|)^gamma <= C (R^(-1) + |Z|)^gamma,
    |grad f_R(Z)| = R^(1 - gamma) |grad rho(RZ)| <= C (R^(-1) + |Z|)^(gamma - 1) <= C (1 + L)^(gamma - 1),
using gamma >= 1 in the second line. By the Arzela-Ascoli theorem and a diagonal argument every sequence
R_n -> infinity has a subsequence along which f_R converges locally uniformly; every limit f is continuous, with
|f(Z)| <= C|Z|^gamma, in particular f(0) = 0.
Step 2 (the limit equations). Put E_R(Z) = R^(-gamma) W_2(RZ) and b_R(Z) = R^(-1) V(RZ) = AZ + R^(-1) W_2(RZ). For
every eta > 0 there is C_eta with |W_2(X)| <= eta |X| + C_eta, so on |Z| <= L, since R >= 1 and gamma >= 1,
|E_R(Z)| <= eta L + C_eta/R and |b_R(Z) - AZ| <= eta L + C_eta/R; hence E_R -> 0 and b_R -> AZ locally uniformly. From
curl W_2 = -rho_x, curl_Z E_R(Z) = R^(1 - gamma) (curl W_2)(RZ) = -d_x f_R(Z). For a test function phi, integration by
parts gives
    int f_R d_x phi = -int (d_x f_R) phi = int (curl E_R) phi = -int (E_{R,2} d_x phi - E_{R,1} d_y phi),
which tends to 0; so int f d_x phi = 0, and f, being continuous with d_x f = 0 in distributions, does not depend on
x (mollify). Since div V = tr A + div W_2 = 2l, transport gives div(V rho) = V.grad rho + 2l rho = (1 + 2l) rho, and
by scaling div_Z(b_R f_R) = (1 + 2l) f_R, that is,
    -int f_R b_R.grad phi = (1 + 2l) int f_R phi.
Passing to the limit, -int f (AZ).grad phi = (1 + 2l) int f phi, i.e. div(f AZ) = (1 + 2l) f in distributions; since
div(f AZ) = (AZ).grad f + 2l f, this is (AZ).grad f = f. With f(x, y) = F(y) and test functions chi(x) vphi(y) this
reads beta y F' = F in distributions on the line. On y > 0 it gives (y^(-p) F)' = 0, so F = a_+ y^p; on y < 0 likewise
F = a_- (-y)^p; and F(0) = 0. This is the layered form of Proposition 2.4(a).
Step 3 (beta gamma > 1). Then p < gamma, and |F(y)| = |f(0, y)| <= C|y|^gamma near y = 0 forces a_+ = a_- = 0: every
limit is 0. If sup_{|Z| = 1} |f_R(Z)| did not tend to 0, a sequence R_n -> infinity with sup >= eps > 0 would have, by
Step 1, a subsequence converging uniformly on the unit circle to a limit, which is 0, a contradiction. Hence
sup_{|X| = R} |rho(X)| = o(R^gamma), i.e. rho(X) = o(|X|^gamma) uniformly in direction.
Step 4 (homogeneous limits). Suppose g >= 1 and R^(-g) rho(RZ) -> f locally uniformly on the plane minus 0, with
f nonzero and f(tZ) = t^g f(Z) for t > 0. The argument of Step 2, with test functions supported in the plane minus 0
and R^(-g) in place of R^(-gamma) (now R^(-g) W_2(RZ) -> 0 locally uniformly since g >= 1), gives d_x f = 0 and
(AZ).grad f = f in distributions on the plane minus 0. Every horizontal line y = c != 0 is connected and avoids 0, so
f(x, y) = F(y) for y != 0, and as in Step 2, F = a_+ y^(1/beta) on y > 0 and F = a_- (-y)^(1/beta) on y < 0. Since
f is nonzero and continuous, F is not identically zero on y != 0: if, say, a_+ != 0, homogeneity gives
a_+ t^g = f(0, t) = a_+ t^(1/beta), so g = 1/beta (likewise if a_- != 0). By continuity
f(x, 0) = lim_{y -> 0} F(y) = 0 for x != 0. Since g >= 1, beta <= 1, i.e. l <= 3/4, and l > 1/2 by Proposition 2.3.
This proves (a).
Step 5 (rates under the power bound). Assume |W_2(X)| <= C(1 + |X|)^(1 - delta); we may take delta <= 1. Then
W_2 = o(r). Let X(s) = Phi_s X be an escaping orbit. By Section 9.20, Step 1, r' >= r/4 once r(s) >= R_0, so
r(s) >= c e^(s/4) for s >= s_0, and the errors in the polar equations of Section 9.20, Step 1, satisfy
|e_r| + |e_th| <= C r^(-delta) <= C e^(-kappa s) with kappa = delta/4. By Proposition 2.3(a) the orbit has a limiting
direction. Let it be e_1 (the case -e_1 follows by th -> th - pi) and write z = th (lifted so that z -> 0). Then
    z' = k(s) z + f(s),   k(s) = d sin z cos z / z (k = d where z = 0),   f = e_th,   |f(s)| <= C e^(-kappa s),
and k(s) -> d, so k >= d/2 for s >= s_1. For s_1 <= s < T,
    z(s) = exp(-int_s^T k) z(T) - int_s^T exp(-int_s^t k) f(t) dt,
and exp(-int_s^T k) <= e^(-d (T - s)/2), so letting T -> infinity (z is bounded) gives
    z(s) = -int_s^infinity exp(-int_s^t k) f(t) dt,
    |z(s)| <= C int_s^infinity e^(-d (t - s)/2) e^(-kappa t) dt <= C e^(-kappa s).
Then r'/r - a = d sin^2 z + e_r = O(e^(-kappa s)) is integrable, so log r(s) - as converges and
r(s) = c_X e^(as) (1 + o(1)) with c_X > 0. If the limiting direction is e_2 (the case -e_2 is the same), put
z = th - pi/2; since sin th cos th = -sin z cos z, z' = -k(s) z + f(s) with the same k and f, and for s >= s_1
    |z(s)| <= e^(-d (s - s_1)/2) |z(s_1)| + C int_{s_1}^s e^(-d (s - t)/2) e^(-kappa t) dt <= C (1 + s) e^(-mu s),
mu = min(d/2, kappa). Then r'/r - beta = -d sin^2 z + e_r = O((1 + s)^2 e^(-mu s)) is integrable, and
r(s) = c_X e^(beta s) (1 + o(1)) with c_X > 0. If rho(X) != 0, the limiting direction is +-e_2 (Proposition 2.3(a)),
rho(Phi_s X) = e^s rho(X), and |Phi_s X|^p = c_X^p e^s (1 + o(1)) since p beta = 1; this gives the displayed limit in
Proposition 2.4(b).
Step 6 (the layered far field). Assume in addition beta gamma = 1, so p = gamma. Take eps and R as in Section 9.20,
Step 3, and a point X_0 with |X_0| > R and th(X_0) = pi/2. The sector {r >= R, |th - pi/2| <= eps} is forward
invariant and r' >= r/4 > 0 on it, so the orbit X(s) = Phi_s X_0 stays in it, r(s) is strictly increasing and tends to
infinity, and the limiting direction is e_2. By Step 5, rho(X(s))/r(s)^gamma -> a_+ := rho(X_0) c_{X_0}^(-gamma)
(zero if rho(X_0) = 0). The points X(s) and r(s) e_2 lie on the circle of radius r(s), joined by an arc of length at
most (pi/2) |X(s) - r(s) e_2| on which |grad rho| <= C (1 + r(s))^(gamma - 1); hence
    |rho(X(s)) - rho(r(s) e_2)| / r(s)^gamma <= C |X(s)/r(s) - e_2| -> 0.
Since r(s) takes every value >= r(0), rho(r e_2)/r^gamma -> a_+ as r -> infinity; in the same way, with the sector
around -pi/2, rho(-r e_2)/r^gamma -> a_- for a constant a_-. The same transfer applied to any orbit with limiting
direction +-e_2 shows that its limit rho(X) c_X^(-gamma) equals a_+ or a_- respectively. Now every limit f of Step 1
satisfies f(0, 1) = lim R^(-gamma) rho(R e_2) = a_+ and f(0, -1) = a_-, so by Step 2 all limits coincide with
f_inf(x, y) = a_+ y_+^gamma + a_- (-y)_+^gamma; by precompactness f_R -> f_inf locally uniformly, in particular
uniformly on the unit circle, which is the displayed expansion. A point X with rho(X) != 0 exists by the jet; its
orbit has limiting direction e_2 or -e_2 and limit rho(X) c_X^(-gamma) != 0 (Step 5), so a_+ or a_- is nonzero. If
rho >= 0, then a_+ and a_- are limits of nonnegative quantities. This proves (b).
Step 7 (the Hessian bound). Assume also |D^2 rho(X)| <= C (1 + |X|)^(gamma - 2). On the disk B = B(e_1, 1/2), where
|Z| >= 1/2,
    |D^2 f_R(Z)| = R^(2 - gamma) |D^2 rho(RZ)| <= C R^(2 - gamma) (R|Z|)^(gamma - 2) <= C 2^(2 - gamma),
so the gradients grad f_R are bounded and uniformly Lipschitz on B. Along a subsequence they converge uniformly on B,
and since f_R -> f_inf uniformly there, f_inf is C^1 on B with Lipschitz gradient. On B,
d_y f_inf(x, y) = gamma a_+ y^(gamma - 1) for y > 0 and -gamma a_- (-y)^(gamma - 1) for y < 0. If 1 < gamma < 2, then
0 < gamma - 1 < 1 and the Lipschitz bound at (1, 0) forces a_+ = a_- = 0, contradicting Step 6. If gamma = 1
(then beta = 1, l = 3/4), d_y f_inf = a_+ above the axis and -a_- below, and continuity forces a_- = -a_+ != 0, so one
of a_+, a_- is negative; then rho(r e_2) or rho(-r e_2) is negative for large r. Under the hypothesis of Proposition
2.3(b), rho = xi^2 >= 0, so that case is excluded as well. This proves (c).

### 9.22 Proposition 2.5 (sublinear W_2: the weak orbits and x-even profiles with nondegenerate zeros)
Step 1 (one orbit in each weak direction). Assume the hypotheses of Proposition 2.3 and use the notation of Section
9.20, Step 1 (a = 1/2, d = beta - a > 0, R_0, R_eta, e_r). Since div V = 2l (Section 9.21, Step 2), Liouville's
formula gives |Phi_s U| = e^(2ls) |U| for every bounded open set U. For r >= R_0 the radius increases strictly along
orbits, and every backward orbit enters the disk {r <= R_0} (Section 9.20, Step 1); so an orbit that escapes crosses
each circle K_R = {r = R}, R >= R_0, exactly once, and its part in {r >= R} is the graph th = th_C(r), r >= R, of a
continuous lift of the angle. Suppose that two distinct orbits C_1, C_2 have limiting direction e_1. Choose eps in
(0, pi/4) and eta in (0, 1/8] with kappa := a + d sin^2 eps + 2 eta < l (possible since a = 1/2 < l, Proposition 2.3),
and then R >= max(R_0, R_eta) such that the lifts th_1, th_2 of the two orbits that tend to 0 satisfy |th_j(r)| < eps
for r >= R. The orbits are disjoint, so th_1(r) != th_2(r) for r >= R, and we may assume th_1 < th_2 there. The open
set D = {(r, th) : r > R, th_1(r) < th < th_2(r)} lies in {r > R, |th| < eps}, where
r'/r = a + d sin^2 th + e_r <= kappa. D is forward invariant: an orbit starting in D cannot reach C_1 or C_2, which
are orbits, and cannot reach the remaining part {r = R} of the boundary of D, where r' > 0. For M > R the set
U = D intersected with {r < M} is open, bounded and nonempty, and Phi_s U is contained in D intersected with
{r < M e^(kappa s)}, so
    e^(2ls) |U| = |Phi_s U| <= pi M^2 e^(2 kappa s)   (s >= 0),
which fails for large s since kappa < l. Hence at most one orbit has limiting direction e_1, and, by the same argument
around th = pi, at most one has limiting direction -e_1; Proposition 2.3(a) gives existence. Call them C_+ and C_-.
Step 2 (the arcs). Take eps and R as in Section 9.20, Step 3, and call this radius R_3 (R_3 >= R_0). The y-sectors
{r >= R_3, |th - pi/2| <= eps} and {r >= R_3, |th + pi/2| <= eps} are forward invariant, and an orbit that lies in the
first (second) at some time has limiting direction e_2 (-e_2), the only one of the four directions of Proposition
2.3(a) in the sector. Let R >= R_3, and let P_+ and P_- be the points where C_+ and C_- cross K_R (Step 1);
P_+ != P_-. By Section 9.20, Step 1, and Proposition 2.3(a) every point of K_R has an escaping orbit with a limiting
direction among +-e_1, +-e_2, and by Step 1 only P_+ and P_- have +-e_1. Let O_+ and O_- be the sets of points of K_R
with limiting direction e_2 and -e_2. O_+ is open in K_R: if the orbit of X tends to e_2, then at some time s_* the
point Phi_{s_*} X lies in the interior of the first y-sector, and by continuity of Phi_{s_*} so does Phi_{s_*} Y for
every Y near X, so these Y have limiting direction e_2. Likewise O_- is open. Each of the two open arcs of K_R minus
{P_+, P_-} is connected and is the disjoint union of its intersections with O_+ and O_-, so it lies in O_+ or in O_-.
The point R e_2 lies in the first sector and -R e_2 in the second, so R e_2 is in O_+, -R e_2 is in O_-, and neither
is P_+ or P_-. Hence the arc containing R e_2 lies in O_+, the arc containing -R e_2 lies in O_-, these are different
arcs, and since the two arcs and P_+, P_- make up K_R, they are O_+ and O_- respectively. This proves (a).
Step 3 (the zeros under nondegeneracy). Assume now that every zero of V is nondegenerate. Let Z be a zero, M = DV(Z)
and g = grad rho(Z). As in Section 9.5, Step 1: rho(Z) = 0; differentiating V.grad rho = rho gives M^T g = g;
tr M = div V = 2l; and curl V = -rho_x (curl(AX) = 0 and curl W_2 = -rho_x) gives M_21 - M_12 = -g_1. If g != 0, then
1 is an eigenvalue of M and the other one is 2l - 1 > 0; if g = 0, then M is symmetric. In both cases the eigenvalues
are real, with sum 2l > 1, and since det M != 0 the zero is a source (both eigenvalues positive) or a saddle
(eigenvalues mu < 0 < nu with nu = 2l - mu > 2l > 1); there are no sinks. At a source Z write X = Z + Pz with
P^(-1) M P in real Jordan form, the off-diagonal entry (present only for a repeated eigenvalue) replaced by a number
small compared with the smaller eigenvalue; then z.(P^(-1) M P z) >= 2c|z|^2 for some c > 0, and since the field in
the z coordinates is P^(-1) M P z + O(|z|^2), on a small ball E_Z = {|z| < delta}
    d|z|^2/ds >= c |z|^2
along the flow. So the closure of E_Z is invariant under the backward flow, backward orbits starting in it converge to
Z, no forward orbit enters E_Z from outside, and B(Z), the increasing union of the sets Phi_n(E_Z), n = 1, 2, ..., is
open, connected and invariant. At a saddle the C^2 stable and unstable manifold theorems apply as in Section 9.5.
Step 4 (the topology; proof of (b)). The zeros of V lie in {r < R_0} (r' > 0 for r >= R_0) and are isolated
(det DV != 0), so they are finitely many. Section 9.5, Steps 3 and 4, now apply with the following changes: the radius
R of Section 9.2 is replaced by R_0, with the backward bound |Phi_(-t) X| <= max(|X|, R_0) and the escape of every
forward orbit that reaches {r >= R_0} (Section 9.20, Step 1); the facts on zeros from Section 9.5, Steps 1 and 2, are
replaced by Step 3 above, and at a source the coordinates z of Step 3 replace the diagonal coordinates; the index
count of Section 9.5, Step 3, is not used. They give: no periodic orbits and no cycles of saddle connections, since an
invariant Jordan curve would bound a bounded invariant domain D with |D| = e^(2ls) |D|; every bounded forward or
backward semiorbit converges to a single zero; every backward orbit converges to a zero, so the plane is the disjoint
union of the source basins and the unstable manifolds of the saddles; and a nonstationary forward orbit escapes or
converges to a saddle. Section 9.5, Step 5, applies with nu > 2l > 1 in place of nu > 2 and gives rho = 0 on the
stable and unstable manifolds of every saddle. This proves (b).
Step 5 (two facts near 0 for x-even densities). Assume in addition that rho is even in x. By the first part of Section
9.20, Step 8, which does not use the hypothesis that V vanishes only at 0, V(JX) = J V(X) for J(x, y) = (-x, y), so
the y-axis is invariant. Let B_1 be the ball about 0 of Section 9.20, Step 5; the estimates used there on B_1, namely
X.V(X) >= (a/2)|X|^2, the invariance under the backward flow of the balls about 0 in B_1 and
|Phi_(-t) Z| <= C e^(-at) |Z| for Z in B_1, are local and do not use that hypothesis either. So B_1 lies in B(0).
(i) For x_0 != 0 small, X_0 = (x_0, 0) lies in B_1 and rho(X_0) = x_0^2 + O(|x_0|^3) > 0. (ii) V_1(0, y) = 0 by the
invariance, and V_2(0, y) = beta y + O(y^2) since V(Z) = AZ + N(Z) with |N(Z)| <= C|Z|^2 (Section 9.20, Step 1), so
there is y_1 > 0 with L_+ = {(0, y) : 0 < y <= y_1} in B_1 and V_2 > 0 on L_+; as the flow on the invariant y-axis is
y' = V_2(0, y), L_+ lies on a single orbit O_+, which leaves 0. For Z in L_+ the backward orbit
z(t) = Phi_(-t) Z stays in L_+, so z_1(t) = 0, rho(z(t)) = O(|z(t)|^3) by the jet, and
    |rho(Z)| = e^t |rho(z(t))| <= C e^((1 - 3a) t) = C e^(-t/2) -> 0.
So rho = 0 on L_+ and, by transport, on O_+. Likewise, with L_- = {(0, y) : -y_1 <= y < 0}, rho = 0 on the orbit O_-
containing L_-.
Step 6 (the amplitudes; proof of (c)). Assume the hypotheses of (c). Proposition 2.4(b) applies and gives constants
a_+, a_- with the uniform expansion displayed there, and, since p = 1/beta = gamma,
rho(Phi_s X)/|Phi_s X|^gamma -> rho(X) c_X^(-gamma) != 0 along every orbit with rho(X) != 0. Let the orbit of X have
limiting direction e_2 and put X(s) = Phi_s X = r(s)(cos th(s), sin th(s)), so that r(s) -> infinity and
sin th(s) -> 1. For large s, (-sin th(s))_+ = 0, and the expansion gives
    rho(X(s)) / r(s)^gamma = a_+ (sin th(s))^gamma + o(1) -> a_+.
If rho(X) = 0, the left side vanishes, so a_+ = 0; if rho(X) != 0, the left side tends to rho(X) c_X^(-gamma) != 0, so
a_+ != 0. Hence either every orbit with limiting direction e_2 has rho = 0 or every one has rho != 0; likewise for
-e_2, with a_-. The orbit of X_0 (Step 5(i)) has rho(Phi_s X_0) = e^s rho(X_0) -> infinity, so it is unbounded; it
escapes (Section 9.20, Step 1), and its limiting direction is e_2 or -e_2 (Proposition 2.3(a)). Suppose it is e_2; the
case -e_2 is the same with -R e_2, a_-, L_- and O_-. Then every orbit with limiting direction e_2 has rho != 0. Take
R >= R_3 (Step 2) with |X_0| < R, and let I_+ be the arc of K_R formed by the points with limiting direction e_2
(Step 2): it is connected, it contains R e_2, and it contains the point Q_0 where the orbit of X_0 crosses K_R. Since
rho != 0 on I_+, I_+ meets no unstable manifold of a saddle, so by (b) it lies in the union of the source basins,
which are open and pairwise disjoint; being connected, it lies in one basin, and that basin is B(0) because Q_0 lies
on the orbit of X_0, which is in B_1, a subset of B(0). So the backward orbit of R e_2 converges to 0. It stays on the
invariant y-axis and does not reach the zero 0 in finite time, so it stays on the positive half-axis, enters L_+ and
therefore lies on O_+ (Step 5(ii)). Hence rho(R e_2) = 0, whereas R e_2 lies in I_+, where rho != 0. This
contradiction proves (c).
Step 7 (beyond beta gamma = 1; proof of (d) and (e)). Put nu = min(d, beta delta), where d = beta - 1/2
(Section 9.20), and m = 1 under the hypotheses of (d), m = 2 under those of (e); in both cases rho is even in x, the
zeros of V are nondegenerate, |W_2(X)| <= C(1 + |X|)^(1 - delta) and beta gamma < 1 + m nu. In Step 6 the hypothesis
beta gamma = 1 enters only through the dichotomy that either every orbit with limiting direction e_2 has rho = 0 or
every one has rho != 0, and likewise for -e_2; the part of Step 6 after the dichotomy uses only Steps 2-5,
Section 9.20, Step 1 and Proposition 2.3(a). We prove the dichotomy under the present hypotheses; Step 6 then gives
(d) and (e).
(i) The angle. Let X(s) = Phi_s X = r(s)(cos th(s), sin th(s)) have limiting direction e_2 and put z = th - pi/2. By
Section 9.21, Step 5, z' = -k(s) z + f(s) with k = d sin z cos z / z (k = d where z = 0) and f = e_th, so that
|f(s)| <= |W_2(X(s))| / r(s) (Section 9.20, Step 1), |z(s)| <= C (1 + s) e^(-mu s) for s >= s_1 and some mu > 0, and
r(s) = c_X e^(beta s) (1 + o(1)) with c_X > 0. Choose s_2 >= max(s_1, 1) such that r(s) >= 1 and
c_X e^(beta s) / 2 <= r(s) <= 2 c_X e^(beta s) for s >= s_2. Then |f(s)| <= C r(s)^(-delta) <= C e^(-beta delta s);
and since |sin u - u| <= |u|^3 / 6, |k(s) - d| <= (2d/3) z(s)^2 <= C (1 + s)^2 e^(-2 mu s), so
K = int_{s_2}^infinity |k - d| ds is finite and exp(-int_t^s k) <= e^K e^(-d (s - t)) for s_2 <= t <= s. Variation of
constants from s_2 gives, for s >= s_2,
    |z(s)| <= e^K e^(-d (s - s_2)) |z(s_2)| + C e^K I(s),   I(s) = int_{s_2}^s e^(-d (s - t)) e^(-beta delta t) dt,
and I(s) <= (s - s_2) e^(-nu s) if d >= beta delta, I(s) <= (s - s_2) e^(-d s) e^((d - beta delta) s_2) if
d < beta delta; so |z(s)| <= C (1 + s) e^(-nu s). Since e^(beta s) <= 2 r(s) / c_X and e^(beta s) >= r(s) / (2 c_X),
this gives
    |z(s)| <= C_X (1 + log r(s)) r(s)^(-nu/beta)   (s >= s_2),
where C_X, like the constants C above, depends on the orbit.
(ii) Comparison with the axis. For large s, |z(s)| <= pi/3, so X(s) = (x(s), y(s)) with
|x(s)| = r(s) |sin z(s)| <= r(s) |z(s)| and y(s) = r(s) cos z(s) >= r(s)/2. Every point (t, y(s)) with |t| <= |x(s)|
has norm between r(s)/2 and r(s). If m = 1, the bound |grad rho| <= C (1 + |X|)^(gamma - 1)
(the bounds of S; gamma >= 1) on this segment gives |rho(X(s)) - rho(0, y(s))| <= C |x(s)| r(s)^(gamma - 1). If m = 2,
d_x rho(0, y) = 0 because rho is even in x, and Taylor's formula in x with the Hessian bound (gamma - 2 < 0) gives
|rho(X(s)) - rho(0, y(s))| <= C x(s)^2 r(s)^(gamma - 2). With (i), in both cases, for large s,
    |rho(X(s)) - rho(0, y(s))| <= C_X (1 + log r(s))^m r(s)^(gamma - m nu/beta).
(iii) The dichotomy. Suppose that the orbits of X and Y both have limiting direction e_2, that rho(X) != 0 and that
rho(Y) = 0. The heights y_X(s) and y_Y(s) of Phi_s X and Phi_s Y are continuous, tend to infinity (y >= r/2) and are
bounded on bounded intervals, so every large H equals y_X(s) and y_Y(s') for some s and s', which tend to infinity
with H; and H <= r_X(s) <= 2H, H <= r_Y(s') <= 2H. Since rho(Phi_(s') Y) = 0, (ii) for Y gives
|rho(0, H)| <= C_Y (1 + log H)^m H^(gamma - m nu/beta) (with a new C_Y). For X, |rho(Phi_s X)| = e^s |rho(X)| and
e^s = (r_X(s) / c_X)^(1/beta) (1 + o(1)) >= (H / c_X)^(1/beta) (1 + o(1)), so (ii) for X gives
    |rho(X)| (H / c_X)^(1/beta) (1 + o(1)) <= (C_X + C_Y) (1 + log H)^m H^(gamma - m nu/beta)   (H -> infinity).
Since beta gamma < 1 + m nu, 1/beta > gamma - m nu/beta, and this is impossible. For -e_2 the same argument applies
with z = th + pi/2 (again z' = -k z + f, since sin th cos th = -sin z cos z), heights y <= -r/2 and the points
(0, -H). This proves the dichotomy, and with it (d) and (e).
(iv) The ranges. Since beta gamma >= 1 (Proposition 2.3), the hypothesis of (d) means beta >= 1/gamma with
(gamma - 1) beta < 1/2 (from beta gamma < 1 + d) and (gamma - delta) beta < 1 (from beta gamma < 1 + beta delta). Each
of the last two conditions holds on an interval of beta > 0 that contains 1/gamma, because gamma < 2 and delta > 0;
the first holds for every beta if gamma = 1, the second for every beta if delta >= gamma. For gamma = 1 and delta = 1
both hold for every beta, and beta >= 1, that is, l >= 3/4. In (e), 1 + 2 nu = min(2 beta, 1 + 2 beta delta);
beta gamma < 2 beta holds since gamma < 2, and beta gamma < 1 + 2 beta delta means (gamma - 2 delta) beta < 1, which
holds at beta = 1/gamma, on an interval of beta, and for every beta if delta >= gamma/2.

### 9.23 Proposition 2.6 (sublinear W_2: amplitude rigidity and exclusion without symmetry)
Step 1 (inputs). Assume the hypotheses of Proposition 2.6 and write a = 1/2, w = W_2 = (w_1, w_2), r = |X|, and
p = 1/beta, q = 1 - delta, Q = max(p/2, q), kappa = (gamma - 1 - delta)/2 as in the statement. By Section 9.20,
Step 1, w is in C^{2,alpha}_loc with w(0) = 0 and Dw(0) = 0, the flow Phi_s of V is complete,
rho(Phi_s X) = e^s rho(X), and beta >= 1/gamma > 1/2 = a; hence 0 < p <= gamma < 2, q is in [0, 1) and Q < 1. Since
a = beta p/2, max(a, beta q) = beta Q. C denotes constants independent of X and s, and C_X, c_X constants that may
depend on X. If V vanishes only at 0, Proposition 2.3(b) (Section 9.20, Steps 5-7) gives rho = xi^2 with grad xi
nowhere zero, so rho and grad rho vanish on the zero set Gamma of rho; Gamma consists of 0 and the two orbits with
limiting directions e_1 and -e_1, and every other orbit escapes, has rho > 0 and has limiting direction e_2 or -e_2.
By Proposition 2.4(b) (Section 9.21, Step 5), |Phi_s X| = c_X e^(as) (1 + o(1)) on the two orbits in Gamma minus 0 and
|Phi_s X| = c_X e^(beta s) (1 + o(1)) on every orbit not in Gamma, with c_X > 0.
Step 2 (an interior gradient bound). Let u be C^2 near the closed disk D = {|Z - X_0| <= h}, with |u| <= M_0 and
|Delta u| <= M_2 on D, and suppose that Delta u is C^1. Then
    (9.23.1)   |grad u(X_0)| <= 2 M_0/h + 3 M_2 h.
Take X_0 = 0, f = Delta u and v(Z) = (1/(2 pi)) int_D log(|Z - W|/h) f(W) dW. Since f is C^1 on D, v is C^2 in the
interior of D, continuous on D, Delta v = f in the interior, and grad v(0) = -(1/(2 pi)) int_D W f(W)/|W|^2 dW
(the Newtonian potential of a locally Holder continuous bounded function). For |Z| <= h the substitution W = Z + hT
and |T| <= 2 give |v(Z)| <= (M_2 h^2/(2 pi)) int_{|T| <= 2} |log |T|| dT = (2 log 2 - 1/2) M_2 h^2 <= 0.9 M_2 h^2, and
|grad v(0)| <= (M_2/(2 pi)) int_D |W|^(-1) dW = M_2 h. The function H = u - v is harmonic in the interior of D and
continuous on D. For a unit vector e and 0 < h' < h, the mean value property of e.grad H and the divergence theorem
give e.grad H(0) = (1/(pi h'^2)) int_{|Z| = h'} H e.n ds, so |grad H(0)| <= (2/h') sup_D |H|; letting h' -> h,
|grad H(0)| <= (2/h)(M_0 + 0.9 M_2 h^2). Adding the bound for grad v(0) gives (9.23.1).
Step 3 (proof of (a)). From div w = 0 and d_x w_2 - d_y w_1 = -d_x rho, and since w is C^2, the Laplacians are
Delta w_1 = d_x(-d_y w_2) + d_y(d_x w_2 + d_x rho) = d_x d_y rho and
Delta w_2 = d_x(d_y w_1 - d_x rho) + d_y(-d_x w_1) = -d_x^2 rho; so Delta w_1 and Delta w_2 are C^1 and, by the
Hessian bound, bounded by C(1 + |Z|)^(gamma - 2). Let |X_0| = r >= 1 and h = r^theta/4 with
theta = (3 - gamma - delta)/2; since 1 <= gamma < 2 and 0 < delta <= 1, 0 < theta < 1, so h <= r/4 and every Z in
D has 3r/4 <= |Z| <= 5r/4. Hence M_0 <= C r^q and M_2 <= C r^(gamma - 2) for u = w_1 and u = w_2 (gamma - 2 < 0), and
(9.23.1) gives |Dw(X_0)| <= C(r^(q - theta) + r^(gamma - 2 + theta)). Both exponents equal kappa:
q - theta = (2 - 2 delta - 3 + gamma + delta)/2 and gamma - 2 + theta = (2 gamma - 4 + 3 - gamma - delta)/2. Since Dw
is bounded on {r <= 1} and (1 + r)^kappa is bounded below there, |Dw(X)| <= C(1 + |X|)^kappa on the plane, and
|d_x rho| <= |d_x w_2| + |d_y w_1| <= 2|Dw| gives (a).
Step 4 (the coordinate Y; first part of (b)). Assume from now on that V vanishes only at 0. Fix X != 0 and write
X(s) = Phi_s X = (x(s), y(s)) and r(s) = |X(s)| > 0. Then r' = (a x^2 + beta y^2 + X(s).w(X(s)))/r <= beta r + |w|, so
z = 1 + r satisfies z' <= beta z + C z^q, and (z^delta)' = delta z^(delta - 1) z' <= delta beta z^delta + C delta
(q + delta - 1 = 0). Hence (e^(-delta beta s) z^delta)' <= C delta e^(-delta beta s),
z(s)^delta <= (z(0)^delta + C/beta) e^(delta beta s), and since z(0) >= 1,
    (9.23.2)   1 + |Phi_s X| <= C_1 (1 + |X|) e^(beta s)   (s >= 0),
with C_1 independent of X and s (the case X = 0 is trivial). The second component satisfies y' = beta y + w_2(X(s)),
so e^(-beta s) y(s) = y + int_0^s e^(-beta t) w_2(X(t)) dt, and by (9.23.2) and the power bound the integrand is at
most C(1 + |X|)^q e^(-beta delta t) in absolute value. Hence Y(X) = y + int_0^infinity e^(-beta t) w_2(Phi_t X) dt
exists and
    (9.23.3)   |Y(X) - y| <= C_2 (1 + |X|)^q   for every X.
The tail of the integral beyond t = T is at most C(1 + |X|)^q e^(-beta delta T)/(beta delta), uniformly for X in a
compact set, and X -> Phi_t X is continuous; so Y is continuous. If X is in Gamma minus 0, then
|y(s)| <= c_X e^(as) (1 + o(1)) with a < beta, so Y(X) = 0; Y(0) = 0. If X is not in Gamma, its orbit has limiting
direction sigma e_2 with sigma = +1 or -1 and |X(s)| = c_X e^(beta s) (1 + o(1)), so Y(X) = sigma c_X, which is
nonzero with the sign sigma. Thus Y vanishes exactly on Gamma and has the stated signs. For X not in Gamma,
rho(X(s)) = e^s rho(X) and |y(s)|^p = |Y(X)|^p e^(beta p s) (1 + o(1)) = |Y(X)|^p e^s (1 + o(1)), so
    (9.23.4)   rho(Phi_s X) / |[Phi_s X]_2|^p -> rho(X) / |Y(X)|^p > 0   (s -> infinity).
Step 5 (the horizontal displacement). Fix X not in Gamma, with Y(X) of sign sigma, and X(s) = (x(s), y(s)) as in
Step 4. By (9.23.2), |X(s)| <= C_X e^(beta s), so |w_1(X(s))| <= C_X e^(beta q s) for s >= 0. From x' = a x + w_1,
x(s) = e^(as) (x + int_0^s e^(-at) w_1(X(t)) dt), and the integral is at most C_X, C_X s or C_X e^((beta q - a) s)
according as beta q < a, beta q = a or beta q > a. In each case |x(s)| <= C_X (1 + s) e^(beta Q s) (Step 1), and
|y(s)| = |Y(X)| e^(beta s) (1 + o(1)) gives
    (9.23.5)   |x(s)| <= C_X (1 + s) |y(s)|^Q   (s >= s_X).
Since Q < 1, |x(s)| = o(|y(s)|). Moreover y' = beta y + w_2(X(s)) = beta y + o(|y(s)|), because w = o(r) and
|X(s)| / |y(s)| -> 1; enlarging s_X, sigma y' > 0 on [s_X, infinity) and sigma y(s) -> infinity. So y maps
[s_X, infinity) homeomorphically onto the closed half-line from y(s_X) in the direction sigma, and a sequence t_n in
that half-line with sigma t_n -> infinity is y(s_n) with s_n -> infinity.
Step 6 (the amplitudes; end of (b)). Under the class bound put G = gamma - 1, and under the Hessian bound put
G = kappa; by the bounds of S, respectively by (a), |d_x rho(Z)| <= C(1 + |Z|)^G, and the hypothesis is p > Q + G. Let
X, sigma and s_X be as in Step 5. For large s the horizontal segment from (0, y(s)) to X(s) has length
|x(s)| = o(|y(s)|), so its points Z satisfy |y(s)| <= |Z| <= 2 |y(s)| and (1 + |Z|)^G <= C |y(s)|^G whatever the sign
of G. By the mean value theorem and (9.23.5),
    |rho(X(s)) - rho(0, y(s))| <= C |x(s)| |y(s)|^G <= C_X (1 + s) |y(s)|^(Q + G).
Since |y(s)| >= c_X e^(beta s) for large s and Q + G < p, (1 + s) |y(s)|^(Q + G - p) -> 0. With (9.23.4), the function
F(t) = rho(0, t) / |t|^p therefore satisfies F(y(s)) -> rho(X)/|Y(X)|^p as s -> infinity, and by the last sentence of
Step 5, F(t_n) -> rho(X)/|Y(X)|^p for every sequence t_n with sigma t_n -> infinity. So the limit A_sigma of F(t) as
sigma t -> infinity exists, and rho(X) = A_sigma |Y(X)|^p for every X not in Gamma with Y(X) of the sign sigma; on
Gamma both sides of the formula in (b) vanish. By (9.23.3), Y(0, sigma R) = sigma R + O(R^q) has the sign sigma for
large R, so (0, sigma R) is not in Gamma, rho(0, sigma R) > 0 and A_sigma = rho(0, sigma R)/|Y(0, sigma R)|^p > 0.
This proves the formula in (b). For the equivalences, 1 - Q = min(1 - p/2, delta), so p > Q + gamma - 1 means
gamma < min(1 + p/2, p + delta), that is, after multiplication by beta = 1/p,
beta gamma < min(beta + 1/2, 1 + beta delta) = 1 + min(beta - 1/2, beta delta); and p > Q + kappa means
p > p/2 + kappa and p > q + kappa, that is gamma < p + 1 + delta and gamma < 2p - 1 + 3 delta.
Step 7 (proof of (c)). Assume the Hessian bound and gamma < min(2 delta + (1 - delta) p, 3 delta + 2p - 1), and
suppose that V vanishes only at 0. Since (p + 1 + delta) - (2 delta + (1 - delta) p) = 1 - delta + delta p > 0, both
conditions gamma < p + 1 + delta and gamma < 2p - 1 + 3 delta hold, so p > Q + kappa and (b) gives
rho = A_+ Y_+^p + A_- (-Y)_+^p with A_+ > 0. Let P(s) = Phi_s P_0 parametrize the orbit in Gamma with limiting
direction e_1. Along it x/r -> 1 and V_1 = a x + w_1 = a x + o(r) > 0 for s >= s_0, so x is strictly increasing on
[s_0, infinity) and tends to infinity, and for every large R there is a point P_R = (R, g(R)) of this orbit with
|g(R)| <= R. Then rho(P_R) = 0, grad rho(P_R) = 0, Y(P_R) = 0 and, by (9.23.3), |g(R)| <= C_2 (1 + 2R)^q <= C R^q.
Since 2 delta + (1 - delta) p = 2 - q(2 - p) and 2 - p > 0, the first condition says q < (2 - gamma)/(2 - p), and
(2 - gamma)/(2 - p) <= 1 because p <= gamma. Choose k with q < k < (2 - gamma)/(2 - p); then k < 1 and
k(2 - p) < 2 - gamma, that is kp > gamma - 2 + 2k. Put Z_R = (R, R^k). By (9.23.3),
Y(Z_R) = R^k + O(R^q) = R^k (1 + o(1)) > 0, so rho(Z_R) = A_+ R^(kp) (1 + o(1)). On the other hand f(t) = rho(R, t) is
C^2 with f(g(R)) = f'(g(R)) = 0, the points (R, t) with t between g(R) and R^k satisfy R <= |(R, t)| <= 2R for large
R, and there |f''| <= |D^2 rho| <= C R^(gamma - 2) (gamma - 2 < 0); since |R^k - g(R)| <= 2 R^k, Taylor's formula
gives rho(Z_R) = f(R^k) <= 2 C R^(gamma - 2 + 2k). As kp > gamma - 2 + 2k and A_+ > 0, this contradicts
rho(Z_R) = A_+ R^(kp) (1 + o(1)) for large R. So V vanishes at some point other than 0; this proves (c).
Step 8 (the ranges). If delta >= (gamma + 1)/3, then 2 delta >= 2(gamma + 1)/3 > gamma since gamma < 2, so
2 delta + (1 - delta) p > gamma, and 3 delta + 2p - 1 >= gamma + 2p > gamma; so the condition of (c) holds for every
beta allowed by Proposition 2.3, and bounded W_2 is the case delta = 1. If beta gamma = 1, then p = gamma, and the
differences 2 delta + (1 - delta) gamma - gamma = delta (2 - gamma) and
3 delta + 2 gamma - 1 - gamma = 3 delta + gamma - 1 are positive; so the condition holds for every delta in (0, 1]. In
that case (c) also follows from Proposition 2.4(c), which under the power bound, the Hessian bound and
beta gamma = 1 gives gamma = 1 and a density with negative values, while rho = xi^2 >= 0 when V vanishes only at
0 (Proposition 2.3(b)).
Step 9 (proof of (d)). Assume the Hessian bound and the condition on gamma in (c), but not that V vanishes only at 0.
The unconditional inputs in Step 1, the estimates in Steps 2-3, and the argument in Step 4 up to and including
(9.23.3) and the continuity of Y do not require that assumption; in Step 4, r(s) > 0 holds because an orbit from
X != 0 cannot reach the equilibrium 0 in finite time. Thus Y is defined and continuous on the plane and satisfies
(9.23.3). By Section 9.20, Step 1, r' >= r/4 wherever r >= R_0, so a forward orbit either stays in the disk {r <= R_0}
or escapes to infinity. On a forward orbit that stays in that disk, y(s) is bounded, so Y(X) = 0, and
rho(X) = e^(-s) rho(Phi_s X) -> 0, so rho(X) = 0. By Proposition 2.3(a) an escaping orbit has a limiting direction
among +-e_1, +-e_2, and rho = 0 on the orbits with direction +-e_1; by Proposition 2.4(b) these orbits satisfy
|Phi_s X| = c_X e^(as) (1 + o(1)), so Y = 0 on them as in Step 4, and an orbit with direction sigma e_2 satisfies
|Phi_s X| = c_X e^(beta s) (1 + o(1)), so Y(X) = sigma c_X has the sign sigma. Hence rho = 0 wherever Y = 0, and the
set {sigma Y > 0} is the union of the orbits with limiting direction sigma e_2; it is not empty, since
sigma Y(0, sigma R) > 0 for large R by (9.23.3). For X with sigma Y(X) > 0, the limit (9.23.4) without the final
inequality, and Steps 5 and 6 up to the formula rho(X) = A_sigma |Y(X)|^p, hold with the same proofs: they use only
the limiting direction sigma e_2, the rate c_X e^(beta s), (9.23.2), (9.23.3), the power bound and (a), and not the
sign of rho(X). The first lines of Step 7 show that p > Q + kappa. So there are constants A_+ and A_- (of any sign)
with
    (9.23.6)   rho = A_+ Y_+^p + A_- (-Y)_+^p   on the plane.
By Proposition 2.3(a) there is an orbit with limiting direction e_1. The argument of Step 7 applies to it and gives,
for every large R, a point P_R = (R, g(R)) of this orbit with |g(R)| <= C R^q, and rho(P_R) = 0 because rho vanishes
on the orbits with direction e_1 (the vanishing of grad rho used in Step 7 is not used here). Choose k as in Step 7,
so that q < k < 1 and kp > gamma - 2 + 2k, put h = R^k and f(t) = rho(R, t). By (9.23.3),
Y(R, g(R) + h) = h (1 + o(1)) and Y(R, g(R) - h) = -h (1 + o(1)), so by (9.23.6) f(g(R) + h) = A_+ h^p (1 + o(1)) and
f(g(R) - h) = A_- h^p (1 + o(1)). For large R the points (R, t) with |t - g(R)| <= h satisfy R <= |(R, t)| <= 2R, so
|f''| <= C R^(gamma - 2) there, and Taylor's formula at g(R), with f(g(R)) = 0, gives
    (9.23.7)   |f(g(R) + h) + f(g(R) - h)| <= C R^(gamma - 2) h^2,
    (9.23.8)   |f(g(R) + h) - f(g(R) - h) - 2h f'(g(R))| <= C R^(gamma - 2) h^2.
Since h^p = R^(kp) and R^(gamma - 2) h^2 = R^(gamma - 2 + 2k) = o(R^(kp)), (9.23.7) gives
(A_+ + A_-) R^(kp) = o(R^(kp)), so A_- = -A_+. Then (9.23.8) gives
f'(g(R)) = A_+ h^(p - 1) + o(h^(p - 1)) + O(R^(gamma - 2 + k)), and R^(gamma - 2 + k) = o(R^(k(p - 1))) because
gamma - 2 + 2k < kp; so f'(g(R)) = A_+ R^(k(p - 1)) + o(R^(k(p - 1))). The left side, d_y rho(P_R), does not depend on
k. If beta != 1, then p != 1; if moreover A_+ != 0, two choices k_1 < k_2 of k give R^((k_2 - k_1)(p - 1)) -> 1 as
R -> infinity, which is false. So for beta != 1, A_+ = A_- = 0 and rho = 0 on the plane by (9.23.6), against
rho(x, 0) = x^2 + O(|x|^3). If beta = 1, then p = 1 and (9.23.6) reads rho = A Y with A = A_+; A != 0 by the jet;
|rho - A y| = |A| |Y - y| <= C(1 + |X|)^q by (9.23.3); and rho(0, R) and rho(0, -R) have opposite signs for large R.
This proves (d). Part (d) contains (c): for beta = 1, rho takes negative values, while rho = xi^2 >= 0 when V vanishes
only at 0 (Proposition 2.3(b)).
Step 10 (a band of small density at 0). This step uses only V = (a x + w_1, beta y + w_2) with beta > a, the
regularity of w, w(0) = 0, Dw(0) = 0, transport and the jet, and no assumption on the zeros of V. Since w is C^2,
there are b_0 > 0 and K with |w(Z)| <= K |Z|^2 and |Dw(Z)| <= K |Z| for |Z| <= b_0. Fix b in (0, b_0] with K b <= 1/4.
For |Z| <= b let z(t) = Phi_(-t) Z (t >= 0), so that z' = -V(z). Since Z.(a x, beta y) >= |Z|^2/2 for Z = (x, y),
d|z|/dt <= -|z|/2 + K |z|^2 <= -|z|/4 while 0 < |z| <= b; hence z(t) stays in {|Z| <= b}, |z(t)| <= |Z| e^(-t/4), and
integrating d log|z|/dt <= -1/2 + K |z(t)| gives |z(t)| <= e^(4Kb) |Z| e^(-t/2). The derivative F(t) = D_Z z(t)
satisfies F' = -DV(z(t)) F, F(0) = I, and for v(t) = F(t) e, d|v|/dt <= (-1/2 + K |z(t)|) |v|, so
|F(t)| <= e^(4Kb) e^(-t/2). From z_1' = -a z_1 - w_1(z), e^(t/2) z_1(t) = x - int_0^t e^(s/2) w_1(z(s)) ds for
Z = (x, y); the integrand is at most C |Z|^2 e^(-s/2) in absolute value and its derivative in Z,
e^(s/2) Dw_1(z(s)) F(s), at most C |Z| e^(-s/2) in norm. So u(Z) = lim e^(t/2) z_1(t) (t -> infinity) exists, u is C^1
on {|Z| < b}, |u(Z) - x| <= C |Z|^2 and |Du(Z) - (1, 0)| <= C |Z|. By transport rho(Z) = e^t rho(z(t)), and by the jet
rho(z) = z_1^2 + O(|z|^3), so rho(Z) = (e^(t/2) z_1(t))^2 + O(|Z|^3 e^(-t/2)); letting t -> infinity, rho = u^2 on
{|Z| < b}. The map chi(Z) = (u(Z), y) is C^1 with D chi(0) = I, so by the inverse function theorem there are a_0 > 0,
b_1 > 0 and m > 0 such that chi^(-1) is defined and C^1 on the closed rectangle [-a_0, a_0] x [-b_1, b_1], maps it
into {|Z| < b}, and has |det D chi^(-1)| >= m there. Let U_0 = chi^(-1)((-a_0, a_0) x (-b_1, b_1)), a bounded open
neighbourhood of 0; on U_0, rho = u^2 >= 0, and the zero set of rho in U_0, chi^(-1)({0} x (-b_1, b_1)), has empty
interior. For T >= 0 put E_T = chi^(-1)((-a_0 e^(-T/2), a_0 e^(-T/2)) x (-b_1, b_1)), a subset of U_0. Then
0 <= rho < a_0^2 e^(-T) on E_T, and the change of variables gives
    (9.23.9)   |E_T| >= 4 m a_0 b_1 e^(-T/2)   (T >= 0),
where |E| is the area of E.
Step 11 (proof of (e)). Assume the hypotheses of (e), and put G = gamma - 1 under the first condition and G = kappa
under the second, so that p > Q + G and |d_x rho(Z)| <= C(1 + |Z|)^G by the bounds of S, respectively by (a). The part
of Step 9 that precedes (9.23.6) uses the Hessian bound and the condition on gamma only through Step 6 with G = kappa,
that is through (a) and p > Q + kappa; with G = gamma - 1 the same argument holds with the bounds of S in place of
(a). So Y is continuous on the plane with (9.23.3), and (9.23.6) holds with constants A_+ and A_- of any sign, which
are not both 0 since rho is not identically 0. For s >= 0, Y(Phi_s X) = e^(beta s) Y(X), since
e^(-beta t) [Phi_t Phi_s X]_2 = e^(beta s) e^(-beta (t + s)) [Phi_(t + s) X]_2. Let U_0, E_T, a_0, b_1 and m be as in
Step 10. If A_+ != 0, then rho = A_+ Y^p on {Y > 0} cap U_0 by (9.23.6) and rho >= 0 there by Step 10, so this set is
empty if A_+ < 0 and |Y| = (rho/|A_+|)^beta on it; if A_+ = 0, then rho = 0 on the open set {Y > 0} cap U_0, which is
therefore empty, since the zero set of rho in U_0 has empty interior. The same holds for {Y < 0} cap U_0 and A_-. So
|Y| <= C_3 rho^beta on U_0, where C_3 is the largest of the numbers |A_+|^(-beta), |A_-|^(-beta) with nonzero A_+,
A_-, and |Y| <= c_4 e^(-beta T) on E_T with c_4 = C_3 a_0^(2 beta). Since V is C^2 and the flow is complete, Phi_T is
a C^1 diffeomorphism of the plane, and by Liouville's formula
det D Phi_T(X) = exp(int_0^T div V(Phi_t X) dt) = e^((a + beta) T), because div V = a + beta + div w = a + beta. With
(9.23.9),
    (9.23.10)   |Phi_T E_T| = e^((a + beta) T) |E_T| >= 4 m a_0 b_1 e^(beta T)   (T >= 0).
Now let X_0 be in E_T and X(s) = Phi_s X_0 = (x(s), y(s)) for 0 <= s <= T. Then
|Y(X(s))| = e^(beta s) |Y(X_0)| <= c_4, so X(s) lies in the strip Sigma = {|Y| <= c_4}. On Sigma, (9.23.3) gives
|y| <= c_4 + C_2 (1 + r)^q; since q < 1 there is M with c_4 + C_2 (1 + r)^q <= r/2 + M for every r >= 0, and
r <= |x| + |y| then gives r <= 2|x| + 2M; so 1 + r <= K_0 (1 + |x|) and |y| <= K_1 (1 + |x|)^q on Sigma, with K_0 and
K_1 independent of X_0 and T. The function z(s) = 1 + |x(s)| is Lipschitz, and by x' = a x + w_1(X(s)), the power
bound and 1 + r <= K_0 (1 + |x|), z' <= z/2 + K_3 z^q for almost every s in [0, T]. As in Step 4,
(z^delta)' <= (delta/2) z^delta + delta K_3 (q + delta - 1 = 0), so z(s)^delta <= (z(0)^delta + 2 K_3) e^(delta s/2).
Since U_0 is bounded, |x(s)| <= K_4 e^(s/2) for 0 <= s <= T, with K_4 independent of X_0 and T. Hence Phi_T E_T is
contained in the rectangle {|x| <= K_4 e^(T/2), |y| <= K_1 (1 + K_4 e^(T/2))^q}, and since
1 + K_4 e^(T/2) <= (1 + K_4) e^(T/2),
    (9.23.11)   |Phi_T E_T| <= K_5 e^((1 + q) T/2) = K_5 e^((1 - delta/2) T)   (T >= 0).
By (9.23.10) and (9.23.11), 4 m a_0 b_1 e^((beta - 1 + delta/2) T) <= K_5 for every T >= 0, which is false for large
T since beta > 1 - delta/2. So the hypotheses of (e) are contradictory. Under the hypotheses of (d), the first lines
of Step 7 give p > Q + kappa; if beta != 1 these hypotheses are contradictory by (d), and if beta = 1, then
beta > 1 - delta/2 since delta > 0, and they are contradictory by (e). For bounded W_2, delta = 1 and q = 0, so
beta > 1/2 = 1 - delta/2 holds for every beta allowed by Proposition 2.3 (Step 1), the condition on gamma in (c) holds
for every gamma in [1, 2) (Step 8), and Q = p/2, so that p > Q + gamma - 1 means gamma < 1 + p/2, that is
beta gamma < beta + 1/2, which holds for every beta when gamma = 1. This proves (e).

### 9.24 Proposition 3.18 (sublevel areas, critical zeros of A and the forced correction)
Step 1 (inputs). Let rho in S be a profile, l = c_l > 1, p = 1/l, V = l X + W, and write |E| for the area of E and
e_a = (cos a, sin a). By Section 9.0 and Section 9.1, Step 1, V is in C^{2,alpha}_loc, the flow Phi_s of V is
complete, each Phi_s is a C^2 diffeomorphism of the plane, rho(Phi_s X) = e^s rho(X), div V = 2l, and
|W(X)| <= C|X|^p (1 + log|X|) for |X| >= 2. By Liouville's formula det D Phi_T = e^(2lT), so |Phi_T E| = e^(2lT) |E|
for every measurable E. By Section 9.1, Steps 4 and 5, the basin B(0) is open, rho = xi^2 on B(0) with xi in C^2, and
D xi(0) = (1, 0). None of this uses an assumption on the zeros of V. Fix R >= 2 with V.X >= l|X|^2/2 for
|X| >= R (possible by the bound on W, since p < 1), and let L and Theta be the maps of Theorem 3.1 for this R: they
are C^2, L > 0, Theta is an orientation-preserving circle diffeomorphism with Theta'(a) = R V_r(R e_a)/(l L(a)^2) > 0,
and A(Theta(a)) = L(a)^(-p) f(a) with f(a) = rho(R e_a).
Step 2 (a band at 0). The map chi(X) = (xi(X), y) is C^2 on B(0) with D chi(0) = I. By the inverse function theorem
there are a_0 > 0, b_1 > 0 and m > 0 such that chi^(-1) is defined and C^1 on a neighbourhood of the closed rectangle
[-a_0, a_0] x [-b_1, b_1], maps the rectangle into B(0) cap {|X| <= 1}, and has |det D chi^(-1)| >= m on it; these
properties persist when a_0 is decreased. For T >= 0 let E_T = chi^(-1)((-a_0 e^(-T/2), a_0 e^(-T/2)) x (-b_1, b_1)).
Then 0 <= rho = xi^2 < a_0^2 e^(-T) on E_T, and by the change of variables |E_T| >= 4 m a_0 b_1 e^(-T/2).
Step 3 (growth of orbits). Put q_1 = (1 + p)/2, which lies in (p, 1), and delta_1 = 1 - q_1. Since W is continuous and
|W(X)| <= C|X|^p (1 + log|X|) for |X| >= 2, there is C_W with |W(X)| <= C_W (1 + |X|)^(q_1) for every X. Let
X != 0 and r(s) = |Phi_s X|, which is positive since 0 is an equilibrium. Then
r' = (l r^2 + Phi_s X.W(Phi_s X))/r <= l r + |W(Phi_s X)|, so z = 1 + r satisfies z' <= l z + C_W z^(q_1), hence
(z^(delta_1))' <= l delta_1 z^(delta_1) + delta_1 C_W and
(e^(-l delta_1 s) z^(delta_1))' <= delta_1 C_W e^(-l delta_1 s). Integrating,
z(s)^(delta_1) <= (z(0)^(delta_1) + C_W/l) e^(l delta_1 s). So |Phi_s X| <= K e^(ls) for |X| <= 1 and s >= 0, with
K = (2^(delta_1) + C_W/l)^(1/delta_1).
Step 4 (proof of (a)). Fix h > 0, and let E'_T be the sets of Step 2 built with a'_0 = min(a_0, h^(1/2)) in place of
a_0. For T >= 0 and X in E'_T, rho(Phi_T X) = e^T rho(X) lies in [0, h), and |Phi_T X| <= K e^(lT) by Step 3, since
E'_T lies in {|X| <= 1}. So Phi_T E'_T is contained in {0 <= rho < h} cap {|X| <= K e^(lT)}, and
|Phi_T E'_T| = e^(2lT) |E'_T| >= 4 m a'_0 b_1 e^((2l - 1/2) T). For R' >= K, a variable radius distinct from the fixed
R of Step 1, choose T >= 0 with K e^(lT) = R'; since (2l - 1/2)/l = 2 - p/2, e^((2l - 1/2) T) = (R'/K)^(2 - p/2). This
gives the inequality of (a) at every radius R' >= K, with c = 4 m a'_0 b_1 K^(p/2 - 2) and R_0 = K.
Step 5 (the circle {|X| = R}). While r(s) = |Phi_s X| >= R, r'(s) = V.X/|X| >= l r(s)/2 >= l R/2 > 0, with V and
X evaluated at Phi_s X. Hence a forward orbit that meets the circle {|X| = R} lies in {|X| > R} at all later times and
meets the circle only once.
Step 6 (proof of (b)). By the hypotheses of Section 9.1 (from Section 9.0), DV(0) = diag(1/2, 2l - 1/2), which is
positive definite, and by Step 1, B(0) is an open neighbourhood of 0 on which rho = xi^2 with xi in C^2, xi(0) = 0 and
D xi(0) = (1, 0). Fix eps in (0, 1) so small that the closed disk {|X| <= eps} lies in B(0), that X.V(X) > 0 for
0 < |X| <= eps, and that u(s) = xi(eps e_s) satisfies |u(s) - eps cos s| <= eps/4 and |u'(s) + eps sin s| <= eps/4 for
every s; this is possible because xi(X) = x + O(|X|^2) and D xi(X) = (1, 0) + O(|X|). Then u has no zero where
|cos s| >= 1/2, and on each of the two arcs where |cos s| < 1/2 we have |sin s| > 1/2, so u is strictly monotone there
and takes values of opposite signs at the two ends; hence u has exactly two zeros s_1 and s_2, both simple. Let I_1
and I_2 be the two open arcs into which s_1 and s_2 divide the circle. Then g(s) = rho(eps e_s) = u(s)^2 is positive
on I_1 and I_2, and g(s) = c_k (s - s_k)^2 (1 + o(1)) as s -> s_k, with c_k = u'(s_k)^2 > 0 (k = 1, 2). An orbit meets
the circle C_eps = {|X| = eps} at most once, since |Phi_t X| increases strictly while 0 < |Phi_t X| <= eps. Now let
s lie in I_1 or I_2. Since rho(Phi_t(eps e_s)) = e^t g(s) -> infinity as t -> infinity and rho is bounded on
{|X| <= R}, the forward orbit of eps e_s meets the circle {|X| = R} of Step 1, by Step 5 at exactly one time
tau(s) > 0; write Phi_(tau(s))(eps e_s) = R e_(H(s)). The orbit crosses that circle transversally (X.V > 0 there), so
the implicit function theorem applied to |Phi_t(eps e_s)|^2 = R^2 shows that tau is C^1 and that H has a C^1 lift on
each of I_1 and I_2. By transport,
    (9.24.1)   f(H(s)) = e^(tau(s)) g(s) > 0.
H is injective on the union of I_1 and I_2: if H(s) = H(s'), then eps e_s and eps e_(s') lie on one orbit, which meets
C_eps only once, so s = s'. Differentiating Phi_(tau(s))(eps e_s) = R e_(H(s)) in s gives
    tau'(s) V(R e_(H(s))) + eps D Phi_(tau(s))(eps e_s) e'_s = R H'(s) e'_(H(s)).
Take the determinant of each side with V(R e_(H(s))) = D Phi_(tau(s))(eps e_s) V(eps e_s) as second column. Since
det D Phi_tau = e^(2l tau) (Step 1) and det(e'_a, V(Z)) = -V(Z).e_a, this gives
    (9.24.2)   R V_r(R e_(H(s))) H'(s) = e^(2l tau(s)) eps V_r(eps e_s),
where V_r(Z) = V(Z).Z/|Z| is positive on both circles. So H' > 0, and J_1 = H(I_1) and J_2 = H(I_2) are disjoint
nonempty open arcs of the circle. Neither is the circle minus one point, since the other is open and nonempty; so each
J_j has two distinct endpoints, and as s tends to an end s_k of I_j, H(s) tends monotonically to an endpoint of J_j.
By (9.24.1), e^(2l tau) = (f(H)/g)^(2l), and (9.24.2) becomes
    (9.24.3)   R V_r(R e_(H(s))) f(H(s))^(-2l) H'(s) = eps V_r(eps e_s) g(s)^(-2l)   on I_1 and I_2.
Fix j, an end s_k of I_j, the endpoint a_* of J_j that H(s) tends to as s -> s_k, and a point s_+ of I_j. For s in I_j
between s_k and s_+ put sigma = |s - s_k| and t = |H(s) - a_*| (along J_j), and let N(s) be the closed arc of I_j
between s and s_+. Since H is increasing, it maps N(s) onto the closed arc H(N(s)) of J_j between H(s) and H(s_+), and
integrating (9.24.3) over N(s) gives an identity between two positive numbers,
    (9.24.4)   int_(H(N(s))) R V_r(R e_a) f(a)^(-2l) da = int_(N(s)) eps V_r(eps e_v) g(v)^(-2l) dv,
both integrals taken with respect to the angle. As sigma -> 0 the right side is
(eps V_r(eps e_(s_k)) c_k^(-2l)/(4l - 1)) sigma^(1 - 4l) (1 + o(1)), which tends to infinity. Since f > 0 on J_j,
f(a_*) >= 0, and if f(a_*) > 0 the left side stays bounded; so f(a_*) = 0. Suppose that f'(a_*) != 0. Then
f(a) = d |a - a_*| (1 + o(1)) on J_j near a_*, with d = |f'(a_*)| > 0, and the left side is
(R V_r(R e_(a_*)) d^(-2l)/(2l - 1)) t^(1 - 2l) (1 + o(1)); comparing the two sides,
t = K_1 sigma^((4l - 1)/(2l - 1)) (1 + o(1)) with a constant K_1 > 0. Then (9.24.1) gives
e^(tau(s)) = f(H(s))/g(s) = (d K_1/c_k) sigma^(1/(2l - 1)) (1 + o(1)), which tends to 0, while tau(s) > 0. Hence
f(a_*) = f'(a_*) = 0. So f > 0 on J_1 and J_2, and f = f' = 0 at the two endpoints of each; in particular J_1 and J_2
are distinct components of {f > 0} (an endpoint of J_1 may also be an endpoint of J_2). By Theorem 3.1,
A(Theta(a)) = L(a)^(-p) f(a) with L > 0, and Theta is an orientation-preserving C^2 circle diffeomorphism with
Theta' > 0; at a zero a_* of f the term containing L' vanishes, so
A'(Theta(a_*)) Theta'(a_*) = L(a_*)^(-p) f'(a_*) = 0. Hence Theta(J_1) and Theta(J_2) are distinct components of
{A > 0}, open arcs with two distinct endpoints each, and every endpoint is a zero of A at which A' = 0. This proves
(b).
Step 7 (proof of (c)). By Theorem 3.1, A is C^2. Let th_0 be an endpoint of the arc Theta(J_1) of Step 6, so that
A(th_0) = A'(th_0) = 0 and A > 0 on Theta(J_1), and let Psi, lambda = p + 1 and J = J_p[A] be as in Theorem 3.16, so
that J = lambda Psi A' - p Psi' A; Psi is C^2 and Psi'' + lambda^2 Psi = sin th A' - p cos th A (Section 9.8, Step 4).
Suppose that J = 0 on an open arc I' contained in Theta(J_1) with endpoint th_0. On I', A > 0 and
p Psi' A = lambda Psi A', so with k = lambda/p = (p + 1)/p > 2, (Psi A^(-k))' = A^(-k) (Psi' - k Psi A'/A) = 0, and
Psi = C A^k on I' for a constant C (C = 0 is allowed). Write t = |th - th_0| and let M be the maximum of |A''| on a
closed arc N around th_0; M > 0, since otherwise A would be affine on N with A(th_0) = A'(th_0) = 0, hence 0 on N,
against A > 0 on I'. On N, A <= M t^2/2 and |A'| <= M t. For th in I' with t small, h = -A'(th)/M satisfies |h| <= t,
so th + h lies in the closure of I', where A >= 0, and Taylor's formula gives
0 <= A(th + h) <= A(th) + h A'(th) + M h^2/2 = A(th) - A'(th)^2/(2M); thus A'^2 <= 2 M A near th_0 on I'.
Differentiating Psi = C A^k twice, Psi'' = C k A^(k - 2) ((k - 1) A'^2 + A A''), so
|Psi'' + lambda^2 Psi| <= C_1 A^(k - 1) near th_0 on I'. Dividing the angular equation by A gives, near th_0 on I',
    (9.24.5)   sin th (log A)' - p cos th = E,   |E| <= C_1 A^(k - 2) <= C_2 t^(2k - 4).
If sin th_0 != 0, (log A)' is bounded near th_0 on I', so log A has a finite limit at th_0, against A(th_0) = 0. If
sin th_0 = 0, (9.24.5) says (log(A/|sin th|^p))' = E/sin th, and |E/sin th| <= C_3 t^(2k - 5) is integrable at th_0
because k > 2; so A/|sin th|^p has a finite positive limit at th_0, and A >= c t^p near th_0 on I' for some c > 0,
against A <= M t^2/2 and p < 1. Hence J does not vanish identically on any open arc with endpoint th_0 inside
Theta(J_1); in particular the continuous function J_p[A] is not identically zero. Section 9.3, Step 6, uses J_p[A]
only through a test function eta with int J_p[A] eta dth != 0, which therefore exists; so the conclusions of
Theorem 3.16(c) hold for rho, and the limit in Theorem 3.16(d), (2^(4p) - 1)/(4p (l - 1)^2) int J_p[A]^2 dth, is
positive. By Section 9.8, Step 4(ii), a profile that equals r^p A(th) outside a disk has J_p[A] = 0 identically; so
rho does not. This proves (c). The argument extends Section 9.8, Step 4(i), and Section 9.3, Step 5, which assume
A''(th_0) > 0.
Step 8 (an unbounded branch of Gamma). Let Gamma = xi^(-1)(0) be the zero set of rho in B(0); it is an embedded
invariant C^2 curve, D xi != 0 on it, and each branch of Gamma minus 0 is a single orbit whose backward limit is
0 (Section 9.1, Steps 4 and 6; on the local arc of Step 6, y is strictly monotone along orbits). Suppose that one
branch is unbounded. Being connected and containing points arbitrarily close to 0, it meets the circle {|X| = R}, by
Step 5 at a single point R e_(a_0), and V(R e_(a_0)).e_(a_0) >= l R/2 > 0. Since B(0) is open, q(a) = xi(R e_a) is
defined and C^2 near a_0, and f = q^2 there. The kernel of D xi at a point of Gamma is the tangent line of Gamma,
which is spanned by V(R e_(a_0)) at R e_(a_0), since Gamma is invariant and V(R e_(a_0)) != 0; as V(R e_(a_0)) is not
a multiple of e'_(a_0), q'(a_0) = R D xi(R e_(a_0)) e'_(a_0) != 0. Hence
f(a_0) = f'(a_0) = 0 < f''(a_0) = 2 q'(a_0)^2, and f > 0 near a_0 except at a_0. Differentiating
A(Theta(a)) = L(a)^(-p) f(a) once and twice at a_0 gives A'(Theta(a_0)) Theta'(a_0) = 0 and
A''(Theta(a_0)) Theta'(a_0)^2 = L(a_0)^(-p) f''(a_0), so, with Theta' > 0, A has a zero th_0 = Theta(a_0) with
A'(th_0) = 0 < A''(th_0), and A > 0 on a punctured neighbourhood of th_0. So if a branch of Gamma is unbounded, A has
a zero at which A'' > 0; this is the argument of Section 9.6, Step 8.

### 9.25 Proposition 3.17a (curvature law on the two branches of Gamma in S^+)
Hypotheses: rho in S^+, l > 1, p = 1/l, beta = 2l - 1/2. Used: Theorem B (F4)
(Section 9.0, Step 7: along a branch of Gamma minus 0, d/dt log(h/|V|^2) = 1 - 4l = -2 beta in the flow time t, with
h = 2|grad xi|^2 > 0); Section 9.1 (xi in C^2 with D xi(0) = (1, 0), V in C^{2,alpha}_loc); Theorem 3.1
(V_r = l r + O(r^p) and |W| <= C r^p for large r); Section 9.4, Steps 1-4 and 6
(each component of Gamma minus 0 is one orbit, which escapes and crosses every large circle once and transversally;
S is a C^2 diffeomorphism of R^2 minus 0 with S(X) = X + O(|X|^p), DS = I + O(|X|^{p-1}) for large |X| and
S(Phi_t X) = e^{lt} S(X); xi = Xi o S with Xi(Y) = |Y|^{p/2} B(arg Y), B in C^2, B(th_j) = 0 != B'(th_j)); and
A''(th_j) = 2 B'(th_j)^2 (Section 9.10, Step 2, whose argument uses only A = B^2 with B in C^1).
Step 1 (the branch near 0). Gamma is a C^2 curve tangent to the y-axis at 0 (Theorem B (F3)), so z_j(q) = +-q
e_2 + O(q^2), and since V is C^2 with V(0) = 0 and DV(0) e_2 = beta e_2, v_j(q) = beta q + O(q^2) as q -> 0. Since xi
is C^2 with |grad xi(0)| = 1, h(z_j(q)) = 2 + O(q). The component Gamma_j is an orbit, so V is tangent to it;
V != 0 on Gamma_j and V is outward near 0 (it is close to beta z_j(q)), so the flow moves along Gamma_j in the
direction of increasing q, and since Gamma_j escapes, q runs over (0, inf).
Step 2 (the branch at infinity). For large r = |z| on Gamma_j, V_r = l r + O(r^p) and V_th = O(r^p) by Theorem 3.1,
and Gamma_j crosses each large circle once with V_r > 0, so r is a parameter there with
dq/dr = |V|/V_r = 1 + O(r^{2p-2}). Integrating, q = r + O(r^p)
(the error is bounded for p < 1/2, O(log r) for p = 1/2 and O(r^{2p-1}) for p > 1/2), so v_j(q) = l q + O(q^p) as
q -> inf. Hence the integrand of T_j is O(1) on (0, 1] and O(q^{p-2}) on [1, inf), and T_j converges absolutely.
Step 3 (integration of (F4)). With dq/dt = v_j(q) on Gamma_j, (F4) reads d/dq log(h_j/v_j^2) = -2 beta/v_j,
h_j(q) = h(z_j(q)). The positive function
    E_j(q) = 2 (v_j(q)/(beta q))^2 exp(-2 beta int_0^q (1/v_j(s) - 1/(beta s)) ds)
has the same logarithmic derivative on (0, inf), and E_j(q) and h_j(q) both tend to 2 as q -> 0 (Step 1), so
h_j = E_j. For q >= 1 the integral in E_j equals T_j + (1/l - 1/beta) log q - int_q^inf (1/v_j(s) - 1/(l s)) ds, the
last term is O(q^{p-1}), and -2 beta (1/l - 1/beta) = 2 - (4l - 1) p = p - 2. Since
v_j(q)/(beta q) = (l/beta)(1 + O(q^{p-1})),
    h_j(q) q^{2-p} -> (2 l^2/beta^2) exp(-2 beta T_j)   (q -> inf).
Step 4 (the limit is A''(th_j)). At Y = |Y| e_{th_j}, B(arg Y) = 0, so grad Xi(Y) = |Y|^{p/2-1} B'(th_j) e_{th_j}^perp
and |grad Xi(Y)|^2 = |Y|^{p-2} B'(th_j)^2. For z in Gamma_j, S(z) lies on this ray, and the chain rule gives grad
xi(z) = DS(z)^T grad Xi(S(z)), so
    h(z) = 2 |DS(z)^T e_{th_j}^perp|^2 |S(z)|^{p-2} B'(th_j)^2.
As |z| -> inf on Gamma_j, DS(z) = I + O(|z|^{p-1}), |S(z)|/|z| -> 1 and q/|z| -> 1 (Step 2), so
h_j(q) q^{2-p} -> 2 B'(th_j)^2 = A''(th_j). With Step 3 this proves A''(th_j) = (2 l^2/beta^2) exp(-2 beta T_j), and
the ratio formula follows by division. Only first derivatives of S and Xi are used.
Step 5 (the pointwise form). Fix z in Gamma_j and put L = |S(z)| > 0. Along the forward orbit z(t) = Phi_t z, which
stays in Gamma_j, (F4) says that (h/|V|^2)(z(t)) e^{2 beta t} is constant. By S(z(t)) = e^{lt} S(z) and Step 4,
h(z(t)) = A''(th_j) (L e^{lt})^{p-2} (1 + o(1)); since |z(t)| -> inf,
|V(z(t))| = l |z(t)| (1 + o(1)) = l L e^{lt} (1 + o(1)). Since l (p - 4) = 1 - 4l = -2 beta, the constant equals
A''(th_j) L^{p-4}/l^2, so h(z)/|V(z)|^2 = A''(th_j) L^{p-4}/l^2, which is the second formula.
Step 6 (the limit at 0). Let z = z_j(q) with q -> 0 in Step 5. By Step 1, h(z) -> 2 and |V(z)|/q -> beta, so
|S(z_j(q))|^{4-p}/q^2 -> A''(th_j) beta^2/(2 l^2) > 0. Since 2/(4 - p) = 2l/(4l - 1) = l/beta, the limit k_j of
|S(z_j(q))| q^{-l/beta} exists, is positive, and A''(th_j) = (2 l^2/beta^2) k_j^{4-p}.
Step 7 (S^+_even). If rho is x-even, Gamma is the y-axis (Theorem 3.3), Gamma_1 and Gamma_2 are the two half-axes with
q = |y|, v_j = B_+- and h_j = h_+- in the notation of Proposition 3.17, and Steps 1-4 are Section 9.10, Steps 1 and 2.

### 9.26 Section 4.18 (singular flux, finite parts and the angular conditions)
Hypotheses for Steps 1-5: rho in S^+, l > 1, p = 1/l, alpha = 4l, beta = 2l - 1/2 = (alpha - 1)/2. Used: Section 9.1
(V in C^{2,eta}_loc for every 0 < eta < 1, the complete C^2 flow, xi in C^2 on R^2 with rho = xi^2, D xi(0) = (1, 0)
and D xi != 0; Gamma = {xi = 0}); Section 9.4, Steps 2-6 (S is a homeomorphism of R^2 fixing 0, a C^2 diffeomorphism
of R^2 minus 0, area preserving, S(Phi_t X) = e^{lt} S(X), DS = I + O(|X|^{p-1}) and |S(X)|/|X| -> 1 at infinity;
rho = |S|^p A(arg S), xi = |S|^{p/2} B(arg S), B in C^2 with simple zeros at the two zeros of A); Theorem 3.16(a), (d)
(Section 9.3, Steps 3 and 7); Section 9.11, items 6 and
7 (the polar-coordinate computation of the integrals of rho^q over D_R; transversality of Gamma and the boundary of
D_R).
Step 1 (closedness and pull-back). For a C^1 function g, d(g (V_1 dy - V_2 dx)) = div(g V) dx dy. Off Gamma,
rho > 0 and div(rho^(-2l) V) = rho^(-2l) (div V - 2l V.grad rho/rho) = rho^(-2l) (2l - 2l) = 0, so omega is closed; no
Darcy relation is used. Differentiating S(Phi_t X) = e^{lt} S(X) at t = 0 gives DS V = l S. Since S is area preserving
and a C^2 diffeomorphism of the connected set R^2 minus 0, |det DS| = 1 there, and det DS = 1 because DS -> I at
infinity. Hence omega = S^*(F^(-2l) i_{lY} dY), F(Y) = |Y|^p A(arg Y), where i_{lY}
dY = l (Y_1 dY_2 - Y_2 dY_1) = l |Y|^2 dth; with F^(-2l) = |Y|^(-2) A^(-2l) (2lp = 2), omega = S^*(l A^(-2l) dth). On
a C^1 arc transverse to V in R^2 minus Gamma, S maps it to an arc transverse to the radial field, along which th is
monotone, so the integral of omega over the arc is l int A^(-2l) dth over its scattering angles. Two such arcs joined
by flow lines have the same scattering angles. On the circle |X| = R, omega = R V_r(R e_a) rho(R e_a)^(-2l) da, which
gives (9.24.3)-(9.24.4).
Step 2 (the far-field expansion). By Theorem 3.16(a) and (d), V_r(R e_th) = l R - R^p Psi'(th) + o(R^p) and
rho(R e_th) = R^p (A + R^(p-1) J/(l - 1) + o(R^(p-1))) uniformly in th, J = J_p[A] = (p + 1) Psi A' - p Psi' A. On a
compact set of angles where A >= a_0 > 0 the expansion of the negative power is uniform, and the coefficient of
R^(p-1) in R V_r rho^(-2l) is -Psi' A^(-2l) - 2 l^2 J A^(-2l-1)/(l - 1). With l p = 1, l^2 (p + 1) = l (l + 1) and
2 l^2 p = 2l, this is ((l + 1)/(l - 1)) (Psi' A^(-2l) - 2l Psi A' A^(-2l-1)) = ((l + 1)/(l - 1)) (Psi A^(-2l))'. Near
a zero of A, A is of order t^2 while J may be of order t, so Theorem 3.16(d) gives no uniform relative expansion of
rho/(R^p A) there, and the expansion is not claimed up to the zeros.
Step 3 (area coordinates and the exact renormalisation). Let x = chi(u, y) be the inverse of (x, y) -> (xi(x, y), y)
near 0; chi is C^2 and chi_u > 0. Put v(u, y) = int_0^y chi_u(u, z) dz. Then v_y = chi_u > 0, dx dy = chi_u du dy = du
dv, and (u, y) -> (u, v) is a C^1 diffeomorphism near 0 with derivative I at 0; restrict to a rectangle in (u, v). In
these coordinates V^u = V.grad xi = xi/2 = u/2, and since the coordinates preserve area, div V = 2l becomes
d_u V^u + d_v V^v = 2l in distributions
(change of variables in the weak divergence identity, valid for a C^1 area-preserving map), so d_v V^v = beta and
V^v = beta v + f(u) with f continuous.
(On y = 0, f(u) = chi_u(u, 0) V_2(chi(u, 0), 0) = (1/2) d_x^2 V_2(0) u^2 + o(u^2), since V(0) = 0 and D xi(0) = (1,
0).) On u != 0, rho^(-2l) = |u|^(-alpha) and
    omega = |u|^(-alpha) ((u/2) dv - (beta v + f(u)) du) = dP,
    P(u, v) = (1/2) u |u|^(-alpha) v - int_{u_*}^u f(s) |s|^(-alpha) ds,
on each half-rectangle
(u_* fixed in it; d/du ((1/2) u |u|^(-alpha)) = -beta |u|^(-alpha) since (1 - alpha)/2 = -beta). Let C be a circle
around 0 inside the rectangle on which X.V > 0. Since xi = x + O(|X|^2) and D xi -> (1, 0), xi restricted to C has
exactly two zeros, both simple, and for small delta > 0 each of the two arcs of C on which rho > 0 contains exactly
two points with |xi| = delta, near its two ends. On the arc where xi > 0, positively oriented from the lower cut point
to the upper one, both cut points have u = delta and the integral term of P cancels, so the integral of omega over the
arc between them is (1/2) delta^(1 - alpha) D(delta), D(delta) = v_+ - v_- > 0 the difference of their v coordinates;
on the arc where xi < 0 the orientation and the sign of u both reverse and the same formula holds. With Step 1 this is
the identity of 4.18(b). It is exact for each delta, so the subtracted quantity is 0 before any limit is taken.
Step 4 (the endpoint coordinate). Let alpha > 4, c real, and h_c(s) = s + c s^alpha on [0, s_0], with s_0 so small
that h_c' > 0; h_c is C^4 at 0 (alpha > 4), every derivative of s^alpha of order less than alpha vanishes at 0, and a
cutoff extends h_c to a coordinate change of [0, b] that fixes b. Then int_delta^b t^(-alpha)
dt = delta^(1-alpha)/(alpha - 1) - b^(1-alpha)/(alpha - 1), while the same integral from h_c(delta) to b has
h_c(delta)^(1-alpha)/(alpha - 1) = delta^(1-alpha)/(alpha - 1) - c + o(1) in place of the first term; so the finite
parts in the coordinates t and s differ by -c. In the coordinate s the density is
h_c(s)^(-alpha) h_c'(s) = s^(-alpha) + O(s^(alpha-2)): the same leading term, no term of order s^(-1), and an
integrable remainder. So derivatives of the endpoint coordinate of order less than alpha do not determine the finite
part; in S^+ the endpoint germs of A are controlled only to second order (A in C^{2,alpha'}, Theorem 3.1) and the
scattering endpoint maps only to second order (S in C^2).
Step 5 (the conditional finite part). Assume that xi is C^infinity and S is a C^infinity diffeomorphism of R^2 minus
0. Then B(th) = xi(S^(-1)(e_th)) is C^infinity, its two zeros are simple, and near either end of a component I of
{A > 0}, in the distance t to the end, A = t^2 a(t) with a smooth and positive. Let sigma be the sign of B on I,
D_R = S^(-1)(B_R) and M_I(q) = int_I A^q dth, holomorphic for Re q > -1/2. Since S is smooth off 0, the boundary of
D_R is a smooth closed curve, and Gamma crosses it transversally at two points
(S maps Gamma to the two zero rays of B, which cross the circle |Y| = R transversally). Hence the coarea density
d(u) = int_{{sigma xi = u} cap D_R} |grad xi|^(-1) ds is C^infinity for u near
0 (finitely many charts (xi, w) along the compact arc of Gamma in the closure of D_R, with the boundary of D_R a
smooth graph w = b(xi) at the two crossings; differentiate under the integrals, including the endpoint terms). The
one-arc form of the computation of Section 9.11, item 6 gives, for Re q > -1/2,
    Z(q) := int_{D_R cap {sigma xi > 0}} rho^q dX = R^(2 + pq) M_I(q)/(2 + pq).
Split Z at u = u_0 > 0 small: the part with sigma xi >= u_0 is entire
(rho is bounded above and below by positive constants there), and int_0^{u_0} u^(2q) d(u) du continues
meromorphically, by Taylor expansion of d to any order, with at most simple poles at q = -(j + 1)/2, j = 0, 1, 2, ...,
with residue d_j/2 (d_j the coefficient of u^j). Likewise int_I t^(2q) a(t)^q dth continues M_I meromorphically
(the Taylor coefficients of a(t)^q are holomorphic in q), with at most simple poles at the same points. At q_0 = -2l,
2 + pq = p (q - q_0). If M_I had a pole at q_0, the right side would have a pole of order at least 2 there, which the
left side has not; so M_I is holomorphic at q_0, and comparing the coefficients of 1/(q - q_0) gives
M_I(q_0)/p = Res_{q_0} Z. If alpha = 4l is not an integer, q_0 is not of the form -(j + 1)/2, so M_I(q_0) = 0; if
alpha is an integer, M_I(q_0) = (p/2) d_{alpha - 1}. For noninteger alpha no exponent 2 q_0 + k (k = 0, 1, 2, ...) in
the endpoint expansion equals -1, so the continued value M_I(q_0) is the ordinary Hadamard finite part
(the integral after subtraction of the finitely many divergent powers of t). This proves 4.18(c). The identity of
4.16(b) is not used at q = -2l itself, where the integral diverges; the continuation uses the extra smoothness.
Step 6 (the second moment family). Let rho, W, p and l be as in 4.18(d) and E = (l X + W).grad rho - rho, which is
continuous, O(r^2) at 0 and O(r^p) at infinity (2p - 1 < p). For f = r^(-m) Phi, integration by parts on
eps < r < R gives int E f dX = -(1 + 2l - ml) int rho f dX - int rho W.grad f dX in the limit, since l X.grad f = -ml
f and div W = 0; the boundary terms are O(eps^(4-m)) and O(R^(2+p-m)), as in Section 9.8, Step 3. So the hypothesis
says int E r^(-m) Phi dX = 0 for every m in (2 + p, 4) and every smooth Phi. Fix Phi, put
e(r) = int_0^{2 pi} E(r e_th) Phi(th) dth and M(z) = int_0^inf e(r) r^(1-z) dr. By the bounds on E, M is holomorphic
in the strip 2 + p < Re z < 4 (dominated differentiation on compact substrips), and it vanishes on the real interval
(2 + p, 4), hence on the strip. For fixed m_0 in (2 + p, 4), g(t) = e(e^t) e^((2 - m_0) t) is in L^1(R) with Fourier
transform M(m_0 + i tau) = 0, so g = 0 (convolution with Gaussians, an approximate identity in L^1, gives 0) and
e = 0 by continuity. Since Phi is arbitrary
(trigonometric polynomials are dense in the continuous functions on the circle), E = 0 on R^2 minus 0, and E(0) = 0 by
continuity. The converse is the same integration by parts. For the last assertion of 4.18(d) let rho be C^3 with the
jet and the growth bounds of S with exponent gamma in [0, 1), and W = W[rho]. Section 9.0, Steps 1-2, which do not
assume transport, give W in C^2_loc, W(0) = 0, div W = 0 and W = O(r^gamma (1 + log r)) = o(r) at infinity ((9.0.1));
so E = O(r^2) at 0 and E = O(r^gamma) at infinity, and the bounds O(r^p) of 4.18(d) are not available before transport
is proved (for p < gamma < 1, x^2 (1 + r^2)^((gamma - 2)/2) satisfies the jet and the growth bounds of S but is not
O(r^p)). For m in (2 + max(p, gamma), 4), a nonempty subinterval of (2 + p, 4), both moment integrals converge
absolutely and the boundary terms are O(eps^(4-m)) and O(R^(2 + gamma - m)); so the family on this subinterval gives
M = 0 there, M is holomorphic on 2 + gamma < Re z < 4, and the argument above gives E = 0 on R^2, which is the profile
equation. Conversely, for a profile in S, Theorem 3.1 gives the bounds of 4.18(d) and Proposition 3.4 the whole family
on (2 + p, 4).
Step 7 (the angular datum A_l). Let l > 1 with alpha = 4l not an integer and
Q(th) = cos^2 th + (alpha - 1) sin^2 th >= 1. A_l = cos^2 th Q^(-1/(2l)) is smooth, nonnegative, invariant under
th -> pi - th, and vanishes exactly at pi/2 and 3pi/2; at th = +-pi/2 + t, cos^2 th = sin^2 t and
Q = alpha - 1 + O(t^2), so A_l = (alpha - 1)^(-1/(2l)) t^2 + O(t^4). On (-pi/2, pi/2),
    (sin th (cos th)^(1 - alpha))' = (cos th)^(2 - alpha) + (alpha - 1) sin^2 th (cos th)^(-alpha)
                                   = (cos th)^(-alpha) Q = A_l^(-2l).
Near th = pi/2 - t the primitive is (cos t)(sin t)^(1 - alpha), which is t^(1 - alpha) times an even analytic function
of t; its exponents 1 - alpha + 2k are never 0 for noninteger alpha, so after removal of the divergent terms it has no
constant term, and the same holds at -pi/2. So the Hadamard finite part on (-pi/2, pi/2) is 0; on (pi/2, 3pi/2) use
the primitive -sin th |cos th|^(1 - alpha). Theorem 3.16(b) applies to any A with a positive quadratic zero
(only the existence of A'' at the zero is used), so J_p[A_l] is not identically zero on either side of either zero.
For E_A: if int (Psi')^2 = 0, Psi is a constant C, and the angular equation gives (p + 1)^2 C = sin th A_l' - p cos th
A_l for all th; at a zero the right side vanishes, so C = 0, but at th = pi/2 + t the right side is 2
(alpha - 1)^(-1/(2l)) t + O(t^2), not identically 0. Hence E_A > 0 (the argument of Section 9.11, item 3). For the
family: fix a compact interval K in (-pi/2, pi/2) with nonempty interior and phi in C_c^infinity of the interior of K
with sup |phi'| < (1/2) min_K A_l^(-2l); put A = (A_l^(-2l) + phi')^(-1/(2l)) on (-pi/2, pi/2), A(pi - th) = A(th), so
that A = A_l near both zeros, A is smooth and positive off the zeros, and the finite part on each arc changes by
int phi' = 0. The zeros and their germs are unchanged, so the arguments above apply. Nonzero phi_n with mutually
disjoint supports in the interior of K, each scaled to satisfy the bound, give functions A_n for which the A_n - A_l
are nonzero with mutually disjoint supports, also after the reflection; so they are linearly independent (the set of
perturbed functions is not a linear space; its differences from A_l span an infinite-dimensional space). For these
functions only angular conclusions are asserted: the conclusions of Theorem 3.2 and Proposition 3.18(b) on the zero
set (exactly two zeros, both quadratic, with A > 0 between them on both arcs) and J_p[A] not identically zero
(Proposition 3.18(c)). This gives only angular functions; no rho or W on R^2 is constructed.

### 9.27 Proposition 2.7 (growth 1 < gamma < 2 without W_2 = o(r): the limits at infinity)
Hypotheses and notation: 1 < gamma < 2, E_gamma(C) and W_2[g] as in Proposition 2.7; K, the bounds
|D^j K(Z)| <= C_j |Z|^(-2-j), the circular cancellation and the Taylor bound
|K(X - Y) - K(-Y) - DK(-Y)X| <= C|X|^2 |Y|^(-4) for |Y| > 2|X| are those of Section 9.14, Steps 1 and 3. Used:
Section 9.0, Step 1, for the smoothness of distributionally harmonic functions; Section 9.14, Steps 2-6, for the
compact Biot-Savart field and the compact twice-subtracted field, the definition and growth of W_2, the explicit
matrix DK(-Y), the harmonic growth lemma and the velocity law V = AX + W_2 of a profile, A = diag(1/2, beta),
beta = 2l - 1/2. No hypothesis W_2 = o(r) and no result of Sections 9.20-9.23 is used.
Step 1 (the inverse on E_gamma(C); proof of (a)). In this Step c denotes constants depending only on gamma. Let g be
in E_gamma(C). Then g(0) = 0, and on every disk B(0, L) the function g is Lipschitz with constant C L^(gamma - 1): a
locally Lipschitz function is Lipschitz on a convex set with constant the essential supremum of |grad g| there, and
|X|^(gamma - 1) <= L^(gamma - 1) on B(0, L) because gamma > 1. Fix X != 0 and split the plane into |Y| > H with
H > 2|X| and the bounded region |Y| < H. On |Y| > H the three kernel terms are combined, and by the Taylor bound the
integral there is at most c C|X|^2 int_H^inf s^(gamma - 3) ds = c C|X|^2 H^(gamma - 2), finite because gamma < 2. On
|Y| < H the two subtraction terms are absolutely integrable: |K(-Y) g(Y)| <= c C|Y|^(gamma - 2) and
|DK(-Y)X g(Y)| <= c C|X| |Y|^(gamma - 3), whose integrals over |Y| < eps are at most c C eps^gamma and
c C|X| eps^(gamma - 1) (this uses gamma > 1), and K(X - Y) g(Y) is bounded near Y = 0. Near Y = X, on a disk
B(X, delta), write g(Y) = g(X) + (g(Y) - g(X)): the constant term has circular principal value 0 by the circular
cancellation of K, and |K(X - Y)(g(Y) - g(X))| <= c C_L |X - Y|^(-1) with C_L = C(|X| + delta)^(gamma - 1), so this
part converges absolutely and is at most c C_L delta. At X = 0 the combined kernel K(-Y) - K(-Y) - 0 vanishes and
g(0) = 0, so W_2[g](0) = 0. Thus the integral converges at every X.
For |X| <= L, H > 2L, eps > 0 and delta > 0 the three removed parts, namely the tail |Y| > H of the combined
integrand, the disk |Y| < eps for the two subtracted terms and the disk B(X, delta) for the translated term, are
bounded, uniformly for g in E_gamma(C) and |X| <= L, by c C L^2 H^(gamma - 2), c C(eps^gamma + L eps^(gamma - 1)) and
c C(L + delta)^(gamma - 1) delta. What remains is an integral of bounded kernels over a bounded region, continuous in
X (continuity of translation in L^1 for the translated term) and, if g_n -> g uniformly on B(0, H), converging to the
corresponding integral for g uniformly in |X| <= L; the local term g(X) e_2/2 is continuous and converges uniformly on
compact sets. Letting n -> infinity first and then H -> infinity, eps -> 0 and delta -> 0 proves the continuity of
W_2[g] and the convergence W_2[g_n] -> W_2[g] locally uniformly.
Scaling. Put D_t g(X) = t^(-gamma) g(tX). Then |D_t g(X)| <= C|X|^gamma and |grad D_t g(X)| = t^(1 - gamma)
|grad g(tX)| <= C|X|^(gamma - 1) almost everywhere, so E_gamma(C) is invariant under D_t. In the integral for
W_2[D_t g](X) substitute Y = Z/t. By the homogeneity of K of degree -2 and of DK of degree -3,
K(X - Z/t) = t^2 K(tX - Z), K(-Z/t) = t^2 K(-Z) and DK(-Z/t)X = t^2 DK(-Z)(tX); the area element gives t^(-2), the
density t^(-gamma), and a circular disk about X goes to a circular disk about tX, so principal values correspond. With
the local term this gives W_2[D_t g](X) = t^(-gamma) W_2[g](tX).
Growth. For |X| = 1 take H = 2, eps = 1/2 and delta = 1/2 in the splitting above: every part, and the local term
|g(X)|/2 <= C/2, is at most a constant depending only on gamma times C, so |W_2[g](X)| <= C_gamma C for every g in
E_gamma(C) and |X| = 1. For X != 0 apply this to D_t g with t = |X|:
|W_2[g](X)| = t^gamma |W_2[D_t g](X/t)| <= C_gamma C |X|^gamma. Since gamma > 1, W_2[g] is differentiable at 0 with
derivative 0.
Divergence and curl. Let chi be the cutoff of Section 9.14, Step 2, and g_H = chi(./H) g, a Lipschitz function with
compact support, and put U_H = p.v. int K(. - Y) g_H(Y) dY - g_H e_2/2. For a smooth compactly supported density this
field has divergence 0 and curl minus the x-derivative of the density (Section 9.14, Step 2). Mollifications of g_H
converge to g_H uniformly, with supports in a fixed disk and a common Lipschitz constant, and the estimates above
(cancellation on B(X, delta), bounded kernels elsewhere) give locally uniform convergence of the corresponding fields
to U_H; so div U_H = 0 and curl U_H = -d_x g_H in distributions. The constant c_H = int K(-Y) g_H(Y) dY and the matrix
B_H = int DK(-Y) g_H(Y) dY are finite by the bounds near 0 above, and W_2[g_H] = U_H - c_H - B_H X. The matrices
DK(-Y), given explicitly in Section 9.14, Step 4, are symmetric and traceless, so B_H X has zero divergence and curl.
Hence W_2[g_H] has divergence 0 and curl -d_x g_H. For |X| <= L and H > 2L + 2, W_2[g] - W_2[g_H] is the integral of
the combined kernel against (1 - chi(Y/H)) g(Y) over |Y| >= H, which is at most c C L^2 H^(gamma - 2) by the Taylor
bound, while d_x g_H -> d_x g in distributions. So div W_2[g] = 0 and curl W_2[g] = -d_x g in distributions.
Uniqueness. If w is continuous with this divergence and curl, w = O(|X|^gamma), w(0) = 0 and w differentiable at
0 with derivative 0, then h = w - W_2[g] is continuous with zero divergence and curl in distributions. By the
identities Lap h^(1) = d_x div h - d_y curl h and Lap h^(2) = d_y div h + d_x curl h of Section 9.14, Step 5, which
hold between distributional derivatives for every continuous field, its components are distributionally harmonic,
hence smooth harmonic functions (Section 9.0, Step 1), and they are O(|X|^gamma) = o(|X|^2). The harmonic growth lemma
of Section 9.14, Step 5, with m = 2 makes h affine, and h(0) = 0 and Dh(0) = 0 give h = 0. This proves (a).
Step 2 (compactness and the stationary equation; proof of (b)). Let rho be C^3 with the jet and the bounds of S with
exponent gamma. For |X| <= 1, Taylor's formula and the jet give |rho(X)| <= C|X|^2 <= C|X|^gamma and
|grad rho(X)| <= C|X| <= C|X|^(gamma - 1); for |X| >= 1, (1 + |X|)^gamma <= 2^gamma |X|^gamma
and (1 + |X|)^(gamma - 1) <= 2 |X|^(gamma - 1). So rho is in E_gamma(C_0), and for g = rho the formula of
Proposition 2.7 is the definition of W_2 in Section 9.14, Step 3. By the invariance in Step 1, f_R = D_R rho is in
E_gamma(C_0) for every R >= 1. On B(0, L) the f_R are bounded by C_0 L^gamma and Lipschitz with constant
C_0 L^(gamma - 1); by the Arzela-Ascoli theorem on the disks B(0, n) and a diagonal sequence, every sequence f_(R_n)
has a subsequence converging locally uniformly. If R_n stays bounded, a subsequence has R_n -> R_* >= 1 and
f_(R_n) -> f_(R_*) locally uniformly by the uniform continuity of rho on compact sets. So the family is precompact.
Let f be a limit along R_n -> infinity. Then |f(X)| <= C_0 |X|^gamma. For X != 0 and 0 < eta < |X|, every f_(R_n) is
Lipschitz on B(X, eta) with constant C_0 (|X| + eta)^(gamma - 1), hence so is f; so f is locally Lipschitz, and at
each point X of differentiability of f, which is almost every point by Rademacher's theorem,
|grad f(X)| <= C_0 (|X| + eta)^(gamma - 1) for every small eta, hence |grad f(X)| <= C_0 |X|^(gamma - 1). So f is in
E_gamma(C_0). By the scaling in Step 1, W_2[f_R](Z) = R^(-gamma) W_2(RZ), and by the convergence in Step 1,
W_2[f_(R_n)] -> W_2[f] locally uniformly.
Now let rho be a profile with V = AX + W_2 (Section 9.14, Step 6). Since W_2 is C^1 (Section 9.14, Step 3),
div V = 1/2 + beta = 2l, and V.grad rho = rho gives div(rho V) = (1 + 2l) rho. At X = RZ, rho(RZ) = R^gamma f_R(Z),
W_2(RZ) = R^gamma W_2[f_R](Z) and A(RZ) = R AZ, and the divergence in X is R^(-1) times the divergence in Z. Dividing
by R^(2 gamma - 1) gives
    div(f_R W_2[f_R]) + R^(1 - gamma) [div(f_R AZ) - (1 + 2l) f_R] = 0
in the variable Z. Integrate against a test function phi. The bracket contributes R^(1 - gamma) times an integral of
f_R against AZ.grad phi and phi, which is bounded uniformly in R because the f_R are uniformly bounded on the support
of phi, and R^(1 - gamma) -> 0 because gamma > 1. Along R_n, the integral of f_(R_n) W_2[f_(R_n)].grad phi converges
to that of f W_2[f].grad phi by uniform convergence on the support. Hence div(f W_2[f]) = 0 in distributions. For the
equivalent form put w = W_2[f], continuous with div w = 0 in distributions, and let f_eps be mollifications of f. For
a test function phi, -int f_eps w.grad phi = -int w.grad(f_eps phi) + int phi w.grad f_eps = int phi w.grad f_eps. As
eps -> 0, f_eps -> f locally uniformly and grad f_eps -> grad f almost everywhere, boundedly on compact sets, so
div(f w) = w.grad f, a locally bounded function. Thus div(f w) = 0 if and only if w.grad f = 0 almost everywhere. Only
the jet near 0, the two class bounds, the velocity law and transport were used.
Step 3 (layered limits; proof of (c)). If f in E_gamma(C) is a function of y alone, then d_x f = 0, so the zero field
has the divergence, curl, growth and normalization of Step 1, and the uniqueness there gives W_2[f] = 0. Suppose that
every limit at infinity of rho is a function of y alone but W_2 is not o(|X|^gamma). Then there are eps > 0 and X_n
with R_n = |X_n| -> infinity and |W_2(X_n)| >= eps R_n^gamma. Pass to a subsequence with f_(R_n) -> f and
X_n/R_n -> Z_0, |Z_0| = 1. By Step 2, R_n^(-gamma) W_2(X_n) = W_2[f_(R_n)](X_n/R_n) -> W_2[f](Z_0) = 0, a
contradiction. Conversely, if W_2 = o(|X|^gamma), then for |Z| <= L, R^(-gamma) |W_2(RZ)| is at most eps L^gamma where
|RZ| >= R_eps and at most R^(-gamma) times the maximum of |W_2| on B(0, R_eps) elsewhere, so
R^(-gamma) W_2(R.) -> 0 locally uniformly and, by Step 2, W_2[f] = 0 for every limit at infinity f. Then
d_x f = -curl W_2[f] = 0 in distributions; the mollifications f_eps satisfy d_x f_eps = 0, so they are functions of
y alone, and so is their locally uniform limit f. No profile equation was used.
Step 4 (stationary solutions that are not layered; proof of (d)). Let e = (e_1, e_2) be a unit vector, s = e.X, F as
in (d) and H(s) = (a_+ s_+^(gamma + 1) - a_- (-s)_+^(gamma + 1))/(gamma + 1), so that H' = F, F is C^1 (gamma > 1) and
H is C^2. The function f = F(e.X) is C^1 with |f(X)| <= C|X|^gamma and |grad f(X)| = |F'(e.X)| <= C|X|^(gamma - 1), so
f is in E_gamma(C) for some C. Put psi = -e_1 H(e.X), which is C^2, and
w = grad-perp psi = (-psi_y, psi_x) = e_1 F(e.X) (e_2, -e_1). Then div w = 0,
curl w = Lap psi = -e_1 F'(e.X) = -d_x f, |w(X)| <= C|X|^gamma, and w(0) = 0 with derivative 0 at 0 because gamma > 1;
by the uniqueness in Step 1, w = W_2[f]. Since grad f = F'(e.X) e and w is a multiple of (e_2, -e_1), w.grad f = 0.
For e = (1, 0) and a_+ = a_- = 1 this is f = |x|^gamma with W_2[f] = (0, -|x|^gamma).
For the parabolic solutions let sigma = 1 or -1, s = r + sigma x and k = gamma + 1. On r > 0, s is smooth and
0 <= s <= 2r, and
    grad s = X/r + sigma e_1,   |grad s|^2 = 2s/r,   Lap s = 1/r,   d_x s = sigma s/r,
the last because x/r + sigma = sigma(r + sigma x)/r. Hence Lap(s^k) = k(k - 1) s^(k - 2) |grad s|^2 + k s^(k - 1)
Lap s = k(2k - 1) s^(k - 1)/r. Let f = a s^gamma and psi = c_0 s^k with c_0 = -sigma a
gamma/((gamma + 1)(2 gamma + 1)). On r > 0, f is C^1
(gamma > 1; s^gamma is C^1 also where s = 0, on the ray {y = 0, sigma x < 0}), psi is C^2 (gamma - 1 > 0), and
    -Lap psi = -c_0 (gamma + 1)(2 gamma + 1) s^gamma/r = sigma a gamma s^gamma/r
             = a gamma s^(gamma - 1) d_x s = d_x f.
Since |grad s| <= 2, |f| <= |a| 2^gamma r^gamma, |grad f| <= 2^gamma |a| gamma r^(gamma - 1) and
|grad psi| <= C r^gamma; so f is C^1 on the plane and in E_gamma(C), and w = grad-perp psi is continuous, O(r^gamma),
and vanishes at 0 with derivative 0. In distributions on the whole plane, -Lap psi = d_x f: integrating by parts on
r > eps against a test function, the boundary terms are O(eps^(k + 1)) and O(eps^(gamma + 1)) and vanish as eps -> 0.
So div w = 0 and curl w = -d_x f, and w = W_2[f] by Step 1. Both grad f and grad psi are multiples of grad s, so
w.grad f = 0. For c > 0, r + sigma x = c holds if and only if r = c - sigma x, that is, y^2 = c^2 - 2 sigma c x with
c - sigma x >= 0; on that parabola c^2 - 2 sigma c x = y^2 >= 0 gives sigma x <= c/2 < c, so the level set is the
whole parabola. For a != 0 the level sets are not lines, so f is not a function of y alone. These are solutions of the
stationary equation; no profile with such a limit at infinity is constructed.
Step 5 (the density of (e)). Let 1 < q < gamma. Let eta be a smooth radial function with 0 <= eta <= 1, eta = 0 for
r <= 1 and eta = 1 for r >= 2, and put h_q = (1 - eta(r)) x^2 + eta(r) r^q, the density rho_* of Section 9.14, Step 4,
with exponent q. It is smooth, nonnegative, even in x and in y, equal to x^2 on r <= 1 and to r^q on r >= 2; it
satisfies the bounds of S and the Hessian bound with exponent q, hence (q < gamma) the bounds of S with exponent gamma
and |D^2 h_q(X)| <= C(1 + |X|)^(gamma - 2). By Step 2 with exponent q, h_q is in E_q(C_1), and, by Step 2 with
exponent gamma, in E_gamma(C_1).
Let g = r^q, which is in E_q(C) for some C. The function psi_g = -x r^q/(q + 2) has
Lap(x r^q) = x Lap(r^q) + 2 d_x(r^q) = q(q + 2) x r^(q - 2) on r > 0, so -Lap psi_g = q x r^(q - 2) = d_x g there,
and, as in Step 4, in distributions on the plane (boundary terms O(eps^(q + 2)) and O(eps^(q + 1))). Its velocity
    w_g = grad-perp psi_g = (q x y r^(q - 2), -r^q - q x^2 r^(q - 2))/(q + 2)
is continuous and O(r^q), and vanishes at 0 with derivative 0 because q > 1; by Step 1 with exponent q, w_g = W_2[g].
The q-rescalings R^(-q) h_q(RZ) are in E_q(C_1), equal g(Z) for |Z| >= 2/R and are at most C R^(-q) for |Z| <= 2/R, so
they converge to g locally uniformly. By Step 1 with exponent q (scaling and convergence),
R^(-q) W_2[h_q](RZ) -> w_g(Z) locally uniformly, and at Z = (0, -1), W_2[h_q](0, -r) = -(0, r^q)/(q + 2) + o(r^q); by
the growth in Step 1, |W_2[h_q](X)| <= C|X|^q.
Let eta_1 be a smooth even function on the line with 0 <= eta_1 <= 1, eta_1 = 0 for |y| <= 1 and eta_1 = 1 for
|y| >= 2, put F(y) = eta_1(y) |y|^gamma and rho = h_q + F. Then rho is smooth, nonnegative, even in x, equal to x^2
near 0 (so it has the jet), and satisfies the bounds of S with exponent gamma. F is in E_gamma(C) and is a function of
y alone, so W_2[F] = 0 by Step 3, and by linearity of the defining integral W_2[rho] = W_2[h_q]. Hence
|W_2(X)| <= C|X|^q, W_2(0, -r) = -(0, r^q)/(q + 2) + o(r^q), W_2 = o(r^gamma), and W_2 is not o(r) because q > 1. The
limits at infinity: R^(-gamma) h_q(RZ) -> 0 locally uniformly because q < gamma, and
R^(-gamma) F(RZ) = eta_1(Ry) |y|^gamma differs from |y|^gamma by at most (2/R)^gamma, so f_R -> |y|^gamma locally
uniformly along every sequence: |y|^gamma is the only limit at infinity.
Since rho is even in x, the field (-W_2^(1)(-x, y), W_2^(2)(-x, y)) is continuous and has the divergence, curl, growth
and normalization of Step 1 for rho (under (x, y) -> (-x, y) the curl changes sign, and so does d_x rho), so it equals
W_2 by the uniqueness in Step 1; in particular W_2^(1)(0, y) = 0. For V = AX + W_2 with A = diag(1/2, beta) and any
real beta, the first component of V vanishes on the y-axis, which is therefore invariant. On it write the orbit as
(0, -r(s)); then
    r'(s) = beta r(s) + r(s)^q/(q + 2) + o(r(s)^q)   (r -> infinity).
Since q > 1 there is r_1 such that the right side is at least r^q/(2(q + 2)) for r >= r_1. For a start with
r(0) >= r_1, r increases and (r^(1 - q))' = (1 - q) r^(-q) r' <= -(q - 1)/(2(q + 2)), so r^(1 - q) reaches 0 before
s = 2(q + 2) r(0)^(1 - q)/(q - 1). Since V is C^1, the maximal solution leaves every compact set, so the orbit escapes
to infinity in finite time T. If rho were a profile with this V, transport along the orbit would give
rho(X(s)) = e^s rho(X(0)), bounded for 0 <= s < T, while rho(0, -r) = r^q + r^gamma for r >= 2 tends to infinity along
the orbit. So rho is not a profile, for any real l.
Without F, the density h_q has the same velocity, the same invariant axis, the same finite-time escape and the same
argument against the profile equation (h_q(0, -r) = r^q -> infinity), satisfies the Hessian bound with exponent gamma,
and has the single limit at infinity 0 because q < gamma. This proves (e). The examples are densities, not profiles:
the first has a unique nonzero layered limit; the second satisfies the Hessian bound and has only the zero limit. Thus
the class bounds, also together with a unique nonzero layered limit or with the Hessian bound, do not imply
W_2 = o(r). Whether the profile equation together with the class bounds implies W_2 = o(r) is not decided.

### 9.28 Proposition 2.8 (growth 1 < gamma < 2 without W_2 = o(r): homogeneous limits, symmetry and the first order)
Hypotheses and notation: 1 < gamma < 2 and the notation of Proposition 2.8; D_t g = t^(-gamma) g(t.) and f_R = D_R rho
as in Section 9.27, Steps 1 and 2; grad-perp psi = (-psi_y, psi_x), so that curl grad-perp psi = Lap psi;
e_r = (cos th, sin th) and e_th = (-sin th, cos th). Used: Section 9.14, Steps 1-4 and 8, for the kernel K and its
bounds and circular cancellation, the compact Biot-Savart field and its derivative at 0, the definition of W_2, the
explicit matrix DK(-Y), the density f_gamma and the field W_2 = (0, -f(x)) of a density f(x); Section 9.14, Step 6,
for the velocity law; Section 9.27 (Proposition 2.7) and the rescaled profile equation of its Step 2. No hypothesis
W_2 = o(r) and no result of Sections 9.20-9.23 is used.
Step 1 (the set of limits; proof of (a)). Let rho be as in (a). By Section 9.27, Step 2, all f_R, R >= 1, lie in one
class E_gamma(C_0) and form a precompact family for locally uniform convergence. Locally uniform convergence is given
by the metric d(g, h) = sum_(m >= 1) 2^(-m) min(1, max_(|X| <= m) |g(X) - h(X)|), and R -> f_R is continuous for d by
the uniform continuity of rho on compact sets. Let C_N be the closure of {f_R : R >= N}. It is compact by
precompactness, nonempty, and connected as the closure of a continuous image of an interval. The set K of limits at
infinity is the intersection of the C_N: a limit along R_n -> infinity lies in every C_N, and a point g of the
intersection is the limit of some f_(R_N) with R_N >= N and d(f_(R_N), g) < 1/N. A decreasing intersection of nonempty
compact sets is nonempty. It is connected: if K = K_1 union K_2 with K_1, K_2 disjoint, closed and nonempty, choose
disjoint open sets O_1, O_2 containing K_1, K_2; if every C_N contained a point outside O_1 union O_2, these points
would have a limit point in every C_N, hence in K, outside the open set O_1 union O_2, which is impossible; so some
C_N lies in O_1 union O_2 and meets both, contradicting its connectedness. Since D_t f_R = f_(tR) and D_t is
continuous for d, D_t maps the limit along R_n to the limit along t R_n, so D_t K is contained in K for every t > 0,
and with 1/t in place of t, D_t K = K. If K = {f}, then f_R -> f as R -> infinity, since otherwise some sequence
f_(R_n) with R_n -> infinity would stay at distance at least some eps > 0 from f and a subsequence would converge to a
second limit; and D_t f = f for every t > 0, that is f(tX) = t^gamma f(X).
Step 2 (the stream function of a homogeneous element; first part of (b)). If g in E_gamma(C) is homogeneous, then
P(th) = g(cos th, sin th) is Lipschitz, because g is Lipschitz on a neighborhood of the unit circle by Section 9.27,
Step 1, and g = r^gamma P. Conversely, if P is Lipschitz and 2 pi-periodic, then f = r^gamma P is continuous with
f(0) = 0 and locally Lipschitz on r > 0 with grad f = r^(gamma - 1)(gamma P e_r + P' e_th) almost everywhere, so
|f| <= C r^gamma and |grad f| <= C r^(gamma - 1) almost everywhere; since gamma > 1, f is Lipschitz on every disk
about 0, and f is in E_gamma(C) for some C. Let w = W_2[f]. Since D_t f = f, the scaling in Proposition 2.7(a) gives
w(tX) = t^gamma w(X), so w = r^gamma (w_r(th) e_r + w_th(th) e_th) with continuous w_r and w_th. In polar coordinates
div w = r^(gamma - 1)(k w_r + w_th') in distributions on r > 0, so k w_r + w_th' = 0 in distributions on the circle.
Hence Q := w_th/k has the continuous derivative Q' = -w_r, Q is C^1, and since
grad-perp(r^k Q) = r^gamma(k Q e_th - Q' e_r), w = grad-perp(r^k Q). Now
curl w = Lap(r^k Q) = r^(gamma - 1)(Q'' + k^2 Q) and d_x f = r^(gamma - 1)(gamma cos th P - sin th P') in
distributions on r > 0, so curl w = -d_x f gives
    Q'' + k^2 Q = -gamma cos th P + sin th P'
in distributions on the circle. The right side is bounded, so Q is in W^(2,inf). Since 2 < k < 3, k is not an integer
and Q'' + k^2 Q = 0 has no nonzero 2 pi-periodic solution, so Q is the unique periodic solution. By the equivalence in
Proposition 2.7(b), whose proof in Section 9.27, Step 2, applies to every f in E_gamma(C) and its continuous
divergence-free field W_2[f], f is stationary if and only if w.grad f = 0 almost everywhere, and almost everywhere
    w.grad f = r^(2 gamma - 1)(k Q P' - gamma Q' P).
On a component I of {P != 0} (an open arc), |P| is bounded below on each compact subarc, where |P|^(-k/gamma) is
therefore Lipschitz, and Q |P|^(-k/gamma) is absolutely continuous with derivative
|P|^(-k/gamma)(gamma Q' P - k Q P')/(gamma P) almost everywhere. So k Q P' = gamma Q' P almost everywhere on I if and
only if Q = c_I |P|^(k/gamma) on I for a constant c_I. On the closed set {P = 0}, P' = 0 almost everywhere
(a Lipschitz function has derivative 0 almost everywhere on its zero set), so k Q P' - gamma Q' P = 0 almost
everywhere there in any case. This proves the first part of (b).
Step 3 (an angular zero). Let f = r^gamma P != 0 be homogeneous and stationary, and suppose that P has no zero. Then
P has a constant sign eps, and Q = c|P|^(k/gamma) on the whole circle. If c = 0, then Q = 0, so d_x f = 0 in
distributions (Step 2), f is a function of y alone, and f(1, 0) = f(0, 0) = 0, contradicting P(0) != 0. If c != 0,
then Q has no zero and |P| = |Q/c|^(gamma/k) is C^1 with Lipschitz derivative; then the right side of the equation for
Q is Lipschitz, Q is in W^(3,inf), and by induction P and Q are smooth. Then f and w are smooth on r > 0, their first
derivatives are O(r^(gamma - 1)), and both are C^1 on the plane with value and derivative 0 at 0. Put
m = |P|^(-1/gamma) and X(th) = m(th) e_r. The curve Gamma = {|f| = 1} = {X(th)} is a smooth closed curve bounding a
region D that contains 0. From k Q P' = gamma Q' P and m'/m = -P'/(gamma P) one gets -Q' = k Q m'/m, so
    w(X(th)) = m^gamma (-Q' e_r + k Q e_th) = k m^(gamma - 1) Q (m' e_r + m e_th) = k m^(gamma - 1) Q X'(th).
The circulation of w around Gamma is therefore int_0^(2 pi) k m^(gamma - 1) Q |X'(th)|^2 dth, which is not 0 because
Q has a constant sign. By Green's formula and curl w = -d_x f it equals -int_D d_x f dX = -int_Gamma f n_x ds = -eps
int_Gamma n_x ds = 0, where n is the outer normal and f = eps on Gamma. This contradiction shows that P has a zero.
Step 4 (the components of {P != 0}). Let f be as in Step 3, so P has a zero, and let I = (a, b) be a component of
{P != 0}, written on a lift of the circle, with 0 < b - a <= 2 pi, where b - a = 2 pi exactly when P vanishes at only
one point.
(i) Suppose c_I = 0. Then Q = 0 on I, so the equation for Q gives sin th P' = gamma cos th P almost everywhere on I.
On every subinterval J of I on which sin th != 0, (P |sin th|^(-gamma))' = 0 almost everywhere, so
P = d |sin th|^gamma on J with d != 0. Hence I contains no zero th_0 of sin th, since otherwise
P(th_0) = lim d|sin th|^gamma = 0 while P(th_0) != 0; so J = I and P = d |sin th|^gamma on I; since P vanishes at the
endpoints of I, both are zeros of sin th. So I is the open upper or lower half-circle, and f = d|y|^gamma on the
corresponding half-plane.
(ii) Suppose c_I != 0. On I, Q = c_I |P|^(k/gamma) has no zero, and as in Step 3, P and Q are smooth on I. Put
eps = sign P on I, s = eps sign(c_I), p = |P|^(1/gamma) and v = lambda p with lambda = k|c_I|/gamma. Substituting
P = eps p^gamma and Q = c_I p^k into the equation for Q and using k - 1 = gamma gives
    c_I k (p^gamma p'' + gamma p^(gamma - 1) p'^2) + c_I k^2 p^(gamma + 1)
        = eps gamma p^(gamma - 1)(p' sin th - p cos th);
dividing by c_I k p^(gamma - 1) and multiplying by lambda^2 (note lambda eps gamma/(c_I k) = s) gives
    v v'' + gamma v'^2 + k v^2 = s(v' sin th - v cos th)   on I.   (28.1)
Here v > 0 is bounded, v tends to 0 at both ends of I, and v^gamma = lambda^gamma |P| is Lipschitz. Put
    G = gamma(v'^2 + v^2) + s(v cos th - v' sin th).
Then (28.1) is equivalent to v'' + v = -G/v, and differentiating G and using this,
    G' = (2 gamma v' - s sin th)(v'' + v) = (s sin th - 2 gamma v') G/v.   (28.2)
On each compact subarc of I the coefficient of G is continuous, so either G = 0 on I, or G > 0 on I, or G < 0 on I.
The substitution th -> -th, with I replaced by -I, maps solutions of (28.1) to solutions of (28.1) and preserves G; it
exchanges the right end of I with the left end of -I.
(iii) Suppose c_I != 0 and G = 0 on I. Then v'' + v = 0 on I, v > 0 on I and v -> 0 at both ends, so v = d sin(th - a)
with d > 0 and b - a = pi. Since sin(th - a) cos th - cos(th - a) sin th = -sin a, G = gamma d^2 - s d sin a, so
d = s sin a/gamma and sin a != 0: the endpoints of I are not horizontal. With n = (-sin a, cos a),
r sin(th - a) = n.X, so f = c(n.X)^gamma on the half-plane n.X > 0 for a constant c != 0.
Step 5 (G != 0 forces a single horizontal zero). Let c_I != 0 and G != 0 on I.
(i) v' has finite limits at both ends of I. If G < 0, the definition of G gives gamma v'^2 <= |v'| + v, so v' is
bounded, and v'' = -v - G/v > -v >= -C_1, so v' + C_1 th is increasing and bounded and has finite limits. If G > 0,
then v'' < -v < 0, so v' is decreasing and has limits in [-inf, +inf]; it suffices to exclude v'(a+) = +inf, the end
b being reduced to this by the substitution th -> -th. Suppose v'(a+) = +inf and fix 0 < eta < 1. By (28.1),
v v'' = -gamma v'^2 - k v^2 + s(v' sin th - v cos th) <= -(gamma - eta) v'^2 where v' is large, so on some
(a, a + delta), where v is increasing, v serves as a variable and d log v'/d log v = v v''/v'^2 <= -(gamma - eta).
Integrating gives v' >= c v^(-(gamma - eta)) on (a, a + delta) with c > 0, and then (v^gamma)' = gamma
v^(gamma - 1) v' >= c gamma v^(eta - 1), which tends to infinity as th -> a+, contradicting the Lipschitz bound on
v^gamma.
(ii) Let d = v'(a+); d >= 0 because v > 0 on I and v(a+) = 0. Then G(a+) = gamma d^2 - s d sin a, and G(a+) = 0:
otherwise |G| >= c > 0 with a fixed sign near a, and since v <= C(th - a), v'' = -v - G/v has a fixed sign and
|v''| >= c/(C(th - a)) - C near a, so int v'' diverges at a, contradicting the finite limit of v'.
(iii) Suppose d > 0. Then d = s sin a/gamma, v = d(th - a)(1 + o(1)), v' -> d and s sin th -> gamma d, so by (28.2),
G'/G = (-gamma + o(1))/(th - a) as th -> a+. Integrating from th to a fixed th_1 gives
log|G(th)| = log|G(th_1)| + int_th^(th_1) (gamma + o(1))/(t - a) dt, which tends to +inf as th -> a+, contradicting
G(a+) = 0. Hence v'(a+) = 0, and by the substitution th -> -th also v'(b-) = 0.
(iv) The ends are horizontal. By (28.1),
    (gamma v^gamma v')' = gamma v^(gamma - 1)(gamma v'^2 + v v'')
        = gamma v^(gamma - 1)(s v' sin th - s v cos th - k v^2),
and since 1 - k = -gamma this is the derivative of s v^gamma sin th - k int_a^th v(t)^gamma (s cos t + gamma v(t)) dt.
Both functions tend to 0 at a, so
    gamma v^gamma v' = s v^gamma sin th - k int_a^th v(t)^gamma (s cos t + gamma v(t)) dt   on I.   (28.3)
For large n let th_n be a maximum point of v on [a, a + 1/n] (with v(a) := 0); then th_n > a, th_n -> a and
v(th_n) = max of v on [a, th_n]. Dividing (28.3) at th_n by v(th_n)^gamma, the integral term is at most
k(1 + gamma C)(th_n - a), so gamma v'(th_n) = s sin th_n + O(th_n - a). Since v'(th_n) -> 0, sin a = 0. By the
substitution th -> -th, sin b = 0.
(v) G > 0 is impossible: then v'' < 0 on I and v'(a+) = 0 give v' < 0 on I and v < v(a+) = 0. So G < 0 and
v'' + v = -G/v > 0 on I. Since a and b are horizontal and 0 < b - a <= 2 pi, b - a is pi or 2 pi. If b - a = pi,
integration by parts on [a + delta, b - delta] gives
    int_(a + delta)^(b - delta) (v'' + v) sin(th - a) dth = [v' sin(th - a) - v cos(th - a)]_(a + delta)^(b - delta),
whose right side tends to 0 as delta -> 0 because v and v' tend to 0 at both ends, while the left side increases to a
positive limit because the integrand is positive. This contradiction gives b - a = 2 pi: I is the circle minus one
horizontal direction, and P has one sign on I and vanishes only at a. With Step 4(ii), this is kind (ii) of (b), the
inequality there being G < 0.
Step 6 (assembly and the zero sets). Let f != 0 be homogeneous and stationary; by Step 3, P has a zero. If some
component I has c_I != 0 and G != 0, Step 5 shows that f is of kind (ii) and I is the only component. Otherwise, by
Step 4(i) and (iii), every component is an open half-circle. Two different components are disjoint open half-circles,
hence complementary, so there are one or two components. A component with horizontal endpoints is of type 4(i),
because type 4(iii) has endpoints that are not horizontal, and a second component is then the complementary
half-circle, also of type 4(i); so f = a_+ y_+^gamma + a_- (-y)_+^gamma, which is F(e.X) with e = e_2. A component
with endpoints that are not horizontal is of type 4(iii), f = c(n.X)^gamma on n.X > 0, and a second component is the
complementary half-circle, also of type 4(iii), on which f = c'(-n.X)^gamma; so f = F(n.X). Thus f is of
kind (i) or (ii). The two kinds exclude each other: for kind (i) the set of zero directions is the pair of directions
of the line e.X = 0 if both amplitudes are nonzero, and a closed half-circle bounded by them otherwise; for kind (ii)
it is one direction. The functions a(r + sigma x)^gamma, a != 0, are stationary (Proposition 2.7(d)), vanish exactly
on the ray r = -sigma x, y = 0, that is in the direction -sigma e_1, and have the sign of a elsewhere; so they are of
kind (ii). In every case {P != 0} has at most two components. Let f be even in x. Its set of zero directions is
invariant under the reflection (x, y) -> (-x, y), which exchanges e_1 and -e_1, so f is not of kind (ii). For
f = F(e.X) != 0 of kind (i) the line e.X = 0 bounding the zero set is then invariant, so it is horizontal or vertical.
If it is horizontal, f is a function of y alone, f = a_+ y_+^gamma + a_- (-y)_+^gamma. If it is vertical,
f = a_+ x_+^gamma + a_- (-x)_+^gamma, and evenness in x gives a_+ = a_- = a, f = a|x|^gamma. Both forms are stationary
by Proposition 2.7(d), and evaluation on the rays in the directions +-e_1 and +-e_2 shows that f >= 0 exactly when the
amplitudes are >= 0.
Step 7 (the functions of kind (ii); rest of (b)). Let f be of kind (ii) with zero direction e_1, so I = (0, 2 pi), and
put z = v e_r + v' e_th. Then
    |z|^2 = v^2 + v'^2,   z_1 = v cos th - v' sin th,
    G = gamma|z|^2 + s z_1 = gamma|z + s e_1/(2 gamma)|^2 - 1/(4 gamma).
Since z' = (v'' + v) e_th, z_1' = -(v'' + v) sin th < 0 on (0, pi) by Step 5(v), and z tends to 0 at th = 0 because
v and v' tend to 0 at the ends of I (Steps 4(ii) and 5(iii)); so z_1 < 0 on (0, pi), and G < 0 gives s = 1. The data
a = v(pi) and b = v'(pi) satisfy G(pi) = gamma(a^2 + b^2) - a < 0, so (a, b) is in D_gamma, and since v(pi) > 0,
(28.1) can be solved for v'' near th = pi, so (a, b) determines v. Conversely, let (a, b) be in D_gamma, and let v be
the solution of (28.1) with s = 1, v(pi) = a and v'(pi) = b, on the largest open interval J containing pi on which it
exists and is positive. Since G(pi) < 0, (28.2) gives G < 0 on J. Hence |z + e_1/(2 gamma)| < 1/(2 gamma), so |v| and
|v'| are less than 1/gamma on J, and v'' = -v - G/v > -1/gamma. At th = 0 and at th = 2 pi a positive solution would
have G = gamma(v^2 + v'^2) + v > 0, so J lies in (0, 2 pi). At each end of J, v' + th/gamma is monotone and bounded,
so v and v' have finite limits, and the limit of v is 0, since otherwise the solution would extend as a positive
solution beyond that end. Steps 5(ii)-(iv) use only (28.1), (28.2), G < 0, the boundedness of v and v' and the limit
0 of v at the ends; so v' tends to 0 at both ends of J, both ends are horizontal, and since J is an interval in
(0, 2 pi) containing pi, J = (0, 2 pi). Extended by 0 at th = 0, v is C^1 and 2 pi-periodic, and so is v^gamma, since
(v^gamma)' = gamma v^(gamma - 1) v' tends to 0 at the ends. Let a_0 != 0, put P = a_0 v^gamma, so that f = r^gamma
P = a_0 (r v(th))^gamma, choose c with sign(c) = sign(a_0) and k|c|/gamma = |a_0|^(-1/gamma), and put
Q = c|P|^(k/gamma) = c|a_0|^(k/gamma) v^k. The computation of Step 4(ii), read backwards with eps = sign(a_0),
p = |a_0|^(1/gamma) v and lambda = |a_0|^(-1/gamma), so that s = 1, shows that Q solves the equation for Q on
(0, 2 pi). There Q' = c k|a_0|^(k/gamma) v^gamma v' and, by (28.1),
Q'' = c k|a_0|^(k/gamma) v^(gamma - 1)(v' sin th - v cos th - k v^2); both tend to 0 at the ends, and so does the
right side -gamma cos th P + sin th P'. So Q, extended by 0, is C^2 and 2 pi-periodic and solves the equation on the
whole circle; it is the periodic solution of Step 2. Since P is Lipschitz and Q = c|P|^(k/gamma) on the only component
of {P != 0}, f is homogeneous, in some E_gamma(C), and stationary by Step 2, of kind (ii) with zero direction e_1; its
function v of (b)(ii) is (k|c|/gamma)|P|^(1/gamma), the given v. The substitution X -> -X maps P to P(th + pi) and
Q to -Q(th + pi): the right side of the equation for Q changes sign under this substitution, so -Q(th + pi) is the
periodic solution for P(th + pi), and k Q P' = gamma Q' P is preserved. So f(-X) is homogeneous and stationary when
f is, the zero directions e_1 and -e_1 are exchanged, c_I and s change sign, and v becomes v(th + pi); this gives the
statement for the zero direction -e_1. The function v = (1 - cos th)/(2 gamma + 1) solves (28.1) with s = 1, by
substitution, and has the data (2/(2 gamma + 1), 0); since r(1 - cos th) = r - x, it gives
f = a_0 (2 gamma + 1)^(-gamma) (r - x)^gamma. Since v is determined by f, through Q and c_I, every a(r - x)^gamma with
a != 0 has this v; the functions a(r + x)^gamma have the zero direction -e_1. So the data (1/(2 gamma), 0), which are
in D_gamma and differ from (2/(2 gamma + 1), 0) because gamma != 1/2, give functions of kind (ii) that are not of the
form a(r + sigma x)^gamma. Finally, the substitution th -> 2 pi - th maps solutions of (28.1) with s = 1 to solutions
of (28.1) with s = 1 and the data (a, b) to (a, -b); for data (a, 0) it follows that v(2 pi - th) = v(th), and f is
even in y. This completes the proof of (b).
Step 8 (proof of (c)). Let rho be an x-even profile. Its limits at infinity are even in x as pointwise limits of the
even functions f_R, and they are stationary by Proposition 2.7(b); by Step 6 a homogeneous one is a|x|^gamma or
a_+ y_+^gamma + a_- (-y)_+^gamma. If rho has only one limit at infinity f, then f is homogeneous by (a); if
f(0, 1) != 0 or f(0, -1) != 0, then f is not a|x|^gamma, so it is a function of y alone, and Proposition 2.7(c) gives
W_2 = o(r^gamma). Now let rho be as in (a) with |D^2 rho(X)| <= C(1 + |X|)^(gamma - 2). For Z != 0 and R >= 1, since
gamma < 2,
    |D^2 f_R(Z)| = R^(2 - gamma) |D^2 rho(RZ)| <= C R^(2 - gamma) (R|Z|)^(gamma - 2) = C|Z|^(gamma - 2).
Let f be the limit along R_n, Z_0 != 0 and B = B(Z_0, |Z_0|/2). On B the gradients grad f_(R_n) are bounded by the
class bound and Lipschitz with constant C_B = C(|Z_0|/2)^(gamma - 2). By the Arzela-Ascoli theorem a subsequence
converges uniformly on B to a field H_B with Lipschitz constant C_B, and passing to the limit in
f_(R_n)(Z) - f_(R_n)(Z_0) = int_0^1 grad f_(R_n)(Z_0 + t(Z - Z_0)).(Z - Z_0) dt shows that f is C^1 on B with
grad f = H_B. Suppose f = F(e.X) != 0, and, replacing e by -e if necessary, a_+ != 0. Take X_0 != 0 with e.X_0 = 0.
For t > 0, grad f(X_0 + te) - grad f(X_0) = gamma a_+ t^(gamma - 1) e, and t^(gamma - 1)/t -> infinity as t -> 0+
because gamma < 2, contradicting the local Lipschitz bound on grad f near X_0. So no nonzero F(e.X) is a limit at
infinity. If a limit at infinity f is a function F(y) of y alone, let y_1 and y_2 be real and L > 2(|y_1| + |y_2|);
the points (L, y_1) and (L, y_2) lie in B((L, 0), L/2), on which grad f = (0, F'(y)) is Lipschitz with constant
C(L/2)^(gamma - 2), so |F'(y_1) - F'(y_2)| <= C(L/2)^(gamma - 2) |y_1 - y_2|, which tends to 0 as L -> infinity. So F'
is constant, F is affine, and |F(y)| <= C|y|^gamma with gamma > 1 gives F = 0. By Proposition 2.7(c), W_2 = o(r^gamma)
holds if and only if every limit at infinity is a function of y alone, that is, 0; by the precompactness of the f_R
this holds if and only if f_R -> 0 locally uniformly, that is, if and only if rho = o(r^gamma). For an x-even profile
with the Hessian bound, each function listed in Step 6 for x-even f is of the form F(e.X): a|x|^gamma with e = e_1 and
a_+ = a_- = a, and the functions of y alone with e = e_2. So every homogeneous limit at infinity is 0. If such a
profile has only one limit at infinity, it is homogeneous by (a), hence 0, so f_R -> 0 locally uniformly, the maximum
of R^(-gamma)|rho(RZ)| over |Z| = 1 tends to 0, that is rho = o(r^gamma), and
Proposition 2.7(c), applied to the layered limit 0, gives W_2 = o(r^gamma). The remaining assertions of (c) concern
kind (ii).
(i) Identities and an energy. Let f be of kind (ii) with zero direction e_1, so that by (b) and Step 7, s = 1,
I = (0, 2 pi), the data (a, b) = (v(pi), v'(pi)) are in D_gamma, and kappa = v'' + v = -G/v > 0 on I (Step 5(v)). Put
c_0 = 1/(2 gamma + 1) and L = 1/gamma, and suppose (a, b) != (2 c_0, 0). We show that (v^gamma)'' is unbounded as
th -> 0+. This suffices: the substitution th -> 2 pi - th maps v to the solution with the data (a, -b) != (2 c_0, 0),
which gives the end 2 pi; replacing f by f(-X), which replaces v by v(th + pi), gives the zero direction -e_1. For
0 < th < pi/2, G < 0 gives gamma v'^2 + v cos th < v' sin th, so 0 < v' < sin th/gamma and
v < sin^2 th/(gamma cos th). Put zeta = v'/sin th, so 0 < zeta < L, and xi = -log tan(th/2), so that xi decreases from
infinity to 0 as th increases from 0 to pi/2 and dth/dxi = -sin th. Since v kappa = -G, the definition of G gives
v(kappa + cos th + gamma v) = v' sin th - gamma v'^2, that is
    v(kappa + cos th + gamma v) = zeta(1 - gamma zeta) sin^2 th.   (28.4)
By (28.2) and kappa = -G/v, kappa' = kappa(sin th - (2 gamma + 1) v')/v. With this, the definition of zeta and (28.4),
    zeta_xi = zeta cos th + v - kappa,   kappa_xi = kappa(kappa + cos th + gamma v) varphi(zeta),   (28.5)
where varphi(zeta) = (zeta - c_0)/(c_0 zeta(1 - gamma zeta)) and the subscript xi denotes d/dxi. Let
    Phi = -log zeta - (k/gamma) log(1 - gamma zeta) - c_0 log kappa + (1 + c_0) log(1 + kappa).
The derivative of the zeta-part of Phi is varphi(zeta), which has the sign of zeta - c_0, and that of the kappa-part
is (kappa - c_0)/(kappa(1 + kappa)); the two parts have their minima at zeta = c_0 and at kappa = c_0, and tend to
infinity at the ends of 0 < zeta < L and of 0 < kappa < infinity, respectively. So Phi is bounded below, and each set
{Phi <= Lambda} is a compact subset of the strip {0 < zeta < L, kappa > 0}. Along the solution, (28.5) gives
    Phi_xi = chi + varphi(zeta) omega,   chi = (zeta - c_0) varphi(zeta) >= 0,
    omega = (cos th - 1) zeta + v + (kappa - c_0)(cos th - 1 + gamma v)/(1 + kappa).
Since |kappa - c_0| <= 1 + kappa and v <= 2 th^2 for small th, |omega| <= C_2 th^2. Where |zeta - c_0| >= c_0/2,
|varphi(zeta)| <= 2 chi/c_0, so |varphi omega| <= chi/2 for small th; where |zeta - c_0| < c_0/2,
zeta(1 - gamma zeta) >= m_0 for some m_0 > 0, since 3 c_0/2 < L, so varphi^2 <= chi/(c_0 m_0) and
|varphi omega| <= c_0 m_0 varphi^2/2 + C_2^2 th^4/(2 c_0 m_0) <= chi/2 + C_3 th^4. Hence there is xi_0 such that
    Phi_xi >= chi/2 - C_3 th^4   for xi >= xi_0.   (28.6)
Since th = 2 arctan(e^(-xi)) <= 2 e^(-xi), the function Phi + C_3 int_(xi_0)^xi th^4 dxi is nondecreasing, so Phi has
a limit in (-infinity, infinity] as xi -> infinity.
(ii) Phi tends to infinity. Suppose that Phi is bounded on [xi_0, infinity). Then (zeta, kappa) stays in a compact
subset of the strip, on which chi(zeta), zeta_xi and kappa_xi are bounded and chi is Lipschitz in zeta, and by
(28.6) chi(zeta(xi)) is integrable on [xi_0, infinity). Being Lipschitz in xi, it tends to 0, so zeta -> c_0. Also
kappa -> c_0: otherwise there are mu > 0 and xi_j -> infinity with |kappa(xi_j) - c_0| >= mu, and if
|kappa_xi| <= C_6, then |kappa - c_0| >= mu/2, with the sign of kappa(xi_j) - c_0, on [xi_j, xi_j + mu/(2 C_6)]; since
zeta_xi = (zeta - c_0) + (cos th - 1) zeta + v - (kappa - c_0), for large j zeta_xi has the opposite sign and modulus
at least mu/4 there, and zeta changes by at least mu^2/(8 C_6) on these intervals, contradicting zeta -> c_0. By
(28.4), v/sin^2 th -> c_0(1 - gamma c_0)/(1 + c_0) = c_0/2. So eta_1 = v/th^2 and eta_2 = v'/th tend to c_0/2 and c_0
as th -> 0+. In the variable tau = log th, (28.1) with s = 1 becomes
    d eta_1/d tau = eta_2 - 2 eta_1,
    d eta_2/d tau = (eta_2 sin th/th - gamma eta_2^2)/eta_1 - cos th - k th^2 eta_1 - eta_2.
At th = 0 the right side vanishes at (c_0/2, c_0), and its derivative with respect to (eta_1, eta_2) there is the
matrix A_0 with rows (-2, 1) and (-4k, 1), of trace -1 and determinant 4 gamma + 2; both eigenvalues of A_0 have real
part -1/2, so there is a positive definite symmetric matrix B_0 with A_0^T B_0 + B_0 A_0 = -I. The function
c_0(1 - cos th) of Step 7 gives a second solution of this system tending to (c_0/2, c_0) as tau -> -infinity. The
difference Delta of the two solutions satisfies d Delta/d tau = A(tau) Delta, where A(tau) is the mean of that
derivative over the segment between the two solutions at th = e^tau, and A(tau) -> A_0 as tau -> -infinity because
both solutions tend to (c_0/2, c_0), where eta_1 > 0. So there is tau_1 such that on (-infinity, tau_1] the derivative
of Delta^T B_0 Delta with respect to tau is at most -|Delta|^2/2. There the nonnegative function Delta^T B_0 Delta is
nonincreasing and tends to 0 as tau -> -infinity, so it vanishes. Hence v = c_0(1 - cos th) near th = 0, and by
uniqueness for (28.1) on the interval where both are positive, v = c_0(1 - cos th) on (0, 2 pi) and
(a, b) = (2 c_0, 0), which is excluded. So Phi -> infinity.
(iii) Phi grows faster than xi. Fix 0 < delta < c_0/2 and put I_delta = [delta, L - delta]. Phi is bounded on the
compact set I_delta times [delta/4, 2L + 2] of the strip, so by (ii) there is xi_1 >= xi_0 such that for xi >= xi_1,
zeta(xi) in I_delta implies kappa < delta/4 or kappa > 2L + 2; we take xi_1 so large that cos th >= 3/4 and v <= 1 for
xi >= xi_1. By (28.5), zeta_xi >= delta/2 where zeta is in I_delta and kappa < delta/4, and
zeta_xi <= L + 1 - (2L + 2) < -1 where kappa > 2L + 2. A visit is a maximal interval of [xi_1, infinity) on which zeta
is in I_delta. By continuity kappa stays on one side of [delta/4, 2L + 2] during a visit, so zeta is strictly monotone
on each visit and every visit has length at most 2L/delta + L. A visit with small kappa ends at zeta = L - delta and,
unless it begins at xi_1, begins at zeta = delta; a visit with large kappa ends at zeta = delta and, unless it begins
at xi_1, begins at zeta = L - delta. Between two consecutive visits zeta stays outside I_delta on the side where the
first one ended, so the second begins where the first ended; hence the visits alternate between the two kinds. Let
0 < delta' < delta. The same reasoning for I_delta' with the bounds delta'/4 and 2L + 2 gives xi_2 >= xi_1 such that
for xi >= xi_2, zeta in I_delta' implies kappa < delta'/4 or kappa > 2L + 2. Let a visit with large kappa end at
xi' >= xi_2 and let the next visit begin at xi''. On (xi', xi'') one has zeta < delta. If zeta >= delta' on
[xi', xi''], then kappa avoids [delta'/4, 2L + 2] on [xi', xi''], while kappa(xi') > 2L + 2 and
kappa(xi'') < delta/4 < 2L + 2, which is impossible. So zeta < delta' at some point of (xi', xi''). By (28.4),
v cos th <= zeta sin^2 th, so v <= zeta for large xi, and zeta_xi <= 2 zeta by (28.5); hence the return from below
delta' to delta takes a xi-interval of length at least (1/2) log(delta/delta'). These intervals are disjoint, and by
the alternation the number of visits that meet [xi_2, Xi] is at most 4(Xi - xi_2)/log(delta/delta') + 2. So the
measure m_delta(Xi) of the set of xi in [xi_0, Xi] with zeta(xi) in I_delta satisfies
m_delta(Xi)/Xi <= 4(2L/delta + L)/log(delta/delta') + o(1) as Xi -> infinity, and letting delta' -> 0 gives
m_delta(Xi)/Xi -> 0. Finally, chi tends to infinity at both ends of (0, L). Given Lambda > 0, choose delta with
chi >= 4 Lambda outside I_delta; integrating (28.6) gives Phi(Xi) >= 2 Lambda(Xi - xi_0 - m_delta(Xi)) - C_4, so the
lower limit of Phi(Xi)/Xi is at least 2 Lambda. As Lambda is arbitrary, Phi/xi -> infinity.
(iv) Large curvature at the slope c_0. Suppose zeta >= c_0 on some [xi_3, infinity), and let delta and xi_1 be as in
part (iii), with xi_1 >= xi_3. A visit with large kappa would end at zeta = delta < c_0; so every visit has small
kappa, it ends at zeta = L - delta, and no visit follows it. Hence, as zeta >= c_0 > delta, zeta > L - delta for all
large xi, and as delta is arbitrary, zeta -> L. Then varphi(zeta) -> infinity, so by (28.5) kappa_xi >= kappa^2 and
(1/kappa)_xi <= -1 for large xi, and 1/kappa would become negative at a finite xi, which is impossible. Suppose
zeta <= c_0 on some [xi_3, infinity). In the same way every visit has large kappa, ends at zeta = delta and is not
followed by another; as zeta <= c_0 < L - delta, zeta < delta for all large xi, so zeta -> 0. Then v'/th -> 0 as
th -> 0+, so sin th - (2 gamma + 1) v' >= th/2 > 0 near th = 0, and
kappa' = kappa(sin th - (2 gamma + 1) v')/v > 0 there; so kappa is increasing, hence bounded and integrable near 0,
and since v and v' tend to 0 at 0,
    v(th) = int_0^th sin(th - t) kappa(t) dt <= kappa(th)(1 - cos th) <= kappa(th) th^2/2.
Then kappa'/kappa >= th/(2v) >= 1/(th kappa), that is kappa' >= 1/th on some (0, th_0]; integrating from t_1 to th_0
gives kappa(t_1) <= kappa(th_0) - log(th_0/t_1), which is negative for small t_1, a contradiction. So zeta - c_0 takes
both signs at arbitrarily large xi, and there are xi_j -> infinity with zeta(xi_j) = c_0 and
zeta_xi(xi_j) <= 0 (the first point with zeta = c_0 after a point with zeta > c_0). Let th_j, v_j and kappa_j be the
values of th, v and kappa at xi_j. By (28.5), kappa_j >= c_0 cos th_j >= c_0/2. At zeta = c_0 the zeta-part of Phi is
a constant, and the kappa-part equals log kappa + (1 + c_0) log(1 + 1/kappa), which is log kappa + O(1) for
kappa >= c_0/2. So (ii) and (iii) give kappa_j -> infinity and log(kappa_j)/xi_j -> infinity.
(v) The second derivative and the conclusion. Differentiating v^gamma twice and using (28.1) with s = 1,
    (v^gamma)'' = gamma v^(gamma - 2)(v' sin th - v'^2 - v cos th - k v^2).
At th_j, v' sin th - v'^2 = (c_0 - c_0^2) sin^2 th = 2 gamma c_0^2 sin^2 th, and by (28.4), since
c_0(1 - gamma c_0) = k c_0^2, v_j <= k c_0^2 sin^2 th_j/kappa_j; so
v_j cos th_j + k v_j^2 <= v_j(1 + k) <= gamma c_0^2 sin^2 th_j for large j. As gamma - 2 < 0, this gives for large j
    (v^gamma)''(th_j) >= gamma^2 c_0^2 (k c_0^2)^(gamma - 2) (sin th_j)^(2 gamma - 2) kappa_j^(2 - gamma).
Since sin th >= tan(th/2) = e^(-xi) for 0 < th <= pi/2,
log (v^gamma)''(th_j) >= (2 - gamma) log kappa_j - (2 gamma - 2) xi_j - C_5, which tends to infinity by (iv) because
2 - gamma > 0. So (v^gamma)'' is unbounded as th -> 0+. Now P = a_1 v^gamma on I with a_1 != 0, by (b)(ii), and in the
orthonormal frame (e_r, e_th) the Hessian of f = r^gamma P has the entry
e_th.D^2 f e_th = r^(gamma - 2)(gamma P + P'') off the zero ray. So D^2 f is unbounded near the point e_1 of the unit
circle, and by homogeneity near every point of the zero ray. Off the zero ray f is C^2, and a Lipschitz constant of
grad f on a ball bounds |D^2 f| at the points of the ball off the ray; so grad f is not Lipschitz on any neighborhood
of a point of the zero ray. If instead (a, b) = (2 c_0, 0), then f is a nonzero multiple of (r - x)^gamma by Step 7,
and (r - x)^gamma is C^2 on the punctured plane: near the ray in the direction e_1, r - x = y^2/(r + x), so
(r - x)^gamma = |y|^(2 gamma)(r + x)^(-gamma), which is C^2 because 2 gamma > 2, and away from that ray r - x > 0 is
smooth. Likewise (r + x)^gamma is C^2 on the punctured plane. Finally let rho be a profile with the Hessian bound. Its
limits at infinity are stationary (Proposition 2.7(b)) and have a locally Lipschitz gradient on the punctured plane,
as shown above; so by (b) a homogeneous one is 0, or F(e.X), which is excluded above, or of kind (ii) and then of the
form a(r + sigma x)^gamma. This completes the proof of (c).
Step 9 (proof of (d)). Let rho, f, h and q be as in (d). (i) h is locally Lipschitz. For |Y| <= 1 the jet gives
|rho(Y)| <= C|Y|^2, so |h(Y)| <= C|Y|^gamma and |grad h(Y)| <= C|Y|^(gamma - 1) almost everywhere; for |Y| >= 1,
|h(Y)| <= C|Y|^q and |grad h(Y)| <= C|Y|^(gamma - 1) almost everywhere by the class bounds for rho and f. So h is in
E_gamma(C') for some C'. Since f_R - f = R^(-gamma) h(R.) and R^(-gamma)|h(RZ)| <= C R^(-gamma)(1 + R|Z|)^q,
f_R -> f locally uniformly, so f is the only limit at infinity. By Section 9.14, Step 4, DK(-Y) is symmetric and
traceless with |DK(-Y)| <= C|Y|^(-3), so the integrand of M is bounded by C|Y|^(gamma - 3) for |Y| <= 1 and by
C|Y|^(q - 3) for |Y| >= 1; both are integrable in the plane because gamma > 1 and q < 1, and M is symmetric and
traceless.
(ii) Put u(X) = p.v. int [K(X - Y) - K(-Y)] h(Y) dY - h(X) e_2/2, the principal value being circular at Y = X. For
|X| <= L the integral converges: |K(X - Y) - K(-Y)| <= C L |Y|^(-3) for |Y| >= 2L by the mean value theorem and
|DK(Z)| <= C|Z|^(-3), and |h(Y)| <= C|Y|^q with q < 1; near Y = 0, |K(-Y) h(Y)| <= C|Y|^(gamma - 2); near Y = X the
circular cancellation and the local Lipschitz bound on h give convergence as in Section 9.27, Step 1. Since the
integral of DK(-Y)X h(Y) converges absolutely, the defining integral of W_2[h] splits, W_2[h] = u + MX, and by the
linearity of the defining integral, W_2 = W_2[rho] = W_2[f] + W_2[h] = W_2[f] + MX + u.
(iii) The bound on u. Let r = |X| >= 2. On B(X, r/2), r/2 <= |Y| <= 3r/2, so |h(Y)| <= C r^q and
|grad h(Y)| <= C r^(gamma - 1) almost everywhere. Put d = min(1, r^(q - gamma + 1)). On B(X, d) the circular
cancellation leaves int |K(X - Y)| |h(Y) - h(X)| dY <= C r^(gamma - 1) d <= C r^q. On d <= |X - Y| < r/2,
|K(X - Y) h(Y)| <= C r^q |X - Y|^(-2), with integral at most C r^q log(r/d) <= C r^q log(2 + r). On the rest of
|Y| < 2r, |K(X - Y)| <= C r^(-2) and the integral of |h| over |Y| < 2r is at most C r^(2 + q), which gives C r^q; and
the integral of |K(-Y) h(Y)| over |Y| < 2r is at most
C int_0^1 s^(gamma - 1) ds + C int_1^(2r) s^(q - 1) ds <= C(1 + r)^q log(2 + r). On |Y| >= 2r,
|K(X - Y) - K(-Y)| <= C r |Y|^(-3), which gives C r int_(2r)^inf s^(q - 2) ds <= C r^q. With |h(X)| <= C r^q this
proves |u(X)| <= C(1 + r)^q log(2 + r) for r >= 2, and for r <= 2 the same splitting with B(X, 1) in place of
B(X, r/2) bounds u by a constant. This proves the expansion of W_2 in (d).
(iv) The first surviving order. Let rho be a profile. By (i) and Proposition 2.7(b), f is stationary. Put
eps_R = R^(1 - gamma). On |Z| <= L, (f_R - f)/eps_R = R^(-1) h(RZ) = O(R^(q - 1)) uniformly. Since D_R f = f, the
scaling in Proposition 2.7(a) gives W_2[f](RZ) = R^gamma W_2[f](Z), so
    W_2[f_R](Z) = R^(-gamma) W_2(RZ) = W_2[f](Z) + eps_R MZ + R^(-gamma) u(RZ),
and R^(-gamma) u(RZ)/eps_R = R^(-1) u(RZ) = O(R^(q - 1) log(2 + RL) + R^(-1)) uniformly on |Z| <= L. By Section 9.27,
Step 2, div(f_R W_2[f_R]) + eps_R [div(f_R AZ) - (1 + 2l) f_R] = 0 in distributions. Subtracting div(f W_2[f]) = 0,
dividing by eps_R and testing against phi gives
    int [((f_R - f)/eps_R) W_2[f_R] + f (W_2[f_R] - W_2[f])/eps_R].grad phi dZ
        + int [f_R AZ.grad phi + (1 + 2l) f_R phi] dZ = 0.
As R -> infinity the first integrand converges to f MZ.grad phi uniformly on the support of phi, and f_R -> f. So
div(f (A + M)Z) = (1 + 2l) f in distributions. Since tr(A + M) = 1/2 + beta = 2l and f is locally Lipschitz,
div(f (A + M)Z) = ((A + M)Z).grad f + 2l f, which gives ((A + M)Z).grad f = f in distributions, and almost everywhere.
(v) Consequences. Put S = A + M, a symmetric matrix. Let f = F(e.X) != 0, and, replacing e by -e if necessary,
a_+ != 0. On the half-plane e.X > 0, grad f = gamma a_+ (e.X)^(gamma - 1) e, so the identity gives gamma e.SX = e.X
there, that is Se = e/gamma. For e = e_1 this is 1/2 + M_11 = 1/gamma and M_12 = 0. Let f be of kind (ii), with zero
direction e_0 = e_1 or -e_1, and let v be as in (b)(ii) on I. Put g = r v(th) for th in I and g = 0 on the ray in the
direction e_0. Since v and v' tend to 0 at the ends of I, g is C^1 on the punctured plane with grad
g = v e_r + v' e_th, which vanishes on that ray; g > 0 off the ray, g(tX) = t g(X) for t > 0, and f = a_0 g^gamma with
a_0 = sign(P)(k|c_I|/gamma)^(-gamma) != 0. So f is C^1 on the punctured plane, the identity holds there pointwise, and
dividing by gamma a_0 g^(gamma - 1) gives SX.grad g = g/gamma off the ray; on the ray both sides vanish. For
X != 0 the function t -> g(e^(tS) X) therefore has derivative g(e^(tS) X)/gamma, so g(e^(tS) X) = e^(t/gamma) g(X).
For X = e_0 this vanishes for all t, so e^(tS) e_0 stays on the ray, S e_0 is a multiple of e_0, and S_12 = 0. At
X = -e_0 and at X = e_2, where g > 0, SX = S_11 X and SX = S_22 X, and Euler's relation X.grad g = g gives
S_11 = S_22 = 1/gamma. So S = I/gamma, and tr S = 2l gives l = 1/gamma. Let M = 0, so S = A. Then Ae = e/gamma with
e_1 != 0, and A = I/gamma, would both give 1/2 = 1/gamma, which is false because gamma < 2. By (b), f is therefore
F(e.X) with e_1 = 0 or f = 0: f is a function of y alone, W_2[f] = 0 by Proposition 2.7(c), and
W_2 = u = O((1 + r)^q log(2 + r)) = o(r). If moreover f = a_+ y_+^gamma + a_- (-y)_+^gamma != 0, the identity reads
beta y f_y = f, and y f_y = gamma f gives beta gamma = 1.
Step 10 (proof of (e)). Let alpha = 1/gamma - 1/2 > 0. The density f_gamma(x) of Section 9.14, Step 8, is smooth,
nonnegative and even, equals x^2 + O(x^4) near 0, satisfies the bounds of S with exponent gamma, and has
W_2[f_gamma] = (0, -f_gamma(x)) (Section 9.14, Step 8). For |x| >= 1, f_gamma(x) = |x|^gamma (1 - t)^((2 - gamma)/2)
with t = 1/(1 + x^2), and 0 <= 1 - (1 - t)^((2 - gamma)/2) <= t because (2 - gamma)/2 < 1, so
|f_gamma(x) - |x|^gamma| <= |x|^gamma/(1 + x^2) <= 1; so f_gamma - |x|^gamma is bounded on the line. Choose a smooth
function g_0 >= 0, not identically 0 and even in x, supported in the union of the two disks of radius 1/2 about
(3^(1/2), 1) and (-3^(1/2), 1). These disks lie in 3/2 <= |Y| <= 5/2 and in the angular sectors |th - pi/6| < pi/9 and
|th - 5 pi/6| < pi/9, where sin(3 th) > 0. Since g_0 vanishes near 0, its compact Biot-Savart field
U[g_0] = p.v. int K(. - Y) g_0(Y) dY - g_0 e_2/2 is C^2 (Section 9.14, Step 2), and DU[g_0](0) = int DK(-Y) g_0(Y) dY
by differentiation under the integral, the kernel being smooth near X = 0 on the support. By the formula in
Section 9.14, Step 4, the (1,1) entry of this matrix is -int sin(3 th)
g_0(Y)/(pi s^3) dY =: -a_0 < 0 (Y = s(cos th, sin th)), the (2,2) entry is a_0, and the off-diagonal entry,
int cos(3 th) g_0(Y)/(pi s^3) dY, vanishes because cos(3(pi - th)) = -cos(3 th) and g_0 is even in x. Put
g = (alpha/a_0) g_0 and rho_* = f_gamma(x) + g. Then rho_* is smooth, nonnegative and even in x, equals f_gamma near
0 (so it has the jet), satisfies the bounds of S with exponent gamma, and
rho_* - |x|^gamma = (f_gamma - |x|^gamma) + g is bounded. Since g is smooth with compact support away from 0, the two
subtraction terms in W_2[g] are absolutely integrable, and the translated term is taken in circular principal value at
Y = X. Thus W_2[g] = U[g] - U[g](0) - DU[g](0)X, with DU[g](0) = diag(-alpha, alpha). The first component
K^(1)(x, y) = -xy/(pi (x^2 + y^2)^2) of K is odd in x, and g is even in x, so U[g]^(1) is odd in x and
U[g]^(1)(0) = 0. For |X| >= 5, U[g](X) = int K(X - Y) g(Y) dY = O(|X|^(-2)), and U[g] is bounded on the plane. By
linearity of the defining integral,
    W_2[rho_*] = (0, -f_gamma(x)) + W_2[g] = (alpha x + U[g]^(1), -alpha y - f_gamma(x) + U[g]^(2) - U[g]^(2)(0)),
which gives the asymptotics in (e). By (d) with f = |x|^gamma and q = 0,
W_2[rho_*] = W_2[|x|^gamma] + MX + O(log(2 + r)), and W_2[|x|^gamma] = (0, -|x|^gamma) by Proposition 2.7(d);
comparing with the display, (M - diag(alpha, -alpha))X = O(log(2 + r)), so M = diag(alpha, -alpha). In particular
M_11 = 1/gamma - 1/2 and M_12 = 0, the condition of (d) for |x|^gamma. For real l the field V = AX + W_2[rho_*] is C^1
and, since 1/2 + alpha = 1/gamma,
    V = (x/gamma + U[g]^(1), (beta - alpha) y - f_gamma(x) + U[g]^(2) - U[g]^(2)(0)).
With |U[g]| <= C_U, the first component bounds |x| on every bounded time interval of a solution, in either time
direction; then f_gamma(x) is bounded there, and the second component, linear in y up to a bounded term, bounds |y|
there by the Gronwall inequality. So no solution leaves every compact set in finite time, and the flow is complete.
Off the support of g, rho_* = f_gamma(x) and grad rho_* = (f_gamma'(x), 0), so with
f_gamma'(x) = x(2 + gamma x^2)(1 + x^2)^((gamma - 4)/2) from Section 9.14, Step 8,
    E := V.grad rho_* - rho_* = x f_gamma'(x)/gamma - f_gamma(x) + U[g]^(1)(X) f_gamma'(x)
       = ((2 - gamma)/gamma) x^2 (1 + x^2)^((gamma - 4)/2) + U[g]^(1)(X) f_gamma'(x).
The first term lies between 0 and (2 - gamma)/gamma; for |X| >= 5 the second is at most
C|X|^(-2)(1 + |X|)^(gamma - 1); and E is continuous on |X| <= 5. So E is bounded. For fixed x != 0 and |y| -> infinity
the second term tends to 0 and the first is a positive constant, so E is not identically 0. Since these values of
E off the support of g do not depend on l, rho_* is not a profile for any real l.
Step 11 (proof of (f)). Let rho be a profile with V = AX + W_2, W_2 = W_2[rho]; rho is in E_gamma(C_0) by
Proposition 2.7(b). Suppose first rho(x, -y) = rho(x, y). The field w(x, y) = (-W_2^(1)(x, -y), W_2^(2)(x, -y)) is
continuous, O(|X|^gamma), vanishes at 0 with derivative 0 there, and has div w = -(div W_2)(x, -y) = 0 and
curl w = (curl W_2)(x, -y) = -rho_x(x, -y) = -rho_x(x, y). By the uniqueness in Proposition 2.7(a), w = W_2, so
W_2^(1)(x, 0) = 0; also rho_y(x, 0) = 0 by evenness in y. On the x-axis the profile equation becomes
(x/2) rho_x(x, 0) = rho(x, 0). As in Section 9.14, Step 8, this gives rho(x, 0)/x^2 constant on x > 0 and on x < 0,
the jet makes both constants 1, and rho(x, 0) = x^2 contradicts |rho| <= C(1 + r)^gamma with gamma < 2. Suppose next
rho(-X) = rho(X). The field w(X) = W_2(-X) is continuous, O(|X|^gamma), vanishes at 0 with derivative 0, and has
div w = -(div W_2)(-X) = 0 and curl w = -(curl W_2)(-X) = rho_x(-X) = -rho_x(X), since rho_x is odd. By the
uniqueness, W_2(-X) = W_2(X). Since grad rho is odd, W_2.grad rho is odd, while AX.grad rho and rho are even; adding
the profile equations at X and at -X gives AX.grad rho = rho on the plane, so (x/2) rho_x = rho on the x-axis, and the
same contradiction follows. The jet x^2 + O(|X|^3) is compatible with both symmetries, so neither is excluded by the
jet alone.
Step 12 (proof of (g)). Let rho be a profile with l > 1/2 whose flow Phi_t is complete, and put d = 2l > 1 and
beta = d - 1/2 > 1/2. By Section 9.14, Step 3, V = AX + W_2 is C^2 on the plane, V(0) = 0, DV(0) = A = diag(1/2, beta)
and div V = tr A = d. So each Phi_t is a C^1 diffeomorphism of the plane with Jacobian determinant e^(dt), and
rho(Phi_t X) = e^t rho(X) for all t and X, because the derivative of rho(Phi_t X) in
t is (V.grad rho)(Phi_t X) = rho(Phi_t X). By the jet and the growth bound with gamma < 2, |rho(X)| <= C_rho |X|^2 on
the plane for some C_rho, and rho(X) = x^2 + O(|X|^3) near 0.
(i) The backward flow near 0. Write V(X) = AX + N(X), so that |N(X)| <= C|X|^2 and |DN(X)| <= C|X| for |X| <= 1. For
P near 0 and t >= 0 put Z_t = Phi_(-t)(P), so that dZ_t/dt = -V(Z_t). Since X.AX >= |X|^2/2,
d|Z_t|/dt <= -|Z_t|/2 + C|Z_t|^2 while |Z_t| <= 1. Hence there is r_0 in (0, 1) such that |P| <= r_0 gives
|Z_t| <= |P| e^(-t/3) for all t >= 0; then d|Z_t|/dt <= -|Z_t|/2 + C|P| e^(-t/3) |Z_t|, so that
|Z_t| <= C|P| e^(-t/2). The derivative Y_t = D_P Z_t solves dY_t/dt = -(A + DN(Z_t)) Y_t with Y_0 = I, and since A is
symmetric with smallest eigenvalue 1/2, |Y_t| <= e^(-t/2) exp(int_0^t |DN(Z_u)| du) <= C e^(-t/2).
(ii) A local coordinate. Since A is diagonal, d(e^(t/2) (Z_t)_1)/dt = -e^(t/2) N_1(Z_t), and
|N_1(Z_t)| <= C|P|^2 e^(-t) and |D_P[N_1(Z_t)]| <= |DN(Z_t)| |Y_t| <= C|P| e^(-t). So for |P| <= r_0 the limit
    nu(P) = lim_(t -> infinity) e^(t/2) (Z_t)_1 = P_1 - int_0^infinity e^(u/2) N_1(Z_u) du
exists, uniformly together with the first derivatives in P; nu is C^1, nu(P) = P_1 + O(|P|^2) and
D nu(P) = (1, 0) + O(|P|). Similarly
    e^(t/2) (Z_t)_2 = e^(-(beta - 1/2)t) P_2 - int_0^t e^(-(beta - 1/2)(t - u)) e^(u/2) N_2(Z_u) du,
and since e^(u/2) N_2(Z_u) and its first derivatives in P are O(e^(-u/2)), and
int_0^t e^(-(beta - 1/2)(t - u)) e^(-u/2) du tends to 0 as t -> infinity because beta > 1/2, this tends to 0 together
with its first derivatives in P, uniformly on |P| <= r_0. So
    e^(t/2) Phi_(-t)(P) -> (nu(P), 0)   in C^1 on |P| <= r_0 as t -> infinity.   (28.7)
Moreover rho(P) = e^t rho(Z_t) = (e^(t/2) (Z_t)_1)^2 + O(e^t |Z_t|^3), which tends to nu(P)^2; so rho = nu^2 on
|P| <= r_0. Decreasing r_0, the x-derivative of nu is at least 1/2 on |P| <= r_0, so nu(x, 0) has the sign of x, and
rho(x, 0) > 0 for 0 < |x| <= r_0. Put delta_0 = r_0.
(iii) A Jordan curve. Let 0 < delta < delta_0, and suppose that (-delta, 0) and (delta, 0) lie in one component of
{rho > 0}. A connected open subset of the plane is connected by polygonal paths, so a polygonal path in {rho > 0}
joins the two points. Its image is compact and does not contain 0, where rho = 0, so it avoids a closed disk B' about
0 of some radius delta' in (0, delta). Adding the segments from (-delta', 0) to (-delta, 0) and
from (delta, 0) to (delta', 0), which lie in {rho > 0} by (ii), and removing loops gives a simple polygonal arc Gamma
in {rho > 0} from (-delta', 0) to (delta', 0) whose other points lie outside B'. With the segment
ell = [-delta', delta'] x {0}, J = ell union Gamma is a Jordan curve. Let Omega be its bounded complementary
component, an open set of positive area, and let m > 0 be the minimum of rho on Gamma.
(iv) Contraction of area. For t >= 0 the map T_t(X) = e^(t/2) Phi_(-t)(X) is a homeomorphism of the plane, so
J_t = T_t(J) is a Jordan curve and Omega_t = T_t(Omega) is its bounded complementary component. By the Jacobian
determinant of Phi_(-t), |Omega_t| = e^t e^(-dt) |Omega| = e^(-(d - 1)t) |Omega|, which tends to 0 as t -> infinity
because d > 1. For P in Gamma, C_rho |Phi_(-t)(P)|^2 >= rho(Phi_(-t)(P)) = e^(-t) rho(P) >= m e^(-t), so T_t(Gamma)
lies outside the disk of radius b_1 = (m/C_rho)^(1/2) about 0.
(v) The contradiction. By (28.7), the curves c_t(x) = T_t(x, 0), |x| <= delta', converge in C^1 as t -> infinity to
x -> (nu(x, 0), 0), and nu(x, 0) has x-derivative at least 1/2, so nu(-delta', 0) <= -delta'/2 and
nu(delta', 0) >= delta'/2. Let 0 < b < min(b_1/2, delta'/4), and let Q_b be the open square (-b, b) x (-b, b), which
lies in the disk of radius b_1 about 0. For all large t the first component of c_t has derivative at least 1/4, is
less than -b at x = -delta' and greater than b at x = delta', and the second component of c_t is less than b/8 in
absolute value. So T_t(ell) meets Q_b exactly in the graph {y = h_t(x), |x| < b} of a continuous function h_t with
|h_t| < b/8, while T_t(Gamma) does not meet Q_b. The sets H_+ = {(x, y) in Q_b : y > h_t(x)} and
H_- = {(x, y) in Q_b : y < h_t(x)} are disjoint from J_t, and they are connected: each vertical segment in H_+ joins
its point to the segment (-b, b) x {b/2}, which lies in H_+, and similarly for H_-. So each of H_+ and H_- lies in
Omega_t or in the unbounded component. By the Jordan curve theorem the point (0, h_t(0)) of J_t is a boundary point of
Omega_t, and a small disk about it meets the complement of J_t only in H_+ union H_-; so Omega_t meets one of H_+ and
H_-, which then lies in Omega_t. Both contain a disk of radius b/8, about (0, b/2) and about (0, -b/2), respectively.
So |Omega_t| >= pi b^2/64 for all large t, which contradicts (iv). Hence (-delta, 0) and (delta, 0) lie in different
components of {rho > 0}.
Step 13 (proof of (h)). Let rho be a profile and let f, h and q be as in (d), so that |h(X)| <= C_h (1 + |X|)^q with
0 <= q < 1 (for q < 0 use q = 0), and suppose that f is of kind (ii), with zero direction e_0 = e_1 or -e_1. Let v,
g and a_0 be as in Step 9(v), so that f = a_0 g^gamma with g = r v(th) >= 0 and grad g = v e_r + v' e_th on the
punctured plane.
(i) The velocity. By (d), A + M = I/gamma and l = 1/gamma, so by Step 9(ii) and (iii)
    V = X/gamma + W_2[f] + u,   |u(X)| <= C(1 + |X|)^q log(2 + |X|),   div V = 2/gamma > 1.
By (b), W_2[f] = grad-perp(r^k Q) with Q = c_I |P|^(k/gamma) on I; Q is continuous and vanishes in the direction e_0,
so r^k Q = c_I |f|^(k/gamma) = c_I |a_0|^(k/gamma) g^k on the plane, and W_2[f] = k c_I |a_0|^(k/gamma) g^gamma
grad-perp g on the punctured plane. For the zero direction e_1, s = 1 by Step 7, and G < 0 in (b)(ii) gives
|z + e_1/(2 gamma)| < 1/(2 gamma) with z = v e_r + v' e_th, hence |z| < 1/gamma; for the zero direction -e_1 the same
bound follows by applying this to f(-X), which replaces v by v(th + pi). So |grad g|^2 = v^2 + v'^2 < 1/gamma^2, and
since |a_0|^(1/gamma) = gamma/(k|c_I|),
    |W_2[f](X)| = gamma |grad g(X)| |f(X)| <= |f(X)|   (X != 0),   W_2[f](0) = 0.   (28.8)
(ii) Completeness. Let X(t) be a maximal solution of X' = V(X) whose interval of existence has a finite endpoint t_*.
On the part of that interval between 0 and t_*, |rho(X(t))| = e^t |rho(X(0))| <= B with
B = max(1, e^(t_*)) |rho(X(0))|, so |f(X(t))| <= B + C_h (1 + |X(t)|)^q, and (i) and (28.8) give
|V(X(t))| <= C_B (1 + |X(t)|) with C_B depending on B. By Gronwall's inequality |X(t)| stays bounded as t -> t_*,
which contradicts maximality. So the flow of V is complete.
(iii) A growth bound. For Lambda >= 1 let T_Lambda be the set of X with |f(X)| <= Lambda(1 + |X|)^q, let R_1 > 0, and
suppose that a forward orbit X(t), t >= 0, with rho(X(0)) > 0 stays in the union of T_Lambda and the closed disk of
radius R_1 about 0. On that union rho = f + h <= C'(1 + |X|)^q and, by (i) and (28.8),
|V(X) - X/gamma| <= C'(1 + |X|)^q log(2 + |X|), with C' depending on Lambda and R_1. Fix eps > 0 with
q(1/gamma + eps) < 1. Since q < 1, d|X(t)|/dt <= (1/gamma + eps)|X(t)| + C'' for t >= 0, so 1 + |X(t)| <= C'''
e^((1/gamma + eps)t), and
    e^t rho(X(0)) = rho(X(t)) <= C' C'''^q e^(q(1/gamma + eps)t)   for t >= 0,
which is false for large t.
(iv) The case a_0 < 0. Then f <= 0, and rho(X) > 0 gives -f(X) < h(X) <= C_h (1 + |X|)^q, so {rho > 0} lies in
T_Lambda with Lambda = max(1, C_h). For small delta > 0, rho(delta, 0) = delta^2 + O(delta^3) > 0, and the forward
orbit of (delta, 0), along which rho(X(t)) = e^t rho(delta, 0) > 0, stays in T_Lambda, which (iii) excludes.
(v) The case a_0 > 0. By (i) and (ii), l = 1/gamma > 1/2 and the flow is complete, so by (g) {rho > 0} has two
different components O_1 and O_2, containing (-delta, 0) and (delta, 0) for small delta > 0. Let Lambda = C_h + 1, and
for R_1 > 0 let Omega_+ be the set of X with |X| > R_1 and f(X) > Lambda(1 + |X|)^q. On Omega_+,
rho = f + h > (1 + |X|)^q > 0. We show below that Omega_+ is path connected for large R_1. Then Omega_+ lies in one
component of {rho > 0}, so one of O_1 and O_2, call it O, does not meet Omega_+. Each X in O with |X| > R_1 satisfies
f(X) <= Lambda(1 + |X|)^q and, since rho(X) > 0, f(X) > -h(X) >= -C_h (1 + |X|)^q; so O lies in the union of T_Lambda
and the closed disk of radius R_1. The forward orbit of a point of O stays in {rho > 0}, and being connected, in O,
which (iii) excludes. It remains to show that Omega_+ is path connected for large R_1. If e_0 = -e_1, then f(-X) is of
kind (ii) with zero direction e_1 by (b), and replacing f by f(-X) replaces Omega_+ by -Omega_+; so let e_0 = e_1.
Then I = (0, 2 pi) and s = 1 by (b), and G < 0 gives v' sin th > gamma(v^2 + v'^2) + v cos th > 0 for 0 < th <= pi/2
and for 3 pi/2 <= th < 2 pi. So v is increasing on (0, pi/2] and decreasing on [3 pi/2, 2 pi), and since v tends to
0 at both ends, for 0 < lambda < m_v, where m_v > 0 is the minimum of v on [pi/2, 3 pi/2], the set of th in (0, 2 pi)
with v(th) > lambda is an open interval containing [pi/2, 3 pi/2]. A point r e_r with r > R_1 and 0 < th < 2 pi lies
in Omega_+ if and only if v(th) > lambda(r) = r^(-1) (Lambda(1 + r)^q/a_0)^(1/gamma), and lambda(r) -> 0 as
r -> infinity because q < gamma. Choose R_1 with lambda(r) < m_v for r > R_1. Then each circle |X| = r > R_1 meets
Omega_+ in an arc containing -r e_1, and the ray {-r e_1 : r > R_1} lies in Omega_+, so Omega_+ is path connected.
(vi) Conclusion. Both cases are impossible, so f is not of kind (ii). The functions a(r + sigma x)^gamma with
a != 0 are of kind (ii) (Step 6), which gives the second assertion. By (d), f is stationary, so by (b), f = 0 or
f = F(e.X) != 0 as in (b)(i), and then (A + M)e = e/gamma by (d). If rho satisfies the Hessian bound, then f, which is
a limit at infinity of rho by (d), is not a nonzero F(e.X) by (c); so f = 0 and |rho| = |h| <= C_h (1 + |X|)^q.
Step 14 (limits F(e.X) in (h)). Let rho be a profile with this velocity law, let f, h and q be as in (d), with
f = F(e.X) != 0 and F as in Proposition 2.7(d), and suppose that q mu < 1, where mu = 2l - 1/gamma. Put S = A + M.
By (d), S is symmetric and Se = e/gamma; since M is traceless, tr S = tr A = 2l, so the unit vector e-perp orthogonal
to e satisfies S e-perp = mu e-perp, and X.SX <= kappa_S |X|^2 with kappa_S = max(1/gamma, mu).
By Step 9(ii) and (iii), V = SX + W_2[f] + u with |u(X)| <= C(1 + |X|)^q log(2 + |X|), and by Proposition 2.7(d),
W_2[f] = (e_1 e_2, -e_1^2) F(e.X), so |W_2[f]| <= |f|. Steps 13(ii)-(iv) then apply with X/gamma replaced by SX:
in (ii), |SX| <= C|X|; in (iii), |V(X) - SX| <= C'(1 + |X|)^q log(2 + |X|) on the union of T_Lambda and the disk,
d|X(t)|/dt = X(t).V(X(t))/|X(t)| <= (kappa_S + eps)|X(t)| + C'' where X(t) != 0, so that
1 + |X(t)| <= C''' e^((kappa_S + eps)t), and eps > 0 is chosen with q(kappa_S + eps) < 1, which is possible because
q/gamma < 1 and q mu < 1. So the flow of V is complete, the conclusion of Step 13(iii) holds, and, by the argument
of Step 13(iv), f <= 0, that is a_+ <= 0 and a_- <= 0, is impossible.
Now let also l > 1/2, and suppose that exactly one of a_+ and a_- is positive; replacing e by -e if necessary, let
a_+ > 0 >= a_-. Let Lambda = C_h + 1, c_+ = (Lambda/a_+)^(1/gamma), and choose R_1 > 0 with
c_+ (q/gamma)(1 + R_1)^(q/gamma - 1) < 1. Since f <= 0 where e.X <= 0, the set Omega_+ of the X with |X| > R_1 and
f(X) > Lambda(1 + |X|)^q is the set of the X with |X| > R_1 and e.X > c_+ (1 + |X|)^(q/gamma). For X in Omega_+ and
tau >= 0, |X + tau e| >= |X| because e.X > 0, and |X + tau e| <= |X| + tau, so
e.(X + tau e) - c_+ (1 + |X + tau e|)^(q/gamma) is at least e.X + tau - c_+ (1 + |X| + tau)^(q/gamma), which is
positive at tau = 0 and increasing in tau by the choice of R_1; hence the ray X + tau e, tau >= 0, lies in Omega_+.
For X and Y in Omega_+ and tau large, the segment from X + tau e to Y + tau e lies in Omega_+, since each of its
points Z satisfies e.Z >= tau, |Z| >= tau and |Z| <= max(|X|, |Y|) + tau, and q/gamma < 1. So Omega_+ is path
connected, and the argument of Step 13(v), with (g), which applies because l > 1/2 and the flow is complete, gives a
contradiction. Finally a|x|^gamma = F(e_1.X) with a_+ = a_- = a, so if f = a|x|^gamma != 0 and q mu < 1, then the
first part gives a > 0.
Step 15 (limits F(e.X) vanishing only on a line). Let rho, f, h, q, S, mu and u be as in Step 14, so that q mu < 1 and
the flow Phi_t of V is complete, and suppose that a_+ != 0 and a_- != 0. Put alpha = 1/gamma - 1/2 > 0, so that
beta = mu + alpha, and c_1 = min(|a_+|, |a_-|) > 0. We show that l > 5/12 leads to a contradiction, and that l > 1/4
does if rho is even in x and e = e_1 or -e_1. As in Step 12, each Phi_t is a C^1 diffeomorphism of the plane with
Jacobian determinant e^(2lt), and rho(Phi_t X) = e^t rho(X).
(i) Orbit bounds. Since |f(X)| >= c_1 |e.X|^gamma and |f| <= |rho| + |h|,
    |e.X| <= C(|rho(X)|^(1/gamma) + (1 + |X|)^(q/gamma)),   |f(X)| <= |rho(X)| + C_h (1 + |X|)^q.   (28.9)
Writing X = (e.X)e + (e-perp.X)e-perp, X.SX = mu|X|^2 + (1/gamma - mu)(e.X)^2 <= mu|X|^2 + |1/gamma - mu| |e.X| |X|,
and V = SX + W_2[f] + u with |W_2[f]| <= |f| by Step 14. With (28.9), |rho|^(1/gamma) <= 1 + |rho| and
q/gamma <= q this gives, for an orbit X(t) and where X(t) != 0,
    d|X(t)|/dt <= mu|X(t)| + C(1 + |rho(X(t))|) + C(1 + |X(t)|)^q log(2 + |X(t)|).
Suppose that beta > 0, which holds in both cases to be treated. Fix sigma > max(mu, 0) with q sigma < 1 and
D = beta - sigma(1 + alpha q) > 0. This is possible: if mu > 0, D tends to
beta - mu(1 + alpha q) = alpha(1 - q mu) > 0 as sigma decreases to mu, and if mu <= 0, D tends to beta > 0 as sigma
decreases to 0. Since q < 1 and sigma > mu, the last inequality gives
d|X(t)|/dt <= sigma|X(t)| + C_sigma(1 + |rho(X(t))|) where X(t) != 0. Put b_0 = 1 - q sigma > 0.
(ii) Thin sets at 0. We find d_1 > 0 and, for every T >= 0, a measurable set E_T in the square [-2d_1, 2d_1]^2 with
|E_T| >= 2d_1^2 e^(-b_0 T/2) and |rho| <= C e^(-b_0 T) on E_T. First let l > 5/12, so that beta > 1/3, and let
lambda = min(1/2, beta) > 1/3, the smallest eigenvalue of A. Write V = AX + N as in Step 12(i). The argument
of Step 12(i), with lambda in place of 1/2 and 2 lambda/3 in place of 1/3, gives r_0 in (0, 1) such that
Z_t = Phi_(-t)(P) satisfies |Z_t| <= C|P| e^(-lambda t) and |D_P Z_t| <= C e^(-lambda t) for |P| <= r_0 and t >= 0.
Then |N_1(Z_t)| <= C|P|^2 e^(-2 lambda t) and |D_P[N_1(Z_t)]| <= C|P| e^(-2 lambda t), and 2 lambda > 1/2, so, as
in Step 12(ii), the limit nu(P) = lim_(t -> infinity) e^(t/2) (Z_t)_1 exists uniformly on |P| <= r_0 together with the
first derivatives in P, nu is C^1, nu(P) = P_1 + O(|P|^2) and D nu(P) = (1, 0) + O(|P|). Since
|rho(Z) - Z_1^2| <= C|Z|^3 near 0,
    rho(P) = e^t rho(Z_t) = (e^(t/2) (Z_t)_1)^2 + O(|P|^3 e^((1 - 3 lambda)t)),
and lambda > 1/3 gives rho = nu^2 on |P| <= r_0. Decreasing r_0, the x-derivative of nu lies in [1/2, 2] on
|P| <= r_0. Choose d_1 in (0, r_0/3] with |nu(0, y)| <= d_1/2 for |y| <= d_1. For |y| <= d_1,
nu(-d_1, y) <= 0 <= nu(d_1, y), so nu(x(y), y) = 0 for some x(y) in [-d_1, d_1], and |nu(x, y)| <= 2|x - x(y)| for
|x| <= 2d_1. Let eps_T = d_1 e^(-b_0 T/2) and let E_T be the closed set of the (x, y) with |x| <= 2d_1, |y| <= d_1 and
|nu(x, y)| <= eps_T. For each such y it contains the interval |x - x(y)| <= eps_T/2, so
|E_T| >= 2d_1 eps_T = 2d_1^2 e^(-b_0 T/2) by Fubini's theorem, and 0 <= rho = nu^2 <= d_1^2 e^(-b_0 T) on E_T. Next
let rho be even in x, e = e_1 or -e_1, and l > 1/4, so that beta > 0. Let J_x(x, y) = (-x, y). The field
w(X) = J_x W_2(J_x X) is continuous, O(|X|^gamma), vanishes at 0 with derivative 0, and has div w = 0 and
curl w = -(curl W_2)(J_x X) = rho_x(J_x X) = -rho_x(X), since rho_x is odd in x; so w = W_2 by the uniqueness
in Proposition 2.7(a), and since J_x A = A J_x, V(J_x X) = J_x V(X). So V_1(0, y) = 0 and the y-axis is invariant. On
it f = F(0) = 0 and W_2[f] = 0, so |rho(0, y)| = |h(0, y)| <= C_h (1 + |y|)^q and, since S e_2 = mu e_2,
V_2(0, y) = mu y + u_2(0, y). For the orbit (0, y(t)) of (0, y_0) this gives d|y(t)|/dt <= sigma|y(t)| + C where
y(t) != 0, so |y(t)| <= e^(sigma t)(|y_0| + C/sigma), and
    e^t |rho(0, y_0)| = |rho(0, y(t))| <= C(1 + |y_0| + C/sigma)^q e^(q sigma t)   for t >= 0.
Since q sigma < 1, rho(0, y_0) = 0. As rho is C^3 and even in x, also rho_x(0, y) = 0, so rho(x, y) = x^2 c(x, y) with
c(x, y) = int_0^1 (1 - t) rho_xx(tx, y) dt, which is continuous with c(0, 0) = 1 by the jet. Choose d_1 > 0 with
|c| <= 2 on [-2d_1, 2d_1]^2 and let E_T = [-d_1 e^(-b_0 T/2), d_1 e^(-b_0 T/2)] x [-d_1, d_1]. Then
|E_T| = 4d_1^2 e^(-b_0 T/2) and |rho| <= 2d_1^2 e^(-b_0 T) on E_T.
(iii) The contradiction. Let T >= 0, P in E_T and X(t) = Phi_t(P). For 0 <= t <= T,
|rho(X(t))| = e^t |rho(P)| <= C e^(t - b_0 T) <= C e^(q sigma t), so by (i)
d|X(t)|/dt <= sigma|X(t)| + C(1 + e^(q sigma t)) where X(t) != 0, and since sigma > 0 and (1 - q)sigma > 0,
    |X(t)| <= e^(sigma t)(|P| + C int_0^t (e^(-sigma u) + e^(-(1 - q)sigma u)) du) <= K_0 e^(sigma t)   (0 <= t <= T),
with K_0 independent of T and P. At t = T, (28.9) gives
|e.X(T)| <= C(e^(q sigma T/gamma) + (1 + K_0 e^(sigma T))^(q/gamma)) <= C' e^(q sigma T/gamma), and
|e-perp.X(T)| <= K_0 e^(sigma T). So Phi_T(E_T) lies in a rectangle of area 4C'K_0 e^(sigma(1 + q/gamma)T). On the
other hand |Phi_T(E_T)| = e^(2lT) |E_T| >= 2d_1^2 e^((2l - b_0/2)T), and
    2l - b_0/2 - sigma(1 + q/gamma) = beta - sigma - q sigma(1/gamma - 1/2) = D > 0,
so the two bounds are incompatible for large T.
(iv) Conclusion. By Step 14, a_+ > 0 or a_- > 0, and both if l > 1/2; by (iii), a_+ = 0 or a_- = 0 if l > 5/12. So for
l > 1/2 no nonzero F(e.X) is possible, and f = 0 by Step 13(vi), so that |rho| = |h| <= C_h (1 + |X|)^q. If
5/12 < l <= 1/2, then mu <= 1 - 1/gamma < 1, so q mu < 1 for every 0 <= q < 1, and f = 0 or, replacing e by -e if
necessary, f = a(e.X)_+^gamma with a = a_+ > 0. For f = a|x|^gamma = F(e_1.X), a_+ = a_- = a, so with q mu < 1,
a != 0 is excluded if l > 5/12, or if rho is even in x and l > 1/4, and a < 0 is excluded by Step 14.
Step 16 (limits a(e.X)_+^gamma). Let rho, f, h, q, S, mu and u be as in Step 14, and suppose that 1/4 < l <= 1/2 and
that f = a(e.X)_+^gamma with a > 0, that is a_+ = a and a_- = 0. Then mu = 2l - 1/gamma <= 1 - 1/gamma < 1/gamma, so
q mu < 1, the flow Phi_t of V is complete by Step 14, and kappa_S = 1/gamma. Put alpha = 1/gamma - 1/2 > 0 and
mu_+ = max(mu, 0), so that beta = mu + alpha > 0, write X = s e + z e-perp with s = e.X and z = e-perp.X. We derive a
contradiction. As in Step 12, each Phi_t is a C^1 diffeomorphism of the plane with Jacobian determinant e^(2lt), and
rho(Phi_t X) = e^t rho(X).
(i) Exponents. As in Step 15(i), fix sigma in (mu_+, 1) with D = beta - sigma(1 + alpha q) > 0; this is possible since
q mu < 1 and beta > 0, and sigma < 1 is no restriction since mu < 1. Fix eta with
0 < eta < min(D/alpha, (1 - q)sigma), put omega = q sigma + eta, so that q sigma < omega < sigma < 1, and put
b = 1 - omega, b_0 = 1 - q sigma and theta = b_0/b > 1. Fix also p in (q, 1).
(ii) rho >= 0. If rho(X) < 0, then 0 <= f(X) < -h(X) <= C_h (1 + |X|)^q, so X lies in T_Lambda with
Lambda = max(1, C_h), and so does every point of its forward orbit, along which rho(X(t)) = e^t rho(X) < 0. The
argument of Step 13(iii), as carried over in Step 14, with |rho| in place of rho, then gives
e^t |rho(X)| <= C e^(q(kappa_S + eps)t) for t >= 0 with q(kappa_S + eps) < 1, which is false for large t. So rho >= 0.
(iii) rho vanishes beyond a curve. Let w = (1 + z^2)^(1/2) and, for L >= 1, let U_L be the open set of the X with
s < -L - w^p. Where s < 0, f = 0 and, by the formula for W_2[f] in Step 14, W_2[f] = 0, so V = SX + u; since S is
symmetric with Se = e/gamma and S e-perp = mu e-perp, along an orbit there ds/dt = s/gamma + e.u and
dz/dt = mu z + e-perp.u. Hence dw^p/dt = p w^(p - 2) z(mu z + e-perp.u) <= p mu_+ w^p + p|u|, and at a point of the
boundary of U_L, where s = -L - w^p,
    d(s + L + w^p)/dt <= -L/gamma - (1/gamma - p mu_+) w^p + (1 + p)|u|.
There |X| <= |s| + |z| <= L + 2w, so, with p_1 in (q, p) fixed,
|u| <= C(1 + |X|)^q log(2 + |X|) <= C((1 + L)^(p_1) + w^(p_1)). Since 1/gamma - p mu_+ > 0 and p_1 < p, the right side
is at most -L/gamma + C(1 + L)^(p_1) + C', which is negative for large L; fix such an L. Then no forward orbit leaves
U_L: at a first time of leaving, the function s + L + w^p of t would reach 0 from below, so its derivative there would
be >= 0. Since f = 0 on U_L, U_L lies in T_Lambda, so by (ii) and the conclusion of Step 13(iii), as carried over
in Step 14, rho = 0 on U_L.
(iv) Thin sets. Let Y_a = (delta, 0) with delta > 0 so small that rho(Y_a) > 0, choose r_1 in (0, 1) such that
rho > 0 on the closed disk B_a of radius r_1 about Y_a, and a point Y_b such that the closed disk B_b of radius r_1
about Y_b lies in U_L. Let H be the convex hull of B_a and B_b, C_H >= 1 a bound for |D^2 rho|/2 on H,
d_* = |Y_b - Y_a|, e_* = (Y_b - Y_a)/d_* and n_* a unit vector orthogonal to e_*. For |v| <= r_1/2 let
rho_v(tau) = rho(Y_a + v n_* + tau e_*), 0 <= tau <= d_*; the segment lies in H. Then rho_v(tau) > 0 for tau <= r_1/2
and rho_v(d_*) = 0, so there is a smallest tau_v with rho_v(tau_v) = 0, and tau_v > r_1/2. Since rho >= 0, rho has a
minimum at Y_a + v n_* + tau_v e_*, so grad rho vanishes there, and Taylor's formula gives
0 < rho_v(tau) <= C_H (tau_v - tau)^2 for 0 <= tau < tau_v. For 0 < xi <= r_1^2/4 let E(xi) be the set of the X in
H with 0 < rho(X) <= xi. It contains the points Y_a + v n_* + tau e_* with |v| <= r_1/2 and
tau_v - (xi/C_H)^(1/2) <= tau < tau_v, so by Fubini's theorem |E(xi)| >= r_1 (xi/C_H)^(1/2).
(v) Orbit bounds. Let T >= 0, let P in H with 0 < rho(P) <= e^(-bT), and let X(t) = Phi_t(P). Then
rho(X(t)) = e^t rho(P) > 0, so X(t) is not in U_L and s(t) >= -L - (1 + |X(t)|)^p, and for 0 <= t <= T,
rho(X(t)) <= e^(t - bT) <= e^(omega t). With f = rho - h, a s(t)_+^gamma = f(X(t)) <= rho(X(t)) + C_h (1 + |X(t)|)^q,
so that, as q/gamma < p and rho^(1/gamma) <= 1 + rho,
    |s(t)| <= C(1 + rho(X(t)) + (1 + |X(t)|)^p)   (t >= 0).
Since X.SX = mu|X|^2 + (1/gamma - mu)s^2 <= mu|X|^2 + |1/gamma - mu| |s| |X| and
|W_2[f]| <= f <= rho + C_h (1 + |X|)^q, where X(t) != 0,
    d|X(t)|/dt <= mu|X(t)| + C(1 + rho(X(t)) + (1 + |X(t)|)^p) + C(1 + |X(t)|)^q log(2 + |X(t)|),
and since p < 1 and sigma > mu, the right side is at most sigma|X(t)| + C_sigma (1 + e^(omega t)) for 0 <= t <= T. As
in Step 15(iii), since omega < sigma, |X(t)| <= K_0 e^(sigma t) for 0 <= t <= T, with K_0 independent of T and of P,
which lies in the compact set H. So if s(T) < 0, then f(X(T)) = 0 and
e^T rho(P) = h(X(T)) <= C_h (1 + K_0 e^(sigma T))^q, that is rho(P) <= C_1 e^(-b_0 T) with a constant
C_1 >= 1 independent of T and P; and if s(T) >= 0, then a s(T)^gamma <= e^(omega T) + C_h (1 + K_0 e^(sigma T))^q, so
that, as omega > q sigma, 0 <= s(T) <= C' e^(omega T/gamma). In both cases |z(T)| <= K_0 e^(sigma T).
(vi) A choice of thin sets. Let m(xi) = |E(xi)| for 0 < xi <= r_1^2/4 and c = r_1 C_H^(-1/2), so that
m(xi) >= c xi^(1/2) by (iv); m is nondecreasing, and m(xi) -> 0 as xi -> 0, since the sets E(xi) decrease to the empty
set. Let xi_* in (0, r_1^2/4] with C_1 xi^(theta - 1) <= 1/9 for xi <= xi_*. We show that there are arbitrarily small
xi in (0, xi_*] with m(xi) - m(C_1 xi^theta) >= (c/2) xi^(1/2). Otherwise there is xi_0 in (0, xi_*] such that this
fails for every xi in (0, xi_0]. Put xi_(k+1) = C_1 xi_k^theta for k >= 0; then xi_(k+1) <= xi_k/9, so xi_k decreases
to 0, xi_k^(1/2) <= 3^(-k) xi_0^(1/2), and m(xi_k) - m(xi_(k+1)) < (c/2) xi_k^(1/2) for every k. Summing over k,
m(xi_0) <= (c/2) (3/2) xi_0^(1/2) < c xi_0^(1/2), which contradicts (iv).
(vii) The contradiction. Let xi be as in (vi), put T = -(log xi)/b, so that xi = e^(-bT) and
C_1 xi^theta = C_1 e^(-b_0 T), and let E_T be the set of the X in H with C_1 e^(-b_0 T) < rho(X) <= e^(-bT). Then
|E_T| = m(xi) - m(C_1 xi^theta) >= (c/2) e^(-bT/2). For P in E_T, (v) applies and excludes s(T) < 0, so Phi_T(P) lies
in the rectangle 0 <= s <= C' e^(omega T/gamma), |z| <= K_0 e^(sigma T), of area 2C'K_0 e^((sigma + omega/gamma)T). On
the other hand |Phi_T(E_T)| = e^(2lT) |E_T| >= (c/2) e^((2l - b/2)T), and
    2l - b/2 - sigma - omega/gamma = beta - sigma - alpha omega = D - alpha eta > 0.
Since xi, and with it 1/T, can be taken arbitrarily small, the two bounds are incompatible.
(viii) Conclusion. For 1/4 < l <= 1/2, f = a(e.X)_+^gamma with a > 0 is impossible, and so, replacing e by -e and
with Step 14, if f != 0 then a_+ != 0, a_- != 0 and a_+ > 0 or a_- > 0. With Step 15(iv), f = 0, and so
|rho| = |h| <= C_h (1 + |X|)^q, if 5/12 < l <= 1/2, and hence, with Step 15(iv) for l > 1/2, for every l > 5/12 with
q(2l - 1/gamma) < 1.
Step 17 (two positive amplitudes). Let rho, f, h, q, S, mu, u and Phi_t be as in Step 15, so that a_+ != 0,
a_- != 0 and q mu < 1, and suppose that 1/4 < l <= 1/2, so that beta > 0 and mu <= 1 - 1/gamma < 1; let alpha, sigma,
D and b_0 be as in Step 15(i). We show that a_+ > 0 and a_- > 0 lead to a contradiction. All auxiliary constants and
sets of this step and the next are chosen anew.
(i) Zeros at which the gradient vanishes. Let Y be a point with rho(Y) = 0 and grad rho(Y) = 0; we show that V(Y) = 0.
Suppose that V(Y) != 0, let n_Y be a unit vector orthogonal to V(Y), and put Psi(t, v) = Phi_t(Y + v n_Y). Since V is
C^1, Psi is C^1, and its derivative at (0, 0) has the columns V(Y) and n_Y, so it is invertible. By the inverse
function theorem there are t_0 and v_0 in (0, 1] and j_0 > 0 such that Psi is injective on
Q_0 = [-t_0, t_0] x [-v_0, v_0] and |det D Psi| >= j_0 there. By Taylor's formula |rho(Y + v n_Y)| <= C_Y v^2 for
|v| <= v_0, so |rho(Psi(t, v))| = e^t |rho(Y + v n_Y)| <= e C_Y v^2 on Q_0. For T >= 0 let v_T = v_0 e^(-b_0 T/2) and
E_T = Psi([-t_0, t_0] x [-v_T, v_T]). These are compact subsets of Psi(Q_0),
|E_T| >= 4 j_0 t_0 v_T = 4 j_0 t_0 v_0 e^(-b_0 T/2) by the change of variables formula, and
|rho| <= e C_Y v_0^2 e^(-b_0 T) on E_T. Of the sets E_T of Step 15(ii), Step 15(iii) uses only that they lie in a
fixed bounded set, that |E_T| >= c e^(-b_0 T/2) with a constant c > 0, and that |rho| <= C e^(-b_0 T) on E_T, besides
a_+ != 0, a_- != 0, q mu < 1 and beta > 0. So it applies to the present sets and gives a contradiction. Hence
V(Y) = 0.
(ii) The zeros of rho. Now let a_+ > 0 and a_- > 0, so that f >= 0. The argument of Step 16(ii) uses only f >= 0 and
q kappa_S < 1, so rho >= 0. Every zero Y of rho is then a minimum of rho, so grad rho(Y) = 0 and, by (i), V(Y) = 0. By
Section 9.14, Step 3, W_2 is C^2 near 0 with W_2(0) = 0 and DW_2(0) = 0, so, for every l, V(X) = AX + N(X) with
|N(X)| <= C_V |X|^2 for |X| <= 1, as in Step 12(i); let lambda = min(1/2, beta) > 0, so that X.AX >= lambda|X|^2.
Choose r_2 in (0, 1] with C_V r_2 <= lambda/2; then X.V(X) >= (lambda/2)|X|^2 for |X| <= r_2. So V(X) != 0, and hence
rho(X) > 0, for 0 < |X| <= r_2. Let m_2 > 0 and M_2 be the minimum and the maximum of rho on the circle |X| = r_2.
(iii) The basin of 0. Let Omega_0 be the set of the X with Phi_(-t)(X) -> 0 as t -> infinity. For |X| <= r_2,
Z(t) = Phi_(-t)(X) satisfies d|Z(t)|^2/dt = -2Z(t).V(Z(t)) <= -lambda|Z(t)|^2 as long as |Z(t)| <= r_2, so
|Z(t)| <= e^(-lambda t/2)|X| for t >= 0, and the closed disk |X| <= r_2 lies in Omega_0. The set Omega_0 is invariant
under the flow, and it is open: if X is in Omega_0, then |Phi_(-t_1)(X)| < r_2 for some t_1, and by the continuity of
Phi_(-t_1) the same holds near X. For X in Omega_0 with |X| > r_2 let tau(X) be the first t > 0 with
|Phi_(-t)(X)| = r_2, and P(X) = Phi_(-tau(X))(X); then X = Phi_(tau(X))(P(X)), |P(X)| = r_2 and
rho(X) = e^(tau(X)) rho(P(X)) >= m_2 e^(tau(X)). The set Omega_0 is also closed. Let X_j in Omega_0 tend to X. If
|X| <= r_2, X lies in Omega_0. Otherwise |X_j| > r_2 for large j, and the tau(X_j) are bounded, since
m_2 e^(tau(X_j)) <= rho(X_j) -> rho(X); so along a subsequence tau(X_j) -> tau and P(X_j) -> P with |P| = r_2, and
X = Phi_tau(P) by the continuity of (t, X) -> Phi_t(X). As P lies in Omega_0, so does X. Hence Omega_0 is the whole
plane.
(iv) A growth bound and the contradiction. Fix sigma_1 in (mu_+, 1), where mu_+ = max(mu, 0). For |P| = r_2 and
X(t) = Phi_t(P), t >= 0, rho(X(t)) = e^t rho(P) lies in [m_2 e^t, M_2 e^t], so X(t) != 0, and the first inequality for
d|X(t)|/dt in Step 15(i) gives, since q < 1 and sigma_1 > mu, d|X(t)|/dt <= sigma_1 |X(t)| + C(1 + M_2 e^t). Hence
    |X(t)| <= e^(sigma_1 t)(r_2 + C int_0^t e^(-sigma_1 u)(1 + M_2 e^u) du) <= K_3 e^t   (t >= 0),
with K_3 = r_2 + C/sigma_1 + C M_2/(1 - sigma_1). For |X| > r_2, (iii) gives X = Phi_(tau(X))(P(X)), so
|X| <= K_3 e^(tau(X)) <= (K_3/m_2) rho(X). Thus |X| <= r_2 + (K_3/m_2) rho(X) on the whole plane. On the line e.X = 0,
f = F(0) = 0, so rho = h and |X| <= r_2 + (K_3/m_2) C_h (1 + |X|)^q, which is false for large |X| since q < 1.
(v) Conclusion. For 1/4 < l <= 1/2, a_+ > 0 and a_- > 0 are impossible together. So, with Steps 14 and 16(viii), a
nonzero F(e.X) with q mu < 1 and 1/4 < l <= 1/2 has a_+ a_- < 0, and for l > 1/2 there is none, by Step 15(iv). For
f = a|x|^gamma = F(e_1.X), a_+ = a_- = a, so for every l > 1/4 with q mu < 1, a < 0 is excluded by Step 14 and
a > 0 by (iv) and Step 15(iv), also if rho is not even in x.
Step 18 (limits a(e.X)_+^gamma for 1/6 <= l <= 1/4). Let rho, f, h, q, S, mu and u be as in Step 14, and suppose that
1/6 <= l <= 1/4 and that f = a(e.X)_+^gamma with a > 0. Then mu = 2l - 1/gamma <= 1/2 - 1/gamma < 0, so q mu < 1,
kappa_S = 1/gamma and mu_+ = 0; the flow Phi_t of V is complete by Step 14, each Phi_t has Jacobian determinant
e^(2lt), and rho(Phi_t X) = e^t rho(X). We use s, z and w as in Step 16, fix p in (q, 1), and derive a contradiction.
(i) Parts (ii)-(iv) of Step 16. Their arguments use only Step 14, f = a(e.X)_+^gamma with a > 0, q kappa_S < 1,
1/gamma - p mu_+ > 0 and the jet of rho, and neither l > 1/4 nor the exponents of Step 16(i). So rho >= 0, rho = 0 on
U_L for some L >= 1, and we have Y_a, r_1, B_a, B_b, H, d_*, e_*, n_* and rho_v as in Step 16(iv). Let m_1 > 0 be the
minimum of rho on B_a. For |v| <= r_1/2, rho_v >= m_1 on [0, r_1/2] and rho_v = 0 on [d_* - r_1/2, d_*], since these
points lie within 2^(-1/2) r_1 of Y_a and of Y_b respectively.
(ii) Thin sets next to the zero region. Fix v with |v| <= r_1/2 and write g = rho_v, a nonnegative C^3 function
on [0, d_*], since rho is C^3. Let Z_v be the set of the zeros of g. At each point of Z_v, g' = 0, since g >= 0 and
g vanishes near d_*. The points of Z_v at which g'' != 0 are isolated points of Z_v, so there are only countably many
of them; at a point of Z_v in (0, d_*) at which g'' = 0, also g''' = 0, since otherwise g would change sign there; and
g''' = 0 at d_*, while 0 is not in Z_v. Hence g', g'' and g''' vanish on Z_v except on a countable set. For
0 < xi < m_1 let t_v = t_v(xi) be the largest tau in [0, d_*] with g(tau) = xi; then r_1/2 < t_v < d_* - r_1/2 and
0 <= g <= xi on [t_v, d_*]. Let N_v(tau) be the length of the set of the u in [tau, d_*] with g(u) > 0; N_v is
Lipschitz, N_v(d_*) = 0, and N_v' = -1 almost everywhere on the set where g > 0 and N_v' = 0 almost everywhere on Z_v,
so that, for j = 0, 1, 2, the integral of N_v^j over the part of [tau, d_*] where g > 0 is N_v(tau)^(j+1)/(j+1). Let
c_3(xi) be the supremum of |rho_v'''(tau)| over |v| <= r_1/2 and t_v(xi) <= tau <= d_*. Integrating g''', g'' and g'
from tau to d_*, where g, g' and g'' vanish, only the part where g > 0 contributes, and successively
    |g''(tau)| <= c_3(xi) N_v(tau),   |g'(tau)| <= c_3(xi) N_v(tau)^2/2,   g(tau) <= c_3(xi) N_v(tau)^3/6
for t_v <= tau <= d_*. At tau = t_v this gives c_3(xi) > 0 and N_v(t_v) >= (6 xi/c_3(xi))^(1/3), and since g <= xi
on [t_v, d_*], N_v(t_v) is the length of the set of the u in [t_v, d_*] with 0 < g(u) <= xi.
(iii) c_3(xi) -> 0 as xi -> 0. If xi' < xi < m_1, then t_v(xi') > t_v(xi), since g(t_v(xi)) = xi > xi' and g(d_*) = 0;
so c_3 is nondecreasing. If c_3(xi) did not tend to 0, there would be xi_j -> 0, v_j and tau_j in [t_(v_j)(xi_j), d_*]
with |rho_(v_j)'''(tau_j)| bounded below by a positive constant, and along a subsequence v_j -> v_*, tau_j -> tau_*
and t_(v_j)(xi_j) -> b_*, with b_* <= tau_* and b_* <= d_* - r_1/2. For every tau in (b_*, d_*], tau > t_(v_j)(xi_j)
for large j, so 0 <= rho_(v_j)(tau) <= xi_j, and in the limit rho_(v_*)(tau) = 0. So rho_(v_*) = 0 on [b_*, d_*], an
interval of positive length, and rho_(v_*)''' = 0 there by continuity, in particular at tau_*; but by the continuity
of D^3 rho, |rho_(v_*)'''(tau_*)| = lim |rho_(v_j)'''(tau_j)| > 0, a contradiction.
(iv) The measure of the thin sets. Let E(xi) be the set of the X in H with 0 < rho(X) <= xi, as in Step 16(iv). For
0 < xi < m_1 and |v| <= r_1/2, by (ii) the points Y_a + v n_* + tau e_* of E(xi) form a set of length
at least (6 xi/c_3(xi))^(1/3), so by Fubini's theorem
    |E(xi)| >= k_3(xi) xi^(1/3),   k_3(xi) = r_1 (6/c_3(xi))^(1/3),
and k_3(xi) -> infinity as xi -> 0 by (iii).
(v) Bounded orbits and the contradiction. Let T >= 0 with e^(-T) < m_1, let P in E(e^(-T)) and X(t) = Phi_t(P). For
0 <= t <= T, 0 < rho(X(t)) = e^t rho(P) <= 1, so X(t) != 0 and X(t) is not in U_L, so that
s(t) >= -L - (1 + |X(t)|)^p, and as(t)_+^gamma = f(X(t)) <= 1 + C_h (1 + |X(t)|)^q; as q/gamma < p,
|s(t)| <= C(1 + |X(t)|)^p. Since X.SX = mu|X|^2 + (1/gamma - mu)s^2 <= mu|X|^2 + (1/gamma - mu)|s| |X|,
|W_2[f]| <= f <= 1 + C_h (1 + |X|)^q on the orbit and |u| <= C(1 + |X|)^q log(2 + |X|),
    d|X(t)|/dt <= mu|X(t)| + C(1 + |X(t)|)^p + C(1 + |X(t)|)^q log(2 + |X(t)|)   (0 <= t <= T).
Since mu < 0 and p, q < 1, the right side is negative for |X(t)| >= R_2, with R_2 independent of T and P, so
|X(t)| <= R_3 = max(R_2, max_H |X|) for 0 <= t <= T. Hence Phi_T(E(e^(-T))) lies in the disk of radius R_3 about 0,
and by (iv), as 2l >= 1/3,
    pi R_3^2 >= e^(2lT) |E(e^(-T))| >= k_3(e^(-T)) e^((2l - 1/3)T) >= k_3(e^(-T)),
which tends to infinity as T -> infinity, a contradiction.
(vi) Conclusion. For 1/6 <= l <= 1/4, f = a(e.X)_+^gamma with a > 0 is impossible, and so, replacing e by -e and
with Step 14, if f != 0 then a_+ != 0, a_- != 0, and a_+ > 0 or a_- > 0. With Step 16(viii) and, for l > 1/2, Step 14,
this holds for every l >= 1/6 with q(2l - 1/gamma) < 1.
Step 19 (limits a(e.X)_+^gamma for C^m profiles). Let m >= 3 be an integer, let rho, f, h, q, S, mu and u be as
in Step 14, and suppose that rho is C^m, that 1/(2m) <= l <= 1/4 and that f = a(e.X)_+^gamma with a > 0. For
m = 3 this is Step 18; we derive a contradiction for every m >= 3. Since l <= 1/4, mu = 2l - 1/gamma < 0, q mu < 1,
kappa_S = 1/gamma and mu_+ = 0 as in Step 18, and Step 18(i), and Step 18(v) up to the conclusion that
Phi_T(E(e^(-T))) lies in the disk of radius R_3 about 0, use only these facts besides the hypotheses of Step 14 and
a > 0, not l >= 1/6. So they hold here: rho >= 0, rho = 0 on U_L for some L >= 1, and we have Y_a, r_1, B_a, B_b, H,
d_*, e_*, n_*, rho_v and m_1 as in Step 18(i), the sets E(xi) of Step 18(iv), and the radius R_3 of Step 18(v), such
that Phi_T(E(e^(-T))) lies in the disk of radius R_3 about 0 for every T >= 0 with e^(-T) < m_1. We
replace Step 18(ii)-(iv) and the rest of Step 18(v), which uses 2l >= 1/3.
(i) Zeros of g. Fix v with |v| <= r_1/2 and write g = rho_v, a nonnegative C^m function on [0, d_*], and let Z_v be
the set of its zeros. Let tau_0 be a point of Z_v that is not an isolated point of Z_v. Then g^(j)(tau_0) = 0 for
j = 1, ..., m, with one-sided derivatives at d_*: otherwise let j <= m be the least index with g^(j)(tau_0) != 0; by
Taylor's formula g(tau) = g^(j)(tau_0)(tau - tau_0)^j/j! + o(|tau - tau_0|^j) as tau -> tau_0, so g(tau) != 0 for
tau != tau_0 close to tau_0, and tau_0 would be isolated. The point d_* is not isolated in Z_v, since
g = 0 on [d_* - r_1/2, d_*], and 0 is not in Z_v. The isolated points of Z_v are countably many, so g', ..., g^(m)
vanish on Z_v except on a countable set.
(ii) Thin sets. For 0 < xi < m_1 let t_v = t_v(xi) and N_v be as in Step 18(ii); the identity of Step 18(ii) for the
integral of N_v^j over the part of [tau, d_*] where g > 0 holds, with the same proof, for every integer j >= 0. Let
c_m(xi) be the supremum of |rho_v^(m)(tau)| over |v| <= r_1/2 and t_v(xi) <= tau <= d_*. For i = 1, ..., m and
t_v <= tau <= d_*, g^(m - i)(tau) is minus the integral of g^(m - i + 1) over [tau, d_*], since
g^(m - i)(d_*) = 0 by (i), and by (i) only the part of [tau, d_*] where g > 0 contributes; by induction on i, with
that identity,
    |g^(m - i)(tau)| <= c_m(xi) N_v(tau)^i/i!   (t_v <= tau <= d_*, i = 1, ..., m),
in particular g(tau) <= c_m(xi) N_v(tau)^m/m!. At tau = t_v this gives c_m(xi) > 0 and
N_v(t_v) >= (m! xi/c_m(xi))^(1/m), and, as in Step 18(ii), N_v(t_v) is the length of the set of the u in [t_v, d_*]
with 0 < g(u) <= xi.
(iii) c_m(xi) -> 0 as xi -> 0. The argument of Step 18(iii) applies with the third derivatives of the rho_v replaced
by their m-th derivatives and the continuity of D^3 rho by that of D^m rho.
(iv) The contradiction. As in Step 18(iv), by (ii) and Fubini's theorem
    |E(xi)| >= kappa_m(xi) xi^(1/m),   kappa_m(xi) = r_1 (m!/c_m(xi))^(1/m),
for 0 < xi < m_1, and kappa_m(xi) -> infinity as xi -> 0 by (iii). For T >= 0 with e^(-T) < m_1, Phi_T(E(e^(-T))) lies
in the disk of radius R_3 about 0, so, as 2l >= 1/m,
    pi R_3^2 >= e^(2lT) |E(e^(-T))| >= kappa_m(e^(-T)) e^((2l - 1/m)T) >= kappa_m(e^(-T)),
which tends to infinity as T -> infinity, a contradiction.
(v) Conclusion. If rho is C^m for an integer m >= 3 and 1/(2m) <= l <= 1/4, then f = a(e.X)_+^gamma with a > 0 is
impossible, and so, replacing e by -e and with Step 14, if f != 0 then a_+ != 0, a_- != 0, and a_+ > 0 or a_- > 0.
With Step 18(vi) this holds for every l >= 1/(2m) with q(2l - 1/gamma) < 1, and if rho is C^infinity, for every
l > 0 with q(2l - 1/gamma) < 1, taking m >= max(3, 1/(2l)).
Step 20 (the case l = 1/4). Let rho, f, h, q, S, mu, u and Phi_t be as in Step 15, so that a_+ != 0, a_- != 0,
q mu < 1 and the flow is complete, and suppose that l = 1/4. Then beta = 0, mu = 1/2 - 1/gamma < 0, kappa_S = 1/gamma,
and each Phi_t has Jacobian determinant e^(t/2). We show that a_+ > 0 and a_- > 0 lead to a contradiction; Step 17
does not apply, since it uses beta > 0. All auxiliary constants and sets of this step are chosen anew.
(i) An absorbing disk. By the first inequality for d|X(t)|/dt in Step 15(i) there is a constant C such that every
orbit satisfies d|X(t)|/dt <= mu|X(t)| + C(1 + |rho(X(t))|) + C(1 + |X(t)|)^q log(2 + |X(t)|) where X(t) != 0. Since
mu < 0 and q < 1, there is R_* >= 1 with 2C + C(1 + r)^q log(2 + r) <= |mu| r/2 for r >= R_*. Let P be a point and
T >= 0 with |rho(Phi_t(P))| <= 1 for 0 <= t <= T, and let X(t) = Phi_t(P). Then d|X(t)|/dt <= -|mu| |X(t)|/2 at every
t in [0, T] with |X(t)| >= R_*. So if |X(t)| > R_* for some t in [0, T], then |X(u)| > R_* for 0 <= u <= t, since at
the last u in [0, t] with |X(u)| <= R_* the function |X| would equal R_*, have a negative derivative, and be larger
than R_* just after u; and then |X(t)| <= |P| e^(-|mu| t/2). Hence
    |Phi_t(P)| <= max(R_*, |P| e^(-|mu| t/2))   (0 <= t <= T).
In particular, for every compact set K there is T_K >= 0 such that |Phi_T(P)| <= R_* whenever T >= T_K, P lies in
K and |rho(P)| <= e^(-T), since then |rho(Phi_t(P))| = e^t |rho(P)| <= 1 for 0 <= t <= T.
(ii) Zeros at which the gradient vanishes. Let Y be a point with rho(Y) = 0 and grad rho(Y) = 0; we show that
V(Y) = 0. Suppose that V(Y) != 0. The orbit of Y is not periodic: otherwise it would be a Jordan curve J with
Phi_t(J) = J for all t, so each Phi_t, a homeomorphism of the plane, would map the bounded complementary component
D of J onto itself, which is false for t != 0 since |Phi_t(D)| = e^(t/2) |D| and 0 < |D| < infinity. So t -> Phi_t(Y)
is injective. Let n_Y be a unit vector orthogonal to V(Y) and Psi(t, v) = Phi_t(Y + v n_Y). Since
d Phi_t(P)/dt = V(Phi_t(P)) = D Phi_t(P) V(P), Psi is C^1 with
    det D Psi(t, v) = e^(t/2) det(V(Y + v n_Y), n_Y).
Choose v_0 in (0, 1] and j_0 > 0 with |det(V(Y + v n_Y), n_Y)| >= j_0 for |v| <= v_0, and C_Y with
|rho(Y + v n_Y)| <= C_Y v^2 for |v| <= v_0, by Taylor's formula, and fix delta in (0, v_0] with C_Y delta^2 <= 1. Now
fix L > 0. There is eps_L in (0, v_0] such that Psi is injective on Q_L = [0, L] x [-eps_L, eps_L]: otherwise there
are pairs (t_j, v_j) != (t'_j, v'_j) in [0, L] x [-1/j, 1/j] with Psi(t_j, v_j) = Psi(t'_j, v'_j), along a subsequence
t_j -> t and t'_j -> t', so Phi_t(Y) = Phi_(t')(Y) and t = t', and since det D Psi(t, 0) != 0, Psi is injective
near (t, 0) by the inverse function theorem, which is false for large j. For T >= 0 with delta e^(-T/2) <= eps_L let
G_T be the set of the (t, v) with 0 <= t <= L and |v| <= delta e^(-(T + t)/2), and E_T = Psi(G_T), a compact subset of
K_L = Psi(Q_L). On E_T, |rho(Psi(t, v))| = e^t |rho(Y + v n_Y)| <= e^t C_Y delta^2 e^(-(T + t)) <= e^(-T), and by the
change of variables formula
    |E_T| >= int_0^L 2 delta e^(-(T + t)/2) e^(t/2) j_0 dt = 2 j_0 delta L e^(-T/2).
By (i), Phi_T(E_T) lies in the disk of radius R_* about 0 for T >= T_(K_L), so that pi R_*^2 >= e^(T/2) |E_T| >= 2 j_0
delta L. Since R_*, j_0 and delta do not depend on L, this is false for large L. Hence V(Y) = 0.
(iii) Two positive amplitudes. Let a_+ > 0 and a_- > 0, so that f >= 0. As in Step 17(ii), rho >= 0, so every zero of
rho is a minimum of rho, at which grad rho vanishes, and hence, by (ii), a zero of V. The zeros of V are bounded: if
V(Y) = 0, then rho(Y) = V(Y).grad rho(Y) = 0, so |f(Y)| = |h(Y)| <= C_h (1 + |Y|)^q, and SY = -W_2[f](Y) - u(Y) with
|W_2[f]| <= |f|; since S is symmetric with the eigenvalues 1/gamma and mu, both different from 0,
min(1/gamma, |mu|) |Y| <= C(1 + |Y|)^q log(2 + |Y|), so |Y| <= R_0 for a constant R_0. So the zero set of rho is
compact. Let R > R_0, let m_0 > 0 be the minimum of rho on the circle |X| = R, and fix c in (0, m_0). The set L_c of
the X with |X| < R and rho(X) = c is compact, since rho > c on the circle, and not empty, since rho(0) = 0 < c < rho
on the circle. On L_c, grad rho != 0, since c = rho = V.grad rho there. So L_c is a compact one-dimensional C^1
submanifold of the plane, and a component J of L_c is a C^1 Jordan curve. Let D be its bounded complementary
component. On J, rho = c, and rho is not constant on D, since otherwise grad rho = 0, and so rho = 0, on D, while
rho = c on the boundary J of D; so rho has a maximum larger than c or a minimum smaller than c over the compact set
D union J, attained at a point Y of D, where grad rho(Y) = 0 and so rho(Y) = 0. As shown above, Y is then a zero of V,
so Phi_t(Y) = Y for every t; let s_Y = |e.Y|. For P in J and X(t) = Phi_t(P), rho(X(t)) = c e^t; fix
sigma_1 in (0, 1). As in Step 17(iv), the first inequality for d|X(t)|/dt in Step 15(i) gives
d|X(t)|/dt <= sigma_1 |X(t)| + C(1 + c e^t), and so |X(t)| <= K_1 e^t for t >= 0, with K_1 independent of P in J. So
|h(X(t))| <= C_h (1 + K_1 e^t)^q <= c e^t/2 for t >= t_1, with t_1 independent of P, and then
f(X(t)) = rho(X(t)) - h(X(t)) >= c e^t/2. As f(X) <= max(a_+, a_-) |e.X|^gamma,
|e.X(t)| >= (c e^t/(2 max(a_+, a_-)))^(1/gamma) for t >= t_1. Choose
t >= t_1 with (c e^t/(2 max(a_+, a_-)))^(1/gamma) > s_Y. Then Phi_t(J), being connected, lies in one of the
half-planes {e.X > s_Y} and {e.X < -s_Y}. Phi_t(D) is the bounded complementary component of the Jordan curve
Phi_t(J), and the complement of that half-plane is connected, unbounded and does not meet Phi_t(J), so Phi_t(D) lies
in the same half-plane. But Y = Phi_t(Y) lies in Phi_t(D) and |e.Y| = s_Y, a contradiction.
(iv) Conclusion. For l = 1/4, a_+ > 0 and a_- > 0 are impossible together. So, with Steps 14 and 18(vi), a nonzero
F(e.X) with l = 1/4 has a_+ a_- < 0, and, with Step 17(v), a nonzero F(e.X) with q mu < 1 has a_+ a_- < 0 for every
l >= 1/4. For f = a|x|^gamma, a_+ = a_- = a, so for every l >= 1/4 with q mu < 1, a < 0 is excluded by Step 14 and
a > 0 by (iii) and Step 17(v).
Step 21 (C^m profiles for 1/4 < l <= 5/12). Let m >= 3 be an integer, let rho, f, h, q, S, mu and u be as in Step 14,
and suppose that rho is C^m and 1/4 < l <= 5/12. Then mu <= 5/6 - 1/gamma < 1/3, so q mu < 1 for every 0 <= q < 1, and
a_+ a_- < 0 by Step 17(v), so that Step 15 applies; replacing e by -e if necessary, let a_+ > 0 > a_-. Put
p_* = 1/beta = 1/(2l - 1/2), so that p_* >= 3. We show that p_* > m or p_* is an odd integer. All auxiliary constants
and sets of this step are chosen anew.
(i) The minimum of rho across the x-direction. Since rho is C^m, rho_x(0) = 0 and rho_xx(0) = 2, there are r_3 and r_4
in (0, 1/2] such that rho_xx >= 1 on Q = [-r_4, r_4] x [-r_3, r_3] and rho_x(-r_4, y) < 0 < rho_x(r_4, y) for
|y| <= r_3. So for |y| <= r_3 there is exactly one chi(y) in (-r_4, r_4) with rho_x(chi(y), y) = 0; by the implicit
function theorem chi is C^(m - 1), and chi(0) = 0. Let C_chi be a bound for |chi'|, so that |chi(y)| <= C_chi |y|, and
put X_y = (chi(y), y) and phi(y) = rho(X_y). Then phi'(y) = rho_x(X_y) chi'(y) + rho_y(X_y) = rho_y(X_y), which is
C^(m - 1), so phi is C^m, and phi(0) = 0. By Taylor's formula in x,
    rho(x, y) = phi(y) + c(x, y)(x - chi(y))^2,
    c(x, y) = int_0^1 (1 - t) rho_xx(chi(y) + t(x - chi(y)), y) dt >= 1/2,
on Q. In particular rho(x, 0) >= x^2/2 for |x| <= r_4.
(ii) The equation for phi. At X_y, grad rho = (0, phi'(y)), so the profile equation gives phi(y) = b(y) phi'(y) with
the continuous function b(y) = V_2(X_y). Write V(X) = AX + N(X) with |N(X)| <= C_V |X|^2 for |X| <= 1 as
in Step 17(ii); then |b(y) - beta y| <= C_2 y^2 with C_2 = C_V (1 + C_chi)^2. Choose r_5 in (0, r_3] with
C_2 r_5 <= beta/2. For 0 < |y| <= r_5, b(y) has the sign of y and |b(y)| >= beta |y|/2, so eta_b(y) = 1/b(y) - p_*/y
satisfies |eta_b(y)| <= 2C_2/beta^2. Solving the linear equation
phi' = (p_*/y + eta_b(y)) phi on (0, r_5] and on [-r_5, 0) gives constants C_+ and C_- with
    phi(y) = C_+ y^(p_*) exp(int_0^y eta_b(u) du)   (0 < y <= r_5),
    phi(y) = C_- |y|^(p_*) exp(-int_y^0 eta_b(u) du)   (-r_5 <= y < 0).
So phi has the sign of C_+ on (0, r_5] and that of C_- on [-r_5, 0), and phi(y) |y|^(-p_*) tends to C_+ as y decreases
to 0 and to C_- as y increases to 0. Let lambda = min(1/2, beta) > 0 and choose r_2 in (0, min(r_4, r_5)] with
C_V r_2 <= lambda/2; then, as in Step 17(ii), X.V(X) >= (lambda/2) |X|^2 for |X| <= r_2, so V(X) != 0 for
0 < |X| <= r_2.
(iii) C_+ != 0 and C_- != 0. If C_+ = 0, then for 0 < y <= r_5, rho(X_y) = phi(y) = 0, rho_x(X_y) = 0 and
rho_y(X_y) = phi'(y) = 0, so V(X_y) = 0 by Step 17(i), which applies since 1/4 < l <= 1/2, a_+ != 0, a_- != 0 and
q mu < 1. But X_y != 0 and |X_y| <= (1 + C_chi) |y|, so this contradicts (ii) for small y. Similarly C_- != 0.
(iv) C_+ and C_- are not both positive. Otherwise phi > 0 on [-r_5, r_5] except at 0, so by (i)
rho > 0 on [-r_4, r_4] x [-r_5, r_5] except at 0, and in particular rho(X) > 0 for 0 < |X| <= r_2. Let m_2 > 0 be the
minimum of rho on the circle |X| = r_2. Step 17(iii) uses only these facts and X.V(X) >= (lambda/2) |X|^2 for
|X| <= r_2, so its basin Omega_0 is the whole plane and rho(X) >= m_2 e^(tau(X)) > 0 for |X| > r_2. So rho > 0 on the
plane except at 0. But f(-s e) = a_- s^gamma for s > 0, so rho(-s e) <= a_- s^gamma + C_h (1 + s)^q < 0 for large s,
since a_- < 0 and q < gamma.
(v) C_+ and C_- are not both negative. First, {rho > 0} is connected. Let Lambda = C_h + 1, and for R_1 > 0 let
Omega_+ be the set of the X with |X| > R_1 and f(X) > Lambda(1 + |X|)^q, on which rho = f + h > 0. The proof
in Step 14 that Omega_+ is path connected for large R_1 uses only a_+ > 0 >= a_- and q/gamma < 1, not l > 1/2; fix
such an R_1. If a component O of {rho > 0} did not meet Omega_+, then, as in Step 13(v), O would lie in the union of
T_Lambda and the closed disk of radius R_1, and the forward orbit of a point of O would stay in O, which the
conclusion of Step 13(iii), as carried over in Step 14, excludes. So every component of {rho > 0} meets the connected
set Omega_+, which lies in one of them; hence {rho > 0} is connected. Now suppose that C_+ < 0 and C_- < 0, and let
0 < delta <= r_4. By (i), rho(x, 0) > 0 for 0 < |x| <= delta, and rho(0) = 0, so the construction of Step 12(iii),
which uses only these facts and the connectedness of {rho > 0}, gives delta' in (0, delta), a simple polygonal arc
Gamma in {rho > 0} from (-delta', 0) to (delta', 0) whose other points lie outside the closed disk B' of radius delta'
about 0, the Jordan curve J = ell union Gamma with ell = [-delta', delta'] x {0}, and its bounded complementary
component Omega. On J, rho >= 0. The open half-disks B'_+ and B'_- of the X = (x, y) with |X| < delta' and y > 0,
respectively y < 0, are connected and do not meet J, so each lies in Omega or in the unbounded complementary
component. By the Jordan curve theorem the point 0 of J is a boundary point of Omega, and the open disk of radius
delta' about 0 meets the complement of J only in B'_+ union B'_-, so Omega contains B'_+ or B'_-. For 0 < |y| <= r_5
with (1 + C_chi) |y| < delta', X_y lies in B'_+ if y > 0 and in B'_- if y < 0, and rho(X_y) = phi(y) < 0. So rho takes
negative values in Omega, and its minimum over the compact set Omega union J is negative and, since rho >= 0 on J,
attained at a point Y of Omega. Then grad rho(Y) = 0, and rho(Y) = V(Y).grad rho(Y) = 0, a contradiction. Hence
C_+ C_- < 0.
(vi) The order of phi at 0. Suppose that p_* <= m. If phi^(j)(0) = 0 for j = 0, ..., m, then phi(y) = o(|y|^m) by
Taylor's formula, so phi(y) |y|^(-p_*) -> 0 as y -> 0, which contradicts (ii) and (iii). Otherwise let n <= m be the
least j with phi^(j)(0) != 0. Then phi(y) y^(-n) -> phi^(n)(0)/n! != 0 as y -> 0, and the comparison with (ii)
and (iii) gives n = p_*; so p_* is an integer, C_+ = phi^(n)(0)/n! and C_- = (-1)^n phi^(n)(0)/n!, and
C_+ C_- < 0 by (v) gives that n is odd.
(vii) Conclusion. If rho is C^m for an integer m >= 3, 1/4 < l <= 5/12 and f != 0, then p_* > m or p_* is an odd
integer, that is, l < 1/4 + 1/(2m), or l = 1/4 + 1/(2n) with an odd integer n, 3 <= n <= m. For m = 3 this is no
restriction; for m = 4 it excludes 3/8 <= l < 5/12. If rho is C^infinity, a nonzero F(e.X) is therefore possible for
1/4 < l <= 5/12 only if l = 1/4 + 1/(2n) with n = 3, 5, 7, ...; so, with Steps 13(vi) and 16(viii), f = 0, and hence
|rho| = |h| <= C_h (1 + |X|)^q, for every other l > 1/4 with q(2l - 1/gamma) < 1.
Step 22 (the mixed case at l = 1/4). Let rho, f, h, q, S, mu, u and Phi_t be as in Step 20, so that l = 1/4, a_+ != 0,
a_- != 0, q mu < 1, the flow is complete and div V = 1/2, and suppose that a_+ a_- < 0; replacing e by -e if
necessary, let a_+ > 0 > a_-. We derive a contradiction. By Section 9.14, Step 3, V is C^2 on the plane, and
by Step 20(ii) every zero Y of rho with grad rho(Y) = 0 is a zero of V. All auxiliary constants and sets of this step
are chosen anew.
(i) Zeros of V at which D^2 rho has a positive direction. Let Y be a zero of V with rho(Y) = 0, grad rho(Y) = 0 and
lambda_Y = w.D^2 rho(Y) w > 0 for a unit vector w. In this item (x, y) are Cartesian coordinates with origin Y in
which w = (1, 0), and V_1, V_2 are the components of V in them; V.grad rho = rho and div V = 1/2 still hold. There are
r_3 and r_4 in (0, 1], which can be taken as small as we wish, such that rho_xx >= lambda_Y/2 on
Q = [-r_4, r_4] x [-r_3, r_3] and rho_x(-r_4, y) < 0 < rho_x(r_4, y) for |y| <= r_3. As in Step 21(i), for |y| <= r_3
there is exactly one chi(y) in (-r_4, r_4) with rho_x(chi(y), y) = 0, chi is C^2 with chi(0) = 0, and with
X_y = (chi(y), y), phi(y) = rho(X_y) and a bound C_chi for |chi'|, phi is C^3, phi'(y) = rho_y(X_y),
phi(0) = phi'(0) = 0, and rho(x, y) = phi(y) + c(x, y)(x - chi(y))^2 on Q with c(x, y) >= lambda_Y/4. Put
p_2(y) = rho_xx(X_y) >= lambda_Y/2, p_3(y) = rho_xxx(X_y), b(y) = V_2(X_y), b_1(y) = V_2x(X_y), b_2(y) = V_2xx(X_y)
and U(y) = V_1(X_y) - chi'(y) V_2(X_y) for |y| <= r_3; p_2 is C^1, b is C^2, and p_3, b_1, b_2 and U are continuous.
Differentiating rho_x(X_y) = 0 in y gives rho_xy(X_y) = -p_2 chi', and p_2' = p_3 chi' + rho_xxy(X_y) gives
rho_xxy(X_y) = p_2' - p_3 chi'; also b' = V_2x(X_y) chi' + V_2y(X_y). At X_y, rho_x = 0 and rho_y = phi', so the
profile equation and its first and second derivatives in x give
    phi = b phi',   p_2 U + b_1 phi' = 0,   2 p_2 (V_1x - chi' V_2x) + p_3 U + b_2 phi' + b p_2' = p_2,
with the derivatives of V taken at X_y. Since div V = 1/2, V_1x - chi' V_2x = 1/2 - V_2y - chi' V_2x = 1/2 - b', and
with U = -b_1 phi'/p_2 the last identity becomes 2 p_2 b' - b p_2' = (b_2 - b_1 p_3/p_2) phi', that is
    (b p_2^(-1/2))' = kappa phi',   kappa = (b_2 - b_1 p_3/p_2)/(2 p_2^(3/2)),   (28.10)
with kappa continuous on [-r_3, r_3]. Let C_kappa be the product of the maxima of p_2^(1/2) and of
|kappa| on [-r_3, r_3], and choose r_6 in (0, r_3] with C_kappa |phi'(y)| < 1 for |y| <= r_6, which is possible since
phi'(0) = 0. We show that phi = 0 on [0, r_6]. Otherwise let I be a component of the set of the y in (0, r_6) with
phi(y) != 0, an open interval with left end y_0 >= 0, where phi(y_0) = 0 since phi(0) = 0. On I, phi = b phi' gives
phi' != 0, so phi' has one sign and phi is strictly monotone on I; hence I = (y_0, r_6), since phi cannot vanish at
both ends of I, so I is the only such component and phi = 0 on [0, y_0]. Then phi' = 0 on [0, y_0], and b p_2^(-1/2)
is constant there by (28.10); since b(0) = 0, because V(Y) = 0, b(y_0) = 0. For y in I, (28.10) and the constant sign
of phi' on (y_0, y) give |b(y)| p_2(y)^(-1/2) <= max|kappa| |phi(y) - phi(y_0)|, so |b(y)| <= C_kappa |phi(y)|, and
phi = b phi' gives |phi(y)| <= C_kappa |phi'(y)| |phi(y)| < |phi(y)|, a contradiction. In the same way, with the right
ends of the components of the set of the y in (-r_6, 0) with phi(y) != 0, phi = 0 on [-r_6, 0]. So
phi = phi' = 0 on [-r_6, r_6]; then b p_2^(-1/2) is constant there, so b = 0, and p_2 U = -b_1 phi' = 0 gives U = 0,
so that V_2(X_y) = 0 and V_1(X_y) = U(y) + chi'(y) V_2(X_y) = 0. Consequently
rho(x, y) = c(x, y)(x - chi(y))^2 >= 0 on [-r_4, r_4] x [-r_6, r_6], and the set Z_Y of the zeros of rho in the open
set N_Y of the points with |x| < r_4 and |y| < r_6 is the arc of the X_y with |y| < r_6. At each point X_y of Z_Y,
V = 0, rho_xx = p_2(y) > 0, so D^2 rho != 0, and det DV = 0, since V vanishes along the arc and its tangent
vector (chi'(y), 1) is not 0.
(ii) A Jordan region. The proof in Step 21(v) that {rho > 0} is connected uses only a_+ > 0 > a_-, q/gamma < 1 and the
conclusion of Step 13(iii) as carried over in Step 14, which holds since q mu < 1; so {rho > 0} is connected. Let r_3,
r_4, r_6, chi, C_chi and X_y be as in (i) for Y = 0 and w = (1, 0), so that the coordinates of (i) are the original
ones; this applies since V(0) = 0, rho(0) = 0, grad rho(0) = 0 and rho_xx(0) = 2. Then rho(0) = 0 and
rho(x, 0) = c(x, 0) x^2 > 0 for 0 < |x| <= r_4, since chi(0) = 0. Let 0 < delta <= r_4. The construction
of Step 12(iii) and the argument after it in Step 21(v), which use only these facts and the connectedness of
{rho > 0}, give delta' in (0, delta), the simple polygonal arc Gamma in {rho > 0}, the closed disk B' of radius delta'
about 0, the Jordan curve J = ell union Gamma with ell = [-delta', delta'] x {0}, its bounded complementary component
Omega and the open half-disks B'_+ and B'_-, and Omega contains B'_+ or B'_-. It does not contain both: otherwise a
small disk about (delta'/2, 0) would lie in the union of Omega and ell, and (delta'/2, 0) would not be a boundary
point of the unbounded complementary component Omega_inf of J, contrary to the Jordan curve theorem. Let
sigma_* = 1 if B'_+ lies in Omega and sigma_* = -1 if B'_- does; the other half-disk lies in Omega_inf, which is open
and does not meet the closure of Omega. On J, rho >= 0, and rho vanishes on J only at 0. Let
r_7 = min(r_6, delta'/(1 + C_chi)). For 0 < |y| < r_7, |X_y| <= (1 + C_chi) |y| < delta', so X_y lies in B'_+ if
y > 0 and in B'_- if y < 0; hence X_y lies in Omega if sigma_* y > 0 and in Omega_inf if sigma_* y < 0.
(iii) The zeros of rho in the closure of Omega. First, rho >= 0 on Omega: otherwise the minimum of rho over the
compact set Omega union J is negative and, since rho >= 0 on J, attained at a point Y of Omega, where
grad rho(Y) = 0 and so rho(Y) = V(Y).grad rho(Y) = 0, a contradiction. Let K_0 be the set of the zeros of rho in Omega
union J, a compact set whose only point on J is 0. Each Y in K_0 other than 0 is a minimum of rho on the open set
Omega, so grad rho(Y) = 0, D^2 rho(Y) is positive semidefinite and, by Step 20(ii), V(Y) = 0; also V(0) = 0. Let L_0
be the set of the Y in K_0 with D^2 rho(Y) != 0, which contains 0. For Y in L_0 other than 0, D^2 rho(Y) has a unit
eigenvector w with w.D^2 rho(Y) w > 0, so (i) applies, with r_3 and r_4, which depend on Y, so small that N_Y lies in
Omega; then L_0 meets N_Y exactly in Z_Y, since every point of Z_Y lies in K_0 and has D^2 rho != 0, and Z_Y is
homeomorphic to an open interval. Let N_* be the open set of the (x, y) with |x| < r_4 and |y| < r_7, with r_4 and r_7
as in (ii); by (i) and (ii), the zeros of rho in N_* are the X_y with |y| < r_7, and those in the closure of Omega are
the X_y with 0 <= sigma_* y < r_7, so L_0 meets N_* in an arc homeomorphic to [0, 1) by a homeomorphism mapping
0 to 0. So L_0 is a one-dimensional manifold with boundary, 0 is a boundary point of it, and every other point of L_0
is an interior point. Let G_0 be the component of L_0 containing 0. Since L_0 is locally connected, G_0 is open and
closed in L_0, so G_0 is a connected one-dimensional manifold with boundary whose only boundary point is 0.
(iv) G_0 is compact. By (i), V = 0 and det DV = 0 at every point of L_0, and tr DV = div V = 1/2 on the plane. Let
Y be a point of the closure of G_0. Then Y lies in K_0, so V(Y) = 0, and by continuity det DV(Y) = 0 and
tr DV(Y) = 1/2, so DV(Y) has the eigenvalues 1/2 and 0, with unit eigenvectors w_1 and w_0, which form a basis of the
plane, not necessarily orthogonal. Suppose that D^2 rho(Y) = 0. Then Y != 0, so Y lies in Omega. Write
V(Y + xi w_1 + eta w_0) = (xi/2 + N_1(xi, eta)) w_1 + N_2(xi, eta) w_0. Since V is C^2 and rho is C^3 with rho(Y) = 0,
grad rho(Y) = 0 and D^2 rho(Y) = 0, there are r_8 > 0 and constants C_N and C_3 such that for |xi| + |eta| <= r_8 the
point Y + xi w_1 + eta w_0 lies in Omega, |N_1(xi, eta)| + |N_2(xi, eta)| <= C_N (xi^2 + eta^2) and
|rho(Y + xi w_1 + eta w_0)| <= C_3 (|xi| + |eta|)^3. Choose xi_0 in (0, r_8/2] with C_N xi_0 <= 1/40, and let Sigma be
the set of the points Y + xi w_1 + eta w_0 with 0 < xi <= xi_0 and |eta| <= xi; there
|N_1| + |N_2| <= 2 C_N xi^2 <= xi/20. For P in Sigma let P_t = Phi_(-t)(P), with coordinates (xi(t), eta(t)); then
d xi/dt = -xi/2 - N_1 and d eta/dt = -N_2, so, while P_t lies in Sigma, -(11/20)xi <= d xi/dt <= -(9/20)xi; at points
of Sigma with eta = xi, d(eta - xi)/dt >= xi/2 - xi/20 > 0, and at points of Sigma with eta = -xi,
d(eta + xi)/dt <= -xi/2 + xi/20 < 0. Let sigma_0 be the segment of the points of Sigma with xi = xi_0, and for P in
sigma_0 let t_P in [0, infinity] be the supremum of the t >= 0 with P_(t') in Sigma for 0 <= t' <= t. Let t_P be
finite. Then xi(t) >= xi_0 e^(-11t/20) for 0 <= t < t_P, so P_(t_P) lies in Sigma, and since d xi/dt < 0 in Sigma and
P_t lies outside Sigma for some t in (t_P, t_P + eps] for every eps > 0, eta = xi or eta = -xi at P_(t_P). If
eta = -xi at P_t for some t < t_P, then eta + xi < 0 at P_(t') for t' > t near t, which is false; so if eta = xi at
P_(t_P), then eta + xi > 0 at P_t for 0 <= t <= t_P, and similarly if eta = -xi at P_(t_P), then eta - xi < 0 at P_t
for 0 <= t <= t_P. Let E_+ and E_- be the sets of the P in sigma_0 for which t_P is finite and eta = xi, respectively
eta = -xi, at P_(t_P). They are disjoint, they contain the ends of sigma_0 with eta = xi_0 and eta = -xi_0,
respectively, and they are open in sigma_0: if P is in E_+, then for some eps > 0, eta + xi > 0 and xi > 0 at P_t for
0 <= t <= t_P + eps and eta > xi at P_(t_P + eps), by the strict inequalities, and by continuous dependence on P the
same holds for every P' in sigma_0 near P, so that t_(P') <= t_P + eps and eta = xi at Phi_(-t_(P'))(P'); similarly
for E_-. Since sigma_0 is connected, there is P in sigma_0 with t_P = infinity. Then P_t lies in Sigma for every
t >= 0, with xi(t) <= xi_0 e^(-9t/20) and |eta(t)| <= xi(t), so |rho(P_t)| <= 8 C_3 xi_0^3 e^(-27t/20), and
|rho(P)| = e^t |rho(P_t)| <= 8 C_3 xi_0^3 e^(-7t/20) for all t >= 0; hence rho(P) = 0. Since P lies in Omega, (iii)
gives V(P) = 0. But the coefficient of w_1 in V(P) is xi_0/2 + N_1 >= xi_0/2 - xi_0/20 > 0, a contradiction. Hence
D^2 rho(Y) != 0, so Y lies in L_0. So the closure of G_0 lies in L_0, and since G_0 is closed in L_0, G_0 is closed in
the plane; as a subset of K_0 it is compact.
(v) Conclusion. By (iii) and (iv), G_0 is a compact connected one-dimensional manifold with boundary whose only
boundary point is 0. But a compact connected one-dimensional manifold with boundary is homeomorphic to a circle or to
a closed interval, so it has no or two boundary points. Hence a_+ a_- < 0 is impossible at l = 1/4. With Step 20(iv),
a profile with l = 1/4 therefore has no limit F(e.X) != 0 with a remainder as in (d), where
q mu = q(1/2 - 1/gamma) < 1 for every 0 <= q < 1, and so, with Step 13(vi), f = 0 and |rho| = |h| <= C_h (1 + |X|)^q
for every profile with l = 1/4 and f, h and q as in (d). Only the C^3 regularity of rho is used.
Step 23 (the mixed case for C^infinity profiles and 0 < l < 1/4). Let rho, f, h, q, S, mu and u be as in Step 14, and
suppose that rho is C^infinity and 0 < l < 1/4. Then beta = 2l - 1/2 < 0 and mu = 2l - 1/gamma < 0, so that
q mu < 1 for every 0 <= q < 1 and kappa_S = 1/gamma, and by Step 19(v), a_+ != 0, a_- != 0, and a_+ > 0 or a_- > 0.
Suppose that a_+ a_- < 0; replacing e by -e if necessary, let a_+ > 0 > a_-. We show that 1/(2l) is an even integer,
that is, l = 1/(4n) for an integer n, and n >= 2 since l < 1/4. By Section 9.14, Step 3, V is C^2; since div V = 2l
and curl V = -rho_x, Delta V_1 = rho_xy and Delta V_2 = -rho_xx, so V is C^infinity by elliptic regularity. By Step 14
the flow Phi_t of V is complete; each Phi_t is a C^infinity diffeomorphism of the plane with Jacobian determinant
e^(2lt), and rho(Phi_t X) = e^t rho(X). The argument at the start of Step 20(ii) uses only l > 0, so there are no
periodic orbits, and t -> Phi_t(P) is injective for every P with V(P) != 0. For a vector w = (w_1, w_2) let
w-perp = (-w_2, w_1), so that w-perp.v = det(w, v) and (Lw)-perp.(Lv) = det(L) w-perp.v for every 2 x 2 matrix L. All
auxiliary constants, functions and sets of this step are chosen anew.
(i) Two lemmas on functions of one variable. (L1) Let G be C^infinity near 0 with G >= 0 near 0, and suppose that
G(s) = kappa s^p e^(E(s)) for 0 < s <= s_2, with constants kappa != 0, p > 0 and s_2 > 0 and a continuous function
E on [0, s_2]. Then p is an even integer. Indeed, G(s) s^(-p) tends to kappa e^(E(0)) != 0 as s decreases to 0, so by
Taylor's formula not all derivatives of G vanish at 0; let k be the least j with G^(j)(0) != 0. Then G(s) s^(-k) tends
to G^(k)(0)/k! != 0 as s decreases to 0, so p = k, and G >= 0 gives G^(k)(0) > 0, from s > 0,
and (-1)^k G^(k)(0) >= 0, from s < 0; so k is even, and G(s) > 0 for all small s != 0. (L2) Let b be C^infinity near
0 with b(0) = 0 and b'(0) = lambda > 0, let s_2 > 0 be such that b > 0 on (0, s_2] and b < 0 on [-s_2, 0), and let
c be a real number. Then b(s) = s(lambda + s beta_2(s)) with a C^infinity function beta_2,
lambda + s beta_2(s) = b(s)/s > 0 for 0 < |s| <= s_2, so
e_b(s) = 1/b(s) - 1/(lambda s) = -beta_2(s)/(lambda(lambda + s beta_2(s))) is continuous on [-s_2, s_2]; put
E_b(s) = int_0^s e_b. If G is C^1 on (0, s_2] with b G' = c G there, then G' = c(1/(lambda s) + e_b) G,
so (G s^(-c/lambda) e^(-c E_b))' = 0 and G(s) = kappa s^(c/lambda) e^(c E_b(s)) on (0, s_2] for a constant kappa.
Similarly, if G is C^1 on [-s_2, 0) with b G' = c G there, then G(s) = kappa |s|^(c/lambda) e^(c E_b(s)) on [-s_2, 0)
for a constant kappa.
(ii) The absorbing disk. Since a_+ != 0 and a_- != 0, the first inequality for d|X(t)|/dt in Step 15(i) holds, and the
proof of Step 20(i) uses only it, mu < 0 and q < 1. So there is R_* >= 1 and, for every compact set K, a T_K >= 0 such
that |Phi_T(P)| <= R_* whenever T >= T_K, P lies in K and |rho(P)| <= e^(-T).
(iii) Zeros of rho at which V does not vanish. Claim 1: let P be a point with rho(P) = 0 and V(P) != 0, let n_P be a
unit vector orthogonal to V(P), and let m > 0 with 2lm >= 1; then there are no v_2 > 0 and C_P with
|rho(P + v n_P)| <= C_P |v|^m for |v| <= v_2. Otherwise the proof of Step 20(ii) applies with P, n_P, C_P |v|^m and
Psi(t, v) = Phi_t(P + v n_P) in place of Y, n_Y, C_Y v^2 and Phi_t(Y + v n_Y), with v_0 <= v_2, with delta in (0, v_0]
such that C_P delta^m <= 1, and with G_T the set of the (t, v) with 0 <= t <= L and |v| <= delta e^(-(T + t)/m), for
T >= 0 with delta e^(-T/m) <= eps_L: now det D Psi(t, v) = e^(2lt) det(V(P + v n_P), n_P), on E_T = Psi(G_T),
|rho(Psi(t, v))| = e^t |rho(P + v n_P)| <= e^(-T), and since 2l - 1/m >= 0,
    |E_T| >= int_0^L 2 delta e^(-(T + t)/m) e^(2lt) j_0 dt >= 2 j_0 delta L e^(-T/m),
so that pi R_*^2 >= e^(2lT) |E_T| >= 2 j_0 delta L for T >= T_(K_L), which is false for large L, as R_*, j_0 and delta
do not depend on L.
Now let P be a zero of rho with V(P) != 0 such that rho >= 0 near P, and let n_P = V(P)-perp/|V(P)|. Since
D Psi_P(0, 0)(t, v) = t V(P) + v n_P for Psi_P(t, v) = Phi_t(P + v n_P), by the inverse function theorem there are
tau > 0 and v_1 > 0 such that Psi_P is a C^infinity diffeomorphism of (-tau, tau) x (-v_1, v_1) onto an open
neighborhood U_P of P on which rho >= 0. Let g_P(v) = rho(P + v n_P), so that rho(Psi_P(t, v)) = e^t g_P(v). By
Taylor's formula and Claim 1, with an integer m >= 1/(2l), not all derivatives of g_P vanish at 0; let m_P be the
least j with g_P^(j)(0) != 0. As g_P >= 0, m_P is even and g_P^(m_P)(0) > 0, and by Claim 1, 2l m_P < 1. Write
g_P(v) = v^(m_P) c_P(v) with c_P(v) = int_0^1 (1 - s)^(m_P - 1) g_P^(m_P)(sv) ds/(m_P - 1)!, a C^infinity function
with c_P(0) = g_P^(m_P)(0)/m_P! > 0, and shrink v_1, replacing U_P by Psi_P((-tau, tau) x (-v_1, v_1)), so that
c_P > 0 on (-v_1, v_1). Then the zeros of rho in U_P are the Phi_t(P) with |t| < tau, an arc of the orbit of P.
Moreover, the derivatives of rho(Psi_P(t, v)) = e^t v^(m_P) c_P(v) of order less than m_P vanish at (0, 0), and those
of order m_P there are those of c_P(0) v^(m_P); so, by the chain rule for Psi_P and its inverse, D^j rho(P) = 0 for
j < m_P, and, writing a vector w as t V(P) + v n_P with v = n_P.w,
    D^(m_P) rho(P)[w, ..., w] = m_P! a(P) (n_P.w)^(m_P),   a(P) = c_P(0) > 0.
As rho = e^(-t) rho(Phi_t) and Phi_t is a C^infinity diffeomorphism, the least j with D^j rho != 0 is the same at all
points of the orbit of P, which are zeros of rho with V != 0 near which rho >= 0, and by the above it equals m_Q at
each such point Q; we call this even integer m the order of the orbit. Let Q be a point of such an orbit, t real,
Q_t = Phi_t(Q) and L_t = D Phi_t(Q). Differentiating rho(Phi_t(X)) = e^t rho(X) m times in X at Q, where the
derivatives of rho of order less than m vanish at Q and at Q_t, gives
D^m rho(Q_t)[L_t w, ..., L_t w] = e^t D^m rho(Q)[w, ..., w] for every w. Since L_t V(Q) = V(Q_t) and
det(L_t) = e^(2lt), n_(Q_t).L_t w = (L_t V(Q))-perp.(L_t w)/|V(Q_t)| = e^(2lt)(|V(Q)|/|V(Q_t)|)(n_Q.w), and therefore,
taking w = n_Q,
    a(Phi_t(Q)) = a(Q) e^((1 - 2lm)t) (|V(Phi_t(Q))|/|V(Q)|)^m.   (28.11)
(iv) Zeros of V. Let Y be a zero of V with rho(Y) = 0 and rho >= 0 near Y, so that grad rho(Y) = 0. As
curl V = -rho_x, B = DV(Y) is symmetric, with trace div V = 2l > 0. Claim 2: if B is singular, then 1/(2l) is an even
integer. Indeed, the eigenvalues of B are then 0 and 2l; let w be a unit eigenvector for 2l. By the strong unstable
manifold theorem (M. W. Hirsch, C. C. Pugh and M. Shub, Invariant Manifolds, Lecture Notes in Mathematics 583,
Springer, 1977), applied to V as a C^1 vector field, the points whose backward orbits stay in a small neighborhood of
Y and converge to Y faster than e^(lt) form a C^1 curve W_u through Y tangent to w, which contains the backward orbits
of its points. For each r >= 2, the theorem applied to V as a C^r vector field gives such a curve on a smaller
neighborhood of Y, which is C^r; by this characterization it lies in W_u, so it is a neighborhood of Y in W_u, and W_u
is C^r near Y. The points of W_u other than Y are not zeros of V, as they converge to Y, so each of the two components
of W_u minus {Y} lies on one orbit of the C^infinity vector field V and is a C^infinity curve. Hence W_u is a
C^infinity curve near Y, and there are s_0 > 0 and an injective C^infinity map zeta of (-s_0, s_0) into the plane with
zeta(0) = Y, zeta'(0) = w and zeta' != 0 such that V is tangent to zeta, that is, V(zeta(s)) = b(s) zeta'(s) with the
C^infinity function b(s) = zeta'(s).V(zeta(s))/|zeta'(s)|^2. Then b(0) = 0, and differentiating at s = 0 gives
Bw = b'(0) w, so b'(0) = 2l. Fix s_2 in (0, s_0) such that b > 0 on (0, s_2], b < 0 on [-s_2, 0), and rho >= 0 on a
neighborhood of zeta([-s_2, s_2]). For 0 < |s| <= s_2, the solution sigma of sigma' = b(sigma), sigma(0) = s,
satisfies Phi_t(zeta(s)) = zeta(sigma(t)) for t <= 0, by uniqueness, and sigma(t) tends to 0 as t tends to -infinity;
so zeta((0, s_2]) and zeta([-s_2, 0)) lie on two orbits converging to Y as t tends to -infinity. Let
g(s) = rho(zeta(s)). Differentiating g(sigma(t)) = e^t g(s) at t = 0 gives b g' = g, and g >= 0. If g does not vanish
identically on (0, s_2], then (L2) with c = 1 and lambda = 2l, and (L1), show that 1/(2l) is an even integer;
similarly if g does not vanish identically on [-s_2, 0), applying (L1) to G(s) = g(-s). Otherwise
g = 0 on [-s_2, s_2], the points zeta(s) with 0 < |s| <= s_2 are zeros of rho with V != 0 near which rho >= 0, and
by (iii) the two orbits have even orders m_+, for s > 0, and m_-, for s < 0. Let m = min(m_+, m_-),
n(s) = zeta'(s)-perp/|zeta'(s)| and a_*(s) = D^m rho(zeta(s))[n(s), ..., n(s)]/m!, a
C^infinity function on (-s_0, s_0). For 0 < |s| <= s_2, n(s) = n_(zeta(s)) or n(s) = -n_(zeta(s)), so
a_*(s) = a(zeta(s)) > 0 on a half of order m, and a_*(s) = 0 on a half of order larger than m; hence a_* >= 0 near 0.
Replacing zeta(s) by zeta(-s) and b(s) by -b(-s) if necessary, let the order on (0, s_2] be m. For 0 < s <= s_2 put
nu(s) = a_*(s)(b(s)|zeta'(s)|)^(-m). Since |V(zeta(s))| = b(s)|zeta'(s)|, (28.11) gives
nu(sigma(t)) = e^((1 - 2lm)t) nu(s) for t <= 0, and differentiating at t = 0, b nu' = (1 - 2lm) nu on (0, s_2].
By (L2), nu(s) = kappa s^((1 - 2lm)/(2l)) e^((1 - 2lm)E_b(s)) with a constant kappa > 0, so, as
b(s) = s(2l + s beta_2(s)),
    a_*(s) = kappa s^(1/(2l)) e^(E_*(s)),   E_*(s) = (1 - 2lm)E_b(s) + m log((2l + s beta_2(s))|zeta'(s)|),
for 0 < s <= s_2, with E_* continuous on [0, s_2]. By (L1), 1/(2l) is an even integer. This proves Claim 2.
(v) Saddles. Let Y be as in (iv), with B having eigenvalues lambda_s < 0 < lambda_u. We call a set H a half-arc at
Y of the first kind if H = {Phi_t(Q) : t > 0} for a point Q with Phi_t(Q) -> Y as t -> infinity, and of the second
kind if H = {Phi_t(Q) : t < 0} for a point Q with Phi_t(Q) -> Y as t -> -infinity; Q != Y, so H does not contain Y,
and since t -> Phi_t(Q) is injective, H is not of both kinds. We show that there is an open neighborhood N_Y of Y,
inside any given neighborhood of Y, such that the zeros of rho in N_Y other than Y form d_Y = 2 or d_Y = 4 pairwise
disjoint half-arcs at Y, each closed in N_Y minus {Y}. By the stable manifold theorem (loc. cit.), the local stable
and unstable manifolds of Y are C^infinity curves through Y, transversal at Y, so there are
C^infinity coordinates (xi, eta) near Y, with Y at the origin, in which they are the eta-axis and the xi-axis. Both
are invariant, so in these coordinates V = (xi A_1(xi, eta), eta B_1(xi, eta)) with C^infinity functions A_1 and B_1,
A_1(0, 0) = lambda_u and B_1(0, 0) = lambda_s. Choose eps > 0 such that the square Q_eps of the points with
|xi| <= eps and |eta| <= eps lies in the given neighborhood, rho >= 0 on a neighborhood of Q_eps, A_1 >= lambda_u/2
and B_1 <= lambda_s/2 on Q_eps. While an orbit stays in Q_eps, |xi| does not decrease, |eta| does not increase, and
they are strictly monotone where xi != 0, respectively eta != 0. For 0 < |eta_0| <= eps, the orbit of the
point (0, eta_0) stays on the eta-axis and |eta(t)| <= |eta_0| e^(lambda_s t/2) for t >= 0, so it converges to Y, and
since rho is bounded near Y and rho(Phi_t(P)) = e^t rho(P), rho(0, eta_0) = 0. On the xi-axis, V(s, 0) = b(s)(1, 0)
with b(s) = s A_1(s, 0), b'(0) = lambda_u, and as in (iv), g(s) = rho(s, 0) satisfies b g' = g and g >= 0. If g does
not vanish identically on one of (0, eps] and [-eps, 0), then by (L2) and (L1) g > 0 near 0 on the other, and by (L2)
on all of it; so rho > 0 on both open half-axes {0 < xi <= eps, eta = 0} and {-eps <= xi < 0, eta = 0}, or rho = 0 on
both. Let P be a zero of rho in the interior of Q_eps with xi(P) != 0 and eta(P) != 0. Backward in time |eta|
increases at least like e^(|lambda_s| |t|/2) while the orbit stays in Q_eps, and |xi| decreases, and forward in time
|xi| increases at least like e^(lambda_u t/2); so the orbit of P passes through Q_eps along a compact arc
Pi_P = {Phi_t(Q_P) : 0 <= t <= t_P} containing P, where Q_P is a zero of rho on one of the sides S_+ and S_- of Q_eps
on which eta = eps, respectively eta = -eps, with 0 < |xi(Q_P)| < eps, and t_P is the least t >= 0 with
|xi(Phi_t(Q_P))| = eps. On S_+ and S_-, the eta-component eta B_1 of V does not vanish, so by (iii) each zero Q of rho
on S_+ or S_- has a neighborhood in which the zeros of rho form an arc of the orbit of Q along which eta is strictly
monotone; hence the zeros of rho on S_+ and S_- form a compact set of isolated points, a finite set. Let Q_1, ..., Q_k
be those with xi != 0, and Pi_i = {Phi_t(Q_i) : 0 <= t <= t_i}, with t_i the least t >= 0 with |xi(Phi_t(Q_i))| = eps,
so that Pi_P is one of the Pi_i for every P as above. Each Pi_i is compact and does not contain Y, so delta_i, the
minimum of max(|xi|, |eta|) over Pi_i, is positive. Choose eps' in (0, eps) with eps' < delta_i for every i, and let
N_Y be the open square of the points with |xi| < eps' and |eta| < eps'. Then every zero of rho in N_Y lies on an axis.
So the zeros of rho in N_Y other than Y are the two half-arcs {Phi_t(0, eps') : t > 0} and {Phi_t(0, -eps') : t > 0}
of the first kind, the open stable half-axes, and, if g = 0 on [-eps, eps], also the two half-arcs
{Phi_t(eps', 0) : t < 0} and {Phi_t(-eps', 0) : t < 0} of the second kind, the open unstable half-axes; each is closed
in N_Y minus {Y}, and d_Y = 2 or d_Y = 4.
(vi) Sources. Let Y be as in (iv), with B having eigenvalues 0 < lambda_1 <= lambda_2. We show that there is an open
neighborhood N_Y of Y, inside any given neighborhood of Y, such that the zeros of rho in N_Y other than Y form an even
number d_Y >= 0 of pairwise disjoint half-arcs at Y of the second kind, each closed in N_Y minus {Y}. Take Cartesian
coordinates z = (x, y) with origin Y along orthonormal eigenvectors of B, so that B = diag(lambda_1, lambda_2).
A monomial vector field x^i y^j d/dx or x^i y^j d/dy with i + j >= 2 is resonant if
i lambda_1 + j lambda_2 = lambda_1, respectively = lambda_2; since 0 < lambda_1 <= lambda_2, the only resonant ones
are x^(i_0) d/dy with lambda_2 = i_0 lambda_1 for an integer i_0 >= 2. So by the Poincare-Dulac
theorem (see V. I. Arnold, Geometrical Methods in the Theory of Ordinary Differential Equations, Springer, 1983) V is
formally conjugate at Y to
    N = lambda_1 x d/dx + (lambda_2 y + c x^(i_0)) d/dy,
with a constant c and an integer i_0 >= 2, where c = 0 unless lambda_2 = i_0 lambda_1; if lambda_2/lambda_1 is not an
integer >= 2, then c = 0 and we take i_0 = 2. Since V and N are C^infinity with a hyperbolic zero, by the theorem of
Sternberg and Chen (S. Sternberg, Amer. J. Math. 80 (1958) 623-631; K.-T. Chen, Amer. J. Math. 85 (1963) 693-722)
there is a C^infinity diffeomorphism H_Y of a neighborhood U of Y onto a neighborhood of 0, with H_Y(Y) = 0 and
DH_Y(X) V(X) = N(H_Y(X)) on U; we take U in the given neighborhood, with rho >= 0 on U. Then R = rho(H_Y^(-1))
satisfies N.grad R = R near 0, and R >= 0. The monomial x^i y^j has weight i lambda_1 + j lambda_2; for each w the
span M_w of the monomials of weight w is finite-dimensional,
N.grad(x^i y^j) = (i lambda_1 + j lambda_2) x^i y^j + c j x^(i+i_0) y^(j-1), where the last monomial has weight
i lambda_1 + j lambda_2 if c != 0, so N.grad maps M_w into M_w. There N.grad - 1 = (w - 1)I if c = 0, and if c != 0,
N.grad - 1 = (w - 1)I + c D_0 with the map D_0(x^i y^j) = j x^(i+i_0) y^(j-1) of M_w into itself, which is nilpotent
since it lowers the exponent of y. So N.grad - 1 is invertible on M_w for w != 1. Since (N.grad - 1)R = 0 and the
Taylor series of N.grad R at 0 is N.grad applied to that of R, each part of weight w != 1 of the Taylor series of
R vanishes, so the Taylor series of R is the polynomial P of its terms of weight 1, N.grad P = P, and R - P is flat
at 0. The flow of N is psi_t(x, y) = (e^(lambda_1 t) x, e^(lambda_2 t)(y + c t x^(i_0))). Choose r in (0, 1] such that
the closed disk D_r of radius r about 0 lies in H_Y(U), contains no zero of N other than 0, and
2(lambda_1 x^2 + lambda_2 y^2 + c x^(i_0) y) >= lambda_1 (x^2 + y^2) for (x, y) in D_r, which is possible since
i_0 >= 2; the left side is d|psi_t(z)|^2/dt at a time t with psi_t(z) = (x, y). Then psi_t(z) lies in D_r for z in D_r
and t <= 0, with |psi_(-tau)(z)| <= (2 + |c| tau) e^(-lambda_1 tau) |z| for tau >= 0, and
H_Y^(-1)(psi_t(z)) = Phi_t(H_Y^(-1)(z)). The function R - P satisfies (R - P)(psi_t(z)) = e^t (R - P)(z), and for
every M there is C_M with |(R - P)(z)| <= C_M |z|^M on D_r, so (R - P)(z) = e^tau (R - P)(psi_(-tau)(z)) gives
|(R - P)(z)| <= C_M (2 + |c| tau)^M e^((1 - M lambda_1) tau), which tends to 0 as tau tends to infinity if
M lambda_1 > 1. So R = P on D_r. P != 0, since otherwise rho = 0 near a point H_Y^(-1)(z), 0 < |z| < r, at which
V != 0, against (iii). For z in D_r other than 0, |psi_t(z)| increases with t while psi_t(z) lies in D_r, and every
crossing of C_r is outward, so the orbit of z meets the circle C_r of radius r about 0 in exactly one point z_1, its
part in the open disk D'_r of radius r about 0 is {psi_t(z_1) : t < 0}, and psi_t(z_1) tends to 0 as t tends to
-infinity. As P(psi_t(z_1)) = e^t P(z_1), the zeros of P in D'_r other than 0 are the sets {psi_t(z_1) : t < 0} with
z_1 a zero of P on C_r. P does not vanish on all of C_r, since otherwise P = 0 on D_r, and
theta -> P(r cos theta, r sin theta) is a trigonometric polynomial, so P has finitely many zeros on C_r; let d_Y be
their number. With N_Y = H_Y^(-1)(D'_r), the zeros of rho in N_Y other than Y are the d_Y half-arcs
{Phi_t(H_Y^(-1)(z_1)) : t < 0} of the second kind, pairwise disjoint and each closed in N_Y minus {Y}. It remains to
show that d_Y is even; P >= 0 near 0 since R >= 0. If c != 0, then on M_1, N.grad - 1 = c D_0, so D_0 P = 0, so no
power of y with a positive exponent occurs in P, and P = kappa x^i with kappa != 0; P >= 0 forces i to be even, and
the zeros of P on C_r are (0, r) and (0, -r), so d_Y = 2. Let c = 0. If lambda_1/lambda_2 is irrational, at most one
monomial has weight 1, so P = kappa x^i y^j, P >= 0 forces i and j to be even, and the zeros of P on C_r are the two
points with x = 0 if i > 0 and the two points with y = 0 if j > 0; so d_Y = 2 or d_Y = 4. If lambda_1 = c_0 k_1 and
lambda_2 = c_0 k_2 with c_0 > 0 and coprime positive integers k_1 and k_2, then a monomial x^i y^j of P has
k_1 i + k_2 j = 1/c_0, so p_0 = 1/c_0 is an integer, and with iota(x, y) = ((-1)^(k_1) x, (-1)^(k_2) y),
P(iota(z)) = (-1)^(p_0) P(z). Since P >= 0 near 0 and P != 0, p_0 is even and P(iota(z)) = P(z). So the involution
iota of C_r maps the zeros of P on C_r onto themselves. Its fixed points on C_r are: none if k_1 and k_2 are
odd; (r, 0) and (-r, 0) if k_1 is even, where P(x, 0) is 0 or kappa' x^i with k_1 i = p_0 and a constant kappa' != 0,
so that both or neither are zeros of P; and (0, r) and (0, -r) if k_2 is even, where similarly both or neither are
zeros of P. Hence d_Y is even.
(vii) The origin and a Jordan region. Step 21(i) holds, with r_3, r_4, chi, C_chi, X_y, phi and c(x, y) >= 1/2, since
it uses only the regularity of rho and rho_x(0) = 0, rho_xx(0) = 2; and as in the first two sentences of Step 21(ii),
which do not use beta > 0, phi = b phi' with b(y) = V_2(X_y) and |b(y) - beta y| <= C_2 y^2. Choose r_5 in (0, r_3]
with C_2 r_5 <= |beta|/2; then y b(y) < 0 for 0 < |y| <= r_5. There (phi^2)' = 2 phi^2/b, which is <= 0 on (0, r_5]
and >= 0 on [-r_5, 0), so, as phi(0) = 0, phi = 0 on [-r_5, r_5]. Hence
rho(x, y) = c(x, y)(x - chi(y))^2 >= 0 on [-r_4, r_4] x [-r_5, r_5], with the zeros X_y, |y| <= r_5, there. At X_y,
grad rho = 0 and rho_xy = -rho_xx chi', so the derivative in x of the profile equation gives
rho_xx(X_y)(V_1(X_y) - chi'(y) V_2(X_y)) = 0, and V(X_y) = b(y)(chi'(y), 1). So for 0 < |y| <= r_5 the solution sigma
of sigma' = b(sigma), sigma(0) = y, satisfies Phi_t(X_y) = X_(sigma(t)) for t >= 0, and |sigma(t)| decreases to 0; in
particular V(X_y) != 0 for 0 < |y| <= r_5. Now, as in Step 22(ii), {rho > 0} is connected, and
rho(x, 0) = c(x, 0) x^2 > 0 for 0 < |x| <= r_4; the rest of Step 22(ii), with r_5 in place of r_6 and the present r_3,
r_4, chi, C_chi and X_y, uses only these facts, rho(0) = 0 and |X_y| <= (1 + C_chi)|y|, and gives delta', Gamma, J,
Omega, B'_+, B'_-, Omega_inf, sigma_* and r_7 = min(r_5, delta'/(1 + C_chi)), with X_y in Omega if 0 < sigma_* y < r_7
and in Omega_inf if 0 < -sigma_* y < r_7. As in the first two sentences of Step 22(iii), which use only
rho = V.grad rho and these properties of J, rho >= 0 on Omega, and the set K_0 of the zeros of rho in Omega union J is
compact and meets J only in 0; each point of K_0 other than 0 lies in the open set Omega, so that rho >= 0 near it.
Let N_0 be the open set of the (x, y) with |x| < r_4 and |y| < r_7. The zeros of rho in N_0 are the X_y with
|y| < r_7, and those in the closure Omega union J of Omega are the X_y with 0 <= sigma_* y < r_7, since Omega_inf does
not meet the closure of Omega. So K_0 meets N_0 minus {0} in A_0 = {Phi_t(X_(sigma_* r_7)) : t > 0}, a half-arc at
0 of the first kind. No zero of V other than 0 lies in [-r_4, r_4] x [-r_5, r_5], which contains the closure of N_0,
since a zero of V is a zero of rho = V.grad rho.
(viii) The contradiction. Suppose that 1/(2l) is not an even integer. Let E_V be the set of the zeros of V in K_0; it
contains 0. For Y in E_V other than 0, Y lies in Omega and rho >= 0 near Y, so by Claim 2, B = DV(Y) is invertible; so
is DV(0) = A. As B is symmetric with trace 2l > 0, Y is a saddle as in (v) or a source as in (vi). Every point of E_V
is an isolated zero of V, and E_V is compact, so E_V is finite. Choose for each Y in E_V other than 0 a neighborhood
N_Y as in (v) or (vi), inside Omega, such that these sets and the closure of N_0 are pairwise disjoint. Below, the
half-arcs at a point Y of E_V other than 0 are the d_Y half-arcs in N_Y given by (v) or (vi), and the only half-arc at
0 is A_0. Let Z_* be the set of the points of K_0 at which V does not vanish. For P in Z_*, P != 0, so P lies in
Omega, and the orbit O of P is connected, consists of zeros of rho and does not contain the zero 0 of V; since the
only zero of rho on J is 0, O does not meet J, so O lies in Omega, and therefore in Z_*. Since O lies in the compact
set K_0, its omega-limit set is not empty, compact and connected. Suppose that it contains a point Q with V(Q) != 0.
Then Q lies in Z_*, and by (iii) there is a neighborhood U_Q of Q in which the zeros of rho are the Phi_s(Q) with
|s| < tau. There are t_1 and t_2 > t_1 + 2 tau with Phi_(t_i)(P) in U_Q, so Phi_(t_i)(P) = Phi_(s_i)(Q) with
|s_i| < tau, and Phi_(t_2 - t_1 + s_1 - s_2)(Q) = Q with t_2 - t_1 + s_1 - s_2 > 0, so the orbit of Q is periodic,
which is impossible. So the omega-limit set of P lies in the finite set E_V, and being connected it is one point Y of
E_V, so Phi_t(P) -> Y as t -> infinity. Then Phi_t(P) lies in N_Y for t >= t_3, for some t_3, so the connected set
T = {Phi_t(P) : t >= t_3} lies in the union of the half-arcs at Y; for Y = 0 this union is A_0, as T lies in K_0. As
these half-arcs are pairwise disjoint and closed in N_Y minus {Y}, T lies in one of them, H. H is of the first kind:
otherwise H = {Phi_s(Q') : s < 0} with Q' on O, and Phi_t(P) = Phi_(t + t_4)(Q') with a constant t_4 would have
t + t_4 < 0 for every t >= t_3. Similarly Phi_t(P) -> Y' as t -> -infinity for a point Y' of E_V, and the backward
orbit of P lies, from some time on, in a half-arc at Y' of the second kind. Let Theta be the set of the
pairs (O, +) and (O, -) with O an orbit in Z_*, and Lambda_0 the set of all half-arcs at the points of E_V. Map (O, +)
to the half-arc of the first kind at the limit of O as t -> infinity containing the forward orbit of a point of O from
some time on, and (O, -) to the half-arc of the second kind at the limit as t -> -infinity containing its backward
orbit from some time on; these half-arcs are unique, since the half-arcs at a point are disjoint. Every half-arc H at
a point Y of E_V consists of zeros of rho in K_0 (for Y != 0 since N_Y lies in Omega) on an orbit not containing Y, so
it lies in Z_*, in exactly one orbit O_H. If H is of the first kind, O_H converges to Y as t -> infinity and contains
H, so (O_H, +) is mapped to H; similarly for the second kind with (O_H, -). And if (O, s) and (O', s') are mapped to
the same H, then O = O' = O_H and s = s', as H is of one kind only. So the map is a bijection of Theta onto Lambda_0,
so Theta is finite, and with k_* the number of orbits in Z_*,
    2 k_* = |Theta| = |Lambda_0| = 1 + (the sum of the d_Y over the Y in E_V other than 0).
The left side is even, and by (v) and (vi) every d_Y is even, so the right side is odd, a contradiction. Hence 1/(2l)
is an even integer.
(ix) Conclusion. If rho is C^infinity, 0 < l < 1/4 and l is not 1/(4n) for any integer n >= 2, then a_+ a_- < 0 is
impossible, so, with Step 19(v), a nonzero F(e.X) as in Step 14 has a_+ > 0 and a_- > 0. The C^infinity regularity of
rho is used in the opening, for the smoothness of V and through Step 19(v), and in (iii)-(vi).
Step 24 (the mixed case for C^m profiles and 3/16 < l < 1/4). Let rho, f, h, q, S, mu and u be as in Step 14, let
3/16 < l < 1/4, and suppose that rho is C^m for an integer m with (m - 1)(2l - 1/4) >= 1. Since 0 < 2l - 1/4 < 1/4,
this forces m - 1 > 4, so m >= 6 and l > 1/(2m); m = 9 is admissible for every such l, and m = 6 if 9/40 <= l < 1/4.
As in Step 23, beta < 0, mu < 0, q mu < 1 for every 0 <= q < 1 and kappa_S = 1/gamma, and by Step 19(v), a_+ != 0,
a_- != 0, and a_+ > 0 or a_- > 0. Suppose that a_+ a_- < 0; replacing e by -e if necessary, let a_+ > 0 > a_-. We
derive a contradiction. The notation w-perp is as in Step 23; all other auxiliary constants, functions and sets of
this step are chosen anew.
(i) Regularity. By Section 9.14, Step 3, V is C^2, and as in Step 23, Delta V_1 = rho_xy and Delta V_2 = -rho_xx.
These functions are C^(m - 2), so they and their derivatives of order m - 3 are locally Lipschitz, and interior
Schauder estimates give V in C^(m-1,alpha)_loc for every 0 < alpha < 1; so V is C^(m - 1). By Step 14 the flow Phi_t
of V is complete, and each Phi_t is a C^(m - 1) diffeomorphism of the plane with Jacobian determinant e^(2lt);
rho(Phi_t X) = e^t rho(X), there are no periodic orbits, and t -> Phi_t(P) is injective if V(P) != 0, as in Step 23.
The lemmas of Step 23(i) hold under weaker regularity. (L1) holds if G is only C^j for an integer j >= p: if all
derivatives of G of order at most j vanish at 0, then G(s) s^(-p) tends to 0 by Taylor's formula, which is false, and
otherwise the proof of (L1) applies, with k <= j. (L2) holds if b is only C^2, with beta_2(s) = int_0^1 (1 - t)
b''(ts) dt, which is continuous; only the continuity of beta_2 and e_b is used there. Step 23(ii) holds as it stands.
(ii) Zeros of rho at which V does not vanish. Claim 1 of Step 23(iii) and its proof hold as they stand; they use the
flow only through Step 23(ii) and the C^1 regularity of the Phi_t. Let P be a zero of rho with V(P) != 0 such that
rho >= 0 near P, and let n_P, tau, v_1, Psi_P, U_P and g_P be as in Step 23(iii), Psi_P now being a C^(m - 1)
diffeomorphism. Then g_P is C^m, g_P(0) = 0, and, as g_P >= 0 near 0, g_P'(0) = 0 and g_P''(0) >= 0. If g_P''(0) = 0,
then by Taylor's formula |g_P(v)| <= C_P |v|^3 for |v| <= v_1 with a constant C_P, which is impossible by Claim 1 with
the exponent 3 in place of m, since 6l > 1. So g_P''(0) > 0, and the rest of Step 23(iii) holds with m_P = 2 and
c_P(v) = int_0^1 (1 - s) g_P''(sv) ds, a C^(m - 2) function with c_P(0) = g_P''(0)/2 > 0. In particular every orbit of
a zero of rho at which V does not vanish and near which rho >= 0 has order 2, and (28.11) holds with 2 in place of m:
    a(Phi_t(Q)) = a(Q) e^((1 - 4l)t) (|V(Phi_t(Q))|/|V(Q)|)^2.
(iii) Zeros of V. Let Y be a zero of V with rho(Y) = 0 and rho >= 0 near Y, so that grad rho(Y) = 0. As in Step
23(iv), B = DV(Y) is symmetric with trace 2l; let lambda_1 <= lambda_2 be its eigenvalues, and let H = D^2 rho(Y),
which is positive semidefinite. Claim 3: if H != 0, then lambda_1 = 2l - 1/2 < 0 and lambda_2 = 1/2. Indeed,
differentiating V.grad rho = rho twice at Y, where V and grad rho vanish, gives B^T H + H B = H, that
is, (lambda_i + lambda_j - 1) H_ij = 0 for i, j = 1, 2 in Cartesian coordinates along orthonormal eigenvectors of B.
As H is positive semidefinite and H != 0, H_ii > 0 for some i, so lambda_i = 1/2; the other eigenvalue is
2l - 1/2 < 0, so lambda_2 = 1/2. Claim 4: if H = 0, then lambda_2 <= 1/4. Suppose that H = 0 and lambda_2 > 1/4. Then
lambda_1 = 2l - lambda_2 < l < lambda_2. As rho >= 0 near Y and the cubic form D^3 rho(Y)[z, z, z] is odd in z,
D^3 rho(Y) = 0, so by Taylor's formula there are r_0 > 0 and C_4 such that |rho(Y + z)| <= C_4 |z|^4 for |z| <= r_0.
Let w be a unit eigenvector of B for lambda_2. By the strong unstable manifold theorem (loc. cit. in Step 23(iv)),
applied to V as a C^(m - 1) vector field, the points X whose backward orbits stay in a small neighborhood of Y and
satisfy e^(-lt)|Phi_t(X) - Y| -> 0 as t -> -infinity form a C^(m - 1) curve W_u through Y tangent to w, which contains
the backward orbits of its points. Its points other than Y are not zeros of V, as their backward orbits converge to Y,
and so V is tangent to W_u. So there are s_0 > 0 and an injective C^(m - 1) map zeta of (-s_0, s_0) into the plane
with zeta(0) = Y, zeta'(0) = w and zeta' != 0 such that V(zeta(s)) = b(s) zeta'(s), where
b(s) = zeta'(s).V(zeta(s))/|zeta'(s)|^2 is C^(m - 2); b(0) = 0, and differentiating at s = 0 gives Bw = b'(0) w, so
b'(0) = lambda_2. Fix s_2 in (0, s_0) as in Step 23(iv), with moreover |zeta(s) - Y| <= r_0 for |s| <= s_2, and define
sigma and g(s) = rho(zeta(s)) as there. Then b g' = g, g >= 0, and |g(s)| <= C_4 C_zeta^4 s^4 for |s| <= s_2, with
C_zeta the maximum of |zeta'| on [-s_2, s_2]. If g does not vanish identically on (0, s_2], then by (L2) with c = 1,
g(s) = kappa s^(1/lambda_2) e^(E_b(s)) on (0, s_2] with a constant kappa != 0, and since 1/lambda_2 < 4, g(s) s^(-4)
is unbounded as s decreases to 0, which is false; similarly on [-s_2, 0). So g = 0 on [-s_2, s_2], and the points
zeta(s) with 0 < |s| <= s_2 are zeros of rho with V != 0 near which rho >= 0; by (ii), their orbits have order 2. Let
n(s) = zeta'(s)-perp/|zeta'(s)| and a_*(s) = D^2 rho(zeta(s))[n(s), n(s)]/2, a C^(m - 2) function on (-s_0, s_0) with
a_*(0) = 0, as H = 0, and a_*(s) = a(zeta(s)) > 0 for 0 < |s| <= s_2, since n(s) = n_(zeta(s)) or n(s) = -n_(zeta(s)).
For 0 < s <= s_2 put nu(s) = a_*(s)(b(s)|zeta'(s)|)^(-2). As in Step 23(iv), (28.11) with 2 in place of m gives
b nu' = (1 - 4l) nu on (0, s_2], and by (L2), with b(s) = s(lambda_2 + s beta_2(s)),
    a_*(s) = kappa s^p e^(E_*(s)),   p = 2 + (1 - 4l)/lambda_2,
for 0 < s <= s_2, with a constant kappa > 0 and E_*(s) = (1 - 4l)E_b(s) + 2 log((lambda_2 + s beta_2(s))|zeta'(s)|),
which is continuous on [0, s_2]. Since 3/16 < l < 1/4, 0 < 1 - 4l < 1/4 < lambda_2, so 2 < p < 3; but (L1), applied to
the nonnegative C^(m - 2) function a_* with j = m - 2 >= 4, shows that p is an even integer, a contradiction. This
proves Claim 4. Consequently B is invertible, and either H != 0 and Y is a saddle with eigenvalues 2l - 1/2 and 1/2,
or H = 0 and Y is a source with 0 < lambda_1 <= lambda_2 <= 1/4; in the latter case
lambda_1 = 2l - lambda_2 >= 2l - 1/4, so (m - 1) lambda_1 >= 1, and
2 lambda_1 - lambda_2 = 4l - 3 lambda_2 >= 4l - 3/4 > 0.
(iv) Saddles. Let Y be as in (iii), with B having eigenvalues lambda_s < 0 < lambda_u. Then Step 23(v) holds for Y,
with the following changes of regularity. The local stable and unstable manifolds of Y are
C^(m - 1) curves (loc. cit.), so the coordinates (xi, eta) are C^(m - 1), V is C^(m - 2) in them, A_1 and B_1 are
C^(m - 3), b(s) = s A_1(s, 0), the xi-component of V at (s, 0), is C^(m - 2), and g(s) = rho(s, 0) is C^(m - 1).
So (L2) applies to b, and (L1) applies to g, since its exponent is 1/lambda_u, and 1/lambda_u < 1/(2l) < 3 <= m - 1 as
lambda_u = 2l - lambda_s > 2l. The rest of Step 23(v) uses only that the coordinates are C^1, the continuity of A_1
and B_1, and Step 23(iii), which (ii) replaces. So there is an open neighborhood N_Y of Y, inside any given
neighborhood of Y, such that the zeros of rho in N_Y other than Y form d_Y = 2 or d_Y = 4 pairwise disjoint half-arcs
at Y, each closed in N_Y minus {Y}.
(v) Sources. Let Y be as in (iii), with B having eigenvalues 0 < lambda_1 <= lambda_2, so
that (m - 1) lambda_1 >= 1 and lambda_2 < 2 lambda_1 by (iii). We show that there is an open neighborhood N_Y of Y,
inside any given neighborhood of Y, such that the zeros of rho in N_Y other than Y form an even number d_Y >= 0 of
pairwise disjoint half-arcs at Y of the second kind, each closed in N_Y minus {Y}. In place of the normal forms
of Step 23(vi) we use a C^(m - 1) linearization. Take Cartesian coordinates z = (x, y) with origin Y along orthonormal
eigenvectors of B, so that B = diag(lambda_1, lambda_2) and V(z) = Bz + N_B(z) with a C^(m - 1) map N_B,
N_B(0) = 0 and DN_B(0) = 0. Choose r_0 in (0, 1] such that the closed disk U_0 of radius r_0 about 0 lies in the given
neighborhood, rho >= 0 on U_0 and |DN_B| <= lambda_1/2 on U_0, and c_N such that |N_B(z)| <= c_N |z|^2 and
|DN_B(z)| <= c_N |z| on U_0. Then z.V(z) >= lambda_1 |z|^2 - |z| |N_B(z)| >= (lambda_1/2)|z|^2 on U_0, so for z in
U_0, Z_t = Phi_(-t)(z) satisfies d|Z_t|^2/dt <= -lambda_1 |Z_t|^2 while it lies in U_0; hence Z_t lies in U_0 for
every t >= 0, |Z_t| is nonincreasing in t, and |Z_t| <= e^(-lambda_1 t/2) |z|. Then
d|Z_t|^2/dt <= -2 lambda_1 |Z_t|^2 + 2 c_N |Z_t|^3 <= (-2 lambda_1 + 2 c_N e^(-lambda_1 t/2)) |Z_t|^2, so
|Z_t| <= C_0 e^(-lambda_1 t) |z| with C_0 = e^(2 c_N/lambda_1). As B is symmetric with smallest eigenvalue lambda_1
and |DN_B(Z_t)| <= c_N C_0 e^(-lambda_1 t), every solution omega of omega' = -(B + DN_B(Z_t)) omega satisfies
d|omega|^2/dt <= (-2 lambda_1 + 2 c_N C_0 e^(-lambda_1 t)) |omega|^2, so
|omega(t)| <= C_1 e^(-lambda_1 (t - t')) |omega(t')| for t >= t' >= 0, with C_1 = e^(c_N C_0/lambda_1). The flow of
the C^(m - 1) field V is C^(m - 1), and its derivatives solve the differentiated equations; so DZ_t applied to a
vector solves this linear equation, and |DZ_t| <= C_1 e^(-lambda_1 t). For 2 <= j <= m - 1, D^j Z_t, applied to fixed
vectors, solves it with the added term -F_j(t), where F_j(t) is a sum of terms
D^i N_B(Z_t)[D^(k_1) Z_t, ..., D^(k_i) Z_t] with 2 <= i <= j, k_1, ..., k_i >= 1 and k_1 + ... + k_i = j, and
D^j Z_0 = 0. By induction on j, the bounds |D^k Z_t| <= C_k e^(-lambda_1 t) for k < j give
|F_j(t)| <= C'_j e^(-2 lambda_1 t) with a constant C'_j, and the variation of constants formula gives
|D^j Z_t| <= C_1 C'_j int_0^t e^(-lambda_1 (t - t')) e^(-2 lambda_1 t') dt' <= C_j e^(-lambda_1 t), with
C_j = C_1 C'_j/lambda_1, for z in U_0 and t >= 0. Hence, by the chain rule, every derivative of order at most m - 1 of
z -> N_B(Z_t(z)) is bounded on U_0 by K_N e^(-2 lambda_1 t) with a constant K_N: N_B(Z_t) by
c_N C_0^2 e^(-2 lambda_1 t), the terms DN_B(Z_t) D^j Z_t by c_N C_0 C_j e^(-2 lambda_1 t), and the others as F_j(t).
Since d(e^(tB) Z_t)/dt = e^(tB)(B Z_t - V(Z_t)) = -e^(tB) N_B(Z_t), |e^(tB)| = e^(lambda_2 t) and
lambda_2 < 2 lambda_1, the map
    nu(z) = lim_(t -> infinity) e^(tB) Z_t(z) = z - int_0^infinity e^(t'B) N_B(Z_(t')(z)) dt'
is defined on U_0 and, by differentiation under the integral sign, C^(m - 1), with D nu(0) = I, since Z_t(0) = 0 and
DN_B(0) = 0. For t_1 >= 0, Z_t(Phi_(-t_1)(z)) = Z_(t + t_1)(z), so nu(Phi_(-t_1)(z)) = e^(-t_1 B) nu(z) for z in U_0.
Choose r_1 in (0, r_0] with |D nu - I| <= 1/2 on the closed disk U_1 of radius r_1 about 0. Then
|nu(z) - nu(z')| >= |z - z'|/2 for z and z' in U_1, so nu is injective on U_1, and by the inverse function theorem
H_Y, the restriction of nu to the open disk U of radius r_1 about 0, is a C^(m - 1) diffeomorphism of U onto an open
neighborhood of 0. Choose r in (0, 1] such that the closed disk D_r of radius r about 0 lies in H_Y(U). For z in U_1
and t <= 0, Phi_t(z) lies in U_1 and nu(Phi_t(z)) = e^(tB) nu(z); since nu is injective on U_1 and
|e^(tB) w| <= e^(lambda_1 t) |w|, it follows that H_Y^(-1)(e^(tB) w) = Phi_t(H_Y^(-1)(w)) for w in D_r and t <= 0. So
R = rho(H_Y^(-1)) is C^(m - 1) on H_Y(U), R >= 0, and R(e^(tB) w) = e^t R(w) for w in D_r and t <= 0. Let P be the
Taylor polynomial of degree m - 1 of R at 0. For fixed t <= 0, the Taylor polynomials of degree m - 1 at 0 of
R(e^(tB) w) and of e^t R(w) are P(e^(tB) w) and e^t P(w), so P(e^(tB) w) = e^t P(w); as e^(tB) multiplies x^i y^j by
e^((i lambda_1 + j lambda_2)t), P consists of monomials x^i y^j of weight i lambda_1 + j lambda_2 = 1, and
P(e^(tB) w) = e^t P(w) for all real t. For 0 < s <= r let eps_R(s) be the supremum of |(R - P)(w)| |w|^(1 - m) over
0 < |w| <= s; it tends to 0 as s decreases to 0, by Taylor's formula. For 0 < |w| <= r and
tau >= 0, (R - P)(w) = e^tau (R - P)(e^(-tau B) w) and |e^(-tau B) w| <= s_tau with s_tau = e^(-lambda_1 tau) r, so,
as e^tau s_tau^(m - 1) <= r^(m - 1) since (m - 1) lambda_1 >= 1,
    |(R - P)(w)| <= e^tau eps_R(s_tau) s_tau^(m - 1) <= eps_R(s_tau) r^(m - 1),
which tends to 0 as tau tends to infinity. So R = P on D_r. The rest of Step 23(vi), from "P != 0" on, now holds with
c = 0, with H_Y, U, D_r and P as here, with psi_t(z) = e^(tB) z, and with (ii) in place of Step 23(iii); it gives N_Y
and shows that d_Y is even.
(vi) The contradiction. Step 23(vii) holds as it stands; it uses only the C^3 regularity of rho. Then Step 23(viii)
applies without its first sentence and without its last sentence, "Hence 1/(2l) is an even integer.", and with the
following replacements: for Y in E_V other than 0, B = DV(Y) is invertible by (iii), in place of Claim 2, and Y is a
saddle as in (iv) or a source as in (v); the neighborhoods N_Y and the numbers d_Y are those of (iv) and (v); and (ii)
replaces Step 23(iii). It gives 2 k_* = 1 + (the sum of the d_Y over the Y in E_V other than 0), where the left side
is even and every d_Y is even by (iv) and (v), a contradiction.
(vii) Conclusion. If 3/16 < l < 1/4 and rho is C^m for an integer m with (m - 1)(2l - 1/4) >= 1, then a_+ a_- < 0 is
impossible, so, with Step 19(v), a nonzero F(e.X) as in Step 14 has a_+ > 0 and a_- > 0. For these l, none of which is
1/(4n) with n >= 2, this is the conclusion of Step 23(ix) under finite regularity. The regularity of rho is used in
the opening, through Step 19(v), and in (i)-(v); l > 3/16 is used in Claim 4 and for lambda_2 < 2 lambda_1 in (iii),
and its consequence l > 1/6 in (ii) and (iv); Claims 3 and 4 replace Claim 2 of Step 23, and the linearization of (v),
which needs lambda_2 < 2 lambda_1, together with the identity R = P, which needs (m - 1) lambda_1 >= 1, replaces the
normal forms of Step 23(vi).
Step 25 (the mixed case for C^infinity profiles at l = 1/(4n)). Let rho, f, h, q, S, mu and u be as in Step 14,
suppose that rho is C^infinity and l = 1/(4n) for an integer n >= 2, so that 0 < l < 1/4, and put p = 1/(2l) = 2n, an
even integer with p >= 4. Suppose that a_+ a_- < 0; replacing e by -e if necessary, let a_+ > 0 > a_-. We derive a
contradiction. Everything in Step 23 before (viii), except the announcement "We show that 1/(2l) is an even integer,
...", holds here with the same proofs, since it uses only that rho is C^infinity, 0 < l < 1/4 and a_+ > 0 > a_-; we
use its notation (Phi_t, R_*, the order of an orbit, a(P), n_P, J, Omega, K_0, N_0, A_0). Claim 2 of Step 23(iv) gives
no information here, as 1/(2l) is an even integer; (iii) below replaces it. The other auxiliary objects of this step
are local to it.
(i) Coordinates at a zero of V at which DV is singular. Claim 5: let Y be a zero of V such that B = DV(Y) is singular,
and let k >= 3 be an integer. Then there are a connected open neighborhood N of Y, inside any given neighborhood of Y,
a number s_* > 0, a C^k diffeomorphism Upsilon of N onto the open square (-s_*, s_*) x (-s_*, s_*) with
Upsilon(Y) = 0 and det D Upsilon = 1 on N, and a C^k function c on an open interval about 0 with c(0) = 0 and
c'(0) = 0, such that for X in N, with (x, y) = Upsilon(X),
    D Upsilon(X) V(X) = (c(x), (2l - c'(x)) y),   (28.12)
that is, in the coordinates (x, y), which are local to (i) and (ii), V is the field
U(x, y) = (c(x), (2l - c'(x)) y). Proof. As tr B = div V = 2l and det B = 0, the eigenvalues of B are 0 and 2l; let
w_0 and w_1 be eigenvectors of B for 0 and 2l. For z = (z_0, z_1) in the plane write
V(Y + z_0 w_0 + z_1 w_1) = G_0(z) w_0 + (2l z_1 + G_1(z)) w_1; then G = (G_0, G_1) is C^infinity on the plane, as
V is, with G(0) = 0 and DG(0) = 0. Fix a C^infinity function chi_c on the plane with chi_c(z) = 1 for |z| <= 2 and
chi_c(z) = 0 for |z| >= 3, and for small delta > 0 let V_delta(z) = (0, 2l z_1) + chi_c(z) delta^(-1) G(delta z). For
|z| <= 2, V_delta is V in the coordinates z given by X = Y + delta(z_0 w_0 + z_1 w_1), with the same time, and
div V_delta = 2l there, as this change of coordinates is affine. V_delta(z) = V_0(z) = (0, 2l z_1) for |z| >= 3, and
for every integer j >= 0 the derivatives of order j of delta^(-1) G(delta z), which are
delta^(j - 1) (D^j G)(delta z), tend to 0 uniformly on |z| <= 3 as delta tends to
0 (for j = 0 and j = 1 since G(0) = 0 and DG(0) = 0); so V_delta tends to V_0 in C^j on the plane for every j. As
V_delta = V_0 for |z_0| >= 3, the field that equals V_delta for |z_0| <= 4 and has period 8 in z_0 is C^infinity; it
defines a vector field on the cylinder (R/8Z) x R, again denoted V_delta, also for delta = 0. The circle
M_0 = (R/8Z) x {0} is invariant under the flow (z_0, z_1) -> (z_0, e^(-2lt) z_1) of -V_0 and normally attracting, with
rate 0 along M_0 and rate -2l normal to it.
Let r = k + 2, and fix eta > 0 with (k + 3) eta < 2l. By the persistence theorem for compact normally hyperbolic
invariant manifolds (N. Fenichel, Persistence and smoothness of invariant manifolds for flows, Indiana Univ. Math. J.
21 (1971), 193-226; Hirsch, Pugh and Shub, loc. cit.), applied to -V_delta, for all small delta > 0 there is a circle
M_delta = {(z_0, h_delta(z_0))} invariant under the flow Psi_t of -V_delta, with h_delta of class C^r,
|h_delta| <= 1 and |h_delta'| <= eta, which is normally attracting with rates within eta of those of M_0: there are a
continuous line field m -> E_m on M_delta, transversal to M_delta and invariant under D Psi_t, and a constant C such
that for m in M_delta and t >= 0
    C^(-1) e^(-eta t) |v| <= |D Psi_t(m) v| <= C e^(eta t) |v|   for v tangent to M_delta at m,
    |D Psi_t(m) w| <= C e^(-(2l - eta)t) |w|   for w in E_m.
So for 0 <= i <= k + 1, m in M_delta and t >= 0, the quotient of |D Psi_t(m) on T_m M_delta|^i |D Psi_t(m) on E_m| by
the minimum norm of D Psi_t(m) on T_m M_delta is at most
C^(i + 2) e^(-(2l - (i + 2) eta)t) <= C^(i + 2) e^(-(2l - (k + 3) eta)t), with 2l - (k + 3) eta > 0. This is the
center bunching condition (11) of J. Eldering, M. Kvalheim and S. Revzen, Global linearization and fiber bundle
structure of invariant manifolds, Nonlinearity 31 (2018), 4202-4245, with k + 1 < r in place of their k. By
their Corollary 2, which rests on N. Fenichel, Asymptotic stability with rate conditions, II, Indiana Univ. Math. J.
26 (1977), 81-93, Theorem 5, and since a compact invariant manifold without boundary is inflowing, the local stable
manifold of M_delta, an open neighborhood W of M_delta, is the union of disjoint curves W_m, m in M_delta, with W_m
meeting M_delta only in m and tangent to E_m there and Psi_t(W_m) contained in W_(Psi_t(m)) for t >= 0, and the map pi
of W onto M_delta with pi = m on W_m is C^(k + 1). Then pi(Psi_t(z)) = Psi_t(pi(z)) for z in W and t >= 0, and
differentiating at t = 0 gives D pi(z) V_delta(z) = V_delta(pi(z)).
The point 0 lies on M_delta. Indeed, let phi_M(z) = V_delta,1(z) - h_delta'(z_0) V_delta,0(z), with V_delta,0 and
V_delta,1 the components of V_delta; phi_M = 0 on M_delta, as V_delta is tangent to M_delta, and the derivative of
phi_M in z_1 tends to 2l uniformly on |z_1| <= 1 as delta tends to 0, so it is >= l there for small delta. As
V_delta(0) = 0, 0 = phi_M(0, 0) - phi_M(0, h_delta(0)) = -h_delta(0) int_0^1 (d phi_M/d z_1)(0, s h_delta(0)) ds, so
h_delta(0) = 0. The flow of V_delta fixes 0 and maps M_delta onto itself, so
DV_delta(0) = diag(0, 2l) (from G(0) = 0, DG(0) = 0) maps the tangent line of M_delta at 0, spanned
by (1, h_delta'(0)), into itself, which gives h_delta'(0) = 0; and as the line field E is invariant, E_0 is an
invariant line of diag(0, 2l) other than the z_0-axis, the z_1-axis. Since pi is the identity on M_delta and constant
on W_0, D pi(0) is the projection onto the z_0-axis along the z_1-axis. Let u_c(z) be the z_0-coordinate of pi(z),
taken in R near 0 with u_c(0) = 0, and v_c(z) = z_1 - h_delta(z_0). Then D(u_c, v_c)(0) is the identity, so (u_c, v_c)
is a C^(k + 1) diffeomorphism of an open neighborhood N_z of 0, inside |z| < 2 and W, onto an open neighborhood of 0.
With c(s) = V_delta,0(s, h_delta(s)), a C^r function with c(0) = V_delta,0(0) = 0 and c'(0) = 0, as
DV_delta(0) = diag(0, 2l) and h_delta'(0) = 0, the identity D pi(z) V_delta(z) = V_delta(pi(z)) gives
Du_c(z) V_delta(z) = c(u_c(z)), and Dv_c(z) V_delta(z) = 0 where v_c(z) = 0, as V_delta is tangent to M_delta.
Let Upsilon_1(X) = (u_c(z), v_c(z)) for X = Y + delta(z_0 w_0 + z_1 w_1) with z in N_z, a C^(k + 1) diffeomorphism of
an open neighborhood of Y onto an open neighborhood of 0, and lambda_A(u_c, v_c) = |det D(Upsilon_1^(-1))(u_c, v_c)|,
a positive C^k function. The map (u_c, v_c) -> (u_c, int_0^(v_c) lambda_A(u_c, s) ds) is C^k with Jacobian determinant
lambda_A(u_c, v_c) > 0 and derivative at 0 invertible, so it is a C^k diffeomorphism of a neighborhood of 0 onto a
neighborhood of 0. Its composition with Upsilon_1 is a C^k diffeomorphism of an open neighborhood of Y onto an open
neighborhood of 0 with first component u_c and Jacobian determinant +1 or -1 at every point. Choose s_* > 0 such that
the preimage N of (-s_*, s_*) x (-s_*, s_*) under it lies in the given neighborhood; N is connected, so the Jacobian
determinant has constant sign on N, and changing the sign of the second component if necessary, we obtain Upsilon with
det D Upsilon = 1 on N and Upsilon(N) = (-s_*, s_*) x (-s_*, s_*). In the coordinates (x, y) = Upsilon(X), x = u_c,
and the set y = 0 is the set v_c = 0, which is invariant. So, writing the field
U = (D Upsilon V)(Upsilon^(-1)) as (U_1, U_2), the identities above give U_1(x, y) = c(x) and U_2(x, 0) = 0. As
Upsilon carries the flow of V to that of U and preserves area, and Phi_t has Jacobian determinant e^(2lt), div U = 2l,
so the derivative of U_2 in y is 2l - c'(x), and as U_2(x, 0) = 0 and Upsilon(N) is a square,
U_2(x, y) = (2l - c'(x)) y. This proves Claim 5.
(ii) Zeros of V in K_0 at which DV is singular. Let Y be a point of K_0 other than 0 with V(Y) = 0 and det DV(Y) = 0.
We show that there is an open neighborhood N' of Y inside Omega such that the zeros of V in N' are the points of an
arc A_Y through Y, the image of an open interval under a homeomorphism, every point of which lies in K_0 and is a zero
of V at which DV is singular. Since Y lies in the open set Omega, Claim 5 with k = 2p gives N, inside Omega, Upsilon
and c; let x_0 > 0 and y_0 > 0 be such that [-x_0, x_0] x [-y_0, y_0] lies in Upsilon(N) and c is defined
on [-x_0, x_0]. The function R(x, y) = rho(Upsilon^(-1)(x, y)) is C^(2p) and >= 0, as rho >= 0 on Omega, and since
V.grad rho = rho,
    c(x) R_x + (2l - c'(x)) y R_y = R   on Upsilon(N).
At x = 0, as c(0) = c'(0) = 0 and 2lp = 1, this gives y R_y(0, y) = p R(0, y), so (R(0, y) |y|^(-p))' = 0 for
0 < |y| < y_0, and R(0, y) = kappa_+ y^p for 0 < y < y_0 and R(0, y) = kappa_- |y|^p for -y_0 < y < 0, with constants
kappa_+ >= 0 and kappa_- >= 0. Since y -> R(0, y) is C^p and p is even, the derivatives of order p at 0 from the right
and from the left, p! kappa_+ and p! kappa_-, agree; let kappa_0 = kappa_+ = kappa_-. Let r(x) = (d_y^p R)(x, 0)/p!
for |x| <= x_0, a C^p function. We show that there are an even integer m with 0 <= m < p and kappa_1 > 0 with
r^(j)(0) = 0 for j < m and r^(m)(0) = m! kappa_1. If kappa_0 > 0, this holds with m = 0 and kappa_1 = kappa_0, as
r(0) = kappa_0. Let kappa_0 = 0. For 0 < |y| < y_0 let Q_y = Upsilon^(-1)(0, y) and L_y = D(Upsilon^(-1))(0, y). As
U(0, y) = (0, 2l y), the line x = 0 is invariant under U, V(Q_y) = L_y (0, 2l y) != 0, and the Q_y with 0 < y < y_0
lie on one orbit of V, as do the Q_y with -y_0 < y < 0; they are zeros of rho, as kappa_0 = 0, and rho >= 0 near them.
By Step 23(iii) these two orbits have even orders m_+ (for y > 0) and m_- (for y < 0) with 2l m_+ < 1 and 2l m_- < 1,
that is, m_+ < p and m_- < p. Let m = min(m_+, m_-). For 0 < y < y_0, D^j rho(Q_y) = 0 for j < m_+, so by the chain
rule for rho composed with the C^(2p) map Upsilon^(-1), the derivatives of R of order less than m_+ vanish at (0, y),
and with e_1 = (1, 0) and e_2 = (0, 1),
    (d_x^(m_+) R)(0, y) = D^(m_+) rho(Q_y)[L_y e_1, ..., L_y e_1] = m_+! a(Q_y) (n_(Q_y).L_y e_1)^(m_+);
here n_(Q_y).L_y e_1 != 0, since L_y e_2 is parallel to V(Q_y) and L_y is invertible. The same holds for
-y_0 < y < 0 with m_- in place of m_+. Let g_m(y) = (d_x^m R)(0, y)/m!, a C^p function on (-y_0, y_0), as 2p - m >= p.
Then g_m(y) = a(Q_y)(n_(Q_y).L_y e_1)^m > 0 for y of the sign whose orbit has order m, and g_m(y) = 0 for y of the
other sign if its order is larger than m; and (d_x^j R)(0, y) = 0 for j < m and 0 < |y| < y_0, hence, by continuity,
for |y| < y_0. Differentiating the equation for R m times in x and putting x = 0, the terms of the derivative of c R_x
contain c(0), c'(0) or a derivative (d_x^j R)(0, y) with j < m, and the terms of the derivative of (2l - c') y R_y
other than (2l - c'(0)) y (d_y d_x^m R)(0, y) contain the derivative in y of some (d_x^j R)(0, y) with j < m; all of
these vanish. So 2l y g_m'(y) = g_m(y), and as at x = 0 above, g_m(y) = kappa'_+ y^p for 0 < y < y_0 and
g_m(y) = kappa'_- |y|^p for -y_0 < y < 0, with kappa'_+ >= 0, kappa'_- >= 0, not both 0. As g_m is C^p and p is even,
kappa'_+ = kappa'_- =: kappa_1 > 0. Since R is C^(2p) and p + m < 2p, the derivatives d_x^j d_y^p R and d_y^p d_x^j R
agree for j <= m, so r^(j)(0) = (d_y^p d_x^j R)(0, 0)/p!, which is 0 for j < m and m! g_m^(p)(0)/p! = m! kappa_1 for
j = m.
By Taylor's formula there is x_1 in (0, x_0] with r(x) >= kappa_1 x^m/2 > 0 for 0 < |x| <= x_1, m being even.
Differentiating the equation for R p times in y and putting y = 0 gives
c(x) p! r'(x) + (2l - c'(x)) p p! r(x) = p! r(x), that is, as 2lp = 1, c r' = p c' r on [-x_0, x_0].
Where r > 0, (c r^(-1/p))' = r^(-1/p - 1)(c' r - c r'/p) = 0, so c(x) = C_+ r(x)^(1/p) for 0 < x <= x_1 with a
constant C_+. As c(0) = c'(0) = 0 and c is C^2, |c(x)| <= C_c x^2 for |x| <= x_0 with a constant C_c, so
|C_+| <= C_c x^2 (kappa_1 x^m/2)^(-1/p) for 0 < x <= x_1, which tends to 0 as x decreases to 0, since m/p < 1; so
C_+ = 0. In the same way c = 0 on [-x_1, 0). So c = 0 on [-x_1, x_1], and U(x, y) = (0, 2l y) on the
rectangle (-x_1, x_1) x (-y_0, y_0). Let N' = Upsilon^(-1)((-x_1, x_1) x (-y_0, y_0)), an open neighborhood of Y in
Omega. The zeros of V in N' are the points Upsilon^(-1)(x, 0) with |x| < x_1; they form an arc A_Y as stated, since
Upsilon^(-1) is a homeomorphism. At each of them DV is similar to DU = diag(0, 2l), so it is singular, and as a zero
of V is a zero of rho = V.grad rho, each of them is a zero of rho in Omega, so it lies in K_0.
(iii) The zeros of V in K_0 are nondegenerate. Let E_s be the set of the zeros Y of V in K_0 with det DV(Y) = 0. It is
closed in the compact set K_0, so it is compact, and 0 is not in it, since det DV(0) = det A = beta/2 < 0. Suppose
that E_s is not empty. By (ii), each Y in E_s has an open neighborhood N' with E_s meeting N' exactly in A_Y, which is
homeomorphic to an open interval; so E_s is a nonempty compact one-dimensional manifold without boundary. Let C be a
component of E_s. As E_s is locally connected, C is open and closed in E_s, so it is a compact connected
one-dimensional manifold without boundary, which is homeomorphic to a circle; so C is a Jordan curve. Let Omega_C be
the bounded component of the complement of C. As V = 0 on C, each Phi_t fixes every point of C, so it maps the
complement of C homeomorphically onto itself and its components onto components; Phi_t(Omega_C) is a bounded
component, as it lies in the compact set Phi_t(Omega_C union C), so Phi_t(Omega_C) = Omega_C. But Phi_1 has Jacobian
determinant e^(2l), so the area of Phi_1(Omega_C) is e^(2l) times the area of Omega_C, which is positive and finite, a
contradiction. Hence E_s is empty: DV(Y) is invertible at every zero Y of V in K_0.
(iv) The contradiction. Step 23(viii) applies without its first sentence, "Suppose that 1/(2l) is not an even
integer.", and without its last sentence, "Hence 1/(2l) is an even integer.", and with "by (iii) of Step 25" in place
of "by Claim 2": for Y in E_V other than 0, B = DV(Y) is invertible by (iii). Its other statements use only the
opening of Step 23, the first two sentences of Step 23(iv) (B = DV(Y) is symmetric, with trace 2l), Step 23(iii)
and Step 23(v)-(vii), which hold here. It gives 2 k_* = 1 + (the sum of the d_Y over the Y in E_V other than 0), where
the left side is even and every d_Y is even by Step 23(v) and (vi), a contradiction.
(v) Conclusion. If rho is C^infinity and 0 < l < 1/4, then a_+ a_- < 0 is impossible: by Step 23(ix) if l is not
1/(4n) for an integer n >= 2, and by (iv) if it is. So, with Step 19(v), a nonzero F(e.X) as in Step 14 has
a_+ > 0 and a_- > 0, without the exception of Step 23(ix). The C^infinity regularity of rho is used as in Step 23 and,
in (ii), through Claim 5 with k = 2p; (iii) replaces Claim 2 of Step 23.
Step 26 (the exponent of a mixed limit for 1/4 < l <= 5/12). Let rho, f, h, q, S, mu and u be as in Step 14, and
suppose that 1/4 < l <= 5/12. By Steps 14, 16 and 17, a_+ a_- < 0, so the setting of Step 15 applies; let Phi_t be
the flow of V. We show that mu = 2l - 1/gamma <= 0, that is gamma <= 1/(2l). Put d = 2l, so that 1/2 < d < 1,
write s = e.X and z = e-perp.X, and let J(v_1, v_2) = (-v_2, v_1). All auxiliary constants of this step are chosen
anew.
(i) Bounded forward orbits of regular zeros. Let P be a point with rho(P) = 0, V(P) != 0 and
grad rho(P) != 0. Since V.grad rho = rho, grad rho(P) is orthogonal to V(P), so grad rho(P) = c_P JV(P) with a real
c_P != 0. Let L_t = D Phi_t(P). Differentiating rho(Phi_t X) = e^t rho(X) at P gives
L_t^T grad rho(Phi_t P) = e^t grad rho(P). Every invertible real 2 x 2 matrix L satisfies L^T J L = (det L) J, so
L^(-T) J = J L/det L; moreover L_t V(P) = V(Phi_t P), and det L_t = e^(dt) (Step 15). Hence
    grad rho(Phi_t P) = c_P e^((1 - d)t) J V(Phi_t P)   for t >= 0,
and, with r(t) = |Phi_t P| and the class bound |grad rho| <= C(1 + r)^(gamma - 1) of Section 2,
|V(Phi_t P)| <= (C/|c_P|) e^(-(1 - d)t) (1 + r(t))^(gamma - 1). Since |dr/dt| <= |V(Phi_t P)| almost everywhere,
d/dt (1 + r)^(2 - gamma) <= (2 - gamma)(C/|c_P|) e^(-(1 - d)t) almost everywhere on [0, infinity), and the right side
is integrable there because d < 1. As 2 - gamma > 0, r is bounded on [0, infinity).
(ii) Zeros far out. Fix theta with q/gamma < theta < 1. For z > 0 the points z e-perp + z^theta e and
z e-perp - z^theta e have the densities a_+ z^(gamma theta) + h and a_- z^(gamma theta) + h, with |h| at most
C_h (1 + 2z)^q for z >= 1; since a_+ a_- < 0 and gamma theta > q, these have opposite signs for z large, so the
segment between the two points contains a zero of rho. At a zero X of rho, |f(X)| = |h(X)| and (28.9) give
|s| <= C(1 + |X|)^(q/gamma); since q/gamma < 1, there is z_0 >= 1 such that |X| <= 2z for every zero X of rho with
z >= z_0.
(iii) Conclusion. Suppose that mu > 0. By Step 14, V = SX + W_2[f] + u with S e-perp = mu e-perp, |W_2[f]| <= |f| and
|u(X)| <= C(1 + |X|)^q log(2 + |X|), so at a zero X of rho with z >= z_0
    e-perp.V(X) >= mu z - C_h (1 + 2z)^q - C(1 + 2z)^q log(2 + 2z).
Enlarging z_0, we get e-perp.V(X) >= mu z/2 > 0 for all such X, and by (ii) we may take a zero P of rho with
e-perp.P >= z_0. The forward orbit of P consists of zeros of rho, since rho(Phi_t P) = e^t rho(P) = 0, so
z(t) = e-perp.Phi_t P satisfies dz/dt >= mu z/2 as long as z(t) >= z_0; hence z(t) >= z(0) e^(mu t/2) for all
t >= 0, and the forward orbit of P is unbounded. But V(P) != 0, so Step 17(i), which applies because
1/4 < l <= 1/2, a_+ != 0, a_- != 0 and q mu < 1, gives grad rho(P) != 0, and (i) makes the forward orbit of P bounded.
This contradiction shows that mu <= 0, that is gamma <= 1/(2l); for l = 1/4 + 1/(2n) this reads gamma <= 2n/(n + 2).
No regularity beyond that of the class is used; in particular C^infinity is not assumed.
