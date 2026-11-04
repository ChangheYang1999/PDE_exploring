# Strain criteria without a bound on vorticity

Status: independent audit of Theory Agent A C62. Exact conclusions and limits are stated below. The source is pinned in the team records. Here S always denotes the strain matrix, not a tail Bernoulli scalar.

## 1. Hypotheses and the pressure input

Let U in C^2(R^3;R^3), P in C^1(R^3), c>0 and omega real satisfy

    (1-c)U + ((Ay+U).grad)U + omega J U + grad P = 0,
    div U = 0,  A=cI-omega J,  J y=e3 x y.

Assume Hb: U is bounded and U(R.) tends to zero in distributions as R tends to infinity. Put M_U=sup|U|, B=Ay+U, G=DU with G_ij=partial_j U_i, S=(G+G^T)/2, W=curl U and t=|W|^2. Then tr S=0, div B=3c and |G|^2=|S|^2+t/2. For the strain criteria assume 0<c<2/3 and put kappa_0=1-3c/2>0 and beta=max(5-2/c,0)<2.

The independently audited energy theorem A052, and its explicit consequence A1530, give

    E(R):=int_{B_R}|U|^2 <= C_E R^beta,  R>=2.                 (1)

This holds under Hb, not just uniform pointwise decay. At c<2/5 the stronger U=0 conclusion is already known; at c=2/5 finite energy gives beta=0; above 2/5 the bounded renormalized energy gives (1). The complete precise statements of Theorem A and EH.0 are pinned alongside this proof. The pressure normalization needed by Theorem A follows from the full momentum equation and Hb, as in the independently checked pressure_normalization proof. No pressure decay is being added as a hypothesis. The present argument uses only (1) from that pressure-dependent theorem.

## 2. Compactly supported identities and iteration

Choose a smooth nonnegative nonincreasing chi, equal to one on [0,1] and zero on [2,infinity), and set phi_R=chi(|y|/R). Every integration below has compact support. There is no use of an unproved boundary term at infinity. Write Y(R)=int_{B_R}|G|^2.

Taking curl of the profile equation and taking its scalar product with W gives

    B.grad t=2(W.SW-t).                                    (2)

Both skew rotation terms disappear from this scalar identity. Twice integrating by parts, using div U=0, gives

    int phi_R (|S|^2-t/2)
      =int phi_R partial_j U_i partial_i U_j
      =int U_i U_j partial_i partial_j phi_R =: E_R,
    |E_R| <= C R^(beta-2).                                 (3)

The sign and factor in (3) follow also from tr G^2=|S|^2-t/2. Define Q_j=U_i G_jk G_ki. Direct differentiation yields

    div Q=tr G^3+(1/2)U.grad tr G^2,
    tr G^3=div(Q-(1/2)U tr G^2).

Consequently

    |int phi_R tr G^3| <= C M_U R^(-1)Y(2R).                (4)

This uses only U in C^2. The products in the differentiated identity are classical; no boundedness of G is required. The algebraic expansion is tr G^3=tr S^3+(3/4)W.SW, since the skew part of G sends v to (W x v)/2.

