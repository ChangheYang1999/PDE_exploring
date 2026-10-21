(normalizations of 4.4). The field is therefore not in the class, whose condition (A4) requires the profile equation on
all of R^2. What is proved is this: for each bounded set K fixed before the field is chosen, (A1) to (A3), the canonical
velocity law, the normalization and the profile equation on a neighbourhood of K are satisfied together by some field,
and K may contain any fixed neighbourhood of 0, of the field's first source P and of the axis segment between them. No
contradiction can be derived from these assumptions alone. The statement concerns regions fixed in advance. A region
chosen from the field after its construction, for instance one containing a nonzero extremum of rho, detects the
failure, and a proof that uses the equation elsewhere to derive a restriction on the axis data and then concludes in a
bounded region is not affected. Exact vanishing of the residual on a bounded region does not certify a small normalized
residual elsewhere: wherever the denominators are positive, |R|/N_f <= 1 and |R|/N_v <= c_l by the triangle inequality,
and the extension attains the value 1 for both. The extension is not a profile and says nothing about the existence of
one.

(d) Structure at the source P (frozen-coefficient models; leading-order statements, not classifications). Use
linearizing coordinates at P, with W = (A xi, y) + ... and rho = g* y + ..., where g* = rho_y(P).
- Conormal balance. A conormal term C |xi|^mu y^j along the weak characteristic {xi = 0} balances only for
  mu_j = (1 + g* - j)/A. At X3, mu_1, mu_3, mu_5, mu_7, mu_9, mu_11 = 2.931, 2.734, 2.537, 2.340, 2.143, 1.946.
  For j = 3, the term needs a companion: a G_1 term xi^(mu_3 + 2) y and a w term xi^(mu_3 + 3). Without them the y^1
  coefficient of the curl equation fails.
- Coupled packets. A high-frequency packet carried along the orbits of W has amplitude rate m = 1 + rho W_2/|W|^2.
  Along the source orbits tangent to the weak direction, on which xi/|y|^A is fixed and finite, this rate tends to
  1 + g* (along the axis it tends to 1), so the packets near P behave as |y|^(1+g*) F(xi/|y|^A), with F smooth and
  compactly supported and the odd extension from y > 0. Such a function is C^(k,alpha) at P if 1 + g* >= (k + alpha) A
  (a sufficient condition). At X3, (1 + g*)/A = 3.0293: the packets are C^(2,alpha) for every alpha < 1 and
  C^(3,alpha) for alpha <= 0.029; a nonzero packet is not C^4, since d_xi^4 of it is |y|^(1+g*-4A) F^(4)(xi/|y|^A)
  and F^(4) is not identically 0. [Corrected 2026-10-20: an earlier version said that the rate tends to 1 + g* at P
  without restricting the orbits.]
- Source motion. The source moves with the solution. Along a differentiable family of exact profiles, or for an
  admissible solution of the linearized problem, a perturbation (dc_l, dw) moves the source by p = -dw(P)/A, and
  dh(P) + p h'(P) = 0. This is the first-order form of h = 1 at the moved source; it does not hold for arbitrary
  perturbations.
- Singular values cannot decide isolation. The operator d_t + (1 - d_s^2)^(-1) from X = {u in L^2(T^2): d_t u in L^2},
  with the graph norm, to L^2(T^2) is injective, its coupling (1 - d_s^2)^(-1) is compact from X to L^2, and it has
  quasimodes with singular values 1/(1 + n^2) -> 0. So a count of small singular values, or their decay with
  resolution, cannot by itself show a family (question Q1).

(e) Fixed-point formulation through the source. On the basin of P, rho = C eta_P[W] with C = rho_y(P) and eta_P[W](X) =
y exp(-int_{-infinity}^0 [b(Phi_t X) - 1] dt), where W_2 = y b and Phi_t is the flow of W (result R6). Its linearization
is the transport-form linearization W.grad d rho - d rho + dW.grad rho = 0 with dW = U[d rho] + dc_l X. The normalization
is dC = d rho_y(P) + p g'(P), with p the source displacement of (d). This holds on the perturbations for which the
orbit integral converges at P; Frechet differentiability in fixed Hoelder spaces is not proved. The formulation
excludes the kernel elements that are not C^1 at P, among them the pure-transport packets (rate 1). The coupled
packets of (d) are not excluded by the C^1 requirement; whether they belong to the kernel of the full coupled
linearization is not proved.

