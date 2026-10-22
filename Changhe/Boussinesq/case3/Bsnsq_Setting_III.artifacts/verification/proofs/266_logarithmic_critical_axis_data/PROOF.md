# Logarithmically enhanced critical tails in the low-order axis system

## Statement and exact scope

Fix beta>=2, A!=0 and ell>0. Put

    d=(3beta+2)/2, kappa=(beta+6)/2, m=1-2/beta,
    a=sqrt(ell/(2-m/2)), p=2a^2, c2=-A/beta.

There exist smooth real functions b,rho,R,r,eta,v,T,G,I on the whole real line with rho>0, T=A/rho^2, b(0)=0, b'(0)=d, T(0)=A, eta(0)=2A/beta, and

    R(y)=integral_0^y rho,       G(y)=integral_0^y rho I,
    rho b=dR,                  b r'+(beta/2)r=A/rho,
    eta=r/rho=-b''-2v,
    rho^3 v=c2+(A/8)(dRI-kappa G).                              (1)

All these functions and their derivatives have polynomial growth bounds at both ends; b(y)/y tends to beta. At the positive end,

    I(y)=L y^(-m)(log y)^ell (1+o(1)),
    L=-8 kappa d^2 C_R^2/(A beta^3),                            (2)

where C_R is a positive finite constant defined below. In particular A L<0. At beta2, m=0 and I diverges with sign opposite A, more slowly than every positive power. At beta>2, I tends to zero but y^m I diverges with sign opposite A. Any prescribed positive logarithmic exponent ell is attained by the displayed choice of a.

This is a construction for four low-order axis identities, not a B2 profile. It does not impose the full transverse PDE, a canonical full-plane inverse or the full-plane sublinearity condition. Its polynomial transverse realization given below violates sublinearity. It makes no assertion that the tail in (2) is attainable by a full profile or compatible with every other necessary condition already proved. Consequently it is neither a YES nor a NO endpoint. The result shows why those four identities and b/y tending to beta alone do not exclude logarithmically enhanced critical tails. It is compatible with P263, which excludes only s>-m.

## A globally smooth oscillating transport

Let theta(s)=exp(-1/s) for s>0 and zero otherwise. Define the two smooth cutoffs

    chi(y)=theta(y^2-1)/[theta(y^2-1)+theta(4-y^2)],
    zeta(s)=theta(s)/[theta(s)+theta(1-s)].

Their denominators are everywhere positive. The first is even, zero on |y|<=1, and one on |y|>=2; the second is zero on s<=0 and one on s>=1. Smoothness and flatness at the endpoints follow by repeated differentiation of exp(-1/s): each derivative is a polynomial in 1/s times exp(-1/s) and tends to zero as s decreases to zero.

Choose t0>max(2,16a^2). Define epsilon(t)=0 for t<=t0 and

    epsilon(t)=a zeta(t-t0) sin(t)/sqrt(t)       for t>t0.

It is smooth at t0 because zeta is flat there; |epsilon|<1/4. Define

    b_base(y)=y[d+(beta-d)chi(y)],
    b(y)=b_base(y)[1+epsilon(log|y|)]       for y!=0,
    b(0)=0.                                                    (3)

The perturbation vanishes near zero. Thus b is globally smooth and odd, b=dy on |y|<=1, and b>0 on y>0 because the bracket in b_base lies between beta and d. It has no zero other than zero. On y>=exp(t0+1), with t=log y,

    b(y)=beta y[1+epsilon(t)],
    epsilon(t)=a t^(-1/2) sin t.                                (4)

It follows that b/y tends to beta at both ends. Its derivatives have polynomial bounds: each derivative in y of a tail factor differentiates its function of log|y| and contributes a factor 1/y, and each derivative in t of epsilon is O(t^(-1/2)). No monotonicity of b, b' or rho is assumed.

## Density and exact logarithmic asymptotics

Set rho=1 on [0,1]. For y>1 solve

    rho'/rho=(d-b')/b,       rho(1)=1,

and extend evenly to y<0. This is smooth and positive, is constant near zero, and satisfies the equation everywhere away from zero. Since (rho b)'=d rho and rho(0)b(0)=0, its integral R satisfies R=rho b/d. In particular R>0 for y>0. On the positive tail,

    d(log R)/dt=d/[beta(1+epsilon(t))].                         (5)

The following integral asymptotic has an actual convergent remainder:

    integral^t (1+epsilon(s))^(-1) ds
       =t+(a^2/2)log t+C+o(1).                                (6)

Indeed, for the tail where epsilon=a sin t/sqrt(t), the exact expansion is

    1/(1+epsilon)=1-epsilon+epsilon^2-epsilon^3/(1+epsilon).

