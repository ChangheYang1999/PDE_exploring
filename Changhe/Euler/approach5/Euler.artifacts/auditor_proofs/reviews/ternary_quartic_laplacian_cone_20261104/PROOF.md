# The Laplacian cone of nonnegative ternary quartics

Status: CONFIRMED at A2790-A2792, with the application boundary OPEN at A2793. The external Hilbert theorem and its source boundary are explicit below.

## 1. Exact result and notation

Let Sym3 be the real symmetric three-by-three matrices with inner product tr(BC). Define K to be the set of C in Sym3 for which some real homogeneous quartic F on R3 satisfies

    F>=0,    Delta F(x)=x^T Cx.

The zero polynomial is allowed. Then K is a closed convex cone and

    K*={0} union {B positive definite: tr(B)tr(B^-1)<=49}.       (1)

Consequently C belongs to K exactly when

    tr(BC)>=0 for every B positive definite with
    tr B=1 and tr(B^-1)<=49.                                 (2)

If c1,c2,c3 are the eigenvalues of C in any order, this is equivalent to

    sum_i b_i c_i>=0 for all positive b_i with
    sum_i b_i=1 and sum_i 1/b_i<=49.                          (3)

The test set in (3) is compact. Membership implies tr C>=0; if C belongs to K and tr C=0, then C=0 and every nonnegative quartic preimage F is zero.

The proof uses Hilbert's theorem that every nonnegative real homogeneous ternary quartic is the sum of three squares of real homogeneous quadratics. This is an explicit established external theorem. It is not a claim that arbitrary nonnegative polynomials admit such a representation.

## 2. Primary source and the singular-case limit

The actual four-page article by Powers, Reznick, Scheiderer and Sottile, A new approach to Hilbert's theorem on ternary quartics, C. R. Acad. Sci. Paris, Ser. I339 (2004), pages617-620, DOI10.1016/j.crma.2004.09.014, was read in full from its retained PDF text. Its introduction states the general Hilbert theorem. Its numbered Theorem1.1 assumes that the complex plane quartic is smooth and describes eight equivalence classes of representations. This smoothness hypothesis is not omitted here. The article's Riemann-Roch, Galois-cohomology, Witt and Weichold inputs are external; this audit does not reprove them or claim an independent algebraic-geometric certification of the article.

The singular case can be recovered from the smooth existence statement as follows. For F>=0 put G=x1^4+x2^4+x3^4 and F_epsilon=F+epsilon G. For epsilon>0 the new form is positive away from zero. The complex projective curve defined by G is smooth: its three partial derivatives vanish simultaneously only at the origin. The discriminant of F+epsilon G is a nonzero polynomial in epsilon, with nonzero highest coefficient equal to the discriminant of G. This uses the standard homogeneous-discriminant property, namely that its zero set is the singular plane quartics. Only finitely many epsilon are exceptional.

Choose positive epsilon_n tending to zero outside that finite set. The smooth theorem supplies F_epsilon_n=sum_(j=1)^3 (x^T A_jn x)^2 with real symmetric A_jn. Section3's trace identity bounds these three matrices uniformly because Delta F_epsilon_n converges coefficientwise. A convergent subsequence of the triples gives F=sum_(j=1)^3 (x^T A_j x)^2. Thus the limiting extension is justified without assuming that an arbitrary linear image of a closed cone is closed. Alternatively the general Hilbert statement in the source introduction is precisely the external theorem needed in Section3.

## 3. The square map, convexity and closedness

For A in Sym3, q_A=x^T Ax satisfies grad q_A=2Ax and Delta q_A=2tr A. The product rule gives

    Delta(q_A^2)=x^T L(A)x,
    L(A)=8A^2+4(tr A)A,
    tr L(A)=8||A||_F^2+4(tr A)^2.                            (4)

Hilbert's theorem gives the equivalence

    C in K iff C=L(A1)+L(A2)+L(A3).                          (5)

Zero matrices may be used for unused summands. The reverse implication follows directly by summing the three squares.

Convexity and closure under nonnegative scaling follow by adding or scaling the nonnegative preimage quartics. For topological closedness, let C_n in K tend to C and choose triples in (5). Taking traces gives

    8 sum_j ||A_jn||_F^2<=tr C_n.

The right side is bounded and nonnegative. A subsequence of the triples converges in a fixed finite-dimensional vector space. The polynomial map L is continuous, so its limit represents C as in (5). This proves closedness. If tr C=0, (4) forces every matrix in such a representation to vanish; applying the same argument to any nonnegative preimage proves the asserted uniqueness of the zero quartic.

