# Mathematical formulation

Rotating backward self-similar profiles of the unforced 3D incompressible Euler equations, 2/5 < c_l < 1/2,
omega != 0. This file states the equations, conventions, exact identities, symmetries, gauges, origin and pressure
conditions, and the proved global facts that the campaign uses or reports. The binding working specification
(diagnostics, thresholds, change log) is SPEC.md; the far-field expansion and the origin conditions are treated
in detail in FAR_FIELD_AND_ORIGIN_AUDIT.md.

Status labels used below:
- [V] verified by an executed exact symbolic or numerical check (script named; all in derivations/ unless said);
- [I] confirmed by the independent validation route of the campaign;
- [P] proof reviewed line by line, independent validation pending (not used as a search input until confirmed);
- [C] search assumption or conjecture.

Last update: 2026-10-26T08:06:01Z (verifier audit of 2026-10-26T08:03:16Z: item 21 (b) split into the exact-profile equality and the independently proved residual identity with its decay hypotheses; item 27 (e) dipole remark restated with its independent proof); 2026-10-26T07:59:01Z (section 7 synchronized with FINAL_REPORT.md section 2: new items 27 to 30 from report items 29, 32, 35 and 36; supplements with the report hypotheses and scopes to section 3 item 3 and section 7 items 2, 6, 7, 8, 11, 12, 14 to 19 and 21 to 26; item 1 restated from the standalone finite-energy proof; completeness of the two tail potentials in item 6; item 23 A > alpha; item 12 (b) exactly divergence-free; item 18 (b) consulted ratio asymptotics marked; item 8 Lyapunov clause restricted to fixed constants; item 19 (c) pointer to item 2; item 21 (b) residual form marked as a lead derivation; hypothesis map in "Not available"); 2026-10-26T07:16:47Z (item 11 and section 7 'Not available': CIV Thm 2.1 is a physical-time statement without similarity ansatz, Thms 3.9 and 4.5 with their hypotheses, B. Pineau; item 12 (e) subsequential limit; wording only, following the source audit of FINAL_REPORT.md section 2, item 5); 2026-10-26T01:27:06Z (references made neutral: no consultation tags or team-internal names; no content change); 2026-10-25T09:42:59Z (item 26 now [I], remainder proved under the hypothesis of item 24 by the flux equation, d81); 2026-10-25T09:28:58Z (item 26, first far-field helicity coefficient, d78); 2026-10-25T06:56:26Z (items 24 and 25 added from report section 2 items 30 and 31, d68, d69); 2026-10-25T05:05:46Z (item 23 now [I] with the decay hypothesis and A >= alpha, report pointer section 2 item 28; 2026-10-25T04:34:42Z item 21 now [I], scope of (a) and (c) explicit, report pointer section 2 item 27; 04:32:49Z item 23 constructive non-axisymmetry threshold [P] from the audit of a consulted answer; item 21 (c) wording: M bounds the mean meridional velocity; 04:12:31Z item 22 pressure-free mean-swirl defect [I]; 04:03:44Z item 21 mean angular-momentum consequences [P] from the audit of a consulted answer; item 20 now [I] after the independent proof, trapping statement corrected to finite entry into every larger ball; 03:31:55Z item 20 eddy generation of the mean swirl added [V/pending]; item 19 (g) wording corrected; 03:08:19Z item 19 extension now [I] after the independent proof, with the Fredholm and escape scope qualified; 02:52:49Z item 18 now [I] except the consulted shell asymptotics, and (c) qualified; item 19 extended [P] from the audit d46 of a consulted answer; 02:34:25Z literature paragraph: Xue wording aligned with the report, R3 title; 02:32:54Z item 17 twisted case now [I]; 02:30:24Z items 18 [P] and 19 [V] of section 7 added; 02:16:11Z item 17 twisted case added [P]; earlier: items 14 to 17 of section 7 and the lower-multipole statement of section 5 added;
the full statements are FINAL_REPORT.md section 2, items 18 to 21).

## 1. Equations and conventions

Unknowns U: R^3 -> R^3 and P: R^3 -> R. Parameters 2/5 < c_l < 1/2 and omega != 0. With J y = (-y_2, y_1, 0)
(J v = e_3 x v) and

    W = (c_l I - omega J) y + U,

the profile equations are

    R_u     := (1-c_l) U + (W.grad) U + omega J U + grad P = 0,
    R_div   := div U = 0,
    R_P     := -Delta P - sum_ij (d_i U_j)(d_j U_i) = 0,       P -> 0 at infinity (full-space solution),
    R_Omega := Omega + (W.grad) Omega + omega J Omega - (Omega.grad) U = 0,   Omega = curl U.

The last equation is a consequence: curl R_u = R_Omega + Omega div U for every smooth U [V, d01].

Notation: alpha = (1-c_l)/c_l, so 1 < alpha < 3/2 and 1/c_l = alpha + 1; spherical coordinates (r, theta, phi)
with theta the polar angle; chi = phi + (omega/c_l) log r (twisted azimuth); spherical components refer to the
local basis (e_r, e_theta, e_phi); y_h = (y_1, y_2, 0); k = 1 - 2c_l > 0; V = c_l y + U; ell = (J y).U (axial
angular momentum density); K = |U|^2/2; h = U.Omega (helicity density); S = sym DU.

Physical solution [V, d01]. With tau = T - t, s = -log tau and E(s) = exp(omega s J), the field

    u(x, t) = tau^(c_l - 1) E(s) U(E(s)^T x tau^(-c_l)),   p(x, t) = tau^(2c_l - 2) P(E(s)^T x tau^(-c_l)),

solves the Euler equations if and only if R_u = 0 and div U = 0; it blows up at time T while rotating about e_3
at the constant rate omega in s. In the rotating similarity variables V(z, s) = E(s) U(E(s)^T z) satisfies
d_s V + (1-c_l) V + (c_l z + V).grad V + grad Pi = E(s) R_u(E(s)^T z), which is time-periodic in s with period
2 pi/|omega| (pi/|omega| under the two-fold symmetry of section 3; these are periods, not necessarily minimal).

Target (from the problem statement): U, P smooth through the origin and the rotation axis (C^2 at least, more for
every derivative used in residuals), genuinely non-axisymmetric, nonzero, and uniformly decaying at infinity.
Axisymmetry, reflection symmetry across z = 0, absence of swirl and U(0) = 0 are not imposed.

## 2. Exact identities [V, d01 with generic functions; the energy and helicity forms need div U = 0]

1. div W = 3c_l + div U; curl W = Omega - 2 omega e_3; R_Omega = (1+c_l) Omega + [W, Omega], with the Lie
   bracket [W, Omega] = (W.grad) Omega - (Omega.grad) W.
2. Bernoulli form: R_u = grad Be - W x Omega + k (c_l y + U), with
   Be = |W|^2/2 + P + c_l(c_l - 1)|y|^2/2 - omega^2 |y_h|^2/2.
   The term k(c_l y + U) = k(W + omega J y) contains the non-gradient part k omega J y. In terms of
   H_0 = |V|^2/2 + P + c_l(c_l - 1)|y|^2/2 = Be + omega ell:
       W.grad ell = -k ell - d_phi P + (J y).R_u,
       W.grad H_0 = -k |V|^2 - omega d_phi P + (W + omega J y).R_u    [V, d06].
   The pressure torque d_phi P has no sign; this is why the non-rotating Bernoulli-Lyapunov argument does not
   transfer.
3. Energy density: U.R_u = (2-5c_l) K + div(W K + U P).
4. Helicity density: Omega.R_u + U.R_Omega = (2-4c_l) h + div(W h + Omega (P - K)).
5. Vorticity amplitude: Omega.R_Omega = |Omega|^2 + W.grad(|Omega|^2/2) - Omega.S Omega [V, d01, d06]. Along the
   flow of W, d/ds |Omega|^2 = 2 Omega.S Omega - 2|Omega|^2 for an exact profile. At every critical point of
   |Omega|^2 (in particular at every local maximum), Omega.S Omega = |Omega|^2; at a nonzero maximum, lambda_max(S) >= 1. (Decay of U alone does not guarantee that
   the maximum is attained; the differentiated tail assumption of section 6 does.) The critical-point statement
   is [I] for C^2 exact profiles; at a numerically located critical point the transport term must be measured.
6. Rotation generator: J U - (J y.grad) U = -d_phi of the spherical components at fixed (r, theta). It vanishes
   exactly for axisymmetric U, and it is the basis of the non-axisymmetry diagnostics.
7. Virial identity [V, d05]: y.R_u = (1-5c_l) y.U - |U|^2 - 3P + div(W (y.U) + P y) - (y.U) div U.

## 3. Symmetries, reductions and gauges

1. Rotations about e_3 (U -> R U(R^T y), P -> P(R^T y), R = exp(b J)) preserve (c_l, omega) [V, I].
2. Dilations U_L(y) = L U(y/L), P_L(y) = L^2 P(y/L) give R_u[U_L](y) = L R_u[U](y/L) and preserve (c_l, omega)
   [V, I]. The tail coefficient transforms as F -> L^(1+alpha) F(theta, chi - (omega/c_l) log L).
3. The reflection y_2 -> -y_2 (S = diag(1, -1, 1), S J S = -J) maps a solution with omega to one with -omega [V, I].
   The search therefore uses omega > 0; negative-omega runs are kept only as code regression tests. With U_new(y) = S
   U(S y), P_new(y) = P(S y), the law holds for residuals of arbitrary fields, not only solutions (the report states
   it for C^4 divergence-free U and C^3 P) [I, independent proof; V, lead review derivations/d73_review_reflection.md,
   2026-10-25T07:45Z]: R_u_new(y) = S R_u(S y), Omega_new(y) = -S Omega(S y), K(U_new)(y) = -S K(U)(S y), h_new(y) =
   -h(S y). Norms, residual ratios on mirrored sets, energy fractions, N_F, e_F and E_ren are unchanged; signed
   helicity, H_F and H_tot change sign. Primary basis: negate omega, the cosine columns of the toroidal blocks A, B
   and the sine columns of the poloidal blocks C, D, E (T in curl(T y) is a pseudoscalar, the poloidal potential a
   scalar) [V, derivations/d73b_primary_mirror.log, exact on nine exports]. Consequence: a state and its mirror are
   one branch, and the helicity sign of a state is a statement about sign(omega) H_tot.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 33) [I: independent proof with its own
   regression, reviewed with separate symbolic checks and an end-to-end check; recorded 2026-10-25T07:45Z]. The law is
   stated for C^4 divergence-free U and C^3 P on R^3 (no equation assumed), with c_l unchanged, so omega/c_l changes
   sign. Every Euclidean norm of U, DU, Omega and R_u is unchanged, and so is the absolute helicity. In the Cartesian
   vector-potential basis of the independent validation route the reflected state is realized by negating omega and
   multiplying the coefficient of vector component j and monomial x^a y^b z^c by -S_jj (-1)^b. Every statement about
   states at omega > 0 therefore transfers to omega < 0 with the sign of the helicity reversed; a sign of omega H_tot
   observed on computed states is a finding about those states, not a consequence of the equation.
4. The reflection Z = diag(1, 1, -1) commutes with J and maps solutions to solutions with the same omega. It is
   not imposed. A candidate and its Z-image may be equivalent through an axial rotation without being
   Z-symmetric, so distinctness is tested by the gauge-orbit distance d_Z (SPEC 2.4).
5. Two-fold equivariance under exp(pi J) is imposed in the primary search: only even azimuthal wavenumbers m
   (m = 0 included) in the spherical components. Under it u_0 = U(0) and grad P(0) are vertical, DU(0) is block
   diagonal and Omega(0) is vertical [V, d03]. Odd m are admitted in a documented part of the budget.
6. Axisymmetric reduction [V for the algebra]: if U is axisymmetric, the rotation generator vanishes and omega
   drops out of R_u, so an axisymmetric profile is a non-rotating one. Genuinely rotating profiles must be
   non-axisymmetric; the search requires and monitors non-axisymmetric content.
7. Gauges. Exactly one dilation gauge, integral_{S^2} |F|^2 dS = 1 (or a core-scale gauge with integral |F|^2
   monitored and every reported number converted), one azimuthal phase gauge (argument of one pivot m != 0
   coefficient, or minimum-norm steps along the rotation null direction), and the pressure constant P -> 0.
   No additional normalization of vorticity, DU(0) or the core radius.

## 4. Origin

Regularity: the representation is smooth in Cartesian coordinates (solid harmonics r^l Y_l^m times smooth
functions of r^2 for the potentials). The local conditions at y = 0, with u_0 = U(0), M = DU(0) and
T_ijk = d_j d_k U_i(0), are [V, d03]

    order 0:  tr M = 0,   (1-c_l) u_0 + M u_0 + omega J u_0 + grad P(0) = 0,
    order 1:  sum_i T_iik = 0 (k = 1, 2, 3),
              M + M^2 + omega (J M - M J) + (u_0.grad) DU(0) + Hess P(0) = 0,

