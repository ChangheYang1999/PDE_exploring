# The scalar axis operator under a high-space velocity perturbation

## Spaces and statement

Use the exact background and fixed functions of topics123,150 and155. Thus sigma=25/4, delta=9/5, gamma=-1/2, a(t)=exp(delta t) sufficiently far left and exp((gamma-3)t) sufficiently far right, and b(t)=exp(3t)a(t). The smooth cutoff chi_0 is one far left and zero far right. Let

 Gamma_H=a H^sigma(R),
 B_H={beta=J chi_0+a v:J real, v in H^(sigma+1)(R)},
 ||beta||B_H=|J|+||v||H^(sigma+1).

Let G_s be the coefficient input space of proof 155, with the same density parity and a possibly nonzero axis cofactor. For g in G_s put c=c[g] and

 tau_g(t)=exp(-t) U_2[g](0,exp(t)),
 d_g=d+tau_g+c/3, ell_g=ell+c/3, D_g=4ell_g-1.

The canonical axis trace exists in the sense established below. The following conclusions hold, with constants depending only on the fixed spaces, cutoffs and background:

 (i) tau_g=c chi_0+e_g, with

 ||e_g||H^(sigma+3/2)+||chi_- e_g/a||H^(sigma+3/2)+|c|
       <=C ||g||G_s,                                      (1)

where chi_- is any fixed smooth cutoff equal to one far left and zero far right.

 (ii) The exact perturbed scalar operator is

 A_g beta=d_g beta'+(D_g-d_g-2d_g')beta
          =A beta+(tau_g+c/3)beta'+(c-tau_g-2tau_g')beta.    (2)

It is a bounded map B_H->Gamma_H and

 ||A_g-A||_(B_H->Gamma_H)<=C_A ||g||G_s.                  (3)

 (iii) A_0 is the isomorphism of proof 114. Consequently, if

 C_A ||g||G_s ||A_0^(-1)||_(Gamma_H->B_H)<1,              (4)

then A_g is an isomorphism on these same spaces. On any smaller fixed ball where the left side is at most q<1, its inverse norm is at most ||A_0^(-1)||/(1-q). The constants in this statement are qualitative, not computed numbers.

## Canonical axis trace and its local gain

On a fixed rescaled annulus meeting the positive y-axis, the density has the form x^2 w, where w has H^sigma regularity. The input from outside a larger axis patch is separated from that axis and has a smooth kernel there. A compactly supported axis patch can be handled by a Fourier transform in y. The multiplier U_2 is -xi^2/(xi^2+eta^2). Writing it as -1+eta^2/(xi^2+eta^2), and using that the local term vanishes at x=0, gives the exact formula

 T_hat(eta)=(|eta|/2) integral_R exp(-|eta||x|) x^2 w_hat(x,eta) dx,
 T(y)=U_2[x^2 w](0,y).                                  (5)

For |eta|>=1, the squared L2_x norm of the kernel in (5) is

 (eta^2/4) integral_R exp(-2|eta||x|) x^4 dx
      =3/(8|eta|^3).                                    (6)

For |eta|<=1, the compact x support gives a uniform bound instead. Multiplying the Cauchy-Schwarz estimate by <eta>^(2sigma+3) and integrating proves

 ||T||H^(sigma+3/2)<=C ||w||H^sigma.                    (7)

Smooth local changes between y and log y, division by y on this rescaled annulus, and the fixed cutoffs preserve the estimate. Approximation defines the trace for every input in G_s and identifies it with the canonical distributional velocity. Formula(5) also fixes the sign of the high-frequency leading term: for a normally constant amplitude, the integral of x^2 gives +2/eta^2 times that amplitude, not -2/eta^2. This local asymptotic observation is not needed for the norm estimate.

## Radial summation and the stronger inner weight

Use the dyadic annuli and local input norms e_R of proof 155. On comparable source and output annuli of radius R, the normalized velocity has size factor b(log R)/R. Estimate(7) improves the axis Sobolev order by3/2 with that same factor. These factors are R^(2+delta) on the inner end and R^(gamma-1) on the outer end; both are bounded and decay at the corresponding end.

For separated annuli, every fixed number of rescaled output derivatives falls on a smooth kernel. Thus the six matrix bounds (11) of proof 155 hold also for the output H^(sigma+3/2) norm of the axis trace, after subtracting the central strain before summing. Their row and column sums were proved bounded there. This proves the first unweighted term of (1) for the annular part of g.

For the weighted inner term, restrict output radii to r<=1, altering the fixed threshold only changes constants. Multiplication by 1/a contributes r^(-delta). The three relevant separated matrices become

 R<=r<=1:       C r^(-delta) R^(2+delta),
 r<=R<=1:       C r^(2-delta) R^delta,
 r<=1<=R:       C r^(2-delta) R^(gamma-3).              (8)

