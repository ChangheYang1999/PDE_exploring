"""Reconstruct public damage and trigger timing without using the policy wrapper."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse
import hashlib
import json
import time
from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def state(snapshot):
    entries = [RosterEntry(e['id'], e['type'], e['bought_round'], e['expires_after_round'])
               for e in snapshot['roster']]
    return PlayerState(snapshot['name'], snapshot['hp'], snapshot['gold'], snapshot['n_factories'],
        [Building(b['x'], b['y'], b['type']) for b in snapshot['buildings']], entries,
        max((entry.id for entry in entries), default=-1) + 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    begin = time.perf_counter()
    root = Path(args.campaign)
    inputs = {}
    def digest(path):
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    def read(path):
        inputs[str(path)] = digest(path)
        return json.loads(path.read_text())
    for path in static_closure({'bot_research.experiments.validation.audit_emergency_activation'}):
        inputs[str(path)] = digest(path)
    history = read(Path(str(root)+'-histories.json'))
    freeze = read(root/'freeze.json')
    for path, sha in freeze['source_sha256'].items():
        assert digest(path) == sha, path
        inputs[path] = sha
    assert history['exact_counter_policy_reproduction']
    cases = []
    for case in history['cases']:
        row = read(Path(case['result']))
        checked_row(case['result'], inputs)
        condition = row['condition']
        side = 1-condition['candidate_side']
        spec = condition['opponent_spec']
        assert spec.partition(':')[0] == 'bot_research.bots.counters.emergency_route_selector'
        params = {key: json.loads(value[0]) for key, value in parse_qs(spec.partition('?')[2]).items()}
        assert set(params) <= {'mode', 'emergency_rule', 'emergency_from'}
        rule, first = params.get('emergency_rule', 'damage'), params.get('emergency_from', 5)
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        cfg = balanced_config()
        engine = Engine(cfg, tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
        observed = {check['round']: check for check in case['emergency_checks']}
        assert len(observed) == len(case['emergency_checks'])
        checks = []
        trigger = None
        for rnd in range(1, row['rounds']+1):
            obs = engine.observation(side)
            invokes_early = rnd <= 4 or case['selected'] == 'early'
            assert (rnd in observed) == invokes_early
            if invokes_early:
                before = trigger
                damage, activated = None, False
                if trigger is None and rnd >= first:
                    if rule == 'damage':
                        defender, attacker = state(obs['players'][side]), state(obs['players'][1-side])
                        g = cfg.globals
                        route = shortest_path(g.width, g.height, [(b.x,b.y) for b in defender.buildings],
                                              tuple(g.spawn), tuple(g.base))
                        assert route is not None
                        damage = simulate_map(attacker, defender, route, rnd, cfg).damage
                        activated = damage > 0
                    elif rule == 'always':
                        activated = True
                    else:
                        assert rule == 'none'
                    if activated:
                        trigger = rnd
                assert observed[rnd] == dict(round=rnd, visible_incoming=damage, emergency_activated=activated)
                if trigger is None and rnd >= 5 and obs['players'][side]['hp'] > obs['players'][1-side]['hp']:
                    trigger = rnd
                checks.append(dict(round=rnd, previous_trigger=before, damage=damage,
                                   emergency_activated=activated, resulting_trigger=trigger))
            pair = records[2*rnd:2*rnd+2]
            actions = [[event['action'] for event in rec['event'] if event['kind'] == 'action'] for rec in pair]
            assert normalized(engine.play_round(actions)) == pair
        assert trigger == case['early_triggered_round']
        assert engine.result == row['result']
        cases.append(dict(condition=condition, selected=case['selected'], checks=checks,
                          early_triggered_round=trigger, all_passed=True))
    assert all(digest(path) == sha for path, sha in inputs.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(), runtime_seconds=time.perf_counter()-begin,
        games=len(cases), checked_early_calls=sum(len(case['checks']) for case in cases),
        emergency_activations=sum(check['emergency_activated'] for case in cases for check in case['checks']),
        all_passed=True, cases=cases, input_sha256=inputs,
        scope='Public trigger logic independently reconstructed on recorded histories using original combat and engine replay. No hidden-current-action prediction is inferred.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({key: output[key] for key in ('time_utc','games','checked_early_calls','emergency_activations','all_passed')}))

if __name__ == '__main__':
    main()
