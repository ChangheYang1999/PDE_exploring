# Adding a fixed wall plan at the defensive handoff

## Exact policy intervention

Start from the unchanged GuardedRound4Trigger policy: a round-four tier4 and corner gun, then a public HP trigger at or after round 5. On the first triggered decision, insert a wall plan before the inherited defensive plan. The plan is the fixed frozen-v7 plan_walls layout, either through stage A or through all listed wall cells, with budget bounded by currently available gold. A third mode inserts no walls and is an exact control. Only the first handoff decision attempts the walls. All later decisions use the inherited policy.

The empirical hypothesis is that lengthening the route at handoff repairs some transfer failures while retaining the two nominee wins. It is not proved by the wall construction. Walls spend gold, alter gun coverage, change the preferred route and change future income. They can make an existing defense worse.

## Legality and observation argument

Copy the observation and reconstruct the current owner state. Validate every wall proposal with the unchanged apply_action. Include only accepted proposals and update that local state. Rebuild only the copied own-player snapshot from that state, including gold, buildings, turret and wall counts and the exact current shortest-path length. Keep both HP totals, the other player's snapshot, the round and the rules unchanged. Feed this legitimate hypothetical post-wall observation to the inherited defender and prepend the accepted walls to its output.

The actual engine accepts those walls by induction on the accepted prefix. It then has exactly the owner-local state described by the hypothetical observation. The parent's returned actions are legal from that state by its previously established induction. Therefore their concatenation is legal. The inserted walls change neither HP total, so the parent's public trigger agrees with the wrapper's precheck. The wrapper sets its one-time flag after this first attempt; no later wall insertion is implied. The original observation is never modified.

No call reads a live engine instance, pending opponent action, opponent private state or unrelated file. The wall planner's static layout and imported source are part of the frozen policy. The no-wall mode immediately returns the inherited output, so its gameplay is identical to the prior fixed policy under equal observations and legitimate private state.

## Component and full-game checks

Before complete games, check the fixed corner-gun map with sufficient gold: run each wall plan through the original validator and compare the rebuilt snapshot and route against an original Engine holding the same state. Record the new route and its attainable off-route splash ceiling, without equating that ceiling with an affordable current defense. Check all declared eight-round prefixes for legal actions and unchanged observations. Then run both assignments, complete original-engine replays, source/data audits and fresh policy regeneration. Compare no-wall controls with the old complete histories.

The tested target set is P4TNUB, P5TNUBM, best_v9e, F36, F37, lead8, E25RM and E30. Use the already measured half-public-budget defender for all three wall modes. These 48 games are development evidence. No reserved scenario or pool C condition is used, and wall-clock-limited target planners retain their existing limitations.
