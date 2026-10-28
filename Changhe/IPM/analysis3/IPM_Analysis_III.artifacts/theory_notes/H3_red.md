Proposition H3-red (reduction of (H3) on X_s to one symbolic estimate; DERIVED, submitted for checking). Notation
of V126 (X_s, b, p, chi, the cofactor u = chi h/(b p), the sector |cos theta| < eps_0 where chi = 1), of V129 (the
domain D_H = {h in X_s : T_R h in X_s} and its graph-dense core) and of Lemma H-spec (S = T_R + C_R, lambda_*). The
cylinder field is W~ = (q, vartheta), so V.grad = q d_t + vartheta d_theta and T_R = V.grad - 1; beta(t) := (log b)'(t),
so beta = 3 + delta = 24/5 for t <= -1 and beta = gamma = -1/2 for t >= 1. For 0 < eps <= 1, X_{s-eps} is defined as
X_s with the orders s(.) - eps and sigma - eps, the same weights and the same parity and trace conditions (closed,
since sigma - eps > 1/2). The low norm is the doubly factored weighted L^2 norm
     N_0(h) := || h / (b(t) cos^4 theta) ||_{L^2(C, dt dtheta)},
that is, near the origin N_0(h)^2 = int |h|^2 |x|^(-8) r^(-18/5) dX; it is the plain L^2 norm of v = h/b away from
the vertical axis and the L^2 norm of sin(theta) u / cos^2(theta), the cofactor divided once more by cos^2 theta, in
the sector.
Hypothesis (Hs_eps) (the symbolic estimate; OPEN). For some eps in (0, 1] there is C_s with
     ||h||_{X_s} <= C_s ( ||(S - lambda) h||_{X_s} + ||h||_{X_{s-eps}} )   for all h in D_H, 0 <= lambda <= lambda_*.
Claim. (Hs_eps) implies (H3) of Lemma H-spec on X_s, with the Banach space W = X_{s-eps} (+) N_0-completion and an
explicit compact K. With (H1) and (J1) to (J3) (V126) and (H2) (V129, with the order of V130 or V132), Lemma H-spec
and Corollary H-spec then give: S_1 : D_H -> X_s and L_red : X_H^full -> Y_H^full are Fredholm of index 0.
No normal-family inversion at either end and no uniformity in the radial frequency is used.

Lemma A (Hardy, interpolation, compactness; elementary). (i) N_0(h) <= C_H ||h||_{X_s} on X_s. (ii) For every
eta > 0 there is C_eta with ||g||_{X_{s-eps}} <= eta ||g||_{X_s} + C_eta N_0(g) on X_s. (iii) For psi smooth in t
with compact support, h -> psi h is compact from X_s to X_{s-eps} and from X_s to the N_0-completion.
Proof. (i) Where |cos theta| >= eps_0, cos^(-4) theta is bounded and ||v||_{L^2} <= ||v||_{H^(s(.))}. On
|cos theta| < eps_0, v/cos^4 theta = sin(theta) u/cos^2 theta, and u(t, pi/2) = 0 (trace condition) and
d_theta u(t, pi/2) = 0 (evenness, sigma > 3/2). The one-dimensional Hardy inequality int_0^a |f/phi|^2 <= 4 int_0^a |f'|^2
for f(0) = 0, applied to d_phi u and then to u, gives ||u/phi^2||_{L^2} <= 16^(1/2) ||d_phi^2 u||_{L^2} for a.e. t,
phi = pi/2 - theta, and cos theta is comparable to phi there; integrate in t. (ii) In the dyadic realization,
||2^(j(s(.) - eps)) Delta_j v|| <= 2^(-j eps) ||2^(j s(.)) Delta_j v|| <= eta ||2^(j s(.)) Delta_j v|| when
2^(j eps) >= 1/eta, and each of the finitely many remaining blocks is bounded by 2^(j sigma) ||v||_{L^2}; the same
for u in H^(sigma - eps). Finally ||v||_{L^2} <= N_0(h), since cos^(-4) >= 1, and ||u||_{L^2} <= C N_0(h), since
|chi/p| <= C cos^(-4) theta (|sin theta| is bounded below on supp chi). (iii) Rellich on a bounded cylinder strip for
the variable order (the order gap is eps > 0); for the N_0 part, Taylor's formula with integral remainder,
u/phi^2 = int_0^1 (1 - tau) (d_phi^2 u)(t, tau phi) dtau, bounds psi u/phi^2 in H^1 of the strip by ||u||_{H^3}, and
H^1 of a bounded strip embeds compactly in L^2. QED.