whose antisymmetric part is the order-0 vorticity equation. Order 2 is obtained by differentiating R_u twice. The
numerical audit evaluates R_u, D R_u and D^2 R_u at y = 0 exactly in the regular basis rather than omitting r = 0
(FAR_FIELD_AND_ORIGIN_AUDIT.md, section 3).

## 5. Pressure

P is the decaying full-space solution of -Delta P = tr((DU)^2) = d_i d_j (U_i U_j); no harmonic pressure is added
or fitted, and no condition is imposed at a finite radius. The divergence of R_u gives -Delta P = tr((DU)^2) for
any pressure of an exact profile, because the divergence of the linear terms vanishes
(div(J U) = div((J y.grad) U) = tr(J DU)); hence any decaying pressure of an exact decaying profile equals the
Riesz-transform pressure (for the decay classes of section 6, P = Q + const with Q the Riesz pressure, the constant
fixed by P -> 0) [I; uniqueness modulo constants by harmonic averaging]. Moreover div R_u = -R_P exactly whenever
div U = 0 [V, d08], so the pressure equation is equivalent to the divergence of the momentum equation.

Green formula per spherical harmonic (orthonormal Y_l^m in the true azimuth phi, f_lm = integral f conj(Y_l^m) dS)
[V, d03]:

    P_lm(r) = (1/(2l+1)) [ r^(-l-1) integral_0^r s^(l+2) f_lm(s) ds + r^l integral_r^inf s^(1-l) f_lm(s) ds ].

Beyond the last resolved radius the exterior integral uses the analytic tail term by term:
integral_R^inf s^(1-l) a s^(-p-2+i nu) ds = a R^(-l-p+i nu)/(l+p-i nu). Pressure multipole coefficients are finite
parts of the source moments (FAR_FIELD_AND_ORIGIN_AUDIT.md, section 2.5).

Lower multipoles [I; lead proof derivations/d38 section 3, confirmed by the independent route 2026-10-25T01:15Z]. If
U = U_0 + U_r for r >= 1 with U_0 the twisted-homogeneous leading field and |U_r| = O(r^(-alpha-1)),
|DU_r| = O(r^(-alpha-2)), then grad P = grad P_0 + O(r^-4), where P_0 = r^(-2 alpha) Q is the unique
twisted-homogeneous pressure coefficient. The monopole and dipole moments of the remainder source vanish because
alpha > 1 (c_l < 1/2), so P has no r^-1 or r^-2 term; at alpha = 1 the dipole boundary term is O(1).

## 6. Search class (an assumption, not a theorem) [C]

The primary class consists of profiles with a smooth, differentiable leading tail

    U = r^(-alpha) F(theta, chi) + r^(-(2alpha+1)) G[F](theta, chi) + (pressure multipole and higher terms),

whose expansion may be differentiated term by term. The leading rate alpha is the unique rate at which the linear
part of R_u annihilates a twisted homogeneous field; the decay dichotomy of section 7 shows that, under uniform
O(r^(-alpha)) decay, no nonzero profile decays faster [I]. The dichotomy gives a positive normalized energy
limit, not a pointwise angular profile, so the existence of F is part of this assumption. A complete expansion with a controlled remainder is not
established by these formal arguments.

## 7. Proved global facts

1. Finite energy is excluded [V for the identities; I, with a standalone independent proof of 2026-10-26 reviewed by
   the lead]. Let c_l > 0, omega real, U in C^2 divergence-free, bounded and in L^2, with the full-space pressure P =
   Q + constant, Q_hat(xi) = -sum_ij (xi_i xi_j/|xi|^2) (U_i U_j)_hat(xi). If U.R_u is absolutely integrable, then
   integral_{R^3} U.R_u = (1 - 5c_l/2) integral_{R^3} |U|^2: in the cutoff form of the energy density
   (section 2, item 3) the rotation flux vanishes by radiality, the dilation flux is bounded by the annular L^2 mass,
   and the nonlinear and pressure fluxes carry a factor 1/R (Q in L^2), so no selection of radii is needed. Hence an
   exact profile of this class is zero whenever c_l != 2/5, for every omega and every omega/c_l, and ||R_u||_2 >= |1 -
   5c_l/2| ||U||_2 whenever R_u is in L^2. This is a statement about global L^2 norms: it gives no lower bound for
   finite-shell residual ratios and does not apply to the natural tail, which is not in L^2. For the natural tail
   integral_{B_R} |U|^2 = (c_l/(5c_l-2)) R^((5c_l-2)/c_l) integral_{S^2} |F|^2 dS (1 + o(1)). FINAL_REPORT.md section
   2, item 3 (stated there for the target range).
2. Decay dichotomy [I]. For 2/5 < c_l < 1/2, U in C^2 with the full-space pressure and |U| <= C (1+r)^(-alpha)
   uniformly: E(R) = integral_{B_R} |U|^2 = L R^(3-2alpha) + O(R^(2-3alpha)) with L >= 0, and L = 0 only if
   U = 0. In particular U = o(r^(-alpha)) uniformly implies U = 0, without any assumption on derivatives or on a
   pointwise pressure bound. The proof combines the exact ball ODE
   d/dR (R^(2alpha-3) E(R)) = -(2/c_l) R^(2alpha-4) integral_{S_R} U_r (K + P) dS, the annulus bound
   integral_{R<r<2R} (|U|^3 + |P U|) <= C R^(3-3alpha) (kernel bounds for the inner and outer source parts,
   L^2 boundedness of Riesz transforms for the middle part) and the monotonicity of E.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 6) [I]. The statement concerns exact
   profiles only, not sequences of approximate states; the limit L is a normalized energy, not a pointwise angular
   profile (section 6).
3. Axisymmetric profiles are trivial [I]. For 0 < c_l < 1/2 and any omega, an axisymmetric C^2 profile with
   U = o(|y|) uniformly is constant (zero if it decays). Backward trajectories of W are trapped by sublinearity;
   ell grows like e^(k t) along them (identity 2.2 with d_phi P = 0), so ell = 0; without swirl,
   W(Omega_phi/rho) = -(1+c_l) Omega_phi/rho [V, d06] forces Omega = 0; a sublinear harmonic field is constant.
   This argument does not use the non-rotating Liouville theorem of the companion study.
4. Dynamics of W for sublinear U [I]. The alpha-limit set of a point with Omega != 0 meets
   {lambda_max(S) >= 1}; a singleton backward limit p of such a point has max Re sigma(DW(p)) >= 1 + c_l; a
   periodic W-orbit carrying vorticity has Floquet multipliers 1, e^((1+c_l)T), e^((2c_l-1)T) (a saddle), and any
   periodic alpha-limit set of a vortical point is a hyperbolic saddle cycle.
5. No Bernoulli-type Lyapunov function in general [V, d06]. For any harmonic polynomial Phi, U = grad Phi with
   P = -k Phi - c_l y.grad Phi - |grad Phi|^2/2 + omega d_phi Phi is an exact, non-decaying profile. An explicit
   quartic Phi has a periodic W-orbit attracting an open tube backward along which Be is not monotone, and the
   affine U = (a y_1, -a y_2, 0) (a >= 1, |omega| > a) has an equilibrium with lambda_max(S) >= 1 and spectrum
   {c_l, c_l +- i (omega^2 - a^2)^(1/2)}, no stable direction. These examples violate decay. They show that
   H_0 + a ell (a constant) is not a Lyapunov function for all smooth rotating profiles and that no universal strict
   identity with exceptional set {W = 0} or {V = 0} holds; they do not exclude other Bernoulli-type functions, in
   particular under decay, and they say nothing about decaying profiles [I for this qualification].
6. Leading vorticity [I]. A nonzero smooth divergence-free exact leading tail cannot have identically vanishing
   leading vorticity H (pointwise zeros of H remain possible).
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 4) [I as formal far-field computations;
   the two logarithmic coefficients below were reproduced exactly by an independent check]. Formal far-field
   statements for a smooth tail whose expansion may be differentiated term by term (this hypothesis is used wherever
   vorticity asymptotics or integrability enter). On twisted fields r^(-p) G(theta, chi) the linear part of R_u acts
   as multiplication by c_l (alpha - p); the leading tail U_0 = r^(-alpha) F(theta, chi) lies in its kernel for every
   F obeying one divergence constraint, whose general smooth solution is given by two free scalar functions on S^2
   (toroidal and poloidal potentials). The first nonlinear correction r^(-(2 alpha + 1)) G[F] and the pressure
   r^(-2 alpha) Q[F] are locally determined by F; the harmonic pressure multipoles r^(-(l+1)) Y_l^m with l >= 2 are
   global data (finite parts of source moments), and the l = 0, 1 moments vanish (section 5). In the formal expansion
   a logarithmic pressure term r^(-(l+1)) log r can arise only from a source term with zero radial frequency and rate
   exactly l + 3, with any azimuthal index m; such rate coincidences occur only for rational c_l = n/K (lowest terms)
   and enter at order n. For c_l = 3/7 nonzero logarithmic coefficients were found at the orders analyzed: a pressure
   term r^(-5) log r from the tail alone, and r^(-10) log r with m = 2 from three tail factors and a quadrupole. These
   are formal findings at the orders analyzed, not a classification of all higher terms.
   Completeness of the two scalar potentials [I: standalone independent proof of 2026-10-26, reviewed by the lead].
   Let 1 < alpha < 3/2 (only 2 - alpha != 0 is used), omega real, beta = omega/c_l, and X the axial rotation generator
   on functions on S^2 (X = d_chi away from the poles). A smooth F = f n + v on S^2 (v tangent) gives a
   divergence-free field r^(-alpha) F(theta, phi + beta log r) if and only if f = -Delta_S sigma and v =
   grad_S[(2 - alpha) sigma + beta X sigma] + grad_S tau x n for smooth sigma, tau on S^2, unique up to additive
   constants (f has zero mean because 2 - alpha != 0). Then U_0 = curl(T y) + curl curl(Psi_p y) on r > 0 with T =
   r^(-alpha) tau(theta, chi) and Psi_p = r^(1-alpha) sigma(theta, chi), chi = phi + beta log r. This concerns the
   linear divergence constraint only: it imposes no momentum equation, gives no approximation theorem for a truncated
   basis and constructs no regular core.
7. Backward stretching [I]. On the open invariant set G = {W x Omega != 0}, dense in {Omega != 0},
   |D Phi_{-t}(p) e| >= |det[W(p), Omega(p), e]| e^((1-2c_l) t)/(max|W| max|Omega|) for t >= 0 (Hadamard's inequality,
   det D Phi_{-t} = e^(-3c_l t), D Phi_{-t} Omega = e^(-(1+c_l) t) Omega(Phi_{-t}), D Phi_{-t} W = W(Phi_{-t}), trapping).
   Hence no point of G has a backward source or attracting cycle as alpha-limit; with countably many equilibria
   and periodic orbits, the vortical points with elementary alpha-limit sets form a null set, so a nonzero profile
   needs non-elementary backward dynamics on a positive-measure set (derivations/d07_backward_stretching.md).
   Strengthenings [I except the last clause, which is P; derivations/d11_stretch1_review.md]: G has full measure in the vortical set (curl(W x Omega)
   = (1-2c_l) Omega on an exact profile); the countability hypothesis is not needed (countable cover by local
   center-stable neighborhoods), so almost every vortical point has an alpha-limit that is neither a single
   equilibrium nor a single periodic orbit (no claim about continua of equilibria or networks); a vortical
   ergodic invariant measure with W, Omega != 0 almost everywhere has backward Lyapunov spectrum {-(1+c_l), 0, 1-2c_l} and integral
   Omega.S Omega/|Omega|^2 dmu = 1; along every vortical backward orbit the lower time average of that ratio is
   at least 1; the vorticity of an exact profile does not have compact support.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 10) [I: independent proofs, each reviewed
   step by step, 2026-10-26]. Two further statements, with DU bounded and U -> 0. (i) A compact invariant set of the
   backward flow on which W x Omega does not vanish is uniformly hyperbolic: the vorticity line contracts like
   e^(-(1+c_l)t), the line of W is neutral, and an explicit continuous invariant line grows like e^((1-2c_l)t) up to a
   bounded factor. (ii) Every nonzero profile carries an ergodic invariant probability measure of the backward flow,
   supported in the compact set of points whose forward W-orbit is bounded, with largest backward Lyapunov exponent at
   least 1 - 2c_l; its support may lie in {Omega = 0}, and neither positive entropy nor the full exponent spectrum is
   asserted for it. Neither statement guarantees the existence of a nonempty compact invariant set on which W x Omega
   does not vanish, and the support of the measure in (ii) may meet {W x Omega = 0}. Flow lemma
   (no Euler equation used): for C^1 uniformly sublinear U, every invariant probability measure of the flow of W is
   supported in the compact set of points whose forward W-orbit is bounded, so compact support need not be assumed in
   the measure statements of this item; when div U = 0 that set has Lebesgue measure zero, so every such measure is
   singular with respect to Lebesgue measure.
