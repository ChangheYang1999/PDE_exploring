# An exact asymptotic for the highest Fourier coefficient

Status: PROVED. Independently reviewed and confirmed by the theory part at 2026-10-31T09:36Z; see sources/lead_review_0936Z.md. The repaired factor 1/2 is retained in topic117. Where topic115 was an assumption, it is now independently confirmed.

## Statement and notation

Fix delta in (0,1), put d=delta/(1-delta), and let the nonzero leading density be a finite real sine polynomial supported at positive odd frequencies. Let L be its largest frequency and alpha its nonzero coefficient there. Put

    B=L+1, eta=B-delta, a=2/eta, b=2(B-1)/eta,
    nu=1/b, Beta=integral_0^1 t^(a-1)(1-t)^(b-1) dt,
    R=4d(a Beta)^(1/a), C=(ab Beta)^nu,
    Kappa=4d C nu/Gamma(1-nu).

Here B>=2 is even, 1<b<2, 1/2<nu<1, and Kappa>0. Gamma denotes the usual positive gamma integral on positive real arguments. Normalize the highest density coefficient at order n as

    A_n=(-1)^(n-1) alpha^n h_n, h_1=1.

For the pure recurrence wherever it exists, and for the entire canonical polynomial-log recurrence, topic38 establishes the same positive sequence h_n. It satisfies

    h_n=Kappa R^(-n) n^(-1-nu) [1+O(n^(-nu))].          (1)

All constants implicit in the error may depend on delta and B. They do not depend on lower leading harmonics. In particular,

    h_(n+1)/h_n -> 1/R,
    h_n^(1/n) -> 1/R,
    log(h_n R^n)/log n -> -1-nu.

This gives a constant-factor asymptotic for a single Fourier sector, including when the complete recurrence has logarithmic terms. It is not a convergence theorem for the complete recurrence.

## The generating function and its boundary values

Topic38 proves that H(z)=sum_(n>=1)h_n z^n has radius R, positive coefficients, and H(R)=4d. Define

    J(z)=sum_(n>=1) h_n z^n/(eta n+2),
    x=H/(4d), v=BJ/(2d), E=z d/dz.

The equations and the real beta parametrization are

    E x=x(1-x)/(1-v), E v=a(Bx-v),                     (2)
    z=4d[a Beta_x(a,b)]^(1/a), H(z)=4dx.               (3)

The branch in (3) is fixed by x=z/(4d)+O(z^2) at zero. Also J(R)=2d/B. Thus H and J converge absolutely and uniformly on the closed disk |z|<=R, by comparison with their finite positive sums at R. In particular x and v are continuous on that closed disk.

The real behavior in (3) by itself does not imply (1). We first exclude competing singularities on the circle and then obtain a complex local expansion.

## Continuation across the rest of the circle

Take z_0=R exp(i theta) with theta not zero modulo 2pi. Positivity of every coefficient of J gives

    |J(z_0)|<J(R)=2d/B.                                (4)

Indeed equality in the triangle inequality for this absolutely convergent sum would require all nonzero terms to have the same argument. The terms with indices one and two are strictly positive at R, so this would require exp(i theta)=exp(2i theta), which is impossible for this theta. Consequently |v(z_0)|<1.

The right side of the ordinary differential system (2), after dividing by z, is holomorphic near (z_0,x(z_0),v(z_0)). Its denominators z and 1-v are nonzero there. The local analytic initial-value theorem therefore produces a holomorphic solution through these boundary values.

This solution agrees with the original one inside the disk. To see the matching at the boundary, approach z_0 on a short radial segment. The original continuous x,v stay in a neighborhood where the vector field and its first derivatives are bounded. Integrating their differential equations up to the boundary gives the integral equation with terminal value (x(z_0),v(z_0)). Local uniqueness for that integral equation identifies the two solutions on the segment; the identity theorem identifies their germs. This also shows that the continuations agree on overlaps.

It follows that H continues holomorphically across every point of |z|=R except possibly R itself. Compact subsets of that punctured circle admit a uniform exterior collar of continuation.

## A complex expansion at the positive singularity

Put u=1-x. Near u=0, integrate the convergent Taylor series of (1-s)^(a-1) to write

    Beta-Beta_(1-u)(a,b)=u^b Phi(u)/b,
    Phi(0)=1,                                         (5)

where Phi is holomorphic near zero. The power u^b is taken on the branch positive for u>0. Equation (3) is equivalent to

    1-(z/R)^a=u^b Phi(u)/(b Beta).                     (6)

The function u Phi(u)^(1/b) is holomorphic near zero and has derivative one there. Its analytic inverse W satisfies W(w)=w+O(w^2). Thus the branch of H coming from the real interval below R is

    u=W([b Beta(1-(z/R)^a)]^nu).                       (7)

