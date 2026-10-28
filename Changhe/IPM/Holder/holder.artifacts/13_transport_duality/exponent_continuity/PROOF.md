# Continuity of the sharp norms in the Holder exponent

## Statement, notation and scope

On R^2 let [f]_alpha=sup_(z!=w)|f(z)-f(w)|/|z-w|^alpha for 0<alpha<1. Let C_alpha and D_alpha denote the real scalar operator seminorms of T_xx and R_1^2=T_xx-I/2, respectively, on the homogeneous Holder space modulo constants. The circular principal-value kernel is K_xx(z)=(z_1^2-z_2^2)/(2pi|z|^4). The quotient extension and equality with the supremum over smooth compactly supported tests are those of ../../01_setup/PROOF.md. The same norms apply to complex scalar inputs by the real-kernel argument in that proof.

Both functions alpha -> C_alpha and alpha -> D_alpha are continuous on (0,1). More precisely, fix 0<a<=b<1, 0<epsilon<1/2 and R>1. Set

    Ebar = 2 epsilon^a/(pi a)
           +(1+2epsilon)^b epsilon^2/[2(1-epsilon)^2]
           +2^b R^(b-1)/[(1-b)(1-1/(4R^2))^2],
    m = (2/pi) log((R+1/2)/epsilon),
    L = max{1/(e a), (2R)^b log(2R)}.

For alpha,beta in [a,b],

    |C_alpha-C_beta| <= 2Ebar + m L |alpha-beta|,             (1)
    |D_alpha-D_beta| <= 2Ebar + (m+1/2)L |alpha-beta|.         (2)

Here e is the base of the natural logarithm. These estimates concern seminorms, not full inhomogeneous norms.

A consequence is that each rigorously certified strict inequality C_alpha0 < D_alpha0 extends to an open neighborhood of alpha0 in (0,1). More explicitly, suppose a<alpha0<b, U>=C_alpha0, V<=D_alpha0 and g=V-U>0. For any epsilon,R with 4Ebar<g, every alpha in [a,b] satisfying

    |alpha-alpha0| < (g-4Ebar)/[(2m+1/2)L]                  (3)

obeys C_alpha<D_alpha. This is a proved neighborhood criterion; it does not assert separation for every exponent.

## Fixed signed measures and uniform truncation

Use x=(1/2,0), y=-x and K_phi(z)=Re(e^(i phi)/(2pi z^2)). The measures in ../PROOF.md are

    Omega = B(0,R) \ (B(x,epsilon) union B(y,epsilon)),
    mu_phi = 1_Omega [K_phi(z-x)-K_phi(z-y)] dA(z),
    mu_phi^D = mu_phi - delta_x/2 + delta_y/2.

They have total mass zero, support in the closed disk of radius R, and no dependence on alpha. Central oddness gives the first zero-mass claim; the two atoms give the second. The positive and negative Jordan masses of mu_phi are at most m, and those of mu_phi^D are at most m+1/2. Indeed, for each pole the integral of the absolute kernel over the annulus epsilon<=|z-pole|<=R+1/2 is

    (2/pi) log((R+1/2)/epsilon),

because the angular integral of |cos(2theta-phi)| equals 4. The total variation of the difference of the two kernels is at most twice that quantity. For a zero-mass signed measure each Jordan mass is half its total variation. The atoms add total variation at most 1. These bounds hold uniformly in phi.

The finite transport norm W_alpha(mu) and its exact duality with the Holder functional are proved in ../PROOF.md. Its truncation estimate is uniform in phi and gives

    |C_alpha-sup_phi W_alpha(mu_phi)| <= E(alpha;epsilon,R),
    |D_alpha-sup_phi W_alpha(mu_phi^D)| <= E(alpha;epsilon,R).

We check E<=Ebar on [a,b]. The local angular constant there is

    a2(t)=2^(1+t/2)/(pi(2+t)) <= 1/pi.

For completeness, the function 2+t-2^(1+t/2) is concave on [0,1], is zero at 0 and equals 3-2sqrt(2)>0 at 1. It is therefore nonnegative throughout. Since epsilon<1, epsilon^alpha<=epsilon^a and 1/alpha<=1/a. The smooth local term is bounded by replacing its exponent with b because 1+2epsilon>1. Since R>1, R^(alpha-1)<=R^(b-1), 2^alpha<=2^b and 1/(1-alpha)<=1/(1-b). This gives exactly Ebar.

## Dependence of finite transport on the exponent

Every distance between two support points lies in [0,2R]. For 0<r<=1 and t in [a,b],

    |d(r^t)/dt| = r^t log(1/r) <= r^a log(1/r) <= 1/(e a).

The last maximum follows by writing r=exp(-u) and maximizing u exp(-a u) for u>=0. For 1<=r<=2R,

    |d(r^t)/dt| = r^t log r <= (2R)^b log(2R).

At r=0 the costs r^alpha and r^beta are both zero. The mean value theorem thus gives

    |r^alpha-r^beta| <= L |alpha-beta|

uniformly on the entire support-distance interval. A coupling of the Jordan parts has total mass M, independent of its choice and of the exponent. Its two costs differ by at most ML|alpha-beta|. Taking an arbitrarily close minimizing coupling in each direction gives

    |W_alpha(mu)-W_beta(mu)| <= ML|alpha-beta|.

This does not require existence of an optimal coupling. It applies to both finite signed measures above. The elementary inequality |sup_phi A_phi-sup_phi B_phi|<=sup_phi|A_phi-B_phi| and their uniform mass bounds give Lipschitz bounds for the two phase suprema. Adding the two truncation errors proves (1) and (2).

## Continuity and strict-separation neighborhoods

Fix alpha0 in (0,1) and choose a<alpha0<b. For any tolerance t>0, first take epsilon small and R large so that 2Ebar<t/2. This is possible because a>0 and b<1. With those parameters fixed, m and L are finite, so (1) and (2) give norm changes less than t whenever |alpha-alpha0| is sufficiently small. This proves continuity without a density claim between distinct Holder spaces.

For the quantitative strict-separation statement, apply (1) and (2) with beta=alpha0. Subtract their adverse bounds to obtain

    D_alpha-C_alpha >= g-4Ebar-(2m+1/2)L|alpha-alpha0|.

Condition (3) makes the right side positive. Appropriate parameters always exist. Thus every accepted positive table gap gives an open interval of strict separation, whether or not those parameters are numerically optimized.

## Dependencies and verification

The only operator input is the accepted finite-transport theorem in ../PROOF.md, previously audited as V077 and re-audited as V156, with the setup and angular-constant proofs referenced there. The argument is otherwise elementary real calculus and finite-mass transport comparison. There is no numerical integral, unseen literature statement, assumption about optimal phase or assumption that an extremizer exists.

Status at creation: OPEN pending independent cross-read. Numerical applications require accepted endpoint bounds and exact checking of the displayed conditions.
