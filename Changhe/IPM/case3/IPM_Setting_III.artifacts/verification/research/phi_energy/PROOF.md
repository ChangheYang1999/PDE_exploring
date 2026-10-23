# Potential energy identity at a nondegenerate source

Status: CONFIRMED after independent derivation/checking and completed Opus 5.5 review 10. Date: 2026-10-20. The actual returned model was claude-opus-5-5; the review is in ../../evidence/opus_review_10/answer.md. Its suggestions were independently checked.

## Statement and assumptions

Let c_l>1, rho_b and U_b be smooth, div U_b=0, and V_b=c_l X+U_b. Let Phi be a real compactly supported smooth function and put h=-Delta Phi. Then the canonical velocity of h is

    psi[h]=Phi_x, U[h]=(-Phi_xy,Phi_xx).

This follows directly from the Poisson equation, decay and canonical uniqueness. Define

    L0 h=V_b dot grad h-h+U[h] dot grad rho_b,
    S(U_b)=(DU_b+DU_b^T)/2,
    M=(1+2c_l)I+S(U_b)+[[rho_b,y,-rho_b,x/2],[-rho_b,x/2,0]].

Then

    -integral (L0 h) Phi = integral grad Phi^T M grad Phi.       (1)

If the background satisfies the primary origin identities, with c=1-c_l and a0=rho_b,y(0), then

    M(0)=diag(3c_l+a0,c_l+2).                                 (2)

Consequently this matrix is positive definite at the source exactly when a0>-3c_l. If a0<-3c_l, the quadratic form in (1) takes negative values on suitable compactly supported test potentials, including the even-x/odd-y parity class. No sign throughout the plane is inferred from (2).

Dependencies: the canonical inverse uniqueness in ../inverse/PROOF.md and origin relations in ../origin/PROOF.md. Compact support of Phi makes every integration by parts below legitimate. Extensions to noncompact potentials require their own decay and boundary estimates.

## Proof of the identity

Since div V_b=2c_l and h=-Delta Phi,

    integral (V_b dot grad h) Phi
      = integral Delta Phi [2c_l Phi+V_b dot grad Phi].

The first term is -2c_l integral |grad Phi|^2. A second integration by parts gives

    integral Delta Phi (V_b dot grad Phi)
      = -integral grad Phi^T S(V_b) grad Phi
           +(1/2) integral div V_b |grad Phi|^2
      = -integral grad Phi^T S(U_b) grad Phi.

Also -integral h Phi=-integral |grad Phi|^2. Finally,

    integral Phi [-Phi_xy rho_b,x+Phi_xx rho_b,y]
      = integral [rho_b,x Phi_x Phi_y-rho_b,y Phi_x^2].

To see the cancellation in the last step, integrate the first summand in y and the second in x; their terms containing Phi Phi_x rho_b,xy cancel. Combining the three formulas proves (1).

At the source DU_b=diag(-c,c) and grad rho_b=(0,a0). Substituting c=1-c_l gives (2). If its first eigenvalue is negative, it remains negative in a small neighborhood. Choose Phi=chi(X) cos(Kx), with a fixed cutoff chi supported there. The leading term of the energy as K tends to infinity is K^2 integral M11 chi^2 sin^2(Kx), which is negative; the remaining terms are O(K) or O(1). To preserve the required parity, take chi even in x and odd in y, nonzero and supported symmetrically in this neighborhood. Phi is then even in x and odd in y and the argument is unchanged.

## Scope: parameter coupling and infinity

For a perturbation of a primary exact profile, the change of c_l is c[h]=-psi[h]_xy(0), a separate functional. The full linearization is Lh=L0h+c[h]G, where G=X dot grad rho_b. Identity (1) alone does not control that term, the scaling direction, or any nonlinear derivative loss. For the compact-potential test above, c[h]=-Phi_xxy(0), visibly not continuous in the H^-1 norm of h.

The growth class gives grad rho_b=O(r^(gamma-1)), with gamma possibly larger than p=1/c_l. The established leading Holder limit and U_b=O(r^p) do not by themselves give grad rho_b or DU_b=O(r^(p-1)). The density-gradient entries already tend to zero from gamma<1. At the time of the initial audit, the remaining gap for M -> (1+2c_l)I was S(U_b)->0. For an IPM background the antisymmetric part also tends to zero because curl U_b=-rho_b,x; thus this limit of M is equivalent to DU_b->0, which was not supplied by those preliminary estimates. The construction in ../far_field_derivative_caveat/PROOF.md isolates this missing information without satisfying the transport equation. Under the actual scaling rho_lambda(X)=lambda rho(X/lambda), U_lambda(X)=lambda U(X/lambda), one has M_lambda(X)=M(X/lambda). Hence the infimum of its smallest eigenvalue over the whole plane is scale invariant whenever defined.

Verification also includes three exact polynomial/Gaussian integrations in verification/exact_gaussian_tests.json. The Gaussian test potentials have rapidly decaying derivatives, and polynomial backgrounds make all boundary terms vanish. The tests check coefficients and signs; the integration-by-parts proof is the mathematical justification.

Update 2026-10-20: result32, ../local_ipm_continuation/PROOF.md, now proves all-order symbol bounds from the exact primary profile assumptions, independently reviewed at16:27. Therefore DU_b=O(r^(p-1)) for every exact primary background, and M=(1+2c_l)I+O(r^(p-1)) follows. No Hdyn assumption is needed. The nontransport density countertest remains valid in its stated class and does not contradict the new consequence of the coupled equation. See also ../transport_coefficient/PROOF.md, Section5.
