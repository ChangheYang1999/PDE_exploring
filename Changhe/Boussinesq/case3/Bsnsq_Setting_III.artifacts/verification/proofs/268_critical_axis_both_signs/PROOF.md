# Critical axis tails with either sign

## Statement and scope

Fix beta>=2 and write d=(3beta+2)/2, kappa=(beta+6)/2, gamma=1/2+1/beta and m=1-2/beta. For every prescribed A>0 there are globally smooth real axis data b,rho,R,r,eta,v,T,G,I, with rho>0, b(0)=0, b'(0)=d, rho(0)=1, T(0)=A, eta(0)=2A/beta, satisfying

    T=A/rho^2, R=integral_0^y rho, rho b=dR,
    br'+(beta/2)r=A/rho, eta=r/rho=-b''-2v,
    G=integral_0^y rho I,
    rho^3 v=-A/beta+(A/8)(dRI-kappa G).                  (1)

All derivatives have polynomial bounds at both ends, b(y)/y tends to beta, and at positive infinity

    I(y)=L y^(-m)+O(y^(-1+1/beta)).                       (2)

Separate choices attain L>0 and L<0. At beta=2 every real finite limit of I can instead be prescribed while keeping the same A. Thus the critical power is compatible with (1) and b/y tending to beta, for either sign, including after the center normalization is fixed. This does not assert compatibility with all necessary conditions for a profile.

The theorem concerns four low-order axis relations. A polynomial transverse realization given below obeys exactly the stated coefficients and the divergence and curl identities, but violates full-plane sublinearity. It is not a B2 profile or an existence argument. No full-plane inverse is claimed for the manufactured fields. The complete B2 problem remains open.

## Smooth concave transport

Let theta(s)=exp(-1/s) for s>0 and zero otherwise, and define

    chi(y)=theta(y^2-1)/[theta(y^2-1)+theta(4-y^2)].

The denominator is positive everywhere. The function is smooth and even, equals zero on |y|<=1 and one on |y|>=2, and has chi'(y)>0 for 1<y<2. To see the last claim, on that interval write chi=u/(u+v), with u=theta(y^2-1) strictly increasing and v=theta(4-y^2) strictly decreasing. Then chi'=(u'v-uv')/(u+v)^2>0. Smoothness and flatness follow because each derivative of exp(-1/s) is that exponential times a polynomial in 1/s, tending to zero as s decreases to zero.

Define

    b(y)=integral_0^y [d+(beta-d)chi(s)] ds.                (3)

Then b is odd, b=dy near zero, beta<=b'<=d, and b>0 for y>0. On the positive axis b''=(beta-d)chi'<=0, strictly negative on (1,2). With

    y0=(d-beta)/beta integral_0^2 (1-chi)>0,

one has b=beta(y+y0) for y>=2. This proves b/y tends to beta at both ends, and b has no zero other than zero. The shift y0 is a consequence of integrating b'; it is not a fitted physical observer velocity.

Set rho=1 on [0,1], solve rho'/rho=(d-b')/b on (1,infinity), and extend rho evenly to the negative axis. It is smooth and positive. Since d-b'>=0 on the positive axis, rho>=1, with rho>1 for y>1. Differentiating b rho gives (b rho)'=d rho. Thus R=integral_0^y rho satisfies rho b=dR. On the positive tail, putting z=y+y0, the exact solutions are

    rho=C z^gamma,   R=(beta C/d) z^(gamma+1), C>0.        (4)

There is no missing additive constant in R: its formula is fixed by rho b=dR. The negative tail is controlled by the evenness of rho and oddness of R.

## Vorticity and quartic coefficient

Let alpha=beta/(2d)>0 and, for y>0, put

    r(y)=(A/d) R(y)^(-alpha) integral_0^y R(s)^(alpha-1) ds.
                                                                    (5)