With normalized sphere measure, mean_S2 F=tr C/60. Indeed, the polar-coordinate Laplacian of a degree-four homogeneous function restricts to 20F+Delta_S2 F on the unit sphere. The integral of the spherical Laplacian is zero, while mean_S2(x^T Cx)=tr C/3. This also gives a direct proof of the trace-zero conclusion for continuous nonnegative F.

## 4. Complete dual calculation

By (4)-(5), B lies in K* exactly when

    2tr(BA^2)+(tr A)tr(BA)>=0 for every A in Sym3.             (6)

Diagonalize B orthogonally, with eigenvalues b_i. Write a_i=A_ii. The left side of (6) is

    a^T D a+2 sum_(i<j)(b_i+b_j)A_ij^2,
    D=2diag(b)+(1 b^T+b 1^T)/2.                             (7)

To verify the split, tr(BA^2)=sum_i b_i a_i^2+sum_(i<j)(b_i+b_j)A_ij^2, and (tr A)tr(BA)=(sum_i a_i)(sum_i b_i a_i).

The diagonal entries D_ii=3b_i show that each b_i must be nonnegative. If one is zero and another is positive, the corresponding principal submatrix is [[0,b_j/2],[b_j/2,3b_j]], which has negative determinant. Thus every nonzero dual matrix is positive definite.

For b_i>0 the off-diagonal terms of (7) are positive, so (6) is equivalent to D being positive semidefinite. Congruence by diag(b_i^-1/2) gives

    2I+(u v^T+v u^T)/2,
    u_i=b_i^-1/2, v_i=b_i^1/2, u.v=3.                      (8)

Set kappa=||u|| ||v||. On span(u,v), the rank-at-most-two perturbation has eigenvalues (3+kappa)/2 and (3-kappa)/2, as is verified by applying it to u/||u|| plus or minus v/||v||. It vanishes on the orthogonal complement. When u and v are dependent, all b_i are equal, kappa=3, and the complete list remains valid with multiplicity by choosing perpendicular vectors. Hence the eigenvalues of (8) are

    2, (7+kappa)/2, (7-kappa)/2.

Positivity is exactly kappa<=7. Since kappa^2=(sum b_i)(sum 1/b_i), this proves (1), including equality and the zero matrix.

## 5. Separation, eigenvalue testing and compactness

The finite-dimensional separating-hyperplane theorem applies because K is a nonempty closed convex cone. It gives K=(K*)*. Scaling a nonzero dual matrix to trace one proves (2).

It remains to justify testing only commuting B without assuming that an arbitrary pair commutes. Fix positive eigenvalues b and minimize tr(O diag(b) O^T C) over the compact orthogonal group. Let B0 attain the minimum. For every skew-symmetric S, varying along exp(tS) gives

    tr(S[B0,C])=0.

The commutator is skew-symmetric; take S=[B0,C]. For a real skew-symmetric matrix K0, tr(K0^2)=-||K0||_F^2. Therefore B0 commutes with C. Two commuting real symmetric matrices admit a simultaneous orthogonal diagonalization. The minimum is accordingly sum_i b_i c_i for some ordering of the b_i. The quantifier in (3) includes every such ordering, proving sufficiency. Necessity follows by taking B diagonal in an eigenbasis of C.

Each positive normalized b in (3) has 1/b_i<=49, so b_i>=1/49. The test set is closed inside [1/49,1]^3 and is bounded. It is nonempty because b_i=1/3 gives reciprocal sum9. This proves compactness. In particular I/3 is an admissible dual test and gives tr C>=0.

## 6. Exact pressure-feasibility equivalence

Let Q:R3->R3 be a real homogeneous quadratic vector polynomial with div Q=0, and write E=|Q|^2. For any real gamma define the unique symmetric C_gamma by

    x^T C_gamma x=-tr((DQ(x))^2)-gamma Delta E(x).           (9)

There exists a real homogeneous quartic R such that

    -Delta R=tr((DQ)^2),    R>=gamma E everywhere            (10)

if and only if C_gamma passes (2), or equivalently (3). The proof is the exact substitution F=R-gamma E. It converts (10) into the defining conditions of K and is reversed by R=F+gamma E. Thus every harmonic quartic pressure adjustment is included; no symmetry assumption on R is introduced.

With the normalization mean_S2|Q|^2=1, the existing Gamma_2 is equivalently the supremum of gamma over such Q for which C_gamma passes the compact test. This is a reformulation, not an evaluation. Neither the stationary momentum equation nor the full similarity equation follows from (10), and no pressure lower bound for a genuine global profile is obtained.

