"""Check completed timing matches, forecast coverage, and paired full replays."""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',nargs='+',required=True)
    parser.add_argument('--expected',type=int,required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    cases=[]
    invalid=[]
    groups=defaultdict(list)
    for name in args.inputs:
        for line in Path(name).read_text().splitlines():
            row=json.loads(line)
            c=row['condition']
            issues=[key for key in ('bot_errors','rejected_actions') if any(row[key])]
            issues.extend(key for key in ('source_changed_during_match','forecast_mismatch_rounds') if row[key])
            if not row.get('source_sha256_at_end'):
                issues.append('missing_end_source_attestation')
            if {x['round'] for x in row['forecast_trace']}!=set(range(1,row['rounds']+1)):
                issues.append('forecast_trace_missing_rounds')
            if issues:
                invalid.append({'source':name,'condition':c,'issues':issues})
                continue
            side=c['counter_side']
            case={'source':name,'condition':c,'outcome':row['counter_outcome'],
                  'hp_counter_first':row['hp'][::1 if side==0 else -1],'rounds':row['rounds'],
                  'runtime_seconds':row['runtime_seconds'],'replay_path':row['replay_path'],
                  'canonical_replay_sha256':canonical_replay(row['replay_path'],side)}
            cases.append(case)
            key=json.dumps({k:v for k,v in c.items() if k not in ('counter_side','index')},sort_keys=True)
            groups[key].append(case)
    pairs=[{'condition':json.loads(key),
            'sides':sorted(c['condition']['counter_side'] for c in group),
            'same_complete_trajectory':len({c['canonical_replay_sha256'] for c in group})==1}
           for key,group in groups.items()]
    result={'time_utc':now(),'input_sha256':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in args.inputs},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'expected':args.expected,'valid_cases':len(cases),'invalid':invalid,
            'outcomes':dict(Counter(c['outcome'] for c in cases)),
            'distinct_canonical_trajectories':len({c['canonical_replay_sha256'] for c in cases}),
            'pairs':pairs,'cases':cases,
            'scope':'Completed paired development conditions. Forecasts checked on every reached round; paired deterministic trajectories are not independent samples.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('valid_cases','invalid','outcomes','distinct_canonical_trajectories')}))
    assert len(cases)==args.expected and not invalid
    assert all(p['sides']==[0,1] and p['same_complete_trajectory'] for p in pairs)


if __name__=='__main__':
    main()
