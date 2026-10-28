# Independent derivation checks

The increment kernel is the complex conjugate of z/[pi(z^2-1/4)^2].
Its leading exterior angular harmonic has order +3. Pairing it with
the input exp(-3i theta) therefore has the correct phase.

The angular shift is 2t, so the multiplier has modulus2 sin(3t), not
2 sin(6t). The input chord length is2r sin(t). These factors give the
limiting upper coefficient2/3 after integration of r^(alpha-2).

The remainder estimate expands (1-w)^(-2), with |w|=1/(4r^2); its
coefficient8/(9pi r^5) integrates to16/[9(3-alpha)]. It has no endpoint
pole at alpha=1.

For the potential, the two complex derivatives contribute factors
alpha+5 and alpha+3. The Laplacian denominator is(alpha-1)(alpha+5),
and S contributes a factor1/2. Thus the output coefficient is positive
(alpha+3)/(2(1-alpha)), with no local identity term omitted.

The radial-power seminorm argument treats all pairs, including the
origin. The resulting H_alpha tends to1. A global3-Lipschitz input
map, followed by that radial power, gives a sufficient input seminorm
bound tending to3. The lower coefficient is consequently2/3.

Status: analytic proof written and independently re-derived. Team
cross-reading remains requested before integration in the lead report.
