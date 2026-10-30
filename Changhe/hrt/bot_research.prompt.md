This is an authorized development and debugging task, not an interview.
Read the active root AGENTS.md first. Its debug-mode rules authorize autonomous
strategy research and multi-agent collaboration. The archived
bot_research/AGENTS.interview.md is not an active instruction file.

Your objective is to discover, implement, and rigorously evaluate the strongest
game-playing bots you can produce under the current, unchanged game rules.
Do actual research, implementation, and experiments; do not stop at a plan.

Use thorough reasoning and substantial experimental effort. Use multiple agents
in parallel up to the concurrency limit actually available. Do not claim to
change a model setting or start workers unless that action actually happened.

1. Keep the original project immutable.

All new or modified project files must be inside bot_research/. Do not edit
AGENTS.md, the engine, game settings, bot adapter, viewer, original tests,
datasets, notebooks, packaging configuration, or other existing files. Do not
patch, copy-and-modify, or monkey-patch the engine to improve results.

Use bots/ for candidate and final bots, experiments/ for evaluation and search,
tests/ for new research tests, runs/ for replay logs and result tables, reports/
for findings, and tmp/ for temporary files, all under bot_research/.

Use Python -B or PYTHONDONTWRITEBYTECODE=1 to prevent bytecode writes outside
this folder. Set TMPDIR to the absolute bot_research/tmp path for test and
experiment processes. Work with the existing environment without changing it.
Verify the protected-file hash manifest at the start and finish, and detect new
project files outside the research folder. Report unexpected changes without
overwriting user changes.

2. Establish the actual game contract.

Read configs/balanced.json, td_game/balanced.json, td_game/config.py,
td_game/actions.py, td_game/combat.py, td_game/engine.py, td_game/state.py,
td_game/pathfinding.py, td_bots/protocol.py, and relevant documentation/tests.
Record the exact settings and behavioral rules. Investigate discrepancies
through source inspection and reproductions, not edits to the game.

Pay particular attention to observations and hidden current actions;
interleaved action application; construction legality; shortest-route selection;
path and factory income; hit bounties; terminal-round settlement; roster lifetime;
one-time costs; dense active-entry indexing; modulo spawn scheduling;
spawn/move/arrival/attack ordering; full-HP respawning; and combat-copy cleanup.

Verify turret targeting and damage stacking. Do not assume conventional
single-target tower-defense behavior. Check splash's eight adjacent cells,
including diagonals, and its zero range.

The current catalogs use tier1 through tier5 and gun1/gun2/gun3/splash; walls
cost 1. Load all exact values from the authoritative configuration. Supplied
historical games use older balance settings and do not validate a current-rules
strategy. Do not pretend the anonymous historical bots' source is available.

3. Organize parallel research.

Assign independent, concrete questions to workers. Cover at least:
- Defensive maps, path effects, building placement, and defensive spending.
- Economy, offensive purchases, roster timing, and finite-horizon planning.
- Opponent adaptation, adversarial counters, and evaluation quality.

The main agent owns integration, experiment coordination, evidence assessment,
and final validation. Assign separate files or subdirectories to avoid write
collisions. Have workers report assumptions, implementations, measurements,
failure cases, and uncertainty. Reuse them for further hypotheses and reviews.

4. Build a trustworthy evaluation harness.

Implement importable bots with decide(observation) returning JSON actions.
Use existing Engine/run_match APIs or the CLI for authoritative outcomes.
Local planning simulations are allowed, but strength comparisons must use the
unchanged engine and current bundled rules.

Provide multiple materially different baselines and candidate opponents.
Evaluate both player assignments. Separate tuning opponents and scenarios from
final validation. Record candidate versions, parameters, seeds, exact conditions,
win/draw/loss outcomes, HP differences, ending rounds, rejected actions, bot
errors, and runtime. Preserve representative logs and reproduction commands.

The engine is deterministic: repeated identical conditions do not create
independent evidence. State what actually varies between experiments.

Bots must decide from their observations and their own legitimate state.
Do not inspect pending opponent actions, live engine objects, call stacks,
or unrelated files for hidden information. Use legal game actions rather
than Python execution privileges to gain an advantage.

5. Implement, challenge, and improve candidates.

Develop competing strategies using rule analysis and experiments. Implement
search and optimization code inside bot_research/, leaving interview exercises
and the engine untouched. Test promising components before integrating them.

For each major iteration:
- State a concrete, falsifiable hypothesis.
- Implement and evaluate the candidate.
- Examine representative losses and rejected actions.
- Run focused comparisons or ablations to identify the source of improvement.
- Build targeted counter-strategies against the strongest current candidate.
- Revise it and evaluate on separate validation opponents and scenarios.

Do not declare success after beating idle bots, a weak baseline, or an earlier
version of the same bot. Investigate counter-strategy cycles and fragility.
If candidates have complementary strengths, report that evidence instead of
assuming a universally dominant policy exists.

Complete at least one full cycle of parallel research, implementation,
evaluation, targeted counter-strategy development, revision, and independent
validation. Continue while productive avenues remain within available resources.
Run long experiments in manageable batches and provide substantive progress
reports instead of ending after the first implementation or first win.

6. Deliver a concrete, reproducible result.

Leave a final entry point at bot_research/bots/best.py exposing decide.
Add package initialization files inside bot_research/ if needed; do not change
the root packaging configuration or the existing loader.

This example smoke command must work from the repository root:

PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B -m td_game.runner --balanced --bot-a bot_research.bots.best:decide --bot-b td_bots.protocol:idle --output bot_research/runs/best-vs-idle-000001.jsonl

Use unique output filenames because existing logs cannot be overwritten.
The idle-opponent run checks integration, not strategy strength.

Run relevant existing tests without editing them and necessary tests for your
own implementation. Document pre-existing issues and write reproductions under
bot_research/ while leaving protected code unchanged.

Write an English report under bot_research/reports/ covering the final bot's
decision rules, tournament results, ablations, validation evidence, counters,
known failures, runtime costs, reproduction commands, and file-integrity checks.
Distinguish proved claims, empirical findings, and conjectures. Describe the
result as strongest within the tested scope unless you establish a broader proof.

Proceed autonomously within this scope. Do not ask for approval for routine
experiments or implementation choices already authorized here. Do not stop
after a proposal, an empty scaffold, or the first successful match.
