# Extended localized weak tests and their row scales

Let rho and u be the exact rational candidate C1-N1-007-d2w-j7-e2bal at c=4076476460239181/2251799813685248, and set F=(cX+u).grad rho-rho. Put t=r^2/(1+r^2), v=1-t, and phi_k=y t^k v^2 for a nonnegative integer k. The target is the finite list K={0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096}. Every lower bound is for this fixed exact candidate and fixed exponent; the maximum over K need not optimize all possible probes.

Assume rho and u=U[rho] are smooth, div u=0, u=O(r^gamma), grad rho=O(r^(gamma-1)) for gamma<1, and F is in L2. Let h be a real L2 correction solving, in distributions,

    F + div((cX+u)h) - (2c+1)h + U[h].grad rho + div(U[h]h) = 0,

where U is the S1 Fourier velocity multiplier, div U[h]=0 and ||U[h]||_2<=||h||_2. Then every such fixed-c correction satisfies

    |I_k| <= D_k ||h||_2 + H_k ||h||_2^2,
    I_k = integral F phi_k,
    D_k = A_k+B_k+C_k,
    A_k = ||phi_k(3c+1+2ckv-4ct)||_2,
    B_k = ||t^k v^2(1+2kv+4t)|u|||_2,
    C_k = ||r t^k v^2 |grad rho|||_2.

An admissible upper bound on the probe gradient is H_0=1 and

    H_k = S(k,2)+2k S(k,3)+4 S(k+1,2),
    S(a,b)=a^a b^b/(a+b)^(a+b), k>0.

For completeness, integrate the difference equation against phi_k and use div u=div U[h]=0. Integration by parts moves the linear derivative on h to (2c+1)phi_k+(cX+u).grad phi_k. Its cX part is phi_k(3c+1+2ckv-4ct). The explicit radial and angular derivatives imply |grad phi_k|<=t^k v^2(1+2kv+4t), and |phi_k|<=r t^k v^2. Cauchy-Schwarz and ||U[h]||_2<=||h||_2 yield the displayed inequality; the smooth cutoff justification and precise admissibility hypotheses are those of the cited proof. Maximizing each t^a(1-t)^b by its derivative gives S(a,b), including the endpoint convention at k=0. Solving the quadratic inequality yields

    ||h||_2 >= m_k = 2|I_k|/(D_k+sqrt(D_k^2+4H_k|I_k|)).

The independent first-mode residual cache retains every angular interaction capable of producing sin(theta). Orthogonality eliminates the other residual modes only from I_k. The background integrals B_k and C_k retain all modes and radial cross terms. Exact compactification and beta-power integration, with outward Arb arithmetic, enclose each quantity on the entire plane; see ../projected_residual/PROOF.md and ../localized_weak_probe/BETA_EVALUATION.md for the algebra, endpoint convergence and positive beta recurrences. This code reuses those already peer-checked implementations on the identical canonical source and exact projected residual.

The peer's frozen JSON contains floating values from a finite radial mesh and a finite asymptotic correction. Each printed floating scalar is interpreted as its recorded decimal rational for comparison. The signed relative difference is (peer-exact)/exact, evaluated as an interval. This is a diagnostic error for that particular output, not a uniform error bound for the floating evaluator. The code compares the same k and the same component before comparing maxima. A difference between maxima over k=0,...,8 and k in {0,128,512,1024} cannot by itself diagnose quadrature error.

The nine k=0,...,8 quantities are reused from their immutable exact computation; the remaining18 are computed here with the same complete-plane method. The result records the source hash of every reused row. All new candidate-specific numbers remain OPEN until independent peer reproduction. Matching floating values are diagnostics, not certificates of the floating implementation.

## Necessary row scales for a prescribed radius

For a proposed upper correction radius R>0, inequality (1) requires

    |I_k| <= D_k R+H_k R^2 = J_k(R)

for each k. Since D_k,H_k>0, the normalized quantity |I_k|/J_k(R) exceeding1 excludes that radius under the stated hypotheses. This is only a necessary condition. It does not prove existence if every row passes. The first-order proxy |I_k|/D_k is different from penalizing all raw I_k with one weight; different probes have different D_k. A fixed-background least-squares penalty on the normalized rows has weights proportional to1/J_k(R)^2. Those frozen weights define an optimization objective, not an invariant certificate when the background changes. New candidates must have their actual D_k,H_k and I_k evaluated again.

The checker records J_k at R=3793/10^9=3.793e-6 as a diagnostic illustration of the scalar reference budget. It also compares the linear normalization weights (D_0/D_k)^2. This does not assume the sufficient inverse and nonlinear closure hypotheses for any named theorem.