The integral converges at zero, where R=y. There r=2A/beta exactly. Extending r evenly gives a globally smooth function. Differentiating (5) using R'/R=d/b and R'=rho proves br'+(beta/2)r=A/rho. Define eta=r/rho, v=-(b''+eta)/2 and T=A/rho^2. In particular v(0)=-A/beta. Direct differentiation gives the physical coefficient equations

    bT'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T.                              (6)

On the positive tail the scalar equation for r has the exact solution

    r=D z^(-1/2)-(A/C)z^(-gamma),       D/A>0.              (7)

Indeed differentiation of z^(1/2)r gives (A/(beta C))z^(-1-1/beta). The integration constant is

    D=z2^(1/2)r(2)+(A/C)z2^(-1/beta), z2=2+y0.

Both terms have the sign of A by (5). All fields constructed so far and all their derivatives have polynomial bounds.

Set G=0 on |y|<=1 and solve outside this interval

    bG'-kappa G=(8/A)(rho^3v+A/beta).                      (8)

The forcing vanishes on the inner interval, is flat at its endpoints, and b is nonzero on each outside half-line. The ordinary integrating factor therefore gives unique smooth global extensions there, matching the inner zero function. Put I=G'/rho. Equation (8), rho b=dR and G(0)=0 give the final two identities of (1). All functions have polynomially bounded derivatives on both tails: their coefficients there are powers of z, and on the negative tail the analogous statement follows with z=|y|+y0. No singular initial-value problem at b(0)=0 is used.

Substituting (4) and (7) into (8) gives the exact positive-tail formulas

    G=K z^(kappa/beta)+(4DC^2/A)z^(1/2+2/beta)
                         -2C z^gamma-8/(beta kappa),
    I=L z^(-m)+(4DC/A)(1/2+2/beta)z^(-1+1/beta)-2gamma/z,
    L=kappa K/(beta C).                                   (9)

The relevant eigenvalues of beta z d/dz-kappa are -1 for z^(1/2+2/beta), -2 for z^gamma and -kappa for a constant. These are nonzero for beta>=2. Formula (2) follows because z=y+y0, z^(-m)=y^(-m)+O(y^(-m-1)), and -m-1<-1+1/beta. At beta2 the leading exponent m=0 makes the shift error identically zero. None of these expansions requires an unproved differentiation of an asymptotic relation.

## Opposite signs of the homogeneous tail

The functions b,rho,R are independent of A, and (5) gives r=A r1, with r1>0 on the positive axis. Decompose

    G=Gb/A+Ge,
    bGb'-kappa Gb=-4rho^3 b'',
    bGe'-kappa Ge=-4rho^2 r1+8/beta,                       (10)

each with zero inner data. Let h=exp(integral_1^y kappa/b)>0 for y>0. Since h'/h=kappa/b, and b'' is compactly supported and strictly negative on (1,2),

    (Gb/h)'=-4rho^3 b''/(b h)>=0,
    lim_(y->infinity) Gb/h>0.                              (11)

The derivative vanishes after y=2. The strict limit follows by integrating the continuous, strictly positive integrand on any compact subinterval of (1,2). On the tail h=Ch z^(kappa/beta) with Ch>0. Consequently the coefficient Kb of z^(kappa/beta) in Gb is positive.

