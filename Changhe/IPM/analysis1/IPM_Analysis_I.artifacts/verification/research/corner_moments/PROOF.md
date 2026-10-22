# Canonical corner moments and a pure-weight coupling obstruction

2026-10-20. Independent verifier derivation. Written before the numerical checks. Application status OPEN until the source, exact algebra and interval constants have been audited.

This note checks the moment assertions K1 to K4 and two coupling identities in the lead's corner note. It does not prove its double Taylor block estimate D1, its annular Sobolev trace estimate T2, or its full variable-coefficient coupling estimate. Those statements remain separate obligations.

## 1. Setting and exact statements

Let a,b>0, A=a+b, and let D be the real smooth compactly supported functions on the plane whose support avoids both coordinate axes, even in x and odd in y. Set

w_0(x,y)=|x|^(-2a)|y|^(-2b),
w_gamma(x,y)=w_0(x,y)(1+r)^(2(A-gamma)), r=(x^2+y^2)^(1/2).

The norm is the square root of the integral of |h|^2 w over the entire plane. D is dense in the corresponding parity subspace: first truncate away from the axes and infinity, then smooth on the resulting compact sets and project onto the two parities. On those sets the weights are positive, bounded and bounded away from zero, so these operations approximate in the weighted norm.

Let U[h] be the canonical IPM velocity, with -Delta psi=partial_x h and U=(-psi_y,psi_x). For h in D the density vanishes near the origin. Write its convergent local expansion as

U_2+i U_1 = i sum_(k odd, k>=1) d_k (x+i y)^k.

For k=l+j odd and a parity-allowed pair of nonnegative integers l,j, put c_(i,l,j)=[x^l y^j]U_i. The allowed pairs have l odd,j even for i=1, and l even,j odd for i=2. Every such coefficient is a nonzero linear functional on D. Its integral kernel, up to sign, is

L_lj r^(-k-2) sin((k+2)theta),
L_lj=(k+1) binom(k,l)/(2pi).

Define

J_k(a,b)=integral_0^(2pi) |cos(theta)|^(2a)|sin(theta)|^(2b) sin^2((k+2)theta) dtheta.

The following statements hold.

1. No nonzero c_(i,l,j) extends to a bounded functional on the parity subspace of L^2(w_0), for any A.
2. On functions supported in the unit square [-1,1]^2 the coefficient extends boundedly if and only if A>k+1. In that case its norm is at most

   L_lj [J_k(a,b) (sqrt(2))^(2(A-k-1))/(2(A-k-1))]^(1/2).

   This is an upper bound, not the exact square-domain norm. The same criterion holds for support in any fixed bounded neighborhood of the origin that contains a disk.
3. On L^2(w_gamma) the coefficient extends boundedly if and only if A>k+1 and gamma<k+1. Its exact norm on the parity subspace is

   L_lj [J_k(a,b) B(2(A-k-1),2(k+1-gamma))]^(1/2),

   where B(p,q)=integral_0^infty t^(p-1)(1+t)^(-p-q)dt for p,q>0.
4. If rho=x^2 y alpha near the origin, alpha is even in both variables and C^4 there, c=psi[h]_(xy)(0)=-d_1, and W=U[h]+(c/3)(x,y), then for G=W dot grad rho,

   [x^2y]G=0,
   [x^4y]G=-alpha(0,0)d_3-(4/3)c alpha_20,

   where alpha_20=[x^2]alpha(x,0)=alpha_(xx)(0,0)/2. Here [x^l y^j]G means a coefficient of the unique degree-at-most5 asymptotic polynomial P with G(X)-P(X)=o(r^5). It does not assert that G is C^5 on a neighborhood; they do not require alpha to be analytic.
5. Let rho=x^2y exactly on B_1, and let T_x^6 and T_y^3 subtract the Cartesian Taylor polynomials of orders respectively less than6 in x and less than3 in y. If A>8, the map

   h -> T_x^6 T_y^3 ((U[h]+(c[h]/3)X) dot grad rho)

   from D with the global L^2(w_0) norm to L^2(B_(1/2),w_0) has no bounded extension. For the working parameters a=129/20,b=307/100 the output for each member of the counterexample sequence belongs to this local space, while its norm tends to infinity. In statement5, c[h] denotes psi[h]_(xy)(0), so the correction to c_l is c[h]/3.

The criterion in statement3 is for this coefficient functional. Boundedness of one moment alone does not construct the full canonical velocity. For example the full canonical strain already requires gamma<2.

## 2. Kernel, sign and parity

For compactly supported smooth h, the two-dimensional fundamental solution of -Delta is -(2pi)^(-1)log r. Integrating the density derivative by parts gives

psi(X)=-(2pi)^(-1) integral h(W) (x-W_1)/|X-W|^2 dW.

