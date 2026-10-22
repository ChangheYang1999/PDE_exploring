# A compact perturbation whose nonlocal image fails strong axis-weighted integrability

Date 2026-10-22T02:46:25.142827+00:00. This standalone proof is written before the new algebra and application checks. The theorem and canonical-modal application remain OPEN until independent checks, complete actual Claude Opus5.5 review and later own adjudication. This result concerns the full operator's mapping of a natural test class, not failure of its inverse on every restricted domain.

## Statement, background and space

Let rho be even in x and odd in y, locally C3 near0, and satisfy

 rho=x^2y+R, |D^j R|<=C r^(5-j), 0<=j<=3,
 rho(0,y)=0 for sufficiently small y.                       (1)

For the canonical modal background the last condition follows from its explicit continuous x^2y factor. Let U[rho] be the specified canonical velocity wherever needed. For a compact perturbation h, use U[h]=(-psi_y,psi_x), -Delta psi=partial_x h with the canonical full-plane inverse, Sigma(h)=psi_xy(0), and

 L_rho h=(ell X+U[rho]).grad h-h+U[h].grad rho
                                      +(Sigma(h)/3)D rho.   (2)

Only its near-center expression is needed below, so ell is arbitrary. Define J(h)=partial_xxy h(0)/2; any normalization depending only on center jets has the same value for the constructed h.

For a real and s>=0, let Y_(a,s) be the logarithmic pullback space of anisotropic_frozen_transport_inverse: T_a h(z,y)=exp((1/2-a)z)h(exp(z),y) lies in H^s(R^2_(z,y)) on x>0. Its norm dominates integral_(x>0) x^(-2a)|h|^2 dxdy. The asserted membership is always for restriction of a physical perturbation to this half-plane.

There exists a fixed h in C_c^infinity(R^2), supported in1<r<2 and at positive distance from both coordinate axes, with even-x/odd-y parity and a smooth global x^2y factor, such that

 J(h)=Sigma(h)=0,
 h|_(x>0) belongs to Y_(a,s) for every finite real a and s>=0,
 (L_rho h)|_(x>0) does not belong to Y_(a,s)
                    for every a>=5/2 and every s>=0.        (3)

The nonmembership already holds on a small rectangle adjacent to x=0 with y strictly positive. It therefore does not depend on any behavior at infinity. In particular, the full operator does not map this natural smooth compact zero-jet/zero-strain test class into Y_(6,153/50), although the frozen operator has the proved inverse there. This does not preclude a full inverse on a smaller maximal domain that excludes this h.

## A perturbation with exactly zero third mode and positive fifth mode

Choose a nonnegative smooth function phi(theta) on the circle, invariant under theta->-theta and theta->pi-theta, zero on neighborhoods of both coordinate axes, and positive on a nonempty open arc in the first quadrant. One construction is to take a nonnegative smooth bump supported inside a small open arc strictly inside the first quadrant and sum its images under these two reflections. Choose eta>=0 in C_c^infinity((1,2)), integral eta dr=1, and put chi(r)=r^4 eta(r).

For i,j in{3,5}, define the exact real Gram entries

 M_ij=(1/pi)integral_0^(2pi) phi(theta)sin(i theta)sin(j theta)dtheta.

The matrix M is positive definite. Indeed its quadratic form is the integral of phi times the square of v3 sin3theta+v5 sin5theta. If it vanishes, that trigonometric polynomial vanishes on an open arc. A trigonometric polynomial vanishing on an arc is identically zero: multiply by a suitable power of exp(i theta) to obtain a polynomial with infinitely many distinct roots. Its distinct sine frequencies then imply v3=v5=0. In particular M33>0 and

 gamma=M55-M35^2/M33>0.

These are exact definitions and strict analytic inequalities, not numerically computed inverse-matrix entries. Define c=M35/M33 and

 h(r,theta)=chi(r) phi(theta)[sin5theta-c sin3theta].          (4)

The reflection invariances make h even in x and odd in y. Its compact support avoids both axes and0, so division by x^2y on that support extends by0 to a global smooth factor. All center jets vanish. Under the standard density sine convention F_l(r)=(1/pi)integral h(r,theta)sin(l theta)dtheta, equation(4) gives exactly

 F3=0, F5=gamma chi.                                       (5)

Other odd sine modes may be present. They are not truncated or assumed absent.

## The interior stream and degree-five image

Inside r<1 the source partial_x h is zero, so the canonical stream is harmonic. Its odd-x/odd-y parity gives an expansion in r^n sin(n theta) for even n>=2. The expansion and all fixed finite derivatives converge on smaller discs because the compact smooth source is separated from the disc; equivalently the logarithmic Green kernel has a locally uniformly convergent Taylor expansion there after differentiating against the smooth source.

