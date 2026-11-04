# Cumulative radial source and finite energy

Status: CONFIRMED at the exact scope of A3063-A3064. No eventual cumulative-source lower bound or eventual pressure monotonicity is inferred from decay.

## 1. Exact kinematic statement

Let U be a C1 divergence-free vector field on R3. For r>0 set

    q=tr((DU)^2),  E(r)=integral_(B_r)|U|^2,
    T(r)=integral_(partial B_r)|U|^2,
    N(r)=integral_(partial B_r)|U.e_r|^2,
    S(r)=integral_(B_r)q,  A(r)=integral_0^r s S(s) ds,
    e_r(y)=y/|y|.

Surface integrals use ordinary area measure. The square in q is matrix multiplication. Then

    E'=T,  0<=N<=T,
    S=N'-(T-N)/r,  A=rN-E.                                (1)

Assume E(r)=o(r). If A(r)>=-C for all sufficiently large r, where 0<=C<infinity, then U is in L2 and ||U||_2^2<=C. Eventual S>=0 suffices for finite energy. If S>=0 for all r>0, then U=0.

Under E=o(r), infinite energy requires liminf_(r->infinity) A(r)=-infinity. Finite energy, with or without a separate o(r) premise, gives

    liminf_(r->infinity) A(r)=-||U||_2^2.                  (2)

No Euler equation, pressure, velocity bound or pointwise decay is assumed in these statements.

## 2. Exact flux calculation at C1 regularity

For smooth divergence-free U, q=div((U.grad)U). Local convolution preserves divergence and converges in C1 on compact sets. The approximating q and acceleration converge uniformly on each closed ball. The divergence theorem therefore passes to the limit and gives, for every r>0,

    S(r)=integral_(partial B_r)((U.grad)U).e_r.             (3)

Write u(r,theta)=U(r theta).theta and V(r,theta)=U(r theta)-u(r,theta)theta, so V is tangential to the unit sphere. Polar divergence and the derivative of e_r give

    div_(S2)V=-r partial_r u-2u,
    ((U.grad)U).e_r=u partial_r u
                     +r^-1 V.grad_(S2)u-r^-1|V|^2.       (4)

Integrating the middle term by parts on the sphere yields

    integral_(S2)V.grad_(S2)u
       =integral_(S2)(r u partial_r u+2u^2).

The factor r^2 in the area measure in (3) is essential. Substitution gives

    S=2r^2 integral u partial_r u+2r integral u^2-r integral |V|^2
     =N'-(T-N)/r.

All integrals in this display are on the unit sphere. Differentiation of N=r^2 integral u^2 is legitimate for C1 U. Coarea gives E'=T and the pointwise inequality u^2<=|U|^2 gives N<=T.

Multiplying the source identity by r gives rS=(rN-E)'. Local boundedness implies E(r)=O(r^3) and rN(r)=O(r^3) at the origin. Integrating from0 to r therefore gives A=rN-E, without an integration constant. No limit at infinity has been taken in this calculation.

## 3. Monotonicity and the limiting lower envelope

Suppose A>=-C for r>=r0. From (1),

    rE'(r)>=rN(r)=E(r)+A(r)>=E(r)-C.

Thus F(r)=(E(r)-C)/r is nondecreasing on [r0,infinity). The hypothesis E=o(r) gives F(r)->0, so F(r)<=0 for every r>=r0. Hence E(r)<=C. Monotonicity of E and passage to infinity prove ||U||_2^2<=C.

If S>=0 for r>=r0, then A'=rS>=0 there and A>=A(r0). Use C=max(0,-A(r0)). If S>=0 everywhere, then A>=0, so C=0 proves U=0. Conversely, if energy is infinite, any finite eventual lower bound on A would contradict the preceding implication. This is exactly the assertion liminf A=-infinity, not necessarily a limit of A.

For finite total energy E_infinity, (1) gives A>=-E>=-E_infinity. Also integral_1^infinity N(r)dr<=integral_1^infinity E'(r)dr<infinity. Nonnegativity implies liminf rN(r)=0: a strictly positive lower limit would bound N below by a positive multiple of 1/r eventually, contradicting that integrability. Choose r_j tending to infinity with r_j N(r_j)->0. Then A(r_j)=r_jN(r_j)-E(r_j)->-E_infinity. This proves (2). It uses a sequence of radii, not an unjustified pointwise surface-decay assertion.

## 4. Actual pressure and the Euler consequence

Suppose in addition U is bounded, P belongs to C1(R3), and for 2/5<c<1/2 and any finite omega,

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0,
    J(x1,x2,z)=(-x2,x1,0).

Assume Hb: U(R.) tends to zero in distributions on compact sets. The confirmed A052-A053 energy law, rechecked in A3053, gives E=o(r); if U is nonzero it gives E(r)=L r^beta+O(r^(beta-1)), with L>0 and beta=5-2/c in (0,1). Such a field has infinite energy. Hence the eventual lower bound on A in Section1 forces U=0. Its contrapositives require liminf A=-infinity and S<0 at arbitrarily large radii for any nonzero candidate.

Define pbar(r)=(4pi)^-1 integral_(S2) P(r theta)d sigma. Divergence of full momentum gives -Delta P=q in distributions, with cancellation of the two rotational contractions. Convolve this equation locally. The C1 convergence of P and uniform convergence of q justify passing the smooth divergence theorem to the limit at every fixed radius. Thus

    S(r)=-integral_(partial B_r) grad P.e_r
        =-4pi r^2 pbar'(r),
    A(r)=-4pi integral_0^r s^3 pbar'(s)ds.                 (5)

