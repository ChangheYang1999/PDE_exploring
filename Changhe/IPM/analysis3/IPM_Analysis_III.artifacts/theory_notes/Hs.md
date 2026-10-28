Lemma Hs-sym (global symbol inequality on the compactified cosphere bundle; THEOREM, CONFIRMED by V144 after the
correction of one decimal at S_y; elementary given V086, V088, V130, V132 and V134). Notation of Proposition H3-red. C-bar is the compactified cylinder of
V130: the radial blow-up of the origin adds the inner circle {t = -infinity} and the far circle F = {t = +infinity} is
added at infinity; W~ = q d_t + vartheta d_theta extends continuously to C-bar as a b-vector field (q rho d_rho near the
inner circle, rho = e^t). Covectors are unit b-covectors nu = (nu_t, nu_theta) in S^1, paired by
W~.nu = q nu_t + vartheta nu_theta. The critical set is Crit = {+-P} u {S_x^+-} u {S_y^+-} u F, with S_x^+- the inner
points theta = 0, pi and S_y^+- the inner points theta = +-pi/2. Lambda is the escape function of V130 (smooth on
C-bar, values 0, 1, 2, 3 on +-P, S_x, S_y, F, W~.grad Lambda > 0 on C-bar \ Crit, hence W~.grad Lambda >= 0 everywhere).
s is the order of V130 or V132 (41/20 near the closed horizontal segments from +-P to S_x^+- and on the source discs,
25/4 on |cos theta| <= 1/2 and on a far collar, W~.grad s >= 0, continuous on C-bar by the origin angular limit of
V132). The sector is Q = {|cos theta| <= eps_1}, where eps_1 <= 1/2 is fixed with supp chi in Q (chi = 1 on
|cos theta| < eps_0 < eps_1, as in Proposition H3-red), so s = 25/4 on Q and the cofactor u = chi h/(b p) lives on Q. The energy symbols are
     m_v(X, nu) = 1 + c_l - (1 + beta) q - s(X) nu^T DW~ nu - p_0(X, nu)                      (bulk v = h/b, order s),
     m_u(X, nu) = 1 + c_l - (1 + beta) q + 2 vartheta tan theta - vartheta cot theta - sigma nu^T DW~ nu - p_0(X, nu)
                                                                            (cofactor u = chi h/(b p), order sigma, on Q),
where p = cos^2 theta sin theta is the cofactor weight, DW~ is the Jacobian of (q, vartheta) in (t, theta) and p_0 is the principal symbol of the coupling (V086 (1),
transported to unit cylinder covectors; the change of variables is conformal). The zeroth-order parts are the exact
energy densities of the operators b^(-1) T_R b and (b p)^(-1) T_R (b p) in L^2(dt dtheta), by div_C W~ = 2 c_l - 2 q
(Lemma B). The logarithmic term (W~.grad s) log<xi> of a variable order (V086) is >= 0 and is not included.
Claim. Put mu_0 := m_x = Sigma (3/2 - 41/20) + delta A = 0.97260878. For every mu < mu_0 there are N >= 0 and L_0 >= 0 with
     G_v := m_v + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu   on C-bar x S^1,
     G_u := m_u + N W~.grad Lambda + L_0 (W~.nu)^2 >= mu   on Q-bar x S^1.
