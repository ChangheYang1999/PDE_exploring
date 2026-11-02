# Retargeting the handoff forecaster to P5TNUBM

## Exact statement and hypotheses

Let the target be the frozen source of lead v30 with the P5TNUBM parameters in the accompanying manifest. Start the bundled balanced engine from its standard empty initial maps. Give ForecastHandoff an independent PersistentFactoryModel of that exact source and parameter dictionary. Call the real target and clone once in every reached round, starting at round 1, with identical public observations of the target. Assume the standard v30 transition and its frozen v7 helpers terminate. They contain no random draw or wall-clock cutoff on this standard path.

Then the clone returns the same action list as the target in every reached round. In particular its forecast of the target's legal active roster after purchase is exact. This is an information claim, not a winning guarantee. The separate empirical hypothesis is that replacing the former P5TNUB clone by P5TNUBM restores a counter win at handoff 9 or 10 on the standard start.

## Notation and proof

Let R be the target's requested-cell set, initially empty. Every building the engine creates for that player comes from one of its own accepted construction requests. Each returned construction cell is inserted into R before the next call. Thus the target's observed building cells are a subset of R in every round. The foreign-map branch of v30 is therefore never reached. This invariant is unaffected by rejected requests, since they also add cells to R and never create an unrequested building.

Let q and q' be the real and cloned private states. They are initially equal. If q=q' before a call, the copied public inputs are equal and the standard transition is deterministic, so the outputs and updated states are equal. In particular both requested-cell sets remain equal and the clone also stays on the standard branch. Induction proves equality for every reached call. All original actions alter only the submitting player's own state, so the opponent's still-hidden current actions cannot change the target's purchase legality or active roster. Applying the equal forecast list to its visible state therefore gives the same active roster as the actual submission.

The v30 addition filters the list of speculative threats and chooses a bounded planner invocation in passive rounds. It does not alter the requested-cell invariant or introduce a random or clock-dependent operation on the standard branch. The same argument would fail with a different target parameter dictionary or skipped observation calls.

## Empirical method and limits

The four games are handoff 9 and 10 in both player assignments. The existing disclosed-counter campaign supplies the old-model controls; only the model specification and parameter dictionary differ. All other counter parameters and the target remain fixed. Fresh-process game results, strict accounting, source/data binding, original-engine replay, and full public-history shadows are checked independently. Shadow checks must report both counter-action reproduction and agreement between the target's recorded actions and clone predictions. A counter win would be evidence only on those exact games. A loss would refute that instance of the proposed repair even if the predictions were exact. No reserved final condition is used.

## Dependencies

The invariant and clone argument instantiate ../forecast_standard_scope/PROOF.md and ../stateful_forecast/PROOF.md. The observation-only counter and sequential legality arguments are in ../forecast_handoff/PROOF.md. Exact source hashes and parameters are in ../../retargeted-forecast-001.json. This is an informal proof with separate executable verification, not a machine-checked theorem.
