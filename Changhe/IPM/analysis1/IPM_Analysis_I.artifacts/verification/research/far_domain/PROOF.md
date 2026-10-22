# Far-field domain obstruction and normalization for the full-plane IPM operator

Status: analytic proof written before computation and review. The result is conditional on an exact profile with the stated properties. It is an obstruction to a proposed operator domain, not a nonexistence theorem for profiles.

## Statement, notation and hypotheses

Let X=(x,y), r=|X|, E=X dot grad and <r>=(1+r^2)^(1/2). Let rho be a nonzero real C1 function on the plane and U a C1 divergence-free velocity, satisfying

V=c_l X+U, V dot grad rho=rho, c_l>1, U(X)=o(r).

Assume also the P2 far bounds |rho|+(1+r)|grad rho|<=C(1+r)^delta for some delta<1. No homogeneous angular asymptotic expansion is assumed. Set k=1/c_l. The first result uses only the equation, nontriviality, C1 regularity and U=o(r). Define

H_gamma=L2(R2,<r>^(-2gamma)dX).

Then rho does not belong to H_gamma for any gamma<1+k. For 1<gamma<1+k, neither E rho nor K=(E-1)rho belongs to H_gamma.

Use ell[h]=psi[h]_{xy}(0) and delta c_l[h]=ell[h]/3 throughout. This distinguishes the strain ell from the prompt's scaling functional c[h]. Suppose U is the canonical IPM inverse of rho. On a compact smooth perturbation h the full normalized linearization is

Lh=(V dot grad-1)h+U[h] dot grad rho+(ell[h]/3)E rho.  (1)

There are compact smooth h with the density parities, zero near both axes and the origin, and ell[h]>0. Each such example lies in the usual compact test core of the proposed correction space. Nevertheless Lh is not in H_gamma when 1<gamma<1+k. In particular a proposed full forcing space contained in H_gamma cannot contain the image of that test core under (1).

The scaling family rho_lambda(X)=lambda^(-1)rho(lambda X), lambda>0, preserves the canonical equation at fixed c_l. Under local C3 regularity with rho=x^2 y+o(r^3), its tangent K has x^2 y coefficient2. It is therefore removed by the coefficient normalization if it belongs to a chosen domain. In the H_gamma-based space just described it does not belong to the domain in the first place. Neither fact determines the dimension of a kernel or cokernel.

## Nonzero transported mass forces far-field nonmembership

The C1 vector field V has at most linear growth, because U=o(r) outside a compact set and is bounded on compact sets. Its flow Phi_t exists uniquely for every real t. The elementary differential inequality 1+|Phi_t(X)|<=C_X exp(C|t|) excludes finite-time escape. Along the flow,

rho(Phi_t X)=exp(t)rho(X), det D Phi_t(X)=exp(2c_l t).  (2)

The first identity is the profile equation and the second follows from div V=2c_l and the initial determinant1.

Choose 0<epsilon<c_l. For all r>=R_epsilon, U(X) dot X/r^2 is between -epsilon and epsilon. Along any trajectory outside that radius,

(c_l-epsilon)r <= d r/dt <= (c_l+epsilon)r.  (3)

A trajectory starting at rho(X0)!=0 cannot stay in any fixed ball for all positive time: (2) would contradict boundedness of the continuous rho on that ball. It thus exits the radius R_epsilon. Once it exits, the positive lower bound in (3) prevents inward re-entry. By continuity, there is a small compact patch A outside that radius, of positive area, with |rho|>=m>0 there. Every forward image Phi_t(A) stays outside and has r<=C_A exp((c_l+epsilon)t).

Let 0<gamma<1+k. Choose epsilon still smaller so that d=1+c_l-gamma(c_l+epsilon)>0. Changing variables in the weighted square norm on Phi_t(A), using (2) and the radius bound, gives

integral_{Phi_t(A)} <r>^(-2gamma)|rho|^2 dX
 >= C exp(2[1+c_l-gamma(c_l+epsilon)]t) integral_A |rho|^2 dX.  (4)

