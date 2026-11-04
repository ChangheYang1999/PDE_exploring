# Boundary uniqueness for quartic Laplacians and optimal polynomial pressure

Status: independent reconstruction and existing Theory Agent C  model comparison complete. Sections 2-5 prove the equality theorem directly. Section 6 names the additional cone characterization used for the boundary corollaries.

## 1. Statements and notation

Let Sym3 be the real symmetric three-by-three matrices, with pairing tr(BC). Let K contain those C for which a nonnegative real homogeneous quartic F on R3 has Delta F(x)=x^T Cx. For B positive definite with tr B=1 and tr B^-1=49, put A=B^-1-7I. If F>=0 and tr(BC)=0, then

    F(x)=kappa (x^T A x)^2

for exactly one real kappa>=0. The equality theorem does not assume a sum-of-squares representation of F. The exposed face of K at B is a single positive ray, and a member of this face has a unique nonnegative quartic preimage.

Using the exact cone characterization reconstructed in the separate elementary-cone audit, every nonzero boundary C of K has a unique such preimage. Moreover, the sum of two nonzero elements of K on different positive rays is in the interior of K.

For every nonzero real homogeneous quadratic vector polynomial Q with div Q=0, put E=|Q|^2. If there is at least one real gamma and homogeneous quartic R with -Delta R=tr((DQ)^2) and R>=gamma E, the supremum gamma_Q of these gamma is finite and attained. Its quartic pressure R is unique. The surplus R-gamma_Q E is either zero or a single quadratic square of the displayed form. These are polynomial Poisson assertions, not existence assertions for the full Euler equation.

## 2. Boundary moment matrix

Work in an orthonormal eigenbasis of B, with eigenvalues b_i. Set a_i=1/b_i-7 and q(x)=sum a_i x_i^2. Then

    sum a_i=28,    sum b_i a_i=-4.

The a_i have both signs. If all were nonpositive, their sum could not be 28. If all were nonnegative, the negative weighted sum would be impossible. Some a_i may be zero, so the quadratic q may have rank two.

For any homogeneous quartic G define ell_B(G)=tr(B C_G), where Delta G=x^T C_G x. Direct differentiation gives

    ell_B(x_i^4)=12b_i,
    ell_B(x_i^2 x_j^2)=2(b_i+b_j),
    ell_B(x^alpha)=0 if any exponent in alpha is odd.

Let M have the first values on its diagonal and the second values off the diagonal. Then M a=0. Indeed M=8diag(b)+2(b 1^T+1 b^T), so its i-th product entry is 8b_i(1/b_i-7)+56b_i-8=0.

Congruence of M/4 by diag(b)^(-1/2) gives 2I+(uv^T+vu^T)/2, where u_i=1/sqrt(b_i), v_i=sqrt(b_i), u.v=3 and |u||v|=7. Its eigenvalues are 2,7,0. Therefore M is positive semidefinite of rank two, its kernel is span(a), and its range is a-perpendicular. These are eigenvalues of the congruent matrix, not assertions about M's own eigenvalues. Every entry of M is strictly positive.

## 3. Positive moment insertion

We need an elementary factorization. Any positive semidefinite symmetric three-by-three matrix N with positive diagonal and nonnegative entries is L L^T for an entrywise nonnegative L with three columns. Normalize the diagonal to one. Permute so r=R12 is a smallest off-diagonal entry, and set s=R13,t=R23. Principal minors give r,s,t in [0,1]. If r=1, R is the all-one matrix. Otherwise the three rows

    (1,0,0),
    (r,sqrt(1-r^2),0),
    (s,(t-rs)/sqrt(1-r^2),sqrt(det R/(1-r^2)))

form a nonnegative square root in the sense L L^T=R. Here t>=r>=rs and det R=(1-r^2)(1-s^2)-(t-rs)^2. Undo the scaling and permutation. This also covers determinant zero.

