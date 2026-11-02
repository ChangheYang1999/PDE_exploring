# Independent reserved validation

Rendered at 2026-10-31T18:43:26.793396+00:00.

Candidate: `bot_research.bots.best:decide`.
SHA256: `36d861fc3790a5b7c4bc9d33be3a769ba144bf72fd25d2e2a3feb2759306b580`.
Pool: C. All 72 prescribed conditions have valid results and complete original-engine replays.

Standard starts measure the declared policy from its normal initial state. The other starts replace the first two or three rounds with registered legal prefixes and skip the underlying policy calls during those prefixes. Their scores are continuation stress results and are kept separate.

| Start | Games | Wins | Draws | Losses |
| --- | ---: | ---: | ---: | ---: |
| standard | 24 | 16 | 4 | 4 |
| mirror_7493_3 | 24 | 24 | 0 | 0 |
| asym_8669_2 | 24 | 24 | 0 | 0 |

36 conditions have both player assignments; 36 pairs have identical complete normalized trajectories. The engine is deterministic. Exchanging seats and replaying actions checks reproducibility; neither supplies an independent random sample.

| Start | Opponent | Seat 0 outcome / HP | Seat 1 outcome / HP | Rounds, seats 0 / 1 |
| --- | --- | --- | --- | --- |
| standard | C-00 | W 800:-162 | W 800:-162 | 10 / 10 |
| standard | C-01 | W 800:-736 | W 800:-736 | 11 / 11 |
| standard | C-02 | W 800:-84 | W 800:-84 | 11 / 11 |
| standard | C-03 | W 795:-75 | W 795:-75 | 9 / 9 |
| standard | C-04 | W 778:-600 | W 778:-600 | 9 / 9 |
| standard | C-05 | W 795:-148 | W 795:-148 | 13 / 13 |
| standard | C-06 | W 800:-424 | W 800:-424 | 13 / 13 |
| standard | C-07 | W 800:-490 | W 800:-490 | 14 / 14 |
| standard | C-08 | L 774:800 | L 774:800 | 50 / 50 |
| standard | C-09 | D 800:800 | D 800:800 | 50 / 50 |
| standard | C-10 | D 795:795 | D 795:795 | 50 / 50 |
| standard | C-11 | L 788:790 | L 788:790 | 50 / 50 |
| mirror_7493_3 | C-00 | W 730:-726 | W 730:-726 | 12 / 12 |
| mirror_7493_3 | C-01 | W 730:-398 | W 730:-398 | 12 / 12 |
| mirror_7493_3 | C-02 | W 730:-50 | W 730:-50 | 12 / 12 |
| mirror_7493_3 | C-03 | W 718:-26 | W 718:-26 | 11 / 11 |
| mirror_7493_3 | C-04 | W 730:-50 | W 730:-50 | 10 / 10 |
| mirror_7493_3 | C-05 | W 730:-326 | W 730:-326 | 14 / 14 |
| mirror_7493_3 | C-06 | W 730:-386 | W 730:-386 | 13 / 13 |
| mirror_7493_3 | C-07 | W 730:-415 | W 730:-415 | 13 / 13 |
| mirror_7493_3 | C-08 | W 704:-15 | W 704:-15 | 11 / 11 |
| mirror_7493_3 | C-09 | W 730:-50 | W 730:-50 | 11 / 11 |
| mirror_7493_3 | C-10 | W 730:-110 | W 730:-110 | 15 / 15 |
| mirror_7493_3 | C-11 | W 730:-110 | W 730:-110 | 15 / 15 |
| asym_8669_2 | C-00 | W 774:-32 | W 774:-32 | 11 / 11 |
| asym_8669_2 | C-01 | W 800:-124 | W 800:-124 | 11 / 11 |
| asym_8669_2 | C-02 | W 520:-6 | W 520:-6 | 11 / 11 |
| asym_8669_2 | C-03 | W 773:-135 | W 773:-135 | 11 / 11 |
| asym_8669_2 | C-04 | W 780:-62 | W 780:-62 | 11 / 11 |
| asym_8669_2 | C-05 | W 775:-20 | W 775:-20 | 13 / 13 |
| asym_8669_2 | C-06 | W 800:-4 | W 800:-4 | 13 / 13 |
| asym_8669_2 | C-07 | W 800:-40 | W 800:-40 | 12 / 12 |
| asym_8669_2 | C-08 | W 800:-32 | W 800:-32 | 11 / 11 |
| asym_8669_2 | C-09 | W 800:-32 | W 800:-32 | 11 / 11 |
| asym_8669_2 | C-10 | W 800:-2700 | W 800:-2700 | 25 / 25 |
| asym_8669_2 | C-11 | W 800:-2700 | W 800:-2700 | 25 / 25 |

