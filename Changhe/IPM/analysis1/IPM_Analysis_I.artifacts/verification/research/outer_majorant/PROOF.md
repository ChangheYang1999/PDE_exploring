# An analytic residual majorant on the entire exterior

Date: 2026-10-20. Status: analytic derivation accepted by actual Opus 5.5. The separate evidence/verdict.json records the completed numerical audit and pins the executed sources and outputs. The exact normalized modal trial is the one defined in ../modal_repair/PROOF.md; the sign convention is -Delta psi=partial_x rho and U=(-psi_y,psi_x). This theorem addresses the exterior r>=R=exp(t_b), where t_b is the final exact log knot. It is not a distance estimate to X3 or a linear inverse.

## Exact data and canonical boundary

Write tau=log(r/R)>=0, and write the finite density as

rho(r,theta)=sum_(j=0)^260 rho_j(tau) sin((2j+1)theta),
rho_j(tau)=exp(3t_b) sum_b exp(beta_b tau) c_(j,b)(tau).

Here each c_(j,b) is a polynomial of degree at most6. There are ten degree-zero exponents beta_b=k-j_b(1-k)-2l_b, with (j_b,l_b) in {(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)}, and one correction exponent beta_c=3-b_o. The leading exponent is exactly k with degree0. Here k is the exact rational1615536043799051/9007199254740992. Assume 0<k<1/2, b_o>120, and c_l=1/k exactly. The coefficients are the exact projected modal data plus the exactly defined normalization correction. They must be reconstructed at the common endpoint exp(t_b), not at a separately rounded radius. The largest density sine frequency is521, and the last auxiliary density slot j=261 is identically zero.

Let m=2n, n=1,...,261. For the forcing f_n in partial_x rho, direct polar differentiation gives

r^2 f_n(r)=exp(4t_b) sum_b exp(a_b tau) F_(n,b)(tau),
a_b=beta_b+1,
F_(n,b)=[(a_b-m)c_(n-1,b)+(a_b+m)c_(n,b)+c'_(n-1,b)+c'_(n,b)]/2.

Define the canonical Green quantities

A_n(r)=r^(-m) integral_0^r s^(m+1) f_n(s)ds,
B_n(r)=r^m integral_r^infinity s^(1-m) f_n(s)ds.

Their equations in tau are A_n'=-m A_n+r^2 f_n and B_n'=m B_n-r^2 f_n. The scalar stream coefficient is (A_n+B_n)/(2m). The boundary A_n(R) is recovered from the independently certified lower density moment i_n(t_b):

A_n(R)=exp(4t_b)[(Rhat_(n-1)(t_b)+Rhat_n(t_b))/2-m i_n(t_b)].

Here Rhat_j(t)=exp(-3t)rho_j(t) and i_n(t)=integral_(-infinity)^t exp(-(m+4)(t-v))Rhat_(n-1)(v)dv. The integration-by-parts identity giving this formula is proved in ../modal_green/PROOF.md. The final-span density polynomial, its left lower moments and the exact interval endpoints determine i_n(t_b) by the same canonical integral. An audited archive supplies enclosing balls for these data; its full hash and completed footer must be checked. No exterior velocity or residual from the numerical lane is used.

## Reconstruction of the exact exterior density

The raw modal definition is rho=x^2 y sum_(m=0)^259 a_m(r)cos(2m theta). Since cos^2(theta)sin(theta)=[sin(theta)+sin(3theta)]/4, multiplication by each cosine contributes signed sine amplitudes1/8 at frequencies1+2m,1-2m,3+2m,3-2m, combining coincident frequencies. Equivalently, use the antisymmetric Laurent amplitude array at frequencies +/-1,+/-3, with amplitudes +/-1/4, and convolve it with the cosine array. Positive frequencies then give the same real sine amplitudes. These are exact finite identities, including the m=0 case.

