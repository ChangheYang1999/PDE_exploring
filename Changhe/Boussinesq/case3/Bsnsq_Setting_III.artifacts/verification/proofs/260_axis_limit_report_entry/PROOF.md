# Audit of the proposed report entry 4.44

## Claim, inputs and dependencies

The finite audit claim is that the frozen preview makes exactly the six declared Z edits, adds one specified Table 8.1 row and one timeline entry, and otherwise preserves the frozen report. Its new mathematical statement and proof must be valid with their stated restrictions. This claim concerns the frozen preview, not an actual insertion or a later version of a changing report. The files are registered in verification/freeze.json.

The main mathematical dependency is P257, research/257_nonzero_axis_ratio_limit/PROOF.md, with its 42 exact controls. The consequence concerning a constant third ratio on all of J also uses the independently proved P242 theorem. The class A remark uses the previously audited derivative bounds of report 4.37(5). The argument for the new claim is given below. No lead or numerics code is executed in this audit.

## Proof of the mathematical statement

Let beta>2. Let W, Theta and Omega be smooth on R2 with divergence 2beta, negative curl Omega, both thermal and vorticity transport equations, W(0)=0, W=beta X+o(|X|), the stated x parities, zero axis temperature, and center temperature a0 x2 with a0 nonzero. Let J be the component containing zero on which T(y)=Theta_xx(0,y) is nonzero. Put A=2a0, rho=sqrt(A/T), R(y)=integral_0^y rho, b=W2(0,y), and d=(3beta+2)/2.

Orient an infinite end positively by the reflection Wnew=Sy W(Sy X), Thetanew=-Theta(Sy X), Omeganew=-Omega(Sy X), where Sy(x,y)=(x,-y). This preserves all equations, maps J to -J, and sends A to -A and I(y) to -I(-y), where I=Theta_xxxx/T2. Keep either sign of A. The reflection cannot independently normalize both the end and that sign.

The x2 thermal coefficient is bT'+(3beta+2-2b')T=0. Substituting T=A/rho2 gives (rho b)'=d rho and b=dR/rho, since b(0)=R(0)=0. Thus b>0 for y>0, and sublinearity gives b/y tending to beta. Integrating logarithmic derivative bounds from R'/R=d/b and then using rho=dR/b gives

    c y^(gamma-epsilon) <= rho(y) <= C y^(gamma+epsilon),
    gamma=1/2+1/beta,

for every sufficiently small positive epsilon. In particular rho tends to infinity and has a positive minimum on the positive half-axis. No asymptotic limit is differentiated.

Let v=W2_xx(0,y)/2 and eta=Omega_x(0,y). Divergence gives W1=(2beta-b')x-v'x3/3+O(x5), and negative curl gives eta=-b''-2v. The x coefficient of vorticity transport gives

    b(rho eta)'+(beta/2)rho eta=A/rho.

The backward orbit from any positive axis point stays in the compact segment joining it to zero. Because b is positive except at zero, that orbit exists for all negative times and tends to zero. Multiplication by exp(beta s/2) and integration give

    r(y)=rho(y)eta(y)
        =A integral_-infinity^0 exp(beta s/2)/rho(y(s)) ds.

The initial term vanishes by boundedness on this particular compact orbit. The positive minimum of rho then gives |r|<=2|A|/(beta min rho). This bound does not require A>0.

Put Q=Theta_xxxx=A2 I/rho4. The x4 coefficient of thermal transport is

    4(2beta-b')Q-8Tv'+bQ'+12vT'=(beta-2)Q.

Substitution and one integration by parts on a finite interval give

    rho3 v=c2+(A/8)[d R I-h integral_0^y rho I],
    h=(beta+6)/2, c2=v(0).

If I tends to L nonzero, positive-weight integration gives integral_0^y rho I=LR+o(R). To justify this without controlling I', split the integral at a point after which |I-L| is small, divide by R tending to infinity, and let that upper bound tend to zero. It follows that

    v=(A(beta-2)L/8)R/rho3+o(R/rho3).

The leading sign is sign(A L). Also R/rho3=b/(d rho2)>=c y^(-2/beta-2epsilon), while |eta|<=C y^(-gamma+epsilon). Choose 3epsilon<(beta-2)/(2beta). The eta term is then lower order. With sigma=sign(A L) and p=2/beta+2epsilon<1, one obtains sigma b''<=-c y^(-p) for all sufficiently large y. Integrating twice from a fixed point gives sigma b(y)<=C y-c y^(2-p). Since 2-p>1, this contradicts b/y tending to beta. Hence a finite limit of I must be zero.

A constant I on a tail is therefore zero. If I is constant on all of an unbounded J, then Theta_xxxx vanishes on J; P242 then implies that I3 cannot be constant on J. Tail constancy alone does not give that I3 conclusion. For a representation Theta(x,y)=H(x/sigma(y)) on a neighbourhood of the axis over an infinite tail K contained in J, one has T=H''(0)/sigma2 nonzero and I=H''''(0)/H''(0)2. Thus H''''(0) nonzero is excluded. Positivity of sigma and the representation imply its smoothness from sigma=sqrt(H''(0)/T); no additional sign normalization is needed.

For class A, the previously proved bounds give |Theta_xxxx|<=C |y|^(-3-2/beta) and |T|>=c |y|^(-1-2/beta-2epsilon). Thus |I|<=C |y|^(-1+2/beta+4epsilon), which tends to zero for 4epsilon<1-2/beta. This observation is not used in the theorem above. The theorem leaves beta=2, bounded J, ratios without a limit and ratios tending to zero open. It does not decide general B2 existence.

## Proof of the finite preview predicate

Parse the six declared Z sections. Insert Z1 at the unique end-of-4.43 anchor. Apply each quoted old/new replacement exactly once for Z2 through Z6. Insert exactly the specified 4.44 table row. Preserve every old timeline entry and add exactly the declared new entry. Comparing the complete normalized resulting string with the frozen preview proves that there are no other substantive report edits. Normalization removes whitespace only, not mathematical symbols or words.

Check the displayed coefficient changes against the identities above. In particular B=A2 I/6 gives Q=6B/rho4 and the coefficient of x4 in Theta is B/(4rho4). The integrated constant-I coefficient is 3alpha B/(2A), where alpha=(beta-2)/2. Verify the signed reflection, the distinction between a tail and all of J, the exponent gap and the class A bound. Audit labels and entry times remain placeholders and require a separate actual-insertion audit after the lead fills them.

The initial proof was written before these new checks; its readability revision is preserved alongside it. The exact results, any failures, input hashes and dates are recorded in verification. No Lean or Lake verification is authorized or claimed.
