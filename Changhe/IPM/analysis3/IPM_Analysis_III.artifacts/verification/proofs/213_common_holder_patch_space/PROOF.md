# A common weighted target for the origin and source patches

## Statement

Fix 0<alpha<1. Use physical coordinates X=(x,y), the joined normalized modal trial rho0, its exponent k=1615536043799051/9007199254740992 and its two sources P_+=(p,0), P_-=(-p,0). Let E2 be the Banach space of bounded continuous even-x, odd-y functions satisfying h(0,y)=0, with norm

 ||h||E2=||h||infinity+[h]_x+[h]_(y,2),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha).

For gamma>4k define

 w_gamma(X)=(1+|X|^2)^(-gamma/2),
 Y_(alpha,gamma)=E2 intersect L2(w_gamma dX),
 ||h||Y=||h||E2+||h||L2(w_gamma).

The value gamma=1 is allowed, since 4k<1. The following statements hold.

1. Y_(alpha,gamma) is a Banach space, and the canonical central strain c is bounded on it with ||c||Y*<=4/pi.
2. The exact modal residual F0=(ell0 X+U[rho0]).grad rho0-rho0 belongs to Y_(alpha,gamma). More precisely, F0 belongs to E2 and belongs to L2(w_gamma) if and only if gamma>4k. Thus F0 does not belong to unweighted L2.
3. Choose a sufficiently small fixed origin extension radius as in proof 203, and denote its normalized inverse on E2 by R_o. For smooth compact radial cutoffs eta_o,chi_o supported in that extension neighborhood, the map

        K_o f=chi_o R_o(eta_o f)

   is bounded Y_(alpha,gamma)->Y_(alpha,gamma).
4. Choose a sufficiently small fixed source extension radius as in proof 210, with radial extension cutoffs, and denote its source-centered, unnormalized inverse on X_alpha=C_b^alpha intersect L2 by R_+. Let eta_+,chi_+ be smooth compact cutoffs in the positive-source disk, even in y, and let that disk and its reflection be disjoint and separated from x=0. Translate eta_+ f to source coordinates, apply R_+, translate back, and multiply by chi_+. Call the result u_+. Then

        K_s f(x,y)=u_+(x,y)+u_+(-x,y)

   is bounded Y_(alpha,gamma)->Y_(alpha,gamma).
5. The strain functional restricted to any fixed compact source patch separated from the physical origin is bounded already in the weighted L2 norm. Its unboundedness in the unrestricted X_alpha norm is therefore an origin effect, not an obstruction caused by translation-invariant regularity near P_+.

All operator constants in statements 3 and 4 depend on the fixed cutoffs, radii, alpha and gamma. No uniform bound as the cutoff radii tend to0 is asserted. These are bounded cutoff constructions, not global inverses or a Fredholm parametrix identity. In particular no estimate for I-LK or I-KL is asserted.

## Completeness and strain

A Cauchy sequence in E2 converges uniformly to a continuous function with the same parities and axis value. The weighted difference quotients pass to that limit and converge in their suprema by the Cauchy property. Thus E2 is complete. A sequence Cauchy in the sum norm also has an L2(w_gamma) limit. Uniform convergence identifies the two limits on every compact set, because w_gamma has a positive lower bound there. Hence Y_(alpha,gamma) is complete.

The strain is the absolutely convergent integral

 c[h]=(1/pi) integral sin(3theta) r^(-3) h(X)dX.

Near0, oddness in y and the weighted seminorm give |h(x,y)|<=[h]_(y,2)|x|^2 |y|^alpha. The polar radial integral is integral_0^1 r^alpha dr=1/(1+alpha). The angular integral is at most integral_0^(2pi)|sin(3theta)|dtheta=4. Outside the unit disk, use ||h||infinity and integral_1^infinity r^(-2)dr=1. Therefore

 |c[h]| <= (4/pi){[h]_(y,2)/(1+alpha)+||h||infinity}
         <= (4/pi)||h||E2 <=(4/pi)||h||Y.

This is the canonical strain by proof 201, whose hypotheses hold because h belongs to E2.

## Exact residual membership

Proof 39 derives the global factorization F0=x^2 y B(X) on punctured annuli directly from the exact modal formulas. Near0, B and all fixed cylinder derivatives are O(r^2). At infinity they are O(r^(2k-4)). On every compact annulus, B is C5 across the finitely many radial joins. The finite angular formulas permit the division by x^2 with the same regularity across the vertical axis. These estimates use the normalized joined trial, for which the cubic residual cancels exactly.

Put H=F0/x^2=y B for x nonzero and take its continuous extension to the axis. Near0,

 |H|<=C r^3, |partial_y H|<=C r^2,
 |F0|<=C r^5, |partial_x F0|<=C r^4.

These differentiated estimates follow by converting one cylinder derivative to a Cartesian derivative, with its factor r^(-1). Any higher-order logarithmic terms in the exact inner expansion are absorbed by the displayed weaker powers. At infinity,

 |H|<=C r^(2k-3), |partial_y H|<=C r^(2k-4),
 |F0|<=C r^(2k-1), |partial_x F0|<=C r^(2k-2).

All four functions are bounded globally, including the compact annular joins. A bounded Lipschitz function of one variable has bounded alpha seminorm: use the derivative bound for differences at most1 and twice the supremum for differences at least1. Apply this first to F0 in x and then to H in y. Since

 |F0(x,y)-F0(x,y')|/|x|^2=|H(x,y)-H(x,y')|,

we obtain F0 in E2 for every alpha in(0,1).

