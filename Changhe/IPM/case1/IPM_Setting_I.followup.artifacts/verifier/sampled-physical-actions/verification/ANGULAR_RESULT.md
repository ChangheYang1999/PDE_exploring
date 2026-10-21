# Sampled physical linearization: angular refinement

Date: 2026-10-20. Numerical audit, no continuum spectral conclusion.

The two exact input snapshots are dnB_n96m40S.npz (md5 f5b77e128474f1f9da8e3051c22ad505) and dnSB_n120m48.npz (md5 0234b3634f747b0a50386d0359bea823). The 58 observation points were fixed before evaluation. At each grid the columns are the first ten reconstructed right Ritz directions and four independently chosen, twice orthogonalized smooth nodal variations. The direction files fix their normalization and signs. No evaluator from the numerics lane is imported.

For coefficient vector z use the finite domain norm

    ||z||_X^2 = (1/58) sum_i [delta rho_z(X_i)/(1+|rho(X_i)|)]^2 + (delta c_l,z)^2.

The output is the numerator variation delta R at these points, divided by the fixed base normalizer N_f=|rho|+sum_i|W_i partial_i rho| and sqrt(58). This is not the derivative of a changing normalizer. QR whitening of the domain map gives the reported singular values. In each comparison the 4096-angle inverse and finest Cartesian gradient fix the same normalizer for both matrices. The auxiliary far-field parameter C is represented through the chosen columns; no separate C weight is silently added to this physical norm.

| Columns | Grid | Smallest singular value | Domain-map condition | Minimum output norm with delta c_l=1 |
| --- | --- | --- | --- | --- |
| 4 | 96,40 | 0.00286249106143 | 41.1646 | 0.00302262447802 |
| 4 | 120,48 | 0.00160316224149 | 40.8784 | 0.00161416177938 |
| 10 | 96,40 | 0.00229824432901 | 233.078 | 0.00245697534157 |
| 10 | 120,48 | 0.000613758680987 | 238.621 | 0.00105728860432 |
| 14 | 96,40 | 0.00213789300872 | 364.557 | 0.00236509534636 |
| 14 | 120,48 | 0.000529268776097 | 368.741 | 0.000732710505139 |

Both angular rules use radial Gauss order24, logarithmic panel width at most0.1, and outer radius10^30. Doubling angles from2048 to4096 changes the full14 whitened matrices by Frobenius norm5.8343652e-11 and5.9846150e-11, respectively. Their spectral changes are smaller, and the maximum singular-value changes satisfy the finite-matrix perturbation inequality. Radial refinement is a separate computation.

Density gradients use Cartesian eighth-order differences at relative steps1/4000,1/8000,1/16000,1/32000. Comparing either of the two middle steps with the finest changes the full14 matrices by at most1.40613e-9. An independently differentiated polynomial chain rule changes them by8.98491e-10 and7.84790e-10. The original1/4000 differences were larger, up to2.36305e-7, which is why the refined gradient is used. These are observed numerical differences, not certified rounding or quadrature error bounds.

The exact outer-tail majorants, propagated using the numerical gradient values and the absolute whitening matrix, give full14 Frobenius upper estimates1.83367e-9 and3.48848e-9. Only the velocity exterior is rigorously enclosed; these propagated numerical-gradient estimates do not enclose the complete matrix error. The unresolved inner disk, interior quadrature and floating arithmetic have not been given interval bounds here.

The 59-coordinate sampled domain spaces have, for10columns, principal cosines with last two0.982319 and0.599430; for14columns the last two are0.982456 and0.594913. Distinct base-density denominators are retained. This finite comparison is not convergence in a continuum function space.

Verdict: CONFIRMED as a numerical finite-sample and finite-span audit. These minimum singular values are positive only on the specified spans. The constrained costs are upper bounds for the corresponding infimum on any larger admissible space, not lower bounds there. They neither establish isolation nor a kernel nor a family. The base fields' maximum normalized residuals on these same58points are0.00548170121946 and0.00262698137479. No endpoint follows.

Reproduction: run code/summary_gradients.py --refined, code/cl_cost.py --refined and code/summary_all.py after the completed actions files. The summary_all_angular.json and summary_all_angular_matrices.npz contain all values, input hashes, matrices, minimizers and reconstruction checks. Do not substitute the earlier summary.py, which used a coarser density gradient.
