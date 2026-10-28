# Center quasimodes with actual saddle coefficients

Status: an analytic theorem under the exact hypotheses below. This proof covers the normalized modal definition in proof 04. Its application to raw X3 still requires a verified bound for its actual central strain. It neither asserts a kernel nor excludes other inverse norms.

## Statement and spaces

Let ell and c be real numbers, set a=ell-c, b=ell+c, and suppose

    a<0<b,   p_2=(2b-1)/(b-a)>1/2,   q_2=(1-2a)/(b-a)>1/2.       (1)

Let rho be even in x and odd in y, C^2 on compact sets, with canonical velocity U[rho]. Assume that for some delta>0 and finite constants,

    |grad rho(X)|<=C r^2,  |D^2 rho(X)|<=C r,                  r<=delta,
    V=ell X+U[rho](X)=B X+E(X), B=diag(a,b),
    |E(X)|<=C r^2, |DE(X)|<=C r,                              r<=delta,
    |rho|+r|grad rho|+r^2|D^2 rho|<=C r^k,                    r>=1,       (2)

where 0<k<1/2. Assume V is C^1 on compact sets. These assumptions concern the actual background, not a sampled matrix. The canonical velocity of a smooth compact perturbation h is the Fourier multiplier

    U[h]hat=(xi_x xi_y/|xi|^2,-xi_x^2/|xi|^2) hhat,

and c[h]=psi[h]_xy(0). Fix L>0, any scalar gamma, and an integer m>=2. Define

    w_m=L^(2m+2) r^(-2m-2)(1+r^2/L^2)^(m-k-1/2),
    ||h||_(X_m)^2=integral (h^2+r^2|grad h|^2)w_m dX,
    L_gamma h=V.grad h-h+U[h].grad rho+gamma c[h] X.grad rho.          (3)

X_m uses Cartesian weak derivatives and the given reflection parities. In particular X_2 is the diagnostic X. A domain for L_gamma must require its full expression, not each summand separately, to lie in X_m.

There are real smooth compact h_j, supported in r<2 after choosing delta<1/4, with a smooth global even-even factor h_j=x^2 y b_j, such that

    J(h_j)=b_j(0)=0, c[h_j]=0,
    ||h_j||_(X_m)=1, ||L_gamma h_j||_(X_m)->0,
    ||h_j||_(H^(m+1/2))->0, h_j weakly converges to 0 in X_m.         (4)

Each h_j vanishes near the origin and near the axes on its support. All derivatives of U[h_j] at the origin of orders at most m-2 are zero. Each has zero far coefficient.

Consequently any linear realization containing this sequence fails a same-X_m bounded-below estimate. For every bounded B_0:X_m->X_m its defect supremum on the realization is at least one. No estimate of the form

    ||h||_(X_m)<=C(||L_gamma h||_(X_m)+||h||_(H^(m+1/2)))

holds on a domain containing the sequence. The same is true with the final term replaced by the norm of any compact linear map from X_m into a Banach space. A closed realization containing the sequence cannot have both closed range and finite-dimensional kernel.

The scalar gamma is arbitrary because c[h_j] is exactly zero. This includes gamma=1/3 for the normalized nonlinear equation and gamma=0 when ell is held fixed. No identity 3ell-c=1 is required for the theorem.

## Homogeneous transport and the angular domain

For each m put

    p=(bm-1)/(b-a), q=(1-am)/(b-a).

Then p+q=m and ap+bq=1. Since b>0 and -a>0, p=p_2+(m-2)b/(b-a) and q=q_2+(m-2)(-a)/(b-a) exceed 1/2. Thus

    H=|x|^p sign(y)|y|^q=r^m F(theta)

solves (BX.grad-1)H=0 away from the axes. Define

    A(theta)=a cos^2(theta)+b sin^2(theta),
    Btheta(theta)=(b-a)sin(theta)cos(theta),
    T_m Z=Btheta Z'+(m A-1)Z.

Then T_m F=0 on each quadrant. Near an axis, F has magnitude O(s^nu) and first derivative O(s^(nu-1)), where s is angular distance and nu is p or q. The threshold nu>1/2 proves F in H^1(S^1), with F not identically zero.

Choose a smooth cutoff chi equal to zero on [0,1] and one on [4,infinity). Let

    chi_e=chi(sin^2(theta)/e^2)chi(cos^2(theta)/e^2),
    F_e=chi_e F, G_e=T_m F_e=Btheta chi_e' F.

