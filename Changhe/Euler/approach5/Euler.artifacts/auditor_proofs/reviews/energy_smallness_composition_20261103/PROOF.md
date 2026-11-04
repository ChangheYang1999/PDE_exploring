# Energy, weighted enstrophy and small-strain consequences

## 1. Exact setting and dependencies

Let U in C2(R3;R3), P in C1(R3), 0<c<1 and omega any finite real number solve

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    div U=0, Jx=e3 cross x.

Write G=DU, S=(G+G^T)/2, W=curl U, alpha=5-2/c, m0=3-2/c and kappa_m=1-(3-m)c/2=(c/2)(m-m0). Matrix magnitudes below are Frobenius norms. Hb means U is bounded and U(R.) tends to zero in distributions as R tends to infinity.

A040/A052 prove under Hb that U=0 for c<2/5, U is in L2 for c=2/5, and E(R)=integral_(B_R)|U|²=O(R^alpha) for c>2/5, with a strictly positive normalized limit if U is nonzero. A1429-A1436 give the weighted cutoff enstrophy argument and its critical shell extension. Their entire ten-section independent proof was freshly reread. A1525 gives the critical vorticity obstruction. No new pressure normalization is added.

## 2. The energy law supplies the needed velocity weights

Under Hb, E(R)<=C_E R^max(alpha,0) for R>=2. If c<2/5 the field is zero. Otherwise alpha>=0 and m>m0 implies m+2>0. On shells 2^k<=|y|<2^(k+1),

    integral <y>^(-m-2)|U|²
      <=E(2)+C_E 2^alpha sum_(k>=1)2^(k(alpha-m-2))<infinity.

The exponent alpha-m-2=m0-m is strictly negative. For c<=2/3, alpha<=2 whenever alpha>=0, so

    M_U=sup_(R>=1) R^(-2) integral_(R<=|y|<2R)|U|²<infinity. (1)

This includes c=2/3 as a shell bound, but does not give a positive enstrophy damping constant at that endpoint.

## 3. Weighted enstrophy without a pointwise velocity rate

Assume W is bounded, set w_inf=limsup_(|y|->infinity)|W(y)|, and suppose

    m>m0, w_inf<sqrt(3) kappa_m.                    (2)

Then integral<y>^(-m)(|W|²+|G|²) is finite. To check the substitution in A1429, take phi_R=<y>^(-m)chi(|y|/R), with a fixed smooth radial cutoff. Its second derivatives are bounded by C_m<y>^(-m-2), uniformly in R. The error in the weighted div-curl identity is therefore bounded by the finite integral in Section2. The transport cutoff proof uses U only through its supremum, the radius R>2||U||infinity/c, and

    (|m|/2)(c rho^(-2)+sup_(|y|>=rho)|U(y)|/|y|)->0.

Every other absorption and monotone cutoff step in A1429 uses only that error bound and (2). Thus replacing its pointwise velocity-decay premise by Hb is legitimate. No weighted pressure estimate or global bound on G is needed.

If U is nonzero and 2/5<c<1, A1525 gives divergence for every m<=m0. Section3 gives convergence for every m>m0+2w_inf/(sqrt(3)c). Consequently the infimum of admissible vorticity weight exponents lies between these two endpoints. If w_inf=0 it is exactly m0 and is not attained. Weighted masses alone imply no pointwise derivative rate.

## 4. Exact global identities and vorticity smallness

Assume 0<c<2/3, Hb and W bounded. Put kappa0=1-3c/2>0. If w_inf<sqrt(3)kappa0, (1) and A1433-A1434 give

    W,G in L2, U in L6,
    integral |G|²=integral |W|²,
    integral |S|²=(1/2)integral |W|²,
    kappa0 integral |W|²=integral W.SW.             (3)

Here m0<0, so setting m=0 in Section3 already proves the required L2 integrability. Alternatively, (1) is precisely the hypothesis of the previously checked critical shell argument. The global identities and the homogeneous Sobolev conclusion then follow as in A1434: the transport boundary term vanishes by L2 integrability, bounded W controls the stretching integral, and Hb removes the constant velocity.

Trace-free symmetric S satisfies W.SW<=sqrt(2/3)|S||W|². Cauchy-Schwarz and (3) give, writing I=integral|W|²,

    kappa0 I<=sqrt(2/3)||W||infinity ||S||2 ||W||2
              =||W||infinity I/sqrt(3).

Hence ||W||infinity<sqrt(3)kappa0 forces U=0. The equality case with a strict far-field limsup also forces zero by the equality analysis already proved in A1435: all the displayed inequalities would have to be equalities, making |W| equal to its positive global supremum wherever W is nonzero; continuity and the strict tail bound preclude that configuration. Thus a nonzero profile has supremum at least the threshold, and equality forces w_inf to equal that threshold. Once U=0, P is constant by the full equation. These are exactly Theory Agent A C56 and coordinator CO59(a).

## 5. Betchov's identity with the boundary terms retained

For this section only, let U be C2, bounded and divergence-free, and assume G is bounded and in L2. It need not solve the profile equation. With phi_R=chi(|y|/R), integration by parts gives

    integral phi_R tr(G³)
      =-integral U_i (partial_j phi_R)G_jk G_ki
         +(1/2)integral tr(G²) U.grad phi_R.        (4)

