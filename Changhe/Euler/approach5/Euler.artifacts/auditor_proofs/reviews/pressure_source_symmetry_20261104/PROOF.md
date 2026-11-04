# Independent review: symmetry of the actual pressure from symmetry of its source

Status: independent reconstruction completed and compared with the existing A and C agents. The pressure theorem is independent of the axisymmetric-pressure rigidity theorem. The Euler corollary uses the exact C2 theorem confirmed in A3029. CONFIRMED in A3040-A3042 at the exact scopes below; stronger conclusions remain OPEN in A3043.

## 1. Exact pressure statement

Let c and omega be arbitrary finite real numbers, J(x1,x2,z)=(-x2,x1,0), and A=cI-omega J. Suppose U in C1(R3;R3) and P in C1(R3) satisfy the full equations

    (1-c)U+((Ay+U).grad)U+omega JU+grad P=0,   div U=0.

Assume E(R)=integral_(B_R)|U|^2=o(R^3). Define the continuous scalar

    q=tr((DU)^2)=sum_(i,j) (partial_j U_i)(partial_i U_j).

For any Q in O(3), if q(Qy)=q(y) for every y, then P(Qy)=P(y) for every y. This holds for reflections as well as rotations. There is no condition QJ=JQ, no pointwise bound on U, no pressure normalization premise and no pressure growth hypothesis.

The standard inputs are distributional product rules, Weyl's lemma, the mean-value property for harmonic functions, and changes of variables in compactly supported integrals. All uses of behavior at infinity are justified by E(R)=o(R^3) below.

## 2. The Poisson equation at the stated regularity

Use G_ij=partial_j U_i. In distributional divergence of the drift term the contribution involving one derivative of Ay is

    sum_(i,j) A_ji G_ij=c div U-omega sum_(i,j) J_ji G_ij.

Divergence of omega JU is omega sum_(i,j) J_ji G_ij, so the skew terms cancel. The remaining drift derivative is (Ay).grad div U=0. Also

    div((U.grad)U)=sum_(i,j) (partial_i U_j)(partial_j U_i)=q.

For C1 fields this last identity follows by convolving locally with a smooth approximation to the identity, using the classical identity for the smoothed divergence-free fields, and passing to the distributional limit. Both first derivatives and the quadratic products converge locally. Consequently

    -Delta P=q.

Orthogonal invariance of the distributional Laplacian implies that h(y)=P(Qy)-P(y) is harmonic when q is Q-invariant. It is initially C1, and Weyl's lemma makes it smooth and harmonic. The problem is to exclude a nonconstant entire harmonic h; Poisson's equation alone would not do so.

## 3. Dilation of the evaluated pressure gradient

Set U_R(z)=U(Rz). For every fixed L>0,

    ||U_R||_(L2(B_L))^2=R^-3 E(LR)=o(1).

Here and below grad P(Rz) is the original y-gradient evaluated at Rz; it is not the z-gradient of P(Rz). Substitute y=Rz in momentum, multiply by a scalar phi in C_c^infinity(R3), and integrate by parts. The result is the vector identity

    integral grad P(Rz) phi
      = integral U_R [(4c-1)phi+(Az).grad phi]
        -omega integral JU_R phi
        +R^-1 integral U_R (U_R.grad phi).                 (1)

The coefficient is -(1-c)+div(Az)=4c-1. The nonlinear sign is positive because div_z U_R=0. A direct check of scales gives (Ay).grad_y U=(Az).grad_z U_R and (U.grad_y)U=R^-1(U_R.grad_z)U_R.

On a support contained in B_L, Cauchy-Schwarz bounds each linear term by a constant times ||U_R||_2, which tends to zero. The nonlinear term is bounded by

    R^-1 ||grad phi||_infinity ||U_R||_(L2(B_L))^2=o(R^-1).

Thus the left side of (1) tends to zero. The same statement holds for a family of translated tests phi(z-x/R), for each fixed x: their supports remain in a common compact ball for R>=1, their derivative norms are fixed, and Az is uniformly bounded on that ball. This uniform test-family estimate is needed in the next section. Ordinary convergence against one fixed test would not by itself justify moving test functions.

## 4. The harmonic increment has zero gradient

Choose radial phi in C_c^infinity(B_1), nonnegative, with integral phi=1. Every component of grad h is harmonic, so its weighted radial mean at any radius reproduces its central value:

    grad h(x)=integral grad h(x+Rz) phi(z) dz.

This follows by writing the radial integral as a weighted integral of spherical averages, each of which equals grad h(x). There is no growth assumption on h, since R is finite at this step.

Insert h=P composed with Q minus P. Its first term is

    Q^T integral grad P(Qx+RQz) phi(z) dz
      =Q^T integral grad P(Rw) phi(w-Qx/R) dw.

The equality uses w=Qz+Qx/R, absolute Jacobian one, and radial invariance of phi under Q. The second term is integral grad P(Rw) phi(w-x/R) dw. Section 3 sends both terms to zero as R tends to infinity. It follows that grad h(x)=0 for every x. Since h(0)=P(0)-P(0)=0, h itself is zero.

Only the scalar Laplacian was transformed. The velocity was not asserted to solve a transformed Euler equation under Q. This explains why Q need not commute with J, and why the proof also covers determinant minus one.

## 5. Rigidity consequence and its extra assumptions

