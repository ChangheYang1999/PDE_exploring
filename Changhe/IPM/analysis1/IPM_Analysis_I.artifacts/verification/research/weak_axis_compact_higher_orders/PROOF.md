# Compact zero-strain tests at higher Sobolev orders

This proof answers the lead's 2026-10-22T04:36Z question about weak_axis_compact_mapping. It is written before new checks and review. It strengthens only the range of Sobolev orders for the same compact test class; it supplies no uniform operator norm or inverse.

## Statement and inputs

Let rho=x²y a(x,y) be the exactly joined and normalized canonical modal_v2 density. Its exponent is k=1615536043799051/9007199254740992 in(0,1/2). Its factor a is even in each coordinate, is C6 on compact annuli, and is piecewise smooth across finitely many circles on each compact annulus. This includes the two exactly matched endpoints of the degree-seven log-radial spline. The inner and outer representations are finite sums of powers times log polynomials with smooth angular factors, as specified in canonical_residual_weak_axis_membership. Use the canonical inverse -Delta psi[f]=partial_x f and U[f]=(-psi_y,psi_x), with no harmonic addition.

Let h be real smooth compact, even in x, odd in y, and supported at positive distance from both coordinate axes. Suppose Sigma(h)=psi[h]_xy(0)=0. All its center jets vanish, including J(h)=partial_xxy h(0)/2. For any fixed real ell, put

 Lh=(ell X+U[rho]).grad h-h+U[h].grad rho+(Sigma(h)/3)X.grad rho.

On x>0 set z=log x and T_b f=x^(1/2-b)f(x,y), with ||f||Y_(b,s)=||T_b f||H^s(R²_(z,y)); the squared Fourier weight is(1+xi²+eta²)^s. Then

 0<=b<5/2 and0<=s<6-b imply h,Lh belong toY_(b,s).       (1)

Consequently, for each fixed0<=s<=7/2, among the nonnegative weights b the entire compact annular zero-strain test class maps intoY_(b,s) exactly when b<5/2. Necessity at b>=5/2 is the already accepted explicit counterexample of axis_weighted_nonlocal_mapping, which fails the zeroth norm and therefore every H^s norm. For orders above7/2 only the sufficient region in(1) is asserted. Neither the critical line s=6-b nor any negative b is classified.

## Annular weak derivatives through order six

The finite actual factor a has bounded derivatives of every fixed order on each closed smooth piece of a compact annulus. Its derivatives through order6 match across each interface circle. Therefore a belongs to W^(7,infinity) locally on the annulus. To justify the weak-derivative statement, integrate by parts on each side of an interface. The boundary terms for one derivative of a continuous piecewise C1 function cancel because the two traces agree and the normals have opposite signs. Apply this successively to derivatives through order6. At order7 the weak derivative equals the bounded piecewise classical derivative; no surface measure appears. Smooth polar coordinate changes are nonsingular on an annulus. There are only finitely many pieces there.

The compact test velocity U[h] is smooth everywhere by the logarithmic Green integral, or by differentiation after transferring derivatives to the smooth compact source. Its parity implies U1=x v1 and U2=y v2 with smooth even factors v1,v2. The division identities U1/x=integral_0^1 partial_x U1(tx,y)dt and U2/y=integral_0^1 partial_y U2(x,ty)dt give their smoothness also at nonzero axis points. Hence

 g=U[h].grad rho=x²y B,
 B=v1(2a+x a_x)+v2(a+y a_y)                             (2)

belongs locally to W^(6,infinity) on annuli. The exact x² factor survives every y derivative. This is the extra derivative input needed beyond the H3/H4 argument of result202; C5 alone would not suffice for the present conclusion.

The local transport term also has enough annular regularity. The background density has finitely many angular modes and is C6 in the radial coordinate on each annulus. Each source mode of partial_x rho is C5. Its radial Poisson equation is a second-order ODE with smooth coefficients away from r=0. Starting from the Green solution, differentiating the ODE successively gives psi-mode C7, and thus U[rho] C6 on the annulus. The finite sum retains this regularity. Multiplying by derivatives of compact h gives a compact C6 function supported away from both axes. Its logarithmic transform has weak derivatives through6 in L2 and belongs to H6. The transformed h is smooth compact. Thus only g needs center and infinity estimates.

## Differentiated estimates for the nonlocal term

The explicit inner factor equals1 plus finitely many homogeneous smooth angular terms of degrees2,4,...,14 and terms r^bi times log polynomials of degree at most6, with bi>50. The explicit outer factor is a finite sum of powers whose largest degree is k-3, with no logarithm at that leading power, plus r^-bo log polynomials with bo>120. Direct differentiation on each end therefore gives, for all Cartesian multi-indices alpha with |alpha|<=7,

 |D^alpha(a-1)|<=C_alpha r^(2-|alpha|) near0,
 |D^alpha a|<=C_alpha r^(k-3-|alpha|) near infinity.      (3)

