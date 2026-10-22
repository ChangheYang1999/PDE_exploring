# The scaling term in logarithmic Sobolev spaces

This proof is written before the new data check. Its application remains OPEN until independent checking, complete actual Claude Opus 5.5 review and later own adjudication. It concerns the canonical trial and compact test images. It does not construct an IPM inverse.

## Statement and definitions

Let rho=x²y a(x,y) be the exactly joined and normalized modal_v2 trial, with k=1615536043799051/9007199254740992 in (0,1/2). Use the canonical inverse -Delta psi[f]=partial_x f and U[f]=(-psi_y,psi_x), without a harmonic addition. Set

 Sigma(f)=psi[f]_xy(0), G=X.grad rho, s=153/50.

For x>0, z=log x, put T_b f=x^(1/2-b)f(x,y) and ||f||Y_(b,s)=||T_b f||H^s(R²_(z,y)), with squared Fourier weight (1+xi²+eta²)^s. All densities are real, even in x and odd in y. For every nonnegative b:

 rho belongs to Y_(b,s) if and only if 1+k<b<5/2;
 G belongs to Y_(b,s) if and only if 1+k<b<5/2.           (1)

Let D consist of all smooth compact parity densities supported away from x=0; the support need not avoid y=0. The scaling term initially defined on D by

 R h = (Sigma(h)/3) G                                   (2)

extends to a bounded operator Y_(b,s) -> Y_(b,s) if and only if

 1+k<b<2.                                               (3)

In this region the extension is unique, has rank one, and is compact. Its bound is ||R||<=C_(b,s)||G||Y/3, with the proved upper bound C_(b,s) from logarithmic_strain_functional. No numerical ceiling for ||G||Y or ||R|| is supplied here.

Finally let T_c be all smooth compact parity densities supported away from both axes, with no zero-strain restriction. For fixed real ell define

 Lh=(ell X+U[rho]).grad h-h+U[h].grad rho+(Sigma(h)/3)G.

Then the setwise inclusion L(T_c) subset Y_(b,s), among nonnegative b, holds if and only if

 1+k<b<5/2.                                             (4)

The same class-level threshold holds if supports are restricted to the fixed annulus 1<r<2 while remaining away from both axes. This statement about a fixed annular test class is separate from bounded extension of R on the dense class D. For a particular h in T_c with Sigma(h)!=0 and 0<=b<5/2, Lh belongs toY if and only if b>1+k. When Sigma(h)=0, result202 gives inclusion for every 0<=b<5/2.

All statements concern this canonical trial. They leave the full transport domain, inverse, range and nonlinear analysis open. In particular the obstruction199 to a closed realization containing the entire frozen graph domain remains unchanged.

## Exact trial inputs

The accepted canonical finite formula gives, on the punctured center region and for Cartesian derivatives through order5,

 |D^alpha(a-1)|<=C_alpha r^(2-|alpha|).

At infinity it gives |D^alpha a|<=C_alpha r^(k-3-|alpha|), and a finite leading expansion with a strictly smaller remainder. Let t_b be the last log knot, R0=exp(t_b), tau=log(r/R0). The leading angular factor is

 A(theta)=sum_(m=0)^259 [Aout[m,0]+z0 delta_(m,0)] cos(2m theta),
 Theta(theta)=cos²(theta) sin(theta) A(theta).

Here z0 is the exact normalization correction, distinct from the logarithmic coordinate z. The leading density is

 rho=R0³ exp(k tau) Theta(theta)+o(exp(k tau)),
 G=k R0³ exp(k tau) Theta(theta)+o(exp(k tau)),            (5)

uniformly in theta. The same finite formula proves differentiated remainder bounds as needed; (5) is not formally differentiated from an unspecified little-o term. The ten pure factor exponents are k-3-j(1-k)-2l with (j,l)=(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2), plus a faster power-log correction r^-bo. Only the first exponent is k-3, with no logarithm. Euler differentiation multiplies the corresponding density term by k, and every other finite power-log term remains strictly smaller.

