# A one-sided constraint on the weighted fourth-order axis ratio

## Statement and scope

Let beta>2 and let smooth real W,Theta,Omega on R2 satisfy

    div W=2beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly,
    W.gradTheta=(beta-2)Theta, W.gradOmega+Omega=Theta_x.

Require W1,Omega odd and W2,Theta even in x, Theta(0,y)=0, and Theta=a0 x^2+O(|X|^3) with a0!=0. Put T(y)=Theta_xx(0,y), A=T(0), and let J be the component of {T!=0} containing0. Define rho=sqrt(A/T)>0, R(y)=integral_0^y rho and I(y)=Theta_xxxx(0,y)/T(y)^2 on J. If J has the positive infinite end, then

    liminf_(y->infinity) A [integral_0^y rho(s)I(s)ds]/R(y) <= 0.       (S)

Here the liminf is in the extended real line. Consequently it is impossible that A I(y)>=delta>0 eventually. At a negative infinite end the same assertion holds with y->-infinity and the signed integrals R and integral_0^y rho I as displayed. In particular the excluded pointwise condition is invariant under the reflection needed to orient an end.

No upper bound or derivative bound on I is assumed. No statement that an eventually negative A I is impossible is made. This necessary signed-average restriction leaves arbitrary ratios, bounded J, beta2 and the general B2 problem OPEN. It is not an existence or whole-class nonexistence theorem. The proof is written before the independent algebra checks and external review.

## 1. Exact axis identities

We first treat y>0 in J and keep A of either sign. Write b=W2(0,y), eta=Omega_x(0,y), v=W2_xx(0,y)/2, d=(3beta+2)/2, h=(beta+6)/2 and gamma=1/2+1/beta. Divergence gives W1_x=2beta-b'. The x^2 coefficient of thermal transport is

    b T'+(3beta+2-2b')T=0.

As T=A/rho^2, it follows that (rho b)'=d rho, whence

    b=dR/rho.                                                    (1)

Thus b>0 for y>0. Negative curl gives eta=-b''-2v. The x coefficient of vorticity transport gives

    b eta'+(2beta+1-b')eta=T.

For r=rho eta this becomes

    b r'+(beta/2)r=A/rho.                                         (2)

With Q=Theta_xxxx(0,y), a finite Taylor expansion has

    W2=b+v x^2+O(x^4), W1=(2beta-b')x-v'x^3/3+O(x^5),
    Theta=T x^2/2+Q x^4/24+O(x^6).

The x^4 thermal equation is

    4(2beta-b')Q-8T v'+b Q'+12v T'=(beta-2)Q.

Substitution Q=A^2 I/rho^4 and (1), followed by one finite integration by parts, gives

    rho^3 v=c2+(A/8)[d R I-h J0],
    J0(y)=integral_0^y rho I, c2=v(0).                            (3)

Every identity is local on J and no derivative at infinity has been assumed.

## 2. Bounds obtained without differentiating a limit

Sublinearity gives b/y->beta. From (1), R'/R=d/b, so logarithmic integration and then rho=dR/b imply, for every sufficiently small epsilon>0,

    c y^(gamma+1-epsilon)<=R<=C y^(gamma+1+epsilon),
    c y^(gamma-epsilon)<=rho<=C y^(gamma+epsilon).                  (4)

Fix large Y. The integrating factor mu=exp(integral_Y^y beta/(2b)) satisfies c y^(1/2-epsilon)<=mu<=C y^(1/2+epsilon). Formula (2) yields

    r(y)=mu(y)^(-1)[r(Y)+A integral_Y^y mu/(b rho)].

The integrand is O(y^(-1-1/beta+2epsilon)), hence integrable if2epsilon<1/beta. Thus

    eta=O(y^(-1-1/beta+2epsilon)).                                (5)

All constants may depend on epsilon. The estimates are valid for either sign of A.

Define on y>0

    M=rho^4 R^(-1-h/d)>0, N=rho R^(-1-h/d)>0.

Since rho'/rho=(d-b')/b, direct differentiation gives

    M'/M=4(beta-b')/b.                                            (6)

