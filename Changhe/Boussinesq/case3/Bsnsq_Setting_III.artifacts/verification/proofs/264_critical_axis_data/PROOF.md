# Critical tails compatible with the low-order axis equations

## Exact statement and limitation

For every beta>2 there exist smooth real functions b,rho,r,eta,v,T,R,G,I on the whole real axis and a constant A>0 with the following properties. Write

    d=(3beta+2)/2, kappa=(beta+6)/2,
    gamma=1/2+1/beta, m=1-2/beta, c2=-A/beta.

Then rho>0, T=A/rho^2, R(y)=integral_0^y rho, G(y)=integral_0^y rho I, b(0)=0, b'(0)=d, and

    rho b=dR,
    b r'+(beta/2)r=A/rho,       eta=r/rho,
    eta=-b''-2v,
    rho^3 v=c2+(A/8)(dRI-kappa G).                              (1)

The functions have polynomially controlled tails, b(y)=beta y for |y|>=2, T never vanishes, T(0)=A, and eta(0)=2A/beta. At the positive end,

    I(y)=L y^(-m)+O(y^(-1+1/beta)),     L<0.                     (2)

Thus the critical exponent in the necessary restriction liminf y^(-s)|I|=0 for s>-m is attained within this system of low-order axis equations.

For beta=2 there are such smooth axis data with any prescribed finite limit of I at the positive end. The same identities (1) hold, with m=0. This is compatible with the supercritical theorem, which at beta2 only treats s>0.

These statements concern a one-dimensional subsystem. They do not construct B2 profiles or a canonical full-plane inverse, do not satisfy all higher transverse equations, and do not show that a critical tail is attainable by a full profile. In particular they cannot be used to refute the general B2 question or any theorem using additional equations. A polynomial transverse realization is given at the end to make the omitted equations explicit. The restriction b(y)=beta y outside a compact set is an axis property, not the required full-plane velocity asymptotic.

## A smooth axis transport and density

Let theta(t)=exp(-1/t) for t>0 and theta(t)=0 for t<=0. Define the even smooth cutoff

    chi(y)=theta(y^2-1)/[theta(y^2-1)+theta(4-y^2)].

Its denominator is positive for every real y. It is zero on |y|<=1 and one on |y|>=2. On (1,2) its numerator increases and the second denominator summand decreases, so chi'>0 there. Both transitions are flat at their endpoints, by the standard derivative formula for exp(-1/t), whose derivatives tend to0 at0 from the right.

Put

    b(y)=y[d+(beta-d)chi(y)].                                   (3)

This is smooth and odd, equals dy for |y|<=1, and equals beta y for |y|>=2. On y>0 it is positive, and b'(y)<=d: the bracket is at most d, and its derivative is(beta-d)chi'<=0. Here beta<d for beta>=2. The derivative b' need not be positive in the transition; no such condition is used.

Set rho=1 on [0,1] and solve on y>1

    rho'/rho=(d-b')/b,     rho(1)=1.                            (4)

The coefficients are smooth and flat where the nonconstant region begins, so rho extends smoothly through1. It remains positive and is nondecreasing, since d-b'>=0. Extend rho evenly to the negative axis, retaining rho=1 around0. Then rho is globally smooth. Equation (4) also holds for y<0 by parity. The product derivative satisfies(rho b)'=d rho everywhere, including0. Since rho(0)b(0)=0, R=rho b/d equals the required integral_0^y rho.

For y>=2, (4) becomes rho'/rho=gamma/y. Hence for some C>0,

    rho=C y^gamma,       R=(beta C/d)y^(gamma+1).                (5)

There is no additive constant in the second formula, since R=rho b/d. On the negative axis the corresponding formulas use |y| and the sign of R. Every derivative has polynomial control at infinity. T=A/rho^2 is smooth, nonzero everywhere and equals A near0. Substitution in (4) gives bT'+(3beta+2-2b')T=0.

## The vorticity coefficient and transverse velocity coefficient

Set a=beta/(2d)>0. On y>0 define

    r(y)=(A/d) R(y)^(-a) integral_0^y R(t)^(a-1) dt.             (6)

The integral converges at0 because R(t)=t there and a>0. For y<=1 it gives r=2A/beta exactly. Thus r has a smooth even extension to all y, defined by reflection. Differentiating (6), using R'/R=d/b, proves b r'+(beta/2)r=A/rho. It also shows r/A>0 for y>0; the even extension preserves this. Define

    eta=r/rho,       v=-(b''+eta)/2.                            (7)

These functions are smooth on R; no parity in y is imposed on v. On |y|<=1, eta=2A/beta and v=c2=-A/beta. Equations (4) and (6) give the first-order vorticity equation

    b eta'+(2beta+1-b')eta=T,