Indeed integrate partial_j U_i in partial_j U_i partial_k U_j partial_i U_k. The derivative on partial_k U_j vanishes by divergence freedom, while partial_k U_j partial_j partial_i U_k=(1/2)partial_i tr(G²). The second integration by parts gives (4). Its right side is at most C||U||infinity R^(-1)integral_(R<|y|<2R)|G|² and tends to zero. The integrand on the left is integrable because G is bounded and square integrable.

Write G=S+Omega, with Omega h=(1/2)W cross h. Since Omega²=(W tensor W-|W|²I)/4 and tr S=0,

    tr(G³)=tr(S³)+(3/4)W.SW.

Consequently

    integral W.SW=-(4/3)integral tr(S³).           (5)

For a symmetric trace-free 3 by 3 matrix, |tr(S³)|<=|S|³/sqrt(6). One direct verification fixes the sum of squared eigenvalues and uses a Lagrange multiplier under their zero-sum constraint: an extremum has at most two distinct eigenvalues, hence is proportional to (2,-1,-1), giving exactly1/sqrt(6). Compactness of the constraint sphere attains both extrema.

## 6. The submitted strain corollary and a one-sided variant

Under Section4's hypotheses, additionally assume S is bounded. Then G=S+Omega is bounded, so (5) applies to (3). It follows that

    kappa0 I<= [2/(3sqrt(6))]||S||infinity I.

Thus ||S||infinity<(3sqrt(6)/2)kappa0 forces U=0. Also W.SW<=lambda_max(S)|W|² in (3), so sup lambda_max(S)<kappa0 forces zero. These are precisely CO59(b1,b2), with all its stated hypotheses.

A useful one-sided refinement of the first inequality is

    -tr(S³)<=(-lambda_min(S))|S|²/2.

To prove it, write the eigenvalues as -a,b,a-b with a>=0. If b(a-b)<=0 the left side is nonpositive. Otherwise 0<b<a and t=b(a-b)<=a²/4; the inequality becomes 3at<=a(a²-t), which is exactly4t<=a². Therefore, still under Section4 and bounded S,

    sup(-lambda_min(S))<3kappa0

also forces U=0, by (5) and (3). The Frobenius criterion implies this one because -lambda_min(S)<=sqrt(2/3)|S|. This is an optional refinement, not a claim about a sharp Euler threshold.

## 7. The far-field vorticity premise is redundant when strain is bounded

Under Hb, bounded W and bounded S, the gradient G is bounded. A492, whose complete nine-section proof was freshly reread, applies for every0<c<1 and finite omega: bounded U and G imply W=O(1/r) and G=O(log r/r). It uses neither enstrophy integrability nor a smallness hypothesis. Thus w_inf=0 follows before using Section4, and the strict far-field condition is automatic for0<c<2/3.

Accordingly CO59(b1) and the one-sided minimum-eigenvalue refinement hold under Hb, W bounded and S bounded without an additional far-field vorticity condition. The final scope paragraph of CO59 says that it still needs that condition; as a logical necessity in this stated bounded-strain class, this is incorrect. The submitted theorem remains valid. This does not remove bounded W or derive bounded G from Hb alone.

## 8. A stronger already established core strain criterion

There is an elementary stronger version of CO59(b2). Let c>0, omega real, U C2 bounded, P C1 solve the full profile equation. Put M=||U||infinity. If

    lambda_max S(y)<1 for all |y|<=M/c,            (6)

then U is constant. Hb or uniform decay makes that constant zero. No global W bound is needed, and c need not be less than2/3.

This is the previously established compact-core criterion in `auditor_proofs/proofs/small_rotational_defect/PROOF.md`, reread in full. For completeness, continuity on the compact ball gives delta,theta>0 such that lambda_max S<=1-theta on |y|<=M/c+delta. The B=(cI-omega J)y+U flow is complete in both directions because B is locally Lipschitz with linear growth. Radially B.y/|y|>=c|y|-M. The enlarged ball is backward invariant and every backward orbit enters it in finite time. On it the exact vorticity equation yields d|W|²/dt<=-2theta|W|². Starting arbitrarily far backward in that compact ball, its bounded vorticity forces the value at any fixed point to vanish. Invertible transport propagates this to every point. Then U is bounded harmonic and hence constant. The case M=0 is immediate.

Thus sup lambda_max S<1 on the whole space is sufficient, and the weaker CO59(b2) threshold kappa0 with its far-field and global vorticity premises is not the best available formulation. This is an existing theorem, not a new claim of novelty.

## 9. Audit and remaining scope

Every section of both submissions was read. All nine independent sections were postread, including the two full dependency rereads identified above. No symbolic check was treated as proof and none was rerun. Existing configured model sources supplied C56 and CO59; runtime model attestation is unavailable. Sections7-8 are sent back for comparison. The numerical decimal thresholds in the submission are only rounded displays of the exact constants. No literature novelty claim is endorsed here. All conclusions retain their displayed smallness or derivative hypotheses. They do not prove nonexistence under bare uniform velocity decay for the campaign's arbitrary omega and helicity.
