# A center residual bound with the canonical strain removed first

Date: 2026-10-20. Status: CONFIRMED for the explicitly repaired modal trial, with the independently audited canonical moment archive as a stated dependency. The scalar-maximum extension and both numerical sources were accepted by actual Claude Opus 5.5 after follow-up; independent interval recomputation passed at 16:52:56Z. The statement is an a priori inequality for an explicitly given trial, not an existence theorem.

## Statement

Fix an integer J>=1. Let rho be a real angular sine series with global frequencies contained in {1,3,...,2J+1}, even in x and odd in y. All its radial coefficients are C^1 for r>0. Use the canonical full-plane equations -Delta psi=partial_x rho and U=(-psi_y,psi_x), with the positive Green formula below. Assume the improper upper Green integrals converge absolutely for every n=1,...,J+1, including integral_1^infinity |f_1(s)|/s ds. Fix R>0 and require the following identity on the whole disk 0<r<=R:

rho(r,theta)=rho_0(r,theta)+eta(r,theta),
rho_0=x^2 y=r^3(sin(theta)+sin(3theta))/4,
eta=sum_(j=0)^J eta_j(r) sin((2j+1)theta).

Suppose finite nonnegative numbers d_j,e_j satisfy, for 0<r<=R,

|eta_j(r)|<=d_j r^5,  |r eta_j'(r)|<=e_j r^5.

Extend these sequences by zero beyond their listed indices. Set nu_j=2j+1, N=J+1, and for n=1,...,N let

F_n=(e_(n-1)+nu_(n-1)d_(n-1)+e_n+nu_n d_n)/2.

Define D=sum_j d_j, E=sum_j e_j, Q=sum_j nu_j d_j. Let c=psi_xy(0) be the canonical strain, assume exactly 3 c_l-c=1, and let B_n(R) be the canonical upper Green moment

B_n(R)=R^(2n) integral_R^infinity s^(1-2n) f_n(s) ds,
partial_x rho=sum_n f_n(r) sin(2n theta).

For m=2n>=4 set C_m=1/2 when m=4, and C_m=1/(m-4) when m>=6. Define

H=(3/16)F_1 R^2
  +(1/2) sum_(n=2)^N [ |B_n(R)|/R^4+F_n R^2(1/(2n+6)+C_(2n)) ],
C_r=1/6+H, C_theta=1/3+H,
B_5=|c_l|E+D+|c|(E+Q)+(3/2)C_r+C_theta
     +R^2(C_r E+C_theta Q).

Then the angular Wiener norm W of the full stationary residual satisfies

W(r):=sum_l |epsilon_l(r)| <= B_5 r^5,  0<r<=R,
epsilon=(c_l X+U[rho]) dot grad rho-rho.

For this pure odd sine series, W is the usual complex Fourier l1 norm. In particular it bounds the pointwise angular supremum. For 0<k<1, L>0 and m(r)=(r/L)^3[1+(r/L)^2]^((k-3)/2),

sup_(0<r<=R) W(r)/m(r) <= B_5 R^5/m(R).

The same bound multiplied by (1+R/L)^delta holds after multiplying W/m by (1+r/L)^delta, for any delta>=0.

## Forcing coefficients

In polar coordinates partial_x=cos(theta) partial_r-sin(theta)r^(-1)partial_theta. The sine product identities give the coefficient at sin(2n theta):

