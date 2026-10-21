# Independent physical linearization at the third resolution

Date: 2026-10-20. Status: finite-dimensional identities and numerical protocol, written before the calculation. This is not a proof about the continuum kernel.

Fix the exact binary nodal state N=72,M=30,L=8 audited in ../third-grid/PROOF.md. Put k=1/c_l, q=1-(1+r^2/L^2)^(-(1-k)/2), theta=s+beta sin(2s)/2, and rho=x^2 y (1+r^2/L^2)^((k-3)/2)b(q,s). The first radial row is exactly1. Let T denote the canonical full-plane inverse in ../inverse/PROOF.md, and U=T rho. Its paired integral defines the gauge; no homogeneous strain is added.

For a nodal direction v=(delta b,delta c_l,delta C), define delta k=-delta c_l/c_l^2 and ell=log(1+r^2/L^2). At a fixed physical point the exact density derivative is

    h=x^2 y (1+r^2/L^2)^((k-3)/2)
      [delta b_interp + delta k ell (b-(1-q)b_q)/2].

Indeed delta q=-(1-q)ell delta k/2, and differentiation of the radial prefactor gives ell delta k/2. The auxiliary C does not enter this physical density map. The whole-plane inverse is linear, and the uniform sublinear/logarithmic tails justified in ../scale-actions/PROOF.md permit differentiation under its paired integral. Hence V=T h is the velocity derivative. For W=c_l X+U and R=W.grad rho-rho, direct differentiation gives

    delta R = W.grad h + (V+delta c_l X).grad rho-h.                 (1)

Use exactly the58 points prescribed before the previous96/120 calculations. At the base field set N_i=|rho_i|+sum_j|W_ij partial_j rho_i| and require N_i>0. The finite action matrix is A_ij=delta_j R(X_i)/(N_i sqrt(58)); denominators are held fixed. Define the59-row domain matrix M with first58rows h_j(X_i)/((1+|rho_i|)sqrt(58)) and lastrow delta_j c_l. The physical norm of coefficients c is ||Mc||_2. If the chosen k-column M has full rank and M=QT is thin QR, setting z=Tc shows that the physical matrix is B=A T^(-1). Its singular values are finite sampled quantities in this precise norm. Stable solves are used instead of an explicit inverse.

The least action cost with delta c_l=1 in the chosen finite span is also recorded. Write A=Q_A R_A and d=(delta_j c_l). If A has full column rank and d!=0, then |d.c|<=||R_A^(-T)d|| ||Ac||. Equality occurs for c=R_A^(-1)R_A^(-T)d/||R_A^(-T)d||^2. Thus the minimum is1/||R_A^(-T)d||. Enlarging the span can lower this cost; the number is not a lower bound for the PDE.

Independently recompute the SVD of the saved reduced array D and multiply its right vectors by the saved basis Q. Only these data arrays, not the numerical lane's evaluator, are used. Select the ten soft directions and append four independently chosen nodal calibrations q^a(1-q)^b cos(2m s), with(a,b,m)=(2,1,2),(1,2,1),(3,1,3),(1,1,0), twice orthogonalized in the node metric. Compare dimensions4,10,14. Freeze direction bytes before any physical evaluation.

Compute U and all14 V with this verifier's independent real-space split-kernel inverse:4096 angular nodes, Gauss radial order32, logarithmic panels at most.075, exterior radius1e30. Compute density gradients with eighth-order Cartesian steps1/32000 and1/16000 times max(1,|x|,|y|), and separately by analytic coefficient chain rule. The direction-tail constants and their exact rational exterior bounds are as proved in ../scale-actions/PROOF.md. Propagation through numerically computed gradients is explicitly labelled. Interior principal-value quadrature is not interval certified.

Compare with the completed96/120 matrices at the same points and quadrature. Domain overlap cosines concern the59-dimensional sampled coordinates; their base-density denominators differ across states. They do not give overlap in a prescribed continuum space. Finite matrices, their numerical singular values, inverse sensitivities and discrete center defects establish neither a kernel dimension nor isolation nor a family of profiles. The exact72field already fails the smooth-center test. No result here changes either endpoint without additional independent evidence.

Dependencies: ../inverse/PROOF.md; ../ritz-resolution/PROOF.md; ../sampled-physical-actions/PROOF.md; ../scale-actions/PROOF.md; ../third-grid/PROOF.md. Only this verifier's implementation is reused. No formal sources or builds are used.
