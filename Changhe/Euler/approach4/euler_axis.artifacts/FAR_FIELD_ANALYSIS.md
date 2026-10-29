# Far-field analysis (prompt sections 4 and 5)

Version v11, 2026-10-29T11:21Z

Conventions. "Symbolic" means an exact symbolic identity verified by the symbolic check scripts in the accompanying
artifacts (all passed). Provenance tags: [verifier] marks a proof or reproduction by the independent validation;
[independent referee] (also "referee" in quoted verdicts) marks a result derived or checked by a separately run review
process with its own code, whose verdicts on sections 5 and 6 are quoted in their headings; [lead] marks a derivation or
check by the authors. Sections 2 to 7 were also tested by the independent validation with its own symbolic and numerical
checks. Statements with a different status (floating-point comparison, formal expansion) say so where they occur.

c denotes c_l. alpha = (1 - c_l)/c_l, in (1/3, 1) for 1/2 < c_l < 3/4; 1 + alpha = 1/c_l.

## 1. Nonzero leading vorticity in the differentiated expansion class [verifier: analytic proof; lead-checked line by line]

Proposition (axisymmetry not needed). Let U, P be a Cartesian C^2 profile with div U = 0 and
(1 - c_l) U + (c_l y + U) . grad U + grad P = 0 for some c_l > 0. Assume U = o(R) uniformly, |DU| <= C R^(-1/c_l) for
R >= R0, and |curl U| = o(R^(-1/c_l)) uniformly. Then U is constant (zero if it decays).
Key steps: forward-bounded initial points have measure zero because the flow of W = c_l y + U expands volume at rate
3 c_l, so escaping initial points have full measure and are dense; along an escaping orbit log R(t) - c_l t converges, and
V(t) = e^t Omega(y(t)), Omega = curl U, solves V' = DU V with integrable coefficient, whose fundamental matrix has an
invertible limit (its determinant is identically 1, since tr DU = div U = 0), so V(t) -> 0 forces V = 0; hence Omega = 0
on a dense set and by continuity everywhere, and a divergence-free, curl-free field that is o(R) is constant.
Corollary. If a nontrivial decaying profile has a uniform differentiated expansion U = R^{-alpha} F + o(R^{-alpha}),
DU = D(R^{-alpha} F) + o(R^{-alpha - 1}), with F of class C^1 on the unit sphere, then its leading vorticity
curl(R^{-alpha} F), homogeneous of degree -1/c_l, is not identically zero; in particular F != 0 and the leading tail
R^{-alpha} F is rotational.
The hypotheses are uniform: pointwise limits of R^{1/c_l} Omega along rays do not supply the uniform smallness of the
vorticity remainder that the proof uses. The proposition does not show that profiles of the primary class have such an
expansion. Within the differentiated expansion class it makes the nonzero rotational tail necessary; it is not an
exclusion of that class.

## 2. Leading term (symbolic)

