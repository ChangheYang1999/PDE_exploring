# Power thresholds for a signed fourth-order axis ratio

## Statement, notation and scope

Let beta>=2. Let smooth real fields W, Theta and Omega on R2 satisfy

    div W=2beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly as |X| tends to infinity,
    W.gradTheta=(beta-2)Theta,
    W.gradOmega+Omega=Theta_x.

Assume W1 and Omega are odd in x, W2 and Theta are even in x, Theta(0,y)=0, and Theta(x,y)=a0 x2+O(|X|3) at the origin, with a0 nonzero. Define

    T(y)=Theta_xx(0,y), A=T(0)=2a0,
    J=the component of {T!=0} containing zero,
    rho(y)=sqrt(A/T(y))>0, R(y)=integral_0^y rho(t)dt,
    I(y)=Theta_xxxx(0,y)/T(y)2,
    G(y)=integral_0^y rho(t)I(t)dt,
    m=1-2/beta.

Suppose J has an infinite end. For every real s>-m, along that end,

    liminf |y|^(-s) A G(y)/R(y) <= 0.                         (A)

The liminf is extended real, and R,G are the signed integrals as displayed, including at the negative end. In particular

    liminf |y|^(-s) a0 I(y) <= 0.                            (B)

Equivalently, no c>0 can satisfy a0 I(y)>=c |y|^s on an entire tail at that end. Statement (A) is stronger than the lead's pointwise assertion (B). No additional derivative bounds on I or W at infinity, no monotonicity, no class A assumption, no sign normalization of a0, and no condition at the other end are used.

For beta>2, s=0 is allowed: a0 I cannot have a positive finite limit or tend to positive infinity. Combined with P257, any extended-real limit of a0 I must be zero or negative infinity. P258 excludes negative infinity if I is eventually monotone; it also excludes either signed nonzero pure-power asymptotic I=L |y|^q(1+o(1)) when q>-m. These last two assertions are separate dependencies, not consequences of (A) alone.

At beta2 the present threshold is s>0. Bounded ratios and subpower growth are not excluded here. Equality s=-m, the opposite signed power bound, bounded J and arbitrary full profiles remain open. No existence or whole-class nonexistence endpoint follows.

## 1. Exact equations on a positive infinite end

Write b(y)=W2(0,y), eta(y)=Omega_x(0,y), v(y)=W2_xx(0,y)/2, d=(3beta+2)/2, h=(beta+6)/2 and gamma=1/2+1/beta. Keep A of either sign. Divergence yields W1_x(0,y)=2beta-b'. Thermal transport at order x2 gives

    bT'+(3beta+2-2b')T=0.

Since T=A/rho2, this is (rho b)'=d rho. The values rho(0)=1 and b(0)=R(0)=0 give

    b=dR/rho.                                               (1)

Consequently b>0 at every y>0 on J. A finite Taylor expansion gives

    W2=b+v x2+O(x4),
    W1=(2beta-b')x-v'x3/3+O(x5),
    Theta=T x2/2+Q x4/24+O(x6), Q=Theta_xxxx(0,y).

The negative curl and the order-x vorticity equation give

    eta=-b''-2v,
    b eta'+(2beta+1-b')eta=T.

Thus r=rho eta satisfies

    b r'+(beta/2)r=A/rho.                                    (2)

Thermal transport at order x4 gives

    4(2beta-b')Q-8T v'+b Q'+12v T'=(beta-2)Q.

Insert Q=A2 I/rho4 and (1). Integration by parts over the finite interval from zero to y gives

    rho3 v=c2+(A/8)(d R I-h G), c2=v(0).                     (3)

No estimate at infinity is needed to obtain these identities.

## 2. Integrable error terms

Since W-beta X=o(|X|), b/y tends to beta. Equation (1) gives R'/R=d/b. Integrating upper and lower bounds on this logarithmic derivative, then using rho=dR/b, gives for every sufficiently small epsilon>0

    c y^(gamma+1-epsilon)<=R(y)<=C y^(gamma+1+epsilon),
    c y^(gamma-epsilon)<=rho(y)<=C y^(gamma+epsilon)           (4)

for large y. The constants may depend on epsilon. No limit of b' is asserted and no asymptotic limit is differentiated.

For large fixed Y, put mu=exp(integral_Y^y beta/(2b)). The same logarithmic argument gives c y^(1/2-epsilon)<=mu<=C y^(1/2+epsilon). Solving (2) on [Y,y],

    r=mu^(-1)[r(Y)+A integral_Y^y mu/(b rho)].

The integrand is O(y^(-1-1/beta+2epsilon)), so it is integrable when 2epsilon<1/beta. Therefore

    |eta(y)|<=C y^(-1-1/beta+2epsilon).                       (5)

Define positive functions on y>0

    k=1+h/d, M=rho4 R^(-k), N=rho R^(-k).

Here 1<k<=2 for beta>=2. Since rho'/rho=(d-b')/b and 3d-h=4beta,

    M'/M=4(beta-b')/b.                                       (6)

The central powers satisfy

    4gamma-k(gamma+1)=0,
    gamma-k(gamma+1)=-1-h/beta.

Consequently (4)-(5) imply

    M |eta|<=C y^(-1-1/beta+(6+k)epsilon),
    N<=C y^(-1-h/beta+(1+k)epsilon).

