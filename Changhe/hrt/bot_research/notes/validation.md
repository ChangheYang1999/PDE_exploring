# Counter-strategies and independent validation

## 2026-10-31 02:00 UTC: startup audit

Claim: the received protected tree has the discrepancies announced by the operator, and existing tests pass.

Method: independently hashed every file outside `bot_research/`, retaining an explicit inventory including the pre-existing `.venv/`, and compared the supplied manifest. Ran the original test discovery with bytecode disabled.

Result: 903 file/symlink inventory entries outside `bot_research/`; 1002 manifest paths absent; hashes differ only for `td_game/combat.py`, `tests/test_engine.py`, and `tests/test_rules.py`. Existing tests: 59 run, 9 skipped, successful in 5.290 seconds. Evidence: `runs/validation/integrity-start.json` and `runs/validation/existing-tests-start.txt`. No repairs made.

Verdict: CONFIRMED. End-of-run integrity must compare against this received tree, not silently assume the stale manifest matches.

## 2026-10-31 02:00 UTC: critical combat contract and initial plan

Claim: guns select one frontmost target per tick; splash attacks all copies in its eight adjacent cells. The prose claim that guns attack every target in `docs/game.md` is stale.

Method: inspect `td_game/combat.py` and the current tests. Gun targets maximize route progress, retaining the first stable spawn-order copy on ties. All guns select before damage resolution, so they may overkill the same copy; they do not retarget after another gun's damage. Splash uses Chebyshev distance exactly one. Base arrivals are removed before attacks.

Result: source and current regression tests agree. This supports developing dense cheap swarms as counters to gun-heavy defense and ordered tough-leading mixed rosters as counters to concentrated target selection. Strength claims remain untested.

Verdict: CONFIRMED for the rules; OPEN for strategic value.

Immediate work: build independent evaluation scripts using the unchanged Engine and adapter, materially distinct rush/mixed/delayed opponents, and exact counter-searches. Reserve separate opponent schedules for final validation. Both player assignments are required. Distinct policy parameters and legal opening histories provide different conditions; repeated deterministic seeds alone do not.

Model collaboration: the lead and economy lane MODEL files identify `us.anthropic.claude-opus-5-5`. Findings are exchanged via team notes. This lane is GPT-6 astra. No separate model client or remote compute is launched.

## 2026-10-31 02:01 UTC: opponent and holdout design (prospective)

Development archetypes to implement: (1) immediate cheap swarm, (2) immediate mid-tier pressure, (3) saved heavy units, (4) fixed growth then swarm, (5) fixed growth then heavy strike, (6) minimal splash insurance then growth, (7) concentrated gun defense then offense, (8) mixed heavy-leading roster, (9) adaptive purchase search against the observed enemy map. These differ in build decisions, attack timing, unit selection, or response to public state.

Held-out pool: schedule-driven alternating mixtures, attack pulse schedules, and legal scripted opening prefixes will be specified before final integration freezes. They will not be included in development tournaments or counter-search objectives. Final evaluation will use a frozen candidate source hash. Once a holdout is inspected, it is retired as a final holdout if the candidate is revised using that result; further final validation must use a separate reserve pool. Synthetic opening scenarios must be reached only by ordinary legal actions from the standard initial state; no balance changes or privileged state edits in strength comparisons.

Verdict: OPEN, implementation in progress. Both assignments, per-action rejection accounting, adapter errors, HP, ending round, source hashes, true varying parameters, and runtime will be recorded.

## 2026-10-31T02:02:30Z: independent evaluator and first development matrix

Claim: the independent loop reproduces the official runner on selected deterministic matches.

Method: compare every decoded replay record, complete result and ending HP for rush_t1 versus rush_t2 and splash_t2 versus eco5_t3. Run each independent match again and compare a canonical replay SHA-256 that excludes wall-clock timing.

Result: all records equal (16 and 18 records respectively), repeated trajectories identical. Evidence: runs/validation/evaluator-crosscheck-001.json; script experiments/validation/check_evaluator.py. The two repeats are reproducibility checks, not additional strength evidence.

Verdict: CONFIRMED for these cases. Additional final checks must address candidate state isolation, source freezing, and ordering effects.

Claim: the 12 initial development archetypes are strategically non-equivalent, but none dominates this small pool.

Method: all 144 ordered pairs, including 12 self-matches, under bundled rules. Both player positions are included. No nominal random seed is used. The off-diagonal conditions represent 66 policy pairs, each in both positions. Results and histories: runs/validation/archetype-round-robin-001.jsonl. Representative full replays: runs/validation/development-archetypes-001-replays/.

Result: 112 decisive games and 32 simultaneous-destruction draws; zero rejected actions and zero bot errors. Total measured match runtime 15.762 seconds, maximum measured decision 0.128 seconds. Splash_t2 has 14 wins, 8 draws, 2 losses across its 24 player appearances (including its self-match counted from both positions). Splash3_t4 has 14/4/6. Immediate tier1 pressure beats undefended five-round growth into tier3, while one early splash reverses the cheap-swarm vulnerability. These are weak developmental controls, not the final candidate's validation pool.

Verdict: CONFIRMED within this matrix; no global strength claim.

Claim: exact visible-defense purchase search automatically improves every simple purchase policy.

Method: bots/counters/visible_search.py constructs local states exclusively from observations and uses the unchanged simulate_map to evaluate pure and heavy-leading/reversed mixed purchase sequences. Its four-round growth and one-splash opening are fixed. Ten paired matches against five development policies.

Result: 6 wins, 2 draws, 2 losses; it loses to splash_t2 in both positions, ending own HP -40 versus 14. The one-step objective cannot value keeping money or damage in future rounds. The search is a useful attack counter, not an automatically stronger complete policy. Evidence: runs/validation/visible-search-001.jsonl.

Verdict: REFUTED. Investigate horizon and timing instead of treating current-turn damage as an adequate whole-game objective.

## 2026-10-31T02:06:32Z: reserved final-validation procedure

A prospective profile pool and a disjoint reserve pool are in experiments/validation/holdout_manifest.json. No game against either pool has been run. experiments/validation/final_validation.py is reserved for the candidate freeze. It records source hashes, full independent replays, both assignments and standard-state W/D/L separately from legal-prefix continuation stress tests. Prefix tests skip the policy's round-one initialization, so they are robustness tests of continuation behavior, not ordinary best.py matches. The shared module implementation means fresh-process/state-isolation checking remains required if the final bot acquires global mutable state.

For the lead: publish a dated candidate-ready assignment when best.py is ready for targeted counter-search. The reserved final pools should remain unused by integration and tuning. Initial development opponents and the visible-search counter are already importable from bots/counters/.

## 2026-10-31T02:08:32Z: lead harness audit, cycle 1

Claim: authoritative match outcomes are taken from the unchanged engine, but some surrounding evaluation behavior needs correction before large tournaments.

Method: read harness/match.py, tournament.py, scenarios.py, gamekit.py and baselines.py. Reproductions in experiments/validation/harness_audit.py; evidence and exact reviewed source hashes in runs/validation/harness-audit-001.json.

Results:

1. HIGH, confirmed resource hazard: the uncapped greedy_eco factory list grows to 1,763,105 actions at round 25, 28,938,001 at round 30 and 2,100,049,354,878 at round 50 under its own exact empty-map recurrence. The turtle and maze baselines also send all spare gold to factories. Do not run these policies to round 50 uncapped; add explicit baseline factory/action limits and report them as policy parameters. These counts were calculated without constructing large lists.
2. CONFIRMED scenario contamination: TimedBot runs the candidate before the scripted override on the same mutable observation. In eco:1 an ordinary empty-return bot yields five factory actions, a bot that changes its private observed gold to zero yields no scripted actions, and an exception prevents the override entirely. Both are reproduced. A fixed scripted scenario should compute its action list from an independent pristine copy before invoking the candidate, with an explicit policy for candidate errors. Current behavior is not a candidate-independent fixed opening.
3. CONFIRMED version-recording gap by inspection: module_hash is computed only after the match, hashes only the entry module and truncates to 16 hex characters. Imported planning/strategy dependencies are not recorded; changing an imported module leaves the entry hash unchanged. Record full dependency hashes before and after each run, or require a frozen source manifest for the batch.
4. CONFIRMED aggregation gap by inspection: results.jsonl appends and summarize groups only by candidate/opponent spec. Reusing the output directory after editing the same bot spec mixes versions silently. Group by source version and scenario, or reject a mixed-version batch. Explicit scenario aggregation can then be reported separately.
5. CONFIRMED small baseline bug: random_legal issues an unaffordable factory at observed gold 1 for seeds 0, 1 and 2. Check gold >= factory_cost before appending. The engine does reject this correctly; it is not an engine bug.
6. GOOD: the tournament uses spawn processes with maxtasksperchild=1, so matches have fresh module state. Both assignments are explicit; W/D/L comes from winner, correctly treating simultaneous destruction as a draw regardless of HP difference.

Verdict: CONFIRMED issues 1-5 with the reviewed source version; core authoritative outcome handling is correct. I have not edited lead-owned files.

Timing note for the lead: the cycle-1 assignment heading currently says 02:55Z, while the actual current wall clock is around 02:08Z. Please replace future-dated headings with date -u output before publication; no work duration should be inferred from that heading.

## 2026-10-31T02:12:07.172969+00:00: expanded tuning pool delivered

Claim: the tuning pool now includes materially different economic, offensive, defensive, adaptive, and seeded policies.
Method: `bots/counters/pool.py` exposes factory functions compatible with the lead's `module:@factory?parameter=value` syntax. Entry points are `archetype` (the 12 registered profiles), `turtle` (splash or gun by `kind`), `stacker`, `mirror`, `random_legal`, and `rush_t5`. Purchases are explicitly bounded for finite evaluation. The registered profiles plus these default factories are TUNING opponents; the parameter combinations in `experiments/validation/holdout_manifest.json` remain unused.
Result: `runs/validation/expanded-pool-smoke-001.jsonl` contains both assignments for six additional policies against `rush_t1`. Pure splash turtle drew at 800:800 on round 50; gun turtle lost 720:800 on round 50; mirror won 800:-130 on round 8; seeded random 130 won 800:-221 on round 13; stacker won 800:-1705 on round 10; tier5 saver lost -75:800 on round 7. All 12 matches had no bot errors and no rejected actions. Runtime was at most 1.65 seconds per match. These are implementation and diversity checks against one weak opponent, not a claim of final strength.
Reproduction: `.venv/bin/python -B -m bot_research.experiments.validation.check_pool`, from the project root with the required environment. The script uses exclusive output creation; choose a fresh output name before rerunning.
Verdict: CONFIRMED for implementation and this exact matchup set; broader strength OPEN.

## 2026-10-31T02:12:07.172969+00:00: purchase order and cutoff control

Claim: putting expensive copies before cheaper copies can improve damage against front-targeting guns, but large-roster order comparisons also change arrival eligibility.
Method: `experiments/validation/order_probe.py`, unchanged `simulate_map`, four fixed legal turret maps, six light/heavy tier pairs, four light counts, three orders. This is a synthetic static-map mechanics experiment, not a match result. `runs/validation/order-probe-001.jsonl` contains 288 rows (96 compositions, three orders each).
Result: 60 of 96 compositions were order-sensitive. Restricting to the 48 compositions with 11 or 110 total copies, where every spawn can arrive before the 250-tick cutoff, 12 were order-sensitive. Against three gun3 turrets at (1,1), (2,1), (3,1), ten tier3 plus one tier5 cost 1650: heavy-first and interleaved caused 400 base damage, heavy-last 244. Thus six additional tier3 copies hit with heavy-first. Short-wave pure splash results were order-invariant. The remaining large-wave differences must not all be described as screening: purchase order also determines which types occupy dead late phases.
Verdict: CONFIRMED for the stated examples and finite set. No claim of a universally optimal ordering.

## 2026-10-31T02:12:07.172969+00:00: lead baseline fixes observed

The current lead `harness/baselines.py` now caps factories at 40 and minions at 60 per decision and guards random factory purchases by affordability. These changes address the earlier uncapped-growth and unaffordable-factory findings for these baseline entry points. They also change the baseline policies and must be versioned separately from older results. `harness/match.py` still calls the bot before computing its scenario override and still records only the entry module's truncated hash after the match. Those findings remain OPEN.

## 2026-10-31T02:14:26.211670+00:00: prospective holdout completion

The still-unused holdout manifest now includes four distinct-policy parameter settings in each pool in addition to six roster/economy profiles: seeded random, spending mirror, stacker, and pure turtle. Pool A uses random seed 2003; pool B reserves 4027. No candidate result was observed on any of these settings. `final_validation.py` now launches a fresh Python process for every match, freezes all bot Python/JSON data plus engine, harness and validation sources, verifies the freeze before and after each match, and records timeouts as explicit failures. Standard starts and prescribed legal continuation prefixes have separate scores. The default batch is bounded to 480 seconds plus one 90-second match. The final procedure has not yet been run.

## 2026-10-31T02:18:19.994833+00:00: independent simulator checks, phase purchases, and cycles

Claim: both shared planning simulators reproduce the engine on additional boundary cases.
Method: `experiments/validation/check_simulators.py --output bot_research/runs/validation/simulator-crosscheck-001.jsonl`; 240 fixed-seed legal static maps and rosters, including serpentine routes and roster sizes 0, 1, 2, 226, 227, 228, 229, 249, 250, 251, 499, 500, 501, 749, 750, 751, 1251. Check all five combat totals for lead gamekit, hits/damage and per-entry arrival damage for economy fastsim.
Result: all 240 agree, with no source changes during the check; 24.12 seconds measured runtime. Exact source versions and conditions are saved with the output metadata. This is finite evidence, not a proof for arbitrary inputs.
Verdict: CONFIRMED on these cases.

Claim: buying cheap fillers in late modulo phases can improve immediate damage.
Method: `phase_defense_probe.py` uses the unchanged combat routine on 63 synthetic fixed-map states. It compares the existing pure/mixed sequence generator to its extension in `bots/counters/phase_search.py`.
Result: 34 conditions improve. With 225 active tier1 entries, 3000 gold, and a splash at (1,1), the plain best sequence deals 636 damage. The phase-aware sequence buys 66 tier2 and 22 tier1 fillers for 2970 gold and deals 792. On the four-splash map with 240 existing tier1 entries and 3000 gold, it improves 560 to 728 damage. No claim is made about future roster expiration or complete matches.
Verdict: CONFIRMED for the finite set. The fixed-map splash criterion and player-assignment symmetry now have standalone informal proofs and a reading index under `experiments/validation/analysis/`.

Claim: the initial development matrix contains genuine counter-strategy cycles.
Method: require every edge to win under both player assignments in the 144-match matrix.
Result: 18 distinct three-policy cycles. One is eco3_t1 > eco5_t3 > gun_t3 > eco3_t1. In that order the decisive outcomes are 150:-505 on round 7, 540:-526 on round 8, and 800:-32 on round 11. This supports testing diverse response classes rather than selecting by success against a single baseline. These are developmental policies, not a claim about the final candidate.
Verdict: CONFIRMED.

Additional harness diversity finding: `maze_eco` only accepts a wall if that single wall immediately increases path length. On the empty square map no one-cell block eliminates every monotone shortest route. Consequently it builds no walls from the standard state and follows the same factory-only actions as `greedy_eco`, until its map is externally changed by a scripted prefix. Count these as one standard-start behavioral baseline, or replace the maze policy with a multi-wall plan.

## 2026-10-31T02:26:52.095495+00:00: complete static screen and adaptation ablation

Claim: a fixed-profile search is insufficient to establish a dominant policy.
Method: all 1,512 profiles in `experiments/validation/profile_search.py`, each against splash_t2, rush_t1, eco5_t3, and splash3_t4 as player 0. Four result shards in runs/validation/profile-search-00[12]-shard[01].jsonl. This is 6,048 deterministic screening conditions, not independent replications. Select eight profiles by worst score, mean score, lower enumerated index, keeping distinct roster/defense combinations, then test all eight against 18 tuning opponents in both positions.
Result: the best screening score was 3 wins and 1 simultaneous-destruction draw. In the 288 confirmation matches, profiles 732 and 984 each scored 28 wins and 8 draws with no losses; profile 627 scored 26/8/2 and lost to random_130. Full selection parameters are in `runs/validation/profile-finalists-001.json`; full confirmation histories are in profile-confirm-001-shard[01].jsonl. All screening and confirmation matches had zero bot errors and zero rejected actions. No reserved holdouts were used.
Verdict: CONFIRMED within the stated development pool; final generalization OPEN.

Claim: identifying an opponent family from its observed purchases can improve over a fixed policy.
Method: `bots/counters/posterior_response.py` predicts only public purchases using fresh local states and the 12 registered archetypes. It ignores names. Each round it compares predicted factory counts, buildings and new roster entries with the next public observation, then selects a response from the fixed development payoff table. The four-way ablation uses growth/splash first-round openings crossed with adaptive/fixed-splash_t2 responses, against all 12 modeled families in both positions.
Result: growth opening plus adaptation won all 24 matches; splash opening plus adaptation scored 18 wins and 6 draws. The fixed response scored 14 wins, 8 draws and 2 losses under either opening. All 96 matches were legal and error-free. Evidence: `runs/validation/posterior-response-001.jsonl`. This is adaptation to a known finite family, trained on its payoff matrix. Transfer to unmodeled opponents is being tested separately.
Verdict: CONFIRMED for the factorial comparison; robustness OPEN.

For integration: factory `bot_research.bots.counters.posterior_response:@make` is ready as an additional tuning opponent. It should not be treated as the final best bot on the basis of the modeled-family result. Targeted switching-policy counter-search is running now.

The old 12-policy empirical matrix also has a 1/2 mixed5 + 1/2 splash_t2 portfolio with at least half-score against every column. Exact rational verification of that finite payoff statement is saved in `runs/validation/archetype-matrix-analysis-001.json`. This is not a mixed-policy optimality claim for the full game.

## 2026-10-31T02:31:43Z: adaptation fails outside its fitted family

Claim: the known-family sweep does not imply robust opponent adaptation.
Method: 30 paired matches against 15 unmodeled development policies: the six expanded pool defaults, eight static-search finalists, and VisibleSearch. Separately screen 385 legal policies that follow one registered profile then switch to another at rounds 2 through 8. No reserved holdouts were used.
Result: PosteriorResponse with growth opening and discount 0.9 scored 12 wins, 2 draws, and 16 losses in transfer. It lost both assignments to spending_mirror, six of the eight static finalists, and VisibleSearch. The switching screen found 29 counter wins, 11 draws, and 345 counter losses as counter player 0. A splash_t2 prefix switched to eco5_t3 at round 3 wins 800:-370 on round 9. Its trace shows that correct late identification does not repair the initial commitment: the response becomes rush_t1 against a map that already has a splash. Evidence is in posterior-transfer-001.jsonl, switch-search-001-shard[01].jsonl, and switch-finalists-001.json under runs/validation. All 415 matches were legal, error-free, and source-stable.
Verdict: REFUTED as a robust-response claim; CONFIRMED as a finite-family adaptation result. Paired counter confirmation and forgetting-rate ablations are running.

## 2026-10-31T02:31:43Z: harness follow-up and remaining version boundary

The lead has fixed the scripted-action mutation/exception issue in source: the override is now computed from a pristine copy before calling the policy, and policy exceptions during the prefix are recorded separately. It now records full entry hashes, local loaded-source hashes, and a before/after change flag. Explicit append is required for an existing tournament output. These address the original findings substantially; a focused reproduction will check the new behavior.

Remaining issue by inspection: spec_version hashes only Python siblings of the entry file and harness files. A best.py import from bots/economy/ or bots/defense/ is outside that set. Editing that dependency between batches can leave version_a unchanged, so the new version-based summary still merges those batches even though individual rows contain different dependency hashes. Grouping by a canonical digest of the complete loaded-source and configuration manifest would avoid this. The current summary also still pools standard starts and scripted scenarios into the same candidate/opponent row; report those separately when making standard-start strength claims. Independent final validation already freezes all bot source/data trees and separates continuation stress scores.

For the defense lane: its latest geometry heading currently says 02:35Z, ahead of this real timestamp. Please replace that heading with the actual recording time before publication. The geometry claims themselves have not been rejected on that basis.

## 2026-10-31T02:36:29Z: first lead Planner has a confirmed HP-lock counter

Claim: an early small attack followed by protected growth beats the first lead Planner even though that Planner grows much richer.
Method: archive best.py as bots/counters/snapshots/lead_planner_001.py (SHA-256 f8b57dca69d4cde6decf0ae35abd4205f172670f7362ce64e23c04d52c798d2d). Counter bots/counters/forecast_lock.py privately simulates that public deterministic policy on a swapped public observation, then uses the economy lane's defense builder against its predicted roster. It never accesses the real opponent object, submitted actions, live engine, or hidden state. Buy 1, 2, 4, or 6 tier1 copies in round 1; vary reserve 0/180 and saturation round 20/45; play both assignments. All 32 matches are in runs/validation/forecast-lock-001.jsonl with complete replays alongside.
Result: one- and two-copy openings won all 16 of their matches, while four- and six-copy openings lost all 16. With opening_units=2, reserve=180, saturate_round=20 the counter wins 800:720 at round 50 in both assignments. The Planner lets the two initial copies hit for 10 damage in each of rounds 1 through 8, eventually saturates, and never recovers the HP deficit. The counter predicts all submitted action lists exactly in all 32 matches; every match has zero errors, rejections, and source changes. All imported source versions were constant across the batch. This is a targeted known-policy counter, not a generally robust bot.
Counter spec for integration: bot_research.bots.counters.forecast_lock:@make?opening_units=2&reserve=180&saturate_round=20. The current default opening of 6 is deliberately not the selected counter; use the explicit spec.
Verdict: CONFIRMED for the archived first Planner. Revision suggestion: account for persistent-roster damage over multiple future rounds and the irreversibility of an HP deficit after mutual saturation. A one-round gold-plus-damage objective can rationally accept the same damaging copy repeatedly while losing the eventual HP comparison. The broader development-pool challenge of this snapshot is still running.

## 2026-10-31T02:36:29Z: two Planner bounds are false as stated

Claim tested: each newly purchased splash can increase total per-copy splash damage by at most 80, and _potential_damage is an upper bound on affordable one-round damage.
Method: planner_rule_probe.py enumerates 8,476 legal near-complete slot layouts; verify the selected case with unchanged td_game.combat.simulate_map via verify_planner_bounds.py. Both scripts and JSON evidence are under experiments/validation and runs/validation.
Result: adding one splash at (1,1) to the saved legal map changes the BFS route from length 58 to 78 and raises total splash damage from 760 to 1,610, an increase of 850. It forces the route past existing towers. One, 100, and 501 tier5 copies have positive hits before the addition and zero afterward in the original engine. Thus 80 is only a bound on the new tower's direct contribution on a fixed route, not total defensive response. Separately, on an empty map at 15,000 attack gold, 1,000 tier1 copies cause 4,560 base damage, while _potential_damage reports 4,236 after its per-type 500-copy truncation. This is a synthetic mechanics counterexample, not a complete-game win.
Verdict: REFUTED for both upper-bound interpretations. Treat them as heuristic estimates or replace them with sound bounds. An exact pure-tier count can be computed with full modulo cycles and a remainder without enumerating all copies.

## 2026-10-31T02:36:29Z: forgetting-rate ablation and maze screen complete

All eight selected switch counters beat the discount-0.9 response in both assignments (16 losses for the response). Discounts 0, 0.25, and 0.5 each convert six of those 16 matches to wins, leaving ten losses. Discount 1 still loses all 16. Faster forgetting helps some switches but does not repair the irreversible-state problem. Evidence: switch-confirm-001.jsonl and representative full replays.

All 360 maze profiles (two/four complete barriers, nine growth horizons, five pure tiers, four defense types) were screened against the same four development opponents, 1,440 matches. No profile beats all four: best worst-score 0.5 and mean 0.875. No errors, rejections, or source changes. Six finalists and selection rules are in maze-finalists-001.json; paired expanded-pool confirmation is still pending. These mazes spend potential future turret sites on cheap walls, so they are pressure opponents rather than saturation-safe designs.

## 2026-10-31T02:44:03Z: broad wins coexist with a specific counter

Claim: the first Planner's broad development score does not establish robustness.
Method: 27 opponents (18 diverse tuning policies, eight static-search finalists, and the fitted PosteriorResponse), each in both assignments, against the archived lead_planner_001.py. All use the unchanged engine. No reserved holdouts were used.
Result: 54 wins, zero draws or losses, with zero bot errors, rejected actions, or source changes. Evidence: runs/validation/lead-planner-v1-development-001.jsonl. This coexists with the previously documented 800:720 loss against ForecastLock. Most broad opponents never both establish an early HP lead and subsequently close every defensive leak.
Verdict: CONFIRMED for these exact conditions; robustness remains OPEN. A forecast-free PokeLock ablation is now being tested against both this Planner and frozen economy v2. It has already found player-0 wins against both; paired confirmation is in progress. This is development work, not final validation.

Claim: faster forgetting improves some transfer outcomes but does not make the finite-family response robust.
Method: repeat the 30 transfer conditions with discount 0 instead of 0.9; other parameters fixed. Evidence: posterior-transfer-002-discount0.jsonl alongside posterior-transfer-001.jsonl.
Result: discount 0 scores 16 wins and 14 losses, compared with 12 wins, 2 draws, 16 losses for discount 0.9. It changes spending_mirror and VisibleSearch from paired losses to paired wins, profile819 from paired draws to wins, but changes random_130 from paired wins to losses. All matches are legal, error-free and source-stable. The gain is not uniform across opponent families.
Verdict: CONFIRMED as a finite ablation; a claim of uniformly better adaptation is REFUTED.

Claim: the repaired scenario wrapper preserves prescribed actions under mutation and exceptions, while summary aggregation still mixes conditions.
Method: experiments/validation/harness_audit_followup.py, evidence runs/validation/harness-audit-002.json.
Result: untouched, mutating, and raising fixtures all produce the same five prescribed factories; the raising fixture has an explicit scenario error and no engine error. Seeds 0 through 99 emit no unaffordable factory at gold 1. A synthetic pair of rows with the same entry version but different imported-source hashes and scenarios is still pooled into one summary row. The latter is a synthetic aggregation check, not a fabricated match result.
Verdict: CONFIRMED repairs and remaining aggregation limitation.

Claim: independent final validation can preserve completed evidence and distinguish failed conditions.
Method: final_validation.py now archives frozen source bytes, records interpreter/affinity/thread context, verifies result conditions, and separates failed, rejected, standard, and continuation outcomes. isolated_match.py publishes JSON atomically and exclusively. Fault-injection checks cover truncated JSON, conflicting failure/result files, pending conditions, rejected actions, and exclusive publication. Fresh-process game checks use only fixtures.
Result: all 12 artifact/scoring checks pass in runs/validation/final-runner-check-001/checks.json. Three fresh-process fixture matches pass the repeatability and prefix checks in isolation-check-002/summary.json. Neither reserved pool has been played.
Verdict: CONFIRMED for the checked failure modes; final candidate validation remains pending.

## 2026-10-31T02:51:48+00:00: forecast-free opening counter and transfer limits

Claim: predicting the opponent's code is not necessary to beat the first Planner or frozen economy v2.
Method: confirm_poke.py tested opening_units 1 and 2, reserve 0 and 180, phi 1, saturation round 20, against lead_planner_001 and economy.frozen.v2.econ (late_round=6, phi=0), in both assignments. PokeLock uses only visible roster, gold and the frozen defensive planner. Complete replays: runs/validation/poke-lock-confirm-002/. The earlier confirm-001 attempt failed while serializing a Path, before producing any result row; it is excluded.
Result: 14 wins and 2 losses, all legal, error-free and source-stable. Opening 1 wins against both targets with either reserve: 800:760 or 800:745 against Planner, and 800:795 against economy. Opening 2 with reserve 0 wins 800:730 and 800:790; opening 2 with reserve 180 loses to economy in round 13.
Counter spec: bot_research.bots.counters.poke_lock:@make?opening_units=1&reserve=0&phi=1.0&saturate_round=20. Use this explicit spec; the module defaults are not the selected parameters.
Verdict: CONFIRMED for these frozen targets.

Claim: this small-opening defense is a universally safe counter.
Method: transfer_poke.py --opening-units 1 --reserve 0, with 18 diverse development opponents in both assignments; no reserved holdout. Evidence: runs/validation/poke-lock-transfer-001-n1.jsonl.
Result: 20 wins, 14 draws and 2 losses. Both losses are against eco6_t5, ending -40:760. Every condition is legal, error-free and source-stable. Several opponents that defend immediately draw 800:800.
Verdict: REFUTED. The targeted win coexists with a delayed heavy-wave vulnerability.

## 2026-10-31T02:51:48+00:00: Planner v3 counter update and pure-tier threat limitation

Current target snapshot: bots/counters/snapshots/lead_planner_003.py, SHA-256 49db78389fc2e32748da1315d0eedd8b2b4e4511c8b4a57c17708c9ebbc7ee93, identical to live best.py when checked at this entry. An updated forecaster is necessary because the original forecast_lock predicts the earlier policy.
Method: evaluate_forecast_v3.py screened 10 opening/reserve combinations, player 0 only, saturation round 20. Evidence: runs/validation/forecast-lock-v3-001.jsonl and full replays.
Result: openings 1 and 2, with reserves 0 or 180, win 800:795 and 800:790 respectively. Opening 0 draws; openings 4 and 6 lose. Every forecast exactly equals the opponent's actual submission; no errors, rejections or source changes. Paired confirmation is running separately.
Counter spec: bot_research.bots.counters.forecast_lock_v3:@make?opening_units=2&reserve=0&saturate_round=20.
Verdict: CONFIRMED only for these player-0 screens so far.

Claim: fixing the 500-copy cap makes the maximum over pure-tier purchases an upper bound on all affordable damage.
Method: exact fixed-combat input and standalone proof in experiments/validation/analysis/pure_tier_threat/, reproduced by verify_pure_tier_bound.py against unchanged simulate_map.
Result: with 225 existing tier1 entries, a single splash at (1,1), and budget 3000, the best pure-tier purchase causes 636 base damage. Appending 3 tier2, then 22 tier1, then 63 tier2 costs 2970 and causes 792. It places cheap padding in the non-arriving phases. Engine evidence: runs/validation/pure-tier-bound-001.json.
Verdict: REFUTED as a universal bound. This is a fixed legal combat input, not a whole-game win or a claim that the current Planner reaches it. The current pure-tier term remains a heuristic threat class.

## 2026-10-31T02:56:54Z: paired confirmation against Planner v3

Claim: the revised Planner still loses to a small first-round poke followed by forecast defense.
Method: evaluate_forecast_v3.py --openings 1 2 --sides 0 1, reserves 0 and 180, saturation round 20, archived lead_planner_003 at the hash in the previous entry. Evidence: runs/validation/forecast-lock-v3-confirm-001.jsonl and eight complete replays.
Result: all eight counter wins, 800:795 for one opening unit and 800:790 for two. Forecasts exactly matched every actual opponent submission. No bot errors, rejections or source changes. These are four parameter conditions with their swapped assignments, not eight independent random trials.
Verdict: CONFIRMED. The revision reduced repeated poke damage from 80 to 10 HP for the selected two-unit opening, but the first-round HP deficit still determines the game after immunity.

Communication with the lead's and economy lane's Opus 5.5 work continues through the shared notes and frozen policies; their MODEL files identify us.anthropic.claude-opus-5-5. No separate remote model client or additional compute service is used. The lead's new static import-closure hashing is now present; a follow-up audit is pending. The timed-wave search against Planner v3 and lam variants is running, with a separate heavier-opening check. Reserved pools A and B remain unused.

## 2026-10-31T02:58:30Z: heavier opening and pressure-search ablation

Claim: making Planner v3 price defense earlier, by lowering lam, removes the opening counter.
Method: confirm_first_wave.py tested tier1, tier2 and tier3 first-round purchases with count caps 1 and 2, against lam 1, 0.5 and 0.2; both assignments. After that single purchase the counter defends against the exact public-policy forecast and invests. Evidence: runs/validation/forecast-first-wave-001.jsonl and 36 complete replays.
Result: 24 counter wins and 12 losses, with no errors, rejections, source changes or forecast mismatches. One tier2 wins 800:740 against lam 1 and 0.5, and 800:776 against lam 0.2. Two tier2 win 620:608 against all three. Tier1 caps 1 and 2 win 800:795 and 800:790 against all three. Tier3 loses. The two tier3 caps buy the same single affordable unit and are duplicate trajectories, not distinct strategic evidence.
Counter spec for the default target: bot_research.bots.counters.forecast_timing:@make?attack_round=1&tier=tier2&count_cap=1&attack_share=1.0&model_lam=1.0. Change model_lam together with the target for these known-policy tests.
Verdict: REFUTED for these lam changes. Stronger defensive valuation alone did not close the tested first-round weakness.

Claim: exact current-action forecasts suffice to make a simple greedy attack policy strong.
Method: PredictedPressure grid of 36 conditions: lam 1, 0.5 or 0.2; immediate-damage values 2, 4 or 12 gold per HP; defensive budget shares 0.5 or 1; opening 0 or 1 tier1. Player 0 screens only. Evidence: predicted-pressure-v3-001-shard0.jsonl and shard1.jsonl.
Result: 3 wins, 3 draws and 30 losses, all source-stable, legal and error-free, with every opponent forecast exact. The three wins all use one tier1, full defense and attack_weight 2; they are the 800:795 opening lock. Larger attack values often spend away the economy needed for later defense.
Verdict: REFUTED as a sufficiency claim for this policy class. A new complete-continuation search is being tested to value that downstream consequence explicitly. Its observation reconstruction passes 45 round-transition checks on two schedules, including roster expiration and later repurchase; the equivalence is up to irrelevant roster-ID renaming.

## 2026-10-31T03:04:18Z: complete-continuation counter and cheap extracted schedule

Claim: valuing purchases by their complete continuation against the known public policy can improve on immediate-damage scoring.
Method: ForecastRollout reconstructs a new Engine from the public observation, predicts the frozen Planner v3 policy, and compares each candidate purchase with no purchase followed by a fixed defensive/economic continuation. Candidates are bounded pure-tier counts through round 12. The continuation runs to the actual end or to both sides' permanent splash immunity after the target's template walls are complete. The tested target is lead_planner_003.py, SHA-256 49db78389fc2e32748da1315d0eedd8b2b4e4511c8b4a57c17708c9ebbc7ee93; live best.py still had this hash at 03:03 UTC. This is legitimate known-policy planning from public state, not inspection of the opponent's pending actions. Evidence: forecast-rollout-001-lam1-side0.json and side1.json, their complete replays, and the 45 reconstruction checks in forecast-rollout-check-001.json.
Result: two counter wins, 800:528 in both assignments, no rejected actions, errors, source changes or forecast mismatches. The selected purchases were one tier2 in round 1, one tier2 in round 5, one tier4 in round 9, and one tier5 in round 12. Each match took about 64 seconds, with a maximum counter decision of 19.75 seconds in the player-0 run. The exact finite-horizon policy-improvement statement, proof, hypotheses and implementation caveats are in experiments/validation/analysis/rollout_improvement/PROOF.md. The proof is for a fixed known opponent and exact continuations; it does not establish universal bot strength.
Verdict: CONFIRMED in these two deterministic assignments. This is a stronger targeted counter than the one-tier2 opening, which wins 800:740.

Claim: the expensive search's selected attack schedule can be used cheaply on this target.
Method: ForecastSchedule fixes the four purchases above and retains forecast defense, with no continuation search. evaluate_forecast_schedule.py tested lam 1, 0.5 and 0.2, changing the private forecast model with the target, in both assignments. Evidence: forecast-schedule-001.jsonl and six complete replays. At lam 1, the complete trajectories, accepted-action counts and round histories are checked equal to the corresponding full-search runs up to bot names.
Result: all six counter wins, no errors, rejections, source changes or forecast mismatches. HP is 800:528 for lam 1 and 0.5, and 800:776 for lam 0.2. Runtime is 3.8 to 4.4 seconds per match. The extracted schedule does not retain a general policy-improvement guarantee away from its derivation conditions.
Counter spec for the current default Planner: bot_research.bots.counters.forecast_schedule:@make. Parameters model_lam and model_kappa must describe the target if changed. The code predicts snapshot 003; if best.py changes, exact prediction is no longer assured.
Verdict: CONFIRMED for these conditions. Recommended addition to the lead's development challenge pool. Reserved validation pools remain unused.

## 2026-10-31T03:06:43Z: import-closure audit and stronger response to lam 0.2

Claim: the lead's new static import closure fixes cross-directory version tracking.
Method: harness_version_audit.py checks direct imports, relative imports, package initializers, a changed dependency in a nested fixture, and the actual ForecastSchedule closure. Evidence: runs/validation/harness-audit-003.json. The first fixture attempt incorrectly formed its module name from an absolute TemporaryDirectory result and failed its own assertion; the corrected attempt is the reported check. The failed diagnostic is retained and path-redacted.
Result: static dependency changes alter the digest, restoring the dependency restores the digest, and ForecastSchedule's frozen economy and Planner dependencies are included. Dynamic import_module dependencies are outside this static closure, as its documentation implies; no such dynamic imports were found in current counter or best.py source. Synthetic summary checks still pool standard and prescribed-opening scenarios, and still count a source-drift win and an opponent-error win as two wins. The summary shows a version warning and error count, but does not exclude those rows.
Verdict: CONFIRMED static repair and remaining aggregation limitations. For final claims, separate scenarios and exclude invalid conditions explicitly. Our independent final runner already does both.

Claim: stronger defensive valuation at lam 0.2 removes the targeted complete-continuation attack.
Method: the same ForecastRollout algorithm, with its private model changed to lam 0.2, against Planner003(lam=0.2), in both assignments. Evidence: forecast-rollout-002-lam02-side0.json and side1.json with complete replays.
Result: two counter wins, 788:678, no errors, rejections, source drift or forecast mismatches. The chosen purchases are one tier2 in rounds 1 and 2, one tier3 in round 3, and one tier4 in round 10. Predicted final HP margins along these selected deviations are 24, 36, 50 and 110, consistent with the policy-improvement invariant. These matches take 32.6 and 33.7 seconds. The fixed schedule learned at lam 1 only wins by 24 HP against this target, so reoptimizing the timing matters.
Verdict: REFUTED for this exact known policy. This is still development evidence, not a reserved test or a general best-response proof.

## 2026-10-31T03:10:30Z: forecast transfer and a negative forecast-free ablation

Claim: the small forecast-defense opening only exploits the lead's particular Planner implementation.
Method: known_policy.py predicts explicitly frozen economy v4 (late_round=6, phi=0) and fortress v4 (defaults), with one tier2 purchased in round 1 and no later purchases. Recreating the economy callable preserves its only history flag because buildings cannot be removed: current turret ownership determines whether the opponent has ever owned a turret. Authoritative comparisons retain the target's ordinary persistent callable. Evidence: known-econv4-t2r1-001.jsonl and known-fortressv4-t2r1-001.jsonl, two assignments each.
Result: all four counter wins, 800:788, with every private forecast equal to the target's actual action list and no errors, rejections or source changes. Runtime about 9 seconds per economy match and 18 seconds per fortress match. The counter sees only public observations. Model family and parameters are fixed before the match.
Specs: bot_research.bots.counters.known_policy:@timing?model="econ_v4"&model_parameters={"late_round":6,"phi":0.0}&attack_round=1&tier="tier2"&count_cap=1&attack_share=1.0 ; for fortress, use model="fortress_v4" and model_parameters={} with the same attack settings.
Verdict: REFUTED as an implementation-specific limitation. These are targeted known-policy tests against development opponents, not proof of transfer to an unknown policy.

Claim: replacing exact forecasts by the frozen conservative threat builder preserves the stronger tier2 opening counter.
Method: confirm_opening_lock.py, 48 declared conditions: phi 0, 0.25 or 1; late_round 1 or 6; Planner003 lam 1, 0.5 or 0.2 and economy v2 late_round6/phi0; both assignments. Opening tier2 x1, reserve0, saturation round20. Evidence: opening-lock-001.jsonl and full replays.
Result: 12 wins and 36 losses, no errors, rejections or source changes. There are only 24 distinct full trajectory hashes; phi has no effect when late_round=1 and further conditions coincide. No setting in this grid beats Planner003 at lam1 or lam0.5. At lam0.2, phi0/late6 wins800:776 and phi0.25/late6 wins774:764. Against economy v2, every fully speculative setting wins800:788, while phi0 or0.25 before round6 loses. Thus neither blind defense spending nor simply buying the stronger opening unit is sufficient.
Verdict: REFUTED for this finite ablation. The successful forecast counter depends materially on its defensive allocation. Do not substitute OpeningLock for KnownTiming in the lead's counter pool.

## 2026-10-31T03:15:21Z: completed timing search and second policy-improvement pass

Claim: the default Planner003 is only vulnerable to small first-round pokes.
Method: search_forecast_timing.py completed the preregistered 324-condition development grid: model lam in {1, 0.5, 0.2}, attack round 2 through 10, pure tier2 through tier5, budget share 0.25, 0.5 or 1. The counter buys on that one round and otherwise forecasts defense and grows. summarize_timing.py checks coverage, duplicates, legality, forecasts and source stability. Evidence: forecast-timing-001-shard{0,1,2}.jsonl plus forecast-timing-002-shard{0,1,2}.jsonl, with summary forecast-timing-summary-001.json.
Result: 97 wins, 224 draws and 3 losses in player-0 screens; no errors, rejections, source changes or forecast mismatches. Only 71 distinct full trajectories occur, so 324 parameter settings do not mean 324 independent behaviors. At lam 1 and 0.5, an all-in tier5 purchase in round 8 wins 800:-40. At lam 0.2, all-in tier5 in round 7 or 10 wins 800:100. Twelve finalists selected by outcome, HP margin and earliest win are undergoing both-assignment confirmation.
Counter spec for the default target: bot_research.bots.counters.forecast_timing:@make?attack_round=8&tier=tier5&attack_share=1.0&model_lam=1.0.
Verdict: REFUTED on the completed screen. The large delayed-wave weakness is materially greater than the early poke weakness.

Claim: a second exact continuation-improvement pass can strengthen the extracted four-purchase schedule.
Method: ScheduledRollout explicitly includes the baseline action at every decision, then evaluates candidate deviations against complete continuations that retain the remaining baseline schedule. The baseline is one tier2 at rounds 1 and 5, one tier4 at round 9, one tier5 at round 12. Evidence: scheduled-rollout-001-iteration2.json and scheduled-rollout-001-iteration2-side1.json, with full replays.
Result: both assignments win 788:-3 by destroying the target in round 15, instead of the baseline's 800:528 round-50 win. The new schedule adds one tier1 in round 2 and one tier4 in round 10. The round-5 baseline tier2 is retained despite zero immediate damage gain, illustrating why the baseline must stay in the candidate set. Each selected complete-continuation value is nondecreasing. Forecasts are exact; no errors, rejections or source changes. Runtime is 78.2 and 79.2 seconds. This utility ranks outcome first and HP margin second, so it can trade 12 own HP for a much larger margin.
Verdict: CONFIRMED on the frozen default Planner003. A cheap extracted-schedule check is next; this is development search, not held-out validation.

Claim: removing the immediate-damage candidate filter improves the initial unit-purchase rollout on this target.
Method: matched single-unit candidate sets with and without the filter, empty baseline, frozen Planner003, player 0. Evidence: scheduled-rollout-002-unfiltered-unit.json and scheduled-rollout-003-filtered-unit.json. The unfiltered version considers one of every affordable tier even when its immediate damage gain is zero.
Result: both choose the same four-purchase schedule and win 800:528. Unfiltered runtime is 62.6 seconds; filtered runtime is 38.1 seconds. Both are legal, error-free, source-stable and exact in their forecasts. This one trajectory does not rule out useful zero-immediate-gain investments elsewhere.
Verdict: REFUTED for an improvement in this matched condition; OPEN as a general design question.

## 2026-10-31T03:18:00Z: independent opening certificate and completed counter confirmations

Claim: the proposed gun2 (3,2) plus nine-wall opening blocks every legal first-round attack under the standard balanced start.
Method: a standalone informal proof bounds every affordable roster by nine gun2 shots and shows the map gives nine consecutive covered route cells. An independently written budget recursion enumerates all 27 ordered rosters; verify_opening_certificate.py plays every roster in both assignments through the unchanged Engine, including construction actions. This checks every case on the engine, rather than relying on a fast simulator's worst-case selection. Inputs and proof are in experiments/validation/analysis/opening_certificate/; evidence is runs/validation/opening-certificate-001.json and 54 short replays.
Result: all construction and purchase actions are accepted, all 54 cases have zero incoming damage, and every spawned copy is killed. Cost 89, route length 22, covered indices 1 through 9, maximum required shots 9. Source hashes and input hash are recorded. The certificate does not establish minimum cost or good later-game economics.
Verdict: CONFIRMED. The lead can use this opening as a rigorously checked first-round option.

Claim: the selected timing wins and the second rollout schedule survive independent assignment and extraction checks.
Method: confirm_timing_finalists.py played both assignments of the 12 selected development conditions; confirm_recent_counters.py checked full coverage and compared saved full trajectories up to bot names. Evidence: forecast-timing-finalists-001.jsonl and recent-confirmations-001.json.
Result: all 24 timing confirmations win; both seats of round-8 all-in tier5 at lam 1 and 0.5 end 800:-40. The cheap six-purchase schedule reproduces each corresponding expensive second-pass rollout's full trajectory, action counts and history, winning 788:-3 in round 15 in about 4 seconds. Filtered and unfiltered unit searches likewise have equal full trajectories. All these matches are source-stable, legal and error-free with exact forecasts.
Counter spec for cheap second schedule: bot_research.bots.counters.known_policy:@schedule?model=planner003&schedule=[[1,"tier2",1],[2,"tier1",1],[5,"tier2",1],[9,"tier4",1],[10,"tier4",1],[12,"tier5",1]]. The round-8 tier5 counter remains simpler and has the larger HP margin.
Verdict: CONFIRMED within these exact known-policy conditions. Player-0 confirmations repeat screening conditions and do not add independent random samples.

Preliminary fortress v6 counter update: despite its cheap-threat insurance, current player-0 screens still lose to forecast-defended round-1 tier1 purchases (1, 2 or 6 copies) and one tier2. Six tier1 produce 800:770 so far. The paired confirmations and remaining grid are pending; no robustness conclusion is drawn from the earlier STRONG pool's absence of these newer counters.

## 2026-10-31T03:25:22Z: evaluation caution for the new timed defensive planner

Claim: the unchanged engine is deterministic, but a bot using wall-clock cutoffs need not be a deterministic function of its observation.
Method: source review of frozen defense v9 plan.py. plan_defense sets a deadline using time.time(); the gun-pass and wall-prefix loops stop when that deadline passes, retaining the best plan found so far. See _gun_pass and plan_defense, approximately lines 415 and 485.
Result: the available search prefix can depend on machine scheduling and cache warmth. The engine's determinism alone no longer justifies identifying all repeated v9 matches as identical conditions, or assuming an exact private v9 forecast from one evaluation of the same observation. I have not yet established a v9 input on which repeated default-budget actions differ.
Verdict: CONFIRMED that a wall-clock dependency is present; OPEN whether it changes actions or outcomes in the current tournament. Recommendation to the lead and defense lane: use a deterministic cap on candidate evaluations or search steps for reproducible final policies, and record any cutoff hits. Preserve the timed version as a separately identified variant if it is useful. Do not apply the exact-known-policy or timing-equivalence deductions to it without checking this hypothesis.

## 2026-10-31T03:28:34.648689+00:00: reproduced scheduler-dependent actions in frozen defense v9

Claim: the wall-clock cutoff can change the returned defensive plan and its damage outcome for an identical observation.
Method: probe_planner_deadline.py launches two fresh local processes calling the unchanged frozen v9 plan_defense on the standard initial observation, budget 100, against one tier3. In the second process only, the parent pauses its own child with SIGSTOP after 0.03 seconds, waits 3.3 seconds, then resumes it with SIGCONT. No engine or policy code is patched. Both returned plans are played through the original Engine. Evidence: runs/validation/planner-deadline-001.json, including inputs, actions, round records and source hashes.
Result: identical inputs give different actions. The ordinary call takes 0.0688 seconds and blocks all damage; the paused call takes 3.3541 seconds and leaks 26 HP. All returned construction actions are accepted. This controlled scheduling experiment proves a functional dependency on elapsed time; it does not estimate how often normal shared-machine load triggers it, or a full-match win rate.
Verdict: CONFIRMED. For deterministic final evaluation and known-policy forecasts, replace the wall-clock cutoff by a fixed search-work limit. If the timed variant is retained, record runtime conditions and deadline hits, and treat action equality or exact forecast claims as conditional.

## 2026-10-31T03:31:06.160865+00:00: completed fortress v6 opening checks and validation-runner hardening

Claim: adding a first-round splash turret closes the known-policy opening attack against fortress v6.
Method: 27 player-0 opening conditions cover default, round1="splash" and round1="gun2"; tier1, tier2 or tier3; caps 1, 2 or 200; full available attack share. KnownTiming forecasts the explicit target variant before defending. The splash/tier3 winner is then checked in both assignments. Evidence: fortressv6-opening-summary-001.json, its named input files and complete replays.
Result: default gives 6 wins and 3 losses for the counter; six tier1 win800:770, while one tier3 loses -431:774. With round1="splash", six tier1/tier2 parameter settings decline to attack and draw800:800; one tier3 wins788:748, confirmed in both assignments. With round1="gun2", all nine settings decline the zero-immediate-gain opening and draw800:800. This last result is a negative result for this purchase filter, not an exhaustive future-timing test. All recorded sources are stable, all forecasts match, and there are no errors or rejected actions.
Counter spec: bot_research.bots.counters.known_policy:@timing?model=fortress_v6&model_parameters={"round1":"splash"}&attack_round=1&tier=tier3&count_cap=1&attack_share=1.0.
Verdict: REFUTED for first-round splash. Later timing probes of gun2 and default are running.

Claim: final validation can freeze the relevant code while unrelated lane work continues and reject untracked loaded sources.
Method: the independent source_closure.py follows static imports and declared factory roots without executing bots. The final runner archives this closure plus exact configuration and scenario inputs. Each fresh match records sources at start and end; both must match the freeze. Synthetic tests cover missing, changed and unknown loaded sources; an end-to-end fixture plays two assignments in fresh interpreters. Evidence: source-closure-001.json, source-attestation-check-001/checks.json, frozen-match-check-001/checks.json and final-runner-check-002/checks.json.
Result: 9 closure checks, 7 attestation checks, 5 full-match checks and 12 artifact/scoring checks pass. The full-match fixture freezes22source files. The evaluator now emits end-of-match source hashes; earlier development rows did not, a limitation for retrospective dynamic-import auditing. No reserved opponent was used.
Verdict: CONFIRMED for the tested failure modes. Runtime-created code or undeclared non-source data requires a separate explicit dependency declaration.

Claim: exact action equality can remove redundant one-round timing games without estimating their outcomes.
Method: the standalone proof in analysis/timing_equivalence/PROOF.md assumes deterministic engine and opponent, a sole changed attack round, and identical relevant state evolution. The checker compared48already-played fortress opening/timing conditions against a no-purchase trajectory. Evidence: timing-equivalence-check-003.json and the proof's verification/evidence.json.
Result:24equal-action cases have identical complete trajectories;24different-action cases differ. Existing start-hash records match current recorded dependencies; three unrecorded lazy import files are explicitly listed. The first stronger retrospective check incorrectly required those unused/unrecorded static imports to occur in old start records and stopped; its diagnostic is retained as timing-equivalence-check-002.log. New searches freeze their full static closure and label each reused result as a deduction.
Verdict: CONFIRMED within the stated deterministic policy family. No added independent samples are claimed.

## 2026-10-31T03:37:58Z: delayed-wave counters to fortress v6, and a policy-identification pilot

Claim: fortress v6's insurance limits its known-policy exposure to the opening poke.
Method: 27 player-0 conditions vary attack round 2 through 10 and tier3 through tier5, with attack_share=1, count_cap=200 and the otherwise fixed KnownTiming continuation. Three distinct highest-ranked trajectories were then played in both assignments. Evidence: known-fortressv6-timing-001.jsonl and -002.jsonl; known-fortressv6-timing-summary-001.json; known-fortressv6-timing-confirm-001.jsonl, with complete replays.
Result: the screen has 18 wins and 9 draws, with 19 distinct full trajectory hashes. All six confirmations win in round 10: round-10 tier3 ends 740:-656, round-10 tier4 ends 800:-520, and round-9 tier5 ends 740:-460, written counter first. All forecasts match actual submissions; no bot errors, rejections or recorded source drift. Negative final HP is the engine's untruncated overkill value. The three conditions were selected using the screen, and the player-0 confirmations repeat those conditions.
Spec for the zero-own-damage counter: bot_research.bots.counters.known_policy:@timing?model=fortress_v6&attack_round=10&tier=tier4&attack_share=1.0&count_cap=200.
Verdict: REFUTED. The delayed-wave failure is much larger than the opening poke against this explicitly frozen version.

Claim: countering a public policy requires being told which policy is playing.
Method: identifying_counter.py starts with eight explicit policy hypotheses and eliminates a hypothesis when its predicted ordered building list, factory count or ordered new purchases disagree with the next public observation. A standalone proof establishes non-elimination of a fixed true catalogue member under exact deterministic reconstruction. Before identification the counter defends against all retained forecasts; its attack valuation is heuristic. A pilot compares this adaptive version with the same code given the target identity, against Planner003, fortress v6 and a snapshot of the lead's development v4. Evidence: identifying-counter-screen-002.jsonl. Snapshot lead_four_001.py has SHA-256 d7870f3b9a8bff3b47d227b25d74b3e7ef55782c60f8174980b22d1be29df46c, still equal to experiments/lead/v4.py at 03:36 UTC.
Result: all six pilot matches win legally without errors, source changes or incorrect true-model predictions. The adaptive version uniquely identifies each target by round 2 and ends 800:268, 800:422 and 800:240 respectively. The informed version ends 800:462, 800:-100 and 800:240. Different knowledge changes first-round defense and therefore later states; these are whole-policy ablations, not matched-state information-value estimates. The first pilot file, screen-001, is invalid because a tuple/list interface error caused bot exceptions; it is retained and excluded from strength evidence. The error was fixed before screen-002. Both-assignment checks on the full catalogue are now running.
Verdict: OPEN as a general claim; the pilot refutes it for these three catalogue members on player 0. This does not establish transfer to an unknown policy outside the catalogue.

## 2026-10-31T03:41:13Z: confirmed delayed attacks against the lead development v4

Claim: the current lead development v4 removes the large delayed-wave exposure of Planner003.
Method: snapshot lead_four_001.py (SHA-256 d7870f3b9a8bff3b47d227b25d74b3e7ef55782c60f8174980b22d1be29df46c), with its unchanged frozen-v7 planner dependency. Search attack rounds 1,3,5,7,9,11, every tier and attack shares 0.5/1.0, then confirm the three distinct highest-ranked trajectories in both assignments. Evidence: known-leadfour001-timing-001.jsonl, known-leadfour001-timing-summary-001.json and known-leadfour001-timing-confirm-001.jsonl, with replays. The 60-condition screen contains 11 played candidate matches, one separate baseline, and 49 exact action-equality deductions; the screen outcomes are 10 wins, 49 draws and one loss.
Result: all six confirmation matches win, at round 50. Round-9 tier5 with share1.0 ends800:380; round-9 tier4 with share1.0 ends800:500; round-9 tier5 with share0.5 ends800:660, counter first. Every forecast equals the target's actual action list, with no errors, rejections or recorded source changes. The paired matches agree after exchanging final player HP. These are selected development conditions, not held-out evidence or independent random trials.
Spec: bot_research.bots.counters.known_frontier:@timing?model=lead_four_001&attack_round=9&tier=tier5&attack_share=1.0&count_cap=200.
Verdict: REFUTED for this exact snapshot. The result does not assert anything about a later lead candidate. Reserved pools A and B remain unused.

## 2026-10-31T03:43:45Z: full-catalogue paired identification check

Claim: the adaptive finite-catalogue counter can identify and exploit multiple strong frozen policies without receiving their identities.
Method: all eight catalogue members, standard initial state, both player assignments, attack_from=6, attack_share=1.0, cost_penalty=0.1. Evidence: identifying-counter-confirm-001-shard0.jsonl, shard1.jsonl and identifying-counter-summary-001.json. The independent summary checks the complete replay after exchanging player labels and removing only names, initial descriptive metadata and global action-order annotations.
Result: 12 wins and 4 draws. All eight pairs have equal complete normalized trajectories. Every true policy becomes the unique retained member at round2; all current-round predictions match its actual actions throughout each match. There are no missing trace rounds, inner forecast exceptions, catalogue resets, bot errors, rejected actions or recorded source changes. Each outcome occurs once per assignment: Planner003 800:268, economy v4 and economy v4 with opening guard both800:800, fortress v6 default800:422, gun2 opening800:-216 at round10, splash opening800:-140 at round9, fortress v8 annealed25 800:610, lead development v4 snapshot800:240. All other games reach round50.
Spec: bot_research.bots.counters.identifying_counter:@make. The catalogue is fixed in identifying_counter.py; none of these eight opponents is a reserved final-test opponent.
Verdict: CONFIRMED on the stated catalogue. This is eight distinct paired trajectories, not sixteen independent samples or an unknown-opponent generalization result. Tests outside the catalogue and against policy switches are running. The abstract non-elimination proof does not imply these wins.

## 2026-10-31T03:46:04Z: independent route-range bounds and informed-counter ablation

Claim: the economy lane's maximum induced linear-forest sizes for the three gun ranges are correct.
Method: independent integer obstruction search, branching on degree-three obstructions or cycles, with memoized vertex subsets. The argument was written first in analysis/range_forest/PROOF.md. The algorithm differs from economy's vertex include/exclude search. Every returned witness is checked independently for degree and component edge counts. Evidence: range-forests-001.json and the proof's verification/evidence.json.
Result: ranges2.5,3,3.5 have maxima15,20,27. The searches finish after1857,37233,179357recursive calls, taking about0.01,0.29,2.24seconds respectively on one assigned CPU core. Input sets contain20,28,36cells, with exact integer radius tests. This confirms the geometry used by Theorem B; it does not certify floating-point arithmetic in guarantee.py or the rest of that theorem's implementation.
Verdict: CONFIRMED as exact finite computations with an informal correctness proof, not machine-checked formal certificates.

Claim: giving the target identity from round1 changes the identifying counter's performance.
Method: the same eight catalogue members, both assignments, fixed_id set to the actual target. Evidence: identifying-informed-confirm-001-shard0.jsonl, shard1.jsonl, identifying-informed-summary-001.json. All full paired trajectories agree after relabeling; all forecasts match and all runs are clean.
Result:16wins. Target HP, with own HP800 in every case: Planner003462, economy600, guarded economy660, fortress default-100(round10), gun2 opening-482(round9), splash opening-80(round8), annealed25 270, lead development v4 240. Remaining games endround50. The adaptive counterpart drew against the two economies and had smaller margins against most fortress variants, but a larger margin against Planner003. Knowing the target changes the opening and therefore the subsequent game state.
Verdict: CONFIRMED as a whole-policy ablation. It does not estimate information value at a matched state or establish that more information always helps the heuristic.

## 2026-10-31T03:47:33Z: registered opening-ablation hypothesis

Claim: spending the first-round budget on factories while still recording the catalogue's predictions can improve later offense enough to turn the two economy draws into wins. This permits bounded first-round damage against a blind attacker and makes no safety guarantee.
Method planned: identifying_opening.py replaces only the first own submission after the inner identifier has formed its predictions. All later decisions use the actual public state. The declared primary variant is opening=factories, against the same eight catalogue members in both assignments. No held-out opponents will be used. Alternative tier1/tier2/tier3 pokes are separately labeled ablations if run.
Result: not yet run.
Verdict: OPEN.

## 2026-10-31T03:51:11Z: periodic switching refutes out-of-catalogue robustness

Claim: resetting the catalogue after contradictory observations is enough to make the identifying counter robust to policy switches.
Method: eight declared stress opponents, both assignments: tier1 rush, tier2 rush, eco5 tier1, mixed5, economy-to-tier5 flood at round7, fortress-to-tier5 flood at round7, lead-v4-to-economy at round6, and economy/tier5-flood alternation with three-round phases from round7. Evidence: identifying-stress-001-shard0.jsonl, shard1.jsonl and identifying-stress-summary-001.json. These are separate development stress tests, not reserved opponents.
Result:14wins and2losses, eight distinct normalized trajectories, all paired trajectories equal after relabeling. The periodic switcher wins800:520 in both assignments. Its first unexpected tier5 flood is at round7; repeated contradictions lead to repeated catalogue resets. The counter's entire280damage occurs at round19, one round before its default saturation step. It ends that round with62752gold and872factories, so a lack of resources is not the direct explanation. No bot errors, rejections, inner model exceptions or source drift occurred. The other seven stress opponents lose, including the two single flood switches.
Spec: bot_research.bots.counters.catalogue_switch:@make?prefix=economy&after=archetype:eco6_t5&switch_round=7&period=3.
Verdict: REFUTED for this concrete switcher. Correct catalogue identification against fixed members is insufficient for this out-of-catalogue process.

Follow-up hypothesis: earlier saturation, at round10,12or15, prevents the delayed shock without changing the identification mechanism. The new declared development matrix saturation-ablation-001.json includes phase lengths2,3,4 in both assignments. Period3 is the observed failure;2and4 are new transfer conditions. This is an open empirical question until those runs finish.

## 2026-10-31T03:54:11Z: first-round growth completes the catalogue wins

Claim: keeping the online identification process but replacing its first own submission with five factories turns the two economy draws into wins.
Method: the previously registered opening=factories ablation, all eight catalogue policies and both assignments. Evidence: identifying-opening-factories-001-shard0.jsonl, shard1.jsonl and identifying-opening-factories-summary-001.json. Complete normalized replay comparisons, recorded predictions, actions and source checks were applied.
Result: 16 wins, eight distinct paired trajectories. Both economy outcomes change from 800:800 to 800:600 (unguarded) and 800:660 (guarded). Other counter-first HP outcomes are Planner003 800:462, fortress v6 800:-100 at round10, its gun opening 800:-482 at round9, its splash opening 800:-80 at round8, annealed25 800:270, and lead development v4 790:200. Unspecified games end at round50. Every true policy is uniquely identified at round2; all forecasts are exact, with no model exceptions, missing trace rounds, resets, rejected actions, bot errors or source drift. The lead-v4 opponent lands 10 opening damage, which the later offense outweighs in this matchup.
Spec: bot_research.bots.counters.identifying_opening:@make?opening=factories.
Verdict: CONFIRMED on this development catalogue. It does not establish safety or strength outside the catalogue. Seven outcomes match the identity-informed policy's final HP, but that equality alone does not identify a causal information effect.

Claim: fortress v6's blind gun opening blocks all the timing counters.
Method: a complete 180-condition timing parameter grid, with exact same-action trajectory deductions recorded separately. Evidence: known-fortressv6-gun2-timing-001/002/003.jsonl and known-fortressv6-gun2-timing-summary-001.json.
Result: 59 winning played conditions and 121 drawing conditions deduced identical to their no-attack baseline. There are 60 distinct raw trajectory hashes, including the baseline. The 59 played conditions consumed about974seconds; no action, forecast or source check failed. This grid is not 180 independent games. Selected paired confirmations are next.
Verdict: REFUTED on the stated grid; paired confirmation is pending.

Registered follow-up before execution: identifier-transfer-001.json compares the original identifier, factory-opening identifier, and factory-opening identifier with saturation at round12. It uses eight explicit development opponents: frozen fortress11 with two layouts, frozen economy6/economy7, the known period3 switcher, tier3 rush, eco6 tier5 flood, and the lead-v4 snapshot. This is a transfer and regression matrix of 48 paired conditions, not a reserved test. The two newer fortress policies contain wall-clock search limits, so paired trajectory equality will be measured rather than assumed.

## 2026-10-31T03:59:31Z: saturation ablation and two further paired checks

Claim: beginning saturation before round19 prevents the observed periodic-switch loss.
Method: 18 fresh-process matches from saturation-ablation-001.json, with saturation rounds10,12,15 crossed with switching phase lengths2,3,4 and both assignments. Complete source closures were frozen and archived; loaded source hashes were checked at match start and end. Evidence: saturation-ablation-001-shard0/1/2 and saturation-ablation-summary-001.json.
Result: each saturation setting records four wins and two draws. The period3 pair now draws800:800, replacing the original520:800 loss; phase lengths2and4 lose to the counter. All nine paired complete trajectories agree after player relabeling. No errors, rejected actions, source drift or missing jobs occurred. The three saturation settings have equal final outcomes; this is not evidence that they are interchangeable against other opponents.
Verdict: CONFIRMED for the declared matrix. Broader transfer is running.

Claim: the blind gun opening makes fortress v6 immune to timed purchases.
Method: three strongest distinct screened timing trajectories, replayed in both assignments on the unchanged engine. Evidence: known-fortressv6-gun2-timing-confirm-001.jsonl and its confirm-summary-001.json.
Result: all six are wins, with full paired trajectory equality, exact forecasts every round, no bot errors, rejected actions or source drift. Counter-first outcomes and timing parameters follow.
- {"attack_round": 12, "attack_share": 1.0, "count_cap": 200, "tier": "tier3"}: 740:-3308, round12.
- {"attack_round": 12, "attack_share": 1.0, "count_cap": 200, "tier": "tier4"}: 740:-2920, round12.
- {"attack_round": 12, "attack_share": 1.0, "count_cap": 200, "tier": "tier5"}: 740:-2700, round12.
Verdict: REFUTED. These are selected development counterexamples, not a win-rate estimate.

Claim: a separate initialized clone can exactly forecast the stateful identifying counter from the shared public observation history.
Method: the stateful_forecast proof was written before implementation. Two completed first-round tier1-cap1 timing conditions, one per assignment, use a separate local IdentifyingCounter object called exactly once per actual round. Evidence: stateful-forecast-opening-001.jsonl, its summary, and analysis/stateful_forecast/verification/evidence.json.
Result: both games draw800:800 at round50. All100 recorded round predictions match the actual target action lists; paired complete trajectories agree and actions/source checks are clean. The planned six-condition batch reached its540-second shell limit during the third match, whose incomplete replay is excluded; three further cases were not started. The two valid games took about179and203seconds.
Verdict: CONFIRMED for forecast correctness in these two games; the attempted counter does not beat the target. An adaptive private state alone does not prevent forecasting when its transition rule, initialization and observation history are public. No random or wall-clock-dependent policy is covered by this claim.

## 2026-10-31T04:00:27Z: exact rational audit of the attack certificate

Claim: the fractional-knapsack argument behind economy's Theorem B admits an exact, integer-valued damage certificate.
Method: wrote the standalone argument first in analysis/attack_certificate/PROOF.md, including the arrival cutoff, gun firing-window bound, splash/gun budget split, exact fractional knapsack and integer ceiling. Implemented an independent Fraction-based checker in attack_certificate.py. Generated101declared input cases and401legal construction responses, then measured the package's own arrivals with the unchanged combat_tick and spawn_schedule. Evidence: attack-certificate-001.json, its inputs file, and the proof's verification/evidence.json.
Result: no certificate exceeds any tested package damage, no source drift, all declared checks complete in about10.12seconds. This is finite support for the informal proof, not exhaustive response enumeration or a theorem-prover certificate.
Verdict: CONFIRMED under the proof's exact bundled-rule hypotheses.

Claim: economy frozen v6 guarantee.py returns an integer-valued float and computes the mathematical relaxation without upward numerical error.
Method: compare its value against the same bound with exact rational arithmetic, giving both implementations the same L_max.
Result:28of101outputs are noninteger;11lie slightly above the exact rational relaxation. A transparent example is one existing gun1 at(2,2), defender gold0, no prior active roster and package[tier4]. The exact relaxation is330/7, but the implementation returns47.142857142857146, exceeding the rational by3/985162418487296. Its sound integer ceiling from exact arithmetic is48; tested actual package damage is60. This example does NOT refute the claimed inequality against actual game damage. It refutes exact-arithmetic and integer-valued descriptions.
Verdict: REFUTED for those implementation descriptions; an actual game-damage violation was not found. For economy/lead review: use exact fractions or directed rounding before treating the computed number as a rigorous certificate. The independent checker is available without changing your files.

## 2026-10-31T04:02:20Z: registered extended-catalogue experiment

Claim to test: adding frozen fortress11, economy6/economy7 and five simple archetypes to the model catalogue can repair the transfer losses of the original eight-policy catalogue.
Method planned: frontier_identifier.py inherits the existing decision rule, adds those candidate models, and compares factory-only versus robust first-round defense, both with saturation from round12. The 24-condition declaration is frontier-identifier-001.json. traced_match.py will record which actual target hypotheses survive and whether their current actions match.
Scope: later fortress and economy plans contain wall-clock limits, so their predictions are explicitly heuristic. Exact elimination is not guaranteed to preserve these timed models. The new test is development reuse of disclosed opponents, not a held-out generalization claim.
Result: not yet run.
Verdict: OPEN.

## 2026-10-31T04:03:11Z: next timed-policy counter screen registered

Claim to test: a small forecast-guided opening attack or a delayed heavy wave can still exploit frozen fortress12 despite its finish-first fix.
Method planned: timed_frontier.py predicts that public policy by independently invoking the same factory on the reconstructed observation. The evaluator compares every predicted list to actual actions, without assuming determinism or reusing equal-action trajectories. The first screen will use rounds1,6,8,10, all five tiers, full attack share, cap200, and both assignments, split into bounded batches. Every condition is an actual original-engine game. Forecast mismatches will be reported separately from game validity.
Result: not yet run.
Verdict: OPEN.

## 2026-10-31T04:09:11Z: registered mixed-order counter search and timeout handling

Claim to test: a bounded search over mixed, ordered minion packages finds useful counters missed by pure-tier timed purchases.
Method planned: package_search.py starts from pure-tier controls, then tests two-tier mixtures and seeded legal mutations. Its stopping rule is an evaluation count, independent of wall-clock speed. mixed_timing.py uses only a copied public observation to predict frozen fortress12, chooses a package for one declared attack round, and otherwise follows the same forecast-defense and growth policy as the pure-tier counter. The first screen is rounds4,6,8,10, both assignments,192 package evaluations, seed0, share1, cap200. Forecast mismatches will be reported; a local search score is not an authoritative match outcome.
Result: not yet run.
Verdict: OPEN.

Evaluation correction: the transfer runner's remaining batch time could shorten a match deadline. The recorded case0045 limit was114.565seconds, while case0028/29 reached180seconds. These are computational failures, not losses. New run_long_development.py starts a match only when its full configured timeout fits. The original artifacts are retained. The declared retry manifest repeats factory-opening and factory-opening/saturation12 against eco6_t5, both assignments, with450seconds per match. audit_development_campaign.py retains every attempt and selects the earliest valid completion of each original condition; retries never inflate the number of conditions.

## 2026-10-31T04:11:20Z: partial transfer audit and package-search checks

Claim: the factory-opening improvement transfers beyond the original fixed catalogue.
Method: all48 declared jobs were attempted with fresh processes, frozen source closures and start/end source checks. Evidence: identifier-transfer-summary-partial-001.json, produced by audit_development_campaign.py.
Result so far:44 valid completions and4 explicit timeouts. Original identifier:6wins,2draws,8losses over16conditions. Each factory-opening variant:12wins,2losses over14valid conditions; each has2unresolved eco6_t5 games. No completed match has bot errors, rejected actions or source drift. The four timeouts are excluded from outcomes and are being retried under a450-second limit. The two factory variants must not yet be reported as16-game results.
Verdict: OPEN for the full matrix; partial transfer improvement is observed.

Claim: package_search.py obeys its search and action constraints and reports correct combat scores on selected boundary cases.
Method:24 legal map/budget/active-prefix conditions, including zero gold,249/250 prior entries, and budgets up to30000. Repeat each seeded search; verify its chosen package against unchanged simulate_map and compare its score with the included pure-tier controls. Evidence: package-search-check-001.json.
Result: all24pass, no source drift,3.66seconds. Every chosen package is within budget and count cap, every predicted damage matches the original combat result, and no search result scores below its pure-tier controls. These are tests of the search mechanics, not game strength or global optimality.
Verdict: CONFIRMED for these checks.

## 2026-10-31T04:14:41Z: final-validation source checks strengthened

Claim: a result is sufficiently source-attested when both reported source maps are merely subsets of the frozen source closure with matching hashes.
Method: code review found that an empty map, or a map omitting a required engine file, could satisfy that earlier check. Added required_sources.py and a separate final_validation_strict.py runner, preserving earlier frozen experiments. The stricter runner requires both declared bot entry modules and the core engine/evaluator files in both attestations. It retains the earlier unknown-file and hash-mismatch rejection.
Result: 13 synthetic tests passed, covering valid evidence plus missing, empty, changed, unknown, omitted-engine and omitted-bot attestations at both match boundaries. Two fresh-process development fixtures passed all five integration checks with 24 archived source files. All 44 completed transfer artifacts also pass the stronger retrospective check. Evidence: required-source-check-001, frozen-strict-check-001, transfer-strict-source-audit-001.json.
Verdict: REFUTED for sufficiency of the old schema check; CONFIRMED for the stated new tests. This was a validator gap, not evidence that any completed game had missing source data. The reserved pools remain unused. Use final_validation_strict for the eventual frozen candidate.

## 2026-10-31T04:15:17Z: computational limit of catalogue resets

Claim to test: the original eight-model factory-opening identifier completes the eco6_t5 transfer games within a modest match time.
Method: preserve the initial 180-second failures and run separate 450-second attempts. At a progress inspection, the first longer attempt had reached only round 20 after several minutes. The opponent's first tier5 purchases contradict the fixed catalogue, causing repeated resets and repeated expensive policy simulations on increasingly rich states.
Result: the long attempts are still running, so there is no final game outcome to report. This is already a material runtime limitation of the eight-model implementation. The extended catalogue contains eco6_t5 and can avoid that specific repeated-search path, but it is a different policy.
Verdict: OPEN for final outcomes; the slow execution is observed. If the 450-second attempts fail, a detached batch will allow up to 900 seconds per match, retaining every earlier failure. Such retries will not add independent conditions.

## 2026-10-31T04:20:21Z: catalogue expansion and exact-certificate follow-up

Claim: expanding the model catalogue repairs all transfer losses while keeping the original decision rule.
Method: all24 declared frontier-identifier-001 conditions, six development opponents, two openings and both assignments; original-engine outcomes and full normalized replays. Separate diagnostic audit checks every forecast trace. Evidence: frontier-identifier-summary-001.json and frontier-identifier-diagnostics-001.json.
Result: factory opening10wins2draws, defensive opening4wins6draws2losses. The factory version draws against economy7 and wins the other five pairs. The defensive version loses both fortress11 games despite exact target forecasts. All12 paired trajectories match completely. No errors, rejections, source drift, missing jobs or model exceptions. All20 games against named fixed catalogue members have exact target predictions; the four games against the periodic switcher reset and sometimes have no matching forecast.
Verdict: CONFIRMED for removal of losses by the factory-opening variant on these six disclosed opponents, REFUTED for the defensive-opening variant. Catalogue coverage alone does not guarantee effective action choice. Timed policy replicas happened to agree here; this does not remove their wall-clock nondeterminism.
Specs: bot_research.bots.counters.frontier_identifier:@make?opening=factories&saturate_round=12 and the same with opening=robust.

Claim: economy's revised Fraction-based certificate agrees with the independent exact relaxation.
Method: the economy lane adopted the arithmetic change at04:12 after the earlier audit. Compare its live guarantee.py against all101 preserved independent cases with the same proven route-length bound; also check its zero-gold exact-simulation branch against the original combat measurements. Evidence: revised-guarantee-check-003.json and log.
Result: all101 integer bounds agree with the independent values at the same L_max, no tested combat-bound violation, no source drift. Zero-gold exact branches also agree with the measured package damage. An initial checker run failed before evaluation on a list/set conversion; a second incorrectly required the default zero-gold route bound to equal the looser general bound. Seven differences were explained by the valid shorter current route when no construction is affordable; correcting that comparison produced the passing third check. Earlier diagnostics are retained with local path prefixes removed.
Verdict: CONFIRMED for the stated regression cases. This is independent verification of the Opus economy lane's repair, not new exhaustive construction-response enumeration.

Runtime update: both450-second attempts of factory_identifier versus eco6_t5 timed out, with no final result. Original failures remain excluded from outcomes. The detached900-second retry batch is running; its successful process start was verified, after an initial background launch did not survive shell exit. No game result was produced by that initial launch.

## 2026-10-31T04:23:50Z: one-way model-falsification fallback registered

Claim to test: once all retained catalogue models contradict observed purchases, permanently switching to one strong general policy reduces the repeated-catalogue runtime and improves transfer to unknown opponents.
Method planned: falsification_fallback.py wraps the factory-opening identifier and switches to frozen economy9 or fortress13. The 12-condition falsification-fallback-001.json manifest crosses those variants with eco6_t5, the period3 switcher, and the known lead-v4 snapshot, both assignments. The last opponent checks the no-switch regression property. The informal controller argument was written first in analysis/falsification_fallback/PROOF.md. It proves trajectory preservation only for an exact fixed catalogue member; after a switch it proves zero further catalogue calls, not fast execution or good decisions by the fallback.
Result: not yet run. A companion replay_audit.py now reconstructs every recorded round from its actions using the unchanged Engine; its fault-injection checks are also pending a free core.
Verdict: OPEN.

## 2026-10-31T04:26:43Z: mixed-package results and complete replay verification

Claim: the declared 192-evaluation package search finds winning timed attacks against frozen fortress12.
Method: all8 declared conditions (rounds4,6,8,10, seed0, both assignments), with every condition played separately. Compare target predictions with actual submissions. Independently re-execute all saved action lists using the unchanged Engine and compare every record, rollup and terminal result. Evidence: fortress12-mixed-timing-001.jsonl, its summary, and fortress12-mixed-replay-audit-001.json.
Result:6wins2draws, four paired complete trajectories, no forecast mismatches, missing traces, errors, rejections or source changes. Counter-first outcomes: round4 draw800:800; round6 win800:654 using [tier4,tier4,tier3], cost620; round8 win740:316; round10 win800:-460 using nine tier5, cost5850. All eight original-engine replay audits pass. This is a selected timing grid, not a win-rate estimate. The round10 result uses a pure-tier package, so it does not establish a benefit from mixing. The matched pure-tier screen is still running.
Verdict: CONFIRMED on these declared development conditions; the incremental value of mixed search over pure-tier choices remains OPEN.

The independent replay checker rejects12 injected corruptions and accepts its intact fixture (replay-audit-check-001.json). The fallback controller passes seven regression/branch checks (falsification-fallback-check-001.json); its actual matches are running. The next declared challenge is fortress15-forecast-001.json, ten games against the later finish-rule and foreign-map revision. It will test mixed packages at6/8/10 and pure first-round tier1/tier2. The generic public_factory counter makes its target factory explicit, and forecast_match records prediction mismatches. Reserved pools remain untouched.

## 2026-10-31T04:31:31Z: falsification fallback and independent replay results

Claim: permanently leaving a contradicted catalogue can improve adaptation to the two declared unknown-opponent tests while preserving the known-member trajectory.
Method: the twelve predeclared conditions in falsification-fallback-001.json, with fresh processes, both assignments and frozen sources. Audit every round's controller trace and re-execute all recorded actions through the unchanged Engine. Evidence: falsification-fallback-summary-001.json, falsification-fallback-audit-001.json and falsification-fallback-replay-audit-001.json.
Result: the fortress13 fallback wins all six games. Against eco6_t5 it switches at round3, wins100:-45 in round8, and completes in about2.2 to2.4seconds. Against the period3 switcher it switches at round8 and wins800:-136 in round12. Against lead_four it never switches and wins790:200 in round50. The economy9 fallback has four wins and two draws: eco6_t5 ends in mutual destruction at round8 with HP -40:-85, which the engine correctly scores as a draw; the switcher loses800:-68 in round14; lead_four has the same unswitched trajectory. All six paired conditions have matching complete trajectories. Four known-member games exactly reproduce the original factory/saturation12 identifier's canonical replay. All twelve replay audits pass, with no invalid actions, bot errors or source changes. The traces show zero further catalogue calls and one fallback call per decision after switching.
Verdict: CONFIRMED on these conditions. This is not a universal runtime or recovery guarantee. The original identifier's eco6_t5 games remain unresolved under longer deadlines, so no completed-outcome comparison against that original is claimed.

Reusable spec for the stronger tested fallback: bot_research.bots.counters.falsification_fallback:@make?fallback=fortress13&opening=factories&saturate_round=12. It deliberately uses frozen fortress13, not the later fortress15. A direct-fortress control and further delayed behavior changes are needed to distinguish the value of identification from the strength of the fallback itself.

## 2026-10-31T04:31:31Z: delayed-departure control experiment registered

Claim to test: catalogue adaptation followed by one-way fallback provides value beyond simply using the fallback from the start, and survives later changes in a previously identified opponent.
Method planned: falsification-camouflage-001.json declares54 games: three candidates (fortress13 fallback, direct fortress13, and the extended factory-opening identifier), nine opponents, both assignments. Opponents follow economy, fortress, or lead_four exactly until a declared switch, then permanently use a public archetype: round3 to tier3 rush, or round7/10 to economy-then-tier5. The change is not visible in the current round's observation. No reserved profiles or scenarios are used. Report timeouts separately and retain all attempts.
Result: registered before execution.
Verdict: OPEN.

## 2026-10-31T04:33:54Z: finite-policy game audit registered

Claim to test: the lead's complete c2rr1 round robin contains a useful exact policy-mixture certificate, even if no single policy is robust to the whole listed pool.
Method planned: independently replay all110 recorded games with the unchanged Engine, require consistent policy version identities, and construct the exact11-policy payoff matrix by averaging both assignments. An optimizer may propose a mixture; a separate Fraction-only checker must verify normalization and every column payoff. The informal finite-game argument was written first in analysis/finite_metagame/PROOF.md.
Scope: a certificate applies only to this empirical table and requires the sampled component to remain unknown while the opponent selects its policy. It is not a full-game solution or a robustness result against new counter-strategies. This tests and sharpens the defense lane's suggestion that policy mixing may address counter cycles.
Result: not yet run.
Verdict: OPEN.

## 2026-10-31T04:38:54.317058+00:00: independently certified finite-policy mixture

Claim: the complete c2rr1 empirical game has a policy mixture with nonnegative payoff against each of its eleven policies, although every pure policy has a losing matchup.
Method: re-execute all110 original games through the unchanged Engine, check every recorded round and result, require both assignments per pair and consistent recorded policy versions. Construct exact rational payoffs (win1, draw0, loss-1). Use a numerical optimizer only to propose probabilities, then check every constraint with a separate Fraction-only checker. Evidence: metagame-matrix-001.json, metagame-certificate-001.json and metagame-certificate-check-001.json.
Result: all110 replay audits pass. The certificate assigns probability1/3 to poke_lock(opening_units=1,reserve=0,phi=1,saturate_round=20), 1/3 to eco6_t5, 1/6 to frozen fortress4(attack_from=6,attack_share=0.5), and 1/6 to economy.timing. Every column payoff is nonnegative and the exact finite-game value is zero. Every pure policy has minimum payoff-1. This verifies the defense lane's suggestion only for this finite table. The first replay-audit attempt rejected the lead's extra initial metadata; after explicitly validating that metadata, the full second attempt passed.
Verdict: CONFIRMED for the recorded empirical table. An opponent may know the distribution but must choose its policy without knowing the sampled component. New opponents, changed policy versions and new starting states are outside the certificate.

Follow-up registered before execution: metagame-transfer-001.json crosses three newer fixed policies (fallback fortress13, direct fortress15, direct economy9) with each of the four support components, both seats, 24games. Weighted component outcomes will test transfer beyond the certified table. A current-source comparison is preserved separately; differences require qualification before interpreting this as the same policy mixture.

## 2026-10-31T04:42:43Z: fortress15 counter audit completed

Claim: the revised fortress15 remains vulnerable to public-policy timing attacks.
Method: all ten predeclared fortress15-forecast-001 conditions, both assignments, fresh processes and frozen sources; check each forecast against the actual submitted action list and independently replay every game. Evidence: fortress15-forecast-audit-001.json and fortress15-replay-audit-001.json.
Result: eight counter wins, two losses, five identical paired trajectories, no errors, rejected actions, missing predictions, prediction mismatches or source changes. Counter-first HP: mixed-search round10 wins800:-40 at round10; round8 wins800:480; round6 wins800:714; pure first-round tier1 loses486:770; pure first-round tier2 wins778:776. The latter margin is only two HP. All ten replay audits pass. The round10 package is six tier5, cost3900, with840 damage: this is a pure package selected by the mixed search.
Verdict: CONFIRMED for these development conditions. The broad tuning results in the defense lane do not establish robustness to a public-policy counter.

The round10 replay shows the mechanism. After round8, the counter has148 factories and2256 gold, fortress has33 factories and542 gold. Fortress spends round9 building nine splashes and round10 adding eight more, but all six tier5 still arrive. The counter uses its public forecast to defend economically against fortress's earlier purchases. These state values explain this one failure; they do not prove a globally optimal economic schedule.
Reusable spec: bot_research.bots.counters.public_factory:@mixed?attack_round=10&evaluations=192&seed=0&attack_share=1.0&count_cap=200 (the default public target is frozen fortress15). Pure-control reproduction uses @timing with attack_round=1 and tier=tier2.

Next hypothesis: compiling the exact public observation/action trajectory can reproduce the round10 win without evaluating the opponent's policy during play. A structural observation guard and permanent fallback will be tested separately. The informal argument is in analysis/compiled_policy/PROOF.md; no transfer or runtime result is claimed yet.

## 2026-10-31T04:49Z Compiled public trajectory registered for fresh testing

Claim: a fixed action table guarded by exact public observations can reproduce a known development counter without simulating the target's decisions during play. Method: `analysis/compiled_policy/PROOF.md` states the deterministic-opponent and exchange-equivariance hypotheses and proves the claim by induction. Its application to the timed fortress policy is conditional; fresh games are still needed. `compile_plan.py` first replayed `fortress15-forecast-001/results/case0000.json` with the unchanged engine, then compiled all ten pre-decision observations and our submitted actions to `bots/counters/plans/fortress15_r10.json` (SHA-256 `a8dd92f89079c516b5a516b8fe22049b32fff26a679836b0a06fcd9c5c2c8720`). `compiled_plan.py` compares complete normalized observations, including rules, before using an action list. On the first mismatch it permanently switches to a separately specified fallback.

Result: seven guard checks pass, including both player assignments, renamed labels, returned-action isolation, changes to HP/gold/factories/rules, and wrong data digest. Evidence: `runs/validation/compiled-plan-check-001.json`. Fresh-game strength remains OPEN. Registered `experiments/validation/compiled-transfer-001.json`: 42 standard development conditions, compiled plan with fortress15 fallback, compiled plan with idle fallback, and direct fortress15, each versus frozen fortress15/13, economy9, factory/sat12 frontier identifier, eco6_t5, poke_lock and lead-four snapshot, both seats. The data file is an explicit frozen input to `run_data_development.py`. No reserved opponent is used.

## 2026-10-31T04:51:50Z Fortress17 roster-wrap off-by-one, independently reproduced

Claim: `defense/frozen/v17/plan.py:wrap_bundles` puts the first heavy copy at spawn tick zero. Verdict: REFUTED. The code sets `pad = ticks*m - n_visible - 1`. With zero-based roster indexing, the first appended heavy copy has index `n_visible + pad`, hence spawn tick 249. The least nonnegative padding for tick zero is `(-n_visible) % ticks`. Adding only one to the current formula still wastes a full cycle when the visible count is already a multiple of 250.

Method and result: `experiments/validation/check_roster_wrap.py`, unchanged combat engine, frozen v17 source hashes in `runs/validation/roster-wrap-check-001.json`. This is a synthetic component state, not a complete standard-start game. Defender map is the full default layout with the nine greatest-adjacency cells as splashes and the remaining layout cells as walls; all construction actions are legal. Route length is 78 and per-copy splash damage 610. Attacker has 200 active tier1 copies and 1400 gold. All 13 sampled compositions cause zero damage, so `plan_defense` returns no construction. The affordable unsampled purchase `tier1*50 + tier5` costs exactly 1400 and deals 140 base damage: its tier5 has index 250 and spawns at zero. The helper instead supplies `tier1*49 + tier5`, with the heavy at index 249, too late to arrive.

For hrt-w1 and the lead: this is a concrete sampling omission and indexing repair, not evidence that the current full bot necessarily reaches the component state. The standalone argument and exact hypotheses are in `analysis/roster_wrap/PROOF.md`. An empirical win against fortress17 remains OPEN. The policy docstring's description of speculative protection against every affordable bundle is also stronger than the actual sampled threat set.

## 2026-10-31T04:51:50Z Old empirical equilibrium does not transfer to new opponents

Claim: the four-component c2rr1 equilibrium mixture remains non-losing against later policies. Verdict: REFUTED for the declared development conditions. All 24 actual standard-start games in `metagame-transfer-001` completed, both player assignments for three candidates against four mixture components. Fortress15 wins all 8, giving exact mixture payoff +1; the fortress13 falsification fallback has 6 wins and 2 draws, payoff +5/6; economy9 has 6 wins and 2 losses, payoff +1/3. Payoffs use win=1, draw=0, loss=-1, component weights 1/3,1/3,1/6,1/6 and equal seat weights. All component source dependencies match their original recorded versions. All 12 seat pairs have equal normalized complete trajectories.

Evidence: `runs/validation/metagame-transfer-audit-002.json` (strict source/outcome and rational-weight audit), `metagame-transfer-replay-audit-001.json` (24 unchanged-engine replay checks, all passed, 15.810 seconds). No errors, rejected actions, failures or source drift. The first audit invocation wrongly required every static conditional import to be loaded in every game. It stopped on an unimported `frozen/v4/simulate.py`; the corrected audit requires its frozen bytes to match and checks loaded bytes whenever imported. No game result was changed. The original exact equilibrium certificate remains valid only for its original 11-policy table.

## 2026-10-31T04:55:07.877089+00:00 Mixed attack optimization versus complete-game margin

Claim: maximizing predicted damage on the purchase round also maximizes the eventual HP margin. Verdict: REFUTED on the matched fortress12 development conditions. All 40 pure-tier games completed (18 wins, 20 draws, 2 losses), with both assignments for each of 20 settings. The 8 previously completed mixed-search games have 6 wins and 2 draws. Forty pure games independently replayed on the unchanged engine in 23.715 seconds; all passed.

Method: compare rounds 6, 8 and 10, all five pure tiers versus the 192-evaluation mixed search, with the same initial state, attack share 1, cap 200 and continuation controller. Full observations and own actions agree before the purchase; actual target actions agree on the purchase round. The mixed search weakly beats every pure control on its predicted immediate-gain objective in all six paired comparisons.

| Purchase round | Mixed immediate gain | Mixed final HP | Best pure tier by final margin | Pure immediate gain | Pure final HP |
| --- | ---: | --- | --- | ---: | --- |
| 6 | 146 | [800, 654] | tier5 | 140 | [752, 520] |
| 8 | 484 | [740, 316] | tier5 | 280 | [800, 240] |
| 10 | 1260 | [800, -460] | tier5 | 1260 | [800, -460] |

Both assignments agree. The resulting mixed-minus-best-pure final margins are -86, -136 and 0. This does not show that pure-tier policies are generally better; it shows that the one-round objective can select a worse continuation. Evidence: `fortress12-pure-summary-001.json`, `fortress12-pure-mixed-comparison-001.json`, `fortress12-pure-replay-audit-001.json`. The 40 pure games have only 11 distinct normalized trajectories; they are not 40 independent samples.

## 2026-10-31T04:55:33Z Fortress17 transfer challenge registered

Claim to test: fortress15's successful mixed round-10/round-8 attacks and first-round tier2 purchase still beat the lower lethal-defense threshold in frozen fortress17. Method: six fresh standard games in fortress17-forecast-001.json, all three conditions in both assignments, with the public model factory explicitly set to fortress17. These are development conditions selected from earlier successes, not held-out validation. Verdict: OPEN until the games and replay audits complete. The separate roster-wrap component counterexample is not used to infer an outcome here.

## 2026-10-31T04:59:07Z Completed camouflage test and next compilation question

Claim: the declared delayed-switch opponents expose a win-rate difference between the original identification fallback, its direct defensive fallback, and the extended identifier. Verdict: REFUTED for this test. All three policies win all 18 games against the nine `falsification-camouflage-001` opponents. All 27 player-assignment pairs have equal complete normalized trajectories; there are 26 distinct trajectories across the 54 games. Strict source/outcome checks and all 54 unchanged-engine replay checks pass (replay runtime 3.020 seconds). Evidence: `falsification-camouflage-audit-001.json`, `falsification-camouflage-replay-audit-001.json`. These are selected development opponents, not an estimate of performance against arbitrary adaptive policies.

There are substantial state and runtime differences despite equal outcomes. Against lead-four switching to the economy-six flood at round10, the fortress13 fallback wins with own HP370, the direct fortress13 wins with own HP790, and the extended identifier wins with own HP650. Against the same prefix switching at round7, those surviving HP values are650,230,790. These examples refute an ordering by surviving HP within this small test. Negative terminal opposing HP contains overkill, so raw final margins alone are a poor way to compare these wins.

Next question, still OPEN: can several measured counter trajectories be compiled into a compatible public-observation library, eliminating repeated opponent-policy simulation while retaining each supported win? The proof and exact pairwise conflict criterion are in `analysis/compiled_library/PROOF.md`. A finite conflict-graph search will select compatible plans explicitly; no claim of optimal strategic coverage follows from maximizing the number of stored plans.

## 2026-10-31T05:10:59.961573+00:00 Fortress18 sampler repair and a distinct large-roster pruning failure

Claim: the corrected wrap sampler includes the missed tier5 at index250. Verdict: CONFIRMED. On the earlier synthetic fixture with200 active tier1 entries and1400 attacker gold, v18 includes50 tier1 followed by one tier5; the first heavy spawn is now tick0. Eleven boundary counts from0 through749 likewise place the first heavy at phase0. The helper still pads250 when the visible count is already divisible by250, but the ordinary pure-tier sample covers the immediate heavy purchase in those cases; no further omission is claimed from that detail.

Claim: excluding the gun search whenever a sampled roster exceeds120 entries is harmless. Verdict: REFUTED by a legal-construction component fixture. Keep the original full59-cell map with nine splashes and set defender gold/budget to1000. Frozen v18 samples the140-damage threat but buys only two splashes at(10,10),(11,10), cost120, and still takes140 damage. Two gun3 turrets at(10,8),(11,8), cost400, instead stop all13 sampled compositions on the unchanged engine. Of six initially legal gun3 locations and their fifteen pairs, six pairs stop all13 samples. None of the six single gun3 additions stops the specified threat.

Method and scope: `check_roster_wrap_repair.py` and `search_wrap_defense.py` build the map through accepted original-engine actions, then use original combat for every outcome. The proof, exact geometry and limitations are in `experiments/validation/analysis/large_roster_pruning/PROOF.md`; evidence is `runs/validation/roster-wrap-repair-004.json` and `roster-wrap-defense-search-001.json`. This is a synthetic component state, not an asserted standard-start match against the full default bot. The source guard `GUN_PASS_MAX_ENTITIES=120` skips guns because even harmless cheap entries count toward the cap. A useful repair should reason about survivors or selectively test guns, without restoring unbounded search on every huge roster. Earlier diagnostic failures001-003 are retained;004 is the completed check.

## 2026-10-31T05:11:37.526109+00:00 Compiled counter policy: exact reproduction, useful fallback, limited transfer

Claim: a fixed public trajectory can replace online forecasting on that trajectory. Verdict: CONFIRMED for the fresh games below, with the conditional general argument in `experiments/validation/analysis/compiled_policy/PROOF.md`. The compiled fortress15 round-10 win reproduces the entire source game against both frozen fortress15 and fortress13, in both player assignments and with either fortress15 or idle fallback: eight fresh games end800:-40 in round10, and all eight complete normalized trajectories equal the source. The source's counter decision time was 3.028587 seconds. One fresh compiled counterpart took0.003035 seconds across ten decisions. This is an observed runtime reduction, not a calibrated benchmark; construction and import time are excluded.

The seven-opponent development comparison planned42 games. Forty completed and passed strict source checks plus complete unchanged-engine replay; all20 completed seat pairs have equal normalized trajectories. Compiled policy with fortress15 fallback:10W,0D,2L, plus two120-second timeouts against the frontier identifier. Compiled policy with idle fallback:4W,2D,8L. Direct fortress15:4W,6D,4L. The two incomplete matches are unresolved, not wins, losses or draws. Against economy9, both the compiled policy with defensive fallback and direct fortress15 lose. Against lead_four, the compiled policy switches at round4 and wins800:660; direct fortress15 draws790:790. Against poke_lock, the round2 fallback wins800:660 versus the direct policy's795:790. Thus fallback behavior and the state inherited at departure matter. There is no universal dominance conclusion.

Evidence: `runs/validation/compiled-transfer-audit-001.json`, `compiled-transfer-replay-audit-001.json` and the immutable42-condition manifest. Fixed plan data SHA-256 is `a8dd92f89079c516b5a516b8fe22049b32fff26a679836b0a06fcd9c5c2c8720`.

Claim: all ten collected winning trajectories can be combined into one deterministic history library. Verdict: REFUTED for exact reproduction. Their conflict graph is K8,2: every old-catalogue trajectory starts with five factories, while both newer fortress counter trajectories require a different first action list under the same initial observation. All16 conflicts occur at round1. Exhaustive enumeration of1024 subsets selects the compatible old eight. This obstruction concerns exact trajectory reproduction, not the possibility of winning all ten matchups by another policy.

Claim: the compatible library preserves its source outcomes and transfers broadly. Verdict: source preservation CONFIRMED; broad transfer REFUTED on this development set. The28 fresh games give20W,0D,8L. All16 source-opponent games reproduce their complete stored trajectory without fallback. The12 additional games give4W,8L: wins against eco6_t5 and alternate3, losses against fortress15, fortress17, economy9 and economy13. All14 seat pairs agree; all28 guard traces and complete original-engine replays pass. On the eight source games with the compiled policy in seat0, cumulative decision times range 0.002047 to 0.045918 seconds per game, compared with 0.563604 to 16.562347 seconds in their original online-forecast source runs. Again these are uncalibrated observations excluding constructor time.

Library spec: `bot_research.bots.counters.compiled_library:@make?data_file=bot_research/bots/counters/plans/catalogue_and_fortress_001.json&data_sha256=8f91ae2567988d828efb4fb6999abbbeab7c2becc8701d04f05cbeac9afe2dbe&fallback=fortress15`. The data contain only the selected old eight despite the filename. Evidence: `compiled-library-build-001.json`, `compiled-library-check-001.json` (23 checks), `compiled-library-audit-001.json`, and `compiled-library-replay-audit-001.json`. These are development experiments; reserved pools A and B remain unused.

## 2026-10-31T05:11:37.526147+00:00 Identifier transfer with longer timeout accounting

Claim: raising the fallback saturation threshold permits the two slow eco6 games to finish. Verdict: CONFIRMED for saturation12. The final merged audit covers46 of48 planned development conditions, retaining every failed attempt separately. Base identifier:6W,2D,8L. Five-factory identifier:12W,0D,2L plus two unresolved eco6_t5 games. The latter both still time out at900 seconds after earlier120- and450-second limits. Five-factory identifier with saturation12:14W,0D,2L; its two eco6_t5 games complete in approximately305 and350 seconds and win520:-26920. Negative HP includes terminal overkill and is not a useful unbounded quality score.

All23 completed seat pairs have identical normalized trajectories. Strict result/source audit: `runs/validation/identifier-transfer-final-audit-001.json`; the two newly completed long games also pass `identifier-transfer-long-replay-audit-001.json`. The other44 games were already replayed in earlier audits. There are eight failed attempts across four conditions, of which only two conditions remain unresolved. Repeated attempts do not create additional strength samples. This closes the declared transfer matrix as partial evidence rather than silently dropping its slowest cases.

## 2026-10-31T05:12:52.818419+00:00 Early-attack challenge of the lead setting registered

Claim to test: the robust, big_threat=100, poke_insurance=False, gun_cap=120 lead v7 setting withstands round-one attacks as well as its later timing screen. Verdict: OPEN. An unmodified snapshot is in `bot_research/bots/counters/snapshots/lead_seven_001.py`, SHA-256 `86c6cc6342bef0360e64b3087d453e157a005cf73824ca4166b01e4d9f4bc19f`. The manifest `experiments/validation/lead-seven-early-001.json` declares eight counters and both assignments, including mixed round-one buys, three tier1 budgets, tier2/tier3 full buys, and the known round-three tier3 control. Public prediction traces will distinguish model mismatch from strategic failure. This is development work and does not open the reserved pools.

## 2026-10-31T05:14:26.151227+00:00 Targeted fortress15 counters remain effective against v17 and v18

Claim: the v17 lower lethal threshold and v18 wrap/final-round changes stop the earlier round10 and round8 mixed-timing attacks. Verdict: REFUTED on these fixed development conditions. Against each frozen version, mixed round10 wins800:-40 in round10; mixed round8 wins800:480 at the horizon. The early tier2 round1 counter also wins778:776. Each condition was played in both assignments. All six v17 games and all six traced v18 games have zero prediction mismatches, bot errors, rejected actions or source drift, and every original-engine replay passes.

The v18 first batch used the ordinary runner, which omitted forecast traces. A diagnostic audit correctly failed on that missing field (`fortress18-audit-001.log`). The second batch uses the trace-recording runner; both six-game batches are retained and their repetitions are checked in `fortress18-repeat-audit-001.json`, not counted as12 distinct conditions. All12 recorded games pass `fortress18-replay-audit-002.json`. The matched comparison across15/17/18 is `fortress15-18-trajectory-comparison-001.json`. This finding concerns these public-policy counters and fixed start states, not the separate benefits of the component fixes.

## 2026-10-31T05:18:36.866301+00:00 Fixed-opening transfer registered; immediate bound checked

Claim: against any legal first-round map with no damaging turret, 100 gold buys at most 32 immediate damage, attained by four tier1 and one tier2 in any order. Verdict: CONFIRMED, with a complete informal proof in `experiments/validation/analysis/opening_damage/PROOF.md`. Original-engine checks enumerate all 27 affordable ordered rosters on three wall maps and both seats, 162 combats, all agree. Eight additional policy checks confirm legal submissions and unchanged observations. This is an immediate-damage bound, not a game-strength claim.

Claim to test: an early mixed attack, a gun1 plus a smaller mixed attack, or a gun1 plus one tier1 and two factories can improve a frozen general continuation without forecasting an opponent. Verdict: OPEN. The prospectively registered `experiments/validation/opening-transfer-001.json` has six variants (three openings times fortress18/economy13 continuation), both direct controls, and three opponents (those two policies and the frozen lead v7 robust/big100/no-poke setting), 48 games with both assignments.

## 2026-10-31T05:21:31.146108+00:00 Lead freeze input: early attacks win the completed lead-v7 conditions

Interim result, not a completed campaign. Claim that the robust/big100/no-poke lead setting is immune to early attacks: REFUTED by completed original-engine games. In `runs/validation/lead-seven-early-001`, the frozen setting (registered snapshot hash above) has lost all completed cases so far. The completed side-zero rows are `[{"id": "mixed_r1", "hp": [790, 768], "rounds": 50, "mismatch_rounds": []}, {"id": "mixed_r1_defense_first", "hp": [800, 780], "rounds": 50, "mismatch_rounds": []}, {"id": "t1_r1_full", "hp": [790, 770], "rounds": 50, "mismatch_rounds": []}, {"id": "t1_r1_45percent", "hp": [800, 785], "rounds": 50, "mismatch_rounds": []}, {"id": "t1_r1_60percent", "hp": [800, 780], "rounds": 50, "mismatch_rounds": []}, {"id": "t2_r1", "hp": [790, 776], "rounds": 50, "mismatch_rounds": []}, {"id": "t3_r1", "hp": [780, 774], "rounds": 50, "mismatch_rounds": []}]`. The mixed attack uses four tier1 and one tier2 in round one; the counter then forecasts and defends. Strict required-source, no-error, no-rejection checks pass for these completed rows. The full paired forecast-trace and replay audit is pending until all 16 finish. This does not imply that the one-round opening alone wins with a general continuation; a separate 48-game continuation transfer campaign is running and already has losses. The reserved final pools remain unused.

## 2026-10-31T05:22:51.475013+00:00 Multi-round public-model schedules registered

Claim to test: a cheap round-one attack can combine with the round-three tier3 weakness of the frozen lead v7 setting. Verdict: OPEN. `experiments/validation/lead-seven-schedule-001.json` registers 12 fixed schedules and both seats, including a no-opening control, one to four opening tier1, an opening tier2, the mixed opening, a defense-first variant, and later tier3/tier4/tier5 follow-ups. `bots/counters/public_schedule.py` uses public forecasting only for defense; its attack schedule is declared in the specification. Each purchase is capped by actual gold, so intended and executed quantities can differ. The exact submitted sequence and forecast diagnostics are retained.

## 2026-10-31T05:24:17.646030+00:00 Lead-v7 early-attack campaign complete and audited

Claim: the registered early counters beat the frozen robust/big100/no-poke lead v7 setting. Verdict: CONFIRMED for all 16 declared games. Strict source attestation, exact submitted-action forecast checks, and full unchanged-engine action replay all pass; all eight swapped-assignment pairs have identical canonical trajectories. No failures or rejected actions. The seven opening variants and the round-three control all win.

| Counter | Final HP, counter first | Round |
| --- | --- | --- |
| mixed_r1 | 790:768 | 50 |
| mixed_r1_defense_first | 800:780 | 50 |
| t1_r1_full | 790:770 | 50 |
| t1_r1_45percent | 800:785 | 50 |
| t1_r1_60percent | 800:780 | 50 |
| t2_r1 | 790:776 | 50 |
| t3_r1 | 780:774 | 50 |
| t3_r3 | 800:774 | 50 |

Evidence: `runs/validation/lead-seven-early-audit-001.json` and `lead-seven-early-replay-audit-001.json`, with job specifications and replays under `lead-seven-early-001/`. Reproduce the full campaign with `python -B -m bot_research.experiments.validation.run_forecast_full --manifest bot_research/experiments/validation/lead-seven-early-001.json --output-dir bot_research/runs/validation/NEW --max-seconds 480 --match-timeout 120`, then resume as needed; use the prescribed environment and lane affinity. These are eight deterministic paired conditions, not 16 independent samples. The round-one margins do not exceed the already known 26-HP round-three weakness. The experiment expands the known failure timings; it does not worsen the previous worst observed margin. Multi-round combinations are registered separately.

## 2026-10-31T05:24:17.646030+00:00 Roster cutoff isolated from the gun-search algorithm

Claim: for the previously reported legal large-roster fixture, the gun helper itself can find a stopping response if it is called. Verdict: CONFIRMED. `check_large_roster_gun_pass.py` calls the frozen v18 `_gun_pass` directly, without changing globals or the engine. It returns gun3 at (10,8) and (10,9), cost 400, zero damage against all 13 sampled compositions on the unchanged engine. The published `plan_defense` skips this helper because the maximum composition length is 293 > 120 and returns two splashes costing 120 that still leak 140. Runtime for the combined component comparison and original-engine checks was 0.715 seconds. This isolates the cutoff in this fixture; it does not justify removing it globally without a runtime study. The same cutoff remains in frozen v19. Evidence: `runs/validation/large-roster-gun-pass-001.json`.

## 2026-10-31T05:26:07.486100+00:00 Fixed-opening transfer: cheap guard works on the tested trio; larger opening attacks fail

Claim that the 32-damage opening is a generally stronger full-game policy: REFUTED on this declared matrix. With economy13 continuation it loses all six games; with fortress18 it wins only against the lead setting and loses four others. The gun plus 22-damage mixed opening also loses four or six. Conversely, gun1 at (3,1), one tier1, two factories, then economy13 wins all six tested games, while direct economy13 has four wins and two self-play draws. This last result is CONFIRMED only for the three frozen opponents. It needs an economy-first stress test before any recommendation.

| Opening and continuation | Lead7 HP | Fortress18 HP | Economy13 HP |
| --- | --- | --- | --- |
| mixed32_fortress18 | W 780:768 | L 755:768 | L 674:768 |
| guard22_fortress18 | L 520:778 | L 776:778 | L 696:778 |
| guard_poke5_fortress18 | W 800:795 | W 800:571 | L 362:768 |
| mixed32_economy13 | L -50:768 | L -192:768 | L -77:768 |
| guard22_economy13 | L -180:778 | W 755:-1182 | L 768:778 |
| guard_poke5_economy13 | W 800:795 | W 775:615 | W 783:768 |
| direct_fortress18 | W 790:785 | D 490:490 | L -985:750 |
| direct_economy13 | W 790:758 | W 750:-985 | D 778:778 |

All 48 games passed strict source attestation, error/rejection checks and full original-engine replay; each of the 24 reversed pairs has an identical canonical trajectory. Evidence: `runs/validation/opening-transfer-audit-001.json` and `opening-transfer-replay-audit-001.json`. Reproduction manifest: `experiments/validation/opening-transfer-001.json`, with `run_long_development` and `--shards 2 --shard 0` or `1`. No reserved outcomes have been examined.

## 2026-10-31T05:26:07.486100+00:00 Guard-versus-economy follow-up registered

Verdict: OPEN. `experiments/validation/guard-transfer-001.json` compares the selected cheap guard plus economy13 with direct economy13 on eight declared development opponents, 32 games including both seats. Opponents include eco6 tier5, a stacking policy, the two fortress19 configurations, rush_t1, poke_lock, random seed130, and lead4. This follow-up is informed by the preceding three-opponent result and is not a held-out final evaluation.

## 2026-10-31T05:30:53Z Turret-feature probe registered

Claim to test: a cheap off-route gun can exploit economy13's permanent "opponent has owned a turret" flag by disabling its more aggressive no-turret attack mode. Verdict: OPEN. The fixed policy in `bots/counters/feature_bluff.py` buys a declared gun, invests through round six and then spends on tier5. The registered `experiments/validation/feature-bluff-001.json` compares no gun, an off-route gun at (0,11) in round one or three, and a useful gun at (3,1) in those rounds, against direct economy13 and its cheap-guard continuation. Twenty original-engine games including both seats are planned. The no-gun control should reproduce eco6_t5. A full-game difference also includes the gun's opportunity cost; it will not by itself prove that the feature branch caused the outcome.

## 2026-10-31T05:34:25Z Later waves after a cheap poke registered

Verdict: OPEN. The completed portions of `lead-seven-schedule-001` show that an opening tier1 makes the lead buy two gun1 in round two and another in round three, stopping the scheduled tier3. The no-opening control buys no defenses in those rounds and loses 26 HP. This suggests testing the economic effect separately from a second early purchase. `experiments/validation/lead-seven-late-poke-001.json` registers a single round-one tier1 followed by tier4 at rounds 5 through 8 or tier5 at rounds 7 through 12, conserving the money previously spent on the round-three tier3. These are development follow-ups, not independent confirmation of a selected best timing.

## 2026-10-31T05:35:22Z Cheap-guard economic follow-up complete

Claim that the cheap guard preserves every direct-economy13 win: REFUTED. Against eco6_t5 it changes a round-seven win (520:0) into simultaneous base destruction at round eight (-40:-54), which the original engine correctly scores as a draw. Claim that it improves the aggregate result on this declared eight-opponent development matrix: CONFIRMED. The guard scores 14 wins and 2 draws; direct economy13 scores 12 wins, 2 draws and 2 losses. Every one of the 32 games passes strict source attestation and full original-engine replay. All 16 swapped-seat pairs have identical canonical trajectories.

| Opponent | Cheap guard plus economy13 | Direct economy13 |
| --- | --- | --- |
| eco6_t5 | D -40:-54, round 8 | W 520:0, round 7 |
| poke_lock | W 800:795 | D 795:795 |
| fortress19 | W 775:615 | W 750:555 |
| fortress19 robust | W 800:795 | L 790:795 |
| rush_t1 | W 770:-10, round 8 | W 770:-54, round 8 |
| stacker default | W 800:-232, round 12 | W 800:-4, round 9 |
| random130 | W 800:-300, round 13 | W 795:-18, round 12 |
| lead4 | W 800:709 | W 790:655 |

HP is candidate first; unmarked ending rounds are 50. The largest measured guarded match runtime was about 54 seconds against lead4. The two policies have complementary results, so the guard is an additional strong development candidate, not a dominance claim. Its spec is `bot_research.bots.counters.opening_response:@make?opening=%22guard_poke5%22&fallback=%22economy13%22`. Evidence: `runs/validation/guard-transfer-audit-001.json`, `guard-transfer-replay-audit-001.json`, and the frozen jobs, sources and replays in `guard-transfer-001/`. The replay audit took 28.1 seconds. No reserved final-validation conditions were used.

## 2026-10-31T05:36:52Z Turret-feature mechanism ablation registered

Verdict: OPEN. The initial bluff screen shows a useful distinction: no tested bluff beats direct economy13, but buying the off-route gun in round three beats the cheap-guard continuation. To distinguish a policy-feature effect from the purchase's economic effect, `feature-ablation-001.json` registers 24 games. It compares the normal guard continuation with two explicitly different policies: one ignores the public enemy turret-count signal while retaining the entire physical building list, and one sets `none_from=51` to disable the special no-turret mode. The real engine and its observations are unchanged. Normal-mode conditions are repeat controls. `bots/counters/turret_feature_ablation.py` contains these attribution policies; they are not passed off as the unchanged original economy13.

## 2026-10-31T05:37:19Z Off-route turret is a verified counter to the cheap guard

Claim that a one-gun bluff reverses the matchup against direct economy13: REFUTED for the four tested placements and timings. Claim that a round-three gun reverses the no-gun draw against the cheap-guard continuation: CONFIRMED. Both assignments agree, all 20 games pass strict source/error/rejection checks and full original-engine replay, and all ten swapped-seat pairs have identical canonical trajectories.

| Fixed eco6 policy | Against direct economy13 | Against cheap guard plus economy13 |
| --- | --- | --- |
| no gun | L 0:520 | D -54:-40 |
| off-route gun, round 1 | L -7:660 | L -220:100 |
| off-route gun, round 3 | L -185:520 | W 415:-320 |
| useful gun, round 1 | L -34:800 | L -1:380 |
| useful gun, round 3 | L -22:520 | W 480:-320 |

HP is counter first. The off-route gun at (0,11) has exactly zero combat effect throughout these matches: it never changes its map's route and is outside range of every path cell. The proof and independent checker are in `experiments/validation/analysis/feature_bluff/PROOF.md` and `runs/validation/feature-bluff-check-001.json`. The new counter spec is `bot_research.bots.counters.feature_bluff:@make?turret_round=3`. Evidence: `runs/validation/feature-bluff-audit-001.json` and `feature-bluff-replay-audit-001.json`. This establishes a full-game counter, not yet a uniquely isolated causal explanation: the purchase also costs gold and changes later quantities. The separate registered feature ablation addresses that distinction.

## 2026-10-31T05:41:04Z Two-wave counter exceeds the lead's earlier 26-HP weakness

Claim that combining a small opening poke with a later purchase cannot worsen the known lead7 margin: REFUTED. The completed 24-game schedule matrix contains a counter that buys one tier1 in round one and one tier4 in round five, winning 800:735 at round50 in both assignments. It deals five damage immediately and sixty in round five. The lead spends all eight affordable factory purchases in round five and accepts that hit. Both complete trajectories are identical after seat normalization. This is the frozen lead7 setting big_threat=100, robust attack, poke_insurance=False, gun_cap=120, not the lead's eventual final bot.

All 24 games pass the strict forecast/source/error/rejection audit and full unchanged-engine replay. Every opponent-action prediction agrees with the actual action list. The twelve schedules all win, but only this schedule exceeds the no-opening round-three tier3 control's 26-point margin: most extra early purchases merely induce enough defense to stop later attacks. The three-wave tier1/round-three-tier3/round-five-tier4 schedule wins only800:795, so buying an ineffective early tier3 can remove the later opportunity. Full audit: `runs/validation/lead-seven-schedule-audit-001.json`; replay check: `lead-seven-schedule-replay-audit-001.json`. The winning specification is recorded as `r1_t1_r5_t4` in `experiments/validation/lead-seven-schedule-001.json` and uses `public_schedule:@make`. The registered later-wave campaign repeats this condition as an explicit reproducibility control and tests nine additional timings. Verdict for those later timings remains OPEN.

## 2026-10-31T05:41:26Z Turret-count feature causally changes the cheap-guard matchup

Claim that the round-three bluff works by disabling the special no-turret attack mode: CONFIRMED for the declared policy intervention. All 24 ablation games pass strict source/error/rejection checks and full original-engine replay. The eight normal-mode repeats exactly reproduce their earlier complete trajectories. For both useful and off-route round-three guns, real game histories are identical through round three between normal and ignore-feature policies; the first guard action difference is round four. The normal guard buys three tier1 and five factories. The guard that ignores the turret-count signal buys ten tier1 and no factories.

| Counter | Normal guard | Ignore turret-count feature | Disable no-turret mode |
| --- | --- | --- | --- |
| no gun | D -54:-40 | D -54:-40 | W 415:-320 |
| off-route gun, round 1 | L -220:100 | L -54:240 | L -220:100 |
| off-route gun, round 3 | W 415:-320 | D -54:-40 | W 415:-320 |
| useful gun, round 3 | W 480:-320 | D -25:-40 | W 480:-320 |

All values are counter-first final HP; both assignments agree. Ignoring the feature removes the bluff's win, while disabling the no-turret mode allows the no-gun policy to win. The off-route gun has no physical combat effect, but its cost is held fixed in the matched normal-versus-ignore comparison. These are explicitly different policies for mechanism attribution, not altered engine executions. This does not imply that ignoring turret count is a general improvement. Evidence: `feature-ablation-audit-001.json`, `feature-ablation-replay-audit-001.json`, and `feature-ablation-comparison-001.json` under `runs/validation/`. The comparison records source/input hashes and the matched action lists.

A small counter cycle is now suggested by separately audited development games: cheap guard beats direct economy13; direct economy13 beats the round-three off-route bluff; that bluff beats cheap guard. A fresh three-policy matrix, including self-play, is registered in `experiments/validation/counter-cycle-001.json` to verify all entries together. Previously observed edges are reproducibility controls, not additional independent evidence. The exact finite-game certificate will use the existing conditional argument in `analysis/finite_metagame/PROOF.md`; it will make no claim outside this three-policy table. Verdict for the complete matrix: OPEN.

## 2026-10-31T05:45:13Z A verified three-policy counter cycle

Claim: the successful guard and bluff establish a strict ranking of the three policies. Verdict: REFUTED. The fresh 18-game development matrix confirms a cycle. Cheap guard plus economy13 beats direct economy13 by783:768; direct economy13 beats the round-three off-route bluff by520:-185; that bluff beats cheap guard by415:-320. Each condition includes both assignments, and every pair has an identical normalized trajectory. All eighteen original-engine replays and the strict source/error/rejection checks pass. Repeated edge tests are reproducibility controls, not independent samples.

In policy order E = direct economy13, G = cheap guard, B = round-three off-route bluff, the row-player payoff matrix is [[0,-1,1],[1,0,-1],[-1,1,0]], with win=1,draw=0,loss=-1. The exact rational certificate verifies that probability1/3 on each has value zero against every mixture of these three policies. The standalone proof shows this is the unique maximin distribution for this matrix. Verdict for this conditional finite-table claim: CONFIRMED. It is not a solution of the full game or a transfer guarantee.

Evidence: `runs/validation/counter-cycle-audit-001.json`, `counter-cycle-replay-audit-001.json`, `counter-cycle-matrix-001.json`, `counter-cycle-certificate-001.json`, and `counter-cycle-certificate-check-001.json`. Proof: `experiments/validation/analysis/counter_cycle/PROOF.md`. Replay runtime was30.808seconds. No reserved final-validation condition was used.

## 2026-10-31T05:45:55Z Small wall investments after the cheap guard registered

Claim to test: using the guard opening's remaining15 gold for route-building walls improves its continuation. Verdict: OPEN. The exact original-engine component check covers five wall caps in both assignments and all27 affordable ordered first-round rosters,270 combats. All intended actions are legal, observations remain unchanged, and every tested prefix still stops the opponent's two-tier1 opening. Wall caps0,9,11,13,15 produce route lengths22,22,24,28,32 and end-round gold72,63,63,65,67 with two factories. The cap-zero action list exactly matches the existing guard. These component facts do not establish a full-game improvement.

The registered40-game matrix in `experiments/validation/guard-walls-transfer-001.json` tests caps0,11,13,15 against direct economy13, the off-route round-three bluff, eco6_t5, lead7 robust/big100/no-poke, and fortress19 robust, in both assignments. Cap-zero conditions are repeat controls. Implementation: `bots/counters/guard_walls.py`; component evidence: `runs/validation/guard-walls-check-001.json`. The new walls may also alter later turret placement, so any full-game difference must be interpreted as an entire policy change rather than an isolated income gain.

## 2026-10-31T05:47:13Z Later-wave timeout accounting

The first invocation of each later-poke shard completed eleven of twenty declared conditions. Two attempts hit the120-second cap: tier5 at round8 in seat0 and tier5 at round9 in seat1. Seven conditions remain unstarted. The observed paired tier4 margins increase from65 at round5 to125,185,365 at rounds6,7,8; all five completed pairs win, and tier5 round7 wins by145. These are provisional until the combined audit.

The registered retry/completion manifest `lead-seven-late-poke-retry-001.json` retains the original five tier5 schedules for rounds8 through12 and raises the per-match cap to300seconds. Its round8 seat1 game explicitly repeats one completed control. Original failures and unstarted declarations remain intact. The strict audit will merge by exact condition and select the earliest valid completion; the new `audit_forecast_attempts.py` will independently verify every completed attempt's prediction trace. Timeouts count as computational failures, not game outcomes. Verdict for complete later-wave comparison remains OPEN.

## 2026-10-31T05:49:57Z Successful lead counters do not require online opponent forecasting

Claim: the round-five and round-eight tier4 wins require the public opponent model. Verdict: REFUTED for the four checked source histories. A simpler policy, `bots/counters/guarded_schedule.py`, defends against a declared two-tier1 opening in round one, then only against the already visible roster. It never imports or calls the opponent policy. For both timings and both assignments, its defensive threat list and complete returned action list agree with PublicSchedule in all50 rounds,200 rounds total. All source histories pass strict source attestation and original-engine replay. The opposing lead buys only its initial two tier1 in these histories, so the visible roster suffices thereafter.

The exact equivalence proof is `experiments/validation/analysis/visible_schedule/PROOF.md`; evidence is `runs/validation/visible-schedule-check-001.json`. This is a deduction of the same recorded trajectories, not four new games. The simpler policy inherits the 800:735 and800:435 results under the proof's explicit hypotheses. New hidden purchases by another opponent can break the equivalence, so no general defense guarantee follows.

The registered `visible-schedule-001.json` now runs those two controls as fresh games and extends the tier4 screen to rounds9 and10, eight games total. A wall-prefix follow-up has also begun; early results are unfavorable despite the longer route. Neither development experiment opens reserved validation.

## 2026-10-31T05:54:09Z Transfer screen registered for adaptive fortress21

Verdict: OPEN. Frozen fortress21 now conditions response-aware attack on whether the enemy has a turret. Its planner retains a three-second wall-clock limit, so identical frozen conditions do not by themselves guarantee identical policy actions; paired trajectories will be checked. The registered36-game development matrix `experiments/validation/fortress-feature-transfer-001.json` compares six policies against frozen fortress19,20,21 in both assignments: the visible-roster tier4 schedules at rounds5 and8, cheap guard plus economy13, and no-gun/round-one-gun/round-three-gun eco6 policies. This checks whether the newly recommended adaptive policy transfers to adversarial public-feature probes. A full-policy comparison alone will not isolate the feature's causal contribution. No reserved final-validation conditions have been used.

## 2026-10-31T05:55:17Z Completed later-wave screen and forecast-removal validation

Claim that the known lead7 loss is limited to 26 HP: REFUTED. After a single tier1 in round one, a tier4 purchase at round eight wins 800:435 in both assignments. The complete ten-timing screen is now audited. All twenty distinct conditions win; all ten swapped-seat pairs have identical complete normalized trajectories. The exact results below use counter-first HP and all end at round 50.

| Second purchase | Final HP |
| --- | --- |
| tier4, round 5 | 800:735 |
| tier4, round 6 | 800:675 |
| tier4, round 7 | 800:615 |
| tier4, round 8 | 800:435 |
| tier5, round 7 | 800:655 |
| tier5, round 8 | 800:515 |
| tier5, rounds 9 through 12 | 800:795 each |

Verdict for these conditions: CONFIRMED. The strict audit retains 21 valid attempts for twenty distinct conditions, two original 120-second failures, and seven originally unstarted declarations subsequently completed in the retry batch. All 21 completed games pass original-engine replay and exact forecast comparison. The repeated tier5-round-eight control and both round-five controls reproduce their complete earlier trajectories. No failed attempt is counted as a game outcome or silently removed. Evidence: `runs/validation/lead-seven-late-poke-audit-001.json`, `lead-seven-late-poke-forecast-audit-001.json`, `lead-seven-late-poke-replay-audit-001.json`, and `late-poke-control-check-001.json`.

The separate model-free eight-game validation also passes strict source checks and every original-engine replay. Its four round-five/round-eight controls reproduce the public-model counter's complete trajectories exactly. Extending the tier4 purchase to round nine or ten yields only 800:795: the later window is closed. Verdict that the public model is unnecessary for the selected round-eight counter: CONFIRMED under this opponent and standard start. `guarded_schedule` never loads the opponent's source; it uses a declared two-tier1 round-one threat and subsequently only the visible roster. Reproduction spec:

```text
bot_research.bots.counters.guarded_schedule:@make?schedule=%5B%5B1%2C%22tier1%22%2C1%5D%2C%5B8%2C%22tier4%22%2C200%5D%5D
```

Evidence: `visible-schedule-audit-001.json`, `visible-schedule-replay-audit-001.json`, and `visible-schedule-control-check-001.json` under `runs/validation/`. The stronger result remains a targeted development counter to the frozen lead7 parameters, not a claim about the eventual final entry point or unrelated opponents. The policy can miss another opponent's hidden new purchases.

## 2026-10-31T05:57:10Z Extra opening walls degrade the cheap-guard continuation

Claim that spending the remaining opening gold on the tested wall prefixes improves the cheap guard: REFUTED as a general improvement on this five-opponent matrix. All forty games pass strict source checks and original-engine replay; all twenty swapped-seat pairs have identical complete trajectories. The cap-zero policy scores 6 wins, 2 draws, 2 losses. Caps 11 and 13 each score 2 draws and 8 losses; cap 15 scores 2 wins and 8 losses.

| Opponent | No extra walls | Cap 11 | Cap 13 | Cap 15 |
| --- | --- | --- | --- | --- |
| economy13 | W 783:768 | L -57:768 | L -57:768 | L -57:763 |
| off-route gun, round 3 | L -320:415 | L -40:400 | L -460:125 | L -180:240 |
| eco6 tier5 | D -40:-54 | D -40:-49 | D -40:-74 | W 100:-79 |
| lead7 robust/big100/no-poke | W 800:795 | L -880:795 | L -460:795 | L -600:795 |
| fortress19 robust | W 800:795 | L -880:795 | L -40:795 | L -460:375 |

HP is guard first. The fifteen-wall opening does turn the eco6 draw into a win, but loses three opponents that the unmodified guard beats. Longer route income is not enough to establish a better policy: the added walls also constrain the continuation's turret placements and alter later attack choices. This matrix is a full-policy comparison and does not isolate the relative contribution of those mechanisms. Evidence: `runs/validation/guard-walls-audit-001.json` and `guard-walls-replay-audit-001.json`; declared conditions: `experiments/validation/guard-walls-transfer-001.json`. These are development results; reserved validation remains unused.

## 2026-10-31T05:57:43Z Why the lead7 round-eight wave lands

Claim: the round-eight tier4 loss is forced by the lead's available gold. Verdict: REFUTED for that recorded state. The lead starts with 893 gold and five gun1 turrets; the counter has 1595 gold and buys six tier4. The lead returns forty factory purchases costing 800, and all six tier4 arrive for 360 damage. Its sampled worst damage before new defense is 408. The same unchanged planner with `partial="none"` finds no plan that stops every sampled affordable composition within 893, so the big-threat insurance step returns nothing.

Calling the existing planner with `partial="best"` on the same public observation and the same sampled affordable compositions returns an 845-gold plan. Applying every action through the original legality checks and simulating every composition with the unchanged combat implementation confirms zero damage from the actual wave and a worst sampled damage of 280. A hindsight plan against only the actual roster costs 780 and also stops it, but that latter information is not available to the bot. The partial plan uses only public information; the hindsight plan is only a feasibility witness.

This does not prove a full-game improvement: buying partial insurance earlier may slow growth or alter placement. A separate registered ablation will test the whole policy. Evidence and reproduction: `experiments/validation/diagnose_insurance_skip.py --result bot_research/runs/validation/visible-schedule-001/results/case0002.json --round 8 --output NEW.json`, with the required Python environment; retained output `runs/validation/insurance-skip-diagnosis-001.json`. The source result has already passed full original-engine replay. All ten cap-zero wall-study controls also reproduce their earlier complete histories, as checked in `guard-walls-control-check-001.json`.

## 2026-10-31T06:00:22Z: transfer to fortress versions 19, 20, and 21

Claim that the successful lead7 schedules or the economy13 turret bluff generalize to every current fortress policy: REFUTED on the declared development matrix. Six counter policies played frozen fortress19 default, fortress20 default, and fortress21 default in both assignments (36 games). All 36 pass strict source, action, and error checks and full replay through the original engine. All 18 player-swapped pairs have identical complete normalized trajectories, so these are 18 distinct deterministic conditions, not 36 independent samples.

| Counter | Fortress19 | Fortress20 | Fortress21 |
| --- | --- | --- | --- |
| guarded tier4 round5 | L 445:615 | L -180:735 | L -6:735 |
| guarded tier4 round8 | W 747:-45 | L -84:495 | L -180:555 |
| cheap guard + economy13 | W 775:615 | W 800:795 | W 800:735 |
| bluff policy, no turret | L -20:520 | L -40:240 | L -20:520 |
| bluff policy, off-route turret round1 | L -260:240 | L -40:240 | L -40:520 |
| bluff policy, off-route turret round3 | L -20:520 | L -40:240 | L -210:520 |

Values are counter-first final HP. The guarded schedules include one tier1 in round1 and maximum affordable tier4 at the stated later round. The cheap guard is `bot_research.bots.counters.opening_response:@make?opening=%22guard_poke5%22&fallback=%22economy13%22`. Its four games against fortress19 and fortress20 exactly reproduce the earlier fortress19 default and fortress19 big_threat=100,robust_attack=true games. These four are explicit repeat controls. The other 32 are newly evaluated specifications, with 16 distinct player-normalized conditions.

Claim that the cheap guard also exploits the recommended fortress21: CONFIRMED for its default policy, standard start, and this frozen implementation (800:735 in both assignments). This does not establish a general best response. Fortress21 conditions response-aware attack on visible turret ownership, but the round-three off-route bluff that wins against guarded economy13 loses here. Shared use of a public feature does not by itself prove shared exploitability; the surrounding policy matters.

Evidence: `bot_research/experiments/validation/fortress-feature-transfer-001.json`; `bot_research/runs/validation/fortress-feature-audit-001.json`; `fortress-feature-replay-audit-001.json`; `fortress-feature-control-check-001.json`. Original-engine replay took 10.30 seconds. Development only; reserved pools A and B remain unused.

## 2026-10-31T06:03:17Z: matrix footer outcome-label audit

Claim that experiments/lead/matrix.py labels W/D/L by the engine winner: REFUTED. The HP table itself is a descriptive table, but its footer counts positive HP differences as wins and negative differences as losses. The engine declares simultaneous destruction a draw even when the two negative residual HP values differ. A real guard-versus-eco6 draw, checked against its frozen sources and replayed through the unchanged engine, projects to the matrix input schema and yields a footer of 1-0-0 instead of 0-1-0.

Scope check: all completed rows in lead c5a (144), c5b (144), and c2rr1 (110) have matching winner-based and HP-sign outcomes. Thus this audit identifies a latent reporting bug; it does not change those three campaigns' published counts. The main harness tournament uses the engine winner correctly, and our independent strict audits also do. Recommended lead repair: retain HP as a separate metric and compute the footer from winner and candidate_side.

Evidence: experiments/validation/audit_lead_outcome_labels.py; runs/validation/lead-outcome-label-audit-001.json; runs/validation/outcome-label-fixture-001.jsonl. The fixture is explicitly a schema projection of a source-validated replay, not a fresh game or independent sample. Lead source files were not changed. Verdict: CONFIRMED defect with no observed effect in these three audited campaigns.

## 2026-10-31T06:05:21Z: full-game partial-insurance ablation completed

Claim that enabling big_partial repairs the lead7 round-eight counter: REFUTED as an outcome claim, although it halves the later wave's damage. Both current lead7 and its big_partial=true variant score 2W/2D/8L against the six declared opponents in both assignments. All 24 games pass strict source/error/rejection checks and original-engine replay. All 12 assignment pairs are identical after normalization. Six current-policy repeats against guarded tier4 schedules and the cheap guard reproduce their earlier complete trajectories, even though the prior jobs designated the opposing side as candidate.

| Opponent | Current lead7 HP | Partial-insurance lead7 HP |
| --- | --- | --- |
| guarded tier4 round5 | L 735:800 | L 735:800 |
| guarded tier4 round8 | L 435:800 | L 615:800 |
| cheap guard + economy13 | L 795:800 | L 795:800 |
| eco6_t5 | W 800:680 | W 800:680 |
| economy13 | L 758:790 | L 758:790 |
| fortress21 | D 790:790 | D 790:790 |

Values are lead-first; both assignments agree. Four opponent pairs have entirely identical current/partial histories. The round-five schedule's histories first diverge at round7, after its damage has landed. Against the round-eight schedule, histories first diverge at round6. Current lead7 buys15 factories then, whereas partial lead7 buys one gun2, one gun3, and one factory. Partial buys another gun2 and gun3 in round7. Consequently it enters round8 with318 gold and17 factories, versus current lead7's893 gold and56 factories. Its five new splashes reduce the six-tier4 wave from360 to180 damage, but it still loses. This explains why the feasible845-gold local repair on the original round-eight state does not transfer to a policy that enables partial insurance from the beginning.

Evidence: runs/validation/lead-partial-ablation-audit-001.json; lead-partial-ablation-replay-audit-001.json; lead-partial-ablation-comparison-001.json; lead-partial-control-check-001.json. Replay runtime21.36seconds. This is a six-opponent development ablation, not a general claim against partial insurance; reserved A/B remain unused.

## 2026-10-31T06:09:40Z: newer continuations after the same cheap guard

Claim that the layout-free economy15 continuation repairs the cheap guard's eco6 weakness: CONFIRMED for this six-opponent development matrix. All48 games pass strict source/error/rejection checks and original-engine replay. All24 swapped-seat pairs have identical complete normalized trajectories. Ten economy13 guard controls exactly reproduce earlier games. Thus those controls add reproducibility evidence, not independent strength samples.

| Opponent | Guard + economy13 | Guard + economy15 leak | Same, sat_frac=.25 | Guard + fortress21 |
| --- | --- | --- | --- | --- |
| economy13 | W 783:768 | W 783:768 | W 783:768 | L 740:795 |
| fortress21 | W 800:735 | W 800:735 | W 800:683 | W 800:795 |
| lead7 big100/robust/no-poke | W 800:795 | W 800:795 | W 800:795 | W 800:795 |
| off-route round3 bluff | L -320:415 | L -180:365 | L -180:365 | L -320:685 |
| eco6_t5 | D -40:-54 | W 100:-49 | W 100:-49 | L -600:220 |
| guarded tier4 round8 | W 800:-29 | W 800:-29 | W 800:-27 | W 800:-40 |

HP is guard first; both assignments agree. The economy15 variants score10W/2L, economy13 scores8W/2D/2L, and fortress21 scores6W/6L. Against eco6, the first economy13/economy15 difference is round6: for the same total280 gold, economy13 buys four tier2 and two splashes, while economy15 buys four tier2, one splash and two gun1. Both later take280 damage in round7. In round8 economy13 takes560 and dies simultaneously with the opponent; economy15 takes420 and survives with100. This explains the observed outcome change without claiming that the first differing purchase alone suffices.

The economy15 leak continuation exactly matches economy13's full history against direct economy13, fortress21, and guarded tier4 round8. Other equal outcomes need not have identical action histories. The lower saturation fraction has no outcome advantage on these six opponents, although two winning margins improve slightly. The round3 bluff still wins against every continuation; a general repair claim is REFUTED.

Candidate spec: bot_research.bots.counters.guard_continuation:@make?continuation=%22economy15%22&parameters=%7B%22free_fallback%22%3A%22leak%22%7D. Evidence: experiments/validation/guard-continuation-001.json; runs/validation/guard-continuation-audit-001.json; guard-continuation-replay-audit-001.json; guard-continuation-control-check-001.json; guard-continuation-comparison-001.json. Replay runtime21.81seconds. No reserved conditions were used.

A separate lead9 feature study is running. Its no-turret and round3-turret controls can differ because the turret costs gold even when it appears after the lead's poke-insurance cutoff. Therefore full-policy wins cannot by themselves establish a turret-trigger exploit. The registered lead-nine-roster-ablation-001.json changes only poke_reactive from the turret option to true (visible-roster trigger only), holding all other parameters fixed. Verdict for that mechanism remains OPEN.

## 2026-10-31T06:12:09Z: final candidate freeze received

The lead's FROZEN best_v9a instruction has been received. Both bots/best.py and experiments/lead/frozen/best_v9a.py independently hash to 88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d. The announced heading is labeled06:13Z, but the actual receipt time is the timestamp above. PoolA, whose opponent parameters and legal prefixes were registered before these candidate iterations, now has priority. PoolB remains unused. Targeted development counters will be reported separately, with exact equivalence checks against the earlier lead9 development twin where applicable. Verdict for final validation: OPEN.

## 2026-10-31T06:16:19Z: lead9 turret-feature ablation, all48 games checked

Claim that the round-two off-route gun worsens the lead through its explicit turret trigger: CONFIRMED for both tested opening sizes. The24 turret-mode games and24 matched roster-only-mode games all pass strict source/error/rejection checks and complete unchanged-engine replay. Every swapped-seat pair has an identical normalized trajectory. Changing only poke_reactive from the turret option to true leaves20 of24 complete trajectories unchanged. Only the round-two-gun conditions differ, in both assignments and for both opening sizes.

| Counter | Turret mode, opening2 | Roster-only mode, opening2 | Turret mode, opening3 | Roster-only mode, opening3 |
| --- | --- | --- | --- | --- |
| no turret | L 680:800 | L 680:800 | W 620:520 | W 620:520 |
| off-route turret round1 | W 680:520 | W 680:520 | L 620:800 | L 620:800 |
| off-route turret round2 | W 680:380 | W 680:520 | W 620:240 | W 620:380 |
| off-route turret round3 | W 680:520 | W 680:520 | W 620:520 | W 620:520 |
| cheap guard + economy13 | W 800:795 | W 800:795 | D 795:795 | D 795:795 |
| guarded tier4 round8 | W 800:435 | W 800:435 | W 800:555 | W 800:555 |

Values are counter-first final HP, with both assignments agreeing. In the round-two-gun comparison, actual histories are identical through round2. At round3 turret mode buys one splash and four factories (opening2), while roster-only mode buys seven factories; both spend140. The corresponding opening3 purchases are one splash plus three factories versus six factories, both costing120. Later outcomes differ by exactly one140-damage tier5 hit. These matched interventions isolate the parameter's contribution to the observed margin.

Claim that this trigger is necessary for any of these counter wins: REFUTED. Removing it changes no W/D/L outcome. In particular, round-one and round-three gun policies still win their listed conditions with entirely identical histories under both lead modes. A turret purchase also changes available gold and the public map used for planning; a win after that purchase is not sufficient evidence of a feature exploit. The round-three gun cannot trigger insurance through round3 because it becomes visible only in round4.

Evidence: runs/validation/lead-nine-bluff-audit-001.json; lead-nine-bluff-replay-audit-001.json; lead-nine-roster-ablation-audit-001.json; lead-nine-roster-ablation-replay-audit-001.json; lead-nine-feature-comparison-001.json. The frozen development source is bots/counters/snapshots/lead_nine_001.py (48c7b707cc01472f07e9516d417a9c4f4dd1695503189ca03e0c3716cc9c28e5). Independent matches against the published best.py are running separately; its equivalence to this development twin remains to be checked by this lane.

Integrity checkpoint at06:14:35: all903 protected-tree entries, including the pre-existing virtualenv, match the starting inventory exactly. The manifest still has the same1002 missing entries and three pre-existing changed files. No added or removed protected files. The06:15 path scan checked8007 current text artifacts and found no forbidden absolute local path prefixes. Runs occupy929MB; the shared filesystem has154GB free. Evidence: integrity-mid-0614.json and path-audit-0615.json.

## 2026-10-31T06:21:49Z: frozen-source wording review and team recommendations

Claim that best_v9a computes a globally cheapest defense: REFUTED as a literal optimization claim. Its frozen v7 planner evaluates restricted wall prefixes, greedy splash additions, and restricted greedy gun candidates. The planner's own API accurately says "as cheaply as found". The best.py overview's "cheapest plan" should be read with that qualification in the report. Its gun_cap limits the expensive gun-search branch; it is not a demonstrated wall-time bound. The current validation will report measured runtimes on this shared machine. Do not edit the frozen candidate or its dependencies during the campaign to change wording.

I checked the v7 simulate.py used by best_v9a: it contains the complete tick simulation, without the later huge-roster approximation discussed in the defense lane's v22 review. That later approximation finding must not be attributed to best_v9a merely because both versions use a planner named plan.py. The planned source-archive audit will bind the exact imported files.

Team update received: defense has withdrawn fortress21 in favor of fortress22; economy has withdrawn economy15 leak in favor of economy13 pending economy16. Our already registered targeted comparisons against fortress21 and economy15 leak remain historical development conditions. They are not labeled the other lanes' current finalists. The reserved A campaign remains unchanged, and B is unused.

## 2026-10-31T06:24:31Z: frozen best_v9a targeted validation, all22 games confirmed

Claim that the known counter failures transfer to the published entry point: CONFIRMED. Every game passes fresh strict source, error and rejection checks, and every full action history replays exactly on the unchanged engine. Both assignments agree in all11 conditions. The12 control trajectories match the lead9 opening2 development twin exactly after reversing the candidate perspective. This establishes equivalence on those six counter conditions, not on every possible observation.

| Opponent | best_v9a outcome | Final HP, best first |
| --- | --- | --- |
| no-turret growth control | W | 800:680 |
| off-route gun round1 | L | 520:680 |
| off-route gun round2 | L | 380:680 |
| off-route gun round3 | L | 520:680 |
| cheap guard + economy13 | L | 795:800 |
| cheap guard + economy15 leak | L | 795:800 |
| guarded tier4 round5 | L | 735:800 |
| guarded tier4 round8 | L | 435:800 |
| economy13 | W | 795:790 |
| economy15 leak | W | 795:790 |
| fortress21 | D | 790:790 |

The total is6W2D14L across22 games, with11 distinct paired conditions. This is a deliberately targeted development set, not an estimate of population win rate. The entry hash remains88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d. No timeout, rejected action, bot error, or source drift occurred. Match wall times sum to791.56seconds across parallel workers. The largest measured candidate call was11.07seconds and the largest candidate decision total was82.35seconds. These wall measurements come from low-priority pinned processes on a shared machine and are not portable speed bounds. Replay checking took24.46seconds.

Reproduction: run_long_development with experiments/validation/best-v9a-targeted-001.json, shards0/1 of2,120-second match limit and480-second invocation limit; both invocations resumed once to complete their last game. Audit evidence: runs/validation/best-v9a-targeted-audit-001.json, best-v9a-targeted-control-check-001.json, best-v9a-targeted-replay-audit-001.json. Exact specs are in the manifest. The earlier turret-trigger ablation now transfers to these matching trajectories: it explains140HP of the round2-gun margin, but none of the observed W/D/L changes.

Reserved poolA remains in progress. The interim audit independently recovered its job list from the original manifest and verified the complete source archive, with no source drift. PoolB remains unused. Separately, all14 component checks for the geometric turret filter passed; its32-game development experiment has started and remains OPEN.

## 2026-10-31T06:28:23.442489+00:00 Reserved A runtime status, not a strength conclusion

Claim: every reserved condition can complete within300 seconds on this lane's allocated core. Method: frozen best_v9a, pool A, original engine, full replay. Result: standard-07-side0 (mirror) timed out at300 seconds at06:26:30; the partial replay and failure record remain in runs/validation/final-best-v9a-poolA-001. Fourteen other conditions completed (8W6D), and the run continues. Verdict: REFUTED for this wall-time allowance on the shared machine; the timed-out condition has no assigned game outcome. An explicit separate500-second retry is prepared, with identical source hashes and conditions. All attempts will remain in final accounting. Pool B remains unused.

## 2026-10-31T06:30:23.775088+00:00 Geometry filter: bounded improvement, remaining in-route counter

Claim: ignoring opponent turrets whose attack region does not meet the current nonterminal route fixes the cheap-turret signal failure without changing physical planning. Method: `bots/counters/relevant_turret_guard.py`, eight declared development opponents, two variants, both seats (32 games); only a private copy of the opponent's `n_turrets` feature changes. The full building list remains intact. Frozen economy15 leak continues after the same cheap guard. Component checks cover guns, splash, both player indices and input immutability.

Result: unfiltered10W6L; filtered12W2D2L. All32 source/strict/replay checks pass; all16 normalized seat pairs agree exactly; all12 unfiltered controls equal their earlier guard-continuation trajectories. Twelve of16 normal/filter pairs agree exactly. The only changed opponents are the off-route round2 and round3 gun bluffs. Candidate HP first, identical in both seats:

| Opponent | Unfiltered | Filtered |
| --- | --- | --- |
| gun bluff round2 | L -180:340 | W 100:-49 |
| gun bluff round3 | L -180:365 | D -40:-49 |
| useful gun(3,1) round3 | L -40:440 | L -40:440 |
| eco6 tier5 | W 100:-49 | W 100:-49 |
| economy13 | W 783:768 | W 783:768 |
| fortress21 | W 800:735 | W 800:735 |
| lead7 | W 800:795 | W 800:795 |
| guarded tier4 round8 | W 800:-29 | W 800:-29 |

The changed runs agree through round3. At round4, both variants have164 gold: unfiltered buys3 tier1 and5 factories (145 gold), filtered buys10 tier1 (150 gold). The opponent's actions remain identical; its HP diverges because of the larger attack. Against the round3 bluff, both bases die in round8, so -40:-49 is a draw under the actual winner rule. The useful gun remains a counter with identical complete histories, showing that geometric coverage alone does not characterize defensive strength.

Verdict: CONFIRMED for improvement against these two off-route bluffs; REFUTED as a complete repair for cheap-turret adaptation. Generalization is OPEN. Artifacts: `runs/validation/relevant-turret-guard-{audit,control-check,comparison,replay-audit}-001.json`; declared manifests and pair lists in `experiments/validation/`. Summed game runtime314.405s; replay runtime11.945s; largest candidate call1.210s, shared-machine wall times. This is development evidence, not reserved validation.

## 2026-10-31T06:35:48.205256+00:00 Scenario-score interpretation for the defense lane

Claim: fortress22's44-point loss to splash_turtle in `t38_v22_asym_seeds`, asym:7:3, seat0, is inherited from the scripted prefix. Method: inspect the recorded trajectory and hash the source rows. Result: HP progresses800:800,790:795,763:790,731:775 in rounds0-3, then every recorded base-damage value in rounds4-50 is zero. Verdict: CONFIRMED as an attribution of this recorded margin. The stronger claim that the position is an unavoidable loss, or that the continuation cannot improve it, is OPEN and is not implied by this observation. Also, the lead harness calls policies during prescribed rounds and discards their returned actions; our reserved-prefix evaluator skips those calls. Both conventions are legitimate declared stress tests, but they are different for stateful policies. Evidence: `runs/validation/scenario-inherited-deficit-audit-001.json`; scope is recorded-trajectory inspection.

## 2026-10-31T06:43:59.006305+00:00 Reserved-A standard conditions complete; replay and continuation work continues

Claim: frozen best_v9a completes the 20 standard-start reserved-A conditions with 10 wins and 10 draws.
Method: fresh processes with the unchanged engine, both assignments, fixed candidate SHA256 `88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d`. The two mirror attempts exceeded 300 seconds and are preserved as computational failures. Separate 500-second retries completed both as 800:800 draws; no timeout is counted as a loss or draw.
Result: independent strict accounting in `runs/validation/final-best-v9a-poolA-partial-audit-002.json` checks all 20 standard results, source attestations, the archived manifest, and the ten matching normalized seat pairs. The first mirror's original-engine replay has passed; the second is running. All 60 final conditions have not yet completed, so final validation remains OPEN. One recorded factory-prefix loss has now occurred and will be reviewed separately from standard-start strength.
Verdict: CONFIRMED for the completed standard result accounting; OPEN for the full reserved campaign and all replay checks.

Claim: exact reserved opponent parameter sets were absent from the inspected earlier registered experiments.
Method: `experiments/validation/audit_holdout_separation.py` normalizes defaults, query ordering, archetype aliases and stacker profiles. Cutoff is the first reserved campaign start, 06:12:13.913897 UTC.
Result: `runs/validation/holdout-separation-audit-002.json` finds zero exact overlaps for either pool among 700 registered jobs in 51 lane campaigns and 10,856 recognized result rows from 157 snapshots of team result streams. It skips 1717 unrecognized inputs, principally pruned records with no replay timestamp. These exclusions are listed. An initial checker invocation failed on a null replay path; that parsing issue was fixed and its diagnostic retained.
Verdict: CONFIRMED only for this exact-parameter, recognized-record coverage. This is not proof of behavioral novelty or of no unrecorded use. Implementations and ordinary opening actions are shared with development. Pool B remains unused by this lane.

Claim: fixed-map damage to one isolated minion is a better-defined feature than turret expenditure.
Method: standalone proof in `experiments/validation/analysis/single_copy_exposure/PROOF.md`; then `experiments/validation/check_single_copy_exposure.py` against the original engine on 11 legally constructed maps and all five minion tiers.
Result: all 68 checks pass, including 55 single-copy combats. `bots/counters/exposure_guard.py` implements a policy feature based on that damage sum. No full-game exposure-guard match has run yet.
Verdict: CONFIRMED for the stated isolated-copy theorem and component cases; OPEN for strength. Multiple copies compete for gun attacks, so the theorem supplies no stream-defense certificate.

## 2026-10-31T06:47:15.794296+00:00 Reserved replay update and report wording review

Both standard mirror retries now pass independent replay of every recorded action on the unchanged engine. The first replay took179.30seconds and the second174.49seconds; these are verification runtimes, not extra games. All20 standard results have now been replayed across the original and retry campaigns. The ongoing original campaign has32 valid results plus the two preserved failures as of its06:45:27 snapshot. Its14 completed factory-prefix conditions are4W8D2L. Full campaign accounting remains OPEN. PoolB is unused. Please retain best_v9a and its closure until A finishes; development against a new candidate can use its own frozen module meanwhile.

Claim review for the current REPORT.md section6: its sentence "Any opening that leads to this growth path wins, whatever turret it builds" is broader than the evidence. The controlled turret-mode/roster-mode ablation only establishes the listed outcomes and a140HP contribution for the round2 gun. It does not establish a universal claim over openings or turrets. Likewise, "Any counter that forecasts the deterministic policy and buys the cheapest attack that leaks for one round wins" needs the explicit condition that its own defense remains successful, that it survives, and that the final HP comparison favors it. Exact forecasting alone guarantees none of these. Verdict: OPEN as universal claims; the recorded counter wins are CONFIRMED. Suggested scope: the tested guarded forecasting counters preserve their early advantage in the recorded games. No new matches are inferred from this wording review.

## 2026-10-31T06:54:52.026787+00:00 Cost-threshold adaptation: local improvement, broader regressions

Claim: requiring greater expenditure on turrets covering the opponent's route repairs the useful-gun counter. Method: three thresholds30,60,120; the same cheap opening guard and frozen economy15 leak continuation; ten declared development opponents, both seats. All60 games pass strict checks and unchanged-engine replay. All30 seat pairs have identical normalized histories. All16 threshold30 controls reproduce the prior geometric-filter histories exactly. There are no failures, errors, rejected actions or source changes.

Result: threshold30 scores16W2D2L, threshold60 scores12W4D4L, and threshold120 scores10W4D6L. Candidate-first HP, equal in both seats:

| Opponent | Threshold30 | Threshold60 | Threshold120 |
| --- | --- | --- | --- |
| economy13 | W783:768 | L-57:750 | L-397:750 |
| guarded tier4 round8 | W800:-29 | L620:752 | L620:752 |
| useful gun(3,1) round3 | L-40:440 | D-40:-25 | D-40:-25 |
| fortress22 | W775:615 | W775:615 | L770:795 |
| fortress21 | W800:735 | W800:735 | W800:795 |

The other five opponent outcomes and margins are unchanged: best_v9a and lead7 W800:795; round2 bluff and eco6 W100:-49; round3 bluff D-40:-49. Equal margins do not imply equal histories. Twenty of40 cross-threshold comparisons have identical full trajectories. Every changed candidate history first changes its actions in round4; opponents other than the fixed useful-gun policy can react in later rounds. This is evidence for a policy tradeoff, not an isolated causal claim about later damage.

Verdict: CONFIRMED for changing the useful-gun loss to a simultaneous-destruction draw; REFUTED as an overall repair on this declared set. Exposure thresholds based on the isolated-copy theorem are being tested separately. Artifacts: runs/validation/defense-strength-guard-{audit,control-check,comparison,replay-audit}-001.json. Summed match wall times841.181s; largest candidate call4.478s; replay14.511s.

Reserved-A update: the independent loss diagnostic confirms both factory-prefix05 losses have equal800:800 HP after the prescribed round1, then exactly10 candidate damage in round2 and no other damage in the whole game. Thus the790:800 margin is created after the prefix. No claim of inevitability follows. Evidence: runs/validation/reserved-loss-diagnostic-partial-001.json. The new conservative holdout audit003 also checks1760 undated team rows, with zero exact parameter overlaps; these rows are no longer excluded merely for missing timestamps. The complete recognized coverage is51 registered validation campaigns/700 jobs,159 team stream snapshots,10856 dated pre-cutoff rows,1760 undated rows.

## 2026-10-31T07:02:17.923903+00:00 Exposure-threshold adaptation and an independent capacity proof

Claim: qualifying turret presence by exact isolated-copy exposure repairs the useful-gun failure without harming the wider declared set. Method: thresholds1,70,180 on the same ten development opponents, both seats; unchanged cheap guard and frozen economy15 leak continuation. Result: threshold1 gives16W2D2L; thresholds70 and180 each give12W4D4L. All60 strict checks and original-engine replays pass;30 normalized seat pairs agree exactly; all20 threshold1 controls match cost30. Twenty-eight of40 cross-threshold trajectories agree exactly. No errors, rejected actions, timeouts or source changes.

Candidate-first HP, equal in both seats:

| Opponent | Exposure1 | Exposure70 | Exposure180 |
| --- | --- | --- | --- |
| economy13 | W783:768 | L-57:750 | L-397:750 |
| guarded tier4 round8 | W800:-29 | L620:752 | L-40:650 |
| useful gun(3,1) round3 | L-40:440 | D-40:-25 | D-40:-25 |

The other seven opponents have identical complete trajectories across thresholds, including fortress21 W800:735 and fortress22 W775:615. Every changed candidate action sequence first diverges in round4; the economy and guarded-schedule opponents first change actions in round5, while the fixed useful-gun policy changes no action. Summed match wall time667.956s, largest candidate call4.006s, replay15.248s. Artifacts: runs/validation/exposure-guard-{audit,control-check,comparison,replay-audit}-001.json. Verdict: CONFIRMED for the useful-gun loss-to-draw change; REFUTED for no wider regression. The exact isolated-copy statistic does not supply a general policy-strength guarantee. These are development conditions; poolB remains unused.

Claim: the economy lane's full-map capacity argument is sound under its explicit hypotheses. Method: independent standalone informal proof in experiments/validation/analysis/full_map_capacity/PROOF.md, followed by component checks on four legally reached full maps. Result: all56 checks pass, including2880 attempted constructions rejected without mutation and40 original-engine combats spanning roster sizes1,17,250,251,500 with and without an expired prefix. The proof makes the arrival cutoff explicit and gives the exact count of eligible dense roster indices. It extends the statement to any standard minion with HP greater than the map's splash exposure. Verdict: CONFIRMED for the stated capacity bound and permanent construction obstruction. Affordability of the required flood, survival of the attacker and availability of a late round remain additional hypotheses; a universal eventual-win claim is OPEN. Evidence: runs/validation/full-map-capacity-check-001.json. The checks do not establish a bot-strength result.

Reserved-A update:48 original valid results and two retained timeouts at07:01:11, hence50 selected valid conditions including the successful retries. Invocation9 continues the remaining ten asymmetric-prefix cases. Standard score remains10W10D. Full final accounting is still OPEN.

## 2026-10-31T07:04:09.829070+00:00 Capacity certificate for the economy15 leak late-flood loss

Claim: the full-map obstruction and damage-capacity bound apply to the recorded round48 loss against endflood(forecast_lock), not only to synthetic fixtures. Method: select both assignments from runs/economy/endflood1, archive the two exact logs, replay all48 rounds through the unchanged Engine, and derive the certificate from the pre-round48 map and the legally applied attack purchases. Result: both full replays agree exactly. Before round48 the defender has790HP, route length56, splash exposure910 and total per-tick gun damage717; all non-route cells are occupied. The attacker has1000 active tier5 entries, of which776 spawn soon enough to arrive. At most floor(250*717/(1500-910)) =303 eligible copies can die, so at least473 arrive, dealing at least66220 damage. Actual damage is80920 from578 hits. The defender ends at-80130HP and the attacker at256HP in both seats.

Verdict: CONFIRMED for inevitable destruction of this fixed defender base under the specified1000-entry purchase. No legal defender construction can change the map at that point. This is not proof that the entire game outcome is forced: another offensive purchase could conceivably destroy the opponent too and force a draw. The certificate does not claim that the map was unavoidable earlier. Artifacts: runs/validation/recorded-capacity-loss-002/audit.json and its archived seat logs. The first checker attempt expected only engine metadata and stopped on the harness's three additional metadata fields; its source and diagnostic remain in recorded-capacity-loss-001. The corrected checker verifies those fields against the selected result, then checks every engine record. This was a checker compatibility failure, not a game result. Full replay time5.627s for both logs; no bot decisions are re-executed.

## 2026-10-31T07:06:44.867986+00:00 Adaptive forecast audit: private history must persist

Claim: the current public_factory forecaster is exact against Lead10 with attack_mode="adaptive". Source inspection finds that PublicFactoryModel creates a new factory instance on every prediction, while Lead10 keeps pending and failed across rounds and switches from current to robust after an unsuccessful attack. Thus the existing wrapper does not satisfy the known-state induction hypotheses in analysis/stateful_forecast/PROOF.md. The source docstring already warns that stateful targets can disagree. Verdict: OPEN for actual mismatches on the lead screening games; exactness is not established by that wrapper. I am freezing Lead10 in my owned snapshot directory and comparing fresh versus persistent models under the same declared development timings. This does not use reserved poolB or change best_v9a.

## 2026-10-31T07:08:37.248587+00:00 Reserved pool A complete for frozen best_v9a

Claim: the frozen submission completes the predeclared independent pool A with valid, reproducible outcomes. Method: 10 held-out opponent parameter settings, both assignments, standard starts plus two separately scored legal-prefix continuations. The exact frozen candidate SHA256 is `88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d`. All 60 selected results pass strict accounting and full unchanged-engine replay; all 30 assignment pairs have identical normalized trajectories. The two original standard mirror attempts exceeded 300 seconds. Both separately archived retries, allowed 500 seconds, completed and replayed; the failed attempts remain in the accounting. No failed attempt is assigned a game outcome.

Result: standard starts 10W10D0L; one-round factory prefix 6W12D2L; asymmetric splash prefix 6W12D2L. The factory-prefix losses finish 790:800. The asymmetric-prefix losses finish 660:800. All four loss margins arise after the prescribed first round, not from damage inherited at the prefix boundary. The complete tables, exact opponent definitions and timing summaries are in runs/validation/final-best-v9a-poolA-summary-001.md. Selected match times sum to 2773.317 seconds; actual time from campaign start to the last selected completion is 3242.685 seconds. These are different quantities.

Verdict: CONFIRMED for these declared conditions. The result does not establish universal dominance or independent random-sample confidence. Shared policy implementations and exact parameter separation are documented in the summary and holdout-separation-audit-003.json. Pool B remains unused. Accounting: final-best-v9a-poolA-final-audit-001.json; replay linkage: final-best-v9a-poolA-final-replay-check-001.json; loss accounting: reserved-loss-diagnostic-final-001.json, all under runs/validation/. The source closure still matches the freeze.

Persistent forecast implementation is now available as `bot_research.bots.counters.stateful_public:@timing`, with the same model_spec/model_parameters and timing arguments as public_factory. It creates one private model per game and requires exactly one call per reached round starting at round1. The Lead10 development snapshot is bots/counters/snapshots/lead_ten_001.py, SHA256 2c3f4f7ec4698e24299801f8cc2fc0cd07bd7d9b6ccece1db8bd627273ce3eec. The declared forty-game comparison uses C2 adaptive, ten timings, two seats, fresh versus persistent models, attack_share=1 and count_cap=1000. This is a development audit, not use of either reserved pool. Results are pending.

### 2026-10-31T07:09:01.407727+00:00 Observed fresh-model mismatch

The first completed fresh-model condition, tier3 round3 against the frozen Lead10 C2 adaptive setting, now has a strict independent check. Forecasted action lists disagree with the actual target at rounds8,11,13,14,16,17,19; the first mismatch is round8. Both assignments record the same mismatch rounds. Verdict: REFUTED for exactness of the fresh-model forecast on this condition. Its observed800:774 counter win does not make the forecasts exact. Evidence: runs/validation/stateful-lead-ten-preliminary-001.json, including the first predicted and actual action lists. Full comparison and engine replay remain pending. Please avoid treating the public-factory adaptive screen as an exact-policy exploitability screen. The persistent wrapper above is intended to meet that condition and is being tested.

## 2026-10-31T07:21:08Z Follow-up on forecast scope and Lead13 counters

The fresh Lead10 model's full-action mismatch does not by itself prove a construction mismatch. For the captured Lead10 source with planner=v7 and foreign_planner=None, pending/failed are read by the attack step after all construction. The standalone source-level argument is in experiments/validation/analysis/construction_projection/PROOF.md. It shows equality of the ordered construction subsequence under equal current public observations and deterministic helpers. Wrong predicted minion purchases can still change the counter's defense and later history. Full forty-game comparisons, projection counts and original-engine replay remain pending; no claim of changed win rate yet.

A persistent schedule wrapper is now available as bot_research.bots.counters.stateful_schedule:@make, with public_schedule's parameters. It invokes the target clone once in every reached round, including rounds with no scheduled purchase. Like stateful_public, it currently requires a standard start with the target's ordinary fresh private state. The lead screen's public mixed and schedule wrappers still create fresh targets; please use the persistent schedule form for adaptive or sticky-state targets if scheduling waves. Lead13's fortress flag is another private state variable and is outside the Lead10 construction argument.

I captured Lead13 in bots/counters/snapshots/lead_thirteen_001.py and prepared a declaration script for three settings: splash_insurance=true, fortress_n=4, fortress_n=2, each with C2 adaptive parameters. The intended screen combines seven mid-tier timings with six opening/repeated-wave schedules, both assignments. This is development only and has not yet launched. Reserved pool B remains unused.

## 2026-10-31T07:31:49.976492+00:00: Fresh versus persistent Lead10 comparison complete

Claim: resetting the C2 adaptive opponent factory every round predicts its full action list exactly. Method: forty predeclared standard games, ten timings in both seats for each model; per-round ordered action projections, full-history comparisons, and fresh unchanged-engine replays. Result: fresh made 136 full-action errors in 1,000 forecasts, with 136 minion-purchase errors, 60 factory-purchase errors and zero construction errors. Every fresh game had an error. Verdict: REFUTED for full actions; CONFIRMED on these observations for the construction projection proved for this fixed Lead10/v7/no-foreign-planner snapshot. That proof does not extend automatically to Lead13 sticky fortress state.

Claim: the persistent factory remains exact when initialized with the same known private state and advanced once per round from the standard start. Result: zero errors in all 1,000 persistent forecasts. Forty games were legal, all original-engine replays passed, and all 20 reversed-seat pairs had identical normalized complete trajectories. Verdict: CONFIRMED on the declared observations, with the general conditional argument in analysis/stateful_forecast/PROOF.md.

Claim: correcting the forecast improves outcomes on this timing set. Result: both styles score 10W10D0L with identical final HP in all 20 comparisons. Counter-first HP by timing: T3r3 800:774, T3r5 800:774, T4r5 800:740, T4r7 800:800, T4r9 800:800, T5r7 800:800, T5r8 800:520, T5r9 800:240, T5r10 800:800, T5r11 800:800. Verdict: REFUTED on this set. Nevertheless all 20 complete histories differ. Opponent action lists are equal across each comparison. At T3r3 round8, a false two-tier1 forecast induces one extra gun1, leaving the fresh counter with 130 factories/1972 gold versus the persistent counter's 131/1997. Wider outcome effects remain OPEN.

Candidate decision-time totals: fresh410.603s and persistent694.445s; maxima5.770s and7.830s. Shared-machine measurements are descriptive. Maximum submitted attack count5 does not establish cap1000/cap200 equivalence for hypothetical attack selection. Full evidence and condition table: runs/validation/stateful-lead-ten-summary-001.md and companion JSON, backed by audit/comparison/projections/replay-audit receipts of the same prefix. Lead13 mid-tier screens use retained state throughout. Pool B remains unused.

## 2026-10-31T07:35:03.827049+00:00: Forecast-defended grower defeats fixed C2 adaptive

Claim: a growth-through-round6, repeated-tier5 policy with delayed forecast defense can defeat the fixed Lead10 C2 adaptive setting. Method: turret round0 or2 crossed with first defense round1,4,6,8, both player assignments; sixteen predeclared standard starts, persistent public-history target model. Result: 16W0D0L, all eight seat pairs have identical normalized complete histories, all sixteen unchanged-engine replays pass, and all 476 full-action forecasts are exact. The two original120s timeouts (no turret, defense from8) remain recorded; separate300s retries completed them. Verdict: CONFIRMED for these conditions.

Conditions, counter-first HP and end round: turret0_defend1 800:-320 r10; turret0_defend4 755:380 r50; turret0_defend6 725:380 r50; turret0_defend8 645:380 r50; turret2_defend1 800:-40 r10; turret2_defend4 755:520 r50; turret2_defend6 725:-40 r9; turret2_defend8 695:-320 r9. Candidate decision sum389.689s, maxcall4.992s; selected match sum791.072s. Shared-machine timing is descriptive.

Whether forecast-based defense is necessary remains OPEN. A no-defense control has not run, and these wins alone do not isolate a mechanism. They also do not establish strength against Lead13 insurance. Evidence: runs/validation/forecast-grower-summary-001.md and JSON, strict/forecast-audit/replay-audit receipts of the same prefix. Pool B remains unused.

## 2026-10-31T07:39:52Z: Stateful wrapper integration and new controls

Claim: the schedule and mixed-search wrappers retain a target model across rounds before, during and after an attack. Method: a counting-factory target whose purchase count reveals a reset, two wrappers, both player assignments, four original-engine rounds per prefix. Result: all sixteen forecast lists match the actual target lists and every submitted action is accepted. Verdict: CONFIRMED for these component fixtures. Receipt: runs/validation/stateful-wrapper-check-001.json. New mixed entry point is bots/counters/stateful_mixed.py:@mixed, with the same search parameters as public_factory:@mixed. Full-game validation of this new mixed wrapper remains OPEN; the Lead13 schedule campaigns are already using stateful_schedule.

The no-defense grower controls are now running: experiments/validation/forecast-grower-nodefense-001.json, four standard conditions. Defense starts at round51, while all growth, purchase caps and the optional round2 gun are preserved. The unused forecast can be removed entirely under the hypotheses in analysis/blind_grower/PROOF.md (result24). That proof was written before these controls completed. The new audit_blind_grower.py will compare the corresponding blind FeatureBluff action list on every replayed public observation; its run is pending.

The Lead13 screens have recorded 120-second timeouts, which are retained separately from outcomes. In particular, fortress_n=4 case0009 and case0010, splash case0004, and fortress_n=2 case0000 timed out. Completed raw results include a tier4 round5 leak of60 against fortress_n=4 (seat0), and tier3 round4 leaks of52 against splash insurance (both seats). These are provisional examples, not complete or independently replay-audited campaign verdicts. All three manifests remain development work; pool B is unused.

## 2026-10-31T07:44:20Z  No-defense grower controls and information ablation

Claim: enabling the tested defensive policy reverses the blind grower's loss against fixed Lead10 C2 adaptive when no early gun is built. Verdict: CONFIRMED for the declared standard-start conditions.

Method: four post-result controls, declared at 07:35:03 UTC, retain the forecast computation but defer all defense until round 51. They otherwise use the same growth through round 6 and repeated tier5 spending as the sixteen completed defensive games. A separate original-engine observation audit recomputes an equivalent blind FeatureBluff every round. Both player assignments are tested.

Result: without the gun, both controls lose at round 12 with counter/opponent HP -125:520. With the round-2 gun, both controls win at round 9 with HP 605:-460. All four games pass strict source/legality checks and unchanged-engine replay; both normalized seat pairs have identical full trajectories. The independent blind-policy recomputation matches all 42 actions. No forecast mismatches occur, although the predictions do not affect the disabled defensive branch. All sixteen original defensive conditions win. The sixteen descriptive defense-versus-control comparisons have different full trajectories and reuse these four baselines; they are not sixteen independent baseline samples.

Claim: accurate opponent forecasts are necessary for the defensive grower's wins. Verdict: OPEN. The defense-off comparison changes the whole defensive policy and does not isolate the value of prediction. Moreover, the round-2-gun blind baseline already wins, so defense is not necessary for that result. A visible-roster ablation was declared at 07:43:57.130569 UTC with the same eight gun/defense-start settings and both seats. It assumes no new purchases, loads no opponent implementation, and preserves the spending controller. Its expected forecast mismatches will be reported separately from game validity. The new sixteen games are running as development work; pool B remains unused.

Evidence relative to bot_research/: runs/validation/forecast-grower-nodefense-summary-001.{json,md}; runs/validation/forecast-grower-nodefense-{strict,forecast-audit,blind-audit,replay-audit}-001.json; runs/validation/grower-defense-comparisons-001.json; experiments/validation/visible-grower-001.json; analysis proof 24 at experiments/validation/analysis/blind_grower/PROOF.md.

## 2026-10-31T07:46:57Z  Scope check for the lead's v15 immunity attack

Claim: post-construction splash exposure at least the largest allowed minion HP guarantees zero damage in the current combat, including on a map that also contains guns. Verdict: CONFIRMED under the explicit fixed-combat-map hypotheses in proof 25, experiments/validation/analysis/current_immunity/PROOF.md. Every hypothetical arriving copy would have received at least its full HP in splash damage before arrival; guns only add nonnegative damage. No strength claim follows from this certificate.

Claim: permanent buildings alone establish immunity for all later rounds. Verdict: OPEN as an application to v15, and not justified by permanence alone. Later buildings can change the selected route; unchanged geometry or rechecking the final map is sufficient. The default v15 walls_first=True branch checks an observation containing the proposed construction. The nondefault walls_first=False branch appends late plan_walls actions without rebuilding o2 before _immune(o2, rules), so its check refers to the earlier map. This is a source-order finding, not a reproduced match failure. No change is requested for the default solely on this evidence.

The proposed current-response attack after saturation is worth testing, but defensive safety does not prove that spending instead of growing is optimal or that the opponent fails to defend. Keep the distinction between the proved current-combat certificate and the empirical attack-policy claim. The source review used experiments/lead/v15.py and harness/gamekit.py; no held-out definitions were consulted.

## 2026-10-31T07:53:30Z  Audited partial frontier at the first shift boundary

Claim: an exact opponent forecast is necessary for the no-gun grower's wins when defense begins at round 1 or round 4. Verdict: REFUTED for those two declared standard-start conditions against fixed Lead10 C2 adaptive, in both player assignments. Replacing the model with an empty-action assumption still wins: defense from round 1 ends 780:-180 at round 9, and defense from round 4 ends 673:380 at round 50. The exact-model counterparts were 800:-320 at round 10 and 755:380 at round 50. Both visible-model seat pairs have identical normalized full trajectories. These interventions change the trajectories and final HP, but retain the wins. No claim of equal strength or equal computation cost follows.

The visible-roster campaign is incomplete: five of sixteen conditions have completed, all legal wins; eleven are unstarted and there are no timeouts so far. Its fifth game, defense from round 6 in seat 0, wins 643:380 at round 50; seat 1 remains pending. Across the five games, 156 of 168 full-action forecasts differ, including 40 construction, 17 minion-purchase and 150 factory-purchase differences. All five original-engine replays pass. Exact-versus-visible full trajectories differ in all five comparisons; first counter action changes are round 1 for defend1 and round 6 for defend4/6. The overall sixteen-condition information comparison remains OPEN.

The three Lead13 matrices also remain OPEN. Fortress4 has eleven valid games (six counter wins, five draws), five recorded 120-second timeouts and ten unstarted conditions. Splash has five valid counter wins, four recorded timeouts and seventeen unstarted conditions. Fortress2 has three timeouts, no completed game, and twenty-three unstarted conditions. All sixteen completed Lead13 games pass strict source/legality checks and original-engine replay; their 800 forecasts exactly match actual target submissions. No ranking over the incomplete matrices is justified, and the twelve timeouts are computational failures, not game losses.

Examples on completed paired conditions: fortress4 concedes 26 HP to tier3 at rounds 3 and 5, draws against tier3 at round 4 and tier4 at round 4; splash concedes 26 HP to tier3 at round 3 and 52 HP at round 4. Remaining one-seat results are retained in the receipt, not silently treated as completed pairs.

Evidence relative to bot_research/: runs/validation/shift1-frontier-checkpoint-001.json; visible-grower-partial-{strict,forecasts,replays,comparisons}-001.json; lead-thirteen-{fortress4,splash,fortress2}-partial-{strict,forecasts}-001.json; lead-thirteen-partial-replays-001.json. The new audit_forecast_interventions.py passed the four-game, 42-round exact-model control and the inexact-model games, separating forecast errors from invalid games. Partial receipts intentionally report unresolved conditions and return status 2; this is expected accounting, not a concealed validation failure.

Protected-file inventory at 07:50:49.797468 UTC still matches all 903 entries from the initial inventory, with zero additions, removals or changes. The supplied manifest's 1002 missing entries and three pre-existing mismatches are unchanged. Existing tests pass again: 59 tests run, 9 skipped, 35.390 seconds. Artifact runs/validation/integrity-shift1-end.json and existing-tests-shift1-end.log. Final resource/path scan is still in progress as of this entry; no new game batch will start in this shift.

## 2026-10-31T07:57:13.667149+00:00  First-shift integrity and resource close

Claim: this lane's protected files remain at the supplied starting state and its recorded resource use stays within the run limits. Verdict: CONFIRMED for the recorded checks. Integrity at 07:50:49.797468 UTC found zero changes among all 903 initial protected entries, preserving the known manifest discrepancies. The unchanged test suite passed 59 tests with 9 skipped. Resource/path scan at 2026-10-31T07:56:03.445757+00:00 covered 10705 owned text files, including these notes, and found no absolute local paths. Total owned project and lane size was 1673658105 bytes; filesystem free space was 111624114176 bytes. Active logs and this final note may add a small amount after the scan.

All lane computations have stopped for the shift handoff. The visible-roster and Lead13 matrices remain explicitly incomplete as documented above. Pool A is complete; pool B is unused. The overall research run continues in the next shift. Evidence: runs/validation/integrity-shift1-end.json, existing-tests-shift1-end.log and resource-path-audit-003.json.

## 2026-10-31T08:00Z  Second-shift continuation

Claim: protected project files still match the first-shift starting inventory. Verdict: CONFIRMED. The read-only check at 07:59:56.299481 UTC found the same 903 entries, with no additions, removals or changed bytes. The supplied manifest still has its known 1002 absent entries and three pre-existing hash differences. Evidence: runs/validation/integrity-shift2-start.json.

The visible-roster grower ablation and the original Lead13 fortress4 and splash screens have resumed. Pool B remains unused pending an explicit new freeze. The existing result summaries remain partial; resumed games will be audited before any completed-campaign claim. The stronger fortress4 preference in the lead's latest notes does not erase the declared fortress2 conditions or their timeout records.

## 2026-10-31T08:08Z: A sharper fixed-map attack-capacity certificate

Claim: the earlier gun-capacity bound can be tightened using the union of the
actual firing opportunities against eligible appended copies, and the smallest
homogeneous package satisfying that bound can be found without a combat search.
Method: wrote standalone informal proof 26 at
`experiments/validation/analysis/fixed_gun_support/PROOF.md`, then implemented
`bots/counters/fixed_capacity.py`. For each gun, OR the route-coverage bitset
shifted by every eligible birth tick. Its damage times the number of set bits
bounds its total damage to the selected package. If each selected copy has HP
H greater than per-copy splash S, at most floor(C/(H-S)) eligible copies die.
After one complete 250-entry spawn cycle the firing supports stop growing;
eligible copies continue growing periodically. Enumerating the first cycle and
solving the remaining 250 residue classes gives the smallest count certified
by this bound. It need not be the smallest actually lethal count.

Result: `runs/validation/fixed-capacity-component-001.json` completed at
08:07:47.833209 UTC in 22.603142 seconds. Four legally constructible full maps,
seven roster offsets, four requested damage thresholds: all 7,028 support/count
comparisons and 112 minimum-count comparisons passed independent explicit-set
and exhaustive checks. All 60 original-combat comparisons also passed, with
mixed earlier rosters, expired entries, offsets crossing 250, and packages
containing up to 500 tier5 entries. The minimum-count checks include an
80,000-damage request to exercise more than one complete spawn cycle.

Verdict: CONFIRMED for the stated fixed-map bound and finite component checks.
The helper `certified_purchase` selects the cheapest affordable sufficient
homogeneous package, counting only active earlier roster entries. Its default
`require_full=True` rejects maps on which further construction is possible.
Only a full map makes the bound valid against every legal simultaneous defender
submission. Setting `require_full=False` changes the claim to the current fixed
map. Neither mode proves attacker survival. No bot-strength or new match-outcome
claim follows from these checks. A probe of the lead's recorded v15 games is
running to determine whether this offers useful opportunities beyond the
60-copy attack limit.

## 2026-10-31T08:12Z: Shift-2 coordination and capacity follow-up

The lead's 08:10Z request is received: pool B remains unused until an explicit
best_v9b freeze, currently planned for 11:00-12:00Z. New counter work will target
V4, the stateful v15 setting with fortress_n=4 and immune_attack=true. The
unfinished Lead13 screens will retain their original attempts and be reported
as partial development evidence; no further Lead13 retry campaign is planned
while this newer target takes priority. The currently running fortress4 batch
will finish its bounded invocation.

The conservative capacity helper found no affordable certified lethal package
in any retained state of the eight selected v15 matches from lead t6
(`runs/validation/lead-capacity-probe-001.json`). This refutes its immediate
usefulness as a lethal-attack detector on those recorded states; it does not
show that larger attacks would fail. A separate, declared one-round
intervention study has replayed all eight histories successfully and measured
60-copy, half-gold and all-gold purchases at the earliest/latest eligible
states. Its detailed results are being reviewed. No full-game improvement is
claimed by that diagnostic.

## 2026-10-31T08:15Z: Larger one-round attacks do not fix the checked v15 failure

Claim: the 60-copy cap explains v15's failure to damage fortress v22 in the
recorded late-game states. Method: preregistered diagnostic
`experiments/validation/capacity-interventions-001.json`, then replayed all eight
retained v15 histories through the unchanged engine. For each, selected the
first and last round with own post-construction S >= 1500, opposing current
S < 1500, and enough remaining gold for at least 61 tier5. Kept the recorded
construction and opposing submission, replaced own purchases by 60 tier5,
half-gold tier5, or all-gold tier5. This is a one-round intervention, not a new
full-game result.

Result: only V2 against v22 had eligible rounds: 23 through 30 in both seats.
At round 23 the budget was 45,941; counts 60, 35 and 70 all dealt zero damage.
At round 30 the budget was 112,168; counts 60, 86 and 172 also all dealt zero.
Every corresponding current-map prediction was zero as well. The target's
S rose from 1230 to 1510 in its actual round-30 submission. HP remained
590:785 in every branch. The V4 games had no state meeting all the declared
selection conditions. Eight complete original histories and twelve branches
passed; receipt `runs/validation/capacity-interventions-001.json`, completed
08:11:38.366391 UTC in 16.640056 seconds.

Verdict: REFUTED for this proposed fix on these selected states. A larger
one-time pure-tier5 purchase was insufficient even on the prior fixed map.
Repeated purchases or other times would be different hypotheses. This does
not invalidate the capacity bound; its earlier conservative check correctly
found no affordable certified lethal package in these histories.

## 2026-10-31T08:16Z: V4 counters and known-prefix model verification

Claim: a private stateful model can remain exact through the lead harness's
known scripted opening. Method: standalone proof 27, then an opening wrapper
that calls its underlying policy every round and returns the prescribed
opening when applicable. It uses the unchanged `harness/scenarios.py` and
was compared directly with `TimedBot` on mirror:1:2, asym:3:2, mirror:22:3 and
asym:23:2, both seats, through round five.

Result: all 40 forecast, call-count, adapter-agreement and legal-action checks
passed in 5.055935 seconds at 08:13:51.075875 UTC. Receipt:
`runs/validation/prefixed-v4-components-001.json`. The wrapper does not suppress
policy exceptions; successful games must have none. This protocol differs
from pool A's continuation stress tests, where underlying calls were skipped
during the prescribed prefix.

Verdict: CONFIRMED for the conditional proof and these component checks.
Full-game work is now running: 26 standard V4 timing/schedule conditions and
24 known-prefix conditions (three counters across the four named development
openings, both seats). The latter are explicitly excluded from standard-start
strength totals. V4 source is snapshotted unmodified in
`bots/counters/snapshots/lead_fifteen_001.py`, SHA256
`1b7485efc6dae9ba3c1409ee4089a79092430c2aa6c61fb21761f1857abed43a`.
Reserved pool B remains unused.

## 2026-10-31T08:20:38Z: Visible-roster ablation completed, exact forecasts unnecessary for these wins

Claim: the forecast grower's wins against the fixed Lead10 C2 adaptive policy
require exact predictions of the opponent's submitted actions. Method: keep
its growth rounds, tier5 flood, optional round-2 gun and defensive start round;
replace the private opponent model by an empty future submission, so defense
uses only the currently visible roster. Eight settings, both assignments,
standard initial state. Declaration: `experiments/validation/visible-grower-001.json`.

Result: both the original exact-model controller and the visible-roster
controller win all sixteen conditions. The visible controller has no rejected
actions or bot errors. Its sixteen primary results pass strict source checks;
all eight reversed-seat pairs have identical normalized complete histories.
All seventeen completed attempts pass full unchanged-engine replay. The one
original 180-second timeout remains recorded; a separately declared 300-second
retry resolved it and repeated the other seat as a control, with no outcome
or trajectory disagreement. The sixteen matched exact/visible histories all
differ, so this is a substantive policy intervention rather than duplicated
play. The deliberately empty prediction differs from actual submissions in
442 of 474 primary rounds: 130 construction, 56 minion and 422 factory
mismatches, with overlap.

| Early gun round; defense from | Exact-model final HP | Visible-roster final HP | Exact / visible ending round |
| --- | --- | --- | --- |
| 0; 1 | 800:-320 | 780:-180 | 10 / 9 |
| 0; 4 | 755:380 | 673:380 | 50 / 50 |
| 0; 6 | 725:380 | 643:380 | 50 / 50 |
| 0; 8 | 645:380 | 633:380 | 50 / 50 |
| 2; 1 | 800:-40 | 735:-180 | 10 / 10 |
| 2; 4 | 755:520 | 709:660 | 50 / 50 |
| 2; 6 | 725:-40 | 635:-40 | 9 / 9 |
| 2; 8 | 695:-320 | 665:-460 | 9 / 9 |

HP is counter first; each row holds in both seats. Verdict: REFUTED for the
necessity claim on these sixteen conditions; CONFIRMED that the simpler
visible-roster controller suffices here. The earlier no-defense control loses
without an early gun and wins with the round-2 gun. Together these tests
support a role for defense in the no-gun conditions, without identifying an
optimal controller. They say nothing yet about V4 or reserved opponents.

Evidence: `runs/validation/visible-grower-{strict,forecasts,replay,summary,comparisons}-final-001.json`,
the matching summary Markdown, and
`experiments/validation/visible-grower-final-comparisons-001.json`. Summary
recorded 08:17:48.600813 UTC. Full replay took 26.122138 seconds.


## 2026-10-31T08:26:15Z: V4 known-prefix counter screen, all evidence checked

Claim: the stateful V4 revision resists the declared mid-tier timing and drip
counters on all four known development openings. Method: three fixed attack
rules (all-gold tier3 in round 5, all-gold tier4 in round 7, one tier4 in each
round 5 through 9), four legal opening prefixes, both assignments. Both the
actual target and its private model advance during opening rounds. These are
continuation scenarios, excluded from standard-start strength totals.

Result: from the counter's perspective, 2 wins, 1 draw and 21 losses in all
24 declared conditions. Both wins are the tier4 drip on mirror:22:3, ending
495:-105 in round 10. Its round-5 purchase is unaffordable; it buys one tier4
in rounds 6, 7, 8 and 9. The draw is tier4 round 7 on asym:23:2 with the counter
in seat 1, simultaneous destruction in round 11, -140:-110. All remaining
conditions lose. Complete per-condition HP and round table:
`runs/validation/lead-fifteen-V4-scenarios-summary-001.md`.

All 24 conditions pass strict source and legality checks, with no bot errors
or rejected actions. All 375 primary round forecasts exactly match the
opponent's submitted action list. Every complete replay matches the unchanged
engine (4.285893 seconds). No attempt failed or timed out. Verdict: REFUTED
for resistance to all declared counters, by the mirror:22:3 drip; CONFIRMED
for the recorded outcomes and exact-model execution. The broad failure of the
other counter settings does not validate V4 against unrelated scenario bots,
including econ17 in the lead's separate tests.

Evidence: `runs/validation/lead-fifteen-V4-scenarios-{strict,forecasts,replay,summary}-001.json`.
A follow-up intervention is declared in
`experiments/validation/lead-fifteen-V4-free-scenarios-001.json`: preserve the
same attack rules and target, but let the counter compare legal-cell defensive
fallbacks when its template plan still leaks. The reused fallback is the
unchanged economy v17 free planner. Its 64-round component check passed exact
forecasts, adapter agreement, legal proposals and lexicographic residual/cost
selection in 24.880240 seconds, completed 08:24:02.187712 UTC. Full games are
running; no improvement is claimed yet.

The standard-start V4 screen is still incomplete. A matched information
ablation has also been declared before its runs: same 26 timing/schedule
conditions, but replace the exact V4 model by an empty future submission.
This tests whether the currently visible roster and map suffice for any wins.
The deliberately wrong forecasts must be audited with
`audit_forecast_interventions.py`, not the exact-forecast checker.


## 2026-10-31T08:26:15Z: Retired Lead13 evidence and resource checkpoint

Per the lead's 08:10Z request, the three incomplete Lead13 counter campaigns
are retired in favor of V4. Their combined 78 declared conditions contain
21 valid completions, 18 original 120-second timeouts and 39 unstarted
conditions. Fortress4 has 9 wins and 5 draws from the counter side; splash
insurance has 7 wins; fortress2 has no completed game. This is partial
development evidence, not an aggregate strength score for any setting.

All 21 completed games pass strict source/legality checks, exact forecast
checks and full unchanged-engine replay (16.615557 seconds). Unresolved cases
remain explicitly unresolved. Artifacts:
`runs/validation/lead-thirteen-retired-{strict,forecasts,replay}-001.json`.
Verdict: CONFIRMED for these recorded completions; OPEN for every uncompleted
condition. No timeout is interpreted as a loss.

At 08:23:22.068473 UTC, the resource/path audit counted 1,707,052,246 owned bytes
including lane files, with 132,117,803,008 bytes free on the filesystem. All
11,201 scanned project text files were free of forbidden absolute local paths.
Artifact: `runs/validation/resource-path-audit-004.json`. Active logs can grow
after the check.


## 2026-10-31T08:31:22Z: V4 visible-roster control and a caught source-freeze omission

Claim: the same timing/schedule controller can retain V4 wins while using only
its visible roster and map. Method: replace its private opponent model with an
empty submission, retaining all 26 declared standard-start conditions and both
assignments. Result: all 26 valid games lose from the counter side. Strict
source/legality checks and original-engine replay pass for all 26, with no bot
errors, rejected actions or timeouts. Full replay took 10.788668 seconds.
The exact-model reference campaign remains in progress. Verdict: REFUTED for
this empty-forecast controller on these conditions; the necessity of any
particular forecast component remains OPEN.

Evidence: `runs/validation/lead-fifteen-V4-visible-{strict,forecasts,replay}-002.json`.
The first attempted campaign, suffix 001, is retired and excluded: its static
source closure omitted two modules loaded through the model-factory string.
Runtime source validation caught every completed attempt, producing eight
source failures and leaving eighteen unstarted conditions. No such attempt is
counted as a game outcome. The corrected module places the empty factory in its
own frozen source file; campaign 002 was newly declared and run from scratch.
All original attempts remain in `lead-fifteen-V4-visible-standard-001` and are
accounted for in `lead-fifteen-V4-visible-aborted-001.json`. This is an
experiment-definition correction, not a change to engine behavior.

The first two legal-cell fallback games on mirror:1:2 are now complete and win
795:769 in round 50, where the template-only control lost -3545:769 in round 21.
These are provisional until that campaign's strict and replay audits finish.


## 2026-10-31T08:33:08Z: Focused V4 forecast-component intervention declared

The empty-forecast failure leaves three distinct explanations: the opening
threat prior, later incoming minion purchases, and defensive construction.
The new declaration `experiments/validation/lead-fifteen-V4-projected-standard-001.json`
selects four timings from the first twelve completed exact-model games:
tier3 in rounds 3 and 5, tier4 in rounds 5 and 6. Three were wins, one a draw.
This selection is explicit and outcome-informed; it is a mechanism study.

For each timing and both seats, test (1) exact minion purchases only, (2) exact
non-minion actions only, (3) a fixed three-tier1 prior in round 1 and no later
new actions. The first two continue the full private model once per round and
save its complete predictions for separate checking. The third never calls
an opponent model. All spending rules are unchanged from the timing control.

The component check passed 72 original-engine rounds, both seats and all three
modes: full predictions where present, selected projections, observation
immutability, one call per round and accepted actions. Runtime 25.281403 seconds,
completed 08:32:24.666827 UTC. Evidence:
`runs/validation/projected-v4-components-002.json`. The first check invocation
failed because the check called the callable target with a nonexistent decide
method; the test driver was corrected before campaign launch, and its failed
log is retained. Verdict: OPEN for strategic effects; CONFIRMED for the checked
component execution. Twenty-four full-game conditions are now running.


## 2026-10-31T08:41:41Z: Report review, implication directions and policy clocks

Claim reviewed: section 5.8 of the current report infers that tier5 copies pass
from S=1140 < 1500 by P1. Method: compare that sentence with P1 and the independent
current-immunity proof. Result: P1 is a sufficient condition for immunity. Its
failure does not establish a leak when guns are present or the spawn cutoff
prevents arrival. Verdict: REFUTED as a deduction from P1. The logged eight-tier5
attack is valid empirical evidence for that particular leak. Suggested wording:
"S=1140 does not provide the splash-immunity certificate; the recorded tier5
attack dealt 840 damage." This does not question the recorded outcome.

Likewise, the section 5.7 statement that S>=180 stops all tier1-tier3 rosters is
correct, but that implication alone does not show that a splash-only answer
exists at bounded cost on every current map. Availability and legal placement
are separate hypotheses, as the full-map obstruction proof demonstrates.
Verdict: CONFIRMED for the immunity implication; OPEN for universal availability.
A construction on a compatible master layout or an explicit checked plan is
needed for the claimed existence.

The section 2 phrase "the engine and all bots are deterministic" is too broad.
Frozen fortress v24 still calls plan_defense without time_budget at five call
sites, and its plan.py uses TIME_BUDGET=3.0, time.time(), and deadline-dependent
candidate stopping. Earlier timed fortress versions have the same limitation.
Identical normalized histories in measured pairs are useful reproducibility
checks; they do not remove this possible timing dependence. Verdict: REFUTED
for the universal source-level claim. The engine is deterministic; record
policy timing limits separately. The present V4 standard controller uses v7,
which has no clock cutoff; its v11/v22 alternatives and econ17 use 1e6 seconds,
so their cutoff cannot be reached within our bounded matches. That operational
condition supports determinism for these tested calls, not an unqualified
claim about all policies and all runtimes. Sources: reports/REPORT.md,
bots/defense/frozen/v24/{fortress,plan}.py, experiments/lead/v15.py,
and bots/economy/frozen/v17/econ17.py.


## 2026-10-31T08:43:15.083313+00:00: Guarded opening roster intervention declared

Claim to test: a second tier1 in the cheap guarded opening improves the final result against V4 while retaining enough factory growth. The opening spends gun1 at (3,1), then the declared roster, then all affordable factories; frozen economy17 (free_fallback zero, foreign_attack_from 11) starts in round 2. Five rosters are fixed before execution: empty, one tier1, two tier1, one tier2, and two tier1 plus one tier2. Direct economy17 is a sixth control. Opponents are V4, economy17, and fortress24, both assignments: 36 development conditions. These choices follow earlier guarded-opening results and are not held-out validation. No opponent model is used. Fortress24 retains a three-second internal planner cutoff, so complete paired histories must be checked rather than assumed equal. Opening checks will precede full games. Manifest: experiments/validation/guard-roster-transfer-001.json. Verdict: OPEN.


## 2026-10-31T08:46:34.513125+00:00: Guarded opening check corrected before full games

The first component check failed on an incorrect expectation: gun1 at (3,1) alone does not stop all three opening tier1 copies. The unchanged engine gives 795 HP, one 5-damage arrival, for all five own roster choices. Verdict: REFUTED for the assumed zero-damage guard; no full-game result was produced under declaration 001. The five diagnostic rounds are in `runs/validation/guard-roster-component-failed-001.json`. The candidate actions are unchanged. Declaration 002 points to a new check expecting the observed 795 HP; the original declaration and failed check remain intact. The larger-poke hypothesis remains OPEN.


## 2026-10-31T08:48:34.407035+00:00: Public-budget defense intervention declared

The minion-only result motivates a weaker information model. `budget_timing.py` uses no opponent-policy simulation: three tier1 as an opening prior, then the existing roster plus the frozen planner's finite purchase-package family at one quarter, one half, or all of the opponent's visible gold. Timed attacks, the spending order, factory limit, and round-20 saturation follow the earlier controller. Four timings, chosen in the earlier mechanism study, give 24 development games against V4 with both seats. The half-budget hypothesis is that the early lead survives the added insurance cost. The package family is heuristic and does not prove safety against every affordable roster. Component checks precede full games. Manifest: `experiments/validation/budget-timing-V4-001.json`. Verdict: OPEN.


## 2026-10-31T08:50:41.641427+00:00: V4 timing screen and forecast ablations fully audited

Claim: V4 removes the earlier timed medium-unit leaks. Method: 13 declared
standard-start timing/schedule counters, both assignments, exact stateful
public forecasts; unchanged engine. Result: **16 wins, 8 draws, 2 losses from
the counter side**, all 26 valid, no errors, rejections or timeouts. Every one
of 1,300 full-action forecasts agrees with the actual opponent submission;
all full replays pass (47.022773 seconds of replay-audit runtime). All 13
assignment pairs have identical normalized histories. Verdict: REFUTED for
eliminating those leaks. This is development evidence, not held-out validation.
The full table is `runs/validation/lead-fifteen-V4-standard-summary-001.md`.
Tier3 at rounds 3/5 wins 800:774, tier4 at round 5 wins 800:740, and one opening
tier1 followed by tier4 at round 5 wins 800:735. One opening tier1 followed by
tier4 at round 6 loses 780:795. All end in round 50.

Claim: full new-action forecasting is necessary for those counter wins.
The same 26 settings with no new-action forecast all lose (previously audited).
In the focused four-timing intervention, **minion-only forecasts give 6 wins
and 2 draws; non-minion-only forecasts lose all 8; a fixed three-tier1 opening
prior and no later forecasts loses all 8**. Strict source/legality checks,
complete-model/projection checks and all 24 full replays pass. There are 536
complete-model rounds and 680 projected rounds; 594 projected action lists
differ from the actual full submission. Verdict: REFUTED for necessity of the
complete action list on these settings; CONFIRMED for the measured failure of
the empty, non-minion and opening-only controls. No general necessity theorem
for another defense policy follows.

The three winning minion-only settings reproduce all six exact-control
histories. The round-6 tier4 setting is more informative than its equal final
score: the full model predicts zero attack gain and buys nothing; minion-only
predicts 120 and buys two tier4, which do not land. Actions first differ in
round 6, opponent actions in round 7; both still draw 800:800. Opening-only
controls first diverge in round 6 when later incoming purchases start. The
conditional source argument is analysis topic 28, `minion_projection/PROOF.md`.
Lead/Opus review is welcome, especially the explicit sign condition; it makes
no monotonicity claim about construction. Evidence:
`lead-fifteen-V4-projected-{strict,components,forecasts,replay,comparisons}-001.json`
and `lead-fifteen-V4-visible-comparisons-001.json` in runs/validation/.

The new public-budget controller passes 72 original-engine component rounds
(9.380252 seconds). It is now in full-game development testing. The guarded
roster controller passes 270 opening checks (2.506659 seconds) after the
previously documented expected-damage correction; its full games also run.
Pool B remains unused pending the new frozen candidate.


## 2026-10-31T08:55:22Z: Corner-guard geometry hypothesis declared

The 30-gold gun at (3,1) leaks one of three tier1 copies. Moving it to
(10,1) appears to give seven consecutive covered route indices, 8 through
14, without changing cost or the initial shortest route. Nine shots should
kill the three copies by ticks 10, 13 and 16. Claim to check: this opening
preserves all 800 HP against three tier1 while retaining the same purchases
and factory count. The declared component enumeration checks every legal
single-gun1 coordinate against that roster, in both assignments, with the
original Engine. The selected coordinate is fixed before execution. This
is not a claim about every affordable roster or about full-game strength.
Source: experiments/validation/search_guard_geometry.py. Verdict: OPEN.


## 2026-10-31T08:56:09Z: Review of the new foreign-map planner claims

I read hrt-w1's 08:49 entry and the live bots/defense/replan.py source. The
recorded successful layouts provide constructive lower bounds on achievable
route length and splash exposure. A finite annealing search does not provide
an upper bound. Thus the phrases "S 1500 is not reachable", "immunity by
splashes alone is impossible", "routes above 44 do not exist", and "not the
optimum but close" are not established by the reported search. Verdict: OPEN
for these impossibility or near-optimality claims; CONFIRMED only for the
reported constructions, subject to their replay checks. Please use "the
search did not find" unless a separate exhaustive bound is available. This
matters to whether gun capacity is mathematically unavoidable or merely the
best available practical continuation.

The same source terminates the annealing loop when time.time()-t0 exceeds
its time_budget (default four seconds). The random seed alone therefore does
not guarantee reproducibility of the returned layout. Fixed iteration counts
with an unreachable clock cutoff would support that narrower claim; otherwise
the actual stopping iteration and layout should be recorded. Verdict: REFUTED
for unconditional determinism from a fixed seed. This is a source-level review,
not a new match result. Lead/Opus review can resolve the scope before these
claims enter the final report.


## 2026-10-31T09:01:59Z: Model-free budget timing result fully audited

Claim: an exact opponent-policy forecast is necessary to preserve the timed
counter win against V4. Method: 24 declared standard-start games, three
visible-gold fractions, four timings, both assignments; the candidate calls
no opponent policy. All 24 pass strict source and legality checks and full
unchanged-engine replay (49.216783 seconds). All 12 normalized seat pairs
are identical. Result: **2 wins, 12 draws, 10 losses** from the counter side.
The half-budget round-3 tier3 attack wins **800:774** in both seats, at round
50. Verdict: REFUTED for exact-policy forecasting being necessary on this
condition; CONFIRMED for that model-free counterexample. The finite defensive
package family remains a heuristic, not a universal safety certificate.

With half-budget insurance the other three timings draw 800:800. Every
quarter-budget timing loses: tier3 round3 -86:774 at round17, tier3 round5
-266:774 at round17, tier4 round5 -100:740 at round19, tier4 round6 60:800 at
round50. Full-budget insurance draws three timings, but tier3 round5 loses
-180:800 at round11. These whole-policy interventions show that increasing
the nominal insurance fraction does not monotonically improve the final
outcome; they do not yet isolate the spending or placement mechanism.

Candidate: bots/counters/budget_timing.py, make(tier="tier3", attack_round=3,
budget_fraction=0.5). Evidence: runs/validation/budget-timing-V4-{strict,replay,
summary}-001.json; the summary also has a Markdown table. This is development
evidence selected after earlier timing studies, not reserved validation.
Pool B remains unused.


## 2026-10-31T09:02:28Z: Corner-guard claim confirmed; full-game test declared

Claim: one gun1 at (10,1) stops three opening tier1 copies for 30 gold.
Method: enumerate all 142 non-endpoint gun coordinates, both assignments,
using the original Engine; independently inspect the seven covered indices
8 through 14. Result: all 284 engine/local-simulator comparisons pass;
(10,1) takes zero damage, whereas (3,1) takes five. Exactly four single-gun
positions in the enumeration stop the three copies: (9,1), (10,1), (9,2),
(10,2). Runtime 4.727912 seconds. A further 270 opening checks, covering the
five own rosters and all 27 ordered affordable enemy rosters in both seats,
pass legality, observation immutability and seat consistency (5.691060
seconds). Verdict: CONFIRMED for the stated opening claim. Other affordable
enemy rosters need not be stopped.

The complete informal proof is analysis topic 29, corner_guard/PROOF.md;
verification/evidence.json registers the source and checks. There is no
formalization. Moving the gun also denies the opponent the bounty for the
previously leaking copy, so later changes need not be limited to five HP.

Full-game hypothesis remains OPEN. Manifest experiments/validation/
guard-geometry-transfer-001.json was declared at 09:02:16Z before these games:
the same five opening rosters with the corner gun, plus an original-coordinate
one-tier1 control, against V4, economy17 and fortress24, both assignments.
Thirty-six development conditions; the prior roster campaign supplies the
other coordinate controls. The changed geometry may affect every later
building decision, and whole trajectories will be compared. Lead/Opus:
please review the constructive opening argument before using it in a revised
candidate; no full-game improvement is asserted yet.

## 2026-10-31T09:06:40.818303+00:00: Original-coordinate guard roster campaign audited

Claim: spending more of the opening budget on a guarded blind poke improves
performance against strong disclosed opponents. Method: five guarded rosters,
the same gun1 at (3,1), a frozen economy17 continuation, and a direct economy17
control, each against V4, economy17 and fortress24 in both assignments. All 36
complete games pass strict checks and unchanged-engine replay. All 18 normalized
assignment pairs have identical histories, including the observed fortress24
runs; its internal clock cutoff still prevents a general determinism claim.

Result: the two-tier1 opening and the one-tier2 opening beat V4 795:790 and
795:788 respectively. The one-tier1 opening draws V4 795:795. Every guarded
roster loses to both economy17 and fortress24. The largest opening, two tier1
plus one tier2, also loses to V4 at round12, -525:778. Direct economy17 wins
against V4 785:769 and fortress24 750:675, and draws itself 778:778. All games
other than the largest opening versus V4 end at round50. Verdict: REFUTED for
a monotone blind-poke benefit; CONFIRMED for the two small V4 counterexamples
and for the observed loss of strength outside that target. The new corner-gun
intervention is still running and is a separate experiment.

Evidence: runs/validation/guard-roster-transfer-{strict,replay,summary}-001.json
and the accompanying summary Markdown. The campaign has 8 wins, 4 draws and
24 losses including the direct control; that aggregate is not a score for one
policy. Five guarded policies alone have 4 wins, 2 draws and 24 losses. No
reserved validation conditions were used.

## 2026-10-31T09:11:23.934759+00:00: Lead17 snapshot and unchanged timing screen

The new local snapshot preserves v15 byte-for-byte and rewrites only the
v16/v17 imports to owned copies. The source and rewrite manifest is
experiments/validation/lead-seventeen-mid5-standard-001.json. Snapshot
lead_seventeen_001.py has SHA-256
5b87add923ec4c2893c7d8483ff8b3c9205fe270560544c8dd41a0e5a83fe2a3.
The target retains the V4 parameters and adds mid_until=5 and
foreign_policy="econ17".

Claim: the copied implementation preserves the original on the checked
histories. Method: original and copied policies receive separate copies of
identical public observations; compare every action, then advance the
unchanged Engine with the original. Result: all 122 decisions match across
the standard start and mirror:1:2, both seats; the foreign switch fires at
round2 in both prefix games. Runtime 87.743198 seconds. Verdict: CONFIRMED
on these four histories, not a proof for every observation. Evidence:
runs/validation/lead-seventeen-snapshot-component-001.json.

The component opponent was the half-budget tier3 round3 policy. In the two
standard games Lead17 ended 774:800 at round 50; mid_rounds was empty. This
is an early diagnostic that the added insurance may leave this opening
window, with full preserved-match/replay confirmation still OPEN. The
26-game standard timing screen now running reuses all thirteen earlier
V4 timing/schedule settings without selecting only winners. No holdout is
used. Lead/Opus: please review the empty mid_rounds condition if this window
matters to the next candidate.

## 2026-10-31T09:11:23.934923+00:00: Pool C prospectively reserved for late revisions

Pool B remains UNUSED. Because the run continues after the planned midday
freeze, I declared a separate late reserve before testing a later candidate:
experiments/validation/late_holdout_manifest.json, SHA-256
fb3acda48f51b0ce5de9497e43216e9be52a4bb68503d778a3e264614279a06a.
It has twelve untested parameter settings within known opponent families,
plus two new prescribed histories and the standard start, both assignments
(72 conditions). No candidate has been loaded or measured on them. Five
scripted opening rounds were executed solely to validate legal prefixes;
that check is runs/validation/late-holdout-prefix-check-001.json.

The reserve is prospective after the existing development results, not a
random sample of independent policy families. Exact overlap with team
experiments must be audited before calling a condition held-out. Prefix
calls will be skipped and the prescribed actions follow the candidate role
when seats swap. Standard results and continuation stress will be reported
separately. Do not use C until an explicit final freeze of a revision after
B; any revision informed by C retires it from confirmatory use. Verdict:
OPEN for all strength claims; CONFIRMED only for the legal prefix checks.

## 2026-10-31T09:14:43.625252+00:00: why the budget envelope changes the timing counter

Claim: the full-budget variant is uniformly safer than the half-budget variant.
Method: compare complete preserved histories for all four timings and both seats,
including half versus quarter, full, and exact-forecast controls. The 24
comparisons are registered in experiments/validation/budget-timing-V4-pairs-001.json
and recorded in runs/validation/budget-timing-V4-comparisons-001.json.
Result: all 24 pairs differ somewhere. The half-budget tier3-round3 counter
buys one gun1 and two factories in round2, leaving exactly 100 gold for a
tier3 in round3; V4 then loses 26 HP. The full-budget variant instead buys a
60-gold splash in round2, adds no factories, and begins round3 with 80 gold,
so it cannot buy that tier3. It draws 800:800 instead of winning 800:774.
The half and exact forecasters also diverge in round2 but both win 800:774;
matching the opponent's exact action list is unnecessary for this outcome.

At tier3-round5, the full-budget variant does buy one tier3, which V4 stops
with its same-round gun2. By round8 its factory counts are 9 versus V4's 95.
It then takes 140, 280, and 560 damage in rounds 9, 10, 11, dying -180:800.
The half-budget variant buys no tier3 at its round5 gate and instead draws
800:800. Quarter-budget tier3-round3 first differs from half in round4
(five factories versus a gun1 and three factories), begins taking 26 damage
in round7, and eventually loses -86:774 in round17.

Verdict: REFUTED for uniform safety of the full envelope; CONFIRMED for these
recorded affordability and combat mechanisms. Changing the envelope changes
both construction and subsequent income, so this is a whole-policy intervention,
not an isolated estimate of the causal value of one factory. No holdout is used.

## 2026-10-31T09:21:34.244079+00:00: Lead17 round-three insurance loses an affordable joint plan

Claim: the remaining round-three tier3 leak can arise from sequential defense
planning, rather than an unaffordable zero-leak response. Method: reconstruct
the complete public history of lead-seventeen-mid5-standard-001 case0000,
verify the persistent Lead17 action at every preceding decision, and inspect
round 3. Test every alternative with the unchanged apply_action and simulate_map.
The recorded result is counter 800 : Lead17 774 at round 50; full campaign replay
audit is still pending. The component uses the same frozen Lead17 snapshot.

Result: at round 3 Lead17 has 110 gold, its turret-based poke condition is true,
and its fortress trigger is false. Its underlying policy buys a 60-gold splash
at (1,3), leaving 50. Mid-tier insurance receives 30 (share 0.6) and returns no
plan. Even giving that second step all 50 returns no plan, including when
tested against only the actual tier3 roster. All these sequential choices
leak 26 HP. Replanning from the original map and all 110 gold instead finds
one gun2 at (9,5), cost 80, with zero damage against all four publicly sampled
mid-tier rosters and the actual incoming roster. Replanning within 66 (the
original share 0.6) also returns no plan. Runtime 0.888166 seconds.

Verdict: CONFIRMED for this reached state and the existence of the 80-gold
legal defense. A whole-game improvement is OPEN. Raising only mid_share
cannot fix this exact state: the splash has already consumed the needed
budget. A candidate change would need a joint pre-poke plan or comparison
against replacing that earlier purchase, with a larger budget than 0.6.
This costs one early factory relative to the recorded splash choice, so
stronger late opponents are necessary regression controls.

Lead/Opus: please review this counterexample before freezing the next
candidate. Evidence: runs/validation/lead-seventeen-mid3-diagnosis-001.json,
script experiments/validation/diagnose_lead_seventeen.py. The two whole-game
variants and long-term opportunity cost are not established by this component.

The original V4 free-layout prefix campaign has now completed all 24 attempts.
Its preserved timeouts are being retried at 450 seconds under the newly
declared retry manifest; original failures will remain in the accounting.
No reserved pool was used.

## 2026-10-31T09:29:08.912886+00:00: Corner guards win some matchups but do not transfer uniformly

Claim: blocking the initial three tier1 entries with the corner gun is
sufficient for a stronger whole-game continuation. Method: five fixed
opening rosters with gun1 at (10,1), followed by frozen economy17, against
V4, economy17 and fortress24 in both assignments. The extra sixth policy
repeats the earlier gun at (3,1) with one tier1. All 36 games pass strict
source/accounting checks and full unchanged-engine replay (41.792792 s);
all 18 assignment pairs have identical normalized complete trajectories.

Results: against V4, empty draws 800:800; one tier1 wins 800:795; two
tier1 win 800:790; one tier2 wins 800:788; two tier1 plus one tier2 lose
-360:778 in round12. Against economy17, all five lose: respectively
773:800, 753:795, 753:790, 773:788 and 773:778. Against fortress24,
only the one-tier2 corner wins, 775:580; the other four lose. All games
except the V4 overbuy loss finish round50. The original-coordinate
one-tier1 control reproduces 795:795, 783:795 and 770:795 against the
three opponents.

Verdict: REFUTED for uniform transfer; CONFIRMED for the recorded
matchup-specific gains. In particular the corner improves the cheap V4
counter from draw to win, yet the one-tier1 version loses more HP against
economy17 than the old coordinate. The 48-game followup varies coordinate
and the inherited foreign-map attack hold. These are development games.
Evidence: runs/validation/guard-geometry-transfer-summary-001.md and its
strict/replay JSON inputs. Matched full-history comparisons are declared
in experiments/validation/guard-coordinate-pairs-001.json.

The defense worker accepted the earlier proof-scope and clock-cutoff
review. Source inspection confirms that frozen v26 replan.py defaults to
fixed iterations without a wall-clock cutoff. This fixes that search,
but plan.py still uses TIME_BUDGET=3.0 in gun planning, so it is not a
proof of whole-policy determinism. A second source-level concern is OPEN:
the replan objective="best" comparison sums new splash slots only,
whereas _score also counts existing fixed splashes. An independent
component check will test whether those orderings differ on recorded
maps. No claim of an observed wrong choice is made yet.

## 2026-10-31T09:33:10Z: Free-map fallback repairs many scripted-start counter losses

Claim: allowing the exact-public-model counter to consider legal-cell defense
outside its template improves its known-prefix results against V4.
Method: retain all three original timings on all four known prefixes and both
seats. Change only the counter's defensive fallback: when template defense
leaks, compare the template, free planning from the original map, and free
planning after template construction by residual damage then cost. The
opponent and call-through prefix semantics are unchanged. Both complete
campaigns are preserved; the two 300-second failures of the new campaign were
retried under the declared 450-second limit, without dropping their records.

Result: old 2W-1D-21L becomes 14W-2D-8L over the same 24 conditions. Eleven
losses become wins, two losses become draws, and one draw becomes a win;
the other ten W/D/L labels stay the same. All 24 full histories differ.
There are no invalid actions, bot errors, source drift or unresolved
conditions. All 932 primary forecast rounds match actual opponent actions.
All 24 selected games replay through the unchanged engine (21.610780 s).
Six symmetric-prefix seat pairs have identical complete normalized histories;
the other six pairs use asymmetric prescribed maps.

The three mirror:1:2 timings first change counter actions only in round 21:
old late destruction becomes respectively W 795:769, D 795:795, W 795:615,
all at round 50. This is evidence of repaired survival, not a stronger early
attack. On asym:3:2, seat 1 still loses all three timings in round 22; on
asym:23:2 the repeated tier4 schedule still loses both seats. One of these
remaining losses has worse final HP than before, so the intervention is not
a proven monotone improvement in damage or lifetime.

Verdict: CONFIRMED for the stated 24 development conditions; broader
improvement is OPEN. Evidence: runs/validation/lead-fifteen-V4-free-scenarios-summary-001.md, its strict/forecast/replay inputs,
and runs/validation/free-prefix-comparisons-001.json. Reproduce the comparison
with experiments/validation/compare_matched_policies.py and the declaration
experiments/validation/free-prefix-pairs-001.json. The original failed attempts
remain in lead-fifteen-V4-free-scenarios-001; retries are in the separate
lead-fifteen-V4-free-scenarios-retry450-001 directory.

The 36 guard-coordinate comparisons are also complete: all six unchanged
control histories match, while all 30 coordinate interventions differ. This
supports the control accounting for the preceding guard study; it does not
make its matchups independent samples.

Freeze coordination: pool B is still unused. The lead's freeze_v9b log records
successful standard/scenario equivalence and smoke checks, but a test failure
at 09:31Z. Source review identifies the obsolete test call
best:@make?kappa=8, rejected by the new candidate's parameter validation.
The lead owns that test and the freeze decision. This observation is not a
claim of a game failure, and does not authorize using B before the FROZEN note.

## 2026-10-31T09:34:52Z: Explicit best_v9b freeze accepted; pool B queued

The lead posted FROZEN at 09:33Z and confirmed the stale harness test was
fixed. Both best.py and experiments/lead/frozen/best_v9b.py match SHA-256
dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7.
I queued the 60 predeclared pool-B conditions, including both assignments and
the two separately reported continuation stresses, to start after the finite
core29 planner check. The authoritative start is the campaign freeze timestamp,
not this queue notice. Evidence will be under runs/validation/final-best-v9b-poolB-001.
The candidate and all imported dependencies must remain unchanged throughout.
Pool C remains unused. No results from B are available at this point.

The Opus lead independently accepted the round-three diagnosis and is testing
joint mid-tier insurance in the next development revision. The fixed Lead17
26-game timing campaign is now fully audited: all 1300 forecast rounds exact,
26 original-engine replays pass in 35.424303 seconds, 13 identical seat pairs.
Counter outcomes remain 16W-8D-2L. Tier3-round5 changes from a counter win to
a draw, while tier4-round7 changes from a draw to a counter win. The remaining
tier3-round3 win persists. This comparison updates the counter's public model
alongside the target; it is not an intervention holding the opponent policy
fixed. The model-free transfer campaign is running for that separate question.

## 2026-10-31T09:38:04.843559+00:00: Negative replan checks and frozen-entry-point counter protocol

Claim: the differing fixed-splash accounting in replan's final selector
can change its choice. Method: compare the exposure and route searches
with 2500 iterations each, independently reconstruct the complete shortest
route and total splash exposure, and validate every construction prefix
on the original rules. Across replan-selection-001 and -002, all 17
comparisons passed their legal-prefix and replay checks. No selection
counterexample was found. The second group covers two later observations
of a retired pool-A match and two observations of the corner-guard game,
with seeds 0, 2 and 7, including maps with 2, 7 and 14 existing splashes.
The first and second checks took 45.130196 and 51.748333 seconds.

Verdict: OPEN, with negative evidence on these observations. This does not
prove the two scoring formulas equivalent. Frozen v26's replan loop uses
fixed iterations, but its plan.py still defaults to TIME_BUDGET=3.0 for
gun planning, and fortress.py does not override that argument. Therefore
whole-policy repeatability is not established by fixing replan alone.

Pool B began at the actual freeze timestamp recorded in its freeze.json
(2026-10-31T09:34:52.829648+00:00); its supervisor PID is 3901142. The
actual best_v9b source hash matches the explicit lead freeze. I have now
declared best-v9b-counter-timing-001 and best-v9b-counter-model-free-001:
all 26 exact-model and all 20 model-free development conditions are
transferred unchanged to bots.best:decide. Their parameters come from
manifests declared before B began. This tests the actual deliverable,
with complete-trajectory equivalence checks against the development twin.
No selection or parameter revision uses the new B outcomes.

Report correction for the lead: economy notes entry 12 corrects the
scripted-start v17 count from 107W-0D-1L to 103W-4D-1L. The four
simultaneous destructions are draws. The current best.py docstring still
quotes 107 wins; this is documentation only and should be corrected after
the active frozen-candidate checks, with the next explicit freeze.

## 2026-10-31T09:39:11.979805+00:00: Pool B games complete; independent audit and actual-entry counters running

All 60 prescribed B games completed at 09:38:11Z with no recorded errors,
rejections, source drift or timeout: 20 standard wins and 20 wins in each
continuation stress set. Full source/accounting and original-engine replay
audits are now starting; these are provisional game counts until audited.
The 46 predeclared targeted games against the actual best.py entry point
follow on two cores. Please keep best_v9b and its imports frozen until
those checks finish, or announce any necessary replacement in advance.
Pool C remains unused. The first attempted audit supervisor launch exited
before producing output; no audit or game was counted from that launch.
The replacement uses an explicitly detached process and a new log.

## 2026-10-31T09:43:43.466586+00:00: Pool B independently confirmed; targeted-run bookkeeping repair

Claim: frozen best_v9b wins all 60 predeclared pool-B conditions. Method:
run each condition in a fresh process, verify the frozen source closure,
audit every action and final outcome against the original engine, and
compare both assignments. Result: 20W-0D-0L from standard starts,
20W-0D-0L after the factory prefix, and 20W-0D-0L after the asymmetric
splash prefix. All 30 paired complete trajectories match. No errors,
rejected actions, source drift, failed attempts or unresolved conditions.

Verdict: CONFIRMED under these exact conditions. These are 30 deterministic
paired conditions, not 60 independent samples; the two prefix groups
replace the opening and skip its underlying policy call. The overlap audit
checked 85 validation campaigns and 218 team result-stream snapshots. All
62 reported exact-parameter overlaps concern retired pool A; none concern B.
Shared policy families and implementations remain a limitation.

The first campaign start was 09:34:52.829648Z; the last selected match
completed at 09:38:10.586316Z, elapsed 197.756668 seconds. Selected match
wall times sum to 107.261448 seconds; this is not elapsed experiment time.
The largest candidate decision took 4.972 seconds in the asymmetric prefix
group. All 60 replay receipts were consolidated at 09:40:20.767510Z.
Evidence: runs/validation/final-best-v9b-poolB-summary-001.md and its
strict, replay and separation JSON inputs. Pool C remains UNUSED.

The separate 26-condition actual-entry timing campaign used the wrong
runner: the generic runner omitted the public model's dynamically named
source modules from its freeze and did not collect forecast traces. Its
source check correctly rejected the completed attempts. I stopped that
campaign at 09:43:08Z, retain all evidence, and will rerun all 26 with
explicitly declared model roots and forecast diagnostics. This is harness
bookkeeping, not a bot loss. No policy or parameter is changed. The
20-condition model-free actual-entry campaign is unaffected.

## 2026-10-31T09:45:03.096297+00:00: Model-free transfer complete and current-model prefix protocol

Claim: the Lead17 development twin still loses to simple counters that do
not model its private policy. Method: all 20 predeclared standard conditions,
both assignments, fresh processes, strict source checks and complete
original-engine replay. Result: counter outcomes 8W-8D-4L, with all ten
seat pairs identical. The half-budget tier3-round3 counter wins 800:774;
corner gun plus one tier1, two tier1, or one tier2 wins 800:795, 800:790,
and 800:788 respectively. The empty corner guard draws 800:800. The
two-tier1-plus-tier2 guard loses in round 12, and direct econ17 loses
785:795 in round 50. Replay time was 15.276144 seconds.
Verdict: CONFIRMED on these conditions; actual best.py transfer is running.
Evidence: runs/validation/lead-seventeen-model-free-summary-001.md.

I accept the lead's 09:41Z model warning. The V4 free-prefix result was
only claimed for V4. The new best-v9b-free-scenarios-001 declaration keeps
all twelve previous counter schedules and four development openings,
both assignments, and changes both the target and the private model to
best_v9b. The target wrapper calls best.decide; the model owns an
independent best.make() instance. Both are called during every prescribed
opening round. The existing prefixed-forecast proof applies conditional
on determinism and equal initial private state; the component check will
compare every forecast, call count and action with the lead's TimedBot
adapter before any full games. This is development, not another holdout.

## 2026-10-31T09:51:41.491799+00:00: Corner-guard continuation experiment declared

Claim under test: economy19 can repair the late losses of a corner gun opening without changing that opening. Method: fix gun1 at (9,1), use one tier1 or one tier2, and compare inherited attack holds of None and 11. The revised continuation is frozen economy19 with free_fallback="zero", doom="next", fac_cap=400 and sat_reach=true. Twenty-four declared games face frozen best_v9b, economy17 and fortress26, both assignments; sixteen separate economy17 controls face best_v9b and fortress26. Existing economy17-opponent controls are reused from guard-hold-coordinate-001. The component check compares eight legacy-control prefixes and requires unchanged first-round actions for economy19.

Verdict: OPEN, no new matches launched yet. This is a whole-continuation intervention, not proof that a particular heuristic causes any improvement. Fortress26 retains a wall-clock bound in gun planning, so repeated histories are checked rather than assumed identical. The frozen best module avoids extending the live entry-point freeze. Manifests: experiments/validation/guard-continuation-econ19-001.json and guard-continuation-econ17-001.json.

## 2026-10-31T09:53:33.039449+00:00: Actual best_v9b model-free failures confirmed; independent label audit

Claim: the model-free failures of the Lead17 development twin also occur through the actual bots.best:decide entry point. Method: all 20 predeclared standard conditions, both assignments, fresh processes, strict source/legality audit and complete original-engine replay. Result: counter outcomes 8W-8D-4L. Every one of the 20 complete trajectories equals its matched development-twin trajectory, and all ten assignment pairs agree. Replay took 28.717432 seconds. The half-budget tier3-round3 counter wins 800:774; corner gun plus one tier1, two tier1, or one tier2 wins 800:795, 800:790, or 800:788. These are simple counters, independent of a private opponent model.

Verdict: CONFIRMED for these conditions. Evidence: runs/validation/best-v9b-counter-model-free-summary-001.md and best-v9b-model-free-equivalence-001.json. The 26 exact-model conditions and 24 current-model prefix conditions remain in progress or queued; the live source must stay frozen until those finish.

A separate reporting audit independently confirms the teams' corrections. Defense x53 has 26 valid reported rows, 22W-0D-4L; x57 and x71 each have 26 valid rows, 24W-2D-0L. Each stream also has two harness-error rows, which must not count as games. Economy scen18 and scen21b each have 108 valid reported rows, 103W-4D-1L. Their four unequal-HP simultaneous destructions were incorrectly classed as wins by a margin-sign rule. All eight affected historical logs replay exactly on the original engine; the historical stream and relevant engine hashes were checked.

Verdict: CONFIRMED as a historical reporting correction, not a fresh frozen-policy evaluation. Evidence: runs/validation/team-outcome-label-audit-001.json. Only the eight label-disagreement logs were replayed in that audit.

## 2026-10-31T09:55:46.579861+00:00: Stateful catalogue experiment declared

Claim under test: an unknown fixed member of a small public-policy catalogue can be identified from public purchases without sacrificing the useful timing counter against best_v9b. The catalogue contains frozen best_v9b, economy17 and economy19, with exact declared parameters. Each clone starts at round 1 and is advanced once per active round; mismatched purchase signatures permanently eliminate it. If all are eliminated, the policy uses a visible-roster defense and visible-map attack heuristic.

Method: three counter settings against all three members and two outside-catalogue opponents, both assignments, 30 declared games. One setting restricts the catalogue to best_v9b as a model-specific control. Component checks and an independent trace audit will distinguish true-model retention, forecast accuracy, eventual identification and game outcomes. The informal proof was written before implementation in experiments/validation/analysis/stateful_catalogue/PROOF.md.

Verdict: OPEN. The catalogue guarantee assumes deterministic outputs and the stated initial private state. It does not imply eventual identification or a winning response. Fortress26 is an outside-catalogue stress opponent because its gun planner retains a clock cutoff. No game has been launched yet.

## 2026-10-31T10:02:18.762807+00:00: Guard-coordinate study and actual-prefix component completed

Claim: a corner guard is uniformly preferable to a central guard. Method: the 48 declared hold/coordinate conditions against V4, economy17 and fortress24, both assignments, with strict source checks and complete original-engine replay. Result: 30W-2D-16L for the guard policies, all 24 assignment pairs identical. One tier1 at x=3 without the inherited hold beats economy17 783:768, whereas x=9 loses -917:768 in round 35 and x=10 loses -922:768 in round 33. These same corner openings beat V4 and fortress24. Every tested tier2 opening loses to economy17.

Verdict: REFUTED for uniform preference; these openings have opponent-dependent strengths. Replay took 71.790054 seconds. Evidence: runs/validation/guard-hold-coordinate-summary-001.md. The declared economy19 continuation comparison is running; its first-round component passed all eight legacy-control prefixes in 14.289561 seconds.

Claim: the current-bot prefix wrapper preserves a synchronized independent private model. Result: check_prefixed_best_v9b passed all eight prescribed openings through eight rounds in 20.234004 seconds, including actual target actions, private-model actions, legal output and call counts. Verdict: CONFIRMED on those component cases. The 24 full games are running; no full-game result is claimed yet. Their queued audit permits a separately declared 450-second retry only for recorded 300-second timeouts, selecting both assignments and preserving failures.

The new stateful-catalogue proof is conditional on determinism and known initial private states. Lead and economy lanes: please review its induction and the proposed public-signature elimination rule when convenient; no universal identification or winning guarantee is claimed. The catalogue uses the frozen economy17/economy19 defaults with plan_time=1e6, while fortress26 is outside the catalogue because its default gun pass has a three-second cutoff.

## 2026-10-31T10:04:14.329024+00:00: A counter cycle involving the actual frozen best bot

Claim: among frozen best_v9b, economy17 and the default corner-tier1 guard, one policy beats both alternatives. Method: bind the exact six existing game records to their strict and original-engine replay receipts, check matching policy specifications and current source hashes, and compare assignment histories. Result, winner first: guard beats best_v9b 800:795; best_v9b beats economy17 795:785; economy17 beats guard 795:753. All six end in round 50 and each assignment pair has identical normalized histories.

Verdict: REFUTED; the three policies form a directed counter cycle. The guard here is exactly GuardGeometry(roster=["tier1"]) at its default (10,1), with foreign_attack_from=11. It is not the new (9,1) continuation experiment. Evidence: runs/validation/best-v9b-counter-cycle-index-001.json, checked in 0.481025 seconds. This is an index of three already tested paired conditions, not six new samples. No self-play values or mixture equilibrium are inferred. The standalone argument and dependencies are in experiments/validation/analysis/current_best_cycle/PROOF.md.

## 2026-10-31T10:05:30.214959+00:00: Immediate correction of an owned-module interface regression

I found and corrected an implementation error: the new corner-continuation experiment overwrote bots/counters/guard_continuation.py, which already supported the older relevant_turret_guard, defense_strength_guard and exposure_guard interfaces. The incompatible module existed from the 09:51Z implementation until this restoration. I stopped the new economy19 continuation campaign and its supervisor, preserved all attempts, copied the new class to bots/counters/corner_continuation.py, and restored the original guard_continuation.py byte for byte from its verified first-shift source archive.

Lead and other lanes: any run launched in that interval that instantiated one of those three older guards may have a TypeError for the continuation keyword or may have captured the wrong source hash. Exclude affected error rows; do not interpret them as opponent losses. Please refresh the restored source snapshot before rerunning affected conditions. I am auditing the scope and preparing a clean, separately named rerun of the new continuation experiment. Existing guarded-timing and GuardGeometry modules are different and have not been edited. Verdict: CONFIRMED interface regression and restoration; scope audit remains OPEN. Evidence: runs/validation/guard-interface-restoration-001.json.

## 2026-10-31T10:08:29.268149+00:00: Guard interface regression scope and restored component checks

Claim: the temporary module replacement affected only the newly declared experiment. Method: snapshot all 232 result streams under runs/lead, runs/defense and runs/economy, bind their complete newline-terminated prefixes by byte count and SHA256, and inspect source attestations and errors. Result: REFUTED. Among 17,529 rows, four have the incompatible guard hash and twelve have the exact unexpected-continuation-keyword error. All sixteen are in defense streams. No affected row appeared in the sampled lead or economy prefixes.

The affected zero-based row indices are x75_v26_foreign 18 and 23 (source drift), 19 through 22 (constructor errors); x78_surplus_misc 4, 5, 6, 8, 9 and 10 (constructor errors); x80_v27_counters 0 and 1 (constructor errors), 8 and 9 (the wrong default policy ran without a source-drift flag). In particular, x80 rows 8 and 9 must not be interpreted as results against the original GuardContinuation. They used the new corner policy under the wrong module name. Please exclude or relabel these recorded attempts and rerun the intended conditions after restoration.

Restoration checks passed twelve original-engine prefixes, six older constructor settings in both assignments through round three, with legal actions and unchanged input observations. The restored source hash matches the first-shift archive exactly. Evidence: runs/validation/guard-regression-scope-001.json and guard-interface-restoration-001.json. The scope audit covers saved stream prefixes, not later appends or unsaved failures. The team harness uses fresh spawned workers with one task each, so later tasks should import the restored source. This does not excuse counting earlier affected rows.

The old guard-continuation-econ19-001 campaign and its unstarted economy17 control are retired. Replacement manifests corner-continuation-econ19-001 and corner-continuation-econ17-001 use a separate corner_continuation module; no old attempt will be counted in their strength results.

## 2026-10-31T10:11:41.369508+00:00: The reported economy17 versus fortress25 sign reversal is a perspective error

Claim in economy entry 13: economy17 lost the standard-start games against fortress25 in defense x73 but won them in economy w1new, demonstrating load-dependent results. Method: independently inspect x73_v25_econ17 rows 2 and 3 and w1new rows 20 and 22, fix the perspective to economy17, verify exact specifications, closure versions and current source hashes, then compare complete canonical replay records. Result: all four games are economy17 wins, 750:735 after 50 rounds. Both same-seat pairs have identical complete trajectories. The negative margin in the defense report is from fortress25's perspective.

Verdict: REFUTED for this claimed sign reversal. Evidence: runs/validation/e17-f25-repeat-comparison-001.json, checked in 0.359255 seconds. This is a saved-history comparison, not a new match. Original-engine replays of these four particular logs are queued separately. The planner's clock cutoff remains a real code limitation, and this comparison does not prove universal determinism. It does show that these four games provide no evidence of load-dependent play. Economy lane: please correct that paragraph rather than treating the opposite candidate perspectives as different results.

The 60 declared hold/coordinate comparisons are also complete (runs/validation/guard-hold-coordinate-comparisons-001.json). None has an identical complete trajectory. For the central one-tier1 guard, removing the inherited attack hold changes economy17 from a 783:795 loss to a 783:768 win; it changes fortress24 from a 770:795 loss to a 775:735 win. The coordinate intervention reverses the economy17 result: moving that no-hold guard from x=3 to x=9 loses -917:768 in round 35. Thus neither the hold nor the corner placement is uniformly beneficial. These are matched full-policy interventions with feedback, not isolated per-round causal estimates.

## 2026-10-31T10:12:45.596823+00:00: Actual best timing audit complete; catalogue component passed

Claim: the 26 disclosed timing conditions against the Lead17 development twin transfer to the actual frozen best_v9b entry point. Method: all 26 conditions in fresh processes, both assignments, strict source and action checks, exact forecast comparison on every round and full original-engine replay. Result: counter outcomes 16W-8D-2L, 1,300 exact primary forecasts, thirteen identical assignment pairs, and all 26 complete histories identical to the development twin. The two earlier source-coverage failures remain excluded and separately replayed; they add no samples. Verdict: CONFIRMED for these conditions. Evidence: runs/validation/best-v9b-counter-timing-summary-001.md and best-v9b-timing-equivalence-001.json.

The standard timing failures therefore remain real: tier3 in round 3 wins 800:774; tier4 in round 5 wins 800:740; tier4 in round 7 wins 800:680. The free-prefix campaign is still running and does not yet have a full-game conclusion.

The stateful catalogue component passed 64 primary prefix rounds and sixteen singleton-control rounds in 17.976952 seconds. Sixteen deliberately corrupted signature or call-count traces were rejected. The true member was always retained and its actions exact. Against best_v9b the final active set was its singleton; against economy17 and economy19 both economy members remained after round 8, illustrating that retention is not identification. Idle caused the empty-catalogue fallback as intended. Verdict: CONFIRMED component behavior; full-game strength OPEN. Thirty games are now running. Evidence is registered beside the standalone proof.

## 2026-10-31T10:20:04.935340+00:00: Adaptive catalogue attack experiment declared; uniform prefix timeout revision

Claim under test: a bounded current-round attack search can improve the stateful catalogue controller over its identical no-attack version. Thirty development games are declared against the three catalogue members and the two outside opponents, both assignments, using weights 4 and 8. Each decision advances the inherited clones once, keeps their defensive construction, evaluates an affordable deterministic set of pure and ordered two-tier purchases, and reinvests the remainder. Rational scoring and a conditional safe-lethal priority are used. The argument was written first in analysis/catalogue_attack_selection/PROOF.md. Verdict: OPEN; component and original-combat checks must pass before any game starts. The experiment waits for the current catalogue campaign on core29.

Lead and economy lanes: review of the retained-catalogue induction and current-round attack argument is welcome. The exact forecast guarantee requires true fixed catalogue membership; visible-state fallback and future-value scoring are explicitly heuristic. No opponent name or policy identity is supplied to the bot.

The actual-best known-prefix suite hit three consecutive 300-second wall-time limits, with partial replays already in late rounds. I stopped its supervisor and old audit queue while letting the last bounded runner finish. A separately declared full retry will preserve all twelve schedules and both assignments with a uniform 450-second allowance. No condition is dropped or selected by its outcome, and all original attempts remain visible. Evidence: runs/validation/best-prefix-budget-revision-001.json. The live best_v9b source must remain frozen for this suite; the other two active counter campaigns use its archived copy. The original prefix manifest contains inherited V4 target-source descriptive fields; actual candidate specifications, the explicit best hash, source closure and executed entry point are best_v9b. The retry declaration corrects those descriptive fields without changing any case.

## 2026-10-31T10:23:25.704681+00:00: Live-entry timing notice and fortress27 clock-scope correction

Lead: the actual best_v9b prefix suite now runs all 24 original conditions at a uniform 450-second limit. All four 300-second attempts timed out and remain preserved; twenty were unstarted. The new declaration is best-v9b-free-scenarios-fullretry450-001.json, made at 10:20:42 UTC. Based on the partial late-round progress, this serial suite may extend beyond 12:30 UTC. Please retain the current live best.py and imported sources until I post completion or an explicit retirement; the frozen-copy campaigns do not need that delay. I will update the estimate when the first longer-limit games finish. This is development validation, separate from reserved pool C.

Claim: fortress27 has removed every clock-dependent planning cutoff. Method: read its frozen plan.py and fortress.py. Result: plan.py still defines TIME_BUDGET = 3.0, computes a deadline in plan_defense, checks it before the first two gun plans and inside _gun_pass; fortress.py invokes that planner without an overriding time budget. Its foreign-layout re-planner uses a fixed iteration count, which removes that particular clock dependency. Verdict: REFUTED for the broader all-cutoffs claim. This is a source-scope finding, not an observed same-condition divergence. The reported speed improvement can make the remaining cutoff inactive in tested games, but does not remove it from the policy. Defense lane: please qualify the final sentence of the 10:18 reproduction note accordingly.

A separate correction remains relevant: the x73 versus w1new economy17/fortress25 standard games agree exactly after fixing candidate perspective. They are not evidence of clock-induced divergence. Four original-engine replays of those already-compared logs are queued on core28 after the continuation experiments.

## 2026-10-31T10:25:33.311529+00:00: Scope of the adaptive policy's final-round score

Claim: the adaptive catalogue purchase ranking certifies an optimal terminal result within its finite purchase set. Method: inspect the declared source and derive an abstract two-member damage-table counterexample. Result: the final round uses minimum marginal outgoing gain, whereas earlier rounds use weight times gain minus cost. It still weakly improves outgoing damage over the empty purchase under the conditional exact-forecast assumptions, but can rank a loss above an available simultaneous-destruction draw when retained members have different baseline damage. Verdict: REFUTED as a general inference from the ranking rule; reachability of the illustrative table in this game is OPEN and is not claimed. The complete argument is analysis/catalogue_terminal_score/PROOF.md. Existing declared source and experiment inputs remain unchanged.

## 2026-10-31T10:28:16.801891+00:00: One-way economy20 continuation declared

Hypothesis: the catalogue controller's visible-only fallback can be improved by switching permanently to a fresh frozen economy20 foreign-map policy when all public models are rejected. The first eight completed, not yet fully audited, ensemble_t3r3 games win against the three catalogue members and lose both fortress26 assignments, 200:774. That outside-catalogue failure motivates a separate experiment.

Method: the new catalogue_continuation module keeps the exact parent branch while any member survives, then invokes economy20 once per reached round from a fresh state. Its fourteen declared development conditions include ten matched existing conditions and four descriptive fortress27 conditions (default and response_memory, both seats). The retained-member trajectory argument was written before implementation in analysis/catalogue_continuation/PROOF.md. Independent parent and fresh-continuation prefix comparisons must pass before the games. Verdict: OPEN. The new module leaves the active catalogue and adaptive-attack experiments unchanged.

## 2026-10-31T10:33:20.668423+00:00: Guarded public-forecast counter prepared

Hypothesis: the planned early catch-up attack can be answered by a cheap prescribed guard followed by a synchronized public-policy defensive model, preserving an opening HP edge. The new guarded_forecast module advances its independent opponent clone in round 1 while returning the unchanged GuardGeometry opening, then uses FreeForecast defense. It does not alter either existing policy. The clone argument and its affordability limitation were written first in analysis/guarded_forecast/PROOF.md.

Method: eight prefixes against frozen best_v9b will compare the prescribed opening, actual opponent actions, original incoming combat, input immutability and legal actions. Full-game development comparisons against the next frozen best can follow those checks. Verdict: OPEN. Only syntax and source review have completed; no new game or successful defense is claimed here.

## 2026-10-31T10:34:43.842413+00:00: Corner economy19 continuation, full audit complete

Claim: replacing the corner guard continuation with the declared economy19 preset removes its vulnerability to economy17. Method: four presets at gun coordinate (9,1), roster tier1 or tier2, attack hold null or 11, each against frozen best_v9b, economy17 and fortress26 in both assignments. Run with `.venv/bin/python -B -m bot_research.experiments.validation.run_long_development --manifest bot_research/experiments/validation/corner-continuation-econ19-001.json --output-dir bot_research/runs/validation/corner-continuation-econ19-001 --max-seconds 480 --match-timeout 300`, then bounded resumes and the strict plus original-engine replay audits. The standard environment and core-28 affinity were used.

Result: 12 wins and 12 losses in 24 conditions, all legal, no bot errors or source drift. All twelve assignment pairs have identical complete normalized trajectories. Each preset beats best_v9b; each loses to economy17. Against fortress26, no hold wins and hold 11 loses, for either opening roster. The tier1/no-hold loss to economy17 ends in round 34 at -357:768; tier2/hold11 ends in round 36 at -3012:788. Verdict: REFUTED for removing the economy17 vulnerability. The paired economy17-continuation controls are still running, so no general improvement or one-feature ablation is claimed.

Evidence: runs/validation/corner-continuation-econ19-summary-001.md and its bound strict/replay receipts. Full replay took 17.535004 seconds. Fortress26 retains its gun-planner clock cutoff; these observed paired trajectories agree but do not establish universal load independence.

## 2026-10-31T10:38:57.824543+00:00 Interim-report corrections and completed catalogue experiment

Claim: the current report's repeated econ17 107/108 statement and its blanket deterministic-bot statement are supported by the saved evidence. Method: read-only review of REPORT.md, pinned in runs/validation/interim-report-claim-audit-001.json, against the earlier winner-label audit, source cutoff audit and paired E17/F25 histories. Result: the audited 108-condition econ17 suite is **103W 4D 1L**, not 107 wins; four mutual-destruction draws have nonzero HP differences. The engine is deterministic, but fortress v27 still has the 3-second gun-planner cutoff even though the foreign-layout planner uses fixed iterations. The cited four E17/F25 standard-start records are all E17 wins 750:735, with equal same-seat histories; they do not demonstrate load-induced divergence. Verdict: **REFUTED** as written. Lead: please correct the interim report's summary/method determinism language and sections 5.8 and 5.10 count. W2: the opposite-sign paragraph in entry 13 remains incorrect. I did not edit report-owned files.

Claim: a fixed three-policy catalogue can improve a forecast counter without access to an opponent identifier. Method: stateful-catalogue-001 declared 30 standard-start games, three counter settings against frozen best_v9b, econ17, econ19, fortress26 and guard_geometry [tier1], both assignments. The counter retains every public-policy clone whose previous construction, roster and factory signature matches the next public observation. In-catalogue models are persistent and advanced once per decision. The singleton-best control differs only in catalogue membership.

Result: all 30 completed legally, with no bot errors or source drift. All 15 assignment pairs have identical canonical histories. The unchanged engine replayed every saved action trace successfully in 31.912566 seconds. Summed match wall time was 1417.159492 seconds, maximum 203.499876; these are computation timings, not independent samples. Counter outcomes were 14W 0D 16L:

| Counter | Opponent | Each assignment, counter HP first |
| --- | --- | --- |
| ensemble_t3r3 | best_v9b | W 800:774 |
| ensemble_t3r3 | economy17 | W 788:774 |
| ensemble_t3r3 | economy19 | W 788:774 |
| ensemble_t3r3 | outside_fortress26 | L 200:774 |
| ensemble_t3r3 | outside_guard_t1 | L 172:774 |
| singleton_best_t3r3 | best_v9b | W 800:774 |
| singleton_best_t3r3 | economy17 | L 104:774 |
| singleton_best_t3r3 | economy19 | L 104:774 |
| singleton_best_t3r3 | outside_fortress26 | L 200:774 |
| singleton_best_t3r3 | outside_guard_t1 | L 172:774 |
| ensemble_t4r5 | best_v9b | W 800:740 |
| ensemble_t4r5 | economy17 | W 800:740 |
| ensemble_t4r5 | economy19 | W 800:740 |
| ensemble_t4r5 | outside_fortress26 | L 82:740 |
| ensemble_t4r5 | outside_guard_t1 | L 95:740 |

The paired membership intervention changes all four econ17/econ19 games from 104:774 losses to 788:774 wins. The other six histories are unchanged. Both three-model timing settings beat all three catalogue members but lose to both outside opponents. There were 700 audited exact true-model predictions. On the three-model runs, best_v9b is isolated at round 2; econ17/econ19 may remain observationally equivalent longer, so an early policy name is not required for conservative planning. The full trace audit records the exact isolation/fallback rounds. Verdict: **CONFIRMED** for the stated membership intervention and **REFUTED** for any claim of general strength against these outside opponents. Catalogue continuation and adaptive purchase experiments are queued/running to address the observed failure, with separately declared conditions.

Evidence: runs/validation/stateful-catalogue-{strict,traces,replay,summary,comparisons}-001.json. Source/conditional-proof scope: experiments/validation/analysis/stateful_catalogue/PROOF.md. These development opponents are not held-out pool C.

## 2026-10-31T10:41:14.012253+00:00 Guarded-forecast full-game declaration

Claim: exact public forecasting after a cheap corner guard can preserve the opening lead against frozen best_v9b. Method: guarded-forecast-best9b-001 declares six opening rosters (empty, tier1, two tier1, tier2, four tier1, two tier1 plus tier2), gun1 at (10,1), remaining round-1 gold spent on factories, and zero later offensive share. Both assignments give 12 standard-start development games. Target and persistent model are the frozen best_v9b make entry. The separate component check must pass first. Full audits will check forecasts and source integrity, recompute incoming damage with original combat, and replay every action. Result: declared and queued after the existing core-28 chain; no games run yet. Verdict: **OPEN**. Files: experiments/validation/guarded-forecast-best9b-001.json and audit_guarded_survival.py.

## 2026-10-31T10:42:37.491183+00:00 A 450-second prefix timeout remains unresolved

Claim: increasing the known-prefix run allowance to 450 seconds completes every original condition. Method: all 24 original conditions remain in the uniform retry. Result: case0003 (mirror:1:2, tier4 round7, counter seat1) reached round49 and timed out at 450 seconds; its complete recorded prefix equals the opposite assignment's prefix through round49, whose full game ended 795:795 at round50. The absent round50 is not inferred. The retry continues the other declared conditions and this failure remains preserved. Verdict: **REFUTED** for universal completion under that allowance; the failed game's outcome is **OPEN**. Evidence: runs/validation/prefix450-timeout-prefix-comparison-001.json. This is development evidence, separate from completed pool B and unused pool C.

## 2026-10-31T10:46:50.244003+00:00 Evidence reading order for report integration

The compact index at experiments/validation/EVIDENCE_INDEX.md links completed reserved validation, actual-entry counters, the catalogue intervention, cycle evidence, and the reporting corrections. Every relative link was checked. Pending campaigns remain explicitly pending. This is navigation for the report owner, not an additional experiment. Verdict: **CONFIRMED** for the linked-file checks; claim scopes remain those of the underlying evidence.

## 2026-10-31T10:47:20.912639+00:00 Corner continuation controls and outcome comparison complete

Claim: replacing the corner guard's econ17 continuation with the declared econ19 preset improves the recorded game outcomes. Method: finish sixteen new econ17 controls against best_v9b and fortress26, reuse eight already-audited econ17-opponent controls, and match all twenty-four conditions by opening, inherited hold parameter, opponent, assignment and initial state. Result: the sixteen new controls are 12W 0D 4L, all legal, with eight identical assignment pairs and every action replayed through the unchanged engine (14.279661 seconds). All twenty-four paired outcomes are unchanged. No complete paired trajectory is identical: first action differences occur in rounds 7 through 14. Twenty final HP pairs are unchanged; four differ, all still losses to econ17. For tier1/no hold, own final HP changes -917 to -357 and defeat moves from round35 to round34; for tier2/hold11, own final HP changes -1192 to -3012. Thus raw negative-HP margins should not be interpreted as a continuous strength measure after destruction. Verdict: **REFUTED** for improved outcomes on this grid. The experiment compares whole continuations; it does not isolate one econ19 feature.

Evidence: runs/validation/corner-continuation-econ17-summary-001.md, corner-continuation-comparisons-001.json, and corner-continuation-outcome-comparison-001.json.

Review note for the defense lane's 10:45 entry: v27 and v28 have the same six-win/four-loss aggregate against econ17, but the listed asym:3:2 seat1 changes from loss to win and asym:23:2 seat1 changes from win to loss. They therefore do not differ only by the 35 HP standard-start margin. The per-condition table should remain the primary statement. Also, v28 imports the same gun planner with the three-second cutoff; the earlier source-level determinism qualification applies. This is a read-only comparison of the lane's reported values, not an independent new replay claim.

## 2026-10-31T10:51:55.574390+00:00 A narrower terminal-ranking guarantee

Claim: the adaptive catalogue's final-round ranking chooses the best terminal result within its evaluated purchase set when exactly one retained model remains and that model is true and synchronized. Method: prove that, with incoming damage and construction fixed, the engine's terminal result is nondecreasing in outgoing damage; then inspect the safe-lethal priority and the singleton gain score. Result: a complete conditional informal proof is in analysis/catalogue_singleton_terminal/PROOF.md. Verdict: **CONFIRMED** under its exact hypotheses. This does not contradict the earlier two-model counterexample, prove that an observed singleton is true, or certify the search over all legal actions. No new implementation, simulation or formal proof-assistant check is claimed.

## 2026-10-31T10:53:21.493220+00:00 Adaptive continuation prepared

Hypothesis: combining the adaptive catalogue attack with the fresh economy20 fallback can retain the wins against catalogue members while reducing outside-opponent losses. The completed but not yet fully audited weight4 block is six wins against the three members and four losses against the two outsiders. The new adaptive_continuation module composes the existing policies without modifying them. It explicitly labels the discarded proposal on the first rejection round and records actual continuation purchases separately. A standalone conditional composition proof precedes the implementation; independent parent/continuation and original-combat component checks are prepared. Verdict: **OPEN**. Only syntax checks have run; no new full-game result is claimed.

## 2026-10-31T10:54:22.953876+00:00 Adaptive continuation experiment declared

Method: adaptive-continuation-001 fixes two candidates (search disabled, or weight4), the original five targets plus fortress27 default and response-memory, and both assignments, for 28 standard-start games. Twenty parent/continuation comparisons are declared in advance. Twenty component prefixes must first match independently run parent and fresh continuation policies, with original-combat checks on executed adaptive attacks. The queue waits for the current adaptive experiment to finish and retains all existing results. Verdict: **OPEN** until these checks and games run.

## 2026-10-31T10:57:53.804746+00:00 Adaptive catalogue attacks, complete audit

Claim: bounded catalogue-based purchase search improves the no-attack controller against the three declared member policies. Method: thirty standard-start conditions compare search disabled, weight4 and weight8, each against best_v9b, economy17, economy19, fortress26 and the tier1 corner guard, with both assignments. The same controller and defensive rule are used. Result: the disabled control is 0W 6D 4L; each attack weight is 6W 0D 4L. All thirty games are legal, with no bot errors or source drift; all fifteen assignment pairs have identical complete normalized histories. Against best_v9b each weight wins 800:765, and against each economy member it wins 800:768. The control draws these six conditions 800:800. Verdict: **CONFIRMED** for these twelve paired draw-to-win changes.

The outsider losses remain: the control loses to fortress26 68:800 and the corner guard 33:800 at round50. Weight4 instead loses -185:780 and -59:775 at round18; weight8 loses -25:420 at round17 to fortress26 and -59:775 at round18 to the guard. Eight of ten weight4/weight8 matched histories are identical; only fortress26 differs. Thus doubling the weight does not improve any recorded outcome, and the search does not solve outside-catalogue weakness. Verdict: **REFUTED** for that broader claim.

There are 900 checked true-model predictions and 742 enabled attack rounds, covering 918 original-combat target evaluations. Full saved-action replay took 15.351948 seconds; the attack audit took 14.249121 seconds. Summed match wall time is 954.959549 seconds, maximum 108.923482. The attack audit checks the selected package, baseline and incoming damage, pool membership and score arithmetic; it does not rerank every package with the original engine. Evidence: runs/validation/adaptive-catalogue-summary-001.md and adaptive-catalogue-outcome-comparison-001.json.

The next continuation experiment stopped before any full game because its component checker reused the name `parameters` for opponent parameters. The original checker, declaration and failure remain preserved. A separately named v2 checker corrects that name; adaptive-continuation-002 redeclares the same 28 conditions and unchanged policy. No failed game is removed because none started. The failure log only had absolute project prefixes removed from traceback filenames, with before/after hashes in adaptive-continuation-checker-correction-001.json.


## 2026-10-31T11:01:57.768381+00:00: catalogue rejection plus economy20 continuation completed

Claim: replacing visible-roster fallback with a fresh economy20 controller after the public catalogue is exhausted will preserve known-member play and rescue the outside-catalogue failures.

Method: `catalogue-continuation-001` runs the unique `catalogue_continuation` module against seven fixed opponents from the standard start, both player assignments. Fourteen conditions were declared before execution. All cases passed strict provenance/legality checks, exact catalogue trace checks, fresh economy20 action recomputation after rejection, and full original-engine replay (9.276475 seconds for replay). The continuation action audit took 98.389123 seconds. Ten already-declared comparisons match the original three-model, tier3-round3 parent against the same five earlier opponents.

Result: 6 wins, 0 draws, 8 losses; all seven assignment pairs have identical normalized trajectories. Counter-first final HP, identical in both seats and all at round 50: best_v9b 800:774; economy17/economy19 788:774; fortress26/fortress27 762:800; guard_t1 763:800; fortress27 with response_memory 788:800. The six known-member trajectories are identical after normalization to the parent. The four old outside-catalogue cases change actions first in round 2, but remain losses: fortress26 changes 200:774 to 762:800, and guard_t1 172:774 to 763:800. Against all four outside opponents the catalogue is exhausted in round 2; every later action agrees with a fresh economy20 continuation. Total measured match wall time is 631.562957 seconds.

Verdict: CONFIRMED for the six tested known-member trajectories remaining unchanged; REFUTED for rescuing these outside-catalogue losses. Smaller HP deficits are descriptive and do not convert a loss into a win. The counter loses by 12 HP against response-memory fortress rather than 38 against its default parent; this remains one declared condition per seat. Evidence: `runs/validation/catalogue-continuation-outcome-comparison-001.json` and its five pinned receipts. The adaptive-attack continuation is a separate ongoing experiment.


## 2026-10-31T11:02:39.958129+00:00: provenance-auditor compatibility correction

Claim: archived manifest promises can be compared across all saved validation campaigns. Method: the first metadata-only auditor stopped on four old declarations that store `snapshot_sha256` as one string rather than a mapping. Result: the original checker and failed log are retained; `audit_declared_sources_v2.py` associates a scalar snapshot hash with the unique snapshot module named by its policy specifications, independently of hash equality, and records unsupported shapes explicitly. It is syntax checked and queued after the running core-28 checks. The guard component had already passed all eight prefixes before this separate metadata audit failed. No policy or game evidence changed. Verdict: OPEN until the corrected metadata audit completes. See `runs/validation/declared-source-checker-correction-001.json`.


## 2026-10-31T11:04:26.041609+00:00: full finite-pool ranking audit declared

Claim: the selected adaptive attacks maximize their declared rank over the entire recorded candidate pool when all damage values are recomputed with original combat. Method: `complete-attack-pool-audit-001.json` declares all ten search-enabled seat-0 cases from the completed adaptive-catalogue experiment and reached rounds 1, 2, 3, 5, 10, 12, 15, 20, 30, 40 and 50. This is post-experiment development verification. The new checker uses original combat for every pool entry and target, then independently reconstructs the rank and stable first-maximum tie rule. Pool generation remains shared; an immunity-pruned pool is audited as that pool, not as an exhaustive action set. Result: checker syntax passes, execution queued after the other core-28 checks; each case has a 540-second bound and preserves errors/timeouts. Verdict: OPEN.


## 2026-10-31T11:07:42.080986+00:00: defensive-search budget diagnosis queued

Claim: the default 15-step layout-free search can miss a legal surviving defense despite ample gold. Method: the recorded pre-round-41 state of prefix retry case0006 has HP790 and gold639450, an exact forecast of 266 tier5 entries, and a recorded1120-damage loss. A new component test holds that observation and actual opponent action list fixed, compares step budgets1/5/15/30/60, validates every construction with original actions, and recomputes original combat. It must reproduce the exact recorded default construction at15. Manifest002 adds the dynamic frozen-v15 constructor dependency omitted from the first unexecuted declaration; all test conditions are unchanged. The standalone conditional proof is `analysis/defense_step_budget/PROOF.md`. Result: implementation syntax checked, queued on core29 after adaptive continuation. Verdict: OPEN. A surviving witness will establish only current-round feasibility, not a full-game win.


## 2026-10-31T11:10:50.767917+00:00: guarded forecasting preserves each tested opening lead

Claim: a prescribed cheap guard and exact synchronized forecast can preserve a small opening advantage against frozen best_v9b. Method: all twelve declared standard-start conditions finished, six opening rosters and both player assignments, with gun1 at (10,1), factories from the remaining opening gold, and no later offensive purchases. The strict, forecast, survival and original-engine replay audits all pass.

Result: 10 wins, 2 draws, no losses; all six assignment pairs have identical normalized trajectories. Every game reaches round50, and the counter always finishes with HP800. Empty roster draws800:800; one tier1 wins800:795; two tier1 win800:790; one tier2 wins800:788; four tier1 win800:780; two tier1 plus one tier2 win800:778. Every opening margin is preserved exactly. All600 predicted opponent decisions agree. Original combat confirms zero incoming damage on every reached round, with zero false-zero residuals and zero disagreement between recorded residual and final damage. The survival audit took5.300969 seconds and full replay7.363991 seconds. Verdict: CONFIRMED for these twelve targeted development conditions. This controller knows the frozen target; no transfer or universal-defense guarantee follows.

Evidence: runs/validation/guarded-forecast-best9b-{strict,forecasts,survival,replay,summary}-001.json. The eight-prefix component check passed before the matches. Proof35 now links both component and full-game evidence.

## 2026-10-31T11:10:50.767917+00:00: fortress threshold helper boundary counterexample verified

Claim: frozen fortress28's `_kill_threshold` always returns the smallest lethal positive tier5 count within its bound. Method: compare the helper with original combat on the empty map, enumerate counts1 through8, and vary current HP and the explicit bound. Result: original combat deals140 damage per tier5 in these cases. With HP5 or140 and default bound2000, one copy is lethal but the helper returns2. HP141 correctly returns2 and HP800 correctly returns6. With bound1 at HP5 or bound6 at HP800 it returnsNone despite a feasible lethal count; bound60 at HP800 returns6. The seven checks pass in0.149598 seconds. Verdict: REFUTED for the helper's exact-minimum claim. Its assumed lower bracket starts at1 without testing lethality, and a bound below its initial test60 yields no search. No recorded full-game result is attributed to these component errors, and reachability of these empty-map low-HP states under a named bot is not established.

Evidence: runs/validation/kill-threshold-boundary-001.json; standalone exact statement and proof at experiments/validation/analysis/kill_threshold_boundary/PROOF.md. The defense lane can consider this as a bounded helper correction, not an observed tournament repair.

## 2026-10-31T11:10:50.767917+00:00: declaration provenance audit completed with explicit coverage

Claim: archived declaration hashes covered by execution freezes agree with the bytes frozen for execution. Method: the corrected auditor checks99 saved campaigns, including the four legacy scalar snapshot fields resolved by unique policy module name. Result:99 covered hash claims agree, zero disagree;61 declared input claims are not present in those policy execution freezes and remain explicitly unverified by this audit. These include auxiliary proof/checker/declaration files and inherited entries. No unsupported scalar shape remains. Runtime0.052145 seconds. Verdict: CONFIRMED for the99 covered comparisons only. This does not validate all160 declarations, descriptive metadata, or the strength of failed/retired campaigns. Evidence: runs/validation/declared-source-audit-002.json. The first failed checker/log and its correction receipt remain preserved.

## 2026-10-31T11:10:50.767917+00:00: complete finite-pool attack reranking passed

Claim: each selected adaptive attack maximizes its recorded rank over the declared finite candidate pool. Method: independently evaluate every pool entry against every retained target with original combat, reconstruct the score and safe-lethal priority, and use stable first-maximum ties. All ten declared search-enabled seat0 cases were checked at their reached rounds from the fixed schedule1,2,3,5,10,12,15,20,30,40,50. Result:94 decisions and1017 outgoing original-combat evaluations pass; total audit-process wall time16.911681 seconds. Verdict: CONFIRMED for this finite-pool ranking claim. Pool generation is shared with the policy; an immunity-pruned pool is not every legal purchase list. Both assignments were already covered by full-match replay, while this extra reranking deliberately uses one of each identical pair. Evidence: runs/validation/complete-attack-pool-audit-001/summary.json and its ten hash-pinned case artifacts.


## 2026-10-31T11:12:52.474925+00:00: guarded adaptive continuation declared

Claim: replacing the first-round package with one cheap guard and one or two tier1 purchases can improve the remaining outside-catalogue failures while preserving known-member wins. Method: the separate guarded_adaptive_continuation wrapper advances the existing parent exactly once on every actual observation; only round1's submitted actions and explanatory trace fields are replaced. A complete conditional proof precedes implementation. Twenty component prefixes must match an independent parent on actual inputs, verify exact known-member predictions, and check legality and input immutability before the 28 declared full games run. The matrix retains the same seven opponents and both assignments for both guard rosters, with 28 matched comparisons to the weight4 parent. Full strict, forecast-trace, selected-attack, fresh-continuation and original-engine replay audits follow. Result: syntax checks pass and the component-first pipeline has started on core28. Verdict: OPEN. Files: experiments/validation/guarded-adaptive-continuation-001.json and analysis/guarded_adaptive_continuation/PROOF.md. No existing policy was edited.


## 2026-10-31T11:13:57.437958+00:00: adaptive continuation completes a partial recovery outside the catalogue

Claim: replacing the visible-only fallback with fresh economy20 can rescue some outside-catalogue losses while keeping the known-member behavior. Method: all 28 declared conditions passed strict checks, catalogue traces, original-combat attack checks, fresh continuation recomputation and full original-engine replay. The disabled-search control is 0W 6D 8L; the weight4 policy is 10W 0D 4L. All 14 assignment pairs have identical complete normalized histories.

For weight4, both seats produce these counter-first final HP: best_v9b 800:765 W; economy17 and economy19 800:768 W; fortress26 and fortress27 776:720 W; corner guard 783:795 L; fortress27 with response memory -52:780 L at round12. All other games reach round50. The control draws the three members and loses to each outsider. In the 20 previously declared parent comparisons, all 12 member trajectories are identical, the two fortress26 losses become wins, and six other losses remain losses. Fortress27 and its response-memory setting were added targets, so they have no old-parent comparison in that table.

The audit checked 600 exact true-member predictions, 308 enabled attack rounds with 404 target evaluations, and 708 fresh economy20 decisions. Every outsider triggers rejection in round2. Replay took 17.725595 seconds; fresh-policy recomputation took 176.297746 seconds; total match wall time was 640.238368 seconds. Verdict: CONFIRMED for the observed fortress26 recovery and unchanged member trajectories; REFUTED for universal outside-catalogue recovery. This is development evidence, separate from reserved pool C.

Reproduction candidate: `bot_research.bots.counters.adaptive_continuation:@make?attack_weight=4`. Evidence: runs/validation/adaptive-continuation-outcome-comparison-002.json and its seven pinned receipts. The ongoing guard-opening intervention keeps this parent and the same seven targets.

## 2026-10-31T11:13:57.437958+00:00: a 15-step search limit causes one recorded defensive failure

Claim: the layout-free controller missed a legal surviving defense despite enough gold in the stated round41 position. Method: hold the exact recorded observation and opponent actions fixed; compare greedy step budgets 1, 5, 15, 30 and 60; check every action and incoming damage with the original engine. The 15-step control reproduces the recorded construction exactly.

Result: budgets 1, 5 and 15 incur 1680, 1540 and 1120 damage respectively. Budgets 30 and 60 return the same 22-turret construction costing 3010, with zero incoming damage and 636440 gold left. The actual pre-round HP is 790 and gold639450. Thus the counter can preserve all 790 HP in this round against those fixed opponent actions, instead of dying at -330. The entire check took 24.289745 seconds; the 15-step and 30-step searches took about 6.08 and 7.21 seconds. Verdict: CONFIRMED for this current-round feasibility and search-limit failure. It does not establish a full-game win, a minimum-cost defense, or that raising the cap improves every earlier decision.

Evidence: runs/validation/defense-step-budget-002.json; the explicit actions discharge the conditional proof at experiments/validation/analysis/defense_step_budget/PROOF.md, with a separate verification/WITNESS.md. Existing policies were unchanged.

## 2026-10-31T11:16:34.171924+00:00 Actual-entry prefix campaign ended; live best freeze released

Lead: the actual best_v9b prefix runner and all evidence checks have ended. You may replace bots/best.py when your candidate is ready. All other currently queued counter games in this lane use frozen modules. The 24 declared prefix conditions have 23 valid completions and 1 unresolved computational conditions. Counter outcomes on completed conditions: {'D': 1, 'L': 18, 'W': 4}. Every valid completion passed source, forecast and original-engine replay checks. This is not a claim about unresolved games, and a missing assignment is never inferred from its partner. Verdict: **CONFIRMED** for these completed traces; unresolved outcomes remain **OPEN**. Evidence: bot_research/runs/validation/best-v9b-free-scenarios-partial-summary-001.json and runs/validation/best-v9b-prefix-freeze-release-001.json.

## 2026-10-31T11:17:06.150643+00:00: full-game defensive step-budget intervention declared

Claim: the verified round41 search-budget failure can be improved in full games by raising free_steps from 15 to 30. Method: twelve declared games use three existing asym:3:2 attack schedules, both assignments and both step budgets, with the identical new wrapper around frozen best_v9b for both arms. The six 15-step controls are rerun, so no module-alias assumption is needed for the matched comparison. Four component prefixes must pass first; strict accounting, forecast checks, full original-engine replay and six declared paired comparisons follow. Result: source and syntax checks pass, component-first pipeline started. Verdict: OPEN. The current-round witness is already proved and checked; full-game improvement remains a separate hypothesis. Evidence: experiments/validation/frozen-best-prefix-steps-001.json and analysis/defense_step_budget/verification/FULL_GAME_HYPOTHESIS.md. No active source depends on the live best.py file.

## 2026-10-31T11:17:57.335003+00:00: completed prefix evidence and new counter targets for lead review

Claim: the V4-targeted free-layout schedules transfer robustly to best_v9b across these four known openings. Method: 24 predefined conditions, both assignments, original 300-second attempts retained, then a uniform 450-second retry allowance. Result: 23 valid completions produce 4W 1D 18L from the counter perspective, with 992 exact forecasts and all original-engine replays passing in 29.117800 seconds. Eleven complete assignment pairs contain five identical histories; six asymmetric pairs differ, and the lone completed half-pair is counted once. This gives 18 distinct completed histories, not 23 independent trials. The missing mirror:1:2 tier4-round7 seat1 condition remains unresolved. The only wins are mirror:1:2 tier3-round5 (795:717) and the tier4 round5-through9 drip (795:735), both seats. The completed single tier4-round7 condition draws 795:795. Every other completed condition loses. Verdict: REFUTED for broad transfer, CONFIRMED for these four wins.

Across the 23 available V4 comparisons, outcome transitions are {'W->W': 4, 'D->D': 1, 'L->L': 8, 'W->L': 10}; no complete history is identical. Both target and private model change, so this is not a one-component ablation. Evidence: runs/validation/best-prefix-outcome-comparison-001.json. The live entry freeze was released at 11:16:34Z.

Lead, for the next development challenge pool: adaptive_continuation:@make?attack_weight=4 beats frozen best_v9b 800:765 in both seats while also beating E17, E19, F26 and F27 default. Its remaining counterexamples are the corner guard and F27 response memory. GuardedForecast with frozen best_v9b as model wins 800:795 or 800:790 using a one- or two-tier1 opening followed by zero further offense. These are targeted development opponents. Do not substitute them into reserved pool C; C stays unused until your explicit new frozen candidate.

## 2026-10-31T11:20:20.663986+00:00: fixed-map append monotonicity argument for review

Claim: appending active roster entries cannot remove an arrival of any old entry on the same fixed map, even after modulo-spawn wrapping. Method: induct on original combat ticks. The larger simulation preserves every old survivor with at least its smaller-simulation HP. A gun that selects an old survivor in the larger population must also select it in the smaller population, since all higher-priority old survivors remain present; splash damage to that survivor is unchanged. Stable relative order is essential. Result: standalone informal proof written before implementation at experiments/validation/analysis/append_monotonicity/PROOF.md. It does not cover inserting before old entries, changing the map or full-game resource decisions. Verdict: OPEN pending component checks and team review; the written argument supports exact positive-count bisection with both endpoint boundaries handled. This responds to the frozen threshold helper counterexample without editing that helper.

## 2026-10-31T11:22:42.913864+00:00: append-monotonicity and bounded threshold checks pass

Claim: the written fixed-map append argument matches the bundled combat behavior on the declared fixtures, and the new positive-count search returns the exact finite-domain answer. Method: 64 paired rosters on eight maps, including four actual recorded layouts, active counts around 250 and 500, and inactive entries. The unchanged spawn_schedule and combat_tick functions check old birth ticks, surviving identities, relative order and HP at all 16000 ticks. Independent simulate_map calls confirm both damage totals. Result: every check passes in 7.687397 seconds; 15 cases strictly improve an old survivor HP at some tick and 35 strictly increase final damage. Another 64 threshold cases on four maps agree with exhaustive original combat on counts through17, including upper bounds0,1,6,17. Verdict: CONFIRMED for these finite checks. The general statement rests on the separate informal proof, not extrapolation from the examples. The helper accepts a pure monotone damage callback and changes no existing bot. Evidence: runs/validation/append-monotonicity-001.json; proof and registered checks in analysis/append_monotonicity.

## 2026-10-31T11:25:06.818758+00:00 Frozen F29 threshold boundaries checked separately

Claim: the older F28 boundary failures do not persist in frozen F29 for the declared positive bounds. Method: call F29's unmodified `_kill_threshold` on four fixed maps, four HP values (5, 140, 800, 2200), and bounds 1, 6, 17; compare every result with the exhaustive original-combat minima already archived by the append-monotonicity check. The input, reference artifact and source closure are hashed. Result: all 48 comparisons pass, elapsed 0.097391571 s. Source inspection confirms that F29 tests one copy first and clips and tests the upper bound before binary search. Verdict: CONFIRMED on these fixtures; no full-game improvement or universal fast-simulator correctness is inferred. F28 remains frozen with its separately documented bug. Artifact: `bot_research/runs/validation/f29-threshold-check-001.json`. Registration: `bot_research/experiments/validation/analysis/append_monotonicity/verification/f29_threshold.json`.

## 2026-10-31T11:26:49.802934+00:00 Delayed-switch hypothesis declared

Claim: a delayed departure from a recognized policy can exploit the one-round delay before observable rejection. Proof 42 states the exact indistinguishability claim; winning is separate. Method: new `delayed_policy_switch` follows frozen E17, substitutes a construction-preserving tier3 or tier5 purchase in round 3, 5, 7, 9, 12 or 20, then starts fresh E20. Both assignments and a no-switch E17 control give 26 declared standard-start games against AdaptiveContinuation(weight4). Components run before games; manifest `experiments/validation/delayed-policy-switch-001.json`. Verdict: OPEN pending results. No reserved C condition is used. Lead and economy lane: please review the proof and the distinction between delayed rejection and successful defense; this is continued model collaboration through shared notes.

## 2026-10-31T11:27:43.955522+00:00 Remaining scope points in the interim report

Claim under review: REPORT section 5.8 says that S=1140 below1500 implies tier5 passage by P1. Method: read the current draft and compare the sufficient immunity statement with proof25/current_immunity. Result: the converse remains invalid; gun damage can stop a roster even with S below1500. The recorded eight-tier5 attack and 840 actual damage support the particular loss independently. Verdict: REFUTED as a deduction from P1, as already noted at06:47. Lead: replace the inference with the actual replay result and retain the one-direction sufficient condition.

Selection wording: the interim opening calls best.py the strongest bot found within all listed conditions. The listed tests now include counter-cycles and materially stronger targeted opponents, with no single fixed pooled selection score. Please name the actual selection criterion or say it is the selected general-purpose entry point with its measured scope, rather than implying dominance over all tested policies. This is a reporting recommendation, not a new performance claim. Latest completed additions await integration: exact guarded-forecast wins, adaptive-catalogue membership and fallback limits, and the23/24actual-entry prefix completion accounting. Reserved C remains unused.

## 2026-10-31T11:30:27.319454+00:00 Guarded adaptive continuation is not a uniform improvement

Claim: replacing only the adaptive controller's opening with the cheap guard improves its result on the seven-opponent development set. Method: 28 declared standard games (two guard rosters, both assignments) and 28 matched comparisons with the unguarded weight4 controller. Result: one-tier1 guard 6W8L; two-tier1 guard 6W2D6L; unguarded parent 10W4L on the same seven opponents. All14 swapped pairs have identical complete trajectories; none of the28 parent comparisons has an identical trajectory. Transitions, counting each of the two interventions separately: 12W->W,8W->L,6L->L,2L->D. Verdict: REFUTED as a uniform improvement.

The one-tier1 guard beats best_v9b800:773, F26/F27 770:515, but loses to E17 (-1426:753,round40), E19 (-4086:753,round39), the corner guard768:800 and F27memory790:795. The two-tier1 guard keeps best_v9b800:773 and E17/E19 800:761, but loses to F26/F27 765:790 and the corner guard768:800; it draws F27memory790:790. These are candidate-first HPs, equal in both assignments. The opening cost alters later planning and economy, so one favorable component does not guarantee a favorable full game.

All sources and actions pass strict audit;558 true-member forecasts are exact,784 fresh E20 continuation decisions reproduce, and all28 games replay on the original engine (19.189639s). The fresh-policy recomputation takes194.465696s. Evidence: `runs/validation/guarded-adaptive-continuation-summary-001.json`, corresponding comparisons/traces/attacks/fresh-policy/replay files, and proof40's full_games receipt. Lead: the unguarded adaptive controller remains the better aggregate on this specific set, while the guarded variant changes the F27memory failure from a round12 loss into a draw. No universal ranking follows.

## 2026-10-31T11:30:27.319454+00:00 Delayed-switch ablation started

Early delayed-switch games include wins with zero purchased copies, so an unexpected wave is not a sufficient explanation. The declared20-game controls use wave/save/original-prefix output at rounds5,9,12 (tier3), an identical fresh E20 continuation next round, and direct E20 from round1; both assignments. Twelve matched comparisons are declared. Component checks precede full games; core28 now runs this pipeline. Claim that the wave itself is necessary: OPEN. Manifest `experiments/validation/delayed-switch-ablation-001.json`; argument `analysis/delayed_policy_switch/ABLATION_HYPOTHESIS.md`.

## 2026-10-31T11:31:01.207265+00:00 Larger defensive search recovers one known full-game loss

Claim: raising the free defensive search budget from15 to30 steps improves at least one of the six predeclared asym:3:2 conditions against frozen best_v9b. Method: the same frozen target, synchronized private model, wrapper, prefix and attack schedule in both arms; three schedules, both assignments;12full games and six matched comparisons. Result:15steps0W0D6L;30steps1W0D5L. Verdict: CONFIRMED within this development set. The winning change is tier3round5, counter in seat0: final HP -330:722 in round41 becomes790:722 in round50. The complete histories agree through round40; their first action difference is the exact round41 position diagnosed by the original-combat witness. This connects the local search-limit failure to a full-game win in that condition.

The tier4round7 seat0 change prevents destruction (-1310:800,round46 becomes790:800,round50) but still loses the HP comparison. The other four conditions still lose: tier3round5seat1 is completely identical (-40:712,round28); tier4round7seat1 improves -320 to-40 at round38; drip seat0 improves -470:740 round42 to-50:740 round43; drip seat1 improves -180 to-160 at round31. No broad guarantee follows. All12games have legal actions, no errors or source drift,466exact forecast rounds, and pass original-engine replay in10.144637s. Allsix physical-seat pairs differ under the asymmetric prefix. Only one of the six15-versus30comparisons is identical. Artifacts: `runs/validation/frozen-best-prefix-steps-summary-001.json`, `frozen-best-prefix-step-comparisons-001.json`, and proof39 full_games receipt. No live best.py freeze is required by these completed frozen-copy tests.

## 2026-10-31T11:32:07.828207+00:00 Integrity and resource checkpoint

Claim: the protected project is unchanged from the recorded starting state. Method: hash every file and symlink outside bot_research, including the pre-existing virtual environment, and compare against integrity-start.json. Result: 903 entries; baseline differences {'added': [], 'changed': [], 'removed': []}; 1002 original missing manifest entries and the same three original hash mismatches. Verdict: CONFIRMED if all three baseline difference lists are empty. No protected file was repaired. Owned artifact scan checks 16741 text files and reports 0 absolute-local-path violations. Total owned project and lane bytes: 2365691925; free filesystem bytes: 116769730560. Artifacts: runs/validation/integrity-mid-1131.json and artifacts-mid-1131.json.

## 2026-10-31T11:36:20.284228+00:00: common five-policy development table declared

Claim: aggregate results against different selected opponents cannot establish a policy ordering. A shared finite table can describe the five listed policies under one exact condition, with no claim about outsiders.

Method: `current-policy-game-001.json` declares all ten unordered pairs, both physical assignments, of best_v9b, frozen economy21 (the recommended parameters), fortress32, the one-tier1 corner guard at (9,1) with unheld foreign attacks, and AdaptiveContinuation weight4. All twenty games use the standard start and the independent unchanged-engine harness, with strict source checks, full replay, and separate rational certificate verification. Proof43 in `analysis/current_policy_game/PROOF.md` precedes execution. The reverse matrix entries reuse these games with opposite payoff; diagonal entries are defined as zero, not measured self-play. Fortress32 retains a time-limited gun search; mismatched assignment histories will be reported, not averaged away as noise or called independent trials.

Result: launched on core29; no game results yet. The first four policy families include recent recommendations but best_v9b is the explicitly older frozen entrypoint. No reserved C condition is used.

Verdict: OPEN. This comparison supplies development evidence and an exactly scoped empirical policy game, not universal strength or final validation. Lead/Opus review can challenge the table interpretation while execution continues.

## 2026-10-31T11:41:28.646116+00:00: relevance-filter counter hypothesis for V23R

Claim: positive route coverage does not establish that a turret can stop even one standard copy. On the otherwise empty map, gun1 at (0,2) can hit a copy at most twice (16 damage); at (9,11), it covers only one nonterminal route cell (8 damage). Every standard type has at least20 HP. Both therefore cover the route but kill no copy, for any roster or modulo-spawn collisions; all base arrivals match the empty map. Standalone informal proof44 is written in `analysis/weak_covering_bluff/PROOF.md`.

Method next: independently check the route/coverage and original combat, then compare a frozen snapshot of the proposed V23 policy with mid_relevant=false/true against the original off-route (0,11) and these two weak covering positions, both assignments. The bluff cost, factory schedule and offensive tier remain fixed. This addresses the new relevance filter in the lead's11:35 status. No reserved C condition is involved.

Result: geometric argument complete; component and full-game evidence pending. Verdict: OPEN for the claimed full-game bypass. The lead can evaluate these positions independently; a turret-count fix and a positive-coverage fix are distinct, but neither is a defense-strength certificate.

## 2026-10-31T11:45:08.327110+00:00: five-policy common table and exact mixture complete

Claim: one of these five policies dominates the other four on the standard start. Method: all ten unordered pairs, both assignments, strict input and source checks, twenty unchanged-engine replays. Result: every policy has at least one losing opponent. Per-policy records on its eight games: corner guard6W2L, best_v9b4W4L, F32 4W4L, adaptive weight4 4W4L, E21 2W6L. Verdict: REFUTED. All ten assignment pairs have identical normalized full histories, so twenty executions represent ten distinct paired trajectories here, not twenty independent samples. Sum of game wall times is 401.893942s.

In order [best_v9b,E21,F32,guard,adaptive], the row payoff matrix is [[0,1,1,-1,-1],[-1,0,-1,1,-1],[-1,1,0,-1,1],[1,-1,1,0,1],[1,1,-1,-1,0]]. A separate exact Fraction checker confirms p=(1,3,1,3,1)/9 makes every column payoff zero. Antisymmetry then proves value0 for this empirical table; every pure policy has worst payoff-1. E21 receives probability1/3 despite the lowest raw win count because it defeats the corner guard. Claim of this finite-table certificate: CONFIRMED, conditional on these recorded policies and conditions. It is not an all-bot equilibrium, a future expectation for F32's clock-limited planner, or an implemented secret-randomized deployment guarantee.

Useful cycle for lead/Opus review: guard beats best_v9b800:795; best_v9b beats E21 795:785; E21 destroys guard768:-1337 at round21. F32 beats adaptive344:-2297 at round39, while adaptive beats best_v9b800:765 and E21 800:768. These are all newly matched conditions from one declaration, not scores assembled from unequal opponent sets. Sources, normalized trajectories, exact specs and certificate are in `runs/validation/current-policy-game-{summary,matrix,certificate,certificate-check}-001.json`; proof43 verification/full_games.json binds the six artifacts.

The weak-covering-bluff12-game pipeline is now on core29 (PID2387041), after the table completed11:43:25. The private V23 snapshot copies nine lead modules with only namespace substitution; its provenance and both mid_relevant settings are declared before execution. Component checks compare original combat on three maps and twelve actual-engine original/snapshot prefixes before any full games. No C condition is used.

## 2026-10-31T11:45:54.910976+00:00: V23R relevance filter bypass CONFIRMED

Claim: changing the bluff gun to positive route coverage can still defeat the proposed V23R filter. Method: a private nine-module snapshot of lead v23, differing only by namespace substitution, with the full V20T parameter set and mid_relevant=false/true; three gun1 positions, both assignments, twelve predeclared standard full games. Original-versus-snapshot equality passed on all108 decisions in twelve9-round prefixes. Independent original combat checked99 map/roster cases, including counts249/250/251/500 and503 mixed entries, with identical per-tick arrivals and zero kills. Component runtime17.092084s.

Result: unfiltered policy loses all6 games, HP-320:660 at round9. Filtered policy beats the old off-route gun(0,11), HP520:-75 at round12, both seats. It still loses to gun(0,2) and gun(9,11), both seats, HP-320:660 at round9. Every full game has legal actions, no bot errors or source drift, and passes original-engine replay. All six seat pairs have identical normalized full histories. Verdict: CONFIRMED for the bypass; REFUTED for the claim that positive route coverage fixes this bluff family. This is an independent test of the proposed policy snapshot, not a test of a newly posted best.py.

Lead/Opus: the gun at(0,2) has only16 possible damage per copy and the gun at(9,11) only8. They satisfy _covering_turret but cannot kill tier1. Both cost the same30 gold as the old off-route gun and preserve its empty-map base arrivals. Their public presence is enough to preserve the losing branch. The original off-route control reproduces your -980 HP margin without filtering and +595 with filtering. Evidence: `runs/validation/weak-covering-bluff-{components,strict,replay,summary}-001.json`; exact parameters and source hashes in `experiments/validation/weak-covering-bluff-001.json`; proof44 and its verification receipts. Reserve C remains unused.

## 2026-10-31T11:47:37.280149+00:00: extent of the one-gun bluff failure

Claim: the observed bypass may extend beyond zero-kill guns. Method: predeclared all142legal single-gun1 cells against the same frozen V23R, both assignments (284games). The post-run checker will independently repeat the legality census and classify each map by original-combat kills for solo tiers1..5, three tier1, and250 tier1. Complete coverage is required before any exhaustive conclusion. Result: launched oncore29. Verdict: OPEN. This is development evidence; C remains untouched.

The six matched relevance-flag comparisons are also complete: both weak covering positions have identical full histories with the flag off/on (four comparisons); the old off-route position first differs in round2 (two comparisons). In the latter, unfiltered buys a splash and one factory in round2 while filtered buys four factories. Evidence: `runs/validation/weak-covering-bluff-comparisons-001.json`.

## 2026-10-31T11:52:49.568114+00:00: frozen best_v9d also loses to both weak covering bluffs

Claim: the proposed frozen best_v9d has the same bypass as the private V23R snapshot. Method: six new direct-entrypoint games against all three earlier bluff positions, both assignments, with frozen file SHA256 95342aa9b39efe01d0fa28eccac1d66a4a05a7085da99e302e8e32b486757e55. Result: all six normalized full histories are identical to the earlier relevance-true games. Off-route (0,11) is beaten 520:-75 in round12; weak covering (0,2) and (9,11) both beat best_v9d -320:660 in round9. Record2W4L, with three identical assignment pairs. All six strict checks and original-engine replays pass. Verdict: CONFIRMED. This is a development counter against the actual frozen file, not just its experimental twin; the live best.py remains separately versioned.

Lead/Opus: this directly challenges promotion based only on the old off-route bluff. A turret that covers the path can be provably unable to kill any copy. Please include these two positions in development regression and review whether the relevance condition should represent a credible defensive commitment rather than any positive coverage. No policy change is prescribed by these two examples alone; a stronger threshold can create other blind spots. Artifacts: `runs/validation/frozen-v9d-bluff-{strict,replay,summary,comparisons}-001.json`; proof44 verification/frozen_entrypoint.json. Reserved C remains UNUSED, pending the explicit final freeze request.

## 2026-10-31T11:54:50.559859+00:00: delayed-switch counter and purchase ablation complete

Claim: a delayed change of policy can defeat AdaptiveContinuation(weight4), even though it beats the unchanged prefix policy. Method:26 predeclared standard games against the E17 prefix, switched at rounds3,5,7,9,12,20 to construction plus tier3/tier5 purchases, then fresh E20; both assignments and two unswitched controls. Result: observer10W16L, with13 identical assignment pairs. Every round3/5/7/9 switch wins against the observer; every round12/20 switch loses, as does unchanged E17. The observer retains800 HP and wins800:768 in all ten winning cases. All24 reached switches change the observed purchase signature; the E17 clone remains valid until the substituted action, and permanent fallback begins in the next round. Verdict: CONFIRMED for this declared targeted set, with no claim of universal deception or a defect in exact forecasting of fixed catalogue members.

Claim: a surprising switch-round attack is necessary for these counter wins. Method:20 additional predeclared controls at switch rounds5,9,12, modes wave/save/original-prefix, plus direct E20 from round1, both assignments. Result: observer8W12L. Wave and save both lose at rounds5/9 and win at12. At5, observer HP is-58 for wave and-40 for save, ending in round11; at9 it is40 and100, respectively, with opponent768 at round50. Submitting the original E17 list at5 still beats the observer-40:768 in round11, and at9 beats it-20:768 in round16; the first mismatches move to rounds6/10 and fallback to7/11. The round12 prefix control wins800:768; E17 first mismatches at18 but another catalogue member survives, so permanent fallback never begins. Direct E20 also loses800:768 to the observer. Verdict: necessity of the surprising attack REFUTED; the opening-plus-continuation combination matters in these conditions. Exact mechanisms after rejection remain a separate analysis, since these policy interventions change later states, income and defense.

All46 games pass strict source/action/error checks and unchanged-engine replay. Base replay26 takes16.424389s, ablation replay20 takes16.915301s. Fresh observer E20 decisions are independently recomputed:512 base calls in424.965883s,362 ablation calls in323.254825s. All opponent decisions are recomputed from their actual public observations as well. The observer trace checks cover836 and698 rounds; these are not836/698 exact predictions of an outside-catalogue policy. Selected attack audits cover324/336 enabled decisions and602/564 target maps. Twelve matched ablations all have different complete histories; their W/D/L outcomes agree within each switch time. Sources and receipts are in proof42 verification/full_games.json and ablation_full_games.json; compact results are `runs/validation/delayed-switch-results-001.csv`.

Lead/Opus review: this is a concrete limit of committing economically to an identified policy. Immediate rejection after visible evidence does not restore the factories forgone before rejection. It supports keeping the distinction between exact conditional prediction and robust play against an opponent that changes policy. It does not justify changing the frozen best entrypoint without a separate matched test.

## 2026-10-31T11:56:07.134708+00:00: complete placement census and a cheaper roster counter

Claim: positive turret coverage removes the bluff failure across all single-gun positions. Method: enumerate every legal round-one gun1 cell with original apply_action, declare all142 positions, and play the private frozen V23R against each with both assignments. Result:284 legal, error-free games, all original-engine replays pass in18.431005s; all142 assignment pairs have identical full histories. Every one of the61 covering placements defeats V23R, and every one of the81 noncovering placements loses to it. Four covering positions cannot kill a solo tier1: (0,2), (9,10), (9,11), (10,11); these eight games all end-320:660 in round9. Verdict: REFUTED for the complete declared placement family. The remaining57 covering maps kill a solo tier1 in the diagnostic combat; their full-game wins are not thereby classified as bluffs or causally attributed to the filter. The finite family does not cover all defenses, timings or rosters. Artifact: `runs/validation/bluff-placement-census-classification-001.json`, with compact CSV and proof45 receipt.

Claim: a cheap round-two roster purchase can also defeat this V23R without any turret. Method: forty predeclared games, two relevance settings, optional weak covering gun1 at(0,2), and five round-two bait lists; unchanged factory growth through6 and tier5 waves from7. Forty four-round component prefixes establish exact purchases, legality, input immutability and visibility of the roster predicate. Result: each relevance setting scores12W8L, and all20 flag comparisons have identical full histories. With no gun, no bait loses to V23R520:-290 in round12, while one tier1 (cost15) defeats it-465:665 in round9 and two tier1 defeat it-330:665 in round9. Three tier1 and one tier2 lose to V23R225:-475 and368:-260. With the weak gun, empty bait and one tier1 defeat V23R; the larger tested baits lose. All40 strict checks and original-engine replays pass, replay time2.957965s. Verdict: CONFIRMED for the stated one/two-tier1 conditions. Buying more bait is not uniformly stronger.

The roster predicate becoming true is proved in result46, but it is not a proof that mid_joint alone causes the losses: bait changes gold, factories, damage and bounties. The next matched ablation will disable mid_joint, with and without the round-one guard, on all ten already declared bait conditions. This follows the lead/Opus11:53 decision to withdraw best_v9c/v9d and compare no-joint policies. I confirm that withdrawal has been read; reserve C remains UNUSED.

## 2026-10-31T12:00:04.439507+00:00 Joint-plan removal does not remove the cheap-roster failure; opening guard worsens this pool

Claim: removing mid_joint removes the round-two small-roster failures, and adding the proposed gun1(4,1) opening does not reopen the grower loss. Method: two declared private V23 snapshots, mid_joint=null and that policy plus r1_gun=[4,1], against every one of the same ten grower/bait settings, both assignments. All40 conditions completed; strict accounting,40 original-engine replays (2.490559s) and40 four-round component prefixes (4.932143s) pass. All20 assignment pairs have identical normalized histories.

Result: no_joint16W4L; no_joint_guard2W18L. The no-turret one- and two-tier1 baits still beat no_joint, respectively -465:665 and -330:665 at round9. Removing the joint plan fixes the weak-gun empty/one-tier1 cases, but all ten no-turret histories are identical to the original relevance-filter candidate. Guarding round1 loses even against the no-turret, no-bait baseline (-460:665, round9); its only winning setting is weak gun plus three tier1 copies (380:-365, round14). The guard's one- and two-tier1 no-turret cases both end -40:710 at round8. Sixty declared pair comparisons reuse40 new and20 earlier executions;10 whole histories coincide. They are not60 new strength samples.

Verdict: both improvement hypotheses REFUTED on this pool. These are private-snapshot interventions; I will check equivalence against the actual proposed V18FT/V24G entry points before attributing their result to those named candidates. Evidence: runs/validation/roster-bait-joint-ablation-summary-001.json, comparisons-001.json, compact CSV, and analysis/roster_bait/verification/joint_ablation.json. Lead: this is a consequential additional counter beyond the covering-turret issue; please inspect before promotion.

Claim: the shared wave settings in delayed-policy-switch and delayed-switch-ablation are equivalent reruns. Method: all six shared conditions, checking matching candidate, assignment, initial state and engine seed, then every normalized action/state record. Result: all six complete trajectories agree. Verdict CONFIRMED for those six conditions. They add reproducibility evidence, not six independent scenarios. Receipt: analysis/delayed_policy_switch/verification/wave_equivalence.json.

## 2026-10-31T12:01:50.780191+00:00 The proposed opening guard is not a universal round-one shield

Claim: gun1(4,1) protects V24G against all legal first-round minion purchases. Method: exhaustive enumeration of all27 ordered words costing at most100 (proof and count in analysis/proposed_opening_rosters/PROOF.md), each against actual V18FT and V24G in both assignments,108 original-engine one-round executions. Every action legal, first policy action list identical across words, observation unchanged, all sources unchanged.

Result: V18FT maximum incoming32; V24G maximum incoming27, attained by the ordered list [tier1,tier2,tier1,tier1,tier1]. Both have worst first-round own-minus-opponent HP margin -17 within this minion-only class, because V24G reduces its own opening poke from three to two tier1. V24G has9 of27 zero-damage rosters (including empty), not all27. Verdict REFUTED for a universal shield; this does not contradict the lead's narrower one-to-six tier1 and one-tier2 checks. Full-game implications remain OPEN. Evidence: runs/validation/proposed-opening-rosters-001.json,108 short replays alongside it, and topic47 verification/components.json.

## 2026-10-31T12:02:41.805653+00:00 Direct V18FT and V24G checks confirm all forty private-snapshot trajectories

Claim: the actual proposed entry points have the preceding ablation outcomes. Method: new forty-game declaration using experiments.lead.v19 with the lead's V18FT parameters and experiments.lead.v22 with its V24G parameters. All ten opponents, both assignments, source hashes before and after, strict outcome accounting and original-engine replay. Compare every normalized action and state with the corresponding private-snapshot run.

Result: all forty complete trajectories are identical. Actual V18FT is 16W4L; actual V24G is 2W18L. V18FT still loses to no-turret round-two one/two-tier1 bait (-465:665 and -330:665, round9). V24G loses the empty no-turret grower control (-460:665, round9), among its eighteen losses. Verdict CONFIRMED for these exact candidate definitions and conditions. This is direct reproducibility evidence, not forty independent new scenario draws. Source closure, component checks and all replays pass; receipt in analysis/roster_bait/verification/direct_entrypoints.json.

## 2026-10-31T12:03:18.573798+00:00 The no-turret roster bait transfers to best_v9b but loses to economy21 and fortress33

Claim: the one- and two-tier1 baits defeat all four tested policies. Method: all five no-turret grower variants against frozen best_v9b, the recommended frozen economy21 configuration, frozen fortress33, and adaptive catalogue continuation (weight4), both assignments. Forty conditions declared before execution; source hashes, component prefixes, strict accounting and original-engine replays pass. All twenty assignment pairs are identical.

Result: best_v9b6W4L, economy21 10W, fortress33 10W, adaptive continuation 10L. Best's one/two-tier1 failures are the same HP and round as V18FT: -465:665 and -330:665, round9. Economy21 beats every grower in rounds7-8. Fortress33 wins in rounds9-10, but ends at88 HP against the one-tier2 bait. Adaptive continuation loses even to the empty grower control (-600:620, round9); the bait is not necessary for that weakness.

Verdict REFUTED for transfer to all four; CONFIRMED for a counter to frozen best_v9b under these conditions. These counters are development data. Fortress33 retains a wall-clock search limit; its results describe this execution. Evidence: runs/validation/roster-bait-cross-policy-summary-001.json and CSV, with receipt analysis/roster_bait/verification/cross_policy.json. All jobs in this lane are now complete. Next I am checking the cheap-poke-insurance mechanism and early-wave regressions.

## 2026-10-31T12:11:48.522964+00:00 Growth-horizon grid does not break E21 or F33; wall-assisted counter is now running

Claim: changing the empty-map bait grower's horizon can defeat the recommended E21 or F33. Method: all horizons4 through9 and five declared round-two bait lists, no turret, both assignments. Result: E21 60W, F33 60W; all60 normalized assignment pairs identical. All120 four-round component prefixes, strict checks and full original-engine replays pass (replay10.134304s). Verdict REFUTED for this finite grid. This includes earlier growth6 controls, which are repetitions rather than independent evidence. The full table is runs/validation/roster-bait-growth-grid-summary-001.json; receipt is proof46 verification/growth_grid.json.

Claim: a searched fixed-wall map can improve cash before the flood. Method: wrote the exact no-hit recurrence proof48, then a deterministic finite search with seed310126,12 starts and1800 steps per start, evaluating12448 distinct maps. The best selected map has46 walls and route length70; its round6 cash is1659 versus1497 on the empty map and1600 with the20-wall lead opening. Every one of12 imported JSON layouts was checked on the original engine against idle for nine rounds and both assignments, including all action legality and income values (2.104208s). Verdict CONFIRMED for these no-hit component values; no global maze optimum or full-game advantage is claimed.

The new maze_grower grid declares216 full games: V18FT, E21, F33; three layouts; horizons5/6/7; four baits; both assignments. It is running oncore30. The imported data are pinned by the policy checksum and campaign manifest, and the new data-aware runner archives and checks every declared data input. Cheap-poke ablation140 continues oncore28. Source inspection shows mid-tier insurance has its own activation path even with poke_insurance=false; I will test that separate intervention after the resource scan. Reserve C remains unused.

## 2026-10-31T12:22Z | Maze-assisted growers: complete 216-game check and delayed-guard follow-up

Claim: a longer first-round wall route can improve the blind grower's economy enough to expose the current candidates. Method: the declared maze-grower-grid-001 has three layouts (empty, lead's 20-wall opening, searched 46-wall cash_rank_1), growth through rounds5/6/7, four round2 baits (none, tier1, two tier1, tier2), V18FT/E21/F33, and both assignments. All216 conditions passed strict accounting and original-engine replay. All108 assignment pairs have identical normalized complete trajectories. These are development conditions, including previously used controls, not216 independent random samples.

Result: V18FT20W52L; E2170W2D; F3372W. E21's two draws are both assignments of lead_opening_g5_t2: HP -52:-177 at round9, with both_bases_destroyed. The engine correctly calls this a draw despite unequal negative HP. The searched cash-maximizing maze did not beat E21 or F33 on this grid. F33 retains a wall-clock search budget; the statement describes these recorded executions.

Verdict: CONFIRMED that this declared family exposes V18FT, REFUTED that it beats E21/F33 within the tested grid; no global conclusion. Evidence: runs/validation/maze-grower-grid-summary-001.json and .md; strict/replay files with the same stem; analysis/maze_growth/verification/full_games.json. The runner archives and hashes the JSON wall layout alongside imported source files.

Next declared intervention: one splash installed in round3/4, empty or cash_rank_1, growth5/6, bait none/tier2, against the same three candidates, both assignments (96 conditions). No reserve-C use. The original-engine component check completed12:21:39 in1.400608s: 12 six-round prefixes and84 combats, including tier1 roster sizes249/250/251/500, all passed. Selected guard cells/exposure: empty(10,1),50; lead_opening(1,3),70; cash_rank_1(2,8),60. Exposure is per-copy splash damage before arrival. Once installed, each guard excludes tier1 arrivals regardless of count; late copies can still be cleared alive. This does not protect against all higher tiers or guarantee survival until installation. Proof49 and exact JSON are under analysis/guarded_maze and bots/counters/data/maze_guards_001.json.

Opus collaboration: I read economy lane entry15 and am independently replaying its asym:24:3 capacity example, checking original combat at counts500/750/1000/3000 and recording affordability separately. The fixed-map capacity proof already covers the stated PropositionG. One wording qualification for that entry: E23 is not at least as good as E21 in every HP margin (the listed mirror:21:2 loss grows from-1022 to-2272). Its listed advantage is in aggregate W-D-L and selected outcomes. These are different objectives.

## 2026-10-31T12:23Z | Opus capacity example independently confirmed on the original engine

Claim: the economy lane's reported 500-copy cap can hide a damaging affordable attack against a sub-immunity fortress. Method: independently replay all35 rounds of w1v29c, asym:24:3, E24 seat0 against frozen fortress28. Then replace the attacker roster in component calls by homogeneous tier5 counts500/750/1000/3000 on the unchanged end-round20 and24 maps. Compare original simulate_map with frozen fastsim and with both exact integer gun-capacity bounds. Full game replay, legal-action checks, source hashes and all eight combats pass; runtime15.329795s.

Result: both recorded maps have route42, splash exposure960, 27 splashes, 26 gun3, two gun2 and one gun1. G=1482. The original engine returns respectively0/201/409/2074 hits, exactly as Opus reported. For1000 copies the coarse bound is146 arrivals. The stronger firing-support bound uses319869 total possible gun damage, hence at most592 tier5 kills. It certifies682 copies as sufficient for at least6 arrivals (840 damage), priced443300. That exceeds the251936 end-round20 cash but is below the518480 end-round24 cash. The map is not full, so this is a fixed-map statement and a defender could still build.

The frozen offense search at a deliberately supplied500000 budget and active_cap4000 returns769 tier5, cost499850, predicted damage30800 in0.202325s, plus a mixed package with the same damage. Thus the reported package and damage are also reproduced. I did not treat these component attacks as new full-game wins or certify the defender's simultaneous response. Opus's separately reported seven additional wins with enlarged caps remain its full-game evidence.

Verdict: CONFIRMED for the exact map, simulator agreement, cap mechanism and stated affordability distinction. Evidence: runs/validation/attack-cap-example-001.json; experiments/validation/check_attack_cap_example.py; analysis/fixed_gun_support/verification/attack_cap_example.json. This is a continuing cross-model check with the economy lane (actual model previously confirmed as us.anthropic.claude-opus-5-5), not an outside model call or remote computation.

## 2026-10-31T12:27Z: cheap-poke insurance ablation complete, partial repair only

Claim: the cheap-poke insurance layer explains the new no-turret roster-bait losses, and disabling it removes them without reviving the early timing losses.
Method: the predeclared `roster-bait-poke-insurance-001.json` runs five variants against the ten roster-bait cases and four budget-timing controls, both assignments, 140 original-engine games. Variants are actual V18FT, V18FT with poke_insurance=false, V18FT with poke_until=2, actual V24G, and V24G with poke_insurance=false. All strict source/action audits and original-engine replays passed; replay took 50.385964 seconds. Seventy assignment pairs have identical complete trajectories. The 84 declared variant comparisons contain 36 identical histories, so repeated baselines and paired seats are reproducibility checks, not independent samples.
Result: W-D-L totals in that order are 16-2-10, 18-2-8, 18-2-8, 2-6-20, 4-6-18. Disabling cheap insurance fixes the TWO-tier1 no-turret bait, from -330:665 in round9 to 370:-300 in round11. The ONE-tier1 bait remains a loss, changing -465:665 to -45:615 in round9. The four early timing controls retain V18FT's -20, -12, -26 and 0 margins. Both changes therefore leave counterexamples. The separate mid_until=null ablation, including E17/E21 regressions, is still running.
Verdict: REFUTED as a complete explanation or repair; CONFIRMED as a partial improvement on these conditions. Receipt: `experiments/validation/analysis/roster_bait/verification/poke_insurance.json`. Detailed pairs and purchases: `runs/validation/roster-bait-poke-insurance-comparisons-001.json`; summary with every condition: `runs/validation/roster-bait-poke-insurance-summary-001.json`. These are development results, not pool C. Pool C remains unused.

## 2026-10-31T12:27Z: exact splash threshold component check and ongoing counter extension

Claim: on the three selected fixed guarded maps, a homogeneous copy can arrive precisely when its spawn index is eligible and its HP exceeds total splash exposure.
Method: original simulate_map on all five tiers at 1, 6, 249, 250, 251 and 500 entries on each of the three maps, plus one alternating tier1/tier2 roster of 502 entries per map. Source and data hashes checked before and after.
Result: all 93 combats passed in 1.143073 seconds. Empty/lead_opening/cash_rank_1 exposures are 50/70/60. The lead_opening guard therefore excludes tier2 arrivals, including equality at HP70. This says no arrival; late copies can still be cleared alive.
Verdict: CONFIRMED on these fixed maps. `analysis/guarded_maze/verification/threshold_components.json` pins the checker, result and prior hypothesis. The 96-game guard experiment is ongoing. Its economy21 block is complete at 18 wins and 14 losses, before final replay audit; this is a new counter to a candidate that won 70 and drew2 in the unguarded grid. No full-game claim is certified yet. A predeclared 48-game extension launched at 12:26:55 tests the lead_opening threshold against economy21 and fortress33, growth4/5/6, guard3/4, no bait or round2 tier2, both seats. All of this is development evidence.

## 2026-10-31T12:32Z: delayed splash is a verified counter to economy21; fortress33 survives

Claim: a single splash, built late enough to leave early spending unchanged, can reverse the unguarded grower's losses.
Method: predeclared `guarded-maze-grid-001.json`, 16 opponents (empty/cash_rank_1, growth5/6, guard3/4, no bait/round2 tier2) against actual V18FT, recommended economy21 and frozen fortress33, both assignments. A second predeclared grid tests lead_opening at growth4/5/6 against economy21 and fortress33, 48 games. These were chosen after earlier development outcomes and are not held-out validation.
Result: the first grid gives V18FT20-0-12, economy21 18-0-14, fortress33 32-0-0. The second gives economy21 16-0-8 and fortress33 24-0-0. All144 games passed strict source/action accounting and unchanged-engine replay (12.850066 and5.457512 seconds), and all72 seat pairs have identical complete trajectories. Every guard3 opponent loses to economy21. On the first grid seven of eight guard4 opponents beat it; the exception is empty/growth5/no bait. On lead_opening both guard4 growth5/6 bait settings beat economy21, while growth4 does not. The exact lead_opening/growth5/tier2 setting changes the unguarded simultaneous-destruction draw (-52:-177, round9) into an economy21 loss (-52:770, round9).
Representative trace: empty/growth6/no bait/guard4 changes economy21's unguarded 520:0 round7 win into -180:544 round9 loss. The public history before round4 is identical. Economy21 still buys eight tier1 and one tier3 in round4, while the grower buys its splash. Guarded versus unguarded, economy21's end-round4 gold is221 versus286, and the grower's HP is734 versus669. The first different economy21 action is in round5. This isolates an unobservable same-round construction change at round4; later reactions, income and purchases also differ. It does not establish that the whole win is caused by any single later branch.
Verdict: CONFIRMED on the declared grids; REFUTED as a counter to fortress33 on these conditions. The 96 and32 comparisons against matching unguarded controls, plus72 guard3/guard4 timing comparisons, are descriptive full-policy interventions. No new games were counted for those comparisons. Receipts are `analysis/guarded_maze/verification/guarded-maze-grid.json` and `guarded-maze-threshold-grid.json` under experiments/validation. The byte-level data archive audit also passed on all360 games across the unguarded and guarded campaigns: exact wall/guard JSON was frozen and archived. The first audit attempt assumed every manifest had an expected_conditions key; the checker was corrected to derive it from the Cartesian product when absent, then passed. No game artifact was changed.

For hrt-w2 (Opus): these are new standard-start counters to economy21. Reproducible opponent: `bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=6&guard_round=4&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000`. I am checking the newer frozen economic policies on the same twelve guard4 settings. For hrt-w1: fortress33 retained all56 wins across both guarded grids. Its representative growth6 trace has48 factories after round6 versus economy21's21, then it stops the third wave. A cheaper tier4-wave extension is now running, with its hypothesis recorded before launch. PoolC is still unused.

## 2026-10-31T12:40Z: the delayed-guard counter transfers unchanged to economy23 and economy25RM

Claim: the newer economic policies avoid the newly found standard-start delayed-guard losses.
Method: all twelve guard4 settings (three wall layouts, growth5/6, no bait or one round2 tier2), economy23 with the recommended replan_base=true parameters, and economy25RM with own_in_layout="replan", own_min_s=1200, min_cap=3000, active_cap=4000. Both assignments, 48 games, all declared before execution. Exact specifications are in guarded-maze-new-economy-001.json.
Result: each policy scores2W22L. Every one of the48 full trajectories is identical to the corresponding recorded economy21 trajectory, after player normalization. Strict source/action accounting and all original-engine replays pass; replay runtime4.630213 seconds, 24 identical assignment pairs. The only winning setting for either policy is empty/growth5/no bait. The exact wall/guard JSON and every declared input are byte-identical in the archived source closure, checked by maze-data-archives-002.json.
Verdict: REFUTED on this finite standard-start family. The changed foreign-layout planning and larger attack caps do not alter these trajectories. This does not contradict their gains on other scripted starts. Receipt: experiments/validation/analysis/guarded_maze/verification/new_economy.json. For hrt-w2: these are direct checks of your stated frozen configurations, not approximations of them. PoolC remains unused.

## 2026-10-31T12:40Z: cheaper tier4 waves fail on all108 delayed-guard conditions

Claim: replacing tier5 floods with cheaper tier4 floods exposes an earlier defensive weakness.
Method: three layouts, growth4/5/6, guard4, no bait or round2 tier2, against V18FT, economy21 and fortress33, both assignments. Result: each candidate wins all36 of its games. Strict accounting and all original-engine replays pass; 54 assignment pairs have identical complete histories. The72 available tier5-to-tier4 control comparisons differ in their histories, so these are substantive interventions rather than equivalent reruns.
Verdict: REFUTED for this declared grid. An initial post-processing assertion expected80 matching controls, but the earlier data did not include V18FT on lead_opening: the correct intersection is72. The assertion was corrected before the comparison artifact was written; no match or replay was modified. Source/data archive check passes for all108 games. Receipt: experiments/validation/analysis/guarded_maze/verification/tier4_grid.json. Tier4 being cheaper does not by itself make the grower stronger.

## 2026-10-31T12:40Z: insurance layers interact; neither removal is a complete repair

Claim: removing mid-tier insurance, alone or with cheap-poke insurance, eliminates the roster-bait failures without economic regressions.
Method: actual V18FT, mid_until=null, and mid_until=null with poke_insurance=false; ten declared gun/bait conditions, four budget-timing controls, economy17 and economy21, both assignments. All96 games, strict checks and original-engine replays pass (45.929542 seconds). All48 assignment pairs are identical. The96 descriptive variant comparisons contain28 identical complete trajectories.
Result: baseline20W2D10L; no_mid18W2D12L; no_mid_no_poke22W2D8L. Removing mid-tier insurance alone fixes the one-tier1 bait (95:-105, round13), but still loses the two-tier1 bait (-190:620, round9) and changes both economic matchups from a10-HP win to a16-HP loss (769:785, round50). Removing both layers restores economic wins (758:745, round50) and beats two-tier1 bait (370:-300, round11), but reopens the one-tier1 loss (-45:615, round9). All four early budget-timing outcomes remain unchanged: margins-20,-12,-26,0.
Verdict: REFUTED as a complete repair. The two insurance switches interact with spending and later reactions; neither isolated branch explains all failures. Receipt: experiments/validation/analysis/roster_bait/verification/mid_insurance.json. For the lead: this is additional evidence against treating a single insurance toggle as a general solution.

## 2026-10-31T12:46Z: two timed splash guards defeat fortress33; a third guard loses the timing race

Claim: extending the single delayed guard to two guards can stop the later tier2 purchases and reverse fortress33's wins.
Method: predeclared staged-guards-grid-001.json, three layouts, growth through round6, no bait, tier5 waves, and guard schedules [4,6], [4,6,8], [3,5], against economy21 and fortress33, both assignments. All36 games passed strict source/action accounting and original-engine replay (4.613358 seconds); all18 assignment pairs have identical complete histories. The separate original-engine component check passed90 combats and18 nine-round construction prefixes. All58 declared source/data inputs are byte-identical in the archive. The48 comparisons against earlier single guards and between two/three guards reuse recorded controls, not new games.
Result: economy21 6W12L; fortress33 16W2L. The new fortress33 loss is the empty layout with guards at (10,1) in round4 and (1,0) in round6, growth through6: -40:753 in round9, both assignments. Its one-guard and three-guard counterparts win. Against economy21 the same two-guard opponent wins in round9 (candidate HP -40, opponent592). All three [3,5] opponents lose to economy21; all other declared staged opponents beat it.
Mechanism: adding the round6 guard raises splash exposure from50 to80 and excludes tier2 arrivals. Against fortress33 this denies20 bounty gold in that round, and the first changed fortress action is in round7. Comparing two to three guards, fortress33 submits identical actions in every common round1..9. The grower enters round8 with1334 gold: without a third guard it buys two tier5 for1300; after spending60 on the third splash it can buy only one. Fortress33's round8 HP is380 versus520, and round9 HP is-40 versus240. The three-guard game ends with fortress33 winning240:-171 in round13. This is a concrete attack-tempo cost, not monotonic strength from extra splash exposure.
Verdict: CONFIRMED for this declared counter; REFUTED for the claim that additional guards always improve the outcome. Receipt: experiments/validation/analysis/staged_guards/verification/full_games.json. Reproduction opponent: `bot_research.bots.counters.staged_guard_maze:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&guard_rounds=[4,6]`. For hrt-w1 and hrt-w2: this is a new, model-free standard-start counter, selected on development results. A separate transfer to fortress34, economy23/25RM and lead candidates is running. For the lead: poolC remains unused; I have read your passive_until proposal and will test it as development, not consume the reserve.

## 2026-10-31T12:46Z: recorded fortress33 runtime is below its planning cutoff on this counter family

Claim: a wall-clock cutoff explains the observed guard-family outcomes.
Method: audit the validated result and replay attestations for all242 fortress33 conditions across roster-bait, maze, guard, threshold, tier4 and staged-guard campaigns. These contain2476 complete recorded decisions.
Result: no complete decision reaches3 seconds; the maximum is2.1058256491 seconds in guarded-maze-grid case0089. The frozen planner has a3-second wall-clock budget, but its individual internal branches were not instrumented. This audit is about recorded durations and cannot certify future runtime or complete determinism on another machine.
Verdict: no recorded duration supports a cutoff explanation here; broader causal attribution is OPEN. Artifact: runs/validation/fortress33-recorded-runtime-001.json; checker: experiments/validation/audit_recorded_runtime.py. Audit runtime1.703327 seconds.

## 2026-10-31T12:54Z: guarded-counter transfer to seven current policies

Claim: the staged two-splash counter and the fixed heavy-drip counter transfer beyond the original fortress33 target.
Method: guard-heavy-transfer-001.json predeclares seven policies, two opponents and both assignments, 28 complete games. The original-engine replay passes for every game (6.508716 seconds), and all14 assignment pairs have identical histories. A separate action-by-action check proves that the affordability filter changes none of the fixed heavy-drip schedule's submitted actions in all14 reached games. Its two fortress33 histories equal the independent hrt-w1 x117 records, whose recorded source hashes were checked. Four staged-guard histories equal the earlier economy21/fortress33 controls. Every declared source and data input is archived byte-for-byte.
Result: against the empty-map grower with splash guards in rounds4 and6, best_v9b wins520:-25 in round12, but V18FT loses520:755 in round50. Economy21, economy23 and economy25RM each lose-40:592 in round9; fortress33 and fortress34 each lose-40:753 in round9. Against the fixed heavy-drip schedule, best_v9b wins515:-671 in round15, V18FT wins375:-1348 in round35, all three economy variants win795:-35 in round12, and both fortress variants lose-45:700 in round10. Aggregate12W16L is a description of this selected transfer table, not a strength ranking.
Verdict: CONFIRMED for the stated transfers; no tested candidate wins both staged guard and roster-bait families. Receipts: experiments/validation/analysis/guarded_heavy_drip/verification/full_games.json and analysis/staged_guards/verification/transfer.json. The independent heavy-drip prescription check is runs/validation/guard-heavy-prescription-check-001.json. For hrt-w1: your counter_astra33 docstring's745 final counter HP is a transcription error; actual HP is700 and its winning margin is745. Your reported margin is correct. PoolC remains unused.

## 2026-10-31T12:54Z: a public opening selector beats all seven fitted policies, then fails a simple opening perturbation

Claim: the two complementary grower arms can be selected using only the opponent's public first-round roster.
Method: bots/counters/public_opening_selector.py buys five factories in round1. In round2 it selects the one-tier1 round2 bait arm exactly when the opponent roster contains three tier1 copies, all bought in round1; otherwise it selects the staged guards [4,6]. Selection is permanent until a new round1. Both arms have the same round1 actions, empty layout, growth through6 and tier5 waves. No pending action, policy name, hidden engine object or model identity is inspected. The standalone proof gives conditional trajectory inheritance for these stateless arms, not identification or strength. Twelve original-engine prefix checks cover both seats, six opening rosters, later roster changes and bot reuse; they pass in1.176919 seconds.
Result: public-selector-known-001.json records wins against all seven fitted policies, both assignments: best_v9b and V18FT end-465:665 in round9; economy21/23/25RM end-40:592 in round9; fortress33/34 end-40:753 in round9. All14 full histories exactly equal the corresponding fixed-arm controls; they do not create14 independent discoveries. On the predeclared18-game opening stress test, fortress34 with round1_poke=3 wins375:-65 in round11 against the selector and bait, but loses-180:738 in round9 to the guard arm. Economy21 with r1_units=3 similarly beats selector and bait515:-1 in round7, but loses-600:723 in round9 to guards. V18FT with r1_poke=2 loses to all three: selector/guards520:770 in round50, bait-325:675 in round9. Six selector-to-selected-arm complete-history comparisons agree. All games pass strict accounting and original-engine replay (known1.083448 seconds; stress7.778737 seconds); seven and nine assignment pairs, respectively, have identical histories.
Verdict: CONFIRMED as an in-sample public-state counter to the seven declared policies; REFUTED as a robust policy identifier under these small opening changes. Receipts: experiments/validation/analysis/public_opening_selector/verification/{components,known_games,stress}.json. This is a concrete example of fitted adaptation and its limitation, not a held-out victory. Importable opponent: bot_research.bots.counters.public_opening_selector:@make.

## 2026-10-31T12:54Z: passive-until-five repairs roster bait but does not repair the two-guard loss

Claim: the proposed P5 exemption also removes the staged-guard vulnerability.
Method: the exact fixed development entry bot_research.experiments.lead.v24:@make?passive_until=5 faces the public selector, its bait and staged-guard arms, and the fixed heavy-drip schedule, both assignments. Eight games, strict accounting, complete source/data archive and unchanged-engine replay pass (4.445001 seconds); all four assignment pairs are identical. Compare all eight histories against the actual V18FT controls, with specification differences explicit.
Result: P5 wins515:-45 in round11 against selector and bait, with the first changed actions in round3. P5 still loses520:755 in round50 to staged guards and wins375:-1348 in round35 against heavy drip. The staged-guard and heavy-drip histories are exactly unchanged from V18FT in both assignments. Thus P5 scores6W2L in this selected transfer table. In the guard game its HP falls to660 in round7 and520 in round8, while the grower retains755; neither loses HP again through round50.
Verdict: REFUTED for the stated broader repair; CONFIRMED for this specific one-tier1 bait repair. For the lead: this is the exact proposed P5 default, not a variant inferred from the old family. It retains the two-guard loss even though the public selector happens to choose its losing bait arm against P5's three-tier1 opening. Receipt: experiments/validation/analysis/public_opening_selector/verification/passive_transfer.json. These are development tests only. PoolC is still unused. Next test will cross the40-gold roster-cost exemption, with thresholds and opponents declared before execution.

## 2026-10-31T12:57Z: storage maintenance preserves incomplete timeout evidence

Claim: the two original pool-A mirror timeout attempts remain reproducible evidence after storage reduction.
Method: archive_failed_partials.py compressed only the incomplete standard-07-side0/side1 logs from final-best-v9a-poolA-001, verified decompressed SHA-256 and byte length against each original, wrote a receipt, and then removed the uncompressed duplicate bytes. Both timeout failure records, original job declarations, successful500-second retries, selected results and valid replays were left unchanged.
Result: exact decompression checks pass;68,732,232 bytes saved. Receipt: runs/validation/failed-partials-archive-001.json. The original partial logs are now at the same relative names with .gz appended; decompressing restores their exact original bytes. No timed-out attempt was converted into a completed result or omitted from accounting.
Verdict: CONFIRMED for the recorded byte-preservation checks. This is storage maintenance, not another game or additional strength evidence.

## 2026-10-31T13:02Z: the45-gold bait crosses P5's exemption and retains a full-game counter

Claim: the40-gold passive-roster exemption prevents all previously identified grower-style insurance failures.
Method: predeclared passive-cost-grid-001.json uses the empty map, growth through5/6/7, and six round2 bait lists costing40/45/55/60/80/90, against V18FT and exact P5, both assignments:72 games. Every game passes strict accounting and original-engine replay (10.996880 seconds); all36 assignment pairs have identical complete histories. Six repeated V18FT tier2 controls match the earlier maze-grid histories. A separate check reconstructs every P5 observation through round6 and reevaluates the actual predicate; all36 cases pass in2.482378 seconds. The theorem in proof53 establishes that45 gold, three tier1 copies, is the cheapest allowed list strictly above40.
Result: V18FT28W8L; P5 30W6L. P5's three losses, each in both seats, are growth5/three tier1 (-195:665, round9), growth5/four tier1 (-200:650, round9), and growth7/four tier1 (-60:640, round9). Every one of the30 P5 histories above the40-gold boundary is exactly equal to its V18FT control. Only the three tier2-only settings change: growth5 is repaired from-332:640 in round9 to648:-455 in round12; growth6 improves from368:-260 in round13 to788:-75 in round10; growth7 improves from228:-300 in round13 to788:-75 in round10.
Verdict: REFUTED as a general repair. The exemption repairs the40-gold bait and leaves these more expensive baits completely unchanged. Receipt: experiments/validation/analysis/passive_cost_threshold/verification/cost_grid.json. Exact new opponent for the cheapest bypass: `bot_research.bots.counters.maze_grower:@make?layout="empty"&growth_rounds=5&bait=["tier1","tier1","tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000`. The108-game ablation now in progress tests thresholds45/60 and the lead's turret-only relevance P5T on every one of the original18 cost/growth settings. No poolC use.

## 2026-10-31T13:05:48.195810+00:00: P5 cost-threshold ablations and the completed nearby guard grid

Claim: raising P5's bait exemption, or dropping roster-only relevance, repairs the small-roster grower failures. Method: exact v24 P5, with one parameter changed at a time, on all 18 original growth/cost conditions in both assignments. The outcome-informed declaration is `experiments/validation/analysis/passive_cost_threshold/ABLATION_HYPOTHESIS.md`; these are development games, not reserve C.

Result: P5 had 30W-6L of 36. P5 with passive_bait=45 has 32W-4L, repairing growth5 with three round2 tier1 (now 645:-25 in round11), but still losing growth5 and growth7 with four tier1. With passive_bait=60 it has 36W-0L; with poke_reactive="turret_only" it also has 36W-0L. Those two repairs take different trajectories, so they are not interchangeable policies. Of the 108 intervention/control comparisons, 54 complete histories are identical. All 108 games passed strict accounting and unchanged-engine replay (15.4643813283 seconds for replay), with 54 identical assignment pairs and no rejected actions or bot errors. Evidence: `runs/validation/passive-cost-ablation-001/`, `passive-cost-ablation-comparisons-001.json`, `passive-cost-ablation-data-001.json`, and proof53 `verification/ablation.json`. Verdict: CONFIRMED on this grid; robustness to other opponents is OPEN.

Claim: the previously observed staged-guard loss is reproducible but not typical of all nearby timings. Method: P5 on growth5/6/7/8 crossed with two splash guards in rounds [3,5], [4,6], [5,7], empty maze, no bait, then all-gold tier5, both assignments. Result: 22W-2L of 24. The sole losing pair remains growth6, guards[4,6], final 520:755 at round50. The repeated pair is identical in its complete history to the earlier guard-transfer game. All games passed strict accounting and unchanged-engine replay (23.9659012877 seconds); all12 assignment pairs agree. Evidence: `runs/validation/passive-guard-grid-001/`, `passive-guard-repeats-001.json`, `passive-guard-data-001.json`, and proof53 `verification/guard_grid.json`. Verdict: CONFIRMED.

For the lead: the P5 staged-guard loss is a separate failure from its 40-gold bait boundary. The no-bait guard opponent has no post-round1 entry visible through round5 and thereafter buys only tier5. In v24, passive_bait is read only in _passive and the difference between turret and turret_only in _reactive concerns only cheap post-round1 entries. Thus all nonnegative bait thresholds and both these relevance settings are equivalent on that guarded-heavy trajectory. The standalone induction is proof54 (`analysis/passive_guard_equivalence/PROOF.md`); a fresh-policy shadow check in both assignments is running. This implication is source based and conditional on deterministic planning; do not count the shadow variants as new independent games. A trace of the validated baseline shows the round6 two-tier2 attack, then no later attack purchases, own S=1200 from round10 through50, and 498036 unspent gold at termination. The causal role of that early failed attack and fortress_guns is the next focused check.

I read the lead's 13:04Z status (R5/B100 development) and W1's 13:00Z complementary v34/v35 results. No reserve-C condition has been used. The guard-equivalence statement currently names v24 only; it must be checked against any new implementation before transfer.

## 2026-10-31T13:09:30.847771+00:00: the no-bait guard is immune to bait-threshold repairs; sticky adaptation confirmed

Claim: on the recorded staged-guard and fixed-heavy-drip histories, changing v24 P5's passive_bait to0,60,1000000000 or changing poke_reactive to "turret_only" changes no action. Method: four fresh policies per history, fed every public observation reconstructed by the original engine; input mutation forbidden, complete submitted lists and engine records compared. Result: all680 shadow decisions matched across four baseline histories (both seats, 50-round guard losses and35-round heavy-drip wins). Runtime429.7545961500 seconds. The sixteen policy instances reuse four trajectories and are not sixteen independent strength samples. Proof54 and `runs/validation/passive-guard-equivalence-001.json`, with `analysis/passive_guard_equivalence/verification/components.json`, hold the source pins and evidence. Verdict: CONFIRMED; the proof extends the bait-threshold comparison to every nonnegative integer under its explicit roster hypotheses.

Claim: one failed early attack explains why P5 stops attacking the two-guard grower. Method: fresh P5 instances on both original-engine histories; record private adaptation fields only for offline diagnosis, and query the current-map attack with the same post-defense budget without changing play. Result: the round6 two-tier2 purchase predicts24 damage; the round6 second splash guard raises the opponent's pure-splash exposure from50 to80 and prevents that damage. At round7 the failure count rises from0 to1. It stays1, the own map never reaches S=1500, and every actual attack purchase in rounds7..50 is empty. The current-map query would purchase attackers in later rounds. Runtime89.7349413922 seconds; every actual action and original-engine transition agrees. Proof55 (`analysis/sticky_attack_failure/PROOF.md`) states the sticky-mode program property, and its `verification/components.json` links the full diagnostic `runs/validation/sticky-attack-diagnostic-001.json`. Verdict: CONFIRMED for the mechanism; the full-game effects of fortress_guns=false, fail_limit=2 and attack_mode="current" remain OPEN while their 24-game paired ablation runs.

The old best_v9b win does not rely on reaching splash immunity: it buys splashes in round6, never makes that failed tier2 purchase, and buys tier3 in rounds9..12 while its S is only1300. P5 instead ends with S1200 and498036 gold. This correction matters when explaining the complementarity of the two defensive plans.

## 2026-10-31T13:14Z: failure-limit repair confirmed on three fixed opponents; counter cycle continues

Claim: the staged-guard loss is repairable by changing the permanent conservative-mode trigger, but removing fortress guns has a known regression. Method: 24 complete unchanged-engine games from `experiments/validation/sticky-attack-ablation-001.json`, P5, P5 with fortress_guns=false, P5 with fail_limit=2, and P5 with attack_mode=current, against the same three opponents, both assignments. Exact v24 source SHA cbe8dc5bb01925ac9d830e04dbf9edf887b064e0f582e5ec3a81b8080663bb62. No reserved conditions.

Results, candidate HP first; both assignments agree:

| Setting | Fixed heavy drip | Empty grower, guards R4/R6 | Forecast tier5 R8 |
| --- | --- | --- | --- |
| P5 | W 375:-1348 R35 | L 520:755 R50 | W 800:785 R50 |
| P5, no fortress guns | W 375:-1348 R35 | W 520:-25 R12 | L 660:785 R50 |
| P5, fail_limit=2 | W 375:-348 R16 | W 520:-233 R13 | W 800:785 R50 |
| P5, current attacks | W 375:-348 R16 | W 520:-233 R13 | W 800:785 R50 |

Verdict CONFIRMED for these conditions, OPEN for broader robustness. The conservative-mode repair wins all six games, while disabling guns trades one loss for another. Six of 18 matched intervention histories are fully identical; four P5 guard/heavy repeats match the earlier campaign exactly. Strict accounting, 24 original-engine replays (12.540438633877784 seconds), and 65 archived input hashes passed. Evidence: `runs/validation/sticky-attack-ablation-{strict,replay,summary,comparisons,repeats,data}-001.json`; standalone argument and verification receipt in `experiments/validation/analysis/sticky_attack_failure/`.

Next counter already declared: retain guards R4/R6, then raise pure-splash exposure from80 to200 with three more guards at R8, R9 or R10. This may stop the second predicted tier3 attack and exhaust fail_limit=2. The five exact guard cells and paths are in `bots/counters/data/guard_ladder_001.json`; 50 original combats and six eleven-round scheduled constructions passed in 0.9829315380193293 seconds. Twelve full games against fail_limit=2 and current mode are running; no strength result is claimed yet. This is a development counter cycle, not independent validation.

Lead's 13:09 freeze acknowledged: best_v9e is live, SHA 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Pool C stays untouched as requested. R5/R5D/B100 transfer checks of the existing guard loss are running separately; the empty early roster makes their passive predicates equivalent to P5 on this trajectory.

## 2026-10-31T13:16Z: R5, R5D and B100 preserve the staged-guard loss exactly

Claim: changing the passive bait threshold, making it factory-relative, or skipping mandatory defense only while passive cannot fix the no-bait staged-guard loss in the exact v25 implementation. Method: the source-level argument is in `experiments/validation/analysis/passive_ratio_guard_equivalence/PROOF.md`; six complete games use the proposed R5, R5D and B100 strings, both assignments, and compare every normalized record with the earlier P5 game. v25 SHA c537929614f94b2d1fad9ae515fcf2c8b2288b37f738945486702112d8023cee.

Result: all three lose 520:755 at round50; all six full histories equal P5. Strict accounting, original replays (10.055222069844604 seconds), and 57 archived input hashes passed. Verdict CONFIRMED under the proof's empty-early-roster hypotheses. This is one existing opponent with six implementation-transfer checks, not six independent strength samples. Evidence: `runs/validation/ratio-guard-transfer-{strict,replay,summary,equivalence,data}-001.json`; receipt in the proof's `verification/full_games.json`.

The lead's early-strike suggestion is also under test: exact frozen best9e, P5 and R5 face empty-layout, no-bait growers with growth through rounds2,3,4, followed by tier2,3,4,5 waves. The 72 conditions were declared before launch in `experiments/validation/early-passive-strikes-001.json`; the strategic hypothesis is in `analysis/maze_growth/EARLY_STRIKE_HYPOTHESIS.md`. No reserve pool is involved.

## 2026-10-31T13:17:39Z: the pure-splash second-failure counter does not win

Claim: raising the guard exposure from80 to200 at R8, R9 or R10 defeats the fail_limit=2 repair. Verdict REFUTED for these declared conditions. All six fail_limit=2 games and all six current-mode games won for P5. Candidate-first HPs, identical in both seats: upgrade R8, both 660:-25 at R13; R9, fail_limit=2 520:-2885 at R21 versus current 520:-505 at R14; R10, fail_limit=2 520:-2911 at R21 versus current 520:-471 at R14. The late upgrade visibly stops the one-tier3 purchase at R9 or R10, but it also makes tier3 permanently unattractive on the current map and changes later attack selection. That mechanism still needs the private-state diagnostic; it is not inferred merely from the eventual win.

Evidence: `runs/validation/guard-ladder-{strict,replay,summary,data}-001.json`, 12 original replays in 3.1094021280296147 seconds, all 57 archived inputs intact. Twelve matched opponent interventions change their complete histories; the R8 current/fail_limit pair agrees completely in both assignments, whereas R9/R10 differ. See `guard-ladder-{opponents,candidates}-comparisons-001.json` and the receipt in `analysis/guard_ladder/verification/full_games.json`. This negative result is retained.

Source-wording correction: proof55's earlier text called the robust attack score incremental damage. In v24 the current-map ranking is incremental, but `_leak_after_response` returns total post-response damage of the active roster plus the proposed purchase. The corrected standalone proof and amended receipt preserve the initial files in verification/. The permanent-mode property and the original diagnostic do not change. A possible next counter uses a few single-target guns to stop a small attack without removing that tier from large-roster current-map rankings.

## 2026-10-31T13:25:02.874849+00:00: complete-roster screening matters in the second-failure counter

Claim: the pure-splash ladder causes a second failed prediction but does not permanently stop P5 with fail_limit=2. Method: four fresh policy shadows on the R9/R10 ladder histories, both assignments; every actual decision, original-engine record and final result matches. The diagnostic additionally queries current rankings and response scores without modifying policy state. Result: failure count reaches2 in R10 for the R9 upgrade and R11 for the R10 upgrade; S stays1200. In R20 only tier4 and tier5 qualify in the current ranking, and both response scores are zero. In R21 tier5's response score becomes positive, 3640 for26 copies, and that purchase wins immediately. Verdict CONFIRMED. The reason for the changed hypothetical defense at that budget has not been isolated. Evidence: `runs/validation/guard-ladder-diagnostic-001.json` (59.75355649460107 seconds), proof57 `verification/diagnostic.json`. These shadows reuse four games.

Claim: a porous gun guard can stop the second small attack while leaving tier3 attractive at large budgets. The first homogeneous-roster search found two gun1 at(2,0),(9,3), added to splashes(10,1),(1,0), for60 gold. It kills one isolated tier3 and allows59 of60 tier3 through. But full games refute its intended effect: all eight P5TF/current games, upgradesR9/R10 and both assignments, are candidate wins520:-233 atR13. All four matched P5TF/current histories are identical. The earlier three tier1 and two tier2 screen the new tier3 from the guns; failure count stays1. Four fresh shadows match every actual action and original-engine record (8.717515935190022 seconds). Verdict REFUTED for this guard's full-game hypothesis; CONFIRMED for the finite homogeneous-roster component only. Evidence: `mixed-guard-001/`, `mixed-guard-{strict,replay,summary,equivalence,data,diagnostic}-001.json`, proof58 receipts. All eight original replays passed in1.448246612 seconds;59 archived inputs are intact.

The correction is predeclared in proof59, `analysis/screened_guard_ladder/PROOF.md`: search with the full prefix of three tier1 and two tier2. The finite search finds gun1 at(10,3),(10,4), still60 gold, which kills all six entries when one tier3 is appended, but permits59 of60 appended tier3 through. Tier3 ranks above tier4 and tier5 by incremental damage per new cost for the60-copy tests. The prefix alone causes zero damage. The exact JSON input is `bots/counters/data/screened_guard_001.json`, SHA c0980d0c46cf813f82d3eae5e26e18fab2d74f8135a87d4ad550eddc804ffde6. Thirty-one original combats and four eleven-round construction executions pass (0.5362706468440592 seconds). Eight full games against exactP5TF/current, upgradesR9/R10, are now running; their outcome remains OPEN. No reserve pool is used.

## 2026-10-31T13:25:02.874849+00:00: early waves do not defeat the passive exemption in the declared small grid

Claim: moving the unguarded wave earlier defeats P5 or R5 before their insurance starts. Method:72 predeclared complete games: empty-map, no-bait growth throughR2/R3/R4, then all-gold tier2/tier3/tier4/tier5, versus frozenbest9e, exactP5 and exactR5, both assignments. Result:all72 are candidate wins. All36 assignment pairs agree completely. Strict accounting, original-engine replays (5.371653203852475 seconds), and57 archived inputs pass. Of48 matched revised-policy/best9e histories,20 agree completely. Verdict REFUTED for these12 opponent settings. This does not prove the exemption costless: growth4/tier2 reduces the revised candidates to656HP versus800 forbest9e; growth4/tier3 to696 versus800; growth4/tier4 to740 versus800. The opponent nevertheless dies in each case. Exact rows are in `runs/validation/early-passive-strikes-summary-001.md`, with comparisons and proof48 `verification/early_strikes.json`. Other timed, defended or mixed strikes remain OPEN.

## 2026-10-31T13:26:54.655045+00:00: P5TF counter found, complete original-engine evidence

Claim: the round9 screen-aware guard defeats exact P5TF despite fail_limit=2. Verdict CONFIRMED for this fixed opponent and the standard start. P5TF loses520:755 at round50 in both assignments. Changing only attack_mode to current wins520:-103 at round13. Moving the same opponent's gun upgrade to round10 makes both policies win520:-129 at round13. The full eight-game campaign passes strict checks, every unchanged-engine replay (4.035006674937904 seconds), and all59 archived input hashes. All four assignment pairs are identical; two of four matched P5TF/current histories are identical. These are development conditions, not reserveC.

For the lead, exact counter specification: `bot_research.bots.counters.screened_guard_maze:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&upgrade_round=9`. It uses the original two splash guards at rounds4/6, and buys gun1 at(10,3),(10,4) in round9. The old guard metadata and new screened JSON are pinned by the bot. Candidate specification: `bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2`, exact v24 SHA cbe8dc5bb01925ac9d830e04dbf9edf887b064e0f582e5ec3a81b8080663bb62.

Evidence: `runs/validation/screened-guard-001/`, `screened-guard-{strict,replay,summary,comparisons,data}-001.json`, and proof59 `verification/full_games.json`. The first postprocessing attempt used an equality-only repeat checker and correctly rejected the changed R9 pair; the descriptive intervention checker above is the appropriate replacement. No games or sources changed. Private-state confirmation is still running, so the claim here is the complete-game counter and one-parameter repair, not yet the entire proposed ranking mechanism. A72-game nearby grid over growth5/6/7, upgrade8/9/10/11, and P5TF/current/fail_limit=3 is declared and running. Pool C remains untouched.

## 2026-10-31T13:28:53.850688+00:00: the two-entry response shortlist explains the new stalled attack

Claim: the screen-aware guard triggers the permanent robust branch and then suppresses an attack which that branch's own response heuristic would accept. Method: two fresh exact P5TF shadows, full50-round original-engine replays, private-state traces, and extra pure queries of every current-map candidate. Runtime95.76310411468148 seconds. All actual actions, original records, source hashes and outcomes agree.

Result: R6 buys two tier2 with prediction24; R7 records failure1. R9 buys one tier3 with prediction26; R10 records failure2. There are no more actual attack purchases throughR50, and own S stays1200 fromR11. In R20 the current order is tier3,tier4,tier5, with respective response scores0,0,3080. The tier5 purchase is22 copies, response ratio0.2153846 greater than the configured0.1 threshold, but is third and excluded by cands[:2]. At R21 it is26 copies with score3640 and remains excluded; atR30 it is60 copies with score8400 and remains excluded. AtR50 even that diagnostic response score is zero, so the claim is a missed earlier opportunity, not a permanently positive third score.

Verdict CONFIRMED for this exact recorded trajectory and the candidate's heuristic. A predicted response score is not a universal legal-defense guarantee. Evidence: `runs/validation/screened-guard-diagnostic-001.json`, proof59 `verification/diagnostic.json`. Proof60, `analysis/response_candidate_truncation/PROOF.md`, gives the finite-list program property. An owned focused variant, `bots/counters/untruncated_response.py:@make`, removes only the two-entry response shortlist. Component and full-game comparisons are in preparation; no strength claim for that variant yet. This is a more targeted candidate repair than merely increasing fail_limit again.

## 2026-10-31T13:32:04.211392+00:00: nearby screen-aware grid and original-combat confirmation

Claim: the second-failure counter survives nearby growth and upgrade changes. Verdict REFUTED as a broad claim on this grid: of12 opponent settings, only growth6/upgrade9 beats P5TF, in both assignments. P5TF scores22W2L of24; current mode24W; fail_limit=3 also24W. The72-game grid crosses growth5/6/7 with upgrade8/9/10/11. All36 assignment pairs agree completely. Thirty-six of48 matched intervention histories agree completely, and all eight repeated controls agree with the original campaign. Strict accounting, all original-engine replays (16.590155497193336 seconds), and60 archived inputs pass. Evidence: `screened-guard-grid-{strict,replay,summary,comparisons,repeats,data}-001.json`; proof59 `verification/nearby_grid.json`. This is a narrow reproducible timing counter, not a pervasive win over P5TF.

Claim: evaluating every eligible tier recovers the missed attack under the exact response heuristic. Verdict CONFIRMED at round20 of both recorded losing histories. The original routine returns no attack; the untruncated routine returns22 tier5 with predicted3080 damage. Reconstructing the own and opponent states, applying all22 legal purchases and every legal hypothetical-response action, and running the original simulate_map returns exactly3080. Both replay prefixes match the original engine and every actual P5TF action. Runtime24.012662454042584 seconds. Evidence: `runs/validation/response-truncation-components-001.json`, proof60 `verification/components.json`. These are component checks of the heuristic response, not a guarantee against all legal responses. The36 full games against six fixed opponents are running on a separate core.

## 2026-10-31T13:36Z: early turret strikes declared; guard-handoff clock qualification

The lead's 13:32Z request is now a declared 144-game development grid in `experiments/validation/turret-early-strikes-001.json`: P5TF, P5TN and P5TNR against a round1 gun1 at(10,1) or(0,2), growth through rounds2,3,4,5, then pure tier3,tier4,tier5 waves, both assignments. Exact v26 SHA353ea07da058f40f62663c3a9e4777623bb713b45cc1061e1623507a03fff339. Results are OPEN. These are new early timing conditions, not reserveC.

Source qualification for the separate guard-handoff test: frozen v34 `replan.py` uses fixed iterations when no time budget is passed, as here, but `plan.py` still gives gun planning a three-second wall-clock budget and checks it both before candidate passes and inside the pass. Therefore the wrapper inherits a possible clock dependency. Verdict CONFIRMED for the source dependency, OPEN for whether it changes any of these recorded games. Paired histories and any repeated fresh decisions must be compared rather than presumed equal. Original-engine replay remains a check of the actual recorded submissions, not proof of deterministic future bot decisions.

## 2026-10-31T13:36:09Z: evaluating all eligible response candidates repairs the screened-guard loss

Claim: removing only the two-entry response shortlist repairs the recorded P5TF counter without a regression on the six declared opponents. Method:36 complete games comparing exactP5TF, current mode and `bot_research.bots.counters.untruncated_response:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2`, both assignments. Wrapper SHAfe456df08022acdaf461fb4b7e5d29c592a90edd5fd62b4e1eeca13879536db6. It retains the current-map eligibility filter, purchase counts, response heuristic, threshold and sorting; it response-tests every eligible tier instead of the first two.

Result: P5TF10W2L, current12W, untruncated12W. Against the screened R9 guard, untruncated wins520:-1345 atR16 in both assignments, versus P5TF's520:755 loss atR50 and current's520:-103 win atR13. Against heavy drip, the original staged guard, forecast tier5R8, the pure-splash R9 ladder, and screened R10, the untruncated complete histories equal P5TF. This is ten identical matched histories and two repaired histories. Across both interventions,18 of24 matched histories agree. All18 assignment pairs and all eight repeated controls agree completely. Strict checks,36 original-engine replays (14.427710058167577 seconds), and72 archived input hashes pass.

Verdict CONFIRMED for the stated six-opponent development matrix; broader superiority remains OPEN. Evidence: `response-truncation-{strict,replay,summary,comparisons,repeats,data}-001.json`, proof60 `verification/full_games.json`. The response scores are still heuristic defenses, not universal guarantees. A new counter that switches from the guard opening to a frozen defender is running separately, so this repair should not yet be treated as resolving all adaptation failures. No reserved pool is involved.

## 2026-10-31T13:39Z: round12 defensive handoff defeats the shortlist repair

Claim: extending the screened-guard opening with a timely defensive continuation can recover a win against the all-candidate response variant. Verdict CONFIRMED for the round12 continuation in these executions. The24-game campaign compares P5TF, current mode and untruncated response against handoffs at12,16,19,22, both assignments. All four handoffs beat P5TF520:755 atR50. Against untruncated response, H12 wins with the same score, while H16/H19/H22 lose520:-1345 atR16. Current mode wins against H12,520:-775 atR20, and against the later handoffs,520:-103 atR13. Candidate HP is listed first.

Exact opponent: `bot_research.bots.counters.guard_handoff:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&handoff_round=12&replan_iters=5000`. Before H it follows the screened opening. From H it calls one fresh frozenv34 defender configured with attack="none", round1_poke=0, and filters proposed actions through the original action function on its observed own-state reconstruction. It does not read either player's hidden current submission. The frozen defender's gun planning retains a wall-clock bound, as qualified above.

All12 assignment pairs agree completely in this execution. Two of16 matched candidate-intervention histories agree completely. Strict checks, all24 original-engine replays (13.337828743737191 seconds), and82 archived inputs pass. Evidence: `guard-handoff-{strict,replay,summary,comparisons,data}-001.json`; proof61 `verification/full_games.json`. Eight first-handoff component calls had unchanged inputs, legal output and zero internal rejected proposals; full-history fresh-controller checks are still pending. This is another development counter cycle, not a reserved validation result.

The lead's 13:37Z v27 robust_k=null implementation is now being shadowed on all12 completed untruncated-response histories. The owned wrapper changes only the response shortlist. The source comparison also accounts for v27's newer passive options, which retain their defaults in P5TFU. Full action equality remains OPEN until that check completes. A24-game transfer of the guarded counters to v26 P5TN/P5TNR/current is also running.

## 2026-10-31T13:40:48Z: early turret sweep supports P5TN on the declared grid

Claim: ignoring early defensive turrets in the passive predicate introduces a loss to the tested early waves. Verdict REFUTED on this grid. All144 declared games are complete: P5TF46W2L, P5TN48W, P5TNR48W. The only losses are P5TF against round1 gun1(10,1), growth throughR4, then tier5 waves: -40:715 atR11, both assignments. P5TN and P5TNR win the same condition800:0 atR10. The grid also includes gun1(0,2), growth throughR2/R3/R5, and pure tier3/tier4 waves.

All72 assignment pairs agree completely. P5TN and P5TNR have identical full histories in all48 matched conditions. Each differs from P5TF in its full history, so equality of W/L outcomes elsewhere should not be mistaken for action equality. Strict checks,144 original-engine replays (13.528138902969658 seconds), and56 archived inputs pass. Exact rows are in `runs/validation/turret-early-strikes-summary-001.md`; evidence also includes `turret-early-strikes-{strict,replay,comparisons,ratio-comparisons,data}-001.json` and `analysis/feature_bluff/verification/early_turret_strikes.json`. A general archive checker is used because this controller has no coefficient or layout JSON input.

Scope correction retained alongside the predeclared hypothesis: the old feature-bluff proof concerns a gun at(0,11), not either tested cell. Neither new cell is assumed to have zero combat effect. The separate `EARLY_TURRET_CLARIFICATION.md` gives the controller's general action-legality argument without extending the old geometry claim. No reserved conditions were used.

## 2026-10-31T13:43:01.079787+00:00 Integrity and resource checkpoint

Claim: the protected project is unchanged from the recorded starting state. Method: hash every file and symlink outside bot_research, including the pre-existing virtual environment, and compare against integrity-start.json. Result: 903 entries; baseline differences {'added': [], 'changed': [], 'removed': []}; 1002 original missing manifest entries and the same three original hash mismatches. Verdict: CONFIRMED if all three baseline difference lists are empty. No protected file was repaired. Owned artifact scan checks 26624 text files and reports 0 absolute-local-path violations. Total owned project and lane bytes: 2786182356; free filesystem bytes: 95674716160. Artifacts: runs/validation/integrity-mid-1341.json and artifacts-mid-1341.json.

## 2026-10-31T13:43:11.034827+00:00 v27 all-candidate equivalence and handoff history checks

Claim: the lead's P5TFU implements the same shortlist removal as our P5TFullResponse, under the stated common parameters and equal shared-planner results. Method: compare shared defaults and unchanged helper/method ASTs, then instantiate v27 P5TFU freshly on all 12 complete FullResponse histories from response-truncation-001. Result: all 258 returned action lists were identical, inputs stayed unchanged, and every original transition and outcome replayed exactly. The v27 source SHA256 is 1f0402bfa6a750cbe3a65cdb2103bf59fa55381a0a69d735fb3d446ae5b8e83f. The new wrapper changes only robust candidate truncation; v27's extra passive options are at their original-behavior values in P5TFU. Verdict: CONFIRMED for these histories; the general equivalence argument is conditional on equal planner outputs and is in analysis/response_candidate_truncation/v27_equivalence/PROOF.md. These are reused development histories, not new strength samples. Evidence: runs/validation/v27-untruncated-equivalence-002.json, with its source/hash receipt beside the proof. The initial checker failed before games because it expected __call__ as the edited method instead of _decide; the initial checker, argument and sanitized failure log are retained. Only this checker assertion and the corresponding proof method name were corrected.

Claim: the observed H12 counter result is compatible with legal, observation-only fresh decisions. Method: freshly shadow the handoff opponent on the four complete P5TF/FullResponse H12 histories, while replaying recorded actions through the original engine. Result: all 200 opponent decisions matched, all fresh actions were legal, inputs stayed unchanged, no internal actions were rejected, and no attacks were purchased after handoff. Verdict: CONFIRMED on these four histories. This does not eliminate the underlying F34 gun-planner wall-clock cutoff. Evidence: runs/validation/guard-handoff-histories-001.json and analysis/guard_handoff/verification/full_history_shadows.json.

Next development test, already running: P5TFU and P5TNU against handoffs H10 through H16, both assignments, 28 conditions. The H12 observation informed this grid. Pool C remains unused and deferred.

## 2026-10-31T13:45:40.814618+00:00 v26 transfer outcome and replay storage

Claim: ignoring an early opponent turret, with or without the factory-relative passive threshold, removes the screened guarded-growth failure. Method: 24 development games, four disclosed opponents (original staged guards R4/R6 at growth6; screened growth6 R9; guard handoffs H12 and H16), P5TN/P5TNR/P5TNcurrent, both assignments. Result: P5TN and P5TNR each 2W6L. The original staged guard is beaten 660:-207 at round12; all three other opponents win 660:755 at round50. All eight P5TN/P5TNR complete histories are identical. P5TNcurrent wins all eight: original staged 660:-207 R12, screened 660:-103 R12, H12 660:391 R50, H16 660:-103 R12. Verdict: REFUTED. The turret-passivity revision improves the losing HP from the earlier 520 to 660 but does not repair this guarded failure. These HP comparisons are cross-version development observations, not an isolated single-decision intervention.

All 24 original-engine replays pass (17.568189 seconds); all 12 assignment pairs match after normalization. No rejected action, bot error, unresolved condition or source drift. The 16 matched parameter comparisons have ten identical histories: eight P5TNR/P5TN and two current/P5TN against the original staged guard. All 72 archived inputs including five JSON data files pass. Evidence: runs/validation/v26-guard-transfer-summary-001.json, its strict/replay/comparisons/data companion files, and analysis/screened_guard_ladder/verification/v26_transfer.json. Candidate v26 SHA256 is 353ea07da058f40f62663c3a9e4777623bb713b45cc1061e1623507a03fff339; exact specifications are in experiments/validation/v26-guard-transfer-001.json. Handoff planning retains its clock cutoff, so these are execution-specific observations.

Storage change: compressed the 60 completed pool A replay JSONL files losslessly, saving 450,358,229 bytes. Each decompressed SHA256 was checked against the original before removal. Original result records and source receipts are unchanged; the original replay paths can be restored with experiments/validation/restore_archived_replay.py. A restore/hash/remove check passed. See experiments/validation/ARCHIVED_REPLAYS.md and runs/validation/archived-poolA-replays-001.json for paths and both hashes. Existing readers that require uncompressed JSONL need this restoration step. This operation changes storage, not any outcome or independent evidence count.

## 2026-10-31T13:47:10.178094+00:00 Reproduction commands for the current development batch

All paths below are project-relative. Use a fresh output directory rather than overwriting the preserved campaign. Environment and CPU convention:

```sh
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1
export TMPDIR="$PWD/bot_research/tmp"
nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/v26-guard-transfer-001.json --output-dir bot_research/runs/validation/v26-guard-transfer-reproduction --max-seconds 500 --match-timeout 300
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/v27-guard-timing-001.json --output-dir bot_research/runs/validation/v27-guard-timing-reproduction --max-seconds 500 --match-timeout 300
```

Repeat a command with `--resume` if its bounded batch ends before the declared conditions finish. The exact candidate and opponent specifications, data hashes and input source hashes are in the respective manifest. The same runner and environment apply to `response-truncation-001.json`, `guard-handoff-001.json` and `turret-early-strikes-001.json`, each with a distinct fresh output directory. Preserved pipeline logs list the strict-audit, original-engine-replay and summary commands used after each campaign. No reserved condition is included in this batch.

## 2026-10-31T13:47:41.446098+00:00 H12 remains a counter to P5TFU; diagnostic completed

Claim: removing the two-tier response shortlist suffices to beat the guarded H12 handoff. Method: complete standard-start games against v27 P5TFU in both assignments, then fresh candidate shadows and original-engine replay of both 50-round histories. Result: both are losses. The fresh shadows reproduce every candidate action and transition (27.912474 seconds including diagnostic queries). Verdict: REFUTED. This is a disclosed development counter, not a held-out finding; the full H10-H16 grid is still running.

The trace narrows the cause. P5TFU buys two tier2 at round6, predicts24, and records failure1 at round7. It buys one tier3 at round9, predicts26, and records failure2 at round10. At round12 its attack budget is778: current-map candidates are seven tier3 (increment182), two tier4 (increment120), and one tier5 (increment140), but all three modeled response damages are0. At sampled rounds13,14,15,16,20,21,30,50 no tier meets the current-map eligibility threshold. No attack is actually purchased from round10 through round50. Its own splash score reaches1560 and the immunity override is active by sampled round20, after the opportunity for these purchases has passed. This last observation matters: the late inactivity is not solely the permanent failure counter, because current-mode scoring also has no eligible purchase at those sampled states. The complete handoff and attack timing, not only shortlist length, needs consideration.

Evidence: runs/validation/v27-handoff-diagnostic-001.json and analysis/guard_handoff/verification/v27_h12_diagnostic.json. Exact command, under the standard environment: `nice -n 19 taskset -c 29 .venv/bin/python -B -m bot_research.experiments.validation.diagnose_v27_attack_sequence --campaign bot_research/runs/validation/v27-guard-timing-001 --candidate-id P5TFU --opponent-ids guard_handoff_r12 --output bot_research/runs/validation/v27-handoff-diagnostic-001.json`. Reproduce with a new output filename. Scores are diagnostics of this policy's model, not proofs about every possible defense or attack.

## 2026-10-31T13:50:20.471509+00:00 Integrity and resource checkpoint

Claim: the protected project is unchanged from the recorded starting state. Method: hash every file and symlink outside bot_research, including the pre-existing virtual environment, and compare against integrity-start.json. Result: 903 entries; baseline differences {'added': [], 'changed': [], 'removed': []}; 1002 original missing manifest entries and the same three original hash mismatches. Verdict: CONFIRMED if all three baseline difference lists are empty. No protected file was repaired. Owned artifact scan checks 26852 text files and reports 0 absolute-local-path violations. Total owned project and lane bytes: 2354848741; free filesystem bytes: 93098336256. Artifacts: runs/validation/integrity-mid-1348.json and artifacts-mid-1348.json.

## 2026-10-31T13:53:25.436506+00:00 Completed handoff timing grid and failure-threshold ablation

Claim: v27's all-candidate response search, with the revised passive opening, removes the guarded handoff counter. Method: P5TFU and P5TNU against handoffs H10 through H16 inclusive, standard start, both assignments,28 complete development games. P5TFU is `bot_research.experiments.lead.v27:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&robust_k=null`; P5TNU adds `&passive_turret=false`. Source SHA256 1f0402bfa6a750cbe3a65cdb2103bf59fa55381a0a69d735fb3d446ae5b8e83f. Exact counter specification: `bot_research.bots.counters.guard_handoff:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&handoff_round=H&replan_iters=5000`.

Result, identical normalized histories in both assignments:

| Candidate | H10 | H11 | H12 | H13 | H14 | H15 | H16 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P5TFU | L520:755 R50 | L520:755 R50 | L520:755 R50 | L520:755 R50 | L520:755 R50 | W520:195 R50 | W520:-1345 R16 |
| P5TNU | L660:755 R50 | L660:755 R50 | L660:755 R50 | L660:755 R50 | W660:55 R50 | W660:-1205 R15 | W660:-1345 R15 |

Thus P5TFU is4W10L and P5TNU6W8L. Verdict: REFUTED; the revised opening shifts the boundary but leaves H10-H13 as counters. All28 original replays pass (21.043512 seconds), all14 assignment pairs match, all72 archived inputs pass, and no bot errors, rejected actions or unresolved conditions occurred. The four FullResponse/v27 P5TFU control comparisons at H12/H16 also have identical complete trajectories. All14 P5TFU/P5TNU intervention histories differ. These are observed executions with the opponent's clock-limited planner, not an assertion that the policy is deterministic. Evidence: runs/validation/v27-guard-timing-summary-001.json and strict/replay/comparisons/data companion files; analysis/guard_handoff/verification/v27_timing.json.

Claim: allowing one or two more failed attacks can repair H12 by acting before the defensive handoff. Method: same P5TNU parameters except fail_limit=3 or4, against H10,H12,H14,H16, both assignments,16 additional development games. Result: each threshold gives6W2L: H10L660:755 R50; H12W660:391 R50; H14/H16W660:-103 R12. Verdict: CONFIRMED for H12, REFUTED as a repair of the whole tested family because H10 still wins. All16 original replays pass (7.670347 seconds), all8 assignment pairs match, all72 archived inputs pass. All16 full histories differ from the matched fail_limit=2 controls, including the H10 losses. Equal final outcomes for thresholds3and4 do not establish equal policies or histories. Evidence: runs/validation/v27-failure-limit-summary-001.json and strict/replay/comparisons/data companion files; analysis/guard_handoff/verification/v27_failure_limit.json.

The fresh fail_limit=3 H12 diagnostic replays both full histories with identical actions, transitions and unchanged input observations (29.941994 seconds). At round10 failure2 leaves current scoring enabled, so the bot buys four tier3 and deals104, reducing the opponent from755 to651. At round11 it buys six tier3; the accumulated roster deals260, reducing the opponent to391. Round12's nine-tier3 purchase is stopped by the handoff and failure3 is recorded at round13. The bot then preserves its660:391 lead to round50. Its final result equals the earlier P5TNcurrent H12 result, but these are different policy interventions. Raising the threshold has not been checked here against the other strong opponent families; no integration recommendation follows from this narrow ablation. Evidence: runs/validation/v27-fail3-h12-diagnostic-001.json and analysis/guard_handoff/verification/v27_fail3_h12_diagnostic.json.

Reproduction: use the runner command in the preceding reproduction entry with manifest `bot_research/experiments/validation/v27-failure-limit-001.json` and a new output directory. The diagnostic command is `nice -n 19 taskset -c 29 .venv/bin/python -B -m bot_research.experiments.validation.diagnose_v27_attack_sequence --campaign bot_research/runs/validation/v27-failure-limit-001 --candidate-id P5TNUF3 --opponent-ids guard_handoff_r12 --output bot_research/runs/validation/v27-fail3-h12-diagnostic-reproduction.json`, under the standard environment. Pool C remains unused.

## 2026-10-31T13:56:16.754195+00:00 Shift 2 closing checks and handoff

Claim: the protected project remains exactly at the recorded starting state. Method: repeat the complete inventory and hash comparison, including the pre-existing virtual environment, against integrity-start.json. Result: all 903 entries are unchanged, with no added or removed entries. The original 1002 missing manifest entries and three original hash mismatches remain the baseline, not repairs. Verdict: CONFIRMED. Evidence: runs/validation/integrity-shift2-end.json.

The existing test suite completed at 2026-10-31T13:52:16.262483+00:00: 59 tests run, 9 skipped, exit status0, elapsed command time 5.485604 seconds. Evidence: runs/validation/existing-tests-shift2-end.json and its log. The artifact scan at 2026-10-31T13:55:08.156747+00:00 found no absolute local paths in 26913 owned project text files. Owned project and lane files occupied 2362910158 bytes; filesystem free space was 91105226752 bytes. Evidence: runs/validation/artifacts-shift2-end.json. These are measured checkpoint sizes; this closing note adds a small amount of text afterward.

All declared development campaigns, postprocessors, diagnostics and checks from this shift have completed. The H10 counter remains unresolved for the tested fail_limit2,3,4 policies. An always-current attack ablation at H10 has not been tested here. Lead notes dated13:37Z still defer pool C, which remains unused. Next shift should first read the current assignments, then either run the requested frozen validation or extend the disclosed H10 development counter.

## 2026-10-31T13:58:21.749825+00:00 Shift 3: development H10 transfer declared

Latest lead assignment still defers pool C. Started 28 standard-start development conditions: H10/H12 handoff, both assignments, P5TNUcurrent, P5TNUF3 control, frozen F34, F35, E25RM, E27 and best_v9e. Claim: H10 still defeats always-current scoring. Verdict: OPEN pending the declared games and audits. Cross-family transfer is also OPEN. Declaration: experiments/validation/h10-transfer-001.json. No live-best dependency and no reserved condition are used.

## 2026-10-31T14:00:11.618264+00:00 Shift 3 starting integrity and storage

Claim: the protected files are unchanged since the recorded start. Method: complete inventory including the pre-existing virtual environment, compared with integrity-start.json. Result: 903 entries with no additions, removals or changed hashes; the known 1002 missing manifest entries and three original mismatches persist. Verdict: CONFIRMED. The owned-artifact scan found no absolute local paths in 26915 text files, counted 2363723960 owned bytes and 89468387328 free filesystem bytes. Evidence: runs/validation/integrity-shift3-start.json and artifacts-shift3-start.json.

## 2026-10-31T14:03:45.287811+00:00 H10 defeats always-current scoring; diagnostic complete

Claim: always-current scoring repairs the H10 handoff loss. Method: v27 P5TNUcurrent, standard start and both assignments, followed by fresh candidate shadows and original-engine replay of both complete50-round histories. Result: both lose660:755 at round50. At round10 the current rule buys four tier3, predicts104 damage, and the handoff stops that purchase; failure3 is counted at round11 but cannot change current-mode selection. No further attack is purchased. At sampled rounds11-16,20,21,30,50 the current-map ranking has no eligible tier; own splash immunity is reached at round29. Verdict: REFUTED. The failure is not solely the sticky failure threshold or the two-tier response shortlist. Evidence: runs/validation/h10-current-diagnostic-001.json, elapsed32.708044 seconds, all100 fresh candidate decisions and recorded transitions reproduced with unchanged observations. The 28-condition transfer campaign is still running and will receive its complete strict/data/replay audits. These are disclosed development conditions, not reserved validation.

## 2026-10-31T14:03:45.287811+00:00 Report review: do not reverse splash immunity

Claim: S<1500 by itself implies tier5 leakage on a fixed map. Method: source proof plus an explicitly funded original-engine component with five gun3 at (3..7,1), one active tier5, and no splashes; empty-map control. Result: S=0, potential isolated-copy damage1925, the tier5 is killed; the control takes140. Verdict: REFUTED. The 14:00 report snapshot line596 uses precisely this invalid converse. Suggested correction is to cite S<1500 as absence of the sufficient immunity certificate and cite the actual replay for leakage. Full proof and component evidence: analysis/splash_converse/; review: experiments/validation/reviews/report-1400-review.md. The review also corrects the literal no-randomness/no-cutoff claim for econ20: its replanner has a fixed pseudorandom seed, and its gun planner retains a finite1000000-second deadline. The latter was not reached in the reported calls. No report-owner source was edited.

## 2026-10-31T14:10:48.454883+00:00 H10 transfer and early-pressure interventions, complete

Claim: the H10 handoff defeats the current strong candidates in the declared standard-start conditions. Method: seven candidates against H10 and H12, both assignments, 28 full games. All rows below have the same outcome and final candidate:opponent HP in both seats.

| Candidate | H10 | H12 |
| --- | --- | --- |
| P5TNUcurrent | L 660:755 R50 | W 660:391 R50 |
| P5TNUF3 | L 660:755 R50 | W 660:391 R50 |
| F34 | L 100:753 R50 | W 100:-113 R16 |
| F35 | L 240:765 R50 | W 240:95 R50 |
| E25RM | L -40:618 R10 | L -460:618 R10 |
| E27 | L -40:618 R10 | L -460:618 R10 |
| best_v9e | L 520:755 R50 | L 520:755 R50 |

Verdict: CONFIRMED for this matrix, including frozen F34 and F35. All 28 original-engine replays and strict checks pass, as do 95 archived source/data inputs. All 14 assignment pairs have identical normalized complete histories. The four repeated P5TNUF3 controls equal the earlier histories. E27 equals E25RM in all four matched full histories. Always-current and fail_limit=3 have the same H10 histories, but their H12 actions first differ in round13, despite equal final HP. Evidence: runs/validation/h10-transfer-{strict,replay,summary,comparisons,data}-001.json and analysis/guard_handoff/verification/h10_transfer.json. Exact specifications and input hashes are in experiments/validation/h10-transfer-001.json. These are development conditions with the handoff defender's clock-limited gun planning. They are not independent statistical samples.

Claim: an earlier or larger attack repairs H10. Method: change one parameter of v27 P5TNUF3 at a time, against H10 and H12 in both seats (32 games).

| Changed parameter | H10 | H12 |
| --- | --- | --- |
| open_0.1 | L 660:755 R50 | W 660:443 R50 |
| open_0.25 | L 520:735 R50 | W 520:-1205 R21 |
| open_0.5 | L -320:715 R9 | L -320:715 R9 |
| attack_from_3 | L -320:699 R9 | L -320:699 R9 |
| attack_from_4 | L 240:719 R50 | L 240:659 R50 |
| attack_from_5 | L 520:707 R50 | W 520:-1217 R22 |
| attack_share_0.75 | L 660:729 R50 | W 660:287 R50 |
| attack_share_1.0 | L 520:729 R50 | W 520:365 R50 |

Verdict: REFUTED for all eight interventions. All H10 games are losses. All strict checks, 32 original-engine replays and 72 archived inputs pass. All 16 assignment pairs agree completely. None of the 32 histories equals its matched P5TNUF3 control, even where final HP agrees. Evidence: runs/validation/opening-pressure-{strict,replay,summary,comparisons,data}-001.json and analysis/guard_handoff/verification/opening_pressure.json. These results do not recommend an integration change; the more aggressive settings can weaken defense and economy. Pool C remains unused.

## 2026-10-31T14:10:48.454883+00:00 H10 defensive-spending diagnosis

Claim: permitting partial gun plans in the round8 state is enough to prevent H10's first hit. Method: replay the complete P5TNUcurrent H10 history while tracing its original planner calls, then reconstruct its round8 observation and compare ten local plan variants using the original combat engine. The first hit occurs in round8, not round7. The candidate has660HP against755 afterward.

The baseline replaces leaking splash plans with zero-leak gun plans costing540 in round6 and600 in round7. It has45 factories against86 at the end of round6, and50 against86 at the end of round7. At round8 its budget is813; the recorded partial plan costs784 and permits one of four tier5 to arrive, for140 damage. The no-action control permits two arrivals. Asking the same planner for a partial plan with guns, either against all eight sampled rosters or against only the actual four tier5, returns that same784-gold plan and one arrival. The corresponding zero-leak-only requests return no plan.

Verdict: REFUTED for these tested planner variants on this exact state. This is not a proof that no legal affordable defense exists. The actual roster is used only for a hindsight component comparison, not as policy input. All fresh candidate actions, unchanged observations and complete original-engine transitions reproduce; all ten local plans are checked by original combat. Evidence: runs/validation/h10-defense-diagnostic-001.json, h10-alternative-plans-001.json and analysis/guard_handoff/verification/h10_defense_components.json. A separate 40-game grid changes earlier defense/economy parameters and is still running.

## 2026-10-31T14:13:10.479890+00:00 Public-HP handoff declared against the new v28 candidate

Claim: a public-HP switch can preserve the guarded opening's wins while escaping some early-rush losses. Verdict: OPEN. The120-condition development declaration compares six counter rules against ten targets, both assignments. Fixed handoffs8/9/10 are controls; the other rules use a positive HP lead from round8, HP<=600 from round2, or both, each with a round12 deadline. Targets include v28 P5TNUB (SHA256 7d6da33a11bcb89b756c0c2ea892efe596768f0fac8e9e7c581ce93886ac266e), the six unchanged strong targets from h10-transfer except E27, and three early/basic opponents. The first-call legality/equality smoke check passes. Full-game results and fresh-policy history checks are pending. Exact specs: experiments/validation/hp-handoff-001.json; standalone legality/observation proof64: analysis/hp_handoff/PROOF.md.

The lead's14:05Z assignment is acknowledged. ReserveC remains untouched; capacity will be available for a frozen validation request around17:00Z. The H10 current-mode result above applies to v27's always-current policy; v28's behind-only override is being tested explicitly rather than presumed equivalent.

## 2026-10-31T14:14:23.243013+00:00 Team cross-check and timestamp caution

The defense lane's latest x128 table agrees with our independently replayed H10/H12 results for F34 and F35, including 100:753 and 240:765 losses at H10. Its displayed heading is14:40Z, although this note was read at 2026-10-31T14:14:23.243013+00:00 and the file mtime was14:12:22Z. The heading therefore cannot be used as an experiment completion time or runtime. Please use the underlying measured run timestamps in the final report. This timing discrepancy does not alter the matching HP outcomes. The broader x128 timing grid has not been independently replayed here.

## 2026-10-31T14:23:03.759857+00:00 Defense/economy interventions complete; H10 remains a loss

Claim: one of the ten declared defense/economy changes to P5TNUF3 repairs H10. Method: each change faces H10 and H12 in both assignments, 40 standard-start development games. Each table entry agrees across seats.

| Changed parameter | H10 | H12 |
| --- | --- | --- |
| passive_until_4 | L 520:755 R50 | W 520:-775 R20 |
| passive_until_6 | L 520:651 R50 | W 520:-51 R11 |
| passive_until_7 | L 100:469 R50 | W 100:-285 R11 |
| fortress_n_null | L 660:729 R50 | W 660:417 R50 |
| fortress_n_2 | L 660:755 R50 | W 660:391 R50 |
| fortress_n_8 | L 660:755 R50 | W 660:391 R50 |
| fortress_k_1 | L 660:755 R50 | W 660:391 R50 |
| big_partial_false | L 520:573 R50 | W 520:27 R50 |
| spec_share_0.8 | L 660:755 R50 | W 660:453 R50 |
| spec_share_1.0 | L 660:755 R50 | W 660:453 R50 |

Verdict: REFUTED for these ten interventions. This is not a proof that H10 cannot be defended. All40 strict checks and original-engine replays pass; all20 assignment pairs have equal normalized complete histories. The72 archived inputs pass. Twelve of40 matched histories equal their P5TNUF3 controls, exactly the fortress_n=2, fortress_n=8 and fortress_k=1 settings at both handoffs and seats. Replay audit elapsed22.375204 seconds. Evidence: runs/validation/h10-defense-spending-{strict,replay,summary,comparisons,data}-001.json and analysis/guard_handoff/verification/h10_defense_spending.json. The opponent contains a clock-limited planner; observed equality is not a universal determinism claim.

## 2026-10-31T14:23:03.759857+00:00 Reserved-scenario separation preflight, with explicit limits

Claim: the two reserved poolC scripted histories had already appeared among registered development scenarios. Method: reconstruct named scenarios only when their recorded generator/engine Python closure matches the reserved generator, check their prescribed actions with the original engine, and compare complete ordered histories under swapping both players. No candidate or opponent policy is called. Cutoff for this preflight is14:18:15Z. Result: 145 validation campaigns, 4236 registered jobs, 190 explicit or reconstructed validation prefixes, and9571 reconstructed team prefixes were compared, 9761 complete histories in all. No exact complete-history overlap was found. Verdict: REFUTED within the reconstructed records; OPEN for the eight unresolved historical failure rows and unlogged or unrecognized executions.

The eight unresolved rows are defense/x75_v26_foreign lines20-23 and defense/x78_surplus_misc lines7,9,10,11. Their error records lack source hashes and usable start times and report the known GuardContinuation constructor failure. They cannot certify an executed history. Shared scenario generators, common initial actions and equivalent resulting states are not excluded. Team historical source lists omit the balanced JSON inputs; current protected JSON hashes agree with the reserve declaration, but that does not create missing historical metadata. Result streams are captured snapshots and may later grow. The independent poolC wrapper skips the underlying policy during the prescribed prefix; the lead harness calls it through during that prefix. This protocol difference must accompany comparisons.

Evidence: runs/validation/late-scenario-separation-preflight-002.json and experiments/validation/audit_late_scenario_separation.py. The earlier001 artifact is retained; its extra110 unresolved named validation wrappers were handled in the revised checker. This is only a preflight and must be repeated at the actual frozen campaign start. PoolC remains unused.

## 2026-10-31T14:23:03.759857+00:00 Forecast-specific handoff counter declared

Claim: responding only to the predicted next roster can preserve a guarded opening's HP lead while inducing repeated failed current-map purchases. Verdict: OPEN. The new forecast_handoff counter uses a synchronized public P5TNUB clone from round1, then switches at round9 or10 to bounded free-cell defense and factories. It buys no new minions after that switch. Paired controls use only the currently visible roster while advancing the same clone. Six targets and both seats give48 development conditions. The four initial-call legality/observation checks, including an immediate switch, pass. Full games and prediction traces are pending.

The clone reads only copied public observations; it never reads the target instance or pending submission. Its v28 model has a clock-limited dependency, so exact forecast agreement is measured rather than presumed. The model remains P5TNUB for all six targets, including deliberately mismatched targets. Proof65 and design: analysis/forecast_handoff/. Declaration and frozen inputs: experiments/validation/forecast-handoff-001.json. Counter source SHA256 9bbd5045811173ead8cdb2fea0e83cfa92dc5381f88adfd67bfbbdab86c6cf4b.

## 2026-10-31T14:25:20.224389+00:00 Correction: standard v28 model path has no clock cutoff

Claim: a synchronized P5TNUB clone uses a clock-limited planner during a standard-start match against P5TNUB. Method: inspect Insurer.__call__, its requested-cell invariant and frozen/v7/plan.py. Result: the actual target can only own buildings it requested, so the foreign-map branch stays inactive; induction gives the clone identical requests and the same inactive branch. The standard v7 planner has no clock use. Verdict: REFUTED. The prior forecast-handoff proof/design caveat was too broad. Exact forecasting is justified under the synchronized standard-path hypotheses in proof66, analysis/forecast_standard_scope/PROOF.md. Its source-review receipt records the inspected hashes.

The foreign fallback imports economy20, whose planner has a finite1000000-second deadline and whose replan seed is fixed. A model of a different target can reach that fallback; a synchronized standard-start P5TNUB model does not. The earlier forecast-handoff source and declaration remain frozen so no running experiment is changed. We still test per-round prediction equality. This correction does not remove the separate3-second cutoff in the F34 handoff defender, which was correctly noted for the HP-handoff and H10 experiments.

## 2026-10-31T14:28:16.753192+00:00 Public-HP handoff complete: v28 loses after the round9 lead trigger

Claim: the positive-HP-lead handoff preserves the guarded opening's win against P5TNUB. Method:120 standard-start development games, ten disclosed targets, six fixed or HP-dependent handoffs, both assignments. Entries below use the target's outcome and target:counter HP.

| Target | fixed8 | fixed9 | fixed10 | lead8 | panic600 | lead8_panic600 |
| --- | --- | --- | --- | --- | --- | --- |
| P5TNUB | W 800:755 R50 | L 660:755 R50 | L 660:755 R50 | L 660:755 R50 | W 660:547 R50 | L 660:755 R50 |
| P5TNUcurrent | W 800:755 R50 | L 660:755 R50 | L 660:755 R50 | L 660:755 R50 | W 660:391 R50 | L 660:755 R50 |
| P5TNUF3 | W 800:755 R50 | L 660:755 R50 | L 660:755 R50 | L 660:755 R50 | W 660:391 R50 | L 660:755 R50 |
| F34 | L 660:753 R50 | L 240:753 R50 | L 100:753 R50 | L 660:753 R50 | W 100:-113 R16 | L 660:753 R50 |
| F35 | L 520:765 R50 | L 240:765 R50 | L 240:765 R50 | L 520:765 R50 | W 240:95 R50 | L 520:765 R50 |
| E25RM | W 660:644 R50 | W 240:-5122 R30 | L -40:618 R10 | W 240:-5122 R30 | L -460:618 R10 | W 240:-5122 R30 |
| best_v9e | L 660:755 R50 | L 520:755 R50 | L 520:755 R50 | L 660:755 R50 | L 520:755 R50 | L 660:755 R50 |
| budget_t3_r3 | L 240:670 R50 | L -320:644 R9 | L -600:644 R9 | L 240:670 R50 | L -600:644 R9 | L 240:670 R50 |
| rush_t1 | L -40:650 R9 | L -40:650 R8 | L -40:650 R8 | L -40:650 R9 | L -40:650 R8 | L -40:650 R9 |
| eco5_t3 | L -40:150 R9 | D -40:-526 R8 | D -40:-526 R8 | D -40:-526 R8 | W 800:592 R50 | W 800:592 R50 |

Verdict: CONFIRMED for P5TNUB. The lead8 and combined lead8_panic600 rules switch in round9 with counter HP755 and target HP660, then buy no further minions and finish755:660. Fixed round9 and10 have that same result; fixed round8 switches before the hit and loses755:800. P5TNUB's behind-only current-rule override therefore does not repair this counterexample.

Claim: the HP trigger improves on fixed H10 generally. Verdict: REFUTED on these conditions. Against E25RM, lead8 loses while fixed10 wins. Against eco5_t3, the panic rules survive with592HP but lose to800; their survival does not make them winning counters. The simple rush_t1 target loses against every variant, so it supplies no evidence of an early-rush repair. These results do not establish a universal best handoff.

All120 strict checks and original-engine replays pass, with28 target wins,86 losses and6 draws. All60 assignment pairs have equal normalized complete histories; these are not120 independent random samples. The12 matched fixed10 histories exactly reproduce the old GuardHandoff H10 histories. Fresh counter runs on the24 P5TNUB and rush_t1 histories reproduce every submitted action, leave all observations unchanged, make no internally rejected proposals and buy no minions after a handoff. The fresh-history audit took63.744060 seconds; original replay took46.272962 seconds. F34's3-second planner cutoff still prevents a universal timing-independent equality claim.

The first data-archive postprocessor failed because it expected the full120-condition manifest in each60-condition shard. The independent sharded checker verifies exact index-modulo shard coverage and92 archived inputs per shard; it passes. No game was rerun or omitted to repair this tooling error. The failure and successful replacement check are retained. Evidence: runs/validation/hp-handoff-{strict,replay,summary,data,fixed10-comparisons,histories}-001.json and analysis/hp_handoff/verification/{full_games,fresh_histories}.json.

## 2026-10-31T14:30:40.176968+00:00 Requested P5TNUB spending trap confirmed: exact public forecast versus visible-only controls

Claim: a guarded opening followed by just-in-time forecast defense makes P5TNUB keep buying blocked attacks while preserving a small HP lead. Method: the eight P5TNUB conditions already declared inside the48-game forecast-handoff experiment, four counter settings in both assignments. All eight complete histories have been replayed in the unchanged engine. Fresh counter calls match every recorded action, and all276 public-model predictions match the actual P5TNUB submission exactly. No observation changes or rejected internal proposals occur.

| Counter setting | Target:counter HP | End round | Attack gold after handoff | Defense gold after handoff | Counter damage after handoff |
| --- | --- | --- | --- | --- | --- |
| forecast, round9 | 660:755 | 50 | 17090 | 4650 | 0 |
| visible only, round9 | 660:-3131 | 24 | 17600 | 280 | 3886 |
| forecast, round10 | 660:755 | 50 | 12700 | 4570 | 0 |
| visible only, round10 | 660:-49 | 14 | 3650 | 140 | 804 |

All entries agree across assignments. Verdict: CONFIRMED on these eight conditions. At the round9 forecast handoff P5TNUB buys new minions every round9-18, with no hit in any remaining played round. At round10 it buys every round10-17 with the same zero-damage result. The counter makes no new attack purchases after switching. The paired visible-only controls advance the same model but choose their defense using only the already visible roster; both lose. This isolates the complete forecasting policy intervention, including its changed later histories, not a single-round effect. Defense spending is construction only, not factories. Blocked attacks can force defensive spending, so these totals do not establish zero economic value or a precise counterfactual loss.

Concrete winning counter: bot_research.bots.counters.forecast_handoff:@make?layout="empty"&growth_rounds=6&bait=[]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000&replan_iters=5000&deadline=9&forecast=true. Default model is exactly P5TNUB, independent and public-history only. Source SHA256 9bbd5045811173ead8cdb2fea0e83cfa92dc5381f88adfd67bfbbdab86c6cf4b. This is a targeted disclosed-development counter, not an unknown-policy guarantee. The remaining40 games against mismatched targets are still running and are not included in this conclusion.

Evidence: runs/validation/forecast-handoff-{histories,spending}-001.json, experiments/validation/check_forecast_handoff_histories.py and summarize_forecast_spending.py, and analysis/forecast_spending/PROOF.md with verification/receipt.json. Fresh replay/policy/model audit elapsed103.214778 seconds. The cost summarizer's first cross-seat check caught unnormalized physical-player HP; it was corrected before any output was published, with a correction receipt retained.

## 2026-10-31T14:36:38.142805+00:00: declared early round6 guard counters against v29 strikes

Claim: a fixed guard extension can answer the proposed round6 strike while retaining the grower's later handoff advantage. Method: new `bots/counters/early_guard_handoff.py` inserts a declared extension after the original round6 splash and before factories, then switches to attack-disabled F34 at round10 or12. `experiments/validation/early-guard-handoff-001.json` declares all72 games before running: six extensions, two handoffs, v28 P5TNUB and v29 with strike_until6 or7, both seats. v29 SHA256 `7fe402850fd6550823d9abef91e4ffcda414394a63e1fb7587f95222b31921c1`. The lead's hd2 original-handoff tests are separate; the empty-extension rows here are controls. Pools A/B remain development-disclosed and pool C remains unused.

Result so far: the exact extension JSON and original-engine checker pass24 funded components and12 six-round legal histories against idle. The original two splashes give S80 and admit all three tier3 in the3tier1+3tier3 fixture. Adding gun2+splash costs140 and blocks that fixture; a gun3 at (8,3), cost200, blocks3tier1+6tier3 and3tier1+1tier4. Adding three splashes costs180 and gives S200, excluding every tier1-tier3 copy on that unchanged map by the splash threshold proof. These are component statements, not yet game outcomes. All six extensions are affordable in the checked idle histories; excessive factory proposals are filtered and counted, not submitted. The generator published complete JSON then failed only in its final display field; the unchanged generator hash and independent component checks are retained. A first checker receipt with an absolute input key was retained privately, the key was made relative, and the checker reran before the campaign declaration.

Verdict: CONFIRMED for the stated component and legality checks; OPEN for full-game strength and the hypothesized counter to strike_until. Evidence: `runs/validation/early-guard-component-check-001.json`; `experiments/validation/analysis/early_guard_extension/PROOF.md` and `DESIGN.md`. Two bounded campaign shards began 2026-10-31T14:36:38.142805+00:00; cores28 and29, one worker each. Core30 is completing the48-game forecast-handoff audits.

## 2026-10-31T14:37:38.515191+00:00: forecast handoff48 fully audited, with targeted-model limits

Claim: forecasting the next roster repairs a visible-roster defensive handoff against the related attack-policy family. Method: six targets, forecast versus visible-only, handoff9 or10, both assignments. Result:48 valid games, all independently engine-replayed, all24 assignment pairs have identical complete normalized histories; all115 declared source/data inputs match. P5TNUB, P5TNUcurrent and P5TNUF3 each lose all four forecast games660:755 at round50 and win all four visible-control games. F34 wins all eight; E25RM wins both modes at handoff9 and loses both at10; rush_t1 loses before handoff. Six of24 intervention/control histories are identical (E25RM H10 and all rush_t1). All24 fresh counter-policy histories for the three related targets reproduce exactly, legally, without observation mutation or internal rejection. The P5TNUB model is exact against P5TNUB; it is deliberately mismatched against F3, with retained prediction differences despite the counter wins.

Verdict: CONFIRMED for this declared finite matrix; REFUTED as a universal winner on this matrix. Generalization of the improvement remains OPEN. The requested repeated-blocked-purchase mechanism is confirmed separately by the14:30 spending analysis, including the substantial defense expense it causes. Evidence: `experiments/validation/analysis/forecast_handoff/RESULTS.md` and `verification/full_games.json`. This is development evidence and leaves pool C unused.

## 2026-10-31T14:41:00.723706+00:00: interim v29 strike6 control failure and mechanism

Claim: moving the current-map attack before insurance in round6 repairs H10. Method: the declared early-guard campaign includes an empty-extension H10 control and the two-gun screened extension, both against v29 P5TNUB+strike_until6. Result so far: both seats lose520:729 in the empty control and520:755 with the screened extension, round50. In the empty control the v29 target buys eight tier2 in round6, against the visible one-splash map; the grower adds its second splash that same round and all eight are stopped. The target then allows two tier5 copies in round7 for280 damage. This is a recorded action trace, not an inference from HP alone. It explains why the proposed three-tier3 attack is not what current-map scoring actually selects. The full72-game replay and fresh-prefix audits remain pending; no source changes or action errors have appeared so far.

Verdict: provisionally REFUTED for strike_until6 on this exact control, pending full audit. Evidence: `experiments/validation/analysis/early_guard_extension/verification/interim_strike6_trace.json`; result cases24,25,28,29 of `runs/validation/early-guard-handoff-001-shard0/1`. Strike_until7 is still running. Pool C unused.

## 2026-10-31T14:41:34.889801+00:00: forecast48 fresh-policy reproduction complete

Claim: the recorded forecast-counter actions can be reproduced independently on all48 full public histories. Method: four disjoint shadow audits replay the recorded joint actions on the original engine while calling a fresh counter. Result: 1130 fresh decisions, all exact and legal, no observation mutations or internal rejections. The private P5TNUB model is deliberately imperfect for other target families; every disagreement is retained. Verdict: CONFIRMED for recorded counter-policy reproduction, with no added strength sample. Evidence: `experiments/validation/analysis/forecast_handoff/verification/full_history_shadows.json`.

## 2026-10-31T14:45:04.659457+00:00: second interim report review

Claim: final wording must distinguish historically held-out tests from later disclosed development and a large finite deadline from no deadline. Method: snapshot review of `reports/REPORT.md`. Result: the14:00 review's sufficient-threshold and finite-deadline qualifications are now largely incorporated. Two residual phrases remain: section2 says A/B are not used for tuning without limiting that claim to best_v9a/b before disclosure; line813 calls econ20's finite deadline absent. Verdict: CONFIRMED as wording issues in this snapshot, not game-outcome errors. Evidence: `experiments/validation/reviews/report-1444-review.md` and its hashed snapshot. Please preserve the version-specific A/B boundary and the still-unused C boundary in the final report.

## 2026-10-31T14:47:58.565928+00:00: early guards72 complete; v29 strikes do not repair H10

Claim: strike_until6 or7 repairs the guarded H10 counter. Method:72 predeclared development games, six round6 guard extensions, handoff10/12, three targets, both assignments. Result: ordinary P5TNUB22W2L; strike6 and strike7 each20W4L. Empty H10 remains a loss: P5TNUB660:755, strike6 520:729, strike7 380:521. Screened H10 also beats strike6 (520:755) and strike7 (520:549), but loses to P5TNUB (800:729). Every140/180/200-cost extension loses against all three targets. Verdict: REFUTED for both strike repairs, and REFUTED that those stronger guards preserve the counter's advantage. The original control already refutes the strike idea; it does not need a new splash answer.

All72 strict checks, original-engine replays and source/data checks pass; all36 assignment pairs have equal full normalized histories. Fresh counter calls reproduce all72 prefixes through round6, completing every extension. All12 full histories for empty/screened H10 against all targets also reproduce exactly (600 decisions), legally, without observation mutation. Filtered factory overflow proposals are retained and never submitted. The handoff delegate's finite3-second cutoff remains a reproducibility limitation beyond these observed checks. Complete table and receipts: experiments/validation/analysis/early_guard_extension/RESULTS.md and verification/. Pool C remains unused.

Claim: one extra splash on the fixed original two-splash map can reach the tier3 immunity threshold180. Method: exhaustive legal single-splash enumeration in a funded round6 fixture, independently repeated. Result:139 legal cells, maximum130. Verdict: REFUTED. Separately, the exhaustive at-most-one-turret-plus-one-wall class has minimum zero-damage cost200 for each of3tier1+3tier3,3tier1+6tier3,3tier1+1tier4. All78541 proposals and77408 accepted constructions are accounted for; all retained witnesses replay correctly. This does not imply a global minimum: the known140-cost two-turret answer is outside the class. Evidence: experiments/validation/analysis/cheap_guard_search/. Search elapsed285.662391 seconds; independent checker0.072730 seconds.

## 2026-10-31T14:50:50.745352+00:00: minimum pure-splash addition is three on the original two-guard map

Claim: two additional splashes suffice for tier3 immunity on the original guards at(10,1),(1,0), with no other construction or relocation. Method: enumerate every zero/one/two-cell addition; independently reconstruct in reverse order and run original one-tier3 combat on every legal map. Result: maximum S is80/130/170 respectively;9729 legal sets among9871 proposals. A checked third addition givesS200. Verdict: REFUTED for two; CONFIRMED that the minimum is three, cost180, within this exact pure-splash class. The universal-arrival equivalence follows from the pure-splash proof: one tier3 born at tick0 survives iffS<180, and every copy dies ifS>=180. All9730 combat checks, including the three-splash witness, pass. Search5.297486s; independent check17.572807s.

Evidence: experiments/validation/analysis/pure_splash_extensions/PROOF.md, RESULTS.md and verification/receipt.json; exact JSON in bots/counters/data/pure_splash_extensions_001.json. This does not claim a minimum over guns/walls. The same180-cost extension already loses all its early-guard full games, so no stronger-counter claim follows.

## 2026-10-31T14:52:07.244308+00:00: nominee counter transfer declared

Claim: the disclosed HP-trigger and forecast counters retain their wins against the two early-defense repairs P4TNUB and P5TNUBM. Method:20 predeclared standard games, two targets, five existing counters (lead8 and forecast/visible-only at handoff9/10), both assignments. The forecast model remains P5TNUB and is deliberately mismatched. Verdict: OPEN until completed checks. Manifest experiments/validation/nominee-handoff-001.json and analysis/nominee_handoff/PROOF.md. This complements the lead's broad timing/grower tests; pool C remains unused.

## 2026-10-31T14:55:40.171093+00:00: frozen fortress v36 handoff transfer declared

Claim: frozen fortress v36 wins the five disclosed HP/forecast/visible handoff conditions on the standard start. Method: ten fresh-process games, both physical assignments; reuse the exact five public opponents from nominee-handoff-001, retain the original P5TNUB forecast model deliberately, and audit all inputs, outcomes and original-engine replays. Result: pending. Verdict: OPEN. Declaration: experiments/validation/fortress36-handoff-001.json; full scope: experiments/validation/analysis/fortress36_handoff/PROOF.md. This is development evidence; pool C remains unused.

## 2026-10-31T14:56:31.598583+00:00: retargeted P5TNUBM forecast counter declared

Claim: replacing the old P5TNUB clone with an exact P5TNUBM clone restores a handoff-counter win at deadline 9 or 10. Method: four fresh standard-start games, both seats, with every other counter parameter fixed; old-model controls are in the still-running nominee-handoff campaign. Complete argument for the information boundary and standard-start clone equality written first in experiments/validation/analysis/retargeted_forecast/PROOF.md. Result: pending. Verdict: OPEN. Declaration: experiments/validation/retargeted-forecast-001.json. This is development, not pool C.

## 2026-10-31T14:59:57.236393+00:00: an early tier4 handoff counter

Claim: one tier4 in round5 makes an HP lead against P5TNUBM before defensive handoff. Method: write the argument first, implement EarlyHeavyHandoff with sequential original-action filtering, then four fresh original-engine openings through round5 (strike and no-strike, both seats). Result: all four pass with exact target predictions, unchanged observations and no rejected engine action. The strike makes target740 versus counter755; controls are800 versus755. The target has only walls and splashes, with exposure190<560, so the copy survives. Verdict: CONFIRMED for the component; full-game strength OPEN. Sixteen full games now declared, handoffs6/7/8/9 x strike/no-strike x seats. Declaration experiments/validation/early-heavy-handoff-001.json, proof74. This counter targets the heavy tier omitted by passive_mid_from, not the earlier P5TNUB forecast mismatch.

## 2026-10-31T15:01:17.724705+00:00: Frozen fortress v36 against disclosed handoff counters

Claim and verdict: The claim that v36 wins all ten conditions is REFUTED: the public-HP trigger wins in both assignments. The four forecast and visible-roster settings are beaten. These are complete-policy results; they do not isolate either of v36's two added options.

Method: 10 declared standard-start games, both physical assignments, strict accounting, complete original-engine replay, source/data archive verification, and 104 fresh public-history forecast-counter calls. Result: F36 8W/0D/2L. All 5 assignment pairs match completely. Full table, exact conditions and proof scope: experiments/validation/analysis/fortress36_handoff/RESULTS.md. Evidence receipt: analysis/fortress36_handoff/verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:01:17.850182+00:00: Exact P5TNUBM forecasting does not restore the counter win

Claim and verdict: The counter-repair hypothesis is REFUTED on both declared deadlines and assignments. The target remains undamaged and wins 800:755. Exact action prediction is confirmed on these 200 reached calls, but it supplies no winning guarantee.

Method: 4 declared standard-start games, both physical assignments, strict accounting, complete original-engine replay, source/data archive verification, and 200 fresh public-history forecast-counter calls. Result: P5TNUBM 4W/0D/0L. All 2 assignment pairs match completely. Full table, exact conditions and proof scope: experiments/validation/analysis/retargeted_forecast/RESULTS.md. Evidence receipt: analysis/retargeted_forecast/verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:02:41.790173+00:00: Early-defense nominees against disclosed handoff counters

Claim and verdict: The disclosed counters do not all retain their wins: P5TNUBM wins all ten conditions. P4TNUB remains vulnerable to the public-HP trigger and both forecast deadlines. The original forecast model is deliberately unchanged and differs from both targets.

Method: 20 declared standard-start games, both physical assignments, strict accounting, complete original-engine replay, source/data archive verification, and 520 fresh public-history forecast-counter calls. Result: P4TNUB 4W/0D/6L; P5TNUBM 10W/0D/0L. All 10 assignment pairs match completely. Full table, exact conditions and proof scope: experiments/validation/analysis/nominee_handoff/RESULTS.md. Evidence receipt: analysis/nominee_handoff/verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:03:32.083132+00:00: provisional round-five heavy counter to P5TNUBM

Claim: the mid-tier-only round-five insurance can concede a lasting HP lead to one tier4. Method: the predeclared early-heavy-handoff-001 campaign compares strike_count=1 with strike_count=0 at defensive handoff rounds6/7/8/9, both seats, using the exact public P5TNUBM model. The completed round6 pair ends target740:counter755 at round50; both no-strike controls end800:755. The round7 first seat also loses740:755. The component check already confirms the round5 map is splash-only with S190, so the single tier4 deals60. No submitted action rejection or bot error in these results.

Verdict: OPEN pending the campaign's independent replay, source/data checks and complete fresh-history reproduction. This is a warning of a concrete completed-game counterexample, not a finished campaign claim. Lead: the counter spec is the early1_handoff6 entry in experiments/validation/early-heavy-handoff-001.json. It buys one tier4 in round5, then switches to exact-public-model defense in round6. The public model never accesses pending submissions. Pool C remains unused.

## 2026-10-31T15:04:05.004409+00:00: early-heavy forecasting ablation declared

Claim: visible-roster defense or the earlier P5TNUB model suffices to preserve the round-five tier4 lead against P5TNUBM. Method: eight standard games, switch rounds6/7, both seats, with exact-model references already in the predeclared early-heavy-handoff campaign. The strike and all non-knowledge parameters are fixed. Verdict: OPEN. Declaration early-heavy-knowledge-001.json; standalone argument analysis/early_heavy_knowledge/PROOF.md. No reserved conditions.

## 2026-10-31T15:07:18.525455+00:00: round-five response cost on the reached P5TNUBM map

Claim: a single additional building can stop the early tier4 while retaining S>=180. Method: enumerate the unchanged map and all five building types at all144 cells, then independently check single-copy exposure and replay an affordable round-five deviation on the original Engine. Result:721 proposals,466 legal, restricted minimum200 gold (gun3 at(0,5), S190). Max exposure of admissible gun2 additions is466, below tier4 HP560. Omitting all ten actual round-five factories pays for the gun3; the changed round ends target800:counter755 and every action is accepted. Verdict: CONFIRMED only in the one-addition class and for this one-round deviation. This does not imply a full-policy improvement, a minimum over two-building plans, or mixed-roster immunity. Evidence: analysis/round5_heavy_defense/RESULTS.md and verification/receipt.json.

## 2026-10-31T15:09:48.508145+00:00: The early-heavy counter depends on accurate anticipatory defense

Claim and verdict: REFUTED: either visible-roster defense or the older P5TNUB model preserves the early-heavy win against P5TNUBM. All eight interventions lose. This is evidence of model dependence in these conditions, not a claim that no other defender could win.

Method: 8 predeclared standard games with both player assignments, strict accounting, original-engine replay, source/data checks and 192 fresh public-history counter decisions. Result from target perspective: 8W/0D/0L; all assignment pairs match. Model disagreements: 118. Local proposals filtered after the strike: 104; no rejected submitted actions. Details and exact conditions: experiments/validation/analysis/early_heavy_knowledge/RESULTS.md; receipt verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:09:49.034616+00:00: One round-five tier4 wins with an early exact-model handoff

Claim and verdict: CONFIRMED: one tier4 in round five followed by exact-public-model defense from round six or seven beats P5TNUBM in both assignments, 755:740. REFUTED: the same claim for handoffs eight and nine; both lose. Every no-strike control loses.

Method: 16 predeclared standard games with both player assignments, strict accounting, original-engine replay, source/data checks and 800 fresh public-history counter decisions. Result from target perspective: 12W/0D/4L; all assignment pairs match. Model disagreements: 0. Local proposals filtered after the strike: 104; no rejected submitted actions. Details and exact conditions: experiments/validation/analysis/early_heavy_handoff/RESULTS.md; receipt verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:12:25.778135+00:00: Model-free handoff experiment declared; storage maintenance

Claim: a budget-based pure-tier forecast can preserve the early-heavy win without any target policy model. Verdict: OPEN. Method: budget-handoff-001 declares twelve development conditions, H6/H7 times public budget fractions1/4,1/2,1, both seats. Source and data are pinned. The standalone argument in analysis/budget_handoff/PROOF.md proves only legality and public-input use; it expressly does not certify all mixed rosters. Prefix checks are running before full matches. Pool C remains unused.

Lossless storage maintenance compressed 30 stateful-catalogue replays and307 earlier forecast-timing replays, verifying every decompressed SHA before deleting its original uncompressed copy. Exact counts, byte savings and restore paths are in runs/validation/archived-wave2-replays-001.json and archived-wave3-replays-001.json. Use restore_archived_replay.py with the appropriate manifest before an older replay reader. All evidence bytes remain available.

## 2026-10-31T15:15:48.139800+00:00: Nominee-counter game declared and partial model-free result

Claim: the four fixed policies P4TNUB, P5TNUBM, early1_handoff6 and lead8 may exhibit a counter-strategy cycle. Verdict: OPEN pending the six newly declared matches and replay checks. The three other pairs reuse already audited games. Exact new declarations: nominee-cross-001.json and counter-cross-001.json; informal statement analysis/nominee_counter_game/PROOF.md. The early counter keeps the same P5TNUBM clone against all targets.

The twelve-case model-free budget-handoff campaign is still running. Completed half-budget and full-budget cases already beat P5TNUBM; the quarter-budget variant loses. These are provisional match results until all campaign checks finish. Thus the earlier knowledge intervention should not be read as evidence that an exact model is necessary for every possible defender.

## 2026-10-31T15:19:06.282803+00:00: A public-budget forecast preserves the early-heavy win

Claim and verdict: CONFIRMED: with the declared round5 tier4 opening, a forecast using half or all of the public enemy budget preserves the 755:740 win against P5TNUBM in both assignments, for handoff6 and handoff7. REFUTED: the quarter-budget variant preserves that win. This also refutes a broader claim that these wins require an exact opponent policy model.

Method and result: Twelve predeclared games, full original-engine replays, six matching assignment pairs, 464 exact fresh counter decisions and source/data checks. Target4W/8L. Half/full forecasts win; quarter forecasts lose740:-285 at round16. No submitted invalid actions. Details: experiments/validation/analysis/budget_handoff/RESULTS.md; receipt verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:19:12.617705+00:00: The two nominees and their counters form a finite cycle

Claim and verdict: CONFIRMED: the four fixed standard-start policies have directed cycles P5TNUBM > lead8 > early1_handoff6 > P5TNUBM and P4TNUB > early1_handoff6 > P5TNUBM > lead8 > P4TNUB. No policy in this set wins against every other one. A rational one-third mixture over P5TNUBM, early1_handoff6 and lead8 has value0 in the stated finite payoff table.

Method and result: Twelve freshly audited recorded games across six pairs, six newly executed and six reused. All assignment histories match; both policies in the new games reproduce496 decisions exactly. Exact rational certificate checks pass. Details: experiments/validation/analysis/nominee_counter_game/RESULTS.md; receipt verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:20:13.134645+00:00: Fixed budget-counter transfer declared

Claim: four already tested budget-handoff policies transfer to P4TNUB, fortress36/37, best_v9e and lead8. Verdict: OPEN. Method:40 new standard-start conditions in budget-transfer-a001/b001/c001.json, both seats. No retuning and no target clone in the budget counter. Full standalone scope in analysis/budget_handoff_transfer/PROOF.md. Frozen best_v9e remains SHA70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Pool C remains unused.

## 2026-10-31T15:22:04.380131+00:00: Public-HP-triggered budget handoff declared

Claim: continuing the opening until a public HP lead improves fixed-deadline counter transfer. Verdict: OPEN. Method: triggered-budget-a001/b001/c001.json declare48games, six targets, strike0/1 and public budget1/2 or1, earliest switch6, margin0, both seats. Proof80 states legal public-only switching and conditional equivalence to the fixed policy at its realized switch. Existing fixed transfer is still running, so no transfer result is assumed. No Cconditions.

## 2026-10-31T15:26:12.505573+00:00: Fixed budget counters do not transfer

Claim and verdict: REFUTED: the four fixed budget-handoff policies transfer their wins against P5TNUBM to the five declared targets. All 40 transfer games are target wins. The earlier wins remain valid for P5TNUBM only in their tested conditions.

Method and result: 40 predeclared standard games, five targets, four unchanged counter settings, both assignments. All original-engine replays and source/data checks pass. All 1,584 fresh counter decisions reproduce and all 20 assignment pairs match. No submitted invalid actions or bot errors. Full table: experiments/validation/analysis/budget_handoff_transfer/RESULTS.md; receipt verification/full_games.json. Pool C remains unused.

## 2026-10-31T15:27:32.112521+00:00: Earlier and later triggered strikes declared

Claim: one fixed strike timing can beat both P4TNUB and P5TNUBM. Verdict: OPEN. Method: 32 new standard games, (strike, earliest handoff)=(4,5),(4,6),(6,7),(7,8), each with budget fraction one-half or one, both seats and nominees. All other settings fixed. The round-four strike competes directly with the first splash guard: on a 291-gold observation, 260+60 is unaffordable. Prefix checks precede full games. Manifests triggered-timing-a001/b001.json; proof analysis/triggered_budget_timing/PROOF.md. No pool C conditions.

## 2026-10-31T15:28:58.794987+00:00: Public-budget counters have complementary wins

Claim and verdict: CONFIRMED: the no-strike HP-triggered budget defender beats P4TNUB and best_v9e, while its one-tier4 variant beats P5TNUBM. REFUTED: one of these four fixed counter settings beats all six targets, or adding the HP trigger repairs transfer of the previous one-strike fixed-handoff counter to any of the five transfer targets.

Method and result: 48 declared standard games, both seats, all strict/replay/source/data checks passed, 1,426 exact fresh counter decisions and 24 identical assignment pairs. Target total 32W/4D/12L. No-strike wins 755:660 against P4TNUB and best_v9e; one tier4 in round 5 wins 755:740 against P5TNUBM. Both fortress targets win all eight settings. lead8 draws the no-strike counter by simultaneous destruction and beats the one-strike counter. Full table and scope: experiments/validation/analysis/triggered_budget_handoff/RESULTS.md. This does not isolate the trigger effect because removing the strike is another intervention. Pool C remains unused.

## 2026-10-31T15:29:24.036588+00:00: Matched no-strike deadline controls declared

Claim: delaying the no-strike handoff from round 6 until an observed HP lead improves outcomes against P4TNUB and best_v9e. Verdict: OPEN. Method: twelve new fixed-H6/H8 controls, budget fraction one-half, targets P4TNUB/P5TNUBM/best_v9e, both assignments; reuse the six corresponding audited trigger games. H8 should reproduce the trigger histories for P4TNUB and best_v9e. Proof: analysis/no_strike_handoff_controls/PROOF.md. This isolates the deadline intervention without also changing the strike count. No pool C conditions.

## 2026-10-31T15:31:56.109421+00:00: An affordable guard for the round-four strike

Claim: a 30-gold gun1 at (10,1) preserves the round-four tier4 lead against both nominees. Verdict: OPEN for full games. The component proof shows that gun plus tier4 costs 290, fits the reached 291-gold budget, and the unchanged empty-route gun stops three tier1 copies. Method: 16 declared standard games, gun enabled/disabled, half/full public-budget defense, both nominees and seats. Prefix checks precede full games. Declaration guarded-round4-001.json; proof analysis/guarded_round4_strike/PROOF.md. No reserved conditions.

## 2026-10-31T15:33:54.446398+00:00: Unguarded timing alone does not beat both nominees

Claim and verdict: REFUTED: one of these eight fixed timing and budget settings beats both nominees. CONFIRMED: the round-six and round-seven variants beat P4TNUB, but neither beats P5TNUBM.

Method and result: 32 predeclared standard games, all strict/replay/source/data checks passed, 692 freshly regenerated decisions and 16 matching assignment pairs. P4TNUB 8W/8L, P5TNUBM 16W. The round-four strike lands but loses its own lead; later P4 wins are counter HP755 against target520 or660. Full table: experiments/validation/analysis/triggered_budget_timing/RESULTS.md. Pool C remains unused.

## 2026-10-31T15:34:32.411106+00:00: Matched deadline controls isolate the no-strike improvement

Claim and verdict: CONFIRMED: delaying the fixed no-strike handoff from round 6 to round 8 converts losses into wins against P4TNUB and best_v9e. The H8 controls reproduce their HP-triggered reference histories exactly.

Method and result: twelve new games, both seats, all strict/replay/source/data checks pass, 600 exact fresh decisions. H6 loses755:800 against all three targets. H8 wins755:660 against P4TNUB and best_v9e and still loses755:800 against P5TNUBM. All four expected H8-trigger full-history equalities pass; the P5TNUBM trigger never switches and instead dies by round13. Six trigger references are reused, not new samples. Full table: experiments/validation/analysis/no_strike_handoff_controls/RESULTS.md. Pool C remains unused.

## 2026-10-31T15:34:47.685820+00:00: Equal-prefix proof and limits of indistinguishability

Claim and verdict: CONFIRMED under equal public labels, P4TNUB and P5TNUBM have identical gameplay prefixes through round4 and the same opponent observation before round5 submission. Source specialization produces equal syntax trees; twelve paired prefixes (six opponents, both seats) pass. Full proof and receipt: experiments/validation/analysis/nominee_prefix_equivalence/.

For lead and defense: this does not establish that one policy cannot beat both nominees. Equal information forces equal decisions only before divergence; it does not prove that every common decision loses one game. The same qualification applies to defense.md 15:32Z claim that no trigger can handle growth6 and growth7: the prefix observation alone does not establish an unavoidable strategic price. A separate exhaustive or analytic payoff argument is needed. Also, engine observations expose names and the runner normally gives full specs as names; our theorem explicitly requires equal labels. Pool C remains unused.

## 2026-10-31T15:35:26.177450+00:00: One fixed guarded strike beats both nominees

Claim and verdict: CONFIRMED: the 30-gold round-four corner gun converts the fixed early-heavy policy from a loss into a 755:740 win against both P4TNUB and P5TNUBM, for both tested public-budget fractions and both assignments.

Method and result: sixteen declared standard games, all strict/replay/source/data checks pass, 496 exact fresh decisions, eight identical assignment pairs and eight exact disabled-control histories. At round4, gun1(10,1)+tier4 costs290 of291 gold; the gun stops the three incoming tier1, preserving counter755 against target740. The public HP trigger hands off at round5 and holds the lead. Disabled gun loses in round12. Winning specs are earlygun1_budget1of2 and earlygun1_budget1of1 in experiments/validation/guarded-round4-001.json; source bots/counters/guarded_round4_trigger.py. Full table and receipt: experiments/validation/analysis/guarded_round4_strike/. No model or name lookup. Pool C remains unused.

## 2026-10-31T15:35:52.721904+00:00: Guarded round-four transfer declared

Claim: the two unchanged guarded round-four counter settings transfer to F36, F37, best_v9e, lead8, E25RM and E30. Verdict: OPEN. Method: 24 standard-start games, both seats, three frozen declarations guarded-transfer-a001/b001/c001.json. The conditional three-tier1 gun lemma is not assumed for other targets. Prefix checks and full replay/source/data/fresh-decision audits follow. Proof: experiments/validation/analysis/guarded_round4_transfer/PROOF.md. No pool C conditions.

## 2026-10-31T15:39:26.100114+00:00: Route-preserving defense has a 560-HP splash ceiling

Claim and verdict: CONFIRMED under the fixed corner-gun and off-current-route construction hypotheses. The unchanged free_plan never builds walls or blocks its current route. From the round4 corner gun alone, route22 remains fixed; the twenty eligible splash cells contribute56 adjacencies, so exposure cannot exceed560. Original-engine placement checks and independent counting pass. On the all-splash maximizing map, tier5 copies survive, as proved and checked for seven combat cases. This does not bound other added-gun layouts or prove a full-game loss. Proof and receipt: experiments/validation/analysis/route_preserving_defense/.

## 2026-10-31T15:39:47.425291+00:00: Guarded strike also beats best_v9e, but five transfer targets win

Claim and verdict: CONFIRMED: both guarded round-four settings beat best_v9e by 15 HP in both assignments. REFUTED: either fixed setting also beats the five other declared targets.

Method and result:24 predeclared standard games, all strict/replay/source/data checks pass, 590 fresh decisions and12 identical assignment pairs. F36/F37 win740:-75 at round15 (half budget) or740:-67 at round25 (full). E25RM/E30 win320:-9 at round14. lead8 wins500:240 at round50 or500:-40 at round9. Best_v9e loses740:755 in both settings. Table: experiments/validation/analysis/guarded_round4_transfer/RESULTS.md. Pool C remains unused.

## 2026-10-31T15:41:01.802259+00:00: Fixed wall intervention declared

Claim: adding fixed walls at the first defensive handoff repairs transfer while retaining nominee wins. Verdict: OPEN. Method:48 standard games across eight targets, modes none/stageA/full, half-public-budget forecast, both seats. Component checks already pass: stageA costs20 and full costs29; both yield route42. Their off-route splash ceilings are only540 and640 respectively, so neither geometry proves tier5 immunity under the inherited route-preserving planner. This is an empirical intervention, not an assumed repair. Declarations wall-handoff-a001/b001/c001.json; proof analysis/handoff_wall_intervention/PROOF.md. No pool C.

## 2026-10-31T15:43:51.693112+00:00: Joint wall and turret handoff declared

Claim: replacing the post-trigger free planner with frozen-v7 joint wall/turret planning repairs transfer while retaining nominee wins. Verdict: OPEN. Method:32 standard games across eight targets, free/template modes, half-public-budget forecast and both seats. The opening, trigger and factory policy remain fixed. Declarations template-handoff-a001/b001/c001.json; proof analysis/template_handoff_defense/PROOF.md. No pool C.

## 2026-10-31T15:46:31.182741+00:00: Public first-roster selector declared

Claim: one public-observation selector improves over two fixed counters on eight development targets. Verdict: OPEN. Method:48 standard games, adaptive/forced-early/forced-growth, both seats. Both branches buy5 factories in round1. Round2 chooses early if at least3 first-round tier1 entries are visible, otherwise growth6/H10. The threshold was chosen from development histories; no held-out claim. Growth branch retains a wall-clock planner. Declarations public-selector-a001/b001/c001.json; proof analysis/public_roster_selector/PROOF.md. Pool C unused.

## 2026-10-31T15:48:47.797451+00:00: wall defensive handoff intervention complete

Claim and verdict: CONFIRMED: both fixed-wall interventions preserve the three nominee/best_v9e wins. REFUTED: either intervention repairs any of the five other transfer targets.

Method and result: all48 predeclared standard games, all strict/replay/source/data checks, 1556 fresh decisions and24 identical seat pairs. Both wall settings lose to F36/F37 in round16, compared with round15 without walls. They reduce lead8's final HP from500 to380 but still lose380:240. The economy targets prevent the trigger entirely, so all three modes have the same outcome320:-9 at round14. The completed tables do not support a strength improvement from fixed walls. All16 old control histories match exactly. Details experiments/validation/analysis/handoff_wall_intervention/RESULTS.md. Pool C remains unused.

## 2026-10-31T15:48:48.707098+00:00: template defensive handoff intervention complete

Claim and verdict: CONFIRMED: the joint wall/turret planner repairs the F36/F37 transfer losses while preserving the three nominee/best_v9e wins. REFUTED: this intervention beats all eight targets.

Method and result: all32 predeclared standard games, all strict/replay/source/data checks, 1172 fresh decisions and16 identical seat pairs. F36/F37 now lose740:765 at round50. The same targets beat the free planner740:-75 at round15. The joint planner still loses500:380 to lead8 at round50, while the free planner loses500:240. E25RM/E30 again prevent the trigger, so a post-trigger intervention cannot alter their320:-9 round14 wins. These matched complete-policy interventions establish the measured differences; they do not attribute them to one particular wall or turret. All16 old control histories match exactly. Details experiments/validation/analysis/template_handoff_defense/RESULTS.md. Pool C remains unused.

## 2026-10-31T15:51:50.780316+00:00: Unchanged selector baseline expansion declared

Claim: the fixed first-roster selector transfers beyond its eight target examples. Verdict: OPEN. Method: all12 existing PROFILES, three unchanged modes and both assignments,72 standard games. These are known development baselines, not a held-out pool. Proof analysis/public_selector_baselines/PROOF.md; declarations selector-baselines-a001/b001/c001.json. Pool C remains unused.

## 2026-10-31T15:53:42.497190+00:00: Public selector targets complete

Claim and verdict: CONFIRMED: the adaptive selector scores strictly more wins plus half draws than either fixed branch on this finite set.

Method and result: 48 declared standard games, all independent audits pass; 1628 fresh decisions,24 identical seat pairs and32 exact complete-history controls. Counter totals: adaptive 14W/2D/0L; early 6W/0D/10L; growth 12W/2D/2L. Details experiments/validation/analysis/public_roster_selector/RESULTS.md. This is a development comparison; pool C remains unused.

## 2026-10-31T15:53:42.884239+00:00: Public selector baselines complete

Claim and verdict: REFUTED: the adaptive selector scores strictly more wins plus half draws than either fixed branch on this finite set.

Method and result: 72 declared standard games, all independent audits pass; 1170 fresh decisions,36 identical seat pairs and24 exact complete-history controls. Counter totals: adaptive 16W/6D/2L; early 18W/0D/6L; growth 18W/6D/0L. Details experiments/validation/analysis/public_selector_baselines/RESULTS.md. This is a development comparison; pool C remains unused.

## 2026-10-31T15:54:24.828596+00:00: For the lead: selector gain and a baseline counterexample

Claim and verdict: CONFIRMED on the eight-target development set, the public first-roster selector wins14 and draws2 of16 assignments. It chooses the guarded round-four strike against P4TNUB, P5TNUBM and best_v9e, and growth6/H10 against F36, F37, lead8, E25RM and E30. All48 games across the three modes have completed with all audits and32 exact history controls. The forced growth6/H10 branch loses755:800 to P5TNUBM, so the new nominee repairs that particular growth counter; the guarded early branch still wins755:740. The adaptive policy draws the lead8 mirror race by simultaneous base destruction in round8. It reads only the visible first-round tier1 count, never labels. Source bots/counters/public_roster_selector.py, default factory.

REFUTED: this selector is uniformly stronger than its fixed growth branch. The unchanged twelve-archetype expansion gives adaptive16W/6D/2L, early18W/0D/6L, growth18W/6D/0L. rush_t1 shows six first-round tier1, selects the early branch, and wins80:-305 at round8; the growth branch instead wins650:-40. All72 games and24 exact branch-history controls pass. Both experiments are development evidence. A count-specific repair and adversarial opening changes are next; no new final-candidate recommendation is implied. Pool C is untouched and capacity will be available for the explicit freeze.

## 2026-10-31T15:56:04.958687+00:00: Exact-count repair and changed opening declared

Claim: selecting early only at exactly3 first-round tier1 repairs the rush_t1 error while retaining the eight-target results. Verdict: OPEN. Method:40 new games against the same20 development targets, with40 declared old forced-branch history controls. Sources and declarations exact-selector-a001/b001/c001.json; proof analysis/exact_roster_selector/PROOF.md.

Counter-claim: changing only the nominee's r1_poke can mislead either selector. Verdict: OPEN. Method: P5TNUBM with r1_poke0,2,3,4 against old adaptive, exact adaptive, forced early and forced growth,32 games, both seats. The3-poke setting is a repeated default control. Source nominee implementation is unchanged; the existing parameter changes its legal first-round actions. Declaration roster-spoof-001.json; proof analysis/roster_feature_spoof/PROOF.md. No pool C.

## 2026-10-31T16:01:01.269279+00:00: exact roster-selection experiment complete

Claim and verdict: CONFIRMED: the exact-count predicate repairs the rush_t1 loss and preserves the selected branch histories on the other nineteen development targets.

Method and result: 40 new standard games, all audits pass, 748 fresh decisions,20 matching assignment pairs and40 exact history controls. The forty new games score32W/8D/0L. The old threshold selector scored30W/8D/2L across the same twenty targets. Fixed early play scored24W/0D/16L and fixed growth30W/8D/2L. Every new history matches its predeclared old forced-branch control exactly. Those controls are reused evidence, not forty further independent samples. The repair was chosen after observing the old rush_t1 failure. Full table: experiments/validation/analysis/exact_roster_selector/RESULTS.md. Pool C remains unused.

## 2026-10-31T16:02:12.239900+00:00: Published entry-point continuation preflight declared

Claim: the direct decide function and default factory reproduce the same recorded actions after skipped opening calls. Verdict: OPEN. Method: six new development games against the existing eco6_t5 archetype, both assignments of three already used histories mirror:1:2, asym:3:2 and mirror:22:3. Candidate is installed best_v9e SHA70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Declaration experiments/validation/entrypoint-continuations-001.json; proof analysis/best_entrypoint_equivalence/PROOF.md. This checks interface and state initialization, not new held-out strength. Pool C remains unused.

## 2026-10-31T16:05:24.034989+00:00: spoof roster-selection experiment complete

Claim and verdict: CONFIRMED: a declared change of opening count makes a selector lose while its alternative fixed branch wins.

Method and result: 32 new standard games, all audits pass, 1448 fresh decisions,16 matching assignment pairs and22 exact history controls. Qualifying controlled counterexamples: [{"alternative": "select_early", "alternative_hp_target_first": [740, 800], "hp_target_first": [800, 566], "selected": "growth", "selector": "select_adaptive", "target": "P5M_poke0"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 800], "hp_target_first": [800, 566], "selected": "growth", "selector": "select_exact", "target": "P5M_poke0"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 770], "hp_target_first": [800, 692], "selected": "growth", "selector": "select_adaptive", "target": "P5M_poke2"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 770], "hp_target_first": [800, 692], "selected": "growth", "selector": "select_exact", "target": "P5M_poke2"}, {"alternative": "select_growth", "alternative_hp_target_first": [660, 740], "hp_target_first": [740, -184], "selected": "early", "selector": "select_adaptive", "target": "P5M_poke4"}]. Each adaptive history matches its selected forced branch, and all six count3 default-control histories reproduce the earlier nominee experiment. The opening changes also change income and damage; the claim is the measured complete-policy comparison, not a pure isolated effect of the displayed count. Full table: experiments/validation/analysis/roster_feature_spoof/RESULTS.md. Pool C remains unused.

## 2026-10-31T16:10:02.147352+00:00: Published entry-point audit complete and x158 count corrections

Claim: the installed best_v9e direct and factory entry points agree on the declared standard and skipped-call continuation histories. Verdict: CONFIRMED for twelve games and358 regenerated policy decisions per entry point. Six standard and six continuation cases; fourteen skipped opening rounds. All fresh actions legal, observations unchanged, exact recorded-policy agreement. SHA70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Evidence: experiments/validation/analysis/best_entrypoint_equivalence/RESULTS.md and verification/preflight_v9e.json. A later freeze needs a new check.

Claim: x158's table and narrative counts agree. Verdict: REFUTED; the correct sixty-game split is twelve standard (fortress0W6D6L) and forty-eight continuation (24W0D24L). All six P5TNUBM standard draws are785:785, with15 damage dealt by each side, not no-hit draws. Against9e the result is785:790 with10/15 dealt. Independent original-engine replay verifies all36 retained logs;24 continuation wins have no retained log and are only row-checked. Evidence: experiments/validation/analysis/team_fortress_report_audit/RESULTS.md and verification/x158.json. For x159, the guarded-round4 counter's defensive forecast is public-budget-based, with no P5TNUBM clone or identification. These corrections do not change x159's measured losses.

Claim: the new round-four selector's local no-enemy-action projection equals original-engine combat under that hypothesis. Verdict: CONFIRMED on48 disclosed prefixes (24 targets, both seats), including equality of both branches through round3, legal actions and unchanged observations. The first component version double-subtracted simulator-mutated HP; it was corrected before any full games, and the old source and receipt are retained and marked superseded. Corrected receipt: experiments/validation/analysis/round4_public_projection/verification/prefixes_corrected.json. Full-game robustness remains OPEN. Pool C is unused.

## 2026-10-31T16:10:23.981965+00:00: Full projected-lead selector campaign declared

Claim: delaying selection until round4 and using a public projected HP lead repairs opening-count spoof failures. Verdict: OPEN. Method:144 new standard games,24 disclosed targets x adaptive/forced-early/forced-growth x both seats. Early now uses joint wall/turret continuation; growth is unchanged H10. Declarations projection-selector-a001/b001/c001.json freeze source, data, proof and the48 prefix checks. Ninety-six predeclared complete-history comparisons check selected-branch equality and old growth controls. This is development after observing the previous failures, with no held-out claim. Positive one-round projection does not promise later survival, especially against the known economy targets. Pool C unused.

## 2026-10-31T16:13:20.553395+00:00: Review for the report's final freeze

Claim: the current interim scope statement can be carried unchanged to P5TNUBM. Verdict: REFUTED by its TIMING2 regressions, already reported by the lead. Keep the predeclared gate-based selection and the grower gains, and state the early-strike tradeoff explicitly. The current H10 failure also needs version attribution: P5TNUBM beats the forced growth6/H10 branch800:755, whereas earlier nominees lose it. Detailed review: experiments/validation/reviews/report-prefreeze-1615-review.md. It also links the simpler round4 public-budget counter, x158 count/damage corrections, and the distinction between first-round exchange and full-game victory. PoolC unused.

## 2026-10-31T16:15:59.320339+00:00: Pool C freeze accepted; final validation begins

Claim: best_v9e is the frozen installed candidate and P5TNUBM is a prespecified comparison only. Verdict: CONFIRMED for byte hashes and lead authorization, strength OPEN. Lead's 16:12Z FROZEN post keeps best_v9e SHA70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Both candidates are now declared before the first C game in experiments/validation/late-comparison-declaration-001.json. The original seventy-two-condition manifest is unchanged. Standard and two skipped-call continuation starts will be reported separately, with both seats, exact replay, failure accounting, loaded-source checks and fresh installed entry-point checks. P5TNUBM cannot be selected from these results. Proof96: analysis/final_reserved_validation/PROOF.md.

## 2026-10-31T16:23:07.306650+00:00: Projected-lead selector full experiment complete

Claim and verdict: CONFIRMED: the selector beats all four declared nominee opening-count variants. REFUTED: a positive one-round projected lead suffices to select a winning complete policy.

Method and result:144 new development games,24 targets,three modes,both seats. Counter scores: project_adaptive: 38W/0D/10L; project_early: 34W/0D/14L; project_growth: 32W/8D/8L. All4778 fresh counter decisions reproduce, all72 seat pairs and96 predeclared control histories agree. All original-engine, source, data and legality audits pass. Wrong-branch witnesses: [{"target": "E25RM", "selected": "early", "hp_target_first": [320, -9], "alternative": "project_growth", "alternative_hp_target_first": [-40, 618]}, {"target": "E30", "selected": "early", "hp_target_first": [320, -9], "alternative": "project_growth", "alternative_hp_target_first": [-40, 618]}, {"target": "eco3_t1", "selected": "early", "hp_target_first": [420, -410], "alternative": "project_growth", "alternative_hp_target_first": [-40, 800]}]. Full table experiments/validation/analysis/round4_public_projection/RESULTS.md. These are disclosed development conditions; the separately declared pool C validation is running.

## 2026-10-31T16:24:04.960274+00:00: Route-gated selector repair, development only

Claim: adding a public route-length predicate to the projected-lead selector removes its ten losses on the disclosed 24-target set while keeping its nominee wins. Verdict: OPEN. The rule is Q and enemy route length greater than spawn-base Manhattan distance, then the unchanged early branch; otherwise unchanged growth. Proof97 records assumptions and the conditional full-history identity argument. The next 48 games and old-branch controls are development checks, not new validation. Pool C remains reserved for its already frozen candidates; none of its outcomes informed this rule.

## 2026-10-31T16:24:53.679454+00:00: Pool C P5TNUBM fully audited

Claim and verdict: CONFIRMED for the exact 72-condition finite evaluation of SHA d79949a584020abc7f35ffd1e340c50f9c6e5a2883545e253b342276cf108f9c. This is the comparison declared before the first pool C game. P5TNUBM remains unselected, regardless of this table. It uses the same fixed conditions as the primary validation and adds no independent sample of opponents.

standard: 18/4/2 W/D/L, worst HP difference -26, rounds[9, 10, 11, 12, 50], largest candidate call 0.829781s.
mirror_7493_3: 24/0/0 W/D/L, worst HP difference 719, rounds[10, 11, 12, 13, 14, 15], largest candidate call 1.019920s.
asym_8669_2: 24/0/0 W/D/L, worst HP difference 526, rounds[11, 12, 13, 25], largest candidate call 0.635131s.

All 72 original-engine replays pass, no bot errors/rejections/source drift. Entry-point verification: The parameterized comparison uses its declared factory. Evidence: experiments/validation/analysis/final_reserved_validation/COMPARISON.md. All per-seat/per-opponent tables: runs/validation/reserved-C-p5tnubm-001-summary.md. Separation qualifications and all computational attempts are retained.

## 2026-10-31T16:28:51.033096+00:00: Pool C effective variation audit

Claim and verdict: CONFIRMED, each candidate has33 distinct complete normalized trajectories among72 games, not36 independent opponent/start behaviors. Standard12, mirror11, asymmetric10; each ordinary seat pair agrees. Guard variants C10/C11 lose their only difference when round-one calls are skipped; budget variants C08/C09 additionally agree on the asymmetric start. Cross-candidate equality: asym_8669_2: 24/24; mirror_7493_3: 24/24; standard: 6/24; 42 distinct histories across144 logs. Every log was reread and compared with strict raw and normalized digests. This does not change declared totals, establish random independence, or erase the eight unresolved historical-source rows. Proof and receipt: experiments/validation/analysis/effective_pool_c_diversity/.

## 2026-10-31T16:29:09.546664+00:00: Pool C best_v9e fully audited

Claim and verdict: CONFIRMED for the exact 72-condition finite evaluation of SHA 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. This is the independent final validation of the installed bot. Selection was fixed before these games.

standard: 18/6/0 W/D/L, worst HP difference 0, rounds[9, 11, 12, 13, 14, 17, 50], largest candidate call 0.867711s.
mirror_7493_3: 24/0/0 W/D/L, worst HP difference 719, rounds[10, 11, 12, 13, 14, 15], largest candidate call 0.652982s.
asym_8669_2: 24/0/0 W/D/L, worst HP difference 526, rounds[11, 12, 13, 25], largest candidate call 1.052337s.

All 72 original-engine replays pass, no bot errors/rejections/source drift. Entry-point verification: 1104 policy calls per entry point over all 72 games. Evidence: experiments/validation/analysis/final_reserved_validation/RESULTS.md. All per-seat/per-opponent tables: runs/validation/reserved-C-best-v9e-001-summary.md. Separation qualifications and all computational attempts are retained.

## 2026-10-31T16:30:18.481250+00:00: Aggressive route-builder challenge declared

Claim: the route gate still selects a losing branch on at least one declared aggressive route builder while its alternative avoids defeat. Verdict: OPEN. Method:16 fixed MazeGrower settings (fourlayouts, growth3/6, tier1/5), adaptive and both forced branches, both seats,96 standard games. Manifests route-challenge-a001/b001.json and proof99. This is development evidence with all conditions retained; no pool-C feedback enters the rule or matrix.

## 2026-10-31T16:31:54.204588+00:00: Route selection repair fully audited

Claim and verdict: CONFIRMED: the route gate removes the ten previous adaptive losses on the disclosed24-target development set.

Method and result:48 declared games; route_adaptive: 40W/8D/0L. All1148 fresh decisions, 24 assignment pairs and48 exact history controls pass, with no bot errors or submitted rejections. Controlled failures: []. Full table: bot_research/experiments/validation/analysis/route_gated_selection/RESULTS.md. Development evidence only; installed bot and pool C unchanged.

## 2026-10-31T16:34:09.207269+00:00: Post-C integrity and tests; route-selector transfer declared

Claim and verdict: CONFIRMED, all903 protected files still match this lane's start, with no added/removed/changed file. The pre-existing1002 missing manifest entries and three old mismatches are unchanged. Existing tests again pass59 run,9 skipped. Receipts: runs/validation/integrity-after-pool-C-001.json and environment-after-pool-C-001.json.

Transfer claim: the unchanged route selector avoids defeat against F38,F39,E20,E27,E29 in standard starts. Verdict: OPEN. Thirty declared games include both forced branches and both seats, with full replay and policy checks. Fortress39 is frozen but still in its owner's regression, not yet recommended. Proof100 and manifest route-transfer-001.json.

## 2026-10-31T16:37:08.151432+00:00: Route selection challenge fully audited

Claim and verdict: CONFIRMED: the declared route-builder matrix contains a selector loss avoided by its alternative fixed branch.

Method and result:96 declared games; route_adaptive: 18W/2D/12L; route_early: 16W/0D/16L; route_growth: 24W/8D/0L. All1974 fresh decisions, 48 assignment pairs and32 exact history controls pass, with no bot errors or submitted rejections. Controlled failures: [{"target": "cash_rank_10_g3_tier1", "selected": "early", "hp_counter_first": [-495, 420], "alternative": "growth", "alternative_outcome": "W", "alternative_hp_counter_first": [800, -40]}, {"target": "cash_rank_10_g6_tier5", "selected": "early", "hp_counter_first": [-180, 320], "alternative": "growth", "alternative_outcome": "D", "alternative_hp_counter_first": [-40, -40]}, {"target": "cash_rank_1_g3_tier1", "selected": "early", "hp_counter_first": [-545, 420], "alternative": "growth", "alternative_outcome": "W", "alternative_hp_counter_first": [800, -40]}, {"target": "cash_rank_1_g6_tier5", "selected": "early", "hp_counter_first": [-40, 440], "alternative": "growth", "alternative_outcome": "D", "alternative_hp_counter_first": [-180, -40]}, {"target": "lead_opening_g3_tier1", "selected": "early", "hp_counter_first": [-495, 420], "alternative": "growth", "alternative_outcome": "W", "alternative_hp_counter_first": [800, -40]}, {"target": "lead_opening_g6_tier5", "selected": "early", "hp_counter_first": [-180, 320], "alternative": "growth", "alternative_outcome": "D", "alternative_hp_counter_first": [-40, -40]}]. Full table: bot_research/experiments/validation/analysis/route_feature_challenge/RESULTS.md. Development evidence only; installed bot and pool C unchanged.

## 2026-10-31T16:38:19.238539+00:00: Common public prefix challenge declared

Claim: two hidden target continuations after identical public histories require opposite choices between the existing early and growth branches. Method:12 declared anonymous-name standard games, full original-engine replay, both-policy fresh regeneration and complete unnormalized observation comparison before rounds1-4. Result: running, verdict OPEN. This is a restricted two-branch statement, not a full-game impossibility claim. Proof and planned conditional matrix bound: bot_research/experiments/validation/analysis/indistinguishable_prefix/PROOF.md.

## 2026-10-31T16:38:52.488684+00:00: Sign and inference cautions for synthesis

Claim: the current defense summary phrase about best_v9e drawing or losing the fortress family on the standard start risks reversing the perspective. Method: refer to the independently checked x158 table in analysis/team_fortress_report_audit/RESULTS.md. Result: best_v9e wins the standard-start fortress comparisons there by5 HP; P5TNUBM draws. Verdict CONFIRMED within x158 only. The new F39 comparison is separate and should be read from its actual results. Economy-worker bootstrap intervals describe resampling its selected opponent/scenario clusters; without a specified sampling population they should not be presented as population confidence in broad superiority. No independent bootstrap audit has yet been performed.

## 2026-10-31T16:41:04.865150+00:00: Route-branch transfer complete

Claim and verdict: CONFIRMED: the unchanged adaptive selector avoids defeat on the five declared transfer targets.

Method and result:30 declared games; route_adaptive: 10W/0D/0L; route_early: 4W/0D/6L; route_growth: 10W/0D/0L. All804 fresh selector decisions and10 complete selected-branch controls agree; all engine/source/data audits pass. These five frozen teammate policies were selected before this30-game transfer matrix. Every target and all three counter modes are retained. The test extends development coverage, without creating held-out evidence or altering the installed bot. The separately reported route-builder challenge exposes losses of this same selector and must be considered alongside this table. The defense worker retains fortress38 as its recommendation and describes fortress39 as a trade-off. Full evidence: bot_research/experiments/validation/analysis/route_selector_transfer/RESULTS.md.

## 2026-10-31T16:42:13.897222+00:00: Route-branch prefix complete

Claim and verdict: CONFIRMED: opposite fixed-branch preferences after identical full public prefixes.

Method and result:12 declared games; route_adaptive: 2W/0D/2L; route_early: 2W/0D/2L; route_growth: 2W/0D/2L. All344 fresh selector decisions and4 complete selected-branch controls agree; all engine/source/data audits pass. The targets share the same P5TNUBM opening with no round-one poke. Baseline continues that policy; flood buys tier1 entries from round4. Public names are held fixed. All ten full-prefix comparisons agree, including the entire observations before rounds1,2,3 and4, without masking names or other fields. Both policies were freshly regenerated on every recorded observation, in addition to the route-selector check. Each deterministic selector that commits to E or G from this common history must lose to one of these two targets. The equal mixture has exact maximin utility0 in this two-by-two W/L game, with win utility+1 and loss utility-1. A third policy, another opening or later adaptation is outside this statement. No impossibility for the full game follows. Full evidence: bot_research/experiments/validation/analysis/indistinguishable_prefix/RESULTS.md.

## 2026-10-31T16:42:49.864692+00:00: Emergency-defense component passes; eight games declared

Claim: after the early strike, a visible-damage trigger can activate defense when the HP-lead trigger remains inactive. Method: independently replay both anonymous-prefix targets to round5, both assignments, compare damage and disabled rules with the actual recorded target submission. Result: against flood, the old branch takes215 damage in round5; the new legal construction takes0, preserving715 HP while the target falls to680. The public no-new-action projection was85 damage and triggers defense. Old round1-4 actions and disabled round5 events agree exactly. Verdict CONFIRMED for the one-round component; full-game claim OPEN. Eight games, including both targets, damage/none and both seats, declared in emergency-prefix-001.json and running. Proof: bot_research/experiments/validation/analysis/emergency_after_strike/PROOF.md.

## 2026-10-31T16:46:32.713972+00:00: Emergency continuation repairs the identical-prefix pair

Claim and verdict: CONFIRMED: the damage trigger preserves the baseline win and repairs the shared-prefix flood loss.

Method: eight declared anonymous-name games, both assignments, unchanged engine. Result: damage 4W, disabled 2W/2L; 314 fresh counter decisions, eight complete replays and six exact previous-trajectory controls pass. Flood outcome changes from -495:420 at round 7 to 715:80 at round 50. Round-five visible damage 85 triggers 20 walls and one gun2, preventing all 215 actual incoming damage that round. Baseline remains 800:740. The third continuation does not contradict the restricted binary commitment proof. Development only; broader transfer remains to be measured. Evidence: bot_research/experiments/validation/analysis/emergency_after_strike/RESULTS.md.

## 2026-10-31T16:49:59.378258+00:00: Report precision and current counter status

Claim: REPORT.md P1 wording "Every copy with HP <= S dies before reaching the base" can be read as asserting death for every late-spawned copy. Method: inspect unchanged combat_tick and simulate_map plus the existing standalone pure-splash proof (analysis/splash_threshold/PROOF.md). Result and verdict: CONFIRMED scope correction. A copy that can reach the base within the 250-tick round is killed first; a later copy may instead be cleared at the end. The immunity conclusion is unchanged. Suggested wording: "No copy with HP <= S reaches the base; arrival-eligible copies die first, while late copies may be cleared." The published pure-splash proof already states the late-copy qualification.

Development update: the emergency continuation repairs the identical-prefix tier1 flood (proof102, 4W versus2W2L disabled) but leaves a delayed tier5 failure unchanged. The lead_opening/growth6/tier5 target still beats it320:-180 at round11. The old HP trigger already starts defense in round5, so the new trigger cannot intervene. The separately declared90-game transfer is finishing; all target conditions and regressions will be retained. No change to final best_v9e or poolC.

## 2026-10-31T16:55:14.192710+00:00: Emergency continuation transfer on 45 prior targets

Claim and verdict: REFUTED: the complete claim of preserving all outcomes and repairing every route-builder loss.

Method: 90 newly declared games, both assignments, compared against all 90 matched old adaptive controls. Result: old 68W/10D/12L, new 74W/10D/6L; transitions {'W->W': 68, 'D->D': 10, 'L->W': 6, 'L->L': 6}; 84 complete histories unchanged. All audits pass: 2434 fresh decisions, 2146 independently reconstructed early calls, 6 emergency activations. Development only; best_v9e unchanged. Evidence: bot_research/experiments/validation/analysis/emergency_transfer/RESULTS.md.

## 2026-10-31T16:59:26.260117+00:00: Complete frozen-delegate transfer declared

Claim: one of the two frozen defender continuations retains every old nonloss and repairs the six delayed-tier5 losses in the full 45-target development union. Method: 180 new games, both continuations, every old target and both assignments, with 180 paired old emergency controls and independently reconstructed public handoffs. The focused six-target matrix is still finishing; both continuations are included regardless of that outcome. Result: running. Verdict OPEN. Source-pinned manifests delegated-transfer-* and analysis/delegated_transfer/PROOF.md record the exact scope. No final-candidate change or held-out claim.

## 2026-10-31T17:03:29.661934+00:00: Frozen defenders after the common counter opening

Claim and verdict: CONFIRMED: at least one frozen delegate wins all six focused target settings.

Method: 36 declared games, three continuations, six focused targets, both assignments. Result: delegated_template: 6W/0D/6L; delegated_econ20: 8W/2D/2L; delegated_fortress38: 12W/0D/0L. All 930 fresh counter decisions, 36 replays, 12 template controls and 12 three-way common-prefix groups agree; no illegal actions or errors. Development only. Evidence: bot_research/experiments/validation/analysis/delegated_defense/RESULTS.md.

## 2026-10-31T17:05:39.117325+00:00: Pool-C reuse and final-choice scope

Claim: repeating pool C for V33C can preserve an independent execution audit, but the stated fallback uses C for candidate selection. Method: read the lead's 16:59 decision note, which reports access to aggregate C tables and promises fallback to best_v9e if V33C regresses there. Result and verdict: CONFIRMED distinction. The fixed development gate and candidate timestamp should remain documented; a later C run must use the unchanged manifest and report every condition. Once C decides the final winner, it is comparison/selection evidence for that winner, not a new untouched assessment. The existing best_v9e C measurement remains valid for that frozen file. Ready to run the requested new frozen file without changing the protocol.

## 2026-10-31T17:06:34.483461+00:00: Thirty-setting timing challenge declared

Claim: the frozen Fortress 38 handoff avoids defeat across the declared thirty timing/defensive-budget settings, and preserves every emergency-template W/D/L outcome. Method: 120 new games, both continuations and assignments, unchanged engine, paired first-four-round histories, fresh policy and independent public handoff checks. Result: running. Verdict OPEN; the two claims will be evaluated separately. Every setting is retained. This is development coverage, with no held-out claim or installed-candidate change. Plan: bot_research/experiments/validation/analysis/delegated_timing/PROOF.md.

## 2026-10-31T17:07:25.269063+00:00: Timing grid data-registration correction

Claim: the first timing manifest set was incomplete. Method: explicit archive audit after its first twelve games. Result and verdict: CONFIRMED; three internally hash-checked JSON inputs were not registered in the manifests. The audit stopped execution. All initial games remain recorded; the identical full grid is now declared as002 with those inputs registered. No policy, condition or selection rule changed. Twelve repeats will be compared with the original complete histories. Details: bot_research/experiments/validation/analysis/delegated_timing/MANIFEST_CORRECTION.md.

## 2026-10-31T17:11:29.899649+00:00: Public-clone challenge declared after components

Claim: at least one of twenty fixed public-clone timing attackers defeats the Fortress 38 continuation in both assignments. Method: eighty declared games, both target continuations and all timing settings; each attacker keeps an independent target instance and only supplies copied public observations. The eight component prefixes passed 64 rounds with exact forecasts, legal actions and original combat agreement. Full-game result pending; verdict OPEN. All forecasts and both policies will be regenerated. Evidence: bot_research/experiments/validation/analysis/delegated_forecaster/PROOF.md.

## 2026-10-31T17:14:17.019340+00:00: Forecast recorder correction, policies unchanged

The first eight declared forecast games passed strict, replay and source/data checks, then forecast auditing failed because isolated_match does not capture forecast_trace. Retained version 001. Version 002 uses the existing forecast_match through a new explicit-data runner, with identical policies and conditions; eight full-history repeat controls will be reported. No full forecast verdict yet: OPEN. Evidence: bot_research/experiments/validation/analysis/delegated_forecaster/TRACE_CORRECTION.md.

## 2026-10-31T17:17:19.826548+00:00: Timing challenge complete

Claim and verdict: no defeats CONFIRMED; no W/D/L regressions CONFIRMED. Method: 120 games, thirty fixed timing/defensive-budget settings, two continuations and both assignments. Result: template 60W/0D/0L, Fortress38 60W/0D/0L; 2504 fresh decisions, all independent handoffs and sixty identical first-four-round prefixes pass. Twelve initial games with incomplete data registration are retained and exactly reproduced by the corrected manifest set. Development only. Evidence: bot_research/experiments/validation/analysis/delegated_timing/RESULTS.md.

## 2026-10-31T17:17:26.873386+00:00: Forced-early response to the growth-branch failure declared

Claim: forcing the already implemented early branch repairs at least one public-clone loss with no W/D/L regression across the fixed twenty-setting family. Method: same timing settings and both assignments, with matching mode=early private target models; forty games after four component prefixes. The initial eight captured adaptive games all select growth and have no Fortress handoff, so defensive continuation strength is not exercised there. This is a response to observed failure, not held-out selection. Result pending; verdict OPEN. Evidence: bot_research/experiments/validation/analysis/forced_early_forecaster/PROOF.md.

## 2026-10-31T17:22:37.168140+00:00: Report wording and C scope review

Claim: P1 says every HP<=S copy dies. Verdict: REFUTED literally, with its zero-base-damage conclusion unchanged. Late-born copies may instead be cleared. Method: unchanged combat source and existing splash-threshold proof. Suggested exact wording and the scope of any later C-based fallback are in bot_research/experiments/validation/reviews/report-1724-review.md. No report-owner file edited.

## 2026-10-31T17:28:05.760207+00:00: Complete frozen-delegate transfer

Claim and verdict: CONFIRMED: at least one tested continuation preserves every old nonloss and turns all six old losses into wins.

Method: 180 declared games, two continuations on all 45 prior targets in both assignments; paired with 90 old controls. Result: econ20 70W/18D/2L, 4 improvements and 8 regressions; fortress38 80W/10D/0L, 6 improvements and 0 regressions. All 3426 fresh decisions, 3426 independently reconstructed handoff calls and 180 identical first-four-round prefixes pass. Development only. Evidence: bot_research/experiments/validation/analysis/delegated_transfer/RESULTS.md.

## 2026-10-31T17:29:15.539571+00:00: Recent teammate transfer and branch ablation declared

Claim: the adaptive Fortress38 continuation avoids defeat against all six fixed recent targets, both assignments. Method: 36 games including forced early and growth controls against Fortress40, Fortress41, V33C, guarded econ29, best_v9e and P5TNUBM; compare common prefixes and complete chosen-branch histories. Result pending, verdict OPEN. This is development work and leaves best.py unchanged. Evidence: bot_research/experiments/validation/analysis/recent_transfer/PROOF.md.

## 2026-10-31T17:33:34.729194+00:00: Fixed-policy counter-cycle test declared

Claim: frozen best_v9e, the Fortress38 adaptive counter and its round3/tier2 public-clone attacker form a directed strict cycle. Method: eight new games (missing edge and measured self-play, both assignments), four reused audited rows, with C keeping exactly the same D model on every edge. Result pending, verdict OPEN. A conditional uniform-mixture proof is stated only for the resulting finite table. Evidence: bot_research/experiments/validation/analysis/latest_counter_game/PROOF.md.

## 2026-10-31T17:35:00.597565+00:00: Display-name grouping audit

Claim and verdict: CONFIRMED, the older local generic summary pairs by displayed IDs, while strict condition identity includes full specs. A census of 225 top-level development manifests found 6 with one ID assigned distinct specifications. These are listed in bot_research/experiments/validation/reviews/display-name-pairing-audit-001.json; recent-transfer deliberately uses a common displayed counter name for equal observations. Its final publisher independently groups full specifications and all18assignment pairs. No game outcome or strict unique-condition accounting changes. The generic abbreviated Markdown table for those campaigns is superseded.

## 2026-10-31T17:40:45.442986+00:00: Defended round-three opening search declared

Claim: one of twelve existing wall layouts plus one or two affordable turrets can stop four tier2 copies in round three while preserving a round-four tier4 purchase. Method: exact budget identity and original-combat enumeration, then selected original-engine fixtures. Result pending, verdict OPEN. This is a component question, not a strength claim. Gun targeting is single-target; coverage alone is insufficient. Search will use core28 only after its current validation finalizer exits. Evidence: bot_research/experiments/validation/analysis/guarded_opening_budget/PROOF.md.

## 2026-10-31T17:43:53.972993+00:00: Recent teammate branch comparison complete

Claim and verdict: CONFIRMED: adaptive avoids defeat on all six declared recent targets in both assignments.

Method: all36declared games, six targets x three modes x two assignments. Result: adaptive 12W/0D/0L; early 12W/0D/0L; growth 6W/0D/6L. All1552fresh decisions and independent handoffs pass; twelve common-prefix groups and twelve exact chosen-branch controls agree. Another fixed branch improves0adaptive conditions; both fixed branches lose in0. Development only. Complete specification-aware table: bot_research/experiments/validation/analysis/recent_transfer/RESULTS.md.

## 2026-10-31T17:45:56.080536+00:00: Forced early branch challenge complete

Claim and verdict: CONFIRMED, at least one public-clone loss repaired with no W/D/L regression; eliminating every target loss is REFUTED. Method: forty new games against correctly updated public-clone models, paired with all forty adaptive controls; identical first-three-round histories. Result: adaptive 0W/2D/38L, early 6W/10D/24L, 14 improvements, 0 regressions. All replay, exact forecast, fresh-policy, legality and independent handoff checks pass. Development ablation, not reserved validation. Evidence: bot_research/experiments/validation/analysis/forced_early_forecaster/RESULTS.md.

## 2026-10-31T17:46:08.258178+00:00: Public-clone timing challenge complete

Claim and verdict: CONFIRMED, at least one declared public-clone timing setting defeats the Fortress 38 continuation in both assignments. Method: eighty games with both target continuations, all twenty settings, unchanged engine and exact public forecasts. Result from forecaster perspective: template 38W/2D/0L, Fortress38 38W/2D/0L. All 3508 fresh forecaster decisions and 3508 fresh target decisions agree, with exact original incoming combat and independent handoff checks. Targeted development only. Evidence: bot_research/experiments/validation/analysis/delegated_forecaster/RESULTS.md.

## 2026-10-31T17:47:26.500425+00:00: Defended-opening budget component complete

Claim and verdict: REFUTED, existence within the declared finite map family. Method: all 743 budget-feasible maps checked by original combat after the proved cash identity. Result: 0 zero-damage maps; 0 selected original-engine fixtures and sixteen extra roster components each. Full-game strength remains OPEN. Evidence: bot_research/experiments/validation/analysis/guarded_opening_budget/RESULTS.md.

## 2026-10-31T17:48:03.055636+00:00: Earlier-wall budget search declared

Claim: moving a fixed wall layout to round one or two permits a zero-damage four-tier2 defense and a round-four tier4 purchase. Method: exact income recurrence, 24 original-engine opening fixtures, all one/two-turret maps on twelve registered layouts, then original combat and selected full action fixtures. Verdict OPEN. Previous round-three-only existence was REFUTED on all743budget-feasible maps. Evidence: bot_research/experiments/validation/analysis/guarded_opening_wall_timing/PROOF.md.

## 2026-10-31T17:48:14.854687+00:00: Fixed three-policy game complete

Claim and verdict: CONFIRMED: the specified cycle B>C>D>B holds in the paired recorded game.

Method: eight new and four reused audited games, both assignments of all edges and measured self-play. Result: payoff rows in B,C,D order are [[0, 1, -1], [-1, 0, 1], [1, -1, 0]]; all 632 new decisions regenerated. The clone retains its same D model against every policy. Uniform mixture has exact value0 only in this finite table. Evidence: bot_research/experiments/validation/analysis/latest_counter_game/RESULTS.md.

## 2026-10-31T17:48:43.131230+00:00: New fortress counter transfer declared

Claims: reproduce A/B Fortress41 margins and test whether either defeats best_v9e, V33C or the adaptive delegated counter in both assignments. Method: all24games, six defenders, two fixed schedules, both seats, original replay and fresh regeneration of both policies. Verdict OPEN. The schedules come from the defense lane; their original fortress outcomes are development controls. Evidence: bot_research/experiments/validation/analysis/bait_guard_transfer/PROOF.md.

## 2026-10-31T17:49:26.648460+00:00: Earlier-wall budget component complete

Claim and verdict: CONFIRMED, finite existence. All 24595 budget-feasible maps checked by original combat; 9 successes and 8 original-engine witness fixtures. The first-ranked witness builds 20 lead walls in round one, splash(1,3) in round three, and reaches round four with 14 factories and267gold. It stops the tested tier2 counts but leaks every tested tier3 copy. Full-game strength remains OPEN. Evidence: bot_research/experiments/validation/analysis/guarded_opening_wall_timing/RESULTS.md.

## 2026-10-31T17:50:21.964673+00:00: Early-wall policy development declared

Claims: guard00 beats its updated round-three/tier2 public clone; at least one of eight fixed witnesses avoids loss against all four teammate targets. Method:16component prefixes followed by80declared games, including correct private clone models and both assignments. Verdict OPEN. No existing policy or best.py is changed. Evidence: bot_research/experiments/validation/analysis/early_wall_policy/PROOF.md.

## 2026-10-31T17:51:06.499493+00:00: Completed primary-target partitions of bait/guard transfer

Claim and verdict: CONFIRMED for these eight completed conditions, both unchanged A/B schedules beat frozen best_v9e and fixed V33C in both assignments. Best_v9e ends85:734 against A and505:755 against B. The full24-game declaration remains in progress; these are checked partitions, not a final aggregate. Strict, original replay, data and all fresh both-policy decisions pass for partitions01and02. Lead can inspect bait-guard-transfer-01-001-summary.json and -02-001-summary.json under runs/validation. No change to the predeclared V33C gate or reserved pool is implied.

## 2026-10-31T17:52:29.268585+00:00: Bait/guard transfer complete

Claim and verdict: fortress margin reproduction CONFIRMED; transfer to at least one declared primary target CONFIRMED. All24games and 2064 fresh decisions pass independent replay, source, legality and action checks. Both-seat losses occur in best_v9e/bait_guard_A, best_v9e/bait_guard_B, V33C/bait_guard_A, V33C/bait_guard_B. Exact complete table: bot_research/experiments/validation/analysis/bait_guard_transfer/RESULTS.md. These are development results.

## 2026-10-31T17:56:45.531333+00:00: Early-wall witness transfer declared

Claim: guard00 has no W/D/L regression and at least one improvement relative to the adaptive delegated counter over all90old conditions; separately no loss against the two bait/guard schedules and two delegated branches. Method: all98newgames, both assignments, original engine and fresh-policy checks. Its eight recorded teammate wins and two clone draws motivate this development expansion; no holdout claim. Result pending, verdict OPEN. Evidence: bot_research/experiments/validation/analysis/early_wall_transfer/PROOF.md.

## 2026-10-31T17:59:04.099458+00:00: Early-wall extended clone challenge declared

Claim: guard00 avoids every loss on the fixed twenty-setting public-clone timing grid; separately it improves on the forced-early delegated target without a single matched regression. Method:40newgames and80explicitoldcontrols; private target models are correctly updated for each policy. A repeated known draw is labeled reproducibility only. Eight new prefix components gate the full games. Result pending, verdict OPEN. Evidence: bot_research/experiments/validation/analysis/early_wall_forecaster/PROOF.md.

## 2026-10-31T18:03:37.782344+00:00: Prepared best_v9f pool C execution audit

Read the lead's17:58freeze and gate result. The unchanged72condition C protocol is now prospectively declared for SHA 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580; it waits for the exact installed bytes and a free core. Claim: complete original-engine and fresh-entry-point audit, with every paired old/new transition reported. Verdict OPEN. C has already been disclosed and the declared fallback selects using C, so this will be labeled reused-pool evaluation. Please keep installed candidate bytes fixed through the replay and fresh-entry checks; the completion note will identify the fallback condition, if any. No C games of9f have run in this lane at declaration. Evidence: bot_research/experiments/validation/analysis/reused_c_validation/PROOF.md.

## 2026-10-31T18:10:41.003455+00:00: Report wording counterexample and scope follow-up

Claim and verdict: literal P1 all-copies-die assertion REFUTED; zero-damage implication unaffected. A legal nine-round original-engine fixture buys250tier1 against one splash, producing249kills,1living clearance,0damage. The last copy has10HP at tick249. Proof118: analysis/late_copy_cleanup/PROOF.md and verification/result.json. Full argument and suggested report wording, plus the best_v9e-only scope of the1104entry-point checks: reviews/report-1811-review.md. No report-owner file changed.

## 2026-10-31T18:12:23.792567+00:00: Terminal reserve D declared before candidate execution

Claim: independently evaluate the final selected best.py on96conditions,16new parameter settings x standard and two legal continuation starts x bothseats. Verdict OPEN. The manifest terminal_holdout_manifest.json is immutable, SHA9267cb4367f21dc0a572594c3523a466769ef1ea3185beb4dd94d632270e07b7; no candidate or opponent policy was called. Shape and original-prefix legality pass. The reserve is not for choosing candidates. Planned start is no earlier than23:00Z after the lead's final selection; keep the final bytes and dependencies fixed through completion. Please do not tune or select on D. Exact overlap will be audited against the team records at campaign start; these are known policy families, not unseen families. Protocol proof119: analysis/terminal_reserved_validation/PROOF.md.

## 2026-10-31T18:13:47.226453+00:00: Fixed-schedule bait removal declared

Claims: deleting only the three round-two tier1 purchases repairs at least one prior defender loss; separately, at least one defender avoids all four former A/B losses. Method:24newgames on the same six defenders and both assignments, paired with all24original audited controls. All other requested actions stay identical and saved gold is not spent. Any new illegality is retained. The100round schedule comparison passes without calling any defender. Verdict OPEN; queued behind primary validation. Protocol: analysis/bait_removal/PROOF.md.

## 2026-10-31T18:17:58.495805+00:00: Early-wall full matrix complete

Claim and verdict: guard00 strict clone win REFUTED; existence of a fixed witness with no teammate loss CONFIRMED. All80games, 3972 fresh decisions and 800 fresh forecasts pass the original-engine, source, legality and observation checks. Nonlosing witnesses: guard00. Filtered proposals: 0; engine rejections and bot errors: zero. Full condition table and timing: bot_research/experiments/validation/analysis/early_wall_policy/RESULTS.md. These are development results; the clone setting is only round3/tier2.

## 2026-10-31T18:20:09.510811+00:00: To the lead, final validation readiness and scope corrections

The unchanged C audit for best_v9f is queued on core28 and starts when the exact installed hash is 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580. All early-wall policy gates have now passed. Keep those installed bytes fixed through fresh direct/factory checks. New terminal pool D was declared at18:11:52Z, SHA9267cb4367f21dc0a572594c3523a466769ef1ea3185beb4dd94d632270e07b7,96conditions. Its prospective protocol and prepared clock-gated runner are in analysis/terminal_reserved_validation. It has no candidate results and will run only after23:00UTC and final selection, strictly report-only. C is reused selection evidence under the16:59fallback; D is reserved to independently report the final selection.

Review report-1811-review.md has an executed legal counterexample to the literal statement that every copy dies under a sufficient splash bound:250tier1 bought in round9,249killed,oneclearedalive,zero damage. The no-base-damage theorem remains correct with the arrival-eligibility qualification. The C paragraph should also distinguish the72replayed P5TNUBM games from best_v9e-only1104fresh direct/factory calls.

New counter transfer: early_wall_guard:@make?witness="guard00" defeats all four current teammates in both seats; best_v9e/V33C/P5TNUBM margin+30,Fortress41+40. It draws its matching r3tier2 clone800:800, with zero attack purchases by that clone. Seven other component-valid guards lose all teammate games, so the opening certificate alone is insufficient. Complete80-game evidence: analysis/early_wall_policy/RESULTS.md; broad98-game transfer and40updated-clone games are running.

## 2026-10-31T18:26:37.564435+00:00: Early-wall round-four attack ablation declared

Claim: omitting tier4 repairs the hp_handoff loss; separately, at least one of no purchase or tier3 has no W/D/L regression and at least one improvement over all14fixedcontrols. Method:28newgames against fourteammates and hp_handoff/adaptive/early counters, bothassignments. The existing factory loop spends savings and Fortress38 still begins at round5. Verdict OPEN. Source and JSON pinned before component or full-game calls. Protocol: analysis/early_wall_attack_ablation/PROOF.md. Queued after the current comparison and bait-removal ablation; reserved validation retains priority.

## 2026-10-31T18:30:04.481073+00:00: Freeze review and pending C hash amendment

Claim and verdict: CONFIRMED, the initial freeze has three failed option-exercise assertions; revised-suite success remains OPEN. Lead RUN_STATUS 18:26 independently identifies stale fixtures and is replacing them. Standard/scenario action equality and harness checks passed. The announced doc correction changes the frozen hash. I archived the original source, checked equal non-docstring AST against the proposed draft, and stopped the exact-old-hash wait before any C candidate game. I will pin the actual installed file in a prospective amendment and resume C; no action is required from the lead. Review: bot_research/experiments/validation/reviews/freeze-1832-review.md.

## 2026-10-31T18:32:24.303546+00:00: Early-wall transfer complete

Claim and verdict: paired strict improvement REFUTED, additional-counter no-loss REFUTED. On90old conditions: delegated 80W/10D/0L, guard00 86W/0D/4L, 8 improvements and 4 regressions. Additional8games: 2W/4D/2L. All 5248 fresh decisions pass. Complete target table, losses and timing: bot_research/experiments/validation/analysis/early_wall_transfer/RESULTS.md.

## 2026-10-31T18:34:13.857030+00:00: Five-policy extension declared

Claim: the old uniform B/C/D mixture remains nonnegative against early-wall guard00 G and HP-triggered grower H; separately, G weakly dominates D on the five-policy table. Verdict OPEN. Ten new games and twenty explicitly reused games complete all pairings and self-play in both seats, retaining C's same private D model. This is development only. Conditional rational certificate and exact definitions: bot_research/experiments/validation/analysis/extended_counter_game/PROOF.md.

## 2026-10-31T18:35:39.856612+00:00: Bait-removal ablation complete

Claim and verdict: at least one previous defender loss repaired CONFIRMED; at least one formerly all-losing defender avoids four losses CONFIRMED. All24newgames,24controls,2064fresh decisions and all original-engine/source/legality checks pass. Transitions {'L->W': 10, 'L->L': 6, 'W->W': 6, 'L->D': 2}. Full table and per-round causal diagnostics: bot_research/experiments/validation/analysis/bait_removal/RESULTS.md. Only the three round-two tier1 purchases were removed, with no replacement spending. This includes bounty and direct-damage effects and does not isolate psychological bait.

## 2026-10-31T18:36:56.434196+00:00: Original freeze declaration retained

The lead's18:29note explicitly drops the proposed docstring edit and retains original SHA36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580. Accordingly no C amendment was issued; declaration001 remains unchanged and its installation wait has resumed on core28. No C game occurred during the stopped wait. The earlier proposed-amendment note is superseded. Verification of all original source pins passes.

## 2026-10-31T18:43:11.260314+00:00: Lead-requested best_v9f counter transfer declared

Claim: both fixed guarded round-four settings still win against frozen best_v9f in both seats. Verdict OPEN. Four games use the exact prior half/full-budget specifications, with all parameters unchanged; installed best.py and frozen best_v9f match SHA 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580 at declaration. The campaign is queued after reused C and lossless archival on core28. Eight-round components, complete replays, both fresh policies, public-trigger checks and old archived controls are required. Scope and proof: bot_research/experiments/validation/analysis/guarded_round4_best9f/PROOF.md.

## 2026-10-31T18:45:35.764990+00:00: best.py changed during reused C entry-point verification

Claim: all requested best_v9f verification is complete. Verdict REFUTED at this checkpoint. The 72 original games and all replays completed before the change, but best.py was replaced at 2026-10-31T18:44:53.656747+00:00 with best_v9e SHA70ef8eab... while the direct/factory audit was still running. Eighteen entry audits passed, one encountered the change after starting, and 53 subsequent audits rejected the source hash. All54 failure records are retained. The only current source mismatch is best.py; frozen best_v9f and all original game archives remain intact. No original game is relabeled or rerun. I will complete a separately named archived-entry verification of the frozen9f bytes, then publish the entire incident and the original C outcomes. Pool D remains untouched. The lead should retain its final selected installation unchanged during D and its entry-point checks. Receipt: bot_research/experiments/validation/analysis/reused_c_validation/verification/installation_change_1845.json.

## 2026-10-31T18:50:36.237826+00:00: Early-wall matching-model grid complete

Claim and verdict: no loss REFUTED; paired improvement over forced early CONFIRMED. Method: forty new games on the fixed twenty-setting timing grid, with correctly updated target models and eighty explicit old controls. Result: guard 6W/26D/8L, forced early 6W/10D/24L, adaptive 0W/2D/38L; 16 improvements and 0 regressions from forced early. All 4000 fresh calls, 2000 forecast checks, original-engine replays and source/data audits pass; two known draw repeats agree. Development evidence. Full table: bot_research/experiments/validation/analysis/early_wall_forecaster/RESULTS.md.

## 2026-10-31T18:50:56.352842+00:00: Early-wall round-four ablation complete

Claim and verdict: no-purchase repairs both hp_handoff losses REFUTED; one tested variant improves all fourteen controls in W/D/L order REFUTED. All28newgames,14controls,2800fresh calls and all source/data/legality/replay checks pass. Per-variant results: {'none': {'L': 14}, 'tier3': {'L': 12, 'W': 2}}. 0 filtered proposals. Full paired table and histories: bot_research/experiments/validation/analysis/early_wall_attack_ablation/RESULTS.md.

## 2026-10-31T18:51:35.655108+00:00: Public-roster-gated follow-up declared

Claim: at least one fixed extra round-five package repairs both early-wall losses against lead8 and P5M_poke0 without regressions on the other six conditions. Method: three packages, five fixed opponents, both assignments, ten explicit old controls, component and full-history checks. The extra attack triggers only when the opponent has no active public roster. Verdict: OPEN. Protocol and source pins were written before any new policy execution: analysis/early_wall_followup/PROOF.md. This targeted development does not use pool D.

## 2026-10-31T18:52:19.112061+00:00: best_v9f reused C audit complete

Claim and verdict: CONFIRMED, all72game conditions, original-engine replays and separately recovered archival fresh-entry checks pass for SHA 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580. The predeclared fallback is TRIGGERED: 4 new losses replace old wins/draws. Full W/D/L transitions: {'W->W': 64, 'D->L': 2, 'D->D': 4, 'W->L': 2}. 1088 fresh calls per direct/factory entry, 120 correctly skipped prefix rounds; zero game errors/rejections/source drift during games. The lead restored9e at18:44:53 while installed-entry checks ran:18passed54failed audit attempts are retained. All72archival checks now pass for the unchanged9fbytes and dependencies; this does not assert9f is installed. C is selection evidence, not untouched final validation. Complete conditions and metrics: bot_research/experiments/validation/analysis/reused_c_validation/RESULTS.md.

## 2026-10-31T18:54:30.421848+00:00: Five-policy extension complete

Claim and verdict: H1 old uniform mixture guarantee REFUTED; H2 G weakly dominates D REFUTED. Old mixture payoffs against G/H: -2/3, -2/3. Ten new and twenty reused games, all fifteen assignment pairs identical, 680 fresh new decisions checked. Exact finite maximin weights in B,C,D,G,H order: ['0', '0', '0', '0', '1']. All claims are restricted to this fixed development table: bot_research/experiments/validation/analysis/extended_counter_game/RESULTS.md.

## 2026-10-31T18:55:52.947126+00:00: Timing-wrapper accounting correction

Claim and verdict: CONFIRMED on144completedCconditions. Old candidate_calls fields include prefix turns; fresh-entry counts were correct. best_v9e has1224wrapper/120prefix/1104policycalls, best_v9f1208/120/1088. Original seconds include prefix overhead. Complete data and per-round audit reconciled; wrong-count fixture rejected. Dpublisher corrected before candidate freeze, with no Dexecution. Existing results preserved with timing addenda. See bot_research/experiments/validation/analysis/decision_timing_accounting/RESULTS.md.

## 2026-10-31T18:56:56.617332+00:00: Fixed guarded round-four check against best_v9f complete

Claim and verdict: CONFIRMED, both unchanged half/full-budget settings still defeat best_v9f in both seats. Candidate outcomes {'L': 4}; exact four rows: bot_research/experiments/validation/analysis/guarded_round4_best9f/RESULTS.md. All four games pass strict/replay/source/data and 400 fresh calls plus 200 counter trigger rechecks. Two identical assignment pairs, 48 filtered proposals, zero submitted rejections or bot errors. The four old best_v9e losses remain separately archived controls. This answers the lead's 18:40Z request and is development evidence.

## 2026-10-31T18:57:01.920317+00:00: Fixed H targeted clone challenge declared

Claim: H has no loss on twelve matching-model timing settings, both assignments. Method:24newgames, four prefix gates, six fixed round/tier pairs, both defense_first values. H is precisely lead8/deadline12 from the five-policy table. Outcome and prediction hypotheses remain OPEN. This deliberately tests the limitation of H's finite-table maximin certificate; it is development, not unseen validation. Protocol: bot_research/experiments/validation/analysis/hp_handoff_forecaster/PROOF.md.

## 2026-10-31T19:02:17.945803+00:00: Separation-audit inputs preserved

Claim and verdict: CONFIRMED, all 802 input versions named by the completed C parameter and scenario audits are retained with exact decompressed hashes. Seven older append-only prefixes were recovered. Five component checks and the complete 802-blob verification pass; compressed size is 7,979,129 bytes. The D pipeline now requires the same preservation check, with its frozen manifest and inputs unchanged and no D policy calls. This preserves evidence without strengthening overlap or independence claims. See bot_research/experiments/validation/analysis/audit_input_snapshots/RESULTS.md.

## 2026-10-31T19:03:41.612311+00:00: Sixth fixed policy declared

Claim H1: I weakly improves on C against all five prior policies, with a strict improvement. Verdict OPEN. I is the round-three tier2 attacker with a fixed private H model; C has the same attack parameters but a fixed private D model. The two I-H wins are known and explicitly reused. Ten new games complete the six-policy table, with thirty-two old records. This is a selected development test. See bot_research/experiments/validation/analysis/six_policy_game/PROOF.md.

## 2026-10-31T19:03:52.528721+00:00: Public-roster follow-up complete

Claim and verdict: a package repairs both targeted losses without other regressions REFUTED; the eighteen non-targeted histories stay unchanged CONFIRMED. All thirty games, ten controls and 2672 freshly regenerated policy calls pass the complete checks, with 0 filtered proposals. Per-package W/D/L: {'one_tier3': {'L': 6, 'W': 4}, 'two_tier3': {'L': 6, 'W': 4}, 'one_tier4': {'L': 6, 'W': 4}}. Full outcomes and scope: bot_research/experiments/validation/analysis/early_wall_followup/RESULTS.md.

## 2026-10-31T19:09:02.720341+00:00: Response to the lead's 19:04Z candidate schedule

The af2g R13 selection rule and 22:15Z installation target are read. No current worker-3 game or fresh-action check reads bots/best.py; both running counter studies use frozen policy modules. Pool D remains untouched and undeclared, and will use the final installed hash after the explicit selection note, no earlier than 23:00Z. Preserve that installed hash through all 96 games and the subsequent entry-point checks. The earlier best_v9f archival recovery has completed: 72 archived-source entry checks pass, with 1088 actual decisions and 120 prescribed-prefix turns. Pool C is selection evidence for all candidates chosen using it.

## 2026-10-31T19:09:04.520586+00:00: Six-policy table complete

Claim H1, I weakly improves on C across the previous five policies: CONFIRMED. Differences I minus C are [0, 0, 0, 0, 2]. Ten new games and thirty-two reused games form twenty-one identical assignment pairs; 848 new decisions pass fresh regeneration. Pure nonnegative rows: []. Exact finite maximin weights in B,C,D,G,H,I order: ['0', '0', '0', '1/3', '1/3', '1/3']. The private model is the only specification difference between C and I. All outcomes and limits: bot_research/experiments/validation/analysis/six_policy_game/RESULTS.md.

## 2026-10-31T19:09:35.114445+00:00: Fixed H clone challenge complete

Claim and verdict: H avoids every declared timing attack REFUTED. H scores{'L': 24} on24games. All2400external decisions and1200additional prediction/combat checks pass. Twelve measured assignment pairs, all outcomes and actual purchase counts retained. This does not change the earlier five-policy certificate; the attackers are new selected development opponents. See bot_research/experiments/validation/analysis/hp_handoff_forecaster/RESULTS.md.

## 2026-10-31T19:10:20.114806+00:00: Protected-file and classified artifact checkpoint

Claim and verdict: CONFIRMED, all 903 outside-research entries match the starting inventory, including the pre-existing environment. The original 1002 missing manifest entries (1000 historical game paths and two metadata paths) and three original mismatches remain unchanged. The received test suite runs 59 tests, with nine skipped and no failures.

The first lexical scan found one outer traceback with a project-root path and one frozen source line containing generic forbidden-root tokens. The traceback was redacted on exactly one line, with before/after hashes retained; failure counts and diagnostics remain. An AST check and exact source/line hashes justify classifying the generic guard separately. The full rerun finds no concrete local-path match. Owned bytes 2816642884; free bytes 150637019136. Evidence: runs/validation/integrity-mid-1905.json, artifacts-mid-1905.json, artifacts-mid-1908.json, existing-tests-mid-1908.log; experiments/validation/analysis/artifact_path_audit/PROOF.md and verification/redaction.json. Earlier failed scan retained.

## 2026-10-31T19:11:45.525042+00:00: Shared-prefix response selection declared

Protocol130 tests a public-observation selector J against B,C,D,G,H,I and itself, fourteen standard games. J runs H and I on the shared first move; at round two it selects H for an opponent with at least twenty walls and an empty roster, otherwise I. The criterion was selected after inspecting the six-policy table. H1 is nonloss against G,H,I and a positive exact uniform-mixture payoff; H2 is nonloss across all prior six. Both are OPEN until components and games complete. Proof: experiments/validation/analysis/shared_prefix_response/PROOF.md. No current work reads bots/best.py.

## 2026-10-31T19:14:45.114719+00:00: Focused report review and fresh integrity evidence

Review: experiments/validation/reviews/report-1915-review.md, with a retained source snapshot. Pool C selection disclosure and P1 arrival qualification are correct. Update the archived-9f recovery from pending to complete; label C timings as wrapper timings (actual policy calls 1104/1088); keep the 19:04Z candidate decision pending until the final selection note. The latest 903-entry protected inventory is unchanged and 59 tests pass with nine skipped. The exact missing-data breakdown is 999 game JSONL files plus data/games/manifest.json and two metadata paths, still 1002 total. New finite-game and matching-clone counter results are complete; the shared-prefix selector experiment is pending. No lead-owned file was changed.

## 2026-10-31T19:18:38.832516+00:00: af2g fixed development counters declared

H1 no regression against five old counters; H2 repair at least one previous loss. Both OPEN. Ten standard games, both seats, compare frozen best_v9f with passive_until=null against D,G,H,I and the half-budget guarded round-four striker. Ten old best_v9e controls are restored and hash checked. The full protocol is experiments/validation/analysis/af2g_fixed_counters/PROOF.md. This does not use pool D or installed best.py, and does not replace R13.

## 2026-10-31T19:19:24.074714+00:00: Replay storage checkpoint

Claim and verdict: CONFIRMED, wave11 preserves all selected historical replay bytes under SHA256-verified gzip round trips. Forty complete historical campaigns contain303947290rawbytes; compaction saves295449160bytes. The initial helper stopped on an already-existing archive. Its assertion failure remains recorded, and a separate resume helper verifies and reuses identical archives rather than overwriting them. Evidence: runs/validation/archived-wave11-replays-001.json, its per-file journal and archive-wave11-log-redaction.json. Only a concrete local path in the original traceback was redacted. A few control replays for protocol131 were subsequently restored and hash checked; these are declared in its manifest.

## 2026-10-31T19:21:38.413100+00:00: Public wall-signal attack declared

H1: K20 wins against J on the exact H-response history. H2: that outcome exceeds K19-J and K20-I. Both OPEN. Two fixed timing attackers replace only the first move with nineteen or twenty cells of guard00, then call the unchanged private-H timing rule. Twelve games include both fixed-response controls and both seats. Components, full replays, fresh decisions and forecast traces are required. Protocol: experiments/validation/analysis/wall_signal_response/PROOF.md. This is deliberately targeted development and does not use pool D or installed best.py.

## 2026-10-31T19:23:05.328199+00:00: af2g fixed-counter development check complete

H1 no regression: CONFIRMED; H2 repair at least one old loss: REFUTED. Ten new outcomes {'L': 8, 'W': 2}, old-to-new transitions {'L->L': 8, 'W->W': 2}. All ten old controls are replayed, and all 864 new external decisions regenerate exactly. Five identical assignment pairs, no errors or submitted rejections. Details: experiments/validation/analysis/af2g_fixed_counters/RESULTS.md. This is a selected development screen, not pool D or the complete R13 gate; no job reads installed best.py.

## 2026-10-31T19:24:34.079194+00:00: Shared-prefix selector complete

H1 nonloss against G,H,I with positive uniform-mixture payoff: CONFIRMED; exact payoff 2/3. H2 nonloss against all six prior policies: REFUTED. Fourteen new games, seven identical assignment pairs, 1400 fresh external calls and 700 exact standalone-response calls. Scores J against B,C,D,G,H,I,J: [-1, 0, 1, 1, 1, 0, 0]. Details: experiments/validation/analysis/shared_prefix_response/RESULTS.md. The criterion was selected from public first-round geometry after the six-policy table, so this is a targeted adaptive counter, not held-out evidence.

## 2026-10-31T19:26:11.343070+00:00: Seven-policy exact reanalysis declared

Protocol133 reuses the complete 42-game six-policy receipt and fourteen-game selector receipt. It checks the former mixture against J and proposes a new exact certificate, with independent rational inequality checks. This is a post-outcome analysis, not a new empirical test. All 56 cases and parent inputs are retained and hash checked. Proof: experiments/validation/analysis/seven_policy_game/PROOF.md.

## 2026-10-31T19:26:16.644411+00:00: Seven-policy arithmetic complete

Claim and verdict: the old G/H/I uniform guarantee extends to J: REFUTED; its payoff is -2/3. An exact value-zero certificate for the enlarged finite table is CONFIRMED, with weights ['1/3', '0', '0', '0', '1/3', '0', '1/3'] in B,C,D,G,H,I,J order. No pure nonnegative row exists. All 56 games are reused; no new policy call was made. Parent inputs, including compressed replays, retain their original hashes. See experiments/validation/analysis/seven_policy_game/RESULTS.md. This is restricted to the measured finite table.

## 2026-10-31T19:28:20.570685+00:00: Public wall-signal attack complete

H1, K20 wins against J on the exact H-response history: REFUTED. H2, it exceeds K19-J and K20-I: REFUTED. Twelve new games, six identical assignment pairs, 708 fresh external decisions and 354 forecast checks pass. K20-J equals K20-H: True; K19-J equals K19-I: True. Complete outcomes and limitations: experiments/validation/analysis/wall_signal_response/RESULTS.md. This deliberately selected signal attack uses no pool D data.

## 2026-10-31T19:28:27.121217+00:00: Delayed wall-signal grid declared

H1 a twenty-wall setting beats J on the exact H-control history; H2 such a win exceeds the I-control outcome. Both OPEN. Four round/tier settings, three targets, both assignments, 24 new games. This follows the nineteen-wall tier2 losses and the earlier wall-free matching-H wins; the twenty-wall tier2 result is still pending. All sources fixed before calls. See experiments/validation/analysis/wall_signal_delayed/PROOF.md. No installed best.py or pool D use.

## 2026-10-31T19:29:35.399684+00:00: Wall-signal result clarification and evidence index refresh

Both original signal-attack hypotheses are REFUTED. K20 loses to J/H and draws I, so selecting H helps J on these histories. A clarification disambiguates the original result paragraph about the proposed failure mechanism. The delayed-grid declaration retained a stale running-status sentence: the parent result completed at 2026-10-31T19:28:20.570685+00:00, before the declaration at 2026-10-31T19:28:27.121217+00:00; its outcomes were read only in the subsequent status check. No new setting or source changed. Both notes and hashes are retained. EVIDENCE_INDEX.md now leads with C selection disclosure, the pending af2g gate, untouched D, completed fixed counters and the seven-policy certificate.

## 2026-10-31T19:33:07.253779+00:00: Follow-up report review and terminal logging readiness

Claim: the validation passages track the latest completed evidence and source-freeze plan. Method: retain the current report snapshot and compare its statements with the 19:04Z R13 note and completed worker-3 receipts. Result: C selection disclosure, archival repair and timing accounting are now incorporated. A remaining sentence promising the 18:44:53Z bytes unchanged through D conflicts with the later pending af2g installation. Verdict: OPEN until that sentence is qualified and the actual final-selection hash is recorded. Review: experiments/validation/reviews/report-1935-review.md. The ten-game af2g counter screen remains 2W/8L, and the seven-policy and failed wall-signal results are also ready to cite. No current worker-3 job reads installed best.py.

## 2026-10-31T19:33:44.596234+00:00: D launch readiness checked without policy calls

Claim: the terminal reserve and launch checks remain ready for the actual final selection. Method: verify the unchanged manifest and every source pin, prefix-check hash, absence of a declaration/run directory, syntax of five launch/publish sources, and three direct diagnostic-redaction cases. Result: all pass, zero candidate or opponent calls. Verdict: CONFIRMED for static readiness only; D outcomes remain OPEN. Evidence: experiments/validation/analysis/terminal_reserved_validation/READINESS.md and verification/readiness_1935.json. New terminal_logged.py only streams/redacts diagnostics around the existing pinned pipeline.

## 2026-10-31T19:36:26.457451+00:00: First-leak defense diagnosis declared

Claim: the first received damage in three selected twenty-wall attacks may be avoidable within the same gold budget despite exact private H forecasts. Method: fixed free-planner and Fortress38 construction proposals, original-engine prefix and one-round replay. The existential witness claim is OPEN until checked; failed heuristic searches cannot refute existence. This is conditional one-round feasibility, not another strength game. See experiments/validation/analysis/wall_signal_defense_diagnosis/PROOF.md.

## 2026-10-31T19:37:15.060867+00:00: First-leak defense diagnosis complete

Claim: the first leak at each of three selected twenty-wall failure states can be prevented within the same gold against the same H action list. Method: exact original-prefix replay plus the two declared construction planners, six one-round interventions. Result: 3 of three states have a zero-damage witness; original private predictions and positive residual damage are exact in all three. Verdict: CONFIRMED. This is conditional one-round feasibility, with zero new full strength games. Evidence: experiments/validation/analysis/wall_signal_defense_diagnosis/RESULTS.md.

## 2026-10-31T19:38:19.239310+00:00: Wall-signal defensive repair declared

H1 the narrowly repaired K20 wins J with exact H-control histories; H2 the J result is better than the I-control result. Both OPEN. Six new games and six explicitly reused controls. This follows the three one-round feasibility witnesses and retains the original first move and round-three attack. See experiments/validation/analysis/wall_signal_repair/PROOF.md.

## 2026-10-31T19:38:32.390121+00:00: Delayed wall-signal grid complete

H1 at least one win against J: REFUTED; H2 such a win improves on the I control: REFUTED. Winning settings []; outcome improvements over I []. All 24 games, twelve assignment pairs, 1072 fresh external decisions and 536 forecast checks pass. Every J history equals its H control. See experiments/validation/analysis/wall_signal_delayed/RESULTS.md. This is selected development evidence.

## 2026-10-31T19:41:05.717182+00:00: Repair source freeze and pre-call clarification

The full original action list is simulated before comparing damage, including saturation construction after round twenty; its inherited trace only recorded the earlier defense step. The clarification was appended to PROOF.md before any L calls. All sources and six old controls are now pinned. H1/H2 remain OPEN.

## 2026-10-31T19:45:21.868143+00:00: Eight-policy extension declared

H1 L is nonnegative against all earlier included policies; H2 the old B/H/J mixture remains nonnegative against L. Both OPEN. Ten new L games against B,C,D,G and self, both seats, with fixed unchanged parameters. The six L-H/I/J games have finished 4W2D but their fresh audits are still pending. Full scope and exact mixture argument: experiments/validation/analysis/eight_policy_game/PROOF.md. No installed best.py or D use.

## 2026-10-31T19:45:57.830536+00:00: Wall-signal defensive repair complete

H1 win against J: CONFIRMED; H2 better J than I: CONFIRMED. Six new games, six reused K20 controls, 600 fresh external calls and 300 forecast checks pass. All unchanged-prefix and paired-history checks pass. See experiments/validation/analysis/wall_signal_repair/RESULTS.md. Selected development only.

## 2026-10-31T19:47:37.895494+00:00: Original-engine comparison of selected wall-signal repairs

Claim: conditional current-round reductions survive replacement of the private simulator by the unchanged engine. Method: six exact replays, 300 separately regenerated parent actions, 22 fixed-enemy one-round interventions. Result: every H/J final damage prediction from round four is exact and every selected H/J repair strictly reduces damage. Verdict: CONFIRMED on these reached states only. No new full strength game. Evidence: experiments/validation/analysis/wall_signal_repair/ENGINE_CHECK_RESULTS.md.

## 2026-10-31T19:49:08.977075+00:00: Worker checkpoint and final-selection coordination

No active worker3 job reads installed best.py. Protocol136 and its engine addendum are complete;137 uses frozen best_v9e and fixed counter sources only. Lead19:40status confirms the stale report freeze sentence was corrected. R13 remains the selection rule and D stays untouched until the actual final selection and23:00Z. The latest protected inventory has all903entries unchanged;59tests pass9skip. Owned scan at19:42Z finds no concrete local paths and2.581GB including the lane. EVIDENCE_INDEX points to all completed results; the eight-policy extension is still pending.

## 2026-10-31T19:51:41.807377+00:00: Eight-policy extension complete

H1 L nonnegative everywhere: REFUTED; H2 old B/H/J mixture nonnegative against L: REFUTED (payoff -1/3). Ten new games, 62 reused records, 36 matching assignment pairs, 708 fresh external calls. Exact restricted value-zero certificate CONFIRMED with weights ['1/5', '0', '0', '1/5', '1/5', '0', '1/5', '1/5']. See experiments/validation/analysis/eight_policy_game/RESULTS.md. This is selected finite-table evidence, not held-out or unrestricted strength.

## 2026-10-31T19:52:56.926681+00:00: Terminal candidate declared

Claim and verdict: OPEN, final installed SHA 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 declared for the unchanged96-condition D reserve. Selection time 2026-10-31T19:50:37+00:00; exact selection excerpt and a copy of the note retained. No candidate or opponent calls occur in this declaration. Games may start only after 2026-10-31T23:00:00+00:00; D is report-only, with no D-informed candidate choice. Declaration: bot_research/experiments/validation/terminal-candidate-declaration-001.json.

## 2026-10-31T19:53:29.744403+00:00: Final selection acknowledged and shift-three handoff

Claim: the final candidate is declared without consuming D. Method: checked installed best_v9e hash against the lead selection posted19:50:37Z, copied the complete selection note and froze85 source/evidence files at19:52:56Z. Result: declaration succeeded with zero policy calls; no D game has run. Verdict: CONFIRMED for declaration and nonconsumption, strength remains OPEN. No worker-3 jobs remain and none read installed best.py. The next shift runs D at/after23:00Z, without using its results for tuning. Protocol137 is complete with its original failed publisher and exact-specification correction retained.

## 2026-10-31T19:54:23.084140+00:00: Final-selection report consistency review

Method: archived current REPORT.md as experiments/validation/reviews/report-1954-source.md and reviewed its selection statements. Result: opening correctly says final best_v9e, but section5.12 still says the freeze is temporary and a final note is due22:15Z. Verdict: REFUTED for that now-stale paragraph. The actual final note is posted19:50:37Z and terminal declaration complete19:52:56Z. Detailed review also links the completed eight-policy table and separates reused game counts. See reviews/report-1954-review.md.

## 2026-10-31T19:55:08.223234+00:00: Shift-three final integrity checkpoint

Claim: protected files remain unchanged and owned artifacts meet the path/storage restrictions. Method: compare all903 entries against the initial inventory and scan owned text files with the exact generic-guard exception. Result: no added, removed or changed protected entries; the1002 absent manifest entries and3 initial mismatches persist. Full artifact scan at19:54:38 passes with 2599192168 owned bytes and 137411776512 free bytes. Later report texts separately pass. Verdict: CONFIRMED at these times. Receipts: runs/validation/integrity-shift3-final-1954.json, artifacts-shift3-final-1953.json, late-text-audit-1954.json. Final D declaration pins also pass, but D has zero games until23:00Z.

## 2026-10-31T19:56:39.662682+00:00: Final shift begins

Claim: the frozen final candidate and reserved D separation remain intact. Method: read the final selection and prior declaration, repeat protected inventory. Result: all903 outside-research entries equal the first-shift inventory; the1002 original absences and3 original hash differences persist. Verdict: CONFIRMED for integrity; D performance remains OPEN. D has not run and will start no earlier than23:00Z. No candidate changes or additional counter variants are planned. Report review and final evidence checks continue.

## 2026-10-31T20:00:08.415327+00:00 Independent final-report claim audit before pool D

Claim: the report's description of the selected policy, R13 and round-one comparisons should match source, pre-stated hypotheses and retained actions.

Method: reviewed a fixed REPORT snapshot (SHA256 25c4048b...), the lead's 19:04Z and 19:50Z notes, frozen v7 threat generation, unchanged Engine/adapter and both retained vbest2 guard60 logs. The checker in experiments/validation/reviews/check_report_shift4_v1.py makes no policy calls and runs no games.

Result: six findings are in experiments/validation/reviews/report-shift4-review.md. The material corrections are (1) R13 is rejected but the narrower stated H13 is not refuted by the guarded-maze regression; the tested early-strike part holds and the GROWERS gain was already known before the gate, (2) the planner checks sampled rosters, with four returned at 100 gold among 27 affordable ordered rosters including empty, (3) V29+r1_guard=60 bought gun2 at (8,1), two walls and a tier1, not a splash, in both kept wins 800:795. Also qualify public labels in the blind-round-one wording and replace the obsolete temporary-freeze paragraph. The deadline coverage note is optional clarification. Source/log-bound receipt: reviews/report-shift4-claim-checks.json.

Verdict: CONFIRMED for the concrete corrections; no change to the selected best_v9e bytes or R13 decision. D remains OPEN and unplayed until 23:00Z. Startup artifact scan passed at19:57:18Z with 2,601,484,389 owned bytes including lane files, no concrete local paths, and over137GB free.

## 2026-10-31T20:05:42.240635+00:00 Public labels and player indices on the frozen candidate

Claim: anonymizing names, with or without swapping player indices, preserves the selected candidate's decisions on the complete 72-history retained C corpus.

Method: predeclared source/input hashes; two fresh factory instances in a fresh process per history; every retained round replayed through the unchanged Engine; prescribed prefixes skipped.

Result: 72/72 cases completed, 0 differences, 0 failures, 1104 + 1104 actual policy calls. Evidence: experiments/validation/analysis/identity_invariance/RESULTS.md and verification/full_check.json.

Verdict: CONFIRMED for this finite invariance assertion only. This is an audit of selected C histories, not new strength evidence or a theorem about every possible observation. No D condition was played.

## 2026-10-31T20:06:26.171013+00:00 Report corrections verified and identity audit handed off

Claim: the six 20:00Z report findings have been applied without changing the final candidate. Method: retained the revised report snapshot and checked its corrected statements against the prior source/log-bound review. Result: all seven textual checks pass (the H13/R13 finding has two checks), and best_v9e remains SHA25670ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Verdict: CONFIRMED for the corrections. Evidence: experiments/validation/reviews/report-shift4-followup.md and report-shift4-followup-checks.json.

For the lead: identity_invariance/RESULTS.md is now complete,72histories,2208actual calls,0differences,0failures,original-engine replay in every case. It audits the selected C histories only and adds no W/D/L. All three worker3 slots are free. No D work has run; the final23:00Z gate is unchanged.

## 2026-10-31T20:08:27.359647+00:00 Exact affordable-roster coverage declared

Claim: H1 the sampled purchase lists attain worst incoming damage, and H2 zero sampled damage implies zero damage for every affordable ordered purchase, on all reached rounds2-6 of the24standard C histories with opponent gold at most250. Both OPEN. Method: enumerate every legal ordered purchase list with the entire actual budget, retain the candidate action list, and execute every intervention through the unchanged Engine. Source/input pins precede all interventions. This is component diagnosis of selected histories, no new policy calls or strength games. See experiments/validation/analysis/affordable_roster_coverage/PROOF.md.

## 2026-10-31T20:09:36.733205+00:00 Exact affordable-roster coverage complete

Claim: H1 sampled purchase lists attain the true fixed-round maximum; H2 zero sampled damage implies zero exhaustive damage, on the declared reached states only. Method: all affordable ordered purchases at actual gold at most250, rounds2-6 of24retained standard C histories, original Engine for every intervention and full original replay. Result: 100states, 74zero-sample states, 13658interventions, 6H1counterexamples, 2H2counterexamples, 0failures. Verdict: H1REFUTED, H2REFUTED. Evidence: experiments/validation/analysis/affordable_roster_coverage/RESULTS.md and verification/full_check.json. No new policy calls or full strength games. D remains unplayed.

## 2026-10-31T20:12:18.403470+00:00: Roster-order witness and continuation protocol

For the lead: the new exact component audit139 gives a concrete reason to retain the word sampled. In C02 round6, all five sampled purchases cause0damage, while the omitted (tier2,tier2,tier3), costing180 of190gold, causes26. The reversed and interleaved orders are sampled and cause0. Both bases finish that changed round at774, so a leak alone is not a full-game win. Witnesses and every enumerated list are retained. I am declaring18complete-policy games: these three same-cost orders, then original C02, frozen F38 or frozen E20 continuation, both seats against frozen best_v9e. H1 at least one screened continuation wins both seats and H2 screened order improves final HP margin in every continuation are OPEN. This tests whether the local omission matters strategically; no change to best.py or the D protocol.

## 2026-10-31T20:13:10.466810+00:00: Continuation sources frozen before calls

Protocol140pins73inputs and declares all18games before execution. All three continuations use the same three orderings. The original-engine witness establishes a component result only; the whole-game hypotheses remain OPEN.

## 2026-10-31T20:15:44.871748+00:00: Cheap wall-guard component result

Claim: one of five declared wall packages prevents the return hit while retaining the screened roster's26damage. Method: five original-engine interventions from the exact selected C02 round6 state, full prefix replay, zero policy calls. Result: H1CONFIRMED; successful costs[5, 6]. Verdict: CONFIRMED on this exact state and fixed target action; no full-game win claim or global minimality. Evidence: experiments/validation/analysis/screened_roster_wall_guard/RESULTS.md.

## 2026-10-31T20:15:49.830727+00:00: Screened-roster continuation complete

Claim: a complete counter converts the omitted-order leak into a win (H1), and the screened order improves every continuation's final HP margin (H2). Method: three equal-cost orders, three fixed continuations, both seats,18new games; full original-engine replay and 900 fresh policy calls. Result: all checks pass, shared prefixes and round6 actions match, round6target damage26versus0. Verdict: H1REFUTED, H2REFUTED. All nine paired outcomes are in experiments/validation/analysis/screened_roster_continuation/RESULTS.md. This is selected development evidence; best.py and D remain unchanged.

## 2026-10-31T20:16:45.043047+00:00: Guarded full-policy test declared

Protocol142pins89inputs,6new games and6reused controls. It adds the selected five-wall package to round6, then tests all three prior continuations. H1/H2 remain OPEN before execution. The component used original actions only; these new matches will independently obtain actual best_v9e actions and test the prefix equality.

## 2026-10-31T20:18:14.720025+00:00: Five-wall screened counter complete

Claim: a guarded continuation wins both seats (H1), and no continuation loses final HP margin relative to its unguarded control (H2). Method:6new games,6reused controls, original-engine replay and 304fresh calls; all common prefixes and round6target actions checked. Result: guard gives800:774 at round6 in every match. Verdict: H1CONFIRMED, H2REFUTED. The complete table is experiments/validation/analysis/screened_roster_guarded_policy/RESULTS.md. Selected development only; final candidate bytes and D remain unchanged.

## 2026-10-31T20:19:43.668748+00:00: Concrete post-selection counter and minimum-cost question

For the lead: a new observation-only counter wins 800:774 at round50 in both seats against frozen best_v9e. Its default specification is bot_research.bots.counters.screened_roster_guarded:@make. It follows the C02 four-splash opening through round5, then buys (tier2,tier2,tier3) and five walls in round6, then uses frozen Fortress38. The unguarded counterpart draws774:774. Six new full games and six reused controls passed all checks, including304 fresh calls. The original and Economy20 continuations still lose. Details: analysis/screened_roster_guarded_policy/RESULTS.md. This is a targeted post-selection counter, not a reason to alter the frozen final entry or use D for selection.

I am also checking whether five is the minimum wall cost for this fixed state and attack. The finite question covers every set of up to four added walls; it is separate from complete-game strength. A native routing enumeration with source correspondence, exact domain checks and original Python/Engine witnesses is planned. Its proof and scope were written before execution.

## 2026-10-31T20:20:42.379307+00:00: Exact wall-cost enumeration declared

H1: five walls are necessary for zero incoming damage in the fixed C02 round6 state while retaining the180gold screened attack. OPEN. The declaration covers 14901218 wall sets of size0 through4, split into three disjoint native scans. Source correspondence, exact set coverage and original-router/Engine checks are required before a conclusion. No policy calls or full strength games.

## 2026-10-31T20:23:15.083943+00:00: Exhaustive wall-cost result

Claim: five walls are necessary on the fixed C02 state with the screened attack. Method: all 14901218 wall sets of size0 through4, exact domain checks, 11097 original-router checks and six original-engine witnesses. Result: minimum 5, maxima [100, 100, 100, 100, 150]. Verdict: H1CONFIRMED, under the source correspondence argument in analysis/screened_guard_minimum/PROOF.md. No formal proof assistant, policy calls or new strength games.

## 2026-10-31T20:24:12.434329+00:00: Screened-guard transfer declared

Claim: guard wins both AS1C assignments (H1), and does not worsen W/D/L against its unguarded matched control on six fixed opponents and both seats (H2). Method: 24 new games, source and JSON pins, strict checks, full replay and fresh policy reproduction. Verdict: OPEN before calls. The set contains AS1C, AS1, best_v9f, Fortress41, V29_g1 and V29_guard60. This is selected development, separate from H14 and D.

## 2026-10-31T20:32:04.962318+00:00: Screened-guard transfer complete

Claim and verdict: both AS1C wins REFUTED; no W/D/L regression against matched controls CONFIRMED. Method: 24 declared new games, both assignments, complete replay and 2092 fresh policy calls. Result: guard {'L': 10, 'D': 2}, control {'L': 12}. The full per-opponent table and limitations are in experiments/validation/analysis/screened_guard_transfer/RESULTS.md. These games are separate from the lead's H14 gate and do not modify the selected final bot or reserved D.

## 2026-10-31T20:32:49.846827+00:00: Screened-order mechanism and transfer limitations

Claim: purchase order changes target competition on the selected C02 round-six state. Method:750 original combat ticks, separate HP/target accounting and three Engine round replays. Result: the tier3 receives168,192,184damage in screen/middle/front order; the screen order alone arrives with12HP and deals26. Verdict: CONFIRMED on these exact states. No new complete games or policy calls. The worked explanation and static figure are in experiments/validation/analysis/screened_order_mechanism/EXPLANATION.md.

Claim: exact next-roster input lets the frozen free planner strictly reduce both later AS1C hits. Method: six selected-state interventions at rounds10and11, fixed actual opposing actions, four planner calls and complete replay checks. Result:280to140at round10,140to140at round11. Verdict: REFUTED. The narrower round10 advantage over visible-roster planning is CONFIRMED. This uses recorded future actions as a diagnostic only. experiments/validation/analysis/screened_forecast_defense/RESULTS.md.

To lead: the completed24-game screened-guard transfer gives guard0W/2D/10L versus control0W/0D/12L,2092 fresh calls, all12assignment histories equal. AS1C and AS1 both beat the new guard774:380, while controls lose774:644; the guard changes the loss margin adversely here despite equal W/D/L. This is outside your H14 gate. best.py and D remain unchanged.

## 2026-10-31T20:37:50.032988+00:00: Terminal validation scheduled, not yet played

The unchanged, hash-pinned terminal pipeline was started at20:36:10.961287Z and is waiting at its internal23:00Z gate. Its wrapper confirms85source pins and the declared candidate hash. No D game or policy call has run. Waiting time is not experiment computation time. The existing process will be monitored; it must not be launched a second time. Final candidate and reserved protocol are unchanged. Pipeline log: runs/validation/reserved-D-final-001-pipeline.log.

## 2026-10-31T20:38:12.768364+00:00: Stronger screened continuations complete

Claim and verdict: some continuation wins AS1C (H1 REFUTED); a successful one retains both best_v9e wins (H2 REFUTED); all first-six-round histories match (H3 CONFIRMED). Method:12 new games,4 reused controls,596 fresh calls and full independent replay. Result: AS1C winners []; joint winners []. Full table: experiments/validation/analysis/screened_continuation_repair/RESULTS.md. Selected development only; best.py and D unchanged.

## 2026-10-31T20:40:31.372533+00:00: Ten-policy extension declared

H1: the old uniform B/G/H/J/L mixture remains nonnegative against the screened counter M and AS1C N. H2: N weakly improves on B across all eight old columns, with at least one strict improvement. Both OPEN. Method:34 declared new games,76 reused records, source and JSON pins, full replay and fresh reproduction. Arithmetic fixtures pass. This selected development table does not alter best.py or reserved D. Protocol: experiments/validation/analysis/ten_policy_game/PROOF.md.

## 2026-10-31T20:42:43.486524+00:00: Independent all-score route audit declared

Claim: all14,901,218 retained wall-set scores agree with a backward-distance router. Verdict: OPEN. Method: every binary record rescored with a separate native algorithm; all11,097 retained original-router cases checked for complete-path equality by Python. No new large score table, game or policy call. Exact argument and scope: experiments/validation/analysis/reverse_route_audit/PROOF.md.

## 2026-10-31T20:43:01.968361+00:00: Independent all-score routing audit

Claim: every one of the14,901,218 retained wall-set scores agrees with a backward-distance route algorithm. Method: full native rescoring,11,097 complete original-Python path comparisons and parent hash/domain rechecks. Result:0mismatches; maxima unchanged. Verdict: CONFIRMED under the route correspondence argument, without a proof-assistant or verified-compiler claim. No games or policy calls. Evidence: experiments/validation/analysis/reverse_route_audit/RESULTS.md.

## 2026-10-31T20:45:04.233835+00:00: Protocol148 publisher normalization amendment

The first publisher failed its spec equality check because the two reused M-B records explicitly name continuation="fortress38" while declared M omits that constructor default. Failure retained in experiments/validation/ten-policy-publisher-amendment-001.json. No result was published. A version-two publisher checks the pinned constructor default and both positive/negative normalization fixtures before preserving every other original check. Games, hypotheses, sources and D are unchanged. Full explanation: analysis/ten_policy_game/PUBLISHER_AMENDMENT.md. Result remains OPEN until the revised publisher completes.

## 2026-10-31T20:45:06.265174+00:00: Ten-policy extension complete

Claim and verdict: H1 old mixture extends to M/N REFUTED; H2 AS1C weakly improves on best_v9e across the eight old columns CONFIRMED. Method:34 new games,76 reused records,55 identical assignment pairs,1732 fresh calls, exact rational certificate verification. Result: old mixture payoff versus M/N -1/5/-3/5; pure nonnegative policies []. Full table and scope: experiments/validation/analysis/ten_policy_game/RESULTS.md. Selected development only; final bot and D unchanged.

## 2026-10-31T20:46:33.423684+00:00: Report review and checkpoint

Review experiments/validation/reviews/report-2047-review.md identifies the18-total/6-screened denominator ambiguity and supplies complete148/149 receipts. Lead H14 guard-roster failure is consistent with148's narrower old-eight-column improvement. Final best.py and D unchanged. Artifact scan runs/validation/artifacts-2044.json passes;2,752,112,495ownedbytes and130,354,941,952free at20:45:07Z.

## 2026-10-31T20:48:14.682118+00:00: Visible-gold runtime declared and running

Protocol150 copies two standard x202a histories with factory_cap1200, pins56inputs, and regenerates100candidate calls plus10separate composition calls. H1allactionsagree;H2walltime>3s;H3CPUtime>3s. No new game, no Duse. Proof argument explains exact maximum threat-list length active_entries+floor(gold/15), regardless of gun_cap. Runs on28and29;each child timeout550seconds.

## 2026-10-31T20:51:56.831684+00:00: Runtime shortcut proposed for independent review

Claim OPEN: with the default frozen best_v9e, rounds after5, an unchanged stage-zero map and splash exposure at least1500, insurance returns no actions. An owned research subclass can preserve _fortress and the attack/state updates while skipping materialized rosters. The informal proof is written before code in experiments/validation/analysis/immune_runtime_shortcut/PROOF.md. Protocol150 is currently regenerating the two historical high-factory games after a documented initial-header checker correction; its first attempt made zero policy calls. This proposed variant does not change best.py or poolD. Lead/Opus review of the exact-state argument is welcome through the usual notes.

## 2026-10-31T20:52:37.364667+00:00: Visible-gold runtime audit complete

Claim H1 exact candidate regeneration CONFIRMED:100calls,2original-engine replayed historical games,0new strength games. H2 call>3wallseconds CONFIRMED; H3 call>3CPUseconds CONFIRMED. Maxima 6.770995s wall and 6.716633s CPU. All10 sampled threat-list lengths equal active entries+floor(gold/15). Gun cap does not cap list construction. Scope and complete evidence: experiments/validation/analysis/visible_gold_runtime/RESULTS.md. Final candidate andDunchanged.

## 2026-10-31T20:54:59.630889+00:00: Protocol151 proof scope corrected before calls

Independent source review confirmed the native immune shortcut but identified an overbroad induction claim: the unchanged E20 foreign delegate uses a finite1e6-second planner cutoff. Preserved PROOF_INITIAL.md and narrowed PROOF.md to native sequences, or matching foreign deadline branches. All74 retained histories will be checked empirically. No shortcut calls have run and no151declaration has been pinned. Final best9e and reservedD are unchanged.

## 2026-10-31T20:56:46.881087+00:00: Runtime finding for the final report; shortcut audit in progress

For the lead and economy Opus lanes: the exact installed best_v9e has now reproduced all100 decisions on the two retained standard x202a factory-cap1200 histories. Both whole histories replay through the original engine. At round50 it returns zero actions while its own splash exposure is1550 and the opponent holds12,149,100 gold. The maximum measured call is6.770995 seconds wall and6.716633 seconds process CPU. The gun-cap statement must therefore describe the gun-search restriction, not a general decision-time bound. This is existing development evidence, not a new final-validation condition.

The ten separate threat-list component calls confirm linear list growth, but list construction itself takes only about0.027 seconds at round50. Do not attribute all6.7 seconds to allocation. The source also runs exact defense simulations over these sampled rosters after immunity; the proposed shortcut removes that redundant work.

Protocol151 is a research variant in bots/counters/immune_runtime_shortcut.py, with no change to best.py or any D pin. Its native action/state equivalence argument has independent source review in experiments/validation/reviews/immune-shortcut-review-001.md. The review caught an overbroad foreign-delegate induction claim; the corrected theorem is native-only, or conditional on matching foreign deadline branches. The original text is retained. The predeclared empirical comparison now runs both implementations on74 retained histories,1204 fresh calls each, comparing complete legitimate state as well as actions. Performance and corpus claims remain OPEN until the receipts finish. Opus review of this interpretation or a counterexample to the shortcut is welcome before it is described as a proved native optimization.

Independent certificate review also completed: experiments/validation/reviews/certificate-review-2050.md reconstructed the110-record ten-policy table, checked6697 distinct artifact hashes and verified the exact G/J/N rational certificate and five-wall route reduction. It found no defect invalidating their restricted claims. It did not rerun the full enumeration or add strength samples.

## 2026-10-31T21:00:49.513989+00:00: Protocol151 immune shortcut complete

Claim H1 exact actions and legitimate state on74 retained histories: CONFIRMED. Result: 1204 calls per implementation, 0 differences, 0 failed attempts; 364 shortcut calls, 508 unchanged foreign calls per implementation. H2 CONFIRMED; H3 high-factory max shortcut CPU<3s CONFIRMED. High-factory maxima parent/shortcut: [{"wall_seconds": {"id": "high-1", "round": 50, "value": 6.700285144150257}, "cpu_seconds": {"id": "high-1", "round": 50, "value": 6.583383948999995}}, {"wall_seconds": {"id": "high-0", "round": 8, "value": 0.29901464795693755}, "cpu_seconds": {"id": "high-0", "round": 8, "value": 0.29886853}}]. Method, scope, original-engine checks and source-bound receipts: experiments/validation/analysis/immune_runtime_shortcut/RESULTS.md. Zero new games. Final candidate andDunchanged.

## 2026-10-31T21:01:24.918578+00:00: Shortcut audit result and supplemental checks declared in prose

Protocol151 CONFIRMED on74 histories,1204 calls per implementation and0 action/state differences.364 calls used the shortcut;508 calls per implementation used the unchanged foreign delegate. High-factory maximum CPU: parent6.583384s, shortcut0.298869s. The independent checker review identified an untimed eligibility preflight and missing explicit whole-stream length/terminal checks. These do not change a recorded action comparison but limit the wording. Protocol152 will close the stream boundaries and run100 shortcut-only calls without preflight or parent calls, plus a separately timed and profiled round50 sampled-leak component. All hypotheses are OPEN until its new receipts complete. Candidate andD stay fixed.

## 2026-10-31T21:03:09.538723+00:00: Runtime supplement complete

Claim H1 exact74 terminal boundaries CONFIRMED; H2 all100 unpaired shortcut calls exact CONFIRMED; H3 shortcut maxCPU<3s CONFIRMED (0.207627s); H4 round50 sampled-leak CPU>3s and result0 CONFIRMED (6.347995s, leak0). No parent policy calls or eligibility preflights in these shortcut processes. Separate profiler timings include overhead. Evidence: experiments/validation/analysis/immune_shortcut_followup/RESULTS.md. No new games or final/D changes.

## 2026-10-31T21:03:42.363309+00:00: Opus follow-up on the runtime mechanism

Protocol152 closes all74 stream boundaries and all100 unpaired shortcut decisions match. Maximum shortcut CPU0.207627s. The parent's isolated seat0 round50 _worst_leak returns0 while using6.347995s CPU, excluding roster construction. A distinct cProfile execution takes22.952603s CPU and records8 simulate_defense calls and49,475,369 list append calls. Profiling times include instrumentation; they are not the unprofiled timings. This supports redundant simulation of a large immune threat set as the observed bottleneck. Final candidate bytes remain unchanged.

## 2026-10-31T21:05:51.328513+00:00: Protocol153 pinned before calls; nested-state checker amended

22new standard games are declared for O against allten old policies and self, both assignments. The185 original pins preserve O and the source argument. Before any decision, source inspection found the reused151 serializer does not cover L's nested bound policy object. A separate version-two checker and logical-value serializer are pinned by wall-prefix-selector-checker-amendment-001.json; constructor fixtures detect nested state changes. No strategy or hypothesis changed. H1/H2/full-row predictions OPEN.

## 2026-10-31T21:08:37.825413+00:00: Delayed-wall counter, before implementation or calls

Claim: moving G's imported wall witness from round1 to2 makes O choose L. Method: standard-start source proof in experiments/validation/analysis/delayed_wall_counter/PROOF.md. The public-branch claim is CONFIRMED by the explicit first-move argument; H1 P beats O in both seats, H2 O/L full-history transfer and H3 paired-history equality remain OPEN. Ten new development games are planned, P against O,L,G,B,N in both assignments. This changes both the public signal and early economy, so no pure signal-effect or G/P equivalence claim is made.

## 2026-10-31T21:10:07.381848+00:00: Independent shortcut follow-up review and next counter declaration

The separate GPT-6Astra reviewer found no new invalidating defect in151/152. See experiments/validation/reviews/immune-shortcut-followup-review-001.md; it confirms all74 stream boundaries and100fresh unpaired action checks, while keeping state-check and foreign-deadline limits explicit. This reviewer is not the Opus collaborator. Protocol154 was pinned21:09:20Z before any P decision; its two pipelines wait for153cores to finish before launching. Actual Opus5.5 collaboration continues throughlead/economy notes.

## 2026-10-31T21:11:07.298794+00:00: To lead and economy lane, selector results and runtime mechanism for Opus review

All22 newly generated O games have passed strict and engine replay checks and have the predeclared outcomes; fresh decision/state audits are still running. O has no loss against the old ten-policy set and an observed +2/3 payoff against uniform G/J/N in each seat. This is a selected finite-set response, not a final-candidate proposal. Protocol154 now probes the public branch by delaying G's walls one round; ten games are queued and no result is claimed. Please assess the branch interpretation and any missing alternative explanation when incorporating this evidence. The early economy also changes, so the test cannot attribute an outcome solely to signaling.

For the high-factory runtime concern, protocols150-152 separate the mechanisms: list construction at the selected round50 state takes about0.027s, while the parent sampled-leak evaluation alone takes6.348 process-CPU seconds despite returning0. The separate profiled execution makes49,475,369 list appends across eight simulations. The worker-only immunity shortcut reproduced74 retained histories; on two additional unpaired history checks its maximum was0.208 CPU seconds. Native equivalence has a source proof; foreign deadline coupling remains conditional. No final-bot source change is requested.

## 2026-10-31T21:13:13.942821+00:00: Round-four reservation hypothesis before Q implementation

P loses both B and N assignments in the completed control shard. Its selected P/B history has254gold entering round4, six short of the260-cost tier4. The exact round3 budget is279-5k for k factories, so withholding two of the five purchases yields264gold; withholding one yields259 and fails. This fixed-opening minimum is CONFIRMED by the source arithmetic. Proposed Q reserves this purchase and otherwise follows P. H1 Q beats O, H2 O/L history transfer, H3 paired histories and H4 the264gold/11factory plus tier4 check remain OPEN;10games will be declared. P/O has not begun, and Q has not been implemented or called. Evidence: experiments/validation/analysis/reserved_wall_counter/PROOF.md.

## 2026-10-31T21:14:57.844502+00:00: Second shared-prefix selector complete

H1 positive mean/no loss against G/J/N CONFIRMED, exact per-seat means{'0': '2/3', '1': '2/3'}; H2 nonloss against allten old policies CONFIRMED; H3 predicted whole row CONFIRMED.22newgames,1888 fresh external decisions,944 extra selector and944 standalone-response calls. PureO11-policy certificate CONFIRMED. Baseline transfer22/22 and identical assignment histories11/11. Scope is the selected standard finite game. Evidence: experiments/validation/analysis/wall_prefix_selector/RESULTS.md. D andbest.pyunchanged.

## 2026-10-31T21:15:35.008529+00:00: Delayed-wall counter complete

H1 P wins both O assignments CONFIRMED; H2 selects L and matches full P/L history CONFIRMED; H3 all five paired histories agree CONFIRMED.10newgames,688 fresh external calls,22 additional O and22 L calls. Exact outcomes and scope: experiments/validation/analysis/delayed_wall_counter/RESULTS.md.

## 2026-10-31T21:18:14.803175+00:00: Completed selector/counter chain; Opus review requested through team notes

Claim and result CONFIRMED on the stated standard starts: O has no losing entry on the eleven-policy table, but the newly fixed P beats O800:-55 at round11 in both seats. P/O and P/L full histories agree; P loses to G740:800, and B/N770:800, all round50. Method:153 has22games,1888fresh external decisions plus944O/944component calls;154 has10games,688fresh external decisions plus22O/22L calls. The half-G/half-O support suggests a value-zero certificate for any skew-symmetric completion of the partially measured twelve-policy table; its proof is now written in analysis/support_only_certificate/PROOF.md, checker pending. This is a restricted matrix statement, not an unrestricted or load-invariant equilibrium.

To lead/economy (actual Opus5.5 lanes): please examine whether this evidence is best described as a public-signal counterexample rather than general opponent identification. P changes both signal and economy. The proof uses only measured support rows and leaves six P matchups explicitly unplayed. Q's ten-game reserved-purchase comparison started21:17:33Z and remains selected development, with no change to best.py or D. Please exchange any counterargument in your own notes; w3 will read and verify it.

The153 provenance supplement verifies1096retained input edges and all amendment start times;13retained constructor/value fault fixtures pass with no policy decisions. Their post-run scope is explicit. Closed private shift logs were losslessly compressed, saving37051528bytes; current run logs and evidence remain intact.

## 2026-10-31T21:19:44.761998+00:00: Reserved-wall counter complete

H1 Q wins both O assignments CONFIRMED; H2 selects L and matches full Q/L history CONFIRMED; H3 all five paired histories agree CONFIRMED; H4 reservation arithmetic CONFIRMED.10newgames,712 fresh external calls,28 additional O and28 L calls. Exact outcomes and scope: experiments/validation/analysis/reserved_wall_counter/RESULTS.md.

## 2026-10-31T21:20:25.637042+00:00: Support-only finite certificate complete

CONFIRMED under the stated skew-completion hypotheses: half G/half O has value0 and is unique on that two-policy support. Replayed46existing games/23assignment pairs; checked all729ternary completions. Zero new games or decisions. Six P off-diagonal pairs and P/P remain explicitly unplayed. Source, proof and limitations: experiments/validation/analysis/support_only_certificate/RESULTS.md.

## 2026-10-31T21:23:44.201076+00:00: To Opus lead and economy, reserved counter and complete paired comparison

Claim CONFIRMED on five selected standard-start targets: Q (bot_research.bots.counters.reserved_wall_guard:@make) beats frozen best_v9e B and AS1C N, both770:740 at round50 in both seats; draws G740:740; beats O and L800:-326 at round14. P instead loses to B/N770:800 and G740:800, and wins O/L800:-55 at round11. Method: allten Q games and allten P games pass strict/source/data/original replay/fresh-decision/paired-history checks. Q's reservation is the only source-rule change from P: it withholds two round3factories to enter round4 with264gold and11factories, then buys one tier4. All10 H4 state/action checks pass.

The complete P/Q comparison reports six improved WDL conditions and four ties, with no omitted target. O/L victories take three more rounds for Q, so neither final overkill nor duration is uniformly improved. Evidence: experiments/validation/analysis/reserved_wall_counter/PQ_CONTROLS.md andverification/PQ_controls.json. No final-bot proposal or D change. Q defeats the earlier halfG/halfO mixture in this added column with payoff -1/2 from the mixture perspective, because G draws Q while O loses; protocol156 explicitly excludes Q and remains valid on its stated set.

Next research hypothesis, not yet implemented or run: extend the G/L shared prefix through round2 when the opponent remained empty after round1, then select using completed round2 state. Source inspection gives five common factories in that branch; P/Q reveal their walls at round2. A separate proof is being written before any new policy code. Please assess whether this finite signal-counter cycle warrants a recommendation about uncertainty, rather than identification from an empty board. Actual Opus5.5 exchange continues through team notes; the local proof reviewer is GPT-6Astra.

The post-run context supplement adds860 checked provenance edges and allfive JSON data pins to the P/fixture linkage without rewriting earlier receipts.288 closed early replay streams were losslessly gzip archived, saving138464557bytes; manifest runs/validation/archived-mature-replays-002.json retains exact original and archive hashes and restoration instructions. Current D and counter-chain inputs remain directly readable.

## 2026-10-31T21:26:01.771537+00:00: Report follow-up for lead

Source/evidence review `experiments/validation/reviews/report-2126-review.md` identifies two concrete wording corrections: original guard00 uses round1 walls (unreserved round2 P loses B/N), and the screened-order four-loss/two-draw count covers six of the eighteen order/continuation games. It also points to the completed CPU-runtime mechanism and Q counterexample for optional inclusion. Snapshot and hash retained; no report or final candidate edited.

## 2026-10-31T21:29:37.045659+00:00: Protocol157 declared and running; final candidate unchanged

OPEN: a two-round public selector R should recover the G branch against delayed-wall P/Q while retaining L against the publicly empty C/D/H/I/J. Prospective proof, 208 input pins and 28-game declaration are in experiments/validation/analysis/two_round_wall_selector and two-round-wall-selector-001.json. Launch21:28:58Z, both seats against14fixed policies including self. No R result was used in its choice. This extends selected development research; D remains unplayed and scheduled23:00Z. Lead21:28 H14/H15 rejection read; no candidate change proposed.

Storage: archived288 mature replay files losslessly with exact original/compressed hashes in runs/validation/archived-mature-replays-002.json, saving138464557bytes. Restoration command is in ARCHIVED_MATURE_REPLAYS_002.md. Current recent controls and D inputs retained directly.

## 2026-10-31T21:37:34.217566+00:00: Two-round selector complete

H1 branch/round CONFIRMED; H2 exact baseline transfers CONFIRMED; H3 predicted row CONFIRMED; H4 pure-R support certificate CONFIRMED.28newgames,2488 fresh external calls,1244 extra R and1244 standalone component calls. Scope and exact outcomes: experiments/validation/analysis/two_round_wall_selector/RESULTS.md. No final-candidate change or reserved D use.

## 2026-10-31T21:38:27.328991+00:00: Two-round selector complete; later signal counter declared

Protocol157 is CONFIRMED on all four declared hypotheses: 28 games, 2488 fresh external decisions, 1244 fresh selector and 1244 standalone member decisions, all 14 assignment pairs and 28 selected full-history controls agree. R's row on B,C,D,G,H,I,J,L,M,N,O,P,Q,R is [1,0,1,0,1,0,1,1,1,1,0,1,0,0]. It supports a pure-R value-zero certificate only for real skew completions of that stated finite set. Results and scope: experiments/validation/analysis/two_round_wall_selector/RESULTS.md.

The first publisher attempt failed after writing its narrative because the verification directory was missing. Its narrative and failure receipt are retained under verification/. Creating the missing directory and rerunning the unchanged publisher required zero new games or decisions. The separate context supplement checks 2577 provenance edges, including this recovery, without claiming it ran before the games.

Protocol158 is OPEN: S, LateReservedWallGuard, hides its walls through round2, builds the guard00 walls and splash in round3, and reserves enough gold for the round4 tier4. Its source proof gives 271-5k projected gold, so exactly two of the four available factories are retained, leaving261gold and11factories. The ten-game declaration against R,L,G,B,N in both seats was made21:37:58Z before S calls, with145 pins. Source review found no invalidating defect. This is a targeted development counter, not a proposed final bot or a change to reserved D.

## 2026-10-31T21:40:45.623312+00:00: Late reserved-wall counter complete

H1 S wins both R assignments CONFIRMED; H2 selects L and matches full S/L history CONFIRMED; H3 all five paired histories agree CONFIRMED; H4 reservation arithmetic CONFIRMED.10newgames,712 fresh external calls,28 additional R and28 L calls. Exact outcomes and scope: experiments/validation/analysis/late_reserved_wall_counter/RESULTS.md.

## 2026-10-31T21:43:01.905139+00:00: Two-round signal counter and conditional ambiguity theorem for Opus review

Claim: waiting one more completed public round repairs O against P/Q, but does not identify the opponent. Method: prospective R row test followed by prospective S counter test, with exact baseline transfers and both physical assignments. Result: R has its predicted nonnegative row on the fourteen declared policies; S then wins both R and L 800:-326 in round14, draws G 740:740 and wins B/N 770:740. Verdict CONFIRMED on those declared conditions, not global strength. S builds in round3 and reserves two factories for a round4 tier4; R chooses L before seeing that construction. Full S/R and S/L histories agree.

A separate proof in experiments/validation/analysis/delayed_signal_ambiguity/PROOF.md shows that H and S share the same first two public rounds against the common G/L opening. Conditional on the measured table G/H=-1, L/H=+1, G/S=0, L/S=-1 and full continuation coupling, an observation-only selector that must permanently choose G or L by round3 has optimal worst expected payoff -1/3 at probability 2/3 of G. This is a restricted theorem: names and identity-correlated timing cannot be inputs, selected private state must be retained, and deadline-sensitive future transitions must reproduce the baseline. The retained-history checker is under static review; no new games or policy calls are required. Opus5.5 lead/economy review can assess the restricted-class interpretation against the repeated signal-counter cycles. This does not propose changing the frozen final candidate or D.

## 2026-10-31T21:48:01.183817+00:00: Pre-terminal audit and additional timing comparison

Claim: the terminal selection and original 85 source pins remain fixed. Method: direct byte checks and independent static pipeline review, without loading D parameters or running a D policy. Result: all85 pins match; the explicit subprocess dependency closure contains nine additional files not pinned by the original selection declaration. A separate dated supplement is being prepared to preserve those sources and prior matching receipts. Verdict: original-pin stability CONFIRMED at the check time; complete supplement OPEN until written and verified. The existing time-gated pipeline remains the only scheduled D run, starting no earlier than23:00Z. Direct and factory regeneration will be two fresh executions compared with the recorded :decide history, not three fresh regenerations.

Protocol160 is prospective: Q and S against F44,F45,V29,V29_g1,V31_g1f,H in both seats, with all8 existing G/N controls included. Source proof: experiments/validation/analysis/wall_timing_transfer/PROOF.md. Q and S have equal maps and11factories after round3 but gold264/261; this does not imply equal HP or opponent state. New24-game outcomes remain OPEN. No candidate replacement or D tuning is involved.

Archive003 losslessly compresses365 closed replays, saves200048449bytes, and preserves the original hashes. The21:46:14 artifact scan reports2546532491 total owned bytes,130422284288 free bytes, and no concrete absolute local paths.

Opus collaboration: I read the lead's21:42:25 prefix-fork findings and economy's21:45:50 signal and attack-hold findings. Their partial signal failures are consistent with needing a precisely stated information set; protocol159 proves only a restricted G/L commitment bound, conditional on full continuation coupling. It does not rule out different openings, later adaptation or a third response. Actual lead/economy model was confirmed earlier as us.anthropic.claude-opus-5-5; local code reviewers are GPT-6Astra.

## 2026-10-31T21:48:58.223996+00:00: Protocol159 complete, restricted ambiguity bound

Claim: the first three normalized observations and first two complete rounds coincide against H and S for G/L and the R controls, with fixed physical seats. Method: twelve complete original-engine replays, exact source/data and source-archive checks,9787 checked input edges and7425 unique inputs; zero new games or policy calls. Result: H1 prefix equality, H2 both-seat payoff table and H3 retained R/L state and transfer checks all pass. Verdict: CONFIRMED for these measured premises.

The table from the member's perspective is G/H=-1, G/S=0, L/H=+1, L/S=-1. For an observation-only selector committed to G/L by round three, independent selection randomness and corresponding full continuation payoffs imply exact worst expected value -1/3, uniquely at p(G)=2/3. General continuation coupling remains conditional because later planners use wall-clock deadlines. A different opening, later commitment, third response, reselection or identity side channel is outside the theorem.

Files: experiments/validation/analysis/delayed_signal_ambiguity/EXPLANATION.md, PROOF.md, RESULTS.md and verification/full_check.json. Checker SHA73e260cd2083d77e7c49690ed741293cbb382ebf7cd5c7893d60214dc3c55bd9; review SHA9fd8d4177d8b015665a0289f87c0a5c804ed6957dbdee1234dec329e8ef6e8d0. Before declaration the review caused two fixes: direct archive-source verification and conditional success wording. The final check completed21:48:19Z. Best_v9e and reserved D remain unchanged.


## 2026-10-31T21:51:33.842724+00:00 | Terminal source supplement and delayed-signal review

Claim: the scheduled terminal campaign has a complete explicit local subprocess source seal before its 23:00 UTC gate. Method: the separate readiness review found nine source dependencies omitted from the original static declaration, then archived those files and a new verifier without modifying the original 85 pins or scheduled pipeline. Result: supplement sealed at21:49:45 UTC, 95 files including all original pins; ten newly covered snapshots; eight added dependencies match selected earlier receipts. Pre-D verification at21:50:08 passed, as did one unchanged control and nine malformed-seal rejection cases. Verdict: CONFIRMED for the later pre-D source seal; successful final execution and post-D source identity remain OPEN. This is an actual later supplement, not a claim that declaration001 originally contained 95 files. See `analysis/terminal_reserved_validation/DEPENDENCY_SUPPLEMENT.md` and `reviews/terminal-readiness-review-2145.md` under the validation experiments folder.

Protocol159's result review found no material mismatch between the twelve retained histories, receipt, exact payoff table and conditional minimax calculation. The local H/S opening qualifier is now explicit in the separately sealed `EXPLANATION_v2.md`; v1 and its original seal remain retained. Its bound applies only to committing to the correctly advanced G/L components by round3 under the stated full-continuation coupling. It is not an impossibility claim for all adaptive bots. Actual local reviewer model was GPT-6 Astra, with its proof authorship disclosed. The ongoing Opus lead/economy collaboration remains through team notes. Opus counterarguments or a narrower useful interpretation are welcome through the existing notes channel; no response is required to proceed.

Protocol160 source review is underway before declaration or policy calls. It compares Q/S wall timing against six additional preselected opponents, with eight old G/N controls. These are development results and do not touch D parameters or selection of best_v9e.


## 2026-10-31T21:55:37.819157+00:00 | Protocol160 launched; reply to Opus lead's ambiguity reading

Claim under test: S is never lower than Q in WDL on eight named opponents and both seats; both physical assignments reproduce complete normalized histories for the twelve new pairs; all32 records satisfy the exact opening and reach round4. Method: declaration `wall-timing-transfer-001.json` at21:54:59 UTC pins122activeinputs and626retainedinputs. Three campaigns launched21:55:13 for24newgames; eight prior G/N controls remain explicitly reused. Before declaration, static review fixed process-group timeout cleanup and narrowed the promise about detailed interrupted fresh-check traces. Verdict: OPEN; no outcomes are inferred from the opening arithmetic. All three assigned cores are occupied until these campaigns finish.

Reply to the Opus lead's21:48:28 note: your reading of protocol159 is correct, with one explicit additional premise. The choice uses normalized public observations through completed round2, commits to one correctly advanced G/L member by the start of round3, and the selected full continuation must reproduce that member's baseline payoff. The last premise is stated because later planners have wall-clock cutoffs; finite trace reproduction is evidence, not a universal load-invariance theorem. Names and timing side channels are excluded. The max-min calculation and its scope therefore agree with your interpretation as opening-based selection evidence. The updated explanation makes the H/S shared-prefix qualification explicit and retains the original version. The new addendum `reviews/delayed-signal-results-review-002.md` verifies both narrative seals.

## 2026-10-31T22:02:39.792164+00:00 | Report ab15 audit: terminal classification and example correction

**Claim.** The report's ab15 GROWERS counts and “no win becomes a loss” statement are consistent with the retained 142 matched baseline conditions.

**Method.** Independent source and artifact review joins by full opponent specification, scenario and seat, isolates baseline V18FTg9a, and checks representative terminal records. No new games or policy calls. Review: `bot_research/experiments/validation/reviews/report-ab15-review-001.md` (SHA256 `470ee9e2788805425b4f1237b32d859427813aac9fc2abf0832cf37b7b08fcd4`).

**Result.** Baseline 66W-0D-76L, ab15 88W-30D-24L. Transitions: 56 W-to-W, 10 W-to-D, zero W-to-L, 32 L-to-W, 20 L-to-D, 24 L-to-L. All 30 draws destroy both bases. The +528 to -97 example changes from a win to a draw; HP margin alone does not determine the terminal label. One example label requires correction: the W-to-D maze layouts are `empty` and `lead_opening`, not `cash_rank_1`. The cash-rank growth-7 tier2-bait conditions are L-to-D. Exact replacement wording is in the review.

**Verdict. CONFIRMED** for counts and no W-to-L; **REFUTED** for `cash_rank_1` as a W-to-D maze example. Lead: please apply that example correction.


## 2026-10-31T22:08:54.775277+00:00 | Protocol160 complete and archive004 verified

**Claim.** S is no worse than Q in WDL on eight named opponents in both seats; each new opponent-policy pair reproduces its full normalized history across physical seats; all32 records meet the declared opening. **Method.** Twenty-four new games against F44,F45,V29,V29_g1,V31_g1f,H, eight reused G/N controls, strict action/source audits, full original-engine replay of all32 records and2400 fresh external decisions for the new games. **Result.** All three hypotheses are CONFIRMED. Q and S each beat F44,F45,V29,V31_g1f,N, lose to V29_g1 and H, and draw G in both seats. Equal WDL does not imply equal margin: against H, Q ends240:500 and S100:500. H2 compares physical-seat histories within each policy/opponent pair; it is not Q/S full-history equality. All results are development evidence. Files: `analysis/wall_timing_transfer/RESULTS.md` and `verification/full_games.json` under validation experiments. Final receipt time22:06:51 UTC; no policy calls by the final checker.

Archive004 completed22:06:40 UTC:963 closed replay files in79 campaigns,62591318 original bytes compressed losslessly, saving58938757 bytes. Original identities, protected control roots and all85 terminal pins are unchanged. Manifest `runs/validation/archived-mature-replays-004.json` has SHA256 `53b0f917ea3234751a91f1d585d9a707cdcf80dce0c1e580191b5ad8bc790f51`. Its generated README retains an inherited “archive003” heading; the004 filename, manifest and verified receipt are authoritative. No additional eligible unpinned pre18:00 replays remained to meet the150MB target.

T161 and its blind fourth-round control U162 remain source-only until separate reviewed declarations. These experiments test later commitment using correctly advanced members. They neither change best_v9e nor use reserved D inputs. The existing single D pipeline remains scheduled for23:00 UTC.


## 2026-10-31T22:11:26.693780+00:00 | T161 declared and launched; report scope correction

**Claim under test.** The fourth-round selector T avoids a loss against both H and S, using the newly visible building signal while retaining correctly advanced private members. **Method.** Exactly four standard-start games, H/S in both physical seats, plus the two original G/S controls. Declaration `experiments/validation/third-round-wait-001.json` was written at22:10:50 UTC with114 active and160 retained pins (SHA256 `59df75dda422880ee3d04e7d073563d35b1ddff717410956017056370ee172ee`). One bounded pipeline launched at22:10:56 on core28. The independent source review is `experiments/validation/reviews/third-round-wait-independent-review-001.md`, SHA256 `c398b808066eb31b82af64929d8763b7cd71aa05e188ab5bd2a73feab182e23c`. **Verdict. OPEN** until all declared games and audits finish. T uses L4, whose attack round is4; it is outside protocol159's fixed G/L, commit-by-round3 class. U162 is a separately prepared blind L4 continuation to distinguish later commitment from using the signal. U has not run.

**Report correction for the lead.** Section5.15 currently describes economy's fresh5/fresh6 opponents as “not chosen from either bot's results.” Economy18.20 explicitly states that most W3 counters in these sets were built against best_v9e and that this construction favors g1. The later comparison can be fresh for g1 while retaining that bias. Please state the construction bias and keep the15 non-W3 opponent subset separate. The updated846-condition gate table in economy18.23 is also being independently checked; the report still cites838. This is a source-scope correction, not a change to the fixed final candidate.

Storage scan completed22:10:33 UTC:2559923037 total owned bytes,130605723648 free bytes, no concrete absolute local paths. The unique reserved-D waiter remains unchanged and has made no calls before its23:00 gate.

## 2026-10-31T22:14:29.644274+00:00: Protocol161 complete; waiting through round three recovers the selected pair

Claim: the fixed T composite is nonnegative against exact H and S, using its G prefix and a round-four choice between the already advanced G and L4. Method: four prospectively declared standard-start games, both physical assignments, complete unchanged-engine replays, strict source/action and archive audits, 400 fresh external decisions, and a separate persistent-member audit. Result: T beats H 800:656 at round50 in both seats and draws S 740:740 at round50 in both seats. All H1-H4 are CONFIRMED; final checker completed 2026-10-31T22:13:57.794346+00:00. Both T/S complete canonical histories equal the matching original G/S controls; both opponent seat pairs agree completely.

The additional component audit made 200 T calls, 106 independent G reference calls and 106 L4 reference calls. Internal G/L4/H-model transitions are separately recorded subsets. The discarded round-three L4 proposal is eight factories; actual T buys splash plus five factories. T chooses L4 against H and G against S at decision four. All required four-round actions, states, selection and model-state checks pass. This tests a new response outside protocol159's two-member, round-three commitment class; it does not contradict its conditional bound. Earlier T selection branches at rounds two and three were source-reviewed but not empirically exercised here.

Evidence: experiments/validation/analysis/third_round_wait/RESULTS.md and verification/full_games.json (SHA256 005cbe7a326d2830c81d120f62277ff2609eaa2c404f49635e50ce5300d25ced); declaration third-round-wait-001.json at22:10:50.829836Z, actual launch22:10:56.030038Z, scheduling completion22:13:58.158430Z. U162 is the prospectively specified unconditional L4 ablation with the same first-three submitted actions. No U calls or result yet; independent source review is finishing. Final best_v9e and reserved D remain unchanged.

## 2026-10-31T22:16:06.780723+00:00: Independent846-pool audit, with denominator corrections for lead and economy

CONFIRMED: independent exact-spec/scenario/seat joins reproduce all note18.23 pool-weighted totals: g1 764-16-66, V29 584-18-244, g0 748-22-76, baseline524-82-240. The baseline uses the declared frozen best_v9e/development twins. Root inspected the aggregation source and full review; no new games or policy calls were used. Evidence: experiments/validation/reviews/economy-gate-846-review-001.md (SHA256e1d124ada88bcabbe5fa3bd3fa1ff84af6bf0d7884c285e03ae2e21c9d345f5a) and matching JSON row-provenance receipt.

REFUTED if interpreted as distinct or disjoint:846 is a sum of pool memberships containing804distinct conditions,402opponents in both seats. The448 subtotal covers416distinct conditions, ten of which also appear in excluded selection pool f5t. The report should call these weighted pool memberships, not independent or unseen conditions. Deduplicated804 totals are g1 726-16-62 versus baseline504-64-236 (68worse,282better). Removing the four selection pools by exact condition leaves406distinct conditions: g1 350-14-42, V29 280-4-122, g0 342-20-44, baseline290-58-58. This latter calculation is descriptive and does not prove absence of all prior exposure or related policies. A decoded-parameter check also identifies a URL-encoding alias of guarded_schedule in opp_key5; it is already among the ten removed conditions.

All joins have matching opponent entry/version hashes, no missing gate conditions or conflicting recorded duplicate outcomes, and no recorded errors/rejected actions. Terminal WDL/HP/rounds agree across both seats; full-history equivalence was not newly established. A follow-up is preserving exact input snapshots because ancillary afs6/fresh6 result files are still growing. The full row-provenance receipt is already retained.

Lead22:14:33 response read: ab15 example and fresh56 construction-bias wording are now corrected. The new846/448 denominator issue above is additional. The lead's Opus5.5 and economy Opus5.5 arithmetic is independently corroborated with this qualification. Final candidate/D remain unchanged. U162 was declared22:14:59.256683Z,116active/618retainedpins, then launched22:15:03.950027Z oncore29; rawgames2W2L, audits stillpending.

## 2026-10-31T22:18:26.899469+00:00: Protocol162 complete; the round-four choice matters on the declared pair

Claim: replacing T's round-four choice by unconditional L4 commitment preserves its H history and worsens its S outcome. Method: four prospectively declared standard-start U games, both physical seats, compared with the four completed T controls; unchanged-engine replays, strict source/action and data-archive audits, 248 ordinary fresh external decisions, and a separate persistent-member audit. Result: U/H and T/H complete canonical histories agree, both winning800:656 at round50. U/S loses-246:800 at round12 in both seats, whereas T/S draws740:740 at round50. H1-H4 are CONFIRMED, with final checker completion 2026-10-31T22:17:29.952350+00:00.

The audited U/S mechanism is the prospectively proved one: at round4, private H forecasts splash(10,1) and ten factories on S's actual map. This forecast kills all proposed tier2 copies, so U submits thirteen factories and no attack. Actual S buys one tier4. U/S closes round4 at gold454/213, factories27/11 and HP740/800. T instead chooses G and buys one tier4, closing at gold264/213, factories14/11 and HP740/740. The opening calculation alone does not prove U's eventual loss; the complete games establish that separate result. U's H model is correctly advanced on actual observations but predicts the wrong policy against S.

Additional successful audit entrypoint calls are U124, independent G12 and L4 124; nested G12/L4 124/H-model124/reference-H-model124 are separately counted subsets. No new T-control policy calls were made. All submitted actions are legal, audited observations unchanged, and attempts complete. Source/state snapshots exclude clocks, module globals and alias identity, so the measured complete-history agreement is not a general future-execution theorem. The pair is disclosed development evidence, not a held-out strength estimate. Earlier T selection branches remain untested by these four openings.

Evidence: experiments/validation/analysis/blind_fourth_round/RESULTS.md and verification/full_games.json, SHA256 ce52e656eb739daa7c3f21d88101eb51d7ef0216005d572e615f89b24de351a8; declaration blind-fourth-round-001.json22:14:59.256683Z, launch22:15:03.950027Z, pipeline completion22:17:30.479674Z. No best.py or reserved-D input changed. The unique D pipeline still waits for23:00Z.

## 2026-10-31T22:20:53.489848+00:00:846 numeric-input archive and current storage check

CONFIRMED: the independent aggregation is now reproducible from59exact input archives, including the original append-only afs6 result prefix. The root separately decompressed all59 archives and checked compressed and original hashes and lengths (41,153,219 original bytes). The archive reconstruction verifies3,384 selected row payload references and all846/804/448/416/406 tables. Evidence: reviews/economy-gate-846-review-001.archive-addendum.md and root-archive-check.json. OPEN: the full earlier REPORT.md prose could not be recovered; the challenged sentence is quoted in the sealed review, and the newer report is retained as a separately dated snapshot. No numeric input is missing. No game or policy call was made for this audit.

The owned-file scan completed2026-10-31T22:19:50.127085+00:00: 2599819913total owned bytes and130303492096free bytes, with no concrete absolute paths in scanned text. The sole generic path-rejection guard is unchanged. This leaves about400MB below the3GB lane limit before further research and D.

## 2026-10-31T22:21:32.197818+00:00: Reader-facing T/U mechanism explanation reviewed

The worked comparison is in experiments/validation/analysis/blind_fourth_round/EXPLANATION.md, SHA256d51faf5793a3032e314e6536edda051473bb7d2b524691ce58046eb0f33b9e70. It separates public timing, persistent state on actual observations, the mistaken H forecast against S and the later full-game loss. The review caught and corrected a draft sentence suggesting both members receive decision4; only the selected member is called then. The reviewer was the checker author, so this is a separate narrative review rather than an independent reimplementation. Verdict CONFIRMED for this exact finite narrative, reviewSHA385131ef2d0766f00461cb4a004d33015613f253c810228a227e39fe2d33ab3d. No new games or policy calls. Lead may use the explanation as a compact account of161/162; finalbest/D unchanged.


## 2026-10-31T22:24:06.777212+00:00: Exact frr1 equilibrium independently checked; prospective V counter

**Claim.** For the recorded standard-start ten-policy W/D/L matrix, every optimal mixture puts one third on g1, one third on guard00, and splits the remaining third over AS1C, best_v9f and P5TNUBM. **Method.** Independently parse all 90 retained games, 45 pairs in both seats, verify terminal labels and available source identities, and prove both necessity and sufficiency with exact rational primal and dual certificates. Root read the full standalone proof and review and checked the three-column inequalities. **Result and verdict: CONFIRMED for this matrix.** No new games or policy calls were made. The optimal row and column sets are the same set S, and all equilibrium profiles form S x S. The five other strategies, including best_v9e, have zero weight. This is stronger than weak dominance alone.

Lead: please explicitly say the ten self-play diagonal entries are imposed as zero, not measured. Both physical assignments agree on each off-diagonal W/D/L and HP margin; they are one game per ordered pair, not repeated stochastic trials. The audit checks 76 distinct Python source files across loaded and static closures. The initial records bind the JSON rules object, but these source digests do not authenticate historical runtime witness JSON. The retained artifact check also cannot establish absence of erased attempts or temporary historical edits. These limits do not change the exact theorem about the displayed matrix. Evidence: experiments/validation/analysis/frr1_equilibrium/PROOF.md, SHA256 e6656f1850ba2cf85deea5170edfcd5a73ab7a53db3830bcb34a7dbcdefd035d; reviews/frr1-equilibrium-review-001.md, SHA256 558fdf02434067cf66de4de37e984ed684740a2d5ff4c088260cf9f796885704. The exact reviewed report paragraph is archived separately. This is an exchange with the Opus 5.5 lead through the existing team notes.

The next counter V has a written first-five-round source proof at analysis/fourth_round_wall_counter/PROOF.md, SHA256 d963f2d9cf20e6c764a37258b145970fbe137d4beec0c80c8850a94b1011f93f. It matches H's first three factory-only rounds, builds guard00 walls and splash in round four, then buys one tier4 in round five. Thus T and U commit to L4 before seeing the new walls. The proof predicts their six tier2 copies all die in round four and that V first hits for60 in round five. Full-game outcomes are OPEN. Implementation and a ten-game declaration against T,U,G,best_v9e,AS1C in both seats are being prepared and reviewed; no V constructor, decision or game has run. Its round-six continuation is the cold default Fortress38 callable, constructed once and not called in rounds one through five. D and final best.py remain unchanged.


## 2026-10-31T22:30:02.989886+00:00: Conditional fourth-decision selection bound reviewed

Claim: for correctly advanced G/U selectors committed by decision four, the common three-round H/V opening prevents an identity-free public-history choice from depending on the opponent. Under the separately stated complete-continuation payoff premise G/H=-1, U/H=1, U/V=-1 and G/V=q, the restricted max-min value is (q-1)/(q+3). Method: standalone informal source proof, exact rational algebra and an independent source review, with no policy constructors, decisions or engine calls. Result: the conditional theorem is CONFIRMED; the numerical V application remains OPEN. At q=0 the unique probability of G is2/3 and the value is-1/3. At q=1 they are1/2 and0. At q=-1 every probability is optimal with value-1.

Evidence: experiments/validation/analysis/fourth_round_ambiguity/PROOF.md, SHA256e2beead506f57753d722fff5f0724bdf1e66d9068311823df9b1945c05fec757, and reviews/fourth-round-ambiguity-proof-review-001.md, SHA2566c9f8c287b923bd05572c4c300fe369511fff8708e89606de5e03961f7eaddb7. The proof excludes raw-name, process, timing and pending-action side channels. Whole-game clock coupling remains an explicit additional assumption; this is not an unrestricted game bound. Protocol163 remains source-only pending the final independent executable review. A zero-new-policy-call application checker is being prepared for the eight required retained outcomes after163. The final candidate and the unique23:00 D waiter are unchanged.


## 2026-10-31T22:34:16.078145+00:00: V counter prospectively declared and launched

Claim: V's fourth-round wall should invalidate the H forecast after T and U commit to L4; full outcomes remain OPEN. Method: the independent source review is READY (reviews/fourth-round-wall-counter-independent-review-001.md, SHA25655f398436f61dfa0651458600ccdda2b926cc918163e20ca541193a486d80596). Root read it and sealed protocol163 at2026-10-31T22:33:35.728173+00:00,137active source/data pins, declarationSHA2028decacd1afc6c560acc15eb4d58950ab22bb1b1d21d8a11e090e1d7092cb3. The ten new standard games are V versus T,U,G,best_v9e and AS1C, both physical assignments, with exact private opening and complete ordinary fresh audits. The one-core pipeline started2026-10-31T22:33:43.650015+00:00. No V policy calls preceded declaration.

The source review supports the opening argument, not the eventual win hypothesis or later private-state equivalence. Additional private checks cover only the first five rounds of the four T/U cases; complete ordinary fresh regeneration covers all reached rounds of all ten games. The corrected scope and unsealed earlier draft are retained. Final candidate and reserved D remain unchanged.


## 2026-10-31T22:36:36.456891+00:00: Final pre-D report review, three precise corrections

Claim: the current lead report still needs three scope corrections. Method: a second independent read of REPORT.md SHA25602a41100735dfea94e069f47bad11b9614d0a3d618c18895d6920e713448bcfc against the completed aggregation, exact matrix proof and current frozen planner. Result and verdict: CONFIRMED. Root read the full review at experiments/validation/reviews/report-final-pre-d-review-001.md, SHA25648f41d1f33d23fc156514454c3e432002a979987864cc829ae04535a2756235e.

Lead: (1) label846 and448 as weighted pool memberships. They cover804 and416 distinct full-spec/scenario/seat conditions. Ten of the416 also belong to selection pool f5t, leaving406 exact-condition-disjoint conditions. Their g1/base totals are350-14-42 and290-58-58. Keep the existing weighted table separately; retrospective condition disjointness does not establish unseen-policy exposure. (2) Before the frr1 proposition, state that its ten unmeasured self-play diagonal entries are set to0 by convention. The exact theorem is correct for that defined matrix. (3) Sections2/7 still call v41 final; call it a former finalist and include the actual final fortress v46 in the clock-limited examples. Its frozen plan retains TIME_BUDGET=3.0.

The review confirms the existing general clock caveat and pending report-only D status. Previously corrected ab15, fresh56 construction bias and poolC selection wording are not new objections. No new games or policy calls were used for this report review. The owned-file scan at2026-10-31T22:35:31.105542+00:00 found2606914093bytes with no concrete absolute paths; free space129126170624bytes. The V163 game batch completed22:35:25 with4W6L and all strict/replay/data checks passing so far; complete fresh/private auditing is still pending, so this is not yet the final163verdict.


## 2026-10-31T22:40:08.656454+00:00: Protocol163 complete, with targeted wins and six retained losses

**Claim.** V, FourthRoundWall, exploits the shared fourth-round response of T and its unconditional L4 control U. **Method.** Ten prospectively declared standard-start games against T,U,G,B,N in both physical seats, complete unchanged-engine replays, strict source/action and data audits,696 fresh external decisions, and a separately journaled first-five-round private comparison on the four T/U histories. **Result.** H1,H2,H3 are CONFIRMED. V beats T and U800:-546 at round12 in both seats. V loses to G680:740 and to B/N755:800 at round50 in both seats. The total is4W/0D/6L, not evidence of general dominance. The V/T and V/U full normalized histories match within each V seat. Final audit completed2026-10-31T22:37:11.017297Z, receipt `analysis/fourth_round_wall_counter/verification/full_games.json` SHA2561d200095e79e23b5179ccca59911ea2eb878835ab479b67c2e6b0e92d7f92aa8.

At decision4 V has291gold,17factories and an empty map. The correctly advanced H model predicts splash(10,1), against which six tier2 hits would deal72damage. Actual V builds the20-wall guard00 route and splash(1,3); all six combat copies die. V buys one tier4 at decision5, then delegates from decision6 to its cold default Fortress38. Additional first-five entrypoint calls were V20, selector20, independentG12 and independentL4 20. Nested calls are subsets; the four cold reference F38 constructions made zero reference F38 decisions. Later private-state equivalence was not freshly compared. Full histories are finite clock-sensitive reproductions. No best.py or reservedD change.

## 2026-10-31T22:40:08.656454+00:00: Protocol164 retained-game application complete

**Claim.** The four G/U by H/V histories have the same normalized public prefix through decision4 in each physical selector seat, and their payoffs give the proof's two-response ambiguity. **Method.** Declaration at2026-10-31T22:38:54.019244+00:00 pins8278 inputs; eight retained complete Engine replays and24 additional opening round steps, zero new games and zero policy imports, constructors or decisions. Exact physical roles and full specifications are joined; original audits, source archives, five data inputs and current executable helpers are authenticated. **Result.** H1 and H2 are CONFIRMED. In both seats the measured table is G/H=-1,U/H=+1,G/V=+1,U/V=-1. The conditional exact optimum chooses G with probability1/2 and has value0; each pure choice has worst payoff-1. All8279 checked physical inputs and28992 exposed input edges pass. Receipt `analysis/fourth_round_ambiguity/verification/full_check.json` SHA2565d60a0586075e25682e48dea3636e8fc56043d48f552325cea029713e1b8ae2b, completed2026-10-31T22:39:14.240550Z.

**Scope.** The proof is restricted to correctly advanced G/U members, the common opening, irrevocable commitment by decision4, normalized identity-free public information and opponent-independent private randomness. Complete selected-continuation payoff coupling remains an explicit hypothesis because planners have time limits. This is neither a run of a randomized selector nor a bound on arbitrary policies. The source review corrected historical-versus-current helper authentication and audit-error-versus-counterexample classification before declaration. Post-result independent review is pending.


## 2026-10-31T22:43:05.955924+00:00: Independent163 narrative and164 application reviews complete

CONFIRMED: root read the full independent reviews and accepted the bounded interpretations. Protocol163's final explanation is `experiments/validation/analysis/fourth_round_wall_counter/EXPLANATION.md`, SHA256a4a53b0a6e37858ff38f60b5667e54ea36ede26baea518a50caf361ed166edd8. Its independent review is `reviews/fourth-round-wall-explanation-independent-review-001.md`, SHA256ce825bd145edb1c3ccf8f0b2628a7bceb4fef9f92a1db70827ca71b396a2f85f. Root separately checked all33 review inputs and reconstructed the original narrative's exact preserved bytes from the amendment. The new `verification/narrative_publication_001.json` binds the final article, old author check, amendment and independent review without changing the original experiment declaration.

Protocol164's independent results review is `experiments/validation/reviews/fourth-round-ambiguity-results-review-001.md`, SHA256bbb80b932ee334cd26e17a5d4534c5a942739ee684e8fd9114044c70cd167ffb. It rehashed8279physical inputs,94active pins and188compressed identities, independently reconstructed all8normalized prefixes from recordedJSON and checked bothphysicalpayofftables and exactrationalcertificates. No policy or Engine call was made by either review. All reviewed files and scopes are bound by `analysis/fourth_round_ambiguity/verification/result_review_publication_001.json`. Both reviewers are GPT-6Astra; actual Opus5.5 collaboration remains the documented lead/economy work.

The terminal95-pin pre-D check passed again at2026-10-31T22:40:53.910181Z (`dependency_supplement_pre_d_002.json`), zero games/calls and no parsedDparameters. The single scheduledDpipeline remains unchanged. Leadreport22:39:55 has now applied846/804 and448/416/406 qualifications and the imposedfrr1diagonal. Sections2/7still need to callv41aformer recommendation and explicitly includev46's time cutoff. Its newfrr3extension is under independent review.

## 2026-10-31T22:46:48.150692+00:00: frr3 matrix confirmed; final-report runtime scope corrections

Claim: the 20 retained frr3 games give v46 4W/4D/12L and preserve the prior matrix optimal face. Method: independent source/JSON review `bot_research/experiments/validation/reviews/frr3-extension-review-001.md` (SHA256 `da160ec42701dfd24a7c92ecc00fae8be65bc02426b1ad5b0136d9849138e758`), followed by my complete review/proof reading, ten-artifact hash check and independent 74-case timing reduction in `bot_research/experiments/validation/reviews/frr3_extension_review_001/root_review_001.json` (SHA256 `03be6b208ebbf518b08b6bc90a3fc3a70319e30f7af8b1f10c15be31544e6a10`). Result and verdict: **CONFIRMED** for those finite outcomes and the matrix extension **with the unmeasured v46 self-entry explicitly imposed as zero**. v46 and v41 share the WDL row, not the full HP or action history. All 20 physical assignments and accepted actions were checked in the independent audit; no new games were added.

Required report correction: protocol151's 0.30-second CPU maximum applies only to the two high-factory histories (exact 0.29886853). Across all 74 histories / 1,204 calls, the shortcut implementation's maximum is 0.837026346, C-mirror_7493_3-03-side0, round4, foreign branch. An overall 0.30-second claim is **REFUTED**. These paired measurements include untimed eligibility preflight and shared caches; protocol152 separately gives 0.207627 CPU seconds on the two high-factory histories with no preflight. **OPEN**: global claim that no outcome depends on runtime. The directly supported statement is that completed games incurred no runner timeout; clock-limited opponent planning need not be load invariant.

Please reconcile sections2/7's final-version labels: v41 was used in frr1/frr2, v46 in frr3, and defense notes22:39 name v48 as that lane's new final recommendation. Frozen v46 and v48 both retain the three-second planner cutoff. Keep measured frr3 results labeled v46. The detailed review applies to retained report snapshot SHA256471620efbf169a2f9118b58c2c2a1fd640b8640c00de05bc034e67044e3175af; it does not assert the moving report is unchanged.

## 2026-10-31T22:48:44.515065+00:00: Adaptation findings guide independently checked and published

Claim: the O/P/Q/R/S/T/U/V sequence and protocols159/160/164 can be read as a finite, auditable adaptation study. Method: research-storytelling guide `analysis/ADAPTATION_FINDINGS.md`, author binding `bot_research/experiments/validation/reviews/adaptation-findings-author-inputs-001.json`, independent review `bot_research/experiments/validation/reviews/adaptation-findings-independent-review-001.md` (SHA256 `e3a24dcd63e031148ef8851b173fac56a11b36997cfded8fed83053fd7f81c8e`), and root rehash of 197 distinct bound inputs. Result and verdict: **CONFIRMED** for the guide's reported finite outcomes and explicitly conditional two-response bounds. The reviewer joined150 receipt mentions to126 distinct original results, checked all16 local links, all16 Q/S paired conditions and six complete stored-history equalities. These are reused evidence references, not extra games. Publication receipt: `bot_research/experiments/validation/reviews/adaptation-findings-publication-001.json` (SHA256 `ab386cc7f7fea9816ebf5f28c5674922602c7e8e7fec146b0d6266479a6afdad`). Guide SHA256 `b371dd4205158191d72499c8efe57a35b33d1ff418467ca725356f1228891cba`.

The guide retains the six V losses, the distinct action-replay/fresh-policy/private-state scopes, the five-round limit of V's additional private audit, and the full-continuation coupling assumption in protocols159/164. It does not claim an infinite counter cycle, a universally strongest bot, or validation on reserved D. The analysis reading index now links it first. This closes the development writing; the already scheduled, unchanged D pipeline remains the next empirical task.

### 2026-10-31T22:54:10.498086+00:00 Supplementary final-D reader prepared; execution remains pending

Claim: a separate read-only posthoc review is ready to authenticate the completed terminal evidence. Method: a separate GPT-6 Astra reviewer prepared `experiments/validation/reviews/terminal_final_independent_001/read_final.py`; root read all 598 source lines and its preparation documents. Input hashes and scope are in `root_preparation_review_001.json` beside it. Preparation made no policy, constructor, Engine, replay or game calls and did not open D parameter values. Result: the reader requires final publication followed by a post-D 95-pin check, reconstructs all 96 declared conditions, checks complete primary records and retained replay/entry receipts, and distinguishes two fresh executions from three histories. It rejects hidden failures and any additional retry campaign for separate review. Verdict: CONFIRMED for preparation only; empirical D findings remain OPEN. The existing core-28 pipeline is unchanged and waits for 23:00 UTC.

### 2026-10-31T22:56:40.932661+00:00 Supplementary reader preparation amendment

Claim: the publication-path sanitizer amendment preserves the reader logic. Method: root decompressed the retained original source and verified that the new file differs only by equivalent construction of generic root strings; both preparations and the previous root review remain retained. Result: revised reader SHA256 `1dadaa406d84694c652b104ead57c8758dda59c0e861d3cf057b4bf484486fb0`; root receipt `experiments/validation/reviews/terminal_final_independent_001/root_preparation_review_002.json`. Verdict: CONFIRMED for this source amendment, with no functional execution or D inspection. This is outside the frozen D pipeline and changes none of its 85 original or 95 supplemented pins.

### 2026-10-31T23:00:10.833553+00:00 Late economy sweep independently checked; follow-up recommendation still OPEN

Claim: af5 is the value selected by the recorded sweep rule. Method: supplementary GPT-6 Astra review `experiments/validation/reviews/economy_final_gate_001/INTERIM_REVIEW.md`, read with `CHRONOLOGY_CLARIFICATION_001.md`. Root read the source and reviews, verified all 466 captured originals from their compressed snapshots, and separately counted the completed afs5/afs6 rows. Result: af5 264W0D26L and af6 238W4D48L over 290 unique conditions each; g1 has 228W14D48L. Both qualify under the stated per-pool tolerance, and af5 has more wins. The 846 named-pool occurrences reduce to 804 unique conditions, partitioned by 145 sweep plus257 remainder specs, both seats. Verdict: CONFIRMED for sweep selection. In this exact22:56 snapshot afq56 is54/86 and afg5 absent, so recommendation remains OPEN. The follow-up interval upper-endpoint-at-least-zero gate is a non-refutation rule, not a superiority or noninferiority guarantee. Fresh56 is candidate-new follow-up on known research families; keep its28 W3 specs separate from the15-spec complement for comparisons with best_v9e.

Chronology clarification: the notes report that rule/code preceded the first disclosed test that printed50 partial rows and that the rule did not change. Stronger independent chronology is not established. The reviewer's earlier contrary message is withdrawn; exact originals and the dated clarification remain retained. This review made no policy or Engine calls and did not inspect D values. Root receipt: `experiments/validation/reviews/economy_final_gate_001/root_interim_review_001.json`.

### 2026-10-31T23:00:28.007371+00:00 Terminal D started after the declared gate

Claim: the unique scheduled terminal pipeline began the reserved validation after23:00 and final selection. Method: read its actual gate event and newly written frozen campaign record. Result: gate passed at2026-10-31T23:00:02.836289+00:00; campaign started2026-10-31T23:00:03.171603+00:00, candidate SHA256 `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. The pipeline is running on core28 and retains all original checks. Verdict: CONFIRMED for start chronology only; empirical outcomes and completion remain OPEN. Receipt: `experiments/validation/analysis/terminal_reserved_validation/verification/start_event_001.json`. No candidate or source revision follows this reserve.

## 2026-10-31T23:03:45.175568+00:00: Report timing corrections accepted; frr4 wording correction

Claim, method and result: source-only reinspection of the current report and all 24 frr4 result rows. CONFIRMED: the runtime paragraph now restricts the 0.30 CPU-second maximum to the two high-factory histories, gives 0.84 across 74, identifies shared-cache preflight, and states that clock-limited opponents are not shown independent of machine load. The broader cutoff list now includes v48. This resolves the material runtime objections in the 22:46 review. REFUTED: frr4 wording "2385 in seat 0 against every opponent". The asym:23:2 v46-versus-v41 seat 0 row is +5455; replace by "2385 against the five opponents other than v41; 5455 against v41". The same paragraph already states 5455 parenthetically. Exact report/result snapshots and root check: experiments/validation/reviews/report-late-acknowledgment-001/review.json. The independent frr4 raw-log/source review continues; frr5/frr6 remain separate incomplete evidence. Pool D primary batch 1 completed 29/96 conditions with 0 failures and its prior-use audits are now running; this is not final completion.

## 2026-10-31T23:07:07.491386+00:00 Final report frr4 wording: seat-one wins and timing scope

Claim: v46 is the only tested bot that wins asym:23:2 from physical seat 1. Method: root independently reread all 60 frr2 result rows and all 24 frr4 rows; the concurrent source/raw-log review identified the same issue. Result: five non-v46 bots (best_v9e, best_v9f, AS1C, V29 and g1) each beat v41 from physical seat 1. v46 wins all twelve of its asym:23:2 conditions. Verdict: REFUTED as currently worded in the report summary and section 5.16. Correct wording: v46 is the only tested bot that wins this start from seat 1 against every other tested bot.

The maximum-call timing parenthesis should say games ending at round 50: no per-round timing record identifies the round of the maximum call. This is an OPEN wording ambiguity, not evidence against the numeric maxima. The earlier 2385-versus-5455 exception remains as reported at 23:03:45Z. Root evidence: `bot_research/experiments/validation/reviews/report-late-acknowledgment-002/review.json`, SHA256 `2af5a45cc3a19bbbef82868d3f251788b6a5f41b75d835905559e096d8e8f7a0`; exact report and result bytes are retained as verified gzip inputs. No new games or policy calls. The fuller independent frr4 review will also distinguish the x215 :decide specification from frr4 :@make when describing repeated conditions.

## 2026-10-31T23:12:28.956932+00:00: completed frr4 independent review and provisional D completion

Claim: frr4 contains 24 distinct completed v46 conditions with 22 wins and two draws. Method: separate reviewer audited all 1,252 round/player records, accounting, terminal outcomes and source identities; root verified all 166 archived originals, 130 sealed review files and the separately captured balanced rules, and independently recounted 425,716 accepted actions and 602 game rounds. Result: counts agree; zero rejected actions, bot errors or scripted-round exceptions. Verdict: CONFIRMED for these retained records, not a fresh policy execution or combat replay. Review: `experiments/validation/reviews/frr4_final_fortress_001/REVIEW.md`; root receipt SHA256 `9c07bb6ae837039ef0a99bfc380eb0a38d045846508c9b2d1a6c1d5447ef4fbc`. The previously posted physical-seat-one and 2,385/5,455 wording corrections remain applicable. Only ten initial frr5 games received full raw review; its later partial status and frr6 are not completed results.

Terminal D primary run completed all 96 conditions at 23:11:44Z: standard 26W/6D/0L; continuation starts combined 60W/0D/4L. The strict audit reports no invalid conditions or failed attempts. Verdict: OPEN for full final validation pending existing replay, fresh-entry and publication pipeline. Four continuation losses are retained, and no D-driven revision will be made.

## 2026-10-31T23:14:16.389572+00:00: frr4 reporting corrections acknowledged

Claim: the current report implements all corrections from the frr4 review. Method: read and archive the current report bytes, SHA256 `d9513b61f50b051727ccea951d0c3a1e3468b33297d75d999859c62dd8f78c58`. Result: the v41 margin exception, physical-seat-one quantifier, maximum-call timing limitation and entry-wrapper distinction are explicit. Verdict: CONFIRMED for this captured report. Receipt: `experiments/validation/reviews/report-late-acknowledgment-003/review.json`.

## 2026-10-31T23:19:17.165196+00:00 Independent D loss accounting; final entry audit still running

Claim: the four primary D losses have the same complete normalized history and terminal purchase/damage accounting. Method: independent review `experiments/validation/reviews/terminal_loss_accounting_001/REVIEW.md`, followed by root rehash of all 577 inputs and six sealed files and a separate parse of the four original logs. Result: all four end round 35 at candidate/opponent HP -3120:785. Candidate buys only 400 factories (8000 gold); guard buys 281 tier5 and 20 factories (183050 gold). Its 28 base hits cause 3920 damage. Candidate retains 1096319 gold before 134332 terminal income. Verdict: **CONFIRMED** for recorded accounting. Whether another decision could save the game remains **OPEN**. No D-driven policy revision or new game. Root receipt `experiments/validation/reviews/terminal_loss_accounting_001/root_review_001.json`.

The two guard settings differ only in round-one branches that the prescribed prefix skips; their continuation delegates therefore see the same inputs, conditional on equal clock-dependent branches. This explains the finite equality without claiming load independence. All 96 raw histories produce 44 distinct canonical histories (15 standard,14 mirror,15 asymmetric), and all48 physical-seat pairs agree. The primary table is 26W/6D/0L standard,32W/0D/0L mirror,28W/0D/4L asymmetric. All original-engine replays passed; final fresh-entry and postchecks remain pending.

## 2026-10-31T23:21:15.287277+00:00 Completed economy fresh56 review and explicit metadata amendment

Claim: af5 passes the declared fresh56 interval gate. Method: independently rehash all255 archived review inputs and14 publication files, join exact opponent specs and both seats, recount three policies and rerun the declared4000-resample clustered bootstrap from archived bytes. Result: af5 78W0D8L, g1 70W0D16L,V29 42W2D42L on86conditions; af5-g1 mean+.093023 interval[+.023256,+.186047]. Verdict: **CONFIRMED** for18.22; overall18.26 recommendation **OPEN** pending afg5. Review `experiments/validation/reviews/economy_final_gate_001/FRESH56_REVIEW_003.md`; root receipt `experiments/validation/reviews/economy_final_gate_001/root_fresh56_review_and_relocation_003.json`.

The LEAD+FORTRESS subset is30conditions: af524W0D6L,g120W0D10L,V296W0D24L. The label NOT_BUILT_AGAINST establishes only membership in this non-W3 complement, not absence of targeting or unbiased sampling. afrr contains four exact repeated opponents fromfresh56(eightconditions), plus the constructor-level guard00 alias. Its af2g loss prediction is already contradicted by afq56(+410), while onlydefaultbest9e/9f are new exact H18.28a targets. Any repeat change should be called repeat variability unless its cause is separately tested; different load alone is not a causal demonstration.

Publication correction: the executed inspector stored one absolute source key. The original map is privately retained byte-identical; the replacement changes only that key to project-relative. All255 input values, timestamps, archives and numerical results are unchanged, with old/new digests in the amendment. This is a metadata correction, not a numerical rerun or erased failure.

## 2026-10-31T23:23:14Z Timing scope correction for report section7

Claim: calls below a planner's cutoff establish load-independent outcomes. Verdict: **REFUTED** as a general implication. The report currently says the frr1-frr5 fortress calls shorter than3seconds mean their outcomes do not depend on machine load through that cutoff. Their short observed durations can support nonactivation on those particular executions, provided the clocks behaved consistently. A slower execution can cross the deadline and take another branch. In addition, the frozen planner reads time.time while the harness times time.perf_counter; inferring nonactivation from their durations requires no relevant wall-clock jump. Please say: "Every observed call of these fortress versions was shorter than three seconds. With consistent clock progression this supports nonactivation of their three-second planner deadline in these recorded games; it does not establish invariance under different load." Remove the later exception that short calls prove load independence. No rerun or outcome change is implied. The final frr5/frr6 review will bind the full source and result evidence.

## 2026-10-31T23:26:30.755552+00:00: Final reserved pool D complete

Claim and verdict: CONFIRMED, all 96 declared games and complete source/replay/fresh-entry checks pass for selected SHA70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87. Per-start W/D/L: {'standard': {'W': 26, 'D': 6}, 'asym_130363_2': {'W': 28, 'L': 4}, 'mirror_104729_3': {'W': 32}}. 1532 fresh decisions per entry point; 160 skipped prefix rounds. 48/48assignment pairs have identical histories, with 44 distinct overall. Parameter overlaps0; prescribed-history overlaps0. All conditions and limitations: bot_research/experiments/validation/analysis/terminal_reserved_validation/RESULTS.md. Do not tune or select using D outcomes and then call them untouched final validation.

The final overlap-audit input bytes are preserved in bot_research/runs/validation/reserved-D-final-001-separation-inputs/manifest.json. Every recorded input version and compressed blob is checked before publication; later appends to team result streams cannot change those retained bytes.

## 2026-10-31T23:28:50.381527+00:00: Post-D checks complete and bvf comparison independently reduced

Claim: the completed D evidence preserves the starting protected tree and the declared source identities. Method: post_terminal_checks.py ran the95-pin verifier, original59-test suite, protected inventory comparison and owned artifact scan after pipeline completion. Result: CONFIRMED, all pass;9 optional tests skipped,903 protected entries unchanged,1002 prior absent entries and3 prior changed manifest hashes unchanged. Pipeline completed23:26:30.819242Z; postchecks completed23:27:52.558823Z. Receipt runs/validation/post-d-checks-001.json SHA14035e05f2daa67ca4ac520f6a2e5c21d8b6caceb0cf0c703c753edb2691e693; D final receipt analysis/terminal_reserved_validation/verification/final_candidate.json SHAc592dbd82ab91b081dc9f49eb125c681df115c5845caae7423aae878287371ae. Owned bytes at scan2692100050, free126152515584. The supplementary independent reader is next; its core29 guard needs an explicitly archived affinity-only core28 amendment because core29 is reserved for the fortress review. No declared source pins or experiment conditions change.

Claim: completed economy18.30 bvf numbers reproduce. Method: root read the two inspector/helper sources and review, verified233 archived inputs and9 sealed files, independently joined all86 conditions and recomputed five family tables and15 cluster-bootstrap intervals. Result: CONFIRMED; root receipt reviews/economy_final_gate_001/root_bvf_review_004.json SHA f6a5279649f21f0d94096d743421b298661532c3956abd1be23a0d0661ba1d2b. Full list best_v9e56W12D18L,af578W0D8L,g170W0D16L,V2942W2D42L. g1-best mean+.093023 interval[-.069767,+.255814] meets only the stated non-refutation gate, not superiority; descriptive af5-best+.186047[+.058140,+.325581]. On the30 LEAD_PLUS_FORTRESS conditions best_v9e20W8D2L,af524W0D6L,g120W0D10L,V296W0D24L.

To lead/economy: the phrases “15 opponents built against neither bot” and “bias shows in the split” exceed the demonstrated family membership. Call the subset LEAD_PLUS_FORTRESS or non-W3 provenance; this does not establish no prior targeting or causally estimate selection bias. A repeated condition changing outcome establishes a repeat discrepancy, not a load-caused difference without further evidence. These scope corrections do not change the numerical tables. af5's covered-pool gate remains OPEN until completed afg5 reduction;95percent agreement is a separate prediction. The completed bvf review is reviews/economy_final_gate_001/BVF_REVIEW_004.md SHAcad9ea371eb4a11fc82c2dc71a77cf47a42fa04ae61a7128e345311c935448bc.

## 2026-10-31T23:32:10Z Independent terminal reader completed and root verified

Claim: completed D evidence is internally consistent across the declaration, raw records, checks and publication. Method: supplementary standard-library reader completed at23:30:52.825327Z; root independently rehashed all2254 recorded inputs and13 postcheck inputs and verified2354 successful reader sections and the metric arithmetic. Result: zero issues,96conditions,44distinct histories,48equal assignment pairs,1532actual calls per fresh entry,160prescribed turns,1692wrappercalls. Verdict: CONFIRMED for source/JSON authentication; this adds no Engine replay, policy call or strength trial. Review reviews/terminal_final_independent_001/completed-review-001/REVIEW.json SHA4a4dd5a021329ce7b9968c9bcb06b1cc747fb6a2860f7b18cfbf315e97f51986; root receipt root_completed_review_001.json SHA9814353a57be479100ef6f4c4b4e448ea3eb048c5f619e4ae3c6c6378a7711a7. All previously stated unresolved-input, historical-identity and timing limitations remain. The guide is undergoing its final prose review.

The current report has accepted the23:23 clock qualification. Two remaining wording corrections from the completed fortress comparison: say44matched conditions across88games for frr3/frr5 and frr4/frr6, rather than44games across the four campaigns. Also qualify “This is the gold effect” after the10.07-versus14.03second comparison: larger visible rosters explain work in the profiled example, but the matched histories contain identical gold and do not causally explain the timing difference between those repeats. The independent fortress review is being sealed.

## 2026-10-31T23:36:39.566869+00:00 Completed validation guide and final fortress cross-check; report precision corrections

Claim: the terminal D evidence and the v46/v48 finite comparison are ready for the report. Method: root authenticated the independent D reader (2,254 identities), guide factual review (332 identities, the mutable report through its retained snapshot), and independently recounted all 88 frr3-frr6 histories and the exact rational matrix certificate. Result: D remains 26W/6D/0L standard, 32W/0D/0L mirror, 28W/0D/4L asymmetric, with 44 canonical histories; all 96 replays, 96 entry audits and postchecks passed. The guide is `experiments/validation/analysis/VALIDATION_FINDINGS.md`, SHA fb4931c66944cfa59058a2947214681d90d05d927b5ecd58b92875df340c19f2; publication receipt `analysis/terminal_reserved_validation/verification/validation_findings_publication_001.json` SHA d20dc86559b5b3d79686aede5d407599edd5d2e252572638d972acf21d98c3da. Independent final signoff is `reviews/terminal_final_independent_001/guide-publication-signoff-001/SIGNOFF.json`, SHA faa2ea62195661a28538cc9e5e23f9290dba091314a9501e28e2506b62b2d918. Verdict: CONFIRMED for the finite outcomes and documented checks. No D-driven tuning or selection.

Root frr3-frr6 receipt `reviews/frr5_frr6_final_fortress_001/root_review_001.json` SHA fc84c4cf0e428f446cb0e9a23c088cc2f2f08a57b877bedfd85b63059fcba389 authenticates 658 archive edges and 191 archive objects, then independently checks 6,272 raw records and 2,652,072 accepted actions. All 44 matched v46/v48 conditions have identical full canonical histories. Each gives 4W/4D/12L standard and 22W/2D/0L on the two scripted starts. The exact conditional finite-matrix proof admits any skew mutual payoff between v46/v48 and gives zero weight to both; it does not assume their unmeasured mutual match is a draw.

For the lead's new section 5.17, root read all 72 records of asym_130363_2-12-side0 and checked the earlier purchase timeline, not just the terminal round. The candidate has path 22 throughout, reaches 48 turrets at round 19 and never adds another, buys 14/8/300 tier5 in rounds 13/14/22, and buys only 400 factories in every round 23 through 35. The guard remains at 785 HP after round 2. Receipt `reviews/terminal_loss_accounting_001/report_d_accounting_002.json` SHA aeb8401017cda333b8c936ee940c1a56c8dece00525c914a02432f2929620871 binds report snapshot 0c44dfd2d0860e61959af61c3bc04d2d7b4234be139b8492a1359ee6078eee76. Please apply these precision corrections: (1) name the history counts explicitly as standard 15, mirror 14, asymmetric 15, since the table orders standard/asymmetric/mirror; (2) the guard reaches path 44 at round 9, not immediately after the prefix; (3) 26,696 and 183,062 are END-round 20/34 balances, visible for decisions 21/35; (4) call (8,2)/(9,3) gun coordinates, not roster positions. The saving-action question remains OPEN.

Two previously noted report corrections remain in this captured report: section 5.16 says '44 games of frr3 to frr6', but the count is 44 matched conditions across 88 games; section 7 follows the 10.07 versus 14.03 second P5TNUBM comparison with 'This is the gold effect'. Those matched histories have identical gold, so they do not establish a causal gold explanation for the elapsed-time difference. The independently measured high-gold cost remains supported; separate that mechanism from variability between equal-history runs. Verdict: CONFIRMED for the checked records; causal timing attribution and untested saving alternatives remain OPEN.

## 2026-10-31T23:38:50.811738+00:00 Completed AF5 gate independently recounted; exact strings and membership denominators retained

Claim: AF5 qualifies under the economy lane's declared standard-start recommendation rule. Method: root read the 005-to-008 correction and independently authenticated 351 archives, rejoined 2,412 raw candidate/baseline values, and reconstructed all 846 retained R13 base memberships and 14 named pools. No bot, Engine, game or replay was invoked. Result: over 804 distinct conditions (402 exact opponent specifications, both seats), AF5 gives 764W/2D/38L, g1 726W/16D/62L, and V29 546W/14D/244L. Over the 846 overlapping memberships the counts are AF5 804W/2D/40L, g1 764W/16D/66L, V29 584W/18D/244L. Multiplicities: 770 conditions occur once, 26 twice, eight three times. Root receipt `reviews/economy_final_gate_001/root_gate_review_008.json`, completed 23:37:57.903084Z, SHA a2e397edcdda875d58dbac67f2c5edabc2eccd15f04bae1d70257fac7283fb87. Independent review `reviews/economy_final_gate_001/FINAL_GATE_REVIEW_008.md`, SHA e87d01a4a1c74a81d8c4ff356880f6767b19d0e20c1dfa8ca1cd36f67f15e19c.

Every pool meets AF5 wins >= g1 wins minus two; GUARDED_MAZE is the sole negative difference, 142 versus 144. Together with the earlier independently checked fresh56 criterion and frozen sweep choice, the declared standard-start rule passes. The separate 95 percent WDL agreement prediction has 512/514 agreements. Its sole different exact spec, screened_guard_maze empty/growth8, improves in both seats; the other 512 conditions include 444 with different HP margins, so do not call this full history equality. The 290 sweep games selected AF5; the 514 remainder and 86 fresh56 conditions have their separate prospective roles. The full gate is not wholly held out. Verdict: CONFIRMED for this finite standard-start rule; scenario continuation scope remains OPEN pending the separately declared scnaf5. This does not select or revise the installed best.py, and does not use D for tuning.

The retained R13 base has 504W/64D/236L on 804 unique conditions and 524W/82D/240L by membership. Those files include literal frozen best_v9e and explicit older lead.v18/lead.v19 parameterizations. Their previously claimed twin relationship is separate from this recount: no new general behavioral equivalence is inferred here. The AF5-versus-exact-g1 gate does not depend on it. The initial reader005 preserved an incomplete null-result receipt when historical partial and completed afq56 records shared one logical path; reader008 separately binds the completed fresh56 data and excludes the AF5-only afq56 file from the g1/V29 baseline scan. No record or criterion changed, and both receipts remain.

The new AF5 standard-start round robin is being reviewed separately, including its effect on the old finite-matrix objective. AF5 against best_v9e after its choice is a new head-to-head condition; repeats and aliases are being identified. A difference on a repeated clock-sensitive match would not by itself establish a causal machine-load effect. The main report should retain the scope of the old ten-policy matrix when presenting any larger table.

## 2026-10-31T23:42:10.983322+00:00 AF5 round robin and retained repeat independently checked; one report margin correction

Claim: completed afrr is 16W/0D/4L, and afrep reproduces the best_v9e win in both seats. Method: root separately authenticated 185 archive edges and 18 sealed review files, independently joined all 20 afrr rows, eight exact fresh56 repeats, and both complete 102-row afrep logs. Result and verdict: CONFIRMED for these records. H18.28a is REFUTED for best_v9e, best_v9f and af2g, each +410 at round50; AS1C and P5TNUBM still beat AF5 by10. H18.28b and the post-exposure H18.33 repeat prediction pass. The repeat logs contain31,078 accepted action events and the same HP changes by policy role: round1 AF5=785/best=795; round9 best loses140 to655; round10 loses280 to375; no later HP changes. This authenticates the recorded damage accounting, not private policy reasoning or a causal load explanation. No policy or Engine was run. Root receipt reviews/economy_final_gate_001/root_afrr_afrep_review_001.json, completed23:41:55.063293Z, SHA39be0a1627df819dfd83a06d78d97692a858627de3312e35754b300b2f1e131b. The296/550 gate-membership partition was also independently reproduced; it represents290/514 distinct conditions, respectively.

Lead: the archived report5.16 frr7 paragraph (REPORT.md SHA74ad93d5c497dbe4c7d6c64d20d8d691b1fb89fed64e4592c1fd3aee04775b8c) incorrectly gives AF5's asym:23:2 seat0 wins over best_v9e/best_v9f/AS1C as4470. Each is790:-460, margin+1250, round14. The opposite-seat losses are-4470 at round21. Root checked the three result rows and terminal raw logs independently; receipt reviews/frr7_frr8_late_af5_001/root_report_discrepancy_001.json SHAb1513f391200b8a4b07a8381fdf4e5494ec987b0a5ee5dad45406e57acc30fe8. The AF5 extension of the finite WDL matrix has a complete informal argument under review, with exact row authentication still pending; it will be reported separately. The old ten-policy theorem remains valid for its defined matrix. D and the installed best.py remain fixed.


## 2026-10-31T23:46:34.889451+00:00 Late repeat timing correction and completed evidence navigation

Claim: economy18.34's largest AF5 afrr call of0.8seconds matches the records. Method: root read review012 and its reader, authenticated68 archived inputs and7 sealed files, and independently scanned the completed20-row afrr result. Result: REFUTED. The maximum is3.0694 elapsed wall seconds, result line8, AF5 physical seat1 againstg1; the row's physical-side maxima are[2.9157,3.0694]. Please correct18.34 and any report summary that repeats0.8. This does not change the standard-start recommendation gate. Evidence: reviews/economy_final_gate_001/root_repeat_narrative_review_012.json SHAbfe5d12e0b956f03e7e4f3e1015827f73a7dbbb2e56dcfee732aed141bb0cf94, completed23:46:23.144014Z; reviewed dated economy bytes SHA db4879ea466e5649345457ff94df4d2decde2d1075743bdce25bd6c15435c64f.

Claim: the recorded repeat mechanism is stable in the two inspected seat0 histories. Method: root independently compared all102 entries of original afrr game9 and afrep game1, plus the first10 round/player entries of afrr against the frr1 g1 control. Result: CONFIRMED, all event lists and complete repeat snapshots agree; the g1 comparison agrees through end round4 after removing only the snapshot name. This is retained-record comparison, not an Engine action replay or fresh policy regeneration. The earlier006 review authenticated afrr result values and did not inspect its raw winning histories; their absence was never established. The new all20-log review is pending. Round5-tier3 causal interpretation remains a conjecture.

The mutable analysis index now links the previously unlinked frr3 and final frr5/frr6 finite-matrix proofs, completedT/U/V and fourth-decision results, and the terminalD result table. Root authenticated384 archived Markdown inputs,383 equal current files and one separately archived mutable lead report, then added12 links without altering any sealed page. Receipt reviews/final_navigation_001/root_publication_002/RECEIPT.json SHA75113778f48ac7fe668c73dd018a559fccd96282bd84e99b489fedcf4fafedeb; index SHA491adf6bc5c548256502c89d712851755ad6b63d4881a0e48642021004dbabe6. The first strict current-equality attempt stopped before any index write when the lead report changed; that receipt is preserved. The AF5 matrix extension route will follow its completed independent check. D remains complete and unchanged.

## 2026-10-31T23:52:32.147179+00:00 Completed scenario control, original repeat logs, and final report corrections

Claim: H18.31a holds for all 120 declared scnaf5 comparisons. Method: root read the independent reader and review, authenticated 85 archived inputs and nine sealed files, independently rejoined all 360 selected records, and recomputed each scenario table. Result: AF5, V29 and g1 each give 113W/0D/7L, with identical recorded winner, candidate-oriented HP margin and ending round on every exact opponent/scenario/seat condition. The largest recorded AF5 call is 1.7023 elapsed wall seconds. Verdict: CONFIRMED for this finite control, not full action-history equality or arbitrary scenario transfer. The restriction triggered by an observed scenario mismatch is not triggered. No policy, Engine, replay or new game ran. Root receipt `reviews/economy_final_gate_001/root_scenario_review_007.json`, completed23:52:01.408514Z, SHA5474715b88bc615d85d2ed3ca580a1efb5ca7106569069af69e11e1472205fc5. Review `SCENARIO_REVIEW_007.md` SHA194395b830a4c2234864e072c2a33623c9d9135ffeb573ec3830fe14f90f51e4. AF5 stays the already selected economy recommendation; this does not change best.py or use D for tuning.

Claim: original afrr winning logs were absent. Method: root independently checked all20 log paths, 1,884 round/player records, metadata, terminal accounting and tournament retention source. Result: REFUTED. All20 originals are present, including16 wins. The one-scenario tournament marks that scenario first_of_pair for both seats, so KEEP=losses still retains all20. The006 review authenticated results and did not inspect these logs; later authentication must not be backdated. Root receipt `reviews/economy_final_gate_001/root_original_repeat_logs_review_013.json`, completed23:47:44.971481Z, SHAc979f54cb7b7dee4e04091a2b44729074f3732e6cfcf79a5f440ed884483b7ba. This corrects economy18.33's missing-log premise and complements the separate18.34 wall-time correction posted above.

To the report owner: the final source-only reading review finds six remaining publication corrections in the23:52:14 captured report. Root authenticated its32 archived inputs and seven earlier pins, rechecked the exact AF5-best_v9e rows and inspected command filename handling and integrity exclusions. Verdict: CONFIRMED for the dated report. Review `reviews/final_report_reading_001/REVIEW.md` SHAb62205f58a74058e646754add79f00ecc58cdff96c7b467fa19a9da5aa9f998d; root receipt `root_review_001.json` SHA596f846d37f47a20d868835786439261f495c03b5413721b259af2652140ed01.

1. Section5.15 still calls g1 the current recommendation and says best_v9e beats every lane's final standalone bot by5–15HP. Call g1 the former recommendation and include AF5's +410 at round50 in both seats. Restrict the all-round1 explanation to its supported earlier policies; the AF5 repeat has additional damage in rounds9 and10.
2. Section6 says round2 blind strikes beat “best_v9e and every candidate”. Name the early tested variants instead. AF5, g1 and V29 each win all40 TIMING2 conditions; unseen current purchases do not imply eventual defeat.
3. Section5.16 calls afrep a replay. It is a two-game policy reproduction after observing afrr. The separate canonical-history comparison is a retained-record audit, not an Engine action replay.
4. Section8's matrix, check_runs, rr_table and rr_nash examples need `bot_research/runs/lead/...` in their result-file arguments when run from the project root. Likewise qualify the historical `bash experiments/lead/freeze_v9f.sh V33C` command or add its `bot_research/` prefix.
5. Eleven-policy paragraph: four possibly positive coordinates leave seven zero coordinates. Replace “g1, best_v9e and the other six” with “all seven remaining policies”. The complete standalone necessity/sufficiency proof is under final root checking and will be linked shortly.
6. Section9's40-file inventory excludes both bot_research and .venv. State both exclusions; the separate903-entry w3 checkpoint includes the pre-existing environment. This is scope clarification, not a protected-file change.

One newly caught error is in our own sealed frr7/frr8 review: frr8 is AF5 790:735, +55 at round50 in both seats, not795:740. Its original audit JSON and result rows were correct. Root's independently written HP assertion stopped on this mismatch, and a separately sealed erratum is being prepared. The original review and failed attempt remain preserved. The finite WDL matrix is unchanged.

## 2026-10-31T23:56:59.581246+00:00 Completed AF5 matrix proof, terminal HP erratum and reading route

Claim: the added AF5 row changes the optimal mixtures of the specified finite WDL matrix. Method: root independently authenticated 1,363 archive edges, recounted 158 games with 9,234 records and 2,739,683 accepted actions, joined all 152 matrix-result rows, and checked the exact rational certificate and its standalone informal argument. Result: every optimal mixture gives AF5 and guard00 weight 1/3 each, with the remaining 1/3 split arbitrarily between P5TNUBM and AS1C; the seven other policies get zero. Every old ten-policy optimum is exploited by AF5, with AF5 payoff 1/3 plus twice its best_v9f weight. The proof also gives zero mass to the two fortress rows for any unmeasured AF5-versus-fortress entries in [-1,1] and any skew mutual fortress entry. No missing match was supplied as a draw. Verdict: CONFIRMED conditional on this finite WDL table, its imposed zero diagonal and the stated added-row hypotheses; not a theorem about all game policies, HP objectives or clock invariance. Read `reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md`, SHA 2d82fbdb2c2fc1f91f0f09656ab07489c73f60dc6a758432fe9ee3453e5d0240. Root receipt `root_review_002.json`, completed 23:51:55.322174Z, SHA 2494c99caf1970368b043be9cd89f72679d8a002f15866a6ce3109ea1753e5b0.

Claim: the associated original review's frr8 absolute HP pair 795:740 is correct. Result: REFUTED. Both retained games finish AF5 790:735 at round50, margin +55; each full 102-record history equals its g1/frr5 comparator after removing only match identity and snapshot names. The result JSON was already correct. The original erroneous review, its seal, the failed root detection and the separate erratum remain preserved. Root authenticated all 508 erratum inputs, six original archive edges and six preserved error/detection archives, then independently repeated the two complete comparisons. Corrective evidence: `reviews/frr7_frr8_late_af5_001/hp_erratum_001/ERRATUM.md`, SHA bb6d6a38d95ea39df7e1de115830ee91e8f4435f0afd49ff486cc023360dfb41; root `root_hp_erratum_review_002.json`, completed 23:55:54.263974Z, SHA 7dfb575ec6e7e87042695167b9e316e030fc37c8ca7cdc0b36d208d23775db3b. A draft erratum checker first used the wrong combined-snapshot shape; its failed script and explanation are retained separately, and the corrected checker uses the actual individual-snapshot format. No input or game changed.

The mutable analysis reading index now links this proof and explicitly gives the erratum precedence. Publication completed 23:56:09.904827Z, index SHA a06cddf3fc12a3432a5af9786673a474a6707f9b4b1e7474537738e882d53179, receipt `reviews/final_navigation_001/root_publication_003/RECEIPT.json` SHA c97f2b8f8730d359bbb813cbd5e60f86a5f92d13bffed73f901bc87336fb73bf. All sealed pages are unchanged. Final link and updated-report review is underway. Lead's 23:55:14Z note acknowledges all six previous publication corrections; independent verification is pending.

Economy18.35: its 120 scenario outcome comparisons are confirmed, but the proposed explanation that foreign hold forbids attack, finish and doom purchases until round11 overstates the source gate. The nested ordinary attack function checks hold; the separate finish and doom branches check attack_from without that guard. An open-case branch can separately suppress doom. A source review will state the exact control flow; merely finding a missing guard does not prove a reachable violating game. Treat the general no-purchase explanation as unestablished. The finite 120-result equality remains unchanged. No new games, policy calls, replay or D-based selection occurred in these checks.

### 2026-11-01T00:01:18.117635+00:00 Root-verified report addendum and foreign attack gate

Claim: the six corrections sent at 23:52 are incorporated. Method: read the archived 23:56:53 report passages, both archived economy chronology entries, and the full addendum; verify its eight compressed inputs, report capture, script and prior receipt hashes. Result: all six are substantively resolved. Verdict: CONFIRMED for report snapshot SHA5aa07ad836f4acfb4314c6299f34b27b74eaebcdd19b95650d7d9f197ad0a02f. Root receipt `experiments/validation/reviews/final_report_reading_001/root_status_addendum_review_001.json` SHA0515c2a0fbfe30dbeb0e4fec54bc488d2024048198f88e255f799fdcf788f552.

Two final report wording updates remain for the lead. The table's new “recommendation from/until 22:43Z” conflates selection with recommendation: economy18.26 at22:47:11 says dec22 selected af5 at22:43:35 for fresh evaluation and the recommendation condition is still open; economy18.32 at23:34:38 announces the standard-start recommendation after afg5 completed23:33:35. Suggested wording: “selected for fresh validation at22:43:35; recommended after the completed gate, announced at23:34:38”; call g1 “former standalone recommendation” without the22:43 cutoff. Also, the report's current “not proved by hand” phrase should now be scoped to the earlier numerical computation or replaced by a link to the completed conditional proof `experiments/validation/reviews/frr7_frr8_late_af5_001/af5_matrix_extension/PROOF.md`. The theorem remains conditional on the stated finite payoffs and imposed zero diagonal. Verdict: CONFIRMED chronology distinction and newly completed proof status.

Claim: economy18.35's parenthetical “no attack, finish or doom purchase before foreign_attack_from=11” describes a shared guard. Method: independent source/AST review of frozen econ29 SHA0c71ec9bc7b772313cc302ed1296b586cdcf98ea3bc2cdf1044e60f5220c855c, resolve exact AF5/g1 defaults, verify87inputs58archiveedges34new sealed outputs39original sealed outputs, and recount45retained histories2046records. Result: ordinary attack checks hold; finish and doom do not. They retain attack_from=5/7 and their other predicates. The open-case call can set attacked even when the ordinary helper returns under hold, suppressing doom. The45histories contain zero accepted minion purchases in356candidate rounds after the scripted prefix and before11. Of120scnaf5histories,17logs are retained and103 unavailable; all28frr7logs were checked. Verdict: REFUTED as a shared control-flow guard; a reachable legal-game violation remains OPEN. This does not refute the independently checked120condition outcome comparison. Suggested economy wording: “A possible explanation is the ordinary attack's separate foreign-map hold before round11. Finishing and doom retain their attack_from checks and bypass that hold, subject to their other predicates. This mechanism was not checked game by game.”

Source proof and evidence: `experiments/validation/reviews/frr7_frr8_late_af5_001/foreign_attack_control_flow_001/INDEX.md`; independent receipt `root_foreign_gate_review_001.json` in its parent, SHAee646bb88fe245bb3ebdf27665892d7e55370d66ce1470f561d38be7c62d5215. Navigation004 added its reading route at00:00:58.681366; analysis/README.md SHAd712c22354dabac72c70efc479ee62a294e9c9a389ac73760c46b8d0d7ce8df2; publication receipt SHAbfbda2f0d2c731ade4c338c05e72acc532d265029c7ff835fcde2db6664485cd. No policy, game, engine, replay or test was run. D and installed best remain fixed. All new prose findings are source and retained-record claims, with actual Opus5.5 collaboration through the lead/economy notes.


## 2026-11-01T00:05:26.513709+00:00 AF4 development audit, final proof navigation and report correction closure

Claim: the completed AF4 sensitivity run supports economy18.36's finite comparison. Method: root read the independent reader and review, authenticated 233 archived inputs and eight sealed outputs, checked 174 source paths, and independently rejoined 1,450 selected rows for the same 145 exact opponent specs in both seats. Result: AF4 162W/2D/126L, AF5 264W/0D/26L, AF6 238W/4D/48L, g1 228W/14D/48L and V29 48W/12D/230L. AF4 is better than AF5 on 16 conditions, worse on 118 and equal in WDL on 156. Its mean score difference is -0.348276, with the specified opponent-cluster bootstrap interval [-0.441379, -0.251724]. On the 28 STRIKE1 conditions AF4 wins 22 and AF5 12; the score difference is +0.357143 [+0.142857, +0.642857]. The bootstrap uses W=1, D=0.5, L=0, 4,000 resamples, seed 1 and both seats kept together. Verdict: CONFIRMED as development evidence on specs selected for V29/g1 disagreement, not a random sample of opponents. The AF4 component of H18.31b holds; its combined AF3 component remains OPEN until that run completes. Largest recorded AF4 call: 2.3101 elapsed wall seconds. No causal load conclusion follows from these records.

Evidence: `experiments/validation/reviews/economy_final_gate_001/AFS4_DEVELOPMENT_REVIEW_014.md`, SHA b37deb3ffa4a026c0322d51ca7c899f4ed158102689e3b0bdb06a692a4697cc3. Root receipt `root_development_afs4_review_014.json`, completed 00:01:58.964806Z, SHA aced7f3074f3023a04e754a108ac4aba2cb5e87575f2c9a0668b6f9d040c4100. No new game or policy call was used in this audit; AF4 is not a new recommendation and D is not involved.

Claim: the completed validation index gives access to the identified standalone proofs. Method: root read both static readers and the final signoff, authenticated 1,165 Markdown archive edges, 19 additional archives and seven pins, verified all three append-only index publications and independently traversed the final link graph. Result: 392 Markdown documents and 372 parsed links, zero missing targets or anchors, all 169 identified proofs reachable. Verdict: CONFIRMED within the declared static inventory and parser. There are 98 RESULTS pages, of which 82 older pages are not linked in this graph; this is disclosed, not claimed complete results coverage. This is not browser rendering, full CommonMark interpretation or a renewed semantic check of every old proof. Index SHA d712c22354dabac72c70efc479ee62a294e9c9a389ac73760c46b8d0d7ce8df2. Root receipt `experiments/validation/reviews/final_navigation_001/root_final_signoff_review_001.json`, completed 00:02:34.186642Z, SHA 2adefbf06d9e0a4e69f6d1e239a7e1573888feb3288090debc85a72960de34c2.

Lead's 00:01:52Z acknowledgement is independently verified. Root read the complete diff from the prior report snapshot, archived the current report and six inputs, checked its new AF4 counts against the independent receipt, and confirmed equality with the lane's final report copy. The remaining AF5 selection/recommendation chronology and proof-status corrections are closed for report SHA b006e7cabd89e5119d5d812e77a5b76fa8192b29bb47596e1466055f9daf7379. Receipt `experiments/validation/reviews/final_report_reading_001/closure_001/RECEIPT.json`, completed 00:04:53.228075Z, SHA e2fd1d86f08d832033462545532f228c51affb9f38c9faddd38f07a6046531af. Verdict: CONFIRMED for this dated correction check, not later report edits. The report does not repeat the foreign shared-guard explanation. Economy18.35's corresponding source correction and the earlier afrr timing/log-retention corrections are still awaiting acknowledgement in that lane's notes. The independent numerical results are unchanged.


## 2026-11-01T00:06:20.672300+00:00 Completed AF3 sensitivity independently verified; research computation finished

Claim: the combined H18.31b prediction holds on the completed development sweep. Method: root read the full new addendum, verified its ten sealed files and 237 archived inputs, rejoined all 1,740 six-policy records, checked 174 current source paths, and independently recomputed every pairwise and pool reduction. Result: AF3 is 146W/0D/144L in 290 conditions. AF4 has 162 wins and AF5 264, so both parts of H18.31b hold. The wins for attack_from=2,3,4,5,6,7 are respectively 48,146,162,264,238,228 on these 145 exact opponent specs in both seats. Verdict: CONFIRMED for the selected development set. No held-out validation of AF3/AF4 was added, no recommendation was changed, and D remains report-only.

AF3 versus AF5 has 18 better, 136 worse and 136 equal WDL outcomes, mean score difference -0.406897 with the declared descriptive bootstrap interval [-0.503448,-0.303448]. Against AF4 it has 26 better, 42 worse and 222 equal, mean -0.058621 [-0.134483,+0.017241]; this interval includes zero. In STRIKE1 AF3 wins 24 of 28 conditions, AF5 12; difference +0.428571 [+0.071429,+0.714286]. Procedure: W=1,D=0.5,L=0, exact opponent clusters retaining both seats, 4,000 resamples, Random(1), sorted endpoints 100 and3899. The largest AF3 decision is 1.9184 elapsed wall seconds. No bot errors, rejects or source-change flags were reported. Same outcomes across physical seats do not establish full-history equality or causal load independence.

Evidence: `experiments/validation/reviews/economy_final_gate_001/AFS3_DEVELOPMENT_REVIEW_015.md`, SHA339ed73252eb56f130fd942984db4c42cb5f2a161d6a5b550f806357748a0c2a; manifest SHAeb2b6792ea82e0d96ba5edd0ca4a184b12fcaee5b3324d721ead69ec4c43d613. Root receipt `root_development_afs3_review_015.json`, completed00:06:07.275019Z, SHA34a0499bc4fd8c0d56fed7a1142530b0456e54e9ae2addb171b9486d4b3d5e69. The unchanged general root reader also checked the AF3-versus-AF4 comparison before writing this receipt. At capture the economy notes still ended at18.36; this audit certifies the completed records and the prior prediction, not later prose.

All hrt-w3 research jobs and delegated static reviews have now completed. Final named dependency, protected-tree and owned-artifact checks follow. Original tests are reused from the successful post-D run because no protected source changed. The lead can use these AF3 counts as descriptive evidence only. Pending economy prose corrections are enumerated above; the final lead report has already incorporated the corresponding numerical and scope corrections.


## 2026-11-01T00:10:17.580596+00:00 Final economy-summary count and scope corrections; final checks passed

Claim: economy Entry19 at00:06:35 correctly states that AF5 is worse than g1 on six gate conditions. The new independent review finds eight, including the omitted `bot_research.bots.economy.timing:@make?attack_round=5&pre_defend=true&pre_gold=60` in both seats. Root directly checked the four original rows: AF5 -34 at round50, g1 +350 at round50, in each seat. Verdict: REFUTED for six; the complete eight-condition review is being sealed. Root omission receipt `experiments/validation/reviews/economy_final_gate_001/root_final_entry19_omission_001.json`, SHA416086317528dbf1e427f07a530c44229fa6ddc79272417e3548476a3d8aa03b. An initial inline all-sweep join stopped before writing because gate1 alone does not contain every g1 baseline; the receipt preserves that failed assumption and the bounded correction. No record was changed.

Entry19 also needs scope corrections already supported by retained reviews: call846 and448 overlapping pool memberships, not distinct conditions; afrr includes eight exact fresh56 repeats and two source-alias guard conditions, while afrep is a post-exposure reproduction control, so neither deserves a blanket held-out label. The non-W3 subset establishes membership, not that opponents were built against neither policy or that targeting causally favors economy. The120 scenario outcomes establish winner, HP margin and round equality, not equality of actions. For frr7 there are24 exact full-history matches per comparator,20 in their intersection and28 in their union, not28 to each comparator. No game cut off by a harness timeout does not show that runtime cost changed no result. A bounded independent review of this final summary is being sealed. Lead's published report already uses most of these qualifications.

Final checks completed00:07:24.723086Z:95 dependency pins match;903 protected entries including the pre-existing environment are unchanged from the first shift; the1002 missing manifest entries and three initial hash differences remain exactly the baseline. Original post-D tests remain59 run,50 passed,9 skipped, completed23:26:49.589555Z and reused without another test run. The artifact scan checked61,615 text files, found zero concrete absolute paths and the one documented frozen generic path guard. Owned project and lane bytes:2,749,078,024; filesystem free bytes:126,027,497,472 at this scan. Verdict: CONFIRMED for this dated check. Receipt `runs/validation/final-checks-001.json`, SHA0cecd0f0558c560715ab7a036deee29094905b4d4fd965cff2bf4e1805bee33b. Small final review artifacts written afterward will receive a narrow follow-up path check. No new games, policy calls or tests were run.


## 2026-11-01T00:11:59.980683+00:00 Final summary review complete and latest report delta authenticated

Claim: the last economy summary accurately reports the completed finite comparisons and their scope. Method: root read the full independent review, reader and inspection; verified six sealed files and25 archived inputs; counted all804 gate rows and independently rejoined the16 original candidate/control rows behind the adverse comparisons. Result: AF5 is worse than g1 on eight unique conditions, also eight memberships, from four exact opponent specifications. The omitted pre-defended timing opponent accounts for two. Verdict: REFUTED for the six-condition statement; CONFIRMED for eight. The ten named pools comprise448 memberships over416 distinct conditions (208 opponent specifications);406 distinct conditions remain when every condition touching any of the four g1 selection pools is excluded. These denominators answer different questions.

The sealed review is `experiments/validation/reviews/economy_final_gate_001/final_summary_019_001/REVIEW_001.md`, SHA67c1cf7ce3ff4d5db1dfffd29b7d9c19cb051824566c4f6f78c9c898b3002e52; manifest SHAb9c1a315ee3c4beb2aa5d610f1907ecbc64cd6849d3377ae61eecb3b0b0ba894. Root receipt `root_final_summary_019_001.json`, completed00:11:23.173413Z, SHA00c0620407259fb6cc4710947a83433a6ab541525ea47c86a35cffb40c567c2f. It also documents the repeat, provenance, scenario, runtime and historical-base qualifications listed above. For the finite-matrix recommendation, the remaining total weight1/3 is split between P5TNUBM and AS1C; AF5 and guard00 each receive1/3. No general optimum is inferred. The completed AF5 safeguard and AF3/AF4 development results remain unchanged. All supplementary agents are finished and all three lane cores are idle after this static verification.

Claim: the lead's latest captured report additions are supported. Method: root read the complete delta from the previously checked report; authenticated the six-policy sweep receipt, final validation check, lead integrity files and current protected source hashes. Result: the captured report SHA f7879a3ae3bebb8224b8baf5b174625e6a74c58f2de28a4d16ccc28fd698769b gives the correct AF3 and six-policy development counts; lead integrity_3 equals integrity_2 and its40 protected source hashes match. Best and test_best hashes are unchanged. Verdict: CONFIRMED for this bounded delta, captured00:08:04.282249Z. Receipt `experiments/validation/reviews/final_report_reading_001/closure_003/RECEIPT.json`, completed00:10:41.591545Z, SHA2401af1c9e3b376598112521c5389eeb51352b75f619cdf4c605fecaecf2ee4c. The00:06:39Z to00:06:49Z integrity-run times are attributed to the archived lead note, not independently timed by this reader. A prior live-hash attempt stopped as the lead edited the report; closure_002 preserves that failure, and closure_003 certifies separately captured stable bytes. No later report edit is silently certified.
