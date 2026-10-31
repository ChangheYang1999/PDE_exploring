# F6 design (specification 8.2): scrambled Sobol in c_l and log omega, 16 points, published before any job uses it (lead 15:52:20Z item 4)

Source: the lead's registered file design/sobol16_v1.json (registered 2026-10-28T20:58Z), copied verbatim to configs/design_sobol16_v1.json, sha256 0d80677af3e2e8f7e978cc7ae0a3196322dc480e00a350d04d99efba58399009 (the release queue checks the first 16 hex digits 0d80677af3e2e8f7).

Design: specification 8.2 F6: scrambled Sobol, 16 points, c_l in [0.405,0.495], log omega in [log 0.05, log 20]
Generator: scipy 1.18.0 scipy.stats.qmc.Sobol(d=2, scramble=True, seed=20261028).random(16); c_l=0.405+0.09*u0; omega=exp(log 0.05+(log 20-log 0.05)*u1); rounded to 6 decimals
Seed: 20261028
Created: 2026-10-28T20:56:54Z

Points in generation order (k, c_l, omega); any sampled value is an initial condition, not a constraint (PROMPT 6):

| k | c_l | omega | log10 omega |
|---|---|---|---|
| 0 | 0.459677 | 1.338884 | 0.1267 |
| 1 | 0.42179 | 0.808573 | -0.0923 |
| 2 | 0.4282 | 7.977286 | 0.9019 |
| 3 | 0.49139 | 0.111227 | -0.9538 |
| 4 | 0.48157 | 13.528808 | 1.1313 |
| 5 | 0.443512 | 0.083427 | -1.0787 |
| 6 | 0.406307 | 4.03034 | 0.6053 |
| 7 | 0.469666 | 0.229523 | -0.6392 |
| 8 | 0.461687 | 6.063528 | 0.7827 |
| 9 | 0.412549 | 0.183571 | -0.7362 |
| 10 | 0.448337 | 1.827552 | 0.2619 |
| 11 | 0.477776 | 0.511008 | -0.2916 |
| 12 | 0.484965 | 2.949162 | 0.4697 |
| 13 | 0.435657 | 0.362546 | -0.4406 |
| 14 | 0.42506 | 17.7776 | 1.2499 |
| 15 | 0.45467 | 0.050461 | -1.2970 |

Use in the queue (lead 14:03:42Z item 3; superseded by the draft of 15:52:20Z item 4 as to order): F2 starts from S01 and S09 at k = 0 (0.459677, 1.338884) and k = 1 (0.42179, 0.808573), coefficients kept and refit; further points as slots allow.
Published 2026-10-29T15:57:18Z by numerics.