(f) A necessary condition for P_inf.
- (C1) holds for every profile of P_inf: if a profile of the class (rho of class C^(2,alpha), growth exponent below 1,
  canonical velocity law) is C^infinity near 0, then rho is C^infinity on an open neighbourhood of the segment (0, x*) x
  {0}. Proof (external
  referee; audited by a second external referee; checked by the verifier, including the localization of the velocity
  law): a localized energy estimate for the derivatives of order k, iterated in k. One-derivative lemma: let T
  u = W.grad u + sum_nu B_nu(X) R_nu u + C(X) u, with W real of class C_b^(2,alpha), B_nu and C of class C_b^(1,alpha),
  and R_nu constant Fourier multipliers whose symbols satisfy |m| <= C and |grad m(xi)| <= C/|xi|; let u be in L^2 and T
  u in H^(-1). If a compact nonstationary arc of W has a tube on which T u is in H^1_loc, and u is in H^1 near the
  forward endpoint, then u is in H^1 near every earlier point of the arc. For the proof, regularize with
  J_eps = (1 - eps^2 Delta)^(-1): the identity T(J_eps u) = J_eps(T u) - eps^2 J_eps([Delta, T](J_eps u)) is exact, and
  its commutator, written in divergence form and read in the sense of distributions, involves DW, Delta W and only the
  first derivatives of B_nu and C (no second derivatives of B_nu and C and no third derivatives of W). The commutator
  bound ||[chi, R] d_j v||_2 <= C (int |zeta| |chi^(zeta)| d zeta) ||v||_2 holds for cutoffs chi of class C_c^(2,alpha),
  which are built from C^(2,alpha) flow coordinates (t, s) with W.grad = d_t. With the weight chi = eta(s) e^(lambda
  t/2) theta(t) and D = W.grad one has D(chi^2) >= lambda chi^2 - K_e e^2, with e supported where u is known to be in
  H^1,
  and for lambda large the L^2 norm of chi grad J_eps u is bounded uniformly in eps; weak compactness gives chi grad u
  in L^2. Iteration: let O be the open set of points whose forward trajectories reach the smooth neighbourhood of 0 in
  finite time along a nonstationary arc; rho is in H^2_loc(O). If rho is in H^k_loc(O), k >= 2, then for each compact
  tube in O and a cutoff eta in C_c^infinity(O) equal to one on a neighbourhood of the tube, the derivatives
  u_I = d^I(eta rho), |I| = k, solve, in the sense of distributions (by mollification, under the induction hypothesis),
  a system of this form near the tube, after the coefficients are extended from a compact neighbourhood of the tube by a
  smooth cutoff so that they have the global regularity required by the lemma and agree with the original ones near the
  tube (W itself contains the unbounded term c_l X): the terms with one derivative on W give a matrix in DW, the term
  with all k derivatives on U is grad rho . R u_I plus a locally H^1 term (by the localization below), with coefficients
  B_nu, the components of grad rho, of class C^(1,alpha), and the remaining products (d^J U)(grad d^(I - J) rho),
  2 <= |J| <= k - 1, are locally H^1 by an interpolation (Gagliardo-Nirenberg) product estimate. Hence rho is in
  H^(k+1)_loc(O); by induction rho is C^infinity on O, which contains the segment (0, x*) x {0} because w < 0 there. The
  referee proves the commutator, interpolation, product and regularization estimates; the other inputs are textbook
  facts of Fourier analysis, distributions, integration, approximation, compactness and ODE flows (among them Plancherel
  and Fourier inversion, the Young and Hoelder inequalities, Fubini's theorem and dominated convergence, mollification,
  the L^2 bound of the maximal function, weak compactness in L^2, the regularity of ODE flows and the inverse function
  theorem), and, in the Localization below, the boundedness of order-0 Fourier multipliers on Hoelder-Zygmund spaces
  with a positive exponent. The proof is qualitative: it gives no bound uniform as the axis point tends to 0 or to x*.
  [Revised 2026-10-20: an earlier version proved (C1) by paradifferential propagation, with a positive-commutator
  estimate cited from M. E. Taylor, Pseudodifferential Operators and Nonlinear PDE, section 6.1, that was not checked
  against the source; that estimate is no longer used.] Localization (verifier). Let X_0 be a point, delta > 0, chi in
  C_c^infinity with chi = 1 on B(X_0, 2 delta), and f = (1 - chi) rho. On B(X_0, delta), U[rho] is the order-0 Fourier
  multiplier (xi_1 xi_2, -xi_1^2)/|xi|^2 applied to chi rho, plus U[f], and U[f] is C^infinity there with |d^k
  U[f](X)| <= C_k int (delta + |Y - X_0|)^(-2-k) |f(Y)| dY for k >= 1, finite because the growth exponent is below 1.
  For compactly supported data the multiplier is (V2): its components are d_1 d_2 and -d_1^2 applied to the logarithmic
  potential, whose kernels are the principal-value kernels of (V2), the second with the local term. The limit in (V2)
  exists for rho and for chi rho, hence for f; for X, X_1 in B(X_0, delta) the kernel of (V2) is smooth on the support
  of f, so U[f](X) - U[f](X_1) is an absolutely convergent integral, which may be differentiated under the integral
  sign. With the boundedness of order-0 multipliers on Hoelder-Zygmund spaces of compactly supported functions, this
  also gives the local C^(2,alpha) regularity of W used in the lemma above and in (h) and (m).