For each column k of L, average evaluations at the eight points with coordinates epsilon_i sqrt(L_ik), epsilon_i in {-1,1}, using weight 1/8. Summing over k defines T_N. Its values on the fifteen quartic monomials are N_ii for x_i^4, N_ij for x_i^2 x_j^2, and zero for the odd monomials. Thus T_N depends linearly on N, irrespective of the chosen factor, and is nonnegative on every nonnegative G. In particular ell_B=T_M.

Take any w with all w_i>0 and a.w=0. If lambda>0 is the smallest eigenvalue of M on a-perpendicular, then for 0<epsilon<lambda/|w|^2 the matrix N=M-epsilon w w^T remains positive semidefinite. Reduce epsilon further so epsilon w_i w_j<M_ij for all i,j. Now N has positive entries and admits the above factorization. The rank-one matrix w w^T itself corresponds to the eight-point sign average at coordinates sqrt(w_i). Consequently

    ell_B(F)=T_N(F)+(epsilon/8) sum_eta F(eta_i sqrt(w_i)).

Every summand is nonnegative. If ell_B(F)=0, each displayed value is zero. For any x with all coordinates nonzero and q(x)=0, choosing w_i=x_i^2 therefore proves F(x)=0. This conclusion covers the entire indicated part of the real quadratic cone, not just a finite collection of atoms from one factorization.

## 4. Divisibility, including the reducible case

Choose a nonzero coefficient a3 so that at least one of a1,a2 has the opposite sign. Divide any real polynomial G by the monic polynomial q/a3 in the variable x3, over R[x1,x2]. Absorbing the nonzero constant a3 into the quotient gives

    G=q H+R1(x1,x2)x3+R0(x1,x2).

There is a nonempty open set of pairs (x1,x2) with x1 x2 nonzero and h=-(a1 x1^2+a2 x2^2)/a3>0. This follows by making the coordinate of the opposite-sign coefficient dominate, while keeping both coordinates nonzero. The two cone points x3=plus or minus sqrt(h) then have every coordinate nonzero. If G vanishes on those points, its two remainder equations give R0=R1=0 on that open set. A real polynomial vanishing on an open set is identically zero, so q divides G.

Apply this to F. Homogeneity gives F=q H with H homogeneous quadratic. At any cone point with every coordinate nonzero, grad q is nonzero because at least one a_i is nonzero. The implicit linear variation in the gradient direction makes q take both signs arbitrarily close to that point. If H were nonzero there, continuity would keep its sign fixed nearby and qH would be negative on one side. Nonnegativity of F therefore forces H to vanish on the same part of the cone. Applying the division argument again yields H=kappa q, where kappa is constant. Since q is not the zero polynomial, F>=0 implies kappa>=0, and q^2 being nonzero makes kappa unique.

The argument does not use irreducibility. In particular, when one a_i=0, the real cone is reducible but the same open set, division and sign argument apply to both branches. Orthogonal invariance returns the formula F=kappa(x^T A x)^2 in the original coordinates.

## 5. Exposed ray and uniqueness for its Laplacian

Direct differentiation gives

    Delta(x^T A x)^2=x^T L(A)x,
    L(A)=8A^2+4(tr A)A.

Its trace is 8|A|_F^2+4(tr A)^2>0, since tr A=28. Thus the preceding theorem forces C=kappa L(A), and kappa=tr C/tr L(A). Every kappa>=0 is realized. If a second nonnegative quartic has the same C, it has the same zero pairing with B, so it has the same kappa and is identical. This proves the exposed-ray and preimage assertions without any cone-classification input.

## 6. All boundary points and strict convexity in the stated sense

This section uses the elementary cone characterization reconstructed in auditor_proofs/reviews/elementary_quartic_cone_20261104/PROOF.md: K={C:tr(BC)>=0 for every B in D}, where D={B>0:tr B=1,tr B^-1<=49}. It also uses the scalar minimizer proved there. These results are now independently CONFIRMED in A2805; they are explicit additional dependencies of this section.

The set D is compact. If C lies on the boundary of K, its minimum pairing over D is zero: a positive minimum would persist under sufficiently small perturbations of C, making C interior. For a nonzero boundary C, the scalar case is impossible. A scalar lambda I with lambda>0 has positive minimum; lambda=0 is zero, and lambda<0 fails a test. Therefore C is nonscalar. The scalar-minimum formula supplies a minimizing B with tr B^-1=49. Section 5 now gives its unique nonnegative quartic preimage.

