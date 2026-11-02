# Selected forecast-defense results

Completed 2026-10-31T20:30:33.196899+00:00. H1: **REFUTED**. H2: **CONFIRMED**.

| Round | Input | Gold spent | Incoming damage | Own:enemy HP | Planner seconds |
| --- | --- | --- | --- | --- | --- |
| 10 | original | 480 | 280 | 520:774 | 0.000002 |
| 10 | visible | 0 | 280 | 520:774 | 0.000641 |
| 10 | post_submission | 480 | 140 | 660:774 | 0.208807 |
| 11 | original | 860 | 140 | 380:774 | 0.000001 |
| 11 | visible | 680 | 140 | 380:774 | 0.213993 |
| 11 | post_submission | 870 | 140 | 380:774 | 0.404717 |

These are six fixed-state interventions, with four local planner calls and zero complete strength games. Every alternative passes original-engine replay and action legality checks. The post-submission input uses the recorded enemy actions; it is not an admissible online information source. A separate public-state forecasting policy and complete-game evaluation are required.
