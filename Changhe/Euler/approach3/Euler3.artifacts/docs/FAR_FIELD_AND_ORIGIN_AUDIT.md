# Far-field and origin audit

Scope: the asymptotic structure of rotating profiles at infinity and the local conditions at the origin, the
checks performed on each statement, and the tests every candidate must pass. Equations and notation are those of
MATHEMATICAL_FORMULATION.md (alpha = (1-c_l)/c_l in (1, 3/2), chi = phi + (omega/c_l) log r, F, H the leading
velocity and vorticity tail coefficients). Status labels: [V] executed exact check (script in derivations/),
[I] confirmed by the independent validation route, [R] reviewed by hand, [C] assumption.

Last update: 2026-10-26T01:27:13Z (references made neutral: the mixed-resonance log path and a consultation tag; no content change); 2026-10-25T10:26Z (2.7 K_H reproduced by the primary route; degree-8 D6-lineage values); 2026-10-25T10:19Z (2.7 K_H rows all independently confirmed; projection reading of K_1 and K_H, d84/d88); 2026-10-25T09:42Z (2.2 helicity pairing now [I], remainder by the flux equation, d81); 2026-10-25T09:28Z (2.2 helicity pairing and 2.7 K_H, d78); 2026-10-25T06:56Z (2.7 K_1 direct ratio for the degree-6 nest rung, -8.98, independent); 2026-10-25T06:47Z (2.2 pairing verified, sufficient hypothesis and pressure qualification; K_1 by direct coefficients, d68); 2026-10-25T06:26Z (2.2 energy pairing of the first correction and test K_1 in 2.7, d67 [R]); 2026-10-25T04:12:20Z (mean-swirl generation test d55 [R], d58 [R], d57 identity [I], d49b wording corrected; 03:32:05Z state-level tail generation: mode split d49b [R]; 03:21:44Z state-level tail generation d49 [R]; 03:13:16Z 4(f) swirl normalization and core radius [I]; 03:08:19Z 4(g) independently confirmed [I]; 02:52:02Z 4(f) tags corrected and split after the independent confirmation of d43 sections 1 and 3; 4(g) ray form and SPEC v1.22 diagnostics; 02:36:04Z 4(e) twisted case confirmed [I]; 4(f) edge and energy law, 4(g) backward-transport inverse added; 02:16:11Z section 4(e) twisted case added; earlier: sections 2.2, 2.4 and 4 extended; earlier text unchanged since 2026-10-24T21:42Z).

## 1. Conclusions in brief

- The leading tail r^(-alpha) F(theta, chi) is free formal data: two arbitrary smooth scalar functions on S^2,
  subject only to one exactly solvable divergence constraint. It is fixed by matching to the core, not by the
  far-field equations. This is the reason the tail coefficients are optimized together with the core.
- The first nonlinear correction r^(-(2alpha+1)) G[F] and the local pressure r^(-2alpha) Q[F] are determined by F.
  A far-field loss that only tests the linear operator is satisfied by every F and therefore proves nothing; the
  campaign's far-shell diagnostics measure the nonlinear balance separately.
- Harmonic pressure multipoles r^(-(l+1)) Y_l^m (l >= 2, untwisted) carry global data (finite parts of source
  moments). The l = 0, 1 moments vanish.
- Logarithmic terms occur only at rate coincidences, which need rational c_l; none is at low order on the
  registered grid c_l in {0.41, 0.43, 0.45, 0.47, 0.49}, but 0.43 is within 0.023 in rate of the order-3
  coincidence of c_l = 3/7, so tail models there use a resonance-regular form.
- Everything above is formal: a complete expansion with a controlled remainder is not established [C].
- At the origin the conditions are the Taylor equations of R_u; they are audited exactly at y = 0.

## 2. Far field

### 2.1 Linear operator and leading tail [V, d02; I]

The linear part L U = (1-c_l) U + c_l (y.grad) U + omega [J U - (J y.grad) U] acts on twisted homogeneous fields
r^(-k) G(theta, chi) (spherical components) as multiplication by c_l (alpha - k). On untwisted fields
r^(-k+i nu) e^(i m phi) the multiplier is c_l (alpha - k) + i (c_l nu - m omega), nonzero for k > alpha. Hence the
twisted rate alpha is the only rate in the kernel, and every other velocity term has a nonzero linear coefficient
that must be balanced by nonlinear or pressure terms of the same rate.

Divergence constraint on F:

    (2-alpha) F_r + (omega/c_l) d_chi F_r + (1/sin th) d_th(sin th F_th) + (1/sin th) d_chi F_ph = 0.

General smooth solution: with smooth scalars sigma, tau on S^2 and B = (2-alpha) sigma + (omega/c_l) d_chi sigma,

    F_r = -Delta_S2 sigma,  F_th = d_th B + d_chi tau / sin th,  F_ph = d_chi B / sin th - d_th tau,

which is the leading tail of curl(T y) + curl curl(S y) with T = r^(-alpha) tau, S = r^(1-alpha) sigma.
Completeness [R, confirmed by an independent audit]: integrating the constraint gives zero mean of F_r; solve
-Delta_S2 sigma = F_r; the remaining tangential part is divergence free on S^2 and equals grad tau x e_r.

Leading vorticity: Omega_0 = r^(-(alpha+1)) H with
H_r = [d_th(sin th F_ph) - d_chi F_th]/sin th, H_th = d_chi F_r/sin th - [(1-alpha) F_ph + (omega/c_l) d_chi F_ph],
H_ph = (1-alpha) F_th + (omega/c_l) d_chi F_th - d_th F_r [V, d02; I, Cartesian versus spherical agreement below
7e-15]. A nonzero exact leading tail cannot have H identically zero (otherwise the Cartesian components would be
harmonic exterior fields without l = 0 part, so the
sphere mean of |U|^2 would decay at least like r^(-4), against the exact r^(-2alpha))
[I; R]. Pointwise zeros of H are possible and are recorded for every candidate.

