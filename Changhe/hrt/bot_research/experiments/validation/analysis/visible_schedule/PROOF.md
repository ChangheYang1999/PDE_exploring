# Removing an unused opponent forecast

## Statement, hypotheses and notation

Fix the bundled deterministic engine, initial state, and a deterministic opposing policy with the same initial private state in two matches. Let F be PublicSchedule and V be GuardedSchedule with the same fixed purchase schedule, count cap, saturation round, factory cap, and defense-first flag. Their shared defensive routines are the unchanged frozen economy-v2 routines.

For a public observation o at round r, let T_F(o) be the ordered active opponent roster obtained after F's public model predicts and applies the opponent's actions. Let T_V(o) be V's declared initial roster if r=1, and the ordered active opponent roster already visible in o otherwise.

Suppose, at every observation reached by the F match, T_F(o)=T_V(o). Suppose also that each invoked routine terminates. Then the V match has exactly the same actions, public states and outcome as the F match, up to irrelevant private diagnostic traces. V does not need to load or evaluate an opponent policy.

## Proof

Initially the observations agree. Assume they agree at the beginning of round r. Both policies construct the same own building list and read the same gold and rules. By hypothesis their ordered defensive threat lists agree. If defense comes first, both call the same function on the same inputs and obtain the same actions, buildings and remaining gold. Both then traverse the same declared schedule in the same order and apply the same affordability and count caps, hence buy the same minion sequence. If defense comes second, the same reasoning applies to that call instead. Their saturation and factory-purchase steps also have identical inputs and rules. The two action lists therefore agree.

The opposing policy has seen the same history and has the same private state, so its next action list agrees as well. Determinism of the engine gives the same next public state. Induction proves equality through termination, including the result.

## Scope and limitations

The roster-equality hypothesis is essential. It holds when the initial prior matches the forecast roster and later predicted opponent actions never add a currently active minion. Walls, turrets and factories alone do not change the roster used by these particular defensive routines. It can also hold when other actions occur but happen to leave the active roster identical.

This result does not prove equality against an opponent that buys new units after round one, nor does it prove that a one-round defense delay is safe. It does not establish strategic strength. It is a conditional equivalence for a restricted controller: PublicSchedule uses the predicted opponent's actions only to form its defensive threat list, while its own purchase schedule is fixed.

Dependencies are the two policy sources, frozen economy-v2 defense/threat helpers, and the unchanged deterministic game engine. Verification evidence is listed under verification/. No proof-assistant formalization is claimed.
