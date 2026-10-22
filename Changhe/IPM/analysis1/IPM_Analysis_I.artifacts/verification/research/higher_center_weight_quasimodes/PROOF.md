# Center quasimodes after imposing finitely many velocity moments

This new argument is OPEN until independent review and the stated input checks are complete. It extends the degree-two construction to a family of more singular center weights. It is not a statement about existence of a stationary IPM profile.

## Statement

Let 0<k<1/2, L>0, ell=1/k, c=3ell-1, and let rho have the background properties of center_weighted_quasimodes/PROOF.md: even-x, odd-y reflection symmetry, rho=x^2 y+O(r^5), |grad rho|<=C r^2, |Hess rho|<=C r near0, local C^{4,a} regularity for some a>0, canonical velocity U[rho] that is C2 near0 and satisfies

    U[rho](0)=0, DU[rho](0)=diag(-c,c),

and |rho|+r|grad rho|+r^2|Hess rho|<=C r^k at infinity. The canonical velocity of a smooth compact density h satisfies

    -Delta psi[h]=partial_x h,
    U[h]=(-partial_y psi[h],partial_x psi[h]),
    Sigma(h)=partial_xy psi[h](0).

It is selected by its reflection parities and sublinear growth. Set D=X dot grad and

    L_rho h=(ell X+U[rho]) dot grad h-h
              +U[h] dot grad rho+(Sigma(h)/3)D rho.

For each fixed integer m>=2 define the weighted weak H1 norm

    ||h||_(X_m)^2=integral_R2 (h^2+r^2|grad h|^2) w_m(r) dX,
    w_m(r)=L^(2m+2) r^(-2m-2)(1+r^2/L^2)^(m-k-1/2).

Let X_m be the real space of reflection-symmetric functions with finite displayed norm and Cartesian weak first derivatives. At infinity w_m is a positive constant times r^(-2k-3). X_2 is exactly the previous diagnostic X.

There is a sequence h_j of smooth compact densities, all supported in r<=2, vanishing near0 and near both axes inside their support, with smooth global factors h_j=x^2y b_j, b_j even-even, such that

    J(h_j)=Sigma(h_j)=0,
    ||h_j||_(X_m)=1,
    ||L_rho h_j||_(X_m)->0,
    ||h_j||_(H^(m+1/2))->0,
    h_j converges weakly to0 in X_m.                       (1)

In addition, all Cartesian Taylor coefficients of U[h_j] at0 of degrees at most m-2 vanish. For m=2 this last condition is weaker than Sigma=0. Every sequence member has zero leading far coefficient.

Consequently a finite same-X_m inverse estimate fails on any graph domain containing this sequence. A bounded B:X_m->X_m cannot have a defect supremum below1 there. No estimate with an H^(m+1/2) remainder, or with any compact linear map from X_m to a Banach space as remainder, holds. Every closed realization T:D(T) subset X_m ->X_m containing the sequence and agreeing with L_rho on it fails to have both closed range and finite kernel.

Each m is fixed before all choices. No estimate uniform in m is asserted. The result concerns weighted H1 norms, not norms controlling additional derivatives. It does not cover graph domains excluding this sequence or forcing norms different from the input norm.

## Critical homogeneous degree and angular cutoffs

Write

    alpha=1-2ell, beta=4ell-1, d=beta-alpha=6ell-2,
    p=(beta m-1)/d, q=(1-alpha m)/d.

Then p+q=m and alpha p+beta q=1. At m=2 these are the exponents in the preceding construction. Since beta>0 and -alpha>0,

    p=p_2+(m-2)beta/d, q=q_2+(m-2)(-alpha)/d.

Thus p,q>1/2 for every m>=2. The homogeneous function

    H(x,y)=|x|^p sign(y)|y|^q=r^m F(theta)

solves (AX dot grad-1)H=0 in every open quadrant, where A=diag(alpha,beta). Put

    a(theta)=alpha cos^2 theta+beta sin^2 theta,
    b(theta)=(beta-alpha)sin theta cos theta,
    T_m Z=b Z'+(m a-1)Z.

Thus T_m F=0 on the quadrants. Choose a smooth cutoff chi on[0,infinity), zero on[0,1] and one on[4,infinity), and restrict0<e<1/4. Define

    chi_e(theta)=chi(sin^2 theta/e^2)chi(cos^2 theta/e^2),
    F_e=chi_e F, G_e=T_m F_e=b chi_e' F.

