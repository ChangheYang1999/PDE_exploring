# Independent reserved validation

Rendered at 2026-10-31T09:40:20.932225+00:00.

Candidate: `bot_research.bots.best:decide`.
SHA256: `dc96ac422078fd2cadafcc72fce10bb1d22bbb50b9c19a4bbe7937a2fba85ee7`.
Pool: B. All 60 prescribed conditions have valid results and complete original-engine replays.

Standard starts measure the declared policy from its normal initial state. The other starts replace round-one actions with the registered legal prefix and skip the underlying policy call in that round. Their scores are continuation stress results and are kept separate.

| Start | Games | Wins | Draws | Losses |
| --- | ---: | ---: | ---: | ---: |
| standard | 20 | 20 | 0 | 0 |
| one_round_factory_prefix | 20 | 20 | 0 | 0 |
| asymmetric_splash_prefix | 20 | 20 | 0 | 0 |

30 conditions have both player assignments; 30 pairs have identical complete normalized trajectories. The engine is deterministic. Exchanging seats and replaying actions checks reproducibility; neither supplies an independent random sample.

| Start | Opponent | Seat 0 outcome / HP | Seat 1 outcome / HP | Rounds, seats 0 / 1 |
| --- | --- | --- | --- | --- |
| standard | B-00 | W 800:-244 | W 800:-244 | 10 / 10 |
| standard | B-01 | W 800:-49 | W 800:-49 | 11 / 11 |
| standard | B-02 | W 800:-214 | W 800:-214 | 13 / 13 |
| standard | B-03 | W 800:-448 | W 800:-448 | 11 / 11 |
| standard | B-04 | W 800:-162 | W 800:-162 | 13 / 13 |
| standard | B-05 | W 800:-50 | W 800:-50 | 9 / 9 |
| standard | B-06 | W 800:-8 | W 800:-8 | 9 / 9 |
| standard | B-07 | W 800:-30 | W 800:-30 | 16 / 16 |
| standard | B-08 | W 800:-412 | W 800:-412 | 17 / 17 |
| standard | B-09 | W 800:-910 | W 800:-910 | 14 / 14 |
| one_round_factory_prefix | B-00 | W 800:-556 | W 800:-556 | 9 / 9 |
| one_round_factory_prefix | B-01 | W 800:-220 | W 800:-220 | 10 / 10 |
| one_round_factory_prefix | B-02 | W 800:-188 | W 800:-188 | 10 / 10 |
| one_round_factory_prefix | B-03 | W 800:-52 | W 800:-52 | 9 / 9 |
| one_round_factory_prefix | B-04 | W 800:-188 | W 800:-188 | 11 / 11 |
| one_round_factory_prefix | B-05 | W 774:-746 | W 774:-746 | 9 / 9 |
| one_round_factory_prefix | B-06 | W 790:-128 | W 790:-128 | 11 / 11 |
| one_round_factory_prefix | B-07 | W 800:-480 | W 800:-480 | 13 / 13 |
| one_round_factory_prefix | B-08 | W 800:-112 | W 800:-112 | 11 / 11 |
| one_round_factory_prefix | B-09 | W 800:-180 | W 800:-180 | 12 / 12 |
| asymmetric_splash_prefix | B-00 | W 776:-424 | W 776:-424 | 12 / 12 |
| asymmetric_splash_prefix | B-01 | W 800:-496 | W 800:-496 | 13 / 13 |
| asymmetric_splash_prefix | B-02 | W 800:-344 | W 800:-344 | 12 / 12 |
| asymmetric_splash_prefix | B-03 | W 752:-372 | W 752:-372 | 12 / 12 |
| asymmetric_splash_prefix | B-04 | W 800:-448 | W 800:-448 | 13 / 13 |
| asymmetric_splash_prefix | B-05 | W 722:-4 | W 722:-4 | 12 / 12 |
| asymmetric_splash_prefix | B-06 | W 800:-560 | W 800:-560 | 12 / 12 |
| asymmetric_splash_prefix | B-07 | W 800:-4 | W 800:-4 | 14 / 14 |
| asymmetric_splash_prefix | B-08 | W 800:-472 | W 800:-472 | 13 / 13 |
| asymmetric_splash_prefix | B-09 | W 800:-320 | W 800:-320 | 13 / 13 |