Lemma B (exact energy identity in N_0; DERIVED, elementary). Put
     kappa(t, theta) := 1 + c_l - (1 + beta(t)) q(t, theta) + 4 vartheta(t, theta) tan theta.
For every g in D_H,
     - Re <T_R g, g>_{N_0} = int_C kappa |g/(b cos^4 theta)|^2 dt dtheta.
Proof. With omega := b^(-2) cos^(-8) theta, integration by parts on C gives - Re <(q d_t + vartheta d_theta - 1) g, g>_omega
= int [1 + (1/2) div_C W~ + (1/2) W~.grad log omega] |g|^2 omega. Since div V = 2 c_l and dX = e^(2t) dt dtheta,
div_C W~ = d_t q + d_theta vartheta = 2 c_l - 2 q exactly; and (1/2) W~.grad log omega = - beta q + 4 vartheta tan theta.
For g in the core of V129 there is no boundary term at the axis: near theta = pi/2, |g|^2 omega = sin^2(theta) |u|^2
/ cos^4 theta is bounded (u vanishes to second order) and vartheta = O(cos theta), because the vertical axis is
invariant (V_1 is odd in x). kappa is bounded (vartheta tan theta = sin theta (vartheta / cos theta) and
|vartheta / cos theta| <= sup |d_theta vartheta|), so both sides are continuous in the graph norm of D_H by Lemma A(i),
and the identity extends from the core to D_H. QED.

Lemma C (positive energy at both ends; DERIVED). As t -> -infinity, kappa -> kappa_-(theta) uniformly, where
     kappa_-(theta) = 1 + c_l - (4 + delta) q_0 + 4 Sigma sin^2 theta
                    = (3 Sigma/2 + delta A) cos^2 theta + (3 Sigma/2 - delta D) sin^2 theta
                    = 65.44956889 cos^2 theta + 8.83565270 sin^2 theta,
and as t -> +infinity, kappa -> 1 + c_l/2 = m_inf = 3.78768131 uniformly. Hence for every c_0 < m_inf there is T_0
with kappa >= c_0 on |t| >= T_0 - 1, and for g in D_H supported in |t| >= T_0 - 1 and Re lambda >= 0,
     (c_0 + Re lambda) N_0(g) <= N_0((T_R - lambda) g).
Proof. At the origin q -> q_0 = -A cos^2 theta + D sin^2 theta and vartheta -> vartheta_0 = Sigma sin theta cos theta
uniformly (continuity of the lifted field on the compactified cylinder, V130 (proof 128)); at infinity q -> c_l and
vartheta -> 0 uniformly (V130: rdot/r = ell + O(r^(k-1)), thetadot = O(r^(k-1))). The second cylinder derivatives of
q and vartheta are bounded (V129), so by the interpolation inequality ||f'||_inf <= C ||f||_inf^(1/2) (||f||_inf +
||f''||_inf)^(1/2) on the circle, d_theta vartheta also converges uniformly, to d_theta vartheta_0 and to 0; hence
vartheta tan theta -> Sigma sin^2 theta and -> 0 uniformly. The closed forms follow from 1 + c_l = 1 + (D - A)/2,
D = 2A + 1 and Sigma = 3A + 1 (both coefficients are 1.5 + 6.3 A and 0.9 A - 0.3). The estimate follows from Lemma B:
(c_0 + Re lambda) N_0(g)^2 <= Re <(lambda - T_R) g, g>_{N_0} <= N_0((T_R - lambda) g) N_0(g). QED.
Why the double factor. With the weight b^(-2) |cos theta|^(-2a) on v the vertical value of the limit energy is
1 + c_l - (4 + delta) D + a Sigma = -116.973 + a Sigma, positive iff a > 3.71908 (= 2 + the vertical threshold
1.71908 of V086), while N_0 <= C ||.||_{X_s} needs a < 9/2 (v vanishes like cos^4 theta at the axis). a = 0 (the bulk
weight) gives -116.97 and a = 2 (the single cofactor) gives -54.07, the value of item 1 of H3-var; a = 4 gives 8.8357. The
horizontal value 65.45 does not depend on a. The radial exponents must be those of X_s, because Lemma A(ii) needs
N_0 to dominate the low-frequency part of X_s at both ends.

