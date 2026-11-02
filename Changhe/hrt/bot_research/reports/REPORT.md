# Bot research report (tower-defense game, bundled balanced rules)

Status: final. Within-scope result only: a validated final bot is delivered, but no bot was shown to be the strongest
in general, and the tested data show no universally dominant policy.

## Summary

Selected policy. The delivered bot in the accompanying artifacts (function `decide`) is best_v9e, a deterministic insurance bot (sha256
70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87, unchanged since 2026-10-31T18:44:53Z). It is the
selected bot within the tested scope: rules stated before the deciding games selected it, and
an independent verifier then validated it on reserved opponents and starts. It does not win the most conditions: the
economy worker's af5 (V29 with attack_from=5), found after best_v9e was pinned, is 764-2-38 on the 804 distinct gate
conditions against best_v9e's 504-64-236 and beats it by 410 HP in both seats on the standard start, but is worse on
30 of those conditions and has no reserved-pool validation, so the pre-stated rules did not install it. Finalists
beat each other in cycles (g1 > guard00 > best_v9e > g1): no single policy dominates on the tested set.

Decision rules (section "Final bot"): walls towards a long route; round 1 three tier1 and factories; from round 2 the
cheapest zero-leak defence found by the planner against the visible roster, plus insurance against sampled rosters the opponent can afford
(splash-only once projected gold buys four tier5, with gun fallback); attacks from round 6, and in rounds 2 to 5 while behind, with the tier
of most simulated damage per gold; factories with the rest, subject to purchase caps and a late-game cutoff; a frozen economy policy only on a foreign map.

Proved from the bundled source (P1 and the certificates also checked independently on the unchanged engine):
- P1 splash immunity: if S = 10 x (sum over route cells before the base of adjacent splashes) >= 1500, no copy of any finite roster
  damages the base. P2 lock: if both maps have S >= 1500 and stay unchanged, the HP difference is final.
- Round-1 certificates: gun2 (3,2) with walls (x,1), x = 0..4, and (6,y), y = 0..3 (89 gold, route 22), and 20
  stage-A walls with gun2 (1,3) (100 gold, route 42) each stop all 27 ordered rosters costing at most 100 gold.
- On the standard start best_v9e never hands the game to its foreign-map policy.

Confirmed by the independent verifier (both seats, W-D-L by engine winner; deterministic, one game per condition):
reserved pool C, 72 games: 18-6-0 standard start (worst margin 0), 24-0-0 on each of two prescribed-history starts
(then used to choose best_v9e over best_v9f); terminal pool D, 96 games on the final hash, used for no decision:
26-6-0 standard, 32-0-0 mirror, 28-0-4 asymmetric start; predecessors best_v9b 60-0-0 (pool B), best_v9a 22-34-4
(pool A); the gate counts and the af5 comparison above. Ablations (main-agent runs, f5t pool, best_v9e 70-6-0):
without the all-gold insurance 26 wins become losses, without the round-1 poke 30 wins become draws.

Remaining gap (no tested revision closes it without a worse outcome on a condition best_v9e wins or draws):
1. Passive growers with a cheap bait: best_v9e loses 76 of 142 GROWERS development conditions; every policy that wins
   most of them (best_v9f, P5TNUBM, af2g, g1, af5) is worse than best_v9e on some early strike or guard.
2. Defended strikers: TIMING2 0-34-6; attacking with all gold wins all 40 but is worse on 14 gate memberships.
3. Pool D: one guard continuation ends best_v9e at -3120 HP against 785 (four games); no fix was tested.
4. Decision time grows with the opponent's hoarded gold (up to 8.13 s per call); the runner has no time limit.

Integrity: starting state recorded, not repaired (1002 manifest entries absent; hash mismatches in the combat implementation,
the engine tests, the rule tests; existing tests 59 run, 9 skipped); no change at the end. The 18 research
tests passed at the end-of-run check (23:42Z). Smoke command at 2026-11-01T00:16:50Z: player 0 wins in round 8, HP 800
to -5, 0.32 s.

## Run record and evidence status

- Run start T0 = 2026-10-31T01:57:42Z (logged). The 24-hour budget ends at 2026-11-01T01:57:42Z. The plan stopped
  the team at 23 hours of the 24-hour run (2026-11-01T00:57:42Z) so that this write-up finishes inside the budget.
  The team was actually stopped at 2026-11-01T00:13:38Z, 22 h 16 min after T0, after the main agent had declared its
  work complete at 00:12:34Z. This write-up ended at T_end = 2026-11-01T00:28:47Z, so the elapsed time is 22 h 31
  min 5 s (22.52 hours of the 24-hour budget).
- Research organization: one integration agent and three concurrent research workers from
  2026-10-31T01:58:35Z to the stop, covering defensive maps and spending; economy, purchases and timing;
  and opponent adaptation, counters and independent validation. An additional referee checked derivations
  and code, with its suggestions verified before use. Sessions were restarted at most every six hours
  from retained records. Each agent ran at most two computations at a time on two low-priority cores of a shared machine.
- Evidence labels. Confirmed by the independent verifier (the validation worker, from retained records): the
  reserved-pool results A to D, P1 including the late-copy cleanup case, the round-1 certificate, the gate counts and
  their deduplication, the af5 gate and matrix results, the max-min mixtures of section 5.16, the runtime
  decomposition of the 8.13 s call, the integrity checks, and its readings of the report text up to
  2026-11-01T00:08Z. All other game results in sections 3 to 7 are the main agent's or a worker's recorded games on
  the unchanged engine: empirical, with the retained evidence available in the accompanying artifacts, but not rerun by a second party
  unless a section says so. Some omitted inputs prevent complete reproduction from this bundle (section 8). Conjectures are labelled as such.
- Code, data, exact reproduction commands and retained verification records are in the accompanying artifacts.
  Some intermediate inputs and most replays were omitted before publication (section 8).

Where the prompt's required report items are answered: decision rules (Final bot); game contract (section 1 and the
accompanying artifacts); tournament results (sections 3 to 5.16); ablations (5.14); validation evidence
(5.4, 5.9, 5.11, 5.17); counters (4.2, 5.3, 5.6, 6); known failures (6); runtime costs (7); reproduction commands
(8); file-integrity checks (9); proved claims, empirical findings and conjectures ("Detailed findings").

## Detailed findings

Scope statement: the delivered bot in the accompanying artifacts is the entry point selected within the tested
scope by rules stated before the deciding games. It scored at
least as well as the previously installed best_v9b on every development pool on which both were run, and better on
several (sections 5.9-5.11); its three revisions that reached a gate each lose conditions that it wins or draws
(P5TNUBM, section 5.11; best_v9f, which passed the development gate and was then rejected by the pool C rule posted
in advance, section 5.12; af2g, rejected by R13, section 5.14). It is not the best tested policy on every
condition: best_v9f, af2g, P5TNUBM, the economy worker's g1 and several targeted counters win conditions it loses (sections
5.12-5.15, 6). By the number of conditions won on the main agent's 14 gate pools, the economy worker's g1 is ahead of it (764 against
524 wins on the 846 gate pool memberships, 726 against 504 on the 804 distinct conditions they cover, section
5.15), but g1 is worse on 72 memberships (68 distinct conditions), and the selection rules required that no
condition be worse. The economy worker's af5 (V29 + attack_from=5, selected for fresh validation at 22:43Z and recommended by the economy worker for the
standard start after its completed gate, the accompanying artifacts, entry 18.32, 23:34:38Z) is further ahead (804 against 524 wins on the
memberships, 764 against 504 on the distinct conditions; worse on 30 distinct conditions) and beats best_v9e by 410
in both seats on the standard start (section 5.16); it was found after best_v9e's hash had been pinned for pool D,
has a worse outcome than best_v9e on 30 gate conditions, and has no reserved-pool validation, so it was not
installed. The reading rule stated before H14 (section 5.14: outcome at least best_v9e's on all 846 gate
memberships, 0 rejected actions, 0 bot errors, no call of 3 s or more) does not name it as the next revision
either: it is worse on 32 memberships, and 3 of its 804 gate games (all in afs5) contain a call of 3 s or more
(slowest 3.77 s; recounted by the main agent from the accompanying artifacts and afg5, not checked by the independent
verifier); the economy worker reaches the same reading. Of the policies whose results on the whole gate are reported here (best_v9e, af2g, AS1C, g0, g1, V29 and
af5), af5 wins the most conditions;
best_v9e is the installed bot because of the pre-stated rules and the held-out checks, not because it wins most
conditions. In the standard-start round robin of ten finalists (section 5.16) it is 8-6-4, behind the validation worker's counter
guard00 (16-0-2) and AS1C (12-4-2); af5, played against the same ten afterwards (the economy worker's afrr), is 16-0-4. W-D-L counts use the engine winner, both
seats. The tested scope is the opponent pools, scenarios and conditions listed below; no claim is made about
opponents or conditions outside it.

### Evidence overview: proved claims, empirical findings and conjectures

The delivered bot in the accompanying artifacts (function `decide`) is best_v9e, frozen at
2026-10-31T12:01Z, installed at 13:07:59Z, replaced by best_v9f from 18:37:45Z to 18:44:53Z and reinstalled then
(frozen copy in the accompanying artifacts, sha256
70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87; sections 5.11, 5.12). It is a deterministic
insurer: it builds a fixed wall layout towards a long route, buys the cheapest plan the frozen
planner finds against sampled rosters the opponent could buy this round when that is affordable, turns
to splash-only defence when the opponent's projected gold buys four tier5 (with guns when a
splash-only plan would still leak), attacks in rounds 2-5 while it trails in HP and from round 6
on, attacks once its own map is immune, and hands the match to the economy worker's frozen econ20 policy (with
the defence worker's re-planner) when its own map holds a building it did not ask for (after a scripted opening).
The validation worker validated it on reserved pool C (no loss in 72 games, section 5.11); pool C was then used to choose between
best_v9e and best_v9f (section 5.12), so for both it is now selection evidence. Its predecessors best_v9a and
best_v9b were validated on pools A and B. On the validation worker's terminal pool D, run once on the final hash after the
selection and used for no choice (section 5.17), best_v9e is 26-6-0 on the standard start, 32-0-0 on a mirror
start and 28-0-4 on an asymmetric start; the four losses are one guard continuation that hoards gold and spends it
on tier5 in round 35 (section 6).

Proved (exact arguments from the source; section 1 and the accompanying artifacts):
- P1 splash immunity (with S >= 1500 no copy of any type reaches the base), P2 lock (both maps immune and
  unchanged freeze the HP difference), and the round-1 certificates (two gun2 layouts that stop all
  27 ordered rosters costing at most 100 gold).
- On the standard start best_v9e never switches to econ20: a building appears on the own map only if
  the bot asked for it and the engine accepted it.

Empirical (recorded games on the unchanged engine, both seats; the engine and our bots are
deterministic, so each result is one observation of a condition, not a sample; some teammate
opponents keep a wall-clock planner cutoff, section 2):
- Development pools: best_v9e's twin 70-6-0 on 38 opponents (FRONTIER5 plus the validation worker's targeted
  counters, run c9i; worst result 0) against 68-4-4 for best_v9b's twin (c8m), 54-2-6 for the best
  earlier setting on FRONTIER5 alone and 42-10-10 for best_v9a; 12-0-4 against the newest teammate
  bots and guarded continuations (t9h) against 8-0-8 for best_v9b's twin (t9b); on scripted openings
  72-6-10 on 88 conditions for best_v9b (run sc1) against 39-12-37 for best_v9a, and 39-0-2 on the 41
  completed of 72 newer scripted-opening games for best_v9e (fx3, partial).
- Independent validation by the validation worker: best_v9a on reserved pool A (10-10-0 standard, 6-12-2 and
  6-12-2 on two prefix families; section 5.4) and best_v9b on reserved pool B (60-0-0: 20-0-0 on the
  standard start and on each of two legal-prefix families; section 5.9); best_v9e, the installed bot, on
  reserved pool C (72 games: 18-6-0 on the standard start, worst 0, and 24-0-0 on each of two
  prescribed-history starts; 33 distinct trajectories; section 5.11); best_v9e on terminal pool D (96 games
  from 23:00:03Z, report-only: 26-6-0 standard, 32-0-0 mirror_104729_3, 28-0-4 asym_130363_2; 44 distinct
  trajectories; section 5.17).
- Cycles 10 and 11 (sections 5.12, 5.13): a capped round-3 purchase (V33C, frozen as best_v9f) passed the
  development gate (498 against 326 wins on the six grower, guard and timing pools, no new loss on the five
  regression pools) and was installed; on pool C it lost C-08 and C-11 (both seats), which best_v9e draws and wins,
  and by the rule posted at 16:59Z best_v9e was reinstalled. Its variant without the round-5 step (V33M) won all
  growers but lost the economy worker's economic timing policy (-37) and was rejected.
- Cycle 12 (section 5.14): af2g, best_v9f with its passive rule off (best_v9e plus four option values), was tested
  under R13, stated at 19:04Z before its gate games: on 14 development pools no condition may be worse than
  best_v9e's. It wins more grower games (GROWERS 128 against 66 wins of 142, GUARDED_MAZE 126 against 66 of 144,
  HANDOFF 24 against 12 of 36, SCREENED 60 against 50 of 60, STAGED 118 against 114 of 140, TARGETED3_P5TF 20
  against 18 of 30) and has the same outcome on every condition of eight other pools, but loses one GUARDED_MAZE
  opponent (growth 4, guard in round 3, tier1 bait) by 815 HP in both seats, where best_v9e wins by 305; R13 therefore rejected it at 19:50Z.
- Attack budget (section 5.14, H14, stated at 20:19:29Z before its games; descriptive, after the final selection):
  best_v9e with all remaining gold for its attacks from round 6 (AS1C; catch-up budget kept at half) wins all 40
  TIMING2 conditions, where best_v9e draws 34 and loses 6, and has a better outcome on 92 of the 846 R13 gate pool memberships,
  but a worse one on 14 (7 opponents in both seats, among them guard_roster with two tier1 and defensive counter 33),
  where accepted attacks reduce factory purchases. It is reported as evidence, not as a revision.
- Complementary strengths (sections 5.12-5.15): best_v9e holds the early strikes and loses about half of the
  passive growers; best_v9f and P5TNUBM win most or all growers and lose early strikes; af2g wins most growers and
  loses one guarded grower that best_v9e beats; the economy worker's g1 wins all growers, handoffs and TIMING2 games and, on
  the 846 R13 gate pool memberships, has a better outcome than best_v9e on 304 and a worse one on 72 (on the 804
  distinct conditions: 282 and 68; mostly early
  exchanges and strikes in STRIKE1 and f5t; the accompanying artifacts, entry 18.18, 18.23), and it loses the standard-start game against
  best_v9e by 10. On the economy worker's 43 fresh opponents (standard start, both seats, section 5.15) best_v9e is 56-12-18,
  g1 70-0-16 and the economy worker's later af5 (V29 + attack_from=5) 78-0-8; on the 15 of them that are not counters built by the validation worker
  (the main agent's bots and the defence worker's fortresses) 20-8-2, 20-0-10 and 24-0-6. On the 804 distinct R13 gate conditions af5
  is 764-2-38 against best_v9e's 504-64-236 (worse on 30, better on 288; section 5.15), and on 120 scenario-start games (the economy worker's scnaf5) every
  af5 game has V29's result. On the standard start best_v9e beats the defence worker's v46 and v48 by 5 and
  g1 by 10 (decided in the blind round 1) and loses to the economy worker's af5 by 410 in both seats (afrr, section 5.16); on scripted starts the defence worker's fortress (v41 3 of 10, v46 and its
  final v48 7 of 10) and V29 win some games against it. Against opponents that all play one grower's opening and then either keep growing or strike with
  budget_timing (H12, section 5.14), best_v9f, V33M and P5TNUBM win all 24 conditions and best_v9e loses only the
  two grow continuations, so there the trade-off is not forced by a common history. The evidence does not support
  one universally dominant policy.
- Ablations (section 5.14): with all four insurance options off, best_v9e wins all 142 GROWERS conditions (it
  loses 76 as installed) and loses 12 wins and 2 draws of the 20 completed f5t conditions (ab3, ab14); each of the
  three insurance options alone costs grower games (ab15-ab17), and the round-1 tier1 poke wins 30 f5t games that
  are draws without it (ab2). Without rule 3b's all-gold insurance (ab12) 13 f5t opponents that best_v9e beats
  at round 50 are lost at round 50 in both seats (44-6-26 instead of 70-6-0); without its least-leak plan (ab4) or
  the fortress trigger (ab5) two f5t opponents are lost; without the gun replacement of rule 3b (ab11) or the
  rounds 2-5 catch-up attack (ab10) one f5t opponent each turns from a win or a draw into a loss in both seats.
- Final round robins (section 5.16; descriptive, one game per pair and seat): on the standard start, among ten
  finalists, best_v9e is 8-6-4, behind the validation worker's counter guard00 (16-0-2; it loses only to g1) and AS1C (12-4-2; it
  beats best_v9e by 60 with a round-6 tier4); every margin between the nine non-baseline bots is at most 60 HP, and
  the results are not transitive (g1 beats guard00, guard00 beats best_v9e, best_v9e beats g1). In the W/D/L game
  of these ten bots every max-min mixture puts 1/3 on g1, 1/3 on guard00 and the remaining 1/3 split between AS1C, best_v9f and P5TNUBM, and
  none on best_v9e, which AS1C and best_v9f weakly dominate there (exact, for that matrix). With the economy worker's af5 added
  (its afrr games; af5 is 16-0-4 against the ten and beats best_v9e by 410) the max-min mixtures put 1/3 on af5,
  1/3 on guard00 and the remaining 1/3 split between P5TNUBM and AS1C, and none on g1 or best_v9e (linear programming, section 5.16). On the scripted
  starts mirror:1:2 and asym:23:2, best_v9e, best_v9f and AS1C are 6-4-10 each, behind V29 and g1 (12-2-6).
  The defence worker's v46 (its final recommendation until 22:39Z, then v48) is 4-4-12 against the ten on the standard start
  (frr3), with v41's outcome against each other bot; it loses to best_v9e by 5 and does not change the max-min
  mixtures; its successor v48 has v46's outcome and margin in all 20 of these games (frr5). On the two scripted
  starts (frr4) v46 is 22-2-0 against the six frr2 bots and is the only bot that wins asym:23:2 in seat 1 against
  every other bot; v48 has the same 24 results (frr6). The economy worker's af5 (V29 + attack_from=5) is 13-4-11 on these two
  starts against best_v9e, best_v9f, v41, V29, g1, AS1C and v48, and each of its 28 games has the result of the
  corresponding V29 or g1 game (frr7).
- Known failures (section 6): passive growers with a cheap bait (found by the validation worker; best_v9b and
  best_v9e lose 76 of 142 such development games; the revision P5TNUBM wins all of them but loses
  small-margin early strikes that best_v9e holds, so it was not installed, section 5.11), locked draws against
  defended strikers and guards (TIMING2 0-34-6: its attacks, with half the remaining gold, land no hit in rounds
  6-19, before budget_timing's map locks at round 20; the economy worker), early walls with a round-3 guard (the validation worker's guard00, 770:740), a counter
  built by the validation worker after the selection from an omitted sampled roster (screened_roster_guarded, 800:774), exact forecasters,
  below-threshold waves, the round-3 tier3 window found by the validation worker, round-2 blind strikes, scripted openings that
  cap the route, and a second counter built by the validation worker after the selection (delayed walls with a reserved round-4
  tier4, 770:740 against best_v9e and AS1C, section 6), and on pool D a guard continuation after a prescribed
  prefix that hoards gold while best_v9e's econ20 handoff keeps a 22-step route and buys only capped factories, then
  spends it on 281 tier5 in round 35 (-3120:785, four games, section 5.17). Its decision time grows with the opponent's hoarded gold
  (8.13 s per call at round 50 against a fortress holding 12 million gold; section 7).

Conjecture (not established): that no deterministic policy of this kind avoids every forecast
counter (the counters in sections 4.2 and 5.3 exploit determinism, but no impossibility argument
covers all policies); that the remaining scripted-opening losses come from the scripted walls capping
the route length and hence S (the defence worker states this as a conjecture for asym:23:2).

## Final bot: decision rules of best_v9e

The delivered bot in the accompanying artifacts (sha256 70ef8eab..., identical to its frozen copy) is one
deterministic policy object per player index, renewed in round 1. Each call reads only the observation and the
object's own record of its earlier calls (the cells it asked to build on, its last attack's predicted damage and the
opponent's HP before it, a failure count and the sticky fortress flag). Every simulation below is the exact combat
model in the accompanying artifacts (tested against the engine); the planner is the defence worker's frozen v7 planning module, imported
unmodified, with no wall-clock cutoff. Its module docstring states the same rules with the development reason for
each. Values are the installed defaults.

0. Walls. Buy the stage-A walls of the defence worker's default master layout first, as far as gold allows, so every plan is made
   on the route that exists after this round's construction.
1. Round 1. Three tier1 (`r1_poke=3`), factories with the rest.
2. Mandatory defence (round 2 on). Buy the cheapest plan the planner finds with zero simulated leaks against the
   opponent's visible active roster, or the least-leak plan the planner finds within all gold when zero leaks are unaffordable.
3. Insurance against sampled rosters the opponent could buy this round (visible active entries plus each purchase
   in a sampled list its visible gold allows; at most nine lists, so not every affordable roster is listed). From the
   first round in which the opponent's visible gold plus 3 rounds of its visible income would buy 4 tier5
   (`fortress_n=4`, `fortress_k=3`), every plan of this step uses splashes and walls only for the rest of the match.
   a. Buy the zero-leak plan against all listed rosters if it costs at most 0.6 of the remaining gold (`spec_share`).
   b. Otherwise, if the worst listed roster deals at least 100 this round (`big_threat=100`), buy that plan with up
      to all gold, or the least-leak plan the planner finds within all gold (`big_partial=true`); a splash-only plan that still leaks
      is replaced by a zero-leak plan with guns when one is affordable (`fortress_guns=true`).
   c. Otherwise, through round 3 (`poke_until=3`) and only while the opponent owns a turret or its visible roster
      holds a tier1 or tier2 entry bought in round 2 or later (`poke_reactive="turret"`), buy the zero-leak plan
      against the tier1/tier2 rosters if it costs at most 0.6 of the remaining gold.
   d. Through round 5 (`mid_until=5`), under the opponent condition of c, buy the zero-leak plan against listed
      rosters made only of types with at most 180 HP if one of them still leaks and the plan costs at most 0.6.
4. Attack. From round 6 (`attack_from=6`): for each tier, simulate 0.5 of the remaining gold (`attack_share`) of
   copies, subject to the purchase cap, against the opponent's current map and buy the tier with the most extra damage per gold if that is at
   least 0.1. After the first attack that dealt less than half of its prediction (judged from the opponent's HP in
   the next observation) the rest of the match uses the robust rule: the two best tiers are replayed after the
   opponent's estimated best response with all its visible gold, and the better one is bought if it still reaches
   0.1 damage per gold (`attack_mode="adaptive"`). In a round in which our own map has S >= 1500 the first rule is
   used whatever the mode (`immune_attack=true`; by P1 gold then has no defensive use). Rounds 2-5: while our HP is
   below the opponent's, the first rule is run on 0.5 of the remaining gold (`catch_up=true`).
5. Factories with the rest, subject to the per-round purchase cap and late-game cutoff.

Foreign maps. From the first round in which the bot's own map holds a building at a cell it never asked for (a
scripted or prescribed start; impossible on the standard start, section 1), the rest of the match is played by a
fresh instance of the economy worker's frozen econ20, imported unmodified, with the defence worker's frozen re-planner (fixed seed, fixed
iteration count). Plans against rosters longer than 120 copies use splashes only (`gun_cap=120`), which bounds the
gun search; it does not bound the decision time, which grows with the opponent's gold (section 7).

What carries which result (single-option and combined ablations of the frozen policy, section 5.14; empirical, within the
named pools): without rule 3 (no insurance at all) 14 of the first 20 f5t conditions are lost, down to -2675, where
best_v9e wins 18 and draws 2 (partial run ab3); without rule 3b's all-gold insurance (`big_threat=null`) 26 of the
70 f5t wins become losses at round 50, by 55 to 270 (ab12); without the round-1 tier1 (`r1_poke=0`) 30 of the 70 f5t wins become draws, and the standard-start
games against the listed fortress bots, V29 and g1 are decided in round 1; af5 is an exception (section 5.15); without rule 3d (`mid_until=null`)
the round-5 tier3 strikes of econ13 and econ15 are lost (+10 becomes -16); without `immune_attack` the
guarded-schedule opponents with a round-5 or round-8 tier4 are lost (4 games, +2194 and +748 become -36). In the
code of best_v9f with its passive rule off (af2g), replacing best_v9e's turret-or-bait condition of rules 3c and 3d
by a turret-only condition accounts for all 62 GROWERS outcome changes and for the one lost guarded maze (runs gy1
and gmchk2): the bait condition is what loses about half of the passive growers and what wins that guarded maze
(best_v9e also loses another guarded maze that af2g wins, after the same history up to its round-3 decision; that
condition was not ablated; section 5.14). The attack budget
limits the TIMING2 results: with `attack_share=1.0` all 34 draws and 6 losses there become wins, while removing the
robust attack rule, rule 3b or the fortress trigger changes no HP (run tsc). On all 846 R13 pool memberships the same
change (with the catch-up budget kept at 0.5) is better on 92 and worse on 14, which are 7 opponents in both seats, and the
shares 0.65 and 0.75 already lose two of them (H14 and the share screen, section 5.14): the half share costs the
budget_timing strikes, and in the two traced losses of the full share its attacks reduced factory purchases.

## 1. Game facts used (see the accompanying artifacts for sources and checks)

All rules are taken from the bundled source; the game contract in the accompanying artifacts lists source references and
10 reproduction checks on the unchanged engine (all pass). The facts the bots rely on:

- Two players, each with its own 12 x 12 map (spawn (0,0), base (11,11)); 50 rounds; 800 HP and
  100 gold at the start. Actions are submitted simultaneously from a full public observation.
- Income per round: route length of one's own map, plus 15 per factory (a factory costs 20 and
  already pays in its purchase round), plus 5 gold per own minion hit on the opponent's base.
- Minions (cost / HP / damage): tier1 15/20/5, tier2 40/70/12, tier3 100/180/26, tier4 260/560/60,
  tier5 650/1500/140. A purchase is a roster entry that spawns one full-HP copy every round for 12
  rounds (purchase round included). Entry k of the active roster spawns at tick k mod 250 and can
  arrive only if spawn tick + route length <= 249.
- Turrets: splash (60 gold) hits every copy on the 8 neighbouring cells for 10 per tick; gun1/gun2/
  gun3 (30/80/200 gold, 8/22/55 per tick, range 2.5/3/3.5) hit only the frontmost copy in range.
  Walls cost 1. Buildings are permanent and may not disconnect spawn from base.

Proved facts (from the code; proofs in the accompanying artifacts):

- P1 (splash immunity). Let S = 10 x (sum over route cells 0..L-1 of the number of adjacent
  splashes). Every copy with HP <= S that has enough ticks left to reach the base is killed before
  it arrives, independently of the number and order of copies; a copy spawned too late to arrive can
  still be alive when combat ends and is then cleared without dealing damage (the validation worker executed such a
  legal game: one splash, S = 30, 250 tier1 bought in round 9; 249 die, one is cleared alive with
  10 HP, zero base damage; the accompanying artifacts). Hence
  S >= 1500 means zero base damage from every finite roster of every minion type.
- P2 (lock). If both players have S >= 1500 on maps they will not change, no further damage can be
  dealt and the HP difference at that moment is the final result (the economy worker, the accompanying artifacts,
  Proposition 5).
- Round-1 certificate (proposal by the external referee, a second model, checked by the main agent and independently by the validation worker on the
  engine for all 27 ordered rosters costing at most 100 gold): a gun2 at (3,2) plus walls (x,1)
  for x = 0..4 and (6,y) for y = 0..3 (89 gold, route 22) lets no copy of any first-round
  purchase reach the base. Within the default master layout, 20 stage-A walls plus a gun2 at (1,3)
  (100 gold, route 42) has the same property (found by the search in the accompanying artifacts with the
  combat simulator; every one of the 27 rosters replayed on the unchanged engine by
  the checker in the accompanying artifacts, zero damage in each).

## 2. Method

- Harness (the accompanying artifacts): unchanged engine and adapter, one fresh process per match,
  both seat assignments for every pairing, per-match version tag (hash of the bot's static import
  closure plus the harness), rejected-action and bot-error counts, decision time per call.
  `the combat simulator` replays one map's combat exactly (a unit test compares it with the
  engine).
