# Uniform response bounds at the period-ten compatibility roots

Status: PROVED in V587, admitted 2026-10-31T21:15:10+00:00, within the exact scope below.

## Statement

Set delta=1/5 and let b_i run over the real roots of the primitive degree20 compatibility polynomial of281. Let I_i be its rational isolating intervals. The response sigma_k(b) is defined in282 for integer k>=2. The intended result is a separately recorded positive rational s_i such that

    |sigma_k(b)| > s_i for every integer k>=2 and every b in I_i.

This is stronger than the assertion at b_i and supplies a valid lower bound for a majorant convergence theorem. It is not a claim that s_i is sharp or that any sampled minimum is the true infimum.

## Proof of the certificate criterion

For k>=21 use the exact identity sigma_k=N(k,b)/D(k) from282, with D monic, degree d, and N of degree at most d in k. For smaller k use its exact response polynomials. Require all supplied expressions and root intervals to match the admitted inputs by hash.

Choose a sign e_i in {1,-1}, a rational s_i>0, and an integer K_i>=21. Expand D(K_i+x) and

    P_i(K_i+x,b)=e_i N(K_i+x,b)-s_i D(K_i+x)

as polynomials in x. Require every coefficient of D(K_i+x) to be strictly positive. Require every coefficient of P_i(K_i+x,b), evaluated by interval arithmetic on the entire I_i, to have a nonnegative lower bound, with strictly positive constant coefficient. An identically zero coefficient may be handled by exact polynomial equality.

For x>=0 the denominator is positive and P_i is strictly positive. Thus e_i sigma_(K_i+x)(b)>s_i>0 for all b in I_i. This proves the desired modulus bound for all integer k>=K_i. For every integer2<=k<K_i, a direct exact-polynomial interval evaluation must prove either sigma_k(b)>s_i or sigma_k(b)<-s_i on all of I_i. These finitely many checks and the positive-coefficient tail prove the statement for every index.

For proposing s_i, one may sample finitely many directed values and the limiting response, take a strict rational underestimate of their least modulus, and round down to a power of two. This proposal is not itself a proof of a global bound. Only the finite and infinite-tail inequalities just described admit s_i. A failed proposal is retained and cannot be admitted.

## Independent replay and scope

The producer uses exact rational polynomial shifts followed by1024-bit directed Horner evaluation. A separate replay reconstructs the shifts from the original response data, uses rational endpoint interval multiplication and addition, verifies every finite comparison and every tail coefficient, and records the number of checked inequalities. It checks the root and formula input hashes and the rational target values. It need not trust the producer's displayed midpoint signs.

No monotonicity, attained minimum, sharp convergence radius, or growth law follows from these bounds. Their use in convergence requires the complete majorant theorem and separately certified initial coefficients. The result depends on281,282 and the elementary interval and polynomial argument given here.

## Completed verification

For the fourteen roots in increasing order, uniform lower bounds s=67108864,32,1/64,1/2048,1/8388608,1/4096,1/2048,1/1024,1/256,1/128,1/32,1/2,32,32768, with tail starts K=21,21,21,21,21,21,21,21,21,21,21,21,21,21. The separate rational-endpoint replay passes1540 nonzero tail coefficients,0 exact-zero coefficients and266 finite-carrier inequalities. Every denominator coefficient after shifting is strictly positive. Producer runtime5.498458seconds; replay runtime2.062611seconds.

The all-index lower bounds are PROVED. Sampled minima only propose targets; no global minimizing index, sharp infimum or exterior radius is asserted here.
