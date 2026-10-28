# Generation and the Fredholm consequence for rough small perturbations

## Exact statement

Use the exact background, fixed repeller-block order s, weights, cutoffs, coefficient space G_s, remainder space X_s and operators T_g,S_g,D_g of proof 158. In particular

 T_g h=(V+U[g]+c[g]X/3).grad h-h,
 S_g=T_g+C_R,
 D_g={h in X_s:T_g h in X_s in distributions}.

There is a qualitative radius r_*>0 such that, for every g in G_s with ||g||G_s<=r_*:

1. T_g with domain D_g generates a strongly continuous semigroup on X_s. Its semigroup bound can be chosen uniformly for this ball.
2. S_g:D_g->X_s is Fredholm of index zero. The same is true of S_g-lambda for every real lambda>=0, with its own graph realization.
3. If S_0:D_0->X_s is injective, then, after decreasing r_* if necessary, every S_g is bijective and

 ||h||X_s+||T_g h||X_s<=C||S_g h||X_s, h in D_g,        (1)

with C independent of g.

The injectivity in item3 is an explicit additional hypothesis and is not established by this theorem. No numerical value of the radius or constant is asserted. The theorem concerns the remainder operator with fixed coupling C_R; the full scalar-axis block and moving-tail parameter are not included in this statement.

## An equivalent positive energy

Let A_j and A_j^u be the bulk and cofactor reductions of proof 157. Its frame proof also gives

 ||v||H^s<=C(||J_s v||_(l2 L2)+||v||L2).                (2)

Indeed the annular parametrix absorbs all sufficiently large j; the finitely many remaining frequency bands have bounded weights and are controlled by L2. There is no need to presume invertibility of a bare order reduction. The same estimate holds at the cofactor order sigma. Hence

 E(h)=sum_j ||A_j v||L2^2+sum_j ||A_j^u u||L2^2
                              +||v||L2^2+||u||L2^2     (3)

is the square of a fixed Hilbert norm equivalent to X_s. The closed trace condition defines a closed subspace for this norm.

For a sufficiently regular solution of partial_tau h=T_g h, the dyadic energy calculation in topics157-158, without the positive matrix or elliptic penalty argument, gives

 dE(h)/d tau<=C E(h),                                  (4)

uniformly on the small coefficient ball. To verify the sign, -Re<A_j T_g h,A_j h> contains the nonnegative logarithmic coefficient (W+B_g).grad s. Its lower bound is minus a fixed lower-order norm squared, hence minus C E. All remaining matrix coefficients are bounded; the rough coefficient commutator is bounded by proof 156 and (5) of proof 158. The cofactor cutoff forcing is bounded by C times the bulk high norm and is absorbed into C E. At ordinary L2 level the divergence and divided scalar coefficients are bounded. These give the final two terms in (3). No positive energy margin is needed for (4).

## Smooth approximation of the perturbation and the flow

The density construction at the end of proof 155 gives g_n of the same parity, with a fixed free cubic jet and a smooth annular remainder, such that g_n->g in G_s and ||g_n||G_s<=2r_*. Decrease the initial radius so that this larger ball still has the robust sign (6) of proof 158. Its normalized velocity fields B_n converge to B_g uniformly with their first derivatives, and in the coefficient Sobolev norms on the vertical sectors. Every B_n is smooth with all cylinder derivatives bounded; those higher bounds need not be uniform. W has the fixed W^(7,infinity) regularity. Thus W+B_n has a global Lipschitz flow and sufficient finite regularity to transport all the Sobolev orders up to25/4 in this argument.

Let Phi_n(tau,X) be the cylinder flow of W+B_n. The physical transport solution is the pullback along that flow with its scalar exponential factor. In bulk cylinder variables its formula is

 v_n(tau,X)=exp(integral_0^tau c_n(Phi_n(a,X)) da)
                                     v_0(Phi_n(tau,X)),
 c_n=beta(q+B_(n,r))-1.                                (5)

