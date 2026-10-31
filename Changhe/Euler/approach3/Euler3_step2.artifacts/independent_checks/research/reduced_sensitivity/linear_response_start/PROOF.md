# A zero-preserving coefficient response need not lower the objective

Status: proved finite-dimensional identities and exact counterexamples. This is a statement about a saved linear least-squares model. It neither rejects the proposed initialization heuristic nor predicts the outcome of an Euler optimization.

## Statement, hypotheses and notation

Let m, a and k be positive integers. Give all real vector spaces their Euclidean inner products. Let A be a real m by a matrix, B a real m by k matrix, q in R^m, and c a nonnegative real constant. The coefficient and parameter displacements are h in R^a and p in R^k. Define the affine least-squares model

M(h,p) = c + (1/2) ||q + A h + B p||^2.

Choose any set I of strictly positive singular values in a singular-value decomposition of A. The empty set is allowed. In particular, I may contain exactly those singular values exceeding tau times the largest singular value, for a fixed tau >= 0; when A = 0, take I empty. Write U_I and V_I for the associated orthonormal left and right singular vectors and Sigma_I for the positive diagonal matrix of their singular values. Define

H = range(V_I), G = V_I Sigma_I^(-1) U_I^T, P = U_I U_I^T.

For empty I take H = {0}, G = 0 and P = 0. For each p define the zero-preserving response h_resp(p) = -G B p. It is the unique minimizer in H of ||A h + B p||^2, and h_resp(0) = 0. The following difference identity holds exactly:

M(h_resp(p),p) - M(0,p)
= - q^T P B p - (1/2) ||P B p||^2.                    (1)

Consequently h_resp(p) is no worse than keeping the coefficients in this affine model if and only if

q^T P B p + (1/2) ||P B p||^2 >= 0.                 (2)

The sufficient condition P q = 0 is stationarity in the retained coefficient subspace: it is equivalent to V_I^T A^T q = 0. It is not assumed by the construction of h_resp. Without it, (2) can fail for arbitrarily small p, even for an exact linear residual.

The unique minimizer of M(h,p) over h in H is instead

h_opt(p) = -G (q+Bp).                               (3)

Thus h_resp(p) = h_opt(p)-h_opt(0). The full affine minimizer (3) preserves zero displacement at p=0 exactly when Pq=0. There is no general incompatibility between a zero-preserving map and descent, but the particular response -GBp does not guarantee descent relative to keeping coefficients.

## Proof

Write every h in H uniquely as V_I y. Then Ah = U_I Sigma_I y. Orthogonal decomposition into range(U_I) and its orthogonal complement gives

||Ah+Bp||^2
= ||Sigma_I y+U_I^T Bp||^2 + ||(I-P)Bp||^2.

Since Sigma_I is invertible, the unique minimizer is y=-Sigma_I^(-1)U_I^T Bp, proving the response formula and its uniqueness. The empty case has only h=0 and satisfies the same formulas.

At the response, Ah_resp=-PBp. Put v=Bp. Expanding squared norms gives

2[M(h_resp,p)-M(0,p)]
= ||q+v-Pv||^2-||q+v||^2
= -2(q+v)^T Pv + ||Pv||^2
= -2q^T Pv - ||Pv||^2,

where v^TPv=||Pv||^2 follows from P being an orthogonal projector. This proves (1), hence the equivalent condition (2). If Pq=0, the first term in (1) vanishes. Conversely V_I^T A^T q=Sigma_I U_I^T q, so its vanishing is equivalent to U_I^T q=0 and hence Pq=0.

Replacing Bp by q+Bp in the first orthogonal decomposition proves (3). Subtracting (3) at p=0 proves the response-difference identity. Since Sigma_I is invertible, Gq=0 is equivalent to Pq=0, which proves the zero-displacement statement.

For the failure at arbitrarily small p, let m=a=k=1, A=B=[1], q=-1, c=0 and retain the sole singular value. For every 0<p<2, h_resp=-p, and

M(h_resp,p)=1/2,
M(0,p)=(1-p)^2/2,
M(h_resp,p)-M(0,p)=p-p^2/2>0.

Thus even a residual that is exactly affine gives a worse response start than the kept start. At p=1/10, the two costs are 1/2 and 81/200, with difference 19/200. At p=-1/10 the response is better by 21/200. At p=0 the response is zero, while h_opt(0)=1. This proves every asserted non-implication without numerical roundoff or nonlinear remainders.

## Transfer from a saved QR factor and its permutation

Let n=a+k, let J be a real M by n matrix, and let r in R^M. Let pi be a permutation of {0,...,n-1} and let the permutation matrix T satisfy (Tz)_i=z_{pi(i)}. Let d_i>0 be the saved scales in that permuted order. Suppose the exact factorization is

J T^T diag(d)^(-1) = Q R,     Q^T Q=I_n.

For a coordinate displacement delta_z define s_i=d_i (delta_z)_{pi(i)}. Reconstruction is the scatter assignment

(delta_z)_{pi(i)} = s_i/d_i.                        (4)

If the stored array d is already permuted, it is used directly in (4). Applying pi to d again generally changes the displacement. The parameter columns are selected by their recorded positions in the permuted coordinates; they need not be the last k columns.

Indeed delta_z=T^T diag(d)^(-1)s, so J delta_z=QRs. Taking q=Q^Tr and c=(||r||^2-||q||^2)/2 gives

(1/2)||r+J delta_z||^2 = c+(1/2)||q+Rs||^2.

Splitting the columns of R into the selected coefficient and parameter positions gives precisely the model above. The component of r orthogonal to Q is constant and cancels from (1). This is an exact isometry identity; a saved floating-point factor requires its own binding and numerical consistency checks. A declared singular-value cutoff changes the retained coefficient subspace and must be recorded.

## Physical parameters and actual initialization

If z_w=log(omega) and omega>0, the optimizer displacement from omega_0 to a specified omega_1>0 is log(omega_1)-log(omega_0). The tangent value (omega_1-omega_0)/omega_0 is only a first-order approximation and is not the same finite displacement. Other nonlinear parameter maps require the corresponding difference of inverse-map coordinates. The proposed response must state which displacement it uses.

A smooth nonlinear residual agrees with its affine model only to first order in displacement. Even when Pq=0 gives an affine comparison, that alone supplies no finite-displacement ordering for the full nonlinear objective. Evaluate kept and response candidates with the same actual parameter values, constraint map, gauge convention and objective settings. Selecting the lower measured iteration-zero objective is a well-defined heuristic; it does not certify a profile minimum or the best finite-budget optimizer output.

## Dependencies and scope

Dependencies: the singular-value decomposition, orthogonal projection, elementary quadratic algebra, and the saved-QR isometry identity also proved in ../PROOF.md. The initialization interpretation uses ../../profile_initialization/PROOF.md.

The exact counterexample is checked using rational arithmetic in verification/check_exact_examples.py. No Lean or other formal build has been run; formal/README.md records that limitation. No Euler checkpoint, Jacobian or nonlinear objective has been recomputed for this proposition. It does not determine whether the proposed response helps any campaign state.
