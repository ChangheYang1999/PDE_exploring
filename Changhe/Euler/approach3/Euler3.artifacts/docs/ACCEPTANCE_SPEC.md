# SPEC: rotating backward self-similar Euler profiles, 2/5 < c_l < 1/2, omega != 0

Version: v1.24, 2026-10-25T09:54:00Z (v1.23 2026-10-25T08:14:16Z, v1.22 2026-10-25T02:49:47Z, (c) clarified 2026-10-25T02:53:01Z; v1.21 2026-10-25T02:23:11Z, v1.20 2026-10-25T01:44:56Z, v1.19 2026-10-25T01:28:56Z, 11c V10 and combined-reading wording qualified 01:36Z; v1.18 2026-10-25T01:23:08Z, v1.17 2026-10-25T01:16:37Z (reason wording qualified 01:28Z), v1.16 2026-10-24T23:41:53Z, change-log wording corrected 2026-10-24T23:57:29Z, V7 registration chronology corrected 2026-10-25T00:17Z, V7 ratio wording qualified 2026-10-25T00:53Z; v1.15 23:32Z, v1.14 23:19Z, v1.13 23:10Z, v1.12 23:04Z, v1.11 22:40Z, v1.10 22:10Z, v1.9 21:57Z, v1.8 20:16Z, v1.7 19:25Z, v1.6 19:17Z, v1.5 19:06Z, v1.4 18:49Z, v1.3 18:41Z, v1.2 18:25Z, v1.1 18:07Z, v1 17:52Z, v0 17:28Z, v0.1 17:33Z, v0.2 17:37Z), lead lane. Binding for the numerics and
verifier lanes. v1 applies the independent audit (astra specaudit1) of sections 1 to 8 after the lead checked each
claim (section 12). Any later change to section 8 (acceptance thresholds) is recorded in section 12 with the
original kept, never silently replaced; v1 only ADDS requirements and tightens one allowance (section 12).
Status of each statement: [V] verified by an executed symbolic/numerical check (script named),
[H] derived by hand, check pending, [A] awaiting independent audit, [C] conjecture or search assumption.

Campaign clock: T0 = 2026-10-24T17:09:12Z. Stage I ends T0+30h = 2026-10-25T23:09Z, Stage II ends
T0+72h = 2026-10-27T17:09Z, Stage III ends T0+96h = 2026-10-28T17:09Z.

Notation: c_l (scaling exponent), omega (rotation), omega/c_l written out, alpha = (1-c_l)/c_l in (1, 3/2),
1/c_l = alpha + 1. Spherical coordinates (r, theta, phi), theta polar, phi azimuth;
chi = phi + (omega/c_l) log r. Spherical components refer to the local basis e_r, e_theta, e_phi.
J = [[0,-1,0],[1,0,0],[0,0,0]], J v = e_3 x v. y_h = (y_1, y_2, 0).

## 1. Equations

    R_u     = (1-c_l) U + (W.grad) U + omega J U + grad P,          W = (c_l I - omega J) y + U,
    R_Omega = Omega + (W.grad) Omega + omega J Omega - (Omega.grad) U, Omega = curl U,
    R_div   = div U,
    R_P     = -Delta P - sum_ij (d_i U_j)(d_j U_i).

Verified identities (derivations/d01_cartesian_identities.py, exact sympy with generic functions):
- [V] curl R_u = R_Omega + Omega div U for every smooth U (generic, not necessarily divergence free); so
  curl R_u = R_Omega exactly when div U = 0.
- [V] div W = 3 c_l + div U; curl W = Omega - 2 omega e_3.
- [V] R_Omega = (1+c_l) Omega + [W, Omega] (Lie bracket (W.grad)Omega - (Omega.grad)W).
- [V] Bernoulli form: R_u = grad Be - W x Omega + (1-2c_l)(c_l y + U), with
  Be = |W|^2/2 + P + c_l(c_l-1)|y|^2/2 - omega^2 |y_h|^2/2 (called Be, not H, to avoid the clash with the tail
  vorticity coefficient H of 3.1). The term (1-2c_l)(c_l y + U) =
  (1-2c_l)(W + omega J y) contains the non-gradient part (1-2c_l) omega J y; this is why the non-rotating
  Lyapunov argument does not transfer directly (see section 2.6).
- [V] Energy density: U.R_u = (2-5c_l)|U|^2/2 + div(W |U|^2/2 + U P) when div U = 0.
- [V] Helicity density: Omega.R_u + U.R_Omega = (2-4c_l) U.Omega + div(W (U.Omega) + Omega (P - |U|^2/2)).
- [V] Vorticity amplitude: Omega.R_Omega = |Omega|^2 + W.grad(|Omega|^2/2) - Omega.(DU)Omega. Hence at a
  nonzero global maximum of |Omega| of an exact smooth decaying profile, Omega.sym(DU)Omega = |Omega|^2, so
  lambda_max(sym DU) >= 1 there. (v1.3) The same equality holds at EVERY critical point of |Omega|^2 (local maxima,
  minima, saddles), since the transport term vanishes there. [CONFIRMED by the independent route, 2026-10-24T18:52Z,
  for C^2 exact profiles; at a numerically located critical point the transport term must be measured.]
- [V, d10] Self-similar Kelvin form (v1.3): W_j d_j U_i + U_j d_i W_j = -(1-2c_l) U_i + d_i(|U|^2/2 - P) + (R_u)_i for
  every smooth U, P (derivations/d10_kelvin_checks.py).
- [V] Physical ansatz: with E(s) = exp(omega s J), V(z,s) = E(s) U(E(s)^T z), Pi(z,s) = P(E(s)^T z),
  d_s V + (1-c_l)V + (c_l z + V).grad V + grad Pi = E(s) R_u(E(s)^T z). So u(x,t) = tau^(c_l-1) V(tau^(-c_l) x, s),
  s = -log tau, tau = T - t, is an Euler solution iff R_u = 0. Period of V in s: 2 pi/|omega|; pi/|omega| under
  the two-fold symmetry.
- [V] J U - (J y.grad) U = - d_phi of the spherical components (at fixed r, theta). This is the rotation
  generator used for the non-axisymmetry diagnostic (section 7.4).

Taylor conditions at the origin [V, d03 for orders 0 and 1 and the symmetry consequences]. With u_0 = U(0), M = DU(0), T_ijk = d_j d_k U_i(0):
  order 0: trace M = 0; (1-c_l) u_0 + M u_0 + omega J u_0 + grad P(0) = 0.
  divergence at order 1 (omitted in v0, astra audit): sum_i T_iik = 0 for k = 1, 2, 3.
  order 1: M + M^2 + omega (J M - M J) + (u_0.grad) DU(0) + Hess P(0) = 0 (matrix with entries
           M_ik + M_ij M_jk + omega(J_ij M_jk - M_ij J_jk) + u0_j T_ijk + d_i d_k P(0)); its antisymmetric part
           is the order-0 vorticity equation.
  order 2: obtained by differentiating R_u twice at 0; numerics must evaluate R_u, D R_u, D^2 R_u at y = 0
           exactly in the regular basis (section 7.6), not by omitting r = 0.
Under the two-fold symmetry u_0 = (0, 0, a), grad P(0) = (0, 0, p_3) and M is block diagonal
(M_13 = M_23 = M_31 = M_32 = 0), so Omega(0) is vertical; u_0 = 0 is NOT imposed.

## 2. Symmetries, reductions and what they imply for the search

2.1 [V] Rotations about e_3: U -> R U(R^T y), P -> P(R^T y), R = exp(b J), map solutions to solutions with the same
    (c_l, omega). One real null direction: fixed by the azimuthal phase gauge (section 6).
2.2 [V] Dilation: U_L(y) = L U(y/L), P_L(y) = L^2 P(y/L) gives R_u[U_L](y) = L R_u[U](y/L),
    curl U_L(y) = Omega(y/L), R_Omega[U_L](y) = R_Omega[U](y/L). One real null direction: fixed by the tail gauge.
    Tail: F -> L^(1+alpha) F(theta, chi - (omega/c_l) log L) [H, trivial], so integral |F|^2 dS scales by
    L^(2(1+alpha)) and the pattern rotates.
2.3 [V] Reflection S = diag(1,-1,1): S J S = -J, so U -> S U(S y), P -> P(S y) maps a solution with omega to a
    solution with -omega, and S commutes with exp(pi J). DECISION: search omega > 0 only. Keep at least three
    negative-omega runs as code regression tests (T06).
2.4 [V] Reflection Z = diag(1,1,-1) commutes with J: it maps a solution to a solution with the same omega. It is NOT
    imposed (the prompt forbids reflection symmetry across z = 0). Correction v1 (astra audit): a candidate and its
    Z-image can be gauge-equivalent through an axial rotation without being Z-symmetric. Report the gauge-orbit
    distance d_Z = min_b ||Z U(Z .) - R_b U(R_b^T .)||_* / ||U||_* over rotations R_b = exp(bJ) (norm of 7.10;
    the F-gauge already fixes the dilation). Candidate and Z-image are distinct members iff d_Z is not ~ 0.
2.5 Two-fold equivariance exp(pi J) is imposed initially: only even azimuthal wavenumbers m in the spherical
    components of U and in the scalar potentials (m = 0 included). Odd m are admitted later (section 11).
2.6 Axisymmetric reduction [V for the algebra; the theorem is CITED, NOT verified input]: if U is axisymmetric then
    J U - (J y.grad)U = 0 and omega drops out of R_u, so U solves the non-rotating profile equation. A companion
    report (Theorem L2 of the earlier non-rotating study) states that every C^2 solution of the non-rotating
    equation with U = o(|y|) uniformly is constant, for 0 < c_l < 1/2; its own text calls its proof informal, the
    prompt (section on literature) forbids treating such a claim as verified input, and the independent audit
    (astra) classifies it as "unclear" because no complete proof was supplied to it. The lead checked only its
    Bernoulli step (grad Be = -[(1-2c_l)I + Omega x](c_l y + U) at omega = 0, consistent with section 1), not its
    limit-set and null-graph steps. Therefore NO result, label or search decision of this campaign depends on L2.
    Non-axisymmetry is required by the prompt anyway (7.4, section 8); the L2 statement is only a reason to expect
    axisymmetric drift to be a failure mode. Approximate states whose non-axisymmetric content decreases under
    refinement are flagged (7.4); this is a warning, not a limit statement: without compactness and uniform bounds
    such a sequence may also escape, become singular or keep a residual (verifier audit 17:33Z). No general rotating
    obstruction is known (the independent audit found none; see 2.8 for what is proved; label D needs a new
    complete argument). A direct proof of the axisymmetric case that does not use L2 is in 2.8(b).
2.7 Energy argument [H, A]: integrating the energy density identity over B_R,
        (5c_l - 2) integral_{B_R} |U|^2/2 = integral_{dB_R} [ (|U|^2/2 + P)(U.n) + c_l R |U|^2/2 ] dS.
    For c_l > 2/5, if U is in L^2 and the boundary flux tends to zero along a sequence R -> infinity, then U = 0.
    The flux condition holds automatically for a smooth bounded U in L^2 with the full-space pressure (verifier
    audit 17:33Z, checked by lead): U in L^2 and L^infinity gives U_i U_j in L^2, so P = R_i R_j(U_i U_j) is in L^2
    (Riesz transforms), hence g(R) = integral_{S_R}(|U|^2 + |U|^3 + |U||P|) dS is integrable in R and
    liminf R g(R) = 0, which kills both boundary terms along one sequence. Also -Delta P = tr((DU)^2) holds for ANY
    pressure of an exact profile, because div of the linear terms vanishes (div(JU) = div((J y.grad)U) = tr(J DU)),
    so the pressure of an exact decaying profile differs from the Riesz pressure by a constant. So every nonzero decaying profile in the target
    range has infinite energy; the natural tail r^(-alpha) F with alpha < 3/2 does, with
        integral_{B_R} |U|^2 dy = (c_l/(5c_l-2)) R^((5c_l-2)/c_l) integral_{S^2}|F|^2 dS + o(R^((5c_l-2)/c_l)).
    The coefficient is consistent with the flux side (c_l/2) R^(3-2alpha) integral |F|^2 [H].

