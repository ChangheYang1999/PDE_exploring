# Independent full-plane first-derivative matrix certificate

## 1. Target and exact setting

Let chi be the exact rational d2 potential described by source/d2_canonical.json, with c=4076476460239181/2251799813685248, delta=1-1/c. Define rho=-partial_y Delta chi, psi=partial_x partial_y chi, u=(-psi_y,psi_x), and

    A=[[rho_y,-rho_x/2],[-rho_x/2,0]], M1=I-sym Du+A.

The target is M1(X)>=(9/10)I for every X in R2. This is the unweighted first-derivative condition in T4-019. It is different from the earlier matrix involving the weight (1+r^2)^(-1/10). No conclusion is asserted until the output has a complete partition, no pending cells and every accepted cell passes its interval test.

This proof gives the exact reconstruction and the soundness of the certificate. Source data, scalar constants and rational polynomial coefficients are imported from JSON, not from rounded tables in this document. No proof assistant is run.

## 2. Independent matrix reconstruction

Set t=r^2/(1+r^2), u0=1-t and z=cos(2theta). T4's independently derived polar fields are

    rho=r sum_(j,n) u0^a R_(j,n)(t) sin(n theta),
    psi=r^2 sum_(j,n) u0^a S_(j,n)(t) sin(n theta),
    a=(j+1)delta/2.

The density has odd n and the stream function has positive even n. All coefficients of the polynomials R,S are rational. The previously completed density-gradient reconstruction gives

    rho_y=sum_j u0^a Y_j(t,z).

Its frozen exact coefficient file is source/T4_gradient.json. It was derived from rho, not from the fourth potential derivatives.

For any polynomial P let T_(a,k)P=(k-2at)P+2t(1-t)P'. Since u1=-partial_y psi, the stream mode S at harmonic n contributes the following cosine coefficients to u1/r:

    C_(n-1)=-(T_(a,2)S+nS)/2,
    C_(n+1)=( T_(a,2)S-nS)/2.

Add coefficients at matching (j,n). For each resulting odd cosine mode r u0^a C cos(n theta), its x derivative has cosine coefficients

    (T_(a,1)C+nC)/2 at n-1,
    (T_(a,1)C-nC)/2 at n+1,

and its y derivative has sine coefficients

    -(T_(a,1)C+nC)/2 at n-1,
     (T_(a,1)C-nC)/2 at n+1.

These follow by writing partial_x=cos(theta)partial_r-sin(theta)r^-1 partial_theta and partial_y=sin(theta)partial_r+cos(theta)r^-1 partial_theta, then applying the product-to-sum identities. Chebyshev identities cos(2m theta)=T_m(z) and sin(2m theta)=sin(2theta)U_(m-1)(z) give rational polynomials D_j,E_j such that

    partial_x u1=sum_j u0^a D_j(t,z),
    partial_y u1=sin(2theta)sum_j u0^a E_j(t,z).

The code verifies exactly D_j=-chi22_j and E_j=-chi13_j against N4's independent derivative arrays. This is a coefficientwise check, not a sampled comparison. Directly from the definitions,

    Du=[[-chi22,-chi13],[chi31,chi22]],
    rho_x=-chi31-chi13, rho_y=-chi22-chi04.

Consequently

    M1-(9/10)I = [[1/10+sum u0^a(Y_j-D_j),
                   -sin(2theta)sum u0^a E_j],
                  [-sin(2theta)sum u0^a E_j,
                   1/10+sum u0^a D_j]].                   (1)

The code also checks Y_j-D_j=-chi04_j exactly. Thus every matrix entry has an independent reconstruction from the density and stream function.

## 3. Interval positivity test

On a rational cell [a,b] times[c,d] in (t,z), let L1,L2 be lower bounds for the two full diagonal entries in (1), and let Q be an upper bound on the modulus of its off-diagonal polynomial factor before sin(2theta). Let zmin be zero if the angular cell contains zero, and otherwise min(|c|,|d|). The following three inequalities suffice:

    L1>=0, L2>=0,
    L1 L2-(1-zmin^2)Q^2>=0.                                (2)

Indeed the actual diagonals are at least L1,L2 and nonnegative, and the square of the off-diagonal is at most(1-zmin^2)Q^2. The determinant is therefore nonnegative, which together with the diagonal inequalities makes the real symmetric two-by-two matrix positive semidefinite. This determinant test is different from N4's least-eigenvalue interval formula.

## 4. Bounds for the branch polynomials

Map each cell affinely to[0,1]^2. For a degree-N power polynomial sum p_k x^k, its degree-N Bernstein coefficient at index i is sum_(k<=i) p_k binom(i,k)/binom(N,k). The tensor Bernstein basis is nonnegative and sums to one, so the extreme coefficients enclose the polynomial on the closed cell. All transformations use outward Arb arithmetic on exact rational input coefficients.

The first enclosure bounds each positive branch weight(1-t)^q independently between(1-b)^q and(1-a)^q and multiplies this by the full branch polynomial interval. It remains valid on cells reaching b=1.

If b<1, use a correlated enclosure. Put v0=1-(a+b)/2, kappa=(b-a)/(2v0), x=(t-a)/(b-a). Then

    (1-t)^q=v0^q(1+kappa(1-2x))^q.

Multiply its degree8 Taylor polynomial by the local branch polynomial before conversion to Bernstein form. All branch exponents here satisfy0<q<9. The remainder is bounded by

    |binom(q,9)|v0^q kappa^9(1-kappa)^(q-9).

This follows from the Lagrange remainder on the positive interval[1-kappa,1+kappa], since the absolute ninth derivative is bounded by its value at the smaller endpoint. Multiply this error by the maximum absolute Bernstein bound of the branch polynomial, and sum all branch errors. Intersecting the correlated and independent intervals preserves a valid enclosure.

## 5. Coverage, continuation and scope

The initial partition consists of N4's227 accepted binary paths. The code independently verifies complete coverage by collapsing deepest sibling pairs to the root, rejecting duplicates, missing siblings and invalid path letters. An inconclusive cell is replaced by its two exact halves on one coordinate. Accepted plus pending cells are checked to form a complete partition after every step. This proves that a completed run covers the full closed rectangle[0,1] times[-1,1]. Stopping with pending cells gives no global assertion; continuation retains their exact paths and verifies all source/code hashes.

The compactification covers a quadrant, its origin and its limiting far field. The entries in(1) extend continuously through those limits, as follows from their rational polynomial representation and positive branch exponents. S1 reflection changes only the sign of the off-diagonal, so the matrix eigenvalues are the same on the other quadrants. A completed certificate thus proves the target on all of R2.

A successful result certifies only the stated first-derivative matrix. It supplies no fourth-derivative cap, residual threshold or existence result. The signed L2 target has its own independent completed certificate in ../signed_cover_audit/ and is not reused as a substitute for(1).