Away from the support, differentiating yields

U_1=integral [- (x-W_1)(y-W_2)/(pi|X-W|^4)] h(W)dW,
U_2=integral [((x-W_1)^2-(y-W_2)^2)/(2pi|X-W|^4)] h(W)dW.

These are exactly the off-support canonical kernels. Their decay at infinity excludes an added affine velocity. With z=x+i y they combine to

U_2+iU_1=(2pi)^(-1) integral h(W)(z-W)^(-2)dW.

If the distance from0 to the support is R>0, expand for |z|<R:

(z-W)^(-2)=sum_(k>=0) (k+1) z^k W^(-k-2).

The series and each fixed number of derivatives converge uniformly on |z|<=qR, q<1, and the source support is compact. Termwise integration is therefore justified. The two parities kill every even k and the real part of every remaining source moment. For odd k,

d_k=-(k+1)/(2pi) integral h(r,theta) r^(-k-2) sin((k+2)theta)dW.

Multiplication by i shows U_1=d_k Re z^k and U_2=-d_k Im z^k. Expanding z^k by the binomial theorem proves the coefficient kernel and its magnitude L_lj. It also gives U_1=d_1 x+O(r^3), U_2=-d_1 y+O(r^3), so c=-d_1. The signs in the coupling identities use this convention.

The moment kernel has the same even-x, odd-y parity as h. It is not zero on an open angular sector away from the axes. A smooth bump in that sector, extended by the parities and multiplied by the sign of the kernel there, makes its moment nonzero. Thus none of the allowed coefficient functionals is identically zero.

## 3. Exact dual norm and the two endpoint conditions

Let K be the real coefficient kernel. Cauchy-Schwarz gives

|integral h K| <= ||h||_(L^2(w)) (integral K^2/w)^(1/2).

If the last integral is finite, equality is attained in the Hilbert space by h=K/w up to scalar multiplication. This representer has the required parity. Density of D shows that the norm restricted to D is the same. If the integral is infinite, choose compact truncations of K/w away from its singular sets, normalize their weighted norms, and then approximate by D. The functional values tend to infinity along a suitable sequence. This proves necessity as well as sufficiency, including in the parity subspace.

For w_gamma the squared dual norm is

L_lj^2 J_k(a,b) integral_0^infty r^(2A-2k-3)(1+r)^(-2(A-gamma)) dr.

The angular factor is positive and finite because a,b>0. At0 the radial integrand is comparable to r^(2A-2k-3), so its integral converges if and only if A>k+1. At infinity it is comparable to r^(2gamma-2k-3), so convergence is equivalent to gamma<k+1. At either equality there is logarithmic divergence. Substitution p=2(A-k-1), q=2(k+1-gamma) identifies the beta integral in statement3 exactly.

On the unit square only the origin can cause a radial divergence. The square contains a disk about0 and lies in the disk of radius sqrt(2). The same positive angular sector proves necessity. Bounding its dual integral by the larger disk and integrating r^(2A-2k-3) proves statement2. The estimate J_k<=2B(a+1/2,b+1/2) follows by replacing sin^2 by1 and evaluating the four quadrant integrals.

For the global pure weight the radial integral has the same exponent at0 and infinity, so it can never converge at both ends. This already proves statement1. Here is an explicit scaling check, including the critical case. For F in D with c_(i,l,j)[F] nonzero, let F_R(X)=F(X/R). Direct substitution gives

||F_R||_(w_0)=R^(1-A)||F||_(w_0),
c_(i,l,j)[F_R]=R^(-k)c_(i,l,j)[F].

The ratio is a nonzero constant times R^(A-k-1), so expanding or shrinking R proves unboundedness unless A=k+1. At equality choose F supported in a narrow annulus and disjoint dilates R_j. Each normalized dilate has the same norm and the same moment. The sum of N such dilates has norm proportional to sqrt(N) and moment proportional to N. Dividing by its norm proves unboundedness in the critical case as well.

## 4. Two corner coupling coefficients

Write alpha_00=alpha(0,0) and alpha_20=[x^2]alpha(x,0). The linear part of W is

W_1=-(2/3)c x+O(r^3), W_2=(4/3)c y+O(r^3).

It annihilates x^2y, since 2(-2c/3)+4c/3=0. The cubic velocity term is

U_1^(3)=d_3(x^3-3xy^2), U_2^(3)=-d_3(3x^2y-y^3).

Its product with grad(alpha_00 x^2y) has coefficient -alpha_00 d_3 at x^4y. The linear W acting on alpha_20 x^4y contributes

(4(-2c/3)+4c/3)alpha_20=-(4/3)c alpha_20.

