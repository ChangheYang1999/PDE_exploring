Prerequisite repair plan, recorded before the new helper qualification:

Retain the exact saved source samples, nodes, weights, tail constants and all raw moments. Convert them once to long double and use the already qualified scaled Green recurrence and angular synthesis. This changes arithmetic only. It does not improve or certify the source quadrature itself.

Check all complex pressure and radial-derivative coefficients against direct70-digit sums at2 R0 and65536 R0, for the saved S01 and V027 base, c_l and omega pressure data. Check the reconstructed P and gradient at three directions against those coefficients with the independently qualified angular table. Require relative differences <=1e-8, the previous helper tolerance. Report absolute differences, conditioning and all original-versus-new differences without treating old float64 values as exact references.

For the stable linear term use long-double radial and angular evaluation. Compare against70-digit direct physical-coordinate values on the two original inputs, three directions, and radii1e-6,0.25,3,4096,65536 times R0. Require relative error <=1e-11, the previous helper tolerance. Both original failures remain recorded.
