# Physical norms and the constant term of the relative inverse

Status: CONFIRMED by the complete independent proof, finite exact and physical-kernel controls, and actual Opus5.5 review350 after the partial written review349. This is a theorem about the full-plane inverse. None of its constructed sources is asserted to solve B2.

## Statement, notation and scope

Write X=(x,y), r=|X| and x=r cos(theta). Let G be a smooth radial function of X with compact support, and put Omega(X)=x G(X). Fix the ordinary full-plane inverse

    Psi(X)=-(1/(2 pi)) integral log|X-Y| Omega(Y) dY,
    U=(-Psi_y,Psi_x),          V=U-U(0).

Thus -Delta Psi=Omega. There is no added harmonic velocity. The odd source has zero integral, so its ordinary velocity tends to zero at infinity. Define C2(G) as the vertical component of the constant limit of V at infinity. All norms below use Lebesgue measure on the physical plane. H^m means the sum in quadrature of the L2 norms of all Cartesian distributional derivatives of order at most the nonnegative integer m. The angular derivative is partial_theta=-y partial_x+x partial_y.

The following assertions hold.

1. The exact functional is

       C2(G)=-1/2 integral_0^infinity r G(r) dr
             =-1/(4 pi) integral_R2 G(X) dX.                       (1)

   If G is supported in R<r<2R, then V is identically zero on r<R. In particular every relative center jet is zero, although the ordinary center velocity is U(0)=(0,-C2(G)).

2. For every real c!=0 there is a sequence of smooth compact radial sources G_n, supported outside disks of radii tending to infinity, such that

       C2(G_n)=-c,
       ||G_n||_(H^m)+||x G_n||_(H^m) ->0                         (2)

   for every fixed m>=0. All angular derivatives of G_n of positive order vanish identically. Each corresponding V_n is zero on an expanding disk. Consequently neither the pair of norms ||G||_L2 and ||partial_theta G||_L2, nor their augmentation by any fixed finite collection of L2-based Cartesian H^m norms of G and Omega, bounds |C2(G)| uniformly even on these smooth radial compact sources.

3. For sigma>1 the functional extends to radial G for which the following weighted norm is finite, and

       |C2(G)| <= 1/[4 sqrt(pi(sigma-1))]
                         ||(1+r^2)^(sigma/2) G||_L2.               (3)

   In this statement C2 is defined by the absolutely convergent right side of (1); for compact sources it equals the inverse constant already defined. The constant in (3) is optimal on smooth compact radial sources. For every sigma<=1 no finite constant gives (3) with that weighted norm on all smooth compact radial sources. At sigma=1 the sequence in (2) can also have the weighted norm tending to zero.

4. If these compact sources are added to a background for which a linear relative inverse has been fixed and agrees, on these compact radial additions, with the ordinary logarithmic inverse minus its actual center velocity, then all its relative velocity center jets remain unchanged. Its temperature center coefficient a0 in Theta=a0 x^2+O(|X|^3) also stays unchanged when the temperature is held fixed. On each inner source-free disk the background B2 equations are unchanged. The ordinary center velocity changes by (0,c) whenever it is defined by the ordinary convergent integral. No equation outside that disk is preserved by this argument.

5. For a radial source supported in an annulus 0<a<r<b<infinity,

       |C2(G)| <= sqrt(log(b/a))/(2 sqrt(pi)) ||Omega||_L2.          (11)

   This constant is sharp on smooth radial sources supported in that open annulus. Consequently a source with C2=-c must satisfy log(b/a)>=4pi c^2/||Omega||_2^2. Fixed annular support therefore supplies control that assertion 2 deliberately does not assume.

All sharp constants in this statement are for radial G. The failure of uniform bounds on that subclass also disproves such bounds on any larger class containing it, but the functional formula and sharp sufficient constant are not asserted for a nonradial G. The finite collection in assertion 2 consists only of the stated nonnegative-order H^m norms; an L1 norm of G does control |C2| by (1).

These claims require no restriction on the B2 parameter beta because they concern an inverse on compact sources, not a solution of the coupled equations. They do not assert convergence of any saved numerical family or an error estimate on such a family. In particular they do not refute a bound under additional equation-dependent hypotheses.

## Direct inverse derivation

Let q(r)=rG(r). The first cosine Green formula is

    Psi(r,theta)=1/2 [r^(-1) integral_0^r s^2 q(s) ds
                         +r integral_r^infinity q(s) ds] cos(theta). (4)

To check it directly, put A(r)=integral_0^r s^2q(s)ds and B(r)=integral_r^infinity q(s)ds. For the radial coefficient f=(A/r+rB)/2 one has

    f'=(-A/r^2+B)/2,
    f''=A/r^3-q,
    f''+f'/r-f/r^2=-q.

