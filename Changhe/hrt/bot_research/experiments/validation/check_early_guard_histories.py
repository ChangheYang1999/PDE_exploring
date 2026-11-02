"""Fresh guard-prefix calls and independent full replay of recorded games."""
from collections import Counter
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,hashlib,json,time
from td_game.actions import apply_action
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.bots.counters.early_guard_handoff import EarlyGuardHandoff
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.compare_recorded_controls import checked_row
from bot_research.experiments.validation.replay_audit import normalized
from bot_research.experiments.validation.source_closure import static_closure


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--campaigns',nargs='+',required=True)
    parser.add_argument('--candidate-ids',nargs='+')
    parser.add_argument('--opponent-ids',nargs='+')
    parser.add_argument('--through-round',type=int,default=6,choices=(6,50))
    parser.add_argument('--expected',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    start=time.perf_counter()
    digest=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
    hashes={str(p):digest(p) for p in static_closure({'bot_research.experiments.validation.check_early_guard_histories'})}
    cases=[]
    for directory in args.campaigns:
        root=Path(directory)
        for p,h in json.loads((root/'freeze.json').read_text())['source_sha256'].items():
            assert digest(p)==h
            if p in hashes:assert hashes[p]==h
            hashes[p]=h
        jobs=root/'jobs.json';hashes[str(jobs)]=digest(jobs)
        for job in json.loads(jobs.read_text()):
            c=job['condition']
            if args.candidate_ids and c['candidate_id'] not in args.candidate_ids:continue
            if args.opponent_ids and c['opponent_id'] not in args.opponent_ids:continue
            file=root/'results'/(job['id']+'.json');checked_row(str(file),hashes)
            row=json.loads(file.read_text());records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
            target=c['candidate_side'];side=1-target;cfg=balanced_config();engine=Engine(cfg,tuple(row['bot_specs']))
            assert normalized(engine.initial_records(tuple(row['bot_specs'])))==records[:2]
            spec=c['opponent_spec'];assert spec.partition(':')[0]=='bot_research.bots.counters.early_guard_handoff'
            params={k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}
            policy=EarlyGuardHandoff(**params);differences=[];details=[];checked_rounds=[]
            for rnd in range(1,row['rounds']+1):
                obs=engine.observation(side)
                pair=records[2*rnd:2*rnd+2]
                actual=[[e['action'] for e in record['event'] if e['kind']=='action'] for record in pair]
                if rnd<=args.through_round:
                    saved=deepcopy(obs);fresh=policy.decide(obs);assert obs==saved
                    state=player_from_snapshot(obs['players'][side])
                    assert all(apply_action(state,a,rnd,cfg)['accepted'] for a in fresh)
                    if fresh!=actual[side]:differences.append(dict(round=rnd,fresh=fresh,recorded=actual[side]))
                    if rnd>=policy.handoff_round:assert not any(a['op']=='buy_minion' for a in fresh)
                    checked_rounds.append(rnd)
                assert normalized(engine.play_round(actual))==pair
                if rnd in (6,7,8):
                    def actions_summary(acts):
                        return dict(Counter(a['op']+(':'+a['type'] if 'type' in a else '') for a in acts))
                    details.append(dict(round=rnd,target_actions=actions_summary(actual[target]),
                        counter_actions=actions_summary(actual[side]),
                        target_hp=pair[target]['snapshot']['hp'],counter_hp=pair[side]['snapshot']['hp'],
                        counter_factories_before=obs['players'][side]['n_factories'],
                        target_factories_before=obs['players'][target]['n_factories'],
                        counter_incoming_damage=next(e['base_damage'] for e in pair[side]['event'] if e['kind']=='combat'),
                        target_incoming_damage=next(e['base_damage'] for e in pair[target]['event'] if e['kind']=='combat')))
            assert engine.result==row['result']
            extension=[t for t in policy.trace if t['round']==6]
            assert len(extension)==1
            cases.append(dict(condition=c,result=str(file),replayed=True,observations_unchanged=True,
                fresh_actions_legal=True,checked_rounds=checked_rounds,extension=extension[0],
                filtered_proposals=policy.filtered_proposals,policy_action_differences=differences,diagnostic_rounds=details))
            print(json.dumps(dict(time_utc=datetime.now(timezone.utc).isoformat(),finished=job['id'],
                candidate=c['candidate_id'],opponent=c['opponent_id'],differences=len(differences),
                extension_complete=extension[0]['extension_complete'])),flush=True)
    assert len(cases)==args.expected
    assert all(digest(p)==h for p,h in hashes.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        input_sha256=hashes,cases=cases,all_replayed=True,all_observations_unchanged=True,
        all_fresh_actions_legal=True,through_round=args.through_round,
        exact_policy_reproduction=all(not c['policy_action_differences'] for c in cases),
        all_extensions_complete=all(c['extension']['extension_complete'] for c in cases),
        scope='Fresh counter-policy calls only through the declared round, on recorded observations; full original-engine replay. '
              'Filtered excess factory proposals are retained. These histories are not new strength samples.')
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('time_utc','runtime_seconds','exact_policy_reproduction','all_extensions_complete')}))

if __name__=='__main__':main()
