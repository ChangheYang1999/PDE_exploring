# A failed attack can permanently select the conservative attack rule

## Statement and hypotheses

Fix the exact `experiments/lead/v24.py` program on a standard start, with
attack_mode="adaptive", fail_limit=1, attack_from=6 and immune_attack=true.
Assume the foreign-policy branch never activates. Its private integer `failed`
starts at zero. A pending attack stores its round, the opponent's previous HP,
and the predicted damage. If that attack's measured damage in the following
observation is less than half its prediction, `failed` increases by one.

After the first such failure, every subsequent normal attack decision for
which the post-construction own map has splash exposure S below 1500 uses
"robust" mode. This remains true regardless of how many rounds have elapsed,
provided these hypotheses continue to hold. If each of the top two current-map
attack candidates has response-adjusted gain below the configured threshold,
no attack is bought in that decision. This is a program property, not a claim
that the conservative response model predicts the actual opponent.

## Argument

The constructor is the only assignment setting `failed` to zero. The normal
decision function can increment it, but never decrements or resets it. Thus it
remains at least one after the stipulated event. Clearing `pending` does not
clear `failed`.

The normal attack call uses an explicit "current" override exactly when
`immune_attack` is true and the post-construction splash total reaches the
largest configured minion HP, here 1500. Otherwise it supplies no override.
The adaptive mode then chooses "robust" because failed >= fail_limit. The
rounds in question are after attack_from, so the earlier catch-up branch does
not apply. Under robust mode the program evaluates only its top two
current-map candidates after a hypothetical defender response, retains those
whose response-adjusted total damage divided by the new purchase cost is
at least min_leak_per_gold, and returns
an empty purchase list when none survive. These code branches give each part
of the statement directly; induction preserves the lower bound on `failed`.

## Empirical question and method

The P5 baseline on the standard start against the no-bait empty grower with
growth_rounds=6 and splash guards in rounds4 and6 loses 520:755 at round50.
The first guard has S=50; the second raises it to80. P5 buys two tier2 in
round6, which the second guard can stop, and buys no later attacker. The
hypothesis is that this failed prediction activates the rule above while the
own map stays below the immunity threshold.

Reconstruct both baseline games on the unchanged engine. Feed fresh P5
instances exactly those public observations, requiring all submitted actions
and engine records to match. Record the legitimate private pending/failure
state for diagnosis only. Independently query the current-map attack choice
with the same pre-factory, post-defense budget; these extra queries never
alter actual play. Compare their proposed purchases with the actual robust
choices.

Then run full games for P5, P5 with fortress_guns=false, P5 with fail_limit=2,
and P5 with attack_mode="current" against this guard, the fixed heavy-drip
schedule, and the established round8 tier5 forecaster. Change no engine code
and no other policy parameter. The ablation tests the full-game effect; the
program property alone cannot imply a win or establish that a repair is
robust against other opponents. These conditions are development data.

## Dependencies and scope

The exact source, configuration, replay and checker hashes are recorded in
verification/. Earlier proof50 supplies the pure-splash arrival condition;
proof54 supplies passive-threshold equivalence on this no-early-minion
trajectory. No formal proof assistant is used. There is no statement about
other source versions, an optimal attacker, or a globally strongest bot.

## Source-wording correction (2026-10-31T13:17:39Z)

The robust branch uses total post-response roster damage, not an incremental
comparison with the no-purchase roster. The current-map branch does subtract
its baseline. The earlier wording called both incremental; the program-property
conclusion and the recorded diagnostic are unchanged. The initial proof and
receipt are preserved under verification/.
