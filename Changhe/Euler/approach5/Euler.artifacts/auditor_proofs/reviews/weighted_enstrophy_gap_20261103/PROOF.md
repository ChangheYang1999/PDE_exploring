# Weighted enstrophy, the critical velocity bound and global smallness

## 1. Exact weighted theorem

Let0<c<1 and omega be any finite real number. Put J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J and L=(1-c)I+omega J. Suppose U in C2(R3;R3), P in C1(R3) satisfy

    LU+DU(Ax+U)+grad P=0, div U=0.                 (1)

Write B=Ax+U, G=DU with G_ij=partial_j U_i, S=(G+G^T)/2, W=curl U, w_inf=limsup_(|x|->infinity)|W(x)| and <x>=(1+|x|²)^(1/2). Assume W is bounded and |U|<=C_U<x>^(-a) for some a>=0. For a real m define kappa_m=1-(3-m)c/2. If

    m>max(1-2a,3-2/c), w_inf<sqrt(3) kappa_m,      (2)

then both integrals of <x>^(-m)|W|² and <x>^(-m)|DU|² over R3 are finite. No helicity assumption, pressure normalization or derivative bound at infinity is imposed. All integrals below use Euclidean volume and Frobenius matrix norm.

Sections7-9 strengthen the m=0 case and give a separate global-smallness Liouville theorem. They do not turn the far-field hypothesis(2) alone into profile nonexistence.

## 2. Exact curl, tensor and stretching identities

The curl of(1) is

    B.grad W=GW-W-omega JW.                       (3)

To check the rotation sign, curl(omega JU-omega(Jx).grad U) equals omega JW-omega(Jx).grad W. The c-dilation term contributes cW in addition to its transport, and curl((1-c)U) contributes(1-c)W. The nonlinear curl is U.grad W-W.grad U. Their sum is(3). Since W.JW=0,

    W.SW=|W|²+(1/2)B.grad|W|², div B=3c.         (4)

The antisymmetric part of G has norm squared |W|²/2. Hence

    |S|²-|W|²/2=tr(G²)=partial_i partial_j(U_i U_j),
    |G|²=|S|²+|W|²/2.                            (5)

The double divergence follows by the product rule and div U=0. For a unit vector v, trace S=0 gives

    v.Sv=S:(v tensor v-I/3)<=sqrt(2/3)|S|.         (6)

The constant follows from |v tensor v-I/3|²=2/3. Thus W.SW<=sqrt(2/3)|S||W|². Every identity is valid at the displayed C2/C1 regularity; taking curl of the C1 pressure is legitimate distributionally and yields zero.

## 3. Compact weights and the contradiction at infinite mass

Choose a smooth nonincreasing radial cutoff chi with chi=1 on[0,1], chi=0 on[2,infinity), and0<=chi<=1. Set phi_R=<x>^(-m)chi(|x|/R), X_R=integral phi_R|W|². These weights increase to <x>^(-m) as R increases. All integrations initially have compact support.

Equation(4) gives

    integral phi_R W.SW=(1-3c/2)X_R
                         -(1/2)integral |W|²B.grad phi_R. (7)

Since x.Jx=0,

    B.grad<x>^(-m)=-m<x>^(-m-2)(c|x|²+x.U).

For R>=max(1,2||U||infinity/c), B.grad chi(|x|/R)<=0 on its support, because the radial speed is at least c|x|/2. Writing |x|²=<x>²-1 and bounding both remaining error terms with |m| gives, for fixed rho>=1,

    integral phi_R W.SW>=(kappa_m-epsilon(rho))X_R-C1(rho),
    epsilon(rho)=(|m|/2)(c rho^(-2)
                          +sup_(|x|>=rho)|U(x)|/|x|)->0.   (8)

The constant C1(rho) controls the compact ball and is independent of R. Absolute values are necessary when m<0; the source's15:04 repair correctly includes them.

From(5), two integrations by parts give

    integral phi_R|S|²=X_R/2+E_R,
    E_R=integral U_i U_j partial_i partial_j phi_R.         (9)

Uniformly for R>=1, |D²phi_R|<=C_m<x>^(-m-2). Therefore

    |E_R|<=E_*=C_m C_U² integral <x>^(-m-2-2a)<infinity,   (10)

using m>1-2a. This estimate bounds the actual compact-weight error, without replacing pressure by an assumed integral formula.

Put W0(rho)=sup_(|x|>=rho)|W(x)|. Splitting off a fixed inner ball and applying(6) and Cauchy-Schwarz gives

    integral phi_R W.SW
      <=C2(rho)+sqrt(2/3)W0(rho)(X_R/2+E_*)^(1/2)X_R^(1/2). (11)

