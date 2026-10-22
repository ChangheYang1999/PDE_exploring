# Curvature spikes prevent critical axis limits

## Exact statement and scope

Fix beta>=2, A>0, ell>0 and 0<delta<1. Set d=(3beta+2)/2, kappa=(beta+6)/2, gamma=1/2+1/beta and m=1-2/beta. There are globally smooth low-order axis data b,rho,r,eta,v,T,G,I with b odd, rho positive and even, b=dy and rho=1 near0, and

    R(y)=integral_0^y rho, rho b=dR,
    br'+(beta/2)r=A/rho, eta=r/rho=-b''-2v,
    T=A/rho^2, G(y)=integral_0^y rho I,
    rho^3v=-A/beta+(A/8)(dRI-kappa G).             (1)

Their central component {T!=0} is the whole real line. On the positive tail they satisfy

    beta<=b'<=d, b''<=0,
    b-beta y=O(y^(1-delta)), b'-beta=O(y^-delta).   (2)

Every derivative of every field in(1) is polynomially bounded. There is a finite real L0 such that

    liminf_{y->infinity} y^m I(y)=L0,
    limsup_{y->infinity} y^m I(y)=+infinity,
    I(y)=O(y^-m(1+(log y)^ell)).                  (3)

At beta>2, I tends to0. At beta2, I has finite liminf and positive infinite limsup, but does not tend to positive infinity. There are explicit sequences at which the critical quantity is asymptotic to a positive constant times (log y)^ell and sequences at which it tends to L0.

P272 assumes |(b-beta y)^(j)|<=C_j y^(1-delta-j) for j=0,1,2 on an infinite end and proves I=L y^-m+O(y^(-m-epsilon)), epsilon=min(delta,1/beta)>0, with finite L. Its conclusion is convergence of the critical quantity y^m I, not only I->0. Thus the curvature assumption j=2 in P272 cannot simply be deleted from the low-order axis theorem, even retaining concavity and its j=0 and j=1 bounds. In particular choose delta=1/beta, which is in(0,1) for every beta>=2. This statement concerns the axis identities alone. It is not a B2 profile, and it does not remove the curvature bound that an actual class-A profile has from the full PDE. The complete logarithmic tails of P266/P270 and the peaks here are different asymptotic assertions.

## A smooth concave axis velocity

Choose a smooth nondecreasing cutoff chi on R which is0 on(-infinity,0] and1 on[1,infinity), with chi'(s0)>0 for some s0 in(0,1). For example take the normalized ratio of exp(-1/s) and exp(-1/(1-s)), using zero extensions; its derivative is strictly positive in(0,1). For integers n>=N let

    Y_n=2^n, w_n=Y_n^(1-delta)/(log Y_n)^ell,
    a_n=c Y_n^-delta,
    c=(d-beta)(1-2^-delta)2^(N delta)>0.           (4)

Choose N sufficiently large that w_n<=Y_n/4 for every n>=N. This is possible because w_n/Y_n=Y_n^-delta/(log Y_n)^ell tends to0 monotonically for n>=1. Then sum_{n>=N}a_n=d-beta and the intervals [Y_n,Y_n+w_n] are disjoint, with nonempty gaps.

For y>=0 define

    b'(y)=beta+sum_{n>=N}a_n[1-chi((y-Y_n)/w_n)]. (5)

Extend b' evenly and integrate with b(0)=0, so b is odd. The series of constants converges uniformly; on each compact interval only finitely many terms are nonconstant, since Y_n tends to infinity. Thus b' is smooth. It is exactly d before Y_N, so the even extension is smooth at0. Each summand is nonnegative and nonincreasing. Consequently beta<=b'<=d and

    b''(y)=-sum_{n>=N}(a_n/w_n)chi'((y-Y_n)/w_n)<=0.          (6)

The flat cutoff gives smooth matching at every endpoint. For a large y only terms with Y_n comparable to or larger than y can be nonzero. More explicitly every term with Y_n+w_n<y vanishes, and the remaining indices have Y_n>=4y/5. Summing their geometric weights gives b'(y)-beta=O(y^-delta). Integrating from a finite point and using delta<1 gives b(y)-beta y=O(y^(1-delta)). This proves(2). The range delta<1 is explicit; integrating y^-delta would not give this conclusion at or above delta1.