The new data check must establish Aout[1,0]!=0 by separate exact NPZ/Fraction and integer-hex/fmpq decoding. This coefficient is unchanged by the normalization, which modifies only mode m=0. Orthogonality then gives A not identically zero. Since cos²(theta)sin(theta) vanishes only at finitely many angular points, Theta is not identically zero. No numerical angular sampling or lower bound for the entire polynomial is required.

On compact annuli a is C6 by the exact joins; G is C5 there. The finite-mode radial ODE gives U[rho] C6 there, as detailed in canonical_residual_weak_axis_membership/REVIEW_RESPONSE.md. These are inherited analytic properties of the canonical profile, not new matching computations.

## Sufficiency for rho and G

Their leading center terms are the Cartesian polynomials x²y and 3x²y. A compact smooth radial cutoff of either polynomial belongs toY_(b,N) for every fixed integer N when b<5/2. Indeed its transform has the form x^(5/2-b)q(x,y), with q smooth on the physical plane and compact in x,y. Each fixed z or y derivative remains x^(5/2-b) times a bounded smooth function on this support. Its squared integral in dzdy=dxdy/x is bounded by a constant times integral_0^C x^(4-2b)dx, which is finite for b<5/2. Fourier derivative characterization gives the claim. No false center-shell derivative loss is assigned to this polynomial part.

For the remaining center terms, direct differentiation and the factor a-1 give, for p+q<=4,

 |E_x^p partial_y^q(rho-x²y)|<=C x² r^(3-q),
 |E_x^p partial_y^q(G-3x²y)|<=C x² r^(3-q), E_x=x partial_x.

For G one uses G=x²y(3a+x a_x+y a_y), so derivatives of a through5 suffice. The same factor persists across all y derivatives. After subtracting the cut-off polynomials, the shell argument of result203 gives center H^s shell norm bounded by C lambda^(6-b-s). This exponent is positive for b<5/2 because s=153/50 and 6-5/2-s=11/25>0. Thus the center contributions belong toY.

At infinity the differentiated bounds for both f=rho and f=G are

 |E_x^p partial_y^q f|<=C x² r^(k-2-q), p+q<=4.           (6)

For a radial dyadic shell r comparable to lambda, the logarithmic Jacobian and vertical-axis integral give

 ||partial_z^p partial_y^q T_b f_shell||L2
       <=C_b lambda^(k+1-b-q), p+q<=4.                 (7)

For lambda>=1 the H4 shell norm is at most C_b lambda^(k+1-b), so these norms sum when b>1+k. Intermediate annuli have finite H4 norms by the C5 factor regularity and the same x²-axis integral. Absolute summation and the locally finite partition identify the H^s sum with each transformed field. This proves sufficiency in(1).

## Necessity for rho and G

By the new nonzero coefficient check, Theta is nonzero on a closed angular interval strictly inside x>0 and away from both axes. Parity allows choosing the positive-x half-plane. Uniformity in(5) gives |rho|>=c r^k and |G|>=c' r^k on that interval for all sufficiently large r, since k>0. The zeroth squared norm is then bounded below by a positive multiple of

 integral^infinity r^(2k-2b+1)dr,

which diverges when b<=1+k, logarithmically at equality.

At a fixed small positive y, the center estimates imply

 rho(x,y)/x² -> y a(0,y)=y+O(y³),
 G(x,y)/x² -> y[3a(0,y)+y a_y(0,y)]=3y+O(y³)

as x decreases to0. Annular continuity gives, for each field, a positive-y rectangle on which its magnitude is at least c x². Hence its zeroth squared norm diverges when b>=5/2. This argument only uses the exact center leading coefficient1 and its differentiated remainder. It does not rely on the residual's much smaller axis coefficientQ. Together these obstructions prove(1).

## Bounded and compact scaling term

