# Reduced parameter sensitivity from a saved QR factor

Status: proved finite-dimensional identities. They describe a linearized least-squares problem, not the Hessian of the nonlinear Euler objective and not statistical uncertainty.

## Statement and notation

Let m >= n = a + 2, let J be a real m by n matrix, and let r be a real m-vector. Let D be a positive diagonal n by n matrix. Suppose

J D^(-1) = Q R, Q^T Q = I_n,

with Q real m by n and R real n by n. No full-rank hypothesis is imposed on J. Write q = Q^T r, d = ||r||^2, and split R = [R_a C] into a coefficient block and two parameter columns. A displacement x_s = D x is in scaled coordinates. Let B be any real a by b matrix with orthonormal columns specifying the allowed coefficient subspace. For example, B may span the orthogonal complement of a nonzero scaled phase generator. Set A = R_a B and P = A A^dagger, where the dagger is the Moore-Penrose inverse. Then the coefficient-minimized linear model at a scaled parameter displacement h in R^2 is exactly

phi(h) = min_z (1/2)||r + J D^(-1)(B z,h)||^2
       = (1/2)|| (I_n-P)(q+C h)||^2 + (1/2)(d-||q||^2).

Its parameter gradient at h=0 and its Hessian are

g = C^T(I_n-P)q, S = C^T(I_n-P)C.

The matrix S is positive semidefinite. Its kernel consists exactly of the parameter directions h for which C h lies in range(A). The minimum-norm minimizing parameter step is h_* = -S^dagger g. Its predicted decrease from phi(0) is (1/2)g^T S^dagger g. Its relative decrease from the original objective d/2, when d>0, is g^T S^dagger g / d.

For a parameter direction e with C e nonzero, the unabsorbed fraction is ||(I-P)C e||/||C e||. This lies in [0,1]. It is undefined when C e=0. A value of zero means complete absorption by an allowed coefficient change in this linear model.

## Proof

Decompose r = Qq + r_perp with Q^T r_perp=0. Orthogonality gives

||r+Q(Az+Ch)||^2 = ||q+Az+Ch||^2 + ||r_perp||^2.

The second term is d-||q||^2. The least-squares residual of minimizing the first term over z is the orthogonal projection of q+Ch onto range(A)^perp. This proves the formula for phi. Since P is symmetric and idempotent, differentiating that quadratic gives g and S. Moreover, h^T S h = ||(I-P)Ch||^2, proving positive semidefiniteness and the kernel characterization.

If h is in ker(S), then (I-P)Ch=0 and h^T g=0. Thus g is orthogonal to ker(S), equivalently g lies in range(S). Solving S h=-g by the Moore-Penrose inverse gives the minimum-norm solution h_*. Substitution in phi(h)-phi(0)=g^T h+(1/2)h^T S h gives the stated decrease. Orthogonal projection cannot increase a Euclidean norm, which proves the bound on the unabsorbed fraction.

## When the bottom two QR rows suffice

Suppose B=I_a and R is upper triangular with its leading a by a block R_aa invertible. Then

R_a = [R_aa; 0], C=[R_ap;R_pp], P=diag(I_a,0_2).

Consequently S=R_pp^T R_pp and g=R_pp^T q_p. If R_aa is rank deficient, or a coefficient direction has been excluded by B, this simplification is not generally valid. One must form the projector for the allowed coefficient block, preferably by an SVD without normal equations. A QR factor alone does not certify the rank assumption.

## Singular-value truncation and gauge directions

For a declared nonnegative threshold tau, let U_tau contain the left singular vectors of A whose singular values exceed tau times its largest singular value. Define P_tau=U_tau U_tau^T. The preceding projection calculations remain true with this projector for the retained coefficient image. They concern a restricted linear model. Discarded directions must not silently be interpreted as exact null directions.

For a nonzero unscaled coefficient phase generator v, the corresponding scaled direction is D_a v. Taking the columns of B to be an orthonormal basis of (D_a v)^perp removes that coordinate direction. Whether it should be removed depends on the gauge convention. With gauge penalty rows included in J, J(v,0) need not vanish. The chosen restriction must be stated; otherwise the reduced sensitivity is ambiguous.

## Physical coordinates and curvature widths

Let D_p be the last two diagonal entries of D. Physical parameter displacements k satisfy h=D_p k, so S_phys=D_p S D_p and g_phys=D_p g. Eigenvectors of S converted by D_p^(-1) are physical displacements, but are not generally eigenvectors of S_phys.

At a minimizing h_*, along a unit eigenvector e of S with eigenvalue lambda>0, the model rise at h_*+t e is exactly lambda t^2/2. Thus a model rise epsilon times a stated positive reference objective L_ref has curvature width |t|=sqrt(2 epsilon L_ref/lambda). A zero eigenvalue gives an unbounded width in this model. It does not justify an enormous finite number produced by replacing lambda with a tiny positive constant.

At the current point h=0, rather than the minimizing point, the rise is t e^T g + lambda t^2/2. Unless e^T g=0, symmetric widths omit a linear term and do not describe a rise from the current objective. The two roots for a prescribed positive rise epsilon L_ref are

t = ( -e^T g +/- sqrt((e^T g)^2 + 2 lambda epsilon L_ref) )/lambda.

