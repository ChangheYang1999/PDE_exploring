# Independent refinement of the older anisotropic coefficient margin

## Exact statement and dependencies

Use the exact normalized joined modal density rho_0 of topics04 and68, reconstructed from the read-only original Analysis I NPZ. The canonical velocity is U=(-R_1 R_2,R_1^2), ell=1/k, V=ell X+U[rho_0], q=V.e_r/r and v=V.e_theta/r. Let

 b_plus=(|grad rho_0|-partial_y rho_0)/2,
 m_old=1+ell-(17/4)q+(17/4)tan(theta)v-b_plus for r<1,
 m_old=1+ell-(5/8)q+(17/4)tan(theta)v-b_plus for r>1.

The proposed assertion is m_old>=2927/1000=2.9270 throughout the punctured plane, with both one-sided expressions at r=1. The weight r^(-17/2) or r^(-5/4), multiplied by |cos(theta)|^(-17/2), is continuous at r=1; the weak energy identity introduces no interface measure there. Parity reduces the enclosure to the closed first quadrant. Products containing tan(theta) are interpreted through their finite trigonometric extensions at the vertical axis. Proof 82 already proves the bound5/2. A new numerical conclusion is accepted only after both production and independent coverage/replay audits succeed.

## Complete cover and replacement rule

Proof 68 gives3276 radial roots: two exact half-spans for each original nonzero spline span, followed by160 outer subintervals of width1/20 through t_plus+8. Its endpoint estimates cover t<=t_minus and t>=t_plus+8. Proof 82 preserves1754 of these roots and refines1522 roots, with128 angular roots in each refined radial root and213985 terminal leaves. Its independent audit proves coverage and all stored bounds.

For each unrefined proof 82 root, retain the root if its original proof 68 lower bound for m_old is at least2927/1000. Otherwise partition its quadrant into128 exact angular subintervals and enclose each separately. For each proof 82 terminal leaf, retain it if its recorded directed lower bound is at least2927/1000. Replace every other leaf by a finite binary partition of precisely the same rectangle. The production journal records the parent identity, exact rational endpoints, every child path and directed lower endpoint. An old leaf cannot be removed merely because a neighboring leaf or a coarser hull covers its extremes.

On each new rectangle, use proof 82's original-data interval reconstruction of all261 velocity modes and262 density modes. The angular calculation gives interval bounds for q, tan(theta)v and both components of grad rho. If G bounds |grad rho| above and L bounds rho_y below, then b_plus<=(G-L)/2. When rho_y>0 throughout the box, the additional identity

 b_plus=rho_x^2/[2(|grad rho|+rho_y)]

provides another valid upper bound. Taking the smaller of two proved upper endpoints remains valid. The independent replay assembles the angular sums in a different evaluation order at640 bits. It must prove the target; numerical monotonicity of interval endpoints across different precisions is not required.

Every new parent is either accepted or split at its exact radial or angular midpoint. A complete binary tree covers its parent and has disjoint interiors. The independent audit reconstructs all expected replaced parents from the two prior certificates, compares their identities and endpoints with the new journal, checks every tree and its stored rational lower endpoints, and ensures that no expected parent is omitted or repeated. Together with the retained roots and leaves, these checks give a complete finite cover.

## Both analytic half-lines

Use the exact certified endpoints E_P,E_T,G from proof 68, where E_P bounds the sum of velocity radial coefficients after subtracting the origin limit, E_T bounds the weighted angular coefficient error and G bounds |grad rho|. Reassembling at512 and640 bits gives

 m_old>=1+ell+(17/4)(2ell-1)-(17/4)(E_P+E_T)-G near the origin,
 m_old>=1+ell-(5/8)(ell+E_P)-(17/4)E_T-G at infinity.

These are the uniform half-line inequalities proved in proof 68. Their interval inputs are exact rational outward endpoints tied by hashes to the original source and canonical Green cache. Both must exceed the same target2927/1000. A finite cover alone would not prove the global bound.

## Scope

The result, if accepted, certifies only this coefficient margin and strengthens proof 82 for the older anisotropic weight. It does not prove injectivity of the complete coupled linearization, a complement inverse or nonlinear existence. The numerics team's separate claim of the same bound is independently supported only when the present original-data certificate passes; the generic merge program remains subject to proof 178's coverage counterexample. The newer decoupled margin of proof 186 is a different quantity and is unchanged by this calculation.

Dependencies: topics04,68 and82, their exact original-data reconstruction and complete partition audits. Acceptance status and real computation times are stored in evidence and VERIFICATION_RECORD.md.

## Accepted original-data certificate

At 2026-10-28T13:16:54.184670+00:00, production and the independent audit both passed. The whole-plane inequality m_old>=2927/1000 is CONFIRMED. The cover retains1352 complete radial roots and199494 old angular leaves, replaces65947 parents by82041 new leaves, and therefore contains1352 complete radial roots plus281535 angular rectangles. Every parent and binary partition is checked exactly. All34 independent640-bit angular replays and both analytic half-lines prove the target. The production used512-bit Arb arithmetic and all stored directed rational endpoints. The run took338.54 seconds; the independent audit took94.27 seconds. These are actual measured durations.

The replay is a separate evaluation of the same certified original-data radial enclosures. It checks representative and worst new rectangles, while exact journal auditing checks every new lower endpoint and parent partition. The production proof supplies the universal enclosure, not a statistical extrapolation from the replay sample. No truncation beyond the exact finite angular expansion is used. The coefficient margin is independent of the numerics team merge heuristic and does not establish a full inverse.
