# Perturbed and moving-tail operators in the decoupled low spaces

## Statement and fixed realizations

Fix an angular exponent a in [18/5,4]. Use the exact normalized modal background rho_0, canonical velocity, cutoffs, scalar B, G and remainder R_a of proof 168. Thus

 w_a=|cos(theta)|^(-2a)r^(-17/2) for r<1,
 w_a=|cos(theta)|^(-2a)r^(-37/20) for r>=1,
 G=L2(g dt), g=e^(-t/2) for t<0, g=e^(123t/20) for t>=0,
 B={J chi_0+w:J real, w,w' in G}.

The B norm is the fixed integrating-factor norm of proof 168, equivalent to the displayed product norm. Write X_a=B direct-sum R_a, Y_a=G direct-sum R_a and E beta=x^2 y beta(log r). No condition J=0 is imposed.

Keep the actual high spaces fixed:

 H_full=B_H direct-sum X_s, Y_H=Gamma_H direct-sum X_s,
 B_H=R chi_0+a_H H^(29/4)(R), Gamma_H=a_H H^(25/4)(R).

Here a_H=e^(9t/5) sufficiently far left and e^(-7t/2) sufficiently far right. X_s is the exact variable-order, zero-axis-cofactor space of proof 123, with s_0=41/20, sigma=25/4 and the fixed robust order of proof 152. Use the fixed graph realizations proved in topics165 and167. In particular H_full embeds continuously in the coefficient class G_s of proof 155. All norms and cutoffs in this statement are fixed before selecting a perturbation radius.

For a coefficient perturbation v in G_s, put

 V_v=V_0+U[v]+c[v]X/3, T_v=V_v.grad-1,
 D_a(v)={u in R_a:T_v u in R_a in distributions}.

Let C_0 be the fixed jointly normalized coupling of proof 168. For a fixed zeta in Y_a define L_(v,zeta)=T_v+C_0+c[.]zeta, with its scalar/remainder meaning and domain B direct-sum D_a(v).

There is a radius r_a>0 such that, for ||v||G_s<=r_a:

1. L_(v,zeta) is Fredholm of index zero on that domain.
2. There are a fixed compact map K_a on X_a and a constant C_a such that

 ||h||X_a<=C_a||L_(v,zeta)h||Y_a+||K_a h||.              (1)

3. If L_(0,zeta) is injective on B direct-sum D_a(0), a smaller radius gives isomorphisms and a uniform graph inverse bound.

For the exact moving-tail family of proof 167, with max(k,sup_I 1/ell)<q_*<1/4, the same statements hold for A_h there when h ranges in a sufficiently small H_full ball. Its base vector zeta_0 is the actual moving-tail Schur vector. If the base low A_0 is injective, there are consistent uniform low and high graph inverses. These are qualitative assertions for each fixed a. No uniform inverse as a varies is asserted. Actual injectivity, radii and inverse norms are not supplied.

## Scalar and lifted transport perturbations

Write c=c[v], tau(t)=U_2[v](0,e^t)/e^t. Proof 164 gives

 tau=c chi_0+e,
 A_v-A=(tau+c/3)partial_t+(c-tau-2tau'),                 (2)

with tau,tau' bounded by C||v||G_s and e,e' bounded by C||v||G_s e^(9t/5) sufficiently far left. The high trace statement used here depends only on v in G_s. It does not require a third axis derivative of an arbitrary R_a input.

Apply (2) to beta=J chi_0+w. The w terms are bounded G multipliers applied to w or w'. The compact transition of J chi_0 is harmless. At the inner end its remaining term is -J(e+2e'), whose squared G exponent is

 18/5-1/2=31/10>0.                                    (3)

Therefore ||A_v-A||_(B->G)<=C||v||G_s. The actual A:B->G is an isomorphism by proof 168. The Neumann series on G proves a uniform inverse for A_v on a small ball, with the same fixed B domain.

Let (B_r,B_theta) be the normalized cylinder velocity increment, including c/3 in B_r. For p(theta)=cos(theta)^2 sin(theta), put

 P_B=3B_r+(p'/p)B_theta,
 K_1=(B_r-B_r|axis)/cos(theta)^2,
 K_0=(P_B-P_B|axis)/cos(theta)^2.

The high coefficient proof in proof 166 gives

 |K_1|<=C||v||G_s,
 |K_0|<=C||v||G_s min(r^(9/5),1).                      (4)

For clarity, reflection evenness supplies the quadratic angular difference on the vertical sector. The sector H^(25/4) bounds and Sobolev embedding control two angular derivatives after the indicated division. Away from that sector cos(theta) is bounded away from zero, and oddness of B_theta controls the cot(theta) term at the horizontal axis. The normalized central strain c(-2x/3,4y/3) has P_B=0 identically, so the free inner jet only sees the decaying K_0 in (4).

The exact lift difference is

 (Err_v-Err_0)beta=x^2y cos(theta)^2(K_1 beta'+K_0 beta).

Its squared R_a norm is the G integral of the bracket squared times

 I_a=integral_0^(2pi)|cos(theta)|^(8-2a)sin(theta)^2dtheta.

This is finite for a<9/2. The same decomposition of beta and (3) therefore prove

 ||Err_v-Err_0||_(B->R_a)<=C_a||v||G_s.                 (5)

This explicitly checks the changed output weight. An inclusion from the old low input space would not have established (5) on all of B.

## Remainder energy and maximal domain

Let mu'=-17/2 for t<0 and -37/20 for t>0. The physical energy coefficient is kappa_v=1+div(V_v)/2+V_v.grad(log w_a)/2. Since div U[v]=0, its exact change is

 kappa_v-kappa_0=c/3+(mu'/2)B_r+a tan(theta)B_theta.     (6)

The divided coefficient bounds of proof 155 control the right side by C_a||v||G_s. The continuous radial weight has no interface measure at r=1. V171 and proof 168 give kappa_0-b_plus>=m_*=55267/50000. Shrink the radius so that

 kappa_v-b_plus>=m_*/2.                                (7)

The field V_v is globally C1 and Lipschitz, tangent to the two axes, and of at most linear growth. Its global flow defines the group e^(-s)f(Phi_s) on R_a. Weighted change of variables and (7) give forward norm at most e^(-m_*s/2). Strong continuity follows from the dense compact smooth core. The generator is exactly the maximal distributional T_v: pairing with transported compact tests proves the integrated group identity in both directions. Thus T_v is invertible with

 ||T_v^(-1)||_(R_a->R_a)<=2/m_*=100000/55267.            (8)

This rational bound is conditional on the qualitative radius in (7). It is not a certified radius or a bound for the coupled inverse.

Angular graph cutoffs have bounded T_v derivatives because B_theta and the background angular field vanish at the axes. Logarithmic radial cutoffs do also. Dominated convergence removes their end strips. On the remaining compact set, Friedrichs approximation for C1 coefficients gives graph convergence. Consequently the exact energy identity extends to D_a(v), including inputs without classical axis traces.

Apply the fixed-background Garding theorem of proof 168 with epsilon=m_*/4. It supplies a fixed compact K on R_a and, for every t in [0,1],

 (m_*/4)||u||R_a<=||(T_v+t C_R)u||R_a+||K u||R_a.       (9)

Indeed kappa_v-t b_plus>=m_*/2+(1-t)b_plus, and the compact error from the form is bounded by ||Ku||||u||. Since C_R is bounded on R_a, (9) also controls the T_v graph norm. For each fixed v, the path t->T_v+t C_R has its one fixed domain D_a(v), stays upper semi-Fredholm and begins at an isomorphism. The local index constancy argument of proof 44 then gives Fredholm index zero throughout. No common domain for different v is assumed.

## Full block and the fixed compact map

In the scalar/remainder coordinates the operator is

 [A_v beta+Gamma_C(E beta+u)+c[E beta+u]zeta_1,
  (Err_v+C_R E)beta+(T_v+C_R)u+c[E beta+u]zeta_2].       (10)

The lower triangular part has diagonal blocks A_v and T_v+C_R, hence index zero. Its lower left entry is bounded by (5) and proof 168. The scalar row Gamma_C is Hilbert-Schmidt on X_a by proof 168, and c[.]zeta is rank one. Thus (10) is Fredholm of index zero.

Solve its first row with the uniform scalar inverse and use (9) on its second row. This gives (1) with a fixed multiple of the compact map

 h=E beta+u -> (Gamma_C h,c[h],K u).                    (11)

If base injectivity holds, suppose no smaller ball admits a uniform lower bound. Choose v_n->0, ||h_n||X_a=1 and L_(v_n,zeta)h_n->0. A weakly convergent subsequence in X_a has a strongly convergent image under (11). Equations (2),(5) pass the bounded scalar and lift terms to the limit. For the unbounded transport use distributional integration by parts: V_vn->V_0 in C1 on every compact set, while u_n is uniformly L1 there. The latter follows from local integrability of w_a^(-1), including at both axes and the origin. Hence the distributional limit h satisfies the base equation. Its second row places its remainder in D_a(0). Base injectivity forces h=0, and (1) now contradicts the unit norms. This gives the uniform low bound; solving the second row recovers the graph term. Index zero gives surjectivity.

## Moving-tail extension in the new low spaces

Use the exact quantities rho_ell=rho_0+z_ell, n(ell), m(ell), M(ell), ell(h) and zeta_ell of proof 167. Their algebraic definitions are unchanged. The normalized velocity from z_ell has a smooth strain-subtracted coefficient which is O(r^2) at0 and O(r^(q_*-1)) at infinity, with every fixed cylinder derivative. Its inner quotient by a_H is integrable because 2-9/5>0. These estimates are linear in |ell-ell_0| and hold for parameter derivatives. Thus it satisfies every coefficient and trace estimate used in (2)-(7).

It remains to check the bounded coupling C_z f=[U[f]+chi_0 c[f]X/3].grad z_ell on the new low inputs, rather than appeal to the old input inclusion. It has zero inner density coefficient. The proof of proof 168 applies directly with outer background exponent q_* in place of k. The axis evaluation exponent is q_*-163/40, so its squared G exponent is 2(q_*-1)<0. The comparable-annulus remainder coefficient is O(r^(q_*-1)). The separated Hilbert-Schmidt outer integral is integral_1^infinity r^(2q_*-3)dr. Every inner-output estimate vanishes near0; the compact cutoff transition has bounded constants. For jet inputs the exact moment formulas still use the same B decay q_B=123/40>2, and give the same squared outer exponent 2(q_*-1). Consequently

 ||C_z||_(X_a->Y_a)<=C_a|ell-ell_0|,                   (12)

with smooth operator-norm dependence on ell. This proof uses only the replaced first-axis-trace origin argument for general R_a inputs, not a third derivative.

Proof 167 proves zeta_ell smooth in the fixed high target Y_H. The continuous embedding Y_H->Y_a from proof 168 therefore implies

 ||zeta_ell-zeta_0||Y_a<=C_a|ell-ell_0|.                (13)

This use of the inclusion has the valid direction, since the input here is a fixed high-target vector. The exact relation n(ell(h))=c[h] and n'>=3 bounds |ell(h)-ell_0| by C||h||H_full. The full transport increment is the sum of the normalized velocities of h and z_ell(h), since

 3(ell(h)-ell_0)=c[h]+c[z_ell(h)].                      (14)

The exact decomposition is

 A_h=T_total(h)+C_0+c[.]zeta_0+D_h,
 D_h=C_zell(h)+c[.](zeta_ell(h)-zeta_0).                (15)

Equations (12),(13) give ||D_h||_(X_a->Y_a)<=C_a||h||H_full. Absorb this small bounded term in (1). The same-domain path replacing D_h by tD_h preserves the graph compact estimate and proves index zero for (15). Its high counterpart is already proved in proof 167.

If the base A_0 is injective on the new low domain, high-to-low embedding proves base high injectivity. The preceding fixed-coupling inverse and the high inverse theorem give uniform Q_h for the first three terms in (15). On a smaller ball, ||D_h Q_h||<1/2 in both targets. Hence

 A_h^(-1)=Q_h(I+D_h Q_h)^(-1)

gives the two graph inverses. High outputs lie in the low domain and satisfy the identical global distributional equation, so low uniqueness identifies their values on Y_H.

## Scope and dependencies

This proof transfers the actual perturbed operators to each specified weaker low realization. The changed scalar domain, energy coefficient, coupling input, canonical distributional meaning and high-to-low inclusion have each been checked. The nonlinear low/high difference estimate is a separate assertion, proved in proof 172. Together they permit the same abstract two-norm iteration, but actual injectivity and every numerical smallness condition remain open.

Dependencies: topics123,152,155,164-168; V171's original-data global coefficient certificate; the maximal-domain and Fredholm arguments explicitly described above. No finite-dimensional singular value is used. The exact-rational checker records the endpoint and margin arithmetic only; it does not replace the analytical proof.

Verdict: CONFIRMED, with the explicit base injectivity condition for the inverse assertions.