- Determinism: the engine is deterministic. Our bots' normal branch and the frozen planner use no
  randomness and no wall-clock cutoff. The foreign-map branch (econ20) imports the defence worker's replanner, which
  uses `random.Random` with a fixed seed and a fixed iteration count (reproducible pseudorandom choices),
  and passes a finite `plan_time=1e6` (a one-million-second gun-planning deadline, not reached in any
  recorded call) to the frozen planner (the validation worker's review, the accompanying artifacts).
  Repeated identical matches are therefore not independent evidence. Some opponent bots are not load-independent at source level: the defence worker's frozen
  fortress v26, v27 and v28 keep a 3-second cutoff in the gun planner (the validation worker, the accompanying artifacts
  10:38Z), and so do the later fortress versions v34 to v48, among them v41 (the worker's final recommendation until
  20:32Z, used in frr1 and frr2), its alternative v43 and the later final recommendations v46 (21:45Z to 22:39Z,
  used in frr3 and frr4) and v48 (from 22:39Z, frr5 and frr6) (`TIME_BUDGET = 3.0` in their frozen planners; the economy worker,
  the accompanying artifacts, entry 18.9 item 12; checked by the main agent for v41 and v43 to v48). The recorded seat pairs against them agree, which does not establish independence of
  machine load. Evidence comes from distinct opponent policies, parameter settings and
  seats. Results are reported as W-D-L counts and HP differences, not as sampled win rates.
- Tuning versus validation: the main agent tunes only against the pools in
  the accompanying artifacts (TUNING, STRONG, FRONTIER to FRONTIER5 and the later development pools).
  The validation worker held four reserved pools. Each is held out only for the first frozen version evaluated on it:
  pool A for best_v9a and pool B for best_v9b. Both pools' results and counterexamples were disclosed
  after those runs, so later revisions do not inherit held-out status on A or B. Pool C was kept unused
  until the late freeze (selection record in the accompanying artifacts at 16:12Z: best_v9e stays installed); the validation worker then ran it on best_v9e, with P5TNUBM as a
  comparison declared beforehand that could not be selected (section 5.11). Pool D (declared 18:11:52Z) was run
  once, from 23:00:03Z, on the hash named in the 19:50Z selection record in the accompanying artifacts and only reported (section 5.17). Many campaigns in the accompanying artifacts are disclosed development tests; the
  label alone does not make a test held out.

## 3. Development history (cycles 1-3, main-agent planner versions)

| version | idea | result (development pools) |
| --- | --- | --- |
| v1 (the accompanying artifacts) | template maze, one-round expected-damage splash rule, attack by exact simulation on the opponent's current map | 56-0-0 vs TUNING (28 opponents); lost to its own kappa=8 variant |
| v2 (the accompanying artifacts) | known threats valued over 4 rounds, income-scaled kappa | beat v1; lost to econ by 8 HP; self-play destroyed both bases (defence cliff) |
| v3b (the accompanying artifacts) | multi-round threat valuation, joint defence/attack scoring, lethal penalty | lost to eco6_t5 (-220 to -756), fortress (-60 to -215), econ (-10 to -35) (the accompanying artifacts) |

Diagnosis of v3b (traces, the accompanying artifacts and c2rr1):
- Splash-only insurance lags single big copies: each new tier leaks for at least one round.
- Attacks were valued against the opponent's current map; opponents that insure every round
  with guns (econ, fortress) stopped all of them.
- The validation worker found targeted counters: a forecast-defended round-8 all-in tier5 wave beats v3b 800:-40;
  a six-purchase schedule destroys it in round 15 (the accompanying artifacts, 03:15Z and 03:18Z).

Round robin c2rr1 (11 bots, 110 matches, both seats): the fortress bot of the defence worker with
attack_from=6, attack_share=0.5 had the best mean HP difference (+251); between bots that insure
every round, nothing lands after round 1, and matches are decided by round-1 tier1 pokes against
bots that buy only factories in round 1.

## 4. Cycle 4: planner v4 to v7

Design: zero-leak insurance against the opponent's affordable purchases using the defence worker's frozen
planning component (the accompanying artifacts, imported unmodified), plus a main-agent policy
layer (round-1 decision, insurance rule, attack rule). Prototype result c3proto1 (fortress v4
plus a round-1 poke of 0/1/2 tier1, FRONTIER pool, 96 matches): 2 tier1 in round 1 gave 24-0-0.

### 4.1 Development pool results (FRONTIER2, 15 opponents, both seats)

The initial implementation, its ablation variants and the result tables are in the accompanying artifacts
(300 matches, no harness errors, rejected actions or bot exceptions).
W-D-L counts in this report use the engine's winner field: a simultaneous destruction of both bases
is a draw whatever the residual HP. The validation worker found (the accompanying artifacts, 06:03Z) that an earlier
version of the results script in the accompanying artifacts counted by HP sign; this changed two rows of the table below
(both now corrected) and no other count in this report.

| setting | W-D-L | notable non-wins (mean HP difference) |
| --- | --- | --- |
| v4 default (poke 2, spec_share 0.6, poke insurance, attack from round 6) | 24-0-6 | v4proto -60, econ v4 late6 -10, known_policy -2 |
| grades 1/0.7/0.5/0.35 (partial-gold insurance) | 12-0-18 | forecast_timing -410, eco6_t5 -680 |
| round 1: factories only | 12-12-6 | |
| round 1: one tier1 | 20-2-8 | |
| attack from round 3 | 26-0-4 | v4proto -140, known_policy -2 |
| no poke insurance | 24-2-4 | econ v4 late6 -50, known_policy -2 |
| adaptive attack | 24-0-6 | as default |
| three tier1 in round 1 | 22-2-6 | forecast_timing -125, econ v4 late6 -45; draws eco6_t5 (both bases destroyed) |
| poke insurance with all gold | 14-2-14 | draws eco6_t5 (both bases destroyed) |

Empirical interpretation (this pool): these ablations suggest that unnecessary early defensive purchases
can lower the result by reducing compounding before a later flood must be
stopped (with full reinvestment one gold in round 1 is worth about 1.75^7, roughly 50 gold, in round
8). The defence worker (x7) and the economy worker (sweep7) report the same direction for their bots.

### 4.2 Known-policy exploitability screen

The validation worker (the accompanying artifacts, 03:41Z) built a counter that forecasts the exact actions of the
deterministic v4 snapshot each round, defends against them, and buys one timed wave; their best
confirmed result was a round-9 tier5 wave, 800:380 for the counter. The main agent's screen
(the counter wrapper and screen in the accompanying artifacts, using the validation worker's ForecastTiming unmodified with an exact
model of any main-agent setting) plays each setting against 10 timings (tier3 at
rounds 3 and 5, tier4 at 5, 7, 9, tier5 at 7 to 11; all of the counter's gold; both seats). The
number reported is the lowest candidate HP difference over the grid (the archived screen results in the accompanying artifacts).

| setting | lowest HP difference (timing) |
| --- | --- |
| v4 default | -980 (tier5 at round 10, base destroyed) |
| spec_share 1.0 | -1120 |
| spec_share 0.8 | -1840 |
| robust attack only | -560 |
| no poke insurance | -840 |
| planner v11 | -1820 |
| big_threat 100 (insure with all gold if the worst affordable purchase would deal at least 100 this round) | -280 |
| big_threat 100 and robust attack | -60 (tier4 at round 5); every tier4/tier5 timing from round 7 on blocked |
| the same, partial plan when zero leaks are unaffordable (big_partial) | -60 (identical results) |
| the same, at most 80 factories per round | -60 (identical lowest cells) |
| big_threat 100, robust attack, no poke insurance | -26 (tier3 at round 3, one copy lands); all other timings 0 |
| the same without the round-1 poke | -26 (same cells) |
| big_threat 50, robust attack, big_partial | -420 (tier5 at round 9) |

Trace of the default's loss (the accompanying artifacts): its attacks in rounds 6-10 never landed (the
counter defends against them in the same round), its speculative guns covered no later wave, and at
round 9 the counter had 275 factories against our 81. "Robust" attacks only if the attack still
leaks after the opponent's estimated best same-round response (the defence worker's planner run from the
opponent's side with its visible gold), which removes those purchases; big_threat removes the
skipped-insurance rounds before the big waves. Both changes are needed (rows above). Lowering the
threshold to 50 insures more often and loses the round-9 tier5 wave again, and the poke insurance
(tier1/tier2 rosters only) costs the gold that stops the round-5 tier4 wave; both observations
repeat the economic finding of 4.1. The remaining -26 (s6-k2): in round 3 the counter has 137 gold
and buys one tier3; the worst affordable roster deals 26 < 100 on our map and the zero-leak plan
costs more than 0.6 of our 230 gold, so we buy factories; the tier3 is stopped from round 4 on.
Against an exact forecaster every leak decides the match, because none of our attacks lands.

## 5. Cycle 5: the poke fallback and the frozen candidate best_v9a

### 5.1 Development pool FRONTIER4 (24 opponents, both seats)

FRONTIER4 is FRONTIER2 plus econ v8 (two layouts), fortress v11 (two layouts), planner v4, fortress v15,
econ v9, econ v10 and the validation worker's falsification_fallback with fortress13. Archived runs in the accompanying artifacts, including `c5b` and
`c5c` (432 matches; no harness errors, rejected actions, bot exceptions or source changes; tables in
the accompanying artifacts). All settings below use big_threat=100 and the robust attack. "Poke fallback" is the
insurance against tier1/tier2 rosters only (rule 3c of the delivered bot in the accompanying artifacts).

| setting | W-D-L | non-wins (HP difference, both seats equal) |
| --- | --- | --- |
| no poke fallback (initial candidate, = v7) | 32-6-10 | fortress v7/v11/v15 default -5, econ late6 -50, known_policy -2; draws econ8, planner v4, v4proto |
| the same, gun_cap=120 | 32-6-10 | identical results; slowest decide 0.83 s instead of 3.70 s |
| poke fallback every round | 34-6-8 | eco6_t5 -160, eco_then_flood(8) -160, econ late6 -10, known_policy -2; draws fortress v15, planner v4, v4proto |
| poke fallback through round 3 | 34-6-8 | eco6_t5 -160, eco_then_flood(8) -160, econ late6 -10, known_policy -2; draws fortress v15, planner v4, v4proto |
| poke fallback through round 4, 0.3 of the gold | 32-6-10 | as without the fallback (the smaller budget buys nothing) |
| fallback only while the opponent shows a tier1/tier2 bought in round >= 2 | 34-4-10 | fortress v7/v11/v15 -5, econ late6 -10, known_policy -2 |
| fallback through round 3, only while the opponent owns a turret or shows such an entry (best_v9a) | 38-6-4 | econ late6 -10, known_policy -2; draws planner v4, v4proto, fortress v15 |
| the same with three tier1 in round 1 | 42-0-6 | eco6_t5 -100, eco_then_flood(8) -100, econ late6 -45 |
| roster condition only, three tier1 in round 1 | 28-8-12 | |

Loss review (traces with the accompanying artifacts):
- Without a fallback, fortress v7 answers our round-1 poke with a gun1 in round 2 and buys three tier1
  in round 3; they are not visible before round 4, so 15 HP land against our 10.
- With the fallback in rounds 2-3, the splash bought in round 3 (60 gold) leaves 626 gold in round 8
  against eco6_t5, while the plan that stops its four tier5 copies costs 840 (14 splashes; without the
  fallback we had 902). The planner then buys nothing and two copies land (280). The loss is
  economic compounding of one early purchase, not a placement effect.
- The turret condition separates the two cases in this pool: fortress and econ bots own a turret
  from round 2, the eco-flood bots own none before their flood. It is a heuristic, and an opponent can
  trigger it with a useless turret (section 6).
- With three tier1 in round 1 the eco-flood bots win the same way (682 gold in round 8 against 840).

Empirical finding (FRONTIER4, these settings): the round-1 to round-3 exchange decides every match
between insurers; the poke fallback gains 5 to 15 HP against pokers and costs 100 to 160 HP against
pure economy floods, so it is worth buying only when the opponent is not on a pure growth path.

### 5.2 Frozen candidate

The 38-6-4 setting was installed as the delivered bot in the accompanying artifacts at 06:11Z and later replaced by best_v9b and
best_v9e (sections 5.9, 5.11) (frozen copy
in the accompanying artifacts, sha256 88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d).
Its decision rules are in the module docstring. Its development twin
in the accompanying artifacts (big_threat=100, robust attack, gun_cap=120, poke_until=3,
poke_reactive="turret") plays identical full trajectories in 8 checked games
(the accompanying artifacts). The candidate was posted
to the validation worker for targeted counters and independent validation at 06:11Z.

### 5.3 Targeted counters by the validation worker against the predecessor (planner v7 snapshot)

The validation worker (the accompanying artifacts, 05:12Z to 05:41Z) froze the no-fallback setting with gun_cap=120 in
the accompanying artifacts and confirmed, with strict source attestation and full
engine replays:
- eight early counters win with margins of at most 26 HP (round-1 mixed and tier1/tier2/tier3
  purchases, round-3 tier3);
- a fixed opening (gun1 at (3,1), one tier1, two factories, then economy13) wins 800:795;
- a two-wave schedule (one tier1 in round 1, one tier4 in round 5) wins 800:735: the tier4 deals 60 in
  round 5, below big_threat, and the zero-leak plan costs more than 0.6 of our gold.

### 5.4 Targeted validation of best_v9a by the validation worker

The validation worker (the accompanying artifacts, 06:16Z and 06:24Z) played the published entry point against eleven
targeted counters, both seats (22 games, strict source checks and full engine replays, both seats
agreeing in every condition). Candidate HP first:

| opponent | best_v9a |
| --- | --- |
| feature_bluff without a turret (growth control) | W 800:680 |
| feature_bluff, off-route gun in round 1 / 2 / 3 | L 520:680 / L 380:680 / L 520:680 |
| cheap guard (gun1 (3,1), one tier1, two factories) + economy13, + economy15 leak | L 795:800, L 795:800 |
| guarded schedule: one tier1 in round 1, tier4 wave in round 5 / round 8 | L 735:800 / L 435:800 |
| economy13, economy15 leak | W 795:790, W 795:790 |
| fortress v21 | D 790:790 |

This is a set of counters built against this bot, not a population estimate. The validation worker's matched
ablation (24 + 24 games with the development twin) replaced the turret condition of the poke
fallback by the roster-only condition: no W-D-L outcome changed, and only the round-2 gun condition
changed its margin, by one tier5 hit (140 HP). The bluff wins are therefore not a feature exploit;
they come from the opponent's growth path (section 6).

Independent validation on reserved pool A (the validation worker, the accompanying artifacts, 06:43Z to 07:08Z). Ten
held-out opponent parameter settings chosen and frozen by the validation worker before the campaign, both seats,
standard starts and two separately scored legal-prefix continuations (60 conditions), frozen sha256
88a8e42f...829d. All 60 selected results pass the validation worker's strict accounting and a full replay on the
unchanged engine, and all 30 seat pairs have identical normalized trajectories. The two original
standard mirror games exceeded the validation worker's 300-second limit; separately archived 500-second retries
completed as 800:800 draws; the failed attempts stay in the accounting with no outcome assigned.

| condition | best_v9a W-D-L |
| --- | --- |
| standard start | 10-10-0 |
| one-round factory prefix | 6-12-2 (losses 790:800) |
| asymmetric splash prefix | 6-12-2 (losses 660:800) |

The validation worker reports that all four loss margins arise after the prescribed first round, not from damage
inherited at the prefix boundary. The main agent has not read the pool definitions. The result
covers these declared conditions only; it does not establish dominance or random-sample
confidence, and the policy implementations are shared with development (the validation worker's
holdout-separation audit found zero exact parameter overlaps among the recognized development
records). Pool B is unused and reserved for a revision.

### 5.5 Cycle 6: partial plans against unaffordable big threats (FRONTIER5)

Loss review of the bluff games (the accompanying artifacts on the c5d logs, bluff with the gun
in round 3): in round 7 best_v9a has 758 gold, the opponent 1407 and no roster; the worst affordable
roster deals 200, so the big-threat rule buys the cheapest zero-leak plan, three gun3 (600 gold). In
round 8 the opponent shows two tier5 and has 1509 gold; no zero-leak plan fits our 867 gold, so
best_v9a buys nothing defensive (40 factories) and takes 280. The least-leak plan within all gold
would have been 14 splashes and 4 walls (844 gold). Two mechanisms: the one-round planner prefers
guns when they are cheapest this round, and guns do not carry forward against a larger wave of the
next round, while splash value adds up towards S >= 1500; and without a partial plan the gold is
not used against the wave at all.

Variant big_partial: when the big-threat plan has no zero-leak solution within all remaining gold,
buy the least-leak plan within all remaining gold. FRONTIER5 is FRONTIER4 plus fortress v19 and v20,
econ13, econ15, cheap guard + economy13, and the bluff with the gun in round 1 and in round 3 (31
opponents, 62 matches per setting). Run recorded in the accompanying artifacts (186 matches; no harness errors, rejected
actions, bot exceptions or source changes; slowest decide 2.38 s). best_v9a's results on the
FRONTIER4 opponents equal those of its twin in c5c (consistency check).

| opponent (HP difference, both seats equal) | best_v9a | + big_partial | + big_partial, three tier1 in round 1 (C2) |
| --- | --- | --- | --- |
| falsification_fallback | +1430 | +990 | +15 |
| bluff, gun in round 1 | -160 | -440 | +180 |
| bluff, gun in round 3 | -160 | -20 | +40 |
| eco6_t5, eco_then_flood(8) | +120 | +120 | +40 |
| best_v3b | +10 | +10 | +269 |
| econ13, econ15 | +5 | +5 | -16 |
| econ v4 late6 | -10 | -10 | -45 |
| known_policy | -2 | -2 | +3 |
| cheap guard + economy13 | -5 | -5 | 0 (draw) |
| fortress v15, v19, v20, planner v4, v4proto | 0 (draws) | 0 | +5 |
| all other 16 opponents | +5 to +120 | as best_v9a | +5 to +180 |
| W-D-L | 42-10-10 | 42-10-10 | 54-2-6 |

Findings (FRONTIER5, these settings):
- big_partial alone is not an improvement: with two tier1 in round 1 the all-gold partial plans of
  rounds 7-9 starve the economy against the round-1 bluff (-440).
- With three tier1 in round 1, the total bounty from that roster (+15 per round while all three copies
  arrive) is a possible contributor to the improved results with partial plans. Trace of the round-1 bluff
  (c5d log 00183): no damage taken in rounds 1-11; in round 8 big_partial buys 12 splashes (S = 770),
  which together with the earlier guns stop the tier5 waves.
- C2's losses: against econ13 and econ15 one round-5 tier3 deals 26, which is below big_threat;
  their round-2 gun1 stops our three tier1, so the 5-HP round-1 gain is not there. Against econ v4
  late6 one more tier3 copy lands (-45).
- C2 is the revision candidate of cycle 6. At this point it had not been screened against forecasters or
  scripted openings (runs queued by a cycle-6 queue script that is not among the accompanying artifacts);
  it was not frozen (section 5.6).

Attack mode ablation on C2 (run recorded in the accompanying artifacts, FRONTIER5, 124 matches; no errors, rejected
actions, bot exceptions or source changes; slowest decide 2.80 s). "current" buys the best attack
against the opponent's current map without the response check; "adaptive" does so until one attack
has dealt less than half of its predicted damage, then switches to "robust".

| opponent | C2 robust (c5d) | C2 adaptive | C2 current |
| --- | --- | --- | --- |
| bluff, gun in round 1 / round 3 | +180 / +40 | +535 / +590 | +535 / +590 |
| eco6_t5 | +40 | +645 | +645 |
| mixed5 | +180 | +1465 | +1465 |
| eco_then_flood(8) / (12, tier4) | +40 / +180 | +810 / +805 | +810 / +805 |
| fortress v7 default | +15 | +155 | +155 |
| fortress v7 and v11 with layout annealed25 | +15 | +135 | +135 |
| best_v3b | +269 | +317 | +177 |
| the other 21 opponents | | identical to robust | identical to robust |
| W-D-L | 54-2-6 | 54-2-6 | 54-2-6 |

Unchecked attacks land against bots that grow without insuring and change no W-D-L outcome in this
pool; they were the cause of the forecaster losses of section 4.2, so the adaptive mode is screened
against the forecaster before it is used (run s10).

### 5.6 C2 against the validation worker's targeted counters (pool TARGETED)

Run recorded in the accompanying artifacts (the eleven opponents of section 5.4 as pool TARGETED in
the accompanying artifacts, both seats, 44 matches; no errors, rejected actions, bot exceptions or
source changes; slowest decide 2.42 s). The best_v9a column reproduces every HP pair of the validation worker's
06:24Z table (an independent check of the two harnesses on 22 games).

| opponent (HP difference, both seats equal) | best_v9a | C2 (robust attack) |
| --- | --- | --- |
| bluff without turret | +120 | +40 |
| bluff, gun in round 1 / 2 / 3 | -160 / -300 / -160 | +180 / -1125 (base destroyed, round 9) / +40 |
| cheap guard + economy13 / + economy15 leak | -5 / -5 | 0 / 0 (draws) |
| guarded schedule, tier4 in round 5 / round 8 | -65 / -365 | -65 / -5 |
| economy13 / economy15 leak | +5 / +5 | -16 / -16 |
| fortress v21 | 0 (draw) | +5 |
| W-D-L | 6-2-14 | 8-4-10 |

Loss review of C2 against the round-2 gun bluff (the accompanying artifacts on t1 log 00027): the
bluff buys only factories after its gun (87 factories in round 6 against our 26) and never defends;
the robust rule never attacks it, because it assumes a same-round response with all of the
opponent's 1327 gold that never comes. From round 6 the big-threat rule buys the cheapest zero-leak
plans against one or two tier5, mostly guns (360 gold in round 6, 450 in round 7). The bluff buys two
tier5 in each of rounds 7, 8 and 9; each entry spawns a copy every round, so 2, 4 and 6 copies arrive,
and 140, 420 and 700 HP land. Guns hit the frontmost copy only; against a growing roster the
gun-heavy plans of one round do not carry over to the next. C2 is therefore not frozen; cycle 6
continues with the adaptive attack (which attacks such growers) and the lead guard (run t2, section
5.7).

### 5.7 Cycle 7: revisions against the round-2 gun bluff

All settings below are C2 with attack_mode "adaptive" (A; section 5.5 showed it equal to C2 robust in
W-D-L on FRONTIER5) plus the named option. Pool TARGETED, both seats, HP difference (equal in both
seats in every pair).

Run recorded in the accompanying artifacts (88 matches; no errors, rejected actions, bot exceptions or source changes;
slowest decide 2.17 s). The lead guard (the accompanying artifacts, lead_guard_from=4) buys the full
zero-leak plan with up to all gold whenever the worst sampled roster would remove our current HP lead;
"turret" restricts it to opponents that own a turret.

| opponent | A | A + lead guard 4 | A + lead guard 4, turret | A with r1_poke=2 |
| --- | --- | --- | --- | --- |
| bluff without turret | +645 | -835 | +645 | +1225 |
| bluff, gun in round 1 / 2 / 3 | +535 / -1065 / +590 | +550 / -785 / -895 | +550 / -785 / -895 | +620 / -855 / +625 |
| cheap guard + economy13 / + economy15 leak | 0 / 0 | 0 / 0 | 0 / 0 | -5 / -5 |
| guarded schedule, tier4 in round 5 / round 8 | +699 / +20 | +193 / -9 | +193 / -9 | -29 / -161 |
| economy13 / economy15 leak | -16 / -16 | +10 / +10 | +10 / +10 | +5 / +5 |
| fortress v21 | +5 | +5 | +5 | 0 |
| W-D-L | 12-4-6 | 10-4-8 | 12-4-6 | 10-2-10 |

In the archived run (the accompanying artifacts), open_attack_from 2 or 3 (the attack step also runs in
the early rounds while no opponent turret covers its route) loses to all four bluffs (-420 to -780;
the early attacks cost the economy that the grower outbuilds). poke_reactive "relevant" (only turrets
that cover the opponent's route) and poke_reactive true (no turret condition) leave every bluff W-D-L outcome
of A unchanged, including the losing margin -925 against the round-2 bluff. None of these options is kept.

Loss review of A against the round-2 bluff (t2 log 00005, the accompanying artifacts). Through round 9
A spends 1830 gold on defence, mostly guns (round 6: three gun2 and a gun3; round 7: gun1, two gun2,
gun3, splash). On the empty map the cheapest plan the defence worker's planner finds against one tier5 costs 420
with guns, against four tier5 1529 with or without guns, the latter being the splash fortress
(the accompanying artifacts, exact computation). The bluff buys two tier5 in each round from
round 7, so the roster grows by two copies per round; gun plans bought for one round's roster do not
carry over to the next round's larger roster, while splashes add to S for every copy.

Revision (the accompanying artifacts, defaults equal to v12):
- splash_insurance: every speculative-insurance plan (the spec_share plan, the big-threat plan and the
  poke fallback) is made with splashes and walls only; the mandatory defence against the visible roster
  may still use guns. A splash-only plan that cannot reach zero leaks buys, with big_partial, the plan
  with the most adjacency within the budget, so the big-threat rule then spends on progress towards
  S >= 1500.
- fortress_n, fortress_k=3: splash_insurance holds from the first round in which the opponent's visible
  gold plus three rounds of its visible income (factories x 15 + its route length x 1) would buy at least
  fortress_n tier5, for the rest of the match.

Development evidence (single seat-0 games, the accompanying artifacts; deterministic, so not
independent samples): A reproduces its t2 results (+645, +535, -1065, +590 against the bluffs without
turret and with a gun in round 1, 2, 3). A + splash_insurance: +995, +845, +560, +995. A + fortress_n=4:
+1330, +925, +640, +1330. A + fortress_n=2: +995, +720, +640, +995. Trace of A + fortress_n=4 against
the round-2 bluff: the trigger fires in round 6 (bluff gold 760, 49 factories); seven splashes in each
of rounds 6 and 7 (S 360, then 790); 280 HP land in round 7 and 140 in round 8 (S 1090 plus a gun2 and a
gun3 from the mandatory defence); nothing lands from round 9 (S 1210 to 1300); our tier1 attacks
destroy the bluff, which never defends, in round 12 (380:-260).

A narrower option (the accompanying artifacts, v13 plus big_splash): only the big-threat plan (the plan
bought with up to all gold when the cheap insurance plan is unaffordable and the worst sampled roster
would deal at least big_threat damage) is made with splashes and walls only; the spec_share plan and the
poke fallback may still use guns. Its aim is to keep cheap gun insurance against mid-tier waves. Seat-0
games of A + big_splash: +995, +865, +960, +1010 against the four bluffs, and +72 against the guarded
round-8 tier4 schedule (A: +20).

Run recorded in the accompanying artifacts (66 matches; no errors, rejected actions, bot exceptions or source changes; slowest
decide 9.30 s under a machine load average above 100), pool TARGETED, both seats, HP difference (equal
in both seats in every pair):

| opponent | A (t2) | A + fortress_n=2 | A + fortress_n=4 | A + splash_insurance |
| --- | --- | --- | --- | --- |
| bluff without turret | +645 | +995 | +1330 | +995 |
| bluff, gun in round 1 / 2 / 3 | +535 / -1065 / +590 | +720 / +640 / +995 | +925 / +640 / +1330 | +845 / +560 / +995 |
| cheap guard + economy13 / + economy15 leak | 0 / 0 | 0 / 0 | 0 / 0 | -12 / -12 |
| guarded schedule, tier4 in round 5 / round 8 | +699 / +20 | 0 / +24 | -35 / +72 | -25 / +24 |
| economy13 / economy15 leak | -16 / -16 | -16 / -16 | -16 / -16 | -16 / -16 |
| fortress v21 | +5 | +5 | +5 | +5 |
| W-D-L | 12-4-6 | 12-6-4 | 12-4-6 | 12-0-10 |

Every splash-only setting beats all four bluffs, but the guarded round-5 schedule, which A beats by 699,
becomes a draw or a loss. Loss review (t4 logs 00037 and 00059, A + fortress_n=4 and =2 against that
schedule): the schedule keeps its gold (1677 in round 8, 13965 in round 12) and buys no turret after
round 8 until round 20, so the fortress trigger fires in round 6 or 7 and the splash-only big-threat plan
spends nearly all our gold on splashes. A single tier1 attack in round 8 deals 0 of its predicted 5, the
adaptive attack switches to the robust rule, and the robust rule assumes the opponent answers with all of
its visible gold, so no attack is bought from round 9 to round 20 although our map has S >= 1500 from
round 10 or 12 and the opponent never defends. A, without the trigger, keeps gold for attacks that land
(735:36, the accompanying artifacts, a seat-0 game outside the tournament).

Revision (the accompanying artifacts, v14 plus immune_attack): in a round in which our own map, after this
round's construction, has S at least the largest minion HP (1500), the attack step uses the current rule
(exact simulation against the opponent's current map, no response assumption) whatever attack_mode says.
Basis (proved, P1): such a map lets no copy of any type reach our base while it is unchanged, so gold has
no defensive use from then on; the rule changes only which attacks are bought, not our own HP. Seat-0
games (development, deterministic): A15 + fortress_n=2 + immune_attack beats the guarded round-5 schedule
+1038 (round 17), the round-8 schedule +1062 and the round-2 bluff +640; with fortress_n=4: +1267, +1092,
+640.

Run recorded in the accompanying artifacts (44 matches; no errors, rejected actions, bot exceptions or source changes; slowest
decide 11.86 s under the high machine load), pool TARGETED, both seats (v14, without immune_attack):

| opponent | A + big_splash | A + big_splash + fortress_n=4 |
| --- | --- | --- |
| bluff without turret | +995 | +995 |
| bluff, gun in round 1 / 2 / 3 | +865 / +960 / +1010 | +720 / +640 / +995 |
| cheap guard + economy13 / + economy15 leak | 0 / 0 | 0 / 0 |
| guarded schedule, tier4 in round 5 / round 8 | -50 / +72 | -50 / +72 |
| economy13 / economy15 leak | -16 / -16 | -16 / -16 |
| fortress v21 | +5 | +5 |
| W-D-L | 12-4-6 | 12-4-6 |

Run recorded in the accompanying artifacts (12 matches; clean; slowest decide 7.93 s), pool LATEST (the defence worker's fortress v22 and
the economy worker's econ17 with free_fallback "zero" and foreign_attack_from 11, the newest recommended worker
artifacts), both seats, with V2 = A15 + fortress_n=2 + immune_attack and V4 = A15 + fortress_n=4 +
immune_attack, where A15 is A on v15:

| opponent | best_v9a (frozen) | V2 | V4 |
| --- | --- | --- | --- |
| fortress v22 | 0 | -195 | +5 |
| econ17 | +5 | -16 | -16 |
| W-D-L | 2-2-0 | 0-0-4 | 2-0-2 |

Loss review of V2 against v22 (t6 log 00005): fortress_n=2 fires in round 5; the splash-only insurance
cannot stop the tier4 of round 7 and the tier5 of round 9 (60 + 140). V2 is dropped. The -16 against
econ13, econ15 and econ17 is the same in every C2-family setting (section 6, below-threshold waves):
t7 log 00017 (V2 against econ13) shows our three round-1 tier1 dealing 15 against their one dealing 5,
then a single tier3 bought in round 5 dealing 26 (769:785); both maps reach S >= 1500 by round 11 and
the difference is then frozen (P2).

Run recorded in the accompanying artifacts (88 matches; no errors, rejected actions, bot exceptions or source changes; slowest
decide 12.84 s under the machine load), pool TARGETED, both seats (HP difference equal in both seats in
every pair):

| opponent | A15 + immune_attack | V2 | V4 | VB = A15 + big_splash + immune_attack |
| --- | --- | --- | --- | --- |
| bluff without turret | +645 | +995 | +1330 | +995 |
| bluff, gun in round 1 / 2 / 3 | +535 / -1065 / +590 | +720 / +640 / +995 | +925 / +640 / +1330 | +865 / +960 / +1010 |
| cheap guard + economy13 / + economy15 leak | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |
| guarded schedule, tier4 in round 5 / round 8 | +939 / +956 | +1038 / +1062 | +1267 / +1092 | +751 / +1092 |
| economy13 / economy15 leak | -16 / -16 | -16 / -16 | -16 / -16 | -16 / -16 |
| fortress v21 | +5 | +5 | +5 | +5 |
| W-D-L | 12-4-6 | 14-4-4 | 14-4-4 | 14-4-4 |

immune_attack restores the guarded round-5 result (t4: -35 for fortress_n=4 without it, +1267 with
it). Without a fortress trigger or big_splash it does not help against the round-2 bluff (-1065, as A).
The remaining losses of V2, V4 and VB are the -16 against econ13 and econ15.

Loss review of the -16 (t7 log 00039, V4 against econ13; log 00017 for V2 is the same through round 5):
the worst sampled roster in round 5 deals less than big_threat (100) on our map, the full zero-leak plan
costs more than 0.6 of our gold, and the poke fallback ends in round 3, so nothing is bought and the
tier3 lands. Revision (the accompanying artifacts, v16 imported unmodified): mid_until, mid_hp (180),
mid_share. In rounds 2 to mid_until, under the poke fallback's opponent condition (poke_reactive), the
gold v15 would put into factories is used first for the zero-leak plan against the sampled rosters made
only of types with HP at most mid_hp (tier1 to tier3), within spec_share of it, if one of those rosters
would still leak; the rest goes into factories. By P1 a map with S >= 180 stops every tier1-tier3
roster, so a map reaching S >= 180 would stop every tier1-tier3 roster; the planner searches for an
affordable completion and may also choose guns (P1 does not by itself show that such a completion exists
around arbitrary permanent buildings). Seat-0 games (development) of V4 + foreign_policy "econ17" + mid_until=5: +10 against
econ13, econ15 leak and econ17 (V4: -16), +802 against the guarded round-5 schedule (V4: +1267), +495
against the round-2 bluff (V4: +640), +1330 against the bluff without turret, +902 against the guarded
round-8 schedule, +5 against fortress v21 and v22, 0 against the cheap guard with economy13.

Run recorded in the accompanying artifacts (pool FRONTIER5 plus the TARGETED counters not in it, 38 opponents,
both seats, 76 matches; no errors, rejected actions, bot exceptions or source changes; slowest decide 6.84 s)
for v17 = V4 + foreign_policy "econ17" + mid_until=5 (on the standard start the foreign switch cannot fire):
68-4-4. On the FRONTIER5 subset 56-2-4 with worst result -125 (C2 on c5d: 54-2-6, worst -45; best_v9a:
42-10-10, worst -160); on the TARGETED subset 18-4-0 with worst result 0 (V4 on t7: 14-4-4, worst -16;
best_v9a in the validation worker's targeted games, section 5.4: 6-2-14). The four losses are forecast_timing
(attack_round 8, tier5, all gold) at -125 and economy v4 late_round=6 phi=0 at -45 (the known C2 loss,
section 6), each in both seats; the four draws are the two cheap-guard counters at 0.

Loss review of the -125 (c8m log 00019): the fortress trigger fires in round 7 (the opponent's 1300 gold
plus three rounds of its income buy seven tier5). In round 8 the opponent spends all of its gold on two
tier5; our splash-only partial plan raises S from 400 to 910, below the tier5 HP (1500), and one copy
deals 140. S reaches 1500 in round 10 and nothing else lands, but the opponent's map is never breached
(785 at the end). The C2 settings, which have no fortress trigger, end +15 against this counter (c5d,
c6a), so this is a cost of the trigger; V4 on FRONTIER5 (c8a, running) separates it from mid_until. The
trigger is kept because it turns the round-2 bluff from -1065 into +640 (t7).

Still queued (the accompanying artifacts): c8a (FRONTIER5: V4, VB), the forecaster screen s14 (V4)
with the validation worker's persistent-model counter in the accompanying artifacts (the public_factory counter
builds a fresh model for each prediction and is therefore not exact against the stateful adaptive
attack; the validation worker, 07:06Z), and rr1/rr2 (fortress v22 and econ17 against TARGETED and LATEST).

### 5.8 Scripted openings: the master layout cannot be completed

the economy worker reported (the accompanying artifacts entry 8) that econ17 wins 107 of 108 scripted-opening conditions
(the validation worker's audit of the same suite by the engine winner label: 103W 4D 1L, the four draws being mutual
destructions with nonzero HP difference; the accompanying artifacts, 10:38Z) and
that best_v9a loses six of their seven scripted scenarios against it by 812 to 1075 HP. The scenarios
(the accompanying artifacts) play the first K rounds for both sides from a seeded script (random walls, a
turret, minions and factories); the bots are called in those rounds but their actions are discarded.

Development games (both seats, against econ17, the accompanying artifacts; deterministic, so each pair
is one result, not two samples), HP difference from our side:

| setting | mirror:1:2 | asym:3:2 | mirror:22:3 | asym:23:2 |
| --- | --- | --- | --- | --- |
| V4 | -980 / -980 | | | -1270 / -1390 |
| V4 + planner v22 | -980 / -980 | | | -1090 / -1250 |
| V4 + foreign_planner v22 | -840 / -840 | -1270 / -830 | -1120 / -1120 | -1270 / -1250 |
| The defence worker's fortress v22 (for comparison) | -780 / -780 | | | -1098 / -805 |

Loss review (kept log in the accompanying artifacts): the scripted walls
block the master layout's template, so our route stays at 26 to 46 cells; the splash-only plans after
the fortress trigger stall at S = 1140 (below P1's sufficient immunity threshold of 1500; the replay
shows the tier5 copies passing); the big-threat and
gun_cap rules leave nothing useful to buy against the huge sampled rosters; our economy reaches 107
factories against econ17's 255. econ17 holds its attacks until round 11 and then floods (eight tier5 in
round 12 deal 840). The defence worker's fortress v22, whose planner searches every legal cell on foreign maps,
loses in the same way, so the failure is not specific to the v7 planner.

Revision (the accompanying artifacts, v15 imported unmodified): foreign_policy "econ17". The bot records
every cell at which it asked to build; from the first round in which its own map holds a building at a
cell it never asked for, the rest of the match is played by a fresh instance of the economy worker's frozen econ17
(free_fallback "zero", foreign_attack_from 11). On the standard start the switch cannot fire (the engine
places a building only where the bot asked), so there v16 plays exactly as v15 with the same
parameters.

Run recorded in the accompanying artifacts (264 matches; no errors, rejected actions, bot exceptions or source changes; slowest
decide 11.35 s): pool scenx (SCEN plus econ17, 11 opponents), scenarios mirror:1:2, asym:3:2,
mirror:22:3 and asym:23:2, both seats, 88 conditions per candidate. W-D-L by engine winner:

| candidate | mirror:1:2 | asym:3:2 | mirror:22:3 | asym:23:2 | total |
| --- | --- | --- | --- | --- | --- |
| v16 (V4 parameters + foreign_policy "econ17") | 18-2-2 | 20-0-2 | 16-2-4 | 18-2-2 | 72-6-10 |
| V4 | 2-0-20 | 2-6-14 | 12-8-2 | 12-0-10 | 28-14-46 |
| best_v9a | 4-2-16 | 6-8-8 | 16-0-6 | 13-2-7 | 39-12-37 |

v16's ten losses: the defence worker's fortress v19 and v22 under mirror:22:3 (-1265, both seats, round 15; V4 wins
these four conditions by 614), economy15 leak under mirror:1:2 (-1150, both seats, round 17), under
asym:3:2 in seat 1 (-1040) and under asym:23:2 in seat 1 (-1175), eco6_t5 under asym:23:2 in seat 1
(-719 in round 11, the single loss the economy worker reported for econ17 in its scen18 set), and econ17 under
asym:3:2 in seat 0 (-2810; after the switch this is econ17 against itself, and the other seat wins by
the same amount). The six draws are econ17 under mirror:1:2, mirror:22:3 and asym:23:2 (both bases
destroyed in the same round). In the trace of the mirror:1:2 loss to economy15 leak (sc1 log 00017),
econ17's S stays at 500 with 14 splashes on a 32-cell route after round 8, and economy15's round-17
flood deals 1120; the scripted walls stand in the master layout's corridors (for example at (3,0), (4,2),
(7,5) and (5,6)), so the route stays at 23 to 33 cells, which caps S. The defence worker was then writing a layout
re-planner for such maps (the accompanying artifacts); a frozen copy is part of best_v9e's foreign-map policy (section
"Final bot").

