# Debug-mode bot research rules

This project is currently in development and debugging mode, not an interview.
The owner explicitly authorizes independent strategy research, algorithm design,
bot implementation, experiments, and multi-agent collaboration for this task.
The previous interview-only restrictions do not apply to this research task.
Their archived copy is `bot_research/AGENTS.interview.md`; it is a historical
reference, not an active instruction file.

## Write boundary

- Read existing project files as needed to understand the game.
- Create and modify project files ONLY inside `bot_research/`.
- Treat every existing file outside `bot_research/` as read-only, including
  this `AGENTS.md`, `td_game/`, `td_bots/`, `td_view/`, `td_stats/`, `configs/`,
  `data/`, `data_analysis/`, `interview_pathfinding/`, `tests/`, `docs/`,
  `README.md`, `pyproject.toml`, and `.gitignore`.
- Put bots in `bot_research/bots/`, experiment tools in
  `bot_research/experiments/`, new tests in `bot_research/tests/`, replay logs
  and result tables in `bot_research/runs/`, and findings in
  `bot_research/reports/`.
- Do not regenerate, rename, remove, or rewrite supplied records or notebook
  outputs. Do not complete or modify the interview exercise files.
- Do not edit the engine, configuration, existing tests, or viewer to support
  a bot. Use imports, adapters, and helper code inside `bot_research/`.
- Prevent imports from creating bytecode outside the research folder: use
  `PYTHONDONTWRITEBYTECODE=1` or Python's `-B` option. Route temporary files
  to `bot_research/tmp/` and keep generated reports and caches in the research
  folder. Do not install dependencies into or modify the existing environment.

## Rules and bot interface

- Inspect the authoritative configuration, engine, combat code, bot adapter,
  documentation, and tests before experimenting. Record the exact rules used.
- Use the current bundled rules for all strategy-strength comparisons. The
  current catalogs are `tier1` through `tier5` and
  `gun1`/`gun2`/`gun3`/`splash`, with wall cost 1.
- Supplied `data/games/` records use earlier balance settings. Their metadata
  describes historical games, not current-rules performance.
- Do not rebalance parameters, substitute a modified engine, monkey-patch
  engine behavior, or silently change rules in an experiment harness.
- Implement importable bots exposing
  `decide(observation: dict) -> list[dict]`, compatible with the existing
  `--bot-a module:function` and `--bot-b module:function` loader.
- Bot decisions may use observations, their own persistent state, and legitimate
  local planning or simulation. Do not inspect live engine objects, the
  opponent's pending submission, or other hidden process state. Do not gain
  an advantage through filesystem or Python-process side effects.
- If an engine issue is suspected, write a reproduction and explanation
  inside `bot_research/`. Keep the original implementation unchanged.

## Parallel research and evaluation

- Use multiple agents for substantive strategy research when supported,
  within the actual available concurrency limit. Assign distinct research
  questions and file ownership; all agents share the same write boundary.
- The main agent integrates candidates, evaluates evidence, and organizes
  independent cross-checks. Reuse workers for later experiments and reviews.
- Run actual matches, exchange player positions, preserve relevant logs,
  record seeds, and compare diverse opponents. Identical deterministic reruns
  are reproducibility checks, not additional independent evidence.
- Separate development opponents and tuning scenarios from final validation.
  Track wins, draws, losses, final HP difference, match length, invalid actions,
  bot errors, and decision runtime.
- Challenge promising bots with targeted counter-strategies and investigate
  representative losses. Distinguish measured results, conjectures, and proofs.
  Do not claim global optimality from a limited tournament.
- Run relevant existing tests without changing them; add necessary tests for
  research code only inside `bot_research/tests/`.

## Integrity and delivery

- `bot_research/protected_files.sha256.json` records existing protected files
  at debug setup. Verify them before and after research, and check that no
  new project files appeared outside `bot_research/`.
- If protected files differ, report the differences. Do not overwrite or
  restore changes that may belong to the user or another process.
- Continue useful work autonomously within this scope. Provide concise
  progress reports and reproducible experiment commands.
- Deliver the strongest validated bot, evaluation tools, results, representative
  replays, a decision-rule explanation, limitations, and reproduction steps
  inside `bot_research/`.