HP is always candidate first. A simultaneous base destruction is a draw even when final HP differ.

0 failed computational attempts are retained separately from the selected completed results. The selected result is the earliest valid completion for that exact condition. No outcome is assigned from a partial replay.


Runtime measurements are low-priority wall times on a shared machine, not portable speed bounds. The sum of parallel match runtimes is not elapsed experiment time. Timed calls include the prefix wrapper; prescribed-round calls do not invoke the underlying policy.

| Start | Sum of selected match times (s) | Largest candidate call (s) | Largest candidate total per match (s) |
| --- | ---: | ---: | ---: |
| standard | 32.392 | 0.660 | 2.235 |
| one_round_factory_prefix | 36.921 | 1.270 | 3.428 |
| asymmetric_splash_prefix | 37.949 | 4.972 | 5.831 |

First campaign start: 2026-10-31T09:34:52.829648+00:00. Last selected match completion: 2026-10-31T09:38:10.586316+00:00.
Elapsed between those events: 197.757 seconds.

The source archive matches the declared freeze. Completed results have no bot errors, rejected actions or source drift. The archived manifest and generated jobs agree. Opponent policy families and implementation code are shared with development. The separate holdout-separation audit addresses exact parameter overlap. No universal strength claim follows.

Opponent definitions:

```json
{
  "00": {
    "profile": {
      "defense": "splash",
      "defense_count": 1,
      "growth_rounds": 1,
      "keep_investing": 0.25,
      "roster": [
        "tier2",
        "tier2",
        "tier1"
      ]
    }
  },
  "01": {
    "profile": {
      "defense": "gun3",
      "defense_count": 1,
      "growth_rounds": 5,
      "keep_investing": 0.25,
      "roster": [
        "tier4",
        "tier2",
        "tier3"
      ]
    }
  },
  "02": {
    "profile": {
      "defense": "splash",
      "defense_count": 3,
      "growth_rounds": 8,
      "pulse_period": 3,
      "pulse_phase": 2,
      "roster": [
        "tier5",
        "tier3",
        "tier1"
      ]
    }
  },
  "03": {
    "profile": {
      "defense": "gun2",
      "defense_count": 1,
      "growth_rounds": 4,
      "pulse_period": 2,
      "pulse_phase": 1,
      "roster": [
        "tier2",
        "tier1",
        "tier1"
      ]
    }
  },
  "04": {
    "profile": {
      "defense": "splash",
      "defense_count": 2,
      "growth_rounds": 6,
      "keep_investing": 0.4,
      "roster": [
        "tier4",
        "tier4",
        "tier2"
      ]
    }
  },
  "05": {
    "profile": {
      "defense": "gun1",
      "defense_count": 1,
      "growth_rounds": 0,
      "keep_investing": 0.2,
      "roster": [
        "tier3",
        "tier1",
        "tier1",
        "tier1"
      ]
    }
  },
  "06": {
    "spec": "bot_research.bots.counters.pool:@random_legal?seed=4027&attack_bias=0.21&action_cap=43"
  },
  "07": {
    "spec": "bot_research.bots.counters.pool:@mirror?attack_floor=0.07&defense_share=0.55"
  },
  "08": {
    "spec": "bot_research.bots.counters.pool:@stacker?growth_rounds=7&tier=tier3&batch_cap=850"
  },
  "09": {
    "spec": "bot_research.bots.counters.pool:@turtle?kind=splash&defense_share=0.37&max_towers=29"
  }
}
```

Campaign accounting: `bot_research/runs/validation/final-best-v9b-poolB-strict-001.json` (SHA256 `3db22ac9bea1622b30de903c7b27266eddb6c69ffa06a9892019a359ab1b85d0`).
Replay accounting: `bot_research/runs/validation/final-best-v9b-poolB-replay-001.json` (SHA256 `962bef9fe9e631a296c7f0dcb3223c90136c0f2a644f81260d701a4b872c4cb6`).
Renderer SHA256: `5afde173a832c06a133627a5803d9417df0445feb01bd722099ae3ac83d7ba0b`.
