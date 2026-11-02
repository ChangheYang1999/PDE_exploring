# A defended round-three opening with a round-four heavy purchase

Written 2026-10-31T17:40:45.442986+00:00, before the finite search.

## Exact claim and scope

Under the bundled balanced rules, begin with an empty map and buy five factories in round one and four in round two. In round three build one of the twelve wall layouts in counters/data/maze_layouts_001.json, then one or two turrets chosen from gun1, gun2 and splash, and spend the remaining gold on factories. The finite existence claim is that at least one such legal map both stops four newly bought tier2 copies completely in round three and leaves enough gold to buy a tier4 in round four. No full-game victory or universal optimality is claimed. The opponent is allowed its standard five/four-factory opening, so its four tier2 purchases are affordable.

## Budget identity and proof

There are no friendly minions or hit bounties in the first three rounds. On the empty map the route length is 22. The first round leaves 0 + 5*15 + 22 = 97 gold. Four additional factories leave 17 + 9*15 + 22 = 174 gold at the beginning of round three. Let c be the legal construction cost, f=floor((174-c)/20) the new factory count, and L the resulting route length. Provided the game has not ended, the round-four gold is

G = 174 - c - 20f + 15(9+f) + L = 309 - c - 5f + L.

The identity follows directly from action costs followed by income settlement in engine.py. Incoming damage has no direct income effect, but terminal damage would prevent a next decision; the zero-damage condition excludes that problem for the declared four-tier2 component. The heavy purchase is affordable exactly when G >= 260. The construction is legal when the chosen cells are distinct, not endpoints, affordable, and their final blocked set retains a route. Every construction prefix removes fewer free cells, so final route existence also ensures route existence at every prefix. The script nevertheless checks the selected action lists through the original engine.

## Combat and finite verification

A gun targets one frontmost copy. Geometric exposure for one copy does not certify a multi-copy defense. Every budget-feasible candidate is therefore checked with the unchanged original simulate_map on four tier2 copies, including original spawn indexing, movement, targeting, stacking and cleanup. Enumerate every unoccupied cell for one turret and every unordered pair of cells for two turrets; for each pair enumerate all ordered type assignments. A gun3 costs more than the entire round-three cash and is excluded. The fixed wall layouts are imported from their exact JSON rather than copied into source.

Rank successful maps by most new round-three factories, then most round-four gold, then least construction cost, then deterministic layout and turret order. Recheck the first eight through an original-engine three-round fixture and all sixteen one/two/four/eight-copy components for tier1 through tier4. Preserve counts for every layout, rejected budget class and legal map. A missing witness refutes only this finite existence claim. The formula is proved above; the existence verdict needs the retained computation. No source or policy is changed by the search.

## Dependencies and remaining work

The search is experiments/validation/design_guarded_opening.py. Its receipt pins the original configuration, engine, actions, combat and pathfinding dependencies, this argument, and the wall-layout JSON. The result belongs in verification/search.json. If a witness exists, a new counter and its correctly updated public-clone opponent require separate component and full-game declarations; this component alone supplies no strength evidence.
