# Axisymmetric obstruction audit

Version v39, 2026-10-29T14:29Z (revision history in the appendix at the end).

Results in brief. The exact-profile class is globally Cartesian C^2, full-space, axisymmetric and uniformly decaying. For
0 < c_l < 1/2 there is no nontrivial profile in this class (Proposition 1, after CIV Theorem 4.5), and for no c_l > 0 is there a
nontrivial one without swirl. The results reviewed here do not exclude 1/2 < c_l < 3/4 (section 4). At c_l = 1/2 the
obstruction needs an additional hypothesis on the stagnation set: it holds when the meridional zero set is countable, in
particular for real analytic profiles (Proposition 5). The structural results of sections 5 to 5g restrict particular
stagnation portraits under extra hypotheses stated with each result (smoothness in the reduced variables, reflection symmetry,
sign conditions on the vorticity); the matching results that need smoothness are identified as such. The prescribed-field
statements and the numerical records of 5e (vii) concern fixed meridional fields and saved numerical fields, not exact
profiles. Section 6 lists every result with its hypotheses.

The cited CIV statements were checked against version 3 of the paper. The extensions, structural results and numerical
observations below carry their own provenance and scope annotations: 'referee' marks a check by an independent referee (an
external model consulted through the campaign's question channel, its answer checked by the lead), 'verifier' a proof or
reproduction by the independent validation, 'lead' a derivation or check by the authors; exceptions and incomplete checks are stated individually. Each verifier-confirmed claim rests on a standalone proof or a
dated, frozen validation record of the independent validation, and each referee check on a referee answer, all among the
accompanying artifacts; where a claim names the record, a proof is named by its folder in the research records of the independent validation
(for example research/obstruction) and a referee answer by its number in the referee records (for example R01). The role annotations describe the check and do not replace those records. An annotation such as 'not verifier-checked' states the checks made by the date of the section or record it belongs to; later independent checks of several such items are recorded with their provenance in the final report (sections 3.11 to 3.13, 4.5 and 5), and those records state the final status. Corrections from those checks are incorporated and marked. Section 6 summarizes the results with
their hypotheses; sections 5 to 5g contain the derivations and, in 5e (vii) (l) to (n), a dated record of numerical tests.

Notation: c = c_l, alpha = (1 - c)/c, W = c y + U, W_m = (c r + U^r, c z + U^z), Gamma = r U^theta,
q = U^theta / r, eta = Omega^theta / r, s = r^2, U^r = -r phi_z, U^z = 2 phi + r phi_r, v = U^r/r = -phi_z,
eta = -Delta_5 phi with Delta_5 = d_r^2 + 3 r^(-1) d_r + d_z^2. 'Cartesian C^2' refers to the velocity field on R^3;
'smooth in (s, z)' refers to the reduced functions phi and q, a stronger condition. The source is P. Constantin, M. Ignatova and V. Vicol, "On putative
self-similarity for incompressible 3D Euler", arXiv:2602.17570v3 (CIV below); its gamma is our c_l. The CIV
statements below were read in the v3 PDF, not taken from the abstract.

## 1. Exact hypotheses of CIV Theorem 4.5

- Profile equations (3.3): (1 - gamma) U + gamma (y . grad) U + (U . grad) U + grad P = 0, div U = 0, identical to
  the prompt's equations with gamma = c_l.
- (3.5): U(0) = 0 and lim_{|y| -> infinity} |y|^{-1} |U(y)| = 0. CIV justify U(0) = 0 "due to Galilean symmetry
  (translation invariance)".
- (3.7) normalization ||D^2 U||_infinity = 1 is used to fix units in section 3; Theorem 4.5 does not use it.
- (3.8): there is C with |U(y)| <= C |y| <y>^{-1/gamma} and |Omega(y)| + |DU(y)| <= C <y>^{-1/gamma} for all y.
- Theorem 4.5: a nontrivial C^2 axisymmetric globally self-similar profile satisfying (3.5) and (3.8) has
  gamma >= 1/2.
- Theorem 4.3: if a meridional fixed point (gamma r + U_r = 0, gamma z + U_z = 0) has U_theta != 0 then gamma = 1/2.
  Such a point is necessarily off the axis (CIV footnote 9).
- Remark 4.6: the proof shows that no swirl-free profile with these hypotheses exists for any gamma > 0.

Proof structure (read in full): (i) the axis r = 0 is invariant for the meridional ODE and off-axis
trajectories never reach it; (ii) by (3.35), |r U_r + z U_z| <= (gamma/2)(r^2 + z^2) outside a disk, so every
backward meridional trajectory stays in a compact half disk (estimate (4.7)); (iii) e^{(1 - 2 gamma) tau} Gamma is
constant along trajectories, so gamma < 1/2 forces Gamma = 0; (iv) with zero swirl, e^{(1 + gamma) tau} eta is
constant along trajectories and eta is bounded on compacts (footnote 10, using Omega^theta in C^1 and zero on the
axis), so eta = 0; (v) U is irrotational and divergence free with DU -> 0, hence constant, hence zero by U(0) = 0.

## 2. Is the campaign's original target covered?

The target class: C^2 (Cartesian) axisymmetric profiles on R^3, uniformly decaying, with leading tail
U ~ R^{-alpha} F(vartheta), U(0) not prescribed.

- The velocity tail of the primary class gives the velocity part of (3.8) far out: |U| = O(R^{-alpha}) = O(|y| <y>^{-1/c}).
  The bound |Omega| + |DU| = O(R^{-1/c}) needs an assumption on the differentiated remainder and does not follow from the
  value asymptotic alone (outside a ball, U^theta = r R^(-alpha-1) (1 + R^(-1) sin R^3) has the leading term R^(-alpha) and
  derivatives of order R^(1-alpha); this smooth divergence-free field is not an Euler profile). Proposition 1 does not use it.
- (3.5) and (3.8) both force U(0) = 0, and the prompt says not to impose U(0) = 0. The profile equation is not
  translation invariant: V(y) = U(y + y0) + c y0, P_V(y) = P(y + y0) - (1 - c) c y0 . y is again a solution (a
  time-dependent translation of the blowup centre, i.e. an accelerating frame), but V tends to the constant
  c y0 at infinity. Choosing y0 at an axial zero of W (so that V is axisymmetric about the same axis) makes V(0) = 0 and V satisfies (3.5) but not (3.8) unless
  y0 = 0. So Theorem 4.5 as stated does not literally cover decaying profiles with U(0) != 0.
- The proof does cover them. Steps (i) to (iv) use only C^2 regularity and uniform sublinearity (U(0) = 0 is not
  used), and step (v) needs only that an irrotational, divergence-free, uniformly decaying field vanishes, which
  holds by the harmonic Liouville theorem. Hence:

**Proposition 1 (c_l < 1/2).** Let 0 < c < 1/2 and let U be a Cartesian C^2 axisymmetric solution on R^3 with a
C^1 pressure, U = o(|y|) uniformly. Then U is a constant axial vector K e_z (and U = K e_z, P = -(1 - c) K z is
an exact profile for every c, so this is sharp); if U -> 0 at infinity, U = 0.
The independent validation wrote an independent detailed proof of the same statement (its proof research/obstruction); the two agree step by step, and
the referee confirmed it. The final step uses only the harmonic gradient estimate
|grad U_i(x)| <= (C/L) sup_{B_L(x)} |U_i| -> 0, so no derivative decay at infinity is needed.

Minimal hypotheses (lead reading, confirmed): step (iii) needs only W_m locally Lipschitz (U in C^1) and Gamma
bounded on compacts; step (iv) needs eta bounded on compacts, which follows from Cartesian C^2 through
eta(r, z) = int_0^1 d_r Omega^theta(t r, z) dt, and is not supplied by C^1 alone; sublinearity is used only for
backward confinement and for the Liouville step. The same argument with Gamma = 0 from the start proves the swirl-free
statement for every c > 0 (section 1, Remark 4.6) under these weaker growth assumptions.

Euler1 Theorem L2 (the group's earlier report, read in its section 3) states the same conclusion for
0 < c_l < 1/2 without any symmetry assumption (C^2, uniformly sublinear), with a Bernoulli Lyapunov argument
whose strictness uses 1 - 2c > 0. It is not needed for the axisymmetric statement and is not used below.

## 3. What would have to fail below one half

An axisymmetric construction of a nontrivial uniformly decaying exact profile (or of a uniformly sublinear one with nonzero
swirl) with 0 < c_l < 1/2 must violate at least one of: (a) global Cartesian C^1 regularity of
U with continuous Gamma and locally bounded eta (C^2 suffices), including at the axis and the origin; (b) the
full-space domain (walls or boundaries, as in Luo and Hou's cylinder computations, change the trajectory
structure because backward orbits can come from the boundary); (c) uniform sublinearity of U; (d) exact,
isotropic, time-independent self-similarity on all of R^3 (anisotropic, local, asymptotic or only approximate
self-similarity, or profiles that depend on the self-similar time, are outside the theorem).

## 4. The regime 1/2 < c_l < 3/4 is not excluded

In step (iii) the weight e^{(1 - 2c) tau} grows as tau -> -infinity when c > 1/2; boundedness of Gamma on the
backward-trapping compact set is then consistent with any value of Gamma at the starting point. No other step
gives a restriction. Theorem 4.3 restricts only off-axis fixed points carrying swirl. Hence the proved results
do not exclude the target class. This is not evidence that profiles exist.

## 5. New structural facts used by the search (lead derivations, refereed)

**Lemma 2 (Dulac).** div_{r,z}(r W_m) = r div W = 3 c r, so the weighted area mu = r dr dz satisfies
mu(phi_t E) = e^{3 c t} mu(E) under the meridional flow. Hence no invariant Jordan curve bounds a region of the
closed half-plane: no periodic orbits and no polycycles, including those closed by an axis segment. At an off-axis
zero tr D W_m = 3c > 0; at an axis zero D W_m = diag(c + A, c - 2A), A = d_r U^r(0, z0), with 2 lambda_r + lambda_z = 3c,
so no zero is asymptotically stable. (Forward convergence to a saddle along its stable manifold is not excluded.)
Every backward orbit is confined to a compact set (Section 1, step (ii)), so its alpha-limit set is nonempty and
compact; by Poincare-Bendixson (with the field reflected across the axis), it contains a zero of W_m. If the zero
set S is finite, each alpha-limit set is a single zero. The zero set is compact. For c_l > 1/2 and an exact profile every
alpha-limit set consists of zeros of W_m (MATHEMATICAL_FORMULATION.md, section 6 (c); verifier argument).
[referee record R01: correct, with the weighted-area argument replacing a Green's-theorem argument on rough boundaries]

**Lemma 3 (axis zeros exist).** For a decaying axisymmetric profile, c z + U^z(0, z) is negative for z -> -infinity
and positive for z -> +infinity, so W_m has at least one zero on the axis.

**Lemma 4 (pointwise conditions at zeros).** At an off-axis zero, (1 - 2c) Gamma = 0, so q = 0 when c != 1/2; then
d_z(q^2) = 0 and the eta equation gives (1 + c) eta = 0, so eta = 0 and D W_m is symmetric: off-axis zeros are never
foci (the eta part is a referee addition). At an axis zero (0, z0), the q equation reduces to q (1 + 2A) = 0. Thus
a nonzero q at an axis zero forces A = -1/2, lambda_r = c - 1/2, lambda_z = c + 1 and d_z U^z = 1; for c > 1/2 this
is a hyperbolic meridional source, and the vorticity (0, 0, 2q) is an eigenvector of DU with eigenvalue 1, consistent
with the general identity (DU) Omega = Omega at zeros of W. [referee: correct]

**Proposition 5 (c_l = 1/2, conditional obstruction).** At c = 1/2, W_m . grad Gamma = 0. Each point y has an
alpha-limit set containing a zero p, and continuity gives Gamma(y) = Gamma(p). So Gamma(half-plane) = Gamma(S), a
compact interval containing 0 (Gamma = 0 on the axis). If Gamma is not identically zero, the interval is
nondegenerate and S is uncountable. Consequently a C^2 decaying axisymmetric profile at c_l = 1/2 whose meridional
zero set is countable (for example, all zeros nondegenerate, in which case S is finite) is trivial: Gamma = 0, then
eta = 0 by step (iv), then U = 0. A swirling profile at c_l = 1/2 needs a continuum of zeros along which Gamma
varies. Local structure (referee): near a zero p where Gamma takes a nonzero regular value, W_m = h J grad Gamma with
J a quarter turn and grad h . J grad Gamma = 3c at p, so {h = 0} is a regular curve of zeros transverse to the
Gamma level curves. Correction to v1: v1 stated that grad Gamma is transverse to the zero curve; that is false
(grad Gamma has a nonzero tangential component, and may be tangent). The referee's exact local example at c = 1/2,
U = (-r/2, kappa r, z), P = (1/8 + kappa^2/2) r^2 - z^2, has the stagnation line z = 0 and Gamma = kappa r^2; it grows
linearly and is not in the decaying class. The verifier proved the same countability criterion independently, and
separately that a smooth critical profile with nonzero q at an axis zero has a local curve of zeros.
Real analytic subclass (verifier proof 2026-10-28T19:46Z, lead review 2026-10-28T19:57Z: correct). For any c > 0, a real analytic,
axisymmetric, divergence-free, uniformly sublinear field has finitely many zeros of W_m in the closed half-plane. Proof
outline: with W_r = r a, W_z = b (a, b even analytic in r), incompressibility gives 2a + r a_r + b_z = 3c, so tr D W_m = 3c at
off-axis zeros and b_z = 3c at axis zeros with a = 0; by the analytic implicit-function and identity theorems each zero is
isolated, an interior point of a regular analytic arc of zeros, or the axis endpoint of a single half-arc; a compact
component of the arc part is a closed curve in r > 0 or an arc with both ends on the axis, and either bounds a region D
in r >= 0 with zero flux of r W_m, contradicting int_D 3c r dr dz > 0 (Lemma 2). Hence the zero set is finite, and at
c = 1/2 the countability criterion above gives Gamma = 0 and U = 0. A real analytic decaying profile at c_l = 1/2 is trivial.
This does not cover smooth non-analytic profiles, and analytic trial functions can still approximate a non-analytic
critical profile. The analyticity hypothesis of the finiteness statement cannot be replaced by smoothness, decay and
incompressibility alone (verifier proof 2026-10-29T06:00Z, lead check 2026-10-29T06:03Z: correct). With s = r^2, a
C-infinity cutoff rho(s) chi(z) equal to one on |s - 1| <= 1/4, |z| <= 1 and zero for |s - 1| >= 1/2 or |z| >= 2, the
potentials phi = rho chi z (5/4 - 3s/4), q = rho chi define through U^r = -r phi_z, U^theta = r q, U^z = 2 phi + 2 s phi_s a
C-infinity, compactly supported, divergence-free axisymmetric Cartesian field with U^theta = 1 at (r, z) = (1, 0). On the
plateau W_r = 3r(s - 1)/4 and W_z = 3z(1 - s) at c = 1/2, so W_m vanishes on the whole segment r = 1, |z| <= 1. It is not
an Euler profile: eta = 6z there and the eta residual on the segment is 9z (the q residual is zero there). Lead check by
hand and by sympy (author_checks/topic88_check.py and author_checks/topic88_cart.py, output author_checks/topic88_check_output.txt: divergence 0,
W_r, W_z, eta = 6z equal to Omega^theta / r, eta residual 9z at r = 1, q residual 3(s - 1)/2, Cartesian divergence 0).
The example bears only on the kinematic step; it is not a counterexample to any statement about Euler profiles.
Status of c_l = 1/2: open in general; excluded for countable stagnation sets and for real analytic profiles.

**Proposition 6 (c_l > 1/2, swirl-emitting sources).** Gamma is a Koopman eigenfunction: W_m . grad Gamma = (2c - 1) Gamma,
so Gamma grows like e^{(2c - 1) t} along forward orbits, and every swirl-carrying orbit emanates, in backward time,
from the zero set. With a = 2c - 1:
(S1) an axis zero with q != 0 requires A = -1/2 exactly (Lemma 4); it is a hyperbolic source.
(S2) a hyperbolic axis source with q = 0 there, for q smooth in (s, z) with a nonzero germ at the source: q has a nonzero finite Taylor jet (a flat germ is incompatible with
transport toward a hyperbolic source), its leading term is a multiple of s^j = r^{2j} with j >= 1 (a factor
(z - z0)^k with k >= 1 is impossible because lambda_z - (-1 - 2A) = c + 1 > 0), and
A = -(1 + 2jc)/(2(j + 1)), lambda_r = a/(2(j + 1)). (v1 allowed general k; corrected.) Smoothness is needed for the integer
quantization: at c = 2/3 the field U^r = A r, U^z = -2 A z, U^theta = r^(5/2), A = -4/7, with
P = -A (1 + A) r^2/2 + r^5/5 + A (1 - 2A) z^2, solves the profile equations exactly near a hyperbolic source with eigenvalues
2/21 and 38/21, is Cartesian C^2 (the swirl vector is (-y, x) r^(3/2)), and has q = r^(3/2) (j = 3/4) [referee, exact symbolic
check; lead check, author_checks/auditrev_check.py]; it does not decay and tests only the local classification.
(S3) an off-axis source: grad Gamma != 0 there requires spec D W_m = {a, c + 1}; grad Gamma = 0 with a nonzero Hessian
requires lambda_min = a/2; a vanishing 2-jet with a nonzero germ requires lambda_min < a/2 (C^2 class). Exact local
Euler profiles on annuli realize all three cases (referee construction), so these are the sharp local conditions.
Foci do not occur (Lemma 4); v1's focus exponent argument is withdrawn as unnecessary.
Degenerate (non-hyperbolic) sources are not classified by these arguments.
Verifier check (2026-10-28T18:59Z): the local S1, S2, S3 alternatives are confirmed by an independent proof with 19 exact
local tests; S2's finite-jet statement assumes smooth q (not merely Cartesian C^2 velocity); the global wording "every
backward orbit converges to one source" is not certified without hypotheses on the zero set and is not used here
(Lemma 2 gives convergence to a single zero only when the zero set is finite). The parity consequence at the origin
(Corollary 7) was confirmed by the verifier for smooth reflection-restricted fields.

**Corollary 7 (parity classes; lead derivation 2026-10-28T18:47Z, from Proposition 6) [verifier-confirmed for smooth fields].** The reflection
z -> -z with (U^r, U^theta, U^z)(r, -z) = (U^r, +-U^theta, -U^z)(r, z) maps profiles to profiles for either sign
(eta is odd and q^2 even in both cases). In a reflection-symmetric profile the origin is an axis zero of W_m.
(E) q even: the origin may be an S1 source (q(0) != 0, A = -1/2) or an S2 source.
(O) q odd: every Taylor monomial of q at the origin has odd k, so the leading term cannot be s^j; by (S2) a nonzero
smooth q vanishes on the basin of repulsion of the origin if the origin is a hyperbolic source (the lowest
homogeneous part of the jet must be a multiple of s^j, so the jet is flat, and a flat germ is excluded). Hence in
class (O) the swirl is emitted by zeros other than the origin, and the origin is either a source whose basin carries
no swirl, a non-hyperbolic zero, or a saddle: A < -c (radial inflow, axial outflow at rate c - 2A > 3c) or A > c/2
(axial inflow, radial outflow). Example of a swirl emitter compatible with (O): an
off-axis ring source on z = 0, where Gamma = 0 and d_z Gamma != 0 force d_z W_z = 2c - 1 and d_r W_r = c + 1 (S3).
(Correction 2026-10-28T19:53Z: v1 to v4 also listed a pair of axis sources at +-z0 with q(0, +-z0) = +-q0 (S1). Corollary 11 below
excludes this in the smooth stratum whenever every axis zero of W_z(0, .) is simple: in class (O) q then vanishes on the whole axis, so the
swirl must come from off-axis S3 rings, from S2-type axis sources with q = O(s), or from degenerate axis zeros.)
Parity-restricted computations are separate experiments; in them U(0) = 0 holds automatically by symmetry.

**Proposition 8 (reflection-monotone swirl; referee derivation 2026-10-28T19:37Z, lead-checked, generalized by the lead;
verifier-confirmed 2026-10-28T19:47Z in the Cartesian C^2 class, by an independent proof using phi(r, z) = int_0^1 t U^z(t r, z) dt,
the maximum principle in the upper half-space and the Hopf lemma, which avoids differentiating the Green integral).** Let c > 0 and let U be a nonzero Cartesian C^2 axisymmetric profile, decaying uniformly at infinity, with the reflection symmetry of Corollary 7 (either parity of q), and let
phi(r, z) = int_0^1 t U^z(t r, z) dt (then U^z = 2 phi + r phi_r, U^r = -r phi_z and eta = -Delta_5 phi, and phi decays uniformly
at five-dimensional infinity).
If d_z(q^2) <= 0 on {r >= 0, z > 0}, then phi_z(0, 0) < 0. Consequently the origin is neither an S1 source
(phi_z = 1/2) nor an S2 source (phi_z = (1 + 2jc)/(2(j + 1)) > 0), and in class (E) q(0, 0) = 0.
Proof. W_z(r, 0) = 0 by parity, so the plane z = 0 is invariant and, by uniqueness for the Lipschitz field W_m, a
backward orbit starting in z > 0 stays in z > 0; it is confined to a compact set (section 1, step (ii)). Along it,
d/dt [e^((1 + c) t) eta(Phi_t y)] = e^((1 + c) t) d_z(q^2)(Phi_t y), and eta is bounded on compacts, so
eta(y) = int_(-infinity)^0 e^((1 + c) t) d_z(q^2)(Phi_t y) dt <= 0 for z > 0. eta is odd in z, so z eta <= 0 everywhere.
Put phi(r, z) = int_0^1 t U^z(t r, z) dt; as a function on five-dimensional space (r the radius in four of the variables) it is
a decaying C^2 function, odd in z, so phi = 0 on z = 0, and Delta_5 phi = -eta >= 0 in z > 0. By the maximum principle
phi <= 0 in z > 0. If eta is not identically zero there, the strong maximum principle gives phi < 0 in z > 0 and the Hopf
lemma at the origin gives phi_z(0, 0) < 0. If eta = 0, then d_z(q^2) = 0 from the eta equation, so q = 0 by decay and U = 0
by step (v), against U != 0; hence the inequality is strict. (When the five-dimensional Green moment converges absolutely,
ORIGIN_AND_AXIS_REGULARITY.md section 6 (c), the same sign follows from phi_z(0, 0) = (3/4) int int z r^3 eta R^(-5) dz dr.) The S1 and S2 conditions are
Lemma 4 and Proposition 6. []
The referee stated this for the single-source reflection class; the proof uses neither the single-source hypothesis
nor c > 1/2. Interpretation: in a reflection-symmetric profile whose swirl magnitude does not increase away from the
symmetry plane, the origin is a point of axial compression, so the simplest "swirl blob centred on a stagnation
source" is impossible for every c_l. Any S1 profile in class (E) needs d_z(q^2) > 0 somewhere in z > 0, hence eta > 0
somewhere there, and eta < 0 somewhere on the upper axis (verifier's wording: the upper axis branch either reaches infinity,
where the pole relation applies, or ends at an axis zero where q = 0, and w eta = 2 q (q - q0) is negative near that end
in both cases): eta changes sign in the upper half-plane.

**Proposition 9 (no regular small-swirl limit; referee, lead-checked; verifier-confirmed 2026-10-28T19:47Z under the stated
convergences).** There is no sequence of smooth exact profiles with S1 sources at the origin such that c_n -> c_* > 0, phi_n -> phi_* in C^3 on compact sets in the regular meridional variables (with smooth axis extensions), q_n -> 0 in C^1_loc, and |U_n(y)| <= C (1 + |y|)^(-a) for a common a > 0 and C. This is a compactness obstruction. Proof: the limit satisfies (1 + c_*) eta_* + W_(*,m) . grad eta_* = 0 with confined backward
orbits, so eta_* = 0 and U_* = 0, while phi_(*,z)(0) = lim phi_(n,z)(0) = 1/2. [] S1 profiles therefore do not bifurcate
from swirl-free states with controlled limits; small q0 is not excluded by itself (q / q0 may grow, derivatives may
blow up, or spatial control may be lost). These considerations motivated O(1) values of q0 in the seeds; they do not exclude
weak-swirl continuation with loss of the stated controls.

**Proposition 10 (axis chain; axis matching computation by the referee, 2026-10-28T19:47Z record; general statement and proof
by the lead; confirmed by the verifier's standalone proof, 2026-10-28T20:11Z record, with the scope clarifications
marked below).** Let c > 0 and let U be a decaying axisymmetric profile with phi, q smooth in (s, z)
and phi(0, z) = O(|z|^(-alpha)), phi_z(0, z) = O(|z|^(-alpha - 1)). Write w(z) = W_z(0, z) = c z + 2 phi(0, z),
a(z) = 1 - 2 phi_z(0, z) = 1 + 2 v(0, z) and delta = 1 + c. The axis restrictions of the profile equations are

    w' = delta - a,     w q' + a q = 0,     w eta' + delta eta = 2 q q'.

Assume every zero of w is simple (true when every axis zero of W_m is hyperbolic). The zeros are isolated and lie in the
compact zero set (Lemma 2), so there are finitely many, z_1 < ... < z_(2n+1); since w ~ c z at both ends they alternate,
with w'(z_i) > 0 (repelling along the axis) for odd i and w'(z_i) < 0 (attracting) for even i.
(i) On each open axis interval between consecutive zeros, or beyond the outermost ones, q(0, .) is either identically
zero or nowhere zero (linear ODE with regular coefficient a/w).
(ii) Repelling zero, w'(z_i) = mu > 0. Near it q = C_(+-) |x|^(1 - delta/mu) h(x), x = z - z_i, h smooth and positive. The
exponent is below 1, so a C^1 q is either identically zero on both adjacent intervals, or mu = delta, a(z_i) = 0 and
q(0, z_i) != 0, with q of one sign on both adjacent intervals. (Verifier clarification: the other meridional eigenvalue
there is c - 1/2, so such a point is a full meridional S1 source only for c_l > 1/2; for c_l <= 1/2 the statement is axial only.)
(iii) Attracting zero, w'(z_i) = -mu < 0. Then q = C_(+-) |x|^k h(x) with k = 1 + delta/mu > 1 and h smooth and positive.
Smoothness of q requires C_+ = C_- = 0, or k an integer >= 2 with C_+ = (-1)^k C_-. In particular swirl on the axis on
one side of an attracting zero and none on the other is not smooth. If k is an integer, mu = delta/(k - 1) and
v(0, z_i) = (1 + k c)/(2(k - 1)).
(iv) Matching across an attracting zero between two S1 sources with amplitudes K_- and K_+ (referee). On the branch from
an S1 source with amplitude K, the first integral w eta = 2 q (q - K) holds up to the next zero (MATHEMATICAL_FORMULATION.md
section 6 (d)). With q = Q x^k + O(x^(k+1)), Q != 0, the right side divided by w is smooth and equals
(2 K Q/mu) x^(k-1) + O(x^k). Both one-sided formulas represent the same smooth eta, so K_- = K_+, and since q keeps the sign
of K on each branch, k is even.
Proof of (ii) and (iii): near a simple zero, -a/w = -a(z_i)/(w'(z_i) x) + (smooth), with a(z_i) = delta - w'(z_i), which
gives the stated exponents; at a repelling zero the exponent 1 - delta/mu is negative (q unbounded unless C_(+-) = 0), zero
(mu = delta) or in (0, 1) (q not C^1 unless C_(+-) = 0); at an attracting zero C_+ x^k and C_- |x|^k glue to a smooth
function only as stated. []

**Corollary 11 (axis swirl is one-signed or absent).** Under the hypotheses of Proposition 10, either q(0, .) is
identically zero, or every repelling axis zero has q = q0 != 0 and A = -1/2 with the same q0 at all of them (a full meridional S1 source when
c > 1/2), q(0, z) has the sign of q0
for all z and vanishes only at the attracting axis zeros, each of even order k_i = 1 + (1 + c)/mu_i, and the polar far-field
amplitudes B(+-1) of q are nonzero with the sign of q0. Proof: by (i) to (iii) the status "identically zero" or "nowhere
zero" propagates through every zero, so if q is not identically zero on the axis it is nonzero on every interval, every
repelling zero has q != 0 and A = -1/2 by (ii), and every attracting zero lies between two such zeros, so (iv) gives a common amplitude and
even orders. Beyond the outermost source, q' / q = -a/w = -1/(c z) + O(|z|^(-2 - alpha)), so q = C_(+-) |z|^(-1/c) (1 + o(1))
with C_(+-) != 0 of the sign of q0, and C_(+-) = B(+-1) for the differentiated tail. []
Consequences. (a) In reflection class (O) of Corollary 7, q(0, -z) = -q(0, z), so q vanishes on the whole axis: no S1 source
anywhere on the axis. (b) In class (E) with an S1 origin, any further axis zeros come in pairs +-z_j, all axis sources share
q0, and every attracting axis zero has its strain quantized by an even k. (c) Several S1 sources on the axis are not
independent: their amplitudes coincide. These are necessary conditions on the axis only; degenerate axis zeros (w' = 0)
are not covered. (d) (verifier) More generally, any profile whose axial swirl q(0, .) is odd in z has q = 0 on the axis under
these hypotheses. None of this excludes off-axis swirl when q vanishes on the axis.

Remark (referee, lead-checked; scope by the verifier). For c_l > 1/2, Gamma = 0 on every orbit that converges in forward
time to a zero of W_m, because Gamma(Phi_t y) = e^((2c - 1) t) Gamma(y) must stay bounded. (At c_l = 1/2 this holds for orbits
converging to an axis point, where Gamma = 0, but not in general for an off-axis zero.) Hence the stable manifold of an off-axis saddle carries no swirl,
and it cannot meet the basin of a nonzero S1 source, where q = K h never vanishes.

Remark on the S1 pressure jet (corrected 2026-10-28T19:14Z after the verifier's check, which the lead confirmed: at a zero of
W, U(y0) = -c y0 and grad P(y0) = -(1 - c) U(y0) = c (1 - c) y0). At an S1 point the momentum equation forces
P = P0 + c (1 - c) z0 (z - z0) + (1/8 + q0^2/2) r^2 - (z - z0)^2 + o(|y - y0|^2), a pressure saddle; the axial maximum
is at the source only when z0 = 0 (v2 omitted the linear term). The structure that the exact local relations
actually force is recorded in ORIGIN_AND_AXIS_REGULARITY.md section 5 (curvature relation, axis growth criterion and
the moment form of the S1 conditions): with q_z = 0 at the source, q has a saddle or degenerate critical point
there, and |q| can grow along the axis away from the source only where phi_z(0, z) > 1/2. This replaces the
heuristic "straddling" remark of v2.

These facts are necessary conditions only. They constrain initializations and are checked numerically for
every candidate (pre-registered specification, section 6.6). Attribution: CIV prove Theorems 4.3, 4.5 and Remark 4.6 under (3.5) and (3.8); the
weaker-growth extensions, Lemmas 2 to 4, Propositions 5 and 6 are deductions made here and are not CIV results.

## 5b. Zero-set portraits and the approach to c_l = 1/2 (added 2026-10-28T20:26Z)

Source: independent referee answers of 2026-10-28T20:21Z (axis chains and portraits) and 20:17Z (near-critical limit), with
exact-arithmetic checks retained in the accompanying artifacts; the lead re-derived the index relation, the separatrix
statement, Propositions 12 and 13 and the B resonance by hand, and re-checked the counterexamples and the ring-source
polynomial below with separately written code (author_checks/portrait_checks.py: all identities exact). Verifier check
(2026-10-28T20:31Z, standalone proof): the index relation, the separatrix exclusion and the resonance formulas are CONFIRMED
for hyperbolic zeros and for the stated nonzero finite jets (the resonances do not classify flat germs at saddles). The
verifier supplied the step that the separatrix statement needs at S2 sources: if the first nonzero source jet is K s^j, the
axis restrictions h_i = d_s^i q(0, .), i < j, solve w h_i' = (beta - 2 i lambda_r) h_i with exponent ratio 2 (j - i) lambda_r / lambda_z
in (0, 1), so a nonzero h_i behaves like |z - z0|^p with 0 < p < 1 and is not smooth; hence h_i = 0 near the source for all i < j,
q = s^j V with V(0, z0) = K by repeated smooth division, and q != 0 at nearby off-axis points. Propositions 12 and 13 have
a standalone verifier proof (research/near_critical_compactness, 2026-10-28T20:27Z).

Necessity of the hypotheses of Proposition 10 (axis level only). At c_l = 3/5 there are smooth axis data (w, q, eta) solving
the three axis equations with zeros of w at 0 and +-1 only, w'(+-1) = 8/5, q(0, +-1) = +-1 and w'(0) = 0 (q flat at the
degenerate zero 0): one degenerate attracting zero joins opposite S1 amplitudes. A second example has only simple zeros,
w'(0) = -8/5 (k = 2) and q(0, z) = sgn(z) Q(z) with Q smooth of order 2 at 0: an odd C^1 solution that is not C^2, with the
same smooth w and eta. So Proposition 10 fails for degenerate axis zeros and for finite regularity below C^k at an order-k
attractor. Neither example is extended to a full Euler profile.

Scope of Proposition 10 in the Cartesian C^2 class (verifier proof recorded 2026-10-28T23:11Z, fractional axis chains; lead cross-review
2026-10-28T23:27Z, author_checks/fracchain_check.py, output author_checks/fracchain_check_output.json, 3 s on one core). At an axis saddle of order
k = 1 + delta/mu with 2 < k < 3, q ~ Q_+- |z|^k on the two sides has vanishing value and first two derivatives at the saddle, and
eta ~ (2 K_+- Q_+-/mu) sgn(z) |z|^(k - 1) is C^1 with vanishing first derivative, for any two side amplitudes. The matching conditions
of Proposition 10 (q C^2 forces Q_+ = Q_-, eta C^1 forces K_+ Q_+ = K_- Q_-, hence K_+ = K_-) exist only for k = 2. The verifier
gives (1) global axis data for 3/5 <= c_l <= 37/50 with three simple zeros, decaying axial velocity and independent source
amplitudes (q may be odd), on the rational T3 axis drift of 5g (j), and (2) an exact local C^2 Euler field near a fractional
saddle with independent sidewise first-integral constants. Neither is a global Euler profile. Consequence: Proposition 10 and
Corollary 11 are theorems in the smooth stratum (k even integer at every axis attractor); in the fractional C^2 stratum the source
amplitudes of T3 are not forced equal by the axis, and the even-swirl reflection class is an assumption there, not a consequence.

Index relation (lead re-derivation of the index count in referee record R06). Assume that every meridional zero is hyperbolic (the zero set is then finite); the
separatrix and inventory statements below are for 1/2 < c_l < 3/4 with uniform sublinearity, and at S2 sources they use the
smooth nonzero-germ hypotheses. Label the zeros of W_m: axis source P (-c < v < c/2), axis saddle with axial
inflow A (v > c/2), axis saddle with radial inflow B (v < -c), off-axis source O, off-axis saddle D. There is no axis sink
(it would need v < -c and v > c/2) and no off-axis focus or sink (q = eta = 0 there, so D W_m is symmetric with trace 3c).
Reflecting r -> -r gives a smooth planar field with index 1 on large circles; with 2n + 1 axis zeros of which t are B,
(n + 1 - t) - (n + t) + 2 (N_O - N_D) = 1, so N_O - N_D = t.

Separatrices (c_l > 1/2). Gamma = 0 on every orbit converging forward to a zero (Remark after Corollary 11). In the basin of
an S1 source q = K h with h > 0, and in the basin of an S2 source q = s^j V with V != 0 near the source and nonvanishing
transported along orbits, so q != 0 off the axis in both. Hence the stable separatrix of an off-axis saddle never lies in an
S1 or S2 basin; it can lie in the basin of an S3 source, along its slow nodal curve. Portraits with an emitting axis source and
an off-axis saddle need a saddle connection or an S3 source to supply each stable branch.

Local resonances (referee, lead-checked for the cases used below). With a = 2c - 1: S2 of order j, v = -(1 + 2jc)/(2(j + 1)); smooth
S3 germ of nodal order m, slow eigenvalue a/m and fast eigenvalue 3c - a/m; B saddle with eigenvalues (-nu, 3c + 2 nu) receiving
Gamma ~ C s^(j+1) z^m, nu = (3cm - a)/(2(j + 1 - m)) with j >= m (from 2(j + 1)(-nu) + m(3c + 2 nu) = a); off-axis saddle with
eigenvalues (3c + mu, -mu) receiving Gamma ~ C u^m v^l, mu = (3cm - a)/(l - m), l > m. These are necessary conditions for a
smooth Gamma with the stated leading term; further conditions come from the eta hierarchy.

Admissible inventories with at most five zeros, all hyperbolic (referee, index count only; "admissible" means not excluded by
the conditions above, not constructed): P (single S1 or S2 source; odd swirl excluded by Corollary 11 for S1); B + O (equatorial
ring S3 source feeding the axis saddle; either parity); P + O + D and P + 2O + 2D (index-admissible; no smooth matching found,
because an emitting P cannot feed the stable branches of D); PAP (S1 pair with even k at A, or S2 pair); B + 2O + D; BAP + O;
PAP + O + D (needs the connection A -> D); BAB + 2O; PAPAP. Three smallest targets recommended for search: T1 a single S1
source with even swirl; T2 the ring portrait B + O with odd swirl and m = j = 1, where nu = (1 + c)/2, v(0, 0) = -(1 + 3c)/2 and
the ring eigenvalues are (1 + c, 2c - 1); T3 an even S1 pair at z = +-z1 with a central A of order k = 2, v(0, 0) = (1 + 2c)/2.
For T2 the polynomial q = K s z, phi = z [c + nu (1 - s)] + (4 nu/3) z^3 - (E/6) s^2 z^3 + (E/5) s z^5 - (4E/105) z^7 with
E = 2K^2/(3c) has eta = E s^2 z exactly, R_q = O(z^3) and R_eta = O(z^3), zeros at the origin (eigenvalues -(1 + c)/2 and 4c + 1)
and on the ring r = 1 (eigenvalues 1 + c along r and 2c - 1 along z): a local seed near the equator, not a solution. The
polynomial is unbounded and may have further zeros away from the equator; no global zero count is claimed for it (verifier).
Under dilation q_z scales as 1/L, so the dilation-invariant amplitude is (ring radius) x q_z at the ring; K = q_z(1, 0) is a
well-defined shape parameter only after the ring radius has been pinned to 1, which uses up the dilation gauge. A decaying
globalization with an exact zero count is in the accompanying artifacts (seeds/ring_t2.py, section 5c below).

**Proposition 12 (near-critical compactness; referee, lead-checked; verifier standalone proof).** Let U_n be smooth axisymmetric profiles for c_n -> 1/2+,
with ||U_n||_(C^2(R^3)) <= M, sup_n sup_(|y| >= R) |U_n(y)| -> 0 as R -> infinity, and an S1 point (0, z_n) for each n
(W_m = 0 and phi_z = 1/2 there; no lower bound on q(0, z_n) is assumed). Then a subsequence converges in C^1_loc to a decaying
C^(1,1) profile U_* at c_l = 1/2 that has nonzero swirl, and the meridional zero set of U_* is uncountable and carries a
nondegenerate interval of circulation values. In particular U_* is not real analytic.
Proof. |z_n| <= M/c_n, so z_n -> z_* along a subsequence; Arzela-Ascoli gives C^1_loc convergence and a C^(1,1) limit (uniform
C^2 bounds do not give C^2 convergence). The momentum vector (1 - c) U + W . grad U involves first derivatives only, so it
converges locally uniformly; its curl vanishes in distributions, so the limit is a gradient and U_* solves the profile equation
at c_l = 1/2; decay, divergence and axisymmetry pass to the limit, and d_z U_*^z(0, z_*) = 2 phi_z = 1, so U_* != 0. If U_* had
no swirl, its eta would be bounded near the axis and satisfy (3/2 + W_m . grad) eta = 0 along the C^1 flow; backward
confinement gives eta = 0, so U_* would be harmonic and decaying, hence zero. With swirl, Proposition 5 (whose argument needs
only a C^1 field) gives the uncountable zero set, and the verifier's analytic theorem excludes analyticity. []
Interpretation: along a sequence of smooth profiles with c_n -> 1/2+ and an S1 point, either the uniform global C^2 bound or the
uniform decay fails in every gauge that fixes an S1 strain (concentration, a diverging swirl amplitude, which violates the
C^1 bound, or escaping scales), or some subsequence converges in C^1_loc to a decaying C^(1,1), nonanalytic critical profile
with nonzero swirl and a continuum of stagnation points; neither a unique endpoint nor C^2 convergence is asserted. It is not an obstruction for any fixed c_l > 1/2.

**Proposition 13 (one-core obstruction near c_l = 1/2; referee, lead-checked; verifier standalone proof; conditional).** Let c = 1/2 + eps with an S1
source at z0, amplitude K, and suppose phi_z(0, z0) is given by the convergent five-dimensional Green moment
(ORIGIN_AND_AXIS_REGULARITY.md section 6 (c)). If the odd part eta_o(r, x) = (eta(r, z0 + x) - eta(r, z0 - x))/2 satisfies
|eta_o(r, x)| <= C K^2 |x| L^(-2) G(r/a) with int_0^infinity rho G(rho) d rho = I_G < infinity, then
1/2 = phi_z(0, z0) <= (C I_G/2) K^2 a^2/L^2, using int_R x^2 (r^2 + x^2)^(-5/2) dx = 2/(3 r^2). If moreover a/L equals the S1
saddle-curvature ratio (4 eps (1 + c)/((1 + c)^2 + K^2))^(1/2), then K^2 a^2/L^2 <= 4 eps (1 + c), and the inequality fails for
eps < 1/(4 C I_G (1 + c)), for every K. So no family of profiles with c_l -> 1/2 has a single core whose radial width is the
Hessian width with uniform shape constants C, G. The hypothesis does not follow from the curvature relation; a broad eta
component, a second axial layer or diverging shape constants evade it. The referee also identified a formal distinguished
balance (radial width delta -> 0 with K delta fixed) that escapes the obstruction; its solvability is open.

## 5c. A decaying T2 seed family with an exact zero count (added 2026-10-28T20:38Z, lead)

The polynomial of section 5b is local. For search initializations the lead built a decaying family
(seeds/ring_t2.py, self-test output seeds/ring_t2_selftest.txt, derivative check author_checks/ring_t2_fdcheck_output.txt):

    phi = z F(rho), rho = s + z^2,  F(rho) = F_inf (1 + (rho/b)^3)^(-1/(6c)) + (c + nu - F_inf)/(1 + (rho/rho_1)^n),  nu = (1 + c)/2,
    q = K s z ((1 + rho)/2)^(-(3 + 1/c)/2),  eta = -z (4 rho F'' + 14 F'),

with (F_inf, rho_1) solved from F(1) = c and F'(1) = -nu, and shape parameters b > 0, n >= 3. Exact facts for this class,
for any F: W_m = (r (c - F - 2 z^2 F'), z (c + 2F + 2 s F')). If F = c holds only at rho = 1 and both c + 2F and c + 2(rho F)'
are positive for all rho >= 0, then W_z/z is positive (it is linear in s on [0, rho] with positive end values), every zero lies
on z = 0, where W_r = r (c - F(s)), and the zeros in the closed half-plane are exactly the origin and the ring (1, 0). Since
F(0) = c + nu and F'(0) = F''(0) = 0, the origin is a B saddle with v = -(1 + 3c)/2, rate -nu radially and 1 + 4c axially, and
eta = O(R^5) there. An exact profile needs more at the origin: eta = (2 C^2/(3c)) s^2 z + ... with no s z^3 or z^5 term (the
monomial s^a z^b has divisor (1 + c)(1 - a) + b(1 + 4c), nonzero for a <= 1), which no field of the form z F(rho) reproduces,
so the seed has a local eta defect of weighted order 5 at the origin. The ring has eigenvalues 1 + c (radial) and 2c - 1
(axial), the m = 1 resonance, and Gamma = K z + O(|x - x_ring|^2) there, along the slow direction. The tails are
phi ~ R^(-1/c) z = O(R^(-alpha)) and q ~ R^(-1/c) (s z/R^3) = O(R^(-alpha-1)), the decay of the target class. The ring balance
eta_z(1, 0) = 2K^2/(3c) is a soft design target, not imposed.

The self-test (run 2026-10-28T20:37Z, 40 s on one core; 24 cases: c_l in {0.56, 0.60, 0.64, 0.68, 0.72, 0.74}, K in
{0.5, 1, 2, 4}) checks the sufficient conditions on 12001 values of rho in [0, 1e10] and independently locates zeros of W_m by
Newton refinement of all grid minima of |W_m|/R on a polar grid (R in [1e-3, 1e3], 1500 x 721): every case passes, and the only
zero found besides the origin is the ring (1, 0). The margin min (c + 2(rho F)')/c is small at c_l = 0.56 and 0.60 with K <= 1
(0.013 and 0.024): those seeds are close to developing extra zeros. The seed residuals are O(1): RMS R_q about half the RMS of
q and RMS R_eta 4.5 to 12 times the RMS of eta on a uniform grid of 0 < s < 9, |z| < 3. The family fixes the topology, the local resonances
and the decay rates, and nothing else; it is an initialization, not an approximation.

Verifier check (2026-10-28T20:45Z record, noted here 2026-10-28T20:58Z): the grid scan was replaced by a proof. For all 24 exported parameter
sets, with the stored decimals read as exact rationals, a finite exact-rational certificate (1 to 11 cells per case, reloaded by
an independent checker, 62 checker tests) proves c + 2(rho F)' > 0 on [0, infinity) (integrating gives rho F > -c rho/2, hence also c + 2F > 0), using monotonicity of the tail term and
integer inequalities for the fractional powers. Scope: the matching equalities F(1) = c and F'(1) = -nu hold only to the
precision of the stored decimals, so the unique nonzero zero is certified to lie in 1 - 1e-8 <= rho <= 1 + 1e-8 on z = 0, not
exactly at rho = 1; the exact resonant ring eigenvalues follow only when both equalities hold exactly. The same proof shows that
no member of the family with positive amplitudes is an exact profile (the nonzero s z^3 and z^5 eta coefficients contradict the
origin transport equation), in agreement with the local defect stated above. Search seeds outside the family are not restricted.

## 5d. T3: an equatorial swirl zero and a decaying seed family (added 2026-10-28T20:44Z, lead; referee-checked, not verifier-checked)

**Lemma 14 (lead).** Let U be a smooth axisymmetric profile in reflection class (E) (phi odd in z, q even) with c_l > 1/2, and
suppose the origin is a hyperbolic axis zero with v(0, 0) > -1/2 and W_r(r, 0) > 0 for all r > 0. Then q(r, 0) = 0 for every r.
Proof. W_z is odd in z, so the equator is invariant and every equatorial orbit leaves the origin, with
r(t) <= C e^(lambda t) as t -> -infinity for any lambda < lambda_r = c + v(0, 0). Along it Gamma(Phi_t y) = e^((2c - 1) t) Gamma(y),
and |Gamma| <= C' r^2 because q is bounded. Choosing lambda with 2 lambda > 2c - 1 (possible since 2 lambda_r = 2c + 2v(0, 0) >
2c - 1) and letting t -> -infinity gives Gamma(y) = 0. []
For an S1 source at the origin (v = -1/2) the inequality is an equality and the lemma does not apply, as it must not (Gamma =
q0 r^2 + ...). It applies to the central axial-inflow saddle of T3 (v(0, 0) = (1 + 2c)/2). In a T3 profile whose only zeros are the two S1
sources and the saddle, every point off the equator lies in the basin of one source, where q = K h with h > 0 (section 5b), and
Proposition 10 gives a common amplitude K, so q has the sign of K everywhere except on the equator, where it vanishes. Near the
saddle the q monomials s^a z^b have divisor (1 + c)(2 - b) + a(1 + 4c); the leading resonant one is z^2 (order k = 2,
q = Q z^2 + ..., Q != 0 with the sign of K), and the others need (b - 2)(1 + c) = a(1 + 4c). With q even in z (b even), the first
one inside (1/2, 3/4) has weight 2a + b = 36 (s^8 z^20 at c_l = 5/7; then s^9 z^22 at c_l = 11/16, s^10 z^24 at c_l = 2/3, s^11 z^26
at c_l = 13/20, and infinitely many further rational resonances, verifier audit of 2026-10-28T21:21Z; v9 omitted 11/16, referee
correction of 2026-10-28T21:03Z); without parity s^4 z^11 at
c_l = 5/7 already has weight 19. The order of vanishing persists along the whole equator: with g(r) = d_zz Gamma(r, 0)/2, the
z^2 coefficient of W_m . grad Gamma = (2c - 1) Gamma gives W_r(r, 0) g' = (2c - 1 - 2 d_z W_z(r, 0)) g, a linear equation with
W_r > 0 and g ~ Q r^2 at r = 0, so g never vanishes and q vanishes exactly to second order on the equator. For eta the divisor
is (1 + c)(1 - b) + a(1 + 4c), so the coefficient e of eta = e z + ... is not fixed by the local eta equation; the axis relation
w eta = 2 q (q - K) with w = -(1 + c) z + ... ties it to the swirl, e = 2 K Q/(1 + c).

Seed family (seeds/pair_t3.py, self-test seeds/pair_t3_selftest.txt). phi = z F(rho) with
F(rho) = F_inf (1 + (rho/b)^3)^(-1/(6c)) + (F_0 - F_inf)(1 + (rho/rho_1)^n)^(-p), F_0 = -(1 + 2c)/2, and (F_inf, rho_1) solved from
F(1) = -c/2 and F(1) + 2F'(1) = 1/2. Then W_r/r = c - F - 2 z^2 F' is linear in z^2 on [0, rho]; if c - F > 0 and c - F - 2 rho F' > 0
for all rho, W_r > 0 off the axis and all zeros are on the axis, where W_z = z (c + 2F(z^2)); if c + 2F vanishes only at rho = 1,
the zeros are exactly the origin (w'(0) = -(1 + c), v = (1 + 2c)/2, order 2) and (0, +-1) (v = -1/2, S1). The axis swirl solves the
exact axis equation w q' = -(1 - 2 phi_z(0, z)) q with q(0, +-1) = K (so q(0, z) ~ Q z^2 at 0 and ~ z^(-1/c) at infinity), and off
the axis q = K z^2 Q2(rho) with Q2(t) = q(0, t^(1/2))/(K t), which vanishes on the equator as Lemma 14 requires. The design scan
and self-test (2026-10-28T20:43Z, 17 s together on one core) found admissible shapes at all six c_l in {0.56, 0.60, 0.64,
0.68, 0.72, 0.74}, with margins min (c - F - 2 rho F')/c from 0.11 to 0.32; the self-test (18 cases, K in {0.5, 1, 2}) passes: sufficient conditions on 12001 values of rho, no off-axis zero in a
Newton-refined polar grid search, q(0, 1) = K, q(0, 0.02)/q(0, 0.01) between 3.996 and 4.000, axis swirl equation residual at most 1.1e-5 relative
(finite differences). Not imposed: the axis relation w eta = 2 q (q - K), the S1 curvature relation and the off-axis equations. Initialization only.

Referee check and further T3 restrictions (added 2026-10-28T21:07Z; referee record of 2026-10-28T21:03Z with 49 exact checks; lead checks in
author_checks/t3_check.py, output author_checks/t3_check_output.json, 1.3 s on one core). Notation: delta = 1 + c, gamma = 1 + 4c, epsilon = c - 1/2,
K > 0 the common source amplitude, Q = q_zz(0, 0)/2.
(a) Lemma 14 and the quadratic zero are confirmed. The axis equation at the saddle (w = -delta z + O(z^3)) gives q(0, z) = Q z^2 + O(z^4)
with Q > 0 on the branch arriving from the source, and w eta = 2 q (q - K) holds on both 0 < z < 1 and z > 1, so e = 2 K Q/delta > 0.
(b) Equator (exact; lead-checked). With f = phi_z(s, 0), A = q_zz(s, 0)/2 and E = eta_z(s, 0):
2s(c - f) A' + (1 + 2c + 2f + 4s f') A = 0 and 2s(c - f) E' + (1 + 2c + 2f + 2s f') E = 0, hence E(s) = (K gamma/delta) A(s)/(c - f(s)) and both
are positive for all s: q vanishes exactly quadratically on the whole equator and eta > 0 just above every equatorial point.
Under the differentiated tail, B(mu) = b_2 mu^2 + o(mu^2) at the equator with b_2 > 0, the eta tail has positive slope there, and
c E(1) = -2 K B(1) < 0 at the pole, so the eta tail changes sign in z > 0.
(c) Moments (exact, 5D Green representation and parity; integrals over r, z > 0): with A_0 = z R^(-5), P_1 = rho_-^(-3) - rho_+^(-3),
S_1 = (z - 1) rho_-^(-5) + (z + 1) rho_+^(-5), rho_-+^2 = r^2 + (z -+ 1)^2: int r^3 A_0 eta = -(1 + 2c)/3 (central strain),
int r^3 S_1 eta = 2/3 (source strain), int r^3 P_1 eta = -2c (source position). Splitting eta and S_1 into signed parts gives
J_- - J_+ = (1 + 2c)/3 with J_+ > 0, and favorable minus unfavorable source-strain contributions F - N = 2/3 with N > 0. Hence T3 is
impossible if eta is one-signed in z > 0; any estimate F <= 2/3 would exclude it. The positive eta near the saddle end of the inner
axis and the negative eta far out on the outer axis both count against the source strain. Only these neighbourhoods are proved
unfavourable: an axial overshoot q > K on part of an axis branch can make S_1 eta positive near the source (verifier audit of
2026-10-28T21:21Z); with q <= K on both whole axis branches the axis neighbourhoods are unfavourable throughout.
Correction (2026-10-28T21:47Z; found by the referee record of 2026-10-28T21:43Z, lead-checked in author_checks/c2saddle_check.py). Versions v13 and
earlier printed S_1 with a minus sign between the two terms. Differentiating the odd Green kernel [r^2 + (z - Z)^2]^(-3/2) -
[r^2 + (z + Z)^2]^(-3/2) in Z at Z = 1 gives 3 S_1 with the plus sign above, and the moment value 2/3 belongs to that kernel. Its
sign regions: S_1 > 0 for z >= 1; for 0 < z < 1 it is negative near the axis and positive at large radius; S_1 = 0 on the equator.
The earlier claim that S_1 < 0 throughout 0 < z <= 1 is withdrawn, and so is the separate "S_1 eta <= 0" row of section 6 (with the
correct kernel that condition only restates the moment and defines no useful class). The one-signed eta obstruction and the axis
sign rules do not use S_1 and stand.
(d) Sources (exact jets; lead-checked). At z0 = 1 with phi(0, 1 + x) = -c/2 + x/2 + h_2 x^2 + h_3 x^3 + ..., q_z = 4 K h_2/delta and the
general curvature identity is 4 epsilon delta q_rr + (delta^2 + K^2) q_zz = 3 (delta^2 + 2K^2) q_z^2/(2K). So h_2 != 0 makes the source
a regular point of q (max q > K); h_2 = 0, h_3 != 0 makes it a saddle; a source maximum needs h_2 = h_3 = h_4 = 0, and then the quartic
threshold of 5e (iii) applies. (The quartic discriminant has the factor K^2 + 4 delta^2, as in author_checks/t1_quartic_check_output.json.)
(e) Inner axis segment (exact). w(z) = -delta q(z) int_z^1 du/q(u) on 0 < z < 1, and oddness of w gives the finite part
int_0^1 (Q/q(z) - 1/z^2) dz = 1, so q >= Q z^2 on the whole segment is impossible; log(Q/K) = -int_0^1 ((w' - delta)/w - 2/z) dz.
(f) Seed defect. For phi = z F(s + z^2) and q = z^2 G(s + z^2) the saddle jets force F'(0) = 0 and hence e = 0, contradicting e > 0: no
exact T3 profile has this combined form. The pair_t3 defaults have e = 0 (n >= 2) or e < 0 (n = 1; about -40.9 at c_l = 0.60 and
-72.9 at 0.68), the wrong sign. The seeds remain usable as topological initializations only.
(g) No obstruction. An explicit smooth axisymmetric model (not an Euler profile) satisfies the axis equations on both segments, the
finite parts, 0 <= q <= K with monotone axial swirl, elliptic closure, all three moments and the source jets; its first defect is the
s z^2 coefficient of R_q at the saddle. Any obstruction to T3 must use the off-axis transport and elliptic coupling.

## 5e. Restrictions on the single-source portrait T1 (added 2026-10-28T20:49Z; referee record of 2026-10-28T20:41Z, lead checks noted)

Setting: reflection class (E), the only zero of W_m is an S1 source at the origin with q0 = K > 0 (so q > 0 everywhere, section
5b), eps = c - 1/2, delta = c + 1, k = 1/c. The referee did not prove that T1 is empty. The following are proved for stated
subclasses, or are necessary conditions.

(i) Source budget. With J_+- = int_0^inf int_0^inf z r^3 eta_+-(r, z) (r^2 + z^2)^(-5/2) dz dr (positive and negative parts), the
moment form of phi_z(0, 0) = 1/2 (ORIGIN_AND_AXIS_REGULARITY.md section 6 (c)) and reflection give J_+ - J_- = 1/3. On the upper
axis w eta = 2 q (q - K) with w > 0 and q -> 0, so eta(0, z) < 0 for large z and J_- > 0, J_+ > 1/3. Hence a one-signed eta in the
upper half-plane excludes T1 (lead check: direct from the moment identity and the axis relation).

(ii) Source maximum of q. If the first nonconstant terms of q have degree 2m, q = K + sum_j a_j s^j z^(2m - 2j), with the phi
deviation sum_j p_j s^j z^(2m + 1 - 2j), the leading equations give a_j = K n_j p_j/d_j and p_(j+1) = -n_j (n_j - 1)(1 + K^2/d_j^2)
p_j/(4 (j + 1)(j + 2)), n_j = 2m + 1 - 2j, d_j = eps j + delta (m - j) > 0. The p_j alternate in sign, so a_m/a_0 has the sign of
(-1)^m: for m odd the axial and equatorial curvatures of q have opposite signs. A nonflat source maximum of q can therefore
first vary only in degree divisible by four. (Lead check: recursion and sign rule verified symbolically for m = 1, 2, 3 with
symbolic c and K, author_checks/t1_jet_recursion_check.py; m = 1 is the curvature relation of ORIGIN_AND_AXIS_REGULARITY.md 6 (a).)

(iii) Quartic threshold. If the Hessian of q vanishes at the source and the first variation is quartic (m = 2, axis coefficient
h_5 of phi), then q <= K forces h_5 < 0, A_4, C_4 < 0, B_4 > 0, and nonpositivity of the quartic is B_4^2 <= 4 A_4 C_4, which is
equivalent to

    (13 - 14c) K^2 >= (c + 1)(56 c^2 + 28 c - 37).

The right side is positive for c_l > c_* = (9 sqrt 7 - 7)/28 = 0.60042. So for c_l > c_* a T1 profile with a quartic-type
source maximum needs K >= K_crit(c_l): 1.726 at c_l = 2/3, 2.309 at 0.70, 3.079 at 0.74, tending to sqrt(217/20) = 3.294 as
c_l -> 3/4. (Lead check: coefficients and the factorization B_4^2 - 4 A_4 C_4 = -25 K^2 h_5^2 (K^2 + 4 delta^2)[(13 - 14c) K^2 -
(c + 1)(56 c^2 + 28 c - 37)] / (16 delta^4 (2c - 1)(4c + 1)^2) verified symbolically, author_checks/t1_quartic_check.py; v13 printed the factor as K^2 + delta^2, a transcription error caught by the verifier.) This is not a
lower bound on K for general T1 profiles: it applies to the stated subclass, and equality only makes the quartic semidefinite.
Orbit-monotone T1 profiles (q nonincreasing along every forward orbit, hence q <= K) must have all nonconstant Taylor terms of q
through degree six equal to zero (degrees 2 and 6 by (ii); degree 4 because the quartic of phi_z - 1/2 takes both signs when
h_5 != 0, referee computation).

(iv) The axis equations do not force axial amplification (referee construction, lead-checked). Take f smooth, nonincreasing,
f = 1 on [0, 1], f(u) = u^(-k/2) for u >= 4; phi_0(z) = (z/2) f(z^2), w = z (c + f(z^2)), Q from w Q' = (2 phi_0' - 1) Q with
Q(0) = K, E_0 = 2 Q (Q - K)/w. These satisfy all three axis equations, the pole relation and the axis-reconstruction finite-part
condition, with 0 < Q <= K, Q' <= 0 and E_0 <= 0 on z > 0. The explicit field Phi(s, z) = (z/2) f(s + z^2) + s z b(s + z^2), with b
chosen so that -Delta_5 Phi = E_0 on the axis, decays like R^(-alpha), and the source moment holds because it is an identity for
any decaying Phi with Phi_z(0, 0) = 1/2. Its positive eta lies off the axis. This field is not a T1 profile (the off-axis eta
equation fails), but it shows that an obstruction to T1 must use the equations away from the axis: the axis data, the pole
relation, elliptic closure and the source moment are compatible with q nonincreasing along the axis.

(v) Conditional size bounds. With m_0(r) = sup_(z > 0) eta_+(r, z) and m_1(r) = sup_(z > 0) eta_+/z, int_0^inf m_0 dr >= 1 + 3 J_- and
int_0^inf r m_1 dr >= 1 + 3 J_-; for example, if eta_+ is supported in r <= a, then ||eta_+||_inf a >= 1 + 3 J_-. If eta_+ obeys an
envelope C Q_*^2 (z/L^2) G(r/a) with a/L at most D times the Hessian width (ORIGIN_AND_AXIS_REGULARITY.md 6 (d)), then
1 + 3 J_- <= 4 A eps delta Q_*^2/(delta^2 + K^2) (A = C D^2 int rho G). With Q_* = K (envelope amplitude equal to the source amplitude)
the subclass is empty when 4 A eps delta <= 1 and otherwise needs K^2 > delta^2/(4 A eps delta - 1) (the Q_* = K qualification is the
verifier's, audit of 2026-10-28T21:21Z). This strengthens
Proposition 13 but keeps its type of hypothesis (referee; not lead-checked beyond the two kernel integrals).

(vi) Energy overshoot (from MATHEMATICAL_FORMULATION.md section 6 (f)). For 1/2 < c_l < 3/5, int (|U|^2 - R^(-2 alpha) |F|^2) = 0
(under the differentiated tail expansion), and for F not identically zero the integrand is negative for small R on an angular open set where |F| is bounded
below (U is bounded there), so |U|^2 <= R^(-2 alpha) |F(y/R)|^2 everywhere is impossible: every nonzero profile in this range exceeds the homogeneous
extrapolation of its tail somewhere (if F = 0 the identity gives U = 0).

(vii) Induced strain of prescribed meridional fields (referee record of 2026-10-28T22:03Z with a proof file and floating-point
numerics; lead checks in author_checks/t1budget_check.py, output author_checks/t1budget_check_output.json, 8.6 s on one core; verifier, by
independent proofs and an independent characteristic integrator, 2026-10-28T22:25Z to 22:46Z: (a), the negative family of (b), (c)
and (d) confirmed, S at c_l = 0.74, a = 1 reproduced to 5.8e-9 (0.0810557); the mechanism wording of (f) corrected). For a meridional
field phi with the T1 portrait let h[phi] and e[phi] be the characteristic swirl and vorticity of unit source amplitude
(q = K h, eta = K^2 e, given by the characteristic transport formulas displayed in (m)) and S[phi] = (3/4) int int z r^3 e R^(-5) dz dr the induced source strain. A T1 profile is a
fixed point phi = K^2 Delta_5^(-1)(-e[phi]) with K^2 S[phi] = 1/2, so it needs S > 0 at the fixed point.
 (a) Sign under monotone swirl (proved for smooth phi odd in z with phi_z(0) = 1/2 whose backward characteristics all tend to the source, the transport
normalized by continuity with h(0) = 1, bounded e, h decaying uniformly and an absolutely convergent strain integral). If d_z(h^2) <= 0 on z > 0 then S < 0. Without decay the statement
fails: phi = z/2, h = 1, e = 0 has the single-source portrait for c > 1/2 and S = 0. This is the mechanism of Proposition 8 applied to
a prescribed field. The referee could not settle the sign under phi_z <= 1/2 everywhere, under an axis strain cap, or under a
source maximum of h alone (phi_z <= 1/2 along orbits gives h <= 1 but not the spatial monotonicity used in (a)).
 (b) An explicit negative subclass (proved; lead check: R_q = 0 to 6e-17 at n = 4, 5, 7). For n >= 4 put c_l = 1/2 + 3/(4n),
u = r^2 + z^2, v(u) the positive root of v^3 + u^n v^(2n + 3) = 1, h = v^2, phi = z v^3/2. Then h solves the swirl equation exactly,
W_R/R >= c_l - 1/2 > 0 (a single source), h <= 1, phi_z <= 1/2 and S < 0.
 (c) No sign theorem for prescribed fields (proved, asymptotic). With p = 1/(2c_l), beta = (1 - p)/2 > 0, d = p + beta < 1,
phi_{B,L} = (z/2)(1 + s/L^2 + B z^2)^beta/(1 + s/L^2 + z^2)^d has the T1 portrait and decays like R^(-alpha), and S[phi_{B,L}] > 0
for B large and then L large (no certified finite thresholds). The mechanism is axial amplification, phi_z(0, z) > 1/2 near the
source: on the axis the exact identities w e = 2h(h - 1), g = h/w, g' = -delta g/w and e = 2 w g^2 - 2g (w = W_z(0, z)) give a
positive axis integral of e for large B, and radial stretching (L large) makes the Green weight see only the axis. (Lead check:
the axis identities symbolically, and the inequality F + s F_s >= (1 - d) F for phi = z F that excludes other zeros.)
 (d) Local closure at the source (exact; lead-checked). If phi = z/2 + p_s s z + p_z z^3 + ..., transport and elliptic closure
give eta = (6 K^2 p_z/delta^2) z + ... and p_s = -(3 p_z/4)(1 + K^2/delta^2); this is the jet recursion (ii) with m = 1, j = 0. For
phi_{B,L} it requires L^2 (beta B - d) = 4p/(3(1 + K^2/delta^2)) < 4p/3, so the positive-strain regime of (c) is incompatible with
closure: (c) is a counterexample to a sign theorem for prescribed fields, not an approximate family of profiles.
 (e) Numerical record (referee; eighth-order characteristic integration with variational equations, Gegenbauer reconstruction of
Delta_5^(-1); two transport grids, selected strains stable to 1.3e-4 relative; floating point, not interval). The seeds
phi_{c,a} = z(1 + 3z^2)/(2(1 + a s + z^2)^(1 + 1/(2c))) have a proved T1 portrait for every a > 0. The best tested aspects
(a in {0.25, 1, 2, 4, 8, 16, 32}) give, with K^2 = 1/(2S) and the relative closure defect ||phi - K^2 Delta_5^(-1)(-e)||/||phi||
in an annular norm (R in [0.05, 8], weight R^4 (1 - mu^2), mu = z/R; not a whole-space or pointwise bound):

| c_l | a | S | K | defect |
|---|---|---|---|---|
| 0.55 | 32 | 4.22e-4 | 34.4 | 0.923 |
| 0.60 | 8 | 4.29e-3 | 10.8 | 0.819 |
| 0.68 | 2 | 3.25e-2 | 3.92 | 0.687 |
| 0.74 | 1 | 8.11e-2 | 2.48 | 0.607 |

The input axial cubic coefficients p_z are positive; the reconstructed ones are negative (about -1.2, -0.82, -0.46, -0.32; the
first is cutoff-sensitive). The c_l = 0.60 seed fails (d): the strain normalization needs K^2 = 116.6, its cubic coefficients
need K^2 = 40.4.
 (f) Iteration (numerical). Three damped (1/4) projected Picard steps at c_l = 0.60, a = 8, with the dilation fixed by
p_s = -22/3: S = 4.29e-3, 2.78e-3, 1.44e-3, -8.5e-4 (defect 0.819, 0.759, 0.802, then no real normalization); the first-step
defect and the third-step sign survive an independent refinement. Mechanism: the reconstructed axial cubic coefficient (b = -1.63
before step 3) is negative, so the damped update drives p_z through 0.583, 0.360, 0.142, -0.300; with p_z < 0 the near-source
axial forcing turns negative. The measured sign change of S coincides with this, but p_z < 0 controls only the near-source
forcing and does not give the spatial monotonicity hypothesis of (a), so it is a measured coincidence, not a proved mechanism
(verifier audit of 2026-10-28T22:27Z). Smaller damping may only delay it. It is the failure of one projected iteration, not a theorem.
 (g) The seed family cannot close (exact; verifier proof of 2026-10-28T22:42Z with ten symbolic checks; lead cross-review 2026-10-28T22:58Z,
author_checks/t1seed_obstruction_check.py, output author_checks/t1seed_obstruction_check_output.json, 5 s on one core). For phi_{c,a} of (e), with
p = 1/(2c): p_s = -a(p + 1)/2 and p_z = (2 - p)/2 > 0, so (d) with K^2 > 0 needs a > 3(2 - p)/(4(p + 1)). On the upper axis
w = W_z(0, z) does not depend on a, h ~ H z^(-2p) with H > 0, and w e = 2h(h - 1) forces eta(0, z) = -(2 K^2 H/c) z^(-1 - 2p)(1 + o(1)) < 0,
while the seed has (-Delta_5 phi)(0, z) = (3/2)[8a(p + 1) - 2p(2p - 1)] z^(-1 - 2p) + O(z^(-3 - 2p)), which needs a < p(2p - 1)/(4(p + 1)).
Since 3(2 - p) - p(2p - 1) = 6 - 2p - 2p^2 > 0 for 2/3 < p < 1, the two bounds are disjoint: no member of the family (any a, any K,
any dilation) is an exact profile. This excludes one rational family only, not its deformations or T1. Pole test for any
prescribed T1 field (same argument): the leading upper-axis tail coefficient of -Delta_5 phi must be negative, in addition to (d).
 (h) The two-parameter family cannot close either (exact; verifier proof of 2026-10-28T23:16Z with sixteen symbolic checks; lead
cross-review 2026-10-28T23:24Z, author_checks/t1bfamily_check.py, output author_checks/t1bfamily_check_output.json, 4 s on one core). For
phi = z(1 + b z^2)/(2(1 + a s + z^2)^(p + 1)), any a > 0 and real b, (d) forces b > p + 1 > 0. On the upper axis w = c z + b z^(1 - 2p) + ...,
h = H z^(-2p)(1 - b z^(-2p) + o(z^(-2p))) and w e = 2h(h - 1) give e = -(2H/c) z^(-1 - 2p) + (2H/c)(H + b + b/c) z^(-1 - 4p) + ..., with a
strictly positive second coefficient, while -Delta_5 phi on the axis has only the powers z^(-1 - 2p - 2j); since 2p < 2 the power
z^(-1 - 4p) lies between the first two and cannot be matched. The strict positivity uses b > p + 1, proved for this family. Lesson for seeds: more general trial spaces should allow the
far-axis term z^(-1 - 4p) in eta (the first nonlinear far-field correction, R^(-2 alpha - 1)-type in the velocity), which a
rational seed in (1 + a s + z^2) lacks; that its coefficient (2 K^2 H/c)(H + b + b/c) is nonzero for every T1 profile has not
been proved.
 (i) Reduced-parameter minimization of the closed T1 problem (referee record of 2026-10-28T23:40Z, 89 min on one core; exact
rational portrait certificates, floating-point transport and Green reconstruction; lead check 2026-10-28T23:42Z of the far-axis sign
test, author_checks/t1newton_tail_check.py, output author_checks/t1newton_tail_check_output.json, 6 s on one core; not verifier-checked). Family:
phi = z u^(-p) P(v, w), u = 1 + a s + z^2, v = a s/u, w = z^2/u, P = 1/2 - v/2 + (p/2 + p_z) w + sum_(j + k >= 2) theta_jk v^j w^k, with
a = 8, 2, 1 at c_l = 0.60, 0.68, 0.74 and the dilation fixed by p_s = -a(p + 1)/2. Every final field has an exact T1 portrait
certificate (W.grad log rho = c + (1 - Q)^p H(Q, T) > 0 by rational Bernstein bounds). Results:
 (1) The annular potential defect falls with the parameter count (4, 8, 16): 0.369, 0.100, 0.040 at c_l = 0.60; 0.340, 0.077, 0.017
at 0.68; 0.328, 0.044, 0.013 at 0.74, with the cubic source relation imposed to about 3e-10 relative. No floor was observed.
 (2) The potential norm is weak at the source: the difference phi - K^2 Delta_5^(-1)(-e) can carry the Delta_5-harmonic cubic
(p_z' - p_z)(z^3 - (3/4) r^2 z), whose squared five-dimensional L^2 mass in a ball of radius rho is O(rho^11) (norm O(rho^(11/2))). In the 16-parameter fields the input p_z
is 0.016, 0.049, 0.069 while the reconstructed p_z' is 12.3, 3.45, 1.76, and the direct vorticity discrepancy between -Delta_5 phi
and K^2 e (normalized by the quadratic sum of the two RMS values on a log-polar grid) is 0.70, 0.60, 0.49.
 (3) The pole sign of (g) fails for all three fields: the upper-axis coefficient of z^(-1 - 2p) in -Delta_5 phi is
T_phi = 8a(pA - B + C) - 2p(2p - 1)A with A = P(0, 1), B = P_v(0, 1), C = P_w(0, 1), equal to 275.2, 28.46, 33.40 > 0 (lead-checked
from the saved coefficients to 1e-6 relative), so these fields also fail the tested far-axis condition (a residual statement, not a bound on the distance to a profile).
 (4) A probe at c_l = 0.74 that penalizes both cubic conditions (p_z' = p_z and the source relation) reaches D = 0.040, K = 5.71,
p_z = 0.0948, p_z' = 0.0943, T_phi = -35.8 < 0 (passes the pole sign), with direct vorticity discrepancy 0.298 after refinement.
 (5) Damped Picard (damping 0.05 and 0.1, two gauge conventions) and depth-three Anderson iterations all end in a gauge failure or
in S < 0 with p_z < 0 within 16 steps; a free-c_l probe runs to the imposed ceiling 0.7499 (D = 0.0128, sampled checks only).
Reading: the annular potential defect is a weak closure diagnostic that can conceal large derivative and vorticity defects at
the source; the direct vorticity discrepancy is the sharper test. Imposing the source jet
and the pole sign leaves it at about 0.3 with 16 parameters at c_l = 0.74. This is a quantified failure for one family, not an
obstruction.
 (j) Scalar conditions on the two-parameter family of (h) (referee record of 2026-10-29T00:18Z, 76 min on one core; exact proofs
for the portrait and the region, floating-point transport and Green reconstruction; lead check 2026-10-29T00:24Z,
author_checks/t1scal_check.py, output author_checks/t1scal_check_output.json, 13 s on one core: the radial-speed formula, the axis coefficients
C0, C1 and the region below symbolically; not verifier-checked). Put p = 1/(2c_l), delta = 1 + c_l, d = b - p - 1. The source jet
condition N2 of (d), K^2 = delta^2 (4a(p + 1)/(3d) - 1) > 0, and the pole sign N3 of (g), a < A(p) = p(2p - 1)/(4(p + 1))
= (1 - c_l)/(4c_l(1 + 2c_l)), together give exactly the triangle 0 < d < p(2p - 1)/3, 3d/(4(p + 1)) < a < A(p). For 0 < b <= 3 and
every a > 0 the field has the T1 portrait (proved: at a = 1 the logarithmic radial speed is c_l + [3t - 1 + b u t(5t - 3)]/(2(1 + u)^(p + 1))
>= c_l - 1/2 with u = R^2, t = z^2/R^2, and the map (r, z) -> (sqrt(a) r, z) conjugates general a to a = 1).
 (1) In the triangle the induced strain S is negative at every sampled point (seven values of b, up to 52 aspects each, a down to
1e-5 A(p)); the largest value, at the corner with K = 0, is -0.024, -0.049, -0.081, -0.120 at c_l = 0.62, 0.66, 0.70, 0.74. So no
sampled member satisfies the strain normalization N1, the jet condition and the pole sign together (sampled, not a certificate over
the triangle).
 (2) Dropping the pole sign, the closest finite-amplitude N1-N2 points have relative potential defects 459 to 1261 (annular norm);
the lowest-defect sampled N1-N2 points have defects 1.00, 0.86, 0.73, 0.64 at c_l = 0.62, 0.66, 0.70, 0.74, all violating N3.
 (3) The baseline b = 3 with the aspect a optimized over a = 2^(j/2) has defect 0.781, 0.715, 0.654, 0.600 at c_l = 0.62, 0.66, 0.70,
0.74 and keeps decreasing through 0.552, 0.510, 0.473 at c_l = 0.78, 0.82, 0.86 (the rows above 3/4 are diagnostics outside the
class). The sampled defects decrease across the values below and above 3/4; no special feature at 3/4 was resolved in this scan, which
does not establish monotonicity between the samples or exclude a threshold in another quantity. The referee found no singularity at c_l = 3/4 in the source eigenvalues
(c_l - 1/2, 1 + c_l), in the transport equations or in the leading odd-mode Newton divisors l - 1 + 1/c_l; A(2/3) = 1/30 > 0.
The only coincidence is formal: the first quadratic term of the far field has degree 3 alpha + 1 = 3/c_l - 2, equal to 2 at
c_l = 3/4, where in unrestricted parity it could feed a constant boundary term into the dipole moment. For fields with
U(x, y, -z) = J U(x, y, z), J = diag(1, 1, -1) (phi odd in z, as in all T1 seeds above), the pressure is even in z and the axial
dipole vanishes by parity (FAR_FIELD_ANALYSIS.md section 6).
 (4) The analytic exclusion of the family repeats (h) independently.
 (k) Direct vorticity discrepancy for a two-series family (referee record of 2026-10-29T01:14Z, 91 min on one core; exact algebra for
the axis expansion and the portrait certificates, floating-point transport and Green reconstruction; lead check
2026-10-29T01:17Z, author_checks/t1vort_check.py, output author_checks/t1vort_check_output.json, 40 s on one core, confirms the axis formulas
T_j and U_1 below, the 5D harmonic identity, K^2 S = 1/2 and U_1 for the three saved best fields; not verifier-checked). Family:
phi = z[u^(-p) P(v, w) + u^(-2p) Q(v, w)], u = 1 + a s + z^2, v = a s/u, w = z^2/u, P = 1/2 - v/2 + (p/2 + p_z) w + O((v + w)^2),
Q = O((v + w)^2), so p_s = -a(p + 1)/2, phi is odd in z and decays. Objective: E = (mean over 81 logarithmic shells, 0.02 <= R <= 50,
of eps(R)^2)^(1/2), eps(R) = RMS_mu(-Delta_5 phi - K^2 e)/RMS_mu(K^2 e), with the cubic source relation of (d), p_z' = p_z and the
first two far-axis coefficient matches as heavy penalties (largest normalized constraint residual 2.5e-4 in the final fields).
 (1) Exact axis expansion. With A_j = P_j(0, 1), B_j = d_v P_j(0, 1), C_j = d_w P_j(0, 1) ((P_1, P_2) = (P, Q)), the coefficient of
z^(-1 - 2jp) in -Delta_5 phi on the upper axis is T_j = 8a(jpA_j - B_j + C_j) - 2jp(2jp - 1)A_j. The axis transport (c_l z + 2 phi) e
= 2h(h - 1) with h = H z^(-2p)(1 - b z^(-2p) + ...), b = 2A_1, gives the transported coefficients -2K^2 H/c_l and
(2K^2 H/c_l)(H + b + b/c_l). On the axis the transported expansion contains only the powers z^(-1 - 2p - 2jp - 2m) (j >= 1, m >= 0)
and z^(-1 - 2p), so it has no term at z^(-3 - 1/c_l), while the first series generates one with coefficient
U_1 = -8a[p(p + 1)A_1 - (p + 1)B_1 + 2(p + 1)C_1 - P_vw + P_ww] + (2p + 1)(2p + 2)(pA_1 + C_1) (second derivatives at (0, 1)). For
1/2 < c_l < 1 the exponent 3 + 1/c_l lies strictly between 1 + 2/c_l and 1 + 3/c_l, so an exact profile in this family needs
U_1 = 0, one linear condition on the jet of P at (0, 1) that was not imposed: U_1 = 714.2, 547.9, 572.3 for the best fields at
c_l = 0.68, 0.74 and the free run (lead recomputation agrees to 1e-12). The family also lacks the power z^(-1 - 3/c_l) that the
transport produces at the next order. This is an incompleteness of the ansatz, not an obstruction.
 (2) Ladder (8, 16, 24 parameters, nested; fine-grid validation). c_l = 0.68 (a = 2): E = 0.340, 0.278, 0.251, max eps 0.78, 0.60,
0.55 near R = 1.1 to 1.2; c_l = 0.74 (a = 1): E = 0.378, 0.267, 0.260, max eps 0.89, 0.54, 0.56 near R = 1.3 to 1.6. From 16 to 24
parameters E falls by 9.7 percent at 0.68 and by 2.7 percent at 0.74, where the worst shell gets worse. At 24 parameters the
shell-band RMS errors are 0.008 and 0.013 for 0.02 <= R < 0.2, 0.31 and 0.30 for 0.2 <= R < 3, and 0.29 and 0.32 for 3 <= R <= 50:
the source conditions remove the source mismatch of (i), and the discrepancy sits at intermediate and large radii. K = 7.89 and
6.44, S = 0.0080 and 0.0121 (K^2 S = 1/2), max q/K = 1.03 and 1.09 on the axis near z = 0.58 and 0.84. The annular potential defect,
small in (i), is 0.84 and 0.73 here. Every final field has exact rational portrait certificates (positive logarithmic radial speed
for two radii; the origin is the only equilibrium and every backward meridional orbit converges to it). The c_l = 0.60 ladder failed
refinement and was not reported.
 (3) c_l free in [0.55, 0.85] (diagnostic beyond 3/4): it ends at 0.849965, within 3.6e-5 of the imposed ceiling, with E = 0.223,
smaller than at either fixed value; no feature at c_l = 3/4 was resolved in this run. In the reflection class the resonance at alpha + 2/c_l = 3 involves
only the 5D l = 0 harmonic (-Delta_5(R^(-g) Y_l) = [l(l + 3) + g(3 - g)] R^(-g - 2) Y_l), which is even in z and excluded, and
int over centered balls of K^2 e dV_5 vanishes by parity, so the finite-part diagnostic is identically zero there. At c_l = 3/5 the
same formula resonates at g = 3/c_l - 1 = 4 with the odd l = 1 harmonic, which parity does not exclude; this is the coincidence
3 alpha + 1 = 3 already listed in FAR_FIELD_ANALYSIS.md section 5.
Reading: E decreases with the parameter count but slows markedly at c_l = 0.74 and is about 0.25 at 24 parameters at both interior
values, with a known unmatched axis power in the family. This is a finite, quantified failure of one ansatz; it neither indicates
convergence nor bounds the discrepancy from below.
 (l) Source-jet closure and transported strain of the two best numerical states (added 2026-10-29T01:28Z; referee record of
2026-10-29T01:00Z, 35 min on one core; identities lead-checked in author_checks/t1diag_check.py; source values verifier-confirmed
2026-10-29T01:09Z; the transported strains of the repaired fields, -0.812 and -0.514, reproduced by the verifier with a separate
implementation 2026-10-29T02:02Z, changes below 5e-6 under angular, step, start-radius and cutoff refinements, tail enclosure open;
band contributions and swirl comparisons not verifier-checked). (1) Source-jet identities. Let z0 be an axis
zero of W_z = c z + 2 phi(0, z) with q(0, z0) = K != 0, so phi_z(0, z0) = 1/2 by the swirl equation. Differentiating
W_z q_z + (1 - 2 phi_z) q = 0 once at z0 gives (1 + c) q_z = 2 phi_zz K, and the vorticity equation at the stagnation point gives
(1 + c) eta = d_z(q^2) = 2 K q_z, hence q_z = 2 K phi_zz/(1 + c) and eta = 4 K^2 phi_zz/(1 + c)^2 at z0, with
eta = -Delta_5 phi = -(4 phi_rr + phi_zz) on the axis. (2) Newton kernel. With the 5D fundamental solution 1/(8 pi^2 |x|^3) of
-Delta_5 and d^5 y = 2 pi^2 R^4 (1 - mu^2) dR dmu for axisymmetric integrands, phi_z at the centre equals
(3/4) int_0^infinity dR int_{-1}^{1} mu (1 - mu^2) eta dmu (R = e^x gives the referee's e^x dx form); the lead check reproduces
phi_z(0) = 1 to 1e-20 for three explicit decaying fields. (3) Measured: for the frozen fields of the degree-36 and degree-48 states
(c_l = 0.749, K = 3.5) the stored jets are q_z = -0.0126 and -0.113 against the required +0.0351 and +0.0430, and
eta = -0.0507 and -0.450 against +0.141 and +0.172. Integrating q and eta along the characteristics of each state's own W from the
source (eighth-order, refreshed angular derivatives of log h; phi plus eps (z - z0) exp(-(r^2 + (z - z0)^2)/0.09) with
eps = 2.96e-7 and 1.94e-7, which makes phi_z(0, z0) = 1/2 exactly and keeps phi_rr, phi_zz at z0) and applying (2) gives K^2 S = -0.812 and -0.514 instead of +1/2; for
the degree-48 field the contributions are +0.030, -0.133, -0.383, -0.027 from source distances (0, 0.3), (0.3, 3), (3, 30), (30, 1000)
in the working gauge (refinement changes K^2 S by 7e-7; two quadratures agree to 1.5e-6; the tail beyond 1000 is extrapolated).
The stored q differs from the transported q_K by 0.022, 0.326, 0.727, 0.807 (relative, measure dlogR dmu) in the R ranges
(0.001, 0.3), (0.3, 3), (3, 30), (30, 1000). (4) The primary search's frozen-phi spectral solve, which had seemed to show an 80
percent change of the swirl coefficients, omitted the q interface rows; its ball, shell and exterior blocks decouple and the
shell and exterior q vanish (verifier, research record of 01:09Z: q-interface cost 1,023,964.6 for the degree-36 field). With
hard C^2 matching of the Legendre coefficients of q, R q_R and R^2 q_RR at both interfaces (199 constraints, 1509 free
variables) the referee's solve has condition number 2214 and agrees with q_K to 0.15 percent.
Reading: these states fail the necessary source-jet relations in sign, and the swirl that their own meridional field
transports induces a source strain of the wrong sign. The measurements do not bound their distance to an Euler profile. The computed transported strains are negative. A rigorous transport and tail error bound establishing S[phi] < 0 would
exclude every source amplitude K for the normalized transported swirl of each fixed meridional field (K^2 S[phi] <= 0); no such
bound exists here (the tail enclosure is open). Excluding all other swirls would additionally need the source-basin and
uniqueness hypotheses of the transport statement for q. This is a statement about two numerical states, not about the class.
Search consequences: the induced-strain route does not exclude T1. A T1 fixed point needs a positive near-axis eta budget that
survives reconstruction, and its cubic source jet must satisfy (d) (p_s and p_z of opposite signs). For these seeds the needed
amplitude is large at small c_l (K about 10.8 at c_l = 0.60, 3.9 at 0.68, 2.5 at 0.74); this is seed-dependent, not a bound.
 (m) Closed single-source Newton-Krylov solve (added 2026-10-29T03:19Z; referee record of 2026-10-29T02:59Z, 88 min on one core,
floating point; lead checks in author_checks/t1nk_check.py and author_checks/t1nk_check2.py with JSON outputs; the solve is not verifier-checked, its end values are, see below). Problem:
phi odd in z with phi_z(0, 0) = 1/2, -Delta_5 phi = K^2 e[phi] with e the source-normalized transported vorticity of phi's own
meridional field, K^2 S[phi] = 1/2 with S the Newton-kernel strain moment of (l) (2), dilation fixed by the cubic source coefficient. Trial
space: the two-series seed of (k) at c_l = 0.68 and 0.74 (degree 24), two cubic source terms, and Gaussians in log R (centres
equally spaced on [-3.8, 5], width 1.2 spacings) times odd angular polynomials; 101 and 401 free coefficients; not nested, and the
seed's second fractional tail is fixed. Result: not converged. With 401 coefficients the vorticity discrepancy E of (k) fell from
0.2507 to 0.1758 (c_l = 0.68) and from 0.2598 to 0.1317 (0.74); with 101 it ended at 0.2562 and 0.2324; K rose to 9.99 and 9.36
(S = 0.0050 and 0.0057). The largest shell errors are 0.79 at R = 1.98 and 0.52 at R = 2.66, toward the pole at radii 0.2 to 3.
The second far-axis vorticity coefficient has opposite signs in the elliptic and transported fields (148 against -2729, 151 against
-2903). Doubling transport and collocation grids changes E by at most 1.3e-6. The smallest Jacobian singular values (0.02 to 0.06,
gauge row included) belong to intermediate and far radii near the axis, and the merit still decreased slightly at the end, so no
stationary minimum was shown. Positive strain and a sampled outflow condition held at every accepted step. Lead checks:
K^2 S = 1/2, phi_z(0, 0) = 1/2, oddness, central-difference -Delta_5 phi against the saved elliptic vorticity at the shell nodes
(relative 4e-4 or better, step 2e-3 R), the saved shell errors recomputed from the saved arrays (agreement 1e-5), and the leading
far-axis coefficient (0.4 percent). The starting values E = 0.2507 and 0.2598 agree to four digits with the verifier's independent
transport of the same fields (2026-10-29T02:59Z, E = 0.250716 and 0.259768). Verifier reproduction of the end values
(2026-10-29T03:43Z, floating point, finite grid of 81 radii and 128 and 256 angles): E = 0.256204, 0.232434, 0.175826, 0.131671
for the four final fields, within 2e-6 of the saved values (largest difference 1.92e-6); the second far-axis coefficients (elliptic 148.39 and 151.09,
transported -2729.38 and -2903.47 for the 401-coefficient fields) by an independent axis quadrature, under the hypothesis that the
positive axis is outgoing, now discharged (next paragraph) (verifier proof that the positive axis is outgoing; lead cross-review 2026-10-29T03:48Z, author_checks/topic82_check.py: the axis first integral
w e = 2 h (h - 1), T2_transport = (2 K^2 H/c_l)(H + 2A + 2A/c_l), and T2_elliptic fixed at the seed value because the added
powers R^(1 - beta - 2j) never equal R^(1 - 2 beta) for 1 < beta < 2).
Verifier global source certificate of the four final fields (2026-10-29T03:56Z; lead cross-review 2026-10-29T04:34Z):
with P(x, mu) = phi, the radial drift is D = W_m . grad log R = c_l + [2 mu P - (1 - mu^2) P_mu]/R (the P_x terms cancel; lead
re-derived), each Gaussian angular factor A = mu L(mu^2) contributes (1 + R^2)^(-p) B(x) [2 mu A - (1 - mu^2) A'], and the cubic
envelope z (b_s s + b_z z^2)(1 + R^2)^(-p-1) contributes R^2 (1 + R^2)^(-p-1) [-b_s + (6 b_s - 3 b_z) mu^2 + 5 (b_z - b_s) mu^4] (lead
re-derived). Interval enclosures (Bernstein form in t = mu^2) on complete partitions of x in [-7, 13], an origin bound for
R <= 2^-9 and an exterior bound for R >= 2^18 give D >= 3.5e-4, 2.5e-4, 3.4e-4 and 6.6e-5 (the regions overlap since
exp(-7) < 2^-9 and 2^18 < exp(13)). The lead sample of D on the saved grids (author_checks/radial_drift_check.py) has minimum c_l - 1/2 at
the source, as the source limit D -> c_l - 1/2 + (3/2) mu^2 requires, so the certified constants are conservative and not
contradicted. D >= gamma > 0 is the hypothesis W . x >= gamma |x|^2 of the smooth transport argument below, so h and e of these
fields are smooth and unique in the bounded class. Verifier full-space strain of the two 401-coefficient fields (floating
point, two refinements, stored K): S = 0.0050105 and 0.0057118, scalar closure defects with the stored K 6.0e-6 and 4.5e-6.
Verifier global strain of the canonical fields (2026-10-29T03:06Z, CONFIRMED by the verifier as numerical values; proof of the
decay and kernel cross-reviewed by the lead 2026-10-29T03:19Z): for the degree-24 two-series fields S = 0.0080398 (c_l = 0.68) and
0.0120563 (0.74) with the stored K^2, 2 K^2 S - 1 = 5.0e-6 and 1.1e-5. The finite-ball smoothness hypothesis of that computation
holds for the seven canonical potentials by the verifier's smooth-source transport argument (lead cross-review 2026-10-29T03:19Z):
for smooth W with W(0) = 0, a global radial bound W . x >= gamma |x|^2, at most linear growth and a positive diagonal source
linearization, and, in the axisymmetric specialization, phi odd in z with phi = z/2 + O(R^3) (all satisfied by the canonical
fields), the source-normalized h = exp(int_(-inf)^0 (2 phi_z - 1)(Phi_t x) dt) and e = int_(-inf)^0 exp((1 + c_l) t) d_z(h^2)(Phi_t x) dt are
C^infinity; h is unique among continuous source-normalized solutions and e among solutions bounded near the source; h is
even and e odd in z, h = 1 + O(|x|^2), e = O(|x|).
Reading: the closed single-source problem was not solved; the trial space kept the second fractional far-axis tail coefficient
at the seed value, with the sign opposite to the transported one, and the largest errors sit at intermediate radii toward the
pole, where the trial space could change the field. Grid doubling and the independent transport support the stability of the
measured E; they are not a discretization bound. This is an unconverged local search, not a
floor and not an obstruction. Search consequence: the next experiment of FINAL_REPORT 7.5.
 (n) Nested closed single-source solve with free tails (added 2026-10-29T05:10Z; referee record of 2026-10-29T05:03Z, about 100 min on
one core, floating point; lead checks in author_checks/t1nk2_check.py and author_checks/t1nk2_T3_check.py with outputs; verifier checks noted).
Same closed problem as (m). Trial space: the final field of (m) plus z^3 (1 + R^2)^(-p-1) (coefficient p_z fixed by the cubic
relation (d)), free quintic source terms z s^2, z^3 s, z^5 times (1 + R^2)^(-p-2), clamped degree-five B-splines in x = log R on
[-7, 7] with 20, 40, 80 intervals times mu P_2j(mu) (14, 16, 18 angular functions), multiplied by R (1 + R^2)^(-p) and the flat
cutoff sigma(x + 7) sigma(7 - x), and four free tails mu-polynomials times R (1 + R^2)^(-nu), nu = p, 2p, p + 1, 3p, with cutoff
sigma((x - 2)/2). The levels are exactly nested by knot insertion. Discrete constraints imposed by algebraic elimination, holding to floating-point root tolerance on every accepted iterate: the cubic
relation (relative defect at most 1.7e-11 on every accepted iterate and 3e-14 or better on the four final fields), K^2 S = 1/2, the far-axis vorticity coefficients T_1, T_2, T_3 of the elliptic field
equal to those of the transported field, and U_1 = 0 (below 1e-10 in the production floating-point evaluation; exact rational evaluation of the saved coefficients
gives |U_1| from 5.3e-11 to 5.6e-10, nonzero for all four fields, so the axis constraints hold to numerical root tolerance and
not exactly; verifier, far-axis coefficient proof); dilation fixed by p_s. Far-axis transport formulas (lead,
sympy, author_checks/t1nk2_T3_check_output.txt), with b = 2A(1), d = 2B(1), a = 2 K^2 H/c and H the axis integral of (2 phi_z - 1):
T_1 = -a, T_2 = a[H + (1 + k) b], T_3 = a[(1 + k)/2 {d - (1 + 2k) b^2} - (2 + k) b H], and the first transported coefficient of
the U-series vanishes. The verifier proves these coefficients and the vanishing transported U_1 from the axis first
integral w e = 2h(h - 1), and extracts the elliptic pole coefficients L_gamma[F] = gamma(3 - gamma)F(1) + 4F'(1) of A, B, C, D
(gamma = k - 1, 2k - 1, k + 1, 3k - 1) exactly from the saved coefficients; the lead rederived that proof, including the seed
pole extraction (author_checks/topic87_C_check.py, sympy, all identities hold, 2026-10-29T05:43Z). Independent relative defects in T_1, T_2, T_3
are at most 8.5e-9 for all four fields, by quadrature refinement for H, not by interval enclosure. Results: E = 0.0779, 0.0544, 0.0547 at 405, 783, 1601 free coefficients for c_l = 0.74 (start 0.1317) and
0.1084 at 405 for 0.68 (start 0.1758); doubled transport and collocation grids change E by at most 1.4e-5. None meets
E < 1e-2. Level 1: the linear model predicts almost no decrease (ratio 0.99995, smallest singular values 0.021 to 0.066; Jacobian against
centred directional differences on these modes up to 14 percent of sigma; not a stationarity proof); level
2 was still decreasing (12 percent in its last step); level 3 was memory-limited (200 Krylov directions, collocation 301 by 208)
and has a narrow inner defect 0.346 at R = 0.001 outside the E window (reproduced by the verifier's independent fixed-K
transport on 26 inner radii: 0.3463 at R = 0.00102; a maximum of about 0.00142 at level 2). The wide-domain relative L2 defect rose from 0.080 to
0.100, so E is not monotone with every norm. Remaining error at level 2: band RMS 0.0056, 0.075, 0.053, 0.011 on R in [0.02, 0.2],
[0.2, 3], [3, 50], [50, 1e4]; largest shell error 0.137 at R = 1, mu = 0.855; 71 percent of the [0.2, 3] squared error at mu > 0.75.
Regularity: each field is a Cartesian C^4 potential with C^3 velocity and not C^5 (exact rational fifth-derivative jumps at the
internal knots; verifier, exact spline registration, all four fields). All four fields have a certified global source portrait (verifier
certificate: D >= 1.9357e-4, 1.6224e-4, 4.4716e-5 at levels 1 to 3 at c_l = 0.74 and 1.2152e-4 at c_l = 0.68, on a complete partition of
[-7, 13] times [0, 1] plus origin and exterior bounds), so h is C^3 and e is C^2 and the full velocity is a globally decaying Cartesian C^3 field, not C^4 in the meridional velocity (verifier proof of the finite-order transport argument, applied to all four certified fields, 2026-10-29T06:37Z); a portrait certificate is not a closure check. The verifier's independent fixed-K transport of the level-3 field gives E = 0.054667 at 128 and 256 angles (largest shell error 0.149 at R = 1, far band 0.0116, transported-vorticity difference 6.0e-6 shell angular-L2 relative; 2026-10-29T06:31Z), so all four nested closure-defect measurements are independently reproduced. The level-1 E is reproduced by an independent fixed-K
transport (0.07793 at 128 and 256 angles against 0.07792 saved; the largest shell angular-L2 relative difference of the
transported vorticity is 1.5e-3; verifier 2026-10-29T05:04Z). Lead checks on all four saved grids:
E recomputed exactly from the shell errors, q = K h and eta = K^2 e exactly, h even and e, phi odd to 1e-14, the quintic-spline
-Delta_5 phi against the saved elliptic eta (largest relative difference 2.0e-5, 9.4e-7, 8.1e-8, 1.5e-5 for 0.02 <= R <= 50), the
axis identity w e = 2 h (h - 1) (3.5e-5 or better), 2 K^2 S - 1 by the trapezoid rule (-3.8e-5 or smaller in magnitude), and H,
T_1 from the grid against the summaries (1e-5 relative). Reading: an unconverged local search, not a floor and not an obstruction;
the closure defect of the closed single-source problem fell to 0.054 at c_l = 0.74 in a C^4 trial space and the remaining error
sits near the axis at intermediate radii. Continuation (added 2026-10-29T06:55Z; referee record of 2026-10-29T06:51Z, 99 min on one
core, floating point; lead check author_checks/t1nk3_check.py with output): level 2 three more accepted steps, E 0.0544 to 0.0529
(last merit decrease 0.07 percent); level 2a, the same radial splines with 24 instead of 16 angular functions (1175
coefficients, exactly nested by zero padding; composite angular collocation, 128 Gauss nodes on each of [0, 0.75] and
[0.75, 1]; 421 radii on [1e-3, 1e4]), solved with a disk-stored assembled Jacobian, streamed QR and LSQR (peak 457 MiB),
two accepted steps, E 0.0473 and 0.0434 (doubled grids 0.0434; 161 by 512 comparison quadrature 0.0435); neither level met
the stop rule. The near-axis error was not removed (largest shell error 0.122 to 0.130 at R = 1, mu = 0.89; share at mu > 0.75
of the [0.2, 3] squared error 71 to 76 percent); band RMS [3, 50] 0.051 to 0.032, [50, 1e4] 0.0095 to 0.018; wide relative L2
0.094 to 0.093. Constraints: cubic relation 3e-15, T_1, T_2, T_3 equal on the production grid (doubled-grid relative tail
mismatch 4e-6), U_1 below 1e-11, K = 9.18. Geometric extrapolation of the three level-2a values gives about 0.035 (low
confidence); weakest singular direction: assembled Jacobian against re-closed differences 20 percent apart. Lead checks on
both saved grids: E recomputed (0.0529492, 0.0433989), q = K h and eta = K^2 e to roundoff, phi and e odd to 7e-15, the
quintic-spline -Delta_5 phi against the saved elliptic eta (1.0e-6 and 1.4e-6 relative for 0.02 <= R <= 50), the axis
identity (2.2e-6, 3.5e-6), 2 K^2 S - 1 by the trapezoid rule (-1.1e-5, -1.2e-5), T_1 from H (5e-6 relative). Not
verifier-checked when added; verifier 2026-10-29T09:00Z: an independent fixed-K characteristic transport with the stored K
reproduces E = 0.052949 and 0.043399 (128 and 256 angular nodes; differences 8e-8 and 3e-7), largest shell errors 0.122 and 0.130
at R = 1, far-band E 0.0095 and 0.0181 on 31 radii from 50 to 1e4. Verifier 2026-10-29T08:24Z and 08:27Z: both saved fields have
certified global source portraits (exact spline registration, interval certificate, independent 224-bit replay;
W . y >= gamma |y|^2 with gamma >= 2.0e-4 for level 2a and gamma >= 3.9e-4 for the continued level 2), so for both h is C^3,
e is C^2 and the full velocity is a globally decaying Cartesian C^3 field. Search consequence: FINAL_REPORT 7.5.
Second continuation (added 2026-10-29T08:44Z; referee record of 2026-10-29T08:39Z, 99 min on one core, floating point; lead check
author_checks/t1nk4_check.py with output). The 20 percent disagreement was a finite-difference step error in ill-scaled tail columns; a
forward tangent of the transport agrees with re-closed differences to 1.3e-4 relative. Frozen-source representability (source
K^2 e[phi], cubic coefficient, K and tail targets frozen at the level-2a endpoint, linear constraints kept, no re-closure):
E_lin = 0.0114 (40 intervals, 24 angular functions), 0.0104 (49 intervals, knots added at the midpoints of the nine radial intervals that meet [0.2, 3]), 0.0071 (40
intervals, 32 angular functions; largest shell error 0.017 at R = 1.10). Level 2b (49 intervals, 24 angular, 1391 coefficients,
exact zero padding): five accepted Gauss-Newton steps, E 0.0434 to 0.03904 (step 4) and 0.03915 (step 5, merit-accepted while E
rose 0.28 percent; last linear model 0.69 percent merit decrease; about 19 min per Jacobian cycle); a matched coarse-space step
gives 0.0414. Endpoint: largest shell error 0.123 at R = 1, mu = 0.896; share at mu > 0.75 of the [0.2, 3] squared error 78
percent; bands 0.0041, 0.060, 0.027, 0.0063; wide relative L2 0.088; K = 9.49, S = 0.0055; doubled grids 0.03915. Lead checks
on the saved grid: E recomputed (0.0391480), q = K h and eta = K^2 e to roundoff, phi odd to 6.5e-15, spline -Delta_5 phi
against the saved elliptic eta 1.6e-6, axis identity 2.8e-6, 2 K^2 S - 1 = -1.2e-5, T_1 from H 4.5e-6 relative, cubic relation
2.1e-15. Reading: in the discrete frozen-source sense below, the remaining defect is mainly a fixed-point mismatch between phi and its
transported source rather than a limit of the trial space at the level of 0.007 (no resolution estimate for the nonlinear
problem follows); Gauss-Newton stagnates near 0.039. Not verifier-checked when added.
Verifier 2026-10-29T08:56Z: the level-2b field registered by an exact change of basis (45 coarse and 9 fine splines to 54; 13245
exact conversion checks, of which 13230 polynomial identities, and 909 operator checks); the potential is C^4, not C^5, across 48 knots and the meridional velocity C^3. Verifier
2026-10-29T09:04:56Z (202 checks, no primary code executed): an independent reconstruction of the six saved fits from their exact
coefficients with its own Laplacian evaluator reproduces the three frozen-source values, 0.01140, 0.01038, 0.00706 against the saved
source and 0.01140, 0.01038, 0.00706 against an independently transported source (far band 0.0072, 0.0072, 0.0023 on 31 radii
and 192 angles); the fits minimizing the core error alone give 0.0104, 0.0094, 0.0052 with far-band errors 2136, 490 and 8230.
Confirmed in this discrete frozen-source sense only: L phi - T(phi) = (L phi - eta_0) + (eta_0 - T(phi)) and the fit measures
only the first term, so the values prove no infimum, nonlinear solution or resolution bound. Verifier 2026-10-29T09:11Z (747
checks): rational corrections of at most 3.2e-9 in the four tail coefficients make T_1, T_2, U_1 and T_3 and the source
coefficient equal exactly to those of the level-2a endpoint's elliptic field (which match the transported targets only to the
production-grid tolerance), changing the fit values by at most 9e-18; verifier 2026-10-29T09:28Z: a standalone derivation of the
source contributions to the four coefficients (22 checks). Lead review of both proofs: correct (author_checks/frozen_constraint_proof_check.py,
21 checks; author_checks/note53_proofs_check.py, part A). Primary runs of the solver code of the first nested levels to its stop rule (merit
decrease below 1 percent over 20 accepted steps): c_l = 0.74 level 2, 25 accepted steps, E = 0.0537; c_l = 0.68 level 2, 24
accepted steps, E = 0.0786; both 0.0537 and 0.0786 on doubled transport and collocation grids [primary search, running the
referee's code]. Verifier 2026-10-29T09:18Z: both final fields frozen; independent operators (522 checks each) and an exact
fifth-derivative recurrence show 39 nonzero jumps at mu = 9/10, so each potential is C^4 but not C^5 and the meridional velocity
C^3 but not C^4; both E values were later reproduced by independent fixed-K transports (below). Lead check: scipy's spline derivative reproduces all
39 jumps of each field to 1.3e-12 (author_checks/note53_proofs_check.py, part B).
Verifier 2026-10-29T09:47:19Z: the level-2b field has a certified global source portrait (exact spline registration, 897 interval
leaves with analytic origin and exterior bounds, independent 224-bit replay; W . y >= gamma |y|^2 with gamma >= 7.5e-4), so the
transport conclusions of the earlier certified fields apply (h in C^3, e in C^2, globally decaying Cartesian C^3 velocity); verifier 2026-10-29T10:09Z: its independent fixed-K transport with the stored K gives E = 0.039149 at 128 and 256 angular nodes against the saved 0.039148, largest shell error 0.123 at R = 1, far band E = 0.0063 on 31 radii (1427 checks). Verifier 2026-10-29T10:23Z: the stopped level-2 solve at c_l = 0.68 has a certified global source portrait as well (505 leaves, 224-bit replay, gamma >= 6.88e-4). Verifier 2026-10-29T11:04Z: so has the stopped level-2 solve at c_l = 0.74 (40 radial intervals, 16 angular functions; 899 leaves, 224-bit replay, gamma >= 5.08e-5), and the independent fixed-K transport of the c_l = 0.68 field with the stored K gives E = 0.078597 (128 angular nodes) and 0.078596 (256) against the saved 0.078595, largest shell error 0.156 at R = 4.34, far band E = 0.011 (1420 checks); E < 0.01 is refuted for that field on these grids. Verifier 2026-10-29T11:33Z: the independent fixed-K transport of the stopped level-2 solve at c_l = 0.74 with the stored K gives E = 0.053678 (128 angular nodes) and 0.053677 (256) against the saved 0.053677, largest shell error 0.121 at R = 1.0, far band E = 0.0091 (1420 checks); E < 0.01 is refuted for that field on these grids as well. Fixed-point test (referee record, started 2026-10-29T08:42:04Z): in a level 3c of 49
intervals and 32 angular functions (1855 coefficients; contains level 2b and the 40 x 32 fit space by exact zero padding;
retransported start E = 0.03915), the frozen-source fit gives E_lin = 0.00454 (0.01085 with 24 angular functions) but
recomputing the source from it (normalization, cubic relation and far-axis conditions imposed again) gives E = 3.13 (largest
shell error 9.68 at R = 37.3, mu = 0.975). Plain iteration accepted one half step (E 0.0391 to 1.65) before the scalar strain
root was lost; Anderson (depth 5) accepted 30 safeguarded damped steps and no accelerated step (last E 0.185); neither lowered
the best E [iteration counts checked by the verifier from the saved histories, 09:35Z]. The stored 1855 x 1855 derivative
matrix A of the map at the start (tangent against fully re-closed differences 5.4e-6 and 9.5e-7 relative) has leading real
eigenvalue 12.588 equal to its spectral radius and a floating-point count of 214 eigenvalues outside the unit disk (3 real above
1), changed to 215 or 218 by relative perturbations of 1e-10. Verifier 2026-10-29T09:40Z (exact rational arithmetic on the
stored binary matrix and the stored real vector from a floating-point eigenvector calculation; no exact eigenpair is
certified or needed): Q = v^T (A - I) v > 0, and since ||v + beta w||^2 - ||v||^2 = 2 beta Q + beta^2 ||w||^2
with w = (A - I) v, every damped map (1 - beta) I + beta A with constant beta > 0 expands v in the solver's coordinate Euclidean
norm. Lead check (author_checks/damping_cert_check.py, 12 PASS): the verifier's frozen matrix is byte-identical to the referee's, the
eigenvector residual is 1.25e-13, the float quotient equals the exact value and lambda - 1, a separate eigen-decomposition gives
12.5881745575, 214 and 3, and the expansion factors for beta = 0.01 to 1 range from 1.0116 to 12.59. Verifier 09:51:45Z
(review of the lead check): CONFIRMED for the stored matrix; for the derivative of the exact nonlinear map the conclusion is
OPEN (no bound relating it to the stored matrix), and other norms and nonlinear neighbourhoods are not covered. Gauss-Newton on the closed residual in level 3c (final answer 2026-10-29T10:23Z) accepted 25 steps: two with full Jacobians (E 0.03828, 0.03712; 56.5 process-wall minutes for both), thirteen chord steps with the second Jacobian (E to 0.0321615, last decrease 0.005 percent), and ten fresh-tangent steps in 24-dimensional subspaces, merit-accepted with E between 0.03222 and 0.03240 (merit 0.027748 to 0.027713). Best state (last chord step): E = 0.0321615 (doubled grids 0.0321622, 161 x 512 comparison quadrature 0.0322571), bands 0.0044, 0.051, 0.018, 0.0042, largest shell error 0.106 at R = 1.10, mu = 0.927, relative L2 0.075, K = 10.22, S = 0.00479, 79 percent of the [0.2, 3] squared error at mu > 0.75; its frozen-source fit gives E_lin = 0.00506 and reclosure 2.53. Lead checks on its saved grid (author_checks/t1nk5_check.py, 10:25Z): E recomputed, q = K h and eta = K^2 e to roundoff, spline -Delta_5 phi against the saved eta 2.7e-6, axis identity 5.8e-6, 2 K^2 S - 1 = -1.2e-5, T_1 from H 4.8e-6 relative. The referee notes that its largest inserted knot is at R = e^1.225 = 3.40, the midpoint of the interval containing R = 3. Reading: Gauss-Newton stalls near 0.032 in this space; the GN values are referee values. Verifier 2026-10-29T10:57Z: the saved level-3c field registered independently from its stored coefficients (909 operator checks on 14061 saved points, 29 exact regularity and provenance checks); all 48 interior fifth-derivative jumps at mu = 9/10 are nonzero (largest -1626.716047), so the potential is C^4 and not C^5 and the meridional velocity C^3 and not C^4 (exact rational arithmetic; the 48 jumps reproduced by the lead to 1e-11 with a separate spline evaluation, author_checks/level3c_jump_check.py). Verifier 2026-10-29T11:35Z: its global source portrait is certified (exact spline registration, 897 interval leaves with analytic origin and exterior bounds, independent 224-bit replay; W . y >= gamma |y|^2 with gamma >= 8.60e-4), so the transport conclusions of the earlier certified fields apply (h in C^3, e in C^2, globally decaying Cartesian C^3 velocity); verifier 2026-10-29T11:34Z: its independent fixed-K transport with the stored K gives E = 0.032162 at 128 and 256 angular nodes against the saved 0.032162, largest shell error 0.106 at R = 1.10, far band E = 0.0042 on 31 radii (1430 checks); E < 0.01 is refuted for that field on these grids.

Missing estimate: a bound on J_+ in terms of controlled source data, from the full transport and elliptic coupling. Search
consequences: report max q/K and its location for every T1 candidate; at c_l >= 0.64, T1 runs whose swirl peaks at the source
with a quartic first variation need K above K_crit(c_l).

## 5f. Restrictions on the odd-swirl ring portrait T2 (added 2026-10-28T21:04Z; referee record of 2026-10-28T20:59Z, lead checks noted)

Setting as in 5b and 5c: reflection class (O), exactly two zeros of W_m in the closed half-plane, the origin (axis saddle with
radial inflow, v(0, 0) = -(1 + 3c)/2, Gamma ~ C s^2 z) and the ring (1, 0) (off-axis source, nodal order m = 1, eigenvalues
1 + c along r and 2c - 1 along z, K = q_z(1, 0)). Write a = 2c - 1, delta = 1 + c, lambda = 1 + 4c, A0 = (1 + 3c)/2,
w(z) = c z + 2 phi(0, z), F(s) = phi_z(s, 0). The lead re-derived (i), (ii), (iii) and (v) by hand and checked (i), (ii), the
origin jets of (vii) and the ring relations of (vii) symbolically (author_checks/t2_ring_check.py, output author_checks/t2_ring_check_output.json,
1.7 s on one core).

(i) Axis vanishing (exact). On the upper axis w > 0 and w = lambda z + O(z^3). The axis swirl equation w q' + (1 - 2 phi_z) q = 0
has 1 - 2 phi_z(0, 0) = -3c, so q(0, z) is a multiple of z^(3c/lambda) (smooth positive factor), with 3c/lambda in (1/2, 9/16):
not C^1, so q(0, z) = 0 on the whole upper axis. Then w eta' + delta eta = 0 there, whose nonzero solutions grow like z^(-delta/lambda)
at the origin, so eta(0, z) = 0. Differentiating the eta equation once in s gives w (eta_s)' + [delta + 2c - 2 phi_z(0, z)] eta_s = 0;
the bracket vanishes at z = 0 (delta + 2c - 2 A0 = 0) and is even in z, so it is O(z^2), every solution has a finite limit at the
origin, and odd parity forces eta_s(0, z) = 0. Hence near the upper axis q = s Q(z) + O(s^2) and eta = s^2 J(z) + O(s^3).

(ii) Axis equations and a closed form (exact). w Q' = (2 w' - lambda) Q and w J' + (1 + 7c - 2 w') J = 2 Q Q', with Q ~ C z and
J ~ 2 C^2 z/(3c) at the origin. Q does not vanish on z > 0, and Y = w J/Q^2 satisfies w (Y - 4)' + (w' - delta)(Y - 4) = -2a.
With tau' = 1/w, normalized so that tau(z) - c^(-1) log z -> 0 as z -> infinity, and M = w e^(-delta tau), regularity at the origin (M -> 0 there, Y -> 2 lambda/(3c)) selects

    w(z) J(z) / Q(z)^2 = 4 - (2a / M(z)) int_0^z e^(-delta tau(u)) du.

So w J < 4 Q^2 on the upper axis. At infinity M ~ c z^(-1/c) -> 0 while the integral tends to I > 0, so J < 0 far out on the
upper axis. Under the differentiated tail expansion, Q ~ B_1 z^(-2-1/c) with B_1/C > 0, J ~ D_2 z^(-5-1/c) with
D_2 = -(2a/c^2) B_1^2 I < 0, and for the far-field coefficients B(mu), E(mu) (both odd): B(1) = 0, B'(1) = -2 B_1, E(1) = E'(1) = 0,
E''(1) = 8 D_2 < 0.

(iii) Equator (exact under the portrait). E(s) = eta_z(s, 0) solves h E' + (delta + b) E = 2 Q_eq(s)^2 with h = 2s(c - F),
b = c + 2F + 2s F' and Q_eq(s) = q_z(s, 0), which does not vanish for s > 0. At the ring h = 0 and E(1) = 2K^2/(3c). Along both
equatorial orbits leaving the ring the forcing is positive, so E cannot reach zero: eta_z(s, 0) > 0 for all s > 0, and the far-field
E'(0) > 0. Together with (ii): eta > 0 near the upper equator, eta < 0 near the upper axis far out, and E(mu) has a zero in 0 < mu < 1.
Consequence: no T2 profile has eta >= 0 in z > 0 (a subclass obstruction; T2 itself is not excluded).

(iv) Sign of the swirl (referee; argument as in MATHEMATICAL_FORMULATION.md 6 (k)). The weighted divergence div(r W_m) = 3 c r
excludes closed orbits and cycles, decay confines backward orbits, and the outgoing manifold of the origin is the axis, so every
orbit in r, z > 0 has the ring as its backward limit and q has the sign of K there.

(v) Amplitude transmission (exact). Integrating the equatorial q equation from the ring to the origin,
C = K exp( int_0^1 (1 + 3c - 2F + 2s F') / (2s (c - F)) ds ), with removable singularities at both ends; C/K > 0. The origin
amplitude is not a second free amplitude. For the linear germ F = A0 - nu s, nu = delta/2, the integrand vanishes and C = K.

(vi) Strain moment (exact, from the 5D Green representation): int_0^inf int_0^inf z r^3 eta (r^2 + z^2)^(-5/2) dz dr = (1 + 3c)/3.
The positive equatorial contribution must dominate the negative polar one; no bound on their ratio was found, so no contradiction.
The eta-norm identity, with the five-dimensional measure dV_5 = 2 pi^2 r^3 dr dz and under differentiated tail assumptions
that make the integrals converge, (2 - 3c + c gamma) int R^(-gamma) eta^2 = int R^(-gamma) (2v - gamma U_R/R) eta^2 + 2 int R^(-gamma) eta d_z(q^2)
(0 < gamma < 15, gamma > 3 - 2/c) and the weighted circulation means of MATHEMATICAL_FORMULATION.md 6 (a) are further tests.

(vii) Local formal theory (formal; no convergence claimed). Ring: on monomials x^i z^(2n+1), x = s - 1, the q and eta divisors are
i delta + 2 n a and (i + 1) delta + (2n + 1) a; only i = n = 0 (q) is resonant and supplies K; the first eta condition is
3c eta_z(1, 0) = 2K^2 (a cubic combination of phi, not a condition on K); no forced logarithms for c_l > 1/2; a small divisor a appears
in the z^3 swirl coefficient as c_l -> 1/2 (for the linear germ T(1) = K (10 c delta - K^2)/(3 c a)). A finite circulation order m at
an off-axis source needs eigenvalues a/m and 3c - a/m; odd parity allows m = 1, 3, 5, .... Origin: with H_3, H_5, H_7 the odd 5D
harmonic polynomials, phi = A0 z + h_3 H_3 + h_5 H_5 + h_7 H_7 - (C^2/(72c)) s^3 z + O_w(9), q = C s z + (5 C h_3/lambda) s z^3 + O_w(7),
eta = (2C^2/(3c)) s^2 z + O_w(7), with no s^2 z term in q (lead-checked). On the equator the first incoming eta branch has exponent
(2 + 5c)/(1 + c), not an integer, so its coefficient must vanish; the first higher resonances are s^10 z^5 (q, c_l = 5/7) and
s^12 z^5 (eta, c_l = 2/3), each a compatibility question. For F = A0 - nu s, Q = K s, E = (2K^2/(3c)) s^2 an all-order formal
polynomial family satisfies every incoming condition for every c_l (it does not decay), so the local conditions are compatible.

(viii) Count (heuristic, not a theorem). In the elementary ledger (MATHEMATICAL_FORMULATION.md section 4), the ring gives one
amplitude and one resonance, c_l free and the ring-radius gauge cancel, and the quantized origin strain v(0, 0) = -(1 + 3c)/2 is
one more condition with no new amplitude, because the origin receives swirl along the equator and C is transmitted by (v). T2 is
therefore heuristically of codimension one among smooth profiles (two if the first incoming eta coefficient counts separately).
Lead remark: the same mechanism applies to any saddle that receives swirl, for example the origin of T3, whose strain is quantized
in the smooth stratum (Lemma 14 gives the vanishing of q on the equator; the selected quadratic stratum q = Q z^2 + ... has
v(0, 0) = (1 + 2c)/2, and the other smooth strata have even k >= 4); among smooth T1 to T3 profiles only T1 has a square elementary
ledger. In the Cartesian C^2 class of the prompt the saddle strain is not quantized and the ledgers of T2 and T3 become square
as well (section 5g; 5g (h) proves algebraic approximation rates for specified interior-cusp model functions, and their implications
for complete profiles and nonlinear residuals are not proved). Consequence for the search: T1 remains the primary smooth target; an elementary equation count
proves neither a Fredholm index nor a positive residual lower bound for T2 or T3, and a T2 or T3 residual that does not
decrease would not by itself be evidence against T1.

Seeds and rows. The referee supplied a finite-jet T2 seed that satisfies (i), (iii), the ring and origin jets of (vii) and a
far-field tail B = K mu (1 - mu^2), E = D mu (1 - mu^2)^2 (1 - 2 mu^2) (accompanying artifacts, referee ring seeds); its zero count
was checked on 391 x 320 grids for K = 1 and c_l in the prompt list (minimum W_z/z from 0.116 at c_l = 0.56 to 0.461 at 0.74), not
certified. The seed of 5c violates eta(0, z) = 0; that is a seed defect, not a solver constraint. Cheapest T2 rejection tests: extra
zeros; wrong sign of q in r, z > 0; nonzero q, eta or eta_s on the axis; eta_z(s, 0) <= 0 somewhere; eta >= 0 everywhere in z > 0;
E''(1) >= 0 for a resolved tail; then the strain moment (vi), the closed form (ii) and the amplitude relation (v).
Verifier check (2026-10-28T20:58Z record, noted here 2026-10-28T21:10Z). The verifier re-proved (i) and (ii) independently, under weaker
hypotheses (decay of phi(0, z) on the axis only, no zero of w for z > 0, C != 0): q = eta = eta_s = 0 on the axis,
J = 2 C^2 z/(3 c_l) + O(z^3) near the origin, the closed form of (ii), and J ~ D_2 z^(-5 - 1/c_l) with D_2 < 0, so eta takes both signs
in the upper half-plane (125 symbolic and high-precision tests). This alone gives the T2 row of the summary table without (iii).
Items (iii) to (viii) were not separately verifier-checked; the final report (3.13) states which of their smooth-portrait
consequences follow from this proof of (i) and (ii).

## 5g. Finite regularity: the Cartesian C^2 class (added 2026-10-28T21:48Z; referee record of 2026-10-28T21:43Z with a standalone proof and 55 passing checks; lead checks in author_checks/c2saddle_check.py, output author_checks/c2saddle_check_output.json, 1.8 s on one core; (a) to (d) verifier-checked 2026-10-28T22:07Z by an independent proof with 45 passing tests, with two qualifications adopted in (a) and (d); (e) to (h) are not verifier-confirmed)

The prompt asks for U globally C^2 or smoother as a Cartesian field, smooth across the axis and the origin. Sections 5b to 5f and
ORIGIN_AND_AXIS_REGULARITY.md assumed phi and q smooth in (s, z) (the smooth stratum). Here "smooth across the axis" is read as
Cartesian C^2 without coordinate artifacts, which is the class of the prompt; a literal C^infinity requirement would exclude the
branches below. Notation: a = 2c - 1, delta = 1 + c, w(z) = W_z(0, z).

(a) Thresholds (proved for the displayed leading power with derivative-controlled remainders; further terms can still fail).
T3 origin saddle: w = -mu z + ..., q ~ A(s) |z|^k with k = 1 + delta/mu. U is Cartesian C^2 iff k > 2 or k = 2 (polynomial
matching), for k not an even integer, C^(2, beta) iff k >= 2 + beta and C^m iff k > m (even integers k, including k = 2, give polynomial
factors and are exceptions; verifier qualification). So 0 < mu <= delta, v(0, 0) = (c + mu)/2,
radial eigenvalue (3c + mu)/2, axial eigenvalue -mu; the selected quadratic smooth value is mu = delta, k = 2 (the other smooth strata have even k >= 4, mu = delta/(k - 1)). A saddle passage argument (the
coefficients are Lipschitz in C^2) shows q(r_*, z)/z^k -> A(r_*) != 0 at every fixed r_* > 0, so the factor r in U^theta = r q
cannot hide the cusp. T2 origin saddle with a simple ring: q ~ C s^j z with nu = delta/(2j); U^theta ~ (-y, x) |x_h|^(2j) has
degree 2j + 1, so C^2 needs only j > 1/2: 0 < nu < delta and -1 - 2c < v(0, 0) < -c (the selected lowest-order simple-ring stratum has j = 1, v(0, 0) = -(1 + 3c)/2; integer higher-order strata are not
treated here).
S3 off-axis source: Gamma ~ C_+- |xi|^p with lambda_1 = a/p; nonpolynomial germs need p > 2, so 0 < lambda_1 < a/2. Requiring
q itself to be C^2 in r, or smooth in s, would impose the wrong condition.
(b) Local fractional T3 solutions exist (proved, local, not decaying). For every k > 2 and K, Q > 0 the s-independent problem
phi = F(z), q = q(z), w q' = (w' - delta) q, w'' = -4 q (q - K)/w with w = -mu z + O(z^(k+1)), q = Q z^k + O(z^(2k)) has a local
solution (contraction with constant O(eps^k)); it solves the full reduced equations including eta = -Delta_5 phi, with the explicit
pressure P = C_r s/2 + int_0^z [-2(1 - c) F - 2 w F'] and C_r = F' - F'^2 + w F'' + q^2 constant. Example (lead-checked to the
orders shown): c_l = 3/5, k = 5/2, K = Q = 1, mu = 16/15, q = |z|^(5/2) + (9/56)|z|^5 + ..., phi = -(5/6) z - (3/14) sgn(z) |z|^(7/2)
+ (139/1792) sgn(z) |z|^6 + ... (the last coefficient computed by the lead), a local C^(2, 1/2) solution with nonquantized strain.
It does not construct the sources at z = +-1 or a decaying profile.
(c) T3 equator in C^2 (proved under outward equatorial drift c - f > 0, f = phi_z(s, 0), h = 2s(c - f), b = c + 2f + 2s f').
Lemma 14's equatorial vanishing survives (Gamma(t) = e^(a t) Gamma(0), |Gamma| <= C r^2, 2 lambda_r > a). The limits
q ~ A(s) |z|^k and eta ~ E(s) sgn(z) |z|^(k - 1) satisfy h A' + (1 - 2f + k b) A = 0 and h E' + [delta + (k - 1) b] E = 0, hence
E(s) = K (3c + mu) A(s) / (mu (c - f(s))), both positive (lead-checked; at mu = delta this is the K gamma/delta formula of 5d (b)).
For k > 2, q_zz(s, 0) = eta_z(s, 0) = 0, so A and E are fractional limits, not the derivatives used in 5d. In a regular conormal
expansion (smooth radial coefficients, derivative-controlled remainders; an assumption, not implied by C^2) Poisson forces
phi_sing = -E(s) sgn(z) |z|^(k + 1) / (k (k + 1)), and nonlinear closure produces the exponent sets q: l k + 2n, eta: l k + 2n - 1,
phi: l k + 2n + 1 (l >= 1, n >= 0), plus homogeneous modes s^m |z|^(k + m d_*), d_* = (3c + mu)/mu; this list is not exhaustive.
A smooth cubic jet phi = f(0) z + h_3 z^3 + p_3 s z satisfies 6 h_3 + 8 p_3 = 0.
(d) Changed T3 statements. Inner finite part (only for 2 < k < 3, in the regular conormal sector; for larger k every
nonintegrable reciprocal term must be subtracted, verifier qualification): int_0^1 (Q/q - z^(-k)) dz = 1/(k - 1); axis C^2
and oddness alone do not force it (an axis-only example has the value 0). Amplitude transmission
log(Q/K) = -int_0^1 ((w' - delta)/w - k/z) dz. Central moment int r^3 z R^(-5) eta = -(c + mu)/3 (lead-checked from
phi_z(0, 0) = -(c + mu)/2). The source moments of 5d (c) are unchanged. The axis sign rules (eta >= 0 iff q <= K, q' >= 0 iff
phi_z <= 1/2 on 0 < z < 1), the angular relation c E(1) = -2 K B(1) < 0 and hence the one-signed eta obstruction for T3 survive in C^2.
(e) T2 in C^2 (formal unless stated). Lambda = 3c + 2 nu, phi_z(0, 0) = c + nu. For q ~ C r^rho sgn(z) |z|^p the indicial relation
is rho = 2(p - 1) + (3cp - a)/nu. An all-order formal family phi = z F(s), q = z A(s), eta = z E(s) exists for noninteger j > 1/2
(no vanishing divisor; convergence not proved). The incoming homogeneous eta mode s^tau, tau = (delta + Lambda)/(2 nu) > 1, is C^2
compatible and cannot be discarded for being nonintegral; eta_s(0, z) = 0 cannot be imposed without proof. Strain moment
int r^3 z R^(-5) eta = 2 (c + nu)/3. Axis q = eta = 0 and equatorial eta positivity survive; the outer-axis argument of 5f (ii) uses
smooth coefficients and does not transfer as it stands, so the T2 row of section 6 is stated for the smooth stratum.
(f) S3 in C^2. An exact annular example (singular at s = 0, so local only): phi = z (c - l/2 + l R_0^2/(2s)), Gamma = C_+- |s - R_0^2|^(a/l),
eta = 0, 0 < l < a/2. Odd fractional S3 germs on a vertical source admit an all-order formal construction.
(g) Count (heuristic bookkeeping, not dimension theorems). Relative excess of equations: T3 with a nonzero quadratic equatorial jet
+1 (k = 2 is still forced there); T3 with k > 2 unknown 0; T2 with a simple ring and j unknown 0; T2 with a fractional ring exponent
also unknown -1. The fractional T3 stratum is not a small C^2 perturbation of the quadratic one ((|z|^(2 + e))''(0) = 0). No
replacement scalar condition is proved; the vorticity-maximum condition is vacuous at the saddle (Omega = 0 there) and the
Bernoulli function gives D^2 H(0) = a (c I + S), compatible with every allowed strain. Fredholm index zero remains unproved for all
portraits, so even T1 isolation is conditional.
(h) Consequences for numerics (rates proved for model functions; measured by the referee at k = 5/2: 2.496 for values, 0.499 for the
C^2 error). For the stated interior-cusp model functions, polynomial approximations converge only algebraically: Chebyshev
coefficients of |z|^p decay like n^(-p-1), value error Theta(N^(-k)) for q, and O(N^(-(k - 2))) for q in C^2 and phi in C^3 for
derivative-aware approximations (approximate q'' or the third derivative of the singular potential and integrate). Verifier
qualification (2026-10-28T22:19Z, independent proof with 59 tests; wording corrected after the verifier audit of 22:27Z): for |z|^k
on [-1, 1] (an interior cusp at z = 0) the raw Chebyshev value truncations converge uniformly, but their second derivatives at the
interval endpoints z = +-1 do not converge for 2 < k <= 3 (successive increments of order N^(3 - k)); moving the cusp to an endpoint,
as a basis in z^2 does, changes the approximation problem and its rates, which are not covered by either proof. These are approximation rates, not rates for a solver or an Euler residual. These
model results suggest diagnostics near a fractional saddle (a slowly decreasing error near the equator, q_N/|z|^k not
converging uniformly at z = 0) but establish no convergence rate or residual floor for a complete profile or a nonlinear solver. A dedicated representation: q = |z|^k sum_j |z|^(j k) G_j(s, z^2),
phi = z F(s, z^2) + sgn(z) |z|^(k + 1) sum_j |z|^(j k) Psi_j(s, z^2) + Poisson corrections, k unknown, principal row
(k - 1)[-c - 2 phi_z(0, 0)] - delta = 0, the source rows q(0, 1) = K, phi(0, 1) = -c/2, phi_z(0, 1) = 1/2, and, if eta is represented,
E = -k(k + 1) Psi_0(s, 0), E(0) = 2 K Q/mu; keep k > 2 + beta for a differentiable chart (d/dk produces |z|^k log|z|). Diagnostics:
convergence of the fractional quotients of q, eta, phi; residuals both raw and divided by the predicted powers; Cartesian second
derivatives across the equator and along several approaches to the origin; Poisson consistency, moments, finite parts, tails and
the zero portrait; stability of k under every refinement.
(i) Other rows in C^2 (lead assessment, not refereed). 5e (i) and the T1 source budget use only the Green representation and the
axis relation, and hold for C^2 profiles. Statements built on finite jets (the quartic threshold 5e (iii), the source jets 5d (d),
the formal theory 5f (vii)) need the regularity of the jets they use. Propositions 1, 5 and 8 apply in the stated Cartesian C^2 class. Corollary 11 requires the smooth axis-matching hypotheses of
Proposition 10; its exclusion of axis swirl in class (O) is not established in the fractional Cartesian C^2 stratum (5b).

(j) The closed T3 problem for an explicit fractional seed family (added 2026-10-28T22:56Z; referee record of 2026-10-28T22:52Z with exact
rational positivity certificates for the portrait and floating-point numerics; lead checks in author_checks/t3frac_check.py, output
author_checks/t3frac_check_output.json, 23 s on one core; verifier, independently, 2026-10-28T23:21Z: the moments (P_3, S_3) = (0.44449,
0.056342) at c_l = 0.68 and (0.52044, 0.12151) at c_l = 0.74 (k = 2.75, a = 1/64), central moments 0.66957 and 0.74824, the wrong signs of
P_3 and A_3, and the transported h, e at 84 points to 1.5e-6; verifier, 2026-10-28T23:25Z: the portrait certificate of (2) on the
stated parameter rectangle, by an independent proof with exact polynomial checks; the iteration and the full-field defects are not
verifier-checked). Family: with delta = 1 + c, mu = delta/(k - 1),
u = a r^2 + z^2 (a > 0), phi = z F(u), F(u) = [-(c + mu)/2 + (-2 - 3c + mu) u + (2 - (c + mu)/2) u^2]/(1 + u)^3.
(1) Exact (lead-checked): F(0) = -(c + mu)/2, F(1) = -c/2, F(1) + 2F'(1) = 1/2, and the axis drift factors as
w = W_z(0, z) = z (z^2 - 1)(c z^4 + (4 + 3c - mu) z^2 + mu)/(1 + z^2)^3, so the axis zeros are the origin saddle (eigenvalues
(3c + mu)/2 radial, -mu axial) and S1 sources at (0, +-1) (eigenvalues c - 1/2, delta). On the axis the swirl factor h (h(0, 1) = 1)
satisfies h_z(0, 1) = (2c - mu + 1)/(1 + c).
(2) Portrait (referee proof, rational Bernstein certificates; verifier re-derived independently; not lead-checked): for 0.60 <= c <= 0.74, 2 <= k <= 3 and every a > 0,
W_r/r = c - F - 2 z^2 F' > 0 off the axis, there are no other zeros, and every off-equator backward orbit tends to a source; the
meridional velocity is O(R^-1) (faster than the similarity rate; the swirl carries the R^-alpha tail).
(3) Transported fields (exact identities, numerical coefficients): w e = 2h(h - 1) on the axis; h ~ Q_h z^k and e ~ (2 Q_h/mu) z^(k - 1) > 0
at the saddle; e < 0 far out on the axis; at each finite equatorial radius E_h (c - f)/A_h = (3c + mu)/mu, the ratio of 5g (b).
The transported vorticity K^2 e is not the seed's own vorticity: for 2 < k < 3 a smooth phi has no fractional axis term, and at
k = 2 the seed has -Delta_5 phi = -(8a + 6)(c + 1/2) z + O(R^3) (lead-checked), opposite in sign to the transported coefficient, so no
member of the family is a fixed point.
(4) Scalars (floating point; corrected plus-sign kernel; psi = (-Delta_5)^(-1) e, S_3 = psi_z(0, 1), P_3 = psi(0, 1), A_3 = psi_z(0, 0)).
At a = 1, S_3 < 0 in all twelve cases c in {0.60, 0.68, 0.74}, k in {2, 2.25, 2.5, 2.75} (from -0.0199 at c_l = 0.60 to -0.0046 at
c_l = 0.74, k = 2.75), so no real K. Over a in {1/128, ..., 4}, S_3 > 0 occurs only for small a (radial stretching), only at
c_l >= 0.68 and only for k > 2; best points (K^2 = 1/(2 S_3), position mismatch M = P_3/(2 S_3) + c/2, annular relative defect,
induced rate mu' = -c - A_3/S_3):
| c_l | k | a | S_3 | K | M | defect | mu' |
|---|---|---|---|---|---|---|---|
| 0.68 | 2.5 | 1/32 | 0.0208 | 4.91 | 8.75 | 21.1 | -27.6 |
| 0.68 | 2.75 | 1/64 | 0.0563 | 2.98 | 4.28 | 8.00 | -12.6 |
| 0.74 | 2.25 | 1/16 | 0.0326 | 3.92 | 5.18 | 19.9 | -16.6 |
| 0.74 | 2.5 | 1/32 | 0.0778 | 2.53 | 3.07 | 9.07 | -8.91 |
| 0.74 | 2.75 | 1/64 | 0.1215 | 2.03 | 2.51 | 5.84 | -6.90 |
A fixed point needs P_3 = -c S_3 < 0 and A_3 = -(c + mu) S_3 < 0; every positive-strain point has P_3 > 0 and A_3 > 0. The full Green
update of the best point is a saddle of the opposite orientation (axial eigenvalue +6.90, radial about -2.34), a portrait failure.
Mechanism: S_1 = 2(r^2 - 4)(r^2 + 1)^(-7/2) z + O(z^3) near the equator (lead-checked), so the kernel favours positive near-equatorial
vorticity at r > 2, which radial stretching supplies in the tested family (the expansion alone does not make that support
necessary: the full reflected kernel is positive at r = 1, z = 2, lead check); the position kernel rho_-^(-3) - rho_+^(-3) is positive in the whole upper
quadrant, so the same positive vorticity makes P_3 positive. No c_l selection root was observed at k = 2.75, a = 1/64
(S_3 = -0.032, 0.056, 0.122 at c_l = 0.60, 0.68, 0.74).
(5) Iteration (floating point). Pinning the source by updating c gives c_l' = (1 - l) c - l P_3/S_3; at the best point l = 0.05
already gives c_l' < 1/2. A projected Picard (back into the family, preserving source value, source strain and central strain)
moved c_l from 0.740 to 0.690 to 0.618, the defect from 5.84 to 7.30, and then lost the sign (S_3 = -0.0126); mu stayed in (0, delta].
The projection removes the generated fractional part, so this iteration cannot reach a fractional fixed point; a retained-fraction
iteration was not run.
(6) Numerical checks: harmonic degrees 31, 63, 95 give the best defect 5.83571, 5.83576, 5.83577; known-potential inversion relative
sup error 3.5e-8; transport residuals (RMS) 5.0e-5 (log swirl) and 1.9e-4 (vorticity). Not interval certificates.
Consequence for the search: in this family T3 is much farther from closure than T1 (best defect 5.84 against 0.61 for the T1
seeds of 5e (vii)), and its positive-strain mechanism opposes the position condition. This is a finite-family finding, not an
exclusion of T3 or of the fractional stratum.

## 6. Summary

Unless a row states otherwise, the nonexistence rows concern nontrivial, full-space, uniformly decaying Cartesian C^2
axisymmetric exact profiles, with the additional hypotheses displayed in the row. The prescribed-field row concerns transport
for a fixed meridional field before elliptic closure; the compactness row has smooth inputs and a C^(1,1) limit.

| range | status | basis |
|---|---|---|
| 0 < c_l < 1/2 | no nontrivial C^2 decaying axisymmetric profile (U(0) free) | CIV Thm 4.5 proof, Prop. 1 (verifier-confirmed) |
| any c_l > 0, no swirl | none | CIV Remark 4.6 argument |
| c_l = 1/2 | open; trivial if the meridional zero set is countable, in particular for real analytic profiles | Prop. 5 (refereed, verifier-confirmed); analytic case: verifier proof, lead-reviewed |
| 1/2 < c_l < 3/4 | not excluded by the results reviewed here | section 4 |
| any c_l > 0, reflection-symmetric, q(0) != 0, d_z(q^2) <= 0 for z > 0 | none | Prop. 8 (verifier-confirmed) |
| any c_l > 0, smooth stratum (hypotheses of Prop. 10), reflection class (O), all zeros of W_z(0, .) simple | no S1 source on the axis (q = 0 on the axis) | Cor. 11 (verifier-confirmed); not established in the fractional Cartesian C^2 stratum (5b) |
| c_n -> 1/2+, smooth profiles, uniform C^2 bound and decay, S1 point | a subsequence converges in C^1_loc to a decaying C^(1,1) nonanalytic critical profile with nonzero swirl and uncountable stagnation set | Prop. 12 (referee, lead-checked; verifier proof) |
| c_l -> 1/2+, single core of Hessian width, uniform shape | none for eps small | Prop. 13 (conditional; referee, lead-checked; verifier proof) |
| 1/2 < c_l < 3/4, T1, eta one-signed in z > 0 | none | 5e (i) (referee, lead-checked) |
| c_* < c_l < 3/4, T1, q <= K with quartic first variation | none unless K >= K_crit(c_l) | 5e (iii) (referee, lead-checked) |
| 1/2 < c_l < 3/4, prescribed smooth T1 meridional field under all hypotheses of 5e (vii) (a) (phi odd in z, phi_z(0) = 1/2, every backward characteristic tending to the source, continuous normalization h(0) = 1, bounded e, h decaying uniformly, absolutely convergent strain integral) with d_z(h^2) <= 0 in z > 0 | induced source strain negative (no T1 fixed point in this class) | 5e (vii) (a) (referee, lead-checked); no sign theorem without such a hypothesis: 5e (vii) (c) |
| 1/2 < c_l < 3/4, T2 (class O), smooth stratum, eta one-signed in z > 0 | none | 5f (i), (ii) (referee, lead-checked, verifier re-proved); C^2 status: 5g (e) |
| 1/2 < c_l < 3/4, T3 (class E), eta one-signed in z > 0 | none | 5d (b), (c) (referee, lead-checked); Cartesian C^2 extension: 5g (d) |
| 1/2 < c_l < 3/4, T2, T3 saddle strain in the Cartesian C^2 class | not quantized: 0 < mu <= delta (T3), 0 < nu < delta (T2 with a simple ring, p = 1; no such bound for a fractional ring exponent p > 2, verifier qualification) | 5g (a) (referee, lead-checked) |

The c_l < 1/2 statement is a proved obstruction for a clearly stated class. It says nothing about existence for c_l > 1/2.

## Appendix. Revision history

- v39, 2026-10-29T14:29Z: after a consistency review against the final report: the provenance paragraph states that 'not
  verifier-checked' annotations are dated and that later checks are recorded in the final report; Lemma 2 adds the
  verifier's statement that alpha-limit sets of exact profiles with c_l > 1/2 consist of zeros; Propositions 12 and 13 cite
  their standalone verifier proof (the earlier text also named an unrelated proof); 5f no longer says 'not yet'; (n)
  records the portrait certificates of the level-2a and continued level-2 fields; the level-2 maximum of the inner transport
  check in (n) is given as about 0.00142 (changed 2026-10-29T13:54Z).
- v38, 2026-10-29T11:39Z: incorporates a second review by the independent referee of v37 against the 26 findings (19 applied, seven
  partially; the new proofs of Proposition 8, the fractional example and the restriction of Corollary 11 found correct). A
  results-in-brief paragraph and a statement of how the provenance annotations map to records are added at the start; the
  summary caption separates the prescribed-field and compactness rows; the 5e (vii) (a) hypotheses (backward source basin,
  continuous normalization, bounded e) are stated in the summary row; the uniqueness classes of h and e are stated separately;
  the 5e (vii) (l) reading no longer asserts an exact sign of the transported strain; the 5g cross-reference no longer asserts
  approximation rates for complete profiles; section titles no longer refer to the task numbering; the formula checks in
  author_checks/auditrev_check.py were repaired (the cancellation root of finding 12 is now tested and every check enters all_pass).
  (n) records the verifier's portrait certificate and fixed-K transport of the level-3c field and the fixed-K transport of the
  stopped level-2 solve at c_l = 0.74.
- v37, 2026-10-29T11:20Z: incorporates an adversarial review of v34 by an independent referee (26 findings, each checked by
  the lead; formula checks in author_checks/auditrev_check.py). Corollary 11 is restricted to the smooth stratum (its exclusion of
  axis swirl in class (O) is not established in the fractional Cartesian C^2 stratum); the (S2) quantization, the
  Proposition 12 interpretation, the index relation and the 5e (vii) (a) sign result state the hypotheses their proofs use;
  Proposition 8 is proved by the maximum principle; the derivative tail bound in section 2 is marked as an extra assumption;
  the numerical record no longer infers distances, monotone trends or residual floors; notation and provenance are stated at the start and the summary table caption in section 6; this history moved to the appendix. (n) records the verifier's registration and
  exact C^4-not-C^5 jumps of the level-3c field and states the damping certificate for the stored matrix and stored vector.
- v36, 2026-10-29T11:05Z and earlier (v35 to v1 at the times listed): v35 2026-10-29T10:52Z, v34 2026-10-29T10:29Z, v33 2026-10-29T09:56Z, v32 2026-10-29T09:35Z, v31 2026-10-29T09:13Z, v30 2026-10-29T08:44Z, v29 2026-10-29T07:03Z, v28 2026-10-29T06:55Z, v27 2026-10-29T06:03Z, v26 2026-10-29T05:43Z, v25 2026-10-29T05:35Z, v24 2026-10-29T05:10Z, v23 2026-10-29T04:34Z, v22 2026-10-29T03:48Z, v21 2026-10-29T03:19Z, v20 2026-10-29T02:10Z, v19 2026-10-29T01:28Z, v18 2026-10-29T01:17Z, v17 2026-10-29T00:22Z, v16 2026-10-28T22:56Z, v15 22:08Z, v14 21:48Z, v13 21:07Z, v12 21:04Z, v11 20:58Z, v10 20:49Z, v9 20:44Z, v8 20:38Z, v7 20:26Z, v6 20:24Z, v5 19:53Z, v4 19:37Z, v3 19:14Z, v2 18:38Z, v1 18:30Z; v3 corrected the S1 pressure remark and recorded the verifier's
audit of Proposition 6; v4 adds Propositions 8 and 9; v5 adds Proposition 10 and Corollary 11 and withdraws the class (O)
S1-pair example of Corollary 7; v6 records the verifier's confirmation of Proposition 10 and Corollary 11; v7 adds section 5b, zero-set portraits and Propositions 12 and 13; v8 records the verifier's confirmation of 5b and adds 5c, a decaying T2 seed family; v9 adds 5d, Lemma 14 and a T3 seed family; v10 adds 5e, T1 restrictions from the referee; v11 records the verifier's exact certificate for the 5c seeds; v12 adds 5f, T2 restrictions from the referee; v13 records the referee check of 5d, corrects its resonance list and adds T3 restrictions; 2026-10-28T21:10Z verifier check of 5f (i), (ii); v14 corrects the sign of the source-strain kernel in 5d (c) and adds 5g, finite regularity in the Cartesian C^2 class; v15 adds 5e (vii), the induced source strain of prescribed T1 fields, and records the verifier check of 5g (a) to (d); v16 adds 5g (j), the closed T3 problem for an explicit fractional seed family, and 5e (vii) (g), (h), the verifier's exclusions of the T1 seed families; v17 adds 5e (vii) (i), (j), referee records on reduced T1 families; v18 adds 5e (vii) (k), the direct vorticity discrepancy for a two-series T1 family; v19 adds 5e (vii) (l), source-jet closure and transported strain of the two best numerical states; v20 records the verifier's reproduction of the (l) strains; v21 qualifies the (l) reading and adds 5e (vii) (m), the closed single-source Newton-Krylov record and the verifier's global strain of the canonical fields; v22 records the verifier's reproduction of the (m) end values and qualifies its reading; v23 records the verifier's global source certificate of the (m) fields; v24 adds 5e (vii) (n), the nested closed single-source solve with free tails; v25 records in (n) the verifier's portrait
certificates of all four nested fields, its exact nonzero U_1 values and its independent inner-window transport; v36 records in (n) the certified portrait of the stopped level-2 solve at c_l = 0.74 and the fixed-K transport of the one at c_l = 0.68; v35 states Proposition 9 for smooth exact profiles with convergence in the regular meridional variables, as its proofs require; v34 records in (n) the final level-3c Gauss-Newton values, the level-2b fixed-K transport and the c_l = 0.68 runner portrait; v33 records in (n) the level-2b portrait certificate, the level-3c fixed-point test and the exact stored-matrix damping certificate; v32 records in (n) the exact frozen-source constraint repair, the source-term supplement, the final runner fields and their C^4 regularity, and qualifies the frozen-source reading; v31 records in (n) the verifier's fixed-K transports of the continued level 2 and level 2a, the
level-2b registration and the independent reconstruction of the frozen-source fits; v30 adds to (n) the frozen-source representability test and the radially refined level 2b; v29 records in (n) the verifier proof of the C^3 regularity for all four nested fields and the independent level-3 transport; v28 adds to (n) the continued level-2 and angularly refined level-2a solves; v27 records in 5 the verifier's smooth stagnation-segment example (analyticity needed in the finiteness statement); v26 records in (n) the verifier's proof of the
far-axis transport and pole coefficients and the lead's check of it.
