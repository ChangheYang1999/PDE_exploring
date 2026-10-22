# Physical weighted norms controlling the center strain

Status: CONFIRMED, 2026-10-21. Complete informal proof preceded implementation and model review. Actual Opus353 and355 written reviews were checked against independent derivations and controls; see verification/review_adjudication.md. All conclusions concern the specified linear full-plane inverse, not solutions of B2.

## Statement and notation

Let X=(x,y), r=|X|, and write x=r cos(theta), y=r sin(theta). Let G be a smooth compactly supported function on R2, even under x reflection, and set Omega=xG. Let Psi be its ordinary logarithmic full-plane inverse with -Delta Psi=Omega and U=(-Psi_y,Psi_x), with no added harmonic term. Write c(G)=Psi_xy(0). Norms use physical area measure. Let B_R={r<R}.

For every R>0 and sigma>0,

    |c(G)| <= sqrt(5)/(12 sqrt(pi)) R ||grad G||_(L2(B_R))
                  +1/(4 sqrt(pi sigma))
                            ||(r/R)^sigma G||_(L2(R2 minus B_R)).   (1)

The numerical constants in this sufficient estimate are not claimed jointly optimal. The strict weight threshold is sharp within this family of power-weight and H^m estimates in this sense: for any prescribed c_*!=0 there is one sequence of compact smooth x-even G_n, supported outside expanding disks, such that c(G_n)=c_* while ||G_n||_(H^m) tends to0 for every fixed nonnegative integer m. For every fixed R and sigma<=0, both norms on the right of(1) also tend to0. Consequently no finite constants multiplying those two norms give a uniform strain bound at such sigma, even if one adds finitely many nonnegative H^m norms of G.

These sources may be chosen so that the ordinary center velocity U_n(0)=0, while on the expanding disk r<4n

    Psi_n=c_*xy,       U_n=(-c_*x,c_*y).                            (2)

Thus their nonzero inner strain comes from the ordinary full-plane source integral. It is not a freely appended affine field. They do not preserve a background's center-strain relation and do not solve the B2 equations with the required nonzero temperature jet. No smallness of their vorticity H^m norms is asserted.

Formula(1) also bounds the absolutely convergent center moment for smooth noncompact G whenever its two right-side norms are finite. A separately prescribed relative inverse must agree with that differentiated full-plane kernel for the moment to be identified as its center strain. The estimate itself supplies no complete inverse or a PDE solution for arbitrary tails.

## Full-plane moment and its sign

For a compact source, differentiating the logarithmic inverse gives

    c(G)=1/pi integral_R2 x y Omega(X)/r^4 dX
        =1/pi integral_0^infinity integral_0^(2pi)
                          cos(theta)^2 sin(theta) G(r,theta)
                                                   dtheta dr.      (3)

Indeed partial_xy log|X-Y| at X=0 is -2xy/r^4, and the fundamental solution has prefactor -1/(2pi). In the circular principal-value representation, the mixed distributional derivative has no delta term since x and y are different coordinates. Near zero Omega=O(r), so the integrand in the first integral is O(1/r), which is area-integrable. This also justifies the ordinary convergent mixed derivative expression using that distribution and a small-circle cutoff. Compact support removes any outer issue. This derivation fixes the sign independently of any stored inverse matrix.

## Local part of the estimate

Put k(theta)=cos(theta)^2 sin(theta). The periodic zero-mean primitive A(theta)=-cos(theta)^3/3 satisfies A'=k, so integration by parts on the full circle gives

    integral k G dtheta=-integral A G_theta dtheta.

This has no angular boundary term. Cauchy-Schwarz on (0,R) times the circle, with weights r and1/r, implies

    |integral_0^R integral kG dtheta dr|
        <= [integral_0^R r dr integral A^2 dtheta]^(1/2)
                            [integral_0^R integral G_theta^2/r
                                                     dtheta dr]^(1/2).

The second squared factor is exactly ||r^-1 partial_theta G||_(L2(B_R))^2 and is at most ||grad G||_(L2(B_R))^2. Thus the former, smaller norm can replace the local gradient norm in(1). Since integral_0^(2pi)cos(theta)^6 dtheta=5pi/8, the first squared factor is R^2(5pi/144). Dividing by pi proves the first term in(1). This argument uses cancellation of the angular kernel. A constant G on the disk contributes zero strain there, so no local ||G||2 term is needed. For smooth G the integrals at zero converge; one may first integrate over epsilon<r<R and then let epsilon decrease to zero.

## Exterior part

In area measure the kernel in(3) is k(theta)/r. Hence weighted Cauchy-Schwarz gives

    |c_exterior| <=1/pi ||(r/R)^sigma G||_2
       [integral_R^infinity (r/R)^(-2sigma) dr/r
                            integral_0^(2pi) k(theta)^2 dtheta]^(1/2).