and (7) is the required curl identity.

For y>=2, the explicit solution of the linear equation is

    r=D y^(-1/2)-(A/C)y^(-gamma),
    eta=(D/C)y^(-1-1/beta)-(A/C^2)y^(-1-2/beta),                (8)

for a constant D. Since r(2)/A>0, the formula
D/A=(r(2)/A)sqrt(2)+C^(-1)2^(-1/beta) proves D/A>0. The ratio D/A depends on beta and the chosen cutoff but not on A. On this tail b''=0, so v=-eta/2.

## The fourth-order thermal coefficient

For beta>2 put G=0 on |y|<=1. Away from that interval solve the two smooth linear equations to its right and left with the endpoint data0:

    bG'-kappa G=(8/A)(rho^3 v-c2).                              (9)

The right hand side is zero throughout |y|<=1 and is flat at its boundary. Since b is nonzero at each boundary and everywhere outside0, the two extensions are smooth and global. Set I=G'/rho. Then G(0)=0 and G'=rho I, so G is exactly integral_0^y rho I. With dR=rho b, equation (9) is precisely the last identity of(1). Define the formal fourth thermal coefficient Q=A^2 I/rho^4. This is smooth and realizes I=Q/T^2.

For beta2, kappa=d, and one may instead set G=I0 y on |y|<=1, with arbitrary real I0. This solves (9) there because b=dy. The same extension defines global smooth G and I. No singular initial-value problem at b(0)=0 is being asserted: the solution is explicitly prescribed on an open neighborhood of0, then continued where b is nonzero.

On y>=2, substitution of (5) and (8) into (9) gives

    beta y G'-kappa G
       =-(4DC^2/A)y^(1/2+2/beta)+4C y^gamma-8c2/A.

The distinct particular exponents have nonzero coefficients under this linear operator: beta(1/2+2/beta)-kappa=-1 and beta gamma-kappa=-2. Thus for a real K,

    G=K y^(kappa/beta)+(4DC^2/A)y^(1/2+2/beta)
        -2C y^gamma+8c2/(A kappa),
    I=L y^(-m)+(4DC/A)(1/2+2/beta)y^(-1+1/beta)
        -2gamma y^(-1),
    L=K kappa/(beta C).                                        (10)

The error exponent -1+1/beta is strictly smaller than -m for every finite beta>0. Formula(10) therefore has the claimed critical leading power whenever L is nonzero. We next prove that L can be chosen strictly negative, rather than assuming that it is generic.

## A nonzero critical coefficient for beta>2

The transport b, rho and R are independent of A. Write r=A r1 and eta=A eta1. For the choice G=0 near0, linearity of (9) gives

    G=A^(-1)G_b+G_eta,
    bG_b'-kappa G_b=-4rho^3 b'',
    bG_eta'-kappa G_eta=-4rho^3 eta1+8/beta,                    (11)

with both summands zero near0. The first forcing is compactly supported on the positive side in [1,2]. Thus G_b/y^(kappa/beta) has a finite real limit K_b as y tends to positive infinity.

