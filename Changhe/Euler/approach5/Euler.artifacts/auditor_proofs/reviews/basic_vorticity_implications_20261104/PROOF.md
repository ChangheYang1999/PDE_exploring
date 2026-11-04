# Three vorticity implications and their boundary terms

## 1. Exact setting and conclusions

Let c>0, omega in R be finite, J(y_1,y_2,y_3)=(-y_2,y_1,0), and A=cI-omega J. A profile satisfies

    (1-c)U+DU(Ay+U)+omega JU+grad P=0,   div U=0

on all of R^3. Write W=curl U, S=(DU+DU^T)/2, B=Ay+U, and E(R)=integral_(|y|<R)|U|^2. The norm of S is the Frobenius norm. In this proof Hb means U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Uniform decay implies Hb.

The following three implications are audited here.

1. For U,P in C^1, Hb and 2/5<c<1, finiteness of

       integral (1+|y|^2)^(1/c-3/2)|W|^2

   implies U=0 and P constant.
2. For U in C^2, P in C^1, Hb and 0<c<2/3, the compact-cutoff nonlinear-weight criterion in Section 5 implies the same conclusion. It also applies when its nonnegative scalar remainder has finitely many zeros, as proved in Section 6. This includes both closed bounds

       sup |W| <= sqrt(3)(1-3c/2)

   for 0<c<2/3, and

       sup |W|^2 <= (15sqrt(7)-20)/42

   for 0<c<=1/2.
3. For U in C^2, P in C^1 and Hb, if

       lambda_max(S(y))<1 for every |y|<=||U||_infinity/c,

   then U=0 and P constant, for every c>0. No global bound on W or DU is needed in this third implication.

All conclusions hold separately for each finite omega; constants may depend on omega. They remain conditional on their explicit vorticity or strain premise. This review does not recertify the optimal-weight ODE, the larger certified thresholds, the mixed strain-vorticity tables, or their optimality statements.

The only profile energy input used in implications 1 and 2 is the already audited Hb energy theorem A052-A053: for 0<c<2/5 a profile is zero; for c=2/5 it has finite energy; for 2/5<c<1, with alpha=5-2/c,

    E(R)=L R^alpha+O(R^(alpha-1)),

where L>=0 and L=0 forces U=0. The pressure normalization needed to prove that theorem is part of that earlier theorem, not an extra assumption silently added here. The present proof checks its use and all new boundary terms, not its entire proof again.

## 2. The weighted Biot-Savart estimate

For measurable locally bounded f and m<1, assume integral `<y>`^(-m)|f|^2 is finite, where `<y>`=(1+|y|^2)^(1/2). Define

    BS(f)(y)=(4pi)^(-1) integral f(z) cross (y-z)/|y-z|^3 dz.

The integral is absolutely convergent. Near y this follows from local boundedness and local integrability of |y-z|^(-2). Away from y, Cauchy-Schwarz bounds it by the weighted L2 norm times the square root of integral `<z>`^m|y-z|^(-4). The radial power at infinity is r^(m-2), integrable precisely when m<1.

Set A_0={|y|<1}, A_k={2^(k-1)<=|y|<2^k} for k>=1, f_k=f 1_(A_k), and N_k=||f_k||_2. For k>=0,

    ||BS(f_k)||_2 <= C_1 2^k N_k,   C_1=sqrt(35/3).

Indeed, inside B_(2^(k+1)), Young's inequality with the truncated kernel gives the bound 3*2^k N_k. Outside this ball, |y-z|>=|y|/2 gives

    |BS(f_k)(y)|<=pi^(-1)|y|^(-2)|A_k|^(1/2)N_k.

Using |A_k|<=(4pi/3)2^(3k), its squared integral there is at most (8/3)2^(2k)N_k^2. The two disjoint regions give 9+8/3=35/3.

If R>=1 and 2^(k-2)>=R, then |y-z|>=2^(k-2) for |y|<R, z in A_k. Consequently

    ||BS(f_k)||_(L2(B_R)) <= C_2 R^(3/2)2^(-k/2)N_k,
    C_2=16/3.

