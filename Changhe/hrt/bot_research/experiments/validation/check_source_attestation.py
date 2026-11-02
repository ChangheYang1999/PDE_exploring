"""Fault injection for final-validation source attestations; no game outcomes."""
from __future__ import annotations
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from bot_research.experiments.validation.final_validation import read_result
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output-dir',required=True)
    a=p.parse_args()
    root=Path(a.output_dir)
    root.mkdir(exist_ok=False)
    job={'condition':{'candidate_side':0}}
    frozen={'bot_research/bots/counters/fixture.py':'expected'}
    base={'condition':job['condition'],'candidate_outcome':'W','result':{'winner':0},
          'bot_errors':[[],[]],'rejected_actions':[{},{}],'source_changed_during_match':[],
          'source_sha256':dict(frozen),'source_sha256_at_end':dict(frozen)}
    variants={'valid':deepcopy(base)}
    for field in ('source_sha256','source_sha256_at_end'):
        missing=deepcopy(base)
        missing.pop(field)
        variants['missing_'+field]=missing
        changed=deepcopy(base)
        changed[field]['bot_research/bots/counters/fixture.py']='different'
        variants['changed_'+field]=changed
        unknown=deepcopy(base)
        unknown[field]['bot_research/bots/counters/unfrozen.py']='unexpected'
        variants['unknown_'+field]=unknown
    checks={}
    for label,row in variants.items():
        path=root/(label+'.json')
        atomic_json(path,row,exclusive=True)
        try:
            read_result(path,job,frozen)
        except ValueError:
            accepted=False
        else:
            accepted=True
        checks[label]=accepted==(label=='valid')
    result={'time_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,
            'all_passed':all(checks.values()),
            'interpretation':'Synthetic source-attestation faults only. No heldout games.'}
    atomic_json(root/'checks.json',result,exclusive=True)
    print(json.dumps(result,sort_keys=True))
    assert result['all_passed']


if __name__=='__main__':
    main()