### 5.9 Frozen candidate best_v9b

Decision (2026-10-31T09:11Z): freeze the V17 implementation in the accompanying artifacts with the V4 parameters plus
foreign_policy "econ17" and mid_until=5 (the full spec is the development specification in the final-bot tests in the accompanying artifacts). Evidence:
c8m (V17 68-4-4 on FRONTIER5 plus TARGETED, section 5.7) and sc1 (the econ17 switch 72-6-10 on scripted
openings, section 5.8). On the standard start the switch cannot fire, so there the frozen bot is V4
plus the mid-tier insurance of rounds 2-5.

Freeze: the candidate in the accompanying artifacts (one self-contained class, rules in its docstring; it
imports only frozen packages: the defence worker's defense v7 planner and, through econ17, defense v9, v11 and v15,
the economy worker's economy v17 and the harness gamekit) was frozen in the accompanying artifacts
(sha256 dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7, listed in
the accompanying artifacts) and installed as the delivered bot. best_v9a is also retained in the accompanying artifacts.

Checks (scripts and log in the accompanying artifacts):
- full-trajectory identity of the delivered bot in the accompanying artifacts and V17 on the standard start (the accompanying artifacts): 14 of 14
  pairings identical (7 opponents, both seats; econ13, three feature bluffs and guarded schedules,
  threat_defender, forecast_timing round 8 tier5, econ v4 late6);
- the same after scripted openings (the check in the accompanying artifacts, which uses the match harness and compares every recorded action event): 12 of 12 identical (econ17
  and econ15 leak under mirror:1:2, asym:23:2 and the standard start, both seats);
- the final-bot tests in the accompanying artifacts, 11 tests, all pass (new tests: the frozen bot reproduces the development specification for 8 rounds
  after both scripted openings and switches in round 2 on mirror:1:2; every line of the five
  checksum manifests of the imported frozen packages verifies), and the combat-model tests in the accompanying artifacts (2 tests) pass;
  the harness tests in the accompanying artifacts failed one test that still passed best_v3b's parameter kappa to the candidate factory
  (best_v9a and best_v9b reject unknown parameters); the test now passes mid_until=5 and all 4 pass;
- a smoke game against idle (the accompanying artifacts): best_v9b wins in round 8.

Independent validation (the validation worker, the accompanying artifacts, rendered
2026-10-31T09:40Z): reserved pool B, ten opponent profiles (defence type and count, growth rounds,
reinvestment share and roster) under three starts, both seats, 60 conditions. best_v9b won all 60:
20-0-0 on the standard start (final HP 800 for best_v9b in all 20, ending rounds 9-17), 20-0-0 after a
one-round factory prefix and 20-0-0 after an asymmetric splash prefix (lowest final HP 722). No bot
errors, rejected actions or source drift; every game was replayed on the unchanged engine; the 30
seat pairs have identical normalized trajectories, so these are 30 distinct observations, not 60.
Pool B uses the same opponent families and code as the development profiles (the validation worker's separation
audit checks only exact parameter overlap), so it tests generalisation to new parameters, not to new
kinds of opponent. Targeted counters against best_v9b were requested from the validation worker.

### 5.10 Cycle 9: insurance revisions, a catch-up attack, the foreign-map policy and round 1

Hypotheses, each from a recorded loss of best_v9b's twin V17 (development module in the accompanying artifacts,
which copies v15's decision method into `the base class` and changes it in two marked places, and adds
the catch-up attack after v17's decision):
- H9a (the validation worker's diagnosis, the accompanying artifacts, 09:21Z). Against budget_timing tier3 attack round 3 with
  budget fraction 0.5, V17 has 110 gold in round 3; the poke fallback buys a splash for 60 and the 50
  left cannot stop the tier3 (26 damage, 774:800). One gun2 at (9,5) for 80 stops every sampled
  composition of tier1-tier3 and the actual roster, but only a plan made before the poke purchase, with
  more than 0.6 of the gold, finds it. Option mid_joint (share): when the poke fallback is reached
  and the poke condition holds (which includes round <= poke_until, so in rounds 2 and 3), first try
  the zero-leak plan against the sampled compositions whose types have HP <= 180, with up to
  mid_joint of the gold.
- H9b (loss review of c8m log 00019, the accompanying artifacts on the saved observations). Against
  forecast_timing tier5 attack round 8, the fortress trigger fires in round 7 and makes the insurance
  splash-only; the splash plan (480 gold) still leaks 140 in round 7, while one gun3 (200 gold) stops
  every sampled composition. In round 8 no plan within the 532 gold stops two tier5. Option
  fortress_guns: when the splash-only big-threat plan still leaks and the planner finds a zero-leak plan
  with guns allowed within all the gold, buy that plan instead.
- H9c (the defence worker, the accompanying artifacts, 09:24Z: frozen fortress v25 beats econ17 by +1300 under mirror:1:2 and
  +1410 under mirror:22:3, both seats). best_v9b plays econ17 after a scripted opening, so it may lose
  to v25 there. Option foreign_target: play the defence worker's fortress v26 or the economy worker's econ19 after the switch
  instead of econ17.

Checks: v18 with mid_joint=0.0 (the inserted plan then has budget 0) submits the same actions as V17
in 8 of 8 full-trajectory pairings (budget_timing tier3 r3 0.5, econ17, feature_bluff r2,
forecast_timing r8 tier5; both seats; the accompanying artifacts).

Quick development games (both seats; the accompanying artifacts; V17's results from
c8m and t6 in brackets):

| Setting | Opponent | Seat 0 | Seat 1 |
| --- | --- | ---: | ---: |
| mid_joint=1.0 | budget_timing tier3 r3 0.5 | 0, r50 [-26] | 0, r50 [-26] |
| mid_joint=1.0 | budget_timing tier3 r3 0.25 | +260, r50 | +260, r50 |
| fortress_guns | forecast_timing tier5 r8 | +15, r50 [-125] | +15, r50 [-125] |
| fortress_guns | feature_bluff r2 | +495, r12 [+495] | +495, r12 [+495] |
| fortress_guns | fortress v22 | +5, r50 [+5 for V4] | +5, r50 [+5 for V4] |
| fortress_guns | guarded tier4 r8 | +902, r18 [+902] | +902, r18 [+902] |

These two losses are repaired in these games, but mid_joint=1.0 failed the next check (below).

- H9d (the validation worker's model-free counters against the actual best_v9b, section 6). guard_geometry with a gun1
  at (10,1) and one tier1 (or two tier1, or one tier2) in round 1 kills our round-1 tier1, lands 5-12
  HP, buys only factories in rounds 2-5 and locks; our first attack comes in round 6. Option catch_up:
  in rounds 2 to attack_from - 1 (5), while our HP is below the opponent's, run the attack rule with
  the current mode (exact simulation against the opponent's current map) on attack_share of the gold
  that would otherwise buy factories; these attacks do not count towards the adaptive mode's failure
  limit.

TARGETED2 baseline (t8a, V17 = best_v9b's twin, 24 opponents, both seats, standard start): 20-16-12.
The twelve losses are six seat pairs: budget_timing tier3 round 3 half budget -26, guard_geometry
[tier1] -5, [tier1, tier1] -10, [tier2] -12, guard_roster [tier1, tier1] -5 and [tier2] -7.

Attribution games (seat 0, standard start; the accompanying artifacts):

| Setting (on V17) | corner [] | corner [tier1] | econ17 | budget_timing tier3 r3 0.5 |
| --- | ---: | ---: | ---: | ---: |
| none (V17; t8a and the validation worker) | 0 | -5 | +10 | -26 |
| mid_joint=1.0 + fortress_guns + catch_up | -1120, r12 | -973, r13 | -270 | not run |
| catch_up | 0 | +7 | +10 | -26 |
| mid_joint=1.0 | -1120, r12 | -5 | -270 | 0 |
| fortress_guns | 0 | -5 | +10 | -26 |
| mid_joint=0.75 | 0 | -5 | +10 | 0 |

mid_joint=1.0 is rejected. Against the passive corner-gun opponent it spent 60 of 67 gold on a splash
in round 2 and 60 of 66 on two gun1 in round 3 (the opponent's visible gold allowed a tier3), so it
had 12 factories in round 10 against the opponent's 159; the opponent's five tier5 of round 11 then
met a map with S < 1500 (800 to -320 in two rounds). The joint plan's budget is the risk: a gun2 for 80
of 110 gold (share 0.73) repairs budget_timing, while the two cheap-threat purchases above needed
shares 0.90 and 0.91. mid_joint=0.75 separates these cases; it was chosen after seeing them and is
therefore checked on the regression pools rather than taken from these games. The combination
V18E = V17 + catch_up + fortress_guns + mid_joint=0.75 was then run on TARGETED2 (t8e).

t8e (V18E, TARGETED2, both seats): 22-20-6 against V17's 20-16-12. Changed conditions (both seats
alike): budget_timing tier3 r3 0.5 -26 to 0 (draw), guard_geometry [tier2] -12 to 0, guard_roster [tier2]
-7 to +5, but guard_geometry [tier1] -5 to -973 (round 13); [tier1, tier1] (-10) and guard_roster
[tier1, tier1] (-5) stay lost. Several wins became smaller (budget_timing tier3 r5 0.25 +1066 to +26).
Loss review of the -973 (log 00037): the joint plan bought two gun1 in round 2 and one in round 3, the
catch-up attack a tier2 in round 4 (+12, so V18E led 795 to 788); with 9 factories in rounds 5-9 against
the opponent's 24-89, the big-threat insurance took all our gold each round, our map reached S = 490 by
round 10, and the opponent, now behind, locked at round 10 and sent tier5 from round 11. V17 had 17
factories at round 5 in the same game. Neither option alone does this (attribution table above), so the
two early spending rules interact through the economy. A larger catch-up budget (catch_up_share=1.0,
seat 0, the accompanying artifacts) wins guard_roster [tier1, tier1] +7 and guard_geometry [tier1, tier1] +2 but
still loses guard_geometry [tier1] -961. V18E is rejected. Next candidates (TARGETED2 runs t8f, t8g):
V18F = V17 + fortress_guns + catch_up (no joint plan), V18F with catch_up_share=1.0, and V20L =
V18F + mid_joint=0.75 used only while our HP is at least the opponent's (the accompanying artifacts;
reason: by P2 a lock freezes the HP difference, so while behind the early gold is worth more as economy
and catch-up attacks, and while level or ahead the insurance keeps the result).

H9c, first test (fx1a; pool new_foreign = the defence worker's frozen fortress v25 and v26 and the economy worker's frozen econ19;
scripted openings mirror:1:2, asym:3:2, mirror:22:3 and asym:23:2; both seats; development pool, not
validation). V17, whose foreign-map policy is econ17, went 4-0-20; all 24 games ended with a destroyed base.

| Opponent | mirror:1:2 | asym:3:2 | mirror:22:3 | asym:23:2 |
| --- | --- | --- | --- | --- |
| fortress v25 | -1300 / -1300 | -2280 / -3395 | -1410 / -1410 | +945 / +1098 |
| fortress v26 | -1460 / -1460 | +1920 / -1580 | -855 / -855 | -1155 / +818 |
| econ19 | -1820 / -1820 | -1970 / -3350 | -840 / -840 | -21450 / -3070 |

(HP difference from V17's side, seat 0 / seat 1.) best_v9b therefore plays a weak policy on scripted-opening
maps against the newest teammate bots, although econ17 won 103 of the economy worker's 108 scripted-opening conditions
when it was frozen (4 draws, 1 loss by the engine winner label; section 5.8): those conditions did not contain these three bots. Other targets on the same 24
conditions (fx1b, the foreign_target implementation in the accompanying artifacts): econ19 14-4-6 (fortress v25 6-0-2 and v26
6-0-2, losing only mirror:1:2, -1020 and -1600; econ19 itself 2-4-2 with seat pairs that differ under
asym:3:2), fortress v26 8-6-10 (econ19 2-0-6). Running: the economy worker's econ20 with the layout re-planner and
the defence worker's fortress v27 (fx1d, the accompanying artifacts, which adds these two targets), then the
deterministic targets on the older foreign-map opponents (fx1c).

t8f and t8g (TARGETED2, 24 opponents, both seats, standard start; the accompanying artifacts; empirical):

| Candidate | W-D-L | Losses (both seats alike) | Slowest decision |
| --- | --- | --- | ---: |
| V17 (t8a) | 20-16-12 | six seat pairs, -5 to -26 (above) | |
| V18F = V17 + fortress_guns + catch_up | 24-20-4 | budget_timing tier3 r3 0.5 -26; guard_geometry [tier1, tier1] -10 | 3.33 s |
| V18F1 = V18F + catch_up_share=1.0 | 22-18-8 | guard_geometry [tier2] -1117 (r13), [tier1, tier1] -970 (r12); guard_roster [tier1, tier1] -420, [tier2] -137 | 1.28 s |
| V20L = V18F + mid_joint=0.75 while level (v20) | 24-22-2 | guard_geometry [tier1, tier1] -10 | 0.81 s |

No candidate had a rejected action or a bot error. V18F1 is rejected: the full catch-up budget repeats
V18E's economic collapse against the guards. V20L keeps V18F's guard repairs and also draws budget_timing
tier3 r3 0.5, so the joint plan restricted to level positions does what H9a intended on this pool.

H9c continued (fx1c, fx1d; the implementation in the accompanying artifacts adds the targets econ20 and fortress v27; scripted
openings mirror:1:2, asym:3:2, mirror:22:3, asym:23:2; both seats; development pools, not validation):

| Target after the switch | new_foreign (fortress v25, v26, econ19; 24 games) | old_foreign (48 games) |
| --- | --- | --- |
| econ17 (V17) | 4-0-20 | (section 5.8) |
| econ19 | 14-4-6 (fx1b) | 47-0-1 |
| econ20 | 18-0-6 | 46-0-2 |
| fortress v26 | 8-6-10 (fx1b) | not run |
| fortress v27 | 8-6-10 | not run |

econ20's losses: against econ19 mirror:1:2 -1260 (both seats), asym:3:2 seat 1 -970, asym:23:2 seat 1
-1810; against fortress v26 mirror:1:2 -55 (both seats); against econ17 asym:23:2 seat 1 -1110 and eco6_t5
asym:3:2 seat 1 -790. econ20 was chosen (64-0-8 over the 72 games, econ19 61-4-7) also because its planner has
a finite wall-clock deadline that no recorded call reached (the economy worker, the accompanying artifacts entry 13): its replanner
uses a fixed seed and its gun planner a one-million-second deadline, so in the recorded runs the actions are a
function of the observation sequence. V20T = V20L + foreign_target="econ20". On the standard start V20T and V20L play the same: the
switch needs a building on our map at a cell we never asked for, and the engine builds only on request
(this rests on the engine's construction rule, which the harness tests check, not on a separate proof).
The economy worker later recommended its econ21 (no eco6_t5 losses, the accompanying artifacts); V21E (the accompanying artifacts,
foreign_target="econ21") is queued on the same conditions (fx2).

c9h (V20T on f5t: FRONTIER5 plus the TARGETED counters not in it, 38 opponents, both seats, 76 games;
the accompanying artifacts; V17 = c8m on the same conditions): V20T 68-6-2 against V17 68-4-4; no rejected action,
no bot error, slowest decision 0.98 s. Changed outcomes (both seats alike): forecast_timing tier5 r8 -125 to
+15 and econ v4 late_round=6 phi=0 -45 to 0 (repairs), but feature_bluff turret_round=1 +595 (r12) to -980
(r9). Margins also shrank against passive growers: eco6_t5 and feature_bluff r0 +1330 to +810, feature_bluff r3
+480 to +245, guarded_schedule tier4 r5 +802 (r17) to +636 (r50) and r8 +902 (r18) to +588 (r50); fortress v7
went from +15 to +155.

Loss review of the -980 (c9h log 00059; the replay utility in the accompanying artifacts rebuilds every observation from the log and
replays a fresh V20T, which repeats the logged actions in every round). The bluff builds one gun1 at
(0,11) in round 1, off its own route, then factories, and sends tier5 from round 7. The off-route gun
satisfies poke_reactive="turret", so the joint plan ran: a splash in round 2 and two gun1 in round 3, then
gun1 purchases by the mid-tier rule in rounds 4-5 and a gun3 in round 6. Our factories stayed far behind
(the opponent had 71 by round 6) and the tier5 floods destroyed our base in round 9. V17, without the joint
plan, kept its economy and won +595. The opponent that the joint plan was added for (budget_timing tier3 r3
0.5) builds its turret on its own route. Revision H9e (the accompanying artifacts, mid_relevant=true; V23R =
V20T + mid_relevant): the joint plan runs only while the opponent owns a turret that covers its own route
(a splash next to a route cell or a gun in range of one) or its roster shows a tier1/tier2 bought in
round 2 or later. Tests d9a (the four bluffs, budget_timing tier3 r3 0.5, guard_geometry [tier1] and
[tier1, tier1]) and c9k (f5t) are queued; best_v9c (frozen twin of V20T, sha256 1a1b2c53...8ff5d) is held
until they finish.

Round 1 (H9f; the accompanying artifacts; exact round-1 simulations on the unchanged engine;
empirical over the listed opponents). Our round 1 buys 20 walls, three tier1 and one factory (85 of 100 gold)
and no turret, so every opponent poke in round 1 lands: 5 per tier1, 12 per tier2. This is the source of
the -5 to -15 "blind round 1" results of the defence worker and of the guard_geometry [tier1, tier1] -10 that no
cycle-9 option repairs (by P2 such a lead can be frozen by the opponent's lock). One gun1 at a middle cell
of row 1 or row 3, in place of a stage-A wall, covers the route twice and stops one to six tier1 and one
tier2 completely (two tier2 still deal 12, a tier3 26). With two tier1 the round-1 spend is 19 + 30 + 30 +
20 = 99 and still buys the one factory. Against the round-1 actions of the f5t, TARGETED2 and TARGETED3
opponents (both seats) the round-1 exchange moves from 1270 dealt and 748 taken to 800 dealt and 72 taken
(gun1 plus two tier1), or 1270 and 72 with three tier1 and no factory. V22G (the accompanying artifacts,
r1_gun=[4,1], two tier1) is queued on TARGETED2 (t9c), TARGETED3 (t9e) and f5t (c9j).

Results of H9e and H9f (empirical; development pools):
- d9a (the accompanying artifacts, V23R against the opponents on which the joint plan decided a result, both seats alike):
  feature_bluff turret_round 0 +810, 1 +595 (V20T -980), 2 +495, 3 +245; budget_timing tier3 r3 0.5 0;
  guard_geometry [tier1] +7, [tier1, tier1] -10.
- c9k (V23R on f5t, 76 games): 70-6-0, worst result 0 (draws only against the two guard continuations and
  econ v4 late6), against c9h's V20T 68-6-2 and c8m's V17 68-4-4. No rejected action or bot error.
- The validation worker's counter to H9e (the accompanying artifacts, 11:45Z; their harness, a private snapshot of v23): a gun1 at
  (0,2) can hit a copy at most twice (16 damage) and a gun1 at (9,11) covers one route cell (8 damage), so both
  cover the route and kill no copy of any type. Against these bluffs the filtered policy loses exactly as the
  unfiltered one, -320:660 at round 9 in both seats, while it beats the original off-route gun 520:-75.
  Refutation of H9e: route coverage is not evidence of a threat, and any turret condition that a 30-gold
  turret can satisfy opens the joint plan. best_v9d (frozen twin of V23R) was withdrawn before it was posted.
- Mechanism (traces of c9h log 00059 and d9a log 00003): with the joint plan, V20T bought a splash in round 2
  and gun1s in rounds 3-5 and had 12 factories at round 6, against 27 for V23R on the off-route bluff. The
  bluff, with 71 factories, sent tier5 from round 7; V20T took 140, 420 and 560 HP in rounds 7-9. Against an
  opponent that only grows and then floods, early gold spent on insurance against attacks that never come
  decides the match.
- c9j (V22G = V20T + r1_gun=[4,1] on f5t): 38-4-34. New losses: eco6_t5 and feature_bluff r0 -1125 (round 9),
  eco_then_flood switch=8 -845 (round 9), fortress v7 (three settings), v11, econ13 and econ15 -130, the
  annealed layouts and econ v4 late6 -50, best_v3b -4. H9f is rejected; the round-1 exchange gain does not
  survive the full game. That the 14 gold of round-1 economy and the third tier1 cause these losses is a
  conjecture; the logs have not been traced.
- Consequence: the joint plan is ablated. The next candidate is V18FT = V17 + fortress_guns + catch_up +
  foreign_target="econ20" (the accompanying artifacts; on the standard start V18FT plays as V18F of t8f), which
  gives up the budget_timing tier3 r3 0.5 repair (-26 comes back) and removes the bluff exposure. The frozen
  candidate in the accompanying artifacts (best_v9c with mid_joint off) has the same actions as V18FT in 12
  full-trajectory pairings (six opponents, both seats; the accompanying artifacts) and passes its 12 tests
  (the accompanying artifacts). Results for V18FT (empirical, both seats; 0 rejected actions, 0 bot errors):
  - b9a (eight feature_bluff settings: the two weak covering guns, round 2, growth_rounds 5 and 7, tier4, no
    turret): V17 16-0-0 and V18FT 16-0-0 (worst +495); V23R 12-0-4 (-980 against both weak covering guns); V24G
    4-0-12 (-730 to -1020), which confirms the rejection of r1_gun.
  - c9i (f5t, 76 games): 70-6-0, worst result 0, against c8m's V17 68-4-4.
  - t9h (TEAMMATES3, six GuardedForecast rosters modelling V18FT, fortress v32; 30 games): 16-2-12, worst -20.
    On the 16 games shared with t9b it is 12-0-4 against V17's 8-0-8; it beats fortress v32 in both seats. The
    forecasters, which model V18FT exactly, take 2 W, 2 D and 8 L from it with margins of 5 to 20 HP, the
    damage of the round-1 poke that their gun at (10,1) stops; the guarded adaptive continuation with one or
    two tier1 wins by 10 in both seats.
  - fx3 (scripted openings): stopped at 41 of 72 games to free a slot; 39-0-2, the two losses -55 against
    fortress v26 under mirror:1:2 (both seats). The stateful forecaster screen s19 was dropped for time.

### 5.11 Frozen best_v9e; passive growers and the rejected revision P5TNUBM

Freeze and promotion. The implementation in the accompanying artifacts (frozen 12:01Z) plays the same actions as its twin V18FT
in 32 standard-start games and 18 scenario games (the accompanying artifacts, all checks exit 0 at 13:06:08Z); its
12 tests and the 6 harness tests pass and the smoke command gives 800:-5 in round 8. Selection rule: V18FT scored at
least as well as best_v9b's twin V17 on every development pool on which both were run (f5t 70-6-0 against 68-4-4,
BLUFFCOV 16-0-0 against 16-0-0, the 16 shared TEAMMATES3 games 12-0-4 against 8-0-8) and better on two. It was
installed as the delivered bot in the accompanying artifacts at 13:07:59Z, with its tests installed as the final-bot tests in the accompanying artifacts. best_v9e has no
reserved-pool validation at that point; the request for pool C was deferred because the revision below was already
under test (pool C was run on best_v9e after the 16:12Z decision; end of this section).

Passive growers (the validation worker, the accompanying artifacts, 12:00Z-12:32Z; empirical). Their counters buy no turret, buy factories
through round 4 to 9 and then spend all gold on tier5 each round; roster_bait adds a round-2 bait (one to three
tier1 or one tier2), maze_grower grows behind a wall layout (empty, our 20-wall opening, or their 46-wall
cash_rank_1), guarded_maze adds one splash in round 3, 4 or 5, staged_guard_maze two or three splashes at fixed
rounds. economy21 and fortress33 beat most of them; V18FT and best_v9b lose most. Mechanism (my traces
in the accompanying artifacts, `rb2`, `rb3`): the bait makes the poke condition of rule 3 true, so it buys gun1, splash and gun2
in rounds 2-4, or the grower's gold makes the big-threat plan buy a gun3 in round 4; either way we own 12 to 18
factories at round 6 against the grower's 26 to 31, and its tier5 entries, which spawn every round, flood us from
round 7.

H9g (passive rule): through round passive_until, while the opponent owns no turret and its minions bought in round 2
or later cost at most passive_bait (40 gold), skip the speculative insurance of rule 3 (the mandatory defence of
rule 2 against visible types still runs); the gold goes to factories. Option poke_reactive="turret_only": the poke
fallback runs only while the opponent owns a turret, not because of a cheap minion bought from round 2.
Implementation: the candidate (best_v9e plus options, all off by default) and its fixed
copies are in the accompanying artifacts (sha256 cbe8dc5b...663bb62 for the first; the second adds passive_ratio and passive_defend). P5 = v24
passive_until=5; P5T = P5 + poke_reactive="turret_only"; P5TF = P5T + fail_limit=2.

Results (empirical, both seats, 0 rejected actions and 0 bot errors in every run; slowest decide 0.94 s in g9a):

| Run | Pool | V17 | V18FT | P5 | P5T | others |
| --- | --- | --- | --- | --- | --- | --- |
| g9a | GROWERS: 35 roster_bait + 36 maze_grower settings (142 games) | 66-0-76 | 66-0-76 | 138-0-4 | 142-0-0 (worst +555) | |
| q25 | ROSTER_BAIT (70 games) | | | | | R5, R5D, B100: 70-0-0 each |

- V17 and V18FT have identical results on every g9a row. P5's four losses are roster_bait with three round-2 tier1
  (45 gold, above the 40-gold limit) at growth 4 (-685) and 5 (-860), both seats; P5T wins them by +1160 and +675.
- The validation worker (the accompanying artifacts, 13:02Z, 13:05Z; development games): on 18 growth and bait-cost settings P5 is 30W-6L, with
  three or four tier1 baits (45 and 60 gold) still winning against it; passive_bait=60 and turret_only each give
  36W-0L with different trajectories. This refutes P5 as a general repair and supports P5T on that grid.
- The validation worker (13:05Z-13:14Z): P5 loses the empty-layout grower with splash guards in rounds 4 and 6 and growth through
  round 6 (520:755 at round 50, both seats), while it wins 22 of the 24 nearby staged-guard games. Mechanism
  (their proof55, confirmed on the original-engine history): the second guard stops our round-6 tier2 attack, the
  adaptive attack mode counts one failure and switches to the robust mode for the rest of the game, which never
  attacks again; we finish with 498036 unspent gold. The bait limit and turret_only do not change any action of
  that game (their proof54 and a 680-decision shadow check). In their six-game ablation fail_limit=2 and
  attack_mode="current" win all six games (heavy drip, this guard grower, forecast tier5 round 8), while
  fortress_guns=false trades the guard loss for a loss to forecast tier5 round 8.
- The defence worker (the accompanying artifacts, 13:10Z) reports that their analogous eco_match option wins the guard-growth class but
  loses to opponents that answer pokes and drip (econ17, economic timing policy), to an early-locking grower and to a
  round-7 tier4 forecaster. Whether P5T and P5TF share this trade-off is tested by f5t, TARGETED2 and TARGETED3.

GUARDED_MAZE and STAGED (gm2 final, st1 partial; empirical, both seats, at 13:34Z): on GUARDED_MAZE (144 games per
candidate) V18FT is 66-0-78 (worst -1340), P5T 138-0-6 (worst -815) and P5TF 138-0-6 with the same six
losses. All six are guarded_maze on the empty layout with the splash in round 3 and a round-2 bait (tier1 at growth
4 and 5: -815; tier2 at growth 6: -726), both seats. Trace (gm2 log 00159): rule 2 buys a gun1 in round 3 against
the bait; once the splash stands on the opponent's map the passive condition is false, rule 3 buys gun1 and gun2 in
rounds 4 and 5, and at round 6 we own 21 factories against the grower's 45. On STAGED (140 games per candidate)
V18FT is 114-0-26 and P5T 136-0-4; P5T's losses are the staged guard case of the validation worker above (empty layout, growth 6,
guards in rounds 4 and 6: -235; guards in rounds 4, 6 and 8: -95; both seats), which fail_limit=2 targets.

H9h (passive_turret): a turret is a defensive purchase and does not change what the opponent can send in the
current round, so the passive condition should ignore it. The revision in the accompanying artifacts (fixed copy of the candidate,
sha256 353ea07d...fff339) adds the option passive_turret (default true keeps v24's behaviour). P5TN = v26
passive_until=5, poke_reactive="turret_only", fail_limit=2, passive_turret=false; P5TNR = P5TN + passive_ratio=0.5
(the bait limit becomes the larger of 40 gold and half the value of the opponent's factories). Risk: an opponent
that builds turrets and factories and then strikes in rounds 3-6 now looks passive, so f5t, BLUFFCOV, TARGETED2 and
TARGETED3 decide.

H9i (robust_k; the validation worker, the accompanying artifacts, 13:26Z-13:32Z, their full games and replays on the unchanged engine):
screened_guard_maze (empty layout, growth through round 6, splash guards in rounds 4 and 6, two gun1 at (10,3) and
(10,4) in round 9) beats P5TF 520:755 in both seats. Our round-6 and round-9 attacks fall short, so after
fail_limit=2 failures the robust rule takes over; it replays only the best two tiers by the current-map ratio
against the estimated response, and tier5, which has a positive score after the response from round 20 (22 copies,
3080 predicted damage), ranks third and is never evaluated. On their 12-setting grid (growth 5-7, upgrade round
8-11) only growth 6 with upgrade round 9 beats P5TF (22W-2L); attack_mode="current" and fail_limit=3 win all 24.
The revision in the accompanying artifacts (sha256 1f0402bf...b8e83f) adds robust_k (default 2 keeps the old rule; null replays every
tier). P5TFU = v27 with P5TF's parameters and robust_k=null; P5TNU = P5TFU + passive_turret=false. A new
development pool SCREENED (defined in the accompanying artifacts: "screened", growth 4-8 by upgrade round 7-12, 30 settings) tests it. On SCREENED
(sg1, 60 games per candidate, both seats, empirical) P5TF is 58-0-2 (it loses only growth 6 with upgrade round 9,
-235 in both seats), P5TFU 60-0-0 (worst +649) and P5TNU 60-0-0 (worst +45); 0 rejected actions, 0 bot errors,
slowest decide 2.20 s. The validation worker's untruncated_response variant makes the same change on
v24.

H9j (behind_mode; trace of the validation worker's guard_handoff case, the accompanying artifacts):
guard_handoff (empty layout, factories only through round 6, two tier5 in each of rounds 7 and 8, then a frozen
fortress defender from round H) beats P5TFU and P5TNU for H = 10 to 13 (the validation worker, 13:39Z-13:53Z). In the H10 game the
opponent owns 86 factories against our 45 to 50 at round 6-7; its map has S 80 and no gun through round 8; one of
four tier5 copies passes our six-gun map in round 8 (660:755); our attacks in rounds 6 and 9 (one tier2, one tier3:
half of what rules 2-3 leave) fall short, and from round 10 the robust rule buys nothing. Hypothesis: while our HP is
lower, a policy that stops attacking keeps a losing comparison once both maps lock, so the adaptive mode should use
the current-map rule in those rounds. The revision in the accompanying artifacts (sha256 7d6da33a...ac266e) adds behind_mode (default
None keeps v27); P5TNUB = P5TNU + behind_mode="current". The validation worker (14:03Z, refuting for H10): always-current scoring
also loses H10 660:755; the current rule buys four tier3 in round 10 (104 predicted damage) and the handoff defender
stops them; from then on no tier has a positive current-map score.

Development pool HANDOFF (defined in the accompanying artifacts: "handoff", growth 5, 6, 7 x handoff 10, 11, 12, 13, 14, 16; 36 games per
candidate, run hd1; empirical): P5TNU 28-0-8, losing exactly growth 6 x handoff 10 to 13 (-95 each, both seats);
P5TNUB 34-0-2, losing only growth 6 x handoff 10 (-95, both seats) and winning handoff 11 (+9), 12 (+113) and 13
(+637). Both win every growth-5 and growth-7 setting by at least +45.

Further development results for the candidates (both seats, 0 rejected actions, 0 bot errors):

| Pool (run) | V18FT | P5TF | P5TN | P5TNU | P5TNUB |
| --- | ---: | ---: | ---: | ---: | ---: |
| STAGED (st1, st2; 140 games) | 114-0-26 | 140-0-0 | 140-0-0 | 140-0-0 | |
| SCREENED (sg1; 60 games) | | 58-0-2 | | 60-0-0 | |
| PUNISH (pu1; 34 games: the defence worker's defensive counters 33 and 28, guarded schedules of 200 tier3-tier5 from rounds 3-7) | 34-0-0 | 34-0-0 | 34-0-0 | 34-0-0 | |
| GROWERS (g9a, g9b; 142 games) | 66-0-76 | | | 142-0-0 | 142-0-0 |
| BLUFFCOV (b9a, b9b; 16 games) | 16-0-0 | | | 16-0-0 | 16-0-0 |
| HANDOFF (hd1; 36 games) | | | | 28-0-8 | 34-0-2 |

the defence worker (the accompanying artifacts x128) reports that their frozen fortress v34 and v35 also lose the H10 handoff (-653 and
-525).

The decision rule for the frozen best_v9f: among P5TNU and P5TNUB (P5TF and P5TFU as fallbacks), the candidate that
keeps f5t (no new loss against V18FT's 70-6-0), PUNISH, BLUFFCOV, TARGETED2 and TARGETED3 and wins the most of
GROWERS, GUARDED_MAZE, STAGED, SCREENED and HANDOFF; the smaller change when tied; best_v9e stays if none keeps f5t.
Regression of the passive family against round-5 strikers (runs c9n and t8h, both seats, empirical). On f5t
(38 opponents, 76 games) V18FT is 70-6-0 (c9i) and P5TNU 70-4-2: the new losses are the economy worker's economic timing policy (-90
in both seats). On TARGETED2 (24 settings, 48 games) P5TNU and P5TNUB are each 34-10-4; V18F (t8f; V18FT plays the
same on the standard start) is 24-20-4. The two losses V18F shares are budget_timing tier3 round 3 half budget (-26);
the new losses are budget_timing tier3 round 5 half budget (-52). Mechanism (seat-0 traces): both strikers buy
nothing visible until round 5, so in rounds 2-5 the passive rule (passive_until=5) skips rule 3 entirely, and the
round-5 wave meets a map that was built only against the round-1 bait. V18FT buys insurance against the visible
threat in rounds 2-5 and holds. Growers and timing strikers therefore pull in opposite directions: growers punish
early insurance (V18FT 66-0-76 on GROWERS) and timing strikers punish no insurance. By the decision rule above,
P5TNU and P5TNUB do not qualify.

Two repairs were then tested (development; results below and in the rest of this section):
- P4TNUB = v28 with P5TNUB's parameters and passive_until=4 (one round less of passivity).
- P5TNUBM = the implementation in the accompanying artifacts (v29 + option passive_mid_from, default None = v29) with P5TNUB's parameters and
  passive_mid_from=5: in passive rounds from round 5, rule 3a (insurance against the specified roster) runs against
  rosters made only of tier1-tier3, while rules 3b-3d stay off. Seat-0 quick games: economic timing policy W +75,
  budget_timing tier3 round 5 half budget D 0.
A new development pool TIMING (defined in the accompanying artifacts: "timing", the twelve budget_timing settings of TARGETED2, economic timing policy,
econ13, econ15 leak and econ17 with foreign_attack_from=11; 16 opponents, 32 games per candidate) checks the
strikers directly.

v29 (option strike_until: in rounds 6 to r, while the opponent has bought no minion costing more than 40 gold since
round 1, rule 4 runs before rule 3 on half the gold left after rule 2) was aimed at the growth 6 x handoff 10 loss.
The validation worker's predeclared early-guard campaign (the accompanying artifacts, 14:36Z-14:47Z; 72 games, both seats, replayed on the
unchanged engine) refutes it: on the empty H10 control P5TNUB loses 660:755, strike_until=6 520:729 and
strike_until=7 380:521. In the strike_until=6 game the bot buys eight tier2 against the visible one-splash map in
round 6; the opponent adds its second splash in the same round, all eight die, and two tier5 copies leak in round 7.
v29 is not a candidate. The validation worker also confirmed (14:30Z-14:37Z, 48 games) that an exact public forecast of P5TNUB at
the handoff (forecast_handoff, handoff 9 or 10) wins 660:755 against P5TNUB, P5TNU with always-current scoring and
P5TNU with fail_limit 3, while the same counter choosing its defence from the visible roster only loses all of those
games. The defence worker's frozen fortress v34, as the target, wins all eight of its games against both versions. This is a targeted, disclosed counter of the "exact
forecaster" class in section 6.

Results of the repairs (development, both seats, 0 rejected actions and 0 bot errors in every run; W-D-L by the engine
winner, worst HP difference in brackets; made with the table generator in the accompanying artifacts):

| Pool (runs) | V18FT | P5TNU | P4TNUB | P5TNUBM | M3 | M2 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GUARDED_MAZE (gm2, gm3; 144 games) | 66-0-78 (-1340) | | 144-0-0 (+378) | 144-0-0 (+268) | | |
| TIMING (tm1; 32 games) | | | 22-8-2 (-26) | 24-6-2 (-26) | | |
| TIMING2 (tm2; 40 games) | 0-34-6 (-26) | | 0-24-16 (-50) | 0-24-16 (-50) | | |
| GROWERS (g9a-g9d; 142 games) | 66-0-76 (-1955) | 142-0-0 (+555) | 134-0-8 (-660) | 142-0-0 (+368) | 142-0-0 (+368) | 142-0-0 (+368) |

TIMING2 (defined in the accompanying artifacts: "timing2", the validation worker's budget_timing with tier1 to tier4 and attack rounds 2 to 6, half budget; 20
settings) was added after tm2's first P4TNUB rows. V18FT loses tier1 and tier2 in round 2 (-20, -12) and tier3 in
round 3 (-26). P4TNUB and P5TNUBM lose the same three settings and five more, all strikes inside the passive window:
tier1 in rounds 3 and 4 (-30, -50), tier2 in rounds 3 and 4 (-24, -36) and tier3 in round 4 (-26). P4TNUB is out: on
GROWERS it loses 8 games by 660 in round 9 (maze_grower growth 6 and 7 and roster_bait with a tier1 bait), because
with the window ending at round 4 the round-5 big-threat insurance costs the factories again.

Three more rules aimed at the TIMING2 strikes failed (development):
- M3 and M2 = P5TNUBM with passive_mid_from 3 and 2 (the tier1-tier3 rule 3a in more passive rounds). Both keep
  GROWERS 142-0-0 (g9d). M2 still loses tier1 in rounds 3 and 4 (-30, -50; tm3, stopped after 10 M2 games) and loses
  the economy worker's economic timing policy -37 on f5t (c9p, both seats, stopped after 34 games), which V18FT and P5TNUBM do not lose.
  Trace of the round-3 tier1 game (tm3 log 00003): with 100 visible opponent gold the listed rosters include one
  tier3, one zero-leak plan against all tier1-tier3 rosters costs more than 0.6 of our gold, rule 3a buys nothing,
  and six tier1 deal 30. M3 was not run further.
- v31 (the accompanying artifacts, sha256 5246cee1...5fe3cce) adds passive_hp, the HP cap of those rosters. Seat-0
  quick games (the accompanying artifacts): M2 with passive_hp=560 (tier4 included) loses the validation worker's early-heavy counter
  (below) -15, with the counter's model retargeted to it and with the original P5TNUBM model, and loses
  economic timing policy -90; with passive_hp=1500 the early-heavy game is still lost -15. Conjectured mechanism (not traced):
  the larger roster list makes one zero-leak plan more expensive than the 0.6 share, so nothing is bought.
- v32 (the accompanying artifacts, sha256 ad97ea85...5f04a6d) adds passive_ladder: when the plan of the passive rule 3a
  does not fit the share, retry against the rosters made only of types with at most 70 HP, then 20 HP. Seat-0 quick
  games (the accompanying artifacts) for M2 with passive_ladder=[70,20]: draws budget_timing tier1 in rounds 2 to 4, tier2
  in rounds 3 and 4 and tier3 in round 4; loses tier3 in round 3 (-26, as V18FT), economic timing policy (-37), maze_grower
  (planner opening, growth 6, tier1 bait; -1105) and guarded_maze (planner opening, growth 5, guard round 5, tier2 bait;
  -1072).

So on these pools early insurance and growth against growers trade off directly: each rule that buys insurance in
rounds 2-4 against these strikes either loses growers or loses economic timing policy. P5TNUBM keeps GROWERS and GUARDED_MAZE
and loses five TIMING2 settings that V18FT draws (margins -24 to -50); V18FT loses 76 of 142 GROWERS games and 78 of
144 GUARDED_MAZE games (margins down to -1955).

The validation worker's counters to P5TNUBM (the accompanying artifacts, 15:01Z-15:19Z; full games replayed on the unchanged engine; these
are disclosed development counters, not pool C):
- nominee_handoff (forecast handoffs and a public-HP trigger): P5TNUBM 10-0-0, P4TNUB 4-0-6.
- early_heavy_handoff: a grower that buys one tier4 in round 5 and defends from round 6 or 7 with an exact public
  model of P5TNUBM wins 755:740 in both seats. P5TNUBM's round-5 plan is three splashes (S 190, below the tier4 HP
  560), so one tier4 deals 60, and our round-1 poke had dealt 45. With the handoff in round 8 or 9 the counter loses.
  A forecast that assumes half or all of P5TNUBM's public gold, without a policy model, keeps the win; a quarter does
  not. The validation worker's round5_heavy_defense finds a one-gun3 answer (200 gold) on that map, which is above rule 3a's share.
- nominee_counter_game: with P4TNUB, P5TNUBM, early1_handoff6 and their HP-trigger handoff handoff8, the results form
  the cycles P5TNUBM > handoff8 > early1_handoff6 > P5TNUBM and P4TNUB > early1_handoff6 > P5TNUBM > handoff8 > P4TNUB (all
  pairs identical in both seats). No policy of the four beats all three others; in that 4x4 win/loss table the
  mixture of one third each of P5TNUBM, early1_handoff6 and handoff8 has value 0 (their exact rational certificate).
The defence worker (the accompanying artifacts x140): P5TNUBM and P4TNUB beat all 8 of their round-5/6 strikers in both seats.

Gating of P5TNUBM (development, both seats, 0 rejected actions and 0 bot errors in every run; W-D-L by the engine
winner, worst HP difference in brackets; the accompanying artifacts; V18FT plays as best_v9e, V18F as V18FT on the standard
start):

| Pool (runs) | P5TNUBM | V18FT | V18F |
| --- | ---: | ---: | ---: |
| f5t (c9i, c9q; 76 games) | 68-8-0 (+0) | 70-6-0 (+0) | |
| TARGETED2 (t8f, t8i; 48 games) | 34-12-2 (-26) | | 24-20-4 (-26) |
| TARGETED3_P5TF (t9j, t9k; 30 games) | 20-4-6 (-10) | 18-2-10 (-12) | |
| PUNISH (pu1, pu2; 34 games) | 34-0-0 (+10) | 34-0-0 (+10) | |
| BLUFFCOV (b9a-b9c; 16 games) | 16-0-0 (+935) | 16-0-0 (+495) | |
| STAGED (st1-st3; 140 games) | 140-0-0 (+810) | 114-0-26 (-1200) | |
| SCREENED (sg2; 60 games) | 60-0-0 (+825) | | |
| HANDOFF (hd2; 36 games) | 36-0-0 (+45) | | |
| GROWERS (g9a-g9d; 142 games) | 142-0-0 (+368) | 66-0-76 (-1955) | |
| GUARDED_MAZE (gm2, gm3; 144 games) | 144-0-0 (+268) | 66-0-78 (-1340) | |
| TIMING (tm1; 32 games) | 24-6-2 (-26) | | |
| TIMING2 (tm2; 40 games) | 0-24-16 (-50) | 0-34-6 (-26) | |

- f5t: no new loss. The only differing games are the defence worker's fortress v11 (V18FT +15, P5TNUBM 0, both seats).
- TARGETED2: no new loss; the two losses are the shared budget_timing tier3 round 3 half budget (-26).
- TARGETED3_P5TF: one new loss in both seats, the defence worker's frozen fortress v32 (-7 at round 50), which V18FT wins (+5, t9h
  and t9k). V18FT instead loses six of the guarded_forecast games (-5 to -12) that P5TNUBM wins or draws; those
  counters forecast P5TF, the passive family's ancestor. Trace (t9j log 00029): v32 buys one tier2 in round 4,
  inside P5TNUBM's passive window (no insurance in rounds 2-4), and it deals 12; the round-1 pokes had left us 5 ahead,
  and both maps lock by round 11, so the -7 stands (P2). This is the TIMING2 mechanism, here from a teammate bot.
- Quick seat-0 games (the accompanying artifacts) of M4 and M3 (passive_mid_from 4 and 3): both win v32 (+5) but lose
  economic timing policy (-37), every TIMING2 strike that P5TNUBM loses, guarded_maze on the empty layout with growth 4 and a
  round-3 guard (-815), guard_ladder with growth 7 (-1075) and the early-heavy counter with its model retargeted (-15).
  Not candidates.

Decision (the rule above, applied as stated, with the precedent of P5TNU and P5TNUB, which were rejected for one new
TARGETED2 loss although their TARGETED2 score was higher): P5TNUBM has a new loss on TARGETED3, so it does not become
best_v9f, and best_v9e stays the installed bot (selection record in the accompanying artifacts at 16:12Z). The evidence is a trade-off, not a dominant
revision: P5TNUBM wins the grower family (GROWERS, GUARDED_MAZE, STAGED) that best_v9e loses in 180 of 426 games,
and loses small-margin early strikes that best_v9e holds (five TIMING2 settings, fortress v32; margins -7 to -50).
Which bot scores higher overall therefore depends on the weight given to each opponent family, and no pooled score
here is a neutral weighting.

The validation worker's later counters (the accompanying artifacts, 15:20Z-15:56Z; disclosed development counters, full games replayed on
the unchanged engine, both seats):
- guarded_round4_trigger: in round 4 one gun1 at (10,1) and one tier4 (290 of 291 gold); the gun stops our three
  persistent round-1 tier1 and the tier4 deals 60 on our map, then a public HP trigger hands off to a defender with a
  public-budget forecast. No model of our policy and no opponent-name lookup is used. It wins 755:740 against P4TNUB,
  P5TNUBM and best_v9e in both seats, and loses against the defence worker's F36 and F37, the economy worker's E25RM and E30 and their own
  handoff8 (the accompanying artifacts). So exact
  forecasting is not needed for this counter, and the counter does not transfer to the other targets.
- A fixed growth handoff without strike at round 8 (H8) wins 755:660 against P4TNUB and best_v9e and loses 755:800
  against P5TNUBM; at round 6 (H6) it loses against all three.
- A fixed public-budget forecast that beats P5TNUBM (early_heavy above) loses against P4TNUB, F36, F37, best_v9e and
  handoff8 (40 games).
- public_roster_selector chooses between the guarded round-4 strike and growth 6 with handoff 10 from the number of
  round-1 tier1 entries visible in round 2. On their eight development targets it scores 14-2-0 against 6-0-10 and
  12-2-2 for the two fixed branches; on twelve baseline archetypes it scores 16-6-2, below the fixed growth branch
  (18-6-0).
So every nominee and best_v9e has a disclosed counter that beats it, and each of these counters loses to other
targets; this is the counter-cycle pattern of section 6, not evidence for one dominant policy.

Independent validation of best_v9e on reserved pool C (the validation worker, the accompanying artifacts, 16:15Z-16:29Z;
the accompanying artifacts; empirical). The 72-condition manifest was
declared at 09:11:05Z; best_v9e (sha256 70ef8eab...) and, as a comparison that cannot be selected, P5TNUBM were
registered at 16:15:59Z, after my 16:12Z decision and before the first pool C game. Twelve opponent settings, three
starts, both seats:

| Start | best_v9e W-D-L (worst) | P5TNUBM W-D-L (worst) |
| --- | ---: | ---: |
| standard (normal start) | 18-6-0 (0) | 18-4-2 (-26) |
| mirror_7493_3 (prescribed 3-round history, policy calls skipped) | 24-0-0 (+719) | 24-0-0 (+719) |
| asym_8669_2 (prescribed 2-round history, policy calls skipped) | 24-0-0 (+526) | 24-0-0 (+526) |

All 72 games of each candidate were replayed on the original engine; there were no bot errors, rejected actions or
source changes. For best_v9e only, a further fresh-process audit regenerated all 1104 policy calls from the direct
`decide`, the default factory and the recorded specification, with identical legal actions and unchanged
observations. The validation worker's separation audit found no
exact parameter or prescribed-history overlap with earlier records for best_v9e and left 8 scenario inputs
unresolved; the opponents are held-out parameter settings of development families, not unseen families. Its
diversity audit found 33 distinct complete trajectories among best_v9e's 72 games (standard 12, mirror 11,
asymmetric 10): the 72 games are not 72 independent behaviours. So the installed bot lost no pool C game and the
rejected revision lost two standard games (one per seat, worst -26), the same direction as its development gate.
Largest best_v9e call 1.05 s.

### 5.12 Cycle 10: a capped round-3 purchase (V33C), frozen as best_v9f

H10a (stated in the candidate module's docstring at 16:22Z, before any of its games): P5TNUBM loses tier1
and tier2 strikes in rounds 3-4 (budget_timing, -24 to -50) and the defence worker's fortress v32 (one tier2 in round 4, -7)
because it buys no insurance in rounds 2-4, while M3 and M4 (the full rule 3a against tier1-tier3 from round 3 or 4)
lose the growers. A zero-leak plan against tier1-tier2 rosters only, capped at 60 gold (one splash) from round 3,
stops those strikes and costs the growers too little to change their result.

Implementation: the revision in the accompanying artifacts adds passive_cheap_from, passive_cheap_hp (70) and passive_cheap_cap (60); every new
branch is guarded by passive_cheap_from, so with it unset the bot is P5TNUBM (code inspection). V33C = P5TNUBM +
passive_cheap_from=3. Quick seat-0 probes (the accompanying artifacts, development): with (3, 60) fortress v32 +5,
economic timing policy +15, budget_timing tier1/tier2 in rounds 3/4 all 0 (P5TNUBM -24 to -50), tier3 round 4 -26, five
growers +253 to +770; passive_cheap_from=4 loses tier1 and tier2 in round 3; cap 30 finds no plan and plays as
P5TNUBM.

Gate (the rule of section 5.11, stated 14:49Z and unchanged; the V33C decision rule and its pool C fallback were
posted at 16:59Z, before its stage-2 results). Development, both seats, 0 rejected actions and 0 bot errors in
every run; W-D-L by the engine winner, worst HP difference in brackets; results in the accompanying artifacts. The best_v9e column
pools its twin V18FT (f5t, TARGETED3_P5TF, PUNISH, BLUFFCOV, STAGED, GROWERS, GUARDED_MAZE, TIMING2), V18F on
TARGETED2 (identical to V18FT on the standard start) and the frozen file itself (SCREENED, HANDOFF and TIMING:
runs bse_sg, bse_hd, bse_tm). STRIKE1 is the economy worker's set of 20 economic timing policy strikers (the accompanying artifacts, entry 17.8; their
runs in the accompanying artifacts (including strike1b) for best_v9e and P5TNUBM, mine x9fs1 for the frozen best_v9f).

| Pool (runs) | V33C | best_v9e | P5TNUBM |
| --- | ---: | ---: | ---: |
| f5t (x33f, c9i, c9q; 76 games) | 70-6-0 (+0) | 70-6-0 (+0) | 68-8-0 (+0) |
| TARGETED2 (x33t2, t8f, t8i; 48) | 24-20-4 (-26) | 24-20-4 (-26) | 34-12-2 (-26) |
| TARGETED3_P5TF (x33t3, t9j, t9k; 30) | 20-4-6 (-10) | 18-2-10 (-12) | 20-4-6 (-10) |
| PUNISH (x33pu, pu1, pu2; 34) | 34-0-0 (+10) | 34-0-0 (+10) | 34-0-0 (+10) |
| BLUFFCOV (x33b, b9a-b9c; 16) | 16-0-0 (+675) | 16-0-0 (+495) | 16-0-0 (+935) |
| STAGED (x33st, st1-st3; 140) | 140-0-0 (+405) | 114-0-26 (-1200) | 140-0-0 (+810) |
| SCREENED (x33sg, bse_sg, sg2; 60) | 60-0-0 (+569) | 50-0-10 (-235) | 60-0-0 (+825) |
| HANDOFF (x33hd, bse_hd, hd2; 36) | 18-0-18 (-375) | 12-0-24 (-235) | 36-0-0 (+45) |
| GROWERS (x33g, g9a-g9d; 142) | 130-0-12 (-835) | 66-0-76 (-1955) | 142-0-0 (+368) |
| GUARDED_MAZE (x33gm, gm2, gm3; 144) | 132-0-12 (-1095) | 66-0-78 (-1340) | 144-0-0 (+268) |
| TIMING (x33tm, bse_tm, tm1; 32) | 18-12-2 (-26) | 18-12-2 (-26) | 24-6-2 (-26) |
| TIMING2 (x33tm2, tm2; 40) | 0-32-8 (-26) | 0-34-6 (-26) | 0-24-16 (-50) |
| STRIKE1 (x9fs1; the accompanying artifacts, strike1b; 40) | 32-4-4 (-35) | 34-2-4 (-35) | 36-0-4 (-35) |

- Stage 1, game by game against best_v9e's twin (the accompanying artifacts): f5t, PUNISH and TARGETED2 have the same outcome
  in every condition; BLUFFCOV is 16 wins for both; on TARGETED3_P5TF V33C's six losses are among V18FT's ten and
  one win becomes a draw (guard_geometry with one tier1 at (9,1), +7 to 0, both seats). No new loss: stage 1 passes.
- Stage 2 (wins on GROWERS, GUARDED_MAZE, STAGED, SCREENED, HANDOFF, TIMING): V33C 498, best_v9e 326; V33C has at
  least as many wins on each of the six pools. Stage 2 passes, so by the pre-stated rule V33C replaces best_v9e.
- Not gates, reported as costs: TIMING2 budget_timing tier3 in round 4 for half its gold (-26, both seats; best_v9e
  draws). STRIKE1: the frozen file loses economic timing policy with all its gold in round 7 (-35, both repeat values, both
  seats; best_v9e and P5TNUBM +155) and draws the round-4 all-in that best_v9e and P5TNUBM lose (-35); the number of
  losses is the same as best_v9e's.
- Against P5TNUBM (the same planner without the round-3 step): V33C wins back fortress v32 (TARGETED3_P5TF) and
  turns eight TIMING2 losses into draws (budget_timing with tier1 or tier2 in round 3 or 4, -24 to -50 for
  P5TNUBM). It loses 12 GROWERS, 12 GUARDED_MAZE and 18 HANDOFF games that P5TNUBM wins, and two TARGETED2 games
  (guard_geometry with two tier1, -10; P5TNUBM +2), and draws budget_timing with all its gold (tier3 in round 3,
  tier4 in round 5 or 6; the same six games appear in TIMING and in TARGETED2) and guard_roster with two tier1, which
  P5TNUBM wins (by 1260 in round 11 and by 7). best_v9e draws the six budget_timing games as well.

Traces of the new costs (logs kept for losses):
- Growers (x33g log 00003, roster_bait growth 4 with one round-2 tier1; 00081, maze_grower growth 6 on the empty
  map): rounds 1-2 are as for P5TNUBM; in round 3 the step buys one splash (rule 2 adds one gun1 against the visible
  tier1); in round 5 rule 3a buys a gun1 and a gun2. We own 23 factories at round 5 against 31 (roster_bait) or 55
  (maze_grower); the tier5 entries hit for 140 per copy from round 6 or 7 while our map is below S >= 1500, and the
  game ends at round 9 or 10 (-820, -830).
- HANDOFF (x33hd; guard_handoff with growth 5, 6 or 7 and a handoff to a defender in round 10, 11, 12, 13, 14 or
  16): V33C loses every handoff in rounds 10 to 12 (18 games, by 27 to 375 at round 50) and wins those in rounds 13
  to 16. best_v9e loses 24 of the 36 (bse_hd), P5TNUBM none (hd2).
- STRIKE1 round 7 (x9fs1 log 00025): rounds 1-5 buy one splash in round 3 and two in round 5 (S 190); in rounds 6
  and 7 the bot buys two gun1 and two gun3 each round and S is 190 and then 140; the striker's two tier5 of round 7
  deal 140 in round 8; from round 9 both maps stop everything and the match ends 660:695 (P2).

Freeze and promotion. The freeze script in the accompanying artifacts wrote a frozen copy with V33C's values as defaults
(sha256 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580,
recorded in the accompanying artifacts). The freeze checks (log in the accompanying artifacts,
17:46Z-18:18Z): hash check exit 0; `same_actions` (the frozen file and the v33 spec submit identical action lists in
every round of full games against 28 opponents, both seats: 56 pairings) exit 0; `same_actions_scen` (18 pairings on
the scripted openings mirror:1:2, asym:23:2 and the standard start) exit 0; harness tests exit 0; smoke exit 0; the
bot's own tests exit 1, with 3 of 18 failing. The three were option-exercise tests (does passive_until, robust_k or
behind_mode change the bot's actions in some scenario?) whose scenarios had been written for P5TNUBM; with the round-3
step those scenarios no longer reach the options. A search (script and output in the accompanying artifacts) found that behind_mode changes the frozen bot's actions in seat 0 only against budget_timing
with tier2 in round 2 or tier3 in round 3 or 4 (first change in round 11, 14 or 12), and that robust_k=2 changes
nothing against any of the 18 HANDOFF, 30 SCREENED and 20 TIMING2 opponents searched (seat 0, first 22 rounds;
V33C wins every SCREENED game in seat 0 by round 13, before its robust rule runs). The tests now use: the baited grower, where the passive rule without its cheap and
mid steps buys 39 factories by round 6 and the bot without the rule 26; budget_timing tier2 in round 2, where the bot
is behind 788:800 from round 3, its attacks of rounds 7 and 8 fall short and only with behind_mode does it buy tier5
in rounds 11 and 12; and, for robust_k, the robust rule from round 1 (attack_mode="robust") against the guarded
grower, where every tier attacks from round 14 and wins in round 15 and the best two do not. So robust_k is live code
that the tested opponents do not reach with the default attack mode (empirical, for those pools). The revised tests
passed 18 of 18 on the frozen copy, and the frozen file was installed unchanged as the delivered bot in the accompanying artifacts at 18:37:45Z,
together with the revised final-bot tests (18 tests OK in 101 s, the accompanying artifacts; smoke result in
the accompanying artifacts, 8 rounds, 800 / -5). The docstring's sentence on the known cost is
narrower than what was observed: it names growers with growth 5 or 6 behind a round-2 tier1 bait, but the 24 losses
also include roster_bait with growth 4 and one game with a tier2 bait, and the ablation af3g (section 5.14) shows
the losses need the round-5 mid step as well as the round-3 step. The file was not edited after freezing because
the validation worker's pool C pipeline was pinned to its hash; section 6 gives the observed cost.

Held-out check and fallback. The validation worker ran the installed best_v9f on reserved pool C with the manifest unchanged
(the accompanying artifacts, rendered 18:43:26Z: 72 conditions, complete replays on the
original engine, no bot errors, rejected actions or source drift; the 36 seat pairs have identical trajectories).
Pool C has 12 opponents: four parameterised profile bots (growth of 1 to 9 rounds behind two to four turrets, then
mixed rosters), four pool archetypes (random_legal, mirror, stacker, turtle), two budget_timing strikers and two
guard_geometry guards, each on the standard start and after two prescribed openings, both seats.

| Start | best_v9f (rendered 18:43Z) | best_v9e (rendered 16:22Z) |
| --- | ---: | ---: |
| standard | 16-4-4 | 18-6-0 |
| mirror_7493_3 (prescribed 3-round history) | 24-0-0 | 24-0-0 |
| asym_8669_2 (prescribed 2-round history) | 24-0-0 | 24-0-0 |

The two differences, both seats each: C-08 (budget_timing, tier3 in round 4 with 0.65 of its gold): best_v9e draws
800:800, best_v9f loses 774:800; C-11 (guard_geometry, one tier2 and a gun at (10,2)): best_v9e wins 788:783,
best_v9f loses 788:790. The other ten standard conditions have the same outcome for both. By the rule posted at
16:59Z (before best_v9f's stage-2 results and before this run), a pool C condition lost by best_v9f that best_v9e
wins or draws reinstates best_v9e: the delivered bot in the accompanying artifacts was set back to frozen best_v9e at
2026-10-31T18:44:53Z with its own test file (12 tests OK in 37 s, the accompanying artifacts; smoke result in
the accompanying artifacts, 8 rounds, 800 / -5). Pool C was therefore used to choose between
best_v9e and best_v9f, and it is selection evidence, not held-out evidence, for both. The reinstall was a process
error on my side: the validation worker's fresh-process entry-point audit of best_v9f was still running. The 72 games and their
replays had finished at 18:43:04Z; of the entry audits 18 passed, one saw the change while running and 53 rejected
the new source hash (the accompanying artifacts, 18:45Z; receipt
the accompanying artifacts). The validation worker kept the
failure records and verified the archived best_v9f bytes separately: that verification finished at 18:52:19Z,
and all 72 archived-source entry checks pass, covering 1088 actual policy calls and 120 prescribed prefix turns
(the accompanying artifacts). It does not
make the installed file best_v9f. The delivered bot in the accompanying artifacts has not been changed since
18:44:53Z. Under the R13 rule posted at 19:04Z (section 5.14) the file could have changed once more, at the final
selection record in the accompanying artifacts; that note (19:50Z) kept best_v9e, so the hash above is the one pool D uses.

What this shows (empirical, within these pools): C-08 is the family of best_v9f's known development cost (TIMING2:
budget_timing tier3 in round 4 for half its gold, -26, best_v9e draws). The development gate traded that cost for
grower wins (172 more stage-2 wins); the pool C rule counts any lost condition, and pool C holds two early strikers
but none of the growers that beat best_v9e in development (factories only behind a bait or no turret, tier5 from
round 6 or 7): its growers (C-02 with growth 9 behind four splash, C-06 stacker with growth 9) are beaten by both
bots. So pool C can only show the cost side of that trade. Neither bot dominates the other in the
tested scope: best_v9e is better against early tier3 strikes and the single-tier2 guard; best_v9f is better against
baited passive growers (GROWERS 130 vs 66 wins, GUARDED_MAZE 132 vs 66, STAGED 140 vs 114, SCREENED 60 vs 50,
HANDOFF 18 vs 12 of 36). The choice between best_v9e and best_v9f followed the pre-stated pool C rule, not a
claim that best_v9e is stronger overall; the separate R13 choice between best_v9e and af2g is in section 5.14.

### 5.13 Cycle 11: best_v9f without the round-5 mid step (V33M), rejected

H11 (rule posted at 18:29Z, before its runs): the ablation af3g (section 5.14) showed that best_v9f without the
round-5 mid step (`passive_mid_from=null`) wins all 142 GROWERS (worst +385; best_v9f 130-0-12), so the grower losses
need both the round-3 step and the round-5 step. V33M = best_v9f with `passive_mid_from=null` might keep the protection of the round-3 step against small early strikes and recover the
growers. Because its GROWERS result was already known, the rule asked for no new loss against V33C game by game on
f5t, TARGETED2, TARGETED3_P5TF, PUNISH and BLUFFCOV, then at least V33C's 368 wins on GUARDED_MAZE, STAGED, SCREENED,
HANDOFF and TIMING and more than its 498 including GROWERS.

Result: on f5t (run `xm_f`) V33M loses the economy worker's economic timing policy (factories through round 4, tier1 in round 5) by
37 in both seats, where V33C wins both by 15. That is a new stage-1 loss, so V33M was rejected at 18:41Z; its other
gate runs were cancelled and xm_f was stopped at 56 of 76 games. On the 56 conditions shared with x33f, V33M is
48-2-6 and V33C 54-2-0: V33M also loses the economy worker's frozen econ13 and econ15 by 16 (V33C +10), both seats, and every
other condition has the same outcome (the accompanying artifacts). The economic timing policy loss is the one M2 showed (section 5.11): without a turret step in round 5 the
round-5 tier1 purchase gets through. This is direct evidence for the reason
the round-5 mid step was added (a round-5 tier1 or tier3 purchase with no turret in place), and it adds a third
member to the trade-off of section 5.12: without the mid step the growers are won and the round-5 strike is lost.

### 5.14 Cycle 12: af2g under rule R13 (rejected); ablations of the final bot and of best_v9f

#### R13: af2g against best_v9e (H13, rule stated at 19:04Z before the gate games)

af2g = best_v9f with `passive_until=null`: best_v9e plus four option values of
best_v9f (poke_reactive="turret_only", fail_limit=2, robust_k=null, behind_mode="current"; best_v9f's passive_turret,
passive_mid_from and passive_cheap_from act only through the passive rule, which is off). H13: with the passive rule
off it keeps every early strike that best_v9e holds and most of best_v9f's grower gain. Rule R13: af2g replaces
best_v9e only if on every condition of the 14 pools below its outcome is at least best_v9e's (W > D > L), with at
least one more win, 0 rejected actions, 0 bot errors and no decide call of 3 s or more, all by 22:00Z. The base runs
are best_v9e's own runs or its twin V18FT (v19 with the development parameters, same actions as best_v9e, section 5.11); differences
counted condition by condition with the accompanying artifacts.

| Pool (conditions) | best_v9e (base run) | af2g (run) | Conditions that change |
| --- | ---: | ---: | --- |
| PCS: pool C's C-08 to C-11, standard start (8) | 2-6-0 (g13pc, same run) | 2-6-0 (g13pc) | none |
| TIMING (32) | 18-12-2 (bse_tm) | 18-12-2 (g13tm) | none |
| TIMING2 (40) | 0-34-6 (tm2, twin) | 0-34-6 (g13tm2) | none; the same HP in all 40 |
| STRIKE1 (40) | 34-2-4 (the economy worker's run in the accompanying artifacts) | 34-2-4 (g13s1) | none |
| TARGETED2 (48) | 24-20-4 (t8f, twin) | 24-20-4 (g13t2) | none |
| f5t (76) | 70-6-0 (ab1) | 70-6-0 (g13f) | none |
| PUNISH (34) | 34-0-0 (pu1, twin) | 34-0-0 (g13pu) | none |
| BLUFFCOV (16) | 16-0-0 (b9a, twin) | 16-0-0 (g13b) | none |
| TARGETED3_P5TF (30) | 18-2-10 (t9k, twin) | 20-2-8 (g13t3) | 2 losses become wins |
| HANDOFF (36) | 12-0-24 (bse_hd) | 24-0-12 (g13hd) | 12 losses become wins |
| SCREENED (60) | 50-0-10 (bse_sg) | 60-0-0 (g13sg) | 10 losses become wins |
| GROWERS (142) | 66-0-76 (g9a, twin) | 128-0-14 (af2g) | 62 losses become wins |
| GUARDED_MAZE (144) | 66-0-78 (gm2, twin) | 126-0-18 (g13gm) | 62 losses become wins; 2 wins become losses |
| STAGED (140) | 114-0-26 (st1, twin) | 118-0-22 (g13st) | 4 losses become wins, none worse |

The 14 pools hold 846 pool memberships, not 846 distinct conditions: 34 (opponent, seat) keys occur in two or
three pools, so the pools cover 804 distinct conditions (402 opponents in both seats, all on the standard start), and
best_v9e's base runs give the same outcome on every repeated key (the validation worker's audit
the accompanying artifacts, 22:16Z; I recounted it with the accompanying artifacts and got the
same numbers). Totals over "846 conditions" in this report are sums over pool memberships.

The two GUARDED_MAZE conditions are one opponent in both seats,
`guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000`
(a tier1 bait in round 2, growth_rounds=4, guard_round=3, tier5 attacks; the GUARDED opponent of the accompanying artifacts):
af2g loses by 815 HP at
round 9, best_v9e wins by 305 at round 14. The run gmchk replays the condition with the frozen best_v9e file itself
(hash 70ef8eab...) in the same run as af2g and gives the same two results. Condition 1 of R13 fails, so best_v9e
stays (decision and note to the validation worker at 19:50Z). The two predictions of H13 hold on the tested pools: af2g has
best_v9e's outcome on every condition of the strike pools (PCS, TIMING, TIMING2, STRIKE1, TARGETED2, f5t, PUNISH,
BLUFFCOV), and most of best_v9f's measured grower gain remains (GROWERS 128 wins against best_v9f's 130; this
GROWERS result was known when H13 and R13 were posted, so it is prior evidence, not a prospective prediction). af2g
nevertheless fails R13, which is a stronger conjunction than H13: it loses one guarded-maze opponent that best_v9e
beats, in both seats, and its largest observed call exceeds three seconds (next paragraph). Empirical, within these
pools.

Condition 2 of R13 fails as well: af2g's largest decide call is 5.81 s (g13t3, guarded_adaptive_continuation with
two tier1, seat 1; 2.99 s in g13pu, at most 1.45 s in the other gate runs). Wall-clock times depend on the load of
the two shared cores; best_v9e's twin reached 3.32 s in t9k on the same pool (guarded_adaptive_continuation with one
tier1, seat 0). af2g had 0 rejected actions and 0 bot errors in all 14 gate runs (846 games); its largest call on STAGED (g13st) was 0.82 s.

