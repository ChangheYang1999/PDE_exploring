# A prescribed opening before adaptive catalogue continuation

## Exact statement and hypotheses

Fix the bundled rules and a standard initial game. Let P be the existing
AdaptiveContinuation policy with fixed parameters. Its catalogue contains
independent clones of three fixed public deterministic policies, with no
randomness, wall-clock choices or hidden inputs. Assume each policy call
completes, each clone receives a copied actual public observation for its
player, and all submitted actions are legal.

Let G call P exactly once at every reached round on the actual observation.
In round 1 only, G discards P's proposed actions and instead returns a fixed
legal GuardGeometry opening. At later rounds G returns P's actions without
change. G changes only explanatory trace fields for the discarded opening;
it does not change P's clone states, pending signatures, active catalogue,
round counter or continuation state.

Then a true catalogue member is retained and its predictions remain exact
through every reached round. Also, the actions returned by G after round 1
equal an independent copy of P fed the same sequence of actual observations,
including round 1. If all catalogue members are rejected, the continuation
is exactly P's fresh economy20 policy on subsequent actual observations.
These statements make no prediction about winning or surviving.

## Proof

Before round 1 every catalogue clone has the same initial private state as
its corresponding real policy. Each clone and the real opponent receive
the same public observation. For a true deterministic member, actions and
next private states agree. G changes its own submitted opening only after
P has advanced the clones. This does not affect the opponent's current
observation or the correctness of that prediction.

Suppose the true clone and real opponent agree before a reached later
round. P uses the actual settled observation to compare the preceding
purchase signature. The true predicted signature equals the settled one,
so the true member is not eliminated. Its next call again has equal input
and private state, producing equal actions and next state. Induction proves
retention and exact prediction despite the changed own opening.

For the second statement, initialize the independent P with the same
parameters. In round 1 both P objects receive the same actual observation
and produce equal private state. G edits only trace fields that no future
policy decision reads. In each later round their actual observations are
again identical. Induction gives identical private updates and proposed
actions. G returns precisely that proposal after round 1. This comparison
feeds the actual G-game observations to the independent P; it does not
claim that an independently played P-game has the same observations.

Complete rejection triggers the unchanged continuation branch. Both copies
initialize economy20 at the same rejection round and call it once on each
same subsequent observation. Their continuation outputs therefore agree.
A genuine deterministic catalogue member cannot trigger this branch under
the hypotheses. Outside opponents can; no prediction guarantee applies to
them after rejection.

## Scope and dependencies

The opening is one gun1 at (10,1), a declared small tier1 roster, and factories
from the remaining affordable gold. Its legality is checked with original
actions. The corner_guard proof covers defense against the three-tier1
opening only. No arbitrary-roster opening safety is assumed.

Dependencies are stateful_catalogue, adaptive_continuation and guarded_forecast.
The attack score remains a bounded heuristic. A new opening changes later
observations and can improve or worsen both known-member and outside games.
This proof was written before implementing the wrapper. Verification must
check opening equality, actual-observation parent equality, clone predictions,
input immutability and legality. Full-game performance requires separate
unchanged-engine matches. No proof-assistant formalization is claimed.
