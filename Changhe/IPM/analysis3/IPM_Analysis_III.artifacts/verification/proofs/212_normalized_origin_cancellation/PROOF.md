# Quadratic smallness from the exact origin cancellation

## Statement

Fix 0<alpha<1. Let E2 be the space of bounded continuous even-x, odd-y functions with h(0,y)=0 and norm

 ||h||E2=||h||infinity+[h]_x+[h]_(y,2),
 [h]_x=sup |h(x,y)-h(x',y)|/|x-x'|^alpha,
 [h]_(y,2)=sup |h(x,y)-h(x,y')|/(|x|^2 |y-y'|^alpha).

Use the canonical IPM velocity U of proof 199, with far subtraction at0, and the exact bounded central strain c of proof 201. Let rho be C^(4,1) on a fixed disk, with the density parities, rho(0,y)=0 and cubic Taylor term x^2 y. Here C^(4,1) means four continuous derivatives with Lipschitz fourth derivatives. Let chi be a fixed smooth radial cutoff, equal1 on B_(1/2) and supported in B1, and let chi_delta(X)=chi(X/delta). There are finite constants C and delta0>0, depending on alpha, the fixed local C^(4,1) bound and chi, such that

 ||chi_delta (U[h]+c[h] X/3).grad rho||E2
                         <=C delta^2 ||h||E2,       (1)

for 0<delta<delta0. The constant is independent of h and delta. No numerical value of C or delta0 is asserted.

For the exact joined normalized modal trial, which is C^(4,1) near0 by proof 33, the power2 is sharp: after decreasing delta0 there is c0>0, independent of delta, such that the norm of the operator on the left of(1) is at least c0 delta^2. The test inputs may be chosen compact smooth with c[h]=J(h)=0. Sharpness concerns the complete E2 norm and this fixed background, not every weaker component seminorm.

The crucial estimates, stronger than a pointwise Taylor expansion, are

 sup_(|x|<=delta,|y|<=2delta)|U2[h](x,y)-c[h]y|
                         <=C M delta^(2+alpha),
 sup_(|x|<=delta)[U2[h](x,.)-c[h](.)]_C^alpha([-2delta,2delta])
                         <=C M delta^2,
 sup_(|x|<=delta,|y|<=2delta)|U1[h](x,y)/x+c[h]|
                         <=C M delta^(1+alpha),
 sup_(|x|<=delta)[U1[h](x,.)/x+c[h]]_C^alpha([-2delta,2delta])
                         <=C M delta,               (2)

where M=||h||E2 and the quotient at x=0 has its continuous extension. These are directional Holder estimates. They do not assert boundedness of h_x or of partial_x U1 on a whole neighborhood. We prove all four estimates below.

## Compact reduction, exact band kernels and the strain sum

Use the fixed product cutoffs of proof 199 and write h=g+(h-g), with g supported in [-4,4]^2, equal to h on [-2,2]^2 and preserving both parities. Then

 ||g(x,.)||infinity+[g(x,.)]_alpha<=C M |x|^2.

The separated far velocity is smooth on a fixed smaller disk, with derivatives of every fixed positive order bounded by C M. Differentiated far kernels are absolutely integrable. Its parities are U1 odd-x/even-y and U2 even-x/odd-y, and it is divergence free. Its Taylor polynomial through degree2 is therefore c_far(-x,y), with no constant or quadratic terms. Taylor's theorem gives the bounds in(2) for that part, with respective stronger sizes delta^3,delta^(3-alpha),delta^2,delta^(2-alpha). Its U1/x quotient is handled by Taylor division in x. These powers imply the stated ones for delta<=1 and alpha<1.

Let g_j be the y-frequency blocks used in proof 199, with lambda=2^j for j>=1. They have y support in a fixed enlarged annulus of size lambda, and

 ||g_j(x,.)||infinity<=C M |x|^2 lambda^(-alpha).

Write

 Q_j=eta^2(-partial_x^2+eta^2)^(-1)g_j,
 U2[g_j]=-g_j+Q_j.                                  (3)

The exact convolution kernel of Q_j has y-integrated absolute value at most C lambda exp(-c lambda|x-x'|). Therefore, for each fixed nonnegative integer k,

 ||partial_y^k Q_j(x,.)||infinity
       <=C_k M lambda^(k-alpha)(x^2+lambda^(-2)).    (4)

Indeed its y derivatives insert lambda^k in the annular kernel estimate, and integration against |x'|^2 gives C(x^2+lambda^(-2)). The same annular derivative estimate for g_j gives

 ||partial_y^k g_j(x,.)||infinity
       <=C_k M |x|^2 lambda^(k-alpha).              (5)

The identity

 partial_x^2 Q_j=eta^2 Q_j-eta^2 g_j                 (6)

holds distributionally and pointwise with a continuous right side. Hence Q_j has two continuous x derivatives. Mixed y derivatives satisfy the same identity. All quantities in(3)-(6) are smooth in y. Parity gives Q_j even in x and odd in y.

Set c_j=partial_y Q_j(0,0). Equation(4) gives

 |c_j|<=C M lambda^(-1-alpha).                       (7)

The low block j=0 satisfies the analogues of(4)-(6) for |x|<=1, with lambda replaced by1 and constants C_k M. One direct check is that its y multipliers, after compact frequency localization, have uniformly bounded H1_eta norms for bounded |x-x'|; the weighted Cauchy-Schwarz bound on their inverse Fourier transforms gives uniform L1 kernels. The compact x support then gives the asserted bounds. Equation(6) and the vanishing g_0(0,y)=0 still apply. Its coefficient is c_0=partial_y Q_0(0,0).

The series of axis derivatives converges uniformly by(4),(7), since g_j(0,y)=0. Thus U2[g](0,y) is differentiable in y, and its derivative at0 is sum_(j>=0)c_j. Proof 201 identifies the actual canonical derivative at0 with c[h]. Consequently

 c[h]=c_far+sum_(j>=0)c_j.                           (8)

This is an absolutely convergent identity, not a formal bandwise subtraction. Compact density parity makes the canonical far-subtraction constants vanish for g, so the compact multiplier and canonical conventions agree.

## Low bands after subtraction of the exact strain

Take 2^N<=1/delta<2^(N+1), with delta<1/4. Initially consider 1<=j<=N, so lambda delta<=1. On |x|<=delta, (4)-(6) give

 ||partial_x^2 partial_y Q_j||infinity
             <=C M lambda^(1-alpha),
 ||partial_y^3 Q_j||infinity
             <=C M lambda^(1-alpha).               (9)

For example, the first bound is lambda^2 times the k=1 bounds for Q_j and g_j; lambda^2 x^2<=1 absorbs the local term. Since Q_j is even in x and odd in y, Taylor expansion first in x and then in y gives

 |partial_y Q_j(x,y)-c_j|
             <=C M (x^2+y^2)lambda^(1-alpha),
 |partial_y^2 Q_j(x,y)|
             <=C M |y| lambda^(1-alpha)             (10)

for |x|<=delta, |y|<=2delta. In the second line use oddness of partial_y^2 Q_j and the second bound of(9). The first line uses the first bound of(9) for the x difference, and the second bound for the even-y function partial_y Q_j on x=0.

Define W_j=U2[g_j]-c_j y. From(5),(10),

 ||partial_y W_j||infinity
             <=C M delta^2 lambda^(1-alpha),
 ||W_j||infinity
             <=C M delta^3 lambda^(1-alpha).        (11)

The second line uses oddness in y. The same bounds with lambda=1 apply to the low block. Summing through N uses

 sum_(j=1)^N lambda^(1-alpha)<=C_alpha delta^(alpha-1).

Thus the low part of W has supremum at most C M delta^(2+alpha), derivative in y at most C M delta^(1+alpha), and Holder seminorm on the interval [-2delta,2delta] at most C M delta^2.

For the first velocity quotient put Z_j=U1[g_j]/x+c_j. Divergence freedom and oddness of U1 in x give exactly

 Z_j(x,y)=-integral_0^1 [partial_y U2[g_j](t x,y)-c_j]dt. (12)

Each band has a continuous x derivative of U1 by its exact partial-Fourier formula, so this identity is pointwise and extends to x=0. Equations(5),(10) give

 ||Z_j||infinity<=C M delta^2 lambda^(1-alpha),
 ||partial_y Z_j||infinity
       <=C M (delta^2 lambda^(2-alpha)
                           +delta lambda^(1-alpha))
       <=C M delta lambda^(1-alpha).               (13)

In the last step lambda delta<=1. Summing the low bands gives supremum C M delta^(1+alpha), y derivative C M delta^alpha and local Holder seminorm C M delta. This proves the low parts of both quotient estimates in(2).

## High bands and their subtracted constants

For j>N, equation(3), the kernel moment bound and(5) give uniformly on |x|<=delta

 ||U2[g_j](x,.)||infinity<=C M delta^2 lambda^(-alpha). (14)

The dyadic Holder reconstruction of proof 199 then bounds the entire high sum's y Holder seminorm by C M delta^2 and its supremum by C M delta^(2+alpha). This assertion uses the band structure of the sum, not the sum of individual Holder seminorms.

Proof 199's exact first-component band estimates at p=2 imply

 ||U1[g_j](x,.)/x||infinity<=C M delta lambda^(-alpha),
                                  |x|<=delta.       (15)

To see the uniformity, if lambda|x|<=1, integrate the band x derivative from0 to x, obtaining C M lambda^(-1-alpha). If lambda|x|>=1, divide its direct bound C M lambda^(-alpha)(x^2+lambda^(-2)) by |x|, obtaining C M |x| lambda^(-alpha). Since lambda>1/delta, either estimate is at most the right side of(15). The quotient is band-limited in y. Dyadic reconstruction therefore gives y Holder seminorm C M delta and supremum C M delta^(1+alpha) for the high sum.

Equation(7) also gives

 |sum_(j>N)c_j|<=C M delta^(1+alpha).                (16)

Subtracting this constant times y in the U2 sum costs at most C M delta^(2+alpha) in supremum and C M delta^2 in the local Holder seminorm. Adding it as a constant to the first quotient costs only C M delta^(1+alpha) in supremum and nothing in the seminorm. Combining the low, high and separated far parts with(8) proves every estimate in(2).

## Background division and the normalized product

Taylor division gives rho_x=x a1 and rho_y=x^2 a2, with

 a1=2y+e1, |e1|<=C r^3, |De1|<=C r^2,
 a2=1+e2, |e2|<=C r^2, |De2|<=C r.                (17)

Here is why the stated C^(4,1) regularity suffices. The even-x, odd-y function rho_xx has Taylor polynomial 2y through degree2 and a C^(2,1) remainder. Integrating rho_xx(t x,y) in t proves the first line. The even-x, even-y function rho_xxy has Taylor polynomial2 through degree1 and a C^(1,1) remainder. Integrating (1-t)rho_xxy(t x,y) proves the second. All constants are uniform on a smaller fixed disk.

Let Z=U1/x+c[h] and W=U2-c[h]y. Then the normalized coupling is exactly

 chi_delta(U+cX/3).grad rho
   =x^2 chi_delta {a1 Z+a2 W+c E},
 E=-(2/3)a1+(4/3)y a2
   =-(2/3)e1+(4/3)y e2.                            (18)

The linear terms in E cancel exactly. By(17), |E|<=C r^3 and |DE|<=C r^2. By proof 200 at p=2, |c[h]|<=(4/pi)M.

On |x|<=delta, |y|<=2delta, equations(2),(17) imply

 ||a1 Z+a2 W||infinity<=C M delta^(2+alpha),
 [a1 Z+a2 W]_(C^alpha_y)<=C M delta^2.              (19)

For the a1 product, its supremum O(delta) multiplies [Z]_alpha=O(Mdelta); its coefficient seminorm O(delta^(1-alpha)) multiplies ||Z||infinity=O(Mdelta^(1+alpha)). Both give O(Mdelta^2). For the a2 product, its bounded supremum multiplies [W]_alpha=O(Mdelta^2); its bounded derivative and ||W||infinity give a smaller contribution. The cE term has supremum O(Mdelta^3) and seminorm O(Mdelta^(3-alpha)), bounded by the respective right sides of(19) for alpha<1.

Multiplication by chi_delta preserves the bound C M delta^2 in the y Holder seminorm: [chi_delta]_alpha=O(delta^(-alpha)) multiplies the supremum O(Mdelta^(2+alpha)). For pairs with one point outside [-2delta,2delta] and one on the cutoff support, the distance is at least delta and the same supremum gives that bound. Pairs with both values zero contribute nothing. Dividing(18) by x^2 thus proves the complete global weighted y seminorm bound in(1).

The ordinary supremum and x seminorm need no improved velocity remainder estimate. On B_delta, |U|<=C M delta by proof 203 and |grad rho|<=C delta^2. Ordinary local C^alpha control of U from proof 199 gives

 ||chi_delta U.grad rho||infinity<=C M delta^3,
 [chi_delta U.grad rho]_x<=C M delta^2.

For the second estimate use product differences, evaluating the undifferenced velocity at a supported point. The coefficient chi_delta grad rho has supremum O(delta^2) and C^alpha norm O(delta^(2-alpha)). The local velocity difference has bound CM; the other term is O(Mdelta^(3-alpha)), which is at most C M delta^2. Pairs outside a fixed local neighborhood use the supported supremum. The column c chi_delta X.grad rho/3 has supremum O(Mdelta^3) and ordinary x seminorm O(Mdelta^(3-alpha)), also at most C M delta^2. Combining these estimates with the weighted y estimate proves(1).

## Sharpness on the actual modal background

Put q_delta=delta/8 and choose Q_delta=(q_delta,q_delta) and a fixed small b>0. For sufficiently small delta, four disks of radius b delta around Q_delta and its reflections are disjoint, avoid the axes, and lie in B_(delta/2). Let chiQ be a smooth cutoff supported in the first disk and equal1 on a smaller disk. For 0<epsilon<<delta put on that disk

 P_epsilon(X)=epsilon^(alpha+2)
        cos((x-q_delta)/epsilon) chiQ(X),
 d_epsilon=-Delta P_epsilon,

then extend P_epsilon evenly in x and oddly in y to the reflected disks. Set the density d_epsilon by the Laplacian of the full reflected potential. These are compact smooth functions supported away from0. Exactly

 U[d_epsilon]=(-partial_x partial_y P_epsilon,
                      partial_x^2 P_epsilon),
 c[d_epsilon]=J(d_epsilon)=0.                       (20)

The strain vanishes because this exact compact velocity vanishes near0, or by integrating its harmonic strain kernel against -Delta P_epsilon.

For epsilon<=delta, direct cutoff differentiation gives sup|d_epsilon|<=C epsilon^alpha and x Lipschitz norm at most C epsilon^(alpha-1), so [d_epsilon]_x<=C. At fixed x, all y derivatives fall on cutoffs, giving [d_epsilon(x,.)]_alpha<=C epsilon^alpha delta^(-alpha). Nonzero vertical lines have |x|>=c delta. Consequently

 ||d_epsilon||E2<=C[1+epsilon^alpha delta^(-2-alpha)]. (21)

For example choose epsilon so small that epsilon^alpha<=delta^(2+alpha). The right side is uniformly bounded in delta. Both points X0=Q_delta and X1=Q_delta+(pi epsilon,0) may also be placed in the smaller cutoff plateau.

On that plateau P_xy=0, P_xx=-epsilon^alpha cos((x-q_delta)/epsilon) and chi_delta=1. By(20) the normalized coupling there equals P_xx rho_y. Equation(17) gives rho_y(Xi)>=c delta^2 for i=0,1, uniformly for small delta and epsilon/delta. Thus its values at these two points differ in absolute value by at least c epsilon^alpha delta^2. Their horizontal distance is pi epsilon, and hence its x Holder seminorm is at least c' delta^2. Together with(21) this proves the operator lower bound c0 delta^2. No plane-wave approximation or limiting pseudodifferential symbol is used.

## Consequences and limits

For the frozen normalized origin extension, write K0=max(1,1/[D0(1-alpha)]), D0=2A0+1. If C delta^2 K0<1, its maximal E2 inverse has norm at most

 K0/(1-C delta^2 K0).

Its strain on a solution therefore satisfies |c[h]| <= (4/pi)K0 ||L_delta h||E2/(1-C delta^2 K0). C remains a finite qualitative coefficient, so this is not a numerical inverse certificate. For the actual-variable extension of proof 202, substitute the new normalized coupling bound into its exact factorization. The perturbation is now bounded by

 C_M delta^(2-alpha)+(q0+C_M delta^(2-alpha))C delta^2,

which tends to0. Its maximal domain is unchanged. No original full-plane inverse, closed cubic constraint or nonlinear existence follows. Topics204 and207 continue to give the graph normalization and semilinear nonlinear obstructions.

The proof uses proof 199's explicit kernels and local ordinary Holder bound, proof 201's canonical strain identity, proof 203's endpoint space, and proof 33's actual C^(4,1) background regularity. Every improved band subtraction, cutoff norm, background cancellation and sharpness step is proved above. No numerical calculation is required. Independent independent cross-audit is requested before integration.
