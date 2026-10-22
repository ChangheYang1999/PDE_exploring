# Independent audit of the 4.45 two-sign power-restriction entry

## Exact verification claim

This packet checks the lead's frozen v2 report entry and entire report preview, based on the actual report with SHA256 0a39b96269adabce98b55b2b51150e9ed085aea305af1a176731c89db03b6e3e. A CONFIRMED verdict means that the inserted mathematics agrees with the independently proved P263 theorem and P261 positive-sign argument, its hypotheses and limitations remain explicit, all declared replacement sentences and table/timeline attributions are accurate, and no undeclared mathematical change appears in the preview. It says nothing about an uninspected later insertion or a complete B2 endpoint.

## Mathematical statement and hypotheses

For a smooth moving-center B2 field with x reflection, Theta(0,y)=0, Theta_xx(0,0)=A=2a0 nonzero, div W=2beta, the defining thermal and vorticity equations, the curl identity, W(0)=0 and W-beta X=o(|X|), let beta>=2. On the connected component J containing zero where T=Theta_xx(0,y) is nonzero, define I2=Theta_xxxx(0,y)/T(y)^2 and m=1-2/beta. At each infinite end of J, for every s>-m,

    liminf |y|^(-s)|I2(y)|=0.

This gives the nonzero-power restriction q<=-m, and, when beta>2, excludes every nonzero extended-real limit. A monotone tail therefore has limit zero. At beta2 only s>0 is covered. No statement concerning arbitrary pointwise decay, critical equality, bounded J, any full profile or a physical inverse follows.

## Independent complete proof

The complete independently checked proof follows verbatim from P263. It is included here so the result is standalone and does not rely on the lead's summary. P263's original physical coefficients and both multiplier slack identities were checked independently, and its completed Opus475 review was adjudicated. Those stored checks bind that proof; the new consumer checks are for the report's notation and scope.

# Both signs of supercritical axis ratios

## Statement, hypotheses and scope

Let beta>=2. Let smooth real fields W=(W1,W2), Theta and Omega on R2 satisfy

    div W=2 beta,  Omega=partial_y W1-partial_x W2,
    W(0)=0,  W(X)=beta X+o(|X|) uniformly as |X| tends to infinity,
    W.grad Theta=(beta-2)Theta,
    W.grad Omega+Omega=Theta_x.

Assume W1 and Omega are odd in x, W2 and Theta are even in x, Theta(0,y)=0, and Theta(x,y)=a0 x^2+O(|X|^3) at0, where a0 is nonzero. Put T(y)=Theta_xx(0,y), A=T(0)=2a0, and let J be the component containing0 of {T!=0}. Define

    I(y)=Theta_xxxx(0,y)/T(y)^2,   m=1-2/beta.

At each infinite endpoint of J, for every s>-m,

    liminf |y|^(-s)|I(y)|=0.                                      (1)

Equivalently, neither AI>=c|y|^s nor AI<=-c|y|^s can hold on a complete tail for c>0. A nonzero power asymptotic I=L|y|^q(1+o(1)) therefore requires q<=-m. If beta>2 and I has an extended-real limit, that limit is zero. Eventual monotonicity in particular implies I tends to zero. At beta2 the theorem only applies to s>0; it does not exclude nonzero finite limits or subpower divergence.

These are necessary restrictions from the displayed equations. They do not settle arbitrary oscillatory behavior, the critical exponent s=-m or its attainability, bounded J, the canonical inverse constraint, or full B2 existence/nonexistence. The velocity hypothesis is essential. No additional derivative bounds at infinity or asymptotic regularity of I are assumed. Smoothness is used only for finite differentiations and ordinary differential equations on compact intervals; no analytic Taylor series is assumed.

## Axis identities and tail bounds

We prove the assertion at the positive infinite end. Then [0,infinity) is contained in J. Set

    b=W2(0,y), v=W2_xx(0,y)/2, eta=Omega_x(0,y),
    d=(3 beta+2)/2, kappa=(beta+6)/2,
    gamma=1/2+1/beta, rho=sqrt(A/T)>0, R(y)=integral_0^y rho.

