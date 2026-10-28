# The full axis and remainder block under small transport perturbations

## Statement and exact realization

Use the fixed background, spaces, cutoffs and canonical velocity of topics150,155,158 and164. Write

 H_full=B_H direct-sum X_s,
 Y_full=Gamma_H direct-sum X_s,
 D_full(g)=B_H direct-sum D_g,
 D_g={u in X_s:T_g u in X_s in distributions}.

The norm on H_full is the sum of the displayed component norms; D_full(g) has the additional norm ||T_g u||X_s. Let h=E beta+u. The background normalized coupling C_ren, its scalar row Gamma_C, and its remainder C_R are fixed. In particular C_R h=C_ren h-E Gamma_C[h]. Set

 Err_g beta=T_g E beta-E A_g beta,
 G_g beta=Err_g beta+C_R E beta,
 S_g=T_g+C_R.

For any fixed zeta=(zeta_1,zeta_2) in Y_full, define

 L_(g,zeta)(beta,u)=
 (A_g beta+Gamma_C[h]+c[h]zeta_1,
  G_g beta+S_g u+c[h]zeta_2).                            (1)

The case zeta=0 is the normalized coupling realization. The fixed moving-tail vector of topics83 and123 is another allowed choice. For sufficiently small ||g||G_s, the following hold:

 1. G_g:B_H->X_s is bounded, and

 ||G_g-G_0||_(B_H->X_s)<=C||g||G_s.                    (2)

 2. L_(g,zeta):D_full(g)->Y_full is Fredholm of index zero.

 3. There are a fixed compact map K:H_full->W and a constant C, independent of g in a sufficiently small ball, such that

 ||(beta,u)||H_full<=C||L_(g,zeta)(beta,u)||Y_full
                                      +||K(beta,u)||W. (3)

 4. If L_(0,zeta) is injective on D_full(0), then on a smaller ball every L_(g,zeta) is an isomorphism and

 ||beta||B_H+||u||X_s+||T_g u||X_s
                   <=C_inv||L_(g,zeta)(beta,u)||Y_full, (4)

with a constant independent of g. The base injectivity is an additional hypothesis, not a conclusion of this result. The radius and constants are qualitative.

## The lifted transport difference

Let B=(B_r,B_theta) be the normalized cylinder velocity increment of proof 155, including c[g]/3 in B_r. Direct differentiation of E beta=r^3 p(theta) beta(t) gives

 (T_g-T_0)E beta
 =r^3{p B_r beta'+[3p B_r+p' B_theta]beta}.             (5)