phi_0 = R^{-alpha} A(mu), q_0 = R^{-alpha - 1} B(mu), mu = cos(vartheta) (vartheta the polar angle, theta the azimuth):

    F_R = 2 mu A - (1 - mu^2) A',  F_vartheta = (alpha - 2) sin(vartheta) A,  F_theta = sin(vartheta) B,
    eta_0 = R^{-alpha - 2} E,  E = -[alpha (alpha - 3) A + (1 - mu^2) A'' - 4 mu A'].

U_0 = R^{-alpha} F satisfies (1 - c) U_0 + c y . grad U_0 = 0 identically, and div U_0 = 0 identically through the
potential representation, equivalently (2 - alpha) F_R + (1/sin) d_vartheta(sin F_vartheta) = 0.
The 5D zonal operator (1 - mu^2) d^2 - 4 mu d has eigenpairs (C_l^{3/2}, -l(l + 3)), so in Gegenbauer components
E_l = [l(l + 3) - alpha(alpha - 3)] A_l = (l + alpha)(l + 3 - alpha) A_l, which never vanishes for alpha in (1/3, 1):
A and E determine each other mode by mode.
Regularity at the poles: A and B smooth on [-1, 1] make R^{-alpha} F a smooth Cartesian field away from the origin.
Gamma_0 = R^{1 - alpha} sin^2(vartheta) B grows like R^{1 - alpha}; the circulation balance
(5c - 1) int_{B_R} Gamma dV = int_{dB_R} Gamma W . n dS (symbolic conservative form) is consistent with this growth
at leading order and gives no constraint on B. Never impose Gamma -> 0.

## 3. First nonlinear correction (symbolic and Cartesian check)

(U_0 . grad) U_0 = R^{-(2 alpha + 1)} N, with the nonlinear angular terms of the profile equation (d_vartheta = d/dvartheta)

    N_R = -alpha F_R^2 + F_vartheta d_vartheta F_R - F_vartheta^2 - F_theta^2,
    N_vartheta = (1 - alpha) F_R F_vartheta + F_vartheta d_vartheta F_vartheta - cot(vartheta) F_theta^2,
    N_theta = (1 - alpha) F_R F_theta + F_vartheta d_vartheta F_theta + cot(vartheta) F_vartheta F_theta.

These agree with a computation in cylindrical components as an exact symbolic identity for general A(mu), B(mu) and
alpha [lead, symbolic; author_checks/docrev_F_check.py], and with a Cartesian computation for concrete A, B at alpha = 3/7 at two
sample points to 1e-20 in 30-digit floating-point arithmetic (author_checks/sym_checks.py).
Expansion U = R^{-alpha} F + R^{-(2 alpha + 1)} G + ..., P = R^{-2 alpha} Q + ... . The linear operator acting on a
degree -(2 alpha + 1) term gives (1 - c) - c(2 alpha + 1) = -1, so the momentum balance at that order is
-G + N + (-2 alpha Q, d_vartheta Q, 0) = 0, i.e. G_R = N_R - 2 alpha Q, G_vartheta = N_vartheta + d_vartheta Q, G_theta = N_theta.
Incompressibility at that order, (1 - 2 alpha) G_R + (1/sin) d(sin G_vartheta) = 0, is identical to the pressure
equation -[2 alpha (2 alpha - 1) + Delta_{S^2}] Q = (1 - 2 alpha) N_R + (1/sin) d(sin N_vartheta) (symbolic, generic Q).

## 4. Resonances

Mode l of the pressure operator: -[2 alpha (2 alpha - 1) - l(l + 1)], zero for l = 2 alpha - 1.
- l = 0, alpha = 1/2 (c_l = 2/3): the l = 0 source is (1 - 2 alpha) <N_R>, so Q_0 = <N_R>/(2 alpha) with <.> the
  average over mu in [-1, 1] (symbolic, generic quartic A, B). At exact resonance the local mode equation is 0 = 0
  and leaves Q_0 undetermined; global incompressibility (zero flux of the degree -2 velocity term, <G_R> = 0)
  selects Q_0 = <N_R>, the continuous extension. No logarithm.
- l = 1, alpha = 1 (c_l = 1/2): the l = 1 source vanishes at alpha = 1 for all quartic A, B (symbolic); away from
  resonance Q_1 = 3 <mu N_R - F_R F_z>/(2 alpha + 1) [independent referee; Legendre normalization (2l+1)<P_l .>], with
  F_z = mu F_R - sin(vartheta) F_vartheta the axial Cartesian component of F; finite at c_l = 1/2, where again a global
  condition selects it.
  Critical endpoint [verifier: analytic proof; lead cross-check]: for a globally smooth decaying profile at c_l = 1/2 with
  U = R^-1 F + R^-3 H + O(R^(-3-eps)) (differentiated bounds through order three) and the Newton pressure, the l = 1
  pressure coefficient is fixed by the exact identity int_0^R s^3 f_1(s) ds = (3/2) int [R^3 mu N_R(R, mu) - R^2 U_R U_z] dmu
  (two applications of the divergence theorem, no inner boundary term because U is smooth at the origin; here
  f_l(R) = ((2l + 1)/2) int f(R, mu) P_l(mu) dmu are the Legendre coefficients of the pressure source f = div((U . grad) U),
  N_R(R, mu) is the radial component of (U . grad) U and U_z the axial Cartesian component of U), whose limit gives
  Q_1 = [(N_R)_1 - T]/3 with (N_R)_1 = (3/2) int mu N_R dmu (N_R now the leading angular coefficient) and
  T = (3/2) int F_R F_z dmu, that is Q_1 = <mu N_R - F_R F_z>, the continuous extension of the formula above. With
  Q_0 = <N_R>/2 (the l = 0 formula above at alpha = 1) and Q_l = f_l/(l(l+1) - 2) for l >= 2 (f_l now the Legendre
  coefficients of the leading source coefficient R^4 f), the order R^-3 momentum balance is H = G, with G given by the
  formulas of section 3 at alpha = 1: G_R = N_R - 2Q, G_vartheta = N_vartheta + d_vartheta Q = sin(vartheta) (N_v - Q'),
  G_theta = N_theta, where N_v = N_vartheta/sin(vartheta) and ' = d/dmu. This is a necessary coefficient condition for such
  profiles (not an existence statement). Cross-checks [lead, symbolic; author_checks/topic89_check.py]: the potential-to-velocity
  formulas (U_R = R^-k (2 mu A - (1 - mu^2) A'), U_vartheta = (k - 2) sin(vartheta) R^-k A for phi = R^-k A), the
  components of N, f_1 = 0, div(R^-3 G) = 0 for any Q_1 and int G_R dmu = 0 on a sample quartic A and cubic B; [lead, by
  hand]: the l = 1 moment identity and the Green formula. A piecewise
  numerical state with derivative jumps does not satisfy the smoothness hypothesis, so for such a state H - G measures the
  distance from a necessary smooth-profile target, not a pressure error.
  Piecewise fields [verifier: analytic proof; lead cross-check]: let U be C^2 on finitely many concentric spherical pieces, smooth at
  the origin, divergence-free in each open piece, with bounded one-sided derivatives and U = R^-1 F + O(R^-3) (differentiated)
  beyond the last interface. Let P_bulk be the decaying Newton pressure of the piecewise classical source f = tr((DU)^2) and
  P_stress that of the distribution div div(U tensor U), which adds at each interface radius a the layers [N].n delta(R - a)
  and div(J delta(R - a)) with J = [U (U.n)] (brackets: outer minus inner trace). Then beyond the last interface
  (P_stress - P_bulk)_0 = C0/R and (P_stress - P_bulk)_1 = C1/R^2 exactly, with C0 = sum_a a^2 ([N].n)_0 and
  C1 = (1/3) sum_a a^2 [a ([N].n)_1 - (J_R)_1 + D_1], D_1 = -(3/2) int (J_z - mu J_R) dmu, while the moment identities above
  (now in the distributional sense) give (P_stress)_0 = Q_0/R^2 + O(R^-4) and (P_stress)_1 = Q_1/R^2 + O(R^-4). Hence
  (P_bulk)_0 = -C0/R + Q_0/R^2 + O(R^-4) and (P_bulk)_1 = (Q_1 - C1)/R^2 + O(R^-4): interface defects of a piecewise
  approximation create a bulk-pressure monopole that eventually dominates the critical R^-2 pressure and shift the dipole.
  This is an identity for a fixed approximation, not an obstruction for smooth profiles. Rederived symbolically [lead;
  author_checks/topic90_check.py]: the surface Green contributions a^(l+1) [a ([N].n)_l - l (J_R)_l + D_l] / ((2l+1) R^(l+1)),
  the D_1 integration by parts, the l = 0 and l = 1 Green identities and the compact-support reference
  U = (b + d z)(-y, x, 0) in a ball (f = -2 (b + d z)^2, C0 = 2 b^2 a^3/3 + 2 d^2 a^5/15, C1 = 4 b d a^5/15, cancelled by
  the volume moments). For the exported c_l = 1/2 state, C0 = -1.57e-7 and C1 = -3.5e-9 against Q_0 = -5.43e-3 and
  Q_1 = -2.80e-3 [verifier, floating point, reporting gauge], so in the spherical mean P_0 the bulk monopole overtakes the
  R^-2 term only beyond R of order 3e4 (|Q_0/C0| is about 3.4e4); this compares the two terms of P_0, not the whole
  angular R^-2 pressure.
Both cancellations come from the double-divergence form f = d_i d_j (U_i U_j): on a homogeneous shell the monopole and
dipole moments of f are boundary integrals, which produce the factors (1 - 2 alpha) and (2 - 2 alpha).

## 5. Higher orders and the exponent set [independent referee: correct under a differentiated asymptotic expansion]

A homogeneous velocity term of degree -d with d != alpha satisfies (1 - c - c d) U_d + grad P_d = -(nonlinear forcing
of degree -d), so it is determined locally once the forcing and the pressure are known. Within a formal power-log
expansion, data not fixed by the local expansion appear only at d = alpha (A, B) and in the irrotational sector
a_l grad h_l, h_l = R^{-l-1} P_l(mu), d = l + 2, where the momentum balance (1 - c(l + 3)) a_l + p_l = 0 ties the
velocity multipole amplitude a_l to the global pressure multipole p_l R^{-l-1} P_l.
The irrotational amplitudes are not free parameters of a global solution: phi = Delta_5^{-1}(-eta) has no harmonic
part on R^5, so they are moments of eta over all space, and p_l is a moment of the pressure source. For l = 0, 1
the moment of f = d_i d_j(U_i U_j) against a harmonic polynomial of degree l is a pure boundary term (its second
derivatives vanish); for l >= 2 it contains the volume integral of (D^2 y^{(l)}) : (U x U), a genuine global quantity.
Degrees present: the chain d = alpha + k/c (k >= 0) from repeated products, the irrotational degrees l + 2 with
l >= 2 (the dipole is absent, section 6), and sums d1 + d2 + 1 of these, each possibly multiplied by powers of log R.
New logarithms can arise only where a pressure degree d1 + d2 equals l + 1 for some l >= 2 present in the source (the
l = 0, 1 coincidences are removable as in section 4), and only if the resonant source coefficient is nonzero; once
generated, a logarithm propagates through subsequent products to nonresonant degrees.
The first such coincidence in the range is 3 alpha + 1 = 3 (l = 2) at c_l = 3/5; it affects the pressure at
order R^{-3} log R. A nonzero example [verifier, exact rational algebra]: A = 0.42 - 0.23 mu - 0.04 mu^2,
B = 0.34 + 0.19 mu + 0.13 mu^2 give the quadrupole source f_2 = -125460142/437653125 and the log coefficient f_2/5, so
the pressure contains R^{-3} log R L(mu) with L = (f_2/5) P_2(mu); the logarithmic slope measured in an independent
full-space pressure computation differs from the exact coefficient by 8.2e-9 [verifier, floating point]. In the same example,
within the formal power-log hierarchy (assumed; its convergence is not proved), the logarithm propagates [independent referee, symbolic; verifier, proof with an exact symbolic check; reproduced by the lead by a separate route in cylindrical
components, author_checks/docrev_F_check.py]: the operator multiplier on degree -4 is 1 - 5c = -2, so the velocity contains
(1/2) log R grad(R^{-3} L); its products with the leading velocity give the pressure source monopole
-(63482831852/492359765625) R^(-20/3) log R, hence a nonzero pressure term R^(-14/3) log R at a nonresonant degree. No other product contributes at this degree: a
logarithmic source term of degree -20/3 is a product of a logarithmic velocity term of degree -d1 with d1 >= 4 (the first
pressure logarithm is at R^-3) and a velocity term of degree -d2 with d1 + d2 = 14/3, and only the leading velocity has
d2 <= 2/3 [lead].
At this pressure degree (velocity degree -4) the l = 2 irrotational relation (1 - c(l + 3)) a_l + p_l = 0 acquires
nonlinear forcing.
The degree rule is d_new = d1 + d2 + 1 for products; arbitrary sums are not generated (the referee notes that
unshifted sums would create spurious critical degrees, for example 3 alpha = 2 at alpha = 2/3).

Classification required by the prompt. It applies to profiles that have a differentiated formal power-log expansion of
the type above; existence, convergence and completeness of such an expansion for every profile of the primary class are
not proved.
- locally determined, once A, B and the global homogeneous multipole amplitudes are specified: G, Q and, recursively,
  the nonresonant coefficients of all chain and mixed terms, and the forced logarithmic coefficients at resonances;
- determined by the global pressure: the multipoles p_l (l >= 2) and through them h_l; at a resonance (for example l = 2
  at c_l = 3/5) the homogeneous coefficient of R^{-l-1} P_l that the local equations leave free is this global multipole;
- free, fixed by matching to the inner solution: A(mu), B(mu);
- inconsistent with Euler for 1/2 < c_l < 3/4 (for profiles with such an expansion): a nonzero irrotational dipole
  (phi ~ R^{-3} in the l = 0 Gegenbauer component), nonzero pressure monopole or dipole coefficients (except the
  c_l = 2/3 monopole, which equals the local Q_0 term), and any term, power or power times a power of log R, that the
  recursion above does not generate.

## 6. Global constraints [independent referee: correct for globally smooth profiles; an exterior-only solution can carry extra multipoles. Also proved by the verifier, see the paragraph after the second item]

- Pressure monopole and dipole: int_{B_R} f dy = int_{dB_R} n_i d_j(U_i U_j) dS and
  int_{B_R} y_k f dy = int_{dB_R} [y_k n_i d_j(U_i U_j) - n_j U_k U_j] dS exactly for smooth U. Their large-R expansions
  have an R^0 term only if some product U_i U_j has degree exactly -1 (monopole) or -2 (dipole). In the range this
  happens only for the monopole at c_l = 2/3 (2 alpha = 1) and for the dipole at the endpoint c_l = 3/4
  (2 alpha + 1/c = 2). Hence the R^{-1} and R^{-2} global pressure coefficients vanish for 1/2 < c_l < 3/4, c_l != 2/3.
  These statements concern the radial powers R^{-1}, R^{-2}; the angular monopole and dipole of R^{-2 alpha} Q need
  not vanish. At c_l = 3/4 the dipole is formally allowed: for A = 1, B = 0 the referee computed the pressure dipole
  coefficient 136/405 != 0, the coefficient of R^{-2} P_1(mu) in the pressure. The normalized source dipole moment
  I_1 = (3/2) int [mu H_R - F_z G_R - G_z F_R] dmu, with H the angular coefficient of the cross advection of R^{-alpha} F
  and R^{-2 alpha - 1} G and G_z the axial Cartesian component of G, has the constant value 136/135, and the pressure
  dipole component is (I_1/3) R^{-2} P_1(mu) [independent referee; verifier, exact rational; lead, separate route in
  cylindrical components, author_checks/docrev_F_check.py].
- Irrotational dipole: by the multipole relation with p_1 = 0 and 1 - 4c != 0, h_1 = 0. Independent route (symbolic
  identities, re-derived by the referee with signs confirmed; W_m = (c r + U^r, c z + U^z) is the meridional part of
  W = c y + U, and div_5 W_m = 5c + 2 U^r/r):
  in R^5, (1 + c) eta + W_m . grad eta - d_z(q^2) = div_5(W_m eta) + (1 - 4c) eta - 2 (U^r/r) eta - d_z(q^2),
  and (U^r/r) eta = d_z phi Delta_5 phi = div_5(d_z phi grad phi) - d_z(|grad phi|^2/2). So (1 - 4c) times the finite
  part of int eta dV_5 is a sum of finite parts of boundary integrals, which vanish when no boundary term has an
  R^0 component; a pair of degrees d_i, d_j contributes R^{2 - d_i - d_j}, so an R^0 term needs d_i + d_j = 2, the
  excluded critical product. Since int_{B_R^5} eta = -int_{dB_R^5} d_R phi, the finite part equals 3 |S^4| d_0,
  so d_0 = 0. With phi = d_0 R^{-3}, U = -d_0 grad(R^{-2} mu): this is exactly the irrotational dipole.
[verifier: analytic proof of the global multipole statements, read in full by the lead] Confirmed
under the differentiated hypothesis U = R^{-alpha} F + O(R^{-2 alpha - 1}) with one derivative, uniformly in angle, by
a different route: the exact identities P_0(R) = int_R^infinity n(s) ds (n the spherical mean of N . n) and
P_1(R) = R int_R^infinity I_1(s) s^{-4} ds, I_1 the dipole source moment, give the local coefficients
<N_R>/(2 alpha) and 3 <mu N_R - F_R F_z>/(2 alpha + 1) with no independent R^{-1} or R^{-2} term, and the degree -3
momentum balance (1 - 4c) U_3 = 0, U_3 the coefficient of the degree -3 velocity term, gives d_0 = 0. A leading-order
hypothesis o(R^{-alpha}) alone is not sufficient.
These are consequences of the exact equations; for numerical candidates they are sharp tests (far-field coefficient
checks of the pre-registered specification, section 6.3 and pressure criterion A7).
- Parity [lead, elementary proof; confirmed by the verifier with an independent proof and symbolic checks; the pressure
  part is also stated by the independent referee]. If
  phi is odd in z (the meridional field satisfies U_m(x, y, -z) = J U_m(x, y, z), J = diag(1, 1, -1)) and q is even or odd in z,
  then the irrotational dipole is excluded by parity at every c_l (phi = d_0 R^{-3} is even in z). The Newton pressure solves
  -Delta P = d_i d_j (U_i U_j); for axisymmetric fields the swirl enters this source only quadratically, so the source is even
  in z and the axial pressure dipole vanishes identically, including at the endpoint c_l = 3/4 where the boundary-term
  argument above allows it. The constraints d_0 = 0 and p_1 = 0 are therefore
  automatic in the reflection class and carry information only for fields without the symmetry (for example states whose
  axis source is off the symmetry plane).

## 7. Energy

Energy-flux identity (5c - 2) int_{B_R} |U|^2/2 = int_{dB_R} [(|U|^2/2 + P) U . n + c R |U|^2/2] dS (divergence form
symbolic). Leading tail: int_{B_R} |U|^2 = R^{5 - 2/c} int_{S^2} |F|^2 / (5 - 2/c) + lower order; both sides of the
identity then agree at leading order (c R^{5 - 2/c} ||F||^2 / 2). The kinetic energy diverges for c_l > 2/5; finite energy
is not imposed.

## 8. Consequences for representations [lead, formal expansion; the two examples are exact symbolic]

The exterior must factor R^{-alpha}. Write t = (R_0/R)^{1/c}. Besides the chain R^{-alpha} t^k (k >= 0) and the
irrotational multipoles d_m R^{-m-3} C_m^{3/2}(mu) (m = l - 1 >= 1), the expansion of section 5 contains the mixed
products and the logarithms generated by the recursion. Two examples [independent referee; reproduced by the lead by a
separate route, author_checks/docrev_F_check.py]: at c_l = 3/5 the potential of the logarithmic velocity term of section 5
contains kappa R^-4 log R C_1^{3/2}(mu) with kappa != 0, which in the variable t is a nonzero multiple of R^{-alpha} t^2 log t
plus a multiple of R^{-alpha} t^2; at c_l = 7/10 (alpha = 3/7) the products of the leading field with a nonzero l = 2
irrotational multipole (velocity degree -4) force a velocity and potential correction of degree -38/7 and a q correction of degree -45/7 (q = U^theta/r), each of relative power t^{7/2} against its leading factor.
A representation phi = R^{-alpha} f(t, mu) + sum_{m >= 1} d_m R^{-m-3} C_m^{3/2}(mu), q = R^{-alpha - 1} g(t, mu) with
f, g smooth holds only terms of the chain degrees and the isolated multipoles, so it represents a restricted truncation.
An exterior representation of the full expansion must allow the powers and logarithms generated by the recursion,
including the products with the global multipoles.
Powers of R^{-1} or R^{-2} alone miss G. Its size relative to the leading term is (||G||/||F||) R^{-1/c}
= C_G (R/a_eff)^{-1/c}, with L2(S^2) norms, a_eff = sup{R : max_{|y| = R} |Omega(y)| >= max |Omega|/2} the vorticity
half-maximum radius, and C_G = (||G||/||F||) a_eff^{-1/c} a dimensionless constant of the profile (invariant under the
dilations U_L(y) = L U(y/L)). For C_G = 1 and c_l = 0.6 the ratio is 1e-3 at R = 10^{1.8} a_eff, about 63 a_eff.

## Revision history

- v1, 2026-10-28T18:34Z, and v2, 2026-10-28T18:38Z: first versions; section 1 gave a heuristic argument.
- v3, 2026-10-28T18:49Z: records the verifier check of section 6.
- v4, 2026-10-28T19:57Z: replaces the heuristic of section 1 by the verifier's proof.
- v5, 2026-10-29T06:21Z: records in section 4 the verifier's proof of the critical dipole selection.
- v6, 2026-10-29T06:26Z: adds its extension to piecewise fields.
- v7, 2026-10-29T07:02Z: restricts the crossover radius of section 4 to the spherical mean.
- v8, 2026-10-29T10:48Z: v8 applies an independent mathematical review: section 1 states the proposition with its uniform
  hypotheses and the corollary, without the raywise argument; section 3 writes out the nonlinear angular formulas, now
  also checked as an exact symbolic identity; section 4 notation made self-contained (F_z, f_l, N_v, polar angle
  vartheta and azimuth theta); section 5 adds the propagation of logarithms to nonresonant degrees (c_l = 3/5 example)
  and restricts the classification to profiles with a formal power-log expansion; section 6 labels 136/405 as the
  pressure dipole coefficient and 136/135 as the source dipole moment; section 8 marks the smooth-in-t representation
  as a restricted truncation (examples at c_l = 3/5 and 7/10), corrects the first-correction radius from 180 a_eff to
  about 63 a_eff for unit amplitude ratio C_G and defines a_eff; dated and process references replaced by descriptions
  of the evidence; checks in author_checks/docrev_F_check.py.
- v9, 2026-10-29T10:55Z: section 8 gives the q correction at c_l = 7/10 its own degree, -45/7 (the velocity and potential correction has degree -38/7), after an independent check of the exponent bookkeeping.
- v11, 2026-10-29T11:21Z: the propagated logarithm at c_l = 3/5 is stated within the assumed formal power-log hierarchy (verifier cross-review 11:14Z).
- v10, 2026-10-29T11:12Z: section 5 tags the propagated logarithm at c_l = 3/5 with the independent proof and states that no other product contributes to the R^(-20/3) log R source coefficient.
