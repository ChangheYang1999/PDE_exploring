# Eliminating identical one-round timing experiments

## Statement

Fix the bundled deterministic engine, one player assignment, a fixed initial
state, and a deterministic opponent with a fresh initial internal state. Let
B be a deterministic baseline policy. Let C be a policy whose action rule
coincides with B on every observation outside round r. Assume any internal
state on which later actions depend evolves identically when observations
and submitted actions agree. If C's action on B's round-r observation equals
B's action there, their entire match trajectories against that opponent agree.
If the baseline match ends before round r, the trajectories also agree.

## Proof

Before round r, induction on rounds gives the same policy inputs and actions,
the same opponent inputs, internal state and actions, and thus the same next
engine state. If the match ends in this prefix, both terminate together.
Otherwise round r starts in the same state. Its actions agree by hypothesis;
the opponent actions agree because its state and observation agree. The engine
therefore makes the same transition. The internal-state hypothesis and the
equality of the later action rules let the same induction continue after r.
Both terminal result and all intermediate records agree. This proves the
claim without a sampling or approximation argument.

## Application and limitations

KnownTiming differs from an attack_round=0 baseline only in the one selected
positive attack round, provided model, model_parameters, defense_first,
saturate_round and max_factories are fixed. The tier, share and count cap are
read only inside that selected-round branch. Its trace is append-only and is
never read to choose later actions. A candidate whose proposed list equals
the baseline's actual list at that round is therefore identical for the full
match. The private forecaster is recreated from the same public observation;
its computation does not mutate the real opponent's internal state.

`search_timing_equivalence.py` first plays and saves a complete baseline with
the original Engine. It reconstructs each pre-round observation from the two
saved snapshots and the saved rules, checks equality of the full ordered
submitted action lists, and records the comparison. Candidates with a
different list are played as separate full original-engine matches. The
source hashes must remain equal to the baseline's hashes throughout.

A reused result is explicitly labeled an equivalence deduction and is not
counted as another played match or independent sample. This method does not
apply to a policy with changed behavior outside the selected round, to
stateful or random candidates that fail the internal-state hypothesis, or
to altered opponent initial states. It cannot infer equivalence merely from
equal HP, equal action counts, or an equal immediate damage estimate.

## Dependencies and evidence

Dependencies are deterministic state transitions and the described restricted
candidate family. The verifier and experiment script are under
`experiments/validation/`, relative to `bot_research/`. Cross-check evidence
will be registered in `verification/evidence.json` before using deductions
in any reported search result. No theorem-prover verification is claimed.
