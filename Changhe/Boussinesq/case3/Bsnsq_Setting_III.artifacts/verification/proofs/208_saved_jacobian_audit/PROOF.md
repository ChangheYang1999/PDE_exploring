# What a saved discrete Jacobian can and cannot verify

Status: identities were written before their evaluators. The saved Jacobian was checked on 2026-10-21 at 21:23 UTC; see verification/matrix_audit.json. This concerns a forced discrete fixed-point map, not an existence theorem for B2.

## 1. Objects and hypotheses

Let x in R^n be the active coefficients of the divided field G=Omega/x_cartesian, where x_cartesian denotes the horizontal physical coordinate. Let T(x;b,lambda) be a differentiable discrete map with fixed a0, fixed source geometry and a basis retied to b=beta. Its affine input projection is

 P(x)=x-q(q^T x+lambda c_f-1-b/2)/(q^T q), q!=0.           (1)

Assume T depends on x only through P(x). At a putative fixed point x*, set J=D_xT, A=J-I, f=T(x*)-x*. Stored forward differences J_h are arrays approximating J, not J itself. Algebra below applied to J_h is exact algebra for that stored array; its connection to a derivative requires independently bounded discretization, trajectory and finite-difference errors that a small sampled step study does not supply.

The native state has already been frozen and audited in P197, before this matrix audit. Its actual basis has degree5 and simple interior knots, so it is C4 across those knots. The active basis, coefficients and source data will be tied to the forthcoming matrix archive using the independently written R2State evaluator. No numerics-lane implementation is imported or executed. The physical Gram construction and canonical strain functional are proved in research/205_physical_gram_and_strain_norm/PROOF.md.

## 2. Projection and neutral directions

Equation(1) gives P(x+tq)=P(x) for every real t, hence T(x+tq)=T(x). Differentiating at zero gives Jq=0 and Aq=-q. Coordinatewise forward differences need not preserve this identity exactly, since each column uses a different finite displacement. The observed size of J_h q is a consistency diagnostic, not a proven global error bound.

A nonzero vector v is neutral for the iteration exactly when Jv=v, equivalently Av=0. The norm ratio ||Av||/||v||=1 excludes the fixed-point neutrality Av=0. The exact projection direction q has that ratio and Jq=0. This explicitly refutes the numerics source log saying that1 would be neutral for T while printing ||Av||/||v||. If instead ||Jv||/||v||=1 were printed, that too would not imply Jv=v: Jv=-v is a counterexample. Unit-modulus eigenvalues concern marginal iteration stability, a broader notion than the eigenvalue1 corresponding to a fixed-point family. The Rayleigh quotient v^T Jv/(v^T v)=1 alone is also insufficient; even for symmetric J it need not make Jv=v. For J=diag(0,2) and v=(1,1), the quotient is1 and Jv differs from v. A small singular value of A measures a small residual in some direction in the specified norm; it is not a certificate of an eigenvalue or an exact symmetry.

## 3. Coordinate and physical norms

Let H be a symmetric positive-definite Gram matrix for the physical norm ||G_x||_w, so ||x||_H^2=x^T Hx. Let C be its upper Cholesky factor, H=C^T C. Under y=Cx, the induced matrix is B=CAC^-1. Indeed ||Ax||_H/||x||_H=||By||_2/||y||_2. Thus its largest and smallest singular values are the induced expansion bounds. The smallest is positive exactly when that same finite-dimensional A is invertible, in exact arithmetic. For A_h=J_h-I this says nothing about D_xT-I without an operator-error bound.

This is a change of norm and coordinates applied to the existing A. It does not replace the actual projection P by the H-orthogonal projection. Eigenvalues of A and J are unchanged by this similarity, whereas singular values generally change. Compute right multiplication by C^-1 with triangular solves, not by interpreting C^-T as C^-1. A saved weighted-residual-grid metric cannot be reconstructed from a few reported singular values; without its factor or full quadrature data the corresponding reported norm is not independently verified.

For physical vector comparisons, inner products are v^T Hw. A coefficient-space angle can differ substantially. All norms, angles and weak directions must state their metric. A finite physical Gram matrix describes only its finite basis; its condition number is not an infinite-dimensional conditioning theorem.

## 4. Formal parameter and Newton solves

