# A concrete low/high bilinear estimate

## Spaces, hypotheses and statement

Use a=17/4, eta=5/4 and the spaces B, R, G, Z and Y of proof 44, including its positive-axis hypothesis (A). Their norms are fixed in this result. Set

 X0=E B direct-sum R, E beta=x^2 y beta(log r),
 R=L2_P(w dX), w=|x|^(-17/2)max(1,r)^(29/4),
 Y=E G direct-sum R,
 ||gamma||_G^2=int_(t<0)|gamma|^2 e^(-t/2)dt
                    +int_(t>=0)|gamma|^2 e^(27t/4)dt.

The parity P is even in x and odd in y. The actual transport V is assumed to have the properties proved in proof 52: C1 and globally Lipschitz, with V_i/X_i bounded and the qualitative lift bounds. Define Z=E B direct-sum D_R, where D_R is the maximal domain of V.grad-1 on R.

Fix a real number gamma<-3/8. Fix a smooth nondecreasing function s:R->[0,1] with s=0 on t<=0 and s=1 on t>=1. Set

 chi(t)=1-s(t), a_gamma(t)=exp(2t+(gamma-5)t s(t)).

Thus a_gamma=e^(2t) for t<=0 and a_gamma=e^((gamma-3)t) for t>=1. Let H_gamma consist of

 h(r,theta)=r^3 cos(theta)^2 sin(theta) b(t,theta),
 b(t,theta)=j chi(t)+a_gamma(t)u(t,theta),
 j real, u in H^7(R x S1),

where u is even under each Cartesian reflection. Give it the Hilbert norm

 ||h||_(H_gamma)^2=|j|^2+||u||_(H^7)^2.

The representation is unique, as shown below. The choices of s and the standard inhomogeneous H7 norm are fixed once and for all.

Then H_gamma embeds continuously and injectively into Z. Its continuous cubic coefficient J agrees with the classical leading expansion

 h=x^2 y[j+O(r^2)] as r->0.

For the canonical velocity U and W[d]=U[d]+c[d]X/3, there is a finite constant C_gamma, depending only on the fixed spaces, cutoffs and gamma, such that

 ||W[d].grad h||_Y <= C_gamma ||d||_(X0)||h||_(H_gamma)    (1)

for every d in X0 and h in H_gamma. In particular (1) holds with ||d||_Z on the right. The product is interpreted by its locally integrable canonical representative and the axis decomposition proved below. No derivative of the low input d is required.

There is also a finite constant C_V,gamma such that

 ||D W[h]||_infinity+|c[h]|<=C_V,gamma ||h||_(H_gamma).    (2)

This is a sufficient low/high mapping theorem. It supplies neither a high-norm inverse nor an a posteriori existence result. In particular, no claim is made that the source inverse preserves this H7-based space. The forcing regularity and uniform inverse hypotheses of a two-norm iteration remain separate.

## Regularity of the high input and its embedding

Sobolev embedding on the two-dimensional cylinder gives bounded continuous derivatives of u through order5. One direct proof is to expand in the Fourier variable xi in t and integer variable n in theta and apply Cauchy-Schwarz: for any multiindex alpha with |alpha|<=5, the squared dual integral is bounded by

 sum_n int_R (1+xi^2+n^2)^(|alpha|-7) dxi < infinity.

The exponent is at most-2, which is integrable in two dimensions. Approximation by smooth Fourier cutoffs gives continuity. Thus all the required derivative bounds are controlled linearly by ||u||_H7.

It follows that b=j+O(r^2) near0 and b=O(r^(gamma-3)) at infinity, uniformly with the t and angular derivatives used below. On each annulus r~R0, Cartesian derivatives through order5 of h have size at most

 C ||h||_(H_gamma) d_gamma(R0) R0^(-m),
 d_gamma(R0)=R0^3 if R0<=1, R0^gamma if R0>=1.            (3)

For the inner correction h-j x^2 y, the sharper scale R0^5 holds. The coefficient in (3) is uniform: derivatives in Cartesian scaled coordinates are finite smooth combinations of t and angular derivatives on a fixed annulus. The interpolation interval0<t<1 is compact. A nonzero change in j would require changing u by a nonzero multiple of chi/a_gamma, which grows as e^(-2t) at the left end and is not L2. This proves uniqueness and completeness of the declared Hilbert realization.

Set beta(t)=b(t,pi/2) and h_R=h-E beta. The evenness in x implies b_theta(t,pi/2)=0, so Taylor's integral formula gives

 |b-beta|+|b_t-beta'|<=C cos(theta)^2 D(t),
 |partial_theta(b-beta)|<=C |cos(theta)| D(t),
 D(t)=O(r^2) near0 and O(r^(gamma-3)) at infinity,         (4)