Let A_(j,b) be the exact projection of the ten stored Aout coefficients, let alpha_b=beta_b-3, and let J_(j,v) be the right spline derivative of Rhat_j at t_b. The uncorrected degree-six polynomial e_j(tau)=sum_l e_(j,l)tau^l is uniquely determined by the seven joins:

e_(j,l)=sum_(v=0)^l b_o^(l-v)[J_(j,v)-sum_b A_(j,b)alpha_b^v]/[v!(l-v)!].

Indeed this is the degree-six Taylor polynomial of exp(b_o tau) times the discrepancy between the spline jet and the ten power terms. Multiplying back by exp(-b_o tau) recovers derivatives0 through6. The triangular jet map has diagonal l!, so these equations determine the polynomial uniquely; this is an exact reconstruction, not a least-squares fit. No seventh-derivative join is claimed.

The normalization repair in modal_repair adds z B(tau) to the m=0 radial factor, where

B(tau)=exp(alpha_0 tau)-exp(-b_o tau)sum_(l=0)^6 (alpha_0+b_o)^l tau^l/l!.

This function has seven zero jets at0. Its projection coefficient is C_j=1/4 for j=0,1 and0 otherwise. Thus c_(j,0,0)=A_(j,0)+C_j z, and the correction coefficient is e_(j,l)-C_j z(alpha_0+b_o)^l/l!. Every coefficient is affine in the single exactly defined scalar z. The code imports an already independently audited enclosing interval for z. It does not replace z by its midpoint. The exact scalar k is pinned to the value above, and c_l is defined as1/k, rather than imported from a separately rounded scalar.

The independent endpoint check reconstructs all eight degree-seven spline coefficients by the Cox recursion and compares them to the canonical span archive, including the degree-seven coefficient. It then integrates this exact polynomial by antiderivatives, using the previously audited canonical left moment. The primary method instead reverses the archived polynomial and integrates a rigorously bounded entire series. Both share the previously audited left moments. A fresh third integration of the entire middle region is not asserted or needed for this dependency-based claim. The auditor separately reads and hashes the full compressed archive and checks that the extracted final span is exactly its last span.

## Exact polynomial Green solutions

For a polynomial P(tau)=sum_(l=0)^d p_l tau^l and a nonzero real lambda, let

I_lambda P=sum_(l=0)^d [sum_(v=l)^d (-1)^(v-l) v! p_v/(l! lambda^(v-l+1))] tau^l.

Coefficient comparison gives (I_lambda P)'+lambda I_lambda P=P. This is a finite identity, valid for either sign of lambda. For the exact exterior exponents, assume and verify a_b+m!=0 and a_b-m<0 for every mode and basis. Then set

P^+_(n,b)=exp(4t_b) I_(a_b+m) F_(n,b),
P^-_(n,b)=-exp(4t_b) I_(a_b-m) F_(n,b),
H_n=A_n(R)-sum_b P^+_(n,b)(0).

The canonical solutions are exactly

A_n(tau)=H_n exp(-m tau)+sum_b exp(a_b tau) P^+_(n,b)(tau),
B_n(tau)=sum_b exp(a_b tau) P^-_(n,b)(tau).

For A, differentiation verifies the ODE and the value at tau=0. For B, integrating exp((a_b-m)s) times a polynomial from tau to infinity gives the displayed formula, because a_b-m<0. Thus its homogeneous exp(m tau) term is absent by the canonical upper-integral condition. These arguments establish the formulas rather than fitting their values at the boundary. The possible small lower denominator is checked, never set to zero or discarded.

## Positive coefficient majorant for the true residual

The exact polar velocity factors are

U_r/r=-sum_n (A_n+B_n)/(2r^2) cos(m theta),
U_theta/r=sum_n (B_n-A_n)/(2r^2) sin(m theta).

