# Finite stationary recursion and its near-resonant angular inverse

## Exact finite statement

Set c=p/q=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma, alpha_j=gamma-j delta and s_j=alpha_j+3. On r>0 let

    V_j=span{cos(2m theta):0<=m<=10(j+1)-1},
    W_j=span{sin((2m+1)theta):0<=m<=10(j+1)-1}.

A potential C_j in V_j denotes chi_j=r^s_j C_j(theta). Define rho_j=-partial_y Delta chi_j and u_j=(-partial_y partial_x partial_y chi_j,partial_x partial_x partial_y chi_j). Thus rho_j=r^alpha_j G_j(theta). Fix the leading C_0 from state131. For each1<=j<=16 there is exactly one C_j in V_j solving the jth stationary homogeneous equation

    -j(c-1)G_j + E_j=0,
    r^alpha_j E_j=sum_(i+k=j-1) u_i.D rho_k.            (1)

N4 independently computed these coefficients and compared them exactly with N1. This audit supplies the exact spaces, checks their closure and nonresonance, and reviews the scope of that finite computation. It does not independently rerun all3060 coefficient comparisons.

## Homogeneity and angular closure

The density and velocity from chi_j both have radial degree alpha_j. Hence u_i.D rho_k has degree alpha_i+alpha_k-1=alpha_j when i+k=j-1. Also c alpha_j-1=-j(c-1). This proves the coefficient equation(1).

Write psi_i=partial_x partial_y chi_i. It is a sine polynomial of even frequencies at most20(i+1), times r^(alpha_i+1). The density uses odd sine frequencies at most20(k+1)-1. The polar Poisson bracket is

    u_i.D rho_k = (partial_r psi_i partial_theta rho_k
                         -partial_theta psi_i partial_r rho_k)/r.

Its largest possible angular frequency is at most20(i+1)+20(k+1)-1=20(j+1)-1. All frequencies are odd and the result is a sine polynomial. Thus E_j belongs to W_j. This uses the bracket cancellation before estimating frequency; separately bounding Cartesian factors would overcount two frequencies.

## Exact triangular inverse

For n>0 even,

    -partial_y Delta(r^s cos(n theta)) = r^(s-3)
       [-(s²-n²)(s-2-n)sin((n+1)theta)/2
         +(s²-n²)(s-2+n)sin((n-1)theta)/2].           (2)

For n=0 the single coefficient at sin(theta) is -s²(s-2). Formula(2) follows by differentiating the polar Laplacian and using angle addition. In descending frequency order, this is a square triangular map from V_j to W_j with diagonal entries

    d_n(s)=-(s²-n²)(s-2-n)/2, n>0;
    d_0(s)=-s²(s-2).

Every root is an even integer. Since delta=d/p with d=p-q odd and gcd(d,p)=1,

    s_j=4-(j+1)d/p

is nonintegral for0<=j<=16. In particular all diagonal entries are nonzero. The angular map is therefore an isomorphism. Knowing the previous coefficients determines E_j, then G_j=E_j/[j(c-1)], then a unique C_j. Induction proves the finite statement. Checking the reconstructed low-frequency coefficient is a useful arithmetic guard, but no additional compatibility condition remains after invertibility is proved.

The original peer phrase “the finite descending angular space” must mean V_j as specified here, or the corresponding finite space determined by the exact forcing support. Uniqueness is not asserted among arbitrary whole-plane potentials or without fixing the leading chart.

## A small divisor at order eight

For a pure first sine density G sin(theta) at radial degree alpha=s-3, its unique homogeneous potential in V=span{1} is

    chi= -G r^s/[s²(s-2)],  s notin{0,2}.

Its stream function is

    psi=-G r^(s-2)sin(2theta)/(2s).

Thus at r=1,

    u_r=(G/s)cos(2theta),
    u_theta=-(s-2)G sin(2theta)/(2s),
    ||u||_L2(circle)/||rho||_L2(circle)
       =sqrt(1+(s-2)²/4)/|s|.                        (3)

At order8, s_8=4-9delta is close to0. Formula(3) quantifies a real small divisor in the homogeneous density-to-velocity algebra. These fields are defined on r>0. No claim is made that the singular homogeneous density by itself belongs to a whole-plane Riesz-transform domain. A regular interior completion can add harmonic exterior fields; this local algebra does not determine that completion.

For the actual order-eight potential, the first density coefficient and second stream coefficient are

    G_1=-s²(s-2)C_0 + s(s²-4)C_2/2,
    Psi_2=s(s-2)C_0/2 -(s+4)(s+2)C_4/4.             (4)

The checker compares the first identity with the stored exact density and records both summands in the second. These are diagnostics of the finite expansion. The small divisor alone does not prove a convergence radius, divergence, or a quantitative full-plane error bound.

## Numerical scope

The N4 record has17 exponent checks,3060 exact potential/density coefficient equalities, and13 exact forcing-energy comparisons through order16. The forcing norms in that record are finite-order values. Norm growth over those orders is insufficient to prove convergence or divergence of an infinite series. Any claimed infinite majorant needs all-order estimates, and a finite-radius residual estimate must include the omitted sectors and a remainder bound.

The verification below checks all1530 diagonal pivots from j=0 through16, the exact arithmetic identities in(4), and the amplification in(3). N4's existing independent computation remains the numerical provenance for the full finite coefficient table.
