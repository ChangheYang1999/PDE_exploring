"""End-to-end frozen-source attestation using development fixtures only."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
from bot_research.experiments.validation.artifact_io import atomic_json, public_diagnostic
from bot_research.experiments.validation.final_validation import (
    archive_sources, drift, freeze_sources, read_result, summarize)
from bot_research.experiments.validation.source_closure import job_source_roots


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',required=True)
    args=parser.parse_args()
    directory=Path(args.output_dir)
    directory.mkdir(exist_ok=False)
    for name in ('jobs','results','replays'):
        (directory/name).mkdir()
    jobs=[]
    for side in (0,1):
        bots=[{'spec':'bot_research.experiments.validation.check_isolation:stateful_probe'},
              {'profile':{'roster':['tier1']}}]
        names=['stateful_probe','rush_t1']
        if side:
            bots.reverse()
            names.reverse()
        job={'id':f'fixture-side{side}','names':names,'bots':bots,
             'condition':{'candidate_side':side,'strength_score_eligible':True,
                          'initial_state':'standard','engine_seed':None,
                          'purpose':'runner fixture; no reserved opponents'},
             'replay_path':str(directory/'replays'/f'fixture-side{side}.jsonl')}
        jobs.append(job)
    roots=job_source_roots(jobs)
    frozen=freeze_sources(roots)
    archive_sources(frozen,directory)
    metadata={'candidate':'stateful_probe fixture','pool':'fixture',
              'source_sha256':frozen,'source_root_modules':roots,
              'interpretation':'Two assignment fixtures, not heldout evaluation.'}
    atomic_json(directory/'freeze.json',metadata,exclusive=True)
    results=[]
    for job in jobs:
        job_path=directory/'jobs'/(job['id']+'.json')
        result_path=directory/'results'/(job['id']+'.json')
        atomic_json(job_path,job,exclusive=True)
        command=[sys.executable,'-B','-m','bot_research.experiments.validation.isolated_match',
                 '--job',str(job_path),'--output',str(result_path)]
        process=subprocess.run(command,timeout=60,capture_output=True,text=True)
        if process.returncode:
            raise RuntimeError(public_diagnostic(process.stderr))
        result=read_result(result_path,job,frozen)
        assert not any(result['bot_errors']) and not any(result['rejected_actions'])
        assert not result['source_changed_during_match']
        assert not any(drift(frozen,roots).values())
        results.append(result)
    summary=summarize(directory,jobs,metadata)
    checks={'both_fresh_process_matches_valid':summary['all_completed_successfully'],
            'both_start_and_end_sources_attested':all(
                row['source_sha256'] and row['source_sha256_at_end'] for row in results),
            'source_freeze_unchanged':not any(drift(frozen,roots).values()),
            'assignment_outcomes_agree':results[0]['candidate_outcome']==results[1]['candidate_outcome'],
            'assignment_hp_agree':results[0]['hp']==list(reversed(results[1]['hp']))}
    output={'time_utc':datetime.now(timezone.utc).isoformat(),'checks':checks,
            'all_passed':all(checks.values()),'frozen_source_count':len(frozen),
            'summary':summary}
    atomic_json(directory/'checks.json',output,exclusive=True)
    print(json.dumps(output,sort_keys=True))
    assert output['all_passed']


if __name__=='__main__':
    main()
