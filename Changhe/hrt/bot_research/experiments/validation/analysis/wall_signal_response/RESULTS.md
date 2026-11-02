# Manipulating the public response signal

Checked 2026-10-31T19:28:20.570685+00:00.

H1, twenty-wall attacker wins against J with exactly the H response history: REFUTED. H2, that win exceeds both the nineteen-wall J result and the same twenty-wall attacker against I: REFUTED.

Each attacker advances its private H model from round one, replaces only its first factory action list with a prefix of the existing guard00 wall witness and affordable factories, then uses the fixed round-three tier2 timing policy. K19 and K20 differ by one wall. J selects H for K20 and I for K19. This criterion was deliberately targeted after inspecting J, so all games are development evidence.

| Walls | Opponent | Attacker outcome | HP attacker:opponent | End round | Tier2 purchases | Forecast mismatch rounds |
|---:|---|---|---|---:|---:|---|
| 19 | J | L | 752:764 | 50 | 3 | 47 |
| 19 | H | L | -40:692 | 9 | 3 | 0 |
| 19 | I | L | 752:764 | 50 | 3 | 47 |
| 20 | J | L | -40:656 | 9 | 4 | 0 |
| 20 | H | L | -40:656 | 9 | 4 | 0 |
| 20 | I | D | 752:752 | 50 | 4 | 46 |

All twelve full games pass source/data archives, strict condition accounting, original-engine replay, legality and observation checks, 708 fresh external decisions and 354 additional attacker/forecast checks. Twelve prefix cases were checked first. Each displayed row represents two physical assignments with identical complete canonical histories. No rejected submissions, bot errors or source drift occurred.

The complete K20-J history equals K20-H: True. The complete K19-J history equals K19-I: True. These matched fixed-response controls separate the chosen response from a comparison that changes wall geometry alone. A nineteen-versus-twenty-wall outcome difference by itself would not identify response selection as the cause, because walls also change cost and path.

A successful attack would show only that this public threshold can be induced to choose an exploitable branch. It would not show that public-history adaptation is generally harmful or that either fixed response is globally superior. J already loses to B in the earlier finite table. This is a specific failure mechanism, not its first counterexample.

Full conditions, timings, traces and hashes are in verification/full_games.json and the two wall-signal manifests. Reproduce with the bounded commands in runs/validation/wall-signal-001-pipeline.log. Pool D and the installed final entry point are not used.
