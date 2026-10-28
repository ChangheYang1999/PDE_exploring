# Uniform low estimates for the full perturbed block

## Statement and fixed spaces

Use the exact normalized modal background and the fixed cutoffs of topics44,49,155,164 and165. Put a_w=17/4, eta=5/4 and

 R=L2_P(w dX), w=|x|^(-17/2) max(1,r)^(29/4),
 G=L2(g(t)dt), g(t)=exp(-t/2) for t<0 and exp(27t/4) for t>=0.

The parity P is even in x and odd in y. The scalar space B is the fixed space in proof 44, defined by the background integrating factor H. In particular it is not redefined for each perturbation. The actual background scalar operator A:B->G is an isomorphism. Set E beta=x^2 y beta(log r) and X_0=B direct-sum R, Y=G direct-sum R. The notation X_0 records the coordinates of E beta+u.

For g_1 in the coefficient space G_s of proof 155, put c=c[g_1], V_(g_1)=V+U[g_1]+cX/3 and T_(g_1)=V_(g_1).grad-1. Its remainder domain is

 D_R(g_1)={u in R:T_(g_1)u in R in distributions}.

Fix the background coupling C_ren, its scalar row Gamma_C and its remainder C_R. Fix any zeta=(zeta_1,zeta_2) in Y. Define A_(g_1), Err_(g_1) and G_(g_1) as in proof 165, now on the low scalar domain, and define

 L_(g_1,zeta)(beta,u)=
 (A_(g_1)beta+Gamma_C[E beta+u]+c[E beta+u]zeta_1,
  G_(g_1)beta+(T_(g_1)+C_R)u+c[E beta+u]zeta_2).          (1)

There is a radius r_*>0 such that for ||g_1||G_s<=r_*:

 1. A_(g_1):B->G is an isomorphism with a uniform inverse bound;
 2. ||Err_(g_1)-Err_0||_(B->R)<=C||g_1||G_s;
 3. L_(g_1,zeta):B direct-sum D_R(g_1)->Y is Fredholm of index zero;
 4. there are a fixed compact K:X_0->W and a constant C such that

 ||(beta,u)||X_0<=C||L_(g_1,zeta)(beta,u)||Y+||K(beta,u)||W. (2)

If, additionally, L_(0,zeta) is injective on B direct-sum D_R(0), then a smaller radius gives an isomorphism for every g_1 in the ball and

 ||beta||B+||u||R+||T_(g_1)u||R
                       <=C_inv||L_(g_1,zeta)(beta,u)||Y. (3)

The radius and constants are qualitative. Base injectivity remains an additional hypothesis. No restriction J=0 is imposed.

## An equivalent description of the scalar domain

For the fixed background,

 B={beta=J chi_0+w_0:J real, w_0 in H1(G)},
 ||beta||B equivalent to |J|+||w_0||G+||w_0'||G,          (4)

where H1(G) means that the function and its distributional first derivative belong to G. To check this equivalence, use beta=Hz from proof 44. At the left end H=1+O(exp(2t)), H'=O(exp(2t)), while H and its reciprocal are bounded. Thus beta-J and its derivative in G are equivalent to z-J and z' in L2(exp(-t/2)dt), with an additional bounded multiple of |J|. The terms J(H-1) and JH' are integrable because 4-1/2>0. At the right end H'/H is bounded and H^2 g is comparable to exp(2(k+3/8)t), exactly the weight omega of that topic. The product rule gives the equivalence of both function and derivative terms there. Compact transition intervals have bounded positive coefficient comparisons.

Conversely, (4) produces z=beta/H with z' in L2(omega), z-J in the negative-end weighted space, and z in the positive-end weighted space. Since omega^(-1) is integrable, the derivative condition gives limits at both ends by Cauchy-Schwarz. The weighted function conditions force these limits to be J and0. Thus z has exactly the endpoint conditions in proof 44. This proves both inclusions in (4), including the domain and the continuous free coordinate.

## Scalar perturbation on B

