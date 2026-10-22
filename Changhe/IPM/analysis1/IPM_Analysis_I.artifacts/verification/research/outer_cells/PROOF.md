# Complete log-cell bounds for the exterior residual

Date: 2026-10-20. Status: analytic derivation written before implementation. This note proves the general enclosure theorem; the exact numerical application and its status are recorded separately in evidence/verdict.json after complete independent output audits. This is a zeroth residual bound for the exact normalized modal trial. It does not assert an inverse theorem, closeness to X3 or derivative bounds.

## Inputs and exact residual

Use the exact modal density and canonical Green decomposition proved and audited in ../outer_majorant/PROOF.md, with its pinned verdict, exact affine polynomial coefficients and canonical transient intervals. Put R=exp(t_b), tau=log(r/R), k=1615536043799051/9007199254740992 and c_l=1/k. The scale is L=8614738245908811/1125899906842624. For j=0,...,260, nu_j=2j+1 and n=1,...,261, m_n=2n, write

rho_j=R^3 sum_b exp(beta_b tau)c_(j,b)(tau),
D_j=partial_tau rho_j=R^3 sum_b exp(beta_b tau)[beta_b c_(j,b)+c'_(j,b)],
H_j=nu_j rho_j,
E_j=R^3 sum_b exp(beta_b tau)[(beta_b/k-1)c_(j,b)+c'_(j,b)/k].

All c are exact affine functions of the single normalization scalar z, enclosed by its audited interval; no midpoint replacement is made. There are eleven bases, the ten constant-degree exterior powers and one degree-six correction. Define the already audited normalized Green polynomials q^+_(n,b), q^-_(n,b) and h_n=H_n/R^4 as in outer_majorant. Then

p_n=R^2{sum_b exp((beta_b-1)tau)[-(q^+_(n,b)+q^-_(n,b))/2]-h_n exp((-m_n-2)tau)/2},
s_n=R^2{sum_b exp((beta_b-1)tau)[(q^-_(n,b)-q^+_(n,b))/2]-h_n exp((-m_n-2)tau)/2}.

The full true residual, including canonical transients, is exactly

epsilon(tau,theta)=sum_j E_j sin(nu_j theta)
 +(sum_n p_n cos(m_n theta))(sum_j D_j sin(nu_j theta))
 +(sum_n s_n sin(m_n theta))(sum_j H_j cos(nu_j theta)).

Every beta, polynomial degree, density mode and velocity mode is retained. The resulting sine frequencies are1,3,...,1043. Set W(tau)=sum_(q=0)^521 |epsilon_q(tau)|, so |epsilon|<=W. The input decomposition has already been reconstructed from exact source data and the canonical full-plane inverse; this note treats that audit as an explicit dependency. A second integration of all interior moments is not claimed.

## Taylor model on a complete interval

Fix exact rationals0<=a<b, t_c=(a+b)/2 and h=(b-a)/2. Let v=(tau-t_c)/h, so |v|<=1. A Taylor model (P,r) means f(tau)=P(v)+e(v), where P is a degree at most Q polynomial, all its real coefficients lie in the recorded interval coefficients, and |e|<=r throughout the interval. Coefficient interval dependence may be forgotten because this enlarges the set of possibilities. Require Q>=6.

For an input term exp(lambda tau)c(tau), shift its polynomial exactly or by enclosing arithmetic:

c(t_c+hv)=sum_(l=0)^d A_l v^l,
A_l=h^l sum_(j=l)^d binom(j,l)c_j t_c^(j-l).

Put ell=lambda h. The retained Taylor polynomial has coefficients

P_q=exp(lambda t_c) sum_(l=0)^min(q,d) A_l ell^(q-l)/(q-l)!, 0<=q<=Q.

A valid uniform remainder is

r=exp(lambda t_c) exp(|ell|) sum_(l=0)^d |A_l| |ell|^(Q-l+1)/(Q-l+1)!.

Indeed for each l, truncate the exponential series at Q-l. Its absolute tail on |v|<=1 is at most exp(|ell|)|ell|^(Q-l+1)/(Q-l+1)!, since (N+j)!>=N!j!. Multiplication by |A_l v^l| and summation prove the claim. Interval upper endpoints enlarge this bound. The exact maximum |lambda|h across all density, velocity and transient terms is recorded for each cell. It is524h for these inputs, since the final transient has lambda=-524; the middle-region value522h is not used. All scalar exponential prefactors R^2 and R^3 are also enclosed. Taylor models for each D_j,H_j,E_j,p_n,s_n are obtained by summing the finitely many input-term polynomials before taking coefficient absolute values and summing their uniform remainders. Thus cancellations between the radial exponentials are retained in the polynomial part. The exact leading linear coefficient vanishes before interval evaluation.

Let N(P)=sum_l |P_l|, bounded with coefficient interval absolute upper endpoints. For two scalar models (P,r),(Q,s), the difference between their exact product and P Q has absolute value at most N(P)s+N(Q)r+rs. For finite sine and cosine expansions the same estimate holds in the real Fourier coefficient sum norm, using the sums of the model polynomial norms and remainder bounds over all physical modes. This follows from the two elementary product-to-sum identities, whose absolute coefficient sums are at most the products of the two input sums. It remains valid for the residual product because the even and odd frequencies have no zero-frequency collision.

## Primary angular product and radial truncation

The primary method encodes a real cosine coefficient f_n as f_n/2 at integer frequencies plus and minus n, and a real sine coefficient as f_n/2 at frequency minus n and -f_n/2 at plus n, removing a common factor i. Each nonlinear product has precisely one sine factor, so the same representation is preserved. Shift all frequencies to nonnegative indices and encode a coefficient at angular index k and radial degree l at univariate power (2Q+1)k+l. Since products have radial degree at most2Q, no radial carry can alias angular indices. Polynomial multiplication gives the exact finite angular and radial product in interval arithmetic. The physical sine coefficient is the negative-frequency coefficient minus the positive-frequency coefficient.

Add the independently formed linear polynomial with its correct angular offset. Retain radial degrees0,...,Q; bound all degrees Q+1,...,2Q in the physical sine coefficient sum by their coefficient absolute sums, denoted R_high. No angular frequency is discarded. The nonlinear Taylor-model remainder and the linear remainder give R_nonpoly. These bounds are uniform on the entire interval, not samples at the center.

For each retained real sine polynomial p_q(v), set x=(v+1)/2. Its Bernstein coefficients at degree Q are

b_(q,k)=sum_(i=0)^k binom(k,i)/binom(Q,i) 2^i sum_(l=i)^Q (-1)^(l-i)binom(l,i)p_(q,l).

This follows by substituting v=2x-1 and using x^i=sum_(k=i)^Q binom(k,i)/binom(Q,i) B_(k,Q)(x). Bernstein basis functions B_(k,Q) are nonnegative and sum to1 on[0,1], so |p_q(v)|<=max_k |b_(q,k)|. Therefore

B_W=sum_q max_k |b_(q,k)|+R_high+R_nonpoly

is a proved upper bound for W on the whole log-cell.

## Independent integer interval convolution

The independent method constructs the Taylor models using mpmath.iv and independently evaluates the finite Green polynomial recurrence. The recurrence q_d=f_d/lambda, q_l=[f_l-(l+1)q_(l+1)]/lambda solves q'+lambda q=f; the minus Green polynomial uses its negative. The equality with the pinned exact affine Green coefficients is checked with rational arithmetic. Canonical transient intervals are shared audited dependencies, with their provenance stated.

It uses compressed angular indices: even frequency2n has index n, odd frequency2j+1 has index j. Cosine velocity has coefficients p_n/2 at both indices plus and minus n; sine velocity has coefficients s_n and -s_n, with the common1/(2i) removed. Density sine D has coefficients D_j and -D_j at j and -j-1; cosine H has H_j/2 at both. The product's positive coefficient is the physical sine amplitude. With even and odd offsets261, output positive q is at index522+q. These indices are distinct from the primary full-frequency representation. The radial Kronecker base is again2Q+1, as forced by the degree bound.

For a fixed integer precision P_int, enclose each iv coefficient by an interval [(M-R)2^-P_int,(M+R)2^-P_int] with integer M and nonnegative integer R, rounding its lower endpoint down and upper endpoint up. For two arrays of these intervals, let * denote exact integer polynomial convolution. The product center and radius arrays are

M_out=M_x*M_y,
R_out=|M_x|*R_y+R_x*|M_y|+R_x*R_y,

with scale2^-2P_int. To prove the enclosure, write each coefficient as2^-P_int(M+delta), |delta|<=R, expand each product and apply the finite coefficientwise triangle inequality. All convolutions in this calculation are exact integer operations using fmpz_poly, so this stage has no floating-point rounding. Enclose and add the linear coefficients at the product scale. The independent code does not import primary convolution coefficients or primary remainder bounds.

Bernstein coefficients can also be bounded by exact integer arithmetic. Multiplying the rational Bernstein matrix by Q! makes every entry an integer, since binom(Q,i) divides Q!. For an input coefficient center vector M and radius vector R, form the transformed centers by matrix multiplication and the transformed radii by multiplication with the entrywise absolute matrix. The absolute upper endpoint is (|center|+radius)/(2^(2P_int)Q!). This proves every independent Bernstein bound. The discarded high degrees have denominator2^(2P_int), and the nonpolynomial remainders are independently computed with iv.

Both constructions individually give valid enclosures under the stated dependencies. Coefficient-interval overlap is a consistency check, not the proof of either enclosure. Publication uses an exact rational upper bound at least as large as both independently computed B_W values; no mere overlap is treated as proof of a numerical inequality. Any disagreement in exact source identities, missing cell, nonfinite interval or disjoint residual coefficient enclosures is an unaccepted audit that must be resolved explicitly.

## Normalized, weighted and L2 consequences

Let u=r/L and m(r)=u^3(1+u^2)^((k-3)/2). Its logarithmic derivative is [3+k u^2]/[1+u^2]>0, since k>0. Thus on the log-cell a<=tau<=b,

W/m <= B_W/m(R exp(a)),
(1+r/L)^delta W/m <= (1+R exp(b)/L)^delta B_W/m(R exp(a))

for delta>=0. All endpoint powers and exponentials are enclosed in each implementation. For the full-angle weighted L2 norm on this annulus, define N_C^2=integral_C |epsilon/m|^2 dX/(1+(r/L)^2). Orthogonality of distinct real sine frequencies gives the upper bound

N_C^2 <= pi (B_W/m(R exp(a)))^2 (L^2/2)
             log[(1+(R exp(b)/L)^2)/(1+(R exp(a)/L)^2)].

This follows by integrating r/[1+(r/L)^2] exactly and using sum|epsilon_q|^2<=W^2. The L2 claim concerns precisely this measure and does not assert any target derivative norm.

For a finite ordered list0=a_0<a_1<...<a_N=T, maxima of the proved cell bounds give the bounds on0<=tau<=T, and the squared L2 cell bounds add. The complete covering must be checked with exact rational endpoints. The independently confirmed tail bound in ../outer_leading_cancellation/PROOF.md, pinned by verdict6a56059e5b9e2041ad94aed5be982b19b94d0b23f0c00563a20452b314ba89f9, handles tau>=T for zeroth suprema when evaluated at exactly the covering endpoint T. A tail L2 bound must be evaluated on that same half-line before any sharper full-exterior L2 claim. Selected cells alone prove no bound in gaps between them. Any full-region numerical assertion requires complete rows and the exact covering audit described here.

## Half-line L2 bound for joining to the cells

Let D_(gamma,l) be the already audited exterior majorant with the entire leading row replaced by the exact rational upper endpoint of C_star. These coefficients are nonnegative exact rational inputs, so their reuse is explicit. Set u_0=R/L and

K_0(T)=u_0^(-k)[1+u_0^(-2)exp(-2T)]^((3-k)/2), a_gamma=k-gamma>0.

For tau>=T, the earlier weight identity and monotonicity give

W/m <= K_0(T) sum_(gamma,l) D_(gamma,l) tau^l exp(-a_gamma tau).

Therefore the exterior tail L2 norm satisfies

N_tail(T) <= sqrt(pi)L K_0(T) sum_(gamma,l) D_(gamma,l) sqrt(I_(2l)(2a_gamma,T)),
I_n(lambda,T)=integral_T^infty tau^n exp(-lambda tau)dtau.

The same angular orthogonality, radial-measure inequality and finite-sum Minkowski argument used above prove this bound. For nonnegative integer n and lambda>0, substitute tau=T+s and integrate the finite binomial expansion to obtain

I_n(lambda,T)=exp(-lambda T) sum_(j=0)^n binom(n,j)T^(n-j)j!/lambda^(j+1).

Alternatively integration by parts gives I_0=exp(-lambda T)/lambda and I_n=T^n exp(-lambda T)/lambda+n I_(n-1)/lambda. These two formulas give independent interval evaluations without an unbounded special-function tail. The limit at infinity is zero because a positive exponential dominates every fixed polynomial. N_exterior^2 is bounded by the sum of the squared cell bounds and N_tail(T)^2; there is no double counting except measure-zero boundaries. No numerical L2 tail value is asserted until both evaluations pass and are pinned.
