# Small coupling at the quadratic Holder weight

## Statement

Let 0<alpha<1 and 1<=p<=2. Use the exact Banach space E_p, canonical velocity U, C4 background rho and reflection-invariant cutoff chi_delta of proof 199. There is a finite C, depending only on alpha,p and the fixed local background and cutoff, such that for all sufficiently small delta>0,

 ||chi_delta U[h].grad rho||_(E_p)
             <=C delta^(3-p-alpha)||h||_(E_p).        (1)

The normalized coupling obeys the same power:

 ||chi_delta(U[h]+c[h]X/3).grad rho||_(E_p)
             <=C_norm delta^(3-p-alpha)||h||_(E_p).   (2)

Thus p=2 is allowed with the strictly positive power 1-alpha. For p=2 the strain functional bound of proof 200 reduces to ||c||_(E_2*)<=4/pi. There is no need for a derivative of h in these norms. These inequalities strengthen proof 199's O(delta^(2-p)) estimate; that earlier estimate did not give smallness at p=2.

Consequently the normalized frozen operator of proof 200 and the localized variable-origin operator of proof 202 are both invertible on E_2, on their stated maximal distributional domains, for sufficiently small delta and every fixed alpha<1. Their inverse norms are uniformly bounded as delta tends to0. These are qualitative theorems for the specified localized operators, with no certified numerical radius. The original full-plane operator, closed cubic normalization and nonlinear existence are not included.

## The additional local velocity estimate

The only improvement needed is

 sup_(|x|<=delta, |y|<=2delta)|U2[h](x,y)|<=C M delta,
 sup_(|x|<=delta)[U2[h](x,.)]_(C^alpha([-2delta,2delta]))
                                            <=C M delta^(1-alpha), (3)

where M=||h||_(E_p). Proof 199 already proves uniformly on a fixed neighborhood that U1/x has bounded supremum and bounded y Holder seminorm, both at most C M. That result includes p=2.

For completeness use the same compact reduction as proof 199: g=chi_x chi_y h, with fixed cutoffs equal1 on[-2,2] and supported in[-4,4]. Its separated far velocity has uniformly bounded derivatives through order2. Its second component is odd in y, so it meets(3). It suffices to handle g.

Let g_j be the dyadic y-frequency blocks of proof 199, lambda=2^j for j>=1. The weighted input estimate and the band kernel of

 U2=-I+eta^2(-partial_x^2+eta^2)^(-1)

give the sharper form of its block estimate

 ||U2[g_j](x,.)||_infinity
     <=C M lambda^(-alpha)(|x|^p+lambda^(-p)).         (4)

