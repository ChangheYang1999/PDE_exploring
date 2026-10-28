# Foundational proof re-audit

This check reads the three proofs identified by SHA256 in verification.json. It introduces no new theorem.

The fundamental solution is -log|x|/(2 pi). Its diagonal Hessian equals the displayed principal-value kernel minus one half of the identity; its mixed Hessian has no local term. The sum of the two diagonal distributions is -delta. The Fourier multipliers are -xi_i xi_j/|xi|^2, and the traceless pair rotates through twice the spatial angle. Rotation by pi/4 exchanges the component norms, and rotation by pi/2 exchanges the signs of T_xx. These operations preserve the real homogeneous Euclidean Holder seminorm.

At each pole, subtracting the pole value gives an integrable radial majorant r^(alpha-1). At infinity the difference of kernels gives r^(alpha-2), integrable precisely for alpha<1. Subtracting a fixed exterior reference kernel therefore defines an operator modulo constants. A different reference changes only the additive normalization.

The compact approximation is not a claim of norm density in the big Holder space. Scalar clipping, or metric projection to a complex disk, preserves the seminorm. The cut-off error for a bounded clipped function is at most a constant times its height times N^(-alpha), which vanishes as the cut-off radius tends to infinity. Mollification preserves the seminorm and gives smooth convergence on fixed compact sets. Taking these operations successively, together with the uniform increment-kernel majorants, preserves every fixed operator increment in the limit. This proves equality of the test-function and homogeneous sharp constants without asserting false norm density.

The finite-transport upper estimate needs only a positive transport plan for the signed finite truncation. The dual identification is on the snowflake metric |x-y|^alpha. The deleted local and exterior terms have uniform explicit bounds, so passing to their limits does not require transporting an infinite positive mass. The same compact approximation justifies the lower test functions.

For a scalar real kernel acting on complex inputs, projecting the output increment to its complex phase reduces the estimate to the real operator bound. This does not identify that norm with the complex-valued operator T_xx+i T_xy, whose two components are coupled. The complex disk projection used in the approximation is nonexpansive in Euclidean distance, so it also preserves the modulus Holder seminorm.

No defect found in these steps. Earlier endpoint, full-norm and complex-norm distinctions remain in force.
