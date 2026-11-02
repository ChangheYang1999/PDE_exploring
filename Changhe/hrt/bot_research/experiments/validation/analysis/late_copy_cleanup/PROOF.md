# A splash-immune copy can be cleared alive

## Statement, hypotheses and notation

Use the unchanged bundled balanced rules and original Engine. Build exactly one splash turret at (1,1) on the defender map in round one, then leave that map unchanged. Let P be the resulting shortest route, L its length in steps and S the total splash damage over its attackable cells, excluding the base. The attacker buys only factories during rounds one through eight, always buying every affordable factory, then buys 250 tier1 entries in round nine. These are legal actions from the standard start.

The round-nine combat causes zero base damage, kills 249 copies and clears one living copy. The last copy has 20 initial HP, and S is at least 20, but the copy does not die during that combat. This refutes the literal assertion that every copy whose HP is at most S is killed. It does not refute the zero-base-damage consequence.

## Complete argument

The splash does not obstruct the usual shortest route along the top row and right column. The route has L=22 steps. Its first three cells (0,0), (1,0), (2,0) are adjacent, including diagonal adjacency, to (1,1). Each contributes 10 damage, so S=30. No other attackable route cell is adjacent to this splash.

The 250 active entries have dense indices 0 through 249. Under the configured 250-tick schedule they spawn on the corresponding ticks. An entry does not move on its birth tick. On its birth tick every tier1 copy takes 10 damage at the spawn. Every entry with index at most 248 has a next tick: it moves to (1,0), takes a further 10, and is removed at zero HP. None reaches the base. Entry 249 has no next tick. It remains at the spawn with 10 HP when the loop ends and is counted as cleared, not killed. The 249 killed copies and one cleared copy exhaust the roster.

Affordability and route legality are checked by the original Engine over the full nine-round prefix. No engine or state field is modified by the check. The separate one-tick observation uses a deep copy of the already legal round-nine defender and the final legally purchased roster entry.

The appropriate general statement is: for any fixed legal pure-splash map, every copy that has enough ticks to reach the base and whose HP is at most S dies first. Copies born too late cannot arrive within the combat. Thus S at least the largest permitted minion HP implies zero base damage from every finite roster, with no requirement that every copy die.

## Dependencies and evidence

Depends on the balanced configuration, Engine action application and route selection, and the spawn, movement, damage and cleanup order in td_game/combat.py. Source hashes, all prefix records and the one-tick observation are written by verification/check.py to verification/result.json. This is a rules counterexample and a wording correction, not a bot-strength experiment.
