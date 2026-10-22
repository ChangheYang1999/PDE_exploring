# Compact zero-strain tests map into the weak axis spaces

This proof is written before new computations. Its theorem and application remain OPEN until independent checks, complete actual Claude Opus5.5 review and later own adjudication. It concerns mapping of a smooth test class, not boundedness on a completed graph domain.

## Statement and hypotheses

Write r=(x^2+y^2)^(1/2). The background is the canonical, exactly joined and normalized modal density of modal_repair/PROOF.md, with its fixed exact k in(0,1/2),

 rho(x,y)=x^2 y a(x,y),

where a is even in both variables. On every compact annulus a is C6. There are constants depending on the background such that, for every Cartesian multi-index alpha of order at most5,

 |D^alpha(a-1)| <= C_alpha r^(2-|alpha|) near0,
 |D^alpha a| <= C_alpha r^(k-3-|alpha|) near infinity.       (1)

The first bound is on the punctured plane; it does not assert C5 regularity of a at0. The canonical velocity U[rho] is locally C4. These hypotheses are verified directly for the finite modal definition below, rather than deduced by differentiating a qualitative big-O statement.

Let h be any real C_c^infinity density, even in x and odd in y, supported at positive distance from both coordinate axes, with canonical stream and velocity

 -Delta psi[h]=partial_x h, U[h]=(-psi_y,psi_x),
 Sigma(h)=psi_xy(0)=0.

All its center jets, in particular J(h)=partial_xxy h(0)/2, vanish. For any fixed real ell set

 Lh=(ell X+U[rho]).grad h-h+U[h].grad rho
                                      +(Sigma(h)/3)X.grad rho.       (2)

For a weight parameter b, distinct from the background factor a(x,y), define Y_(b,s) by

 T_b f(z,y)=exp((1/2-b)z)f(exp(z),y),
 ||f||Y_(b,s)=||T_b f||H^s(R^2_(z,y)), x>0.

The Sobolev norm uses the Fourier multiplier (1+xi^2+eta^2)^(s/2). Then for every fixed0<=b<5/2 and s=153/50,

 h|_(x>0), (Lh)|_(x>0) belong to Y_(b,s).                 (3)

In particular the specific density of axis_weighted_nonlocal_mapping, and every member of its compact annular zero-strain test class, has its image in these weak axis spaces. Its nonmembership obstruction for b>=5/2 does not persist as nonmembership of this test class in0<=b<5/2. No uniform bound in h or b, extension to the full frozen graph domain, inverse, range property, nonlinear closure or stationary profile is claimed. Result199 still excludes a closed full-L realization whose domain contains the whole frozen graph domain, for these b as well as the strong weights.

## Canonical velocity of the compact test

The full-plane logarithmic Green integral for partial_x h is smooth everywhere. Its oddness in x and y follows from the source parity and uniqueness of the specified canonical inverse; its velocity therefore has U1 odd in x and even in y, U2 even in x and odd in y. Near0 the stream is harmonic, since the support is separated from0. Its convergent harmonic Taylor series contains only even sine modes r^n sin(n theta), n=2,4,6,... . The coefficient of the quadratic xy term is Sigma(h). Its vanishing implies psi=O(r^4), with differentiated estimates on smaller discs. Dividing the odd velocity components by their odd coordinates gives smooth even factors

 U1=x v1, U2=y v2,
 |D^alpha v_i|<=C_alpha r^(2-|alpha|), |alpha|<=4, near0.  (4)

This follows also term by term from the convergent Taylor series, whose quotient terms have degree at least2. For orders above the leading degree, the displayed negative powers merely give weaker bounds on bounded derivatives.

At infinity the canonical Green integral has no logarithmic term, because integral partial_x h=0. Its first moments vanish as well:

 integral Y_j partial_x h(Y)dY=-delta_(j1) integral h(Y)dY=0,

where integral h=0 by oddness in y. The Taylor expansion of log|X-Y| for |X| greater than twice the support radius thus starts with order r^-2. The expansion and every fixed derivative converge uniformly there, giving

 |D^alpha psi|<=C_alpha r^(-2-|alpha|),
 |D^alpha U|<=C_alpha r^(-3-|alpha|).                     (5)

Equivalently the exterior harmonic modes start at the decaying n=2 mode. No affine velocity or growing harmonic mode is added. Division by an odd coordinate improves these bounds by a further power:

 |D^alpha v_i|<=C_alpha r^(-4-|alpha|), |alpha|<=4.        (6)

To justify this uniformly near an axis, when |x|<=|y| use U1(x,y)/x=integral_0^1 partial_x U1(tx,y)dt, including its derivatives. Every point(tx,y) has radius comparable to r, so(5) gives(6). When |x|>|y| use direct division and the product rule, since |x|>=r/sqrt2. The argument for U2/y interchanges x and y. The same division formula proves global smoothness of v_i on the axes. Constants may depend on h.

## Exact factor of the nonlocal term

Put g=U[h].grad rho. Direct differentiation gives the exact identity

 g=x^2 y B,
 B=v1(2a+x partial_x a)+v2(a+y partial_y a).               (7)

The x^2 factor is preserved under arbitrarily many y derivatives. This fact avoids trying to control a quotient by using two extra derivatives of rho. Using(1), (4), (6) and the product rule, for |alpha|<=4,

 |D^alpha B|<=C_alpha r^(2-|alpha|), near0,
 |D^alpha B|<=C_alpha r^(k-7-|alpha|), near infinity.      (8)

