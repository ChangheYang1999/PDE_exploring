# Origin and axis regularity

Version v11, 2026-10-29T14:12Z

## Notation

c = c_l is the similarity exponent (1/2 < c_l < 3/4 in sections 5 and 6), delta = 1 + c, and alpha = (1 - c)/c is the
far-field decay exponent of U. Cylindrical coordinates (r, theta, z), s = r^2, x_h = (x, y). phi is the regular potential,
U^r = -r phi_z, U^z = 2 phi + 2 s phi_s, q = U^theta / r is the swirl variable, eta = Omega^theta / r = -Delta_5 phi, and
W_m = (c r + U^r, c z + U^z) is the meridional similarity field, with W_z(0, z) = c z + U^z(0, z) on the axis. Far-field
angular profiles: q ~ R^(-1/c) B(cos vartheta) and eta ~ R^(-1-1/c) E(cos vartheta), so B(+-1) and E(+-1) are the polar
values. a_eff is the vorticity half-maximum radius, used as the length unit of the audits.
Swirl-emitting zeros of W_m (AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Proposition 6): S1, an axis zero with q != 0 there, which
forces d_r U^r = -1/2 (for c_l > 1/2 a hyperbolic source with eigenvalues c - 1/2 radially and c + 1 axially); S2, a
hyperbolic axis source with q = 0 there; S3, an off-axis source (q = 0 there).
Search portraits: T2 has an off-axis S3 ring source on the plane z = 0, odd swirl, and an axis saddle at the origin with
radial inflow (radial eigenvalue -nu < 0, axial eigenvalue 3c + 2 nu); T3 has two S1 sources at z = +-z1, even swirl, and
an axis saddle at the origin with axial inflow, W_z(0, z) = -kappa z + O(z^2), where kappa > 0 is the axial contraction rate
(radial eigenvalue (3c + kappa)/2).
Reflection class (E): phi odd and q even in z, that is (U^r, U^theta, U^z)(r, -z) = (U^r, U^theta, -U^z)(r, z). The label
(E) is unrelated to the far-field profile E.

## 1. Cartesian smoothness in cylindrical variables

An axisymmetric vector field is C^infinity on R^3 if and only if
U^r = r a(s, z), U^theta = r b(s, z), U^z = C(s, z), with a, b, C smooth on {s >= 0}. The Cartesian components U_x, U_y
are not rotation invariant; the scalars x U_x + y U_y = r U^r, x U_y - y U_x = r U^theta and U_z are. A smooth function of
(x, y, z) invariant under rotations about the z axis is a smooth function of (s, z), and the first two scalars vanish at
s = 0, so Hadamard division by s gives r U^r = s a and r U^theta = s b with a, b smooth. Conversely U_x = x a - y b,
U_y = y a + x b, U_z = C are smooth. For finite regularity the correspondence is not exact: a Cartesian C^k field need not
have a, b, C of class C^k in (s, z) (the example q = r^3 chi below gives a Cartesian C^3 field with b = s^(3/2) chi, which
is not C^2 in s). The representations of the primary search are smooth in (s, z) on each of their pieces (origin ball,
spherical shells, exterior), which are joined by approximate interface matching, and the spline fields of the closed
single-source formulation are C^4 potentials only; smoothness in (s, z) is a sufficient and stronger choice for the
Cartesian C^2 class, not a characterization.

Equivalent reduced statement. If phi = Phi(s, z) and q = Q(s, z) are smooth, then
U^r / r = -Phi_z, U^z = 2 Phi + 2 s Phi_s, U^theta / r = Q are smooth in (s, z). Conversely, for a smooth divergence-free
axisymmetric field the Stokes stream function psi(s, z) solves psi_z = -s a, psi_s = C/2 (compatible exactly
because div U = 2a + 2 s a_s + C_z = 0), psi(0, z) is constant (set to 0), and Phi = psi / s is smooth by the
Hadamard lemma. So the class "phi, q smooth in (s, z)" is exactly the class of smooth axisymmetric
divergence-free fields. The potential is fixed by U only up to Phi -> Phi + C0/s (C0 constant), which changes neither
U^r / r nor U^z; the gauge psi(0, z) = 0 selects the unique representative that is smooth at the axis, and the
correspondence is stated in that gauge.

