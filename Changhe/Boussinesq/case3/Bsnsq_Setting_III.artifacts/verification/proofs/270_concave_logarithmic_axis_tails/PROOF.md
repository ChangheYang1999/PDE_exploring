# Both signs of logarithmically enhanced critical axis tails

## Statement and precise scope

Fix beta>2, ell>0 and a prescribed A>0. Put d=(3beta+2)/2, kappa=(beta+6)/2, gamma=1/2+1/beta and m=1-2/beta>0. For either prescribed sign sigma there are globally smooth real axis functions b,rho,R,r,eta,v,T,G,I satisfying

    rho>0, rho=1 near0, R=integral_0^y rho, rho b=dR,
    T=A/rho^2, br'+(beta/2)r=A/rho, eta=r/rho=-b''-2v,
    G=integral_0^y rho I,
    rho^3v=-A/beta+(A/8)(dRI-kappa G).                    (1)

They have b(0)=0, b'(0)=d, eta(0)=2A/beta and polynomial bounds on all derivatives at both ends. Moreover b'>=beta, b''<=0 on the positive axis, b(y)/y tends to beta, and

    I(y)=L y^(-m)(log y)^ell (1+o(1)), sigma L>0,         (2)

at positive infinity. In particular the critical quantity y^m I may diverge with either sign even for concave transport and fixed center amplitude. The parameter ell is arbitrary. The low-order identities alone therefore do not exclude either sign of a logarithmically enhanced critical tail for beta>2.

This is an axis-data theorem. It is not a B2 profile, not a full-plane inverse construction, and not a claim that all higher transverse equations can be satisfied. The polynomial fields at the end explicitly violate sublinearity. The axis velocity defect in this particular construction is of order y/log y, so it also does not obey the stronger class-A axis velocity estimate O(y^(1-1/beta)). The theorem uses only the broad axis condition b/y tending to beta, and must not be substituted for that stronger class. General B2 is OPEN. No endpoint is reached.

## Smooth concave transport with a logarithmic correction

Let theta(s)=exp(-1/s) for s>0 and zero otherwise, and set

    zeta(s)=theta(s)/[theta(s)+theta(1-s)],
    F(t)=integral_0^t zeta(s) ds.

The denominator is positive everywhere. The function zeta is smooth, zero for s<=0, one for s>=1, and strictly positive for s>0. The exponential and all its derivatives vanish at0 from the right, which proves smoothness at the junctions. Thus F=0 for t<=0, F'>=0, and F=t-c0 for t>=1, where c0=1-integral_0^1 zeta lies in(0,1).

Put a=ell/m>0 and mu=(d-beta)/(beta a)>0. For y!=0 define the even smooth derivative

    b'(y)=beta+(d-beta)/[1+mu F(log|y|)],
    b(0)=0,

and obtain b by integration from0. This definition is constant b'=d for |y|<=1, so it extends smoothly over zero, and b is odd. The denominator is at least1. Therefore beta<=b'<=d, b=dy on |y|<=1 and b>0 on y>0. For y>1,

    b''(y)=-(d-beta) mu zeta(log y)
                         /[y(1+mu F(log y))^2]<0.          (3)

The second derivative b'' vanishes for |y|<=1 and is flat at both1 and-1. Oddness of b gives b''>0 for y<-1. Define c=1/mu-c0. On y>=e, with t=log y, the exact derivative is

    b'=beta+beta a/(t+c),
    b''=-beta a/[y(t+c)^2].                               (4)

The denominator t+c is positive on this tail because it equals (1+mu F(t))/mu. Integration gives

    b(y)=beta y[1+a/t+O(t^(-2))].                          (5)

For completeness, put H(y)=y/(log y+c). Its derivative is1/(log y+c)-1/(log y+c)^2. Thus integrating1/(log y+c) differs from H by an integral of1/(log y+c)^2 and a fixed constant. For large y, splitting at sqrt(y) bounds this remainder by O(sqrt(y))+O(y/(log y)^2)=O(y/(log y)^2). Expanding1/(t+c)=1/t+O(t^-2) proves(5). In particular b/y tends to beta at both ends, and b-beta y is asymptotic to beta a y/log y at the positive end. All derivatives of b are polynomially bounded, directly from(4), smoothness on compact sets and oddness.

## Density and its powers

Set rho=1 on[0,1], solve rho'/rho=(d-b')/b beyond1 and extend rho evenly. The coefficient is smooth, flat at1, and b>0 there. This gives a smooth positive function on the real line. Since d-b'>=0, rho is nondecreasing on y>0 and is strictly greater than1 for y>1. Differentiating gives(rho b)'=d rho. Because b(0)=0, R=integral_0^y rho satisfies rho b=dR. In particular R>0 for y>0 and R'/R=d/b.