Suppose x*(p) is a differentiable exact fixed-point branch and I-J is invertible. Differentiating T(x*(p);p)-x*(p)=0 gives

 (I-J) x_p=T_p.                                            (2)

For m=q(b)^T x*(b,lambda)+lambda c_f-1-b/2, where c_f is fixed, therefore

 m_lambda=q^T(I-J)^-1 T_lambda+c_f,
 m_b=q_b^T x*+q^T(I-J)^-1 T_b-1/2.                          (3)

If m_lambda!=0 and the implicit branch is valid, lambda_b=-m_b/m_lambda. These are conditional derivative identities. Replacing J,T_p by sampled differences and x* by a nonzero-defect state gives a linearized diagnostic, not a verified differentiable branch. Near singularity, small data errors can produce large errors in the solves.

For a Newton step delta in T(x*+delta)-(x*+delta)=0, first-order expansion yields (I-J)delta=f. Check this solve by its residual as well as its size. A small residual of this linear solve does not bound the nonlinear remainder or prove a nearby fixed point.

At fixed L and fixed knot vector, the exact strain row in the native r2 basis is proportional to b:

 q_kj=-(b L/4)(1_{k=1}-1_{k=3})(t_{j+d+1}-t_j)/(d+1),
 q_b=q/b.                                                  (4)

The lower active index is j>=floor(k/2); it is independent of b. Formula(4) follows by the exact radial and angular integrations in P205. Retieing the basis changes T_b and the represented field; it does not alter the derivative identity q_b=q/b at these fixed coordinates. The source geometry and c_f must remain fixed for (3).

## 5. The correct divided-field dilation

The exact B2 spatial family is Omega_l(X)=Omega(X/l), hence

 G_l(X)=l^-1 G(X/l),
 v_true(X)=d_l G_l(X)|_{l=1}=-G(X)-X.grad G(X).             (5)

The field v_old=-X.grad G omits the amplitude factor. It has v_old(0)=0, whereas v_true(0)=-G(0). The canonical strain c(G_l) is constant under the full dilation, so c(v_true)=0; c(v_old)=c(G), whenever differentiation and the strain integral commute. They do commute for the actual degree5 native finite-spline class with simple interior knots: G and rG_r have the same integrable endpoint orders uniformly for l in a compact interval about1, and knot points have measure zero with continuous first derivatives. More generally this reasoning applies at degree d>=2 with interior knot multiplicity at most d-1. We make no C1 assertion about arbitrary degree1 splines. In this forced map a0, lambda and the source are fixed, so even the true dilation is not an exact symmetry of T. No condition Av_true=0 is expected from B2 scaling alone.

For e!=0 and e^2!=1 write G_plus=G(X/(1+e)), G_minus=G(X/(1-e)). The centered finite-difference fields satisfy the exact identity

 [G_plus/(1+e)-G_minus/(1-e)]/(2e)
 = { [G_plus-G_minus]/(2e) - (G_plus+G_minus)/2 }/(1-e^2).   (6)

For any fixed linear fit operator F, the same identity holds after F. Thus subtracting the fitted original coefficient vector from an old finite-difference direction only approximates the corrected finite-step direction: it is exact at the derivative limit if F reproduces G, with an O(e^2) difference under sufficient radial differentiability. That correction must not be labeled an exact reconstruction of an unpublished finite-step fit.

## 6. Independent physical evaluation of dilation directions

Use r,phi with x_cartesian=r sin(phi), y=-r cos(phi). Put u=1-t=(1+r^2/L^2)^(-1/(2b)), eta=r/sqrt(r^2+L^2), D=u^(b+1), and for mode k write

 G_k(r)=D eta^o S_k(t), o=k mod2,
 r t_r=u eta^2/b,
 r (log D)_r=-(b+1)eta^2/b,
 r (log eta)_r=1-eta^2.

Differentiating gives

 -r G_k'(r)=D eta^o [ ((b+1)eta^2/b-o(1-eta^2))S_k
                              -u eta^2 S_k'/b ],          (7)

and the bracket for v_true is that of (7) minus S_k. This uses analytic SciPy B-spline derivatives, separately from the numerics lane's finite differences. Radial centered differences at points strictly inside knot cells supply an independent consistency control; they do not prove a finite-resolution error bound.

