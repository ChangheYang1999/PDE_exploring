# Refined energy and weighted transport on one invariant set

Status: A435 CONFIRMED at the conditional hypotheses below; broad route closure remains OPEN as A436. The source is the Theory Agent A  REFINED_BASIN submission. The conclusions are conditional on Dini derivative decay. They do not exclude a profile or determine a sign for the basin pressure work.

## 1. Exact setting and inputs

Let U in C2(R3;R3) and P in C1(R3) satisfy

    (1-c)U + B.grad U + omega JU + grad P = 0, div U=0,
    A=cI-omega J, B=Ay+U, J(y1,y2,y3)=(-y2,y1,0),
    2/5<c<1/2, omega in R.

Assume U is bounded, U(R .) tends to zero in distributions as R tends to infinity, and

    integral_1^infinity m(r) dr/r < infinity,
    m(r)=sup_{|y|>=r} ||DU(y)||.                                (D)

Boundedness alone is not the large-scale normalization assumption. Fix the additive pressure constant by P=P_can, the canonical Riesz pressure of U tensor U. The canonical-gradient theorem A031 justifies this choice for these hypotheses; a different constant must be subtracted before using the decay assertions below.

Set

    k=(1-c)/c in (1,3/2), a=1-2c=c(k-1),
    alpha=3-2k=(5c-2)/c in (0,1),
    gamma=(5c-2)/2=c alpha/2 > 0,
    q=|U|^2/2, Omega=curl U, h=U.Omega,
    H=P+q+(Ay).U.

Let Phi_s be the complete B flow. A209 supplies the continuous proper scattering map S, its compact null zero fibre K, and the volume-preserving C1 diffeomorphism

    S: R3 minus K -> R3 minus {0},
    S(Phi_s y)=exp(sA)S(y), |S(y)-y|<=M/c, M=sup|U|.

The set K is carrier-invariant. A210 and its asymptotic supplements supply V and Wtilde=curl V, continuous off zero, with

    V(exp(sA)z)=exp(-(1-c)s) Q_s^T V(z),
    Wtilde(exp(sA)z)=exp(-s) Q_s^T Wtilde(z),
    Q_s=exp(omega sJ), DS Omega=Wtilde composed with S,
    |U(y)|<=C(1+|y|)^(-k), |Omega(y)|<=C(1+|y|)^(-k-1),
    exp((1-c)s) Q_s U(Phi_s y) -> V(S(y)).                      (1)

Also DU is bounded. A354 gives

    |P(y)|<=C(1+|y|)^(-2k) log(2+|y|).                         (2)

The confirmed Bernoulli and helicity tail formulas give, uniformly on an escaping unit section,

    exp(a s) H(Phi_s y) -> tau(S(y)), tau(z)=(Az).V(z),
    exp((2-c)s) h(Phi_s y) -> htilde(S(y)), htilde=V.Wtilde.    (3)

These are conditional inputs already proved in the campaign. They are not derived here from mere velocity decay. The exact Euler identities used below are

    Bq+2(1-c)q=-f, f=U.grad P,
    BH+aH=a(P-q),
    Bh+(2-c)h=Omega.grad(q-P),
    div(Bh+Omega(P-q))=-2a h.                                  (4)

For a measurable set D invariant under Phi_s for every real s, put

    C_D=S(D minus K), sigma_D=C_D intersect S2,
    E_D(r)=integral_{D intersect {|S|<r}} |U|^2,
    L_D=(1/alpha) integral_{sigma_D}|V|^2 dA.

The null part D intersect K never affects these integrals. Measurability of sigma_D follows in flow coordinates: the pullback of C_D is R times sigma_D, and Fubini provides a measurable section; exact invariance makes every section the same. No smooth boundary of D is required.

## 2. Coordinates, backward boundedness, and the section identity

Every z!=0 is uniquely exp(sA)z1 with z1 in S2 and s=log|z|/c. Since (Az1).z1=c, Lebesgue measure in these coordinates is

    dz=c exp(3cs) ds dA(z1).

The same holds for dy after applying S inverse. Write y_s(z1)=S inverse(exp(sA)z1)=Phi_s(S inverse(z1)). Thus D minus K corresponds exactly to R times sigma_D.

