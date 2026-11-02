# Splash-immunity wording and validation scope review

Checked 2026-10-31T17:22:37.168140+00:00 against the current report and unchanged combat source.

Claim and verdict: REFUTED as a literal statement, the report's P1 sentence that every copy with HP <= S dies before reaching the base. The zero-base-damage conclusion is valid. A copy spawned too late can remain alive at the tick limit and be cleared. The standalone proof in analysis/splash_threshold/PROOF.md already states this qualification correctly.

Source argument: a copy born on the final tick does not move on that tick. Only adjacent splash damage at the spawn can hit it before combat ends. For example, a legal map containing one splash at (1,1) has positive exposure along the beginning of the usual length-22 route. A tier1 in roster position 249 has 20 HP and receives only 10 damage at its spawn on tick 249; simulate_map then counts it as cleared. Its full-route exposure would exceed its HP. No newly executed simulation is claimed here. The exact source separates killed and cleared and the earlier phase-defense probe also records cleared copies.

Suggested replacement: Every copy with HP <= S that could reach the base before the tick limit is killed first. Later copies cannot arrive before combat ends. Hence S >= 1500 guarantees zero base damage for every finite roster. This also remains a sufficient condition when guns add damage.

Validation scope: retain the historical held-out status of best_v9e's completed pool C run. If a later candidate is tested on the disclosed C conditions and reverted on a regression against best_v9e, that is an independent execution check used for candidate selection. It does not become untouched validation of the selected winner. The lead's 16:59 note explicitly states that fallback rule. No report-owner file was edited.
