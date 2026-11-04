# Tail rigidity with an A2 scalar weight

Status: CONFIRMED at the exact conditional or countertest scopes in A596, A597. Full independent proof postread completed. The unrestricted campaign conjecture is not proved.

## 1. Exact statements and notation

Let D=R3 minus{0}, 1/3<c<1/2, p=(1-c)/c in(1,2), a=1-2c, beta=(p-1)/(2p), A=cI-omega J, Jx=(-x2,x1,0), Q_t=exp(omega tJ) and T_t=exp(tA). The real number omega is arbitrary and finite. Let S be C1 on D with S(T_t x)=exp(-2(1-c)t)S(x). Set b=|S|^beta. Assume b is locally A2: b>0 almost everywhere, b and its reciprocal are locally integrable, and the products of their ball averages have a finite bound on each compact subdomain. Assignments on null sets are irrelevant.

Core theorem. Suppose Y is locally Lipschitz on D, has continuous actual distributional curl Z, and satisfies

    div Y=0, Y(T_t x)=exp(-(1-c)t)Q_t^T Y(x),
    grad S cross Y=(S/beta)Z.

Then Y=0.

Global-rank corollary. Suppose V is C1 and divergence free on D with the same velocity homogeneity. Write W=curl V, k=(Ax).V and E=grad k. If W.grad S=0 and E cross grad S=0 on ALL D, then V=0. No Poisson equation, symmetry, global E0 or separate helicity premise is required in this standalone corollary.

Localization corollary. Instead let V be locally C1,alpha for every0<alpha<1, impose rank only where W!=0, and retain W.grad S=0 everywhere. Then W!=0 implies k,S!=0, and E=0 implies V=0 at that point. This does not assert V=0 globally.

The only substantial imported analytic regularity theorem is the signed weak-solution continuity in Fabes, Jerison and Kenig, The Wiener test for degenerate elliptic equations, Ann. Inst. Fourier32(3)(1982),151-182, Definition1.3 and estimates(1.7)-(1.8), printed154-156. Its primary statement and completed Lipschitz solution space have been read. The underlying FKS theorem is imported, not independently reproved. The proof below establishes the needed completion; it uses neither a weighted maximal theorem nor reverse Holder. In particular it does not use the visibly defective printed typography of FJK display(1.6).

## 2. A2 across the spatial origin

Put d=p-1 in(0,1). Exact homogeneity gives b(T_t x)=exp(-at)b(x). Consequently b(r theta)=r^-d b(R_r theta) for an axial rotation R_r. Integrate b and its reciprocal on1<r<2 by Tonelli; rotational invariance of spherical measure gives finite positive constants

    B_plus=integral_S2 b, B_minus=integral_S2 b^-1.

This conclusion uses annular integrability, not a trace theorem for a general integrable function. Exact covariance holds pointwise off the null scalar nodes and permits the calculation. Thus

    integral_(r<R)b=B_plus R^(3-d)/(3-d),
    integral_(r<R)b^-1=B_minus R^(3+d)/(3+d).

For B(x,R) with |x|<=2R, enclose it in B(0,3R). The two average bounds are C R^-d and C R^d, so their product is uniformly bounded. If |x|>2R, use T_t to put the center on S2 and reduce the radius below1/2. Covariance makes the product of averages invariant. These balls lie in one compact annulus. A finite cover of that annulus by local A2 neighborhoods handles all sufficiently small balls by a Lebesgue number. The remaining radii have a positive lower bound, so annular integrability bounds both averages. This proves a global A2 bound on R3 after arbitrary assignments at0 and on the null nodes. No constant is claimed uniform in omega.

## 3. Weighted approximation and the initially unbounded potential

We prove the needed functional-analytic facts for any global A2 weight w on R3. A ball-average A2 bound implies a cube bound by enclosing cubes in comparable balls. Let rho_epsilon be a nonnegative mollifier bounded by C epsilon^-3, supported in a ball of radius epsilon. Partition space into disjoint cubes Q of side epsilon, and let Q* be concentric with a fixed larger side, sufficient to contain every point sampled from Q. Cauchy-Schwarz gives

    integral_Q w|rho_epsilon*f|^2
      <=C epsilon^-6 w(Q) w^-1(Q*) integral_Q* |f|^2w
      <=C K integral_Q* |f|^2w,

