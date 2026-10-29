# Pre-registered specification: formulation, residuals, gauges and acceptance thresholds

Version v0, registered 2026-10-28T18:24Z (campaign hour 0.41), before any candidate exists or is ranked.
Owner: the report author. The primary numerical search and the independent verifier work to this document. Section 9 (thresholds) is frozen from the
registration time. Later edits may add diagnostics or clarify wording; they may never relax a threshold.
Every edit is logged in section 12 with its time and reason.

Status of the derivations quoted here: items marked [audit pending] are lead derivations still being
checked (sympy and an independent external referee, a second model). Items marked [checked] passed at least one independent check.

## 1. Equations and notation

c = c_l, alpha = (1 - c)/c. For 1/2 < c_l < 3/4, 1/3 < alpha < 1.

Profile equations (y in R^3):

    (1 - c) U + (c y + U) . grad U + grad P = 0,      div U = 0.

Cylindrical (r, theta, z); spherical R = sqrt(r^2 + z^2), r = R sin(vartheta), z = R cos(vartheta),
mu = cos(vartheta). s = r^2.

Reduced variables (prompt section 2):

    Gamma = r U^theta,  q = U^theta / r,  eta = Omega^theta / r,  Omega = curl U,
    -Delta_5 phi = eta,  Delta_5 = d_rr + (3/r) d_r + d_zz,
    U^r = -r d_z phi,  U^z = 2 phi + r d_r phi,  U^theta = r q,
    W = c y + U,  W_m = (c r + U^r, c z + U^z).

Reduced residuals (these exact sign conventions are used by everyone):

    R_q   = q + W_m . grad_{r,z} q + 2 (U^r / r) q
    R_eta = (1 + c) eta + W_m . grad_{r,z} eta - d_z(q^2)
    R_ell = -Delta_5 phi - eta          (formulation A only; identically zero in formulation B)
    R_Gam = (1 - 2c) Gamma + W_m . grad Gamma = r^2 R_q   (diagnostic only; algebraic identity [checked by hand])

Primitive residuals (Cartesian vector, evaluated from the reconstructed Cartesian field):

    R_M   = (1 - c) U + (c y + U) . grad U + grad P,     P = full-space pressure of section 4,
    R_div = div U.

The components R_M^r, R_M^theta, R_M^z are reported separately, with the cylindrical forms of prompt section 1.
Note U^r/r = -d_z phi and Gamma/r^2 = q are regular limits; never divide by r numerically near the axis.

Derived identities used as checks (energy flux and div(r W_m): sympy-checked 18:34Z; the others by hand):

- Vorticity: Omega + W . grad Omega - (Omega . grad) U = 0. At any critical point of |Omega|^2, and in particular
  at a nonzero global maximum of |Omega|, Omega . sym(DU) Omega = |Omega|^2.
- Energy flux on balls B_R: (5c - 2) int_{B_R} |U|^2/2 dy = int_{dB_R} [(|U|^2/2 + P) U.n + c R |U|^2/2] dS.
- Dilation: U_L(y) = L U(y/L), P_L(y) = L^2 P(y/L); phi_L = L phi(y/L), q_L = q(y/L), eta_L = L^{-1} eta(y/L).
- div_3D W = 3c. Hence div_{r,z}(r W_m) = 3 c r > 0 for r > 0 (Dulac function r), see section 7.

## 2. Function class and regularity

- phi and q are smooth (at least C^3 for residual evaluation) functions of (s, z) = (r^2, z) on the closed
  half-plane s >= 0. This is equivalent to the Cartesian regularity U^r = r A(s,z), U^theta = r B(s,z), U^z = C(s,z).
  A representation that is not of this form must prove regularity by the Taylor audit of section 6.5.
- Do not impose U(0) = 0, U^theta = 0, U^z = 0, z-parity, finite energy, exponential decay, compact support,
  or any boundary condition on a finite sphere. Optional parity-restricted runs are separate experiments and
  must be labelled as such.
- Uniform decay: |U| -> 0 as R -> infinity. Primary class: U = R^{-alpha} F(vartheta) + o(R^{-alpha}) with F not
  identically zero.

## 3. Far field (primary class)

