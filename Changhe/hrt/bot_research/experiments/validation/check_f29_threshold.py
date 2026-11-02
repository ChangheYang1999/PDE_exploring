"""Check frozen F29 threshold returns against archived original-combat minima."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.harness.gamekit import Rules, route
from bot_research.bots.defense.frozen.v29.fortress import _kill_threshold
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    start=time.perf_counter()
    manifest_path=Path('bot_research/experiments/validation/append-monotonicity-001.json')
    reference_path=Path('bot_research/runs/validation/append-monotonicity-001.json')
    manifest=json.loads(manifest_path.read_text())
    reference=json.loads(reference_path.read_text())
    assert reference['all_passed']
    assert reference['input_sha256'][str(manifest_path)]==digest(manifest_path)
    inputs={str(manifest_path):digest(manifest_path),str(reference_path):digest(reference_path)}
    sources={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_f29_threshold'})}
    sources['td_game/balanced.json']=digest('td_game/balanced.json')
    rules=Rules.from_observation(Engine(balanced_config(),('a','b')).observation(0))
    maps={m['id']:m['buildings'] for m in manifest['maps']}
    cases=[]
    for expected in reference['threshold_cases']:
        if expected['n_max']==0:
            continue
        buildings=maps[expected['map_id']]
        path=route((b['x'],b['y']) for b in buildings)
        actual=_kill_threshold(path,buildings,rules,expected['hp'],n_max=expected['n_max'])
        assert actual==expected['exact_minimum'],'F29 differs from original-combat enumeration.'
        cases.append({k:expected[k] for k in ('map_id','hp','n_max','exact_minimum')} | {'f29_returned':actual})
    assert all(digest(p)==h for p,h in {**inputs,**sources}.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,input_sha256=inputs,source_sha256=sources,cases=cases,
        scope='Positive bounds1,6,17 only, four fixed maps and four HP values. Exact minima were independently computed using original combat in the pinned reference. F28 remains frozen with the earlier boundary bug; F29 is checked separately. No full-game effect is inferred.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps(dict(all_passed=True,cases=len(cases),runtime_seconds=result['runtime_seconds'])))


if __name__=='__main__':
    main()