Write B(t)=b(e^t)/e^t. Equation(5) gives

    d(log R)/dt=d/B=(d/beta)[1-a/t+O(t^-2)].

The remainder has a convergent integral with tail O(1/t). Consequently there exists C_R>0 with

    R=C_R y^(d/beta) t^(-d a/beta)(1+O(1/t)),
    rho=C y^gamma t^(-d a/beta)(1+O(1/t)), C=d C_R/beta.   (6)

No derivative of a limiting equivalence is used. Set h=exp(integral_1^y kappa/b)>0. Its exact relation to R is

    h=C_h R^(kappa/d), C_h>0.                              (7)

With P=rho^3/(b h), exact elimination of rho gives

    P=(d^3/C_h) R^(4beta/d)/b^4
     =P0 t^(-4a)(1+O(1/t)),
    P0=d^3 C_R^(4beta/d)/(C_h beta^4)>0,                  (8)

where3d-kappa=4beta. These formulas establish all required power bounds for rho, its inverse and h. Their derivatives have polynomial bounds by their scalar equations and(4).

## Vorticity and the quartic identity

Let alpha=beta/(2d)>0. For y>0 define

    r=(A/d) R^(-alpha) integral_0^y R(s)^(alpha-1) ds,

and extend r evenly. Near0, R=y and this gives r=2A/beta exactly. Its derivative, using R'=rho and R'/R=d/b, proves br'+beta r/2=A/rho. The integral at infinity converges: its integrand has y power(alpha-1)d/beta=-1-1/beta<-1, multiplied by a fixed power of log y. It is strictly positive and has a finite positive limiting value. Thus, writing r=A r1,

    r1=D1 y^(-1/2) t^(a/2)(1+o(1)), D1>0.                 (9)

Define eta=r/rho, v=-(b''+eta)/2 and T=A/rho^2. They are smooth and have v(0)=-A/beta. To make the endpoint matching explicit, r-2A/beta solves a regular scalar equation at y=1 with zero inner data and a forcing proportional to1/rho-1, flat at1. All its derivatives therefore match the zero inner values. Direct differentiation gives the second-order thermal and first-order vorticity identities

    bT'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T.                              (10)

Let G=0 on|y|<=1 and solve the regular scalar equation

    bG'-kappa G=(8/A)(rho^3v+A/beta)                      (11)

on each outside half-line. Its forcing vanishes and is flat at the inner endpoints, and b has no zero on either outside half-line. It therefore has unique smooth extensions from the zero inner data. Define I=G'/rho. Then G(0)=0 and rho b=dR imply every identity of(1). All derivatives remain polynomially bounded on both tails, by the scalar equations with b comparable to|y|, polynomial forcing and power-bounded integrating factors. This existence argument does not presume the desired sign or asymptotic.

## Backward-axis normalization

For the axis flow dY/ds=b(Y), Y(0)=y, the bounds beta<=b'<=d give global existence for negative s and convergence Y(s)->0 as s->-infinity. For y>0 this follows from beta Y<=b(Y)<=dY, and for y<0 from odd reflection. Variation of constants in the r equation along the orbit gives, for s0<0,

    r(y)=exp(beta s0/2)r(Y(s0))
       +A integral_{s0}^0 exp(beta s/2)/rho(Y(s)) ds.

The first term tends to0 because r is bounded near0. Since rho>=1 and A>0, the integral converges absolutely and yields

    r(y)=A integral_{-infinity}^0 exp(beta s/2)/rho(Y(s)) ds,
    0<r(y)<=2A/beta.

After the fixed-A dilation below, the derivative bounds for b_lambda and rho_lambda>=1 still hold, so this argument also applies there. The finite-point tail argument used for(9) does not require this representation; it additionally verifies the stronger backward-axis normalization in the report's definition of axis data.

## Strict signs of the limiting coefficients

The functions b,rho,R and r1 do not depend on A. Split G=Gb/A+Ge, with both summands zero near0 and

    bGb'-kappa Gb=-4rho^3 b'',
    bGe'-kappa Ge=-4u, u=rho^2 r1-2/beta.                 (12)

The first equation gives

    (Gb/h)'=-4P b''.

It is positive for y>1. Its integral converges: on the tail, equations(4) and(8) bound it by C/[y t^(4a+2)], whose integral is finite for a>0. Thus Gb/h tends to a finite positive number Kb.

