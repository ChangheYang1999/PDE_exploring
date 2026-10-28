# A finite-radius certificate for the far residual tail

## Statement

Use the actual normalized C6 modal trial, k, t_+, alpha_0=k-3, alpha_1=2k-4, and S from proof 117. Let alpha_2=3k-5 and beta_0=k-1, beta_1=2k-2. All coefficients and norms below refer to the fixed target Y=E G direct-sum R, with G radial weight exp(27t/4) at the outer end. This statement concerns that specific axis norm.

Suppose the exact modal expansions give, for every s>=0 at a chosen T>t_+,

 ||F(T+s,.)/r^3-exp(alpha_1(T+s-t_+))S||_(sine coefficient l1)
 <= B_T exp(alpha_2 s).                                      (1)

Let N bound the residual sine indices, C_N=4N^4(2N+1), M=2 Beta(1/4,3/2), and r_0=4k-5/4<0, r_2=6k-13/4<0. Put

 L_R(T)=[exp(27T/4+2alpha_1(T-t_+)) E_S/(-r_0)]^(1/2),
 D_R(T)=sqrt(M) C_N B_T exp(27T/8)/sqrt(-r_2),                 (2)

where E_S is the angular squared remainder norm of S. Then the actual remainder tail obeys

 max(0,L_R(T)-D_R(T))^2
 <= integral_T^infinity e_R(t)dt
 <= [L_R(T)+D_R(T)]^2.                                      (3)

For the complete Y tail replace E_S in L_R by E_S+gamma_S^2, and sqrt(M) in D_R by sqrt(1+M). These constants are deliberately conservative.

## Proof of the angular and integral bounds

The finite sine-to-cosine division by sin(theta) has coefficient l1 norm at most2N+1. The exact division by cos(theta)^2 on the conforming range, or the division after subtracting the axis value, has norm at most2N^2, by the explicit quotient formula of proof 98. Composing both divisions gives C_N. Thus the remainder quotient has supremum at most C_N times the input sine coefficient norm. Its angular L2 norm is at most sqrt(M) times that supremum. The intermediate axis value has norm at most2N^2(2N+1), which is no larger than C_N for N>=1. Consequently the full angular norm is bounded by sqrt(1+M) C_N times the sine coefficient norm. The exact error in (1) is conforming because both the actual residual and its leading term are conforming.

Multiplying (1) by the square root exp(27(T+s)/8) of the target weight and integrating its square gives D_R(T), since 2alpha_2+27/4=r_2. The leading term has exact tail norm L_R(T), since 2alpha_1+27/4=r_0. The triangle and reverse triangle inequalities in the tail L2 space prove (3). No point-sampling extrapolation is used.

## Construction of B_T from the exact modal expansions

Write h=(h_j) for the sine coefficients of rho/r^3, h_0=A exp(alpha_0 tau), h_*=h-h_0, P=P_0+P_*, Q=Q_0+Q_*, with tau=t-t_+. Here P_0 and Q_0 are the velocity terms at exponent beta_0. Let D h=3h+h' and Theta h=((2j+1)h_j). The exactly cancelled linear residual is Lh=ell D h-h. Remove its term (1-ell) B exp(alpha_1 tau) as well and call the result L_*.

The error after the leading term is exactly

 L_*-P_0 D h_*-P_* D h+Q_0 Theta h_*+Q_* Theta h.              (4)

Products mean the usual angular products. Their coefficient l1 norms are bounded by the products of the corresponding norms, by the sine/cosine product formulas. The rates of the five terms in (4) are at most alpha_2: L_* has rate alpha_2, P_0 and Q_0 have rate beta_0, h_* has rate alpha_1, P_* and Q_* have rate beta_1, and h has rate alpha_0. Derivatives D and Theta do not change these rates. The actual matching exponent is -b_o, with b_o>125, and the exterior harmonic rates are at most-4, so none is slower than the stated bounds.

For an exponential polynomial f(tau)=sum_e exp(e tau)p_e(tau), shift tau=T-t_++s and write its shifted polynomial coefficients as p_(e,j;T). To bound f by B exp(a s), assume every nonzero term has e<=a, and every term with e=a is constant. Then

 B=sum_(e<a) sum_j |p_(e,j;T)| j!/(a-e)^j
   +sum_(e=a)|p_(e,0;T)|                                   (5)

is valid. The exponential exp(e(T-t_+)) is included in the shifted coefficients. Indeed s^j exp(-(a-e)s)<=j!/(a-e)^j follows from one nonnegative term of the exponential series. Formula (5) applies separately to all modal coefficients and their D derivatives. Summing the resulting positive bounds in (4) gives B_T.

## Data and scope

The code reconstructs only the outer coefficients from the read-only original NPZ: exact binary-rational data, the C6 endpoint matching correction, and the already certified scalar normalization interval. It uses the independently certified outer Green boundary moments from proof 68 and checks their source hash. This is the same exact modal object as topics105 and117. A lightweight reconstruction avoids computing unused interior spline coefficients. The leading angular coefficient is checked against proof 117's independent full reconstruction.

The resulting certificate concerns the outer half-line only. A complete residual upper bound still needs the interval between the origin and T. All endpoint values and bounds are recorded with exact outward rational endpoints.
