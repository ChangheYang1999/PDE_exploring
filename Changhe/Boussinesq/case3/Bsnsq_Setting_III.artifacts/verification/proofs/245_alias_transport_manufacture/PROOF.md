# A value-invisible temperature changes the transported vorticity

## Exact diagnostic statement

This is a manufactured test of the temperature-value-fit and vorticity-transport operations, not a solution of B2. Fix the linear transport field W=(x/2,11y/2). This field has divergence6 and Jacobian eigenvalues1/2 and11/2, which equal (beta-2)/2 and (3beta+2)/2 at beta=3, but its relative velocity contains affine strain and its curl does not equal the vorticities below. No canonical full-plane B2 inverse or far-field claim is made for this test.

Use the angular samples phi_j=(j+1/2)pi/12, j=0,...,11, with x=r sinphi, y=-r cosphi. Put

    P(z)=Re(-z+i)^12=sum_(n even,0<=n<=12) c_n z^n,
    c_n=binomial(12,n)(-1)^(n/2).

Since i^12=1, this expression follows by the binomial theorem. Define

    D(x,y)=x^14 P(y/x)=x^2 Re(-y+i x)^12.

The right expression is a homogeneous polynomial of degree14, even in x. It vanishes at every point of the12 sampled rays, at every radius, because -y+i x=r exp(i phi) there and cos(12phi_j)=0. All its center derivatives of total order<14 vanish, and D(0,y)=0. Thus adding any real multiple of D to Theta_0=x^2 leaves all sampled values and the prescribed quadratic center jet unchanged.

For a polynomial forcing F=Theta_x, consider W.gradOmega+Omega=F and select the polynomial solution. The monomial x^(13-n)y^n has eigenvalue

    ell_n=1+(13-n)/2+11n/2=15/2+5n>0.

Consequently define

    Q(z)=sum_(n even,0<=n<=12) [(14-n)c_n/(15/2+5n)]z^n,
    O(x,y)=x^13 Q(y/x).

Direct differentiation gives W.gradO+O=D_x. The polynomial O is odd in x and has no center terms below degree13. The unique polynomial vorticity response to Theta_lambda=x^2+lambda D is therefore

    Omega_lambda=4x/3+lambda O.

Uniqueness holds because the operator on every polynomial monomial x^m y^n has eigenvalue1+m/2+11n/2>0. It also equals the convergent backward-flow integral integral_0^infinity exp(-s) F(x exp(-s/2),y exp(-11s/2)) ds, since integrating each monomial divides by its positive eigenvalue. Neither the added temperature nor its forcing response is claimed to satisfy the separate temperature transport equation.

At least one sampled ray has O nonzero. Indeed the12 distinct numbers z_j=-cot(phi_j) are precisely the12 roots of P. The polynomials P and Q both have degree12. If Q vanished at all these roots, it would be a scalar multiple of P. Their constant coefficient ratio is28/15, while their leading coefficient ratio is4/135. These differ. Thus Q does not vanish at all the nodes. At any sample point on a ray where O!=0, choosing lambda of either sign and arbitrary magnitude makes Omega_lambda/x have either sign while all temperature value samples remain identical.

The statement is exact for this manufactured transport operator. It proves that those samples alone cannot determine the sign of transported vorticity for smooth (here polynomial) temperatures sharing those samples, parity and center jet. It does not prove a sign error for the physical Gaussian experiment. That assertion requires the independent controlled numerical calculations in P240. The polynomial D grows rapidly, so no admissible B2 far-field interpretation is intended.

## Independent checks planned after this proof

Use exact rational polynomial arithmetic to verify the two PDE identities, parity, center orders, angular-root reduction, nonproportionality, and absence of zero denominators. Use independent five-point finite differences and adaptive integration only as optional controls, not as proof. Store the exact polynomial coefficients in JSON rather than an opaque executable certificate. No proof-assistant build is used.
