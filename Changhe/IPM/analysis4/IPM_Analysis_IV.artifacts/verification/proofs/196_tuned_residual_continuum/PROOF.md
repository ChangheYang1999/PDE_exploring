# Continuum residual checks near the empirical tuned-series radii

Status: finite continuum checks CONFIRMED for ['Q5r6', 'Q6r1', 'Q6r6'], under the stated coefficient-enclosure hypotheses; no new infinite-radius assertion.

## Statement and scope

Consider the normalized two-mode branches Q5 root6 and Q6 roots1,6, with delta=2/Q, c=Q/(Q-2), and f_1=sin(theta)+b sin(3theta). Root indices refer to the increasing real roots in topics130 and154. The exact branch and its tuned free harmonics are fixed by the previously proved compatibility and response theorems. The source coefficients through order81 come from the specified completed interval checkpoints, with all free harmonics through that order determined. Their enclosure status is subject to the producer induction in194 and the independent prefix checks in180/185; the source hash and retained extension identify the precise finite input.

For each specified positive rational radius R and truncation N in{10,20,40,80}, this audit encloses the continuum angular supremum of the density-weighted stationary residual, its first two angular derivatives, and the first omitted term and its first angular derivative. It also encloses the weighted density partial sum at angles3/10,9/10,13/10. All conclusions concern these finite truncations. In particular, a decrease or increase of these residuals at finitely many orders does not prove an infinite convergence threshold.

## Exact Cartesian residual identity

Use the Laurent representation and Cartesian operators X_q,Y_q from191: the physical sine field is -i times its real antisymmetric Laurent representative. Put z=R^(-delta), p_n=1-n delta and P_n=2-n delta. Define the finite Laurent sums

    A = sum_(n<=N) z^(n-1) X_(P_n) G_n,
    B = sum_(n<=N) z^(n-1) Y_(P_n) G_n,
    C = sum_(n<=N) z^(n-1) X_(p_n) F_n,
    D = sum_(n<=N) z^(n-1) Y_(p_n) F_n.

The Laurent representative of the weighted stationary residual is

    E = -(c-1) sum_(n<=N) (n-1) z^(n-1) F_n + z(AD-BC).

This follows directly by Cartesian differentiation and multiplication of the finite fields: each nonlinear pair has weight z^(i+j-1), while the stationary linear coefficient is -(n-1)(c-1). It also follows from the ordered-pair identity in188. The present computation keeps the low-order cancellation inside the finite arithmetic instead of invoking cancellation to remove those terms. Thus it independently tests the weighted signs and all pair contributions through a product of finite sums. The first omitted weighted density term is z^N F_(N+1).

Every operation in this formula is finite. Outward interval arithmetic therefore encloses E whenever the input coefficient balls enclose the exact branch. Known S1 parity justifies reading the sine coefficients after checking all unwanted coefficients contain zero. Exact parity follows from the original recursion, not from that numerical containment test.

## From samples to the full circle

For a real trigonometric polynomial H(theta)=sum_m a_m sin(m theta), the kth derivative has second derivative norm at most M_2=sum_m |a_m|m^(k+2). On a uniform grid theta_j=j pi/L, the linear-interpolation remainder on each subinterval is at most (pi/L)^2 M_2/8. The absolute value of the linear interpolant is at most the larger absolute value at its endpoints. Consequently the largest interval sample upper bound plus that remainder bounds the continuum supremum, and the largest sample lower bound bounds it from below. S1 parity gives the same absolute supremum on the full circle. For odd k one samples the cosine polynomial; the irrelevant common derivative sign does not affect the absolute value.

The computation evaluates each grid sample by complex interval polynomial evaluation at exp(i theta_j). It uses the same elementary interpolation proof as162, with independently formed Cartesian residual coefficients. Strict inequality between the upper bound at one truncation and the lower bound at another certifies the corresponding finite decrease or increase. Comparison with the numerical experiments' binary64 sampled maxima retains those reported values as numerical evidence; it does not silently identify them with the exact supremum.

## Dependencies and limitations

The algebraic roots and tuned branches are established earlier;194 proves the producer enclosure induction under its stated arithmetic and execution hypotheses. Topics180/185 provide separate low-order reconstructions. Topic191 checks the Q5root6 and Q6root6 Cartesian equations through300. Topic188 supplies an independent analytic residual derivation, and162 supplies the interpolation argument. Source hashes, archived extensions, exact rational radii, arithmetic precision, grid size, interval outputs and actual elapsed times are retained with each completed case. No global extension or new infinite convergence radius follows from this finite audit.

## V396 | 2026-10-31T14:35:29+00:00 | Q6r1 continuum residual audit

