"""Audit completed development shards and expose every paired condition."""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.final_validation import now,read_result
from bot_research.experiments.validation.summarize_identifying import canonical_replay


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inputs',nargs='+',required=True)
    parser.add_argument('--output',required=True)
    parser.add_argument('--expected',type=int)
    args=parser.parse_args()
    cases=[]
    failures=[]
    pending=[]
    manifests=set()
    input_hashes={}
    for name in args.inputs:
        directory=Path(name)
        metadata=json.loads((directory/'freeze.json').read_text())
        jobs=json.loads((directory/'jobs.json').read_text())
        manifests.add(metadata['manifest_sha256'])
        for filename in ('freeze.json','jobs.json'):
            p=directory/filename
            input_hashes[str(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
        for job in jobs:
            path=directory/'results'/(job['id']+'.json')
            failed=directory/'results'/(job['id']+'.failure.json')
            if failed.exists():
                failures.append({'directory':name,'condition':job['condition'],
                                 'failure':json.loads(failed.read_text())})
                continue
            if not path.exists():
                pending.append({'directory':name,'job':job['id']})
                continue
            input_hashes[str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
            try:
                row=read_result(path,job,metadata['source_sha256'])
            except (ValueError,KeyError,TypeError,OSError) as error:
                failures.append({'directory':name,'condition':job['condition'],
                                 'error_type':type(error).__name__})
                continue
            issues=[key for key in ('bot_errors','rejected_actions') if any(row[key])]
            if row['source_changed_during_match']:
                issues.append('source_changed_during_match')
            if issues:
                failures.append({'directory':name,'condition':job['condition'],'issues':issues})
                continue
            side=job['condition']['candidate_side']
            cases.append({'condition':job['condition'],'outcome':row['candidate_outcome'],
                          'hp_candidate_first':row['hp'][::1 if side==0 else -1],
                          'rounds':row['rounds'],'runtime_seconds':row['runtime_seconds'],
                          'replay_path':row['replay_path'],'result_path':str(path),
                          'canonical_replay_sha256':canonical_replay(row['replay_path'],side)})
    groups=defaultdict(list)
    counts=defaultdict(Counter)
    for case in cases:
        c=case['condition']
        groups[(c['candidate_id'],c['opponent_id'])].append(case)
        counts[c['candidate_id']][case['outcome']]+=1
    pairs=[]
    for (candidate,opponent),group in sorted(groups.items()):
        sides=sorted(case['condition']['candidate_side'] for case in group)
        pairs.append({'candidate':candidate,'opponent':opponent,'sides':sides,
                      'exactly_two_assignments':sides==[0,1],
                      'same_complete_trajectory':len({c['canonical_replay_sha256'] for c in group})==1,
                      'outcomes':[c['outcome'] for c in group],
                      'hp_candidate_first':[c['hp_candidate_first'] for c in group]})
    result={'time_utc':now(),'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':input_hashes,'manifest_sha256':sorted(manifests),
            'valid_cases':len(cases),'expected_cases':args.expected,'failures':failures,'pending':pending,
            'outcomes':{k:dict(v) for k,v in counts.items()},'pairs':pairs,'cases':cases,
            'distinct_canonical_trajectories':len({c['canonical_replay_sha256'] for c in cases}),
            'scope':'Explicit development conditions, not reserved validation. Paired deterministic assignments are not independent samples.'}
    atomic_json(args.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in ('valid_cases','expected_cases','failures','pending','outcomes','distinct_canonical_trajectories')}))
    assert len(manifests)==1,'Input shards must use the same manifest.'
    assert not failures and not pending
    assert all(p['exactly_two_assignments'] for p in pairs)
    if args.expected is not None:
        assert len(cases)==args.expected


if __name__=='__main__':
    main()
