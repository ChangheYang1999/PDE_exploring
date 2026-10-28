# Quadratic vertical vanishing is the largest preserved power

## Statement

Fix 0<alpha<1 and p>2. Define E_p as in proof 215, with the weighted y seminorm divided by |x|^p. Let rho0 be the exact joined normalized modal density. Let V be either its actual transport or an origin extension agreeing with it near0, and let chi_delta be a smooth radial cutoff equal1 near0. Every global chart column below uses the canonical physical central strain c.

There exists h in C_c^infinity intersect E_p, compactly supported away from both axes and the origin, with exact J(h)=c[h]=0, such that its transport image (V.grad-1)h belongs to E_p, but

 chi_delta {U[h].grad rho0+c[h]M} does not belong to E_p (1)

for every column M for which the expression is defined. In particular (1) holds for the leading normalized column X.grad rho0/3 and for the exact moving-tail M0. It also holds without chi_delta for the full actual expression. Adding an L2 factor with any smooth positive radial weight does not repair this failure of the E_p factor.

Thus the bounded-coupling realization on the pure transport domain cannot be extended from p=2 to p>2. This concerns that specified space and domain, not every possible stronger anisotropic norm or a full inverse on a different domain. The result is exact, not a numerical observation.

## Independent velocity moments

For a compact smooth input supported away from0, the local multiplier term of U2 vanishes near0, and its nonlocal kernel is

 K2(X)=(x^2-y^2)/(2pi |X|^4)=Re((x+iy)^(-2))/(2pi).

Differentiating this explicit kernel in y and evaluating at -Y gives

 partial_y K2(-Y)=sin(3theta)/(pi r^3),
 partial_y^3 K2(-Y)=-12 sin(5theta)/(pi r^5).

All derivatives may be passed through the separated integral. Therefore

 c[h]=partial_y U2[h](0)
     =(1/pi) integral sin(3theta) r^(-3)h(Y)dY,
 b[h]=partial_y^3 U2[h](0)/6
     =-(2/pi) integral sin(5theta) r^(-5)h(Y)dY.    (2)

Choose a nonnegative nonzero smooth bump in a small first-quadrant disk about angle pi/6, radius between1 and2, where both sin(3theta) and sin(5theta) are positive. Reflect it evenly in x and oddly in y, to obtain H. The two sine factors have exactly that same parity. Hence c[H]>0 and b[H]<0. Its support is separated from both axes.

For a fixed a>1 define H_a(X)=H(X/a). Exact homogeneity in (2) gives

 c[H_a]=a^(-1)c[H], b[H_a]=a^(-3)b[H].

The input

 h=H-a H_a

is compact, smooth, physical-parity compatible, vanishes near both axes and0, and satisfies

 c[h]=0, b[h]=(1-a^(-2))b[H]!=0, J(h)=0.            (3)

It belongs to E_p for every finite p because every vertical line meeting its support has |x| bounded below. Its actual transport image has the same compact support and is smooth; choose the initial bump radii away from the finitely many radial joins if desired. The actual C3 transport regularity alone already supplies the C^alpha bounds needed. An origin-extended transport has the same property. Thus this image is in E_p as claimed.

## Failure at the vertical axis after exact strain cancellation

The velocity of h is smooth near0. Physical parity makes U2 even in x and odd in y, and U1 odd in x and even in y. Equation (3) removes the linear part. Along the vertical axis,

 U2(0,y)=b y^3+O(y^5),
 U1(x,y)/x at x=0=-partial_y U2(0,y)
                     =-3b y^2+O(y^4),              (4)

where b=b[h]!=0. The second identity is incompressibility and division by the odd x factor. The compact separated kernel gives every remainder derivative used here.

Proof 212's actual C^(4,1) density division gives, on that axis,

 (rho0_x/x)(0,y)=2y+O(y^3),
 (rho0_y/x^2)(0,y)=1+O(y^2).

Thus the continuously divided image has axis value

 lim_(x->0) U[h].grad rho0(x,y)/x^2
 =(-3b y^2+O(y^4))(2y+O(y^3))
       +(b y^3+O(y^5))(1+O(y^2))
 =-5b y^3+O(y^5).                                  (5)

Choose a sufficiently small fixed y0>0, inside the region where chi_delta=1, so that (5) is nonzero. The image is odd in y and vanishes at y=0. Consequently its weighted vertical difference between y0 and0 has size comparable to

 |x|^(2-p) |5b y0^3+O(y0^5)|/y0^alpha

as x tends to0. This tends to infinity because p>2. The cutoff is1 at the tested points for all sufficiently small x. The entire normalization column is zero because c[h]=0, so it cannot change the conclusion, regardless of which exact column M is used.

The transport image of h vanishes near0 and cannot cancel (5). Thus the full operator applied to this smooth transport-domain input fails membership in E_p. The maximal domain of a possible full E_p realization must be a proper restriction of that transport domain. Proof 214's p=2 mapping is consistent: the same x^2 image is then permitted. The proof identifies a membership obstruction, not merely a poor bound.

Dependencies: proof 212 for the actual background division and proof 01 for the velocity convention. Kernel differentiation, independent moments, exact zero-strain construction and all domain statements are proved above. No numerical computation is used.
