# Independent reserved validation

Rendered at 2026-10-31T07:08:02.198626+00:00.

Candidate: `bot_research.bots.best:decide`.
SHA256: `88a8e42f954cfb06a611eb002fb256a954cdd0984d1b2e1cac47c254bdeb829d`.
Pool: A. All 60 prescribed conditions have valid results and complete original-engine replays.

Standard starts measure the declared policy from its normal initial state. The other starts replace round-one actions with the registered legal prefix and skip the underlying policy call in that round. Their scores are continuation stress results and are kept separate.

| Start | Games | Wins | Draws | Losses |
| --- | ---: | ---: | ---: | ---: |
| standard | 20 | 10 | 10 | 0 |
| one_round_factory_prefix | 20 | 6 | 12 | 2 |
| asymmetric_splash_prefix | 20 | 6 | 12 | 2 |

30 conditions have both player assignments; 30 pairs have identical complete normalized trajectories. The engine is deterministic. Exchanging seats and replaying actions checks reproducibility; neither supplies an independent random sample.

| Start | Opponent | Seat 0 outcome / HP | Seat 1 outcome / HP | Rounds, seats 0 / 1 |
| --- | --- | --- | --- | --- |
| standard | A-00 | D 800:800 | D 800:800 | 50 / 50 |
| standard | A-01 | W 800:-262 | W 800:-262 | 10 / 10 |
| standard | A-02 | W 800:-640 | W 800:-640 | 15 / 15 |
| standard | A-03 | D 800:800 | D 800:800 | 50 / 50 |
| standard | A-04 | D 800:800 | D 800:800 | 50 / 50 |
| standard | A-05 | W 790:-6 | W 790:-6 | 9 / 9 |
| standard | A-06 | W 778:-202 | W 778:-202 | 10 / 10 |
| standard | A-07 | D 800:800 | D 800:800 | 50 / 50 |
| standard | A-08 | D 800:800 | D 800:800 | 50 / 50 |
| standard | A-09 | W 800:-1200 | W 800:-1200 | 17 / 17 |
| one_round_factory_prefix | A-00 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-01 | W 800:-296 | W 800:-296 | 10 / 10 |
| one_round_factory_prefix | A-02 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-03 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-04 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-05 | L 790:800 | L 790:800 | 50 / 50 |
| one_round_factory_prefix | A-06 | W 783:-268 | W 783:-268 | 10 / 10 |
| one_round_factory_prefix | A-07 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-08 | D 800:800 | D 800:800 | 50 / 50 |
| one_round_factory_prefix | A-09 | W 800:-1300 | W 800:-1300 | 16 / 16 |
| asymmetric_splash_prefix | A-00 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-01 | W 800:-504 | W 800:-504 | 11 / 11 |
| asymmetric_splash_prefix | A-02 | L 660:800 | L 660:800 | 50 / 50 |
| asymmetric_splash_prefix | A-03 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-04 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-05 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-06 | W 788:-280 | W 788:-280 | 14 / 14 |
| asymmetric_splash_prefix | A-07 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-08 | D 800:800 | D 800:800 | 50 / 50 |
| asymmetric_splash_prefix | A-09 | W 800:-1440 | W 800:-1440 | 20 / 20 |

HP is always candidate first. A simultaneous base destruction is a draw even when final HP differ.

2 failed computational attempts are retained separately from the selected completed results. The selected result is the earliest valid completion for that exact condition. No outcome is assigned from a partial replay.

- `standard-07-side0`: 300-second timeout; evidence in `bot_research/runs/validation/final-best-v9a-poolA-001`.
- `standard-07-side1`: 300-second timeout; evidence in `bot_research/runs/validation/final-best-v9a-poolA-001`.

Runtime measurements are low-priority wall times on a shared machine, not portable speed bounds. The sum of parallel match runtimes is not elapsed experiment time. Timed calls include the prefix wrapper; prescribed-round calls do not invoke the underlying policy.

| Start | Sum of selected match times (s) | Largest candidate call (s) | Largest candidate total per match (s) |
| --- | ---: | ---: | ---: |
| standard | 1151.603 | 5.425 | 65.608 |
| one_round_factory_prefix | 1102.590 | 3.133 | 44.535 |
| asymmetric_splash_prefix | 519.124 | 1.182 | 32.299 |

First campaign start: 2026-10-31T06:12:13.913897+00:00. Last selected match completion: 2026-10-31T07:06:16.598448+00:00.
Elapsed between those events: 3242.685 seconds.

The source archive matches the declared freeze. Completed results have no bot errors, rejected actions or source drift. The archived manifest and generated jobs agree. Opponent policy families and implementation code are shared with development. The separate holdout-separation audit addresses exact parameter overlap. No universal strength claim follows.

Opponent definitions:

```json
{
  "00": {
    "profile": {
      "defense": "splash",
      "defense_count": 1,
      "growth_rounds": 2,
      "keep_investing": 0.2,
      "roster": [
        "tier2",
        "tier1",
        "tier2",
        "tier1"
      ]
    }
  },
  "01": {
    "profile": {
      "defense": "gun2",
      "defense_count": 2,
      "growth_rounds": 4,
      "keep_investing": 0.15,
      "roster": [
        "tier3",
        "tier1",
        "tier1",
        "tier2"
      ]
    }
  },
  "02": {
    "profile": {
      "defense": "splash",
      "defense_count": 2,
      "growth_rounds": 6,
      "pulse_period": 2,
      "pulse_phase": 0,
      "roster": [
        "tier5",
        "tier2",
        "tier2"
      ]
    }
  },
  "03": {
    "profile": {
      "defense": "gun1",
      "defense_count": 2,
      "growth_rounds": 3,
      "pulse_period": 3,
      "pulse_phase": 1,
      "roster": [
        "tier4",
        "tier1",
        "tier3"
      ]
    }
  },
  "04": {
    "profile": {
      "defense": "splash",
      "defense_count": 1,
      "growth_rounds": 7,
      "keep_investing": 0.35,
      "roster": [
        "tier3",
        "tier3",
        "tier1"
      ]
    }
  },
  "05": {
    "profile": {
      "defense": "splash",
      "defense_count": 1,
      "growth_rounds": 0,
      "keep_investing": 0.3,
      "roster": [
        "tier1",
        "tier1",
        "tier2"
      ]
    }
  },
  "06": {
    "spec": "bot_research.bots.counters.pool:@random_legal?seed=2003&attack_bias=0.42&action_cap=31"
  },
  "07": {
    "spec": "bot_research.bots.counters.pool:@mirror?attack_floor=0.22&defense_share=0.45"
  },
  "08": {
    "spec": "bot_research.bots.counters.pool:@stacker?growth_rounds=6&tier=tier2&batch_cap=750"
  },
  "09": {
    "spec": "bot_research.bots.counters.pool:@turtle?kind=gun3&defense_share=0.47&max_towers=23"
  }
}
```

Campaign accounting: `bot_research/runs/validation/final-best-v9a-poolA-final-audit-001.json` (SHA256 `950a2eea9f994a487c8b6bda7bf86312f6e8149ed2bcdaf953f63d5acf459b9d`).
Replay accounting: `bot_research/runs/validation/final-best-v9a-poolA-final-replay-check-001.json` (SHA256 `36225ce46988b7832e978a105fd841c5ca07d1c78f5b94407746b2ed9e6da947`).
Renderer SHA256: `5afde173a832c06a133627a5803d9417df0445feb01bd722099ae3ac83d7ba0b`.
