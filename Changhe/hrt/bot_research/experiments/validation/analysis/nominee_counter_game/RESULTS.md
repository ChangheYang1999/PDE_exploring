# The two nominees and their counters form a finite cycle

Checked 2026-10-31T15:19:12.617705+00:00.

CONFIRMED: the four fixed standard-start policies have directed cycles P5TNUBM > lead8 > early1_handoff6 > P5TNUBM and P4TNUB > early1_handoff6 > P5TNUBM > lead8 > P4TNUB. No policy in this set wins against every other one. A rational one-third mixture over P5TNUBM, early1_handoff6 and lead8 has value0 in the stated finite payoff table.

The table reports the row policy's result, HP and final round. Each row covers both physical assignments, whose complete normalized histories agree.

| Row policy | Opponent | Row outcome per seat | HP | Final round |
|---|---|---|---|---:|
| P4TNUB | P5TNUBM | D | 785:785 | 50 |
| P4TNUB | early1_handoff6 | W | 800:-2605 | 24 |
| P4TNUB | lead8 | L | 660:755 | 50 |
| P5TNUBM | early1_handoff6 | L | 740:755 | 50 |
| P5TNUBM | lead8 | W | 800:-1439 | 21 |
| early1_handoff6 | lead8 | L | 520:620 | 50 |

The early-heavy counter always retains its P5TNUBM clone, even against P4TNUB or lead8. No model is silently retargeted between opponents. The lead8 controller retains the HP trigger and forecast settings declared in nominee-handoff-001. Full specifications and source hashes appear in the matrix and campaign declarations.

Only six games are newly executed: P4TNUB against P5TNUBM and early1_handoff6, and early1_handoff6 against lead8, both assignments. The other six reuse previously audited nominee-handoff and early-heavy-handoff games. The assembler freshly checks all twelve replays and source identities. Both fresh policies reproduce all496 decisions in the six new games; observations remain unchanged and every action list is legal. Original campaign audits report no bot errors or rejected submitted actions.

Assign1 to a win,0 to a draw and-1 to a loss and average assignments. In policy order P4TNUB, P5TNUBM, early1_handoff6, lead8, the payoff matrix is:

```text
 0  0  1 -1
 0  0 -1  1
-1  1  0 -1
 1 -1  1  0
```

Diagonal zeros use the symmetric payoff convention; no self-play games are claimed. Exact rational checking verifies p=(0,1/3,1/3,1/3), pA=(0,0,0,0), and the value0 certificate. Every pure row has worst payoff-1. This statement is conditional on the fixed finite matrix, with a component sampled secretly before the opponent chooses its policy. It says nothing about new policies, continuation states, or global game-theoretic optimality. The six assignment pairs are deterministic controls, not twelve independent samples. No random mixture was installed as best.py.

To reproduce, run the two declared development manifests into new directories, replay them with the original engine, regenerate fresh policy histories, then use assemble_nominee_counter_game.py, solve_metagame.py and check_metagame_certificate.py. The solver uses local numerical Python; the certificate checker uses exact fractions and the game environment. Respect the project-root, bytecode-disabled, temporary-directory and assigned-affinity run conventions.

Audit inputs:

- `bot_research/runs/validation/nominee-counter-game-matrix-001.json`.
- `bot_research/runs/validation/nominee-counter-game-certificate-001.json`.
- `bot_research/runs/validation/nominee-counter-game-certificate-check-001.json`.
- `bot_research/runs/validation/nominee-cross-strict-001.json`.
- `bot_research/runs/validation/nominee-cross-replay-001.json`.
- `bot_research/runs/validation/nominee-cross-summary-001.json`.
- `bot_research/runs/validation/nominee-cross-data-001.json`.
- `bot_research/runs/validation/nominee-cross-histories-001.json`.
- `bot_research/experiments/validation/nominee-cross-001.json`.
- `bot_research/runs/validation/counter-cross-strict-001.json`.
- `bot_research/runs/validation/counter-cross-replay-001.json`.
- `bot_research/runs/validation/counter-cross-summary-001.json`.
- `bot_research/runs/validation/counter-cross-data-001.json`.
- `bot_research/runs/validation/counter-cross-histories-001.json`.
- `bot_research/experiments/validation/counter-cross-001.json`.
- `bot_research/experiments/validation/analysis/nominee_handoff/verification/full_games.json`.
- `bot_research/experiments/validation/analysis/early_heavy_handoff/verification/full_games.json`.