3.1 Leading term [sympy-checked 18:27Z; independent referee: correct].
phi_0 = R^{-alpha} A(mu), q_0 = R^{-alpha-1} B(mu), eta_0 = R^{-alpha-2} E(mu), with

    F_R = 2 mu A - (1 - mu^2) A',  F_vartheta = (alpha - 2) sin(vartheta) A,  F_theta = sin(vartheta) B,
    E = -[alpha (alpha - 3) A + (1 - mu^2) A'' - 4 mu A'].

The 5D zonal operator (1 - mu^2) d^2 - 4 mu d has eigenfunctions the Gegenbauer polynomials C_l^{3/2}(mu) with
eigenvalues -l(l+3). A and B are free inner-matching data; they are never frozen.
Gamma_0 = R^{1-alpha} sin^2(vartheta) B grows: never impose Gamma -> 0.

3.2 Gauge (section 5): int_{S^2} |F|^2 dS = 1.

3.3 Exponent set [referee: correct under a differentiated asymptotic expansion, with the nonlinear degree rule
d_new = d1 + d2 + 1, not arbitrary sums]. Away from coincidences the velocity expansion contains homogeneous terms of
degree -d with d in the set generated from {alpha} (free data) and {l + 2 : l >= 1} (irrotational multipoles
grad(R^{-l-1} P_l)) under (d1, d2) -> d1 + d2 + 1. The leading chain is d = alpha + k/c (k = 0, 1, 2, ...), that is
R^{-alpha} times powers of R^{-1/c}; the first correction G has d = 2 alpha + 1 = alpha + 1/c. The irrotational
dipole (d = 3) vanishes for 1/2 < c_l < 3/4 (3.5), so the first irrotational term is the quadrupole d = 4.
Logarithms can appear where a pressure term of degree d1 + d2 hits a harmonic degree l + 1 with l >= 2
(for example 3 alpha + 1 = 3 at c_l = 3/5, l = 2; the verifier computed a nonzero example); these occur at high
order. At the same coincidence the irrotational relation of 3.5 for l = 2 acquires nonlinear forcing. Representations must factor
R^{-alpha} and must be able to express the R^{-alpha - k/c} chain (for example R^{-alpha} f(x, mu) with
x = (R_0/R)^{1/c}, or explicit factored correction families). A representation whose exterior is
R^{-alpha} times a smooth function of R^{-1} or R^{-2} only cannot represent G and must not be used for
acceptance. BASIS.md must list exactly which exponents the representation can express.

3.4 First nonlinear correction (prompt section 5) [checked by hand: N formulas, pressure operator, div G].
Resonances: the pressure operator -[2 alpha (2 alpha - 1) - l(l+1)] vanishes at l = 2 alpha - 1, i.e. l = 0 at
c_l = 2/3 and l = 1 at c_l = 1/2. Both are removable because the source f = d_i d_j (U_i U_j) is a double
divergence: on a homogeneous shell the monopole of the degree -(2 alpha + 2) source carries the factor (1 - 2 alpha)
and the dipole the factor (2 - 2 alpha) [sympy-checked; referee: correct]. Away from resonance
Q_0 = <N_R>/(2 alpha) and Q_1 = 3 <mu N_R - F_R F_z>/(2 alpha + 1) (Legendre normalization (2l+1)<P_l .>,
<.> the mu-average on [-1, 1]). At exact resonance the local mode equation is 0 = 0; global incompressibility
(zero flux of the degree -2 velocity term) selects Q_0 = <N_R> at c_l = 2/3, which equals the continuous extension. No logarithm may be fitted at c_l = 2/3 or c_l = 1/2 unless the solvability computation shows it.

3.5 Global multipoles [referee: correct for a globally smooth profile with U = R^{-alpha} F + O(R^{-2 alpha - 1})
under the needed differentiations; an exterior-only solution may carry extra multipoles].
- Pressure: int_{B_R} f dy and int_{B_R} y f dy are surface integrals; their expansions contain no R^0 term
  for 1/2 < c_l < 3/4 with c_l != 2/3, so the global pressure monopole (R^{-1}) and dipole (R^{-2}) coefficients vanish.
  At c_l = 2/3 the R^{-1} pressure term coincides with the local Q_0 term and is fixed by it. These statements
  concern the radial powers R^{-1}, R^{-2}, not the angular monopole or dipole of R^{-2 alpha} Q. At the endpoint
  c_l = 3/4 a nonzero dipole is formally allowed (referee example A = 1, B = 0: boundary coefficient 136/405).
- Velocity: an irrotational multipole grad h_l, h_l = R^{-l-1} P_l(mu), has (1 - c(l + 3)) grad h_l + grad p_l = 0,
  where p_l is the global pressure multipole of degree -(l+1). Hence the irrotational dipole vanishes (c != 1/4).
  In phi this is the coefficient d_0 of R^{-3} in the l = 0 Gegenbauer component of phi (5D monopole):
  d_0 = 0 is required for 1/2 < c_l < 3/4. For l >= 2, h_l = -p_l / (1 - c(l + 3)) is a global consistency check.

## 4. Full-space pressure

    -Delta P = sum_{i,j} (d_i U_j)(d_j U_i) = d_i d_j (U_i U_j),   P -> 0 as R -> infinity.

The Newtonian potential converges absolutely (source O(R^{-2 alpha - 2}), alpha > 0). Per Legendre mode f_l(R):

    P_l(R) = (1/(2l+1)) [ R^{-l-1} int_0^R s^{l+2} f_l(s) ds + R^l int_R^infty s^{1-l} f_l(s) ds ]   [checked by hand]

with the exterior integral evaluated from the analytically factored tail, never truncated at a finite sphere.
No harmonic term may be added to P. A second, independent free-space quadrature (direct Newton integral with
singularity subtraction) must agree at selected points (section 9).
Equivalence lemma [verifier proof, 18:31Z: the sublinearity of P~ follows by integrating M along radial lines
or from a principal-value Newton formula; absolute convergence of the Newton integral itself uses the stronger
differentiated decay |DU| = O(R^{-alpha-1}) of the primary class]: if the reduced system holds exactly and U = O(R^{-alpha}) with
|y| |DU| bounded, then M = (1 - c)U + W . grad U is a gradient -grad P~ with sublinear P~, so P~ - P is a
harmonic sublinear function, hence constant. Exact reduced solutions therefore satisfy the primitive equation
with the full-space pressure; for numerical approximations the primitive residual is an independent test.

## 5. Gauge and invariants

- Exactly one dilation gauge. Reporting gauge: int_{S^2} |F|^2 dS = 1, F = lim R^alpha U(R .). Under dilation
  F_L = L^{1+alpha} F. A working gauge (for example core radius a_eff = 1) is allowed during optimization; every
  report converts to the reporting gauge and records L.
- Dilation invariants to report: c_l, DU(0), q(0), Omega(0), max |Omega|, the shape F/|F|, swirl fractions.
- z-translation is not a symmetry (the c y term). Translation maps decaying profiles to non-decaying ones.
- a_eff (core scale, dilation covariant): a_eff = sup{ R : max_{|y| = R} |Omega(y)| >= max |Omega| / 2 } (vorticity
  half-maximum radius). Moment definitions are not used because int |Omega|^2 R^2 dy diverges for c_l > 1/2.
  Report also the location of max |Omega| and R_tail: the smallest R such that
  ||R'^alpha U(R', .) - F||_{L2(S^2)} <= 0.1 ||F|| for all R' >= R.

