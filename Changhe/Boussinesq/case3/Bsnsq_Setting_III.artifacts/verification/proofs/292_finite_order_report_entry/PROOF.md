# P292. Complete finite-order endpoint report entry

## Exact statement and scope
This audit concerns lead item4.51 textv1 and previewv1c on the already checked placeholder4.50 preview. It certifies the finite-order theorem of P286 and checks the complete declared report transformation. It does not certify an actual adoption until a separate fresh comparison. The four equations, notation, hypotheses, complete proof and local realization are included below verbatim from our independently proved P286, including its corrected translated polynomial. The finite symbolic controls supplement that proof.

## Two necessary wording corrections
The theorem on an endpoint of the component J containing0 has epsilon=sign(y_*). For arbitrary local data on the side y=y_*-epsilon s, epsilon is determined by the side, not by the coordinate y_*. A translation of a local solution changes sign(y_*) without changing the side or the equations. For example take y_*=1, epsilon=-1, p=2 and b=-a(y-1)^2 on y>1, with T,eta,D as constructed below. This is an attractive local endpoint, with b negative although sign(y_*) is positive. Thus statement(c), which permits either side, must explicitly replace sign(y_*) by epsilon in conclusion(a). The profile conclusions(a),(b) are unchanged.

The leading coefficient of s^2D/T depends only on beta,p. The rate of A I_2 does not. For the exact monomial B=a s^p, write L=3beta+2, d=L/2 and gamma=(3d/beta)p(p-1)>0. The exact T and proved K asymptotic give

    A I_2=-(A gamma/(C a^2)) s^(-2p-2) exp(L t(s))(1+o(1)),
    t(s)=[s^(1-p)-s0^(1-p)]/[a(p-1)].

Since A/C>0, this is negative. Its exponential rate depends on a. At p=2, a=1 versus a=2, the ratio of the magnitudes tends to infinity, after any fixed positive normalizations. Thus the Summary clause 'with the rate fixed by beta and p' must refer explicitly to s^2D/T, not to A I_2. These are presentation corrections to a valid theorem; general B2 remains OPEN.

## Verification design
Freeze the full base report, candidate text, candidate preview, readonly driver, timeline lists, A166public answer and proof, and the P286 proof/control ledger. Never execute or import lead code. Independently concatenate normalized paragraphs at the unique anchor, perform precisely the three declared replacements, insert the table row and reconstruct the complete timeline. Check every original table row and every previous timeline entry, plus equality of the entire preview modulo whitespace. Treat the two mathematical wording requirements separately, preserving the initial candidate and initial results. Verify factorials, coordinate signs, the ratio and scaled equations, reflection covariance, monomial rate and translated counterexample by own exact symbolic calculations. Report complete proof audit separately from control counts. A166 is Astra, not an Opus consultation; an actual separate Opus5.5 call will review the two findings and theorem scope.

## Complete independent mathematical proof (P286)

# P286. Universal ratio law at a finite-order axis endpoint

## Exact statement
Fix beta>0 and set L=3beta+2, M=2beta+1 and d=L/2. Let b,T,eta,v,D be real C-infinity functions on a neighborhood of y_*. They satisfy the four axis equations

    b T'+(L-2b')T=0,
    b eta'+(M-b')eta=T,
    eta=-b''-2v,
    b D'+(7beta+2-4b')D=8v'T-12vT'.             (1)

A prime in (1) is a y derivative. Suppose b has a zero of finite order p>=2 at y_*, and T is nonzero on one adjacent punctured interval. Write that side as y=y_*-epsilon s, with epsilon=+1 or -1 and 0<s<s0. Then necessarily

    b(y_*-epsilon s)=epsilon B(s),
    B(s)=a s^p(1+O(s)), a>0,                  (2)

where the remainder and its derivatives come from a smooth Taylor expansion. In particular the forward axis flow approaches the endpoint from this side. The functions T,eta,D are flat at y_*. On the punctured interval, K=D/T satisfies

    K(s)=-(3d/beta)p(p-1)s^(-2)(1+o(1)).       (3)

For any fixed nonzero A with A/T>0 on that side, define I_2=D/T^2. Then A I_2 tends to negative infinity as s decreases to zero. The coefficient in (3) is independent of the nonzero leading coefficient a of b.

The hypotheses are local axis hypotheses. They do not assert that these functions extend to a full B2 profile or that every finite endpoint has finite order. In particular this result does not cover a simple zero or a zero of infinite order. It applies to every beta>=2 in the research setting, but the local proof works for all beta>0.

## Proof of flatness and the endpoint-approaching sign
Since b(y_*)=b'(y_*)=0, the first equation at the endpoint gives L T(y_*)=0. Suppose the first n-1 derivatives of T vanish. Differentiate the equation n times. Every term other than L T^(n)(y_*) contains either b, b', or a lower derivative of T. It vanishes, so T^(n)(y_*)=0. This proves flatness by induction. Applying the same argument to the second equation, with M>0 and the already flat T, proves that eta is flat. Applying it to the fourth equation, whose zeroth-order coefficient at y_* is 7beta+2>0 and whose right side is flat, proves that D is flat. Smoothness of v is sufficient for the last assertion.

Initially B may have either sign. The first equation in s coordinates reads

    B T_s=(L+2B_s)T.

Since T and B do not vanish on the punctured side, integration gives exactly

    T(s)=C B(s)^2 exp(L integral_(s0)^s du/B(u)), C!=0.       (4)

If B(s)=a s^p(1+O(s)) with a<0, the integral tends to positive infinity at rate s^(1-p)/(|a|(p-1)). Thus the exponential in (4) dominates the polynomial B(s)^2 and |T| tends to infinity, contrary to smoothness. Hence a>0. Shrinking s0 makes B positive. Define

    t(s)=integral_s^s0 du/B(u).

