# What the single-harmonic support criterion classifies

Status: PROVED in V519 after independent review at18:06Z. The stronger classification by actual compatibility is not established by this support argument.

## Statement

Let h>=2 and Q>2h be integers, with Q odd. For an odd positive M put

    K_M={M s+e: s=-Q,-Q+2,...,Q; e=-(Q-1),-(Q-3),...,Q-1}.

Let t=2h-3 be the first compatibility frequency and u=2h-1 the fixed response offset. Then

    t not in K_M if and only if M>Q+2h-4,
    u in K_M if and only if M<=Q+2h-2.

Consequently M=Q+2h-2 is the unique odd positive frequency for which the first compatibility coordinate is absent from the support bound and the fixed response offset is present in that bound. This is a classification of the support test. It is not a classification of every leading harmonic whose actual first compatibility coefficient vanishes.

## Proof

For v equal to t or u, v is positive and odd, and v<Q. If M<=v+Q-1, the allowed odd sum s=1 gives v=M+(v-M). The even integer v-M is at least -(Q-1) by hypothesis and at most Q-1 because v<Q and M>=1. Hence v belongs to K_M. If M>v+Q-1, every allowed s is odd and nonzero, so |Ms+e|>=M-(Q-1)>v. Thus neither v nor -v belongs to K_M. This proves both equivalences.

The simultaneous inequalities are Q+2h-4<M<=Q+2h-2. Their endpoints are odd and differ by two, so exactly one odd M satisfies them, namely the upper endpoint.

The actual support is only a subset of K_M. A coefficient at a frequency in K_M may still cancel. Therefore the implication from missing support to vanishing coefficient cannot be reversed without a separate noncancellation theorem or exact calculation for every remaining case. No such theorem is supplied by the support induction alone.

## Audit consequence

The sentence in theory version47, Corollary T_(Q,h).9(a), calling this M the only single harmonic for which the first condition holds identically and the support test does not force eventual response vanishing, is stronger than its proof. The supported formulation is: the only frequency for which the first condition is forced by this support bound and the same support bound does not force eventual response vanishing. This correction does not affect any certified center or convergence radius.

Dependencies: the signed-support inclusion and fixed response alternative in201; elementary integer arithmetic.

The corrected support-only formulation is present in theory version49. The independent review and its source hash are retained alongside this proof.
