# Combining two finite physical sampling norms

Date: 2026-10-20. This protocol and its elementary matrix proof are written before the second-sample results are complete. The result concerns specified finite arrays, not an operator on a function space.

## Data and statement

Fix one frozen state and the same k ordered parameter directions in both experiments, with k in {4,10,14}. The first experiment has58 physical points with equal field weights and the second has64 prescribed Gauss points with positive weights summing to one. In each experiment let F_i be the weighted density-value matrix, A_i the weighted transport-numerator derivative matrix with its previously fixed computed normalizers, and d the common scaling-parameter row. The domain matrix is M_i=[F_i;d]. Assume each M_i has full column rank. The protocols defining these rows and their canonical inverse are in ../third-grid-actions/PROOF.md, ../sampled-physical-actions/PROOF.md and ../gauss-sampled-actions/PROOF.md. Normalizers are held fixed; only the transport numerator is differentiated.

For a chosen mixing weight alpha in[0,1], set

    M_alpha = [sqrt(alpha) F_1; sqrt(1-alpha) F_2; d],
    A_alpha = [sqrt(alpha) A_1; sqrt(1-alpha) A_2].

Thus the parameter row retains unit weight. The physical field weights still sum to one. If G_i=M_i^T M_i and H_i=A_i^T A_i, direct multiplication gives

    G_alpha=alpha G_1+(1-alpha)G_2,
    H_alpha=alpha H_1+(1-alpha)H_2.                    (1)

The singular minimum in the mixed physical norm is

    sigma_alpha = min_(t != 0) ||A_alpha t||/||M_alpha t||.

For alpha in[0,1],

    sigma_alpha >= min(sigma_1,sigma_2).                (2)

If each A_i also has full column rank and the truncated row d=d[:k] is nonzero, let

    c_i=min_(d t=1)||A_i t||,
    c_alpha=min_(d t=1)||A_alpha t||.

Then

    c_alpha^2 >= alpha c_1^2+(1-alpha)c_2^2.           (3)

For0<alpha<1, ker(A_alpha)=ker(A_1) intersect ker(A_2). The same assertion holds for the domain matrices when written as the equivalent stack[sqrt(alpha)M_1;sqrt(1-alpha)M_2].

## Proof

Identity(1) follows by multiplying the blocks. Since the two coefficients of d^T d add to one, the single parameter row agrees with the duplicated, weighted parameter rows. Positive definiteness of each G_i implies that of G_alpha, including the endpoint weights. For every t, ||A_i t||^2 >= sigma_i^2 ||M_i t||^2 by the definition of sigma_i. Multiplying these two inequalities by their nonnegative weights and adding proves(2) after division by ||M_alpha t||^2 and minimization. Every t satisfying d t=1 obeys ||A_i t||^2>=c_i^2; the same weighted addition and minimization prove(3). Finally, a sum of two nonnegative squared norms with strictly positive coefficients is zero exactly when both terms are zero. This proves the kernel statement.

There is no corresponding universal upper bound by max(sigma_1,sigma_2). For M_1=M_2=I_2, A_1=diag(epsilon,1), A_2=diag(1,epsilon), and0<epsilon<1, both individual minima are epsilon. At alpha=1/2 the mixed minimum is sqrt((1+epsilon^2)/2)>epsilon. Thus a larger mixed minimum can occur merely because the two finite tests see complementary directions. It proves no continuum coercivity.

For computation, write M_alpha=QT with T invertible and Q^T Q=I. The change of variable z=Tt gives the physical matrix B=A_alpha T^(-1). Stable triangular solves and the SVD of B give the finite singular values. Independently using M_alpha=U S V^T gives coordinates V S^(-1), with the same singular values. For the unit-parameter cost, an SVD A_alpha=U_A S_A V_A^T gives

    c_alpha=1/||S_A^(-1) V_A^T d^T||.

Indeed put y=S_A V_A^T t. Then ||A_alpha t||=||y|| and the constraint is the scalar product of y with S_A^(-1)V_A^T d^T equal to one. Cauchy-Schwarz proves the formula, with equality in the dual-vector direction. The minimizing coefficient vector is reconstructed and checked.

## Prespecified experiment and scope

Use alpha=0,1/4,1/2,3/4,1 and k=4,10,14 for the frozen72x30,96x40 and120x48 states. For this mixed experiment, A_i use the independently implemented eighth-order centered Cartesian gradients with h=max(1,|x|,|y|)/32000 on both coordinate axes. This selects the Gauss source experiment's stencil diagnostic, whereas that source designates analytic gradients as primary; the source designation is unchanged. The mixed experiment makes no analytic-gradient primary claim. At each sample the density row is sqrt(weight)*delta_rho/(1+|rho|). In both samples N_f=|rho|+|W_1 rho_x|+|W_2 rho_y|, with the finer inverse for W. The64point action uses the finer-rule analytic gradients in this fixed normalizer; the58point action uses the stencil gradients just specified in its fixed normalizer. The field weights are1/58 and the recorded positive Gauss weights, respectively. The denominators are therefore specified computed quantities, not exact canonical normalizers. The first inverse rule is4096 angular nodes, radial order32, maximum log-panel width0.075; the second is4096 angular nodes, radial order24, maximum width0.1. Both have exterior cutoff radius10^30. Their earlier sensitivity and exterior estimates remain separate and do not become a global error bound upon mixing. No new inverse evaluation is performed by this topic.

The code verifies matching frozen-state and ordered-direction hashes across the two source experiments, checks both source completions, reconstructs every source matrix entry from the raw scalar rows, reconstructs the mixed Gram identities, and compares two distinct matrix factorizations. A pre-results manifest authenticates all existing source files and the inspected implementation files that establish the stencil convention. Gauss action files, which are not yet complete at registration, must match the already pinned run/proof/data/dependency hashes, source rule metadata, and summary action hash; every stored Gauss matrix is independently reconstructed before use. The current proof, run and contract hashes are checked against the revised plan. Optimized Python execution is rejected explicitly, so assertion removal cannot yield PASS. The common parameter row is checked entry by entry. The arrays and all input hashes are retained. Domain condition numbers and finite numerical ranks are floating-point diagnostics. Cross-resolution comparisons change the density, direction space and computed normalizers. No kernel dimension, isolation, family, smooth-limit assertion or endpoint follows from this calculation.

## Protocol revision record

The first actual Claude Opus5.5 review ended at22:20:50Z with max_tokens, after confirming the mathematics and identifying provenance/convention gaps. This revision records and repairs those gaps before any mixed arrays or results exist. The original proof, code and plan are retained under verification/v1_*. The sampling weights, states, spaces, gradient choices and matrix definitions have not changed. The review's optional interpolation observations are not needed here.