Finite regularity. The class of the prompt is a globally Cartesian C^2 (or smoother) velocity, which is strictly larger
than the smooth stratum above. A local statement of sections 3 to 6 that uses Taylor coefficients or derivatives of phi or
q in (s, z) beyond those that a Cartesian C^2 velocity provides is proved only under that additional smoothness, in
particular in the smooth stratum; where the C^2 class gives no classical derivative (for example eta_z on the axis), the
corresponding equation is used in characteristic integral form. Two examples, with phi = 0 and a smooth cutoff
chi(r^2 + z^2) equal to 1 near the origin, so that U = q (-y, x, 0) [exact symbolic checks, author_checks/docrev_O_check.py]:
q = r^3 chi gives U = chi (-y r^3, x r^3, 0), divergence-free and Cartesian C^3 but not C^4; q = r^(3/2) chi gives a
divergence-free field that is Cartesian C^2 but not C^3, with q_rr = (3/4) r^(-1/2) unbounded at the axis.
At an axis saddle that receives swirl the strain need not be quantized in the C^2 class [independent referee; verifier
standalone proof] (AXISYMMETRIC_OBSTRUCTION_AUDIT.md section 5g). At a T3 origin saddle the leading term
q ~ A_k(s) |z|^k, k = 1 + delta/kappa, is Cartesian C^2 for k = 2 and for every real k > 2, and exact local Euler solutions
exist for every k > 2 (local only: they do not decay and contain no sources); in the smooth stratum, under the hypotheses
of AXISYMMETRIC_OBSTRUCTION_AUDIT.md Proposition 10 (decaying axial data, simple axis zeros), k is an even integer at an
attracting axis zero between two S1 sources (Proposition 10 (iv)). At a T2 origin saddle the
leading term q ~ C s^j z, j = delta/(2 nu), is Cartesian C^2 for every j > 1/2 (a leading indicial calculation, not a
construction of a global T2 field), while the smooth T2 target has j = 1. For U^theta = r q the extra factor r matters,
so the right test is the Cartesian degree 2j + 1 of (-y, x)|x_h|^(2j) z, not the regularity of q in r or s. The S1 local
theory of sections 5 and 6 (formal jets, the curvature relation and the curvature ratio) is stated in the smooth stratum
and is not asserted for arbitrary Cartesian C^2 fields.

## 2. Regular forms of every operator

With d_r = 2 r d_s, r d_r = 2 s d_s:

- Delta_5 = 4 s d_ss + 8 d_s + d_zz, so eta = -(4 s Phi_ss + 8 Phi_s + Phi_zz).
- W_m . grad = 2 s (c - Phi_z) d_s + (c z + 2 Phi + 2 s Phi_s) d_z.
- R_q = Q + 2 s (c - Phi_z) Q_s + (c z + 2 Phi + 2 s Phi_s) Q_z - 2 Phi_z Q.
- R_eta = (1 + c) eta + W_m . grad eta - 2 Q Q_z.
- Primitive, with a = -Phi_z, b = Q, C = 2 Phi + 2 s Phi_s:
  M_r / r = (1 - c) a + (c + a)(a + 2 s a_s) + (c z + C) a_z - b^2 + 2 P_s,
  M_theta / r = (1 - c) b + (c + a)(b + 2 s b_s) + (c z + C) b_z + a b  ( = R_q ),
  M_z = (1 - c) C + 2 s (c + a) C_s + (c z + C) C_z + P_z.
  (P is a smooth function of (s, z) for a smooth axisymmetric pressure.)

No expression divides by r. Implementations must use these forms, or Cartesian evaluation, near the axis.

## 3. Values on the axis and at the origin

