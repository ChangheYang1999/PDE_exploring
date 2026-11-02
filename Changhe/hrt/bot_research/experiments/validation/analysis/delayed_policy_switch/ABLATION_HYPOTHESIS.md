# Controls for delayed-switch wins

Declared before these new control games. The first campaign has completed
some early switching conditions, including switches that buy zero copies.
Those observations motivate these controls and are not held-out evidence.

For switch rounds 5, 9 and 12 and tier3, compare three versions of the same
wrapper, with both assignments against AdaptiveContinuation(attack_weight=4):

- wave: preserve the original substituted construction and tier3 purchase;
- save: preserve precisely that construction, buy no minions and keep the gold;
- prefix: submit the original E17 proposal in the switch round.

All three initialize the same fresh E20 continuation only in the following
round. In addition, play the same E20 parameters directly from round1 in both
assignments. This makes 20 new standard-start games. The wave controls are
rerun in the new wrapper so equivalence is measured as well as argued.

The save versus wave comparison changes only purchases in the specified round;
after that, both policies process their resulting actual observations. It can
change all later play. It isolates neither current-round damage from future
income nor a single later decision. Prefix versus save also changes the
switch-round factory and original minion purchases. Direct E20 changes the
entire opening and initialization time. These limitations must accompany any
causal interpretation.

The component identity follows directly from the wrapper definition. Every
mode advances the same parent once on the same input. Wave returns its actions
unchanged; save filters only buy_minion at the designated switch; prefix uses
the exact recorded pre-substitution proposal. The parent policy's state is
unchanged by these output transformations. In later rounds its E20 state is
initialized fresh and depends only on the actual observations subsequently
received. This proves same-input parent equivalence for wave, not full-game
equality across different modes. Public-history equivalence through the
unchanged prefix is exactly the argument in PROOF.md.

Hypotheses to test: some delayed wins persist with no switch-round attack;
submitting the original proposal before the fresh continuation may postpone
rejection without removing the win; direct E20 may already defeat this
observer, in which case delay is not necessary for a successful counter.
Record every declared case, including unreached switches and losses. These
are development controls, not reserved validation or a universal exploit.
