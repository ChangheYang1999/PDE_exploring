# Pressure multipoles restrict the escaping-sheet rate

Status: CONFIRMED at the explicit scopes below, A550-A552. Independent reconstruction of C38 and an additional rotational-rigidity consequence. Complete postread; no computation.

## 1. Hypotheses, notation and precise conclusions

Fix 2/5<c<1/2 and any finite real omega. Put p=(1-c)/c in(1,3/2), a=1-2c, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, Q_t=exp(omega tJ), L=(1-c)I+omega J. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, LU+DU(Ax+U)+grad P=0,
    |U(y)|<=C(1+|y|)^-p,
    |DU(y)|<=C(1+|y|)^(-p-1).                        (1)

These natural bounds follow from the confirmed target-range square-root screen when U tends uniformly to0 and DU=O(sqrt r). They are stated explicitly here. Helicity is not needed until the sheet application.

Let Pinf be the canonical pressure constant, V the actual leading velocity, P2 its canonical quadratic pressure, Wstar=curl V, and D=R3 minus{0}. Define

    u_t(x)=exp((1-c)t)Q_t U(exp(tA)x),
    p_t(x)=exp(2(1-c)t)[P(exp(tA)x)-Pinf],
    S_t=p_t-|u_t|²/2, S=P2-|V|²/2,
    n_t=Du_t u_t+grad p_t.

The confirmed A530,A533,A538 give C1 canonical pressure convergence, uniform local C^(1,alpha) velocity bounds for every alpha<1, and the relevant limits. The exact equation is

    partial_t u_t=-exp(-t)n_t.                       (2)

For integers k>=0 put

    r_k=(k+5)c-2,
    K={k>=0:r_k<1}={k>=0:k<3p-2}.

Then K={0,1} when c>=3/7 and K={0,1,2} when c<3/7. Write the tensor difference, as one integrand,

    m(y)=U(y) tensor U(y)-V(y) tensor V(y),
    Mom_k=integral_R3 y^(tensor k) tensor m(y)dy,
    Theta_k(x)=-((-1)^k/k!) D^(k+2)N(x):Mom_k,
    N(x)=-1/(4pi|x|).                                (3)

All moments in (3) for k in K converge absolutely. This does not assign values to two separately divergent moments of U tensor U and V tensor V.

For every real gamma<1 and every compact subset of D,

    S_t-S=sum_(k in K) exp(-r_k t)Theta_k(Q_t^T x)
                       +O_(C1)(exp(-gamma t)).       (4)

The notation means that the scalar remainder and its spatial first derivatives have that bound; its constant may depend on gamma and the compact set. Each Theta_k is harmonic and homogeneous of degree-(k+3). It vanishes identically exactly when the fully symmetrized trace-free part of Mom_k vanishes. In original variables,

    P(y)-Pinf=P2(y)+sum_(k in K)Theta_k(y)
                       +O(|y|^(-2p-gamma/c)).        (5)

Now assume an escaping level patch as specified in Section6, with positive rate mu and the already confirmed identities giving mu>=1. Then

    mu in {1} union {1+r_k:k in K} union [2,infinity). (6)

If mu=1 or mu>=2, every Theta_k vanishes identically. If 1<mu<2, exactly one k obeys mu=1+r_k; all other Theta_j vanish, while the nonzero Theta_k vanishes on the limiting sheet and has the prescribed nonzero normal gradient in (24) below.

For omega!=0 in that resonant case, Theta_k is globally axisymmetric. The sheet avoids the rotation axis and lies locally on a cone where P_(k+2)(x3/|x|)=0. The polynomials and their roots are listed in Section8. This last conclusion strengthens the source's circular-cone statement and is proved independently below.

For a global zero-helicity profile satisfying (1), every vortical carrier equilibrium has

    rho in {-a,-(2-2c)} union {-(k+3)c:k in K}
                              union (-infinity,-(3-2c)].  (7)

The same necessary condition holds for the effective rho=-a lambda on any A536 zero-g component with lambda>1, and for the irrotational-equilibrium cases to which that component result applies. It does not constrain separating levels or flat witnesses beyond those explicit premises. At rho=-a this proof gives no moment-vanishing conclusion.

## 2. Uniform rates for the velocity and its first derivatives

