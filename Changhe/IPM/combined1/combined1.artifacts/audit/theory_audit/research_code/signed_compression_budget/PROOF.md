# A signed finite-compression bound for the largest commutator eigenvalue

## Setting and exact statement

Let K be the self-adjoint Hilbert-Schmidt commutator of the two parity-budget dependencies. Let H be its S1 reducing subspace. Suppose the complete squared Hilbert-Schmidt norm of K is kappa2, and finite compressions in the other three parity spaces have total squared norm T_other. Thus

    ||K restricted to H||HS^2 <= kappa2-T_other.

Choose any finite linearly independent real family in H. Write G for its L2 Gram matrix and B for its K-compression matrix. Define

    T_H=tr(G^-1 B G^-1 B).

Let q>=0 be any number such that qG-B is positive semidefinite. Then the quadratic-form upper bound on H is

    <K h,h> <= gamma ||h||2^2,
    gamma=sqrt(kappa2-T_other-T_H+q^2).                  (1)

The radicand is nonnegative whenever the hypotheses hold. The bound improves the unspecialized Hilbert-Schmidt estimate whenever T_H>q^2. If it does not, one may retain the previous bound. In validated arithmetic use an upper bound on kappa2, lower bounds on the two T values, and an upper certificate q for the finite generalized eigenvalue problem.

For the IPM low generator under the exact hypotheses in the parity-budget dependency, (1) yields the decay and inverse rate

    beta=c+1-theta-gamma,

provided beta>0. Only the largest positive commutator eigenvalue is relevant to this energy estimate. This is not an upper bound on the absolute operator norm if negative eigenvalues are larger in magnitude. It neither proves a high-space inverse nor enlarges a nonlinear ball without a new closure calculation.

## Proof of the spectral budget

Write A=K restricted to H and let P be the orthogonal projection onto the selected finite span. Its finite self-adjoint compression C=PAP has positive eigenvalues mu_1>=mu_2>=...>0 and negative eigenvalues -nu_1<=-nu_2<=...<0, where the nu_i are listed in decreasing order. Zero eigenvalues can be omitted. Put alpha=max(0,lambda_max(C)), with alpha=0 if C has no positive eigenvalue. Then

    ||C||HS^2=alpha^2 + sum_{i>=2} mu_i^2 + sum_i nu_i^2,

where the positive sum is empty when C has no positive eigenvalue.

The compact self-adjoint operator A has positive eigenvalues lambda_1>=lambda_2>=...>0 and negative eigenvalues -eta_1<=-eta_2<=...<0. The min-max characterization gives lambda_i>=mu_i and eta_i>=nu_i for every index present in C. For completeness, the positive characterization takes the supremum, over all i-dimensional subspaces, of the infimum of the Rayleigh quotient on that subspace. Restricting those subspaces to ran P gives the compression eigenvalue and cannot increase the supremum. Apply the same argument to -A for the negative eigenvalues.

The largest spectral point of A is max(0,lambda_1), with value zero if A has no positive eigenvalue, since A is compact on the infinite-dimensional H. Its square plus the squared compression eigenvalues other than the first positive one is at most ||A||HS^2. Consequently

    max(0,sup spectrum(A))^2 <= ||A||HS^2-||C||HS^2+alpha^2.

The isometry from coefficient space is S G^-1/2, where S maps coefficients to the chosen functions. Hence ||C||HS^2=T_H. The matrix inequality qG-B>=0 implies C<=qI, so alpha<=q. The complementary parity bound proves (1). This derivation accounts for each eigenvalue once and does not infer that the finite matrix has captured the whole spectrum.

## Exact tests and validation

Use the Poisson derivative functions of the angular parity proof with odd sine harmonics only:

    f_{m,n}=Im(partial_x+i partial_y)^m partial_z^n
             (z^2+r^2)^(-1/2) evaluated at z=1,
    h_{m,n}=-Delta f_{m,n},  m odd.

They are even in x and odd in y. Their Gram and commutator matrices are rational after division by pi, by the exact full-plane formulas already derived. Positive definiteness of G follows either from distinct Fourier monomials within each harmonic or an exact LDL check. T_H is evaluated as a rational number. A positive definite rational LDL decomposition of qG-B is a certificate of the required eigenvalue upper bound; no floating eigenvalue is accepted as that certificate.

A floating generalized eigenvalue calculation may select q, but the final q and LDL pivots must be exact rationals. Binary search based on exact positive-definiteness checks is also permitted. Existing exact complementary-block matrices can be reused only with their recorded input hashes and the same canonical candidate.

## Dependencies, status and scope

Dependencies: the self-adjoint signed decomposition and complete commutator Hilbert-Schmidt identity; the parity-budget theorem; the explicit Poisson pairing formulas; the elementary compact self-adjoint spectral theorem and min-max argument supplied above. This is a new theorem awaiting independent T1/T2 review. Candidate calculations require a separate independent arithmetic review. All computations are local and finite. No numerical evidence is used to assert invertibility or existence.
