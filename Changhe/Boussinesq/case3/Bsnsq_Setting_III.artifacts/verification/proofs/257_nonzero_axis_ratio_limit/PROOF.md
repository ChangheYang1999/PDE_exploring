# No nonzero finite fourth-order axis-ratio limit at an infinite end

## Statement, notation and scope

Let beta>2. Let smooth real fields W=(W1,W2), Theta, Omega on the whole plane satisfy

    div W=2 beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly at infinity,
    W.grad Theta=(beta-2)Theta, W.grad Omega+Omega=Theta_x.

Assume W1 and Omega odd in x, W2 and Theta even in x, Theta(0,y)=0, and Theta=a0 x^2+O(|X|^3) at0 for a0!=0. Set T(y)=Theta_xx(0,y), A=T(0)=2a0, let J=(y_-,y_+) be the component of {T!=0} containing0, and define

    I(y)=Theta_xxxx(0,y)/T(y)^2, y in J.

At any infinite end of J, I cannot tend to a finite nonzero limit. No sign of A, no condition on the other end, no convergence of I3, and no derivative bounds at infinity are required. This is a necessary condition on actual B2 profiles, whose canonical moving-center velocity gives these divergence, curl and sublinearity conditions. It is not a whole-class exclusion. Bounded J and varying I, including I tending to0 or having no limit, remain unexcluded.

