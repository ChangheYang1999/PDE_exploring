# Data-registration correction

Written 2026-10-31T17:07:25.269063+00:00, before replacement games.

The original 001 grid omitted three counter JSON inputs from its manifest: maze_layouts_001.json, staged_guards_001.json and screened_guard_001.json under bot_research/bots/counters/data. The constructors check their fixed SHA256 values internally, but the audit correctly requires explicit data registration and archive copies. The first twelve games completed and replayed; their data audit stopped the pipeline. No other original grid games ran. Retain those twelve as an incomplete initial attempt, not as the main result.

The 002 manifests retain all target and counter specifications, physical assignments, order and evaluation rules. They add these three exact data files and this correction note to the declared input hashes. No bot source or condition is changed. Rerun the full 120-game matrix. Compare all twelve repeated complete histories with the initial attempt and report any mismatch. The main claim remains the one in PROOF.md; the correction does not select conditions based on outcomes.