- On the axis: R_q(0, z) = (1 + 2A(z)) q + W_z q_z with A(z) = -Phi_z(0, z) = d_r U^r(0, z), W_z = c z + 2 Phi(0, z).
  At an axis zero of W_z this gives q (1 + 2A) = 0 (AXISYMMETRIC_OBSTRUCTION_AUDIT.md, Lemma 4).
- U(0) = (0, 0, 2 Phi(0, 0)); U(0) = 0 is equivalent to Phi(0, 0) = 0 and is not imposed.
- DU(0) = [[A0, -q0, 0], [q0, A0, 0], [0, 0, -2 A0]] with A0 = -Phi_z(0, 0), q0 = Q(0, 0): an axial strain with rate
  -2 A0 along z plus solid rotation with angular velocity q0. Omega(0) = (0, 0, 2 q0). DU(0) and q0 are dilation
  invariant.

## 4. Required audits (pre-registered specification 6.5 and criterion A8)

1. Representation regular by construction (functions of (s, z), or of Cartesian coordinates); the basis definition of
   each reported state must state how. Odd powers of r in a radial basis make the field nonsmooth on the axis: a term
   r^n g(z) with n odd and g not identically zero gives, in q, a swirl velocity of Cartesian class C^n but not C^(n+1),
   and, in phi, U^z = (n + 2) r^n g(z) of class C^(n-1) but not C^n (n = 1: an |x|-type kink). Admissibility in the C^2
   class is therefore decided on the reconstructed Cartesian velocity, not by the parity of the radial powers (q = r^3 chi
   of section 1 is Cartesian C^3). The representations used here contain no odd powers of r. For piecewise
   representations, smoothness of each piece does not imply smoothness across the interfaces; the interface jumps of
   section 6.5 of the pre-registered specification are measured separately. [lead; exact symbolic checks of the cases n = 1, 3 in author_checks/docrev_O_check.py]
2. Cartesian evaluation across the axis on the line y = 0, x in [-h, h], with finite-difference derivatives in
   x, y, z at several step sizes (h = 1e-2 to 1e-5 a_eff): smooth U_x, U_y, U_z with converging derivatives.
3. Taylor coefficients of a, b, C, Q, eta, Phi at the origin and along the axis (on a grid of z values that includes
   every axis zero), through second order in s and in z, that is through s^2 and (z - z0)^2 about each expansion point
   (0, z0) (pre-registered specification, section 6.5); residuals R_q, R_eta, M_r / r, M_z and their s-derivatives at s = 0. These coefficients exist for
   representations smooth in (s, z), such as each piece of the primary-search representation; for a merely Cartesian C^2 field some of them need not exist
   (section 1).
4. Axis-collar residual ratios (sin(vartheta) < 0.05, no sin weight) reported per shell beside the 3D-weighted ones.
5. Hidden singularities: max |Omega| and max |D^2 U| must stay bounded under refinement (A8: change at most 1 percent
   between the two finest levels for label A).

## 5. Local theory at swirl-emitting axis sources

Source: independent referee derivation with exact-arithmetic checks (retained as author_checks/s1_jet_check.py and its
output); the lead re-checked the c_l = 3/5 sample below with separately written cylindrical residuals
(author_checks/s1_jet_independent.py: R_q vanishes through weighted order 5 and R_eta through order 4). All Taylor
statements are formal (identities of series); convergence is not claimed. They are made in the smooth stratum (section 1).

Weights: s = r^2 has weight 2, x = z - z0 weight 1; delta = 1 + c.

S1 (A = -1/2, q0 = K != 0). phi = -c z0/2 + x/2 + sum_{d >= 2} P_d, q = K + sum_{n >= 1} Q_n. At each weight d >= 2 the
equations for (P_d, Q_{d-1}) are triangular with strictly positive divisors (j(2c - 1) + (k + 1) delta for the phi
coefficients, j(2c - 1) + k delta for q), so the formal solution exists and is unique once one coefficient per weight
is chosen. The free local data are c, z0, K and the axis Taylor coefficients h_d of phi(0, z0 + x) = -c z0/2 + x/2 +
sum h_d x^d. They are fixed by the global elliptic problem, not by the local analysis, and the local homogeneous
freedom is not Delta_5-harmonic when K != 0. First terms:

    P_2 = h_2 [x^2 - (1/4 + K^2/delta^2) s],   Q_1 = (4 K h_2/delta) x,   eta(0, z0) = 8 K^2 h_2 / delta^2.

