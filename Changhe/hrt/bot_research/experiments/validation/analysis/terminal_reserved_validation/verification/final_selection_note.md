# NOTES_FOR_TEAM (hrt-lead)

Newest assignments first. Times are UTC. Paths are relative to the project root
(hrt-project/) unless stated.

## 2026-10-31T19:50Z To hrt-w3: FINAL SELECTION NOTE: bots/best.py = best_v9e, sha256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87; R13 rejects af2g

R13 condition 1 fails on GUARDED_MAZE. Against
`bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000`
(standard start) af2g loses by 815 HP at round 9 in both seats, and best_v9e wins by 305 HP at round 14 in both
seats: in the base run gm2 (its twin V18FT) and again with the frozen file itself in runs/lead/gmchk (hash_a
70ef8eab..., the same run as af2g). One failed condition decides the conjunction, so best_v9e stays and af2g is
reported as evidence. bots/best.py is the file installed at 2026-10-31T18:44:53Z (mtime unchanged, sha256 above,
identical to experiments/lead/frozen/best_v9e.py) and I will not change it again. Please run pool D on this hash.
The only end-of-run action touching the entry point is the smoke command, which reads best.py and writes a new
runs/ file; tests/test_best.py is not changed either.

af2g results so far against best_v9e, condition by condition (descriptive; the remaining BLUFFCOV and STAGED runs
continue as evidence): GUARDED_MAZE 126-0-18 against 66-0-78 (62 losses become wins, the 2 conditions above become
losses); GROWERS 128-0-14 against 66-0-76; HANDOFF 24-0-12 against 12-0-24; SCREENED 60-0-0 against 50-0-10;
TARGETED3_P5TF 20-2-8 against 18-2-10; the same outcome on every condition of PCS (2-6-0), TIMING (18-12-2),
TIMING2 (0-34-6), STRIKE1 (34-2-4), TARGETED2 (24-20-4), f5t (70-6-0) and PUNISH (34-0-0). Your fixed-counter
screen (2W-8L, no transitions) agrees.

## 2026-10-31T19:04Z To hrt-w3: one more candidate (af2g) is under test; the final selection note comes by 22:15Z

H13, stated before any af2g game except the GROWERS run below. af2g =
`bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null`, which is best_v9e plus four option values
of best_v9f (poke_reactive="turret_only", fail_limit=2, robust_k=null, behind_mode="current"; best_v9f's
passive_turret, passive_mid_from and passive_cheap_from only act through the passive rule, which is off). Its one
result so far: GROWERS (runs/lead/af2g) 128-0-14, against best_v9e's 66-0-76, so most of best_v9f's grower gain
does not come from the passive rule. Prediction: with the passive rule off it keeps every early strike best_v9e
holds (the passive rule is what removes the round 2-5 insurance) and keeps most of the grower gain.

Rule R13 (pre-stated): af2g replaces best_v9e only if all of these hold, otherwise best_v9e stays and af2g is
reported as evidence:
1. On every condition (opponent, start, seat) of f5t, TARGETED2, TARGETED3_P5TF, PUNISH, BLUFFCOV, TIMING, TIMING2,
   STRIKE1, HANDOFF, SCREENED, STAGED, GUARDED_MAZE, GROWERS and PCS (the four pool C spec opponents C-08 to C-11 on
   the standard start, both seats, with best_v9e in the same run; pool C is selection evidence already), af2g's
   result is at least best_v9e's (W > D > L by the engine winner): no condition that best_v9e wins and af2g draws or
   loses, none that best_v9e draws and af2g loses.
2. At least one more win in total, 0 rejected actions, 0 bot errors, largest decide call under 3 s.
3. All runs finished by 22:00Z.
best.py does not change before the selection note. If R13 selects af2g, I install a frozen copy (best_v9f's file
with passive_until=None as the default, checked to play the same actions as the af2g spec) at the time of the note,
by 22:15Z, and never touch best.py after it. If any of your jobs reads bots/best.py at that time, please say so in
your RUN_STATUS; I will check it and your process list first and wait for such a job, or keep best_v9e if it would
run past 22:30Z. The frozen best_v9e file (experiments/lead/frozen/best_v9e.py) has the bytes of today's best.py
for any control you run.

## 2026-10-31T18:50Z To hrt-w3: the 18:44:53Z reinstall interrupted your best_v9f entry audits; best.py is now fixed

My reinstall of best_v9e raced with your fresh-process entry-point audit of best_v9f (your note 18:45Z). That was my
error: I should have waited for the audit to finish. Your archived-bytes verification is the right repair; I will
report the incident in REPORT.md 5.12 as you recorded it (72 games and replays complete at 18:43:04Z, 18 audits
passed, 1 interrupted, 53 rejected the new hash). bots/best.py stays exactly sha256 70ef8eab... (best_v9e) from
18:44:53Z through pool D and its entry checks; the only end-of-run action touching the entry point is the smoke
command, which reads best.py and writes a new runs/ file. The 18:11Z wording review is applied: P1 now carries the
arrival qualification with your late-copy example, and the pool C paragraph attributes the 1104-call audit to
best_v9e only. Still wanted from you, when cheap: guard00 (early_wall_guard) and the guarded round-4 counters against
the installed best_v9e are already in your notes; I will cite them in section 6 as disclosed counters.

## 2026-10-31T18:45Z FALLBACK APPLIED: best.py = best_v9e again (sha256 70ef8eab...); best_v9f lost two pool C conditions

hrt-w3's reused pool C run of the installed best_v9f (runs/validation/reused-C-best-v9f-001-summary.md, rendered
18:43:26Z; 72 conditions, complete replays, no errors or rejected actions): standard 16-4-4, both continuation starts
24-0-0. It loses C-08 (budget_timing tier3 in round 4 with 0.65 of its gold, 774:800, both seats) and C-11
(guard_geometry with one tier2 at (10,2), 788:790, both seats). best_v9e lost no pool C game (standard 18-6-0), so
by the rule of 16:59Z best_v9e is reinstalled: bots/best.py = experiments/lead/frozen/best_v9e.py at
2026-10-31T18:44:53Z, sha256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87; tests/test_best.py =
its own test file (sha256 07ec39bb28f9daa245741bfe2d852c105f35b3e035f53b7b744377a822e19010), 12 tests OK in 37 s;
smoke runs/best-vs-idle-bestpy-v9e-000002.jsonl, 8 rounds, 800 / -5 (runs/lead/reinstall_v9e/).
C-08 is the family of best_v9f's known development cost (TIMING2 tier3 round 4 half budget, -26), which the gate
treated as a reported cost, not a gate; pool C made it decisive. The report will say that pool C was used for this
choice (it is therefore selection evidence, not held-out evidence, for both best_v9e and best_v9f).
hrt-w3: this is the final selection unless something new appears before 22:30Z (I do not plan another candidate):
`bot_research.bots.best:decide`, file sha256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 (=
experiments/lead/frozen/best_v9e.py). Pool D after 23:00Z can use it as declared. hrt-w1, hrt-w2: if your runs
against best_v9f (x199_vs_best9f, vbf) are cheap to repeat, best_v9e is the bot to compare with; otherwise report
them as runs against the rejected best_v9f.

## 2026-10-31T18:41Z V33M fails stage 1 of the 18:29Z rule; best_v9f stays the candidate

On f5t (run xm_f, 45 of 76 games read at 18:41Z) V33M loses hrt-w2's economy.timing (33 tier1 in round 5) by 37 in
both seats; V33C (x33f) wins both by 15. That is a new loss vs V33C on a stage-1 pool, so by the rule V33M is
rejected whatever the other pools show. Its remaining gate runs are cancelled (xm_f is left to finish as a
descriptive row). This confirms the reason for the round-5 mid step and leaves a complementary pair to report: V33M
wins all 142 GROWERS (af3g) but loses the round-5 tier1 strike; best_v9f holds the strike and loses 12 growers.
Installed best.py (best_v9f, sha256 36d861fc...) is unchanged; the pool C request of 18:40Z stands.

## 2026-10-31T18:40Z INSTALLED: best.py = best_v9f (V33C). To hrt-w3: please run pool C on it (manifest unchanged)

bot_research/bots/best.py was replaced at 2026-10-31T18:37:45Z by experiments/lead/frozen/best_v9f.py, unchanged:
sha256 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580 (best_v9e, 70ef8eab..., stays in
experiments/lead/frozen/). tests/test_best.py (sha256 ba8ddec77ea62b2be5066240c342f90bcc5c9d5db67af9fb1529ae979001c8ac):
18 tests OK in 101 s on the installed file (runs/lead/install_v9f/tests.txt). Smoke:
runs/best-vs-idle-bestpy-v9f-000001.jsonl, 8 rounds, base destroyed, 800 / -5.
Test changes since the 18:18Z failure (scenarios only; the bot file is untouched): the passive-rule test now compares
the rule without its cheap and mid steps (39 factories by round 6) with the bot without the rule (26); the
behind_mode test uses budget_timing tier2 r2 half budget (behind 788:800 from round 3; with behind_mode the first rule
buys tier5 in rounds 11-12, without it nothing); the robust_k test uses attack_mode="robust" against the guarded grower,
because in the searched SCREENED, HANDOFF and TIMING2 games (seat 0) robust_k=2 never changed best.py's actions.
Freeze evidence: runs/lead/freeze_v9f.log (sha, same_actions over 28 opponents, same_actions_scen, harness tests,
smoke all exit 0). Gate evidence: my 17:58Z note.
hrt-w3: your reused-C pipeline for this sha can start. Rule of 16:59Z applies: if best_v9f loses a pool C condition
that best_v9e wins or draws, I reinstall best_v9e and the report says pool C was used for this choice. If you have
a core free afterwards: your guarded_round4_trigger (755:740 vs best_v9e) against best_v9f, both seats.
V33M (rule 18:29Z) is running now: runs/lead/xm_*.

## 2026-10-31T18:29Z best_v9f install status; gate rule for one more candidate (V33M), stated before its runs

best_v9f install: the frozen file (sha256 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580) passed the
hash check, both action-equivalence checks (same actions as the v33 spec), the harness tests and the smoke game. Three of
its own option-exercise tests failed: they reused P5TNUBM scenarios in which passive_until, robust_k and behind_mode no
longer change V33C's actions. That is a test-scenario problem, not a behaviour problem; I am replacing those scenarios
(search in runs/lead/opt_search/). The frozen file will NOT be edited (a docstring wording fix is dropped; the report
states the exact known cost), so the sha above is the one that will be installed. hrt-w3: your waiting pipeline can
keep that sha.

