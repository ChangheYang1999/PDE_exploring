# Decay restrictions on fourth-order axis-ratio tails

## Statements and scope

Let beta>2 and let smooth real fields W,Theta,Omega on R2 satisfy

    div W=2beta, Omega=partial_y W1-partial_x W2,
    W(0)=0, W(X)=beta X+o(|X|) uniformly at infinity,
    W.gradTheta=(beta-2)Theta, W.gradOmega+Omega=Theta_x.

Assume W1,Omega odd and W2,Theta even in x, Theta(0,y)=0, and Theta=a0 x^2+O(|X|^3) at0 with a0!=0. Let T(y)=Theta_xx(0,y), A=T(0), J the component of {T!=0} containing0, and I(y)=Theta_xxxx(0,y)/T(y)^2 on J. Put m=1-2/beta>0. At an infinite end of J:

1. If I(y)=L |y|^q(1+o(1)) for a finite real q and L!=0, then q<=-m. In particular a nonzero power tail decaying more slowly than |y|^(-1+2/beta) is impossible.
2. If I is eventually monotone as a function of distance along that end, then I tends to0. No power expansion is assumed in this second assertion.

No sign of a0 or global sign of Theta or Omega, no derivative bounds at infinity, and no condition at the other endpoint are required. These are necessary restrictions, not existence or whole-class nonexistence results. The first assertion does not exclude the equality q=-m, prove that equality is attained, or exclude faster decay. The second does not cover general nonmonotone ratios. Beta2 and bounded J remain outside both statements.

The proof extends P257 with a stronger bound for the first vorticity coefficient. All needed identities and analytic arguments are proved again below. It is written before new controls and external review. The full B2 endpoint remains OPEN.

## 1. Axis identities with signed center data

We treat a positive infinite end first and keep A!=0 of either sign. Define

    rho=(A/T)^(1/2)>0, rho(0)=1,
    R(y)=integral_0^y rho(s)ds,
    b(y)=W2(0,y), d=(3beta+2)/2,
    gamma=1/2+1/beta, h=(beta+6)/2.

Writing w=partial_xW1(0,y), divergence gives w=2beta-b'. The x^2 thermal coefficient is bT'+2wT=(beta-2)T. It gives (rho b)'=d rho and, since b(0)=0,

    b=dR/rho.                                (1)

Thus b>0 on y>0 in J. Sublinearity gives b(y)/y->beta. Since R'=rho, one has yR'/R->d/beta=gamma+1. Integrating logarithmic-derivative inequalities and using(1) proves, for every sufficiently small epsilon>0,

    c y^(gamma-epsilon)<=rho(y)<=C y^(gamma+epsilon),
    c y^(gamma+1-epsilon)<=R(y)<=C y^(gamma+1+epsilon). (2)

No derivative of b/y is taken. The constants may depend on epsilon. In particular rho has a positive minimum on[0,infinity).

Let eta=Omega_x(0,y), r=rho eta, and v=partial_x^2W2(0,y)/2. Negative curl and the x coefficient of vorticity transport give

    eta=-b''-2v,
    b eta'+(2beta+1-b')eta=T,
    b r'+(beta/2)r=A/rho.                     (3)

Every backward axis orbit from y in J stays on the compact segment from0 to y and tends to0. This follows from(1), the sign of b, and smooth local existence. Integrating(3) along that orbit gives

    r(y)=A integral_-infinity^0 exp(beta s/2)/rho(y(s))ds. (4)

The lower endpoint term vanishes by boundedness on the compact segment. Thus r has the sign of A and |r|<=C on the positive half-axis. No positivity normalization of A is used.

