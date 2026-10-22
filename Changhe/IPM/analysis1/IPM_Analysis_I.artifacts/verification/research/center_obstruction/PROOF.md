# The exact modal trial has a nonsmooth fifth-order center term

2026-10-20. This proof was written before the numerical application. Exact Fourier and independent Arb/iv arithmetic checks passed at19:14:16Z. ActualOpus5.5 accepted the narrow argument conditionally at19:19:51Z. Its requested local operator definition, explicit derivative orders, Green expansion detail and independent binary layout check are now supplied; closure review was accepted at2026-10-20T19:23:37Z. Status: CONFIRMED for the narrow exact-modal-trial obstruction. This is an obstruction to a proposed background regularity hypothesis and weighted forcing space. It is not exclusion of an exact IPM profile in any neighborhood.

## Statement

Let M>=3 and R>0. Suppose an even-x, odd-y density has, for 0<r<R,

rho=x^2 y a,
a(r,theta)=1+r^2 R^(-2) D(theta)+O(r^4),
D(theta)=sum_(m=0)^(M-1) d_m cos(2m theta).

The remainder and each finite number of polar derivatives have the corresponding order, allowing powers of log(r) in higher terms. For the concrete modal trial the remainder is a finite sum of even powers beginning at r^4 and r^bi times a degree-six polynomial in log(r/R), with bi>49. Thus its derivatives through all orders used below have the stated bounds. Assume the density outside this disk is the same canonical, sublinear modal extension as in ../modal_repair/PROOF.md and ../inner_majorant/PROOF.md. Let c=psi_xy(0), c_l=(1+c)/3, c>0, and epsilon=(c_l X+U[rho]).grad rho-rho.

If some d_m with m>=2 is nonzero, a is not twice Frechet differentiable at the origin. If d_(M-1) is nonzero, rho is C^(4,1) near the origin but is not C^5 there, and the residual has the expansion

epsilon(r,theta)=r^5 E(theta)+O(r^7(1+|log r|)),

with |partial^beta(error)| <= C_beta r^(7-|beta|)(1+|log r|) on the punctured disk for every Cartesian multiindex |beta|<=7. These bounds include the one-dimensional axis traces used below. The sine coefficient of E at frequency 2M+3 is

E_(2M+3) = c (M-2) d_(M-1)/(8 R^2).

In particular E is nonzero and is not the restriction of any homogeneous degree-five Cartesian polynomial.

Define P_x^6 F=sum_(l=0)^5 x^l partial_x^l F(0,y)/l! and P_y^3 F=sum_(j=0)^2 y^j partial_y^j F(x,0)/j!, using the indicated axis traces and their continuous extensions at zero where needed. Put T_x^6=I-P_x^6 and T_y^3=I-P_y^3. The order T_x^6 T_y^3 means apply T_y^3 first. The two orders need not commute. For either specified order, its residual remainder is

T_x^6 T_y^3 epsilon=r^5 E_rem(theta)+O(r^7(1+|log r|)),

where E_rem has the same nonzero frequency 2M+3 coefficient. For any real weights a_w,b_w with A_w=a_w+b_w>=6, this remainder is not in L^2(|x|^(-2a_w)|y|^(-2b_w)) on any neighborhood of zero. The same is true of epsilon without subtraction. Restricting the weight to any sufficiently small cone on which the respective angular leading coefficient is nonzero already gives divergence. The working weights (6.45,3.07) have A_w=9.52.

## Taylor regularity of the factor and density

If a were twice Frechet differentiable, its O(r^2) behavior and parity would give a quadratic Taylor polynomial q_0(x^2+y^2)+q_1(x^2-y^2). Dividing the Taylor remainder by r^2 and taking a fixed ray would force R^(-2)D(theta)=q_0+q_1 cos(2theta). Uniqueness of a finite Fourier expansion excludes every nonzero coefficient with m>=2.