Then F_e is smooth with the required reflections and vanishes near the axes. Moreover F_e->F in H1 of the circle and G_e->0 in H1. Indeed, near an axis the exponent nu is p or q. The cutoff transition has width O(e), b=O(e), cutoff first and second derivatives have orders e^-1 and e^-2, and F,F' have orders e^nu,e^(nu-1). Therefore G_e and G_e' have orders e^nu and e^(nu-1). Their squared integrals have orders e^(2nu+1) and e^(2nu-1), which tend to0 because nu>1/2. The same estimate proves F_e->F. The limit is nonzero.

## Compact logarithmic annuli

Fix0<delta<1/4 within the disc of the background estimates, t0=log delta, and a smooth zeta with values in[0,1], zero on(-infinity,0] and one on[1,infinity). For N>2-t0 set

    eta_N(t)=zeta(t+N)zeta(t0-t),
    f_(e,N)=r^m eta_N(log r)F_e(theta).

It is smooth, supported in exp(-N)<r<delta, and vanishes near each axis. Division by x^2y extends by zero across those axis neighborhoods and the center, so its global factor is smooth and even-even. In particular J=0.

Polar differentiation gives, for any smooth eta and Z with the indicated compact radial support,

    ||r^m eta(t) Z(theta)||_(X_m)^2
      =L^(2m+2) integral (1+exp(2t)/L^2)^(m-k-1/2)
        [eta^2 Z^2+(m eta+eta')^2 Z^2+eta^2(Z')^2] dt dtheta.  (2)

