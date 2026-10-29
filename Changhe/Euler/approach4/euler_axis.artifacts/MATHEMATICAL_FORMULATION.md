# Mathematical formulation (prompt sections 1, 2, 8 and 9)

Version v11, 2026-10-29T10:55Z

## 1. Self-similar ansatz and profile equations

tau = T - t, y = (x - x_*)/tau^{c_l}, u = tau^{c_l - 1} U(y), p = tau^{2 c_l - 2} P(y). Then
d_t u = tau^{c_l - 2} [(1 - c_l) U + c_l y . grad U], u . grad u = tau^{c_l - 2} U . grad U, grad p = tau^{c_l - 2} grad P, so

    (1 - c) U + (c y + U) . grad U + grad P = 0,    div U = 0,     c = c_l.

Vorticity omega = tau^{-1} Omega(y) gives Omega + W . grad Omega - (Omega . grad) U = 0 with W = c y + U.
div W = 3c. The divergence of the linear similarity terms is div[(1 - c)U + c y . grad U] = div U + c y . grad(div U),
which vanishes when div U = 0 (exact symbolic identity, author_checks/docrev_M_check.py). The divergence of the momentum equation
therefore gives -Delta P = d_i U_j d_j U_i (checked symbolically in cylindrical form).

## 2. Axisymmetric reduced system

With U = U^r e_r + U^theta e_theta + U^z e_z independent of theta, W_r = c r + U^r, W_z = c z + U^z and
W_m . grad = W_r d_r + W_z d_z, the component equations are

    M_r     = (1 - c) U^r + W_m . grad U^r - (U^theta)^2 / r + d_r P = 0,
    M_theta = (1 - c) U^theta + W_m . grad U^theta + U^r U^theta / r = 0,
    M_z     = (1 - c) U^z + W_m . grad U^z + d_z P = 0,
    (1/r) d_r(r U^r) + d_z U^z = 0

(agreement with the Cartesian momentum equation: exact symbolic check on polynomial test fields, author_checks/docrev_M_check.py).
Define phi by U^r = -r d_z phi, U^z = 2 phi + r d_r phi (so phi = psi / r^2 for the Stokes stream function
psi with U^r = -d_z psi / r, U^z = d_r psi / r). Then div U = 0 identically and Omega^theta = d_z U^r - d_r U^z =
r (-Delta_5 phi), Delta_5 = d_rr + (3/r) d_r + d_zz, the axisymmetric Laplacian in R^5 = R^4 x R. So
eta = Omega^theta / r = -Delta_5 phi. Write q = U^theta / r, Gamma = r^2 q = r U^theta and v = U^r / r.

Checked symbolically for arbitrary phi, q, P (exact SymPy identities in author_checks/sym_checks.py, all passed; results in
author_checks/sym_checks_result.json):
- the swirl momentum component equals r R_q with R_q = q + W_m . grad q + 2 (U^r/r) q;
- the theta component of curl(momentum), d_z M_r - d_r M_z, equals r R_eta with
  R_eta = (1 + c) eta + W_m . grad eta - d_z(q^2);
- (1 - 2c) Gamma + W_m . grad Gamma = r^2 R_q (circulation form);
- div M = Delta P + d_i U_j d_j U_i.

So the reduced equations are the swirl equation divided by r and the azimuthal vorticity equation divided by r.
The meridional momentum equations are recovered from them only up to a gradient; the full-space pressure fixes
that gradient (FULL_SPACE_PRESSURE.md, section 3).

## 3. Function class

U is C^2 (or smoother) as a Cartesian field on R^3, uniformly decaying, axisymmetric, with nonzero swirl.
Not imposed: U(0) = 0, z-parity, finite energy, compact support, exponential decay, finite-domain boundary data.

Notation: R = |y|, vartheta the polar angle from the positive z-axis, mu = cos(vartheta), alpha = (1 - c)/c, so that
alpha + 1 = 1/c. Primary class: U = R^(-alpha) F(vartheta) + o(R^(-alpha)) uniformly in the angle, with F not
identically zero; this is an assumption on the class, not a consequence of decay. Where the corresponding expansions
exist, q = R^(-1/c) B(mu) + o(R^(-1/c)) and eta = R^(-1 - 1/c) E(mu) + o(R^(-1 - 1/c)). A uniform leading expansion of U
does not by itself give differentiated asymptotics or uniform decay of q; items that need them state them.

