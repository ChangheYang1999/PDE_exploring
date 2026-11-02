# A guarded opening followed by an observation-based defender

## Exact statement and hypotheses

Fix the balanced bundled rules and an integer H from10 through50. Before
round H, use ScreenedGuardMaze with its round9 gun extension. From round H,
use a fresh frozen v34 fortress controller with attack=none and round1_poke=0.
It is initialized once and receives exactly the observations for rounds H
onward. Apply every proposed action in order to a private reconstruction
of the observed own state; retain an action exactly when apply_action
accepts it, otherwise omit it. Assume the delegated controllers terminate,
return action lists and do not mutate the observations.

The filtered post-handoff list contains only sequentially legal actions
from the observed state. The wrapper uses no hidden current submission and
its pre-handoff actions coincide with the fixed opening at every identical
observation. This statement does not assert that the fresh defender
reconstructs its hypothetical private history from rounds before H.

## Argument

Before H the branch returns the opening controller's action list directly.
At H the already-created defender is called for the first time, and later
calls use that same instance. Its input is precisely the public observation;
its legitimate private state consists only of its initialization and these
calls. The fresh defender intentionally treats existing unrequested own
construction as an input map for its map-replanning branch.

For legality, use induction over proposed actions. The private state is
initially a reconstruction of the observed own state. An accepted action
updates it exactly as in the original action function and is appended to
the output. A rejected action is omitted. Under the original action
function's rejection semantics, no accepted-state transition is lost. Thus
the retained sequence has the same sequential acceptance and final state
when submitted. All effects are on the acting player's own state.

## Empirical hypothesis and limitations

The round9 gun extension defeats the two-failure rule but a response-search
repair may eventually buy tier5. A late transition to a defender might
preserve the earlier HP lead and stop that eventual purchase. Test H=12,16,
19,22 against P5TF, current mode and the untruncated-response variant, both
assignments. This is a new development family, selected after the guard
findings; no independent-validation claim is made.

A handoff can fail by spending too late, choosing a poor completion map,
or overestimating the opposing threat. The legality filter does not fix
those strategic errors. Full-game outcomes, controller input immutability
and internal rejected-proposal counts must be checked separately. No
proof-assistant formalization or guarantee of a win is claimed.
