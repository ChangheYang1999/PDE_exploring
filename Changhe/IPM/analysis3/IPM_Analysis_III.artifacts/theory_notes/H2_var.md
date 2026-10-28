Lemma H2-var (the variable-order remainder space and (H2); DERIVED, submitted for checking). It gives a
concrete space on which (J1) to (J3) carry over and proves (H2) for it; (H1) and (H3) on it are OPEN.
Coordinates. t = log r, theta, measure dt dtheta on the cylinder R x S^1, parity class P. In these coordinates
V.grad = q d_t + vartheta d_theta with q = V.X/r^2 and vartheta = V.grad(theta). The weight a(t) is that of V117
(e^(9t/5) for t <= 0, e^(-7t/2) for t >= 1, smooth and positive). Factored variable u = h/(x^2 y a), bulk variable
v = h/(r^3 a); u = v/(cos^2(theta) sin(theta)).
Assumptions.
(A_V) q, vartheta and the multipliers q_1 = 2 V_1/x + V_2/y + q a'/a, q_2 = q (3 + a'/a) have bounded derivatives of
     order <= 5 on R x S^1, and vartheta = 0 on the axes. (Expected from rho~ in H^(15/2-) locally, the degree-seven
     knot regularity of V069, so V in C^(6.5-), together with the expansions of V at 0 and at infinity; to be checked.)
(A_s) s is smooth on R x S^1 with bounded derivatives, 41/20 <= s <= 25/4, s = 25/4 on {|cos theta| < eps_1}, and
     V.grad s >= 0. (s = F(Lambda) of remark (7) has these properties if Lambda is chosen smooth off the critical sets
     of 6.4, smooth up to the arc r = 0 of the blow-up, and F is constant near 0, 1, 2 and 3.)
Space. Choose smooth functions psi_1, psi_2 of cos^2(theta) with psi_1 = 1 on {|cos theta| <= eps_1/2}, supp psi_1 in
{|cos theta| < eps_1}, psi_2 = 1 on {|cos theta| >= eps_1}, supp psi_2 in {|cos theta| > eps_1/2}, and
psi_1^2 + psi_2^2 >= c_0 > 0. Let O = {eps_1/2 <= |cos theta| <= eps_1} be the overlap; s = 25/4 on a neighbourhood of
O, and cos^2(theta) sin(theta) is smooth and nonvanishing there. With the left quantization
Op(m) w(x) = int e^{i x.xi} m(x, xi) w^(xi) dxi of the uniform calculus on R x S^1, put
Lambda_1 = Op(<xi>^(25/4)), Lambda_2 = Op(<xi>^(s(x))) and
     ||h||_var^2 := sum_j (||Lambda_j w_j||^2 + ||w_j||^2),   w_1 = psi_1 u, w_2 = psi_2 v
(L^2 norms in dt dtheta over one period; the periodic (toroidal) form of the uniform calculus on R^2). H_var is the
space of h in R in the parity class with finite norm; it is a Hilbert space. The axis zero of R_base is automatic: if
u is in H^(25/4) and u(t, pi/2) != 0, then int |u|^2 |cos theta|^(-9/2) dtheta = infinity near that point, so u is not
the factored variable of an element of R; with the parity, u = O(cos^2 theta) at the y-axis.
Claim 1 (the jet row). R_base is continuously included in H_var (on supp psi_2, v = cos^2(theta) sin(theta) u and
s <= 25/4), and H_var is continuously included in R (write h = sum_i psi_i g_i h with g_i = psi_i/(psi_1^2 + psi_2^2); the psi_1
piece lies in R_base, which is included in R by V118, and the psi_2 piece is of the type of Q in V118, the angular
weight being bounded on supp psi_2). (J1) and (J3) of V118 land in R_base, so they hold with
target H_var. (J2) of V116 and V118 needs the input remainder only in R_(4,s); on the sector {|cos theta| < eps_1/2}
H_var is the factored order 25/4 space with the axis zero, which embeds in R_(4,s) by V114, so (J2) holds for every
D_H in H_var if the sector cutoff of the jet row is placed inside {psi_1 = 1}. (DERIVED.)
Claim 2 ((H2)). Under (A_V) and (A_s) there is omega_H < infinity such that for every lambda > omega_H the operator
T - lambda, T = T_R, maps D_H := {h in H_var : T h in H_var} bijectively onto H_var and
     ||(T - lambda)^{-1} f||_var <= (lambda - omega_H)^{-1} ||f||_var.