## 6. Diagnostics required for every reported candidate

6.1 Residual metrics (section 8 sets). For each equation E with linear damping term L_E and nonlinear part N_E:

    E = M:   L = (1 - c) U,   N = (U . grad) U        (Cartesian vectors)
    E = q:   L = q,           N = U_m . grad q + 2 (U^r/r) q
    E = eta: L = (1 + c) eta, N = U_m . grad eta - d_z(q^2)
    E = ell: denominator RMS(eta)
    E = div: denominator RMS(|DU|) (Frobenius)

    D_E(S)   = min( RMS_S(L_E), RMS_S(N_E) )
    rho_E(S) = RMS_S(R_E) / D_E(S)          (shell RMS ratio)
    m_E(S)   = max_S |R_E| / D_E(S)         (shell maximum ratio)

The min makes the metric robust against both known escapes: large-amplitude steady-Euler-like cores (where
N >> L) and the far tail where the leading homogeneous term cancels the linear operator (where L >> N).
For M the three components R_M^r, R_M^theta, R_M^z are each divided by the vector D_M(S).
Also report: absolute RMS(R_E) in the reporting gauge, the single-term ratio sigma_E = RMS(R_E)/RMS(L_E),
the nonlinear ratio RMS(R_E)/RMS(N_E), and the classical per-term ratio RMS(R_E)/max_k RMS(T_k) over the
individual terms T_k of the equation. If either piece of D_E(S) is below 1e-12 times its value in the core
shell, the shell is reported explicitly as degenerate.

6.2 Scaled far-field residuals: R^{2 alpha + 1} |R_M|, R^{2 alpha + 2} |R_q|, R^{2 alpha + 3} |R_eta| per shell.

6.3 Far-field coefficient checks. The verifier extracts F (and A, B) from the candidate at large R, computes G from
F with its own implementation of prompt section 5, and reports
delta_G(R) = ||R^{2 alpha + 1}(U - R^{-alpha} F) - G||_{L2(S^2)} / ||G||_{L2(S^2)} on shells R in [2^6, 2^10] a_eff.
Also: Legendre/Gegenbauer coefficients of A and B up to degree 8, pressure multipoles l = 0, 1, 2, and d_0 (3.5).

6.4 Swirl and nontriviality. Swirl fractions s_core = ||U^theta||_{L2(B_{4 a_eff})} / ||U||_{L2(B_{4 a_eff})} and
s_far = ||F_theta||_{L2(S^2)} / ||F||_{L2(S^2)}; max |q|; sign structure of q.

6.5 Axis and origin. Taylor coefficients at the origin and along the axis (z in a grid) of U^r/r, U^theta/r, U^z,
q, eta, phi to second order in s and z; reduced and primitive residuals evaluated at r = 0 with regular limits;
Cartesian finite differences across the axis with a step-size study (h = 1e-2 ... 1e-5 a_eff).
Piecewise representations (elements, patches, matching zones): at every internal interface, on at least 64 angular
points, the jumps of phi and its R- and mu-derivatives up to total order 3, and of q up to order 2, relative to
the local scale of the same derivative (added 2026-10-28T18:44Z, before any candidate).

6.6 Stagnation structure of W_m in r >= 0 (lead derivation, section 7) [referee: correct]. Find all zeros of W_m in
R <= 2^6 a_eff (axis zeros: c z + U^z(0, z) = 0; off-axis zeros: 2D Newton from a dense seed grid). For each:
position, eigenvalues of D W_m, q value, and the checks

    off-axis zero:   q = 0 and eta = 0 (c != 1/2), so D W_m is symmetric there (no foci)
    axis zero:       q (1 + 2 A) = 0,  A = d_r U^r(0, z0) = -d_z phi(0, z0)

