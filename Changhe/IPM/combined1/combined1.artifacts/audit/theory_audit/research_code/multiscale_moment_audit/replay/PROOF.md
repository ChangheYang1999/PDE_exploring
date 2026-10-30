# Finite-panel certificates for several radial denominators

## Statement and intended use

Let b be rational with b>-1, let P be a rational polynomial, and let
a_i>=0 and m_i>=1 be rational and integer parameters, respectively.
There are finitely many denominator factors. This note constructs
arbitrarily accurate, rigorous enclosures of

    I = integral_0^1 v^b P(v) product_i (1+a_i v)^(-m_i) dv.       (1)

Every panel endpoint, polynomial coefficient, truncation order and
remainder bound is exact rational data. Only positive real powers at
panel endpoints need outward real arithmetic. The result includes a
signed numerator P; positivity of I is not assumed.

The purpose is to extend the elementary power-moment integrator to
profiles containing several radial scales. In v=(1+r^2)^(-1), the
denominator R^2+r^2 becomes v^(-1)[1+(R^2-1)v]. Thus scales R>=1
give the factors in (1). The fractional common radial exponent gives b.

This statement alone does not certify any candidate. A candidate
application must first derive its exact finite Fourier and rational
radial representation, collect cancellations, establish b>-1 for
each integrated term, and retain every angular and radial cross term.
Integrating a divergent term before its cancellation is invalid.
No certificate is inferred from merely observing small quadrature
differences.

## 1. A finite panel partition

Let a_max=max_i a_i, with a_max=0 for an empty list. If a_max<=1,
use the single panel [0,1]. Otherwise set h=1/a_max and use

    [0,h], [h,2h], [2h,4h], ..., [2^k h,1],

stopping as soon as the next right endpoint would exceed one.
This is a finite exact rational partition. For a panel [l,h], put
c=(l+h)/2 and

    d_i=1+a_i c, z_i(v)=a_i(v-c)/d_i,
    q_i=a_i(h-l)/(2d_i).

Then |z_i(v)|<=q_i<=1/3. On the first panel, a_i h<=1, hence
q_i=a_i h/(2+a_i h)<=1/3. On any later panel h<=2l,

    q_i=a_i(h-l)/(2+a_i(h+l))<=1/3.

The same first-panel argument applies if a_max<=1. These estimates
include a_i=0, for which q_i=0 and the denominator factor is exactly one.

## 2. One denominator and its exact tail bound

For integer m>=1 and |z|<1, the binomial series is

    (1+z)^(-m)=sum_(k>=0) (-1)^k C(m+k-1,k) z^k.

Its first K+1 terms define a polynomial T_K(z). For |z|<=q,
the absolute tail is bounded by

    e_K = C(m+K,K+1) q^(K+1)/(1-r_K),
    r_K = q (m+K+1)/(K+2),                              (2)

whenever r_K<1. Indeed the first omitted term has the numerator
shown, and all subsequent successive-term ratios are at most r_K:
q(m+k)/(k+1) is nonincreasing for m>=1 and k>=K+1.
The geometric-series comparison proves (2).

Since q<=1/3, r_K<1 for all sufficiently large K and e_K tends
to zero. Thus a prescribed rational tolerance can be reached by
increasing K. For q=0 the factor is represented exactly by K=0.

On the panel, define

    A_i(v)=d_i^(-m_i) T_(K_i)(z_i(v)),
    E_i=d_i^(-m_i)e_(K_i),
    B_i=(1+a_i l)^(-m_i).

All are exact rational polynomials or numbers. The true factor f_i
satisfies |f_i-A_i|<=E_i, |f_i|<=B_i, and |A_i|<=B_i+E_i.

## 3. The product error

Let A=product_i A_i. The telescoping identity

    product_i f_i-product_i A_i
      =sum_i (f_i-A_i) product_(j<i) A_j product_(j>i) f_j

implies the exact uniform bound

    |product_i f_i-A|<=E,
    E=sum_i E_i product_(j<i)(B_j+E_j) product_(j>i) B_j.  (3)

For no factors, A=1 and E=0. If P(v)=sum_k p_k v^k, then
on [l,h] subset [0,1],

    |P(v)|<=C_P=sum_k |p_k| h^k.

Consequently the panel contribution differs from

    J=integral_l^h v^b P(v) A(v) dv

by at most

    D=E C_P [h^(b+1)-l^(b+1)]/(b+1).                    (4)

The bound does not require the numerator coefficients to have one
sign. It may be conservative when they cancel strongly. That affects
cost, not validity.

## 4. Outward evaluation and convergence

Expand P A exactly as a rational polynomial sum_k c_k v^k. Then

    J=sum_k c_k [h^(b+k+1)-l^(b+k+1)]/(b+k+1).           (5)

All denominators in (4)-(5) are positive because b>-1 and k>=0.
At l=0 its positive powers are exactly zero. Evaluate (4)-(5) by
outward ball arithmetic. If J belongs to [J_lo,J_hi] and
0<=D<=D_hi, the panel integral belongs to
[J_lo-D_hi,J_hi+D_hi]. Summing these panel intervals encloses (1).

For this fixed finite partition, taking each K_i to infinity makes
E_i, E and D tend to zero. The polynomial sum in (5) is finite at
every stage. Increasing the arithmetic precision makes its evaluation
radius arbitrarily small. Thus the procedure can achieve any positive
absolute error tolerance, with no claim of uniform efficiency in
the degree, coefficients or denominator multiplicities.

## 5. Independent elementary calibration cases

The accompanying exact JSON defines cases whose integrals also have
elementary formulas. For a>0 and m>1,

    integral_0^1 (1+a v)^(-m) dv
       = [1-(1+a)^(1-m)]/[a(m-1)].

For m=1 it is log(1+a)/a. Substituting v=t^2 gives

    integral_0^1 v^(-1/2)/(1+a v) dv
       =2 atan(sqrt(a))/sqrt(a),
    integral_0^1 v^(1/2)/(1+a v) dv
       =2[1-atan(sqrt(a))/sqrt(a)]/a.

For distinct positive a and d, partial fractions give

    integral_0^1 1/[(1+a v)(1+d v)] dv
       =[log(1+d)-log(1+a)]/(d-a),
    integral_0^1 v^(-1/2)/[(1+a v)(1+d v)] dv
       =2[sqrt(d)atan(sqrt(d))-sqrt(a)atan(sqrt(a))]/(d-a).

Polynomial-only cases follow directly from (5) with no denominators.
These checks exercise the endpoint, several scales, high multiplicity,
signed coefficients and the empty product. Agreement is a calibration
of the implementation, not an independent review of this new theorem
or a certificate for a research candidate.

Dependencies are the binomial theorem on its open convergence disk,
the geometric-series tail bound, rational polynomial arithmetic,
and outward positive real powers. No adaptive quadrature library,
special multivariable function or external computation is required.
