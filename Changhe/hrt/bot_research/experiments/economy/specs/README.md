# Candidate specs of the economy lane (hrt-w2)

One spec per file, as passed to the lead's tournament (bot_research.harness.tournament) and read by
experiments/economy/gate_vs_base.py. All bots are frozen copies under bots/economy/frozen/<tag>/ (SHA256SUMS in each).

| file | name in notes/economy.md | definition |
| --- | --- | --- |
| e20.spec | E20 | frozen v20 econ20 with the lead's parameters (the foreign target inside best_v9e) |
| v25rm.spec | V25RM | frozen v25 econ25 with the re-plan and attack-cap parameters (entry 15) |
| v29.spec | V29 | frozen v29 econ29 with the V25RM parameters plus fill, fill_reserve and fill_threat (entry 17) |
| g1.spec | g1 | V29 + attack_from=7 (17.14) |
| g0.spec | g0 | V29 + r1_units=0 + attack_from=7 (17.10) |
| g1f.spec | g1f | frozen v31 econ31 with the g1 parameters + fill_own=true (18.15; rejected in 18.21 and 18.24) |
| af6.spec | af6 | V29 + attack_from=6 (18.22) |
| af5.spec | af5 | V29 + attack_from=5 (18.22) |
| af4.spec | af4 | V29 + attack_from=4 (18.31, sensitivity only) |
| af3.spec | af3 | V29 + attack_from=3 (18.31, sensitivity only) |