#### Ablations of the final bot and of best_v9f

Development pools, both seats, the unchanged engine, 0 rejected actions and 0 bot errors in every run; single-option
and combined ablations of the frozen policy (the other values as installed); outcomes by the engine winner, worst HP
difference in brackets; differences counted condition by condition against the unablated run using
the accompanying artifacts. f5t is the 38-opponent regression pool of section 5.11 (76 games); GROWERS is the 71-opponent
pool of section 5.11 (142 games). Empirical, within these pools.

best_v9e (base: ab1 = c9i, f5t 70-6-0; GROWERS: its twin V18FT in g9a, 66-0-76):

| Run | Option changed | Pool | W-D-L (worst) | Conditions that change against the base (both seats unless stated) |
| --- | --- | --- | ---: | --- |
| ab2 | r1_poke=0 (no tier1 in round 1) | f5t | 40-32-4 (-5) | 30 wins become draws (15 opponents, among them fortress v7, v11, v19-v21, econ4, econ8-econ10, economic timing policy; margins +5 to +75), 2 opponents lost (poke_lock -5, known_policy timing against fortress_v4 -2), 2 draws won (guard_continuation, opening_response, +7) |
| ab3 (partial: first 20 of 76 conditions) | spec_share=0&big_threat=null&poke_insurance=false&mid_until=null (no insurance, rule 3 off) | f5t | 6-0-14 (-2675) | 12 wins and 2 draws become losses, 7 of the 10 opponents in both seats: econ v4 late_round=6 phi=0 (-2675, the 2 draws), fortress v7 with attack_from=6 (-1129), best_v3b (-953), fortress v7 annealed25 (-798), v4proto fortress_poke (-249), forecast_timing tier5 round 8 (-125) and economic timing policy (-90); the base wins 18 and draws 2 of these 20. Stopped at 20:22Z: game 21 (the known_policy fortress_v4 forecaster) had not finished after about 9 minutes, where the base game takes 15.5 s |
| ab4 | big_partial=false (no least-leak plan in rule 3b when zero leaks are unaffordable) | f5t | 66-6-4 (-540) | feature_bluff turret_round=3: +245 at round 13 becomes -540 at round 9; guarded_schedule with a tier1 in round 1 and a tier4 in round 8: +748 at round 16 becomes -96 at round 50; 6 other opponents (feature_bluff turret_round 0, 1 and 2, pool eco6_t5, eco_then_flood switch 8 and switch 12 with tier4) keep their outcome with a different margin |
| ab5 | fortress_n=null (rule 3 never switches to splash-and-wall-only plans) | f5t | 66-6-4 (-845) | feature_bluff turret_round=2: +495 at round 12 becomes -845 at round 9; turret_round=3: +245 at round 13 becomes -755 at round 9; 8 other opponents (feature_bluff turret_round 0 and 1, guarded_schedule with a tier4 in round 5 or 8, pools eco6_t5 and mixed5, fortress v7 and v11 with layout annealed25) keep their outcome with a different margin |
| ab12 | big_threat=null (no all-gold insurance, rule 3b) | f5t | 44-6-26 (-270) | 13 opponents won by the base at round 50 by 5 to 75 are lost at round 50: econ13, econ15 and econ15 with free_fallback "leak" (-270 each; base +10), v4 (-255), v4proto fortress_poke (-135), econ8 (-133), fortress v11 and falsification_fallback fortress13 (-125; base +15), economic timing policy (-90), fortress v7 and v11 with layout annealed25 (-65; base +75), fortress v15 and v19 (-55); in these 26 games the damage taken rises from 0-10 to 70-285, and in 14 of them best_v9e builds one or two gun3 fewer; 12 other opponents (feature_bluff turret_round 0 to 3, forecast_timing tier5 round 8, guarded_schedule with a tier4 in round 5 or 8, pools eco6_t5 and mixed5, fortress v7, eco_then_flood switch 8 and switch 12 with tier4) keep their outcome with a different margin |
| ab6 | attack_mode="current" (rule 4's first rule for the whole match: no switch to the robust rule after an attack falls short) | f5t | 70-6-0 (+0) | none; 6 conditions (guarded_schedule with a tier4 in round 5 or 8, best_v3b) keep their outcome with a different margin |
| ab7 | immune_attack=false | f5t | 66-6-4 (-36) | guarded_schedule with a tier4 purchase in round 5 or 8: +2194 and +748 become -36 |
| ab8 | mid_until=null (no mid-tier insurance) | f5t | 64-6-6 (-16) | econ13, econ15 and econ15 with free_fallback "leak": +10 becomes -16 |
| ab9 | poke_insurance=false | f5t | 68-8-0 (+0) | fortress v11: +15 becomes a draw |
| ab10 | catch_up=false (no rounds 2-5 attack while behind in HP) | f5t | 70-4-2 (-45) | econ v4 late_round=6 phi=0: a draw becomes -45 at round 50; 6 conditions (guarded_schedule with a tier4 in round 5 or 8, best_v3b) keep their outcome with a different margin |
| ab11 | fortress_guns=false (rule 3b keeps the leaking splash-only plan) | f5t | 68-6-2 (-125) | forecast_timing tier5 round 8: +15 becomes -125 (the loss that H9b traced and fortress_guns repaired in cycle 9, section 5.10); 22 other conditions keep their outcome with a different margin |
| ab14 | spec_share=0&big_threat=null&poke_insurance=false&mid_until=null (as ab3) | GROWERS | 142-0-0 (+200) | all 76 losses become wins; the 66 wins stay wins |
| ab15 | big_threat=null (no all-gold insurance, rule 3b) | GROWERS | 88-30-24 (-735) | 32 losses become wins, 20 losses become draws, 10 wins become draws (five opponents in both seats: maze_grower empty and the planner opening layout with growth 7 and a tier2 bait, and three roster_bait growers; for empty, a round-13 win with HP difference +528 becomes a round-9 draw with both bases destroyed and HP difference -97; the validation worker's audit, the accompanying artifacts); no win becomes a loss; all 30 draws destroy both bases |
| ab16 | poke_insurance=false | GROWERS | 128-0-14 (-1240) | 62 losses become wins, none worse; the same outcome as af2g on all 142 (8 differ in HP only) |
| ab17 | mid_until=null | GROWERS | 104-0-38 (-1240) | 38 losses become wins, none worse |

Slowest call in ab14-ab17: 0.46 s. On GROWERS each of the three insurance options (rule 3b, the poke insurance, the
mid-tier insurance) costs games against some growers; disabling all insurance in ab14 turns all 76 losses into wins; on f5t ab3, ab8
and ab9 show what they protect (ab3: 12 wins and 2 draws of 20 become losses), and rule 3b alone protects 26 f5t
games (ab12). The f5t ablations ab4 (big_partial=false), ab5 (fortress_n=null), ab6 (attack_mode="current"), ab10
(catch_up=false), ab11 (fortress_guns=false) and ab12 (big_threat=null) were dropped by the queue scripts in the accompanying artifacts at about 21:28Z
to free the slots for the final round robins; separate queue scripts in the accompanying artifacts ran ab6, ab10 and ab11 and then ab4, ab5 and
ab12 on f5t after the round robins (rows above; tsc also ran attack_mode="current" on TIMING2). best_v9f's af9, af10
and af8 (below) change the same three options as ab4, ab5 and ab12 on f5t: in best_v9f big_partial=false and
fortress_n=null change no f5t outcome (70-6-0), while in best_v9e each loses two feature_bluff or guarded_schedule
opponents in both seats; big_threat=null gives 42-14-20 in best_v9f and 44-6-26 in best_v9e. Of the ten options
changed alone on f5t (ab2 and ab4-ab12 without ab3), only attack_mode="current" (ab6) changes no outcome there.
Slowest call in ab4-ab6 and ab10-ab12: 1.60 s (ab5; ab4 1.35 s, ab12 0.52 s, ab6, ab10 and ab11 at most 0.96 s).

#### TIMING2 screen of best_v9e (tsc) and H14

the economy worker found that in all 40 TIMING2 games of best_v9e's twin budget_timing's map locks at round 20 (S = 1510) and
best_v9e lands no hit in rounds 6-19 (the accompanying artifacts, entry 18.6, 18.10). tsc (the accompanying artifacts, the 40 TIMING2 conditions,
both seats, standard start, 0 rejected actions, 0 bot errors, all logs kept) changes one option of the frozen
best_v9e at a time; base tm2 (the twin, 0-34-6, worst -26). Empirical, within this pool:

| Option changed | W-D-L (worst) | Slowest call | Conditions that change against tm2 |
| --- | ---: | ---: | --- |
| attack_mode="current" (no robust rule) | 0-34-6 (-26) | 1.13 s | none; the same HP in all 40 |
| big_threat=null (no all-gold insurance, rule 3b) | 0-34-6 (-26) | 0.57 s | none; the same HP in all 40 |
| fortress_n=null (no splash-only trigger) | 0-34-6 (-26) | 1.42 s | none; the same HP in all 40 |
| attack_share=1.0 (all remaining gold for the attack) | 40-0-0 (+146) | 1.38 s | 34 draws and 6 losses become wins, all at round 50, by +146 to +760 (median +460) |

Changing the attack budget alone turns all 40 games into wins; the other three options change no HP. Example (log
00121, budget_timing tier1 in round 2 with half its gold, seat 0; the twin loses it by 20): with attack_share=1.0 the
attacks deal 26 in round 6 and 60, 26, 60, 60 and 60 in rounds 14, 15 and 17-19, and the opponent is at 508 HP when
its map locks in round 20, against our 780. In best_v9e the catch-up budget (rounds 2-5, while behind) defaults to
attack_share, and a full catch-up budget was rejected in cycle 9 (V18F1 on TARGETED2, section 5.10). H14 (stated
at 20:19:29Z in the selection records in the accompanying artifacts, before any game of the candidate) therefore tests
AS1C = best_v9e with `attack_share=1.0&catch_up_share=0.5`: it predicts that
AS1C wins all 40 TIMING2 conditions and has best_v9e's outcome on every condition of PCS, TIMING, STRIKE1,
TARGETED2, f5t, PUNISH, BLUFFCOV and TARGETED3_P5TF, with no prediction for the five grower pools. Reading rule
(also stated before the games): the report names AS1C as the recommended next revision only if on all 846
conditions of the R13 pools its outcome is at least best_v9e's, with 0 rejected actions, 0 bot errors and no call
of 3 s or more. The delivered bot in the accompanying artifacts stays best_v9e in every case, since the validation worker's pool D is pinned to its hash.

H14 result (runs h14pc, h14tm, h14tm2, h14s1, h14t2, h14f, h14pu, h14b, h14t3, h14hd, h14sg, h14g, h14gm and h14st;
all 846 conditions, both seats, each pool on its own starts; 0 rejected actions, 0 bot errors; best_v9e's runs as
in R13; comparison table in the accompanying artifacts; "worse" and "better" compare outcomes, W > D > L):

| Pool | AS1C | best_v9e | Worse | Better | Same outcome, other HP | AS1C slowest call |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| PCS (8) | 6-2-0 | 2-6-0 | 0 | 4 | 0 | 1.01 s |
| TIMING (32) | 26-6-0 | 18-12-2 | 0 | 8 | 10 | 1.53 s |
| TIMING2 (40) | 40-0-0 | 0-34-6 | 0 | 40 | 0 | 0.75 s |
| STRIKE1 (40) | 36-0-4 | 34-2-4 | 0 | 2 | 20 | 0.47 s |
| TARGETED2 (48) | 32-12-4 | 24-20-4 | 2 | 8 | 16 | 1.31 s |
| f5t (76) | 70-6-0 | 70-6-0 | 0 | 0 | 26 | 1.14 s |
| PUNISH (34) | 32-0-2 | 34-0-0 | 2 | 0 | 30 | 1.02 s |
| BLUFFCOV (16) | 16-0-0 | 16-0-0 | 0 | 0 | 16 | 0.30 s |
| TARGETED3_P5TF (30) | 26-0-4 | 18-2-10 | 0 | 8 | 8 | 8.88 s |
| HANDOFF (36) | 16-0-20 | 12-0-24 | 2 | 6 | 22 | 0.65 s |
| SCREENED (60) | 60-0-0 | 50-0-10 | 0 | 10 | 50 | 0.81 s |
| GROWERS (142) | 62-0-80 | 66-0-76 | 4 | 0 | 136 | 0.42 s |
| GUARDED_MAZE (144) | 66-0-78 | 66-0-78 | 2 | 2 | 108 | 0.38 s |
| STAGED (140) | 116-0-24 | 114-0-26 | 2 | 4 | 112 | 0.56 s |
| All (846) | 604-26-216 | 524-82-240 | 14 | 92 | 554 | 8.88 s |

AS1C's outcome is better on 92 conditions and worse on 14, which are 7 opponents in both seats: guard_roster
["tier1","tier1"] (TARGETED2; -840 at round 12, where best_v9e draws), defensive counter 33 (PUNISH) and heavy_drip
(STAGED), whose games against AS1C have the same actions in all 50 rounds (-445 at round 50, where best_v9e wins
+1723 at round 35), guard_handoff on the empty layout with growth 7 (HANDOFF; -95 against +139), two maze growers
(cash_rank_1 with growth 7, -665 at round 9 against +380 at round 13; the planner opening layout with growth 6 and a tier2 bait,
-652 at round 9 against +713 at round 14) and guarded_maze cash_rank_1 with growth 6 and a round-4 guard (-887 at
round 9 against +185 at round 14). The 8.88 s call is against guarded_adaptive_continuation, at a machine load
average of about 155; best_v9e's twin took up to 3.32 s on the same pool (t9k). H14 is refuted: AS1C wins all 40
TIMING2 conditions as predicted, but its outcome differs from best_v9e's on PCS, TIMING, STRIKE1, TARGETED2, PUNISH
and TARGETED3_P5TF; only f5t and BLUFFCOV keep every outcome. By the reading rule AS1C is not named as a
recommended revision. Reading (empirical, on these pools): the attack budget of half the remaining gold costs
best_v9e the budget_timing strikes (TIMING, TIMING2, PCS and the budget_timing part of TARGETED2) and protects it
against the 7 opponents above. Mechanism in the two traced losses (seat 0; logs h14t2 00029 and h14pu 00001): rule 4
buys as many copies of the chosen tier as its budget pays for (at most max_minions = 60), so with all remaining
gold as the budget an accepted attack leaves rule 5 less than the price of one more copy. Against guard_roster AS1C
spends its round-6 gold on 11 tier1, all killed, and has 7 factories against the counter's 25; the counter has 124
factories by round 11, and its tier5 deal 280 and 560 in rounds 11 and 12. Against defensive counter 33 AS1C has 14 or
15 factories from round 5 to round 11 and takes 140 in each of rounds 7 to 10; the game ends 235:680 at round 50.
Screen of intermediate shares (runs s75tm2, s75x, s65tm2, s65x; best_v9e with attack_share 0.75 or 0.65 and
catch_up_share 0.5; rule stated before the games, selection records in the accompanying artifacts at 21:05:30Z: a share goes to the full gate only if
its outcome is at least best_v9e's on all 46 screen conditions and it wins at least one TIMING2 condition). Both
seats, 0 rejected actions, 0 bot errors, slowest call 1.07 s:

| Share | TIMING2 (40) | guard_roster ["tier1","tier1"] | defensive counter 33 | guarded_maze cash_rank_1, growth 6, guard 4 |
| --- | ---: | ---: | ---: | ---: |
| 0.5 (best_v9e) | 0-34-6 (worst -26) | D 0, round 50 | W +1723, round 35 | W +185, round 14 |
| 0.65 | 38-0-2 (-12) | L -280, round 50 | L -470, round 50 | W +341, round 14 |
| 0.75 | 38-0-2 (-12) | L -280, round 50 | L -470, round 50 | W +449, round 14 |
| 1.0 (AS1C) | 40-0-0 (+460) | L -840, round 12 | L -445, round 50 | L -887, round 9 |

At 0.65 and 0.75 the two remaining TIMING2 losses are the condition best_v9e's twin also loses by 12 (tier2 in
round 2 with half the budget). Neither share passes, so none was gated. Reading (empirical, on these 46
conditions): already at a share of 0.65 the budget_timing strikes are won and guard_roster and defensive counter 33 are
lost, so within this option the trade-off is not removed by an intermediate value.

Diagnostic AS1 (h14t2b; attack_share=1.0 with the catch-up budget at its default, also 1.0) on TARGETED2: 30-10-8
against AS1C's 32-12-4. It also loses guard_geometry ["tier2"] (-1097 at round 13) and guard_roster ["tier2"] (-697
at round 50), both seats, which AS1C draws and wins (+5); V18F1, the full catch-up budget rejected in cycle 9
(section 5.10), lost the same two opponents, which is why AS1C keeps catch-up at 0.5.

AS1C against the validation worker's targeted counters on the standard start (development evidence; one start, so these games
are not independent samples). In the validation worker's ten-policy table (the accompanying artifacts;
M is the guarded screened-order counter with the frozen fortress v38 continuation, N is AS1C, and the other eight
rows keep their definitions from the validation worker's eight-policy table), AS1C's payoff against each of the eight older
policies is at least best_v9e's and higher against two (N minus B is [1, 0, 0, 0, 2, 0, 0, 0] on
B, C, D, G, H, I, J, L). The screened guarded counter that beats best_v9e 800:774 loses to AS1C 380:774 (section
6). The delayed-wall counter Q beats both best_v9e and AS1C 770:740 (section 6), and AS1C beats best_v9e by 60
head to head (section 5.16). None of this changes the selection: AS1C failed the gate on the 14 pools (H14 above).

