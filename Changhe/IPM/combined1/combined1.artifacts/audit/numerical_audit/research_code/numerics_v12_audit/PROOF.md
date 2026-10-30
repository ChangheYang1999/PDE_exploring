# Numerical report v12: literal claims and quantity audit

Written UTC 2026-10-29T12:41:58.228681+00:00, before the checker. This is a source and report audit, not
certification of the reported floating point values or an optimizer replay.

## Statement, notation and scope

Let v12 denote the exact frozen publication source/numerics_v12.md. Let
m_(candidate,n,K) denote its printed FLOAT weak-distance proxy. This is the
quantity m=2|I|/(D+sqrt(D^2+4H|I|)) in the frozen weak_tests3 source,
where I is a signed mesh residual pairing, D=A+B+C, and H is a mesh
estimate. These are distinct quantities and have no certified error bounds.
The claims below concern consistency of the literal report with its table
and code. We do not identify printed decimals with exact PDE quantities.

## Complete argument and findings

1. The header is still corrupted. Its consulted bullet contains the entire
three-item status passage from section6, between RUN_1. Reading and the
closing parenthesis. Section0(a)'s assertion that this header is clean is
therefore false. The supplied text suffices to decide this literal claim.

2. The blanket claim in the header and section6 that candidate025 reduces
all five K=600 registered values by factors3 to30 is false. At n=19,
2.04e-4 exceeds8.18e-6 by about24.94. The improvement factors016/025
for n=23,25,29,31 are about3.875,29.26,2.403,2.008. In particular two
improve by less than3 and one worsens. These discrepancies are far larger
than last-place rounding of the displayed three-significant-digit values.
The exact ratios of printed decimals are retained in JSON for checking;
they are not certified ratios of the underlying infinite-plane quantities.

3. The blanket claim that all K>=1200 values are25 to40 percent above016
is also false. At(25,1200) the ratio025/016 is4.05e-4/1.16e-4,
about3.491. At(31,1200) it is4.22e-5/1.27e-4, about0.3323, and
at(29,1200) it is about0.599. The value at the reported maximizing
probe(19,1800) changes from9.02e-4 to1.27e-3, about40.8 percent.
Only a statement scoped to particular probes or the sampled maximum can
be justified by this table. No cause or basis capability follows.

4. The14 held-in table entries are m values, not raw pairings I. The
source computes both and stores them under different keys. Calling these
rows satisfied to1e-8 to6e-6 without naming m conflates a necessary-distance
proxy with the analytic objective pairing. The actual residual pairings
require their own I values and normalization. A small m does not prove
that the field satisfies the corresponding equation exactly.

5. Section0(h) correctly limits independent observation of the024 hash
repair but then asserts without qualification that both versions precede
launch. The single reverse-heading edit proves the equality of byte hashes
and preserves all60 probes. It does not observe either09:13 save time.
Retain the author's assertion explicitly as a historical claim, distinct
from the independently observed byte reconstruction. No false registration
is inferred. Section1's heading needs the same qualification.

6. The summary LOSS header and footer still assign MID16 to024, despite
section0(h)'s explicit correction and the actual024 launch using MID32.
The per-step paragraph repeats MID16 as its blanket mesh and optimizer
label. Correct these labels. Both radial rule and CPU/CUDA backend changed
between016 and024, so their difference is not an isolated rule experiment.

7. The sum of rounded FLOAT accepted-step norms does not establish a
certified bound on the density difference between exact candidate files.
For exact iterates in one fixed norm, telescoping plus the triangle
inequality gives ||rho_last-rho_first|| <= sum step norms. The displayed
step numbers are rounded FLOAT mesh values without outward error bounds.
The initial Taylor projection occurs before optimization and the final
exact rational conversion after it, so those endpoint changes require
separate accounting. The per-step Taylor projection DOES occur before
dRho2 is measured in ipm_opt3 and is included in that logged step. Do not
claim it is omitted. Only the initial projection and final conversion are
outside the accepted-step chain. No own024/025 certified full-plane
density-difference bound has been computed as of this audit. The existing
022 comparison concerns another pair of references.

8. Section0's factors5.764,924.7 for023 and3.404 for024 are rounded
summaries, not valid literal certified lower floors. Keep them explicitly
approximate or round down against the accepted root and exact ceiling.
The underlying strict floors .002634958245163687 and
.001556067368832641 remain unchanged. This audit does not introduce a
new exclusion theorem or reverse an accepted certificate.

## Verification and dependencies

The checker binds every frozen source, checks the duplicated status text,
parses all25 registered rows of section2, and records exact rational ratios
of their printed decimals. It checks the two counterexamples and source
ordering of the per-step Taylor projection and dRho2 measurement. A source
inspection record covers the historical and quantity-scope distinctions.
All conclusions retain the exact publication hash. Changes belong in a
new immutable publication, never an edit of v12.
