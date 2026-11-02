"""Fresh-process development matrix with explicit manifests and frozen sources.

This runner never selects reserved opponents. All candidate and opponent
specifications are supplied explicitly in its development manifest.
"""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
import json
from pathlib import Path
import subprocess
import sys
import time
from bot_research.experiments.validation.artifact_io import atomic_json,public_diagnostic
from bot_research.experiments.validation.final_validation import (
    archive_sources,digest,execution_context,now,read_result)
from bot_research.experiments.validation.source_closure import static_closure


def summarize(directory,jobs,metadata):
    scores=defaultdict(Counter)
    valid=[]
    invalid=[]
    failures=[]
    for job in jobs:
        path=directory/'results'/(job['id']+'.json')
        failed=directory/'results'/(job['id']+'.failure.json')
        if failed.exists():
            failures.append(json.loads(failed.read_text()))
            continue
        if not path.exists():
            continue
        try:
            row=read_result(path,job,metadata['source_sha256'])
        except (ValueError,KeyError,TypeError,OSError) as error:
            failures.append({'job':job['id'],'error':public_diagnostic(str(error))})
            continue
        if any(row['bot_errors']) or any(row['rejected_actions']) or row['source_changed_during_match']:
            invalid.append(job['id'])
            continue
        scores[job['condition']['candidate_id']][row['candidate_outcome']]+=1
        valid.append(row)
    result={'time_utc':now(),'planned':len(jobs),'valid_completed':len(valid),
            'invalid':invalid,'failures':failures,'outcomes':{k:dict(v) for k,v in scores.items()},
            'complete':len(valid)+len(invalid)+len(failures)==len(jobs),
            'purpose':metadata['purpose'],
            'scope':'Explicit development conditions. Paired deterministic games are not independent random samples.'}
    atomic_json(directory/'summary.json',result)
    with (directory/'matches.jsonl').open('w') as stream:
        for row in valid:
            stream.write(json.dumps(row,sort_keys=True)+'\n')
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--manifest',required=True)
    parser.add_argument('--output-dir',required=True)
    parser.add_argument('--shard',type=int,default=0)
    parser.add_argument('--shards',type=int,default=1)
    parser.add_argument('--max-seconds',type=float,default=3600)
    parser.add_argument('--match-timeout',type=float,default=900)
    parser.add_argument('--resume',action='store_true')
    args=parser.parse_args()
    if not 0<args.max_seconds<=3600 or not 0<args.match_timeout<=900:
        parser.error('Detached batches allow at most 3600 seconds total and 900 seconds per match.')
    directory=Path(args.output_dir)
    manifest_path=Path(args.manifest)
    for path in (directory,manifest_path):
        if path.is_absolute() or '..' in path.parts or path.parts[:1]!=('bot_research',):
            parser.error('Use project-relative research paths.')
    if args.resume:
        metadata=json.loads((directory/'freeze.json').read_text())
        jobs=json.loads((directory/'jobs.json').read_text())
        if digest(manifest_path)!=metadata['manifest_sha256']:
            parser.error('Development manifest differs from the frozen campaign.')
    else:
        manifest=json.loads(manifest_path.read_text())
        directory.mkdir(parents=True,exist_ok=False)
        for name in ('jobs','results','replays'):
            (directory/name).mkdir()
        jobs=[]
        index=0
        for candidate in manifest['candidates']:
            for opponent in manifest['opponents']:
                for side in (0,1):
                    if index%args.shards==args.shard:
                        job_id=f'case{index:04d}'
                        bots=[{'spec':candidate['spec']},{'spec':opponent['spec']}]
                        names=[candidate['id'],opponent['id']]
                        if side:
                            bots.reverse()
                            names.reverse()
                        job={'id':job_id,'names':names,'bots':bots,
                             'replay_path':str(directory/'replays'/(job_id+'.jsonl')),
                             'condition':{'candidate_side':side,'candidate_id':candidate['id'],
                                'candidate_spec':candidate['spec'],'opponent_id':opponent['id'],
                                'opponent_spec':opponent['spec'],'initial_state':'standard',
                                'engine_seed':None,'purpose':manifest['purpose'],
                                'strength_score_eligible':True,'pool':'development'}}
                        jobs.append(job)
                    index+=1
        roots={'bot_research.experiments.validation.run_background_development',
               'bot_research.experiments.validation.isolated_match'}
        roots.update(bot['spec'].partition(':')[0] for job in jobs for bot in job['bots'])
        paths=set(static_closure(roots))|{manifest_path,Path('td_game/balanced.json'),Path('configs/balanced.json')}
        frozen={str(path):digest(path) for path in sorted(paths)}
        metadata={'started_utc':now(),'manifest_sha256':digest(manifest_path),
                  'purpose':manifest['purpose'],'source_sha256':frozen,'source_roots':sorted(roots),
                  'runtime':execution_context(),'match_timeout':args.match_timeout,
                  'shard':args.shard,'shards':args.shards}
        archive_sources(frozen,directory)
        atomic_json(directory/'freeze.json',metadata,exclusive=True)
        atomic_json(directory/'jobs.json',jobs,exclusive=True)
        for job in jobs:
            atomic_json(directory/'jobs'/(job['id']+'.json'),job,exclusive=True)
    def check_sources():
        changed=[name for name,value in metadata['source_sha256'].items()
                 if not Path(name).is_file() or digest(name)!=value]
        if changed:
            raise RuntimeError('Changed frozen development inputs: '+repr(changed))
    check_sources()
    started=time.perf_counter()
    for job in jobs:
        path=directory/'results'/(job['id']+'.json')
        failed=directory/'results'/(job['id']+'.failure.json')
        if path.exists() or failed.exists():
            continue
        remaining=args.max_seconds-(time.perf_counter()-started)
        if remaining<metadata['match_timeout']:
            break
        check_sources()
        timeout=metadata['match_timeout']
        command=[sys.executable,'-B','-m','bot_research.experiments.validation.isolated_match',
                 '--job',str(directory/'jobs'/(job['id']+'.json')),'--output',str(path)]
        failure=None
        try:
            result=subprocess.run(command,capture_output=True,text=True,timeout=timeout,check=False)
            if result.returncode:
                failure={'job':job['id'],'time_utc':now(),'returncode':result.returncode,
                         'stderr':public_diagnostic(result.stderr)[-12000:]}
            else:
                read_result(path,job,metadata['source_sha256'])
        except subprocess.TimeoutExpired:
            failure={'job':job['id'],'time_utc':now(),'timeout_seconds':timeout}
        except (ValueError,KeyError,TypeError,OSError) as error:
            failure={'job':job['id'],'time_utc':now(),'error':public_diagnostic(str(error))}
        if failure:
            atomic_json(failed,failure,exclusive=True)
        check_sources()
        summary=summarize(directory,jobs,metadata)
        print(json.dumps({'finished':job['id'],'outcomes':summary['outcomes'],
                          'failures':len(summary['failures']),'invalid':summary['invalid']}),flush=True)
    print(json.dumps(summarize(directory,jobs,metadata)),flush=True)


if __name__=='__main__':
    main()