with constants at most C||h||_(H_gamma). The squared angular integral is

 I_a=int_0^(2pi)|cos theta|^(8-2a)sin(theta)^2 dtheta
     =2 B(1/4,3/2)<infinity.

The squared radial powers for h_R are e^(7t/2) at the left end and e^((2gamma+3/4)t) at the right end. They are integrable precisely in the present strict far range. Thus ||h_R||_R is bounded by C||h||_(H_gamma).

The scalar beta belongs to B. Indeed its integrating factor H satisfies H=1+O(e^(2t)), H'=O(e^(2t)) at the left end and H~Hplus e^((k-3)t) at the right end. Therefore z=beta/H has z-j,z'=O(e^(2t)) at the left and z,z'=O(e^((gamma-k)t)) at the right. In the B weight these give the same positive left exponent7/2 and negative right exponent2gamma+3/4. The bounds are uniform and linear in the high norm. Hence J=j.

Finally T h_R=(V.grad-1)h_R is in R. Write V.grad=q partial_t+v_theta partial_theta, where q is bounded and v_theta=V.grad theta. The bounded divided components imply |v_theta|<=C|cos theta sin theta|. In (4), its vanishing factor supplies the extra cos(theta) needed when differentiating angularly. The prefactor r^3 cos^2(theta)sin(theta) is differentiated by a bounded cofactor because V1/x and V2/y are bounded. The same radial and angular integrals therefore bound ||T h_R||_R. This proves the continuous embedding H_gamma->Z. It also proves the classical expansion independently of weighted trace notation.

## Low-input trace bounds and the exact axis row

For d in X0 let T_d(y)=U2[d](0,y), interpreted by the canonical trace pairings of proof 46, and c_d=c[d]. These are bounded functionals of d. The proven trace estimates give, in X0 dual norm,

 |T_d(r)/r-c_d|+|T_d'(r)-c_d|<=C r^2 ||d||_(X0), r<=1,
 |T_d(r)/r|+|T_d'(r)|<=C r^(-11/8)||d||_(X0), r>=1.     (5)

They follow for the remainder input by the weighted kernel estimate through three derivatives, and for the jet input from its exact two angular Green modes. In both cases the strain is bounded on X0. These estimates require no classical derivative of d.

