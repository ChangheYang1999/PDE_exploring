# Force the existing early branch against the public-clone family

Written 2026-10-31T17:17:26.873386+00:00, before this component check or full-game matrix.

## Statement and finite question

The first eight trace-capturing games of delegated_forecaster show a public-clone attacker taking an early HP lead against the adaptive route selector. The target selects growth, so its stronger Fortress 38 continuation is unused. Test the already implemented mode='early' with delegate='fortress38', keeping every other parameter unchanged. This intervention forces the existing round-four early package; it does not introduce a new policy algorithm. The attacker receives a matching private model with mode='early'. It therefore adapts to the changed target rather than forecasting the old target by mistake.

Use exactly the twenty timing configurations previously declared in delegated_forecaster: attack_share=1, count_cap=200, defense_first in {false,true}, and round/tier pairs (3,tier2), (3,tier3), (4,tier3), (4,tier4), (5,tier3), (5,tier4), (6,tier4), (7,tier4), (7,tier5), (8,tier5). Play both physical assignments, forty new games. Compare against the forty existing adaptive Fortress 38 conditions, including every outcome. The falsifiable repair claim is that at least one previous target loss becomes a draw or win and no condition becomes worse in target W/D/L ordering. Also report the stricter question of eliminating every target loss. Neither claim implies a universally stronger bot.

## Informal policy argument

Before round four, ProjectedLeadSelector calls its early and growth policies and verifies that their actions agree. The mode parameter is not consulted there. Hence adaptive and forced-early target actions agree on any equal first-three-round observations. Each forecaster keeps an independent model of its actual target, and the models obey the same prefix property. Conditional on deterministic private transitions, induction therefore gives equal complete histories through round three between the paired experiments. Round four can differ because mode='early' overrides the route-and-projection choice. Later delegation still requires a positive public HP lead or positive incoming damage from the visible roster, so forcing the early branch does not itself guarantee handoff.

This argument has exactly the same public-information and wall-clock qualifications as delegated_forecaster/PROOF.md. Forecasting is conditional on deterministic policy transitions; actual forecasts are checked rather than inferred. Sources remain unchanged. Every decision uses only the supplied public observation and legitimate private model state.

## Components, dependencies and verification

First run four prefixes, both assignments of (round4,tier3,defense_first=false) and (round7,tier5,defense_first=true), through round eight or termination. Check model calls once per reached round, exact target predictions, unchanged observations, legal actions and original incoming combat. Then freeze the same twenty configurations into five manifests, eight games apiece. Pin all policy and checker dependencies, the three exact layout/guard JSON inputs, component evidence, this proof and the original manifests.

Use run_data_forecasts so actual decision traces are captured. Each campaign requires strict accounting, original-engine replay, source/data checks, forecast diagnostics, fresh regeneration of both players and independent handoff reconstruction. Rehash paired adaptive controls and check equality through round three after removing only the run identifier. Report target and attacker W/D/L, HP, ending round, actual purchases, selection, handoff time, every regression and timing. This is an adversarial development ablation after observing the initial failure, not reserved final validation. No change to best.py is authorized by this experiment.
