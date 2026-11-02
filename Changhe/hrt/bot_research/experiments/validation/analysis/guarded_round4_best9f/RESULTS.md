# Fixed guarded round-four counter against best_v9f

Checked 2026-10-31T18:56:56.617332+00:00.

H1 is **CONFIRMED**: the candidate outcomes in four declared games are {'L': 4}. All four old best_v9e controls are losses for that candidate, 740:755. The two counter settings and all their parameters are unchanged. This is a development transfer test requested after the candidate was installed, not a held-out validation set.

The new candidate is frozen best_v9f, SHA256 36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580, byte-identical to installed best.py when declared. Results and HP below are from the candidate's perspective.

| Counter | Candidate seat | Outcome | HP candidate:counter | Final round | Counter handoff |
|---|---:|---|---|---:|---:|
| earlygun1_budget1of2 | 0 | L | 740:755 | 50 | 5 |
| earlygun1_budget1of2 | 1 | L | 740:755 | 50 | 5 |
| earlygun1_budget1of1 | 0 | L | 740:755 | 50 | 5 |
| earlygun1_budget1of1 | 1 | L | 740:755 | 50 | 5 |

Every game passes complete condition accounting, original-engine replay, source/data archival checks, fresh regeneration of both policies (400 calls), and a second counter-only check (200 decisions) of the exact public trigger and no purchases after handoff. There are 48 locally filtered proposals, zero submitted rejected actions, and zero bot errors. Both physical-assignment pairs have identical normalized complete histories. The old four controls and their source archives are checked but not counted as new games. The inherited gun lemma is not used as a substitute for these actual games.

Recorded candidate timing: 200 decisions, 45.740700 seconds total, maximum 0.768386 seconds. Counter timing: 200 decisions, 10.223833 seconds total, maximum 0.765269 seconds. These are observed shared-machine timings, not worst-case bounds.

A result here concerns these exact settings only. Equal player swaps do not supply independent samples or establish absence of load effects in other branches.

Reproduce from the project root with the supplied Python, disabled bytecode, research temporary directory, one assigned low-priority core and one numerical thread. Run run_data_development on guarded-round4-best9f-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_fixed_game_histories and check_guarded_round4_histories. The pipeline log records exact bounded invocations. See verification/full_games.json for complete input hashes and old/new rows.