Since supports in(6) are disjoint, at most one transition contributes at a given y. For k>=1, each derivative of order k of b' on the nth transition has magnitude at most

    C_k a_n w_n^-k
       =C_k c Y_n^(-delta-k(1-delta))(log Y_n)^(k ell).        (7)

These give polynomial bounds on all derivatives, and also

    0<=-y b''(y)<=C(1+(log y)^ell).             (8)

At y_n=Y_n+s0 w_n one has y_n/Y_n->1 and

    -y_n b''(y_n)
       ~c chi'(s0)(log Y_n)^ell ->+infinity.   (9)

At the gap points z_n=3Y_n/2 one has b''(z_n)=0, because Y_n+w_n<=5Y_n/4<z_n<Y_{n+1}. In particular the curvature estimate b''=O(y^(-1-delta)) fails: the ratio of its absolute value at y_n to y_n^(-1-delta) tends to infinity by(9).

## Reconstruction of all low-order axis jets

Set rho=1 near0, solve rho'/rho=(d-b')/b on the positive half-axis outside the inner interval, and extend rho evenly. The forcing vanishes on the inner interval. Since b>0 for y>0, this defines a global smooth positive function. Moreover rho>=1 because d-b'>=0. Differentiating gives (rho b)'=d rho, and integration from0 gives rho b=dR.

For y>0 define, with alpha=beta/(2d)>0,

    r(y)=(A/d)R(y)^(-alpha)integral_0^y R(u)^(alpha-1)du.      (10)

The integral is convergent at0 because R=y there and alpha>0. On the inner interval r=2A/beta. Differentiation using R'=rho and b rho=dR proves the r equation in(1). Its even extension is smooth and satisfies the same equation. Define eta=r/rho, v=-(b''+eta)/2 and T=A/rho^2 globally. These satisfy the center data and the following physical axis equations, by substituting rho'/rho=(d-b')/b and the equation for r:

    bT'+(3beta+2-2b')T=0,
    b eta'+(2beta+1-b')eta=T.


Take G=0 near0 and solve

    bG'-kappa G=(8/A)(rho^3v+A/beta)             (11)

on the positive and negative exterior intervals. The forcing vanishes on the inner interval and the coefficients are regular outside0. Its solutions therefore join smoothly to the zero inner solution. Let I=G'/rho. Then G(0)=0 and G'=rho I, and(11) gives the final identity of(1). For D=T^2 I, differentiation of this identity gives

    (rho^3v)'=(A/8)rho[bI'+(beta-2)I],
    bD'+(7beta+2-4b')D-8v'T+12vT'=0.

The second equation follows by multiplying the first by8T/rho^3 and substituting D=T^2I and T=A/rho^2. It is the fourth thermal jet equation, without invoking higher transverse equations. This establishes the claimed axis data with J=R, since T>0 everywhere.

For completeness all derivatives are polynomially bounded. The estimates below bound rho, rho^-1, r and the integrating factor h by powers. Equation(7) gives polynomial bounds on the derivatives of b, while b is comparable to|y| on each exterior half-axis. The rho and r equations then bound their derivatives inductively. The same holds for eta and v. The integrating-factor formula for(11), with h'/h=kappa/b and polynomially bounded forcing, bounds G by a power, allowing an extra logarithm if an exponent is -1. Differentiation of(11) then gives every derivative bound for G and I. Compact intervals cause no issue. Reflection supplies identical absolute tail estimates on the negative end, with no physical y parity assumed for v or I.

## Quantitative tail constants and the finite limit of G/h

Put p=d/beta and q=kappa/beta. By(2),

    d/b=d/(beta y)+O(y^(-1-delta)).

Integration of R'/R=d/b gives C_R>0 such that

    R=C_R y^p(1+O(y^-delta)),
    rho=C_rho y^gamma(1+O(y^-delta)), C_rho=dC_R/beta>0.      (12)