Consequently their particular terms have exponent beta_b-1, and their transient terms have exponent -m-2. Set their polynomial coefficient bounds, after summing absolute values over n, to P_(b,l), Q_(b,l), respectively. Explicitly, P_(b,l)=exp(-2t_b)sum_n |[P^+_(n,b)+P^-_(n,b)]_l|/2 and Q_(b,l)=exp(-2t_b)sum_n |[P^-_(n,b)-P^+_(n,b)]_l|/2. This prefactor is exp(-2t_b), since P^+ and P^- already include exp(4t_b). Equivalently, using the normalized polynomials p^+=I_(a_b+m)F and p^-=-I_(a_b-m)F, these two bounds have prefactor exp(2t_b)/2. For a transient both bounds equal exp(-2t_b)|H_n|/2. For the density set

D_(b,l)=exp(3t_b) sum_j |beta_b c_(j,b,l)+(l+1)c_(j,b,l+1)|,
E_(b,l)=exp(3t_b) sum_j (2j+1)|c_(j,b,l)|,
L_(b,l)=exp(3t_b) sum_j |(beta_b/k-1)c_(j,b,l)+(l+1)c_(j,b,l+1)/k|,

with missing coefficients zero. For the leading degree-zero basis L is identically zero by beta_b=k, an exact algebraic cancellation before interval evaluation.

The Wiener norm of a real sine/cosine product is at most the product of its two coefficient sums. Indeed each elementary product is the sum or difference of two modes with coefficients1/2, with coincident or zero modes only reducing this bound. Applying this identity to the exact residual

epsilon=(1/k)partial_t rho-rho+(U_r/r)partial_t rho+(U_theta/r)partial_theta rho

gives epsilon=sum_(q=0)^521 epsilon_q(tau)sin((2q+1)theta), with522coefficients and highest sine frequency1043, and the finite nonnegative majorant

W(tau):=sum_(q=0)^521 |epsilon_q(tau)| <= sum_(gamma,l) C_(gamma,l) tau^l exp(gamma tau).

Construct C by adding the linear L terms, then every polynomial convolution P_b D_c+Q_b E_c, including each transient. Particular products have gamma=beta_b+beta_c-1 and degree at most12. Transient products have gamma=-m-2+beta_c and degree at most6. Linear exponents are the nonleading beta_b. Therefore every gamma<=2k-1<0. All modes and all polynomial degrees are retained; aggregation combines equal exact rational exponents without discarding coefficients. Replacing coefficient absolute values and sums by outward upper bounds preserves the inequality.

## Uniform absolute and weighted bounds

For a>0 and integer l>=0, the exact maximum of tau^l exp(-a tau) on tau>=T>=0 is obtained at x=max(T,l/a):

M_(a,l,T)=x^l exp(-a x),

where the l=0 power is1, including at x=0. This follows by differentiation for tau>0 and continuity at0. Thus sum C_(gamma,l) M_(-gamma,l,T) bounds the absolute residual on the full exterior tau>=T, without a finite sampling assumption.

Let u_0=R/L and m(r)=(r/L)^3[1+(r/L)^2]^((k-3)/2). For delta in {0,1/2,1/2-k}, all delta>=0. The identity

(1+r/L)^delta/m(r)=u_0^(delta-k) exp((delta-k)tau)
 *[1+u_0^(-2) exp(-2tau)]^((3-k)/2)
 *[1+u_0^(-1) exp(-tau)]^delta

shows that the last two factors decrease with tau. Put

K_delta(T)=u_0^(delta-k)[1+u_0^(-2)exp(-2T)]^((3-k)/2)
 *[1+u_0^(-1)exp(-T)]^delta.

Then, on tau>=T,

sup (1+r/L)^delta W/m <= K_delta(T)
 *sum_(gamma,l) C_(gamma,l) M_(k-delta-gamma,l,T).

Every rate k-delta-gamma is positive because gamma<=2k-1 and k<1/2. The formula is an exact finite positive sum followed by outward evaluation of scalar exponentials and powers. It does not require the separate numerical-lane monotonicity test or subtraction from an absolute upper bound.