For completeness, every nonzero feasible C has positive trace. If F>=0 and Delta F=x^T Cx, sphere averaging gives mean F=tr C/60. A nonzero homogeneous nonnegative polynomial has positive mean. If C=0 this argument makes every such F zero, so a nonzero C necessarily has positive trace.

If two nonzero feasible C1,C2 have a boundary sum, the minimizing B pairs to zero with the sum and nonnegatively with each summand. Both pairings are zero. Section 5 puts both on the same positive ray. Their sum cannot be zero by the trace argument. Consequently two nonzero feasible matrices on distinct positive rays have an interior sum. This is the precise asserted strict-convexity property; no claim is made about a strictly convex norm or boundary smoothness.

## 7. Fixed-Q pressure optimum

Write -tr((DQ)^2)=x^T Nx. Sphere averaging gives mean R=tr N/60 for every quartic Poisson pressure. The number mean E is positive because Q is nonzero. Hence every feasible gamma satisfies

    gamma <= tr N/(60 mean E).

The nonempty feasible set therefore has a finite real supremum gamma_Q. Choose feasible gamma_n tending to it, and set F_n=R_n-gamma_n E>=0. Their sphere means are tr N/60-gamma_n mean E and are bounded. The integral of the absolute value on the unit sphere is a norm on the finite-dimensional space of homogeneous quartics. Its minimum on the Euclidean coefficient unit sphere is positive by compactness: a continuous polynomial with zero absolute integral vanishes on the sphere and, by homogeneity, identically. Thus the means of these nonnegative F_n bound all their coefficients. A subsequence converges to F>=0 with the limiting Laplacian. Setting R=gamma_Q E+F proves attainment. No cone theorem is needed for this compactness argument.

The matrix C_gamma=N-gamma D_E, where Delta E=x^T D_E x, depends continuously on gamma. At gamma_Q it cannot be interior to K, because a small positive increase of gamma would remain feasible by the cone characterization. If C_gamma_Q=0, the nonnegative harmonic quartic F has zero sphere mean and is zero. If it is a nonzero boundary point, Section 6 gives its unique preimage, which Section 5 expresses as kappa(x^T A x)^2. This proves uniqueness of R and the surplus formula in both cases.

If a pair attains the unrestricted optimum over all normalized Q, its R must already be optimal for that fixed Q, or the unrestricted value could be improved. The same surplus conclusion therefore applies, without evaluating that unrestricted optimum.

## 8. Evidence and scope

All seven submitted source sections were read. This proof is an independent reconstruction of the rank-two moment kernel, positive insertion at every nonzero-coordinate null-cone point, two division steps, exposed ray, boundary criterion and compactness argument. No numerical computation or supplementary check is used. The complete existing Theory Agent C  hand comparison has now been read; the additional coordinator comparison is checked in Section 10.

The full momentum equation and a global pressure inequality for an actual decaying Euler profile are not consequences of these polynomial statements. A nonzero homogeneous quadratic Q grows and is outside the decaying class. No value of Gamma_2, no decaying example and no resolution of the arbitrary-omega conjecture is asserted.

## 9. Existing model comparison

The Theory Agent C  note dated 2026-11-04 02:56Z was read in full. Its six substantive checks agree with the reconstruction: the moment-kernel calculation and congruent eigenvalues, linearity of the atomic functional, insertion at every positive-coordinate moment, two polynomial divisions including the rank-two case, the trace/mean identity and boundary minimizer, and compactness plus the fixed-Q optimum argument. The particular axial surplus is consistent with the earlier fixed-field certificate; no decimal approximation is a dependency here.

The note reports numerical checks with a root-finder tolerance and a Monte Carlo mean. Those logs were not read or rerun and do not certify the theorem. The comparison is useful for its explicit hand arguments. The C agent is configured as model; actual provider execution is not independently attested. This exchange uses existing files only and launches no new model client or agent. The additional coordinator comparison is checked in Section 10.