## 7. Fixed axial swirl

For Q=(-x2 x3,x1 x3,0), direct differentiation gives

    E=(x1^2+x2^2)x3^2,
    tr((DQ)^2)=-2x3^2,
    Delta E=2(x1^2+x2^2)+4x3^2,
    C_gamma=diag(-2gamma,-2gamma,2-4gamma).                 (11)

The matrix C_gamma commutes with rotations around the third axis. Averaging any admissible nonzero B in K* over these rotations preserves its pairing with C_gamma and preserves dual membership, since the dual inequalities (6) are linear in B. The average is diag(a,a,b) with a,b>0. Thus all tests reduce exactly to these axial matrices, not merely to a subset of necessary tests.

Scale b to1 and put t=a/b. The dual condition becomes

    (2t+1)(2/t+1)<=49,
    t+1/t<=22,
    11-2sqrt(30)<=t<=11+2sqrt(30).                         (12)

The pairing is 2-4gamma(t+1). For gamma>=0 its minimum occurs at the largest allowed t. Consequently pressure feasibility is exactly

    0<=gamma<=1/[2(12+2sqrt(30))]=(6-sqrt(30))/24.          (13)

At gamma=0 one can also exhibit R=x3^4/6 directly; it is nonnegative and has Delta R=2x3^2. The same R works for all negative gamma because E>=0. Thus the complete feasible range for this Q is gamma<=(6-sqrt(30))/24. No axial symmetry was imposed on the pressure, and the constant agrees with the earlier independently confirmed fixed-Q result.

## 8. Evidence and remaining scope

All seven source sections and all sixteen exact-check entries were read. The four-page primary-source text was read through its references. The source checks were not rerun. No mathematical computation is needed for the direct proof above; the recorded algebra checks cannot prove Hilbert's theorem, separation, an optimization over all Q, or a global Euler hypothesis.

The non-elementary external input is Hilbert's ternary-quartic theorem, with the source and smoothness boundary explained in Section2. The remaining inputs are finite-dimensional separation, real symmetric diagonalization, compactness, and polynomial differentiation. The optional singular-case derivation additionally uses the standard homogeneous-discriminant property. All constants and dimensions are specific to this setting. The arbitrary-omega decaying Euler conjecture and the exact value of Gamma_2 remain unresolved by this result.

## 9. Existing comparison and designated verdicts

The existing coordinator comparison, dated 2026-11-04T02:30Z, was read in full: all four substantive items and W1-W3. Its nineteen check entries were also read, not rerun. The comparison agrees with Sections1-7. Its one randomly sampled item is supplementary only. In the commutator argument the intermediate trace is minus the squared Frobenius norm; its zero value gives precisely the conclusion in Section5.

W1 is correct: the exact count of three squares may be replaced by the sum-of-squares existence theorem and conic Caratheodory in the six-dimensional matrix space, bounding the number of square maps by six. The present proof retains the simpler three-square statement and its explicit source. W2 is resolved by the previously confirmed attained-maximum result A2699: our supremum formulation defines the same Gamma_2, but normalization by itself does not prove attainment. W3 is an appropriate report scope. The scalar-root reformulation mentioned there is a separate new submission and is not certified by this audit.

A2790 confirms the closed cone, dual and compact eigenvalue test, with the external input recorded in Section2. A2791 confirms the exact quartic-pressure feasibility equivalence. A2792 confirms the complete fixed-axial-field range, allowing every quartic pressure. A2793 leaves both the value of the unrestricted Gamma_2 and the automatic pressure premise for a genuine profile open. No full similarity equation is inferred from a Poisson pair.

Model comparison used the existing coordinator configured as model, through the existing working files; the actual provider execution is independently unattested. No new model client, remote compute or agent was used.


## 10. Source status revision

The complete delta from the archived submission to current source SHA256 88bdb0c90855bf1647cc0aee8cbadf1b00a6d56b2eb79dac0c07bcc414bef635 was read. The revision changes status and adds Section8. The explicit Hilbert dependency remains. The Caratheodory alternative is already checked in Section9 above. The negative-gamma range uses the nonnegative pressure x3^4/6 exactly as in Section7 above, and the Gamma_2 attainment pointer retains its separate dependency.

All added reading-scope statements distinguish this audit from the submitting agent's own reading. The retained delta and hashes are in the team records and in the team records. This revision needs no new mathematical computation.
