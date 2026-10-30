# Certified radial moments for finitely many scales

## Statement and exact input class

Let alpha,beta be rational numbers greater than -1. Let nu_1,...,nu_m be arbitrary rational numbers and let z_i be rational with 0<=z_i<1. Consider the finite positive moment

    I=integral_0^1 t^alpha (1-t)^beta
                 product_i (1-z_i t)^(-nu_i) dt.        (1)

There is a finite, convergent enclosure algorithm using rational polynomial arithmetic, positive real powers and an explicit analytic error. In particular no sampling quadrature, floating cancellation test or unproved tail cutoff is needed.

The algorithm below gives a rational polynomial approximation on a geometric partition with a rigorously bounded remainder. For any prescribed positive error it terminates as the polynomial degree increases. A finite signed linear combination of moments is enclosed by interval summation, provided every individual moment meets the stated endpoint hypotheses. Exact endpoint cancellations must be performed before applying this theorem if the uncombined terms are not integrable.

This is an integration theorem, not a proof that a candidate belongs to a required space. Its use in a candidate certificate requires an exact derivation of the integrand and verification of all endpoint exponents.

## Geometric partition

Choose an integer J>=2 such that 2^(-J)<=min_i(1-z_i); use J=2 if the product is empty. Partition [0,1] at

    0, 1/2, 3/4, ..., 1-2^(-J), 1.

Write each interval as t=l+h x, 0<=x<=1. Every nonfinal interval has l=1-2^(-k), h=2^(-k-1) for some k=0,...,J-1. The final interval has l=1-2^(-J), h=2^(-J). Separate the endpoint factors as follows.

On the first interval, t^alpha=h^alpha x^alpha; on every other interval, t^alpha=l^alpha(1+(h/l)x)^alpha. On the final interval, (1-t)^beta=h^beta(1-x)^beta; on every other interval, it equals (1-l)^beta(1-hx/(1-l))^beta. Each denominator factor is

    (1-z_i t)^(-nu_i)
      =(1-z_i l)^(-nu_i)(1-q_i x)^(-nu_i),
    q_i=z_i h/(1-z_i l).

Every analytic linear factor has a parameter of absolute value at most 1/2. For t^alpha away from the first interval, h/l<=1/2. For (1-t)^beta before the last interval, h/(1-l)=1/2. For each q_i on a nonfinal interval,

    q_i<=h/(1-l)=1/2.

On the final interval, h<=1-z_i implies z_i h<=1-z_i, so q_i<=1/2 there too.

Consequently each interval contribution is

    C integral_0^1 x^a (1-x)^b G(x) dx,                 (2)
    G(x)=product_j (1+q_j x)^(e_j), |q_j|<=1/2,

where C>0 is an explicit finite product of rational positive bases to rational powers. Here (a,b)=(alpha,0) on the first interval, (0,beta) on the final interval, and (0,0) otherwise. The exponents e_j and parameters q_j are rational. The Jacobian h is included in C.

## Polynomial coefficients and remainder

Fix rho=3/2. Each binomial factor is analytic in |x|<2. Its branch is the one equal to 1 at x=0. Its exact Taylor coefficients are binom(e_j,k)q_j^k. Form the product through degree N, discarding only degrees greater than N after each polynomial multiplication. This computes the exact first N+1 coefficients g_0,...,g_N of G.

For real e and |w|<1,

    |(1+w)^e|<=sum_k |binom(e,k)||w|^k
                 <=(1-|w|)^(-|e|).

The second inequality follows factor by factor from |e-r|<=|e|+r. Thus on |x|=rho,

    |G(x)|<=M:=product_j(1-rho|q_j|)^(-|e_j|).

All bases in M are at least1/4. Cauchy's coefficient estimate gives |g_k|<=M rho^(-k). For 0<=x<=1, summing the geometric tail yields

    |G(x)-sum_(k=0)^N g_k x^k|
       <= M rho^(-N-1)/(1-rho^-1)=:E_N.                (3)

Multiplying by the nonnegative integrable endpoint weight in (2) proves the enclosure

    |I_interval-C sum_(k=0)^N g_k mu_k|
       <= C E_N mu_0,
    mu_k=integral_0^1 x^(a+k)(1-x)^b dx.               (4)

These moments are exact rational numbers. If b=0, mu_k=1/(a+k+1). On the last interval a=0, mu_0=1/(b+1) and

    mu_k=mu_(k-1) k/(b+k+1), k>=1.

The recurrence follows by integration by parts in the beta integral. Therefore (4) needs no gamma-function evaluation. Sum the finitely many interval enclosures. For fixed input J,C,M, the error tends geometrically to zero as N increases. Outward evaluation of the finite positive powers and subsequent arithmetic adds only controlled interval width. Increasing arithmetic precision and N gives arbitrarily narrow enclosures, proving termination for each fixed input and target error.

## Connection with whole-plane radial integrals

For R_i>=1 with R_i^2 rational, and alpha,gamma,nu_i rational with the right-hand endpoint conditions satisfied, substitution t=r^2/(1+r^2) gives

    integral_0^infinity r^(2alpha+1)(1+r^2)^(-gamma)
                        product_i(R_i^2+r^2)^(-nu_i) dr
      = (1/2) product_i R_i^(-2nu_i)
          I(alpha, gamma+sum_i nu_i-alpha-2;
                     z_i=1-R_i^-2, nu_i).              (5)

The factor1/2 is the polar radial Jacobian. A separate angular integral must still be included. Formula (5) follows from r^2=t/(1-t) and r dr=dt/[2(1-t)^2]. A polynomial numerator can be expanded into a finite linear combination after all required cancellations have been performed exactly.

Positive radii with rational squares smaller than1 cause no obstruction. First rescale r=L v with L=min(1,R_1,...,R_m)>0. Include the original factor1+r^2 as the scale1 factor. Every transformed radius, including1/L, is at least1. Constants from this rescaling are explicit positive rational powers. The moment theorem allows either sign of nu_i, so a growing factor can be represented as a negative exponent.

Cartesian derivatives of the scaled generators remain finite sums of polynomial numerators times rational powers of1+r^2 and integer powers ofR_i^2+r^2. Squared norms and finite products introduce only finitely many scales. Thus (5) supplies a possible certificate once a separate exact algebra step has produced integrable terms. It does not justify expanding a divergent term before cancelling it, and it does not itself validate the new candidate's residual-sector constraints.

## Verification status and dependencies

The proof uses the binomial series, elementary complex Cauchy estimates, and the explicitly derived rational beta recurrence. A small implementation checks exact manufactured moments, including a pole close to the endpoint. Those finite tests supplement the proof; they do not prove general correctness or certify any candidate norm. This is an original T4 result and remains CLAIMED until independently reviewed by T1 or T2.
