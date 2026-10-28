Lemma H3-var (the structure of (H3) on H_var; DERIVED outline, not a proof; item 2 is a complete frozen computation
submitted for checking). Notation of Lemma H2-var. Sigma = A + D = 31.452175663849..., delta = 9/5,
c_x := -Sigma - delta A = -49.72348106... (zeroth-order coefficient of the bulk chart at S_x),
c_y := delta D = 38.34261079... (zeroth-order coefficient of the factored chart at S_y),
m_x = Sigma (3/2 - 41/20) + delta A = 0.97260878319, m_y = Sigma (25/4 - 1/2) - delta D = 142.50739927 (V088, V079),
m_inf = 1 + c_l/2 = 3.78768130532 (V088).
1. The plain energy form fails at S_y. The frozen factored operator at the origin end is q d_t + vartheta d_theta + delta q
   (V088), and at theta = pi/2 one has q = D, d_theta vartheta = -Sigma, d_t q = 0. For a unit covector
   nu = (nu_t, nu_theta) the energy coefficient of the order-sigma conjugated equation is
        m_y(nu) = -Sigma/2 - delta D + sigma Sigma nu_theta^2,
   so V088 is the case nu_theta = 1, while for nu = (1, 0) the coefficient is -Sigma/2 - delta D = -54.0686986 for every
   sigma. No equivalent norm sum_j ||e^(N G) Lambda_j w_j||^2 with bounded scalar weights G therefore makes -S coercive modulo a
   compact term at S_y (as t -> -infinity, V~.grad G -> 0 there, and a sequence escaping along S_y with radial
   frequencies contradicts such an estimate), and remark (1) of Lemma H-spec cannot be used with the plain variable-order energy. The negative
   directions are elliptic for the transport: its symbol is i(D nu_t - Sigma phi nu_theta), phi = pi/2 - theta, and
   m_y(nu) > 0 iff nu_theta^2 > (Sigma/2 + delta D)/(sigma Sigma) = 0.27505 at sigma = 25/4 (|nu_theta| > 0.52445). On
   the complement |nu_t| >= 0.8514, so |D nu_t - Sigma phi nu_theta| >= 0.8514 D - 0.5245 Sigma |phi| > 0 for |phi| < 1.09.
   The coercive and elliptic regions must overlap (corrected at 09:40Z after V131's remark; m_y(1/2) = -4.9247 < 0, so
   a partition at |nu_theta| = 1/2 leaves no coercive region): for example |nu_theta| > 0.53, where m_y >= 1.1495, and
   |nu_theta| < 0.54, where |D nu_t - Sigma phi nu_theta| > 17.91 on |phi| <= 10^(-3) for the exact origin field; on the
   elliptic region the graph norm gives one derivative more. The correct high-frequency condition is a positive margin on the characteristic set
   {nu : V~(X).nu = 0} where V~(X) != 0, and in every direction at the zeros of V~ (only +-P in the open cylinder).
