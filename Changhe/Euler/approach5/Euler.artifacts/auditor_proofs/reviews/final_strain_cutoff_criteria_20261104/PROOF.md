# Final compact-cutoff recheck of the strain criteria

Status: CONFIRMED A3260 after the complete existing C comparison and six-section independent disposition. The scope is the existing A2004-A2005 and A2009 implications. No numerical instance or algebraic optimality claim is included.

## 1. Exact statements and notation

Let 0<c<2/3 and let omega be any fixed finite real number. Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J. Suppose U belongs to C2(R3;R3), P belongs to C1(R3), and

    (1-c)U+(DU)(Ay+U)+omega JU+grad P=0, div U=0.

Assume Hb: U is bounded and U(R.) tends to zero in distributions on R3 as R tends to infinity. Set V=sup|U|, G=DU with G_ij=partial_j U_i, S=(G+G^T)/2, W=curl U, t=|W|^2, B=Ay+U and kappa0=1-3c/2. Every matrix norm in this proof is the Frobenius norm. Eigenvalue notation applies to real symmetric matrices.

The two conclusions are conditional:

1. If -lambda_min(S(y))<=l for every y, for some real l<3kappa0, then U=0 and P is constant. In particular, sup|S|<(3sqrt(6)/2)kappa0 suffices. No bound on W or on G is assumed.
2. Suppose K is a compact set of trace-free symmetric3by3matrices, S(y) belongs to K, and |W(y)|<=M for every y, where M>0 is finite. Suppose a>0, b is real, g belongs to C1([0,M^2]), g>=0, g(0)=0 and g'(0)>a/(4kappa0). Define

       D(S,W)=a|S|^2+b tr(S^3)+(3b/4-2g'(t))W.SW
              +2g'(t)t-3c g(t)-a t/2, t=|W|^2.

   If D(S,W)>0 for every (S,W) in K times {|W|<=M} except possibly (0,0), then U=0 and P is constant.

The second conclusion includes only the bounded-vorticity subcase of the first. Neither statement assumes uniform U decay, bounded pressure, a finite integral of a positive power of vorticity, symmetry or helicity. Hb is retained. Constants may depend on the fixed profile, c, omega, the cutoff, and the displayed parameters. No sharpness theorem for Euler profiles is asserted.

## 2. Actual pressure dependency and compact identities

The already accepted A3235 energy theorem under Hb gives

    E(R)=integral_(|y|<=R)|U|^2<=C R^beta,
    beta=max(5-2/c,0)<2, R>=2.                                (1)

For c<2/5 it gives U=0 directly; for c=2/5 finite energy; above2/5 its finite renormalized coefficient gives (1). Its actual-pressure normalization comes from momentum and Hb. No pressure assumption is added here. The remainder of this argument uses only (1) from that theorem.

Take a smooth nonnegative nonincreasing chi, one on [0,1] and zero on [2,infinity), and phi_R(y)=chi(|y|/R). Its derivatives are supported in R<=|y|<=2R. Set Y(R)=integral_(|y|<=R)|G|^2. The curl equation and the skewness of J give

    B.grad t=2(W.SW-t), div B=3c.                             (2)

The skew part of G is v maps to W cross v/2, so |G|^2=|S|^2+t/2 and tr(G^2)=|S|^2-t/2. Twice integrating by parts with compact support, using div U=0, gives

    integral phi_R(|S|^2-t/2)=integral U_i U_j partial_i partial_j phi_R=:E_R,
    |E_R|<=C R^(beta-2).                                      (3)

There is no assertion here that the separate unweighted integrals are finite.

For Q_j=U_i G_jk G_ki, the ordinary product rule gives

    partial_j Q_j=tr(G^3)+(1/2)U.grad tr(G^2),
    tr(G^3)=div(Q-(1/2)U tr(G^2)).                            (4)

Indeed the derivative on G_jk vanishes by div U=0; the derivative on G_ki is half the derivative of tr(G^2) after interchanging the summed j,k. Only second derivatives of U are used. Also tr(G^3)=tr(S^3)+(3/4)W.SW. Therefore

    |integral phi_R tr(G^3)|<=C V R^-1 Y(2R).                 (5)

The potentially nonzero shell term is retained; G need not be bounded.

For nonnegative C1 g on the attained t range, equation (2) and compact integration give

    integral phi_R[2g'(t)(t-W.SW)-3c g(t)]=-F_R,
    F_R=-integral g(t) B.grad phi_R>=0 for R>V/c.             (6)

The sign follows from B.y=c|y|^2+U.y>0 on the cutoff shell. Rotation is tangent to that shell. For g(t)=t no global bound on t is needed, because each integration has compact support. Combining a times(3), b times(4) and(6), and bounding the cubic term by |b| times(5), yields

    integral phi_R D<=C R^(beta-2)+C R^-1 Y(2R).              (7)

This estimate assumes no trajectory escape or global characteristic completeness; no flow representation is used.

## 3. Finite iteration and the strain-only theorem

If D>=kappa|G|^2 with kappa>0 and Y(R)<=C R^3 initially, (7) gives

    kappa Y(R)<=C R^(beta-2)+C R^-1 Y(2R).                    (8)

Since beta<2, the first term is bounded for large R. Successively inserting the current bound gives Y(R)<=C(1+R^2), then C(1+R), then C. Inserting the last bound gives Y(R)<=C(R^(beta-2)+R^-1)->0. Nonnegative monotonicity of Y forces Y(R)=0 for every R. Constants can change between the finitely many steps; none depends on R. No infinite contraction without a growth bound is invoked.

For conclusion1, trace zero implies -lambda_min>=0, so an admissible l is nonnegative. If lambda_min>=-l, the eigenvalues lie in [-l,2l] and |S|^2<=6l^2. For ordered eigenvalues lambda1>=lambda2>=lambda3, trace zero gives

    tr(S^3)=3lambda1 lambda2 lambda3,
    |S|^2/2-3lambda1 lambda2=(lambda1-lambda2)^2.

Multiplying the latter inequality by -lambda3>=0 gives -tr(S^3)<=l|S|^2/2. Set g(t)=t, b=8/3, a=2kappa0+2l/3. The W.SW coefficient vanishes exactly, and

    D>=((2/3)(3kappa0-l))(|S|^2+t/2)=kappa|G|^2,
    kappa=(2/3)(3kappa0-l)>0.                                 (9)

The initial growth bound is derived, not assumed: (3) gives

    (1/2)integral phi_R t<=6l^2 volume(B_(2R))+C R^(beta-2),

so Y(R)<=C R^3 although W may be unbounded. The finite iteration gives G=0. Thus U is constant; Hb forces that constant to vanish and momentum then gives grad P=0. The norm version follows from -lambda_min<=sqrt(2/3)|S|, retaining its strict inequality.

## 4. Compact mixed criterion

For conclusion2, write g0=g'(0). As (S,W)->(0,0), C1 regularity of g gives

    D=a|S|^2+(2kappa0 g0-a/2)t+o(|S|^2+t).                   (10)

The terms tr(S^3) and |S|t are smaller order; the remaining errors are bounded by 2|g'(t)-g0|t+3c|g(t)-g0t|. Both leading coefficients in (10) are positive. Hence D>=kappa1(|S|^2+t/2) near zero. On the compact complement of a smaller such neighborhood, positivity and continuity give a positive minimum of D; |S|^2+t/2 has a finite maximum there. Combining the two regions gives one kappa>0 with D>=kappa|G|^2 on all the permitted pairs. If a region is empty it imposes no restriction.

Now G is bounded by compactness of K and |W|<=M, so Y(R)<=C R^3. Equations (7)-(8) and the finite iteration give G=0. The same Hb and momentum argument gives U=0 and P constant. No numerical search for a,b,g is part of this implication; positivity on the entire compact set is an additional premise.

## 5. Scope and evidence

The source setting, master identity, iteration, TheoremSF and TheoremSF.3 were read in full at lines75-132 and214-232 of the captured source version. All145lines of the earlier independent reconstruction were read. The present fresh result covers only A2004-A2005 and A2009, not the other algebraic threshold claims, any positive numerical instance, the optimal-weight ODE, or later exact tables. Source identities are in the team records. A3235 is the sole external energy dependency within this audit; all subsequent estimates are derived above.

Every fixed finite omega is included: the curl scalar identity cancels its skew contribution, and the radial cutoff eliminates its shell-normal contribution. This does not prove the strict strain or mixed positivity hypotheses for an arbitrary decaying Euler profile. The main nonexistence conjecture remains unresolved. No computation or formalization is claimed. Existing configured model collaboration uses the existing working files, with actual provider execution independently unattested.