For the second equation, differentiate u directly with the rho and r1 equations. The result is

    b u'=(2d-beta/2-2b')u+4(d-b')/beta+rho-1.             (13)

Here u=0 on[0,1], and the final two terms are positive for y>1. The positive scalar integrating factor shows u>0 for y>1, regardless of the sign of the coefficient of u. Consequently(Ge/h)'=-4u/(b h)<0. From(6),(7),(9),

    u/(b h)=O(y^(-1-1/beta) t^((-2+1/beta)a)).            (14)

The subtracted constant in u contributes the faster term1/(bh); it can be included in this bound since the positive power rho^2r1 grows. The y power in(14) is integrable, independently of its logarithm. Therefore Ge/h tends to a finite negative number Ke. These strict signs are analytic consequences of positive integrals, not numerical estimates.

Set Jb=Gb/h and Je=Ge/h. Besides their convergence, their exact equations give, in t=log y,

    dot Jb=O(t^(-4a-2)) ->0,
    dot Je=O(y^(-1/beta) t^((-2+1/beta)a)) ->0.           (15)

Let J=G/h=Jb/A+Je. If K=Kb/A+Ke is nonzero, then J->K and dot J->0. Differentiating G=hJ exactly yields

    I=h/(b rho)[B dot J+kappa J]
     =(C_h/d) R^(kappa/d-1)[B dot J+kappa J].             (16)

By(6), kappa-d=-(beta-2), and therefore

    R^(kappa/d-1)
      =C_R^(kappa/d-1) y^(-m) t^(ma)(1+O(1/t)).          (17)

Equations(15)-(17) prove(2), with

    L=L_b/A+L_e,
    L_b=(kappa C_h/d) C_R^(kappa/d-1) Kb>0,
    L_e=(kappa C_h/d) C_R^(kappa/d-1) Ke<0,
    ell=ma.

At variable A>0 both signs follow by choosing A on opposite sides of L_b/|L_e|. This already proves the theorem without fixed-amplitude normalization.

## Choosing the sign at prescribed A

For the fixed A in the statement choose lambda>0. Starting with b,rho,R,r1,Gb,Ge independent of A, define w=y/lambda and

    b_lambda=lambda b(w), rho_lambda=rho(w),
    R_lambda=lambda R(w), r_lambda=A r1(w),
    eta_lambda=A r1(w)/rho(w),
    v_lambda=-[lambda^(-1)b''(w)+eta_lambda]/2,
    G_lambda=Gb(w)/(A lambda)+Ge(w),
    I_lambda=Ib(w)/(A lambda^2)+Ie(w)/lambda,

where Ib=Gb'/rho and Ie=Ge'/rho. Substitution verifies(1), with the same center A, b_lambda'(0)=d and v_lambda(0)=-A/beta. The inequalities b_lambda'>=beta and b_lambda''<=0 on y>0 are preserved. The derivative factor in I_lambda is essential.

Each Ib and Ie has the asymptotic already proved separately, with coefficients L_b and L_e. For fixed lambda, log(y/lambda)/log y tends to1. Hence

    L_lambda=lambda^(m-1)[L_b/(A lambda)+L_e].            (18)

The positive prefactor does not affect the sign. Choosing lambda<L_b/(A|L_e|) gives L_lambda>0 and choosing lambda>L_b/(A|L_e|) gives L_lambda<0. The prescribed ell and A are unchanged. This is a dilation of axis data, not the physical scaling symmetry of full B2 profiles.

## Physical coefficient check and explicit failure of sublinearity

The defining equations whose coefficients are checked here are W.grad Theta=(beta-2)Theta and W.grad Omega+Omega=Theta_x, with div W=2beta and Omega=partial_y W1-partial_x W2. Put Q4=A^2I/rho^4 and define

    Theta=T(y)x^2/2+Q4(y)x^4/24,
    W2=b(y)+v(y)x^2,
    W1=(2beta-b'(y))x-v'(y)x^3/3,
    Omega=partial_y W1-partial_x W2
         =eta(y)x-v''(y)x^3/3.

These have the required x parities, div W=2beta, W(0)=0, Theta(0,y)=0 and center coefficient a0=A/2. Their x^2 thermal and x vorticity equations are exactly(10). The x^4 thermal coefficient, multiplied by24, is

    bQ4'+(7beta+2-4b')Q4-8v'T+12vT'.

On substituting T=A/rho^2 it becomes A^2/rho^4 times

    bI'+(beta-2)I-8(rho^3v)'/(A rho),

which is zero by differentiating(1) and using d-kappa=beta-2. No higher coefficient has been imposed. On y=0, W2(x,0)=-Ax^2/beta, so W-beta X is not o(|X|). This alone prevents a full-profile interpretation. Moreover(5) shows the failure of the stronger class-A axis growth estimate even before making a transverse extension. Neither statement is repaired by a constant velocity gauge.

## Dependencies and verification status

This proof uses flat cutoffs, exact scalar integrating factors, finite differentiation and explicitly bounded improper integrals. Every asymptotic derivative used is obtained from an exact differential equation. No numerical result is a premise. P268 motivates the concave decomposition and fixed-A dilation, both rederived here. The complete informal argument is written before new exact controls and an actual Opus5.5 audit request. All evidence and any review limitation will be recorded in verification. No Lean or Lake build is run.
