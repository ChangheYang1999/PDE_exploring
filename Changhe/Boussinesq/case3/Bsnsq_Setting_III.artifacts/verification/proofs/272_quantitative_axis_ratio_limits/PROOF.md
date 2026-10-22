# Quantitative critical limits of normalized axis jets

## Exact statements and scope

Fix beta>=2 and A!=0. Put

    d=(3beta+2)/2, kappa=(beta+6)/2,
    gamma=1/2+1/beta, m=1-2/beta.

Consider smooth real axis data b,rho,r,v,I on an interval J containing0, with rho>0, rho(0)=1, b(0)=0. Define R=integral_0^y rho, G=integral_0^y rho I, eta=r/rho and c2=v(0). Assume the four exact relations

    rho b=dR, b r'+(beta/2)r=A/rho,
    eta=-b''-2v,
    rho^3v=c2+(A/8)(dRI-kappa G).                 (1)

Suppose J has an infinite positive end and, for some delta>0,

    |(d/dy)^j[b(y)-beta y]|<=C_j y^(1-delta-j),
                             j=0,1,2, y>=Y.       (2)

Then, with epsilon=min(delta,1/beta)>0, there is a finite real L such that

    I(y)=L y^(-m)+O(y^(-m-epsilon)).               (3)

In particular the normalized critical ratio y^m I has a finite limit. No sign or nonzero value of L is asserted. The same result holds at a negative infinite end, with |y| and its own finite real coefficient. The result uses only(1)-(2); neither full-plane inversion nor the higher transverse PDE coefficients are needed for this first statement.

For a smooth nontrivial class-A B2 profile, the independently proved velocity symbol bound |D^j V|<=C_j |X|^(1-1/beta-j), V=W-beta X, gives(2) with delta=1/beta. Thus at every infinite end of the central component of {Theta_xx(0,y)!=0},

    I_2=Theta_xxxx/Theta_xx^2
       =L |y|^(-m)+O(|y|^(-1+1/beta)).             (4)

At beta2, I_2 has a finite limit. P266 proves I_2=L y^(-m)(log y)^ell(1+o(1)), L!=0, ell>0, for every beta>=2; P270 proves the same form with either sign for beta>2. In both constructions y^m I_2 diverges with the sign of L. This contradicts the finite critical limit in(3), for every beta in the construction's stated range, not only beta2. The logarithmic axis constructions P266 and P270 therefore cannot satisfy all these necessary quantitative conditions of a class-A profile. Their incompatibility is stronger than saying that a particular polynomial extension fails sublinearity. This does not invalidate those constructions as low-order axis data under the weaker condition b/y->beta.

A further consequence uses the established smooth rescaled temperature limit of P36. For every integer n>=1 let

    I_n(y)=partial_x^(2n)Theta(0,y)/T(y)^n,
    T(y)=Theta_xx(0,y).

Then, for an actual class-A profile and each infinite end, finite real constants L_n exist with

    I_n(y)=L_n |y|^(-(n-1)m)
                   +O(|y|^(-(n-1)m-1/beta)).       (5)

Here I_1=1 and L_1=1. These are necessary far-field statements, not an assertion that the normalized ratios are constant on J. They do not treat bounded J, prove a profile, or give a general B2 exclusion. All uses of previously verified class-A regularity are explicit dependencies below.

## The full axis proof at the positive end

An infinite positive end means [0,infinity) is contained in J. Since rho>0, R(y)>0 for y>0, and(1) gives b>0 there. Also

    R'/R=d/b.

For large y, (2) implies b=beta y(1+O(y^-delta)), so

    d/b=d/(beta y)+O(y^(-1-delta)).

The error is absolutely integrable to infinity, and its tail integral is O(y^-delta). Integrating the logarithmic derivative and exponentiating gives a finite C_R>0 with

    R=C_R y^(d/beta)(1+O(y^-delta)),
    rho=C_rho y^gamma(1+O(y^-delta)),
    C_rho=d C_R/beta>0.                             (6)