The constant part of a causes no loss in the center bound. Only derivatives of a through order5 are used. On each compact annulus B is C5. Write E_x=x partial_x. For p+q<=4, identity(7) and(8) imply

 |E_x^p partial_y^q g|<=C x^2 r^(3-q), near0,
 |E_x^p partial_y^q g|<=C x^2 r^(k-6-q), near infinity.   (9)

Expand E_x^p as a finite sum of x^j partial_x^j to see that the x^2 factor survives and each differentiated factor gains enough x<=r powers. These are differentiated bounds, not formal differentiations of undifferentiated estimates.

## Dyadic proof of fractional Sobolev membership

Choose a smooth radial partition sum_(j in Z) chi(2^-j r)=1 on r>0, with chi supported in[1/2,2]. Such a partition follows from chi(r)=eta(r)-eta(2r), where eta is a smooth nonincreasing cutoff equal1 on r<=1 and0 on r>=2. Put lambda=2^j, g_j=chi(r/lambda)g, and F_j=T_b g_j. Differentiating the cutoff leaves(9) valid with r replaced by lambda. The z derivative conjugates to E_x+(1/2-b). Thus, for p+q<=4,

 |partial_z^p partial_y^q F_j|
    <=C_b x^(5/2-b) lambda^(3-q) near0,
 |partial_z^p partial_y^q F_j|
    <=C_b x^(5/2-b) lambda^(k-6-q) near infinity.          (10)

The Jacobian is dzdy=dxdy/x. On the annular support,0<x<2lambda and |y|<2lambda. The exact elementary integral

 integral_0^(2lambda) x^(4-2b)dx
            =(2lambda)^(5-2b)/(5-2b)                    (11)

is finite precisely for b<5/2. Combining(10), (11) and the y interval length gives

 ||partial_z^p partial_y^q F_j||L2
    <=C_b lambda^(6-b-q), for small lambda,
 ||partial_z^p partial_y^q F_j||L2
    <=C_b lambda^(k-3-b-q), for large lambda.             (12)

These are ordinary weak derivatives: on the punctured physical plane all functions have the required classical regularity, the map x=exp z never reaches the vertical axis at finite z, and the displayed bounds make all derivatives through order4 square integrable for each fixed shell. Exact C6 joins prevent interface distributions. For a fixed shell extending to z=-infinity, integrability in(11) suffices; compact support in z is not required. The Fourier derivative characterization then gives F_j in H4.

For small lambda<=1, the H3 and H4 bounds are respectively

 ||F_j||H3<=C_b lambda^(3-b),
 ||F_j||H4<=C_b lambda^(2-b).

The Fourier Hölder inequality, proved by writing the H^s squared integrand as the product of its H3 and H4 integrands with exponents1-theta and theta, yields

 ||F_j||H^(3+theta) <= ||F_j||H3^(1-theta) ||F_j||H4^theta
                      <=C_b lambda^(3-b-theta), theta=3/50.         (13)

Here3-b-theta=6-b-s>11/25>0 for b<5/2. Hence the sum of the H^s norms of all small shells converges geometrically. This interpolation is necessary: H4 membership of the complete center part need not follow when b>=2.

For large lambda>=1, every derivative bound in(12) is at most C_b lambda^(k-3-b). Therefore

 ||F_j||H^s<=||F_j||H4<=C_b lambda^(k-3-b).

Its sum over large shells converges because k<1/2 and b>=0. Finitely many intervening shells have finite H4 norms by the annular regularity and the same x^2 factor argument. Thus sum_j F_j converges absolutely in H^s. The partition is locally finite in(z,y), so its distributional sum equals T_b g. Completeness of H^s proves g inY_(b,s).

## Local terms and application to the exact modal background

The remaining term (ell X+U[rho]).grad h-h has compact support separated from both axes. Local C4 regularity of U[rho] makes its logarithmic transform compactly supported C4, hence inH4 andH^s. The rank-one term vanishes since Sigma(h)=0. The transformed h is smooth compact. This proves(3).

For the actual background, the exact inner factor is1 plus finitely many r^(2j) smooth angular factors, j=1,...,7, and r^bi times log polynomials of degree<=6 with smooth angular factors. Since bi>2, each fixed derivative through5 of the latter is bounded by C r^(2-|alpha|); r^(bi-2)(1+|log r|^6) is bounded near0. This proves the first line of(1) directly even though the homogeneous angular terms need not be Cartesian polynomials. The exact outer factor is a finite sum r^alpha_q times smooth angular factors, with alpha_q<=k-3, plus r^-bo log polynomials. The leading exponent k-3 has no logarithm, and -bo<k-3. Every fixed derivative through5 is bounded by C r^(k-3-|alpha|), proving the second line of(1). The dependent mode-zero normalization coefficient is finite and changes no exponent.

Simple degree-seven spline knots and the exact order-six endpoint matching give the required C6 annular regularity. The canonical background velocity is locally C4, as established for this exact modal density in modal_graph_scaling: rho is locally C^(4,alpha) for each alpha<1, and its canonical Poisson equations give the same local regularity for U. This is a qualitative regularity input; no numerical constant from it is claimed. The parent input chain, exact exponents, degrees and multiplicities will be rehashed and checked by separate data-decoding paths.

No physical residual bound is computed here. In particular this theorem does not establish membership of the actual residual in these spaces, continuity of L in the frozen graph norm, or an inverse on a smaller domain. It answers only the compact-test nonmembership question in the stated nonnegative weak-weight range.