The integral of epsilon converges by integration by parts, since t^(-1/2) tends to zero and its derivative is integrable. The square equals a^2[1-cos(2t)]/(2t); its nonconstant integral converges by the same argument. The cubic remainder is absolutely integrable since |epsilon|<1/4 and |epsilon|^3=O(t^(-3/2)). The compact transition changes only the constant C. Integrating (5) and exponentiating (6) therefore gives a finite positive constant C_R with

    R=C_R y^(d/beta) t^(d a^2/(2beta))(1+o(1)),
    rho=dR/[beta y(1+epsilon)].                                (7)

The factor 1+o(1) has a limiting value one; no derivative of an asymptotic equivalence is used later.

## The remaining smooth axis fields

Put alpha_r=beta/(2d)>0. For y>0 define

    r(y)=(A/d) R(y)^(-alpha_r)
                    integral_0^y R(s)^(alpha_r-1) ds.          (8)

Near zero R(y)=y, so the integral is finite and r=2A/beta exactly. Extend r evenly to all y. Differentiation, using R'/R=d/b and rho=dR/b, gives the r equation in (1). Let

    eta=r/rho,       v=-(b''+eta)/2,       T=A/rho^2.

They are smooth, T never vanishes, eta(0)=2A/beta and v(0)=c2. The first two nontrivial axis coefficient equations are

    bT'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T.                                   (9)

They follow by differentiation of these definitions.

Prescribe G=0 on |y|<=1, and solve on each outside half-line the regular linear equation

    bG'-kappa G=(8/A)(rho^3 v-c2).                              (10)

The forcing vanishes on the inner interval and is flat at its endpoints. As b is nonzero at those endpoints and on the outside intervals, the two solutions extend smoothly and exist on the whole half-lines. Set I=G'/rho. Then G(0)=0 gives its asserted integral representation, and rho b=dR makes (10) precisely the final identity of (1). Thus every identity has been imposed exactly. No singular initial-value theorem at b(0)=0 is needed.

For later estimates, the integral in (8) converges at positive infinity. Its power in y from (7) is

    (d/beta)(alpha_r-1)=-1-1/beta<-1,

with a fixed logarithmic power, which does not affect convergence. Hence

    r=O(y^(-1/2) t^(-a^2/4)),
    eta=O(y^(-1-1/beta) t^(-a^2(1+1/(2beta)))).                (11)

The second formula uses rho from (7) and the bounded factor 1+epsilon. On the negative side the even extensions give the same estimates for r and rho. Every derivative of these functions has polynomial growth bounds: differentiate their regular scalar equations on the tails, where b is bounded below by a positive multiple of |y| and derivatives of b have polynomial bounds. The inverse rho also has polynomial bounds by (7). The forcing of (10), divided by b, has polynomially bounded derivatives, and its integrating factor has polynomial growth and decay because kappa/b=O(1/|y|). The integral representation for (10) thus bounds G and its derivatives polynomially at both ends, and the same follows for I. These bounds do not presume (2).

## Exact dissipative identity and its weight

For y>0 put h=exp(integral_1^y kappa/b)>0. Equations R'/R=d/b and h'/h=kappa/b imply

    h=C_h R^(kappa/d),       C_h>0.

Define

    P=rho^3/(b h)>0, H=A G/h, E=b'-beta,
    f=eta+2c2/rho^3, Q=H+4PE.                                  (12)

Direct logarithmic differentiation, using rho'/rho=(d-b')/b and 3d-kappa=4beta, gives

    bP'=-4PE.

Equation (10) says 2v=2c2/rho^3+H'/(4P). Substituting eta=-b''-2v, and E'=b'', gives

    H'=-4P(E'+f),
    Q'=-16PE^2/b-4Pf.                                         (13)

These are exact identities, not inequalities. On the tail in (4), write B=b/y=beta(1+epsilon) and use a dot for d/dt. They become

    Hdot=-4P(Edot+yf),
    Qdot=-16PE^2/B-4Pyf.                                      (14)

The weight can be expressed without derivatives:

    P=(d^3/C_h) R^(3-kappa/d)/b^4,
    3-kappa/d=4beta/d.

Using (7) and b=beta y(1+epsilon), the powers of y cancel exactly. Thus

    P=P0 t^p(1+o(1)), p=2a^2>0,
    P0=d^3 C_R^(4beta/d)/(C_h beta^4)>0.                        (15)

In particular P has at most a fixed logarithmic growth. By (7) and (11), yf is bounded by an exponentially decreasing function of t times a fixed power of t. Therefore integral^infinity |P y f| dt is finite. This is an absolute-integrability statement, not a cancellation assertion.

## The accumulated square term