So (H2) of Lemma H-spec holds with M = 1 in the norm ||.||_var.
Proof.
Step 0 (charts). For h in D_R and f = (T - lambda) h, T h = x^2 y a (T_1 u) = r^3 a (T_2 v) with
T_j = V.grad + q_j - 1 in cylinder coordinates (V is tangent to both axes, so V_1/x and V_2/y are bounded). Hence
w_j := psi_j (chart variable j) solves (T_j - lambda) w_j = psi_j f_j + vartheta psi_j'(theta) (chart variable j),
with f_1 = f/(x^2 y a), f_2 = f/(r^3 a). The last term is supported in O.
Step 1 (regularization). The chart equations hold in distributions on the whole cylinder: the axes carry no singular
part, because vartheta vanishes there (the argument of the density step of Lemma C'2). The R norm controls the w_j
only up to a power of r, so choose rho_delta(t) = (1 + delta cosh(beta t))^(-1) with beta so large that rho_delta w_j
is in L^2 for every h in R; then |d_t log rho_delta| <= beta uniformly in delta, and rho_delta w_j solves the chart
equation with the extra bounded multiplier q d_t log rho_delta (of size <= beta sup |q|). Below w_j stands for
rho_delta w_j. For 0 < delta <= 1 let J_delta = Op(<delta xi>^(-8)) and Lambda_{j,delta} = Lambda_j J_delta;
the left quantization gives Op(m(x, xi)) Op(b(xi)) = Op(m b) exactly, so Lambda_{2,delta} has the symbol
m_delta = <xi>^(s(x)) <delta xi>^(-8). For each delta it has order <= 25/4 - 8 = -7/4, and the family is bounded,
uniformly in delta, in the order-m_delta symbol class (with the log losses of the variable order:
d_x m_delta = (grad s) log<xi> m_delta). For h in D_R the w_j are in L^2 (on supp psi_1 the angular weight |cos theta|^(-9/2) of the factored variable
is >= 1), so z_j := Lambda_{j,delta} w_j lies in H^(7/4) and the L^2 energy identity
     Re <Lambda_{j,delta} (T_j - lambda) w_j, z_j> = - int (div V~/2 - Re q_j + 1 + lambda) |z_j|^2
         + Re <[Lambda_{j,delta}, V.grad] w_j, z_j> + Re <[Lambda_{j,delta}, q_j] w_j, z_j>
is valid (V~ = (q, vartheta), the divergence taken in dt dtheta).
Step 2 (the commutator symbol). By the composition formula, [Lambda_{2,delta}, V.grad] = Op(e_delta) Lambda_{2,delta}
+ R_delta with
     e_delta = s xi^T DV~ xi/<xi>^2 - 8 delta^2 xi^T DV~ xi/<delta xi>^2 - (V.grad s) log<xi>,
and R_delta of order m_delta <xi>^(-1+eps) uniformly in delta. The first two terms are bounded by (25/4 + 8) sup|DV~|.
For j = 1 the same holds without the log term. [Lambda_{j,delta}, q_j] is of order m_delta <xi>^(-1+eps).
Step 3 (sign of the log term; the only place where V.grad s >= 0 is used). The symbol (V.grad s) log<xi> is
nonnegative and in S^eps_{1,0} with bounded x-derivatives, so the sharp Garding inequality gives
Re <Op((V.grad s) log<xi>) z, z> >= - C_G ||z||^2.
Step 4 (estimate). Interpolation, ||Op(m_delta <xi>^(-1+eps)) w|| <= eta ||Lambda_{j,delta} w|| + C_eta ||w||
uniformly in delta, and steps 1 to 3 give
     Re <Lambda_{j,delta} (T_j - lambda) w_j, z_j> <= (omega_0 - lambda) ||z_j||^2 + C ||w_j||^2,
     omega_0 = sup (|div V~|/2 + |q_j|) + (25/4 + 8) sup |DV~| + C_G + eta - 1.
The overlap terms: s = 25/4 near O, so on functions supported in O, Lambda_{2,delta} and Lambda_{1,delta} differ by an
operator of order -infinity (uniformly in delta), and since psi_1^2 + psi_2^2 >= c_0 on O and cos^2(theta) sin(theta)
is smooth and nonvanishing there, ||Lambda_{j,delta}(vartheta psi_j' (chart variable j))|| <= C_O (||z_1|| + ||z_2||)
+ C (||w_1|| + ||w_2||). The order-zero parts obey the plain L^2 identity
Re <(T_j - lambda) w_j, w_j> = - int (div V~/2 - Re q_j + 1 + lambda) |w_j|^2, with the same overlap terms. With the
inner product <h, g>_delta := sum_j (<Lambda_{j,delta} w_j(h), Lambda_{j,delta} w_j(g)> + K <w_j(h), w_j(g)>) and any
fixed K > 0, Re <(T - lambda) h, h>_delta <= (omega_H - lambda) ||h||_delta^2 for every h in D_R, with omega_H
independent of delta (it contains omega_0, beta sup|q|, C_O and C/K). By Cauchy-Schwarz, (lambda - omega_H) ||h||_delta <= ||(T - lambda) h||_delta for lambda > omega_H.
Step 5 (delta -> 0). For f in H_var, ||f||_delta -> ||f||_var (norm with the same K; rho_delta -> 1 boundedly): Lambda_{j,delta} w = J_delta Lambda_j w +
[Lambda_j, J_delta] w, J_delta -> 1 strongly on L^2, and [Lambda_j, J_delta] is bounded from the order-s space to L^2
uniformly in delta, tends to 0 on smooth w, hence strongly. For h with ||h||_delta bounded, a subsequence of
Lambda_{j,delta} w_j converges weakly in L^2, and the limit is Lambda_j w_j in distributions, so
||h||_var <= liminf ||h||_delta. Hence for f in H_var and h := (T_R - lambda)^{-1} f in D_R (Lemma C'2 with the shift:
T_R - lambda is a bijection of D_R onto R for lambda > -kappa_*, h = -int_0^infinity e^{-(1 + lambda) s} f o Phi_s ds):
     ||h||_var <= liminf ||h||_delta <= (lambda - omega_H)^{-1} lim ||f||_delta = (lambda - omega_H)^{-1} ||f||_var.
Step 6 (bijectivity). h is in H_var by step 5, and T h = f + lambda h is in H_var, so h is in D_H. Injectivity on
D_H follows from D_H in D_R and Lemma C'2. QED.
Remarks. (a) Necessity of the sign. If V.grad s < 0 on an open set, -(V.grad s) log<xi> is positive and unbounded
there and no finite omega_H exists: h(X) = -int e^{-(1+lambda)s} f(Phi_s X) ds samples f downstream, so h has at X only
the regularity of f downstream. This is the transport analogue of V119, where the defect came from the coupling.
(b) The proof uses only (A_V), (A_s), the tangency of V to the axes, the parity and Lemma C'2. It does not use the
coupling, the margin certificates or the Morse structure beyond V.grad s >= 0; constant orders are a special case.
(c) omega_H is not computed; its main term is (25/4 + 8) sup |DV~| plus the overlap constant C_O. For Lemma H-spec only
finiteness matters: omega_H enters through lambda_* = omega_H + 1 + 2 ||C_R||, and (H3) in energy form at lambda = 0
gives (H3) for every lambda >= 0 at once (remark (1)).
(d) For the perturbed operators A_g of remark (3) the sign condition is stable: with s = F(Lambda) and F' = 0 near
0, 1, 2, 3, the set {F'(Lambda) > 0} is compact in the compactified blow-up and disjoint from the critical sets, so
V~.grad Lambda >= c > 0 there, and (V + W)~.grad s >= 0 whenever sup |W|/r <= c/sup |grad Lambda| (implied by a small
sup ||DW||, as in V090). The commutator step for W[g], which has only the regularity of g, needs the tame Kato-Ponce
form ||[Lambda_s, W.grad] h|| <= C (||DW||_infinity ||h||_s + ||W||_s ||grad h||_infinity) in place of the symbol
calculus (remark (3)); grad h is bounded because s >= 41/20 > 2.
What remains for the high inverse on H_var: (H1), boundedness of C_R on H_var (order-zero operators of the
dilation-invariant calculus on the variable-order space, the multiplier grad rho~ in C^(6.5-), the strain and axis
terms, and the factored structure of C_R h near the y-axis), and (H3), the a priori estimate with compact error,
which needs the joint high-energy symbol margin where s is locally constant (6.5, V088) and an escape weight
e^(N G(Lambda)) (equivalent norm) on the transition sets; and low injectivity.
