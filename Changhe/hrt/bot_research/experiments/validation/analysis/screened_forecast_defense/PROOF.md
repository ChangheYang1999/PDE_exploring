# Forecast defense at two selected loss states

## Exact question

The guarded screened-roster counter loses 380:774 to the fixed AS1C variant in screened-guard-transfer-00-001, case0000. Its first damage arrives in round10: two new tier5 entries deal280. One further tier5 deals140 in round11. These states are selected after observing that loss. This is a local diagnosis, not held-out evidence or a new complete-policy comparison.

At each of the two original pre-action states, fix AS1C's actual submitted actions. Compare exactly three own submissions: the original actions; the frozen v17 free planner with the full available gold, partial="best", max_steps=30 and only the currently visible active enemy roster; and the same planner with the active roster after the fixed enemy submission. No factories or attacks are appended to either alternative. All values and outcomes are checked with the unchanged Engine.

H1: the full-roster alternative strictly reduces incoming damage in both selected states. H2: at round10 the full-roster alternative strictly reduces incoming damage relative to the visible-roster alternative. Both are OPEN before execution. No global optimality, affordability of future defenses, exact opponent prediction or eventual win follows from either hypothesis.

## Argument and verification

Replaying the recorded legal actions through round r-1 reconstructs the selected state exactly. Apply the fixed enemy actions to a private PlayerState to obtain the post-submission active roster used only in the forecast alternative. This diagnosis may inspect a recorded submission because it is not a playing policy. Any later playing policy must predict it from public information and legitimate private state.

A fresh copy of the reconstructed Engine applies each own alternative together with the same enemy submission. Every action must be accepted. The Engine determines the route, spawn schedule, gun targeting, splash damage and arrivals. Replaying every retained alternative history from a new Engine must reproduce all records. This establishes each reported local outcome under the pinned rules. It does not validate the planner on all inputs. The three calls share their pre-action state, and their difference isolates the fixed planning input and spending choices at that state.

Pin the original result and replay, this protocol, checker, free-planner source closure and bundled configuration before calls. Retain every alternative action list, resulting HP, combat totals, available and spent gold, decision duration and complete component replay. No final candidate or reserved D input is modified or called.