Report the phase portrait (sources, saddles) and, for each source, the swirl-carrying condition of section 7.
Axis relation (added 2026-10-28T18:54Z, before any candidate): for an axis source at z0 with q0 = q(0, z0) != 0, on each axis
branch from z0 to the next axis zero or to infinity, W_z(0, z) eta(0, z) = 2 q(0, z) (q(0, z) - q0) exactly
(integrate the axis restriction of the eta equation, using the q equation; derivation in MATHEMATICAL_FORMULATION.md
section 6). Report its defect on at least 200 axis points per branch, relative to max |2 q (q - q0)| on the branch;
it is one of the stagnation checks used in A9 and B5.
S1 moment and curvature checks (added 2026-10-28T19:14Z, before any candidate; ORIGIN_AND_AXIS_REGULARITY.md section 6): at each
S1 source report (i) the relative defects of (1/4) int int r^3 eta rho^(-3) dz dr = phi(0, z0) = -c z0/2 and
(3/4) int int (z - z0) r^3 eta rho^(-5) dz dr = phi_z(0, z0) = 1/2, with eta from the candidate (exterior integrated to
infinity), which tests the 5D inversion and the resonance condition together; (ii) if q_z(0, z0) = 0 to 1e-8 relative,
the defect of 4(c - 1/2)(c + 1) q_rr + [(c + 1)^2 + q0^2] q_zz = 0 relative to its larger term. Both are reported, and
(i) is one of the stagnation checks used in A9 and B5.

Axis reconstruction, equatorial and sign checks (added 2026-10-28T19:38Z, before any candidate; reported, no threshold;
MATHEMATICAL_FORMULATION.md section 6 (n) to (p), AXISYMMETRIC_OBSTRUCTION_AUDIT.md Proposition 8): (iii) on each axis branch from an
axis source at z0 on which q(0, z) != 0, the defect of W_z(0, z) = (1 + c) q(0, z) int_(z0)^z dzeta / q(0, zeta), relative to
max |W_z| on the branch (equal to q times the axis integral of R_q / q^2, so it measures the integrated axis swirl
residual); (iv) in reflection-symmetric runs with q(0, 0) != 0: whether d_z(q^2) > 0 somewhere in z > 0 (necessary by
Proposition 8) and, if the origin is the only zero, the equatorial conditions W_r(r, 0) > 0 and d_r(r^2 q(r, 0)) > 0 for
r > 0 with the defect of phi_z(r, 0) = (1 + c l)/(2 + l), l = r q_r / q, on 200 equatorial points.
Axis chain check (added 2026-10-28T19:53Z, before any candidate; reported, no threshold; AXISYMMETRIC_OBSTRUCTION_AUDIT.md Proposition 10 and
Corollary 11): list all zeros of W_z(0, .) with w' there; at each attracting axis zero report k = 1 + (1 + c)/mu (mu = -w')
and its distance to the nearest integer; report whether q(0, .) is one-signed and whether all axis S1 sources have the same
q(0, z_i) (relative spread). A violation means the run is not a smooth profile with simple axis zeros (class F3 or F5).
Zero inventory check (added 2026-10-28T20:24Z, before any candidate; reported, no threshold; AXISYMMETRIC_OBSTRUCTION_AUDIT.md section 6):
all zeros of W_m in the closed half-plane (grid scan plus Newton polish, and a separate axis root search), each classified
as axis source P, axis saddle with axial inflow A, axis saddle with radial inflow B, off-axis source O or off-axis saddle D;
the index relation N_O - N_D = t (t the number of B zeros); at every off-axis zero the values of q and eta and the asymmetry
of D W_m (all zero for a smooth profile); the resonance defects (S1: v + 1/2; S3: slow eigenvalue minus (2 c - 1)/m for the
nearest integer m; B: radial eigenvalue nu against (3 c m - (2 c - 1))/(2 (j + 1 - m)); D: mu against (3 c m - (2 c - 1))/(l - m));
and max |Gamma| on two traced stable separatrices of each saddle relative to max |Gamma| (zero for c_l > 1/2).

6.7 Identities: energy-flux identity on B_R for R in {a_eff, 4 a_eff, 16 a_eff}, relative to its largest term;
vorticity-maximum identity at argmax |Omega|; Gamma transport along at least three meridional trajectories
(Gamma(s) = Gamma(s0) exp((2c - 1)(s - s0))).
Weighted circulation identities (added 2026-10-28T18:54Z; reported, no threshold): for p = 1 and p = 2 and three values of beta in
(3 + p(1 - alpha), 2p + 2), the relative defect of
int Gamma^p R^(-beta-1) U_R dV + (c/beta)(beta - 3 - p(1 - alpha)) int Gamma^p R^(-beta) dV = 0
(integrals over all of R^3, exterior included), relative to the larger of the two terms.
Further exact identities (added 2026-10-28T19:04Z; MATHEMATICAL_FORMULATION.md section 6 (e) to (j)): the pointwise defect of
W . grad H = (2c - 1)|W|^2 on the holdout sets (uses the full-space pressure); the energy finite part (zero for
c_l != 3/5; for 1/2 < c_l < 3/5 the convergent integral of |U|^2 - R^(-2 alpha)|F|^2); the helicity finite part (zero);
the virial c ||L||^2 + int N . L = 0; for 1/2 < c_l < 2/3 the 5D eta-norm identity; and the swirl-maximum condition
U^r/r = -1/2 at the maximum of |q|. Each is reported as a relative defect with its largest term as the scale.

## 7. Theory status (details in AXISYMMETRIC_OBSTRUCTION_AUDIT.md)

- c_l < 1/2: no nontrivial Cartesian C^2, decaying axisymmetric profile (uniformly sublinear ones are constant
  axial vectors); CIV Theorem 4.5 proof, with U(0) = 0 replaced by decay at the last step. C^2 is used for the
  boundedness of eta = Omega^theta / r; C^1 alone does not supply it (corrected 18:37Z, verifier remark). Do not spend search compute below c_l = 1/2.
