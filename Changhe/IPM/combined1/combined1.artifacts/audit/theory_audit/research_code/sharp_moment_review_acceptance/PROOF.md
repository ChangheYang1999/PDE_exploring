# Acceptance of the independent sharp-moment review

Status: CONFIRMED. T4-372 is AUDITED through the T1/T3 theory worker R1-039. The full
review, independent checker, output and original proof are frozen in
source/. No foreign code was executed in accepting this review.

## Exact statement and complete argument

Let d>0, theta=d/(d+2), nu=2(d+2)/(d+4), and
J=integral_0^(2pi)|sin phi|^nu dphi. Set
C0=(d+4)J/[4(d+2)] and C=(d+2)C0^(1-theta/2)/d.
If h is real measurable on R2, ||h||2<=beta and
|h(X)|<=H|X|^(-d-3) almost everywhere, for finite beta,H>=0,
then its first moment converges absolutely and

    |integral y h|<=C beta^theta H^(1-theta).

The same bound holds for the norm of its vector first moment. The
constant is sharp, also when scalar h is required to be S1. It is
not asserted optimal for the smaller weighted C1 class.

For completeness, Cauchy-Schwarz inside radius R and direct polar
integration outside give the absolute bound
sqrt(pi) beta R^2/2+4H R^(-d)/d. If either budget vanishes the result
is trivial. Otherwise set

    h_lambda=sign(y) min(lambda |y|,H r^(-d-3)),
    lambda=[beta^2/(C0 H^(4/(d+4)))]^(1/nu).

At each angle with b=|sin phi|>0 the switching radius is
R_phi=[H/(lambda b)]^(1/(d+4)). Direct integration below and above
that radius gives

    ||h_lambda||2^2=C0 H^(4/(d+4)) lambda^nu,
    integral y h_lambda=(d+2)C0 H^(4/(d+4))lambda^(d/(d+4))/d.

The chosen lambda sets the norm to beta. Eliminating lambda in the
second identity gives C beta^theta H^(1-theta). For each point the
concave function t -> y t-t^2/(2lambda), restricted to the amplitude
interval, has maximum at h_lambda. Integrating this pointwise
inequality bounds integral y h by integral y h_lambda, since the
norm of h is no larger. Apply the same argument to -h. Equality
for h_lambda proves sharpness and its formula gives S1 parity.
Rotation gives the vector statement. Finally
J=2sqrt(pi)Gamma((nu+1)/2)/Gamma((nu+2)/2) by the substitution
u0=sin(phi)^2 on a quadrant.

A weighted C1 bound H_q with q=-d-3 implies the amplitude hypothesis
with H=H_q. It does not make this sharpness statement valid in that
smaller class. Indeed h_lambda equals lambda y in increasingly thin
strips near the horizontal axis at arbitrarily large radii, where
its weighted gradient grows without bound. The optimal exponent in
the weighted C1 class is a separate result in T4-371.

## Independent review and quantitative comparison

R1-039 checks the argument above in ten steps. The26 independent
checks all pass: exact symbolic exponents and identities, directed
60-digit interval constants, and separately labeled floating
quadrature diagnostics. The pointwise concavity proof, rather than
the801 sampled rational values, proves the variational inequality.
Neither floating quadrature nor its agreement is used for acceptance.
At the campaign exponent the interval for C lies strictly between
9.155134741153639269902 and9.155134741153639269903. The ratio to the
split constant lies between0.971488103354059961363 and
0.971488103354059961364. These agree with the independent Arb record.

The review's closing statement about unchanged endpoint reach is
accepted only in the precise sense established by T4-379: the cap
obtained by discarding moment-dependent error terms is unchanged.
A moment estimate may improve an actual subthreshold CI lower bound;
it cannot bypass that moment-independent cap. No upper H_q budget,
PDE inverse or existence statement follows from the sharp inequality.