The constants include the factor 1/(4pi). Combining the two estimates gives

    ||BS(f)||_(L2(B_R))
      <= C_1 sum_(2^k<4R) 2^k N_k
          +C_2 R^(3/2) sum_(2^k>=4R) 2^(-k/2)N_k.        (1)

Absolute convergence of the pointwise integral and finite sums followed by Fatou justify the use of these series bounds; the bounds on their tails below also give L2 convergence.

Now assume -2<m<1, put K_k=integral_(A_k)`<y>`^(-m)|f|^2, s=1+m/2>0, and t=(1-m)/2>0. On each shell,

    N_k<=2^(|m|/2)2^(km/2)K_k^(1/2).

After division by R^s, the two weights in (1) are (2^k/R)^s and (R/2^k)^t. Their sums are bounded by geometric constants depending on s,t. Since K_k tends to zero, the terms above a fixed sufficiently large index are uniformly small. The finitely many earlier terms tend to zero as R tends to infinity. Therefore

    integral_(B_R)|BS(f)|^2=o(R^(m+2)).                    (2)

No pointwise decay estimate for f or its derivatives was used.

## 3. Removal of the harmonic ambiguity

For compactly supported C^1 vector fields F, the Helmholtz formula is

    F=BS(curl F)+Q(div F),
    Q(g)(y)=(4pi)^(-1) integral g(z)(y-z)/|y-z|^3 dz.

For smooth F this follows by convolution with the fundamental solution of -Delta. Mollification gives the C^1 statement, because the first-derivative kernels are locally integrable and the supports remain in a fixed compact set.

Choose a smooth radial cutoff chi equal to one on B_1 and zero outside B_2. Apply the formula to F_N=chi(y/N)U. For fixed y and N>|y|,

    U(y)=BS(chi(. /N)W)(y)+E_N(y),
    E_N=BS(grad chi(. /N) cross U)+Q(grad chi(. /N).U),

where grad chi(. /N) denotes the actual scaled gradient N^(-1)(grad chi)(. /N). The first term tends to BS(W)(y) by the absolute integrability proved above.

In E_N change variables z=Nx. The gradient contributes N^(-1), the volume N^3 and the kernel N^(-2), so no power remains. On the fixed annulus 1<=|x|<=2, replace the vector kernel q(y/N-x) by q(-x), q(v)=v/|v|^3. Its derivative is bounded along these segments when |y|<=N/2, and bounded U makes the replacement error O(|y|/N). Every remaining component is a pairing of U(N.) with one fixed smooth compactly supported test function. Hb makes those pairings tend to zero. Thus

    U=BS(W).                                               (3)

This argument removes the whole harmonic ambiguity using Hb. It does not assume that the velocity tends pointwise to zero, or that a harmonic remainder is already bounded. It uses no profile equation beyond div U=0.

For implication 1 use m=3-2/c, which lies in (-2,1). Equations (2)-(3) give E(R)=o(R^(5-2/c)). The energy theorem makes L=0 and hence U=0. A stronger weight with any exponent m<=3-2/c also suffices by monotonicity of `<y>`^(-m). The pressure is constant by the full equation.

In particular, |W(y)|<=C(1+|y|)^(-gamma) with gamma>1/c suffices. So does |W(y)|<=C|y|^(-1/c)(log|y|)^(-beta) for |y|>=2 and beta>1/2: the weighted radial integral is bounded by a constant times integral_2^infinity r^(-1)(log r)^(-2beta)dr. The strict logarithmic exponent is not replaced by its endpoint.

## 4. Two compact identities

For implications 2 and 3 use U in C^2. The full equation gives P in C^2 and the classical curl equation

    W+B.grad W-(W.grad)U+omega JW=0.

Set t=|W|^2. Taking its scalar product with W gives

    B.grad t=2(W.SW-t),   div B=3c.                         (4)