This proves -Delta Psi=q cos(theta)=Omega away from r=0. Smooth radial G has q=O(r) at zero; expanding its smooth even radial Taylor terms in (4) gives a smooth odd-in-x stream function there. Alternatively the logarithmic convolution is smooth there and its first angular coefficient is (4). The logarithmic convolution has no other angular modes: after angular integration against cos(phi), the kernel contributes (r/(2s)) q(s)s ds for s>r and (s/(2r)) q(s)s ds for s<r, including the minus sign of the fundamental solution. These coefficients follow by expanding log|1-z|=-sum_(k>=1) Re(z^k)/k for |z|<1 and integrating the first cosine. The measure s ds then gives exactly (4). The equality at s=r follows by integrability of the logarithmic singularity, or by a limit from either side. This establishes the specified inverse, not merely an unspecified Poisson solution.

If q vanishes on [0,R], then A=0 and B is constant there, so

    Psi=X_1/2 integral_0^infinity q(s)ds,
    U=(0, 1/2 integral_0^infinity q(s)ds)

throughout the disk. Hence V=0 there. Outside the compact source, B=0 and A is constant. Equation (4) gives Psi=(A/2)x/r^2 and U=O(r^-2). Subtraction of the actual center value gives (1). Polar integration gives integral_R2 G=2pi integral rG dr. This proves assertion 1 and fixes both its sign and its factor.

## A single remote annulus

Choose phi>=0, nonzero, in C_c^infinity((1,2)), and set

    I=integral_1^2 s phi(s)ds>0,
    g(X)=2c phi(|X|)/I,
    G_R(X)=R^-2 g(X/R),          Omega_R(X)=x G_R(X),     R>=1.       (5)

These are smooth on the entire plane because the support stays away from the origin and phi is flat at its support boundaries. The integral of rG_R is 2c, so C2(G_R)=-c. The source and relative velocity vanish on r<R.

Put omega(X)=x g(X). A change of variables and the Cartesian chain rule give, for every multi-index alpha of order j and 1<=p<infinity,

    ||partial^alpha G_R||_Lp
        = R^(2/p-2-j) ||partial^alpha g||_Lp,
    ||partial^alpha Omega_R||_Lp
        = R^(2/p-1-j) ||partial^alpha omega||_Lp.                    (6)

The same formula with 2/p=0 holds for p=infinity. Thus G_R tends to zero in every fixed H^m; Omega_R does so in W^(m,p) for p>2, while its L2 norm is constant and its positive-order L2 derivatives tend to zero. Radiality makes every positive angular derivative of G_R zero. The p=2 vorticity norm requires the next construction.

## Disjoint averaging at the critical norm

For each integer n>=1 choose R_(n,j)=n 4^j for 1<=j<=n, and define

    G_n=(1/n) sum_(j=1)^n G_(R_(n,j)),       Omega_n=xG_n.           (7)

The supporting annuli are pairwise disjoint, and their inner radii are at least 4n. The construction is smooth, compact and radial for each n. Linearity of (1) gives C2(G_n)=-c exactly. Since every summand's relative inverse vanishes on r<4n, so does their sum.

The supports of Cartesian derivatives also lie in these disjoint closed annuli. Therefore their L2 squares add with no cross terms. For |alpha|=j, (6) yields

    ||partial^alpha G_n||_2^2
       = ||partial^alpha g||_2^2 n^-2
                         sum_(k=1)^n R_(n,k)^(-2-2j),
    ||partial^alpha Omega_n||_2^2
       = ||partial^alpha omega||_2^2 n^-2
                         sum_(k=1)^n R_(n,k)^(-2j).                 (8)

The first is at most ||partial^alpha g||_2^2 (4n)^(-2-2j)/n, and the second at most ||partial^alpha omega||_2^2 (4n)^(-2j)/n. Each tends to zero, including j=0 for Omega. Summing over the finitely many multi-indices proves (2) for every fixed m with one and the same sequence. It does not claim uniformity as m tends to infinity.

A fixed finite list of these norms consequently tends to zero while |C2| stays equal to |c|. This proves the asserted failure of uniform control. The argument concerns norms, not an abstract topology on arbitrary solutions of B2.

## The weighted threshold

For sigma>1, Cauchy-Schwarz and polar integration give

    integral_R2 (1+r^2)^(-sigma) dX = pi/(sigma-1),
    |integral G| <= sqrt(pi/(sigma-1))
                                 ||(1+r^2)^(sigma/2)G||_2.

This proves absolute convergence and (3). Equality in Cauchy-Schwarz is obtained by G=(1+r^2)^(-sigma). To establish sharpness within compact smooth radial sources, multiply this G by smooth radial cutoffs equal to one on expanding disks and between zero and one everywhere. Dominated convergence applies both to its integral and to its squared weighted norm, since both are controlled by (1+r^2)^(-sigma). The quotients approach the stated constant. Smooth cutoffs at the origin can be chosen constant near the origin, so no radial regularity issue arises.