Write rho=rho_3+rho_5+O(r^7), rho_3=x^2y. A smooth homogeneous function of integer degree five outside zero, with a smooth angular factor, extends to C^(4,1) at zero: its derivatives of order j<=4 are O(r^(5-j)), and derivatives of order five away from zero are bounded. Integration along a line segment, split at zero if necessary, makes the fourth derivatives Lipschitz. The remaining inner terms are C^5, in fact more regular, because their radial degrees are at least seven or bi+3>52, with only finite logarithmic factors. Thus rho is C^(4,1).

The identity x^2 y=r^3(sin(theta)+sin(3theta))/4 gives

rho_5=R^(-2) r^5 sum_m d_m[sin((1+2m)theta)+sin((1-2m)theta)+sin((3+2m)theta)+sin((3-2m)theta)]/8.

Its highest frequency is 2M+1, with coefficient d_(M-1)/(8R^2). For M>=3 this frequency exceeds five. If rho were C^5, its fifth-order term after removing rho_3 would be a homogeneous Cartesian polynomial of degree five, whose angular frequencies are at most five. The nonzero highest coefficient contradicts that assertion.

## The canonical cubic velocity

The density satisfies partial_x rho=2xy+O(r^4). The finite-mode Green formula shows

psi=cxy+psi_4+O(r^6(1+|log r|)),
U=(-cx,cy)+U_3+O(r^5(1+|log r|)),

where psi_4 is a homogeneous degree-four polynomial, U_3=grad^perp psi_4 is a homogeneous cubic polynomial. To see the asserted structure directly, the forcing 2xy=r^2 sin(2theta) has particular stream -r^4 sin(2theta)/12. Canonical upper moments supply the regular homogeneous terms r^(2n)sin(2n theta). Up to degree four these are precisely n=1 (strain) and n=2 (a harmonic quartic polynomial). The O(r^4) forcing contributes streams of order r^6, except for a possible r^6 log r resonance at n=3; higher forcing powers and the finite logarithmic correction have still higher orders. There are finitely many modes, so these estimates and their needed differentiated forms follow term by term. No harmonic strain is chosen independently of the canonical extension.

Here the differentiated estimates can also be verified without importing a regularity theorem. Each local forcing term is a finite linear combination of r^s(log r)^j sin(m theta), with m a positive even integer and either s an even integer>=2 or s>=bi+2. For j=0 and s+2!=m, the particular stream is -r^(s+2)sin(m theta)/((s+2)^2-m^2), times the forcing coefficient. At resonance s+2=m it is -r^m log(r)sin(m theta)/(2m), times that coefficient. Differentiating with respect to s or solving the finite triangular log-power system gives the same structure for j>0. Homogeneous terms are multiples of r^m sin(m theta); the canonical lower integral excludes r^(-m). The only terms below stream degree6 are consequently the strain and quartic polynomial already identified. Termwise Cartesian differentiation through order8 gives the asserted velocity estimates, and the residual product rule gives its remainder estimates through order7. The inner density is a finite sum and bi>49, so the higher logarithmic terms satisfy all these estimates.

For completeness the canonical integrals converge: near zero f_m=O(r^2), so the lower integrand r^(m+1)f_m is integrable. At infinity the exact modal extension has f_m=O(r^(k-1)) with k<1, so the upper integrand r^(1-m)f_m=O(r^(k-m)) is integrable for every m>=2. Its actual decay can include still smaller logarithmic corrections. Thus the local Green expansion is for the same full-plane inverse, with no additional harmonic term at infinity. Exact normalization c=3/k-1 is the separate audited scalar-repair dependency.


Set V_lin=(-A x,D_s y), A=2c_l-1, D_s=4c_l-1. The exact normalization annihilates rho_3. Hence

epsilon_5=(V_lin.grad-1)rho_5+U_3.grad rho_3.

The second summand is a degree-five polynomial and has no angular frequency greater than five. In polar form V_lin.grad=c_l r partial_r-c cos(2theta)r partial_r+c sin(2theta)partial_theta. Acting on r^5 sin(nu theta), the coefficient at sin((nu+2)theta) is c(nu-5)/2. Apply this to nu=2M+1 and its coefficient d_(M-1)/(8R^2). This determines the highest residual coefficient and proves that it cannot be canceled by the unknown canonical quartic stream. This calculation also permits an independent reconstruction using z=x+iy: V_lin z=c_l z-c conjugate(z), acting on z^p conjugate(z)^q with p+q=5.