Proof 164 proves, with tau=U_2[g_1](0,exp(t))/exp(t),

 tau=c chi_0+e,
 A_(g_1)-A=(tau+c/3)partial_t+(c-tau-2tau').              (5)

It also proves uniform boundedness of tau,tau' by C||g_1||G_s and the stronger inner estimate chi_- e/a in H^(31/4), where a=exp(delta t) far left and delta=9/5. Apply (5) first to w_0 in (4). Its G norm is at most C||g_1||G_s||w_0||H1(G). On J chi_0 the transition terms are compactly supported. Far left the result is exactly -J(e+2e'). This belongs to G with norm at most C|J|||g_1||G_s: e/a and e'/a are bounded there, and a^2 g=exp((2delta-1/2)t) is integrable. Therefore

 ||A_(g_1)-A||_(B->G)<=C_A||g_1||G_s.                  (6)

The Neumann series for [I+(A_(g_1)-A)A^(-1)] on G proves item1 when C_A r_*||A^(-1)||<1. This argument does not need the perturbed axis coefficients to have the same limiting exponents as the background.

## The perturbed lift on the low domain

Write B=(B_r,B_theta) for the normalized cylinder velocity increment, including c/3 in B_r. Set p(theta)=cos(theta)^2 sin(theta) and

 P_B=3B_r+(p'/p)B_theta,
 K_1=(B_r-B_r|axis)/cos(theta)^2,
 K_0=(P_B-P_B|axis)/cos(theta)^2.                        (7)

The quotients in (7) are defined by their continuous extensions at the vertical axis. They obey

 ||K_1||infinity<=C||g_1||G_s,
 |K_0(t,theta)|<=C||g_1||G_s min(exp(delta t),1).          (8)

Here is the required division argument. In the vertical sector, proof 155 gives H^(25/4) regularity for B and B_theta/cos(theta), after removing the explicit smooth strain. Two-dimensional Sobolev embedding supplies bounded second angular derivatives of P_B and B_r there. These functions are even under reflection about the vertical axis. Their differences from the axis values therefore vanish quadratically, by Taylor's formula with integral remainder. The same reasoning with the weighted inner estimate at the end of proof 164 gives a factor exp(delta t) for the strain-subtracted coefficients. The normalized central linear field c(-2x/3,4y/3) has P_B=0 identically, so it contributes nothing to K_0. It contributes a bounded constant to K_1. Away from the vertical sector cos(theta)^2 is bounded below. Near the horizontal axis the only apparent singularity is cot(theta)B_theta; C1 regularity and oddness of B_theta at that axis bound this quotient. The inner weighted estimate supplies the same exp(delta t) factor there. These observations prove (8) globally. The decay asserted for K_0 is exp(delta t), not an unproved quadratic Taylor rate for the rough input.

The exact identity is

 (Err_(g_1)-Err_0)beta=x^2 y cos(theta)^2[K_1 beta'+K_0 beta]. (9)

For beta=J chi_0+w_0, (4), (8), and the same angular integral as proof 44 give

 ||(Err_(g_1)-Err_0)beta||R
 <=sqrt(I_a) C||g_1||G_s
       (||w_0'||G+||w_0||G+|J|),
 I_a=2 Beta(1/4,3/2).                                   (10)

Indeed beta' contains only a compactly supported additional term J chi_0', while K_0 J chi_0 is in G because delta>1/4. Formula(9) first holds for smooth scalar inputs and then for every beta in B by (4) and distributional convergence. This proves item2. In particular G_(g_1)=Err_(g_1)+C_R E is uniformly bounded B->R.

## Uniform remainder energy and maximal domains

The original global certificate V086 gives kappa_w-bplus>=5/2, where bplus=(|grad rho|-rho_y)/2. For the perturbed field the exact weight change is

 kappa_(g_1)-kappa_w=c/3+(mu'/2)B_r+(17/4)tan(theta)B_theta, (11)
 mu'=-17/2 for t<0 and -5/4 for t>0.

To derive (11), use kappa=1+(div V)/2+(V.grad log w)/2. The physical divergence changes by2c/3, the radial logarithmic derivative is mu', and partial_theta log w=(17/2)tan(theta). Proof 155 bounds every term on the right by C||g_1||G_s. The divided angular bound is essential for the last term. Shrink r_* so that

 kappa_(g_1)-bplus>=5/4.                                (12)

The physical field V_(g_1) is globally Lipschitz, C1 and tangent to both axes. This follows by differentiating rB(t,theta): its physical derivative is a bounded linear combination of B,partial_t B and partial_theta B; the central expansion ensures the C1 extension at0. Its flow is complete, since its magnitude grows at most linearly. The flow argument in proof 43 now applies to each field and gives a strongly continuous group on R, with norm at most exp(-5s/4) for s>=0. Its generator is exactly the maximal distributional T_(g_1). The proof by pairing with transported tests only needs these C1 coefficients. The angular and radial graph cutoffs in proof 44 have uniformly bounded transport derivatives, by the bounds on B and B_theta/cos(theta), and compactly supported Friedrichs approximation applies away from the axes. Therefore the energy identity

 Re<T_(g_1)u,u>R=-integral kappa_(g_1)|u|^2w

holds on D_R(g_1). The pure transport inverse has norm at most4/5 on R; this numeric bound is conditional on the qualitative choice of radius giving (12), not a computed radius.

Choose once and for all epsilon=5/8 in the fixed-background Garding theorem of proof 49. For S_(g_1,tau)=T_(g_1)+tau C_R, 0<=tau<=1, it gives

 (5/8)||u||R<=||S_(g_1,tau)u||R+||K_epsilon u||R.          (13)

The compact operator is independent of g_1 and tau; multiplying it by tau only decreases its norm estimate. On the fixed domain D_R(g_1), (13) and the boundedness of C_R give the corresponding graph estimate. The upper-semi-Fredholm path argument in proof 44, starting at the transport isomorphism at tau=0, proves that S_(g_1,1) is Fredholm of index zero. No common domain for different g_1 is asserted or used.

## The complete block and its uniform inverse

The map (beta,u)->(A_(g_1)beta,G_(g_1)beta+S_(g_1,1)u) factors into the diagonal blocks A_(g_1),S_(g_1,1) followed by an invertible lower triangular target map. It is Fredholm of index zero. Proof 46 proves that Gamma_C:X_0->G is compact, and proof 44 proves that c is bounded on X_0. Adding the scalar-row compact map and the rank-one c[.]zeta proves item3.

For f=L_(g_1,zeta)(beta,u), the scalar inverse and (13) give successively

 ||beta||B<=C(||f_1||G+||Gamma_C[E beta+u]||G+|c[E beta+u]|),
 ||u||R<=C(||f_2||R+||beta||B+|c[E beta+u]|+||K_epsilon u||R).

This proves (2) with the fixed compact map

 K(beta,u)=(Gamma_C[E beta+u],c[E beta+u],K_epsilon u).     (14)

The associated graph estimate follows by solving for T_(g_1)u in the second row.

Assume base injectivity but suppose that no smaller ball admits a uniform bound without the compact term. Then there are g_n->0 in G_s and x_n=(beta_n,u_n) in the corresponding graph domains with ||x_n||X_0=1 and L_(g_n,zeta)x_n->0 in Y. Passing to a subsequence, x_n converges weakly in the Hilbert space X_0. Compactness makes Kx_n converge strongly. Equations(6) and(10) send the varying scalar and lift terms to zero in norm. For every compactly supported smooth test on the plane, integration by parts and ||V_(g_n)-V||C1->0 show (T_(g_n)-T_0)u_n->0 in distributions. Here R embeds into L1 on every compact set, including sets meeting the axes, since the reciprocal weight is locally integrable. Thus no axis-supported distribution is omitted. The fixed bounded coupling maps pass to their weak limits. Thus the weak limit x solves L_(0,zeta)x=0 distributionally. The second row then places its remainder in D_R(0); its scalar part already belongs to B. Base injectivity forces x=0. Hence Kx_n->0, and (2) contradicts ||x_n||=1. This proves a uniform X_0 bound. The graph bound follows from the equation; index zero gives surjectivity. This proves (3).

If zeta also belongs to the high target of proof 165, its low and high realizations are consistent on the high domain. Under the same base low injectivity, proof 165 supplies the high inverse on a possibly smaller ball, and low uniqueness identifies the two inverses whenever the forcing is in the high target. This observation does not assert injectivity of the actual base operator or evaluate either inverse norm.

## Dependencies and scope

The proof uses the scalar isomorphism and domain from topics38 and44, fixed coupling bounds and compactness from topics46-49, the certified original margin V086, velocity bounds from proof 155 and the weighted axis estimates from proof 164. It concerns a fixed coupling and a fixed rank-one vector. Moving backgrounds require a separate coefficient argument. The result supplies the qualitative low perturbation estimate requested in P4 for this fixed-background family.
