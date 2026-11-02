# Full-game intervention declared 2026-10-31T11:16:09.873655+00:00

The verified round41 witness establishes only current-round feasibility. The
next falsifiable hypothesis is that a 30-step defensive search improves the
full-game outcome over 15 steps against frozen best_v9b after the known
asym:3:2 opening, for one or more of three fixed offensive schedules.

Both arms use the same new wrapper, the same frozen target and private model,
the same initial state, the same opening and the same attack schedule. Only
free_steps differs. Each arm plays both assignments. The schedules are the
previously studied tier3 purchase in round5, tier4 purchase in round7, and one
tier4 in each round5 through9. All twelve conditions are declared before play.
The no-change control is rerun under this wrapper to avoid treating a changed
module name as an unverified equivalent opponent.

The known-prefix forecast theorem in ../prefixed_forecast/PROOF.md applies:
all target and model calls are retained during the prefix. Four component
prefixes must pass exact forecast, adapter, legality, call-count, and input
immutability checks before full games. Neither this theorem nor the witness
proves a full-game improvement. The 30-step policy may spend more earlier,
change its economy, or still face an unavoidable later loss. The complete
matched trajectories, runtime and original-engine replay determine the
empirical result. Unresolved timeouts are excluded from outcome comparisons
and remain visible. These are development conditions, not reserved validation.