Every backward carrier orbit is bounded. Indeed B.y>=c|y|^2-M|y|, so the backward flow is strictly inward outside any fixed ball of radius larger than M/c. An orbit eventually enters each such larger ball. Finite entry into the exact closed M/c ball does not follow from this estimate and is not used.

Let F be C1 on R3, lambda>0, G=BF+lambda F, and let w1 be bounded measurable on S2. Extend it by

    w(exp(sA)z1)=exp((lambda-3c)s)w1(z1).

Then, for r>0,

    integral_{D intersect {|S|<r}} w(S)G
      = c r^(lambda/c) integral_{sigma_D} w1(z1) F(y_log(r)/c(z1)) dA.   (5)

To prove this, use the coordinates above. The integrand becomes the s derivative of exp(lambda s)F(y_s), multiplied by c w1. Its lower endpoint is zero because the backward orbit is bounded and lambda>0. Absolute integrability on the finite S ball follows from boundedness of G there and |w(z)|<=C|z|^(lambda/c-3); the exponent is greater than -3. This justifies Fubini and all endpoint operations.

If F has escaping rate lambda_F with the uniform power bound needed for domination, the right side of (5) is

    c r^((lambda-lambda_F)/c)
      [integral_{sigma_D}w1 Ftilde dA + o(1)].                 (6)

This classifies the particular section identity (5) into equal-rate, lower-rate, and higher-rate cases. It is not a classification of all possible transport estimates or a proof that every higher-rate identity has a finite constant term.

## 3. Pressure work and an absolute-convergence strengthening

We prove

    f in L1(R3), integral_R3 f=0,
    grad P and grad q in Lp(R3) for every 1<p<infinity.         (7)

From (1), Omega is in Lp for p>3/(k+1), and U is in Lp for p>3/k. The Biot-Savart uniqueness argument already verified in A165/A166 identifies U with the Biot-Savart velocity. One direct uniqueness check chooses 3/(k+1)<p<3. The Biot-Savart field is in the finite space L^(3p/(3-p)); its difference from U is an entire harmonic distribution in a sum of two finite Lp spaces, hence zero by the harmonic mean-value estimate. Standard singular-integral differentiation now gives

    DU in Lp for p>3/(k+1).

For any fixed p>1 choose p1>3/k and p2>3/(k+1) with 1/p1+1/p2=1/p. Such choices exist because k/3+(k+1)/3>1. Holder gives derivatives of U_i U_j, and also grad q, in Lp. Canonical Riesz transforms commute with derivatives in distributions and are bounded on Lp for 1<p<infinity. Therefore grad P is in the same spaces.

Choose p1>3/k and p2=p1/(p1-1). Then U in Lp1 and grad P in Lp2, proving f in L1. Since f=div(PU), the divergence theorem on the ordinary radius-R ball and (1)-(2) give flux O(R^(2-3k) log R), tending to zero. L1 convergence proves the zero integral in (7).

There is a useful improvement to the submitted helicity section formula. The vector field

    Z(y)=|S(y)|^(2k-2) Omega(y)

belongs to L2. Near K it is bounded, since 2k-2>0 and Omega is bounded. At large radius, |S| is comparable to |y| and Z=O(|y|^(k-3)). Its square is integrable because k<3/2. Consequently

    |S|^(2k-2) Omega.grad(q-P) in L1(R3)                       (8)

by Cauchy-Schwarz and (7). No pointwise decay estimate for grad P is needed. The source's exhaustion limit can therefore be strengthened to an absolutely convergent integral.

## 4. Refined energy on every carrier-invariant measurable set

Define, off the null set K,

    Fdef(y)=|U(y)|^2-|V(S(y))|^2.

Then

    Fdef(y)=2 integral_0^infinity exp(2(1-c)s) f(Phi_s y) ds,   (9)
    ||Fdef||_1 <= gamma^(-1)||f||_1,
    e_D:=integral_D Fdef=gamma^(-1)integral_D f.                (10)

First integrate the energy identity in (4) over a finite time interval. Formula (1) gives the limit of its left endpoint expression at positive infinity, proving (9) as an improper integral for every y outside K. For absolute integrability after integration in y, change variables x=Phi_s y. The Jacobian is exp(3cs), and D is invariant. Thus

    2 integral_D integral_0^infinity exp(2(1-c)s)|f(Phi_s y)| ds dy
      =2 integral_0^infinity exp(-(5c-2)s)ds integral_D |f|
      =gamma^(-1)integral_D |f|.

