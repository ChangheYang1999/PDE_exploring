"""Select top development timing outcomes, then replay both assignments."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from bot_research.experiments.validation.search_timing_equivalence import run_case
from bot_research.experiments.validation.artifact_io import atomic_json


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--inputs',nargs='+',required=True)
    p.add_argument('--count',type=int,default=3)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    rows=[]
    for source in a.inputs:
        for line in Path(source).read_text().splitlines():
            row=json.loads(line)
            if row.get('evidence_type')=='deduced_identical_trajectory':
                continue
            if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match'] or row['forecast_mismatch_rounds']:
                continue
            row['screen_source']=source
            rows.append(row)
    def key(row):
        side=row['condition']['counter_side']
        hp=row['hp'][side]-row['hp'][1-side]
        return ({'W':2,'D':1,'L':0}[row['counter_outcome']],hp,-row['rounds'])
    selected=[]
    seen=set()
    for row in sorted(rows,key=key,reverse=True):
        # Equal complete replay hashes are the same screen behavior.
        if row['trajectory_sha256'] in seen:
            continue
        seen.add(row['trajectory_sha256'])
        selected.append(row)
        if len(selected)>=a.count:
            break
    root=Path(a.output).with_suffix('')
    root.mkdir(exist_ok=False)
    atomic_json(root/'selection.json',{'time_utc':datetime.now(timezone.utc).isoformat(),
        'criterion':'Outcome, raw final HP margin, earlier termination; skip duplicate screen trajectories.',
        'selected':[{'source':r['screen_source'],'condition':r['condition'],'hp':r['hp'],
                     'trajectory_sha256':r['trajectory_sha256']} for r in selected],
        'input_sha256':{s:hashlib.sha256(Path(s).read_bytes()).hexdigest() for s in a.inputs}},exclusive=True)
    started=time.perf_counter()
    with Path(a.output).open('x') as out:
        for i,screen in enumerate(selected):
            c=screen['condition']
            keywords={}
            if screen.get('model_family')=='frontier':
                from bot_research.bots.counters.known_frontier import KnownTiming, policy_factory
                keywords={'counter_type':KnownTiming,'target_factory':policy_factory}
            for side in (0,1):
                if time.perf_counter()-started>480:
                    raise RuntimeError('Confirmation batch exceeded its work budget; completed rows retained.')
                row=run_case(c['model'],c['model_parameters'],c['parameters'],side,
                             root/f'finalist{i}-side{side}.jsonl','paired development finalist',**keywords)
                row['screen_condition']=c
                row['screen_source']=screen['screen_source']
                row['selection_index']=i
                out.write(json.dumps(row,sort_keys=True)+'\n')
                out.flush()
                print(json.dumps({k:row[k] for k in ('condition','counter_outcome','hp','rounds','runtime_seconds')}),flush=True)


if __name__=='__main__':
    main()