Let phi_R=chi(|y|/R), with chi smooth, nonnegative, nonincreasing, equal to one up to 1 and zero from 2 onwards. For R>2||U||_infinity/c,

    B.grad phi_R=(chi'(|y|/R)/R)(c|y|+U.y/|y|)<=0.          (5)

The rotation is tangent to the cutoff spheres. Fix M>0. If g in C^1([0,M^2]), g(0)=0, g'>=0 and |W|<=M, the chain rule in (4) gives

    integral phi_R T=F_R>=0,
    T=2g'(t)W.SW-2g'(t)t+3c g(t),
    F_R=-integral g(t) B.grad phi_R.                        (6)

A C^1 extension beyond the closed interval justifies composition at an attained endpoint. All integrals in (6) are compactly supported and g>=0 by monotonicity.

Independently, incompressibility and two integrations by parts give

    integral phi_R(|S|^2-t/2)=E_R,
    E_R=integral U_iU_j partial_i partial_j phi_R.            (7)

Here |S|^2-t/2=partial_jU_i partial_iU_j. In the two integrations all terms containing derivatives of div U vanish. Hence

    |E_R|<=C_chi R^(-2)E(2R)=o(1)                          (8)

for 0<c<2/3 by the exact energy input in Section 1. This includes c=2/5 and the already vanishing range below it. We have not integrated any unsigned stretching term over all of space.

## 5. The exact tensor square

Let a>0 and define

    H(t)=2tg'(t)-3c g(t)-at/2-(2/(3a))t^2g'(t)^2,
    D=a(|S|^2-t/2)-T.

For Q=W tensor W-tI/3, trace freedom of S gives S:Q=W.SW and |Q|^2=2t^2/3. Thus the following is an identity, not just an eigenvalue inequality:

    D=a|S-(g'(t)/a)Q|^2+H(t).                              (9)

If H(t)>0 for 0<t<=M^2, then D>=0 and its only possible zero has t=0 and S=0. Equations (6)-(8) give

    0<=integral phi_R D=aE_R-F_R<=a|E_R| ->0.

The cutoffs increase pointwise to one as R increases. Monotone convergence, or restriction to each fixed ball, forces D=0 everywhere by continuity. Hence DU=0. Hb removes the constant velocity, and the profile equation gives constant P. This proves the strict nonlinear-weight criterion without assuming finite enstrophy or any global bound on DU.

## 6. Finite-zero endpoints

The same argument works if H is nonnegative on [0,M^2] and its zero set there is finite. Indeed D=0 first implies H(t(y))=0. A continuous function on connected R^3 whose values belong to a finite set is constant, so t=t_0.

If t_0>0, then g(t_0)>0. Otherwise g>=0, g' >=0 and g(0)=0 give g=0 on [0,t_0]; C^1 regularity gives g'(t_0)=0, including when t_0=M^2 by the one-sided derivative. But then H(t_0)=-at_0/2<0, a contradiction. Equation (4) with constant t gives W.SW=t_0. Consequently T=3c g(t_0), and D=0 yields

    a(|S|^2-t_0/2)=3c g(t_0)>0

pointwise. Integrating against phi_R contradicts (7)-(8): the left side is aE_R tending to zero, while the right side is a positive constant times R^3 integral phi_1. Thus t_0=0, and (9) gives S=0. This endpoint argument uses no maximum attainment and no derivative-decay theorem.

For kappa=1-3c/2>0 choose a=1, g=t/(2kappa). Then

    H(t)=t/2-t^2/(6kappa^2),

nonnegative on [0,3kappa^2] with exactly the two zeros 0 and 3kappa^2. This proves the first closed bound in Section 1.

For the second choose a=1, g=t+(21/20)t^2. Direct algebra gives

    H_c(t)=(3/2-3c)t+[(21/20)(4-3c)-2/3]t^2
               -(14/5)t^3-(147/50)t^4,
    H_(1/2)(t)=t^2[47/24-(14/5)t-(147/50)t^2],
    H_c=H_(1/2)+(3/2-3c)g.

The bracket is strictly decreasing for t>=0 and has the positive root t_*=(15sqrt(7)-20)/42. Thus H_c is nonnegative on [0,t_*] for 0<c<=1/2, with zero set {0} when c<1/2 and {0,t_*} when c=1/2. Section 6 proves the asserted closed threshold exactly. No decimal approximation or numerical root isolation is used.

This argument does not handle a weight whose scalar remainder vanishes on an interval. In particular it is not a fresh proof of the optimal-weight endpoint, where a separate argument is necessary.

## 7. The compact-core strain criterion

Let M=||U||_infinity. The carrier B has at most linear growth and is C^1, hence its flow Phi_t is complete. Variation of constants for the reverse-time equation gives

    |Phi_(-t)y|<=exp(-ct)|y|+(1-exp(-ct))M/c,   t>=0.       (10)

The factor exp(-tA) has norm exp(-ct), because its remaining factor is orthogonal. In particular every backward orbit is bounded, and its distance from the closed ball of radius M/c tends to zero.

Assume lambda_max(S)<1 at every point of that closed ball. Continuity and compactness give a uniform positive gap, which persists in some open neighborhood of the ball. Every backward trajectory eventually lies in that neighborhood by (10). Along its sufficiently negative tail, (4) gives

    d|W(Phi_s y)|^2/ds<=-2delta|W(Phi_s y)|^2.

The homogeneous linear vorticity equation along a trajectory preserves nonvanishing over every finite time interval. If W were nonzero anywhere on that orbit, backward integration of this inequality would make its norm grow without bound. This contradicts continuity of W on the compact backward orbit closure. Hence W=0 everywhere. Each component of U is entire harmonic because div U=0 and curl U=0. Boundedness gives a constant vector, and Hb makes it zero. This proof uses neither the energy theorem nor global control of S outside the indicated neighborhood.

The strict pointwise condition on the closed ball cannot silently be replaced by a non-strict inequality: the positive gap was essential. At M=0 the conclusion U=0 is immediate and no separate core argument is needed.

## 8. Scope of this repeated audit

The full current in the team records, in the team records and in the team records sources were read, together with the earlier independent nonlinear-weight and endpoint proofs. The analysis above rechecks only the explicitly stated implications. It does not certify every historical sentence or numerical experiment in those files. In particular a functional concentration example is not a full Euler profile, and compatibility of two scalar mass bounds does not prove a universal obstruction to every future argument.

The three additional premises here have not been derived from bare decay. The integral proof makes no statement at the logarithmic endpoint beta=1/2, the smallness proof uses a global vorticity bound rather than only a far-field limsup, and the core criterion uses a strict strain bound. The full arbitrary-omega nonexistence question remains open; the separately established omega=0 theorem is not reopened.

No mathematical computation was needed. The completed existing configured model A110 comparison is discussed in Section 9. Actual provider execution is independently unattested. Advanced Theorem 8 weights and all exact certificate tables retain their separate earlier audits.

## 9. Existing A110 comparison and scope qualification

The full A110 comparison in the team records has been read. Its checks of the weighted Biot-Savart bounds, Hb cutoff normalization, exact square, finite-zero argument and compact-core localization agree with Sections 1-7. No gap was found. The three implications are supported by their complete independent proofs here, with the previously named energy theorem as their only profile-energy dependency.

A110 correctly qualifies the earlier note that the report's strict vorticity bound is weaker. That comparison concerns the first two elementary sentences of Theorem 8(a), not the entire theorem: the same report also states a stronger optimal-weight closed endpoint. The current proof supplies a direct elementary closed-bound argument; no new threshold or improvement over the report as a whole is claimed. The relevant printed Theorem 8(a) passage was read directly. A110's strict comparison with the optimal ODE threshold uses additional results that are outside this repeated audit and is not newly certified here. The general finite-zero remainder criterion is stated and proved in Section 6, rather than asserted to be a verbatim report theorem.

The named fourteen-item scratch diagnostic script and log have not been read or rerun here. Their count, exactness and pass claim are not certified. No part of the independent proof depends on them. This review likewise does not newly certify the optimal-weight ODE, its numerical brackets, mixed strain tables or their global optimality. Existing configured model file collaboration occurred; actual provider execution is independently unattested.