Rigorous decay fact [R; I, standalone independent proof]: for |U| <= C (1+r)^(-alpha) uniformly, any nonzero profile has
integral_{B_R} |U|^2 = L R^(3-2alpha) + O(R^(2-3alpha)) with L > 0, and U = o(r^(-alpha)) uniformly forces U = 0.
So within that class the natural rate cannot be beaten. The rescaled limits R^alpha U(R .) (with the rotation
by (omega/c_l) log R) show, without differentiating the remainder, that the leading tail is divergence free and in
the kernel of L. The dichotomy gives a positive normalized energy limit, not convergence to a pointwise angular
profile; the existence of F is part of the assumed tail class, and nothing follows for sequences of approximate
states (a numerical tail collapse is not evidence of a zero limit).

### 2.2 First nonlinear order [V, d02; I]

(U_0.grad) U_0 = r^(-(2alpha+1)) N; the local pressure r^(-2alpha) Q solves -Delta(r^(-2alpha) Q) =
div(r^(-(2alpha+1)) N) = tr((DU_0)^2); G = N + ((-2alpha + (omega/c_l) d_chi) Q, d_th Q, d_chi Q/sin th);
div(r^(-(2alpha+1)) G) = 0 and L U_1 + (U_0.grad) U_0 + grad(r^(-2alpha) Q) = 0 for U_1 = r^(-(2alpha+1)) G (the
linear factor is -1). The pressure eigenvalue on Y_l^m(theta) e^(i m chi) is
(-2alpha + i m omega/c_l)(1 - 2alpha + i m omega/c_l) - l(l+1), nonzero in the open range: for m != 0 its
imaginary part is (m omega/c_l)(1 - 4alpha), for m = 0 a zero needs 2alpha = l+1. Near-singular modes are
(l, m) = (1, 0) as c_l -> 1/2 and (2, 0) as c_l -> 2/5; the smallest modulus used is printed for every run.
Independent tests: pressure coefficient reconstruction below 1.6e-13 and explicit angular divergence of G below
2e-14 on a non-axisymmetric seed [I].

Seed family [V, d02]: F_r = 0, F_th = 2 eps sin th sin 2chi, F_ph = sin th + 2 eps sin th cos th cos 2chi (toroidal,
tau = cos th - eps sin^2 th cos 2chi, smooth at the poles; at eps = 0, H = (2 cos th, (alpha-1) sin th, 0) has no
zeros). It is one of several seed families; poloidal, mixed and random order-one non-axisymmetric tails are also
used.

Carried coefficient in a representation with separate rate channels [I, independent proof of 2026-10-25; R, lead
review derivations/d38, CORRECT; V, derivations/d38_normcheck.py, norm formula to 4e-16]. For the twisted channel
U_1 of rate 2alpha+1 one has DU_1 y + (omega/c_l)(J U_1 - DU_1 J y) = -(2alpha+1) U_1, and since
c_l(2alpha+1) = 2 - c_l the self-similar operator acts on U_1 as minus the identity. Hence the rate-(2alpha+1)
coefficient of R_u is exactly G_required - G_carried, where G_required = G[F] is computed from the state's own F; it
cannot be reduced by any other linear tail adjustment. Other rates do not mix with it: the velocity rates alpha + j
skip 2alpha+1 because alpha + 1 is not an integer, the untwisted multipole rates are integers >= 4 > 2alpha+1, and
products involving U_1 have rate >= 2alpha+2. The incorrect rates alpha+1 and alpha+2 of 2.6(2) both lie below
2alpha+1 and are tested separately.

Energy pairing of the first correction [R, theory route, derivations/d67 (sympy check of the ball-identity algebra);
V, independently proved, with a sufficient hypothesis for the expansion reviewed in derivations/d68; report section 2,
item 30; recorded 2026-10-25T06:26Z, verified 06:33Z]. Since U_1 = (U_0.grad) U_0 + grad P_0 with P_0 = r^(-2alpha) Q,
U_0 . U_1 = div(U_0 (|U_0|^2/2 + P_0)); every factor is equivariant under the dilation-rotation, so integration over
1 < r < s gives int_(S^2) F . G[F] dS = (2 - 3alpha) Phi_F, Phi_F = int_(S^2) F_r (|F|^2/2 + Q) dS. Consequently the
angular energy s^(2alpha) int_(S^2) |U(s n)|^2 dS (written E_F(s) in the report's section 2b, item 6; not the
distance E_F(r) of 2.7) equals 1 + 2 (2 - 3alpha) Phi_F s^(-(alpha+1)) + O(s^(alpha-4)) in the gauge int |F|^2 = 1,
the remainder rate being that of the l = 2 multipole cross term (4 - alpha > alpha + 1 for c_l > 2/5), the first
allowed rate, not a term known to be nonzero. A sufficient hypothesis (independent proof) is a smooth exact profile with
its decaying whole-space pressure and |D^j(U - U_0)| = O(r^(-alpha-1-j)), j = 0, 1: then the pressure remainder is
O(r^-3) with gradient O(r^-4), L V = O(r^-4) for V = U - U_0 - U_1, and integration along the twisted characteristics
gives V = O(r^-4). Q is unique in the twisted-homogeneous class (nonresonant multiplier); exterior decay
P = O(r^(-2alpha)) alone would allow an added harmonic eps r^-3 Y_2m, which the whole-space convention excludes. An
s^(-2) term, as produced by a regularized envelope or a channel of rate alpha + 2, is excluded. Test 2.7 (K_1) uses this.

