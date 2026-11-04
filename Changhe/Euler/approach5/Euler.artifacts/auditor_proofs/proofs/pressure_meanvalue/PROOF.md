# Canonical pressure by moving mean-value tests

Date: 2026-11-02T22:08:33Z. CONFIRMED as part of A219. This verifies the new proof in report Section 2, Lemma 2.2.

## Statement

Let U be bounded on R3, div U=0 in distributions, and U(R dot) tend to zero in distributions as R tends to infinity. Let c,omega be finite real constants, A=cI-omega J, and suppose the distributional profile equation

    (1-4c)U+omega JU+div(U tensor Ay+U tensor U)+grad P=0

holds. Here div(V tensor W)_i=partial_j(W_j V_i). Put F_ij=U_i U_j and T_ij=R_i R_j. Define G_k by

    <G_k,phi>=-sum_ij int F_ij T_ij(partial_k phi).

Then grad P=G. In particular no nonconstant harmonic pressure gradient can be added. No pressure decay or differentiability of U is assumed.

## Proof

For compact smooth phi, T_ij(partial_k phi) is locally L2 and decays like |x|^-4 at infinity. The local assertion follows from the bounded L2 multiplier. Outside a ball containing the support, differentiate the Newton kernel and integrate by parts to write it as the convolution of partial_k K_ij with phi, where K_ij=partial_i partial_j(1/(4 pi |x|)) off zero. This proves L1 integrability and continuity in test-function seminorms, so G is well defined.

Divergence of the equation gives -Delta P=partial_i partial_j F_ij: the two rotation contributions cancel, and div U removes the scalar drift term. The multiplier identity T_ij Delta=-partial_i partial_j shows Delta G_k=Delta partial_k P. Thus h_k=partial_k P-G_k is a harmonic distribution and has a smooth harmonic representative.

Boundedness and distributional convergence imply int U(Rz)psi(z) dz tends to zero for every L1 test psi. Indeed approximate psi in L1 by compact smooth tests and use the common L-infinity bound. The same conclusion holds for psi_R converging to psi in L1.

The scaled equation reads

    (grad P)(Rz)=-(1-c)U_R-omega JU_R-(Az dot grad)U_R-R^-1 div(U_R tensor U_R).

Against a test psi this gives a term int U_R dot Lambda psi, with Lambda a fixed first-order operator whose coefficients are linear in z, plus a term bounded by C R^-1 ||U||_infinity^2 ||grad psi||_1. Homogeneity of T_ij gives

    <G_k(R dot),psi>=-R^-1 sum_ij int F_ij(Rz) T_ij(partial_k psi)(z) dz.

Fix x and choose a radial compact smooth phi with integral one. Harmonic mean values imply

    h_k(x)=int h_k(x+Rz)phi(z) dz=<h_k(R dot),phi(dot-x/R)>.

For psi_R=phi(dot-x/R), Lambda psi_R converges in L1 to Lambda phi. The U term therefore tends to zero. The quadratic derivative term is O(R^-1). The canonical term is also O(R^-1), because T commutes with translations and its L1 test norm is unchanged. Hence h_k(x)=0. Since x was arbitrary, grad P=G.

The argument fixes a given finite rotation rate but does not estimate a rotation-dependent remainder: the eventual pressure kernel estimates involve only U. This is why the subsequent energy constants can be independent of omega at fixed c and velocity bounds.

## Dependencies and verification

Inputs: the L2 Riesz multiplier, its off-support differentiated Newton kernel, Weyl's lemma and harmonic mean values. All scaling factors and signs were checked directly. This is an alternative to the tempered-harmonic-polynomial proof A031, and also works for Theorem W's distributional momentum equation. It does not imply pointwise decay of pressure.
