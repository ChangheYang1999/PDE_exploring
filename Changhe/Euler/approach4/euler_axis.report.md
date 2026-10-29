# Backward self-similar axisymmetric Euler profiles with swirl for 1/2 < c_l < 3/4: final report

Status: final. Outcome label C (unsuccessful numerical search) for 1/2 < c_l < 3/4; separate label D (rigorous obstruction)
for uniformly decaying Cartesian C^2 axisymmetric profiles on R^3 with 0 < c_l < 1/2; the smooth case c_l = 1/2 is open.
No existence theorem, no nonexistence theorem for c_l > 1/2 and no accepted numerical candidate was obtained.

Run record. Campaign start T0 = 2026-10-28T17:59:44Z (logged). The team was stopped at 2026-10-29T16:44:44Z, 22 h 45 min into
the 24-hour budget, so that this write-up finishes inside it; the write-up ended at T_end = 2026-10-29T17:02:05Z, 23 h 2 min after T0.
Stages I, II and III (including the protected Stage III validation) were completed; times and resources are in section 8.

## Summary

- Main question (did this search obtain convincing numerical evidence for a nontrivial, smooth, globally decaying axisymmetric profile
  with nonzero swirl and c_l > 1/2?): no. Label C. In 526 finished search runs (starting c_l from 0.505 to 0.74, free-c_l
  continuations, ball degrees 24 to 64; section 4) and the closed-formulation solves, no state met label A (among its
  conditions A1 rho_max <= 1e-6, A2 m_max <= 1e-4, A7 pressure, A8 interface jumps, A9 identities) or the pre-candidate
  condition B1 (rho_max <= 1e-3 at two resolution levels). The thresholds were registered before any candidate existed
  and never changed. This does not establish nonexistence.
- Independently measured values (floating point, by a separate implementation; all states are approximations, not
  solutions): smallest rho_max = 1.79 at c_l = 0.749, the imposed bound of its run (interface jump 4.8e-3 against 1e-6);
  2.34 at c_l = 0.745; 2.71 at c_l = 0.74 (2.74, 2.71, 2.84 at ball degrees 36, 48, 64, so no decrease with resolution).
  These are order-one residuals, three orders of magnitude above B1.
- Closed single-source formulation (4.5, C^3 velocities from C^4 spline potentials): smallest closure defect E = 0.032 at c_l = 0.74 with 1855 coefficients, against the
  handoff criterion E <= 1e-2 at two consecutive levels; Gauss-Newton stalled. Certified: the single-source stagnation
  portrait of all ten saved nested fields (interval enclosure), and an exact certificate that the stored matrix approximating
  the derivative of the fixed-point map admits no positive constant damping contractive in the solver norm (open for the
  exact map).
- Proved, label D (3.1): for 0 < c_l < 1/2 every Cartesian C^2, uniformly decaying, axisymmetric profile on R^3 is zero,
  without assuming U(0) = 0 (the argument of Constantin, Ignatova and Vicol, arXiv:2602.17570, Theorem 4.5, with decay
  used at the Liouville step). For every c_l > 0 a nontrivial decaying Cartesian C^2 axisymmetric profile has nonzero swirl.
- Proved, c_l = 1/2 (3.3): a swirling decaying C^2 profile needs uncountably many meridional stagnation points carrying an
  interval of circulation values; real analytic decaying profiles are trivial. Numerically no state below rho_max 4.7 was
  found at c_l = 1/2 (primary search).
- Proved structure for c_l > 1/2 (3.4 to 3.14): W_m . grad Gamma = (2 c_l - 1) Gamma, so all swirl is emitted from zeros of
  the meridional transport field; a swirl-carrying axis zero has d_r U^r = -1/2 exactly and is a hyperbolic source with
  rates c_l - 1/2 and c_l + 1 (3.4); further necessary conditions on the stagnation portraits hold under the hypotheses
  stated in 3.4a to 3.14. None excludes any subinterval of 1/2 < c_l < 3/4 (3.2: the circulation weight
  e^{(1 - 2 c_l) tau} grows backward, so the c_l < 1/2 argument has no analogue).
- Remaining gap. Existence for 1/2 < c_l < 3/4 is open in both directions. Numerically, the first failed condition is B1
  (best 1.79 against 1e-3), and in the closed formulation E <= 1e-2 (best 0.032). Mathematically, no inequality excluding the
  target class is known; the near-critical criterion of 3.10 (ii) would exclude only families with uniform shape constants
  C and I_G, which are not established, and it excludes nothing at fixed c_l > 1/2.
  At c_l = 1/2 the missing step is to exclude a smooth non-analytic profile whose stagnation set is uncountable and carries an
  interval of circulation values (finiteness of the stagnation set is proved only for real analytic fields, and an explicit
  smooth divergence-free field shows that smoothness alone does not give it).
- Most promising next experiment (7.5): continue the nested Newton-Krylov solve of the closed single-source problem at
  c_l = 0.74 and 0.68 with a changed method or trial space; second option, a fractional S1-pair search.
- Checks: an independent verifier (separate code) audited the claim groups described below, with the stated coverage limits,
  and confirmed labels C and D and the open status of c_l = 1/2; an external referee (a second model) checked derivations, and its results are used as claims.
  The edits made after the team stop (this summary, the run record and the description of the accompanying artifacts in 9)
  restate audited results and were not re-audited by that verifier.

## 1. Outcome

Label C for the main search, 1/2 < c_l < 3/4: an unsuccessful numerical search. No tested state met the acceptance
conditions of label A or the pre-candidate condition B1 (scaled RMS residual rho_max <= 1e-3 at two resolution levels). This
does not establish nonexistence. The main measurements:
- The smallest independently measured value is rho_max = 1.79 [verifier, floating point], an order-one equation residual in the
  origin region, for a state at c_l = 0.749, the imposed upper bound of the free-c_l run it descends from; the same state fails
  the interface-jump test (4.8e-3 against 1e-6), and its saved first nonlinear far-field correction has relative mismatch
  0.025 with the one forced by the equations (sections 5 and 6).
- Below that bound the smallest independently measured value is rho_max = 2.34 at c_l = 0.745 [verifier, Stage III], for a
  state of a fixed-c_l continuation from the 0.749 state (primary value 2.37, the smallest primary value below c_l = 0.7485
  [primary search; figure data audited by the verifier]); it also fails A2 (m_max 11.5) and A8 (largest relative interface
  jump 1.3e-3). A free-c_l run that stopped at its imposed upper bound 0.745 is registered at 2.70 [verifier, Stage III].
- At c_l = 0.74 the smallest independently measured value is rho_max = 2.71 [verifier], for a ball-degree-48 state. The
  registered values of the direct-seed branch at that c_l are 3.59 and 2.74 at ball degree 36 (after 1500 and 3000
  iterations), 2.71 and 2.78 at degree 48 and 2.84 at degree 64 [verifier], and
  the primary values are 2.86, 2.81 and 2.95 at degrees 36, 48 and 64 [primary search], so the value does not decrease
  materially with resolution; it depends at order one on the outer interface position, on the shell weights and on steps of
  0.005 in c_l.
- At c_l = 0.68 the smallest primary value is 3.37 (ball degree 48) [primary search], and the degree-36 state with primary
  value 3.38 measures 5.10 under the verifier's registered evaluation [verifier] (4.4a, 4.6).
- In the closed single-source formulation (4.5) the smallest relative closure defect reached is E = 0.032 at c_l = 0.74,
  with 1855 coefficients after angular and radial refinements, in a C^4 spline trial space; Gauss-Newton stalled there, and
  iteration of the frozen-source fixed-point map did not lower E [independent referee, floating point; lead-checked from the
  saved grids]. An independent fixed-K transport reproduces E for this field and for the nine other saved nested fields, and
  the single-source portrait of all ten is certified by interval enclosure. An exact certificate shows that the stored matrix
  approximating the derivative of the fixed-point map admits no positive constant damping that is contractive in the
  solver's coordinate norm; the corresponding statement for the exact map is open [verifier].

The searched range, initializations, resolutions,
budget and failure mechanisms are given in sections 4 (summary table in 4.6), 7 and 8, and the most promising next numerical experiment in 7.5.

Separately reported rigorous result (label D for its class): no nontrivial Cartesian C^2, uniformly decaying,
axisymmetric profile exists for 0 < c_l < 1/2, without the normalization U(0) = 0 (section 3.1).

The case c_l = 1/2, studied separately: a decaying swirling C^2 profile would need uncountably many meridional stagnation points
carrying an interval of circulation values, so real analytic decaying profiles at c_l = 1/2 are trivial; smooth non-analytic
profiles remain open (3.3, 3.10). Numerically, the runs at c_l = 1/2 found no state with rho_max below 4.7, and none below 12.5
among the ball-degree-24 runs that kept the swirl (4.3) [primary search; verifier audit of the saved run records]. The exported
state of that run measures 14.4 under the registered evaluation, with core and far swirl fractions 0.12 and 0.053; its
ball-degree-32 level measures rho_max 7.47 and m_max 32.9, with fractions 0.088 and 0.057 (the core fraction reduced, the far
fraction slightly above 0.053; it passes the magnitude filter) [verifier]; and 2000 further iterations at degree 24 brought the
swirl below the filter (core and far fractions 0.060 and 0.032) [primary search; scalar arithmetic checked by the verifier from
the saved records].

Independent check of the labels. A final claim audit of this report by the independent validation (all 21
claim groups, checked against its proofs, its evaluations of the frozen coefficients and the logs; report state of
2026-10-29T12:58Z) found no unresolved corrections. It confirms label C for the search on 1/2 < c_l < 3/4 and the separate
label D for uniformly decaying Cartesian C^2 axisymmetric profiles with 0 < c_l < 1/2; it finds the smooth case c_l = 1/2
open, with the real analytic subclass excluded under the proved hypotheses; and it finds labels A and B refuted for the saved
approximations by their measured failures [verifier, Stage III].

Provenance tags. [verifier]: proved or reproduced by the independent validation; its evaluator is a separate implementation written from the
exchange-format description and the stated equations (section 6 states which later audits inspected primary code). [primary search]: measured by the
primary numerical search and not independently reproduced unless stated. [independent referee]: derived or computed by an
external referee, a second model consulted with self-contained questions and running its own code on the same machine; such results are treated as claims and checked as stated. [lead]: a
derivation or check by the authors of this report. [verified: ...] lists the sources that checked a statement independently;
[verified] alone marks a statement checked by the lead and the independent validation. Each tag also says whether the evidence is a proof, an exact symbolic or
rational certificate, or a floating-point computation. Statements described as proved are supported by complete arguments in the accompanying
artifacts or by independent proofs recorded in the validation evidence. Where the accompanying artifacts give only an outline,
the complete independent proof archive is not included.

## 2. Problem and function class

Profile equations (1 - c_l) U + (c_l y + U) . grad U + grad P = 0, div U = 0 on R^3, from u = tau^{c_l - 1} U(x / tau^{c_l}).
Class of the prompt: axisymmetric, nonzero swirl, U globally C^2 or smoother as a Cartesian field (no axis or origin
artifacts), uniformly decaying with U = R^{-alpha} F(vartheta) + o(R^{-alpha}), alpha = (1 - c_l)/c_l, F not identically zero;
U(0), parity, finite energy not imposed. The smooth stratum consists of the profiles with phi and q smooth functions of (r^2, z) (in the stream gauge psi(0, z) = 0 this is equivalent to U in C^infinity). Each finite expansion in polynomials of (r^2, z) defines a smooth Cartesian field;
general smooth fields require approximation, and limits in a finite-order norm can have finite regularity only. Section 3.14
shows that the C^2 class is genuinely larger at saddles that receive swirl.
Notation: cylindrical coordinates (r, theta, z), s = r^2, R = |y|, and mu = z/R the cosine of the polar angle (mu is used for
nothing else). Reduced unknowns: the meridional potential phi with U^r = -r d_z phi and U^z = 2 phi + r d_r phi, the swirl
q = U^theta / r, and the azimuthal vorticity eta = Omega^theta / r = -Delta_5 phi, where
Delta_5 = d_rr + (3/r) d_r + d_zz = 4 s d_ss + 8 d_s + d_zz is the Laplacian of R^5 acting on functions of (r, z). With
W = c_l y + U and its meridional part W_m = (c_l r + U^r, c_l z + U^z), the profile equations reduce to
    R_q = W_m . grad q + (1 - 2 d_z phi) q = 0,      R_eta = (1 + c_l) eta + W_m . grad eta - d_z(q^2) = 0,
and an exact reduced solution with the stated regularity and differentiated decay solves the primitive equations with the
full-space Newton pressure (3.7). The far-field angular profiles are written q ~ R^(-1/c_l) B(mu) and
eta ~ R^(-1 - 1/c_l) E(mu).
Residual metrics. For each equation (momentum components, R_q, R_eta, divergence, and the elliptic relation) and each dyadic
shell, rho is the RMS of the residual divided by the smaller of the RMS of the linear damping part and of the nonlinear part of
that equation (with two exceptions: the elliptic relation is divided by RMS(eta) and the divergence by the RMS of the Frobenius
norm of DU; the three momentum components share the vector denominator built from (1 - c_l) U and (U . grad) U), and m is the maximum of the residual divided by the same quantity; rho_max and m_max are the maxima over all
equations, the origin ball, 18 dyadic shells and three point sets (Gauss, random, axis collar). All are evaluated in the
reporting dilation gauge (unit L2 norm of the leading far-field coefficient on the sphere); a_eff is the vorticity half-maximum
radius. The thresholds of labels A and B were registered before any candidate existed and never changed. Label A needs, among
other conditions, A1 rho_max <= 1e-6, A2 m_max <= 1e-4, A7 agreement of the per-mode Green-function pressure with direct
free-space quadrature to 1e-6 relative at 20 or more points and pressure monopole and dipole coefficients consistent with
zero within the registered tolerances after subtraction of the locally forced terms, interface jumps at most 1e-6 relative
(A8), and the energy-flux,
vorticity-maximum, swirl-maximum and stagnation identities (A9); label B needs B1 rho_max <= 1e-3 at two resolution levels
improving by at least a factor 2, B2 core and far swirl fractions at least 0.05 and stable to 10 percent, B4 pressure agreement,
Taylor residuals and interface jumps at most 1e-3, and B5 stability of a_eff and of the vorticity-maximum location to 10
percent. The complete rules, and the interface-jump measure (derivatives of phi up to total order 3 and of q up to order 2,
each relative to the local scale of the same derivative, at least 64 angular points per interface), are in the accompanying
specification. Details of the formulation are in the accompanying formulation and origin-and-axis documents.

## 3. Mathematical results

3.1 Obstruction below one half. [proof: lead, verifier, independent referee] (Accompanying audit,
Proposition 1.) The theorem of Constantin, Ignatova and Vicol (arXiv:2602.17570v3, Theorem 4.5) assumes U(0) = 0
and power-law bounds; its proof, with decay replacing U(0) = 0 at the final Liouville step, shows that for
0 < c_l < 1/2 a Cartesian C^2, uniformly sublinear axisymmetric profile is a constant axial vector, hence zero if it
decays. By the same argument every nontrivial decaying Cartesian C^2 axisymmetric profile, for any c_l > 0, has nonzero swirl
(without decay, U = K e_z with P = -(1 - c_l) K z is an exact swirl-free profile). The statement concerns exact,
isotropic, time-independent profiles on all of R^3. Outside it are solutions in domains with boundaries (backward orbits can
then come from the boundary), fields without global Cartesian C^1 regularity with continuous circulation and locally bounded
eta (C^2 suffices), fields that are not uniformly sublinear, and anisotropic, local, asymptotic or only approximate
self-similarity (accompanying audit, section 3).

3.2 Why 1/2 < c_l < 3/4 is not excluded. [verified] The circulation weight e^{(1 - 2 c_l) tau} grows backward, so the
characteristic argument gives no restriction. No exclusion of the full target class was established in this campaign.

3.3 c_l = 1/2. [verified: lead, verifier, referee] A swirling decaying C^2 profile needs uncountably many meridional
stagnation points carrying a nondegenerate interval of circulation values; with countably many (for example, all
nondegenerate) the profile is trivial. For real analytic fields the stagnation set is always finite (for every c_l > 0;
the weighted area expansion excludes closed zero curves and zero arcs ending on the axis), so a real analytic decaying
profile at c_l = 1/2 is trivial. [analytic case: verifier proof, lead review] Open for smooth non-analytic profiles. The
analyticity cannot be traded for smoothness in the finiteness step: an explicit C-infinity, compactly supported,
divergence-free axisymmetric field with nonzero swirl has W_m = 0 on a whole meridional segment at c_l = 1/2 (it is not an
Euler profile; its eta residual on the segment is 9z). [verifier proof, lead check]

3.4 Structure of swirl-carrying profiles for c_l > 1/2. [Lemmas 2 to 4 and Proposition 6: lead, independent referee,
verifier (independent proofs of the local statements with exact local tests)] The meridional transport field
W_m = (c_l r + U^r, c_l z + U^z) has no periodic orbits, polycycles or sinks (the weighted area r dr dz expands at
rate 3 c_l); backward orbits are bounded, and for an exact profile every alpha-limit set consists of zeros of W_m (it is a single zero if the zero set is finite). The circulation Gamma = r U^theta satisfies
W_m . grad Gamma = (2 c_l - 1) Gamma, so all swirl is emitted from zeros of W_m. At an off-axis zero q = 0 and eta = 0. At
an axis zero carrying swirl (S1) d_r U^r = -1/2 exactly, so the zero is a hyperbolic source with rates c_l - 1/2 and
c_l + 1; other swirl emitters are axis sources with q = 0 there (S2: q ~ r^(2j), d_r U^r = -(1 + 2 j c_l)/(2(j + 1))) and
off-axis sources with prescribed eigenvalues (S3). In the reflection class with odd swirl the origin cannot emit
swirl as a hyperbolic source (Corollary 7, verifier-confirmed for smooth fields). Non-hyperbolic zeros are not
classified. These are necessary conditions, used to shape initializations and as diagnostics. The S2 jet classification
(j a positive integer) and the Taylor-jet statements of 3.5, 3.11 and 3.12 (ii) to (v) are made in the smooth stratum; they are
not asserted for arbitrary Cartesian C^2 fields.

3.4a Two further exclusions. [independent referee; lead-checked and generalized; verifier-confirmed with standalone
proofs, the first in the Cartesian C^2 class by a maximum-principle and Hopf-lemma argument] (i) In a
reflection-symmetric profile (z -> -z, either parity of the swirl) whose swirl satisfies d_z(q^2) <= 0 for z > 0, the
axial strain at the origin is compressive: d_z phi(0, 0) < 0. The proof combines the invariance of the plane z = 0,
the characteristic formula for eta, and the maximum principle with the Hopf lemma for the auxiliary potential
int_0^1 t U^z(t r, z) dt on the upper half of R^5 (the five-dimensional Green representation of phi gives the same sign when it
converges absolutely). Hence such a profile has no
swirl-emitting source at the origin, and in the class with even swirl and q(0) != 0 no profile has |q| nonincreasing
away from the symmetry plane, for any c_l > 0. (ii) There is no sequence of smooth exact profiles with an S1 source at the origin such that c_n -> c_* > 0, phi_n -> phi_* in C^3 on compact sets in the regular meridional variables (with smooth axis extensions), q_n -> 0 in C^1_loc and |U_n(y)| <= C (1 + |y|)^(-a) with common C and a > 0. This is a compactness obstruction: a small source amplitude of an individual profile, or a sequence without these controls, is not excluded. Neither statement excludes any subinterval of
1/2 < c_l < 3/4.

3.4b Swirl on the symmetry axis. [axis matching computation: independent referee; general statement and proof: lead;
confirmed by an independent standalone proof for the smooth stratum] Suppose U is smooth (phi, q, eta smooth functions of
(r^2, z) near the axis) and every zero of W_z(0, .) on the axis is simple. Then either q vanishes on the whole
axis, or every axis zero that repels along the axis has q0 != 0 and v = -1/2 (an S1 source when c_l > 1/2), all S1 sources on the axis have the same value
q0 of q, q(0, z) has the sign of q0 at every z except the axis zeros that attract along the axis, where it vanishes, each
of even order k = 1 + (1 + c_l)/kappa (kappa the axial contraction rate), and, under the differentiated far-field bounds, the polar
far-field amplitudes of q are nonzero with the sign of q0. In particular, whenever q(0, .) is odd in z (for example odd swirl in the reflection class), q vanishes on the axis and no
axis zero emits swirl as an S1 source; off-axis swirl is not excluded. Degenerate axis zeros are not covered. Separately,
for c_l > 1/2 the circulation vanishes on every orbit that converges in forward time to a zero of W_m. The equal-amplitude and
even-order conclusions match derivatives of order k of q and k - 1 of eta at the attracting zeros and need the smooth hypothesis:
in the Cartesian C^2 class with a fractional saddle exponent 2 < k < 3, axial transport data and exact local C^2 Euler solutions
glued across the saddle allow independent amplitudes on the two sides (independent verifier construction, local and axial only;
no global decaying example is known). In the reflection class with even swirl the two amplitudes of an S1 pair are equal by
symmetry.