Helicity pairing of the first correction [I, theory route, derivations/d78 (symbolic identity with negative control;
sampled density-versus-flux check to 8.1e-5 on six exports); independently proved by the independent route at
2026-10-25T09:35Z, remainder argument reviewed in d81; report section 2, item 34, values in section 2b, item 8;
recorded 2026-10-25T09:28Z, label updated 09:42Z]. For any smooth U, P with N = (U.grad) U + grad P and h = U . Omega,
U . curl N + N . Omega = div(h U + (P - |U|^2/2) Omega). Applied to (U_0, P_0), whose left side is twisted-homogeneous of
degree -(3alpha+2), integration over 1 < r < s gives the s^(-(alpha+1)) coefficient of s^(2alpha+1) int_(S^2) h:
K_H = (1 - 3alpha) Psi_F, Psi_F = int_(S^2) [(F . H) F_r + (Q - |F|^2/2) H_r] dS, under the hypothesis above, with
remainder O(s^(alpha-4)). A direct substitution would need DV = O(r^-5) for V = U - U_0 - U_1, which that hypothesis
does not state; the proof instead integrates the sphere-averaged exact helicity balance, h_F' = -(1/c_l) s^(2alpha-2) T'
with T the flux through |y| = s, which needs only U, DU and P (independent route, reviewed by the theory route). Reading the head fluxes Psi_F and Phi_F from sampled full fields
needs care: they converge only with relative error O(s^(2alpha - 3)) because the whole-space pressure contains the
exterior harmonic quadrupole of degree -3 (no monopole or dipole for a double-divergence source). Test 2.7 (K_H) uses
this.

### 2.3 Formal structure of the full expansion [R, corrections from an independent audit applied; V where named]

Exact formal velocity rates (real parts):

    n(alpha+1) - 1 + sum_{j=1..d} (l_j + 3),   n tail factors, d pressure multipoles of degrees l_j >= 2, n + d >= 1,

i.e. alpha (n = 1), 2alpha+1 (n = 2), n/c_l - 1 (pure tail), l + 2 (one multipole: velocity
-grad p_l/((1 - c_l(l+3)) - i m omega), real part of the denominator below -1), and mixed terms. Pressure rates are
one less. Coefficient dependence: F is free; pure-tail terms are determined by F; multipole coefficients C_lm are
global; mixed coefficients are determined by F and the previously determined multipoles. Products of pure multipole
velocities give no new terms (their velocity is a harmonic gradient V whose self-interaction is cancelled by the
local pressure -|V|^2/2).

Monopole and dipole: the source tr((DU)^2) = d_i d_j(U_i U_j) is a double divergence, so under differentiated tail
decay its l = 0 and l = 1 moments vanish (boundary terms O(R^(1-2alpha)), O(R^(2-2alpha))): no homogeneous r^(-1),
r^(-2) pressure terms. This does not remove the l = 0, 1 parts of r^(-2alpha) Q [R; I].

### 2.4 Pressure multipoles and finite parts [V, d03 for the Green formula; R]

With f_lm(s) ~ sum a_{p,nu} s^(-p-2+i nu) the complete asymptotic source in the true azimuth,

    C_lm = (1/(2l+1)) lim_{R->inf} [ integral_0^R s^(l+2) f_lm ds - sum_{Re p <= l+1} a_{p,nu} R^(l+1-p+i nu)/(l+1-p+i nu) ],

subtracting every non-integrable term, including bounded oscillatory ones (Re p = l+1, nu != 0). At a resonance
((p, nu) = (l+1, 0) with a != 0) a log R is subtracted as well; with the particular pressure
(a/(2l+1)) r^(-(l+1)) log r, C_lm = FP M_lm/(2l+1) + a/(2l+1)^2. Exterior contributions beyond the resolved radius:
integral_R^inf s^(1-l) a s^(-p-2+i nu) ds = a R^(-l-p+i nu)/(l+p-i nu). Source harmonics oscillate like
s^(i m omega/c_l) in the true azimuth; radial quadrature uses a logarithmic variable.

Lower multipoles of the full-space pressure [R, derivations/d38 section 3; I, confirmed 2026-10-25T01:15Z]. If, for
r >= 1, U = U_0 + U_r with U_0 the leading twisted-homogeneous field of degree -alpha, |U_r| = O(r^(-alpha-1)) and
|DU_r| = O(r^(-alpha-2)), then the decaying pressure satisfies grad P = grad P_0 + O(r^-4) with P_0 = r^(-2alpha) Q[F].
The remainder source g = f + Delta(chi_c P_0) is O(r^(-2alpha-3)); its monopole vanishes because the fluxes through the
sphere of radius R are O(R^(1-2alpha)), and its dipole vanishes because the boundary terms are O(R^(2-2alpha)), which
uses alpha > 1 (c_l < 1/2). Its quadrupole is finite (|y|^2 |g| = O(r^(-2alpha-1)), integrable since 2alpha > 2). So the
pressure has no r^-1 or r^-2 term and the only pressure contribution at gradient rate 2alpha+1 is grad P_0. At c_l = 1/2
(alpha = 1) the dipole boundary term is O(1) and a pressure term of gradient rate 3 could appear.

### 2.5 Logarithms (resonances) [V, d03 arithmetic; mixed example V, derivations/consult_repro/mixed_resonance.log; both examples I]

A pressure term r^(-p+i nu) Y_l^m produces r^(-(l+1)) log r iff nu = 0, p = l+1 and its source projection is
nonzero; m is arbitrary (the radial frequency counts only the twisted indices of tail factors). Since 1/c_l and
2/c_l are never integers in the range, coincidences need n >= 3 tail factors and rational c_l: pure-tail ones at
c_l = n/K with 2n < K < 5n/2 (3/7, 4/9, 5/11, 5/12, 6/13, ...). Examples with nonzero coefficient at c_l = 3/7:
pressure r^(-5) log r (pure tail, l = 4; explicit case reproduced independently: omega = 1, poloidal tail
sigma = P_2(cos th), tau = 0, cubic source coefficient -860928/385 on r^(-7) P_4, hence pressure
-286976/1155 r^(-5) log r P_4, using -Delta(r^(-5) log r P_4) = 9 r^(-7) P_4; the P_3 tail has no degree-4 cubic
source by parity), and pressure r^(-10) log r with m = 2 from three tail factors and a
quadrupole (poloidal tail sigma = P_3(cos th), omega = 1; exact source coefficient
77883280853706560/25794632597097 - 165879152402176640 i/143712953040969). Velocity resonances occur only at k = alpha.
Endpoint coincidences (c_l = 1/2 with l = 1, c_l = 2/5 with l = 2) need not produce logs (at alpha = 1 the leading
dipole source cancels).