8. Self-similar Kelvin law [local identity V, d10; consequences I except the strong-stable and cohomology clauses, P].
   For every smooth U, P, W_j d_j U_i + U_j d_i W_j = -(1-2c_l) U_i + d_i(|U|^2/2 - P) + (R_u)_i, i.e. L_W U^flat = -k
   U^flat + d(K - P) on an exact profile. Hence the circulation of U around a W-transported loop and the vorticity
   flux through a transported surface scale like e^(-ks); the circulation around every periodic W-orbit vanishes;
   Omega is tangent to every compact invariant surface; finite vortex segments contract like e^(-(1+c_l)t) under the
   backward flow (calling vortex lines the strong-stable leaves needs a hyperbolic splitting); the set of points with
   bounded forward orbit is compact, null and has trivial Cech cohomology; every W-invariant probability measure mu
   satisfies integral (c_l|y|^2 + y.U) dmu = 0, integral U.W dmu = 0, integral |c_l y + U|^2 dmu = omega integral ell
   dmu and integral (k ell + d_phi P) dmu = 0; and no function H_0 + a ell + b|y|^2/2 with fixed constants a, b is a
   Lyapunov function for all smooth rotating profiles when omega != 0 (non-decaying examples; the decaying class is
   open; supplement below) (derivations/d10_kelvin_invariant_measures.md).
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 13) [I]. The last clause is shown with
   explicit non-decaying examples, and only in the form: no function H_0 + a ell + b|y|^2/2 with fixed constants a, b
   is monotone along W for all smooth rotating profiles; the decaying class and other functions are open
   (compare item 5).
9. Zeros of W and parameter count [proved statements checked in d09; existence of a zero and the eigenvalue
   condition I; the rest formal]. W has a zero (degree 1 on a large sphere, U = o(|y|)); at a zero with
   Omega != 0, DW has the eigenvalue 1+c_l along Omega and the other two eigenvalues sum to 2c_l - 1 < 0, so it has
   expanding and contracting directions and is never a source; backward basins of sources carry no vorticity; the forward
   non-escaping set is null. Local transport germs at a prescribed saddle can be infinite dimensional, and the
   critical-rate exterior linearization is not Fredholm in ordinary weighted spaces, so no dimension of the
   solution set in (c_l, omega) is justified.
10. Dilation-invariant strength. DU, lambda_max(S) and the ratios Sigma_Z, Sigma_E of section 8 are dilation
   invariant; every nonzero exact profile has sup lambda_max(S) >= 1 (item 4) and Sigma_Z = Sigma_E = 1, while a
   weak field has all of them proportional to its amplitude. No gauge choice can turn a weak state into a strong one.
11. Outgoing conditions and the CIV bounds with rotation [I for (a)-(d) and the attributions;
   derivations/d13_civ_transfer.md, checks d13_civ_checks.py all True]. W.y = (c_l y + U).y and sym DW = c_l I + S, so the outgoing quantities of
   Constantin-Ignatova-Vicol (arXiv:2602.17570; their profile arguments are non-rotating) do not see omega. (a) A vortical zero of W is never
   locally outgoing for c_l < 1/2 + c* (rotating Thm 3.8). (b) For decaying U, global outgoing W.y >= c*|y|^2, c* > 0
   (Elgindi's Hypothesis 6.7) forces U = 0 for c_l < 1/2 and any omega (decay is needed: affine irrotational fields
   satisfy the other assumptions) (transferred second half of their proof of Thm 3.9:
   along a backward orbit trapped near a zero y* with Omega(y*) = 0 and c_l + lambda_min(S(y*)) >= 0, the Cauchy
   formula gives Omega = 0 at its start). (c) Under local outgoing at finitely many zeros, vortical backward orbits
   avoid a neighbourhood of N_W, so their alpha-limits are zero-free compact invariant sets; for omega = 0 the
   Bernoulli function excludes these, for omega != 0 this is OPEN (a necessary reduction only: it is not claimed
   that such a set is a topological attractor or that such dynamics suffice for a profile). (d) Their Thm 3.4 bound
   C_p ||grad Omega||_inf^(3/(p+3)) ||Omega||_p^(p/(p+3)) >= 1 (p > max(3c_l, 1), C_2 = 2(162/pi)^(1/5) = 4.40051) holds verbatim; a value
   computed from a state with a sampled sup|grad Omega| is an estimate, not a certified bound.
   Attributions: item 3 is CIV Thm 4.5 and Remark 4.6 (the omega terms vanish for axisymmetric U); 2.5 at the global
   maximum is CIV Prop 3.3; item 8 for omega = 0 is CIV (3.24)-(3.28), and CIV Thm 4.3 is its axisymmetric
   periodic-orbit case.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 15) [I]. Hypotheses of (d) as stated: a
   nonzero decaying rotating profile with |Omega| <= C (1 + r)^(-1/c_l) and bounded grad Omega, and p > max(3c_l, 1);
   the bound transfers because the stretching identity at the maximum of |Omega| (section 2, item 5) and the
   Biot-Savart estimate do not involve omega. A value computed with a sampled supremum of |grad Omega| or an
   unresolved enstrophy is an estimate, not a certified bound.
12. Localized strength, quantitative non-axisymmetry and fast rotation [I for (a)-(d) and the (e) reduction,
   2026-10-24T19:35Z; (e) conditional on L2; derivations/d14_quantrot_review.md, checks d14_quantrot_checks.py all
   True]. (a) Every backward alpha-limit lies in the closed ball of radius R_trap <= max|U|/c_l
   (y.W = c_l|y|^2 + y.U), so every nonzero exact profile has lambda_max(S) >= 1 somewhere in |y| <= max|U|/c_l. (b)
   Normalize A = max|U|, u(x) = A^(-1) U(Ax), R = 2/c_l + 4 and B(u) = max_{B_R}|Du| + max_{B_R}|D^2 u|
   (dilation invariant). For each B there is delta(c_l, B) > 0, independent of omega, such that every nonzero exact
   profile with B(u) <= B has max_{B_AR}|KU| >= delta max_{B_AR}|U|, and a similar L^2 bound for K Omega (compactness;
   the rotation average removes the omega term from the vorticity equation, and an axisymmetric limit is excluded by
   the local version of item 3 and the harmonic gradient bound). Consequently |omega| >= omega_0(c_l, B) excludes such
   profiles: exact profiles with |omega| -> infinity at fixed c_l need unbounded normalized core derivatives. A
   sequence of exactly divergence-free fields with bounded B(u_n), core strain bounded below by any level above 3/8,
   residual -> 0 in L^2(B_R) and core non-axisymmetry -> 0 does not exist. The constants are not computed; none of
   this is a numerical threshold. (c) Along X' = -W, ell(p) = e^(-kT) ell(X(T)) + integral_0^T e^(-kt) [(JX).R_u -
   d_phi P] dt, so on a backward-invariant ball |ell| <= (R ||R_u||_inf + ||d_phi P||_inf)/(1-2c_l); -d_phi P = R_i
   R_j((KU)_i U_j + U_i (KU)_j). (d) On a compactly supported invariant probability measure, omega integral d_phi P
   dmu = -k integral |c_l y + U|^2 dmu and integral |c_l y + U|^2 dmu <= omega^2 integral rho^2 dmu; the exact affine
   profile U = (-c_l y_1 - omega y_2, omega y_1 + (c_l - 1) y_2, y_3) (non-decaying, non-axisymmetric, every c_l and
   omega) shows that these identities impose no relation between c_l and omega. (e) Slow rotation, conditional on the
   companion non-rotating Liouville theorem L2 (not verified input): under uniform normalized C^{2,beta} bounds and a
   uniform envelope |u| <= C(1+|x|)^(-alpha), a sequence of exact profiles with omega_n -> 0 has a subsequence with a
   C^2_loc limit that is a nonzero decaying non-rotating profile (max|u| = 1 is kept by the envelope); L2 excludes it,
   so there is omega_1 > 0 with no such profile for 0 < |omega| < omega_1. Unconditionally only the existence of such
   a subsequential limit is proved; convergence of the whole sequence and uniqueness of the limit are not shown.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 16) [I]. Scope as stated: the sequence
   statement of (b) concerns exactly divergence-free fields with uniform normalized bounds, momentum residual tending
   to zero in L^2 of the core ball and core strain kept above a fixed lambda_* > 3/8; a strain excess over 3/8 that
   tends to zero does not suffice (the interior gradient bound for harmonic fields, used to exclude an axisymmetric
   limit, caps the strain at 3/8). In (e) uniform normalized C^{2,beta} bounds on all of R^3 are assumed, the limit is
   a non-rotating C^2 profile at the same c_l, and bounds on the core alone do not suffice.
13. Zero-free invariant sets [I, lead-checked 2026-10-24T20:15Z, CONFIRMED by the independent route 20:38Z;
   derivations/d15_alphalim_review.md, checks d15_alphalim_checks.py]. Notation: B = U.W - |U|^2/2 + P,
   D = y.U + |y|^2/2, beta = (W x Omega)/k, h = U.Omega, averages <.> over a compactly supported W-invariant
   probability measure, E = <|V|^2>, L = <ell>, I = <rho^2>, T = <d_phi P>, Q = <|W|^2>, R_2 = <|y|^2>.
   (a) W.grad D = |V|^2 + c_l(1-c_l)|y|^2 - y.grad P; if y.grad P <= (c_l(1-c_l) - delta)|y|^2 on a compact K
   (delta > 0), K contains no compact invariant set on which W != 0; <y.grad P> = E + c_l(1-c_l) R_2.
   (b) grad B = W x Omega - kU, W.grad B = -k U.W, Omega.grad B = -k h; beta = U^flat + dB/k satisfies
   beta(W) = beta(Omega) = 0, d beta = dU^flat, L_W beta = -k beta, beta ^ d beta = 0 (so span(W, Omega) is a
   W-invariant foliation of G); a compact invariant set in G admits no positive C^1 q near it with d(q beta) = 0.
   For every smooth U, P: L_W beta + k beta = R_u^flat + d(W.R_u)/k with beta = U^flat + dB/k (generic Kelvin
   identity of item 8, residual-corrected), so M_t^T beta(Phi_{-t} p) = e^(kt) beta(p) with M_t = D Phi_{-t}(p)
   exactly on profiles; this is the signed form of SPEC 2.8(e) (an exact refinement of the bound of item 7.7),
   [H] until 20:37Z. On an approximate state beta_0 = (W x Omega)^flat/k instead has L_W beta_0 + k beta_0 =
   (W x curl R_u)^flat/k (vorticity-residual transport); the two forms coincide only for exact solutions.
   Qualifications from the audit: (a) needs delta > 0; the foliation is regular only where W x Omega != 0, and
   the integrating-factor statement concerns one positive C^1 factor on a neighborhood of a compact invariant subset
   of that set; the strict signs in (d) need E > 0.
   (c) Under local outgoing at finitely many zeros (item 11(c)), W has exactly one zero (total index +1, each
   outgoing zero has index +1), and Omega = 0 on a ball around it; Omega = 0 everywhere would follow from unique
   continuation, which is not available for smooth profiles.
   (d) E + Q = omega^2 I, so 0 <= E < omega^2 I on a zero-free support; for E > 0, sgn L = sgn omega = -sgn T;
   <Jy.W> = -Q/omega; I E - L^2 = E Q/omega^2; |omega| >= min|W|/sqrt(I) and |omega| >= 2 sqrt(<V_z^2>/I);
   <|U|^2> = E + c_l^2 R_2, <V> = omega J<y>, <grad P> = -((1-c_l)I + omega J)<U>; for omega = 0 no zero-free
   compact invariant set exists. <f'(ell)(k ell + d_phi P)> = 0 for every C^1 f, and
   ell(p) = -integral_0^infinity e^(-kt) d_phi P(Phi_{-t} p) dt on bounded backward orbits. E = 0 forces mu to be
   the uniform measure on one horizontal circle (which can carry vorticity).
   (e) Helicity: W.grad h = -(2-c_l) h + Omega.grad(K - P); for the natural tail
   integral_{R^3} f(B) h dy = 0 for every continuous f (div(F(B) Omega) = -k f(B) h, flux O(r^(2-2alpha))).
   (f) On a vortical ergodic measure with W != 0 almost everywhere (spectrum {-(1+c_l), 0, k} by item 7), Ruelle's
   inequality gives entropy h_mu <= k.
   (g) Bounded backward orbits with liminf e^(-kt)||Lambda^2 D Phi_{-t}|| = 0 start at non-vortical points
   (Omega(p) = e^(-kt) cof(D Phi_{-t})^T Omega(Phi_{-t} p)); the vortical spectrum sits exactly at this threshold.
   (h) Exact example on r > 0 (decay, axis regularity and full-space pressure fail): U_r = -r/2 + kR^2/(2r),
   U_theta = nu(r^2 - R^2)/(2r), U_z = z, curl U = nu e_3; the vortical circle r = R, z = 0 is a backward saddle with
   basin the cylinder r = R when k > 0 (an open basin only for c_l > 1/2); its translates show that supp mu need
   not meet {V = 0}, {ell = 0} or {d_phi P = 0}, and that E/(omega^2 I) has no uniform gap below 1.
   None of (a)-(h) excludes a compact zero-free alpha-limit set of vortical points; the rotating CIV Thm 3.9 stays
   OPEN.