The square root is positive because T has the sign of A throughout J. At0, rho=1. Divergence and parity imply W1_x(0,y)=2beta-b'. The second-order thermal coefficient gives

    bT'+(3beta+2-2b')T=0.

After substituting T=A/rho^2, this becomes (rho b)'=d rho. Since b(0)=0, integration on [0,y] gives

    rho b=dR,    b=dR/rho>0 for y>0,    R'/R=d/b.                  (2)

The assumed velocity asymptotic gives b(y)/y -> beta. Integrating the last identity, and then using rho=dR/b, proves that for every epsilon>0, after increasing the starting point and adjusting positive constants,

    c y^(gamma-epsilon)<=rho<=C y^(gamma+epsilon),
    c y^(gamma+1-epsilon)<=R<=C y^(gamma+1+epsilon).                (3)

Here d/beta=gamma+1. Derivatives of b/y -> beta have not been taken.

The curl and the first-order vorticity coefficient give

    eta=-b''-2v,
    b eta'+(2beta+1-b')eta=T.

For r=rho eta these reduce to

    b r'+(beta/2)r=A/rho.                                         (4)

On a tail [Y,infinity), define mu=exp(integral_Y^y beta/(2b)). From b/y -> beta, mu lies between positive constants times y^(1/2-epsilon) and y^(1/2+epsilon). Variation of constants in (4) yields

    r(y)=mu(y)^(-1)[r(Y)+A integral_Y^y mu/(b rho)].

The integrand has absolute value at most C y^(-1-1/beta+2epsilon). Choose 2epsilon<1/beta. Its integral converges, so

    |r|<=C y^(-1/2+epsilon),
    |eta|<=C y^(-1-1/beta+2epsilon).                              (5)

No sign of A or r is needed for this estimate. All finite initial data are absorbed into C.