Indeed the identity term uses ||g_j(x,.)||_infinity<=C M |x|^p lambda^(-alpha). The convolution term has y-integrated absolute kernel bounded by C lambda exp(-c lambda|x-x'|), and integration against |x'|^p gives C(|x|^p+lambda^(-p)). This proves(4) for every 1<=p<=2. The low block has a uniformly bounded y derivative on |x|<=1 by the low-frequency argument of proof 199. All these U2 blocks are odd in y.

Choose N>=1 so that 2^N<=1/delta<2^(N+1), shrinking delta below1/4. Split the velocity into the low sum j<=N and the high sum j>N. A slightly larger frequency cutoff gives Bernstein's bound

 ||partial_y U2[g_j](x,.)||_infinity
   <=C M lambda^(1-alpha)(delta^p+lambda^(-p)),
   |x|<=delta.

Summing through N bounds the first part by C M delta^(p+alpha-1) and the second by C M sum_(j>=1)2^((1-p-alpha)j). The latter converges because p+alpha>1. Both bounds are uniform as delta tends to0. Including the low block, the whole low sum has y derivative at most C M. Oddness implies it vanishes at y=0. Its supremum on |y|<=2delta is therefore at most C M delta, and its alpha seminorm on that interval is at most C M delta^(1-alpha).

For the high sum, lambda>1/delta implies lambda^(-p)<delta^p. Equation(4) becomes

 ||U2[g_j](x,.)||_infinity<=C M delta^p lambda^(-alpha).

The elementary dyadic characterization proved in proof 199 bounds the global y alpha seminorm of this sum by C M delta^p, uniformly for |x|<=delta. Summing the supremum bounds gives C M delta^(p+alpha). Since p>1-alpha and p+alpha>1, these are bounded respectively by C M delta^(1-alpha) and C M delta. This proves(3). The split depends on delta, but its constants do not. No derivative of the entire high-frequency velocity is asserted.

## Product estimates

As in proof 199, Taylor division of the C4 background gives

 rho_x=x a1, rho_y=x^2 a2,
 ||a1||_(infinity,B_(3delta))<=C delta,
 ||Da1||+||a2||+||Da2||<=C.

Write V1=U1/x, including its continuous extension on x=0. The coupling is

 chi_delta U[h].grad rho
           =x^2 chi_delta(a1 V1+a2 U2).              (5)

On the relevant small y interval, the first coefficient on the right has alpha seminorm at most C M delta^(1-alpha), by the fixed-neighborhood bound for V1 and the cutoff difference. Equation(3) gives the same estimate for the second coefficient: its ordinary cutoff seminorm O(delta^(-alpha)) multiplies an O(M delta) supremum, and its U2 difference is already O(M delta^(1-alpha)). Thus

 [chi_delta U[h].grad rho]_(y,2)<=C M delta^(1-alpha).

This is a global y seminorm after extension by0. For pairs inside[-2delta,2delta] use the preceding product bound. If one point lies outside that interval and the other lies on the cutoff support, their separation is at least delta and the coefficient's supported supremum is O(M delta), giving the same quotient bound. Pairs where the supported expression is zero need no estimate. Since its x support is |x|<=delta,

 [chi_delta U[h].grad rho]_(y,p)
                         <=C M delta^(3-p-alpha).    (6)

Also |U1|<=C M delta by the bound for U1/x, and |U2|<=C M delta by(3). The coupling's supremum is O(M delta^3). Its x Holder seminorm is at most C M delta^2: use the ordinary local C^alpha bound for U from proof 199, the O(delta^2) supremum of chi_delta grad rho, and its O(delta^(2-alpha)) Holder bound multiplied by the O(M delta) velocity supremum. Pairs outside a fixed larger neighborhood are covered by the supported supremum. For 1<=p<=2 and alpha<1, the power 3-p-alpha is positive and less than2. These supremum and x bounds, together with(6), prove(1).

Proof 200 proves that H_delta=chi_delta X.grad rho/3 has E_p norm at most C_H delta^(3-p-alpha). Its strain functional estimate was proved for the same input norm and remains valid at p=2, since p+alpha>1. Combining those two estimates with(1) proves(2). Proof 201 verifies that c is the actual canonical central strain for these inputs.

## Frozen and variable transport at p=2

For the frozen transport T0=-A0 x partial_x+D0 y partial_y-1, D0=2A0+1, its exact criterion at p=2 is

 kappa_2=1+2A0-alpha D0=D0(1-alpha)>0.

Proof 25's inverse on the maximal E_2 domain therefore has norm at most max(1,1/[D0(1-alpha)]). The normalized coupling in(2) tends to0 as delta tends to0, so a Neumann series gives the frozen assertion on the identical domain.

For the variable extension of proof 202, its direct characteristic estimates(3)-(12) require p>0 and kappa=q0+p-alpha L>0; none requires p<2. That restriction entered there only through the earlier coupling estimate. At p=2,

 kappa0=q0+2-alpha beta0=beta0(1-alpha)>0,
 q0=1/A0, beta0=D0/A0.

The cutoff coefficients still give L<=beta0+C delta^2 and uniformly bounded characteristic inverse norm C_R for small delta. The exact maximal-domain and multiplier identities are unchanged. Replace proof 202's bound(14) by

 ||E_delta||<=C_M delta^(2-alpha)
       +(q0+C_M delta^(2-alpha)) C_norm delta^(1-alpha).

It tends to0 for every fixed alpha<1. The same Neumann factorization proves the E_2 inverse. This application uses the whole-plane extension defined there, equal to the actual operator only in B_(delta/2). It does not assert a bounded transfer by a spatial conjugacy.

## Scope and dependencies

Topics199-201 establish the precise norms, band kernels, canonical strain and background factorization; the additional short-interval velocity estimate is proved here. Proof 25 supplies the exact frozen maximal resolvent, and proof 202 supplies the directly checked variable-flow estimate and domain factorization. There is no numerical calculation. The E_2 origin weight expresses quadratic vanishing in x in the y seminorm; it does not prescribe a cubic Taylor coefficient. A separate proof below the reading-order index records why that coefficient is not closed even in these local graph norms. An independent cross-audit of this endpoint strengthening is requested.