The S1 profile recurrence has no exceptional c_l in (1/2, 3/4): no compatibility conditions and no forced logarithms.
The values c_l = (n + 1)/(2n - 1), n >= 4 (5/7, 2/3, 7/11, 8/13, 3/5, ...), where the fast eigenvalue is an integer
multiple of the slow one in (s, x), obstruct only smooth linearization of the meridional field, not smoothness of
the profile.

Given W_m, the swirl and eta are unique among fields continuous at the source (boundedness alone allows orbit-dependent,
discontinuous solutions) [independent referee qualification]:
q(y) = K exp( int_{-infinity}^0 [2 phi_z(Phi_t y) - 1] dt ) and eta(y) = int_{-infinity}^0 e^{delta t} d_z(q^2)(Phi_t y) dt,
with Phi_t the meridional flow, on the basin of the source. The dimension of the global solution set is not known.
Conditional count [lead heuristic; independent referee: the right conditional generic count]. The profile map is
dilation-equivariant, so the dilation orbit of a solution costs one unknown; with the unknowns (phi, K, c_l) and the
equations (fixed point, resonance phi_z(0, z0) = 1/2), the quotient by dilations is square only with c_l free, and the
generic expectation is an isolated pair (c_l, K) modulo dilation. This is valid if the linearization is Fredholm of index 0
with kernel spanned by the dilation tangent and a transversality condition holds; none of this is proved. In the direct
realizations that use the same critical decay weight in the domain and in the residual space (so that the bounded bump
sequences on logarithmic annuli of MATHEMATICAL_FORMULATION.md section 4 belong to the domain), the transport part is not
Fredholm; other asymptotic realizations (for example a slightly weaker weight, or spaces that separate the leading angular
tail) are not excluded and need their own analysis. The local transport analysis at an S1 source does
support exactly one amplitude and one compatibility condition: with h = exp(-int_(-inf)^0 beta(Phi_t y) dt) and
beta = 1 - 2 phi_z = 1 + 2v, v = U^r / r, the equation (W_m . grad + beta) f = g has a smooth local solution iff
g(source) = 0, and then f = h [C + int_(-inf)^0 (g/h)(Phi_t y) dt].
Axis saddles between S1 sources impose further matching (AXISYMMETRIC_OBSTRUCTION_AUDIT.md Proposition 10, a theorem in
the smooth stratum; its scope in the Cartesian C^2 class is stated in section 5b of that audit).

Sample S1 jet at c_l = 3/5 (K = 1, h_2 = h_3 = 0, h_4 = eps, h_5 = tau free), usable as a local seed:

    phi = -3 z0/10 + x/2 + eps (x^4 - (169/96) s x^2 + (30589/93312) s^2)
          + tau (x^5 - (1405/512) s x^3 + (546545/591872) s^2 x) + O_w(6),
    q   = 1 + eps ((5/3) x^3 - (845/216) s x)
          + tau ((25/16) x^4 - (21075/4352) s x^2 + (2732725/591872) s^2) + O_w(5).

S2 with j = 1 (A = -(1 + 2c)/4, q = K s + ...): all axis Taylor coefficients of q vanish (a nonzero axis solution
behaves like |x|^{(2c - 1)/(4c + 1)} and is not C^1), so q = s V with V smooth, V(0, z0) = K. The leading phi jet is
Delta_5-harmonic up to weight 5, and eta starts at weight 4: eta_4 = 16 K^2 h_2 s^2 / (3c (2c + 1/2)).