where K is the global A2 constant. Enlarged cubes have bounded overlap, hence the convolution operators have a uniform L2(w) norm. Compactly supported continuous functions are dense for the locally finite regular measure w dx; their mollifiers converge uniformly with common compact support. Uniform boundedness therefore proves convergence in L2(w) for every f in that space. Exactly the same bound applies to normalized ball averages, since kernel smoothness was unused.

If u and its ordinary weak derivatives lie locally in L2(w), multiply by a smooth compact cutoff inside the domain. The product lies in ordinary W1,1 by Cauchy-Schwarz with w^-1, and its zero extension has no boundary derivative. Mollification commutes with weak differentiation and converges for the function and all derivatives in L2(w). Thus u lies in the local completion of Lipschitz functions for the weighted function-and-gradient norm.

We still need to show the function integral for a potential whose gradient alone is known. For a smooth u on a ball B of radius R, average the line-segment fundamental theorem of calculus over y in B. With z=x+t(y-x), the Jacobian is t^-3 and the segment factor contributes |z-x|/t; necessarily t>=|z-x|/(2R). Integrating t^-4 yields

    |u(x)-average_B u|<=C integral_B |grad u(z)|/|x-z|^2 dz.

Split this integral into dyadic distance annuli with radii r_j=2^(1-j)R. It is at most C sum_j r_j average_(B(x,r_j)) (|grad u|1_B). The uniform weighted averaging bound and Minkowski give

    ||u-average_B u||_L2(B,w)<=C R ||grad u||_L2(B,w).

The weighted mean minimizes distance to constants, so it may replace the ordinary mean. By the approximation already proved, the same estimate holds for functions known to be in the completed space.

Now suppose u is locally W1,1 and grad u locally L2(w). Its truncation u_M=max(-M,min(u,M)) is bounded and has gradient1_{|u|<M}grad u almost everywhere, so both weighted integrals are finite and the preceding density result applies. The weighted Poincare estimate bounds ||u_M-m_M||_L2(w) uniformly in M, with m_M its weighted mean. Since u is finite almost everywhere and w>0 almost everywhere, some measurable E in B of positive w measure has |u|<=M0. For M>=M0,

    |m_M|<=M0+w(E)^(-1/2)||u_M-m_M||_L2(B,w).

Thus the means and the full norms of u_M are uniformly bounded. Fatou proves u in L2(B,w). Dominated convergence for u_M and its gradient then gives convergence in the weighted norm. This proves the precise completed energy membership without presupposing boundedness or continuity of u.

## 4. A global closed factor and its additive homogeneity

Under the core theorem's assumptions, weak product differentiation gives

    curl[(S^2+epsilon^2)^(-beta/2)Y]
      =epsilon^2(S^2+epsilon^2)^(-beta/2-1)Z.

Its right side tends to0 almost everywhere and is dominated locally by b^-1|Z|. The vector on the left converges locally in L1 to G=Y/b. Therefore curl G=0 in distributions on ALL D, including every node. This checks explicitly that no nodal curl survives. No inverse power beyond b^-1 is used.

To construct a potential, mollify G on a slightly larger ball, integrate the smooth closed fields and fix their ordinary mean on the smaller ball. The usual L1 Poincare inequality makes these potentials Cauchy in W1,1. On overlaps their differences are constants. Since D is simply connected, a loop homotopy subdivided into balls makes the constants consistent. Thus there is a global locally W1,1 real potential psi with grad psi=G and div(b grad psi)=div Y=0.

Bounded Y on compact subsets gives integral b|grad psi|^2=integral |Y|^2/b<infinity. Section3 now supplies its function integral and completed space. Smooth distributional tests extend to compact Lipschitz tests by mollification with uniformly bounded gradients and dominated convergence against b; completion and Cauchy-Schwarz then extend to all tests in the required energy space. The FJK signed-solution estimates apply to the coefficient bI and give continuity on D. Nonnegativity is required only for the separate Harnack estimate(1.9), which is not used here.

