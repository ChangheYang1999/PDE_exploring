# Timing challenge for the frozen defensive continuation

Written 2026-10-31T17:06:34.424150+00:00, before the new manifests and games.

## Statement, hypotheses and scope

The empirical claim is that the existing adaptive route counter with its frozen Fortress 38 continuation avoids defeat against all thirty BudgetTiming specifications below, in both physical assignments on the standard start. A second claim is that it never worsens a W/D/L outcome relative to the existing emergency-template continuation on the same conditions. Both claims are open until the full matrix is complete. A loss refutes the first; any strict W-to-D, W-to-L or D-to-L change refutes the second. Report the claims separately.

The fixed pairs of attack round and tier are (3,tier2), (3,tier3), (4,tier2), (4,tier3), (4,tier4), (5,tier3), (5,tier4), (6,tier4), (6,tier5) and (7,tier5). Cross each pair with budget_fraction in {0, 0.5, 1}, giving thirty targets. All other BudgetTiming parameters retain their current defaults. Its budget fraction controls the sampled defensive forecast of opposing purchases, not its own attack spending. The policy only attempts the timed purchase if the visible-map damage gain is positive; therefore an attack-round parameter is not a guarantee that a purchase happens. The actual records determine purchases and damage.

Evaluate DelegatedRouteSelector(delegate='fortress38') and DelegatedRouteSelector(delegate='template') against every target in both assignments: 120 games. Every run uses unchanged authoritative code. This is a newly expanded development grid, selected after the focused handoff results and while the full 45-target transfer is running. Some target specifications may overlap earlier development or validation conditions; no independence or held-out status is claimed. The installed best.py is not changed.

## Informal policy argument

The policies and their information-use argument are unchanged from delegated_defense/PROOF.md. They differ only after the public early-branch handoff, which cannot occur before round five. At all earlier calls they invoke exactly the same controller on identical public observations. If the target is deterministic on those observations, induction on rounds shows identical complete records through round four. The grid keeps identical visible player names for each paired comparison, so names cannot distinguish the continuations. Check the full prefix directly instead of assuming arbitrary-load determinism.

On a selected growth branch neither policy invokes the frozen defender. The same induction then predicts identical complete histories. This is a conditional reproducibility statement, not a proof of winning. Source inspection and independent public handoff reconstruction establish the allowed-information property; the original engine determines actual outcomes. BudgetTiming uses public observations and a fixed sampled forecast, never the opponent's pending action.

## Verification and dependencies

Pin the unchanged controllers, target policy, transitive sources, current configurations and this plan. Use both assignments in ten bounded twelve-game campaigns. Each campaign requires strict accounting, original-engine replay, source/data checks, fresh counter action regeneration, unchanged observations, legality checks and independent public handoff reconstruction. Compare every one of the sixty paired prefixes and every selected growth history. Retain all failed attempts and distinguish them from game outcomes. Summarize W/D/L, HP, final rounds, selected branch, handoff round, timing totals/maxima and actual timed-purchase counts. Report all thirty settings, including every loss and draw.

Dependencies are the existing original engine, BudgetTiming, DelegatedRouteSelector, the component checks in delegated_defense/verification/component.json, and the named audit scripts in the manifests. No proof-assistant verification or global strength theorem is claimed. A complete result belongs in RESULTS.md with verification receipts alongside this proof.