For every even n>=2, projection of partial_x h gives

 f_n=[F_(n-1)'-(n-1)F_(n-1)/r
                      +F_(n+1)'+(n+1)F_(n+1)/r]/2.

The full radial Green formula restricted to r<1 and compact-support integration by parts give

 Gamma_n=(1/(2n))integral r^(1-n) f_n dr
          =(1/2)integral r^(-n)F_(n+1)dr.                  (6)

This coefficient calculation is valid for each mode of the smooth angular function; no exchange with an unbounded series is needed. In particular Sigma=2Gamma2=0 and Gamma4=gamma/2>0 by(5). Therefore, writing C=4Gamma4=2gamma>0,

 psi=C(x^3y-xy^3)+E6,
 |D^j E6|<=C_j r^(6-j), 0<=j<=3, on a fixed smaller disc.  (7)

The even-mode harmonic Taylor expansion proves these differentiated remainders. With U4=(-Cx^3+3Cxy^2,3Cx^2y-Cy^3), direct multiplication gives

 U4.grad(x^2y)=C(x^4y+5x^2y^3).                            (8)

On r<1 the local terms involving h and grad h and the strain term vanish, so g:=L_rho h=U[h].grad rho there. Combining(1), (7) and(8), the product rule gives

 g=C(x^4y+5x^2y^3)+E7,
 |D^j E7|<=C_j r^(7-j), 0<=j<=2.                           (9)

For clarity, the second derivative uses up to D3 rho and D2 U, which are among the stated hypotheses and the third stream derivative. The terms U4.grad R have differentiated order r^(7-j), as do (U-U4).grad(x^2y); the remaining product has higher order. No differentiating of an undifferentiated big-O estimate is used.

## A uniform lower bound near the vertical axis

From parity, g is even in x. The trace condition rho(0,y)=0 and C1 regularity give rho_y(0,y)=0; evenness gives rho_x(0,y)=0. Hence g(0,y)=0. Since g is C2 and even in x, g_x(0,y)=0 as well. Evaluating the differentiated expansion(9) on the axis gives

 g_xx(0,y)=10C y^3+O(y^5).                                 (10)

Because C>0, choose a sufficiently small y_*>0 so that g_xx(0,y)>=5C y^3 for0<y<=y_*. Fix I=[y_*/2,y_*]. The positive lower bound on I and continuity of g_xx imply that some epsilon>0 and c0>0 satisfy g_xx(x,y)>=c0 on[0,epsilon]xI. The rectangle lies in r<1 after shrinking y_* and epsilon. Taylor's integral formula now gives, uniformly there,

 g(x,y)=integral_0^x (x-t)g_xx(t,y)dt >= (c0/2)x^2.          (11)

Thus the zeroth-order weighted square integral on this rectangle dominates a positive multiple of integral_0^epsilon x^(4-2a)dx. It diverges if and only if a>=5/2, logarithmically at equality. This proves the nonmembership in(3) for those a and every s>=0. No lower conclusion is drawn from an upper majorant alone. The proof does not assert membership of the image when a<5/2; higher derivatives or other regions may still matter.

## Input membership, canonical application and scope

The positive-x part of the support of h has x bounded above and below by positive constants and y in a bounded interval. Under z=log x the transformed h is therefore smooth and compactly supported in(z,y). Multiplication by exp((1/2-a)z) preserves that property for any fixed finite a. A smooth compact function belongs to every finite H^s, so h belongs to all the stated Y_(a,s). In fact its frozen transport image also remains smooth compact in(z,y); the local domain is not the source of the nonmembership.

The actual canonical modal background satisfies(1): modal_graph_scaling/PROOF.md gives local C^(4,alpha) and differentiated remainder bounds through order3; modal_repair/PROOF.md gives the explicit x^2y factor and exact finite joins. The parent191 pins carry these sources through187. The application must rehash all191parentpins, and separately pin the source mapping used here. No rounded unjoined stored representation is substituted. No numerical norm or parent finite enclosure is used to prove the positive Gram determinant or the analytic Taylor lower bound.

The planned independent algebra paths reconstruct the projected third/fifth coefficients, the positive Gram determinant identity, the sine-frequency independence, the quartic velocity, its degree-five image, the axis second derivative and the exact weight threshold. One path uses rational polynomial dictionaries; the other independent Sympy and Laurent-frequency expressions. These finite checks verify identities only. The choice of smooth bump, strict Gram positivity, harmonic convergence and Taylor argument are analytic parts of this proof.

This result rejects preservation of the entire indicated smooth test class by L_rho in a strong axis-weighted Y. It does not prove nonexistence of a stationary IPM profile, failure of an inverse on every smaller graph domain, failure of the frozen theorem, or any decisive endpoint of IPM Analysis I. A workable full nonlinear framework could require nonlocal compatibility conditions, additional range restrictions, or different spaces; none is established here.
