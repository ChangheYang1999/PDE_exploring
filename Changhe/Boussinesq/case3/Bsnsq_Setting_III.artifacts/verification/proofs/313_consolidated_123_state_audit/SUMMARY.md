# P313: consolidated123-entry residual audit

Published 2026-10-22T08:19:10.529794+00:00. The numerical transcription, archive/metadata joins and direct reductions of this verifier's saved evaluation arrays are CONFIRMED. Two grid-header assertions and the blanket all-forced sentence are REFUTED as written. The repaired text is in verification/approved_consolidated_residuals.md and approved_NUM_REPORT.md, with exact replacements in required_wording_replacements.json. Actual adoption remains OPEN. General B2 remains OPEN.

## Count and provenance

There are123 keyed audit entries from62 folders, with5904 measurement rows: each entry has2 velocity kinds,4 fields and6 radial bands. There are121 forced entries (5808 rows), covering117 distinct archive hashes, and2 manufactured controls (96 rows) with distinct hashes disjoint from the forced subset. The complete set covers119 distinct archive hashes. A hash count is not a count of mathematically distinct fields.

Here forced means the entry was computed for a stored source-velocity or defect-forcing problem rather than the unforced B2 equations; the self-velocity evaluation reports its B2-P residual separately. The two manufactured controls are S0 and manufactured_picard, both in farfield_grid_20261020T1930.

Four source archives are deliberately audited twice, with different folder/label keys:

| Hash prefix | First entry | Second entry |
|---|---|---|
|37a27aab|217_three_map_scale_audit / L1l096_L1p5|native_lambda096_K16_K24_20261021T025257Z / blam24v_lambda0.96|
|e3a4cb7c|217_three_map_scale_audit / L2v_L1p5|mbb_regional_20261021T1820Z / mbb_b3.0952_lambda0.989973|
|ee48b27b|K40_beta305_20261021T1631Z / blamB32_beta3.05|native_beta3p04_3p05_20261021T084200Z / K32_beta3.05|
|bc09e0a1|K40_beta3062_20261021T1653Z / blamB32_beta3.062|native_beta3p062_20261021T0910Z / K32_beta3.062|

These are documented aliases, not mislabeled distinct states. Radii and grid_points describe each audit's evaluation sampling; the archive hash identifies its source coefficient state. The first two duplicate pairs use166 versus161 evaluation radii, despite identical source bytes. All full hashes and per-audit counts are in duplicate_scope.json.

## Direct comparison and corrections

All5904 CSV key/value rows, archive metadata, Markdown summary cells and regional cells agree with the original records. Every radial reduction is independently recomputed from the saved own-evaluator raw arrays. Cartesian measurements omit x=0 where their factored residual is vacuous; F and G retain their axis treatment. The checks use each actual recorded mask. Zero numerator and zero normalizer are assigned ratio0 by the documented numerical convention; nonzero numerator at zero normalizer yields infinity. No denominator floor is introduced. The earlier95 entries have identical keyed CSV values, accounting for4560 rows; the28 added entries account for1344 rows. Whole-file byte identity is not asserted.

A decimal display cell is accepted within half of its displayed final decimal unit plus1e-14 conversion tolerance. This checks consistency at the displayed precision without claiming one specific tie-breaking rule. CSV parsed finite values are checked against the original JSON values. Missing metadata remains missing.

| Header assertion | Independent result | Verdict |
|---|---|---|
|Uniform161 radii|Actual per-audit counts145,161,166,177,189|REFUTED|
|13920-16992 points|Actual field-dependent counts range13630-18144|REFUTED|
|Every state is a forced-problem state|121 forced entries and2 manufactured controls|REFUTED as a blanket statement|
|123 archives means123 distinct hashes|The source did not assert distinctness. The verifier introduced that interpretation.|Verifier attribution withdrawn; not a source error|

The initial data run records133047/133050 passing controls: the first two false controls expose the two grid-header errors; the third is the withdrawn distinctness interpretation. Every numerical cell/join/reduction control passes. The separate scope audit passes4692/4692, and the final wording preservation check passes25/25. The initial4689/4692 scope run failed only on differing display precision and a literal vertex annotation, then used an explicit rounding comparison; its source and output are retained. The initial23/25 wording run contained a Python chained-comparison mistake in its negative-string control, fixed without changing any artifact numbers; it too is retained.

## New comparison claims

The63 NUM_REPORT summary rows agree with the original audit measurements at their stated precision. Q percentages are100(new-original)/original, using the matched12-point-quadrature source archive as baseline. Across the six48-point restarts, the largest absolute change in a normalized forced F/G sampled maximum is3.9730078%, whereas the largest absolute change in the absolute thermal sampled maximum is15.7341163%. These concern different quantities. The K32 coefficient changes are0.2239401% for F and0.1188500% for G; they are not asserted for every case. The two tighter secant states round to forced F/G maxima0.068/0.109. No exact discrete-root or continuous-problem conclusion follows.

EQ percentages compare each equal-budget result to its matched production K24/K32/K40 entry. The maximum absolute change among the four stated forced maxima is0.1437521%, hence below0.15%. The two map-scale triples have the following normalized forced sampled ranges:

| Triple | F range | G range |
|---|---|---|
|Lineage2 vertex|0.0002354429370 to0.0003187598903|0.0002411367694 to0.0003258719232|
|Lineage1 lambda0.96|0.0002674028984 to0.0002713108805|0.0005535393479 to0.0005568469640|

These comparisons concern the saved sampled maxima. Evaluation sets differ between some audits, so the differences cannot isolate changes in the represented fields from sampling effects. The121 forced entries' B2-P F maximum ratios range0.693002738 to1; their G maximum ratios range0.412113426 to0.993766813. These are not continuum bounds.

## Evidence, times and scope

The main reduction ran08:06:45.792281 to08:06:52.587884 UTC (6.795635s), the scope comparison08:10:00.943488 to08:10:01.037138 (0.093640s), and the final wording check08:17:17.650715 to08:17:17.700014 (0.049306s). Frozen CSV9367a7e4, artifact Markdown db3fcb81 and NUM_REPORT85f1c358 identify the inputs. Full SHA-256 records, checks and approved-text hashes accompany this report.

Actual Opus546/547 both returned claude-opus-5-5 and completed review and follow-up of the criterion and inference. Their requested scope, duplicate and grid clarifications were independently checked. See verification/model_adjudication.md. They did not inspect the raw arrays or reverify antecedent certificates.

This packet does not rerun the independent whole-plane inverse or PDE evaluator. Those computations and exact literal-state rejection certificates remain in the individual source packets. No new universal certificate-coverage claim is inferred from this consolidation. Neither rejection of stored states nor sampled residual floors excludes nearby exact solutions or proves nonexistence in the whole B2 class.