14. Angular degree of the first nonlinear far-field coefficient [I, both routes; exact symbolic check for d = 1, 2, 3
   at c_l = 0.45, omega = 0.3, omega/c_l = 2/3]. If the leading tail r^(-alpha) F is the curl of a twisted homogeneous
   potential of angular degree d in the rotating frame, the first nonlinear coefficient G[F] (rate 2 alpha + 1, with
   its pressure coefficient of rate 2 alpha) has degree at most 2d + 3 and is the curl of a twisted potential of degree
   at most 2d + 2, because curl(y x V) = [(p - 2) - (omega/c_l) L] V on divergence-free twisted fields of rate p, with
   L skew and p - 2 = 2 alpha - 1 > 0. The bound is attained (axisymmetric potential n_3^d e_3). The rate-(2 alpha + 1)
   correction U_1 of the primary exchange representation satisfies L U_1 = -U_1 exactly (since
   c_l (2 alpha + 1) = 2 - c_l), so the rate-(2 alpha + 1) residual coefficient is G_required - G_carried and no other
   linear tail adjustment changes it [I, proof by the independent route, reviewed in derivations/d38; symbolic and
   quadrature check d38_normcheck.py].
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 18) [I]. Degrees are spherical-harmonic
   degrees of Cartesian components restricted to the unit sphere. If the angular part of the potential has degree d,
   then F has degree at most d + 1 and n . F at most d, the coefficient N = (DU_0) F of (U_0 . grad) U_0 has degree at
   most 2d + 1, and the pressure source tr((DU_0)^2) at most 2d + 2. Since the bound is attained, a correction space
   of degree below 2d + 2 cannot carry G[F] for every leading tail of degree d. The statement concerns a formal
   far-field coefficient, not the existence of a profile.
15. Residual identities for approximate states [I; exact symbolic checks by the independent route]. For any C^2
   divergence-free U with the natural tail bounds (no smallness): (a) integral R_u . curl Omega = (1 - 3c_l/2)(1 - Sigma_Z) Z
   with Z the enstrophy, so a stretching defect forces a momentum residual; (b) (1 - 2c_l) integral f(B) U.Omega =
   integral f(B) Omega . R_u for every continuous f. Ball forms carry boundary terms of order R^(1 - 2 alpha).
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 19) [I]. Hypotheses as stated: |D^j U| <=
   C (1 + r)^(-alpha - j) for j = 0, 1, 2, and |grad P| <= C (1 + r)^(-alpha), with B = U . W - |U|^2/2 + P as in
   item 13. On B_R, (a) holds with the boundary terms (1/2) int (W . n) |Omega|^2 - int n . (R_u x Omega) added on the
   right (they are O(R^(1 - 2 alpha))), and (b) with the boundary term -int Phi_f(B) Omega . n (Phi_f' = f, Phi_f(0) =
   0), which is zero on every sphere where |B| is small when f vanishes near 0. From (a), ||R_u||_(L^2(w)) >=
   (1 - 3c_l/2) |1 - Sigma_Z| Z / ||curl Omega||_(L^2(1/w)) for w = (1 + r)^(-1), and, on a partition into shells S of
   volume V_S with five-term denominators D_S, the shell ratios rho_S satisfy max_S rho_S >= |int R_u . curl Omega| /
   sum_S V_S D_S (V_S^(-1) int_S |curl Omega|^2)^(1/2). Every normalized bound needs a positive denominator (a zero
   denominator gives no quotient bound); a stretching defect forces a momentum residual, but a small defect does not
   force a small residual. Numerical values that add leading-tail exterior estimates are estimates, not certified
   bounds.
16. Finite-shell residual ratios are not proximity certificates [I, both families; derivations/d37, d39]. For every
   compact steady Euler flow V (they exist: Gavrilov arXiv:1810.08020, Constantin-La-Vicol arXiv:1903.11699 Thm 1) and
   every smooth divergence-free H, integral V . [L V + (H.grad)V + (V.grad)H + grad P_x] = (1 - 5c_l/2)||V||^2 exactly.
   Fixed copies of amplitude a drive the five-term and nonlinear-balance ratios to zero as 1/a; shrinking copies at
   points where a compactly patched background makes the transport field vanish drive the five-term, nonlinear,
   self-similar-sum and smaller-sum ratios (and, at lambda = delta^(-3), the quadratically normalized residuals) to
   zero, while a pressure-free functional keeps the family a fixed local L2 distance from every exact profile. The
   single-term ratios resist (global ||R_Omega||/||Omega|| >= 1 - 3c_l/2; shell RMS R_u / RMS (1 - c_l)U >=
   |1 - 5c_l/2|/(1 - c_l) for lambda = delta^(-3)), as do the fixed-gauge absolute residual, the peak factor and the
   maximum speed. Hence SPEC v1.17 and v1.19. Continuum statement; not an obstruction.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 20) [I]. The steady pressure of a compact
   steady flow V is constant on the unbounded component of the complement of its support, so it can be normalized to
   vanish outside a ball (not necessarily in bounded holes); it is then the decaying full-space pressure. The pairing
   coefficient 1 - 5c_l/2 lies in (-1/4, 0). Local L^2 convergence of the fields alone does not resist lambda =
   1/delta: the family converges to the modified field, which is not a profile. The single-term ratios are not shown
   to certify proximity to a profile; they only resist these constructions. The statements concern continuum
   quantities on finitely many shells; finite representations only approximate such copies.
17. Homogeneous steady fields of degree -alpha, 1 < alpha < 2 [I, both routes; derivations of the lead and the
   independent route]. For u = r^(-alpha) f(sigma) smooth on R^3 minus the origin solving steady Euler, with
   H = p + |u|^2/2 = r^(-2 alpha) h(sigma) and f = v + b sigma: the sphere integrals of b Phi(h) and of the radial
   vorticity times Phi(h) vanish for every bounded Borel Phi; h >= 0, positive somewhere, zero somewhere, and every
   zero of h is critical; u = 0 if h^(-(alpha - 1)/(2 alpha)) is integrable on {h > 0}, and for Beltrami,
   irrotational, axisymmetric, tangential and zero-radial-vorticity fields. Several subclasses and the moment identity
   are in Shvydkoy arXiv:1510.03378v1 (Props 3.1, 3.2, 4.1, 5.1; Lemma 6.1, Remark 6.2); no novelty is claimed. The
   general smooth non-axisymmetric case is OPEN. Twisted fields (u(lambda R(k log lambda) y) = lambda^(-alpha)
   R(k log lambda) u(y)): all of the above extend to every real k, and alpha = 1 is excluded for every k; the profile
   tail has k = -omega/c_l in this convention [I, lead audit derivations/d42 with the check d42_twisted_check.py;
   confirmed by the independent route 2026-10-25T02:27Z with its own proof and Cartesian check, worst error 2.0e-14].
   Supplement, untwisted case (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 21) [I]. Momentum fixes
   the pressure up to a constant and homogeneity fixes the constant, p = r^(-2 alpha) q(sigma). Integrating div_S(b v
   Phi(h)) over the sphere with Phi = (-h)_+^s, 0 < s < (2 - alpha)/(2 alpha), gives h >= 0, and Phi = 1 gives 2 alpha
   int h = (2 - alpha) int b^2 + (alpha - 1) int |v|^2 (sphere integrals), so u = 0 if h <= 0; h > 0 everywhere is
   excluded by the hairy-ball theorem on the Bernoulli surfaces. With h = q + (b^2 + |v|^2)/2 the same identity gives
   alpha int q = (1 - alpha) int b^2 - (1/2) int |v|^2, so the sphere mean of q is strictly negative for a nonzero
   field. The integrability criterion uses a stream-function pairing of h^((2 - alpha)/(2 alpha)) v and
   h^((1 - alpha)/(2 alpha)) times the tangential vorticity. Smoothness alone does not give the integrability of
   h^(-(alpha - 1)/(2 alpha)) on {h > 0}; it holds if the zero set of h is covered by finitely many smooth curves and
   points near which h is bounded below by a constant times the m-th power of the distance, with m
   (alpha - 1)/(2 alpha) < 1 near curves and < 2 near points. The sign of h, the integrability condition and the
   zero-radial-vorticity class were not found in the cited paper; no wider literature search was made. Consequence
   (formal and conditional; its conditional reading was independently confirmed): a profile with a strongly
   concentrated core and a regular matched intermediate region, where the nonlinear terms dominate and the field is
   close to an ordinary homogeneous field of degree -alpha, would need a nonzero field of this kind outside the
   classes above; no asymptotic overlap region has been established in the saved states, and this is not an
   obstruction to profiles.
   Supplement, twisted case (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 22) [I: derivation checked
   step by step, with an exact pointwise check of every sphere identity on generic twisted fields for both signs of
   the twist rate; proved separately with its own Cartesian check]. Here k is the twist rate of item 17 (a local
   symbol, not 1 - 2c_l). Write curl u = r^(-alpha - 1)(w + zeta sigma) on the unit sphere, X = e_3 x sigma, V_k = v -
   k b X and W_k = w - k zeta X. On the unit sphere div V_k = (alpha - 2) b, V_k . grad h = 2 alpha b h, W_k . grad h
   = 2 alpha zeta h, div W_k = (alpha - 1) zeta and det(V_k, W_k) = -2 alpha h (the twist terms cancel exactly), and
   momentum along the generator y + k J y gives V_k . grad g = (alpha - 1) b g - (alpha - 1)(b^2 + |v|^2) + 2 alpha h
   with g = b + k v . X. For every k: the sphere-integral identities and the mean identity of the untwisted case hold
   unchanged; h >= 0 (for alpha < 3/2 by integrating div(|h|^delta g V_k) = |h|^delta (2 alpha h -
   (alpha - 1)(b^2 + |v|^2)), delta = (3 - 2 alpha)/(2 alpha), over {h < 0}; for alpha < 2 by a bounded-test argument
   with the divergence-free field |h|^((2 - alpha)/(2 alpha)) V_k); h > 0 everywhere is impossible because V_k would
   be a nowhere-zero tangent field on the sphere (nonzero Bernoulli levels are graphs along the dilation-rotation
   orbits, so a compact one is a sphere); u = 0 if h^(-(alpha - 1)/(2 alpha)) is integrable on {h > 0} (the pairing
   with V_k and W_k gives exactly -2 alpha times the integral of h_+^(3/(2 alpha))); the zero-radial-vorticity class
   needs no integrability assumption. A nonzero example needs h >= 0 with zeros, h^(-(alpha - 1)/(2 alpha)) not
   integrable on {h > 0}, and b and zeta not identically zero. Under passage-to-the-limit hypotheses (convergence of
   velocity and pressure in C^1 on expanding annuli, vanishing steady-Euler residual, a smooth limiting angular
   profile and a verified limiting homogeneity), none of which is established for the saved states, a twisted
   intermediate field does not evade these obstructions. Not an obstruction to profiles; no novelty is claimed.
