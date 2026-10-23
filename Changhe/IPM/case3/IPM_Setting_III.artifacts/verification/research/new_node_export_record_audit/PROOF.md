# New160 and oversampled128 node-export record audit

Written UTC 2026-10-22T06:01:45.458359+00:00, before implementation and before these exports are read.

This audit concerns producer arrays on6400 standard160x40 nodes and12288 oversampled128x32 rows. It checks record consistency and arithmetic on the exported velocities. It does not independently recompute those full-node inverses. Result320 remains a separate frozen computation on its own targets.

For exact dyadic operands x,y,g,g_x,g_y,V_1,V_2 and c=2 define E=x g_x+y g_y and A=V_1 g_x+V_2 g_y. The auxiliary residual and prompt denominators are

R=2E+A-g,
N_f=|2x g_x+V_1 g_x|+|2y g_y+V_2 g_y|+|g|,
N_v=|g|+|E|+|A|.

These equal the expanded transport quantities by distributivity. Import each finite binary64 operand as an exact Fraction. Compute these five quantities, rounding only for stored summaries. A zero denominator gives an undefined ratio, recorded as null or NaN, never zero by fiat. With positive denominator underflow would be rejected rather than hidden.

The exports' binary64 R_h and N_f are compared with the exact values. For standard separate binary64 round-to-nearest operations and no underflow or overflow, a conservative path bound is gamma_8 N_f, gamma_8=8u/(1-8u), u=2^-53. Indeed each transport product involves at most one exact multiplication by2, one rounded addition, and one rounded multiplication, followed by at most two additions or subtractions. The usual multiplication of the factors(1+delta), |delta|<=u, bounds the summed absolute errors by gamma_8 times the exact sum of the three absolute terms. The same bound covers N_f. We check normal-range nonzero intermediates. This bound checks finite arithmetic only and does not estimate inverse error or field interpolation error.

Reconstruct expected coordinates independently from stored radial nodes t_i (i>=1), r_i=sqrt((1+t_i)/2)/(1-t_i)^2, and angles(j+.5)pi/(2m), where m=M or3M. Because separate libraries may differ by last bits, record coordinate discrepancies and require componentwise scaled error at most32u. Match source hashes and parameter metadata to the already frozen states. The radial/angular enumeration is radial-major. Physical hypot radii define half-open regions[0,.1),[.1,1),[1,100),[100,infinity). First occurrence resolves ties. Store each regional max|R|, max|R|/N_f, max|R|/N_v with the signed residual, its own denominators, and coordinates. Recompute both export-arithmetic maxima and exact-operand maxima, distinguishing them. Compare producer rounded tables by exact decimal half-ulp intervals; no historical execution authenticity follows.

At only the deterministic first/middle/last rows and union of regional maximizing rows, compare the three density jets with the verifier's independently implemented Cartesian analytic derivatives. This selected check does not turn all-node inverse records into independently evaluated inverses. The gradient error is stated as a finite discrepancy with a1e-10 times(1+|jet|) acceptance tolerance; it is not a certified differentiational error bound. Axes are not nodes in these sets; zero-denominator behavior is manufactured separately. Further candidate evaluation and any uniform bound remain OPEN. No conclusion about primary IPM existence or nonexistence follows.

Dependencies: the exact auxiliary residual algebra above, the previously independently implemented coefficient reader and Cartesian differentiation, and finite frozen exports with their metadata. No producer Python is imported or executed. All writes stay in the verifier lane. No JS/TS/Node, servers/listeners/tunnels, RLScience, Lean/Lake, commits/push/posts or contact with people. At most one heavy numerical process is permitted; this record audit is a short foreground calculation.
