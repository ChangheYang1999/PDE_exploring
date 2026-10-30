# Independent audit of finite-panel multiscale integration

Status: theoretical audit CONFIRMED; arithmetic calibration is recorded separately in verification. This certifies the stated integration method and its listed tests, not a candidate norm.

## Exact statement

Let b be rational and greater than -1, let P be a rational polynomial, and let there be finitely many rational a_i >= 0 and integer m_i >= 1. The integral

    I = integral_0^1 v^b P(v) product_i (1+a_i v)^(-m_i) dv

has rigorous enclosures by the finite-panel method in source/PROOF.md. Given any positive absolute tolerance, the abstract method can achieve it by increasing truncation orders and arithmetic precision. The implementation has a finite work cap, so this assertion does not promise termination of that particular implementation for every tolerance. Its returned intervals are enclosures regardless of width.

## Complete argument

Set a_max=max a_i, with zero for the empty list. For a_max<=1 use [0,1]. Otherwise start with [0,1/a_max] and double the positive right endpoint, truncating the last endpoint to 1. This is a finite rational partition. Write each panel as [l,h], let c=(l+h)/2 and d_i=1+a_i c. The relative displacement z_i=a_i(v-c)/d_i has absolute value at most q_i=a_i(h-l)/(2+a_i(h+l)). On the first panel a_i h<=1 gives q_i<=1/3. On later panels h<=2l, and 3a_i(h-l)<=2+a_i(h+l) follows from a_i(h-2l)<=1. Thus every q_i<=1/3.

The binomial series for (1+z)^(-m) has coefficient (-1)^k binom(m+k-1,k). After order K the first omitted absolute term at radius q is binom(m+K,K+1)q^(K+1). The ratio of its successor to it is q(m+K+1)/(K+2). Subsequent ratios decrease for m>=1. Once this ratio r is less than 1, dividing the first omitted term by 1-r bounds the entire absolute tail. It tends to zero as K increases. Multiplying the polynomial and error by d_i^(-m_i) gives a polynomial A_i and error E_i for the true factor f_i. The bound B_i=(1+a_i l)^(-m_i) bounds |f_i|, and B_i+E_i bounds |A_i|.

The exact telescoping product identity gives

    |product f_i-product A_i|
      <= sum_i E_i product_(j<i)(B_j+E_j) product_(j>i)B_j = E.

On the panel, |P(v)|<=C_P=sum_k |p_k|h^k. Since v^b is nonnegative and integrable, the integral error is at most

    E C_P (h^(b+1)-l^(b+1))/(b+1).

Expand P product A_i exactly as sum c_k v^k. Its integral is the finite sum c_k(h^(b+k+1)-l^(b+k+1))/(b+k+1). All powers have positive exponents. Outward ball evaluation of each sum and nonnegative remainder followed by outward endpoints encloses the true integral. Summing panel intervals encloses I. With the finite partition fixed, the remainders tend to zero; for every fixed finite polynomial the ball evaluation radius tends to zero as precision increases. Taking these two limits in that order proves arbitrary accuracy, without a uniform efficiency claim.

## Implementation audit

The frozen moments.py follows these formulas. In power_integral the endpoint powers are initialized at b+1 and multiplied by the corresponding endpoint after every coefficient, including zero coefficients. Therefore the exponent and denominator indices stay aligned. tail_order updates the first omitted term by the current successor ratio before incrementing K. Zero denominators and the empty factor list are handled exactly.

The raw API converts m with int(m), so callers must validate that their supplied multiplicities are integers before calling it. The theorem does not cover fractional multiplicities rounded by that conversion. The tolerance parameter controls factor truncations; it is not a guarantee that the returned total width equals that tolerance. A candidate consumer must check the returned final interval and derive its integrand, endpoint integrability and every cross term independently.

## Independent calibration argument

For b=0 and linear denominator factors, ordinary rational partial fractions provide a second exact route. Polynomial terms integrate rationally. A term C/(1+a v)^k integrates as C log(1+a)/a for k=1 and C[1-(1+a)^(1-k)]/[a(k-1)] for k>1. The independent checker obtains the partial fractions over the rational field, reconstructs their sum exactly and evaluates these explicit primitives with outward balls. This checks signed numerators, several scales, repeated factors, improper fractions and a zero scale without reusing the binomial expansion.

The original eight elementary calibration cases are also replayed on frozen files. Interval overlap is a calibration check, not a substitute for the proof above. No floating quadrature result enters the certificate.

Dependencies: binomial series, geometric series, exact rational polynomial arithmetic and outward evaluation of positive powers and logarithms. Canonical PDE normalization, function spaces and residual expansions are outside the scope of this integration primitive.