Other degree-five density monomials contain at least y^3 and cannot contribute x^4y under the diagonal linear field. Higher velocity terms and higher density remainders have degree too large. For detail, evenness and C^4 regularity give alpha=alpha_00+alpha_20 x^2+alpha_02 y^2+R, with R=O(r^4) and grad R=O(r^3). Thus grad(x^2yR)=O(r^6). Since W=O(r), its contribution is O(r^7). The analytic velocity terms of degree at least5 also contribute only O(r^7). This gives an asymptotic polynomial through degree5 with remainder O(r^7), uniquely determined independently of direction. G need only be C^3 on the neighborhood. This proves statement4 without assuming that G has classical fifth derivatives there.

## 5. Explicit unbounded remainder sequence

The degree-seven velocity polynomial is

U_1^(7)=d_7(x^7-21x^5y^2+35x^3y^4-7xy^6),
U_2^(7)=-d_7(7x^6y-35x^4y^3+21x^2y^5-y^7).

Consequently

2xy U_1^(7)+x^2 U_2^(7)
=d_7(-5x^8y-7x^6y^3+49x^4y^5-13x^2y^7).

The ordered Taylor remainders retain precisely -7d_7 x^6y^3. Their projections commute here because the functions are analytic. Terms of velocity degree1,3,5 give no monomial with x degree at least6 and y degree at least3; the added strain also vanishes after subtraction.

Choose F in D supported in a fixed annulus bounded away from0 and satisfying d_7[F] nonzero. Let h_R=R^(A-1)F(X/R) and send R to infinity. Its input norm is constant. Every degree-k velocity coefficient scales by R^(A-k-1). On the fixed square [-1/2,1/2]^2, contained in B_1, for R large enough its analytic kernel expansion and derivatives converge uniformly. The degree-seven contribution to the remainder is

-7d_7[F]R^(A-8)x^6y^3.

After division by R^(A-8), every higher contribution is O(R^(-2)) in C^9 on that square. Taylor's integral formula for T_x^6 T_y^3 supplies the factor x^6y^3; hence the normalized error is bounded by C R^(-2)|x|^6|y|^3 pointwise. For a<13/2 and b<7/2 this polynomial belongs to L^2(B_(1/2),w_0). Its norm is positive. The remainder norm divided by R^(A-8) thus converges to 7|d_7[F]| times this positive polynomial norm. At a=129/20,b=307/100 these strict inequalities hold and A-8=38/25>0, proving the asserted unboundedness with finite output norms.

For arbitrary a,b>0 with A>8, if either a>=13/2 or b>=7/2, the leading nonzero analytic factor of x^6y^3 already fails local weighted integrability on a small strip away from the other axis. For all sufficiently large R that factor is nonzero by the same uniform expansion. In that case the map does not even send this sequence into the stated local space. This proves statement5 in its full stated range.

This obstruction concerns a particular global pure-weight operator estimate. It excludes neither an exact IPM solution nor an a posteriori theorem with a composite weight or additional asymptotic data. The original exact modal trial also fails the lead's C^8 factor hypothesis, by the separate center_obstruction proof; that distinct fact is not used here.

## 6. Independent computation plan

For k=1,3,5,7 at a=129/20,b=307/100,gamma=1129/1000, enclose J_k and the moment bounds twice. The first method uses Arb gamma-function beta values and the polynomial identity sin(n theta)=sin(theta)U_(n-1)(cos theta). Since n=k+2 is odd, U_(n-1) is a polynomial in cos^2 theta. Squaring its integer polynomial gives

J_k=2 sum_j p_j B(a+j+1/2,b+3/2).

The second method uses mpmath.iv gamma-function beta values and the direct binomial expansion of Im(cos theta+i sin theta)^n. It yields

J_k=2 sum_(r,s=0)^((n-1)/2) (-1)^(r+s) binom(n,2r+1)binom(n,2s+1)
 B(a+n-r-s-1/2,b+r+s+3/2).

Each identity follows by integrating the squared finite polynomial on the first quadrant and multiplying by4. The implementation must retain all signed terms as intervals; cancellation does not authorize dropping terms. The beta radial arguments and all constants are exact rationals before interval evaluation. Exact sparse bivariate polynomial code, independent of the lead's sympy scripts, will check the velocity expansion, the two corner coefficients and the degree-seven remainder. This numerical work verifies the formulas and their effective constants; the proofs of boundedness and unboundedness are analytical.

The two interval implementations independently verify arithmetic and rounding in different finite angular expansions. They share the proved quadrant beta integration and gamma-based radial beta identity. Agreement of their enclosures is not an additional proof of the analytic dual-norm theorem. Outside the two local integrability windows, statement5 means failure even to map into the target; only inside the windows is it an unbounded norm ratio among finite-norm outputs.