Write A(t)=b(t,pi/2). The exact axis coefficient of W[d].grad h is

 Gamma_(d,h)(t)=(A+A')T_d(r)/r-2A T_d'(r)
                                  +c_d(A+A'/3).        (6)

To derive (6), expand h=x^2 y A(log|y|)+O(x^4), use incompressibility partial_x U1(0,y)=-T_d'(y), and then add c_d X/3. At the left end, rewrite (6) as

 (A'-A)(T_d/r-c_d)-2A(T_d'-T_d/r)+(4/3)c_d A'.          (7)

Here A=j+O(r^2) and A'=O(r^2). Thus (5) gives O(r^2)||d||_X0||h||_Hgamma. At infinity, (6) gives O(r^(gamma-3)) with the same norm factors, including the full strain term. Its G square integrals have exponents7/2 and2gamma+3/4. Therefore Gamma_(d,h) belongs to G, with a bilinear bound.

## Remainder estimate and the full strain at infinity

First use the cutoff-normalized operator

 C_h d=[U[d]+chi0(r)c_d X/3].grad h,

where chi0 is smooth, equal1 near0 and compactly supported. The proofs of topics46-48 apply linearly in h with the following replacements: the cubic coefficient1 becomes j, and the far density exponent k becomes gamma. Their estimates are homogeneous in |j| and the coefficient bounds (3)-(4), so every constant is at most C||h||_Hgamma. For completeness, the integrability and cancellation steps are listed explicitly.

For jet inputs d=E beta_d, the two divided velocity components have X0-dual norm O(r^2) after their linear strain is subtracted near0, and O(r^(-11/8)) at infinity. The gradient cofactor of h is a linear combination of b,b_t,b_theta. Its constant-strain contribution is exactly

 c_d[(4/3-2 cos(theta)^2)b_t
                         +2 cos(theta)sin(theta)b_theta].

The constant j cancels. Subtracting (6) gives an additional cos(theta)^2 by two angular derivatives. Consequently its radial square integrals have exponents7/2 and2(gamma-1), both admissible. This proves the jet-input remainder bound.

For remainder inputs d_R, split every output annulus r~R0 into input scales R0/8<|Z|<8R0 and their complement. The comparable-scale strip estimate of proof 23, with the axis coefficient subtracted, gives operator norm at most

 C ||h||_Hgamma d_gamma(R0)/R0.

The radial lift differs from the vertical lift by an extra O(cos(theta)^2); the trace derivative bounds give the same norm estimate. The coefficients are at most C R0^2 near0 and C R0^(gamma-1) at infinity, and the dyadic input annuli have overlap at most7. This gives a globally bounded nearby-scale operator.

For the separated scales, the reflected velocity kernels are smooth. Subtracting the axis row gives the angular factor |cos(theta)|^4|sin(theta)|. Inner sources have divided kernel O(r^(-3)); their squared weighted double integral is bounded by constants times

 int_0^1 r^3 dr + int_1^infinity r^(2gamma-3)dr.

For outer sources, the parity expansion is U=c_Z(-x,y)+O(r^3|Z|^(-5)). Its constant-strain cofactor cancels after the axis subtraction even for arbitrary j. The remaining kernel near0 is bounded by

 C ||h||_Hgamma |cos(theta)|^4|sin(theta)|
                                r^5(|Z|^(-3)+|Z|^(-5)).

The source integrals converge because a>4, while the output integral is int_0^1 r^(11-2a)dr. At infinity the kernel is bounded by C||h||_Hgamma |cos(theta)|^4|sin(theta)| r^gamma |Z|^(-3), again giving int_1^infinity r^(2gamma-3)dr. All are finite since gamma<1 and11-2a=5/2. These are Hilbert-Schmidt estimates, so in particular they are bounded-operator estimates linear in the high norm. The cutoff-normalization difference is a bounded rank-one term with the same inner cancellation. This proves ||C_h d||_Y<=C||d||_X0||h||_Hgamma.

The actual W[d] has no cutoff. The omitted part is

 (c_d/3)(1-chi0)X.grad h.

It vanishes near0. Its cofactor is (1-chi0)(3b+b_t); the axis coefficient is (1-chi0)(3A+A'). Subtracting the latter again supplies cos(theta)^2. At infinity both have order r^(gamma-3). The resulting squared radial exponent is2gamma+3/4<0. Hence this fixed-function term belongs to Y with norm at most C|c_d|||h||_Hgamma. Combining the two parts proves (1). The strict gamma<-3/8 requirement is what makes the full strain term permissible here.

All formulas first hold for smooth approximations in the displayed high and low spaces. Local L2 convergence of the low-input canonical velocity and bounded local derivatives of h identify the extension with the locally integrable product. The axis traces converge by (5), so the Y-valued limit has exactly the decomposition (6). This verifies both input and output membership.

## A direct velocity Lipschitz bound

For a scalar function g that is Lipschitz, bounded and L2, each component of the velocity multiplier satisfies

 ||U_i[g]||_infinity
 <= (1/2)||g||_infinity+Lip(g)+(1/(2 sqrt(pi)))||g||_2.   (8)

The harmless first term is only needed for U2. To prove (8), use its off-diagonal kernels K1=-xy/(pi r^4), K2=(x^2-y^2)/(2pi r^4), both bounded by1/(2pi r^2) and having zero angular mean. On |Z|<1 subtract g(X) and integrate Lip(g)|Z| against this kernel bound, which gives Lip(g). On |Z|>=1 use Cauchy-Schwarz; the squared integral of the kernel bound is1/(4pi). The local point mass of U2 has magnitude1/2. This proves (8) directly and fixes its convention.

For h in H_gamma, each g=partial_j h is globally bounded and Lipschitz by (3), including the origin, where h=j x^2 y+O(r^5) with differentiated bounds. It is L2 because its squared far radial exponent is2gamma-1<-1, using gamma<0. Near0 its squared radial power is5. Each quantity in (8) is at most C||h||_Hgamma. Derivatives commute with the canonical multiplier, by local regularization and the convergent far integral. Thus every entry of D U[h] is bounded by

 M(h)=max_j[(1/2)||partial_j h||_infinity
             +Lip(partial_j h)+(1/(2 sqrt(pi)))||partial_j h||_2].

The strain c[h]=partial_y U2[h](0) has absolute value at most M(h). Continuity at0 follows by the same kernel split and approximation. The matrix norm is bounded by2M(h), so

 ||D W[h]||_infinity+|c[h]|<=(10/3)M(h).

This proves (2). No smallness follows until the high norm is quantitatively bounded.

## Scope and dependencies

The theorem gives a reflexive, explicit high space with the desired bilinear mapping, continuous classical normalization, and Lipschitz velocity. It removes a mapping gap only under this stated strong regularity. A compatible uniform inverse into H_gamma is not known. The actual frozen source regularity loss must be respected, and a localization or different high space would be needed to avoid imposing unnecessary H7 regularity near that source. The variable-tail problem also remains: this space describes decaying corrections after the moving leading tail has been treated separately.

Dependencies: the fully specified low realization and strain bound in proof 44; trace estimates and jet Green formulas in topics46-47; local strip theorem proof 23 and global decomposition proof 48; actual transport coefficient bounds in proof 52. Every endpoint exponent and the uncut strain contribution have been checked here for the new high-input class.
