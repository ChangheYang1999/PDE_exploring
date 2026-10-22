# The canonical strain functional in logarithmic Sobolev spaces

This proof is written before new numerical computations. Its numerical application remains OPEN until both interval paths, complete actual Claude Opus5.5 review and later own adjudication. It concerns a linear functional, not the full IPM inverse.

## Statement, domain and normalization

For real densities h even in x and odd in y, initially smooth and compactly supported away from x=0, use the canonical full-plane Poisson inverse

 -Delta psi[h]=partial_x h, U[h]=(-psi_y,psi_x),
 Sigma(h)=psi[h]_xy(0).

There is no added harmonic xy term. For x>0 put z=log x,

 T_b h(z,y)=x^(1/2-b)h(x,y),
 ||h||Y_(b,s)=||T_b h||H^s(R^2_(z,y)).

Use the unitary Fourier transform in each coordinate; in y it is (2pi)^(-1/2) integral e^(-iy eta)f(y)dy. The squared H^s norm has weight(1+xi^2+eta^2)^s. The real odd-y subspace is understood throughout.

If s>=0, 0<=b<2 and s+b>2, then Sigma extends uniquely to a bounded real linear functional on Y_(b,s), with

 |Sigma(h)| <= C_(b,s) ||h||Y_(b,s),
 C_(b,s)^2 = Gamma(2b+1) B(2-b,s+b-2) / [pi 2^(2b+2)].  (1)

The constant is a proved upper bound for the full isotropic logarithmic H^s norm; sharpness in that norm is not claimed. For s=153/50 and nonnegative b, bounded extension exists exactly when b<2. For every fixed b>=2 there are smooth compact parity densities, supported away from both axes and vanishing near0, whose Y norm is bounded but whose |Sigma| tends to infinity. The counterexamples remain in the exactly center-normalization-preserving test class J(h)=0; they need not have Sigma(h)=0.

For b=3/2 and s=153/50,

 C^2 = [3/(16pi)] B(1/2,64/25).                         (2)

We will independently enclose this expression and C. The profile scaling functional is c[h]=Sigma(h)/3, so its operator bound is C/3. No full operator domain, inverse, nonlinear closure or decisive PDE endpoint follows.

## Derivation of the whole-plane strain kernel

Let F_l(r)=(1/pi)integral_0^(2pi) h(r,theta)sin(l theta)dtheta. For even stream frequency n, integration by parts in the canonical Green formula gives

 psi_n(r)=-r^(-n)/2 integral_0^r t^n F_(n-1)(t)dt
                    +r^n/2 integral_r^infinity t^(-n)F_(n+1)(t)dt.

The test density vanishes near0 and is compact, so all endpoint terms converge and no interface or boundary contribution remains. At n=2, the coefficient of r²sin2theta=2xy yields

 Sigma(h)=integral_0^infinity r^(-2)F_3(r)dr
          =(1/pi)integral_R² h(X)r^(-3)sin(3theta)dX.     (3)

This is the same normalization as psi=Sigma xy+... . Since sin3theta=y(3x²-y²)/r³ and h is even in x, (3) becomes

 Sigma(h)=integral_0^infinity integral_R K(x,y)h(x,y)dydx,
 K(x,y)=2y(3x²-y²)/[pi(x²+y²)^3].                       (4)

Every test integral is absolutely convergent. The factor2 is the full-plane even-x factor; it cannot be omitted.

For P_x(y)=x/[pi(x²+y²)], direct differentiation gives

 K=partial_x partial_y P_x.

For x>0 the Fourier transform of P_x is (2pi)^(-1/2)exp(-x|eta|). One elementary verification integrates exp(-iy eta)/(y²+x²) along the semicircle in the lower half-plane for eta>0 and in the upper half-plane for eta<0; the sole enclosed pole is respectively -ix or ix, giving pi exp(-x|eta|)/x. At eta=0 the same value follows by integrating1/(y²+x²). Multiplication by x/pi and the unitary convention gives the stated transform. Differentiation in x and y is valid for this smooth integrable kernel and its required derivatives, yielding

 K_hat(x,eta)=-(2pi)^(-1/2) i eta|eta| exp(-x|eta|).      (5)

The sign is irrelevant for the norm but is fixed here by the velocity convention and checked algebraically.

## A quantitative dual bound

With F=T_b h and x=e^z, equations(4),(5) represent Sigma as the distribution pairing of F with

 K_b(z,y)=x^(b+1/2)K(x,y).

The power includes dx=x dz as well as h=x^(b-1/2)F. Partial Fourier transformation in y and Cauchy-Schwarz give

 |Sigma(h)| <= ||(1-partial_y²)^(s/2)F||L2 * C,
 C²=integral_R integral_R (1+eta²)^(-s)|K_b_hat(z,eta)|² deta dz. (6)

The first factor is at most ||F||H^s, since s>=0 and1+eta²<=1+xi²+eta². This comparison uses the full two-dimensional Fourier transform only for this elementary monotone-weight inequality.

All integrands in C² are nonnegative. Substituting(5), dz=dx/x, and using the evenness in eta gives

 C²=(1/pi) integral_0^infinity eta^4(1+eta²)^(-s)
                         [integral_0^infinity x^(2b) exp(-2eta x)dx]deta
    = Gamma(2b+1)/[pi 2^(2b+1)]
                         integral_0^infinity eta^(3-2b)(1+eta²)^(-s)deta
    = Gamma(2b+1) B(2-b,s+b-2)/[pi 2^(2b+2)].            (7)

The inner gamma integral is legitimate because2b+1>0. The final substitution t=eta² and then u=t/(1+t) gives the beta integral. Its two arguments are positive precisely under b<2 and s+b>2. Tonelli justifies the interchange before finiteness is known, and the resulting finite beta integral proves finiteness. This establishes(1) on the initial tests.

