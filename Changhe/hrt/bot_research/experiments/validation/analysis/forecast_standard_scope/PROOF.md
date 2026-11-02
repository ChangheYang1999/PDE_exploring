# Standard-start v28 forecasting and the foreign-map fallback

## Statement and hypotheses

Fix the bundled balanced engine, a standard initial state with no buildings,
and the exact v28 Insurer source used for P5TNUB. Let the real target be a
fresh Insurer with fixed parameters and let its private model be a second
fresh Insurer with the same parameters. Both receive the same public
observation of the target at every reached round, once per round starting
at round1. The model receives copied observations and has no access to the
real target object or pending action list. Assume the inspected standard
Insurer path and its frozen v7 planner are deterministic functions of their
arguments and own state, and that each call terminates. They use no clock
cutoff or random source. Engine actions may be rejected, but the engine
creates no building except through an accepted action of its owner.

Then the real target and model return the same action list and maintain the
same private state at every reached round. Neither enters Insurer's foreign
map fallback. Therefore the model's legal purchases give the target's exact
active roster after submission. This conclusion does not assume that the
other player's policy is deterministic. It does not extend to a model of a
different target, a skipped-call prefix, an externally supplied map, or an
interrupted call.

## Proof

Write R for Insurer.requested, the set of all cells at which that Insurer
has returned a construction request so far. Initially R is empty and the
engine's map is empty. After each call on the standard path, Insurer adds
every returned construction cell to R. Every building present next round
was created by an accepted request of that player. Hence its cell belongs
to R, even if other requests were rejected. Buildings are permanent under
the bundled rules. By induction the actual target's observed building cells
are a subset of R before each call. The foreign test, which asks whether
there is a building cell outside R, is always false.

Induct simultaneously on equality of the two Insurer states. They start
equal. If they are equal before a round, their inputs are equal and their
standard transition is deterministic. Thus their returned lists and next
states are equal. In particular their requested sets are equal, so the
model's foreign test is also false on the observed target map. This closes
the induction. Applying equal legal purchase lists to the same observed
roster yields equal post-submission rosters. Opponent actions do not alter
this player's purchase legality or roster activation.

## Dependencies and scope

The argument depends on td_game/engine.py, td_game/actions.py, v28's
Insurer.__call__, its requested-cell update, and the deterministic frozen
v7 planner and gamekit helpers on the standard path. Source hashes are
recorded alongside this proof. This is an informal proof, not a machine
checked theorem. Actual prediction traces remain an independent implementation
check; they are not a substitute for the hypotheses.

v28 imports economy20 for its foreign fallback. That component passes a
finite 1000000-second deadline to a different planner and uses a fixed
pseudorandom replanning seed. Its mere presence in the import closure does
not mean that a standard-start v28 call executes it. When the modeled target
has different parameters or is a different policy, a real construction
outside the clone's requested set may activate that fallback in the clone.
Such models require separate empirical checks.

The frozen forecast_handoff/PROOF.md line73 and DESIGN.md lines15-16 described
the clock limitation too broadly. This result corrects that explanation
without changing the frozen experimental source or plan. The forecast-handoff
legality theorem and declared forecast-versus-visible comparison are unchanged.