If X_R tended to infinity, divide(8),(11) by X_R, let R tend to infinity and then rho tend to infinity. It would give kappa_m<=w_inf/sqrt(3), contrary to(2). Hence X_R is bounded and monotone convergence proves the W integral finite. Equations(5),(9),(10) give integral phi_R|G|²<=X_R+E_* and prove the derivative integral finite too.

## 4. Shell rates, ball averages and sparsity

For either f=|W|² or f=|G|², weighted integrability gives

    integral_(R<=|x|<2R) f=o(R^m)                (12)

for every m satisfying(2). If m>=0 compare the weight with <2R>^(-m); if m<0 compare it with <R>^(-m). In either case the weighted integral over {|x|>=R} tends to zero, proving the little-o claim including m=0.

At m=3, kappa_3=1 and(2) holds for every a>=0 whenever w_inf<sqrt(3). The dyadic shell averages of W² and G² are summable. For

    0<d<min(2+2a,(2/c)(1-w_inf/sqrt(3))),

one can use m=3-d and obtain summability after multiplying those averages by2^(dk). The averages over arbitrary shells tend to zero by covering each with at most two adjacent dyadic shells. The averages over B_R tend to zero by splitting into a fixed inner ball and the remaining region, where R^(-3) integral f<=integral <x>^(-3)f up to a fixed factor. The latter tail can be made arbitrarily small. Chebyshev's inequality then gives a vanishing volume fraction for {|W|>=delta} in distant shells for each delta>0.

Equivalently let

    m_*=max(1-2a,3-(2/c)(1-w_inf/sqrt(3))).

Equation(12) holds for every m>m_*. For the natural velocity exponent a=1/c-1 in the campaign interval, the shell averages are

    o(R^(-(2/c)(1-w_inf/sqrt(3))+epsilon))

for every epsilon>0. Here natural refers to velocity decay; the theorem has not assumed a natural derivative bound.

## 5. The coefficient and an exact test field

The source correctly distinguishes sharpness of its algebraic estimates from optimality for bounded profiles. The affine field

    G=diag(-1/2,-1/2,1)+(sqrt(3)/2)J,
    U(x)=Gx, P=(x1²+x2²)/2-x3²                    (13)

solves(1) for every c and omega. Indeed G commutes with A and L, L+A=I, and G²+G=diag(-1,-1,2)=-D²P. Its vorticity is sqrt(3)e3, |S|²=3/2=|W|²/2 and W.SW=3=|W|³/sqrt(3). Thus it simultaneously attains the two algebraic constants in(6),(11). It is unbounded and outside Section1, so it does not show sharpness among bounded decaying profiles.

If instead the additional pointwise condition v.Sv<=theta|S| holds outside a compact set, with theta>0 and v=W/|W|, the same proof replaces sqrt(3)kappa_m by sqrt(2)kappa_m/theta. For alignment with a middle eigenvector one may take theta=1/sqrt(6): if the middle eigenvalue is positive, trace zero and ordering imply |S|²>=6lambda_middle²; if it is nonpositive the upper bound is immediate. This is a conditional improvement, not an established alignment property.

## 6. A minor m=0 correction and limits of the method

The source's FS-EG1 says M(R)=integral_(|x|<3R)|W|²=o(R^m) for m>=0. Weighted integrability proves this for m>0, but at m=0 a nonzero field with finite enstrophy has M(R) tending to its positive total enstrophy, not to zero. The correct bound there is M(R)=O(1). A single smooth compactly supported divergence-free field with nonzero curl is an exact test of this functional inference. It is not asserted to be a profile. The correction does not change the logarithmic scale comparison made in that paragraph.

Weighted integrability alone does not give pointwise decay. To see the functional obstruction, take a fixed smooth compactly supported divergence-free bump with nonzero curl and place translated copies in disjoint balls centered at(4^n,0,0). All derivatives remain bounded and the weighted W²,G² integrals are finite for every m>0, while both fields retain fixed nonzero pointwise values arbitrarily far away. This field fails the profile equation. Thus it only shows why that equation or additional local control must be used again. No general pointwise or nonexistence conclusion follows from Section1 alone.

## 7. Critical velocity extension at m=0

For this section assume0<c<2/3, retain(1), bounded U,W, and replace the power decay premise by the critical shell bound

    M_U=sup_(R>=1) R^(-2)
                    integral_(R<=|x|<2R)|U|²<infinity.     (14)