#### Ablations of best_v9f and the turret-only condition of af2g

best_v9f (base: x33g, GROWERS 130-0-12, and x33f, f5t 70-6-0; options on the frozen best_v9f file):

| Run | Option changed | Pool | W-D-L (worst) | Conditions that change against the base (both seats unless stated) |
| --- | --- | --- | ---: | --- |
| af2g | passive_until=null (no passive rule) | GROWERS | 128-0-14 (-1240) | 8 losses become wins, 10 wins become losses |
| af3g | passive_mid_from=null (no round-5 mid step) | GROWERS | 142-0-0 (+385) | 12 losses become wins |
| af14g | spec_share=0&big_threat=null&poke_insurance=false&mid_until=null (no insurance) | GROWERS | 142-0-0 (+200) | 12 losses become wins |
| af8 | big_threat=null | f5t | 42-14-20 (-270) | 20 wins become losses, 8 wins become draws |
| af9 | big_partial=false | f5t | 70-6-0 (+0) | none |
| af10 | fortress_n=null | f5t | 70-6-0 (+0) | none |

Reading (empirical, within these pools): on GROWERS the passive rule is not where best_v9f's gain over best_v9e comes
from (af2g wins 128 games against best_v9f's 130: it loses 10 that best_v9f wins and wins 8 that best_v9f
loses), and best_v9f's insurance steps cost grower games (without the round-5
mid step or without any insurance it wins all 142). On f5t the all-gold insurance against big threats (rule 3b) is
needed (af8 loses 20 games), while big_partial and the fortress trigger change no outcome there. To find which of af2g's four
values carries its GUARDED_MAZE loss, gmchk2 played af2g with one best_v9e value restored at a time on the lost
condition (both seats): with poke_reactive="turret" restored it wins by 305 HP in round 14, as best_v9e does; with
fail_limit=1, robust_k=2 or behind_mode=null restored it still loses by 815 HP in round 9. Restoring poke_reactive="turret" alone removes the loss, while each other individual restoration leaves it
(with poke_reactive="turret_only" the opponent condition of rules 3c and 3d holds only while the
opponent owns a turret, not when its roster holds the tier1 bait bought in round 2). The same four specs on GROWERS (runs gy1-gy4, 142 games each, 0 rejected actions, 0 bot errors)
give the same answer: with poke_reactive="turret" restored (gy1) the outcome and HP difference equal those of
best_v9e's twin on all 142 conditions (66-0-76), and with fail_limit=1, robust_k=2 or behind_mode=null restored
(gy2-gy4) they equal af2g's on all 142 (128-0-14). Each of the other three individual restorations changes no GROWERS result and no result on
the lost guarded maze; restoring the turret-or-bait condition alone removes af2g's whole grower gain and its one GUARDED_MAZE loss.