For the fourth-order identity write Q=Theta_xxxx(0,y)=A^2 I/rho^4. Finite smooth Taylor expansion and divergence give

    W2=b+v x^2+O(x^4),
    W1=(2beta-b')x-v'x^3/3+O(x^5),
    Theta=T x^2/2+Q x^4/24+O(x^6).

The x^4 thermal coefficient is

    4(2beta-b')Q-8Tv'+bQ'+12vT'=(beta-2)Q.

Substituting T=A/rho^2 and(1), this becomes (rho^3v)'=(A/8)[(beta-2)rho I+dR I']. Finite integration by parts gives exactly

    rho^3v=c2+(A/8)[dR I-h integral_0^y rho I], c2=v(0). (5)

No derivative of I is estimated at infinity.

## 2. Sharper bound for the first vorticity coefficient

Fix a sufficiently large Y>0 and define

    mu(y)=exp(integral_Y^y beta/(2b(s))ds), y>=Y.

From b(y)/y->beta, logarithmic integration gives

    c y^(1/2-epsilon)<=mu(y)<=C y^(1/2+epsilon)

for every small epsilon>0, after changing constants. Equation(3) has the ordinary integrating-factor solution

    r(y)=mu(y)^(-1)[r(Y)+A integral_Y^y mu(s)/(b(s)rho(s))ds]. (6)

By(2), b(s) is comparable to s and the absolute integrand is at most C s^(-1-1/beta+2epsilon). It is integrable if2epsilon<1/beta. The bracket in(6) is therefore bounded, giving

    |r(y)|<=C y^(-1/2+epsilon),
    |eta(y)|<=C y^(-1-1/beta+2epsilon).       (7)

This improvement uses only the axis ODE and b/y->beta. It does not assume a derivative asymptotic for b or a decay hypothesis on Omega.

## 3. Exclusion of slower power tails

Assume I(y)=L y^q(1+o(1)), with L!=0 and q>-m. Put k=q+m>0. Then q+gamma+1>0, since at q=-m its value is1/2+3/beta. Define

    H_q(y)=integral_Y^y rho(s)s^q ds.

For sufficiently small epsilon, (2) shows both H_q and R(y)y^q tend to infinity. A direct differentiation, using R'=rho and(1), gives

    (R y^q)'/(rho y^q)=1+q b/(dy)->1+q/(gamma+1)>0.

Consequently

    H_q/(R y^q)->(gamma+1)/(gamma+1+q).       (8)

For completeness this limit follows by integrating the derivative ratio inequalities from a fixed large point. If the ratio of the derivatives lies between ell-delta and ell+delta, integrate against the positive derivative of the denominator; finite initial values vanish after division by its divergent value. This avoids differentiating I or invoking an unproved regular-variation theorem.

The assumed asymptotic for I and a split at fixed large Y imply, by the same positive-weight comparison,

    integral_0^y rho I
      =L R y^q (gamma+1)/(gamma+1+q) (1+o(1)).

The finite initial integral is negligible. Since d=beta(gamma+1), h/beta=(gamma+1)-m, equation(5) yields

    v=(A L/8) d (q+m)/(gamma+1+q)
                     (R y^q/rho^3)(1+o(1)). (9)

The displayed scalar apart from A L is positive. The term c2 is negligible because R y^q tends to infinity. Equations(1)-(2) give

    R y^q/rho^3=b y^q/(d rho^2)>=c y^(q-2/beta-2epsilon). (10)

Choose epsilon>0 so that

    2epsilon<1/beta,
    2epsilon<q+m,
    4epsilon<q+1-1/beta,
    epsilon<q+gamma+1.

All right sides are positive when q>-m. For example epsilon=k/[16(1+beta k)] satisfies these inequalities. Put p=2/beta+2epsilon-q<1. Equations(7),(10) show eta=o(y^-p). With sigma=sign(A L), equations(3),(9) therefore give

    sigma b''<=-c y^-p

eventually. Twice integrating from a fixed point gives

    sigma b(y)<=O(y)-c y^(2-p)/[(1-p)(2-p)].

This holds for every real p<1, including negative p. Since2-p>1 it contradicts b(y)/y->beta. Thus a nonzero power tail must have q<=-m, proving assertion1. At q=-m the coefficient in(9) cancels; no conclusion at that exponent is claimed.

## 4. Eventual monotonicity forces zero limit

An eventually monotone real function has a limit in the extended real line. A finite nonzero limit is the already proved power case q=0, which is excluded because m>0. It remains to exclude either infinite limit.

In that case, for some Y, the function K=s I is positive, nondecreasing and unbounded on[Y,infinity), where s=1 if I tends to plus infinity and s=-1 otherwise. It is enough that K be bounded below by a positive constant. Let C0=integral_0^Y rho K, which is a finite signed number even if K changes sign before Y. Then

    integral_0^y rho K
      <=C0+K(y)[R(y)-R(Y)]<=C0+R(y)K(y).

Because h>0, equation(5) gives

    s[dR I-h integral_0^y rho I]
      >=(d-h)R K-hC0=(beta-2)R K-hC0.

As R K tends to infinity, this is eventually at least a fixed positive multiple of R K, hence of R. Taking sigma=sign(A s) and including the finite c2 term, one obtains sigma v>=c R/rho^3. From(2), this is at least c y^(-2/beta-2epsilon). The eta bound(7) is lower order for a sufficiently small epsilon, and2/beta+2epsilon<1. The same twice-integrated contradiction follows. Both infinite limits are impossible, so the only possible limit of an eventually monotone I is0.

## 5. Negative ends and B2 interpretation

Reflect the vertical coordinate by S_y(x,y)=(x,-y), and set Wnew=S_y W(S_yX), Thetanew=-Theta(S_yX), Omeganew=-Omega(S_yX). Component chain rules preserve all hypotheses and send J to-J, A to-A and I(y) to-I(-y). The power exponent and nonzero magnitude, and eventual monotonicity along the end, are preserved. Since the proof retained either sign of A and L, it applies to negative infinite ends as well.

For an actual B2 profile, W=beta X+U-U(0), div U=0 and U=(-Psi_y,Psi_x) with -DeltaPsi=Omega give exactly the divergence and negative-curl identities above. The center subtraction changes neither. Canonical sublinear U implies W-beta X=o(r). Thus the theorem applies without changing the inverse or imposing a stationary physical center.

The proof requires only low-order smooth identities, ordinary scalar ODE integration, positive-weight estimates and sublinearity. It gives no sign restriction on the full vorticity or temperature and no bounds on higher derivatives. The asymptotic assumption in assertion1 and eventual monotonicity in assertion2 are explicit additional conditions on a ratio. No claim about arbitrary oscillatory ratios, bounded components, beta2, or the full existence problem follows. Formal Lean/Lake execution is prohibited and is not used.