Proof. (a) Continuity. q, vartheta and DW~ converge uniformly as t -> -infinity to q_0 = -A cos^2 theta + D sin^2 theta,
vartheta_0 = Sigma sin theta cos theta and their Jacobian, and as t -> +infinity to (c_l, 0) and 0 (proof of Lemma C;
the t-derivatives tend to 0 by the same interpolation argument). p_0 = O(e^(2t)) at the origin end and O(e^((k-1)t)) at
infinity (6.5), so p_0 -> 0 uniformly at both ends. vartheta tan theta = sin theta (vartheta / cos theta) is continuous
up to the vertical axis, and |vartheta / cos theta| <= sup |d_theta vartheta|. beta is constant near both ends, s
and Lambda are continuous on C-bar. Hence m_v, m_u, W~.grad Lambda and W~.nu are continuous on the compact sets
C-bar x S^1 and Q-bar x S^1.
(b) Characteristic margins over Crit. Let Sigma_0 = {(X, nu) : W~(X).nu = 0}. At +-P, W~ = 0, every nu is
characteristic, q = 0, s = 41/20, and min over nu of m_v(P, nu) = min(b_P - s mu_P, b_P + g_P - s A_P) = 4.52536 (V134;
b_P = 1 + c_l, the Jacobian is diagonal on the x-axis and p_0(P, nu) = -g_P nu_1^2). At S_x^+-, W~ = (-A, 0), the
characteristic covectors are nu = (0, +-1), DW~ = diag(0, Sigma), s = 41/20, so m_v = 1 + c_l + (4 + delta) A - (41/20)
Sigma = 3 Sigma/2 + delta A - (41/20) Sigma = m_x = 0.97261 (V086, V131). At S_y^+-, W~ = (D, 0), nu = (0, +-1),
DW~ = diag(0, -Sigma), s = sigma = 25/4: m_v = 1 + c_l - (4 + delta) D + (25/4) Sigma = -116.97305 + 196.57610 = 79.60305,
and m_u = m_v + 2 Sigma = Sigma (sigma - 1/2) - delta D = 142.50740 (V088). On F, W~ = (c_l, 0), nu = (0, +-1),
DW~ = 0, p_0 = 0, vartheta tan theta = vartheta cot theta = 0: m_v = m_u = 1 + c_l - (1 + gamma) c_l = 1 + c_l/2 =
3.78768 (V088). The minimum of these values is m_x = mu_0. The points of Crit in Q-bar are S_y^+- and F n Q-bar.
(c) Choice of N. Fix mu' in (mu, mu_0). The set E = {(X, nu) in Sigma_0 : m_v(X, nu) <= mu'} is compact and, by (b),
contains no point over Crit. Its projection B is compact in C-bar \ Crit, so c_B := min_B W~.grad Lambda > 0. With
N c_B >= mu' + max |m_v|, the function G_0 := m_v + N W~.grad Lambda satisfies G_0 >= mu' on Sigma_0: on E by the choice
of N, off E because m_v > mu' and W~.grad Lambda >= 0.
(d) Choice of L_0. The set {G_0 <= mu} is compact and disjoint from Sigma_0, so |W~.nu| >= c_U > 0 on it; take
L_0 c_U^2 >= mu + max |G_0|. Then G_v >= mu everywhere. The same steps on Q-bar x S^1 with m_u (and the larger of the
two N and L_0) give G_u >= mu. QED.
Explicit values at S_y (illustration of (d) and of remark (4) of H3-red): at S_y, W~.nu = D nu_t and
m_v(S_y, nu) = -116.97305 + 196.57610 nu_theta^2, m_u(S_y, nu) = -54.06870 + 196.57610 nu_theta^2, so
m + L_0 D^2 nu_t^2 >= mu for all nu iff L_0 D^2 >= 116.97305 + mu (bulk) and 54.06870 + mu (cofactor); with
D^2 = 453.7518 this is L_0 >= 0.2578 + mu/D^2 and L_0 >= 0.1192 + mu/D^2. The negative-energy covectors near the
radial direction at S_y are thus absorbed by the elliptic term, whose cost is of lower order by the equation (Step 3
below). This replaces the overlapping cones of remark (4) of H3-red by one inequality.

Proposition Hs (the high a priori estimate on X_s; THEOREM, V151: every input is CONFIRMED, by V146 to V150 and V144,
and the assembly below is CONFIRMED with its order of choices; with it, the high Fredholm theorem V152). Matrix form of Lemma Hs-sym: every term of G_v and G_u is a quadratic form in nu
(kappa = kappa |nu|^2, (W~.nu)^2 = nu^T W~ W~^T nu, and p_0(X, nu) = nu^T P(X) nu with the symmetric coupling matrix
P(X) = R_theta^T [[-rho_y, rho_x/2], [rho_x/2, 0]] R_theta in the cylinder covector frame, rho_x, rho_y the Cartesian
derivatives of the renormalized density at X and R_theta the rotation by theta, since the change of variables is
conformal), so G_v(X, nu) = nu^T M_v(X) nu for unit nu with
     M_v(X) := (kappa_v + N W~.grad Lambda) I - s(X) sym DW~ - P + L_0 W~ W~^T,   kappa_v = 1 + c_l - (1 + beta) q,