Their row and column sums on dyadic radii are uniformly finite. In the first line the row sum is O(r^2) and the column sum is O(R^2), by summing a geometric series with exponent delta>0. In the second line the row sum is O(r^(2-delta)) and the column sum is O(R^2), since both delta and2-delta are positive. The third is a product of two summable geometric sequences, since2-delta>0 and gamma-3<0. On comparable annuli the weighted factor is R^2. The derivatives of the normalized weight on a unit annulus are uniformly bounded to every fixed order, so (8) bounds the full H^(sigma+3/2) norm, not just L2.

The free input J x^2 y chi_0(log r) is a fixed smooth compactly supported physical function. Its velocity has expansion c(-x,y)+O(r^3) at0, including all fixed rescaled derivatives, and O(r^(-3)) at infinity. Hence its e_g is O(r^2) at0 and O(r^(-4)) at infinity. Dividing the inner remainder by a leaves O(r^(2-delta)), which has every finite cylinder Sobolev order. This proves (1) for the free jet as well. Continuity and the density construction of proof 155 complete the proof for all g in G_s.

## Derivation of the scalar row

The perturbed physical field V_g=V+U[g]+cX/3 has divergence2ell_g. On the positive y-axis V_(g,2)(0,y)=y d_g(log y), so

 partial_y V_(g,2)(0,y)=d_g+d_g',
 partial_x V_(g,1)(0,y)=2ell_g-d_g-d_g'.                 (9)

The parity and C1 regularity from proof 155 justify these identities and the axis limits. Acting on E beta=x^2 y beta(log r), the axis cofactor of V_g.grad(E beta)-E beta is therefore

 d_g beta'+[2(2ell_g-d_g-d_g')+d_g-1]beta.

This is the first expression in (2). Subtracting the background row, and using D_g-D=4c/3, gives its second expression. In particular the normalization contributes +c/3 to d_g and +c to the zeroth-order difference. No fixed-ell linearization has been substituted.

## Boundedness on the exact scalar domain

For beta=a v, divide the difference in (2) by a to obtain

 (tau_g+c/3)v'
 +[(tau_g+c/3)a'/a+c-tau_g-2tau_g']v.                  (10)

By (1), tau_g is a fixed smooth step times c plus an H^(sigma+3/2) function; its derivative is in H^(sigma+1/2) after the analogous smooth part is removed. The logarithmic derivative a'/a is smooth and bounded with all derivatives. The one-dimensional H^sigma algebra estimate, sigma>1/2, therefore bounds (10) in H^sigma by C||g||G_s||v||H^(sigma+1).

For beta=J chi_0 the difference divided by a is

 J[(tau_g+c/3)chi_0'+(c-tau_g-2tau_g')chi_0]/a.          (11)

The chi_0' terms have fixed compact support and are bounded by (1). Far left chi_0=1 and tau_g=c+e_g, so (11) is exactly

 -J(e_g+2e_g')/a.                                     (12)

The constant strain cancels. The second estimate in (1), together with e_g'/a=(e_g/a)'+(a'/a)(e_g/a), bounds (12) in H^sigma. Far right (11) vanishes. Combining (10)-(12) proves (3) on all of B_H. This also shows why the free coefficient must be handled before taking the weighted norm.

Finally write A_g=[I+(A_g-A_0)A_0^(-1)]A_0. Condition(4) permits the Neumann series on Gamma_H and gives the stated uniform inverse bound. Completeness and the closed free coefficient J come from the direct-sum definition of B_H and proof 114.

## Scope

The full perturbed scalar row is controlled on a fixed Banach domain with its classical free cubic coefficient. This result does not impose J=0, prove the full coupled inverse, or evaluate the constants in (4). The fixed-normalization subspace is a separate codimension-one issue, already exposed by the low index calculation.

## Companion inner coefficient estimate

The same argument also proves the weighted coefficient estimate (8) used in proof 165. Namely, for Z=B[g]-c[g]chi_0(-cos(2theta),sin(2theta)), multiply the three inner-output matrices of proof 155 by r^(-delta), obtaining exactly (8) above. On comparable annuli proof 155 supplies the bulk H^{s(.)}, vertical H^sigma and divided angular H^sigma bounds, all with the factor b(R)/R; after division by a this is R^2. On separated annuli all fixed output derivatives and the divided angular expression have the same matrix majorants. The free jet has the O(r^2) remainder, including the divided expression by parity. Schur summation therefore gives (8) of proof 165 with a constant times ||g||G_s. This statement concerns only an inner cutoff of Z/a; no global outer estimate of Z/a is asserted.