If I is constant near an infinite end, that constant is0. In particular no representation Theta(x,y)=H(x/sigma(y)), with sigma>0 and H''(0)H''''(0)!=0, can hold near an axis half-ray in J tending to that end. If I is constant on unbounded J then I=0 and the independently proved P242 theorem implies I3=Theta_xxxxxx/T^3 is nonconstant on J. Only this last statement depends on P242; the theorem and first two corollaries have the complete elementary proof below.

This proof is written before symbolic controls. It audits the lead's z444 claim independently. We retain A of either sign. Reflecting y reverses both the end and A and does not, by itself, justify arranging a positive infinite end and A>0 simultaneously. Retaining A avoids that normalization gap in the draft.

## 1. Axis transport, component geometry and growth

Parity and divergence give w(y)=partial_x W1(0,y)=2beta-b'(y), where b(y)=W2(0,y). The x^2 coefficient of thermal transport is

    b T'+2wT=(beta-2)T,
    b T'+(3beta+2-2b')T=0.                    (1)

At0, b=0 and T=A!=0, so b'(0)=d=(3beta+2)/2>0 and w(0)=alpha=(beta-2)/2. On J the sign of T equals the sign of A, so

    rho=(A/T)^(1/2)>0, rho(0)=1,
    R(y)=integral_0^y rho(s)ds

are well defined and smooth. Equation(1) is exactly (rho b)'=d rho; thus

    b=d R/rho.                               (2)

Consequently b has the sign of y and its only zero in J is0. The backward orbit of y'=b(y) through any point of J remains between that point and0. Smooth scalar ODE existence extends it to all negative times since that segment is a compact subset of J. Its limit as time tends to minus infinity must be the only equilibrium0. This argument uses no condition outside J.

Suppose first that y_+=infinity. Along the positive axis, sublinearity gives b(y)/y->beta. From R'=rho and(2),

    y R'/R=d y/b -> d/beta=3/2+1/beta.

For every epsilon>0, integrating the corresponding logarithmic-derivative upper and lower bounds from a sufficiently large fixed y0 gives positive constants such that R is bounded below and above by those constants times y^(d/beta-epsilon) and y^(d/beta+epsilon). Dividing by b/d, which is comparable to y, yields, with gamma=1/2+1/beta,

    c y^(gamma-epsilon)<=rho(y)<=C y^(gamma+epsilon). (3)

No derivative of b(y)/y->beta was taken. In particular rho tends to infinity for epsilon<gamma. Since rho is positive and continuous on[0,infinity), its global minimum m_rho there is strictly positive.

## 2. The first vorticity coefficient is controlled without a sign normalization

Write eta(y)=Omega_x(0,y). The x coefficient of the vorticity equation gives

    b eta'+(2beta+1-b')eta=T.

For r=rho eta, equations(1)-(2) give exactly

    b r'+(beta/2)r=A/rho.                     (4)

Let y(s), s<=0, be the backward axis orbit ending at y. Integrating(4) after multiplication by exp(beta s/2), the lower endpoint term tends to0 because r is bounded on the compact orbit segment. Therefore

    r(y)=A integral_{-infinity}^0 exp(beta s/2)/rho(y(s)) ds. (5)

In particular r has the sign of A. On the positive half of J,

    |r(y)|<=2|A|/(beta m_rho),
    |eta(y)|<=C/rho(y)<=C' y^(-gamma+epsilon). (6)

These bounds remain valid for negative A. At0, eta(0)=2A/beta is consistent with the local jet in the task specification.

## 3. Exact fourth-order thermal identity

All expansions below are finite smooth Taylor expansions, locally on compact subintervals of J, with remainders smoothly divisible by the displayed powers. Put Q(y)=Theta_xxxx(0,y), and write

    W2=b+v x^2+O(x^4),
    W1=w x-v' x^3/3+O(x^5),
    Theta=T x^2/2+Q x^4/24+O(x^6).

The expression for W1 follows from divergence and odd parity. The x coefficient of the negative curl relation is

    eta=-b''-2v.                              (7)

The x^4 coefficient of thermal transport is

    4w Q-8T v'+b Q'+12v T'=(beta-2)Q.        (8)

Using T=A/rho^2, Q=A^2 I/rho^4, b=d R/rho and w-b rho'/rho=alpha, equation(8) becomes

    (rho^3 v)'=(A/8)[(beta-2)rho I+d R I'].

Integrating from0 and using R'=rho gives the exact identity

    rho^3 v=c2+(A/8)[d R I-h integral_0^y rho I],
    h=(beta+6)/2, c2=v(0).                   (9)

No constancy or convergence of I has yet been used. In particular no derivative of I is estimated at infinity; its derivative has been integrated exactly.

## 4. A nonzero finite limit forces superlinear axis drift

Suppose I(y)->L with 0<|L|<infinity. Since R->infinity and rho>0, its weighted average obeys

    integral_0^y rho I=L R+o(R).

Indeed split the integral at a fixed Y beyond which |I-L|<delta. The finite initial integral divided by R tends to0 and the remaining quotient is at most delta. Then let delta tend to0. Also R I=L R+o(R). Equation(9), d-h=beta-2 and alpha=(beta-2)/2 give

    v=(A alpha L/4)(R/rho^3)(1+o(1)).        (10)

Choose epsilon>0 such that 3epsilon<gamma-2/beta=(beta-2)/(2beta). This implies p=2/beta+2epsilon<1. From(2)-(3),

    R/rho^3=b/(d rho^2)>=c y^(-p),
    |eta|<=C y^(-gamma+epsilon)=o(y^(-p)).   (11)

Let sigma=sign(A L), so sigma is either1 or-1. Since alpha>0, equations(7),(10)-(11) imply for all sufficiently large y,

    sigma b''(y)<=-c1 y^(-p), c1>0.         (12)

This is a one-sided bound of a fixed sign; oscillatory integration cannot cancel it. Twice integrating from a fixed Y gives

    sigma b(y)<=sigma b(Y)+sigma b'(Y)(y-Y)
                  -c1 integral_Y^y (y-t)t^(-p)dt.

The last integral is y^(2-p)/[(1-p)(2-p)]+O(y). Since 2-p>1, the right side divided by y tends to minus infinity. This contradicts b(y)/y->beta, regardless of sigma. Thus no finite nonzero limit exists at a positive infinite end.

## 5. Negative end, corollaries and dependencies

For S_y(x,y)=(x,-y), define

    Wnew(X)=S_y W(S_y X),
    Thetanew(X)=-Theta(S_y X),
    Omeganew(X)=-Omega(S_y X).

Direct chain rules preserve both transport equations, divergence, negative curl, parity, the center, and uniform sublinearity. They send J to-J, A to-A and I(y) to-I(-y). A negative infinite end with finite nonzero limit would therefore produce a positive infinite end with finite nonzero limit. The preceding proof permits either sign of A, so the contradiction applies. No simultaneous normalization of the end and A is needed.

Constancy near the end supplies a finite limit and hence gives0. For the separated germ, T=H''(0)/sigma(y)^2 and Q=H''''(0)/sigma(y)^4, so I=H''''(0)/H''(0)^2 is a nonzero constant, impossible. If I is constant on all of unbounded J, it is0; P242 then rules out constant I3 on J under the same smooth equations and sublinearity. That last corollary uses P242's complete finite-algebra proof, not numerical fits.

The main proof uses only the displayed low-order equations, scalar ODE existence and an integrating factor, finite Taylor expansion, ordinary integration and sublinearity of the axis drift. It requires neither real analyticity nor global positivity of temperature/vorticity, higher symbol estimates, an integration by parts at spatial infinity, a special canonical inverse, or a condition on the other endpoint. The canonical inverse is left fixed in the B2 application. At beta2 the coefficient alpha and exponent gap vanish, so this proof gives no claim there. All remaining B2 classes and the full endpoint stay OPEN.
