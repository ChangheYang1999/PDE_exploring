"""Check pinned timing prefixes before full games, preserving complete actions."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse, hashlib, json, time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.public_roster_selector import PublicRosterSelector
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--manifest',required=True);p.add_argument('--output',required=True);args=p.parse_args()
    start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    m=json.loads(Path(args.manifest).read_text())
    hashes={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_public_selector_opening'})}
    hashes[args.manifest]=digest(args.manifest)
    for path,sha in m['input_sha256'].items():
        assert digest(path)==sha
        if path in hashes:assert hashes[path]==sha
        hashes[path]=sha
    cases=[]
    for target in m['candidates']:
        for counter in m['opponents']:
            params={k:json.loads(v[0]) for k,v in parse_qs(counter['spec'].partition('?')[2]).items()}
            for side in (0,1):
                policy=PublicRosterSelector(**params);other=resolve(target).decide
                policies=[other,policy.decide] if side==0 else [policy.decide,other]
                cfg=balanced_config();engine=Engine(cfg,('prefix0','prefix1'));rounds=[];first=None
                for rnd in range(1,9):
                    obs=[engine.observation(s) for s in (0,1)];saved=deepcopy(obs)
                    count=sum(e['type']=='tier1' and e['bought_round']==1 for e in obs[1-side]['players'][side]['roster'])
                    if first is None and rnd>=2:first='early' if count>=policy.threshold else 'growth'
                    acts=[policies[s](obs[s]) for s in (0,1)];assert obs==saved
                    assert policy.selected==(first if policy.mode=='adaptive' else policy.mode)
                    for s in (0,1):
                        state=player_from_snapshot(obs[s]['players'][s])
                        assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in acts[s])
                    rec=engine.play_round(acts)
                    assert all(e['accepted'] for r in rec for e in r['event'] if e['kind']=='action')
                    rounds.append(dict(round=rnd,counter_start_gold=obs[1-side]['players'][1-side]['gold'],
                        trace=policy.trace[-1],hp=[x.hp for x in engine.players],actions=acts))
                    if engine.result is not None:break
                cases.append(dict(target=target['id'],counter=counter['id'],target_side=side,selected=policy.selected,
                    rounds=rounds,observations_unchanged=True,all_actions_legal=True,early_filtered_proposals=policy.early.filtered_proposals,growth_filtered_proposals=policy.growth.rejected_proposals))
                print(json.dumps(dict(target=target['id'],counter=counter['id'],side=side,selected=policy.selected)),flush=True)
    assert len(cases)==m['expected_conditions']
    assert all(digest(p)==h for p,h in hashes.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,cases=cases,all_passed=True,scope='Eight-round component checks only; no full-game strength inferred.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