Regularity in reduced variables (ORIGIN_AND_AXIS_REGULARITY.md). In the stream gauge psi(0, z) = 0 (without it,
phi + C/r^2 gives the same velocity), U is C^infinity iff phi and q are smooth functions of (r^2, z) (the smooth stratum,
which the polynomial solvers search). For the C^2 class this is a sufficient, stronger representation choice, not a
characterization: radial powers must be tested in the reconstructed Cartesian velocity. Examples (exact symbolic check in
author_checks/docrev_M_check.py; chi a smooth compactly supported function of r^2 + z^2): phi = 0, q = r^3 chi gives
U = (-y r^3, x r^3, 0) chi, which is divergence free and Cartesian C^3 but not C^infinity; q = r^(3/2) chi gives a
Cartesian C^2 field with q_rr = (3/4) r^(-1/2) unbounded at the axis. The C^2 class is also larger at saddles that receive
swirl: there it admits fractional powers with nonquantized strain (AXISYMMETRIC_OBSTRUCTION_AUDIT.md section 5g). For
piecewise representations, smoothness of each piece does not give smoothness across the interfaces. Statements below that
use Taylor jets or classical axis derivatives (the S1, S2, S3 classification and items (c), (d), (j), (m) and (p) of
section 6) assume the regularity they use, which is the smooth stratum unless stated otherwise; where a classical
derivative is not available, a justified integral (characteristic) form of the equation is needed.

## 4. Gauge and nontriviality (prompt section 8)

Exact symmetries of the profile equation that preserve the decaying axisymmetric class: dilations
U_L(y) = L U(y/L), P_L(y) = L^2 P(y/L) (c_l unchanged), and rotations about the axis (trivial on axisymmetric fields).
The reflection z -> -z combined with U^z -> -U^z, U^r -> U^r, U^theta -> U^theta (or U^theta -> -U^theta) maps
solutions to solutions; it is a symmetry of the class but parity is not imposed. Reduced variables:
phi_L = L phi(y/L), q_L = q(y/L), eta_L = L^{-1} eta(y/L) (direct substitution: U^r = -r d_z phi scales correctly
because r d_z is dilation invariant). Far field: F_L = L^{1 + alpha} F, so int_{S^2} |F_L|^2 = L^{2(1 + alpha)} int |F|^2.

Reporting gauge: int_{S^2} |F|^2 dS = 1, a single dilation gauge. Invariant under dilation: c_l, DU(0), q(0),
Omega(0), max |Omega|, F / ||F||, and dimensionless shape ratios. Not a gauge: translation in z, vorticity amplitude, and
any second core normalization. Translation in z is not a symmetry of the decaying class: a plain translate
U(y - a e_z), P(y - a e_z) still decays, but its momentum residual is c a d_z U, which is generally nonzero; the
compensated map U(y - a e_z) - c a e_z, P(y - a e_z) + c (1 - c) a z solves the profile equation but tends to the constant
-c a e_z at infinity (exact symbolic checks in author_checks/docrev_M_check.py).

