# Matrix-floor pinning and its quantitative scope

## Exact statement and dependencies

For the exact state131 reference, set A=[[rho_y,-rho_x/2],[-rho_x/2,0]], V=cX+u, c=4076476460239181/2251799813685248 and omega=(1+4r^2)^(2/5). Define

    M1=I-Sym Du+A,
    Mk=(1+c+V.D log omega)I-k Sym DV+A, k=2,3.

Let m_k=inf_(X in R^2) lambda_min M_k(X). The existing A2 theorem P96 supplies the global lower bounds. The independently verified T4-093 point caps give the upper bounds. Together they imply

    972875/1000000 <= m1 < 99116/100000,
    293619/500000 <= m2 < 61151/100000,
    -307719/250000 <= m3 < -120662/100000.

The interval widths are respectively 0.018285,0.024272,0.024256. These widths measure uncertainty relative to the improved P96 floors. In particular 0.024272 bounds the possible increase over the P96 value0.587238. Relative to the earlier theorem floor1/2, the upper improvement is0.11151. Neither statement gives the norm of an arbitrary stationary inverse.

## Identification and proof

Write chi_ab for the Cartesian derivatives of the canonical potential. Then

    Du=[[-chi22,-chi13],[chi31,chi22]],
    rho_x=-chi31-chi13, rho_y=-chi22-chi04.

Substitution gives M1=[[1-chi04,chi13],[chi13,1-chi22]]. For k=2,3 the scalar transport term and remaining matrix are exactly the B2 and B3 of the frozen P96 proof. The identity V.D log omega=(16/5)t(c+e)/(1+3t), t=r^2/(1+r^2), e=X.u/r^2, gives the same compactified coefficients. These are the unweighted order-one and omega-weighted order-two and order-three matrices, not the decreasing-weight order-one matrix.

The source P96 theorem is already A2-THEOREM. Its full proof and certificate records are frozen here. The present integrity check verifies the primary/recheck hashes, exact targets, positive recorded leaf bounds, complete nonoverlapping compactified rectangles and successful independent polynomial audit. It does not claim to rerun the original polynomial construction or its entire numerical certificate.

For each k, the global lower certificate implies m_k is at least its target. At the explicitly stored rational point, lambda_min M_k is rigorously below its stored rational cap, so m_k is below the cap. Subtraction gives the widths. The packet theorem T4-092 explains why these caps also limit a corresponding contractive principal energy rate, under that theorem's exact spaces and normalization. It does not turn a numerical-range cap into an actual inverse lower bound.

## Gram sensitivity and the meaning of an improvement factor

Fix beta_L=2, the commutator constant C'=401 for sharp weights or397 for sharpw, and all off-diagonal and lower-order constants of TP-5. Its symmetric matrix is

    G(mu;m2,m1)=
      [[m2-mu, -34.7, -5],
       [-34.7, w1(m1-mu)-40, -3w1],
       [-5,-3w1,w0(2-mu)]].

Increasing m1,m2 increases G in the positive-semidefinite order. Hence the positive-rate endpoint mu_* cannot exceed that obtained by substituting the point caps. A finite exact bisection bracket, already independently verified in T4-113, gives a certified rational upper endpoint for mu_*.

For a high ball of radius r and regularity s, the residual threshold from this fixed scheme is at most

    r(mu-C's-(8/5)r/sqrt(s)).

For fixed s it is a concave quadratic in r, maximized at r=(5/16)(mu-C's)sqrt(s) when mu>C's. Maximizing the resulting expression over all s>0 gives

    eta <= mu^(5/2)/(10 sqrt(5 C')),
    s=mu/(5C').

Ignoring any other restrictions can only increase this upper bound. It is increasing in mu. Substitution of the rational upper Gram endpoint therefore gives a rigorous upper limit for improvements that change only these two matrix floors and retain beta_L=2 and the other constants. It is not an upper bound for every possible linear estimate or every background reference.

Compare this ceiling both with the optimized baseline Gram endpoint and with the actual published T2-R3 thresholds7.6219e-5 and2.1035e-4. These are different denominators. A rounded factor relative to an optimized baseline must not be presented as a directed upper factor relative to the published threshold. Moreover state131's point caps do not limit the possible floors of d2 or another reference.

## Verification and scope

The local script checks source integrity, all three rational intervals, and the two ceiling ratios with outward arithmetic. The existing P96 proof supplies the global theorem; T4-093 and T4-113 supply independently checked point and Gram data. These comparisons do not establish residual membership or smallness for state131, and they do not make the proposed floor improvements attainable.