A516 and canonical normalization give |grad P(y)|<=C|y|^(-2p-1) at large radius. Increasing C extends this and the bounds (1) to all y!=0. Rescaling yields

    |u_t(x)|<=C|x|^-p, |Du_t(x)|<=C|x|^(-p-1),
    |grad p_t(x)|<=C|x|^(-2p-1),
    |n_t(x)|<=C|x|^(-2p-1), t>=0.                    (8)

Integrate (2) at fixed x to its terminal limit V:

    u_t-V=integral_t^infinity exp(-s)n_s ds,
    |u_t-V|<=C exp(-t)|x|^(-2p-1).                   (9)

At t=0 this proves m(y)=O(|y|^(-3p-1)) at infinity. At the origin, boundedness of U and the homogeneous bound for V give |m(y)|<=C(1+|y|^-2p). Thus the moments in (3) converge: near zero 2p<3, and at infinity their radial exponent is k+1-3p<-1 precisely when k<3p-2.

We also need a rate for Du_t-DV, but not convergence of D[exp(t)(u_t-V)]. Fix nested balls compactly contained in D and 0<alpha<1. The confirmed tail regularity bounds Du_t in C^alpha on the larger ball, uniformly in t. The same holds for DV. The local pressure split of Section3, differentiated once, applies a truncated Calderon-Zygmund operator to D(u_t tensor u_t), which is uniformly C^alpha there; its remaining kernel is smooth and has a uniform integrable tensor majorant. Hence grad p_t and n_t are uniformly C^alpha on a smaller ball. Alternatively A539 supplies the uniform local pressure regularity directly.

Let phi_epsilon be a smooth mollifier supported in a radius-epsilon ball. On a still smaller ball,

    |(Du_t-DV)-(Du_t-DV)*phi_epsilon|<=C epsilon^alpha.

Differentiate the convolution of (9). Since D phi_epsilon has integral zero,

    |(Du_t-DV)*phi_epsilon|
       <=integral_t^infinity exp(-s)
                 [n_s]_alpha epsilon^alpha ||D phi_epsilon||_1 ds
       <=C exp(-t)epsilon^(alpha-1).

Take epsilon=exp(-t) for large t. Therefore

    |Du_t-DV|<=C_alpha exp(-alpha t)                 (10)

on compact subsets of D, for every alpha<1. The radii of all balls can be fixed before t tends to infinity. No rate for a second velocity derivative is used.

## 3. Canonical pressure split and the low moments

Let m_t=u_t tensor u_t-V tensor V. From (9),

    |m_t(y)|<=C exp(-t)|y|^(-3p-1),                  (11)

and in the small core |y|<=exp(-ct),

    |m_t(y)|<=C[exp(2(1-c)t)+|y|^-2p].              (12)

Fix an annulus r1<=|x|<=r2 and a small d<=r1/8. Let N_d=chi(x/d)N, where chi equals1 on the unit ball and0 outside the radius-two ball. Define the compactly supported distributional operator T_d F=D²N_d:F and the smooth far kernel K_d=D²(N-N_d). The canonical tensor formulas of A530 give exactly

    p_t-P2=-T_d m_t-integral K_d(x-y):m_t(y)dy.      (13)

This is justified by testing the canonical distribution; it does not require integrating a singular limiting pressure source through the origin. The operator T_d is a local Calderon-Zygmund operator, including its distributional trace term, and depends only on F within distance2d of x.

Choose a smooth chi0(y) equal1 for |y|<=r1/4 and0 for |y|>=r1/2. On its support and for x in the annulus, K_d(x-y)=D²N(x-y). Split the last term in (13) into

    I_t(x)=-integral chi0(y)D²N(x-y):m_t(y)dy

and its outer complement.

Let k*=1+max K, so r_(k*)>=1. Taylor expansion at y=0 gives, uniformly on the integration region,

    D²N(x-y)=sum_(k in K)((-1)^k/k!)D^(k+2)N(x)[y^k]+R(x,y),
    |R(x,y)|+|D_x R(x,y)|<=C|y|^(k*).                (14)

For every integer j>=0, split the weighted integral at exp(-ct), using (12) in the core and (11) outside. The result is

    integral_(|y|<=r1/2)|y|^j |m_t(y)|dy
          <=C(1+t)exp(-min(r_j,1)t).                 (15)

