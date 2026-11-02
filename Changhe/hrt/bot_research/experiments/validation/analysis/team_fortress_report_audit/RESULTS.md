# Independent audit of the fortress x158 table

Recorded 2026-10-31T16:10:02.147352+00:00. Verdict: CONFIRMED for corrected counts and retained replay results.

The table contains sixty games: three fortress versions, two lead policies, five initial conditions and two player assignments. Fortress has 0W/6D/6L in twelve standard games and 24W/0D/24L in forty-eight continuation games. The published defense note's counts of ten and forty omit one fortress version from its denominators.

All six standard games against P5TNUBM draw at 785:785 after each side deals fifteen damage. These are not no-hit draws. Against best_v9e, fortress finishes 785:790: fortress deals ten damage and the lead policy deals fifteen.

All thirty-six retained replay logs reproduce exactly through the unchanged engine, with pinned current engine sources and matching row attestations. Twenty-four winning continuation rows have no saved replay. Their labels and counts are checked from their result rows; they are not independently replay-verified here. This audit adds no new strength games.

Evidence: [row and replay receipt](verification/x158.json). Initial checker failure on absent logs is retained in `../../../../runs/validation/x158-table-audit-001.log`; the corrected audit explicitly records missing logs.

A separate terminology correction applies to x159: `guarded_round4_trigger` uses public-budget pure-tier defensive forecasts and does not clone or identify P5TNUBM. Its failed transfer to fortress is still valid evidence. The exact-model counter is the distinct `early_heavy_handoff` family.