## One explicit exterior L2 consequence

Define N_ext^2=integral_(r>=R) |epsilon/m|^2 dX/[1+(r/L)^2], with the full angular range0<=theta<=2pi. The distinct real sine frequencies give integral |epsilon|^2dtheta<=pi W^2. Also r dr/[1+(r/L)^2]=r^2dtau/[1+(r/L)^2]<=L^2dtau. Minkowski's triangle inequality for the finite positive monomial sum therefore yields

N_ext<=sqrt(pi) L K_0(0) sum_(gamma,l) C_(gamma,l)
 *sqrt((2l)!/[2(k-gamma)]^(2l+1)).

The scalar integral used here is integral_0^infinity tau^(2l)exp(-2(k-gamma)tau)dtau=(2l)!/[2(k-gamma)]^(2l+1), proved by repeated integration by parts. This may be a coarse estimate. Its norm is explicitly stated and is not identified with an unresolved full forcing norm in SPEC.

## Verification requirements and scope

Before accepting any numerical bound, verify the input and canonical archive hashes, exact coefficient reconstruction and joins, all rational rates and polynomial identities, finite outward endpoints, full index counts, and the sums with a different interval implementation. Numerical polynomial cancellation is enclosed before absolute values are taken. A second method must independently reconstruct the polynomial Green solutions and endpoint recovery, rather than copying output sums. The canonical scalar correction and archive are dependencies already audited elsewhere; using them does not independently reintegrate the whole density twice here.

No derivative norm, factor distance from X3, bounded full linear inverse, nonlinear closing estimate, exact profile or exclusion follows from this exterior majorant alone.

## Canonical dependency and numerical scope

The initial lower moment at t_a is the integral over the entire inner half-line in log radius. If the normalized inner coefficient is C+sum_l D_l exp((2l+2)tau)+exp(b_i tau)sum_l E_l tau^l, tau<=0, then

i_n(t_a)=C/(2n+4)+sum_l D_l/(2n+6+2l)+sum_l E_l(-1)^l l!/(2n+4+b_i)^(l+1).

This follows by integrating each exponential polynomial from minus infinity to0. The denominators are positive. The independently audited middle construction starts with this value and propagates through every complete spline span; there is no truncated inner lower limit. The exact initialization is in ../middle_residual/code/modal_setup.py and the propagation in build_knot_moments.py. Their proof and executed source hashes, the canonical archive audit and the modal normalization proof are pinned by this topic's final verdict. The archive audit is a source, structure and selected independent-moment comparison audit; it is not mislabeled as a second complete reintegration of the archive. The independent exterior computation adds a second formula for the final-span propagation.

The completed computation uses Arb384 and mpmath.iv160, checking8908 affine density coefficient components,1834 exact joins,2096 Cox polynomial coefficients,17748 affine Green coefficient components, and4394 interval containments. It retains1864 exact exponents and3508 monomials. All2871 upper-integrability inequalities and lower nonzero denominators are checked exactly. The final verdict records the minimum lower denominator.

For the entire exterior tau>=0, the conservative public upper bounds are

sup W < 17145164,
sup W/m < 5740483,
sup (1+r/L)^(1/2)W/m < 121375357,
sup (1+r/L)^(1/2-k)W/m < 40621858,
N_ext < 4949755.

For tau>=9 the corresponding unweighted and normalized bounds are sup W<0.498894793 and sup W/m<0.033247226. These bounds are far too large to support a perturbative closing estimate. They discard cancellation between the linear and nonlinear exterior coefficients and between Green particular and transient terms. Their role is a fully checked finite exterior bound and a source of exact Green constituents for a future sharper calculation. The inequalities are confirmed by exact rational comparison to both sets of outward endpoints in evidence/verdict.json; decimal displays in logs are not used as endpoints.