Practical rule: c_l = 3/7 and 4/9 are not fixed search points. On the grid the exact coincidences are at pressure
rate >= 18; c_l = 0.43 is within 0.023 in rate of the 3/7 coincidence (3/0.43 = 6.977), so any tail model term
within 0.05 of a coincidence uses the resonance-regular pair a (s^(-q) - s^(-(l+3)))/((l+3) - q), which tends to
a s^(-(l+3)) log s, and every omitted term is bounded by the next-order estimate from the fitted coefficients.

### 2.6 Consequences for representations

1. Radial channels. A single expansion that is smooth in a compactified variable (integer powers of 1/s times one
   envelope r^(-alpha)) cannot represent the rate 2alpha+1 (offset alpha+1 is not an integer) or the untwisted
   multipole rates (relative oscillation e^(-i m (omega/c_l) log r)); it shows up as O(1) far-shell nonlinear
   residual. Representations carry separate channels for alpha, 2alpha+1 and the multipoles (SPEC 4.4).
2. Rate bookkeeping. Regularized envelopes s = (r^2 + R_0^2)^(1/2), compactified variables and a regularized twist
   (omega/(2c_l)) log(1 + r^2/R_0^2) generate rates alpha + j and 2alpha + 1 + j that the exact expansion does not
   contain (alpha+1, alpha+2, alpha+3 and 2alpha+2 are all outside the exact set for 1 < alpha < 3/2). The linear
   operator multiplies their angular coefficients by c_l(alpha - k) != 0 and nothing else has that rate, so these
   coefficients must vanish in an exact profile [R; the alpha+2 case was proved and implemented by the independent
   route]. An uncancelled alpha + j term gives a far-shell nonlinear-balance ratio growing like r^(alpha+1-j).
   Near c_l = 1/2 the rates alpha+2 and 2alpha+1 nearly coincide (3.041 and 3.082 at c_l = 0.49), which makes the
   unconstrained fit ill conditioned.
3. Cancellation. In float64, direct evaluation of L U in the far field loses about eps_mach r^(alpha+1) relative
   to the nonlinear scale (measured: relative error about 96 at r ~ 1e9 with a smooth leading-tail basis; an
   analytically factorized potential-commutator form gives 3.4e-14 against 90-digit arithmetic) [I]. Far-shell
   diagnostics therefore evaluate L[U - r^(-alpha) F] algebraically, and sensitive cases are repeated in extended
   precision (SPEC 7.2).
4. Explicit constraints for a compactified Chebyshev basis [V, derivations/d17_tail_moment_check.py for k <= 8; R;
   I, CONFIRMED 2026-10-24T21:07Z by the independent route: own derivation, 16 cases at 70 digits, moment errors < 1e-60].
   With x = (s-R_0)/(s+R_0), s = (r^2 + R_0^2)^(1/2), a potential column r^l s^(-(a+l)) sum_k a_k T_k(2x-1)
   e^(i m psi) with psi = chi + (kappa/2) log(1 + R_0^2/r^2), kappa = omega/c_l, has, relative to its leading term
   r^(-a) (sum_k a_k) e^(i m chi), the expansion
       T_k(2x-1) = 1 - 4 R_0 k^2/r + R_0^2 (4k^2 + (8/3) k^2 (k^2-1))/r^2 + O(r^-3),
       s^(-(a+l)) = r^(-(a+l)) (1 - (a+l) R_0^2/(2r^2) + O(r^-4)),
       e^(i m psi) = e^(i m chi) (1 + i m kappa R_0^2/(2r^2) + O(r^-4)).
   Hence the relative order 1/r vanishes iff sum_k k^2 a_k = 0, and, given that, the order 1/r^2 vanishes iff
   (8/3) sum_k k^2(k^2-1) a_k = ((a+l)/2 - i m kappa/2) sum_k a_k (the sign of the imaginary part follows the
   twist convention of the code). The toroidal velocity curl(T y) uses only angular derivatives and the radial
   velocity of curl curl(S y) is proportional to the angular Laplacian of S, so for l >= 1 a velocity coefficient of
   a given twisted rate vanishes iff the corresponding potential coefficients do. Measured [I, independent route,
   exact rational sums of the stored coefficients]: the primary exchanged state at c_l = 0.45, omega = 1,
   omega/c_l = 20/9 has a nonzero sum k^2 a_k in all 24 toroidal and all 24 poloidal columns, and its rate alpha+1
   velocity coefficient has L2 norm 284 when ||F|| = 1. Its forbidden term exceeds the leading tail out to
   r of about 284 (R_0 = 1). Rows weighted by the five-term scale see only about 284/r of it, which is why far
   anchoring by momentum rows does not remove it. Since solver v5 (2026-10-24T20:50Z) the primary route eliminates the
   top two coefficients of each A/C column and the top coefficient of each B/D column (k^2 moment, rate 2alpha+2);
   with both moments cancelled the independent test measures a far decay slope within 7e-7 of 3. A single-coefficient
   B/D column is an edge case (its k^2 moment is already zero; the primary _solve_k2 would divide by zero).
