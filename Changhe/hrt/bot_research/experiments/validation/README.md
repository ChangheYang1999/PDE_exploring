# Independent counter and validation evidence

The chronological findings, conditions and qualifications are in
`bot_research/notes/validation.md`. Informal arguments and their verification
artifacts are indexed in [analysis/README.md](analysis/README.md).

The development tools here use the unchanged game engine. A repeated deterministic
trajectory is a reproducibility check, not an independent sample. Both player
assignments are recorded. Timeouts and invalid games are excluded from strength
scores and retained separately.

Useful entry points:

- `run_long_development.py`: bounded, resumable, fresh-process games from an explicit
  development manifest. It records source closures, failures and replays.
- `audit_development_campaign.py`: validates complete or partial campaigns and
  explicit retries, retaining unresolved conditions.
- `run_forecast_full.py` and `audit_forecast_campaign.py`: actual games and independent
  checks of a public-policy counter's predictions against submitted actions.
- `replay_audit.py`: reconstructs each saved game from its submitted actions and
  compares every round and outcome with the original engine.
- `final_validation_strict.py`: reserved validation, with critical-source checks,
  separate standard and continuation-stress conditions, and a frozen candidate.
  Each pool is reserved until its nominated frozen candidate is tested; subsequent
  disclosure retires it from fresh validation of later revisions.
- `audit_lead_metagame.py`, `solve_metagame.py`, `check_metagame_certificate.py`:
  original-engine replay, a proposed empirical policy mixture, and exact independent
  algebraic checking. The optimizer requires the offline numerical environment;
  the checker does not.

Run from the project root with `PYTHONDONTWRITEBYTECODE=1`, `python -B`, and
`TMPDIR="$PWD/bot_research/tmp"`. Use the existing environment, the lane's assigned
CPU affinity and low priority. Each command exposes its options with `--help`.
Output paths must be new unless a documented `--resume` option is used. Actual
commands and exact manifests are recorded alongside each result. No tool here
requires a server, JavaScript, a GPU, or remote compute.

Completed independent validation of best_v9a is recorded in
`bot_research/runs/validation/final-best-v9a-poolA-summary-001.md`. It binds the
candidate source hash to all 60 prescribed pool-A conditions and complete
original-engine replays. The standard result is 10 wins and 10 draws; each of
the two continuation stress sets is 6 wins, 12 draws and 2 losses. The two
original 300-second mirror timeouts and their successful 500-second retries
remain separately recorded.

Frozen best_v9b subsequently completed all 60 pool-B conditions, with
20 wins in each of the three separately reported start groups and all
60 original-engine replays passing. See
`bot_research/runs/validation/final-best-v9b-poolB-summary-001.md`.
All 30 seat pairs match completely. The exact-parameter overlap audit
finds no overlap for B within its recorded scope at that evaluation. A and B
were subsequently disclosed; later candidates cannot inherit their held-out
status. Pool C remains unused. See [EVIDENCE_INDEX.md](EVIDENCE_INDEX.md) for
the newer development counters and their completed independent checks.

The saved evidence can be rechecked with `audit_reserved_campaign.py`, followed
by `summarize_reserved_replays.py` and `render_reserved_summary.py`. These tools
check the original manifest, generated jobs, source archive, all attempts,
selected replay receipts and final source identity. Choose new output names;
do not overwrite the completed receipts. The separate loss accounting is in
`bot_research/runs/validation/reserved-loss-diagnostic-final-001.json`.

A public-factory forecast is exact only under its stated state assumptions.
`bots/counters/public_factory.py` makes a fresh policy on every call;
`bots/counters/stateful_public.py` retains one independent policy object and
requires one call per consecutive round from round 1. See the stateful-forecast
proof in the analysis index and the explicit development manifests before
using either wrapper to characterize a target as exactly forecastable.

Recent completed work (2026-10-31T15:20:40.185068+00:00) includes model-free public-budget handoffs and a four-policy cycle. The exact conditions, complete replay checks, fresh policy-generation checks, and finite rational certificate are linked from EVIDENCE_INDEX.md. Use check_budget_handoff_histories.py for those counters and check_declared_policy_histories.py for both factory policies in a standard-start campaign. publish_budget_and_cycle.py records the budget result; its v2 publisher records the cycle because the first publisher expected an integer matrix instead of the stored rational objects. That pre-publication assertion affected no game. Neither frozen publisher should be edited.

Update 2026-10-31T15:37:03.030963+00:00: the current counter result is [one guarded round-four strike against both nominees](analysis/guarded_round4_strike/RESULTS.md). The exact eight matched disabled controls are included. [No-strike deadline controls](analysis/no_strike_handoff_controls/RESULTS.md) and the [equal-prefix proof](analysis/nominee_prefix_equivalence/RESULTS.md) clarify the adaptation claims. See EVIDENCE_INDEX.md for all recent results. Pool C is still unused.

Update 2026-10-31T16:13:20.553395+00:00: `run_prefix_development.py` supports explicit development cases with prescribed candidate-relative prefixes and skipped policy calls. `check_best_entrypoints.py`, `audit_best_entrypoints_bounded.py`, and `summarize_entrypoint_audits.py` compare fresh direct and factory entry points on recorded histories, with source and input pinning. The best_v9e preflight covers12 games and358 decisions per entry point. `audit_team_fortress_table.py` independently replays the retained x158 logs and explicitly records missing ones. Current counter and selector results are indexed in EVIDENCE_INDEX.md and analysis/README.md.