- No swirl-free profile exists for any c_l > 0 (CIV Remark 4.6 argument): swirl is necessary.
- Dulac: div(r W_m) = 3 c r > 0 excludes periodic orbits and polycycles of W_m in r >= 0 and attracting
  stagnation points. Backward W orbits are bounded (sublinearity). With finitely many stagnation points every
  backward orbit converges to a stagnation point [referee: correct; forward convergence to a saddle along its
  stable manifold is not excluded].
- c_l = 1/2: Gamma is constant on W_m orbits, so Gamma takes only values in Gamma(stagnation set). A swirling
  profile at c_l = 1/2 needs a continuum of stagnation points along which Gamma varies (for example a curve of
  stagnation points; the Gamma level curves are transverse to that curve, while grad Gamma itself need not be).
  With countably many stagnation points the profile is trivial [referee and verifier: correct].
- c_l > 1/2: no obstruction known. Necessary conditions at swirl-emitting sources [referee: correct as corrected]:
  (S1) axis source with q(y0) != 0 requires A = -1/2 exactly, so lambda_r = c - 1/2, lambda_z = c + 1
       (locally a Burgers-type strain with rotation; d_z U^z = 1);
  (S2) hyperbolic axis source with q(y0) = 0: the leading Taylor term of q is a multiple of s^j, j >= 1 (no
       (z - z0) factor is possible), with A = -(1 + 2jc)/(2(j + 1)), lambda_r = (2c - 1)/(2(j + 1)); j = 1 gives
       A = -(1 + 2c)/4;
  (S3) off-axis source: grad Gamma != 0 requires spectrum {2c - 1, c + 1}; grad Gamma = 0 with nonzero Hessian
       requires lambda_min = (2c - 1)/2; a vanishing 2-jet with nonzero germ requires lambda_min < (2c - 1)/2.
       Off-axis zeros have eta = 0, so D W_m is symmetric and no focus occurs.

## 8. Evaluation sets

- Units: a_eff of the candidate. Dyadic shells S_k = {2^k a_eff <= R < 2^{k+1} a_eff}, k = -6, ..., 11, plus the
  origin ball R < 2^{-6} a_eff. Representations restricted to a finite exterior must say so; acceptance
  requires k up to 11 at least.
- In each shell: Gauss-Legendre in log R (at least 8 nodes) times Gauss-Legendre in mu (at least 1.5 times the
  candidate's angular resolution and at least 64), plus 256 uniformly random points. 3D measure dV = 2 pi r dr dz.
- Axis collar: the part of each shell with sin(vartheta) < 0.05, evaluated with measure R^2 dR dvartheta
  (no sin weight). Thresholds apply to the collar separately.
- Holdout: the verifier generates its own points with its own seeds; they are never given to an optimizer.
  Numerics may use its own holdout for ranking, but acceptance uses only verifier-measured values.

## 9. Pre-registered acceptance thresholds (frozen 2026-10-28T18:25Z, after the wording fix below)

Let rho_max = max over E in {M^r, M^theta, M^z, q, eta, div, ell} and over all shells and collars of rho_E(S),
and m_max likewise for m_E(S). All values below are measured by the verifier with independent code.

Label A (strong numerical candidate). All of:
- A1 rho_max <= 1e-6.
- A2 m_max <= 1e-4.
- A3 Three refinement levels (each raising every resolution parameter by at least 1.3x): rho_max decreases at
  each step and by a total factor of at least 10, or reaches 1e-9.
- A4 If c_l is free: |c_l(N3) - c_l(N2)| <= 1e-5. If c_l is fixed: report rho_max for the same branch at two
  other fixed c_l values within 0.01 (continuation evidence).
- A5 s_core >= 0.05 and s_far >= 0.05, each changing by at most 1 percent (relative) between the two finest levels.
- A6 delta_G <= 1e-3 on the shell [2^10, 2^11] a_eff and decreasing from [2^6, 2^7] to [2^10, 2^11]; A and B coefficients up to degree 8 stable to 1e-4
  (relative to ||F||, reporting gauge) between the two finest levels; R_tail finite and stable to 5 percent.
- A7 Pressure: per-mode Green-function pressure and direct free-space quadrature agree to 1e-6 relative at
  >= 20 points (core, axis, matching zone, far field; relative to the local |P| scale of the shell);
  pressure monopole and dipole coefficients p_0, p_1 (of R^{-1} P_0 and R^{-2} P_1, after subtracting the part
  forced by the local expansion: at c_l = 2/3 the local Q_0 term; otherwise nothing) and d_0 consistent with zero:
  |p_0| / a_eff <= 1e-5 max|P|, |p_1| / a_eff^2 <= 1e-5 max|P|, |d_0| / a_eff^3 <= 1e-5 max|phi|.
- A8 Regularity: axis and origin Taylor residuals <= 1e-6 relative; finite-difference derivative checks agree
  with analytic derivatives to 1e-6 relative (first derivatives) with a converging step study; max |Omega| and
  max |D^2 U| change by at most 1 percent between the two finest levels. For piecewise representations the
  interface jumps of 6.5 are <= 1e-6 relative (label B: <= 1e-3); these are part of the derivative checks.
- A9 No escape: a_eff and the location of max |Omega| stable to 1 percent between the two finest levels; the
  core lies inside the representation's resolved inner region; energy-flux identity holds to 1e-6 relative;
  vorticity-maximum identity holds to 1e-5 relative; the swirl-maximum condition of 6.7 holds to 1e-5 (absolute
  defect of U^r/r + 1/2 at the maximum of |q|); the stagnation checks of 6.6 hold to 1e-5 relative.
- A10 Independence: the verifier's own basis evaluator (written from BASIS.md) reproduces field_eval.py values
  to 1e-12 relative, and all of A1 to A9 use the verifier's own derivatives, pressure and quadrature; at least
  one check (A1 on four shells) is repeated in a representation that is numerically independent of the
  candidate's (for example a projection onto the verifier's grid with its own differentiation).

