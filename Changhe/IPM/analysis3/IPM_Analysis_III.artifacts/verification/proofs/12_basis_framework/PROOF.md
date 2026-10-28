# Conformity, Gram matrices, and what a finite section can certify

## Scope and the interface test

This topic gives exact criteria for auditing Avenue IV. It supplies no missing complement inverse. Let L be the full normalized linearization defined in proof 01 at a background whose coefficients have the stated local regularity. On an interface Gamma away from the origin and infinity, suppose h is continuous, piecewise C2, has continuous tangential derivatives, and its canonical U[h] is continuous. The latter follows, for example, for the piecewise smooth globally locally Lipschitz basis functions with the admitted sublinear tails, by local singular-integral regularity and a smooth exterior contribution. Assume grad rho and G=X dot grad rho are continuous at Gamma.

Then the jump in the full image is exactly

    [Lh] = (V dot n)[partial_n h].                        (1)

Indeed the trace of -h is continuous, the two velocity couplings are continuous, and the jump of grad h has only its normal component. If the right side is nonzero on a positive-length interface segment, Lh has a jump there and cannot belong to H1 locally. Its distributional gradient contains the nonzero jump times the normal surface measure, which is not an L2 function. A nonzero jump in h itself likewise excludes h from H1, however small its numerical size.

Consequently exact C1 matching is a sufficient local interface condition for piecewise smooth basis functions to have h and Lh in H1 locally. C0 matching alone is insufficient unless the exceptional flux cancellation in (1) is proved. Local conformity does not establish origin, axis-factor or infinity membership; those are separate checks. At circular joins r=R, radial C1 matching in t=log r is equivalent to spatial radial C1 matching because R>0.

A defining B-spline with exact knots and exact control coefficients is conforming at its simple internal knots. Exporting separately rounded polynomial coefficients creates a different piecewise function. The latter must have its own exact matching identities; a small floating residual is not such an identity. Exact rational nullspaces of endpoint matching matrices can define valid joined functions if every matrix entry is actually rational under the chosen local exponential coordinates. If endpoint exponentials enter those matrices, rationality must not be assumed.

## Exact angular Gram matrices

For h(r,theta)=r^3 sum_(m=0)^(M-1) b_m(log r) Phi_m(theta), put

    Phi_m=cos^2 theta sin theta cos(2m theta).

Use sin(-n theta)=-sin(n theta). The exact finite sine expansion is

    Phi_m=[sin((1+2m)theta)+sin((1-2m)theta)
           +sin((3+2m)theta)+sin((3-2m)theta)]/8.

Let d_(n,m) be the resulting rational coefficient of sin(n theta), n positive odd. Then

    A0_(m,j)=pi sum_n d_(n,m)d_(n,j),
    A1_(m,j)=pi sum_n n^2 d_(n,m)d_(n,j).

These give the exact angular value and derivative matrices without trigonometric floating quadrature. For any radial weight w(r), the genuine weighted spatial H1 Gram is

    integral [b^T A0 b +(3b+b')^T A0(3b+b')+b^T A1 b]
                                           e^(8t) w(e^t) dt. (2)

Cross terms are understood by polarization. This follows directly from r^2|grad h|^2=|partial_t h|^2+|partial_theta h|^2 and dX=e^(2t)dt dtheta.

Replacing (2) by a diagonal norm of the factor coefficients is a different infinite-dimensional norm unless a uniform comparison is proved. In fact multiplication of an angular factor by cos^2 theta sin theta has no uniformly bounded inverse in H1. A smooth factor concentrated in an epsilon-neighborhood of theta=pi/2 has factor H1 norm of order epsilon^(-1/2), while the multiplied density angular H1 norm is of order epsilon^(3/2). Their ratio tends to zero as epsilon^2. Reflection gives the required even-even factor parity. Trigonometric polynomials approximate each fixed smooth example in H1, so no uniform comparison is restored by considering arbitrarily large finite Fourier sections. Finite-section comparison constants may exist and deteriorate with dimension.

## Exact finite bandwidth, and its limits

Suppose the background has Mb factor modes m=0,...,Mb-1 and an input column has Mh factor modes m=0,...,Mh-1. Their density sine frequencies are at most 2Mb+1 and 2Mh+1. The Poisson forcing partial_x rho has even frequencies at most one greater than those of rho; radial inversion does not add angular frequencies. In polar coordinates the velocity coupling is a Jacobian of the stream function and density, divided by r. Its largest frequency is therefore at most the sum of a stream frequency and a density frequency. Both bilinear terms have frequencies at most

    2(Mb+Mh)+3.

