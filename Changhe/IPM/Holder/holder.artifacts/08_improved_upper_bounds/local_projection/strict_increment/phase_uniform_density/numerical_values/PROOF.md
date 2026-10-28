# Directed evaluation of orientation-uniform reflection moments

## Statement

Use the scalar homogeneous Holder spaces, positive local measure and disks of ../PROOF.md. Its orientation-uniform reflection theorem must be independently accepted before the numerical values in this folder are admitted. Use exactly the rational center c and a=1-c of the accepted optimal-disk numerical certificate V226. The outer disk scale s is the selected rational radius in each row. All rows satisfy 2as<1. The original translation-cost base is the exact rational upper endpoint named base_upper in V226, before any reflection saving.

For each row subtract the first eight positive reflection moments from that base. For an unperturbed row use I_n of the parent proof. For a cutoff row subtract the constant-density integral in equation (2) of the parent proof. For a uniform remainder coefficient on 0<alpha<=epsilon=1/100, evaluate each positive binomial coefficient divided by alpha at epsilon. This bounds the saving divided by alpha from below throughout the interval, since every factor k-alpha decreases with alpha. No previous saving is subtracted twice, and no omitted positive moment is used without an enclosure.

## Positive series with an explicit tail

Because a+c=1,

    c^2+2cx+a^2 = 1-2c(a-x).

Put q=2ca<1. For x in [0,a], the geometric series gives

    I_n = sum_(k>=0) (2c)^k integral_0^a x^(2n)(a-x)^k sqrt(a^2-x^2) dx.

Every term is nonnegative. The ratio of successive terms is at most q, directly from the positive integrands. After terms k=0,...,N-1, the omitted tail is at most the first omitted term divided by 1-q. Only the finite partial sum is used as a lower bound in an operator saving.

Let j_m=integral_0^1 t^m sqrt(1-t^2)dt. Then

    j_0=pi/4, j_1=1/3, j_(m+2)=(m+1)j_m/(m+4).

The kth term therefore equals

    (2c)^k a^(2n+k+2) sum_(l=0)^k (-1)^l binom(k,l) j_(2n+l).

Each such value has the form A*pi+B with exact rational A and B. The finite expression may have cancellations, so the program checks strict positivity with directed ball arithmetic; positivity itself is established by the integral. Rational coefficients and pi are evaluated at 384 and 768 bits with different summation orders. The two answers must give the same outward ten-place endpoint.

## Independent closed-form check

Put A=c^2+a^2, B=2c, Delta=c^2-a^2>0, and J_m=a^(m+2)j_m. For all integers m>=0 define

    F_m=integral_0^a x^m sqrt(a^2-x^2)/(A+Bx) dx.

The substitution x=a sin(theta), followed by tan(theta/2), gives

    F_0=[A*pi/2-Ba-2Delta*atan((c-a)/(c+a))]/B^2.

Polynomial division then gives the exact recurrence

    F_m=(J_(m-1)-A F_(m-1))/B,  m>=1.

This independently evaluates I_n=F_(2n), without the geometric series or its polynomial expansion. Its 768-bit ball must be enclosed in the positive-series lower/upper interval. It is a diagnostic corroboration of the finite lower sum, not a replacement for its analytic tail proof.

## Normalization and rounding

For comparison with V226, define

    Btilde_(2n+1)=2^(2n+1) I_n/[pi*binom(2n,n)].

The saving is exactly A_n(alpha)s^(2n)Btilde_(2n+1), where A_n is defined in the accepted even-moment theorem. In a cutoff row subtract kappa*a^(2n+2)/(2n+2) from Btilde, with kappa=rho^2/(1-rho)^2. This identity follows from the exact integral j_(2n)=pi*binom(2n,n)/[4^(n+1)(n+1)]. The retained moments are positive because the parent retained density is positive; the program checks their directed lower endpoints.

The computation records every exact lower sum, upper remainder, independent closed-form ball, and final saving. Upper operator decimals are rounded upward using exact rational arithmetic. All analytic and numerical dependencies are hashed. This proof is written before execution; no new numerical claim is accepted without the completed accepted.json.