This obtains a nonzero coefficient, rather than merely upper and lower power bounds. No asymptotic formula has been differentiated. Positivity of C_R follows from the positive value of R at a fixed point times the exponential of a convergent real integral.

Choose a sufficiently large Y and set

    mu_r=exp(integral_Y^y beta/(2b)),
    h=exp(integral_Y^y kappa/b).

The same integrable-error argument gives positive constants C_mu,C_h with

    mu_r=C_mu y^(1/2)(1+O(y^-delta)),
    h=C_h y^(kappa/beta)(1+O(y^-delta)).             (7)

Variation of constants in the second relation of(1) gives

    r=mu_r^(-1)[r(Y)+A integral_Y^y mu_r/(b rho)].

By(6)-(7), the integrand is O(y^(-1-1/beta)). This is absolutely integrable because beta is finite and positive. Thus

    r=O(y^-1/2), eta=O(y^(-1-1/beta)).               (8)

No sign of A, r or the integral's limiting constant is required here. The exact formula could also give a finer expansion, but the stated estimate suffices.

Define

    H=A G/h, P=rho^3/(b h), f=eta+2c2/rho^3.

Since 3gamma-1-kappa/beta=0, (6)-(7) show

    P=P_infinity(1+O(y^-delta)), P_infinity>0.       (9)

Rearrange the last identity in(1), using dR=b rho and G'=rho I:

    bG'-kappa G=(8/A)(rho^3v-c2).

Differentiating H exactly and using h'/h=kappa/b yields

    H'=8P(v-c2/rho^3)=-4P(b''+f).                 (10)

By(2), b''=O(y^(-1-delta)). By(6), rho^-3=O(y^-3gamma). Since

    3gamma>1+1/beta,

(8)-(10) imply

    H'=O(y^(-1-epsilon)), epsilon=min(delta,1/beta).

This is an absolute bound with epsilon>0. Therefore a finite real H_infinity exists, and direct tail integration gives

    H=H_infinity+O(y^-epsilon), bH'=O(y^-epsilon). (11)

Finally, differentiate G=hH/A and divide by rho to get the exact identity

    I=h/(A b rho)[kappa H+bH'].                   (12)

The prefactor in(12) is

    h/(A b rho)=C_h/(A beta C_rho)
                        y^-m(1+O(y^-delta)),

because kappa/beta-1-gamma=-m. Combining this with(11) proves(3), with

    L=kappa C_h H_infinity/(A beta C_rho).         (13)

Changing the positive normalization of h changes C_h and H_infinity reciprocally, so L is independent of the chosen integrating-factor normalization. The proof is valid when H_infinity or L is zero. It contains no division by either quantity.

## Reflection and application to actual profile data

For physical B2 fields, write V=W-beta X and use the convention Omega=partial_y W1-partial_x W2. The exact equations are

    div W=2beta, W.grad Theta=(beta-2)Theta,
    W.grad Omega+Omega=Theta_x.

Assume W1 and Omega are odd in x, W2 and Theta are even in x, Theta(0,y)=0, W(0)=0, and T(0)=A!=0. These are the relevant class-A parity and center hypotheses. They give, on the central component where T has the sign of A,

    b=W2(0,y), rho=sqrt(A/T), r=rho Omega_x(0,y),
    v=W2_xx(0,y)/2, I=Theta_xxxx(0,y)/T^2.

For clarity the two transport coefficients are

    bT'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T.

The x^4 thermal coefficient is

    b D'+(7beta+2-4b')D-8v'T+12vT'=0,
    D=Theta_xxxx.

Substitution of T=A/rho^2 and D=T^2 I gives the derivative of the last identity in(1); integration from0 supplies the constant c2. Curl supplies eta=-b''-2v. Thus the data satisfy all relations(1), without assuming an analytic Taylor series.

Reflect a negative end by

    Wtilde(x,y)=(W1(x,-y),-W2(x,-y)),
    Thetatilde(x,y)=-Theta(x,-y),
    Omegatilde(x,y)=-Omega(x,-y).