From b=beta y(1+epsilon), with epsilon as in (4), direct differentiation gives

    E=beta(epsilon+epsilon_dot)
      =beta a t^(-1/2)(sin t+cos t)+O(t^(-3/2)),
    Edot=beta a t^(-1/2)(cos t-sin t)+O(t^(-3/2)),
    E^2=beta^2 a^2 t^(-1)(1+sin(2t))+O(t^(-2)).                (16)

Combining (15), (16) and B=beta(1+epsilon) gives

    16PE^2/B
       =16beta a^2 P0 t^(p-1)(1+sin(2t))(1+o(1))
         +O(t^(p-2)).                                         (17)

For every p>0,

    integral^t s^(p-1)(1+sin(2s)) ds=t^p/p+o(t^p).              (18)

The constant term integrates exactly. One integration by parts bounds the oscillatory integral by O(1+t^max(p-1,0)), hence by o(t^p). The extra multiplicative o(1) in (17) also integrates to o(t^p): the weight s^(p-1)(1+sin(2s)) is nonnegative, so split the integral at a fixed large time where its relative error is uniformly small and then let that small bound decrease to zero. The additive O(s^(p-2)) integrates to O(1+t^max(p-1,0)+log t), also o(t^p). No monotonicity of P or E is required.

Integration of (14), using the absolute-integrability of Pyf, now yields

    Q=-(16beta a^2 P0/p)t^p+o(t^p)
      =-8beta P0 t^p(1+o(1)).                                 (19)

Since PE=O(t^(p-1/2))=o(t^p), H=Q-4PE has the same leading term. Also the first identity in (14) and (16) give Hdot=O(t^(p-1/2))+o(1)=o(t^p). This derivative estimate comes from the exact equation; it is not obtained by differentiating (19).

## Extraction of the critical logarithmic tail

Differentiating G=hH/A exactly and dividing by rho gives

    I=h/(A b rho)[B Hdot+kappa H]
      =C_h/(A d) R^(kappa/d-1)[B Hdot+kappa H].                 (20)

Here B tends to beta, Hdot=o(t^p), and H has the negative leading coefficient in (19). From (7),

    R^(kappa/d-1)
      =C_R^((kappa-d)/d) y^(-m) t^(-m a^2/2)(1+o(1)).           (21)

Equations (19)-(21) give exponent

    ell=p-m a^2/2=a^2(2-m/2)>0,

and leading coefficient

    L=-8beta kappa C_h P0 C_R^((kappa-d)/d)/(A d)
      =-8kappa d^2 C_R^2/(A beta^3).                            (22)

The last equality uses (15) and 4beta+kappa-d=2d. Its factors except A are positive. This proves (2). At beta2, d=kappa=4 and m=0, so ell=2a^2 and L=-64C_R^2/A. At beta>2, m>0, so the power y^(-m) dominates every fixed logarithmic power and I tends to zero, while y^m I has the asserted divergence. For any s>-m, y^(-s)|I| tends to zero, in agreement with the P263 theorem.

## Relation to the physical coefficients and failure of a full profile

Let Q4=A^2 I/rho^4 and define smooth polynomial fields

    Theta=T(y)x^2/2+Q4(y)x^4/24,
    W2=b(y)+v(y)x^2,
    W1=(2beta-b'(y))x-v'(y)x^3/3,
    Omega=partial_y W1-partial_x W2
         =eta(y)x-v''(y)x^3/3.

Their parities in x, div W=2beta and curl equation hold exactly; W(0)=0 and Theta has coefficient A/2 at x^2. Equation (9) gives the x^2 thermal and x vorticity coefficients. The x^4 thermal coefficient, multiplied by24, is

    bQ4'+(7beta+2-4b')Q4-8v'T+12vT'.

Using T=A/rho^2, its vanishing is equivalent to

    bI'+(beta-2)I=8(rho^3 v)'/(A rho),

which follows by differentiating the last identity of (1), since d-kappa=beta-2. This verifies precisely the coefficients claimed.

All higher residual coefficients remain unconstrained. Moreover, on y=0, v(0)=-A/beta is nonzero and b(0)=0, so W2(x,0)=-A x^2/beta. It follows directly that W-beta X is not o(|X|) along this line. A uniform observer velocity cannot remove a quadratic term. No canonical inverse of these polynomial fields is claimed. This concrete violation prevents any reading of the construction as a full B2 candidate.

## Dependencies and verification plan

Only smooth flat cutoffs, exact scalar integrating factors, elementary improper-integral bounds and integration by parts are used. The energy identity is rederived above; P263 and P264 supply context but are not unproved steps. This complete informal proof is written before new verification code or review requests. Independent symbolic controls will check all algebraic identities, logarithmic powers and coefficient normalization. Any finite quadrature will be labeled diagnostic. No Lean or Lake build is permitted or claimed.
