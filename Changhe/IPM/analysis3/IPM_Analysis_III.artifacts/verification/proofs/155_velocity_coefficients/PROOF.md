# The velocity coefficients of a high-space perturbation

## Statement and conventions

Use the exact values and fixed smooth functions of proof 123:

 s_0=41/20, sigma=25/4, delta=9/5, gamma=-1/2,
 b(t)=exp(3t)a(t), p(theta)=cos(theta)^2 sin(theta).

Thus b(t)=exp((3+delta)t) on the left and b(t)=exp(gamma t) on the right. The order s is smooth with bounded derivatives, s_0<=s<=sigma, and s=sigma on an open vertical sector. Choose nested sector cutoffs chi and chi_1, with chi_1=1 near supp chi, and s=sigma on an open neighborhood of supp chi_1. The input cofactor norm below uses chi_1. Let chi_0(t) be smooth, equal to1 sufficiently far left and0 sufficiently far right. Its derivatives are bounded and supported in a fixed finite interval.

Let G_s consist of real parity-P functions of the form

 g(X)=J x^2 y chi_0(log r)+b(log r)v(log r,theta),
 v in H^{s(.)}(C), chi_1 v/p in H^sigma(C),                (1)

where C=R times S1 and J is a real scalar. Give this space the sum norm

 ||g||G=|J|+||v||H^s+||chi_1 v/p||H^sigma.

No zero cofactor trace is required here. The representation is unique: the free jet divided by b grows as exp(-delta t) at the left, so cannot be absorbed into the L2 function v. The high full space B_H plus X_s of proof 150 embeds continuously in G_s, by the scalar representation beta=J chi_0+a beta_1 with beta_1 in H^(sigma+1), and the definition of X_s. A harmless change between fixed scalar cutoffs gives equivalent decompositions.

Let U=(-R_1 R_2,R_1^2) be the canonical full-plane IPM velocity, and let c[g]=partial_y U_2[g](0), defined equivalently by the absolutely convergent kernel of proof 1. In polar components put

 B[g]=(U[g].e_r/r, U[g].e_theta/r),
 B_0(theta)=(-cos(2theta),sin(2theta)),
 Z[g]=B[g]-c[g]chi_0(t)B_0(theta).                       (2)

Then c and Z are bounded linear maps, with

 |c[g]|+||Z[g]||H^{s(.)}(C)
 +||chi Z[g]||H^sigma(C)
 +||chi Z_theta[g]/cos(theta)||H^sigma(C)
 <=C||g||G.                                             (3)

The quotient in (3) is its Sobolev extension at the vertical axis. For every 0<alpha<1/20,

 ||B[g]||C_b^(1,alpha)+|c[g]| <=C_alpha||g||G.            (4)

The same conclusions hold for the normalized transport variation

 B_norm[g]=B[g]+c[g](1,0)/3,                             (5)

