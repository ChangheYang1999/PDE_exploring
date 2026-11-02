# Independent report review at 2026-10-31T20:00:08.415327+00:00

Reviewed snapshot: report-shift4-source.md, SHA256 25c4048b1b03f7d0e6ed5e1c4fea2ebffe8c716a4abaa627db7ff68450d72754. The live report may have changed since this snapshot. These are report corrections, with no recommendation to change the selected policy. Pool D remains unplayed.

## Findings for the report owner

1. **Keep the H13 hypothesis distinct from the R13 acceptance rule** (section 5.14, lines 1386-1421). H13 says af2g keeps the early strikes best_v9e holds and most of best_v9f's grower gain. The results paragraph says both of those things happened, then labels H13 refuted because a guarded-maze condition regressed. The regression and the 5.81-second call reject the stronger R13 conjunction; they do not contradict the narrower H13 sentence. Suggested conclusion: "The early-strike prediction holds on the tested strike pools and most of the measured grower gain remains, but af2g fails R13: it loses one guarded-maze setting that best_v9e wins, in both seats, and its largest observed call exceeds three seconds." The scope must remain the named pools. The 19:04Z team note already knew the GROWERS result before the other gate games, so that grower count is prior evidence, not a prospective prediction.

2. **Name the sampled threat set in the summary** (line 29). Replace "against the rosters the opponent could buy this round" with "against sampled rosters the opponent could buy this round." The frozen v7 planner's affordable_bundles constructs at most nine lists and takes a prefix of that list. At the bundled initial 100 gold it returns four lists, while complete enumeration gives 27 affordable ordered rosters including the empty roster. This is an exact finite check of sampling, not evidence that an omitted roster defeats the returned plan. The installed bot's docstring already calls these sampled rosters.

3. **Correct the round-one turret in section 5.15** (line 1488). The V29 + r1_guard=60 variant builds a gun2 at (8,1), costing 80, plus two walls and one tier1. It builds no splash and no factory in round one. This is directly present in both kept vbest2 logs, with final score 800:795. The report copied the earlier economy note 17.11, which says splash; the later note 17.12 correctly says gun2. Use the retained actions, not the older prose.

4. **Qualify the shared initial information** (lines 1486-1488). "Same initial observation" is literally false because Engine.observation contains the player index and both configured names. In benchmark logs these names can disclose policy specifications. Say "the same public game state up to player labeling, with neither pending action visible." This does not change the observed round-one results. For a theorem about indistinguishability, equal public labels are an explicit hypothesis in analysis/nominee_prefix_equivalence/PROOF.md.

5. **Replace the obsolete temporary-freeze paragraph** (section 5.12, lines 1347-1348). The final 19:50Z decision has already committed to best_v9e through D. The 22:15Z possible future change is historical, not current. Keep the history if useful but use past tense and link the final decision.

6. **Optional scope improvement for deadline discussion** (sections 2 and 7). Later fortress versions used in the final comparison, including v41 and v43, also retain a three-second planner cutoff. The current wording says "some" and is not a universal false claim, but listing only v26-v28 near the general methods paragraph understates which current opponents this caveat covers. The later economy note 18.9 records the v26-v43 audit.

## Verification and limits

check_report_shift4_v1.py completed with no candidate or opponent policy calls and no games. Its receipt report-shift4-claim-checks.json binds the relevant source and log hashes, the four sampled purchase lists, the 27-list enumeration count, the exact two guard actions and their final HP, and the observation-label check. Findings 1 and 5 are logical and chronological checks against the quoted report and the lead's dated notes. Finding 6 is a requested clarification supported by the teammate's source audit, not a new runtime experiment.

The selected bytes remain best_v9e SHA256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. The report already states the important empirical limit: the selection rule favors best_v9e even though af2g, best_v9f and g1 win many conditions that it loses. No result here changes that decision or supplies pool-D evidence.