Here 3d-h=4beta. The powers in (4) give the following useful integrability facts, with a sufficiently small fixed epsilon:

    integral_Y^infinity M |eta| < infinity,
    integral_Y^infinity N < infinity.                            (7)

To spell this out, put k0=1+h/d>0. The central power of M is4gamma-k0(gamma+1)=0, so M<=C y^((4+k0)epsilon). By (5), M|eta|<=C y^(-1-1/beta+(6+k0)epsilon), integrable if(6+k0)epsilon<1/beta. The central power of N is gamma-k0(gamma+1)=-1-h/beta; hence N<=C y^(-1-h/beta+(1+k0)epsilon), integrable if(1+k0)epsilon<h/beta. Such epsilon exists. The same epsilon can also satisfy2epsilon<1/beta and2epsilon<1-2/beta.

## 3. A signed energy identity

Because J0'=rho I and b=dR/rho, equation (3) is equivalent to

    (J0 R^(-h/d))'=(8/(A d)) N (rho^3 v-c2).

Using v=-(b''+eta)/2 and M=N rho^3 gives

    ((A d/4) J0 R^(-h/d))'=-M b''-M eta-2c2 N.                    (8)

From (6),

    (M(b'-beta))'=M b''-4M(b'-beta)^2/b.

Therefore the quantity

    S=(A d/4) J0 R^(-h/d)+M(b'-beta)

obeys the exact identity

    S'=-4M(b'-beta)^2/b-M eta-2c2 N.                              (9)

Since b>0, the first term is nonpositive. The other terms are absolutely integrable by (7). Integrating over finite intervals and using those integrable bounds proves

    S(y)<=C for every y>=Y.                                      (10)

No integrability of the nonnegative square is claimed or needed. In particular no boundary value of b' or of M(b'-beta) has been assumed at infinity.

## 4. Contradiction from a positive eventual weighted mean

If (S) were false, there would be delta>0 and Y1 such that

    A J0/R >= delta for y>=Y1.

Then (10) implies

    M(b'-beta)<=C-(d delta/4) R^(1-h/d).

Since1-h/d=(beta-2)/d>0 and R->infinity, the constant is eventually absorbed, yielding

    b'<=beta-c R^(1-h/d)/M
       =beta-c R^2/rho^4
       =beta-c b^2/(d^2 rho^2).                                 (11)

By b~beta y and (4), the last positive quantity is at least c y^(1-2/beta-2epsilon). Choose2epsilon<1-2/beta, so this exponent is strictly positive. Integrating (11) forces b(y)/y->-infinity along an eventual upper bound. This contradicts b/y->beta and proves (S).

If A I>=delta>0 eventually, then A J0>=delta R-C after finite integration. Thus A J0/R>=delta/2 eventually, contradicting (S). This proves the pointwise consequence without monotonicity, upper bounds, or derivative assumptions on I.

## 5. Negative ends and application

Set Sy(x,y)=(x,-y), Wnew=Sy W(SyX), Thetanew=-Theta(SyX), Omeganew=-Omega(SyX). Chain rules preserve the two transport equations, divergence, negative curl and all remaining assumptions. Then Anew=-A, rhonew(y)=rho(-y), Rnew(y)=-R(-y), Inew(y)=-I(-y), and J0new(y)=J0(-y). Hence Anew J0new/Rnew=A J0(-y)/R(-y) and Anew Inew=A I(-y). The positive-end proof gives exactly the negative-end statements. This reflection does not require an independent normalization of A's sign.

For B2, W=beta X+U-U(0) has the stated divergence and negative curl; the constant center subtraction affects neither. Canonical sublinear U gives W-beta X=o(r). Thus the theorem is a necessary condition for the prompt's profiles. It uses neither an artificial boundary nor a free added velocity. General B2 existence remains OPEN, and no claim about the opposite sign of the weighted mean follows from the one-sided bound (10).
