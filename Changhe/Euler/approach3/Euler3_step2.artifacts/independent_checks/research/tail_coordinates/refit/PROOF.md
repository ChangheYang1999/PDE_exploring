# Fixed-parameter field refitting in reduced coefficient coordinates

## Statement and hypotheses

Let p be a fixed admissible pair (c,omega). Let x belong to R^n, let E_p:R^n -> R^N be a linear map imposing the homogeneous tail constraints at p, and let A_p:R^N -> R^m give the sampled velocity of the represented field at p. The same velocity components and evaluation points are used in the target b in R^m. Let W be a positive diagonal m by m matrix. Define B_p=W A_p E_p. Every map in this statement acts on finite-dimensional real spaces; no continuum error bound is assumed.

The weighted refit minimizes ||B_p x-W b||_2 over x. Holding p fixed, the field derivative at x=0 is A_p E_p and the field value at x=0 is zero. Thus a coefficient Jacobian at zero is the correct linear fit matrix. Treating the entries of p as additional fit coordinates does not implement this problem. The map E_p must be evaluated at the prescribed p even at the zero coefficient vector.

Suppose the fit scales columns by a positive diagonal matrix D and uses the singular value decomposition B_p D^(-1)=U Sigma V^T. Select a set I of strictly positive retained singular values. Then x_I=D^(-1) sum_{i in I} v_i (u_i^T W b)/sigma_i minimizes the weighted residual among coefficient vectors whose scaled coordinates lie in span{v_i:i in I}. Its weighted residual is W b minus its orthogonal projection onto span{u_i:i in I}. This is the full least-squares minimum only if all omitted singular directions have zero target component or no smaller residual is possible in those directions.

In particular, if a self-refit uses identical parameters, nodes, basis and constraints, and the target has a representation in the retained subspace, then the exact-arithmetic residual is zero. Without the retained-subspace hypothesis, a nonzero self-refit error can come from singular-value truncation even if the source field is representable in the full space.

## Proof

At fixed p, both E_p and A_p are linear. Therefore A_p E_p x has value zero at x=0 and derivative A_p E_p at every x. Multiplication by W gives the first assertion. In contrast, the joint expression A_p E_p x is generally not a linear function of (x,p); the campaign's tail-constraint matrices contain alpha=(1-c)/c and omega/c. Evaluating their parameter slots as zero can make the map undefined, before any least-squares step takes place.

Set y=D x and expand y in the orthonormal right singular vectors. In the retained subspace, ||U Sigma V^T y-W b||_2^2 is a sum of (sigma_i y_i-u_i^T W b)^2 over retained indices plus the squared norm of the target component orthogonal to their left singular vectors. Each retained square is minimized by the stated coefficient. This proves the minimization and projection statements. The self-refit conclusion follows when W b lies in the retained left singular subspace.

## Relevance and scope

The implementation can preserve the free-parameter model layout while fitting only coefficient coordinates: append the prescribed p before expanding the tail constraints, retain only the expanded coefficient entries, and let the field wrapper append p exactly once. The returned full vector then has N+2 entries and the prescribed last two entries. This layout statement is separate from numerical conditioning or field accuracy.

A raw fit can be changed by a subsequent far-field gauge projection or phase alignment. Comparisons of accepted starts must therefore identify whether they use raw fits or the actual post-projection starts. An unweighted array norm on selected training nodes is a discrete sampling diagnostic; it is not a physical-volume shell integral unless the correct quadrature weights are included. Changing p can also change the weights, far exponent and represented field despite unchanged coefficients.

Dependencies are elementary finite-dimensional linear algebra and the campaign tail-coordinate definition in ../PROOF.md. The result is conditional on invertibility of the tail-constraint elimination at the fixed p. It proves neither a continuum approximation guarantee nor equality of optimized Euler profiles.