F_e is smooth and vanishes near every axis. It has the required parities. On a transition s comparable to e, Btheta=O(e), Btheta'=O(1), chi_e'=O(e^-1), chi_e''=O(e^-2). Hence G_e=O(e^nu), G_e'=O(e^(nu-1)). Their squared angular integrals are respectively O(e^(2nu+1)) and O(e^(2nu-1)). The analogous estimates for F-F_e give

    F_e->F in H^1, G_e->0 in H^1.                                 (5)

This argument checks the angular weak derivative at the axes; an H^2 limit is neither needed nor asserted.

## The logarithmic annulus and its exact norm

Fix delta<1/4 in (2), t0=log(delta). Choose smooth zeta valued in [0,1], zero for t<=0 and one for t>=1. For N>2-t0 set

    eta_N(t)=zeta(t+N)zeta(t0-t),
    f_(e,N)=r^m eta_N(log r) F_e(theta).

It is smooth, vanishes near zero and the axes, and is supported in exp(-N)<r<delta. Its quotient by x^2 y extends smoothly by zero near the axes. Every derivative of eta_N of a fixed order is bounded independently of N. Its nonconstant regions have uniformly bounded total length.

For any smooth eta and Z with compact logarithmic radial support, direct polar differentiation gives

    ||r^m eta Z||_(X_m)^2
      =L^(2m+2) integral (1+exp(2t)/L^2)^(m-k-1/2)
          [eta^2 Z^2+(m eta+eta')^2 Z^2+eta^2(Z')^2] dt dtheta.      (6)