Choose epsilon with (6+k)epsilon<1/beta and (1+k)epsilon<h/beta. These quantities are then absolutely integrable on [Y,infinity). This includes beta2, where k=2 and h/beta=2.

## 3. The exact energy identity and its one-sided consequence

Because G'=rho I and b=dR/rho, (3) is equivalent to

    (G R^(-h/d))'=(8/(A d))N(rho3 v-c2).

Substitute v=-(b''+eta)/2 and use M=N rho3 to obtain

    ((A d/4)G R^(-h/d))'=-M b''-M eta-2c2 N.

Combining this with (6), the quantity

    S=(A d/4)G R^(-h/d)+M(b'-beta)

satisfies exactly

    S'=-4M(b'-beta)2/b-M eta-2c2 N.                           (7)

The square term is nonpositive because b>0. The remaining terms have finite absolute integral by section 2. Finite-interval integration therefore gives S(y)<=C for all large y. This proof needs no limit of S or b', and asserts no integrability of the square. In particular it gives no lower bound for S.

## 4. Exclusion of a positive power lower bound for the weighted mean

Suppose (A) fails for some s>-m. There are c>0 and Y1 such that

    A G(y)/R(y)>=c y^s for all y>=Y1.

Put delta=s+m>0. Since 1-h/d=(beta-2)/d>=0 and

    (gamma+1)(1-h/d)=m,

the term y^s R^(1-h/d) is bounded below by c y^(delta-(1-h/d)epsilon). Choose epsilon small enough that this exponent is positive, in addition to the integrability conditions of section 2. The upper bound for S gives

    M(b'-beta)<=C-c y^s R^(1-h/d).

The growing negative term eventually absorbs C. Dividing by M and using (1),

    b'<=beta-c y^s R2/rho4
       =beta-c y^s b2/(d2 rho2)
       <=beta-c y^(s+2-2gamma-2epsilon)
       =beta-c y^(delta-2epsilon).                           (8)

The last step uses b~beta y and the upper bound for rho. Further choose 2epsilon<delta. Integrating (8) from a fixed point forces b(y)/y to be bounded above by a quantity tending to negative infinity. This contradicts b/y->beta. Thus (A) holds.

For an explicit simultaneous choice, epsilon=delta/[128 beta(1+beta delta)] satisfies all preceding strict inequalities for beta>=2 and delta>0: it is positive, epsilon<delta/256, epsilon<1/(128 beta2), 0<=1-h/d<1, 1<k<=2 and h/beta>=1/2. These elementary bounds also ensure 2epsilon<1/beta.

## 5. Deduction of the pointwise result

If a0 I(y)>=c y^s eventually, then A I>=2c y^s and

    A G(y)>=C0+2c integral_Y^y rho(t)t^s dt.

Put H(y)=integral_Y^y rho(t)t^s dt and F(y)=R(y)y^s. Direct differentiation, with no derivative of I, gives

    F'(y)/(rho(y)y^s)=1+s R/(y rho)
                    =1+(s/d)b/y -> 1+s/(gamma+1)>0.

The limiting constant is positive because s>-m and gamma+1-m=1/2+3/beta>0. Bounds (4) also show F(y) tends to infinity for sufficiently small epsilon. Finite positive-weight integration of the last derivative comparison gives H/F tending to the positive reciprocal of that limiting constant. More explicitly, for any small error e, bound F' between (L-e)rho y^s and (L+e)rho y^s on a tail, integrate, divide by H tending to infinity and let e tend to zero. Hence A G/R>=c1 y^s eventually, with c1>0, contrary to (A). This proves (B) for either sign of A.

## 6. Negative infinite ends and relation to the lead's proof

Reflect by Sy(x,y)=(x,-y): Wnew(X)=Sy W(Sy X), Thetanew(X)=-Theta(Sy X), Omeganew(X)=-Omega(Sy X). Chain rules preserve every equation and parity assumption. The transformed quantities are

    Anew=-A, rhonew(y)=rho(-y), Rnew(y)=-R(-y),
    Inew(y)=-I(-y), Gnew(y)=G(-y).

Therefore Anew Gnew/Rnew=A G(-y)/R(-y) and anew Inew=a0 I(-y). Positive-end statements (A)-(B) give exactly their negative-end versions, including all signs. A cannot simultaneously be normalized positive by that same reflection.

For comparison only, the lead defines h0(y)=exp(integral_1^y h/b), P=rho3/(b h0), Phi=G/h0 and Q0=A Phi+4P(b'-beta). Integrating R'/R=d/b gives h0=C R^(h/d) with C=R(1)^(-h/d)>0. Thus P=M/(d C), Q0=4S/(d C), and its identity

    Q0'=-16P(b'-beta)2/b-4P(eta+2c2/rho3)

is precisely a positive constant multiple of (7). Its contradiction from Q0=A Phi-b P' and P=y^(o(1)) is valid: the same epsilon choice can make 4epsilon<delta-2epsilon and 6epsilon<1/beta. The proof above derives (A) directly and hence independently verifies the lead's weaker pointwise statement. No lead code is used.

For the prompt, W=beta X+U-U(0) has the divergence and negative curl assumed here, and canonical sublinear U gives W-beta X=o(|X|). The result adds a necessary axis condition; it neither changes the inverse nor appends a gauge. General B2 remains OPEN.
