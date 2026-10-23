# Pointwise reconstruction of a saved stream interpolant

Written on 2026-10-21 UTC before the evaluator. This document proves the algebraic identities used in a finite comparison. It makes no claim that an interpolated stream is the canonical inverse or that a nearby exact profile exists.

## Statement, inputs and scope

Fix positive L and kappa, ell>1, distinct real nodes t_i, and real values V_ij. At each mode j let P_j be the unique polynomial of degree less than the number of nodes with P_j(t_i)=V_ij. The exported data specify

    s=(t+1)/2, w=1-s, r=L sqrt(s)/(2w)^kappa,
    psi_I(r,theta)=r^2 w S(t,theta),
    S(t,theta)=sum_j P_j(t) sin(m_j theta),  m_j=2(j+1).

These definitions specify an actual function for r>0, whether or not it is smooth at zero. The checkpoint separately specifies a smooth density rho by the finite Q formula in the shared-sampling proof. We compare the exact polynomial interpolant of the exported binary numbers with the independently implemented canonical inverse U_C of that density. The export convention and source hashes must agree. This interpolant need not coincide bit for bit with the producer's floating-point evaluation: interpolation arithmetic and rounded differentiation matrices can differ. Comparisons with the producer's printed numbers have their printed precision as a limit.

## Interpolation and its derivatives

Define b_i=1/prod_{h!=i}(t_i-t_h). At a point t different from every node put

    D_k=sum_i (-1)^k k! b_i/(t-t_i)^(k+1),
    N_{k,j}=sum_i (-1)^k k! b_i V_ij/(t-t_i)^(k+1), k=0,1,2.

The barycentric interpolation identity gives P_j=N_{0,j}/D_0. Differentiating N_{0,j}=D_0 P_j once and twice gives

    P'_j=(N_{1,j}-D_1 P_j)/D_0,
    P''_j=(N_{2,j}-D_2 P_j-2D_1 P'_j)/D_0.

The barycentric identity itself follows by writing the Lagrange interpolation polynomial over the common denominator prod_i(t-t_i). Applying the same formula to the constant polynomial shows sum_i b_i prod_{h!=i}(t-t_h)=1, proving the denominator identity and hence the quotient. Thus no assumption about a special distribution of nodes is involved. The evaluator selects points away from the nodes; node limits can be handled separately but are not needed for these six comparisons.

## Polar and Cartesian fields

Let D=r d/dr. Taking logarithms of the radial map yields

    h=D s=2sw/(w+2 kappa s),
    k=D^2 s=h^2 [1/s-1/w-(2 kappa-1)/(w+2 kappa s)].

The second identity is h times d_s h. Since D w=-h and D t=2h, direct differentiation gives

    U_{I,r}=-psi_{I,theta}/r=-r w S_theta,
    U_{I,theta}=psi_{I,r}=r[(2w-h)S+2wh S_t].

Consequently

    U_{I,1}=U_{I,r} cos(theta)-U_{I,theta} sin(theta),
    U_{I,2}=U_{I,r} sin(theta)+U_{I,theta} cos(theta).

For the Laplacian use Delta=r^-2(D^2+partial_theta^2). If A=wS, then

    A_s=-S+2wS_t,  A_ss=-4S_t+4wS_tt,
    D^2 A=k A_s+h^2 A_ss.

Expanding (D^2+4D+4)A+A_thetatheta therefore proves

    Delta psi_I=(4w-4h-k)S
        +(8wh-4h^2+2wk)S_t+4wh^2 S_tt+w S_thetatheta.

The Poisson defect of this interpolant at a point is -Delta psi_I-rho_x. It is a pointwise quantity; no claim about a global norm or the source of all endpoint defects follows from measuring it.

## Residual difference and denominators

Hold the density and gradient g=grad rho fixed. For either velocity U define

    R(U)=(ell X+U).g-rho,
    N_f(U)=|(ell x+U_1)g_x|+|(ell y+U_2)g_y|+|rho|,
    N_v(U)=|rho|+|x g_x+y g_y|+|U_1 g_x+U_2 g_y|.

Then exactly

    R(U_I)-R(U_C)=(U_{I,1}-U_{C,1})g_x+(U_{I,2}-U_{C,2})g_y.

This identity distinguishes both component contributions. It does not permit identifying delta U_2 with delta R/g_y without also controlling delta U_1 g_x. The denominators depend on the velocity too; agreement of rho and its gradient alone does not prove identical N_f or N_v. Their difference bounds, from ||a|-|b||<=|a-b|, are

    |N_f(U_I)-N_f(U_C)| <= |delta U_1 g_x|+|delta U_2 g_y|,
    |N_v(U_I)-N_v(U_C)| <= |delta U.g|.

These inequalities will be checked along with the exact residual identity. No residual denominator is floored or removed in this comparison.

## Verification protocol and dependencies

The interpolation is tested on full-degree polynomials at irregular rational nodes, with independently evaluated exact derivatives. The polar velocity and Laplacian formulas are tested against direct multiprecision Cartesian derivatives of the explicit rational stream obtained with kappa=1/2 and L=sqrt(2), so s=r^2/(1+r^2). These manufactured functions are tests of the formulas, not proposed IPM profiles. All gates run at two precisions and record every error.

At the six recorded shared-grid extrema from N=128,160,192, use their exact saved Cartesian coordinates. Evaluate the saved density with the verifier's independent multiprecision map and Chebyshev derivative, and the stream with the formulas above at two precisions. Compare density and gradient with the already recorded canonical source-primitives values, preserving their source hashes and target precision. Recompute the canonical residual from these same quantities before using it in the difference identity. Record the two velocities, both component contributions, both denominators, the Poisson defect and precision differences.

Dependencies: research/shared_sampling_inverse_audit/PROOF.md for the Q density and residual conventions; research/q_full_inverse_primitives/PROOF.md for the independent full-plane inverse; research/interpolated_inverse_regularity/export_audit/PROOF.md for binary-data and interpolation conventions. These are finite checks, not interval enclosures. A discrepancy at six points cannot establish a uniform maximum or prove that a particular endpoint derivative defect caused it.