Label B (promising but unresolved). Not A, and all of:
- B1 rho_max <= 1e-3 at each of at least two resolution levels, with rho_max improving by at least 2x.
- B2 s_core >= 0.05 and s_far >= 0.05, stable to 10 percent.
- B3 c_l (if free) stable to 1e-2.
- B4 Pressure two-way agreement <= 1e-3; regular by construction or Taylor residuals <= 1e-3; interface jumps
  (6.5) <= 1e-3.
- B5 No escape: a_eff and max |Omega| location stable to 10 percent; the stagnation checks of 6.6 hold to 1e-2.
Every unmet A criterion is quantified in the report.

Label C (unsuccessful numerical search): neither A nor B. Includes every candidate whose small residual is seen
at only one resolution, any candidate that fails an escape or independence test, and every stalled branch.

Label D (rigorous obstruction): only for a complete proof excluding a clearly stated class. The c_l < 1/2
obstruction is reported separately; it is not a label for the main 1/2 < c_l < 3/4 search.

Stall rule: a branch whose rho_max has not improved by a factor of 2 across two consecutive refinements
(each at least 1.4x in every resolution parameter) is stalled. A stalled branch cannot be A, and numerics stops
spending GPU time on it beyond diagnosing the cause.

These numbers are not relaxed for an appealing candidate. A numerical candidate is an approximation, never an
exact profile; a small training or collocation loss is never evidence of existence.

### 9.1 Failure-map protocol (pre-registered 2026-10-28T19:28Z, before any candidate; reporting rules only, no threshold changed)

Purpose: if no branch reaches label B by the end of Stage II, the Stage II deliverable is a quantitative failure map
defined here in advance, so that the reading of the numbers is not chosen after seeing them.
- Floor. For each c_l (prescribed or free-c_l endpoint), initialization family and resolution level N, the floor
  f_N(c_l) is the smallest holdout rho_max (section 9) among runs that satisfy B2 (s_core >= 0.05, s_far >= 0.05). Runs
  failing B2 are reported separately as collapsed and never define a floor.
- Refinement reading. A floor is "decreasing" if f_(N+1) <= f_N / 2 at the last refinement, and "plateaued" if
  f_(N+1) > 0.7 f_N at the last two refinements (each at least 1.3x in every resolution parameter). Only a decreasing
  floor is evidence of anything. A plateau at a prescribed c_l is consistent with solutions that occur only at isolated
  c_l, but it is expected only locally, near a transverse isolated profile (referee verdict 2026-10-28T19:47Z record,
  MATHEMATICAL_FORMULATION.md section 4); a plateau can also come from discretization or optimization error at a true
  exponent, and a decreasing floor need not converge to an attained solution. The failure map therefore reports floors
  and never reads a plateau as evidence of non-existence at that c_l.
- Jacobian diagnostics (added 2026-10-28T19:53Z, reported, no threshold). For the best free-c_l run per family and level, report the
  five smallest singular values of the gauged free-c_l Jacobian (unknowns including c_l, with the dilation gauge row),
  normalized by the largest. A singular value that decreases under refinement while the residual decreases is the
  signature of a one-parameter family (extra null vector); a well-separated smallest singular value is consistent with
  an isolated solution. Report also the signed projection of the residual on the left singular vector of the smallest
  singular value of the fixed-c_l gauged Jacobian across the c_l list (a sign change brackets a candidate c_l).
- Dip. A local minimum of f_N(c_l) over the c_l list (or a free-c_l endpoint c_l*) is reported as a dip only if it is
  at least 3x below both neighbours at each of the two finest levels and its location moves by less than 0.01 between
  them. A dip is a pointer for a free-c_l refinement, not a candidate.
- Mechanism. Each plateaued or failed branch is assigned one primary failure class, with the measured quantity:
  (F1) swirl collapse (B2 fails); (F2) fictitious tail or cancelling exterior terms (delta_G or tail-coefficient
  instability, 6.3); (F3) stagnation-structure violation (6.6 checks, including the S1 moment and curvature checks);
  (F4) pressure mismatch (two-way pressure disagreement or nonzero p_0, p_1, d_0 after subtraction, A7);
  (F5) regularity defect (axis, origin or interface, A8); (F6) solver non-convergence at fixed resolution (no
  decrease over the last 20 percent of the iteration budget); (F7) refinement plateau with none of F1 to F6 dominant;
  for F7 the shell and equation carrying the largest rho_E are reported.
- Table. The failure map lists, per c_l: initialization families tried, resolution levels, f_N at each level, the
  dominant equation and shell, the failure class, GPU hours and wall time used.

## 10. Candidate exchange format

Numerics writes each candidate to
numerical_search/candidates/<branch>/<level>/ containing:
- candidate.json: id, branch, level, c_l, whether c_l was free, alpha, working gauge and the conversion factor L
  to the reporting gauge, a_eff, representation name, all resolution parameters, quadrature used, creation time,
  source hash, and self-measured metrics (rho_max, m_max, per-equation).
