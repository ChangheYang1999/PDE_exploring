# The Garding inequality in the axis-subtracted remainder space

## Statement

Assume the background hypotheses (B1)-(B2) and the parameters of proof 48. In particular a=17/4, eta=5/4, 0<k<1, and rho=x^2 y b has the normalized cubic leading term and the stated annular derivative bounds. Let

 R=L2_P(w dX), w=|x|^(-2a)max(1,r)^(2a-eta),
 C_R h=[U[h]+chi0(c[h]/3)X].grad rho-E Gamma_h.

Proof 48 defines C_R as a bounded operator R->R; proof 46 defines the exact axis row Gamma. Put

 bplus(X)=(|grad rho(X)|-rho_y(X))/2.

Then for every epsilon>0 there is a compact self-adjoint operator K_epsilon:R->R such that, for every h in R,

 Re<C_R h,h>_R <= integral_R2 (bplus+epsilon)|h|^2w dX
                                 +<K_epsilon h,h>_R.      (1)

Thus the full hypothesis (E-G) of proof 44 holds. Together with topics46-48, all three nonlocal hypotheses (E0), (E-J), (E-G) follow from the stated coefficient regularity and endpoint bounds. No positive numerical transport margin or inverse norm is claimed here.

## Output tails of the coupling

We first prove that C_R can be localized in its output variable with arbitrarily small operator-norm error. Proof 48 gives

 C_R=D_near+K,

where K is compact (the separated-scale Hilbert-Schmidt part and a rank-one normalization term), and the dyadic pieces of D_near satisfy

 ||1_{2^j<=r<2^(j+1)}D_near h||_R
    <=C min(2^(2j),2^((k-1)j))
                 ||1_{2^(j-3)<r<2^(j+3)}h||_R.          (2)

The finite-overlap sum proves that its output tails at0 and infinity tend to zero in operator norm. For any compact operator, output multiplication by indicators of shrinking measurable sets also tends to zero in operator norm if the indicators tend strongly to0. Indeed approximate the compact operator by a finite-rank operator, for which this follows by applying the strong convergence to finitely many vectors. Hence the same radial-tail statement holds for C_R.

Now fix an output annulus I={r0<=r<=r1}, 0<r0<r1<infinity. We prove

 lim_(delta->0) ||1_{I,|x|<delta} C_R||_(R->R)=0.          (3)

The compact part already has this property. Only finitely many output annuli in (2) meet I, so fix one and its corresponding input h_j supported in B_j. All weight comparisons on these fixed annuli have finite constants independent of delta and epsilon0 below.

Choose a small absolute strip width epsilon0>0 and split

 h_j=h_in+h_out,
 h_in=1_{|x|<epsilon0}h_j.

For h_in use the verified strip theorem of proof 23 with strip radius epsilon0. On the output set near the axis, y stays in a fixed compact interval away from0. The background coefficient bounds in its Taylor expansion are uniform. The vertical-axis-subtracted coupling therefore has norm at most C_I epsilon0 ||h_j||_R, provided epsilon0<=1. The terms with higher powers of the strip radius are absorbed into this bound.

The difference between the vertical lift and the radial lift is

 p[gamma_U[h_in](log|y|)-gamma_U[h_in](log r)].

The pointwise derivative bounds in (5)-(6) of proof 48, applied to h_in as a subset of h_j, are independent of epsilon0. Since |log r-log|y||<=C_I x^2 on I near the axis, this difference has pointwise absolute value at most C_I |x|^4 ||h_j||_R. Its output norm on |x|<delta is therefore at most

 C_I delta^(9/2-a)||h_j||_R=C_I delta^(1/4)||h_j||_R.      (4)

For h_out, choose delta<epsilon0/2. Every source point has |s|>=epsilon0, while every output point has |x|<delta. The velocity kernel and its required derivatives are smooth with bounds depending only on I and epsilon0. Taylor subtraction of the full axis row, including the radial-versus-vertical lift correction, leaves an O(x^4) kernel. The source is in a fixed bounded annulus, so its inverse-weight volume is finite. Cauchy-Schwarz gives the operator bound

 ||1_{I,|x|<delta}D h_out||_R
                  <=C_(I,epsilon0)delta^(1/4)||h_j||_R.  (5)

Equivalently this separated kernel is Hilbert-Schmidt on the displayed input and output sets. There is no assertion that C_(I,epsilon0) remains bounded as epsilon0 tends to0.

Taking delta->0 first, then epsilon0->0, proves (3). This order of limits is essential. Summing the finitely many dyadic pieces and adding the compact part completes the proof.

It follows that for every epsilon>0 one can choose a smooth parity-preserving cutoff 0<=chi<=1, compactly supported away from x=0 and0, such that

 ||(1-chi)C_R||_(R->R)<epsilon.                            (6)

Choose the radial support first using (2), then the axis exclusion using (3); transition regions can be contained in the same small-output sets.

## The localized coupling modulo compact operators

On the support of chi, multiplication by p followed by radial lifting is bounded from L2 of a compact t interval to R. Proof 46 shows that Gamma:R->G is compact. The unnormalized row gamma_U differs from Gamma by the rank-one local strain row. Consequently chi p gamma_U is compact R->R. The remaining normalization term is also rank one. Therefore

 chi C_R = chi [rho_x U1+rho_y U2] + a compact operator.   (7)

