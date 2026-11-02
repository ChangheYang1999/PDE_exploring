# Final reserved validation protocol

Written 2026-10-31T16:15:59.320339+00:00, before either registered candidate is evaluated on pool C.

## Statement and hypotheses

Let C be the exact seventy-two conditions in late_holdout_manifest.json, declared at 09:11:05Z. Let B be the installed best_v9e and M the P5TNUBM comparison, with entry points and full source hashes in late-comparison-declaration-001.json. Each condition specifies an opponent, physical player assignment and either the standard state or an explicit legal opening history. The policies are not called during prescribed opening rounds. Assume the source archive and loaded-source attestations match the declarations, the original Engine resolves every recorded action, and each result passes a complete independent replay.

Then the win/draw/loss counts reported separately for standard and each continuation start are exact finite counts for these policies and conditions. A paired seat swap is a reproducibility control, not a new random opponent. No population win probability or global dominance follows.

## Argument

The manifest generator constructs twelve opponent settings times three start conditions times two seats. The runner freezes all relevant sources and creates a fresh Python interpreter for each condition. It uses the original engine, passes only each player's public observation to its policy, and records both submitted actions and the engine events. The result's winner determines the candidate outcome by its recorded seat. Both-bases-dead outcomes are therefore draws even if residual HP differ.

The accounting checker reconstructs the seventy-two jobs from the archived manifest and compares every job, condition and source attestation. It retains failures separately; where a retry is necessary the earliest valid completion is the primary result. The independent replay starts a fresh original engine, reapplies each recorded action, and checks events, final HP, ending round and winner. Hence every accepted outcome is an outcome of the unchanged engine on the stated actions. Counting the primary outcome exactly once per job proves the finite table, conditional on successful checks. Fresh entry-point audits separately verify that installed decide and default factory reproduce the recorded policy actions on the actual public histories. They are not additional strength samples.

Exact parameter and prescribed-history overlap audits compare pre-campaign development records. Absence of a recorded overlap is limited to those records; the implementation families remain known. The second candidate is declared before the first candidate's games. It is a descriptive comparison and cannot change the selected bot. Its overlap with the first campaign is expected repeated evaluation of the same fixed pool, not new independent validation data.

## Dependencies, evidence and open steps

Dependencies are the original rules, the archived manifest and prefix legality receipt, source_closure.py, late_validation.py, isolated_match.py, audit_late_campaign.py and replay_audit.py. Player-assignment interpretation uses ../assignment_symmetry/PROOF.md. The integrity baseline predates all research and must remain unchanged.

At writing, no pool C game has run. Completion, exact scores, runtime measurements, overlap checks, failure accounting and final source integrity remain OPEN. The result will be recorded with dates and relative evidence paths in RESULTS.md.
