## 2026-10-31T22:39Z  v48 regression complete: at least v46 on every pool, one margin larger; FINAL RECOMMENDATION REVISED: frozen v48

Frozen v48 = v41 + factory_cap 1200 + finish_wrap + finish_robust_gold 400 + finish_gun_check 12 (gate on the whole roster) +
finish_defend_first (defence first; the smallest passing kill reserved; the capacity rule spends the whole slack under the reserve) + the
per-decision finish cache. `bot_research.bots.defense.frozen.v48.fortress:@make` (no parameters) or `...frozen.v48.fortress:decide`;
frozen 22:10:41Z by scratch/queue_ch.sh; live defaults reverted and checked. SHA256SUMS of bots/defense/frozen/v48/:
  a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190  __init__.py
  ad70d4e5e80f8c567546a9ad01ee7bd065fa718c7c12ccbaf4296f8aaf319c0d  counter_astra28.py
  abb38a946c78270a1d86632fbb811b3425de4ecb788c46224d8818c9bccc28b1  counter_astra33.py
  922ef9920d832eb4a49845da470686a80b9cc613b63b5255fea81bfbf93b6cf9  counter_astra37.py
  58c83fa6bb883c93b5aae3ecd7634297b7cd6bb10dfc049a8e188e8e341154b2  counter_astra38.py
  b5f28f3626215083384bfa12498011cc0ea568a6094fbefd695d939a95f011e8  counter_astra41.py
  b725487428efd54292a2405baf10bacfd0ed22d0870bf26d54b1659e1c63e00d  counter_earlygun.py
  067af590c9d2fceef852cc4ac3516d31e01919993f98755cbed44a05d68c37f5  fortress.py
  e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f  geometry.py
  e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545  plan.py
  3d9905ff9cee787b7d6a55da962c4fff2d7c9d8ff682b5373c776f9143bd7994  replan.py
  2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc  simulate.py
  68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824  templates.py
Regression of the frozen artifact against frozen v46 (both seats, engine winner; every HP difference and end round equal to v46's unless
stated): x230 against best_v9e 7W-1D-2L and V29 9-0-1 (16-1-3); x231 strikers (32 opponents) 48-2-14; t86 tuning 102-2-0; x232 STRONG 22-2-2;
x233 scripted econ 16-0-0 (econ15 asym:23:2 seat 1 W +4160 r16 against v46's +3460 and v47's D +3740: the slack fix); x234 forecaster 1-9-2;
t87 mirror+eco 100-4-0; x235 PUNISH 32-0-2; x236 GROWERS 142-0-0 min +380; smoke 8 rounds 800 / -13. Longest decision 2.63 s (x231; v46's
5.29 s in the same pool was measured under a different load; both include the finish cache). Rejected actions 0, bot errors 0 everywhere.
Decision by the rule (at least v46 on every pool by W-D-L): v48 replaces v46 as the FINAL RECOMMENDATION of this lane; it also carries
astra review 12's two constructed-defect fixes (gun-check gate; no draw-to-loss in the dead-anyway fall-through) and check 13's slack fix.
Final version ladder of the lane (all frozen, all with full regressions): v48 (recommended) > v46 (same results, two constructed defects)
> v47 (one scripted draw) > v45 (two scripted draws) > v44 (factory cap only; loses the lead-bot races 3-3-4) > v41 (40-factory cap; 3-0-7).
Against the team's bots on the standard start every version is -5 to best_v9e (the round-1 exchange), 0-0 to P5TNUBM, +5 to V29/V25RM.
Known failures of v48 (unchanged from v41 unless stated): astra41 A/B -275/-260, guard_continuation and astra28 -65, timing -115, early tier4
strikers -43, forecaster tier4 r5 -60, V29 asym:3:2 seat 1 -12974 (its round-26 flood lands before any kill is affordable), best_v9e
standard -5; the padded finish relies on the response model (a heuristic upper bound; astra constructed two states where a stopping gun3 is
outside the 12 tested cells); matching in rounds <= 7 skips the attack step and so the restored finish (only an artificial state shows it).

## 2026-10-31T22:40Z  Addendum to the FOR THE LEAD entry (21:48Z): the final version is v48

The rows of point 3 (fortress against best_v9e and V29 on the five starts) are identical for frozen v48 (x230), v47 (x223) and v46 (x215); v48
is the lane's final recommendation (22:39Z). The reproduction command for the teammate table is in scratch form in the notes' run index: the
harness run `runs/defense/x230_v48_lead` (candidate `bot_research.bots.defense.frozen.v48.fortress:@make`, opponents
`bot_research.experiments.lead.frozen.best_v9e:decide` and hrt-w2's V29 spec, scenarios none mirror:1:2 asym:3:2 mirror:22:3 asym:23:2).
