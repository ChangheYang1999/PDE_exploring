# Elementary dual certificates for the ternary-quartic Laplacian cone

Status: independent reconstruction and existing coordinator comparison complete. Exact verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md). This proof does not import Hilbert's theorem, cone separation or any earlier quartic-cone result.

## 1. Exact theorem

Let K consist of the real symmetric three-by-three matrices C for which there is a nonnegative real homogeneous quartic F on R3 with Delta F(x)=x^T Cx. Let

    D={B symmetric positive definite: tr B=1, tr B^-1<=49}.

Then C belongs to K exactly when tr(BC)>=0 for every B in D. Every such C has some quartic preimage which is the sum of at most two squares of real homogeneous quadratics. This does not say that every nonnegative quartic itself is a sum of two squares.

The exact dual cone is

    K*={0} union {B positive definite: tr B tr B^-1<=49}. (1)

For each nonzero B in this cone, define ell_B(F)=tr(BC) when Delta F=x^T Cx. This linear functional on all homogeneous quartics is a positive weighted sum of at most24 point evaluations. The points need not be on the unit sphere; the weights are not required to sum to1. The feasible cone is closed and convex as a consequence of the test characterization, not as an assumption in its proof.

## 2. Elementary nonnegative Gram factorization

We first prove a finite matrix lemma. Every real symmetric positive semidefinite three-by-three matrix M with positive diagonal and nonnegative entries can be written M=L L^T with L entrywise nonnegative and three columns.

Scale by the positive diagonal square roots to reduce to a positive semidefinite R with diagonal1. Its off-diagonal entries lie in [0,1], by the two-by-two principal minors. Permute coordinates so that a=R12 is one of their smallest values; write b=R13 and d=R23. If a=1, all entries equal1 and a single all-one column suffices, with two zero columns. If a<1, set

    L0=[1, 0, 0;
        a, sqrt(1-a^2), 0;
        b, (d-ab)/sqrt(1-a^2), sqrt(det R/(1-a^2))].   (2)

Every entry is nonnegative: d>=a and b<=1 give d-ab>=0, and det R>=0. Expansion gives

    det R=(1-a^2)(1-b^2)-(d-ab)^2.

This verifies the last row norm in L0 L0^T, while the other five entries are immediate. Thus L0 L0^T=R, including det R=0. Undo the positive diagonal scaling and row permutation to obtain L. The proof handles singular matrices without dividing by their determinant.

## 3. Moment matrix and exact spectral condition

Diagonalize B=O diag(b_i) O^T. Initially work in these coordinates. The functional on the fifteen quartic monomials has the values

    ell_B(x_i^4)=12b_i,
    ell_B(x_i^2 x_j^2)=2(b_i+b_j), i!=j,
    ell_B(x^alpha)=0 if any alpha_i is odd.           (3)

For the last assertion, differentiating twice leaves a mixed quadratic or zero whenever an odd exponent occurs; the diagonal trace pairing kills every mixed quadratic.

Let M have diagonal12b_i and off-diagonal2(b_i+b_j). For q=sum a_i x_i^2, (3) gives ell_B(q^2)=a^T M a. When b_i>0, put u_i=b_i^(-1/2), v_i=b_i^(1/2) and kappa=||u|| ||v||. Then

    diag(b)^(-1/2)(M/4)diag(b)^(-1/2)
                    =2I+(uv^T+vu^T)/2.               (4)

Here u.v=3. The rank-at-most-two perturbation has eigenvalues (3+kappa)/2 and (3-kappa)/2 on its span, and zero perpendicular to that span. Adding2 gives the eigenvalues 2,(7+kappa)/2,(7-kappa)/2. If u and v are parallel, the actual list is5,2,2, which agrees with kappa=3. Thus

    M positive semidefinite iff kappa<=7
                  iff (sum b_i)(sum 1/b_i)<=49.       (5)

This is a congruence argument, so it establishes positivity even though it does not identify M's own eigenvalues.

## 4. Atomic representation and the complete dual

For positive b satisfying (5), every entry of M is positive. Apply Section2 to write M=L L^T with L>=0. For each column k and sign vector epsilon in {-1,1}^3 define

    z_(k,epsilon),i=epsilon_i sqrt(L_ik).

Then the functional

    T(F)=(1/8) sum_(k=1)^3 sum_epsilon F(z_(k,epsilon)) (6)