18. The edge c_l -> 1/2 and the lower edge [I, lead audit derivations/d43 of a consulted answer; (a), (c), (d) and the
   exact identities of (b) confirmed by the independent route 2026-10-25T02:38Z with its own proof and checks; the
   shell asymptotics of (b) are consulted, not independently derived, and are not used]. (a) Twisted degree -1 steady
   fields smooth on complete spheres vanish (second proof: with X = y - (omega/c_l) J y, f = u.X and H = P + |u|^2/2,
   div(f sgn(H)|H|^(1/2) u) = 2|H|^(3/2) forces H = 0, then the stress u (x) u - |u|^2 I/2 forces u.n = 0). (b) An
   explicit smooth axisymmetric swirl family with exact unit tail, U = A J y [a^4 + Q^2]^(-(alpha+1)/4), Q = rho^2 +
   eps^2 z^2, eps = 1/2 - c_l, satisfies L U = b U, b = a^4/(a^4 + Q^2), exactly; its five-term ratio is O(eps) while
   its resolved single-term ratio stays near 1/(1 - c_l) (continuum statement; these ratio asymptotics are consulted,
   not independently derived, and are not used; motivates SPEC v1.21). (c) For divergence-free U with a unit tail, a
   uniformly bounded remainder O(r^(-alpha-1)) and its decaying pressure, integral U.R_u = beta_0 E_ren (ball energy
   identity of section 8 with the tail cancellation beta_0/p = -c_l/2); a little-o remainder alone does not suffice.
   So E_ren = 0 for an exact profile, and at c_l = 2/5 a unit tail is incompatible with an exact profile. (d) Compact
   steady seeds fail the first solvability condition of a regular small-core expansion. None is an obstruction in the
   open range.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 23) [I; the core-radius asymptotic and the
   exact maxima below were proved independently, with high-precision quadratures]. Labels refer to item 18. (a): the
   closing step is that a tangential, surface-divergence-free field with zero radial vorticity on S^2 vanishes; the
   axis-singular swirl u = A e_phi/rho is an exact example outside the class (infinite sphere L^2 norm). (b): with eps
   = 1/2 - c_l and a = (A eps)^(1/(alpha + 1)), U = eps^(-1) J y + o(|y|) at the origin; L U = b U holds for every
   omega; as eps -> 0 the core radius satisfies a ~ eps^(1/2) (4 pi log(1/eps))^(-1/4); exactly, max|U| = eps^(-1) a
   alpha^(-1/4) (1 + 1/alpha)^(-(alpha + 1)/4) (at z = 0, rho = a alpha^(-1/4)) and max|Omega| = 2/eps
   (at the origin). (c): the exact-profile conclusion E_ren = 0 uses a unit leading tail U_0, the remainder bound U -
   U_0 = O(r^(-alpha - 1)) and the pressure bound P = O(r^(-2 alpha)); for an approximate state the existence of E_ren
   and the limit relation need a quantified tail remainder, and the integral converges absolutely when the remainder
   bound holds with one derivative and is otherwise a limit over balls; at c_l = 2/5 the identity would give 0 =
   c_l/2. (d): with U(y) = a^(-alpha) V_a(y/a), V_a = V + mu w + ... and mu = a^(alpha + 1), pairing the first-order
   equation with V gives 0 = beta_0 ||V||^2; this excludes one regular scheme only. Edge limit: an exactly homogeneous
   smooth outer limit at the edge is excluded by (a), but obtaining such a limit from profiles with c_l -> 1/2 would
   need the additional hypothesis that a nonzero angular norm is retained; a homogeneous leading tail is not excluded,
   and nothing here excludes a smooth non-homogeneous profile at or near c_l = 1/2.
   Supplement (synchronized with FINAL_REPORT.md section 2, item 23 (e)) [I; independent proof, reviewed step by step by
   the theory route on 2026-10-26]. Fix omega != 0 and, for n >= 4, c_l,n = 1/2 - 1/n^2, alpha_n = (1 - c_l,n)/c_l,n =
   (n^2 + 2)/(n^2 - 2), omega/c_l,n = 2 omega n^2/(n^2 - 2). With a fixed plateau cutoff chi, a_n = e^(-n) and the
   transverse potential psi_n = chi(rho)(1 - chi(rho/a_n)) Re(rho^(s_n) e^(2 i phi)/(s_n^2 - 4)), s_n = 2 - alpha_n + 2
   i omega/c_l,n, the jet is n^(-1/2) curl(chi(z/n) e_z x grad psi_n) (supported in r < 3n) and the tail is the curl of
   kappa_n (1 - chi(r/(4n))) Re(r^(-alpha_n - 1 + 2 i omega/c_l,n) w^2) e_z, w = y_1 + i y_2, with kappa_n fixing the
   unit sphere gauge; the tail is zero for r <= 4n, equals r^(-alpha_n) T_(-(omega/c_l,n) log r) F_n on r >= 8n and
   satisfies L V = 0 there. The fields are smooth and divergence-free, lie in azimuthal modes +/-2 (rotation average
   zero, non-axisymmetric energy fraction 1) and have zero total helicity. On every fixed B_R: int_(B_R)|U_n|^2 -> 2 pi
   R, ||R_u,n||_(L2(B_R)) <= C_R n^(-1/2) with the decaying Newton pressure, sup|P_n| <= C_R n^(-2), sup|grad P_n| <=
   C_R n^(-3), |U_n|^2 dy -> pi mu_axis and U_n -> 0 weakly but not strongly in L2_loc, while sup_(B_R)
   of |U_n|, |Omega_n| and |R_u,n| tend to infinity. The family approaches the excluded endpoint c_l = 1/2 and moves its
   tail outward; it gives no fixed-c_l analogue, no global residual estimate and no balance or acceptance result, and it
   is neither a profile nor an obstruction.
   Supplement (synchronized with FINAL_REPORT.md section 2, item 23 (f)) [I; independent proof, reviewed step by step by
   the theory route on 2026-10-26, with quadrature spot checks]. For a vertical shear U(x_perp, z) = f(x_perp) e_z on
   B_R (f smooth near the closed disk |x_perp| <= R, P smooth near the closed ball), the rotating residual reduces to
   R_u = (T f) e_z + grad P with T f = (1 - c_l) f + c_l x.grad f - omega Jx.grad f, because J e_z and (U.grad)U vanish.
   With rho = |x_perp|, n_z = z/R and E = int_(B_R)|U|^2: int_(B_R) U.R_u = (1 - 2c_l) E + (c_l/(2R)) int_(S_R) rho^2
   f^2 + int_(S_R) P f n_z. Hence, if E > 0, ||R_u||_(L2(B_R)) >= (1 - 2c_l)||U||_(L2(B_R)) for every omega when the
   pressure boundary work W_P = int_(S_R) P f n_z is nonnegative (for example P even in z),
   and ||R_u||_(L2(B_R))/||U||_(L2(B_R)) >= max(0, 1 - 2c_l - |W_P|/E) in general. For real smooth compactly supported f
   on R2 (the whole plane), ||T f||_2^2 = (1 - 2c_l)^2 ||f||_2^2 + ||S f||_2^2 with S = T - (1 - 2c_l), and the constant
   1 - 2c_l is sharp within real azimuthal mode-2 functions concentrating at the origin; no nonzero f attains it. These
   are shear-subclass estimates: they restrict a z-independent vertical shear core at fixed c_l in (2/5, 1/2) (the gap
   is 1/10 at c_l = 0.45) and explain why the family of (e) needs c_l,n -> 1/2; they are not estimates for general
   three-component fields, not a nonexistence theorem and not an obstruction.
19. Backward-transport inverse of L [V, lead derivation; numerical check derivations/d45_backward_inverse_check.py,
   defect 2e-16 on two test fields]. With Phi_s y = e^(c_l s) R(-omega s) y and R(t) = e^(tJ), d/ds [e^((1 - c_l) s)
   R(omega s) V(Phi_s y)] = e^((1 - c_l) s) R(omega s) (L V)(Phi_s y), so for V bounded near 0, V = G(L V) with G f(y)
   = integral_(-infinity)^0 e^((1 - c_l) s) R(omega s) f(Phi_s y) ds; G f(y) uses f only on the inward spiral from y
   to the origin. Consequently U - T(U) = G R_u for T(U) = -G N(U), and a smooth U bounded near 0 solves the profile
   equation iff U = T(U); the leading tail is then an output of G. Extension [I since 2026-10-25T03:08:19Z
   (independent proof and 63 numerical controls of the verifier, with the scope qualifications in (e) and (g)); lead
   audit derivations/d46_backward_formulation_audit.md of a consulted answer; numerical checks
   d46_spiral_ray_check.py, d46_tail_rate.py, d46_ray_identity_check.py]: (a) G is the unique inverse of L among
   fields bounded near 0 (the kernel r^(-alpha) F(theta, phi + (omega/c_l) log r) of L is unbounded at 0), G f(0) =
   B^(-1) f(0) with B = (1 - c_l) I + omega J, and G preserves divergence-free fields. (b) In spherical components at
   fixed (theta, chi), chi = phi + (omega/c_l) log r, L = (1 - c_l) + c_l r d_r, so (G f)(r, theta, chi) = (1/c_l)
   r^(-alpha) integral_0^r rho^(alpha-1) f(rho, theta, chi) d rho (worst difference to the Cartesian quadrature
   3.3e-16) and the tail coefficient of G f is the full ray integral F_f, with remainder O(r^(alpha - q)) for |f| ~
   r^(-q); the truncated ray integral of L U up to R is R^alpha U(R, ., .). (c) A profile tail is generated by the
   core: F_U = -F_(N(U)); F = 0 forces U = 0 (then U = o(r^(-alpha)) uniformly and item 2 applies). (d) T(tU) = t^2
   T(U), so plain fixed-point iteration has the eigenvalue 2 on the unit-tail slice; the amplitude factor m(U) = <U,
   U>_eta / <U, T(U)>_eta (weight |y|^(-eta), 3 - 2 alpha < eta < 3) removes only that direction (the eigenvalue 2 is
   conditional on a nonzero fixed point existing). (e) The linearization has the symmetry kernel U - y.grad U, JU -
   (Jy.grad)U (not claimed to exhaust the kernel) and principal symbol i (b.xi), b = (c_l I - omega J) y + U, so it
   has no bounded Fredholm realization with local isotropic H^(s+1) (domain) and H^s (output) norms; on unweighted
   whole-space spaces the unbounded coefficient needs its own domain, and graph spaces are not excluded. (f)
   Pure-swirl U: [G N(U)]_phi = 0, so |U - T(U)| >= |U|. (g) Concentration of compact steady copies at a stagnation
   point y_0 != 0 of (c_l I - omega J) y + U rules out a uniform inverse estimate near an isolated solution orbit (not
   distance from every exact profile) and drives the normalized delta_G = RMS(G R_u)/RMS(U) on B(y_*, a_eff/2) to zero
   for any fixed smooth background U_b; the absolute defect d(U_b + t_eps V_eps) = d(U_b) + O(t_eps eps) need not tend
   to zero unless U_b is exact (wording corrected 2026-10-25T03:31Z at the independent route's request). SPEC v1.22
   reports tau_F = ||F_(R_u)|| / ||F_U|| and RMS(G R_u)/RMS(U) without threshold. No obstruction.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 24) [I]. Labels refer to item 19. (a):
   also L G f = f; the solutions of L Y = 0 on R^3 minus the origin are r^(-alpha) R(-(omega/c_l) log r)
   F(R((omega/c_l) log r) n), unbounded unless F = 0, and decay at infinity alone does not give uniqueness. (b): in
   azimuthal Fourier modes e^(i m phi) the ray formula carries the factor (r/rho)^(i m omega/c_l). (c): the
   equivalence L U + N(U) = 0 if and only if U = -G N(U), with N(U) = (U . grad) U + grad P, is stated for
   divergence-free U in the symbol class of order -alpha with its decaying full-space pressure (P = O(r^(-2 alpha))
   with derivatives); every such fixed point has leading tail F_U = -(1/c_l) int_0^infinity rho^(alpha - 1) N(U) d rho
   along the twisted rays and remainder O(r^(-2 alpha - 1)). (d): T commutes with dilations and axial rotations; at a
   nonzero fixed point the eigenvalue 2 of the linearized unit-tail normalized iteration has eigenvector U -
   Z/(alpha + 1), Z = U - y . grad U, so plain normalized fixed-point iteration is unstable whenever a nonzero profile
   exists; the amplitude normalization is U -> m(U)^2 T(U). (e): graph-space formulations would need new estimates.
   (g): for a compactly supported steady Euler field V, the backward defect d(U) = U + G N(U) = G R_u satisfies
   d(U_b + t V) = d(U_b) + t G (L + DN(U_b)) V and d(t V) = t V exactly; at a stagnation point y_0 != 0 of
   (c_l I - omega J) y + U_b, concentrated copies V_eps = V((y - y_0)/eps) have G (L + DN(U_b)) V_eps = O(eps) in sup
   norm, which rules out a uniform inverse estimate near an isolated solution orbit in weighted C^m tail norms. (f):
   the statement is for an axisymmetric pure swirl U = u_phi e_phi, and the azimuthal part of the truncated tail
   integral of R_u is that of R^alpha U(R). None of these is an obstruction or a proximity certificate.