- coeffs.npz: all coefficient arrays, with names matching BASIS.md.
- BASIS.md: a complete mathematical definition sufficient for independent reimplementation: coordinates and
  maps (with all constants), basis functions and normalization, coefficient array shapes and index ordering,
  envelope powers, the list of exponents the exterior can express (3.3), matching or partition functions,
  and how phi, q (and eta if primary) are formed. Nothing may be defined only by reference to code.
- field_eval.py: numpy only, self-contained, exposing eval_phi_q(r, z) -> (phi, q) (values only; optionally
  eval_eta(r, z)). Used only for value cross-checks; the verifier differentiates with its own code.
- samples.npz: r, z, phi, q, U^r, U^theta, U^z, P on a numerics-chosen grid, for spot checks.
The leaderboard ranks by holdout rho_max (section 6.1 metric), never by training loss.

## 11. Search guidance (non-binding)

c_l in {0.505, 0.525, 0.56, 0.60, 0.64, 0.68, 0.72, 0.74}, then free c_l. c_l = 1/2 is a separate experiment.
Pay attention to c_l = 2/3 (removable l = 0 pressure resonance) and c_l = 3/5 (first logarithmic coincidence, 3.3).
Initializations should include the swirl-emitting source structures of section 7.
(2026-10-28T19:20Z, non-binding; qualified 2026-10-28T19:53Z) Conditional generic count: isolated (c_l, q0) modulo dilation are expected
if the linearization is Fredholm of index 0 and transverse (MATHEMATICAL_FORMULATION.md section 4, not proved), so search
with c_l free and one dilation gauge, keep fixed-c_l scans as diagnostics, and report the best residual floor per c_l.
Revised S1 seeds: the seed script s1_sym_v2.py of the report author (its parameters are in numerical_code/configs/s1_sym_v2_params_from_lead.json).
(2026-10-28T20:24Z, non-binding) Zero-set portraits (AXISYMMETRIC_OBSTRUCTION_AUDIT.md section 5b; referee inventory, lead-checked, verifier-confirmed 20:31Z): T1 a single
S1 axis source with even swirl (current branch); T2 an equatorial ring source (S3, m = 1) feeding a radial-inflow axis saddle at
the origin, odd swirl, nu = (1 + c)/2, v(0, 0) = -(1 + 3c)/2, ring eigenvalues (1 + c, 2c - 1); T3 an even S1 pair at z = +-z1 with
a central axial-inflow saddle of order k = 2, v(0, 0) = (1 + 2c)/2. Gauges: z0 or z1 = 1, ring radius 1. Near c_l = 1/2 a single
Hessian-matched core is excluded under a uniform-shape hypothesis (audit Proposition 13), so runs there are diagnostics.
(2026-10-28T20:39Z, non-binding) Decaying T2 seeds with an exact two-zero inventory: seeds/ring_t2.py (audit section 5c). With the
ring pinned at r = 1 the dilation gauge is used up, and K = q_z(1, 0) is a shape parameter; the dilation invariant is (ring radius)
x q_z(ring). For reporting, convert to the gauge of section 5.
(2026-10-28T20:47Z, non-binding) Decaying T3 seeds with an exact three-zero inventory: seeds/pair_t3.py (audit section 5d). In a T3
profile q vanishes exactly to second order on the whole equator (Lemma 14), q = Q z^2 + ... at the saddle, and the eta
coefficient there is e = 2 K Q/(1 + c); a representation for T3 must contain z^2 times a smooth function, not a nonzero q(r, 0).
The sources at z = +-1 use the dilation gauge.
(2026-10-28T21:04Z, non-binding) T2 restrictions (audit section 5f, referee, lead-checked): on the upper axis q = eta = eta_s = 0, so
q = s z V and eta = s^2 z J near the axis; eta_z(s, 0) > 0 on the whole equator; eta < 0 near the upper axis far out (E''(1) < 0);
the origin amplitude C is transmitted from K. Heuristic count: a saddle that receives swirl has a quantized strain with no new
amplitude, so T2 and T3 are expected to be codimension one among smooth profiles and T1 is the only square portrait of the
three; T1 stays the primary smooth target, and a flat T2 or T3 residual floor is the expected generic outcome. (Qualified
2026-10-28T21:50Z: this holds in the smooth stratum only; in the C^2 class of the prompt the T2 and T3 strains are free, see below.)
(2026-10-28T21:09Z, non-binding) T3 restrictions (audit section 5d addendum, referee, lead-checked): the seeds of the form phi = z F(rho),
q = z^2 G(rho) give e = 0 or e < 0 at the saddle, while e = 2 K Q/(1 + c) > 0 is required, so they need a localized correction at
the saddle; on the equator eta_z = (K gamma/delta) q_zz/(2 (c - phi_z)) > 0; T3 needs eta of both signs in z > 0 and favourable
source-strain contributions above 2/3 from regions other than the axis (source-strain kernel sign corrected 2026-10-28T21:50Z, audit
section 5d (c); the kernel is (z - 1) rho_-^(-5) + (z + 1) rho_+^(-5)).

