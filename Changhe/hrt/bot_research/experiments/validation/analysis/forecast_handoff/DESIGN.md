# Declared development design

Six targets face four counter variants in both player assignments: 48 games.
The targets are P5TNUB, P5TNUcurrent, P5TNUF3, F34, E25RM and rush_t1.
Each counter grows behind the screened guard through a fixed round9 or
round10 deadline, then buys no further minions and uses the bounded free-cell
planner plus factories. One version defends against the next roster predicted
by an independent P5TNUB model. Its paired control uses only the visible roster.
Both versions advance this model from round1 so call timing is comparable.
The primary comparison is forecast versus visible-only at the same deadline
and target. The guard-handoff and HP-handoff counters remain separate controls;
their different planners prevent assigning every difference to forecasting.

A forecast does not inspect pending submissions. It is a private policy clone
using a copied public observation. P5TNUB contains a wall-clock cutoff, so
per-round agreement with its actual actions must be audited, not assumed.
For other targets the same P5TNUB clone is deliberately an imperfect model.
A higher HP margin does not establish repeated failed purchases. That mechanism
requires prediction, action and damage traces. All conditions are disclosed
development cases; reserved pool C remains unused.
