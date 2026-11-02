"""A fresh match plus public-policy hypothesis diagnostics after completion."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.evaluate import evaluate
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--job',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    job=json.loads(Path(args.job).read_text())
    if job.get('prefixes'):
        raise ValueError('This diagnostic runner is for standard development matches only.')
    bots=[resolve(x) for x in job['bots']]
    side=job['condition']['candidate_side']
    owner=getattr(bots[side].decide,'__self__',None)
    result=evaluate(tuple(job['names']),bots=bots,replay_path=job['replay_path'],condition=job['condition'])
    winner=result['result']['winner']
    result['candidate_outcome']='D' if winner is None else ('W' if winner==side else 'L')
    trace=getattr(owner,'trace',None)
    if not isinstance(trace,list):
        raise ValueError('Candidate did not expose its own hypothesis trace.')
    result['identification_trace']=trace
    result['trace_missing_rounds']=sorted(set(range(1,result['rounds']+1))-{t['round'] for t in trace})
    result['catalogue_reset_rounds']=[t['round'] for t in trace if t['catalogue_reset']]
    result['forecast_model_errors']=[{'round':t['round'],**error} for t in trace for error in t['forecast_errors']]
    expected=job['condition']['opponent_id']
    records=[json.loads(line) for line in Path(job['replay_path']).read_text().splitlines()]
    actions={r['round']:[e['action'] for e in r['event'] if e['kind']=='action']
             for r in records if r['round']>0 and r['player']==1-side}
    result['declared_target_model']=expected
    result['target_model_present_rounds']=[t['round'] for t in trace if expected in t['active']]
    result['target_forecast_mismatch_rounds']=[t['round'] for t in trace
        if expected in t['predicted_actions'] and t['predicted_actions'][expected]!=actions[t['round']]]
    result['no_matching_forecast_rounds']=[t['round'] for t in trace
        if not any(proposal==actions[t['round']] for proposal in t['predicted_actions'].values())]
    atomic_json(args.output,result,exclusive=True)


if __name__=='__main__':
    main()