If w_inf<sqrt(3)(1-3c/2), then W and DU are in unweighted L2(R3). In particular |U|<=C<x>^(-1/2) suffices, including the endpoint excluded by the strict m>1-2a condition of Section1.

Proof: use phi_R=chi(|x|/R). The lower estimate(7) is now exactly at least kappa_0 X_R; there are no bulk weight errors. Its cutoff derivative still has the favorable sign for large R. The Hessian is supported only in the annulus and |D²phi_R|<=C/R², so |E_R|<=C M_U uniformly. Equation(11) is unchanged. If X_R diverged, division and the two limits would give kappa_0<=w_inf/sqrt(3), a contradiction. The derivative integral then follows from(9). This proof uses the special unweighted cutoff; it does not extend arbitrary nonzero-m endpoints where the bulk error may diverge logarithmically.

## 8. Removing the unweighted boundary error

Under Section7 one also has U in L6 and E_R->0. Here is a self-contained Sobolev justification. For a smooth compactly supported scalar f, define F_i by integrating |partial_i f| in its i-th variable. The fundamental theorem of calculus gives |f|^(3/2)<=(F1F2F3)^(1/2). Successive Cauchy-Schwarz, first in x1 and then in(x2,x3), gives

    integral |f|^(3/2)<=product_i ||partial_i f||1^(1/2).

Raising to power2/3 and using the arithmetic-geometric mean yields ||f||_(3/2)<=C||Df||1. Apply this to f=|v|^4 for a compactly supported smooth vector field v and use Cauchy-Schwarz to obtain

    ||v||6^4<=C||v||6^3||Dv||2,
    ||v||6<=C||Dv||2.                            (15)

Approximation gives the same inequality for compactly supported C1 fields. Apply it to chi(|x|/R)U. Its derivative L2 norm is bounded uniformly by ||DU||2+C M_U^(1/2), using(14). Fatou's lemma gives U in L6. Hence

    |E_R|<=C R^(-2) integral_(R<=|x|<2R)|U|²
          <=C(integral_(|x|>=R)|U|^6)^(1/3)->0.   (16)

Passing to the limit in(9) yields the exact global identity integral|S|²=(1/2)integral|W|² and therefore integral|DU|²=integral|W|². The stretching is absolutely integrable since W is bounded and S,W lie in L2. The cutoff term in(7) is bounded by C(c+||U||infinity/R) times the W² mass of the cutoff annulus, which tends to zero. Thus

    (1-3c/2)integral|W|²=integral W.SW.           (17)

All boundary terms have now been controlled explicitly.

## 9. Global small-vorticity Liouville consequence

Under(1),0<c<2/3, bounded U,W and(14), the additional global bound

    ||W||infinity<sqrt(3)(1-3c/2)                (18)

forces U=0. The far-field strict inequality needed in Section7 follows from(18). Using(6), Cauchy-Schwarz and the exact global norm identity of Section8 in(17) gives

    kappa_0 integral|W|²
       <=(||W||infinity/sqrt(3))integral|W|².

The strict inequality forces W=0. The exact derivative norm identity then gives DU=0, so U is constant. Bound(14) excludes a nonzero constant, hence U=0.

A slightly stronger formulation permits ||W||infinity<=sqrt(3)kappa_0 provided w_inf<sqrt(3)kappa_0 remains strict. The preceding steps still give finite integrals. If the global bound is attained and the enstrophy were positive, equality in all three upper estimates would force |S|=|W|/sqrt(2) almost everywhere and |W| either zero or sqrt(3)kappa_0 almost everywhere. Continuity and connectedness then make |W| a single constant. Finite L2 excludes the positive constant. Thus U=0 also in this formulation. Without the strict far-field inequality at global equality, this proof does not establish finiteness and makes no claim.

This is an additional conditional theorem for every omega, with no helicity assumption. In the campaign interval the natural velocity bound satisfies(14), but neither it nor bare decay supplies the global small-vorticity hypothesis.

## 10. Evidence, comparison and unresolved scope

All source sections, the15:04 negative-m correction and15:05 addendum were read. The exact identities, affine example and estimates were reconstructed without new computation; the parent symbolic log is not used as proof. The source and real capture time are pinned under verification. The existing source agent is configured model; its provider runtime remains unattested. Sections7-9 are additional independently checked results for comparison through those existing working files. No new model client or formal build was used.

The original weighted theorem, its rates and its algebraic constants are confirmed at their exact scopes. The m=0 cumulative-mass wording requires Section6's repair. Sections7-9 retain the critical velocity and vorticity size assumptions. The unrestricted bare-decay, arbitrary-helicity, all-rotation conjecture remains open.
