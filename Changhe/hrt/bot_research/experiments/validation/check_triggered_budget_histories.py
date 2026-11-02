"""Regenerate HP-triggered budget decisions and verify the public trigger."""
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse, hashlib, json, time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.triggered_budget_handoff import TriggeredBudgetHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--campaign',required=True)
    parser.add_argument('--expected',required=True,type=int);parser.add_argument('--output',required=True)
    args=parser.parse_args();start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_triggered_budget_histories'})}
    root=Path(args.campaign)
    for p,h in json.loads((root/'freeze.json').read_text())['source_sha256'].items():
        assert digest(p)==h
        if p in hashes:assert hashes[p]==h
        hashes[p]=h
    hashes[str(root/'jobs.json')]=digest(root/'jobs.json');cases=[]
    for job in json.loads((root/'jobs.json').read_text()):
        condition=job['condition'];side=1-condition['candidate_side'];path=root/'results'/(job['id']+'.json')
        checked_row(str(path),hashes);row=json.loads(path.read_text())
        records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
        cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
        assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
        spec=condition['opponent_spec'];assert spec.partition(':')[0]=='bot_research.bots.counters.triggered_budget_handoff'
        params={k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}
        policy=TriggeredBudgetHandoff(**params);rounds=[];differences=[];first=None
        for rnd in range(1,row['rounds']+1):
            obs=engine.observation(side);saved=deepcopy(obs)
            ownhp=obs['players'][side]['hp'];enemyhp=obs['players'][1-side]['hp']
            if first is None and rnd>=policy.lead_from and ownhp>enemyhp+policy.lead_margin:first=rnd
            begin=time.perf_counter();fresh=policy.decide(obs);seconds=time.perf_counter()-begin
            assert obs==saved and policy.triggered_round==first
            own=player_from_snapshot(obs['players'][side])
            assert all(apply_action(own,a,rnd,cfg)['accepted'] for a in fresh)
            if first is not None:assert not any(a['op']=='buy_minion' for a in fresh)
            pair=records[2*rnd:2*rnd+2]
            actual=[[e['action'] for e in rec['event'] if e['kind']=='action'] for rec in pair]
            if fresh!=actual[side]:differences.append(rnd)
            assert normalized(engine.play_round(actual))==pair
            incoming=next(e['base_damage'] for e in pair[side]['event'] if e['kind']=='combat')
            rounds.append(dict(policy.trace[-1],decision_seconds=seconds,incoming_damage=incoming,
                               fresh_actions_agree=fresh==actual[side]))
        assert engine.result==row['result']
        cases.append(dict(condition=condition,result=str(path),rounds=rounds,differing_rounds=differences,
            first_switch=first,filtered_proposals=policy.filtered_proposals,replayed=True,
            observations_unchanged=True,fresh_actions_legal=True,no_post_handoff_minions=True))
        print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],
            differences=differences,first_switch=first)),flush=True)
    assert len(cases)==args.expected and all(digest(p)==h for p,h in hashes.items())
    output=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,cases=cases,exact_counter_policy_reproduction=all(not c['differing_rounds'] for c in cases),
        all_replayed=True,all_observations_unchanged=True,all_fresh_actions_legal=True,no_post_handoff_minions=True,
        all_public_triggers_verified=True,scope='Original-engine replay, exact public-trigger check and fresh controller regeneration. No other conditions inferred.')
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','runtime_seconds','exact_counter_policy_reproduction')}))

if __name__=='__main__':main()
