# Augmented finite matrices and conditional continuation

## Statement, notation, and scope

Let T(x,lambda,beta) be a C1 map into R^n, defined on an open set, and let
h(x,lambda,beta)=q(beta)^T x+lambda c_f-1-beta/2.
The source number c_f is fixed. At a specified evaluation point write J=D_x T, A=I-J, t_p=partial_p T, d_lambda=c_f, and d_beta=q_beta^T x-1/2. These are partial derivatives at fixed coefficient coordinates. Assume A is invertible. Put v_p=A^{-1}t_p and m_p=q^T v_p+d_p. Define

B_p = [[A,-t_p],[q^T,d_p]],
C = [[A,-t_lambda,-t_beta],[q^T,d_lambda,d_beta]].

All linear algebra below is exact for any finite arrays bearing these names, whether or not they approximate the claimed derivative. Derivative identities for the nonlinear map require that the arrays actually be those derivatives. Nonlinear implicit-function conclusions additionally require the evaluation point to solve the corresponding nonlinear equations. A finite difference array at an approximate state is not automatically covered by those conclusions.

The conclusions are:

1. det B_p=det A times m_p. Moreover B_p(v_p,1)=(0,m_p), hence its smallest Euclidean singular value is at most |m_p|/sqrt(1+|v_p|^2).
2. C has full row rank if and only if (m_lambda,m_beta) is nonzero. In that case its nullspace has dimension one. When m_lambda is nonzero, a spanning vector is (v_beta-v_lambda m_beta/m_lambda,-m_beta/m_lambda,1).
3. Under the exact-root and smoothness assumptions, m_lambda nonzero makes beta a valid local parameter for the augmented solution set, with lambda'(beta)=-m_beta/m_lambda. At a point where m_beta=0, the graph lambda(beta) is stationary. If the map is C2 and the reduced second derivative m_beta_beta is nonzero, lambda''=-m_beta_beta/m_lambda at that point. This is the nondegenerate fold criterion for projection to lambda. Merely small sampled m_beta establishes none of these exact-root properties.
4. Singular values depend on chosen norms and parameter units. Nonzero singular values of the rectangular C describe its restriction perpendicular to its kernel in the chosen input norm. They do not remove its exact null direction and do not measure the conditioning of a nonlinear profile problem without further hypotheses.

## Proof of the finite identities

Multiply B_p on the left by the invertible block matrix
L=[[I,0],[-q^T A^{-1},1]]. This gives [[A,-t_p],[0,m_p]]. The determinant formula follows since det L=1. Direct substitution gives the displayed action on (v_p,1); divide the input by its norm and use the minimum characterization of the smallest singular value.

The same row operation transforms C into [[A,-t_lambda,-t_beta],[0,m_lambda,m_beta]]. Its first n rows are independent. Its last row supplies an additional independent row exactly when the final two entries are not both zero. If the row is nonzero, rank-nullity gives a one-dimensional kernel. The first n equations impose z=v_lambda ell+v_beta b. The final equation is m_lambda ell+m_beta b=0. For m_lambda nonzero set b=1 and solve for ell. The row operation is not orthogonal; it proves rank and determinants, not equality of singular values with those of the triangular array.

This also shows why a small m_beta can coexist with a much larger smallest positive singular value of C: the parameter direction that nearly nulls B_beta may lie near the exact nullspace of C. The assertion does not require A to be normal or contractive.

## Exact nonlinear interpretation

Set F=x-T. At an actual solution F=0 where D_x F=A is invertible, the implicit-function theorem supplies a unique C1 local function x=x(lambda,beta). Differentiating F=0 gives x_p=A^{-1}t_p. The reduced function M(lambda,beta)=h(x(lambda,beta),lambda,beta) therefore has derivatives M_p=m_p at that solution.

