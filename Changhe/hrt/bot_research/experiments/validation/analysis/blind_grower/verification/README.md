# Verification evidence

The source argument was written before completion of the no-defense control
campaign. The declaration is experiments/validation/forecast-grower-nodefense-001.json.
It specifies four standard-start games with first defensive round 51.

The completed audit at 2026-10-31T07:41:06.293197+00:00 recomputed the equivalent
blind FeatureBluff on original-engine observations. All actions matched in four
games and 42 rounds. Both player assignments were checked for each of the two
early-gun settings. There were no rejected actions or source changes.

Evidence relative to bot_research/:

- runs/validation/forecast-grower-nodefense-blind-audit-001.json
- runs/validation/forecast-grower-nodefense-strict-001.json
- runs/validation/forecast-grower-nodefense-replay-audit-001.json
- experiments/validation/audit_blind_grower.py

The separate unchanged-engine replay also passed all four games. This is finite
verification of the recorded instances, not a formal machine proof of the
universal statement. The source argument gives the conditional equivalence.
The completed forecast-grower-001 campaign starts defense by round 8 and is
outside that equivalence statement.
