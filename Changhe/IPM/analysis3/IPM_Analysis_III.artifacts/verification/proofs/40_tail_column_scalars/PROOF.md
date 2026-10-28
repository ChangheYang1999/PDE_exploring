# Independent strain integrals of the S0 tail columns

## Exact definitions

The S0 finite section uses the exact modal input identified by SHA-256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874, with the scalar normalization repair from V005. Let t_plus be the last exact dyadic knot, k the exact input exponent, and a_m the repaired outer coefficient Aout[m,0]. Let chi(t) be the sum of the last ten clamped degree7 B-splines on the exact input knots, extended by zero to the left and by one to the right. This is a nonnegative C6 cutoff.

Put tau=t-t_plus. The two scalar columns are

 KP_s=x^2 y chi(t) tau exp((k-3)tau) sum_{m=0}^{259} a_m cos(2m theta),
 TAU=x^2 y chi(t) exp((k-3)tau) sum_{m=0}^{259} b_m cos(2m theta).

Here b_0=a_1/2, b_1=a_0+a_2/2, and b_m=(a_{m-1}+a_{m+1})/2 for m>=2, with a_260=0. This deliberately truncates the extra cosine mode260 of the exact product with cos(2theta). Its omission has no effect on strain, since the strain functional sees only modes0 through3.

These columns use tau=log r-t_plus. They must not be identified with the theoretical column KP_log=chi log(r) r^k Theta, which uses log r. If Phi=chi r^k Theta with the same physical leading angular profile, then

 KP_log=KP_s+t_plus Phi.                                    (1)

## Integral formula and independent evaluation

The exact angular strain weights are (1/4,1/8,-1/8,-1/8) on modes0,1,2,3 and zero thereafter. Let C_A and C_B be the corresponding weighted sums of a_m and b_m. Define

 I0=integral_R chi(t_plus+tau) exp((k-1)tau) d tau,
 I1=integral_R chi(t_plus+tau) tau exp((k-1)tau) d tau.

Then

 c[Phi]=exp(2t_plus) C_A I0,
 c[KP_s]=exp(2t_plus) C_A I1,
 c[TAU]=exp(2t_plus) C_B I0.                                 (2)

This follows directly from c[x^2 y b(t) cos(2m theta)]=w_m integral exp(2t)b(t)dt. The outer half-line contributes exactly 1/(1-k) to I0 and 1/(1-k)^2 to I1. There are only ten nonzero transition intervals.

The code reads the original read-only NPZ, reconstructs the cutoff by an independent rational de Boor recurrence, and integrates each transition polynomial after mapping its interval to [0,1]. For any real z and nonnegative integer j, it uses

 integral_0^1 u^j exp(zu)du
 =sum_{n=0}^{N-1} z^n/[n!(n+j+1)]+R,
 |R|<=exp(|z|)|z|^N/[N!(N+j+1)].                            (3)

Formula (3) follows from the exponential Taylor remainder at zu and integration. All coefficients and knots are exact rationals; all transcendental evaluation is in 512-bit Arb. The unknown exact normalization repair is enclosed by the independently certified V005 ball. Separate computations with N=80 and N=128 must overlap. The resulting c[KP_s] and c[TAU] balls must overlap the S0 metadata balls, which are used only for comparison, not as inputs to the integration.

The exact endpoint enclosures are in evidence/recomputed.json. They certify c[KP_s]>0 and c[TAU]>0. In particular the shifted-column bordering denominator

 d_s=3/k+k c[KP_s]

is strictly larger than3/k. This positivity is established by the actual integral, rather than by applying the nonnegative-log argument of V034 to a shifted logarithm that is negative on part of the transition interval.

This verifies two scalar entries and the relevant denominator of the finite section. It does not certify its Gram matrix, operator matrix, smallest singular value or any continuum inverse.
