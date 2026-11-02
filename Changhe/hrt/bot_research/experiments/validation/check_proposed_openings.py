"""Exhaust every affordable ordered first-round roster on the original engine."""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.match import resolve_spec
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def words(budget, costs, prefix=()):
    yield prefix
    for tier, cost in sorted(costs.items()):
        if cost <= budget:
            yield from words(budget-cost, costs, prefix+(tier,))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manifest', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    manifest = json.loads(Path(args.manifest).read_text())
    inputs = {args.manifest: digest(args.manifest), **manifest['input_sha256']}
    source = {str(p): digest(p) for p in static_closure({'bot_research.experiments.validation.check_proposed_openings'})}
    proof = 'bot_research/experiments/validation/analysis/proposed_opening_rosters/PROOF.md'
    inputs[proof] = digest(proof)
    assert all(digest(p) == h for p, h in {**inputs, **source}.items())
    cfg = balanced_config()
    assert cfg.globals.initial_gold == 100
    costs = {t: m.cost for t, m in cfg.minions.items()}
    rosters = list(words(100, costs))
    assert len(rosters) == len(set(rosters)) == 27
    root = Path(args.output).with_suffix('')
    root.mkdir(exist_ok=False)
    rows = []
    for candidate in manifest['candidates']:
        submissions = {}
        for index, roster in enumerate(rosters):
            for side in (0, 1):
                policy = resolve_spec(candidate['spec'])
                engine = Engine(cfg, ('opening-a', 'opening-b'))
                records = engine.initial_records(('opening-a', 'opening-b'))
                obs = engine.observation(side)
                before = deepcopy(obs)
                actions = policy(obs)
                assert obs == before
                if side in submissions:
                    assert actions == submissions[side]
                else:
                    submissions[side] = deepcopy(actions)
                attack = [{'op': 'buy_minion', 'type': t} for t in roster]
                pair = [actions, attack] if side == 0 else [attack, actions]
                settled = engine.play_round(pair)
                assert all(e['accepted'] for r in settled for e in r['event'] if e['kind'] == 'action')
                path = root / f"{candidate['id']}-roster{index:02d}-side{side}.jsonl"
                with path.open('x') as stream:
                    for record in records + settled:
                        stream.write(json.dumps(record, sort_keys=True) + '\n')
                hp = [engine.players[side].hp, engine.players[1-side].hp]
                rows.append(dict(candidate=candidate['id'], side=side, roster=roster,
                                 cost=sum(costs[t] for t in roster), hp=hp,
                                 incoming_damage=cfg.globals.initial_hp-hp[0],
                                 outgoing_damage=cfg.globals.initial_hp-hp[1],
                                 actions=actions, replay=str(path), replay_sha256=digest(path)))
    groups = {}
    for candidate in manifest['candidates']:
        selected = [x for x in rows if x['candidate'] == candidate['id']]
        for i in range(0, len(selected), 2):
            assert selected[i]['hp'] == selected[i+1]['hp']
        maximum = max(x['incoming_damage'] for x in selected)
        groups[candidate['id']] = dict(maximum_incoming_damage=maximum,
                                      zero_damage_assignments=sum(x['incoming_damage'] == 0 for x in selected),
                                      worst_rosters=[x['roster'] for x in selected if x['side'] == 0 and x['incoming_damage'] == maximum])
    assert len(rows) == 54 * len(manifest['candidates'])
    assert all(digest(p) == h for p, h in {**inputs, **source}.items())
    result = dict(time_utc=datetime.now(timezone.utc).isoformat(), all_passed=True,
                  runtime_seconds=time.perf_counter()-start, ordered_rosters=27,
                  assignment_checks=len(rows), summaries=groups, checks=rows,
                  input_sha256=inputs, source_sha256=source,
                  scope='Exhaustive minion-only round-one rosters for the standard initial state; no full-game or construction-opponent claim.')
    atomic_json(args.output, result, exclusive=True)
    print(json.dumps({k: result[k] for k in ('time_utc', 'runtime_seconds', 'assignment_checks', 'summaries', 'all_passed')}), flush=True)


if __name__ == '__main__':
    main()
