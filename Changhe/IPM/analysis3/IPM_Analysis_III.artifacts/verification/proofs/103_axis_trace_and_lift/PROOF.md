# Explicit axis-trace norms and the radial lift error

## The trace functional

Set a=17/4, B=29/4, W(r)=max(1,r)^B and R=L2_P(|x|^(-2a)W(r)dX). The parity is even in x and odd in y. Let T_h(y)=U_2[h](0,y) mean the bounded extension of the off-diagonal axis trace from smooth core inputs supported away from the vertical axis. For j=0,1,2,3 and y>0 define

 c_j=(j+1)!/(2 pi), I_a=2 Beta(a+1/2,1/2),
 p=2a+1, q_j=2a-2j-3,
 A_p(R)=integral_0^R r^p/W(r) dr,
 B_q(R)=integral_R^infinity r^q/W(r) dr,

 N_j(y)^2=c_j^2 I_a [
  (y/2)^(2a-2j-2)/((2a-2j-2)W(y/2))
  +2^(2j+4) B_(q_j)(2y)
  +(2/y)^(2j+4) A_p(2y)].                               (1)

Then the trace and its first three y derivatives are bounded functionals on R, with

 |T_h^(j)(y)|<=N_j(y)||h||_R.                            (2)

These bounds are explicit majorants, not claimed sharp norms. The elementary integrals in (1) are

 A_p(R)=R^(p+1)/(p+1), R<=1,
 A_p(R)=1/(p+1)+(R^(p-B+1)-1)/(p-B+1), R>=1,

 B_q(R)=(1-R^(q+1))/(q+1)+1/(B-q-1), R<=1,
 B_q(R)=R^(q-B+1)/(B-q-1), R>=1.                         (3)

For the displayed exponents none of the denominators vanishes. In particular p+1=21/2, p-B+1=13/4, q_j+1=13/2-2j and B-q_j-1=3/4+2j. The same inequalities hold for negative y after replacing y by |y|.

## Proof of the trace estimate

The off-diagonal kernel vector of the canonical IPM velocity has magnitude 1/(2 pi|X|^2). It is the real and imaginary components of a fixed complex multiple of (x+i y)^(-2), so its jth derivative in y has vector magnitude (j+1)!/(2 pi|X|^(j+2)). Thus the scalar second component has magnitude at most c_j|X|^(-j-2). The local multiplication term in U_2 is zero on the axis for core inputs; all its tangential derivatives are also zero there.

Cauchy-Schwarz with the actual weight reduces (2) to the integral of the squared kernel times |Y_x|^(2a)/W(|Y|). Put X=(0,y), and split the source plane into the following three regions, permitting overcounting for an upper bound.

On |Y-X|<y/2, write Y-X in polar coordinates. Since Y_x=(Y-X)_x and |Y|>=y/2, angular integration gives I_a and radial integration gives the first term in (1). The exponent 2a-2j-2 is positive for j<=3.

On |Y|>=2y, one has |X-Y|>=|Y|/2. Polar coordinates about0 give the second term in (1), with the exact angular integral I_a=int_0^(2pi)|cos theta|^(2a)dtheta.

The remaining points satisfy |Y|<2y and |Y-X|>=y/2. Bounding the kernel by c_j(2/y)^(j+2) and integrating the exact radial weight gives the third term. This proves (1)-(2). Formulas (3) follow by splitting at radius1. All tails are convergent at the stated a and B.

Restricting the input to its parity subspace can only decrease a functional norm. Thus no pointwise replacement of a reflected distance is used. To justify differentiation at the moving singularity, fix a compact positive y interval. The squared R-dual norm of the jth kernel on a ball of radius epsilon about (0,y) is bounded uniformly by a constant times epsilon^(2a-2j-2), which tends to zero for j<=3. If two centers are closer than epsilon, the union of these balls is contained in a ball of radius3epsilon about either center. Away from this union, ordinary dominated convergence applies, including at infinity by the radial tail bound above. Consequently the jth kernel is continuous in R-dual norm for j<=3. The pointwise fundamental theorem of calculus away from x=0, followed by its Bochner-integral version in the dual space, identifies the derivative of kernel j-1 with kernel j for j=1,2,3. Pairing with h proves that T_h is C3 on each compact interval not containing0. No integrable pointwise supremum over moving centers is asserted.

## The derivative of the axis jet

Write the background near the vertical axis as rho=x^2 y alpha(log|y|)+O(x^4). For y>0 the raw axis jet of U[h].grad rho is

 gamma_h(t)=(alpha(t)+alpha'(t))T_h(y)/y-2alpha(t)T_h'(y),
 y=exp(t).

The signs use incompressibility, partial_x U_1(0,y)=-T_h'(y). One differentiation in t gives exactly

 gamma_h'(t)=(alpha''-alpha)T_h(y)/y
                  +(alpha-alpha')T_h'(y)-2alpha y T_h''(y). (4)

Consequently a certified bound on the three axis coefficient functions alpha,alpha',alpha'' gives

 ||gamma_t'||_(R*)<=|alpha''-alpha|N_0(y)/y
                     +|alpha-alpha'|N_1(y)+2|alpha|y N_2(y). (5)

This is an explicit substitute for an unspecified trace constant in the radial-versus-vertical lift error. It concerns the raw axis jet; the normalization rank term is an additional explicitly known finite-rank term when present.

## A strip bound for the lift difference

Let 0<Y0<Y1, d>0 and let M_gamma bound the right side of (5) for

 Y0<=y<=sqrt(Y1^2+d^2).

For the output set Omega={|x|<d, Y0<=|y|<=Y1}, put Wmax=max(1,sqrt(Y1^2+d^2))^B. The difference between the radial and vertical lifts is

 L_h(x,y)=x^2 y[gamma_h(log r)-gamma_h(log|y|)].

Then

 ||1_Omega L_h||_R
 <=sqrt(2 Wmax(1/Y0-1/Y1)) M_gamma d^(1/4)||h||_R.       (6)

Indeed log(r/|y|)<=x^2/(2y^2), so |L_h|<=|x|^4 M_gamma||h||/(2|y|). The exact x integral is int_(-d)^d |x|^(8-2a)dx=4d^(1/2). The y integral, including both signs and the factor1/4, is (1/2)(1/Y0-1/Y1). This gives (6), with no omitted quadrant factor. Output restriction to an annulus only decreases the norm. If the coefficient bound uses a fixed upper d0>=d, it remains valid for all smaller d.

## Scope and verification

The constants N_j are universal explicit functions for the actual remainder weight. Formula (6) becomes numerical when actual axis coefficient bounds and a window are supplied. None is presently substituted by floating samples. The separate near-input strip, separated-input kernel, radial-tail, localization and finite-rank errors in INJ-Q remain additional. This lemma does not itself certify a global inverse.

The code independently checks the elementary radial integrals and the differentiated jet identity symbolically, and evaluates N_j(1) with directed arithmetic at256 and384 bits. These sample values are checks of the formulas, not bounds over an interval of y.