Lemma D (coupling tails; DERIVED from (8) of V126). Let psi_E^T(t) be smooth, 0 for |t| <= T - 1 and 1 for |t| >= T,
with derivatives bounded independently of T. Then N_0(psi_E^T C_R h) <= eps(T) ||h||_{X_s} with
eps(T) <= C (e^(-(2 - delta) T/2) + e^(-(1 - k) T/2)) -> 0.
Proof. In the annular matrix bounds (8) of V126 for C_ren/b and, near the axis, C_ren/(b p), restrict the output to
radii r <= e^(-T). The row sums are O(e^(-2T)) for s <= r, O(r^(2 - delta)) for r <= s <= 1 and O(r^(2 - delta)) for
s >= 1, so O(e^(-(2 - delta) T)); the column sums stay bounded. For outputs r >= e^T the rows are O(r^(k-1)) and
O(r^(k - 4 - gamma)), so O(e^(-(1 - k) T)); the strain cutoff is supported in a fixed annulus. Schur's test gives
||psi_E^T C_ren h/b||_{H^(s(.))} + ||psi_E^T chi C_ren h/(b p)||_{H^sigma} <= C eps(T) ||h||_{X_s}. Now
C_R h/(b p) = C_ren h/(b p) - Gamma_C[h]/a, and Gamma_C[h]/a is the axis trace of C_ren h/(b p) (the exact axis
identity used in V126), so ||psi_E^T Gamma_C[h]/a||_{H^2(R)} <= C ||psi~ chi C_ren h/(b p)||_{H^(5/2)}, psi~ a slightly
larger cutoff of the same type. C_R h/(b p) is even with zero trace, so the Hardy step of Lemma A(i) bounds the sector
part of N_0(psi_E^T C_R h) by its H^2 norm; away from the axis N_0 is the L^2 norm of v. QED. (The X_s-norm version of
this tail bound would need the H^sigma norm of the jet coefficient on the ends, which the trace does not give; it is
not needed here.)

Proof of the claim. Put psi_m := 1 - psi_E^T. By (Hs_eps), the triangle inequality, Lemma A(ii) with eta and the
uniform multiplier bound ||psi_E^T||_{X_s -> X_s} <= C_2,
     ||h||_{X_s} <= C_s ||(S - lambda) h|| + C_s ||psi_m h||_{X_{s-eps}} + C_s eta C_2 ||h||_{X_s} + C_s C_eta N_0(psi_E^T h).
