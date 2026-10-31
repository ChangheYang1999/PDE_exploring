# Amplitude normalization and the Euler profile residual

Status: proved identities under the stated hypotheses. The numerical application is a comparison of saved vectors, not a proof that either vector represents an Euler solution.

## Statement, hypotheses and notation

Fix c in (2/5, 1/2) and omega > 0. Let J be the matrix with J(x,y,z)=(-y,x,0). Let U:R^3 -> R^3 be a C^2 vector field, and suppose there are C>0 and beta>1/2 such that |D^j U(y)| <= C(1+|y|)^(-beta-j) for j=0,1,2. Matrix derivatives have entries (DU)_ij=partial_j U_i. Define the decaying Newton pressure

P_U(y) = (1/(4 pi)) integral_R^3 tr((DU(z))^2)/|y-z| dz.

The hypotheses ensure absolute convergence and the classical pressure equation, as proved in ../pressure_consistency/PROOF.md. Divergence freedom may additionally be assumed for the incompressible Euler interpretation; it is not needed for the scaling identities below. Write

L(U)(y) = (1-c)U(y) + DU(y)(c y-omega Jy) + omega JU(y),

N(U)(y) = DU(y)U(y) + grad P_U(y),

R(U) = L(U)+N(U).

For every scalar s>0, amplitude scaling U_s(y)=sU(y) satisfies

P_{U_s}=s^2 P_U,  L(U_s)=s L(U),  N(U_s)=s^2 N(U),

R(U_s)=s R(U)+s(s-1)N(U).

On any measure space and for any vector-valued norm for which R(U) and N(U) are finite, the exact identity implies

max(0, s|s-1| ||N(U)||-s||R(U)||) <= ||R(U_s)||
    <= s||R(U)||+s|s-1| ||N(U)||.

Here the same norm and measure are used on all terms. These inequalities do not apply without modification to a residual ratio whose denominator or measure is changed along with U.

In contrast, for each lambda>0 define the spatial profile dilation

V_lambda(y)=lambda U(y/lambda).

Then

P_{V_lambda}(y)=lambda^2 P_U(y/lambda),

R(V_lambda)(y)=lambda R(U)(y/lambda).

If a fixed-parameter coefficient representation is linear, U_a=sum_j a_j Phi_j, replacing every coefficient by s a_j implements U_s at the same spatial coordinates. It does not in general implement V_lambda. No claim that the two transformations differ for every special U is required.

## Proof

The derivative DU_s=sDU, so its pressure source is s^2 tr((DU)^2). Absolute convergence permits multiplication of the Newton integral by this constant. Thus its pressure and pressure gradient scale by s^2. Each term in L is linear in U. Both DU U and grad P_U scale quadratically. Summing these identities proves the residual formula. The upper norm inequality is the triangle inequality. Applying the reverse triangle inequality with the nonlinear correction as the first summand gives the lower inequality, and a norm is nonnegative.

For the spatial dilation, DV_lambda(y)=DU(y/lambda), so its source at y equals the original source at y/lambda. In the absolutely convergent Newton integral use z=lambda x. The volume contributes lambda^3 and the denominator contributes lambda, yielding lambda^2 P_U(y/lambda). Its gradient is lambda grad P_U(y/lambda). Also c y-omega Jy=lambda(c(y/lambda)-omega J(y/lambda)). Substitution into each of the three linear terms and the convective term shows that every term of R(V_lambda)(y) is lambda times the corresponding original term at y/lambda. Finally, linearity of the coefficient representation gives U_{sa}(y)=sU_a(y) directly.

## Normalization and scope of the application

Suppose a leading-tail map a -> F_a is also linear at the fixed parameters, and q=||F_a|| is finite and positive. Dividing every coefficient by q changes the leading-tail norm to one. It is an amplitude normalization. The residual formula above, with s=1/q, shows why the raw optimizer residual and the residual after this normalization cannot be identified merely from the normalization rule. If R(U)=0 and N(U) is nonzero, then R(U_s) is nonzero for s different from one. This last sentence is conditional and does not assert the existence of an exact profile in this campaign.

The production objective also contains weights and additional rows. The proof makes no homogeneity claim for that complete objective. It does not infer a pressure error bound, stationarity, or a physical-residual improvement from coefficient scaling. V727 compares actual saved raw and normalized coefficient vectors for two fixed-parameter PROFILE runs and identifies which state each stored diagnostic uses. No independent pressure solve for those two runs is claimed.

Dependencies: the Newton-pressure existence and uniqueness argument in ../pressure_consistency/PROOF.md, the chain rule, a linear change of variables, linearity, and the triangle and reverse triangle inequalities. No formal proof has been built.