5. Angular closure of the rate 2alpha+1 channel [R, lead degree count 2026-10-24T21:03Z; V, derivations/d18_G_degree_count.py;
   independent projection evidence I; I, independent proof with the sufficiency construction (curl(y x V_1) =
   [(2alpha-1) - (omega/c_l) L] V_1 inverted per degree) and the attaining example n_3^d e_3, 2026-10-24T21:23Z,
   reviewed by the lead in d18 section 6]. G[F] is quadratic in F, so its angular content is that of the square of
   the leading space. For a twisted potential of degree d, with F = curl A, the following hold on |y| = 1:
   - F has harmonic degree <= d+1, and F_r <= d (y.(y x H) = 0);
   - N = (DU_0)F, the coefficient of (U_0.grad)U_0 for the homogeneous leading field U_0, <= 2d+1, and the
     pressure source tr((DU_0)^2) <= 2d+2 (degrees of Cartesian components on the unit sphere);
   - hence G[F] <= 2d+3, and the correction potential must have degree 2d+2.
   All these bounds are attained (d = 1, 2, 3). The independent projection agrees: for F of degree 2 and 4,
   G[F] is carried to roundoff at correction degree 6 and 10, respectively, and to 1e-3 at degree 2d.
   For T/S scalars with leading l <= L and even m <= M_max, a sufficient correction set is
   B (toroidal) l <= 2L+3, D (poloidal) l <= 2L+2, and even m <= 2 M_max.
   If the correction set is smaller, the mismatch Delta = dist(G[F], carried span) > 0 for generic F. Then E_G does
   not decay, and far-checkpoint rho_nl tends to Delta_b/(RMS(T4) + RMS(T5)). A pointwise matching penalty with
   too small a correction space pulls F toward {Delta = 0}. This is a truncation effect; it is not a property of
   exact profiles. The bounds are stated in the SPEC twist convention; the d18 script uses the opposite sign of the
   twist, which the reflection y_2 -> -y_2 (omega -> -omega) maps over without changing degrees.
   Review: derivations/d18_nonlinear_tail_review.md.
   Exact elimination [I, independent construction theory/hard_tail_elimination, reviewed by the lead in d18 section 7,
   CORRECT under its range hypothesis]: with E the leading map, B the carried map, Z spanning ker E and M = BZ,
   a(z) = q + Z M^+ (G(Eq) - Bq), q = z/||Ez||, gives ||Ea|| = 1 and Ba = G(Ea) exactly when the defect lies in
   range M, and is idempotent; the composed Jacobian has a null space of dimension at least rank M + 1. It changes the
   core of a state, so a state built with it is a new approximation. Not yet implemented outside tests.