For any fixed real sigma<1, changing variables in (5) gives

    ||(1+r^2)^(sigma/2)G_R||_2^2
       = R^-2 integral_(1<|Z|<2) (1+R^2|Z|^2)^sigma |g(Z)|^2 dZ
       = O(R^(2sigma-2)).                                          (9)

The two weights are uniformly comparable on this annulus for R>=1, also when sigma is negative. Hence this norm tends to zero at fixed nonzero C2.

At sigma=1, radiality gives the exact identity

    ||Omega||_2^2 = pi integral_0^infinity r^3 G(r)^2 dr
                 = (1/2)||rG||_2^2.                               (10)

For the disjoint averages (7),

    ||(1+r^2)^(1/2)G_n||_2^2 = ||G_n||_2^2+2||Omega_n||_2^2 ->0.

This proves failure at the critical threshold with the same smooth, locally invisible sequence. It also makes explicit why an unweighted L2 estimate for Omega does not remove this particular low-frequency obstruction.

## Fixed support and the cost of the countersequence

For 0<a<b and support in a<r<b, Cauchy-Schwarz in the radial measure gives

    |integral_a^b rG dr|^2
       <= integral_a^b r^3 G^2 dr integral_a^b dr/r
        = ||Omega||_2^2 log(b/a)/pi.

Since |C2|^2=(1/4)|integral rG dr|^2, taking square roots proves (11). The equality function on this interval is G=r^-2, extended by zero. To prove sharpness within the smooth open-annulus class, multiply r^-2 by smooth cutoffs supported in(a,b), between zero and one, and tending pointwise to one throughout(a,b). Dominated convergence on a fixed finite annulus makes both the mass and the squared vorticity norm converge to their equality values. This proves sharpness without calling the discontinuous cutoff function a smooth source.

For (7) one may take a=4n and b=2n4^n. Their ratio is 2*4^(n-1); its logarithm grows linearly in n, while ||Omega_n||_2 is a constant times n^-1/2. Thus the outer-to-inner radius ratio grows exponentially in n, equivalently exponentially in the inverse squared vorticity norm. It is not super-exponential in n. This quantifies the large radial range needed by this particular critical construction and prevents treating it as a fixed-domain numerical error example. A noncompact family would instead need a separately proved tail control; none is supplied merely by agreement at finite radii.

## Consequences and limitations for the candidate audits

The inverse is linear and its agreement on compact additions is part of assertion 4. Adding Omega_n changes neither Omega nor the relative velocity on r<4n, so holding Theta fixed leaves both stationary B2 residuals and every relative velocity center relation exactly unchanged there. It also leaves a chosen background's asymptotic vorticity coefficients unchanged, since each added source is compact. If the background absolute center integral is defined, it gains (0,c). This is consistent with a moving material center; that drift is not held fixed. For a background with only a specified relative inverse, only the relative conclusion is used.

The stationary residuals meant here are exactly R_Omega=(beta X+V) dot grad Omega+Omega-Theta_x and R_Theta=(beta X+V) dot grad Theta-(beta-2)Theta. They depend only on these fields on the disk. Absolute center drift and physical reconstruction are not being held fixed.

Beyond the expanding disk the residuals may change. This construction supplies no B2 solution, no approximate global solution with controlled residual, and no obstruction to a sequence satisfying additional global equations. Its point is a precise limitation of convergence tests using the particular norms in assertion 2. Packet187 certifies full-plane L2 distances of G=Omega/x and of its angular derivative for explicitly interpreted stored functions. Those are useful field comparisons, but they alone do not bound the inverse constant C2. Even small additional unweighted H^m vorticity distances would not yield such a general bound.

The sufficient weighted norm in (3) concerns integrable differences for which (1) applies. A native tail G~r^(-1-1/b), b>2, need not have that norm finite: the radial norm integral has large-r power 2sigma-1-2/b and converges only if sigma<1/b when the leading coefficient is nonzero. Thus (3) is not an unproved estimate on the nonintegrable background's finite-part constant. Compact perturbations with the same tail do satisfy (1), and are enough to disprove the proposed weak controls. Packet181 separately proves the compactified Hölder threshold for finite-part constants of broader noncompact sources.

Dependencies: the proof above rederives the full-plane first cosine inverse, dilation, disjoint-support orthogonality and the weighted integral. It requires only ordinary smooth bump functions and Cauchy-Schwarz. Packet181 and packet187 explain its context, not a missing step in its proof. No formal proof-assistant verification is claimed. Finite polynomial and physical-kernel controls are recorded alongside this file. The polynomial controls have C5 regularity, distinct from the theorem's smooth bumps.
