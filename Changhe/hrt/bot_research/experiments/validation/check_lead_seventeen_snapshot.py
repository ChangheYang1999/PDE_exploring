"""Check copied Lead17 actions against the original on unchanged-engine games.

Both policy instances receive separate copies of the same public history.
The original alone submits actions; the snapshot never reads that submission.
"""
from copy import deepcopy
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.lead.v17 import make as original
from bot_research.bots.counters.snapshots.lead_seventeen_001 import make as snapshot
from bot_research.bots.counters.budget_timing import make as counter
from bot_research.harness.scenarios import make_overrides
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',required=True)
    a=p.parse_args()
    declaration=Path('bot_research/experiments/validation/lead-seventeen-mid5-standard-001.json')
    manifest=json.loads(declaration.read_text())
    assert all(digest(f)==sha for f,sha in manifest['original_source_sha256'].items())
    params=dict(big_threat=100,gun_cap=120,poke_until=3,poke_reactive='turret',
                big_partial=True,r1_poke=3,attack_mode='adaptive',fortress_n=4,
                immune_attack=True,mid_until=5,foreign_policy='econ17')
    paths=set(static_closure({'bot_research.experiments.validation.check_lead_seventeen_snapshot'}))
    paths.update((declaration,Path('td_game/balanced.json'),Path('configs/balanced.json')))
    sources={str(f):digest(f) for f in paths}
    started=time.perf_counter()
    rows=[]
    for scenario in (None,'mirror:1:2'):
        for side in (0,1):
            e=Engine(balanced_config(),('check0','check1'))
            orig,copy=original(**params),snapshot(**params)
            enemy=counter(tier='tier3',attack_round=3,budget_fraction=0.5)
            equal=0
            overrides=make_overrides(scenario) if scenario else None
            while e.result is None:
                obs=e.observation(side)
                before=deepcopy(obs)
                sa=copy(deepcopy(obs))
                oa=orig(obs)
                assert obs==before and sa==oa
                equal+=1
                pair=[None,None]
                pair[side]=oa
                pair[1-side]=enemy(e.observation(1-side))
                if scenario:
                    for player in (0,1):
                        scripted=overrides[player](e.observation(player))
                        if scripted is not None:
                            pair[player]=scripted
                records=e.play_round(pair)
                assert all(ev['accepted'] for rec in records for ev in rec['event'] if ev['kind']=='action')
            rows.append(dict(scenario=scenario,side=side,matched_rounds=equal,
                hp_candidate_first=[e.players[side].hp,e.players[1-side].hp],
                original_switch_round=orig.switch_round,snapshot_switch_round=copy.switch_round,
                original_mid_rounds=orig.mid_rounds,snapshot_mid_rounds=copy.mid_rounds))
    assert all(digest(f)==sha for f,sha in sources.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-started,
             all_passed=True,cases=rows,source_sha256=sources,
             scope='Action equivalence on four reached histories, including a known call-through prefix; this is not an independent strength comparison.')
    atomic_json(a.output,out,exclusive=True)
    print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed','cases')}))


if __name__=='__main__':
    main()