with the explicit nondecaying part c[g](chi_0 B_0+(1,0)/3). In particular its bulk zeroth-order coefficient beta(t) B_norm,r is the sum of a bounded smooth scalar multiple of c[g] and an H^{s(.)} function, for any fixed smooth bounded beta with bounded derivatives. Its cofactor coefficient

 chi [beta(t) B_norm,r+(p'/p)B_norm,theta]

has the analogous H^sigma bound after its explicit smooth part is removed. Here the product is only used in the vertical sector, where sin(theta) is bounded away from zero.

These are qualitative bounds. They do not prove a rough transport commutator, a uniform inverse, or nonlinear existence.

## Definition of the velocity and the strain

First take finitely many smooth radial annular pieces of v. The kernel of U has degree minus2 away from its local distributional term; the strain kernel has degree minus3. The latter local term vanishes for (1), since partial_y g(0)=0. On an annulus of radius R, the L1 size of the input is at most C R^2 b(log R)e_R, where e_R is its normalized local high norm. The strain contribution is therefore at most

 C b(log R)e_R/R.                                      (6)

The sequence b(log R)/R is square summable over dyadic radii: its powers are R^(2+delta) at0 and R^(gamma-1) at infinity. Cauchy-Schwarz proves the absolute strain bound. The free-jet input is a fixed smooth compactly supported physical function, so its strain is finite and bounded by C|J|.

The velocity integral is locally well defined by its usual principal value on comparable annuli. Contributions from distant annuli converge absolutely by the bounds below. They define the same canonical velocity as the distributional multipliers, by taking radial cutoffs to0 and infinity. Thus (2) introduces no alternate inverse Laplacian or far-field gauge.

## Comparable annuli and the vertical quotient

Use a fixed smooth radial partition with bounded overlap. Let the source and target radii be comparable to R and rescale Cartesian coordinates by R. A localized U is an order-zero pseudodifferential operator plus a smooth kernel. Proof 123 proves its boundedness on H^{s(.)} in the rescaled coordinates, uniformly over annuli. Dividing the physical velocity by r contributes the scale factor

 b(log R)/R=R^(2+delta) on the left, R^(gamma-1) on the right.

These factors are uniformly bounded. Smooth coordinate multipliers and the fixed finite transition annuli preserve the estimate. The local strain subtraction obeys the same bound by (6).

For a vertical output patch the portion of the input outside a larger vertical patch is separated and has a smooth kernel. Inside the larger patch write g=x^2 w, with its rescaled w in H^sigma. Proof 141 gives the exact localized identities

 U_1[x^2 w]/x=x U_1[w]+2[U_1,x]w+x^(-1)[[U_1,x],x]w,
 U_2[x^2 w]=x^2 U_2[w]+2x[U_2,x]w+[[U_2,x],x]w.          (7)

The single and double commutators have orders minus1 and minus2. The double U_1 commutator is odd in x; division by x costs one derivative, by the integral formula in proof 123. Every term in (7) is therefore bounded in H^sigma, with the scale factor just displayed. In polar coordinates

 B_theta/cos(theta)=-sin(theta) U_1/x+U_2/r.              (8)

Consequently the cofactor norm in (3) is bounded on comparable annuli. The nested cutoffs ensure that the input required in this argument is covered by chi_1. No division of an arbitrary nonzero trace has been used. Parity also gives the exact vanishing B_theta=0 on each axis.

## Separated annuli and removal of the strain

Write r for the output radius and R for the source radius, and let e_R be the source norm. Oddness of g in y makes its mean zero. If R is much smaller than r, Taylor expansion of the degree-minus2 kernel in the source point gives

 |U[g_R](X)|/r <= C r^(-4)R^3 b(log R)e_R.               (9)

If r is much smaller than R, Taylor expansion in the output point gives

 U[g_R](X)=c[g_R](-x,y)+O(r^3 b(log R)R^(-3)e_R).         (10)

There is no constant or quadratic term. The parity of U_1 is odd in x and even in y; that of U_2 is even in x and odd in y. Divergence zero identifies the two linear coefficients as minus c[g_R] and c[g_R]. The same bounds hold for every fixed number of rescaled output derivatives. The corresponding bounds for U_1/x follow either from its odd kernel or the integral division formula after one such derivative.

For r sufficiently small, chi_0=1. Subtract (10) before summing source annuli. Up to constants and finitely many transition annuli, the matrix majorants for Z, including its two vertical norms, are

 R<=r<=1:       C R^(2+delta),
 r<=R<=1:       C r^2 R^delta,
 1<=R<=r:       C r^(-4) R^(gamma+3),
 1<=r<=R:       C R^(gamma-1),
 r<=1<=R:       C r^2 R^(gamma-3),
 R<=1<=r:       C r^(-4) R^(6+delta).                    (11)

In the first line, (9) is bounded by R^(2+delta), and the subtracted strain has exactly that size by (6). In the second and fifth lines (10) gives the stated cubic remainder. The third and sixth lines are (9). In the fourth line the unsubtracted strain and remainder are bounded by R^(gamma-1). This line is only used where the cutoff has vanished. Shifting the threshold1 to either fixed cutoff endpoint changes constants only.

Every matrix in (11) has bounded row and column sums on dyadic radii. For example, the first line has row sum O(r^(2+delta)) and column sum O((1+|log R|)R^(2+delta)); the second has row sum O(r^2) and column sum O(R^(2+delta)). The fourth has row sum O(r^(gamma-1)) and column sum O((1+log R)R^(gamma-1)). These are bounded because delta>0 and gamma<1. The third uses gamma+3>0 and gamma-1<0; the two mixed matrices are products of summable geometric sequences. Schur's test thus bounds the separated maps on the square-summable sequence of local high norms.

For precision about these high norms, separated kernels have arbitrarily many rescaled output derivatives, with the same powers in (11); choose more than sigma+2. The input is estimated in local L2, already controlled by e_R. Smooth output cutoffs then bound the variable-order and the fixed-order output norms. Comparable annuli were handled separately above. Bounded-overlap localization characterizes the global H^{s(.)} norm because the order and its derivatives are uniformly bounded. This proves (3) for the b v part.

## The free cubic jet and completion

The remaining input is J g_*, where g_*=x^2 y chi_0(log r). It is a fixed smooth compactly supported physical function and agrees with a polynomial near0. Its canonical velocity is smooth. Near0 its Taylor expansion is c[g_*](-x,y)+O(r^3), with bounds for all derivatives; hence Z[g_*]=O(r^2) in cylinder coordinates. At infinity the mean-zero estimate gives B[g_*]=O(r^(-4)), again with all rescaled derivatives. Parity supplies (8) and its uniform differentiated form. Thus Z[g_*] and both vertical expressions belong to every finite cylinder Sobolev space. Their norms are fixed constants times |J|.

For completeness, simultaneous approximation in the two input norms can be made with a smaller vertical partition: approximate the cofactor in H^sigma there and multiply by p; away from the axis approximate v in H^{s(.)}. On the transition strips p is nonzero and s=sigma, so these constructions agree in the norm after a fixed partition of unity. First truncate in t and then smooth, preserving the two reflections. The resulting smooth annular approximation converges in both input norms in (1). The bounds just proved give convergence of c and Z in the claimed target spaces. The kernel construction agrees with these limits on compact annuli and in distributions, so the limiting maps remain canonical. The strain bound and the target norms also show their continuity. This proves (3) for all g in G_s without assuming a special normalized graph core.

Finally H^{s(.)} embeds in H^(41/20) by the order comparison of proof 144. In dimension2 the Sobolev embedding H^(41/20) into C_b^(1,alpha) holds for every alpha<1/20. Add the explicit smooth strain term to obtain (4). Equation(5) only adds a bounded smooth field. Near the vertical axis, p'/p=-2tan(theta)+cot(theta); (8) handles tan(theta)B_theta and cot(theta) is smooth there. Multiplication by the fixed smooth factors proves the two coefficient assertions following (5).

## Dependencies and scope

The proof uses the canonical kernels and parities of proof 1; the exact high-space and local order-zero calculus of proof 123; the parity division identities of proof 141; and the order comparisons of proof 144. It uses no property of the approximate solution beyond those already fixed in the spaces. It does not assert that U preserves the density remainder space X_s, which has an additional zero cofactor trace. The velocity instead takes values in the coefficient space (2)-(3), with a necessary explicit nondecaying strain.