Choose a second smooth parity-preserving cutoff psi, also compactly supported away from the axis and0, equal to1 on a neighborhood of supp chi. The part of the right side of (7) acting on (1-psi)h is Hilbert-Schmidt. The source and output supports are separated; near source0 the inverse weight is integrable, and at source infinity the squared kernel is O(r^(-4)) while w^(-1)<=r^eta, with eta<2. The output set is compact and its weight is bounded. Thus, modulo compact operators, h may be replaced by psi h in (7).

Let J:R->L2_P be the unitary map Jh=w^(1/2)h. Choose a globally bounded positive Lipschitz function v, bounded away from0, equal to w^(1/2) on a neighborhood of supp psi and supp chi, and equal to1 outside a compact set. This is possible because w^(1/2) is bounded and Lipschitz on that neighborhood. The radial knot at r=1 is harmless. Under J, the localized operator is

 chi rho_x v U1 psi v^(-1)+chi rho_y v U2 psi v^(-1).

For a bounded Lipschitz function v constant outside a compact set, [v,U_i] is compact on ordinary L2. A direct proof is given below. It follows that the last display differs compactly from

 chi rho_x U1 psi+chi rho_y U2 psi.

Removing psi again changes the operator by a separated-support Hilbert-Schmidt kernel. Therefore

 J chi C_R J^(-1) = g1 U1+g2 U2+K_chi,
 g1=chi rho_x, g2=chi rho_y,                              (8)

where K_chi is compact on L2_P. All coefficients g1,g2 are real, compactly supported and Lipschitz.

## Compact commutators without a weighted theorem

Let S be either a first-order Riesz transform R_j or one of U1,U2, and let v be bounded Lipschitz and constant outside a compact set. Off the diagonal the kernel of [v,S] is

 (v(X)-v(Y))K_S(X-Y).

The kernels in dimension2 satisfy |K_S(Z)|<=C|Z|^(-2). A local point mass in U2 commutes with v and makes no contribution. On |X-Y|<delta the absolute kernel is at most C Lip(v)|X-Y|^(-1). Both Schur integrals are at most C Lip(v)delta, so this part has operator norm tending to0.

On |X-Y|>=delta the kernel is square integrable: v(X)-v(Y) vanishes unless at least one variable lies in a fixed compact set, and integral_{|Z|>=delta}|Z|^(-4)dZ is finite. This part is Hilbert-Schmidt. Thus [v,S] is a norm limit of compact operators. The proof applies to every compactly supported Lipschitz coefficient used below.

## The exact bulk principal bound

Use the convention that R_j has multiplier i xi_j/|xi|. Then R_j*=-R_j,

 U1=-R1 R2, U2=R1^2,
 R1*R1+R2*R2=I.

For any real compactly supported Lipschitz g1,g2, move R1 across the L2 pairing in

 C_g=g1(-R1R2)+g2 R1^2.

The commutators with g1,g2 are compact by the preceding section. Hence, modulo a compact quadratic form,

 Re<C_g f,f>
   = integral [g1 Re(R2 f conjugate(R1 f))-g2 |R1 f|^2].   (9)

The pointwise Hermitian matrix acting on (R1 f,R2 f) is

 M_g=[[-g2,g1/2],[g1/2,0]].

Its largest eigenvalue is

 b_g=(sqrt(g1^2+g2^2)-g2)/2>=0.

Thus the right side of (9) is at most

 integral b_g (|R1 f|^2+|R2 f|^2).

The function b_g is compactly supported and Lipschitz. Commuting it through the two Riesz transforms, again modulo compact operators, and using R1*R1+R2*R2=I, turns the last expression into

 integral b_g |f|^2 + a compact quadratic form.           (10)

For the coefficients in (8), chi>=0 gives b_g=chi bplus. Combining (8)-(10), and taking the self-adjoint part of the compact remainder, proves

 Re<chi C_R h,h>_R
       <= integral chi bplus |h|^2 w +<K_chi' h,h>_R.     (11)

The argument works first on the full unweighted L2 space and then on the parity subspace by orthogonal compression. All compact operators remain compact under that compression.

Finally, (6) bounds the omitted quadratic form by epsilon ||h||_R^2. Since bplus>=0 and 0<=chi<=1, replacing chi bplus by bplus in (11) proves (1).

## Consequence and limits

This establishes the analytic nonlocal part of Theorem C' on the strong jet-plus-remainder realization. Under its remaining positive-axis hypothesis, lift bounds and positive transport margin, the Fredholm-index-zero conclusion now follows from proof 44 without separate unproved coupling assumptions. The actual positivity and its numerical constants still require independent certification. Injectivity, a quantitative inverse, classical normalization of a weak solution and a nonlinear iteration remain distinct problems.

The proof supplies existence of compact remainders, not a computable finite-rank approximation with a certified error. A computer-assisted inverse must still construct that approximation or another quantitative complement estimate. The finite section S0 uses different norms and does not supply it.

## Verification evidence

The accompanying symbolic audit verifies the bulk matrix eigenvalue identity and the source/target exponents used in the edge limit. The operator proof is fully contained above; no pseudodifferential theorem or weighted singular-integral theorem outside its range is invoked.

Dependencies: topics23,44,46-48. Verdict: CONFIRMED under the stated coefficient hypotheses. No existence theorem for the nonlinear profile is asserted.
