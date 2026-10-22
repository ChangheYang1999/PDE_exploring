# Selected finite radial models: publication scope

The corrected v3 check at2026-10-21T02:31:45Z passes all261 modes on
middle cells0,4102,7808. Each engine verifies20,358 coefficient inclusions
and1,566 uniform remainder comparisons. The first engine evaluates exact
closed Taylor weights with Arb512. The second propagates affine coefficient
weights through its own ODE recursion with mpmath.iv180. Both independently
bound degree20 Taylor tails, then add the absolute orders13 through20 to
obtain a degree12 model. Candidate coefficients and radii are the frozen
producer's current-runtime reconstruction, with exact dyadic semantics.

The original smoke failure of iv dependence, and the43-mode outer-cell
failures of the derivative-only remainder method, are retained. They were
failures of sufficient comparisons, not counterexamples. The refined proof
changes neither input boxes nor producer remainder budgets.

Canonical Green-moment and spline-input membership for all modes at these
cells remains an additional obligation. Only3 of7809 middle cells are
checked, and the full field inequalities also need all angular evaluations,
range arithmetic, coverage and classification. No whole-flow certificate
or decisive endpoint follows. The second whole-middle residual method is
resumed through its unchanged audited driver and remains the priority.