At the level of arbitrary axis data, the corresponding reflection is btilde(y)=-b(-y), rhotilde(y)=rho(-y), Rtilde(y)=-R(-y), rtilde(y)=-r(-y), vtilde(y)=-v(-y), Itilde(y)=-I(-y), Gtilde(y)=G(-y), Atilde=-A and c2tilde=-c2. Substitution preserves every identity(1), so the negative-end result also holds for abstract axis data without any physical realization.

These definitions preserve the PDE, parities and power symbol bounds. They send A to-A, rho(y) to rho(-y), b(y) to-b(-y), I(y) to-I(-y). Applying the positive-end proof and reflecting back proves the asserted negative-end expansion, with a possibly different signed coefficient. No y-reflection symmetry of the original solution is assumed.

The class-A velocity symbol estimate is precisely (12) in P36, with s=1/beta. Restricted to x=0 it gives(2) for j=0,1,2. This implication uses actual derivatives of the velocity bound from P36; it does not differentiate a mere estimate of b-beta y. Consequently(4) is an unconditional consequence within the established class-A theory, although that theory itself uses both full PDEs and canonical inversion.

## Higher normalized axis jets from smooth physical limits

P36 proves that for physical rescalings

    theta_tau(z)=tau^(beta-2)Theta(tau^-beta z),

there is a smooth limit theta_0(z) on R2 minus{0}, and a smooth theta_1 such that, on each compact annulus and for every finite j,

    theta_tau=theta_0+tau theta_1+o_C^j(tau).       (14)

Its proof establishes all spatial derivative convergence by a localized transport/div-curl induction, then integrates the exact physical temperature equation in time. This result applies for beta>=2. It is stronger than convergence of values on circles, which would not suffice here.

For positive y take tau=y^-1/beta and z=e2=(0,1). Differentiating the exact rescaling in x a finite number of times, and using(14) at j=2n, gives

    partial_x^(2n)Theta(0,y)
       =y^(m-2n)[a_n+O(y^-1/beta)],
    a_n=partial_z1^(2n)theta_0(e2).                (15)

The denominator coefficient is nonzero. Indeed(6), specialized to delta=1/beta, gives

    T=A/C_rho^2 y^(-1-2/beta)(1+O(y^-1/beta)).    (16)

Since m-2=-1-2/beta, comparison of(15) for n=1 with(16) shows

    a_1=A/C_rho^2!=0.

The quotient of(15) by the nth power of(16) is therefore well-defined on the tail, and its leading coefficient is

    L_n=a_n/a_1^n.

Its power of y is

    m-2n-n(m-2)=-(n-1)m.

Elementary multiplication of the finitely many factors (1+O(y^-1/beta)) and inversion of the nonzero denominator prove(5), including when a_n=0. For a negative end use e2 replaced by-e2 and |y|, or use the reflected fields. The sign change of I_n under reflection is (-1)^(1-n), which only changes the corresponding coefficient; finiteness and the error order are unchanged.

At beta2 all powers -(n-1)m vanish. Thus every I_n has a finite limit at any infinite end of J for an actual class-A profile. This fact neither makes the profile analytic nor imposes constancy of the ratios at finite y.

## Dependencies, evidence and limits

The first theorem is proved entirely from(1)-(2) by exact calculus and absolutely convergent integrals. The profile specialization uses the previously independently verified P36 all-order symbol bounds, whose local proof has been reread for this argument, and its explicit class-A prerequisites from P33 and P35. The higher-ratio result uses P36's full annular C^j expansion(14), not a numerical fit or an unproved differentiation of angular asymptotics.

These dependencies will be frozen and hashed. The present complete informal proof is written before independent algebraic controls and a new Opus5.5 consultation. No formal build is authorized. Any external-review availability limitation and every actual result will be recorded in verification/SUMMARY.md. The broad B2 problem remains OPEN.
