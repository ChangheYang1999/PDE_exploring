# Physical actions on a second prescribed sample

Date: 2026-10-20. This is a finite-dimensional protocol and proof of its matrix formulas. It is written before evaluating the new points. The experiment tests sensitivity to the physical sampling used to measure candidate directions. It gives no continuum spectrum or PDE endpoint.

## Fields, directions and points

For each frozen L=8 state at resolutions (72,30), (96,40) and (120,48), retain the fourteen directions already constructed in third-grid-actions and sampled-physical-actions. The first ten are the numerics lane's supplied nodal Ritz directions; four independent calibration directions were appended by this verifier. The saved last scalar C is auxiliary data for the orbit solver. It is not an argument of this density reconstruction: only its nodal values b and scaling parameter c determine rho. Hence variation of C gives no extra density or physical transport term. The physical domain matrix must still have full column rank on every span used. The values of the directions are data. All evaluation, differentiation and full-plane inverse code is the verifier's own.

Let rho denote one fixed density, c its scaling parameter, U its canonical velocity and W(X)=cX+U(X). For a direction h with parameter derivative d, let V be the canonical velocity of h. On the positive quadrant the frozen fields are smooth away from zero. The differentiated transport numerator R=W.grad rho-rho is

    L(h,d)=(cX+U).grad h+(dX+V).grad rho-h.                 (1)

Indeed differentiation of the product W.grad rho contributes the derivative of each factor, and the last term contributes -h. Linearity of the fixed canonical inverse gives delta U=V. Only the numerator is differentiated.

Let a=log(0.05), b=log(100). Let (z_i,w_i), i=1,...,8, be the degree-eight Gauss-Legendre nodes and positive weights on [-1,1]. Prescribe, before evaluation,

    r_i=exp((a+b)/2+(b-a)z_i/2),
    theta_j=pi(1+z_j)/4,
    X_ij=r_i(cos theta_j,sin theta_j), lambda_ij=w_i w_j/4. (2)

The 64 weights are positive and sum to one, because sum_i w_i=2. They are the tensor quadrature weights for the probability measure d(log r) dtheta / ((b-a)pi/2) on this rectangle. We use them only to define a finite norm, and do not assume a quadrature error bound for a continuous norm. The represented binary points and weights, including their sum error, are saved before any velocity is evaluated. All comparisons use these same saved binary values.

At every point set N_i=|rho(X_i)|+|W_1 partial_1 rho|+|W_2 partial_2 rho|, using the finer inverse rule described below, and require N_i>0. For coefficients t in a selected k-dimensional prefix of the direction matrix, define

    ||t||_D^2=sum_i lambda_i |h_t(X_i)/(1+|rho(X_i)|)|^2
                  +|d_t|^2,
    ||L t||_R^2=sum_i lambda_i |L(h_t,d_t)(X_i)/N_i|^2.     (3)

The last row of the domain matrix is the derivative of c, with unit weight. These are norms on the chosen span only when the domain matrix has full column rank; this is checked numerically. They can have a nullspace on a larger function class.

## Matrix formulas

Let M_ij=sqrt(lambda_i) h_j(X_i)/(1+|rho(X_i)|), with the row d appended. Let A_ij=sqrt(lambda_i)L(h_j,d_j)(X_i)/N_i. If M=QT is a thin QR factorization with invertible T and Q^TQ=I, then ||Mt||=||Tt||. The change of variable s=Tt identifies the physical input norm with the Euclidean norm. Thus the matrix of the sampled operator in a physical orthonormal coordinate is

    B=A T^(-1).                                            (4)

Its least singular value is min_(||Mt||=1)||At||, by the definition of singular value. This concerns only the selected finite matrices.

For the cost of one unit of c, assume A has full column rank and d is nonzero. Write A=Q_A R_A. With y=R_A t and z=R_A^(-T)d, the constraint d^Tt=1 is z^Ty=1. Cauchy-Schwarz gives ||y||>=1/||z||, with equality at y=z/||z||^2. Consequently

    min_(d^Tt=1)||At||=1/||R_A^(-T)d||.                    (5)

The code also constructs this minimizing coefficient vector and verifies its constraint and attained cost. No generalized eigenproblem obtained by squaring a poorly conditioned matrix is needed.

## Separate error comparisons

Evaluate the base and all direction velocities with the independently implemented full-plane split kernel at two rules: (angular nodes, radial Gauss order, maximum log-panel width) equal to (2048,24,0.1) and (4096,24,0.1). Both truncate only the exterior beyond radius 10^30, whose separately proved tail bound is recorded. No periodic or finite-box inverse is used. Direct analytic coefficient chain rules supply grad rho and grad h; independent Cartesian stencils at two step sizes provide a differentiation diagnostic.

Fix the normalizers from the finer rule for both matrices. For their velocity differences delta U and delta V, exact subtraction of (1) yields

    delta A_ij=sqrt(lambda_i)[delta U_i.grad h_j
                                  +delta V_ij.grad rho]/N_i. (6)

Compute delta B with (4). Its Frobenius and spectral norms are differences between finite rules, not bounds on either rule's canonical quadrature error. Replacing both the base and direction analytic gradients by their stencil gradients, including the d X.grad rho term, with all velocities and normalizers fixed, gives a separate finite-matrix differentiation comparison. The exterior-tail proof bounds the Euclidean velocity norm. Thus each scalar product is bounded by that velocity bound times the computed gradient one-norm, and entrywise propagation through |T^(-1)| bounds the resulting Frobenius norm. These estimates use the computed gradients and the fixed finer-rule normalizers; they do not bound a change to exact-velocity normalizers.

The earlier 58-point protocol uses weights 1/58 for both residual and density rows and appends the same unit-weight d row. Thus both samples have total field weight one and the same parameter weight. The prescribed sample differs from the earlier 58 points in both support and weights. Comparing the least singular values and unit-c costs measures this change jointly. Comparing different resolutions also changes the base state, its normalizers and its finite direction space. No monotonicity, continuum limit, kernel dimension, global coercivity or family follows from agreement or disagreement of these numbers. The earlier near-axis, near-stagnation and far-field checks remain separate; the Gauss sample is not a replacement for them.

## Dependencies and verification scope

The nodal density contract, full-plane kernel, tail estimate and direct coefficient differentiation are specified in inverse/PROOF.md, linearized-check/PROOF.md, exterior-tail/PROOF.md, scale-actions/PROOF.md and sampled-physical-actions/PROOF.md. This argument adds only positive quadrature weights to the previously proved finite-matrix formulas and supplies their proof here. Input hashes and every sampled row are saved. Numerical ranks, singular values and differences are floating-point diagnostics. No theorem about the coupled admissible class is inferred.