Tonelli proves the bound and almost-everywhere absolute convergence along orbits; Fubini gives (10). The theorem does not claim absolute time convergence on every exceptional individual orbit.

Homogeneity and the section coordinates give

    integral_{D intersect {|S|<r}} |V(S)|^2
      = integral_{C_D intersect B_r}|V(z)|^2 dz
      = L_D r^alpha.                                         (11)

In particular this integral is finite near K, since alpha>0. It follows that

    E_D(r)=L_D r^alpha+e_D+epsilon_D(r),
    epsilon_D(r)=-integral_{D intersect {|S|>=r}} Fdef
      =-gamma^(-1) integral_{D intersect {|S|>=r}}
           [1-(r/|S|)^alpha] f,
    |epsilon_D(r)|<=gamma^(-1)integral_{D intersect {|S|>=r}}|f| ->0.  (12)

For the second remainder formula substitute (9), interchange the absolutely integrable terms, and note that x=Phi_s y transforms |S(y)|>=r into |S(x)|>=r exp(cs). At fixed x the remaining integral is

    2 integral_0^(log(|S(x)|/r)/c) exp(-2gamma s)ds
       =gamma^(-1)[1-(r/|S(x)|)^alpha].

For completeness an exact two-term identity is

    gamma E_D(r)=Pi_D(r)-r^alpha mu_D(r),
    Pi_D(r)=integral_{D intersect {|S|<r}} f,
    mu_D(r)=integral_{D intersect {|S|<r}} |S|^(-alpha)f.        (13)

Apply (5) to q with (lambda,w)=(3c,1), obtaining gamma E_D-Pi_D=c r^3 Q_D(r), where Q_D is the section integral of q. Apply it again with (lambda,w)=(2(1-c),|z|^(-alpha)), obtaining -mu_D=c r^(2k)Q_D. Elimination proves (13).

The assignment e_D is countably additive on disjoint invariant measurable sets because Fdef is L1. Also e_R3=0 by (7). Hence any countable partition into invariant basins and their invariant complement satisfies sum e_D=0, with absolute convergence. No sign of an individual e_D follows.

For D=R3, (12) gives E_S(r)=L r^alpha+o(1). The sets {|y|<r} and {|S|<r} differ only in a shell of fixed width M/c and volume O(r^2). Formula (1) bounds its kinetic energy by O(r^(2-2k)), tending to zero. Thus the ordinary ball energy also satisfies E(r)-L r^alpha ->0. This is a derivation under (D), not an improvement to the decay-only hypotheses of the earlier global energy theorem.

The ordinary ball error can be sharpened under the same hypotheses. Set E_ball(r)=integral_{B_r}|U|^2 and F_ball(r)=integral_{|y|=r}(P+q)U.n. The energy identity gives div(Bq+PU)=gamma|U|^2, while (Ay).n=cr. Hence

    r E_ball'(r)-alpha E_ball(r)=-(2/c)F_ball(r),
    E_ball(r)-L r^alpha=(2/c)r^alpha integral_r^infinity
                              t^(-alpha-1)F_ball(t)dt
                      =O(r^(2-3k)log r).

Indeed F_ball=O(r^(2-3k)log r) by (1)-(2), and -alpha-1+2-3k=-2-k<-1. Integration uses the already proved limit r^(-alpha)E_ball(r)->L. This is a weaker logarithmic version of the previously confirmed global error estimate, not a new decay-only result.

The backward companion also follows directly from the q identity and bounded past orbits:

    q(y)=-integral_{-infinity}^0 exp(2(1-c)s) f(Phi_s y)ds,
    E_D(r)/2=-integral_{-infinity}^0 exp(-2gamma s)Pi_D(r exp(cs))ds.

For the second formula, Fubini is valid before cancellation: on the bounded preimages of the S-ball, f is bounded, and the volume of {|S|<r exp(cs)} is O(exp(3cs)). Thus the integrable negative-time bound is a constant times exp(2(1-c)s).

## 5. Weighted identities and all boundary terms