For g in C^1([0,infinity)), g>=0, equation (2) gives

    int phi_R [2g'(t)(t-W.SW)-3c g(t)] = -F_R,
    F_R=-int g(t) B.grad phi_R >=0  if R>M_U/c.             (5)

Indeed B.y=c|y|^2+U.y>0 on that shell. Polynomial or faster growth of g at infinity does not impair this compactly supported identity, since W is bounded on each compact set. With constants a,b define

    D=a|S|^2+b tr S^3+(3b/4-2g'(t))W.SW
        +2g'(t)t-3c g(t)-a t/2.

Equations (3)-(5) imply

    int phi_R D <= C R^(beta-2)+C R^(-1)Y(2R).              (6)

Suppose D>=kappa|G|^2 for a fixed kappa>0 and Y(R)<=C R^3. Then (6) implies successively Y(R)<=C(1+R^2), Y(R)<=C(1+R), and Y(R)<=C. One more substitution gives Y(R)<=C(R^(beta-2)+R^(-1)), which tends to zero. Nonnegativity and monotonicity of Y imply Y(R)=0 for every R. All constants may change during the finite sequence; none depends on R. This is the exact point where beta<2 is needed.

## 3. The strain bound and the power weight

For a trace-free symmetric 3 by 3 matrix,

    -tr S^3 <= (-lambda_min(S)) |S|^2/2,
    -lambda_min(S) <= sqrt(2/3)|S|,
    lambda_max(S) <= -2lambda_min(S).

For the first inequality use ordered eigenvalues lambda_1>=lambda_2>=lambda_3, tr S^3=3lambda_1lambda_2lambda_3 and |S|^2/2-3lambda_1lambda_2=(lambda_1-lambda_2)^2. If lambda_min>=-l then each eigenvalue lies in [-l,2l], and the maximum of their squared sum subject to trace zero is 6l^2.

Theorem SF. Under the hypotheses of Section 1, if sup(-lambda_min(S))<=l<3kappa_0, then U=0 and P is constant. No bound on W is assumed.

Proof. Take g(t)=t, b=8/3 and a=2kappa_0+2l/3. The W.SW term cancels exactly. The cubic inequality gives

    D >= (2/3)(3kappa_0-l)(|S|^2+t/2).

Because |S|^2<=6l^2, (3) gives int phi_R t/2<=6l^2|B_{2R}|+C R^(beta-2). Thus Y(R)<=C R^3 even if W is unbounded. Section 2 forces DU=0. Hb forces the resulting constant U to be zero, and momentum gives grad P=0. In particular sup|S|<(3sqrt(6)/2)kappa_0 suffices by the second matrix inequality.

Power-weight proposition. For any c>0, if the same full profile and Hb hypotheses hold and lambda_max(S)<=r<1 everywhere, then U=0. Choose q>=1 with 2q(1-r)>3c, and use a=b=0, g(t)=t^q in (5). The integrand is at least [2q(1-r)-3c]t^q. Its integral is nonpositive, hence t=0 on every sufficiently large ball. U is then bounded, curl free and divergence free, so each component is harmonic and constant; Hb gives U=0. This proof uses no pressure estimate and no energy bound. It requires the curl equation inherited from the full profile.

The earlier characteristic theorem A093 assumes lambda_max<1 only on the compact ball |y|<=M_U/c; its finite-dimensional consequences are |S|<sqrt(3/2) or -lambda_min<1/2 on that ball. These are inherited consequences, not a new proof of A093 here. The strain-norm thresholds agree at c=4/9, and the minimum-eigenvalue thresholds agree at c=5/9. The core and global hypotheses must remain distinct when comparing their numerical sizes.

## 4. Exact obstruction within the constant-coefficient weight family

Let K be a compact subset of trace-free symmetric matrices containing a neighborhood of zero. Suppose s_+=max_K lambda_max>=1, let s_-=min_K lambda_min, and suppose D[a,b,g]>=0 for every S in K and every W in R^3, where a,b are constants and g in C^1([0,infinity)), g>=0, g(0)=0. These are purely algebraic assumptions.

At W=0 and S=epsilon S_1, both signs of S_1 show a>=0. If a=0, the nonzero cubic tr S_1^3 and its negative imply b=0. Choose a matrix in K with an available Rayleigh quotient 1. At W=sqrt(t)w in that direction the remaining expression is -3c g(t), forcing g=0. Thus the a=0 case is trivial when s_+>=1.

If a>0, divide through by a, write d=b/a and replace g by g/a. Then

    A(S):=|S|^2+d tr S^3 >=0.                              (7)

For any s in [s_-,s_+] a matrix S_s in K has a unit vector with Rayleigh quotient s: for positive s use a matrix attaining s_+, and for negative s a matrix attaining s_-. Trace zero puts zero in each Rayleigh interval. Positivity at W=sqrt(t)w_s gives

    A(S_s)/t +3ds/4-1/2 +2(1-s)g'(t)-3c g(t)/t >=0.        (8)

The case s=1 bounds m(t)=g(t)/t on [1,infinity), with m>=0. Put t=exp(tau). Since g'=m+partial_tau m, average (8) over tau in [T,2T]. The integrated derivative is a bounded endpoint difference divided by T, and A(S_s)exp(-tau) tends to zero in average. A subsequence of the bounded averages of m converges to some gamma>=0, independent of s. For each fixed s, passing along that same subsequence gives

    (3d/4-2gamma)s+2gamma kappa_0-1/2 >=0.                  (9)

No bound on g' at infinity is required. The same sequence proves (9) for every s; one is not taking an unjustified subsequence depending on s.

Put X0=2gamma kappa_0-1/2>=0. The following exact positive linear combinations prove the three claimed restrictions.

For K={lambda_min>=-l}, l>=1/2, let X1 be the left side of (9) at s=2l. From (7) at diag(l/2,l/2,-l), X2=2-dl>=0. Then

    (3/2)X2+X1+((2l-kappa_0)/kappa_0)X0
      =(3kappa_0-l)/kappa_0 >=0.

Thus l<=3kappa_0. For K={|S|<=sigma}, sigma>=sqrt(3/2), put r=sqrt(2/3)sigma>=1. Let Y1 be (9) at s=r and Y2=sqrt(6)/sigma-d, nonnegative by (7) at sigma diag(1,1,-2)/sqrt(6). Then

    Y1+(3r/4)Y2+((r-kappa_0)/kappa_0)X0
      =(3kappa_0-r)/(2kappa_0) >=0.

Thus sigma<=(3sqrt(6)/2)kappa_0. For K={lambda_max<=r}, r>=1, use Z1 from (9) at s=r and Z2=1/r-d>=0 from (7) at diag(r,r,-2r). Then

    Z1+(3r/4)Z2+((r-kappa_0)/kappa_0)X0
      =((3/2)kappa_0-r)/(2kappa_0) >=0.

Every multiplier is nonnegative because 0<kappa_0<1 and the specified l,r bounds hold. All three sets K are compact in the trace-free symmetric subspace. These necessary conditions, together with Section 3 applied below either threshold, give the strict-bound suprema

    max{3kappa_0,1/2},
    max{(3sqrt(6)/2)kappa_0,sqrt(3/2)},
    max{(3/2)kappa_0,1}

for the minimum-eigenvalue, norm and maximum-eigenvalue versions respectively. For the last sufficiency, lambda_max<=r implies lambda_min>=-2r. The endpoints themselves are not classified. This is a limitation of D[a,b,g] with constant a,b and scalar g, not a sharpness theorem for Euler profiles or all multiplier methods.

## 5. A conditional theorem with both strain and vorticity bounds

Let 0<c<2/3, retain the profile and Hb hypotheses, and suppose S(y) belongs to a compact K and |W(y)|<=M<infinity. Suppose a>0, b real, g in C^1([0,M^2]), g>=0, g(0)=0, g'(0)>a/(4kappa_0), and D[a,b,g](S,W)>0 throughout K times {|W|<=M} except possibly at (0,0). Then U=0.

Indeed, near zero continuity of g' gives

    D=a|S|^2+(2kappa_0 g'(0)-a/2)t+o(|S|^2+t).

The cubic term and mixed term |S|t are of smaller order; the other remainders are controlled by g'(t)-g'(0) and g(t)-g'(0)t. Both displayed coefficients are strictly positive. Hence D>=kappa_1(|S|^2+t/2) near zero. On the compact remaining set D is positive and |S|^2+t/2 is bounded, giving a uniform positive coercivity constant there as well. Since G is bounded, Y(R)<=C R^3, and Section 2 applies.

This theorem includes the bounded-vorticity subcase of SF, not the whole unbounded-vorticity result by its statement alone. For a=1 and fixed b, minimization first over matrices with a given Rayleigh quotient gives exactly the source's function Lambda(t,p). Its superlevel set in p is convex and closed because Lambda is an infimum of affine functions; it can be empty or unbounded as well as a finite closed interval. The claim that a numerically integrated lower branch is optimal requires a further comparison argument, not supplied here.

## 6. Verification and scope

All six sections of C62 and every section of this independent proof were read. The identities and three multiplier certificates above were checked by exact algebra. No source script, random check or numerical region search was executed or used as proof. The proposed example values near c=1/2 have no verified exact admissibility certificate here, and do not become instances of Section 5.

The proof is uniform in arbitrary real omega because the rotation is skew in (2) and tangent to cutoff spheres in (5). It uses no global characteristic-flow argument, no assumption of pressure decay, no unbounded-domain integration without cutoffs, and no assumed bound on W in Section 3's SF theorem. Bounded strain and the strict threshold remain essential hypotheses. The unrestricted decaying-profile conjecture is not resolved.