## 10. Coordinator follow-up and the exact averaging bound

All five coordinator items, W1-W3 and all 25 supplementary log entries were read. They agree with Sections 2-7. In W1 the nonscalar boundary formula from A2806 is indeed the unique quartic. If the optimal surplus is zero, the separate scalar zero case in Section 7 applies; no nonzero A or coefficient is forced. The boundary test in any report summary must retain B>0, tr B=1 and tr B^-1=49. All changed source lines at hash d952989fb3c0f7696d36ec0a616ff6b3e3ceec2587db06552749df81c2b2e2c4 were read. The proof equations are unchanged, and A2805 is now an explicit confirmed dependency. All 34 source-check entries and the recorded earlier failed test were read. A zero proper minor in the rank-two case is consistent with positive semidefiniteness; the failed strict-minor test did not refute the proof. Neither set of checks was rerun.

Here is an exact elementary resolution of W2, independent of a floating-point eigenvalue computation. For any nonzero homogeneous quadratic divergence-free Q and any quartic R with -Delta R=tr((DQ)^2), put

    e0 = mean |Q(n)|^2,  v0 = mean (Q(n).n)^2,  p0 = mean R(n),

where mean denotes normalized surface measure on the unit sphere. The tensor S=Q tensor Q+R I satisfies div div S=0. To verify the spherical identity without a boundary assumption at infinity, let n=x/|x| and A(r)=mean n.S(rn)n. The flux of div S across every sphere is zero by the divergence theorem on the enclosed ball. Since

    div(S n)=(div S).n+(tr S-n.S n)/r,

integration over a ball and differentiation with respect to its radius give

    r A'(r)=mean tr S(rn)-3 A(r)=e(r)-3v(r).

All fields are polynomials, so these operations are classical, and the origin contributes no flux. Homogeneity gives A=r^4(v0+p0), e=r^4 e0 and v=r^4 v0. Consequently

    4p0=e0-7v0,
    tr N/(60 mean E)=p0/e0=1/4-7v0/(4e0) <= 1/4.

Equality holds exactly when Q(x).x=0 identically. Indeed v0 is the mean of a continuous nonnegative square. The tangential fields are exactly Q=x cross Mx with M real symmetric, modulo adding a scalar multiple of I. To see necessity, the identity

    x cross curl Q = grad(x.Q)-Q-(x.grad)Q = -3Q

writes Q in this form with M=-curl(Q)/3 as a linear map. The equation div Q=0 forces the skew part of M to vanish, because div(x cross Mx)=-x.curl(Mx). Sufficiency follows from these same identities. The kernel of M -> x cross Mx consists exactly of scalar matrices: Mx parallel to x for every x forces one common eigenvalue by considering sums of basis vectors. This is a five-dimensional space.

The Theory Agent C  03:01 note correctly identifies this five-dimensional equality space for the averaging quotient. Its sentence that the bound gamma_Q<=1/4 is attained there must not be read literally as attainment of gamma_Q=1/4. The optimal pressure coefficient is strictly smaller. In fact, if R>=E/4, the displayed mean identity first forces v0=0 and then R=E/4. Diagonalizing the symmetric M gives Q=(a yz,b xz,d xy), a+b+d=0. The three coefficients in -Delta(E/4)=tr((DQ)^2) require

    a^2=-2bd,  b^2=-2ad,  d^2=-2ab.

For example the x^2 equation is -(b^2+d^2)/2=2bd; replacing b+d by -a gives a^2=-2bd. Multiplying the three equations gives (abd)^2=-8(abd)^2, so abd=0 and all three coefficients vanish. This contradicts Q nonzero. Since Section 7 proves fixed-Q attainment, every nonempty fixed-Q optimum satisfies gamma_Q<1/4. The averaging quotient attains 1/4; gamma_Q does not. The Theory Agent C  note itself gives the smaller axial optimum, consistent with this correction. Its additional eigenvalues and representation-theoretic multiplicities are not audited here.

The existing coordinator and C agents are configured as model; their actual provider execution is not independently attested. The follow-up uses existing files only. It supplies no pressure premise for a decaying Euler profile.
