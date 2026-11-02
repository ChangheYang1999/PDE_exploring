"""Original-engine prefixes for stateful identification and its known-model control."""
from copy import deepcopy
from datetime import datetime,timezone
import argparse
import hashlib
import json
from pathlib import Path
import time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.stateful_catalogue import StatefulCatalogue, CATALOGUE, BEST_FACTORY
from bot_research.bots.counters.free_forecast import FreeForecast
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.audit_stateful_catalogue import audit_trace, EXPECTED
from urllib.parse import urlencode


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    start=time.perf_counter()
    sources=set(static_closure({'bot_research.experiments.validation.check_stateful_catalogue'}))
    sources.add(Path('td_game/balanced.json'))
    source_hashes={str(p):digest(p) for p in sources}
    cases=[]
    mutation_rejections=0
    for name in [*CATALOGUE,'idle']:
        for side in (0,1):
            counter=StatefulCatalogue()
            enemy=(lambda observation: []) if name=='idle' else CATALOGUE[name][0](**CATALOGUE[name][1])
            engine=Engine(balanced_config(),('component0','component1'))
            traces=[]
            all_records=json.loads(json.dumps(engine.initial_records(('component0','component1'))))
            previous=None
            for rnd in range(1,9):
                if engine.result is not None:break
                own=engine.observation(side)
                before=deepcopy(own)
                acts=counter.decide(own)
                assert own==before
                other=enemy(engine.observation(1-side))
                trace=counter.trace[-1]
                if name in CATALOGUE:
                    assert name in trace['active']
                    assert trace['predictions'][name]['actions']==other
                if previous is not None:
                    observed=purchase_signature(own['players'][1-side],rnd-1)
                    assert trace['active']==[n for n in previous['active'] if previous['predictions'][n]['signature']==observed]
                if name=='idle' and rnd>=2:
                    assert trace['fallback'] and not trace['active']
                pair=[None,None];pair[side]=acts;pair[1-side]=other
                records=engine.play_round(pair)
                assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
                all_records.extend(json.loads(json.dumps(records)))
                traces.append(trace)
                previous=trace
            if name=='idle':
                spec='td_bots.protocol:idle'
            else:
                mod,params=EXPECTED[name]
                spec=mod+':@make?'+urlencode({k:json.dumps(v) for k,v in params.items()})
            row=json.loads(json.dumps(dict(condition=dict(candidate_side=side,opponent_spec=spec),catalogue_ids=counter.ids,catalogue_trace=traces,rules=engine.config.to_dict(),rounds=engine.round)))
            audit=audit_trace(row,all_records)
            for defect in ('signature','calls'):
                corrupted=deepcopy(row)
                first=corrupted['catalogue_trace'][0]
                member=first['active'][0]
                if defect=='signature':first['predictions'][member]['signature'][0]+=1
                else:first['call_counts'][member]+=1
                try:audit_trace(corrupted,all_records)
                except ValueError:mutation_rejections+=1
                else:raise AssertionError('Trace mutation escaped the audit.')
            cases.append(dict(target=name,side=side,traces=traces,audit=audit))
            print(json.dumps(dict(target=name,side=side,rounds=len(traces),last_active=counter.active)),flush=True)
    controls=[]
    for side in (0,1):
        counter=StatefulCatalogue(catalogue_ids=['best_v9b'])
        control=FreeForecast(model_spec=BEST_FACTORY,attack_round=3,tier='tier3',attack_share=1.0,count_cap=1000)
        enemy=CATALOGUE['best_v9b'][0]()
        engine=Engine(balanced_config(),('control0','control1'))
        for rnd in range(1,9):
            if engine.result is not None:break
            obs=engine.observation(side)
            acts=counter.decide(deepcopy(obs))
            assert acts==control.decide(deepcopy(obs))
            pair=[None,None];pair[side]=acts;pair[1-side]=enemy(engine.observation(1-side))
            records=engine.play_round(pair)
            assert all(e['accepted'] for r in records for e in r['event'] if e['kind']=='action')
        controls.append(dict(side=side,rounds=engine.round,identical_actions=True))
    changed=[p for p,h in source_hashes.items() if digest(p)!=h]
    assert not changed
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
                source_sha256=source_hashes,source_changed_during_run=changed,all_passed=True,
                cases=cases,singleton_controls=controls,mutation_rejections=mutation_rejections,
                scope='Eight prefixes of three catalogue members and idle, plus two singleton-control prefixes. Checks true-model retention, exact true forecasts, monotone elimination, visible fallback, legal actions and observation immutability. No full-game strength claim.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps(dict(all_passed=True,runtime_seconds=output['runtime_seconds'])),flush=True)


if __name__=='__main__':main()
