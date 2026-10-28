# Quadratic multiplier error for the actual origin extension

## Statement

Fix 0<alpha<1 and p>0. Let E_p consist of bounded continuous functions h on R^2, even in x and odd in y, with h(0,y)=0 and norm

 ||h||E_p=||h||infinity+[h]_x+[h]_(y,p),
 [h]_x=sup_(x!=x',y)|h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,p)=sup_(x!=0,y!=y')|h(x,y)-h(x,y')|/(|x|^p|y-y'|^alpha).

Let 0<delta<=1. Suppose m_delta is C1, even in both variables, supported in B_delta, and satisfies

 ||m_delta||infinity<=C0 delta^2,
 ||D m_delta||infinity<=C1 delta,

where C0,C1 do not depend on delta. Then multiplication by m_delta preserves E_p and

 ||m_delta h||E_p<=C delta^2 ||h||E_p.               (1)

Here C depends only on alpha,p,C0,C1. In particular proof 202's reciprocal coefficient m_delta=1/A_delta-1/A0 obeys (1). This improves that topic's valid but weaker bound (11).

For the exact joined normalized modal background, take the actual origin extension, canonical full-plane velocity, cutoff and maximal distributional domain of proof 202, with p=2. The extension is

 L_delta h=V_delta.grad h-h+B_delta h,
 B_delta h=chi(X/delta)(U[h]+c[h]X/3).grad rho0.

With the notation of that topic,

 L_delta=A_delta(S_delta+E_delta),
 E_delta=-m_delta+q_delta B_delta,
 q_delta=1/A_delta=q0+m_delta,
 S_delta=-x partial_x+(D_delta/A_delta)y partial_y-q0.

There are qualitative constants C_E,C_R,delta0>0 such that

 ||E_delta||E2->E2<=C_E delta^2,
 ||S_delta^(-1)||E2->E2<=C_R,

for 0<delta<delta0. If C_E C_R delta^2<1, the closed maximal-domain inverse satisfies

 L_delta^(-1)=S_delta^(-1)(I+E_delta S_delta^(-1))^(-1)q_delta,
 ||L_delta^(-1)||<=C_R(q0+C delta^2)/(1-C_E C_R delta^2). (2)

All constants depend on fixed alpha<1. No numerical inverse bound or radius is supplied. This is the explicitly localized whole-plane extension, equal to the actual operator only near the origin. It is not a full-plane actual inverse and does not close the cubic trace or a nonlinear iteration.

## Proof of the multiplier estimate

Put M=||h||E_p. Oddness in y gives the useful pointwise bound

 |h(x,y)|<=M |x|^p |y|^alpha.                        (3)

For two points on either coordinate line, splitting their separation at delta in the supremum and Lipschitz bounds gives

 |m_delta(X)-m_delta(X')|<=C delta^(2-alpha)|X-X'|^alpha. (4)

Indeed, for d<=delta use C1 delta d<=C1 delta^(2-alpha)d^alpha; for d>=delta use 2C0 delta^2<=2C0 delta^(2-alpha)d^alpha.

The supremum of the product is at most C0 delta^2 M. For an x difference, there is nothing to check if both product values vanish. Otherwise name an endpoint A=(x,y) at which m_delta is nonzero; it lies in B_delta. Let B=(x',y). Use the identity with the undifferenced h at the supported endpoint:

 m_delta(A)h(A)-m_delta(B)h(B)
 =m_delta(B)(h(A)-h(B))+(m_delta(A)-m_delta(B))h(A).  (5)

The first term is at most C0 delta^2 M |x-x'|^alpha. By (3), |h(A)|<=M delta^(p+alpha). By (4) the second term is at most C M delta^(p+2)|x-x'|^alpha. Since p>0 and delta<=1, their sum proves

 [m_delta h]_x<=C M delta^2.                        (6)

This argument also covers a supported endpoint paired with an arbitrarily distant point. If both m values vanish, the original product difference is zero.

For a y difference use the same identity, naming A=(x,y) on the support when possible. The first term in (5) is at most C0 delta^2 M |x|^p|y-y'|^alpha. At A, (3) gives |h(A)|<=M |x|^p delta^alpha. Consequently the second term is at most C M delta^2 |x|^p|y-y'|^alpha. This proves

 [m_delta h]_(y,p)<=C M delta^2.                    (7)

The slice x=0 remains zero, and multiplication preserves both parities and continuity. Equations (6), (7) and the supremum bound prove (1). The small amplitude of h on the multiplier support is essential to the improved estimate. No derivative of h is used.

## Application to the actual variable operator

Proof 202 proves that A_delta-A0 and D_delta-D0 have supremum O(delta^2), derivative O(delta), both even parities and support in B_delta. A_delta>=A0/2 for sufficiently small delta. Differentiating its reciprocal proves the same hypotheses for m_delta. Thus (1) gives

 ||m_delta||E2->E2<=C_M delta^2,
 ||q_delta||E2->E2<=q0+C_M delta^2.                  (8)

The actual background is C^(4,1) at the origin, with leading term x^2y, as verified in proof 33. Proof 212 gives the complete normalized bound

 ||B_delta||E2->E2<=C_B delta^2.                     (9)

Combining (8) and (9) yields

 ||E_delta||<=C_M delta^2+(q0+C_M delta^2)C_B delta^2
             <=C_E delta^2.                        (10)

The characteristic inverse in proof 202 applies at p=2: its positive limiting exponent is q0+2-alpha beta0=(D0/A0)(1-alpha)>0, because D0=2A0+1. Its exact formula and bound (10) there give a uniform C_R for sufficiently small delta. This endpoint application was explicitly checked in proof 203 and the V216 audit.

For completeness the domains remain exactly the maximal ones. Multiplication by A_delta,q_delta,m_delta is bounded on E2 by (1) and their constant parts. The distributional identity T_delta=A_delta(S_delta-m_delta) therefore gives

 {h in E2:T_delta h in E2}={h in E2:S_delta h in E2}.

Adding B_delta, bounded by (9), does not change this domain. The bounded perturbation of the closed S_delta graph is closed. Factoring S_delta+E_delta=(I+E_delta S_delta^(-1))S_delta and summing the operator-norm Neumann series proves (2), including uniqueness and surjectivity into the stated maximal domain. No derivative of the coefficient error is treated as a bounded first-order perturbation. Its transport contribution is handled by the characteristic inverse itself.

Dependencies: proof 202 for the precise extension and characteristic inverse; proof 203 for the p=2 applicability; proof 212 for the sharp normalized coupling; proof 33 for actual background regularity. The multiplier estimate is independently proved here after the optional observation in the independent V219 cross-audit, remark12. Only the error bound is asserted quadratic; sharpness of this particular Neumann error is not claimed.
