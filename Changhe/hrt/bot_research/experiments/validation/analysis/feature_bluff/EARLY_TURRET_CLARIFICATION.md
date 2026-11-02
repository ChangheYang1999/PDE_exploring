# Scope correction for the early turret hypothesis

Recorded 2026-10-31T13:36Z before completion of the 144-game campaign.
The pinned EARLY_TURRET_HYPOTHESIS.md refers to PROOF.md for the controller's
legality argument. That reference is too broad: PROOF.md establishes the
zero-combat-effect property only for a lone gun1 at (0,11). It does not
establish that property for either (10,1) or (0,2), which are the cells in
this new experiment. No zero-effect property is assumed for them.

The relevant general legality argument is instead direct. FeatureBluff
reconstructs its own observed state, and applies each proposed action with
the unchanged apply_action before retaining it. Begin with that exact own
state. Induct over proposals: an accepted action updates the reconstructed
state and is retained; a rejected action is omitted and leaves the relevant
state unchanged under the engine's rejection semantics. Thus the retained
list is sequentially legal from the observed own state. Actions concern
only this player's state, so interleaving an opponent's actions does not
alter their acceptance. The experiment independently checks actual action
acceptance and original-engine replay. This argument asserts legality,
not strategic quality or a guarantee of a win.