Here C>0 is independent of t>=0; <r> is bounded above by another constant times exp((c_l+epsilon)t). If the total H_gamma norm were finite, it would bound the left side for every t, contrary to (4). No disjointness of the images is required. For gamma<=0 choose gamma' in (0,1+k) with gamma'>gamma. H_gamma is contained in H_gamma', so nonmembership follows. This proves the claim for every gamma<1+k and for every exterior region after increasing R.

## Two weighted radial Hardy arguments

Work on r>=R>=1, where <r>^(-2gamma) and r^(-2gamma) are comparable. Set t=log r, a=gamma-1>0 and v(t,theta)=exp(-a t)rho(exp(t),theta). The exterior H_gamma norm with the pure radial weight is precisely the L2(dt dtheta) norm of v.

If E rho belongs to H_gamma, put q=exp(-a t)E rho. Then v'+a v=q, so

v(t)=exp(-a(t-t0))v(t0)+integral_{t0}^t exp(-a(t-s))q(s) ds.  (5)

The first term is in L2 because the circle trace is continuous and finite. Young's inequality in the Hilbert space L2(dtheta), proved by Minkowski's integral inequality, bounds the second term by (1/a)||q||_2. Thus E rho in H_gamma would imply rho in H_gamma, which is impossible. This proof includes the boundary trace and does not infer the statement merely from a formal leading exponent.

For K=(E-1)rho, let b=2-gamma>0; positivity follows from gamma<1+k<2. Now v'-b v=q with q=exp(-a t)K. The P2 sublinear bound implies

exp(-b T)v(T)=exp(-T)rho(exp(T),theta) ->0 uniformly in theta.  (6)

Integrating the equation backwards from infinity is therefore justified. If q is in L2, its integral converges by Cauchy-Schwarz and

v(t)=-integral_t^infinity exp(-b(s-t))q(s) ds,
||v||_2 <= (1/b)||q||_2.  (7)

The uniform limit (6) removes the growing homogeneous solution. Again this contradicts nonmembership of rho. The hypotheses delta<1 and gamma<2 are essential to this argument as stated.

## A compact perturbation with nonzero canonical strain

Choose a nonnegative nonzero smooth cutoff chi, even in each coordinate, supported in a compact set disjoint from both axes. Ensure its support is not confined to the algebraic zero set of y(3x^2-y^2), which is automatic for a nonzero smooth function. Set

h(x,y)=y(3x^2-y^2)chi(x,y).  (8)

It is even in x and odd in y, and vanishes near the origin. Its cubic normalization coefficient is zero. For compact h the canonical Poisson fundamental solution is G(Z)=-(1/(2pi))log|Z| and psi[h]=partial_x G * h. There is no harmonic strain. Because h vanishes near0, differentiation under this integral has no singularity at0. Direct differentiation gives

partial_x^2 partial_y log|Z|=2 z_y(3 z_x^2-z_y^2)/|Z|^6,
ell[h]=integral y(3x^2-y^2)/(pi r^6) h(X) dX
        =integral y^2(3x^2-y^2)^2 chi(X)/(pi r^6) dX >0.  (9)

The sign in (9) includes evaluation of the kernel at -X. It is not the sign of the derivative kernel at +X.

For a concrete example, put eta(s)=exp(-1/((s-1)(2-s))) for1<s<2 and zero otherwise, and chi(x,y)=eta(|x|)eta(|y|). This is a smooth cutoff with the required support and parities. On each of the four reflected rectangles5/4<=|x|,|y|<=7/4, chi>=exp(-32/3), |y|>=5/4, 3x^2-y^2>=13/8 and r^2<=49/8. Their combined area is1. Thus the explicit lower bound is

ell[h] >= [4225/(235298 pi)]exp(-32/3).  (9a)

The forthcoming two interval methods enclose the right side, not a numerical approximation to the full strain integral. This suffices for strict nonzero strain without a quadrature assumption.