- Endpoint condition at P. If d_y^3 rho(x, 0) stays bounded as x -> x*^-, then (C2') holds for j = 3, because
  H_3 -> infinity at P. More generally, (C2') for j holds if the rescaled functions R_t(z) = rho(x* - t^A, t z)/t on a
  fixed interval |z| <= z_0 are relatively compact in C^j as t -> 0. Only the derivatives
  d_z^j R_t(0) = j! t^(j-1) G_j(x* - t^A) enter, and the Taylor series in z need not converge. Since R_t(z) -> g* z
  pointwise, every C^j limit point is g* z, so t^(j-1) G_j(x* - t^A) -> 0 for j >= 2; this is (C2'), because
  H_j ~ C t^(-(j-1)) at x = x* - t^A. [Clarified 2026-10-20: an earlier version wrote R_t as its Taylor series in z.]
- Theorem. Let rho be a profile of the class that is C^infinity near 0 and such that d_y^3 rho(x, 0) stays bounded as
  x -> x*^-. Then B_3(c_l, w) = 0. Proof. By (C1) the third axis equation holds on (0, x*), so (G_3/H_3)' = F_3/(w H_3)
  there. By the endpoint condition G_3/H_3 -> 0 at x*, so the improper integral of F_3/(w H_3) up to x* converges
  (F_3 need not be bounded at P) and equals -G_3/H_3(x). At 0, G_3 is smooth and even and H_3/x^(p_3) is smooth, even
  and positive, so G_3/H_3 is a sum of powers x^(2m - p_3), 2m < p_3, plus o(1); since p_3 is not an even integer, the
  finite part removes these powers without a log term, and the constant term B_3(c_l, w) is 0. Without (C1) (external
  referee; checked by the verifier): the limit M = lim K/y of (m) exists on (0, x*) by integration along the
  characteristics, which uses only second derivatives, so d_y^3 rho(x, 0) exists as a transverse limit and the third
  axis equation holds in the sense of distributions (a_2 is in general only Hoelder continuous). If d_y^3 rho(x, 0) is
  bounded at P, then l_3 = 0 and Q_3 - Q_3(x*) = O(x* - x), where Q_3 = a_2/g^3 and m = -w/g are as in (i) (integrate
  dQ_3/dm = -3 A^beta m^(1 - beta) dZ/dm in m, with Z = G_3/H_3 = O(m^beta)); so the convergent form of B_3 displayed in
  (i) converges at P with no Hoelder condition there, and it is 0, because C_0 = l_3 + B_3 holds in this weak form and
  C_0 = 0 by smoothness near 0. This proves the theorem without (C1) for B_3 in the derivative-free form of (i); with
  (C1) the classical form holds as well. At C^(2,alpha) alone this argument does not reach order 5, since it does not
  construct the traces a_4 and b_5.
- For odd j >= 5 the same argument gives B_j(c_l, w) = 0 when p_j is not an even integer, provided the endpoint
  condition (C2') holds for every odd i with 3 <= i <= j (the functional B_j uses G_3, ..., G_(j-2), which must be the
  solutions selected by these conditions, with zero normalized limit at P; they need not be bounded). These conditions
  hold if rho is C^(j-1,alpha) near P with 0 < alpha < 1 and alpha > 1 - (j-1)/A (6.3.1 (h), Higher odd orders).
  [Corrected 2026-10-20: an earlier version said "every odd i <= j" and "bounded at P"; since G_1/H_1 = 1 the conditions
  start at i = 3.]
- This is a necessary condition for a profile of P_inf with bounded d_y^3 rho on the axis next to P. It is not a NO_inf
  theorem: it does not decide whether a profile of the class satisfies it, and it says nothing about profiles with d_y^3
  rho(x, 0) unbounded at P, except under the rescaled compactness criterion above or the hypotheses of (h)
  (for 1 < A <= 2, (m)); see 6.4.

(g) In the frozen coupled model at P, Hoelder regularity with exponent at most 1 - 2/A does not give the endpoint
condition, and one-sided smoothness does not give a finite l_3.
- Frozen model. Freeze the coefficients at P: with s = x - x* and g* = rho_y(P), the linearization of
  W.grad rho = rho about W = (A s, y), rho = g* y is
    L_g v := (A s d_s + y d_y - 1) v + g* U_2[v] = 0,
  where U_2[v] is the second component of the velocity of v (Fourier multiplier -xi^2/(xi^2 + eta^2)).
- Solution (external referee, checked by the verifier). For A > 2 and 3 < g*/(A - 1) < 4 (at X3, g*/(A - 1) = 3.251),