A finite angular function is smooth on the circle, and each Cartesian derivative lowers the radial degree by one and differentiates that angular function. Logarithms at the faster powers remain absorbed by their strictly positive degree gaps. These bounds do not claim C7 at0.

Since Sigma(h)=0 and h vanishes near0, its harmonic stream expansion starts at degree4. At infinity its source has zero integral and zero first moments: integral partial_x h=0 and integral Y_j partial_x h=-delta_(j1) integral h=0 by oddness in y. Its convergent exterior harmonic expansion therefore starts at degree-2. Differentiating these convergent harmonic expansions and dividing the odd velocity coordinates as in result202 gives, now through order6,

 |D^alpha v_i|<=C_alpha r^(2-|alpha|) near0,
 |D^alpha v_i|<=C_alpha r^(-4-|alpha|) near infinity.     (4)

For division near an axis use the integral formula on the cone where the undivided coordinate keeps the radius comparable; on the other cone direct division is allowed by |x| or |y|>=r/sqrt2. Derivatives of U through7 suffice and follow from the harmonic expansions. No new regularity premise is added to h.

Equations(2)--(4), by the product rule through6, give |D^alpha B|<=C r^(2-|alpha|) near0 and <=C r^(k-7-|alpha|) near infinity. For E_x=x partial_x and p+q<=6 this implies

 |E_x^p partial_y^q g|<=C x² r^(3-q) near0,
 |E_x^p partial_y^q g|<=C x² r^(k-6-q) near infinity.     (5)

The derivative order on a is at most7. On intermediate annuli the derivatives are interpreted weakly using the matching argument above.

## Shell summation for arbitrary s in the stated region

Take a smooth radial dyadic partition sum_j chi(2^-j r)=1 for r>0, with chi supported in[1/2,2], and write lambda=2^j, F_j=T_b(chi(r/lambda)g). Conjugation of partial_z gives E_x+(1/2-b). The Jacobian dzdy=dxdy/x and the factor x² give the axis integral

 integral_0^(2lambda) x^(4-2b)dx=(2lambda)^(5-2b)/(5-2b),

which is finite for b<5/2. Bounds(5), with the cutoff differentiated, imply for p+q<=6

 ||partial_z^p partial_y^q F_j||L2<=C_b lambda^(6-b-q), lambda<=1,
 ||partial_z^p partial_y^q F_j||L2<=C_b lambda^(k-3-b-q), lambda>=1. (6)

There are no interface distributions in these weak derivatives because g is annular W^(6,infinity). For a fixed shell x approaches0 only as z approaches-infinity, so the finite axis integral supplies all required integrability. Thus each F_j belongs to H6. For every integer0<=n<=6, (6) and the Fourier derivative characterization yield

 ||F_j||H^n<=C_b,n lambda^(6-b-n), lambda<=1,
 ||F_j||H^n<=C_b,n lambda^(k-3-b), lambda>=1.            (7)

For a noninteger0<s<6, choose n=floor(s) and theta=s-n in(0,1). Fourier Holder gives ||F_j||H^s<=||F_j||H^n^(1-theta)||F_j||H^(n+1)^theta. The center exponent becomes6-b-s. The same formula at integer s uses(7) directly, including s=0. Under(1), s<6, so no order above6 is required. Therefore

 ||F_j||H^s<=C_b,s lambda^(6-b-s) near0,
 ||F_j||H^s<=C_b,s lambda^(k-3-b) near infinity.         (8)

The first exponent is strictly positive by(1), and the second is strictly negative because b>=0 and k<1/2. Both series of shell norms converge. Finitely many intervening shells lie in H6 by the annular argument. The sum converges absolutely in H^s; local finiteness of the partition identifies it with T_b g. The remaining transport term and h already lie in H6 after transformation, and the rank-one term vanishes. This proves(1).

If0<=s<=7/2 and b<5/2, then6-b-s>=7/2-s+(5/2-b)>0, so(1) holds. The inherited nonzero x²-axis coefficient counterexample excludes every b>=5/2 for these orders. This proves the stated exact weight threshold for this range of orders. No endpoint regularity at s=6-b, uniform norm in h, closed graph extension, inverse, or PDE conclusion follows. In particular the variable-transport obstruction199 at s=153/50 remains unchanged.

## Verification plan and dependencies

The analytic proof uses the canonical finite modal representations, exact order-six matching, compact harmonic expansions and the already checked strong-axis counterexample. Fresh independent data checks will read the exact NPZ binary64 coefficients as Fractions versus manually decoded hexadecimal JSON as fmpq, checking the degree, knot multiplicities, all end exponents and strict gaps. Independent finite checks of the x² factor identities through6 and the exponent arithmetic are diagnostics of the written calculation, not a finite proof of the analytic statement. No new interval enclosure, numerical quadrature, physical norm ceiling or heavy job is needed. Complete actual Claude Opus5.5 review of the proof and later own adjudication are required before the theorem is marked CONFIRMED.
