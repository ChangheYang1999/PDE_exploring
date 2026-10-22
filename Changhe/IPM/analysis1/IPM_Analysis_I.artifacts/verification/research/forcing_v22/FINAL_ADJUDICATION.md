# Final scope of the p9 v2.2 forcing audit

Read this with PROOF.md, ADDENDUM.md, RANGE_REFINEMENT.md,
DISTANCE_ADDENDUM.md, HESSIAN_EXPORT_ADDENDUM.md, CODE_ANNOTATIONS.md,
FINAL_PROVENANCE_SUPPLEMENT.md and UPSTREAM_SCOPE.md. The timestamp and
complete file hashes of the executed final audit are in evidence/verdict.json.
This document becomes final only when that audit succeeds.

## Conditional finite theorem

CONFIRMED: for the exact dyadic data in v22_p9_merged.json, under H0,H1,H2
of ADDENDUM.md, uniformly over the entire saved source bracket,

| lambda | N at order3 | N at order4 | N at order31/10 |
| --- | --- | --- | --- |
| 1 | <0.7759 | <893.16 | <1.5700 |
| 500 | <1.8107 | <1638.56 | <3.5769 |

N is the unitary-Fourier multiplier norm with weight
(lambda^2+|xi|^2)^(s/2). These are conditional bounds on tau times the
physical residual. They are not accepted physical forcing norms.

The fixed source pair is cert_forcing.py
5066d240ea60b89d137025f60fbda4e631b7cf7e67f8ef5968bab307bbeddcd9
and cert_forcing2.py
012e106b568ec68876058ee0588aa64cfbe9c846dc44523c164424015c238197.
The merged data hash is
b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201.
All26 part files are retained locally as compressed, hash-checked copies.
The33 snapshots contain164893125 original bytes in93208855 stored bytes.
Recompression or removal of the numerics lane's original part files does
not change these copies. The separately pinned external Green and trial
files remain read-only inputs for the source-geometry linkage.

## Methods and finite results

The preceding v2.1 geometry audit is inherited only after rehashing all
208 pins and comparing219745 exact fields over43949 retained rows.
The106496-case cover includes62547 omitted cells outside the support.
All7810 canonical partition points lie in the current Green endpoint
boxes;52 local endpoint fields and the exact source bracket agree.
The179 pins of topic118 additionally bind the current trial hash to its
contemporary replay. The geometric cover itself does not use trial
coefficients. Every retained regime label and its source sigma branch
are checked directly in exact rational arithmetic.

Each of263694 cutoff inequalities passes an Arb256 complete-algebraic-
extrema check and an independent exact rational full-polynomial Bernstein
check. The latter uses nine contiguous batches covering every row. A
second complete replay of those batches records the source and input
hashes before and after each bounded subprocess, its exit status, and
the output hash. All nontime fields must equal the original results.
The17870 nonconstant-cutoff rows consist of16502 transition rows and1368
straddling rows; the remaining26079 rows have constant cutoff1. The old
output key called transition counts all nonconstant rows, not H2 alone.

For all27447 inside or straddling rows,137235 pointwise product checks
pass separately by exact rational arithmetic and regrouped Arb384
expressions. The331 active scalar series triples on38445 row occurrences
pass exact squared inequalities, Arb384 roots and guarded iv120 log/exp.
The43 fallback blocks contain5504 inside rows; no series claim is made
for them. Those scalar tests do not establish the physical series operands.

All43949 row contributions are aggregated by direct Arb512 expressions
and a different exact nine-moment polynomial expansion with iv160 powers.
Fourteen cross-engine comparisons pass. Each of the six strict public
ceilings has an exact positive power-comparison gap. The source's15
Cartesian multiindices,30 table entries,4 radial derivatives,5 scalar
composition orders,7 Leibniz expressions,16 binomial ratios and91
centering identities agree with independent exact symbolic formulas.
No inequality between the two older/current G0 arrays is assumed;52 G0
endpoints increased, while all43949 GL2 endpoints stayed equal.

## Rejected attempts and repaired verifier errors