HP is always candidate first. A simultaneous base destruction is a draw even when final HP differ.

0 failed computational attempts are retained separately from the selected completed results. The selected result is the earliest valid completion for that exact condition. No outcome is assigned from a partial replay.


Runtime measurements are low-priority wall times on a shared machine, not portable speed bounds. The sum of parallel match runtimes is not elapsed experiment time. Timed calls include the prefix wrapper; prescribed-round calls do not invoke the underlying policy.

| Start | Sum of selected match times (s) | Largest candidate call (s) | Largest candidate total per match (s) |
| --- | ---: | ---: | ---: |
| standard | 153.769 | 1.166 | 11.818 |
| mirror_7493_3 | 56.931 | 1.113 | 1.800 |
| asym_8669_2 | 71.624 | 0.760 | 6.300 |

First campaign start: 2026-10-31T18:37:47.010670+00:00. Last selected match completion: 2026-10-31T18:43:04.131262+00:00.
Elapsed between those events: 317.121 seconds.

The source archive matches the declared freeze. Completed results have no bot errors, rejected actions or source drift. The archived manifest and generated jobs agree. Opponent policy families and implementation code are shared with development. The separate holdout-separation audit addresses exact parameter overlap. No universal strength claim follows.

Opponent definitions:

```json
{
  "00": {
    "profile": {
      "defense": "splash",
      "defense_count": 2,
      "growth_rounds": 3,
      "keep_investing": 0.3,
      "roster": [
        "tier3",
        "tier2",
        "tier1"
      ]
    }
  },
  "01": {
    "profile": {
      "defense": "gun2",
      "defense_count": 2,
      "growth_rounds": 5,
      "pulse_period": 4,
      "pulse_phase": 2,
      "roster": [
        "tier4",
        "tier4",
        "tier1"
      ]
    }
  },
  "02": {
    "profile": {
      "defense": "splash",
      "defense_count": 4,
      "growth_rounds": 9,
      "pulse_period": 5,
      "pulse_phase": 1,
      "roster": [
        "tier5",
        "tier2"
      ]
    }
  },
  "03": {
    "profile": {
      "defense": "gun1",
      "defense_count": 2,
      "growth_rounds": 1,
      "keep_investing": 0.45,
      "roster": [
        "tier1",
        "tier2",
        "tier1"
      ]
    }
  },
  "04": {
    "spec": "bot_research.bots.counters.pool:@random_legal?seed=7919&attack_bias=0.33&action_cap=37"
  },
  "05": {
    "spec": "bot_research.bots.counters.pool:@mirror?attack_floor=0.31&defense_share=0.39"
  },
  "06": {
    "spec": "bot_research.bots.counters.pool:@stacker?growth_rounds=9&tier=%22tier2%22&batch_cap=920"
  },
  "07": {
    "spec": "bot_research.bots.counters.pool:@turtle?kind=%22splash%22&defense_share=0.43&max_towers=31"
  },
  "08": {
    "spec": "bot_research.bots.counters.budget_timing:@make?tier=%22tier3%22&attack_round=4&budget_fraction=0.65"
  },
  "09": {
    "spec": "bot_research.bots.counters.budget_timing:@make?tier=%22tier4%22&attack_round=6&budget_fraction=0.65"
  },
  "10": {
    "spec": "bot_research.bots.counters.guard_geometry:@make?roster=%5B%22tier1%22%5D&x=9&y=2"
  },
  "11": {
    "spec": "bot_research.bots.counters.guard_geometry:@make?roster=%5B%22tier2%22%5D&x=10&y=2"
  }
}
```

Campaign accounting: `bot_research/runs/validation/reused-C-best-v9f-001-strict.json` (SHA256 `25d0e09e2e29771c15690b5993534de1d99627f9e0f304dc2fe0b9f0a49c1d5c`).
Replay accounting: `bot_research/runs/validation/reused-C-best-v9f-001-replay.json` (SHA256 `4708a85f3e42ca833c1e8db6854ca920855631faacf8810afe5262439757d711`).
Renderer SHA256: `59183900107084c215584d4becb77ab5751e4df610e42fe51a27b22f6521a7ed`.
