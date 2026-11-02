# Finite public-label and player-index check

Completed 2026-10-31T20:05:42.230463+00:00. Verdict: **CONFIRMED**.

The declared 72 of 72 C histories yielded 0 action differences and 0 failed attempts. There were 1104 actual candidate calls with both public names replaced by `anonymous`, and 1104 calls with that replacement plus a swap of the player snapshots and observer index. The 120 prescribed prefix rounds per transformation were skipped, not counted as policy calls. Every completed case independently replayed its retained game through the original engine, checked observation preservation and checked generated action legality.

This checks metadata transformations of the selected best_v9e on retained selection histories. It adds no games, no W/D/L results and no independent strength evidence. Passing does not prove name independence on all reachable states or remove the engine's public identity information. See PROOF.md for the exact finite assertion and verification/full_check.json for source-bound evidence.
