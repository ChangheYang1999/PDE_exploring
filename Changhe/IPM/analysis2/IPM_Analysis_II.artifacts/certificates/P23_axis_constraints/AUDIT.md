# Analytical audit of the axis constraints

Verdict: CONFIRMED V099 and V100. Actual audit time: 2026-10-28T06:59:29.706306+00:00.

1. Parity sets both off-diagonal velocity derivatives and rho_x to zero on x=0. Incompressibility supplies u1_x=-v'. This gives the displayed diagonal matrix exactly.
2. Integration of both diagonal inequalities uses q(0)=v(0)=0 and y>0. The result is necessary, not equivalent to the local matrix condition.
3. The origin ceiling c+2 follows by testing the vertical unit vector. It holds for every normalized reference with the given canonical velocity.
4. For an exact profile V>=a y>0, positivity of q follows from its linear axis ODE starting at positive y0. Division by q' is then justified by q'=q/V>0.
5. Differentiating V=q/q' gives K=q q''/(q')^2. Direct substitution yields both diagonal inequalities, not just the lower one.
6. The exponent a=1-epsilon is positive. Direct differentiation of q^a yields precisely K<=epsilon. This is an exact-profile consequence only.
7. With a residual, differentiating V=(q+f)/q' gives K_f. Multiplying out verifies the residual curvature correction in equation(11), including its sign.
8. The center cubic identity is obtained by multiplying y+d y^3 and a0+3b y^2. Its coefficient is2b+a0 d. At the critical matrix floor only, d>=0 implies b<=0 for an exact profile.
9. The axial M22 perturbation is exactly partial_y U2[h]. The Euclidean derivative embedding therefore gives denominator4 in the distance bound. No density-gradient or factor2 is lost.
10. The corrected candidate jets and all three points are evaluated by the full Cartesian Taylor program and independently assembled one-dimensional axis powers. Both match the earlier polar field values where applicable.
11. The A2/A3 distance ratios exceed12000 and5000 by Arb comparisons. Every displayed decimal interval lies outward of its saved ball; no sampled eigenvalue is used to prove global positivity.
12. A3 at(0,1) passes the density-only K bound and fails the true K_f bound. This is a concrete counterexample to dropping residual terms from the approximate-profile matrix test.

A provenance omission in the older topic19 point evaluator was corrected: its compact_matrix.py dependency is in02_energy/verification, not11_residual_norms/verification. Both A2/A3 point records and this axis record were rerun after that correction. All numerical enclosures are unchanged.
