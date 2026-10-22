# No positive signed divergence of the quartic axis ratio at beta2

## Exact statement and scope

Let smooth real fields W=(W1,W2), Theta and Omega on R2 satisfy

    div W=4, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=2X+o(|X|) uniformly at infinity,
    W.grad Theta=0, W.grad Omega+Omega=Theta_x.

Assume W1 and Omega are odd in x, W2 and Theta are even in x, Theta(0,y)=0 and Theta(x,y)=a0 x^2+O(|X|^3) at0 with a0!=0. Put A=Theta_xx(0)=2a0, T(y)=Theta_xx(0,y), and let J be the component containing0 of {T!=0}. Define I(y)=Theta_xxxx(0,y)/T(y)^2 on J. At every infinite end of J it is impossible that

    A I(y) -> +infinity.                                      (1)

Equivalently, liminf A I(y)<+infinity there, where a liminf of -infinity is allowed. If I has an extended-real limit, its sign multiplied by A cannot be positive infinity. Finite limits and divergence with the opposite sign are not excluded. No monotonicity of I, no derivative bounds at infinity beyond smoothness, and no specified rate in W-2X=o(|X|) are assumed.

The proof only uses four low-order axis identities and b(y)/y->2, stated below. Thus the claim also holds for any globally defined smooth axis data obeying those identities on an infinite end of their central nonvanishing component, with rho>0, regardless of whether a full profile realizes them. The oscillatory example P266 with A L<0 is compatible with this restriction. The positive and negative logarithmic examples P270 require beta>2, so they do not contradict it. This is a necessary partial result at beta2, not a general B2 exclusion or an early endpoint. Canonical inversion is not used.

## Axis identities derived from the fields

First consider a positive infinite end, so [0,infinity) lies in J. Define

    b=W2(0,y), v=W2_xx(0,y)/2, eta=Omega_x(0,y),
    rho=sqrt(A/T)>0, R(y)=integral_0^y rho,
    G(y)=integral_0^y rho I, c2=v(0).

Here rho(0)=1. Parity, divergence and curl give W1_x(0,y)=4-b' and eta=-b''-2v. Twice differentiating thermal transport on x=0 gives

    bT'+(8-2b')T=0.

Since T=A/rho^2, this is(rho b)'=4rho. Integrating from0 and using b(0)=0 yields

    rho b=4R, R'/R=4/b, b>0 for y>0.                         (2)

The first vorticity coefficient gives b eta'+(5-b')eta=T. With r=rho eta this is

    b r'+r=A/rho.                                             (3)

For completeness, write D=Theta_xxxx(0,y)=A^2I/rho^4. Near the axis the needed finite coefficients are

    Theta=Tx^2/2+Dx^4/24+O(x^6),
    W2=b+vx^2+O(x^4),
    W1=(4-b')x-v'x^3/3+O(x^5).

The x^4 thermal coefficient, multiplied by24, is

    bD'+(16-4b')D-8v'T+12vT'=0.

Substituting T,D and using(2) gives bI'=8(rho^3v)'/(A rho). Its finite integral from0 to y, together with G'=rho I and R'=rho, is

    rho^3v=c2+(A/2)(RI-G).                                   (4)

No infinite integration by parts is used in deriving(4). These equations hold on each compact subinterval of J by smoothness, with the same constant c2.

## Tail bounds and an absolutely integrable error

Sublinearity on the axis implies b/y->2. From R'/R=4/b, for every sufficiently small epsilon>0 there are positive constants c,C and a starting point Y such that

    c y^(2-epsilon)<=R<=C y^(2+epsilon),
    c y^(1-epsilon)<=rho<=C y^(1+epsilon).                    (5)

This follows by integrating inequalities for the logarithmic derivative of R; it does not differentiate b/y->2. The rho bounds follow from rho=4R/b and comparability of b and y, with epsilon relabeled if needed.

For(3) let mu_r=exp(integral_Y^y1/b), so mu_r lies between constants times y^(1/2-epsilon) and y^(1/2+epsilon). Variation of constants gives

    r=mu_r^(-1)[r(Y)+A integral_Y^y mu_r/(b rho)].

The integrand is O(y^(-3/2+2epsilon)), integrable if2epsilon<1/2. Thus

    |r|<=C y^(-1/2+epsilon),
    |eta|<=C y^(-3/2+2epsilon).                              (6)

Put h=exp(integral_Y^y4/b)>0. Equation(2) gives the exact identity h=C_h R for some C_h>0. Define

    P=rho^3/(b h)>0, E=b'-2,
    H=A G/h, f=eta+2c2/rho^3, Q=H+4PE.                      (7)

From(5), h has the same power bounds as R and P lies between constants times y^(-4epsilon) and y^(4epsilon). The terms in Pf satisfy

    |P eta|<=C y^(-3/2+6epsilon),
    |2c2 P/rho^3|=|2c2|/(b h)<=C y^(-3+epsilon).

Choose0<epsilon<1/24. Both powers are integrable at infinity. Therefore

    integral_Y^infinity |P f| dy < infinity.                 (8)

This is absolute integrability, without any sign assumption. All objects are smooth on the tail.

## Exact weighted identities

Logarithmic differentiation of P, using rho'/rho=(4-b')/b and h'/h=4/b, gives

    P'/P=-4E/b.