The cofactor formula agrees with (5) after division by p and the fixed angular cutoff. On the vertical axis its uncut divided equation uses the coefficient beta(q+B_(n,r))+(p'/p)(vartheta+B_(n,theta))-1, which has the bounds in proof 158. The flow is tangent to each axis because its angular component vanishes there. Thus it preserves parity and the zero cofactor trace. The same conclusion follows directly by transporting that trace; no reflection-breaking approximation is used.

For smooth normalized initial data with compact radial support, the flow, its scalar factor and the divided cofactor factor are W^(7,infinity) on every bounded time interval. The support remains in a bounded radial interval because the cylinder field is bounded. Consequently both transformed components belong to H7 there, which is above the maximum order25/4. This justifies their membership in X_s before using (4), without presuming bounded pullback on the final rough variable-order space. This is the same core argument used in proof 126. One may perform the energy argument first for finite frequency sums and then use their summable bounds. Equation(4) gives

 E(h_n(tau))<=exp(C tau) E(h_0), tau>=0,                 (6)

with C independent of n. The fixed-order cofactor and variable-order bulk versions are covered by the same dyadic proof. The monotonicity of the order is what makes this a forward semigroup estimate; a backward high-space bound is neither needed nor asserted.

The fields converge in C^1_b, so their flows converge uniformly on compact time intervals and compact spatial sets, together with first derivatives. Their scalar factors in (5) converge there as well. Thus the physical functions converge locally to the pullback h(tau) defined by the limiting Lipschitz flow. Uniform boundedness in (6), weak compactness in X_s and local distributional convergence identify this limit uniquely in X_s and prove

 E(h(tau))<=exp(C tau) E(h_0).                           (7)

Extend the solution from the dense normalized smooth data to all of X_s by this bound. The extension equals the same local pullback, so the semigroup property follows from the flow identity.

For completeness, strong continuity does not follow merely from weak compactness. The flow formula gives distributional continuity at zero. Together with (7), every weak subsequential limit in X_s is h_0. Weak lower semicontinuity and (7) then give convergence of the norm E^(1/2) to E(h_0)^(1/2). In a Hilbert space, weak convergence plus convergence of the norms implies strong convergence. This proves strong continuity at zero on the dense initial set, and then on X_s by the uniform bound. The semigroup property gives it at every nonnegative time.

## Identification of the generator domain

Write G_g for the semigroup generator. Differentiating (5) against smooth compactly supported test functions shows G_g h=T_g h in distributions for h in its generator domain. Hence Dom(G_g) is contained in D_g.

Conversely, let h in D_g and f=T_g h in X_s. The minimum bulk order is41/20>2, so h/b is C^1 locally in cylinder coordinates. The fixed physical weights are smooth on every annulus, so the physical h is also C^1 there. The limiting flow is C^1, and f agrees with the continuous first-order expression T_g h. The chain rule along the flow therefore gives pointwise on every compact annulus

 U_g(tau)h-h=integral_0^tau U_g(a)f da,                 (8)

where U_g is the semigroup just constructed. The right side is a Bochner integral in X_s, by its strong continuity. Both sides define the same distribution, so (8) is an equality in X_s. Divide by tau and let tau decrease to zero. Strong continuity yields the derivative f in X_s. Thus h belongs to Dom(G_g), proving Dom(G_g)=D_g. This argument uses neither a common domain for different g nor a graph-core assumption.

By equivalence of E and the original norm, there are fixed M,omega such that ||U_g(tau)||<=M exp(omega tau) on this ball. The Laplace integral therefore gives, for real lambda>omega,

 ||(lambda-T_g)^(-1)||<=M/(lambda-omega).               (9)

## Fredholm continuation

C_R is a fixed bounded operator on X_s. The bounded perturbation theorem, or a direct Neumann series using (9), shows that S_g-lambda is invertible for all sufficiently large real lambda, uniformly in the small ball. Fix such a Lambda_0.

Proof 158 gives a compact-error estimate for S_g-lambda on every bounded interval0<=lambda<=L. For each fixed g the domain is D_g throughout this lambda path, and

 ||h||D_g<=C_g(||(S_g-lambda)h||X_s+||Kh||W_*).

Indeed T_g h=(S_g-lambda)h-C_Rh+lambda h. The compact map K on X_s is compact on graph-bounded subsets. Peetre's lemma gives finite-dimensional kernel and closed range. The path in lambda is norm continuous as a path of bounded operators D_g->X_s. The upper semi-Fredholm continuation argument already checked in proof 150 applies: from the invertible endpoint it remains Fredholm of index zero throughout the interval. If an initially Fredholm branch approached a point with infinite cokernel, nearby Fredholm operators would have arbitrarily large negative index, contradicting the constant index zero; this is the standard extended-index local constancy for upper semi-Fredholm operators. This proves item2 at lambda=0 and on any finite interval. No norm-continuous variation of D_g with g is asserted or needed.

## Uniform inverse under base injectivity

Suppose S_0 is injective. We prove a uniform lower bound on a sufficiently small ball by contradiction. If none exists, choose g_n->0 in G_s and h_n in D_(g_n) with

 ||h_n||X_s=1, ||S_(g_n) h_n||X_s->0.                  (10)

Take a weakly convergent subsequence h_n weakly converging to h in X_s. The fixed compact map K from proof 158 gives K h_n->K h strongly. In distributions,

 S_0 h_n=S_(g_n)h_n-B_(g_n).grad(h_n/b)b
                                      -beta B_(g_n,r)h_n.

The new terms tend to zero locally: B_(g_n)->0 in C^1_b and h_n is bounded in the local H^s space with s_min>2. The fixed coupling is bounded on X_s, hence weakly continuous. Therefore S_0 h=0 in distributions. Since C_R h is in X_s, this also gives T_0 h=-C_R h in X_s; thus h belongs to D_0. Injectivity implies h=0.

Apply the uniform compact-error estimate of proof 158 to h_n. Its right side tends to zero by (10) and K h_n->0, contradicting ||h_n||X_s=1. Hence there are a smaller radius and C_0 with ||h||X_s<=C_0||S_g h||X_s on that ball. Each S_g is Fredholm of index zero by item2, so this injectivity and closed range imply surjectivity. Finally T_g h=S_g h-C_R h gives (1).

## Scope and remaining obligations

This theorem supplies qualitative uniform high regularity for the small frozen-coupling remainder family, conditional on the single base injectivity assertion for its inverse conclusion. It gives no numerical smallness threshold. The complete nonlinear problem still requires the full scalar-axis block, control of the moving far-field family, low inverse consistency, a residual small enough in a closed target space, and explicit constants for a contraction or a posteriori theorem. None is inferred from the compact-error estimate alone.
