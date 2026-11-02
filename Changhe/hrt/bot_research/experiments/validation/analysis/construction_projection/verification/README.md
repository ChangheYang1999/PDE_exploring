# Evidence registration

The proof was written before executing the full projection audit.
experiments/validation/audit_forecast_projections.py compares ordered
construction, minion-purchase and factory-purchase projections separately
for every recorded prediction in a declared complete campaign. It freshly
checks result and source attestations and compares predicted actions with
actual submitted actions in the archived original-engine log.

The first application is experiments/validation/stateful-lead-ten-001.json,
forty standard games comparing fresh and persistent models of the same Lead10
adaptive setting. The completed receipts are in runs/validation:

- stateful-lead-ten-projections-001.json: fresh construction0 errors, full actions136
  errors, minion purchases136 errors and factory purchases60 errors in1000 calls;
  persistent0 errors in every projection across1000 calls.
- stateful-lead-ten-audit-001.json: all40 games valid, all20 normalized seat pairs exact.
- stateful-lead-ten-replay-audit-001.json: all40 unchanged-engine full replays pass.
- stateful-lead-ten-summary-001.json and .md: exact conditions and aggregate evidence.

The audit finished at 2026-10-31T07:29:12Z. These finite checks support the
source-level argument; they do not replace its hypotheses or prove correctness
for another snapshot. In particular, Lead13's sticky fortress flag is outside
this proof. No Lean formalization was performed.
