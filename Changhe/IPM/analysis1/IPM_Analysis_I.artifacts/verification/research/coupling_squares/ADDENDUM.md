# Clarifications after the first model review

The R_j convention in PROOF.md is self-adjoint with a real-valued symbol. Each R_j alone maps a real-valued function to an imaginary-valued one because its symbol is odd. The complex Hilbert-space proof is unchanged; the products R_1R_2, R_1^2 and the physical U preserve real-valuedness.

D in the double-commutator identity is not asserted to be negative as an operator. It enters the energy identity with a minus sign. The proof uses its absolute norm bound.

All matrix positivity used in(4), (5) and(8) is global, as are the bounded coefficients and their finite Wiener integrals. A smooth global majorant is one sufficient choice, but smoothness is not required in addition to the explicitly finite Wiener norms. Choosing b=b_+ without checking those norms is not allowed; it can fail at zeros of (a,c). The source estimate in section4 does not assert that its local coefficient data give a global positive matrix or the global commutator constants.

For section5, the precise cone statement is h(r,theta)=r^k(Theta(theta)+e(r,theta)), with ||e(r,.)||_L2(cone) tending to zero and 0<||Theta||_L2(cone)<infinity. The displayed integrability equivalence is for the tail restricted to that cone. For a whole-plane equivalence, impose this asymptotic globally in angular L2, or additionally bound the complementary angular regions. Divergence on the one cone already proves global divergence. A bounded escape factor does not change either conclusion.

The review's phrase that the directional gap449/1000 absorbs only epsilon approximately0.9 describes the range epsilon<=2lambda of the quadratic branch. It is not the full absorption threshold: for epsilon>=2lambda, F_lambda(epsilon)=epsilon-lambda, which is still below kappa when epsilon<kappa+lambda. No numerical absorption or local inverse improvement is claimed here.
