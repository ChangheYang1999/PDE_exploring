# Strengthening the guarded opening before an early strike

## Statement and hypotheses

Fix the unchanged balanced engine and a standard-start ScreenedGuardMaze
opening with its original round4 and round6 splash guards. Fix a finite
construction list E, an extension round U=6 and a later handoff D>=10.
Until D, obtain the opening's list on a deep copy of the public observation.
In round U, preserve its construction actions first, insert E second, then
consider its remaining actions. In all rounds retain only actions accepted
sequentially by original apply_action on a private reconstruction of the
observed own state. From round D use one fresh F34 defender with attacks
disabled, applying the same acceptance filter. Assume delegated calls
terminate and return finite action lists. Then every submitted action is
legal and the external observation is unchanged. Decisions depend only on
public observations, the fixed extension and legitimate private state.

For an empty extension, the wrapper gives the ordinary GuardHandoff action
list on any common history where the delegates agree and the opening list
was legal and already placed construction before economic actions. This
is a conditional equivalence because F34 has a clock-limited planner.

A separate component assertion uses a funded fixture whose only buildings
are the two original splashes. If E is accepted completely and original
combat records zero arrivals for a stated active roster R, this fixture
defends R. Neither affordability at round6 nor defense of any other roster
is implied. If its checked pure-splash exposure is S>=180, the earlier
pure-splash theorem additionally excludes every tier1-tier3 arrival on
that unchanged map. Additional construction can change the route, so later
maps require separate checks.

## Proof

Each delegate receives a copy and no other live game object. The extension
round and fixed construction read no pending opponent submission. Rebuilding
the private state from the public snapshot and then applying accepted
actions gives, by induction on the finite proposal list, exactly the state
that the retained prefix will have when submitted. A rejected action changes
neither the private state nor the retained prefix. Thus every retained
action is accepted from its actual predecessor state. The observation itself
is never passed to mutating code, proving the boundary and legality claims.

For E empty, construction-first order agrees with the already ordered parent
list in round6; other opening rounds and defender rounds use the same
lists. Under the stated acceptance and delegate-equality hypotheses the
filter removes nothing and the full action lists agree by induction.

For the fixture, the actual accepted constructions, actual roster and
original combat are precisely the objects in the asserted check. Zero
arrivals therefore gives zero base damage on that fixture. For the stronger
S>=180 special case, each tier1-tier3 copy that could reach the base traverses
every attack cell before arriving and receives at least its180-or-less HP
in splash damage. It cannot arrive alive. No untested budget or future
map property is used.

## Dependencies and empirical scope

Dependencies are original action rejection, pathfinding and combat semantics;
the public observation contract; ScreenedGuardMaze; F34; and the pure-splash
threshold proof. Exact proposed constructions and component outcomes are
kept in JSON and verified before policy experiments. JSON import alone is
not proof. No proof assistant or numerical-proof library is used here.

Hypothesis: early guard extensions answer the new v29 strike-before-insurance
rule without preventing the grower's round7 tier5 attack. The target policy's
new early attack is being tested by the lead; this experiment changes the
opponent's defense instead. Outcomes are development measurements, not a
reserved validation or proof of a winning counter. Empty extensions are
controls; all selected extensions and targets must be declared before games.
