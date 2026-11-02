# Replacing the defensive continuation after the early strike

Written 2026-10-31T16:51:09.272721+00:00, before implementation and experiments.

## Exact policy and hypotheses

Keep the EmergencyRouteSelector opening, its public round-four route/HP predicate and its growth branch. If the early branch is selected, hand control to a fresh frozen teammate defender when its current trigger would begin defense: an existing trigger, a positive own HP lead from round five, or positive simulated incoming damage from the visible current roster from round five. Test the recommended frozen econ20 and fortress38 defenders separately. A template mode retains the original emergency continuation as the control.

The hypothesis is that an improved defensive continuation can preserve the baseline and tier1-flood wins while repairing the delayed tier5 route-builder failure. This is an empirical question. Starting a frozen defender on a reached map may be substantially different from using it from round one. All losses, illegal actions and computation failures must be retained, and no component success establishes a full-game win.

## Informal policy argument

The wrapper makes no change before round five. It delegates exactly the same first four calls to the existing selector. The delegate is constructed at initialization but receives no observations or decisions before its actual handoff, so it cannot affect the common opening. It begins with legitimate empty persistent state, like a policy first activated on a public continuation. Every later call uses the current public observation and its own accumulated state. The old and new targets have no access to pending actions.

The trigger is a function of public HP, round and an original-combat projection on copies of the public map and roster. It does not claim to infer future purchases. Once delegation starts it is irreversible. In template mode every call is delegated to the original EmergencyRouteSelector; therefore exact complete-trajectory equality with that control is expected under reproducible shared planning. In a selected growth branch, the new delegates are never used. These observations establish prefix and information-use properties, not improved game strength.

## Component and full-game verification

First reconstruct the reached round-five states against the common-prefix baseline, common-prefix tier1 flood and lead_opening/growth6/tier5. Compare all first-four-round actions with their recorded originals, check that observations are unchanged, check every proposed action against the original action interpreter, and resolve that round against the target's recorded simultaneous action. Retain costs, incoming/outgoing damage, maps and HP.

Only after the component checks should a full matrix be declared. Each full game requires an explicit source-pinned manifest, both assignments, strict accounting, original-engine replay, data checks, fresh regeneration of the new policy and disabled-control comparison. The later expanded transfer set, if any, must be declared separately. No held-out claim or change to best_v9e follows from this development experiment.