Axis relation (MATHEMATICAL_FORMULATION.md section 6 (d)) [lead; verifier standalone proof]: W_z eta = 2 q (q - K) on
each axis branch issuing from an S1 source on which W_z(0, z) != 0 away from the source and q != 0. If that branch reaches
z = +infinity (respectively z = -infinity) and phi(0, z) = O(|z|^(-alpha)), phi_z(0, z) = O(|z|^(-alpha - 1)) on it, then
q(0, z) ~ C_+ |z|^(-1/c) (respectively C_- |z|^(-1/c)) with C_+-/K > 0, and eta(0, z) ~ -+(2K/c) C_+- |z|^(-1 - 1/c) as
z -> +-infinity; with the differentiated far-field expansion, C_+- = B(+-1). No pole asymptotics are asserted for a branch
that ends at another axis zero (q tends to 0 there, section 6 (b)).

## 6. Structure forced at an S1 source

(a) Curvature relation [verifier derivation; lead re-derivation with symbolic c and q0 from the weight-2 q and weight-3
phi jets, an exact symbolic identity, author_checks/s1_curvature_check.py]. At an S1 source with q0 != 0 and q_z(0, z0) = 0
(h_2 = 0, automatic in reflection class (E)), assuming smoothness sufficient for the Taylor coefficients below (for example
the smooth stratum; Cartesian C^2 alone does not provide it, section 1),

    4 (c - 1/2)(c + 1) q_rr + [(c + 1)^2 + q0^2] q_zz = 0.

With h_3 the axis coefficient of phi, q_zz = 6 q0 h_3/(c + 1) and q_rr = -3 q0 h_3 [(c + 1)^2 + q0^2]/((2c - 1)(c + 1)^2).
Both coefficients of the displayed linear relation, 4 (c - 1/2)(c + 1) and (c + 1)^2 + q0^2, are positive for c_l > 1/2, so the quadratic part of q at the source is indefinite or zero: an S1
source is never a nondegenerate extremum of q. It can still be a degenerate extremum: when h_3 = 0 the quadratic part of q
vanishes, and in the c_l = 3/5 sample of section 5 with eps = 0 the quartic correction tau (A4 x^4 + B4 s x^2 + C4 s^2),
A4 = 25/16, B4 = -21075/4352, C4 = 2732725/591872, has B4^2 - 4 A4 C4 = -102389375/18939904 < 0 and A4, C4 > 0, so for
tau < 0 the formal jet has a strict local maximum of q at the source with zero Hessian [verifier; exact rational
computation on the formal jet; no realization by a profile is claimed]. Whether the global maximum of |q| can sit at an S1
source is therefore OPEN; the curvature relation alone does not place it elsewhere.
The swirl-maximum identity (MATHEMATICAL_FORMULATION.md section 6 (j)) is consistent with either case, since U^r/r = -1/2
holds at an S1 source.

(b) Axis growth criterion (exact, from the axis restriction of R_q). On an axis interval without zeros of W_z,
d/dz log|q(0, z)| = -(1 - 2 phi_z(0, z))/W_z(0, z). Stated along the forward W_m orbit, that is outward along each branch
leaving the source (the sign of d/dz reverses on the lower branch, where W_z < 0), |q| grows exactly where
phi_z(0, z) > 1/2 (axial stretching stronger than at the source), and an axial maximum of |q| is again a point where
phi_z = 1/2. By the axis relation W_z eta = 2 q (q - q0), eta(0, z) has the sign of (z - z0) where |q| > |q0| (same sign
as q0) and the opposite sign where |q| < |q0|. If the branch reaches infinity with the axial decay of the axis relation in
section 5, |q| < |q0| far out on it; if in addition the far-field expansion of q and eta holds with differentiated
remainders, this gives c E(+1) = -2 q0 B(+1) (upper branch) and c E(-1) = 2 q0 B(-1) (lower branch) [verifier: independent
proof of the pole relations under these two hypotheses]. If instead the branch ends at another axis zero, q tends to 0
there and eta again has the sign opposite to (z - z0) near it.