Why one value decides both (traces of the logs kept in runs gmchk, gm2 and g13gm, seat 0; empirical). Call C1 the
GUARDED condition above (growth 4, splash guard in round 3) and C3 the same opponent with growth_rounds=5 and
guard_round=4 (same layout, bait and tier). In rounds 1 and 2 the two opponents play the same actions (factories,
and the tier1 bait in round 2); from round 3 they differ (C1 builds its splash in round 3, C3 in round 4). In round 3
best_v9e, whose opponent condition counts the tier1 in the opponent's roster, buys a gun1, a splash at (1,3) and two
factories; af2g, whose condition needs an opponent turret and so does not hold yet, buys the gun1 and five
factories. Against C1 the opponent buys tier5 units from round 6; best_v9e then takes 140, 0, 140 and 280 HP in
rounds 6 to 9 and nothing afterwards, ends round 9 with 235 HP and wins by 305 in round 14 with tier2 attacks from
round 11, while af2g takes 140, 140, 280 and 280 and ends round 9 at -45 (loss by 815). Against C3 the order is
reversed: best_v9e's twin V18FT loses by 1080 in round 9 (gm2) and af2g wins by 936 in round 12 (g13gm). In every
one of these logs both players' actions in rounds 1 and 2 are the same in the C1 and the C3 game, and so is the
bot's own round-3 action (best_v9e: gmchk 00001 against gm2 00021, which is the twin; af2g: gmchk 00003 against g13gm
00021). Actions of a round are submitted together and applied interleaved (engine action_order), so a round-3
decision is made from the state after round 2. That state is the same in the C1 and the C3 game for any
deterministic bot that, like these two, does not read the players' name fields (the engine's observation includes
them), so such a bot makes the same round-3 purchase against both opponents. With their purchases best_v9e wins C1
and loses C3, af2g the reverse. The pair does not make the two conditions incompatible: in the economy worker's run g1chk
(the accompanying artifacts, kept logs 00147 and 00165, seat 0) its bot g1 (V29 with attack_from=7, section 5.15) also plays the
same actions in rounds 1-3 in both games, buys a gun1 and six factories in round 3 (14 factories after round 3,
against best_v9e's 7 and af2g's 10) and wins both (+681 in round 10, +1106 in round 11). So the pair is a weakness
of the two main-agent bots, not of every bot. That the cause is their smaller factory count after round 3 is a conjecture:
g1 also differs from them in its later rules (section 6, item "Same history, opposite answers").

#### H12: opponents with a common opening (prefix forks, run fk1)

H12 (module header in the accompanying artifacts, written at 18:57Z before any game against these opponents): these
opponents play the no-bait grower on the planner opening layout with growth 6 (or, with
bait=["tier1"], the same grower with a tier1 bait in round 2) in the rounds before fork_round, and from fork_round
on either keep growing ("grow") or play the validation worker's budget_timing with attack_round=fork_round ("strike", tier and
budget fraction as given). Prediction: best_v9e wins or draws every strike and loses the grow continuation;
best_v9f, P5TNUBM and V33M win the grow continuation and each loses at least one strike. fk1 (the accompanying artifacts) has 12
opponents: grow, grow with the bait, and ten strikes (fork_round 3, 4 or 5, tiers 1 to 4, one with budget_fraction
0.5 and one with the bait). Candidates: best_v9e, best_v9f, V33M (best_v9f with passive_mid_from=null), af2g and
P5TNUBM; both seats, standard start, 120 games, 0 rejected actions, 0 bot errors, slowest call 0.47 s, all logs
kept. Every condition has the same outcome and HP difference in both seats. Empirical, within this pool:

| Candidate | grow | grow, tier1 bait | 10 strikes |
| --- | --- | --- | --- |
| best_v9e | L -1240 r9 | L -1270 r9 | all won, +970 to +2300 |
| best_v9f | W +1040 r12 | W +770 r13 | all won, +1055 to +1445 |
| V33M | W +760 r11 | W +1000 r12 | all won, +785 to +1445 |
| af2g | L -1240 r9 | W +870 r13 | all won, +968 to +1404 |
| P5TNUBM | W +800 r11 | W +620 r12 | all won, +968 to +1895 |

The best_v9e half of the prediction holds; the other half fails: best_v9f, V33M and P5TNUBM win all 24 conditions,
so H12 is refuted. Check of the determinism argument (the accompanying artifacts, exit 0): in
all 100 strike and grow pairs (5 candidates, 2 seats, 10 strikes) the fork's actions first differ in round
fork_round and the candidate's in round fork_round + 1, as the argument in the module docstring requires. Reading:
after this grower's opening, a budget_timing strike from round 3, 4 or 5 does not punish the purchases with which
best_v9f, V33M and P5TNUBM beat the grower. The strike with fork_round=4, tier3 and budget fraction 0.65 plays pool
C's C-08 policy from round 4 on; best_v9f loses C-08 774:800 (section 5.12) and wins this fork by 1382 HP in round 13.
The strikes these bots lose in other pools (TIMING2, C-08) come from budget_timing from round 1, which defends with
its own envelope before its attack round instead of growing. So this pool gives no case in which a common history
forces the trade-off between best_v9e and best_v9f; whether another common opening forces it is open.

### 5.15 The teammates' final bots against best_v9e

Results reported by the workers that own the runs (unchanged engine, both seats, 0 rejected actions and 0 bot errors;
empirical). HP differences are from the teammate bot's side, seat 0 / seat 1 of the teammate bot.

