# Exact residual sectors and exclusion from the unweighted forcing space

## Statement and hypotheses

Use the potential and exact rational checkpoint interpretation in ../baseline/PROOF.md. Put gamma=1/c, delta=1-gamma, and alpha[j,q]=gamma-j delta-2q. For r>1 its convergent binomial expansion has potential sector

r^(alpha[j,q]+3) sum_m C[j,q,m] cos(2m theta),

C[j,q,m]=sum_k a[j,m,k] binom(p[j]-k,q).

Termwise differentiation is valid on every r>=1+epsilon because the binomial series and its finitely many differentiated series converge locally uniformly. Form rho and U by the Cartesian derivatives in the baseline proof. Their sector exponents are alpha[j,q]. A product U[i,u].grad rho[j,v] has exponent alpha[i,u]+alpha[j,v]-1=alpha[i+j+1,u+v]. Thus each residual sector is the sum of the linear contribution (c alpha[h,q]-1)rho[h,q] and all such nonlinear pairs with i+j+1=h and u+v=q. Exact rational arithmetic decides whether its angular trigonometric polynomial is zero.

For a finite cosine polynomial C(theta), the formulas in the baseline proof with A=r^s give exact Cartesian derivatives by finite shifts of Fourier indices. Products use the exact product-to-sum identities. This independent computation need not use a specialized stream-density recursion.

## Norm convention

If E(theta)=sum_{k positive, odd} e[k] sin(k theta), then integral_0^(2 pi) E^2=pi sum e[k]^2, whereas integral_0^(pi/2) E^2=(pi/4)sum e[k]^2. Therefore the full-circle norm is twice the quadrant norm, not four times. Norm certificates must identify which convention they use.

## Tail obstruction

Suppose F(r,theta)=r^a E(theta)+O(r^(a-epsilon)) uniformly in theta, with epsilon>0 and nonzero smooth E. If a>=-1, F is not L2(R2). Indeed, the angular squared integral is asymptotic to r^(2a)||E||_L2(S1)^2 and its radial integral includes r dr.

If a>=-2, F is not homogeneous H^-1(R2), interpreted as the continuous dual of homogeneous H^1 with norm ||grad phi||_2. Choose a smooth function phi supported in 1<r<2 whose angular component has nonzero pairing with E, and with sign chosen to make its radial-angular pairing positive. The rescaling phi_R(x)=phi(x/R) has the same gradient norm in two dimensions, while pairing F with phi_R equals A R^(a+2)+O(R^(a+2-epsilon)), A>0. For a>-2 these pairings are unbounded. For a=-2, take disjoint dyadic annuli with radii growing by a factor at least four. The test sum of K such rescalings divided by sqrt(K) has bounded gradient norm, while its pairing grows like A sqrt(K); finitely many initial annuli and the summable error do not change this divergence. Thus F is not in the dual space.

This proves failure of any forcing norm containing the homogeneous H^-1 component. It alone makes no assertion about a solution in some different weighted correction class. A formal asymptotic series alone is not an exact solution, and floating cancellation is not sector vanishing.

## Dependencies and scope

The argument uses the explicit binomial series, elementary differentiation, Fourier orthogonality, and the dual characterization of the homogeneous negative Sobolev norm. Numerical evidence belongs in verification/, and exact source coefficients in ../baseline/data/. No Lean build is used.

## Unique principal stationary recursion

For a leading density sector G_0 at exponent alpha_0=gamma, let alpha_j=gamma-j delta for j>=1. The jth stationary residual equation is

-j(c-1) G_j + sum_{i+k+1=j} U_i.grad G_k = 0,

where the displayed product means its angular coefficient after homogeneous Cartesian differentiation. Every summand only uses indices below j. Therefore G_j is uniquely determined from the previous sectors by division by j(c-1).

A homogeneous potential r^s sum_{m=0}^M C_m cos(2m theta), with s=alpha_j+3, maps under -partial_y Delta to a density sine polynomial with largest possible harmonic 2M+1. For m>0 the coefficient of sin((2m+1)theta) from C_m is -(s^2-4m^2)(s-2-2m)C_m/2; for m=0 it is -s^2(s-2)C_0. If these factors are nonzero, descending elimination recovers the potential uniquely. In the finite set computed here, nonvanishing is checked exactly. This proves existence and uniqueness of each finite stationary truncation. It does not prove convergence of the infinite series.

After retaining branches 0 through B-1, the first omitted principal residual sector has index B and exponent gamma-B delta. Its angular coefficient is the nonlinear forcing that would determine G_B. This fixed coefficient is independent of all faster radial descendants. It may be removed by adding the Bth stationary branch, but that operation does not ensure smallness of the near-field residual or preservation of background coercivity.

## Extension and comparison through order twelve

The same finite recurrence applies at every additional order for which the displayed potential inversion factors are nonzero. For each j=9,...,12, the independent extension computes the forcing from all ordered pairs i+k=j-1, divides by j(c-1), and reconstructs the unique homogeneous potential by descending angular elimination. Exact recomputation of its density checks the inversion. The first eight independently generated orders may be used as a checkpoint because their exact coefficients, not decimal norms, are preserved.

Comparison with another lane requires equality of every rational density and potential coefficient and the exponent at each order. Multiplication of the density by j(c-1) then determines the omitted residual sector exactly. Its full-circle norm is sqrt(pi sum_n e_n^2), enclosed with Arb. All comparisons concern finite stationary coefficients in the fixed primary chart. They neither establish an infinite convergence radius nor bound the actual full-plane residual of an inner continuation.

The independent extension through order sixteen is stated and proved in [PROOF_EXTENSION_16.md](PROOF_EXTENSION_16.md). All finite coefficient and forcing-energy comparisons passed in verification/stationary_extension_16_summary.json. No convergence assertion is added.
