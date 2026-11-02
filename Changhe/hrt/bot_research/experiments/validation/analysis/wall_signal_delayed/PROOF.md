# Heavier timing attacks behind the twenty-wall signal

Declared 2026-10-31T19:28:27.121217+00:00, before any call to the new delayed policy.

## Exact claim and hypotheses

Fix H, I and J exactly as in shared_prefix_response/PROOF.md. Fix the twenty-wall first move and private H model of wall_signal_response/PROOF.md. Define four attacker policies by replacing only the purchase-round and purchase-tier fields of that twenty-wall attacker with (3,tier3), (4,tier3), (4,tier4) and (5,tier4). All other parameters, the wall sequence, first factory purchases and private model remain unchanged.

H1: at least one setting wins against J in both physical assignments, and its entire normalized game history equals the same attacker against H. H2: at least one such winning setting has a strictly better win/draw/loss result against J than the same attacker against I. Test all four policies against J,H,I in both assignments from the standard start, 24 games total. A complete absence of the required setting refutes the corresponding hypothesis. A missing or invalid condition leaves the question OPEN.

This is a selected follow-up. The earlier matching-H attacks without walls won all 24 tested games. The nineteen-wall tier2 attack has now lost all six of its games; the twenty-wall tier2 campaign is still running and its result records have not been examined when this declaration is written. The new grid was chosen to test whether more time or a stronger tier can overcome the wall opening's changed cost and reached history. It is not a held-out sample and the earlier outcomes are not counted as new evidence.

## Conditional argument and dependencies

The inherited first move calls the original timing procedure, which advances its own H model exactly once on the first public observation, then legally substitutes twenty declared walls and all affordable factories. Altering a purchase round no earlier than three does not change that first move. The shared J prefix has already processed both H and I. At round two the attacker exposes twenty walls and no roster, so J selects H and keeps it. Subject to the already stated determinism and common-prefix hypotheses, induction on rounds gives the same states and actions as a standalone H game. The new prefix and full-history checks establish this equality on each observed run, including the wall-clock-bounded dependencies.

No argument here proves a win. A correct private prediction only supplies the opponent's current actions; the one-shot attack rule can still choose an inadequate purchase or lose later. The fixed I control keeps the same attacker while changing the selected response, which is needed to identify a response-selection cost. Neither adjacent wall counts nor increased damage alone justify that causal conclusion.

## Verification and scope

Check every setting, target and assignment through eight rounds before full matches, using the original action checker and engine, unchanged observations, the twenty-wall signal and exact H-model predictions for H and J. Require strict condition accounting, original-engine replay, archived source/data identity, fresh regeneration of both external action streams, and separate attacker/forecast regeneration for every complete game. Preserve actual purchase counts, HP, ending rounds, rejected actions, errors, forecast mismatches and timings. Report every setting and both assignments, including losses.

The exact rational certificates for earlier fixed finite tables do not include these four new policies. This experiment neither invalidates those restricted statements nor extends them to arbitrary opponents. No pool D data or installed best.py is used.