Indeed the core is O(exp(-r_j t)), since r_j=(j+3-2p)c. In the outer portion the radial integral is exp(-t) integral r^(j+1-3p)dr. It is bounded, logarithmic, or controlled by its lower endpoint according to the exponent, and 1-(3p-2-j)c=r_j. Thus (14) contributes O((1+t)exp(-t)) in C1.

For each k in K make the change Y=exp(tA)y. Exact homogeneity gives

    integral chi0(y)y^(tensor k) tensor m_t(y)dy
      =exp(-r_k t)Q_t^(tensor(k+2))
           [Mom_k-integral(1-chi0(exp(-tA)Y))Y^(tensor k) tensor m(Y)dY].   (16)

The discarded moment tail has norm at most C exp((k+2-3p)ct), since it is supported outside a ball of radius comparable to exp(ct). After its prefactor this is O(exp(-t)). Rotation invariance of N gives

    D^(k+2)N(x):[Q_t^(tensor(k+2))Mom_k]
                     =D^(k+2)N(Q_t^T x):Mom_k.

The same identity can be differentiated in x. We conclude

    I_t=sum_(k in K)exp(-r_k t)Theta_k(Q_t^T x)
                              +O_(C1)((1+t)exp(-t)). (17)

The outer complement in (13) is O(exp(-t)) in C1: its smooth kernel and first derivative are bounded near the diagonal and decay at least as |x-y|^-3 at infinity, while (11) has an integrable majorant away from the excluded core.

## 4. The local singular operator has a fast remainder

For the C0 estimate localize m_t to a fixed ball containing the support of T_d at x. Its sup norm is O(exp(-t)) and its Lipschitz norm is bounded uniformly. The elementary interpolation bound gives

    ||m_t||_(C^beta)<=C_beta exp(-(1-beta)t), 0<beta<1.

The truncated Calderon-Zygmund operator maps this local C^beta class to bounded functions. Hence the near term is O(exp(-(1-beta)t)). Cutoffs and ball sizes are fixed and bounded uniformly over a compact annulus.

For its gradient, choose nested balls around x0 away from0, with T_d at the inner points supported strictly inside the next ball. Distributional differentiation commutes with T_d. Use a fixed cutoff equal1 on that support, and put F_t=chi1 Dm_t. By (9)-(10),

    ||F_t||_infinity<=C exp(-alpha t), [F_t]_alpha<=C.

For 0<beta<alpha the interpolation inequality yields

    ||F_t||_(C^beta)<=C exp(-(alpha-beta)t).           (18)

Therefore D T_d m_t= T_d F_t is bounded by that last quantity on the inner ball. This avoids applying a singular gradient kernel directly to an uncontrolled remainder.

The kinetic difference in S_t-S is O(exp(-t)), and its gradient is O(exp(-alpha t)) by (9)-(10). Given gamma<1, choose 0<beta<alpha<1 with alpha-beta>gamma. Combine (17)-(18) and the outer estimate to prove (4). Cover a compact set by finitely many inner balls. The same local pressure split shows S in C^(1,alpha) for every alpha<1, as already supplied by A539.

Returning to y=exp(tA)x, multiplying by exp(-2(1-c)t), and using r_k+2(1-c)=(k+3)c proves (5) uniformly in direction. No bound O(exp(-t)) for the C1 remainder is asserted, including at the borderline moment c=3/7.

## 5. Two elementary rigidity facts

First, a harmonic function h on a connected open subset of R3 which vanishes together with its gradient on a nonempty C1 embedded surface must vanish identically. Otherwise choose a point of the surface and its lowest nonzero homogeneous Taylor term h_m. Harmonicity makes h real analytic and h_m a nonzero harmonic polynomial; m>=2. Points of the surface approach every tangent direction as x0+epsilon xi+o(epsilon). Dividing h=0 and grad h=0 by epsilon^m and epsilon^(m-1) shows h_m and grad h_m vanish on the tangent plane.

If that plane is {ell=0}, the polynomial h_m is divisible by ell². If h_m=ell^j q for j>=2 with |grad ell|=1, harmonicity implies

    0=j(j-1)q+2j ell grad ell.grad q+ell² Delta q

