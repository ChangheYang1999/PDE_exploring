"""Check concrete report claims without running any candidate game."""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

from bot_research.bots.defense.frozen.v7.plan import affordable_bundles
from bot_research.harness.gamekit import Rules
from td_game.config import balanced_config
from td_game.engine import Engine

ROOT = Path('bot_research/experiments/validation/reviews')


def sha(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main() -> None:
    cfg = balanced_config()
    engine = Engine(cfg, ('left_policy', 'right_policy'))
    obs0, obs1 = engine.observation(0), engine.observation(1)
    rules = Rules.from_observation(obs0)
    gold = cfg.globals.initial_gold
    enumerated: list[list[str]] = []

    def visit(prefix: list[str], remaining: int) -> None:
        enumerated.append(prefix)
        for tier, entry in sorted(cfg.minions.items()):
            if entry.cost <= remaining:
                assert entry.cost > 0
                visit(prefix + [tier], remaining - entry.cost)

    visit([], gold)
    bundles = affordable_bundles(gold, rules)
    all_rosters = {tuple(x) for x in enumerated}
    sampled = {tuple(x) for x in bundles}
    assert sampled < all_rosters
    assert ('tier1',) in all_rosters - sampled
    left = deepcopy(obs0)
    right = deepcopy(obs1)
    left.pop('player')
    right.pop('player')
    assert left == right
    assert obs0 != obs1
    assert [p['name'] for p in obs0['players']] == ['left_policy', 'right_policy']

    result_path = Path('bot_research/runs/economy/vbest2/results.jsonl')
    evidence = []
    input_hashes = {str(result_path): sha(result_path)}
    for line in result_path.read_text().splitlines():
        row = json.loads(line)
        side = row['candidate_side']
        spec = row['spec_a' if side == 0 else 'spec_b']
        if 'r1_guard=60' not in spec:
            continue
        assert row['error'] is None and row['source_changed'] is False
        log_path = Path(row['log'])
        input_hashes[str(log_path)] = sha(log_path)
        records = [json.loads(x) for x in log_path.read_text().splitlines()]
        r1 = [r for r in records if r['round'] == 1 and r['player'] == side]
        assert len(r1) == 1
        action_events = [e for e in r1[0]['event'] if e['kind'] == 'action']
        assert all(e['accepted'] for e in action_events)
        actions = [e['action'] for e in action_events]
        assert actions == [
            {'op': 'build_wall', 'x': 0, 'y': 1},
            {'op': 'build_wall', 'x': 11, 'y': 3},
            {'op': 'buy_minion', 'type': 'tier1'},
            {'op': 'build_turret', 'type': 'gun2', 'x': 8, 'y': 1},
        ]
        evidence.append({
            'candidate_side': side, 'spec': spec, 'log': str(log_path),
            'round1_actions': actions,
            'round1_costs': [e['cost'] for e in action_events],
            'final_hp_candidate': row['hp_a' if side == 0 else 'hp_b'],
            'final_hp_opponent': row['hp_b' if side == 0 else 'hp_a'],
        })
    assert {e['candidate_side'] for e in evidence} == {0, 1}
    for path in (
        __file__, 'td_game/config.py', 'td_game/engine.py', 'td_bots/protocol.py',
        'td_game/balanced.json', 'bot_research/bots/defense/frozen/v7/plan.py',
        ROOT / 'report-shift4-source.md',
    ):
        path = Path(path)
        if path.is_absolute():
            path = path.relative_to(Path.cwd())
        if path.exists():
            input_hashes[str(path)] = sha(path)
    receipt = {
        'time_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Source and retained-record checks. No candidate or opponent policy call; no match run.',
        'input_sha256': input_hashes,
        'affordable_bundle_example': {
            'gold': gold, 'costs': {k: v.cost for k, v in cfg.minions.items()},
            'all_ordered_rosters_including_empty': len(enumerated),
            'sampled_bundles': bundles, 'sampled_count': len(bundles),
            'omitted_legal_example': ['tier1'],
            'interpretation': 'The generator samples affordable rosters. This does not assert that the omitted roster defeats a plan or changes a result.',
        },
        'observation_identity': {
            'same_public_state_before_submissions': left == right,
            'literal_observations_equal': obs0 == obs1,
            'distinct_player_indices': [obs0['player'], obs1['player']],
            'public_names': [p['name'] for p in obs0['players']],
            'interpretation': 'Round-one pending actions are hidden; seat index and configured player names are visible.',
        },
        'guard60_retained_records': evidence,
        'checks_passed': True,
    }
    target = ROOT / 'report-shift4-claim-checks.json'
    with target.open('x') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps({'receipt': str(target), 'all_ordered_rosters': len(enumerated),
                      'sampled_bundles': len(bundles), 'guard_seats': len(evidence), 'checks_passed': True}))


if __name__ == '__main__':
    main()