(partial_x eta)_n
 = (eta_(n-1)'-(2n-1)eta_(n-1)/r)/2
   +(eta_n'+(2n+1)eta_n/r)/2.

The stated d,e bounds therefore imply |(partial_x eta)_n(r)|<=F_n r^4. Also partial_x rho_0=2xy=r^2 sin(2theta). Hence f_1=r^2+q_1, f_n=q_n for n>=2, with |q_n(r)|<=F_n r^4.

## Canonical velocity and the strain decomposition

Put m=2n and

A_n(r)=r^(-m) integral_0^r s^(m+1) f_n(s) ds,
B_n(r)=r^m integral_r^infinity s^(1-m) f_n(s) ds.

The canonical Green formula and its differentiated identity are

psi_n=(A_n+B_n)/(2m),
psi_n'=(B_n-A_n)/(2r).

Indeed A_n'=-m A_n/r+r f_n, B_n'=m B_n/r-r f_n. The resulting velocity has radial coefficient -m psi_n/r and tangential coefficient psi_n'.

For n=1, convergence gives c=(1/2)integral_0^infinity f_1(s)/s ds. Thus

A_1=r^4/6+a_1,
B_1=2c r^2-r^4/2+b_1,
|a_1|<=F_1 r^6/8,  |b_1|<=F_1 r^6/4.

The n=1 stream coefficient is c r^2/2-r^4/12+(a_1+b_1)/4. Its first term is cxy and gives the affine velocity U_lin=(-cx,cy). After subtracting it, the radial velocity coefficient has absolute value at most r^3/6+(3/16)F_1 r^5, and the tangential coefficient has absolute value at most r^3/3+(3/16)F_1 r^5. These constants follow from the exact cubic contributions before taking absolute values.

For n>=2, the lower moment obeys |A_n(r)|<=F_n r^6/(m+6). Split the upper integral at R:

B_n(r)=(r/R)^m B_n(R)+r^m integral_r^R s^(1-m)q_n(s) ds.

Dividing by r^4, the first term is at most |B_n(R)|/R^4 because m>=4. The second is at most

F_n r^(m-4) integral_r^R s^(5-m) ds.

For m=4 this is F_n(R^2-r^2)/2<=F_n R^2/2. For m>4, write its integral as integral_r^R (r/s)^(m-4) s^2 ds/s and use s^2<=R^2. The result is at most F_n R^2[1-(r/R)^(m-4)]/(m-4)<=F_n R^2/(m-4). In particular this estimate includes m=6 without any division by the resonant exponent 6-m or any logarithmic monotonicity claim.

Each of the radial and tangential velocity coefficients is bounded by (|A_n|+|B_n|)/(2r). Summing the preceding estimates proves

||U_rem,r(r,.)||_W <= C_r r^3,
||U_rem,theta(r,.)||_W <= C_theta r^3,
U_rem=U[rho]-U_lin.

This also verifies the stated affine strain at zero under the hypotheses: the remainder is O(r^3). The formula for c comes directly from the n=1 Green integral and agrees with psi_xy(0). For completeness, the bounds give psi-cxy=O(r^4) and its first derivatives O(r^3). The radial mode equation psi_n''+psi_n'/r-m^2 psi_n/r^2=-f_n then bounds the second radial derivatives of the remainder by O(r^2). Finitely many angular modes give the corresponding Cartesian second-derivative bounds, so the mixed derivative at zero is indeed c.

## Residual estimate

Let V_lin=c_l X+U_lin. In polar coordinates its radial component is r(c_l-c cos(2theta)) and its tangential component is cr sin(2theta). Exact normalization gives

(V_lin dot grad-1)rho_0=(3c_l-c-1)rho_0=0.

Consequently

epsilon=(V_lin dot grad-1)eta+U_rem dot grad rho_0+U_rem dot grad eta.

The Wiener norm is submultiplicative, because the product's Fourier coefficients are the convolution of the factors' coefficients and the triangle inequality bounds its l1 norm. A sine or cosine of a nonzero integer frequency has Wiener norm1. The eta bounds give

||(V_lin dot grad-1)eta||_W/r^5 <= |c_l|E+D+|c|(E+Q).

The two polar derivatives of rho_0 have norms

||partial_r rho_0||_W=(3/2)r^2,
||r^(-1)partial_theta rho_0||_W=r^2.

Therefore ||U_rem dot grad rho_0||_W/r^5 <=(3/2)C_r+C_theta. The corresponding derivatives of eta have norms at most E r^4 and Q r^4, so

||U_rem dot grad eta||_W/r^5 <=r^2(C_r E+C_theta Q)
 <=R^2(C_r E+C_theta Q).

Adding these bounds proves the stated B_5 estimate.

Finally, with u=r/L, the logarithmic derivative of m is (3+k u^2)/(1+u^2), which is at most3 when 0<k<1. Thus r^5/m is increasing, with logarithmic derivative at least2. The additional positive weight with delta>=0 is also increasing. This proves the two uniform weighted consequences.

## Obtaining the d,e bounds from the exact modal trial

The independent modal definition uses t_a equal to its exact first spline knot, tau=log(r)-t_a, and

eta_j(r)=r^3 sum_(alpha,l) c_(j,alpha,l) exp(alpha tau) tau^l,

where all alpha are real and alpha>=2. The alpha=2 terms have l=0. The remaining powers are in {4,6,...,14}, each with polynomial degree zero, together with the inner correction exponent b_i, of polynomial degree at most6. The cubic part is checked separately: its coefficients are exactly1/4 at sin(theta) and sin(3theta), with no other cubic term and no cubic logarithm. Its exact rational input must be checked to satisfy b_i>=49; no rounded description of that exponent is used. Take R=exp(t_a-T). If T>=l/(alpha-2) for every nonzero term with alpha>2, then |tau|^l exp((alpha-2)tau) is increasing on tau<=-T, as follows by differentiating its logarithm. Therefore valid choices are

d_j=exp(-2t_a) sum_(alpha,l) |c_(j,alpha,l)| exp(-(alpha-2)T) T^l,
e_j=exp(-2t_a) sum_(alpha,l) |(3+alpha)c_(j,alpha,l)+(l+1)c_(j,alpha,l+1)| exp(-(alpha-2)T) T^l.

Terms beyond the stored polynomial degree are zero. The special alpha=2,l=0 terms are constant after division by r^5 and satisfy the same formula. Every monotonicity condition must be checked from the exact rational alpha,T values for both the original and regrouped derivative polynomials. The derivative polynomial has no larger degree and has the same exponent, so checking all degrees0,...,6 for each correction exponent suffices. This gives a finite exact/interval computation with no tail truncation. The independent boundary B_n(R) can be obtained from the already certified canonical density moments by integrating the explicit inner representation. Its computation and independent output audit are recorded below.

## A version covering the entire inner interval

The preceding sufficient endpoint monotonicity condition can be removed by evaluating each scalar monomial at its exact maximum. For T>=0, alpha>2 and integer l>=0, put

x_(alpha,l)=max(T,l/(alpha-2)),
M_(alpha,l)(T)=x_(alpha,l)^l exp(-(alpha-2)x_(alpha,l)).

Interpret x^0 as1, including x=0. The derivative of x^l exp(-(alpha-2)x) has the sign of l-(alpha-2)x for x>0. Thus M is exactly its maximum on x>=T. For alpha=2,l=0 set M=1. Replace every exp(-(alpha-2)T) T^l in the formulas for d_j,e_j by M_(alpha,l)(T). These choices are valid for every T>=0. In particular T=0 covers the complete inner region 0<r<=exp(t_a), rather than leaving a finite inner annulus. This is a scalar maximum calculation; it does not bound the residual by its endpoint value.

For the canonical B_n(R), define Rhat_j by rho=r^3 sum_j Rhat_j(log r) sin((2j+1)theta). Integration by parts in the upper Green integral gives, for m=2n,

B_n(R)/R^4=m j_n(log R)-(Rhat_(n-1)(log R)+Rhat_n(log R))/2,
j_n(t)=integral_t^infinity exp((4-m)(v-t)) Rhat_n(v) dv.

This identity additionally requires the boundary terms exp((4-m)v)Rhat_j(v) to tend to zero and the corresponding derivative integrals to converge absolutely. These hypotheses hold for the explicit modal extension: each Rhat_j is a finite sum of exponentials with rates alpha<=k-3< -2, and polynomial-times-exp(-b_o v) terms with b_o>0 large enough that 4-m-b_o<0, together with their derivatives. For every m>=2 the largest combined rate is k-1<0. The finite matching knots preserve continuity; the inner and spline jets are checked exactly through order6. This identity follows directly by inserting f_n=r^2[(Rhat_(n-1)'+Rhat_n')/2+(2-n)Rhat_(n-1)+(2+n)Rhat_n] and integrating the derivative term. If a=t_a, R=exp(a-T), then

j_n(a-T)=exp((4-m)T)j_n(a)+integral_0^T exp((4-m)v) Rhat_n(a-T+v) dv.

For the first spline interval [a,b] and its exact polynomial p_n about (a+b)/2,

j_n(a)=exp((4-m)(b-a))j_n(b)+integral_0^(b-a) exp((4-m)v) p_n(a+v-(a+b)/2) dv.

These finite integrals use complete exponential-polynomial formulas, including zero and near-zero exponents. For T=0 the second integral vanishes. Each j_n(b) must be taken from the independently audited canonical moment archive for the repaired density. In that archive, j_right[n-1] is the density integral of Rhat_n with rate4-2n at the right endpoint, and density_polynomials[n] contains the degree7 coefficients of Rhat_n about the span midpoint. The backward loop in build_knot_moments.py integrates precisely that index, initialized from the exact repaired outer representation; modal_green/PROOF.md and middle_residual/PROOF.md give its construction and audit. The local computation also checks the strain identity c=exp(2t_a)[j_1(t_a)+integral_(-infinity)^0 exp(2tau)Rhat_1(t_a+tau)d tau] against the exact rational3/k-1. This is a consistency check in addition to, and not a replacement for, the exact normalization theorem. All arithmetic uncertainty is retained when taking the positive B_5 majorant.

## Exact normalization under interval arithmetic

The hypothesis 3c_l-c=1 is an exact identity, not the assertion that two numerical intervals overlap. It can be enforced by setting c_l=(1+c)/3. In the normalized modal application, it instead follows from the exact repair definition c=3/k-1, with c_l=1/k; the separate modal_repair/PROOF.md proves that this is the canonical strain of the same density. A finite-precision ball for c or the Green moment does not replace that symbolic identity. Once exact normalization is established, separate enclosing bounds for |c| and |c_l| in the positive formula B_5 are safe even if they discard correlation. Without the exact identity, a cubic residual remains and the r^5 conclusion is not asserted.

## Scope and dependencies

Dependencies are the canonical Green formula, finite Fourier identities, elementary integration and interval bounds on explicitly listed scalar inputs. The estimate controls only the zeroth residual and its r^5 center behavior on this inner disk. It says nothing about derivative residual norms, the annulus outside R, a distance to X3, an inverse operator or a closing fixed-point inequality. The polynomial degree is finite and all sums above are finite. No arbitrary exterior strain may be added: c and B_n(R) must come from the same canonical trial.

## Verified numerical application, 2026-10-20T16:52:56Z

The exact repaired modal definition and the independently audited original-knot archive give the following upward-rounded bounds. Here R=exp(t_a-T); every bound is uniform for 0<r<=R. The final column uses u=r/L.

| T | B_5 upper bound | sup W/m upper bound | sup (W/m)(1+u)^(1/2) upper bound |
|---|---|---|---|
| 0 | 1.77720288286255 | 0.04660678400642 | 0.04663008157548 |
| 1/8 | 1.62972571399884 | 0.03328533171603 | 0.03330001557820 |
| 5/2 | 1.55763625124964 | 0.00027523594803 | 0.00027524724417 |

The T=0 row covers the entire inner disk 0<r<=exp(t_a), whose endpoint is about 0.00765142460138. These coarse bounds preserve exact cubic cancellation; they do not exploit the small fifth-order residual seen in floating samples. The primary Arb computation was independently recomputed with mpmath.iv at 160 decimal digits. The audit checked 7860 exact coefficient, Cox-polynomial and join identities, plus 1318 enclosure containments per cutoff. All passed. It reconstructed the angular transform by Laurent coefficients and used exact antiderivative endpoint formulas or integrated exponential Taylor series for the finite moments, independently of the primary moment recurrence. The canonical exterior archive remains a shared, separately audited dependency.

Files: `code/certify_inner.py`, `code/audit_inner_iv.py`, `evidence/inner_result.json`, `evidence/inner_iv_audit.json`, and `evidence/verdict.json`. The verdict pins their hashes and the actual review metadata.