Then t tends to positive infinity and ds/dt=-B. Its leading behavior is t(s)~s^(1-p)/(a(p-1)). Formula (4) becomes T=C B^2 exp(-Lt).

## Exact ratio equation
From now on primes on B, T and eta in formulas involving s denote s derivatives. The coordinate conversion gives b_y=-B', b_yy=epsilon B'', and

    T_s/T=(L+2B')/B,
    eta_s=((M+B')eta-T)/B,
    v=-epsilon B''/2-eta/2.                   (5)

Divide the fourth equation in (1) by T and subtract K times the thermal equation divided by T. This is legitimate at every point of the punctured side, even though T tends to zero. It gives

    -B K_s+(4beta+2B')K=Q(s),                 (6)
    Q=4B'''-6B''(L+2B')/B
      -epsilon[(10beta+8+8B')eta+4T]/B.

To check the signs directly, 8v_y=4B'''+4epsilon eta_s, while -12v T_y/T=-6B''(L+2B')/B-6epsilon eta(L+2B')/B. Insert (5) and use 4M-6L=-(10beta+8). This establishes (6) without an asymptotic approximation.

Put Z=s^2 K. Since ds/dt=-B, equation (6) becomes

    Z_t+[4beta+2B'+2B/s]Z=s^2 Q(s).           (7)

Smooth finite order gives B^(j)(s)=a(p)_j s^(p-j)+O(s^(p-j+1)) for the needed derivatives, with vanishing leading factor when j>p. In particular

    s^2 B''/B -> p(p-1),
    s^2 B''' -> 0,
    s^2 B''B'/B -> 0,
    B' -> 0, B/s -> 0.

The estimate on the third derivative also holds when p=2, since B''' is bounded. Flatness of eta and T gives s^2 eta/B ->0 and s^2 T/B ->0, because division by B loses only the finite power p. Thus the coefficient on the left of (7) tends to 4beta>0 and its right side tends to -6L p(p-1).

For completeness, if z_t+a(t)z=f(t), a(t)->a_*>0 and f(t)->f_*, then z(t)->f_*/a_*. Subtract z_*=f_*/a_* and write the integrating-factor formula from any sufficiently late t1. The initial term decays at least as exp(-a_*(t-t1)/2). If |f-a z_*|<=delta on [t1,infinity), the integral term has absolute value at most 2delta/a_*. As delta is arbitrary, the difference tends to zero. Applying this fact to (7) yields

    Z -> -6L p(p-1)/(4beta)=-(3d/beta)p(p-1),

which is a strictly negative constant. This proves (3). Since T tends to zero and A/T is positive, A I_2=(A/T)K tends to negative infinity. No sign of eta or v is used.

## Sharpness as local smooth axis data
Every p>=2, a>0, epsilon in {-1,1} and beta>0 occurs in local smooth solutions of (1) with nonzero T on the interior side. This demonstrates that the endpoint theorem does not itself rule out these axis data.

Choose B(s)=a s^p for s>0 and take

    t(s)=[s^(1-p)-s0^(1-p)]/[a(p-1)],
    T=C B^2 exp(-Lt), C!=0.

Solve the eta equation in forward time. Since d(log B)/dt=-B', its exact solution with an arbitrary real constant H is

    eta=B exp(-Mt) [H+C integral_0^t B(s(u)) exp(-(L-M)u) du].       (8)

Here L-M=beta+1>0 and B(s(u)) is bounded, so the bracket is bounded. Differentiating the explicit functions and the integral shows that every s derivative of eta is a polynomially bounded factor times exp(-Mt), or a faster decaying exponential in t. Each derivative of T has the same property with exp(-Lt). Because t is a positive constant times s^(1-p) plus a constant, these functions and every derivative tend to zero.

Set v as in (5). Solve the nonsingular first-order equation (6) from any fixed interior point with arbitrary finite K there. Equation (7), whose forcing has the same limit just established, proves K=O(s^-2) and the asymptotic (3). The explicit Q and every s derivative of Q have at most polynomial growth in 1/s: B is a monomial, and the terms involving T and eta remain flat after any finite number of divisions by powers of s. Rewriting (6) as K_s=[(4beta+2B')K-Q]/B and differentiating inductively shows that every derivative of K has at most polynomial growth. Therefore D=T K and all its derivatives tend to zero.

Continue b across y_* by the signed polynomial epsilon a[epsilon(y_*-y)]^p. On the other side set T=eta=D=0 and v=-b''/2. The flatness just proved gives smooth joins; v also joins smoothly. All four equations hold on each open side and hence at the endpoint by continuity. The functions need not retain compact support, center normalization, a global canonical inverse or the remaining axis equations. This is only a local realization of the four displayed equations.

## Dependencies and verification scope
The four equations are the physical second thermal, first vorticity, curl and fourth thermal axis identities. Their derivation and relation to the original B2 equations are in P273 and P278. The present proof independently derives (4)-(8) and the limiting argument, rather than assuming A161's proposed generalization. A161 D5(i) suggested examining arbitrary finite order; its subsequent infinite-order and simple-end examples are separate claims not certified here. Exact symbolic checks are supplementary to the proof. No Lean or formal build is used.

Written 2026-10-22T05:48:21.839955+00:00 before controls.

Translation formula corrected 2026-10-22T05:51:34.081781+00:00 after actual Opus 496 review, before corrected controls. The original proof is preserved in verification/PROOF_before_translation_correction.md.

P292 audit written 2026-10-22T06:20:38.832904+00:00 before controls.
