# Full-game tests of the early-wall guard

Declared 2026-10-31T17:50:21.964673+00:00, before the policy component and full-game tests.

## Policy and hypotheses

For each of the eight witnesses exported by the earlier-wall component, instantiate a separate fixed policy. Build its complete walls in the specified first or second round, its selected turret in round three, and one tier4 in round four. In each of these rounds spend the remaining cash on factories. From round five use a fresh, persistent frozen Fortress38 policy. Construction proposals are checked on a private state through original apply_action; only accepted actions are submitted, and filtered proposals are retained in the policy trace. No engine object or hidden opponent action is available to the policy. All tables are loaded from the exact registered JSON.

The first full-game hypothesis is that guard00 defeats its correctly updated round-three/tier2 public-clone adversary in both assignments. The second is that at least one fixed witness avoids loss on all four teammate targets: frozen best_v9e, frozen Fortress41, fixed V33C and P5TNUBM, in both assignments. These are separate claims. Neither says that a single policy is universally optimal. All eight policies are tested, including unfavorable outcomes, and selection after seeing results is labeled development selection.

## Component argument and limits

The preceding proved budget identity and original-combat enumeration establish that each witness can legally build its guard, stop four new tier2 copies in round three and still buy one tier4 at decision four, under the stated passive first-two-round opening. Earlier attacks may reduce HP; they do not change the incoming-damage-independent cash identity. Friendly attacks start only in round four, so there is no earlier friendly hit bounty. A changed defensive map can change a public-clone adversary's chosen package. Its full-game result is therefore a separate experiment, not a corollary of the component.

The continuation receives only the real public observation at round five. It has no fabricated private prefix. That cold start is part of the fixed policy and must be measured rather than assumed equivalent to a Fortress38 game from round one.

## Verification and finite matrix

Before the full matrix, test eight witnesses in both assignments through round five against a matching public clone with attack_round=3, tier=tier2, defense_first=false, attack_share=1 and count_cap=200. Check independent target actions against its private predicted actions, input immutability, legal submissions and original incoming combat. A failed component is a recorded failure and blocks the dependent full matrix until explained.

Then run 64 teammate games: eight witnesses times four fixed targets times two assignments. Run sixteen separate clone games, with each clone's model_parameters containing the exact witness ID; hold all other clone settings fixed. Preserve all80games. Regenerate both fixed policies on every complete public history, replay the original engine, verify source/data archives and strict condition accounting. Clone runs additionally check every predicted action and forecast residual against actual actions and original combat. Neither seat exchange nor repeated deterministic trajectories count as independent samples. Report HP, W/D/L, end round, rejected actions, errors and measured decision time.