Taking q,H,h in (5) at their escaping rates gives

    integral_D |S|^(-alpha) f=-(c/2)integral_{sigma_D}|V|^2,     (14)
    a integral_D |S|^(k-4)(P-q)=c integral_{sigma_D}tau,         (15)
    integral_D |S|^(2k-2) Omega.grad(q-P)
         =c integral_{sigma_D}htilde.                         (16)

All three are absolutely convergent. For (14), use (7) outside {|S|<1} and bounded f with alpha<3 inside. For (15), the near-K power k-4 exceeds -3 and the far-field bound is O(r^(-k-4)log r). Formula (16) uses (8). Tail domination follows from (1)-(3).

Let m(z)=z.Wtilde(z), so |m(z)|<=C|z|^(-k) and

    Omega.grad|S|=m(S)/|S|, B.grad|S|=c|S|.                    (17)

Suppose additionally that D is invariant under the complete frozen-vorticity flow. Completeness follows here because Omega is C1 and bounded. Then

    2(k-1) integral_D |S|^(2k-4)m(S)(P-q)
         =c integral_{sigma_D}htilde.                         (18)

To justify integration by parts on an arbitrary D, a compactly supported C1 test psi satisfies integral_D Omega.psi=0 by differentiating the preserved measure of the vorticity flow. Use psi=chi(|S|)|S|^(2k-2)(q-P), with chi vanishing below epsilon and above 2R and equal to one between 2epsilon and R. Its support is compact and disjoint from K. The derivative of chi contributes O(epsilon^(k-1)) near K and O(R^(-1-k)log R) at infinity. The main right integrand is bounded by C|S|^(k-4) near K and C r^(-k-4)log r at infinity. Both are integrable. Formula (8) handles the left side directly by dominated convergence, and (16) proves (18).

Use (5) again with F=H, lambda=a, and w(z)=|z|^(2k-4)m(z). The weight has degree k-4 and the correct twisted homogeneity. It follows that

    a integral_D |S|^(2k-4)m(S)(P-q)
       =c integral_{sigma_D}m tau.                            (19)

Combining (18)-(19) gives exactly the known tail relation

    a integral_{sigma_D}htilde=2(k-1)integral_{sigma_D}m tau.   (20)

Thus this particular core integral identity restates that tail relation. It gives no sign for e_D.

Further lower-rate instances of (5) are

    -integral_D |S|^beta f
      =c(-alpha-beta)/2 integral_D |S|^beta |U|^2,
        -3<beta<-alpha,                                      (21)

    a integral_D |S|^beta(P-q)
      =c(k-4-beta)integral_D |S|^beta H,
        -3<beta<k-4.                                         (22)

All displayed integrals converge absolutely by the powers already given. Equation (21) is strictly positive on its right if U is nonzero on a positive-measure subset of D. For a general measurable D, the phrase "U is not zero on D" must mean this measure-theoretic condition. A nonzero value on a null D is not enough. The function W_D(beta)=-integral_D |S|^beta f is continuous for -3<beta<=0. On a compact beta interval its near-K integrand is dominated by the smallest admissible power, and its far-field integrand by |f|. Thus W_D is positive on (-3,-alpha) when the strict condition holds, W_D(-alpha)=c integral_{sigma_D}|V|^2/2, and W_D(0)=-gamma e_D. These facts alone give no sign between -alpha and 0.

When D is also vortex-invariant, multiplying the last identity in (4) by chi(|S|)|S|^beta gives

    (2a-c beta) integral_D |S|^beta h
       = beta integral_D |S|^(beta-2)m(S)(P-q),
        k-1<beta<2k-2.                                       (23)

For the B flux use integral_D div(B psi)=0, which follows from carrier invariance and its constant Jacobian; B is not divergence free. For the Omega flux use its measure preservation. The inner cutoff errors have orders epsilon^(beta+3) and epsilon^(beta+1-k); the outer errors have orders R^(beta+2-2k) and R^(beta+1-3k)log R. They all tend to zero in the written interval. The main right integrand is locally integrable near K since beta>k-1. This is the sufficient range supplied by the stated bounds, not a necessary integrability condition for every profile. The main left tail is integrable because beta<2k-2.

The cancellation integral_D h=0 at beta=0 is the separate confirmed A302 result. It cannot be obtained by substituting beta=0 into the written proof of (23).