3.5 Local structure at a swirl-emitting axis source. [formal Taylor theory: independent referee with exact
arithmetic, lead re-check at c_l = 3/5; curvature relation: verifier, lead re-derived symbolically] At an S1 source the
formal Taylor series exists to all orders for every c_l in (1/2, 3/4), with free data c_l, the source position z0,
q0 = q(0, z0) and one axis coefficient of phi per order; the recurrence imposes no restriction on these freely chosen
data and forces no logarithms, so local analysis selects neither q0 nor c_l (formal solvability only; convergence is
not claimed). [verifier: independent all-order proof, 41 exact tests] If q_z vanishes at the source,
4(c_l - 1/2)(c_l + 1) q_rr + [(c_l + 1)^2 + q0^2] q_zz = 0, so the source is a saddle or a degenerate critical point
of q (a degenerate strict local maximum is not excluded at the level of formal jets). Outward along each axis branch
from the source |q| grows exactly where d_z phi(0, z) > 1/2, and W_z eta = 2 q (q - q0) along each axis branch from the source on which q does not vanish and W_z(0, z) vanishes only at the source; if the upper (lower) branch reaches infinity and the far-field expansion holds with differentiated
remainders, the polar amplitudes satisfy c_l E(+1) = -2 q0 B(+1) (c_l E(-1) = 2 q0 B(-1)). Because a decaying phi has no
harmonic part on R^5 and the Green integrals converge under that expansion, the S1 conditions are equivalent to two weighted moments of the azimuthal vorticity (the second
says that eta is, in a weighted sense, positive above the source and negative below). [moment identities: lead,
numerically checked on a test field; verifier confirmed constants and signs]

3.6 Exact identities used as diagnostics. [referee symbolic script rerun by the lead; partly re-derived by hand; the
verifier's independent tests: 43 checks of the weighted circulation identity and the axial first integral, 46 global-diagnostic checks (q-maximum, Bernoulli, energy
and helicity finite parts, 5D eta norm, virial) and nine axis-moment cases; the single-source sign rule is
verifier-confirmed under explicit uniform differentiated far-field bounds] Weighted circulation identities, a Bernoulli-Lyapunov function
H = |U|^2/2 + P + c_l y . U + c_l (2 c_l - 1)|y|^2/2 with W . grad H = (2 c_l - 1)|W|^2, energy and helicity finite-part
identities, a convergent virial identity, a five-dimensional eta-norm identity, and the swirl-maximum
condition U^r/r = -1/2 at the maximum of |q|. The global identities need a differentiated matched far-field expansion,
stronger than the leading-order statement of section 2, and hold in stated ranges: zero energy finite part for
1/2 < c_l < 3/5, zero helicity finite part for 1/2 < c_l < 3/4, the eta-norm identity for 1/2 < c_l < 2/3. None of
them excludes any subinterval of 1/2 < c_l < 3/4. The energy-flux identity of the task specification,
(5 c_l - 2) int_{B_R} |U|^2/2 dy = int_{dB_R} [(|U|^2/2 + P) U . n + c_l R |U|^2/2] dS, holds on every ball for every C^1
profile (it is the divergence form of U . (profile equation)); for the leading tail int_{B_R} |U|^2 dy =
R^(5 - 2/c_l) ||F||^2_{L2(S^2)}/(5 - 2/c_l) + lower order, both sides then equal c_l R^(5 - 2/c_l) ||F||^2/2 at leading order
(the pressure and cubic flux terms are smaller by R^(-1 - alpha)), and the kinetic energy diverges for c_l > 2/5, so finite
energy is not imposed [lead symbolic; verifier balance tests, section 6]. Each is reported as a relative defect for a candidate when its
hypotheses hold and is marked not applicable otherwise (accompanying formulation document, section 6).

3.7 Far field and pressure. [lead symbolic checks, referee, verifier tests] Leading term, first nonlinear correction,
removable resonances at c_l = 2/3 and 1/2, a logarithmic resonance at c_l = 3/5 (within a formal power-log expansion, whose existence is not proved, the logarithm then propagates to nonresonant degrees), vanishing irrotational dipole and
pressure monopole/dipole for 1/2 < c_l < 3/4 (c_l != 2/3). Under global regularity and the differentiated decay
|U| = O(R^(-alpha)), |DU| = O(R^(-alpha - 1)), the full-space Newton pressure is well defined and an exact reduced solution
solves the primitive equations with this pressure, up to an additive constant (accompanying far-field and pressure
documents). The statements about absent dipole and pressure terms are likewise conditional on a differentiated matched expansion, and forced local and logarithmic terms are subtracted before independent homogeneous coefficients are identified; at a resonance the subtracted particular solution and its logarithm scale must be stated, since subtracting only the forced logarithm leaves a homogeneous coefficient that contains an exterior constant of the Green formula (accompanying pressure document) [verifier proof with exact symbolic checks; lead symbolic cross-check].
At c_l = 1/2 the resonant pressure dipole is fixed globally [verifier proof; lead symbolic cross-check]: for a globally
smooth decaying profile with U = R^-1 F + R^-3 H + O(R^(-3-eps)) (differentiated through order three) the Newton pressure
has the dipole coefficient Q_1 = <mu N_R - F_R F_z>, the continuous extension of the formula for c_l > 1/2 (N is the leading
coefficient of (U.grad)U and <g> = (1/2) int_{-1}^{1} g(mu) dmu the angular mean), and the order R^-3 momentum balance is a necessary coefficient
condition H = G with G computed from F. For a piecewise field, outside the outermost interface the pressure of the full distributional stress (including the interface jump layers) and the Newton pressure of the bulk stress alone differ exactly by C0/R in the spherical mean and by C1/R^2 in the dipole moment, (P_stress - P_bulk)_0 = C0/R and (P_stress - P_bulk)_1 = C1/R^2; equivalently the bulk pressure carries the monopole -C0/R and the dipole coefficient Q_1 - C1, where C0 and C1 are moments of the interface traces; this is an identity for a fixed
approximation, not an obstruction [verifier proof; lead symbolic cross-check]. If on a radial piece the potential and the swirl
variable have Legendre degree at most N and M in mu, the bulk pressure source tr(DU^2) there has Legendre degree at most
D = 2 max(N,M) + 2; if this holds on every radial piece, the Newton pressure of the bulk source has no modes above D, and
Gauss-Legendre projection with n nodes is exact in exact arithmetic for retained degrees L with 2n - 1 >= D + L [verifier
proof; lead cross-check by an independent Cartesian construction]. The bound is sharp (phi = R^2 z^N and q = R^2 z^M attain it)
but not always attained (phi = 0, q = z^16 on an annulus has M = 16 and source -2 z^32 of degree 32), so a pressure truncated at degree 32
can omit source modes when max(N,M) > 15, and whether it does depends on the nonzero source coefficients [verifier proof;
lead check]. For each of the 13 exported states with c_l > 1/2 examined (the exports existing at the time of that computation) the top source coefficient at R = 1, computed exactly from the stored
binary coefficients, is nonzero at degree 50, 66 or 88, so their bulk Newton pressure has nonzero modes above degree 32; these
Legendre coefficients are small (about 1e-11 to 6e-9 at degree 50, 7e-21 to 2.5e-19 at degree 66, 1e-25 at degree 88) and give
no lower bound on the pressure error, and the critical-exponent state has degree 26 [verifier exact computation; lead
recomputation of the formula and of two of the exports]. This bounds the angular content only; radial quadrature and
rounding are separate.

3.8 Expected dimension of the solution set. [lead heuristic; independent referee verdict] Because c_l multiplies the
generator of the dilation symmetry, a solution at a prescribed c_l is expected to be nongeneric: if the linearization
is Fredholm of index zero, its kernel is spanned by the dilation tangent and a transversality condition holds, the
pair (dilation class, c_l) is locally isolated. None of these hypotheses is proved, and in the direct realizations with the natural decay weights (the same critical
weight in the graph and residual spaces) the transport part is not Fredholm; other asymptotic charts, for example a slightly
weaker weight or spaces that separate the leading angular tail, are not excluded. The search therefore treats c_l as an unknown with one dilation gauge and uses
fixed-c_l runs as diagnostics; a positive residual floor at a fixed c_l is not read as evidence of non-existence.

3.9 Stagnation portraits. [index count and local resonances: independent referee; re-derived by the lead with independent
exact checks; index count, separatrix exclusion and resonance formulas confirmed by an independent standalone proof, the
resonances for the stated nonzero finite jets] For c_l > 1/2 the circulation vanishes on every stable separatrix, and the basin of an
S1 or S2 source carries nonzero swirl off the axis, so such a source cannot feed an off-axis saddle. With hyperbolic zeros
the planar index gives N_O - N_D = t (off-axis sources minus off-axis saddles equals the number of axis saddles with radial
inflow). Among portraits with at most five zeros, all hyperbolic, three were selected as the smallest search targets: a single S1 axis source
with even swirl; an equatorial ring source (S3) feeding a radial-inflow axis saddle at the origin, with odd swirl and the
necessary strain v(0, 0) = -(1 + 3c_l)/2; and an S1 pair joined by an axial-inflow saddle of order two (order k >= 2 in the C^2 class, 3.14). The hypotheses of
3.4b, including smoothness, are needed: explicit axis data show that a degenerate axis zero, or regularity below C^2 at an order-two attractor,
allows opposite S1 amplitudes.

3.10 Approach to c_l = 1/2. [independent referee; lead-checked; conditional] (i) If smooth profiles exist for c_l -> 1/2+ with an
S1 point, a uniform global C^2 bound and uniform decay, some subsequence converges in C^1_loc to a decaying C^(1,1) profile at
c_l = 1/2 with nonzero swirl and an uncountable stagnation set; by 3.3 that limit is not real analytic. So along such a branch
one of these controls fails, or a subsequence converges in C^1_loc to a nonanalytic critical profile (neither C^2 convergence
nor a unique endpoint is asserted). (ii) Let the S1 source at z0 have amplitude K, and suppose the odd part
eta_o(r, x) = (eta(r, z0 + x) - eta(r, z0 - x))/2 satisfies |eta_o(r, x)| <= C K^2 |x| L^(-2) G(r/a) with
int_0^infinity rho G(rho) d rho = I_G < infinity and a^2/L^2 = 4 (c_l - 1/2)(1 + c_l)/((1 + c_l)^2 + K^2) (a single core whose
radial width is the S1 saddle-curvature width). Then the S1 strain condition fails once 4 C I_G (c_l - 1/2)(1 + c_l) < 1, for
any K; the shape constants C and I_G must be uniform for this to bound a family. Neither statement excludes profiles at any fixed c_l > 1/2.

3.11 Swirl on the symmetry plane and restrictions on the S1-pair portrait. [lead; independent referee; lead symbolic checks;
verifier-confirmed in the smooth stratum: (i), (ii), (iv) to (vi), (viii) and the moments of (iii), with the scope of (iii)
and (vii) as stated here] In the smooth stratum and the reflection class, if the origin is an axis zero of W_m with U^r/r > -1/2 there and W_r > 0 on the
equator, the circulation vanishes on the whole equator. In the S1-pair portrait (sources at z = +-1 with common amplitude K > 0
and an axial-inflow saddle at the origin): (i) in the quadratic stratum, where q vanishes on the equator exactly to second order (smooth axis matching also allows the
even orders k = 4, 6, ... at the saddle, with axial contraction rate (1 + c_l)/(k - 1); they are not treated here), q has the
sign of K elsewhere,
and at the saddle q = Q z^2 + ... with Q > 0 and eta = (2 K Q/(1 + c_l)) z + ...; (ii) on the equator d_z eta and d_zz q are
proportional with a positive factor, so eta > 0 just above every equatorial point, while at the pole the far-field coefficients
satisfy c_l E(1) = -2 K B(1) < 0, so eta changes sign in z > 0; (iii) three exact moments of eta (central strain, source strain,
source position) imply again that the portrait is impossible if eta is one-signed in z > 0, and the axis contributions to the
source strain from a neighbourhood of the saddle end of the inner axis and from the far outer axis are unfavourable (on the
whole axis if q <= K on both axis branches; an axial overshoot q > K can contribute favourably near a source), so the favourable
part must come from elsewhere (an earlier version used a source-strain kernel with a sign error and stated a further exclusion
based on it; that exclusion is withdrawn); (iv) at a source,
4 (c_l - 1/2)(c_l + 1) q_rr + ((1 + c_l)^2 + K^2) q_zz = 3 ((1 + c_l)^2 + 2K^2) q_z^2/(2K), and a source maximum of q needs the axis
coefficients h_2 = h_3 = h_4 = 0 of phi; (v) on the inner axis segment the finite part of int_0^1 (Q/q - 1/z^2) dz equals 1, so
q >= Q z^2 cannot hold on the whole segment; (vi) no exact profile has the separated form phi = z F(r^2 + z^2), q = z^2 G(r^2 + z^2);
(vii) the first even-swirl resonances at the saddle inside the interval are at c_l = 5/7 (weighted order 36), 11/16 (40) and
2/3 (44); there are infinitely many rational resonances, each a compatibility question, and no low-order logarithms arise; (viii) an explicit smooth model satisfying all axis, finite-part, moment and source
conditions fails only off the axis. The portrait is not excluded.

