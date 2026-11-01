# Finite cancellation in the polynomial Poisson inverse

Status: exact identities and a finite interval audit. No all-order cancellation estimate is asserted.

## Exact claim

At a nonresonant order n of the canonical logarithmic recursion, let p=1-n delta and P=p+1. For an odd density frequency m, write its polynomial amplitude as a(t)=sum_h a_h t^h and the amplitude at m+2 as b(t)=sum_h b_h t^h. Put l=m+1, s=m+3-n delta=P+l, and v=l-P. Assume s and v are nonzero. The constant coefficient of the stream at frequency l is

\[
 G_{n,l,0}=U+D,
\quad U=-\frac1{2s}\sum_{h\ge0}\frac{(-1)^h h!a_h}{s^h},
\quad D=\frac1{2v}\sum_{h\ge0}\frac{h!b_h}{v^h}.
 \tag{1}
\]

The sums are finite. Define

\[
 B=\frac1{2|s|}\sum_h\frac{h!|a_h|}{|s|^h},
 \qquad H=\frac1{2|s|}\sum_h h!|a_h|,
 \qquad A=\sum_h|a_h|.
 \tag{2}
\]

Then |U|<=B. The ratios B/|U| and H/|U| measure different effects: the first is the full loss from discarding cancellation in the upward inverse, while the second omits the additional powers of |s|^(-1). No inequality between H and |U| is asserted in general. Comparing U with the full stream coefficient must account for D.

The particular audit uses delta=2/3 and f_1=sin(theta), with the canonical zero resonant stream constants. It evaluates (1)-(2) at the nearest nonresonant density modes and also sums B over every density frequency at the selected order.

## Proof

The canceled upward channel is -(1/2)(D_t+s)^(-1)a. Since a is a polynomial, its exact inverse is the finite Neumann sum -(1/(2s))sum_h(-D_t/s)^h a. Evaluating at t=0 gives U because D_t^h a(0)=h!a_h.

The downward channel from frequency m+2 is (1/2)(l-P-D_t)^(-1)b. Its finite inverse has only positive powers of D_t/v, and gives D. These are the only density frequencies contributing to the stream mode l. Summing them proves (1). The triangle inequality proves |U|<=B.

For the interval certificate, decode the exact dyadic centers and radii already retained in topic64. All factorials and rational shifts are exact; sum the expressions with outward rounding at 640 bits. The separately stored stream ball must overlap U+D. Every reported logarithm or ratio requires a strictly positive denominator enclosure. The checkpoint and selected-input hashes identify the finite data used.

## Scope

The coefficient enclosures depend on the audited numerical recurrence. This computation independently checks the algebra of the Poisson inversion and quantifies cancellation on those enclosures. It does not prove that the same cancellation persists as n grows, or that nonlinear products are the sole source of future growth. The general-input Poisson obstruction from topic71 remains valid.
