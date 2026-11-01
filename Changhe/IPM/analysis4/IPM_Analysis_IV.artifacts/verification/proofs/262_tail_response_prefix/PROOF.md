# Prefix majorants with a response bound only on the remaining tail

Status: comparison theorem already PROVED in226. The Q8 and Q7 third-root applications below are PROVED by V538 and V542. The complete argument is repeated below to keep this result standalone.

## Statement

Fix an integer Q>=3, delta=2/Q, an even integer bandwidth B>=2, and a nonzero real leading sine polynomial supported on positive odd frequencies below B. Put p_n=1-n delta, P_n=2-n delta and lambda_n=(n-1)delta/(1-delta). Use the density and stream recurrence of01 and delete the resonant output in the particular Poisson inverse. The positive-frequency stream resonances are n=kQ, k>=2, with free coefficient H_(kQ) in mode2k-2.

Let M>=2 and N=MQ. Suppose an actual compatible finite prefix has been determined through f_N and g_(N-1). It solves every stationary coefficient equation and Poisson equation at those orders, including the compatibility condition for f_N. Suppose the earlier tuning choices are those of the Q-step response construction131. Assume

    |sigma_k| >= s_tail > 0 for every integer k>=M,

where sigma_k is the coefficient of H_(kQ) in the next forbidden density coefficient. No numerical lower bound on sigma_k for k<M is part of this hypothesis; the existence and validity of the finite prefix have already been supplied.

Choose rational bounds d_j>=j||f_j||_1>0 for1<=j<=N and e_a>=aQ|H_(aQ)| for2<=a<M, with e_1=0. Set

    L=3Q^2/[4(3Q-1)],
    kappa_N=B[2-delta+max(delta,1-delta)](1-delta)/delta*(N+1)/N.

Form exactly the nonnegative residue system and transformed map G of175, but put s=s_tail in its harmonic row. If a rational w0>0 and nonnegative vector v satisfy v>=Y0 and G(w0,v)<=v, the unique tuned extension has absolutely and uniformly convergent density, stream and common-potential series, with every fixed appropriately weighted spatial derivative, on each closed exterior

    r>=R>w0^(-1/2).

For leading amplitude epsilon, the unit-amplitude sufficient radius is multiplied by |epsilon|^(Q/2). The common potential has at most the two finite logarithmic corrections at ordersQ and2Q. No optimal-radius or global-extension conclusion is asserted.

## Proof

The compatible prefix permits the next step at n=N. With the provisional choice H_N=0, continue the recurrence through N+Q. The response identity of131 makes the forbidden density coefficient at N+Q equal to R_N+sigma_M H_N. The condition |sigma_M|>=s_tail makes H_N=-R_N/sigma_M uniquely defined. It enforces the next compatibility condition. Repeating at n=(M+1)Q and later constructs the extension, since every later response is covered by the same hypothesis. No inverse response with index below M is taken in this continuation.

Initialize the scalar bounds of175 by the supplied d_j and e_a. Its lookahead bounds use only those earlier density and harmonic coefficients and previously constructed lookahead terms. At n=kQ>=N, divide the provisional obstruction bound by |sigma_k|>=s_tail. This is the only place where a response bound enters the scalar induction. All ordinary density estimates use the Poisson constant L and the advection constant kappa_N; every newly estimated total order is at least N+1. Thus the scalar equalities of175 dominate the actual density and harmonic coefficients at every later order with this tail-only value of s.

The residue projection does not depend on any response values before N. It therefore gives the same polynomial map Phi, the same strictly lower triangular affine part J at w=0, and the same finite nonnegative inverse T=(I-J)^(-1). For Y0=T Phi(0,0), the map G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)] has only positive powers of w outside its constant term. Iteration from zero is monotone and stabilizes coefficient by coefficient. The rational supersolution bounds every iterate at w0, so each residue generating series has a finite nonnegative sum there. Consequently the scalar coefficients have geometric base at most w0^(-1/Q).

The finite angular bandwidth absorbs every fixed derivative factor on a strict exterior R>w0^(-1/2), and permits a sufficiently small angular analytic strip. The common-potential reconstruction132 has the same geometric base, with only the two stated finite logarithms. Absolute convergence justifies multiplication and differentiation in the stationary equation. Amplitude homogeneity gives the displayed scaling. This completes the proof.

## Intended applications and independent checks

At Q7 and Q8, use the third real compatibility root from253 and256. The small early responses occur near k18 and k10, respectively. A prefix ending after those indices can use a different tail bound. This observation alone proves neither the size of that bound nor an improved radius.

Produce a longer directed Cartesian prefix, then repeat it using the separate polar recurrence with two full provisional continuations at every resonance. Retain exact root intervals, norm and harmonic enclosures, and verify the rational upper bounds. Certify the remaining integer tail by finite responses and a complete compact-response partition; a second precision must recompute every leaf and its exact integer coverage. Finally rebuild the residue map from the rational prefix, compare it with independently indexed scalar sums, and check every supersolution inequality in exact arithmetic. Retain all actual timings and source hashes.

Dependencies:01,131,132,169,175,226,232,234,253,256,261. The proof changes only the range of the response-bound hypothesis; it does not infer an infinite bound from a finite sample.

## Admitted Q8 application

On 2026-10-31T19:05:16+00:00, V538 admits the third increasing real root of the Q8 compatibility polynomial. The directed Cartesian prefix through N96 uses2048 bits. The independent3072-bit positive-frequency polar prefix checks192 density/stream norms and11 harmonics/responses, with two provisional continuations at each resonance. For every k>=12 the response satisfies |sigma_k|>2^-19:13 directly evaluated responses and two closed degree-three Taylor leaves cover the remaining integer tail, including t=0. A3072-bit replay reconstructs every leaf and its integer coverage. The rational residue map closes at w0=2^-130;48 independently indexed scalar identities and every exact box inequality pass. Thus R>2^65|epsilon|^4 is a sufficient exterior. All earlier admitted exteriors remain valid. This does not identify an optimal radius.

## Admitted Q7 application

On 2026-10-31T19:22:20+00:00, V542 admits the third increasing real root of the Q7 compatibility polynomial. The Cartesian2048-bit prefix reaches N140 and its independent3072-bit positive-frequency polar replay checks280 density/stream norms and19 harmonic/response pairs. The polar replay checks31,010 ordered products and62,243 Poisson columns. For every k>=20, |sigma_k|>2^-19: eight direct responses and two closed degree-three Taylor leaves cover the integer tail. The3072-bit replay reconstructs the complete partition and all42 scalar identities. The rational map closes at w0=2^-109, giving the sufficient exterior R>2^(109/2)|epsilon|^(7/2). The Cartesian, polar, tail construction and final replay took454.4481,636.7266,10.5433 and9.9587seconds respectively. No sharp-radius statement is inferred.
