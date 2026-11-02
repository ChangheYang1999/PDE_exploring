# Cross-policy transfer of the bait counter

Test every no-turret bait setting (empty, one tier1, two tier1, three tier1,
one tier2) from the first roster-bait study against frozen best_v9b, the
recommended frozen economy21 parameter set, frozen fortress33, and adaptive
catalogue continuation with attack_weight=4. Use both player assignments,
forty games in total. The falsifiable hypothesis is that the one- and two-
tier1 counters defeat all four policies. An outcome table is primary; no
pooling with previous tuning samples is intended. Fortress33 has a finite
wall-clock search limit, so its measured outcomes are conditional on this
execution. The other policies are not claimed to be globally optimal.

These are development opponents already chosen from observed weaknesses.
The comparison is not reserved validation. All actions and final outcomes
require strict accounting and original-engine replay; component prefixes
check the bait's legality and observation boundary.
