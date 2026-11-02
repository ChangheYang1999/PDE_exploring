# Transfer of the bait, guard and three-heavy-copy schedules

Declared 2026-10-31T17:48:43.131230+00:00, before this lane's matches.

## Claims and fixed conditions

The defense lane supplied two legal schedules, A and B, in bots/defense/counter_astra41.py. Their reported Fortress41 outcomes are losses of 275 and 260 HP respectively from the defender's perspective. First test: reproduce those margins in both player assignments. Second test: at least one schedule defeats frozen best_v9e, V33C or the adaptive Fortress38-backed counter in both assignments. These are separate empirical claims; either may fail.

Use the exact A/B schedules without modification. Six defenders are frozen Fortress41, frozen best_v9e, the fixed V33C specification, P5TNUBM, and the Fortress38 delegated counter in its adaptive and forced-early modes. Cross two schedules and both assignments for 24 complete standard-start games. Keep all conditions, including losses and rejected-action failures. This is development transfer, not reserved validation. The schedules were designed against Fortress38/41 and their fortress results are reproductions, not new held-out tests.

## Mechanism and verification

A and B send three tier1 copies in round two, add fixed guard turrets, and buy three tier5 copies in round eight before completing a splash defense. Whether this bait transfers to a different decision rule is not implied by its original success. Action legality can also depend on earlier combat bounties. Reconstruct every full match with the unchanged engine, check all action acceptances and bot errors, then regenerate both fixed policies from fresh instances on their recorded public histories. Record complete source closure, all data dependencies and both assignment results. Identical repeated conditions are reproducibility checks only; no sampling confidence interval applies.

If the targets use a public-state model or local simulation, regenerate their actual actions. Do not demand an exact private prediction against a different policy. The original engine determines game outcomes. Retain canonical trajectory comparisons and decision timing separately from outcome claims.