The exact degrees give G(T_t x)=T_t^(-T)G(x). By the weak chain rule, psi(T_t x)-psi(x) has zero weak gradient on connected D. It is constant, and the continuous representative makes this pointwise. The constants are continuous and additive in t, hence equal gamma t for a real gamma:

    psi(T_t x)=psi(x)+gamma t.

Moving x to S2 yields |psi(x)|<=C(1+|log|x||). This step retains the possible logarithmic drift rather than assuming gamma0.

## 5. Removal of the origin and proof of the core theorem

Velocity homogeneity and compactness of S2 give |Y(x)|<=C r^-p. The spherical reciprocal-weight integral is finite, so

    integral_(r<epsilon)|Y|^2/b<=C epsilon^(2-p),
    integral_(r<epsilon)|G|<=C epsilon^2.

The first exponent follows from radial integrand r^(2-2p+d)=r^(1-p). Also psi is weighted square integrable at0 from its logarithmic bound and the b-volume formula. Its weak derivative extends through0: the inner-cutoff error is bounded by C epsilon^2(1+|log epsilon|). The divergence of Y similarly has cutoff error epsilon^-1 integral_(epsilon<r<2epsilon)|Y|<=C epsilon^(2-p), which tends to0. Thus div(b grad psi)=0 globally, with no hidden point charge.

For completeness, if chi_epsilon vanishes below epsilon and equals1 above2epsilon, then

    integral b|grad(chi_epsilon psi-psi)|^2
      <=C epsilon^(2-p)(1+|log epsilon|)^2 ->0.

The weighted function error tends to0 too. For fixed epsilon, completion away from0 and a finite partition of unity approximate the cut-off function by Lipschitz functions. A diagonal sequence gives the completed space on a ball containing0. Alternatively Section3 now applies directly to the verified weak derivative and weighted integrals there.

FJK continuity therefore holds at0. Sending t to minus infinity in psi(T_t x)=psi(x)+gamma t first gives gamma0, then psi(x)=psi(0) for every x. Hence G0 and Y0. This proves the core theorem; p<2 is essential to these cutoff estimates.

## 6. Global rank and one constant on a whole vortical component

For a C1 homogeneous velocity,

    Ax cross W=aV+E, Ax.grad S=-2(1-c)S,
    Ax.E=-ak.

Global rank and W.grad S0 turn the cross product of the first identity with grad S into grad S cross V=(S/beta)W. The core theorem applies and proves the global-rank corollary.

For localization let C be one connected component of {W!=0}. The same cross identity holds on C; the regularized proof of Section4 gives curl(V/b)=0 on C, including its scalar nodes. The spiral preserves C, because it preserves W!=0 and each orbit segment is connected. For G=V/b on C, distributional homogeneity is DG Ax=-A^T G. Curl G0 makes DG symmetric in distributions. Thus

    grad[(Ax).G]=A^T G+(DG)^T Ax=0.

A distribution with zero gradient on connected C is constant. Since k and b are continuous and b>0 almost everywhere, this yields ONE real constant d_C with k=d_C b on all C. Constants on separate scalar chambers are not treated as independent.

If d_C=0, then k=E=0 on C. On its boundary in D, continuity gives W=E=0, so the cross identity gives V=0. Extend Y=V on C and0 outside. It is locally Lipschitz: for two points on opposite sides of the boundary, use the first exit point of their joining segment and the local bound for DV. Its weak derivative is DV on C and0 almost everywhere off C, including almost every boundary point because a Lipschitz function has derivative0 almost everywhere on its zero set. Consequently div Y0 and curl Y=Z, the continuous extension of W by0. The spiral preserves Y's homogeneity. Globally Ax cross Z=aY and Z.grad S0, so the core theorem gives Y0, contradicting W!=0 on C. Thus d_C!=0.

## 7. A2 excludes a scalar node when the component constant is nonzero

