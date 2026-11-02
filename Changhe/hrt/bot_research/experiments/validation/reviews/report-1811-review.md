# Report wording follow-up

Written 2026-10-31T18:10:41.003455+00:00. Reviewed the current REPORT.md, SHA256 `a16f82591d05fcb33646d9e9b38ce677090f80519cc456b4cabb645e6c3208db`, the unchanged combat implementation, the complete pool C results and comparison, and the earlier 17:22 review. This review applies the research-storytelling skill: keep the useful technical argument and correct its exact evidential scope.

## 1. P1 needs the cleanup qualification

Claim and verdict: REFUTED, the literal sentence "Every copy with HP <= S dies before reaching the base". The zero-base-damage conclusion is unaffected. The prior source argument is now independently executed as a fully legal nine-round original-engine prefix. With one splash at (1,1), S=30 and 250 tier1 entries bought in round nine, 249 copies die, one is cleared alive, and base damage is zero. A direct original combat_tick call on the final legal roster entry leaves that copy at the spawn with 10 HP on tick249.

Evidence: `bot_research/experiments/validation/analysis/late_copy_cleanup/PROOF.md` and its `verification/result.json`, completed 2026-10-31T18:10:15.905630+00:00 in 0.050247 seconds. No protected engine state or source was modified.

Suggested text: Every copy with HP <= S that has enough ticks to reach the base is killed first; later copies cannot arrive before combat ends. Thus S >= 1500 guarantees zero base damage for every finite roster.

## 2. Pool C entry-point checks apply to best_v9e

Claim and verdict: CONFIRMED for best_v9e only. The paragraph beginning "All72games of each candidate" immediately joins both candidates to the 1104-call direct/default-factory/recorded-spec check. That can be read as attributing those checks to P5TNUBM as well. The complete 72-game replay check applies to both candidates. The 1104-call entry-point equivalence check applies to the primary best_v9e campaign, as its RESULTS.md states; COMPARISON.md makes no such claim.

Suggested text: All72games of each candidate were independently replayed. For best_v9e, a further fresh-process audit regenerated all1104actual decisions from direct decide, the default factory and the recorded specification, with identical legal actions and unchanged observations.

## 3. Preserve the two dates and uses of pool C

Claim and verdict: CONFIRMED. Best_v9e was selected before its original pool C run. The subsequent fallback decision between best_v9f and best_v9e explicitly uses previously disclosed pool C. The new execution audit can independently validate the bytes and outcomes, but pool C is then reused for selection. The queued proof117 reports every transition and this limitation. Neither the original manifest nor the old evidence is edited.

No report-owner file was changed. This is a source- and receipt-based review, not a fresh review of every tournament row in the report.