20. Eddy generation of the mean swirl [I: identity, representation and bound confirmed by the independent route
   (separate proof, three exact symbolic controls with arbitrary c_l and omega, twelve 65-digit transport controls)
   at 2026-10-25T03:37Z; lead numerical check derivations/d50_mean_swirl_identity.py, 1.5e-8, the finite-difference
   size; trapping wording corrected 2026-10-25T03:39:26Z]. With azimuthal averages <.> about e_3, u' = U - <U>,
   Gamma_0 = <(J y).U>, W_0 = c_l y + <u_rho> e_rho + <u_z> e_z and S = -<(J y).((u'.grad) u')> = -div(rho <u'
   u'_phi>): rho <R_u . e_phi> = (1 - 2 c_l) Gamma_0 + W_0.grad Gamma_0 - S for every smooth divergence-free U, every
   P and every omega (the rotation term and the pressure average out). If U, DU are bounded and M_0 = sup|U|,
   backward W_0 trajectories obey |Psi_s y| <= e^(c_l s)|y| + (M_0/c_l)(1 - e^(c_l s)) (bounded; finite entry into
   every ball of radius larger than M_0/c_l, not necessarily into the closed ball of radius M_0/c_l), and Gamma_0(y)
   = int_(-infinity)^0 e^((1 - 2 c_l) s) [S + rho <R_u . e_phi>](Psi_s y) ds. For an exact profile the mean swirl,
   including that of the leading tail, is generated only by the eddy angular-momentum flux, S = 0 forces Gamma_0 = 0
   (the swirl part of item 3), and (1 - 2 c_l) sup|Gamma_0| <= sup rho <|u'| |D u'|>. No obstruction. FINAL_REPORT.md
   section 2, item 25.

21. Mean angular-momentum consequences [I: consulted answer checked step by step, derivations/d56_meanswirl1_audit.md
   and d56_meanswirl1_checks.py; independently proved by the independent route 2026-10-25T04:11Z; recorded
   2026-10-25T04:03:44Z, status 2026-10-25T04:34:32Z]. Scope: (a) needs T_0 > 0; (c) holds for exact profiles only.
   Notation of item 20, a = 1 - 2 c_l, v = <U>, E = -div <u' (x) u'>, f the mean azimuthal component of the leading
   tail. (a) With p_0 = 3 c_l/a and T_0 = int_(S^2) |sin(theta) f|^(p_0): (a/3) T_0 = int S Gamma_0
   |Gamma_0|^(p_0 - 2) dy for every exact profile (volume coefficient a - 3 c_l/p vanishes at p_0; boundary limit
   (c_l/p_0) T_0); the defect D_0 of approximate states is the normalized residual integral of the supplement below.
   (b) For an exact profile of the tail class, a int v . curl v = int E . curl v. More generally, for C^2
   divergence-free U with U = O(r^(-alpha)), DU = O(r^(-alpha-1)), D^2U = O(r^(-alpha-2)), P = O(r^(-2alpha)) and grad
   P = O(r^(-2alpha-1)), the absolutely convergent identity int <R_u> . curl v = a int v . curl v - int E . curl v
   holds for every omega and omega/c_l; the exact-profile equality is its zero-residual case (residual form proved by
   the independent route, 2026-10-25T04:09Z, and rechecked by the lead 2026-10-26: averaging removes the rotation
   term, the nonlinear and pressure pairings are boundary fluxes O(R^(1-3alpha)), and (y . grad)v = grad(y . v) - v -
   y x curl v gives int (y . grad)v . curl v = -int v . curl v; FINAL_REPORT.md states (b) for exact profiles only).
   (c) A bound M on the mean meridional velocity, delta_0 = sup (1 + r)^alpha |u'|, delta_1 = sup (1 + r)^(alpha + 1)
   |D u'| imply sup |sin(theta) f| <= (1 + M/c_l)^(alpha - 1)(1 + 1/a) delta_0 delta_1 (one integral bound checked
   numerically). No obstruction. FINAL_REPORT.md section 2, item 27.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 27) [I]. (a): the defect is normalized,
   D_0 = 1 - (3/(a T_0)) int S Gamma_0 |Gamma_0|^(p_0 - 2) dy = (3/(a T_0)) int rho <R_u . e_phi> Gamma_0
   |Gamma_0|^(p_0 - 2) dy; the S pairing converges absolutely under the stated derivative decay, while with only a
   uniform leading mean-tail limit the residual pairing is a limit over balls, absolutely convergent when the
   differentiated tail remainder decays with a positive power. (b): for an exact profile, with zero total helicity
   (item 13 (e)), the eddy helicity is minus the mean helicity; this is sign-indefinite and not coercive. (c):
   exactness is essential, since a smooth pure-swirl approximate state has delta_0 = delta_1 = 0 and f != 0; the bound
   says nothing about tails without mean swirl, and tail normalization alone gives no flux threshold, since mean-swirl
   tails can concentrate in polar caps; the integral bound used in (c) is proved for all parameters. None of (a) to
   (c) is an obstruction for the target class.

22. Pressure-free mean-swirl tail defect [I: independent derivation, reviewed by the lead in
   derivations/d57_pressure_free_mean_swirl_review.md; recorded 2026-10-25T04:12:31Z]. With v = <U . e_phi>, A = <e_phi . (DU) U>
   and E = <R_u . e_phi> averaged at fixed (r, theta): E = c_l(alpha v + r d_r v) + A for every C^1 U, single-valued P
   and omega, so (1/c_l) int_0^R r^(alpha - 1) E dr = R^alpha v(R, theta) + (1/c_l) int_0^R r^(alpha - 1) A dr, with limit
   D_0phi = F_0phi + (1/c_l) int_0^inf r^(alpha - 1) A dr (zero for an exact profile). A = A_mean + A_eddy with rho A_mean
   = M.grad Gamma_0 and rho A_eddy = -S (the latter for div U = 0). The ray integral contains mean-meridional transport;
   only the characteristic form of item 20 isolates the eddy source. FINAL_REPORT.md section 2, item 26.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 26) [I]. Scope as stated: E = c_l
   (alpha v + r d_r v) + A holds for every C^1 field U, every single-valued C^1 pressure P and every omega, and the
   ray identity for 0 < theta < pi and every R > 0; the limit D_0phi needs U = O(r^(-alpha)), DU = O(r^(-alpha - 1))
   and a mean-swirl tail F_0phi(theta).

23. Constructive non-axisymmetry threshold [I: consulted answer checked step by step, derivations/d59_nonaxi1_audit.md
   and d59_nonaxi1_constants.py; independently proved by the independent validation route
   (theory/constructive_mean_bound in its artifacts) with controls, CONFIRMED for decaying U at 2026-10-25T04:52Z; now
   [I] at 2026-10-25T05:05:46Z]. Hypothesis U(y) -> 0 required (U = e_3 refutes its omission); decay gives |U| <= A
   h^(-alpha)/alpha and A > alpha (equality excluded; supplement below). With max|U| = 1, h = 1 + |y|, u' = U - <U>,
   delta_j = sup h^(alpha + j) |D^j u'| and global A = max(1, sup h^(alpha + 1)|DU|), B = max(1, sup h^(alpha + 2)|D^2
   U|): ||<U>||_inf <= C_G G^gamma + C_F F^theta, with G = (delta_0 delta_1 + sigma)/a, F = 2(delta_1^2 + delta_0
   delta_2) + kappa, sigma = sup|rho <R_u . e_phi>|, kappa = sup|(curl <R_u>)_phi|, gamma = alpha/(3(alpha + 2)),
   theta = alpha lambda/((alpha + 2)(lambda + A)), lambda = 1 + c_l, and C_G, C_F explicit and independent of omega.
   Exact profiles have delta_0 >= delta_*(c_l, A, B) > 0, numerically vacuous (9.9e-10 at the boundary value A = alpha
   of the admissible range, B = 1, c_l = 0.45; d59b). Residual corollary: sigma >= a max|Gamma_0| - max|S|. No
   obstruction. FINAL_REPORT.md section 2 item 28.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 28) [I; the exclusion of A = alpha is a
   supplement to the independent proof (2026-10-25T05:19Z), checked by the review]. The admissible range is A > alpha:
   decay and max|U| = 1 give A >= alpha, and equality would put the maximum at the origin and force dU/dr = -alpha
   U(0) there along a ray, which contradicts the vanishing derivative of |U|^2 at an interior maximum. The global
   weighted bounds are stronger than the core-ball bounds of item 12 (b), delta_* is a computed version of item 12 (b)
   in a weighted global norm, and kappa needs only U, DU and D^2 U. The residual corollary holds for every field of
   the class because |Gamma_0| vanishes on the axis, decays at infinity and so attains its maximum at an interior
   point, where W_0 . grad Gamma_0 = 0; when max|S| > 0 its right side is max|S| (Q_sw - 1) with Q_sw = (1 - 2c_l)
   max|Gamma_0|/max|S|, and applied to sampled maxima it is a numerical consistency check, not an enclosed lower
   bound. A mean bound from weighted L^2 residuals alone is impossible: dilations V(y/eps) of a compactly supported
   swirl at fixed amplitude, with pressure P_V(y/eps), have no eddies, mean norm one and residual tending to zero in
   the weighted L^2 norm with weight (1 + r)^w for w < 5/2, and w = alpha + 1 is admissible exactly when c_l > 2/5;
   these fields have zero leading tail, so they are outside the target class, and their sup residual diverges, so they
   are not near-profiles in the sup sense.
24. First far-field energy coefficient [I: lead derivation d67; independent proof with the sufficient hypothesis,
   reviewed by the lead in derivations/d68_review_far_coefficient_proof.md; recorded 2026-10-25T06:56Z]. With U_0 = r^(-alpha) F
   twisted-homogeneous, P_0 = r^(-2 alpha) Q its unique twisted-homogeneous pressure and U_1 = (U_0 . grad)U_0 + grad P_0 =
   r^(-2 alpha - 1) G: int_(S^2) F . G dS = (2 - 3 alpha) Phi_F, Phi_F = int_(S^2) F_r (|F|^2/2 + Q) dS. If |D^j(U - U_0)| =
   O(r^(-alpha - 1 - j)), j = 0, 1, with the whole-space pressure, then E_F(s) = int |F|^2 + 2 (2 - 3 alpha) Phi_F
   s^(-(alpha + 1)) + O(s^(alpha - 4)); there is no s^(-2) term, and s^(alpha - 4) is the first allowed rate, not a
   proved nonzero one. P = O(r^(-2 alpha)) alone permits an exterior eps r^(-3) Y_2m. FINAL_REPORT.md section 2 item 30.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 30) [I]. Here U_0 is a smooth
   divergence-free twisted-homogeneous field on R^3 minus the origin, and the expansion is stated for a smooth exact
   profile U with its decaying whole-space pressure, with E_F(s) = s^(2 alpha) int_(S^2) |U(s n)|^2 dS and K_1 = 2
   (2 - 3 alpha) Phi_F. Q is unique in the twisted-homogeneous class: the mode multiplier l(l + 1) - s_m (s_m + 1),
   s_m = -2 alpha + i m omega/c_l, has imaginary part m (omega/c_l)(4 alpha - 1) for m != 0, and for m = 0 it would
   vanish only if l(l + 1) = 2 alpha (2 alpha - 1), which lies strictly between 2 and 6. The sphere identity uses no
   profile equation: U_0 . U_1 = div(U_0 (|U_0|^2/2 + P_0)), integrated over 1 < r < s, with 2 - 3 alpha != 0. Under
   the hypothesis of the expansion, U = U_0 + U_1 + O(r^(-4)) uniformly in angle; when Phi_F != 0, E_F(s) - int_(S^2)
   |F|^2 eventually has the sign opposite to Phi_F (no radius beyond which this holds is given), and when Phi_F = 0
   the first term vanishes. The exterior harmonic eps r^(-3) Y_2m leaves Q and the sphere identity unchanged; the
   whole-space convention fixes the later multipoles. Nothing here concerns existence.
25. Local vorticity representation [I: lead d64 part C; independent derivation and exact controls (27 of 27); reviewed
   by the lead in derivations/d69_review_lamb_lemma.md; recorded 2026-10-25T06:56Z]. For C^2 divergence-free U and C^2
   single-valued P near a closed origin-centred ball B: Omega(y_0) = int_(-infinity)^0 e^s e^(omega s J)[curl(U x Omega)
   + curl R_u](e^(c_l s) e^(-omega s J) y_0) ds, so sup_B|curl R_u| >= sup_B|Omega| - sup_B|curl(U x Omega)|; an exact profile
   with a gradient Lamb vector on B has Omega = 0 on B. The helicity flux through S_R has leading term (c_l/2) H_F
   R^(2 - 2 alpha) (not O(R^(1 - 3 alpha)) when H_F != 0). Local necessary condition, not an obstruction. FINAL_REPORT.md
   section 2 item 31.
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 31) [I]. The representation uses no decay,
   symmetry or tail, and its integral converges absolutely; an exact profile has |Omega(y_0)| at most the supremum of
   |curl(U x Omega)| on the ball of radius |y_0|. The flux statement assumes that U and Omega have differentiated
   twisted-homogeneous tails of rates alpha and alpha + 1 and that P = O(r^(-2 alpha)): in int_(B_R) Omega . R_u =
   (1 - 2 c_l) int_(B_R) U . Omega + int_(S_R) B Omega . n, with B = U . ((c_l I - omega J) y) + |U|^2/2 + P
   (the B of item 13), the flux has leading term (c_l/2) H_F R^(2 - 2 alpha), H_F = int_(S^2) F . H, which cancels
   against the exterior helicity H_F R^(2 - 2 alpha)/(2 alpha - 2), so an exact profile has H_tot = 0. A ratio of
   sampled maxima gives no one-sided bound and does not certify the inequality of item 25.