These are identities for the actual pressure. They require neither a normalization nor second derivatives of P. Eventual pbar'<=0 is equivalent to eventual S>=0 and therefore forces U=0 under the stated Euler hypotheses. A nonzero candidate must have pbar'>0 at arbitrarily large radii and

    limsup_(r->infinity) integral_0^r s^3 pbar'(s)ds=+infinity.

The latter statement is an unbounded upper envelope, not necessarily divergence to plus infinity. Uniform decay implies boundedness and Hb, so the target profiles are included. Neither c=2/5 nor c=1/2 is asserted by this argument.

## 5. Exact controls for the growth and sign directions

Let f be nonzero, smooth and compactly supported on R2, and take U=(0,0,f(x1,x2)). Its derivative matrix squares to zero, so q=S=A=0. For sufficiently large r,

    E(r)=2 integral sqrt(r^2-|x|^2)f(x)^2 dx
        =2r integral f^2+O(r^-1).

Thus replacing E=o(r) by E=O(r) would invalidate the theorem. Identity (1) gives rN=E. This is also visible directly from the two graph parametrizations of the sphere. The field fails decay on vertical lines. If f equals1 near the origin, horizontal and vertical momentum at the core and outside the support rule out a target Euler profile: P would depend only on z but would need P'=-(1-c) and P'=0 simultaneously.

For the sign control choose 1<a<3/2 and U=(1+|y|^2)^(-(a+1)/2)Jy. It is smooth, divergence-free, decaying, and tangent to every sphere. Therefore N=0, A=-E and S=-T/r<0 for r>0. Direct radial integration gives E of order r^(3-2a), which is infinite and o(r). Eventual S<=0 therefore does not force finite energy even with kinematic uniform decay.

This field also fails the full Euler equation. Writing f(s)=(1+s^2)^(-(a+1)/2), its angular momentum is Gamma=(x1^2+x2^2)f(|y|). The torque identity would give partial_theta P=-(x1^2+x2^2)[f(s)+c s f'(s)]. This is independent of theta and nonzero on sufficiently small nonzero horizontal circles for every finite c. Integration around a circle contradicts a single-valued C1 P. The cancellation is independent of finite omega.

## 6. Source, comparison and scope

All six LIT367 source sections, the twenty-two manual author checks, reading record and formal-source note were read. The proof above independently reconstructs the C1 flux, all radial factors, monotonicity sign, lower-envelope assertion and actual-pressure conversion. The kinematic proof is independent of LIT366 and the spherical-sign lemma. Only the stated target Euler consequence imports A052-A053. No computation or formal build is needed. The existing configured model comparison is addressed in Section7; actual provider execution is independently unattested. No eventual source sign, eventual lower bound or eventual pressure monotonicity is derived from decay, and the unrestricted rotating conjecture remains open.

## 7. Existing comparison and quantitative consequence

The complete C07:31:27 comparison, all ten numbered items, has now been read. Its flux, monotonicity, lower-envelope, pressure and negative-control calculations agree with Sections1-5. Its described symbolic and numerical diagnostics were not read or independently certified. The named far-field file was not reread in this comparison.

Here is a direct verification of the additional rate assertion. Assume only the kinematic hypotheses in Section1 and

    E(r)=L r^beta+O(r^(beta-1)),  L>0, 0<beta<1.

From A=rN-E<=rE'-E, integration by parts, with no differentiation of the error term, gives

    (1/R) integral_R^(2R) A(r)dr
      <=2E(2R)-E(R)-(2/R) integral_R^(2R)E(r)dr
      =-k L R^beta+O(R^(beta-1)),
    k=(2^(beta+1)-1)(1-beta)/(1+beta)>0.                  (6)

Let F_R={r in [R,2R]: A(r)<=-(k/2)L R^beta} and let m_R=|F_R|/R. The universal lower bound A>=-E(2R) and the complementary bound A>-(k/2)L R^beta imply

    (1/R) integral_R^(2R) A
       >=-m_R E(2R)-(1-m_R)(k/2)L R^beta.                (7)

For all sufficiently large R, the upper bound in (6) is at most -(3k/4)L R^beta and E(2R)<= (2^beta+k/4)L R^beta. Combining (6)-(7) gives

    m_R >= (k/4)/(2^beta-k/4) >= k/2^(beta+2)>0.         (8)

The denominator is positive: k<2^(beta+1), immediately from its formula and 0<beta<1. Thus the comparison's stated, conservative measure bound is valid. In particular A is unbounded below. Eventual S>=0 would make A nondecreasing and bounded below, so S<0 and, for an actual Euler pressure, pbar'>0 occur at arbitrarily large radii.

These target consequences are deductions from the already confirmed energy law and the kinematic identity. They do not eliminate the remaining arbitrary-rotation candidates or derive an eventual source sign. Only the stronger additional condition in Section1 or4 yields a conditional exclusion. The content independent of full Euler is the finite-energy criterion for arbitrary C1 divergence-free fields.

Conditionally, if r^alpha U(r theta) converges in L2(S2) to F(theta), alpha=(3-beta)/2, then integration of the spherical energy yields E(r)/r^beta -> (1/beta) integral|F|^2, and rN(r)/r^beta -> integral|F.theta|^2. Therefore

    A(r)/r^beta -> integral|F.theta|^2-(1/beta)integral|F|^2.

This is negative for nonzero F and 0<beta<1. The conclusion is conditional on that angular asymptotic, not a claim that all target profiles admit it. No uninspected far-field construction is certified.