The radial factor lies between1 and a fixed constant on t<=t0. Define

    A_m(Z)^2=integral_circle ((1+m^2)Z^2+(Z')^2).

The plateau of length N+t0-2 gives

    ||f_(e,N)||_(X_m)>=L^(m+1)sqrt(N+t0-2) A_m(F_e).       (3)

For L0=AX dot grad-1,

    L0 f_(e,N)=r^m eta_N G_e+r^m eta_N' a F_e.

Equation(2) and the bounded length of the two cutoff transitions imply

    ||L0 f_(e,N)||_(X_m)<=C_m sqrt(N) A_m(G_e)+C_(m,e).    (4)

Constants with an e subscript need only be finite for each fixed e. The remaining C_m is independent of e,N.

## Uniform Sobolev bounds

For fixed m,e, the annular family is uniformly bounded in H^s, s=m+1/2. Use a smooth radial dyadic partition of unity on0<r<=delta. Each localized piece at radius R<=1 has the form R^m g(X/R), where g is supported in a fixed annulus with uniformly bounded derivatives through order m+1. These bounds follow from the explicit radial logarithmic factors, whose derivatives in log radius are uniform in N. They are also uniform in R, for fixed m,e. The Fourier scaling formula gives

    ||R^m g(X/R)||_(H^s)^2
       =R^(2m+2) integral (1+|xi|^2/R^2)^s |hat g(xi)|^2 dxi
       <=R^(2m+2-2s)||g||_(H^s)^2
       =R||g||_(H^s)^2.

Since ||g||_(H^s)<=||g||_(H^(m+1)) is uniformly bounded, the triangle sum of R^(1/2) proves sup_N ||f_(e,N)||_(H^s)<infinity.

The Fourier velocity multiplier is

    M(xi)=(xi_x xi_y/|xi|^2,-xi_x^2/|xi|^2), |M|<=1.

It preserves H^s bounds. Fourier Cauchy-Schwarz gives a uniform C^{m-1} bound for U[f_(e,N)], because

    integral_R2 (1+|xi|)^(2(m-1))(1+|xi|^2)^(-s) dxi

is finite: its large-radius radial power is2(m-1)-2s+1=-2. Lower derivatives satisfy the same conclusion. These Fourier velocities are canonical by their Darcy identities, decay and reflection parities. No boundedness of a singular integral on L-infinity is asserted.

## The finite center moments and their exact correction

For a smooth compact density h vanishing near0, let Gamma_n(h) be the coefficient of r^n sin(n theta) in the harmonic expansion of psi[h] near0, for even n>=2. The stream is odd in x and y, so these are the only possibly nonzero homogeneous stream terms; a constant has no velocity and is excluded by the stream parity. The coefficient Gamma_n is a fixed linear combination of derivatives of U[h] of order n-1 at0. In particular Sigma(h)=2 Gamma_2(h).

Here is a formula that also constructs independent corrections. Define the density Fourier coefficient

    F_l(r)=(1/pi) integral_0^(2pi) h(r,theta)sin(l theta) dtheta.

For even n>=2, the sin(n theta) source coefficient of partial_x h is

    g_n=(F_(n-1)'-(n-1)F_(n-1)/r
                 +F_(n+1)'+(n+1)F_(n+1)/r)/2.

The regular-at-zero, sublinear-velocity Green solution has central coefficient

    Gamma_n(h)=(1/(2n)) integral_0^infinity r^(1-n) g_n(r)dr
              =(1/2) integral_0^infinity r^(-n) F_(n+1)(r)dr. (5)

The second equality follows by integration by parts. For F_(n-1), the derivative contributes n-1 and cancels its negative n-1 term. For F_(n+1), it contributes n-1, which added to n+1 gives2n before the factor1/2 in g_n. All boundary terms vanish because h is compact and vanishes near0. The Fourier projection and derivatives are justified for smooth compact h; only one selected angular mode at a time is used. The Green coefficient follows by solving the scalar radial Poisson equation; regularity excludes r^-n near0 and sublinear velocity excludes a growing homogeneous r^n term at infinity. Thus no finite angular truncation is required.

Let S_m be the finite set of even integers n with2<=n<=max(2,m-1). It includes2 even when m=2. Choose a nonnegative nonzero smooth radial chi0 supported in1<r<2. Choose a smooth nonnegative angular phi, even under both coordinate reflections, vanishing in neighborhoods of the axes and positive on some open arc. For l in S_m define preliminary densities

    B_l(r,theta)=chi0(r) phi(theta) sin((l+1)theta).

They are smooth and compact and have global smooth even-even factors after division by x^2y. Formula(5) gives

    Gamma_n(B_l)=I_n G_(n,l)/(2pi),
    I_n=integral_0^infinity r^(-n)chi0(r)dr>0,
    G_(n,l)=integral_0^(2pi) phi(theta)sin((n+1)theta)sin((l+1)theta)dtheta.

The real matrix G is positive definite. If a linear combination has zero quadratic form, the finite trigonometric polynomial sum z_n sin((n+1)theta) vanishes on an open arc where phi>0. Multiplying by a sufficiently high power of exp(i theta) turns it into a polynomial in exp(i theta) with infinitely many distinct roots, so it is identically zero. Orthogonality of distinct sine frequencies then gives every z_n=0. Consequently diag(I_n/(2pi))G is invertible. Define fixed real linear combinations b_l of the B_l so that

    Gamma_n(b_l)=delta_(n,l), n,l in S_m.                 (6)

These functions depend on m but not on e or N. Their coefficients are exact real numbers defined by the finite integrals and matrix inverse. No numerical value of that inverse is being presumed.

For fixed m,e, all Gamma_n(f_(e,N)) are uniformly bounded in N. Indeed, n-1<=m-2 for n<=m-1; for the extra n=2 when m=2, n-1=m-1. Each is therefore controlled by the C^{m-1} velocity bound just proved. Set

    q_(e,N)=sum_(l in S_m) Gamma_l(f_(e,N)) b_l,
    v_(e,N)=f_(e,N)-q_(e,N).

Then Gamma_n(v_(e,N))=0 for n in S_m, so Sigma(v_(e,N))=0. The correction is supported in1<r<2, while f is supported in r<delta. Thus

    ||v_(e,N)||_(X_m)^2=||f_(e,N)||_(X_m)^2+||q_(e,N)||_(X_m)^2,

and in particular the lower bound(3) also holds for v. The correction and v are uniformly bounded in H^s for fixed m,e. All center normalization and factor properties are preserved.

## Taylor cancellation and the full nonlocal term

The density v vanishes on some neighborhood of0 for each N, so its stream is harmonic there. Its reflection symmetries allow only the even stream degrees n>=2. Cancelling Gamma_n for n<=m-1 removes all velocity homogeneous degrees at most m-2. The remaining constant velocity is already zero by parity. Thus all Cartesian derivatives of U[v] at0 through order m-2 vanish. For m=2 this only asserts U[v](0)=0, and the extra Gamma_2 condition supplies Sigma(v)=0 separately.

The global C^{m-1} velocity bound is uniform in N for fixed m,e. Taylor's theorem along radial segments therefore yields, throughout the fixed center disc,

    |U[v](X)|<=C_(m,e) r^(m-1),
    |DU[v](X)|<=C_(m,e) r^(m-2).                         (7)

The radius on which v itself vanishes may shrink with N; this causes no loss. Harmonicity is used only to identify the derivatives at0, while the Taylor remainder in(7) uses uniform derivative bounds on the whole fixed disc.

Combining(7) with the two background derivative bounds gives

    |U[v] dot grad rho|<=C_(m,e) r^(m+1),
    |grad(U[v] dot grad rho)|<=C_(m,e) r^m.

Their squared X_m norm near0 is controlled by integral_0^delta r dr. At infinity, the fixed support r<=2 and uniform L1 bound give |U[v]|<=C_(m,e)r^-2 and |DU[v]|<=C_(m,e)r^-3 for r>=4. The product and its gradient then have orders r^(k-3) and r^(k-4). With w_m=O(r^(-2k-3)), the squared norm uses integral_4^infinity r^-8 dr. On the intervening compact region all quantities are bounded. Hence the nonlocal product has uniformly bounded X_m norm for fixed m,e.

This argument estimates the corrected v directly. For m>=3, D rho need not belong to X_m, and the individual images of f and the correction need not belong to X_m. We do not subtract their separate norms. The rank-one term of the full expression is exactly zero because Sigma(v)=0.

## The remaining transport error and normalization

Near0, V=ell X+U[rho]=AX+O(r^2) and DV=A+O(r). The explicit annular f has derivative bounds of orders r^m,r^(m-1),r^(m-2), uniformly in N for fixed m,e. Thus

    |(V-AX) dot grad f|<=C_(m,e)r^(m+1),
    |grad((V-AX) dot grad f)|<=C_(m,e)r^m.

Their X_m norm is bounded by the same integral r dr. The correction q has fixed support in1<r<2 and bounded coefficients. Its local transport image therefore has bounded X_m norm. Combining these local estimates, (4), and the corrected nonlocal bound yields

    ||L_rho v_(e,N)||_(X_m)<=C_m sqrt(N)A_m(G_e)+C_(m,e).  (8)

Here the decomposition is between local transport expressions, which are all in X_m, and the single full nonlocal product of v. It is not a decomposition into potentially nonintegrable full images of f and q.

Choose e_j tending to0 with A_m(F_(e_j)) bounded below and A_m(G_(e_j))->0. For each j choose N_j sufficiently large that all fixed-e constants in(8), and the fixed-e uniform H^s bound for v, divided by the lower bound(3), are at most1/j. The ratio sqrt(N_j) divided by that lower bound remains bounded. Normalize v by its exact X_m norm. This proves every strong convergence and exact normalization assertion in(1).

## Weak convergence and operator consequences

The space X_m is Hilbert by the same direct weighted-L2 completeness argument: on every bounded disc w_m and r^2w_m have positive lower bounds, so the limits of a norm-Cauchy function and its gradients also converge in ordinary local L2, and distributional testing identifies the gradient limits. The reflection subspace is closed.

Since s=m+1/2>=5/2, the H^s convergence implies uniform convergence of h_j and grad h_j. For any g in X_m, split its inner product with h_j into r<a, a<=r<=2, and r>2. Cauchy-Schwarz bounds the first by ||g||_(X_m,r<a), which tends to0 as a tends to0. On the fixed annulus the weights are bounded, so uniform convergence gives convergence to0. Outside2 the sequence vanishes. Taking j to infinity first proves weak convergence to0.

The reverse triangle inequality gives ||h_j-B L_rho h_j||>=1-||B|| ||L_rho h_j||->1 for bounded B. The H^s-remainder estimate is contradicted directly by(1). A compact linear map sends the weakly-null sequence to a norm-null sequence: every norm-convergent image subsequence has zero pairing with every bounded functional, and hence zero limit by Hahn-Banach. This proves the compact-remainder assertion.

Finally, for a closed realization T containing the sequence, its graph norm makes D(T) Hilbert, ||h_j||_graph->1, and h_j is graph-weakly null. If its kernel were finite dimensional, the graph-orthogonal projection P onto the kernel would satisfy ||P h_j||_graph->0. If its range were also closed, the restriction from the graph-orthogonal complement of the kernel to its range would be a bounded Banach-space bijection. The Banach inverse theorem would imply ||h_j-P h_j||_graph<=C||T h_j||, contradicting the limits1 and0. No density assumption is needed, and closedness is a hypothesis rather than a conclusion.

## Dependencies and verification scope

All critical identities, the finite moment-correction argument and the analytic estimates are given above. The problem-specific application uses the already accepted canonical modal background and its exact normalization. The inherited degree-two result is a consistency check, not a replacement for the new moment-cancellation proof. The standard Fourier representation, Taylor theorem, finite-dimensional linear algebra, Banach inverse theorem and Hahn-Banach separation are the stated analytic dependencies.

Before acceptance, check the two-variable exponent identities and radial/Fourier powers with two independent exact algebra paths; reconstruct the Green moment factors and angular parity; rehash the canonical-trial evidence; obtain complete actual Claude Opus5.5 review and resolve every substantive objection with a later adjudication. No finite matrix of sampled moments is used to infer invertibility; the positive-definite Gram argument proves it for every fixed finite S_m.

The conclusions apply separately to every fixed integer m>=2 and to graph domains containing the constructed functions, with the same X_m norm on input and image. They do not rule out estimates with higher derivative norms, distinct input and forcing norms, or stronger domain restrictions. They do not establish nonlinear stationarity, distance to X3, nonexistence of a profile, or a decisive IPM Analysis I endpoint.
