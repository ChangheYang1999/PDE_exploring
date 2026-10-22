# Proof corrections and implementation domain

The first reviewer identified a real endpoint error in the abstract Taylor statement: Q=7 leaves the forcing coefficient g_7 in the residual. The assertion and bound in PROOF.md are to be read with Q>=8 throughout. The actual checker uses Q=16 and explicitly asserts Q>=8. At Q=7 the correct residual would include -s h g_7 u^7. No numerical run uses that case.

Every exact radial subcell is required to lie inside one original spline span; this is asserted before computing its center and subnodes. C6 continuity is used only to identify endpoint derivative values at shared joins, never to extend a span polynomial across a knot. The archive anchors are I(a) and J(b) for that same span.

The scalar c_l is constant, so X maps to c_l X is affine and has zero second derivative. The letter D in operator polynomials denotes d/dt; the fourth tensor sum denoted D in PROOF.md is a scalar sum, not that operator. The source computation keeps these as distinct variables. For J propagation the exponential rate is -(m-4), including the zero-rate mode n=2. The density derivative polynomials are differentiated in the unscaled variable t-t_c, then their coefficients are multiplied by h^l for evaluation at t-t_c=h u. Thus no missing h^(-j) factor occurs.

The series center propagation, whole-subcell ODE residual, transformed derivative remainder, Bernstein range and trace-decomposition Horner range will all be checked as one numerical chain. Moment overlap tests are diagnostic only. Each engine must separately establish its entire finite norm bound. The source moment archive remains an explicit shared dependency.