(c) Moment form of the S1 conditions [lead; the five-dimensional Green representation and the absolute convergence of both
integrals are proved in the verifier's standalone proof of the axis moments; the lead's check author_checks/s1_moment_check.py is
a floating-point comparison on one test field at three axis points, with the integration truncated at rho = 1e4, agreeing
to the ten printed decimals]. phi = Delta_5^(-1)(-eta) has no harmonic part, the Newton kernel of -Delta_5 on R^5 is
|y|^(-3)/(8 pi^2) and dV_5 = 2 pi^2 r^3 dr dz, so for any axis point z1, with rho^2 = r^2 + (z - z1)^2,

    phi(0, z1)   = (1/4) int_0^inf int_R r^3 eta(r, z) rho^(-3) dz dr,
    phi_z(0, z1) = (3/4) int_0^inf int_R (z - z1) r^3 eta(r, z) rho^(-5) dz dr.

(The kernel of the second integral is O(rho^(-1)) in the (r, z) half-plane, hence locally absolutely integrable, and no
principal value is needed [verifier].)

Both integrals converge for eta = O(R^(-alpha - 2)). The S1 conditions W_z(0, z0) = 0 and phi_z(0, z0) = 1/2 are therefore

    int int r^3 eta rho^(-3) = -2 c z0,      int int (z - z0) r^3 eta rho^(-5) = 2/3.

The second identity says that the first moment of eta about the source, with weight r^3 rho^(-5), is positive (loosely:
eta is, in this weighted sense, positive above the source and negative below). By the characteristic formula
eta(y) = int_(-inf)^0 e^((1 + c) t) d_z(q^2)(Phi_t y) dt, a point with eta > 0 needs d_z(q^2) > 0 somewhere on its
backward orbit, and a point with eta < 0 needs d_z(q^2) < 0 somewhere on it. The identities do not locate these
contributions: the moment integrates the whole half-plane and eta samples entire backward orbits, so nothing here shows
that a neighbourhood of the axis or of the source dominates the moment. Exact statements: (a), (b) and the two moment
identities. A possible qualitative picture, not a theorem: stronger stretching and stronger swirl in the regions that
contribute positively to the moment, together with the sign reversal of eta farther out along the axis that (b) proves.
Proved restrictions on the shape of q: (a) excludes a nondegenerate local extremum of q at the source, in particular a
negative-definite Hessian, so a swirl blob q = q0 (1 + R^2/L^2)^(-p), p > 0, R^2 = r^2 + (z - z0)^2, centred on the
source violates (a) for every q0 != 0; (a) does not exclude a degenerate maximum (the quartic example in (a)); and in
reflection class (E) with an S1 source at the origin, d_z(q^2) > 0 somewhere in z > 0 (see (e)). The revised seeds in the
accompanying artifacts (seeds/s1_sym_v2.py) satisfy (a) at the source, phi_z(0, z) > 1/2 next to the source and the pole
sign c E(+1) < 0 for q0 > 0 and B(+1) > 0; a numerical grid scan of the half-plane (finite, not a certificate) found no
other zero of W_m for each c_l in {0.505, 0.525, 0.56, 0.60, 0.64, 0.68, 0.72, 0.74}.

(d) Curvature ratio of q at the source [independent referee; immediate from (a)]. This is the ratio of the two nonzero
quadratic curvatures of q at a saddle-type S1 source, not a measured core width, and it is undefined when the Hessian
of q vanishes [verifier qualification]. At a smooth S1 source with q_z(0, z0) = 0 (h_2 = 0) and h_3 != 0, put
l_r^(-2) = |q_rr|/|q0| and l_z^(-2) = |q_zz|/|q0|; then l_r / l_z = sqrt(4 (c - 1/2)(c + 1)/((c + 1)^2 + q0^2)). The
ratio is small when c_l is close to 1/2 or q0 is large. It decreases in |q0|, so at c_l = 0.505 it is below its q0 -> 0
limit sqrt(4 (0.005)/1.505) = 0.115278... for every q0 != 0, and at c_l = 0.6 with q0 = 1 it is 0.4240 (exact values
2/sqrt(301) and 4/sqrt(89), author_checks/docrev_O_check.py). Representations must resolve this radial scale near the axis.