Every smooth compact real odd-y F(z,y) is the transform of a smooth compact even-x, odd-y h supported away from x=0, by reflecting h from x>0. This test class is dense in the odd subspace of H^s. Consequently the bounded extension is unique. Requiring separation from the horizontal axis here would be inappropriate for this density argument at s>3/2; that extra condition is used only for the later counterexamples, not for density.

If a physical density h belongs toY and obeys |h(X)|<=Cr³ near0 and |h(X)|<=C(1+r)^gamma at infinity for some gamma<1, then (3) is absolutely convergent. The bounded extension agrees with the canonical strain given by (3). To see this, multiply F by smooth cutoffs in z and y tending to1, bounded between0and1. Such cutoffs converge in H^s, by the usual smooth compact density argument and their uniformly bounded multiplier norms. Their corresponding physical integrals converge by dominated convergence in(3). On each cutoff support the kernel is smooth and bounded, so further smooth approximation is valid in both the integral and Y norm. This identifies the extension with the canonical functional for the stated center/growth class. No strain is assigned from an arbitrary harmonic gauge.

## Large-radius obstruction for b>=2

Choose a nonnegative smooth radial eta supported in1<r<2, not identically zero. Choose a nonnegative smooth angular phi invariant under x and y reflection, supported away from both axes and nonzero where sin3theta!=0. Define

 h_*(r,theta)=r³ eta(r)phi(theta)sin3theta.

Then h_* is smooth compact, even in x and odd in y, with all center jets zero. Equation(3) gives

 Sigma(h_*)=(1/pi)[integral_1^2 r eta(r)dr]
                         [integral_0^(2pi)phi(theta)sin²3theta dtheta]>0. (8)

Let R>=1 and h_R(X)=R^(b-1)h_*(X/R). Homogeneity of the kernel in(3) gives Sigma(h_R)=R^(b-2)Sigma(h_*). If F_*=T_b h_*, then direct substitution gives

 T_b h_R(z,y)=R^(-1/2) F_*(z-log R,y/R).                 (9)

Fourier scaling, with eta rescaled to eta/R, yields for any finite s>=0

 ||h_R||Y_(b,s)^2
   =integral (1+xi²+eta²/R²)^s |F_*hat(xi,eta)|² dxi deta
   <=||F_*||H^s².                                     (10)

Thus for b>2 the strain tends to infinity with a uniformly bounded Y norm. Every h_R remains a smooth compact parity density with support away from both axes and all center jets zero. An individual large support is allowed; no common compact support is claimed.

At b=2, take R_j=q^j with q large enough that the positive-x projections of the scaled supports are disjoint. This is possible because h_* is supported where0<alpha<=x<=beta, so choose q>beta/alpha. The transformed supports are then disjoint in z. Choose an integer m>=s and

 h^(N)=N^(-1/2) sum_(j=1)^N h_(R_j).

Every mixed derivative through m of the transformed terms has disjoint z support. The integer H^m norm is a finite positive sum of their squared derivative norms, so the cross terms are zero. Equation(10) at m gives ||h^(N)||Y_(2,s)<=||F_*||H^m independently of N. Linearity and(8) give Sigma(h^(N))=sqrt(N)Sigma(h_*), which diverges. This proves unboundedness also at b=2 for every finite s. It is not inferred from divergence of the sufficient bound(7).

For s=153/50, every nonnegative b<2 satisfies s+b>2, so the bounded/unbounded alternatives cover all nonnegative weights and prove the stated exact threshold.

## Independent arithmetic plan for the useful weight b=3/2

At the fixed weight and order, Gamma(4)=6 reduces(7) to(2). The primary computation will use Arb gamma quotients and Arb pi, with exact rational inputs and a square root. The independent computation will avoid the gamma routine by reducing

 B(1/2,64/25)=(2184/5459) B(1/2,14/25),                 (11)

using twice B(u,v+1)=v B(u,v)/(u+v). For0<u,v<1, splitting the beta integral at1/2 and expanding the positive binomial series gives

 B(u,v)=2^(-u) sum_(n>=0) (1-v)_n/[n!(u+n)2^n]
       +2^(-v) sum_(n>=0) (1-u)_n/[n!(v+n)2^n].         (12)

In either positive sum, the ratio of successive complete terms is

 [(n+1-v)/(n+1)] [(u+n)/(u+n+1)] /2 <1/2

or the same formula with u,v exchanged. Therefore after terms0throughN-1 the positive remainder is at most twice the first omitted term. Exact rational partial sums and tail bounds, followed by mpmath.iv exponentials for2^(-u),2^(-v), give an enclosure with no unbounded truncation error.

The independent pi enclosure will use Machin's identity pi=16 arctan(1/5)-4 arctan(1/239). Its identity follows by the tangent double-angle formula twice: tan(4 arctan(1/5))=120/119, and subtraction of arctan(1/239) gives tangent1. The angle lies in(0,pi/2), so it is pi/4. Each arctangent is enclosed by its alternating series with error bounded by the first omitted term; exact rational endpoint subtraction is directed. mpmath.iv division and square root then enclose C²,C and C/3. Both complete interval outputs must lie inside the same stated strict rational windows. The beta tail and arctangent tail bounds are analytic premises, not empirical convergence tests.

This scalar application establishes a quantitative bound for the canonical scaling functional at one weight. It does not assert that the constant is optimal inY, nor that the full IPM linearization is defined or invertible on allY. The trial residual belongs toY at b=3/2 by canonical_residual_weak_axis_membership, but that result supplies no norm ceiling. The separate variable-transport graph-domain obstruction remains unchanged.
