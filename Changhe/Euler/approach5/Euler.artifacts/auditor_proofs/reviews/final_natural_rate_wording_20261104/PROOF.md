# Natural gradient decay does imply the strict strain branch

Date: 2026-11-04T12:50:55.168674+00:00.

## 1. Exact claim under review

The captured literature scope note, SHA256 6f91361c9354e9fb071e7cdc3d5b92f96d20257c657716efa9f9c5bd0007edb9, says at line78 that the natural rate |DU(y)|=O(|y|^(-1/c)) "neither forces U=0 nor establishes the strict small-strain premise Lambda<1 at infinity". The second assertion is false. The issue is the implication from the natural rate, not the separate unproved implication from velocity decay to that rate.

Here c>0, U is a C1 divergence-free vector field on R3, S=sym DU, and Lambda=limsup_(|y| to infinity) lambda_max(S(y)). These hypotheses include the bounded C2 profile class of the already confirmed A476-A477. No profile equation, pressure normalization or finite-energy premise is needed for the elementary implication below.

## 2. Complete argument and corrected wording

Assume there are finite C,R0 such that ||DU(y)||<=C|y|^(-1/c) for |y|>=R0. Since c>0, the right side tends to zero. For every y, trace S=div U=0, so lambda_max(S)>=0. The operator norm inequality gives

    0 <= lambda_max(S(y)) <= ||S(y)|| <= ||DU(y)||.

Therefore Lambda=0, and in particular Lambda<1. This is also one of the explicit equivalences in Section1 of the A476-A477 reconstruction. No unknown global profile needs to be constructed to refute the printed denial of this implication.

For completeness, the preceding physical-to-profile implication in the scope note is valid. Write tau=T-t. The rotating similarity change of variables has |y|=tau^(-c)|x| and

    grad_x u(x,t)=tau^(-1) Q(tau) DU(y) Q(tau)^T,

with Q orthogonal. If grad_x u is uniformly bounded for sufficiently small tau throughout a fixed annulus a0<|x|<b0, choose any r0 strictly between a0 and b0 and tau=(r0/|y|)^(1/c). For every sufficiently large y its associated x has norm r0. Hence ||DU(y)||<=C tau=C r0^(1/c)|y|^(-1/c). This gives Lambda=0 by the preceding inequality, for every fixed finite omega.

Replace the two opening sentences of the affected paragraph by:

> Uniform physical gradient on an annulus gives the natural profile rate |grad U(y)|=O(|y|^(-1/c)) by the exact similarity scaling. This rate implies Lambda=0, hence Lambda<1, but does not alone establish U=0. The missing implication is from velocity decay alone to either this rate or the strict strain premise.

The subsequent exact A476-A477 hypotheses and the final bounded-profile dichotomy sentence may remain. The separate period clarification omega!=0 is correct by A030; it is not affected by this repair.

## 3. Method, verdict and transfer boundary

The entire91-line current scope note, all four hunks of its displayed diff, the exact A476-A477 ledger statements and the A476 reconstruction's statement were read. The period proof was also read completely. No fresh audit of all external manuscripts in the note is claimed. The actual evidence directory contains separate diff files; in the team records itself lists hashes and replacement counts, not the textual deltas. The reading-scope correction is retained and explicitly distinguishes the initial incomplete reading from its subsequent completion.

REFUTED for the quoted implication denial at this exact source hash. A476-A477 remain CONFIRMED at their original hypotheses. No occurrence of the offending phrase was found in the coordinator's current report, so the approved report9836a8ea and its A3239 verdict are unchanged. A local literature-note repair is pending. The main conjecture remains OPEN. This is an editorial repair to an existing implication, not a new mathematical direction after the freeze.
