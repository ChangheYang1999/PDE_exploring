"""Audit catalogue matches and compare complete paired trajectories."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def canonical_replay(path, side):
    records=[json.loads(line) for line in Path(path).read_text().splitlines()]
    for row in records:
        row.pop('match',None)
        row['player']^=side
        row['snapshot']['name']='counter' if row['player']==0 else 'opponent'
        for event in row['event']:
            event.pop('order',None)
        if 'result' in row and row['result']['winner'] is not None:
            row['result']['winner']^=side
    records.sort(key=lambda row:(row['round'],row['player']))
    return hashlib.sha256(json.dumps(records,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',nargs='+',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--expected',type=int)
    args=parser.parse_args()
    rows=[]
    for source in args.inputs:
        for line in Path(source).read_text().splitlines():
            row=json.loads(line)
            row['input_file']=source
            rows.append(row)
    invalid=[]
    cases=[]
    counts=defaultdict(Counter)
    paired=defaultdict(list)
    for row in rows:
        c=row['condition']
        issues=[key for key in ('bot_errors','rejected_actions') if any(row[key])]
        issues.extend(key for key in ('source_changed_during_match','trace_missing_rounds',
            'true_model_missing_rounds','true_forecast_mismatch_rounds','catalogue_reset_rounds',
            'forecast_model_errors') if row.get(key))
        if not row.get('source_sha256_at_end'):
            issues.append('missing_end_source_attestation')
        if issues:
            invalid.append({'input':row['input_file'],'condition':c,'issues':issues})
            continue
        side=c['counter_side']
        trace_hash=canonical_replay(row['replay_path'],side)
        case={'input':row['input_file'],'condition':c,'outcome':row['counter_outcome'],
              'hp_counter_first':row['hp'][::1 if side==0 else -1],
              'rounds':row['rounds'],'runtime_seconds':row['runtime_seconds'],
              'first_singleton_round':row['first_singleton_round'],
              'trace_rounds':len(row['identification_trace']),
              'canonical_replay_sha256':trace_hash,
              'replay_path':row['replay_path']}
        cases.append(case)
        counts[c['mode']][row['counter_outcome']]+=1
        key=json.dumps({k:v for k,v in c.items() if k not in ('counter_side','index')},sort_keys=True)
        paired[key].append(case)
    pairs=[]
    for key,group in paired.items():
        sides=sorted(x['condition']['counter_side'] for x in group)
        pairs.append({'condition':json.loads(key),'sides':sides,
                      'exactly_two_assignments':sides==[0,1],
                      'same_complete_trajectory':len({x['canonical_replay_sha256'] for x in group})==1})
    output={'time_utc':datetime.now(timezone.utc).isoformat(),
            'input_sha256':{source:hashlib.sha256(Path(source).read_bytes()).hexdigest() for source in args.inputs},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'rows':len(rows),'expected':args.expected,'invalid':invalid,
            'outcomes_by_mode':{key:dict(value) for key,value in counts.items()},
            'distinct_canonical_trajectories':len({x['canonical_replay_sha256'] for x in cases}),
            'pairs':pairs,'cases':cases,
            'interpretation':'Fixed development catalogue, standard start. Paired deterministic assignments check symmetry and are not independent samples. Informed and adaptive openings may differ, so their comparison is a whole-policy ablation.'}
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({key:output[key] for key in ('rows','invalid','outcomes_by_mode','distinct_canonical_trajectories')}))
    assert not invalid
    assert all(x['exactly_two_assignments'] and x['same_complete_trajectory'] for x in pairs)
    if args.expected is not None:
        assert len(rows)==args.expected


if __name__=='__main__':
    main()
