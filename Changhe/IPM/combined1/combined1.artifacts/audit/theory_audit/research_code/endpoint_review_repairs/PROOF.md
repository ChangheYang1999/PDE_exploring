# Acceptance of the repaired endpoint review

## Exact claim and hypotheses

The five repairs requested in T4-385 concern the independent T2 review
of T4-375. They do not change the theorem: if q < 0, h is real C1,
H_q(h) <= H, b is C1 on the circle, and r^(-q) h(r,theta) converges
uniformly to b(theta), then

 H >= sup_theta max(|b(theta)|, sqrt(q^2 b(theta)^2+b'(theta)^2)).

Here H_q is the maximum of the weighted amplitude and gradient suprema,
with weights (1+r)^(-q) and (1+r)^(1-q). In the three repaired-reference
applications q=gamma-4 and b=(A+(m/pi)P)/(4c), under all hypotheses of
T4-335 and T4-351. This acceptance concerns the repaired review text,
not a new proof of the folded-kernel upper constant in its remark R3.

## Argument and comparison

The theorem follows by scaling h_R(X)=R^(-q)h(RX). On a disk away from
zero its Lipschitz constant is at most H times the maximum of
(|X|+R^(-1))^(q-1). Uniform convergence transfers this bound to
|X|^q b(arg X). Taking the disk radius to zero gives the gradient
bound at each point. The amplitude inequality follows directly from
the weighted supremum. Polar differentiation at unit radius gives
(qb,b'). No derivative of an asymptotic error is used.

For b=(A+tP)/(4c), minimizing at one fixed angle over t is a distance
to the line spanned by (qP,P'). If that vector is nonzero the distance
is |q||AP'-A'P|/(4c sqrt(q^2P^2+P'^2)); if it vanishes the distance
is |(qA,A')|/(4c). Taking the supremum of these lower bounds is valid.
It need not equal the minimax over a single common t. The repaired
review states this distinction and leaves the FLOAT saddle inference
OPEN.

The accepted exact pointwise budgets and the positive error term in
CI imply the universal-E cap already proved in T4-380 and T4-381.
For 013 the radius lower bound 19280 and the cap upper bound
1.2484e-6 were too tight. The repaired common statements
r_grad >= 19279.98 and cap < 1.2485e-6 agree with the accepted complete
Arb records. The displayed per-candidate bounds are now outward.

The review now gives its actual first save, 10:19:20Z, and its actual
repair save minute, 10:46Z. The erroneous anticipated 10:40Z finish is
identified in its history. The three new scripts, results and logs are
frozen here; their current hashes equal the full hashes printed in
section 4. This is a provenance comparison, not execution of those
scripts. The original accepted review is retained and the complete
diff is saved.

Remark R3 is explicitly awaiting separate audit. Its revised code
keeps the beta interval arithmetic in Arb, parses the full B4c ball,
and directs the relevant float conversions outward. That repairs the
identified conversion mechanism. A full proof and validation of its
million-cell integral are still required before accepting the numeric
upper constant 1.749109. The inherited label "proved" in one output
table is explicitly limited by the review to an unaudited Arb result.

## Verdict and scope

CONFIRMED: all five T4-385 repair requests are satisfied in the frozen
review. T4-375 remains AUDITED, with no change in theorem or candidate
status. T2 R2 was independently confirmed by T4-380, and R4 by
T4-386. The universal lower bound is also AUDITED through T4-391 and
the normalized extension through T4-396. R3 remains OPEN here.
No foreign code was executed and no numerical calculation repeated.