and Lemma Hs-sym is the pointwise matrix inequality M_v(X) >= mu I on C-bar; likewise M_u (kappa_u, sigma) >= mu I on
Q-bar. Fix mu in (0, m_x) and N, L_0 accordingly. Since supp chi is a closed subset of {|cos theta| < eps_1} (V126),
there are open sectors Q_1, Q_2 with supp chi inside Q_1, closure(Q_1) inside Q_2 := {|cos theta| < eps_1}, and s = 25/4
on Q_2. On the cylinder R x S^1 (flat metric, coordinates (t, theta)) let <D> = (1 - d_t^2 - d_theta^2)^(1/2),
R = (R_t, R_theta) = (d_t, d_theta) <D>^(-1), so that R^* R = I - <D>^(-2) and ||R w||^2 = ||w||^2 - ||w||^2_{H^(-1)}.
Let A_v = Op(e^(N Lambda) <xi>^(s(X))) and A_u = Op(e^(N Lambda) <xi>^sigma) = e^(N Lambda) <D>^sigma (uniform left
quantization; the cofactor u is extended by zero outside supp chi), w = A_v v, z = A_u u, and fix eps in (0, 1/32].
||h||^2_{X_s} is equivalent to ||v||^2_{H^(s(.))} + ||u||^2_{H^sigma} (V126), and X_{s-eps} is the space of
Proposition H3-red. The inputs, all CONFIRMED:
 (Q0) (V146) ||w|| <= C ||v||_{H^(s(.))}, ||v||_{H^(s(.))} <= C (||w|| + ||v||_{H^(s(.)-eps)}), and
      ||w||_{H^(-r)} <= C ||v||_{H^(s(.)-r)} for 0 <= r <= 1; the same for z, u and sigma. No invertibility of the bare
      left quantization is used (it may have a low-frequency kernel). Sector support: z and R z are not supported in
      supp chi, but if psi = 1 on Q_1 and supp psi is in Q_2, then ||(1 - psi) R z||_{H^K} <= C_K ||u||_{H^(sigma-eps)}
      for every K; hence for a bounded matrix field M with M >= mu I on Q_2,
           <M R z, R z> >= mu ||R z||^2 - C ||h||_{X_{s-eps}} ||h||_{X_s}.
 (Q1) (V149 on test functions, V150 on the maximal domain) Let P = B.grad + c with B, c in W^(7,inf) uniformly on the
      cylinder, a = B.grad s >= 0, and M_B = ((1/2) div B - c + N B.grad Lambda) I - s sym DB. If v and P v are in
      H^(s(.)), then for every eta > 0
           - Re <A_v P v, A_v v> >= <M_B R A_v v, R A_v v> - eta ||v||^2_{H^(s(.))} - C_eta ||v||_{H^(s(.)-eps)} ||v||_{H^(s(.))},
      and the same for A_u at the constant order sigma (a = 0). On test functions the identity holds with the term
      Re <a log<D> w, w> on the right (V149: a Taylor expansion of the coefficients to degree 6 in the kernel, the
      C^(6,1/2) remainder times the order-25/4 kernel being O(|z|^(-7/4)), integrable in two dimensions; [d_j, A] is
      separated exactly so that the actual coefficient W~.grad s of the logarithm is kept); V150 regularizes w in its
      conjugated equation (two Friedrichs commutators) and discards the logarithmic form by its lower bound
      Re <a log<D> w_n, w_n> >= - C ||w_n||^2_{H^(-1/32)} (V145) before the limit, so no graph-dense core is used. Applied
      to the bulk, B = W~, c = beta q - 1, so M_B = (kappa_v + N W~.grad Lambda) I - s sym DW~ (div_C W~ = 2 c_l - 2 q,
      Lemma B); to the cofactor, c = beta q + vartheta p'/p - 1, so (1/2) div W~ - c = kappa_u. For h in D_H both
      hypotheses hold: P_v v = (T_R h)/b, and P_u u = chi (T_R h)/(b p) + (W~.grad chi) v/p, where the last term is
      supported where p is bounded below and s = sigma.
 (Q2) (V147) For every eta > 0 there is a compact operator K_eta on X_s with
           |- Re <A_v (C_R h/b), w> + <P R w, R w>| + |- Re <A_u (chi C_R h/(b p)), z> + <P R z, R z>|
                <= (eta ||h||_{X_s} + ||K_eta h||_{X_s}) ||h||_{X_s}
      (smooth approximation of the localized H^(51/8) coefficients in multiplier norm, so that each local commutator is a
      limit of compact ones; the exact cofactor identity of V143, the compact axis row of V142 and the tail bounds of
      V140).
 (Q5') (V148) C_R is bounded on X_{s-eps}, and for every a > 0 there is C_a with, f = (S - lambda) h,
           ||W~.R w|| + ||W~.R z|| <= C_5 ||f||_{X_s} + a ||h||_{X_s} + C_a ||h||_{X_{s-eps}},
      C_5 independent of a, uniformly for lambda in [0, lambda_*] (smooth approximation of W~ in C^6 and the equation
      W~.grad v = f/b + (1 + lambda - beta q) v - C_R h/b and its cofactor analogue).
(F1) If M(X) >= mu I pointwise, then <M R w, R w> >= mu ||R w||^2 = mu ||w||^2 - mu ||w||^2_{H^(-1)}: no symbol calculus
is needed, because the symbol is a quadratic form in the covector, and ||w||_{H^(-1)} <= C ||h||_{X_{s-1}} by (Q0).
Claim. (Hs_eps) of Proposition H3-red holds with an additional term ||K h||_{X_s} on the right, K compact on X_s and
independent of lambda in [0, lambda_*] (the proof of H3-red absorbs it into its compact operator): there is C_s with
     ||h||_{X_s} <= C_s (||(S - lambda) h||_{X_s} + ||h||_{X_{s-eps}} + ||K h||_{X_s}),   h in D_H, 0 <= lambda <= lambda_*.
With Proposition H3-red, (H3) follows, and S_1 and L_red are Fredholm of index 0 (Corollary H-spec).
Proof. Let h in D_H, f = (S - lambda) h, f_v = f/b, f_u = chi f/(b p); then ||A_v f_v|| + ||A_u f_u|| <= C ||f||_{X_s}.
Write ||.|| for ||.||_{X_s}, l(h) := ||h||_{X_{s-eps}}, and C for constants that depend only on mu, N, L_0, chi, eps and
the inputs (not on eta, a, theta below).
Step 1 (bulk). f_v = (P_v - lambda) v + C_R h/b. By (Q1) with B = W~, (Q2) and lambda >= 0,
     - Re <A_v f_v, w> >= <(M_v - L_0 W~ W~^T) R w, R w> - (2 eta ||h|| + ||K_eta h||) ||h|| - C_eta l(h) ||h||,
and <L_0 W~ W~^T R w, R w> = L_0 ||W~.R w||^2 exactly, so by (F1)
     mu ||w||^2 <= ||A_v f_v|| ||w|| + L_0 ||W~.R w||^2 + (2 eta ||h|| + ||K_eta h||) ||h|| + C_eta l(h) ||h||.
Step 2 (cofactor). Since b p u = chi h, f_u = (P_u - lambda) u - (W~.grad chi) v/p + chi C_R h/(b p), and the cutoff term is
supported in Q_1 minus {|cos theta| < eps_0}, where p is bounded below and s = 25/4, so
||A_u ((W~.grad chi) v/p)|| <= C_chi ||v||_{H^(s(.))}. As in Step 1, with (Q1) for the cofactor, (Q2), and the sector
form of (Q0) for M_u (which is >= mu I on Q-bar, a superset of Q_2),
     mu ||z||^2 <= (||A_u f_u|| + C_chi ||v||_{H^(s(.))}) ||z|| + L_0 ||W~.R z||^2 + (2 eta ||h|| + ||K_eta h||) ||h||
                   + C_eta l(h) ||h||.
Step 3 (penalty). By (Q5'), L_0 (||W~.R w||^2 + ||W~.R z||^2) <= 3 L_0 (C_5^2 ||f||^2 + a^2 ||h||^2 + C_a^2 l(h)^2).
Step 4 (assembly). Put e := 3 L_0 a^2 + 2 eta + 2 theta for theta > 0. Young's inequality on ||A_v f_v|| ||w||,
(||A_u f_u|| + C_chi ||v||) ||z||, ||K_eta h|| ||h|| and l(h) ||h|| in Steps 1 to 3 gives
     (mu/2) ||w||^2 <= C ||f||^2 + e ||h||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2),
     (mu/4) ||z||^2 <= C ||f||^2 + (2 C_chi^2/mu) ||v||^2_{H^(s(.))} + e ||h||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2).