The second formula uses rho=dR/b rather than differentiating an asymptotic. On the positive tail choose a positive integrating factor h for kappa/b. Then

    h=C_h y^q(1+O(y^-delta)), C_h>0,
    P=rho^3/(b h)->P_infinity>0,
    y^m h/(b rho)->H0=C_h/(beta C_rho)>0.       (13)

The power cancellations are 3gamma-1-q=0 and q-1-gamma=-m. For the r equation the integrating factor for beta/(2b) is comparable to y^1/2, so its forcing integral has size y^(-1-1/beta) and converges. Thus r=O(y^-1/2), eta=O(y^(-1-1/beta)), and

    f=eta-2A/(beta rho^3)=O(y^(-1-1/beta)).      (14)

Here 3gamma>1+1/beta. In particular f is absolutely integrable and bf tends to0. This bound involves 1/beta, not the arbitrary delta in(2).

Set Phi=G/h. From(11) and the definition of v one has the exact identity

    Phi'=-(4/A)P(b''+f).                        (15)

Concavity and b'->beta give integral_Y^infinity |b''|=b'(Y)-beta<infinity. Since P is bounded and f is absolutely integrable, Phi' is absolutely integrable. There is therefore a finite real K with Phi->K. No pointwise curvature bound stronger than(8) has been used.

## Critical peaks and lower limit

Differentiate G=h Phi exactly and divide by rho. Using(15) gives

    y^m I=M(y)[kappa Phi-(4/A)bP(b''+f)],
    M(y)=y^m h/(b rho)->H0>0.                   (16)

By(12)-(15), the part M[kappa Phi-(4/A)bPf] tends to L0=H0 kappa K. The remaining part -(4/A)M bP b'' is nonnegative, since A>0, b>0, P>0, M>0 and b''<=0. Hence liminf y^m I>=L0. At the gap points z_n the remaining part is zero, giving equality.

At y_n, equations(9), (13) and b(y_n)/y_n->beta give

    y_n^m I(y_n)
       ~[4H0 beta P_infinity c chi'(s0)/A](log Y_n)^ell.     (17)

The bracket is strictly positive. This proves the positive infinite limsup. Formula(8) and(16) also give the global upper bound in(3). At beta>2, m>0 and y^-m(log y)^ell tends to0, proving I->0. At beta2, m=0, so the two lower/upper limit statements apply to I itself. This agrees with P271: an infinite limsup with finite liminf is different from a limit equal to positive infinity.

The first and zeroth derivative bounds in(2), even with concavity, therefore do not imply the conclusion of P272. The j=1 estimate also follows from j=0 and j=2 directly, without concavity. Indeed let g=b-beta y and h0=y/2. Taylor's formula with integral remainder on[y,y+h0] is

    g(y+h0)-g(y)=h0 g'(y)+integral_0^h0(h0-s)g''(y+s)ds.

If g=O(y^(1-delta)) and g''=O(y^(-1-delta)), the endpoint difference divided by h0 is O(y^-delta), and the remainder divided by h0 is also O(y^-delta), since all points of the interval are comparable to y. Thus g'=O(y^-delta). This holds for any delta>0. Independently, P272's integrating-factor proof uses only j=0 and j=2. This example establishes the independent role of curvature control for that axis theorem. It says nothing contrary to the full-PDE regularity estimates that supply j=2 for an actual class-A profile.

## Provenance and verification

The starting proposal is the public A158 referee answer in lead astra/z447_conc/answer.md, D3. Its delta there is1/beta. This proof independently supplies the global construction, checks the restriction0<delta<1, extends it to beta2, makes the f exponent independent of delta explicit, and proves the exact finite liminf and both sequences. The argument uses only displayed scalar equations and elementary integrable-error estimates. P272 is the comparison theorem; P270 and P273 provide consistent notation but are not substitutes for the proofs above. Public model statements are not accepted without this argument and independent exact controls.

No full-plane inverse, full PDE solution, formal Lean verification or early endpoint is claimed. Verification evidence, frozen source inputs and actual-model review status are retained in verification/.