Since (T_R - lambda) psi_E^T h = psi_E^T (S - lambda) h - psi_E^T C_R h + q (psi_E^T)' h, Lemma C (T >= T_0), Lemma A(i)
and Lemma D give
     N_0(psi_E^T h) <= c_0^(-1) [ C_H ||(S - lambda) h||_{X_s} + eps(T) ||h||_{X_s} + N_0(q (psi_E^T)' h) ].
Choose eta with C_s eta C_2 <= 1/4, then T >= T_0 with C_s C_eta c_0^(-1) eps(T) <= 1/4. Then
     ||h||_{X_s} <= C_1 ||(S - lambda) h||_{X_s} + ||K h||_W,   C_1 = 2 C_s (1 + C_eta C_H / c_0),
     K h := (2 C_s psi_m h, 2 C_s C_eta c_0^(-1) q (psi_E^T)' h) in X_{s-eps} (+) N_0,
and K is compact by Lemma A(iii) (both cutoffs have compact t-support; q is a bounded smooth multiplier). The
constants do not depend on lambda in [0, lambda_*]. QED.

Remarks. (1) The ends need neither the normal family nor its uniformity in xi (item 2 of H3-var, V131 and the
uniform statement under check): the identity of Lemma B is exact for the actual field, so the first-order
coefficient error (V - V_0).grad, which is not small in the graph norm (a standard counterexample: Q_0 = d_t - 1,
R_eps = eps d_theta, u_n = n^(-s) chi(t) e^(i n theta)), never appears; only the zeroth-order quantities q and
vartheta tan theta enter, through their uniform limits. The alternative route through the uniform exact origin normal inverse (V133)
and the stable principal end inverses at the vertical, horizontal and far ends (V135, V137) gives full-order end
estimates for the principal transport; it needs in addition the angular transitions at the origin end and the
coupling in the X_s norm. Lemmas B to D need neither, but they give only the low-order (N_0) end bound and leave the
whole high-frequency estimate to (Hs_eps). (2) The essential growth bound of
the semigroup is at least delta D + Sigma/2 = 54.07 (a computation with explicit escaping packets, not yet
checked, consistent with V128). This does not contradict (H3): the packets are elliptic, and (H3) is a real-parameter
Fredholm estimate, not a semigroup bound. (3) (Hs_eps) is the whole remaining analytic content of (H3). A formulation
without a microlocal partition: with the escape function Lambda of V130 and the order of V130 or V132
there are N, L_0 and mu > 0 with m + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu on the compactified cosphere bundle,
where m is the energy symbol (V086 (1), including the log term (W~.grad s) log|xi| >= 0 and the coupling symbol);
quantizing this inequality and bounding L_0 ||W~.grad h||^2_{X_{s-1}} through the equation gives (Hs_eps). What must
be proved is the finite-regularity quantization: for the W^(7,inf) transport coefficients, the coupling with its
H^(51/8) coefficients (surplus 1/8 over sigma, so eps <= 1/32 is a plausible target), the variable order and the
two-component norm with the cofactor division, the conjugation, positive-quantization and elliptic remainders are
bounded by a strictly lower X norm, uniformly under t-translations and for lambda in [0, lambda_*]. The bounded
commutator estimate of V129 does not give this (its constant is not compared with the margin m_x = 0.9726).
(4) Margins entering (Hs_eps) on the characteristic set {W~.nu = 0} near the critical elements: at +-P (all
covectors) min(b_P - s mu_P, b_P + g_P - s A_P) at s = 41/20, which is 4.52536 (slow branch; the fast branch is
15.51587), from the formula of V011 with the exact source parameters (A_P = 10.150725..., mu_P = 0.99999998,
g_P = 29.749491; CONFIRMED with the sharp interval (4.52536265678952, 4.52536265685856) and a sharpness packet, V134); the earlier value "about
14.8" in remark (5) of Lemma H-spec and item 4 of H3-var was wrong; at S_x m_x = 0.97261 (bulk, angular covector); at
S_y 142.507 (cofactor) and -116.973 + 25/4 Sigma = 79.603 (bulk component at order 25/4); at infinity 3.78768. Near
S_y the negative-energy covectors are elliptic, but the partition must overlap: m_y = 0 at |nu_theta| = 0.524454 and
m_y(1/2) = -4.9247, so cones |nu_theta| > 0.53 (coercive, m_y >= 1.1495) and |nu_theta| < 0.54 (elliptic,
|W~.nu| > 17.91 on |pi/2 - theta| <= 10^(-3) for the exact origin field) are used, not a partition at 1/2.