| Worker and bot | Standard start | Other conditions | Source |
| --- | --- | --- | --- |
| The defence worker, fortress v46 (v45 + finish_gun_check 12 + finish_defend_first + a per-decision finish cache; the worker's final recommendation from 21:45Z to 22:39Z) | -5 / -5 | mirror:1:2 +1555 / +1555; asym:3:2 +5735 / D +150 (both destroyed); mirror:22:3 +2940 / +2940; asym:23:2 +2385 / +4222 (7W-1D-2L) | the accompanying artifacts, 21:48Z |
| The defence worker, fortress v48 (v46 with the capacity rule spending the whole slack under a reserve; the worker's final recommendation from 22:39Z) | -5 / -5 | the same ten outcomes and margins as v46 | the accompanying artifacts (compared condition by condition with the defence worker's earlier v46 run by the accompanying artifacts: no difference); the accompanying artifacts, 22:39Z |
| The defence worker, fortress v44 (v41 + factory_cap 1200; the worker's final recommendation from 20:32Z to 21:45Z, then its alternative where decision time matters) | -5 / -5 | mirror:1:2 +2195 / +2195; asym:3:2 +1795 / D +150 (both bases destroyed); mirror:22:3 -6160 / -6160; asym:23:2 D +705 / D +1282 (both destroyed) (3W-3D-4L, live module with v44's parameters) | the accompanying artifacts, 20:04Z, 20:32Z |
| The defence worker, fortress v45 (v44 + finish_wrap + finish_robust_gold 400; documented alternative from 21:18Z) | -5 / -5 | mirror:1:2 +1695 / +1695; asym:3:2 +5735 / D +150 (both destroyed); mirror:22:3 +2940 / +2940; asym:23:2 +2385 / +4222 (7W-1D-2L) | the accompanying artifacts, 21:18Z |
| The defence worker, fortress v41 (the worker's final recommendation until 20:32Z) | -5 / -5 | mirror:1:2 +1555 / +1555; asym:3:2 +1255 / -4330; mirror:22:3 -6160 / -6160; asym:23:2 -2515 / -5858 | the accompanying artifacts, 17:31Z, 18:50Z |
| The defence worker, fortress v43 (v41 + eco_match_insure_cap 260; documented alternative) | -5 / -5 | the same five starts: identical to v41's rows (3W-0D-7L over ten games) | the accompanying artifacts, 18:52Z |
| The defence worker, fortress v40 (lethal_share 0.4) | -5 / -5 | mirror:1:2 +1555 / +1555; asym:3:2 +1395 / +10; mirror:22:3 -1260 / -1260; asym:23:2 -2515 / -5858 (4W-0D-6L) | the accompanying artifacts, 18:52Z |
| The economy worker, V29 (frozen econ29) | -10 / -10 | 12 scripted starts (ho1): 9-0-3 / 6-1-5, worst -5185; held-out sets 3 and 4 (6 starts each): 3-0-3 / 5-0-1 and 4-1-1 / 1-1-4 | the accompanying artifacts, entry 17.11 |
| The economy worker, af5 = V29 + attack_from=5 (selected for fresh validation at 22:43:35Z; recommended for the standard start after the completed gate, announced at 23:34:38Z) | +410 / +410 (round 50) | mirror:1:2 +2660 / +2660; asym:23:2 +1250 / -4470 (frr7); scnaf5 (five other opponents, 12 scripted starts): 113-0-7, V29's result in all 120 games | the accompanying artifacts, entry 18.22, 18.34, 18.35 |
| The economy worker, g1 = V29 + attack_from=7 (the worker's former standalone recommendation) | -10 / -10 | GROWERS 142-0-0, GUARDED_MAZE 144-0-0, HANDOFF 36-0-0 (best_v9e: 66-0-76, 66-0-78, 12-0-24); copies of the main agent's pools (fam2b): TIMING2 40-0-0, STAGED 136-4-0, SCREENED 54-4-2, PUNISH 32-0-2 (best_v9e or its twin: 0-34-6, 114-0-26, 50-0-10, 34-0-0) | the accompanying artifacts, entry 17.14, 17.15, 18.7 |
| The economy worker, g0 = V29 + r1_units=0&attack_from=7 | -15 / -15 | GROWERS 142-0-0, GUARDED_MAZE 144-0-0, HANDOFF 36-0-0; fam2b: TIMING2 40-0-0, STAGED 138-2-0, SCREENED 58-2-0, PUNISH 32-0-2; the economy worker's opp_key5 70-2-18 (V29 82-2-6) | the accompanying artifacts, entry 17.11-17.13, 18.7 |
| The economy worker, V29 + r1_guard=60 (rejected by the economy worker) | +5 / +5 | The economy worker's opp_key5 pool: 40-4-46, against V29's 82-2-6 | the accompanying artifacts, entry 17.11, 17.12 |
| The validation worker, early_wall_guard guard00 (a counter, development) | +30 / +30 (770:740) | 86-0-4 over 90 development target conditions; loses to P5TNUBM with r1_poke=0 and to one bait guard | the accompanying artifacts, early_wall_transfer |

What this shows, within these conditions:
- On the standard start best_v9e beats the defence worker's fortress versions in the table by 5, V29 and g1 by 10 and g0 by 15,
  and every one of these games is decided by the round-1 exchange (the economy worker traced the V29 games: both maps lock and no later attack
  lands; the defence worker reports the same -5 for every fortress version v34-v43). Both players choose round 1 from the same
  public game state up to player labeling (the observation also holds the player index and both configured names;
  the validation worker's identity audit replayed all 72 retained pool C histories with both names replaced and with the players
  swapped, 2208 calls, and best_v9e's actions did not change, the accompanying artifacts),
  with neither pending action visible (section 6, "Round 1 is blind"), so the margin comes from a fixed round-1
  choice, and fixed alternatives turn it around: a round-1 gun2 at (8,1) with two walls and one tier1 (V29 +
  r1_guard=60; 800:795 in both kept logs of the economy worker's run vbest2) or an early wall plus guard (guard00). Both
  lose elsewhere. This round-1 account does not cover af5: it wins by 410 at round 50 in both seats, and in the
  inspected seat-0 history it loses round 1 by 10 (785:795) and best_v9e then loses 140 HP in round 9 and 280 in
  round 10 (afrr and afrep, the accompanying artifacts, entry 18.34; section 5.16).
- On scripted starts best_v9e is not ahead: the fortress wins mirror:1:2 in both seats and asym:3:2 in one, and
  V29 wins 15 of 24 ho1 games. These are continuation starts with buildings best_v9e did not choose, where it plays
  the economy worker's econ20 (section 5.8). The defence worker traces v41's two heavy losses (asym:3:2 seat 1, mirror:22:3) to its
  emergency threshold lethal_share 0.3: partial insurance against econ20's growing flood, which no partial plan
  stops; v40 (threshold 0.4) keeps that gold and loses less there (x201). The worker's later versions win more of
  these starts: v44 (factory cap 1200) 3W-3D-4L over the ten games and v45 (a padded finish that spawns the new
  tier5 alongside the respawning ones) 7W-1D-2L, including mirror:22:3 in both seats (+2940), which v41 and v44 lose
  by 6160; v46 (v45 with a defence-first finish) and the defence worker's final recommendation v48 (from 22:39Z) have the same
  ten outcomes as v45.
  On the standard start every one of them loses to best_v9e by 5.
- The economy worker's growth-first g1 wins every grower, guarded-maze and handoff game in the main agent's pools, where best_v9e
  loses about half, and loses to best_v9e by 10 on the standard start. On copies of four more of the main agent's pools
  (the economy worker's run fam2b, 19:19Z) g1 and g0 win all 40 TIMING2 games, where best_v9e draws 34 and loses 6, and they
  win more STAGED and SCREENED games than best_v9e; they lose 2 PUNISH games (defensive counter 28, -5 at round 50)
  that best_v9e wins. The economy worker traces the TIMING2 difference to the window of rounds 6-19, before budget_timing
  locks at round 20 (the accompanying artifacts, entry 18.6, 18.10). Together with best_v9f (section 5.12) and
  P5TNUBM (section 5.11) this is the complementary-strength evidence of this run: each of these bots wins
  conditions the installed bot loses, and each of them loses conditions that best_v9e wins or draws (best_v9f:
  C-08, C-11 and TIMING2; P5TNUBM: the early strikes of TIMING2; g1 and g0: the standard-start game against
  best_v9e and two PUNISH games).
- On all 846 R13 gate pool memberships (804 distinct conditions, section 5.14; the economy worker's runs gate1 and pcs1 with its earlier runs fam2b, g1chk, grow1, gmaze1,
  hand3 and hand4, compared with best_v9e's base files of the gate; the accompanying artifacts, entry 18.18, 18.23), g1 scores
  764-16-66 against best_v9e's 524-82-240, with a better outcome on 304 conditions and a worse one on 72 (V29:
  584-18-244, worse 150, better 208; g0: 748-22-76, worse 84, better 298; AS1C, for comparison: 604-26-216, section
  5.14). Worse/better per pool for g1: STRIKE1 18/0, f5t 22/2, TARGETED2 10/16, TIMING 6/14, TIMING2 0/40, PUNISH
  2/0, BLUFFCOV 0/0, TARGETED3_P5TF 4/12, HANDOFF 0/24, SCREENED 6/10, GROWERS 0/76, GUARDED_MAZE 0/78, STAGED 4/26,
  PCS 0/6 (g1 8-0-0, best_v9e 2-6-0). I recomputed the STRIKE1, f5t, TARGETED2 and TIMING counts and the two PCS
  totals from the result files with the accompanying artifacts and got the same numbers.
  g1's worse conditions are lock-against-lock games decided by the early exchange (with attack_from=7 it does not
  attack in rounds 2 to 6), two round-7 floods by economic timing policy (-2139 and -1859) and five growth-8 guarded mazes
  that best_v9e wins by more than 1000 (the economy worker's reading). Under R13 g1 would be rejected, as af2g and AS1C were;
  by the count of conditions won on these pools it is ahead of best_v9e. Counted once per distinct condition (804),
  g1 is 726-16-62 and best_v9e 504-64-236, worse 68, better 282 (V29: 546-14-244, worse 146, better 186; the validation worker's
  audit, recounted with the accompanying artifacts). Four of the pools informed g1's choice (GROWERS, GUARDED_MAZE and HANDOFF
  directly, f5t through its overlap with the economy worker's opp_key5; 398 conditions, the accompanying artifacts, entry 17.14, 18.23). The
  other ten pools (448 memberships, all run after g1 was fixed at 17:53Z) cover 416 distinct conditions, ten of which
  are also in f5t; on the 406 distinct conditions outside the four selection pools g1 is 350-14-42 (worse 46, better
  102), V29 280-4-122 and best_v9e 290-58-58; those pools were built by the main agent and the validation worker, many from
  conditions where best_v9e had been found weak, so they are not neutral either. The economy worker's run bvf (best_v9e on that
  worker's fresh5 and fresh6 opponents, prediction H18.20 stated at 21:35:43Z) is fresh for both bots' selection but
  not neutral: most counters built by the validation worker in those sets were built against best_v9e, which may favour g1 (the economy worker's
  statement in 18.20; the size of that effect is not measured, and the split below does not estimate it); the 15 opponents that are not counters built by the validation worker (the main agent's af2g, V33M, P4TNUB,
  P5TNUBM and AS1C and the defence worker's fortress v36 to v45) are reported separately. bvf finished at 23:20:13Z (86 games,
  0 rejected actions, 0 bot errors). Counted by the main agent with the accompanying artifacts from bvf, the economy worker's fresh5a and
  fresh6 (g1, V29) and afq56 (the economy worker's later af5 = V29 + attack_from=5, selected by its rule 18.22 at 22:43Z for fresh validation, before
  afq56; the accompanying artifacts, entry 18.26, 18.29), on the 43 opponents in both seats:

  | Opponents | Conditions | best_v9e | af5 | g1 | V29 |
  | --- | ---: | --- | --- | --- | --- |
  | the main agent's bots (af2g, V33M, P4TNUB, P5TNUBM, AS1C) | 10 | 0-8-2 | 4-0-6 | 2-0-8 | 2-0-8 |
  | The defence worker's fortress v36 to v45 | 20 | 20-0-0 | 20-0-0 | 18-0-2 | 4-0-16 |
  | The validation worker's counters | 56 | 36-4-16 | 54-0-2 | 50-0-6 | 36-2-18 |
  | all | 86 | 56-12-18 | 78-0-8 | 70-0-16 | 42-2-42 |
  | the first two rows (the economy worker's NOT_BUILT_AGAINST: not counters built by the validation worker; membership only, not a test of targeting) | 30 | 20-8-2 | 24-0-6 | 20-0-10 | 6-0-24 |

  Against best_v9e's outcome g1 is worse on 14 conditions and better on 20, af5 worse on 6 and better on 24. af5's
  six: delayed_wall_guard (-5 at round 50; best_v9e +30) and P4TNUB and P5TNUBM (-10 at round 50; best_v9e draws).
  best_v9e loses to AS1C by 60 (af5 and g1 by 10) and loses to eight and draws two of the validation worker's counters at round 50
  (by 26 to 235), all of which af5 beats. The economy worker's mean score differences over the 43 opponents (bootstrap over
  opponents, the accompanying artifacts, entry 18.30; same tables): g1 - best_v9e +0.093 [-0.070, +0.256], so H18.20 is not falsified
  and g1 is not shown better either; af5 - best_v9e +0.186 [+0.058, +0.326]; on the 15 opponents that are not
  the validation worker's counters g1 - best_v9e -0.133 [-0.300, +0.033] and af5 - best_v9e +0.000 [-0.133, +0.133]; the validation worker
  reproduced the af5, g1 and V29 counts and af5 - g1 +0.093 [+0.023, +0.186] (the accompanying artifacts, 23:21Z). Empirical, within
  these 43 opponents on the standard start. The economy worker's gate run afg5 (af5 on the 514 gate conditions outside its
  290-condition sweep afs5, 18.26) finished before 23:38Z, and the validation worker recounted the whole gate (the accompanying artifacts
  23:38:50Z): on the 804 distinct R13 gate conditions af5 is 764-2-38 (g1 726-16-62, V29 546-14-244, best_v9e
  504-64-236), 804-2-40 on the 846 memberships, every pool has af5 wins at least g1 wins minus two, and the validation worker
  confirmed that the economy worker's declared standard-start rule passes. The economy worker's scnaf5 (the accompanying artifacts, entry 18.35,
  23:39:18Z to 23:47:49Z, 120 games: the five opponents of opp_heldout3 without a clock read in their import closure,
  the 12 scenarios of held-out sets 3 and 4, both seats; 0 errors, 0 rejected actions) has af5 113-0-7, all seven
  losses against eco6_t5, and every game has the winner, HP difference and length of V29's game in hs3 or hs4
  (main-agent check in the accompanying artifacts: 120 paired, 0 differ). The clock-reading opponents of those sets and the other
  scenario sets were not run with af5. Counted by the main agent with the accompanying artifacts: against best_v9e af5 is worse on 30 distinct
  conditions and better on 288, and on the 406 conditions outside g1's four selection pools 384-0-22 (worse 14,
  better 108). The 290 sweep conditions informed af5's choice, so the gate is not wholly held out for it. On those 290 conditions
  (development evidence, the accompanying artifacts, entry 18.26, 18.36, 18.37) the wins for attack_from = 2 (V29), 3, 4, 5 (af5), 6 and
  7 (g1) are 48, 146, 162, 264, 238 and 228; the main agent recounted af3's 146-0-144 and af4's 162-2-126 from
  the accompanying artifacts and afs4, and the validation worker confirmed the six counts (the accompanying artifacts, 00:05:26Z and 00:06:20Z).

### 5.16 Final round robins of the finalists (frr1, frr2)

Runs frr1 (standard start, ten bots, 45 pairs, 90 games) and frr2 (mirror:1:2 and asym:23:2, six bots, 15 pairs,
60 games), using frozen specifications from the accompanying artifacts (the delivered bot file is not read;
its bytes equal the frozen best_v9e copy). Both seats, one deterministic
game per pair, seat and start; 0 rejected actions and 0 bot errors in all 150 games; slowest call 4.57 s (af2g, frr1).
The games are descriptive: no selection depends on them. The bots are the installed best_v9e, the main agent's other
gated or screened candidates best_v9f, af2g, P5TNUBM and AS1C, the defence worker's fortress v41 (its final recommendation
when the finalist list was recorded, by 20:05Z; a former finalist since 20:32Z), the economy worker's V29 and g1,
the validation worker's counter guard00 and the baseline threat_defender. mirror:1:2 gives both players the same scripted two-round
opening; asym:23:2 gives each seat its own (seat 0 from seed 46, seat 1 from seed 47), so that start is not
symmetric between the seats. Tables from the accompanying artifacts; each cell is the row bot's
outcome in seat 0 and seat 1 and its HP difference in each.

frr1:

Start std: row bot's result, seat 0 / seat 1 HP difference of the row bot

| | AS1C | best_v9e | best_v9f | af2g | P5TNUBM | v41 | g1 | V29 | guard00 | threat_defender |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AS1C | - | WW +60/+60 | DD +0/+0 | WW +60/+60 | DD +0/+0 | WW +5/+5 | WW +10/+10 | WW +10/+10 | LL -30/-30 | WW +1020/+1020 |
| best_v9e | LL -60/-60 | - | DD +0/+0 | DD +0/+0 | DD +0/+0 | WW +5/+5 | WW +10/+10 | WW +10/+10 | LL -30/-30 | WW +980/+980 |
| best_v9f | DD +0/+0 | DD +0/+0 | - | DD +0/+0 | DD +0/+0 | WW +5/+5 | WW +10/+10 | WW +10/+10 | LL -30/-30 | WW +1400/+1400 |
| af2g | LL -60/-60 | DD +0/+0 | DD +0/+0 | - | DD +0/+0 | WW +5/+5 | WW +10/+10 | WW +10/+10 | LL -30/-30 | WW +980/+980 |
| P5TNUBM | DD +0/+0 | DD +0/+0 | DD +0/+0 | DD +0/+0 | - | DD +0/+0 | WW +10/+10 | WW +8/+8 | LL -30/-30 | WW +880/+880 |
| v41 | LL -5/-5 | LL -5/-5 | LL -5/-5 | LL -5/-5 | DD +0/+0 | - | LL -55/-55 | WW +5/+5 | LL -40/-40 | WW +800/+800 |
| g1 | LL -10/-10 | LL -10/-10 | LL -10/-10 | LL -10/-10 | LL -10/-10 | WW +55/+55 | - | LL -17/-17 | WW +28/+28 | WW +840/+840 |
| V29 | LL -10/-10 | LL -10/-10 | LL -10/-10 | LL -10/-10 | LL -8/-8 | LL -5/-5 | WW +17/+17 | - | LL -45/-45 | WW +840/+840 |
| guard00 | WW +30/+30 | WW +30/+30 | WW +30/+30 | WW +30/+30 | WW +30/+30 | WW +40/+40 | LL -28/-28 | WW +45/+45 | - | WW +820/+820 |
| threat_defender | LL -1020/-1020 | LL -980/-980 | LL -1400/-1400 | LL -980/-980 | LL -880/-880 | LL -800/-800 | LL -840/-840 | LL -840/-840 | LL -820/-820 | - |

| bot | W-D-L | worst HP diff | slowest call (s) | rejected | bot errors |
| --- | ---: | ---: | ---: | ---: | ---: |
| guard00 | 16-0-2 | -28 | 0.62 | 0 | 0 |
| AS1C | 12-4-2 | -30 | 3.35 | 0 | 0 |
| best_v9f | 8-8-2 | -30 | 2.35 | 0 | 0 |
| P5TNUBM | 6-10-2 | -30 | 3.33 | 0 | 0 |
| af2g | 8-6-4 | -60 | 4.57 | 0 | 0 |
| best_v9e | 8-6-4 | -60 | 2.70 | 0 | 0 |
| g1 | 6-0-12 | -17 | 2.78 | 0 | 0 |
| v41 | 4-2-12 | -55 | 2.22 | 0 | 0 |
| V29 | 4-0-14 | -45 | 3.48 | 0 | 0 |
| threat_defender | 0-0-18 | -1400 | 0.15 | 0 | 0 |

frr2:

Start asym:23:2: row bot's result, seat 0 / seat 1 HP difference of the row bot

| | AS1C | best_v9e | best_v9f | v41 | g1 | V29 |
| --- | --- | --- | --- | --- | --- | --- |
| AS1C | - | WL +4470/-4470 | WL +4470/-4470 | WW +5858/+2515 | WL +4470/-1250 | WL +4470/-1250 |
| best_v9e | WL +4470/-4470 | - | WL +4470/-4470 | WW +5858/+2515 | WL +4470/-1250 | WL +4470/-1250 |
| best_v9f | WL +4470/-4470 | WL +4470/-4470 | - | WW +5858/+2515 | WL +4470/-1250 | WL +4470/-1250 |
| v41 | LL -2515/-5858 | LL -2515/-5858 | LL -2515/-5858 | - | LL -3215/-2218 | LL -3215/-2218 |
| g1 | WL +1250/-4470 | WL +1250/-4470 | WL +1250/-4470 | WW +2218/+3215 | - | WL +1250/-1250 |
| V29 | WL +1250/-4470 | WL +1250/-4470 | WL +1250/-4470 | WW +2218/+3215 | WL +1250/-1250 | - |

Start mirror:1:2: row bot's result, seat 0 / seat 1 HP difference of the row bot

| | AS1C | best_v9e | best_v9f | v41 | g1 | V29 |
| --- | --- | --- | --- | --- | --- | --- |
| AS1C | - | DD +0/+0 | DD +0/+0 | LL -1555/-1555 | LL -2660/-2660 | LL -2660/-2660 |
| best_v9e | DD +0/+0 | - | DD +0/+0 | LL -1555/-1555 | LL -2660/-2660 | LL -2660/-2660 |
| best_v9f | DD +0/+0 | DD +0/+0 | - | LL -1555/-1555 | LL -2660/-2660 | LL -2660/-2660 |
| v41 | WW +1555/+1555 | WW +1555/+1555 | WW +1555/+1555 | - | WW +15/+15 | WW +15/+15 |
| g1 | WW +2660/+2660 | WW +2660/+2660 | WW +2660/+2660 | LL -15/-15 | - | DD +0/+0 |
| V29 | WW +2660/+2660 | WW +2660/+2660 | WW +2660/+2660 | LL -15/-15 | DD +0/+0 | - |

| bot | W-D-L | worst HP diff | slowest call (s) | rejected | bot errors |
| --- | ---: | ---: | ---: | ---: | ---: |
| V29 | 12-2-6 | -4470 | 3.36 | 0 | 0 |
| g1 | 12-2-6 | -4470 | 3.38 | 0 | 0 |
| v41 | 10-0-10 | -5858 | 2.47 | 0 | 0 |
| AS1C | 6-4-10 | -4470 | 3.51 | 0 | 0 |
| best_v9e | 6-4-10 | -4470 | 2.78 | 0 | 0 |
| best_v9f | 6-4-10 | -4470 | 3.51 | 0 | 0 |

What this shows, within these conditions (empirical; ten selected bots on one start and six on two scripted
starts, not a population of opponents):
- On the standard start every pair has the same outcome and margin in both seats, and the four frr1 pairs that
  repeat a game of section 5.15 (best_v9e against v41, g1, V29 and guard00) give the margins reported there by the
  owning workers.
- The validation worker's guard00, built as a counter to best_v9e, wins 16 of its 18 games: 30 against each of the main agent's five
  bots, 40 against v41 and 45 against V29; it loses only to g1 (-28). AS1C is 12-4-2: it beats best_v9e and af2g by
  60, draws best_v9f and P5TNUBM and loses only to guard00. best_v9e is 8-6-4: it beats v41 (+5), g1 and V29 (+10)
  and threat_defender (+980), draws best_v9f, af2g and P5TNUBM, and loses to AS1C (-60) and guard00 (-30).
- AS1C against best_v9e (kept log 00018, the accompanying artifacts): both play the same actions in rounds 1 to 5; in round 6
  AS1C buys a tier4 with part of its budget and best_v9e buys 15 factories; the tier4 deals 60 damage, no later
  attack of either side lands, and the game ends 785:725 at round 50. best_v9e's attack budget in round 6 is half of
  AS1C's (attack_share 0.5 against 1.0, section 5.14), and it buys no minion.
- Results are not transitive: g1 beats guard00 (+28), guard00 beats best_v9e (+30) and best_v9e beats g1 (+10);
  g1 beats v41 (+55), v41 beats V29 (+5) and V29 beats g1 (+17). By wins minus losses the order is guard00 +14,
  AS1C +10, best_v9f +6, best_v9e, af2g and P5TNUBM +4, g1 -6, v41 -8, V29 -10, threat_defender -18. Every
  standard-start margin between the nine non-baseline bots is at most 60 HP.
- The standard-start matrix as a game. Score each frr1 pair +1, 0 or -1 for the row bot (every pair has the same
  outcome in both seats), giving a symmetric zero-sum game on the ten bots with value 0. The ten self-play diagonal
  entries are set to 0 by symmetry, not measured, and each off-diagonal entry is one deterministic game per seat,
  not a mean over repeated trials. Proposition (exact, for
  this recorded matrix only): its max-min mixtures are exactly those that put 1/3 on g1, 1/3 on guard00 and the
  remaining 1/3 in any split on AS1C, best_v9f and P5TNUBM; best_v9e, af2g, v41, V29 and threat_defender get weight
  0 in every one. Proof: let a, b be the weights of g1 and guard00 and r the total weight of best_v9e, af2g, v41,
  V29 and threat_defender. A max-min mixture scores at least 0 against every column. Against guard00, which only g1
  beats, this gives a >= 1 - a - b; against g1, which loses to the five main-agent bots and V29 and beats v41, guard00 and
  threat_defender, it gives 1 - a - b - 2u >= b, where u is the weight of v41 and threat_defender; against AS1C,
  which only guard00 beats and which beats best_v9e, af2g, v41, g1, V29 and threat_defender, it gives b >= a + r.
  The first two give a >= 1 - a - b >= b and the third b >= a, so a = b, r = 0, u = 0 and 1 - 2a = a, that is
  a = b = 1/3. Conversely, with weight c on AS1C, every such mixture scores 0 against AS1C, best_v9f, P5TNUBM, g1
  and guard00, c against best_v9e and af2g, and more than 0 against v41, V29 and threat_defender (checked in exact
  fractions; the matrix-analysis script in the accompanying artifacts finds the same support by linear programming). The validation worker checked the proposition
  independently from the 90 kept games with exact primal and dual certificates
  (the accompanying artifacts, 22:24Z); since the game is symmetric, the equilibria
  are exactly the pairs of such mixtures. In this matrix AS1C and
  best_v9f each weakly dominate best_v9e: no column where best_v9e scores more, and AS1C scores more against AS1C,
  best_v9e and af2g, best_v9f against AS1C. This is a statement about nine selected bots and a baseline on one
  start; on the 14 gate pools AS1C and best_v9f each lose conditions that best_v9e wins or draws (sections 5.12,
  5.14).
- On mirror:1:2 the three main-agent bots draw each other and lose to v41 (-1555) and to g1 and V29 (-2660) in both
  seats; v41 beats g1 and V29 by 15. On asym:23:2 the seat decides every pair that does not include v41: the bot in
  seat 0 wins (by 4470 between two main-agent bots, by 1250 between g1 and V29, and by 4470 or 1250 between a main-agent bot and
  g1 or V29); v41 loses all ten of its asym:23:2 games. Over frr2 V29 and g1 are 12-2-6, v41 10-0-10 and each insurance
  bot 6-4-10. These continuation starts are where best_v9e plays the economy worker's econ20 (section 5.8).
- Caveats: v41 is not the defence worker's final bot (v46 from 21:45Z to 22:39Z, then v48; runs frr3 and frr4 add v46 and
  frr5 and frr6 add v48 against the same bots, section 5.16 addendum below). guard00's record here is on the start it was built for; the validation worker
  reports 86-0-4 over its 90 development targets and losses to P5TNUBM with r1_poke=0 and to one bait guard (section
  5.15). None of these games changes the selection, which was closed at 19:50Z under R13.

#### Section 5.16 addendum: the defence worker's v46 and v48 (frr3 to frr6) and the economy worker's af5 (frr7, frr8)

The defence worker's v46, its final recommendation from 21:45Z (the accompanying artifacts, 21:48Z),
played against the same bots through its `:@make` entry point, both seats, one deterministic game per pair,
seat and start. The defence worker replaced it at 22:39Z by v48, also using its `:@make` entry point,
played against the same bots after frr4 (frr5, from 22:49:46Z, and frr6, from 23:15:51Z, in a newly freed slot;
the queue scripts are in the accompanying artifacts).

frr3 (standard start, v46 against the ten frr1 bots, 20 games, 22:08:43Z to 22:36:52Z; 0 rejected actions, 0 bot
errors): v46 is 4-4-12, with the same outcome and margin in both seats against every opponent. It loses to AS1C,
best_v9e, best_v9f and af2g by 5, to g1 by 55 and to guard00 by 40, draws P5TNUBM and v41, and beats V29 by 5 and
threat_defender by 2000 (round 11). Against each of the nine bots other than v41 this is v41's outcome in frr1
(v41 beats threat_defender by 800 at round 10). The games against best_v9e and V29 repeat the defence worker's run
in the accompanying artifacts with the same results (-5 and +5 in both seats); x215 loads best_v9e as
the `:decide` entry point and frr3 as the `:@make` entry point, the same file (sha256 70ef8eab...). With v46 added the standard-start
matrix has the same max-min mixtures as in the proposition above, and v46 gets weight 0 in every one: v46's row
equals v41's on the ten frr1 columns and v46 draws v41, so each inequality of the proof holds with v46 counted
with v41 in u and r, and the mixtures of the proposition score at least 2/3 against v46 (the matrix-analysis script in the accompanying artifacts on
frr1 and frr3 together gives the same support). The main-agent bots' calls are slower against v46 than against any frr1
bot (section 7).

frr4 (mirror:1:2 and asym:23:2, v46 against the six frr2 bots, 24 games, 22:36:52Z to 22:49:43Z; 0 rejected
actions, 0 bot errors): v46 is 22-2-0. On mirror:1:2 it beats AS1C, best_v9e and best_v9f by 1555 at round 14 and
g1 and V29 by 15 at round 50, in both seats, and draws v41 at round 50. On asym:23:2 it wins all twelve games, in
both seats: in seat 0 by 2385 against the five opponents other than v41 and by 5455 against v41, and in seat 1 by
4222 against the three main-agent bots, by 9822 against g1 and V29 and by 1265 against v41. In frr2 every asym:23:2 pair
without v41 was won by the bot in seat 0, and v41 lost all ten of its asym:23:2 games in both seats; the five other
frr2 bots win this start in seat 1 only against v41, and v46 is the only one of the seven bots that wins it in seat 1
against every other bot. The games
against best_v9e and V29 repeat the defence worker's earlier v46 run (best_v9e loaded as `:decide` there, `:@make` here) with the same
results. Over frr2 and frr4 together, on these two
scripted starts, v46 is 22-2-0, V29 and g1 12-2-10, v41 10-2-12 and each main-agent bot 6-4-14. Slowest calls: V29 8.71 s
and g1 8.60 s (mirror:1:2 against v46, in games that end at round 50; the logs do not record which round's call
was the slowest), v46 2.00 s, the main-agent bots at most 2.05 s.

frr5 (standard start, v48 against the ten frr1 bots, 20 games, 22:49:46Z to 23:18:15Z; 0 rejected actions, 0 bot
errors): v48 is 4-4-12, and every one of the 20 games has frr3's winner, HP difference and length (v48 against
v46's opponents, compared condition by condition with the accompanying artifacts). The max-min mixtures above therefore
also give v48 weight 0. The opponents' slowest calls against v48 are P5TNUBM 14.03 s, V29 11.41 s, g1 10.52 s,
af2g 7.67 s, best_v9e 6.97 s, AS1C 6.47 s and best_v9f 6.33 s; v48's own is 2.25 s.

frr6 (mirror:1:2 and asym:23:2, v48 against the six frr2 bots, 24 games, 23:15:51Z to 23:28:24Z; 0 rejected actions,
0 bot errors): v48 is 22-2-0, and every game has frr4's winner, HP difference and length (compared with
the accompanying artifacts against v46's frr4 games). Everything said above about v46 on these two starts therefore holds
for v48. Slowest calls: g1 9.58 s, V29 9.02 s, best_v9e 1.76 s, best_v9f 1.66 s, AS1C 1.45 s, v48 1.26 s, v41
1.17 s. The defence worker's two final recommendations v46 and v48 are thus not distinguished by any of the 44 matched
conditions (88 games) of frr3 to frr6 (the validation worker found all 44 pairs of full histories identical, the accompanying artifacts
23:36:39Z); the defence worker's own regression (x230 against x215, section 5.15) also gives them the same ten outcomes
against best_v9e and V29, and in the defence worker's full regression of v48 against v46 (nine pools) the only reported
difference is one margin (econ15 under asym:23:2 in seat 1, a win by 4160 instead of 3460; the accompanying artifacts, 22:39Z).
The defence worker prefers v48 for two defects that the external referee (a second model) constructed in v46 (artificial states, not observed in a game).

frr7 (mirror:1:2 and asym:23:2, the economy worker's af5 = V29 + attack_from=5 (the accompanying artifacts, chosen by
its rule 18.22 at 22:43Z for fresh validation) against best_v9e, best_v9f, v41, V29, g1, AS1C and v48, 28 games,
the accompanying artifacts, 23:20:46Z to 23:37:28Z; 0 rejected actions, 0 bot errors): af5 is 13-4-11. On
mirror:1:2 it beats AS1C, best_v9e and best_v9f by 2660, draws g1 and V29 at round 50 and loses to v41 and v48 by
15 at round 50, in both seats. On asym:23:2, against the five bots other than v41 and v48, af5 wins in seat 0 (by
1250 at round 14 against each of the five) and loses in seat 1 (by 1250 at round 14 against g1 and V29, by 4470 at round 21 against the
three main-agent bots; margins corrected after the validation worker's check, the accompanying artifacts, 23:42:10Z); it beats v41 in both seats (+2218, +3215) and loses to v48 in both (-9822 in seat 0, -2385 in seat 1). Every one of
the 20 games against the five bots other than V29 and g1 has V29's and g1's winner, HP difference and length in
frr2 and frr6, and the 8 games against V29 and g1 have the results of g1 against V29 in the same seat
(the accompanying artifacts). On these two starts attack_from=5 therefore changes no recorded result (winner, HP difference
and length; this comparison does not compare action histories, but the validation worker found equal full histories for each
comparator's 24 matched games, 20 matched to both and 28 in the union, the accompanying artifacts, 00:10:17Z), as the economy worker found
for attack_from=7 (g1) on every scenario start it tested (the accompanying artifacts, entry 18.8, 18.19, 18.31). Slowest calls: af5
8.62 s, V29 3.52 s, g1 3.38 s, best_v9f 2.39 s, best_v9e 2.34 s, AS1C 2.19 s, v41 1.30 s, v48 1.19 s.

frr8 (standard start, af5 against v48, 2 games, 23:37:28Z to 23:41:54Z; 0 rejected actions, 0 bot errors): af5
beats v48 by 55 at round 50 in both seats, which is g1's result against v48 (frr5) and v46 (frr3); V29 loses that
pair by 5. The economy worker's afrr (the accompanying artifacts, entry 18.34, 23:20Z to about 23:37Z) played af5 against the
ten frr1 bots on the standard start: af5 is 16-0-4, with one outcome per opponent in both seats. It beats
best_v9e, best_v9f and af2g by 410, v41 by 55, guard00 by 2, V29 by 7 and g1 by 31 at round 50 and
threat_defender at round 11, and loses to P5TNUBM and AS1C by 10; the economy worker's afrep, two new games of af5 against best_v9e
after afrr (a reproduction run, not an engine replay of a log), repeats the seat-0 log of that game event for event. In the frr1 matrix the best record is guard00's 16-0-2 against nine
bots. The proposition of this section is for the ten-bot frr1 matrix only. Each of its max-min mixtures scores at
most -1/3 against af5 (af5 beats g1, guard00 and best_v9f; of the mixture's bots only AS1C and P5TNUBM beat it), so
none is max-min in the eleven-bot matrix with af5 added (diagonal 0 by symmetry, value 0). In that matrix (frr1
plus afrr, analyzed from the two files concatenated in the accompanying artifacts; linear programming, with the found mixture checked
in exact fractions; the validation worker's conditional proof is cited below) the max-min mixtures put 1/3 on af5, 1/3 on guard00 and the remaining 1/3
on P5TNUBM and AS1C in any split; all seven remaining policies, among them g1 and best_v9e, get weight 0. The self-play entries are set, not
measured, and v46 and v48 are not in it. The validation worker confirmed this result conditional on the finite table and its
zero diagonal (the accompanying artifacts, 23:56:59Z):
every old ten-policy max-min mixture gives af5 the payoff 1/3 plus twice its best_v9f weight, and the two fortress
rows still get weight 0 for any values in [-1, 1] of the unmeasured af5-against-fortress entries and any
antisymmetric entry between the two fortresses. It is not a statement about all policies, HP objectives or clock
invariance.

### 5.17 Terminal reserved pool D (the validation worker, report-only)

The validation worker ran best_v9e (sha256 70ef8eab...a2fd87, the hash named in the 19:50Z selection record in the accompanying artifacts) once on its reserved
pool D (records in the accompanying artifacts, 23:19:17Z to 23:28:50Z; empirical). The 16 opponent parameter settings and the two
prescribed histories were declared at 18:11:52Z. They come from known implementation families (counters such as
guard_geometry among them) and were designed after earlier development results, so pool D is not a random sample of
opponents. The games started at 23:00:03Z and the last primary game finished at 23:11:44Z. Pool D reports the fixed
choice; it is not used to choose or revise a bot, and the delivered bot was not changed after it.

| Start | W-D-L | Seat 0 | Seat 1 | Worst HP difference | Slowest timed call (wrapper) |
| --- | --- | --- | --- | ---: | ---: |
| standard | 26-6-0 | 13-3-0 | 13-3-0 | 0 | 0.73 s |
| asym_130363_2 (prescribed two-round prefix for each side) | 28-0-4 | 14-0-2 | 14-0-2 | -3905 | 2.82 s |
| mirror_104729_3 | 32-0-0 | 16-0-0 | 16-0-0 | +360 | 1.23 s |

The 96 games have 44 distinct canonical histories (standard 15, mirror_104729_3 14, asym_130363_2 15) and all 48 seat pairs give identical
histories, so the deterministic repeats are reproducibility checks, not further evidence. There was no bot error,
rejected action or source drift; every game replays on a fresh original engine, and fresh processes reproduce the
1532 candidate decisions through both entry points. The timing wrapper also covers the prescribed turns, so the
slowest call is a wrapper measurement. The validation worker's checks after pool D (23:27:52Z, the accompanying artifacts)
found the 95 source pins, the original tests (59 run, 9 skipped, no failure) and the protected tree unchanged
relative to the starting state.

The four losses are asym_130363_2 against two guard_geometry settings (job 12: roster tier1 x3, gun at (8,2); job 13: roster tier2, tier1, gun at (9,3)), both
seats. The two settings differ only in round-one branches that the prescribed prefix skips, so all four games have
the same history: round 35, HP -3120:785. The validation worker's accounting (the accompanying artifacts,
CONFIRMED for the recorded accounting): in round 35 best_v9e buys only 400 factories (8000 gold) and keeps 1,096,319
gold before income, while the guard buys 281 tier5 and 20 factories (183,050 gold); 28 base hits deal 3920. The
replay reading in the accompanying artifacts adds: the prefix puts walls on best_v9e's map that it did
not ask for, so by its foreign-map rule econ20 plays from round 3. Its route stays at 22 steps throughout (the
guard's reaches 44 at round 9), it builds 48 turrets by round 19 and none afterwards, and its tier5 attacks (14 in round 13, 8 in
round 14, 300 in round 22) never reduce the guard's 785 HP. From round 23 on it buys only the 400 factories per
round that fac_cap allows, while the guard's gold grows from 26,696 at the end of round 20 to 183,062 at the end of
round 34 (balances visible to the decisions of rounds 21 and 35). The validation worker checked this reading against all 72 records
(the accompanying artifacts, 23:36:39Z).
Whether another decision (for example spending the unspent gold on minions or turrets before round 35) would save
the game is an open question: no game was run to test it, and pool D is not used to revise the bot.

## 6. Known failures

- Hoarding guard after a prescribed prefix (pool D, section 5.17). On asym_130363_2 against the validation worker's guard_geometry
  continuation, best_v9e's econ20 handoff keeps a 22-step route, builds no turret after round 19 and from round 23
  buys only capped factories, with 1.1 million gold unspent before round 35, while the guard hoards visible gold and
  spends 183,050 of it on 281 tier5 in round 35 (-3120:785, both seats, two settings). It wins the pool's other 28
  asymmetric games.
- Passive growers (best_v9b and best_v9e; section 5.11). Against an opponent that only buys factories through
  round 4 to 9 and then all-gold tier5, a round-2 bait, a maze or the opponent's large gold makes rule 3 buy
  insurance in rounds 2-4; with 12 to 18 factories against 26 to 31 the persistent tier5 entries win (best_v9e's twin
  loses 76 of 142 GROWERS, 78 of 144 GUARDED_MAZE and 26 of 140 STAGED development games). The revision P5TNUBM
  wins all 426, but it loses the early strikes of the next item, so it was not installed. best_v9f wins most of
  them (sections 5.12, 5.14) and the economy worker's growth-first g0 and g1 win all GROWERS and GUARDED_MAZE games (section
  5.15); each of those loses other conditions.
- Early strikes inside a passive window (the reverse side of the item above; P5TNUBM and P4TNUB, section 5.11). A
  policy that buys no insurance in rounds 2-4 loses budget_timing strikes with tier1 or tier2 in rounds 3-4 and tier3
  in round 4 (-24 to -50) and the defence worker's fortress v32 (one tier2 in round 4, -7). Every tested change of the window
  (P4TNUB ends it one round earlier; M2, M3, M4, v31 and v32 buy tier1-tier3 insurance inside it) lost
  economic timing policy (-37 or -90) or growers (down to -1105). None of those tested passive-window settings holds both families.
- Rejected candidates (sections 5.12, 5.13). best_v9f (V33C) loses pool C's C-08 (budget_timing tier3 in round 4
  with 0.65 of its gold, 774:800) and C-11 (guard_geometry with one tier2 at (10,2), 788:790), TIMING2 tier3 in
  round 4 (-26), every guard_handoff with the handoff in rounds 10-12 (18 games, down to -375) and the economy worker's
  economic timing policy all-in of round 7 (-35); V33M also loses economic timing policy (-37), econ13 and econ15 (-16).
- Locked draws (best_v9e). Against strikers that keep a defended map and against guards, best_v9e often holds but
  does not win: budget_timing with all or 0.65 of its gold (pool C C-08 and C-09 800:800; TIMING 12 draws, TIMING2
  34 draws) and guard_geometry with one tier1 (C-10, 795:795). Both maps lock (P2) before any of our attacks lands.
- Early walls with a round-3 guard (the validation worker, development counter, 18:17Z). guard00 (walls in round 1, a guard turret in
  round 3, one tier4 in round 4, then frozen fortress v38) wins 770:740 against best_v9e,
  V33C and P5TNUBM and 780:740 against fortress v41, both seats; seven other walls-and-guard settings lose every
  such game, and guard00 itself loses 4 of 90 development target conditions (section 5.15).
- Delayed walls with a reserved round-4 purchase (the validation worker, development counter built after the selection, 21:19Z).
  Q (the accompanying artifacts) places guard00's walls in round 2 instead of round 1 and withholds two of
  its round-3 factories, so it enters round 4 with 264 gold and 11 factories and buys one tier4 (cost 260). It
  beats best_v9e and AS1C 770:740 at round 50 in both seats. The same counter without the reservation (P) has 254
  gold entering round 4 and loses 770:800 to both. Evidence: the accompanying artifacts. The validation worker also built bots that choose between two counters from the
  public opening and counters that beat those selectors in turn; this is evidence about selection from the
  opening, not about best_v9e's strength on a pool (the accompanying artifacts). In protocol 160 (22:08Z) Q and the late variant S (walls in round 3, two factories
  reserved for a round-4 tier4) each beat the defence worker's fortress v44 and v45, V29, the economy worker's V31 with attack_from=7 and
  fill_own=true, and AS1C, and lose to g1 and to the handoff counter H (hp_handoff, growth 6, handoff from round 8),
  in both seats (the accompanying artifacts). A selector T that waits through round 3 and chooses between two
  continuations at round 4 beats H 800:656 and draws S 740:740; the same bot with that choice fixed to one of the
  two continuations (U) loses to S at round 12 (base HP -246 against 800) (protocols 161 and 162, the accompanying artifacts).
  The validation worker's next counter V (guard00's walls and a splash in round 4, one tier4 in round 5) beats T and U at round 12
  (800 against -546) and loses to G (680:740) and to best_v9e and AS1C (755:800 at round 50), in both seats
  (protocol 163, the accompanying artifacts, 22:40Z). The validation worker's summary of the whole
  chain is in the accompanying artifacts.