3.12 Restrictions on the single-source portrait. [independent referee; lead symbolic checks of the jet statements;
(i) to (iv) verifier-confirmed (independent proof, 100 exact tests); (v) referee with a proof file and floating-point numerics,
lead symbolic checks, the sign statements (including, by an independent proof, the positive strain of the explicit family in
the large-B, large-L regime and its incompatibility with the cubic relation) and the jet relation verifier-confirmed, the numerical strain at c_l = 0.74 reproduced
by the verifier to 5.8e-9; (vi) verifier proof, lead-checked] With one S1 source at the origin in the reflection class and q0 > 0: (i) the source condition d_z phi(0, 0) = 1/2
is equivalent to J_+ - J_- = 1/3 for the positive and negative parts of the weighted moment of eta over z > 0, and the axis
relation forces J_- > 0, so eta of one sign in z > 0 is excluded; (ii) a nonflat source maximum of q can first vary only in
degree divisible by four; (iii) if q <= q0 with a quartic first variation, then (13 - 14 c_l) q0^2 >= (c_l + 1)(56 c_l^2 + 28 c_l - 37),
which for c_l > (9 sqrt 7 - 7)/28 = 0.6004 requires q0 >= K_min(c_l) with K_min^2 = (1 + c_l)(56 c_l^2 + 28 c_l - 37)/(13 - 14 c_l),
K_min approximately 1.72621 (c_l = 2/3), 2.30949 (0.70) and 3.07919 (0.74); (iv) an explicit smooth
axis model shows that the axis equations, the pole relation, elliptic closure and the source moment together do not force the
swirl to grow along the axis, so any obstruction must use the equations off the axis; (v) for a prescribed meridional field
with the single-source portrait, the induced source strain (the Green moment of the characteristic vorticity of unit source
amplitude, which must be positive at a profile) is negative whenever the characteristic swirl decreases away from the equatorial
plane and decays at infinity (with the normalization and integrability hypotheses stated in 5e (vii) (a) of the accompanying obstruction audit; without decay the statement fails), as for an explicit family of such prescribed fields (not Euler profiles) at c_l = 1/2 + 3/(4n), n >= 4, but it has no sign in general: an explicit family with
axial amplification (d_z phi(0, z) > 1/2 near the source) has positive induced strain. In the regime used to prove positive strain (the family's two shape parameters B and then L
sufficiently large) the exact cubic jet relation at the source, p_s = -(3 p_z/4)(1 + q0^2/(1 + c_l)^2) for phi = z/2 + p_s r^2 z + p_z z^3 + ..., fails
(it bounds a combination of the family's shape parameters that this large-B, large-L regime makes arbitrarily large), so no field
in that regime is an exact
profile; finite-parameter members with positive strain outside that regime are not covered by this argument; how well such fields approximate a profile is the measured defect below. Numerically (floating point), fields with a proved
single-source portrait reach positive induced strain at c_l = 0.55, 0.60, 0.68 and 0.74 with closure defects 0.92, 0.82, 0.69 and
0.61 and required source amplitudes q0 = 34, 10.8, 3.9 and 2.5; three damped Picard steps at c_l = 0.60 lowered the defect once
(0.82 to 0.76) and then lost the sign of the strain, at the step where the updated axial cubic coefficient became negative (a
measured coincidence; a negative cubic coefficient controls only the near-source forcing). (vi) This seed family
phi = z(1 + 3z^2)/(2(1 + a r^2 + z^2)^(1 + 1/(2 c_l))) cannot close for any aspect a, amplitude or dilation: the cubic source relation
of (v) needs a > 3(2 - p)/(4(p + 1)), p = 1/(2 c_l), while the negative far upper-axis vorticity forced by the transport needs
a < p(2p - 1)/(4(p + 1)), and these ranges are disjoint. With a second parameter, phi = z(1 + b z^2)/(2(1 + a r^2 + z^2)^(p + 1)),
no member is exact either: the transported vorticity on the far upper axis has a nonzero term of order z^(-1 - 4p), the trace of
the first nonlinear far-field correction, which the family cannot produce. This excludes two explicit families, not their
deformations. The portrait is not
excluded.

3.13 Restrictions on the odd-swirl ring portrait. [independent referee; lead re-derivation and symbolic checks; (i) and (ii)
re-proved by the verifier under weaker hypotheses (125 symbolic and high-precision tests); (iii) and (iv) for smooth portraits
also follow from the verifier's standalone proof of (i) and (ii), and their Cartesian C^2 extensions are derivations of the
referee and the lead, not verifier-checked; (v) is a heuristic] For the smooth odd-swirl portrait of 3.9 with exactly the
origin saddle and a simple equatorial ring source: (i) q, eta and d_s eta (s = r^2) vanish on the upper axis, so q = r^2 Q(z) + O(r^4)
and eta = r^4 J(z) + O(r^6) near it; (ii) on the upper axis w J / Q^2 = 4 - (2(2c_l - 1)/M(z)) int_0^z e^(-(1 + c_l) tau) du, with
w = W_z(0, z), tau' = 1/w and M = w e^(-(1 + c_l) tau), so eta is negative near the upper axis far out and, if the far-field expansion of eta holds with its transverse derivatives
uniformly near the pole (as in 3.7), the far-field coefficient of eta has negative second derivative at the pole; (iii) d_z eta(r, 0) > 0 for r > 0, while d_z eta(0, 0) = 0. Already (i) and (ii) show that eta takes
both signs in z > 0 (eta > 0 near the origin side of the axis, eta < 0 far out), so no smooth ring-portrait profile has eta of
one sign there. In the Cartesian C^2 ring class the axis vanishing and the equatorial positivity survive, but the outer-axis
argument of (ii) uses smooth coefficients and is not established there. (iv) For a given meridional transport field, the
swirl amplitude C of the origin saddle (q ~ C r^2 z there; q(0, 0) = 0) is determined by the ring amplitude. (v) Heuristically (not a theorem),
the quantized strain of a saddle that receives swirl is a condition without a new amplitude, so the ring portrait and the S1-pair
portrait are expected to be of codimension one among smooth profiles, while the single-source portrait has a square count. In
the C^2 class the strain is not quantized (3.14). The ring portrait is not excluded.

3.14 Finite regularity at saddles that receive swirl. [independent referee with a standalone proof; lead symbolic checks;
(i) to (iii) verifier-confirmed with scope by an independent proof, with two qualifications included below; (iv) is a
heuristic; (v) states approximation rates for model functions, with the verifier's qualification; (vi) independent referee with
exact portrait certificates and floating-point numerics, lead symbolic checks; portrait certificate verifier-confirmed, and the
three moments independently confirmed for the two tested fields c_l = 0.68 and 0.74 (k = 2.75, a = 1/64); the other scan points,
the closure norm 5.84 and the iteration not verifier-checked] In the Cartesian C^2 class the saddle strains of the S1-pair and ring portraits are not quantized.
(i) At the S1-pair origin saddle, with axial contraction rate kappa, the swirl vanishes on the whole equator like A(r^2) |z|^k,
k = 1 + (1 + c_l)/kappa, and the leading factor is compatible with Cartesian C^2 for every k > 2 as well as k = 2, so
0 < kappa <= 1 + c_l (in the smooth stratum k is an even integer; the quadratic stratum k = 2 gives kappa = 1 + c_l); this is a leading-factor test, and C^2 regularity of U needs in addition a
controlled local expansion (differentiated remainders), which the construction of (ii) supplies;
for k not an even integer, the nonzero leading factor A(r^2)|z|^k is C^(2, beta) exactly when k >= 2 + beta (even integers, including
k = 2, are exceptions); for U itself this needs the same controlled expansion. For a simple ring source, the leading factor C r^(2j) z of the swirl at the origin saddle is compatible with Cartesian C^2
velocity when j > 1/2; the corresponding fractional ring construction is formal and its convergence is not proved. (ii) Local
solutions of the full reduced equations with nonquantized strain exist: for every k > 2 there is an exact local solution near
the saddle, for example at c_l = 3/5, k = 5/2: q = |z|^(5/2) + (9/56)|z|^5 + ..., phi = -(5/6) z - (3/14) sgn(z)|z|^(7/2) + ...,
with an explicit pressure. It does not decay and does not construct the sources. (iii) The equatorial ratio of 3.11 (ii) becomes
E(r^2) = K (3 c_l + kappa) A(r^2) / (kappa (c_l - phi_z(r^2, 0))) for the fractional coefficients, the inner finite part becomes
int_0^1 (Q/q - z^(-k)) dz = 1/(k - 1) for 2 < k < 3 under a regular conormal expansion, and the one-signed eta exclusion of 3.11 survives.
(iv) The elementary count (heuristic) becomes square for both portraits in the fractional strata, as for the single-source
portrait; no condition that restores the smooth value is known. (v) For model functions with the
saddle cusp, polynomial approximation has no positive floor but is only algebraic: value error of order N^(-k), and C^2 error of
order N^(-(k - 2)) for derivative-aware approximations (approximate the second derivative and integrate); for |z|^k on [-1, 1]
the raw Chebyshev truncations converge in value but their second derivatives at z = +-1 do not converge for 2 < k <= 3. These are approximation rates,
not rates for a solver or for an Euler residual. A dedicated representation with the exponent k as an unknown is described in
the accompanying audit (section 5g). (vi) The closed S1-pair problem was tested on an explicit rational family
phi = z F(a r^2 + z^2) with a proved S1-pair portrait for 0.60 <= c_l <= 0.74 and 2 <= k <= 3 (sources at z = +-1, origin saddle with
rate kappa = (1 + c_l)/(k - 1)). The characteristic swirl and vorticity are computed from the sources, and the three Green moments of
3.11 (iii) give the source strain S_3, the source position P_3 and the central strain A_3 of the reconstructed field. With a
round aspect (a = 1) the source strain is negative in all twelve cases (c_l in {0.60, 0.68, 0.74}, k in {2, 2.25, 2.5, 2.75}).
Among the tested points (a from 1/128 to 4) it is positive only with strong radial stretching (a = 1/16 to 1/64), only for
c_l >= 0.68 and only for k > 2; these are observations on a finite scan, not thresholds. The strain kernel near the equator,
2(r^2 - 4)(r^2 + 1)^(-7/2) z, favours positive vorticity beyond r = 2, which radial stretching supplies in the tested family. The best closure defect is 5.84
(c_l = 0.74, k = 2.75; annular norm), against 0.61 for the single-source fields of 3.12 (v). At every positive-strain point the
position and central-strain moments have the sign opposite to the one a profile needs (the position kernel is positive in the
whole upper quadrant), the reconstructed field has a saddle of the opposite orientation, and an iteration projected back into the
family drives c_l from 0.74 to 0.62 and loses the sign of the strain. No selection of c_l was observed. These are finite-family
floating-point findings; they do not exclude the S1-pair portrait or its fractional stratum.

## 4. Numerical campaign

Counts attributed to the primary search are computed from its frozen failure map (526 finished runs, frozen in the
Stage II freeze, which ran from 2026-10-29T11:37Z to 11:40Z) and count primary-search runs only.

4.1 Representations and solvers.
(a) Primary search. phi and q are polynomials in (r^2, z) on a central ball (a regular subspace of the Cartesian polynomials,
reflection parity available as an option and used only in labelled parity-restricted runs; the single-source ladder below is
unrestricted; radial factor Chebyshev at first, then a three-dimensional Zernike-type Jacobi family after a
conditioning test: column-scaled Jacobian condition 2e10 with 54 near-null directions, against 1e8 with 2), log-mapped
Chebyshev-Legendre spherical shells, and an analytically factored power-law exterior with the exponent chain alpha + k/c_l (a restricted truncation of the formal far-field expansion: it omits the logarithms and the products with the global multipoles).
Interface rows target phi in C^3 and q in C^2, so at an exact root the velocity would be Cartesian C^2; the saved approximations
have nonzero measured interface defects (section 6). Residuals are the reduced equations R_q, R_eta with
analytic Jacobians, plus weighted constraint rows for the source structure; Levenberg-Marquardt and L-BFGS; held-out collocation
points for the reported metric. The registered metric is rho_E = RMS(R_E)/min(RMS L_E, RMS N_E) on dyadic shells (section 9 of the
accompanying specification), with acceptance thresholds registered before any candidate existed and never changed.
(b) Second method in the primary search: Newton-Krylov on the transport and elliptic fixed-point map in (phi, q0), with and
without c_l as an unknown.
(c) Independent search, written separately from the primary code: a monomial-envelope basis with exact linear constraints for an
S1 source and reflection parity, a source-compatible Green-function variant, free-c_l variants and an odd-swirl ring branch,
with analytic Jacobians checked against finite differences.
(d) Closed characteristic formulation of the single-source portrait (independent referee computation, section 3.12 (v)):
swirl and vorticity by eighth-order characteristic integration from the source, phi reconstructed by the 5D Green function,
damped Picard iteration.

4.2 Tests. Primary code: its operator suite (identities, manufactured fields, dilation covariance, axis limits, basis exactness) passed all 68 checks at their stated tolerances in all three Stage III runs in its own directory (2026-10-29T12:00:27Z, 12:03:08Z and 12:21:52Z; 6.6, 6.4 and 6.4 s of test time) and in two runs from fresh copies of its artifacts (12:41:07Z and 12:43:14Z; 6.6 and 6.5 s of test time); the two retained earlier runs of the suite, which then had 65 checks (2026-10-28T19:16Z and 19:19Z), each recorded 64 passes and one failure, the exactness test of the exterior basis for third derivatives at alpha = 0.55 (relative errors 6.3e-5 and 2.8e-5 against the tolerance 1e-9) [verifier check of the logs; lead count]. Algebraic identities agree near roundoff. Jacobian-vector products passed finite-difference tests, with differences 2.4e-14 to 5.5e-14 for fixed-c_l directions, up to 7.9e-13 for free-c_l directions, up to 5.4e-8 for the source-constraint directions and 2.6e-9 for the source-location columns, each within its stated tolerance [primary search; verifier check of the test logs];
manufactured-solution recovery after the basis change (to round-off from a 3 percent perturbation, cost 5e-8 from 10 percent;
c_l recovered to 1e-14 in the free-c_l manufactured case), the first nonlinear far-field correction verified (scaled residuals decay like R^(-1/c_l) with it
and stay constant without it), interrupt and resume of a worker (repeated in Stage III, section 9.1). Independent validation code: 86 operator check cases, 25
far-field cases and 22 identity cases (cases within test groups), high-precision and direct-Newton pressure checks; its complete
clean-process suite of 59 operator test groups passed in 140 s at the end of Stage I (these are implementation checks, not
candidate checks).

4.3 Stage I sweep and outcome (primary search; the 311 finished runs labelled Stage I in the primary failure map, finished between 2026-10-28T19:39Z and 2026-10-29T04:47Z, of which 282, including 81 of the 97 swirl-retaining runs below, finished before the end of Stage I at 00:59:44Z; the counts below are computed from the primary failure map with the stated filters [lead check of the primary run records, repeated on the frozen map; counts confirmed by the verifier]). Starting c_l in {0.505, 0.525, 0.56, 0.60, 0.64, 0.68,
0.72, 0.74} and a separate c_l = 0.500 experiment. Initializations: single-source seeds with an exact S1 structure (symmetric and
shifted families, source amplitude q0 in {0.5, 1, 2}), transfer from neighbouring c_l, Gaussian cores, ring seeds for the
odd-swirl portrait and pair seeds for the S1-pair portrait. Branches: S1 rows with q0 free; q0 pinned with c_l free; an explicit
swirl amplitude; continuations to 3000 iterations. One resolution level (ball degree 24 with n <= 12, one shell to R = 10
with 16 radial nodes, two radial bases). No run met all the conditions of label A or of label B. Among the 97 runs that keep the swirl (core and far swirl fractions at
least 0.05) the smallest rho_max per starting c_l is 13.1 (0.505), 79.5 (0.525), 25.6 (0.56), 6.9 (0.60), 6.7 (0.64), 7.2 (0.68),
7.5 (0.72) and 7.5 (0.74); the dominant equation of these best runs is axial momentum, except at 0.505 (reduced vorticity). By
failure class, 214 runs lost the swirl (the optimizer lowers the cost by removing it), 74 plateaued and 19 stopped decreasing at
that single resolution (fixed-resolution stalls, not refinement plateaus in the sense of the failure-map protocol), and 4 failed
the interface test. The 43 free-c_l runs end near their start (from 0.505 at 0.532 to 0.549, from 0.60 mostly at 0.601 to 0.607,
from 0.72 and 0.74 slightly below the start), except six that reach the upper bound 0.749 (from 0.60, 0.64 and 0.68) and one
that reaches the lower bound 0.501 (from 0.60); these are endpoints of separate runs, not stages of one run. The four odd-swirl ring runs fail (c_l runs to the bounds, rho_max 129 to 620); the S1-pair runs
plateau. Newton-Krylov finds no root near the S1 seeds (residual about 0.35 relative with the induced source strain of the wrong
sign; with c_l unknown it oscillates between the c_l bounds). Later the same Stage I runs: with the first far-field correction
slaved to the leading tail the swirl is still lost (rho_max 6.4 to 25); the S1-pair runs end at the upper c_l bound with rho_max
239 to 2.4e4. Interim (2026-10-28T22:48Z, before verification): a single-source run (ball degree 36, so not among the degree-24
runs counted above) started from the closed-formulation seed at c_l = 0.74 with q0 = 2.5 pinned and c_l free retained the swirl (core and far swirl fractions at least 0.05; core swirl
fraction 0.84; this alone does not establish B2, whose stability across levels was not tested), with rho_max 4.6, but c_l runs to the upper bound 0.749 and the far-field swirl changes sign, which is impossible for a
profile in which every backward characteristic converges to the source (along each characteristic the swirl equation is a linear
ordinary differential equation, so q keeps the sign of q0); a finite stagnation search does not establish that basin property
for a numerical state.
The separate c_l = 1/2 experiment (single-source and generic seeds from nine initialization families, ball degree 24, two
radial bases, 23 runs each) is complete with 46 runs: 26 lost the swirl, and among the 20 (10 per basis) that kept core and far
swirl fractions of at least 0.05 the smallest rho_max is 12.5 on one basis (core swirl fraction 0.13) and 24.2 on the other;
the smallest rho_max of any run, 4.7, belongs to a run that lost the swirl (core and far swirl fractions 0.03 and 0.02)
[primary search; counts and minima confirmed by the verifier against the saved run records; cross-level swirl stability was
not measured, so the 20 runs pass only the magnitude part of B2]. In view of 3.3 a decaying swirling
profile at c_l = 1/2 would need an uncountable stagnation set and could not be real analytic; the piecewise representation can
in principle approximate such a profile, but none of these runs came close. The exported c_l = 1/2 state of that run (rho_max 12.5 in the search) measures rho_max 14.4 under the verifier's registered evaluation (reduced vorticity equation at axis-collar points of shell 2; core and far swirl fractions 0.12 and 0.053) [verifier]. Its interface moments of 3.7 are C0 = -1.6e-7 and C1 = -3.5e-9, against Q_0 = -5.4e-3 (the coefficient of R^-2 in the spherical mean of the bulk pressure) and Q_1 = -2.8e-3, so in the spherical mean of its bulk pressure a small 1/R monopole overtakes the R^-2 term only beyond R of order 3e4 [verifier, floating point]. A finite stagnation search on this state reported an off-axis zero of W_m at r = 1.1e-6 next to an axis source; it is not a zero: on the working-unit rectangle 0 <= r <= 1e-5, |z - z_0| <= 1e-7 the radial factor W_r/r = c_l - phi_z of the ball polynomial lies between 1.265e-5 and 1.281e-5 and the axial component changes sign once with positive derivative, so the rectangle contains exactly one zero, on the axis, with both meridional eigenvalues positive [verifier proof with exact rational bounds; lead cross-check with a different enclosure]. This is a local statement about the fixed approximation, not a stagnation inventory. Late in Stage II the best swirl-retaining state was refined to ball degree 32 (1500 iterations) and both best states were continued for 2000 iterations at degree 24: the refinement gave 7.49 (axial momentum; core and far swirl fractions 0.090 and 0.057, against 0.13 and 0.053 at degree 24; training cost 0.29, a poor fit), its continuation gave 12.05 with fractions 0.060 and 0.032 (below the filter), the continuation of the second state gave 48.2 with fractions 0.016 and 0.005, and a degree-32 refinement of the second state gave 41.8 (fractions 0.064 and 0.021): three of these four follow-up runs fall below the swirl magnitude filter, and the degree-32 refinement of the best state passes it with a reduced core fraction (0.090 against 0.13) and a far fraction slightly above its parent's (0.057 against 0.053); passing the filter does not establish stability under refinement [primary search; scalar arithmetic checked by the verifier from the saved records]. The registered evaluation of the two degree-32 exports gives rho_max 7.47 and 40.5 (both largest in the axial momentum equation, at axis-collar points of shells 0 and 2), m_max 32.9 and 68.7, core and far swirl fractions 0.088 and 0.057 (passing the magnitude filter) and 0.064 and 0.021 (failing it), and relative interface derivative jumps 3.5e-3 and 8.8e-4, so A1, A2 and A8 fail for both [verifier].

4.4 Independent search. 56 restricted single-source runs (custom held-out objective 0.065 to 1.12), 18 constrained refinements
(raw swirl defects at least 1.24, coefficients about 1e5, normalized Jacobian condition about 1e8), 30 odd-swirl ring starts (best
objective 5.66), 12 free-c_l runs that all end at the imposed upper bound c_l = 0.7495, and enriched Green-basis fits whose held-out
objective worsens from the second to the third level (0.028 to 0.105). A globally smooth chart with the exact first far-field
correction and no interfaces reaches held-out objectives 0.40, 0.026 and 0.017 at three resolutions while the raw swirl defect stays
at 3.0, 1.41 and 1.14 and the reduced-equation screens give rho_max at least 6.7, 4.7 and 2.1. A registered single-source ladder
at c_l = 0.74, q0 = 2 measures rho_max 4.07, 6.54 and 5.71 and m_max 18.9, 19.1 and 31.3 at levels 0, 1 and 2 (level 2: 9150 s
of process wall time); each level was reoptimized from the previous one with a larger basis and fitting domain, so this is a
continuation ladder, not a refinement of a fixed field. In total the independent search has 197 completed search records and the validation has 27 registered validation records (25 distinct fully evaluated states, one full repeat and one incomplete record; count of 2026-10-29T12:28Z, including the two Stage III registrations at c_l = 0.745 of 4.4a); all 21 exported primary-search states have full registered evaluations, all rejected (coverage audit of 12:28Z) [verifier]. No candidate. [verifier]

4.4a The pinned-amplitude single-source ladder (end of Stage I). Started from the positive-strain fields of 3.12 (v) at
c_l = 0.74 with the source amplitude q0 pinned (dilation invariant), the first nonlinear far-field correction slaved to the leading
tail and c_l free, the primary search produced states with core and far swirl fractions 0.5 to 0.9.
In each of these runs c_l moved to the imposed upper bound 0.749. The best state (q0 = 3.5, ball degree 36 with n <= 24, 3000
iterations) was exported and validated independently on all registered shells: rho_max = 1.92 (axial momentum with the full-space
pressure, shell 2 collar), m_max = 21.0 (eta, shell 11), maximum relative interface derivative jump 6.1e-3, relative mismatch of
the first far-field correction 0.084 (the optimizer slaves that correction to the leading tail; 0.084 is the independently
measured mismatch of the export); A1, A2, A8 and B4 fail [verifier]. The angular polynomial of its leading swirl coefficient
changes sign: the native exterior Legendre polynomial, before the strictly positive radial factor, takes the values about
-7.3e-4 at mu = -89/512 and 0.467 at mu = -1 (decimal displays of exact rational values) [verifier]. This is impossible for a profile in
which every backward characteristic converges to the source (section 4.3), a property not established for the numerical state.
(The degree-48 state L2 below has a complete exact positivity certificate for the same polynomial [verifier].) Early
fixed-c_l steps measured rho_max 2.39 at c_l = 0.745 (q0 = 3.5) and, at q0 = 2.5, 5.97 at 0.74 and 36 at 0.73 (two separate
direct steps from one q0 = 2.5 parent state, not one continuation); the small-step q0 = 3.5 chain below gave 10.7 and 19.3 at
0.74 and 0.73, so these are different runs, not unique values per exponent. The continuations have larger measured residuals away from the bound (this does not establish a floor for the representation or
the class). Ball degree 48 gave rho_max 2.33 on the primary holdout evaluator (its registered value as the
export L2 is 2.90 [verifier]), against 2.55 for its degree-36 parent; that parent is a 6000-iteration
continuation of the 3000-iteration state above (1.88), so this is not a refinement of one fixed state with all else unchanged. Early Stage II tests of the same branch: at q0 = 2.5 the levels 36, 48, 64
gave 4.24, 2.79, 3.37 (unsuccessful finite refinements; the ratios do not meet the formal plateau definition of the
failure-map protocol, and B1 fails plainly); continuing the degree-48 state gave 3.19; separating the exterior exponents 3 and 3 alpha + 2,
which nearly coincide near c_l = 3/4 and had been merged into one column, gave 3.15 (registered value 3.31, axial momentum in
the origin collar, with m_max 4.90, interface jump 6.4e-3 and first-tail mismatch 1.0001, so A1, A2 and A8 fail [verifier])
and an irrotational dipole coefficient of
about 4 percent of the tail at the matching radius, where an exact profile has none (section 3, far field). These states are not symmetric under z -> -z (in the export metadata the axis source of L1 sits at
z = 0.0079 and that of L2 at z = 0.039). In the reflection class (phi odd and q even in z, source fixed at the origin, separated
exterior exponents, started from L2) ball degrees 36 and 48 gave rho_max 4.44 and 10.4 at c_l = 0.749 and 26.6 and 32.2 at
c_l = 0.74: no decrease with degree [primary search; the registered value of the degree-36 state at c_l = 0.749 is 4.46, with
m_max 44.9, both in the vorticity equation on shell 11, and it also fails the interface and tail checks [verifier]]. The dominant entry is the vorticity equation in the far shell R in [2048, 4096] a_eff
at both degrees for c_l = 0.749 and at degree 48 for c_l = 0.74 (axial momentum in the shell R in [8, 16] a_eff at degree 36). A continuation at q0 = 3.5 and ball degree 36 from c_l = 0.749 into the interval gave rho_max 2.39, 10.7,
15.3, 19.3, 21.9 and 24.7 at c_l = 0.745, 0.74, 0.735, 0.73, 0.72 and 0.70; at c_l = 0.74 the ball degrees 24, 36 and 48 of this
chain gave 14.6, 10.7 and 8.0 (2500, 2500 and 1000 steps in the final optimization stage; the saved iteration counter of the
degree-24 run, 3260, double counts a 760-row history prefix duplicated at a checkpoint resume, so it ran 2500 iterations [verifier]); a further step to c_l = 0.65 moved the core outward (a_eff from
2.6 to 13.7 in working units), so its value is not comparable, and the next step to 0.60 from that state failed to transfer
(final cost 6.5e7). A chain at q0 = 5.0 gave 2.04, 142, 40.7 and 71.9 at c_l = 0.749, 0.74, 0.72 and 0.70 and lost its far
swirl at 0.65 (rho_max 83.5, far swirl fraction 0.002); raising q0 along the continuation (5.5, 6.0, 7.0) gave 2.375, 23.0 and
20.1 at 0.745, 0.74 and 0.73 [primary search]. The registered evaluation of the 2.375 state (frozen export, 537 s) gives rho_max 2.34 (q, shell 1, random points), m_max 11.5 (eta, shell 11), largest relative interface jump 1.3e-3 and first far-field correction 0.21 relative to the Euler term, so A1, A2, A8 and B4 fail; its core and far swirl fractions are 0.78 and 0.76 by fixed-field quadrature, which is not the B2 stability test [verifier, Stage III]. Moving the matching radius from 10 to 20 at c_l = 0.70 failed to transfer (rho_max 39.0, core
and far swirl fractions 0.04). Both chains were stopped there; below c_l = 0.70 the search relies on direct positive-strain
seeds at fixed c_l (ball degree 36, started from the referee's positive-strain single-source fields; working-unit source
amplitudes q0 = 3.9, 5.7, 10.8 and 20 at c_l = 0.68, 0.65, 0.60 and 0.55, the second and fourth interpolated): rho_max 7.73
at c_l = 0.68 with core and far swirl fractions 0.38 and 0.57 and a_eff 2.78 [rho_max and fractions reproduced by the verifier from the saved record; this passes the swirl magnitude filter only], 35.1
for the degree-24 level of that state; continuing that state at ball degree 36 for 1500 further steps lowered rho_max to 3.50
(core and far swirl fractions 0.64 and 0.68, a_eff 2.34) and 1500 more to 3.38 (core swirl fraction 0.67), and 1500 more raised it to 4.83, while a seed with q0 = 5.5 gave 4.39 and then 6.31 after 1500 further iterations, so at c_l = 0.68 the held-out value fluctuates between 3.4 and 6.3 under further iterations without converging; the degree-48 and degree-64 levels started from the 3.50 state gave 5.12 and 4.85 (2500
iterations at degree 64), and a degree-48 level started from the 7.73 state gave 3.37, so the degree levels at 0.68 (35.1 at
degree 24, 3.38 to 3.50 at 36, 3.37 and 5.12 at 48, 4.85 at 64) cluster near 3.4 to 5 without decreasing, and a 1000-iteration
step from the 3.50 state to c_l = 0.6667 (near 2/3) gave 53.4 (vorticity equation in the far shell; 33.9 at degree 48), and a
step to 0.70 gave 102; these tested steps worsened the residual, which does not show that the state cannot be continued.
Seeds tabulated for c_l = 0.68 applied at c_l = 0.70 lost the far swirl (rho_max 60.2, far swirl fraction 0.007), and
direct seeds at c_l = 0.72 (q0 = 3.0) and 0.70 (q0 = 5.0) gave 75.6 (axial momentum at the collar, core and far swirl
fractions 0.52 and 0.62, plateaued) and 45.0 (far swirl fraction 0.01). A free-c_l
run from the 3.50 state moved c_l to the imposed bound 0.749 (rho_max 2.62, core swirl fraction 0.67), as did two free-c_l restarts from the 0.74 state: with the upper bound widened to 0.80, c_l moved to 0.80 (rho_max 3.09; its own training cost decreased from 0.0140 to 0.0121), and with the upper bound 0.745, c_l reached 0.745 within 55 iterations (rho_max 2.60, core and far swirl fractions 0.67 and 0.62) [primary search; scalar arithmetic checked by the verifier from the saved records], and the registered evaluation of its frozen export gives rho_max 2.70 (axial momentum, axis collar of shell 2), m_max 7.76, largest relative interface jump 1.5e-2 and first-correction mismatch 0.017, so A1, A2, A8 and B4 fail [verifier, Stage III]; these three runs drifted to the imposed bound, which does not show that every upper bound would be reached, whereas four free-c_l runs of the earlier ladder seeds of this class (started at 0.60 and 0.68) drifted down to c_l = 0.506 to 0.596 with rho_max 331 to 1.2e6 [primary search; endpoints confirmed by the verifier from the saved records]. Under the verifier's registered evaluation the frozen 3.50 and 3.38 states measure 3.58 and 5.10 (the larger value from fresh random shell points in the reduced swirl equation) and the frozen 3.55 state at c_l = 0.74 measures 3.59 [verifier]. The values 3.58 and 3.59 are maxima of the momentum equation, evaluated with the bulk pressure truncated at Legendre degree 32, and are therefore finite-truncation diagnostics; for the two states at c_l = 0.68 raising that degree from 32 to 40 changes the pressure gradient by about 1.7e-3, and the pressure-independent swirl equation alone gives 3.32 for the 3.50 state and 5.10 for the 3.38 state [verifier]. A direct run at fixed c_l = 0.74 from the seed field of the pinned-amplitude ladder (q0 = 2.5, degree 36) gave 3.55 (core and far swirl fractions 0.50 and 0.58), against 10.7 for the continuation chain at the same c_l and degree; 1500 further iterations lowered it to 2.86 (core and far swirl fractions 0.66 and 0.61). Two degree-48 levels of 1500 iterations gave 2.85 (started from the 1500-iteration state; swirl fractions 0.66 and 0.60) and 2.81 (started from the 3000-iteration state; 0.66 and 0.60), and a degree-64 level of 2500 iterations from the 3000-iteration state gave 2.95 (0.67 and 0.61), all with the largest residual in the reduced swirl equation and interface jumps of 1.2e-2 to 1.6e-2: over three resolution levels the value stays at 2.8 to 3.0 without decreasing, so B1 fails by a factor of about 3e3 at every level [primary search]. The verifier's registered evaluations give rho_max 2.74 for the 3000-iteration state and 2.71 and 2.78 for the degree-48 levels started from the 3000-iteration and from the 1500-iteration state, all in the reduced swirl equation on random points of the first shell, which does not involve the pressure, with core and far swirl fractions 0.66 and 0.60 for both degree-48 states; the first far-field correction is matched to 0.017 at degree 36 but has relative mismatch 0.99 and 1.00 at degree 48 [verifier]. The exported degree-64 level measures rho_max 2.84 under the registered evaluation (reduced swirl equation on random points of the first shell; m_max 8.40; core and far swirl fractions 0.67 and 0.61; relative interface derivative jump 3.4e-3; first-correction mismatch 1.00), so A1, A2 and A8 fail [verifier]. A second optimizer (L-BFGS with a strong Wolfe line search) made no accepted step from the degree-36, 3000-iteration state, and 500 further Levenberg-Marquardt iterations lowered the training cost from 1.40e-2 to 1.31e-2 (costs of separate runs are not directly comparable: that run computes 1.40e-2 for the start state, whose own run recorded 1.46e-2) and the held-out value to 2.65 (core and far swirl fractions 0.67 and 0.61) [primary search; scalar arithmetic checked by the verifier from the saved records]; first-order stationarity was not measured. Under the registered evaluation that exported state measures rho_max 2.74 (axial momentum at axis-collar points of the second shell; the pressure-free equations alone give 2.71, in the reduced swirl equation), m_max 7.87, core and far swirl fractions 0.66 and 0.61, relative interface derivative jump 1.5e-2 and first-correction mismatch 0.014, so A1, A2 and A8 fail [verifier]. Continuing the 3000-iteration state to 6000 iterations in total lowered the training cost from 1.46e-2 to 1.12e-2 while the held-out value went to 3.27, and three restarts after relative coefficient perturbations of 1e-2, 3e-2 and 1e-1 (1500 iterations each) returned to 2.85, 2.75 and 3.12 with training costs 1.24e-2, 1.17e-2 and 1.21e-2: at 0.74 the held-out value stays between about 2.6 and 3.3, including after the three tested perturbations (1, 3 and 10 percent), while the training cost keeps decreasing [primary search; scalar arithmetic checked by the verifier from the saved records]. The same seed optimized directly at ball degrees 24 and 48 (1500 iterations) gave 5.41 and 3.32, against 3.55 at degree 36, and six unrelated initializations at c_l = 0.74 (Gaussian, ring, asymmetric dipole, swirl-dominant, poloidal-dominant, random spectral) gave 22.4, 18.9, 11.0, 16.5, 109 and 5.7e3 [primary search; scalar arithmetic checked by the verifier from the saved records]. Source amplitudes q0 = 1.8, 2.0, 3.0 and 3.5 at c_l = 0.74 gave 5.57, 4.70, 2.87 and 4.60 after 1500 iterations (3.55 for q0 = 2.5) [primary search]. Chains of steps in c_l (1000 iterations each; steps of 0.005, and 0.01 below 0.72 and above 0.70) from the 0.74 state gave 13.7, 25.5, 35.8, 35.9, 23.9 and 31.3 at c_l = 0.735, 0.73, 0.725, 0.72, 0.71 and 0.70, and from the 3.38 state at 0.68 gave 7.49, 16.5, 33.4, 110 and 163 at 0.685, 0.69, 0.695, 0.70 and 0.71, so these transferred chains did not keep the low values at the tested neighboring c_l (direct seeds at neighboring c_l are reported below) [primary search; scalar arithmetic checked by the verifier from the saved records]. Sensitivity runs from the 3000-iteration state (1000 to 1500 iterations each) gave 2.83 with 1.5 times the quadrature nodes and 2.79 with the interface weight raised from 100 to 1000, but 8.23 and 8.54 with the outer interface moved from R = 10 to R = 5 and to R = 20, and 7.55 with a different radial-shell weighting (scale power shift -2 changed to 0) while the reduced-equation residual fell [primary search] (at ball degree 48 that weighting gave 14.5 in the axial momentum equation with a reduced-equation value of 0.71, a small reduced residual with a large primitive residual [primary search; scalar arithmetic checked by the verifier from the saved records]). At c_l = 0.68 the corresponding variations of the 3.38 state gave 6.39 (R = 5), 17.0 (R = 20), 6.78 (denser quadrature) and 16.9 (shifted shell weights, with a reduced-equation value of 1.46) [primary search; scalar arithmetic checked by the verifier from the saved records]. These runs reoptimize the field; they do not establish a stable approximation under the tested representation and weight changes, and every measured residual remains far above acceptance. Five final runs from the same seed or state: without the S1 rows and the q0 pin (gauge row only, 1000 iterations from the 3000-iteration state) the swirl was kept and rho_max was 3.02 (core and far swirl fractions 0.67 and 0.62; the run stopped at its iteration limit, so this is a finite continuation and says nothing about stationarity); with separated exterior columns in place of the slaved first correction it was 12.6 (far swirl fraction 0.45); and the seed optimized directly at fixed c_l = 0.745, 0.7425 and 0.7375 (1500 iterations, as for the 3.55 run at 0.74) gave 3.09, 6.89 and 10.7 (reduced-equation values 2.96, 3.40 and 2.28), so within 0.0075 of c_l = 0.74 these direct-seed values vary non-monotonically by a factor of about 3 [primary search; scalar arithmetic checked by the verifier from the saved records]. Further direct
seeds: 23.3 at c_l = 0.65 (not converged, core moved outward to a_eff 6.4), and failure at 0.60 and
0.55 (rho_max 1.1e4 and 1.6e6). [primary-search values, not verifier-measured unless marked] Jacobian diagnostics of the specification (column-scaled gauged Jacobian at the final state, c_l free): condition numbers 3.2e9 for the 0.74 direct-seed state at ball degree 36, 1.9e11 for its degree-64 level and 4.0e9 for the 0.68 state, with the five smallest singular values between 3.1e-10 and 4.3e-10 of the largest at degree 36 and between 5.3e-12 and 6.9e-12 at degree 64, against 5.7e9 for L1; for the three direct-seed states fixing c_l changes the condition numbers by less than one percent (by 1.0 percent for L1) [primary search]. The smallest singular values are not separated from each other and decrease under refinement while the residual does not, so the diagnostic indicates neither an isolated solution nor a one-parameter family; the projection of the residual on the left singular vectors across the c_l list was not computed.

4.5 Closed characteristic formulation (single source). Fields with a proved single-source portrait reach a positive induced
source strain at c_l = 0.55, 0.60, 0.68, 0.74 with relative closure defects 0.92, 0.82, 0.69, 0.61 (annular norm); damped Picard
iteration at c_l = 0.60 lowers the defect once and then loses the sign of the strain (section 3.12 (v)) [independent referee,
floating point]. The same closed problem
for an explicit S1-pair family in the fractional stratum reaches positive source strain, in a finite scan, only at c_l >= 0.68 with strong radial
stretching, with best defect 5.84 and moments of the wrong sign (section 3.14 (vi)) [independent referee, floating point, this
finite family]. A larger rational family
with up to 16 coefficients and a proved single-source portrait lowers the annular potential defect to 0.040, 0.017 and 0.013 at
c_l = 0.60, 0.68 and 0.74 [independent referee, floating point; far-axis sign test lead-checked; not verifier-checked], but this
norm hardly sees the source region: the vorticity of those fields differs from the transported vorticity by 0.70, 0.60 and 0.49
(relative, on a log-polar grid), their reconstructed axial cubic coefficients exceed the input ones by factors 26 to 770, and
their far upper-axis vorticity has the sign that no single-source profile can have. Targeting both cubic source conditions by penalties (met to about 5e-3 relative) and
imposing that sign at c_l = 0.74 leaves a relative vorticity discrepancy of 0.30 (potential defect 0.040) [the exact portrait
bound 0.0300027, the exact far upper-axis coefficient -35.834 and the transport discrepancy 0.267, 0.287, 0.298 on three grids
verifier-confirmed; the cubic conditions are penalized, not exact]. Damped and Anderson-accelerated
fixed-point iterations end with a gauge failure or a negative source strain, and a free c_l runs to the imposed ceiling 0.7499,
as in both searches. A small potential defect is not evidence of closure. In the two-parameter rational family of 3.12 (vi) the
three scalar conditions (strain normalization, cubic source relation, far-axis sign) were not met together at any sampled point:
on the sampled closed region where the last two hold, the sampled source strain is negative; its largest sampled values, -0.024 at
c_l = 0.62 and -0.120 at 0.74, lie on the limiting boundary K = 0 of that region, which the strict conditions exclude. At the sampled exponents through c_l = 0.86 (values above 3/4 are auxiliary, outside the target range) this family's measured
closure defect decreases, with no observed minimum or change of trend at 3/4, and the source eigenvalues, transport equations and leading Newton divisors have no singularity at 3/4; the drift of free-c_l
searches to the upper bound is therefore not explained, in this family, by a threshold at c_l = 3/4; this finite-family
diagnostic does not determine whether 3/4 has significance for other profiles [independent referee, sampled
floating point; region and portrait proofs lead-checked; not verifier-checked].
Minimizing the direct vorticity discrepancy itself (E, the root mean square over logarithmic shells 0.02 <= R <= 50 of the
shell-relative discrepancy between -Delta_5 phi and the transported K^2 e), for a two-series rational family with the cubic
source relation and the first two far-axis coefficient matches imposed as heavy penalties and an exact portrait certificate for
every final field, gives at 8, 16 and 24 parameters E = 0.340, 0.278, 0.251 at c_l = 0.68 and 0.378, 0.267, 0.260 at c_l = 0.74
(9.7 and 2.7 percent decrease from 16 to 24). The remaining discrepancy lies at intermediate and large radii (shell-band errors
about 0.3 for R >= 0.2, about 0.01 below). The family has one exactly identified gap: on the axis the transported vorticity has
no z^(-3 - 1/c_l) term while the family generates one with a coefficient U_1 (714 and 548 for the best fields at 0.68 and 0.74)
that was not constrained, and it lacks the transported z^(-1 - 3/c_l) power. The verifier has confirmed, for every final
field of this family (three at each of c_l = 0.68 and 0.74), that U_1 is nonzero (U_1 = 714.2235 and 547.9013 for the best
fields), with exact certificates of strictly outgoing transport along the positive axis, so, under the stated axis hypotheses, none of these
individual potentials is the meridional field of a single-source profile with nonzero source swirl; and that the stored vorticity fields and the E
values reproduce from the coefficients and the saved transport arrays (E differences at most 1.5e-15). The verifier has also
certified exactly, for each of these fields, that the meridional field has a single zero, the source at the origin, and that
every backward meridional orbit converges to it (an exact positive lower bound for W . grad log R on the compactified quadrant).
The verifier has also integrated the transport of all seven saved fields of this family (the six above and the free-c_l field
below) independently (81 radii from 0.02 to 50, 128 and 256
angles) and reproduced their E values to 1.8e-6, and for the two 24-parameter fields computed the global source strain
(S = 0.00804 and 0.01206, so that 2 K^2 S - 1 = 5.0e-6 and 1.1e-5 with the stored K), under smoothness and decay hypotheses that it
proved for these fields [verifier, floating point for the values; proofs cross-reviewed by the lead]. A free c_l in [0.55, 0.85] ends at the ceiling with
E = 0.223; in this family nothing observed marks c_l = 3/4. This is a quantified failure of one ansatz, neither a sign of
convergence nor a lower bound [independent referee, floating-point transport and reconstruction; axis formulas and U_1 values
lead-checked; verifier checks as stated].
A Newton-Krylov solve of the closed single-source problem itself (-Delta_5 phi = K^2 e[phi] with K^2 S[phi] = 1/2, phi odd in z
with source slope 1/2, the dilation fixed by the cubic source coefficient), started from the best fields of this family at
c_l = 0.68 and 0.74 in a larger trial space (the seed, two cubic source terms, and Gaussian functions of log R times odd
angular polynomials; 101 and 401 free coefficients), did not converge. With 401 coefficients E fell from 0.2507 to 0.1758
(c_l = 0.68) and from 0.2598 to 0.1317 (c_l = 0.74); with 101 it ended at 0.2562 and 0.2324. The largest shell error of the
401-coefficient fields is 0.79 at R = 1.98 and 0.52 at R = 2.66, and the error sits at radii 0.2 to 3 toward the pole (band RMS
0.29 and 0.19, against 0.009 and 0.008 for R from 0.02 to 0.2 and 0.09 and 0.11 for R from 3 to 50). The source amplitude rose to
K = 9.99 and 9.36 (S = 0.0050 and 0.0057), the cubic source relation held to 2.2e-3 and 6.7e-4 relative, and the second far-axis
vorticity coefficient has opposite signs in the elliptic and the transported field (148 against -2729 and 151 against -2903; confirmed by the verifier's independent axis quadrature, whose outgoing-axis hypothesis
is discharged by the global source certificate below),
because the trial space keeps the seed's second fractional tail fixed. Doubling the transport and collocation grids changed E by
at most 1.3e-6, and the verifier's independent transport of the four final fields (81 radii, 128 and 256 angles) gave
E = 0.2562, 0.2324, 0.1758 and 0.1317, within 2e-6 of the saved values [verifier, floating point]. This supports the stability
of the measured finite-shell E; it is not a discretization bound. For all four final fields the radial drift
W_m . grad log R = c_l + [2 mu phi - (1 - mu^2) phi_mu]/R is bounded below by a positive constant (interval enclosure over a complete
partition of the meridian, with explicit origin and exterior bounds) [verifier; the drift identity and the cover argument
lead-checked; the sampled values approach c_l - 1/2 near the source], so the origin is the only meridional stagnation point and
every backward characteristic converges to it: the single-source portrait of these fields is proved, which is what the
transport construction of h and e assumes. The smallest Jacobian singular values (0.02 to
0.06, with the gauge row) belong to modes at intermediate and far radii near the axis, and the final merit still decreased
slightly (0.10032 to 0.10011 and 0.08888 to 0.08875), so a stationary minimum was not demonstrated. Positive strain and a sampled
outflow condition held at every accepted step (sampled, not certified). This is an unconverged local search in a restricted,
non-nested trial space, not a floor [independent referee, floating point; K^2 S = 1/2, the source slope, the oddness, the
elliptic vorticity of the saved fields (central differences, relative 4e-4 or better), the saved shell errors and the leading
far-axis coefficient lead-checked; the starting and final values of E and the second far-axis coefficients are verifier-reproduced as stated; the
solve itself is not verifier-checked].
A second Newton-Krylov solve of the same closed problem, in exactly nested trial spaces, freed the far-field tails and
imposed the source and far-axis conditions by algebraic elimination, so that they hold to floating-point root tolerance. Trial space: the final field above, plus a cubic source term
z^3 (1 + R^2)^(-p-1) whose coefficient is fixed by the cubic source relation and three free quintic source terms
(z s^2, z^3 s, z^5 times (1 + R^2)^(-p-2)), plus clamped degree-five splines in log R on -7 <= log R <= 7 with 20, 40 and 80
equal intervals times odd angular polynomials mu P_2j(mu) (14, 16 and 18 angular functions), multiplied by R (1 + R^2)^(-p)
and a smooth cutoff supported in |log R| <= 7, plus four free angular tails with envelopes R (1 + R^2)^(-nu), nu = p, 2p,
p + 1, 3p (p = 1/(2 c_l)), switched on between R = e^2 and R = e^4 by a smooth cutoff. The dilation gauge holds the coefficient
of s z in the source expansion at its previous value. On every accepted iterate the cubic source relation held to 1.7e-11
relative or better (3e-14 or better on the four final fields; floating point), the first three far-axis vorticity coefficients of the elliptic and the transported field agreed to all
displayed digits on the production grid and within 1e-4 relative on a doubled transport grid (for example T_2 = -1901.06 in
both at the second level, where the previous solve had opposite signs; an independent extraction of the four pole coefficients
from the exact saved coefficients, with an independent quadrature for the axis amplitude, gives relative defects in T_1, T_2 and
T_3 of at most 8.5e-9 for all four fields, by quadrature refinement and not by interval enclosure [verifier]), and the forbidden axis coefficient U_1 was below
1e-10 in the production floating-point evaluation (exact rational evaluation of the saved coefficients gives |U_1| from 5.3e-11
to 5.6e-10, nonzero for all four fields [verifier]; the tail constraints hold to numerical root tolerance, not exactly). These potentials are Cartesian C^4 with C^3 meridional velocity and are not C^5: the fifth radial derivative jumps at the knots
(exact rational computation of the jumps at the internal knots, for all four fields below) [verifier]; they meet the C^2 minimum of the
class but are not smooth.

| c_l | level | free coefficients | accepted steps | E | E, doubled transport grid | solver wall time (s) |
|---|---|---|---|---|---|---|
| 0.74 | 1 | 405 | 21 | 0.0779 | 0.0779 | 889 |
| 0.74 | 2 | 783 | 4 | 0.0544 | 0.0544 | 1432 |
| 0.74 | 3 | 1601 | 2 | 0.0547 | 0.0547 | 1545 |
| 0.74 | 2, continued | 783 | 3 more | 0.0529 | 0.0529 | 2439 |
| 0.74 | 2a (24 angular functions) | 1175 | 2 | 0.0434 | 0.0434 | 2143 |
| 0.74 | 2b (49 radial intervals) | 1391 | 5 | 0.0391 | 0.0391 | 4190 |
| 0.74 | 3c (49 radial intervals, 32 angular functions) | 1855 | 25 | 0.0322 | 0.0322 | 5650 |
| 0.68 | 1 | 405 | 3 | 0.1084 | 0.1084 | 440 |

The doubled-grid column keeps the shell comparison quadrature fixed; a separate refinement of that quadrature changes E by 1.6e-4
to 3.2e-4 (at the second level from 0.05443 to 0.05460) [independent referee]. The starting values were 0.1317 (c_l = 0.74) and
0.1758 (0.68), so E fell by 59 percent at 0.74. At the second level the band
RMS errors are 0.0056, 0.075, 0.053 and 0.011 for R in 0.02 to 0.2, 0.2 to 3, 3 to 50 and 50 to 1e4, the largest shell error is
0.137 at R = 1.0, mu = 0.855, and about 71 percent of the squared error in the band 0.2 to 3 lies at mu > 0.75, near the axis.
The relative L2 norm of the closure defect on the wider domain rose from 0.080 at the start to 0.100 at the second level, so the
decrease of E is not a decrease of every norm. The source amplitude fell from K = 9.22 to 8.91 and 8.79 over the three levels
at 0.74 (S = 0.0059, 0.0063, 0.0065); K = 9.64 at 0.68. At the first level the linearized model predicted almost no further decrease (best linear least-squares
residual over the current residual 0.99995; smallest Jacobian singular values 0.021 to 0.066, with potential modes near
R = 8 to 14); this is a finite computational observation, not a proof of stationarity, since on these weak modes the
assembled Jacobian and independent centred directional differences disagree by up to 14 percent of the singular value. The second level was still decreasing (its last step lowered E by about 12 percent) when its time share ended. The primary search later ran the solver code of these first nested levels to its stop rule (merit decrease below 1 percent over 20 accepted steps): at c_l = 0.74 from the level-2 endpoint, 25 accepted steps ended at E = 0.0537 (0.0537 on doubled transport and collocation grids; band RMS values 0.0073, 0.075, 0.050 and 0.0091, largest shell error at R = 1.0), and at c_l = 0.68 a level-2 solve (783 coefficients) from the level-1 field ended after 24 accepted steps at E = 0.0786 (0.0786 on doubled grids; band RMS values 0.0068, 0.098, 0.089 and 0.011, largest shell error on the axis at R = 4.3) [primary search, running the referee's code; the c_l = 0.68 value independently reproduced, below]. The verifier froze both final fields and confirmed with its own operators that each potential is C^4 but not C^5 (39 nonzero fifth-derivative jumps at mu = 9/10), so the meridional velocity is C^3 and not C^4 [verifier]; the global source portraits of both fields are certified as well (interval enclosures with independent 224-bit replays, lower bounds 5.08e-5 at c_l = 0.74 and 6.88e-4 at c_l = 0.68, rounded down), so their full velocities are globally decaying Cartesian C^3 fields [verifier]. An independent fixed-K characteristic transport of the c_l = 0.68 field with the stored K gives E = 0.078597 with 128 and 0.078596 with 256 angular nodes, against the saved 0.078595, the largest shell error 0.156 at R = 4.34 and far-band E = 0.011 on 31 radii from 50 to 1e4 [verifier]. An independent fixed-K transport of the c_l = 0.74 field with the stored K gives E = 0.053678 with 128 and 0.053677 with 256 angular nodes, against the saved 0.053677, the largest shell error 0.121 at R = 1.0 and far-band E = 0.0091 on 31 radii from 50 to 1e4 [verifier].
The third level, limited by a memory cap of 1800 MiB per process to 200 Krylov directions per step and to a collocation grid
refined only from 281 by 192 to 301 by 208 points, did not lower E and has a narrow defect 0.346 at R = 0.001, near the inner
end of the spline interval and outside the E window (the largest inner value at the second level is 0.0023, at R = 0.010);
an independent fixed-K transport on 26 inner radii reproduces the level-3 peak (0.3463 at R = 0.00102, unchanged to 3e-7 when
the angular nodes are doubled) and gives a maximum of about 0.00142 at the second level on those 26 radii [verifier]. None of these four time-limited runs met the stop rule of 7.5
(merit decrease below 1 percent over 20 accepted steps); the two later primary-search level-2 runs described above did, and the level-3c continuation below stalled. For all four fields the global source portrait is certified (interval
enclosure of the radial drift, lower bounds 1.9e-4, 1.6e-4 and 4.4e-5 at levels 1 to 3 at c_l = 0.74 and 1.2e-4 at c_l = 0.68), so
their transported h and e are Cartesian C^3 and C^2 and the full velocity is a globally decaying Cartesian C^3 field (not C^4 in the meridional velocity, because of the exact knot jumps) [verifier proof, applied to the four certified fields]; a portrait certificate is not a closure check. This is again an unconverged search, not a floor [independent referee, floating point,
about 100 minutes on one core; lead checks from the saved grids of all four fields: E recomputed, q = K h and eta = K^2 e,
all to floating-point roundoff, the quintic-spline -Delta_5 phi of the saved phi against the saved elliptic vorticity (relative 2e-5 or
better for 0.02 <= R <= 50), the axis identity w e = 2h(h - 1) (3.5e-5 or better), 2 K^2 S - 1 by the trapezoid rule (4e-5 or
better), and the far-axis transport formulas for T_1, T_2, T_3 symbolically; verifier: an independent fixed-K characteristic
transport of the level-1 field at c_l = 0.74 gives E = 0.07793 with 128 and with 256 angular nodes, against the saved 0.07792,
with shell angular-L2 relative differences of the transported vorticity of at most 1.5e-3 (largest absolute sample difference
0.0135); the same independent transport of the level-2 field at c_l = 0.74, with the stored K, gives E = 0.054432 with 128 and
with 256 angular nodes, against the saved 0.054432, the largest shell error 0.137 at R = 1, far-band E = 0.0108 on 31 radii from
50 to 1e4, and shell angular-L2 relative differences of the transported vorticity of at most 8.1e-5 (largest absolute sample
difference 1.5e-3); the same independent transport of the level-1 field at c_l = 0.68 gives E = 0.10842 with 128 and with
256 angular nodes, against the saved 0.10841, the largest shell error 0.233 at R = 1.63, far-band E = 0.0196, and shell
angular-L2 relative differences of the transported vorticity of at most 3.9e-3 (largest absolute sample difference 0.058);
the same independent transport of the level-3 field at c_l = 0.74 gives E = 0.054667 with 128 and with 256 angular nodes, the largest shell error 0.149 at R = 1, far-band E = 0.0116, and shell angular-L2 relative differences of the transported vorticity of at most 6.0e-6 (largest absolute sample difference 1.2e-4); all four closures fail the handoff criterion E < 1e-2].
A third continuation [independent referee, floating point, 99 minutes on one core] took the second level three accepted
steps further (E 0.0544, 0.0533, 0.0534, 0.0529; the frozen merit fell by 0.07 percent in the last step, close to the stop
rule) and then refined the angular space from 16 to 24 functions mu P_2j(mu) with the same radial splines (level 2a in the
table, 1175 coefficients; the zero-padded start represents the identical field), with angular collocation of 128 Gauss nodes on
each of [0, 0.75] and [0.75, 1] and 421 radii from 1e-3 to 1e4. To stay under the memory cap it replaced the Krylov basis by an
assembled Jacobian stored on disk, a streamed QR factorization and LSQR (peak 457 MiB at level 2a; on the same level-1
Jacobian its step agrees with the original one within 9e-7 relative). The two accepted level-2a steps lowered E to 0.0473 and
0.0434 (0.0434 on the doubled transport and collocation grid, 0.0435 with a separate 161 by 512 comparison quadrature); both
levels ended at their time share without meeting the stop rule. The refinement did not remove the near-axis error: the
largest shell error rose from 0.122 to 0.130 (at R = 1, mu = 0.89), the share of the squared error at mu > 0.75 in the band
0.2 to 3 rose from 71 to 76 percent, most of the decrease came from 3 <= R <= 50 (band RMS 0.051 to 0.032), the band 50 to 1e4
nearly doubled (0.0095 to 0.018) and the wide-domain relative L2 norm fell only from 0.094 to 0.093. The constraints held as
before (absolute cubic-relation residual 3.2e-15, T_1, T_2, T_3 of the elliptic and transported fields equal on the production grid, U_1 below
1e-11; K = 9.18, S = 0.0059). A geometric fit to the three level-2a values gives a limit of about 0.035; with two decreases
and trust-limited steps this has low confidence, and along the weakest singular direction the assembled Jacobian and fully
re-closed differences disagree by 20 percent, so the endpoint spectra do not support a floor estimate either. Lead checks
from the saved grids of both endpoints: E recomputed (0.0433989), q = K h and eta = K^2 e to roundoff, the quintic-spline
-Delta_5 phi of the saved phi against the saved elliptic vorticity (1.4e-6 relative or better for 0.02 <= R <= 50), the axis
identity w e = 2h(h - 1) (3.5e-6 or better), 2 K^2 S - 1 by the trapezoid rule (1.2e-5) and T_1 from the axis integral (5e-6 relative or better)
[lead]. Both fields pass the verifier's 522 independent spline, derivative and source checks each, and exact rational
fifth-derivative jumps at interior knots (39 nonzero in each field) show that their potentials are C^4 and not C^5, so the
meridional velocities are C^3 and not C^4 [verifier]; their global source portraits are certified as well (interval enclosure,
lower bounds 3.9e-4 for the continued level 2 and 2.0e-4 for level 2a), so their transported h and e are again Cartesian C^3 and
C^2 and the full velocity a globally decaying Cartesian C^3 field [verifier proof]. An independent fixed-K characteristic transport with the stored K gives, for the continued level 2 and for level 2a, E = 0.052949 and 0.043399 with 128 and with 256 angular nodes, against the saved 0.052949 and 0.043399 (differences 8e-8 and 3e-7), the largest shell errors 0.122 and 0.130, both at R = 1, and far-band E = 0.0095 and 0.0181 on 31 radii from 50 to 1e4 [verifier].
A fourth continuation [independent referee, floating point, 99 minutes on one core] first located the 20 percent
disagreement: it came from the finite-difference step in ill-scaled tail columns, and a forward tangent of the transport agrees
with fully re-closed differences to 1.3e-4 relative. It then tested whether the trial space can represent the remaining
defect. With the source K^2 e[phi], the cubic coefficient, K and the transported tail targets frozen at the level-2a endpoint and
the linear constraints kept, the least-squares potential has E_lin = 0.0114 in the level-2a space, 0.0104 with 9 knots inserted at the midpoints of the nine radial intervals that meet [0.2, 3] (49 intervals, 24 angular functions) and 0.0071 with 40 intervals and 32 angular functions
(largest shell error 0.017 at R = 1.10). An independent reconstruction of these three fits from their saved coefficients, with its own Laplacian evaluator, reproduces 0.0114, 0.0104 and 0.0071 against the saved frozen source and against an independently transported frozen source, with far-band values 0.0072, 0.0072 and 0.0023 on 31 radii, and an exact rational correction of at most 3.2e-9 in the tail coefficients makes the four elliptic far-axis coefficients equal exactly to those of the frozen endpoint and preserves the source coefficient, without changing these values; the endpoint coefficients match the transported targets only to the tolerance of the production grids [verifier]; fits that minimize the core error alone reach 0.0104, 0.0094 and 0.0052 but have far-band errors between 490 and 8230 [verifier]. These are not closures, since the source is not recomputed from the fitted potential;
they show, in this discrete frozen-source sense (no lower bound or resolution estimate for the nonlinear problem is implied), that most of the level-2a defect is not a representation limit of the trial space but a mismatch between phi and the source that phi transports. The refined level 2b (49 intervals, 24 angular functions, 1391 coefficients, exactly zero-padded
start) took five accepted Gauss-Newton steps with the corrected tangent: E fell to 0.03904 at the fourth step and ended at
0.03915 at the fifth, which the frozen-weight merit accepted although E rose by 0.28 percent; the linear model of the last step
predicted a merit decrease of only 0.69 percent, and each Jacobian cycle took about 19 minutes. A matched corrected step in the
coarse space reached 0.0414, so the decrease cannot be attributed to the radial refinement alone. The near-axis error is
unchanged in character: largest shell error 0.123 at R = 1, mu = 0.896, 78 percent of the squared error in 0.2 to 3 at
mu > 0.75, band RMS values 0.0041, 0.060, 0.027 and 0.0063, and the residual at R = 1, mu = 0.888 grew in magnitude from 1.89
to 2.05; the wide-domain relative L2 norm is 0.088, K = 9.49, S = 0.0055, and E = 0.03915 on doubled transport and collocation
grids. Lead checks from the saved grid of the level-2b endpoint: E recomputed (0.0391480), q = K h and eta = K^2 e to roundoff,
the quintic-spline -Delta_5 phi against the saved elliptic vorticity (1.6e-6 relative or better for 0.02 <= R <= 50), the axis
identity (2.8e-6), 2 K^2 S - 1 by the trapezoid rule (1.2e-5) and T_1 from the axis integral (4.5e-6 relative) [lead]. The verifier registered the saved level-2b field independently: an exact change of basis of its stored coefficients (45 coarse and 9 inserted fine splines per angular function) to the 54-spline basis, checked by 13245 exact conversion checks (13230 polynomial identities and 15 other checks), and 909 operator checks; the potential is C^4 but not C^5 across 48 knots, so the meridional velocity is C^3 [verifier, exact rational conversion]. Its global source portrait is certified as well (interval enclosure with an independent 224-bit replay, lower bound 7.5e-4), so its transported h and e are again Cartesian C^3 and C^2 and the full velocity is a globally decaying Cartesian C^3 field [verifier]. An independent fixed-K characteristic transport with the stored K gives E = 0.039149 with 128 and with 256 angular nodes, against the saved 0.039148, the largest shell error 0.123 at R = 1, and far-band E = 0.0063 on 31 radii from 50 to 1e4 [verifier].

A fifth continuation [independent referee, floating point, about 101 minutes on one core] tested the fixed-point route suggested by the frozen-source fits, in a level 3c of 49 radial intervals and 32 angular functions (1855 free coefficients; it contains level 2b and the 40-interval, 32-function space of the frozen fits by exact zero padding, and the retransported start has E = 0.03915). With the source frozen at the start, the least-squares potential of this space has E_lin = 0.0045 (0.011 with 24 angular functions), but recomputing the source from that potential (one step of the frozen-source fixed-point map, with the normalization, the cubic relation and the far-axis conditions imposed again) gives E = 3.13, with the largest shell error 9.7 at R = 37 near the axis. Plain iteration of this map accepted one half step (E from 0.0391 to 1.65) before the scalar root for the source strain was lost, and an Anderson iteration of depth five took 30 safeguarded damped steps and accepted none of its 29 accelerated proposals (last E 0.185); neither lowered E below the start [independent referee; the iteration counts and E values checked by the verifier from the saved histories]. The failure of the tested root procedure does not show that no other root exists. The derivative of the map at the start, assembled as an 1855 by 1855 matrix from a tangent that agrees with fully re-closed differences to 5e-6 relative, has the real eigenvalue 12.59 as its spectral radius and 214 eigenvalues outside the unit disk, a floating-point count for the stored matrix that changed to 215 and 218 under random relative perturbations of 1e-10 [independent referee; the eigenvalue and the count reproduced by the lead with a separate eigen-decomposition]. For the stored matrix A and the stored real vector v obtained from a floating-point eigenvector calculation near 12.59 (no exact eigenpair is certified or needed), v^T(A - I)v > 0 in exact rational arithmetic, so no damped map (1 - beta)I + beta A with constant beta > 0 is a contraction in the coordinate norm of the solver [verifier, exact certificate; lead check]. For the exact map the same conclusion (in any norm, through the real eigenvalue above 1) holds only if the stored matrix is close enough to its derivative, which is not bounded, and the start is not a fixed point. The leading mode has its largest relative amplitude in the far tail (R about 38, mu near 1), while its unnormalized vorticity is largest at R = 1.26 near the axis. Gauss-Newton on the closed residual in the same space was the only tested method that lowered E, and it stalled. It accepted 25 steps: two with newly assembled full Jacobians (E 0.0383 and 0.0371; the two complete assemblies took 28 and 25 minutes), thirteen chord steps with the second Jacobian (E to 0.03216, the last of them lowering E by 0.005 percent) and ten steps from fresh tangent products in 24-dimensional subspaces, which the solver's merit function accepted (with E allowed to rise by at most 10 percent) while E stayed between 0.0322 and 0.0324 and the merit fell by 0.13 percent in total. The best state, the last chord step, has E = 0.03216, 18 percent below the start (0.03216 on doubled transport and collocation grids and 0.03226 with a separate 161 by 512 comparison quadrature; band RMS values 0.0044, 0.051, 0.018 and 0.0042; largest shell error 0.106 at R = 1.10, mu = 0.927; relative L2 norm 0.075; K = 10.2, S = 0.0048). At this state the frozen-source fit again reaches E_lin = 0.0051, and recomputing the source from it again gives E = 2.53, so the mismatch between phi and the source it transports persists. The 5650 s of the table include the fixed-point runs. Lead checks from the saved grid of the best state: E recomputed (0.0321615), q = K h and eta = K^2 e to roundoff, the quintic-spline -Delta_5 phi against the saved elliptic vorticity (2.7e-6 relative or better for 0.02 <= R <= 50), the axis identity (5.8e-6), 2 K^2 S - 1 by the trapezoid rule (1.2e-5), T_1 from the far-axis amplitude (5e-6 relative), and 79 percent of the shell-normalized squared error in 0.2 <= R <= 3 at mu > 0.75, as at level 2b [lead]. The verifier registered the saved level-3c field independently from its stored coefficients: 909 operator checks on 14061 saved points and 29 exact regularity and provenance checks pass, and all 48 interior fifth-derivative jumps at mu = 9/10 are nonzero (the largest -1626.7), so the potential is C^4 but not C^5 and the meridional velocity is C^3 but not C^4 [verifier, exact rational arithmetic; the 48 jumps reproduced by the lead to 1e-11 with a separate spline evaluation]. Its global source portrait is certified (interval enclosure with an independent 224-bit replay, lower bound 8.60e-4, rounded down), so its transported h and e are Cartesian C^3 and C^2 and the full velocity is a globally decaying Cartesian C^3 field, and an independent fixed-K characteristic transport with the stored K gives E = 0.032162 with 128 and with 256 angular nodes, against the saved 0.032162, the largest shell error 0.106 at R = 1.10 and far-band E = 0.0042 on 31 radii from 50 to 1e4 [verifier].

4.6 Failure map (summary of 4.3 to 4.5). Each row is one search
class; "best" is the smallest measured value of the residual used in that class (rho_max for the Euler residual of section 2,
E for the closure defect of 4.5), with its provenance. The two measures are not comparable. No rho_max row reaches B1
(rho_max <= 1e-3 at two levels), and no E row reaches the handoff criterion of 7.5 (E < 1e-2 at two levels), which would
only pass a field on to the primitive-variable validation and is not an acceptance test.

| search class | c_l | levels or trial spaces | best measured value | why it did not converge |
|---|---|---|---|---|
| generic and S1-structured seeds, q0 free or pinned, c_l free or fixed (4.3) | 0.505 to 0.74 (start) | ball degree 24, one shell | rho_max 6.7 to 79.5 per starting c_l with swirl kept [primary search] | swirl removed in 214 of the 311 Stage I runs (failure class), and 103 of the 335 runs of this class pass the swirl magnitude filter; free c_l mostly stays near its start, some runs reach a bound; Newton-Krylov finds no root (strain of the wrong sign) |
| c_l = 1/2 experiment (4.3) | 0.500 | ball degree 24, two radial bases | rho_max 12.5 with swirl kept, 4.7 without [primary search; counts and minima confirmed by the verifier]; exported 12.5 state 14.4 [verifier]; its degree-32 level 7.47 with swirl fractions 0.088 and 0.057 [verifier] | swirl below the magnitude filter in 29 of 50 runs, and in three of the four follow-up runs of the two best states (the degree-32 refinement of the best state passes the filter with a reduced core fraction); 3.3 requires an uncountable stagnation set |
| independent single-source, Green and ring searches (4.4) | 0.74; free c_l | three continuation levels | rho_max 4.07, 6.54, 5.71 [verifier] | order-one core residuals; free c_l ends at the bound 0.7495; ring objective at least 5.66 |
| pinned-amplitude single-source ladder (4.4a, 5) | 0.749 (imposed bound of a free-c_l run) | ball degree 36, 48, 64; outer interface radius 5, 10, 20 | rho_max 1.79 (R5), 1.92 (L1), 2.90 (L2) [verifier] | axial momentum in the axis collar (origin ball for R5 and L2, shell 2 for L1); interface jumps 4.8e-3 to 6.8e-3 and first far-field correction mismatch 0.025 to 0.9998 (R5, L1, L2); no consistent decrease with degree (4.24, 2.79, 3.37 at degrees 36, 48, 64, q0 = 2.5) |
| reflection class (4.4a) | 0.749, 0.74 | ball degree 36, 48 | rho_max 4.46 [verifier] (4.44 [primary search]) | rho_max rises with degree (10.4; 26.6 and 32.2 at 0.74) |
| fixed-c_l continuation from 0.749 (4.4a) | 0.745 to 0.65 | ball degree 36 (24 and 48 at 0.74) | rho_max 2.37 at 0.745 (q0 = 5.5; 2.39 at q0 = 3.5), 10.7 at 0.74 (8.0 at degree 48) [primary search]; registered 2.34 for the q0 = 5.5 state at 0.745, interface jump 1.3e-3 [verifier] | residual grows away from 0.749 (24.7 at 0.70); core moves outward at 0.65; swirl lost at q0 = 5.0 |
| direct positive-strain seeds (4.4a) | 0.74, 0.70, 0.68, 0.65, 0.60, 0.55 | ball degree 24, 36, 48, 64 | rho_max 2.65 to 3.27 at 0.74 (degrees 36, 48, 64), 2.60 at 0.745 (free c_l stopped at the imposed bound; registered 2.70 [verifier]) and 3.37 at 0.68 (degree 48) [primary search]; frozen states 3.59 and 2.74 (0.74, degree 36, 1500 and 3000 iterations), 2.74 (0.74, degree 36, 500 further Levenberg-Marquardt iterations), 2.71 and 2.78 (0.74, degree 48), 2.84 (0.74, degree 64), 3.58 and 5.10 (0.68) [verifier] | degree levels at 0.74 (2.86 at 36, 2.85 and 2.81 at 48, 2.95 at 64) stay at an order-one value, which becomes 8.23 and 8.54 with the outer interface at R = 5 and 20 and 7.55 with another shell weighting; steps in c_l raise it to 7.5 to 36 within 0.02 and to 31 and 110 at 0.70; the three tested restarts after relative coefficient perturbations of 1, 3 and 10 percent returned to 2.75 to 3.12; at 0.68 (35.1 at 24, 3.38 to 3.50 at 36, 3.37 and 5.12 at 48, 4.85 at 64) they do not decrease and further iterations move the value between 3.4 and 6.3; in the three tested free-c_l runs from the 3.50 and 0.74 states c_l moved to the imposed upper bound (0.749, 0.80, 0.745), and in four from earlier ladder seeds of this class it drifted down to 0.506 to 0.596; direct runs at fixed c_l = 0.745, 0.7425 and 0.7375 gave 3.09, 6.89 and 10.7; a 1000-iteration step to c_l = 0.6667 (near 2/3) gave 53.4; core moves outward at 0.65; no transfer at 0.60 and 0.55 |
| closed single-source problem, rational families with penalties (4.5) | 0.60 to 0.74 (free c_l to 0.85) | 8, 16, 24 parameters | E = 0.251 (0.68), 0.260 (0.74) [independent referee; values reproduced by the verifier] | nonzero axis coefficient U_1, which excludes a single-source profile under the stated axis hypotheses; far-axis vorticity of the wrong sign in the 16-coefficient family; free c_l to the ceiling |
| closed single-source problem, Gaussian Newton-Krylov (4.5) | 0.68, 0.74 | 101 and 401 coefficients | E = 0.1758, 0.1317 [independent referee; reproduced by the verifier] | second far-axis coefficient of the wrong sign (fixed seed tail); weak far modes |
| closed single-source problem, nested splines with free tails (4.5) | 0.68, 0.74 | 405, 783, 1175, 1391, 1601, 1855 coefficients | E = 0.032 at 0.74, 1855 coefficients, and 0.079 at 0.68, 783 coefficients (primary search, running the same code) [independent referee; lead-checked; E of all ten saved nested fields, including the 1855-coefficient field, reproduced by the verifier] | not converged; Gauss-Newton stalled at 0.032 although a frozen-source fit reaches 0.0045 (the frozen-source value holds only in the discrete frozen-source sense of 4.5 and is not a resolution estimate for the nonlinear problem; recomputing the source from that fit gives 3.1); the stored matrix approximating the derivative of the frozen-source map admits no positive constant damping that is contractive in the coordinate norm (floating-point eigenvalue 12.6; open for the exact map); error concentrated near the axis at radii 0.2 to 3, persisting through the tested angular and radial refinements; memory-limited third radial level |
| closed problem for the fractional S1-pair family (4.5) | at least 0.68 for positive strain | finite scan | closure defect 5.84 [independent referee] | moments of the wrong sign |

In total the main search of the primary search finished 526 runs by 2026-10-29T08:51:42Z (the nested closed-problem solves it ran with the referee's code, the last of which ended at 08:59:22Z, are not among them) (by class: 335 generic and S1-structured, 50 at c_l = 1/2, 35 pinned-amplitude ladder, 4 reflection, 31 fixed-c_l continuation, 71 direct seeds; 257 of them pass the swirl magnitude filter) [primary search; class partition checked by the verifier], and the independent search has 197 search records and the validation 27 registered validation records (4.4) [verifier].

## 5. Candidates

No state met the pre-candidate threshold B1 (rho_max <= 1e-3), so there is no serious candidate in the sense of the
specification. For transparency five selected registered states are described with the quantities measured for them; quantities that
were not measured are marked. They are failed numerical iterates with order-one residuals, not approximate profiles, and no
convergence rate has been established.

| quantity | R5 | L1 | L2 | S74 | S74d48 |
|---|---|---|---|---|---|
| c_l, alpha | 0.749, 0.33511 | 0.749, 0.33511 | 0.749, 0.33511 | 0.74, 0.35135 | 0.74, 0.35135 |
| columns per field: ball, shell, exterior (phi / q) | 319, 625, 100 / 50 | 319, 625, 100 / 50 | 553, 1089, 132 / 66 | 319, 625, 125 / 50 | 553, 1089, 165 / 66 |
| outer interface radius (working gauge) | 5 | 10 | 10 | 10 | 10 |
| rho_max (equation, place) | 1.79 (axial momentum, origin ball, collar) | 1.92 (axial momentum, shell 2, collar) | 2.90 (axial momentum, origin ball, collar) | 2.74 (reduced swirl, shell 1, random) | 2.71 (reduced swirl, shell 1, random) |
| m_max (equation, place) | 8.57 (reduced vorticity, shell 11) | 21.0 (reduced vorticity, shell 11) | 5.03 (axial momentum, shell 2, collar) | 7.98 (reduced swirl, shell 1, random) | 7.93 (reduced swirl, shell 1, random) |
| core and far swirl fractions | 0.703, 0.646 | 0.598, 0.592 | 0.676, 0.577 | 0.665, 0.611 | 0.658, 0.602 |
| a_eff (reporting gauge) | 0.571 | 0.644 | 0.593 | 0.717 | 0.720 |
| first far-field correction, relative mismatch | 0.025 | 0.084 | 0.9998 | 0.017 | 0.99 |
| pressure, Green against direct Newton (20 points) | 6.8e-9 | 9.4e-9 | 7.3e-9 | 7.6e-6 (degree 40), 1.2e-8 (degree 80) | 5.3e-6 (degree 40), 1.4e-8 (degree 96) |
| largest relative interface derivative jump | 4.8e-3 | 6.1e-3 | 6.8e-3 | 1.6e-2 | 1.2e-2 |
| convergence rate | none | none (no controlled refinement) | none | none | none |

All entries [verifier], from the registered validations and supplemental verifier diagnostics; the pressure entries are the largest absolute differences at the 20
points: for R5, L1 and L2 at the highest spherical Green order (80 for R5; 80/128/96 for L1 and L2); for S74 and S74d48 the direct Newton integral against the Green pressure at the baseline degree 40 and at the refined highest retained degrees, 80 for S74 and 96 for S74d48, where the differences are 1.2e-8 and 1.4e-8); they are absolute differences in the working gauge at those points, not shell-normalized
bounds, and a uniform pressure error bound is not available for any state.

State R5 (the state L1 below with its outer element interface moved from R = 10 to R = 5 in the working gauge and 1000
further iterations; c_l = 0.749 and q0 = 3.5 as for L1, the same column counts, shell element 2 <= R <= 5, axis source at
z = 0.053 in the working gauge) [verifier, registered validation of the frozen export]:
- rho_max 1.79 (axial momentum, origin ball, collar set) and m_max 8.57 (reduced vorticity, shell 11): A1 fails by a factor
  1.8e6 and A2 by a factor 8.6e4. The primary search had measured 1.58 on its own held-out points, which do not contain the
  registered collar sets.
- Reporting gauge: dilation factor 0.2359; a_eff = 0.571; largest sampled vorticity 7.68 (not a proved global maximum).
- Swirl: integrated core and far swirl fractions 0.703 and 0.646 (the magnitude part of B2; stability across levels not tested).
- Far field: relative mismatch of the first nonlinear correction 0.025 (absolute 6.2e-3 on the sphere).
- Interfaces: maximum relative derivative jump 4.8e-3 (A8 and B4 fail).
- Pressure: the Green pressure at order 80 agrees with direct Newton quadrature to 6.8e-9 at 20 points (orders 64 and 80 differ
  by 5e-12; at order 40 the difference was 3.8e-6); finite-difference gradients at five points agree to 6.0e-8. The dominant
  origin defect is unchanged by this refinement: the full axial momentum residual at the origin is 0.0437 and the collar rho
  stays 1.7939 at Green degrees 32, 80 and 96.
- Balances: raw relative energy defects 0.156, 0.034 and 0.0021 on the balls of radius a_eff, 4 a_eff and 16 a_eff in the working
  gauge (helicity 0.130, 0.081, 0.017), so A9 fails; adding the measured residual work and interface fluxes closes the energy
  identity to 1.1e-11 (1.4e-15 after refining the pressure to order 80/128/96 and the volume quadrature to 48 by 96, which leave
  the raw defects unchanged), which checks the computation, not the approximation.
- Extremes: at the detected vorticity maximum the relative defect of the stretching identity is 0.31; a later peak search found
  a reduced-vorticity residual ratio 9.96 on shell 11 with the frozen denominator, a lower bound above the registered m_max.
- Cartesian finite differences at 14 points (extended-precision stencil arithmetic; float64 velocity, Jacobian and momentum
  arrays) agree with the analytic-derivative momentum residual to 3.3e-10 at the smallest of five steps, so the registered defect is not an artifact of the reduced variables.
- A value-only float64 projection at Legendre degrees 24, 36 and 48 on four shells gives rho 0.783 at all three degrees, with
  largest momentum differences from the native evaluator 3.7e-7, 2.2e-12 and 1.3e-12 at the three degrees (a four-shell
  comparison sharing the retained pressure, not the full registered score), so the defect is not a differentiation artifact.
- Moving the interface inward lowered rho_max from 1.92 to 1.79 and m_max from 21.0 to 8.57 without changing the order of the
  defect; moving it outward to R = 20 gave held-out rho_max 8.40 [primary search] (7.2).

State L1 (seeded from a single-source field, with a prescribed axis source of pinned amplitude q0 = 3.5 in the working gauge; a prescribed source does not certify that every backward characteristic converges to it) [verifier, registered validation of
the frozen export; per-equation maxima extracted by the lead from the verifier's registered record]:
- c_l = 0.749 (fixed in the exported state; reached as the imposed upper bound of a free-c_l run), alpha = 0.33511.
- Basis per field: 319 ball columns (Cartesian polynomials of degree <= 36 with Legendre degree <= 24, R <= 2 in the working
  gauge), 625 shell columns (log-Chebyshev degree 24 times Legendre degree 24 on 2 <= R <= 10) and an exterior of factored power
  laws R^(-e) (100 columns for phi, 50 for q); continuity across the interfaces is imposed by least squares.
- Reporting gauge (unit leading far-field norm): dilation factor 0.2359; core size a_eff = 0.644; maximum vorticity 7.69 at the
  axis point z = -0.178 (sampled search, not a proved global maximum).
- Scaled RMS residuals rho (maximum over the 18 registered dyadic shells and the origin ball, over Gauss, random and collar point
  sets): momentum (vector) 1.92, axial 1.92 (shell 2, R in [4, 8] a_eff, collar set), radial 0.90, azimuthal 0.79, reduced swirl
  1.38, reduced vorticity 1.00, divergence 3e-17. Scaled maximum residuals m: momentum 3.31, reduced swirl 4.74, reduced
  vorticity 21.0 (shell 11, R in [2048, 4096] a_eff). A1 (rho_max <= 1e-6) fails by a factor 1.9e6 and A2 (m_max <= 1e-4) by a factor 2.1e5.
  These are maxima over the fixed registered point sets. A later adversarial check (38912 fresh quasi-random points and bounded
  local maximizations) finds m = 24.4 for the reduced vorticity, a larger sampled lower bound for the same pointwise maximum, not
  a different definition of the registered score; 70- and 100-digit evaluation at selected points changes nothing, so the
  defects are not floating-point cancellation.
- Swirl: the swirl part of the leading far-field coefficient has L2 norm 0.59 on the unit sphere (leading norm 1); its angular
  polynomial changes sign (exact rational witnesses), which is impossible when every backward characteristic converges
  to the source (section 4.3); that basin property is not established for the numerical state.
- Far field: the saved first nonlinear correction differs from the one forced by the Euler equations by 8.4 percent (relative,
  on the sphere).
- Pressure: full-space Newton pressure from the bulk source. At the lower spherical Green orders (32/64/48 and 40/96/64) the
  two resolutions differed by up to 6.9e-5 in P and from direct Newton quadrature by up to 3.4e-5; the pressure source has
  angular content above degree 32 (relative norm up to 2.6e-3). At the higher orders 64/112/80 and 80/128/96 the Green and
  Newton values agree to 9.4e-9 (absolute) at 20 points, 1.1e-8 relative to the local pressure RMS, the refinement changes P
  and grad P by 7.4e-12 and 3.5e-12, and the dominant residual (axial momentum, shell 2 collar) stays 1.9237. This confirms
  the bulk pressure at the selected points, not every A7 moment or interface term. The stress-surface correction is at most
  2.1e-6 (P) and 2.8e-5 (grad P). A check by Cartesian finite differences (shared pressure) confirms the differentiation to 7e-10, and an
  independent projection at Legendre degrees 24, 36 and 48 gives the same order-one residual (1.43 on four shells).
- Dynamical checks: core and far swirl norm fractions 0.598 and 0.592. The sampled swirl maximum lies on the axis at
  z = -0.178 with q = 3.84, above the source value 3.5; there an exact profile has u_r/r = -1/2 (the swirl equation at a
  critical point of q, a dilation-invariant condition), while the state has |u_r/r + 1/2| = 0.171 and swirl residual 1.31.
  The axis first integral of the swirl equation drifts by 0.059 and 0.056 (relative) on the two axis branches from the source
  out to 64 a_eff; relative vortex-stretching defect 0.34 at the sampled vorticity maximum. A9 and B5 fail.
- Interfaces: maximum relative derivative jump 6.1e-3 (A8 and B4 fail).
- Convergence: there is no convergence rate to report. The next level of the same branch (L2 below, ball degree 48, started
  from a longer degree-36 continuation, not from this state) has registered rho_max 2.90 against 1.92 here, while m_max falls
  from 21.0 to 5.03 [verifier]; the primary search measures 2.55, 2.33 and 2.83 at ball degrees 36 (the continuation), 48 and
  64 [primary search]. These states have different optimization histories, so the sequence is not a controlled refinement.

State L2 (same branch, c_l = 0.749, q0 = 3.5; axis source at z = 0.039 in the working gauge) [verifier, registered validation
of the frozen export, 2938 s; per-equation maxima extracted by the lead from the verifier's registered record]:
- Basis per field: 553 ball columns (degree <= 48, Legendre degree <= 32), 1089 shell columns (log-Chebyshev degree 32 times
  Legendre degree 32 on 2 <= R <= 10), exterior 132 columns for phi and 66 for q.
- Reporting gauge: dilation factor 0.2359; a_eff = 0.593; maximum vorticity 7.70 at the axis point z = -0.168 (sampled).
- rho maxima over the origin ball and 18 shells: momentum 2.90 (axial, origin ball, collar set), radial 0.26, azimuthal 0.98,
  reduced swirl 1.58, reduced vorticity 0.28, divergence 2.4e-17. m maxima: momentum 5.03 (axial, shell 2, collar set), reduced
  swirl 4.58, reduced vorticity 1.11. A1 fails by a factor 2.9e6 and A2 by a factor 5.0e4.
- Swirl: its leading swirl polynomial is certified positive on [-1, 1] (exact Bernstein bounds); core and far swirl norm
  fractions 0.676 and 0.577; at the sampled swirl maximum |u_r/r + 1/2| = 0.168; axis first-integral drifts 0.050 and 0.035
  (A9 and B5 fail).
- Far field: the relative mismatch between the saved and the forced first nonlinear correction is 0.9998 (0.084 for L1).
- Interfaces: maximum relative derivative jump 6.8e-3 (A8 and B4 fail).
- Spectral decay of both states (largest native coefficient per Legendre degree over the radial columns of one element, relative
  to the largest in that element; native normalizations differ between elements, so only within-element ratios are meaningful).
  Neither state is resolved in angle. Swirl, even degrees: in the ball from about 0.1 to 0.2 at degree 10 down to 1.0e-2 at the
  truncation degree 24 (L1) and 4.8e-4 to 1.8e-3 at even degrees 26 to 32 (L2); in the exterior between 1.2e-2 and 4.4e-2 up to degree 24
  in both states and still 4e-3 to 5e-3 at degrees 26 to 32 (L2). Meridional potential, odd degrees: exterior 7.1e-3 to 8.2e-3 at
  degrees 21 to 23 (L1) and 4.7e-4 to 2.2e-3 at degrees 25 to 31 (L2). Radially (L1) the envelopes fall to 2e-10 (potential, ball), 7e-8
  (potential, shell), 1.6e-4 (swirl, ball) and 4e-5 (swirl, shell) at the last index. Second angular derivatives weight degree n by about n^2, so tails of this size are not small
  in the equations. [lead, from the exported coefficients; the L1 values coincide with the data of the verifier's L1 figures]

State S74 (direct positive-strain seed at fixed c_l = 0.74 with q0 = 2.5, after 3000 iterations at ball degree 36; section
4.4a) [verifier, registered validation of the frozen export, 2633 retained-array checks, and the follow-up audits]:
- rho_max 2.74 and m_max 7.98, both in the reduced swirl equation on random points of shell 1. That equation does not involve the
  pressure, so A1 fails by a factor 2.7e6 and A2 by a factor 8.0e4 independently of the pressure truncation. The momentum maxima
  (rho 2.56, axial and vector, shell 2, collar set) use the bulk pressure at Legendre degree 32 and are finite-truncation
  diagnostics (3.7).
- Reporting gauge: dilation factor 0.2863; a_eff = 0.717; largest sampled vorticity 5.89 (not a proved global maximum). Core and
  far swirl fractions 0.665 and 0.611.
- Far field: relative mismatch of the first nonlinear correction 0.017. Interfaces: maximum relative derivative jump 1.6e-2
  (A8 and B4 fail).
- Pressure follow-up: raising the bulk pressure degree from 32 to 40 changes the pressure by 3.0e-5 and its gradient by 9.4e-5;
  direct Newton integration agrees with the degree-40 Green pressure to 7.6e-6 at the comparison points. At full bandwidth (Legendre degrees 64 to 80, above the proved source degree bound 50) the pressure changes by 1.0e-12 between the last two of three quadrature levels and the direct integral agrees to 1.2e-8 [verifier; finite-point comparison].
  With the degree-32 pressure the relative raw energy defects at a_eff, 4 a_eff and 16 a_eff are 0.209, 0.127 and 0.029; the
  finite vorticity-maximum identity defect is 0.451 and the strain at the sampled |q| maximum differs from -1/2 by 0.226 (both
  identities hold for exact profiles, 3.6) [verifier].
- Its descendants at ball degree 48 are registered at 2.71 (S74d48, below) and 2.78 (from the 1500-iteration state) [verifier];
  the degree-64 descendant measures 2.95 on the primary held-out points [primary search] and 2.84 under the registered evaluation (reduced swirl equation on the first shell, m_max 8.40, interface jump 3.4e-3, first-correction mismatch 1.00) [verifier]. The levels have different optimization
  histories, so there is no convergence rate.

State S74d48 (the ball-degree-48 level of S74, 1500 iterations started from S74; the lowest registered value at c_l = 0.74) [verifier, registered validation of the frozen export, 2633 retained-array checks, and the follow-up audit with
54 pressure, 119 balance and Cartesian and 2390 adversarial checks]:
- rho_max 2.71 and m_max 7.93, both in the reduced swirl equation on random points of shell 1, which does not involve the
  pressure; core and far swirl fractions 0.658 and 0.602.
- Pressure: raising the bulk pressure degree from 32 to 40 changes the pressure by 2.1e-4 and its gradient by 1.3e-4; direct
  Newton integration agrees with the degree-40 Green pressure to 5.3e-6 at the comparison points; at full bandwidth (degrees 80 to 96, above the bound 66) the last refinement changes the pressure by 5.1e-13 and the direct integral agrees to 1.4e-8 [verifier; finite-point comparison].
- Reporting gauge: dilation factor 0.2863; a_eff = 0.720; largest sampled vorticity 5.78.
- Far field: relative mismatch of the first nonlinear correction 0.99 (0.017 for S74). Interfaces: maximum relative derivative
  jump 1.2e-2 (A8 and B4 fail).
- Identities: relative raw energy defects 0.201, 0.125 and 0.029 at a_eff, 4 a_eff and 16 a_eff with the degree-32 pressure;
  finite vorticity-maximum identity defect 0.436 and |q|-maximum strain defect 0.218. The finite stagnation search found one
  axis source, without proving that it is the only stagnation point.
- The registered sequence from S74 to S74d48, 2.74 to 2.71, changes the order-one residual by 1.4 percent.

## 6. Independent validation

The independent evaluator was constructed from the exchange-format basis description and the frozen specification only; no primary implementation was reused in it. Later adversarial audits did inspect primary solver code (notably the frozen-meridional-field swirl solve and the differentiated variable projection). For the exported
single-source pilot at c_l = 0.6 it reproduces all 765 sample values (velocity to 3.1e-15, eta to 3.3e-14) and measures, on all
registered shells and the origin with separate Gauss, random and collar point sets, rho_max = 13.18 (axial momentum, collar) and
m_max = 34.4 (eta, collar): A1 and A2 fail. The full-space pressure is consistent (two spherical Green resolutions agree to
2.7e-13, direct Newton quadrature to 1.3e-8 on 20 points), so pressure evaluation does not explain the order-one momentum defects.
The interface Taylor check finds relative derivative jumps up to 4.1e-4 (A8 fails). The finite-ball energy and helicity identities,
with residual work and interface flux terms included, close to at most 3.8e-10 (energy) and 2.3e-14 (helicity) at R/a_eff = 1, 4, 16, while the raw energy
defects are 14.5, 4.8e3 and 5.1e4: the identity is implemented correctly and the field fails the energy balance decisively. The
coefficient-tail audit compares the saved first far-field correction H with the correction G forced by the saved leading tail
and the full-space angular pressure: ||H - G||/||G|| = 0.997 and 1.03 for the two exports, and the defect lies mostly in angular
modes the basis represents. For these two saved fields, replacing the exterior by the forced correction makes ||H - G||/||G|| <
1.5e-11 but breaks the interface matching (phi jumps 0.11 and 0.14). This is not a general incompatibility: a globally smooth
chart without interfaces in which the first correction is exact (to 1.1e-10) still fails in the core (reduced-equation screens at
three resolutions give rho_max at least 6.7, 4.7 and 2.1). The verifier's
own single-source pilot at c_l = 0.6 fails registered acceptance with rho_max = 5.33, m_max = 14.6. No tested state qualified as a serious numerical candidate.

Best state of the primary search at the end of Stage I (single-source ladder, c_l = 0.749, q0 = 3.5; section 4.4a). The full
registered validation (origin and 18 shells, separate Gauss, random and axis-collar point sets, independently differentiated
reduced and primitive equations, full-space pressure, interface derivative traces, first-correction comparison; 1373 s wall time)
gives rho_max = 1.924, m_max = 21.0, interface jump 6.1e-3 and first-correction mismatch 0.084: rejected by A1, A2, A8 and B4.
Fourth-order Cartesian finite differences of the saved values at 14 points (origin, axis, collar, core, shell, exterior) converge
with the step (momentum differences 4.5e-5 down to 7.1e-10 at five successively halved step sizes), which confirms the differentiation, not the
pressure (the pressure is shared in that check) and not a small residual. A value-only projection onto an independent
representation (degrees 24, 36, 48 on four shells) reproduces the large defects (component rho maxima 1.427 on those shells,
largest momentum differences from direct differentiation 7.2e-10, 4.3e-13 and 3.8e-13 at degrees 24, 36 and 48). The finite-ball energy and helicity balances, with both
spherical interfaces split and their flux jumps retained, have relative defects (absolute defect over the largest balance term)
0.173, 0.070, 0.029 for energy and 0.143, 0.227, 0.103 for helicity at R = a_eff, 4 a_eff, 16 a_eff, unchanged under quadrature
refinement, while the identities corrected by the residual work and interface terms close to 6e-11 and 2e-12 in absolute value (at most
1.4e-14 and 4.6e-13 relative to the largest balance term): the energy-flux
part of A9 fails for this export, and the implementation is consistent. The degree-48 state of the same branch has a leading
swirl polynomial that is certified positive on [-1, 1] by exact Bernstein bounds, unlike the degree-36 state. Its registered
validation (all 19 radial units, the same point sets and checks, 2938 s) gives rho_max = 2.902 (axial momentum, origin ball,
collar set), m_max = 5.03 (axial momentum, shell 2, collar set), interface jump 6.8e-3 and first-correction mismatch 0.9998:
rejected by A1, A2, A8 and B4. For L1 the bulk pressure was refined to Green orders 64/112/80 and 80/128/96, where Green and
direct Newton values agree to 9.4e-9 at 20 points and the dominant residual is unchanged (1.9237). For eight exported states (among them L2, S74 and S74d48 of section 5), at Legendre degrees 64 to 96 above the proved degree bound of the bulk source, the pressure changed by at most 4.7e-12 and its gradient by at most 1.1e-12 between the last two of three quadrature levels, and a direct Newton integral agrees to 1.4e-8 at 20 points; these absolute finite-point comparisons alone do not establish the relative pressure checks and the moment and coefficient checks of A7, and they change no rejection [verifier]. The dynamical checks fail
for both states (A9, B5; section 5). The matching-radius-5 state R5 of section 5 (full registered validation of the origin ball and all
18 shells) gives rho_max = 1.794 (axial momentum, origin ball, collar set),
m_max = 8.57 (reduced vorticity, shell 11), interface jump 4.8e-3 and first-correction mismatch 0.025: rejected by A1, A2, A8 and
B4; it is the lowest registered value of the campaign. [verifier] The direct-seed state S74 at c_l = 0.74 and its two
ball-degree-48 levels (section 5) give rho_max = 2.743, 2.706 and 2.779, each in the reduced swirl equation, which does not
involve the pressure: rejected by A1 and A2 independently of the pressure truncation, and by A8 and B4. [verifier]

At the actual axis source of both states the closure relations of a single-source profile fail in sign (section 7.2): the
measured source jets are q_z = -0.0126 (L1) and -0.113 (L2) where the relation q_z = 2K phi_zz/(1 + c_l) requires +0.0351 and
+0.0430, and eta = -0.0507 and -0.450 where 4K^2 phi_zz/(1 + c_l)^2 requires +0.141 and +0.172 [verifier; the relations
lead-checked].

Closed single-source fields (4.5). The verifier registered the ten saved nested-spline fields from their stored coefficients (exact
rational conversion and operator checks; its summary table of the ten fields is among the accompanying artifacts), proved for each that the potential is C^4 and not C^5 at its knots, certified the single-source portraits of all ten by interval enclosure, reproduced E for all ten with its own fixed-K characteristic transport (differences in core E of at most 7e-6; this does not bound far-band or pointwise differences),
reproduced the frozen-source fits of 4.5 with its own Laplacian evaluator, and certified in exact rational arithmetic that the
stored matrix approximating the derivative of the frozen-source fixed-point map at level 3c admits no positive constant damping
that is contractive in its coordinate norm (open for the exact map) [verifier].

Stage III (from 2026-10-29T11:59:44Z; no optimization by the verifier). The portable single-command reproduction of R5 and an
interruption and fresh-process resume of its native route both reproduced the rejection with rho_max = 1.793889555852889 and
m_max = 8.565619692094037, the resumed and uninterrupted runs giving bitwise identical arrays (9.1). The two remaining exported
c_l = 0.745 states of 4.4a were registered (rho_max 2.34 and 2.70; A1, A2, A8 and B4 fail), so all 21 exported primary-search
states now have full registered evaluations, all rejected. Protected follow-ups of both c_l = 0.745 states (54 pressure, 119
balance and Cartesian and 2390 adversarial checks each) confirmed the retained diagnostic values; they concern rejected
approximations, the raw relative energy-flux defects at 1, 4 and 16 times a_eff lie between 0.017 and 0.20, and the complete
A7 checks remain open. Rereadings of the foundational proofs and of the implementation
(derivatives, residuals, pressure, metrics and checkpointing) confirmed eight scoped groups each; these are static reviews, not
further tests or error bounds [verifier]. The final claim audit of the report and its label verdicts are summarized at the
end of section 1 [verifier, Stage III].

## 7. Failure mechanisms and the most promising next experiment

7.1 Swirl collapse. Most runs (214 of the 311 Stage I runs of the primary search) lower the residual by removing the swirl. Nontrivial swirl-free
decaying profiles do not exist (3.1), and S1 profiles are not limits of profiles whose swirl tends to zero under the controls of
3.4a (ii); this does not exclude sequences with vanishing swirl that lose those controls, but the optimizer moves toward the
trivial profile, and swirl collapse is not evidence of a nontrivial solution.
7.2 Order-one residuals with swirl retained. When the source amplitude is pinned, residuals stay of order one in the core and in the tail.
The first nonlinear far-field correction is matched only approximately or not at all (relative mismatch between 0.014 and
1.0001 among the primary-search states with c_l above 1/2 whose registered evaluations are reported in sections 4 and 5). Imposing it exactly
broke the matching for two saved fields. The primary search slaves it to the leading tail by optimizer rows, which the
saved fields meet only approximately (independently measured mismatches 0.084 for L1 and 0.9998 for L2); the independent search
builds it exactly (to 1.1e-10) into an interface-free chart, which still leaves order-one core residuals. Reweighting the far rows
did not change this in the tested runs. The measured residual also depends on the artificial outer interface radius of the
piecewise representation: at c_l = 0.749 and q0 = 3.5, interface radii 5, 10 and 20 (working gauge) gave holdout rho_max 1.58,
1.88 and 8.40, from different starts and iteration budgets [primary search; the registered value of the radius-5 state is 1.79, section 5 [verifier]]. At c_l = 0.74, from one 3000-iteration state, radii 5, 10 and 20 gave 8.23, 2.86 and 8.54, and a different radial-shell weighting gave 7.55 while the reduced-equation residual fell; chains of small steps in c_l from that state, and from the 3.38 state at c_l = 0.68, raised the value to 13.7 to 35.9 (c_l = 0.735 to 0.70) and to 7.49 to 163 (0.685 to 0.71), while the training cost of the first step down was 1.35e-2 against 1.46e-2 for its parent, so the low held-out values are not continued in c_l (4.4a) [primary search].
For the two earlier states L1 and L2 of section 5 the defect is located more precisely. At a swirl-emitting axis source z0 of
a single-source profile, differentiating the swirl and vorticity equations on the axis gives q_z = 2K phi_zz/(1 + c_l) and
eta = 4K^2 phi_zz/(1 + c_l)^2 with K = q(0, z0) [lead-checked symbolically]. Both states violate these relations in sign
(section 6) [verifier]. Integrating the swirl and the vorticity along the characteristics of each state's own meridional field
(phi frozen, plus an additive correction eps (z - z0) exp(-(r^2 + (z - z0)^2)/0.09) with eps = 3.0e-7 for L1 and 1.9e-7 for L2,
which raises phi_z at the source from its stored value 0.4999997 or 0.4999998 to exactly 1/2 so that a smooth swirl with
q = K at the source exists, and leaves phi_rr and phi_zz there unchanged; piecewise classical values are used across the remaining interfaces) and inserting the transported vorticity into the five-dimensional Newton kernel for the source strain,
K^2 S = (3/4) int_0^infinity dR int_{-1}^{1} mu (1 - mu^2) eta dmu (R and mu centred at the source; the kernel lead-checked on
test fields), gives K^2 S = -0.81 (L1) and -0.51 (L2) where a single-source profile needs +1/2 [independent referee; reproduced by the
verifier with a separate implementation: -0.8119 and -0.5136, with changes below 5e-6 under angular, radial-step,
starting-radius and cutoff refinements; a rigorous enclosure of the tail is open]. For L2 the contributions are
+0.03 from source distances below 0.3, -0.13 from 0.3 to 3, -0.38 from 3 to 30 and -0.03 from 30 to 1000 (working gauge;
band contributions reproduced by the verifier: +0.0301, -0.1331, -0.3831 and -0.0273);
the contribution beyond 1000 is estimated from the leading asymptotic decay, not enclosed. The
stored swirl of L2 differs from the transported swirl by 2, 33, 73 and 81 percent (relative L2 norm in the measure dlogR dmu)
for R in 0.001 to 0.3, 0.3 to 3, 3 to 30 and 30 to 1000, and the stored vorticity from the transported one by order one in every range [independent
referee: characteristic integration, Green quadrature and two quadratures of the kernel; the swirl and vorticity differences
are not verifier-checked]. So for these states
the single-source closure has order-one defects: for the repaired meridional fields and the swirl generated from the source
along their characteristics, the computed strain is negative. A rigorous transport and tail error bound establishing S < 0 would exclude every real source
amplitude K (K^2 S = 1/2 is then impossible) for the normalized transported swirl of each field; no such bound is available
(the tail enclosure is open). Excluding every other swirl for these fixed meridional fields would also need the source-basin
and uniqueness hypotheses of the transport statement for q; within the tested
setting the meridional field itself would have to change. These are measured
fixed-point defects, not a bound on the distance from the states to a profile. An earlier frozen-field swirl
solve of the primary search, which had suggested an 80 percent change of the swirl coefficients and a cost increase by a
factor 2.5e8, had
omitted the swirl interface equations, so that its ball, shell and exterior blocks were decoupled and the shell and exterior
swirl vanished [verifier]; with C^2 matching of the swirl at both interfaces imposed as hard numerical constraints, a spectral solve for the frozen L2 field
reproduces the characteristic swirl to 0.15 percent [independent referee]. The corrected primary solve with interface rows, for
the frozen L1 field, gives a swirl that differs from the stored one by 0.48 (relative L2 on the inner holdout grid; at most 1.83
pointwise), whose leading far-field swirl coefficient is one-signed in mu while the stored one changes sign four times, and with
which the vorticity rows rise from 1.1e-3 to 0.36 in weighted cost; for the frozen L2 field the same solve gives 0.44 (at most
1.65 pointwise, at R = 1 to 4) and vorticity rows 2.18 against 3.5e-4. These transported swirls satisfy the source relation for
q_z that the stored swirls violate in sign [primary search]. Moving the swirl linearly from the stored one to the transported one
with the L1 meridional field frozen raises the relative vorticity residual from 0.022 to 0.20 at the midpoint and 0.42 at the
endpoint; refitting the meridional field alone with the endpoint swirl frozen stalled at relative vorticity residual 0.10 and
relative swirl residual 0.12 (the refitted field no longer transports that swirl), holdout rho_max 17.1, and at the midpoint
reached rho_max 6.73 [primary search; not independently reproduced]. The tested meridional refits did not close the vorticity
equation; the small vorticity residual of the coupled states uses a swirl that their own meridional field does not transport.
7.3 The single-source closure loop. For a prescribed field the induced source strain must be positive, which is impossible if
the characteristic swirl decreases away from the symmetry plane and decays (3.12 (v)); in the tested seeds the positive strain came from axial
amplification near the source. The elliptic reconstruction of their vorticity has a negative axial cubic coefficient, and in the
damped iteration the strain changed sign when the updated cubic coefficient did (3.12 (v)); this is a measured coincidence, not a
proved mechanism. With more freedom (4.5) the potential defect decreases over the tested 4, 8 and 16 coefficients while the
vorticity discrepancy stays at 0.3 or above; in those fields the failures are located at the source (reconstructed axial cubic
coefficients far from the input ones) and on the far axis (wrong vorticity sign), where the potential norm is weak. Minimizing
the vorticity discrepancy directly, with the cubic source relation and the first two far-axis conditions included as penalty
terms (not enforced exactly), brings it to 0.25 to 0.26 at 24 coefficients, with a slowing decrease and the remaining error at
intermediate and large radii; a Newton-Krylov solve of the closed problem from those fields in a larger, still restricted trial
space lowered it to 0.18 (c_l = 0.68) and 0.13 (0.74) at 401 coefficients without converging, and a nested solve with
free tails and the source and far-axis conditions imposed by elimination (to floating-point root tolerance) lowered it to 0.108 (0.68, 405 coefficients; 0.079 at 783 coefficients in a later run of the primary search with the same code) and 0.054 (0.74, 783 coefficients), with a third radial level that did not improve, and angular and radial refinements lowered it to 0.043, 0.039 and 0.032 (0.74, 1175, 1391 and 1855 coefficients) without moving the error away from the axis, while iterating the frozen-source fixed-point map did not lower it (4.5). The seeds that do reach a positive strain need large
source amplitudes (q0 about 10.8 at c_l = 0.60, 3.9 at 0.68, 2.5 at 0.74), above the pinned values of the main sweep.
7.4 Portraits with a saddle. In the smooth stratum the saddle strain is quantized (one more condition than unknowns, heuristically);
in the Cartesian C^2 class it is free (3.14). For the model interior cusp |z|^k in a polynomial basis on [-1, 1],
derivative-aware approximations converge only at algebraic rates and raw truncations need not converge in the second
derivative at the endpoints (3.14 (v)); these model rates do not establish a rate for a solver, for the Euler residual, for a
complete fractional profile or for a basis in z^2. In the closed S1-pair
problem for one explicit family, in a finite scan, the vorticity that makes the source strain positive also pushes the sources
apart and reverses the saddle (3.14 (vi)).
7.5 Most promising next numerical experiment. Continue the nested Newton-Krylov solve of the closed single-source problem
(end of 4.5). Here the four original nested levels ran only to time-limited endpoints, the two later level-2 runs at c_l = 0.74 and 0.68 met the stop rule at E = 0.054 and 0.079, and the level-3c Gauss-Newton continuation stalled at E = 0.032; a continuation should therefore change the method or the trial space as below rather than only add steps. Trial space as there: the source jet z/2 plus cubic and
quintic source terms tied by elimination to the relation of 3.12 (v) inside decaying envelopes, free far-field tails with the first
three far-axis vorticity coefficients matched and U_1 removed, and nested degree-five splines in log R times odd angular
polynomials; unknowns phi and the source amplitude K, residual -Delta_5 phi - K^2 e[phi], normalization K^2 S = 1/2 and one
dilation gauge; c_l fixed at 0.74 and 0.68 first, then free. Changes indicated by the run: (i) run every level to the stop rule
(merit decrease below 1 percent over 20 accepted steps; the 1175-coefficient level took about 18 minutes of wall time per accepted step, the 1391-coefficient level about 19 minutes per fresh Jacobian cycle and the 1855-coefficient level 25 to 28 minutes per completed full Jacobian on a shared core, so roughly 6 to 9 hours of solver wall time for 20 steps if every step needs a fresh Jacobian) and record the smallest Jacobian singular values and their modes, checked against fully re-closed differences; (ii) keep the memory-light solvers of the last three continuations (the third with the assembled Jacobian on disk, streamed QR and LSQR, which held 1175 coefficients at 457 MiB; the fourth with streamed QR and an SVD of the reduced small matrix, which held 1391 coefficients at about 478 MiB, and the fifth, which held 1855 coefficients at about 750 MiB), all three under the cap of 1800 MiB (about 1.89 GB) per process, whereas the Krylov solver held the 1601-coefficient level to 200 directions; (iii) a change of the trial space or of the merit function rather than more steps of the tested iterations: with the source frozen, a space of 49 radial intervals and 32 angular functions represents the potential to E_lin = 0.0045 (0.0051 at the best state), but recomputing the source from that fit gives E = 3.1 (2.5), plain and Anderson-accelerated iteration of that map did not lower E, and the stored matrix approximating its derivative has the floating-point eigenvalue 12.6 and admits no positive constant damping that is contractive in the coordinate norm (4.5; open for the exact map); Gauss-Newton on the full closed residual, the only tested method that lowered E, stalled at E = 0.032 with 1855 coefficients (its merit function fell by 0.13 percent over the last ten accepted steps), so a continuation should keep at least 32 angular functions, treat the far-axis tail explicitly (the leading unstable mode of the stored derivative has its largest relative amplitude at R about 38 near the axis, and 186 of its 214 unstable modes peak at radii between 3 and 50) and, near the axis at radii 0.2 to 3, where 76 to 79 percent of the remaining squared error lies at mu > 0.75 after the angular refinements from 16 to 24 and to 32 functions and the radial refinement of the intervals that meet that band, use an angular representation adapted to the axis (functions of 1 - mu^2, collocation clustered at mu = 1), since no tested refinement changed the near-axis share; (iv) collocation and the E window extended to the inner end of the spline
interval, where the third level developed a narrow defect outside the window; (v) at the last level a smooth radial basis in
place of the splines, since spline fields are C^4 potentials only. Criterion for passing a field to the primitive-variable
validation: E below 1e-2 at two consecutive levels with the single-source portrait certified. The portrait part is complete for all ten nested fields (levels 1, 2 and 3, the continued level 2, levels 2a, 2b and 3c and the stopped level-2 solve at c_l = 0.74, and level 1 and the stopped level-2 solve at c_l = 0.68); the E part is met by none of them. This is a handoff criterion, not the acceptance test, which
remains the registered primitive-variable validation.
Reason for the ranking: within the closed single-source formulation E at c_l = 0.74 decreased from 0.260 (rational family) to
0.132 (Gaussian Newton-Krylov) to 0.054 (nested solve), 0.043 (angular refinement), 0.039 (radial refinement) and 0.032 (angular refinement to 32 functions); the 1391-coefficient level stagnated (its last accepted step raised E by 0.28 percent) and the 1855-coefficient level stalled (its merit function fell by 0.13 percent over its last ten accepted steps); the frozen-source fits show only that the trial space represents the potential of a frozen source to 0.007 and 0.0045, and since recomputing the source from such a fit raises E to 3.1, they do not locate a nearby closed solution; the remaining error is localized near the axis at intermediate radii. E is a closure norm specific to this formulation; it is not
comparable with the Euler residual rho_max of the coupled states R5, L1 and L2 (for which no source-normalized E was computed)
or with the closure defect 5.84 of the S1-pair calculation. The evidence for convergence is weak: E fell from 0.078 to 0.054 between the first two levels and to 0.043 after the angular refinement, the restricted third level did not improve, the wide-domain norm rose from 0.080 to 0.100 and then changed little (0.093), the far band doubled under the angular refinement, a geometric fit to the level-2a values pointed to a limit near 0.035 rather than zero (low confidence), the radially refined level stopped decreasing at 0.039, and the 32-function level stalled at 0.032; whether the defect falls to discretization level under
(i) to (iv) is what the experiment tests. This is a practical priority based on the tested seeds. The projected S1-pair
iteration of 3.14 (vi) discarded the generated fractional terms, so it does not rank an appropriately represented fractional
S1-pair search, which is the second option (saddle exponent k as an unknown, representation in the accompanying audit,
section 5g (h)).

## 8. Elapsed time and resources

Campaign start 2026-10-28T17:59:44Z. Stage I ended at 2026-10-29T00:59:44Z and Stage II at 11:59:44Z; Stage III (validation and
reporting, no discovery or refinement optimization) ended with the team stop at 16:44:44Z, 22 h 45 min after the start. The
team was stopped then so that the final write-up finishes inside the 24-hour budget; the write-up (document edits and the
assembly of the published folder, no research computation) ended at 2026-10-29T17:02:05Z, 23 h 2 min after the start, so the whole
campaign used 23 h 2 min of its 24 hours. All times are measured (process logs, file timestamps, scheduler records); nothing is
estimated unless stated. Core-hours stated as allocated are the number of allocated cores times elapsed wall time, not process
CPU time.
- Lead (formulation, analysis, report): one CPU core, no GPU. Agent sessions (first and last session records) 2026-10-28T18:00:24Z to 2026-10-29T00:00:24Z,
  00:01:01Z to 06:00:55Z, 06:01:27Z to 11:58:51Z and 11:59:23Z to the team stop at 16:44:44Z, then the final write-up session
  from 16:46:11Z to 2026-10-29T17:02:05Z. Independent-referee computations ran on the same core, one process each, at most
  two at once: 31 questions completed by 2026-10-29T12:54:37Z (the last one; no referee process ran after it) with summed wall time 1340 minutes (7.7 to 101.9 minutes each; concurrent
  questions shared the core, so this is not core time) [lead ledger]. In each of the 17 questions
  launched before 2026-10-29T00:25Z the referee process, following a standing instruction in its own tool configuration to
  consult a further hosted model, ran client code that tried to obtain cloud credentials for such a model; every attempt failed at
  credential retrieval before any model request (no model response appears in any log), so no remote model computation occurred
  and no further model contributed to any result. From 00:25Z every question forbade remote services explicitly, and the logs of
  those questions contain no such client code [lead scan of all question logs].
- Primary search: five GPUs until 2026-10-28T20:31Z and four after that (two job slots per GPU), and six CPU cores at low
  priority, from the first launch at 2026-10-28T19:37Z. At 2026-10-29T00:17:45Z it had 341 finished jobs, 21.2 GPU-slot hours
  summed over jobs and about 28 allocated core-hours (six cores times elapsed time). All GPU allocations were withdrawn at
  00:57:59Z and the running GPU jobs were stopped at 00:58:14Z; the 370 finished runs of this first GPU phase sum to 23.8
  GPU-slot hours (recount from the run records; a first ledger entry gave 373 and 23.9). From 01:06:41Z the search ran on CPU
  only (five single-thread workers and a driver), resuming from checkpoints. GPUs 0 to 2 were made available again at
  02:51:04Z and used from 04:59:18Z.
  Totals at the Stage II freeze (11:40Z): 90 runs completed on CPU (the CPU-only phase ran from 01:06:41Z to 04:59:18Z; runs
  resumed on CPU completed until 05:42:07Z), one core each at low priority. Their recorded elapsed times, captured before each
  run's final validation, sum to 19.4 hours (69994 s); for the six jobs resumed from GPU checkpoints this includes 2239 s of
  earlier GPU segments (about 18.8 hours remain), the 90 final validations add 10398 s that are not in the sum, and none of
  these is CPU consumption [verifier check of the run records]. The second GPU phase (from 04:59:18Z) has 70 finished runs and
  8.2 GPU-slot hours. The 53 bounded invocations of the nested closed-problem solver, one core each, between 05:32:25Z and
  08:59:22Z, have 23031 s (6.4 hours) of summed invocation wall time, not measured CPU time [verifier pairing of the invocation
  logs]. These per-phase totals are the frozen 11:40Z values; a later rerun of the totals script counts the Stage III resume
  test in place of the earlier test run of the same name and is not used.
  The final failure map lists 526 finished runs. The per-phase counts (370 + 90 + 70 = 530) include four test runs of the first
  GPU phase (the resume test, an aborted first attempt of it, an amplitude-parametrization test and a homotopy-stage test, 787 s
  of slot time in total) that are not search runs and are not in the failure map; the other 526 run records match the 526 rows
  one to one [lead recount of the run records]. The result of the last search run was written at 08:51:42Z (supervisor
  completion 08:51:52Z) [lead and referee check of the run records]; the size of the primary-search directory at the freeze is
  recorded as 302M in the disk-usage output of the primary-search ledger.
  In Stage III no discovery or refinement optimization ran. The primary search ran its operator suite three times on one core
  (wrapper wall times 9.2, 8.9 and 8.9 s; the first belongs to the attempt that was later cut), twice more from fresh copies
  of its artifacts (12:41:07Z and 12:43:14Z, 6.6 and 6.5 s of test time, the second with self-tests of four exported states), and disposable optimization
  restart tests on GPU 0: a first attempt cut by a shell time limit (about 110 s, 12:00:36Z to 12:02:27Z), a test of 291.6 s of
  wrapper wall time (about 12:03:17Z to 12:08:09Z) and a repaired rerun of the whole suite from 12:21:52Z to 12:26:55Z (about
  303 s: the 8.9 s operator wrapper and a resume wrapper of 293.8 s from 12:22:01Z). These are wrapper wall times, not measured
  GPU execution times [primary search; verifier check of the logs].
- Independent validation: two CPU cores at low priority. GPUs were allocated to it until the withdrawal at 2026-10-29T00:57:59Z
  (three until 2026-10-28T20:31Z, one after that) and one again from 02:51:04Z, which it did not use. A per-process monitor
  sampled from 2026-10-29T00:57:32Z; summing each sampled process's largest lifetime CPU counter once gives at least 79452 CPU
  seconds (22.1 CPU hours, 49 s of them the monitor's own) by 16:39:12Z, the last sample before the monitor was stopped at
  16:40:23Z, a lower bound that omits jobs before 00:57Z, processes
  too short to be sampled and increases after the last sample; the largest sampled resident memory of one process was 594 MB,
  an observed maximum and not a certified peak [verifier process-counter audit]. Before the withdrawal it used GPUs only in operator tests: 18 timed GPU-using test invocations (17 completed, one timed
  out) sum to 217 s of whole-process wall time, which includes CPU work, setup and teardown and is therefore not GPU time;
  three further GPU test records carry no process timing, so its total earlier GPU use cannot be reconstructed. Its
  optimizations and evaluations ran on the CPU [verifier record audit].

## 9. Artifacts and figures

The accompanying artifacts (the folder published beside this report) contain: a start file with a map of the deliverables;
the formulation documents (mathematical formulation, obstruction audit, origin and axis regularity, far-field analysis,
full-space pressure) and the pre-registered acceptance specification; the numerical methods, failure analysis and runbook of
the primary search with its parameter sweep, candidate leaderboard and failure map; the independent validation log; the
figures with their data; the numerical code (solver, supervisor and worker, sweep, revalidation and resume scripts, operator
tests, optimizer configurations, environment lock file, hardware inventory) with the exported coefficients, basis
definitions and evaluation self-tests of the registered primary-search states; the source code, tests and environment lock
files of the independent validator with the exported R5 state; the symbolic and numerical check scripts of the report author
with their outputs; and a hash manifest. The original assembly record lists 678 files (27738050 bytes, about 28 MB, including the hash manifest); the current contents are indexed in the accompanying artifacts. Not included, because of
the size limit of the published folder: the full run archive of the primary search (run folders, all optimizer checkpoints,
logs and run ledger), the complete validation bundle (about 190 MB, with its evidence records and the checksum manifest that
its single-command reproduction verifies) and the external referee's reports with their code and outputs. The assemblies
checked by the independent verifier in Stage III (the last one of 2026-10-29T15:43:51Z, about 11100 checksum-listed files,
about 217 MB) contained all of these; the published folder and its manifest were assembled after the team stop and were not
checked by the verifier.

Figures. Every figure shows approximate states that are not solutions; the data of each figure are stored next to it, and
the start file of the accompanying artifacts lists the location of every figure file.
- F1 Residual versus spectral resolution: the best holdout rho_max per level with its dominant equation (all plotted primary-search states have outer interface radius R = 10) for the pinned-amplitude
  single-source ladders and the reflection-class ladder of 4.4a, and in a separate panel the independent single-source ladder of
  4.4, whose representation and levels differ. All displayed residuals exceed the acceptance threshold, and no displayed series establishes convergence to an accepted
approximation; the levels of each series (for example 14.6, 10.7, 8.0 for the c_l = 0.74 chain and 2.86, 2.81, 2.95 for the c_l = 0.74 direct seed, shown with the separately optimized degree-24 run of the same seed, 5.41, which is not a refinement ancestor of the other levels) have different optimization histories. [primary
search; verifier audit of the figure data]
- F2 Residual versus spatial radius: registered component ratios of the L1 state on all 18 dyadic shells. [verifier]
- F3 Spectral coefficient decay: per-degree angular envelopes and radial envelopes of the native coefficients of the L1 and
  L2 states. [verifier; the top-degree values agree with the lead's separate extraction]
- F4 Swirl and poloidal field distributions of the L1 state on an 81 x 145 meridional grid, with the element interfaces
  marked. [verifier]
- F5 c_l continuation: per c_l and basis level, the smallest holdout rho_max among states with outer interface radius R = 10 and core and far swirl fractions at
  least 0.05 (the swirl magnitude filter of the failure map; the stability part of B2 is a separate test), the fixed-c_l continuation chains from c_l = 0.749, the small-step chains from the c_l = 0.74 and
  c_l = 0.68 direct-seed states, and the start and end values of the free-c_l runs. [primary search; verifier audit of the figure data]
- F6 Far-field convergence: full-sphere L2 norms of the field and of the first remainder against R, with the coefficient-tail
  mismatch. [verifier]
- F7 Energy-flux identity errors: the balance terms and the defect, normalized by the largest balance term. [verifier]
- F8 Axis and origin residuals: exact-axis reduced residuals and the origin-region defect. [verifier]
- F9 Interface jumps by field and derivative order. [verifier]
- F10 Pressure differences at the retained comparison points. [verifier]
- F11 Closed single-source problem (4.5): (a) the discrepancy E against the number of free coefficients for the Gaussian trial
  spaces (not nested), the nested spline spaces at c_l = 0.68 and 0.74, and at c_l = 0.74 the continued level 2 with its
  angular (1175 coefficients) and radial (1391) refinements and the further angular refinement to 32 functions (level 3c,
  1855 coefficients, E = 0.032), with the criterion E = 1e-2; (b) the relative shell error against R at c_l = 0.74 for the
  start field, the three nested levels and the three refinements (shells beyond R = 50 exist only for the nested and refined
  fields). No level reaches the criterion. [independent referee; plotted by the lead from the saved fields, values lead-checked]

9.1 Commands. Exact command lines and usage instructions are given in the accompanying artifacts; the procedures of the validation project were run in the complete validation bundle,
of which only the source code is published. This section describes what each procedure does and records its tests. The procedures rerun in the protected Stage III (from 2026-10-29T11:59:44Z, no discovery or
refinement optimization) are the portable R5 reproduction, three resume tests (the primary optimizer worker, the general validation
evaluator and the native validation route used for R5) and the primary operator suite; their Stage III outcomes are given with
each item. All processes use the Python 3.12.13 interpreter recorded in the environment lock files with one numerical thread.
- Launch (numerical project): the durable job supervisor in the accompanying artifacts (detached, polling every 15 s, with the GPU list set in
  the environment) runs the queued optimizer jobs; the sweep generator queues jobs by sweep name.
- Monitor (numerical project): the supervisor heartbeat file (running jobs, counts and devices, rewritten every 30 s), the
  supervisor log, a heartbeat file in each job folder, and the ranking script in the accompanying artifacts, which writes the candidate leaderboard and the
  parameter sweep table ranked by the held-out rho_max.
- Resume one interrupted optimizer job (numerical project): rerunning the worker in the accompanying artifacts on the job continues it from its
  last atomic checkpoint; restarting the supervisor resumes every interrupted job. The resume path was tested by the accompanying artifacts' resume test
  on a disposable job before the sweep (terminated at iteration 220, resumed at iteration 220) and again in Stage III (SIGTERM at
  2026-10-29T12:03:37Z after a checkpoint at iteration 403, relaunch and reload from that checkpoint at 12:03:40Z, run finished
  at 12:08:08Z, 291.6 s of wrapper wall time on GPU 0; this shows a restart from the checkpoint, not equality with an
  uninterrupted solve), and in a repaired rerun with exit-status logging (SIGTERM at 12:22:21Z after a checkpoint at iteration 405, first worker exit 3 at 12:22:22Z, reload at 12:22:24Z, exit 0 at 12:26:55Z, 293.8 s of wrapper wall time; its saved iteration counter, 5405, double counts the 405-row prefix of the 5000 iterations) [primary search; logs checked by the verifier], and it was used for real when the GPUs were withdrawn:
  the six interrupted jobs were requeued on CPU at 2026-10-29T01:06:41Z and reloaded their checkpoints at 01:06:44Z (five jobs)
  and 01:21:59Z (the sixth) [primary search; verifier check of the logs].
- Validate a saved state without optimization (validation project): the reproduction wrapper in the accompanying artifacts, with the packages of
  its reproduction lock file available, verifies the bundled checksums and reruns the registered evaluation of R5 with the
  independent implementation on one core at low priority. Its native validation driver (applied to the bundled R5
  export with a new output folder) must return exit code 2 (completed rejection; 544 s of wall time in the retained run), and
  the wrapper returns 0 only after confirming that rejection, collecting the 684 freshly computed arrays of the 57 registered
  rows, recomputing the metrics from them (2633 checks) and comparing rho_max and m_max with the retained values; it does not
  compare the arrays with the retained archive. In Stage III the reproduction ran from 2026-10-29T12:00:01Z to 12:08:46Z (measured
  wall time 528 s including the initial integrity check; the unrounded recorded start and end stamps are 524.3 s apart), with driver exit 2, wrapper exit 0, all 2633 checks passed and
  rho_max = 1.793889555852889, m_max = 8.565619692094037 as retained [verifier]. Exit code 3 of the driver means the exchange
  record was rejected before any Euler evaluation, 2 that completed checks rejected the approximation, 0 that A1, A2 and A8
  passed (which is not full acceptance). The first version of the reproduction lock file omitted mpmath, which the
  validator imports unconditionally (the run above had it installed); with the corrected lock file the reproduction was run
  again in a fresh environment containing only NumPy 2.5.0, SciPy 1.18.0 and mpmath 1.3.0, on one core without GPU, and
  finished at 2026-10-29T13:22:44Z after 542 s of wrapper wall time with driver exit 2, all 2633 checks passed and the same
  rho_max and m_max [verifier].
- Resume an interrupted validation (validation project): the general registered evaluator in the accompanying artifacts resumes
  an interrupted validation when rerun with its resume option; its resume test interrupts a disposable
  validation of that evaluator after a real checkpoint, resumes it from a fresh process and compares it with an uninterrupted
  run (run 2026-10-29T01:00:05Z and again in Stage III, completed 12:00:09Z in 11.7 s: all seven checks passed, 72 arrays
  bitwise identical; this tests the general evaluator only) [verifier]. The native route used for R5 was tested in Stage III by
  interrupting it with SIGTERM after three committed rows, resuming it in a clean process and comparing it with a fresh
  uninterrupted run (2026-10-29T12:00:34Z to 12:19:53Z, 1158 s of wall time): all 19 checks passed, both runs returned the
  rejection code 2 with all 57 rows, the 684 arrays are bitwise identical, the committed prefix was unchanged, an attempt to
  overwrite the completed output returned 1 and changed nothing, and both give rho_max = 1.793889555852889 and
  m_max = 8.565619692094037 [verifier]. This confirms a reproducible rejection, not an accepted profile. In the accompanying artifacts the reproduction wrapper, the validator
source and the R5 export are included for inspection; the script first verifies the checksum manifest of the complete
validation bundle, so it does not run unchanged from the published subset.
- Test suites in the accompanying artifacts: the numerical operator suite (68 operator checks, all passed in Stage III, section 4.2) and the
  validation suite (environment as in its lock files); all 59 test scripts of the latter passed in a fresh copy of a
  compact validation bundle with only the bundled module paths (140 s of wall time, completed 2026-10-29T09:37Z) [verifier].
  Four of these scripts import PyTorch, which the first version of the broader lock file of the validation project omitted;
  the corrected lock file lists it, and the four unchanged scripts passed again (114 checks, 2026-10-29T13:38:52Z to 13:39:10Z,
  18.6 s of wall time, in the existing full environment rather than a fresh one) [verifier].

## 10. References

P. Constantin, M. Ignatova, V. Vicol, On putative self-similarity for incompressible 3D Euler, arXiv:2602.17570v3.