For D=Theta_xxxx(0,y), Taylor coefficients of order four in the thermal equation give

    4(2beta-b')D-8T v'+bD'+12vT'=(beta-2)D.

Indeed W1=(2beta-b')x-v'x^3/3+O(x^5), W2=b+vx^2+O(x^4), and Theta=Tx^2/2+Dx^4/24+O(x^6) on compact y intervals. Substituting D=A^2 I/rho^4, using (2), differentiating and integrating only on the finite interval [0,y] gives

    rho^3 v=c2+(A/8)(dRI-kappa G),
    G(y)=integral_0^y rho I,     c2=v(0).                         (6)

For detail, differentiation of the right hand side is
A[(d-kappa)rho I+dRI']/8=A[(beta-2)rho I+dRI']/8, exactly the substituted fourth-order equation. The integration constant is v(0) since rho(0)=1 and R(0)=G(0)=0. There is no integration by parts over an infinite interval.

On the tail define positive h and P, and real E,H,f,Q, by

    h=exp(integral_1^y kappa/b), H=AG/h,
    P=rho^3/(b h), E=b'-beta,
    f=eta+2c2/rho^3, Q=H+4PE.

The lower endpoint1 may be replaced by any positive point without changing the argument. Equations (2) and (6) yield

    2v=2c2/rho^3+H'/(4P),
    P'/P=-4E/b,
    E'=-f-H'/(4P),
    Q'=-16PE^2/b-4Pf,       Q=H-bP'.                            (7)

For example 3d-kappa=4beta, so differentiating log P gives
[3(d-b')-b'-kappa]/b=-4(b'-beta)/b. The square in Q' comes from4P'E. These identities hold exactly, with either sign of A.

Logarithmic integration of h'/h=kappa/b and (3) give

    c y^(kappa/beta-epsilon)<=h<=C y^(kappa/beta+epsilon),
    c y^(-4epsilon)<=P<=C y^(4epsilon).                           (8)

We used 3gamma-1-kappa/beta=0 and b comparable to y. Also

    P/rho^3=1/(b h)<=C y^(-1-kappa/beta+epsilon).

Together with (5), this shows Pf is absolutely integrable if6epsilon<1/beta. In particular Q has an upper bound by (7). The same estimates imply y f ->0; for the constant term this uses1-3gamma<0, and for eta it uses2epsilon<1/beta.

Fix s>-m and delta=s+m>0. We can and do choose epsilon positive so small that

    6epsilon<1/beta, 6epsilon<delta,
    s+gamma+1-epsilon>0, 1-3gamma+3epsilon<0.                     (9)

These are compatible since s+gamma+1=delta+kappa/beta>0. Estimates (3), (5) and (8) remain available with that same epsilon.

If AI>=c y^s eventually, positive-weight integration gives

    AG>=c1 y^(s+gamma+1-epsilon),
    H>=cL y^nu,        nu=delta-2epsilon>4epsilon.                (10)

The constants c1,cL are positive. To justify the first inequality, integrate the lower bound rho AI>=c' y^(s+gamma-epsilon) from a fixed tail point to y; by (9) its power integral diverges, so the fixed initial part of AG is negligible. If AI<=-c y^s, precisely the same proof applied to -AG gives Z=-H>=cL y^nu. This argument allows negative s and uses no derivative or monotonicity of I.

## Exclusion of the positive sign

Under the first alternative in (10), the upper bound Q<=C and Q=H-bP' imply bP'>=c y^nu eventually. As b<=C y, this gives P'>=c y^(nu-1). Its finite integration yields P>=c' y^nu for large y. This contradicts P<=C y^(4epsilon) because nu>4epsilon. Thus the positive alternative is impossible.

## Exclusion of the negative sign

Assume instead AI<=-c y^s on a tail, and put Z=-H. Then Z>=c y^nu with nu>0. Use t=log y and a dot for d/dt. Set B(t)=b(e^t)/e^t, so B->beta and

    E=dot B+B-beta.

Since H'=-Z', (7) and G'=rho I give

    dot Z=4P(dot E+yf),
    dot Z+(kappa/B)Z=-A y rho I/h>=0.

Consequently

    dot E>=-kappa Z/(4BP)-yf.                                   (11)

The sign in (11) is indispensable; an upper bound on Q alone would not give the negative case.

Set theta=nu/4>0, after choosing epsilon and nu above. Choose a fixed constant B0<beta sufficiently close to beta, then a sufficiently late tail on which B>B0. Thus epsilon, nu, theta, B0 and the final tail are chosen in that order. Define

    w=(B/B0)^4, Pstar=P w,
    lambda=-4(B-beta)/B, chi=kappa(w-1)/B.

We may choose B0 and the tail so that

    0<chi<theta/2,      |lambda|<theta/2.                        (12)

Indeed chi tends to kappa[((beta/B0)^4)-1]/beta, which can be arbitrarily small and positive, and lambda tends to0. Since B0 is fixed, all these functions are smooth on the chosen tail. Direct differentiation, without differentiating a limiting asymptotic, gives

    dot Pstar/Pstar=lambda.                                    (13)

One way to verify (13) is Pstar=rho^3 b^3/(h B0^4 y^4), and (rho b)'=d rho. Its logarithmic derivative is(3d-kappa)/B-4=4beta/B-4. Thus Pstar<=C exp(theta t/2). The uncontrolled derivative dot B has canceled exactly.

Set M=Z-4Pstar E. Since Pstar>P, multiplying (11) by the negative quantity -4(Pstar-P) reverses its inequality. Substitution of dot Z and (13) then yields

    dot M<=chi M+4Pstar(chi-lambda)E+4Pstar y f.                  (14)

For clarity, the coefficient of Z before replacing Z by M+4Pstar E is kappa(Pstar-P)/(BP)=chi; the yf contributions combine to4Pstar yf.

Introduce the following explicit smooth function near beta:

    F(B)=kappa(B^4-beta^4)/B0^4+16(B-beta)
         -4(kappa+4beta) log(B/beta).

It has F(beta)=0 and F'(B)=4(chi-lambda). Put N=M-Pstar F(B). Differentiating, using E=dot B+B-beta in (14), and canceling dot B exactly, gives

    dot N<=chi N+Pstar{(chi-lambda)[F(B)+4(B-beta)]+4y f}.        (15)

The expression in braces is bounded because B->beta, F is smooth near beta, and yf->0. Hence dot N<=chi N+C Pstar. Scalar variation of constants and (12)-(13) imply

    N(t)<=C(1+t)exp(theta t/2)<=C_theta exp(theta t)

after moving the fixed lower time to0 if necessary. No sign of N is assumed: bound its initial value in absolute value in the scalar integrating-factor formula. Since F(B) is bounded, the same upper bound holds for M.

Recall theta=nu/4. The identity4Pstar E=Z-M and the lower bound Z>=c exp(nu t) give4Pstar E>=c exp(nu t)/2 on a late tail. Since Pstar<=C exp(theta t), this forces

    E>=c' exp(3nu t/4).

It follows that dot B=E-(B-beta)>=1 eventually. Finite integration contradicts B->beta. This excludes the negative alternative for all beta>=2.

## Absolute value, reflection and consequences

If (1) failed, nonnegativity would imply |I(y)|>=c y^s on a complete tail for some c>0. Continuity then prevents I from changing sign there, since a sign change would pass through0. Because A is a fixed nonzero real number, one of the two excluded signed alternatives would hold. This proves (1) at the positive end.

For a negative infinite end, define

    Wtilde(x,y)=(W1(x,-y),-W2(x,-y)),
    Thetatilde(x,y)=-Theta(x,-y),
    Omegatilde(x,y)=-Omega(x,-y).

Direct differentiation verifies every displayed field equation, parity and asymptotic. It sends A to -A, J to -J, and I(y) to -I(-y). Therefore |I| is unchanged under the reflected parameter and the positive-end result applies. No sign normalization of A has been imposed.

A nonzero power with q>-m would contradict (1) with s=q. If beta>2, then m>0 and s=0 is allowed, so (1) gives a sequence on each infinite end with I tending to0. Any extended-real limit must therefore equal0. An eventually monotone function has an extended-real limit, which proves the last consequence.

## Dependencies and verification status

The independent derivation uses the equations stated above, finite Taylor coefficients, positive integrating factors and elementary one-dimensional integration. P258 and P261 supplied earlier separately checked axis estimates and the positive-sign restriction, all rederived here. The additional multiplier was proposed in the lead's separate z445_tails referee answer; it has been rederived here with an explicit primitive F and a complete scalar-inequality argument. This proof was written and inspected before writing or running the new exact controls. Its algebraic checks and independent-model consultation, including any availability limitation, will be recorded in verification/. Numerical checks cannot replace its analytic argument. No formal build is authorized or claimed.


## Report-comparison argument

Split the proposal at its six numbered Z sections. Z1 is the new theorem and proof outline. In the normalized base text, insert it after the unique final line of 4.44, with the two prescribed audit-description substitutions. Each of Z2 to Z6 has one quoted old sentence and one new sentence; replace the old exactly once. Insert precisely the advertised table row after the unique 4.44 row. Add precisely the advertised new chronology entry, retaining all 147 old entries and their text. These operations determine a unique normalized expected preview. Equality with the full frozen preview proves there is no additional change except line reflow. A mismatch leaves that comparison OPEN, regardless of mathematical correctness elsewhere.

Each mathematical expression in the inserted outline is checked against the physical derivation above. In particular, the report's u,u0,P1 are the proof's B,B0,Pstar. Their definitions give P1dot/P1=-4(u-beta)/u. The exact primitive F satisfies F'=4(chi-lambda), and the slack in each displayed multiplier inequality is -4P(w-1) times a nonnegative slack. Thus no inequality sign changes under the renaming. The integration-factor bound does not presume a sign for N. At beta2 the same proof applies; beta>2 is only used for s=0>-m when deducing zero extended-real limits. All other consequences of 4.44 still follow using its already established auxiliary results.

The P258, P261 and P263 attributions and exact-control counts are checked against stored evidence, and the A154 attribution against the public referee answer, not an inferred model endorsement. Timeline arithmetic does not create a new audit. Actual report insertion requires a fresh file comparison.

## Dependencies and evidence

This proof was written before new consumer code. The formal_sources directory records that no Lean or Lake build is permitted or claimed. Frozen input hashes, consumer checks and publication status belong in verification/. The original prompt and all standing machine restrictions remain in force.
