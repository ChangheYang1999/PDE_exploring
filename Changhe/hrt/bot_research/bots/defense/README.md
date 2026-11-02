# bots/defense (lane hrt-w1): defensive planning component and the fortress bot

- `plan.py`: `plan_defense(observation, budget, required_hp=None, threat_types=None, *, allow_guns=True, layout=LAYOUT,
  partial="best", time_budget=None)` and helpers (`threat_compositions`, `plan_walls`, `defense_cost`, `opponent_leak`,
  `threat_damage`, `robust_leak`, `layout_by_name`, `MasterLayout`). Exact planning on the engine's own route and a
  verified replica of its combat; see the module docstring and bot_research/notes/defense.md.
- `simulate.py`: exact one-map replay with leaked-HP tally (checked against td_game.combat.simulate_map).
- `geometry.py`: routes, splash adjacency, serpentine helpers. `templates.py`: WALLS/SLOTS pairs for slot defenders.
- `fortress.py`: the bot, `make(**options)` (docstring lists every option); `decide` = default options.
- `counter_earlygun.py`: a test opponent (reproduction of a review finding), not a candidate.
- `frozen/vN/`: snapshots used by the tournaments (README.md inside).

Reproduction (from the project root; PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp"):

    .venv/bin/python -B -m bot_research.experiments.defense.check_plan 200
    .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.defense.frozen.v41.fortress:decide \
        --bot-b td_bots.protocol:idle --output bot_research/runs/defense/<new-name>.jsonl
    .venv/bin/python -B -m bot_research.harness.tournament --name <name> --out-dir bot_research/runs/defense/<name> \
        --candidates bot_research.bots.defense.frozen.v41.fortress:@make \
        --opponents $(cat bot_research/experiments/economy/opponents_tuning.txt) --scenarios none asym:3:2 --jobs 3

Note: every fortress.py (live and frozen) exposes both `make(**options)` and a plain `decide(observation)` that calls
`make()` with the defaults; the runner's `module:decide` form and the harness's `module:@make?k=v` form both work.

Shift 2 (2026-10-31, 07:57Z-13:57Z): the recommended artifact is frozen v34 (`bot_research.bots.defense.frozen.v34.fortress:@make`; attack_share 0.25 plus the fifth review fixes; v33 = the same without the fixes, v32 = 0.35, v29 = 0.7);
see frozen/README.md for the version table and notes/defense.md (entries from 08:10Z, summary at 11:13Z, recommendation with
hashes at 12:43Z). New modules: replan.py (layout re-planner for scripted-opening maps), counter_astra28.py and counter_astra33.py (fixed schedules
from astra's reviews; the second beats every fortress version by 600-745). The live fortress.py equals v34 plus switched-off options (eco_match, replan_every, guard_insure).

Shift 3 (2026-10-31, 13:57Z-): the recommended artifact is frozen v41 (`bot_research.bots.defense.frozen.v41.fortress:@make`
= v34 with eco_match=True, eco_match_ratio=1.0, race_kill=True (with the sixth review's fixes), eco_match_insure_cap=200,
covered_fix=True and lethal_share=0.3; notes/defense.md 17:21Z with hashes and the decision rules; v40 (17:06Z, lethal 0.4) is the
same policy with larger striker margins; v43 (18:30Z, insurance cap 260) wins the model-free early strikers (timing, round-6
tier4) but loses two exact-forecaster timings; v42 (planner gun-pass fix) was rejected; v38 (15:52Z, ratio 1.5) is the alternative for pools of
answering economy bots, early strikers and exact forecasters; v36 (14:50Z) is v38 without the cap and the fixes; v34 is the poking
insurer for opponent sets without model-free strikers; v37 (pre-strike insurance) is rejected but kept as evidence; v39 = v38 + lethal_share 0.3 + covered_fix is the
alternative with smaller worst cases against the handoff strikers and astra's schedules A/C at the price of two H11 wins, one
tuning win and one scripted draw, notes 16:36Z). Test bots counter_astra37.py (hoarders) and counter_astra38.py (A-D) reproduce
astra's seventh and eighth reviews. New options in the live module (all off by default, so the live module still plays as v34):
eco_match_pokes and poke_min_frac (pokes while out-grown; rejected, x129/x132), race_kill (adopted in v36, fixed in v37/v38),
big_threat_prestrike (rejected, v37) and eco_match_insure_cap (adopted in v38). Test bots added: counter_astra37.py (hoarders);
counter_earlygun.py gained tier/guard_round/gun_cell options (defaults unchanged). Measurements
of the shift: x128-x138 (notes 14:08Z-14:50Z): the fortress family beats the lead's whole GROWERS pool (142-0-0 for v34 and
v36), v36 beats hrt-w3's staged/screened guards and the handoff strikers except H10 (and growth 5 H11).

Shift 4 (2026-10-31, 19:50Z-): the recommended artifact is frozen v48 (`bot_research.bots.defense.frozen.v48.fortress:@make`
= v41 with factory_cap=1200, finish_wrap, finish_robust_gold 400, finish_gun_check 12 (gate on the whole roster), finish_defend_first
(smallest passing kill reserved, the capacity rule spending the whole slack) and the finish cache; notes/defense.md 22:39Z with hashes;
v46 (21:45Z) gives the same results with two constructed defects, v44 = v41 + factory_cap 1200 (notes 20:32Z) is the alternative where
action-list size matters, v41 the one with the 40-factory cap). The per-round factory limit (formerly the constant
MAX_FACTORIES_PER_ROUND = 40, a practical limit shared by every research bot, not an engine rule) is now the option factory_cap; with
1200 the late economy compounds and the capacity races on the obstructed scripted openings against econ20-based bots (best_v9e, V29,
V25RM) turn from losses into draws or wins while every regression pool stays equal to v41 by W-D-L. New options in the live module (off
by default): factory_cap (40), finish_wrap (the roster-padding finish candidate of plan.wrap_bundles inside the finish rule, astra review
10: a verified kill of best_v9e at round 18 of the mirror:22:3 game where the plain floods landed nothing) and finish_robust_gold (the
finish rule's opponent-response check also for small floods against rich turret owners); plan.py flag GUN_CANDIDATES_LEGAL_FIRST
(legality before the top-8 truncation of gun candidates, off). v45 = v44 + finish_wrap + finish_robust_gold 400 (frozen 20:54Z) is the documented alternative that wins the capacity races against
best_v9e (7W-1D-2L against 3W-3D-4L) but turns two scripted wins into same-round draws (notes 21:18Z: the finish-first branch bought the
padded kill with everything in a round whose worst-case flood looked lethal, skipping the capacity rule's 1700-gold defence). v46 = v45 +
finish_gun_check 12 (one-gun3 veto for finishes above the planner's 120-entry gun-pass limit) + finish_defend_first (defence first, the
kill with the remainder) + a per-decision cache of the finish simulations passed the full regression (at least v44 everywhere, better
against best_v9e, on the scripted pool and on the forecaster) and is the recommendation; astra review 12 found two constructed defects
(gun-check gate counting purchases instead of the whole roster; the fall-through losing a kill-or-be-killed draw when defence spending
removes the only kill) that v47 fixes (frozen 21:47Z; every pool equal to v46 except one scripted win turned into a same-round draw, so v46 stays); v48 = v47 +
the capacity rule spending the whole slack under a reserve (frozen 22:10Z) passed the full regression (at least v46 on every pool, the
scripted draw a win again) and is the recommendation. Replay check of its finish rule: experiments/defense/check_v48_x222.py (3 s, exit 0).