(e) No regular small-swirl limit [independent referee; verifier standalone proof] (AXISYMMETRIC_OBSTRUCTION_AUDIT.md
Proposition 9). There is no sequence of smooth exact profiles (phi_n, q_n, c_n) with S1 sources at the origin such that
c_n -> c_* > 0, phi_n -> phi_* in C^3 on compact sets in the regular meridional variables (with smooth axis extensions),
q_n -> 0 in C^1 on compact sets, and |U_n(y)| <= C (1 + |y|)^(-a) for fixed C, a > 0 and all n, y. This is a compactness
obstruction: it does not exclude a small source amplitude of an individual profile, or a sequence that loses these
controls. Separately, a nonzero Cartesian C^2 exact profile in reflection class (E), uniformly sublinear and decaying so
that phi = Delta_5^(-1)(-eta) has no harmonic part, with q(0) != 0 (so that the origin is an S1 source), has
d_z(q^2) > 0 somewhere in z > 0 (Proposition 8 of that audit, contrapositive form).

## Revision history

- v1 (2026-10-28T18:33Z): sections 1 to 4.
- v2 (2026-10-28T19:05Z): section 5, local theory at swirl-emitting axis sources; it included a one-parameter solution
  set in (K, c_l), later replaced by the conditional count of section 5.
- v3 (2026-10-28T19:14Z): section 6, structure forced at an S1 source; it stated that the maximum of |q| lies away from
  an S1 source and wrote the derivative moment in (c) as a principal value.
- v4 (2026-10-28T19:27Z): corrections to section 6 from the verifier: the degenerate-extremum caveat in (a), which
  withdraws the v3 statement on the maximum of |q| (it does not follow), the branch orientation in (b), and no principal
  value in (c).
- v5 (2026-10-28T19:38Z): adds 6 (d) and 6 (e).
- v6 (2026-10-28T19:53Z): records the independent referee's verdict on the conditional count of section 5.
- v7 (2026-10-28T20:26Z): states the uniqueness of q at a source under continuity.
- v8 (2026-10-28T21:49Z): adds the finite-regularity remark in section 1.
- v9 (2026-10-29T10:43Z): v9 applies an independent mathematical review: a notation section (S1 to S3, T2, T3,
  reflection class (E), mu, nu, alpha, a_eff, B, E); in section 1 the rotation-invariant scalars in the smoothness
  argument, the stream gauge, the finite-regularity examples q = r^3 chi and q = r^(3/2) chi, the scope of the T3 and T2
  statements, and the restriction of the S1 theory to the smooth stratum; in section 4 the odd-power statement replaced
  by a test on the Cartesian velocity, an interface remark, and the Taylor audit set to second order in s and z along
  the axis as in section 6.5 of the pre-registered specification; in section 5 the branch and decay hypotheses of the pole asymptotics and the realization
  qualification of the non-Fredholm statement; in section 6 the smoothness hypothesis of the curvature relation, the
  differentiated-tail hypothesis of the pole relations, the moment discussion without the unsupported necessity claim,
  the hypothesis h_2 = 0 and the bound 0.115278 for the curvature ratio, and the full hypotheses of Propositions 8 and
  9; dated references replaced by status descriptions and the version history moved to this section (checks in
  author_checks/docrev_O_check.py).
- v10 (2026-10-29T10:55Z): section 6 (a) names the two positive coefficients of the linear curvature relation explicitly, after an independent review.
- v11 (2026-10-29T14:12Z): the axial contraction rate of the T3 saddle is written kappa (as in the final report, where mu is the
  cosine of the polar angle); section 1 states that the primary-search representations are smooth in (s, z) on each
  piece and that the spline fields of the closed formulation are C^4 potentials only, and section 4 item 3 is worded
  accordingly.