Claim: Q6r1 reported finite residuals and omitted terms agree with independently formed continuum bounds.

Method: Independent finite Cartesian residual sums, 1024-bit interval polynomial evaluation at 2049 angular points, and a second-derivative interpolation bound on every intervening interval. Fresh source and archive checksums were verified.

Result: For Q6r1, the 12 pairs N in {10,20,40,80}, R in {256,512,1024} yield continuum residual bounds through two angular derivatives and first-omitted-term bounds through one derivative. All 60 reported sampled values lie within the one-percent comparison tolerance. Three partial-sum angles are also enclosed at every pair. Runtime 33.79047672776505 seconds. All bounds and strict finite comparisons are retained in topic196.

Verdict: CONFIRMED as finite interval calculations under the coefficient-enclosure hypotheses in194. They do not prove a sharp convergence radius or imply convergence from a finite decreasing sequence;194 separately records the algorithmic enclosure proof and its team review status.

## V397 | 2026-10-31T14:35:29+00:00 | Q6 root1 finite decay counterexample

Claim: The finite tested residuals decrease geometrically at every R>=512.

Method: Compare disjoint continuum supremum enclosures at N=40 and N=80.

Result: At delta=1/3, root b=-0.608726913792658..., R=512, the weighted residual supremum lies strictly between0.0005197 and0.0005206 at N=40, and between0.0007497 and0.0007501 at N=80. It increases by a factor greater than1.44. Thus the14:26 numerical note claiming geometric decay at R>=512 fails at its stated finite orders. At R=1024, all three successive residual decreases in N=10,20,40,80 are certified; neither fact bounds the true infinite-series threshold.

Verdict: REFUTED at R=512 for the stated finite truncations. Eventual convergence or divergence at R=512 remains undecided by these data.

## V398 | 2026-10-31T14:35:29+00:00 | Q5r6 continuum residual audit

Claim: Q5r6 reported finite residuals and omitted terms agree with independently formed continuum bounds.

Method: Independent finite Cartesian residual sums, 1024-bit interval polynomial evaluation at 2049 angular points, and a second-derivative interpolation bound on every intervening interval. Fresh source and archive checksums were verified.

Result: For Q5r6, the 24 pairs N in {10,20,40,80}, R in {4,8,16,32,64,128} yield continuum residual bounds through two angular derivatives and first-omitted-term bounds through one derivative. All 120 reported sampled values lie within the one-percent comparison tolerance. Three partial-sum angles are also enclosed at every pair. Runtime 65.90480730589479 seconds. All bounds and strict finite comparisons are retained in topic196.

Verdict: CONFIRMED as finite interval calculations under the coefficient-enclosure hypotheses in194. They do not prove a sharp convergence radius or imply convergence from a finite decreasing sequence;194 separately records the algorithmic enclosure proof and its team review status.

## V399 | 2026-10-31T14:38:27+00:00 | Q6r6 continuum residual audit

Claim: Q6r6 reported finite residuals and omitted terms agree with independently formed continuum bounds.

Method: Independent finite Cartesian residual sums, 1024-bit interval polynomial evaluation at 2049 angular points, and a second-derivative interpolation bound on every intervening interval. Fresh source and archive checksums were verified.

Result: For Q6r6, the 24 pairs N in {10,20,40,80}, R in {16,32,64,128,256,512} yield continuum residual bounds through two angular derivatives and first-omitted-term bounds through one derivative. All 120 reported sampled values lie within the one-percent comparison tolerance. Three partial-sum angles are also enclosed at every pair. Runtime 66.61662097927183 seconds. All bounds and strict finite comparisons are retained in topic196.

Verdict: CONFIRMED as finite interval calculations under the coefficient-enclosure hypotheses in194. They do not prove a sharp convergence radius or imply convergence from a finite decreasing sequence;194 separately records the algorithmic enclosure proof and its team review status.

## V405 | 2026-10-31T14:43:09+00:00 | Q6root1 continuum residual extension to R2048

Claim: The reported finite residual and next-term quantities decrease at R2048 for N10,20,40,80.

Method: Recompute the finite Cartesian residual in interval arithmetic and bound each angular supremum with a rigorous interpolation remainder; compare disjoint enclosures.

Result: The extended1024-bit continuum check includes R2048 as well as256,512,1024. At R2048 all fifteen successive decreases are certified across N10,20,40,80 for residual angular derivatives0..2 and next-term derivatives0..1. The N80 weighted residual supremum is strictly between7.3707e-20 and7.3740e-20. All80 sampled comparisons across16 pairs pass. Runtime 48.25570409791544 seconds. The original three-radius receipt remains retained.

Verdict: CONFIRMED at the stated finite truncations. These inequalities do not determine the true infinite-series convergence threshold.
