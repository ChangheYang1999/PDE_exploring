# Repaired N3 calibration runs: independent finite checks and their limits

## Claims and exact inputs

Let delta=1824676646553933/4076476460239181 and
J(b,i,a)=integral_0^1 v^b/(1+a v)^i dv for a>0, integer i>=0, b>-1.
The repaired test A has scales 624,99,2499; base exponents -37/100,0,
delta/2-1; i=0,...,14; and b=b0+m, m=0,7,...,35. It has 810 cases.
The additional three cases have a=624, i=23, b=-37/100+m with
m=600,1800,2400. This proof concerns all 813 exact instances, the
repaired published output, the six-generator quadrature fixture and
the two printed d2 Laplacian norms. It asserts no actual-016 norm.

The six-generator exact input and its already independently accepted
norms are ../n3_synthetic_field_audit/data/synthetic.json and its
verification/result.json (N4-305). Define G0=||F||_2, rF=||r F||_2
on the full plane for that input. For d2 define
N_a=||(1+r^2)^((2-a)/2) Delta F_d2||_2. The exact d2 input and accepted
all-mode results are ../weighted_laplacian_audit/PROOF.md and
verification/d2.json (N4-099). Those complete derivations are
prerequisites; this check does not reconstruct their large fields.

## Moment identity and finite validation

The integrand of J is absolutely integrable since b>-1 and the
positive denominator is bounded away from zero. Write u=1-v and
z=a/(1+a), so 0<z<1. Then

 J=(1+a)^(-i) integral_0^1 (1-u)^b (1-z u)^(-i) du
  =(1+a)^(-i)/(b+1) * 2F1(i,1;b+2;z).                 (1)

Euler's integral gives the last equality; its endpoint exponents 0,b
are both greater than -1. Equivalently, expand (1-z u)^(-i) into
its nonnegative binomial series and integrate each term. Monotone
convergence justifies the exchange for i>0, and i=0 is immediate.
The beta integral gives (1)_k/(b+2)_k, yielding the same series.
The already proved own pole-moment recurrence in
../rational_pole_moments/PROOF.md uses a different argument -a for its
base moment and rational recurrence for higher i. Evaluating both
paths with outward Arb arithmetic and checking overlap validates the
finite table values under these integral hypotheses. The checker
retains both containing balls and relative accuracy for every case.
It uses no floating quadrature to evaluate J.

The original divergent base delta-3/2 remains a historical error.
Successful checks at the repaired base delta/2-1 do not retroactively
certify that earlier analytic-continuation calculation.

## What the repaired quadrature record establishes

The exact repaired 58-panel partition is already proved and source
checked in ../n3_scaled_calibration_repairs/PROOF.md. In the six-generator
fixture m is at most 3. The density has angular frequency at most 7
and the stream function at most 8. In polar form the advective term
is (psi_r rho_theta-psi_theta rho_r)/r, so its frequency is at most
15. Thus F squared has frequency at most 30. The mathematical 36-node full-circle
trapezoid rule integrates that trigonometric polynomial exactly:
for integer k with 0<|k|<=30, the finite geometric sum
sum_(j=0)^35 exp(2 pi i k j/36) is zero. This is an identity before
floating evaluation. The actual code approximates pi, trigonometric
values and fractional powers, and its 20-point Gaussian nodes and
weights are rounded decimal rationals obtained from binary64 values.
Only the radial rational-polynomial factors are evaluated exactly.
The physical points and complete residual values are not all rational.

The published quadrature numbers are approximations Q, not rigorous
norm intervals. Rebind the identical fixture and compare their recorded
decimal values with the independently certified G0 and rF intervals.
The observed relative discrepancies |Q-N|/N are evaluated outward.
Their smallness is an observed finite comparison. It supplies no
Gaussian truncation bound, rounding bound, uniform radius bound or
certificate for any other candidate. The certified norm intervals
continue to come from the accepted analytic integration route.

## The d2 printed-reference comparison

The repaired N3 cells test prints intervals for N_1 and N_0 and compares
them to shortened decimal reference strings at absolute tolerance 10^-12.
Compare its full saved intervals directly with the accepted N4-099
intervals. Such agreement is the meaningful reproduced norm check.
The shortened reference 1161.65961265051 differs from the actual N_0
by about 1.7752*10^-12, so its Boolean tolerance test is expected to be
false. This does not refute either computed norm. Recompute both
Boolean comparisons and retain the discrepancy interval. Any claim
that both printed Boolean tests passed is false for this saved run.

## Verification and scope

Freeze the actual logs, JSON and source bytes before comparison.
Rehash the accepted source repairs, synthetic integral certificate and
d2 proof/results. The repaired test-A log supplies its actual reported
outcome; the own 813-case calculation independently verifies all its
mathematical moment instances. Current publisher source is read as
text only. Common decimal enclosures, rather than unverified hundreds
of endpoint digits, state the norm comparisons. No server, cluster,
foreign-directory execution or spatial quadrature is used here.
