# Finite branch-comparison criteria and their scope

Status: exact elementary statements about the registered numerical comparison. These statements do not identify Euler solution branches.

## Statement and notation

Let J be a finite nonempty shell index set. On each shell let ||.||_j be a norm, and let U and V have strictly positive finite norms in every shell. Define

d(U,V) = max_j ||U-V||_j / ||V||_j,

D(U,V) = max(d(U,V), d(V,U)).

Then D is symmetric and nonnegative. It vanishes if and only if U and V agree as elements of every shell normed space. For each j,

| ||U||_j - ||V||_j | <= ||U-V||_j <= ||U||_j + ||V||_j.

Consequently D(U,V)<=tau implies, in both directions, a norm difference at most tau times the corresponding denominator norm. A missing, nonfinite or zero denominator does not define this criterion. Omitting that shell changes the index set and therefore changes the test.

Let z(c,w)=(log(x/(1-x)),log(w)), where x=(c-0.4)/0.1, 0.4<c<0.5 and w>0. Let D_p be a positive diagonal two by two matrix in these optimizer coordinates. Let S be a symmetric positive definite two by two matrix, with orthonormal eigenvectors w_1,w_2 and eigenvalues lambda_1,lambda_2>0. Let L>0, epsilon>0, and t_i=sqrt(2 epsilon L/lambda_i). For two parameter points z_a,z_b define

h=D_p(z_b-z_a), c_i=w_i^T h.

The registered coordinatewise criterion is |c_i|<=t_i for both i. It is a box in eigenvector coordinates. It implies

(1/2) h^T S h <= 2 epsilon L.

It does not in general imply the smaller bound epsilon L. The latter requires the elliptical criterion sum_i(c_i/t_i)^2<=1.

For a quadratic q(h)=q(0)+g^T h+(1/2)h^T S h, neither box nor ellipse bounds the rise q(h)-q(0) without controlling g. About the minimizer h_*=-S^(-1)g, the quadratic rise equals the curvature term. A profile displacement z=z_a+k t_i D_p^(-1)w_i has h=k t_i w_i and curvature term k^2 epsilon L.

## Proof

Symmetry and nonnegativity follow directly from the definition of D. Since each denominator is positive, D=0 is equivalent to every difference norm being zero. The two norm inequalities follow from the triangle inequality, applying it also to U=(U-V)+V and V=(V-U)+U.

Because the eigenvectors form an orthonormal basis, h=sum_i c_i w_i and h^T S h=sum_i lambda_i c_i^2. Under the box criterion each term lambda_i c_i^2/2 is at most epsilon L. Summing two terms proves the factor-two bound. Taking c_i=t_i for both i attains it, so the smaller bound is false in general. Dividing by epsilon L gives the stated ellipse formula.

Expanding q(h_*+v), and using g+S h_*=0, cancels the linear term in v and gives q(h_*+v)-q(h_*)=v^T S v/2. At the current point the term g^T h remains. Substituting the profile displacement gives its curvature term directly.

## Threshold agreement need not be transitive

Even with positive unit norms, a threshold comparison need not be an equivalence relation. On a single shell take a two-dimensional Euclidean subspace with orthonormal elements e_1,e_2 and U(theta)=cos(theta)e_1+sin(theta)e_2. Each U(theta) has norm one and

D(U(theta),U(phi))=2|sin((theta-phi)/2)|.

Choose delta=2 arcsin(0.04). Consecutive fields U(0),U(delta),U(2delta) have distance 0.08, while the endpoint distance is 0.16 sqrt(1-0.04^2)>0.10. Thus consecutive pairs pass the threshold 0.10 and the endpoints fail. Declaring a whole connected component to satisfy every pairwise comparison is invalid without checking those pairs.

The same construction can be repeated on all shells. The additional registered parameter criterion does not restore transitivity when all three fields have identical parameter values, since all their parameter displacements then vanish.

## Missing endpoint evidence

The registered parameter criterion is the logical OR of the tests at the two endpoints, with each endpoint's own sensitivity and scaling. If one endpoint passes, the OR passes. If both fail, it fails. If one fails and the other is unknown, the OR is unknown. The full pair criterion is the logical AND with the field criterion: a confirmed field failure makes the conjunction fail even if parameter evidence is missing. These are statements about the declared tests, not about actual equality of mathematical solution branches.

## Dependencies and scope

Dependencies: triangle inequality, elementary trigonometry, the spectral theorem for a real symmetric matrix, and the reduced quadratic identities in ../reduced_sensitivity/PROOF.md. Finite quadrature norms require positive weights and adequate angular evaluation; numerical validity is checked separately.

The shell list, F normalization, coordinate map, cutoff, matrix record and endpoint bindings must be fixed explicitly. Neither observed finite-grid agreement nor these linear-model boxes prove that two fields solve Euler, belong to a common continuation branch, or have identified physical parameters.
