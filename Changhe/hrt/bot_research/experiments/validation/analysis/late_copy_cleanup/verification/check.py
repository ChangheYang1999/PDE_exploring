"""Check a fully legal prefix and one last-tick cleanup counterexample."""
from copy import deepcopy
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from td_game.combat import combat_tick
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    started = time.perf_counter()
    engine = Engine(balanced_config(), ('factory_attacker', 'one_splash_defender'))
    records = []
    for rnd in range(1, 10):
        gold = engine.players[0].gold
        if rnd < 9:
            a = [{'op':'buy_factory'}] * (gold // engine.config.globals.factory_cost)
        else:
            a = [{'op':'buy_minion','type':'tier1'}] * 250
        b = [{'op':'build_turret','type':'splash','x':1,'y':1}] if rnd == 1 else []
        rr = engine.play_round([a, b])
        assert all(e['accepted'] for r in rr for e in r['event'] if e['kind'] == 'action')
        assert engine.result is None
        records.extend(rr)
    path = engine.path(1)
    exposure = sum(10 for x,y in path[:-1] if max(abs(x-1), abs(y-1)) == 1)
    combat = next(e for e in records[-2]['event'] if e['kind'] == 'combat')
    assert len(path)-1 == 22 and exposure == 30
    assert combat['spawned'] == 250 and combat['killed'] == 249 and combat['cleared'] == 1
    assert combat['damage_dealt'] == 0 and engine.players[1].hp == 800
    living, totals = combat_tick(249, [], [engine.players[0].roster[-1]], path,
        deepcopy(engine.players[1]), engine.config)
    assert len(living) == 1 and living[0].hp == 10 and living[0].path_index == 0
    paths = set(static_closure({'td_game.combat','td_game.engine',
        'bot_research.experiments.validation.analysis.late_copy_cleanup.verification.check'}))
    paths.update(map(Path, ['configs/balanced.json','td_game/balanced.json',
        'bot_research/experiments/validation/analysis/late_copy_cleanup/PROOF.md']))
    out = dict(time_utc=datetime.now(timezone.utc).isoformat(),
        runtime_seconds=time.perf_counter()-started, all_passed=True,
        source_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)},
        route=path, full_route_exposure=exposure, records=records,
        final_combat=combat, last_tick_survivors=[asdict(e) for e in living],
        last_tick_totals=asdict(totals),
        scope='Legal nine-round original-engine prefix; rules counterexample, not a strength comparison.')
    dest='bot_research/experiments/validation/analysis/late_copy_cleanup/verification/result.json'
    atomic_json(dest, out, exclusive=True)
    print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed','final_combat','last_tick_survivors')}))


if __name__ == '__main__':
    main()