For beta tending to 2k-2 from below, the Abel limit of the left side of (23) is c integral_{sigma_D}htilde. Indeed in section coordinates its tail is c integral exp(-c(2k-2-beta)s)[Hsec(s)]ds, where Hsec(s) tends to integral_{sigma_D}htilde and is bounded. Multiplication by c(2k-2-beta) gives the stated Abel limit; the bounded negative-time part tends to zero. The right side tends by domination to (18). If the signed tail integral is zero, this still proves a zero Abel limit. It does not assert a nonzero-pole divergence in that case.

For the full space, (15) can also be written

    a integral_R3 |S|^(k-4)(P-q)
      =-c omega e3.integral_{B_1}Wtilde.                      (24)

The radial flux of V is independent of radius by div V=0 off zero, but homogeneity scales it as r^(2-k); since k!=2 it is zero. The identity integral_S2 n cross V=integral_B1 curl V is justified by removing a small ball; its inner boundary term is O(r^(2-k)), tending to zero, and Wtilde is locally integrable. These divergence and Stokes formulas also hold at the stated continuous tail regularity: mollify on each fixed annulus, apply the classical formulas, and use uniform convergence of V and of its continuous distributional curl there before shrinking the inner sphere. This proves (24), including its omega sign.

## 6. Physical and gauge scope

With s=-log(T-t), the fluid initially in D intersect {|S|<r} has kinetic energy

    KE_r(t)=1/2 exp(-2gamma s) E_D(r exp(cs)).

Formula (12) therefore gives terminal energy L_D r^alpha/2 and

    KE_r(T-1)-KE_r(T)=[e_D+epsilon_D(r)]/2.

Differentiating the exact finite-r formula with (13) gives d KE_r/ds=-exp(-2gamma s)Pi_D(r exp(cs)). Consequently gamma e_D is the limiting signed loss rate at the reference time s=0, while the pressure force supplies power -gamma e_D. Thus e_D/2 is a signed net kinetic-energy loss as r tends to infinity. It may be negative. The energy difference has a limit although each energy separately diverges when L_D>0. If L_D=0, no divergence assertion is made. Changing the initial reference time to T-exp(-s0) multiplies the limiting constant by exp(-2gamma s0), preserving its sign.

For the A372 gauge v=U-grad F/a, F in C3_c, the carrier B, vorticity, scattering data and leading tail are held fixed as independent fields. The new velocity is not asserted to equal B-Ay or to satisfy incompressibility or momentum. Nevertheless

    e_D^v-e_D=a^(-2)integral_D|grad F|^2
                   -(2/a)integral_D U.grad F.                (25)

If supp F is contained in one open basin D1, incompressibility of the original U gives integral_D1 U.grad F=0. The chosen basin constant increases by a^(-2)integral|grad F|^2, and every disjoint basin is unchanged. This tests the expansion-with-an-unspecified-constant alone. It does not test the full Euler pressure-work identity for the new field, and it violates the original global zero-sum law. Neither arbitrary signed changes nor independent realizability of basin constants by Euler profiles is proved.

The identities above establish one additive pressure-work constant per invariant set and its global cancellation. They do not show that cancellation is the only possible restriction, that no other transport argument can work, or that pressure work is unrelated to helicity in every possible theorem. The broader route-closure assessment remains open.

## 7. Verification and dependencies

The full submitted proof was read, and every formula above was independently derived by hand. No numerical or symbolic computation was needed: rerunning an exponent-substitution script would not address the boundary and scope questions. Dependencies are the previously confirmed scattering and tail theorems A209-A210; pressure normalization A031 and quadratic bound A354; the Bernoulli/helicity tail package A295-A296, A302, A360-A363; the exact Euler identities; and the elementary Lp Biot-Savart uniqueness argument A165-A166. Their needed hypotheses are explicitly repeated above.

The source and relevant proof inputs are pinned in the team records. The Theory Agent A  focused review at 2026-11-03 03:10Z read this proof in full and checked the Holder exponents, null-core change of variables, arbitrary measurable invariant sets, six cutoff orders, Abel limit and physical sign. Its one wording correction, replacing necessary-sounding integrability language by a sufficient range, is included. The review and current submitted source are pinned in the team records. The collaboration used the existing A agent configured for the primary model; configuration is not provider attestation. Existing working files are the only model-collaboration channel.
