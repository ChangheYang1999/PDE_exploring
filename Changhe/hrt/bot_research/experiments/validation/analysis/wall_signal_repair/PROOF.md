# Repairing the wall-signal attack's defensive continuation

Declared 2026-10-31T19:38:19.239310+00:00, before implementation or new-policy calls.

## Exact policy and hypotheses

Keep K20's twenty-wall first move, private H model, round-three tier2 purchase and all other parameters. From round four on, after calculating its normal action list, inspect the private model's predicted residual base damage. If it is positive, call the frozen economy-v17 free planner on the original public own map, full current gold and predicted active enemy roster, with partial=best and max_steps=30. Adopt the free construction plan only when every action is legal and its simulated residual damage is strictly below the original plan's. Spend the remainder on factories with the same per-round cap and stopping round as K20. Otherwise retain the original action list. Advance the private H model exactly once per decision. This defines a fixed policy, L.

H1: L wins against J in both assignments, with the same normalized histories as L against fixed H. H2: L has a strictly better W/D/L result against J than against fixed I. Test J,H,I in both assignments, six new standard-start games. Reuse the six completed K20 games as explicitly selected old controls. The hypotheses are distinct: fixing defense could beat both responses, which would confirm H1 but not H2.

This revision is selected after three one-round feasibility witnesses found an 880-gold free plan that prevents the original 280 damage at round seven. These witnesses do not establish a complete-game improvement. The delayed heavier-attack grid is still undergoing its final action checks at declaration time; the revision does not change its sources or outcomes.

## Conditional argument

Until a free plan is selected, L submits exactly K20's actions, uses the same public observations and advances the same private model once. Under deterministic decisions, induction yields equal histories up to the first changed action. A free-plan selection is based solely on a copied public observation and the private model, never an opponent object or pending action. Its legality is checked against the actual own budget. The strict local damage comparison is not a proof of better future HP or a win: spending, path, future roster order and future opponent behavior may change.

The first move still exposes twenty walls and no roster at round two, so J selects H. Under the stated shared-prefix and determinism hypotheses, L-J and L-H have equal complete histories. Check this equality rather than assuming planner timing is invariant. The L-I control distinguishes beating the selected response from a response-selection cost. A win alone does not establish H2.

## Verification and scope

Check all six prefixes through round eight before full games. Require legal submissions, unchanged observations, exact private H predictions against H/J, and recorded repair decisions. Then require complete case accounting, original-engine replay, frozen source/data checks, fresh regeneration of both external policies and separate regeneration of L's forecast/repair trace. Compare each old control's history through the first actual changed action, and keep every outcome. No new decision may be chosen from pool D or installed best.py. This is selected development, not held-out validation or an unrestricted equilibrium claim.

## Pre-call implementation clarification, 2026-10-31T19:40:52.490897+00:00

The inherited trace records damage before its optional saturation construction from round twenty. Before freezing or calling L, the comparison was refined to recompute the original full action list's residual damage, including saturation. From round four this recomputed value is also written to L's trace. The free plan must strictly reduce that full-plan value. This preserves the first move and attack and avoids claiming an improvement from comparison with an incomplete original plan. No L policy call or game preceded this clarification.