Expected dimension of the solution set ([lead] heuristic; the conditional local-isolation statement below was proved by
the [independent referee] and checked by the [verifier]; its hypotheses are not established, so this is a conditional
count, not a theorem). Write the profile equation as F(U, c) = U + (U . grad) U + grad P + c D U = 0
with D U = y . grad U - U. Then c multiplies the generator of the dilation symmetry and F(U_L, c) = L F(U, c)(./L), so at a
solution Z = U - y . grad U lies in the kernel of A = D_U F. Statement: if the equation is realized as a C^1 map between
Banach spaces of axisymmetric fields in a chart that treats the c-dependent tails correctly, A is Fredholm of index 0,
ker A = R Z, and a nonzero functional psi annihilating the range of A satisfies the transversality condition
kappa = psi(b) != 0, with b the c-derivative of the equation in that chart, then the free-c system with one dilation gauge
g (Dg Z != 0) has an invertible linearization and the pair ([U], c_l) is locally isolated. b = -Z holds only in a common
physical-field space; in an exponent-dependent asymptotic chart b differs ([verifier] qualification). None of the three
hypotheses is proved. Caveats: (1) in the direct realization whose domain and residual spaces carry the same critical
weights (phi ~ R^(-alpha), q ~ R^(-alpha-1), eta ~ R^(-alpha-2)) with their ordinary weighted or graph norms, the transport
operators c R d_R + 1 and c R d_R + 1 + c are not Fredholm: bump sequences on logarithmic annuli are bounded in the domain,
have no convergent subsequence, and have images tending to zero ([verifier] proof). Other realizations (a space that
separates the leading angular tail from a faster remainder, stronger residual norms, or a weaker common weight) are not
covered by this argument and need their own estimates; (2) varying c moves the tail exponent,
d_c(R^(-alpha) F) = R^(-alpha)(d_c F + (log R / c^2) F), so the tail representation must follow alpha(c_l); (3) saddles on
the axis add matching conditions (Proposition 10 of AXISYMMETRIC_OBSTRUCTION_AUDIT.md), and local counts at several
emitters do not simply add; (4) local isolation does not make the set of admissible c_l discrete (loss of compactness is
not controlled); (5) no identity of the form <F(U, c), xi(U, c)> = 0 for all admissible U is known (energy and virial
pairings do not vanish identically). Such an identity could explain a family, but a family does not require one: the
scalar map F(x, c) = (x - c)^2 has the solution family x = c, while every continuous xi with F xi = 0 on a neighborhood
vanishes (checked in author_checks/docrev_M_check.py). A family of gauged solutions through the profile in the same chart
contradicts local isolation, so it forces at least one of the three hypotheses to fail; a regular differentiable family (a C^1 parametrization with nonzero derivative; a C^1 parametrization of a nonconstant family can have zero derivative at an isolated parameter) has a tangent (h, c') != 0 with A h + b c' = 0 and Dg h = 0. Consequences for the search: free-c_l runs with one genuine dilation
gauge are the primary mode, fixed-c_l scans are diagnostics, and the gauge may be the phase condition
g(U) = <U - U_ref, Z(U_ref)>_H (or int_(S^2) |F|^2 = 1, or int |Omega|^4 = 1); q(0), source amplitudes and max |Omega| are
dilation invariant and cannot fix the scale. A positive residual floor at fixed c_l away from a solution is expected only
locally, near a transverse isolated profile; globally, residual infima can vanish without attainment, and discretization
error can leave a floor at a true exponent. Signatures: an isolated solution gives a signed scalar residual
r(c) = kappa (c - c_*) + ..., a stabilizing residual minimum whose value decreases under refinement, a sign change of the
adjoint-projected residual, and an invertible gauged free-c Jacobian; a regular differentiable family makes the gauged free-c Jacobian singular (its tangent is a null vector) and gives continuation with vanishing residual over an interval. A
shallow minimum alone distinguishes neither.

Nontriviality: swirl is necessary. This is the argument of Remark 4.6 of P. Constantin, M. Ignatova and V. Vicol,
arXiv:2602.17570v3, adapted to the present class (Cartesian C^2, uniformly decaying, U(0) not prescribed) in
AXISYMMETRIC_OBSTRUCTION_AUDIT.md sections 1 and 2. Swirl diagnostics: s_core = ||U^theta|| / ||U|| on B_{4 a_eff},
s_far = ||F_theta|| / ||F|| on S^2, with a_eff the vorticity half-maximum radius (the pre-registered specification, section 5).

## 5. Residuals (prompt section 9)

Defined in the pre-registered specification, sections 6.1, 6.2 and 8. For E = M, q, eta the linear damping term L_E and the nonlinear part N_E are
L_M = (1 - c) U, N_M = (U . grad) U (Cartesian vectors); L_q = q, N_q = U_m . grad q + 2 (U^r/r) q; and
L_eta = (1 + c) eta, N_eta = U_m . grad eta - d_z(q^2). For these equations the shell denominator is
D_E(S) = min(RMS_S(L_E), RMS_S(N_E)), and the three momentum components R_M^r, R_M^theta, R_M^z are each divided by the
vector denominator D_M(S). The elliptic residual R_ell = -Delta_5 phi - eta uses the denominator RMS_S(eta), and the
divergence residual R_div = div U uses RMS_S(|DU|) (Frobenius norm). Reported per shell: rho_E(S) = RMS_S(R_E) / D_E(S) and
m_E(S) = max_S |R_E| / D_E(S), on the dyadic shells 2^k a_eff <= R < 2^(k+1) a_eff, k = -6, ..., 11, and the origin ball
R < 2^(-6) a_eff, and separately on the axis collars (the part of each shell with sin(vartheta) < 0.05, with measure
R^2 dR dvartheta, without the sin weight); also absolute norms, the single-term ratio RMS(R_E)/RMS(L_E), the nonlinear
ratio RMS(R_E)/RMS(N_E) and the classical per-term ratio. Scaled far-field residuals R^{2 alpha + 1} R_M,
R^{2 alpha + 2} R_q, R^{2 alpha + 3} R_eta.

Reason for the min: two escapes are known. A large multiple of a compact steady Euler flow makes the nonlinear terms
dominate, so ratios with nonlinear denominators become small while the linear similarity terms are not balanced at all.
In the far tail, the full linear similarity operator ((1 - c) U + c y . grad U, and its reduced analogues
q + c y . grad q and (1 + c) eta + c y . grad eta) annihilates the leading term R^{-alpha} F (and R^(-1/c) B,
R^(-1 - 1/c) E) exactly, while its damping component L_E alone does not; so ratios with linear denominators become small in
the tail even if the nonlinear correction is wrong. Using the smaller of the two scales in each shell defeats both.

## 6. Exact identities used as diagnostics

Provenance rule: each item states who derived or checked it; items without such a statement are [lead] derivations that
were not independently checked.

Scope. These are necessary identities for exact profiles. They use different equations: the swirl equation (with
div U = 0 and the definitions of phi and W) for (a), (b), (j) and (p); the swirl and eta equations for (d) and (m); the
eta equation with eta = -Delta_5 phi for (i), (n) and the first part of (q), while (l) uses eta = -Delta_5 phi and the S1
conditions; the primitive momentum equation with its pressure for (e), (f) and (h), and also its curl for (g); (c), (k)
and (o) use the swirl equation and (e), and the axis part of (c) also uses the eta equation. The swirl equation alone does
not imply the others: phi = z^2, q = 0,
P = 0 gives R_q = 0 identically but W . M = 2 (c + 2)(c + 5) != 0 at r = 0, z = 1, where M is the momentum residual
(exact symbolic check in author_checks/docrev_M_check.py; this field is not a decaying profile and only shows the logical gap).
Integrated identities also need boundary estimates at infinity. Unless an item says otherwise, the integrated forms assume
the differentiated far-field expansion U = R^(-alpha) F + O(R^(-2 alpha - 1)), P = R^(-2 alpha) Q + o(R^(-2 alpha)), with the
corresponding derivative estimates (in particular |DU| = O(R^(-alpha - 1))), and a remainder that is integrable after the
stated finite-part subtractions.

(a) Weighted circulation identities. W_m . grad Gamma = (2c - 1) Gamma and div W = 3c give, for p > 0,
div(W Gamma^p R^{-beta}) = c [3 + p(1 - alpha) - beta] Gamma^p R^{-beta} - beta Gamma^p R^{-beta - 1} U_R. The boundary term
at infinity vanishes for beta > 3 + p(1 - alpha) (Gamma = O(R^{1 - alpha})); at the origin Gamma = O(r^2) and W = O(1)
make it vanish for beta < 2p + 2. Hence, for beta in (3 + p(1 - alpha), 2p + 2) (nonempty iff p > c_l),

    int Gamma^p R^{-beta - 1} U_R dV = -(c/beta) (beta - 3 - p(1 - alpha)) int Gamma^p R^{-beta} dV.

For p = 1 or p = 2 no sign condition on Gamma is needed. For non-integer p, assume Gamma >= 0 (a negative number has no
real non-integer power), or replace Gamma^p by |Gamma|^p with the regularity needed for its chain rule; p > 1 is
sufficient, since |Gamma|^p is then C^1 ([verifier] qualification). For p = 2 (Gamma^2 >= 0) the Gamma^2 R^{-beta}-weighted
mean of U_R / R is strictly negative for every admissible beta: on average the swirl region has radial inflow toward
the origin. At the endpoint beta -> 2p + 2 both integrals stay finite, so the limit does not localize the identity at the
origin ([verifier]). Status: [verifier] proof for p = 1 and p = 2, and 43 floating-point checks that cover (a) and the
axial first integral of (d) together (largest consistency error 2.36e-11).

(b) Normalized circulation G = Gamma R^{alpha - 1}: W . grad G = -(1 - alpha) G U_R / R exactly (from (2c - 1) +
(alpha - 1) c = 0; exact symbolic check in author_checks/docrev_M_check.py). Where G != 0 this reads
W . grad log|G| = -(1 - alpha) U_R / R, so there G is constant along W-orbits exactly where U_R = 0 and, for c_l > 1/2,
|G| increases where U_R < 0 (G itself only where G > 0; [verifier] correction). Where G = 0, for example on the axis,
W . grad G = 0 whatever the sign of U_R. Along rays G tends to sin^2(vartheta) B(mu) where the q tail exists.

(c) One-signed swirl. Gamma(phi_t y) = e^{(2c - 1) t} Gamma(y) along meridional orbits. Every backward meridional orbit stays
in a compact set; its alpha-limit set is nonempty, compact and contains a zero of W_m, and it is a single zero if the zero
set is finite (AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Lemma 2). For c_l > 1/2 and an exact profile, H of (e) is constant on an
alpha-limit set, so every alpha-limit set consists of zeros of W ([verifier]). The hyperbolic swirl-emitting zeros are
classified (AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Proposition 6, confirmed by the [verifier]): S1 is an axis zero with
q != 0, where d_r U^r = -1/2 and the zero is a hyperbolic source; S2 is a hyperbolic axis source with q = 0 there; S3 is
an off-axis source. Non-hyperbolic zeros are not classified. If every orbit with Gamma != 0 converges in backward time to
one S1 source y0 with q(y0) = q0 (near which Gamma = q0 r^2 (1 + o(1))), then Gamma has the sign of q0 wherever it is
nonzero, and B(mu), where it exists, does not change sign. A sign change of B therefore requires a swirl-carrying orbit
whose alpha-limit set is a zero other than y0 (among hyperbolic sources: S2, S3 or a second S1 point; non-hyperbolic zeros
are not classified) or is not a single point. On the axis: if phi and q are smooth in (r^2, z),
phi(0, z) = O(|z|^(-alpha)), phi_z(0, z) = O(|z|^(-alpha - 1)) and every zero of W_z(0, .) is simple, then either q(0, .)
vanishes identically, or every repelling axis zero is an S1 source with the same amplitude q0 and q(0, .) has the sign of
q0 except at the attracting axis zeros, where it vanishes (AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Corollary 11, confirmed by
the [verifier]). Under these hypotheses a second axis S1 point cannot change the sign of B at the poles.

(d) Axis relation (first stated by the referee; re-derived by the lead). On the axis W_r = 0, so with
A(z) = -phi_z(0, z), W_z(z) = c z + 2 phi(0, z) and W_z' = c - 2A, the axis restrictions are
(1 + 2A) q + W_z q' = 0 and (1 + c) eta + W_z eta' = 2 q q'. Since (1 + c) eta + W_z eta' = (W_z eta)' + (1 + 2A) eta,
F = W_z eta satisfies F' = -(1 + 2A) eta + 2 q q'. Let z0 be an axis source with q0 = q(0, z0) != 0 (so 1 + 2A(z0) = 0)
and kappa = (1 + 2A)/W_z, which is regular at z0 and on the axis interval from z0 to the next axis zero (or to
infinity). There q' = -kappa q and F' = -kappa F - 2 kappa q^2, so H = F - 2 q^2 + 2 q0 q satisfies H' = -kappa H with
H(z0) = 0. Hence H = 0:

    W_z(0, z) eta(0, z) = 2 q(0, z) (q(0, z) - q0)

on each axis branch leaving z0, up to the next axis zero. On a branch that reaches z = +-infinity (W_z ~ c z), with the
axis tails q ~ B(+-1) |z|^(-1/c) and eta ~ E(+-1) |z|^(-1 - 1/c), this gives +-c E(+-1) = -2 q0 B(+-1) at leading order,
so the far-field axis amplitudes of eta and q are tied to q0.

Identities (e) to (j) were derived by the independent referee; its symbolic script checks every local identity for
arbitrary phi, q, P (exact symbolic identities) and is retained as author_checks/identities_verify.py. The lead re-derived (e),
(f), (h), (i) and (j) by hand; (g) was checked through the symbolic script only. The integrated statements need tail
arguments beyond the local identities: the [verifier] proved the integrated forms of (f) for 1/2 < c_l < 3/5, (g), (h) and
(i) under the expansion stated at the start of this section, and (j) under uniform decay of q. Statements about finite
parts (FP: the constant left after removing the growing powers of R) assume a differentiated far-field expansion through
the order needed, with an integrable remainder after the subtractions.

(e) Bernoulli-Lyapunov function. H = |U|^2/2 + P + c y . U + c (2c - 1) |y|^2 / 2 satisfies
W . grad H - (2c - 1) |W|^2 = W . M for arbitrary U and P (exact symbolic check in author_checks/docrev_M_check.py), so
W . grad H = (2c - 1) |W|^2 for an exact profile. For c_l > 1/2, H then increases strictly along every non-stationary
orbit. At a zero of W_m the left side vanishes (H does not depend on theta), so U^theta = 0 there for c_l != 1/2
(AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Lemma 4). This is a pointwise test of the momentum equation including the pressure.

(f) Energy finite part. With e = |U|^2/2 and E(R) = int_{B_R} e, the energy balance div(W e + P U) = (5c - 2) e + U . M
(for div U = 0; exact symbolic check in author_checks/docrev_M_check.py) and the expansion U = R^{-alpha} F + R^{-2 alpha - 1} G + ...
give FP E = 0 for c_l != 3/5. For 1/2 < c_l < 3/5 the difference is absolutely integrable and, for an exact profile
([verifier] proof),

    int_{R^3} ( |U|^2 - R^{-2 alpha} |F(y/R)|^2 ) dy = 0.

For c_l > 3/5 the statement FP E = 0 is a formal expansion result: the growing first correction must also be subtracted,
and the remainder must be integrable after the subtractions. At c_l = 3/5 the finite part equals the constant flux
int_{S^2} (|F|^2/2 + Q) F_R dS, which is generally nonzero (formal expansion result under the same requirement).
(The R^{5 - 3/c} coefficient relation int F . G = (5 - 3/c) int (|F|^2/2 + Q) F_R is automatic from the local expansion.)

(g) Helicity finite part. For an exact profile, div(h W + (P - |U|^2/2) Omega) = (4c - 2) h with h = U . Omega, so for
1/2 < c_l < 3/4, int_{R^3} ( U . Omega - R^{-2 alpha - 1} F . K ) dy = 0, where R^{-alpha - 1} K is the vorticity tail
([verifier] proof; the remainder h - R^{-2 alpha - 1} F . K must be O(R^(-3 alpha - 2))). It is trivial in the reflection
class (E), in which phi is odd and q is even in z (so U^r and U^theta are even and U^z is odd): there the helicity density
is odd in z.

(h) Convergent virial. L = y . grad U + alpha U satisfies c L + (U . grad) U + grad P = 0 and div L = 0; L and
N = (U . grad) U are O(R^{-2 alpha - 1}) and square integrable, so c ||L||^2 = - int N . L. A nonzero profile needs
int N . L < 0.

(i) Five-dimensional eta norm. Multiplying the eta equation by eta and integrating over R^5 with
div_5 W_m = 5c + 2 v, v = U^r / r: (2 - 3c) ||eta||^2_{L^2(R^5)} = 2 int_{R^5} (v eta^2 + eta d_z(q^2)) for
1/2 < c_l < 2/3 (the boundary term is O(R^{1 - 2 alpha})). The right side must be positive.

(j) Swirl maximum. At any critical point of q with q != 0 (including the axis, where W_m . grad q = W_z q_z), the swirl
equation gives v = U^r / r = -1/2. If q is not identically zero and tends to zero uniformly at infinity (for example
under |DU| = O(R^(-alpha - 1))), |q| attains a nonzero maximum, where v = -1/2; consequently inf v <= -1/2.

(k) Single-source sign rule (referee, refining (c); [verifier] proof). Assume 1/2 < c_l < 3/4, a smooth exact profile with
the differentiated tails U = R^(-alpha) F + O(R^(-2 alpha - 1)), DU = O(R^(-alpha - 1)), P = O(R^(-2 alpha)) and
q = R^(-1/c) B(mu) + o(R^(-1/c)) uniformly in mu, including the poles, and assume that the only zero of W_m is an S1
source y0 with q(y0) = q0. Then every backward orbit converges to y0 (because of (e)), q has the strict sign of q0
everywhere, and B(mu) has the strict sign of q0 on [-1, 1], including the poles. The finite-space part (convergence and
the sign of q) does not use the tail hypotheses beyond the decay of U, which gives backward confinement; it uses the
uniqueness of the zero and (e). Without the uniform tail hypotheses, the sign of q at every finite point does not give a
nonzero limiting B. Under the tail hypotheses, odd B, a zero of B or a
sign change of B therefore requires further zeros of W_m.

(l) Moment form of the S1 conditions (lead; ORIGIN_AND_AXIS_REGULARITY.md section 6). Because phi has no harmonic
part on R^5, phi(0, z1) = (1/4) int int r^3 eta rho^(-3) dz dr and phi_z(0, z1) = (3/4) int int (z - z1) r^3 eta rho^(-5) dz dr,
rho^2 = r^2 + (z - z1)^2. At an S1 source these must equal -c z0/2 and 1/2. [verifier: constants and signs correct; the
second kernel is locally absolutely integrable] The second requires eta to be, in this weighted
sense, positive above the source and negative below.

(m) S1 curvature relation (verifier, lead-checked): if q_z(0, z0) = 0 at an S1 source,
4 (c - 1/2)(c + 1) q_rr + [(c + 1)^2 + q0^2] q_zz = 0, so the source is a saddle or a degenerate critical point of q.
A degenerate strict local maximum is possible at the level of formal jets (verifier example, ORIGIN_AND_AXIS_REGULARITY.md
section 6 (a)); whether the maximum of |q| can lie at the source is open.

Items (n) to (q) were derived by the independent referee, with SymPy (exact symbolic) and mpmath (floating-point) checks
retained in the accompanying artifacts; the lead re-derived (n), (o) and (p) by hand.

(n) Source balance with the contact term. With chi = z R^(-5) (5D dipole harmonic about the source at the origin),
d_z chi = PV (R^(-5) - 5 z^2 R^(-7)) + (|S^4|/5) delta_0 in the sense of distributions, |S^4| = 8 pi^2/3 (from
d_z chi = -(1/3) d_zz R^(-3) and the delta part of the second derivatives of the 5D Newton kernel). Multiplying the eta
equation by chi gives int eta [(1 - 2v) chi - U_m . grad chi] dV_5 = -PV int q^2 (R^(-5) - 5 z^2 R^(-7)) dV_5 - (8 pi^2/15) q0^2,
and phi_z(0, 0) = (3/(8 pi^2)) int eta chi dV_5, so the S1 condition reads int eta chi dV_5 = |S^4|/2. The referee showed by
explicit positive smooth test fields (with the S1 Hessian relation imposed) that neither the swirl term nor the meridional
quadratic term has a fixed sign, so this balance alone gives no obstruction.

(o) Equatorial structure in reflection-symmetric single-source profiles. In the reflection class (E), on z = 0, W_z = 0
and, if the origin is the only zero, W_r(r, 0) > 0 for r > 0. Then W_m . grad Gamma = (2c - 1) Gamma reads
W_r d_r Gamma = (2c - 1) Gamma on z = 0, so for c_l > 1/2 the sign of d_r(r^2 q(r, 0)) is the sign of q(r, 0). Choose the
orientation q0 > 0 (the swirl reversal U^theta -> -U^theta maps solutions to solutions); then q > 0 by the finite-space
part of (k), and d_r(r^2 q(r, 0)) > 0. In either orientation, where q(r, 0) != 0, d_r(r^2 q) = r q (2 + l) gives
l = r q_r / q > -2, and the equatorial swirl equation gives phi_z(r, 0) = (1 + c l)/(2 + l) and
W_r(r, 0) = (2c - 1) r/(2 + l) (exact symbolic check in author_checks/docrev_M_check.py).

(p) Axis reconstruction. With w(z) = W_z(0, z), the axis equations give w' = c + 2 phi_z and w q' = (2 phi_z - 1) q, hence
(w/q)' = (1 + c)/q exactly, and on an axis branch from a source z0 on which q != 0,

    W_z(0, z) = (1 + c) q(0, z) int_(z0)^z dzeta / q(0, zeta).

If the branch reaches z = +infinity with B != 0, and under the differentiated expansions q = B z^(-k) + D z^(-2k) + O(z^(-3k)),
phi = A z^(1 - k) + O(z^(1 - 2k)), k = 1/c (verifier: a remainder that does not exclude a z^(-k) term in phi is not enough), the
swirl equation gives D = -2 A B. Since 1 - 2k < -k, the stated remainder in phi excludes a z^(-k) term in w = c z + 2 phi,
while a nonzero finite part C_* of the integral would add (1 + c) B C_* z^(-k) to the reconstructed w (exact check for
c_l = 3/5, 2/3 and 7/10 in author_checks/docrev_M_check.py). Reconstruction therefore forces the finite part to vanish:
lim_(Z -> infinity) [ int_(z0)^Z dz / q(0, z) - Z^(k + 1)/(B (k + 1)) + (D/B^2) Z ] = 0 (finite-Z error O(Z^(1 - k))).

(q) eta norm at c_l = 2/3 (endpoint of (i)): int_(R^5) (v eta^2 + eta d_z(q^2)) dV_5 = (1/3) int_(S^4) E^2 dS, strictly positive
when the eta tail E is not identically zero (verifier: a nonzero velocity tail alone does not give this, since it may be
azimuthal). Weighted circulation at an S1 source with q0 != 0 located at the origin (reflection class): W = O(R) there, so (a)
holds for beta < 2p + 3, and beta -> 2p + 3 gives the source mean -p/(2p + 3).

## Revision history

- v1 states sections 1 to 5 (2026-10-28T18:32Z).
- v2 adds section 6 (2026-10-28T18:53Z).
- v3 adds (l) and (m) (2026-10-28T19:14Z).
- v4 applies [verifier] corrections to (a), (b), (l) and (m) (2026-10-28T19:27Z).
- v5 adds (n) to (q) (2026-10-28T19:38Z).
- v6 records the [independent referee] verdict on the expected-dimension count in section 4, adds the Corollary 11
  consequence to (c) and the [verifier] qualifications to (p) and (q) (2026-10-28T19:53Z).
- v7 states the transversality covector as psi(b) (2026-10-28T20:35Z).
- v8 qualifies section 3 for the C^2 class (2026-10-28T21:49Z).
- v9 replaces the status marker of section 6 by a per-item provenance rule (2026-10-29T09:36Z).
- v10 applies an independent mathematical review: corrects the divergence identity (section 1) and the translation
  statement (section 4); writes out the cylindrical component equations (section 2); adds notation, the stream gauge,
  finite-regularity examples and a regularity rule (section 3); restricts the non-Fredholm caveat to its realization and
  corrects the family caveat (section 4); states the denominators and collars of the residual audit (section 5); states
  the equations and tail hypotheses used by section 6 and qualifies (a), (b), (c), (f), (j), (k), (o) and (p); moves the
  revision history to this section (2026-10-29T10:50Z).
- v11 states that the tangent and singular-Jacobian consequences of section 4 hold for a regular differentiable family, after an independent review (2026-10-29T10:55Z).