6. Exact exterior control of the primary representation [I, independent proofs; V, lead reviews
   derivations/d70_review_primary_tail_bounds.md, d71_review_leading_moments.md, d72_review_exterior_integrals.md,
   2026-10-25T07:14Z to 07:33Z]. For a finite sum of primary channels with fixed coefficients and leading field U0
   (A and C at their endpoint sums, s replaced by r): (a) |U - U0| <= sum_j u_j r^(-b_j) and |Omega - Omega0| <=
   sum_j o_j r^(-b_j - 1) for r >= R with explicit Cauchy constants; rates alpha + 1 (only through q'(1) of A and
   C), alpha + 2, 2 alpha + 1 (B, D), l + 2 (E). The constants depend strongly on the disk radius rho in w = R0/r;
   choose rho per R. (b) int |F|^2, H_F, the enstrophy moment, e_F and N_F are exact quadratic forms in the endpoint
   sums (sign of the k (2 - alpha) Y term fixed by the export's twist and sine convention). (c) The signed exterior
   helicity beyond R lies in t(R) H_F -+ B_H(R), t(R) = R^(2 - 2 alpha)/(2 alpha - 2); the absolute exterior
   helicity in [max(0, t |H_F| - B_H), t (int |F|^2 int |H|^2)^(1/2) + B_H] (upper endpoint slack 1.4 to 2.6 on the
   exports). On the nine exports at R = 2^28: omitted energy at most 2.0e-6, omitted helicity at most 2.3e-14,
   max q'(1) 1.73e-11. These are statements about the representation; they enclose no finite-ball quadrature and use
   no equation. An export without the endpoint constraint would fall to the R^(2 - 2 alpha) rate: report q'(1).

### 2.7 Far-field tests for every candidate (SPEC 7.7, 7.11)

- E_F(r): relative S^2 distance of r^alpha U (untwisted back) from F, expected O(r^(-(alpha+1)));
- E_G(r): relative distance of r^(2alpha+1)(U - r^(-alpha) F) from G[F] computed from the candidate's own F,
  expected O(r^(2alpha-3)) (faster after subtracting the fitted l = 2 multipole); absolute defect when G[F] is
  degenerate; fitted C_2m compared with the finite-part source moment;
- E_H(r), E_D(r): the same for vorticity against H and for DU against the derivative of the leading tail;
- X1-X5: diagnostics before analytic closure; jumps of U, DU, D^2 U at the matching radius; matching radius moved by
  a factor 4 each way; independent full-pressure evaluation at far checkpoints; systematic maximization of |R_u|,
  |R_Omega| in every far shell (4096 random points plus local maximization from the 20 worst);
- K_1 (2.2): the ratio K_carried/K_required of the carried to the required rate-(2alpha+1) energy coefficient, with
  K_required = 2 int F . G[F] = 2 (2 - 3alpha) Phi_F; exact value 1. Evaluate it directly from the coefficient formulas
  at unit radius, not from E(s) at a finite radius: subtracting the last sampled E(s) and multiplying by s^(alpha+1)
  amplifies the offset. It tests one projection of the vector defect of G and does not replace it. Independent values
  on eight primary exports (2026-10-25T06:38Z and 06:51Z): -3.25, -15.2, -434, -2835 on the D6-lineage states with
  rate-(2alpha+1) channels, -8.98 on the degree-6 nest rung at omega = 0.3 and -32.6 on the one at omega = 1 (07:35Z), 0 on the three without them; the finite-radius estimates of d67 (-3.2 to about -1800) are diagnostics only;
- K_H (2.2): the helicity analogue of K_1, K_carried/K_required with K_required = (1 - 3alpha) Psi_F and
  K_carried = int_(S^2) (U_0 . curl V_1 + V_1 . Omega_0) for the rate-(2alpha+1) part V_1; exact value 1. Theory-route
  values on eight exports (d78): +1.26, +1.21, +4.24, +2.19, +1.07 and +0.18 on the six with rate-(2alpha+1) channels,
  0 on the two without; all eight confirmed by the independent route (2026-10-25T09:56Z and 10:13Z). The energy
  ratios of the same states are -32.6 to +29.7. A different projection of the same vector defect; it does not replace
  K_1 or the defect of G. Cauchy-Schwarz gives |K_1 - 1| <= m / c with m the relative L2 defect of G and c the cosine
  of G_required against F (0.007 to 0.044 here); on the six states 33 to 91 per cent of the squared defect is
  orthogonal to F (independent route, 10:15Z), so the defect is not only a radial modulation of the leading tail.
  The primary route's own implementation (10:23Z) reproduces all eight rows to 4e-12 relative; on the two degree-8
  D6-lineage states (primary-route values only) m = 4.4 and 4.3 with helicity ratios 1.39 and 1.60.
- E_G small does not imply a small nonlinear residual and vice versa; both are required.
Values generated from the analytic tail model alone count as model values, never as evidence of resolution.

## 3. Origin

### 3.1 Conditions [V, d03; I]

With u_0 = U(0), M = DU(0), T_ijk = d_j d_k U_i(0):

    order 0: tr M = 0, (1-c_l) u_0 + M u_0 + omega J u_0 + grad P(0) = 0;
    order 1: sum_i T_iik = 0 (k = 1, 2, 3), M + M^2 + omega (J M - M J) + (u_0.grad) DU(0) + Hess P(0) = 0.

The antisymmetric part of order 1 is the order-0 vorticity equation. Under the two-fold symmetry u_0, grad P(0)
and Omega(0) are vertical and M is block diagonal; u_0 = 0 is not imposed. The pressure at the origin is the
full-space pressure, so these conditions couple the core to the whole field through P(0)-derivatives.

### 3.2 Regularity of the representation

Potentials are solid harmonics r^l Y_l^m times smooth functions of r^2 (Cartesian polynomials times radial
functions of r^2), so U is smooth through the origin and the axis by construction. The twist factor
e^(i m psi(r)) with psi = (omega/(2c_l)) log(1 + r^2/R_0^2) is smooth in r^2 and nonvanishing, and the curls are
taken exactly, including psi' and psi''. An r-dependent rotation of an already divergence-free field is not used,
because it does not preserve the divergence.

### 3.3 Audit procedure (SPEC 7.6)

R_u, D R_u and D^2 R_u are evaluated exactly at y = 0 in the regular basis (automatic differentiation or exact
formulas), not by omitting r = 0. The reported ratios are tau_j = |D^j R_u(0)| / max(sum_i |D^j T_i(0)|, 1e-3 S_j),
j = 0, 1, 2, with the momentum terms T_i and the floor S_j = U_c r_core^(-j)(1 + U_c/r_core), U_c = max|U|; the
floor turns the 0/0 case (for example u_0 = 0) into an absolute test. Independent manufactured tests with nonzero
U(0) check the constant-order formula, every linear and quadratic residual coefficient at 0, and fourth-order
finite differences (minimum Hessian discrepancy about 1.3e-9; quadratic Taylor remainder falls by about 8 when the
radius halves) [I]. These tests validate the audit, not any trained state.

Full-space pressure at the origin [I, implementation confirmed 2026-10-24T20:06Z]. The independent route now
computes the decaying pressure's Taylor coefficients at y = 0 through degree 3 from full-space solid-harmonic
moments of the source tr((DU)^2), with the singular inner part of each moment integral replaced by the analytically
integrated local Taylor expansion of the source, and extracts the momentum residual jets through order 2 by exact
polynomial algebra. On a manufactured decaying pressure the coefficient error falls from 8.73e-6 to 8.75e-10 as the
inner cutoff goes from 0.03 to 0.003 (fourth order, as predicted); velocity jets through order 3 agree with
automatic differentiation to 2.3e-16 relative. Pressure harmonics through degree 3 suffice for the residual jets
through order 2. The moments are numerical integrals, not interval bounds.

## 4. Open items

- Existence of a complete far-field expansion with a controlled remainder (formal only).
- Size of omitted high-order and logarithmic terms for each candidate (to be bounded from fitted coefficients).
- State-level results added 2026-10-25T02:04:07Z (c_l = 0.45, omega = 0.3, omega/c_l = 2/3 throughout; all states are
  unvalidated approximations below the discovery tier):
  (a) Angular closure of the rate 2alpha+1 channel, primary code [primary-reported; agrees with I]: the primary route's
      own implementation of G[F] (automatic differentiation of the closed-form leading field, mode-by-mode twisted
      pressure) gives ||G[F]|| = 0.609959 for ||F|| = 1 on its degree-6 descendant of the independent degree-6 state,
      against the independent value 0.6099595. The degree-L span misses 14 per cent of G[F]; the span of 2.6(5)
      (B up to 2L+3, D up to 2L+2) contains it to 7e-14. This confirms the degree count of 2.6(5) in a second code.
  (b) Carried-coefficient mismatch [primary-reported 1.419 and correlation 0.157; independently 1.42 and 0.16]: in the
      first primary state with the full span of 2.6(5), ||G_required - G_carried||/||G_required|| = 1.419 and the two
      coefficients have correlation 0.157. So the span carries G[F] exactly but the optimizer did not set the
      coefficient; by 2.2 this is the whole rate-(2alpha+1) residual coefficient. Its far-shell rho_nl rises to 0.56 at
      r = 2e4 (primary-reported), the level 2.6(5) predicts for a fixed mismatch. Rows tying the carried coefficient to
      G[F] are under test.
  (c) Origin structure of the independent ladder states [lead reading of verifier samples, derivations/d31; I,
      CONFIRMED 2026-10-25T01:47Z, six rows to 5.3e-13]: every state has an axial jet u_z(0) = 2.2 to 3.1 and a
      stretching rate Omega.S Omega/|Omega|^2 = 7.5 to 24 at the origin, balanced by axial advection; the exact origin
      condition of 3.1 is violated by |R_Omega(0)|/|Omega(0)| = 0.19 to 1.69. The origin is not a critical point of
      |Omega|^2 in these states (d Omega_z/dz != 0), so the critical-point strain identity does not apply there.
  (d) Backward vorticity transport of the released degree-6 state [I, 2026-10-25T01:51Z]: the residual-corrected
      transport identity closes to 2e-7 with fourth-order step convergence, while the uncorrected identity, exact for a
      profile, fails by 0.66, 0.92 and 1.00 at times 0.25, 0.5, 1.
  (e) Matched intermediate region [FINAL_REPORT section 2, item 21; proved in both routes]: an ordinary homogeneous
      steady field of degree -alpha (1 < alpha < 2) has a nonnegative Bernoulli sphere function with zeros at critical
      points, and vanishes in the Beltrami, irrotational, axisymmetric, tangential and zero-radial-vorticity classes and
      under an integrability condition on h. A strongly concentrated core matched through a region where the field is
      close to such a field would need one outside these classes. For fields homogeneous under dilations combined
      with rotations about e_3 (twist k) the same conclusions hold for every k, with V = v - k b X and W = w - k zeta X
      (derivations/d42; I, confirmed by the independent route 2026-10-25T02:27Z; FINAL_REPORT section 2, item 22); the
      profile tail is the case k = -omega/c_l. No asymptotic overlap region has been established in the saved states
      (core radius 0.15, outer radius 1: best two-sided scale separation 2.58, at an optimally chosen radius).
  (f) Edge c_l -> 1/2 and the energy law [I for the rigidity, the energy identity and the exact swirl identities,
      confirmed by the independent route 2026-10-25T02:38Z (FINAL_REPORT section 2, item 23); I since 2026-10-25T03:13:16Z for
      the swirl normalization a = (A eps)^(1/(alpha+1)), the core-radius asymptotic and the exact maxima
      (max|Omega| = 2/eps; a_eff = 0.096566 at c_l = 0.45; lead check derivations/d48*); R for the shell
      asymptotics (FINAL_REPORT section 2b, item 1); derivations/d43]: degree -1 twisted
      steady fields vanish (second proof); an explicit smooth axisymmetric escape with an exact unit-gauge tail has
      rho_u^max = Theta(1/2 - c_l) and a core of radius a ~ (1/2 - c_l)^(1/2) (log)^(-1/4), so a fixed core ball stops
      resolving it near the edge (0.45 a at c_l = 0.45, 1.21 a at c_l = 0.48, 2.47 a at c_l = 0.49, from
      derivations/d43_core_scale.log, reproduced by d48b_swirl_rcore.log); SPEC v1.21 adds core-resolution sets at a_eff = 2 sqrt2 max|U|/max|Omega| and
      near-edge stability checks. For an exact profile in the tail class the finite part of the energy vanishes
      (E_ren = 0, from int U.R_u = beta_0 E_ren); E_ren and both sides of the ball energy identity are reported without
      threshold (SPEC v1.21(e)). At c_l = 2/5 a unit tail is impossible.
  (g) Backward-transport inverse [V, derivations/d45_backward_inverse_check.py; MATHEMATICAL_FORMULATION section 7,
      item 19]: with Phi_s y = e^(c_l s) R(-omega s) y, G f(y) = int_(-inf)^0 e^((1-c_l)s) R(omega s) f(Phi_s y) ds
      inverts L on fields bounded near the origin, so a profile is a fixed point U = -G N(U) whose tail is an output
      of the core, and U - T(U) = G R_u. In spherical components G is a radial integral along twisted rays
      (theta and chi = phi + (omega/c_l) log r fixed), (G f)_sph = (1/c_l) r^(-alpha) int_0^r rho^(alpha-1) f_sph d rho,
      and the tail coefficient of G f is the full ray integral F_f; for smooth U the truncated ray integral of L U is
      R^alpha U_sph(R, .) [V, derivations/d46_spiral_ray_check.py and d46_ray_identity_check.py; R for the consulted
      answer, derivations/d46_backward_formulation_audit.md; I since 2026-10-25T03:08:19Z: independent proof and 63 controls
      of the verifier, G L V = V to 3.9e-15, time and radius forms to 1.4e-15]. A profile's tail is therefore generated by its core:
      F_U = -F_(N(U)). SPEC v1.22 reports the tail-generation defect tau_F = ||F_(R_u)|| / ||F_U|| and the backward
      defect RMS(G R_u)/RMS(U) without threshold; for the pure-swirl escape of (f) both are at least about 1.
- State-level tail generation [R, lead computation from primary exports, derivations/d49_tauF_deltaG.md,
  2026-10-25T03:21:44Z; awaiting the independent evaluation]: on the five saved D6-lineage states (c_l = 0.45, omega
  = 0.3, omega/c_l = 2/3, degrees 6 and 8) tau_F = 0.898 to 0.968 at R = 2^20 r_core (converged from 2^10 r_core),
  ||F_(N(U))|| = 0.74 to 0.84 at cosine -0.41 to -0.52 with F_U; the backward defect is 0.90 to 0.97 in every shell
  beyond r_core. The defect is built between r_core/4 and 4 r_core. The far shells follow the imposed tail, which the
  core does not generate. By azimuthal mode (derivations/d49b_tail_modes.md, 2026-10-25T03:32Z, three of the states):
  the imposed tail is 82 to 84 per cent mean (m = 0) swirl in squared norm. The ray-integrated nonlinear mean
  azimuthal term has norm 0.23 to 0.31 of the required amplitude, with signed projection 0.15 to 0.24 [corrected
  2026-10-25T04:12Z; the earlier wording said the core supplies 0.23 to 0.31]. This entry carries 63 to 68 per cent
  of tau_F^2. In an exact profile the mean swirl of the tail can only be generated by the eddy angular-momentum
  flux along the nonlinear mean flow c_l y + M [I, MATHEMATICAL_FORMULATION.md item 20]. The ordinary ray integral
  also contains mean-meridional transport [I, independent pressure-free identity, reviewed by the lead,
  derivations/d57_pressure_free_mean_swirl_review.md].
- Mean-swirl generation test [R, lead computation from primary exports, derivations/d55_swirl_generation.md,
  2026-10-25T04:12Z; awaiting the independent evaluation]: an exact profile has Q_sw = (1 - 2 c_l) max|Gamma_0| / max|S|
  <= 1. The state with the smallest tau_F, nest4_L4_cl0.45_om1.0_p0 (c_l = 0.45, omega = 1, omega/c_l = 20/9,
  tau_F 0.66, tail 96 per cent m = 0, core eddy energy fraction 1.6 per cent), has Q_sw = 2.0, and the part of its
  mean swirl generated along W_0 trajectories by its eddies is anti-aligned with Gamma_0. Its tail agreement is
  therefore carried by the residual of a near-axisymmetric swirl state; it is not evidence of a near-profile. The
  D6 lineage has Q_sw 0.15 to 0.29. The weighted bound of MATHEMATICAL_FORMULATION.md item 21 (c) holds with a
  margin of 90 to 1000 on all three states (derivations/d58_eddy_norms.md) and does not discriminate.
- Candidate-level results: none yet (no state has reached the discovery tier). In Stage I (as reported by
  the primary route, not yet independently checked) every plain least-squares start converged to a weak
  axisymmetric state whose tail onset lies far outside its core (r_tail/r_core about 300); the far-field tests
  above are meaningless for such a state, which fails the nontriviality guards before any tail test.
- State-level origin result [I, 2026-10-24T20:27Z snapshot]: on the independent route's best full-volume state (projected
  pressure, two-fold symmetric degree 2, c_l = 0.45, omega = 0.3, omega/c_l = 2/3), the origin ratios are
  tau_0 = 0.00197, tau_1 = 0.0274, tau_2 = 0.0706; the pressure Taylor coefficients agree to 8.4e-11 between two
  radial and angular resolutions, and the quadratic residual remainder falls by a factor of about 8 per halving of
  the radius. The origin conditions of 3.1 are therefore violated by amounts well above discretization error: the
  state is not an exact profile at the origin.