For 1+k<b<2, (1) gives G inY, and result204 supplies the bounded extension of Sigma with |Sigma(h)|<=C_(b,s)||h||Y. This proves(2),(3) in the sufficient direction and the stated bound. The transformed smooth compact odd-y tests are dense inH^s, so D is dense inY and the extension is unique. Its range is the nonzero span of G. For a bounded sequence of inputs, their strain scalars are bounded, so a scalar convergent subsequence makes the outputs converge inY. This proves compactness directly.

If b<=1+k or b>=5/2, then G is not inY. There exists h inD supported in1<r<2 and away from both axes with Sigma(h)>0: take r³ eta(r)phi(theta)sin3theta with nonnegative smooth cutoffs eta,phi as in result204. The kernel formula gives a product of positive radial and angular integrals. Thus Rh is not inY and no bounded extension agreeing onD exists.

For 2<=b<5/2, G is a nonzero element ofY because 1+k<2. The result204 compact tests have uniformly bounded Y norms and |Sigma| tending to infinity. Their images underR therefore have norms |Sigma| ||G||Y/3 tending to infinity. This proves necessity throughout the remaining range, including b=2. The counterexamples have supports at radii tending to infinity; no claim of such unboundedness on a fixed annulus is used.

## Full compact-test images and the center cancellation

For h inT_c write sigma=Sigma(h). Near0 its canonical velocity has the harmonic expansion

 U[h]=(-sigma x,sigma y)+(x v1,y v2),
 |D^alpha v_i|<=C r^(2-|alpha|), |alpha|<=4.

The local transport term vanishes near0. Direct differentiation shows that the remaining full coupling has the exact form

 U[h].grad rho+(sigma/3)G = x²y B_h,
 B_h=(sigma/3)(-2x a_x+4y a_y)
                      +v1(2a+x a_x)+v2(a+y a_y).       (8)

The cubic terms cancel exactly, for every sigma. Since a-1 and the v_i have order2, differentiated bounds through4 give |D^alpha B_h|<=C r^(2-|alpha|). The same H3/H4 center-shell argument proves membership near0 for every b<5/2. On compact annuli the term is C4 with its x² factor; the local transport term is compact C4 away from the axes.

At infinity, the compact source has zero mass and first moments, so U[h] has differentiated order r^-3 and its coordinate quotients have order r^-4. Thus U[h].grad rho has shell exponent k-3-b, as in result202. The rank-one contribution has the slower exponent k+1-b. Therefore for every h inT_c, the whole image belongs toY when 1+k<b<5/2. If sigma=0, the rank term vanishes and result202 applies throughout 0<=b<5/2.

If sigma!=0, (5) and the compact-source velocity decay give the uniform far expansion

 Lh=(sigma/3)k R0³ exp(k tau)Theta(theta)+o(exp(k tau)).

The local transport term is zero outside a compact set, and the nonlocal velocity-density term has degree k-4, strictly smaller than k. The nonzero-sector argument therefore proves Lh not inY for b<=1+k. A fixed annular positive-strain test proves failure of the class-level inclusion for all those weights. For b>=5/2, the accepted zero-strain annular counterexample192 already proves failure of the class inclusion. This proves(4) and the stated individual classification below5/2.

## Evidence and remaining scope

The only new numerical premise is a nonzero exact exterior cosine coefficient and its elementary products with k. Two independently decoded rational computations will check it, the exponent gaps and the factor identities. Existing canonical joining, strain, residual and zero-strain compact-test results remain explicit inherited dependencies. No numerical quadrature, interval norm estimate or derivative-tail run is used. The independent full derivative enclosure179 retains priority as the sole heavy job.

At b=3/2 the residual, rho and G all have finiteY norms, and the scaling functional is bounded by the result204 constant C/3<0.087815300222. This does not supply the size of those norms or an inverse. The compactness of the isolated rank-one term does not repair the variable-transport graph-domain obstruction, which uses tests with Sigma=0. The decisive PDE endpoint remains unresolved.
