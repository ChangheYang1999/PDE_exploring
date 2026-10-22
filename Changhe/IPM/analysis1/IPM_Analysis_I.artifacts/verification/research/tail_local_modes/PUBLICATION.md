# Finite-mode bounds for the higher exterior repair

Use PROOF.md with ADDENDUM.md and CLOSURE_NOTES.md. The overall current
acceptance status is recorded in evidence/verdict.json when finalized.

For the exact topic106 family, every admissible cutoff
T>=max(R_b,L,1)=R_b, with R_b>3412.96685816, obeys the following strict
bounds on the disk |X|<=9:

| order j | every individual velocity component or Cartesian partial |
|---|---|
| 0 | <1.006144e-11 |
| 1 | <3.394241e-12 |
| 2 | <7.827257e-13 |
| 3 | <1.056035e-13 |

These are upper bounds for U[rho_T-rho0], not measured values or full
vector/tensor norm bounds. Both independent methods use the conservative
comparison T=3000; monotonicity transfers the result to every admissible T.

At the original source P=(p,0), the resulting strict lower bound is

 |partial_y F(rho_T,c0)(P)|>6.6989e-7.

The new estimate separates the small fifth angular sine coefficient after
exact strain compensation. The three physical fifth-sine coefficients
are approximately0.01721261812862, -6.107958081865, -1492.795538213.
These displayed approximations are explanatory only; exact endpoint
intervals are in the two engine outputs. Higher angular modes are all
included. Arb512 evaluates6240 finite positive derivative terms; the
independent iv180 method uses the quotient coefficient sum and a proved
positive geometric tail, giving a slightly larger sufficient majorant.
The two majorants have different values and are not compared by overlap.

The complete audit checks249 prior pins, original2600 binary coefficients
and1573knots,782 angular basis vectors,306935 projected coordinates,
6240 derivative weights,4 exact geometric sums,1024 tail-ratio tests,
8 strict ceiling tests,12 majorant-order comparisons, source bounds,
the exact admissible radius, and two full output reruns. It explicitly
reuses the two independently certified full H2 arrays of topic113.
No third independent convolution is claimed.

This closes the cutoff-range gap of topic113's local nonstationarity
result. It concerns only the exact specified family. The family could
be corrected further. It excludes no surrounding neighborhood, gives
no upper bound making the global forcing small, and supplies no linear
inverse, stationary solution or decisive task endpoint.
