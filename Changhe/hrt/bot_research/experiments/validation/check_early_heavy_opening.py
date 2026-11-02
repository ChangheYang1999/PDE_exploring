"""Verify the actual five-round early-heavy opening on the original engine."""
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse
import hashlib
import json
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.early_heavy_handoff import EarlyHeavyHandoff
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    started = time.perf_counter()
    digest = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
    declaration = Path('bot_research/experiments/validation/retargeted-forecast-001.json')
    m = json.loads(declaration.read_text())
    target = m['candidates'][0]['spec']
    parameters = {k: json.loads(v[0]) for k, v in parse_qs(m['opponents'][0]['spec'].partition('?')[2]).items()}
    parameters['deadline'] = 6
    paths = set(static_closure({'bot_research.experiments.validation.check_early_heavy_opening',
                               'bot_research.experiments.lead.v30'}))
    paths |= {Path(p) for p in m['input_sha256'] if '/data/' in p}
    paths |= {declaration, Path('td_game/balanced.json'), Path('configs/balanced.json')}
    before = {str(p): digest(p) for p in sorted(paths)}
    cases = []
    for count in (0, 1):
        for side in (0, 1):
            cfg = balanced_config()
            counter = EarlyHeavyHandoff(strike_count=count, **parameters)
            target_policy = resolve(dict(spec=target))
            names = ['P5TNUBM', 'early_heavy']
            policies = [target_policy.decide, counter.decide]
            if side:
                policies.reverse()
                names.reverse()
            engine = Engine(cfg, tuple(names))
            rounds = []
            for rnd in range(1, 6):
                observations = [engine.observation(s) for s in (0, 1)]
                originals = deepcopy(observations)
                actions = [policies[s](observations[s]) for s in (0, 1)]
                assert observations == originals
                assert counter.trace[-1]['predicted_actions'] == actions[side]
                records = engine.play_round(actions)
                assert all(e['accepted'] for rec in records for e in rec['event'] if e['kind'] == 'action')
                rounds.append(records)
            own = engine.players[side]
            route = engine.path(side)
            splash = sum(cfg.turrets[b.type].damage
                for b in own.buildings if b.type == 'splash'
                for x, y in route[:-1] if max(abs(b.x-x), abs(b.y-y)) == 1)
            assert all(b.type in ('wall', 'splash') for b in own.buildings)
            assert splash < cfg.minions['tier4'].hp
            assert own.hp == 800 - 60 * count
            assert engine.players[1-side].hp == 755
            assert counter.strike_trace[0]['accepted'] == count
            cases.append(dict(strike_count=count, target_side=side, target_hp=own.hp,
                counter_hp=engine.players[1-side].hp, target_splash_exposure=splash,
                target_route_length=len(route)-1, observations_unchanged=True,
                predictions_exact=True, all_actions_accepted=True,
                strike_trace=counter.strike_trace,
                filtered_parent_proposals=counter.filtered_parent_proposals,
                records=rounds))
    assert all(digest(p) == h for p, h in before.items())
    output = dict(time_utc=datetime.now(timezone.utc).isoformat(),
                  runtime_seconds=time.perf_counter()-started, input_sha256=before,
                  all_passed=True, cases=cases,
                  scope='Original-engine opening component through round five, not a full-game result.')
    atomic_json(args.output, output, exclusive=True)
    print(json.dumps({k: output[k] for k in ('time_utc', 'runtime_seconds', 'all_passed')}))


if __name__ == '__main__':
    main()
