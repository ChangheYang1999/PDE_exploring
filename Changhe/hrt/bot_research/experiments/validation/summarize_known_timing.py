"""Summarize full timing screens, keeping deductions separate from played games."""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--inputs',nargs='+',required=True)
    p.add_argument('--output',required=True)
    p.add_argument('--expected',type=int)
    a=p.parse_args()
    rows=[]
    for source in a.inputs:
        for text in Path(source).read_text().splitlines():
            row=json.loads(text)
            row['input_file']=source
            rows.append(row)
    counts=Counter()
    invalid=[]
    played=[]
    deduced=[]
    conditions=[]
    for row in rows:
        derived=row.get('evidence_type')=='deduced_identical_trajectory'
        if not derived:
            issues=[name for name in ('bot_errors','rejected_actions') if any(row[name])]
            issues += [name for name in ('source_changed_during_match','forecast_mismatch_rounds') if row[name]]
            if issues:
                invalid.append({'input':row['input_file'],'condition':row['condition'],'issues':issues})
                continue
            played.append(row)
        else:
            deduced.append(row)
        counts[row['counter_outcome']]+=1
        side=row['condition']['counter_side']
        conditions.append({'input':row['input_file'],'condition':row['condition'],
            'evidence_type':'deduced_identical_trajectory' if derived else 'played_original_engine',
            'outcome':row['counter_outcome'],'hp_counter_first':row['hp'][::1 if side==0 else -1],
            'rounds':row['rounds'],'trajectory_sha256':row['trajectory_sha256']})
    result={'time_utc':datetime.now(timezone.utc).isoformat(),
            'input_sha256':{s:hashlib.sha256(Path(s).read_bytes()).hexdigest() for s in a.inputs},
            'rows':len(rows),'expected':a.expected,
            'coverage_count_matches':None if a.expected is None else len(rows)==a.expected,
            'valid_played_conditions':len(played),'deduced_conditions':len(deduced),
            'invalid_conditions':invalid,'outcomes':dict(counts),
            'distinct_raw_trajectory_hashes':len({r['trajectory_sha256'] for r in played+deduced}),
            'played_runtime_seconds':sum(r['runtime_seconds'] for r in played),
            'conditions':conditions,
            'interpretation':'A parameter grid, not independent random samples. Deductions are not new games. Identical timing baselines saved separately are not included in played count.'}
    atomic_json(a.output,result,exclusive=True)
    print(json.dumps({k:result[k] for k in result if k not in ('conditions','input_sha256')},sort_keys=True))
    assert not invalid
    if a.expected is not None:
        assert len(rows)==a.expected


if __name__=='__main__':
    main()
