# Vorticity endpoint exclusions without a strain-decay assumption

## Statement

Let 2/5<c<1/2, let omega be any finite real number, and let U in C2(R3;R3), P in C1(R3) solve

    (1-c)U+((cI-omega J)y+U).grad U+omega JU+grad P=0,
    div U=0,    U(y)->0 uniformly as |y|->infinity.

Here J(x,y,z)=(-y,x,0) and Omega=curl U. If either

1. Omega belongs to Lp(R3) for some 1<=p<=3c, or
2. Omega(y)=o(|y|^(-1/c)) uniformly,

then U=0. No decay of S=(DU+DU^T)/2 is assumed. The range 1<p<=3c and the pointwise assertion confirm CO10; the p=1 case is a separate extension proved below.

## Energy input

A053, proved in the team records, gives the following consequences of this exact profile equation and velocity decay. Put

    q*=3c/(1-c),    d=5-2/c>0.

A nonzero profile has E(R)=integral_(|y|<R)|U|^2 with E(R)/R^d tending to a strictly positive finite number. Hence U in Lq for any 0<q<=q*, or U=o(r^(1-1/c)), forces U=0. In particular U in L2 is excluded. The proof of A053 includes canonical pressure normalization; no new pressure assumption is made here.

## Potential estimate and the harmonic ambiguity

Write G(x)=1/(4 pi |x|). For a vector field f define the differentiated Newton potential

    Tf(x)=(4 pi)^(-1) integral f(y) cross (x-y)/|x-y|^3 dy.

For 1<p<3 and 1/q=1/p-1/3,

    ||Tf||_q <= C_p ||f||_p.                           (1)

For completeness, this estimate does not depend on a convention for the vector cross product. The scalar majorant is I1|f|=integral |x-y|^-2 |f(y)|dy. If M is the centered maximal operator, splitting at radius R and then into dyadic shells gives

    I1|f|(x) <= C R M|f|(x)+C_p ||f||_p R^(1-3/p).

The inner bound follows by summing C 2^-j R M|f|. The outer bound is Holder's inequality; the power integral converges precisely when p<3. Choosing R=(||f||_p/M|f|(x))^(p/3) gives

    I1|f|(x) <= C_p ||f||_p^(p/3) M|f|(x)^(1-p/3).

The maximal inequality ||Mf||_p<=C_p||f||_p completes (1), since q(1-p/3)=p. Its standard short proof is the weak (1,1) ball-covering estimate, followed by truncating f at height lambda/2 and integrating

    |{Mf>lambda}| <= C lambda^-1 integral_(|f|>lambda/2)|f|.

Multiplication by p lambda^(p-1) and Tonelli give a constant times integral |f|^p for p>1. The weak estimate itself follows by selecting disjoint balls with averages above lambda whose fivefold dilates cover the level set and summing their volumes. Thus all exponents and endpoint exclusions in (1) are explicit.

For smooth compactly supported f, Tf=curl(G*f), so -Delta Tf=curl f. Approximate an arbitrary Lp field by such fields; (1) gives local L1 convergence of their potentials and proves the same identity in distributions. Since -Delta U=curl Omega, h=U-T Omega is distributionally harmonic whenever (1) applies. It is represented by a smooth harmonic function. For any fixed x its mean-value formula gives

    h(x)=average_(B_R(x)) U-average_(B_R(x)) T Omega.

The first term tends to zero: split the ball into a fixed compact set and its complement, where U is uniformly small. The second tends to zero by (1) and Holder, with bound C R^(-3/q)||T Omega||_q. Consequently h=0. This argument removes every harmonic ambiguity directly; no unproved decay of the potential or polynomial-growth normalization is used.

## The Lp criterion for 1<p<=3c

Take f=Omega. Since 3c<3/2, (1) applies, with

    3/2<q=3p/(3-p)<=3c/(1-c)=q*.

The preceding mean-value argument shows U=T Omega in Lq. A053 now gives U=0. This includes p=3c exactly. The ordinary natural power r^(-1/c) would give a logarithmically divergent L^(3c) integral, so the endpoint does not exclude that power on its own.

## The L1 extension

Let f belong to L1. Split the scalar kernel |x|^-2 at radius R. Its inner part has L1 norm C R, and its outer part has supremum R^-2. For lambda>0 choose R=(2||f||_1/lambda)^(1/2). The outer convolution is at most lambda/2, and Markov's inequality on the inner convolution gives

    |{|Tf|>lambda}| <= C (||f||_1/lambda)^(3/2).        (2)

In particular Tf is locally integrable, with

    integral_E |Tf| <= C ||f||_1 |E|^(1/3)             (3)

for every finite-measure E. To obtain (3), integrate the minimum of |E| and the bound (2) over lambda. Approximation in L1 and (3) justify -Delta Tf=curl f as before. For f=Omega, the harmonic mean-value argument now uses (3), whose ball average is O(R^-2), and again gives U=T Omega.

Let M=||U||_infinity, finite by velocity decay and continuity. Integrating (2) only up to M gives

    integral |U|^2
      =2 integral_0^M lambda |{|U|>lambda}| d lambda
      <= C ||Omega||_1^(3/2) M^(1/2)<infinity.

Therefore A053 excludes U. There is no claim here for 0<p<1 without a further hypothesis.

## The pointwise little-o endpoint

Set beta=1/c, so 2<beta<5/2. The hypothesized Omega is continuous and bounded, and its tail lies in L2. Thus it belongs to L2 globally. Its potential is also given by an absolutely convergent integral: the local kernel is integrable, and beta>1 ensures convergence at infinity.

Given epsilon>0, choose R_epsilon so |Omega(y)|<=epsilon |y|^-beta outside that ball. For r=|x|>=2 R_epsilon the compact contribution is at most C_epsilon r^-2. The remaining part is bounded by

    C epsilon integral |x-y|^-2 |y|^-beta dy
       =C_beta epsilon r^(1-beta).

The scaled integral is finite at y=0 because beta<3, at y=x because the kernel has exponent 2<3, and at infinity because beta>1. Since beta<3, r^-2=o(r^(1-beta)). Hence T Omega=o(r^(1-beta)). The harmonic argument, either using (1) with p=2 or the just proved decay, gives U=T Omega. Thus U=o(r^(1-1/c)), and A053 gives U=0.

## Scope and verification

These proofs use the actual curl coupling and the previously proved profile energy law. They apply to all angular modes and every finite omega. Neither critical big-O vorticity decay nor mere DU->0 is covered. The pointwise assertion and the Lp assertion need no extra pressure normalization. All calculations are analytic; no numerical experiment is used.
