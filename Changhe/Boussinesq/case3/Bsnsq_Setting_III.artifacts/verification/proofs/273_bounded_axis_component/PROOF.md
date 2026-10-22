# A bounded central component for the low-order axis equations

## Statement and scope

For every beta>=2 and A!=0 there are globally smooth real functions b,T,eta,v,D on the real axis with the following properties. The function b is odd, equals d y for |y|<=1, where d=(3beta+2)/2, and equals beta y for |y|>=5. Its zeros are precisely 0,3,-3. The central component J of {T!=0} is (-3,3), T(0)=A, eta(0)=2A/beta, and v(0)=-A/beta. The functions T,eta,D vanish outside J and are flat at both endpoints. The following physical axis identities hold on the entire real line:

    b T'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T,
    eta=-b''-2v,
    b D'+(7beta+2-4b')D-8v'T+12vT'=0.          (1)

All derivatives of b-beta y, T,eta,v,D have compact support. On J set rho=sqrt(A/T)>0, R=integral_0^y rho, r=rho eta, I=D/T^2 and G=integral_0^y rho I. They obey

    rho b=d R, b r'+(beta/2)r=A/rho,
    rho^3v=c2+(A/8)(d R I-kappa G),            (2)

where c2=-A/beta and kappa=(beta+6)/2. At either finite endpoint, putting s=3-|y|, one has

    D/T=-(6d/beta)s^(-2)(1+o(1)),
    A I -> -infinity.                         (3)

In particular the low-order axis identities and arbitrarily strong decay along the axis do not imply that J is unbounded. This is a construction of axis jets, not a solution of B2. An explicit smooth polynomial extension below obeys divergence, curl, parity and the center equations, and the full transport equations near the center, but fails the required sublinear velocity bound. No completion satisfying the full-plane inverse or all transverse transport equations is asserted or excluded.

## Construction of b and the second-order thermal jet

Let theta(t)=exp(-1/t) for t>0 and theta(t)=0 otherwise. For a<c put chi_{a,c}(y)=theta(y-a)/(theta(y-a)+theta(c-y)). Its denominator is positive everywhere, and it is smooth, equals0 on y<=a and1 on y>=c, and lies strictly between0 and1 in between. For y>=0 put

    q(y)=(1-chi_{1,2}(y))d y+chi_{1,2}(y)(y-3)^2,
    b(y)=(1-chi_{4,5}(y))q(y)+chi_{4,5}(y) beta y.

Extend b oddly. It is smooth because it equals d y near0. Each interpolation is between positive functions away from3; near3 it is exactly (y-3)^2. Thus there are no further positive zeros. Odd reflection gives the negative zeros. On J, b has the sign of y and b=d y near0.

Set rho=1 on |y|<=1 and solve

    rho'/rho=(d-b')/b

on the remainder of J. The coefficient has all derivatives zero at the inner attachment points -1 and 1, where b is nonzero, so the positive solutions join smoothly to rho=1. Since b is odd, rho is even. Differentiation gives (rho b)'=d rho; integration from0 proves the first equation in(2). In particular R>0 for y>0. Define T=A/rho^2 on J.

For 2<=y<3 put s=3-y and tau=1/s. Direct integration of the rho equation gives an exact constant C_rho>0 such that

    rho=C_rho s^(-2) exp(d/s),
    R=(C_rho/d) exp(d/s),
    T=(A/C_rho^2)s^4 exp(-2d/s).                (4)

The formula for R follows from rho b=dR, so no unspecified additive constant is present. At -3 use s=3+y; rho and T have the same formulas and R has the opposite sign. Each spatial derivative of T is a finite sum of powers of s times exp(-2d/s); these tend to0. Extend T by0 outside J. This is smooth and flat at both endpoints, and its first equation in(1) holds on J by the definition of rho and everywhere else by smooth continuation.

## The first vorticity jet and curl

Put alpha=beta/(2d), which lies in (0,1), and define for 0<y<3

    r(y)=(A/d) R(y)^(-alpha) integral_0^y R(u)^(alpha-1) du.       (5)

Since R=y on (0,1], the integral at0 is convergent and r=2A/beta there. Differentiating(5), using R'=rho and b rho=dR, gives b r'+(beta/2)r=A/rho. Extend r evenly to J, where the same equation holds because b and r' both change sign. Set eta=r/rho.

The integral in(5) tends to a positive finite limit as y approaches3: near0 its integrand is u^(alpha-1), while near3 formula(4) makes it an exponentially decreasing function. In terms of tau the tail of that integral is a positive constant times

    integral_tau^infinity sigma^(-2) exp(-(d-beta/2)sigma) d sigma.

Here d-beta/2=beta+1>0. Repeated differentiation of this tail, or its defining integral followed by differentiation, shows that its tau derivatives are polynomially bounded multiples of exp(-(beta+1)tau). Hence r and all its tau derivatives are bounded by powers of tau times exp(-beta tau/2). Multiplication by rho^-1 then gives, with a nonzero constant of the sign of A,

    eta=C_eta tau^(-2) exp(-(2beta+1)tau)(1+o(1)).                (6)

All tau derivatives of eta have the same form of exponential bound. Spatial differentiation is plus or minus tau^2 d/dtau, so eta and all spatial derivatives tend to0. Extend eta by0 outside J. The equation for r implies the second equation in(1), since d+beta/2=2beta+1. Define v=-(b''+eta)/2 globally. This is smooth and compactly supported and gives the curl identity. In |y|<=1 it equals c2=-A/beta.