Equation(4) and G'=rho I imply

    H'=8P(v-c2/rho^3)=-4P(E'+f).

Differentiating Q therefore gives

    Q'=-16PE^2/b-4Pf.                                       (9)

Let t=log y, B(t)=b(e^t)/e^t, and let a dot denote d/dt. In the following formulas P,E,H,Q and f are evaluated at y=e^t. Then B->2 and

    dot P=-4PE/B,
    dot Q=-16PE^2/B-4P e^t f,
    E=dot B+B-2.                                            (10)

By(8), the smooth tail integral

    e(t)=4 integral_t^infinity P(e^s)e^s f(e^s) ds

is finite and tends to0, and dot e=-4P e^t f. Define q=Q-e. It follows exactly that

    dot q=-16PE^2/B<=0,
    H=q+e-4PE.                                              (11)

The monotone q has a finite upper bound on every tail, but it may tend to minus infinity. The two cases below do not assume it is bounded below.

## Positive signed divergence would force H to infinity

Differentiate G=hH/A exactly and divide by rho. Since h=C_hR and b rho=4R,

    A I=C_h[H+(B/4) dot H].                                 (12)

Suppose(1). In logarithmic time AI/C_h tends to positive infinity. Equation(12) is

    dot H+(4/B)H=(4/B)(AI/C_h).

On a late tail4/B is bounded above and below by positive constants. For any real M>0, choose a starting time with AI/C_h>=2M thereafter. Variation of constants applied to H-2M gives

    H(t)>=2M+[H(T)-2M] exp(-integral_T^t4/B).

The exponential tends to zero, so H>=M eventually. As M is arbitrary, H->positive infinity.

Put D=-E on a late tail. Equation(11), the upper bound on q and e->0 show

    4PD=H-q-e -> +infinity.

Consequently D>0 eventually, P is increasing by(10), and

    dot P=4PD/B -> +infinity.                               (13)

We now show these conclusions are impossible in both possible sign histories of the monotone q.

## Case 1: q becomes strictly negative

Assume q(T)<0 at some sufficiently late time. Since q is nonincreasing, q remains strictly negative. Define z=-q/P>0. Equations(10)-(11), with E=-D, give

    dot z=(4D/B)(4D-z),
    P(4D-z)=H-e.                                            (14)

Since H->infinity and e->0, the second quantity is positive on a late tail. Thus dot z>0 there, and z>=z0>0 from any fixed time on that tail. Again by(14),4D>z, so D>=z0/4. The last equation of(10) says

    dot B=2-B-D.

For large t, |2-B|<z0/8, giving dot B<=-z0/8. Finite integration contradicts B->2. This case is impossible, including when q tends to minus infinity.

## Case 2: q never becomes negative on the late tail

Then q>=0 and q is nonincreasing, so q has a finite nonnegative limit. Integrating(11) proves

    integral_T^infinity P D^2 dt < infinity,                (15)

because B is bounded above and below by positive constants. Let F=sqrt(P)>0. By(13),

    dot F=2sqrt(P)D/B,

so(15) gives integral_T^infinity |dot F|^2 dt<infinity. This forces

    F(t)/sqrt(t)->0, hence P(t)/t->0.                        (16)

Here is the full elementary argument. For a fixed late S and t>S, Cauchy-Schwarz yields

    |F(t)|<=|F(S)|+sqrt(t-S)
                         (integral_S^infinity |dot F|^2)^(1/2).

Divide by sqrt(t), take the limsup as t tends to infinity, and then let S tend to infinity. The squared-integral tail tends to zero, proving(16). This does not claim that F itself has a finite limit.

But(13) gives dot P>=1 for all sufficiently large t. Integration implies liminf P(t)/t>=1, contradicting(16). This case is also impossible. Therefore(1) cannot hold at a positive infinite end.

## Negative infinite end and interpretation

For a negative infinite end set

    Wtilde(x,y)=(W1(x,-y),-W2(x,-y)),
    Thetatilde(x,y)=-Theta(x,-y),
    Omegatilde(x,y)=-Omega(x,-y).

Direct differentiation preserves all field equations, parities and sublinearity. It sends A to-A, J to-J and I(y) to-I(-y); the product AI is therefore unchanged at the reflected point. The proved positive-end assertion applies and gives the same exclusion at the negative end.

For a real function, liminf equal to positive infinity is exactly convergence to positive infinity. Thus the stated liminf form is equivalent. At beta2 this rules out positive signed divergence even slower than any positive power, which is not excluded by the supercritical-power theorem alone. It does not assert a universal numerical upper bound, boundedness of I, existence of a limit, or any conclusion when J is bounded. The negative signed logarithmic construction remains compatible, as do the finite critical limits. General B2 remains OPEN.

## Dependencies and verification plan

The proof is complete from the displayed equations. It uses finite Taylor coefficient calculations, positive scalar integrating factors, elementary power bounds, an absolutely convergent tail integral, and Cauchy-Schwarz. The weighted identity from P263 is rederived. No numerical estimate is used as a premise and no unjustified asymptotic derivative is taken. This full informal argument is written before independent exact controls and an actual Opus5.5 consultation. Their outcomes, timestamps and any limitations will be recorded in verification. No formal build is authorized or claimed.