after division by ell^(j-2). Restricting to the plane shows ell divides q. Iteration makes h_m divisible by every power of ell, impossible. This proves the assertion without assuming the original surface is analytic.

Second, let distinct exponents s1<...<sn<gamma and continuous finite-dimensional coefficient functions phi_j be constant or periodic. If sum exp(-s_j t)phi_j(t)=O(exp(-gamma t)), then all phi_j vanish. Multiplication by exp(s1 t) gives phi1(t)->0; a periodic or constant function with that limit is zero. Repeat. When a constant and a periodic coefficient share a rate, combine them first. The applications below all use the same rotation period when omega!=0.

For completeness the tensor interpretation in Section1 is also elementary. D^ell N is a nonzero constant times r^(-2ell-1) times the symmetric trace-free tensor of x^(tensor ell). Only the full symmetrization and removal of traces of Mom_k can contract with it, where ell=k+2. If that trace-free tensor is T, the resulting numerator is the harmonic homogeneous polynomial T:x^(tensor ell). It is zero identically only if all its symmetric coefficients, hence T, are zero. This proves the stated equivalence for Theta_k.

## 6. The exact sheet premises and rate comparison

Let B=Ay+U, H=P+|U|²/2+(Ay).U and g=U.B. Assume a C1 local surface patch D0 in a regular invariant zero-g H-level has H=Pinf and consists of escaping points with f!=0. Let

    v_t(z)=exp(-tA)Phi_t(z), M_t=Dv_t(z),
    v_t(z)->v(z), M_t->M(z),
    |v_t-v|+|M_t-M|<=C exp(-t), det M=1.

The confirmed A534 or A536 level construction supplies the following exact identities, with a fixed mu>=1 on the component:

    S_t(v_t(z))=0, S(v(z))=0,
    grad S_t(v_t(z))=-(mu/a)exp((1-mu)t)M_t^-T grad H(z),
    M^-T grad H(z)=aV(v(z))/f(z), V(v(z))!=0.          (19)

The limiting sheet T=v(D0) is C1 and embedded after shrinking the patch; its tangent plane contains Ax and Wstar. For mu=1,

    grad S(v(z))=-V(v(z))/f(z),

and for mu>1 it is zero. These are explicit premises of the present local comparison, not consequences of natural bounds alone.

Fix z in D0, x=v(z), and define periodic or constant coefficient functions

    theta_k(t)=Theta_k(Q_t^T x),
    g_k(t)=Q_t grad Theta_k(Q_t^T x).                 (20)

Choose gamma<1 larger than every r_k, and also larger than mu-1 if mu<2. The O(exp(-t)) difference v_t-x changes the evaluations of each smooth multipole and its gradient by O(exp(-t)); their entire rotation circles are compact subsets of D. Since S is C1, S(v_t)=O(exp(-t)). The scalar identity in (19) and (4) therefore give

    sum exp(-r_k t)theta_k(t)=O(exp(-gamma t)).       (21)

The exponential-sum fact implies theta_k=0 for every k and all t. Thus every Theta_k vanishes on T and on every rotation of T.

The gradient difference grad S(v_t)-grad S(x) is O(exp(-gamma t)), using its local C^gamma modulus. If mu=1, subtract the limiting nonzero value from (19) to obtain

    sum exp(-r_k t)g_k(t)=O(exp(-gamma t)).           (22)

If mu>1, the limit gradient is zero and the identity becomes

    sum exp(-r_k t)g_k(t)
        +exp(-(mu-1)t)mu V(x)/f(z)
           =O(exp(-gamma t))+O(exp(-mu t)).         (23)

For mu>=2 the second term is absorbed into the error. In these cases every g_k vanishes, so each harmonic Theta_k has zero value and gradient on T. Section5 gives Theta_k=0 globally.

For 1<mu<2, if mu-1 differs from all r_k, the same exponential-sum argument would force mu V(x)/f(z)=0, contradicting (19). Hence mu-1=r_k for exactly one k. The other g_j vanish, giving Theta_j=0 globally for j!=k. For the surviving index,

    Theta_k(Q_t^T x)=0,
    Q_t grad Theta_k(Q_t^T x)=-mu V(x)/f(z) for every t.  (24)

At t=0 this is a nonzero normal gradient. Thus Theta_k itself is not identically zero. This proves (6) and the source's moment and gradient conclusions.

