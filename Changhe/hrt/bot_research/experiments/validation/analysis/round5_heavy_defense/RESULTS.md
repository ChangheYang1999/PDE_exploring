# A single extra building costs200 on the reached round-five map

Checked 2026-10-31T15:07:18.525455+00:00.

Within the class stated in PROOF.md, the minimum is200 gold. A gun3 at(0,5) stops the one tier4 while retaining splash exposure190. All721 proposals were enumerated;466 are legal. Independent isolated-copy arithmetic agrees with original combat on every legal map. The maximum total one-copy exposure among additions that retain S>=180 is466 for gun2 and262 for gun1. Neither can stop a560-HP tier4.

The geometric fixture is funded independently. A separate original-engine counterfactual establishes affordability: omit all ten round-five factory purchases from the actual target action list and add the gun3. Every action is accepted; target and counter HP end800:755 rather than740:755. This sacrifices ten factories and their future income. It does not establish a stronger complete policy. Multiple-building responses and mixed attacking rosters are outside this minimum claim.

Search runtime: 1.017611s. Independent check runtime: 0.248632s. Inputs, outputs and exact counterfactual records are in runs/validation/round5-heavy-defense-search-001.json and round5-heavy-defense-check-001.json.

Reproduce from the project root with the prescribed no-bytecode environment and a new output filename:

```sh
nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.search_round5_heavy_defense --output bot_research/runs/validation/round5-heavy-defense-search-reproduction.json
nice -n 19 taskset -c 30 .venv/bin/python -B -m bot_research.experiments.validation.check_round5_heavy_defense --input bot_research/runs/validation/round5-heavy-defense-search-reproduction.json --output bot_research/runs/validation/round5-heavy-defense-check-reproduction.json
```