- Scripted continuations against the teammates' bots (section 5.15): fortress v41 (the defence worker's final recommendation
  until 20:32Z) wins mirror:1:2 (+1555, both
  seats) and asym:3:2 in one seat (+1255); the defence worker's v46 and its final v48 win 7 of the same ten games, including
  mirror:22:3 in both seats (+2940); the economy worker's V29 wins 15 of 24 games on twelve scripted starts. In frr4 (section
  5.16) v46 also beats AS1C and best_v9f on mirror:1:2 and asym:23:2 in both seats, as it beats best_v9e.
- Same history, opposite answers (best_v9e and af2g; section 5.14). Two guarded_maze opponents on the empty layout
  with a round-2 tier1 bait (growth 4 with the guard in round 3, and growth 5 with the guard in round 4) leave the
  same state after round 2, so each bot makes the same round-3 purchase against both. best_v9e's purchase (a splash
  and two factories) wins the first by 305 and its twin loses the second by 1080; af2g's (five factories) loses the
  first by 815 and wins the second by 936. The economy worker's growth-first g1, which keeps more factories in rounds 1-3, wins
  both with one round-3 purchase, so the pair defeats these two bots, not every bot (that their smaller early
  factory count is the cause is a conjecture).
- Round-2 blind strikes (best_v9e and the earlier tested variants V18FT, P4TNUB, P5TNUBM and af2g). budget_timing
  with tier1 or tier2 in round 2 (half budget) wins by 20 and 12 (TIMING2, tm2). Round-2 purchases are not visible
  when we decide round 2, but that alone does not decide these games: AS1C, g0, g1, V29 and af5 win all 40 TIMING2
  conditions (sections 5.14, 5.15; the validation worker, the accompanying artifacts, 23:52:32Z).
- Disclosed counters that beat best_v9e (the validation worker, section 5.11): the growth 6 grower with a defender from round 10 or
  12 (H10, H12: 520:755; P5TNU and P5TNUB also lose H10, P5TNUBM wins it), the growth handoff without strike at round
  8 (755:660) and the guarded round-4 strike (gun1 at (10,1) plus one tier4, 755:740). Each of them loses to other targets, and in the validation worker's four-policy
  counter game no policy beats all three others (section 5.11).
- Exact forecasters. The tested counters that forecast the deterministic policy, buy an attack that
  leaks for one round and keep their own defence successful afterwards preserve that early advantage
  in the recorded games (sections 4.2, 5.3); none of our later attacks lands against an opponent that
  insures every round. Exact forecasting alone does not guarantee such a win: the counter must also
  survive and keep the final HP comparison in its favour (wording after the validation worker's 06:47Z review). Lowering the thresholds that would
  close a given gap (big_threat 50, spec_share 0.8 or 1.0) lost larger amounts to later floods in
  the screens of section 4.2.
- Growth paths with late heavy waves (best_v9a; section 5.4, 5.5). Gun insurance bought in rounds
  3-7 against a bot that keeps its gold leaves the next, larger tier5 wave unaffordable, and
  best_v9a then buys nothing against it. In the validation worker's controlled ablation the turret mode of the poke
  fallback did not change any listed outcome, so the turret condition is not the cause in those games;
  the ablation does not establish a claim about all openings or turrets.
- Below-threshold waves. A guarded tier4 in round 5 deals 60, below big_threat=100, and its zero-leak
  plan costs more than 0.6 of our gold, so best_v9a lets it through (735:800). The same holds for C2's
  26-HP tier3 against econ13/econ15.
- Cheap guards. A gun1 at (3,1) in round 1 stops the round-1 poke and lets the opponent's own tier1
  land (795:800 for cheap guard + economy13 or economy15). best_v9b draws these at 0 (c8m), but
  the validation worker's model-free counters against the actual best_v9b entry point (the accompanying artifacts, 20 conditions, both seats, replayed on the unchanged
  engine) win with a gun1 at (10,1) plus one tier1, two tier1 or one tier2 in round 1 (800:795, 800:790,
  800:788): the gun kills our three round-1 tier1, the counter's minions land, it then buys only
  factories in rounds 2-5 and both maps lock before our first attack (round 6) can land. The same
  20 conditions give the counter 8W-8D-4L; the other counter win is the half-budget tier3 in round 3
  (800:774, H9a in section 5.10).
- Fortress-trigger lag (best_v9b; section 5.7). After the trigger the insurance is splash-only; a
  one-round all-gold tier5 purchase that arrives while S < 1500 deals 140 per leaking copy
  (forecast_timing attack_round 8: -125; the C2 settings without the trigger: +15).
- Unseen round-2 pokes (C2 family including best_v9b). Purchases of round 2 are not visible when we
  decide round 2, and the poke fallback runs only while the opponent owns a turret or shows a tier1/tier2
  entry bought in round 2 or later; economy v4 late_round=6 phi=0 gains 45 HP this way (c5d, c8m).
- Scripted openings (section 5.8). With buildings the bot did not choose, best_v9b hands the match to
  econ17, which still loses ten of 88 sc1 conditions: to economy15 leak (four), to fortress v19 and v22
  under mirror:22:3 (four), to eco6_t5 under asym:23:2 in seat 1 and to econ17 itself under asym:3:2 in
  seat 0. The scripted walls block the master layout, the route stays short and S stays low.
- Round 1 is blind. This is a statement about the round-1 exchange only, not about the complete game: the
  earlier versions' two round-1 tier1 (best_v9a and the C2 family) deal at most 10 HP, so they lose the round-1
  exchange to any round-1 purchase that deals more than 10 HP (the validation worker proved at most 32 for 100 gold against a map
  with no damaging turret). best_v9e sends three tier1 (at most 15 HP), and a round-1 gun1 at (10,1) stops them
  (the model-free counters above).
- Sampled rosters (rule 3; the validation worker, 20:09Z and 20:15Z). In rounds 2-6 of the 24 retained standard-start pool C
  histories, at the 100 reached states where the opponent had at most 250 gold, the validation worker enumerated every affordable
  ordered purchase with the unchanged engine (13658 interventions). In 6 states the worst affordable purchase deals
  more than the worst sampled one, and in 2 states best_v9e's map stops every sampled list but not every affordable
  one. Example: C02 round 6, where all sampled purchases deal 0 and the omitted order (tier2, tier2, tier3; 180 of
  190 gold) deals 26. The validation worker compared three roster orders (this one and two
  others), each followed by one of three fixed continuations, in both seats (18 complete games). The 12 games with
  the other two orders all lose; the 6 with the omitted order lose 4 and draw 2, and the two draws (774:774) are the
  frozen fortress v38 continuation, which loses 774:800 with the other orders (counter's HP first). So the omission turns best_v9e's win into a draw in that
  continuation, in both seats, and changes no other of these outcomes.
  The validation worker then added five walls to the counter's round 6 (in that state no set of at most four added walls stops
  the return hit while keeping the 180-gold attack; exhaustive over 14901218 wall sets, the accompanying artifacts).
  With the fortress v38 continuation this counter beats best_v9e
  800:774 at round 50 in both seats; with the other two continuations it still loses (rounds 12 to 14). It is a
  counter built after the selection against the fixed best_v9e, so it shows a concrete loss, not a measure of
  strength on any pool. Against AS1C and AS1 (section 5.14) it loses 380:774 in both seats, and none of the validation worker's
  stronger fixed continuations beats AS1C. Evidence: the accompanying artifacts.
- The planner is the defence worker's frozen v7 module, which finds plans "as cheaply as found" (restricted wall
  prefixes, greedy splash and gun additions); "cheapest" in the decision rules means the cheapest plan
  the planner finds, not a proved optimum (the validation worker, 06:21Z).

## 7. Runtime

The bundled runner and action-collection protocol impose no time limit on `decide`. All
main-agent runs use `taskset -c 20,21 nice -n 19` on a shared machine, with two tournament workers until
08:15Z on 2026-10-31 and from then on two queues of one worker each (the accompanying artifacts); the
times below are wall-clock measurements of those processes, not portable bounds.
- Slowest single `decide` call (computed over every recorded call of the candidate settings):
  c5a 3.96 s without gun_cap and 2.6 s with it (c5a-c5c); c6a 2.80 s; t1 2.42 s; t2 2.17 s; c8m (V17,
  the development twin of best_v9b) 6.84 s; sc1 (scripted openings, where the econ17 policy plays)
  11.35 s.
- The validation worker's pool-B campaign for best_v9b: largest candidate call 0.66 s on the standard start, 1.27 s
  and 4.97 s after the two prefix families; largest candidate total per game 5.83 s.
- The validation worker measured a largest candidate call of 11.07 s and a largest per-game candidate total of
  82.35 s for best_v9a on its targeted set (the accompanying artifacts, 06:24Z), and two pool-A mirror games
  of best_v9a exceeded its 300-second per-game limit before completing within 500 seconds.
- Section 5.11 runs (computed over every recorded call): V18FT 0.80 s on f5t (c9i) and 3.32 s on
  TARGETED3_P5TF (t9k); frozen best_v9e 0.88 s on f5t (ab1); P5TNUBM 1.26 s (c9q), 3.16 s (t9j) and 1.47 s
  (t8i); V33C 1.35 s on f5t (x33f) and 1.72 s on TIMING2 (x33tm2); the ablated variants of best_v9e up
  to 1.54 s (ab7). The slowest calls come from the rule-3 plan search against several threat
  compositions; the grower and scripted-opening pools stay below 0.51 s.
- Sections 5.12-5.13 runs: frozen best_v9e 0.93 s on TIMING (bse_tm), 1.16 s on SCREENED (bse_sg) and 0.77 s on
  HANDOFF (bse_hd); V33C 0.64 s to 0.83 s on the grower, guarded-maze, staged and handoff pools (x33g, x33gm,
  x33st, x33hd); frozen best_v9f 0.56 s on STRIKE1 (x9fs1).
- Section 5.14 runs: best_v9e's options on TIMING2 (tsc) up to 1.42 s; AS1C up to 8.88 s (h14t3, against
  the validation worker's guarded_adaptive_continuation, while the machine load average was about 155; best_v9e's twin's slowest
  call on that pool is 3.32 s, t9k) and at most 1.53 s on the other 13 R13 pools; the shares 0.75 and 0.65 up to
  1.07 s; the ablations ab14-ab17 up to 0.46 s; the five fk1 candidates up to 0.47 s.
- The validation worker's pool C timings are outer-wrapper measurements (wall time on low-priority shared cores; the wrapper
  also times the prescribed prefix turns, which copy scripted actions without calling the candidate). Largest
  timed candidate-wrapper call, standard / mirror_7493_3 / asym_8669_2 start, and largest total wrapper time per
  match: best_v9e 0.868 / 0.653 / 1.052 s and 11.81 s; best_v9f 1.166 / 1.113 / 0.760 s and 11.82 s. The actual
  policy calls number 1104 (best_v9e) and 1088 (best_v9f); details in the accompanying artifacts. The defence worker reports at most 3.93 s per call for fortress v41.
- Decision time grows with the opponent's gold. Against the defence worker's fortress with factory_cap 1200 (v44's setting)
  on the standard start the opponent holds 12,149,100 gold before round 50, and best_v9e's slowest call in the defence worker's
  run x202a is 8.13 s (round 50; the game took 100 s, against 42 s with cap 400; the accompanying artifacts, 20:04Z and the
  20:22Z correction that the call is best_v9e's). Rule 3 builds its sampled roster lists from the opponent's
  visible gold (longest list = the opponent's active entries + floor(gold / 15), 809,940 at round 50) and the
  planner then evaluates them by exact simulation, although the own map is already splash-immune (S = 1550).
  The validation worker regenerated all 100 decisions of two retained x202a histories with fresh calls (identical actions; slowest
  6.77 s wall and 6.72 s CPU, round 50) and timed the parts: building the lists takes about 0.027 s, the sampled-leak
  evaluation alone 6.35 s CPU, and it returns 0 (the accompanying artifacts,
  the follow-up analysis). A variant that skips this evaluation on an immune map
  (the accompanying artifacts, research only, not installed) gave the same actions and states on 74
  retained histories, with at most 0.30 s CPU per call on the two high-factory histories and at most 0.84 s over all
  74 (1,204 calls; these paired measurements include an untimed eligibility check and shared caches; the validation worker,
  the accompanying artifacts, 22:46Z). The bundled runner has no time limit, so no recorded game was cut off by it, but a
  50-round match against an opponent that hoards gold takes minutes instead of seconds.
- Section 5.16 runs: in frr1 and frr2 the slowest call of any bot is 4.57 s (af2g, frr1); best_v9e's is 2.70 s
  (frr1) and 2.78 s (frr2). In frr3, against the defence worker's v46 on the standard start, the opponents' slowest calls are
  g1 10.72 s, P5TNUBM 10.07 s, best_v9e 7.83 s, V29 7.67 s, af2g 7.35 s, AS1C 6.81 s and best_v9f 6.46 s (v46
  itself 2.35 s); the 50-round games took 92 s to 132 s against the main-agent bots and 120 s to 141 s against g1 and V29,
  and 30 s against v41 and 23 s against guard00. The defence worker's the defence worker's earlier v46 run records
  6.70 s for best_v9e in the same game; in frr5, against v48, P5TNUBM's slowest call is 14.03 s (10.07 s against
  v46) with the same 20 outcomes as frr3. On the scripted starts the slowest calls are V29 8.71 s and g1 8.60 s
  against v46 (frr4), g1 9.58 s and V29 9.02 s against v48 (frr6) and af5 8.62 s (frr7), all in mirror:1:2 games
  that end at round 50. In the economy worker's afrr (standard start) af5's slowest call is 3.07 s, in seat 1 against g1
  (the validation worker, the accompanying artifacts, 23:46:34Z). Long games against the fortresses reach large visible gold and rosters, whose planning
  cost the previous item measured. That cost does not explain the difference between frr3 and frr5 (P5TNUBM
  10.07 s against 14.03 s): those games have identical histories and therefore identical gold, so it is variability
  between runs with equal histories, of unmeasured cause (the validation worker, the accompanying artifacts, 23:32:10Z). best_v9e's planner has no
  wall-clock cutoff, so its own actions do not depend on these times. v41, v46 and v48 keep the three-second
  gun-planning cutoff of the last paragraph; its deadline is measured (with time.time) from the start of the
  planning function inside the same decision call, and the harness times the whole call (with perf_counter). Every
  observed call of v41, v46 and v48 in frr1 to frr7 was shorter than three seconds (slowest v41 2.47 s in frr2, v46
  2.35 s in frr3, v48 2.25 s in frr5; at most 2.00 s in frr4, frr6 and frr7). With consistent clock progression this supports that their three-second
  deadline was not reached in these recorded games; it does not establish invariance under a different load, where
  a slower execution can cross the deadline and take another branch (the validation worker, the accompanying artifacts, 23:23Z). In the
  frozen files of v41, v46 and v48 the only other clock read is the annealing budget of the replanner in the accompanying artifacts, which their
  fortress module calls without a budget.
- From about 07:10Z the machine load average was above 100 (processes of other users), and the same
  matches took three to five times longer than before.

The normal branch's planner runs without a wall-clock cutoff, and the foreign-map branch's deadline is one
million seconds (never reached), so the actions do not depend on the machine speed in the recorded runs;
the cost is that a slow machine makes games slow rather than different. Some opponents (the defence worker's fortress
v26-v28 and v34-v48, including the former final v41, v43, the final recommendations v46 (frr3, frr4) and v48
(frr5, frr6), F34, F35 and the validation worker's guard-handoff bots) keep a three-second gun-planning cutoff
(`TIME_BUDGET = 3.0`, checked in the frozen files of v41 and v43 to v48); equal seat
histories against them do not prove load independence.

## 8. Reproduction

The accompanying artifacts provide exact commands for the smoke game, tests, integrity checks, tournaments,
per-game comparisons, traces and finite-matrix calculations. The commands require the original unchanged game
project and its existing Python environment. Each replay command needs a fresh output name.

Some intermediate inputs and most per-game replays were omitted before publication. Retained scripts and
summaries support inspection of the included results, but some archived analysis and freeze commands depend on
omitted inputs and cannot be run unchanged from this bundle. The accompanying artifacts document these limits.
Repeated conditions add no independent evidence; opponents with a wall-clock planning cutoff can take different
branches under a different machine load (section 7).

## 9. Integrity

The accompanying artifacts record the starting state before any work: 1002 manifest entries absent from the
working copy (999 game JSONL files, the historical-record manifest, filesystem metadata and viewer metadata, as
itemized by the validation worker) and three hash mismatches (the combat implementation, the engine tests and the
rule tests). The project's existing tests ran 59 with 9 skipped. These differences were recorded, not repaired.
The validation worker's 06:14Z checkpoint found the integrity result unchanged, as did the checkpoints at
19:05:48Z (903 entries outside the research artifacts) and 19:10:20Z (59 tests run, 9 skipped). The checks after
pool D (23:27:52Z) found the 903 protected entries, the 1002 absent entries and the three changed hashes unchanged.

The end-of-run checks started at 2026-10-31T23:42:01Z after the last experiment queue and finished at 23:43:04Z;
every step was pinned with `taskset -c 20,21 nice -n 19`. The accompanying artifacts retain these records:

- The delivered bot has sha256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 and the final-bot tests
  have sha256 07ec39bb28f9daa245741bfe2d852c105f35b3e035f53b7b744377a822e19010, unchanged before and after the checks.
- Smoke game: the first smoke replay (02:26Z) was preserved, and the documented command generated another replay
  with the installed bot: player 0 wins in 8 rounds (base_destroyed), HP 800 against -5.
- The integrity checks before and after the tests produced identical records: `identical_to_baseline` true with
  no differences; 1041 manifest entries, 1002 absent (1000 historical-record entries, filesystem metadata and viewer
  metadata); the three changed hashes belong to the combat implementation, engine tests and rule tests. There are
  40 files outside the research artifacts and the pre-existing environment (the check excludes both collections;
  the validation worker's 903-entry checkpoints include the pre-existing environment). The one extra entry outside
  them is the task prompt, which is part of the baseline. No change relative to the starting state.
- The project's existing tests: 59 run, 9 skipped, OK. The research tests: 18 run, OK.
- The outputs contain no absolute local path.
- The integrity check after the final report edits (2026-11-01T00:06:39Z to 00:06:49Z, same command and pinning)
  again reported `identical_to_baseline` true with no differences. Its record equals the second integrity record
  in the accompanying artifacts; the delivered bot and final-bot tests still have the hashes above.

Publication record (2026-11-01, after the team stop; no new research games):

- The smoke command was run once more from the original project root with a fresh output name at
  2026-11-01T00:16:50Z, pinned as above: exit status 0, player 0 wins in 8 rounds (base_destroyed), HP 800 against -5,
  0.32 s wall time for the whole process.
- The last integrity check (2026-11-01T00:28:00Z) reported `identical_to_baseline` true with no differences. Its record
  is byte-identical to the third integrity record in the accompanying artifacts. The delivered bot and final-bot
  tests keep the hashes above; the protected-file manifest was unchanged before and after publication preparation
  (sha256 63472591f7bb83e4cecbfd0e83bed4755c1f6382ef0399640d849241334ba19c).
- Temporary working files were removed, and most per-game replays and bulky intermediate evidence were omitted.
  The accompanying artifacts record these omissions. Every retained text file was checked for absolute local paths;
  none were found. The frozen-bot checksums still verify.