- State-level far-field behaviour [primary route report, not independently checked]: before far anchoring, the
  Sigma_Z = 1 states of the primary route were not tail-like within the sampled radii (E_F > 0.1 up to r = 2000,
  nonlinear ratios up to 1e6 in far shells), because the representation's x = 1 limit F differed from the field
  at the last radial nodes. Momentum rows at r = 4096, 16384, 65536 R_0 were added (as extra nodes of the main
  grid) and the anchored states report tail onset r_tail between 470 and 1900. E_G, E_H, E_D and X1-X5 have not
  yet been reported on any primary state; they are required before any discovery-tier claim (SPEC 7.7, 7.11).
  Independent diagnosis [I, 2026-10-24T20:29Z]: the exchanged primary state (c_l = 0.45, omega = 1,
  omega/c_l = 20/9, before the anchored runs) carries a forbidden rate alpha+1 term of coefficient norm 284
  (||F|| = 1), which by 2.6(4) dominates the leading tail out to r of about 284 and explains its late tail onset;
  the exact constraints of 2.6(4) were requested at 20:39Z. Its off-grid pressure gradient is also inaccurate
  (3.4e-3 relative; quadrature endpoint defect), so its holdout momentum values are not yet validated.
- State-level E_G [independent route's fresh evaluation files, 2026-10-24T20:33Z; not yet in its report]: on the two best
  independent states (degree 2 released and degree 4 with stretching guidance, c_l = 0.45, omega = 0.3), E_F, E_D
  and E_H decay at the predicted rate (E_F about 1e-12 at r = 2e5), but E_G levels off near 0.1 (0.074 at r = 49
  rising to 0.115 at r = 2e5 for degree 2; 0.071 at r = 364 and 0.101 at r = 1.9e5 for degree 4) instead of
  decaying like r^(2alpha-3). The far-shell nonlinear ratio rho_nl is correspondingly 0.03 to 0.07 for
  16 < r < 1024. So the r^(-(2alpha+1)) part of these states is not the state's own G[F]: about 10 percent of it is
  wrong. [V, derivations/d16_far_G_spectrum.py] G[F] of these states has 0.09 percent (degree 2) and
  0.21 percent (degree 4) of its S^2 energy above Cartesian degree d+1, the highest degree that the rate-2alpha+1
  channel built from degree-d monomials carries. At most 3 to 5 percent in amplitude is unrepresentable, so the
  mismatch is mainly in the fitted channel coefficients, not in the channel's angular content. Remedy: momentum
  rows at radii far beyond 1e3, or channel coefficients tied to G[F] by linear constraints.
  [V, derivations/d16_far_G_consistency.py] The G[F] used in these E_G values was checked by the lead from the
  exported F, DF, Q, grad Q on S^2: G = (U_0.grad)U_0 + grad(r^(-2alpha) Q) at r = 1 (exact to rounding, with
  DF[i,j] = d_j U_i), Q satisfies -Delta(r^(-2alpha) Q) = tr((DU_0)^2) r^(-2alpha-2) with the twisted multiplier
  (-2alpha + i m omega/c_l)(1 - 2alpha + i m omega/c_l) - l(l+1) for every (l, m), l <= 10, to 5e-15, and the radial
  component of grad Q equals -2alpha Q + (omega/c_l) d_chi Q to 3e-15. This checks the G[F] formula and its
  pressure, not the extraction of F and DF from the state (which E_F and E_D test).