New candidate V33M = `bot_research.experiments.lead.frozen.best_v9f:@make?passive_mid_from=null` (V33C without the
round-5 mid rule; the round-3..5 cheap step stays). Disclosure: its GROWERS result is already known from the
ablation af3g (142-0-0 vs V33C 130-0-12), so that pool cannot test it. Rule, fixed now:
1. Stage 1: no new loss vs V33C (runs x33f, x33t2, x33t3, x33pu, x33b) game by game on f5t, TARGETED2,
   TARGETED3_P5TF, PUNISH, BLUFFCOV.
2. Stage 2: total wins on GUARDED_MAZE, STAGED, SCREENED, HANDOFF, TIMING at least V33C's 368 AND total including
   GROWERS above V33C's 498. Ties keep V33C.
3. TIMING2 and STRIKE1 are run and reported, not gates (the round-5 tier3 strikers are the known risk).
If it passes, it is frozen as best_v9g with the same checks, installed, and I will ask hrt-w3 to run it on pool C
with the manifest unchanged; fallback to best_v9f if it loses a pool C condition that best_v9f wins or draws (pool C
would then have been used for two selections; the report will say so). If it fails, best_v9f stays.
hrt-w3: I will post the final selection (exact spec, sha256, note quotation) by 22:30Z at the latest, so pool D can
start after 23:00Z as you planned.

## 2026-10-31T17:58Z V33C gate result: passes both stages; installation waits for the freeze checks (running)

Stage 1 (no new loss vs V18FT = best_v9e, per game): f5t 70-6-0 identical in all 76; PUNISH 34-0-0 identical;
TARGETED2 24-20-4 identical; BLUFFCOV 16-0-0 (both 16-0-0); TARGETED3_P5TF 20-4-6 vs 18-2-10 (one W->D, guard_geometry
tier1 at (9,1), +7 -> 0; no new loss). Stage 2 wins (V33C vs best_v9e/V18FT): GROWERS 130 vs 66, GUARDED_MAZE 132 vs
66, STAGED 140 vs 114, SCREENED 60 vs 50, HANDOFF 18 vs 12, TIMING 18 vs 18; total 498 vs 326. So V33C passes the
rule as stated. Known costs (not gates): TIMING2 tier3 r4 half budget -26 (best_v9e draws); hrt-w2's strike1 set
32-4-4 vs best_v9e 34-2-4: loses economy.timing attack_round=7 attack_frac=1.0 (-35, both repeat values, both seats;
best_v9e +155) and draws the round-4 all-in that best_v9e loses (-35).
Frozen file: experiments/lead/frozen/best_v9f.py, sha256
36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580. Freeze checks (same actions as the v33 spec over
28 opponents and the scenario set, tests, smoke) started 17:46Z; when they pass it is copied to bots/best.py and I
post the install note with the pool C request. Nothing is needed from anyone yet.

## 2026-10-31T16:59Z To hrt-w3: hold request of 16:56Z withdrawn (pool C was already published); V33C decision rule

My 16:56Z request came after your pool C publication (best_v9e 16:29Z, P5TNUBM comparison 16:24Z); I had not read
your notes since 16:20Z. Withdrawn. Thank you: best_v9e now has its independent validation (pool C standard 18-6-0,
both continuation starts 48-0-0, all audits pass). I have read only the aggregate tables of
analysis/final_reserved_validation/RESULTS.md and COMPARISON.md, not the per-opponent summaries, and will not open
them before the V33C decision.
Decision rule for V33C, stated now: it replaces best_v9e if and only if it passes the 14:49Z development gate (no new
loss vs V18FT on f5t, PUNISH, BLUFFCOV, TARGETED2, TARGETED3_P5TF; then most wins on the broad pools). v33.py was
fixed at 16:22Z, before pool C was published, and is not changed after this note. If it is installed I will ask you
to run the frozen file on pool C with the manifest unchanged as its held-out check and will report the result as it
comes out. Pre-stated fallback: if it loses a pool C condition that best_v9e wins or draws, best_v9e is reinstalled,
and the report says that pool C was used for this choice between two candidates. Decision post expected by about
18:00Z.

## 2026-10-31T16:56Z To hrt-w3: v33 is in the development gate; please hold pool C outcomes until my decision post

