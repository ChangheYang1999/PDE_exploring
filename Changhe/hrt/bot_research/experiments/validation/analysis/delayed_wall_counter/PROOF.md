# Delaying a wall signal by one round

Written 2026-10-31T21:08:37.825413+00:00, before creation or execution of the proposed delayed-wall policy P.

## Exact definition and scope

Let G be `EarlyWallGuard(witness='guard00')`. Define P by the same class behavior and the same imported exact JSON witness, with only its instance-local `wall_round` changed from1 to2 before its first call. P still builds the same turret at round3, buys at most one tier4 at round4 if affordable, buys factories from remaining opening gold, and delegates to the same frozen Fortress38 from round5. It neither reads opponent identity nor predicts or reads pending actions. The change does not edit G or the shared JSON.

Use the bundled standard start, with100gold,800HP, no roster/buildings/factories, wall cost1 and factory cost20. Calls begin at round1, use consecutive rounds and one consistent player. Rules and imports are fixed. General starts and arbitrary altered rules are outside the following branch claim.

## Proved public-branch claim

Against P, O (`WallPrefixSelector`) selects L at round2. Against G, O selects G at round2. This is a deterministic statement about the first submitted actions and completed public snapshots, not a victory theorem.

Proof. In P's round1 call, the wall-round equality fails because1 differs from2. The turret and minion conditions also fail because their rounds are3 and4. With100gold and no prior purchase, the factory loop buys exactly five factories and has0gold remaining. Factories are counted separately and do not enter either the building list or roster. Combat and round settlement do not create buildings or roster entries. Thus at round2 O sees both lists empty and takes its L branch. Conversely, G places the guard00 witness's20walls at round1 and then four factories. Legality follows from the explicit surviving path in `analysis/wall_prefix_selector/PROOF.md`, and the100gold covers all purchases. The completed round1 opponent building list is nonempty, so O takes G. O selects only once. P's round2 actions are hidden when O selects; those actions cannot retroactively change the branch. This proves both claims.

Delaying walls also changes path income and factory timing. P therefore need not reach the same later gold, map, actions or outcome as G. No behavioral-equivalence claim is made between P and G. Subject to the environmental coupling hypotheses of the O proof, O against P behaves as standalone L against P; retained games will test this full-history transfer in the actual executions.

## Prospective empirical checks

Run P against O, L, G, B (frozen best_v9e) and N (best_v9e with attack_share1 and catch_up_share0.5), in both physical assignments:10new standard games. Exact specs and all source/data inputs will be pinned before any P decision. The O result from protocol153 is not needed to choose this counter: its public rule and the old G/L payoff already motivate delaying the distinguishing action.

H1: P wins against O in both assignments. This is a falsifiable conjecture, motivated by G's earlier wins against L, not a logical consequence of the branch proof.

H2: O selects L against P and the complete normalized P/O game history equals the corresponding P/L history, separately in each assignment. This is a falsifiable execution-level test of the conditional transfer. A difference must be retained and diagnosed; deadline-sensitive equality cannot be assumed.

H3: The two assignments have the same candidate outcome and normalized full history for each of the five opponents. No outcome prediction is made for P against G, B or N. Those three measure the cost of the signal change.

Require strict source/action accounting, full original-engine replay, explicit terminal boundaries and fresh regeneration of both external policies. Retain all failures, branch traces, round1 and round2 actions, early economy and runtime. Compare O's older games against G for context, without counting reused games as new. No final-bot change or reserved D condition is involved. These are selected development conditions, not independent random samples or a universal-strength test.

## Dependencies and present status

The source proof uses `early_wall_guard.py`, its exact `early_wall_guard_001.json` witness, `wall_prefix_selector.py`, and the unchanged action and engine settlement rules. Victory and full-history hypotheses are OPEN before execution. The first-move public-branch claim is proved under the stated standard-start hypotheses. This topic has no formal-assistant source; verification receipts will record the executable checks beside this proof.