At an actual zero M=0 with M_lambda nonzero, apply the scalar implicit-function theorem to obtain lambda=g(beta). Differentiation of M(g(beta),beta)=0 gives g'=-M_beta/M_lambda. With C2 regularity, differentiation again gives
M_lambda g''+M_lambda_lambda(g')^2+2M_lambda_beta g'+M_beta_beta=0.
At a stationary point g'=0 this reduces to the asserted second derivative. Nonzero g'' gives a strict local extremum of lambda as a function of beta. Taylor expansion and the nonzero derivative of g' imply strict monotonicity on each sufficiently small side, so lambda values on the allowed side sufficiently close to the extremum have exactly two nearby beta values. The other side has none. These statements need an exact stationary point and the nonzero second derivative. At a sampled point with m_beta nonzero, the corresponding exact derivative, if known, would instead give a nonzero slope; one cannot call that point a fold.

## A counterexample preserving the scalar strain-equation form

Fix epsilon>0 and beta_0>0, let b=beta-beta_0, choose n=1, q=1 and c_f=1, and define
T(x,lambda,beta)=1+beta/2-lambda+epsilon exp(lambda/epsilon)+b^2.
Then F=0 has the exact solution x=T for every pair of parameters and A=1. Along it,
M=lambda+x-1-beta/2=epsilon exp(lambda/epsilon)+b^2>0.
There is no augmented solution anywhere. At lambda=0,b=0 take x=1+beta_0/2+epsilon. The inner residual vanishes and h=epsilon, as small as desired. The exact derivatives give t_lambda=0, t_beta=1/2, m_lambda=1, m_beta=0. Thus C has full row rank, a one-dimensional kernel, and the formal fold derivative M_beta_beta=2, but there is no augmented root or solution curve. This counterexample refutes any unconditional passage from those local arrays and a small residual to an exact branch, even with the specified affine scalar h. The exponential derivative varies on the epsilon scale, which is precisely why a quantitative neighborhood estimate would matter.

## Norms, changes of units, and derivative error

For positive definite input/output matrices H_in,H_out choose invertible factors R_in,R_out with H=R^T R. The singular values representing the operator between these metrics are those of R_out B R_in^{-1}. This follows by substituting y=R_in x in the Rayleigh quotient |Bx|_out/|x|_in. For a parameter measured in units kappa, the input metric must include that unit consistently. Multiplying only a parameter column rescales its coordinate and generally changes singular values and condition numbers. With no declared natural parameter metric, both raw and chosen rescaled results are descriptions of those particular finite arrays.

For C of full row rank, its n+1 positive singular values are the extrema for inputs in the orthogonal complement of its one-dimensional kernel. The full map still has minimum ratio zero over all inputs. To say there is no additional nearly null transverse direction means a comparison with the displayed finite singular values in the specified metric; it is not a coordinate-invariant absolute notion of nearness.

If a computed square array B_hat and the true B satisfy the induced Euclidean operator estimate ||B-B_hat||<=delta, then for every unit vector v, ||Bv||>=||B_hat v||-delta>=sigma_min(B_hat)-delta. Thus delta<sigma_min(B_hat) proves invertibility. For a rectangular full-row-rank array apply this argument to its transpose to preserve full row rank. In floating computations even sigma_min(B_hat) has an error; include that additional error in delta. No such operator enclosure is supplied by one finite difference step, selected directional checks of a different map, or agreement of decimal printouts. A rank verdict for the stored array does not transfer to the exact map in their absence.

## Dependencies and verification plan

Only finite-dimensional linear algebra, the usual C1/C2 implicit-function theorem, and the displayed complete counterexample are needed. P208 supplies independently frozen arrays, q, and prior inner-matrix checks. P205 supplies an optional physical Gram norm for G=Omega/x. The present computation must be implemented independently and must not import or run the numerics lane's code. It will form A,B_lambda,B_beta,C from the raw archive, recompute singular values and Schur residuals, and compare the freshly read report and JSON. Those computations verify sampled arrays only. B2 existence and nonexistence remain open.

## Refinements after the adversarial review

The upper bound for sigma_min(B_p) has no converse without additional estimates. For example take A=[epsilon], t_p=[0], q=[1], d_p=1. Then m_p=1 whereas B_p=[[epsilon,0],[1,1]] has sigma_min at most epsilon/sqrt(2), by testing (1,-1)/sqrt(2). Thus a small singular value alone does not identify a weak reduced parameter derivative.

The positive singular values of C have the complementary lower bound sigma_min_positive(C)>=sigma_min(B_p), for either p and the same raw Euclidean coordinate units. Indeed C C^T=B_p B_p^T+c c^T after reordering columns, where c is the added column. For every unit y, y^T C C^T y >= y^T B_p B_p^T y. Taking the minima proves the claim. The comparison need not apply when the two matrices use different ad hoc column scales.

At a nondegenerate stationary point lambda*, if M_beta_beta/M_lambda>0, g''<0, lambda* is a strict local maximum, and the two nearby beta values lie at lambda<lambda*. If the ratio is negative, the extremum is a minimum and the two values lie at lambda>lambda*. The counts are restricted to a sufficiently small implicit-function neighborhood; no remote branches are excluded.

Here is an elementary conditional bound on the kernel direction. Suppose C_hat and C are matrices of size (n+1) by (n+2), C_hat has full row rank with smallest positive singular value sigma, and ||C-C_hat||<=delta<sigma. The transpose argument above gives full row rank of C. For any unit t in ker C, ||C_hat t||<=delta. Write t=t_0+t_perp using Euclidean orthogonal projection onto ker C_hat. Then C_hat t=C_hat t_perp and ||C_hat t_perp||>=sigma ||t_perp||. Consequently the sine of the angle between the two null lines is at most delta/sigma. In weighted coordinates apply the same proof to R_out C R_in^{-1}. This estimates a tangent to an exact solution curve only when C is the derivative at an actual root with the smoothness and rank hypotheses above. No such delta is available in this numerical audit.

Convergence to a stationary optimization point does not establish the globally minimum attainable residual. It is insufficient by itself to prove a representation-imposed floor. A shared seed and equal iteration counts do provide a controlled comparison of the stated runs; they do not make the iterates, costs, or nonlinear basins identical. The comparison may support sensitivity to the combined discretization change without isolating the basis error or proving the optimum. These distinctions reject overly strong auxiliary language in review423 while retaining its valid cautions.