The radial integral is1/(2sigma). The angular integral is pi/8, since cos^4 sin^2=cos^4-cos^6 and their full-circle integrals are3pi/4 and5pi/8. Their product, divided by pi^2 and square-rooted, is1/(4 sqrt(pi sigma)). This proves(1), including absolute convergence of the exterior integral under its stated hypothesis. The same two proofs apply to noncompact G when the right side is finite. No integration by parts at infinity is used.

## A source with fixed strain on a remote annulus

Choose a nonnegative nonzero phi in C_c^infinity((1,2)), put I=integral_1^2 phi(s)ds, and define

    g(r,theta)=4c_* phi(r) sin(theta)/I,
    G_R(X)=R^-1 g(X/R),              R>=1.                         (4)

Its angular dependence sin(theta) is smooth on its support away from0; extension by zero makes g and every G_R smooth on the whole plane. It is even in x, and odd in y only for this counterexample. That extra y parity is not a hypothesis on the B2 class or on estimate(1). The integral of cos^2 sin^2 is pi/4, so(3) gives c(G_R)=c_* exactly.

For completeness the ordinary inverse is identified directly. Write G_R=a_R(r)sin(theta). Then Omega=xG_R=q(r)sin(2theta), with q(r)=r a_R(r)/2. The second angular Green formula is

    Psi(r,theta)=1/4 [r^-2 integral_0^r s^3 q(s)ds
                     +r^2 integral_r^infinity s^-1 q(s)ds]
                                                        sin(2theta). (5)

For f=(r^-2 A+r^2 B)/4, A'=r^3q and B'=-r^-1q imply f''+f'/r-4f/r^2=-q. It is regular at0 and decays as r^-2 outside the compact source. The logarithmic kernel has the same second sine coefficient by expanding log|1-z| into its angular series and integrating; thus(5) is the ordinary full-plane inverse, with no homogeneous addition. Inside the source-free hole, (5) equals

    r^2 sin(2theta)/8 integral a_R(s)ds
          = xy/4 integral a_R(s)ds=c_*xy.

Its center velocity vanishes, proving(2) for one annulus. The exterior velocity is O(r^-3).

## Critical disjoint averaging

For every integer n>=1 set R_(n,j)=n4^j for1<=j<=n and

    G_n=(1/n) sum_(j=1)^n G_(R_(n,j)).                             (6)

The supports are disjoint annuli, outside r=4n. The source is smooth and compact for each n. Linearity gives c(G_n)=c_*, and the inner stream functions in(2) average to c_*xy. A change of variables gives, for every Cartesian multi-index alpha of order j,

    ||partial^alpha G_R||_2^2=R^(-2j)||partial^alpha g||_2^2,
    ||partial^alpha G_n||_2^2=n^-2 ||partial^alpha g||_2^2
                                     sum_(k=1)^n R_(n,k)^(-2j)
              <= (4n)^(-2j) ||partial^alpha g||_2^2/n.              (7)

Derivative supports remain disjoint, so the equality follows with no cross terms. Summing the finitely many derivatives proves H^m convergence for every fixed m. For any fixed disk B_R the functions and their local gradients vanish there eventually. For sigma<=0, (r/R)^sigma<=1 on the exterior, so the weighted exterior norm is bounded by ||G_n||2 and also tends to0. This proves the sharp strict threshold statement. It does not assert uniformity as m tends to infinity, or smallness of Omega_n=xG_n.

## Relevance and limits

For a native tail G=O(r^(-1-1/b)), a squared exterior weighted norm has radial bound r^(2sigma-1-2/b). It is finite for0<sigma<1/b when the angular coefficient is bounded and the remainder has the same bound. Thus unlike the sigma>1 sufficient drift weight in packet189, positive strain weights can be compatible with the native b>2 tails. This is a conditional integrability comparison, not a measured error bound on any saved family. Applying(1) to a difference would require actually estimating both of its norms, and a common canonical kernel convention.

For that native tail, the center moment already converges absolutely at infinity because integral_1^infinity r^(-1-1/b)dr is finite. The estimate supplies a possible quantitative error norm, not a necessary convergence test. The stated big-O bound is sufficient for the weighted integrability range; an if-and-only-if claim would require additional lower-tail information.

The construction explains how local source agreement and small unweighted global G norms can fail to control the center strain. The exact center certificates already used for the numerical states avoid making that inference. It does not refute a bound on solutions under additional coupled-equation hypotheses. The beta parameter is absent because the claims concern an inverse, not a stationary B2 solution.

Dependencies: ordinary full-plane logarithmic kernel, angular integration, Cauchy-Schwarz, smooth bumps and Cartesian dilation are derived or used explicitly above. Packet160 supplies context for the center certificates and packet189 for the distinct drift norm. Neither is a missing proof step. No formal Lean/Lake verification is claimed.