## 7. Equilibrium and general-level consequences

At a vortical carrier equilibrium under global zero helicity, A496 gives rho<=-a. If rho<-a, A517 supplies a nonempty escaping patch in the associated f!=0 level. A518 gives mu=-a-rho>=1, and A534 supplies (19). Therefore (6) yields (7), since

    -a-1=-(2-2c),
    -a-1-r_k=-(k+3)c,
    -a-2=-(3-2c).

All resonant points lie strictly between -(3-2c) and -(2-2c): r_k is strictly between0 and1. If rho=-(2-2c) or rho<=-(3-2c), all low trace-free moments vanish. At a resonant rho only its one permitted moment can have a nonzero trace-free part. The case rho=-a has no such conclusion from this proof.

For any regular zero-g component with lambda>1 in A536, its constant rate is mu=a(lambda-1), its value is H=Pinf, and it has the same dense escaping patches and identities. Replacing rho by -a lambda proves the identical restriction there. An irrotational equilibrium to which A537's nearby-vortical-level case applies inherits that condition. No claim is made for the separating case or for a component not meeting the exact patch hypotheses.

## 8. Additional global axisymmetry of a resonant multipole

Suppose omega!=0 and 1<mu<2. The rotation parameter t ranges over the full circle group. For any fixed rotation Q_s define the harmonic function

    h_s(x)=Theta_k(Q_s^T x)-Theta_k(x).

Equation (24) shows h_s=0 and grad h_s=0 at every point of the nonempty sheet patch T: the rotated gradient is independent of t and equals its value at0. Section5 therefore gives h_s=0 on all D. Since s was arbitrary, Theta_k is globally axisymmetric about the third axis.

A homogeneous harmonic multipole of degree-(ell+1), with ell=k+2, has the form r^(-(ell+1)) times a spherical harmonic of degree ell. Axisymmetry reduces its angular polynomial to a multiple of the Legendre polynomial P_ell(z), z=x3/r. This can be verified without classification machinery: its trace-free homogeneous polynomial numerator is rotationally invariant, and the harmonic equation reduces to

    ((1-z²)P_ell')'+ell(ell+1)P_ell=0.

Polynomial coefficient comparison leaves one free leading coefficient. For the only degrees here,

    P2(z)=(3z²-1)/2,
    P3(z)=(5z³-3z)/2,
    P4(z)=(35z^4-30z²+3)/8.

They have simple roots in(-1,1):

    k=0: z=+/-1/sqrt3;
    k=1: z=0 or z=+/-sqrt(3/5);
    k=2: z=+/-sqrt((15+2sqrt30)/35)
             or +/-sqrt((15-2sqrt30)/35).             (25)

The multipole coefficient is nonzero by (24). Its regular zero surface is the union of the corresponding circular cones, with z=0 denoting the equatorial plane. Each connected sufficiently small T lies on one of them. Since grad Theta_k is nonzero there, inclusion of the C1 surface with equal tangent dimension makes it locally a relatively open piece of that cone. The vector Wstar is tangent by the original sheet geometry.

The sheet cannot meet the rotation axis. At an axial x, (24) makes grad Theta_k(x) invariant under all rotations, hence axial. Euler's homogeneous identity and Theta_k(x)=0 give x.grad Theta_k(x)=0, so that gradient would be zero, contradicting (24). This also follows from P_ell(+/-1)!=0 in (25).

This is rigidity of a single finite pressure multipole. It does not make V or the full profile axisymmetric, does not globalize E=0, and supplies no contradiction to the remaining resonant witnesses.

## 9. Source comparison and remaining scope

The complete C38 Section5e was read. The proof reconstructs its moment, pressure, harmonic and rate arguments with the canonical constants, spatial derivative estimates and exact surface hypotheses stated. The additional Section8 consequence was posted to the existing configured-model Theory Agent C agent through the auditor notes for a continued comparison. No reply is assumed before it is actually read.

The main decay-only conjecture remains open. Even in the natural derivative class, the cases mu=1, the finite resonant rates, and mu>=2 are not excluded. No gradient expansion at the exact exp(-t) order is claimed, and no low-moment condition is inferred at rho=-a. All statements cover every fixed finite omega; constants may depend on it. No computation, new model client or formal build was used.