kills all odd-exponent monomials by sign cancellation. Its value on x_i^4 is sum_k L_ik^2=M_ii, and its value on x_i^2 x_j^2 is sum_k L_ik L_jk=M_ij. By (3), T=ell_B on the full fifteen-dimensional quartic space. In the original coordinates use the points O z_(k,epsilon): the Laplacian commutes with the orthogonal change of variables. Thus ell_B is nonnegative on every F>=0. This proves the inclusion in K* of every matrix on the right side of (1).

Conversely, if B is dual, the tests x_i^4 in its eigenbasis give b_i>=0. If b_i=0 and b_j>0, use the nonnegative square F=(x_j^2-4x_i^2)^2. Formula (3) gives ell_B(F)=12b_j-16b_j=-4b_j<0, impossible. Every nonzero dual B is therefore positive definite. If (5) fails, M has a negative quadratic direction a and the test (sum a_i x_i^2)^2 contradicts duality. This proves (1) completely, including zero and the exclusion of all nonzero singular matrices.

No representation theorem for general nonnegative polynomials was used. The square tests only exclude invalid dual matrices; the positive atomic formula proves validity on arbitrary nonnegative quartics.

## 5. Exact normalized minimum

It remains to prove directly that the dual tests are sufficient for membership in K. The set D is compact: each eigenvalue lies in [1/49,1], its trace is1, and the inverse trace is continuous there. It is nonempty because I/3 is admissible.

For fixed eigenvalues of B, minimize tr(BC) on its compact orthogonal orbit. Varying by exp(tS), with S skew-symmetric, gives tr(S[B,C])=0. Setting S=[B,C] gives minus its squared Frobenius norm, hence the minimizer commutes with C. Therefore the minimum over D is the minimum of sum b_i c_i over positive b with sum b_i=1 and sum1/b_i<=49, where c_i are the eigenvalues of C and every permutation is allowed.

If C=lambda I this minimum is lambda. Otherwise define Z_+=sum sqrt(c_i+mu) and Z_-=sum(c_i+mu)^(-1/2) for mu>-min c_i. Their product decreases strictly from infinity to9, since

    2(Z_+Z_-)'=Z_-^2-Z_+ sum(c_i+mu)^(-3/2)<0

by Cauchy-Schwarz, with equality excluded by nonconstant c. Thus exactly one mu gives Z_+Z_-=49. Set

    b_i=1/[Z_-sqrt(c_i+mu)], nu=1/Z_-^2,
    m=49nu-mu.                                       (7)

These b are admissible with inverse sum49. For any other admissible beta, Cauchy-Schwarz gives sum(c_i+mu)beta_i>=Z_+^2/(sum1/beta_i)>=49nu. Equality holds at b, so m is exactly min_D tr(BC). Repeated eigenvalues are allowed. The matrix B=(C+mu I)^(-1/2)/Z_- is unambiguous.

## 6. Constructive sufficiency and closedness

For scalar C=lambda I, the test with I/3 forces lambda>=0. Then F=lambda|x|^4/20 is nonnegative and has the desired Laplacian. For nonscalar C use the minimizing B,nu,m from (7). The hypothesis of nonnegative dual tests gives m>=0. Put A=B^-1-7I. Then

    tr A=28, C=mI+nu(B^-2-49I),
    F=(nu/8)(x^T A x)^2+(m/20)|x|^4.                 (8)

Direct differentiation gives Delta(x^T A x)^2=x^T(8A^2+4tr(A)A)x. Since tr A=28, the bracket is8(B^-2-49I). Also Delta|x|^4=20|x|^2 in dimension3. Therefore Delta F=x^T Cx exactly, and m>=0 makes (8) nonnegative. It is the sum of the two quadratic squares with factors sqrt(nu/8) and sqrt(m/20); a zero factor may be omitted. For m>0 it is bounded below by (m/20)|x|^4, and for m=0 it is one square.

This proves sufficiency constructively. Necessity was proved by (6), so K equals the intersection of the closed half-spaces tr(BC)>=0 indexed by B in D. Hence K is closed and convex. There was no appeal to cone separation or closedness of a linear image.

## 7. Polynomial pressure consequence and limits

For a real solenoidal homogeneous quadratic Q and E=|Q|^2, define C_gamma by

    x^T C_gamma x=-tr((DQ)^2)-gamma Delta E.

The substitution F=R-gamma E proves that a homogeneous quartic R with -Delta R=tr((DQ)^2) and R>=gamma E exists exactly when C_gamma passes the dual tests. Formula (8), or the scalar formula, constructs R=gamma E+F. No harmonic quartic adjustment is excluded.

