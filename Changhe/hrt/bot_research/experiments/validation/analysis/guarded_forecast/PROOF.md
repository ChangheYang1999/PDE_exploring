# A prescribed guard opening with a synchronized public forecast

## Statement and hypotheses

Fix the unchanged bundled rules and a standard initial game. Let h be a
known deterministic opponent policy with known initial private state. Its
actions and next private state depend only on its private state and its
public observation. Exclude effects from randomness, wall-clock cutoffs,
mutable files, process identity and shared opponent objects. Assume all
model calls complete and predicted actions are legal.

Initialize an independent clone of h before round 1. At every reached round,
including round 1, advance that clone exactly once on a private copy of the
opponent's actual public observation. The observer may choose a prescribed
legal guard opening in round 1 and arbitrary legal, forecast-dependent
actions thereafter. Then every predicted opponent action list is exact.
Replacing only the observer's first action list does not invalidate the
forecast induction.

For a reached round r, reconstruct both players from the public observation,
apply the forecast opponent actions to its private player copy, and apply
the observer's chosen construction to its own private copy. If original
combat on those copies reports zero damage to the observer, then the
observer loses zero HP in that actual round. This second statement requires
that the private computation uses the same roster, ordering, route,
construction and combat rules as the actual round. A heuristic planner's
claim of zero damage without this equality is insufficient.

## Proof

Before round 1 the real opponent and its clone have equal private states.
They receive equal public observations, because changing only the player
index of a copied observation reconstructs the opponent's input. Thus they
produce equal actions and equal next private states. The observer's chosen
opening is submitted after this prediction and does not enter the real
opponent's current observation.

Suppose the opponent and its clone have equal private states before a later
reached round. Feed the clone the actual observation for that round, rather
than a predicted next state from the previous round. It equals the real
opponent's input, so determinism again gives equal actions and next private
states. This proves the first claim by induction. The observer's opening
may change all subsequent public observations, but both the real policy and
the clone receive those changed observations, so equality is preserved.

Each player's legal actions modify only that player's state. Therefore the
order of interleaving with the other player's actions does not change the
accepted constructions or purchases on either copied state. Original
combat is deterministic once the resulting map, ordered active roster,
round and rules are fixed. Equality of these inputs implies equality of
actual and privately computed damage. If the latter is zero, so is the
former.

## Strategic scope

The intended controller uses a gun1 at a declared coordinate, a declared
small round-1 roster, and factories for the remaining affordable gold. It
then uses the existing FreeForecast defensive search. The opening need not
be safe against an arbitrary affordable roster. The corner_guard result
covers only its stated three-tier1 opponent opening.

Exact prediction gives no guarantee that a zero-damage defense is affordable
or that the defensive search finds it. A positive opening HP lead can still
be lost. The controller's factory, attack and later saturation choices are
heuristics. No dominance or full-game winning claim follows from this
argument. Testing it against a different target from its declared model
also removes the exactness guarantee.

## Dependencies and planned checks

The clone induction is the stateful_forecast result. Action isolation and
observation semantics come from the unchanged engine audit. The existing
corner_guard proof establishes one particular first-round defensive case.
The intended module is bots/counters/guarded_forecast.py, a separate module
that does not alter GuardGeometry or FreeForecast.

Checks must compare the round-1 actions with an independent GuardGeometry,
compare every predicted action with the actual opponent, check input
immutability and legal submissions, and recompute the claimed incoming
damage with original combat. Full-game comparisons remain separate from
these component checks. This informal argument was written before the new
implementation. No machine-checked proof is claimed.
