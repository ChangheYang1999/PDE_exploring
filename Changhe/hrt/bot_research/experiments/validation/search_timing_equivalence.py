"""Reuse a timing baseline only after a complete action-equality certificate.

See analysis/timing_equivalence/PROOF.md. Derived conditions are explicitly
separated from newly played original-engine matches in the output.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import time
from bot_research.bots.counters.known_policy import KnownTiming, policy_factory
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.isolated_match import CallableBot
from bot_research.experiments.validation.source_closure import static_closure


def hash_value(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def observations_and_actions(row, side):
    records=[json.loads(s) for s in Path(row['replay_path']).read_text().splitlines()]
    by_round={}
    actions={}
    for record in records:
        rnd=record['round']
        by_round.setdefault(rnd,{})[record['player']]=record['snapshot']
        if record['player']==side and rnd>0:
            actions[rnd]=[event['action'] for event in record['event'] if event['kind']=='action']
    observations={rnd:{'round':rnd,'player':side,'rules':row['rules'],
                       'players':[by_round[rnd-1][i] for i in (0,1)]}
                  for rnd in actions}
    return observations,actions


def run_case(model, model_parameters, parameters, side, replay, purpose,
             counter_type=KnownTiming, target_factory=policy_factory):
    counter=counter_type(model=model,model_parameters=model_parameters,**parameters)
    target=CallableBot(target_factory(model,model_parameters))
    bots,names=[counter,target],('known_timing',model)
    if side:
        bots.reverse()
        names=tuple(reversed(names))
    row=evaluate(names,bots=bots,replay_path=str(replay),condition={
        'counter_side':side,'model':model,'model_parameters':model_parameters,
        'parameters':parameters,'initial_state':'standard','engine_seed':None,'purpose':purpose})
    row['counter_outcome']='D' if row['result']['winner'] is None else ('W' if row['result']['winner']==side else 'L')
    row['forecast_trace']=counter.trace
    _,enemy_actions=observations_and_actions(row,1-side)
    row['forecast_mismatch_rounds']=[t['round'] for t in counter.trace
                                   if t['predicted_actions']!=enemy_actions[t['round']]]
    if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match'] or row['forecast_mismatch_rounds']:
        raise ValueError('Invalid source, action or forecast in authoritative timing match.')
    return row


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--model',required=True)
    p.add_argument('--family',choices=('known','frontier'),default='known')
    p.add_argument('--model-parameters',type=json.loads,default={})
    p.add_argument('--rounds',type=int,nargs='+',default=list(range(1,13)))
    p.add_argument('--tiers',nargs='+',default=['tier1','tier2','tier3','tier4','tier5'])
    p.add_argument('--shares',type=float,nargs='+',default=[0.25,0.5,1.0])
    p.add_argument('--caps',type=int,nargs='+',default=[200])
    p.add_argument('--side',type=int,choices=(0,1),default=0)
    p.add_argument('--start',type=int,default=0)
    p.add_argument('--shard',type=int,default=0)
    p.add_argument('--shards',type=int,default=1)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    counter_type,target_factory=KnownTiming,policy_factory
    if a.family=='frontier':
        from bot_research.bots.counters.known_frontier import KnownTiming as counter_type
        from bot_research.bots.counters.known_frontier import policy_factory as target_factory
    frozen={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in static_closure([
        'bot_research.experiments.validation.search_timing_equivalence'])}
    root=Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    started=time.perf_counter()
    baseline=run_case(a.model,a.model_parameters,{'attack_round':0},a.side,root/'baseline.jsonl',
                      'played no-purchase baseline for timing equivalence',counter_type,target_factory)
    baseline['experiment_source_sha256']=frozen
    (root/'baseline.json').write_text(json.dumps(baseline,sort_keys=True)+'\n')
    observations,actions=observations_and_actions(baseline,a.side)
    with Path(a.output).open('x') as out:
        for index,(rnd,tier,share,cap) in enumerate(itertools.product(a.rounds,a.tiers,a.shares,a.caps)):
            if index<a.start or index%a.shards!=a.shard:
                continue
            if time.perf_counter()-started>480:
                print(json.dumps({'stopped_before_index':index,'reason':'480-second bound'}),flush=True)
                return
            changed=[name for name,digest in frozen.items()
                     if hashlib.sha256(Path(name).read_bytes()).hexdigest()!=digest]
            if changed:
                raise ValueError(f'Source changed since baseline: {changed}')
            parameters={'attack_round':rnd,'tier':tier,'attack_share':share,'count_cap':cap}
            counter=counter_type(model=a.model,model_parameters=a.model_parameters,**parameters)
            proposal=counter.decide(observations[rnd]) if rnd in observations else None
            same=rnd not in observations or proposal==actions[rnd]
            if same:
                row={key:baseline[key] for key in ('counter_outcome','hp','rounds','result','trajectory_sha256')}
                row.update({'condition':{'index':index,'counter_side':a.side,'model':a.model,
                            'model_parameters':a.model_parameters,'parameters':parameters},
                            'evidence_type':'deduced_identical_trajectory',
                            'baseline_result':str(root/'baseline.json'),
                            'equality_certificate':{'round_reached':rnd in observations,
                              'observation_sha256':hash_value(observations[rnd]) if rnd in observations else None,
                              'submitted_actions_sha256':hash_value(proposal) if proposal is not None else None,
                              'full_ordered_action_lists_equal':True}})
            else:
                row=run_case(a.model,a.model_parameters,parameters,a.side,root/f'case{index:04d}.jsonl',
                             'played non-equivalent timing candidate; no reserved holdout',counter_type,target_factory)
                row['condition']['index']=index
                row['evidence_type']='played_original_engine'
            row['model_family']=a.family
            row['experiment_source_reference']=str(root/'baseline.json')
            out.write(json.dumps(row,sort_keys=True)+'\n')
            out.flush()
            print(json.dumps({key:row[key] for key in ('condition','evidence_type','counter_outcome','hp','rounds')}),flush=True)


if __name__=='__main__':
    main()