Let w=(r/R)^delta+(R/r)^delta with 0<delta<min(2,2/b). Angular orthogonality gives the exact squared norm of any error expressed by bracket E_k(t):

 ||E||_w^2=pi b L^2 sum_k a_k int_0^1 u eta^(2o) w(r(t)) E_k(t)^2 dt,
 a_0=2, a_k=1 for k>0.                                    (8)

Indeed the cosine modes have squared angular norms pi a_k and D^2 r dr=b L^2 u dt. Equation(8) is used with S_saved minus either bracket in(7), not with the numerics fitting quadrature. Endpoint-weighted Gauss-Jacobi rules and a refinement comparison approximate these full-plane integrals. The physical projection of v_true onto the finite basis solves H z=h, where h is formed with the same physical inner product. That projection is not the numerics lane's residual-grid least-squares fit. It need not preserve the exact zero strain of v_true: q^T z can be nonzero because v_true is generally outside the finite span. The sharp P205 dual bound controls |q^T z-c(v_true)| by the physical approximation error; a test of A_h z applies to this coefficient projection, not directly to the continuum derivative.

## 7. Scope and forthcoming evidence

The archive must be identified by hash and tied to its state, active indices, beta, lambda and step. Verify all reported algebra that the arrays support. The raw map evaluations, full coordinate-column step study, weighted-grid Gram factor and nonlinear remainder are not present unless explicitly saved; do not invent their independent verification. Independently recomputed scalar summaries of a given stored matrix confirm its algebra, not the validity of the underlying PDE discretization. No full-plane profile is accepted on the basis of this packet.

## 8. What an operator-error bound would need to establish

Let M_h=I-J_h and let C be the physical upper Cholesky factor of Section3. Write sigma=sigma_min(C M_h C^-1). Let M=I-J be an exact derivative matrix in the same finite-dimensional space at the same point and with the same fixed parameters. Suppose an independently justified error bound

 ||C(J-J_h)C^-1||_2 <= eta < sigma                         (9)

is available. Then M is invertible and ||C M^-1 C^-1||_2 <= 1/(sigma-eta). Indeed for every y,

 ||C M C^-1 y|| >= ||C M_h C^-1 y||-eta||y||
                    >= (sigma-eta)||y||,

which implies injectivity and hence invertibility in the fixed finite dimension. Equivalently one may use the convergent Neumann series of the perturbation of M_h. This argument does not apply to the infinite-dimensional PDE operator merely because a finite basis was used.

For a parameter column t with approximation t_h, let z_h=M_h^-1 t_h. If ||t-t_h||_H<=epsilon, then the exact solution z=M^-1 t obeys

 ||z-z_h||_H <= (epsilon+eta||z_h||_H)/(sigma-eta).          (10)

To prove (10), put E=J-J_h, so M=M_h-E and M(z-z_h)=(t-t_h)+E z_h, and use (9). The physical dual norm of the exact strain row is Q=sqrt(q^T H^-1 q). Thus the error in q^T z is at most Q times the right side of (10). Errors in an explicit source term, in q itself, or in the base point must be added separately. Formula(10) is not an error bar when eta and epsilon have not been established. In particular a step study on12 chosen coordinate columns does not supply (9): it omits other columns, potential coherent error, trajectory errors and their conversion into the chosen physical norm.

For interpretation of weak vectors we will use physical energy. If the angular modes are orthogonal, the energy in mode k is z_k^T H_k z_k, not the unweighted sum of squared coefficients. Radial energy in an interval [r1,r2] is the corresponding restricted version of (8), summed over modes. Both are nonnegative and their sums over a partition equal ||G_z||_w^2. Numerical quadrature can report these fractions with an order comparison. They describe spatial distribution of the represented vector in the declared norm, not continuum eigenfunctions or a proof of neutral scaling.

## 9. Comparison with the previously independent characteristic response

P200 independently reconstructed scalar transport for the same frozen native state, beta and lambda. Its velocity is obtained by this lane's full-plane adaptive modal inverse, with a separate Cartesian inverse check, then interpolated for backward characteristics. At each lambda it projects the total strain with the exact row q, holding the unprojected coefficients, beta, source geometry and temperature amplitude fixed. The resulting finite-cutoff map at a physical point is not the numerics lane's fitted coefficient map.

