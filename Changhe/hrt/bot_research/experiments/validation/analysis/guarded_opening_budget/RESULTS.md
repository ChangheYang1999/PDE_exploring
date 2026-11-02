# Early defense and a round-four heavy purchase

Checked 2026-10-31T17:47:26.500425+00:00.

The finite existence claim is REFUTED. The search found 0 maps that stop the four-tier2 component and retain at least 260 gold at the next decision. This is a component result. No full-game outcome is inferred.

The unchanged combat code checked every one of the 743 budget-feasible maps. The enumeration crossed all twelve registered wall layouts with one or two distinct turret cells and every assignment of gun1, gun2 or splash. Walls and occupied turret cells retain a legal route.

| Wall layout | Legal cell/type assignments | Budget-feasible maps | Zero-damage maps |
|---|---:|---:|---:|
| empty | 90507 | 142 | 0 |
| lead_opening | 46575 | 102 | 0 |
| cash_rank_1 | 7404 | 82 | 0 |
| cash_rank_2 | 6351 | 38 | 0 |
| cash_rank_3 | 8919 | 46 | 0 |
| cash_rank_4 | 8130 | 49 | 0 |
| cash_rank_5 | 9435 | 46 | 0 |
| cash_rank_6 | 8628 | 44 | 0 |
| cash_rank_7 | 7857 | 42 | 0 |
| cash_rank_8 | 8175 | 43 | 0 |
| cash_rank_9 | 11130 | 50 | 0 |
| cash_rank_10 | 15531 | 59 | 0 |

No witness survived: all budget-feasible maps leaked. Consequently no selected engine fixture or additional roster component was run. This refutes the finite existence claim while leaving earlier construction schedules open.

| Witness | Layout | Turrets | Cost | New factories | Next gold | Route length |
|---|---|---|---:|---:|---:|---:|

The search took 5.496060 seconds at low priority on one assigned core of the shared machine. The source receipt pins the actual code and exact input JSON. All sixteen extra component results per selected witness are retained, including damage against larger or heavier rosters.

The budget formula in PROOF.md applies only to the specified first-two-round factory opening, no own minions or hit bounties, and a surviving player. Four-copy defense is not an arbitrary-roster guarantee. A gun still chooses a single target; every multi-copy claim here comes from original combat execution. An eventual counter using this map will require separate full-game evaluation with the public attacker model updated to that counter.

Reproduce from the project root with the existing Python environment, disabled bytecode, research temporary directory, one numerical thread, assigned affinity and low priority: run module bot_research.experiments.validation.design_guarded_opening with --output set to a new JSON path, then compare its complete counts and selected witnesses. The actual command is in runs/validation/guarded-opening-search-001.log.