For t=1-z/R, the inner analytic factor satisfies 1-(z/R)^a=a t(1+O(t)). On any sufficiently small disk about R with a sector about the ray z>R removed, (7) is holomorphic on the branch t^nu positive for real t>0. It gives

    H(z)=4d-4d C(1-z/R)^nu+O(|1-z/R|^(2nu)).          (8)

The estimate is uniform in every closed sector |arg(1-z/R)|<=pi-epsilon. It uses nu<1: the correction of order t^(nu+1) is smaller than t^(2nu). The branch in (7) matches H along the real interval and hence on their connected overlap.

Combining this local continuation with the compact collars from the preceding section gives numbers epsilon>0 and theta in (0,pi/2) for which H is holomorphic in

    |z|<R+epsilon, z != R, |arg(z-R)|>theta.           (9)

We can shrink epsilon and enlarge theta if necessary. The original disk |z|<R is contained in this domain. Thus both the location and the angular shape needed for coefficient extraction have been established.

## A coefficient estimate with its contour proof

We use the following elementary estimate. Suppose F is holomorphic in a domain of the form (9) with R=1 and is holomorphic at zero. Suppose, for a real beta>-1,

    F(z)=O(|1-z|^beta) as z->1 within that domain.

Then its Taylor coefficients obey

    [z^n]F(z)=O(n^(-beta-1)).                          (10)

Here is the contour argument, to make the analytic hypothesis explicit. Choose phi strictly between theta and pi/2. Deform a small circle about zero into a contour consisting of a circle of radius 1/n about 1, traversed on the side away from the excluded ray; two segments z=1+r exp(plus or minus i phi), with 1/n<=r<=r_0; and a fixed outer connecting arc. Choose the outer arc in the continuation collar so that its modulus is bounded below by 1+kappa for some kappa>0. The two segments and their endpoints can be joined to such an arc within the domain. All portions remain in the analytic region and enclose zero.

On the small circle the integrand F(z)/z^(n+1) has magnitude O(n^(-beta)), since |z|^(-n-1) stays bounded there. The arc length is O(1/n), giving O(n^(-beta-1)). Along either segment, cos(phi)>0 gives |z|>=1+c r and hence |z|^(-n-1)<=exp(-c' n r), after fixing r_0 small enough. Its contribution is bounded by a constant times

    integral_(1/n)^(r_0) r^beta exp(-c' n r) dr
       <= n^(-beta-1) integral_1^infinity s^beta exp(-c' s) ds.

The last integral is finite. The fixed outer arc contributes exponentially little because F is bounded on that compact arc and |z|>=1+kappa. Cauchy's coefficient formula proves (10). Rescaling z by R adds the factor R^(-n).

Apply this estimate to

    F(z)=H(z)-4d+4d C(1-z/R)^nu,

using beta=2nu. It is holomorphic in (9) on the same branch, and (8) gives its required local bound. Therefore

    [z^n]F(z)=O(R^(-n)n^(-1-2nu)).                    (11)

No real-axis transfer principle is being assumed here; the required complex continuation and contour estimate were proved above.

## The leading coefficient and its sign

The generalized binomial identity gives, for n>=1,

    [z^n](1-z/R)^nu
       =R^(-n) Gamma(n-nu)/[Gamma(-nu)Gamma(n+1)].     (12)

The negative gamma value is defined by Gamma(-nu)=Gamma(1-nu)/(-nu)<0. Formula (12) can also be checked without analytic continuation of Gamma: both sides have the same first coefficient -nu and the same recurrence ratio (n-nu)/(n+1).

The gamma-ratio estimate, obtained by applying Stirling's formula to the positive arguments n-nu and n+1, is

    Gamma(n-nu)/Gamma(n+1)=n^(-1-nu)[1+O(1/n)].        (13)

Equations (8), (11), (12) and (13) yield

    h_n=(-4d C/Gamma(-nu)) R^(-n)n^(-1-nu)
         [1+O(n^(-nu))].

The prefactor equals Kappa by the gamma recurrence. This proves (1). Since the relative error tends to zero and Kappa is strictly positive, division of consecutive terms, taking nth roots, and taking logarithms prove the three stated limits.

## Dependencies and verification scope

The only model-specific input is topic38: the exact top-frequency recurrence, positive coefficients, beta parametrization, exact radius, and boundary sums. The additional arguments use a holomorphic ordinary differential equation, the local analytic inverse theorem, Cauchy's coefficient formula, the binomial identity, and the gamma-ratio estimate. The coefficient-transfer estimate is proved here rather than imported from an unchecked reference.

Finite verification compares the normalized coefficient h_n R^n n^(1+nu) with Kappa for several exact delta and B values and checks the first local expansion coefficients, with interval enclosures retained in verification/20261031T094100Z. Such comparisons diagnose constants or signs; the independent argument review recorded in V238 establishes the limiting formula. The later finite checks are recorded separately in V250.
