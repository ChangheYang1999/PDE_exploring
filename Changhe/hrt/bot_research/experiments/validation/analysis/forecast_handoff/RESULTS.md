# Forecast-specific handoff: development results

2026-10-31T14:37:38.515191+00:00

All48 declared games were valid and replayed on the unchanged engine.
Both assignments have identical normalized action and state histories in
all24 pairs. Each table entry is target HP : counter HP at termination;
parentheses give the final round. All cells apply to both assignments.

| Target | Forecast R9 | Visible R9 | Forecast R10 | Visible R10 |
|---|---:|---:|---:|---:|
| P5TNUB | 660:755 (50) | 660:-3131 (24) | 660:755 (50) | 660:-49 (14) |
| P5TNUcurrent | 660:755 (50) | 660:-251 (14) | 660:755 (50) | 660:-225 (14) |
| P5TNUF3 | 660:755 (50) | 660:-251 (14) | 660:755 (50) | 660:-345 (15) |
| F34 | 240:-507 (15) | 240:-27 (13) | 100:-227 (15) | 100:-357 (14) |
| E25RM | 240:-12662 (40) | 240:-38 (21) | -40:618 (10) | -40:618 (10) |
| rush_t1 | -40:650 (8) | -40:650 (8) | -40:650 (8) | -40:650 (8) |

Each of the three related attack policies wins its four visible-control
games and loses its four forecast games. F34 wins regardless of the
intervention. E25RM wins at handoff9 and loses at handoff10; rush_t1 loses
before either handoff. The six identical intervention/control histories
are E25RM at handoff10 and rush_t1 at both deadlines, in both assignments.
The aggregate24 target wins and24 losses is a count over this designed
matrix, not an estimate of a deployment win rate.

Fresh counter-policy calls have been checked on all24 histories against
P5TNUB, P5TNUcurrent and P5TNUF3. All actions reproduce exactly, all are
legal, all observations remain unchanged, and no internal proposals are
rejected. The public P5TNUB model predicts every target action on all
P5TNUB histories. Its predictions also match P5TNUcurrent throughout the
forecast-treated histories, but differ in rounds13-14 of the visible R9
control and11-14 of the visible R10 control. Against P5TNUF3, mismatches
occur in rounds11,12,13,15,18 for both forecast deadlines and in rounds13-14
or11-12 for the visible R9 or R10 controls. These mismatches are retained,
not reclassified as an exact opponent model.

The spending mechanism against P5TNUB is separately reconstructed in
analysis/forecast_spending/RESULTS.md. It spends17090 or12700 gold on
post-handoff minions without ever damaging the counter after handoff.
The counter spends4650 or4570 gold defending, respectively. Those purchases
have a defensive cost for the opponent; zero damage does not mean zero
economic effect. The visible controls instead permit lethal damage.
The comparison is between complete policies, not a causal valuation of
one isolated purchase.

The general exact-model induction and its standard-start scope are in
analysis/forecast_standard_scope/PROOF.md. The older design's blanket
clock caveat is corrected there: the P5TNUB standard branch uses no clock,
while its foreign-map delegate has a finite cutoff. Fresh-policy checking
remains distinct from replaying submitted actions on the engine.

Evidence: forecast-handoff-001.json declaration; runs/validation/
forecast-handoff-{strict,replay,summary,data,comparisons}-001.json;
forecast-handoff-{histories,current-histories,f3-histories}-001.json;
and analysis/forecast_handoff/verification/full_games.json.
Reserved pool C was not used.

At 2026-10-31T14:41:34.889801+00:00, all48 full counter-policy histories have now been checked: 1130 fresh decisions reproduce exactly, legally and without changing observations or rejecting internal proposals. The additional24 histories cover F34, E25RM and rush_t1. Their model predictions differ as expected; the differences are retained in verification/full_history_shadows.json. Separate shadow runs used 420.012552 seconds in total, not additional elapsed campaign time.