Suppose S(x0)=0 in C. The relation b=k/d_C makes b nonnegative and locally C1,alpha for every alpha<1. At x0, b=grad b=0. Choose an affine transverse disk sigma(z), z in R2, to Ax0 and set Phi(t,z)=T_t sigma(z). On a smaller box this is a smooth diffeomorphism with bounded Jacobian, derivative and inverse derivative. Covariance gives

    b(Phi(t,z))=exp(-at)w0(z), w0(z)=b(sigma(z)).

Local A2 is preserved by this coordinate map: images of sufficiently small balls lie in comparable physical balls, their volumes are comparable, and Jacobians are bounded above and below. Multiplication by exp(at), bounded and positive on the box, also preserves A2. The resulting weight w0(z), independent of t, is A2 in three dimensions. Testing on product cubes of equal side in t,z1,z2 cancels the t-length and gives the two-dimensional A2 condition for w0, with some finite constant K. Fubini gives positivity almost everywhere and local integrability of w0 and v0=w0^-1 in two dimensions.

Let Q_r=(-r,r)^2 and E_r=Q_r minus Q_(r/2). Then |E_r|=3|Q_r|/4. Cauchy-Schwarz and A2 imply

    |E_r|^2<=v0(E_r)w0(E_r)<=v0(E_r)w0(Q_r),
    w0(Q_r)v0(Q_r)<=K|Q_r|^2.

Hence v0(E_r)>=9v0(Q_r)/(16K). Writing theta=1-9/(16K) in(0,1),

    v0(Q_(r/2))<=theta v0(Q_r).

Iteration and comparison of adjacent dyadic radii give v0(Q_r)<=C r^delta with delta=-log(theta)/log2>0. This is an elementary mass-decay argument; no reverse-Holder import is required.

On the other hand, C1,alpha regularity and the nonnegative zero imply w0(z)<=C_alpha |z|^(1+alpha). Integrating the reciprocal lower bound gives v0(Q_r)>=c_alpha r^(1-alpha). Choose alpha<1 sufficiently near1 that1-alpha<delta. The lower bound then exceeds the upper bound for small r, a contradiction. Thus S has no zero in C, and k=d_C b has no zero there either.

If E0 at a vortical point, Ax.E=-ak forces k0, already excluded. If E0 and W0, Ax cross W=aV+E directly gives V0. This proves the localization corollary. A single unspecified Holder exponent or C1 alone does not give this proof.

## 8. Full-profile application and limits

In the target interval2/5<c<1/2, assume the full C2 velocity/C1 pressure profile, U->0, global U.curl U=0 and natural bounds |U|<=C(1+r)^-p, |DU|<=C(1+r)^(-p-1). The independently confirmed gradient results allow decay plus DU=O(sqrt r) in place of the natural bounds. These premises supply actual C1,alpha tails for every alpha<1, C2,alpha canonical pressure, W.grad S0 and rank on {W!=0}. If |S|^beta is A2, localization excludes E0,V!=0 tail witnesses, including the lower escaping sheets. This alone is not full nonexistence.

If rank holds on ALL D as well, the global-rank corollary gives V0. Rank transfer from original exterior-vorticity density, or exterior analyticity unless U0, is independently reconstructed in the team records. Neither density nor analyticity supplies the A2 property. The alternative S identically0 is a separate branch: the exact Poisson mean in A591 forces V0 although the A2 condition then fails.

Once V0, the full spiral remainder gives U=O(r^(-q)) with q=2p+1>3, and P-Pinf=O(r^-2p). The exact cutoff energy identity has bulk coefficient1-5c/2!=0. Its dilation, cubic and pressure boundary terms are respectively O(R^(3-2q)), O(R^(2-3q)) and O(R^(2-2p-q)); each tends to0. Therefore U0.

Every strict radial surface/curve chart and transverse product chart from the earlier nodal results is A2 by the elementary power-weight average test. The present theorem removes prescribed nodal geometry, but not its analytical substance. The exact local high-order analytic constructions fail reciprocal-weight integrability and do not contradict it. No global canonical-pressure nonzero tail or full Euler counterexample is constructed. No computation is used in this proof.
