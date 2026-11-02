# Component evidence

The informal argument was written before the checks. `conditions.json`
declares four full-map fixtures inherited from the earlier capacity study,
seven dense-roster offsets, four requested damage thresholds, and sixty
original-combat comparisons. The largest requested threshold exercises
multiple complete spawn cycles. Earlier entries cycle through three types,
and an expired entry precedes them to check dense active indexing.

Executed from the project root with the prescribed Python, bytecode,
temporary-directory and CPU settings:

    .venv/bin/python -B -m bot_research.experiments.validation.check_fixed_capacity --output bot_research/runs/validation/fixed-capacity-component-001.json

The receipt completed at 2026-10-31T08:07:47.833209+00:00 in 22.603142 seconds.
All 7,028 prefix support/count comparisons, 112 sufficient-package minima
and 60 original-combat damage comparisons passed. The check independently
forms sets of possible firing times, exhaustively excludes every smaller
package under the certificate, and measures package arrivals through the
unchanged `combat_tick` and `spawn_schedule`. It does not establish a least
actual damaging package or bot strength. Source and input hashes are in the
receipt; the complete progress output is in the matching `.log` file.