## The fourth-order thermal jet

Set G=0 on |y|<=1. On each remaining part of J solve the linear equation

    b G'-kappa G=(8/A)(rho^3v-c2).               (7)

Its forcing vanishes on |y|<=1, so the solutions join smoothly to the zero solution there. There is no singular point of b on J except0, already covered by this zero solution. Define I=G'/rho and D=T^2 I on J. Then G=integral_0^y rho I and (7) is exactly the last identity in(2). These definitions also give D=0 near0.

To see the fourth equation of(1), differentiate

    rho^3v=c2+(A/8)(d R I-kappa G).

Its derivative is

    (rho^3v)'=(A/8)[dR I'+(d-kappa)rho I].

Use dR=b rho, d-kappa=beta-2, rho'/rho=(d-b')/b, T=A/rho^2 and D=T^2 I. After multiplication by 8T/rho^3, this is

    b D'+(7beta+2-4b')D=8v'T-12vT'.             (8)

This is an exact algebraic identity on J; it does not presuppose convergence of a transverse Taylor series.

It remains to prove that D extends smoothly by0, since G itself may diverge at the endpoints. At either endpoint use tau=1/(3-|y|). There b d/dy=d/dtau and b'=-2/tau. Put c=7beta+2 and F=8v'T-12vT'. Equation(8) becomes

    D_tau+(c+8/tau)D=F.                         (9)

At the positive endpoint v=-1-eta/2 and T'/T=-4tau-2d tau^2. At the negative endpoint v=1-eta/2 and T'/T=4tau+2d tau^2. Formula(6) and its derivative bounds show, at either endpoint,

    F/T=-24d tau^2-48tau
         +O(tau^N exp(-(2beta+1)tau))            (10)

for some fixed finite N. All tau derivatives of the remainder admit such exponential bounds, with possibly different polynomial powers. The leading sign in(10) is the same at both endpoints. From(4), F=O(tau^-2 exp(-2d tau)). The integrating-factor formula for(9) is

    D=tau^-8 exp(-c tau)
         [C+integral_{tau0}^tau sigma^8 exp(c sigma) F(sigma) d sigma].     (11)

Since c-2d=4beta>0, its integral is O(tau^6 exp(4beta tau)); this bound follows by integration by parts, or by differentiating a polynomial times exp(4beta tau). Thus

    D=O(tau^-2 exp(-2d tau)).                   (12)

Repeated differentiation of(9), using the derivative bounds of F, bounds each derivative of D by a polynomial times exp(-2d tau). Converting back to y proves that every derivative tends to0. The zero extension of D is therefore smooth. On the complement of J, all thermal and vorticity jets in(1) vanish, so the transport identities hold there; at the endpoints they hold by continuity. This proves all global identities.

For the sharper assertion(3), set K=D/T inside J. Since T_tau/T=-4/tau-2d, equations(9)-(10) imply

    K_tau+(4beta+4/tau)K
        =-24d tau^2-48tau+O(tau^N exp(-(2beta+1)tau)).          (13)

Multiply by tau^4 exp(4beta tau). Integration by parts shows that the contribution of -24d tau^6 exp(4beta tau) is asymptotic to -(6d/beta)tau^6 exp(4beta tau); the term of degree5 is one degree lower. The exponentially smaller forcing contributes o(tau^2) after division by the integrating factor. Its integral estimate holds whether its net exponential exponent is positive, zero or negative. The homogeneous term also decays. Thus K/tau^2 tends to -6d/beta. Finally A I=(A/T)K with A/T=rho^2>0 diverging at the endpoints, proving(3).

## A smooth extension and its failure as a profile

The following are globally smooth fields, with no y-reflection condition imposed on the physical quantities:

    Theta(x,y)=T(y)x^2/2+D(y)x^4/24,
    W2(x,y)=b(y)+v(y)x^2,
    W1(x,y)=(2beta-b'(y))x-v'(y)x^3/3,
    Omega(x,y)=eta(y)x-v''(y)x^3/3.             (14)

Their x parities are the required ones, Theta(0,y)=0, W(0)=0, div W=2beta, and Omega=partial_y W1-partial_x W2 with the B2 sign convention. The x^2 and x^4 thermal equations and the x vorticity equation are precisely(1); higher transverse coefficients are not asserted to vanish.

In |y|<=1 the fields reduce to

    W1=(beta-2)x/2, W2=d y-Ax^2/beta,
    Theta=Ax^2/2, Omega=2Ax/beta.

Direct substitution verifies both full stationary transport equations in this strip. The center normalization is a0=A/2 and Omega_x(0)=2A/beta=4a0/beta. However, on y=0 the relative velocity V=W-beta(x,y) has second component -Ax^2/beta. For A!=0 this fails V=o(|X|), independently of any additive constant velocity. Thus(14) is not an admissible B2 profile. The axis construction does not address whether another full-plane completion could satisfy all the equations. The general B2 problem remains OPEN.

## Dependencies and verification

The proof is self-contained in the smooth cutoff definition and the displayed ordinary differential equations. The physical axis equations are derived directly by the polynomial coefficient calculation in(14); they use the prompt's negative-curl convention. P237 motivates the bounded-component question, and P272 treats infinite ends under quantitative bounds, but neither is needed as an unproved input here. The finite endpoint divergence in(3) does not contradict either an infinite-end limit or an infinite-end exclusion.

Independent exact symbolic controls and the model-review adjudication belong in verification/. They supplement this argument and do not constitute a numerical existence claim. No Lean or Lake execution is authorized.