## Dependencies and scope

The proof uses orthogonal projection, the singular-value decomposition, and elementary differentiation of a quadratic. It assumes exact arithmetic; saved factors require numerical rank and orthogonality checks. No Euler existence, optimizer convergence, or parameter identification conclusion follows from these identities alone. Testing this linear model against the nonlinear objective is a separate experiment.

## Explicit phase complement and singular bands

For a unit vector v in R^a, set s=1 if v_1 >= 0 and s=-1 otherwise, and set u=(v+s e_1)/||v+s e_1||. This denominator is nonzero because ||v+s e_1||^2=2(1+|v_1|). Let H=I-2uu^T. Then H is symmetric, H^2=I, and Hv=-s e_1. The last a-1 columns B of H therefore satisfy B^T B=I and range(B)=v^perp. Moreover BB^T=I-vv^T. Thus R_a B and R_a(I-vv^T) have the same image and the same nonzero singular values, because their products with their transposes are equal. The first can form the coefficient projector without inserting an artificial zero column. This identity holds even when R_a is rank deficient. A zero generator is treated separately by B=I.

Let R=U diag(s_i) V^T be an SVD with all n left singular vectors retained, and q=Q^T r as above. For any chosen set I of positive singular values, orthogonality gives the least-squares step x_I=-sum_{i in I} (u_i^T q)/s_i v_i. Substitution shows that its decrease in one half of the squared linear residual is one half of sum_{i in I}(u_i^T q)^2. For d>0 its relative decrease is that sum divided by d. Disjoint singular bands have additive shares. Their steps are orthogonal in scaled coordinates, so ||x_I||^2=sum_{i in I}(u_i^T q)^2/s_i^2.

The residual component outside the stored Q space has squared norm d-||q||^2. This is a component outside range(J), but it equals the full component outside range(J) only if every component of q along a zero singular value vanishes. Otherwise the latter also includes sum_{s_i=0}(u_i^T q)^2. A floating SVD of a rank-deficient matrix often returns tiny positive singular values. Counting those at threshold zero is a numerical convention and does not prove rank or identify the exact range. Band steps divided by such tiny values have no established accuracy. A finite threshold and its sensitivity must be reported.

## Equality of residual components versus equality of subspaces

Under the hypotheses above let U_0 contain the left singular vectors of R with zero singular value. Then

range(J)^perp = range(Q)^perp direct-sum range(Q U_0).

Indeed range(J)=Q range(R). Inside range(Q), the vectors orthogonal to this image are exactly Q ker(R^T)=range(Q U_0), and every vector outside range(Q) is already orthogonal to range(J). The sum is orthogonal since Q is an isometry. It follows that the two complementary subspaces are equal if and only if R has full rank. Their orthogonal projections of a particular residual r agree if and only if U_0^T Q^T r=0. These are different conditions.

For example, in R^2 take Q=I, R=diag(1,0), J=R and r=(1,0). The complementary subspaces are {0} and span((0,1)), so they differ. Both projections of r are zero. Thus equality for one residual cannot establish equality of subspaces. This is an exact finite-dimensional statement, independent of a numerical rank decision.

## Logarithmic widths must use their stated center

Assume the reduced quadratic is q(h)=q(0)+g^T h+(1/2)h^T S h on R^2, with S symmetric positive definite, physical scaling D_p diagonal and positive, current omega w_0>0, and h_*=-S^(-1)g. Its physical minimizing omega is w_*=w_0+(D_p^(-1)h_*)_2. Assume w_*>0. For a unit eigenvector e of S with positive eigenvalue lambda, a positive reference objective L_ref and f>0, set t=sqrt(2 f L_ref/lambda) and delta=(D_p^(-1)t e)_2.

At either endpoint h_* +/- t e the model rise from its minimum is f L_ref: the linear term in the displacement vanishes because g+S h_*=0, leaving lambda t^2/2. If w_*+delta>0 and w_*-delta>0, the corresponding log-omega displacements from the minimizing point are exactly

log(w_*+delta)-log(w_*) = log(1+delta/w_*),
log(w_*-delta)-log(w_*) = log(1-delta/w_*).

These signed displacements generally differ in absolute magnitude. If an endpoint has nonpositive omega, its real log displacement is undefined. Reversing e only exchanges the two endpoints. Substituting w_0 for w_* computes displacements about the current physical omega, not about the minimizer; it is correct at a nonzero delta only when w_*=w_0. The linear approximation delta/w_* is also distinct from the exact logarithmic displacement.

For an exact counterexample take S=diag(1/50,1/50), g=(0,-1/50), D_p=I, q(0)=L_ref=1, w_0=1, e=(0,1), and f=1/100. Then h_*=(0,1), w_*=2, t=delta=1, and the two log displacements are log(3/2) and -log(2). Substitution of w_0 gives log(2) for the positive endpoint and an undefined negative endpoint. Both physical endpoints about the actual minimum have positive omega. This counterexample involves a positive quadratic minimum 99/100 and does not rely on a singular model.

The same conversion at a displacement from the current point correctly uses w_0. In that case the two roots derived above include the linear term g^T e. These statements concern an unconstrained local quadratic; they do not assert feasibility in the original parameter interval or agreement with a nonlinear objective.
