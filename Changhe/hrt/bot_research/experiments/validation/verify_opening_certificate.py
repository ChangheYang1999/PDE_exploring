"""Check every affordable ordered opening with the unchanged Engine."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.evaluate import source_hashes
from bot_research.experiments.validation.artifact_io import atomic_json


def rosters(budget, costs, prefix=()):
    yield prefix
    for tier, cost in sorted(costs.items()):
        if cost <= budget:
            yield from rosters(budget-cost, costs, prefix+(tier,))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', required=True)
    p.add_argument('--input', default='bot_research/experiments/validation/analysis/opening_certificate/certificate.json')
    args = p.parse_args()
    path = Path(args.input)
    inputs = json.loads(path.read_text())
    cfg = balanced_config()
    assert cfg.globals.initial_gold == inputs['initial_gold'] == 100
    costs = {t: m.cost for t, m in cfg.minions.items()}
    sequences = list(rosters(100, costs))
    assert len(sequences) == len(set(sequences)) == 27
    rows = []
    output = Path(args.output)
    root = output.with_suffix('')
    root.mkdir(exist_ok=False)
    started = time.perf_counter()
    source_start = source_hashes()
    for index, seq in enumerate(sequences):
        shots = sum((cfg.minions[t].hp + cfg.turrets['gun2'].damage-1)//cfg.turrets['gun2'].damage for t in seq)
        assert shots <= 9
        for side in (0, 1):
            engine = Engine(cfg, ('opening_certificate', 'attacker') if side == 0 else ('attacker', 'opening_certificate'))
            records = engine.initial_records(('certificate' if side == 0 else 'attacker', 'attacker' if side == 0 else 'certificate'))
            attack = [{'op': 'buy_minion', 'type': t} for t in seq]
            submissions = [inputs['actions'], attack] if side == 0 else [attack, inputs['actions']]
            settled = engine.play_round(submissions)
            assert all(e['accepted'] for r in settled for e in r['event'] if e['kind']=='action')
            assert engine.players[side].hp == cfg.globals.initial_hp
            route = engine.path(side)
            covered = [i for i,(x,y) in enumerate(route[:-1]) if (x-3)**2+(y-2)**2 <= 9]
            assert covered == list(range(1,10))
            incoming = next(e for e in settled[side]['event'] if e['kind']=='combat')
            assert incoming['base_damage'] == incoming['incoming_hits'] == 0
            outgoing = next(e for e in settled[1-side]['event'] if e['kind']=='combat')
            assert outgoing['spawned'] == outgoing['killed'] == len(seq)
            assert outgoing['cleared'] == 0
            replay = root / f'case{index:02d}-side{side}.jsonl'
            with replay.open('x') as f:
                for r in records+settled:
                    f.write(json.dumps(r,sort_keys=True)+'\n')
            rows.append({'sequence':seq,'cost':sum(costs[t] for t in seq), 'shots':shots,
                         'defender_side':side, 'hp':engine.players[side].hp,
                         'incoming_combat':incoming, 'replay':str(replay)})
    sources_end = source_hashes()
    changed = [k for k,v in source_start.items() if sources_end.get(k)!=v]
    assert not changed
    result = {'time_utc':datetime.now(timezone.utc).isoformat(),'input':str(path),
              'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
              'source_sha256':source_start,'source_changed_during_check':changed,
              'ordered_sequences':len(sequences),'assignment_checks':len(rows),
              'route':route,'coverage':covered,'defense_cost':89,'max_required_hits':max(r['shots'] for r in rows),
              'runtime_seconds':time.perf_counter()-started,'checks':rows,'status':'PASS'}
    atomic_json(output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','ordered_sequences','assignment_checks','defense_cost','max_required_hits','status')}))


if __name__ == '__main__':
    main()
