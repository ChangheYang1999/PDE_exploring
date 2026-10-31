# Exact identities behind the elementary-function audit

## Statement and notation

Let h and l be finite binary64 numbers, interpreted as exact real numbers, and let x=h+l. For every integer n,

    exp(x) = 2^n exp(x-n log(2)).

For every integer k, the pair (sin(x),cos(x)) is obtained from (sin(r),cos(r)), where r=x-k*pi/2, by the quadrant permutation and signs determined by k modulo 4. These identities do not require n or k to be the nearest integer. Nearest-integer reduction gives |r|<=pi/4 for the trigonometric functions and |x-n log(2)|<=log(2)/2 for the exponential, provided the rounding decision is made from the exact quotient.

Let P_N(t)=sum_{j=0}^N t^j/j!. For real t,

    |exp(t)-P_N(t)| <= exp(|t|) |t|^(N+1)/(N+1)!.

Let S_15(t)=sum_{j=0}^7 (-1)^j t^(2j+1)/(2j+1)! and C_14(t)=sum_{j=0}^7 (-1)^j t^(2j)/(2j)!. If |t|<=1, then

    |sin(t)-S_15(t)| <= |t|^17/17!,
    |cos(t)-C_14(t)| <= |t|^16/16!.

These are exact-real statements. They do not certify any floating-point implementation or an observed error bound.

## Proof

The exponential addition law gives exp(x)=exp(n log(2))*exp(x-n log(2)); the first factor equals 2^n. The sine and cosine addition formulas at integer multiples of pi/2 give the quadrant rule. The nearest-integer inequalities follow directly from |q-round(q)|<=1/2.

Taylor's theorem with Lagrange remainder bounds the exponential remainder by exp(|t|)|t|^(N+1)/(N+1)!. In the sine and cosine series, successive term magnitudes decrease for |t|<=1. The alternating-series remainder has magnitude at most the first omitted term, which gives the two stated bounds. The double-angle identities sin(2t)=2sin(t)cos(t), cos(2t)=1-2sin(t)^2 and repeated squaring of exp(t) are exact consequences of the same addition laws.

## Audit interpretation and dependencies

The implementation under review reduces an approximate pair for log(2) or pi/2, evaluates finite Taylor polynomials in pair arithmetic, and reverses the reductions. The reference audit imports each stored input h and l exactly into 90-digit mpmath, computes the reference at h+l, and compares that value with the exact real sum of the two returned binary64 words. This separates pair accuracy from the accuracy of their rounded binary64 sum. It also reports subnormal outputs separately: near the smallest positive binary64 number, a uniform relative pair bound is impossible.

Dependencies are the real exponential/trigonometric addition laws, Taylor's theorem and the alternating-series theorem. No Euler field, pressure discretization, or actual table argument range is certified by this analytic argument. Each sampled implementation observation is recorded separately in verification record. Formalization is not attempted because Lean/Lake builds are prohibited.
