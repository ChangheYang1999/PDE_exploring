# Completing verification after installation changed

Recorded 2026-10-31T18:46:26.423773+00:00, after the source check rejected the replacement and before the new archival checks.

## Facts and question

The 72 best_v9f games ended at 18:43:04Z, and the original-engine replay audit completed before the installed entry changed. At 18:44:53Z, while fresh entry-point checks were still running, best.py changed from the frozen best_v9f hash to the existing best_v9e hash. Eighteen per-game checks passed, the next check detected the change after execution, and the remaining 53 rejected the initial hash. Preserve all of these checks and failures. They are audit attempts, not failed games and not additional samples.

The remaining question is whether the exact archived best_v9f direct and factory entry points regenerate all recorded candidate actions. No match outcome, initial condition or opposing policy changes. No installation is restored or edited by this worker.

## Conditional equivalence argument

Verify the candidate's archived bytes against the original freeze and verify all other imported source and data files against their original hashes and archives. Load the archived candidate module in a fresh interpreter using Python's ordinary import machinery under a separate module name. Its inspected source uses absolute imports, has no __file__ or __name__ dependency and does not inspect module identity. Its initial globals and function bodies are therefore those of the original byte-identical source, apart from Python's administrative module identity. Call its direct decide and a new make() instance on separate copies of each public observation. Skip the same prescribed prefix calls. Replay only recorded actions through the unchanged Engine and compare every produced action list.

Agreement establishes the same finite-history direct/factory statement as the original check for the archived candidate, conditional on the verified imported files. It does not establish that the currently installed best.py is best_v9f; it is not, and the report must name this distinction. The actual installation was used for all original games, whose initial and final source attestations remain separately checked. No engine module or game object is modified.

## Reporting

Use a separately named checker, wrapper, per-game audit directory and summary. Publish all original and archival attempts, the replacement timestamp, all four known candidate losses and the matched fallback rule. The old declaration, 72 games, original replay checks and failed entry directory remain untouched. Source hashes, complete action equality, legal submissions and unmodified observations are required for every archival check. A mismatch remains a failed verification, never a reason to alter the recorded game.