This theorem improves the dependency list of the earlier cone proof. It is not a new proof that arbitrary nonnegative quartics have two-square representations, does not evaluate the optimum over all Q, and supplies no pressure premise for a genuine Euler profile. A nonzero Q grows quadratically and is not a decaying profile. The full momentum equation remains an additional condition.

## 8. Verification record

All seven source sections and all fifty-one source-check entries were read. The reported final check duration is0.320908seconds; checks were not rerun. They cover two explicit interior atomic lists, every quartic monomial for each, a singular Gram factor, the all-one case, and the singular-dual separating square. The complete proof of general positivity is Sections2-4, not those selected examples.

The dependencies are finite-dimensional real symmetric diagonalization, compactness, elementary differentiation, Cauchy-Schwarz and the intermediate value theorem. No Hilbert theorem, general completely-positive-matrix theorem, sum-of-squares classification, cone separation, numerical optimization or earlier pending result is needed. The existing coordinator comparison is addressed in Section9.

## 9. Existing model comparison and independent response

All four items and W1-W4 of the coordinator comparison dated02:44Z were read, together with all nineteen existing log entries. The source hash matches the archived submission. The algebraic factorization, fifteen monomial moments, singular-dual exclusion and orbit variation agree with Sections2-5. The sampled matrices and rotated numerical identities were not rerun and are not needed for the general proof.

W1 is correct: homogeneity of degree4 makes F(-z)=F(z), so pairing each sign vector with its negative reduces the bound to twelve evaluations with weight1/4. The stated bound of twenty-four remains valid. W2 is optional historical context; no general theorem on completely positive matrices is imported. For W3, at the minimizing B the vector a_i=1/b_i-7 satisfies Ma=0. Each column L_k is then orthogonal to a because a^TMa=sum_k(a^TL_k)^2=0. Thus x^TAx=0 at every atom, and F_C there equals (m/20)|x|^4. Some atom is nonzero since every M_ii>0, so there exists a negative atom exactly when m<0. Zero columns may give zero atoms and are harmless. W4 accurately distinguishes this elementary proof from the earlier Hilbert-dependent proof.

The existing coordinator is configured as model; actual provider execution is not independently attested. This exchange used only the existing shared files. No new client or agent was launched. The full proof is independent of all supplementary floating checks.

## 10. Source confirmation revision

The revised LIT334 source records A2805 and the open application boundary A2807. Its new comparison paragraph correctly uses antipodal symmetry for twelve weighted evaluations, the null direction Ma=0 for the synthesis square, and at least one nonzero atom because the moment matrix has positive diagonal. The wording handles zero columns of the factor correctly. It asserts existence of some two-square preimage, not a two-square representation of every nonnegative quartic. All changed lines were read; no original proof equation changes.

The exact revised-source hash and the complete delta are retained in the team records and in the team records. No new mathematical computation was run.

## 11. Repeated dependency audit for the one-eighth bound

The full ten-section proof and the complete original coordinator comparison were reread after the one-eighth theorem was confirmed. The polynomial bound uses only the positive-functional direction from Sections 2 to 4. For positive eigenvalues b_i, the moment matrix has diagonal 12b_i and off-diagonal 2(b_i+b_j). Its normalized congruence is 2I+(uv^T+vu^T)/2 with u.v=3, so positivity follows exactly from ||u||||v||<=7. The entrywise nonnegative Gram factor then yields the finite positive evaluation formula on every homogeneous quartic. This covers nonnegative quartics regardless of whether a particular square representation has been chosen.

The singular factor cases were checked again: det R=0 causes no division by the determinant, and a=1 forces the all-one matrix. The atom formula remains valid with zero columns. In the separate synthesis direction, the endpoint mu approaches minus the smallest c_i and the product Z_+Z_- diverges for every nonscalar C, including repeated smallest eigenvalues; at infinity it tends to 9. The strict derivative inequality excludes any second root. The Cauchy-Schwarz minimization and the explicit square preimage therefore have no missing spectral multiplicity case.

This confirms that the one-eighth proof imports no unverified general theorem about nonnegative polynomials, no cone-separation assumption and no numerical search. Its strict functional is obtained by applying this result to B-I/300 and adding a positive multiple of the spherical mean. The theorem concerns homogeneous polynomial data, not a decaying Euler profile. Rotation does not enter this finite-dimensional lemma; no missing pressure hypothesis for actual profiles is supplied by it. This repeated audit used no new computation.