(2026-10-28T21:50Z, non-binding) Finite regularity (audit section 5g, referee with proof, lead-checked). The class of section 3 is
Cartesian C^2. In it the T3 origin saddle may carry q ~ A(s)|z|^k with any k > 2 (k = 1 + (1 + c)/mu, axial rate mu in
(0, 1 + c]) and the T2 origin saddle q ~ C s^j z with any j > 1/2; the elementary counts of these strata are square, like T1.
Polynomial bases in (s, z) approximate such profiles without a floor but only algebraically (C^2 error about N^(-(k - 2))), so in
a smooth basis such a branch would meet the stall rule of section 9 and could not reach A or B there; that is the expected
signature, not evidence against it. Diagnosis of a stalled T2 or T3 branch therefore includes the fitted algebraic rate of
rho_max in N and of the quotient q/|z|^k near the equator. A dedicated representation (q = |z|^k G, phi = z F + sgn(z)|z|^(k + 1) Psi,
k unknown, row (k - 1)(-c - 2 phi_z(0, 0)) = 1 + c) is a separate experiment; for it, A8's axis and origin Taylor residuals are
read as the Cartesian C^2 checks of audit 5g (h) (thresholds unchanged), and the verifier decides whether the regularity
checks are met.

## 12. Change log

- 2026-10-28T18:24Z v0 registered.
- 2026-10-28T18:25Z v0 wording fixed before any candidate existed or was announced: a_eff redefined as the
  vorticity half-maximum radius (the moment form diverges for c_l > 1/2); delta_G shell moved outward to
  [2^10, 2^11] a_eff so that the next asymptotic order is below the 1e-3 tolerance; multipole tolerances made explicit.
- 2026-10-28T18:37Z referee results recorded (referee civ-theory and farfield-algebra, verifier notes 18:28Z and
  18:31Z). Markers updated in 1, 3.1, 3.3, 3.4, 3.5, 4, 6.6, 7. Corrections: section 7 needs Cartesian C^2, not C^1;
  S2 and S3 sharpened; c_l = 1/2 transversality statement corrected. A7 wording clarified (the zero test applies
  to the coefficient left after subtracting the locally forced term, which is nonzero only at c_l = 2/3); no
  tolerance changed. 6.6 gains the eta = 0 check at off-axis zeros.
- 2026-10-28T18:44Z added the interface-jump diagnostic (6.5) and made it explicit in A8 and B4. Reason: the numerics
  representation is piecewise (ball, shells, exterior) with interface continuity imposed only by penalty rows for
  phi in C^2 and q in C^1, while the class requires a Cartesian C^2 velocity (phi in C^3, q in C^2). This is a
  stricter, pre-candidate addition; no existing threshold is relaxed.
- 2026-10-28T18:54Z added the axis relation W_z eta = 2 q (q - q0) to 6.6 (so it enters the A9 and B5 stagnation checks) and the
  weighted circulation identities to 6.7 as reported diagnostics. Both are exact consequences of the reduced
  equations. Stricter, pre-candidate additions; no existing threshold is relaxed.
- 2026-10-28T19:04Z added further exact identities to 6.7 (Bernoulli-Lyapunov, energy and helicity finite parts, virial, 5D eta
  norm, swirl maximum; source: referee answer checked by the lead, see MATHEMATICAL_FORMULATION.md section 6) as
  reported diagnostics, and the swirl-maximum condition to A9 at the same 1e-5 level as the vorticity-maximum
  identity. Stricter, pre-candidate additions; no threshold relaxed.
- 2026-10-28T19:14Z added the S1 moment and curvature checks to 6.6 (exact consequences: 5D Green representation of phi and the
  verifier's curvature relation, lead-checked). Stricter, pre-candidate addition; no threshold relaxed.
- 2026-10-28T19:28Z added 9.1, the Stage II failure-map protocol (floor, refinement reading, dip criterion, failure classes F1-F7).
  Reporting rules defined before any candidate; no acceptance threshold changed.
- 2026-10-28T19:38Z added checks (iii), (iv) to 6.6 (axis reconstruction, Proposition 8 sign condition, equatorial
  conditions); reported only. Pre-candidate; no threshold changed.
- 2026-10-28T19:53Z softened the plateau sentence of 9.1 after the referee verdict on the count (positive floors are only a local
  prediction); added the Jacobian diagnostics to 9.1 and the axis chain check to 6.6. Reported only; pre-candidate; no
  threshold changed.
- 2026-10-28T20:24Z added the zero inventory check to 6.6 and the portrait list to 11 (referee inventory, lead-checked).
  Reported only; pre-candidate; no threshold changed.
- 2026-10-28T20:39Z section 11: portrait reference corrected to audit section 5b, T2 seed pointer and the T2 amplitude-gauge remark
  (verifier qualification). Guidance only; no threshold changed.
- 2026-10-28T20:47Z section 11: T3 seed pointer and the equatorial zero of q (audit section 5d, Lemma 14). Guidance only; no
  threshold changed.
- 2026-10-28T21:04Z section 11: T2 restrictions and the saddle count remark (audit section 5f). Guidance only; no threshold changed.
- 2026-10-28T21:09Z section 11: T3 restrictions and the T3 seed sign defect (audit section 5d addendum). Guidance only; no threshold changed.
- 2026-10-28T21:50Z section 11: source-strain kernel sign corrected in the T3 pointer; T2 count remark qualified to the smooth stratum; finite-regularity pointer (audit section 5g) with the reading of A8 for fractional representations. Guidance only; no threshold changed.