## Rectangular subtraction and weighted divergence

The leading function epsilon_5 has the parity and strong factor x^2y. For fixed nonzero x, its y-linear trace is a constant times x^4. For fixed nonzero y, its x^2 and x^4 traces are constants times y^3 and y. These facts follow from homogeneity, evenness in x, oddness in y and smoothness on the punctured coordinate axes. Thus P_y^3 epsilon_5 and P_x^6 epsilon_5 are homogeneous degree-five polynomials, as is either iterated corner subtraction. These corner subtractions need not agree: mixed fifth derivatives can depend on the order of taking traces. Each specified operator order nevertheless subtracts only a polynomial. Removing them does not affect any frequency above five.

For the actual higher-order expansion, the y-linear trace remainder is O(x^6(1+|log|x||)), whose derivatives through order five extend at zero as required for P_x^6 P_y^3. The x^2 and x^4 trace remainders have orders y^5(1+|log|y||) and y^3(1+|log|y||), respectively, whose derivatives through order two extend at zero. Thus the iterated subtraction has the displayed leading expansion; no nonexistent general C^6 density jet is being assumed.

A continuous nonzero angular function is bounded away from zero on some closed angular interval avoiding the axes. On that cone the Taylor-subtracted residual has magnitude at least C r^5 for sufficiently small positive r. The product weight is a positive angular factor times r^(-2A_w), and polar area is r dr dtheta. Its squared norm therefore dominates a positive multiple of

integral_0^delta r^(11-2A_w) dr,

which diverges exactly for A_w>=6. The same argument applies to epsilon itself. This is independent of how small the nonzero highest coefficient is.

## Application obligations and scope

The actual d_m are exact dyadic entries D[m,0] of data_exact/modal_v2.json, with R=exp(t_a) and t_a the exact first stored log knot. The inner join corrections have exponent bi>49 and cannot change the r^2 factor term. Exactification of the exterior and canonical normalization leaves these D entries unchanged. The application must check the input hash, exact shape, d_(M-1)!=0, c=3/k-1>0, and the highest coefficient by a separate full Fourier reconstruction.

No C^8-background corner lemma applies to this trial's factor as presently represented. This does not refute that lemma for C^8 backgrounds. It does not rule out a different center representation, a space containing this angular fifth-order component as explicit data, or a regularizing correction. A finite trial residual, even a nonmember of this particular forcing space, supplies neither a YES nor a NO endpoint.

## Exact-input arithmetic application

`code/check_center.py` verifies all1820Dvalues against the pinned binary NPY member using an independent header/payload parser. It requires the exact(260,7)shape, little-endian binary64 type and the stored Fortran-order flag, then converts the physical column-major payload to the row-major JSON order before selecting D[m,0]. It also parses every JSON D entry twice, by an integer hexadecimal parser and by exact binary64 conversion. It reconstructs all 261 positive density modes by trigonometric products, then all 262 positive linear residual modes by the polar transport formula. A second reconstruction multiplies Laurent polynomials in z and conjugate(z), then applies the Cartesian linear vector field to every monomial. All coefficients agree exactly. The highest residual frequency is523.

The raw nonzero d_259 is6648046164061931/10384593717069655257060992658440192. Before the positive factor exp(-2t_a), its residual coefficient is21788186580205656983744084358793575/67106741800540769614338755967513446322238199431168. Arb384 evaluates exp(-2t_a), and independent mpmath.iv160 evaluates1/exp(t_a)^2. Each separately proves that the resulting coefficient lies strictly between5e-12 and6e-12. The intervals also overlap, but overlap is only a consistency check; the independently proved common bracket is the stated enclosure. The raw d_2 is also nonzero.

The complete exact mode lists and arithmetic provenance are in `evidence/exact_modes.json` and `evidence/center_checks.json`. With working A_w=238/25, the divergent radial integrand power is-201/25. The size of the leading coefficient does not affect this divergence.