The first factored iv cutoff attempt timed out. The separate-factor
Bernstein attempt was too coarse on ten diagnostic rows. Neither result
is a completed range certificate or a refutation of the producer's bound.
The full-polynomial exact Bernstein method subsequently passed every row.

An initial full-polynomial assertion incorrectly demanded dmin>=0.
Row20999 has dmin=-2^(-1074), a valid outward lower endpoint for distance,
and dmax<231/8000. Replacing that assertion with dmin<=dmax and dmax>=0
is justified by the exact physical intersection with nonnegative radii.
This verifier assertion failure is retained and is not a producer defect.

REFUTED: the original auxiliary Hessian export claimed every exported
endpoint was below the producer's T2F. On26079 constant rows it exported
nextafter(0,+infinity)=2^(-1074), while T2F=0. The core Arb check used the
exact value0 before export and was correct. The separate repair changes
only those26079 auxiliary entries to their proved constant value0 and
checks all43949 output entries. The original code/output and failure
record remain immutable and explicitly annotated. Neither aggregation
nor the core cutoff check consumed the erroneous auxiliary array.

The first equality diagnostic also wrongly required old/current G0
identity. It failed on an increased endpoint and was replaced by
geometry-only transfer. The complete row linkage records all52 increases.
Every failed attempt is preserved with its limited scope.

## Independent model exchange

The first actual Claude Opus5.5 response, request
f4b7c98b-0755-4a00-b5a7-12f6f5d49848, ended09:38:36Z with max_tokens.
Its partial objections were useful, but that response was not acceptance.
A later request with thinking disabled was rejected by the provider's
configuration validation before any model execution. That failed request
and its metadata are retained; no substitute model was used.

The complete adaptive follow-up used actual claude-opus-5-5, request
5538c439-4092-46aa-96be-2d8cbb75f73a, input hash
8125e83370fe50b8c6e1caca79092b05392a670f061c6e629e59763476ccf323,
and ended2026-10-21T09:56:15.009566Z with end_turn. It accepted the restricted
conditional theorem after reconstructing the norm, radial, product,
extremum and Bernstein identities. It retained H0,H1,H2 as open and
requested three mechanical provenance improvements. These are addressed
by FINAL_PROVENANCE_SUPPLEMENT and the complete pinned replay, not by
silently changing previously reviewed files. The final audit authenticates
all current request bundles, raw model text and actual-model metadata.

## What remains open

H0 identifies the residual and its weak derivatives with the canonical
physical trial, including the interface regularity needed for H4.
H1 requires the actual G bounds on26079 inside and1368 straddling rows.
H2 requires the five actual composed forcing bounds on16502 transition
rows. They hold throughout each restricted physical cell and uniformly
in the source bracket, rather than just at mesh points.

The upstream jet producer is _cell_core_deriv in cert_resid.py
1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053,
using midrad.py
5b5feb4ad511e66d57d228a3b754e44cfa2ceb17a33f717dde991c464d5f598e.
It reads cert_green.npz
c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1
and trial_v2_h0.008.npz
a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.
The independent full Green/T/P/R audits98,99,101 are queued and unfinished.
Their completion would still not certify the five nonlinear residual
jets,441935 coefficient boxes and33995 remainders on these13 parents.
The angular assembly, Cartesian conversion, recentering, cutoff products,
truncations and Bernstein ancestry also require complete physical checks.
Topic72's conditional dot-product arithmetic lemma does not verify the
actual BLAS kernel. A C0 remainder cannot be differentiated to fill a gap.

The15 partial-derivative suprema on B_{9delta/4}(P) and B_{3delta}(P)
have separate unresolved physical ancestry. The larger disk includes
unretained cells. Its certificate does not follow from the43949 support
rows, even though partwise maxima merge exactly. Topics120 and121 concern
a different contemporary replay and do not certify the historical v2.2
forcing model by equality of a few scalar operands.

This physical chain cannot be closed from the present evidence in a few
hours. The working priority returns to the middle-region second method
and then98,99,101,107. No global inverse, nonlinear closing inequality,
meaningful neighborhood exclusion, or decisive IPM endpoint is established.