Suppose additionally U is C2 and uniformly sublinear, 0<c<1/2, and q is invariant under all rotations about the z-axis. The pressure theorem implies the same invariance for P. The axisymmetric-pressure theorem confirmed in A3029 then implies

    U=b e_z,   P=-(1-c)b z+p0.

The mean condition gives b=0, since a constant b e_z has E(R)/R^3=(4pi/3)b^2. Thus the conclusion is zero under the added scalar symmetry and growth hypotheses. Its pressure part needs none of the flow arguments used by the named rigidity theorem.

For a uniformly decaying C2 profile, the mean condition and uniform sublinearity are automatic. The scalar symmetry is still additional. In Frobenius notation, writing S=(DU+DU^T)/2 and Omega=curl U,

    q=|S|_F^2-|Omega|^2/2.

Indeed the symmetric-skew cross trace vanishes, and the squared Frobenius norm of the skew part is |Omega|^2/2. The proposed condition concerns this scalar combination, not separate symmetry of either term. No argument here derives its symmetry from the target assumptions.

## 6. Negative checks and limits

The pair U=0, P=x1 has q=0 and satisfies the divergence and Poisson equations, but violates the full momentum equation. Hence Poisson's equation without momentum does not imply pressure symmetry.

For a constant horizontal vector b nonzero, the exact full profile

    U=b,   P=-([(1-c)I+omega J]b).y

has q=0. Unless c=1 and omega=0, the horizontal linear pressure is nonzero and is not axisymmetric. This is particularly a countertest throughout 0<c<1/2. It violates the mean condition and target decay. It is not a counterexample to the Euler conjecture. Boundedness alone cannot replace the vanishing mean square in the pressure theorem.

The entire argument used compact test functions and exact identities. No singular-integral theorem, flow completeness, numerical computation, prescribed pressure normalization or external Liouville result was used. The seven-section source LIT361 and its fourteen author checks are retained in verification; their exact capture hashes are recorded there.


## 7. Existing-agent comparisons and the equivalent symmetry premise

The full A112 comparison and C note of 2026-11-04T07:02:05Z were read. Their checks of the Poisson cancellation, the evaluated-gradient identity, moving tests, harmonic averaging and constant-profile countertests agree with Sections 1-6. No gap or additional hypothesis was identified. A112 correctly observes that the implication in Section 1 is an equivalence: if P composed with Q equals P, then applying the orthogonally invariant distributional Laplacian gives q composed with Q equals q. The continuity of q makes this pointwise. Therefore, under the theorem's mean-square hypothesis, source symmetry is not a strictly weaker assumption than pressure symmetry.

The already confirmed energy law A052-A053 implies E(R)=o(R^3) for every bounded full profile with Hb and 0<c<1: below c=2/5 the velocity is zero; at c=2/5 it is in L2; above that endpoint the exponent 5-2/c is strictly less than 3. Thus in this class the mean-square premise follows from Hb. This deduction uses the energy law, not an independent general implication from distributional convergence of arbitrary bounded functions.

The C note's twenty-three diagnostic results and corresponding script/log were not read or rerun in this comparison and are not certified. Its analytical mode remark is proved separately below. The same note also compares LIT362; those points are assessed in that result's own review. The comparisons use the existing configured model agents; actual provider execution is not independently attested.

## 8. Zero-mass angular averages and exact nonzero mode support

Keep precisely the hypotheses of Section 1. Let mu be a finite complex Borel measure on O(3), and define

    T_mu f(y)=integral_(O(3)) f(Qy) dmu(Q).

If T_mu q is identically zero, then T_mu P is constant, equal to P(0) times mu(O(3)). In particular, when mu has mass zero, T_mu P is identically zero. Conversely, T_mu P identically zero implies T_mu q identically zero.

To prove the forward statement, compactness of O(3), finite total variation and local C1 regularity allow differentiation under the integral for T_mu P. Orthogonal invariance of the distributional Laplacian gives Delta T_mu P=-T_mu q=0. Hence h=T_mu P is smooth and harmonic. Its radial mean for the gradient is

    grad h(x)=integral_(O(3)) Q^T I(R,Qx) dmu(Q),
    I(R,xi)=integral grad P(Rw) phi(w-xi/R) dw.

For fixed x, the estimate in Section 3 is uniform over xi=Qx: the supports all lie in B_(1+|x|), and the translated test norms are fixed. It follows that sup_Q |I(R,Qx)| tends to zero. The right side is bounded by that supremum times the total variation of mu, so grad h=0. Evaluating at zero identifies the constant. Fubini is legitimate at every finite R because all integrands are continuous on compact sets and mu has finite variation. For the converse, apply the distributional Laplacian to T_mu P=0.

For rotations Q_alpha about the z-axis and any nonzero integer m, choose dmu=(2pi)^-1 exp(-im alpha) d alpha. This measure has mass zero, and T_mu f(r,theta,z)=f_m(r,z) exp(im theta) for the standard Fourier coefficient. Therefore

    q_m identically zero if and only if P_m identically zero,   m != 0.

The nonzero angular mode supports of the actual pressure and its quadratic source coincide. This is a statement about these two scalar functions, not a decoupling of the velocity equations or an exclusion of nonzero modes. For m=0 the measure has mass one; q_0=0 only forces P_0 to be constant. Neither conclusion removes the additional symmetry premise in Section 5.
