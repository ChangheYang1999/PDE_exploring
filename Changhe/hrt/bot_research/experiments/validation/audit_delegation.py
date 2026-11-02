"""Reconstruct handoff decisions from public states without the policy wrapper."""
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
    roster = [RosterEntry(e['id'], e['type'], e['bought_round'], e['expires_after_round'])
              for e in snapshot['roster']]
    return PlayerState(snapshot['name'], snapshot['hp'], snapshot['gold'], snapshot['n_factories'],
        [Building(b['x'], b['y'], b['type']) for b in snapshot['buildings']], roster,
        max((e.id for e in roster), default=-1) + 1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--campaign', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    begin = time.perf_counter()
    root = Path(args.campaign)
    inputs = {}
    def digest(p):
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    def read(p):
        inputs[str(p)] = digest(p)
        return json.loads(p.read_text())
    for p in static_closure({'bot_research.experiments.validation.audit_delegation'}):
        inputs[str(p)] = digest(p)
    histories = read(Path(str(root)+'-histories.json'))
    assert histories['exact_counter_policy_reproduction']
    freeze = read(root/'freeze.json')
    for p, sha in freeze['source_sha256'].items():
        assert digest(p) == sha, p
        inputs[p] = sha
    cases = []
    for case in histories['cases']:
        row = read(Path(case['result']))
        checked_row(case['result'], inputs)
        side = 1-row['condition']['candidate_side']
        spec = row['condition']['opponent_spec']
        assert spec.partition(':')[0] == 'bot_research.bots.counters.delegated_defense'
        parameters = {k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}
        assert set(parameters) <= {'mode', 'delegate'}
        delegate = parameters.get('delegate', 'econ20')
        trace = case['delegation_trace']
        assert len(trace) == row['rounds']
        records = [json.loads(line) for line in Path(row['replay_path']).read_text().splitlines()]
        cfg = balanced_config()
        engine = Engine(cfg, tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs']))) == records[:2]
        started = None
        projections = 0
        for rnd in range(1,row['rounds']+1):
            obs = engine.observation(side)
            damage, reason = None, None
            if delegate != 'template' and case['selected'] == 'early' and rnd >= 5:
                if started is None:
                    if obs['players'][side]['hp'] > obs['players'][1-side]['hp']:
                        reason = 'positive_hp_lead'
                    else:
                        defender, attacker = state(obs['players'][side]), state(obs['players'][1-side])
                        grid = cfg.globals
                        route = shortest_path(grid.width,grid.height,[(b.x,b.y) for b in defender.buildings],
                                              tuple(grid.spawn),tuple(grid.base))
                        assert route is not None
                        damage = simulate_map(attacker,defender,route,rnd,cfg).damage
                        projections += 1
                        if damage > 0:
                            reason = 'visible_damage'
                    if reason is not None:
                        started = rnd
            expected = dict(round=rnd,delegate=delegate if started is not None else None,
                            started=started,trigger=reason,visible_incoming=damage)
            assert trace[rnd-1] == expected, (case['result'],rnd,trace[rnd-1],expected)
            pair = records[2*rnd:2*rnd+2]
            actions = [[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            assert normalized(engine.play_round(actions)) == pair
        assert engine.result == row['result']
        assert started == case['delegate_started']
        cases.append(dict(result=case['result'],delegate=delegate,selected=case['selected'],
                          started=started,checked_calls=row['rounds'],combat_projections=projections))
    assert all(digest(p)==h for p,h in inputs.items())
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-begin,
               all_passed=True,games=len(cases),checked_calls=sum(c['checked_calls'] for c in cases),
               handoffs=sum(c['started'] is not None for c in cases),cases=cases,input_sha256=inputs,
               scope='Independent public handoff reconstruction and original-engine replay; no controller or trigger-helper import.')
    atomic_json(args.output,out,exclusive=True)
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','input_sha256')}))


if __name__ == '__main__':
    main()