If supp h is contained in r<=R_h, the local term -h e2/2 is zero for r>R_h. The canonical velocity there is an ordinary integral against the prompt's two kernels. Their component absolute values are at most1/(2pi|Z|^2). For r>=2R_h, |X-Y|>=r/2 gives

|U[h](X)| <= (4/pi)r^(-2)||h||_L1.  (10)

The displayed constant safely exceeds2sqrt(2)/pi. Hence U[h] dot grad rho=O(r^(delta-3)), which belongs to H_gamma for gamma>1. On compact sets it is bounded. Outside supp h, the correct exact equation is

Lh=U[h] dot grad rho+(ell[h]/3)E rho.  (11)

It is false to drop the first term merely because h is compactly supported. By (9), (10) and nonmembership of E rho, the sum (11) is not in H_gamma. This establishes the domain obstruction. It is consistent with existence of an exact profile in a larger space, or a formulation with explicit tail coordinates.

## Embedding of the proposed jet-plus-remainder far norm

This paragraph only checks the zeroth-order far norm. Let a>0 and let phi be bounded. For x!=0 use the remainder weight

omega=x^(-2a)<r>^(2(a-gamma))exp(phi).

Since |x|<=<r>, omega>=exp(inf phi)<r>^(-2gamma). A remainder with finite weighted norm thus belongs to H_gamma. For j=1,2 use a fixed bounded cutoff chi_0 supported on |x|<=C<y> and the jet extension

E_{2j}a_{2j}=x^(2j)chi_0(x/<y>)a_{2j}(y).

On its support <r> is comparable to <y>. Integrating |x|^(4j) over |x|<=C<y> yields a bound by a constant times <y>^(4j+1). Therefore

||E_{2j}a_{2j}||_{H_gamma}^2
 <=C_{chi_0,j,gamma} integral <y>^(4j+1-2gamma)|a_{2j}(y)|^2 dy.  (12)

If the full proposed norm includes these two jet norms and the remainder norm, the sum embeds in H_gamma by the triangle inequality. Compact h as in (8) has zero jets, lies in the smooth remainder test core, and satisfies every local vanishing constraint. Neither adding the jet norms nor imposing the cubic normalization repairs (11). An unbounded correction weight phi or a different tail space would require a separate analysis.

## Scaling covariance and scope

For the canonical inverse, U[rho_lambda](X)=lambda^(-1)U[rho](lambda X). To prove uniqueness directly, a difference of two such velocities has zero div and curl. Its components are entire harmonic functions. The interior gradient estimate on a ball of radius R bounds each derivative at any fixed point by C/R times the supremum on that ball. Sublinear growth makes this bound tend to zero as R tends to infinity, so the difference is constant. The specified parity sets that constant to zero. Dilation of U has div0, curl equal to -partial_x rho_lambda, the required parity and sublinear growth, hence it is this unique canonical velocity. The rescaled transport field is V_lambda(X)=lambda^(-1)V(lambda X), rather than the unscaled background field V(X). Consequently F(rho_lambda)(X)=lambda^(-1)F(rho)(lambda X) at the same c_l. The strain ell[rho_lambda]=ell[rho] is constant in lambda. Whenever differentiation in lambda is justified, K=(E-1)rho satisfies

L K=(E-1)F(rho), ell[K]=0.  (13)

At an exact profile F=0 this is a formal linearized solution, without implying K belongs to any domain. Under local C3 regularity, the cubic coefficient of rho_lambda is lambda^2, whose derivative at1 is2. Fixing that coefficient to1 removes this direction only in a space where it is present and the coefficient evaluation is continuous. P2 with merely a continuous factor requires a separate argument for differentiating the center condition, so the cubic coefficient assertion here retains its explicit C3 hypothesis.

These proofs do not establish a Fredholm index, compactness of the coupling, boundedness of a complete nonlinear map, existence of a stationary profile, or an exclusion neighborhood. Computations below check exact algebra and illustrative parameter inequalities, not the existence of the unknown profile used in this conditional theorem.