For the weighted L2 condition, proof 117 and V120 establish, with a nonzero finite angular polynomial S,

 F0(r,theta)=r^(2k-1) S_0(theta)+O(r^(3k-2)),

uniformly in theta, where S_0 is a fixed nonzero rescaling of that proof's S. Since k<1, the remainder is lower order. The squared angular L2 norm is therefore

 integral |F0(r,theta)|^2dtheta
       =r^(4k-2)(||S_0||2^2+o(1)).

The positive leading constant gives both an upper and a lower comparison with r^(4k-2) for all sufficiently large r. Since w_gamma is comparable to r^(-gamma), polar integration is finite precisely when

 integral_1^infinity r^(4k-1-gamma)dr<infinity,

that is gamma>4k. Local integrability follows from the boundedness already proved. This also proves unweighted L2 failure. No new numerical residual bound is claimed; the nonzero leading coefficient is the independently certified input V120.

## Multiplication and local norm comparisons

A fixed smooth compact radial cutoff eta acts boundedly on E2. The x seminorm follows from the product difference and the bounded derivative of eta. For the weighted y seminorm, one term is ||eta||infinity[h]_(y,2). In the other term use

 |h(x,y)|/|x|^2<=[h]_(y,2)|y|^alpha.

If |y-y'|<=1 and eta differs at the two points, one of the points lies in a fixed bounded set, so both |y| and |y'| are uniformly bounded. The cutoff difference is at most C|y-y'|. If |y-y'|>1, orient the product identity so the undifferenced h is evaluated at a point on the cutoff support; its |y| is bounded. These estimates give a finite multiplier bound. Compact support and ||eta h||infinity also give

 ||eta h||L2(w_gamma)<=C_eta,gamma||h||infinity.

Next let K be a fixed bounded set with |x|>=a>0. Every compact C^alpha function supported in K belongs to E2, once extended with the required parities, with norm at most C_(K,alpha)||h||C^alpha. On vertical lines meeting the support, |x|^(-2)<=a^(-2); lines not meeting it contribute zero. The x seminorm and supremum are ordinary Holder quantities. Its weighted L2 norm is bounded by the supremum times the square root of the finite weighted volume.

Conversely, on a bounded box |x|<=R, an E2 function satisfies a full local C^alpha estimate. Connect (x,y) to (x',y') by a horizontal segment and then a vertical segment at x'. The two bounds are [h]_x|x-x'|^alpha and [h]_(y,2)R^2|y-y'|^alpha. Their sum is at most C_R||h||E2 |X-X'|^alpha. After a fixed compact cutoff this is a global C^alpha estimate, and the cutoff gives an unweighted L2 bound.

## The two cutoff solution maps

For K_o, eta_o f belongs to E2 by the multiplier estimate. Proof 203 gives R_o(eta_o f) in E2 with norm at most ||R_o|| ||eta_o f||E2. Multiplication by chi_o retains E2, makes the output compact, and supplies the weighted L2 bound. Thus K_o is bounded on Y. This proof never assumes the full, uncut origin inverse preserves L2(w_gamma).

For K_s, the positive-source cutoff eta_+ f is compact and has a bounded full C^alpha norm by the local comparison. Translation preserves C^alpha and unweighted L2, so the source forcing lies in X_alpha with norm at most C||f||Y. Proof 210's inverse applies to this forcing and returns an X_alpha function, without a support restriction on that output. Multiplication by the source cutoff chi_+ then makes u_+ compact and separated from x=0. It is odd in y: eta_+ f is odd, the radial source extension preserves oddness, and uniqueness of the source inverse preserves it. Reflection and addition supply evenness in x. The support comparison above gives

 ||K_s f||Y<=C ||R_+||_(X_alpha->X_alpha)||f||Y.

No smallness or cancellation between the two source patches is used in this bound. The Fourier multiplier velocity in R_+ agrees with the canonical global velocity only after the appropriate global parity is imposed; contributions of the reflected patch and of the output cutoff remain part of the still unestimated gluing error.

## Strain on the source patch and the unresolved operator identity

For a fixed cutoff eta supported in a compact set K with distance(K,0)>0, Cauchy-Schwarz gives

 |c[eta f]| <= C_(eta,gamma)||f||L2(w_gamma),
 C_(eta,gamma)=(1/pi){integral_K |sin(3theta)|^2 r^(-6)
                                      |eta|^2 w_gamma^(-1)dX}^(1/2)<infinity.

This statement uses the absolutely convergent kernel integral, even when eta f does not have both global parities. When the cutoff is paired by reflection, it is the canonical strain of the resulting parity-class input. No singularity occurs on K. The packets proving unrestricted X_alpha unboundedness concentrate at the physical origin, which is outside K.

The bounded maps K_o and K_s do not settle the full problem. Applying the actual global operator introduces transport-cutoff terms, nonlocal cutoff commutators, the other source's velocity, interactions with the invariant axes and the far region, and the moving-tail normalization column. None of those errors has been estimated here. In particular the raw global column X.grad rho0 grows like r^k and is not in Y_(alpha,1); the finite renormalized split of proof 186 or proof 190 is still required. A common target and bounded local maps remove a mismatch of norm definitions, but do not establish a complement inverse, a closed cubic normalization or a nonlinear theorem.

Dependencies: topics39 and117 for the exact residual expansions and V120 for nonvanishing; topics200,201,203 for E2 strain and origin inversion; topics208-210 for the no-support source inverse and its reflection-invariant extension. All new norm comparisons, completeness and localization claims are proved above. There is no numerical calculation.