For the sign of Ge put u=rho^2 r1-2/beta. Differentiating with the equations already proved gives

    b u'=(2d-beta/2-2b')u+4(d-b')/beta+(rho-1).             (12)

Here u=0 on [0,1]; the final two terms are nonnegative and strictly positive for y>1. On each finite positive interval beyond1 the scalar integrating factor for (12) is positive. Its integral representation proves u(y)>0 for y>1. In (10) the forcing of Ge is exactly -4u. Hence

    (Ge/h)'=-4u/(b h)<0 for y>1.                           (13)

Its integral is finite at infinity. By (4) and (7), u=O(z^(1/2+2/beta)); dividing by b h gives O(z^(-1-1/beta)), an integrable power. Therefore Ge/h has a finite strictly negative limit. The coefficient Ke of z^(kappa/beta) in Ge is negative. This also follows directly from (9), since both other nonconstant powers there are smaller than kappa/beta.

Define Lb=kappa Kb/(beta C)>0 and Le=kappa Ke/(beta C)<0. Linearity now gives

    L=Lb/A+Le.                                             (14)

For a variable positive A this is positive for A<Lb/|Le| and negative for A>Lb/|Le|. Neither coefficient depends on A. The argument proves nonzero signs exactly; numerical quadrature is unnecessary for the sign theorem.

## Fixing A while choosing either sign

To obtain the theorem with every prescribed A>0, use the base transport and r1 above. For lambda>0 and w=y/lambda set

    b_lambda(y)=lambda b(w), rho_lambda(y)=rho(w),
    R_lambda(y)=lambda R(w), r_lambda(y)=A r1(w),
    eta_lambda(y)=A eta1(w),
    v_lambda(y)=-[lambda^(-1)b''(w)+A eta1(w)]/2,
    G_lambda(y)=Gb(w)/(A lambda)+Ge(w),
    I_lambda(y)=Ib(w)/(A lambda^2)+Ie(w)/lambda,            (15)

where eta1=r1/rho, Ib=Gb'/rho and Ie=Ge'/rho. Substitution into (1) verifies all identities and retains T_lambda(0)=A, b_lambda'(0)=d, eta_lambda(0)=2A/beta, v_lambda(0)=-A/beta. In particular the derivative factor in I_lambda must not be omitted. Its leading coefficient is

    L_lambda=lambda^(m-1)[Lb/(A lambda)+Le].                (16)

The prefactor is positive. For lambda<Lb/(A|Le|) the coefficient is positive, and for lambda>Lb/(A|Le|) it is negative. The tail begins at y=2lambda and uses y+lambda y0 in the exact formulas. This dilation of axis data is not claimed to be the physical spatial scaling of full B2 profiles.

When beta=2, d=kappa. Adding I0 R_lambda to G_lambda solves the same equation (8) because b_lambda R_lambda'=dR_lambda. It adds I0 to I_lambda while changing none of b,rho,r,eta,v,T. Thus any chosen finite limiting value of I is obtained. No additional smoothness condition is lost at zero, where the new G is I0 y.

## Physical realization and explicit obstruction

Define Q4=A^2 I/rho^4 and polynomial fields

    Theta=T(y)x^2/2+Q4(y)x^4/24,
    W2=b(y)+v(y)x^2,
    W1=(2beta-b'(y))x-v'(y)x^3/3,
    Omega=partial_y W1-partial_x W2
         =eta(y)x-v''(y)x^3/3.                             (17)

They obey the x parities, W(0)=0 and div W=2beta. The center jet has a0=A/2 and Omega_x(0)=2A/beta=4a0/beta. The two equations in (6) are the x^2 thermal and x vorticity coefficients. The x^4 thermal coefficient, multiplied by24, is

    bQ4'+(7beta+2-4b')Q4-8v'T+12vT'.

After substituting T=A/rho^2, its vanishing is equivalent to

    bI'+(beta-2)I=8(rho^3v)'/(A rho).

This follows by differentiating the final identity of (1), since d-kappa=beta-2. Thus the claimed coefficient relations hold exactly. Higher transverse equations are not imposed. On y=0 the second component is W2(x,0)=-A x^2/beta, so W-beta X is not o(|X|). A constant center velocity cannot remove the quadratic term. These data therefore do not give a B2 profile even though their prescribed low-order identities and tail conditions hold globally on the axis.

## Dependencies and evidence

This proof independently checks the lead's concave-transport variant in ../analysis/work/z446/NOTES.md and includes the fixed-A extension, using the corrected dilation from P264. All needed identities and sign arguments are given here. They require only smooth flat cutoffs, positive integrating factors, elementary power integrals and explicit coefficient calculation. No numerical result is a premise. The complete informal proof precedes the new controls and review request. Scripts, frozen inputs, hashes, actual UTC times and any public review will be kept in verification/. No Lean or Lake build is run.