To determine the sign of the second limit, put q=rho^3 eta1=rho^2 r1 and u=q-2/beta. Direct differentiation using (4) and the r1 equation gives

    b u'=[2d-beta/2-2b']u+(4/beta)(d-b')+(rho-1).                (12)

Initially u=0. Both forcing terms on the right are nonnegative on y>0 by b'<=d and rho>=1; they are strictly positive on a subinterval after1. The scalar integrating-factor formula applied on [1,y], with b>0, proves u>=0 everywhere on the positive side and u>0 after that subinterval. In particular the G_eta forcing in (11) equals -4u and is strictly negative on a tail.

Let mu_h=exp(integral_1^y kappa/b)>0. Then

    G_eta/mu_h=-4 integral_1^y u/(b mu_h).                       (13)

The improper integral is finite. Indeed for y>=2, formula(8) gives q=(D/A)C^2 y^(1/2+2/beta)-C y^gamma, whereas mu_h=C_h y^(kappa/beta) for a positive C_h. The integrand in(13) is O(y^(-1-1/beta)), with further faster-decaying terms. It is integrable for every finite beta>0. Since it is nonnegative and strictly positive on an interval, its integral is strictly positive. Therefore

    K_eta=lim G_eta/y^(kappa/beta)<0.

It follows from (10)-(11) that L=L_b/A+L_eta, where L_b is finite real and L_eta<0. Taking, for example, any A>1+2|L_b|/|L_eta| yields L<0. This proves existence of the critical asymptotic(2) for every beta>2 using an explicit smooth transport and a finite choice of A. The argument is independent of numerical quadrature.

## Optional dilation with prescribed A>0

The preceding result allows A to be chosen after the cutoff. A related version permits any prescribed A>0 if the transition scale is also free. Let b,rho,r1,G_b,G_eta be the base objects above. For lambda>0, put s=y/lambda and

    b_lambda(y)=lambda b(s), rho_lambda(y)=rho(s),
    R_lambda(y)=lambda R(s), r_lambda(y)=A r1(s),
    eta_lambda(y)=A eta1(s),
    v_lambda(y)=-[lambda^(-1)b''(s)+A eta1(s)]/2,
    G_lambda(y)=(A lambda)^(-1)G_b(s)+G_eta(s).

All four identities (1) follow by direct differentiation, with the same beta,d,kappa and c2=-A/beta. Near zero G_lambda=0. In particular b_lambda G_lambda'-kappa G_lambda equals
lambda^(-1)A^(-1)[bG_b'-kappa G_b]+[bG_eta'-kappa G_eta], precisely the required forcing. The derivative of G introduces a further factor lambda^(-1). Thus, if I_b=G_b'/rho and I_eta=G_eta'/rho,

    I_lambda(y)=(A lambda^2)^(-1) I_b(y/lambda)
                    +lambda^(-1) I_eta(y/lambda),
    L_lambda=lambda^(m-2)L_b/A+lambda^(m-1)L_eta
             =lambda^(m-1)[L_b/(A lambda)+L_eta].              (14)

The common positive prefactor lambda^(m-1) is essential for the numerical coefficient, although it does not affect its sign. Since L_eta<0, taking lambda>1+2|L_b|/(A|L_eta|) gives L_lambda<0 for every prescribed A>0. The transport now equals beta y for |y|>=2lambda and dy for |y|<=lambda. This is a dilation of the axis-data construction; no claim that it is the physical spatial-scaling symmetry of a full profile is made.

## Arbitrary finite critical limit at beta2

At beta2, kappa=d. The globally defined R satisfies bR'-kappa R=0. If G_base solves(9) with zero inner value, then G=G_base+I0 R solves the same equation and has G=I0 y near0. Accordingly I=I_base+I0 everywhere. Formula(10), with m=0, shows I_base tends to a finite real L_base at the positive end. Taking I0=L_target-L_base realizes any prescribed finite real limit L_target. The fields T, b, eta and v are unchanged by this modification; only the fourth thermal coefficient changes.

## Explicit transverse realization and the missing equations

One can realize these data as smooth whole-plane polynomial jets by setting

    Theta=T(y)x^2/2+Q(y)x^4/24,
    W2=b(y)+v(y)x^2,
    W1=(2beta-b'(y))x-v'(y)x^3/3,
    Omega=partial_y W1-partial_x W2
         =eta(y)x-v''(y)x^3/3.

These fields have the required x parity, exact div W=2beta, W(0)=0 and local quadratic thermal coefficient A/2. Equations(1) make the x^2 and x^4 coefficients of the thermal residual and the x coefficient of the vorticity residual zero. For completeness, the coefficient of x^4 in 24 times the thermal residual is

    bQ'+(7beta+2-4b')Q-8v'T+12vT'.

Substituting Q=T^2 I and T=A/rho^2, and using bT'=-2(d-b')T, its vanishing becomes

    bI'+(beta-2)I=8( rho^3 v)'/(A rho).

Differentiating the last identity of (1), with R'=rho and G'=rho I, gives this equation because d-kappa=beta-2. Conversely its integration from zero gives the last identity of (1), with integration constant v(0)=c2 since rho(0)=1 and R(0)=G(0)=0. The value v(0)=c2 is supplied by the construction: b=dy near zero gives b''(0)=0, r(0)=eta(0)=2A/beta, and hence v(0)=-A/beta by (7). Higher coefficients are not imposed and generally do not vanish. For a concrete nonzero defect when I0!=0, at beta2 and |y|<1 the vorticity residual has coefficient -A^2 I0/6 at x^3. Moreover the cubic-in-x term in W1 and quadratic-in-x term in W2 generally violate W-beta X=o(|X|) along other directions. This realization is not a B2 candidate and no canonical inverse is claimed.

The construction proves a precise limitation of deductions based solely on the four low-order axis identities and b/y -> beta. It leaves the full transverse PDE, canonical inverse and general profile problem OPEN.

## Dependencies and evidence

The proof uses smooth flat cutoffs, exact scalar integrating factors and the explicit tail solutions. The relation of (1) to the B2 Taylor coefficients is derived in the preceding section and in the complete P263 proof. This standalone argument was written and checked before writing new verification code. Exact algebra controls and any optional independent quadrature will be stored in verification/. Such computations check formulas but are not the existence argument. No formal build is run.