26. First far-field helicity coefficient [I: lead derivation d78, symbolic identity with negative control and sampled
   checks on six exports; independently proved by the independent route at 2026-10-25T09:35Z, including the remainder
   argument below, reviewed in d81; recorded 2026-10-25T09:28Z, label updated 09:42Z]. For smooth U, P with N = (U . grad) U + grad P
   and h = U . Omega: U . curl N + N . Omega = div(h U + (P - |U|^2/2) Omega), with no divergence condition. Under the
   hypothesis of item 24, s^(2 alpha + 1) int_(S^2) h (s n) dS = H_F + K_H s^(-(alpha + 1)) + O(s^(alpha - 4)) (proof
   through the sphere-averaged exact helicity balance h_F' = -(1/c_l) s^(2 alpha - 2) T', T the flux of the identity
   through |y| = s, which needs only U, DU and P; independent route 09:35Z, reviewed by the theory route), with
   K_H = (1 - 3 alpha) Psi_F and Psi_F = int_(S^2) [(F . H) F_r + (Q - |F|^2/2) H_r] dS. Together with item 24 this gives
   two projections of the first correction that an exact profile carries at ratio 1. Not an obstruction.
   FINAL_REPORT.md section 2, item 34 (values on the exports: section 2b, item 8).
   Supplement (synchronized 2026-10-26 with FINAL_REPORT.md section 2, item 34) [I]. The identity needs only C^2 U and
   P, and it fails with P + |U|^2/2 in place of P - |U|^2/2. With Omega_0 = curl U_0 = r^(-alpha - 1) H and U_1 as in
   item 24, int_(S^2) (F . curl U_1 + U_1 . H) dS = K_H, the curl taken in R^3 and evaluated on r = 1; no profile
   equation is used (the left side of the identity for (U_0, P_0) is twisted-homogeneous of degree -(3 alpha + 2), its
   flux field of degree -(3 alpha + 1), and 1 - 3 alpha != 0). The expansion of h_F(s) = s^(2 alpha + 1) int_(S^2)
   h(s n) dS is stated for a smooth exact profile; a direct substitution of U = U_0 + U_1 + O(r^(-4)) into h would
   need an O(r^(-5)) bound on the derivative of that remainder, which item 24 does not state, and the flux equation
   avoids it. Consequently int_(r > s) h = H_F s^(2 - 2 alpha)/(2 alpha - 2) + K_H s^(1 - 3 alpha)/(3 alpha - 1) +
   O(s^(-alpha - 2)). If the rate-(2 alpha + 1) part of an approximate field is V_1, its carried coefficients are
   K_1(carried) = int_(S^2) 2 U_0 . V_1 and K_H(carried) = int_(S^2) (U_0 . curl V_1 + V_1 . Omega_0) at r = 1; an
   exact profile has V_1 = U_1, so both ratios carried/required equal 1 whenever the required value is nonzero; the
   two ratios are different projections of the defect V_1 - U_1, and equality of either does not imply V_1 = U_1.
27. Artificial-viscosity identities (used only to design a labelled continuation device, never as Euler results) [I:
   (a) to (e) independent proof with symbolic and Gaussian controls and a wrong-factor negative control, reviewed, the
   commutator also checked symbolically, recorded 2026-10-25T05:15Z; (f) to (i) derived from a consulted answer and
   independently confirmed with symbolic and Gaussian checks and a wrong-sign negative control, recorded
   2026-10-25T05:35Z]. Regularized equation R^nu = R_u - nu Delta U = 0 with constant nu > 0, under the differentiated
   tail U = r^(-alpha) F + O(r^(-alpha - delta)), delta > 3 - 2 alpha, and P = O(r^(-2 alpha)). (a) The Euler
   full-space pressure is unchanged, since div Delta U = 0. (b) With E_ren the finite part of int_(B_R) |U|^2 and
   beta_0 = 1 - 5 c_l/2 < 0, every exact solution has beta_0 E_ren + nu int_(R^3) |grad U|^2 = 0, so E_ren > 0 for
   every nonzero solution; for an approximation, lim int_(B_R) U . R^nu equals the left side. The ten
   independent-route states evaluated in FINAL_REPORT.md section 6.4 have E_ren from -1.021 to -0.519; their energy
   defect lim int_(B_R) U . R_u = beta_0 E_ren > 0 has the sign of a negative viscosity, and an exact viscous solution
   would need E_ren to change sign, to a positive value. This gives no quantitative distance from these states to
   viscous solutions. (c) U_L(y) = L U(y/L) maps a solution with viscosity nu to one with viscosity L^2 nu; when
   int_(S^2) |F|^2 > 0, the quantity nu (int_(S^2) |F|^2)^(-1/(alpha + 1)) is invariant. (d) Formally, the first
   viscous far-field correction is -(nu/(2 c_l)) Delta U_0, of rate alpha + 2, because [y . grad, Delta] = -2 Delta
   and the rotation generator commutes with Delta; it is divergence free and precedes the nonlinear rate 2 alpha + 1
   (alpha > 1), and the rate-(alpha + 1) coefficient remains zero. (e) A localized viscosity nu(y) needs the operator
   specified. For -nu(y) Delta U the energy relation gains -(1/2) int (Delta nu) |U|^2 and loses its sign, and the
   pressure source gains -grad nu . Delta U = -div(nu Delta U), which can produce a pressure dipole of order r^(-2):
   for compactly supported nu this source has zero mass and first moment int nu Delta U, which need not vanish, so the
   pressure gains (y . M)/(4 pi |y|^3) with M = int nu Delta U (proved by the independent route and checked by the
   lead; it says a dipole can occur, not that every field has one); a nonzero dipole is incompatible with P =
   O(r^(-2 alpha)), so in this branch that assumption must be rechecked, while the pressure part of the boundary
   energy flux still vanishes, as R^(-alpha). For -div(nu grad U) the energy relation keeps the form beta_0 E_ren +
   int nu |grad U|^2 = 0, and the pressure source gains -grad nu . Delta U - sum_ij (d_i d_j nu) d_j U_i, a double
   divergence. (f) Differentiating (c) at dilation factor 1 at an exact solution gives (L - nu Delta +
   DN(U))(U - y . grad U) = 2 nu Delta U, with L the linear part of R_u and N(U) = (U . grad) U + grad P, so for nu >
   0 the dilation generator is not a null direction of the linearization, unlike the inviscid case. (g) At fixed
   (c_l, omega), dilation maps the solutions for any nu > 0 to solutions for every other nu > 0, so scaling alone
   cannot lower nu in the fixed gauge int_(S^2) |F|^2 = 1; a separate solution family at fixed (c_l, omega) is not
   excluded by this argument. (h) L - nu Delta is injective on C^2 uniformly decaying fields (maximum principle for
   |U|^2/2, using 1 - c_l > 0). (i) At the maximum of |Omega|, a nonzero C^3 solution with U and Omega decaying has
   Omega . S Omega = |Omega|^2 - nu Delta(|Omega|^2/2) + nu |D Omega|^2 >= |Omega|^2, so sup lambda_max(S) >= 1 (the
   viscous analogue of item 12 (a)); hence every such solution (C^3, with U and Omega decaying) with sup |DU| < 1 is
   zero, and no nonzero branch bifurcates from U = 0 in any norm that controls sup |DU| (C^1, for example). The linear
   injectivity (h) alone gives no nonlinear small-solution statement, and no statement in terms of sup |U| alone is
   claimed. None of (a) to (i) says anything about existence for either equation. FINAL_REPORT.md section 2, item 29.
28. Representation bounds for the primary basis (statements about the representation, not about the equation) [I:
   independent proofs, each reviewed with separate symbolic, high-precision and end-to-end checks; recorded
   2026-10-25T07:14Z, 07:23Z and 07:33Z]. Let U = curl(T y) + curl curl(Psi_p y) (toroidal potential T, poloidal
   potential Psi_p) be a finite sum of the primary channels (twisted A and C, damped B and D, untwisted E with l >= 2)
   with fixed coefficients, Omega = curl U, and U0 its leading field: A and C at their endpoint sums, sqrt(r^2 + R0^2)
   replaced by r, twist (omega/c_l) log(r/R0). (a) For R with R0/R below the radius of the Cauchy disk in w = R0/r
   used in the proof, on every sphere of radius r >= R, |U - U0| <= sum_j u_j r^(-b_j) and |Omega - Omega0| <= sum_j
   o_j r^(-b_j - 1), with explicit constants from Cauchy estimates of the compactified radial amplitudes on that disk;
   the rates b_j are alpha + 1 (from the endpoint derivatives q'(1) of A and C), alpha + 2, 2 alpha + 1 (B and D) and
   l + 2 (E), all above 3 - alpha. Integration bounds the omitted exterior finite-part energy and the omitted signed
   and absolute helicity beyond R, after their leading terms, without any profile equation. The rate-(alpha + 1) part
   decays only like R^(2 - 2 alpha), so at the radii used the bound is small only because q'(1) is small (at most
   1.8e-11 on the exports). (b) The leading moments are exact quadratic forms in the endpoint sums. With a_c, a_s and
   c_c, c_s the cosine and sine endpoint sums of mode (l, m) in channels A and C and L_l = l(l + 1), mode (l, m)
   contributes L_l R0^(2 alpha + 2l) (a_c^2 + a_s^2) + L_l (L_l + (2 - alpha)^2 + (m omega/c_l)^2)
   R0^(2 alpha + 2l - 2) (c_c^2 + c_s^2) to int_(S^2) |F|^2, and 2 L_l R0^(2 alpha + 2l - 1) [(L_l + (m omega/c_l)^2)
   X + (m omega/c_l)(2 - alpha) Y], with X = a_c c_c + a_s c_s and Y = a_s c_c - a_c c_s, to the leading helicity
   coefficient H_F of item 25; the enstrophy moment, the m > 0 energy fraction e_F and N_F^2 = sum m^2 E_lm /
   int_(S^2) |F|^2 (E_lm the contribution of mode (l, m) to int_(S^2) |F|^2) follow in the same way, without angular
   quadrature (the quotients e_F and N_F need int_(S^2) |F|^2 > 0). The sign of the Y term refers to the convention in
   which the cosine and sine harmonics belong to the same complex harmonic and the field is a function of phi +
   (omega/c_l) log r; the opposite convention changes H_F. (c) With t(R) = R^(2 - 2 alpha)/(2 alpha - 2) and B_H(R)
   the helicity remainder bound of (a), the signed exterior helicity beyond R lies in [t(R) H_F - B_H(R), t(R) H_F +
   B_H(R)], and the absolute exterior helicity lies in [max(0, t(R) |H_F| - B_H(R)), t(R) (int_(S^2) |F|^2 int_(S^2)
   |H|^2)^(1/2) + B_H(R)] (triangle inequality and Cauchy-Schwarz on the sphere; the logarithmic rotation preserves
   the sphere measure, so the angular integrals do not depend on the radius). All three are statements about the
   representation, not about the equation, and none bounds a finite-domain quadrature. FINAL_REPORT.md section 2, item
   32.
29. Vorticity flow and vorticity zeros [I: independent proofs, each reviewed step by step, 2026-10-26]. Let U be an
   exact C^2 profile with C^2 pressure and U = o(|y|) uniformly, W = (c_l I - omega J) y + U and Omega = curl U. For
   every omega and every omega/c_l the curl of the profile equation gives the exact bracket D Omega W - DW Omega =
   -(1 + c_l) Omega (the rotation terms commute with the curl because J y generates rotations). Hence the backward
   flow Psi_t of W (the flow of -W) satisfies D Psi_t(p) Omega(p) = e^(-(1+c_l)t) Omega(Psi_t(p)); it maps vortex
   lines to vortex lines with their parameter rescaled by e^(-(1+c_l)t), and all backward images of a compact set stay
   in one ball. (a) Omega has no nonconstant periodic integral curve, so no closed vortex line carries nonzero
   vorticity: the backward images of such a curve of period T would be periodic vortex lines in one ball with periods
   e^(-(1+c_l)t) T -> 0, below the minimum period 4/Lambda of a field with Lipschitz constant Lambda on that ball. (b)
   On every compact set invariant under the vorticity flow (the flow of Omega), the derivative of that flow grows
   subexponentially in time (all its Lyapunov exponents vanish) and its time-one map has topological entropy zero.
   Such a set may consist of vorticity zeros, and no nontrivial one is asserted to exist. This concerns the vorticity
   flow, not the backward flow of W, whose exponents item 7 describes. (c) If Omega(p) = 0, then (D Omega(p))^3 = 0:
   the zero is carried backward to zeros q_t in the same ball, and D Omega(q_t) is similar to e^((1+c_l)t) D Omega(p),
   so every complex eigenvalue of D Omega(p) vanishes. In particular det D Omega(p) = tr((D Omega(p))^2) = 0, so an
   exact profile has no nondegenerate vorticity zero; D Omega(p) need not vanish, and isolated degenerate zeros are
   not excluded. (d) Local exclusion. Let V be a C^2 field on a closed ball B of radius r_0 about q, Z = curl V, and M
   an invertible matrix with |M Z(q)| <= eta and sup_B ||I - M DZ|| <= kappa_0. If d_0, d_1 >= 0, kappa_0 + d_1 < 1
   and eta + d_0 < (1 - kappa_0 - d_1) r_0, then no exact profile of the class satisfies |M curl(U - V)(q)| <= d_0 and
   sup_B ||M D curl(U - V)|| <= d_1: by contraction such a U would have a vorticity zero in B at which D curl U is
   invertible, against (c). It suffices that ||D(U - V)(q)||_F <= d_0/(sqrt(2) ||M||) and sup_B ||D^2(U - V)||_F <=
   d_1/(sqrt(2) ||M||), so the excluded set contains a C^2 neighbourhood of V. The suprema must be verified bounds,
   not sampled values; no saved state has been tested against (d). These are necessary conditions on an exact profile;
   none of them excludes the class. FINAL_REPORT.md section 2, item 35.