Near the vertical axis define p_g=3B_r+(p'/p)B_theta by its Sobolev extension. Proof 155 proves the needed H^sigma bound for this expression after its explicit smooth strain part is removed. Proof 164 and the divergence identity show

 B_r|axis=tau_g+c[g]/3,
 p_g|axis=c[g]-tau_g-2tau_g'.                           (6)

Thus the scalar row of (5) is exactly (A_g-A_0)beta. The equality of traces is meaningful at these orders: the cofactor coefficients have H^sigma regularity, while the scalar factors beta have the regularity stated in B_H. No trace of an arbitrary L2 function is used.

First take beta=a v. Dividing (5) by b gives

 p B_r[v'+(a'/a)v]+[3p B_r+p' B_theta]v.                (7)

The scalar functions v,v' on the cylinder have H^sigma regularity, and v belongs to H^(sigma+1). The variable-order product inequality of topics156 and161, the bound s<=sigma, and proof 155 bound (7) in H^{s(.)} by C||g||G_s||v||H^(sigma+1). The explicit smooth nondecaying strain is a bounded multiplier. On the vertical sector, division by p gives the same expression with the H^sigma coefficient p_g. The ordinary H^sigma algebra estimate gives its cofactor bound. Subtracting E(A_g-A_0)beta preserves both norms by proof 164, and its exact cofactor trace is zero by (6).

For the free input beta=J chi_0, its derivative is supported in a fixed compact radial interval and is handled by the same product bounds. Far left beta=J. The normalized central strain is

 c[g](-2x/3,4y/3).

Its action on x^2 y is zero exactly. Consequently its contribution to (5) vanishes identically there. Only the strain-subtracted Z of proof 155 remains. The stronger inner weighted estimate proved with (8) in proof 164 gives

 ||chi_- Z/a||H^s+
 ||chi chi_- Z/a||H^sigma+
 ||chi chi_- Z_theta/(a cos(theta))||H^sigma
                                  <=C||g||G_s.        (8)

The factors in (5), divided by b, are therefore bounded in the required bulk and cofactor norms, even for this free jet. On compact transition intervals all weights are bounded; far right beta is zero. The scalar subtraction is bounded by (11)-(12) of proof 164. Its zero trace again follows from (6). Hence

 ||Err_g-Err_0||_(B_H->X_s)<=C||g||G_s.

Adding the fixed bounded C_R E proves (2). Notice that this argument never divides a general zero-trace function by a further power of cos(theta). Membership in X_s requires only the stated cofactor and its zero trace.

## Fredholm property on the varying graph domains

Proof 164 gives an isomorphism A_g:B_H->Gamma_H on a sufficiently small ball. Proof 159 gives the unconditional Fredholm index-zero property of S_g:D_g->X_s on that ball. The lower triangular map

 M_g(beta,u)=(A_g beta,G_g beta+S_g u)

factors as

 M_g=[[I,0],[G_g A_g^(-1),I]] diag(A_g,S_g).

The first factor is an isomorphism of Y_full, with bounded inverse obtained by changing the sign of its lower off-diagonal entry. Thus M_g has index zero. The first-row perturbation Gamma_C[E beta+u] is compact on B_H direct-sum X_s by topics123 and140, hence also compact on D_full(g). The functional c is bounded on H_full and its product with zeta has finite rank. Adding these two compact maps gives (1) and proves item2. This argument uses a fixed domain only for each individual g; it does not presume that the different D_g coincide.

## A fixed compact error map

Let f=L_(g,zeta)(beta,u). The uniform scalar inverse bound of proof 164 applied to the first row gives

 ||beta||B_H<=C[||f_1||Gamma_H+||Gamma_C[h]||Gamma_H
                                                +|c[h]|]. (9)

The uniform remainder estimate of proof 158, applied to the second row, gives

 ||u||X_s<=C[||f_2||X_s+||G_g beta||X_s+|c[h]|]
                                                 +||K_R u||. (10)

Here K_R is fixed and compact on X_s. The constants absorb the fixed norm of zeta and the uniformly bounded norm of G_g. Combining (9)-(10) proves (3) with K the finite direct sum, with suitable fixed factors, of

 (beta,u) -> Gamma_C[E beta+u],
 (beta,u) -> c[E beta+u],
 (beta,u) -> K_R u.

Every component is compact on H_full. In particular no g-dependent compactness assertion is being used.

## Uniform inverse from one base injectivity hypothesis

Suppose L_(0,zeta) is injective and item4 fails. Then there are g_n->0 in G_s and (beta_n,u_n) in D_full(g_n) with H_full norm one and images f_n->0 in Y_full. Take a weakly convergent subsequence in H_full, with limit (beta,u). Its image under the fixed K converges strongly.

The first row passes to the limit in Gamma_H: A_0 is bounded on B_H, (A_(g_n)-A_0)beta_n tends strongly to zero by (3) of proof 164, and the two compact terms converge. Thus the first row of L_(0,zeta)(beta,u) vanishes. In the second row G_(g_n)beta_n-G_0 beta_n tends strongly to zero by (2). The perturbation T_(g_n)u_n-T_0u_n tends to zero in distributions, because its coefficients tend to zero in C1 on compact annuli and u_n is bounded there in H^{s(.)}, with s_min>2. The remaining coupling and finite-rank terms pass to the distributional limit. Hence the second row also vanishes in distributions.

Its right side expresses T_0u as an element of X_s, so u belongs to D_0. The base injectivity now implies beta=u=0. Therefore K(beta_n,u_n)->0. Applying (3) contradicts the unit H_full norm. This proves a uniform lower bound. Each operator already has index zero, so injectivity gives surjectivity. Finally the second row of (1) expresses T_g u in terms of f and bounded maps on H_full, yielding the graph term in (4).

## Scope and compatibility

This proves the full block counterpart of proof 159 for a fixed background coupling and a fixed rank-one vector. It covers all high-space correction velocities in a sufficiently small ball, since the high full space embeds continuously into G_s. It proves neither the base injectivity nor a numerical inverse constant. If a corresponding low inverse is independently known, the continuous high-to-low embeddings and identical distributional equations identify the high inverse with its restriction by uniqueness.

The theorem retains the free scalar coefficient J. Imposing J=0 is a separate restriction, with the previously established index and compatibility issue. Dependence of the background profile and of zeta on a moving far-field exponent is also separate; it is not hidden in the fixed-coupling operator (1).
