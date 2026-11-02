# Threshold and relevance interventions

Declared UTC: 2026-10-31T12:58:57.110193+00:00

After observing that P5 loses to the growth5 three-tier1 and four-tier1
round2 bait settings, test the same18 declared growth/cost combinations
against P5 with passive_bait=45, P5 with passive_bait=60, and the lead's
P5T proposal (poke_reactive="turret_only"). Both assignments give108 games.
The default P5 results from passive-cost-grid are the matched controls.
The exact intervention is one parameter per variant. The hypothesis is that
raising the exemption to include the bait, or ignoring roster-only relevance,
repairs the new losses. It may introduce other failures, and every condition
is retained. This is an outcome-informed development ablation, not a reserved
validation set. No reserve-C definition or result enters this selection.

The45 threshold includes three tier1 but excludes four; the60 threshold
includes both. Other costs provide controls above and below these boundaries.
Compare complete histories, record first changed actions and replay all games
on the unchanged engine. Do not infer an isolated causal effect from aggregate
win counts alone.
