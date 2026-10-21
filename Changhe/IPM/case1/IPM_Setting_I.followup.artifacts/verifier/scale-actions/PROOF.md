# Physical linearized actions at three compactification scales

Date: 2026-10-20. Status: finite-dimensional identities and a numerical protocol, not a continuum spectral theorem.

## Statement and conventions

For each frozen nodal trial rho at radial compactification scale L, let U=T rho be its canonical whole-plane velocity, W=c_l X+U, and R=W.grad rho-rho. The scale L belongs to the coordinates q=1-(1+|X|²/L²)^(-(1-k)/2), k=1/c_l; it is not a finite boundary. The angular coordinate satisfies theta=s+beta sin(2s)/2. The density is x² y (1+|X|²/L²)^((k-3)/2) b(q,s), with b at the first radial row fixed at1.

Let v=(delta b,delta c_l,delta C) denote a finite nodal parameter direction. Differentiation, including k's dependence on c_l, gives a density h and canonical velocity V=T h. At any physical point,

    D R[v] = W.grad h + (V+delta c_l X).grad rho-h.       (1)

Indeed T is linear and its defining convergent canonical integral permits this finite parameter differentiation; the finite trial and derivative densities obey the sublinear/logarithmic tail bounds in ../exterior-tail/PROOF.md and ../ritz-resolution/PROOF.md. Expanding R at parameter t to first order gives (1). The auxiliary C does not enter the reconstructed density or velocity directly.

Fix the same 58 positive physical points as ../sampled-physical-actions/PROOF.md. At each base state set N_i=|rho_i|+sum_j|W_ij partial_j rho_i|>0. Form a matrix A with columns (1)/(N_i sqrt(58)) and a domain matrix M consisting of h_i/((1+|rho_i|)sqrt(58)), followed by the row delta c_l. No auxiliary penalty is inserted. For a chosen column span with full-rank M, its thin QR factor M=QT gives the physical action matrix B=A T^(-1). This follows because z=T c has Euclidean norm ||M c|| and A c=B z. Its singular values therefore refer to exactly this finite physical norm. For full column rank A, QR factor A=Q_A R_A yields the minimum ||A c|| subject to d.c=1 as 1/||R_A^(-T)d||. Cauchy-Schwarz proves the bound, attained by c=R_A^(-1)R_A^(-T)d/||R_A^(-T)d||².

## Prescribed numerical comparison

Independently decompose the saved reduced action array D by SVD and multiply its right vectors by the supplied node basis Q. The saved arrays define directions only. They are not used to evaluate (1). Retain ten soft directions and append the four shape calibrations q^a(1-q)^b cos(2m s) with (a,b,m)=(2,1,2),(1,2,1),(3,1,3),(1,1,0), each orthogonalized twice in the supplied node metric. Compare spans of dimensions4,10,14.

Reconstruct h by this lane's own cosine polynomial transform and differentiated density map. Compute U and V by its independent physical polar principal-value integral, using angular trapezoids and panelwise Gauss-Legendre radial quadrature with separate global and local pieces. This discretization is independent of the numerical researcher's collocation velocity solver. Evaluate physical gradients with the eighth-order Cartesian stencil at relative steps1/16000 and1/32000 and independently by a direct coefficient chain rule. The latter differentiates q, k, the envelope, and the inverse angular map; it is a check of the stencils rather than an imported collocation derivative.

Use 4096 angular nodes, radial order32 and log-panel width.075, with exterior radius1e30. The previously completed L8 calculation supplies its own matching matrices and refinement study. The new L4 and L16 calculations use identical physical points and quadrature. Base and directional exterior-velocity bounds are exact rational bounds from the shared tail proof, with L³ dependence retained; their propagation through numerical gradients is labelled accordingly. All source and direction data are frozen before evaluation. Checks of CPU/GPU density and the node reconstruction are recorded.

## Scope

The whitened singular values and c_l costs are finite sampled measurements. A positive cost in a finite span is an upper bound for the infimum in a larger span. Different L states may represent different solutions or discretization errors, so variation with L is not a convergence test without further controls. Finite-point norms do not control continuum norms. Differentiation and inverse-refinement discrepancies are numerical sensitivity measurements, not rigorous global errors. No kernel dimension, isolation, family, exact profile, or smooth-center endpoint follows from these calculations.

Dependencies: ../inverse/PROOF.md, ../ritz-resolution/PROOF.md, ../sampled-physical-actions/PROOF.md and ../exterior-tail/PROOF.md. This argument and protocol were written before the new computations. No Lean sources or builds are used.

## Tail constants for variable L

Let H be the ceiling of sqrt(2N(2M-1)), B the ceiling of the largest absolute base nodal value, B_d the analogous direction bound, and epsilon=1/5-k>0. Tensor discrete orthogonality gives |b|<=HB and |delta b|<=HB_d. The one-dimensional Markov inequality on q in[0,1] gives |b_q|<=2N²HB. For L>=1 and r>=1, the radial prefactor has modulus at most L³r^k and ell=log(1+r²/L²)<=1+2log r. Differentiating the exponent and compactification with delta k=-delta c_l/c_l² gives

    h=prefactor[delta b + delta k ell (b-(1-q)b_q)/2].

Since r^(-epsilon)<=1 and (log r)r^(-epsilon)<=1/epsilon, a valid growth constant for |h|<=C_d r^(1/5) is

    C_d=L³ H [B_d+|delta c_l| B(1+2N²)(1+2/epsilon)/(2c_l²)].

The base constant is C=L³HB. This derivation justifies replacing the old L8-specific factor512 by exact L³; it introduces no dependence on a numerical asymptotic fit.

## Selected-point inverse refinement

The additional inverse sensitivity test uses the prescribed indices 0,11,16,22,28,34,35,40,46,50,54,57 of the same 58-point list, fixed before this new test runs. It samples small radii, intermediate angles, the region near the source and the far field. For each scale it recomputes the base and all 14 directional velocities at (2048 angles, order24, panel0.1) and (4096 angles, order24, panel0.1). Comparing those two rules isolates angular sensitivity. Comparing the second rule with the main (4096,32,0.075) data isolates radial sensitivity. All action differences use the main run's density gradients and normalizers. Whitened comparisons use its full 58-point domain matrix, but retain only these 12 output rows. They are sensitivities on this subset, not bounds on the omitted rows or a continuum error certificate.
