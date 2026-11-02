# Generic persistent factory checks

The original evidence.json records the earlier IdentifyingCounter experiment.
The generic implementation is bots/counters/stateful_public.py. The component
checker is experiments/validation/check_persistent_factory.py. Its receipt is
runs/validation/persistent-factory-check-001.json: all ten checks pass. These
cover persistence, fresh-model reset, independent instances, rejected duplicate
and skipped rounds, fixed player assignment, and no state advance after rejected
calls. The fixture is a pure policy; no combat result is claimed.

The development manifest experiments/validation/stateful-lead-ten-001.json
specifies forty standard games against the fixed Lead10 C2 adaptive snapshot.
All completed. The audit receipts in runs/validation are:

- stateful-lead-ten-audit-001.json: forty legal games, twenty exact normalized seat pairs.
- stateful-lead-ten-projections-001.json: fresh136 full-action errors in1000 forecasts;
  persistent0 in1000. Construction errors0 in both styles.
- stateful-lead-ten-replay-audit-001.json: forty complete unchanged-engine replays pass.
- stateful-lead-ten-comparison-001.json: twenty fresh/persistent comparisons,
  equal final HP and outcomes, no identical complete histories.
- stateful-lead-ten-summary-001.json and .md: aggregated counts and exact conditions.

Audit completion was 2026-10-31T07:29:12Z. The finite observations support the
conditional proof under known identical initial state and one call per observed
round. They do not establish exactness after an unobserved prefix or against an
unknown factory. The earlier preliminary receipt is retained as historical evidence.