The scalar transport and rank-one term obey smaller bounds. Thus Lh has no sine mode above index N=Mb+Mh+1 when the sine convention is sin((2N+1)theta). Keeping all indices 0,...,Mb+Mh+1 safely captures every angular mode of that column. If an input column uses all Mb tail modes, set Mh=Mb.

This statement applies to the explicit finite modal density. The raw X3 density is the exponential of an angular expansion and generally has infinitely many density modes. Finite bandwidth of its logarithm is not finite bandwidth of the density. In either case, angular bandwidth alone says nothing about the infinite-dimensional radial input complement.

## Finite section and off-section image from exact Grams

Let X,Y be Hilbert spaces and phi_1,...,phi_N in D(L) linearly independent, with images in Y. Let psi_1,...,psi_M in Y be linearly independent and let P,Q be the orthogonal projections onto their respective spans. Write

    GX_(i,j)=<phi_j,phi_i>_X,
    GY_(i,j)=<psi_j,psi_i>_Y,
    B_(i,j)=<L phi_j,psi_i>_Y,
    H_(i,j)=<L phi_j,L phi_i>_Y.

Then the matrix of QL on the input section is GY^(-1) B. Its smallest singular value in the continuum norms is that of

    GY^(-1/2) B GX^(-1/2).                               (3)

The exact squared off-section norm is the largest eigenvalue of

    GX^(-1/2) [H-B* GY^(-1) B] GX^(-1/2),               (4)

where * is adjoint. To prove this, the coefficients of the orthogonal projection of Lh solve GY y=B x. Pythagoras gives ||(I-Q)Lh||_Y^2=x*[H-B*GY^(-1)B]x, while ||h||_X^2=x*GX x. Taking the extreme Rayleigh quotients proves (3)-(4).

Thus a verified Loewner inequality H-B*GY^(-1)B <= epsilon^2 GX certifies the off-section column error. All matrices and inversions must be enclosed with rounding and integration errors. A sampled row matrix is not automatically B or H. It requires a proved relation between its row functional and the chosen continuum norm. Finite samples cannot dominate the full norm on an unrestricted radial function space: a nonzero smooth function can vanish at every sampled radius, even with all sampled derivatives zero, by being supported strictly between them.

Taking the output space to contain the exact images of all input columns makes (4) zero by definition. This can be a valid finite-section choice, but it does not bound the action on the input complement.

## Block inverse theorem with domains

Assume D(L) is a linear domain invariant under P and containing ran P. Put X0=ran P, X1=ker P, Y0=ran Q, Y1=ker Q and D1=D(L) intersect X1. Define

    A=QL|X0, B=QL|D1, C=(I-Q)L|X0, D=(I-Q)L|D1.

Suppose D:D1->Y1 is bijective and its inverse is bounded from Y1 to X1 with bound d. In addition assume BD^(-1):Y1->Y0 is bounded with bound e; this is an independent domain/mapping requirement if L is unbounded on X. The finite block C is bounded, with bound c. Let

    S=A-BD^(-1)C

be bijective X0->Y0 with inverse bound s. Then L:D(L)->Y is bijective, with

    x0=S^(-1)(f0-BD^(-1)f1),
    x1=D^(-1)f1-D^(-1)C x0.                              (5)

Both terms in x1 lie in D1, so (5) is a domain-valid solution. Substitution proves Lx=f; the same identities with f=0 prove uniqueness. For the orthogonal Hilbert sum norms,

    ||L^(-1)|| <= norm_2 [[s, s e],
                         [d c s, d(1+c s e)]].           (6)

The matrix on the right bounds the two output component norms from the two forcing component norms, so its Euclidean operator norm proves (6). No compactness of a Riesz term is required or inferred. If s,d,e or the domain hypotheses are missing, finite singular values alone do not give (6).

## Why a purely finite-rank approximate inverse cannot close

Let D be any infinite-dimensional linear subspace of X and B:Y->X have finite rank. For any linear L:D->Y, the map BL has finite rank and therefore has a nonzero kernel in D. For such h,

    ||h-BLh||_X=||h||_X.

Hence an inequality ||I-BL||<1 on D in the X norm is impossible. If BL extends boundedly to X, its operator-norm defect is at least one. An infinite-dimensional analytic component is necessary for this form of certification. Increasing a finite basis never changes that argument.

## Audit scope

The supplied c2_fminus.py and c2_gram2.py implement a floating collocation construction, broken piecewise energies, numerical nullspaces, and sampled derivative rows. Their own comments now distinguish these from a continuum certificate. The formulas above define what must be rebuilt and checked. They do not certify the numerical singular values in those files, nor do they assert that the new numerics team has completed its planned exact construction. In the diagnostic X_m spaces, the confirmed center quasimodes of proof 05 also obstruct the required complement estimate on natural domains. A different factor or anisotropic norm must be assessed on its own terms.
