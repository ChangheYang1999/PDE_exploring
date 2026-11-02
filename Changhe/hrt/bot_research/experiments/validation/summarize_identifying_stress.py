"""Summarize out-of-catalogue results without treating forecast failure as truth."""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',nargs='+',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--expected',type=int)
    args=parser.parse_args()
    cases=[]
    invalid=[]
    groups=defaultdict(list)
    for source in args.inputs:
        for line in Path(source).read_text().splitlines():
            row=json.loads(line)
            issues=[key for key in ('bot_errors','rejected_actions') if any(row[key])]
            issues.extend(key for key in ('source_changed_during_match','trace_missing_rounds') if row[key])
            if not row.get('source_sha256_at_end'):
                issues.append('missing_end_attestation')
            if issues:
                invalid.append({'input':source,'condition':row['condition'],'issues':issues})
                continue
            side=row['condition']['counter_side']
            case={'input':source,'condition':row['condition'],'outcome':row['counter_outcome'],
                  'hp_counter_first':row['hp'][::1 if side==0 else -1],'rounds':row['rounds'],
                  'runtime_seconds':row['runtime_seconds'],
                  'catalogue_reset_rounds':row['catalogue_reset_rounds'],
                  'no_matching_forecast_rounds':row['no_matching_forecast_rounds'],
                  'forecast_model_errors':row['forecast_model_errors'],
                  'canonical_replay_sha256':canonical_replay(row['replay_path'],side)}
            cases.append(case)
            key=json.dumps({k:v for k,v in row['condition'].items() if k not in ('index','counter_side')},sort_keys=True)
            groups[key].append(case)
    pairs=[]
    for key,group in groups.items():
        pairs.append({'condition':json.loads(key),'sides':sorted(x['condition']['counter_side'] for x in group),
                      'same_complete_trajectory':len({x['canonical_replay_sha256'] for x in group})==1})
    output={'time_utc':datetime.now(timezone.utc).isoformat(),
            'input_sha256':{source:hashlib.sha256(Path(source).read_bytes()).hexdigest() for source in args.inputs},
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'valid_matches':len(cases),'invalid':invalid,'expected':args.expected,
            'outcomes':dict(Counter(case['outcome'] for case in cases)),
            'distinct_canonical_trajectories':len({case['canonical_replay_sha256'] for case in cases}),
            'cases':cases,'pairs':pairs,
            'scope':'Eight declared development stress opponents; model forecasts may be wrong. Forecast exceptions are reported separately from actual policy errors. No reserved opponents.'}
    atomic_json(args.output,output,exclusive=True)
    print(json.dumps({key:output[key] for key in ('valid_matches','invalid','outcomes','distinct_canonical_trajectories')}))
    assert not invalid
    assert all(row['sides']==[0,1] and row['same_complete_trajectory'] for row in pairs)
    if args.expected is not None:
        assert len(cases)==args.expected


if __name__=='__main__':
    main()
