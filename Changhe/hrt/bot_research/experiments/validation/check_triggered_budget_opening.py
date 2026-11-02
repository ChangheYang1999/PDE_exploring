"""Check public HP switching and legality before full transfer games."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.triggered_budget_handoff import TriggeredBudgetHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
    start=time.perf_counter();digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    paths=static_closure({'bot_research.experiments.validation.check_triggered_budget_opening'})
    hashes={str(p):digest(p) for p in paths};cases=[]
    for tag in 'abc':
        path=Path(f'bot_research/experiments/validation/triggered-budget-{tag}001.json')
        m=json.loads(path.read_text());hashes[str(path)]=digest(path)
        for name,h in m['input_sha256'].items():
            assert digest(name)==h
            if name in hashes:assert hashes[name]==h
            hashes[name]=h
        for target in m['candidates']:
            for counter in m['opponents']:
                params={k:json.loads(v[0]) for k,v in parse_qs(counter['spec'].partition('?')[2]).items()}
                for side in (0,1):
                    policy=TriggeredBudgetHandoff(**params);other=resolve(target).decide
                    policies=[other,policy.decide] if side==0 else [policy.decide,other]
                    cfg=balanced_config();engine=Engine(cfg,('prefix0','prefix1'));rounds=[];first=None
                    for rnd in range(1,9):
                        obs=[engine.observation(s) for s in (0,1)];saved=deepcopy(obs)
                        ownhp=obs[1-side]['players'][1-side]['hp'];enemyhp=obs[side]['players'][side]['hp']
                        if first is None and rnd>=policy.lead_from and ownhp>enemyhp+policy.lead_margin:first=rnd
                        acts=[policies[s](obs[s]) for s in (0,1)];assert obs==saved
                        assert policy.triggered_round==first
                        if first is not None:assert not any(a['op']=='buy_minion' for a in acts[1-side])
                        for s in (0,1):
                            state=player_from_snapshot(obs[s]['players'][s])
                            assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in acts[s])
                        rec=engine.play_round(acts)
                        assert all(e['accepted'] for r in rec for e in r['event'] if e['kind']=='action')
                        rounds.append(dict(round=rnd,trace=policy.trace[-1],hp=[x.hp for x in engine.players],actions=acts))
                        if engine.result is not None:break
                    if target['id']=='P5TNUBM' and params['strike_count']==1:assert first==6
                    cases.append(dict(target=target['id'],counter=counter['id'],target_side=side,
                        first_switch=first,rounds=rounds,observations_unchanged=True,all_actions_legal=True))
                    print(json.dumps(dict(target=target['id'],counter=counter['id'],side=side,first_switch=first)),flush=True)
    assert len(cases)==48
    assert all(digest(p)==h for p,h in hashes.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,cases=cases,all_passed=True,scope='Eight-round components only, not complete strength comparisons.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','all_passed')}))

if __name__=='__main__':main()
