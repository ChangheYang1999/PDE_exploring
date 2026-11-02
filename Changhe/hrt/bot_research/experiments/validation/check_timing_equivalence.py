"""Cross-check action-equality deductions against complete already-played games."""
from __future__ import annotations
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.bots.counters.known_policy import KnownTiming
from bot_research.experiments.validation.search_timing_equivalence import observations_and_actions, hash_value
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure


def normalize(path):
    rows=[json.loads(s) for s in Path(path).read_text().splitlines()]
    for row in rows:
        row.pop('match',None)
        row['snapshot']['name']=str(row['player'])
    return rows


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--inputs',nargs='+',required=True)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    counter_sources={str(p):hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in static_closure(['bot_research.bots.counters.known_policy'])}
    unrecorded_sources=set()
    groups=defaultdict(list)
    for name in a.inputs:
        for line in Path(name).read_text().splitlines():
            row=json.loads(line)
            recorded={**row['source_sha256'],**row.get('source_sha256_at_end',{})}
            for source,digest in counter_sources.items():
                if source in recorded:
                    assert recorded[source]==digest, source
                else:
                    unrecorded_sources.add(source)
            c=row['condition']
            key=(c['model'],json.dumps(c['model_parameters'],sort_keys=True),c['counter_side'])
            groups[key].append((name,row))
    checks=[]
    for (model,model_json,side),group in groups.items():
        baselines=[(name,r) for name,r in group if all(t['attack_count']==0 for t in r['forecast_trace'])]
        if not baselines:
            raise ValueError(f'No zero-purchase baseline for {model} {model_json}')
        baseline_name,baseline=baselines[0]
        assert not any(baseline['bot_errors']) and not any(baseline['rejected_actions'])
        assert not baseline['source_changed_during_match'] and not baseline['forecast_mismatch_rounds']
        obs,actions=observations_and_actions(baseline,side)
        baseline_records=normalize(baseline['replay_path'])
        for name,row in group:
            assert not any(row['bot_errors']) and not any(row['rejected_actions'])
            assert not row['source_changed_during_match'] and not row['forecast_mismatch_rounds']
            parameters=row['condition']['parameters']
            assert parameters.get('defense_first',False) is False
            counter=KnownTiming(model=model,model_parameters=json.loads(model_json),**parameters)
            rnd=parameters['attack_round']
            proposal=counter.decide(obs[rnd]) if rnd in obs else None
            same=rnd not in obs or proposal==actions[rnd]
            full_same=normalize(row['replay_path'])==baseline_records
            assert same==full_same
            checks.append({'input':name,'baseline':baseline_name,
                           'condition':row['condition'],'action_equality':same,
                           'complete_trajectory_equality':full_same,
                           'observation_sha256':hash_value(obs[rnd]) if rnd in obs else None})
    output={'time_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,
            'conditions':len(checks),'equal':sum(c['action_equality'] for c in checks),
            'different':sum(not c['action_equality'] for c in checks),'all_passed':True,
            'counter_source_sha256':counter_sources,
            'legacy_sources_not_attested':sorted(unrecorded_sources),
            'source_check_scope':'Every recorded counter dependency matches current bytes. Static but unrecorded lazy imports are listed; legacy rows lack end attestations.',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':{name:hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in a.inputs},
            'interpretation':'Checks existing played games; does not add independent match samples.'}
    atomic_json(a.output,output,exclusive=True)
    print(json.dumps({k:output[k] for k in ('time_utc','conditions','equal','different','all_passed')}))


if __name__=='__main__':
    main()
