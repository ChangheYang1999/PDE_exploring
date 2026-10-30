# Audit of numerical report v11

## Statement and scope

This is an audit of the immutable numerical report numerics_v11, published
at2026-10-29T10:45:46Z. It checks transcription and the logical use of
previously accepted certificates. It does not independently rerun every
FLOAT experiment in that report. Exact source hashes and capture times
are stored with the proof.

The report contains duplicated status paragraphs in its header, calls020
OPEN after its independent weak certificate was accepted, omits021's
accepted weak exclusion from its status update, and writes the certified016
floor as greater than0.0014704. The comparison code checks these literal
statements against the frozen report and accepted result records. The
other three displayed floor roundings are checked separately. No candidate
verdict is reversed by correcting a transcription.

## Strict lower bounds and rounding

Let S be the set of stationary corrections satisfying one fixed accepted
certificate's hypotheses, and let d=inf{||h||_2:h in S}, with inf(empty)=+infinity.
An accepted weak certificate establishes d>l, for its stated exact rational
l. The distance root r obtained from its stable quadratic formula is enclosed
in an explicit interval, with l<r. A displayed strict lower bound d>b is
licensed by this certificate if b<=l; alternatively one may use a separately
justified b<r. If the printed b lies above the upper endpoint for r, this
certificate cannot supply it. This observation does not prove d<=b. It
refutes the description of b as this certificate's confirmed floor.

Every saved ball used here has the form[c +/- e], with decimal rational
c,e and e>=0. It therefore supplies exact rational bounds c-e and c+e.
The checker converts these strings to rational numbers without binary
floating arithmetic, compares each printed floor with its accepted l and
root endpoints, and supplies a safe downward-rounded decimal.

For016 the accepted exact floor is367590231030927/250000000000000000,
and the root is between0.00147036092412370996622 and0.00147036092412370996623.
Thus0.0014704 is above the root, whereas0.0014703 is below the accepted floor.
For017 use the separate19/1800 acceptance, not its earlier23/2400 result.
All these statements retain the common fixed-c canonical real S1 L2
hypotheses of their own accepted proofs. Scalar and graded ball exclusions
use their established L2 embeddings. This audit supplies no dyadic or
localized exclusion.

## Objective-value fractions do not establish inactivity

For M>0 define B_M(x)=M+x^2 and P(x)=25(x-1)^2 on the real line. Equivalently
P=w I^2 with w=10^12 and I(x)=(x-1)/200000. The unique minimizer of B_M is0.
Since(B_M+P)'=52x-50 and(B_M+P)''=52>0, the unique minimizer of B_M+P is25/26.
At this point P=25/676, so P/(B_M+P) tends to0 as M tends to infinity.
The minimizer change remains25/26. Thus an arbitrarily small relative
objective contribution does not imply a small effect on the optimizer.
The same counterexample also has P(0)=25 and P(0)/B_M(0)=25/M tending to0.
This is an exact logical counterexample, not a model of the campaign's
unmeasured Jacobian. The causal effect of021's fourteen rows remains OPEN.
The T4-390 independent argument gives a second scalar quadratic example
with variable derivatives; its complete proof is frozen alongside this one.

## Status provenance and report boundaries

The accepted020 weak result is N4-299, through T4's complete polar replay.
The accepted021 weak result is N4-320, through T4-392. They predate v11.
Their exact IDs, times, hypotheses and positive distance floors are retained
in their original standalone proofs and source-bound certificates. Binding
those accepted records is a transcription check, not a fresh proof of the
whole-plane weak theorem.

The numerical values for022 and023 in v11 are explicitly FLOAT. Their
independent acceptance must be stated separately. A partial norm calculation
or source audit is not a completed norm certificate. N4's own016 exact
reconstruction is a distinct implementation from N3's production code;
its components remain OPEN until the numerical comparisons finish. No
exclusive claim about all possible methods for exact norms is justified.
The theorem followed by a run and the latest theory report read by its
publisher should be distinguished explicitly.

## Verification dependencies

The checker binds the full v11 bytes, this proof, the independent T4-390
proof and the original accepted floor records. It verifies exact rational
comparisons and a scalar quadratic fixture. No foreign code, remote
computation or numerical optimization is executed. The result records
which source statements are confirmed, contradicted, or still open.