30. Vorticity-amplitude identities [I: independent proof, reviewed step by step with a manufactured-field check,
   2026-10-26]. Let U be a C^2 divergence-free field, W = (c_l I - omega J) y + U, a = |Omega|, e = Omega/a and s = e
   . DU e on {a > 0}, and R_Omega = Omega + (W . grad) Omega - (Omega . grad) U + omega J Omega, the curl of the
   momentum residual (no pressure enters). Then W . grad a = (s - 1) a + e . R_Omega, and div W = 3 c_l. (a) If a -> 0
   uniformly at infinity, then for every psi in C_c^1((0, infinity)), int [3 c_l psi(a) + (s - 1) a psi'(a)] dy = -int
   psi'(a) e . R_Omega dy, which vanishes for an exact profile. On a bounded domain B with outward normal n both
   integrals are taken over B and the boundary flux is subtracted from the left side, which becomes int_B [3 c_l
   psi(a) + (s - 1) a psi'(a)] dy - int_(dB) psi(a) W . n dS. When the L^2 norm of psi'(a) on the domain is positive,
   Cauchy-Schwarz bounds the L^2 norm of R_Omega on the support of psi'(a) from below by the absolute value of the
   left side divided by that norm; when it is zero the identity gives no bound. The left side and the norm of psi'(a)
   need U and DU only. The bound holds for exact integrals; quadrature values are readings, not certified bounds. (b)
   For an exact profile with a -> 0 at infinity and a regular value t > 0 of a whose superlevel set {a > t} is
   nonempty, the average of s over the level set {a = t} with weight 1/|grad a| equals 1 - 3 c_l vol(t)/(t g(t)) < 1,
   where vol(t) is the volume of {a > t} and g(t) the integral of 1/|grad a| over that level set. At a positive
   maximum of a the identity gives s = 1 for an exact profile (section 2, item 5), while these level averages lie
   strictly below 1. These are identities with the residual retained, not an obstruction. FINAL_REPORT.md section 2,
   item 36.

Not available: the non-rotating Liouville theorem of the companion study (stated there for 0 < c_l < 1/2 with a
proof its authors call informal) is not used as an input, and its Bernoulli step fails for omega != 0 (item 2.2).
The exclusion theorems for discretely self-similar Euler solutions of Chae and Tsai (arXiv:1304.7414) do not cover
this tail class because their integrability or L^2 hypotheses fail for it. Xue (arXiv:1408.6619, Theorem 1.1(1))
does apply to exponents in the target range, but its conclusion is the alternative "zero velocity or ball energy
growing like R^(3-2alpha)", which the natural tail satisfies; it is a compatibility condition, not an exclusion
(corrected 2026-10-25 to agree with FINAL_REPORT.md section 2, item 5). The full text of D. Chae, "Removing rotated
discretely self-similar singularity for the Euler equations", J. Differential Equations 377 (2023) 113-120, was not
accessible on 2026-10-24 or 2026-10-25 (publisher 403; no preprint in arXiv, Crossref or OpenAlex); its
applicability is not assessed. CIV Thm 2.1 (c_l >= 2/5 for a smooth finite-energy Euler blowup with
sup (T-t)^(1+c_l) ||grad omega||_inf finite) is a physical-time statement with no similarity ansatz, so it does not
restrict omega. CIV Thms 3.8-3.9 (c_l >= 1/2 under outgoing conditions; Thm 3.9 for a nontrivial C^2 profile with the
decay (3.8), the normalization (3.7) ||D^2 U||_inf = 1 and a finite nodal set with the local outgoing property of
their Definition 3.7) and Thm 4.5 (nontrivial C^2 axisymmetric profiles with (3.5), U(0) = 0 and U = o(|y|), and
(3.8)) concern non-rotating profiles. Together with Thm 2.1 they bracket the target range; item 11 records what
transfers. B. Pineau and V. Vicol (arXiv:2607.09619v2) treat rotated self-similar Navier-Stokes solutions and are
not used.

Hypothesis map (FINAL_REPORT.md section 2, item 5; theorem texts read; checked by the independent route). The
hypotheses are applied to the profile-variable field V(y, s) = exp(omega s J) U(exp(-omega s J) y), periodic in s with
period 2 pi/|omega| and with spatial norms independent of s, whose similarity exponent is alpha. Chae-Tsai Theorem 2.1
needs the vorticity in L^q for all sufficiently small q > 0 and Theorem 2.2 in some L^q with 0 < q < 3c_l, while a
nonzero differentiated leading tail has vorticity in L^q only for q > 3c_l; their Theorem 3.1 needs space-time L^2
velocity, which fails for alpha < 3/2; their Theorem 3.2 (velocity in L^p, p >= 3) excludes alpha <= 3/p or alpha >
3/2, which misses 1 < alpha < 3/2. Xue's Theorem 1.1(1) needs C^1 in s and C^3 in y, the full-space pressure formula
and V in L^3_s L^p_y with p >= 3 (true for the tail class with p = 3; C^3 is an extra regularity requirement). These
statements concern the tail class and would have to be re-checked against any candidate, with its own decay.

Open: existence or nonexistence of a nonzero decaying non-axisymmetric rotating profile in the target range.

## 8. Integral identities used as diagnostics

Ball laws (exact for every R; [V, d04] for the conservation forms):
- energy: (c_l/2) R E'(R) - ((5c_l-2)/2) E(R) = -R^2 integral_{S^2} (K + P) U_r dOmega, hence
  E(R) R^(2alpha-3) -> K_E = (c_l/(5c_l-2)) integral |F|^2 with remainder O(R^(-(alpha+1))) and no finite part;
- angular momentum A(R) = integral_{B_R} (y_1 U_2 - y_2 U_1) and momentum V(R) = integral_{B_R} U satisfy
  c_l R A' - (5c_l - 1) A = boundary flux and c_l R V' + ((1-4c_l) I + omega J) V = boundary flux, with no finite part;
- helicity: (1-2c_l) integral_{B_R} h = -(1/2) integral_{dB_R} [ (W.n) h + (Omega.n)(P - K) ] dS; the total
  helicity is zero and the ball value decays like -R^(2-2alpha) integral_{S^2} F.H dS/(2alpha-2);
- virial: integral_{B_R} (|U|^2 + 3P) dy = R integral_{dB_R} (U_r^2 + P) dS for every R, for all c_l and omega
  [V, d05]; with the energy law it gives FP_{R->inf} integral_{B_R} P dy = 0.
Global weighted identities (absolutely convergent; exact local divergence forms [V, d05b], global limits by the
boundary terms W.n = c_l R + U_r and the natural tail):
- (E)   integral r^(2alpha-4) U_r (K + P) dy = -c_l integral_{S^2} |F|^2 dS/(2(3-2alpha));
- (O)   integral r^(2alpha-1) [ Omega.S Omega + (2alpha-1)(U_r/r)|Omega|^2/2 ] dy = (c_l/2) integral_{S^2} |H|^2 dS;
- (Hel) (2alpha-2) integral r^(2alpha-4) [ (y.U) h + (y.Omega)(P - K) ] dy = c_l integral_{S^2} F.H dS.
None of the integrands has a sign, so these are consistency checks for candidates (with the corresponding
weighted residual integrals reported alongside), not obstructions. (E), (O), (Hel) and the virial law are [I].
Further identities [local forms V, d08; global limits P]:
- the virial law is a pressure-consistency identity: integral_{B_R} y.R_u = -integral_{B_R} ((R^2 - r^2)/2) R_P, so it
  holds for every divergence-free U with its exact full-space pressure, whatever R_u; leading coefficient
  integral_{S^2} Q = (q integral F_r^2 - integral |F|^2)/(2alpha), q = 3-2alpha;
- total stretching (Z0): integral Omega.S Omega dy = (1 - 3c_l/2) integral |Omega|^2 dy > 0, the m = 0 member of the
  family integral r^m [Omega.S Omega + (m/2)(U_r/r)|Omega|^2 - (1 - 3c_l/2 - m c_l/2)|Omega|^2] dy = 0 for
  -3 < m < 2alpha-1 (absolutely convergent at the origin for -2 < m, or -3 < m if U(0) = 0; otherwise a
  spherical improper integral) [I], and = (c_l/2) integral |H|^2 at m = 2alpha-1 (this is (O)); ratios
  Sigma_Z = integral Omega.S Omega/((1 - 3c_l/2) integral |Omega|^2) and
  Sigma_E = -2(3-2alpha) integral r^(2alpha-4) U_r (K+P)/(c_l integral |F|^2) equal 1 for an exact profile;
  residual form (from item 5 integrated, same decay): (1 - 3c_l/2) Z - integral Omega.S Omega = integral Omega.R_Omega,
  so (1 - Sigma_Z)(1 - 3c_l/2) Z = integral Omega.R_Omega and, by Cauchy-Schwarz,
  ||R_Omega||_L2 >= |1 - Sigma_Z| (1 - 3c_l/2) ||Omega||_L2 [R, added 2026-10-24T21:22Z]; a converged Sigma_Z far from 1 is a
  lower bound on the vorticity residual of an approximate state;
- special conformal fields K_a = 2(a.y)y - r^2 a: [(1-6c_l) I + omega J] FP integral_{B_R}[2y(y.U) - r^2 U]
  = 2 FP integral_{B_R} y(|U|^2 + 3P);
- angular momentum to next order: A(R) = a_F R^(4-alpha)/(4-alpha) + a_0 R^(3-2alpha) + O(R^(2-3alpha)) with
  a_F = integral sin(theta) F_phi, a_0 = integral F_r sin(theta) F_phi [I]; momentum is kinematic
  (integral_{B_R} U = integral_{dB_R} y U_r);
- residual error formulas: FP E = -(2/(5c_l-2)) integral U.R_u, FP A = -(1/(5c_l-1)) integral (Jy).R_u,
  total helicity = (1/(1-2c_l)) integral Omega.R_u.
- velocity from vorticity (Biot-Savart) [I, proved by the independent route; lead-reviewed line by line, d19; ray
  form V, d19_biot_savart_check.py]: if div U = 0, U is C^2, |U| -> 0 and |DU| <= C (1 + |y|)^(-alpha-1) with
  alpha > 1, then U(x) = (1/4pi) integral Omega(y) x (x - y)/|x - y|^3 dy = (1/4pi) integral_{S^2} integral_0^inf
  n x Omega(x + rho n) drho dS(n), absolutely convergent. The twisted tail satisfies the hypothesis (the rotation by
  (omega/c_l) log r is orthogonal with derivative O(r^-1)). For a curl representation this is a check of derivative
  conventions, exported vorticity and exterior continuation, not of the Euler balance.
- momentum-residual lower bounds [R, added 2026-10-24T22:27Z; external answer reviewed in d20, exact checks d22]: with
  B = U.W - K + P one has grad B = W x Omega - (1 - 2c_l) U + R_u and U.R_u = (2 - 5c_l) K + div(WK + UP);
  Omega.curl R_u - R_u.curl Omega = div(R_u x Omega). Hence, for the natural tail, integral R_u.curl Omega =
  (1 - 3c_l/2)(1 - Sigma_Z) Z and ||R_u||_{L2(w)} >= (1 - 3c_l/2)|1 - Sigma_Z| Z / ||curl Omega||_{L2(1/w)} with
  w = (1 + r)^(-2 sigma), 3/2 - alpha < sigma < alpha - 1/2; and (1 - 2c_l) integral g(B) U.Omega = integral g(B)
  Omega.R_u up to a boundary term (helicity push-forward). Per-shell Cauchy-Schwarz converts either into a lower bound on
  rho_u^max. These bound the momentum residual of a given state; they are not floors for a class without uniform
  bounds on the class.

## 9. Verification scripts

derivations/d01_cartesian_identities.py (section 2 identities, generic functions), d02 (far-field leading and first
nonlinear orders, seed family), d03 (Taylor conditions, Green formula, resonance arithmetic), d04 (ball laws),
d05_virial.py and d05b_weighted.py (virial and weighted identities on random exact polynomial fields),
d06_obstruction_checks.py (angular momentum, rotating Bernoulli, vorticity transport, axisymmetric no-swirl
transport, exact potential-flow examples), d07_backward_stretching.md (proof note, item 7.7),
d08_integrallaws_checks.py (local forms of the further identities of section 8), d09_paramcount_checks.py (saddle
germ, tail parameter derivatives, Burgers selection, eigenvalues at zeros of W; item 7.9), d10_kelvin_checks.py
(Kelvin form and invariant-measure identities; item 7.8). d19_biot_savart_check.py (ray form of the Biot-Savart law
with a twisted algebraic tail, alpha = 11/9). d21_forced_recovery_check.py (pressure source without rotation terms,
the momentum and pressure-source difference identities used by the forced optimizer test, quotient-rule Jacobian of
the shell residual). d22_floor1_checks.py (residual lower-bound identities, manufactured twisted tail and its first
nonlinear coefficient, Bernstein widths of the compactified core). d23_helicity_checks.py (helicity push-forward
identity, its decay and the exterior substitution). Each script has a .log file with PASS/FAIL lines. Line-by-line
review notes for the decay, axisymmetric and dynamics proofs: derivations/obstruction_notes.md.