The radial power cancels because r^(2m) r^(-2m-2) r dr=dr/r. Define A_m(Z)^2=integral ((1+m^2)Z^2+(Z')^2). On the plateau eta_N=1 over a length N+t0-2. Since m-k-1/2>0,

    ||f_(e,N)||_(X_m)>=L^(m+1) sqrt(N+t0-2) A_m(F_e).               (7)

The frozen image is

    (BX.grad-1)f_(e,N)=r^m eta_N G_e+r^m eta_N' A F_e.

Equation (6), bounded cutoff derivatives through order two, and fixed transition lengths imply

    ||(BX.grad-1)f_(e,N)||_(X_m)
        <=C_m sqrt(N) A_m(G_e)+C_(m,e).                            (8)

The first constant is independent of e,N. The second need only be finite for each e.

## Sobolev control that is uniform in N

Use a fixed smooth dyadic partition on 0<r<=delta. A piece at radius R<=1 has the form R^m g(X/R). For fixed m,e, g is supported in one fixed annulus and has uniformly bounded derivatives through order m+1, independently of R,N. This follows from the explicit logarithmic derivatives of eta_N. For s=m+1/2, the Fourier scaling formula gives

    ||R^m g(X/R)||_(H^s)^2
      =R^(2m+2) integral (1+|xi|^2/R^2)^s |ghat(xi)|^2 dxi
      <=R^(2m+2-2s)||g||_(H^s)^2=R||g||_(H^s)^2.

The triangle inequality and the convergent sum of R^(1/2) show that f_(e,N) is uniformly bounded in H^s. The vector velocity multiplier has Euclidean norm at most one, so U[f_(e,N)] has the same uniform H^s bound. Fourier Cauchy-Schwarz implies a uniform C^(m-1) velocity bound: the radial power in the highest-derivative dual integral at infinity is

    2(m-1)-2s+1=-2,

which is integrable. Its integral at zero is also finite. These bounds apply to continuous classical derivatives, by the absolute Fourier integrals.

## Exact cancellation of the finite velocity jet

For a smooth compact h vanishing near zero, the stream is harmonic there. Its odd-x, odd-y parity permits only r^n sin(n theta) with even n>=2. Let Gamma_n(h) be that coefficient. Then c[h]=2 Gamma_2(h). Let

    F_l(r)=(1/pi)integral h(r,theta)sin(l theta)dtheta.

The sin(n theta) component of partial_x h is

    g_n=(F_(n-1)'-(n-1)F_(n-1)/r
              +F_(n+1)'+(n+1)F_(n+1)/r)/2.

Solving the radial Poisson equation gives Gamma_n=(1/(2n))integral r^(1-n)g_n dr. Integration by parts, whose boundary terms vanish by the compact support away from zero, cancels the F_(n-1) terms and combines the F_(n+1) terms. Therefore

    Gamma_n(h)=(1/2)integral r^(-n)F_(n+1)(r)dr.                    (9)

Let S_m be the even n in 2<=n<=max(2,m-1). Choose nonnegative smooth chi0 supported in 1<r<2 and a smooth nonnegative angular phi invariant under both coordinate reflections, zero near the axes and positive on an open arc. For l in S_m let

    B_l=chi0(r)phi(theta)sin((l+1)theta).

These are smooth compact admissible densities with smooth quotients by x^2 y. Equation (9) yields

    Gamma_n(B_l)=I_n G_(n,l)/(2pi),
    I_n=integral r^(-n)chi0(r)dr>0,
    G_(n,l)=integral phi sin((n+1)theta)sin((l+1)theta)dtheta.

G is positive definite. A zero quadratic form would force a finite sine polynomial to vanish on the open arc where phi>0. Multiplication by a power of exp(i theta) turns it into a polynomial with infinitely many distinct roots. It is identically zero; sine orthogonality gives all coefficients zero. Thus the displayed moment matrix is invertible. Exact real linear combinations b_l of the B_l can be chosen with Gamma_n(b_l)=delta_(n,l).

The derivatives at zero of U[f_(e,N)] through order m-1 are uniformly bounded. Hence every Gamma_n(f_(e,N)), n in S_m, is uniformly bounded: Gamma_n is a fixed linear combination of order n-1 velocity derivatives. Define

    q_(e,N)=sum_(l in S_m) Gamma_l(f_(e,N)) b_l,
    v_(e,N)=f_(e,N)-q_(e,N).                                    (10)

The coefficients and the H^s norm of q are uniformly bounded in N for fixed m,e. Its support is disjoint from that of f, so ||v||_(X_m)^2=||f||_(X_m)^2+||q||_(X_m)^2 and (7) remains a lower bound. Equation (10) gives c[v]=0 and removes every velocity Taylor degree through m-2. The extra Gamma_2 for m=2 enforces strain zero even though the required zero-order jet already vanishes by parity.

## Membership and the complete image estimate

Taylor's theorem applied to the uniformly bounded C^(m-1) velocities, with all lower jets zero, gives on the entire fixed center disk

    |U[v](X)|<=C_(m,e)r^(m-1), |DU[v](X)|<=C_(m,e)r^(m-2).        (11)

The source-free disk for each v may shrink with N. It is used only to identify the Taylor coefficients at zero. The remainder estimate in (11) uses uniform derivative bounds on the whole fixed disk and does not require that disk to be source-free.

Combining (11) with (2) shows

    |U[v].grad rho|<=C_(m,e)r^(m+1),
    |grad(U[v].grad rho)|<=C_(m,e)r^m.

Its center squared norm is bounded by C integral_0^delta r dr. At infinity the fixed compact support and uniform L^1 norm of v imply, by the nonsingular differentiated Green kernel,

    |U[v]|<=C_(m,e)r^-2, |DU[v]|<=C_(m,e)r^-3, r>=4.

Thus the density product and its derivative have orders r^(k-3) and r^(k-4). Since w_m=O(r^(-2k-3)), the squared far norm is bounded by C integral_4^infinity r^-8 dr. The intervening compact annulus is controlled by the uniform C^1 velocity bound. Therefore the full nonlocal product is uniformly bounded in X_m.

The scalar term is exactly zero, since c[v]=0. For m>=3, X.grad rho need not lie in X_m. It would be invalid to estimate the images of f and q separately in X_m, because each can have a nonintegrable cubic contribution. We have estimated the combined nonlocal velocity U[v] instead.

For the remaining local error, |D^j f|<=C_(m,e)r^(m-j), j=0,1,2. Equation (2) therefore gives |E.grad f|<=C_(m,e)r^(m+1) and |grad(E.grad f)|<=C_(m,e)r^m, whose X_m norm is uniformly bounded. The local image V.grad q-q is supported in the fixed annulus 1<r<2 and is uniformly bounded. Combining these estimates with (8) proves both L_gamma v in X_m and

    ||L_gamma v_(e,N)||_(X_m)<=C_m sqrt(N)A_m(G_e)+C_(m,e).        (12)

## Normalization, weak limit and operator consequences

Choose e_j->0 such that A_m(F_(e_j)) stays bounded below and A_m(G_(e_j))->0. For each j choose N_j large enough that every fixed-e remainder and the H^s bound, divided by the lower bound (7), are at most 1/j. Normalize v_(e_j,N_j) by its exact X_m norm. This yields all strong limits and exact constraints in (4).

For g in X_m, split its pairing with h_j into r<epsilon and epsilon<=r<=2. The first contribution is at most ||g||_(X_m,r<epsilon), which tends to zero as epsilon->0. On the fixed annulus, h_j and its first derivatives converge uniformly to zero by H^s convergence and s>=5/2. Thus the second pairing tends to zero. Outside r<=2, h_j vanishes. This proves weak convergence in X_m.

X_m is Hilbert: on every bounded disk both weights w_m and r^2w_m have positive lower bounds, so a norm-Cauchy sequence and its gradients converge in local L^2; distributional testing identifies the limiting gradients. The parity subspace is closed.

The bounded-below and H^s-remainder conclusions follow by substitution of (4). The reverse triangle inequality gives ||h_j-B_0 L_gamma h_j||>=1-||B_0||||L_gamma h_j||, proving the defect bound. A compact linear map sends a bounded weakly null sequence to a norm-null sequence, since every convergent image subsequence has all bounded functional pairings zero. This proves the compact-remainder conclusion.

Finally let T be a closed realization containing the sequence. Its graph is a Hilbert space with norm squared ||h||_(X_m)^2+||Th||_(X_m)^2. The sequence has graph norm tending to one and is graph-weakly null. If ker T is finite dimensional, its graph-orthogonal projection of h_j tends to zero. If ran T is also closed, the restriction of T from the graph-orthogonal kernel complement onto ran T is a bounded Banach-space bijection. Its inverse is bounded, contradicting the sequence's graph norm tending to one while ||Th_j|| tends to zero.

## Application and limitations

For an exactly normalized background with ell=1/k>2 and c=3ell-1,

    p_2=(8ell-3)/(6ell-2), q_2=(4ell-1)/(6ell-2),

so (1) holds. More generally ell>1 and c>2ell-1 suffice for (1). This last criterion can apply to a held-scalar raw X3 operator after independently verifying its actual central strain.

The exact-join, exactly normalized modal density of proof 04 meets (2) analytically. Its finite degree-seven splines with simple knots are C^6. The endpoint corrections are defined by exact matching equations, so the same regularity holds across their joins. At the origin the nonconstant core terms have density degrees at least five; the inner logarithmic terms have degree bi+3>7. Finite smooth angular factors therefore give rho=x^2y+O(r^5), grad rho=O(r^2), Hess rho=O(r), and local C^(4,alpha) regularity for every alpha<1. The outer density is a finite sum of powers and logarithmic powers, with leading exponent k and every other exponent strictly smaller. Its first two differentiated bounds are O(r^(k-j)). These exponent inequalities are exact for the pinned data; proof 04 checks k and bi, and the leading/subleading forms directly give the comparisons. In particular bo>2 with k>0 suffices here for the correction degree 3-bo<k only when bo>3-k; the actual input bo>125 satisfies the stronger condition and must be checked as such.

The canonical velocity exists by the finite angular Green formulas. Local elliptic regularity, or termwise evaluation of those finite formulas, gives U in C^2 near zero. Parity gives U(0)=0 and DU(0)=diag(-c,c). Its strain is the scalar in proof 04, exactly 3/k-1 after the prescribed exact-real correction. Hence the Taylor remainder in (2) follows. The scalar repair changes coefficients, not any regularity exponent.

This application concerns that explicit modal object. It does not establish its stationarity or proximity in an inverse norm to X3. The theorem does not cover a different input/image norm, a high-derivative norm, a characteristic boundary realization excluding the constructed functions, or a restriction that excludes the required moment-corrected compact perturbations. A finite-dimensional section can be invertible while the full realization in (3) has this sequence.

Dependencies: elementary Fourier multipliers, finite-mode Poisson Green formulas, Taylor's theorem, Fourier Cauchy-Schwarz, finite-dimensional positivity, the Banach inverse theorem and standard local elliptic regularity. No prior numerical spectrum, compactness of the velocity operator, or unproved center-trace continuity is used.
