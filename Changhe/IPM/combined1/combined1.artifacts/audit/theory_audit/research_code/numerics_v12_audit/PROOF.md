# Audit of the v12 numerical summary and its FLOAT comparisons

## Statement and scope

This audit concerns the frozen numerical publication numerics_v12, SHA256
20763c86645a954697bb617b57efc7d81f7afbbcd3aa173d5ee4d00d352bae9c,
and the copy of NUMERICS_FINAL frozen alongside it. It proves internal
contradictions between several universal summaries and their printed tables.
A printed finite decimal is treated as an exact rational for this comparison.
This does not certify the FLOAT values as enclosures of the actual profiles.
The contradictions below are large enough that ordinary last-digit display
rounding cannot explain them. No existence claim or candidate exclusion
changes as a result of these reporting repairs.

## Complete argument for the FLOAT comparison repairs

For positive printed parent and child values p and q, define R=q/p. A fall
by a factor between a and b requires 1/b <= R <= 1/a. An increase by
25 to 40 percent requires 1.25 <= R <= 1.40. Being within25percent requires
0.75 <= R <= 1.25. These are elementary exact rational inequalities.
Every table entry used below is copied by parsing the frozen document,
not by substituting a new diagnostic or a different candidate.

1. In section2, the five candidate025 values at K=600, relative to016,
are 2.04e-4/8.18e-6, 5.60e-5/2.17e-4, 6.63e-6/1.94e-4,
3.62e-5/8.70e-5 and3.91e-5/7.85e-5, in modes19,23,25,29,31.
The first exceeds24.9, so it increases. The last two decrease by less
than3. Thus the header and section6 assertion that these probes decrease
by factors3to30 is refuted as a summary of all five probes. Exactly four
of the five decrease; their reduction factors lie between2and30. It is
accurate to say approximately2to29, with the mode19 exception explicitly
reported as an approximately25-fold increase.

2. In the same section the ratios at K>=1200 are mixed. At(25,1200),
4.05e-4/1.16e-4 > 3.49, outside[1.25,1.40]. At(31,1200),
4.22e-5/1.27e-4 < 0.333, and at(29,1200),5.78e-5/9.65e-5 < 0.60,
so these decrease. Even the largest reported probe(19,1800) changes
from9.02e-4to1.27e-3, a ratio above1.4079, approximately41percent.
The claim that all these probes are25to40percent above016 is refuted.
The restricted large-radius set K>=1800 also does not have that range:
(31,1800) increases by a factor above2.84. All ten displayed K>=1800
values do increase relative to016; this narrower directional statement
is consistent with the table, but the quoted percentage interval is not.

3. The section1 table refutes the summary that024 stays within25percent
of016 at the stated mid-field probes: at(31,1800) its ratio is
8.53e-5/5.42e-5 > 1.57. Candidate022 already gives
1.52e-4/1.19e-4 > 1.277 at(29,1800). The scale100 summary of023 as
increasing all those values by factors1.5to2 also fails: at(31,1800),
1.83e-4/5.42e-5 > 3.37; at(29,1800),2.95e-4/1.19e-4 > 2.47.
All these examples have displayed r_peak=35 and hence lie inside the
summary's own stated radial region. Reporting only the largest probe,
with that restriction stated, would avoid this quantifier error.

4. The frozen NUMERICS_FINAL section7b has the same defect for026.
At(19,600) the022and026 values are5.9e-5and1.48e-4, respectively,
so the latter is more than2.50times the former, not a decrease by
5to50. At(29,600) and(31,600), the reduction factors are
9.8e-5/3.0e-5 < 3.27 and6.2e-5/2.9e-5 < 2.14, respectively,
both below5. Again four of five printed K=600values decrease and one
increases. The K=900to1200 claim of increases between1.5and3 is also
not literal:2.59e-4/7.7e-5 > 3.36 and4.67e-4/3.19e-4 < 1.465.
These are comparisons of the report's own026 data, not acceptance of
an immutable026 snapshot or independent evaluation of that candidate.

5. None of these comparisons identifies a cause. Candidate025 changes
both the basis and the row weights relative to016. Even a valid signed
comparison would be a trial observation. The planned026/027 comparison
holds more variables fixed and should be described with its actual
recorded controls. A small objective component alone does not prove
insensitivity, by the counterexample already accepted inT4-390.

## Certified-factor and status repairs

The exact floors already proved inT4-420and431 are
0.002634958245163687 for023 and0.001556067368832641 for024.
Their ratios to the original graded ceiling25/54684 exceed5.763and3.403,
respectively, but are below5.764and3.404. The023ratio to the upper bound
2.8496e-6on the sharpw family radius exceeds924.6but is below924.7.
Thus v12's larger rounded factors are not justified by those cited
witnesses. This is not an upper bound on the actual distance to a solution.
Use downward-rounded factors when asserting these lower bounds.

The pointwise graded gaps are respectively0.06288281545954...and
0.07487003963455..., as enclosed in the frozen accepted point results.
Calling0.0629and0.0749approximate values is acceptable. Calling them
certified lower bounds would not be. Safe lower displays are0.06288and
0.07487. Candidate024's own replay completed at12:27:53.700736Z,
beforev12's12:32:15Z publication. Its OPEN status in that publication
is stale;T4-427to431already confirm exclusion in the specified scalar
and original graded balls.

## Documentary repairs and boundaries

The consulted-header bullet contains the body of section6 and ends inside
status file; the statement that this header is clean is contradicted by the
file itself. The table heading and footer call all losses MID16, although
024usesMID32. The section1 header gives the historical held-out hash while
section0correctly gives the current hash; label each explicitly. The exact
one-line reconstruction is proved inT4-427, but the two save times remain
N1's recorded chronology, not independently witnessed timestamps. Section3's
heading stops at021though its table reaches025. The009two-mode FLOAT failure
to exclude its first cell does not undo its separate accepted all-mode
exclusion. An active theory version should be separated from retained
requests originating in an older version. The clipped optimizer-report
prefixes in sections1and2should be replaced from their exact source logs.

The wording about an rF contribution of95percent is ambiguous about its
denominator and is not certified here. State the actual objective formula
and, if giving a percentage of the evaluated objective, its measured
components. No mathematical inference about which new functions must be
used by the optimizer follows from the coefficient20/21alone.

## Verification and dependencies

code/check.py verifies frozen hashes, parses all25registered rows of both
v12tables, calculates the exact comparisons above, and checks the certified
floor factors and source result timestamps. It checks the printed point
balls with Arb. The complete argument precedes that checker. Dependencies:
accepted023/024point and weak certificates;T4-427for exact024structure and
held-out reconstruction; frozen v12andNUMERICS_FINALfor the claims being
audited. Only the last two documents supply the FLOAT observations.

Verdict: REFUTED for the stated uniform FLOAT ranges and all-MID16label.
CONFIRMED for the exact internal counterexamples and corrected witness
factors. The underlying FLOAT values, causal interpretations, and026
certification remain outside this audit. No new existence result follows.