2.8 Rigorous partial results (v1.1; source astra obstruction1, reviewed line by line by the lead, identities
    re-derived symbolically in d06 (16/16 exact checks PASS). v1.2: (a), (b), (c) CONFIRMED by the independent
    route with standalone proofs (its SPEC_AUDIT_v1_1.md, 18:18Z), status [V, I], with the qualifications written
    into (a) and (d); (e) is new, status [H, A]). k = 1-2c_l, ell = (Jy).U, V = c_l y + U.
    (a) Decay dichotomy. If 2/5 < c_l < 1/2, U in C^2, div U = 0, P the full-space pressure and
        |U| <= C(1+r)^(-alpha) uniformly, then E(R) = integral_{B_R}|U|^2 = L R^(3-2alpha) + O(R^(2-3alpha)) with
        L >= 0, and L = 0 iff U = 0. Hence a profile with U = o(r^(-alpha)) uniformly is zero (no assumption on
        DU or a pointwise pressure bound). Proof: the exact ball ODE of 7.8, an annulus estimate
        integral_{R<r<2R}(|U|^3 + |PU|) <= C R^(3-3alpha) (Riesz transforms on L^2 for the middle part, kernel
        bounds for the inner and outer parts) and monotonicity of E. Consequence: in this decay class no nonzero
        profile decays faster than the natural rate. Qualification (independent audit): L > 0 is a normalized
        energy limit, not convergence to an angular profile; the pointwise tail F, and with it the F-gauge of
        section 6, belongs to the separately assumed tail class of section 3. The dichotomy concerns exact
        profiles only; it says nothing about optimizer sequences (no compactness), so a numerical tail collapse
        is not evidence that the limit is zero.
    (b) Axisymmetric sublinear profiles are constant, directly (independent of L2), for 0 < c_l < 1/2 and any
        omega: W ell = -k ell - d_phi P, so with axisymmetric P, ell grows like e^(k t) along bounded backward
        orbits and vanishes; with no swirl, W(Omega_phi/rho) = -(1+c_l) Omega_phi/rho forces Omega = 0; a
        sublinear harmonic U is constant. This replaces the citation in 2.6 once confirmed.
    (c) Dynamics of W (U = o(r)): backward orbits are trapped; the alpha-limit set of a vortical point meets
        {lambda_max(sym DU) >= 1}; a singleton backward limit p of a vortical orbit has max Re sigma(DW(p)) >=
        1 + c_l; a periodic orbit carrying vorticity has Floquet multipliers 1, e^((1+c_l)T), e^((2c_l-1)T)
        (saddle), and a periodic alpha-limit set of any vortical point is a hyperbolic saddle cycle.
    (d) Bernoulli with rotation: W H_0 = -k|V|^2 - omega d_phi P, H_0 = Be + omega ell; the pressure torque has
        no sign. Exact NON-decaying potential flows U = grad Phi (any harmonic polynomial Phi) include a periodic
        backward attractor on which Be is not monotone, and an equilibrium with lambda_max(S) >= 1 and no stable
        direction. So H_0 + a ell (any constant a) is not a Lyapunov function for all smooth rotating profiles,
        and no universal strict identity with exceptional set {W = 0} or {V = 0} holds. This does not exclude
        other Bernoulli-type functions, in particular under decay (independent audit). The non-rotating proof
        route fails as it stands; the examples say nothing about the decaying search class.
    (e) Backward stretching (v1.2, lead, derivations/d07_backward_stretching.md; CONFIRMED by the verifier's
        v1.2 audit 18:36Z, the measure statement under the stated countability hypothesis). On the open invariant
        set G = {W x Omega != 0}, which is dense in {Omega != 0} (if W x Omega = 0 on an open set, the Bernoulli
        form gives curl(c_l y + U) = Omega = 0 there), D Phi_{-t} grows at least like e^((1-2c_l) t) transversally
        to span(W, Omega): Hadamard's inequality with det D Phi_{-t} = e^(-3c_l t), D Phi_{-t} W = W(Phi_{-t}) bounded
        and D Phi_{-t} Omega = e^(-(1+c_l) t) Omega(Phi_{-t}). Consequences: no point of G has a backward source,
        attracting cycle or normally attracting torus as alpha-limit set; if W has countably many equilibria and
        periodic orbits, the vortical points whose alpha-limit set is one of them form a Lebesgue-null set (each
        lies on a center-unstable manifold of dimension <= 2, by the spectral facts of (c)). Hence a nonzero
        profile needs non-elementary backward W-dynamics (chaotic, heteroclinic or degenerate families) on a
        positive-measure part of the vortical set. A necessary condition, not an obstruction.
        (v1.4) Strengthenings from the astra stretch1 audit, lead-reviewed in derivations/d11_stretch1_review.md
        (algebra d11_stretch_checks.py 6/6 PASS) [CONFIRMED by the independent route 18:58Z (SPEC_AUDIT_v1_4) for the
        full measure of G, the countability removal for convergence to an equilibrium (no claim when the
        alpha-limit is a continuum), the null union of hyperbolic periodic alpha-limits, the ergodic spectrum and
        mean strain one when W, Omega != 0 a.e. (equilibrium measures excluded) and the liminf bound; the signed
        form was H until it was lead-checked as algebra 2026-10-24T20:37Z and CONFIRMED by the independent route
        20:38Z: for every smooth U, P, L_W beta + k beta = R_u^flat + d(W.R_u)/k with beta = U^flat + dB/k,
        B = U.W - |U|^2/2 + P, so on a profile beta = (W x Omega)^flat/k and the signed form is the pullback
        identity, derivations/d15_alphalim_review.md (b)]: curl(W x Omega) = (1-2c_l) Omega, so
        G has full measure in the vortical set; signed form (W x Omega)(Phi_{-t} p).D Phi_{-t}(p) e =
        e^((1-2c_l)t)(W x Omega)(p).e, valid for every p (d07's constant needs p in the trapping ball); the
        countability hypothesis is not needed (countable cover by local center-stable neighborhoods), so for almost
        every vortical point the alpha-limit set is neither a single equilibrium nor a single periodic orbit; every
        ergodic invariant measure with W, Omega != 0 a.e. has backward Lyapunov spectrum {-(1+c_l), 0, 1-2c_l} and
        integral Omega.S Omega/|Omega|^2 dmu = 1; along every vortical backward orbit the time average of
        Omega.S Omega/|Omega|^2 has liminf >= 1. The non-rotating remark of d07 is withdrawn.
    (f) Dilation-invariant nontriviality facts used as guards (v1.2): DU, lambda_max(S), the stretching ratio
        Sigma_Z and the energy ratio Sigma_E of 7.8 are invariant under the dilation of 2.2, while they scale like
        the amplitude for a weak field. Every nonzero exact profile has sup lambda_max(S) >= 1 (from (c) and from
        the vorticity maximum identity, N2 of 7.5) and Sigma_Z = Sigma_E = 1. No gauge choice can remove a weak
        (small-DU) state; only the residual, these exact identities, or constraints derived from them can.
    (g) Kelvin, vortex lines and invariant measures (v1.3) [local identities V, d10; derivations/
        d10_kelvin_invariant_measures.md; CONFIRMED by the independent route 18:58Z for the Kelvin and flux laws,
        periodic circulation, surface tangency, vortex-segment contraction and the four measure identities; the
        strong-stable-foliation wording and the cohomology of A remain H]. For an exact profile: the circulation of U around a closed curve
        transported by W, and the vorticity flux through a transported surface, scale like e^(-(1-2c_l)s); hence the
        circulation of U around every periodic W-orbit is zero, Omega is tangent to every compact invariant surface,
        and the circulation vanishes on every cycle of an invariant torus. Vortex lines are strong-stable leaves of
        the backward flow (exact contraction e^(-(1+c_l)t) in vortex time), so alpha-limit sets are constant along
        vortex lines (verifier qualification 18:58Z: proved is the contraction of finite vortex segments, hence
        equal alpha-limits along a segment; identifying vortex lines with the whole strong-stable foliation needs a
        hyperbolic splitting). The forward non-escaping set A is compact, invariant, null, contains every alpha-limit set and
        has trivial Cech cohomology. For every W-invariant probability measure mu: integral (c_l|y|^2 + y.U) dmu = 0,
        integral U.W dmu = 0, integral |c_l y + U|^2 dmu = omega integral ell dmu, integral ((1-2c_l) ell + d_phi P)
        dmu = 0. No function H_0 + a ell + b|y|^2/2 is a Lyapunov function when omega != 0. Necessary conditions and
        diagnostics, not an obstruction.
    (h) Parameter count (v1.3; astra paramcount1, checked by the lead in derivations/d09_paramcount_checks.py,
        11/11 PASS, and by hand). W has a zero in every exact profile (degree 1 on a large sphere; CONFIRMED by
        the independent route 18:52Z together with the eigenvalue condition, for U = o(|y|)); at a zero
        carrying vorticity DW has the eigenvalue 1+c_l along Omega and the other pair sums to 2c_l - 1 (never a
        source). Local transport germs at a prescribed saddle can be infinite dimensional (explicit flat example),
        and the critical-rate exterior operator is not Fredholm in ordinary weighted spaces; no statement on the
        dimension of the solution set in (c_l, omega) is available (open set, curve, isolated points and
        fixed-parameter families all remain possible).
    (i) Outgoing conditions (v1.6; (a)-(d) independently confirmed 2026-10-24T19:22Z; derivations/d13_civ_transfer.md, d13_civ_checks.py all True; source
        Constantin-Ignatova-Vicol arXiv:2602.17570, non-rotating). W.y = (c_l y + U).y and sym DW = c_l I + S.
        (a) A vortical zero of W is not locally outgoing for c_l < 1/2 + c* (lambda_max(c_l I + S) >= 1 + c_l there).
        (b) For decaying U, global outgoing W.y >= c*|y|^2 (c* > 0) forces U = 0 for c_l < 1/2, any omega. (c) Under local outgoing
        at finitely many zeros, vortical alpha-limits are zero-free compact invariant sets; excluded for omega = 0
        by the Bernoulli function, OPEN for omega != 0. (d) CIV Thm 3.4 holds verbatim:
        Gamma_p := C_p ||grad Omega||_inf^(3/(p+3)) ||Omega||_p^(p/(p+3)) >= 1, p > max(3c_l, 1), C_2 = 2(162/pi)^(1/5)
        = 4.40051, dilation invariant. Attribution: 2.8(c) axisymmetric triviality is CIV Thm 4.5 / Remark 4.6 (K U = 0 for
        axisymmetric U), the 2.1 critical-point identity at the maximum is CIV Prop 3.3, 2.8(g) Kelvin for omega = 0
        is CIV (3.24)-(3.28).
    (j) Zero-free invariant sets (v1.8 [A], CONFIRMED by the independent route 2026-10-24T20:38Z with the
        qualifications of FINAL_REPORT_AUDIT; derivations/d15_alphalim_review.md, d15_alphalim_checks.py; formulation
        7.13). With D = y.U + |y|^2/2 and B = U.W - |U|^2/2 + P: W.grad D = |V|^2 + c_l(1-c_l)|y|^2 - y.grad P, so a
        compact zero-free invariant set meets {y.grad P >= c_l(1-c_l)|y|^2}; grad B = W x Omega - kU and
        beta = (W x Omega)/k obeys L_W beta = -k beta; under local outgoing at finitely many zeros W has exactly one
        zero; on invariant measures E + Q = omega^2 I (Q = <|W|^2>); for the natural tail
        integral f(B) U.Omega dy = 0 for every continuous f; on vortical ergodic measures with W != 0 a.e. (spectrum
        as in 2.8(e)) the entropy is at most k (Ruelle's inequality).
    No obstruction for the search class follows: the rotating problem remains open (no label-D argument).

## 3. Far field (primary search class; a search assumption, not a theorem)

3.1 Leading tail. U_0 = r^(-alpha) F(theta, chi), Omega_0 = r^(-1/c_l) H(theta, chi). [V, d02]
    The linear operator L U := (1-c_l)U + c_l (y.grad)U + omega [J U - (J y.grad)U] acts on twisted homogeneous
    fields r^(-k) G(theta, chi) (spherical components) as multiplication by c_l (alpha - k). In particular
    L[r^(-alpha)F] = 0 for every F and L[r^(-(2alpha+1)) G] = -r^(-(2alpha+1)) G. [V, d02]
3.2 Leading divergence constraint [V, d02]:
        (2-alpha) F_r + (omega/c_l) d_chi F_r + (1/sin th) d_th(sin th F_th) + (1/sin th) d_chi F_ph = 0.
    General solution [V for the representation formulas, d02]: with smooth scalars sigma, tau on S^2 (functions of
    (theta, chi)), B = (2-alpha) sigma + (omega/c_l) d_chi sigma,
        F_r = -Delta_S2 sigma,  F_th = d_th B + d_chi tau / sin th,  F_ph = d_chi B / sin th - d_th tau.
    These are exactly the leading tails of curl(T y) + curl curl(S y) with T = r^(-alpha) tau(theta, chi) and
    S = r^(1-alpha) sigma(theta, chi). Completeness: mode by mode, the l >= 1 parts of F_r and of the tangential
    Helmholtz decomposition determine sigma, tau uniquely; the l = 0 constraint forces the mean of F_r to vanish.
    So F carries two free scalar functions on S^2 (l >= 1). F must be a smooth vector field on S^2; parametrizing it
    by smooth sigma, tau (spherical harmonics in (theta, chi)) guarantees that.
3.3 Leading vorticity [V, d02]: H_r = [d_th(sin th F_ph) - d_chi F_th]/sin th,
    H_th = d_chi F_r/sin th - [(1-alpha) F_ph + (omega/c_l) d_chi F_ph],
    H_ph = (1-alpha) F_th + (omega/c_l) d_chi F_th - d_th F_r. Record zeros and min |H| of every candidate; do not
    impose H != 0.
3.4 First nonlinear correction [V, d02]: the prompt's formulas for N, Q, G are correct as written:
    (U_0.grad)U_0 = r^(-(2alpha+1)) N; -Delta(r^(-2alpha) Q) = div(r^(-(2alpha+1)) N) is exactly the prompt's Q
    equation; G = N + ((-2alpha + (omega/c_l) d_chi)Q, d_th Q, d_chi Q/sin th); div(r^(-(2alpha+1)) G) = 0 is
    equivalent to the Q equation; L U_1 + (U_0.grad)U_0 + grad(r^(-2alpha) Q) = 0 holds identically.
    The Q equation's source equals r^(2alpha+2) tr((DU_0)^2) because div U_0 = 0.
    Pressure eigenvalues on Y_l^m(theta) e^{i m chi} [V, d02]: (-2alpha + i m omega/c_l)(1 - 2alpha + i m omega/c_l)
    - l(l+1). Nonzero in 1 < alpha < 3/2: for m != 0 the imaginary part is (m omega/c_l)(1-4alpha) != 0; for m = 0
    zero would need 2alpha = l+1, impossible strictly inside. Near-singular modes: (l,m) = (1,0) as c_l -> 1/2 and
    (2,0) as c_l -> 2/5. Numerics must print the smallest |eigenvalue| used at each (c_l, omega).
3.5 Structure of the full expansion [H; audited (astra specaudit1, corrections applied in v1, each checked by the
    lead); resonance arithmetic V, d03; mixed example reproduced, derivations/astra_repro/mixed_resonance.log].
    Notation in the true (untwisted) azimuth: a term r^(-k+i nu) Y_l^m(theta, phi); a twisted term r^(-k) e^{i m chi}
    has nu = m omega/c_l. Velocity decay rates k (real parts):
      alpha                       leading tail F: FREE formal data (2 functions on S^2), fixed only by inner-outer
                                  matching;
      2alpha + 1 = alpha + 1/c_l  G[F]: determined by F;
      n/c_l - 1, n >= 2           pure-tail products of n tail factors: determined by F;
      l + 2, l >= 2 (first: 4)    velocity -grad p_l / ((1 - c_l(l+3)) - i m omega) of the harmonic pressure
                                  multipole p_l = C_lm r^(-(l+1)) Y_l^m(theta, phi) (untwisted); C_lm are GLOBAL
                                  (finite-part moments of the full-space source); the real part of the denominator
                                  is below -1 for l >= 2;
      mixed                       n >= 1 tail factors and multipoles of degrees l_1..l_d: velocity rate
                                  n/c_l + sum_j (l_j+3) - 1, pressure rate p = n/c_l + sum_j (l_j+3) - 2; their
                                  coefficients are computable from F AND the previously determined multipoles, not
                                  from F alone.
    This classification is formal: the existence of a complete expansion with a controlled remainder is NOT
    established by a differentiable leading tail [C].
    Pressure: r^(-2alpha) Q (determined by F), r^(-(l+1)) multipoles l >= 2 (global), then products.
    Vanishing moments: the l = 0 and l = 1 source moments vanish under the differentiated decay assumption (the
    source is a double divergence d_i d_j(U_i U_j); the boundary terms are O(R^(1-2alpha)), O(R^(2-2alpha))), so there
    are no homogeneous r^(-1), r^(-2) pressure terms and no r^(-2), r^(-3) velocity terms from them. This does NOT
    remove the l = 0, 1 components of r^(-2alpha) Q.
    Finite parts. Write the complete asymptotic source f_lm(s) ~ sum a_{p,nu} s^(-p-2+i nu) (pure-tail, mixed and
    oscillatory contributions; v0 notation q = p+2). Nonresonant (l, m):
        C_lm = (1/(2l+1)) lim_{R->inf} [ integral_0^R s^(l+2) f_lm ds
                                         - sum_{Re p <= l+1} a_{p,nu} R^(l+1-p+i nu) / (l+1-p+i nu) ],
    subtracting EVERY non-integrable contribution, including bounded oscillatory ones (Re p = l+1, nu != 0). Not
    every (l, m) has a nonzero leading divergent coefficient. Resonant (l, m), i.e. a term with (p, nu) = (l+1, 0)
    and coefficient a != 0: subtract a log R as well (unit log scale in the F-gauge; log-power sources need
    log-polynomial subtractions). With the particular-pressure convention P_part = (a/(2l+1)) r^(-(l+1)) log r the
    exterior Green integral adds a constant:
        C_lm = FP M_lm/(2l+1) + a/(2l+1)^2,   FP M_lm = lim_R [ integral_0^R s^(l+2) f_lm ds - (other subtractions)
                                                          - a log R ]
    (checked by the lead from the Green formula of 5.2).
    Resonance rule (corrected in v1; v0 required m = 0, which is wrong). A pressure term r^(-p+i nu) Y_l^m is
    resonant (produces r^(-(l+1)) log r) iff nu = 0, p = l+1 and the source projection is nonzero; m is arbitrary.
    The radial frequency counts only the twisted azimuthal indices of the tail factors, while the final m also
    counts the multipole indices, so nu = 0 with m != 0 occurs. Pure-tail (p = n/c_l - 2) and mixed resonances both
    need n/c_l to be an integer; 1/c_l in (2, 5/2) and 2/c_l in (4, 5) never are, so n >= 3 and the resonant
    parameters are exactly c_l = n/K with integers 2n < K < 5n/2 (n = 3: 3/7; n = 4: 4/9; n = 5: 5/11, 5/12;
    n = 6: 6/13; n = 7: 7/15, 7/16, 7/17; n = 8: 8/17, 8/19; ...). Every rational c_l = n/K in lowest terms has
    rate coincidences, entering at order n (pressure rate >= K - 2), and then infinitely many of them; each gives a
    log only if its source projection is nonzero (generic, verified only in the examples below).
    First pure-tail ones: c_l = 3/7, l = 4, p = 5 (velocity r^(-6) log r); c_l = 4/9, l = 6, p = 7.
    First mixed example (astra, exact sympy, reproduced by the lead): c_l = 3/7, omega = 1, poloidal tail
    sigma = P_3(cos th), tau = 0, quadrupole velocity proportional to grad(r^(-3) sin^2 th e^{2 i phi}); three tail
    factors and one quadrupole give a nonzero r^(-12) P_9^2(cos th) e^{2 i phi} source (coefficient
    77883280853706560/25794632597097 - 165879152402176640 i/143712953040969), hence pressure r^(-10) log r and
    velocity r^(-11) log r with m = 2. Rate coincidence alone is not sufficient: products of multipole velocities
    form a harmonic gradient V whose self-interaction is cancelled by the local pressure -|V|^2/2.
    Velocity: the multiplier of the linear operator on r^(-k+i nu) e^{i m phi} fields is
    c_l(alpha-k) + i(c_l nu - m omega), nonzero for k > alpha; velocity resonances occur only at k = alpha.
    Endpoint coincidences: c_l = 1/2 (2alpha = 2, l = 1) and c_l = 2/5 (2alpha = 3, l = 2: the r^(-3) multipole
    meets r^(-2alpha) Q). A rate coincidence gives a log only if the source projection is nonzero (at alpha = 1 the
    leading dipole source cancels by the double-divergence identity).
    Binding practical rule. c_l = 3/7 and 4/9 are not used as fixed search points. On the registered grid
    c_l = 0.41, 0.43, 0.45, 0.47, 0.49 the exact resonances have K = 100, 100, 20, 100, 100 (pressure rate >= 18,
    beyond any tail model), but 0.43 lies within 0.05 in rate of the n = 3 resonance of 3/7 (3/0.43 = 6.977).
    A resonant or near-resonant log term is NOT assumed negligible: if the analytic tail model includes a term
    within 0.05 in rate of a resonance, it uses the resonance-regular form for the pair (q = p+2, l+3)
        a (s^-(q) - s^-(l+3)) / ((l+3) - q)  ->  a s^-(l+3) log s   as q -> l+3,
    so that free-parameter runs can cross a resonance without a pole; every omitted term (resonant or not) is
    bounded from the fitted coefficients by the next-order estimate and shown below the error budget of each
    far-shell diagnostic (7.7, 7.11).
3.6 Seed family [V, d02]: F_r = 0, F_th = 2 eps sin th sin 2chi, F_ph = sin th + 2 eps sin th cos th cos 2chi
    satisfies 3.2 exactly; it is the toroidal tail with tau = cos th - eps sin^2 th cos 2chi, a restriction of a
    polynomial to S^2, so it is smooth at both poles. At eps = 0, H = (2 cos th, (alpha-1) sin th, 0), nowhere zero.
    Use it as ONE seed family; also poloidal, mixed and order-one non-axisymmetric random (sigma, tau).

## 4. Representation requirements (primary route; numerics lane)

4.1 U = curl(T y) + curl curl(S y), with even-m expansions of T and S under the two-fold symmetry; remove the
    l = 0 parts of T and S (null modes). Document normalization of Y_l^m.
4.2 Twist: angular argument phi + psi(r), psi(r) = (omega/(2c_l)) log(1 + r^2/R_0^2), applied to the potentials,
    with actual curls including psi'(r) and psi''(r). R_0 is a basis parameter: vary it (factor 2) in Stage III.
4.3 Origin: radial coefficient functions T_lm(r), S_lm(r) = r^l times smooth functions of r^2 in the core (the
    factor e^{i m psi(r)} is smooth in r^2 and nonvanishing, so this is equivalent to smoothness of T, S).
4.4 Far field: T ~ r^(-alpha) tau, S ~ r^(1-alpha) sigma with the decay powers and spiral factored analytically;
    corrections (rates 2alpha+1, 4, ...) either factored or shown resolved by the E_G test (7.7). Beyond the last
    resolved radius R_far, use an explicit analytic tail model r^(-alpha) F + r^(-(2alpha+1)) G[F] + multipole terms,
    with its truncation error estimated by the next term. No velocity or pressure boundary condition at a finite
    radius.
    Radial channels (required for Stage II and for any Tier R/A claim; recommended from the start). The exact far
    field contains, besides the leading rate alpha, the twisted rates alpha + n(alpha+1) (n = 1: 2alpha+1) and the
    UNTWISTED multipole rates l+2 (complex in the twisted frame), with 2alpha+1 in (3, 4) close to the first
    multipole rate 4. Offsets alpha+1 in (2, 5/2) are not integers and the untwisted terms oscillate like
    exp(-i m (omega/c_l) log r) relative to the twist. A single expansion that is smooth in a compactified variable
    such as x = (s-R_0)/(s+R_0) (integer powers of 1/s times one envelope) therefore cannot represent them: it gives
    an algebraically convergent fit of (1-x)^(alpha+1) and an O(1) relative error in the correction for
    r >> N^2 R_0, which shows up as rho_nl = O(1) in the far shells and as E_G = O(1). Minimum remedy, per (l, m):
      T_lm = r^l [ s^-(alpha+l) A_lm(x) + s^-(2alpha+1+l) B_lm(x) ] e^{i m psi},
      S_lm = r^l [ s^-(alpha+l-1) C_lm(x) + s^-(2alpha+l) D_lm(x) ] e^{i m psi}
             + r^l s^-(2l+1) E_lm(x) (untwisted: no e^{i m psi}; harmonic r^-(l+1) Y_l^m at infinity, l >= 2),
    with A..E smooth (Chebyshev) in x; B, D, E may have few modes. curl curl(r^-(l+1) Y_l^m y) =
    -l grad(r^-(l+1) Y_l^m), so the E channel carries the pressure-multipole velocity. The channels are
    asymptotically independent but nearly redundant in the core: report the conditioning and use damping or a
    far-field-supported form (e.g. multiply B, D, E by (r^2/(r^2+R_1^2))^k) if needed. Any equivalent scheme is
    acceptable if documented and if E_F and E_G of 7.7 converge at the predicted rates.
    Rate bookkeeping (v1.1, from the independent lane's first_tail_constraint, checked by the lead). The exact
    formal velocity rates are n(alpha+1) - 1 + sum_{j=1..d}(l_j + 3) (n tail factors, d multipoles l_j >= 2,
    n + d >= 1): alpha, 2alpha+1, l+2, 3alpha+2, ... Any regularized envelope (s = sqrt(r^2+R_0^2)), compactified
    variable x or regularized twist psi(r) also generates rates alpha + j, 2alpha+1+j (j = 1, 2, ...). On a
    twisted term of rate k the linear operator acts by c_l(alpha - k) != 0, and in 2/5 < c_l < 1/2 the rates
    alpha+1, alpha+2, alpha+3, 2alpha+2 are not in the exact set, so the angular velocity coefficient of each such
    term must vanish in an exact profile. Either impose this as a linear constraint on the coefficients (the
    independent lane does so for alpha+2) or report the far-field size of these coefficients relative to F; an
    uncancelled alpha+j term gives far-shell rho_nl growing like r^(alpha+1-j) (j = 1, 2).
    Angular closure (v1.8 addition 2026-10-24T21:03Z, derivations/d18_nonlinear_tail_review.md; no threshold). The
    angular span of the rate 2alpha+1 channels must contain G[F] for every F in the leading span. By the degree
    count: a correction potential of degree 2d+2 for a leading potential of degree d; for T/S scalars with
    leading l <= L and even m <= M_max, B up to l = 2L+3, D up to l = 2L+2, and even m up to 2 M_max. Otherwise
    E_G (7.7) does not decay and far-checkpoint rho_nl has a positive limit. Report dist(G[F], carried span) /
    ||G[F]|| with every exported state that has rate 2alpha+1 channels.
4.5 If c_l or omega is optimized, the derivatives of alpha, the twist, the factored envelopes, the tail model and
    the pressure reconstruction with respect to them must be included (no frozen Jacobian blocks).

## 5. Pressure (both lanes)

5.1 P is the full-space decaying solution of -Delta P = tr((DU)^2) (= d_i d_j (U_i U_j)), P -> 0 at infinity; no
    harmonic pressure is added or fitted; no condition at a finite radius.
5.2 Green formula (orthonormal Y_l^m, f_lm = integral f conj(Y_l^m) dS) [V, d03: manufactured twisted sources, l = 0..4,
    rel. error < 1e-30 with the closed-form exterior series]:
        P_lm(r) = (1/(2l+1)) [ r^(-l-1) integral_0^r s^(l+2) f_lm(s) ds + r^l integral_r^inf s^(1-l) f_lm(s) ds ].
    The exterior integrals beyond R_far use the analytic tail model term by term: for a source term
    a s^(-p-2+i nu), integral_R^inf s^(1-l) a s^(-p-2+i nu) ds = a R^(-l-p+i nu)/(l+p-i nu) (Re(l+p) > 0) [astra,
    checked by the lead]; the leading local term has p = 2alpha, nu = m omega/c_l (twisted index m), and mixed terms
    use their own (p, nu) (3.5); report the size of the exterior contribution and of its truncation error per (l, m).
5.3 Note the source spherical-harmonic coefficients must be taken in the true azimuth phi (pressure multipoles are
    untwisted harmonics); f_lm(s) then oscillates like s^(i m omega/c_l): radial quadrature must resolve this
    (logarithmic radial variable recommended).
5.4 Cross-check selected values with an independent method (direct free-space kernel, or the verifier's
    ray-integral formula grad P(x) = (1/4pi) integral_S2 n integral_0^inf f(x + rho n) d rho dS).

## 6. Gauges (exactly one dilation gauge, one phase gauge, the pressure constant)

6.1 Dilation: integral_{S^2} |F|^2 dS = 1 (primary). Alternative allowed for the optimizer: a core-scale gauge
    with integral |F|^2 free, provided (i) integral |F|^2 is monitored and bounded away from zero (a vanishing F
    leaves the primary class) and (ii) every reported number is converted to the F-gauge. Never both at once.
    No vorticity, DU(0) or core-radius normalization in addition.
6.2 Phase: fix the argument of one nonzero m != 0 coefficient (pivot (l*, m*)), e.g. of tau or sigma at the outer
    boundary; switch pivot (logged) when its modulus falls below 1e-3 of the largest m != 0 coefficient; or handle
    the rotation null direction by a minimum-norm Gauss-Newton step and report alignment afterwards.
    (v1.23, 2026-10-25T08:14:16Z) Implementation clarification: a chart Im(pivot) = 0 fixes the argument only up to pi. After
    every accepted step check Re(pivot); if it is negative, apply the logged discrete rotation C(pi/m*) (the
    coefficient map a -> a e^(i pi m/m*) on every (l, m) column, never the global sign change c -> -c), or record
    the argument and rotate at commit and export. The endpoint switch rule above cannot detect a crossing of the
    vanishing-pivot set between two non-small endpoints (derivations/d75_review_gauge_frame.md).
6.3 Pressure: P -> 0 at infinity (5.1). Nothing else.

## 7. Diagnostics (definitions used for ranking and acceptance)

7.1 Domain decomposition in the F-gauge. Core radius r_core := argmax_r of r^3 <|Omega|^2>_{S_r} (sphere mean).
    Shells: dyadic [2^j, 2^(j+1)) covering at least [r_core 2^-5, r_core 2^12], plus the core ball r < r_core 2^-5,
    the origin neighborhood r < r_core 2^-8 together with the point y = 0, axis sets {sin th < 0.05} inside every
    shell, and far checkpoints thin shells [R, 1.1R] at R = r_core 2^14, 2^16, 2^20 (via the representation or the
    tail model). Each shell RMS is taken w.r.t. normalized volume measure inside the shell; shells are combined by
    max and by equal-weight RMS (never by total volume or point count).
7.2 Momentum terms (5-term frame-invariant split, PRIMARY): T1 = (1-c_l)U, T2 = c_l (y.grad)U,
    T3 = omega [J U - (J y.grad)U], T4 = (U.grad)U, T5 = grad P. R_u = T1+...+T5. Also report the 6-term split
    (omega J U and -omega (J y.grad)U separately, as in the verifier's registration). Since
    RMS(a) + RMS(b) >= RMS(a+b), the 5-term denominator never exceeds the 6-term one, so the 5-term ratio is the
    larger (stricter) one and is used for acceptance.
      rho_u(k)   = RMS_k(R_u) / sum_i RMS_k(T_i),
      rho_nl(k)  = RMS_k(R_u) / (RMS_k(T4) + RMS_k(T5))      (nonlinear balance; essential in the far field,
                   where T1+T2+T3 cancel identically on the leading tail),
      pi_u(k)    = max_{x in shell k} |R_u(x)| / sum_i RMS_k(T_i),
      peak(k)    = pi_u(k)/rho_u(k) (concentration factor; flag if > 30).
    Vorticity: terms Omega, c_l (y.grad)Omega, omega [J Omega - (J y.grad)Omega], (U.grad)Omega, -(Omega.grad)U;
      rho_Om(k), rho_Om_nl(k) analogously.
    Poisson: rho_P(k) = RMS_k(R_P)/(RMS_k(Delta P) + RMS_k(tr (DU)^2)). Divergence: rho_div(k) = RMS_k(div U)/RMS_k(|DU|).
    Flag a shell whose term sum is below 1e-14 times the largest shell term sum (v0: 1e-14 absolute, which is not
    dilation invariant) or more than 1e3 below both neighbours; flagged shells are reported, never counted as
    successes.
    Absolute fixed-gauge values reported per shell: RMS_k(R_u), r_k^alpha RMS_k(R_u), r_k^(2alpha+1) RMS_k(R_u),
    r_k^(1/c_l) RMS_k(R_Omega).
    Added in v1 (astra audit: relative ratios can be made small by inflated denominators, e.g. large m omega in T3
    or large mutually balancing T4, T5). With r_k the geometric midpoint of shell k, in the F-gauge:
      pi_nl(k)  = max_{x in shell k} |R_u(x)| / (RMS_k(T4) + RMS_k(T5)),
      A_u       = max_k (1+r_k)^(2alpha+1) RMS_k(R_u) / Lambda_u,  Lambda_u = max_k (1+r_k)^(2alpha+1) RMS_k(U)^2 / r_k,
      A_Om      = max_k (1+r_k)^(2alpha+2) RMS_k(R_Omega) / Lambda_Om, Lambda_Om = max_k (1+r_k)^(2alpha+2) RMS_k(U)^2 / r_k^2.
    The reference scales Lambda use |U|^2/r, the size of the nonlinear terms of a smooth field, which high-m or
    high-radial-frequency content cannot inflate (it inflates DU, not U). On the leading tail both weighted
    quantities are O(integral |F|^2) = O(1).
    Float64 cancellation (astra audit, checked by the lead). In far shells T1+T2+T3 cancel to the nonlinear scale,
    so direct summation amplifies roundoff by about eps_mach r^(alpha+1) relative to that scale (2e-4 to 0.25 at
    r = 2^20 with unit core scale). Therefore: evaluate the leading cancellation algebraically (apply the linear
    operator to U - r^(-alpha)F, or to the represented corrections, using L[r^(-alpha)F] = 0 exactly), and repeat
    the far checkpoints (r >= 2^14 r_core) at extended precision (float128 or mpmath, >= 256 points per checkpoint);
    the float64 and extended values of rho_nl, pi_nl must agree within 10% or the extended value is used.
    Added in v1.14 (2026-10-24T23:19:15Z; reported only, no threshold; derivations/d29). Self-similar balance ratios, the
    core counterpart of rho_nl (in a near-steady core T4 and T5 are large and cancel, so rho_u is small whatever T1 to T3
    do):
      rho_lin(k) = RMS_k(R_u) / (RMS_k T1 + RMS_k T2 + RMS_k T3),   rho_sp(k) = max(rho_lin(k), rho_nl(k)),
      and the same for the vorticity equation (rho_Om_lin, linear group Omega, c_l (y.grad)Omega,
      omega [J Omega - (J y.grad)Omega]). Report also RMS_k(L) and RMS_k(N), L = T1+T2+T3, N = T4+T5 (by the triangle
      inequality rho_lin(k) <= RMS_k(R_u)/RMS_k(L)). Report rho_sp^max over all shells and over shells inside |y| < 1, for
      every ranked state. A tier requirement on rho_sp awaits the astra audit steadycore1.
    Added in v1.15 (2026-10-24T23:31:23Z; astra steadycore1, lead-checked; derivations/d30). The rho_sp requirement is now in section 8.
    Report also, per shell, the Gram data of L and N: a = RMS_k(L), b = RMS_k(N), gamma = <L, N>_k / (a b), with the
    exact check RMS_k(R_u)^2 = a^2 + b^2 + 2 a b gamma, and b / (RMS_k T4 + RMS_k T5). A resolved balance has b/a near 1
    and gamma near -1; a near-steady core missing its self-similar part has b/a << 1. Report the single-term ratios
    ||R_u|| / ||(1 - c_l) U|| over |y| < 1 and ||R_Omega||_2 / ||Omega||_2 (all resolved shells, with the exterior of
    7.8 when available). None of these is divided by the nonlinear pair, so inflating a cancelling pair cannot lower
    them. Denominator flags for rho_sp: with A_k = sum of RMS_k T1..T3 and B_k = RMS_k T4 + RMS_k T5, put
    A~_k = (1 + r_k)^alpha A_k and B~_k = (1 + r_k)^(2 alpha + 1) B_k (r_k the shell's geometric mean radius; the tail
    gauge has ||F|| = 1; for the origin ball [0, r_max), r_k = 0, v1.16).
    A shell is flagged if either rescaled group is below 1e-14 times its largest value over
    shells, or below 1e-3 times both neighbours. A flagged shell is unresolved, not a pass; no epsilon is added to a
    denominator. The evaluation error of R_u on a shell must be at most 0.1 tau min(A_k, B_k), tau the tier threshold.
7.3 Global numbers: rho_u^max = max_k rho_u(k) (likewise rho_nl^max, pi_u^max, rho_Om^max, rho_P^max, rho_div^max)
    and the equal-weight shell RMS rho_u^bal. Ranking key: holdout rho_u^max, then rho_nl^max, then refinement trend.
    A training loss is never a ranking key.
7.3a Half-offset shell family (v1.11, 2026-10-24T22:40Z; an addition that only tightens). Every shell quantity is also evaluated
    on the half-offset dyadic shells [2^(j+1/2), 2^(j+3/2)), with the measures of 7.1. The largest single-sphere
    rho_u on the exchange grid of section 10 is reported as well.
    (i) A claim that one state has the lower rho_u^max (or rho_nl^max) requires it on both shell families; otherwise
        the two states are reported as not ordered. The ranking key of 7.3 is unchanged and is applied per family.
    (ii) Every threshold of section 8 must hold on both families. This adds a requirement and relaxes none.
    Reason: the primary d6t_L6 state is lower than the independent D6 state on the standard family (grid values
    0.0597 vs 0.0747) but equal on the half-offset family (0.0766 vs 0.0769). Its residual peak sits on the shell
    edge r = 1/4, and its largest single sphere is 0.103 vs 0.0857 (derivations/d26_shell_offset.log).
7.3b Ordering under the single-term and absolute diagnostics (v1.20, 2026-10-25T01:44:56Z; tightens the ordering, changes no
    acceptance threshold). State X is ranked ahead of state Y only if (i) X has the lower holdout rho_u^max on both
    shell families (7.3a (i)), and (ii) X's sigma_u^max (section 8, v1.19 (a)), sigma_Om (v1.19 (b), same radius and
    quadrature for both states) and a_max (fixed velocity-tail gauge, 7.2 and v1.17) each exceed Y's by at most 10 per
    cent. Otherwise X and Y are reported as not ordered, and both stay on the shortlist when either would. Within
    ordered pairs the 7.3 key applies. A quantity missing for either state makes the pair not ordered.
    Reason: rho_u^max can be lowered by denominator growth without approach to a profile (d39, FINAL_REPORT section 2
    item 20); the single-term ratios and the fixed-gauge absolute residual resist the known continuum escapes. Chronology:
    registered after the verifier's Gauss-Newton continuation of the independent D6 state was read, which lowered
    rho_u^max on both families (0.0581 -> 0.0574, 0.0609 -> 0.0541) while raising sigma_u^max (2.52 -> 3.13 standard,
    2.39 -> 2.60 offset), sigma_Om (2.04 -> 2.46, finite ball R = 1024) and a_max (4.40 -> 5.14, 3.97 -> 5.22); under
    7.3b these two states are not ordered. No state is near any acceptance tier.
7.4 Non-axisymmetric content: N_k = RMS_k(d_phi U_sph)/RMS_k(U) = RMS_k(T3)/(|omega| RMS_k(U)) per shell;
    core value N_core = max over shells with r <= r_tail; tail value N_F = ||d_chi F||/||F|| (L2 on S^2);
    also the m != 0 energy fraction per shell e_k = RMS_k(U - <U>_phi)^2 / RMS_k(U)^2 (<.>_phi: azimuthal mean of
    the spherical components), its core value e_core = max over shells with r <= r_tail, and e_F = ||F - <F>_chi||^2
    /||F||^2. N_k is derivative weighted and can be inflated by high m; e_k cannot (astra audit), so both are used.
    Warning if N_core < 1e-2, N_F < 1e-2, e_core < 1e-4 or e_F < 1e-4; "collapsing" if any of them decreases by more
    than 2x per refinement level.
7.5 Nontriviality and anti-artifact guards (all reported for every shortlisted state):
    N1 F-gauge holds to 1e-8. N2 max|Omega| and its location; at that point Omega.S Omega/|Omega|^2 (exact value 1)
    and lambda_max(S) (exact >= 1); (v1.3) the same ratio at the three largest further local maxima of |Omega|
    found by local maximization (exact value 1 at each). N3 = 7.4. N4 core location r_core, width (radii containing 10% and 90% of
    the enstrophy per log radius), amplitude max|U|, max|DU|, max|D^2 U|; r_core at least 4 octaves inside the
    sampled range. N5 tail onset r_tail := min radius beyond which E_F(r) <= 0.1 at all sampled radii; flag if
    r_tail/r_core > 2^8 or growing by > 2x per refinement level. N6 spectral decay: fraction of energy in the top 20%
    of angular degrees and of radial modes per element.
7.6 Origin Taylor audit: tau_j = |D^j R_u(0)| / max(sum_i |D^j T_i(0)|, 1e-3 S_j), j = 0, 1, 2 (Frobenius norms),
    evaluated exactly at y = 0 in the regular basis (AD or exact formulas). The floor S_j = U_c r_core^(-j)
    (1 + U_c/r_core), U_c = max|U|, is the natural size of the j-th derivative of the momentum terms; it removes the
    0/0 case (e.g. u_0 = 0 makes every order-0 term vanish) by turning tau_j into an absolute test (v1). Report both
    the raw ratio and the floored one; the floored one is used for acceptance.
7.7 Far field: E_F(r) = || r^alpha U_sph(r, th, chi - (omega/c_l) log r) - F || / ||F|| on S^2 (expected
    O(r^-(alpha+1)) from G); E_G(r) = || r^(2alpha+1) (U - r^-alpha F) - G[F] || / ||G[F]|| with G[F] computed from the
    candidate's own F by 3.4 (expected O(r^(2alpha-3)), faster after subtracting the fitted l = 2 multipole term);
    if ||G[F]|| < 1e-8 ||F|| (degenerate), report the absolute defect || r^(2alpha+1)(U - r^-alpha F) || in the
    F-gauge instead and say so;
    report the fitted C_2m and compare with the finite-part moment of the source.
    Derivative and vorticity tails (v1): E_H(r) = || r^(1/c_l) Omega_sph(r, th, chi - (omega/c_l) log r) - H || / ||H||
    with H from 3.3 computed from the candidate's F, and E_D(r), the same for r^(alpha+1) DU against the derivative
    of the leading tail; both must decrease at the rate predicted by the next term.
    Note (astra audit): E_G <= 1e-2 neither implies nor contradicts rho_nl <= 1e-5; both are required.
7.8 Identities (Stage III, also cheap earlier): energy flux at radii R in {2^j r_core}: relative mismatch
    |LHS-RHS|/(|LHS|+|RHS|); helicity at finite R: (1-2c_l) integral_{B_R} U.Omega
    = -(1/2) integral_{dB_R} [(W.n)(U.Omega) + (Omega.n)(P - |U|^2/2)] dS, and the total helicity with the exterior
    estimate R^(2-2alpha)/(2alpha-2) integral_{S^2} F.H dS; flux integral_{dB_R} U.n dS = 0; Poisson independently
    of momentum; vorticity-maximum identity; V(z,s) equation at several s.
    Ball-integral laws [conservation forms V, d04; consequences H, audit pending]. With E(R) = integral_{B_R}|U|^2,
    the energy identity is the exact ODE (c_l/2) R E'(R) - ((5c_l-2)/2) E(R) = -Phi(R),
    Phi(R) = R^2 integral_{S^2} (|U|^2/2 + P) U_r dOmega = O(R^(2-3alpha)) for the natural tail with P = O(r^-2alpha).
    Integrating, E(R) = K_E R^(3-2alpha) + (2/c_l) R^(3-2alpha) integral_R^inf Phi(s) s^(2alpha-4) ds, so
        E(R) R^(2alpha-3) - K_E = O(R^-(alpha+1)),   K_E = (c_l/(5c_l-2)) integral_{S^2}|F|^2,
    i.e. the ball energy has NO constant (finite-part) term: FP_{R->inf} E(R) = 0. Similarly, with
    A(R) = integral_{B_R} (y_1 U_2 - y_2 U_1) and V(R) = integral_{B_R} U:
        c_l R A'(R) - (5c_l-1) A(R) = -R^3 integral_{S^2} U_r (y_1U_2 - y_2U_1)/R dOmega,
        c_l R V'(R) + ((1-4c_l) I + omega J) V(R) = -R^2 integral_{S^2} (U_r U + P n) dOmega,
    whose right sides have no R^0 term in the natural-tail expansion (rates a alpha + b never equal 3 inside the
    range), so FP A = 0 and FP V = 0 (V_1 = V_2 = 0 anyway under the two-fold symmetry). Helicity: the ball value
    h(R) = integral_{B_R} U.Omega tends to 0 like -R^(2-2alpha) integral_{S^2} F.H dS/(2alpha-2). For a candidate,
    report E(R)R^(2alpha-3)/K_E - 1, FP-type remainders of A and V_3 against their fitted power laws, and h(R) against
    the exterior estimate, at R = 2^j r_core, with the flux side evaluated independently; deviations must be
    explained by the measured residual (integrate U.R_u, (Jy).R_u, R_u over B_R and report them alongside).
    First far coefficients (v1.24, 2026-10-25T09:54:00Z; ADDITION ONLY, diagnostic, no threshold; FINAL_REPORT section 2,
    items 30 and 34, both independently proved). Let V_1 be the rate-(2alpha+1) part of a state (blocks B and D of
    the primary representation, channel 2 of the independent basis), U_0 = r^-alpha F, Omega_0 = r^-(alpha+1) H and
    P_0 = r^(-2alpha) Q the pressure of the leading tail. Report beside the energy ratio K_E(carried)/K_E(required)
    (the primary route's K_ratio_direct, K_E = 2(2-3alpha) Phi_F) the helicity ratio K_H(carried)/K_H(required),
    with K_H(required) = (1-3alpha) Psi_F, Psi_F = integral_{S^2} [(F.H) F_r + (Q - |F|^2/2) H_r] dS, and
    K_H(carried) = s^(3alpha+2) integral_{S^2} (U_0.curl V_1 + V_1.Omega_0)(s n) dS (independent of s). An exact
    profile has both ratios equal to 1 where the required value is nonzero; the two are different projections of the
    defect V_1 - N_0, N_0 = (U_0.grad)U_0 + grad P_0. With H_F = integral_{S^2} F.H dS the exterior helicity of the
    first sentence of 7.8 is integral_{r>R} h = H_F R^(2-2alpha)/(2alpha-2) + K_H R^(1-3alpha)/(3alpha-1)
    + O(R^(-alpha-2)) for an exact profile.
    Global weighted identities (v1.1) [V, d05/d05b: exact local divergence forms on random polynomial fields;
    global limits H, by the boundary terms W.n = c_l R + U_r and the natural tail]. K = |U|^2/2, h = U.Omega,
    S = sym DU, F and H the leading velocity and vorticity tail coefficients, all integrals absolutely convergent:
      (E) integral_{R^3} r^(2alpha-4) U_r (K + P) dy = - c_l integral_{S^2}|F|^2 dS / (2(3-2alpha))
          (weight r^(2alpha-3) on U.R_u; the global form of the ball ODE; with the F-gauge the left side is < 0);
      (V) integral_{B_R} (|U|^2 + 3P) dy = R integral_{dB_R} (U_r^2 + P) dS for EVERY R (from y.R_u; independent of
          c_l and omega); its right side has no R^0 term, so FP_{R->inf} integral_{B_R} P dy = 0 given FP E = 0;
      (O) integral_{R^3} r^(2alpha-1) [Omega.S Omega + (2alpha-1)(U_r/r)|Omega|^2/2] dy = (c_l/2) integral_{S^2}|H|^2 dS
          (weight r^(2alpha-1) on Omega.R_Omega; right side > 0 for a nonzero tail);
      (Hel) (2alpha-2) integral_{R^3} r^(2alpha-4) [(y.U) h + (y.Omega)(P - K)] dy = c_l integral_{S^2} F.H dS
          (weight r^(2alpha-2) on Omega.R_u + U.R_Omega).
    These are consistency checks, not obstructions (no integrand has a sign). For a Stage III candidate report
    each side, the mismatch relative to the larger side, and the corresponding weighted residual integrals
    (r^(2alpha-3) U.R_u, y.R_u, r^(2alpha-1) Omega.R_Omega, r^(2alpha-2)(Omega.R_u + U.R_Omega)) over the resolved
    region plus the analytic-tail exterior; a mismatch not explained by them is a defect.
    v1.2 additions (source astra integrallaws1; every local identity re-checked exactly by the lead,
    derivations/d08_integrallaws_checks.py, d08.log 17/17 PASS; global limits [H, A]; (E), (V), (O), (Hel) of
    v1.1 confirmed by the independent route and re-derived by astra):
      (V) is a PRESSURE-CONSISTENCY identity, not a momentum test: for div U = 0, div R_u = -R_P exactly, so
          integral_{B_R} y.R_u = -integral_{B_R} ((R^2 - r^2)/2) R_P. It holds for every divergence-free U with the
          exact full-space pressure, whatever R_u; the same is true for X = r^2 y and every radial gradient
          multiplier. Use it to test the pressure solve and quadrature only. Leading coefficient:
          integral_{S^2} Q dS = (q S_r - S)/(2alpha), q = 3-2alpha, S = integral |F|^2, S_r = integral F_r^2.
          The radial cubic identity has a nonzero constant only at c_l = 3/7 (not a grid point).
      (Z0) total stretching: integral_{R^3} Omega.S Omega dy = (1 - 3c_l/2) integral_{R^3} |Omega|^2 dy > 0
          (absolutely convergent; boundary term (c_l/2) R^(1-2alpha) integral |H|^2 -> 0; residual form:
          (1 - 3c_l/2) integral |Omega|^2 - integral Omega.S Omega = integral Omega.R_Omega). It is the m = 0 member
          of the family, for -3 < m <= 2alpha-1 (v1.3, verifier qualification: absolutely convergent near the
          origin for -2 < m, or for -3 < m if U(0) = 0; for general smooth U and -3 < m <= -2 the integral is the
          spherical improper limit over r > eps),
              integral r^m [Omega.S Omega + (m/2)(U_r/r)|Omega|^2 - (1 - 3c_l/2 - m c_l/2)|Omega|^2] dy
                  = (c_l/2) integral_{S^2}|H|^2 dS if m = 2alpha-1 (this is (O)), and 0 if m < 2alpha-1.
          Stretching ratio Sigma_Z := integral Omega.S Omega / ((1 - 3c_l/2) integral |Omega|^2), exact value 1.
          (v1.15) By Cauchy-Schwarz on the residual form above, ||R_Omega||_2 / ||Omega||_2 >= (1 - 3c_l/2)|1 - Sigma_Z|
          (factor 0.325 at c_l = 0.45; d30). Report this bound beside Sigma_Z. It is necessary, not sufficient.
          (v1.16) Local form (verifier proof 23:39Z; d29 addendum 2): for every field and every centred ball B_a,
          ||Q_1 Omega||_{B_a} >= (1 - 3c_l/2)||Omega||_{B_a}, so an exact profile has ||[U,Omega]||_{B_a} >= 0.325
          ||Omega||_{B_a} at c_l = 0.45 on every centred ball. Report ||[U,Omega]||_{B_a} / ||Omega||_{B_a} and
          ||R_Omega||_{B_a} / ||Omega||_{B_a} for a = 1/4, 1/2, 1 (reported diagnostics, no threshold). For momentum the
          same integration gives the factor 1 - 5c_l/2 < 0: no momentum L2 coercivity follows.
          Energy ratio Sigma_E := -2(3-2alpha) integral r^(2alpha-4) U_r (K+P) dy / (c_l integral |F|^2), exact value 1.
          Both are dilation invariant and proportional to the amplitude for a weak field (2.8(f)). The exterior
          beyond the resolved region is added analytically from the tail (|Omega|^2 ~ r^(-2alpha-2)|H|^2 decays slowly).
      (K) special conformal fields K_a = 2(a.y)y - r^2 a: with S(R) = integral_{B_R} [2y(y.U) - r^2 U] and
          M(R) = integral_{B_R} y(|U|^2 + 3P), [(1-6c_l) I + omega J] FP S = 2 FP M (finite parts after subtracting
          the R^(5-alpha), R^(4-2alpha) terms, whose transverse coefficients rotate by exp(-(omega/c_l) log R J));
          under the two-fold symmetry only the third components remain: (1-6c_l) FP S_3 = 2 FP M_3. A signed
          core-moment relation, not an obstruction.
      Angular momentum to next order: A(R) = a_F R^(4-alpha)/(4-alpha) + a_0 R^(3-2alpha) + O(R^(2-3alpha)),
          a_F = integral_{S^2} sin(theta) F_phi, a_0 = integral_{S^2} F_r sin(theta) F_phi (the same coefficient was
          obtained independently by the verifier route and by astra [I]); quadrupole velocities carry no torque.
      Momentum is kinematic: integral_{B_R} U = integral_{dB_R} y U_r for div U = 0, so FP V = 0 carries no
          information about R_u.
      Residual error formulas (when the residual moments converge): FP E = -(2/(5c_l-2)) integral U.R_u,
          FP A = -(1/(5c_l-1)) integral (Jy).R_u, h_inf = (1/(1-2c_l)) integral Omega.R_u, and (Z0) above. On a shell
          A_R, |integral_{A_R} X.R_u| <= ||X||_{L^2(A_R)} ||R_u||_{L^2(A_R)}; absolute summation needs at least R_u = o(r^-4)
          for A and o(r^-6) for the radial cubic (necessary power thresholds only; v1.3, verifier: a sufficient
          condition is O(r^(-4-delta)), respectively O(r^(-6-delta)), delta > 0, or explicit integrability; r^-4/log r
          is not enough), otherwise the residual moment is itself finite-part regularized.

7.9 Required tests before production results are used for ranking (numerics lane; verifier repeats the starred ones
    in its own code):
    T01* operator test on a manufactured smooth divergence-free field with exactly computed R_u, R_Omega, R_P
         (relative error <= 1e-12 in float64);
    T02* curl R_u = R_Omega numerically on a non-solution field;
    T03* pressure: Green formula on manufactured sources with known decaying solutions, including a source with
         twisted r^(-2alpha-2) tail and m != 0 (closed-form exterior integrals), and a cross-check against the
         independent ray-integral or free-space kernel;
    T04* dilation regression: for L in {2^-3, 2^-1, 3, 2^4}, evaluate the diagnostics of 7.2 to 7.5 on (U_L, P_L)
         with shells rescaled by L (and before re-gauging). Invariant (agree to 1e-10): all rho, pi, peak, tau_j,
         N_k, E_F and E_G at corresponding radii, max|DU|, max|Omega|, lambda_max(S) at max|Omega|, ratios of radii.
         Covariant, with the stated powers checked: r_core, r_tail, widths ~ L; max|U| ~ L; max|D^2 U| ~ L^-1;
         P ~ L^2; R_u ~ L, R_Omega ~ L^0, R_P ~ L^0 (pointwise at y <-> y/L); F and r^alpha R_u ~ L^(1+alpha);
         integral |F|^2 ~ L^(2(1+alpha)). After re-imposing the F-gauge all values return to the original ones;
    T05* rotation covariance (phase shift b): diagnostics unchanged to 1e-12;
    T06  reflection S: omega -> -omega regression (2.3): the S-mirrored state evaluated on mirrored points has the
         same diagnostics to 1e-12; optimizer histories are compared only if nodes, quadrature, coefficient
         coordinates, gauge pivot and optimizer state are mirrored exactly;
    T07* far-field: L[r^(-alpha)F] = 0 numerically for the seed and for random (sigma, tau); the Q equation and
         G[F] against a direct evaluation of (U_0.grad)U_0 + grad(r^(-2alpha)Q);
    T08  origin regularity: R_u and its first two derivatives at y = 0 finite and consistent with nearby points;
    T09  aliasing: raising nonlinear quadrature by 1.5x changes the residual by < 10% at the working resolution;
    T10  holdout: holdout and training residuals within a factor 3 (else flagged);
    T11  restart determinism: kill/resume from checkpoint reproduces the next 10 iterations to 1e-10;
    T12  gauge: F-gauge and pivot phase hold after every accepted step; switching pivot leaves diagnostics unchanged.
7.10 Field-comparison norm (v1; an unweighted full-space L^2 difference diverges for these tails). For two
    gauge-aligned states (same F-gauge, rotation phase aligned by minimizing the norm over b),
        ||V||_* = max over the shells of 7.1 (core ball and dyadic shells up to the outermost resolved shell, and the
                  far checkpoints) of RMS_k(V) / RMS_k(U_ref),
    with U_ref the finer state; the same with DU and Omega in place of U gives ||.||_*,1. All "field difference"
    statements in section 8 use ||.||_* and ||.||_*,1. Parameter differences are reported with the uncertainties of
    the fits (c_l, omega, C_lm, F coefficients).
7.11 Exterior closure tests (v1; an unresolved exterior can otherwise pass, astra audit). For any state using an
    analytic tail model beyond R_far:
    X1 diagnostics of 7.2-7.7 evaluated on shells just inside R_far BEFORE analytic closure (resolved field only);
    X2 matching: the jumps of U, DU, D^2 U across r = R_far, relative to the shell RMS of each, <= the Tier
       threshold of rho_u (for Tier A: 1e-6, 1e-5, 1e-4 for U, DU, D^2 U);
    X3 matching-radius change: R_far moved by a factor 4 in each direction changes rho_u^max, rho_nl^max and the
       fitted C_lm by less than a factor 2 (rho) and less than their stated uncertainty (C_lm);
    X4 independent full-pressure evaluation (5.4) at the far checkpoints, not the tail model's pressure;
    X5 systematic maximization of |R_u| and |R_Omega| in every far shell: 4096 random points per shell plus local
       maximization started from the 20 worst points; the maximum enters pi_u and pi_nl.
    Checkpoint values generated from the same analytic tail are labelled "model" and never count alone as
    evidence of resolution.
7.12 Orbit averages along the backward flow (v1.4; CONFIRMED 18:58Z, O1 where Omega != 0; diagnostic and failure-mode explanation, not an acceptance
    criterion; derivations/d11_stretch1_review.md section 3, signs checked numerically in d11 S6). For a computed
    state with its own W and residuals, along each backward orbit y_t (dy/dt = -W), <f>_T = (1/T) int_0^T f(y_t) dt:
     (O1) <s + rho_Om>_T = 1 + [log|Omega(p)| - log|Omega(y_T)|]/T, s = Omega.S Omega/|Omega|^2,
          rho_Om = Omega.R_Omega/|Omega|^2;
     (O2) (1-2c_l) <U.W>_T = <W.R_u>_T + [g(y_T) - g(p)]/T, g = U.W - |U|^2/2 + P;
     (O3) (1-2c_l) <|V|^2 - omega ell>_T = <W.R_u>_T + [G(y_T) - G(p)]/T, G = H_0 - omega ell, V = c_l y + U;
     (O4) <(1-2c_l) ell + d_phi P>_T = <(J y).R_u>_T + [ell(y_T) - ell(p)]/T.
    These are exact for any field. For an exact profile, <s>_T >= 1 - O(1/T) on every vortical orbit and the left
    sides of (O2)-(O4) tend to 0. Residuals enter linearly, not amplified. Report for 64 vortical seeds per ranked
    state (|W x Omega| >= 0.2 |W||Omega|, |Omega| >= 1e-3 max|Omega|), T in {2, 4, 8, 16}/c_l: <s>_T, <rho_Om>_T, the
    (O1) boundary term, the left sides of (O2)-(O4) with their residual and boundary terms, and finite-time backward
    Lyapunov exponents (QR method) compared with 1-2c_l. The vorticity-transport defect of d07 is not used beyond
    a few time units (it is amplified by up to e^((1+M_-)t)).

7.13 Outgoing and strength diagnostics (v1.6; diagnostic only, not an acceptance criterion; 2.8(i)). For every
    ranked state: (a) at every located zero y* of W, the eigenvalues of sym DW(y*) = c_l I + S(y*) and
    |Omega(y*)|/max|Omega| (an exact vortical zero has lambda_min < 0 and lambda_max >= 1 + c_l); (b) on the core
    shells, min and max of W.y/|y|^2 over the sphere (a state with W.y >= c*|y|^2 everywhere, c* > 0, is
    incompatible with an exact profile); (c) Gamma_2 = 4.40051 ||grad Omega||_inf^(3/5) ||Omega||_2^(2/5) (an exact
    profile has Gamma_2 >= 1; ||grad Omega||_inf from located maxima plus a dense sample, so the computed value is a
    lower estimate of the state's Gamma_2, not a certified bound when sup|grad Omega| or the enstrophy is
    unresolved).
    (v1.7, derivations/d14_quantrot_review.md) (d) Trapping radius R_trap = smallest R with
    c_l|y| + (y/|y|).U(y) > 0 on the sampled region |y| > R (exact bound R_trap <= max|U|/c_l; report both), the
    maximum of lambda_max(S) over |y| <= R_trap (an exact profile has it >= 1: every backward alpha-limit set lies
    in that ball, and the alpha-limit set of every vortical point meets {lambda_max(S) >= 1}), and whether the
    located maximum of |Omega| lies inside R_trap. A sampled radial sign gives an estimate of R_trap, not a
    certified value. (e) With A = max|U| and R = 2/c_l + 4: B(u) = max_{B_AR}|DU| + A max_{B_AR}|D^2 U| and the core
    non-axisymmetry ratios max_{B_AR}|K U| / max_{B_AR}|U| and integral_{B_AR}|K Omega|^2 / integral_{B_AR}|Omega|^2
    (dilation invariant; an exact profile has them bounded below by a positive constant depending only on c_l and
    B(u), whose value is unknown, so no threshold is attached).

7.14 Exact checks along orbits and on invariant sets (v1.8; diagnostic only, not an acceptance criterion; 2.8(j)).
    Reported for ranked states when the corresponding objects are located; no threshold is attached. Along a
    backward orbit X' = -W(X), M' = -DW(X) M, M(0) = I, X(0) = p:
    (a) det M_t = e^(-3c_l t); M_t Omega(p) = e^(-(1+c_l)t) Omega(X_t); M_t^T beta(X_t) = e^(kt) beta(p),
        beta = (W x Omega)/k (relative defects as functions of t). (Wording 20:47Z, independent route 20:38Z: on an
        approximate state beta_0 = (W x Omega)^flat/k has L_W beta_0 + k beta_0 = (W x curl R_u)^flat/k, so this
        pullback tests vorticity-residual transport; beta_1 = U^flat + dB/k has defect R_u^flat + d(W.R_u)/k and
        tests the momentum residual. Report which form is used; they coincide only for exact solutions.)
    (b) Endpoint-corrected integrals over [0, T] (integrands at X_t): integral y.W = (|p|^2 - |X_T|^2)/2;
        integral U.W = (B(X_T) - B(p))/k; integral (k ell + d_phi P) = ell(X_T) - ell(p);
        integral (k|V|^2 + omega d_phi P) = H_0(X_T) - H_0(p);
        integral (|V|^2 + c_l(1-c_l)|y|^2 - y.grad P) = D(p) - D(X_T). For a state each defect is an integral of
        R_u-terms along the orbit (it is a residual measured along the backward dynamics, not a new norm).
    (c) A located vortical periodic orbit of period T_0: forward multipliers 1, e^((1+c_l)T_0), e^(-k T_0);
        circulation 0; signed projected area 2 omega A_z = -integral_0^T_0 |W|^2 dt.
    (d) The pressure-virial region {y.grad P >= c_l(1-c_l)|y|^2} inside the estimated trapping ball: volume fraction
        and whether located recurrent orbits visit it.
    (e) Pressure Poisson defect Delta P + tr((DU)^2) (local; does not certify the full-space pressure of 5.1).
    (f) Helicity push-forward integral f(B) U.Omega dy (exact value 0) for smoothed bins f of B, with the exterior
        contribution estimated from the leading tail; reported only with that tail estimate.
    (g) On any located compact invariant set: min|W|, min|Omega|, min|W x Omega| and the moments E, L, I, T, Q
        (exact: E = omega L, omega T = -kE, E + Q = omega^2 I) before uniform hyperbolicity is invoked.

## 8. Pre-registered acceptance thresholds (registered 2026-10-24T17:28Z, before any candidate exists)

All on points not used in training or adaptive sampling, with the full-space pressure of 5.1 computed from the
candidate's U (a separately learned pressure may be reported but never replaces 5.1), in float64 with the
algebraic far-field cancellation and extended-precision checks of 7.2. v1: model-selection HOLDOUT points (used
for ranking, early stopping, choosing levels or hyperparameters) are distinct from FINAL-TEST points, drawn with a
fresh recorded seed after the candidate's coefficients are frozen (by the verifier for Tier R and A) and used only
for acceptance. Each tier includes every requirement of the lower tiers (nested), evaluated at the tier's own
level.

Tier S (Stage I discovery lead): rho_u^max <= 1e-2, rho_nl^max <= 1e-1, rho_P^max <= 1e-3, rho_div^max <= 1e-8
  (all representations; curl representations reach roundoff), N1 to N6 without failure flags (N2:
  lambda_max(S) >= 0.9 at max |Omega|), N_core >= 1e-2 and N_F >= 1e-2, and (v1) e_core >= 1e-4 and e_F >= 1e-4.
  States above the screen are still ranked and kept, labelled "below screen".
Tier R (Stage II refinement-stable): three levels L1 < L2 < L3 (each raises angular degree and radial dofs by at
  least 1.3x and nonlinear quadrature by at least 1.5x); rho_u^max(L3) <= 1e-4 and rho_nl^max(L3) <= 1e-3;
  monotone decrease with rho_u^max(L1)/rho_u^max(L3) >= 10; gauge-aligned field differences decreasing
  (||U_L3 - U_L2||_* < ||U_L2 - U_L1||_*, and the same for ||.||_*,1; norms of 7.10); parameter drift L2->L3
  smaller than L1->L2; verifier's independent pressure and momentum re-evaluation within a factor 3 of the
  numerics values; N1 to N6 stable; (v1) N_core, N_F, e_core, e_F not collapsing (7.4); X1 and X4 of 7.11 done.
Tier A (label A requires all): rho_u^max <= 1e-6, rho_Om^max <= 1e-5, rho_nl^max <= 1e-5, pi_u^max <= 1e-4,
  rho_P^max <= 1e-7, rho_div^max <= 1e-10 (exactly solenoidal representation; else <= 1e-8, v1: was 1e-7, which
  was looser than Tier S), tau_0, tau_1, tau_2 <= 1e-5 (floored ratios of 7.6); three progressively improving
  refinements; E_F(r) decreasing at the predicted rate and E_G <= 1e-2 at
  the outermost resolved checkpoint after subtracting the fitted l = 2 multipole velocity term; energy and helicity identities
  consistent within their error estimates; vorticity-maximum identity within 1e-4; no peak factor above 30
  without explanation; verifier's independent re-evaluation in its own code within a factor 3 and its independent
  refinement in its own representation converging to the same gauge-aligned field (relative difference <= 1e-4)
  and parameters within the stated uncertainty.
  Added in v1 (stricter; astra audit, values chosen by the lead before any candidate exists): all Tier S and Tier R
  requirements at the finest level, including N1-N6, N_core, N_F, e_core, e_F and the non-collapse rule;
  A_u <= 1e-5 and A_Om <= 1e-4 (7.2); pi_nl^max <= 1e-3 and rho_Om_nl^max <= 1e-4; E_H and E_D decreasing at the
  predicted rates (7.7); X1-X5 of 7.11 passed; the bound on every omitted tail term (3.5) below each threshold;
  the field comparison "relative difference <= 1e-4" is in ||.||_* and ||.||_*,1 (7.10); float64 and extended
  precision far checkpoints agree (7.2). (Astra proposed 1e-6, 1e-6, 1e-4, 1e-5 for A_u, A_Om, pi_nl, rho_Om_nl
  with an unnormalized A; the lead normalized A by Lambda and kept the pattern of the v0 tiers, where the
  nonlinear and vorticity ratios are 10x and the pointwise ratios 100x the momentum RMS value.)
Added in v1.15 (2026-10-24T23:31:23Z; tightening, astra steadycore1, values chosen by the lead before any candidate exists; at
  registration no saved state of either route meets Tier S: the independent route's states have rho_u^max >= 0.07 and
  core rho_sp^max >= 0.72; the primary route's best states have rho_u^max 0.046 to 0.055 on standard shells and
  rho_nl^max >= 2.9 over all shells, so rho_sp^max >= 2.9): rho_sp^max <= 1e-1 in Tier S, <= 1e-3 in Tier R (at L3), <= 1e-5 in Tier A,
  and in Tier A also rho_Om_sp^max <= 1e-4 (vorticity form, the 10x pattern of v1). Momentum form, all positive-volume
  shells of both families of 7.3a, with the denominator flags of 7.2 (a flagged shell fails the item until cleared by
  refinement or an explicitly registered structural-zero treatment). No point ratio at y = 0; the origin jets of 7.6
  are unchanged. All earlier requirements are retained.
Added in v1.17 (2026-10-25T01:16:37Z; tightening, astra noncoer1 audited in derivations/d39, values chosen by the lead before any
  candidate exists; at registration no saved state of either route meets Tier S). Reason: in the continuum no ratio of
  7.2 is a proximity certificate. (Wording qualified 2026-10-25T01:28:56Z after the verifier's notes of 2026-10-25T01:21Z and
  01:24Z: the ratios meant are rho_u, rho_nl, rho_lin, rho_sp, pi_u, pi_nl, A_u and A_Om; the two single-term ratios
  of 7.2 resist both constructions, see v1.19.) Large multiples of fixed disjoint compact steady Euler copies drive rho_u, rho_nl,
  pi_u, pi_nl, A_u and A_Om to zero (rho_lin and rho_sp keep positive limits); shrinking copies centred at zeros of the
  transport field (c_l I - omega J) y + U drive all of these, rho_lin and rho_sp included, to zero at a fixed local L2
  distance from every exact profile, with the tail, gauge and phase unchanged (d39). The
  escapes need growing amplitude or shrinking support, so for Tier R and Tier A, in addition to all earlier items:
  (a) a_max = max_k (1 + r_k)^(2alpha+1) RMS_k(R_u) in the F-gauge (the fixed-gauge value of 7.2) decreases
      monotonically over L1, L2, L3 with a_max(L1)/a_max(L3) >= 10;
  (b) the gauge-aligned field sizes max |U|, max |Omega| (over the shell nodes of 7.3a and the FINAL-TEST points)
      and ||U||_L2(|y| < 1) grow by at most 10 per cent from L2 to L3;
  (c) on every shell, peak(k) of 7.2 grows by at most a factor 2 from L2 to L3 (Tier A keeps its bound of 30).
  These items do not make any criterion a proximity certificate; they make the two known escapes visible as
  resolution-dependent growth. All earlier requirements are retained.
Added in v1.19 (2026-10-25T01:28:56Z; tightening, verifier proof of the concentration construction (2026-10-25T01:24Z)
  reviewed in derivations/d39 section 6, values chosen by the lead before any candidate exists; at registration no
  saved state of either route meets Tier S, and every state's single-term values are far above the thresholds below).
  Reason: of the registered ratios, the two single-term ratios of 7.2 are the ones proved to stay bounded away from
  zero along the continuum escapes of d39. The global vorticity ratio ||R_Omega||_2/||Omega||_2 tends to a limit
  >= 1 - 3c_l/2 for shrinking copies of amplitude 1/delta and delta^-3; the shell momentum ratio
  RMS_k(R_u)/RMS_k((1 - c_l)U) tends to a limit >= |1 - 5c_l/2|/(1 - c_l) on each shell carrying a copy of amplitude
  delta^-3, and to the value of the patched background for amplitude 1/delta (0.325 and 0.227 at c_l = 0.45). They are
  not proximity certificates. In addition to all earlier items:
  (a) sigma_u^max = max_k RMS_k(R_u)/RMS_k((1 - c_l)U), over all positive-volume shells of both families of 7.3a and the
      ball |y| < 1: <= 1e-1 (Tier S), <= 1e-3 (Tier R, at L3), <= 1e-5 (Tier A);
  (b) sigma_Om = ||R_Omega||_2/||Omega||_2 over all resolved shells (with the exterior of 7.8 when available):
      <= 1e-1 (Tier S), <= 1e-3 (Tier R, at L3), <= 1e-4 (Tier A, the 10x vorticity pattern of v1).
  Denominator flag for (a): a shell is flagged if (1 + r_k)^alpha RMS_k((1 - c_l)U) is below 1e-14 times its largest
  value over shells or below 1e-3 times both neighbours (r_k as in 7.2, origin ball r_k = 0); a flagged shell fails
  (a) until cleared as in v1.15. Values at registration (lead computation from the verifier's fresh pressure-order-18
  shell files, standard / offset family): sigma_u^max 3.04 / 3.19 (independent D4 at 8000 iterations), 2.52 / 2.39
  (D6 at 10000), 3.13 / 2.60 (D6 after 400 Gauss-Newton steps), each on a shell inside [1/16, 1/2); the ball value
  over |y| < 1 was 1.16 to 2.19 in the six states of d30. All earlier requirements are retained.
Added in v1.21 (2026-10-25T02:23:11Z; tightening, astra edge1 audited in derivations/d43, values chosen by the lead before any
  candidate exists; at registration no saved state of either route meets Tier S, since every checked state has
  sigma_u^max >= 2.39). Reason: an explicit smooth axisymmetric swirl family with exact unit tail (d43 section 2) has
  rho_u^max = Theta(1/2 - c_l) while its resolved single-term ratio stays near 1/(1 - c_l) on shells inside its core
  radius a; when the innermost registered set is much larger than a, sigma_u^max and a_max on the registered sets tend
  to zero logarithmically. The 7.1 core ball r < r_core 2^-5 has radius 0.45 a at c_l = 0.45, 1.21 a at c_l = 0.48 and
  2.47 a at c_l = 0.49 for that family (d43_core_scale.log). In addition to all earlier items, for every tier and for
  the 7.3b ordering:
  (a) core scale: a_eff = 2 sqrt2 max|U| / max|Omega| (gauge-aligned maxima as in v1.17 (b)), with y_* a node where
      |Omega| is largest. Reported for every state and level.
  (b) core-resolved sets: sigma_u^max (v1.19 (a)) and a_max (v1.17 (a)) are taken over the sets of v1.19 (a) together
      with (i) dyadic shells extending the 7.1 family inward to inner radius a_eff/16, plus the ball r < a_eff/16, when
      r_core 2^-5 > a_eff/16, and (ii) the balls B(y_*, a_eff/2) and B(y_*, a_eff/4). sigma_Om (v1.19 (b)) is unchanged
      (global), and its ratio restricted to B(y_*, a_eff/2) is reported.
  (c) core resolution: on each added set the quadrature value of RMS(R_u) and RMS((1 - c_l)U) changes by less than 10
      per cent when the radial and angular node counts are doubled, and a_eff changes by less than 10 per cent from L2
      to L3. A state failing (c) is "core unresolved": it fails every tier and is not ordered under 7.3b.
  (d) near edge: a state or free-parameter arm with 1/2 - c_l < 0.02 or c_l - 2/5 < 0.02 is labelled "near edge"; it
      can support label A or B only if, besides (a) to (c), a_eff, the enstrophy containment radius R_90 (or the
      statement that the saved window does not contain 90 per cent of the enstrophy) and the tail-fit onset radius
      each change by at most a factor 2 between L2 and L3. An interior-family claim states its positive distance
      from 1/2.
  (e) reported without threshold: E_ren = lim_R (int_(B_R) |U|^2 - R^p/p), p = 3 - 2 alpha, with the omitted remainder
      bounded, and both sides of the ball identity int_(B_R) U.R_u = beta_0 E(R) + (c_l R/2) E'(R) + int_(S_R) H U.n
      (H = P + |U|^2/2, beta_0 = 1 - 5c_l/2) at the far checkpoints of 7.1. Every exact profile in the tail class has
      E_ren = 0 and int U.R_u = beta_0 E_ren (d43 section 3 (b)); agreement of the two sides checks the pressure
      convention and the quadrature.
  These items do not make any criterion a proximity certificate. All earlier requirements are retained.
Added in v1.22 (2026-10-25T02:49:47Z; ADDITION ONLY, reported without threshold; astra formul1 audited in
  derivations/d46_backward_formulation_audit.md; no tier, ordering, stall or label rule changes, apart from the stricter
  reading of an ambiguity in (c)). Both quantities use G,
  the unique inverse of L with outputs bounded near 0: G f(y) = int_(-inf)^0 e^((1-c_l)s) R(omega s) f(e^(c_l s) R(-omega s) y) ds,
  R(t) = exp(tJ). In spherical components G acts along twisted rays (theta and chi = phi + (omega/c_l) log r fixed):
  (G f)_sph(r, theta, chi) = (1/c_l) r^(-alpha) int_0^r rho^(alpha-1) f_sph(rho, theta, chi) d rho, where f_sph(rho, theta, chi)
  denotes the spherical components of f at radius rho, polar angle theta and azimuth chi - (omega/c_l) log rho (d46 checks
  this against the Cartesian form to 3.3e-16).
  (a) tail-generation defect tau_F(R_w) = ||F^(R_w)[R_u]||_(L2(S^2)) / ||F_U||_(L2(S^2)), with
      F^(R_w)[f](theta, chi) = (1/c_l) int_0^(R_w) rho^(alpha-1) f_sph(rho, theta, chi) d rho and F_U the registered
      leading-tail coefficient in the same (theta, chi) variables (unit norm in the tail gauge). Exactly, for smooth U,
      F^(R_w)[L U] = R_w^alpha U_sph(R_w, theta, chi), so F^(R_w)[R_u] = R_w^alpha U_sph(R_w, theta, chi) + F^(R_w)[N(U)],
      N(U) = (U.grad)U + grad P. Report tau_F at two radii R_w >= 2^8 r_core where the residual is evaluated, by both
      routes (direct ray integral of R_u, and the identity); their difference is a quadrature check. A value that
      changes by more than 10 per cent when the radial and angular node counts are doubled is reported as unresolved.
  (b) backward defect delta_G(S) = RMS_S(G R_u) / RMS_S(U) on the 7.1 core ball and on B(y_*, a_eff/2) (v1.21 (a)),
      by both routes (G R_u directly, and U + G N(U), since G L U = U for U bounded near 0), with the same
      node-doubling rule.
  Interpretation fixed at registration: both are zero for an exact profile in the tail class; the pure-swirl near-edge
  family of v1.21 has |G R_u| >= |U| pointwise and tau_F >= R_w^alpha ||U_sph(R_w)|| / ||F_U||, close to 1 (d46 item 12);
  a pure compact steady copy V has backward defect V; shrinking copies at a zero of (c_l I - omega J) y + U drive
  delta_G on B(y_*, a_eff/2) to zero (d46 item 11). Neither quantity is a proximity certificate or enters a tier.
  (c) convention for v1.21 (b)(ii) (clarification 2026-10-25T02:53:01Z, requested by the verifier at 02:38Z; no result was
      promoted under the ambiguity): on the balls B(y_*, a_eff/2) and B(y_*, a_eff/4) the a_max weight uses
      r_k = |y_*| (centre weight, the analogue of the shell midpoint); the upper-radius value
      (1 + |y_*| + radius)^(2 alpha + 1) RMS(R_u) is reported alongside, and the v1.17 (a) decrease requirement must
      hold with both weights, each compared across levels with the same weight. This is the stricter reading.
Stall rule: a branch is "stalled" if over the last two refinement levels rho_u^max decreases by less than 2x while
  rho_u^max >= 1e-3. A stalled branch cannot be labelled B.

## 9. Outcome labels (mapping used in FINAL_REPORT.md)

A: a Tier A candidate, verified. Not a proof of existence.
B: a structured candidate that passes Tier S at the finest level, decreases rho_u^max by a total factor >= 10
   under at least three refinements without stalling, has an independent re-evaluation agreeing within a factor 3,
   stable N1 to N6, but fails some Tier A item; all defects stated quantitatively.
C: otherwise, with the precise searched class (parameters, representations, symmetry, seeds, budgets, failure
   modes). Not nonexistence.
D: only a complete, independently confirmed proof covering the stated class. An optimizer failure never gives D.

## 10. Candidate exchange format (numerics -> verifier)

candidates/<id>/ with: meta.json (c_l, omega, basis version, L_max, radial dofs, element breakpoints, R_0,
gauges and pivot, software versions, numerics diagnostics, sha256 of every file); BASIS.md (exact mathematical
definition: Y_l^m normalization, potential decomposition, radial functions, twist, exterior factorization, tail
model) sufficient to write an independent evaluator; coeffs.npz; samples.npz with U (Cartesian), DU (3x3), P and
grad P on (i) the tensor grid r = 2^(j/4) r_core, j = -24..80, theta max(32, 3L_max/2 + 1) Gauss-Legendre
nodes, phi max(64, 3L_max + 1) uniform nodes (v1: N_phi >= 2L_max + 1 is needed even for linear
reconstruction, more for nonlinear terms; this exchange grid is for transfer only and is NEVER the acceptance
grid, which follows the candidate's resolution, 7.9 T09 and 7.11 X5), (ii) 65536 random points (seed recorded) uniform in log r over the same range and uniform on S^2,
(iii) the axis theta = 0, pi at the grid radii, and y = 0; linearization.npz with the action of the residual
Jacobian on 8 recorded random directions and the 20 smallest singular values (with vectors) if computed;
conditioning estimates and the observed convergence rates. Accepted candidates are immutable (read-only, hashed).

## 11. Search guidance (numerics; adjust to throughput, report deviations)

c_l in {0.41, 0.43, 0.45, 0.47, 0.49}, omega in {0.1, 0.3, 1, 3, 10} (positive; 2.3), fixed first, then free
(watch for saturation at bounds and for drift to c_l = 1/2, 2/5, omega -> 0 or large). Seeds: the eps-family of
3.6 with several eps including order one; random poloidal/toroidal (sigma, tau) mixtures; different core sizes
before gauge fixing; distinct helicity signs and distributions; transferred low-residual states of other routes
(labelled). Aim for 100 to 300 starts if throughput permits; preserve failures with reasons. Spectral ladder
starting l_max 6, 10, 14 with 16, 24, 36 radial dofs per domain; test aliasing by raising quadrature. At least two
optimizers compared (e.g. Levenberg-Marquardt/Gauss-Newton with matrix-free Jacobian and L-BFGS). If the two-fold
search stalls by the Stage I gate, a documented part of Stage II goes to odd-m searches.
Weak-collapse remedy (v1.2). Observed in Stage I by the numerics lane: plain least squares of the vorticity
residual drives every start at fixed c_l to one omega-independent axisymmetric weak state (max|U| = 0.03 in the
F-gauge, r_core = 6, r_tail = 1870, rho_u ~ 1). Since the dimensionless strength (DU, lambda_max(S), Sigma_Z,
Sigma_E) is dilation invariant, no gauge removes this basin (2.8(f)). Training-only remedies, acceptance unchanged:
(i) scale-free residual weighting (each shell's residual divided by its own momentum-term scale, including T4 and
T5); (ii) constraints that every exact profile satisfies, imposed as equality constraints, penalties or by
continuation from a weaker value: Sigma_Z = 1 and Sigma_E = 1 (7.8 v1.2; integrals with the analytic exterior),
and Omega.S Omega = |Omega|^2 at the vorticity maximum; (iii) continuation in the non-axisymmetric energy fraction
e_F or e_core; (iv) seeds whose core strain is of order one (sup lambda_max(S) >= 1). Every state obtained with such
constraints is diagnosed with the unconstrained definitions of section 7; the constraint values are reported.
Compressed-maximum basin (v1.3). The best Stage I states of the independent route have sup lambda_max(S) about 1.5
but Omega.S Omega/|Omega|^2 about -0.3 at the vorticity maximum (exact +1): strong strain away from the vorticity.
Remedy (training only): the stretching identity at the located local maxima of |Omega|^2 as a penalty, or the
pointwise term (Omega.S Omega - |Omega|^2)^2 on points where |grad|Omega|^2| is small relative to |Omega|^2/r_core
[pointwise term WITHDRAWN in v1.5, see (i) below].
Free parameters and branch diagnostics for Stage II (v1.3, from 2.8(h)). (i) c_l and omega become unknowns, kept
inside the registered range, with the two gauges of section 6 (integral_{S^2}|F|^2 = 1 and one azimuthal phase);
fixed-pair runs continue as controls. The parameter derivative of the tail chart contains r^(-alpha) log r terms
(F held fixed in (theta, chi)); the Jacobian must include them (automatic differentiation of the full chart does).
(ii) For each ranked state: singular values of the unregularized, physically scaled Jacobian after gauge removal
(smallest six), the (c_l, omega) components of the corresponding right singular vectors, and the shell localization
of the left singular vectors. (iii) A residual map over (c_l, omega) from warm starts at neighboring pairs: a narrow
valley suggests a curve, an isolated low region suggests selection, a broad low region suggests an open set; none of
these is evidence by itself. (iv) Branch test: perturb in both signs of a small right singular vector, re-solve with
the slice, require a nonzero step that survives refinement. (v) Representation kernels to remove: l = 0 radial parts
of either potential give zero velocity.

Discovery devices (v1.5, from astra strategy1, lead-checked in derivations/d12_strategy1_checks.py, 15/15 PASS;
training only, acceptance unchanged).
(i) Withdrawn: the v1.3 pointwise term (Omega.S Omega - |Omega|^2)^2 on "nearly critical" points. Near a maximum the
    omitted transport term W.grad q/(2q), q = |Omega|^2, is not small (|W| grows like c_l r), so the term biases the
    fit. Use instead (a) tracked peaks: peak positions p_j as unknowns with grad q(p_j) = 0, eta(p_j) = 1,
    eta = Omega.S Omega/q, D^2 q(p_j) negative definite, active-set updates when peaks cross or degenerate; the
    global maximum must be confirmed between nodes and in the tail before it is called global; and (b) the full
    vorticity residual R_Omega, or its exact projection h = Omega.S Omega - q - (1/2) W.grad q = -Omega.R_Omega,
    weighted toward the vortical region.
(ii) Quantitative content: Z > 0 and |Sigma_Z - 1| <= delta give sup lambda_max(S) >= (1 - delta)(1 - 3c_l/2);
    |eta - 1| <= delta_p at the true global maximum of q gives sup lambda_max(S) >= 1 - delta_p. Impose Sigma_Z in
    the normalized form I/Z - (1 - 3c_l/2), never as I - (1 - 3c_l/2) Z with an absolute tolerance (vacuous near 0).
(iii) Gauge: the enstrophy Z = integral |Omega|^2 (with the analytic exterior) scales as L^3 under U_L(y) = L U(y/L)
    and is an admissible 6.1 alternative dilation gauge, Z = Z_* > 0 imposed exactly; it excludes U = 0, which a
    penalized F-gauge row does not. Exactly one dilation gauge (Z or F, never both); integral |F|^2 monitored and
    reported in the F-gauge.
(iv) Affine-core seeds. U = M y with tr M = 0 is an exact non-decaying profile for every c_l iff
    skew(M + M^2 + omega[J, M]) = 0, i.e. S_M Omega_M = Omega_M + omega J Omega_M (so eta = 1). Family:
    M = [[-1/2 + a, b - gamma, 0], [b + gamma, -1/2 - a, 0], [0, 0, 1]], gamma != 0, (a, b) != 0: Omega = 2 gamma e_3,
    non-axisymmetric, DW at the vortical W-zero has spectrum {1 + c_l, c_l - 1/2 +- sqrt(a^2 + b^2 - (gamma - omega)^2)}
    (one expanding, two contracting directions when the root is imaginary or below 1/2 - c_l in size; example
    c_l = 9/20, omega = 1/3, a = 1/4, b = 0, gamma = 1: strain (-1/4, -3/4, 1), DW 29/20, -1/20 +- i sqrt(55)/12).
    A strict local maximum of q at 0 without changing the first jet: add -eps |y|^2 J y with gamma eps > 0
    (D^2 q(0) = diag(-32, -32, -16) gamma eps). Localize through potentials, not by cutting off U:
    U_seed = curl{chi (A_M + A_delta) + (1 - chi) A_tail}, A_M = -(1/3) y x (M y), A_delta = -(1/5) y x delta U,
    A_tail the twisted tail potentials of 3.6; recompute the full-space pressure (the affine quadratic pressure is not
    admissible). Enstrophy budget: a core with eta near 1 needs a low-stretching shoulder with Z_shoulder/Z_core
    about (1 - k_Z)/k_Z in (1.5, 3), k_Z = 1 - 3c_l/2; a compactly supported pure-swirl field f(rho, z) e_phi in a gap
    has Omega.S Omega = 0 pointwise and adjusts Sigma_Z to 1 exactly with amplitude d^2 = (I_0/k_Z - Z_0)/Z(V) when
    I_0 > k_Z Z_0. These seeds are not claimed to satisfy the global backward-dynamics conditions of 2.8(e), (g).
(v) Pseudo-time (dynamic rescaling) only as a short preconditioner before Newton/LM. Facts: with Z = Z_* the
    dilation rate is c_l = (2/3)(1 - I/Z) (a weak field gives c_l near 2/3, outside the range); in finite pseudo-time
    the leading tail exponent and twist cannot change (only amplitude and rotation of F), so the flow keeps a fixed
    reference alpha and omega/c_l, and infinity is characteristic (no boundary data); while sup lambda_max(S) <= eps < 1,
    max|Omega| decays at rate at least 1 - eps, so relaxation does not create stretching; U = 0 is linearly
    attracting in sup|U|, sup|DU| and the vorticity L^2 norm and neutral in sup r^alpha |U|. GPU budget: a pilot of at
    most one GPU for 4 h that measures the right-hand-side time and the stable step before any longer run.
(vi) Shell normalization of the training objective (v1.15, 2026-10-24T23:32:08Z; astra steadycore1, d29, d30). Each normalization
    has a known escape. "nl" (divide by RMS T4 + RMS T5): core inflation, observed in both routes. all5 / all5far
    (five-term sum): large cancelling T4, T5 in a near-steady core still dominate the core denominators (d29). An
    absolute residual with fixed scales from the tail gauge, a_k = (1 + r_k)^(2 alpha + 1) RMS_k(R_u): no reward for
    inflation, but U -> 0 in the core lowers it, which is the weak-collapse basin of v1.2. The split denominator
    min(A_k, B_k) (A_k, B_k as in 7.2) resists both: inflating a cancelling pair leaves A_k, and shrinking the core by
    eps raises the ratio like 1/eps wherever L != 0. It is still not coercive: T2 and T3 can be large and cancel on
    helical modes, so the shell's A_k can be inflated, and ||F|| = 1 does not fix angular derivatives of F. Guidance:
    pilot "split" in both routes from the existing ladder states, labelled; a fixed-scale objective only together
    with the enstrophy gauge (iii), which excludes U = 0; report rho_sp, the 7.2 Gram data and the single-term
    ratios for every run whatever its objective. A state's acceptance never depends on the objective it was trained with.

## 11b. Gates and deliverable ownership

Gate I.4 (2026-10-25T23:09Z), evaluated by the lead from NUM_REPORT.md, the campaign ledger and VERIFY_REPORT.md:
  G1 tests T01-T12 pass in the primary code (starred ones also in the independent code); G2 the independent route
  has run its own random starts (not transferred states); G3 the sweep is reproducible from a config and ledger
  (each start: seed, parameters, basis level, optimizer, wall time, GPU, final diagnostics vector of 7.2-7.7 on
  holdout, failure reason); G4 a ranked shortlist by the 7.3 key with the 7.3b ordering (v1.20) and at least three structurally different
  branches if they exist (different c_l/omega regions, helicity distribution, dominant m, core shape), each with its
  full residual vector and resource cost. A Stage I candidate is only a discovery lead: N1-N6 not failed, measurable
  vorticity and non-axisymmetric content, no core or tail escape. If no state reaches Tier S: diagnose (parameter
  trapping, gauge or normalization errors, pressure truncation, missing radial channels or modes, conditioning,
  aliasing) and move part of Stage II to corrected search and odd m.
Gate II.4 (2026-10-27T17:09Z): either a small set of Tier R candidates with independently checked pressure, or a
  failure map: for each branch, residual versus level, which diagnostic stalls (core, far shells, rho_nl, pressure,
  origin, axis), parameter drift, and the tested remedies (bases, primal versus curl, odd m, continuation).
Deliverables (prompt section 8). Lead: FINAL_REPORT.md, MATHEMATICAL_FORMULATION.md, FAR_FIELD_AND_ORIGIN_AUDIT.md.
  Numerics: START_HERE.md, RUNBOOK.md, NUMERICAL_METHODS.md, PARAMETER_SWEEP.csv, CANDIDATE_LEADERBOARD.csv,
  FAILURE_ANALYSIS.md, environment lock and hardware inventory, tested launch/status/resume/validate scripts
  (single-command validation of the best candidate without retraining, single-command recovery, both tested from a
  clean process), candidate data, immutable accepted checkpoints, integrity manifest with hashes, plots listed in
  prompt section 8. Verifier: INDEPENDENT_VALIDATION.md (and VERIFY_REPORT.md), its own sweep records.

## 11c. Floor diagnosis (v1.9, registered 2026-10-24T21:57Z, before any result of these tests; steering only)

Applies while the Stage II allocation rule (reports/gate_I4_checklist.md, registered 21:19Z) is in its floor branch
for a route. Nothing here changes section 8. Notation: rho_f^max is the 7.2 shell maximum of the forced residual
R_u[U] - f, normalized by the term sum of the target U_m; "holdout" as in section 8.
(V1) In-span optimization test. U_m = a saved state of the route at level d, f = R_u[U_m] with the 5.1 pressure;
  solve R_u[U] = f in the same level-d space, objective, gauge and iteration budget as the unforced run, from the
  exactly embedded level d-2 state and from two random starts. Optimizer adequate in that space: rho_f^max <= 1e-4 on
  holdout from at least one start, recorded with the start. Optimizer-limited: rho_f^max >= 1e-2 from every start
  (it cannot reach a point known to lie in the space). Otherwise inconclusive.
(V2) Core-scale test. Same protocol and level at basis scales r_0/2 and 2 r_0. Representational at that level:
  best holdout rho_u^max changes by a factor >= 1.5 between the three scales; insensitive: all three within a factor
  1.15; otherwise inconclusive.
(V3) Parameters and class. Same protocol at the registered pairs (c_l, omega) = (0.42, 0.3), (0.48, 0.3), (0.45, 1)
  and in the all-m class. "The floor moves with (c_l, omega)" means the best holdout rho_u^max ranges over a factor
  >= 1.5. Reported with the shells of the maxima; no inference about existence by itself.
(N1) Cross-representation test. The other route's best saved state, fitted into this route's representation by field
  least squares on a volume grid (tail constraints kept; labelled transferred), at its levels. Can represent: the
  fitted field's own holdout rho_u^max <= 1.5 times the source state's value at some level; cannot represent near the
  maxima: >= 3 times at the highest level; otherwise inconclusive. A fitted state is a warm start, never evidence.
(V6) Optimization budget (v1.10, registered 2026-10-24T22:10Z, before any continuation result). A run is stationary if its
  objective fell by at most 1e-3 relative over the last 10 per cent of its iterations; otherwise it is
  budget-limited. A step ratio q of the allocation rule computed from a budget-limited state is reported as such.
  Continue each budget-limited level (retained optimizer state where available, else a fresh optimizer with a
  same-protocol control) until stationary or for at most 4 times its original budget, then re-evaluate on fresh
  holdout. Budget-explained: the continued holdout rho_u^max is lower by a factor >= 1.5 than the value used in q;
  budget-insensitive: within a factor 1.15; otherwise inconclusive. The allocation rule is then re-read with the
  continued values of all levels involved (thresholds unchanged), and the reading is labelled with the budgets used.
(V7) Sharpening and stretching share (v1.12, registered 2026-10-24T23:04:38Z; at registration the degree-2 value ell_Omega =
  0.0676 existed, and two partial values of the running degree-6 continuation had been written (2026-10-24T22:56:02Z
  and 23:03:59Z, verifier audit); no final continued value existed. Chronology corrected 2026-10-25T00:17Z; the earlier wording
  "only the degree-2 value exists" was false). ell_Omega := ||Omega||_L2 / ||curl Omega||_L2 on |y| <= 1024
  (F-gauge, unweighted); report it and the fixed-gauge finite-radius ratio ell_Omega / r_core (7.1). It is invariant
  under dilation only if the cutoff radius scales too: ell_[Omega_L](R) = L ell_Omega(R / L) (wording qualified
  2026-10-25T00:53Z after a verifier remark; no criterion changed). Along a degree ladder or a
  continuation whose rho_u^max falls by a factor >= 1.3: "sharpening" if ell_Omega / r_core falls by a factor >= 1.5
  from the first to the last state, "scale-stable" if it stays within a factor 1.15, otherwise inconclusive. Stretching
  share b := (R1 lower bound on rho_u^max of a shell, from |integral R_u . curl Omega| on that shell) / (measured rho_u^max
  of the same shell): "stretching-limited" if b >= 0.5 on the maximizing shell, "not stretching-limited" if b <= 0.1.
  Reading: sharpening together with Sigma_Z bounded away from 1 means the residual is being lowered by concentrating
  vorticity while the total stretching identity stays violated. This fits both an unresolved narrow core and a
  limit that is not a smooth profile; V2 and the manufactured narrow-core test (R4) separate the two. Scale-stable
  with rho_u^max falling and Sigma_Z moving toward 1 is the pattern expected on the way to a smooth profile.
  Reported only; no threshold of section 8 depends on V7, and no reading of V7 supports label D.
(V8) Identity-consistent ladder (v1.13, registered 2026-10-24T23:10:33Z; at registration the Sigma_Z-penalized degree-6 state of the
  independent route has only a TRAINING value, rho_u^max 0.0794 at Sigma_Z 0.99997, after 2200 iterations stopped at
  maximum_steps; its holdout is not known; degree 2 and 4 holdout values 0.13252 and 0.10720 are known). An exact
  profile with the decay of section 3 has Sigma_Z = 1 (7.8), so along a ladder converging to it Sigma_Z -> 1. The
  released family has Sigma_Z 0.15 / 0.22 / 0.35 at degrees 2 / 4 / 6, and its continuation lowers it (V7). The
  Sigma_Z-penalized family of the same route (|Sigma_Z - 1| <= 1e-3 at every level) is therefore read under the
  allocation rule beside the released family, with the same thresholds and the V6 budget labels: q_S = holdout
  rho_u^max at degree 6 / holdout rho_u^max at degree 4, on both shell families of 7.3a. The route's branch is the one
  given by the smaller of q and q_S (the rule's first bullet already takes the more favourable of two routes); both
  values, their budget status and the family used are reported. A step whose states fail the Tier S class condition
  e_F >= 1e-4 is reported and not used for a branch. Steering only; nothing in section 8 changes, and a branch read
  from either family says nothing about existence.
  Qualification (v1.15, verifier 23:16Z): Sigma_Z -> 1 along a ladder needs convergence of the global enstrophy and
  stretching integrals with nonzero limiting Z; local C^2 convergence alone does not give it. Also, Sigma_Z near 1
  makes the global signed integral of R_Omega.Omega small; it does not make the per-shell R1 stretching share b of V7
  small, so b is still reported for this family.
(V9) Core self-similar balance (v1.14, registered 2026-10-24T23:19:15Z; the released degree 2/4/6 values were known at registration:
  max over shells inside |y| < 1 of rho_lin = 0.73 / 0.73 / 0.79, d29; the continued D6 and the degree-6 Sigma_Z-penalized
  values were not). Along a ladder or continuation whose rho_u^max falls by a factor >= 1.3: "core-converging" if
  rho_sp^max (shells inside |y| < 1) also falls by >= 1.3; "denominator-driven" if it falls by less than 1.15 or rises;
  otherwise inconclusive. A denominator-driven decrease is reported as such wherever the rho_u decrease is quoted, and a
  step ratio q of the allocation rule computed on such a ladder is labelled with it. Steering only.
(V10) Local stationarity by Gauss-Newton (v1.18, registered 2026-10-25T01:23:08Z; thresholds are those of V6. Chronology: at
  registration the independent route's unforced GN continuation of its capped degree-6 state had finished training
  (objective 1.3348e-4 -> 1.1772e-4 over 400 GN steps, last-tenth decrease 4.9e-4 relative; training rho_u^max 0.0579
  -> 0.0576, not evidence), and a fresh pressure-order-18 holdout file of that state existed in the verifier's records
  (written 01:01Z) that the lead had not read; no other GN continuation of an unforced state existed). From a saved
  state, run the route's verified fixed-parameter GN or LM step in the same space, objective, gauge and constraints
  until the objective falls by at most 1e-3 relative over the last 10 per cent of steps (GN-stationary) or for 400
  steps. Locally floored: GN-stationary and fresh holdout rho_u^max within a factor 1.15 of the start state's fresh
  holdout on both shell families; locally optimizer-limited: lower by a factor >= 1.5 on either family; otherwise
  inconclusive. When GN-stationary states exist at two consecutive levels of a ladder, the allocation rule is re-read
  with their fresh holdouts (thresholds unchanged) and labelled GN-stationary; for those levels this reading replaces
  the budget-limited one of V6. Steering only. A local floor concerns one basin of one objective in one space; it is
  not a floor of the problem and says nothing about existence. "Locally floored" is an operational stopping label, not a
  proof that the state is a local minimum (qualified 01:36Z).
Combined reading (recorded at gate II.4 with the tests available then). Optimization failure is favoured if V1 is
optimizer-limited or V6 is budget-explained (v1.18: unless V10 reads locally floored at the same levels, in which case
the reading is that local descent from the saved states has stalled for this objective and space, and the global search is
unreliable; wording qualified 2026-10-25T01:36Z after the verifier's 01:29Z note: the operational label is not a
local-minimum certificate, since no Hessian test exists and a stalled step can reflect a shallow slope or ill-conditioning;
no threshold changed). An approximation limit of the representation is favoured if V1 passes and V2 is
representational, or N1 shows that one representation reaches the other's floor only at much higher cost. A floor of
the problem in the searched classes is favoured only if V1 passes, V2 is insensitive, both routes stall at comparable
values on the same shells, and the identity defects (Sigma_Z, ||R_Omega||/||Omega||, origin jets) stay bounded away
from zero along the ladder. Even then this is a numerical finding about finite classes and does not support label D,
which needs a proof (section 9).

## 12. Change log

- v0 2026-10-24T17:28Z: first version.
- v0.1 2026-10-24T17:33Z: 4.4 radial-channel requirement; 7.9 tests; 3.5 finite parts for all l >= 2; wording of 7.2.
  No threshold changed. (This line first carried the wrong stamp 17:40Z; the edit was made at 17:33Z.)
- v0.2 2026-10-24T17:37Z: verifier audit of v0 (its SPEC_AUDIT_v0.md, 17:33Z) applied: 2.6 qualified; 2.7 flux justification
  for bounded L^2 profiles; 3.5 finite parts subtract all divergent terms, resonance-regular tail form, avoid exact
  resonant grid points; 7.7 degenerate E_G rule; T04 invariant versus covariant quantities; T06 mirrored-history
  condition. d02 (far field) and d03 (Green, Taylor, resonances) all PASS. No threshold changed.
- v0.2+ 2026-10-24T17:38-17:44Z (no version number at the time): 7.8 ball-integral laws (conservation forms V,
  d04; consequences H, audit pending); section 11b gates and deliverable ownership. No threshold changed.
- v1 2026-10-24T17:52Z: independent audit astra specaudit1 (28 symbolic checks, exact mixed-resonance example)
  applied after the lead checked each claim: the exterior integral and the resonant finite-part constant
  a/(2l+1)^2 re-derived from the Green formula of 5.2; the mixed-resonance rate rule re-derived; astra's exact
  example re-run unchanged (derivations/astra_repro/mixed_resonance.log, MIXED NONZERO m RESONANCE VERIFIED).
  Changes: Bernoulli function renamed Be; order-1 divergence Taylor conditions and vertical Omega(0) (section 1);
  2.4 Z-image test by gauge-orbit distance; 2.6 L2 is cited only, no result depends on it; 3.5 rewritten (formal
  classification, mixed terms, complete finite parts with oscillatory and log subtractions, resonant convention,
  resonance rule nu = 0 and p = l+1 for any m, every rational c_l resonant at order n, endpoint coincidences not
  automatically logs, practical rule for 0.43 and 0.45); 5.2 general exterior integral; 7.2 relative shell flag,
  pi_nl, A_u, A_Om, float64 cancellation rule; 7.4 energy fraction e_k; 7.6 floored Taylor ratios; 7.7 E_H, E_D;
  7.10 comparison norm; 7.11 exterior closure tests X1-X5; section 8 holdout versus final-test points, nested
  tiers, Tier S adds e_core, e_F >= 1e-4, Tier R adds non-collapse and X1, X4, Tier A adds A_u <= 1e-5,
  A_Om <= 1e-4, pi_nl <= 1e-3, rho_Om_nl <= 1e-4, E_H, E_D, X1-X5, omitted-term bounds and precision agreement;
  Tier A divergence allowance for non-solenoidal representations tightened from 1e-7 to 1e-8 (it was looser than
  Tier S). No v0 threshold was relaxed. Section 10 exchange grid enlarged and declared not an acceptance grid.
- v1.1 2026-10-24T18:07Z (lead): ADDITIONS ONLY, no threshold in section 8 changed. 2.8 rigorous partial results from astra
  obstruction1 (decay dichotomy, direct axisymmetric exclusion, W-dynamics, rotating Bernoulli torque and exact
  non-decaying examples), lead-reviewed (derivations/obstruction_notes.md) and symbolically re-checked
  (derivations/d06_obstruction_checks.py, d06.log, 16/16 PASS); verifier check requested. 4.4 rate bookkeeping
  for regularized or compactified bases. 7.8 global weighted identities (E), (V), (O), (Hel) with residual
  accounting (derivations/d05_virial.py, d05b_weighted.py, logs all PASS).
- v1.2 2026-10-24T18:25Z (lead): no threshold in section 8 changed. 2.8(a)-(c) and the 7.8 identities marked confirmed by the
  independent route (SPEC_AUDIT_v1_1.md), with its two qualifications written into 2.8(a) (F is a tail-class
  assumption; no statement about optimizer sequences) and 2.8(d) (only H_0 + a ell and universal strict identities
  are refuted). New 2.8(e) backward stretching and 2.8(f) dilation-invariant nontriviality facts. 7.8 additions from
  astra integrallaws1 after exact re-checks (derivations/d08_integrallaws_checks.py, 17/17 PASS): (V) reclassified
  as a pressure-consistency identity, total stretching (Z0) and the weighted family, ratios Sigma_Z and Sigma_E,
  conformal relation (K), next-order angular momentum, kinematic momentum, residual error formulas. 11 search
  guidance for the weak axisymmetric collapse observed in Stage I. Snapshot of v1.1: derivations/SPEC_v1.1_snapshot.md.
- v1.3 2026-10-24T18:41Z (lead; qualifications added 18:44Z): ADDITIONS ONLY, no threshold in section 8 changed. 2.1 the stretching identity holds at
  every critical point of |Omega|^2, and the self-similar Kelvin form [V, d10]; 2.8(g) Kelvin, vortex lines and
  invariant-measure identities [H]; 2.8(h) parameter count from astra paramcount1 (lead checks d09, 11/11 PASS);
  7.5 N2 extended to further local maxima; 11 compressed-maximum basin remedy and Stage II free-parameter and
  branch diagnostics; 7.8 two convergence qualifications from the verifier's v1.2 audit (range of m in the weighted
  family; residual moment decay is a necessary, not sufficient, threshold). Snapshot of v1.2:
  derivations/SPEC_v1.2_snapshot.md.
- v1.4 2026-10-24T18:49Z (lead): ADDITIONS ONLY, no threshold changed. 2.8(e) strengthenings from astra stretch1
  (lead review d11, [H]); new 7.12 residual-corrected orbit averages (O1)-(O4) as a diagnostic; the d07 transport
  defect is limited to short times. Snapshot of v1.3: derivations/SPEC_v1.3_snapshot.md.
  Status annotations 18:54Z (no content or threshold change): 2.1 critical-point identity and 2.8(h) zero of W with the
  eigenvalue condition marked CONFIRMED by the independent route (18:52Z).
  Status annotations 19:03Z (no threshold change): 2.8(e) v1.4 strengthenings and 2.8(g) marked CONFIRMED (verifier
  18:58Z, SPEC_AUDIT_v1_4) with the qualifications stated there; 7.12 (O1)-(O4) CONFIRMED (O1 where Omega != 0).
- v1.5 2026-10-24T19:06Z (lead): ADDITIONS ONLY, no threshold changed. Section 11 discovery devices (i)-(v) from astra strategy1,
  lead-checked (d12, 15/15 PASS); the v1.3 pointwise near-critical penalty is withdrawn (training guidance only).
  Snapshot of v1.4: derivations/SPEC_v1.4_snapshot.md.
- v1.24 2026-10-25T09:54:00Z (lead): ADDITION ONLY, no threshold changed. 7.8: first far coefficients; the helicity ratio
  K_H(carried)/K_H(required) is reported beside the energy ratio, and the exterior helicity estimate gains its second
  term (FINAL_REPORT section 2, item 34; derivations/d78, d81). Snapshot of v1.23: derivations/SPEC_v1.23_snapshot.md.
- v1.23 2026-10-25T08:14:16Z (lead): CLARIFICATION ONLY, no threshold changed. 6.2: after every accepted step the real pivot must be
  positive; a negative real pivot is mapped back by the logged discrete rotation C(pi/m*) or rotated at commit and
  export (independent-route accepted-step gauge diagnosis 07:49Z; review d75). Snapshot of v1.22:
  derivations/SPEC_v1.22_snapshot.md.
- v1.22 2026-10-25T02:49:47Z (lead): ADDITION ONLY, no threshold changed. Section 8: tail-generation defect tau_F and backward defect
  delta_G (ray integrals of the residual through the bounded inverse G of L), reported without threshold, with two
  evaluation routes and a node-doubling rule (astra formul1, audited in derivations/d46_backward_formulation_audit.md).
  2026-10-25T02:53:01Z: (c) translated-ball a_max weight convention (centre weight registered, upper-radius weight reported, v1.17
  (a) required under both; stricter reading of an ambiguity). Snapshot of v1.21: derivations/SPEC_v1.21_snapshot.md.
- v1.21 2026-10-25T02:23:11Z (lead): one TIGHTENING, no threshold relaxed. Section 8: core-resolution rule (a_eff, core-resolved
  inner shells and balls at the vorticity maximum for sigma_u^max and a_max, quadrature and level stability, "core
  unresolved" fails every tier), near-edge label within 0.02 of either edge, E_ren and the ball energy identity
  reported (astra edge1, audited in derivations/d43). No state meets Tier S at registration. Snapshot of v1.20:
  derivations/SPEC_v1.20_snapshot.md.
- v1.20 2026-10-25T01:44:56Z (lead): ORDERING TIGHTENING, no acceptance threshold changed. 7.3b: a state ranks ahead of another only
  if it has the lower holdout rho_u^max on both families and its sigma_u^max, sigma_Om and a_max are each at most 10 per
  cent larger; otherwise not ordered. Chronology and reason in 7.3b. Snapshot of v1.19: derivations/SPEC_v1.19_snapshot.md.
- Wording qualification 2026-10-25T01:36:41Z (lead, no version, no threshold changed): 11c V10 and the combined reading state that
  "locally floored" is an operational label, not a local-minimum certificate (verifier note 2026-10-25T01:29Z).
- v1.19 2026-10-25T01:28:56Z (lead): one TIGHTENING, no threshold relaxed. Section 8: the single-term ratios of 7.2 become
  requirements in Tiers S, R and A (sigma_u^max over all shells of both families and |y| < 1: 1e-1 / 1e-3 / 1e-5;
  sigma_Om = ||R_Omega||_2/||Omega||_2: 1e-1 / 1e-3 / 1e-4), because they resist the continuum escapes (verifier
  proof 2026-10-25T01:24Z, d39 section 6). The v1.17 reason sentence is qualified to name the ratios it covers. No
  state meets Tier S at registration (values in section 8). Snapshot of v1.18: derivations/SPEC_v1.18_snapshot.md.
- v1.18 2026-10-25T01:23:08Z (lead): ADDITION ONLY, no threshold changed. 11c (V10) Gauss-Newton local stationarity reading
  (V6 thresholds, chronology stated there) and its effect on the combined reading and the allocation re-read.
  Snapshot of v1.17: derivations/SPEC_v1.17_snapshot.md.
- v1.17 2026-10-25T01:16:37Z (lead): one TIGHTENING, no threshold relaxed. Section 8: for Tier R and Tier A, the
  fixed-gauge absolute residual a_max must fall by >= 10 over L1 to L3, gauge-aligned field sizes may grow by at most
  10 per cent and shell peak factors by at most 2x from L2 to L3 (astra noncoer1, audited in derivations/d39: no 7.2
  ratio is a proximity certificate; fixed and shrinking compact steady Euler copies). No state meets Tier S at
  registration. Snapshot of v1.16: derivations/SPEC_v1.16_snapshot.md.
- v1.16 2026-10-24T23:41:53Z (lead): ADDITIONS ONLY, no threshold changed. 7.8: local L2 form of the vorticity bound on centred balls
  and the ball ratios to report (verifier proof 2026-10-24T23:39Z). 7.2: origin-ball characteristic radius r_k = 0 in the
  denominator flags (for r_max <= 1/32 at c_l = 0.45 the convention changes the momentum factor by at most 1.112 and the
  vorticity factor by at most 1.147; wording corrected 2026-10-24T23:57Z after verifier review). Snapshot of v1.15:
  derivations/SPEC_v1.15_snapshot.md.
- v1.15 2026-10-24T23:32:08Z (lead): ADDITIONS and one TIGHTENING; no threshold relaxed. Section 8: rho_sp^max <= 1e-1 (S),
  1e-3 (R), 1e-5 (A) and rho_Om_sp^max <= 1e-4 (A), with the 7.2 denominator flags (astra steadycore1; registered when no
  state of either route meets Tier S, values stated there). 7.2: Gram data of L and N per shell, single-term ratios,
  denominator flags. 7.8: Sigma_Z residual lower bound (d30). V8 qualification (verifier 23:16Z). 11 device (vi):
  objective normalizations and their escapes. Corrections recorded in d29 (addendum): the nonlinear-to-linear range
  is 8.5 to 84, and the independent ladder was trained with the nonlinear denominator, not the five-term one.
  Snapshot of v1.14: derivations/SPEC_v1.14_snapshot.md.
- v1.14 2026-10-24T23:19:15Z (lead): ADDITION ONLY, no threshold changed. 7.2 self-similar balance ratios rho_lin, rho_sp (reported);
  11c item V9 (core self-similar balance; registered after the released ladder values were known, stated in V9).
  Finding behind it: derivations/d29 (cores of all ladder states are near-steady Euler flows). Snapshot of v1.13:
  derivations/SPEC_v1.13_snapshot.md.
- v1.13 2026-10-24T23:10:33Z (lead): ADDITION ONLY, no threshold changed. 11c item V8 (identity-consistent ladder): the
  Sigma_Z-penalized family of the independent route is read under the Stage II allocation rule beside the released
  family; branch from the smaller of the two step ratios; registered before the degree-6 penalized holdout exists (its
  training value 0.0794 was known and is stated in V8). Snapshot of v1.12: derivations/SPEC_v1.12_snapshot.md.
- v1.12 2026-10-24T23:04:38Z (lead): ADDITION ONLY, no threshold changed. 11c item V7 (sharpening via ell_Omega / r_core and stretching
  share b from the R1 bound), registered before any final continued ell_Omega value (two partial continued values existed;
  wording corrected 2026-10-25T00:17Z). Snapshot of v1.11:
  derivations/SPEC_v1.11_snapshot.md.
- v1.11 2026-10-24T22:40Z (lead): ADDITION ONLY, tightening; no threshold relaxed. 7.3a half-offset shell family:
  ordering claims and section 8 thresholds must hold on both families. Registered after the lead's grid check of the
  primary d6t_L6 export. No state is near any threshold, so no acceptance outcome changes. Snapshot of v1.10:
  derivations/SPEC_v1.10_snapshot.md.
- v1.10 2026-10-24T22:10Z (lead): ADDITION ONLY, no threshold changed. 11c item V6 (stationarity definition, continuation protocol,
  budget-explained / budget-insensitive criteria) registered after the verifier's record that the degree-4 and degree-6
  released runs stopped at their budgets with last-10% objective decreases 3.4e-2 and 4.7e-2, before any continuation result.
- v1.9 2026-10-24T21:57Z (lead): ADDITIONS ONLY, no threshold changed. 11c floor-diagnosis tests V1-V3, N1 with interpretation
  criteria registered before any result (allocation rule read in the floor branch for the independent route, lead
  note 21:55:39Z). Snapshot of v1.8: derivations/SPEC_v1.8_snapshot.md.
- v1.8 2026-10-24T20:16Z (lead): ADDITIONS ONLY, no threshold changed. 2.8(j) zero-free invariant sets [A] and
  7.14 exact checks along orbits and on invariant sets (derivations/d15_alphalim_review.md). Snapshot of v1.7:
  derivations/SPEC_v1.7_snapshot.md.
  Status annotation 20:37Z (no content or threshold change): 2.8(e) signed form lead-checked as algebra (d15 (b)),
  awaiting independent check. Status 20:47Z (no threshold change): 2.8(e) signed form and 2.8(j) CONFIRMED by the
  independent route (20:38Z); 7.14(a) wording distinguishes beta_0 and beta_1 for approximate states.
  Addition 21:03Z (no threshold change): 4.4 angular closure of the rate 2alpha+1 channels (d18).
- v1.7 2026-10-24T19:25Z (lead): ADDITIONS ONLY, no threshold changed. 7.13(d) trapping radius and localized
  strength, 7.13(e) core non-axisymmetry ratios (derivations/d14_quantrot_review.md). Wording per the independent
  CIV audit (19:22Z): 2.8(i)(b) states decay explicitly; C_2 = 2(162/pi)^(1/5) = 4.40051 exactly; 7.13(c) caveat.
  Wording 2026-10-24T20:02Z (no content or threshold change), per the independent audit of 19:43Z: 7.13(d) the
  strain conclusion is stated for alpha-limit sets of vortical points; sampled R_trap is an estimate.
- v1.6 2026-10-24T19:17Z (lead): ADDITIONS ONLY, no threshold changed. 2.8(i) outgoing conditions and the CIV bounds
  with rotation [H], attributions to arXiv:2602.17570; 7.13 outgoing and strength diagnostics.
  Snapshot of v1.5: derivations/SPEC_v1.5_snapshot.md.