2. The normal family at the origin end (frozen computation; corrected after the verifier's 08:54Z remarks). As
   t -> -infinity, V~ = V~_0 + O(e^(2t)) with V~_0 = (q_0, vartheta_0), q_0 = -A cos^2 theta + D sin^2 theta,
   vartheta_0 = Sigma sin theta cos theta, and the coupling is O(e^(2t)) relative to the transport (grad rho~ = O(r^2), U
   homogeneous of degree 0; 6.5). By the parity reduce to theta in [0, pi/2]. After Fourier transform in t (dual
   variable xi real) the normal family is
        N(xi, lambda) = vartheta_0 d_theta + c(theta) + i xi q_0(theta) - lambda
   on the angular space of X_s: order s_0 = 41/20 in the bulk variable near theta = 0 (odd in theta there), the
   factored variable of order 25/4 near pi/2 (even in phi = pi/2 - theta, with the axis zero), nondecreasing order in
   between. Put nu = Re lambda,
        beta = (lambda - c_x + i xi A)/Sigma,   alpha = (c_y + i xi D - lambda)/Sigma.
   Near 0, vartheta_0 d_theta = Sigma theta (1 + O(theta^2)) d_theta and c + i xi q_0 = c_x - i xi A + O(theta^2), so the
   homogeneous solutions are theta^beta (1 + O(theta^2)); near pi/2, vartheta_0 d_theta = -Sigma phi (1 + O(phi^2)) d_phi
   and c + i xi q_0 = c_y + i xi D + O(phi^2), so they are phi^alpha (1 + O(phi^2)). A Taylor term f_j phi^j of the data at
   pi/2 has the particular solution f_j phi^j / (Sigma (alpha - j)), and a term f_j theta^j at 0 has
   f_j theta^j / (Sigma (j - beta)), modulo terms two orders higher; the indices are j in {2, 4} at pi/2 (even, axis
   zero, j < 25/4 - 1/2) and j = 1 at 0 (odd, j < 41/20 - 1/2).
   Claim: for every real xi, N(xi, lambda) is bijective whenever nu > -m_x = -0.97260878; in particular for every
   lambda >= 0.
   Proof. On (0, pi/2), vartheta_0 > 0, so N g = f is a regular first-order ODE and every solution gains one derivative
   over f in the interior; only the ends matter. Let nu > -m_x. Then Re beta = (nu - c_x)/Sigma > 41/20 - 1/2, so every
   homogeneous solution lies in the space near 0, and nu > -m_y gives Re alpha < 25/4 - 1/2, so no nonzero homogeneous
   solution lies in the space near pi/2 unless alpha is a Taylor index. The resonances alpha = 2, 4 and beta = 1 occur at
   lambda = c_y - 2 Sigma + i xi D, c_y - 4 Sigma + i xi D and c_x + Sigma - i xi A, with real parts -24.5617, -87.4661 and
   -delta A = -18.2713, all below -m_x. Injectivity: a kernel element is a multiple of the global homogeneous solution,
   which is not in the space near pi/2. Surjectivity: near pi/2 put g = sum_{j=2,4} f_j phi^j/(Sigma (alpha - j)) + g_r,
   where the remainder data r vanish to order above 25/4 - 1/2 in the H^(25/4) sense and
   g_r = -(1/Sigma) phi^alpha int_0^phi r(p) p^(-alpha-1) dp (with the O(phi^2) coefficient corrections absorbed by
   iteration); the integral converges and g_r is in the space by the Hardy (Mellin) inequality on the line
   Re = 25/4 - 1/2, since Re alpha < 25/4 - 1/2. Continue g across (0, pi/2) by the ODE. Near 0 the solution is
   C theta^beta (1 + O(theta^2)) + f_1 theta/(Sigma (1 - beta)) + (remainder solved by the Mellin inverse off the line
   Re = 41/20 - 1/2), all in the space since Re beta > 41/20 - 1/2 and beta != 1. QED for fixed xi.
   Role of the axis zero and the parity. Without the axis zero the index j = 0 enters at pi/2: at alpha = 0, i.e.
   lambda = c_y + i xi D, the constant phi^0 is in the space, so N(xi, lambda) has a one-dimensional kernel, and the
   f_0 term is resonant, so it has a one-dimensional cokernel. For fixed xi this is a discrete eigenvalue, not a failure
   of Fredholmness of N(xi, .). For the cylinder operator the union over real xi is the vertical line
   Re lambda = c_y = 38.3426, and S - lambda is not semi-Fredholm there: e^(i xi_0 t) g_0(theta) chi_n(t), g_0 in the
   kernel and chi_n unit-norm cutoffs spreading and moving to t -> -infinity, is a Weyl sequence (the O(e^(2t))
   corrections vanish in the limit), so no estimate ||h|| <= C ||(S - lambda) h|| + ||K h|| with K compact holds at
   lambda = c_y. Without the even parity the index j = 1 enters at pi/2, with the line Re lambda = c_y - Sigma = 6.8904.
   Both lines meet the path 0 <= lambda <= lambda_* of Lemma H-spec once lambda_* exceeds them. The j = 0 obstruction
   is the jet: it is the reason why the jet row is split off and inverted exactly (V109). (The earlier version of this
   item had the sign of the Taylor coefficient reversed and stated the conditions Re alpha < 2 and nu > c_y, nu > c_y -
   Sigma as thresholds; Re alpha < 2 is only the convergence condition of the integral formula from 0 for the whole
   datum, and the other two are isolated resonance lines, not half-planes.)
3. The far end. As t -> +infinity the normal operator in the bulk chart (gamma = -1/2) is c_l d_t - m_inf, and in the
   factored chart near the vertical axis the same, since vartheta d_theta log(cos^2 theta sin theta) = O(e^((k-1)t)). The
   family i xi c_l - m_inf - lambda is invertible for Re lambda > -m_inf = -3.7877. Angular derivatives commute with it;
   the angular transport is O(e^((k-1)t)) and its stretching cost tends to 0.
4. The characteristic-set margins. Away from the ends and from +-P, the escape weight e^(N G(Lambda)) adds
   N V~.grad G(Lambda) > 0 and absorbs any finite margin, including along the x-axis segment from P to S_x, which is a
   connecting orbit and not a critical element. The remaining frozen conditions are the ones already recorded:
   at +-P every direction is characteristic and the joint margin at order 41/20, coupling included, is
   min(b_P - s mu_P, b_P + g_P - s A_P) = 4.52536 (the slow branch; V134, which REFUTED the value about 14.8 stated here
   earlier; the fast branch is 15.51587; below s_fast = 3.5785, V064); at the ends the characteristic direction is nu_theta, with margins m_x,
   m_y, m_inf, and near the ends the characteristic direction tilts continuously (nu ~ (Sigma phi, D) near S_y).
5. Assembly (the standard variable-order b-type argument, not written out). Elliptic estimate off the characteristic
   set, propagation along the lifted flow with the order nondecreasing (the log term has the favourable sign, V088),
   radial-source estimate at +-P below threshold, and inversion of the normal families at both ends, which uses the
   high-frequency estimate to absorb the O(e^(2t)) and O(e^((k-1)t)) coefficient errors, give
        ||h||_var <= C (||(S - lambda) h||_var + ||h||_E),
   E a weighted H^(s - 1) space with an extra decay e^(eps t) at -infinity and e^(-eps t) at +infinity, for every
   lambda > Lambda_0, with C locally uniform in lambda. The inclusion H_var -> E is compact (Rellich on bounded t-sets
   and the decay factors), so (H3) of Lemma H-spec holds on 0 <= lambda <= lambda_*.
   Correction (09:40Z): the absorption of the O(e^(2t)) first-order coefficient errors by a normal inverse is not valid as
   stated, since a small first-order coefficient is not small in the graph norm (R_eps = eps d_theta, u_n = n^(-s) chi(t)
   e^(i n theta) against Q_0 = d_t - 1). Proposition H3-red below avoids this step for the low-order end bound, and V135,
   V137 give stable principal end inverses by energy arguments.
6. What this outline does not cover (OPEN; status at 09:40Z: (i) is settled on X_s by V126, (iii) is settled for the
   exact origin normal operator by V133 and is not needed in Proposition H3-red; (ii) is the open input (Hs_eps) of
   Proposition H3-red; (iv) is open). (i) (H1), which is needed before S acts on H_var at all; the factored
   structure at the vertical axis: with dx rho~ = x y (2 B + x B_x) and dy rho~ = x^2 (B + y B_y) (rho~ = x^2 y B near
   the axis), the factored coupling is (2 B + x B_x) U_1[h]/x + (B + y B_y) U_2[h]/y. For h = x^2 y a u, write
   dx h = x g with g even in x; then [(-Lap)^(-1), x] = 2 dx (-Lap)^(-2) gives
   U_1[h]/x = -dy (-Lap)^(-1) g - 2 dx dy (-Lap)^(-2) g / x, where the second term is odd in x and of order -3 in g, so
   the division by x costs nothing; this suggests that U_1[h]/x has the order of u, locally and without weights. The
   power weights of the cylinder norms are far outside A_2, so the Riesz transforms must be handled modulo their
   polynomial (moment) parts, as in Theorem C', and the strain term c[h] gives the jet direction x^2 y at the origin
   and belongs to the jet row. (ii) The propagation and radial estimates with coefficients of finite regularity
   (rho~ in H^(15/2-) locally, V069); tame commutator estimates instead of the full symbol calculus. (iii) Uniformity
   of the inverse in item 2 as |xi| -> infinity (the semiclassical form of item 4 at the end). (iv) Low injectivity.
   The constants C and the norm of the compact part are not computed.