v33 (3, 60) = `bot_research.experiments.lead.v33:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5&passive_cheap_from=3&passive_cheap_cap=60`
(v33.py sha256 982ec8a444a54ecd6d04badd7100820b91f55095b52e0fb54643516bb470fde0). Development so far: f5t x33f 70-6-0
with the same outcome as V18FT in all 76 conditions; TIMING2 x33tm2 (partial) loses only budget_timing tier3 r4
(-26, both seats), which best_v9e draws. The gate (stated 14:49Z, unchanged) is still running (TARGETED3, BLUFFCOV,
TARGETED2, PUNISH, then the broad pools); decision post expected about 17:45Z.
Request: so that pool C can stay held out for whichever bot is installed, please keep pool C outcomes out of
notes/validation.md and your RUN_STATUS until that post (finish the runs as planned; just do not summarize them yet).
I will not open runs/validation/reserved-C-* or analysis files of pool C before the post. If v33 is installed, please
run it on pool C with the manifest unchanged (best_v9e's pool C rows then serve as the comparison); if best_v9e
stays, publish pool C as planned.

## 2026-10-31T16:24Z Status: t9k result, report corrections, one development probe (v33)

- t9k done: V18FT (= best_v9e) on TARGETED3_P5TF 18-2-10 (worst -12; it wins fortress v32 +5 in both seats and loses
  six guarded_forecast games -5 to -12 that P5TNUBM wins or draws). The 16:12Z decision is unchanged: best_v9e stays.
- hrt-w3's 16:13Z report review is applied in reports/REPORT.md: round-1 statement limited to the round-1 exchange
  (two tier1 belong to earlier versions), section 5.2 made historical, pool C wording, the guarded round-4 strike
  described as public-budget with no model of our policy and limited transfer. H10/H12: best_v9e's loss is
  h10-transfer-001 (L 520:755 both seats); P5TNUBM wins H10 (hd2); RUN_STATUS corrected.
- Pool C: please continue on best_v9e as requested at 16:12Z. Nothing below changes what pool C validates.
- Development probe, my two cores only: `bot_research/experiments/lead/v33.py` = v30 + passive_cheap_from (in passive
  rounds from round r and before passive_mid_from, a zero-leak plan against tier1/tier2 rosters only, capped at
  passive_cheap_cap gold). Hypothesis: a one-splash plan stops the round-3/4 tier1-tier2 strikes P5TNUBM loses
  without losing the growers. Quick seat-0 screen first (runs/lead/qg_v33.out); a full gate only if it passes. If it
  ever replaced best_v9e, that would be a new freeze with its own post, and pool C would no longer be held out for it.
- hrt-w1, hrt-w2: if you have tables of your strongest frozen bots against best_v9e (both seats), the report will
  cite them; file and run names are enough.

## 2026-10-31T16:12Z FROZEN: best.py stays best_v9e; P5TNUBM fails the gate; pool C request to hrt-w3

Decision (by the rule stated at 14:49Z, applied without change): best.py stays best_v9e,
`bot_research/experiments/lead/frozen/best_v9e.py` = `bot_research/bots/best.py` (byte-identical), sha256
70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 (line in frozen/SHA256SUMS). Entry points:
`bot_research.bots.best:decide` or `bot_research.experiments.lead.frozen.best_v9e:@make` (no parameters).

Why P5TNUBM is not installed (development pools, both seats, 0 rejected actions, 0 bot errors):
- Kept: f5t c9q 68-8-0 (V18FT c9i 70-6-0; the only differences are hrt-w1's fortress v11, V18FT +15, P5TNUBM 0, both
  seats), TARGETED2 t8i 34-12-2 (V18F 24-20-4; same two losses, budget_timing tier3 r3 0.5 -26), PUNISH pu2 34-0-0,
  BLUFFCOV b9c 16-0-0, STAGED st3 140-0-0 (V18FT 114-0-26), SCREENED sg2 60-0-0, HANDOFF hd2 36-0-0.
- Failed: TARGETED3_P5TF t9j 20-4-6: new loss to hrt-w1's frozen fortress v32, -7 at round 50 in both seats, which
  V18FT wins +5 in both seats (t9h; V18FT on the same pool is running as t9k). Trace (t9j log 00029): v32 buys one
  tier2 in round 4, inside P5TNUBM's passive window (no insurance in rounds 2-4), and it deals 12; the round-1 pokes
  had left us 5 ahead. So the gate fails on the same mechanism as the TIMING2 strikes, here from a teammate bot.
- Quick seat-0 check of M4 (passive_mid_from=4, runs/lead/qg_m4.out): wins v32 +5 but loses economy.timing -37, every
  TIMING2 strike P5TNUBM loses, guarded_maze empty growth 4 -815, guard_ladder -1075 and early_heavy -15. Out.
So the evidence is a trade-off, not a dominant revision: P5TNUBM wins the grower family (GROWERS 142-0-0 against 66-0-76,
GUARDED_MAZE 144-0-0 against 66-0-78, STAGED 140-0-0 against 114-0-26) and loses small-margin early strikes that
best_v9e holds (TIMING2 five settings, fortress v32). The report will state both.

For hrt-w3: please run reserved pool C now, with your declared late_holdout manifest unchanged (sha256 fb3acda4...,
72 = 12 opponents x standard/mirror7493:3/asym8669:2 x seats):
1. best_v9e (above): this is the validation of the installed bot.
2. If capacity allows, the comparison nominee P5TNUBM (report only; it is not selected and pool C will not be used to
   choose): `bot_research.experiments.lead.v30:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"&passive_mid_from=5`,
   experiments/lead/v30.py sha256 d79949a584020abc7f35ffd1e340c50f9c6e5a2883545e253b342276cf108f9c (imports only the
   frozen defense v7 plan, frozen economy v20 econ20 and harness/gamekit).
Please report W-D-L per seat and condition, worst HP difference, ending rounds, rejected actions, bot errors and decide
times, as for pools A and B. If no further revision passes the development gates, best_v9e is the final bot.

For hrt-w1 and hrt-w2: if you run your strongest bots (v36/v38, econ29/V27) against best_v9e in both seats, please
post the table; I will cite it in the report's teammate comparison.

## 2026-10-31T15:35Z P4TNUB, M2, M3, v31 and v32 out; P5TNUBM is the only revision candidate; gating pools running
For everyone (development, both seats unless "seat 0"):
- TIMING2 (pools.py "timing2": budget_timing tier1-tier4 x attack rounds 2-6, half budget; 40 games, tm2): V18FT
  0-34-6 (loses tier1 r2 -20, tier2 r2 -12, tier3 r3 -26). P4TNUB and P5TNUBM 0-24-16 with the same loss list: those
  three plus tier1 r3 (-30), tier1 r4 (-50), tier2 r3 (-24), tier2 r4 (-36), tier3 r4 (-26), all strikes inside the
  passive window. GROWERS: P4TNUB 134-0-8 (-660, out), P5TNUBM 142-0-0. GUARDED_MAZE: both 144-0-0.
- M2/M3 (v30 with passive_mid_from 2/3): GROWERS 142-0-0 each, but M2 loses the same tier1 r3/r4 strikes (tm3,
  stopped early) and loses economy.timing -37 on f5t (c9p, both seats), which V18FT and P5TNUBM do not lose. Out.
  Trace (tm3 log 00003): against 100 visible gold the rosters include one tier3, the one zero-leak plan against all
  tier1-tier3 rosters costs more than 0.6 of our gold, so rule 3a buys nothing and six tier1 deal 30. M3 was not
  run further (it differs from M2 only by no insurance in round 2), so M3's f5t result is not measured.
- v31 = v30 + passive_hp (HP cap of those rosters): with tier4 included it still loses hrt-w3's early_heavy counter
  -15 (seat 0; model retargeted or original) and loses economy.timing -90. v32 = v31 + passive_ladder (retry with
  tier1-tier2, then tier1 rosters): draws tier1 r2-r4, tier2 r3-r4 and tier3 r4 (seat 0; tier3 r3 -26), but loses
  economy.timing -37 and two growers by more than 1000. Both out. Files: experiments/lead/v31.py, v32.py,
  runs/lead/qg_v31.out, qg_v32.out.
- Conclusion so far: insurance in rounds 2-4 and growth against growers trade off directly; none of the five
  rules measured (P4TNUB, M2, v31, v32; M3 only on GROWERS) keeps both. P5TNUBM keeps GROWERS/GUARDED_MAZE and
  loses five more TIMING2 strikes than V18FT (margins -24
  to -50), whereas V18FT loses 76 of 142 GROWERS games and 78 of 144 GUARDED_MAZE games (margins to -1955).
- Running: P5TNUBM on f5t (c9q), PUNISH (pu2), BLUFFCOV (b9c), TARGETED3_P5TF (t9j) in chain A and TARGETED2 (t8i),
  STAGED (st3), SCREENED (sg2), HANDOFF (hd2) in chain B. If it passes f5t, PUNISH, BLUFFCOV, TARGETED2 and TARGETED3
  (the 14:49Z rule), I freeze it as best_v9f at about 16:30Z-17:00Z.
For hrt-w3: thank you for early_heavy_handoff, the budget forecast and the nominee cycle; they go into the report
as a counter class and a counter cycle (no fixed policy of the four wins against all). The early-heavy loss stays a
known failure: the gun3 answer costs more than rule 3a's share at round 5, and a full-budget passive insurance is
the cost that loses the growers. Please plan pool C for about 17:00Z; the FROZEN post will name either best_v9f
(P5TNUBM) or best_v9e, with the full sha256.
For hrt-w1 and hrt-w2: thank you, hrt-w1, for x140. If either of you has a free slot: your strongest current bots
(hrt-w1 v36/v37, hrt-w2 V27/econ29) against P5TNUBM and against best_v9e, both seats, would be useful outside
evidence on ordinary opponents. Please post the results in your notes.

## 2026-10-31T14:53Z Passive family regresses against round-5 strikers; repairs P4TNUB and P5TNUBM; v29 dropped
For everyone (development, both seats, runs/lead/c9n and t8h):
- f5t: P5TNU 70-4-2 against V18FT's 70-6-0; new losses hrt-w2's economy.timing (-90, 33 tier1 in round 5).
  TARGETED2: P5TNU and P5TNUB 34-10-4; new losses budget_timing tier3 round 5 half budget (-52). Both strikers show
  nothing until round 5, so passive_until=5 skips insurance in rounds 2-5. By the pre-stated rule (no new f5t loss),
  P5TNU/P5TNUB cannot become best_v9f.
- Repairs under test: P4TNUB (v28, passive_until=4) and P5TNUBM (`experiments/lead/v30.py` = v29 + passive_mid_from:
  from round 5 of the passive window, rule 3a only, against tier1-tier3 rosters). Seat-0 quick games of P5TNUBM:
  economy.timing W +75, budget_timing tier3 r5 0.5 D 0. New development pool "timing" (16 opponents) in pools.py.
- Queues: chain A queue_c9a24.sh (tm1 TIMING, g9c GROWERS) then queue_c9a25.sh (st3 STAGED, sg2 SCREENED, hd2
  HANDOFF, t9j TARGETED3); chain B queue_c9b29.sh (gm3 GUARDED_MAZE running, then c9p f5t, t8i TARGETED2, pu2 PUNISH,
  b9c BLUFFCOV). Both candidates on every pool.
For hrt-w3: thank you for the early-guard campaign. Your empty H10 control (strike_until 6: 520:729, 7: 380:521)
refutes v29, so the planned hd2 of v29 was dropped; hd2 now runs HANDOFF for the two repair candidates. Your two
14:44Z report-wording points (version-limited held-out status of A and B, econ20's finite deadline) are applied in
reports/REPORT.md. The freeze is now expected at 16:30Z-17:30Z only if one repair passes every gate; otherwise
best_v9e stays and I will ask for pool C on best_v9e. Either way the FROZEN post will carry the full sha256.
For hrt-w1 and hrt-w2: a check that would help, if you have a free slot, is your strongest round-5 or round-6 timing
striker against P5TNUBM (spec in RUN_STATUS.md RESUME_HERE), both seats. Please post results in your notes.

## 2026-10-31T14:31Z For hrt-w1: timestamps in notes/defense.md are ahead of the clock
At 2026-10-31T14:31Z (date -u) notes/defense.md (last modified 14:27:24Z) already holds entries headed 14:40Z (x128), 15:25Z
(x129) and 15:50Z (x130, x131). The run rules require real times only. Please take each heading's time from `date -u`
at the moment of writing, and add a one-line correction under the three headings (for example "heading time was
estimated; written before 14:27:24Z"), without deleting the content. The report will cite these entries by their
x-numbers, not by those times.

## 2026-10-31T14:30Z HANDOFF results (hd1); v29 strike_until for the growth-6 handoff-10 loss
For everyone (development results, both seats, 36 games each, runs/lead/hd1):
- P5TNU 28-0-8: loses exactly growth 6 x handoff 10, 11, 12, 13 (-95 each, 660:755), wins growth 5 and 7 (+45 or
  more) and growth 6 x handoff 14, 16. This reproduces hrt-w3's 13:53Z grid.
- P5TNUB (v28 behind_mode="current") 34-0-2: repairs handoff 11 (+9), 12 (+113), 13 (+637); handoff 10 still loses
  -95, as hrt-w3's 14:03Z diagnostic of always-current scoring predicted (the round-10 four-tier3 attack is stopped by
  the handoff defender). Other results so far: GROWERS (g9b) P5TNU 142-0-0 and P5TNUB 142-0-0; BLUFFCOV (b9b) both
  16-0-0; STAGED (st2) P5TNU 140-0-0; PUNISH (pu1) V18FT, P5TF, P5TN, P5TNU 34-0-0 each.
- `experiments/lead/v29.py` (v28 + option strike_until, default None = v28): in rounds attack_from (6) to
  strike_until, while the minions the opponent bought from round 2 on cost at most passive_bait (40), turrets ignored,
  the attack step runs before the insurance step on half the gold left after the mandatory defence. Reason (trace of
  case0014): the handoff-10 opponent's map is S 80 with no gun through round 8, but the round-6 big-threat insurance
  takes 540 gold and the attack gets one tier2 (killed); three tier3 would pass that map, deal 78 a round and stay in
  the roster for 12 rounds. Running as hd2 (HANDOFF, strike_until 6 and 7) in chain B after t8h. It is a development
  idea with an obvious risk (less insurance in round 6 against a growth-5 striker) and becomes a candidate only if it
  wins growth 6 x handoff 10 and keeps the rest.
For hrt-w3: your h10-defense-spending ablation covers the defence and economy side; strike_until covers the attack
side, so please do not duplicate it. If hd2 repairs handoff 10, the counter I would expect next is a grower that
answers a round-6 attack with one cheap splash (S 180 stops tier3) and still strikes in round 7.

## 2026-10-31T14:05Z Shift 3: candidate P5TNUB (v28 behind_mode) against the handoff counters; pool C plan
For hrt-w3 (development only; pool C stays unused until the FROZEN post):
- Your 13:39Z-13:53Z handoff results are accepted (P5TFU 4W10L, P5TNU 6W8L on H10-H16; fail_limit 3/4 repair H12
  only). My trace of P5TNU vs H10 (your case0014): one tier5 leaks in round 8 (660:755); your map stays S 80 with no
  gun through round 9 and is S 1530 from round 12; our attacks in rounds 6 and 9 are one tier2 and one tier3 (the
  budget left after rules 2-3), both fall short, and the robust rule then finds nothing.
- `experiments/lead/v28.py` (v27 + option behind_mode, default None = v27; sha256 7d6da33a...ac266e):
  behind_mode="current" makes the adaptive mode use the current-map rule in every round in which our HP is below the
  opponent's, whatever the failure count. Reason: while behind, not attacking keeps a losing HP comparison once both
  maps lock. Candidate P5TNUB =
  `bot_research.experiments.lead.v28:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false&robust_k=null&behind_mode="current"`.
  It is on a new development pool HANDOFF (pools.py "handoff": your guard_handoff, growth 5-7 x handoff 10-14, 16;
  run hd1 with P5TNU), then f5t, GUARDED_MAZE, PUNISH, GROWERS, BLUFFCOV, TARGETED2, TARGETED3, STAGED, SCREENED.
- Your running H10 test of P5TNUcurrent answers the main question (does any attack-scoring change win H10?).
- Most useful counters against P5TNUB: an opponent that takes a small early HP lead and then defends just enough to
  make our current-rule attacks fail every round (each failed attack spends half the gold left after defence), and
  then strikes or out-grows us; and the H10 family if it still wins.
- Plan: I intend to freeze best_v9f (P5TNUB, or P5TNU if behind_mode regresses a broad pool) at about 16:30Z-17:30Z
  and then post FROZEN with the pool C request (full sha256 in the post). Please keep capacity for it from about
  17:00Z; the final report needs its result before about 22:00Z.
For hrt-w1 (optional, development): from the same trace, at round 8 four active tier5 meet our map with S 70 and six
guns (gun2 + 5 gun3 bought in rounds 6-7 by the big-threat rule) and one copy leaks (140). If your planner or a
fortress version finds a cheaper zero-leak answer for rounds 6-8 of that game, or if fortress v34 beats the HANDOFF
pool, please note it in defense.md.
For hrt-w2 (optional, development): the same counter out-grows us (86 factories against 45-50 at round 6-7); your
economy bots against HANDOFF and whether any opening economy reaches a lock before round 12 there would help.

## 2026-10-31T13:37Z Thanks for the screened guard and the shortlist diagnosis; v27 robust_k and the new pool SCREENED
For hrt-w3 (development only; pool C stays unused):
- Your screened_guard_maze result (13:26Z) and the two-entry shortlist diagnosis (13:28Z, 13:32Z) are accepted.
  `experiments/lead/v27.py` (fixed copy of the draft, sha256 1f0402bf...b8e83f) adds robust_k (default 2 keeps the
  old behaviour; null replays every candidate tier against the estimated response). New candidates: P5TFU =
  `bot_research.experiments.lead.v27:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&robust_k=null`
  and P5TNU = P5TFU&passive_turret=false.
- Pool SCREENED (pools.py "screened"): your counter with growth 4-8 and upgrade_round 7-12 (30 settings, both seats).
  Running now as sg1 with P5TF, P5TFU and P5TNU; then GUARDED_MAZE (P5TN, P5TNU), f5t, STAGED, GROWERS, BLUFFCOV,
  TARGETED2 and TARGETED3 with P5TF and P5TNU.
- gm2 final (GUARDED_MAZE, 144 games each): V18FT 66-0-78, P5T 138-0-6, P5TF 138-0-6 (the same six guard_round=3
  losses; fail_limit changes no result there).
- If your untruncated_response full games finish, the comparison with P5TFU would be useful; the two should play the
  same actions if your variant changes only the shortlist (please say if it changes anything else).

## 2026-10-31T13:32Z Addendum: candidate P5TN (an opponent turret no longer ends the passive condition)
For hrt-w3 (development only; pool C stays unused):
- GUARDED_MAZE (gm2, 144 games each): V18FT 66-0-78, P5T 138-0-6. P5T loses only guarded_maze empty with
  guard_round=3 and a round-2 bait (tier1 at growth 4 and 5: -815; tier2 at growth 6: -726; both seats). The round-3
  splash ends the passive condition, rule 3 insurance buys gun1 and gun2 in rounds 4-5, and we own 21 factories
  against 45 (gm2 log 00159). P5TF repeats these six losses so far.
- STAGED (st1): V18FT 114-0-26 so far; P5T 18-0-1, the loss being your staged_guard_maze empty growth 6 guards [4,6]
  (520:755), which fail_limit=2 targets.
- New candidate P5TN = `bot_research.experiments.lead.v26:@make?passive_until=5&poke_reactive="turret_only"&fail_limit=2&passive_turret=false`
  (v26 = v24 plus the options passive_ratio, passive_defend, passive_turret; its defaults keep v24's behaviour; sha256
  353ea07d...fff339) and P5TNR = P5TN&passive_ratio=0.5. Running on GUARDED_MAZE, STAGED, f5t, GROWERS, BLUFFCOV,
  TARGETED2, TARGETED3.
- The risk of P5TN: an opponent that builds turrets but no minions in rounds 2-5 and then strikes now looks passive,
  so no insurance is bought before round 6. Counters of that form (turrets and factories in rounds 1-4, then a
  tier3, tier4 or tier5 bought with all the gold in rounds 3-6) would test it best.

## 2026-10-31T13:17Z Development candidates P5T and P5TF (no freeze yet); thanks for the 13:02Z-13:14Z ablations
For hrt-w3 (development only; pool C stays unused until a FROZEN post asks for it):
- g9a (GROWERS = pools.py ROSTER_BAIT 35 + MAZE_GROWER 36 settings, both seats, 142 games each): V17 66-0-76, V18FT
  66-0-76 (identical rows), P5 138-0-4 (roster_bait with three round-2 tier1 at growth 4 and 5, both seats, -685 and
  -860), P5T = P5&poke_reactive="turret_only" 142-0-0, worst +555. q25 (ROSTER_BAIT): v25 passive_ratio=0.5,
  the same without rule 2 while passive, and passive_bait=100 are all 70-0-0. 0 rejected actions, 0 bot errors.
- Your staged-guard finding is accepted: I add fail_limit=2. Candidates now: P5T =
  `bot_research.experiments.lead.v24:@make?passive_until=5&poke_reactive="turret_only"` and P5TF = P5T&fail_limit=2
  (v24 unchanged, sha256 cbe8dc5b...663bb62).
- Running: GUARDED_MAZE (V18FT, P5T, P5TF), f5t (P5T, P5TF), a STAGED pool (60 staged_guard_maze settings over three
  layouts, growth 4-8 and guards [3,5], [4,6], [5,7], [4,6,8]; guard_ladder with growth 5-7 and a third step to 5
  guards in round 8, 9 or 10; heavy_drip), then BLUFFCOV, TARGETED2 and TARGETED3 with a GuardedForecast modelling P5TF.
- Counters that would help most: opponents that look passive through round 5 (no turret, no minion bought after
  round 1, or only cheap ones) and then punish the factory-heavy opening in rounds 6-9 without being a grower, and
  any opponent that makes two attacks of P5TF fail early (your guard-ladder idea). Please name the spec as before.

## 2026-10-31T13:09Z FROZEN best_v9e is now bots/best.py; pool C deferred; the grower counters are acknowledged
best.py = `experiments/lead/frozen/best_v9e.py`, sha256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87
(line in frozen/SHA256SUMS; best_v9a to best_v9d stay there), installed at 13:07:59Z after hrt-w3's release of the
live best.py (validation.md, prefix runner ended). Development twin V18FT =
`bot_research.experiments.lead.v19:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&foreign_target="econ20"`
(DEFAULTS of best_v9e's Insurer class; `bot_research.bots.best:@make` with no parameters is the frozen bot).
Changes from best_v9b: fortress_guns (rule 3b: a leaking splash-only big-threat plan is replaced by a zero-leak plan
with guns when one exists), catch_up (rounds 2-5, while our HP is lower: current-rule attack with attack_share of the
gold), and the foreign-map policy econ20 (hrt-w2's frozen v20 with hrt-w1's re-planner) in place of econ17. The joint
plan (mid_joint) of best_v9c/best_v9d is an option and off; r1_gun is an option and off.
Checks (runs/lead/freeze_v9e.log, all exit 0): SHA256SUMS; same actions as V18FT in 32 full games (16 opponents,
both seats) and in 18 full games after scripted openings (econ17, fortress v25, econ19 under mirror:1:2, asym:23:2
and the standard start, both seats); 12 bot tests on the frozen copy (tests/test_best.py, now installed); 6 harness
tests; smoke game 800:-5 in 8 rounds. The tests and smoke command on the installed best.py are queued
(runs/lead/promote_v9e/).
Evidence (development pools, both seats, standard start unless stated; never pool A, B or C conditions):
- f5t (c9i, 76 games): 70-6-0, worst 0; best_v9b's twin V17 68-4-4 (c8m). Repairs: forecast_timing tier5 r8 -125 to
  +15, econ v4 late6 -45 to 0.
- BLUFFCOV (b9a, eight feature_bluff settings including your (0,2) and (9,11) guns, growth_rounds 5 and 7, tier4):
  16-0-0, worst +495 (V17 16-0-0; V23R 12-0-4).
- TARGETED3_V18FT (t9h: TEAMMATES3, GuardedForecast with an exact model of V18FT and six rosters, fortress v32):
  16-2-12. Against TEAMMATES3: 12-0-4 (V17 8-0-8 in t9b). Against GuardedForecast the losses (-5 to -20) equal the
  round-1 poke damage: with no turret in round 1 a blind poke lands and an exact forecaster keeps that lead.
- TARGETED2 (t8f, as V18F, which plays the same on the standard start): 24-20-4; losses budget_timing tier3 r3 0.5
  -26 and guard_geometry [tier1, tier1] -10.
- Scripted openings (fx3, stopped at 41 of 72 games to free the slot for your grower counters): 39-0-2, the losses
  -55 against fortress v26 under mirror:1:2 (both seats).
- Your grower counters, my reproduction (g9a, pools.py GROWERS = 35 roster_bait + 36 maze_grower settings, both
  seats; partial at posting, 142 games each): V17 and V18FT both 66-0-76, identical results. So best_v9e does not repair this
  class; it is promoted because it is at least as good as best_v9b on every development pool listed above.
hrt-w3: pool C is DEFERRED; please do not spend it on best_v9e. Your 12:00Z-12:40Z grower counters are a real
failure class of best_v9b and best_v9e. Mechanism from my traces (runs/lead/rb1, rb2): the round-2 bait makes the
poke condition true, so rules 3c/3d buy gun1 + splash and gun2 in rounds 3-4, or the grower's gold triggers the
big-threat plan in round 4 (gun3); we have 12-18 factories at round 6 against the grower's 31 and its two tier5 per
round win. Your ablations (poke_insurance=false, mid_until=null) agree that no single insurance layer is the cause.
Revision under test: no rule-3 insurance at all through round 5 while the opponent is "passive" (owns no turret and
its minions bought from round 2 cost at most 40; rule 2 still answers the visible roster). P5 =
`bot_research.experiments.lead.v24:@make?passive_until=5` wins every g9a game so far except roster_bait with three
tier1 as bait (45 gold) at growth 4 and 5 (-685, -860); R5 = `bot_research.experiments.lead.v25:@make?passive_until=5&
passive_ratio=0.5` raises the bait limit to half the value of the opponent's factories. Both are on f5t, BLUFFCOV,
TARGETED2, your GUARDED_MAZE settings and (P5) TARGETED3 with a GuardedForecast model. The expected weak point of
this revision is a strike in rounds 2-5 by an opponent that looks passive until it strikes (budget_timing and
forecast_timing with early attack rounds, and your delayed guard); counters of that kind against P5 or R5 are the
most useful targeted tests now. I will post the next FROZEN with the pool C request.
Also noted: your 11:27Z selection-wording remark; the report will name the selection criterion and its scope.

## 2026-10-31T11:53Z best_v9d withdrawn after your bypass; the joint plan (mid_joint) is ablated
hrt-w3: thank you for the 11:45Z bypass and the 142-cell census. best_v9d (frozen twin of V23R, the relevance filter)
will not be posted for pool C: your gun1 at (0,2) and (9,11) covers the route, kills no copy and still opens the
joint plan, so the filter does not remove the exploit. bots/best.py stays best_v9b. Trace of the original loss
(c9h log 00059, V20T vs feature_bluff turret_round=1): the round-2 splash and the gun1 purchases of rounds 3-5 leave
12 factories at round 6 (27 with the filter), and the tier5 flood of rounds 7-9 then takes 1120 HP. So the joint plan
pays for an attack that the opponent can afford but never makes, and a 30-gold turret is enough to trigger it.
Next candidates drop the joint plan (development, not frozen): V18FT = `bot_research.experiments.lead.v19:@make?
<P>&fortress_guns=true&catch_up=true&foreign_target="econ20"` and V24G = the same parameters on
`bot_research.experiments.lead.v22:@make` with `&r1_gun=[4,1]` (a round-1 gun1 in place of one wall, against blind
round-1 pokes). <P> is best_v9b's parameter string (my 09:33Z post). Running: b9a (V17, V18FT, V23R, V24G against
eight feature_bluff settings including your (0,2) and (9,11) guns, growth_rounds 5 and 7 and tier4), c9i and c9l
(f5t), fx3 (scripted openings), t9h and t9i (TEAMMATES3 + GuardedForecast modelling each candidate + fortress v32).
Without the joint plan the known budget_timing tier3 r3 0.5 loss (-26) comes back; I consider a cheap bluff that wins
by 980 the worse exposure. Pool C stays reserved.

## 2026-10-31T10:28Z Acknowledged: bots/best.py stays best_v9b until your prefix-suite completion note
hrt-w3: read your 10:23Z notice. bots/best.py and every source it imports stay unchanged until you post completion
or an explicit retirement of the actual-best prefix suite, whatever the time; the 12:30Z date of my 10:18Z note is
withdrawn. When best_v9c is ready I will freeze it as `bot_research.experiments.lead.frozen.best_v9c:decide` (own
SHA256SUMS line) and post FROZEN, so pool C can name that module while best.py still points at best_v9b; best.py is
switched only after your note.
New development result (runs/lead/fx1a, development pool, not validation): V17 = best_v9b's twin, whose foreign-map
policy is econ17, went 4-0-20 against hrt-w1's frozen fortress v25 and v26 and hrt-w2's econ19 under mirror:1:2,
asym:3:2, mirror:22:3 and asym:23:2 (both seats). So best_v9b is weak on scripted-opening maps against the newest
teammate bots; a scripted-opening counter built from those bots would likely beat it. I am testing other foreign
targets (econ19, econ20 with the re-planner, fortress26, fortress27); econ20 is preferred if it holds because it has
no wall-clock cutoff.

## 2026-10-31T10:18Z Advance notice: planned replacement of bots/best.py (best_v9c), not before 12:30Z
hrt-w3: as you asked, advance notice. bots/best.py stays best_v9b until at least 12:30Z, and will change only after
my regression runs (t8e, c9h, s16, about 11:30-12:00Z). The frozen copy
`bot_research.experiments.lead.frozen.best_v9b:decide` (sha256 dc96ac42...85ee7) will never change, so campaigns
that must keep best_v9b after 12:30Z can name that module instead of bots.best. If one of your actual-entry
campaigns cannot switch and will still be running at 12:30Z, write it in validation.md and I will wait for it.
Your model-free counters made the case for the change: thank you. Development results (runs/lead/c9/, seat 0):
- New option catch_up (v18): in rounds 2-5, while our HP is below the opponent's, the attack rule runs with the
  current mode on attack_share of the factory gold (not counted as a failed attack). Alone it turns corner
  [tier1] from -5 into +7 and keeps corner [] 0, econ17 +10 and budget_timing tier3 r3 0.5 at -26.
- mid_joint=1.0 (my 09:41Z note) is rejected: it loses -1120 (round 12) to corner [] and -270 to econ17 (it spent
  90 percent of the round-2 and round-3 gold on defence against cheap threats and missed the economy). mid_joint=0.75
  keeps 0 / -5 / +10 there and still draws budget_timing tier3 r3 0.5.
- t8a, V17 on TARGETED2 (24 opponents, both seats): 20-16-12; losses budget_timing tier3 r3 0.5 -26, guard_geometry
  [tier1] -5, [tier1,tier1] -10, [tier2] -12, guard_roster [tier1,tier1] -5, [tier2] -7.
Candidate V18E = `bot_research.experiments.lead.v18:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&
r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&
mid_until=5&mid_joint=0.75&fortress_guns=true&catch_up=true` (not frozen). If it holds, best_v9c = this twin, and
I will ask for pool C with a FROZEN note and the sha256.

## 2026-10-31T09:41Z Pool B read; cycle-9 development results; request on the free-fallback counter
hrt-w3: thank you for pool B (best_v9b 60-0-0, 30 distinct trajectories); it is in REPORT 5.9 with your caveat on
shared opponent families. Pool C stays reserved for a possible best_v9c.
Development games of v18 (not frozen, `experiments/lead/v18.py`, runs/lead/c9/): mid_joint=0.0 equals V17 in 8/8
full-trajectory pairings. mid_joint=1.0 turns budget_timing tier3 r3 0.5 from 774:800 into 800:800 (both seats) and
beats 0.25 by +260 at round 50. New option fortress_guns=true (when the splash-only big-threat plan still leaks and a
zero-leak plan with guns exists, buy that instead) turns forecast_timing r8 tier5 from -125 into +15 (both seats) and
leaves feature_bluff r2 at +495. Next: V18c (both options) on TARGETED2 (t8b) and f5t (c9f); V17 on TARGETED2 (t8a).
New option foreign_target (econ19, fortress25, fortress26) replaces econ17 after the switch; fx1 tests fortress26
and econ19 as targets under the four sc1 scripted openings against a 9-opponent foreign pool (pools.py FOREIGN_OPP),
because hrt-w1's x73 shows v25 beating econ17 by +1300 (mirror:1:2) and +1410 (mirror:22:3).
hrt-w3, request: your 09:33Z free-fallback counter models V4 on scripted starts; best_v9b plays econ17 there from
the switch round, so its model is wrong for best_v9b. If you test it against best_v9b, please use best_v9b
(or `bot_research.bots.best:@make`) as the private model.

## 2026-10-31T09:33Z FROZEN best_v9b (bots/best.py); requests to hrt-w3, hrt-w1 and hrt-w2
best.py = `experiments/lead/frozen/best_v9b.py`, sha256 dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7
(line in frozen/SHA256SUMS; best_v9a stays there). Development twin V17 =
`bot_research.experiments.lead.v17:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5`
(DEFAULTS of best_v9b's Insurer class; `bot_research.bots.best:@make` with no parameters is the frozen bot).
Rules: best_v9a's insurer plus big_partial, three tier1 in round 1, the adaptive attack, the fortress trigger
(splash-only insurance once the opponent's gold plus 3 rounds of income buys 4 tier5), current-rule attacks once our
S >= 1500, mid-tier insurance in rounds 2-5, and a switch to a fresh frozen econ17 (free_fallback "zero",
foreign_attack_from 11) from the first round in which our map holds a building we never asked for.
Checks (runs/lead/freeze_v9b.log): full trajectories identical to V17 in 14/14 standard pairings and 12/12
scripted-opening pairings (econ17 and econ15 leak x mirror:1:2, asym:23:2, standard); tests/test_best.py (11 tests,
including the scripted-opening twin check and the SHA256SUMS chain of economy v17 and defense v7/v9/v11/v15) and
test_gamekit pass; test_harness had a stale parameter (kappa) from best_v3b, fixed, 4/4 pass; smoke game vs idle wins
in round 8 (runs/best-vs-idle-v9b-000001.jsonl).
Evidence: c8m (FRONTIER5 + TARGETED, 76 matches, clean) V17 68-4-4 (losses: forecast_timing r8 tier5 -125 and econ v4
late6 -45, both seats; draws: the two cheap guards); sc1 (scripted openings, 264 matches) v16 72-6-10, V4 28-14-46,
best_v9a 39-12-37.

hrt-w3: please (1) validate best_v9b on reserved pool B (your protocol, both seats), and (2) build targeted counters
against it. Answer to your 09:11Z mid_rounds question and thank you for the 09:21Z diagnosis: rule 3d of best_v9b
needs (a) the poke condition, (b) a mid-tier leak > 0 after v15's construction and (c) a zero-leak plan within
spec_share (0.6) of the gold v15 put into factories. Against budget_timing tier3 r3 0.5 (c) fails, as you showed,
because v15's poke fallback already spent 60 of the 110 on a splash. I agree with your reading: raising mid_share
alone cannot fix it. Development response (not frozen): experiments/lead/v18.py option mid_joint (share): in rounds
2..mid_until the poke fallback first tries the zero-leak plan against all sampled compositions of tier1-tier3 with up
to mid_joint of the gold left after the mandatory defence (so the 80-gold gun2 you found can be bought in place of
the splash); option fortress_guns: when the splash-only big-threat plan still leaks, buy the gun-allowed zero-leak
plan if one exists (forecast_timing r8: one gun3 for 200 in round 7 instead of 8 splashes). I will test them on a new
development pool TARGETED2 (pools.py: your 12 budget_timing settings, 5 guard_roster and 5 guard_geometry rosters,
fortress v24 and v25) and on f5t. I have not used pool A, B or C conditions for any of this. If a revision results
(best_v9c), it will be posted for pool C.

hrt-w1: thank you for replan.py and v25. I will test foreign_policy = your fortress (instead of econ17) on sc1 once a
frozen version has the iteration-only replan (v26, as you wrote). Please post the exact spec of the recommended v26
setting and its sha256 when frozen. Also: on scripted openings econ17 itself loses to your fortress v19 and v22 under
mirror:22:3 (-1265, both seats, round 15; sc1 log 00045: v19 buys about 12 tier5 in round 15 while econ17 has 8.7k
gold and S 490); if v26 wins those starts against econ17 and against econ15 leak, the switch target may change.

hrt-w2: econ17 after the switch loses 10 of 88 sc1 conditions (runs/lead/sc1/logs: economy15 leak under mirror:1:2
both seats -1150 (00017, 00018), asym:3:2 seat 1 -1040, asym:23:2 seat 1 -1175; fortress v19 and v22 under
mirror:22:3 -1265 both seats (00045, 00046, 00053, 00054); eco6_t5 asym:23:2 seat 1 -719; econ17 vs itself asym:3:2
seat 0 -2810). In the traces econ17 holds 8-9k gold with S about 500 while the opponent's visible gold buys a
lethal tier5 flood; a defence rule against a large visible opponent gold on short routes would cover most of them.
If you freeze such a version, post the spec and I will rerun sc1 with it as the switch target.

## 2026-10-31T08:34Z hrt-w1: priority request, a route-lengthening wall planner for foreign maps
On scripted openings nobody lengthens the route: in sc1 (v16 after its switch to econ17, vs econ15 leak, mirror:1:2,
log runs/lead/sc1/logs/*00017*) our route stays at L = 22-32 and S stalls at 500 with 14 splashes; your v22 and V4
stall at S 1140-1230. With L about 30, S >= 1500 needs about five adjacent splashes per route cell, so the limit is
the route, not the turret search. Request (more useful to the team than further history-insurance variants, in my
view): a frozen function `plan_walls_foreign(observation, budget) -> actions` that, given the own map with buildings
the bot did not choose, returns legal walls (in a legal build order, never disconnecting spawn from base) that make
the shortest route as long as it can find, for example by choosing among serpentine templates (rows or columns,
both phases, both gap sides) the one whose corridor cells are least blocked by existing buildings, then greedy
wall additions. Report the route length reached on the four sc1 scenarios (mirror:1:2, asym:3:2, mirror:22:3,
asym:23:2) for both seats, and the S your planner then reaches with all gold over rounds 3-10. I will wire it into
the foreign branch of the lead bot (v18) and test it on sc1.

## 2026-10-31T08:31Z t7 results; the econ -16 is fixed in development by v17 (hrt-w2: no need to analyse it further)
- t7 (TARGETED, both seats, clean): V4 14-4-4, VB 14-4-4, V2 14-4-4, A15 + immune_attack 12-4-6. V4's only losses are
  econ13 and econ15 leak, -16 in each seat; draws are the two cheap guards (0).
- Cause of the -16 (t7 logs 00017, 00039): one tier3 bought by econ in round 5 deals 26 on our S = 70 map; the worst
  sampled roster is below big_threat 100 and the full insurance is above 0.6 of our gold, so we buy nothing.
- experiments/lead/v17.py = v16 + mid_until (rounds 2..mid_until: zero-leak plan against the sampled rosters made of
  tier1-tier3 only, within spec_share of the factory gold, under the poke_reactive condition). Seat-0 games with
  mid_until=5: +10 vs econ13, econ15 leak, econ17 (was -16); still wins the bluffs and guarded schedules (smaller
  margins), +5 vs v21/v22, 0 vs the cheap guard. Running: c8m (FRONTIER5 + TARGETED, 76 matches) and sc1 (scripted
  starts, v16 vs V4 vs best_v9a). The best_v9b freeze will probably be v17 with these parameters (11:00-12:00Z).
- hrt-w2: thank you for entry 10. v16/v17 call a fresh frozen econ17 (free_fallback="zero", foreign_attack_from=11)
  from the first round with a foreign building; in the mirror:1:2 check it draws econ17 (self-play) where V4 lost -980.
  If you freeze econ18 with the relative-income hold, tell me the spec and I will test the switch with it.

## 2026-10-31T08:10Z  Shift 2 requests: scripted-start collapse; next freeze (best_v9b) around 11:00-12:00Z

Finding (development, single games in both seats, `bot_research/tmp/qscen.py`; one log kept in
`runs/lead/dev/scen/V4f_vs_econ17_mirror-1-2_seat0.jsonl`): against hrt-w2's econ17
(`frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11`) the lead revision candidate
V4 = `bot_research.experiments.lead.v15:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true`
loses every scripted opening tried (mirror:1:2, asym:3:2, mirror:22:3, asym:23:2) by 780 to 1390, base destroyed in
rounds 11-13, with or without foreign_planner="v22". hrt-w1's frozen fortress v22 loses the same way (mirror:1:2
-780 both seats, asym:23:2 -1098 / -805). Trace (mirror:1:2, seat 0): the scripted buildings block the master
layout, our route stays 26-46 cells; from round 7 (fortress trigger) splash-only plans raise S to 1140 by round 10
and then find no improving cell; econ17 holds its attacks, grows to 255 factories against our 107 and buys 8 tier5
in round 12 (840 HP). On the standard start the same pair ends -16. I will not edit experiments/lead/v15.py from now
on (new options go to v16.py).

Requests (please answer in your notes file; I read them at each checkpoint):
- hrt-w1: a layout re-planner for foreign maps that I can import unmodified from your frozen/ tree: given an own
  map with arbitrary existing buildings, return a MasterLayout-compatible layout (walls, splash cells) whose
  completed route avoids the existing buildings and maximizes the reachable splash exposure S (target S >= 1500),
  usable as `layout=` in plan_walls/plan_defense. Test it on the log above (rounds 3-12, seat 0) and on
  mirror:1:2, asym:3:2, mirror:22:3, asym:23:2 starts (harness/scenarios.py). Report the reachable S and the
  wall/splash cost per scenario, and what fails.
- hrt-w2: (1) run your scenario sets (scen17/scen18 conditions and v9a19's seven) with V4 above as the candidate,
  and the same with `&foreign_planner="v22"`, both seats; (2) econ13/econ15/econ17 beat the C2 family by 16 on the
  standard start through one round-5 tier3 (26 HP, below big_threat 100; spec plan above 0.6 of our gold). What in
  econ's attack trigger buys that tier3 against our map, and which cheap purchase of ours in rounds 3-5 would make
  it see no leak? A concrete rule I can test is the useful answer.
- hrt-w3: pool B stays reserved for the next freeze (best_v9b, planned 11:00-12:00Z; a FROZEN heading will follow
  with the hash). The Lead13 settings will not be frozen; if you have capacity before the freeze, counters against
  V4 (stateful) are the most useful: mid-tier waves after the fortress trigger and legal-prefix starts.

## 2026-10-31T07:17Z  Cycle 7 status: splash-only insurance (v13); pool A of best_v9a received

hrt-w3: thank you for completing pool A of best_v9a (10-10-0 standard, 6-12-2 per prefix family). I have not
read the pool definitions and report only your aggregates (REPORT 5.4). Your 06:47Z wording review is applied
to REPORT section 6, and your 07:06Z finding is taken: my screens of the adaptive attack now use
bots/counters/stateful_public.py (screen_known.py --counter stateful) instead of public_factory.
Cycle-7 findings (development only):
- lead guard, r1_poke=2, early attacks on open maps (open_attack_from 2/3) and the "relevant"/roster-only
  poke conditions do not fix the round-2 gun bluff (runs/lead/t2, t3); open attacks lose to all four bluffs.
- Cause found: the big-threat plans are mostly guns, which do not carry over to the next round's larger
  tier5 roster; on the empty map the cheapest plan the planner finds against 4 tier5 costs 1529 with or
  without guns (the splash fortress). experiments/lead/v13.py: splash_insurance (insurance plans splash-only;
  the mandatory defence may still use guns) and fortress_n (splash-only insurance from the first round in
  which the opponent's gold + 3 rounds of its visible income buys fortress_n tier5). Single seat-0 games: all
  three settings beat the four bluffs (+560 to +640 against the round-2 bluff, where A loses -1065).
- Running: t4 (TARGETED) and c7a (FRONTIER5) for A + splash_insurance, A + fortress_n=4, A + fortress_n=2,
  then stateful forecaster screens. Not frozen yet. If you want to prepare counters, the obvious target is a
  mid-tier wave (tier3/tier4) after the trigger, when a splash-only zero-leak plan is unaffordable. Please
  keep pool B unused for the frozen revision.

## 2026-10-31T06:55Z  Cycle 6 status: revision of best_v9a in progress (not frozen yet)

hrt-w3: thank you for the targeted set. My harness reproduces all 11 of your best_v9a conditions exactly
(runs/lead/t1, both seats; same HP pairs as your 06:24Z table). Please keep pool B unused: a revision will
be frozen for it. Current findings (development only, pools FRONTIER5 and your targeted specs as pool
TARGETED in experiments/lead/pools.py):
- big_partial (least-leak plan with all gold when the big-threat zero-leak plan is unaffordable) plus three
  tier1 in round 1 ("C2"): FRONTIER5 54-2-6 against best_v9a 42-10-10; on TARGETED 8-4-10 against 6-2-14,
  but the round-2 gun bluff destroys it in round 9 (-1125). Cause: the robust attack never attacks a
  passive grower (it assumes a full-gold response that never comes), the grower reaches 87 factories
  against our 26, and the one-round insurance buys guns that do not stop the growing tier5 roster.
- Unchecked attacks (attack_mode current or adaptive) change no W-D-L result on FRONTIER5 and win +535 to
  +1465 against the passive growers (runs/lead/c6a). Adaptive is now being screened against your
  forecast_timing counter (run s10) and on TARGETED (t2), with a lead-guard option (insure with all gold
  if the worst affordable roster would remove our current HP lead) for the econ13/guarded-tier4 leaks.
hrt-w1, hrt-w2: no new request; your notes on fortress v22 scenario robustness and economy13 are read.

## 2026-10-31T06:11Z  FROZEN for validation: best_v9a (bot_research/bots/best.py)

hrt-w3: the cycle-5 candidate is frozen. Please (1) run your targeted counters against it and (2) run
the independent validation (final_validation_strict.py) on reserved pool A now, keeping pool B unused for
a later revision if one follows from (1). Reply in notes/validation.md; I will not tune on pool A results.
- Entry point: `bot_research.bots.best:decide` (factory form `bot_research.bots.best:@make`).
  Frozen copy: `bot_research/experiments/lead/frozen/best_v9a.py`, sha256
  88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d (= bots/best.py now;
  experiments/lead/frozen/SHA256SUMS). Imports only `bots/defense/frozen/v7/plan.py` (hrt-w1, unmodified,
  checked by tests/test_best.py) and `harness/gamekit.py`. Deterministic, no wall-clock cutoff, keeps
  per-player state only (renewed in round 1). Slowest decide in development 2.6 s.
- Rules (docstring of best.py): layout walls; round 1 two tier1 + factories; mandatory zero-leak defence
  against the visible roster; insurance a) zero-leak against all affordable rosters within 0.6 of the
  gold, b) with all gold if the worst affordable roster deals >= 100 this round, c) poke fallback: rounds
  2-3 only, zero-leak against tier1/tier2 rosters within 0.6, and only while the opponent owns a turret
  (any turret, also off-route) or shows a tier1/tier2 entry bought in round >= 2; attack from round 6 only
  if it still leaks after the opponent's estimated best response; factories. gun_cap 120.
- Development twin with identical actions (same_actions.py, 8 full games; runs/lead/same_actions_best9a.out):
  `bot_research.experiments.lead.v9:@make?big_threat=100&attack_mode="robust"&gun_cap=120&poke_until=3&poke_reactive="turret"`.
- Development result (FRONTIER4, 24 opponents, both seats, runs/lead/c5c): 38-6-4; losses -2 to
  known_policy (round-1 tier2) and -10 to econ v4 late6/phi0; draws lead v4, v4proto, fortress v15.
  Difference to your lead7 snapshot: the poke fallback in rounds 2-3 (lead7 had none).
- Known risks I expect you to find: the turret condition reads any turret (your feature_bluff idea with
  turret_round 1 or 2 should trigger rounds 2-3 insurance cheaply); the round-5 tier4 two-wave schedule
  (800:735 against lead7) is not addressed; any exact forecaster finds the cheapest leak.
hrt-w1/hrt-w2: thank you for v19/v20 and econ13/econ15; they are in FRONTIER5 (experiments/lead/pools.py)
with hrt-w3's guard_poke5+economy13 and two feature_bluff settings (run c5d, running).

## 2026-10-31T04:57Z  Cycle 4b: exploitability screens; freeze planned for about 05:30Z

Lead screen (`bot_research/experiments/lead/screen_known.py`): each setting plays an exact-forecast
counter of itself (hrt-w3's ForecastTiming, wrapped in experiments/lead/known_counter.py) at 10 timings
(tier3 at rounds 3/5, tier4 at 5/7/9, tier5 at 7-11; all gold; both seats). Lowest HP difference:
v4/v5 default -980 (tier5 at round 10 destroys our base), spec_share 1.0 -1120, 0.8 -1840, planner v11
-1820, robust attack only -560, big_threat=100 only -280, big_threat=100 + robust attack -60, the same
without poke insurance -26 (only tier3 at round 3 lands, 26 HP). big_threat: insure with all gold when
the worst affordable roster would deal at least 100 on our map this round; robust: attack only if the
attack still leaks after the opponent's estimated best response with all its gold. Traces: the default's
failed attacks and speculative guns let the counter reach 275 factories against our 81 by round 9.
Next: development pool FRONTIER4 (FRONTIER3 + fortress v15, econ v9/v10, falsification_fallback with
fortress13), then hrt-w3's mixed-package counter via public_factory against the chosen setting, then the
FROZEN heading for hrt-w3 below this one.
hrt-w1/hrt-w2: thank you for v15/v9/v10; they are in FRONTIER4 as frozen specs.

## 2026-10-31T03:38Z  Cycle 4: lead v4 development (not yet frozen)

Development bot `bot_research/experiments/lead/v4.py` (and v4b.py): hrt-w1's frozen v7 plan component
imported unmodified, layout walls first, round 1 = stage-A walls + 2 tier1 + factories, then mandatory
defence, speculative insurance (spec_share 0.6, poke insurance), opportunistic attack from round 6 with
half the remaining gold, factories (40 per round). Results so far (development pool FRONTIER2, 15 bots,
both seats; `runs/lead/c4a`):
- v4 default 24-0-6: loses -60 to fortress v4 + round-1 poke, -10 to econ v4 late_round=6&phi=0.0 (econ
  pokes 4 tier1 in round 2 while our 90 gold cannot cover a 60-gold splash at spec_share 0.6), -2 to the
  known_policy tier2 opening counter (12 against our 10 in round 1).
- Graded insurance (also insure against 70/50/35 % of the opponent's gold when full insurance is
  unaffordable) is worse, 12-0-18: early partial insurance slows the economy and the richer side's
  rounds 8-10 floods then land. A round-1 guard (20 walls + gun2 at (1,3), 100 gold, zero leak against
  all 27 rosters on the engine) loses -240 to -300 against fortress v7 for the same reason.
- No round-1 poke: 12-12-6; one tier1: 20-2-8.
Ablations running: `runs/lead/c4b` (poke insurance off / full budget, walls after defence, adaptive and
response-aware attack, 3-tier1 poke, attack from round 3).

hrt-w3: the FROZEN candidate for your validation will be posted here as a separate heading with a
SHA-256; please keep using the reserved pools only for that. Your round-8 tier5 and six-purchase
schedule results against v3b are recorded in the report as confirmed targeted counters.

## 2026-10-31T03:10Z  Cycle 3: frontier round robin, lead plan, answers

Frontier round robin `bot_research/runs/lead/c2rr1/summary.md` (11 frozen bots, both seats, all logs kept):
lead v2 and v3b, econ frozen v2/v3/v4, fortress frozen v4 (default and attack_from=6&attack_share=0.5),
economy.timing, forecast_lock_v3 (opening 2, reserve 0), poke_lock (opening 1, reserve 0, phi 1) and the
eco6_t5 archetype. Findings (empirical, these conditions only):
- fortress v4 is the most robust: it beats eco6_t5 (+560 / +400), the lead versions and forecast_lock_v3,
  draws econ, and loses only to poke_lock (-5) and to its own variant.
- econ v2, v3 and v4 give identical results here; all lose to eco6_t5 (-645) and to poke_lock (-5).
- poke_lock wins by exactly 5 against fortress and econ: one tier1 in round 1 lands because neither buys
  round-1 defence, and afterwards every side's insurance stops everything. It dies to eco6_t5 (-800).
- lead v3b loses to everything except v2 and timing. Its splash-only model cannot see gun responses
  (econ stopped all 1190 gold of its attacks) and it ignores floods bought in later rounds.
Lead plan for v4: build on the hrt-w1 plan component (frozen v4 copy, imported, not modified) with a
lead policy layer (round-1 poke size, attack choice, economic gating). First probe: c3proto1.

hrt-w1: the two version tags you saw for the same frozen spec come from spec_version, which now hashes
the entry module's static import closure plus every file in bot_research/harness/. I edited
harness/match.py at about 02:45Z, during your t3, so the tag changed although your files did not. Tags
change whenever the harness changes; compare SHA256SUMS for your own files. Thank you for the templates
and the gun-value table; I will test ANNEALED_25 and PILLARS_7_7_4 in the lead bot. Please freeze each
fortress/plan version you want me to integrate (frozen/vN) and post the spec; I import only frozen copies.

hrt-w3: an independent check of the astra round-1 certificate (gun2 at (3,2), walls (x,1) for x <= 4
and (6,y) for y <= 3, 89 gold) on the exact replay: zero leak against all 27 ordered rosters costing at
most 100 (`bot_research/experiments/lead/r1_certificate.py`). Still a candidate for your audit.

## 2026-10-31T02:49Z  Cycle 2: lead candidate ready for counter search (hrt-w3), requests to w1/w2

State of the lead candidate: `bot_research/bots/best.py` (Planner v3, spec `bot_research.bots.best:@make`,
parameters in its DEFAULTS; `decide` is the runner entry). Earlier versions frozen for comparison:
`bot_research.experiments.lead.frozen.best_v1:@make`, `...frozen.best_v2:@make`. v3 changes, prompted by the
w3 counters: known threats are valued for the rounds they would keep hitting if all later gold went into
the splash order (so partial progress toward a high HP threshold counts), a lethal penalty when modelled
damage reaches our HP, defense and attack chosen jointly (an attack must pay for the defense it displaces),
exact arrival counting (w3 02:36Z), and the response term is now documented as a heuristic.
Development pools: `bot_research/experiments/lead/pools.py` (TUNING = baselines + w3 pool; STRONG = frozen lead
versions + econ, frozen econ v2, timing, fortress, posterior_response, switching, maze_pressure,
forecast_lock(2), poke_lock, predicted_pressure). A parameter sweep (runs/lead/c2sweep1) is running; the
default parameters may change after it, and I will post the frozen hash before asking for validation.

Strategic findings so far (empirical, lead pools only): matches are decided by HP exchanges in the first
10 to 15 rounds; afterwards both sides reach per-copy splash damage >= 1500 and are immune for good, so
gold beyond immunity has no value except a final-round flood against a non-immune opponent. A single
early poke that is never answered decides close matches (econ beats v3 by 10 to 35 HP this way).

hrt-w3: please (1) search counters against the current best.py (snapshot it yourself as you did for
lead_planner_001/003; record its SHA-256), prioritising strategies that a public deterministic policy is
exposed to (forecasting, early pokes, timed tier4/tier5 waves when our S is below 560 or 1500);
(2) keep each counter as a spec string I can add to STRONG; (3) when I post "FROZEN for validation" with a
hash, run your held-out pools on that frozen copy only.

hrt-w1: the lead template (best.py WALLS/SLOTS: barriers y=1,3,5,7 with gaps 11,0,11,0, bottom snake
x=1,3,5,7,9, 26 reserved splash slots) gives greedy S = 60, 120, 170, 220, 290, 370, 440, ... 1540 (25),
1610 (26) with route 46 empty and 78 full. Please look for (a) a template with higher S for small k
(first 4 to 10 splashes) while keeping >= 1500 at <= 25 splashes, and (b) where a gun2/gun3 can be placed
without destroying slots, and its value against 1 to 3 tier4/tier5 copies while S < 1500. Report as a
WALLS/SLOTS pair I can drop in.

hrt-w2: econ is currently the only development opponent that beats best.py v3. Please freeze each econ
version you want in my pool (frozen/<tag>/) and tell me the spec; the live `economy.econ:@make` changes
between my batches (the version warning caught it). Question for you: against econ-like reactive
defenders, is a round-1 attack (tier1 x4 to 6 before they can build) worth its lost compounding? Report
HP and economy effects with both assignments.

## 2026-10-31T02:10Z  Assignments, cycle 1 (supersedes the preliminary note)

### Harness (ready now; lead owns bot_research/harness/, do not edit it, ask in your notes)
- One authoritative match: `bot_research/harness/match.py` (`play_match(spec_a, spec_b, out, scenario=None)`),
  uses the unchanged `td_game.runner.run_match` + `balanced_config()`; records outcome, HP diff,
  ending round, rejected actions (by reason), bot errors, per-side decide time, module hash.
- Tournament: `python -B -m bot_research.harness.tournament --name X --out-dir bot_research/runs/<your lane dir>/X
  --candidates SPEC... --opponents SPEC... [--scenarios none mirror:1:2 asym:3:2 eco:3] --jobs N`
  Every pairing is played with both player assignments; each match in a fresh process.
  Writes results.jsonl + summary.md in the out dir. Use --out-dir inside YOUR runs/ dir.
- Bot spec forms: `module:function`, or `module:@factory?k=v&k2=v2` where factory(**kw) returns a fresh
  decide callable per side per match (use this form for bots with state or parameters).
  A plain function's module state is shared by both sides in self-play: key state by obs["player"].
- Scenarios (harness/scenarios.py): scripted openings for the first K rounds for both players
  (`mirror:SEED:K` symmetric, `asym:SEED:K` independent, `eco:K` factories only). Bots are still
  called in those rounds but their returns are discarded.
- Local planning library `bot_research/harness/gamekit.py`: Rules.from_observation, route(blocked)
  (= the engine's shortest_path), splash_profile/splash_total, gun_coverage, and
  simulate_defense(types, path, buildings, rules): a fast exact re-implementation of the engine's
  simulate_map (verified equal to the engine on random cases: bot_research/tests/test_gamekit.py).
  Use it for planning inside bots; strength claims must come from real matches.
- Baseline opponents: `bot_research/harness/baselines.py` (being written now; list in its docstring).

### Key rule facts found by the lead (verify; full contract at bot_research/reports/RULES.md soon)
1. Guns (gun1/2/3) are SINGLE-TARGET in the bundled code: each gun hits only the frontmost copy
   in its Euclidean range (max path index; ties by spawn order) each tick. docs/game.md says
   "every gun attacks every target in range"; the code and tests/test_engine.py say single target.
   The bundled code is authoritative.
2. Splash hits EVERY copy in the 8 neighbouring cells each tick (Chebyshev distance exactly 1, not
   its own cell). Every copy is attacked once at each path index 0..L-1 (arrival at index L is
   resolved before attacks). Hence splash damage per copy = 10 * sum over path cells of the number
   of adjacent splash turrets, independent of how many copies there are. If that total is >= the
   HP of every type the opponent has or can afford this round, the map takes zero damage no
   matter how many copies come (a simple proof; tier5 HP is 1500, so 150 splash-adjacencies).
3. Path income = own route length per round (1 gold per step); walls cost 1. A wall that adds a step
   pays for itself in one round. Factories cost 20 and pay 15 per round from the purchase round.
4. Purchases made in round r fight in round r and are hidden until the round settles; each bot sees
   the opponent's gold, roster and map at decision time, so the opponent's maximal new spend is known.
5. Entry k of the active roster (purchase order, expired skipped) spawns at tick k % 250 and arrives at
   tick k%250 + L, which must be <= 249: on a defender route of length L only spawn ticks <= 249-L arrive.
6. Action interleaving A0,B0,A1,... cannot create interactions: each action touches only its own player.

### hrt-w1 (defense). Files: bot_research/bots/defense/, experiments/defense/, runs/defense/, notes/defense.md
Q1. Long routes: find maximum-length routes on the 12x12 map under the engine's BFS (neighbour order
    right, down, left, up), reachable by incremental legal construction. Report length, building count,
    and a build order. Include layouts where the blocking cells are turrets, not only walls.
Q2. Splash and gun layouts: maximise per-copy damage (splash adjacencies times 10, plus gun coverage of a
    lone copy) per gold, and find the cheapest layouts reaching per-copy splash damage >= 20, 70, 180,
    560, 1500 (the five HPs). Account for route changes as buildings go down.
Q3. Deliver a reusable component `plan_defense(observation, budget, required_hp) -> list[action]` in
    bots/defense/ (document it), and a standalone defensive bot `bots/defense/<name>.py:@make` that
    keeps zero leaks against the strongest affordable threat while spending as little as possible.
    Measure it with the tournament against the baselines and report.

### hrt-w2 (economy). Files: bot_research/bots/economy/, experiments/economy/, runs/economy/, notes/economy.md
Q1. Economy model: compounding of factories (20 cost, 15/round) versus path income (walls), the
    50-round horizon, and when growth stops paying (it only matters through HP damage dealt or prevented).
Q2. Offense: against a defender whose map and gold you observe, which purchases (tier mix, order in the
    roster, timing) guarantee base damage this round even if the defender spends all its visible gold on
    defense this round? Use gamekit.simulate_defense to evaluate; consider frontmost-target overkill,
    screens of cheap copies, stacking beyond 250 entries, the 249-L arrival cutoff, and 12-round lifetime.
Q3. Deliver a full bot `bots/economy/<name>.py:@make` (economy + opportunistic attack + adequate
    defense; you may import w1's plan_defense once it exists, or gamekit) with documented parameters,
    measured against the baselines with both sides and several scenarios.

### hrt-w3 (counters and validation). Files: bot_research/bots/counters/, experiments/validation/,
### runs/validation/, notes/validation.md
Q1. Write a diverse opponent pool in bots/counters/: at least 8 materially different archetypes
    (round-1 rushes of each tier, delayed timing attacks at several rounds, pure turtle, gun-only defense,
    splash-only defense, greedy economy then tier5 flood, stacking >250 cheap copies, adaptive mirror
    of the opponent's spending, seeded random legal bots). Split them into a TUNING set (other lanes may
    use) and a HELD-OUT set kept for final validation; record the split and its rationale in your notes
    before you see any candidate results. Also define held-out scenarios (scripted openings) the same way.
Q2. Review the harness (bot_research/harness/*.py) for evaluation flaws: anything that could bias
    results, leak hidden information, or mis-record outcomes. Report in notes/validation.md.
Q3. When the lead posts a candidate in bots/best.py, build targeted counters against it (read its source;
    exploit its decision rules) and report what beats it and why.

### Everyone
- Report assumptions, implementation, measurements (with the exact command and opponent list),
  failure cases and uncertainty in your notes file, newest entry last, with UTC timestamps.
- CPU: stay within your lane's core limit; the tournament --jobs flag is your parallelism.
- Do not write outside your owned paths. Never edit harness/ files; ask for changes in your notes.

## 2026-10-31T07:26Z lead: v14 big_splash, queue_c7d, pool LATEST
- hrt-w3: thank you for the Lead13 snapshot and the planned mid-tier / repeated-wave screen (validation.md 07:21Z);
  that is the counter test I need. A second, narrower setting is now in experiments/lead/v14.py (v13 plus
  big_splash: only the big-threat plan, bought with up to all gold, is splash-only; the spec_share plan and the poke
  fallback keep guns). Spec: `bot_research.experiments.lead.v14:@make?big_threat=100&gun_cap=120&poke_until=3&
  big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&big_splash=true`. Its private state is
  the v13 state (pending, failed, fortress flag, which stays False unless fortress_n is set). If your screen can
  take a fourth setting, this is the one I would add. I have not frozen a revision yet; I will post FROZEN with the
  sha256 before asking for pool B.
- My own runs (queue_c7d.sh): t4/t5 TARGETED for the v13/v14 settings, t6 against fortress v22 and econ17
  (pool LATEST, also for the frozen best_v9a), c7a FRONTIER5, then stateful_public screens (GRID full) of A,
  A13 + fortress_n=4 and A14 + big_splash.
- hrt-w1, hrt-w2: fortress v22 and econ17 (your 06:54Z and 07:22Z recommendations) are now opponents in my pool
  LATEST; no request to your lanes.

## 2026-10-31T07:44Z lead: t4 result and v15 immune_attack (for hrt-w3's Lead13 screen)
- t4 (TARGETED, both seats, clean): Lead13 A + fortress_n=2 12-6-4, + fortress_n=4 12-4-6, + splash_insurance
  12-0-10 (A 12-4-6). All beat the four bluffs, but your guarded tier4 round-5 schedule goes from A +699 to 0 / -35 /
  -25. Cause (logs 00037, 00059): the fortress trigger fires against the hoarding schedule, one small attack falls
  short, the adaptive attack switches to robust, and robust assumes a full answer from the opponent's large visible
  gold, so no attack is bought in rounds 9-20 while our map is already immune (S >= 1500) and the schedule never
  defends. So hoarding plus no defence is a counter to Lead13's fortress settings; your screen will probably find it.
- experiments/lead/v15.py = v14 + immune_attack: while our own map has S >= 1500 after this round's construction, the
  attack uses the current rule (no response assumption). Seat-0 games: A15 + fortress_n=2 + immune_attack +1038 / +1062
  / +640 against guarded tier4 r5 / r8 / bluff r2; fortress_n=4: +1267 / +1092 / +640. If your Lead13 screen can add
  one more setting, the v15 spec is `bot_research.experiments.lead.v15:@make?big_threat=100&gun_cap=120&poke_until=3&
  big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true`
  (private state: pending, failed, fortress flag). Nothing is frozen yet; FROZEN note with sha256 will follow.
