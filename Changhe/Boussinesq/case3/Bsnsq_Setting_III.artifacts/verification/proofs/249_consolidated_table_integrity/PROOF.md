# Integrity of the consolidated finite residual table

## Exact statement

This packet checks a finite transcription claim. For each published CSV row, the key is the tuple (verifier audit folder, state label, inverse label, field, radial band). The authoritative measurement is the row with exactly this key in that folder's REGIONAL_RESIDUALS.json. The authoritative represented state is the frozen archive whose SHA256 is recorded both in the regional record and in the folder's manifest and original result. Numerical metadata must be read from that archive, with a blank cell when the archive omits a requested metadata item. A stored leading coefficient can be reported separately, but is not substituted for a missing target amplitude. A filename prefix, rounded beta or neighboring row is not a join key.

If every key occurs exactly once in each compared table, the full key sets agree, all displayed measurements agree with their source records, and every metadata entry agrees with the archive fixed by the source hash, then the published finite table is a faithful copy of these records. This statement concerns data identity and attribution, not the correctness of the PDE evaluator. Conversely a mismatched key, value, hash or metadata field refutes the corresponding transcription claim.

## Proof and scope

Unique keys define functions on the finite key set. Equal domains and pointwise equality imply equality of the functions. Agreement of the state hash with the manifest and original result fixes which literal archive the record represents. Recomputing the archive hash and reading its scalar data checks the reported parameters without relying on a label parser. Source measurement hashes connect the regional reduction to the existing result; the PDE and inverse audits are separate dependencies with their own checks. Hash matching is an operational file-identity safeguard, not a mathematical theorem that cryptographic collisions are impossible.

For each state, the sampled maximum of one residual is the maximum of the six disjoint radial-band maxima. It is a finite sampled quantity. The corresponding regional point counts sum to the actual number of grid points used for that field. Divided fields retain the two axis directions, while the original Cartesian ratios omit their vacuous axis values. Therefore a single asserted radial or point count must be checked across all represented grids, not copied from one grid. An exact positive center residual or a rigorously certified infinite tail residual, when already proved, remains a separate fact and is not newly inferred from this table.

Agreement of two rows' scalar metadata or maxima does not prove equality of their fields. Exact duplicate archive hashes should be reported so an audit-state count is not confused with a distinct-field count. Family labels describe provenance and must be justified by the archived source and continuation records, not merely by epsilon=1. A source with an additive lambda term and a source homotopy using epsilon have different diagnostic equations, though both have separately evaluated self B2 residuals. No table of failed states excludes uncomputed profiles or proves a continuum limit, exact branch or local fold.

This argument was written before freezing and checking the consolidated table. The code will read only the numerical lane's published CSV/Markdown and the verifier's own frozen JSON/NPZ records. It will not execute numerical-lane code or recompute the long regional grids. Input hashes, comparison outcomes, any counterexamples and actual times belong in verification/. No formal build is used.

## Verified finite conclusions

The comparison finished 2026-10-22T02:04:57.628362+00:00. All CSV values, metadata and rounded Markdown cells match their stated frozen source records. The radius counts are 145, 161, 177 and 189, refuting the uniform 161-radii description. The 95 audit entries use 93 distinct archive hashes. These finite conclusions and the initial parser repair are recorded in verification/SUMMARY.md and checks.json. They do not supply a new PDE proof.
