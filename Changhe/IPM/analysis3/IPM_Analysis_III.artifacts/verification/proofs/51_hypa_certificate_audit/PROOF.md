# Audit of the first hypothesis-A and lift-bound certificate

## Object, claim and verdict

The archived snapshot `evidence/hypA_snapshot.py` is the numerics team's first implementation of the axis-rate, lift-bound and anisotropic transport estimates. It is intended to certify the hypotheses (A), (CB) and a positive transport margin for the exact normalized modal density.

The angular identities below are confirmed. The snapshot is not yet a sound complete certificate: it can omit failed endpoint cells, it omits the unweighted part of a cell crossing t=0 in its M_P summary, and its float-to-radius conversion can lose a positive subnormal tail. These are counterexamples to generic certificate steps, not a claim that any printed finite endpoint is already known to exclude the actual mathematical value. The test itself reports enormous two-sided intervals, not a positive transport bound.

No number from this test is accepted here as a certified global constant. Its ten selected cells do not cover the plane. The full verification of a repaired run remains open.

## Confirmed exact identities

Put s=sin(theta), z=cos(theta)^2 and let U_j be the Chebyshev polynomial of the second kind, with U_-1=0. For n>=1,

 cos(2n theta)-(-1)^n=-2(-1)^n z U_(n-1)(s)^2,

 tan(theta)sin(2n theta)-(-1)^(n+1)2n=z g_n(s),
 g_n(s)=2(-1)^n sum_(j=1)^n [U_(j-2)(s)^2+U_(j-1)(s)^2],

 cot(theta)sin(2n theta)=2z U_(n-1)(cos(2theta)).

The first follows from cos(2n theta)=(-1)^n cos(2n arccos s) and 1-cos(2nu)=2sin^2(nu), using sin(nu)=sin(u)U_(n-1)(cos u). The third is sin(2n theta)=sin(2theta)U_(n-1)(cos(2theta)).

For the second, the same substitution gives tan(theta)sin(2n theta)=(-1)^(n+1)s U_(2n-1)(s). The polynomial identity

 [2n-s U_(2n-1)(s)]/(1-s^2)
       =2 sum_(j=1)^n [U_(j-2)(s)^2+U_(j-1)(s)^2]

follows by induction. The n=1 case is2=2. The difference of the two successive left numerators is2[1-s T_(2n+1)(s)]. Writing s=cos u, the identity sin^2(nu)+sin^2((n+1)u)=1-cos u cos((2n+1)u) identifies this with2(1-s^2)[U_(n-1)(s)^2+U_n(s)^2], the successive right difference. This proves the polynomial identity for all n. It also shows the quotient extends at s=+-1. The code independently verifies these polynomial identities for n=1,...,19; the recurrence argument covers all n.

If U_r/r=-sum P_n cos(2n theta) and U_theta/r=sum Q_n sin(2n theta), then

 q=ell-sum P_n cos(2n theta),
 p=3ell-1+3 U_r/r-2tan(theta)U_theta/r+cot(theta)U_theta/r.

The axis formulas and the a1,a0 quotients in the snapshot follow by substitution. The n=1 contribution to a0 is exactly6(Q_1-P_1), so combining it before interval evaluation is legitimate. The Green identity nQ_n=P_n+P_n'/2 is exactly the divergence-free identity in polar coordinates.

## Failed-cell omission

The snapshot constructs the left endpoint index set by

 left=[i for i in sel if isfinite(DD2[i])].

It then maximizes DD2, DP2 and the weighted lift table A0W on that filtered set. If DD2=(1,infinity), the second selected cell is omitted and the printed DD2 maximum is1. A failure is thus converted into a finite reported bound. The right endpoint list has the analogous problem with DCK. The code records this exact counterexample.

The required index sets must instead be determined geometrically from the cell endpoints. Every required entry must be finite, or the corresponding global claim must be marked failed. A separate count of selected cells is insufficient to detect loss inside the selected set.

## A cell crossing the radial weight knot

For M_P, the target is sup |a0|/min(exp(2t),1). On a cell [t0,t1] with t0<0<t1, the implementation includes the maximum of exp(-2t)|a0|, but excludes its unweighted maximum because it includes the latter only when t0>=0.

Take [t0,t1]=[-1,1] and a0(t)=exp(2t). The weighted maximum is1, while the required maximum at t=1 is exp(2)>1. Thus the weighted whole-cell estimate does not bound the positive part's unweighted target. Every cell meeting t>=0 must contribute to the unweighted maximum, or the cells must be split at0. Applying both bounds on a crossing cell is safe, even if it is not sharp.

## Float and radius conversion

The snapshot inserts tail radii as arb(0,float(tail.upper())). For the exact positive value tail=2^-1200, conversion to binary64 is0, and the resulting ball has radius0. It does not enclose the symmetric interval of the claimed radius. The exact code test confirms this failure.

For normal-sized floats, Arb's magnitude constructor introduces an additional upward padding. In particular the initially proposed example1+2^-80 is NOT a counterexample: although it converts to1, the constructor's padding encloses it. This audit does not ignore that padding or claim every plain float conversion produces a wrong ball.

Products such as b*b are not individually upward bounds: for b=1+2^-52, binary64 b*b is strictly less than the exact square. This is also checked exactly. The final magnitude padding may absorb these normal rounding errors; an implementation may either prove a full error budget, including all intermediate operations and underflow, or avoid the issue by using directed conversions and Arb products. The snapshot contains no such full error budget. C_left and C_right are also ordinary floating sums when reported as purported upper bounds.

## Near-resonant inner Green representation

The original input has

 bi=3518437208883275/70368744177664.

For the n=27 mode of the outer-directed inner Green integral,

 lambda=bi+4-2n=75/70368744177664>0.

Thus lambda is approximately1.07e-12. The exponential-polynomial primitive for a degree-six term contains inverse powers up to lambda^-7, whose base-two size is about278.4. A representation that obtains a small finite-interval moment by cancelling such primitive terms is badly conditioned at160-bit precision. The test's inner-cell widths and the failed small identity residual are consistent with this mechanism. This is a conditioning diagnosis, not a proof that every large interval in the test has the same cause.

A stable alternative is to evaluate the short-interval moments by their convergent exponential series with a proved remainder and to preserve the integral form or centered Taylor models when bounding a whole cell. Raising precision can repair cancellation in a point value, but taking independent absolute bounds of huge cancelling exponential-polynomial terms can still be very pessimistic at arbitrarily high precision.

## The S0 log is a failed certificate

The archived contemporaneous S0 log reports non-decaying terms in the J column, then a failed positive-definiteness test for G_X and a Cholesky exception. Consequently it has not produced a certified smallest singular value. This does not by itself prove that the exact mathematical domain Gram is indefinite: a positive-definiteness test can fail through conditioning or an implementation defect. Any subsequent corrected certificate needs a new audit.

## Dependencies and evidence

All code snapshots and logs are read from the numerics team and copied into this topic. The near-resonance value is recomputed from the read-only original NPZ. The accompanying check uses exact rational comparisons, exact symbolic polynomial identities and an actual Arb underflow example. It neither launches the full certificate nor changes another team's files.

Verdict: CONFIRMED for the angular formulas and the stated counterexamples; REFUTED for the snapshot's generic global-coverage and underflow-enclosure steps; OPEN for every proposed actual positive transport bound and S0 singular value.