By (Q0), ||v||^2_{H^(s(.))} <= C_0 (||w||^2 + l(h)^2) and ||u||^2_{H^sigma} <= C_0 (||z||^2 + l(h)^2). Insert the first
bound for ||v||^2 into the second line (the system is triangular: the bulk inequality contains no cutoff term in u, and
the coupling enters both lines only through (Q2)) and add:
     ||h||^2 <= C' (||f||^2 + C_(eta, a, theta) (||K_eta h||^2 + l(h)^2)) + C_4 e ||h||^2,
     C_4 = C_eq ((2 C_0/mu) (1 + 8 C_0 C_chi^2/mu^2) + 4 C_0/mu),
C_eq the constant of the norm equivalence, and C_4 does not depend on eta, a, theta. L_0 is fixed by Lemma Hs-sym before a is chosen, so a, eta and theta can be
taken with C_4 e <= 1/2. This gives the claim with K a fixed multiple of K_eta (for the chosen eta). The inequality is proved for every h in D_H
directly, since (Q1) is stated on the maximal domain (V150) and (Q0), (Q2), (Q5') hold on X_s and D_H. QED.
Remarks. (1) Nothing in Lemma Hs-sym is numerical beyond the five confirmed margins m_x, m_y (bulk 79.603, cofactor
142.507), m_inf and the source margin 4.52536; N, L_0, C_s and K are qualitative (the escape function of V130 carries no
derivative constants). mu can be any number below m_x = 0.9726. (2) The bulk margin at S_y at order 25/4 is positive
(79.60), so the bulk component is coercive on its own characteristic set there; the cofactor is needed for the space
(J1 to J3, V126), not for coercivity. (3) The three arbitrarily small high-norm errors (the matrix conversion in (Q1),
the coupling in (Q2) and the penalty in (Q5')) are what the finite coefficient regularity costs: the W^(7,inf)
transport and the H^(51/8) coupling coefficients are approximated uniformly by smooth ones, and only the smooth
approximants enter the symbolic composition, whose constants then multiply only the lower norm or the compact term.
The exact logarithmic coefficient W~.grad s >= 0 is never approximated. (4) The earlier versions of this proposition
used a lower-norm-only (Q5) and a scalar positivity step (F2) for the logarithmic term; (F2) is superseded by V150, which
discards the logarithmic form by V145 inside the proof of (Q1). (5) With V140 (||chi_+- C_R||_{X_s -> X_s} -> 0),
Lemma D of H3-red also follows from Lemma A(i). V140 reduces the full equation to a compact core with a high-norm error;
this is consistent with, but does not replace, (Hs_eps): a core estimate with a compact error requires the same global
propagation structure that Lambda encodes (the flow passes from the core through the horizontal entry of the inner
end, around the inner circle and out through the vertical exit back into the core), so a purely local core estimate
would be circular. (6) Consequence (THEOREM, V152). On the exact maximal domain D_s = D_H, S - lambda : D_s -> X_s is
Fredholm of index 0 for every lambda >= 0 (the path from lambda_* of Lemma H-spec, enlarged to contain any given
lambda); with B_H = {J chi_0 + a v : J in R, v in H^(29/4)(R)}, a = e^(-3t) b, Gamma_H = a H^(25/4)(R), the operators
L_ren and L_red = L_ren + c[.] zeta (zeta the actual moving-tail vector) are Fredholm of index 0 from B_H (+) D_s to
Gamma_H (+) X_s. A high null vector is a low null vector; under low injectivity the high operator is bijective and
its inverse is the restriction of the low inverse. No constant is computed. (7) Perturbation (status 10:30Z). The full
variable-order Kato-Ponce bound ||[A, B.grad] v|| <= C (||grad B||_inf ||v||_{H^s} + ||B||_{H^s} ||grad v||_inf) is
false (REFUTED, V153): [A, B.grad] contains -(B.grad s) log<D>, and localized packets with bounded H^s norm give a
commutator of size log n. The repair keeps (W + B).grad s as the single logarithmic coefficient: the order of V132
satisfies W.grad s >= kappa_s |grad s| (V154), so (W + B).grad s >= 0 for ||B||_inf <= kappa_s/2, and this
coefficient is discarded by V155 when it is C^(1,alpha). The global weighted bounds for the perturbation velocity
are a THEOREM (V156: B_norm[g] = c[g] (chi_0 B_0 + (1, 0)/3) + Z[g], Z[g] in H^(s(.)), B_norm[g] in C_b^(1,alpha) for
alpha < 1/20). The uniform estimate for small perturbations is a THEOREM in the square-summed (dyadic)
form (V157 to V160, Theorem Hs-pert below), with generation, index 0 and, under injectivity of S, a uniform inverse; the
single-operator variant through the tame commutator bound of Lemma K is a second confirmed route (V161, V163, with the
sign correction V162).