At fixed beta the native basis is independent of lambda. Therefore a stored column dT_dlambda represents a divided-field response G_{dT_dlambda}(X). Its vorticity response at a physical point is x_cartesian G_{dT_dlambda}(X). This is a fixed-input map response, not the branch response (I-J)^-1 dT_dlambda. It can be compared with P200's independently computed lambda derivative of reconstructed vorticity. Similarly x_cartesian G_{x_star+f0} can be compared with its reconstructed base vorticity.

The scalar transport reconstruction at a fixed velocity is linear in the seed amplitude a0: the temperature, its gradient, the seed vorticity and the forcing in the vorticity equation all scale by that factor. P200 used the native stored F(0), whereas the supplied matrix run declares its a0 separately. A ratio of those explicit amplitudes converts its values to the same seed amplitude without changing any field, inverse or trajectory. The negligible difference is still recorded.

We will compare every one of P200's saved cutoff, interpolation, step and tolerance variants at five already chosen points. A finite spread among those variants is a convergence diagnostic, not an enclosure. A discrepancy between the fitted column and these point values includes representation, map-discretization and differentiation effects; the comparison cannot isolate them, and does not bound the error of the entire finite matrix. No pass/fail threshold for the full derivative will be inferred from a few points.

## 10. Sharp finite-matrix perturbation threshold and expansion

Write B=C(J_h-I)C^-1 and suppose unit real singular vectors u,v satisfy Bv=sigma u for its smallest singular value sigma. The rank-one perturbation E_H=-sigma u v^T has norm sigma and (B+E_H)v=0. Consequently E=C^-1 E_H C is a perturbation of J_h with induced H-norm sigma for which J_h+E has eigenvalue1. Combined with Section8, sigma is exactly the unstructured normwise distance to loss of invertibility of I-J_h in this finite-dimensional metric. This is an algebraic sensitivity statement. It neither supplies an actual error perturbation nor shows that a perturbation obeying the structure of the true derivative has this size or direction. A floating-point SVD supplies numerical values, not interval-certified singular vectors.

The triangle inequality gives ||J_h||>=||J_h-I||-1, in either the coefficient or induced H norm. A value larger than1 rules out contraction in that norm for this linear matrix. If J_h were the exact derivative at an exact fixed point, spectral radius below1 would imply asymptotic linear stability and allow an equivalent finite-dimensional norm in which the derivative norm is below1. It would not imply contraction in an already specified norm. For the actual sampled array, neither the exact derivative nor an exact fixed point has been certified, so no such nonlinear conclusion follows.

For any nonzero v the inner-product identity is

 ||J_h v||^2/||v||^2 = ||(J_h-I)v||^2/||v||^2 - 1
                         + 2 <v,J_h v>/||v||^2.           (11)

It follows by expanding the squared norm of J_h v-v. In particular a ratio1 for J_h-I does not imply J_h v=0: J_h v=2v is a counterexample. Only Av=0 is excluded. The exact projection direction q is removed by the exact map, whereas a general dilation direction need not be. Measure its action directly rather than calling it removed solely because its A ratio is near1.

Finally, if two independent numerical methods differ by more than the spread of a finite set of variants of either method, that is an inter-method discrepancy. Without an enclosure for either method one cannot assign the error to one method or prove that its variant spread underestimates its own true error. The discrepancy can include representation, derivative, inverse and trajectory errors on either side. The lambda-response comparison is recorded on this basis.

## 11. A small defect and an invertible exact derivative do not prove a nearby root

For epsilon>0 define the smooth scalar map T_epsilon(x)=epsilon+x^2/epsilon. At x0=0 its defect is epsilon and its exact derivative is0. Thus I-T_epsilon'(0)=1, the spectral radius of the derivative is0, and the linearized Newton correction is epsilon. Nevertheless the fixed-point equation would require

 x^2-epsilon x+epsilon^2=(x-epsilon/2)^2+3epsilon^2/4=0,

which is impossible for every real x. Its defect and Newton step can be arbitrarily small without any fixed point. This refutes the general implication from a small Newton correction and an invertible derivative at an approximate point to a certified nearby exact fixed point. A posteriori existence needs additional neighbourhood information, such as a suitable bound on the nonlinear remainder and a verified ball mapped into itself. In particular, the stored matrix diagnostics alone do not establish an error bar for m, an exact fixed-point branch, or an implicit zero curve of m. They do not refute existence of a fixed point for the numerics lane's particular map; that existence remains open.
